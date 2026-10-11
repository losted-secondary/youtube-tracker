"""Identificações revisadas: chave por vídeo, nunca pelo número de linha."""
import re

import confirmacao

REVIEWED = [
  {
    "video_id": "hNIp0R12Ujk",
    "title": "Psychopath in Murim",
    "aliases": [
      "Murim Psychopath"
    ],
    "evidence": "Frame aos 40s corresponde ao painel do capítulo 1. https://www.mangaread.org/manga/psychopath-in-murim/chapter-1/",
    "reviewed_at": "2026-10-11",
    "confirmado": True
  },
  {
    "video_id": "fE7n-MslLWM",
    "title": "God of Killers",
    "aliases": [],
    "evidence": "Narração cita Gungnir; sinopse editorial corresponde. https://m.webtoons.com/en/action/god-of-killers/list?title_no=10736",
    "reviewed_at": "2026-10-11"
  },
  {
    "video_id": "9V8sUBpwtPA",
    "title": "Spend More, Earn More",
    "aliases": [
      "Money Keeps Piling Up No Matter How Much I Spend",
      "Even If I Keep Spending, Money Keeps Piling Up"
    ],
    "evidence": "Frame aos 30s corresponde ao capítulo 1. https://vortexscans.org/series/spend-more-earn-more/chapter-1",
    "reviewed_at": "2026-10-11",
    "confirmado": True
  },
  {
    "video_id": "xDfmMGD1mk4",
    "title": "Earthen Keyboard Immortal",
    "aliases": [
      "Keyboard Immortal",
      "Lu Di Jian Xian"
    ],
    "evidence": "Legendas citam Zu An e Chu Chuyan; premissa corresponde. https://anilist.co/manga/141681/Lu-Di-Jian-Xian",
    "reviewed_at": "2026-10-11"
  },
  {
    "video_id": "ycKWC4EEz6c",
    "title": "Popularity Above All: I Play the Role of a Super Genius",
    "aliases": [
      "Popularity is Everything; I Play a Super Genius",
      "人气至上，我扮演超级天才"
    ],
    "evidence": "Novel ilustrada com IA conforme evidências. Comentário da parte 1 e sinopse. https://www.youtube.com/watch?v=6mJUJjuzGcs&lc=Ugwytsu1Vhz0Bh5xEZd4AaABAg https://www.novelupdates.com/series/popularity-above-all-i-play-the-role-of-a-super-genius/",
    "reviewed_at": "2026-10-11"
  },
  {
    "video_id": "T2Wx3nsn6Ks",
    "title": "The Genius Blacksmith's Game",
    "aliases": [
      "Genius Blacksmith's Game"
    ],
    "evidence": "Comentário e sinopse editorial. https://www.youtube.com/watch?v=T2Wx3nsn6Ks&lc=Ugxqc5GMuCtkIfecnR54AaABAg https://tapas.io/series/the-genius-blacksmiths-game/info",
    "reviewed_at": "2026-10-11"
  },
  {
    "video_id": "WSQlv2nyhDE",
    "title": "The Regressor and the Blind Saint",
    "aliases": [
      "The Regressor and the Blind Saintess"
    ],
    "evidence": "Comentário e premissa específica. https://www.youtube.com/watch?v=WSQlv2nyhDE&lc=UgzVVGnsq_AEjamp2Ax4AaABAg https://genztoons.net/the-regressor-and-the-blind-saint",
    "reviewed_at": "2026-10-11"
  },
  {
    "video_id": "Po0rPmnrZVc",
    "title": "The Return of the Mythical Archmage",
    "aliases": [
      "The Return of the Legendary Archmage"
    ],
    "evidence": "Comentário e sinopse tecnológica correspondente. https://www.youtube.com/watch?v=Po0rPmnrZVc&lc=UgxByNuYuhKGUf8x89N4AaABAg https://en-thunderscans.com/comics/the-return-of-the-mythical-archmage/",
    "reviewed_at": "2026-10-11"
  },
  {
    "video_id": "O2qxTxkCd7g",
    "title": "Revenge of the Wrongly Accused",
    "aliases": [
      "Enzai Fukushou",
      "Revenge for a False Conviction"
    ],
    "evidence": "Comentário e protagonista Manabu Toujou. https://www.youtube.com/watch?v=O2qxTxkCd7g&lc=UgzxsOqsDv743KaUnx94AaABAg https://newm.fanfox.net/manga/revenge_of_the_wrongly_accused/",
    "reviewed_at": "2026-10-11"
  }
]


