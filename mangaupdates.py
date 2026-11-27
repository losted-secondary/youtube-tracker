"""MangaUpdates (api.mangaupdates.com, pública, sem chave) para o Caçador de Obras.

Melhor que o AniList para o que o dono procura:
  - CATEGORIAS feitas pela comunidade (Reincarnation, Nobility/Aristocracy, Child Protagonist, Academy...):
    dá para caçar direto os arquétipos que rendem;
  - todos os nomes alternativos (o inglês que os canais usam), último capítulo e ranking de popularidade.

Uso no caçador:
  pools(cache, now)            -> candidatas das buscas por arquétipo/premissa (manhwa, manhua, mangá)
  enriquecer(c, cache)         -> junta categorias, nomes e capítulos do MU numa candidata que veio de outra fonte
"""
import re
import time
from datetime import datetime

import requests

from comick import normalize

API = "https://api.mangaupdates.com/v1"
H = {"User-Agent": "cacador-obras/1.0", "Content-Type": "application/json"}
TIPOS = {"Manhwa": "KR", "Manhua": "CN", "Manga": "JP"}
FORA_GENEROS = ["Romance", "Shoujo", "Josei", "Yaoi", "Yuri", "Shoujo Ai", "Shounen Ai", "Hentai", "Smut", "Adult"]
# buscas por categoria (todas as categorias da lista precisam estar na obra). As 4 primeiras são os ARQUÉTIPOS
# que o dono diz que rendem em todos os nichos; as outras são premissas fortes do nicho.
BUSCAS = [
    ("Reencarna criança em família nobre", ["Reincarnation", "Nobility/Aristocracy", "Child Protagonist"]),
    ("Reencarna em família nobre", ["Reincarnation", "Nobility/Aristocracy"]),
    ("Regride em família nobre", ["Regression", "Nobility/Aristocracy"]),
    ("Protagonista nobre", ["Noble Protagonist"]),
    ("Reencarna criança", ["Reincarnation", "Child Protagonist"]),
    ("Academia de magia", ["Academy", "Magic"]),
    ("Regressão", ["Regression"]),
    ("Fraco que vira forte", ["Weak to Strong"]),
    ("Reencarna em outro mundo", ["Reincarnated in Another World"]),
    ("Poder escondido", ["Hidden Ability"]),
    ("Vingança", ["Revenge"]),
    ("Sistema", ["Game Elements"]),
    ("Cultivo", ["Cultivation"]),
]
FORA_CATEGORIAS = ["Female Protagonist"]     # protagonista feminina fica de fora (o público é masculino)
PAGINAS = 2          # 50 por página, ordenado por nota dos leitores
_ultimo = [0.0]


def log(*a):
    print(*a, flush=True)


def _req(metodo, caminho, **kw):
    for tent in range(4):
        espera = 0.7 - (time.time() - _ultimo[0])
        if espera > 0:
            time.sleep(espera)
        _ultimo[0] = time.time()
        try:
            r = requests.request(metodo, API + caminho, headers=H, timeout=40, **kw)
        except requests.RequestException:
            time.sleep(3 * (tent + 1))
            continue
        if r.status_code == 429 or r.status_code >= 500:
            time.sleep(5 * (tent + 1))
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"MangaUpdates não respondeu: {caminho}")


def _fresco(e, dias):
    return e and time.time() - e.get("_t", 0) < dias * 86400


def busca(categorias, tipo, pagina, cache):
    k = f"mu|busca|{'+'.join(categorias)}|{tipo}|{pagina}"
    if _fresco(cache.get(k), 7):
        return cache[k]["r"]
    d = _req("POST", "/series/search", json={"category": categorias, "type": [tipo], "exclude_genre": FORA_GENEROS,
                                              "exclude_category": FORA_CATEGORIAS, "orderby": "rating",
                                              "perpage": 50, "page": pagina})
    r = [x["record"] for x in d.get("results", [])]
    cache[k] = {"_t": time.time(), "r": r}
    return r


def detalhe(sid, cache):
    k = f"mu|serie|{sid}"
    if _fresco(cache.get(k), 15):
        return cache[k]["d"]
    s = _req("GET", f"/series/{sid}")
    d = {"nomes": [a["title"] for a in s.get("associated") or []],
         "categorias": [c["category"] for c in s.get("categories") or [] if (c.get("votes") or 0) >= 0],
         "caps": s.get("latest_chapter"), "status": s.get("status") or "", "completo": s.get("completed"),
         "rank_mes": ((s.get("rank") or {}).get("position") or {}).get("month"),
         "generos": [g["genre"] for g in s.get("genres") or []], "url": s.get("url"),
         "capa": ((s.get("image") or {}).get("url") or {}).get("original", ""),
         "descricao": s.get("description") or "", "ano": s.get("year"), "tipo": s.get("type")}
    cache[k] = {"_t": time.time(), "d": d}
    return d


