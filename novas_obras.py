"""Aba `Novas Obras`: obras que acabaram de entrar nos sites de scan, + aba `Sites` com
a lista de sites trackeados e como foi a ultima coleta de cada um.

Roda dentro do main.py na varredura completa (1x/hora) ou sozinho:
    python novas_obras.py              -> so coleta e imprime, sem planilha (teste local)
    python novas_obras.py --planilha   -> coleta e grava (precisa GOOGLE_CREDENTIALS_JSON;
                                          e o que o workflow `novas-obras` roda)

Regras:
  - Bloqueia shoujo/josei e BL/GL. Adulto/mature/ecchi passam (publico masculino). Romance
    so e bloqueado quando nao vem com genero de acao (action/fantasy/martial arts/adventure)
    nem com demografia masculina (shounen/seinen).
  - So entra obra NOVA: aparece com ate MAX_CAPS_NOVA capitulos e ano recente. Site que
    despeja catalogo traz obra antiga ja com 60, 100, 150 caps -> nem entra na aba.
  - Mesma obra em dois sites vira UMA linha (titulo normalizado); a coluna `Sites`
    acumula onde ela apareceu. `Visto em` nunca muda depois.
  - `Visto em` e a data em que a obra entrou no site quando o site informa (HiveToons, Kayn,
    OTL, Mist: janela de NEW_SITES_DAYS); senao, a hora da coleta.
  - `Peguei` e um checkbox que anda junto com a linha (a aba e reescrita e reordenada a cada
    rodada, entao pintar a linha na mao nao serve: a cor fica parada e a obra muda).
    Marcado, a linha inteira fica verde por formatacao condicional.
  - `Já tem vídeo`: o titulo bate com `obra`/`nomes_variantes` de algum video do `todos`.
  - `Capa` e =IMAGE(url). O #REF! que aparecia antes era a trava do Google para dados
    externos ("allow access"): alguem precisa clicar em Permitir acesso uma vez na planilha.
    Como =IMAGE le vazio, a URL e relida pela formula (ver `_read`).
"""
import json
import re
import time
from datetime import datetime, timezone, timedelta

import requests
from bs4 import BeautifulSoup

from comick import normalize

TAB = "Novas Obras"
SITES_TAB = "Sites"
OLD_TABS = ("novas_obras", "sites")   # nomes da primeira versao (11/10/2026)
HEADER = ["Peguei", "Capa", "Obra", "Capítulos", "Gêneros", "Ano", "Sites", "Visto em", "Já tem vídeo", "Link"]
KEYS = ["peguei", "capa", "obra", "capitulos", "generos", "ano", "sites", "visto_em", "ja_tem_video", "link"]
NCOLS = len(HEADER)
SITES_HEADER = ["Site", "URL", "Método", "Última coleta", "Obras lidas", "Status"]

MAX_CAPS_NOVA = 25       # obra que aparece com mais capitulos que isso e catalogo antigo
NEW_DAYS = 30            # quando o site informa a data de entrada, so pega obra recente
NEW_SITES_DAYS = 20      # HiveToons/Kayn/OTL/Mist: janela pela data real de entrada no site
MAX_ROWS = 500
COMIX_DETAIL_MAX = 20    # paginas de detalhe (generos) do comix por rodada
DATE_FMT = "%d/%m/%Y %H:%M"
BRT = timezone(timedelta(hours=-3))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}

BLOCKED = {"shoujo", "josei", "boys love", "girls love", "yaoi", "yuri", "shounen ai", "shoujo ai"}
ACTION = {"action", "fantasy", "martial arts", "adventure", "murim"}
CAPA_ROW_PX = 110        # altura das linhas da aba para a capa caber
MALE = {"shounen", "seinen"}


def _get(url, **kw):
    r = requests.get(url, headers=HEADERS, timeout=25, **kw)
    r.raise_for_status()
    return r


def _int(s):
    m = re.search(r"\d+", str(s or ""))
    return int(m.group()) if m else 0


def _dt(iso):
    try:
        return datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def _recent(iso, now, days=NEW_DAYS):
    dt = iso if isinstance(iso, datetime) else _dt(iso) if iso else None
    return dt is None or now - dt <= timedelta(days=days)


