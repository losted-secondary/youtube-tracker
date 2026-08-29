import os
import json
import re
import unicodedata
from datetime import datetime, timezone, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import gspread
from google.oauth2.service_account import Credentials

from comick import fill_names
import intro

SHEET_ID = "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0"
SHEET_TAB = "todos"
CHANNEL_HANDLES = [
    "FrierenManhwa1", "Manhwa_Fresh", "Manhwa_Teller1",
    "Magical_ManhwaRecaps", "MamoruManhwa", "TobsManhwa",
    "ManhwaVoidd", "Gave-k8y", "kawaiikotoYT", "manhwaexplorer5310",
    "John.Manhwa", "FuriosToon", "manhwadealer", "ManhwaRecapZone",
    "MrManhwas01", "Dazai_manhwa", "MobManhwa",
    "Manhwachatter", "Villainscan", "Tyler_Manhwa", "AniRayManhwa",
    "Manhwa_First", "ManhwaRecapsOfficial", "Manga_Explained", "ManhwaOutpost",
]
BACKFILL_DAYS = 305
# Nas rodadas normais so atualiza os viewers dos videos dos ultimos RECENT_DAYS dias;
# a varredura completa acontece 1x por hora (rodada do comeco da hora). Video velho
# quase nao ganha view, e `videos.list` custa 1 unidade a cada 50 videos: com 2.500
# videos na planilha, atualizar todo mundo a cada 10 min estouraria a cota diaria.
RECENT_DAYS = 45
# O nome da obra so era extraido quando o video ENTRAVA na planilha. Muito canal fixa o
# comentario com o nome depois do upload, e a celula ficava vazia pra sempre. Entao a
# cada varredura completa (1x/hora) o script tenta de novo nos videos recentes que ainda
# estao sem obra. Teto baixo porque cada tentativa custa ate 2 unidades de cota.
OBRA_RETRY_DAYS = 3
OBRA_RETRY_MAX = 10
FULL_SWEEP_BEFORE_MINUTE = 10   # ~1 rodada por hora cai nessa faixa (gatilho de 10 min)

# playlist de uploads de cada canal (`UU` + id do canal). E fixa pra sempre, entao nao
# vale gastar 1 unidade de cota por canal por rodada chamando `channels.list` — o nome
# do canal vem do proprio `playlistItems` (`videoOwnerChannelTitle`), sempre atualizado.
# Handle que nao estiver aqui cai no `channels.list` normal (canal novo na lista).
UPLOADS_PLAYLISTS = {
    "FrierenManhwa1": "UUEQWc3zNnGKmVyViM7jPdYQ",
    "Manhwa_Fresh": "UUz3IjVYoX-tmmPPTedhXQEQ",
    "Manhwa_Teller1": "UURepIiX_QAUnxr2XL1EDYUQ",
    "Magical_ManhwaRecaps": "UUXirHhcCTfZediXFsjTrMuw",
    "MamoruManhwa": "UUjtG_KmctknonQtG5M_RUDg",
    "TobsManhwa": "UU6RUVkRxvDGAswPx4fIBh-g",
    "ManhwaVoidd": "UUP0U_knol46nPB8itOhGLfA",
    "Gave-k8y": "UUQn6wzk1TibcW1kZHpmkK9w",
    "kawaiikotoYT": "UU66gPCteiijwe4dhjZ4kI3g",
    "manhwaexplorer5310": "UUHqVd77nLslVkVx7WSI6-dg",
    "John.Manhwa": "UU6Fj81aY7z0X8GUF_agdVNw",
    "FuriosToon": "UU_Fs1Df-cMqF4J20OF6B6Yw",
    "manhwadealer": "UUJpBKflQM-kk4OJ19s3comA",
    "ManhwaRecapZone": "UUB62Dqx3sFCg9wdh8b5fpJA",
    "MrManhwas01": "UUxTN-InpXxUuKFYyTuso_1A",
    "Dazai_manhwa": "UUqVmdoA7CKELyMX3Tav4Odw",
    "MobManhwa": "UUe-Gaq4OcJD_iJN4XEpLliA",
    "Manhwachatter": "UUmIT58FeYE7qni9ahy2oSuQ",
    "Villainscan": "UUyWojyDxf7bJ_5jpCd0bAOw",
    "Tyler_Manhwa": "UUj3KZkYeIw-x7hi9IK9R4fw",
    "AniRayManhwa": "UU5fPmMjjCEMoW5_D738cFMQ",
    "Manhwa_First": "UUTiIqLIqI9EKaR8riKZ6-8g",
    "ManhwaRecapsOfficial": "UUdfDbwFJf0wc0aVp_xpIf7w",
    "Manga_Explained": "UUc3xCO79t87Y2D5MevDAL_Q",
    "ManhwaOutpost": "UUsRXoBg1Na4Hw75tDZowQmg",
}

