"""Caçador de Obras: acha obras boas para os canais e diz se ainda estão livres no YouTube.

    python cacador.py                 -> caça e grava artifacts/cacador/recomendadas.{csv,html}
    python cacador.py --planilha      -> idem + aba `Obras Recomendadas` (GOOGLE_CREDENTIALS_JSON)
    python cacador.py --max-yt 120    -> quantas obras checar no YouTube (as de maior nota)

Funil:
  1. GOSTO: a aba `todos` diz quais obras renderam (views ÷ mediana do mesmo canal, na mesma
     época). As melhores e as piores, com a sinopse do AniList, viram os exemplos que a IA usa
     para dar nota. Nada de achismo: o gosto é o resultado do nicho.
  2. POOL: (a) AniList, coreanas (Mamoru/Tobs), chinesas (Kamen) e japonesas (mangá), por
     tendência e popularidade, sem romance/BL/GL/shoujo/josei/adulto; (b) obras da `todos` que
     renderam e cujo último vídeo tem 6+ meses (dá para repostar).
  3. FILTRO: >= MIN_CAPS capítulos (estimado pela data de início quando ainda está saindo);
     sem vídeo nos nossos canais; sem vídeo de canal monitorado nos últimos 6 meses.
  4. NOTA: gpt-5.4-mini lê a premissa e dá 0-10 com os 7 ganchos (contraste, humilhação, aura,
     sistema, segredo, tensão, beleza) e os exemplos do passo 1.
  5. YOUTUBE: as melhores notas são pesquisadas no YouTube (página de busca, sem cota da API):
     LIVRE (ninguém fez recap longo), ESFRIOU (último recap 6+ meses), TOMADA (recap recente).
  6. SAÍDA: nota final = nota da IA + demanda provada (views de recaps antigos / popularidade).

Cache em artifacts/cacador/ (AniList 7 dias, YouTube 3 dias, notas para sempre por obra).
"""
import csv
import html
import io
import json
import math
import os
import re
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

import comick
from comick import normalize

SHEET_ID = "1ordgWcnAmJpxAVD8qXy0dXjhgqu5Y_g2LkJFnzxA9f0"
TAB_OUT = "Obras Recomendadas"
DIR = Path(__file__).parent / "artifacts" / "cacador"
MODELO = "gpt-5.4-mini"
MIN_CAPS = 15                 # ~1h30 de vídeo
ESFRIOU_DIAS = 180            # último vídeo há 6+ meses: pode repostar
NOSSOS = {"mamoru manhwa", "tobs manhwa"}   # nome do canal (normalizado) na coluna `canal`
CANAL_PAIS = {"KR": "Mamoru/Tobs", "CN": "Kamen", "JP": "Mangá"}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
BRT = timezone(timedelta(hours=-3))
GANCHOS_MD = Path(r"C:\Users\victo\Desktop\analytics-analyses\thumbs\plano\ganchos.md")

TAGS_FORA = ["Boys' Love", "Yuri", "Shoujo", "Josei"]
GENEROS_FORA = ["Romance", "Hentai"]
# (país, ordem, páginas de 50)
# (país, ordem, páginas de 50, filtro de data de início, rótulo)
POOLS = [("KR", "TRENDING_DESC", 4, None, "Em alta"), ("KR", "POPULARITY_DESC", 6, None, "Popular"),
         ("CN", "TRENDING_DESC", 3, None, "Em alta"), ("CN", "POPULARITY_DESC", 5, None, "Popular"),
         ("JP", "TRENDING_DESC", 4, None, "Em alta"), ("JP", "POPULARITY_DESC", 6, None, "Popular"),
         # obra NOVA: começou de 2025 para cá e já tem público
         ("KR", "POPULARITY_DESC", 3, ("depois", 20250101), "Nova"),
         ("CN", "POPULARITY_DESC", 3, ("depois", 20250101), "Nova"),
         ("JP", "POPULARITY_DESC", 3, ("depois", 20250101), "Nova"),
         # obra CLÁSSICA: começou antes de 2020 (muita gente nunca viu recap)
         ("KR", "POPULARITY_DESC", 4, ("antes", 20200101), "Clássica"),
         ("CN", "POPULARITY_DESC", 3, ("antes", 20200101), "Clássica"),
         ("JP", "POPULARITY_DESC", 4, ("antes", 20200101), "Clássica")]
ABA_MANHWA, ABA_MANHUA, ABA_MANGA = "Manhwa", "Manhua", "Mangá"     # uma página/aba por tipo
ABAS = (ABA_MANHWA, ABA_MANHUA, ABA_MANGA)
ABAS_ANTIGAS = ("Obras Recomendadas", "Manhwa e Manhua")


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- cache

def _cache(nome):
    p = DIR / f"{nome}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def _salva(nome, d):
    DIR.mkdir(parents=True, exist_ok=True)
    (DIR / f"{nome}.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")


def _fresco(entrada, dias):
    return entrada and time.time() - entrada.get("_t", 0) < dias * 86400


# ---------------------------------------------------------------- planilha (leitura pública)

def ler_aba(nome):
    r = requests.get(f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq",
                     params={"tqx": "out:csv", "sheet": nome}, timeout=60)
    r.raise_for_status()
    return list(csv.DictReader(io.StringIO(r.content.decode("utf-8"))))


def _views(s):
    d = re.sub(r"\D", "", s or "")
    return int(d) if d else 0


def _data_todos(s):
    try:
        return datetime.strptime((s or "").strip(), "%d/%m/%Y - %H:%M").replace(tzinfo=BRT)
    except ValueError:
        return None


def desempenho(todos, now):
    """-> {chave_normalizada: info} por obra. ratio = views ÷ mediana das views do MESMO canal
    entre vídeos postados até 45 dias antes/depois (vídeo novo ainda não juntou view). Vídeos
    com menos de 10 dias não entram na nota (não deu tempo), mas contam como cobertura."""
    vids = []
    for r in todos:
        dt = _data_todos(r.get("data_postado"))
        if not dt:
            continue
        vids.append({"obra": (r.get("obra") or "").strip(), "canal": r.get("canal", ""), "dt": dt,
                     "views": _views(r.get("viewers")), "link": r.get("link", ""),
                     "nomes": [p for n in [r.get("obra", "")] + (r.get("nomes_variantes") or "").split(" | ")
                               for p in [n] + (n.split(" / ") if " / " in n else [])]})
    por_canal = {}
    for v in vids:
        por_canal.setdefault(v["canal"], []).append(v)
    for lst in por_canal.values():
        for v in lst:
            viz = [o["views"] for o in lst if abs((o["dt"] - v["dt"]).days) <= 45 and o is not v]
            med = statistics.median(viz) if len(viz) >= 4 else None
            v["ratio"] = v["views"] / med if med and (now - v["dt"]).days >= 10 else None
    obras = {}
    for v in vids:
        if not v["obra"]:
            continue
        k = normalize(v["obra"])
        o = obras.setdefault(k, {"obra": v["obra"], "videos": [], "chaves": set()})
        o["videos"].append(v)
        o["chaves"].update(normalize(n) for n in v["nomes"] if normalize(n))
    for o in obras.values():
        rs = [v["ratio"] for v in o["videos"] if v["ratio"]]
        o["ratio"] = max(rs) if rs else None
        o["ultimo"] = max(v["dt"] for v in o["videos"])
        o["nossos"] = any(normalize(v["canal"]) in NOSSOS for v in o["videos"])
        nv = [v for v in o["videos"] if normalize(v["canal"]) in NOSSOS]
        o["nossos_ultimo"] = max(v["dt"] for v in nv) if nv else None
        o["nossos_canais"] = sorted({v["canal"] for v in nv})
        o["canais"] = sorted({v["canal"] for v in o["videos"]})
        o["max_views"] = max(v["views"] for v in o["videos"])
        melhor = max(o["videos"], key=lambda v: (v["ratio"] or 0, v["views"]))
        o["melhor"] = {"canal": melhor["canal"], "views": melhor["views"], "dt": melhor["dt"],
                       "ratio": melhor["ratio"], "link": melhor["link"]}
        o["nomes"] = [n for n in dict.fromkeys(n.strip() for v in o["videos"] for n in v["nomes"]) if n]
    return obras


