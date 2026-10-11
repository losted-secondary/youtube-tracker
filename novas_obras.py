"""Aba `novas_obras`: obras que acabaram de entrar nos sites de scan, + aba `sites` com
a lista de sites trackeados e como foi a ultima coleta de cada um.

Roda dentro do main.py na varredura completa (1x/hora) ou sozinho:
    python novas_obras.py      -> so coleta e imprime, sem planilha (teste local)

Regras:
  - Bloqueia mature/adulto, shoujo/josei e BL/GL. Ecchi passa. Romance so e bloqueado
    quando nao vem junto de genero de acao (action/fantasy/martial arts/adventure).
  - Site que despeja catalogo: obra que ENTRA na aba ja com REPOST_MIN_CAPS capitulos ou
    mais quase sempre e obra antiga trazida de outro site, nao lancamento -> tipo REPOST?.
    Quando o site informa o ano e ele e velho, o tipo vira ANTIGA.
  - Mesma obra em dois sites vira UMA linha (titulo normalizado); a coluna `sites`
    acumula onde ela apareceu. `caps_ao_entrar` e `visto_em` nunca mudam depois.
  - `ja_tem_video`: o titulo bate com `obra`/`nomes_variantes` de algum video do `todos`.
"""
import json
import re
import time
from datetime import datetime, timezone, timedelta

import requests
from bs4 import BeautifulSoup

from comick import normalize

TAB = "novas_obras"
SITES_TAB = "sites"
HEADER = ["capa", "obra", "tipo", "capitulos", "caps_ao_entrar", "generos", "ano",
          "sites", "link", "visto_em", "ja_tem_video"]
NCOLS = len(HEADER)
SITES_HEADER = ["site", "url", "metodo", "ultima_coleta", "obras_lidas", "status"]

REPOST_MIN_CAPS = 30
NEW_DAYS = 30            # quando o site informa a data de entrada, so pega obra recente
MAX_ROWS = 500
COMIX_DETAIL_MAX = 20    # paginas de detalhe (generos) do comix por rodada
DATE_FMT = "%d/%m/%Y %H:%M"
BRT = timezone(timedelta(hours=-3))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}

BLOCKED = {"mature", "adult", "smut", "hentai", "erotica", "pornographic",
           "shoujo", "josei", "boys love", "girls love", "yaoi", "yuri",
           "shounen ai", "shoujo ai"}
ACTION = {"action", "fantasy", "martial arts", "adventure", "murim"}


def _get(url, **kw):
    r = requests.get(url, headers=HEADERS, timeout=25, **kw)
    r.raise_for_status()
    return r


def _int(s):
    m = re.search(r"\d+", str(s or ""))
    return int(m.group()) if m else 0


def _recent(iso, now):
    if not iso:
        return True
    try:
        dt = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except ValueError:
        return True
    return now - dt <= timedelta(days=NEW_DAYS)


def _item(site, titulo, link, capa="", caps=0, generos="", ano="", adulto=False):
    return {"site": site, "titulo": (titulo or "").strip(), "link": link, "capa": capa or "",
            "caps": int(caps or 0), "generos": generos or "", "ano": str(ano or ""), "adulto": adulto}


# ---------------------------------------------------------------- coletores por site

def asura(now):
    d = _get("https://api.asurascans.com/api/series",
             params={"page": 1, "order": "latest", "count": 50}).json()
    out = []
    for s in d.get("data") or d.get("series") or []:
        if s.get("type") not in ("manhwa", "manhua") or not _recent(s.get("created_at"), now):
            continue
        out.append(_item("AsuraScans", s.get("title"),
                         "https://asurascans.com" + (s.get("public_url") or f"/comics/{s.get('slug')}"),
                         s.get("cover"), s.get("chapter_count"),
                         ", ".join(g.get("name", "") for g in s.get("genres") or []),
                         s.get("release_year")))
    return out


COMICK_DEMOGRAPHIC = {1: "Shounen", 2: "Shoujo", 3: "Seinen", 4: "Josei"}
# a busca do comick nao devolve os generos, mas aceita excluir por genero. Aqui romance
# sai inteiro (sem a excecao de acao), porque nao da pra ver o resto dos generos.
COMICK_EXCLUDES = ["romance", "yaoi", "yuri", "shoujo-ai", "shounen-ai", "smut", "adult", "mature", "hentai"]


