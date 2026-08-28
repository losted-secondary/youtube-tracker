"""Aba `intro`: subconjunto do `todos` com so os videos do Manhwa Void e do Tobs Manhwa,
mais 5 checkboxes de controle (minha intro / Paguei? / 150k / 500k / 1M).

Alimentada a cada sync pelo main.py. A coluna `obra` e ACORRENTADA nos dois sentidos:
preencheu no principal, aparece aqui; preencheu aqui, aparece no principal.

Como o sentido e decidido (coluna oculta M, `_obra_sync` = ultimo valor sincronizado):
  - um lado vazio, outro preenchido -> o preenchido ganha;
  - os dois preenchidos e diferentes -> ganha o lado que mudou desde o ultimo sync
    (se os dois mudaram, o `intro` ganha).
As outras colunas (canal, data, viewers, duracao, link, nomes) sao espelho do principal:
o `todos` manda, editar aqui nao adianta. Os 5 checkboxes existem so aqui e nunca sao
tocados depois que a linha entra.
"""
import re
from datetime import datetime, timezone, timedelta

BRT = timezone(timedelta(hours=-3))
# So entra video publicado a partir daqui. Em 27/08/2026 o usuario zerou a aba pra
# acompanhar so o que vier daqui pra frente — os 275 videos antigos foram apagados de
# proposito, e sem esse corte o proximo sync recriaria todos eles.
INTRO_START = datetime(2026, 8, 27, 18, 35, tzinfo=BRT)
# a data chega do Sheets como numero serial (dias desde 30/12/1899), entao o corte
# tambem vira serial em vez de converter cada linha pra datetime.
INTRO_START_SERIAL = (INTRO_START - datetime(1899, 12, 30, tzinfo=BRT)).total_seconds() / 86400.0

INTRO_TAB = "intro"
INTRO_HEADER = [
    "minha intro", "Paguei?", "150k", "500k", "1M",
    "obra", "canal", "data_postado", "viewers", "duracao", "link", "nomes_variantes",
    "_obra_sync",   # coluna oculta: ultimo valor de obra sincronizado (resolve conflito)
]
NINTRO = len(INTRO_HEADER)          # 13, contando a oculta
NINTRO_VISIBLE = NINTRO - 1         # 12, o que o filtro do cabecalho cobre
LAST_COL = "M"
N_CHECKS = 5                        # A:E = os 5 checkboxes de controle

# indices no `intro`
I_OBRA, I_CANAL, I_DATA, I_VIEWS, I_DUR, I_LINK, I_NOMES, I_SHADOW = 5, 6, 7, 8, 9, 10, 11, 12
# indices no `todos`
T_OBRA, T_CANAL, T_DATA, T_VIEWS, T_DUR, T_LINK, T_NOMES = 1, 2, 3, 4, 5, 6, 7

# o `todos` guarda o TITULO do canal, nao o handle; aceitamos as duas formas
# normalizadas caso o dono renomeie o canal pro proprio handle.
INTRO_CHANNELS = ("Manhwa Void", "Tobs Manhwa", "ManhwaVoidd", "TobsManhwa")


def _norm_chan(s):
    return re.sub(r"[^a-z0-9]+", "", str(s or "").lower())


CHANNEL_KEYS = {_norm_chan(c) for c in INTRO_CHANNELS}


def _pad(row, n):
    row = list(row)
    return row + [""] * (n - len(row)) if len(row) < n else row[:n]


def _read(spreadsheet, tab, ncols, last_col, content_from):
    """Le a aba com UNFORMATTED_VALUE: viewers/duracao/data voltam como NUMERO e os
    checkboxes como bool. Ler formatado devolveria '1.234' e regravar isso dependeria
    do locale pra virar numero de novo.

    `content_from` = primeira coluna que conta como conteudo de verdade. Celula vazia
    com validacao de checkbox volta como False, entao as linhas em branco do fim da
    grade viriam como [False, False, ...] e seriam contadas como dados.
    """
    data = spreadsheet.values_get(
        "'{}'!A1:{}".format(tab, last_col),
        params={"valueRenderOption": "UNFORMATTED_VALUE"},
    )
    rows = [_pad(r, ncols) for r in data.get("values", [])]
    while len(rows) > 1 and not any(str(c).strip() for c in rows[-1][content_from:]):
        rows.pop()
    return rows


