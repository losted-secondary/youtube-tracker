"""Preenche a coluna `nomes` (H) com os nomes alternativos da obra, vindos do comick.

Regra: so busca linha com `obra` preenchida e `nomes` VAZIA. Nunca sobrescreve o que
ja esta la (nem o que o usuario digitou na mao). Pra forcar nova busca, apagar a celula.

Roda dentro do main.py a cada sync (com teto de buscas por rodada) ou sozinho:
    python comick.py          -> backfill completo, sem teto
"""
import os
import json
import re
import time
import unicodedata
from difflib import SequenceMatcher

import requests

API_URL = "https://api.comick.dev/v1.0/search"
# so nomes em alfabeto latino: ingles + romanizacoes do japones/coreano.
LANGS = ("en", "ja-ro", "ko-ro")
NOT_FOUND = "não encontrado"
SEP = " | "
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
THROTTLE = 0.25          # segundos entre chamadas (comick nao publica limite; ser educado)
MATCH_MIN = 0.88         # similaridade minima pra aceitar um resultado nao-exato
                         # (0.86 deixava passar 'hello killer' -> 'Hero Killer')

# valores da coluna obra que NAO sao nome de obra
IGNORE = {
    "unnamed", "unamed", "sem nome", "no name", "shorts", "short", "ia", "ai",
    "privado", "private", "removed", "deleted", "unknown", "desconhecido",
    "none", "null", "na", "n a", "teste", "test", "tbd", "x", "varios", "various",
    "manhwa", "manhua", "manga", "recap", "strike", "live", "anime",
}