REVIEWED.append({
    "video_id": "j_lwugWFCps",
    "title": "The Ruler of Darkness",
    "aliases": ["Ruler of the Dark Age", "Amheukgiui Jibaeja"],
    "evidence": "Teste de investigate.js: narração inicial sobre herdeiro do clã Luoyang e frame aos 40s correspondem ao capítulo 1. https://www.mangaread.org/manga/the-ruler-of-darkness/chapter-1/ https://freewebnovel.com/novel/the-ruler-of-darkness/chapter-1",
    "reviewed_at": "2026-10-11",
    "confirmado": True,
})


REVIEWED.extend([
    {
        "video_id": "JPU-wHenQ7s",
        "title": "Shut Up, Evil Dragon! I Don't Want to Raise a Child With You Anymore",
        "aliases": ["Shut Up, Evil Dragon!", "闭嘴恶龙我不想再跟你生孩子了"],
        "evidence": "Piloto da linha 17, pesquisado nesta sessão (não pelo dot). Nome explícito na descrição do vídeo e enredo de caçador de dragões com filhas da rainha inimiga correspondem à sinopse. https://www.youtube.com/watch?v=JPU-wHenQ7s https://olympusscanlation.org/shut-up-evil-dragon-manga/",
        "reviewed_at": "2026-10-11",
        "confirmado": True,
    },
    {
        "video_id": "RBib2cJkYlU",
        "title": "Genius Martial Arts Trainer",
        "aliases": ["Genius Murim Trainer"],
        "evidence": "Piloto da linha 19, pesquisado nesta sessão (não pelo dot). Falas de 0-180s: treinador Choi Kang-hyuk, academia prejudicada pela pandemia, leitura de novel Shaolin e despertar como Mujin; sequência corresponde ao capítulo 1. https://www.youtube.com/watch?v=RBib2cJkYlU https://faqwiki.us/novel/genius-martial-arts-trainer-chapter-1/",
        "reviewed_at": "2026-10-11",
    },
    {
        "video_id": "6xZguXtB-Dc",
        "title": "Popularizing Science: Oxygen is Toxic, and the Whole Internet is Saying I'm Crazy",
        "aliases": ["科普氧气有毒，全网骂我有病"],
        "evidence": "Piloto da linha 20, pesquisado nesta sessão (não pelo dot). Identificação por sequência de enredo: apresentador de ciência diz que oxigênio encurta a vida e demonstra oxidação com maçã cortada e metais, como no capítulo 2; descrição relaciona mitos a civilizações antigas, também presentes na sinopse. O recap adapta o nome do protagonista para Theo; original Ye Zhen. https://www.youtube.com/watch?v=6xZguXtB-Dc https://m.jingwx.com/140189/3217785.html https://wtr-lab.com/en/novel/73213/popularizing-science-oxygen-is-toxic-and-the-whole-internet-is-saying-im-crazy",
        "reviewed_at": "2026-10-11",
    },
    {
        "video_id": "L2Pt016Ev5U",
        "title": "Legendary Youngest Son of the Marquis House",
        "aliases": ["Jack Be Invincible", "The Marquess's Youngest Son"],
        "evidence": "Piloto da linha 21, pesquisado nesta sessão (não pelo dot). Comentários indicam o título; narração 0-180s identifica Jack Valantier, retorno aos 14 anos, irmão abusivo e irmã protetora. Correspondência com sinopse da editora Tapas e capítulo 1. https://www.youtube.com/watch?v=L2Pt016Ev5U https://tapas.io/series/jack-be-invincible/info https://wuxia.click/chapter/legendary-youngest-son-of-the-marquis-house-2",
        "reviewed_at": "2026-10-11",
    },
])