def ensure_tab(spreadsheet):
    import gspread
    try:
        return spreadsheet.worksheet(INTRO_TAB)
    except gspread.WorksheetNotFound:
        # rows=2: `append_rows` insere linhas conforme precisa. Grade grande sobrando
        # daria centenas de linhas em branco com checkbox (que a API le como FALSE).
        return spreadsheet.add_worksheet(title=INTRO_TAB, rows=2, cols=NINTRO)


def setup_formatting(spreadsheet, sheet):
    sid = sheet.id
    spreadsheet.batch_update({"requests": [
        {"updateSheetProperties": {
            "properties": {"sheetId": sid, "gridProperties": {"frozenRowCount": 1}},
            "fields": "gridProperties.frozenRowCount",
        }},
        # os 5 controles = checkbox
        {"setDataValidation": {
            "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": N_CHECKS},
            "rule": {"condition": {"type": "BOOLEAN"}, "strict": False},
        }},
        # e checkbox NENHUM fora deles (mesma autodefesa do `todos`)
        {"setDataValidation": {
            "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": N_CHECKS, "endColumnIndex": NINTRO},
        }},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": I_DATA, "endColumnIndex": I_DATA + 1},
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "DATE_TIME", "pattern": 'dd/mm/yyyy" - "HH:mm'}}},
            "fields": "userEnteredFormat.numberFormat",
        }},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": I_VIEWS, "endColumnIndex": I_VIEWS + 1},
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
            "fields": "userEnteredFormat.numberFormat",
        }},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": I_DUR, "endColumnIndex": I_DUR + 1},
            "cell": {"userEnteredFormat": {"numberFormat": {"type": "TIME", "pattern": "hh:mm:ss"}}},
            "fields": "userEnteredFormat.numberFormat",
        }},
        {"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": I_NOMES, "endColumnIndex": I_NOMES + 1},
            "cell": {"userEnteredFormat": {"wrapStrategy": "CLIP"}},
            "fields": "userEnteredFormat.wrapStrategy",
        }},
        # coluna de controle do sync: escondida, o usuario nao precisa ver
        {"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": I_SHADOW, "endIndex": I_SHADOW + 1},
            "properties": {"hiddenByUser": True},
            "fields": "hiddenByUser",
        }},
    ]})


def _is_new_enough(data_postado):
    """Linha nova so entra se for de depois do INTRO_START. Data vem como serial do
    Sheets; se vier texto (linha digitada na mao, formato estranho) fica de fora — a
    aba e alimentada pelo script, entao no duvida melhor nao entrar."""
    return isinstance(data_postado, (int, float)) and not isinstance(data_postado, bool)         and data_postado >= INTRO_START_SERIAL


def _as_bool(v):
    if isinstance(v, bool):
        return v
    return str(v).strip().upper() == "TRUE"


