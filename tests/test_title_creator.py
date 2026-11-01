import json
from datetime import date
from threading import Thread
from http.server import ThreadingHTTPServer

import pytest
import requests

from title_creator import core, server


def raw(ident, views, **kwargs):
    return {"link": "https://youtu.be/" + ident, "viewers": views, "canal": "Channel", "data_postado": "01/10/2026 - 10:30", **kwargs}


def test_threshold_dedup_dates_and_comparison():
    data = [raw("abcdefghij0", "200.000"), raw("abcdefghij1", "200.001"), raw("abcdefghij1", "210.000")]
    data += [raw(f"abcdefghij{i}", "100.000") for i in range(2, 8)]
    rows = core.prepare_rows(data, date(2026, 11, 1))
    assert len(rows) == 8
    assert rows[0]["group"] == "control"
    assert rows[1]["group"] == "winner"
    assert rows[1]["views"] == 210000
    assert rows[1]["peer_ratio"] == 2.1
    assert rows[1]["peer_count"] == 7
    assert rows[1]["age_days"] == 31


def test_no_comparison_when_insufficient_peers_or_unknown_date():
    rows = core.prepare_rows([raw("abcdefghij0", "300.000"), raw("abcdefghij1", "500.000", data_postado="unknown")])
    assert all(row["peer_ratio"] == "" for row in rows)
    assert rows[1]["age_days"] is None


@pytest.mark.parametrize("url", ["https://evil.test/watch?v=abcdefghij0", "https://youtube.com.evil.test/watch?v=abcdefghij0", "https://youtu.be/not-an-id"])
def test_invalid_video_urls(url):
    assert core.video_id(url) is None


def test_csv_roundtrip(tmp_path):
    rows = [{"id": "abcdefghij0", "title": 'Título com "aspas", vírgula e ação', "views": 300000}]
    path = tmp_path / "library.csv"
    core.save_library(rows, path)
    assert core.read_library(path)[0]["title"] == rows[0]["title"]


@pytest.mark.parametrize("changes", [{"story": "curto"}, {"story": []}, {"count": 11}, {"count": True}, {"count": "8"}, {"language": "x"}, {"constraints": "x" * 2001}])
def test_bad_input(changes):
    with pytest.raises(core.AppError):
        core.validate_input({"story": "Uma história suficientemente longa para o teste.", **changes})


def valid_result():
    return {"story_reading": "Resumo", "cautions": [], "suggestions": [{"title": f"Título {i}", "angle": "poder", "why": "estrutura", "story_evidence": "fato", "reference_ids": ["abcdefghij0"]} for i in range(5)]}


def winner():
    return {"abcdefghij0": {"title": "A real title", "channel": "Channel", "views": "300000"}}


def test_unknown_references_duplicate_or_long_titles_are_rejected():
    result = valid_result()
    result["suggestions"][0]["reference_ids"] = ["invented"]
    with pytest.raises(core.AppError):
        core.validate_result(result, winner(), 5)
    result = valid_result()
    result["suggestions"][1]["title"] = result["suggestions"][0]["title"]
    with pytest.raises(core.AppError):
        core.validate_result(result, winner(), 5)
    result = valid_result()
    result["suggestions"][0]["title"] = "a" * 101
    with pytest.raises(core.AppError):
        core.validate_result(result, winner(), 5)


def test_references_are_resolved_on_server():
    result = core.validate_result(valid_result(), winner(), 5)
    assert result["suggestions"][0]["references"][0]["url"] == "https://www.youtube.com/watch?v=abcdefghij0"
    assert result["model"] == "gpt-6-astra"


def test_generation_preserves_model_and_never_returns_key(monkeypatch):
    monkeypatch.setattr(core, "api_key", lambda: "test-secret")
    monkeypatch.setattr(core, "read_library", lambda: [{"id": "abcdefghij0", "group": "winner", **winner()["abcdefghij0"]}])
    def post(url, **kwargs):
        assert url == "https://api.openai.com/v1/responses"
        assert kwargs["json"]["model"] == "gpt-6-astra"
        assert kwargs["json"]["store"] is False
        assert "test-secret" not in json.dumps(kwargs["json"])
        class Response:
            ok = True
            def json(self):
                return {"status": "completed", "output": [{"type": "message", "content": [{"type": "output_text", "text": json.dumps(valid_result())}]}]}
        return Response()
    monkeypatch.setattr(core.requests, "post", post)
    result = core.generate({"story": "Um curandeiro descobre que pode restaurar armas antigas.", "count": 5})
    assert "test-secret" not in json.dumps(result)


def test_sync_preserves_library_on_bad_sheet(monkeypatch, tmp_path):
    path = tmp_path / "library.csv"
    core.save_library([{"id": "abcdefghij0", "title": "previous"}], path)
    original = path.read_bytes()
    class Response:
        content = b"<html>Login required</html>"
        def raise_for_status(self):
            pass
    monkeypatch.setattr(core.requests, "get", lambda *a, **kw: Response())
    def forbidden_save(*args, **kwargs):
        pytest.fail("Invalid source must not overwrite the library")
    monkeypatch.setattr(core, "save_library", forbidden_save)
    with pytest.raises(core.AppError):
        core.sync_library()
    assert path.read_bytes() == original


def test_server_boundaries(monkeypatch):
    monkeypatch.setattr(server, "api_key", lambda: "test-secret")
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{httpd.server_port}"
    try:
        assert requests.get(base + "/").status_code == 200
        assert requests.get(base + "/../core.py").status_code == 404
        assert requests.get(base + "/data/library.csv").status_code == 404
        assert requests.get(base + "/api/status", headers={"Host": "evil.test"}).status_code == 403
        assert requests.post(base + "/api/generate", json={}).status_code == 403
        assert requests.post(base + "/api/generate", json={}, headers={"X-Session-Token": server.TOKEN, "Origin": "https://evil.test"}).status_code == 403
        status = requests.get(base + "/api/status")
        assert "test-secret" not in status.text
        assert status.json()["token"] == server.TOKEN
    finally:
        httpd.shutdown()
        httpd.server_close()