def _item(site, titulo, link, capa="", caps=0, generos="", ano="", data=None):
    """data: quando a obra entrou no site (datetime com fuso), se o site informa."""
    return {"site": site, "titulo": (titulo or "").strip(), "link": link, "capa": capa or "",
            "caps": int(caps or 0), "generos": generos or "", "ano": str(ano or ""), "data": data}


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
COMICK_EXCLUDES = ["romance", "yaoi", "yuri", "shoujo-ai", "shounen-ai"]


def comick(now):
    out = []
    for country in ("kr", "cn"):
        for s in _get("https://api.comick.dev/v1.0/search",
                      params={"sort": "created_at", "limit": 50, "country": country,
                              "excludes": COMICK_EXCLUDES,
                              "content_rating": ["safe", "suggestive", "erotica", "pornographic"]}).json():
            if not _recent(s.get("created_at"), now):
                continue
            covers = s.get("md_covers") or []
            out.append(_item("Comick", s.get("title"), f"https://comick.dev/comic/{s.get('slug')}",
                             f"https://meo.comick.pictures/{covers[0]['b2key']}" if covers else "",
                             _int(s.get("last_chapter")),
                             COMICK_DEMOGRAPHIC.get(s.get("demographic"), ""), s.get("year")))
        time.sleep(0.3)
    return out


_COMIX_DATA = re.compile(r'<script type="application/json" id="initial-data">(.*?)</script>', re.S)
_COMIX_AGE = re.compile(r"(\d+)\s*(mos|y|w|d|h|m|s)\b")


def _comix_get(url):
    """O Cloudflare do comix da 403 pro IP do GitHub Actions com `requests`; o curl_cffi
    imita o TLS do Chrome e costuma passar."""
    try:
        return _get(url)
    except requests.HTTPError as e:
        if e.response is None or e.response.status_code != 403:
            raise
        from curl_cffi import requests as creq
        r = creq.get(url, impersonate="chrome", timeout=25)
        r.raise_for_status()
        return r


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
    for key, val in _comix_queries(_comix_get("https://comix.to/home").text).items():
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
                             "", s.get("year")))
    for it in out[:detail_max]:
        try:
            for key, val in _comix_queries(_comix_get(it["link"]).text).items():
                if key.startswith('["manga","detail"'):
                    it["generos"] = _comix_generos(val)
            time.sleep(0.3)
        except Exception:
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


def _max_cap(chapters):
    return max((c.get("number") or 0 for c in chapters or []), default=0)


def hivetoons(now):
    """Mesma API da Vortex, mas a lista nao traz a data de criacao: ela vem do /api/post.
    Obra com capitulo demais e catalogo -> entra sem data (so atualiza linha ja existente)."""
    api = "https://api.hivetoons.org/api"
    d = _get(f"{api}/query", params={"page": 1, "perPage": 30, "orderBy": "createdAt",
                                     "orderDirection": "desc"}).json()
    out = []
    for p in d.get("posts", []):
        if (p.get("seriesType") or "").upper() not in ("MANHWA", "MANHUA"):
            continue
        caps, criado = _max_cap(p.get("chapters")), None
        if caps <= MAX_CAPS_NOVA:
            criado = _dt((_get(f"{api}/post", params={"postId": p.get("id")}).json().get("post") or {})
                         .get("createdAt"))
            time.sleep(0.3)
            if not _recent(criado, now, NEW_SITES_DAYS):
                continue
        out.append(_item("HiveToons", p.get("postTitle"), f"https://hivetoons.org/series/{p.get('slug')}",
                         p.get("featuredImage"), caps,
                         ", ".join(g.get("name", "") for g in p.get("genres") or []), data=criado))
    return out


def _cuid_date(cuid):
    """id cuid = 'c' + timestamp em ms (base36, 8 chars). A Kayn nao expoe a data de criacao
    da obra, mas ela esta no proprio id."""
    try:
        return datetime.fromtimestamp(int(str(cuid)[1:9], 36) / 1000, timezone.utc)
    except ValueError:
        return None


def kayn(now):
    out = []
    for s in _get("https://kaynscans.com/api/series", params={"sort": "newest", "limit": 40}).json().get("data", []):
        criado = _cuid_date(s.get("id"))
        if s.get("type") not in ("MANHWA", "MANHUA", "WEBTOON") or not _recent(criado, now, NEW_SITES_DAYS):
            continue
        out.append(_item("KaynScans", s.get("title"), f"https://kaynscans.com/series/comic/{s.get('urlSlug')}",
                         "https://kaynscans.com" + (s.get("coverImage") or ""), _max_cap(s.get("chapters")),
                         ", ".join(g["genre"]["slug"].replace("-", " ").title()
                                   for g in s.get("genres") or [] if g.get("genre")), data=criado))
    return out