def comick(now):
    out = []
    for country in ("kr", "cn"):
        for s in _get("https://api.comick.dev/v1.0/search",
                      params={"sort": "created_at", "limit": 50, "country": country,
                              "excludes": COMICK_EXCLUDES,
                              "content_rating": ["safe", "suggestive"]}).json():
            if not _recent(s.get("created_at"), now):
                continue
            covers = s.get("md_covers") or []
            out.append(_item("Comick", s.get("title"), f"https://comick.dev/comic/{s.get('slug')}",
                             f"https://meo.comick.pictures/{covers[0]['b2key']}" if covers else "",
                             _int(s.get("last_chapter")),
                             COMICK_DEMOGRAPHIC.get(s.get("demographic"), ""), s.get("year"),
                             adulto=s.get("content_rating") in ("erotica", "pornographic")))
        time.sleep(0.3)
    return out


_COMIX_DATA = re.compile(r'<script type="application/json" id="initial-data">(.*?)</script>', re.S)
_COMIX_AGE = re.compile(r"(\d+)\s*(mos|y|w|d|h|m|s)\b")


def _comix_queries(html):
    m = _COMIX_DATA.search(html)
    return json.loads(m.group(1)).get("queries", {}) if m else {}


def _comix_recent(age):
    """'3d ago' / '2mos ago' / '1y ago' -> entrou no site ha no maximo NEW_DAYS."""
    m = _COMIX_AGE.search(age or "")
    if not m:
        return True
    n, unit = int(m.group(1)), m.group(2)
    return unit not in ("y", "mos") or (unit == "mos" and n * 30 <= NEW_DAYS)


def _comix_generos(s):
    return ", ".join(g.get("title", "") for g in (s.get("genres") or []) + (s.get("demographics") or []))


def comix(now, detail_max=COMIX_DETAIL_MAX):
    """comix.to: a API exige token assinado, mas toda pagina ja vem com os dados no
    <script id="initial-data">. A home traz recem-adicionadas, atualizadas, em alta e mais
    seguidas; os generos so existem na pagina da obra."""
    out, seen = [], set()
    for key, val in _comix_queries(_get("https://comix.to/home").text).items():
        if not key.startswith('["manga"'):
            continue
        for s in (val.get("items", []) if isinstance(val, dict) else val) or []:
            url = s.get("url") or ""
            if (s.get("type") not in ("manhwa", "manhua") or url in seen
                    or not _comix_recent(s.get("createdAtFormatted"))):
                continue
            seen.add(url)
            out.append(_item("Comix", s.get("title"), "https://comix.to" + url,
                             (s.get("poster") or {}).get("medium", ""), s.get("latestChapter"),
                             "", s.get("year"),
                             adulto=s.get("contentRating") in ("erotica", "pornographic")))
    for it in out[:detail_max]:
        try:
            for key, val in _comix_queries(_get(it["link"]).text).items():
                if key.startswith('["manga","detail"'):
                    it["generos"] = _comix_generos(val)
            time.sleep(0.3)
        except requests.RequestException:
            pass
    return out


def qimanga(now):
    d = _get("https://api.qimanga.com/api/v1/series", params={"page": 1, "perPage": 40}).json()
    return [_item("QiManga", s.get("title"), f"https://qimanga.com/series/{s.get('slug')}", s.get("cover"))
            for s in d.get("data", []) if _recent(s.get("createdAt"), now)]


def vortex(now):
    d = _get("https://api.vortexscans.org/api/query",
             params={"page": 1, "perPage": 30, "orderBy": "createdAt", "orderDirection": "desc"}).json()
    return [_item("VortexScans", p.get("postTitle"), f"https://vortexscans.org/series/{p.get('slug')}",
                  p.get("featuredImage"), max((c.get("number") or 0 for c in p.get("chapters") or []), default=0),
                  ", ".join(g.get("name", "") for g in p.get("genres") or []))
            for p in d.get("posts", [])]


def _img(card):
    im = card.select_one("img")
    return (im.get("data-src") or im.get("src") or "") if im else ""


def _wp_manga(site, url):
    """Tema Madara do WordPress (/manga/?m_orderby=new-manga)."""
    out = []
    for c in BeautifulSoup(_get(url).text, "html.parser").select(".page-item-detail"):
        a = c.select_one("h3 a, .post-title a")
        if a:
            ch = c.select_one(".chapter a")
            out.append(_item(site, a.get_text(strip=True), a.get("href"), _img(c), _int(ch and ch.get_text())))
    return out