class Indice:
    """acha a obra da planilha por QUALQUER nome, mesmo diferente: "The Magic Genius of the Marquis"
    (Tobs) = "The Magic Genius of the Marquis House" (AniList). Bate se o nome é igual, se as palavras
    de um estão todas no outro (3+ palavras) ou se 80% das palavras coincidem."""

    def __init__(self, obras):
        self.exato, self.tok, self.por_token = {}, {}, {}
        for o in obras.values():
            for k in o["chaves"]:
                self.exato.setdefault(k, []).append(o)
                ts = frozenset(_tokens(k))
                if len(ts) >= 2:
                    self.tok[k] = ts
                    for t in ts:
                        self.por_token.setdefault(t, set()).add(k)

    def achar(self, nomes):
        achou = {}
        for n in nomes:
            for o in self.exato.get(normalize(n), []):
                achou[id(o)] = o
            ts = set(_tokens(n))
            if len(ts) < 2:
                continue
            perto = set()
            for t in ts:
                perto |= self.por_token.get(t, set())
            for k in perto:
                ct = self.tok[k]
                inter, menor = len(ts & ct), min(len(ts), len(ct))
                maior = max(len(ts), len(ct))
                if (inter == menor and menor >= 3 and inter / maior >= 0.5) or inter / maior >= 0.8:
                    for o in self.exato[k]:
                        achou[id(o)] = o
        return list(achou.values())


def juntar(achadas):
    """a mesma obra pode estar na planilha com nomes diferentes (um por canal): vira uma só."""
    if not achadas:
        return None
    if len(achadas) == 1:
        return achadas[0]
    melhor = max(achadas, key=lambda o: ((o["melhor"]["ratio"] or 0), o["melhor"]["views"]))
    return {**melhor, "ratio": max((o["ratio"] or 0) for o in achadas) or None,
            "ultimo": max(o["ultimo"] for o in achadas), "nossos": any(o["nossos"] for o in achadas),
            "canais": sorted({c for o in achadas for c in o["canais"]}),
            "nomes": list(dict.fromkeys(n for o in achadas for n in o["nomes"])),
            "nossos_ultimo": max((o["nossos_ultimo"] for o in achadas if o.get("nossos_ultimo")), default=None),
            "nossos_canais": sorted({c for o in achadas for c in o.get("nossos_canais", [])})}


# ---------------------------------------------------------------- AniList

_ANI_CAMPOS = """id idMal countryOfOrigin title{romaji english native} synonyms chapters status genres
 tags{name rank} popularity averageScore startDate{year month day} siteUrl isAdult
 coverImage{large} description(asHtml:false)"""
_ultimo_ani = [0.0]