def _cap_order(href):
    """'/read/x/20-5' -> (20, 5): ordena capitulo pelo numero, nao pelo texto."""
    return tuple(int(n) for n in re.findall(r"\d+", href.rstrip("/").rsplit("/", 1)[-1])) or (10 ** 9,)


def otl(now):
    """Site estatico (Astro) com poucas obras. O card traz tipo e capitulos; generos e ano
    vem do JSON-LD da obra e a data de entrada e o datePublished do primeiro capitulo."""
    base = "https://otl.moe"
    out = []
    for li in BeautifulSoup(_get(f"{base}/series/").text, "html.parser").select("li[data-series-item]"):
        a = li.select_one('a[href^="/series/"]')
        badges = [t for t in (s.get_text(strip=True) for s in li.select("span")) if t]
        if not a or not badges or badges[0].lower() not in ("manhwa", "manhua"):
            continue
        img = li.select_one("img[src]")
        it = _item("OTL", li.get("data-series-title"), base + a["href"], base + img["src"] if img else "",
                   caps=_int(badges[-1]))
        if it["caps"] <= MAX_CAPS_NOVA:
            page = BeautifulSoup(_get(it["link"]).text, "html.parser")
            for ld in page.select('script[type="application/ld+json"]'):
                info = json.loads(ld.string or "{}")
                if info.get("@type") == "BookSeries":
                    it["generos"] = ", ".join(info.get("genre") or [])
                    it["ano"] = str(info.get("datePublished") or "")[:4]
            caps = sorted({c["href"] for c in page.select('a[href^="/read/"]')}, key=_cap_order)
            if caps:
                m = re.search(r'"datePublished":"([^"]+)"', _get(base + caps[0]).text)
                it["data"] = _dt(m.group(1)) if m else None
            time.sleep(0.3)
            if not _recent(it["data"], now, NEW_SITES_DAYS):
                continue
        out.append(it)
    return out


_REL_AGE = re.compile(r"(\d+|an?|one)\s*(second|minute|hour|day|week|month|year)s?\s+ago", re.I)
_AGE_UNIT = {"second": 1 / 86400, "minute": 1 / 1440, "hour": 1 / 24, "day": 1, "week": 7,
             "month": 30, "year": 365}


def _mist_date(txt, now):
    """'15 hours ago' / '1 day ago' / 'Oct 22, 2026' -> datetime."""
    txt = (txt or "").strip()
    m = _REL_AGE.search(txt)
    if m:
        n = int(m.group(1)) if m.group(1).isdigit() else 1
        return now - timedelta(days=n * _AGE_UNIT[m.group(2).lower()])
    try:
        return datetime.strptime(txt, "%b %d, %Y").replace(tzinfo=BRT)
    except ValueError:
        return None


_MIST_CAPA = re.compile(r"url=(?:https?://)?([^&)\s]+)")


def mist(now):
    """Sem API. A pagina /latest/ lista todas as obras pela ultima atualizacao; obra que
    entrou nos ultimos dias tem capitulo recente, entao so essas abrem a pagina da obra
    para ler a data do capitulo 1 (atributo `d` do link)."""
    base = "https://mistscans.com"
    out = []
    for card in BeautifulSoup(_get(f"{base}/latest/").text, "html.parser").select(".latest-poster"):
        a = card.select_one("a[title]")
        chapters = card.select('a[href*="/chapter/"]')
        badges = [s.get_text(strip=True).lower() for s in a.select("span")] if a else []
        if not a or not chapters or not {"manhwa", "manhua", "mangatoon"} & set(badges):
            continue
        if not _recent(_mist_date(chapters[0].get("d"), now), now, NEW_SITES_DAYS):
            continue
        generos = [g.get("title", "") for g in card.select('a[href*="genre="]')]
        # a capa e AVIF, que o =IMAGE do Google nao abre: o proprio wsrv.nl do site converte em jpg
        capa = _MIST_CAPA.search(a.get("style") or "")
        it = _item("MistScans", a.get("title"), base + a["href"],
                   f"https://wsrv.nl/?url={capa.group(1)}&w=240&output=jpg" if capa else "",
                   caps=_int(chapters[0].get("title")), generos=", ".join(generos))
        if it["caps"] <= MAX_CAPS_NOVA:
            # a[d]: o botao "ler capitulo 1" do topo tambem aponta pro capitulo, mas sem data
            caps = BeautifulSoup(_get(it["link"]).text, "html.parser").select('a[href*="/chapter/"][d]')
            primeiro = min(caps, key=lambda c: _int(c.get("title")), default=None)
            it["data"] = _mist_date(primeiro.get("d"), now) if primeiro else None
            time.sleep(0.3)
            if not _recent(it["data"], now, NEW_SITES_DAYS):
                continue
        out.append(it)
    return out