def _mangareader(site, url):
    """Tema MangaReader do WordPress (cards .bsx)."""
    out = []
    for c in BeautifulSoup(_get(url).text, "html.parser").select(".bsx"):
        a, tt = c.select_one("a[href]"), c.select_one(".tt")
        if a:
            ch = c.select_one(".epxs")
            out.append(_item(site, tt.get_text(strip=True) if tt else a.get("title"), a.get("href"),
                             _img(c), _int(ch and ch.get_text())))
    return out


SITES = [
    ("AsuraScans", "https://asurascans.com", "API", asura),
    ("Comick", "https://comick.dev", "API", comick),
    ("Comix", "https://comix.to", "HTML (dados embutidos)", comix),
    ("MadaraScans", "https://madarascans.net", "HTML",
     lambda now: _mangareader("MadaraScans", "https://madarascans.net/series/?order=latest")),
    ("MangaRead", "https://www.mangaread.org", "HTML",
     lambda now: _wp_manga("MangaRead", "https://www.mangaread.org/manga/?m_orderby=new-manga")),
    ("ManhwaTop", "https://manhwatop.com", "HTML",
     lambda now: _wp_manga("ManhwaTop", "https://manhwatop.com/manga/?m_orderby=new-manga")),
    ("QiManga", "https://qimanga.com", "API", qimanga),
    ("ThunderScans", "https://en-thunderscans.com", "HTML",
     lambda now: _mangareader("ThunderScans", "https://en-thunderscans.com/project/?order=latest")),
    ("VortexScans", "https://vortexscans.org", "API", vortex),
]


def collect(now):
    """-> (itens de todos os sites, status por site)."""
    itens, status = [], {}
    for nome, _, _, fn in SITES:
        try:
            got = fn(now)
            itens += got
            status[nome] = (len(got), "OK")
        except Exception as e:
            status[nome] = (0, f"ERRO: {str(e)[:80]}")
    return itens, status


# ---------------------------------------------------------------- regras

def blocked(it):
    if it["adulto"]:
        return True
    gens = {normalize(g) for g in it["generos"].split(",") if g.strip()}
    if gens & BLOCKED:
        return True
    return "romance" in gens and not (gens & ACTION)


def classify(caps, ano, now):
    if ano.isdigit() and int(ano) < now.year - 1:
        return "ANTIGA"
    return "REPOST?" if caps >= REPOST_MIN_CAPS else "NOVA"


def video_titles(todos_rows):
    """Titulos normalizados que ja tem video no `todos` (obra + nomes_variantes)."""
    out = set()
    for r in todos_rows[1:]:
        for name in [r[1] if len(r) > 1 else ""] + ((r[7] if len(r) > 7 else "").split(" | ")):
            n = normalize(name)
            if n:
                out.add(n)
    return out


def _image_url(formula):
    m = re.match(r'=IMAGE\("([^"]+)"', formula or "", re.I)
    return m.group(1) if m else ""


def merge(existing, itens, now, com_video):
    """existing: dicts lidos da aba. Devolve a lista nova de dicts (ordem: visto_em desc)."""
    by_key = {normalize(e["obra"]): e for e in existing if e["obra"]}
    stamp = now.astimezone(BRT).strftime(DATE_FMT)
    for it in itens:
        key = normalize(it["titulo"])
        if not key or blocked(it):
            continue
        e = by_key.get(key)
        if e:
            e["capitulos"] = max(_int(e["capitulos"]), it["caps"]) or ""
            sites = [s for s in e["sites"].split(", ") if s]
            if it["site"] not in sites:
                e["sites"] = ", ".join(sites + [it["site"]])
            for f, v in (("generos", it["generos"]), ("ano", it["ano"]), ("capa", it["capa"])):
                if not e[f] and v:
                    e[f] = v
            continue
        by_key[key] = {
            "capa": it["capa"], "obra": it["titulo"], "tipo": classify(it["caps"], it["ano"], now),
            "capitulos": it["caps"] or "", "caps_ao_entrar": it["caps"] or "",
            "generos": it["generos"], "ano": it["ano"], "sites": it["site"], "link": it["link"],
            "visto_em": stamp, "ja_tem_video": "",
        }
    rows = list(by_key.values())
    for r in rows:
        r["ja_tem_video"] = "SIM" if normalize(r["obra"]) in com_video else ""

    def when(r):
        try:
            return datetime.strptime(r["visto_em"].replace(" - ", " "), DATE_FMT)
        except ValueError:
            return datetime.min
    rows.sort(key=when, reverse=True)
    return rows[:MAX_ROWS]


