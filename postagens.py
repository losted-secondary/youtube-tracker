"""Calendario de postagens dos canais Juicy e Senzu -> aba `postagens` + mensagem no Discord.

Regra: cada canal tem um rodizio de pessoas e o proximo video do canal e sempre
`ultimo post daquele canal + INTERVALO dias`. Se atrasa, a fila inteira do canal anda
junto. Os canais sao independentes (podem cair no mesmo dia).
Linha pendente nunca fica no passado: virou o dia e nao postou, a proxima_data do canal
vira HOJE (e as seguintes acompanham). A lista e pra cada um abrir e ver o seu dia.

Nada do futuro fica guardado: por canal so `proxima_data` + `proximo` (aba
`postagens_config`), e o que ja foi postado sao as linhas marcadas na aba `postagens`.
O resto e calculado a cada rodada.

Abas:
  postagens_config: canal | youtube_id | ordem | proxima_data | proximo | discord_canal |
                    discord_mensagem | _ultimo_publicado
    - `ordem` = nomes separados por virgula. Trocar aqui troca o rodizio (quem era o
      proximo continua sendo, se ainda estiver na lista).
    - `proxima_data` / `proximo` = editaveis: e assim que se "inicia" ou corrige um canal.
    - `_ultimo_publicado` = controle interno (ultimo video visto no feed). Nao mexer.
  postagens: data | dia | canal | responsavel | postado
    - reescrita inteira a cada rodada. Marcar o checkbox da PRIMEIRA linha pendente de um
      canal = "postou nessa data" na mao (caso o YouTube nao tenha sido detectado).
      Desmarcar a ULTIMA linha postada de um canal = desfazer.

Deteccao: feed RSS do YouTube (sem cota da API). Video novo -> marca postado na data de
publicacao (horario de Brasilia) e recalcula. Primeira rodada de um canal so memoriza o
feed, nao marca nada.

Comandos: o usuario escreve no proprio #calendario (`ordem juicy wood losted momo rafoso`,
`proximo senzu 14/09 losted`, `postou juicy [13/09]`, `desfazer juicy`, `ajuda`). A cada
rodada o script le as mensagens novas do canal, aplica, apaga a mensagem e responde;
a resposta e apagada na rodada seguinte (toda mensagem do bot que nao seja a tabela).
`_ultimo_comando` na config = id da ultima mensagem processada.

Discord: a tabela e UMA mensagem que o script edita via REST (nao precisa de bot ligado).
Token em `DISCORD_BOT_TOKEN`. O canal e achado pelo NOME (`CANAL_DISCORD`) em qualquer
servidor onde o bot esteja; o usuario so cria o canal de texto e pronto. Ids do canal e
da mensagem ficam na config so como cache: se o canal foi apagado e recriado, o script
acha o novo e posta de novo.
"""
import os
import re
import json
from datetime import datetime, date, timezone, timedelta

import requests

BRT = timezone(timedelta(hours=-3))
INTERVALO = 2           # dias entre videos do MESMO canal
LINHAS_FUTURAS = 15     # por canal, na tabela
LINHAS_POSTADAS = 8     # por canal, na tabela (as mais recentes)

CONFIG_TAB = "postagens_config"
CONFIG_HEADER = ["canal", "youtube_id", "ordem", "proxima_data", "proximo",
                 "discord_canal", "discord_mensagem", "_ultimo_publicado", "_ultimo_comando"]
C_CANAL, C_YT, C_ORDEM, C_PROX_DATA, C_PROXIMO, C_DC_CANAL, C_DC_MSG, C_ULTIMO, C_ULTIMO_CMD = range(9)

TABELA_TAB = "postagens"
TABELA_HEADER = ["data", "dia", "canal", "responsavel", "postou?"]
T_DATA, T_DIA, T_CANAL, T_RESP, T_POSTADO = range(5)

