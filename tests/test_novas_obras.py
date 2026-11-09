from datetime import datetime, timezone
import unittest

import novas_obras as n

NOW = datetime(2026, 10, 11, 18, 0, tzinfo=timezone.utc)


def item(site, titulo, caps=5, generos="Action", ano="", capa=""):
    return n._item(site, titulo, f"https://{site}.x/{titulo}", capa, caps, generos, ano)


class NovasObrasTest(unittest.TestCase):
    def test_bloqueia_so_blgl_e_deixa_shoujo_adulto_e_ecchi(self):
        self.assertFalse(n.blocked(item("A", "x", generos="Drama, Shoujo")))   # vai pra aba Femininas
        self.assertFalse(n.blocked(item("A", "x", generos="Romance, Drama")))
        self.assertTrue(n.blocked(item("A", "x", generos="Boys' Love")))
        self.assertTrue(n.blocked(item("A", "x", generos="Yaoi, Mature")))
        self.assertTrue(n.blocked(item("A", "x", generos="Girls Love")))
        self.assertFalse(n.blocked(item("A", "x", generos="Action, Mature")))
        self.assertFalse(n.blocked(item("A", "x", generos="Drama, Adult, Smut, 19+")))
        self.assertFalse(n.blocked(item("A", "x", generos="Action, Ecchi")))

    def test_feminina_pela_demografia_ou_romance_sem_acao(self):
        self.assertTrue(n.is_female("x", "Drama, Shoujo"))
        self.assertTrue(n.is_female("x", "Action, Josei"))            # demografia manda
        self.assertTrue(n.is_female("x", "Romance, Drama"))
        self.assertTrue(n.is_female("x", "Romance, Fantasy, Drama"))  # fantasy nao salva
        self.assertFalse(n.is_female("x", "Romance, Martial Arts"))
        self.assertFalse(n.is_female("x", "Romance, Mature, Seinen"))
        self.assertFalse(n.is_female("x", "Action, Fantasy, Romance"))
        self.assertFalse(n.is_female("x", "Drama"))
        self.assertFalse(n.is_female("x", ""))
        self.assertTrue(n.is_female("x", "Yaoi"))   # BL que so mostrou o genero depois de entrar

    def test_titulo_so_decide_quando_o_genero_nao_diz_nada(self):
        for t in ("The Reason the Villainess Saved the Male Lead's Brother", "I'll Quit as The Empress",
                  "The Strongest Duke's One and Only Granddaughter", "My Husband's Funeral",
                  "The Good Daughter-in-Law No Longer Exists", "N Years of Unrequited Love",
                  "I Seduced the Male Lead's Mother (GL)", "This Young Lady Hates Being Productive!"):
            self.assertTrue(n.is_female(t, ""), t)
        self.assertTrue(n.is_female("I'll Quit as The Empress", "Fantasy, Drama"))
        for t in ("The Northern Grand Duke's Crazy Son-in-Law", "My Dragon Girlfriend Has Returned",
                  "My Daughter Is the Final Boss", "Global Beast Taming", "Solo Swordmaster",
                  "The Academy's Weapon Replicator", "Bandit King"):
            self.assertFalse(n.is_female(t, ""), t)
        # genero de acao ou demografia masculina ganha do titulo
        self.assertFalse(n.is_female("The Princess in the Dragon's Belly", "Seinen"))
        self.assertFalse(n.is_female("The Regressor and the Blind Princess", "Action, Fantasy, Romance"))

    def test_aba_de_cada_linha(self):
        def linha(obra, generos="", adulto=False):
            return {"obra": obra, "generos": generos, "adulto": adulto}
        self.assertEqual(n.tab_of(linha("Solo Swordmaster", "Action")), "")
        self.assertEqual(n.tab_of(linha("Solo Swordmaster", "Action, Mature", True)), "adulto")
        self.assertEqual(n.tab_of(linha("X", "Josei, Smut", True)), "feminina")   # +18 e so masculino
        self.assertEqual(n.tab_of(linha("The Remarried Empress")), "feminina")

    def test_genero_do_comix_e_buscado_so_em_linha_do_comix_sem_genero(self):
        pedidos = []

        def fake(url):
            pedidos.append(url)
            if "morto" in url:
                raise RuntimeError("404")
            return "Romance, Josei"
        rows = [{"generos": "", "link": "https://comix.to/title/a"},
                {"generos": "Action", "link": "https://comix.to/title/b"},
                {"generos": "", "link": "https://qimanga.com/series/c"},
                {"generos": "", "link": "https://comix.to/title/morto"}]
        original, n._comix_page_generos = n._comix_page_generos, fake
        try:
            n.fill_genres(rows)
        finally:
            n._comix_page_generos = original
        self.assertEqual([r["generos"] for r in rows], ["Romance, Josei", "Action", "", ""])
        self.assertEqual(sorted(pedidos), ["https://comix.to/title/a", "https://comix.to/title/morto"])

    def test_sync_renomeia_a_aba_antiga_e_separa_em_tres(self):
        try:
            import gspread
        except ImportError:
            self.skipTest("gspread nao instalado")

        class Ws:
            def __init__(self, ss, title, vals=None, formulas=None):
                self.ss, self.title, self.vals = ss, title, [list(r) for r in vals or []]
                self.formulas = formulas or {}
                self.id = abs(hash(title)) % 10 ** 6
                self.row_count = 501

            @property
            def index(self):
                return self.ss.sheets.index(self)

            def row_values(self, i):
                return self.vals[i - 1] if len(self.vals) >= i else []

            def get_all_values(self):
                return [list(r) for r in self.vals]

            def col_values(self, col, value_render_option=None):
                return [self.formulas.get(i, r[col - 1] if len(r) >= col else "") for i, r in enumerate(self.vals)]

            def update_title(self, title):
                self.title = title

            def batch_clear(self, ranges):
                self.vals = self.vals[:1]

            def add_rows(self, k):
                self.row_count += k

            def update(self, values, cell, value_input_option=None):
                if cell == "A1":
                    self.vals = [list(r) for r in values]
                else:   # como o USER_ENTERED do Sheets: o apostrofo some, fica o texto
                    self.vals = self.vals[:1] + [[c[1:] if isinstance(c, str) and c.startswith("'") else c
                                                  for c in r] for r in values]

        class Ss:
            def __init__(self):
                self.sheets, self.deleted = [], []

            def worksheets(self):
                return list(self.sheets)

            def worksheet(self, title):
                for ws in self.sheets:
                    if ws.title == title:
                        return ws
                raise gspread.WorksheetNotFound(title)

            def add_worksheet(self, title, rows, cols, index=None):
                ws = Ws(self, title)
                self.sheets.insert(len(self.sheets) if index is None else index, ws)
                return ws

            def del_worksheet(self, ws):
                self.deleted.append(ws.title)
                self.sheets.remove(ws)

            def batch_update(self, body):
                pass

        def linha(peguei, obra, generos, link):
            return [peguei, "", obra, "3", generos, "2026", "Comix", "01/11/2026 10:00", "", link]

        ss = Ss()
        ss.sheets = [
            Ws(ss, "todos"),
            Ws(ss, "Novas Obras", [n.HEADER,
                                   linha("TRUE", "Solo Swordmaster", "Action", "https://x/1"),
                                   linha("TRUE", "The Remarried Empress", "", "https://x/2"),
                                   linha("FALSE", "Sem Genero", "", "https://comix.to/title/3"),
                                   linha("FALSE", "Frost", "", "https://comix.to/title/4")],
               formulas={1: '=IMAGE("https://c.x/capa.jpg")'}),
            Ws(ss, "Novas Obras +18", [n.HEADER, linha("FALSE", "Adulta", "Action, Mature", "https://x/5")]),
            Ws(ss, "Sites", [n.SITES_HEADER]),
        ]
        antiga = ss.sheets[1]
        nova = n._item("Asura", "Nova Shoujo", "https://x/6", caps=2, generos="Drama, Shoujo")
        originais = n.collect, n.fill_covers, n._comix_page_generos
        n.collect = lambda now: ([nova], {nome: (0, "OK") for nome, _, _, _ in n.SITES})
        n.fill_covers = lambda rows: None
        n._comix_page_generos = lambda url: "Romance, Josei" if url.endswith("/3") else "Action, Shounen"
        try:
            n.sync(ss, [["quero_postar", "obra"]], NOW)
        finally:
            n.collect, n.fill_covers, n._comix_page_generos = originais

        self.assertEqual([ws.title for ws in ss.sheets],
                         ["todos", "Novas Obras Shonen", "Novas Obras Femininas", "Novas Obras +18", "Sites"])
        self.assertIs(ss.sheets[1], antiga)    # renomeada, nao recriada
        self.assertEqual(ss.deleted, [])

        def obras(title):
            return [(r[0], r[2]) for r in ss.worksheet(title).vals[1:]]
        self.assertEqual(obras("Novas Obras Shonen"), [("TRUE", "Solo Swordmaster"), ("FALSE", "Frost")])
        self.assertEqual(sorted(obras("Novas Obras Femininas")),
                         [("FALSE", "Nova Shoujo"), ("FALSE", "Sem Genero"), ("TRUE", "The Remarried Empress")])
        self.assertEqual(obras("Novas Obras +18"), [("FALSE", "Adulta")])
        self.assertEqual(ss.worksheet("Novas Obras Shonen").vals[1][1], '=IMAGE("https://c.x/capa.jpg")')
        # segunda rodada: nada muda de lugar e nada e recriado
        n.collect = lambda now: ([], {nome: (0, "OK") for nome, _, _, _ in n.SITES})
        n.fill_covers = lambda rows: None
        try:
            n.sync(ss, [["quero_postar", "obra"]], NOW)
        finally:
            n.collect, n.fill_covers = originais[:2]
        self.assertEqual(len(ss.sheets), 5)
        self.assertEqual(obras("Novas Obras Shonen"), [("TRUE", "Solo Swordmaster"), ("FALSE", "Frost")])
        self.assertEqual(len(obras("Novas Obras Femininas")), 3)

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
        existente = {"peguei": "TRUE", "capa": "", "obra": "Do Meio", "capitulos": "2", "generos": "", "ano": "",
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
        self.assertEqual((d["obra"], d["visto_em"], d["link"], d["peguei"], d["capa"]),
                         ("X", "29/10/2026 22:02", "https://x", "", ""))
        self.assertEqual(n._row(d)[:2], ["FALSE", ""])

    def test_capa_volta_da_formula_e_vira_image(self):
        class Ws:
            def get_all_values(self):
                return [["Peguei", "Capa", "Obra"], ["TRUE", "", "X"]]

            def col_values(self, col, value_render_option=None):
                assert (col, value_render_option) == (2, "FORMULA")
                return ["Capa", '=IMAGE("https://c.x/a.jpg")']
        d = n._read(Ws())[0]
        self.assertEqual((d["peguei"], d["capa"]), ("TRUE", "https://c.x/a.jpg"))
        self.assertEqual(n._row({**d, **{k: "" for k in n.KEYS if k not in d}})[1], '=IMAGE("https://c.x/a.jpg")')

    def test_capa_relativa_do_comix_vira_url_completa(self):
        rel = "/images/covers/1c/8d/abc@280.jpg"
        self.assertEqual(n._comix_capa({"medium": rel}), "https://comix.to" + rel)
        absoluta = "https://static.comix.to/2c4f/i/f/4f/x@280.jpg"
        self.assertEqual(n._comix_capa({"medium": absoluta}), absoluta)
        self.assertEqual(n._comix_capa(None), "")
        # linha que ja estava gravada com o caminho relativo
        d = {k: "" for k in n.KEYS}
        d["capa"] = rel
        self.assertEqual(n._row(d)[1], f'=IMAGE("https://comix.to{rel}")')

    def test_linha_sem_capa_busca_na_pagina_e_link_morto_nao_quebra(self):
        def fake(url):
            if "morto" in url:
                raise RuntimeError("404")
            return "https://c.x/" + url
        rows = [{"capa": "", "link": "a"}, {"capa": "ja", "link": "b"}, {"capa": "", "link": "morto"}]
        original, n._page_cover = n._page_cover, fake
        try:
            n.fill_covers(rows)
        finally:
            n._page_cover = original
        self.assertEqual([r["capa"] for r in rows], ["https://c.x/a", "ja", ""])

    def test_capa_preenche_linha_existente_sem_capa(self):
        rows = n.merge([], [item("Comix", "Obra X")], NOW, set())
        rows = n.merge(rows, [item("Asura", "Obra X", capa="https://c.x/a.jpg")], NOW, set())
        self.assertEqual(rows[0]["capa"], "https://c.x/a.jpg")

    def test_data_da_obra_kayn_vem_do_id(self):
        self.assertEqual(n._cuid_date("cmtzutgp5006igis8txkekkx9").date().isoformat(), "2026-09-13")

    def test_datas_da_mist(self):
        self.assertEqual(n._mist_date("4 days ago", NOW), datetime(2026, 10, 7, 18, 0, tzinfo=timezone.utc))
        self.assertEqual(n._mist_date("Oct 22, 2026", NOW).date().isoformat(), "2026-10-22")
        self.assertIsNone(n._mist_date(None, NOW))

    def test_ordem_dos_capitulos_otl(self):
        self.assertEqual(sorted(["/read/x/10", "/read/x/2-5", "/read/x/2"], key=n._cap_order),
                         ["/read/x/2", "/read/x/2-5", "/read/x/10"])

    def test_obra_adulta_pelo_site_ou_pelo_genero_e_continua_adulta(self):
        self.assertTrue(n.is_adult(item("A", "x", generos="Action, Smut")))
        self.assertTrue(n.is_adult(item("A", "x", generos="Fantasy, 19+")))
        self.assertTrue(n.is_adult(n._item("Comick", "x", "l", adulto=True)))
        self.assertFalse(n.is_adult(item("A", "x", generos="Action, Ecchi")))
        rows = n.merge([], [n._item("Comick", "Obra X", "l", caps=3, adulto=True)], NOW, set())
        self.assertTrue(rows[0]["adulto"])
        # proxima rodada: vem de outro site sem a marca, mas a linha ja estava na aba +18
        rows = n.merge([{**rows[0], "adulto": True}], [item("Comix", "Obra X")], NOW, set())
        self.assertTrue(rows[0]["adulto"])
        # linha antiga da aba normal que nao reaparece: classificada pelo genero
        velha = {"peguei": "FALSE", "capa": "", "obra": "Velha", "capitulos": "", "generos": "Mature",
                 "ano": "", "sites": "Comix", "visto_em": "01/10/2026 10:00", "ja_tem_video": "", "link": ""}
        self.assertTrue(n.merge([{**velha, "adulto": False}], [], NOW, set())[0]["adulto"])

    def test_titulos_com_video_vem_de_obra_e_variantes(self):
        todos = [["quero_postar", "obra", "canal", "", "", "", "", "nomes_variantes"],
                 ["FALSE", "God of Killers", "Tobs", "", "", "", "", "God of Killers | Sat-in-ui Sin"]]
        self.assertEqual(n.video_titles(todos), {"god of killers", "sat in ui sin"})


if __name__ == "__main__":
    unittest.main()