HEADER = ["quero_postar", "obra", "canal", "data_postado", "viewers", "duracao", "link", "nomes_variantes"]
NCOLS = len(HEADER)
# teto de buscas no comick por rodada (cada uma ~0.5s). O backfill inicial foi feito
# rodando `python comick.py` na mao; no dia a dia entram poucos videos por rodada.
COMICK_MAX_LOOKUPS = 60
DATE_FMT = "%d/%m/%Y %H:%M"
BRT = timezone(timedelta(hours=-3))


def duration_fraction(iso):
    # devolve a duracao como FRACAO DO DIA (numero), nao string. Gravar string tipo
    # "11:40" fazia o Sheets ler como HH:MM (11h40) em vez de 11min40s; gravando o
    # numero direto nao ha parse ambiguo. A coluna F tem formato hh:mm:ss fixado.
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return ""
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return (h * 3600 + mi * 60 + s) / 86400.0


def extract_video_id(url):
    m = re.search(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})", url or "")
    return m.group(1) if m else None


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# prefixos mais especificos primeiro (alternancia do regex casa da esquerda p/ direita)
OBRA_PATTERN = re.compile(
    r"^\s*[^\w]*\s*(manhwa name|manhwa title|original name|original title|name|title|manhwa)\s*[:\-–—→]\s*(.+?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
OBRA_BLACKLIST = re.compile(r"in the comments?|pinned|below|see below", re.IGNORECASE)


def extract_obra_from_text(text):
    if not text:
        return None
    # NFKC: converte letras unicode "chique" (ex: 𝖳𝗂𝗍𝗅𝖾 -> Title) para ASCII
    text = unicodedata.normalize("NFKC", text)
    m = OBRA_PATTERN.search(text)
    if not m:
        return None
    name = m.group(2).strip().rstrip(",")
    # tira sufixo de capitulos colado no titulo: "1~265", "1-47 chaps", "___45_chaps"
    # sufixo de capitulos: "1~265", "1 - 100 ch", "1-47 chaps", "1 a 80 chapters"
    name = re.sub(r"[\s_]*\d+\s*[-~]\s*\d+\s*(?:ch(?:ap(?:ter)?)?s?\.?)?\s*$", "", name, flags=re.I)
    name = re.sub(r"_+\d+_?chaps?\.?\s*$", "", name, flags=re.I)
    name = name.strip(" _\t-")
    if not (2 < len(name) < 200):
        return None
    if name.lower().startswith(("http", "manhwa recap", "the manhwa")):
        return None
    if OBRA_BLACKLIST.search(name):
        return None
    return name


def fetch_owner_comment(yt, video_id, channel_id):
    # varre ate ~200 comentarios (2 paginas de 100); o comentario do dono com o
    # nome da obra raramente esta no top-5, entao paginamos. maxResults nao custa
    # cota extra (commentThreads = 1 unidade por chamada).
    token = None
    for _ in range(2):
        try:
            r = yt.commentThreads().list(
                part="snippet", videoId=video_id, maxResults=100,
                order="relevance", pageToken=token,
            ).execute()
        except HttpError:
            return None
        for item in r.get("items", []):
            tc = item["snippet"]["topLevelComment"]["snippet"]
            if tc.get("authorChannelId", {}).get("value") == channel_id:
                return tc["textOriginal"]
        token = r.get("nextPageToken")
        if not token:
            break
    return None


def extract_obra(yt, video_id, channel_id, description):
    obra = extract_obra_from_text(description)
    if obra:
        return obra
    comment = fetch_owner_comment(yt, video_id, channel_id)
    return extract_obra_from_text(comment)


def parse_legacy_date_to_brt(s):
    if not s:
        return None
    try:
        return datetime.strptime(s, "%d/%m/%Y %H:%M").replace(tzinfo=BRT)
    except ValueError:
        pass
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).astimezone(BRT)
    except ValueError:
        pass
    return None


