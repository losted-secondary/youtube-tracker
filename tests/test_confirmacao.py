import unittest

import confirmacao
from reviewed_identifications import plan_confirmed

HEADER = ["quero_postar", "obra", "canal", "data_postado", "viewers", "duracao", "link", "nomes_variantes"]


class FakeSpreadsheet:
    def __init__(self):
        self.requests = []

    def batch_update(self, body):
        self.requests.extend(body["requests"])


class FakeSheet:
    id = 7


class ConfirmacaoTests(unittest.TestCase):
    def test_marca_celula_da_obra_em_verde_com_nota(self):
        ss = FakeSpreadsheet()
        confirmacao.mark(ss, FakeSheet(), [(5, "nome na descrição do vídeo")])
        (req,) = ss.requests
        cell = req["updateCells"]
        self.assertEqual(cell["range"], {"sheetId": 7, "startRowIndex": 4, "endRowIndex": 5,
                                         "startColumnIndex": 1, "endColumnIndex": 2})
        value = cell["rows"][0]["values"][0]
        self.assertEqual(value["note"], "✅ CONFIRMADO: nome na descrição do vídeo")
        self.assertTrue(value["userEnteredFormat"]["textFormat"]["bold"])

    def test_sem_marcas_nao_chama_api(self):
        ss = FakeSpreadsheet()
        confirmacao.mark(ss, FakeSheet(), [])
        self.assertEqual(ss.requests, [])

    def test_plan_confirmed_so_marca_confirmado_com_o_mesmo_nome(self):
        rows = [HEADER,
                ["", "Shadow Slave", "Gaku", "", "", "", "https://youtu.be/DUpaLD29WXw", ""],
                ["", "", "Gaku", "", "", "", "https://youtu.be/hNIp0R12Ujk", ""],          # vai ser preenchida
                ["", "Outro Nome", "X", "", "", "", "https://youtu.be/9V8sUBpwtPA", ""],   # trocado na mao
                ["", "My Wife Is Actually the Empress?", "Ash", "", "", "", "https://youtu.be/Ahr1vUkIdDw", ""]]  # palpite
        self.assertEqual([n for n, _ in plan_confirmed(rows)], [2, 3])


if __name__ == "__main__":
    unittest.main()
