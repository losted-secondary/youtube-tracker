from datetime import datetime, timezone
import sys
import types
import unittest

# descobrir so precisa do HttpError; nao exige o SDK instalado pra rodar o teste.
if "googleapiclient.errors" not in sys.modules:
    errors = types.ModuleType("googleapiclient.errors")
    errors.HttpError = type("HttpError", (Exception,), {})
    sys.modules.setdefault("googleapiclient", types.ModuleType("googleapiclient"))
    sys.modules["googleapiclient.errors"] = errors

import descobrir

NOW = datetime(2026, 10, 11, 12, 0, tzinfo=timezone.utc)


def hit(vid, channel_id, title="Canal X"):
    return {"id": {"videoId": vid},
            "snippet": {"channelId": channel_id, "channelTitle": title,
                        "publishedAt": "2026-10-08T15:00:00Z"}}


class FakeYoutube:
    def __init__(self, search_pages, views):
        self.search_pages = search_pages
        self.views = views
        self.search_calls = []
        self._next = None

    def search(self):
        self._kind = "search"
        return self

    def videos(self):
        self._kind = "videos"
        return self

    def list(self, **kw):
        if self._kind == "search":
            self.search_calls.append(kw)
            self._next = self.search_pages.get((kw["q"], kw.get("pageToken")), {"items": []})
        else:
            self._next = {"items": [{"id": i, "statistics": {"viewCount": str(self.views[i])}}
                                    for i in kw["id"].split(",") if i in self.views]}
        return self

    def execute(self):
        return self._next


class DescobrirTest(unittest.TestCase):
    def test_filtra_canal_principal_proprio_conhecido_e_poucas_views(self):
        pages = {
            ("manhwa recap", None): {"items": [
                hit("aaaaaaaaaaa", "UCnovo", "Canal Novo"),
                hit("bbbbbbbbbbb", "UCprincipal"),
                hit("ccccccccccc", "UCUnLH9qyXBI8ijs9Kmbt9Ng"),  # Juicy
                hit("ddddddddddd", "UCnovo"),
                hit("eeeeeeeeeee", "UCnovo"),
            ], "nextPageToken": "p2"},
            ("manhwa recap", "p2"): {"items": [hit("fffffffffff", "UCoutro", "Outro")]},
            # mesmo video em duas buscas so pode entrar uma vez
            ("manhua recap", None): {"items": [hit("aaaaaaaaaaa", "UCnovo", "Canal Novo")]},
        }
        views = {"aaaaaaaaaaa": 250_000, "ddddddddddd": 99_999,
                 "eeeeeeeeeee": 500_000, "fffffffffff": 100_000}
        yt = FakeYoutube(pages, views)
        found = descobrir.find(yt, {"UCprincipal"}, {"eeeeeeeeeee"}, NOW)
        self.assertEqual(sorted(v["id"] for v in found), ["aaaaaaaaaaa", "fffffffffff"])
        a = next(v for v in found if v["id"] == "aaaaaaaaaaa")
        self.assertEqual(a["channel"], "Canal Novo")
        self.assertEqual(a["published"], datetime(2026, 10, 8, 15, 0, tzinfo=timezone.utc))
        self.assertEqual(yt.search_calls[0]["publishedAfter"], "2026-10-04T12:00:00Z")
        self.assertEqual(yt.search_calls[0]["order"], "viewCount")

    def test_main_channel_ids_e_agenda(self):
        self.assertEqual(descobrir.main_channel_ids({"x": "UUabc", "y": "PLzzz"}), {"UCabc"})
        self.assertTrue(descobrir.should_run(NOW, True))
        self.assertFalse(descobrir.should_run(NOW, False))
        self.assertFalse(descobrir.should_run(NOW.replace(hour=13), True))


if __name__ == "__main__":
    unittest.main()