SITES = [
    ("AsuraScans", "https://asurascans.com", "API", asura),
    ("Comick", "https://comick.dev", "API", comick),
    ("Comix", "https://comix.to", "HTML (dados embutidos)", comix),
    ("HiveToons", "https://hivetoons.org", "API", hivetoons),
    ("KaynScans", "https://kaynscans.com", "API", kayn),
    ("MadaraScans", "https://madarascans.net", "HTML",
     lambda now: _mangareader("MadaraScans", "https://madarascans.net/series/?order=latest")),
    ("MangaRead", "https://www.mangaread.org", "HTML",
     lambda now: _wp_manga("MangaRead", "https://www.mangaread.org/manga/?m_orderby=new-manga")),
    ("ManhwaTop", "https://manhwatop.com", "HTML",
     lambda now: _wp_manga("ManhwaTop", "https://manhwatop.com/manga/?m_orderby=new-manga")),
    ("MistScans", "https://mistscans.com", "HTML", mist),
    ("OTL", "https://otl.moe", "HTML", otl),
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
    gens = {normalize(g) for g in it["generos"].split(",") if g.strip()}
    if gens & BLOCKED:
        return True
    return "romance" in gens and not (gens & (ACTION | MALE))


def is_new(it, now):
    """Obra nova de verdade: chega no site com poucos capitulos e ano recente. Site que
    despeja catalogo traz obra antiga ja com 60, 100, 150 caps -> fica de fora."""
    if it["caps"] > MAX_CAPS_NOVA:
        return False
    return not (it["ano"].isdigit() and int(it["ano"]) < now.year - 1)


def video_titles(todos_rows):
    """Titulos normalizados que ja tem video no `todos` (obra + nomes_variantes)."""
    out = set()
    for r in todos_rows[1:]:
        for name in [r[1] if len(r) > 1 else ""] + ((r[7] if len(r) > 7 else "").split(" | ")):
            n = normalize(name)
            if n:
                out.add(n)
    return out


def merge(existing, itens, now, com_video):
    """existing: dicts lidos da aba. Devolve a lista nova de dicts (ordem: visto_em desc).
    Obra ja na aba so atualiza capitulos/sites; obra nova so entra se passar no is_new."""
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
        if not is_new(it, now):
            continue
        visto = min(it["data"], now).astimezone(BRT).strftime(DATE_FMT) if it["data"] else stamp
        by_key[key] = {
            "peguei": "FALSE", "capa": it["capa"], "obra": it["titulo"], "capitulos": it["caps"] or "",
            "generos": it["generos"], "ano": it["ano"], "sites": it["site"], "visto_em": visto,
            "ja_tem_video": "", "link": it["link"],
        }
    rows = list(by_key.values())
    for r in rows:
        r["ja_tem_video"] = "Sim" if normalize(r["obra"]) in com_video else ""

    def when(r):
        try:
            return datetime.strptime(r["visto_em"], DATE_FMT)
        except ValueError:
            return datetime.min
    rows.sort(key=when, reverse=True)
    return rows[:MAX_ROWS]


# ---------------------------------------------------------------- planilha

HEADER_BG = {"red": 0.20, "green": 0.22, "blue": 0.25}
BAND = {"red": 0.96, "green": 0.97, "blue": 0.98}
GRAY = {"red": 0.45, "green": 0.45, "blue": 0.45}


def _style(spreadsheet, ws, widths, center_cols=(), link_col=None, extra=None):
    """extra: funcao sheetId -> requests a mais, aplicadas so quando a aba e criada."""
    sid, n = ws.id, len(widths)

    def cols(c0, c1):
        return {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": c0, "endColumnIndex": c1}

    reqs = [
        {"updateSheetProperties": {"properties": {"sheetId": sid, "gridProperties": {"frozenRowCount": 1}},
                                   "fields": "gridProperties.frozenRowCount"}},
        {"repeatCell": {"range": cols(0, n),
                        "cell": {"userEnteredFormat": {"verticalAlignment": "MIDDLE", "wrapStrategy": "CLIP"}},
                        "fields": "userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy"}},
        {"repeatCell": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1},
                        "cell": {"userEnteredFormat": {
                            "verticalAlignment": "MIDDLE",
                            "textFormat": {"bold": True, "foregroundColor": {"red": 1, "green": 1, "blue": 1}}}},
                        "fields": "userEnteredFormat.verticalAlignment,userEnteredFormat.textFormat.bold,"
                                  "userEnteredFormat.textFormat.foregroundColor"}},
        {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "ROWS", "startIndex": 0, "endIndex": 1},
                                       "properties": {"pixelSize": 32}, "fields": "pixelSize"}},
        {"addBanding": {"bandedRange": {"range": {"sheetId": sid, "startRowIndex": 0, "startColumnIndex": 0,
                                                  "endColumnIndex": n},
                                        "rowProperties": {"headerColor": HEADER_BG,
                                                          "firstBandColor": {"red": 1, "green": 1, "blue": 1},
                                                          "secondBandColor": BAND}}}},
    ]
    for i, w in enumerate(widths):
        reqs.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": i, "endIndex": i + 1},
            "properties": {"pixelSize": w}, "fields": "pixelSize"}})
    for c in center_cols:
        reqs.append({"repeatCell": {"range": cols(c, c + 1),
                                    "cell": {"userEnteredFormat": {"horizontalAlignment": "CENTER"}},
                                    "fields": "userEnteredFormat.horizontalAlignment"}})
    if link_col is not None:
        # URL fica azul e sublinhada sozinha; aqui vira cinza e sem sublinhado
        reqs.append({"repeatCell": {"range": cols(link_col, link_col + 1),
                                    "cell": {"userEnteredFormat": {"textFormat": {
                                        "underline": False, "foregroundColor": GRAY}}},
                                    "fields": "userEnteredFormat.textFormat.underline,"
                                              "userEnteredFormat.textFormat.foregroundColor"}})
    spreadsheet.batch_update({"requests": reqs + (extra(sid) if extra else [])})


