"""Tipos de história × views (estudo de 28/11/2026, 2.976 vídeos de 23 canais do tracker).

Cada obra recebe os tipos que tem (título/nomes, sinopse e tags do AniList) e um MULTIPLICADOR para a nota:
a média (geométrica) dos efeitos isolados desses tipos (regressão: desconta os tipos que andam juntos). Média e
não produto: uma sinopse longa bate ~6 tipos e o produto inflava toda obra; a média diz "os tipos desta obra
rendem, em média, X" e fica na faixa da própria tabela (~0.8× a ~1.4×). A tabela fica em cacador_saida/tipos_historia.json, que
também vira a aba `Ranking de tipos` da planilha do caçador.
"""
import json
import math
import re
from pathlib import Path

ARQ = Path(__file__).parent / "cacador_saida" / "tipos_historia.json"
MULT_MIN, MULT_MAX = 0.75, 1.6

# tipo: (regex para título/nomes, regex para a sinopse — None = a mesma, "" = não olha a sinopse, tags AniList)
TIPOS = {
    "Reencarnação / renascimento": (r"reincarnat|reborn|rebirth|born again|second life|new life", None, {"Reincarnation"}),
    "Regressão / volta no tempo": (r"regress|back in time|back to the past|returns? to (?:the )?past|time loop|went back|second chance|goes back", None, {"Time Manipulation"}),
    "Transmigração (vira personagem de livro/jogo)": (r"transmigrat|possess|inside (?:a|the|his) (?:novel|game|book)|became the (?:villain|extra)|in a novel", None, set()),
    "Isekai / invocado para outro mundo": (r"isekai|summoned|another world|transported|other world", None, {"Isekai"}),
    "Nobreza / família nobre": (r"\bnoble|duke|duchess|\bcount\b|marquis|aristocra|young master|\bheir\b|baron", None, {"Royal Affairs"}),
    "Realeza (príncipe, rei, imperador)": (r"prince|princess|\bking\b|emperor|empress|royal|throne|kingdom", r"prince|princess|\bking\b|emperor|empress|royal|throne", set()),
    "Protagonista apelão (OP)": (r"overpowered|\bop\b|strongest|invincib|absurdly strong|god[- ]?level|sss|maxed|max level|level 9999|99x|100x|1000x|unbeatable|unstoppable",
                                 r"overpowered|strongest|invincib|unrivaled|unmatched|god[- ]level|absurd(?:ly)? (?:strong|power)", set()),
    "Fraco / desprezado que vira forte": (r"weakest|\btrash\b|useless|loser|f[- ]rank|e[- ]rank|zero talent|no talent|mocked|underestimat|worthless|\bweak\b|ignored|looked down",
                                          r"weakest|\btrash\b|useless|worthless|f[- ]rank|e[- ]rank|no talent|talentless|looked down|despised|mocked", set()),
    "Sistema / skill / status": (r"system|\bskill|stats?\b|level[s]? up|leveling|status window|\bclass\b|talent", r"\bsystem\b|status window|\bskills?\b|level(?:s|ing)? up", set()),
    "Mundo de game / jogador": (r"\bplayer|\bgame\b|\bnpc|\bquest|tutorial|gamer", None, {"Video Games", "Virtual World"}),
    "Caçador / portais / dungeon": (r"hunter|\bgates?\b|dungeon|\braid|\btower\b|floor", r"hunter|\bgates?\b|dungeon|\braid", {"Dungeon"}),
    "Academia / escola": (r"academy|school|student|classmate|university|\bexam\b", None, {"School"}),
    "Vingança": (r"revenge|avenge|vengean", None, {"Revenge"}),
    "Traição / abandonado": (r"betray|backstab|abandon|dumped|left him|cheated|expelled|kicked out|exiled|banished|disowned|fired", None, set()),
    "Cultivo / murim / artes marciais": (r"cultivat|murim|martial|\bsect\b|\bqi\b|heavenly demon|\bclan\b|kung ?fu", None, {"Cultivation", "Wuxia", "Martial Arts"}),
    "Mago / magia": (r"\bmage|magic|wizard|sorcer|archmage|\bspell", None, {"Magic"}),
    "Espadachim / cavaleiro": (r"sword|blade|\bknight", None, {"Swordplay"}),
    "Necromante / mortos-vivos": (r"necromanc|undead|skeleton|lich", None, {"Necromancy"}),
    "Demônios / rei demônio / inferno": (r"demon|devil|\bhell\b|succubus", None, {"Demons"}),
    "Deuses / divino": (r"\bgods?\b|goddess|divine|heaven", None, {"Gods"}),
    "Vilão": (r"villain|\bevil\b", r"villain", {"Anti-Hero"}),
    "Herói": (r"\bhero", "", set()),
    "Apocalipse / zumbis / sobrevivência": (r"apocalyp|zombie|end of the world|survival|survive|doomsday", None, {"Post-Apocalyptic", "Zombie", "Survival"}),
    "Garotas / harém / esposas": (r"\bgirls?\b|\bwi(?:fe|ves)\b|harem|waifu|beaut|\bhot\b|seduc|girlfriend|fianc|bride|\bdate\b|yandere|women",
                                  r"harem|\bwives\b", {"Female Harem"}),
    "Garota monstro / elfa / fantasma": (r"monster girl|demon girl|ghost girl|slime girl|succubus|\belf\b|elves|vampire girl", r"monster girls?|succubus|\belf\b|elves|ghost girl|slime girl", {"Monster Girl", "Elf"}),
    "Ecchi / fanservice": (r"\bhorny|agitated|aroused|naughty|lewd|nude|naked|bath", "", {"Ecchi", "Nudity"}),
    "Mundo de gênero invertido": (r"gender|reversed|women rule|world where women|inverted|only man|only guy|only male", r"gender|reversed|women rule|only man|only male", set()),
    "Identidade escondida / ninguém sabe": (r"hidden|secret|disguis|pretend|nobody knows|no one knows|no idea|doesn.t know|in secret",
                                            r"hid(?:es|ing|den) (?:his|her) (?:identity|power|strength|true)|secret identity|disguis", set()),
    "Por acidente / mal-entendido": (r"accident|by mistake|misunderstand|thinks he|unknowingly|without knowing", r"misunderstand|by accident|accidentally|unknowingly", set()),
    "Família (irmã, mãe, filha)": (r"family|sister|mother|\bmom\b|father|\bdad\b|parents|daughter|brother",
                                   r"(?:his|her) (?:little |younger )?(?:sister|daughter|mother|mom)\b|(?:save|protect) (?:his|her) family", {"Family Life"}),
    "Dinheiro / rico / empresa": (r"\brich|money|billion|million|wealth|chaebol|\bceo\b|company|business", None, {"Economics"}),
    "Chef / culinária": (r"\bchef|\bcook|\bfood|restaurant", None, {"Food"}),
    "Médico / curandeiro": (r"doctor|healer|\bheal|medic", None, set()),
    "Ferreiro / alquimista / artesão": (r"blacksmith|\bcraft|forge|alchemi|smith", None, set()),
    "Fazenda / vida tranquila": (r"\bfarm|slow life|peaceful|retire|relax", r"\bfarm|slow life", {"Slice of Life"}),
    "Treinou por N anos": (r"trained|\d[\d,]* ?years?|centur", r"(?:trained|training|cultivat\w*) (?:for )?(?:\d[\d,]*|a thousand|ten thousand|hundreds of|thousands of) years", {"Time Skip"}),
    "Invocações / bestas / domador": (r"summon|\bpet|\bbeast|tamer|dragon", None, {"Dragons"}),
    "Militar / guerra": (r"soldier|\barmy|military|general\b|\bwar\b|sergeant", r"soldier|\barmy\b|military|\bwar\b", {"Military", "War"}),
    "Assassino / mercenário": (r"assassin|killer|mercenar", None, {"Assassins"}),
    "Criança / bebê prodígio": (r"\bbaby|\bkid\b|child|year[- ]old|\byrs?\b|y/o|genius", r"\bbab(?:y|ies)|infant|\bchild\b|year[- ]old|prodigy|genius", set()),
    "Morte / morre e volta": (r"\bdies\b|\bdied\b|\bdeath|killed|immortal", "", set()),
    "Torre / andares": (r"\btower\b|floor", r"\btower\b", set()),
    "Sobrenatural / fantasmas": (r"ghost|spirit|curse", None, {"Supernatural"}),
    "Ficção científica / tecnologia": (r"robot|cyborg|space|alien|\bai\b|mech", r"robot|cyborg|alien|spaceship|\bmech", {"Sci-Fi", "Mecha"}),
    "Comédia": (r"funny|hilarious", "", {"Comedy"}),
    "Terror / gore": (r"horror|gore|creepy", r"horror|gore", {"Horror", "Gore"}),
    "Romance": (r"love|romance|marri|kiss", "", {"Romance", "Heterosexual"}),
    "Bullying / humilhação": (r"bull(?:y|ied)|humiliat|laughed at|made fun", r"bull(?:y|ied|ying)|humiliat|ridiculed", {"Bullying"}),
    "Gestão de reino / território": (r"territor|lord\b|kingdom building|build(?:s|ing)? (?:a|his) (?:kingdom|empire|city)", None, {"Kingdom Management"}),
    "Protagonista mulher": (r"\bshe\b|\bher\b|girl who|woman who", "", {"Female Protagonist"}),
}
_RE = {k: (re.compile(t, re.I), re.compile(s, re.I) if s else (re.compile(t, re.I) if s is None else None), tags)
       for k, (t, s, tags) in TIPOS.items()}