# estado inicial, usado so quando a aba de config nao existe ainda
DEFAULT_CONFIG = [
    ["Juicy", "UCUnLH9qyXBI8ijs9Kmbt9Ng", "Momo, Wood, Losted, Rafoso", "13/09/2026", "Momo", "", "", "", ""],
    ["Senzu", "UCOcsn9uPit7AW3QvneP3bBg", "Losted, Rafoso, Momo, Wood", "14/09/2026", "Losted", "", "", "", ""],
]

CANAL_DISCORD = "calendario"   # nome do canal de texto onde a tabela vive

DIAS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
ICON = {"ok": "✅", "pending": "⬜"}


# ---------- datas ----------
def _parse_date(s):
    """'13/09/2026' ou '13/09' -> date. Vazio/invalido -> None."""
    m = re.match(r"^\s*(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?\s*$", str(s or ""))
    if not m:
        return None
    y = m.group(3)
    y = int(y) + 2000 if y and len(y) == 2 else int(y) if y else datetime.now(BRT).year
    try:
        return date(y, int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


def _fmt(d):
    return d.strftime("%d/%m/%Y")


def _today():
    return datetime.now(BRT).date()


# ---------- feed do YouTube ----------
def fetch_feed(channel_id):
    r = requests.get(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}", timeout=20)
    r.raise_for_status()
    entries = []
    for m in re.finditer(r"<entry>([\s\S]*?)</entry>", r.text):
        pub = re.search(r"<published>(.*?)</published>", m.group(1))
        title = re.search(r"<title>([\s\S]*?)</title>", m.group(1))
        if pub:
            entries.append({"published": pub.group(1), "title": title.group(1) if title else ""})
    return sorted(entries, key=lambda e: e["published"])


# ---------- abas ----------
def _pad(row, n):
    row = list(row)
    return row + [""] * (n - len(row)) if len(row) < n else row[:n]


def _col(i):
    return chr(65 + i)


def ensure_tabs(spreadsheet):
    import gspread
    try:
        cfg = spreadsheet.worksheet(CONFIG_TAB)
    except gspread.WorksheetNotFound:
        cfg = spreadsheet.add_worksheet(title=CONFIG_TAB, rows=len(DEFAULT_CONFIG) + 1, cols=len(CONFIG_HEADER))
        cfg.update([CONFIG_HEADER] + DEFAULT_CONFIG, "A1", value_input_option="RAW")
        sid = cfg.id
        spreadsheet.batch_update({"requests": [
            # aba escondida: o usuario nao quer ver (Planilha > Ver > Abas ocultas pra abrir)
            {"updateSheetProperties": {"properties": {"sheetId": sid, "hidden": True, "gridProperties": {"frozenRowCount": 1}},
                                       "fields": "hidden,gridProperties.frozenRowCount"}},
            {"updateDimensionProperties": {
                "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": C_ULTIMO, "endIndex": len(CONFIG_HEADER)},
                "properties": {"hiddenByUser": True}, "fields": "hiddenByUser"}},
        ]})
    if cfg.col_count < len(CONFIG_HEADER):  # config antiga sem as colunas novas
        cfg.add_cols(len(CONFIG_HEADER) - cfg.col_count)
        cfg.update([CONFIG_HEADER], "A1", value_input_option="RAW")
    try:
        tab = spreadsheet.worksheet(TABELA_TAB)
    except gspread.WorksheetNotFound:
        tab = spreadsheet.add_worksheet(title=TABELA_TAB, rows=2, cols=len(TABELA_HEADER))
        tab.update([TABELA_HEADER], "A1", value_input_option="RAW")
        sid = tab.id
        spreadsheet.batch_update({"requests": [
            {"updateSheetProperties": {"properties": {"sheetId": sid, "gridProperties": {"frozenRowCount": 1}},
                                       "fields": "gridProperties.frozenRowCount"}},
            {"setDataValidation": {
                "range": {"sheetId": sid, "startRowIndex": 1, "startColumnIndex": T_POSTADO, "endColumnIndex": T_POSTADO + 1},
                "rule": {"condition": {"type": "BOOLEAN"}, "strict": False}}},
        ]})
    return cfg, tab