def _ensure_tab(spreadsheet, title, header, rows=200, **style):
    """Cria a aba formatada. Se o cabecalho mudou (versao antiga da aba), recria do zero;
    quem precisa dos dados antigos le antes (ver `sync`)."""
    import gspread
    try:
        ws = spreadsheet.worksheet(title)
        if ws.row_values(1) == header:
            return ws
        spreadsheet.del_worksheet(ws)
    except gspread.WorksheetNotFound:
        pass
    ws = spreadsheet.add_worksheet(title=title, rows=rows, cols=len(header))
    ws.update([header], "A1")
    _style(spreadsheet, ws, **style)
    return ws


def _novas_obras_rules(sid):
    """Checkbox na coluna Peguei + linha verde quando marcado (a regra segue o valor, entao
    a cor acompanha a obra quando a aba e reordenada) + linhas altas para a capa."""
    body = {"sheetId": sid, "startRowIndex": 1, "endRowIndex": MAX_ROWS + 1}
    return [
        {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "ROWS", "startIndex": 1,
                                                 "endIndex": MAX_ROWS + 1},
                                       "properties": {"pixelSize": CAPA_ROW_PX}, "fields": "pixelSize"}},
        {"setDataValidation": {"range": {**body, "startColumnIndex": 0, "endColumnIndex": 1},
                               "rule": {"condition": {"type": "BOOLEAN"}}}},
        {"addConditionalFormatRule": {"index": 0, "rule": {
            "ranges": [{**body, "startColumnIndex": 0, "endColumnIndex": NCOLS}],
            "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=$A2=TRUE"}]},
                            "format": {"backgroundColor": {"red": 0.85, "green": 0.92, "blue": 0.83}}}}}},
    ]


_IMAGE_URL = re.compile(r'=IMAGE\("([^"]+)"')


