"""Caçador de Obras — rodada noturna com agente (Codex + gpt-6-astra pela assinatura, sem API paga).

Fases (o cacador_noite.ps1 chama nesta ordem):
    python cacador_noite.py fase1    -> coleta (AniList + planilha + DESCOBERTA NO YOUTUBE), sem checar
                                        cobertura; gera fila_nomes.json e fila_notas.json para o agente
    [agente A]                       -> nomes_agente.json (obra de cada vídeo) + notas_agente.json
    python cacador_noite.py fase2    -> ranking completo + checagem no YouTube + top_dossie.json
    [agente B]                       -> dossies.json (pesquisa a fundo as melhores)
    python cacador_noite.py html     -> recomendadas.html final com os dossiês

Ferramentas para o agente (imprimem JSON):
    python cacador_noite.py video ID                 título, canal, views, data, descrição, comentários
    python cacador_noite.py yt "busca"               resultados da busca do YouTube
    python cacador_noite.py obra "nome"              AniList + Comick (nomes, país, capítulos, sinopse)
    python cacador_noite.py cobertura "n1" ["n2"]    recaps longos em inglês dessa obra no YouTube
"""
import json
import re
import sys
import time
from datetime import datetime, timezone

import cacador as C
from comick import normalize

SP_ANO = "CAMSBAgFEAE="        # mais vistos, este ano, só vídeo
SP_TUDO = "CAMSBBgCEAE="       # mais vistos, longos, todos os tempos
SP_RELEVANCIA = None           # ordem normal do YouTube: traz canal médio/pequeno, não só os gigantes
QUERIES = [
    # manhwa
    "manhwa recap", "full manhwa recap", "regression manhwa recap", "system manhwa recap", "murim manhwa recap",
    "reincarnated manhwa recap", "overpowered mc manhwa recap", "weakest to strongest manhwa recap",
    "revenge manhwa recap", "hunter manhwa recap", "tower manhwa recap", "academy manhwa recap",
    "villain manhwa recap", "necromancer manhwa recap", "sss rank manhwa recap", "returned manhwa recap",
    "dungeon manhwa recap", "genius manhwa recap", "demon king manhwa recap", "transmigrated manhwa recap",
    "player manhwa recap", "level up manhwa recap", "zombie manhwa recap", "chaebol manhwa recap",
    "military manhwa recap", "sword master manhwa recap", "mage manhwa recap", "healer manhwa recap",
    # manhua
    "manhua recap", "cultivation manhua recap", "apocalypse manhua recap", "martial arts manhua recap",
    "system manhua recap", "sect manhua recap", "immortal manhua recap", "doomsday manhua recap",
    "beast tamer manhua recap", "urban cultivation manhua recap", "xianxia manhua recap", "god level manhua recap",
    # mangá
    "manga recap", "isekai manga recap", "op mc manga recap", "reincarnation manga recap", "dark fantasy manga recap",
    "revenge manga recap", "dungeon manga recap", "system manga recap", "overpowered manga recap",
    "monster manga recap", "seinen manga recap", "full manga recap",
]
SP_FILTROS = (SP_ANO, SP_TUDO, SP_RELEVANCIA)
POR_CANAL = 3                  # máx. de vídeos por canal: canal gigante não domina a descoberta
DOSSIES_POR_NOITE = 30
# dossiês por noite, por aba e tipo (o que sobrar de uma cota vai para as melhores da aba)
COTAS = {C.ABA_MANHWA: {"Testada": 5, "Arquétipo ⭐": 3, "Descoberta (YouTube)": 3, "Nova": 2, "Clássica": 2},
         C.ABA_MANHUA: {"Testada": 3, "Arquétipo ⭐": 2, "Descoberta (YouTube)": 2, "Nova": 2, "Clássica": 1},
         C.ABA_MANGA: {"Testada": 2, "Arquétipo ⭐": 2, "Descoberta (YouTube)": 2, "Nova": 2, "Clássica": 2}}
MIN_VIEWS = 50_000
MIN_IDADE = 170               # dias: vídeo mais novo que isso bloqueia a obra (regra dos 6 meses)
MAX_DESC = 260                # descrições abertas por noite (o resto fica no cache para a próxima)

