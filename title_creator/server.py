"""Loopback-only server: python -m title_creator.server [--sync] [--open]."""
import argparse
import json
import secrets
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from .core import ROOT, AppError, api_key, generate, library_stats, sync_library

TOKEN = secrets.token_urlsafe(32)
JOB_LOCK = threading.Lock()
STATE_LOCK = threading.Lock()
STATE = {"syncing": False, "message": "", "error": ""}


def update_state(**kwargs):
    with STATE_LOCK:
        STATE.update(kwargs)


def sync_job():
    try:
        sync_library(progress=lambda message: update_state(message=message))
        update_state(error="")
    except AppError as error:
        update_state(error=str(error))
    except Exception:
        update_state(error="Falha ao atualizar a biblioteca. Os dados anteriores foram preservados.")
    finally:
        update_state(syncing=False)
        JOB_LOCK.release()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def send_body(self, body, content_type, status=200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self' data:; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def send_json(self, body, status=200):
        self.send_body(json.dumps(body, ensure_ascii=False).encode(), "application/json; charset=utf-8", status)

    def local_request(self):
        host = self.headers.get("Host", "")
        allowed = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        if host not in allowed:
            self.send_json({"error": "Host não permitido."}, 403)
            return False
        origin = self.headers.get("Origin")
        if origin and origin not in {"http://" + h for h in allowed}:
            self.send_json({"error": "Origem não permitida."}, 403)
            return False
        return True

    def do_GET(self):
        if not self.local_request():
            return
        path = urlparse(self.path).path
        if path == "/api/status":
            try:
                api_key()
                configured = True
            except AppError:
                configured = False
            with STATE_LOCK:
                state = dict(STATE)
            self.send_json({**library_stats(), **state, "configured": configured, "token": TOKEN})
            return
        files = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"), "/style.css": ("style.css", "text/css")}
        if path not in files:
            self.send_json({"error": "Página não encontrada."}, 404)
            return
        filename, content_type = files[path]
        self.send_body((ROOT / "static" / filename).read_bytes(), content_type + "; charset=utf-8")

    def do_POST(self):
        if not self.local_request():
            return
        if not secrets.compare_digest(self.headers.get("X-Session-Token", ""), TOKEN):
            self.send_json({"error": "Sessão expirada. Atualize a página."}, 403)
            return
        if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            self.send_json({"error": "Envie JSON."}, 415)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 64000:
                raise ValueError()
            data = json.loads(self.rfile.read(length))
        except (ValueError, UnicodeError):
            self.send_json({"error": "Pedido inválido ou grande demais."}, 400)
            return
        if self.path not in {"/api/generate", "/api/sync"}:
            self.send_json({"error": "Rota não encontrada."}, 404)
            return
        if not JOB_LOCK.acquire(blocking=False):
            self.send_json({"error": "Aguarde a geração ou atualização em andamento."}, 409)
            return
        if self.path == "/api/sync":
            update_state(syncing=True, message="Iniciando atualização…", error="")
            threading.Thread(target=sync_job, daemon=True).start()
            self.send_json({"started": True}, 202)
            return
        try:
            self.send_json(generate(data))
        except AppError as error:
            self.send_json({"error": str(error)}, 422)
        except Exception:
            # Never expose upstream request URLs, headers, credentials or tracebacks.
            self.send_json({"error": "Falha inesperada ao gerar. Tente novamente."}, 500)
        finally:
            JOB_LOCK.release()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--sync", action="store_true", help="Atualiza a biblioteca e encerra")
    parser.add_argument("--refresh-titles", action="store_true", help="Consulta títulos novamente com --sync")
    parser.add_argument("--open", action="store_true", help="Abre a interface no navegador")
    args = parser.parse_args()
    if args.sync:
        try:
            print(json.dumps(sync_library(print, force=args.refresh_titles), ensure_ascii=False))
        except AppError as error:
            parser.exit(1, str(error) + "\n")
        return
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{server.server_port}"
    print("Criador de títulos: " + url, flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