def _anilist(query, variables):
    for tentativa in range(6):
        espera = 2.2 - (time.time() - _ultimo_ani[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo_ani[0] = time.time()
        r = requests.post("https://graphql.anilist.co", json={"query": query, "variables": variables},
                          timeout=40)
        if r.status_code == 429:
            time.sleep(int(r.headers.get("Retry-After", 30)) + 1)
            continue
        if r.status_code >= 500:
            time.sleep(5 * (tentativa + 1))
            continue
        r.raise_for_status()
        return r.json()["data"]
    raise RuntimeError("AniList não respondeu")


def ani_pool(pais, ordem, pagina, cache, data=None):
    k = f"pool|{pais}|{ordem}|{pagina}" + (f"|{data[0]}{data[1]}" if data else "")
    if _fresco(cache.get(k), 3):
        return cache[k]["media"]
    filtro = {"depois": "startDate_greater:$d,", "antes": "startDate_lesser:$d,"}[data[0]] if data else ""
    q = f"""query($p:Int,$c:CountryCode,$s:[MediaSort],$g:[String],$t:[String]{',$d:FuzzyDateInt' if data else ''}){{
      Page(page:$p,perPage:50){{media(type:MANGA,countryOfOrigin:$c,sort:$s,genre_not_in:$g,tag_not_in:$t,
      {filtro}isAdult:false){{{_ANI_CAMPOS}}}}}}}"""
    var = {"p": pagina, "c": pais, "s": [ordem], "g": GENEROS_FORA, "t": TAGS_FORA}
    if data:
        var["d"] = data[1]
    media = _anilist(q, var)["Page"]["media"]
    cache[k] = {"_t": time.time(), "media": media}
    return media


def ani_busca(titulo, cache):
    """melhor obra do AniList para um título da planilha (precisa bater o nome)."""
    k = "busca|" + normalize(titulo)
    if _fresco(cache.get(k), 30):
        return cache[k]["m"]
    q = f"""query($s:String){{Page(perPage:5){{media(type:MANGA,search:$s){{{_ANI_CAMPOS}}}}}}}"""
    try:
        res = _anilist(q, {"s": titulo[:90]})["Page"]["media"]
    except Exception:
        res = []
    alvo, m = normalize(titulo), None
    for c in res:
        nomes = [normalize(n) for n in nomes_de(c)]
        if alvo in nomes or any(_parecido(alvo, n) for n in nomes):
            m = c
            break
    cache[k] = {"_t": time.time(), "m": m}
    return m


ROMANIZADOS = set()      # título romanizado do AniList (Na Honjaman Level Up, Hujakgaui Mabeop Cheonjae)


def nomes_de(m):
    """inglês primeiro, depois sinônimos, o romanizado por último."""
    t = m.get("title") or {}
    if t.get("romaji") and t.get("romaji") != t.get("english"):
        ROMANIZADOS.add(normalize(t["romaji"]))
    out = [t.get("english")] + (m.get("synonyms") or []) + [t.get("romaji")]
    return ordem_nomes([n for n in out if n and re.search(r"[A-Za-z]", n)
                        and not re.search(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]", n)])


_INGLES = re.compile(r"\b(the|of|a|an|i|my|is|in|to|and|with|who|became|return|returns|level|system|player|god|king|son)\b", re.I)


def eh_ingles(n):
    return bool(_INGLES.search(n or "")) and all(ord(ch) < 0x250 or ch in "’‘" for ch in n)


def nomes_busca(nomes):
    """nomes para pesquisar no YouTube: sem o romanizado (ninguém usa); ele só entra se não houver outro."""
    en = [n for n in nomes if normalize(n) not in ROMANIZADOS and all(ord(ch) < 0x250 or ch in "’‘—–…" for ch in n)]
    return en or list(nomes)


def ordem_nomes(nomes):
    """nome em inglês primeiro (é o que os canais usam e o que a busca do YouTube acha); romanizado
    (Hujakgaui Mabeop Cheonjae, Quanmin Zhuanzhi) por último."""
    uniq = list(dict.fromkeys(n.strip() for n in nomes if n and n.strip()))
    return sorted(uniq, key=lambda n: 1 if normalize(n) in ROMANIZADOS else 0)     # sort estável


def titulo_de(m):
    t = m.get("title") or {}
    return t.get("english") or t.get("romaji") or (m.get("synonyms") or ["?"])[0]


PARADAS = {"the", "a", "an", "of", "i", "to", "is", "in", "and", "my", "me", "with", "for", "on", "at",
           "as", "be", "manhwa", "manhua", "manga", "recap", "s", "was", "became", "become", "who"}


def _tokens(s):
    return [t for t in normalize(s).split() if t not in PARADAS]


def _parecido(a, b):
    ta, tb = set(_tokens(a)), set(_tokens(b))
    if not ta or not tb:
        return False
    return len(ta & tb) / max(len(ta), len(tb)) >= 0.8


def caps_estimados(m, now):
    if m.get("chapters"):
        return m["chapters"], False
    sd = m.get("startDate") or {}
    if not sd.get("year"):
        return None, True
    inicio = datetime(sd["year"], sd.get("month") or 6, sd.get("day") or 1, tzinfo=timezone.utc)
    meses = max(0.0, (now - inicio).days / 30.4)
    por_mes = 2 if m.get("countryOfOrigin") == "JP" else 4
    return int(meses * por_mes), True


def sinopse(m, n=700):
    d = re.sub(r"<[^>]+>", " ", m.get("description") or "")
    d = re.sub(r"\(Source:.*?\)|\[Written by.*?\]", " ", d, flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(d)).strip()[:n]


# ---------------------------------------------------------------- YouTube (página de busca)

_IDADE = re.compile(r"(\d+)\s*(seconds?|minutes?|hours?|days?|weeks?|months?|years?|mo|[smhdwy])\b", re.I)
_DIAS = {"s": 1 / 86400, "m": 1 / 1440, "h": 1 / 24, "d": 1, "w": 7, "mo": 30.4, "y": 365}


def _idade_dias(txt):
    m = _IDADE.search(txt or "")
    if not m:
        return None
    n, u = int(m.group(1)), m.group(2).lower()
    u = "mo" if u.startswith("mo") and u != "m" and not u.startswith("min") else u[0]
    return n * _DIAS[u]


def _dur(txt):
    s = 0
    for p in (txt or "").split(":"):
        s = s * 60 + (int(p) if p.isdigit() else 0)
    return s


def yt_busca(q, sp=None):
    params = {"search_query": q, "hl": "en", "gl": "US"}
    if sp:
        params["sp"] = sp
    r = requests.get("https://www.youtube.com/results", params=params,
                     headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}, timeout=30)
    r.raise_for_status()
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", r.text, re.S)
    if not m:
        return []
    out = []

    def txt(o):
        o = o or {}
        return o.get("simpleText") or "".join(x.get("text", "") for x in o.get("runs", []))

    def anda(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                v = o["videoRenderer"]
                snip = " ".join(txt(s.get("snippetText")) for s in v.get("detailedMetadataSnippets", []))
                dono = ((v.get("ownerText") or {}).get("runs") or [{}])[0]
                out.append({"id": v.get("videoId"), "titulo": txt(v.get("title")), "canal": txt(v.get("ownerText")),
                            "canal_id": dono.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId"),
                            "views": _views(txt(v.get("viewCountText"))), "idade": _idade_dias(txt(v.get("publishedTimeText"))),
                            "dur": _dur(txt(v.get("lengthText"))), "snip": snip})
                return
            for x in o.values():
                anda(x)
        elif isinstance(o, list):
            for x in o:
                anda(x)
    anda(json.loads(m.group(1)))
    return out


_INSCRITOS = re.compile(r'"([\d.,]+)\s*([KMB]?) subscribers"')


def canal_inscritos(cid, cache):
    """inscritos do canal (página do canal; cache de 15 dias). None se não der para ler."""
    if not cid:
        return None
    k = "subs|" + cid
    if _fresco(cache.get(k), 15):
        return cache[k]["n"]
    n = None
    try:
        r = requests.get(f"https://www.youtube.com/channel/{cid}", params={"hl": "en"},
                         headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}, timeout=30)
        m = _INSCRITOS.search(r.text)
        if m:
            n = int(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])
    except Exception:
        pass
    cache[k] = {"_t": time.time(), "n": n}
    return n


def _fala_da_obra(video, nomes):
    alvo = normalize(video["titulo"] + " " + video["snip"])
    for n in nomes:
        tk = _tokens(n)
        if not tk:
            continue
        if len(tk) == 1:
            if re.search(rf"\b{re.escape(normalize(n))}\b", alvo):
                return True
            continue
        if sum(1 for t in tk if re.search(rf"\b{re.escape(t)}\b", alvo)) / len(tk) >= 0.75:
            return True
    return False


_NAO_EN = re.compile(r"[ãõçâêôáéíóúñ]|\b(de|do|da|que|seu|sua|para|completo|resumo|um|uma|el|la|los)\b", re.I)
_DESC = re.compile(r'"shortDescription":"((?:[^"\\]|\\.)*)"')
_PUB = re.compile(r'"publishDate":"([^"]+)"')


def yt_video(vid):
    """descrição + data exata de um vídeo (página do vídeo)."""
    r = requests.get("https://www.youtube.com/watch", params={"v": vid, "hl": "en"},
                     headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}, timeout=30)
    r.raise_for_status()
    m, pd = _DESC.search(r.text), _PUB.search(r.text)
    desc = json.loads('"' + m.group(1) + '"') if m else ""
    return desc, (_dt_iso(pd.group(1)) if pd else None)


def _dt_iso(s):
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        return None


def cobertura(nomes, cache, monitorados, now=None, max_desc=6):
    """-> {status, videos, n, ultimo_dias, max_views, nossa}. Recap = vídeo de 40+ min, em inglês, que
    fala da obra no título/trecho OU na descrição (canal grande põe só o gancho no título)."""
    now = now or datetime.now(timezone.utc)
    nomes = nomes_busca(nomes)
    chave = "yt3|" + normalize(nomes[0])
    if _fresco(cache.get(chave), 3):
        return cache[chave]["c"]
    vistos, abertos, nossos_talvez = {}, 0, []
    for n in nomes[:2]:
        try:
            res = yt_busca(f"{n} recap")
        except Exception as e:
            log("   yt erro:", str(e)[:80])
            res = []
        for v in res:
            if v["id"] in vistos or v["dur"] < 40 * 60 or _NAO_EN.search(v["titulo"]):
                continue
            ok = _fala_da_obra(v, nomes)
            if abertos < max_desc:
                try:
                    desc, pub = yt_video(v["id"])
                    abertos += 1
                    if pub:
                        v["idade"] = (now - pub).total_seconds() / 86400
                    ok = ok or _fala_da_obra({"titulo": desc[:1500], "snip": ""}, nomes)
                except Exception:
                    pass
            if ok:
                vistos[v["id"]] = v
            elif normalize(v["canal"]) in NOSSOS:
                nossos_talvez.append(v["canal"])
        if vistos:
            break
        time.sleep(0.5)
    vids = sorted(vistos.values(), key=lambda v: v["idade"] if v["idade"] is not None else 9e9)
    c = {"videos": vids[:6], "n": len(vids)}
    recentes = [v for v in vids if v["idade"] is not None and v["idade"] < ESFRIOU_DIAS]
    c["nossa"] = [v["canal"] for v in vids if normalize(v["canal"]) in NOSSOS] or nossos_talvez
    c["busca"] = nomes[:2]
    if any(normalize(v["canal"]) in NOSSOS for v in recentes):
        c["status"] = "TOMADA"
    elif not vids:
        c["status"] = "LIVRE"
    elif any(v["views"] >= 10_000 or normalize(v["canal"]) in monitorados for v in recentes):
        c["status"] = "TOMADA"
    elif recentes:
        c["status"] = "MORNA"          # recap recente, mas fraco e de canal pequeno
    else:
        c["status"] = "ESFRIOU"
    c["ultimo_dias"] = vids[0]["idade"] if vids else None
    c["max_views"] = max((v["views"] for v in vids), default=0)
    cache[chave] = {"_t": time.time(), "c": c}
    return c


# ---------------------------------------------------------------- IA

def _cliente():
    from openai import OpenAI
    chave = os.environ.get("OPENAI_API_KEY")
    if not chave:
        p = Path(__file__).parent.parent / "momo-manga" / ".keys"
        chave = json.loads(p.read_text(encoding="utf-8"))["api_keys"]["openai"]
    return OpenAI(api_key=chave)


def exemplos(obras, cache_ani, n_bons=30, n_ruins=15):
    """vencedoras e perdedoras reais do nicho, com a premissa do AniList."""
    com = [o for o in obras.values() if o["ratio"]]
    com.sort(key=lambda o: -o["ratio"])
    bons, ruins = [], []
    for o in com:
        if len(bons) >= n_bons:
            break
        m = ani_busca(o["obra"], cache_ani)
        if m and sinopse(m):
            bons.append(f"- VENCEU ({o['ratio']:.1f}x a mediana do canal): {o['obra']} — {sinopse(m, 260)}")
    for o in reversed(com):
        if len(ruins) >= n_ruins:
            break
        if o["ratio"] > 0.5:
            break
        m = ani_busca(o["obra"], cache_ani)
        if m and sinopse(m):
            ruins.append(f"- FRACASSOU ({o['ratio']:.2f}x): {o['obra']} — {sinopse(m, 200)}")
    return bons, ruins


def _instrucao(bons, ruins):
    ganchos = GANCHOS_MD.read_text(encoding="utf-8") if GANCHOS_MD.exists() else ""
    return f"""Você é o caçador de obras de canais de recap de manhwa/manhua/mangá no YouTube (público
masculino, vídeos longos de 1h30+ narrando a história). Sua tarefa: dar nota à PREMISSA de cada obra —
o quanto ela vende num título + thumbnail e segura um vídeo longo.

O que rende no nicho: protagonista homem com uma virada clara (regressão, sistema, poder escondido,
fraco que vira o mais forte, vingança, família/clã que o desprezava), conflito desde o capítulo 1,
escalada de poder, gente subestimando e depois reagindo. A premissa importa mais que a arte ou a idade
da obra. O que não rende: romance como foco, slice of life sem conflito, comédia sem escalada,
protagonista feminina em trama de corte/casamento, premissa confusa que não cabe numa frase.

{ganchos}

EXEMPLOS REAIS (views do vídeo ÷ mediana do mesmo canal na mesma época):
{chr(10).join(bons)}
{chr(10).join(ruins)}

Calibre a nota assim: 9-10 = premissa no nível das melhores vencedoras; 7-8 = forte, fácil de vender;
5-6 = mediana; 3-4 = fraca ou nichada; 0-2 = romance/slice of life/não serve.
ARQUÉTIPOS QUE RENDEM EM TODOS OS NICHOS (o dono confirmou; valorize na nota): protagonista que REENCARNA
CRIANÇA em FAMÍLIA NOBRE (o melhor de todos), reencarna em família nobre, reencarna quando ainda é criança/bebê,
e garoto mágico na ACADEMIA/escola de magia.
Responda SÓ JSON: {{"obras":[{{"id":<id>,"nota":<0-10, pode ter .5>,"premissa":"<1 frase em português,
o gancho da história>","ganchos":["<ids dos ganchos: contraste|humilhacao|aura|sistema|segredo|tensao|beleza>"],
"porque":"<até 25 palavras, compare com uma vencedora se fizer sentido>","risco":"<até 12 palavras ou vazio>","origem":"<KR|CN|JP: país da obra; chute pelo título se não souber>"}}]}}"""


def dar_notas(cands, instrucao, cache_notas, lote=12):
    falta = [c for c in cands if str(c["id"]) not in cache_notas]
    if not falta:
        return
    cli = _cliente()
    lotes = [falta[i:i + lote] for i in range(0, len(falta), lote)]
    log(f"IA: {len(falta)} obras em {len(lotes)} lotes ({MODELO})")

    def um(lt):
        corpo = "\n\n".join(f"id={c['id']} | {c['titulo']} | gêneros: {', '.join(c['generos'])} | tags: "
                            f"{', '.join(c['tags'][:8])}\n{c['sinopse'] or '(sem sinopse; julgue pelo título)'}" for c in lt)
        for tent in range(3):
            try:
                r = cli.chat.completions.create(
                    model=MODELO, response_format={"type": "json_object"},
                    messages=[{"role": "system", "content": instrucao}, {"role": "user", "content": corpo}])
                return json.loads(r.choices[0].message.content).get("obras", [])
            except Exception as e:
                log("   IA erro:", str(e)[:100])
                time.sleep(3 * (tent + 1))
        return []
    with ThreadPoolExecutor(6) as ex:
        for i, res in enumerate(ex.map(um, lotes), 1):
            for o in res:
                cache_notas[str(o.get("id"))] = o
            if i % 5 == 0 or i == len(lotes):
                log(f"   {i}/{len(lotes)} lotes")
                _salva("notas", cache_notas)


# ---------------------------------------------------------------- funil

def _cand_de_media(m, fonte, now):
    caps, est = caps_estimados(m, now)
    return {"id": m["id"], "titulo": titulo_de(m), "nomes": nomes_de(m) or [titulo_de(m)],
            "pais": m.get("countryOfOrigin"), "canal": CANAL_PAIS.get(m.get("countryOfOrigin"), "?"),
            "generos": m.get("genres") or [], "tags": [t["name"] for t in (m.get("tags") or []) if t["rank"] >= 50],
            "sinopse": sinopse(m), "caps": caps, "caps_est": est, "status_obra": m.get("status"),
            "popularidade": m.get("popularity") or 0, "capa": (m.get("coverImage") or {}).get("large", ""),
            "link": m.get("siteUrl", ""), "fonte": fonte, "inicio": (m.get("startDate") or {}).get("year")}


def _yt_thumb(link):
    m = re.search(r"(?:youtu\.be/|v=)([\w-]{11})", link or "")
    return f"https://i.ytimg.com/vi/{m.group(1)}/hqdefault.jpg" if m else ""


def comick_busca(titulo, cache):
    k = "comick|" + normalize(titulo)
    if _fresco(cache.get(k), 30):
        return cache[k]["m"]
    try:
        res = comick.search(comick.clean_query(titulo), requests.Session()) or []
        m = comick.best_match(titulo, res)
    except Exception:
        m = None
    if m:
        covers = m.get("md_covers") or []
        m = {"titulo": m.get("title"), "nomes": comick.english_titles(m), "caps": _int(m.get("last_chapter")),
             "pais": (m.get("country") or "").upper(), "slug": m.get("slug"),
             "capa": f"https://meo.comick.pictures/{covers[0]['b2key']}" if covers else ""}
    cache[k] = {"_t": time.time(), "m": m}
    return m


def _int(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def _cand_da_planilha(o, cache):
    """obra testada que o AniList não conhece: Comick dá nome oficial, país, capítulos e capa;
    sem Comick, a capa é a thumbnail do vídeo que rendeu."""
    cid = "t" + normalize(o["obra"]).replace(" ", "_")[:60]
    cm = None
    for n in o["nomes"][:3]:
        cm = comick_busca(n.split(" / ")[0], cache)
        if cm:
            break
    pais = cm["pais"] if cm and cm["pais"] in CANAL_PAIS else None
    return {"id": cid, "titulo": (cm or {}).get("titulo") or o["obra"],
            "nomes": list(dict.fromkeys(((cm or {}).get("nomes") or []) + o["nomes"]))[:5],
            "pais": pais, "canal": CANAL_PAIS.get(pais, "?"), "generos": [], "tags": [], "sinopse": "",
            "caps": (cm or {}).get("caps"), "caps_est": False, "status_obra": "", "popularidade": 0,
            "capa": (cm or {}).get("capa") or _yt_thumb(o["melhor"]["link"]),
            "link": f"https://comick.dev/comic/{cm['slug']}" if cm and cm.get("slug") else o["melhor"]["link"],
            "fonte": "Testada", "inicio": ""}


# ARQUÉTIPOS que o dono diz que rendem em TODOS os nichos (manhwa, manhua, mangá):
#   reencarna CRIANÇA em FAMÍLIA NOBRE (o melhor) > reencarna em família nobre = reencarna criança = academia de magia
_RE_REENCARNA = re.compile(r"reincarnat|reborn|rebirth|regress|transmigrat|isekai|possess(?:ed|es|ing) the body|"
                           r"wakes? up (?:as|in)|in the body of|second life|past life|reencarn|renasc|regress|"
                           r"volta (?:no tempo|ao passado)|transmigr", re.I)
_RE_NOBRE = re.compile(r"\bnobl|aristocra|\bduke|duchy|ducal|duchess|marquis|marquess|margrav|\bearl\b|\bbaron|"
                       r"viscount|\bcount(?:'s|ess)?\b|young master|\blord(?:'s)? (?:son|family|house)|"
                       r"\bhouse of\b|prestigious (?:family|clan)|royal|prince|imperial (?:family|clan)|"
                       r"\bnobre|aristocr|duque|marqu[eê]s|conde|bar[aã]o|fam[ií]lia (?:nobre|real|imperial)|pr[ií]ncipe", re.I)
_RE_CRIANCA = re.compile(r"\bbab(?:y|ies)|infant|toddler|newborn|\bchild(?:hood)?\b|\bkid\b|little boy|"
                         r"(?:\d|three|four|five|six|seven|eight|nine|ten)[- ]year[- ]old|youngest son|"
                         r"\bbeb[eê]|crian[cç]a|garotinho|menino de \d|ca[cç]ula", re.I)
_RE_ACADEMIA = re.compile(r"academy|magic(?:al)? school|school of magic|wizard(?:ing)? school|"
                          r"\bacademia|escola de magia", re.I)
_RE_MAGIA = re.compile(r"\bmagic|\bmage\b|wizard|sorcer|archmage|\bmana\b|spell|\bmagia|\bmago", re.I)


def arquetipo(c):
    """-> (bônus, rótulo) pelo texto da obra (sinopse, título, tags, premissa da IA)."""
    texto = " ".join([c.get("titulo") or "", " ".join(c.get("nomes") or []), c.get("sinopse") or "",
                      " ".join(c.get("tags") or []), c.get("premissa") or ""])
    re_ = bool(_RE_REENCARNA.search(texto)) or "Reincarnation" in (c.get("tags") or [])
    nobre = bool(_RE_NOBRE.search(texto))
    crianca = bool(_RE_CRIANCA.search(texto))
    academia = bool(_RE_ACADEMIA.search(texto)) and bool(_RE_MAGIA.search(texto))
    bonus, rotulos = 0.0, []
    if re_ and nobre and crianca:
        bonus, rotulos = 2.5, ["reencarna criança em família nobre"]
    else:
        if re_ and nobre:
            bonus, rotulos = 1.5, ["reencarna em família nobre"]
        if re_ and crianca:
            bonus, rotulos = max(bonus, 1.5), rotulos + ["reencarna criança"]
    if academia:
        bonus, rotulos = bonus + 1.5, rotulos + ["academia de magia"]
    return min(3.0, bonus), " + ".join(rotulos)


def pontuar(c):
    st = (c.get("yt") or {}).get("status")
    pen = 4 if st == "TOMADA" else 6 if st == "JÁ FIZEMOS" else 1 if st == "MORNA" else 0
    c["bonus_arq"], c["arquetipo"] = arquetipo(c)
    c["final"] = round(c.get("nota", 0) + _prova(c) + 0.5 * _demanda(c) + c["bonus_arq"] - pen, 2)
    return c["final"]


def tipo_de(c):
    """por que a obra está na lista: a prova manda; senão, de onde veio."""
    if _prova_planilha(c) >= 1:
        return "Testada"
    if _prova_yt(c) >= 1:
        return "Descoberta (YouTube)"
    if arquetipo(c)[0] >= 1.5:
        return "Arquétipo ⭐"
    ano = c.get("inicio")
    if c.get("fonte") == "Nova" or (isinstance(ano, int) and ano >= 2025):
        return "Nova"
    if c.get("fonte") == "Clássica" or (isinstance(ano, int) and ano < 2020):
        return "Clássica"
    return c.get("fonte") or "Popular"


def aba_de(c):
    canal = str(c.get("canal", ""))
    if c.get("pais") == "JP" or canal.startswith("Mangá"):
        return ABA_MANGA
    if c.get("pais") == "CN" or canal.startswith("Kamen"):
        return ABA_MANHUA
    return ABA_MANHWA


def _demanda(c):
    yt = c.get("yt") or {}
    mv, pop = yt.get("max_views", 0), c["popularidade"]
    d_yt = 2 if mv >= 200_000 else 1.5 if mv >= 50_000 else 1 if mv >= 10_000 else 0
    d_ani = 1.5 if pop >= 50_000 else 1 if pop >= 10_000 else 0.5 if pop >= 3_000 else 0
    return max(d_yt, d_ani)


def _prova(c):
    return max(_prova_planilha(c), _prova_yt(c))


def _prova_yt(c):
    """vídeo de recap achado na busca do YouTube (canal fora da planilha): 50k -> +1, 100k -> +2,
    200k -> +3, 400k+ -> +4."""
    py = c.get("prova_yt") or {}
    v, subs = py.get("views", 0), py.get("subs")
    base = math.log2(v / 25_000) if v > 25_000 else 0.0
    if base and subs and v / subs >= 3:          # vídeo fez 3x+ os inscritos do canal: a OBRA puxou
        base += 1
    return min(4.0, base)


def _prova_planilha(c):
    """Já foi testada: rendeu no canal de outra pessoa (views ÷ mediana do canal). É o sinal mais
    forte que existe, vale mais que a nota da IA: 1.5x -> +1.2, 2x -> +2, 3x -> +3.2, 4x+ -> +4."""
    r = c.get("ratio_todos") or 0
    if r <= 1:
        return 0.0
    v = ((c.get("todos") or {}).get("melhor") or {}).get("views", 0)
    peso = 1.0 if v >= 50_000 else 0.8 if v >= 20_000 else 0.5 if v >= 5_000 else 0.2   # canal minúsculo prova pouco
    return min(4.0, 2 * math.log2(r)) * peso


_FONTES_FRACAS = ("Popular", "Em alta")


def mesclar(atual, c):
    """a mesma obra veio de duas fontes: junta nomes, categorias, prova e capítulos."""
    atual["nomes"] = list(dict.fromkeys(atual["nomes"] + c["nomes"]))
    atual["tags"] = list(dict.fromkeys((atual.get("tags") or []) + (c.get("tags") or [])))
    if c.get("prova_yt") and c["prova_yt"]["views"] > (atual.get("prova_yt") or {}).get("views", 0):
        atual["prova_yt"] = c["prova_yt"]
    if c.get("mu_id") and not atual.get("mu_id"):
        atual["mu_id"] = c["mu_id"]
    if c.get("caps") and (atual.get("caps") is None or atual.get("caps_est")):
        atual["caps"], atual["caps_est"] = c["caps"], c.get("caps_est", False)
    if atual.get("fonte") in _FONTES_FRACAS and c.get("fonte"):
        atual["fonte"] = c["fonte"]
    if not atual.get("sinopse") and c.get("sinopse"):
        atual["sinopse"] = c["sinopse"]


def cacar(max_yt=100, now=None, extras_fn=None, sem_api=False):
    """extras_fn(cache_ani, cache_yt, idx, now) -> candidatas de outras fontes (descoberta no YouTube).
    sem_api: não chama a OpenAI; obras sem nota vão para fila_notas.json (o agente noturno preenche
    notas_agente.json, que tem prioridade sobre o cache)."""
    now = now or datetime.now(timezone.utc)
    cache_ani, cache_yt, cache_notas = _cache("anilist"), _cache("youtube"), _cache("notas")
    cache_notas.update(_cache("notas_agente"))
    try:
        log("Lendo a aba todos…")
        todos = ler_aba("todos")
        obras = desempenho(todos, now)
        idx = Indice(obras)
        monitorados = {normalize(r.get("canal", "")) for r in todos}
        log(f"   {len(todos)} vídeos, {len(obras)} obras, {sum(1 for o in obras.values() if o['ratio'])} com nota de desempenho")

        log("Montando o gosto (vencedoras e perdedoras com sinopse)…")
        bons, ruins = exemplos(obras, cache_ani)
        _salva("anilist", cache_ani)
        log(f"   {len(bons)} vencedoras, {len(ruins)} perdedoras")
        instrucao = _instrucao(bons, ruins)

        log("Pool AniList…")
        cands = {}
        for pais, ordem, paginas, data, rotulo in POOLS:
            for p in range(1, paginas + 1):
                for m in ani_pool(pais, ordem, p, cache_ani, data):
                    cands.setdefault(m["id"], _cand_de_media(m, rotulo, now))
            _salva("anilist", cache_ani)
        log(f"   {len(cands)} obras do AniList")

        log("Pool repostagem (renderam e o último vídeo tem 6+ meses)…")
        n_rep = 0
        for o in sorted(obras.values(), key=lambda o: -(o["ratio"] or 0)):
            if not o["ratio"] or o["ratio"] < 1.3 or (now - o["ultimo"]).days < ESFRIOU_DIAS:
                continue
            m = ani_busca(o["obra"].split(" / ")[0], cache_ani)
            if m and (m.get("isAdult") or set(m.get("genres") or []) & set(GENEROS_FORA)):
                continue
            if m:
                c = cands.setdefault(m["id"], _cand_de_media(m, "Testada", now))
            else:   # o AniList não conhece: tenta o Comick; senão, entra com o que a planilha sabe
                c = cands.setdefault("t" + normalize(o["obra"]).replace(" ", "_")[:60], _cand_da_planilha(o, cache_ani))
            c["fonte"] = "Testada"
            n_rep += 1
        _salva("anilist", cache_ani)
        log(f"   {n_rep} obras para repostar")
        if extras_fn:
            n_ex, n_mesc = 0, 0
            por_nome = {}
            for c0 in cands.values():
                for n in c0["nomes"]:
                    por_nome.setdefault(normalize(n), c0)
            for c in extras_fn(cache_ani, cache_yt, idx, now):
                atual = cands.get(c["id"]) or next((por_nome[normalize(n)] for n in c["nomes"]
                                                     if normalize(n) in por_nome), None)
                if atual:
                    mesclar(atual, c)
                    n_mesc += 1
                else:
                    cands[c["id"]] = c
                    for n in c["nomes"]:
                        por_nome.setdefault(normalize(n), c)
                    n_ex += 1
            _salva("anilist", cache_ani)
            _salva("youtube", cache_yt)
            log(f"   {n_ex} obras novas de outras fontes (YouTube, MangaUpdates, tracker); {n_mesc} juntadas a uma que já existia")

        # filtro: capítulos, nossos canais, monitorado recente
        fora = {"poucos caps": 0, "canal monitorado recente": 0, "fora do perfil": 0}
        vivos, ja = [], set()
        for c in cands.values():
            achadas = idx.achar(c["nomes"])
            if any(id(a) in ja for a in achadas):     # mesma obra por dois caminhos: fica a primeira
                continue
            ja.update(id(a) for a in achadas)
            o = juntar(achadas)
            if o:
                c["todos"] = o
                c["ratio_todos"] = o["ratio"] or 0
                c["nomes"] = ordem_nomes([n for n in o["nomes"] if len(n) < 90] + c["nomes"])
            tags = set(c["tags"])
            if tags & set(TAGS_FORA) or set(c["generos"]) & set(GENEROS_FORA):
                fora["fora do perfil"] += 1
                continue
            if c["caps"] is not None and c["caps"] < MIN_CAPS:
                fora["poucos caps"] += 1
                continue
            if o and (now - o["ultimo"]).days < ESFRIOU_DIAS:     # vale para os nossos canais também
                fora["canal monitorado recente"] += 1
                continue
            if o and (o["ratio"] or 0) >= 1.3:
                c["fonte"] = "Testada"
            vivos.append(c)
        log(f"Filtro: {len(vivos)} seguem | fora: {fora}")

        if sem_api:
            falta = [c for c in vivos if str(c["id"]) not in cache_notas]
            (DIR / "instrucao_notas.md").write_text(instrucao, encoding="utf-8")
            _salva("fila_notas", {"obras": [{"id": c["id"], "titulo": c["titulo"], "nomes": c["nomes"][:5],
                                             "generos": c["generos"], "tags": c["tags"][:8], "sinopse": c["sinopse"],
                                             "fonte": c["fonte"]} for c in falta]})
            log(f"IA: {len(falta)} obras sem nota foram para fila_notas.json (sem API)")
        else:
            dar_notas(vivos, instrucao, cache_notas)
            _salva("notas", cache_notas)
        for c in vivos:
            n = cache_notas.get(str(c["id"])) or {}
            c["nota"] = float(n.get("nota") or 0)
            c["premissa"], c["porque"], c["risco"] = n.get("premissa", ""), n.get("porque", ""), n.get("risco", "")
            c["ganchos"] = n.get("ganchos") or []
            c["sem_nota"] = not n
            if c["canal"] == "?" and n.get("origem") in CANAL_PAIS:
                c["canal"] = CANAL_PAIS[n["origem"]] + " (chute)"
                c["pais"] = c["pais"] or n["origem"]

        def pontua(c):
            return -pontuar(c)

        if max_yt:
            import mangaupdates as MU
            vivos.sort(key=pontua)
            log("MangaUpdates: categorias, nomes e capítulos das 150 primeiras…")
            for i, c in enumerate(vivos[:150], 1):
                try:
                    MU.enriquecer(c, cache_ani)
                except Exception as e:
                    log("   MU erro:", str(e)[:80])
                if i % 50 == 0:
                    _salva("anilist", cache_ani)
            _salva("anilist", cache_ani)

        # checa o YouTube das melhores; quem cai (TOMADA) abre espaço e a próxima também é checada,
        # até as `max_yt` primeiras estarem todas conferidas
        feitos = 0
        while feitos < max_yt * 3:
            vivos.sort(key=pontua)
            falta = [c for c in vivos[:max_yt] if "yt" not in c]
            if not falta:
                break
            log(f"YouTube: {len(falta)} para checar (já foram {feitos})…")
            for c in falta:
                c["yt"] = cobertura(c["nomes"], cache_yt, monitorados, now)
                feitos += 1
                if feitos % 10 == 0:
                    log(f"   {feitos}")
                    _salva("youtube", cache_yt)
        _salva("youtube", cache_yt)
        for c in vivos:
            pontua(c)
        vivos.sort(key=lambda c: -c["final"])
        return vivos
    finally:
        _salva("anilist", cache_ani)
        _salva("youtube", cache_yt)
        _salva("notas", cache_notas)


# ---------------------------------------------------------------- saída

def _yt_txt(c):
    yt = c.get("yt")
    if not yt:
        return "não checado"
    if yt["status"] == "LIVRE":
        return "LIVRE: nenhum recap longo"
    d = yt["ultimo_dias"]
    quando = f"{d / 30.4:.0f} meses" if d and d >= 45 else f"{d:.0f} dias" if d is not None else "?"
    u = yt["videos"][0] if yt.get("videos") else {}
    return (f"{yt['status']}: {yt['n']} recap(s); o último foi {u.get('canal', '?')} há {quando} ({u.get('views', 0):,} views); "
            f"o maior fez {yt['max_views']:,}").replace(",", ".")


def _quando(dias):
    if dias is None:
        return "?"
    return f"há {dias / 30.4:.0f} meses" if dias >= 45 else f"há {dias:.0f} dias"


def _mil(v):
    v = int(v or 0)
    if v >= 1_000_000:
        return f"{v / 1_000_000:.1f} mi".replace(".", ",")
    return f"{v / 1000:.0f} mil" if v >= 1000 else str(v)


_ICONE = {"LIVRE": "🟢 Livre", "ESFRIOU": "🔵 Esfriou", "MORNA": "🟠 Só canal pequeno", "TOMADA": "🔴 Tomada",
          "JÁ FIZEMOS": "🔴 Já fizemos"}


def _yt_curto(c):
    yt = c.get("yt")
    if not yt:
        return "—"
    if yt["status"] == "LIVRE":
        return "🟢 Livre · ninguém fez recap longo"
    u = yt["videos"][0] if yt.get("videos") else {}
    return f"{_ICONE.get(yt['status'], yt['status'])} · último {_quando(u.get('idade'))} ({_mil(u.get('views'))} views)"


def _prova_curta(c):
    """-> (texto, link do vídeo, views do vídeo)"""
    py = c.get("prova_yt")
    if py and _prova_yt(c) > _prova_planilha(c):
        subs = f" · canal de {_mil(py['subs'])} inscritos" if py.get("subs") else ""
        return f"{py['canal']} · {_quando(py['idade'])}{subs}", py["link"], py["views"]
    o = c.get("todos")
    if not o or not (o.get("ratio") or 0):
        return "", "", 0
    b = o["melhor"]
    dias = (datetime.now(timezone.utc) - b["dt"]).days
    return f"{(b['ratio'] or 0):.1f}× a média do {b['canal']} · {_quando(dias)}".replace(".", ","), b["link"], b["views"]


def _texto_prova(c):
    py = c.get("prova_yt")
    if py and _prova_yt(c) > _prova_planilha(c):
        subs = f", canal com {py['subs']:,} inscritos" if py.get("subs") else ""
        return (f"{py['views']:,} views no {py['canal']} há {py['idade'] / 30.4:.0f} meses{subs} (achado no YouTube)"
                .replace(",", "."))
    return _ultimo_todos(c)


def _texto_nossos(c):
    o = c.get("todos") or {}
    if not o.get("nossos_ultimo"):
        return ""
    meses = (datetime.now(timezone.utc) - o["nossos_ultimo"]).days / 30.4
    return f"{', '.join(o['nossos_canais'])} já fez há {meses:.0f} meses"


def _ultimo_todos(c):
    o = c.get("todos")
    if not o:
        return ""
    b = o["melhor"]
    meses = (datetime.now(timezone.utc) - b["dt"]).days / 30.4
    return (f"{b['ratio'] or 0:.1f}x a média do {b['canal']} há {meses:.0f} meses ({b['views']:,} views)"
            .replace(",", ".") + f" · último vídeo {o['ultimo'].astimezone(BRT):%d/%m/%Y}")


def linhas(vivos):
    out = []
    for c in vivos:
        caps = "" if c["caps"] is None else (f"~{c['caps']}" if c["caps_est"] else str(c["caps"]))
        out.append({"nota": c["final"], "nota_ia": c["nota"], "obra": c["titulo"], "canal": c["canal"],
                    "premissa": c["premissa"], "ganchos": ", ".join(c["ganchos"]), "porque": c["porque"],
                    "risco": c["risco"], "caps": caps, "youtube": _yt_txt(c), "planilha": _texto_prova(c), "nossos": _texto_nossos(c),
                    "id": c["id"], "nomes": " | ".join(c["nomes"][:6]),
                    "fonte": c["fonte"], "aba": aba_de(c),
                    "tipo": tipo_de(c) + (f" · ⭐ {c['arquetipo']}" if c.get("arquetipo") else ""),
                    "popularidade": c["popularidade"], "inicio": c["inicio"] or "",
                    "capa": c["capa"], "link": c["link"],
                    "yt_curto": _yt_curto(c), "prova_curta": _prova_curta(c)[0], "video_views": _prova_curta(c)[2],
                    "arquetipo": c.get("arquetipo") or arquetipo(c)[1],
                    "video_prova": (c.get("prova_yt") or {}).get("link") if _prova_yt(c) > _prova_planilha(c)
                    else ((c.get("todos") or {}).get("melhor") or {}).get("link", "")})
    return out


def salvar_local(ls, dossies=None):
    DIR.mkdir(parents=True, exist_ok=True)
    dossies = dossies if dossies is not None else _cache("dossies")
    _salva("ultimo", {"linhas": ls, "t": time.time()})
    for l in ls:
        d = dossies.get(str(l.get("id"))) or {}
        l["dossie"], l["veredito"] = d.get("dossie", ""), d.get("veredito", "")
        if d.get("nome_ingles"):
            l["obra"] = d["nome_ingles"]
        if d.get("youtube"):
            l["youtube"] = d["youtube"]
        st = (d.get("status") or "").upper()
        if st in _ICONE:
            u = d.get("ultimo_recap") or {}
            if st == "LIVRE":
                l["yt_curto"] = "🟢 Livre · ninguém fez recap longo"
            else:
                meses = u.get("meses")
                quando = f"há {meses} meses" if meses not in (None, "") else "?"
                l["yt_curto"] = f"{_ICONE[st]} · último {quando} ({_mil(u.get('views'))} views)"
            l["yt_conferido"] = True
        if d.get("caps"):
            l["caps"] = d["caps"]
    # quem o agente reprovou (TOMADA/descartar) desce para o fim
    ls.sort(key=lambda l: (1 if ((l.get("veredito") or "").upper().startswith(("DESCART", "TOMADA"))
                                 or (l.get("yt_curto") or "").startswith("🔴")) else 0, -l["nota"]))
    with open(DIR / "recomendadas.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(ls[0].keys()))
        w.writeheader()
        w.writerows(ls)
    cor = {"JÁ FIZEMOS": "#7c3aed", "LIVRE": "#16a34a", "ESFRIOU": "#2563eb", "MORNA": "#d97706", "TOMADA": "#dc2626"}
    por_aba = {}
    for l in ls:
        por_aba.setdefault(l.get("aba") or ABA_MANHWA, []).append(l)
    for aba in ABAS:
        _pagina(aba, por_aba.get(aba, [])[:150], por_aba, cor)
    # recomendadas.html = índice: as 5 melhores de cada tipo + link para a página de cada um
    blocos = []
    for aba in ABAS:
        top = por_aba.get(aba, [])[:5]
        itens = "".join(f"<li><b>{l['nota']:.1f}</b> · {html.escape(l['obra'])} "
                        f"<span class=m>{html.escape(l.get('yt_curto') or '')}</span></li>" for l in top)
        blocos.append(f'<div class=c style="display:block"><h2><a href="{_arq_pagina(aba)}">{html.escape(aba)} · '
                      f'{len(por_aba.get(aba, []))} obras →</a></h2><ol>{itens}</ol></div>')
    (DIR / "recomendadas.html").write_text(_cabeca("Caçador de Obras") + "".join(blocos), encoding="utf-8")


def _arq_pagina(aba):
    return f"recomendadas_{normalize(aba).replace(' ', '_') or 'manga'}.html"


def _cabeca(titulo):
    nav = " · ".join(f'<a style="color:#93c5fd" href="{_arq_pagina(a)}">{html.escape(a)}</a>' for a in ABAS)
    return f"""<!doctype html><meta charset=utf-8><title>{html.escape(titulo)}</title>
<style>body{{font:15px system-ui;background:#0f1115;color:#e5e7eb;margin:20px}}h1{{font-size:26px}}h2 a{{color:#fff}}li{{margin:4px 0}}
.c{{display:flex;gap:14px;background:#181b22;border-radius:10px;padding:12px;margin:10px 0}}img{{width:92px;height:130px;object-fit:cover;border-radius:6px}}
.h{{font-size:21px}}.h a{{color:#fff;text-decoration:none}}.k{{background:#374151;border-radius:4px;padding:1px 6px;font-size:13px}}
.p{{margin:6px 0;font-size:16px}}.m{{color:#9ca3af;font-size:13px}}.s{{color:#fff;border-radius:4px;padding:1px 6px;margin-right:6px}}
.g{{display:grid;grid-template-columns:1.3fr 1.3fr .5fr;gap:10px;margin-top:12px;font-size:17px}}.g span{{display:block;color:#9ca3af;font-size:13px;margin-bottom:2px}}.a{{color:#fbbf24;font-size:15px}}.vv{{color:#e5e7eb;text-align:center;text-decoration:none;font-size:15px}}
.w{{color:#cbd5e1;font-size:13px;margin-top:4px}}.c>.t{{flex:1}}img.v{{width:240px;height:135px;border-radius:6px;object-fit:cover}}.tt{{color:#4ade80;font-size:14px;margin-top:4px;font-weight:600}}.n{{color:#c4b5fd;font-size:13px;margin-top:3px}}.d{{background:#0b1220;border-left:3px solid #f59e0b;padding:8px 10px;margin-top:8px;font-size:14px;line-height:1.45;color:#e5e7eb}}</style>
<h1>{html.escape(titulo)} · {datetime.now(BRT):%d/%m/%Y %H:%M}</h1><p><a style="color:#93c5fd" href="recomendadas.html">Índice</a> · {nav}</p>"""


def _pagina(aba, ls, por_aba, cor):
    cards = []
    for i, l in enumerate(ls, 1):
        estrela = f" ⭐ <span class=a>{html.escape(l['arquetipo'])}</span>" if l.get("arquetipo") else ""
        video = (f'<a class=vv href="{html.escape(l["video_prova"])}" target=_blank><img class=v src="'
                 f'{_yt_thumb(l["video_prova"])}"><br>▶ {_mil(l.get("video_views"))} views</a>') if l.get("video_prova") else ""
        cards.append(f"""<div class=c><img src="{html.escape(l['capa'])}" loading=lazy><div class=t>
<div class=h><b>#{i} · {l['nota']:.1f}</b> <a href="{html.escape(l['link'])}" target=_blank>{html.escape(l['obra'])}</a>{estrela}</div>
<div class=g><div><span>YouTube hoje</span>{html.escape(l.get('yt_curto') or '—')}</div>
<div><span>Testada</span>{html.escape(l.get('prova_curta') or '—')}</div>
<div><span>Capítulos</span>{html.escape(str(l['caps']) or '?')}</div></div>
{('<div class=d>' + html.escape(dossie_curto(l.get('dossie'))).replace(chr(10), '<br>') + '</div>') if l.get('dossie') else ''}</div>{video}</div>""")
    (DIR / _arq_pagina(aba)).write_text(_cabeca(f"Caçador de Obras · {aba}") +
                                        f"<h2>{html.escape(aba)} · {len(por_aba.get(aba, []))} obras</h2>" +
                                        "".join(cards), encoding="utf-8")


HEADER_OUT = ["Peguei", "Capa", "Nota", "Obra", "Caps", "YouTube hoje", "Testada", "Dossiê", "Vídeo que rendeu",
              "Link", "ID"]
MAX_LINHAS_OUT = 250
SAIDA = Path(__file__).parent / "cacador_saida" / "recomendadas.json"   # o PC publica; o GitHub grava a aba


def exportar(ls):
    """lista final (com veredito/dossiê) -> cacador_saida/recomendadas.json, que vai para o GitHub."""
    campos = ["id", "nota", "obra", "arquetipo", "caps", "yt_curto", "prova_curta", "dossie", "video_prova", "video_views",
              "link", "capa"]
    abas = {a: [] for a in ABAS}
    for l in ls:
        lst = abas.setdefault(l.get("aba") or ABA_MANHWA, [])
        if len(lst) < MAX_LINHAS_OUT:
            lst.append({k: l.get(k, "") for k in campos})
    SAIDA.parent.mkdir(exist_ok=True)
    SAIDA.write_text(json.dumps({"gerado": datetime.now(BRT).strftime("%d/%m/%Y %H:%M"), "abas": abas},
                                ensure_ascii=False, indent=0), encoding="utf-8")
    return SAIDA


def dossie_curto(txt):
    linhas = [x.strip() for x in (txt or "").splitlines() if x.strip()]
    chave = [x for x in linhas if x.split(":")[0].strip().lower() in ("prova", "hoje", "gancho", "risco")]
    return chr(10).join(chave or linhas[1:] or linhas)


def _regras_out(sid):
    n = len(HEADER_OUT)
    corpo = {"sheetId": sid, "startRowIndex": 1, "endRowIndex": MAX_LINHAS_OUT + 1}

    def cols(a, b):
        return {**corpo, "startColumnIndex": a, "endColumnIndex": b}

    def fmt(a, b, f, campos):
        return {"repeatCell": {"range": cols(a, b), "cell": {"userEnteredFormat": f}, "fields": campos}}
    return [
        {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "ROWS", "startIndex": 1,
                                                 "endIndex": MAX_LINHAS_OUT + 1},
                                       "properties": {"pixelSize": 200}, "fields": "pixelSize"}},
        {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": n - 1,
                                                 "endIndex": n}, "properties": {"hiddenByUser": True},
                                       "fields": "hiddenByUser"}},          # ID: só para o Peguei andar junto
        {"setDataValidation": {"range": cols(0, 1), "rule": {"condition": {"type": "BOOLEAN"}}}},
        fmt(0, n, {"textFormat": {"fontSize": 12}, "verticalAlignment": "MIDDLE", "wrapStrategy": "WRAP"},
            "userEnteredFormat.textFormat.fontSize,userEnteredFormat.verticalAlignment,userEnteredFormat.wrapStrategy"),
        fmt(2, 3, {"textFormat": {"fontSize": 15, "bold": True}, "numberFormat": {"type": "NUMBER", "pattern": "0.0"}},
            "userEnteredFormat.textFormat.fontSize,userEnteredFormat.textFormat.bold,userEnteredFormat.numberFormat"),
        fmt(3, 4, {"textFormat": {"fontSize": 13, "bold": True}}, "userEnteredFormat.textFormat.fontSize,userEnteredFormat.textFormat.bold"),
        fmt(5, 7, {"horizontalAlignment": "CENTER"}, "userEnteredFormat.horizontalAlignment"),
        fmt(7, 8, {"textFormat": {"fontSize": 11}, "verticalAlignment": "MIDDLE"},
            "userEnteredFormat.textFormat.fontSize,userEnteredFormat.verticalAlignment"),
        fmt(8, 10, {"horizontalAlignment": "CENTER"}, "userEnteredFormat.horizontalAlignment"),
        {"addConditionalFormatRule": {"index": 0, "rule": {
            "ranges": [cols(0, n)],
            "booleanRule": {"condition": {"type": "CUSTOM_FORMULA", "values": [{"userEnteredValue": "=$A2=TRUE"}]},
                            "format": {"backgroundColor": {"red": 0.85, "green": 0.92, "blue": 0.83}}}}}},
    ]


