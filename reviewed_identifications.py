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


REVIEWED.extend([{'video_id': 'UT1tTO-FWAU',
  'title': 'Lucky Billion Player',
  'aliases': ['The Billion-Luck Player',
              'Lucky Billion Players',
              'The Billion Lucky Player',
              '幸运亿的玩家'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:00–0:49, Fan Xiao '
              '(grafias automáticas Fon Shiao/Fans Shia) acumula sorte por um mês e ganha '
              'repetidamente na loteria; 3:18–4:23, entra no Evolution Game, escolhe Assassin e '
              'recebe Angel of Slaughter, associado aos sete pecados capitais. A página oficial da '
              'novel na Ciweimao identifica 范肖, a capacidade de poupar sorte para ganhar na '
              'loteria e o Evolution Game, e informa expressamente sua adaptação Tencent '
              'intitulada 幸运亿的玩家. Catálogos corroboram os títulos ingleses Lucky Billion Player / '
              'The Billion-Luck Player e a habilidade de sete pecados; comentário do vídeo também '
              'fornece Lucky Billion Player. https://www.youtube.com/watch?v=UT1tTO-FWAU&t=22s '
              'https://www.youtube.com/watch?v=UT1tTO-FWAU&t=198s '
              'https://www.youtube.com/watch?v=UT1tTO-FWAU&lc=UgxWGW2S6lEvUWsRFBF4AaABAg '
              'https://mip.ciweimao.com/book/100295569 '
              'https://ravenscans.org/manga/lucky-billion-player/ '
              'https://inkstory.net/content/the-billion-luck-player . Título inglês de catálogo; '
              'edição inglesa oficial não verificada.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'zVEmnB9PRCQ',
  'title': 'The Regressor and the Blind Saint',
  'aliases': ['The Regressor and the Blind Saintess', '회귀자와 맹인 성녀'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:07–0:38, marca do '
              'deus dos votos transforma restrições autoimpostas em poder; 0:58–1:07, antigo rei '
              'dos subúrbios regressa e promete proteger a santa cega; 1:22–1:46, heróis o '
              'amaldiçoaram após derrotar o lorde demônio; 2:11–3:23, encontra santa cega de '
              'cabelo branco tida por morta; 5:54–6:11, Vera/Bera e Renee são nomeados (grafia '
              'automática variável). A sinopse oficial da adaptação em quadrinhos da RIDI nomeia '
              '베라 (Vera/Bera), 르네 (Renee), a maldição, encontro no esgoto, morte da santa e '
              'regresso para protegê-la. Correspondência específica de personagens e trama; não '
              'depende de comentários. https://www.youtube.com/watch?v=zVEmnB9PRCQ&t=7s '
              'https://www.youtube.com/watch?v=zVEmnB9PRCQ&t=363s '
              'https://ridibooks.com/books/6344000001?type=rent '
              'https://mangabaka.org/manhwa/606406/The-Regressor-and-the-Blind-Saintess '
              'https://the-regressor-and-the-blind-saint.fandom.com/wiki/Vera',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'RzasqVwpLOA',
  'title': 'Infinite Rebate: Back Off, Senior Sister',
  'aliases': ['Ten-Thousandfold Return, Senior Sister, Please Behave',
              'Ten-Thousandfold Payback, Senior Sister, Have Some Self-Respect',
              '万倍返还，师姐请自重'],
  'evidence': 'Pesquisado exclusivamente na nuvem. Transcrição pública do recap: 0:15–0:54, '
              'protagonista Xiao Mu/Zhao Mu transmigrou como nobre noivo de uma princesa, foi '
              'sequestrado pela seita demoníaca e explorado por seu corpo Pure Yang; 2:20–3:02 '
              'desperta sistema de retorno de até 10.000 vezes, com primeira compensação '
              'garantida; 4:16–4:31 recebe Crimson Yang Sacred Body após ter energia extraída. '
              'Essa combinação específica e o personagem Zhao Mu correspondem às sinopses oficiais '
              'de Kuaikan e WebComics, que confirma o título inglês Infinite Rebate: Back Off, '
              'Senior Sister. https://www.youtube.com/watch?v=RzasqVwpLOA&t=15s '
              'https://www.youtube.com/watch?v=RzasqVwpLOA&t=140s '
              'https://www.youtube.com/watch?v=RzasqVwpLOA&t=256s '
              'https://www.kuaikanmanhua.com/web/topic/27125/ '
              'https://www.webcomicsapp.com/en/eastern-fantasy/infinite-rebate-back-off-senior-sister/69dde6cd62661d4e296bac38 '
              '. Aliases ingleses atestados em '
              'https://mudae.net/series/5082103/Ten-Thousandfold%20Return%2C%20Senior%20Sister%2C%20Please%20Behave '
              '.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'VZsId8F4DWY',
  'title': "Shut Up, Evil Dragon! I Don't Want to Raise a Child With You Anymore",
  'aliases': ["Shut up, Evil Dragon, I Don't Want to Raise A Child with You Anymore",
              'Shut Up, Evil Dragon! I Don’t Want to Raise a Child with You Anymore',
              'Shut Up, Malevolent Dragon! I Don’t Want to Have Any More Children With You',
              '闭嘴恶龙我不想再跟你带孩子了'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Descrição do uploader liga a playlist com o '
              "nome Shut Up, Evil Dragon, I Don't Want to Raise a Child With You Anymore. "
              'Transcrição: 0:00–0:14, rainha do clã dos dragões prateados, inimiga há dez anos, '
              'tem filhas gêmeas híbridas após maldição de sangue; 0:55–1:11, o matador de dragões '
              'é traído pelos compatriotas e capturado por Loswiss; 3:02–4:01, maldição do sangue '
              'cria ligação de almas. A sinopse oficial inglesa LoLoBun nomeia Leon, captura pela '
              'Silver Dragon Queen e a maldição proibida, correspondendo à combinação específica '
              'do vídeo; a edição chinesa está na SFACG. '
              'https://www.youtube.com/watch?v=VZsId8F4DWY '
              'https://www.youtube.com/watch?v=VZsId8F4DWY&t=55s '
              'https://www.youtube.com/watch?v=VZsId8F4DWY&t=182s https://www.lolobun.com/c/20103 '
              'https://manhua.sfacg.com/mh/BZELW/ '
              'https://www.novelupdates.com/series/shut-up-malevolent-dragon-i-dont-want-to-have-any-more-children-with-you/',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'sfUeECfxfRo',
  'title': '全民选择进化，我选孢子产氧气',
  'aliases': [],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública, 0:00–0:34: bilhões '
              'participam de um jogo de evolução ligado à sobrevivência dos países; Su Bai escolhe '
              'esporos produtores de oxigênio e elimina organismos anaeróbicos; peixe supera '
              'hipóxia, pequeno mamífero supera asteroide e, na quarta versão, ele escolhe primata '
              'e investe todos os pontos no cérebro. A descrição reforça Su Bai, fotossíntese e '
              'extinção por oxigênio. A sinopse da obra de 何时能起飞 no catálogo de 小说阅读网 confirma o '
              'protagonista 苏白, o jogo 进化狂潮, esporo unicelular, pontos em fotossíntese/oxigênio e '
              'extinção de 99% dos anaeróbios. Correspondência específica de personagem e '
              'mecânica, não apenas semelhança de título. '
              'https://www.youtube.com/watch?v=sfUeECfxfRo&t=0s '
              'https://www.youtube.com/watch?v=sfUeECfxfRo&t=7s '
              'https://www.youtube.com/watch?v=sfUeECfxfRo&t=28s '
              'https://www.readnovel.com/bqx/njwzmilwlw https://m.readnovel.com/bqx/sknjosamlw . '
              'Mantido título chinês atestado; não foi verificada edição inglesa oficial. A '
              'tentativa de visualizar o cartão final em 2:49:18 permaneceu carregando e não é '
              'usada como prova.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'wzUi2N73tco',
  'title': "The Back Alley Mage's Second Life",
  'aliases': ['Return of the Back Alley Wizard', "The Back-Alley Mage's Return", '뒷골목 마법사의 회귀생활'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:14–1:27, Aster, '
              'antigo mendigo da zona cinzenta e mercenário, foge da família Declan, é morto por '
              'Faren von Declan após queimar um grimório e retorna à infância; 2:15–2:38, pretende '
              'criar uma biblioteca/torre aberta a todos e expor o manual secreto dos Declan na '
              'entrada. Personagem e combinação específica de regressão, família e projeto da '
              'biblioteca coincidem com a sinopse oficial Naver de 뒷골목 마법사의 회귀생활. WEBTOON publica '
              "a edição inglesa com o título The Back Alley Mage's Second Life e identifica Aster. "
              'https://www.youtube.com/watch?v=wzUi2N73tco&t=14s '
              'https://www.youtube.com/watch?v=wzUi2N73tco&t=135s '
              'https://m.comic.naver.com/webtoon/list?titleId=841129 '
              'https://series.naver.com/comic/detail.series?productNo=12931289 '
              'https://www.webtoons.com/en/fantasy/the-back-alley-mages-second-life/list?title_no=9175 '
              'https://www.anime-planet.com/manga/return-of-the-back-alley-wizard . Descrição do '
              'vídeo declara capítulos 1–46, mas não foi necessária como prova de identidade.',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


REVIEWED.extend([{'video_id': 'QRgV-BiVMLk',
  'title': 'Sword of the Undying',
  'aliases': ['The Necromancer of a Renowned Sword Family',
              'The Necromancer of the Renowned Sword Family',
              'The Necromancer of a Swordsmanship Family',
              '검술명가의 네크로맨서'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:00–0:14 nomeia Klein '
              'da família Reinrandt (grafias automáticas Klene/Rinrand); 0:38, ao nascer recita '
              'invocação como Archimond; 0:47, passou sete anos preso numa igreja; 1:03–1:21, é a '
              'reencarnação do necromante Archimond, derrotado 200 anos antes por Berkel '
              'Reinrandt. A sinopse oficial Naver de 검술명가의 네크로맨서 confirma os dois personagens, '
              'morte pela espada do herói, intervalo de 200 anos e bebê que recita a invocação; o '
              'capítulo 1 é intitulado Klein Reinrandt. Comentário do vídeo sugere Sword of the '
              'Undying, alias inglês também documentado nos catálogos, mas a confirmação vem da '
              'trama e nomes. https://www.youtube.com/watch?v=QRgV-BiVMLk&t=38s '
              'https://www.youtube.com/watch?v=QRgV-BiVMLk&t=63s '
              'https://www.youtube.com/watch?v=QRgV-BiVMLk&lc=Ugw7hoZmVGag0ov243Z4AaABAg '
              'https://m.comic.naver.com/webtoon/list?titleId=850499&week=fri '
              'https://series.naver.com/comic/detail.series?productNo=14132199 '
              'https://www.asurascans.com/comics/sword-of-the-undying-b6e039fe',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'ZChs2KiSak8',
  'title': 'Absolute Necromancer: Ascension Through Skeleton Clone',
  'aliases': ['Becoming Necromancer God Through a Skeleton Clone',
              'Necromancer: Becoming a God Starting with Skeleton Clone',
              '亡灵法师：从骷髅分身开始成神'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:08–0:35, protagonista '
              'desperta necromante considerado fraco e obtém acesso ao reino dos mortos; '
              '5:01–6:38, o sistema cria um clone esqueleto nesse reino, permite possuí-lo e '
              'devorar mortos-vivos para ganhar atributos e invocações. Essa mecânica específica '
              'corresponde à sinopse oficial de 亡灵法师：从骷髅分身开始成神, da 爱豆喵漫画, no Kuaikan. O recap '
              'pronuncia Fang Zhou com variantes de legenda; professor Lu Hu e aluna Bai Xiaochan '
              'também aparecem (1:45 e 7:16). Comentário fornece o título inglês e catálogos '
              'externos o relacionam ao título chinês, usado apenas como apoio. '
              'https://www.youtube.com/watch?v=ZChs2KiSak8&t=8s '
              'https://www.youtube.com/watch?v=ZChs2KiSak8&t=301s '
              'https://www.youtube.com/watch?v=ZChs2KiSak8&t=359s '
              'https://www.kuaikanmanhua.com/web/topic/27711/ '
              'https://www.mangaread.org/manga/becoming-necromancer-god-through-a-skeleton-clone/',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'mfCNyWlZq2w',
  'title': 'The End Has Come',
  'aliases': ['종말이 찾아왔다',
              'The Apocalypse Has Arrived',
              'The Apocalypse Has Come',
              'The Apocalypse Is Here'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:15–1:26, Minjun e '
              'Yena (transcrição automática Yana/Jana/Yenna) atravessam cidade infestada e '
              'discutem por água; ela o menospreza pela pobreza, mas depende dele para escapar dos '
              'infectados; 2:49–3:28, ela volta pedindo ajuda para chegar a Gangnam, é descrita '
              'como garota rica e popular, enquanto Minjun era pobre e sofria bullying antes do '
              'vírus devastar Seul. Essa dupla e a premissa correspondem diretamente às sinopses '
              'oficiais WEBTOON e Naver (정민준, 한예나). Comentário dá The End Has Come, corroborado '
              'por personagens/enredo, não usado isoladamente. '
              'https://www.youtube.com/watch?v=mfCNyWlZq2w&t=15s '
              'https://www.youtube.com/watch?v=mfCNyWlZq2w&t=169s '
              'https://www.youtube.com/watch?v=mfCNyWlZq2w&lc=UgzBcup6WW9vdMxjAo14AaABAg '
              'https://www.webtoons.com/en/thriller/the-end-has-come/list?title_no=8421 '
              'https://m.comic.naver.com/webtoon/list?titleId=838002 '
              'https://mangatlas.com/title/the-end-has-come',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'cgQuVO6OeSQ',
  'title': 'Leveling Up: Reshaping the World',
  'aliases': ['I Use a Top-Tier System to Reshape the World', '我用顶级系统重塑世界'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:26–1:07, protagonista '
              'Wei (transcrição Wii/Weii) é F-rank incapaz de subir de nível num planeta refeito '
              'por inteligência artificial Creation; a fusão com um companheiro permite analisar '
              'inimigos/copiar habilidades, e ele quer derrubar os criadores dessa ordem e '
              'reconstruir o mundo. Em 2:23–2:40, seu amuleto veio de um companheiro robô, e as '
              'inteligências artificiais foram destruídas após a revolução. A premissa específica '
              'da IA Creator que reformata a realidade em níveis/monstros e a missão de derrubar '
              'seu regime correspondem às sinopses oficiais Tapas e WEBTOON. Tapas confirma título '
              'original 我用顶级系统重塑世界; comentário do vídeo fornece os dois títulos ingleses, '
              'corroborados pela trama. https://www.youtube.com/watch?v=cgQuVO6OeSQ&t=26s '
              'https://www.youtube.com/watch?v=cgQuVO6OeSQ&t=143s '
              'https://www.youtube.com/watch?v=cgQuVO6OeSQ&lc=Ugwm7SmnWh5fdJYwDol4AaABAg '
              'https://tapas.io/series/leveling-up-reshaping-the-world/info '
              'https://www.webtoons.com/en/action/leveling-up-reshaping-the-world/list?title_no=10229',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'IMISaGSZcR4',
  'title': 'Copying Skills with Affinity!',
  'aliases': ['Copy Skills with Affinity!', '호감도로 스킬 복사!'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:24 nomeia Aiden '
              'Kellerman (variante automática de Kellermain); 0:57–1:13, vigarista lembra a Terra '
              'e sabe que vive num jogo; 2:11 nomeia Noel Astria; 2:42–3:31, ela o sequestra e '
              'exige que finja ser seu marido durante um ano; 3:40–3:49, sistema Weaver of Fate '
              'permite copiar habilidade dela. Sinopse oficial Naver da adaptação 호감도로 스킬 복사! '
              'confirma Aiden, vigarista, sequestro pela maior cavaleira do império e casamento '
              'fingido por um ano; a sinopse oficial da novela confirma a habilidade 운명의 길쌈꾼 '
              '(Weaver of Fate) e cópia por afinidade. '
              'https://www.youtube.com/watch?v=IMISaGSZcR4&t=24s '
              'https://www.youtube.com/watch?v=IMISaGSZcR4&t=203s '
              'https://m.comic.naver.com/webtoon/list?titleId=855599&week=sat '
              'https://series.naver.com/comic/detail.series?productNo=14773359 '
              'https://series.naver.com/novel/detail.series?productNo=11147099 '
              'https://mangabaka.org/manhwa/605992/Copying-Skills-with-Affinity '
              'https://www.novelupdates.com/series/copy-skills-with-affinity/',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': '_y1P2hYlMUM',
  'title': 'Ode of the Brave',
  'aliases': ["The Warrior's Ballad",
              "Hero's Ballad",
              'Ballad of the Hero',
              "The Hero's Ballad",
              '용사의 발라드'],
  'evidence': 'Pesquisado exclusivamente na nuvem. Transcrição pública: 0:08–0:40 nomeia Ricky, '
              'enfrenta Vulca na academia e o identifica como Steel Reaper e primeiro swordmaster '
              'do continente; 1:20–1:44, foi pastor nas planícies de Heiden; 2:24–2:38 foi '
              'convocado por sorteio; 9:21 menciona cem anos separando a guerra da nova vida; '
              '42:18, Rickart/Ricardt é terceiro filho da casa Stormt. Naver confirma Ricky, '
              'pastor de Heiden, Steel Reaper morto e reencarnado cem anos depois como terceiro '
              "filho de nobres; WEBTOON inglês confirma Ricardt e título oficial The Warrior's "
              'Ballad. https://www.youtube.com/watch?v=_y1P2hYlMUM&t=8s '
              'https://www.youtube.com/watch?v=_y1P2hYlMUM&t=80s '
              'https://www.youtube.com/watch?v=_y1P2hYlMUM&t=561s '
              'https://www.youtube.com/watch?v=_y1P2hYlMUM&t=2538s '
              'https://m.comic.naver.com/webtoon/list?titleId=854122&week=sun '
              'https://www.webtoons.com/en/action/the-warriors-ballad/list?title_no=11210 . '
              'Aliases atestados em https://mangakatana.com/manga/ode-of-the-brave.27936 .',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'AW98afSTGEU',
  'title': 'All I Can See Is You',
  'aliases': ['I Can Only See You', 'I Only See You', '너만 보인단 말이야'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:00–1:19, após vinte '
              'rejeições, Park Jinyong segue a orientação do amigo imaginário Jason e passa cinco '
              'anos enxergando garotas como pedras; uma garota é a primeira exceção. Aos 3:46 ele '
              'se apresenta como Park Jin-yong; aos 5:27 a garota é chamada Sunwoo. Personagens e '
              'premissa incomum correspondem integralmente à sinopse oficial de 너만 보인단 말이야, de '
              '채군/닷지, na Naver Series: Park Jinyong, amigo imaginário Jason, mulheres como pedras, '
              'Sunwoo como exceção após cinco anos. Títulos ingleses atestados em catálogos de '
              'tradução. https://www.youtube.com/watch?v=AW98afSTGEU&t=15s '
              'https://www.youtube.com/watch?v=AW98afSTGEU&t=72s '
              'https://www.youtube.com/watch?v=AW98afSTGEU&t=226s '
              'https://www.youtube.com/watch?v=AW98afSTGEU&t=327s '
              'https://series.naver.com/comic/detail.series?productNo=13939347 '
              'https://comic.naver.com/webtoon/list?titleId=849279 '
              'https://lunatoons.net/all-i-can-see-is-you',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


REVIEWED.extend([{'video_id': 'QvBiMfQZQz8',
  'title': 'Idle Player Returns as a God',
  'aliases': ['I Awoke as a God After Auto Battling for a Million Years',
              'After Millions of Years, I Woke Up to Be a God!',
              '网游：挂机百万年，我醒来成神'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. A descrição do uploader identifica Idle '
              'Player Returns as a God. Transcrição pública: 0:54–1:18, herói Shu Luo morreu '
              'protegendo o Dragon Kingdom e é lembrado no centenário; 2:20–2:43, reencarna em '
              'jovem homônimo (Zhang Yue, transcrição Jang Yua); 3:03–3:19, sistema o reconhece '
              'como Shu Luo e informa 36.552 dias offline; 3:28–4:22, recompensa Supreme Oracle e '
              'seleção de necromante como classe mítica; 5:08 troca o ID para Zero. Capítulo 1 '
              'oficial da novela em Zongheng nomeia 张越/修罗, 36.552 dias offline, morte há 100 anos, '
              'tesouro 至尊神谕 e escolha de 死灵法师; adaptação oficial encontrada em Kuaikan. '
              'Correspondência específica, independente do título informado no vídeo. '
              'https://www.youtube.com/watch?v=QvBiMfQZQz8&t=54s '
              'https://www.youtube.com/watch?v=QvBiMfQZQz8&t=192s '
              'https://m.zongheng.com/book/1271862 '
              'https://www.kuaikanmanhua.com/webs/comic-next/739064 '
              'https://www.novelupdates.com/series/idle-player-returns-as-a-god/ . A transcrição '
              'diz bônus 999 vezes enquanto a novela diz 9999; esta discrepância numérica não foi '
              'usada para confirmar o título.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': '9O28Mn4LNyM',
  'title': 'For My Own Good',
  'aliases': ["I'll Retire After Saving the World",
              'I Will Save the World and Retire',
              'I Will Save the World And Then Retire',
              '세상만 구하고 은퇴하겠습니다'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 2:28–4:42, Woo '
              'Hwijae/Heejae (grafias automáticas Wuhi Jay/Hi Jay) trabalha na agência de gestão '
              'de habilidades e é filho adotivo do hunter Hong Seokyoung; 10:18–11:41, um '
              'dispositivo o salva do colapso do mundo transportando-o vinte anos ao passado, para '
              '5/4/2024, junto dos alunos da Hunter Academy; 1:46:31 é identificado como instrutor '
              'Woo Hwijae. A sinopse oficial WEBTOON de For My Own Good identifica Woo Heejae e a '
              'viagem de 2044 para 2024, usando conhecimento futuro para ensinar hunters e salvar '
              'o mundo. A edição alemã oficial confirma seu emprego na agência e o objeto '
              'temporal. https://www.youtube.com/watch?v=9O28Mn4LNyM&t=148s '
              'https://www.youtube.com/watch?v=9O28Mn4LNyM&t=618s '
              'https://www.youtube.com/watch?v=9O28Mn4LNyM&t=6391s '
              'https://www.webtoons.com/id/fantasy/for-my-own-good/list?title_no=6900 '
              'https://www.webtoons.com/de/fantasy/for-my-own-good/list?title_no=7535 '
              'https://www.mangaread.org/manga/ill-retire-after-saving-the-world/chapter-26-1/ . '
              'For My Own Good é título oficial usado nas edições internacionais verificadas; '
              'aliases e coreano corroborados pelo catálogo.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'u2UfQ4zTVTQ',
  'title': 'I Am the Strongest Transcendent',
  'aliases': ['I am the Most Powerful Transcendent Being', '俺だけ最強超越者～全世界のチート師匠に認められた～'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Descrição do vídeo nomeia I am the Most '
              'Powerful Transcendent Being. Transcrição: 0:32, protagonista Minato Kannagi; '
              '1:31–1:38, reprova três vezes no exame de hunter; 4:46–5:41, Kaisei Hizaki o leva '
              'ao santuário dos Progenitores e profana as tumbas; 8:33–8:41, Minato exige os '
              'poderes de todos os espíritos; 11:14, confirma possuir 106 almas heroicas. '
              'Personagem, armadilha na tumba e 106 Progenitores correspondem à sinopse da edição '
              'oficial WEBTOON I Am the Strongest Transcendent, de Eto Shunji/Tsuchida Kenta. '
              'https://www.youtube.com/watch?v=u2UfQ4zTVTQ&t=32s '
              'https://www.youtube.com/watch?v=u2UfQ4zTVTQ&t=286s '
              'https://www.youtube.com/watch?v=u2UfQ4zTVTQ&t=513s '
              'https://www.youtube.com/watch?v=u2UfQ4zTVTQ&t=674s '
              'https://m.webtoons.com/en/fantasy/i-am-the-strongest-transcendent/list?title_no=6676 '
              'https://www.anime-planet.com/manga/i-am-the-strongest-transcendent/characters',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


REVIEWED.extend([{'video_id': 'a9i82-nZRE8',
  'title': "Go Deok-chun's Food Truck",
  'aliases': ["Go Deokchun's Food Truck", "Godeokchun's Food Truck", '고덕춘의 푸드트럭'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:44–2:15, protagonista '
              'arruinado por golpe de compras recebe takoyaki grátis de Deok-chun, passa três anos '
              'ajudando no food truck e, após a morte do mentor, promete levar o nome Go Deok-chun '
              'ao país inteiro; 2:22–2:56, apresenta Sehee, filha de magnata; 4:14–5:45, ela '
              'começa a trabalhar no food truck e o protagonista é chamado Jun/June (Junho). A '
              'combinação do food truck herdado do falecido Deokchun, Junho viajando para divulgar '
              'seu nome, e herdeira Sehee é explicitamente confirmada pela sinopse oficial Naver '
              'Series e Naver Webtoon de 고덕춘의 푸드트럭, por 포포. Catálogos corroboram as grafias '
              'inglesas. https://www.youtube.com/watch?v=a9i82-nZRE8&t=44s '
              'https://www.youtube.com/watch?v=a9i82-nZRE8&t=127s '
              'https://www.youtube.com/watch?v=a9i82-nZRE8&t=321s '
              'https://series.naver.com/comic/detail.series?productNo=13407372 '
              'https://comic.naver.com/webtoon/list?tab=sun&titleId=844982 '
              'https://komascans.com/en/series/go-deok-chuns-food-truck '
              'https://www.manhwaden.com/manga/godeokchuns-food-truck/ . Inglês é título de '
              'catálogo/romanização; edição inglesa oficial não verificada.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'q5vSNczWC2c',
  'title': 'Hoarding in Hell',
  'aliases': ['지옥에서 독식', 'Jiogeseo Doksik'],
  'evidence': 'Pesquisado na nuvem pelo Momo Tracker. Transcrição pública: 0:00–0:26, protagonista '
              'recolhe musgo cristalino com mana em esgotos com uma colega; 0:41, televisão '
              'noticia a conquista da masmorra Taebaek de cinco estrelas; 0:49–0:57, advogado '
              'comunica a morte do pai e entrega medalhão herdado; 1:30–2:06, ao apertar o '
              'medalhão, é transportado a mundo arruinado, sem sol, identificado como estrela do '
              'apocalipse e dificuldade Hell; 2:14–3:45 morre e ressuscita repetidamente; 5:44 '
              'recebe missão de sobreviver à primeira noite. A edição oficial Tapas de Hoarding in '
              'Hell identifica Hyunmoo Kang, mineiro que herda hearthstone, vai ao Inferno, morre '
              'e regenera para desenvolver habilidades e acumular itens; sua lista de episódios '
              'inclui An Inheritance, First Night in Hell e Selling Crystal Moss. O capítulo 1 da '
              'novela, em fonte secundária, confirma os detalhes distintivos do esgoto/musgo '
              'cristalino, colega Yumin, advogado, herança paterna e notícia do clã Taeseong '
              'conquistando Taebaek. Manga News confirma título original 지옥에서 독식. O recap usa '
              'nomes ocidentalizados (Buster/Bugster, Judy e Robert) em vez dos nomes originais; a '
              'confirmação baseia-se na sequência específica de eventos, não nessa nomenclatura. '
              'https://www.youtube.com/watch?v=q5vSNczWC2c&t=0s '
              'https://www.youtube.com/watch?v=q5vSNczWC2c&t=49s '
              'https://www.youtube.com/watch?v=q5vSNczWC2c&t=107s '
              'https://tapas.io/series/hoarding-in-hell/info '
              'https://www.fanmtl.com/novel/hoarding-in-hell-novel_1.html '
              'https://www.manga-news.com/index.php/serie/Hoarding-in-Hell',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


REVIEWED.extend([{'video_id': 'F93-5vx5OHQ',
  'title': 'You Might Die If I Use My Healing Skills On You',
  'aliases': ['If I Use My Healing Skills, You May Die', '我一个治疗术下去你可能会死'],
  'evidence': 'Transcrição pública do vídeo: 0:00–0:42, em 2050 o VR Immortals afeta a realidade, '
              'Jiang Chen/Mortal morre diante de um deus após sacrificar artefato yin-yang e '
              'retorna ao lançamento; 0:42–1:17, Xia Ruier entrega o capacete; 1:32–1:49 escolhe '
              'sacerdote com talento Yin-Yang Inversion; 2:06 chega à vila inicial 1001; 3:58 '
              "coleta 705 chifres; 5:30 obtém Cupid's Blessing. A página oficial da novel na "
              'Fanqie identifica Jiang Chen, jogo 諸神, sacerdote regressado cujas curas e bênçãos '
              'viram dano e maldição, e declara explicitamente a adaptação em quadrinhos '
              '我一个治疗术下去你可能会死. Seu índice inicia com entrada no jogo, inversão yin-yang, caçada de '
              'ovelhas e bênção de Eros, mesma sequência do vídeo. DragonTea atesta o título '
              'inglês e alias com Jiang Chen e essa premissa; o catálogo chinês Qimanwu confirma o '
              'mesmo título. https://www.youtube.com/watch?v=F93-5vx5OHQ&t=0s '
              'https://www.youtube.com/watch?v=F93-5vx5OHQ&t=92s '
              'https://www.youtube.com/watch?v=F93-5vx5OHQ&t=330s '
              'https://fanqienovel.com/page/7008014590231448613 '
              'https://dragontea.ink/novel/you-might-die-if-i-use-my-healing-skills-on-you/ '
              'https://qimanwu.org/comic/Ob2NaZ6vKn . O capítulo inicial corroborado traz ainda '
              '2050, Jiang Chen, artefato yin-yang e Xia Ruier: '
              'https://m.shuhaige.net/213760/90373205.html . Distinção revisada: Não confundir com '
              'You Might Die If I Cast My Healing Spell/Catastrophic Priest, cuja história é de '
              'Lin Ye; o vídeo é de Jiang Chen e jogo VR.',
  'reviewed_at': '2026-10-11',
  'confirmado': True},
 {'video_id': 'pHR4Ytni2Bg',
  'title': 'The Old Man Vows Revenge Against His Demon Wife',
  'aliases': ['The Man Who Vowed Revenge on His Demon Wife',
              'Ossan, Oniyome e no Fukushuu o Chikau',
              'おっさん、鬼嫁への復讐を誓う'],
  'evidence': 'Descrição pública do próprio vídeo nomeia expressamente The Old Man Vows Revenge '
              'Against His Demon Wife. Transcrição 0:00–0:17 descreve masmorras surgidas há 70 '
              'anos, descoberta de mana e Seishirou (grafado Seiru na legenda) salvando mulher '
              'oni; 0:17–0:57, esposa Ruka torna-se cruel após morte do pai, trai o marido, mata a '
              'filha e o atira na masmorra. 5:00–7:57, vampira Elana oferece pacto de vingança que '
              'deixa apenas um ano de vida. JumpTOON oficial e anúncio do autor confirmam título '
              'japonês, protagonista 誠志郎/Seishirou, masmorras há 70 anos, mulher oni resgatada, '
              'casamento e traição que lhe retira tudo. Os catálogos externos associam '
              'explicitamente os títulos inglês e japonês. '
              'https://www.youtube.com/watch?v=pHR4Ytni2Bg '
              'https://www.youtube.com/watch?v=pHR4Ytni2Bg&t=0s '
              'https://www.youtube.com/watch?v=pHR4Ytni2Bg&t=300s '
              'https://jumptoon.com/series/JT00120/ '
              'https://mypage.syosetu.com/mypageblog/view/userid/638162/blogkey/3681362/ '
              'https://softkomik.co/the-old-man-vows-revenge-against-his-demon-wife-bahasa-indonesia '
              '.',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


REVIEWED.extend([{'video_id': 'E-NdLRfVBIg',
  'title': 'The Wind Mage',
  'aliases': ['바람의 마도사'],
  'evidence': 'Transcrição pública: 0:07–1:02, Simon tem afinidade com espírito pássaro e perde '
              'pessoas queridas; 2:22–3:12 salva aldeia inundada com espírito do vento; 6:30–8:15 '
              'desmascara falso mago e invoca Elcane, rei dos espíritos do vento; 30:16 procura '
              'Klein Hayes; 40:44–42:32 aparecem Diana, Raiden, mestre Rouette e Klein; 2:19:08 '
              'nome Ranian. Catálogos inglês Thunderscans e QiManga identificam Simon Hice/Heis, '
              'depois Ranian/Lanian, pai Klein, mestre Rosette/Ruzette, Diana e irmão Raidin na '
              'obra The Wind Mage/바람의 마도사. Namu documenta Elcane/엘케인 e o episódio exclusivo do '
              'webtoon com falso mago do vento. KakaoWebtoon oficial confirma título coreano e '
              'autoria Next Level Studio/Kim Geun-woo. '
              'https://www.youtube.com/watch?v=E-NdLRfVBIg&t=7s '
              'https://www.youtube.com/watch?v=E-NdLRfVBIg&t=495s '
              'https://www.youtube.com/watch?v=E-NdLRfVBIg&t=1816s '
              'https://www.youtube.com/watch?v=E-NdLRfVBIg&t=2444s '
              'https://www.youtube.com/watch?v=E-NdLRfVBIg&t=8348s '
              'https://en-thunderscans.com/comics/the-wind-mage/ '
              'https://qimanga.com/series/the-wind-mage https://m.namu.moe/w/바람의%20마도사 '
              'https://webtoon.kakao.com/content/바람의-마도사/4934 .',
  'reviewed_at': '2026-10-11',
  'confirmado': True}])


REVIEWED.append({'video_id': '4zgCQqFhDxM',
 'title': 'The Crazy Villain Regains His Sanity',
 'aliases': ['미친 빌런이 정신을 되찾음'],
 'evidence': 'Transcrição pública: 0:00–0:49, Junho conversa com a irmã sobre trabalho como '
             'servidor público antes de um assalto a banco; 3:28–3:37, após derrotar os '
             'assaltantes, quase usa seu antigo nome de vilão (grafado Bloodkin na legenda '
             'automática), mas se corrige para futuro hunter do serviço público. 4:30–5:41, dom '
             'de consumir sangue/essência absorve habilidades, corrompe sua mente e gera '
             'personalidade destrutiva; 6:51–6:58, a legenda automática registra Chay Junho, de '
             'volta à mesa da família como desempregado de 25 anos. A página oficial do '
             'quadrinho no Kakao identifica 최준호 (Choi Junho), ex-vilão 혈종, dom 혈중섭식 que o faz '
             'perder o autocontrole, e Junho recuperado tornando-se servidor público para '
             'combater vilões; créditos Next Level Studio, original 김현우. A combinação específica '
             'de personagem, poder e carreira confirma a identificação. Novel Updates associa o '
             'título inglês ao coreano e a Choi Joon-ho; a descrição do próprio criador também '
             'nomeia o título inglês. Edição inglesa oficial não verificada. '
             'https://www.youtube.com/watch?v=4zgCQqFhDxM&t=0s '
             'https://www.youtube.com/watch?v=4zgCQqFhDxM&t=208s '
             'https://www.youtube.com/watch?v=4zgCQqFhDxM&t=270s '
             'https://www.youtube.com/watch?v=4zgCQqFhDxM&t=411s '
             'https://page.kakao.com/content/70776768/?tab_type=about '
             'https://www.novelupdates.com/series/the-crazy-villain-regains-his-sanity/',
 'reviewed_at': '2026-10-12',
 'confirmado': True})

REVIEWED.append({
    "video_id": "cOEwYHR3DDE",
    "title": "合约疯妻",
    "aliases": [],
    "evidence": (
        "Identificação do manju chinês de animação por IA, pelo título original. "
        "Transcrição pública em hindi lida na tentativa anterior de 12/10/2026: "
        "0:17–1:15, protagonista simula a morte após contrato conjugal de cinco anos "
        "e passa a viver com irmã e sobrinha; 2:05–3:26, reencontra a esposa durante "
        "compras de relógio com a sobrinha; 5:11–6:28, é sequestrado. A página externa "
        "Duanju Baike nomeia 合约疯妻, Jiang Bai (姜白) e Chen Keyue (陈可月), e reproduz "
        "a sequência específica: contrato de cinco anos, morte simulada, irmã e "
        "sobrinha, encontro no shopping e rapto após golpe na cabeça. Seus 18 episódios "
        "somam 28 minutos, compatíveis com o recap de 27:54–27:55. Metadados do vídeo "
        "conferidos novamente nesta revisão. Título e nomes vêm de um único catálogo "
        "externo; comparação de enredo usa a transcrição já lida, sem alegar nova "
        "transcrição ou correspondência visual, pois essas coletas falharam nesta "
        "rodada. Edição inglesa, alias inglês e eventual novel ou quadrinho original "
        "separado não verificados. "
        "https://www.youtube.com/watch?v=cOEwYHR3DDE&t=17s "
        "https://www.youtube.com/watch?v=cOEwYHR3DDE&t=125s "
        "https://www.youtube.com/watch?v=cOEwYHR3DDE&t=311s "
        "https://www.duanjubaike.net/manju/info-7596877098732506137.html"
    ),
    "reviewed_at": "2026-10-12",
    "confirmado": True,
})


REVIEWED.append({
    "video_id": "u-balFxgGDY",
    "title": "我能加载旧日设定",
    "aliases": [],
    "evidence": "Descrição pública do próprio vídeo, observada em 12/10/2026 às 13:24 UTC e preservada na primeira pesquisa, corresponde aos capítulos 1–3 da novel de 鹅毛浮开水: câncer terminal de pulmão, busca de três anos pelo sobrenatural, mansão herdada e Codex of Fate (命运法典) visível só ao protagonista. O capítulo 2 confirma que morrer por ação de um deus permite retroceder ou reviver e obter poder divino por vingança; o capítulo 3 encena a primeira morte e essas escolhas. Correspondência específica de trama e mecânicas, não apenas sinopse genérica. A equivalência entre Dorian Lockwood, citado pelo canal, e 陆延年 (Lu Yannian), da fonte chinesa, é inferida; não foi verificada uma edição ou alias oficial em inglês. A revisão usou a descrição anteriormente lida e novos capítulos externos, sem nova transcrição, frames ou timestamps do vídeo. https://www.youtube.com/watch?v=u-balFxgGDY https://www.198touzi.com/book/127911/ https://www.198touzi.com/book/127911/54894331.html https://www.198touzi.com/book/127911/54894332/2.html https://www.198touzi.com/book/127911/54894333/2.html",
    "reviewed_at": "2026-10-12",
    "confirmado": True
})


REVIEWED.append({
    "video_id": "p5C2EkqAjKM",
    "title": "断绝关系？我反手激活万倍返利！",
    "aliases": [],
    "evidence": (
        "Novel chinesa de 咸鱼小笼包, identificada pelo título original oficial. "
        "Transcrição pública preservada da pesquisa anterior: 0:25–3:12, Xiao Fan, "
        "sete irmãs, sacrifício na vida anterior, rompimento familiar e ativação do "
        "sistema; 4:12–5:09, saldo de 38 yuan e água de 1 yuan que rende 10.000 pontos "
        "de qi/sangue; 7:15–9:11, loteria de 36 yuan em 18 apostas, prêmio de 324 "
        "milhões, imposto de 64,8 milhões e líquido de 259,2 milhões, com técnica "
        "de combate e cartão preto; 9:42–11:01, compra da escola Dragon Tiger por "
        "3 milhões e energia maligna de um osso. Na revisão de 12/10/2026, leitura "
        "nova dos capítulos oficiais 1–4 no Fanqie confirma a mesma sequência, "
        "os valores exatos, 萧凡 (Xiao Fan), falso herdeiro 林风 (Lin Feng), "
        "龙虎武馆 e herança 混沌神魔诀. Lin Fang da legenda automática anterior "
        "é corrigido pela fonte chinesa. Correspondência da novel de origem; "
        "quadrinho separado, edição inglesa e aliases em inglês não verificados. "
        "Esta revisão não fez nova transcrição nem comparação visual do vídeo. "
        "https://www.youtube.com/watch?v=p5C2EkqAjKM&t=25s "
        "https://www.youtube.com/watch?v=p5C2EkqAjKM&t=252s "
        "https://www.youtube.com/watch?v=p5C2EkqAjKM&t=435s "
        "https://www.youtube.com/watch?v=p5C2EkqAjKM&t=582s "
        "https://fanqienovel.com/page/7538015427515911193 "
        "https://fanqienovel.com/reader/7538019216746627609 "
        "https://fanqienovel.com/reader/7538019374322418201 "
        "https://fanqienovel.com/reader/7538019528530199065 "
        "https://fanqienovel.com/reader/7538019879878656537"
    ),
    "reviewed_at": "2026-10-12",
    "confirmado": True,
})


REVIEWED.append({
    "video_id": "9oh1PCGsEEA",
    "title": "There's No Such Thing as a Bad Lady",
    "aliases": [
        "There Are No Bad Young Ladies in This World",
        "Noble Lady Reformation Guide",
    ],
    "evidence": (
        "Transcrição pública do vídeo lida diretamente na interface do YouTube "
        "em 13/10/2026 às 01:14 UTC: 0:17 apresenta Derek nas favelas de "
        "Ebblestein; 1:21 explica que plebeus chegam somente a duas estrelas "
        "de magia; 2:16 cita Kadia Flameheart; 3:20:22 cita House Duplane. "
        "A sinopse oficial do WEBTOON identifica Derek, mercenário e mago "
        "de segundo nível criado nas favelas de Ebelstein, contratado para "
        "ensinar Diella Duplain. A combinação de protagonista, cidade, "
        "limite mágico e família confirma a obra, além da pista em comentário. "
        "Grafias Ebblestein e Duplane vêm das legendas automáticas; a fonte "
        "oficial usa Ebelstein e Duplain. Canônico da edição oficial inglesa; "
        "ManhuaTop relaciona os dois aliases. Trechos efetivamente lidos na "
        "interface, sem exportação integral bem-sucedida, escuta independente "
        "do áudio ou comparação visual de painéis. "
        "https://www.youtube.com/watch?v=9oh1PCGsEEA&t=17s "
        "https://www.youtube.com/watch?v=9oh1PCGsEEA&t=81s "
        "https://www.youtube.com/watch?v=9oh1PCGsEEA&t=136s "
        "https://www.youtube.com/watch?v=9oh1PCGsEEA&t=12022s "
        "https://www.webtoons.com/en/fantasy/theres-no-such-thing-as-a-bad-lady/list?title_no=9716 "
        "https://manhuatop.org/manhua/there-are-no-bad-young-ladies-in-this-world/"
    ),
    "reviewed_at": "2026-10-12",
    "confirmado": True,
})


REVIEWED.append({
    "video_id": "eSzpxFfhbTA",
    "title": "I Have Been Stuck on the Same Day for 3,000 Years",
    "aliases": [
        "I've Been Stuck on This Day for Three Thousand Years",
        "I'm Trapped in This Day for Three Thousand Years",
        "I’ve Been Trapped on the Same Day for Over 3000 Years",
        "我困在这一天已三千年",
        "Wǒ Kùn Zài Zhè Yī Tiān Yǐ Sān Qiān Nián",
    ],
    "evidence": (
        "Transcrição pública do próprio vídeo lida na interface do YouTube "
        "em 13/10/2026 às 01:19 UTC: 0:00–0:58 apresenta três mil anos "
        "repetindo o mesmo dia, batalha contra um boss e despertar no quarto; "
        "1:07 nomeia Obsidian Ruins e o ovo do steel-winged colossus trazido "
        "para o quarto; 1:14 apresenta a irmã Lu Yao em cadeira de rodas; "
        "2:14–2:22 nomeia Shadow Worlds. A sinopse externa do MangaRead liga "
        "Obsidian Ruins, Shadow World, o ciclo de três mil anos e seu término "
        "após um boss à obra 我困在这一天已三千年. Essa combinação específica "
        "de cenário e sequência confirma a identificação; comentário de "
        "espectador é apenas apoio. Título em inglês e aliases conforme o "
        "catálogo MangaRead, sem edição inglesa oficial verificada. O catálogo "
        "usa Lu Feng, enquanto a legenda automática varia entre Lufang e "
        "Lu Fang; a grafia não foi critério principal. Identificação textual, "
        "sem correspondência visual verificada de frames ou painéis. "
        "https://www.youtube.com/watch?v=eSzpxFfhbTA&t=0s "
        "https://www.youtube.com/watch?v=eSzpxFfhbTA&t=67s "
        "https://www.youtube.com/watch?v=eSzpxFfhbTA&t=74s "
        "https://www.youtube.com/watch?v=eSzpxFfhbTA&t=134s "
        "https://www.mangaread.org/manga/i-have-been-stuck-on-the-same-day-for-3000-years/"
    ),
    "reviewed_at": "2026-10-12",
    "confirmado": True,
})


REVIEWED.append({
    "video_id": "UFuiCscincY",
    "title": "校花别追了，爷的深情你不配",
    "aliases": [
        "校花倒追我不要，我只爱小同桌",
        "School Belle, Stop Chasing Me — You Don’t Deserve My Love",
    ],
    "evidence": (
        "Novel chinesa de 榴莲味的西瓜, identificada como obra-base do recap, "
        "pelo título original vigente no catálogo oficial Fanqie. Transcrição "
        "pública do vídeo lida na interface do YouTube em 13/10/2026: "
        "0:15–2:33, acidente fatal a caminho do casamento da antiga paixão, "
        "visita ao túmulo com estrelas de papel, receio de desdobrá-las e "
        "não conseguir refazê-las, mensagens amorosas fixadas à lápide e "
        "espírito incapaz de abraçá-la; 3:27–4:45, clarão, retorno à aula "
        "em 22/09/2008, amigo com câmera para a 999ª declaração e desistência "
        "dela para preparar a carteira da aluna transferida. A sequência "
        "corresponde ao capítulo 1 reproduzido em WFXS e ao capítulo 2 "
        "oficial. Em 30:24–31:34, o representante esportivo Optimus bloqueia "
        "a passagem após a antiga paixão sair irritada, e o amigo diz que "
        "um bom cachorro não bloqueia o caminho: episódio do capítulo 7 "
        "oficial, com 秦天柱 (Qin Tianzhu). A confirmação combina cenas "
        "específicas e separadas, data exata e sequência, não só a premissa. "
        "O recap usa Xiao Yi, Wen Wan e Lu Yanran; o original, 叶林 (Ye Lin), "
        "兰呦呦 (Lan Youyou) e 凌飞雪 (Ling Feixue). A renomeação é inferida "
        "pelas cenas, sem alegar identidade fonética. Há divergência entre "
        "sinopses/edições quanto à morte da moça; esse detalhe isolado não "
        "sustenta a identificação. Alias chinês antigo atestado em catálogos; "
        "alias inglês atestado no catálogo/MTL WTR-LAB, sem edição inglesa "
        "oficial verificada. Não foi confirmado um quadrinho licenciado "
        "separado nem o título próprio da adaptação visual. Sem comparação "
        "de painéis, exportação integral da transcrição ou escuta independente. "
        "https://www.youtube.com/watch?v=UFuiCscincY&t=15s "
        "https://www.youtube.com/watch?v=UFuiCscincY&t=207s "
        "https://www.youtube.com/watch?v=UFuiCscincY&t=1824s "
        "https://fanqienovel.com/page/7288544802038090812 "
        "https://m.wfxs.tw/xiaoshuo/2572003/79911397/ "
        "https://fanqienovel.com/reader/7308405788995748402 "
        "https://fanqienovel.com/reader/7324010535731593790 "
        "https://ixdzs8.com/read/571505/ "
        "https://wtr-lab.com/en/novel/14138/school-belle-stop-chasing-me-you-dont-deserve-my-love"
    ),
    "reviewed_at": "2026-10-13",
    "confirmado": True,
})


REVIEWED.extend([
    {
        "video_id": "BTkZ47ABOP8",
        "title": "I Rely On My Harem To Conquer The World",
        "aliases": ["我靠后宫征服世界"],
        "evidence": (
            "Manhua identificado pela transcrição pública do vídeo, lida na interface "
            "do YouTube em 13/10/2026, e pelos painéis oficiais da WebNovel Comics "
            "inspecionados visualmente. Em 0:00–0:34, o ano 2050 corresponde à abertura "
            "do capítulo 1, Backstab; em 3:53–5:06, a serpente de quinto nível, a fuga "
            "da equipe e o capitão ferindo o carregador doente para usá-lo como isca "
            "correspondem ao Titanboa tier 5 e à referência a Beastblight nos painéis "
            "58, 69, 72 e 74 de 116. Em 5:46–6:39, a invocação pelas súcubos e a "
            "janela de status correspondem ao cartão Li Haoran, Blood Demon God, "
            "Bloodkin do painel 109/116. Em 6:56–7:03, a primeira seguidora possui "
            "88% de afeição, como Nicole, Succubus, favorability 88% no painel 4/82 "
            "do capítulo 2, I Drained The Succubus Village. Os números são contadores "
            "de imagens do leitor, não páginas impressas. Título inglês oficial da "
            "WebNovel; alias chinês atestado no AniList. Grafias variáveis na legenda "
            "automática não são aliases da obra. Confirmação por sequência específica "
            "e personagens; sem comparação direta da arte do recap, exportação integral "
            "da transcrição ou alegação de novel separada. "
            "https://www.youtube.com/watch?v=BTkZ47ABOP8&t=0s "
            "https://www.youtube.com/watch?v=BTkZ47ABOP8&t=233s "
            "https://www.youtube.com/watch?v=BTkZ47ABOP8&t=346s "
            "https://www.youtube.com/watch?v=BTkZ47ABOP8&t=416s "
            "https://www.webnovel.com/comic/33460735100887601 "
            "https://www.webnovel.com/comic/33460735100887601/92159213643552306 "
            "https://www.webnovel.com/comic/33460735100887601/92159214180423620 "
            "https://anilist.co/manga/192158/Wokao-Hougong-Zhengfu-Shijie"
        ),
        "reviewed_at": "2026-10-13",
        "confirmado": True,
    },
    {
        "video_id": "OHVNP0eLZuE",
        "title": "Living with an Aberrant Lifeform in My Body",
        "aliases": ["Strongest Parasitic Human", "寄宿我身，这个异生人不好惹！"],
        "evidence": (
            "Manhua identificado pela transcrição pública do vídeo, lida na interface "
            "do YouTube em 13/10/2026, e pela sequência de painéis oficiais do episódio "
            "1 da Tappytoon, inspecionados visualmente. Em 0:27–0:43, o protagonista "
            "ouve música de fones num trem lotado enquanto os demais passageiros estão "
            "exaustos; em 2:27–2:45, o agressor é caracterizado como criminoso de "
            "demolição; em 2:45–3:11, o protagonista vê uma menina com a avó, propõe "
            "distrair o monstro para elas fugirem e cita sua experiência na equipe "
            "universitária de atletismo. Essa sequência específica corresponde ao "
            "episódio 1, além da sinopse oficial sobre Lucas Qin e o ataque no metrô. "
            "Título inglês licenciado da Tappytoon; Strongest Parasitic Human é título "
            "de fãs atestado no Komikindo e RezoScan, e o original chinês está no "
            "MangaBaka e Komikindo. Qin Xi e Lucas Qin são formas documentadas nos "
            "catálogos; as variações da transcrição automática não são aliases da "
            "obra. O player ficou preto/em carregamento, portanto não houve comparação "
            "direta entre a arte do recap e os painéis. Não se afirma novel separada "
            "nem o capítulo final coberto pelo vídeo. "
            "https://www.youtube.com/watch?v=OHVNP0eLZuE&t=27s "
            "https://www.youtube.com/watch?v=OHVNP0eLZuE&t=147s "
            "https://www.youtube.com/watch?v=OHVNP0eLZuE&t=165s "
            "https://www.tappytoon.com/en/book/living-with-an-aberrant-lifeform-in-my-body "
            "https://www.tappytoon.com/en/chapters/339174933 "
            "https://mangabaka.org/manhua/94279/Living-with-an-Aberrant-Lifeform-in-My-Body "
            "https://komikindo.ch/komik/strongest-parasitic-human/ "
            "https://rezoscan.org/series/strongest-parasitic-human"
        ),
        "reviewed_at": "2026-10-13",
        "confirmado": True,
    },
])


REVIEWED.extend([{'video_id': 'yFeCAGnFqcQ',
  'title': 'My Slain Dragon Bride',
  'aliases': ['I Married the Dragon I Killed',
              'The Dragon I Killed Became My Bride',
              '내가 죽인 드래곤과 결혼했다'],
  'evidence': 'Manhwa identificado pela transcrição pública do vídeo, lida na interface do YouTube '
              'em 13/10/2026, e por painéis externos inspecionados visualmente. Em 0:22–0:40, a '
              'dragão entrega voluntariamente o coração, cuja ingestão revela seu sofrimento e '
              'motiva a regressão; a sinopse oficial da Naver confirma Valdrova entregando o '
              'coração para a ascensão ao nono círculo. Em 0:49–1:14, Ferda Rosnova recebe o '
              'decreto de noivado e precisa escolher entre exílio e a dragão, como no capítulo 1, '
              'imagem 2 do leitor Asura. Em 1:52:51–1:53:25, Luri recomenda atingir o quarto '
              'círculo, manda Ferda descansar e o parabeniza quando ele inesperadamente alcança o '
              'terceiro: sequência correspondente aos painéis finais do capítulo 18, imagem 17; a '
              'imagem 18 é o cartão final. Abertura e término sustentam o alcance aparente dos '
              'capítulos 1–18, sem alegar verificação de todos os painéis intermediários; a '
              'numeração da transcrição do YouTube não é a dos capítulos. Título e aliases '
              'ingleses atestados na descrição do uploader e no catálogo Asura, sem edição inglesa '
              'licenciada verificada; título original confirmado na Naver. Comparação de cenas '
              'narradas com painéis externos, sem alegar comparação direta da arte do recap. '
              'https://www.youtube.com/watch?v=yFeCAGnFqcQ&t=22s '
              'https://www.youtube.com/watch?v=yFeCAGnFqcQ&t=49s '
              'https://www.youtube.com/watch?v=yFeCAGnFqcQ&t=6771s '
              'https://asurascans.com/comics/my-slain-dragon-bride-1bb35e56 '
              'https://asurascans.com/comics/my-slain-dragon-bride-1bb35e56/chapter/1 '
              'https://asurascans.com/comics/my-slain-dragon-bride-1bb35e56/chapter/18 '
              'https://series.naver.com/comic/detail.series?productNo=14451876',
  'reviewed_at': '2026-10-13',
  'confirmado': True},
 {'video_id': '3s6gYhewIss',
  'title': 'Whispers of a Scheming Demon',
  'aliases': ["A Demon's Life From Day One",
              'Starting Life as a Baby Demon',
              'Starting My New Life as a Demon Kid',
              'Saekkibuteo Sijakaneun Angmasaenghwal',
              '새끼부터 시작하는 악마생활'],
  'evidence': 'Adaptação manhwa identificada pela transcrição pública do vídeo, lida na interface '
              'do YouTube em 13/10/2026. Em 1:44–3:08, moradores pedem a Gaff/Gaf que abandone o '
              'bebê meio-demônio no desfiladeiro da morte; o bebê reconhece o capitão dos '
              'mercenários Kandea, recorda sua filha desaparecida como futura Grande Bruxa e '
              'oferece encontrá-la para sobreviver. A sequência, personagens e barganha coincidem '
              'com Johan, Gaf e Ilea no capítulo 1 do romance-base, The Demon Whispers, lido '
              'diretamente em We Tried Translations. Em 4:25–4:58, o bebê resiste a um impulso '
              'cruel e oferece localização da filha em troca de proteção, com as almas em '
              'garantia; corroborado pelo conteúdo indexado do capítulo 2 do romance em Asura, não '
              'por leitura direta desse capítulo. Naver Webtoon, via resultado oficial indexado, '
              'identifica o original 새끼부터 시작하는 악마생활, Yohan e o mundo de Inmarok; a abertura direta '
              'não forneceu texto legível. Inglês e aliases são títulos de catálogo/scanlation '
              'atestados nas fontes abaixo, sem licença inglesa estabelecida. Variações fonéticas '
              'da legenda não são aliases. A descrição do uploader declara capítulos 1–10; o '
              'término não foi verificado independentemente. Capítulos 1 e 2 citados como prova '
              'são do romance, não limites da adaptação. Sem comparação de painéis do recap. '
              'https://www.youtube.com/watch?v=3s6gYhewIss&t=104s '
              'https://www.youtube.com/watch?v=3s6gYhewIss&t=265s '
              'https://wetriedtls.com/series/whispers-of-a-scheming-demon/chapter-1 '
              'https://asurascans.com/novels/whispers-of-a-scheming-demon/chapter/2 '
              'https://comic.naver.com/webtoon/list?mobile=y&titleId=854302 '
              'https://asurascans.com/comics/whispers-of-a-scheming-demon-1bb35e56 '
              'https://mistscans.com/series/a-demons-life-from-day-one/ '
              'https://lagoonscans.com/manga/starting-life-as-a-baby-demon/ '
              'https://roliascan.com/manga/starting-my-new-life-as-a-demon-kid/ '
              'https://anilist.co/manga/216731/Saekkibuteo-Sijakaneun-Angmasaenghwal',
  'reviewed_at': '2026-10-13',
  'confirmado': True},
 {'video_id': 'tDllG4mJ2Vk',
  'title': "Shut Up, Evil Dragon! I Don't Want to Raise a Child With You Anymore",
  'aliases': ['Shut Up, Malevolent Dragon! I Don’t Want to Have Any More Children With You',
              "Shut Up, Evil Dragon, I Don't Want to Raise a Child with You Anymore"],
  'evidence': 'Obra identificada pela transcrição pública do vídeo exato, lida na interface do '
              'YouTube em 13/10/2026 até 1:03:03, e por correspondência direta com o romance, '
              'volume 1, capítulo 43. Em 0:00–6:31, a rainha visita o caçador Leon Cosmo preso, '
              'prova seu sangue e ativa a maldição; ele desperta dois anos depois e conhece a '
              'filha Muen. Em 1:02:05–1:02:29, ela traz a avaliação de compatibilidade da academia '
              'para matrícula de Noah; a cor preferida dela é preto e a dele prata, e ambos dizem '
              'coincidência. Em 1:02:46, ela observa que ele acerta hábitos físicos e o conforto '
              'da cauda, mas erra pensamentos. O capítulo V1C43 lido integralmente em Etherreads '
              'reproduz a sequência, a finalidade do teste para Noia na St. Hys Academy e as '
              'respostas incomuns de Rosvitha e Leon. A confirmação se apoia em cenas específicas, '
              'além da premissa; grafias da legenda automática variam. Alias Malevolent Dragon '
              'atestado no capítulo e variante Evil Dragon/Raise a Child no resultado indexado de '
              'ReiManga, cuja abertura direta falhou. Sem frames ou comparação de painéis; trecho '
              'transcrito não cobre as seis horas integrais, e nenhum capítulo final do vídeo foi '
              'confirmado. https://www.youtube.com/watch?v=tDllG4mJ2Vk&t=0s '
              'https://www.youtube.com/watch?v=tDllG4mJ2Vk&t=3725s '
              'https://etherreads.com/shut-up-malevolent-dragon-i-dont-want-to-have-any-more-children-with-you-v1c43/ '
              'https://reimanga.net/manga/shut-up-evil-dragon-i-dont-want-to-raise-a-child-with-you-anymore-94813',
  'reviewed_at': '2026-10-13',
  'confirmado': True},
 {'video_id': 'TYc1WJ_xyH4',
  'title': 'The Unlimited Bacteriomancer',
  'aliases': ['The Infinite Bacteria Necromancer',
              'The Limitless Germ Necromancer',
              'Unlimited Bacteria Magician',
              '무제한의 세균술사'],
  'evidence': 'Manhwa identificado pela transcrição pública deste vídeo, lida na interface do '
              'YouTube em 13/10/2026, e por combinação de personagens e termos raros em glossário '
              'externo. Em 0:16–0:23, Kim Seyun elimina dez coelhos de três olhos; em 2:16–2:31, '
              'Ahmad Train supera o andar 57 e obtém um elixir; em 2:40–2:51, o protagonista '
              'desperta como necromante com traço EX de comandante de legião infinita. Em '
              '7:45–11:44, um funcionário exausto quebra uma placa de Petri e sua necromancia '
              'revive as bactérias; a cepa é transcrita Perpetuous Exomodulus em 9:18, 9:45 e '
              '11:44. Em 36:53–38:54, surge o golem de sangue e ouro de Avisenna. O glossário '
              'comunitário NovelList de 무제한의 세균술사 reúne Kim Sekyun, Ahmad Triain, Three-Eyed '
              'Rabbit, Infinite Legion Master, Perpetuus Exomodulus Strain, Avicenna e Bloodgold '
              'Golem. Os raros termos e a combinação específica sustentam a correspondência, com '
              'variações explícitas de transcrição; o glossário não é capítulo oficial. Página '
              'oficial Naver inspecionada no navegador confirma original coreano e necromancia '
              'microscópica; MangaBaka relaciona esse original a The Unlimited Bacteriomancer. '
              'Aliases ingleses atestados em ManhwaToNovel/MangaTown, sem licença inglesa '
              'verificada. Sem comparação de painéis nem capítulo numerado da adaptação '
              'confirmado; divisões da transcrição não são capítulos verificados do quadrinho. '
              'https://www.youtube.com/watch?v=TYc1WJ_xyH4&t=16s '
              'https://www.youtube.com/watch?v=TYc1WJ_xyH4&t=136s '
              'https://www.youtube.com/watch?v=TYc1WJ_xyH4&t=558s '
              'https://www.youtube.com/watch?v=TYc1WJ_xyH4&t=2213s '
              'https://www.novellist.co/novels/unlimited-bacteriologist/glossary '
              'https://series.naver.com/comic/detail.series?productNo=14539733 '
              'https://mangabaka.org/manhwa/602040/The-Unlimited-Bacteriomancer '
              'https://www.manhwatonovel.com/titulos/t/ '
              'https://m.mangatown.com/manga/unlimited_bacteria_magician',
  'reviewed_at': '2026-10-13',
  'confirmado': True}])


REVIEWED.append({'video_id': '_8LZIgTD8pM',
 'title': 'By Changing One Word in My Skills, I Broke Everything',
 'aliases': ['I Turn Skills Into Broken Ones With a Single Word', '技能改一个字，他们被我玩坏了'],
 'evidence': 'Manhua identificado pela transcrição pública deste vídeo, lida na interface do '
             'YouTube em 13/10/2026, por painéis externos do capítulo 1 e por combinação rara de '
             'personagem e mecanismo. Em 0:00–0:20, Jang Yan abre os olhos num ônibus com alunos '
             'concluintes e reconhece o dia do despertar, dois anos e meio antes da destruição da '
             'cidade. As imagens 1/16 e 2/16 do leitor Elf Toon, inspecionadas visualmente, exibem '
             'os títulos inglês/chinês, crédito de adaptação do romance homônimo e a abertura no '
             'ônibus de alunos de Nanrong no dia do despertar. Em 1:30–2:44, seu poder altera um '
             'caractere de nomes de habilidades/equipamentos, ele é explorado por poderosos, um '
             'monstro de nível 96 o mata e uma habilidade modificada produz renascimento. Em 4:12 '
             'e 5:06–5:14 desperta as duas profissões F, Repair Man e Farmer; em 5:43–6:05 explica '
             'a modificação e os efeitos do fazendeiro. A sinopse do manhua Elf Toon identifica '
             'Jiang Yan, exploração e regressão; a ficha MTL do romance-base no WTR-LAB confirma '
             'especificamente as duas profissões F, a alteração textual e o monstro de nível 96. A '
             'terminologia crescimento/ressurreição difere entre sinopse e narração, ressalva '
             'preservada. Alias inglês atestado nos resultados indexados de MangaTime e KomikLab, '
             'com aberturas diretas indisponíveis; título chinês consta da arte e da ficha do '
             'manhua. O título MTL da novel não foi adotado automaticamente como alias do '
             'quadrinho. Comparação da transcrição com painéis externos, sem frames reproduzíveis '
             'do recap ou escuta independente. Imagens citadas são contadores do leitor; não se '
             'afirma leitura integral do capítulo nem capítulo final do vídeo. '
             'https://www.youtube.com/watch?v=_8LZIgTD8pM&t=0s '
             'https://www.youtube.com/watch?v=_8LZIgTD8pM&t=130s '
             'https://www.youtube.com/watch?v=_8LZIgTD8pM&t=252s '
             'https://www.youtube.com/watch?v=_8LZIgTD8pM&t=306s '
             'https://www.youtube.com/watch?v=_8LZIgTD8pM&t=343s '
             'https://elftoon.net/series/comic/by-changing-one-word-in-my-skills-i-broke-everything '
             'https://elftoon.net/series/comic/by-changing-one-word-in-my-skills-i-broke-everything/chapter/1 '
             'https://wtr-lab.com/en/novel/75862/i-changed-one-word-in-the-skill-and-they-were-ruined-by-me '
             'https://mangatime.net/catalog/i-turn-skills-into-broken-ones-with-a-single-word/ '
             'https://komiklab.org/manga/i-turn-skills-into-broken-ones-with-a-single-word/',
 'reviewed_at': '2026-10-13',
 'confirmado': True})


REVIEWED.append({'video_id': 'rr9-Eh9QZNM',
 'title': 'Dungeon Gourmet',
 'aliases': ['Reincarnated as the Strongest Monster Eater: Revenge on the Tyrant Dragon', '던전 미식가'],
 'evidence': 'Manhwa identificado pela transcrição pública do vídeo exato, lida na interface do '
             'YouTube em 13/10/2026, e por painéis externos do capítulo 1 inspecionados '
             'visualmente. Em 0:23–0:50, um tanque de elmo e pequeno escudo segura o orc para seus '
             'companheiros o abaterem; o líder agradece. Em 0:50–1:19, ele corta um membro do orc, '
             'remove os pelos, drena o sangue, cozinha com especiarias e prepara macarrão cremoso '
             'enquanto o grupo demonstra repulsa. A sequência distintiva corresponde às imagens 3 '
             'e 4 do leitor MangaRead, capítulo 1: vanguarda de elmo/escudo, agradecimento a '
             'Maron, retirada dos pelos, sangue e especiarias, pedaços de carne e massa. Em 4:58, '
             'o protagonista se apresenta ao mercador; a legenda automática registra Marin Glades. '
             'A sinopse oficial da Tapas identifica Marron Glace, escudeiro de rosto coberto que '
             'só come monstros, e o título inglês licenciado Dungeon Gourmet. Original coreano '
             'atestado no catálogo oficial Kakao, disponível em resultado indexado; o catálogo '
             'EraScans relaciona o título inglês longo ao original e aos mesmos criadores. Grafias '
             'da transcrição são ressalvas, não aliases. Comparação da narração transcrita com '
             'painéis externos, sem reprodução visual verificável do recap. Imagens são contadores '
             'do leitor; não se afirma capítulo final coberto nem se confundem divisões da '
             'transcrição com capítulos da obra. https://www.youtube.com/watch?v=rr9-Eh9QZNM&t=23s '
             'https://www.youtube.com/watch?v=rr9-Eh9QZNM&t=50s '
             'https://www.youtube.com/watch?v=rr9-Eh9QZNM&t=298s '
             'https://www.mangaread.org/manga/reincarnated-as-the-strongest-monster-eater-revenge-on-the-tyrant-dragon/chapter-1/ '
             'https://tapas.io/series/dungeon-gourmet/info '
             'https://webtoon.kakao.com/content/%EB%8D%98%EC%A0%84-%EB%AF%B8%EC%8B%9D%EA%B0%80/4715 '
             'https://erascans.com/series/reincarnated-as-the-strongest-monster-eater-revenge-on-the-tyrant-dragon/',
 'reviewed_at': '2026-10-13',
 'confirmado': True})


REVIEWED.append({'video_id': 'xP18d9gnXR0',
 'title': '都觉醒恶魔法则了，你契约蚂蚁？',
 'aliases': [],
 'evidence': 'Romance chinês de 风动江湖 identificado pela transcrição pública deste vídeo, lida '
             'na interface do YouTube em 14/10/2026, e pelo capítulo 3 oficial da Fanqie, 第三章 '
             '意料之外，变态的融合特性. Em 0:45–1:11, o painel Roach Ant Queen descreve uma fera de nível '
             '1 e grau baixo, Super Breeding, descendentes que herdam todos os atributos '
             'maternos, reprodução multiplicada por dez, resistência cem vezes e força mil '
             'vezes a de criatura de mesmo tamanho, além de autocura. A combinação corresponde '
             'ao painel de 蜚蠊蚁后/超级生育 no capítulo 3. Em 1:26–1:52, o protagonista é '
             'ridicularizado na escola, chamado pelo professor ao escritório, recebe um '
             'formulário de retirada da escola e ouve que seus pais o confiaram ao professor '
             'antes de morrer. A mesma sequência encerra o capítulo 3 com 沈洛 e 刘军. A '
             'confirmação se apoia nessa combinação específica de mecânica e cena, não apenas '
             'na premissa de evolução de formigas. O recap adapta 沈洛 para Lucas Kane e o '
             'professor/guardião para Mr. Reed/Uncle Marcus; nomes de personagens não são '
             'aliases da obra. A página oficial confirma título e autor. A fonte personalizada '
             'do leitor produziu alguns glifos privados na extração acessível, mas o capítulo '
             'foi inspecionado no navegador e os mecanismos e cenas foram identificados. O '
             'recap comprime/altera detalhes iniciais; não se presume equivalência literal '
             'integral. Sem título inglês licenciado ou alias independente estabelecido, '
             'mantém-se o original chinês. Trata-se do romance-base; adaptação em quadrinhos '
             'separada não foi verificada. Sem reprodução visual verificável do recap, '
             'comparação de painéis ou capítulo final confirmado. '
             'https://www.youtube.com/watch?v=xP18d9gnXR0&t=45s '
             'https://www.youtube.com/watch?v=xP18d9gnXR0&t=86s '
             'https://fanqienovel.com/page/7517195003517488190 '
             'https://fanqienovel.com/reader/7517939929746263102',
 'reviewed_at': '2026-10-14',
 'confirmado': True})


REVIEWED.extend([{'video_id': '8jVw2r5RZt8',
  'title': 'Villain: Marrying a Blind Fiancée, Crazy in Love',
  'aliases': ['反派：迎娶盲人未婚妻，疯狂恩爱'],
  'evidence': 'Romance chinês de 牛头人战士 identificado pela transcrição pública em hindi deste '
              'vídeo, lida na interface do YouTube em 14/10/2026, e pelos capítulos oficiais '
              '1, 3 e 4 da Fanqie. Em 0:58–2:12, Gu Yan recebe o Universe Pure Love System e '
              'trata do casamento arranjado com a futura vilã cega Leng Qingqiu; em '
              "2:12–3:42, sua mãe Su Murong se surpreende com o abandono de Shen Wan'er. "
              'Sistema, personagens e telefonema correspondem ao capítulo 1; não se usa a '
              'reação posterior do pai como prova de leitura do capítulo 2. Em 6:12–8:29, o '
              'nervoso chefe da família Leng espera o cancelamento do noivado e Old Gao '
              'apresenta dois documentos, um preparado em Braille, como no capítulo 3. Em '
              '8:49–9:20, Gu Yan conduz a mão de Qingqiu até o documento, recebe um ponto de '
              'amor e a irmã protesta; em 10:17–11:20, oferece 5% da empresa avaliada em um '
              'trilhão, metade de seus 10%, e surpreende a família com a proposta. A ordem '
              'dessas cenas e os números correspondem ao capítulo 4. A legenda automática em '
              'hindi distorce algumas grafias; elas não são aliases. Título original e autor '
              'confirmados na editora. O título inglês é atestado em Novel Updates e '
              'NoBadNovel como título de tradução/catálogo, sem licença inglesa verificada; '
              'os campos N/A do índice não provam inexistência de licença. Original chinês é '
              'o único alias incluído. Identidade do romance-base confirmada; adaptação '
              'oficial em quadrinhos não estabelecida. O player permaneceu preto/carregando '
              'na tentativa de frame aos 8:21, portanto não se afirma comparação de arte, '
              'escuta independente nem capítulo final do vídeo. '
              'https://www.youtube.com/watch?v=8jVw2r5RZt8&t=58s '
              'https://www.youtube.com/watch?v=8jVw2r5RZt8&t=372s '
              'https://www.youtube.com/watch?v=8jVw2r5RZt8&t=529s '
              'https://www.youtube.com/watch?v=8jVw2r5RZt8&t=617s '
              'https://fanqienovel.com/page/7296670623839816740 '
              'https://fanqienovel.com/reader/7297073160984527399 '
              'https://fanqienovel.com/reader/7297247631397847586 '
              'https://fanqienovel.com/reader/7297248583034765824 '
              'https://www.novelupdates.com/series/villain-marrying-a-blind-fiancee-crazy-in-love/ '
              'https://www.nobadnovel.com/series/villain-marrying-a-blind-fiancee-crazy-in-love',
  'reviewed_at': '2026-10-14',
  'confirmado': True},
 {'video_id': 'yof-IrYDULw',
  'title': 'For Your Perfect Ending',
  'aliases': ['For Our Perfect Ending', '당신의 완벽한 엔딩을 위하여'],
  'evidence': 'Manhwa identificado pela transcrição pública deste vídeo, lida na interface '
              'do YouTube em 14/10/2026, pela sequência visual do episódio 1 oficial e pelos '
              'personagens da sinopse licenciada. Em 0:14–0:33, o príncipe ameaça a '
              'protagonista após capturar sua tentativa de fuga e a mata com uma espada; em '
              '0:38–1:14, ela desperta no quarto moderno com alarme às 7:45, um mês depois '
              'de retornar de vinte anos no mundo fictício. No episódio 1 da WEBTOON, '
              'inspecionado visualmente, o homem de uniforme preto com detalhes '
              'vermelhos/dourados e espada ensanguentada a repreende por ter sido capturada; '
              'a transição do ataque leva ao celular marcando exatamente 07:45. Essa '
              'sequência específica confirma a correspondência além da premissa. Em '
              '5:26–6:24, os colegas descrevem o popular e rico Lee Haewon; ela o reconhece '
              'como Killian Dell Winfred, seu assassino no romance. A sinopse oficial '
              'relaciona Sum/Ines, Killian e Haewon Lee. Variações fonéticas da legenda '
              'automática não são aliases. For Your Perfect Ending é o título inglês oficial '
              'licenciado na WEBTOON, de MaryHappy e Hedgebog. O original coreano é atestado '
              'na Naver; For Our Perfect Ending é variante de catálogo não oficial atestada '
              'em Kagane e Valir Scans. Comparação da transcrição com painéis externos '
              'oficiais, sem afirmar comparação de frames do recap, escuta independente ou '
              'capítulo final coberto pelo vídeo. '
              'https://www.youtube.com/watch?v=yof-IrYDULw&t=14s '
              'https://www.youtube.com/watch?v=yof-IrYDULw&t=38s '
              'https://www.youtube.com/watch?v=yof-IrYDULw&t=326s '
              'https://www.webtoons.com/en/romance/for-your-perfect-ending/list?title_no=9654 '
              'https://www.webtoons.com/en/romance/for-your-perfect-ending/episode-1/viewer?episode_no=1&title_no=9654 '
              'https://m.comic.naver.com/webtoon/list?titleId=843868&week=fri '
              'https://kagane.to/series/019c6b8e-5371-7be0-b607-716af30800d6 '
              'https://valirscans.org/series/comic/for-your-perfect-ending',
  'reviewed_at': '2026-10-14',
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
