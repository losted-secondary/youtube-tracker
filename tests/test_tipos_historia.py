"""Tipos de história: multiplicador da nota e aba `Ranking de tipos` (dono, 28/11/2026)."""
import unittest
from unittest import mock

import cacador as C
import tipos_historia as TH


class TiposHistoriaTest(unittest.TestCase):
    def test_tipos_pela_sinopse_e_tags_sem_falso_positivo(self):
        c = {"titulo": "Reborn as the Duke's Youngest Son", "nomes": [], "tags": ["Magic"], "generos": [],
             "sinopse": "She smiled at him. He was reincarnated into a noble family and studies magic."}
        tipos = TH.tipos_de(c)
        self.assertIn("Reencarnação / renascimento", tipos)
        self.assertIn("Nobreza / família nobre", tipos)
        self.assertIn("Mago / magia", tipos)
        self.assertNotIn("Protagonista mulher", tipos)          # "she/her" na sinopse não conta

    def test_multiplicador_e_media_dos_tipos(self):
        bom = {"titulo": "The Noble Necromancer", "nomes": [], "tags": [], "generos": [], "sinopse": ""}
        fraco = {"titulo": "Waiting", "nomes": [], "tags": ["Female Protagonist"], "generos": [], "sinopse": ""}
        nada = {"titulo": "Waiting", "nomes": [], "tags": [], "generos": [], "sinopse": ""}
        m_bom, tipos = TH.multiplicador(bom)
        self.assertGreater(m_bom, 1.1)
        self.assertEqual(set(tipos), {"Nobreza / família nobre", "Necromante / mortos-vivos"})
        self.assertLess(TH.multiplicador(fraco)[0], 1.0)
        self.assertEqual(TH.multiplicador(nada), (1.0, []))
        self.assertTrue(TH.texto(bom).startswith(f"{m_bom:.2f}×"))

    def test_nota_final_multiplica_antes_da_penalidade(self):
        c = {"titulo": "The Noble Necromancer", "nomes": [], "tags": [], "generos": [], "sinopse": "",
             "nota": 8, "popularidade": 0, "yt": {"status": "TOMADA"}}
        with mock.patch.object(C, "arquetipo", return_value=(0.0, "")):
            final = C.pontuar(c)
        self.assertAlmostEqual(final, round(8 * c["mult_tipo"] - 4, 2))

    def test_aba_ranking_de_tipos(self):
        escrito = {}

        class Aba:
            id = 77

            def batch_clear(self, r):
                escrito["clear"] = r

            def update(self, linhas, inicio, value_input_option=None):
                escrito["linhas"] = linhas

            def update_note(self, celula, texto):
                escrito["nota"] = texto

        with mock.patch("novas_obras._ensure_tab", return_value=Aba()) as ensure:
            self.assertEqual(C.gravar_ranking_tipos(object(), 3), 77)
        self.assertEqual(ensure.call_args.args[1], C.TAB_TIPOS)
        self.assertEqual(ensure.call_args.args[2], C.HEADER_TIPOS)
        primeira = escrito["linhas"][0]
        self.assertEqual(primeira[0], 1)
        self.assertEqual(len(primeira), len(C.HEADER_TIPOS))
        self.assertEqual(len(escrito["linhas"]), len(TH.tabela()["ranking"]))
        self.assertIn("vídeos", escrito["nota"])

    def test_coluna_tipo_antes_do_id(self):
        self.assertEqual(C.HEADER_OUT[-2:], ["Tipo de história", "ID"])


if __name__ == "__main__":
    unittest.main()