_NOME_DESC = re.compile(
    r"(?im)^[^\w\n]*(?:manhwa|manhua|manga|webtoon|comic|series|story|novel|original)?\s*(?:name|title)?"
    r"\s*(?:name|title|manhwa|manhua|manga)\s*[:：\-–=]+\s*(.{3,120})$")
_SUJEIRA = re.compile(r"(?i)\b(manhwa|manhua|manga|full|recap|recaps|explained|summary|completed?|season \d+|s\d-\d|"
                      r"chapters?|ch\.?|episodes?|ep)\b|[\[\(][^\]\)]*[\]\)]|#\S+|[^\w\s'’:,!?.-]")


_ANIME = re.compile(r"(?i)\banime\b|\bnovel\b|\bmovie\b|\bseries explained\b")
_QUADRINHO = re.compile(r"(?i)manhwa|manhua|manga|webtoon|webcomic|comic")


def log(*a):
    print(*a, flush=True)


def _limpo(t):
    t = _SUJEIRA.sub(" ", t or "")
    return re.sub(r"\s+", " ", t).strip(" -–|:,.")


def nomes_do_video(v):
    """palpites de nome da obra a partir da descrição e do título."""
    out = []
    for m in _NOME_DESC.finditer(v.get("desc") or ""):
        n = _limpo(re.split(r"\s+[|/]\s+|https?://", m.group(1))[0])
        if 3 <= len(n) <= 100:
            out.append(n)
    for parte in re.split(r"\s*[|｜]\s*|\s+-\s+|- ", v.get("titulo") or ""):
        n = _limpo(parte)
        if len(n.split()) >= 3 and not re.search(r"(?i)\b(when|after|he|his|she|they|got|became)\b", n.split()[0]):
            out.append(n)
    return list(dict.fromkeys(out))[:4]


def _cand_generico(nomes, cm, prova, now):
    pais = cm["pais"] if cm and cm.get("pais") in C.CANAL_PAIS else None
    base = (cm or {}).get("titulo") or nomes[0]
    return {"id": "y" + normalize(base).replace(" ", "_")[:60], "titulo": base,
            "nomes": C.ordem_nomes(((cm or {}).get("nomes") or []) + nomes),
            "pais": pais, "canal": C.CANAL_PAIS.get(pais, "?"), "generos": [], "tags": [], "sinopse": "",
            "caps": (cm or {}).get("caps"), "caps_est": False, "status_obra": "", "popularidade": 0,
            "capa": (cm or {}).get("capa") or C._yt_thumb(prova["link"]),
            "link": f"https://comick.dev/comic/{cm['slug']}" if cm and cm.get("slug") else prova["link"],
            "fonte": "YouTube", "inicio": ""}


def _resolver(nomes, cache_ani, now, prova):
    """nome -> candidata (AniList > Comick > só o nome que o agente deu)."""
    for n in nomes[:2]:
        cm = C.comick_busca(n, cache_ani)
        if cm:
            m = C.ani_busca(cm["titulo"], cache_ani) or C.ani_busca(n, cache_ani)
            if m:
                return C._cand_de_media(m, "YouTube", now)
            return _cand_generico([n], cm, prova, now)
    m = C.ani_busca(nomes[0], cache_ani) if nomes else None
    if m:
        return C._cand_de_media(m, "YouTube", now)
    return None