def _as_bool(v):
    return str(v).strip().upper() == "TRUE"


# ---------- regras ----------
class Canal:
    def __init__(self, row):
        self.row = _pad(row, len(CONFIG_HEADER))
        self.nome = self.row[C_CANAL].strip()
        self.youtube_id = self.row[C_YT].strip()
        self.ordem = [p.strip() for p in re.split(r"[,;\n]+", self.row[C_ORDEM]) if p.strip()]
        self.proxima_data = _parse_date(self.row[C_PROX_DATA])
        self.proximo = self.row[C_PROXIMO].strip()
        self.ultimo_publicado = self.row[C_ULTIMO].strip()
        self.postados = []   # [(date, pessoa)] em ordem cronologica
        self.eventos = []

    @property
    def ativo(self):
        return bool(self.proxima_data and self.ordem)

    def _idx(self, pessoa):
        for i, p in enumerate(self.ordem):
            if p.lower() == str(pessoa).strip().lower():
                return i
        return -1

    def _proximo_idx(self):
        i = self._idx(self.proximo)
        return i if i >= 0 else 0

    def marcar_postado(self, d, motivo):
        if not self.ativo:
            return None
        i = self._proximo_idx()
        pessoa = self.ordem[i]
        self.postados.append((d, pessoa))
        self.proximo = self.ordem[(i + 1) % len(self.ordem)]
        self.proxima_data = d + timedelta(days=INTERVALO)
        self.eventos.append(f"[{self.nome}] {pessoa} postou em {_fmt(d)} ({motivo})")
        return pessoa

    def set_ordem(self, pessoas):
        atual = self.ordem[self._proximo_idx()] if self.ordem else ""
        self.ordem = pessoas
        self.proximo = atual if self._idx(atual) >= 0 else pessoas[0]
        self.eventos.append(f"[{self.nome}] ordem: {', '.join(pessoas)} (proximo: {self.proximo})")

    def set_proximo(self, d, pessoa):
        if self._idx(pessoa) < 0:
            raise ValueError(f"{pessoa} não está na ordem de {self.nome}: {', '.join(self.ordem)}")
        self.proxima_data = d
        self.proximo = self.ordem[self._idx(pessoa)]
        self.eventos.append(f"[{self.nome}] proximo: {self.proximo} em {_fmt(d)}")

    def desfazer(self):
        if not self.postados:
            return None
        d, pessoa = self.postados.pop()
        self.proximo = pessoa
        self.proxima_data = d
        self.eventos.append(f"[{self.nome}] desfeito: {pessoa} em {_fmt(d)}")
        return d, pessoa

    def correr(self):
        """Nao postou no dia previsto -> o proximo vira hoje e a fila do canal anda junto."""
        hoje = _today()
        if self.proxima_data and self.proxima_data < hoje:
            self.eventos.append(f"[{self.nome}] {self.proximo} nao postou em {_fmt(self.proxima_data)}, vai pra {_fmt(hoje)}")
            self.proxima_data = hoje

    def linhas(self):
        out = [(d, self.nome, p, "ok") for d, p in self.postados[-LINHAS_POSTADAS:]]
        if self.ativo:
            i = self._proximo_idx()
            for k in range(LINHAS_FUTURAS):
                d = self.proxima_data + timedelta(days=k * INTERVALO)
                out.append((d, self.nome, self.ordem[(i + k) % len(self.ordem)], "pending"))
        return out

    def to_row(self):
        r = list(self.row)
        r[C_ORDEM] = ", ".join(self.ordem)
        r[C_PROX_DATA] = _fmt(self.proxima_data) if self.proxima_data else ""
        r[C_PROXIMO] = self.proximo
        r[C_ULTIMO] = self.ultimo_publicado
        return r