_TABELA = None


def tabela():
    """{"meta": {...}, "ranking": [{pos, tipo, rende, isolado, lo, hi, certeza, videos, obras, canais}]}"""
    global _TABELA
    if _TABELA is None:
        _TABELA = json.loads(ARQ.read_text(encoding="utf-8")) if ARQ.exists() else {"meta": {}, "ranking": []}
    return _TABELA


def tipos_de(c):
    """tipos da obra pelo título/nomes (palavras do gancho), sinopse (versão mais estrita) e tags do AniList."""
    titulo = " ".join([c.get("titulo") or "", *(c.get("nomes") or [])])
    sinopse = c.get("sinopse") or ""
    tags = set(c.get("tags") or []) | set(c.get("generos") or [])
    achou = []
    for nome, (re_titulo, re_sinopse, tags_tipo) in _RE.items():
        if re_titulo.search(titulo) or (re_sinopse and re_sinopse.search(sinopse)) or (tags & tags_tipo):
            achou.append(nome)
    return achou


def multiplicador(c):
    """-> (multiplicador da nota, [tipos da obra do que mais rende ao que menos])."""
    efeito = {r["tipo"]: r["isolado"] for r in tabela()["ranking"]}
    tipos = sorted((t for t in tipos_de(c) if t in efeito), key=lambda t: -efeito[t])
    mult = math.exp(sum(math.log(efeito[t]) for t in tipos) / len(tipos)) if tipos else 1.0
    return round(min(MULT_MAX, max(MULT_MIN, mult)), 3), tipos


def texto(c):
    """'1.32× · Nobreza / família nobre, Mago / magia, …' para a planilha."""
    mult, tipos = c.get("mult_tipo"), c.get("tipos_historia")
    if mult is None:
        mult, tipos = multiplicador(c)
    return f"{mult:.2f}×" + (" · " + ", ".join(tipos) if tipos else "")