def descobrir(cache_ani, cache_yt, idx, now):
    """busca recaps longos em inglês que explodiram há 6+ meses e acha a obra de cada um."""
    conhecidos, monitorados = set(), set(C.NOSSOS)
    for o in idx.exato.values():
        for x in o:
            for v in x["videos"]:
                monitorados.add(normalize(v["canal"]))
                m = re.search(r"([\w-]{11})$", v.get("link") or "")
                if m:
                    conhecidos.add(m.group(1))
    achados = {}
    k = "desc_busca3|" + datetime.now().strftime("%Y-%m-%d")
    if k in cache_yt:
        achados = cache_yt[k]
    else:
        log(f"Descoberta no YouTube: {len(QUERIES)} buscas x {len(SP_FILTROS)} filtros…")
        for q in QUERIES:
            for sp in SP_FILTROS:
                try:
                    res = C.yt_busca(q, sp)
                except Exception as e:
                    log("   erro busca:", str(e)[:80])
                    continue
                for v in res:
                    if (v["dur"] >= 40 * 60 and v["views"] >= MIN_VIEWS and (v["idade"] or 0) >= MIN_IDADE
                            and not C._NAO_EN.search(v["titulo"]) and normalize(v["canal"]) not in monitorados):
                        achados.setdefault(v["id"], v)
                time.sleep(0.6)
        cache_yt[k] = achados
        C._salva("youtube", cache_yt)
    log(f"   {len(achados)} recaps longos com {MIN_VIEWS:,}+ views e 6+ meses, de canais que você NÃO monitora"
        .replace(",", "."))
    novos, por_canal = [], {}
    for v in sorted(achados.values(), key=lambda v: -v["views"]):
        if v["id"] in conhecidos or normalize(v["canal"]) in monitorados:
            continue
        if por_canal.get(v["canal"], 0) >= POR_CANAL:
            continue
        por_canal[v["canal"]] = por_canal.get(v["canal"], 0) + 1
        novos.append(v)
    log(f"   {len(novos)} vídeos de {len(por_canal)} canais (máx. {POR_CANAL} por canal)")
    agente = C._cache("nomes_agente")
    fila, cands, abertos = [], {}, 0
    for v in sorted(novos, key=lambda v: -v["views"]):
        kv = "vid|" + v["id"]
        if kv not in cache_yt and abertos < MAX_DESC:
            try:
                desc, pub = C.yt_video(v["id"])
                cache_yt[kv] = {"_t": time.time(), "desc": desc[:3000], "pub": pub.isoformat() if pub else None}
                abertos += 1
            except Exception:
                continue
        if kv not in cache_yt:
            continue
        v = {**v, "desc": cache_yt[kv]["desc"]}
        if _ANIME.search(v["titulo"]) or not _QUADRINHO.search(v["titulo"] + " " + v["desc"]):
            continue                     # recap de anime/novel, não de manhwa/manhua/mangá
        if cache_yt[kv].get("pub"):
            v["idade"] = (now - datetime.fromisoformat(cache_yt[kv]["pub"])).total_seconds() / 86400
        prova = {"views": v["views"], "canal": v["canal"], "idade": v["idade"] or 0,
                 "link": f"https://youtu.be/{v['id']}", "titulo": v["titulo"],
                 "subs": C.canal_inscritos(v.get("canal_id"), cache_yt)}
        ag = agente.get(v["id"])
        if ag is not None:
            nomes = [re.sub(r"(?<=\w)\?(?=\w)", "'", n) for n in [ag.get("obra")] + (ag.get("outros_nomes") or []) if n]
            if not nomes:
                continue            # o agente olhou e não achou
        else:
            nomes = nomes_do_video(v)
        c = None
        if nomes:
            achadas = idx.achar(nomes)           # já está na planilha com outro vídeo? usa os nomes de lá
            if achadas:
                nomes = C.ordem_nomes(nomes + [n for a in achadas for n in a["nomes"]])
            c = _resolver(nomes, cache_ani, now, prova)
            if c is None and ag and ag.get("obra"):
                c = _cand_generico(nomes, None, prova, now)
        if c is None:
            fila.append({"video_id": v["id"], "titulo": v["titulo"], "canal": v["canal"], "views": v["views"],
                         "meses": round((v["idade"] or 0) / 30.4, 1), "descricao": v["desc"][:700],
                         "palpites": nomes})
            continue
        c["fonte"] = "Descoberta (YouTube)"
        c["prova_yt"] = prova
        atual = cands.get(c["id"])
        if not atual or prova["views"] > atual["prova_yt"]["views"]:
            cands[c["id"]] = c
    C._salva("youtube", cache_yt)
    C._salva("fila_nomes", {"videos": fila})
    log(f"   {len(cands)} obras identificadas; {len(fila)} vídeos sem nome foram para fila_nomes.json")
    return list(cands.values())