def _linhas_ordenadas(canais):
    rows = [l for c in canais for l in c.linhas()]
    rows.sort(key=lambda l: (l[0], 0 if l[3] == "ok" else 1, l[1]))
    return rows


def render_discord(canais):
    rows = _linhas_ordenadas(canais)
    if not rows:
        return "Nenhum canal iniciado. Preencha `proxima_data` e `proximo` na aba `postagens_config`."
    w1 = max([5] + [len(r[1]) for r in rows])
    w2 = max([6] + [len(r[2]) for r in rows])
    head = f"{'Data':<9}  {'Canal':<{w1}}  {'Pessoa':<{w2}}  Postou?"
    lines = [f"{DIAS[d.weekday()]} {d:%d/%m}  {c:<{w1}}  {p:<{w2}}  {ICON[s]}" for d, c, p, s in rows]
    return "```\n" + head + "\n" + "-" * len(head) + "\n" + "\n".join(lines) + "\n```"


# ---------- Discord (REST, sem gateway) ----------
DISCORD_API = "https://discord.com/api/v10"


def _discord(method, path, token, **kw):
    r = requests.request(method, DISCORD_API + path, headers={"Authorization": f"Bot {token}"}, timeout=20, **kw)
    if not r.ok:
        raise RuntimeError(f"Discord {method} {path}: {r.status_code} {r.text[:200]}")
    return r.json() if r.text else {}


def find_channel(token):
    """Id do primeiro canal de texto chamado CANAL_DISCORD nos servidores do bot."""
    for g in _discord("GET", "/users/@me/guilds", token):
        for c in _discord("GET", f"/guilds/{g['id']}/channels", token):
            if c.get("type") == 0 and c.get("name", "").lower() == CANAL_DISCORD:
                return c["id"]
    return None


AJUDA = (
    "**Comandos** (escreve aqui no canal, o bot lê em até 10 min):\n"
    "`ordem juicy wood losted momo rafoso` — troca o rodízio do canal\n"
    "`proximo senzu 14/09 losted` — define o próximo vídeo do canal\n"
    "`postou juicy` ou `postou juicy 13/09` — marca o próximo como postado\n"
    "`desfazer juicy` — desfaz a última marcação\n"
    "`ajuda` — isso"
)


def aplicar_comando(canais, texto):
    """Devolve a resposta pro usuario (None = nao era comando). ValueError = erro pro usuario."""
    partes = [p for p in re.split(r"[\s,;\-]+", texto.strip()) if p]
    if not partes:
        return None
    cmd = partes[0].lower().lstrip("/!")
    if cmd in ("ajuda", "help"):
        return AJUDA
    if cmd not in ("ordem", "proximo", "próximo", "iniciar", "postou", "desfazer"):
        return None  # conversa normal, ignora
    if len(partes) < 2:
        raise ValueError(f"faltou o canal. Ex: `{cmd} juicy`")
    c = next((c for c in canais if c.nome.lower() == partes[1].lower()), None)
    if not c:
        raise ValueError(f"canal `{partes[1]}` não existe. Tem: {', '.join(x.nome for x in canais)}")
    args = [a[:1].upper() + a[1:] for a in partes[2:]]  # wood -> Wood
    if cmd == "ordem":
        if not args:
            return f"Ordem de {c.nome}: {' → '.join(c.ordem)} (próximo: {c.proximo})"
        c.set_ordem(args)
        return f"{c.nome}: ordem agora é {' → '.join(c.ordem)}. Próximo: {c.proximo}."
    if cmd in ("proximo", "próximo", "iniciar"):
        if len(args) < 2 or not _parse_date(args[0]):
            raise ValueError(f"use `proximo {c.nome.lower()} dd/mm pessoa`")
        c.set_proximo(_parse_date(args[0]), args[1])
        return f"{c.nome}: próximo vídeo {_fmt(c.proxima_data)} por {c.proximo}."
    if cmd == "postou":
        d = _parse_date(args[0]) if args else _today()
        if not d:
            raise ValueError("data inválida, use dd/mm")
        pessoa = c.marcar_postado(d, "comando no Discord")
        if not pessoa:
            raise ValueError(f"{c.nome} não tem próximo definido. Use `proximo {c.nome.lower()} dd/mm pessoa`")
        return f"{c.nome}: {pessoa} marcado como postado em {_fmt(d)}."
    if cmd == "desfazer":
        r = c.desfazer()
        if not r:
            raise ValueError(f"{c.nome} não tem nada pra desfazer")
        return f"{c.nome}: desfeito {r[1]} em {_fmt(r[0])}."