def parse_sheet_date(s):
    """Le a data do jeito que o get_all_values devolve: 'dd/mm/yyyy - HH:mm' (o ' - '
    vem do formato da coluna D, nao do que o script grava). Usada so pra decidir se o
    video e recente o bastante pra atualizar os viewers nesta rodada."""
    s = (s or "").replace(" - ", " ").strip()
    for fmt in ("%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=BRT)
        except ValueError:
            pass
    return None


def setup_formatting(spreadsheet, sheet):
    sheet_id = sheet.id
    requests = [
        {
            "updateSheetProperties": {
                "properties": {"sheetId": sheet_id, "gridProperties": {"frozenRowCount": 1}},
                "fields": "gridProperties.frozenRowCount",
            }
        },
        {
            "setDataValidation": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 1},
                "rule": {"condition": {"type": "BOOLEAN"}, "strict": False},
            }
        },
        {
            # autodefesa: checkbox so vale na coluna A. Remove qualquer validacao
            # que apareca em B:H (ex: caixa colada por engano na coluna da obra).
            "setDataValidation": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 1, "endColumnIndex": NCOLS},
            }
        },
        {
            "repeatCell": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 3, "endColumnIndex": 4},
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "DATE_TIME", "pattern": 'dd/mm/yyyy" - "HH:mm'}}},
                "fields": "userEnteredFormat.numberFormat",
            }
        },
        {
            "repeatCell": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 4, "endColumnIndex": 5},
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
                "fields": "userEnteredFormat.numberFormat",
            }
        },
        {
            # coluna F (duracao) = sempre hh:mm:ss. Sem isso o Sheets auto-formatava
            # cada celula de um jeito (hh:mm escondia os segundos).
            "repeatCell": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 5, "endColumnIndex": 6},
                "cell": {"userEnteredFormat": {"numberFormat": {"type": "TIME", "pattern": "hh:mm:ss"}}},
                "fields": "userEnteredFormat.numberFormat",
            }
        },
        {
            # coluna H (nomes_variantes) e longa: CLIP pra nao esticar a altura da linha.
            "repeatCell": {
                "range": {"sheetId": sheet_id, "startRowIndex": 1, "startColumnIndex": 7, "endColumnIndex": 8},
                "cell": {"userEnteredFormat": {"wrapStrategy": "CLIP"}},
                "fields": "userEnteredFormat.wrapStrategy",
            }
        },
    ]
    spreadsheet.batch_update({"requests": requests})


def ensure_filter_covers_data(spreadsheet, sheet, data_row_count, ncols=NCOLS):
    md = spreadsheet.fetch_sheet_metadata()
    bf = None
    for s in md.get("sheets", []):
        if s.get("properties", {}).get("sheetId") == sheet.id:
            bf = s.get("basicFilter")
            break

    current_end = bf.get("range", {}).get("endRowIndex", 0) if bf else 0
    # tambem refaz o filtro se ele nao cobre todas as COLUNAS (ex: ficou em A:G depois
    # que a coluna H entrou) — senao ele so seria corrigido quando entrasse linha nova.
    current_cols = bf.get("range", {}).get("endColumnIndex", 0) if bf else 0
    if current_end >= data_row_count and current_cols >= ncols:
        return

    new_filter = {
        "range": {
            "sheetId": sheet.id,
            "startRowIndex": 0,
            "endRowIndex": max(current_end, data_row_count),  # nunca encolher o range
            "startColumnIndex": 0,
            "endColumnIndex": ncols,
        }
    }
    if bf:
        for key in ("sortSpecs", "criteria", "filterSpecs"):
            if bf.get(key):
                new_filter[key] = bf[key]
    requests = []
    if bf:
        requests.append({"clearBasicFilter": {"sheetId": sheet.id}})
    requests.append({"setBasicFilter": {"filter": new_filter}})
    spreadsheet.batch_update({"requests": requests})


def sort_by_filter_order(spreadsheet, sheet, data_row_count, ncols=NCOLS, date_col=3):
    """Reordena as linhas de dados SEMPRE por data (coluna D) descendente, pra video
    novo subir pro topo. NAO usar o sortSpecs salvo no filtro: se o usuario clica um
    cabecalho na UI (ex: ordenar por duracao), esse spec fica salvo e o script passava
    a reordenar TODA a planilha por aquele criterio a cada rodada, embaralhando tudo.
    O sort da UI e so pra visualizar; a ordem fisica fica fixa por data."""
    specs = [{"dimensionIndex": date_col, "sortOrder": "DESCENDING"}]
    spreadsheet.batch_update({"requests": [{
        "sortRange": {
            "range": {
                "sheetId": sheet.id, "startRowIndex": 1, "endRowIndex": data_row_count,
                "startColumnIndex": 0, "endColumnIndex": ncols,
            },
            "sortSpecs": specs,
        }
    }]})