def procurar(titulo, cache):
    """série do MU com esse nome (precisa bater um dos nomes associados)."""
    k = "mu|procura|" + normalize(titulo)
    if _fresco(cache.get(k), 30):
        return cache[k]["sid"]
    sid = None
    try:
        d = _req("POST", "/series/search", json={"search": titulo[:90], "perpage": 5})
        alvo = normalize(titulo)
        for x in d.get("results", []):
            rec = x["record"]
            if normalize(rec.get("title")) == alvo or normalize(x.get("hit_title")) == alvo:
                sid = rec["series_id"]
                break
    except Exception:
        pass
    cache[k] = {"_t": time.time(), "sid": sid}
    return sid


def _texto(html_):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_ or "")).strip()


def _so_latino(n):
    return n and re.search(r"[A-Za-z]", n) and not re.search(r"[぀-ヿ一-鿿가-힯Ѐ-ӿ]", n)


_INGLES = re.compile(r"\b(the|of|a|an|i|my|is|in|to|and|with|who|became|return|returns|level|system|player|"
                     r"god|king|son|lord|master|genius|reborn|reincarnat\w*|regress\w*|academy|mage|magic|sword)\b", re.I)


def _ordem(nomes):
    """inglês primeiro (o que os canais usam e o YouTube acha); romanizado por último."""
    uniq = list(dict.fromkeys(n.strip() for n in nomes if _so_latino(n)))
    return sorted(uniq, key=lambda n: 0 if _INGLES.search(n) else 1)


def candidata(rec, det, rotulo, now, CANAL_PAIS, MIN_CAPS):
    pais = TIPOS.get(det.get("tipo") or rec.get("type"))
    ano = int(det["ano"]) if str(det.get("ano") or "").isdigit() else None
    caps = det.get("caps")
    nomes = _ordem([rec["title"]] + det["nomes"]) or [rec["title"]]
    return {"id": f"mu{rec['series_id']}", "titulo": nomes[0],
            "nomes": nomes,
            "pais": pais, "canal": CANAL_PAIS.get(pais, "?"), "generos": det["generos"],
            "tags": det["categorias"], "sinopse": _texto(det["descricao"])[:700],
            "caps": caps, "caps_est": False, "status_obra": det["status"][:40],
            "popularidade": 0, "rank_mu": det.get("rank_mes"), "nota_leitores": rec.get("bayesian_rating"),
            "capa": det["capa"] or ((rec.get("image") or {}).get("url") or {}).get("original", ""),
            "link": det["url"] or rec.get("url", ""), "fonte": rotulo, "inicio": ano, "mu_id": rec["series_id"]}


def pools(cache, now, CANAL_PAIS, MIN_CAPS):
    """candidatas das buscas por arquétipo/premissa, nos 3 tipos (manhwa, manhua, mangá)."""
    out, vistos = [], set()
    for rotulo, cats in BUSCAS:
        n0 = len(out)
        for tipo in TIPOS:
            if rotulo == "Cultivo" and tipo != "Manhua":
                continue
            for p in range(1, PAGINAS + 1):
                try:
                    recs = busca(cats, tipo, p, cache)
                except Exception as e:
                    log("   MU erro:", str(e)[:80])
                    break
                for rec in recs:
                    if rec["series_id"] in vistos:
                        continue
                    vistos.add(rec["series_id"])
                    try:
                        det = detalhe(rec["series_id"], cache)
                    except Exception:
                        continue
                    if (det.get("caps") or 0) and det["caps"] < MIN_CAPS:
                        continue
                    out.append(candidata(rec, det, f"MangaUpdates · {rotulo}", now, CANAL_PAIS, MIN_CAPS))
                if len(recs) < 50:
                    break
        log(f"   MangaUpdates · {rotulo}: {len(out) - n0}")
    return out


def enriquecer(c, cache):
    """categorias + nomes + capítulos do MU numa obra que veio do AniList/planilha/YouTube."""
    if c.get("mu_id"):
        return c
    sid = None
    for n in (c.get("nomes") or [c["titulo"]])[:2]:
        sid = procurar(n, cache)
        if sid:
            break
    if not sid:
        return c
    det = detalhe(sid, cache)
    c["mu_id"] = sid
    c["tags"] = list(dict.fromkeys((c.get("tags") or []) + det["categorias"]))
    c["nomes"] = list(dict.fromkeys((c.get("nomes") or []) + _ordem(det["nomes"])))
    if det.get("caps") and (c.get("caps") is None or c.get("caps_est")):
        c["caps"], c["caps_est"] = det["caps"], False
    if not c.get("sinopse"):
        c["sinopse"] = _texto(det["descricao"])[:700]
    c["link_mu"] = det.get("url")
    return c
