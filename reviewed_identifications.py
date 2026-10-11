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