# videos de fora dos canais principais (descobrir.py), sem nome na descricao.
REVIEWED.extend([
    {
        "video_id": "DUpaLD29WXw",
        "title": "Shadow Slave",
        "aliases": [],
        "evidence": "Comentário do próprio canal (Gaku Recaps): 'Name; Shadow Slave'. https://www.youtube.com/watch?v=DUpaLD29WXw",
        "reviewed_at": "2026-10-11",
        "confirmado": True,
    },
    {
        "video_id": "Ahr1vUkIdDw",
        "title": "My Wife Is Actually the Empress?",
        "aliases": ["我家娘子竟然是女帝"],
        "evidence": "Comentário de espectador com o título e ~190-200 capítulos (vídeo cobre até o 25); contagem bate com a ficha (202 caps, finalizado). Não é o mesmo que 'My Wife is Actually the Future Tyrant Empress'. https://www.youtube.com/watch?v=Ahr1vUkIdDw https://myanimepulse.com/manga/-130567/my-wife-is-actually-the-empress",
        "reviewed_at": "2026-10-11",
    },
])


REVIEWED.append({
    "video_id": "PtlAIwY5knk",
    "title": "I Become a God in Twelve Days, and the Whole World Is Hunting Me",
    "aliases": ["十二天后成神，我被全世界追杀"],
    "evidence": "Pesquisado pelo Momo Tracker; aplicado pela CLI porque o executor local do Dot falhou. Original de 芝士饭桶. Sequência 1:00:54–1:01:19 do vídeo: fuga como pássaro e perseguidores transformados em formigas corresponde ao capítulo 17. O recap adapta Lin Yu para Ryan Quinn. Título inglês é alias de catálogo, não edição oficial confirmada. https://www.youtube.com/watch?v=PtlAIwY5knk&t=3654s https://www.qidian.com/book/1050573847/ https://www.qidian.com/chapter/1050573847/925313243/ https://daosearch.io/qidian/book/1050573847/i-become-a-god-in-twelve-days-and-the-whole-world-is",
    "reviewed_at": "2026-10-11",
})


REVIEWED.extend([
    {
        "video_id": "Z-AghRYVoDc",
        "title": "The Return of the Scorned Genius",
        "aliases": [
            "深淵の主～蔑まれた天才の帰還～"
        ],
        "evidence": "Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:00–0:53, prodígio com ressonância superior a 100%, ferido ao proteger criança, cadeira de rodas e poderes selados com contagem regressiva; 2:05–2:14, busca o pai no Reino Divino; 18:15, classe Abyss Lord. A combinação específica corresponde à sinopse de The Return of the Scorned Genius; comentário também dá esse título. O recap usa Suo Tomahiro e o catálogo Chiyuan Suou; identificação apoiada no enredo, não na grafia do nome. https://www.youtube.com/watch?v=Z-AghRYVoDc&t=125s https://www.youtube.com/watch?v=Z-AghRYVoDc&t=1095s https://www.youtube.com/watch?v=Z-AghRYVoDc&lc=UgztKyioI4iPwS64HTB4AaABAg https://mangabaka.org/manhua/605878/The-Return-of-the-Scorned-Genius https://softkomik.co/the-return-of-the-scorned-genius-bahasa-indonesia . Alias japonês atestado em catálogos; Piccoma indicado por MangaBaka (https://piccoma.com/web/product/196779) bloqueia leitura fora do Japão, portanto não foi usado como evidência de conteúdo diretamente verificado.",
        "reviewed_at": "2026-10-11",
        "confirmado": True
    },
    {
        "video_id": "_ZcaDBS8AY8",
        "title": "My Girlfriend Returned as a Dragon",
        "aliases": [
            "My Dragon Girlfriend Has Returned",
            "드래곤 여친이 귀환했다"
        ],
        "evidence": "Pesquisado na nuvem pelo Momo Tracker. Descrição do próprio vídeo fornece os dois títulos ingleses. Transcrição: 0:00–0:49, namorada desapareceu num gate e retorna um ano depois; 2:01, identifica-se como Jong Sia, namorada de Minjun (grafia automática varia); 23:03–24:08, energia dracônica de Sia ameaça a vida de Minjun e ele precisa dominá-la completamente. Personagens e combinação específica do enredo correspondem à sinopse oficial da Naver, 드래곤 여친이 귀환했다, de LICO/뚠딴/세칸. https://www.youtube.com/watch?v=_ZcaDBS8AY8 https://www.youtube.com/watch?v=_ZcaDBS8AY8&t=121s https://www.youtube.com/watch?v=_ZcaDBS8AY8&t=1383s https://m.comic.naver.com/webtoon/list?titleId=855153&week=wed https://series.naver.com/novel/moreDetail.series?OSType=pc&productNo=12525081",
        "reviewed_at": "2026-10-11",
        "confirmado": True
    }
])