PLANILHA_ARQ = Path(__file__).parent / "cacador_saida" / "planilha.json"   # {"id": "<id da planilha do caçador>"}


def _cliente_google():
    import gspread
    from google.oauth2.service_account import Credentials
    creds = Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
                                                  scopes=["https://www.googleapis.com/auth/spreadsheets"])
    return gspread.authorize(creds)


def tirar_aba_do_tracker(gc):
    """o caçador tem planilha própria: a aba que ele criou no tracker (27/11/2026) sai de lá."""
    import gspread
    ss = gc.open_by_key(SHEET_ID)
    try:
        ss.del_worksheet(ss.worksheet(TAB_OUT))
        log(f"Aba `{TAB_OUT}` removida da planilha do tracker.")
    except gspread.WorksheetNotFound:
        pass


def gravar_planilha(abas, gerado="", gc=None):
    """Planilha própria do caçador (id em cacador_saida/planilha.json): uma aba por tipo de obra
    (`Manhwa e Manhua`, `Mangá`). O Peguei acompanha a obra pelo ID (a aba é reescrita e reordenada)."""
    import gspread
    import novas_obras as NO
    gc = gc or _cliente_google()
    ss = gc.open_by_key(json.loads(PLANILHA_ARQ.read_text(encoding="utf-8"))["id"])
    peguei = {}
    for ws in ss.worksheets():             # Peguei de qualquer aba (inclusive da antiga `Obras Recomendadas`)
        for r in ws.get_all_values()[1:]:
            if r and r[-1] and r[0] == "TRUE":
                peguei[r[-1]] = "TRUE"
    total, feitas = 0, set()
    for i, (titulo, ls) in enumerate(abas.items()):
        ws = NO._ensure_tab(ss, titulo, HEADER_OUT, rows=MAX_LINHAS_OUT + 1, index=i,
                            widths=[70, 130, 70, 280, 70, 240, 260, 560, 150, 90, 60],
                            center_cols=(0, 1, 2, 4, 8, 9), link_col=None, extra=_regras_out)
        ws.batch_clear([f"A2:J{MAX_LINHAS_OUT + 1}"])

        linhas_ = [[peguei.get(str(l["id"]), "FALSE"), f'=IMAGE("{l["capa"]}")' if l.get("capa") else "",
                    l["nota"], ("⭐ " if l.get("arquetipo") else "") + l["obra"], str(l.get("caps") or ""),
                    l.get("yt_curto") or "—", l.get("prova_curta") or "—", dossie_curto(l.get("dossie")), "", "",
                    str(l["id"])]
                   for l in ls[:MAX_LINHAS_OUT]]

        def celula_link(url, texto):   # link de verdade no texto (vale em qualquer idioma da planilha)
            if not url:
                return {"userEnteredValue": {"stringValue": ""}}
            return {"userEnteredValue": {"stringValue": texto},
                    "textFormatRuns": [{"startIndex": 0, "format": {"link": {"uri": url}}}]}
        links = [{"values": [celula_link(l.get("video_prova"), f"▶ {_mil(l.get('video_views'))} views"),
                             celula_link(l.get("link"), "abrir obra")]} for l in ls[:MAX_LINHAS_OUT]]
        if linhas_:
            ws.update(linhas_, "A2", value_input_option="USER_ENTERED")
            ss.batch_update({"requests": [{"updateCells": {
                "rows": links, "fields": "userEnteredValue,textFormatRuns",
                "start": {"sheetId": ws.id, "rowIndex": 1, "columnIndex": 8}}}]})
        if gerado:
            ws.update_note("A1", f"Caçador de Obras · gerado em {gerado}")
        total += len(linhas_)
        feitas.add(ws.id)
    for outra in ss.worksheets():          # aba vazia da planilha nova e a antiga `Obras Recomendadas` saem
        if outra.id not in feitas and (outra.title in ABAS_ANTIGAS or not any(c for r in outra.get_values("A1:C3") for c in r)):
            ss.del_worksheet(outra)
    return total


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--planilha-de" in sys.argv:        # GitHub Actions: grava a aba a partir do json que o PC publicou
        d = json.loads(Path(sys.argv[sys.argv.index("--planilha-de") + 1]).read_text(encoding="utf-8"))
        gc = _cliente_google()
        tirar_aba_do_tracker(gc)
        if not PLANILHA_ARQ.exists():
            log("Sem planilha do caçador configurada (cacador_saida/planilha.json): nada gravado.")
            sys.exit()
        conta = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]).get("client_email", "?")
        try:
            abas = d.get("abas") or {TAB_OUT: d.get("linhas", [])}
            n = gravar_planilha(abas, d.get("gerado", ""), gc)
        except Exception as e:
            # ::error:: vira anotação pública no GitHub: dá para ler o motivo sem abrir o log
            msg = f"{type(e).__name__}: {str(e)[:300]}".replace("\n", " ")
            print(f"::error::Planilha do caçador não gravada ({msg}). A planilha precisa estar compartilhada "
                  f"como Editor com {conta}")
            sys.exit(1)
        print(f"::notice::Planilha do caçador gravada: {n} obras em {len(abas)} abas (lista de {d.get('gerado')}).")
        sys.exit()
    max_yt = int(sys.argv[sys.argv.index("--max-yt") + 1]) if "--max-yt" in sys.argv else 100
    vivos = cacar(max_yt=max_yt)
    ls = linhas(vivos)
    salvar_local(ls)
    log(f"\nTop 30 (de {len(ls)}):")
    for i, l in enumerate(ls[:30], 1):
        log(f"{i:2}. {l['nota']:4.1f} [{l['canal']}] {l['obra'][:50]} | {l['youtube']} | caps {l['caps']}\n    {l['premissa']}")
    log(f"\n-> {DIR / 'recomendadas.html'}")
    if "--planilha" in sys.argv:
        gravar_planilha(ls)
        log(f"Aba `{TAB_OUT}` gravada.")