def novas_do_tracker(cache_ani, idx, now, limite=120):
    """aba `Novas Obras Shonen` do tracker: obras que acabaram de entrar nos sites de scan. Entram as que já
    têm capítulos para um vídeo e ainda não têm vídeo nos canais monitorados."""
    try:
        rows = C.ler_aba("Novas Obras Shonen")
    except Exception as e:
        log("   Novas Obras: erro", str(e)[:80])
        return []
    out = []
    for r in rows[:limite]:
        caps = C._int(r.get("Capítulos")) or 0
        nome = (r.get("Obra") or "").strip()
        if not nome or caps < C.MIN_CAPS or (r.get("Já tem vídeo") or "").strip() == "Sim" or idx.achar([nome]):
            continue
        m = C.ani_busca(nome, cache_ani)
        if m:
            if m.get("isAdult") or set(m.get("genres") or []) & set(C.GENEROS_FORA):
                continue
            c = C._cand_de_media(m, "Nova", now)
        else:
            cm = C.comick_busca(nome, cache_ani)
            c = _cand_generico([nome], cm, {"link": r.get("Link") or ""}, now)
            c["link"] = r.get("Link") or c["link"]
            c["generos"] = [g.strip() for g in (r.get("Gêneros") or "").split(",") if g.strip()]
        c["fonte"] = "Nova"
        c["caps"] = max(c.get("caps") or 0, caps)
        c["caps_est"] = False
        out.append(c)
    log(f"   {len(out)} obras novas do tracker (sites de scan) com {C.MIN_CAPS}+ capítulos e sem vídeo")
    return out


def extras(cache_ani, cache_yt, idx, now):
    import mangaupdates as MU
    try:
        log("MangaUpdates: buscas por arquétipo e premissa…")
        mu = MU.pools(cache_ani, now, C.CANAL_PAIS, C.MIN_CAPS)
        log(f"   {len(mu)} obras do MangaUpdates")
    except Exception as e:
        log("   MangaUpdates fora do ar:", str(e)[:100])
        mu = []
    return mu + descobrir(cache_ani, cache_yt, idx, now) + novas_do_tracker(cache_ani, idx, now)


# ---------------------------------------------------------------- fases

def escolher_para_dossie(vivos, dossies):
    """cotas por aba e tipo (testada, descoberta, nova, clássica): a lista não fica só com o que os canais
    monitorados já fizeram. Cada escolhida é conferida no YouTube antes; TOMADA não entra."""
    cache_yt = C._cache("youtube")
    monitorados = {normalize(r.get("canal", "")) for r in C.ler_aba("todos")}
    escolhidas, checadas = [], 0

    def ok(c):
        nonlocal checadas
        if "yt" not in c:
            c["yt"] = C.cobertura(c["nomes"], cache_yt, monitorados)
            C.pontuar(c)
            checadas += 1
        return c["yt"]["status"] not in ("TOMADA", "JÁ FIZEMOS") and not c.get("sem_nota")

    for aba, cotas in COTAS.items():
        da_aba = [c for c in vivos if C.aba_de(c) == aba and str(c["id"]) not in dossies]
        pegas = []
        for tipo, n in cotas.items():
            tentou = 0
            for c in da_aba:
                if len([x for x in pegas if C.tipo_de(x) == tipo]) >= n or tentou >= 3 * n + 5:
                    break
                if C.tipo_de(c) != tipo or c in pegas:
                    continue
                tentou += 1
                if ok(c):
                    pegas.append(c)
        sobra = sum(cotas.values()) - len(pegas)
        for c in da_aba:
            if sobra <= 0:
                break
            if c not in pegas and ok(c):
                pegas.append(c)
                sobra -= 1
        log(f"   {aba}: {len(pegas)} para dossiê " + str({t: sum(1 for x in pegas if C.tipo_de(x) == t) for t in cotas}))
        escolhidas += pegas
    C._salva("youtube", cache_yt)
    log(f"   ({checadas} conferidas no YouTube para as cotas)")
    return escolhidas