def sync(spreadsheet, verbose=True):
    """Devolve (novas, obras_pro_principal, obras_pro_intro)."""
    import main as m

    sheet = ensure_tab(spreadsheet)
    setup_formatting(spreadsheet, sheet)

    # Le os dois lados AGORA e grava logo em seguida: as escritas no `todos` sao por
    # numero de linha, entao a janela entre ler e gravar tem que ser de segundos
    # (mesmo cuidado do comick.write_names).
    main_rows = _read(spreadsheet, m.SHEET_TAB, m.NCOLS, "H", content_from=T_OBRA)
    intro_rows = _read(spreadsheet, INTRO_TAB, NINTRO, LAST_COL, content_from=N_CHECKS)

    if not intro_rows:
        intro_rows = [list(INTRO_HEADER)]
        sheet.update([INTRO_HEADER], "A1:{}1".format(LAST_COL))
    elif [str(c) for c in intro_rows[0]] != INTRO_HEADER:
        sheet.update([INTRO_HEADER], "A1:{}1".format(LAST_COL))
        intro_rows[0] = list(INTRO_HEADER)

    intro_by_id = {}
    for i, row in enumerate(intro_rows[1:], start=2):
        vid = m.extract_video_id(str(row[I_LINK]))
        if vid and vid not in intro_by_id:
            intro_by_id[vid] = (i, row)

    before = [list(r) for r in intro_rows]
    main_updates, new_rows = [], []
    to_intro = 0
    seen = set()

    for i, row in enumerate(main_rows[1:], start=2):
        if _norm_chan(row[T_CANAL]) not in CHANNEL_KEYS:
            continue
        vid = m.extract_video_id(str(row[T_LINK]))
        # o mesmo link pode aparecer 2x no `todos` (link colado errado numa linha de
        # strike, p.ex.). So a primeira ocorrencia manda, senao as duas linhas ficam
        # brigando pela mesma linha do intro a cada rodada.
        if not vid or vid in seen:
            continue
        seen.add(vid)
        obra_main = str(row[T_OBRA]).strip()
        mirror = [row[T_CANAL], row[T_DATA], row[T_VIEWS], row[T_DUR], row[T_LINK], row[T_NOMES]]

        if vid not in intro_by_id:
            if _is_new_enough(row[T_DATA]):
                new_rows.append([False] * N_CHECKS + [obra_main] + mirror + [obra_main])
            continue

        _, irow = intro_by_id[vid]
        obra_intro = str(irow[I_OBRA]).strip()
        shadow = str(irow[I_SHADOW]).strip()

        if obra_intro != obra_main:
            if obra_intro and (not obra_main or obra_intro != shadow):
                # editado aqui -> sobe pro principal
                main_updates.append({"range": "B{}".format(i), "values": [[obra_intro]]})
                obra_main = obra_intro
            else:
                # editado no principal (ou vazio aqui) -> desce pro intro
                obra_intro = obra_main
                to_intro += 1

        irow[:N_CHECKS] = [_as_bool(c) for c in irow[:N_CHECKS]]
        irow[I_OBRA] = obra_intro
        irow[I_CANAL:I_NOMES + 1] = mirror
        irow[I_SHADOW] = obra_main

    # 1) principal primeiro: escrita por numero de linha, o mais perto possivel da leitura
    if main_updates:
        spreadsheet.worksheet(m.SHEET_TAB).batch_update(
            main_updates, value_input_option="USER_ENTERED"
        )
    # 2) intro: matriz inteira numa escrita so (nada de mexer linha a linha)
    if intro_rows[1:] != before[1:]:
        sheet.update(intro_rows[1:], "A2:{}{}".format(LAST_COL, len(intro_rows)),
                     value_input_option="USER_ENTERED")
    if new_rows:
        sheet.append_rows(new_rows, value_input_option="USER_ENTERED")

    total = len(intro_rows) + len(new_rows)
    m.ensure_filter_covers_data(spreadsheet, sheet, total, ncols=NINTRO_VISIBLE)
    if new_rows:
        m.sort_by_filter_order(spreadsheet, sheet, total, ncols=NINTRO, date_col=I_DATA)

    if verbose:
        print("intro: {} novas, {} obras -> todos, {} obras -> intro".format(
            len(new_rows), len(main_updates), to_intro))
    return len(new_rows), len(main_updates), to_intro


def main():
    import json
    import os
    import gspread
    from google.oauth2.service_account import Credentials
    from main import SHEET_ID

    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    sync(gspread.authorize(creds).open_by_key(SHEET_ID))


if __name__ == "__main__":
    main()