# ---------------------------------------------------------------- planilha

def _ensure_tab(spreadsheet, title, header, image_rows=False):
    import gspread
    try:
        return spreadsheet.worksheet(title)
    except gspread.WorksheetNotFound:
        ws = spreadsheet.add_worksheet(title=title, rows=200, cols=len(header))
        ws.update([header], "A1")
        reqs = [
            {"updateSheetProperties": {"properties": {"sheetId": ws.id, "gridProperties": {"frozenRowCount": 1}},
                                       "fields": "gridProperties.frozenRowCount"}},
            {"repeatCell": {"range": {"sheetId": ws.id, "startRowIndex": 0, "endRowIndex": 1},
                            "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
                            "fields": "userEnteredFormat.textFormat.bold"}},
        ]
        if image_rows:
            reqs += [
                {"updateDimensionProperties": {"range": {"sheetId": ws.id, "dimension": "ROWS", "startIndex": 1},
                                               "properties": {"pixelSize": 110}, "fields": "pixelSize"}},
                {"updateDimensionProperties": {"range": {"sheetId": ws.id, "dimension": "COLUMNS",
                                                         "startIndex": 0, "endIndex": 2},
                                               "properties": {"pixelSize": 260}, "fields": "pixelSize"}},
                {"updateDimensionProperties": {"range": {"sheetId": ws.id, "dimension": "COLUMNS",
                                                         "startIndex": 0, "endIndex": 1},
                                               "properties": {"pixelSize": 80}, "fields": "pixelSize"}},
            ]
        spreadsheet.batch_update({"requests": reqs})
        return ws


def _read(spreadsheet, ws):
    shown = ws.get_all_values()
    formulas = spreadsheet.values_get(f"'{TAB}'!A2:A", params={"valueRenderOption": "FORMULA"}).get("values", [])
    out = []
    for i, r in enumerate(shown[1:]):
        r = (r + [""] * NCOLS)[:NCOLS]
        d = dict(zip(HEADER, r))
        d["capa"] = _image_url(formulas[i][0] if i < len(formulas) and formulas[i] else "")
        out.append(d)
    return out


def _row(d):
    capa = f'=IMAGE("{d["capa"]}")' if d["capa"] else ""
    # apostrofo = texto puro no USER_ENTERED: `obra` nunca vira formula/numero e `visto_em`
    # nao vira data (que voltaria em outro formato na proxima leitura e quebraria a ordem)
    row = [capa, "'" + d["obra"]] + [d[h] for h in HEADER[2:]]
    row[HEADER.index("visto_em")] = "'" + d["visto_em"]
    return row


def sync(spreadsheet, todos_rows, now_utc=None):
    now = now_utc or datetime.now(timezone.utc)
    ws = _ensure_tab(spreadsheet, TAB, HEADER, image_rows=True)
    itens, status = collect(now)
    rows = merge(_read(spreadsheet, ws), itens, now, video_titles(todos_rows))

    if ws.row_count < len(rows) + 1:
        ws.add_rows(len(rows) + 1 - ws.row_count)
    ws.batch_clear([f"A2:{chr(64 + NCOLS)}"])
    if rows:
        ws.update([_row(d) for d in rows], "A2", value_input_option="USER_ENTERED")

    sites_ws = _ensure_tab(spreadsheet, SITES_TAB, SITES_HEADER)
    stamp = now.astimezone(BRT).strftime(DATE_FMT)
    sites_ws.batch_clear(["A2:F"])
    sites_ws.update([[n, u, m, stamp, status[n][0], status[n][1]] for n, u, m, _ in SITES], "A2")
    erros = [n for n, (_, st) in status.items() if st != "OK"]
    print(f"[novas_obras] {len(itens)} lidas em {len(SITES)} sites, {len(rows)} na aba"
          + (f", ERRO em: {', '.join(erros)}" if erros else ""))


if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    itens, status = collect(now)
    for n, (qtd, st) in status.items():
        print(f"{n:14} {qtd:4}  {st}")
    rows = merge([], itens, now, set())
    print(f"\n{len(rows)} obras depois do filtro/dedup")
    for r in rows[:15]:
        print(f"  [{r['tipo']:7}] {r['obra'][:55]:55} caps={r['capitulos']!s:4} {r['sites']} | {r['generos'][:50]}")