def normalize(s):
    """minusculo, sem acento, sem pontuacao — pra comparar/deduplicar nomes."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def clean_query(obra):
    """tira lixo grudado no nome antes de buscar: 'X Chapter 262', 'X ep 12', 'X (2023)'."""
    q = unicodedata.normalize("NFKC", obra).strip()
    q = re.sub(r"\s*[\(\[][^)\]]*[\)\]]\s*$", " ", q)
    q = re.sub(r"[\s\-–—_,|]*\b(chapter|chap|cap|ch|episode|epi?|part|season|s)\.?\s*\d+.*$", "", q, flags=re.I)
    q = re.sub(r"[\s\-–—_,|]*\bchapters?\b.*$", "", q, flags=re.I)
    return q.strip(" \t-–—_|,.:")


def is_ignorable(obra):
    n = normalize(obra)
    if len(n) < 3:
        return True
    if n in IGNORE:
        return True
    # so numero/pontuacao, ou coisas tipo "-------- STRIKE ----------"
    if not re.search(r"[a-z]{3}", n):
        return True
    return False


def _titles_of(item):
    """todos os nomes conhecidos do resultado (qualquer idioma) — pra decidir o match."""
    names = [item.get("title") or ""]
    for t in item.get("md_titles") or []:
        if t.get("title"):
            names.append(t["title"])
    return [n for n in names if n]


def english_titles(item):
    """os nomes que vao pra planilha: title principal + md_titles em en/ja-ro/ko-ro."""
    out, seen = [], set()
    for name in [item.get("title") or ""] + [
        t["title"] for t in (item.get("md_titles") or [])
        if t.get("title") and (t.get("lang") or "").lower() in LANGS
    ]:
        key = normalize(name)
        if name and key and key not in seen:
            seen.add(key)
            out.append(name.strip())
    return out


def search(query, session, tries=3):
    """devolve a lista de resultados do comick, ou None se a API falhou (rede/429/5xx)."""
    for attempt in range(tries):
        try:
            r = session.get(
                API_URL, params={"q": query, "limit": 8, "page": 1}, timeout=20,
                headers={"User-Agent": UA, "Accept": "application/json", "Referer": "https://comick.dev/"},
            )
        except requests.RequestException:
            time.sleep(1.5 * (attempt + 1))
            continue
        if r.status_code == 200:
            try:
                data = r.json()
            except ValueError:
                return None
            return data if isinstance(data, list) else None
        if r.status_code == 404:
            return []
        # 429 / 5xx / cloudflare: espera e tenta de novo
        time.sleep(2.0 * (attempt + 1))
    return None


def best_match(obra, results):
    """casa o nome digitado com um resultado. Exato (normalizado) ganha; senao o mais
    parecido, desde que passe de MATCH_MIN — evita gravar nomes de outra obra."""
    target = normalize(clean_query(obra))
    if not target:
        return None
    best, best_score = None, 0.0
    for item in results:
        for name in _titles_of(item):
            cand = normalize(name)
            if not cand:
                continue
            if cand == target:
                return item
            score = SequenceMatcher(None, target, cand).ratio()
            # nome digitado truncado ("Regressor's Tale of Cultivatio") ainda casa
            if cand.startswith(target) or target.startswith(cand):
                score = max(score, 0.90 if min(len(cand), len(target)) >= 10 else score)
            if score > best_score:
                best, best_score = item, score
    return best if best_score >= MATCH_MIN else None


def lookup(obra, session):
    """-> string pra celula, ou None se a API falhou (nao gravar nada, tentar no proximo run)."""
    query = clean_query(obra)
    if not query or is_ignorable(query):
        return ""
    results = search(query, session)
    if results is None:
        return None
    item = best_match(obra, results)
    if not item:
        return NOT_FOUND
    names = english_titles(item)
    if not names:
        return NOT_FOUND
    cell = SEP.join(names)
    return cell[:49000]  # limite de 50k caracteres por celula do Sheets


def fill_names(sheet, rows, max_lookups=None, verbose=True):
    """rows = sheet.get_all_values() ja lido (com cabecalho). Devolve (preenchidas, nao_achadas).

    Uma busca por obra DISTINTA (normalizada) por rodada: o mesmo manhwa aparece em
    varios canais, entao cache em memoria corta a maior parte das chamadas.
    """
    pending = {}   # obra normalizada -> texto original de exemplo
    for row in rows[1:]:
        obra = row[1].strip() if len(row) > 1 else ""
        atual = row[7].strip() if len(row) > 7 else ""
        if not obra or atual or is_ignorable(obra):
            continue
        key = normalize(clean_query(obra))
        if key:
            pending.setdefault(key, obra)

    if not pending:
        return 0, 0

    session = requests.Session()
    resolved, found, missing, done = {}, 0, 0, 0
    total = min(len(pending), max_lookups or len(pending))
    for key, obra in pending.items():
        if max_lookups and done >= max_lookups:
            if verbose:
                print(f"comick: teto de {max_lookups} buscas, {len(pending) - done} obras ficam pro proximo run")
            break
        cell = lookup(obra, session)
        done += 1
        time.sleep(THROTTLE)
        if cell is None:      # API fora do ar: nao grava nada, tenta no proximo run
            if verbose:
                print(f"comick: falha de rede em '{obra}'")
            continue
        if not cell:
            continue
        missing, found = (missing + 1, found) if cell == NOT_FOUND else (missing, found + 1)
        resolved[key] = cell
        if verbose:
            print(f"comick [{done}/{total}] {obra} -> {cell[:90]}")
        if len(resolved) >= 300:
            write_names(sheet, resolved)   # grava parcial: backfill longo nao pode
            resolved = {}                  # perder tudo se cair no fim

    write_names(sheet, resolved)
    return found, missing


def write_names(sheet, resolved):
    """Grava a coluna H relendo a planilha AGORA.

    Critico: as buscas levam minutos e o sync reordena as linhas por data (sort_by_filter_order),
    entao o numero de linha lido ANTES das buscas pode ja estar velho — foi assim que o
    primeiro backfill gravou os nomes uma linha fora do lugar. Reler na hora e mandar a
    coluna inteira numa unica escrita deixa a janela de risco em ~1 segundo.
    """
    if not resolved:
        return 0
    fresh = sheet.get_all_values()
    col, wrote = [], 0
    for row in fresh[1:]:
        obra = row[1].strip() if len(row) > 1 else ""
        atual = row[7] if len(row) > 7 else ""
        if obra and not atual.strip() and not is_ignorable(obra):
            cell = resolved.get(normalize(clean_query(obra)))
            if cell:
                col.append([cell])
                wrote += 1
                continue
        col.append([atual])   # nunca sobrescreve o que ja esta la
    if wrote:
        sheet.update(col, f"H2:H{len(fresh)}", raw=True)
    return wrote


def main():
    import gspread
    from google.oauth2.service_account import Credentials
    from main import SHEET_ID, SHEET_TAB, HEADER

    creds = Credentials.from_service_account_info(
        json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    spreadsheet = gspread.authorize(creds).open_by_key(SHEET_ID)
    sheet = spreadsheet.worksheet(SHEET_TAB)
    rows = sheet.get_all_values()
    if rows and rows[0][:len(HEADER)] != HEADER:
        sheet.update([HEADER], "A1:H1")
    found, missing = fill_names(sheet, rows, max_lookups=None)
    print(f"comick: {found} obras preenchidas, {missing} nao encontradas")


if __name__ == "__main__":
    main()
