from datetime import datetime, timezone
import unittest

import novas_obras as n

NOW = datetime(2026, 10, 11, 18, 0, tzinfo=timezone.utc)


def item(site, titulo, caps=5, generos="Action", ano="", adulto=False):
    return n._item(site, titulo, f"https://{site}.x/{titulo}", "", caps, generos, ano, adulto)


class NovasObrasTest(unittest.TestCase):
    def test_bloqueia_mature_shoujo_blgl_mas_deixa_ecchi(self):
        self.assertTrue(n.blocked(item("A", "x", generos="Action, Mature")))
        self.assertTrue(n.blocked(item("A", "x", generos="Drama, Shoujo")))
        self.assertTrue(n.blocked(item("A", "x", generos="Boys' Love")))
        self.assertTrue(n.blocked(item("A", "x", generos="Girls Love")))
        self.assertTrue(n.blocked(item("A", "x", adulto=True)))
        self.assertFalse(n.blocked(item("A", "x", generos="Action, Ecchi")))

    def test_romance_so_passa_com_acao(self):
        self.assertTrue(n.blocked(item("A", "x", generos="Romance, Drama")))
        self.assertFalse(n.blocked(item("A", "x", generos="Romance, Martial Arts")))

    def test_so_entra_obra_nova(self):
        rows = n.merge([], [item("A", "Nova", 5, ano="2026"), item("A", "Catalogo", 146),
                            item("A", "Velha", 4, ano="2019")], NOW, set())
        self.assertEqual([r["obra"] for r in rows], ["Nova"])

    def test_mesma_obra_em_dois_sites_vira_uma_linha_e_preserva_entrada(self):
        rows = n.merge([], [item("Comix", "The Crazy Villain", 20)], NOW, set())
        self.assertEqual(len(rows), 1)
        visto = rows[0]["visto_em"]
        later = datetime(2026, 10, 12, 18, 0, tzinfo=timezone.utc)
        # ja na aba: continua mesmo passando do limite de capitulos
        rows = n.merge(rows, [item("Asura", "The Crazy Villain!", 40)], later, {"the crazy villain"})
        self.assertEqual(len(rows), 1)
        r = rows[0]
        self.assertEqual(r["sites"], "Comix, Asura")
        self.assertEqual((r["capitulos"], r["visto_em"]), (40, visto))
        self.assertEqual(r["ja_tem_video"], "Sim")

    def test_visto_em_usa_data_do_site_e_ordena_por_ela(self):
        antiga = n._item("Hive", "Antiga", "l", caps=3, generos="Action",
                         data=datetime(2026, 10, 1, 15, 0, tzinfo=timezone.utc))
        recente = n._item("Kayn", "Recente", "l", caps=3, generos="Action",
                          data=datetime(2026, 10, 9, 15, 0, tzinfo=timezone.utc))
        existente = {"peguei": "TRUE", "obra": "Do Meio", "capitulos": "2", "generos": "", "ano": "",
                     "sites": "Comix", "visto_em": "05/10/2026 10:00", "ja_tem_video": "", "link": ""}
        rows = n.merge([existente], [antiga, recente, item("Comix", "Sem Data")], NOW, set())
        self.assertEqual([(r["obra"], r["visto_em"]) for r in rows], [
            ("Sem Data", "11/10/2026 15:00"), ("Recente", "09/10/2026 12:00"),
            ("Do Meio", "05/10/2026 10:00"), ("Antiga", "01/10/2026 12:00")])
        self.assertEqual([r["peguei"] for r in rows], ["FALSE", "FALSE", "TRUE", "FALSE"])

    def test_le_aba_antiga_sem_peguei_pelo_nome_da_coluna(self):
        class Ws:
            def get_all_values(self):
                return [["Obra", "Capítulos", "Gêneros", "Ano", "Sites", "Visto em", "Já tem vídeo", "Link"],
                        ["X", "3", "Action", "2026", "Comix", "29/10/2026 22:02", "", "https://x"]]
        d = n._read(Ws())[0]
        self.assertEqual((d["obra"], d["visto_em"], d["link"], d["peguei"]), ("X", "29/10/2026 22:02", "https://x", ""))
        self.assertEqual(n._row(d)[0], "FALSE")

    def test_data_da_obra_kayn_vem_do_id(self):
        self.assertEqual(n._cuid_date("cmtzutgp5006igis8txkekkx9").date().isoformat(), "2026-09-13")

    def test_datas_da_mist(self):
        self.assertEqual(n._mist_date("4 days ago", NOW), datetime(2026, 10, 7, 18, 0, tzinfo=timezone.utc))
        self.assertEqual(n._mist_date("Oct 22, 2026", NOW).date().isoformat(), "2026-10-22")
        self.assertIsNone(n._mist_date(None, NOW))

    def test_ordem_dos_capitulos_otl(self):
        self.assertEqual(sorted(["/read/x/10", "/read/x/2-5", "/read/x/2"], key=n._cap_order),
                         ["/read/x/2", "/read/x/2-5", "/read/x/10"])

    def test_titulos_com_video_vem_de_obra_e_variantes(self):
        todos = [["quero_postar", "obra", "canal", "", "", "", "", "nomes_variantes"],
                 ["FALSE", "God of Killers", "Tobs", "", "", "", "", "God of Killers | Sat-in-ui Sin"]]
        self.assertEqual(n.video_titles(todos), {"god of killers", "sat in ui sin"})


if __name__ == "__main__":
    unittest.main()