def fase(max_yt):
    vivos = C.cacar(max_yt=max_yt, extras_fn=extras, sem_api=True)
    # dossiê vale 7 dias: a rodada diária pesquisa as melhores que ainda não têm (ou cujo dossiê venceu)
    dossies, meta, agora = C._cache("dossies"), C._cache("dossies_meta"), time.time()
    for k in dossies:
        meta.setdefault(k, agora)
    for k in [k for k in meta if agora - meta[k] > 7 * 86400]:
        meta.pop(k)
        dossies.pop(k, None)
    C._salva("dossies_meta", meta)
    C._salva("dossies", dossies)
    escolhidas = escolher_para_dossie(vivos, dossies) if max_yt else []
    vivos.sort(key=lambda c: -c.get("final", 0))
    ls = C.linhas(vivos)
    C.salvar_local(ls)
    ids = {str(c["id"]) for c in escolhidas}
    top = [l for l in ls if str(l["id"]) in ids]
    C._salva("top_dossie", {"obras": [{k: l[k] for k in ("id", "obra", "nomes", "canal", "aba", "tipo", "nota",
                                                           "premissa", "caps", "youtube", "planilha", "nossos",
                                                           "fonte", "link")}
                                      for l in top]})
    log(f"{len(ls)} obras no ranking; top_dossie.json com {len(top)} (já com dossiê: {len(dossies)})")
    return ls


def html():
    ult = C._cache("ultimo")
    ls = ult["linhas"]
    C.salvar_local(ls)            # junta veredito/dossiê e reordena
    saida = C.exportar(ls)
    log(f"HTML refeito com {len(C._cache('dossies'))} dossiês -> {C.DIR / 'recomendadas.html'}; "
        f"lista para a planilha -> {saida}")


# ---------------------------------------------------------------- ferramentas do agente

def _comentarios(vid, n=25):
    try:
        import yt_dlp
        opts = {"quiet": True, "skip_download": True, "getcomments": True, "no_warnings": True,
                "extractor_args": {"youtube": {"max_comments": [str(n), "all", "0", "0"], "comment_sort": ["top"]}}}
        with yt_dlp.YoutubeDL(opts) as y:
            info = y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
        return [{"autor": c.get("author"), "dono": c.get("author_is_uploader"), "fixado": c.get("is_pinned"),
                 "texto": (c.get("text") or "")[:400]} for c in (info.get("comments") or [])[:n]]
    except Exception as e:
        return [{"erro": str(e)[:200]}]


def ferramenta(args):
    cmd = args[0]
    if cmd == "video":
        vid = re.search(r"([\w-]{11})$", args[1].strip()).group(1)
        desc, pub = C.yt_video(vid)
        res = [v for v in C.yt_busca(vid) if v["id"] == vid]
        out = {"id": vid, "publicado": pub.isoformat() if pub else None, "descricao": desc[:2500],
               "comentarios": _comentarios(vid)}
        if res:
            out.update({k: res[0][k] for k in ("titulo", "canal", "views", "dur")})
        return out
    if cmd == "yt":
        return [{**{k: v[k] for k in ("id", "titulo", "canal", "views", "dur")},
                 "dias": round(v["idade"]) if v["idade"] is not None else None, "minutos": v["dur"] // 60}
                for v in C.yt_busca(args[1])]
    if cmd == "obra":
        cache = C._cache("anilist")
        m, cm = C.ani_busca(args[1], cache), C.comick_busca(args[1], cache)
        C._salva("anilist", cache)
        return {"anilist": m and {"nomes": C.nomes_de(m), "pais": m.get("countryOfOrigin"), "capitulos": m.get("chapters"),
                                  "status": m.get("status"), "inicio": m.get("startDate"), "generos": m.get("genres"),
                                  "sinopse": C.sinopse(m, 900), "link": m.get("siteUrl")},
                "comick": cm}
    if cmd == "cobertura":
        r = C.cobertura(args[1:], {}, set())
        return r
    raise SystemExit(__doc__)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if not a:
        raise SystemExit(__doc__)
    if a[0] == "fase1":
        fase(0)
    elif a[0] == "fase2":
        fase(int(a[1]) if len(a) > 1 else 80)
    elif a[0] == "html":
        html()
    else:
        print(json.dumps(ferramenta(a), ensure_ascii=False, indent=1, default=str))