def migrate_column_a_booleans(spreadsheet, sheet):
    last_row = sheet.row_count
    data = spreadsheet.values_get(
        f"'{sheet.title}'!A2:A{last_row}",
        params={"valueRenderOption": "UNFORMATTED_VALUE"},
    )
    values = data.get("values", [])
    updates = []
    for i, row in enumerate(values, start=2):
        if not row:
            continue
        v = row[0]
        if isinstance(v, str) and v.strip().upper() in ("FALSE", "TRUE"):
            updates.append({"range": f"A{i}", "values": [[v.strip().upper() == "TRUE"]]})
    if updates:
        sheet.batch_update(updates, value_input_option="USER_ENTERED")
    return len(updates)


def main():
    yt = build("youtube", "v3", developerKey=os.environ["YOUTUBE_API_KEY"])
    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    spreadsheet = gspread.authorize(creds).open_by_key(SHEET_ID)
    sheet = spreadsheet.worksheet(SHEET_TAB)

    setup_formatting(spreadsheet, sheet)
    n_a_migrated = migrate_column_a_booleans(spreadsheet, sheet)

    rows = sheet.get_all_values()
    if not rows or rows[0] != HEADER:
        sheet.update([HEADER], "A1:H1")
        rows = sheet.get_all_values()

    now_utc = datetime.now(timezone.utc)
    full_sweep = now_utc.minute < FULL_SWEEP_BEFORE_MINUTE
    recent_cutoff = now_utc - timedelta(days=RECENT_DAYS)

    obra_retry_cutoff = now_utc - timedelta(days=OBRA_RETRY_DAYS)
    existing_by_id = {}
    recent_ids = []
    obra_retry = []
    date_migrations = []
    for i, row in enumerate(rows[1:], start=2):
        if len(row) >= 7:
            vid = extract_video_id(row[6])
            if vid:
                existing_by_id[vid] = i
                dt = parse_sheet_date(row[3]) if len(row) >= 4 else None
                # data ilegivel -> trata como recente (uma linha a mais nao pesa)
                if dt is None or dt >= recent_cutoff:
                    recent_ids.append(vid)
                obra_vazia = not (row[1].strip() if len(row) > 1 else "")
                if obra_vazia and dt is not None and dt >= obra_retry_cutoff:
                    obra_retry.append((vid, i))
            if len(row) >= 4 and row[3] and "/" not in row[3]:
                dt = parse_legacy_date_to_brt(row[3])
                if dt:
                    date_migrations.append({"range": f"D{i}", "values": [[dt.strftime(DATE_FMT)]]})

    if date_migrations:
        sheet.batch_update(date_migrations, value_input_option="USER_ENTERED")

    cutoff = datetime.now(timezone.utc) - timedelta(days=BACKFILL_DAYS)
    new_videos = []

    for handle in CHANNEL_HANDLES:
        uploads = UPLOADS_PLAYLISTS.get(handle)
        if not uploads:
            # canal recem-adicionado a lista: descobre a playlist uma vez (1 unidade) e
            # avisa pra colar em UPLOADS_PLAYLISTS.
            resp = yt.channels().list(part="contentDetails", forHandle=handle).execute()
            if not resp.get("items"):
                print(f"channel not found: @{handle}")
                continue
            uploads = resp["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
            print(f'novo canal: adicione "{handle}": "{uploads}" em UPLOADS_PLAYLISTS')

        page_token = None
        stop = False
        while not stop:
            try:
                r = yt.playlistItems().list(
                    part="snippet,contentDetails", playlistId=uploads,
                    maxResults=50, pageToken=page_token,
                ).execute()
            except HttpError as e:
                if e.resp.status == 404:
                    print(f"uploads playlist not accessible for @{handle} ({uploads}) — skipping")
                else:
                    print(f"error fetching @{handle}: {e}")
                break
            items = r["items"]
            n_new = 0
            for it in items:
                pub_str = it["contentDetails"].get("videoPublishedAt")
                if not pub_str:
                    continue
                pub = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
                if pub < cutoff:
                    stop = True
                    break
                vid = it["contentDetails"]["videoId"]
                if vid in existing_by_id:
                    continue
                title = it["snippet"].get("videoOwnerChannelTitle") or it["snippet"].get("channelTitle", "")
                new_videos.append({"id": vid, "channel": title, "published": pub})
                n_new += 1
            # so vai pra proxima pagina se a pagina INTEIRA era novidade — ai a planilha
            # esta atrasada de verdade (backfill). Na rodada normal a 1a pagina ja tem
            # video conhecido, entao para em 1 unidade de cota por canal.
            if stop or n_new < len(items):
                break
            page_token = r.get("nextPageToken")
            if not page_token:
                break

    refresh_ids = list(existing_by_id.keys()) if full_sweep else recent_ids
    all_ids = [v["id"] for v in new_videos] + refresh_ids
    stats = {}
    for batch in chunk(all_ids, 50):
        r = yt.videos().list(part="snippet,statistics,contentDetails", id=",".join(batch)).execute()
        for it in r["items"]:
            stats[it["id"]] = {
                "views": int(it["statistics"].get("viewCount", 0)),
                "duration": duration_fraction(it["contentDetails"]["duration"]),
                "description": it["snippet"].get("description", ""),
                "channelId": it["snippet"].get("channelId"),
            }

    new_rows = []
    for v in new_videos:
        s = stats.get(v["id"], {"views": 0, "duration": "", "description": "", "channelId": None})
        obra = extract_obra(yt, v["id"], s.get("channelId"), s.get("description", "")) or ""
        new_rows.append([
            False, obra, v["channel"],
            v["published"].astimezone(BRT).strftime(DATE_FMT),
            s["views"], s["duration"],
            f"https://youtu.be/{v['id']}",
            "",  # nomes_variantes: preenchido logo abaixo pelo comick
        ])
    if new_rows:
        sheet.append_rows(new_rows, value_input_option="USER_ENTERED")

    updates = []
    for vid, row_num in existing_by_id.items():
        if vid in stats:
            updates.append({"range": f"E{row_num}", "values": [[stats[vid]["views"]]]})
    if updates:
        sheet.batch_update(updates)

    # 2a tentativa de pegar o nome da obra (comentario fixado depois do upload).
    # So na varredura completa, senao seria 1-2 unidades de cota por video a cada 10 min.
    obra_updates = []
    if full_sweep:
        for vid, row_num in obra_retry[:OBRA_RETRY_MAX]:
            st = stats.get(vid)
            if not st:
                continue
            obra = extract_obra(yt, vid, st.get("channelId"), st.get("description", ""))
            if obra:
                obra_updates.append({"range": f"B{row_num}", "values": [[obra]]})
        if obra_updates:
            sheet.batch_update(obra_updates, value_input_option="USER_ENTERED")

    # nomes alternativos (comick): so mexe em linha com obra preenchida e coluna H vazia.
    # As linhas novas ja entram nessa conta — append_rows coloca elas logo apos `rows`,
    # entao a numeracao de rows + new_rows bate com a da planilha (mesma premissa do sort).
    n_found, n_missing = fill_names(
        sheet, rows + [[str(c) for c in r] for r in new_rows], max_lookups=COMICK_MAX_LOOKUPS
    )

    # contar linhas FISICAS reais (cabecalho + todas as linhas preenchidas) + as novas.
    # NAO usar len(existing_by_id): ele ignora linhas sem link e funde IDs duplicados,
    # subcontando o total e deixando as ultimas linhas fora do filtro/sort.
    total_data_rows = len(rows) + len(new_rows)
    ensure_filter_covers_data(spreadsheet, sheet, total_data_rows)
    if new_rows:
        sort_by_filter_order(spreadsheet, sheet, total_data_rows)

    # aba `intro` (Manhwa Void + Tobs Manhwa). Por ultimo, pra ja pegar os videos novos
    # e os nomes do comick desta rodada; ela rele as duas abas por conta propria.
    intro.sync(spreadsheet)

    modo = "completa" if full_sweep else f"recentes({RECENT_DAYS}d)"
    print(f"[{modo}] added {len(new_rows)} new, {len(obra_updates)} obras achadas na 2a tentativa, updated {len(updates)} viewer counts, migrated {len(date_migrations)} legacy dates, {n_a_migrated} checkboxes, comick: {n_found} nomes / {n_missing} nao encontrados")


if __name__ == "__main__":
    main()
