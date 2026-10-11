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

    def test_titulos_com_video_vem_de_obra_e_variantes(self):
        todos = [["quero_postar", "obra", "canal", "", "", "", "", "nomes_variantes"],
                 ["FALSE", "God of Killers", "Tobs", "", "", "", "", "God of Killers | Sat-in-ui Sin"]]
        self.assertEqual(n.video_titles(todos), {"god of killers", "sat in ui sin"})


if __name__ == "__main__":
    unittest.main()
