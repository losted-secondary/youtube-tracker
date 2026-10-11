"""Coleta pública para investigate.js. Não edita Sheets nem usa API de IA."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")


def get_video_id(value):
    if VIDEO_ID.fullmatch(value):
        return value
    match = re.search(r"(?:youtu\.be/|youtube\.com/watch\?[^\s]*?v=)([\w-]{11})(?:[?&#/]|$)", value)
    if not match:
        raise ValueError("Informe um ID de 11 caracteres ou link youtube.com/watch / youtu.be.")
    return match.group(1)


class Logger:
    def debug(self, message):
        pass

    def warning(self, message):
        print("Aviso yt-dlp: " + message, file=sys.stderr)

    def error(self, message):
        # Não imprimir URLs assinadas/headers em logs.
        print("Falha yt-dlp na coleta; tente abrir o vídeo no navegador.", file=sys.stderr)


def collect(vid, out_dir, frames=True):
    import requests
    import yt_dlp
    errors = []
    opts = {
        "quiet": True, "no_warnings": True, "skip_download": True,
        "logger": Logger(), "getcomments": True,
        "socket_timeout": 20, "retries": 1, "extractor_retries": 1,
        "extractor_args": {"youtube": {"max_comments": ["120"], "comment_sort": ["top"]}},
    }
    data = yt_dlp.YoutubeDL(opts).extract_info("https://www.youtube.com/watch?v=" + vid, download=False)
    result = {
        "video_id": vid, "url": "https://www.youtube.com/watch?v=" + vid,
        "title": data.get("title", ""), "description": data.get("description", ""),
        "channel": data.get("channel", ""), "published": data.get("upload_date"),
        "comment_count": data.get("comment_count"),
        "comments": [{"text": c.get("text", ""), "author": c.get("author", ""),
                      "is_owner": c.get("author_is_uploader", False),
                      "id": c.get("id"), "parent": c.get("parent")}
                     for c in data.get("comments", [])],
        "transcript": "", "frames": [], "errors": errors,
    }
    result["comments_sampled"] = len(result["comments"])
    tracks = data.get("automatic_captions", {})
    subtitles = data.get("subtitles", {})
    available = subtitles.get("en", []) or tracks.get("en-orig", []) or tracks.get("en", [])
    track = next((t for t in available if t.get("ext") == "json3"), None)
    if track:
        try:
            response = requests.get(track["url"], timeout=20)
            response.raise_for_status()
            result["transcript"] = " ".join(
                "".join(s.get("utf8", "") for s in event.get("segs", [])).strip()
                for event in response.json().get("events", [])
                if event.get("tStartMs", 0) < 180000
            ).strip()
        except (requests.RequestException, ValueError):
            errors.append("Legendas não puderam ser lidas; ouvir o começo no navegador.")
    else:
        errors.append("Não encontradas legendas em inglês; tentar outro idioma ou ouvir o vídeo.")
    if frames:
        preview = next((f for f in data.get("formats", []) if f.get("format_id") == "sb0"), None)
        if preview and preview.get("fragments"):
            try:
                response = requests.get(preview["fragments"][0]["url"], timeout=20)
                response.raise_for_status()
                target = out_dir / (vid + "-preview.jpg")
                target.write_bytes(response.content)
                result["preview"] = target.name
            except requests.RequestException:
                errors.append("Imagens de prévia não disponíveis.")
        ffmpeg = shutil.which("ffmpeg")
        formats = [f for f in data.get("formats", []) if f.get("vcodec") not in (None, "none")
                   and f.get("height") and f.get("protocol") == "https" and f.get("ext") == "mp4"]
        if ffmpeg and formats:
            chosen = min(formats, key=lambda f: abs(f["height"] - 720))
            for timestamp in (20, 40, 80):
                if timestamp >= (data.get("duration") or 0):
                    continue
                target = out_dir / f"{vid}-{timestamp}s.jpg"
                try:
                    run = subprocess.run([
                        ffmpeg, "-hide_banner", "-loglevel", "error", "-ss", str(timestamp),
                        "-i", chosen["url"], "-frames:v", "1", "-y", str(target),
                    ], capture_output=True, timeout=40)
                    if run.returncode == 0 and target.exists():
                        result["frames"].append({"seconds": timestamp, "file": target.name})
                    else:
                        errors.append(f"Frame de {timestamp}s indisponível.")
                except subprocess.TimeoutExpired:
                    errors.append(f"Frame de {timestamp}s excedeu o limite de tempo.")
        else:
            errors.append("Frames completos precisam de ffmpeg e formato acessível; usar prévia/navegador.")
    return result


def first_missing():
    import gspread
    from google.oauth2.service_account import Credentials
    if not os.environ.get("GOOGLE_CREDENTIALS_JSON"):
        raise ValueError("--first-missing precisa de GOOGLE_CREDENTIALS_JSON; use --video para testar sem credenciais.")
    credentials = Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
                                                       scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    rows = gspread.authorize(credentials).open_by_key(
        "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0").worksheet("todos").get_all_values()
    if not rows or rows[0][:7] != ["quero_postar", "obra", "canal", "data_postado", "viewers", "duracao", "link"]:
        raise ValueError("Cabeçalho da aba todos diferente do esperado.")
    for row in rows[1:]:
        if len(row) >= 7 and not row[1].strip() and row[6].strip():
            return get_video_id(row[6])
    raise ValueError("Nenhum vídeo com link e obra vazia encontrado.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--video")
    target.add_argument("--first-missing", action="store_true")
    parser.add_argument("--out", required=True)
    parser.add_argument("--no-frames", action="store_true")
    parser.add_argument("--no-related", action="store_true")
    args = parser.parse_args()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    vid = first_missing() if args.first_missing else get_video_id(args.video)
    primary = collect(vid, out_dir, frames=not args.no_frames)
    result = {"primary": primary, "related": [], "status": "aguardando_revisao"}
    if not args.no_related:
        linked = re.findall(r"(?:youtu\.be/|youtube\.com/watch\?v=)([\w-]{11})", primary["description"])
        for other in list(dict.fromkeys(linked))[:2]:
            if other == vid:
                continue
            try:
                result["related"].append(collect(other, out_dir, frames=False))
            except Exception:
                primary["errors"].append(f"Parte vinculada {other} inacessível; tentar pelo navegador.")
    print(json.dumps(result, ensure_ascii=True))


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Instale as dependências: python -m pip install -r requirements-investigate.txt", file=sys.stderr)
        sys.exit(1)
    except Exception:
        # Tracebacks de bibliotecas podem incluir parâmetros de credenciais/URLs assinadas.
        print("Coleta falhou. Confira dependências, credenciais (se --first-missing), acesso ao vídeo e rede.", file=sys.stderr)
        sys.exit(1)