REVIEWED.extend([{'video_id': 'o9jlJepDKl8',
  'title': 'Slacking My Way to Immortality',
  'aliases': ['Becoming Immortal by Doing Nothing', '摆烂成仙', 'Bai Lan Cheng Xian'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. A transcrição pública mostra Kian/Keon Luo, '
              'herdeiro de uma família imortal, insultado durante um banquete (0:05–0:54); ele '
              'rejeita as ofertas de poder e riqueza do sistema (2:14–2:51) e contrata a '
              'cultivadora que o insultou por 10.000 pedras espirituais mensais (4:20–4:38). A '
              'sinopse oficial da WebNovel identifica Kian Luo e a poderosa família imortal; a '
              'sinopse da adaptação na LeTV confirma especificamente o banquete, a recusa do '
              "sistema e a contratação por 10.000 pedras. O próprio canal responde 'Becoming "
              "immortal by doing nothing' ao pedido de nome, usado como apoio, não como prova "
              'única. https://www.youtube.com/watch?v=o9jlJepDKl8&t=5s '
              'https://www.youtube.com/watch?v=o9jlJepDKl8&t=134s '
              'https://www.youtube.com/watch?v=o9jlJepDKl8&t=260s '
              'https://www.youtube.com/watch?v=o9jlJepDKl8&lc=UgzvNJXlB2_BwbsUqhB4AaABAg.AbiwJos3PC-AbkK6ys9kUi '
              'https://www.webnovel.com/comic/slacking-my-way-to-immortality_31895717908597701 '
              'https://www.le.com/comic/10080056.html '
              'https://www.kuaikanmanhua.com/web/topic/26907/',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'RNN7Ce1LJK4',
  'title': 'The Knight Only Lives Today',
  'aliases': ['Eternally Regressing Knight', 'Infinite Regressing Knight'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública do YouTube: 0:18–1:23, '
              'Enkrid (transcrição automática: Ankrid/Anker) sonha em ser cavaleiro após incentivo '
              'de um mercenário e lidera um esquadrão problemático; 1:31–2:34, morre com uma '
              'estocada na garganta e retorna à mesma manhã, com Rem encontrando sempre um inseto '
              'na bota; 2:47–3:03, aprende Beast Heart e repete batalha entre Naurilia e Aspen. '
              'Nome e ciclo de morte/treino correspondem à sinopse oficial WEBTOON de The Knight '
              'Only Lives Today. Comentário específico também lista o título e Eternally '
              'Regressing Knight, mas a confirmação se apoia no personagem e enredo. '
              'https://www.youtube.com/watch?v=RNN7Ce1LJK4&t=18s '
              'https://www.youtube.com/watch?v=RNN7Ce1LJK4&t=91s '
              'https://www.youtube.com/watch?v=RNN7Ce1LJK4&lc=Ugzi1obhlbmMukcxmlR4AaABAg '
              'https://usw-m.webtoons.com/en/fantasy/the-knight-only-lives-today/list?title_no=6672 '
              'https://m.webtoons.com/fr/action/the-knight-only-lives-today/list?title_no=6948 . O '
              'exportador de transcrição falhou, mas o painel público Show transcript carregou e '
              'foi lido diretamente.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'WBBmt_S2phg',
  'title': 'Bowblade Spirit',
  'aliases': ['Lord of the Bow and Blade', '궁귀검신', '궁귀검신 1부'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública do vídeo: 0:00–0:16, So '
              'Moon aprende arco com o avô em uma montanha; 0:55–1:28, flechas guiadas por energia '
              'contornam árvore e acertam aves; 3:27–4:58, cuida do falcão ferido por ordem do '
              'avô; 5:12–5:20, aprende técnica familiar de passos baseada no lobo. Personagem e '
              'combinação específica correspondem à análise de Bowblade Spirit da Popculture.id, '
              'que nomeia Eulji So Moon, avô, arco guiado por ki e passo do lobo. A sinopse '
              'oficial Naver de 궁귀검신 1부, de Cho Don-Hyung/Park Gwang-Jin, confirma treino com avô, '
              'viagem a Zhongyuan para buscar noiva e flecha guiada por ki superior à espada. '
              'https://www.youtube.com/watch?v=WBBmt_S2phg&t=7s '
              'https://www.youtube.com/watch?v=WBBmt_S2phg&t=312s '
              'https://popculture.id/bowblade-spirit-komik-pemanah-sakti/ '
              'https://series.naver.com/comic/detail.series?productNo=12295802 '
              'https://atsu.moe/manga/V1W7',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


def video_id(value):
    match = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})(?:[?&#/]|$)", value or "")
    return match.group(1) if match else None


def plan_updates(rows):
    if not rows or rows[0][:8] != [
        "quero_postar", "obra", "canal", "data_postado",
        "viewers", "duracao", "link", "nomes_variantes",
    ]:
        raise ValueError("Cabeçalho da aba todos diferente do esperado; nenhuma edição.")
    known = {item["video_id"]: item for item in REVIEWED}
    updates = []
    notes = []
    for index, row in enumerate(rows[1:], start=2):
        row = list(row) + [""] * max(0, 8 - len(row))
        item = known.get(video_id(row[6]))
        # Não sobrescrever nomes já presentes, nem variantes de outra identificação.
        if not item or str(row[1]).strip():
            continue
        updates.append({"range": f"B{index}", "values": [[item["title"]]]})
        if item["aliases"] and not str(row[7]).strip():
            updates.append({"range": f"H{index}", "values": [[
                " | ".join([item["title"]] + item["aliases"])
            ]]})
        notes.append((index, item))
    return updates, notes


def plan_confirmed(rows):
    """Linhas cuja obra e (ou vai ser, neste mesmo sync) o titulo de uma identificacao com
    `"confirmado": True`. Roda toda vez: e idempotente e cobre linha preenchida antes de
    a entrada ganhar o "confirmado". Se alguem trocou o nome na mao, nao marca."""
    known = {item["video_id"]: item for item in REVIEWED if item.get("confirmado")}
    marks = []
    for index, row in enumerate(rows[1:], start=2):
        row = list(row) + [""] * max(0, 8 - len(row))
        item = known.get(video_id(row[6]))
        if item and str(row[1]).strip() in ("", item["title"]):
            marks.append((index, item["evidence"]))
    return marks


def apply_reviewed(spreadsheet, sheet, dry_run=False):
    # Leitura fresca: ordenação/novas linhas podem ter mudado os índices.
    rows = sheet.get_all_values()
    updates, notes = plan_updates(rows)
    if dry_run:
        print(f"Identificações revisadas: {len(notes)} nomes disponíveis (sem gravar).")
        return len(notes)
    if updates:
        # RAW impede interpretação de títulos como fórmulas.
        sheet.batch_update(updates, value_input_option="RAW")
        spreadsheet.batch_update({"requests": [
            {"updateCells": {
                "range": {"sheetId": sheet.id, "startRowIndex": row - 1,
                          "endRowIndex": row, "startColumnIndex": 1, "endColumnIndex": 2},
                "rows": [{"values": [{"note":
                    "Identificação revisada em " + item["reviewed_at"] + ". " + item["evidence"]
                }]}],
                "fields": "note",
            }} for row, item in notes
        ]})
    # depois das notas acima: a nota de confirmado substitui a de "revisada".
    confirmacao.mark(spreadsheet, sheet, plan_confirmed(rows))
    print(f"Identificações revisadas: {len(notes)} nomes preenchidos.")
    return len(notes)