def _read(ws):
    """Le pelo nome da coluna, nao pela posicao: assim a aba antiga (sem `Peguei`) migra sem
    perder nada."""
    vals = ws.get_all_values()
    if not vals:
        return []
    col = {h: i for i, h in enumerate(vals[0])}
    if "Capa" in col:   # =IMAGE() le vazio; a URL so existe na formula
        formulas = ws.col_values(col["Capa"] + 1, value_render_option="FORMULA")
        for i, r in enumerate(vals):
            m = _IMAGE_URL.match(formulas[i] if i < len(formulas) else "")
            r[col["Capa"]:col["Capa"] + 1] = [m.group(1) if m else ""]
    out = []
    for r in vals[1:]:
        d = {k: (r[col[h]] if h in col and col[h] < len(r) else "") for h, k in zip(HEADER, KEYS)}
        if d["obra"]:
            out.append(d)
    return out


def _row(d):
    # apostrofo = texto puro no USER_ENTERED: `obra` nunca vira formula/numero e `visto_em`
    # nao vira data (que voltaria em outro formato na proxima leitura e quebraria a ordem)
    row = [d[k] for k in KEYS]
    row[KEYS.index("peguei")] = "TRUE" if str(d["peguei"]).upper() == "TRUE" else "FALSE"
    row[KEYS.index("capa")] = f'=IMAGE("{d["capa"].replace(chr(34), "%22")}")' if d["capa"] else ""
    row[KEYS.index("obra")] = "'" + d["obra"]
    row[KEYS.index("visto_em")] = "'" + d["visto_em"]
    return row


def sync(spreadsheet, todos_rows, now_utc=None):
    import gspread
    now = now_utc or datetime.now(timezone.utc)
    for ws in spreadsheet.worksheets():
        if ws.title in OLD_TABS:
            spreadsheet.del_worksheet(ws)
    itens, status = collect(now)   # a parte lenta vem antes de mexer na aba
    try:
        existing = _read(spreadsheet.worksheet(TAB))   # antes do _ensure_tab, que pode recriar a aba
    except gspread.WorksheetNotFound:
        existing = []
    rows = merge(existing, itens, now, video_titles(todos_rows))
    ws = _ensure_tab(spreadsheet, TAB, HEADER, rows=MAX_ROWS + 1,
                     widths=[65, 80, 340, 85, 260, 60, 220, 125, 110, 300],
                     center_cols=(0, 1, 3, 5, 7, 8), link_col=9, extra=_novas_obras_rules)

    if ws.row_count < len(rows) + 1:
        ws.add_rows(len(rows) + 1 - ws.row_count)
    ws.batch_clear([f"A2:{chr(64 + NCOLS)}"])
    if rows:
        ws.update([_row(d) for d in rows], "A2", value_input_option="USER_ENTERED")

    sites_ws = _ensure_tab(spreadsheet, SITES_TAB, SITES_HEADER, widths=[130, 230, 170, 130, 100, 300],
                           center_cols=(3, 4), link_col=1)
    stamp = now.astimezone(BRT).strftime(DATE_FMT)
    sites_ws.batch_clear(["A2:F"])
    sites_ws.update([[n, u, m, "'" + stamp, status[n][0], status[n][1]] for n, u, m, _ in SITES], "A2",
                    value_input_option="USER_ENTERED")
    erros = [n for n, (_, st) in status.items() if st != "OK"]
    print(f"[novas_obras] {len(itens)} lidas em {len(SITES)} sites, {len(rows)} na aba"
          + (f", ERRO em: {', '.join(erros)}" if erros else ""))


if __name__ == "__main__":
    import os
    import sys
    if "--planilha" in sys.argv:
        import gspread
        from google.oauth2.service_account import Credentials
        creds = Credentials.from_service_account_info(
            json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )
        ss = gspread.authorize(creds).open_by_key("1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0")
        sync(ss, ss.worksheet("todos").get_all_values())
        sys.exit()
    now = datetime.now(timezone.utc)
    itens, status = collect(now)
    for n, (qtd, st) in status.items():
        print(f"{n:14} {qtd:4}  {st}")
    rows = merge([], itens, now, set())
    print(f"\n{len(rows)} obras depois do filtro/dedup")
    for r in rows[:15]:
        print(f"  {r['obra'][:55]:55} caps={r['capitulos']!s:4} {r['sites']} | {r['generos'][:50]}")
