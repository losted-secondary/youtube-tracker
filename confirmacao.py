"""Marca na aba `todos` as obras com nome 100% confirmado.

Confirmado = o proprio canal disse o nome (descricao ou comentario do dono do video), ou
uma identificacao revisada com `"confirmado": True`. A celula da obra (coluna B) fica em
verde e negrito, com uma nota dizendo de onde veio. Nome sem essa marca e palpite
(comentario de espectador, sinopse parecida, etc.).

A formatacao e a nota andam junto com a linha no sortRange, entao a marca sobrevive a
reordenacao por data.
"""
VERDE = {"red": 0.06, "green": 0.50, "blue": 0.18}


def mark(spreadsheet, sheet, marks):
    """marks: [(numero_da_linha, texto_da_nota)]."""
    if not marks:
        return
    spreadsheet.batch_update({"requests": [{
        "updateCells": {
            "range": {"sheetId": sheet.id, "startRowIndex": n - 1, "endRowIndex": n,
                      "startColumnIndex": 1, "endColumnIndex": 2},
            "rows": [{"values": [{
                "note": "✅ CONFIRMADO: " + nota,
                "userEnteredFormat": {"textFormat": {"bold": True, "foregroundColor": VERDE}},
            }]}],
            "fields": "note,userEnteredFormat.textFormat.bold,userEnteredFormat.textFormat.foregroundColor",
        }
    } for n, nota in marks]})
