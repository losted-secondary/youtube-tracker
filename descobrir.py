"""Descoberta de videos fora dos canais principais.

Faz o mesmo que pesquisar "manhwa recap" no YouTube com filtro "esta semana" + "mais
vistos": pega o que esta bombando no nicho mesmo que o canal nao esteja em
CHANNEL_HANDLES. O que passar de MIN_VIEWS entra na aba `todos` como um video qualquer
(viewers continuam sendo atualizados, obra/comick tambem), mas com a linha pintada de
COR_FORA pra dar pra ver que nao e de um dos canais principais.

`search.list` custa 100 unidades de cota por pagina (o resto do tracker gasta ~1 por
chamada), entao isso so roda a cada RUN_EVERY_HOURS horas, na varredura completa.
So entra recap em ingles (ver is_english). Com 2 buscas x 2 paginas = 400 unidades por
rodada, 4 rodadas/dia = 1.600 unidades/dia.
"""
import os
import re
from datetime import datetime, timedelta, timezone

from googleapiclient.errors import HttpError

QUERIES = ["manhwa recap", "manhua recap"]
PAGES_PER_QUERY = 2          # 50 resultados por pagina, ordenados por views
WINDOW_DAYS = 7              # "esta semana"
MIN_VIEWS = 100_000          # views minimas (dentro da janela) pra entrar na planilha
RUN_EVERY_HOURS = 6          # roda quando hora UTC % isso == 0 (na varredura completa)

# fundo laranja-claro nas linhas de canal de fora; linhas normais ficam sem cor.
COR_FORA = {"red": 0.99, "green": 0.90, "blue": 0.80}
COR_NORMAL = {"red": 1.0, "green": 1.0, "blue": 1.0}

# so recap em ingles. "Manhwa Explainer Hindi" & cia marcam o titulo como "en" mas falam
# hindi, entao a palavra no titulo/canal derruba mesmo com idioma "en".
NAO_INGLES = re.compile(r"\bhindi\b", re.IGNORECASE)

# canais proprios (Juicy, Senzu): video nosso que bombar nao e "oportunidade".
OWN_CHANNEL_IDS = {"UCUnLH9qyXBI8ijs9Kmbt9Ng", "UCOcsn9uPit7AW3QvneP3bBg"}


def should_run(now_utc, full_sweep):
    # DESCOBRIR_AGORA=1 (input do workflow_dispatch) forca a busca fora do horario.
    if os.environ.get("DESCOBRIR_AGORA") == "1":
        return True
    return full_sweep and now_utc.hour % RUN_EVERY_HOURS == 0


def main_channel_ids(uploads_playlists):
    # playlist de uploads "UU..." -> id do canal "UC..." (mesmo sufixo).
    return {"UC" + p[2:] for p in uploads_playlists.values() if p.startswith("UU")}


def is_english(snippet):
    """Idioma do AUDIO manda; canal que nao preenche cai no idioma do titulo/descricao."""
    lang = (snippet.get("defaultAudioLanguage") or snippet.get("defaultLanguage") or "").lower()
    if not lang.startswith("en"):
        return False
    return not NAO_INGLES.search(snippet.get("title", "") + " " + snippet.get("channelTitle", ""))


def find(yt, known_channel_ids, known_video_ids, now_utc):
    """Devolve [{"id", "channel", "published"}] dos videos de fora que passaram do corte,
    no mesmo formato que o main usa pros videos novos dos canais principais."""
    after = (now_utc - timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    skip_channels = known_channel_ids | OWN_CHANNEL_IDS
    candidates = {}
    for q in QUERIES:
        token = None
        for _ in range(PAGES_PER_QUERY):
            try:
                r = yt.search().list(
                    part="snippet", q=q, type="video", order="viewCount",
                    publishedAfter=after, videoDuration="long",  # >20 min: corta shorts
                    relevanceLanguage="en",
                    maxResults=50, pageToken=token,
                ).execute()
            except HttpError as e:
                print(f"[descobrir] erro na busca '{q}': {e}")
                break
            for it in r.get("items", []):
                vid = it["id"].get("videoId")
                sn = it["snippet"]
                if not vid or vid in known_video_ids or sn.get("channelId") in skip_channels:
                    continue
                candidates[vid] = sn
            token = r.get("nextPageToken")
            if not token:
                break

    if not candidates:
        return []

    found = []
    ids = list(candidates)
    for i in range(0, len(ids), 50):
        r = yt.videos().list(part="snippet,statistics", id=",".join(ids[i:i + 50])).execute()
        for it in r.get("items", []):
            if int(it["statistics"].get("viewCount", 0)) < MIN_VIEWS:
                continue
            if not is_english(it["snippet"]):
                continue
            sn = candidates[it["id"]]
            found.append({
                "id": it["id"],
                "channel": sn.get("channelTitle", ""),
                "published": datetime.fromisoformat(sn["publishedAt"].replace("Z", "+00:00")),
            })
    return found


def color_rows(spreadsheet, sheet, row_colors, ncols):
    """row_colors: [(numero_da_linha, cor)]. Pinta A:ncols. O sortRange do main leva a
    formatacao junto com a linha, entao a cor acompanha o video depois de ordenar."""
    if not row_colors:
        return
    requests = [{
        "repeatCell": {
            "range": {"sheetId": sheet.id, "startRowIndex": n - 1, "endRowIndex": n,
                      "startColumnIndex": 0, "endColumnIndex": ncols},
            "cell": {"userEnteredFormat": {"backgroundColor": cor}},
            "fields": "userEnteredFormat.backgroundColor",
        }
    } for n, cor in row_colors]
    spreadsheet.batch_update({"requests": requests})


# Registro de tudo que ja entrou pela descoberta. Sem isso, apagar a linha de um video de
# fora na `todos` faria ele voltar na proxima busca (ainda esta no top da semana).
SEEN_TAB = "_descobertos"
SEEN_HEADER = ["video_id", "adicionado_em"]


def _seen_sheet(spreadsheet):
    try:
        return spreadsheet.worksheet(SEEN_TAB)
    except Exception:
        ws = spreadsheet.add_worksheet(SEEN_TAB, rows=1000, cols=len(SEEN_HEADER))
        ws.update([SEEN_HEADER], "A1:B1")
        spreadsheet.batch_update({"requests": [{"updateSheetProperties": {
            "properties": {"sheetId": ws.id, "hidden": True}, "fields": "hidden"}}]})
        return ws


def load_seen(spreadsheet):
    return {r[0] for r in _seen_sheet(spreadsheet).get_all_values()[1:] if r and r[0]}


def save_seen(spreadsheet, video_ids, now_utc):
    if video_ids:
        stamp = now_utc.strftime("%Y-%m-%d %H:%M")
        _seen_sheet(spreadsheet).append_rows([[v, stamp] for v in video_ids],
                                             value_input_option="RAW")