def processar_comandos(canais, token, canal_id, msg_tabela, ultimo_id):
    """Le mensagens novas do canal, aplica comandos, apaga o que processou.
    Devolve o id da ultima mensagem vista."""
    msgs = _discord("GET", f"/channels/{canal_id}/messages?limit=50", token)
    msgs.sort(key=lambda m: int(m["id"]))
    respostas = []
    for m in msgs:
        if m["author"].get("bot"):
            if m["id"] != msg_tabela:  # resposta da rodada passada: some
                _discord("DELETE", f"/channels/{canal_id}/messages/{m['id']}", token)
            continue
        if int(m["id"]) <= int(ultimo_id or 0):
            continue
        ultimo_id = m["id"]
        try:
            resp = aplicar_comando(canais, m.get("content", ""))
        except ValueError as e:
            resp = f"❌ {e}"
        if resp is None:
            continue
        respostas.append(resp)
        try:
            _discord("DELETE", f"/channels/{canal_id}/messages/{m['id']}", token)
        except RuntimeError:
            pass
    if respostas:
        _discord("POST", f"/channels/{canal_id}/messages", token, json={"content": "\n".join(respostas)[:1900]})
    return ultimo_id


def update_discord(canais, token, canal_id, msg_id):
    """Edita a mensagem da tabela; cria (e fixa) se nao houver. Devolve (canal_id, msg_id)."""
    embed = {
        "title": "📅 Calendário de postagens",
        "description": render_discord(canais),
        "color": 0x5865F2,
        "footer": {"text": "✅ postado   ⬜ previsto   •   escreva `ajuda` aqui pra ver os comandos"},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if canal_id and msg_id:
        try:
            _discord("PATCH", f"/channels/{canal_id}/messages/{msg_id}", token, json={"embeds": [embed]})
            return canal_id, msg_id
        except RuntimeError as e:
            if ": 404 " not in str(e):
                raise
            # mensagem ou canal apagados: acha o canal de novo e posta outra
    novo = find_channel(token)
    if not novo:
        raise RuntimeError(f"nenhum canal de texto chamado #{CANAL_DISCORD} nos servidores do bot")
    canal_id = novo
    msg = _discord("POST", f"/channels/{canal_id}/messages", token, json={"embeds": [embed]})
    try:
        _discord("PUT", f"/channels/{canal_id}/pins/{msg['id']}", token)
    except RuntimeError:
        pass
    return canal_id, msg["id"]


# ---------- sync ----------
def sync(spreadsheet, verbose=True):
    cfg_ws, tab_ws = ensure_tabs(spreadsheet)
    cfg_rows = cfg_ws.get_all_values()
    canais = [Canal(r) for r in cfg_rows[1:] if _pad(r, 1)[0].strip()]
    by_name = {c.nome.lower(): c for c in canais}

    # 1. le a tabela atual: linhas marcadas = historico; e detecta marcacao/desmarcacao manual
    tab_rows = [_pad(r, len(TABELA_HEADER)) for r in tab_ws.get_all_values()[1:]]
    manual_marks, manual_undo = {}, set()
    for r in tab_rows:
        c = by_name.get(r[T_CANAL].strip().lower())
        d = _parse_date(r[T_DATA])
        if not c or not d:
            continue
        marcado = _as_bool(r[T_POSTADO])
        if not c.proxima_data or d < c.proxima_data:
            # linha que o script escreveu como postada
            if marcado:
                c.postados.append((d, r[T_RESP].strip()))
            else:
                manual_undo.add((c.nome, d))
        elif marcado and d == c.proxima_data:
            manual_marks[c.nome] = d
    for c in canais:
        c.postados.sort()
        # desmarcou a ultima postada -> desfaz. Outras desmarcadas sao ignoradas (voltam TRUE).
        if c.postados and (c.nome, c.postados[-1][0]) in manual_undo:
            c.desfazer()
        if c.nome in manual_marks:
            c.marcar_postado(manual_marks[c.nome], "marcado na planilha")

    # 2. comandos escritos no canal do Discord
    token = os.environ.get("DISCORD_BOT_TOKEN")
    dc = canais[0] if canais else None
    if token and dc:
        try:
            canal_id = dc.row[C_DC_CANAL].strip() or find_channel(token)
            if canal_id:
                dc.row[C_DC_CANAL] = canal_id
                dc.row[C_ULTIMO_CMD] = processar_comandos(
                    canais, token, canal_id, dc.row[C_DC_MSG].strip(), dc.row[C_ULTIMO_CMD].strip())
        except Exception as e:
            print(f"[postagens] comandos falharam: {e}")

    # 3. YouTube
    for c in canais:
        if not c.youtube_id:
            continue
        try:
            entries = fetch_feed(c.youtube_id)
        except Exception as e:  # feed fora do ar nao pode derrubar o resto
            if verbose:
                print(f"[postagens] feed de {c.nome} falhou: {e}")
            continue
        if not entries:
            continue
        if not c.ultimo_publicado:
            c.ultimo_publicado = entries[-1]["published"]
            c.eventos.append(f"[{c.nome}] feed sincronizado ({c.ultimo_publicado})")
            continue
        for e in entries:
            if e["published"] <= c.ultimo_publicado:
                continue
            d = datetime.fromisoformat(e["published"].replace("Z", "+00:00")).astimezone(BRT).date()
            c.marcar_postado(d, f'YouTube: "{e["title"]}"')
            c.ultimo_publicado = e["published"]

    for c in canais:
        c.correr()

    # 4. grava config + tabela
    cfg_ws.update([c.to_row() for c in canais], f"A2:{_col(len(CONFIG_HEADER) - 1)}{len(canais) + 1}",
                  value_input_option="RAW")
    linhas = _linhas_ordenadas(canais)
    valores = [[_fmt(d), DIAS[d.weekday()], canal, pessoa, s == "ok"] for d, canal, pessoa, s in linhas]
    tab_ws.clear()
    tab_ws.update([TABELA_HEADER] + valores, "A1", value_input_option="RAW")

    # 4. Discord
    # 5. tabela no Discord. Ids do canal/mensagem ficam na 1a linha da config, so como cache
    if token and dc:
        antes = (dc.row[C_DC_CANAL].strip(), dc.row[C_DC_MSG].strip())
        try:
            depois = update_discord(canais, token, *antes)
            if depois != antes:
                cfg_ws.update([list(depois)], f"{_col(C_DC_CANAL)}2:{_col(C_DC_MSG)}2", value_input_option="RAW")
                if verbose:
                    print(f"[postagens] tabela postada no Discord (canal {depois[0]})")
        except Exception as e:  # planilha ja esta certa; o Discord tenta de novo na proxima rodada
            print(f"[postagens] Discord falhou: {e}")
    elif verbose:
        print("[postagens] Discord pulado: falta DISCORD_BOT_TOKEN")

    if verbose:
        for c in canais:
            for ev in c.eventos:
                print("[postagens]", ev)
        print(f"[postagens] {len(linhas)} linhas na tabela")


def main():
    import gspread
    from google.oauth2.service_account import Credentials
    import main as m
    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    sync(gspread.authorize(creds).open_by_key(m.SHEET_ID))


if __name__ == "__main__":
    main()
