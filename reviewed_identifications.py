Warning: truncated output (original token count: 102228)
Total output lines: 3005

"""Identificações revisadas: chave por vídeo, nunca pelo número de linha."""
import re

import confirmacao

REVIEWED = [
{"video_id":"oBoeJILi2wQ","title":"The Dragon Slayer's Regression on Another Level","aliases":["A Dragonslayer's Peerless Regression","용살자의 클래스가 다른 회귀"],"evidence":"Native transcript 00:00–00:39: Northern Phantom with severed arm, Zeke Draker named at 00:26, rejected by dragon-slayer family after failed aura Awakening. 01:13–01:52: dying after pursuit with ancient relic emperor wanted, regresses to age twelve in the Cradle training ground. This distinctive named protagonist and plot sequence matches official Tapas synopsis. Expanded description and pinned uploader comment name both English titles. Four Top comments inspected. Sources: https://www.youtube.com/watch?v=oBoeJILi2wQ&t=26s ; https://www.youtube.com/watch?v=oBoeJILi2wQ&lc=UgxiUZvCDos3qkf5rwZ4AaABAg ; https://tapas.io/series/the-dragon-slayers-regression-on-another-level/info ; https://onisaga.com/title/a-dragonslayers-peerless-regression . Official Tapas page opened and read; alternate-title catalog from search. Transcript samples, not full-video viewing, visual panel comparison or exact chapter matching.","reviewed_at":"2026-11-12","confirmado":True},
{"video_id":"8ebyZsGjLls","title":"Cyberpunk Chivalry","aliases":["Cyberpunk Swordsman","사이버펑크 협객전"],"evidence":"Native transcript: 00:07 Kunlun immortal dies after revenge; 02:05 awakens as robot Ash; 02:44 repairer Akina Greenwood; 02:52 scrapyard workshop; 04:34–05:31 mechanical body lacks dantian and electricity replaces internal energy. Specific characters and sequence match official Naver synopsis of 사이버펑크 협객전 (Ash/애쉬, Akina/아키나, scrapyard, electricity martial arts). Expanded description names Cyberpunk Chivalry; 0 comments displayed. English title/alias from secondary catalog, no official English edition claimed. Sources: https://www.youtube.com/watch?v=8ebyZsGjLls&t=125s ; https://series.naver.com/comic/detail.series?productNo=14780774 ; https://mangakatana.com/manga/cyberpunk-chivalry.27954 . Transcript samples, not full-video viewing or panel comparison.","reviewed_at":"2026-11-12","confirmado":True},
{'video_id': 'Q94sgDJqDoM', 'title': 'My Healing Skill Can Copy Anything, So I Conquered the Abyss', 'aliases': ['I Can Copy Anything with Healing Magic, So I’m Farming the Abyss', '治疗术复制一切，我刷爆了深渊'], 'evidence': 'Full description checked; generic promotional text only. Actual public viewer comment UgwuCOZUOpGhL43UPpt4AaABAg explicitly names this work, and YouTube marks it Pinned by @stilesmanhwafresh (comment author is not the creator). Independent viewer comments UgwWu2sFn8jGJX_H2Gx4AaABAg and UgxAi02LjZNzkn97Q694AaABAg discuss healing to gain skills and class emblems being stolen before bonding, corroborating the copy-through-healing and stolen rare class premise. External catalogs identify Lin Ye, SSS Healing Master, regression and copied talents. Sources: https://www.youtube.com/watch?v=Q94sgDJqDoM&lc=UgwuCOZUOpGhL43UPpt4AaABAg; https://www.youtube.com/watch?v=Q94sgDJqDoM&lc=UgwWu2sFn8jGJX_H2Gx4AaABAg; https://komik62.com/comics/my-healing-skill-can-copy-anything-so-i-conquered-the-abyss; https://atsu.moe/manga/9NRt . No opening frames or reverse image search performed; playback requires sign-in. Confirmation is from creator-pinned explicit identification plus specific corroborating mechanics.', 'reviewed_at': '2026-11-04', 'confirmado': True},
{"video_id":"ucqLUqvJrVA","title":"The Glutton: Devourer of Kings","aliases":["Return of the Devourer"],"evidence":"Actual exact-video comments explicitly name The Glutton and Return of the Devourer. Deeper comments independently mention character Leo at2:08:57/58 and Wrath; external chapter33,39,41 and45 references corroborate Leo and Wrath in this series, in addition to official WEBTOON title. Not directly viewed video frames. Sources: https://www.youtube.com/watch?v=ucqLUqvJrVA&lc=Ugx-0OEzAMyZbl8QUlJ4AaABAg; https://www.youtube.com/watch?v=ucqLUqvJrVA&lc=Ugz_f-Maa0eYdL-iSZV4AaABAg.AcdgnPGylzNAce-bIV8SfT; https://www.webtoons.com/en/action/the-glutton-devourer-of-kings/list?page=1&title_no=9786; https://www.reddit.com/r/manhwa/comments/1u32gk6/anyone_know_the_sauce/ Specific character matches: {\"video_comments\": [{\"id\": \"UgwZc6FA9PtINdVFO3R4AaABAg\", \"text\": \"2:08:57😂leo flipped him off\"}, {\"id\": \"Ugzk-XogzISReChzmWR4AaABAg\", \"text\": \"Leo flip him of 😂 2:08:58\"}, {\"id\": \"Ugw4dSUiLfVOGIO1vyV4AaABAg\", \"text\": \"Why does the wrath looks like beru the ant king from solo leveling?\"}], \"source_matches\": [\"https://manga-oni.com/manhua/el-devorador chapter33 named Leo transforms; synopsis SiChen regression10years\", \"https://zolotube.com/watch?v=8jHFfk3CFsE explicit Return of the Devourer/The Glutton chapters1-50 description chapter33 Leo protects SiYun, chapter39 Preparing for Wrath, chapter41 Leo joins dungeon team\", \"https://poseidon-scans.net/serie/return-of-the-devourer/chapter/45 reader discussion Leo and lightning fox companion\"]}","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"rWRnvZt4QGw","title":"The End Has Come","aliases":["The Apocalypse Is Here","종말이 찾아왔다"],"evidence":"[{\"url\": \"https://www.youtube.com/watch?v=rWRnvZt4QGw&lc=UgxpAnmlBaCqdqC4o-14AaABAg.AchMktzkr7tAcj_voAHbjS\", \"type\": \"public_comment_reply\", \"author\": \"@noahjeon-m5b\", \"text\": \"종말이 찾아왔다\", \"context\": \"Reply to Name of the Manhwa?\"}, {\"url\": \"https://www.youtube.com/watch?v=rWRnvZt4QGw&lc=UgxPV_IrYiCTNqBL8ap4AaABAg\", \"type\": \"public_comment\", \"text\": \"David casually unlocking the ability to speak and understand Korean😭🙏🥀\"}, {\"url\": \"https://namu.moe/w/종말이%20찾아왔다\", \"type\": \"external_character_match\", \"finding\": \"David Briggs (데이비드 브릭스) is an American sergeant who cannot speak Korean; Yena translates for him. Specific match to viewer remark about David speaking Korean.\"}, {\"url\": \"https://www.webtoons.com/en/thriller/the-end-has-come/list?title_no=8421\", \"type\": \"official_english_title\", \"finding\": \"The End Has Come, SW Jeon. Bullied Minjun and classmate Yena survive zombie outbreak.\"}, {\"url\": \"https://series.naver.com/comic/detail.series?productNo=12424386\", \"type\": \"official_korean_title\", \"finding\": \"종말이 찾아왔다, 전선욱. Jeong Minjun and Han Yena zombie survival.\"}, {\"url\": \"https://genztoons.org/series/the-apocalypse-is-here/\", \"type\": \"alias\", \"finding\": \"The Apocalypse Is Here, alternative 종말이 찾아왔다\"}] No video frames inspected. Confirmation uses direct exact-title public reply plus independent character-specific detail and official catalog matches.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"ZzA_QrlySzU","title":"The Swordsmanship Family’s Butler Was the Heroic Emperor","aliases":["The Butler of the Swordmaster Family Was the Hero Emperor","剣術名家の執事は英雄皇だった"],"evidence":"Multiple actual public target comments name same work; reply gives alternate title and coverage1-28. Target title butler/swordsmanship-family and viewer discussion betrayal killer already dead by reincarnation fit source Crowley betrayed by Raphael and reborn200 years later as slave Faris tutoring Rimuru. Sources: https://www.youtube.com/watch?v=ZzA_QrlySzU&lc=UgzpIAmVG7FYYtpnTw14AaABAg; https://www.youtube.com/watch?v=ZzA_QrlySzU&lc=UgzpIAmVG7FYYtpnTw14AaABAg.Acf72Rhrb04AcmI8DLv3bO; https://en-thunderscans.com/comics/the-swordsmanship-familys-butler-was-the-heroic-emperor/; https://wurmz.net/detail/manga/sang-butler-keluarga-ahli-pedang-adalah-kaisar-pahlawan No video frames verified; chapter coverage reported by commenter, not independently checked.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"0vtHQxQ1Hag","title":"末世天灾：从打造避难所开始","aliases":["Apocalyptic Disasters: Starting by Building a Shelter"],"evidence":"Identificado por descrição integral e sequência específica dos capítulos 1 e 3. O recap localiza Su Wu/Jianghe como Kade Walker/Riverford. Romance original de 夏天的葡萄; não inferir título da adaptação separado. Evidence: [{\"url\": \"https://www.youtube.com/watch?v=0vtHQxQ1Hag\", \"location\": \"full video description\", \"match\": \"Kade Walker arrives in parallel world, sells apartment, moves inland Riverford, buys scrap; survival points upgrade tools into engineering robots, drilling machinery and geothermal generator. Names localized by recap.\"}, {\"url\": \"https://www.biquge321.com/zhangjie/024424/502751095.html\", \"location\": \"chapter 1\", \"match\": \"Su Wu sells inherited coastal apartment, moves inland Jianghe city, buys 3000 tonnes scrap metal for six million; apocalypse survival points upgrade mechanical arms to build engineering robot.\"}, {\"url\": \"https://www.biquge321.com/zhangjie/024424/602351095.html\", \"location\": \"chapter 3\", \"match\": \"Engineering robot, 10km drilling upgrade and 300kW geothermal generator assembled with survival points; distinctive technical sequence matches description.\"}, {\"url\": \"https://shanghaifantasy.com/novel/apocalyptic-disasters-starting-by-building-a-shelter/\", \"location\": \"title, raw title and synopsis\", \"match\": \"English alias explicitly mapped to Chinese raw title and author Summer Grapes; Su Wu, apocalypse survival system, upgrading technology, underground shelter.\"}] No scene timestamps or full chapter coverage established.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"odfuzkICaOo","title":"史前生物哪家强？恐怖直立猿称王","aliases":[],"evidence":"Descrição corresponde à sequência específica de Earth Online, observador nacional, 始祖地猿 e adaptação dos ombros para arremesso. Romance de 七七霖; protagonista Yang Chen, renomeado Ethan Dawson no recap. Sem alias inglês comprovado. Evidence: [{\"url\": \"https://www.youtube.com/watch?v=odfuzkICaOo\", \"location\": \"full description\", \"match\": \"Ethan Dawson as national Civilization Observer in Earth Online chooses Ancestral Ground Ape; other world lacks evolution theory. Intervention changes shoulders/collarbones/tendons to enable rock throwing against sabertooth cats, switching diet from fruit to meat.\"}, {\"url\": \"https://www.xs.cn/bookquery/pelwgtkgdydy\", \"location\": \"synopsis and chapter index\", \"match\": \"Yang Chen chosen by Earth Online as civilization observer; world lacks evolution theory. Chapter5 Ancestral Ground Ape; chapter17 Throwing; chapter18 shoulder modification/biological slingshot; chapter19 rocks; chapter21 sabertooth submission; chapter23 fruit to meat.\"}, {\"url\": \"https://www.xxsy.net/bookquery/pelwgtrhxaen\", \"location\": \"chapter index\", \"match\": \"Same distinctive chapter sequence including 17 Throwing,18 Shoulder Modification Biological Slingshot,21 Sabertooth,23 From Fruit to Meat.\"}] No scene timestamps or full chapter coverage established.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"aZEMPQcUw2M","title":"The Return of the Scorned Genius","aliases":["I Came From the Abyss","深淵の主～蔑まれた天才の帰還～"],"evidence":"Nome informado pelo próprio canal em resposta de comentário. Não usar apenas Lord of the Abyss, sugestão corrigida pelo criador. Descrição pública não continha nome. Evidence: [{\"url\": \"https://www.youtube.com/watch?v=aZEMPQcUw2M&lc=UgzBwrSqRVcKgsKxFeJ4AaABAg.AckkErsLtGMAclBtEQUbPD\", \"location\": \"creator comment reply\", \"match\": \"Verified channel @MrManhwas01, isCreator=true, explicitly answers The Return of the Scorned Genius. Another commenter suggested Lord of the Abyss, rejected then corrected by creator.\"}, {\"url\": \"https://mangak.io/the-return-of-the-scorned-genius\", \"location\": \"title, alternate Japanese title, synopsis\", \"match\": \"Chiyuan Suou former genius with resonance over100%, wheelchair three years, awakening Lord of Abyss summoner class and searching for vanished father.\"}, {\"url\": \"https://hwa.so/series/the-return-of-the-scorned-genius-mu-27517739708\", \"location\": \"alternate titles and English edition record\", \"match\": \"Maps title to I Came From the Abyss and Japanese alias, official English protagonist Dylan Zhou, talent sealed13yo, awakens Lord of Abyss16yo.\"}] No scene timestamps or full chapter coverage established.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"UE1v2V3iMLc","title":"Reborn As A Big Mouth Flower","aliases":["Infinite Devouring Flower","Devour It, Chomper","吞噬吧大嘴花"],"evidence":"Nome informado pelo próprio canal em resposta de comentário; aliases sustentados por catálogo externo. Descrição pública não continha nome. Evidence: [{\"url\": \"https://www.youtube.com/watch?v=UE1v2V3iMLc&lc=UgxhV0xsrk7UiAwcoSJ4AaABAg.AchMPVFGxRKAchkGUXA_OW\", \"location\": \"creator comment reply\", \"match\": \"Verified channel @MrManhwas01, isCreator=true, explicitly answers Reborn As A Big Mouth Flower.\"}, {\"url\": \"https://manhwatop.com/manga/reborn-as-a-big-mouth-flower/\", \"location\": \"aliases and synopsis\", \"match\": \"Aliases and plot: high school boy reborn as chomper, Flower system absorbs traits of plants to evolve into Giant Continent guardian; matches flower reincarnation/evolution video.\"}, {\"url\": \"https://dragontea.ink/novel/reborn-as-a-big-mouth-flower/\", \"location\": \"synopsis\", \"match\": \"High school teenager reborn big-mouthed flower, other plants assimilated by Flower system; threatened by monsters and hunters.\"}] No scene timestamps or full chapter coverage established.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"RmDVez05OOU","title":"I Became a Transcendent-Class Hunter with 100,000x EXP","aliases":["I Became a Transcendent-Class Hunter with 100,000x Experience"],"evidence":"Identified from comments on the exact video ID, corroborated against linked series source. Exact target title20-year regression and100000x growth; two name comments. Comments: https://www.youtube.com/watch?v=RmDVez05OOU&lc=Ugz5ciDSz-GL8tfLT2V4AaABAg; https://www.youtube.com/watch?v=RmDVez05OOU&lc=UgyaudCpUw8loW7N9ER4AaABAg External: https://www.novelupdates.com/series/i-became-a-transcendent-class-hunter-with-100000x-experience/. Direct frames/transcript not verified; no unsupported chapter coverage claim. Naming comments are ordinary viewers, not asserted uploader comments. Sources corroborate series identity; chapter count and timestamps are reported comments, not independent coverage verification.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"CK-Gc-V_RzU","title":"The Pharmaceutical Chairman Is a Poison Master","aliases":["제약회사 회장님은 절대독마"],"evidence":"Identified from comments on the exact video ID, corroborated against linked series source. Named comment; other exact-video comments discuss poison martial artist and immortals in afterlife. Comments: https://www.youtube.com/watch?v=CK-Gc-V_RzU&lc=UgyL8KhH2alUV3yGetp4AaABAg External: https://en-thunderscans.com/comics/the-pharmaceutical-chairman-is-a-poison-master/. Direct frames/transcript not verified; no unsupported chapter coverage claim. Naming comments are ordinary viewers, not asserted uploader comments. Sources corroborate series identity; chapter count and timestamps are reported comments, not independent coverage verification.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"z4PVlBgZvfU","title":"The Rebel of the Tyrant Noble House","aliases":["The Rebel of the Tyrant Noble House — Aster"],"evidence":"Identified from comments on the exact video ID, corroborated against linked series source. Named comment; target adopted child plot, duke betrayal at15:10 and wing-power comments match Ash/Seven Wings. Comments: https://www.youtube.com/watch?v=z4PVlBgZvfU&lc=Ugwv0Ntb5p4z_1MHdRx4AaABAg External: https://www.topmanhua.fan/manhua/the-rebel-of-the-tyrant-noble-house-aster. Direct frames/transcript not verified; no unsupported chapter coverage claim. Naming comments are ordinary viewers, not asserted uploader comments. Sources corroborate series identity; chapter count and timestamps are reported comments, not independent coverage verification.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"WXOfjib598Q","title":"SSS Grade Saint Knight","aliases":["SSS Rank Saint Knight"],"evidence":"Identified from comments on the exact video ID, corroborated against linked series source. Two naming comments and hidden SSS-class premise. Comments: https://www.youtube.com/watch?v=WXOfjib598Q&lc=Ugx0pEgnRY5tnVSB0aJ4AaABAg; https://www.youtube.com/watch?v=WXOfjib598Q&lc=UgzwBXBAuPwNo9vZanV4AaABAg External: https://www.novelupdates.com/series/sss-grade-saint-knight/. Direct frames/transcript not verified; no unsupported chapter coverage claim. Naming comments are ordinary viewers, not asserted uploader comments. Sources corroborate series identity; chapter count and timestamps are reported comments, not independent coverage verification. Comments at57:45 reference a Pokeball, at1:59:59 a sister, plus wolf mount/pup. External series discussion explicitly locates Beast Ball in chapter17: https://www.reddit.com/r/manhwarecommendations/comments/1s7fjyx/did_they_just_copy_and_paste_this_into_the_manhwa/ . Novel synopsis identifies Zhou Yi, hidden Saint Knight and buff system: https://fullchapters.com/sss-grade-saint-knight/ . No direct panel comparison.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"mFhNWS4mRNY","title":"Sandmancer of the Scorched Desert","aliases":["Sand Mage of the Scorched Desert","Sand Mage of the Burnt Desert","불탄 사막의 모래술사"],"evidence":"Identified from comments on the exact video ID, corroborated against linked series source. Direct reply names series; sand mage target title and33chapter comment correspond to Zeon series. Comments: https://www.youtube.com/watch?v=mFhNWS4mRNY&lc=UgxyaOpPuFbzdaSreVd4AaABAg.Acaw0TUhnCSAcbDbuMTn2a External: https://en-thunderscans.com/comics/sand-mage-of-the-scorched-desert/. Direct frames/transcript not verified; no unsupported chapter coverage claim. Naming comments are ordinary viewers, not asserted uploader comments. Sources corroborate series identity; chapter count and timestamps are reported comments, not independent coverage verification.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"HL_c7nLOSCI","title":"The Perfect Curse","aliases":["A Bad Example of a Perfect Curse"],"evidence":"Comentário público @erangik de 31/10/2026 no HTML do vídeo exato informa 'Name - Bad Example of a Perfect Curse'. Título promocional do vídeo descreve mulher disfarçada de cavaleiro e duque amaldiçoado. Manta oficial confirma Adrina vivendo como o irmão gêmeo morto e protegendo Duke Julius, que aparenta ser criança; ComicK liga explicitamente o alias ao título oficial The Perfect Curse e à mesma sinopse. Comentário não é do uploader e não foi tratado sozinho como prova: corroborado pela combinação específica e fonte oficial. Nenhum timestamp ou cobertura de capítulos alegado; contagem de capítulos do comentário não verificada. https://www.youtube.com/watch?v=HL_c7nLOSCI https://manta.net/en/series/the-perfect-curse?seriesId=3884 https://comick.dev/comic/a-bad-example-of-a-perfect-curse","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"NLkYn5Jun5w","title":"Monsters (2022)","aliases":["Global Invasion: I Was Hunted by the Demons and Became a God"],"evidence":"Descrição completa extraída do HTML público do vídeo de ID exato em 04/11/2026 informa explicitamente 'Manhwa Name: Monsters (2022) / Global Invasion: I Was Hunted by the Demons and Became a God'. Catálogo MangaTime associa ambos os nomes à mesma obra de High Ground/Dream Factory Studio, com Naro e invasão de criaturas numa cidade moderna. Ligação vídeo-obra confirmada pela identificação explícita do uploader, não inferida do título promocional. Fonte externa via índice de busca; abertura direta retornou Cache miss. Sem alegar cenas assistidas, timestamps ou capítulos cobertos. https://www.youtube.com/watch?v=NLkYn5Jun5w https://mangatime.net/catalog/monsters/","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"jUD5Hrg3TVY","title":"Helmut: The Forsaken Child","aliases":["Helmut"],"evidence":"Descrição do vídeo identifica explicitamente 'Manhwa Name: Helmut: The Forsaken Child', conforme captura de tela fornecida pelo usuário para o URL exato e inspecionada em 04/11/2026. O título oficial inglês Helmut e o protagonista homônimo são corroborados pela editora Tapas: bebê abandonado na Forest of Pahe, criado por uma fera mágica e um espadachim exilado, com uma dark seed. A confirmação do vínculo com o vídeo é a identificação explícita na descrição mostrada pelo usuário; não foi assistida uma cena nem alegado timestamp ou capítulo coberto. Fonte do vídeo: https://www.youtube.com/watch?v=jUD5Hrg3TVY . Fonte oficial da obra/alias: https://tapas.io/series/helmut/info .","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"wqoUI0tbBiQ","title":"女神今晚留下来","aliases":[],"evidence":"Identificação confirmada por correspondência narrativa específica, não pelo título promocional. A página espelho do ID exato wqoUI0tbBiQ em Zolotube identifica o canal Gave e publicação em 31/10/2026, e descreve Hellen levado por Zeus do Monte Ida ao Olimpo; Hera o considera filho ilegítimo de Zeus; ele ganha tempo contando One Thousand and One Nights e interrompendo a narrativa em suspense; Pandora é sua avó e Eris participa do enredo. O catálogo oficial de listas de leitura do Qidian atribui 女神今晚留下来 a 紫夜弦歌 e nomeia o protagonista 希伦, levado por Zeus ao Olimpo. O capítulo 3 da obra, 恶堕，了解一下？, confirma a combinação rara: 希伦 conta a Hera histórias de 天方夜谭/一千零一夜, interrompe antes do desfecho, e recebe mais tempo para viver/investigar. O título/autor do capítulo são corroborados pelo índice da obra. Descrição sem timestamps; não foi obtida transcrição do vídeo. Não foi estabelecido um título inglês oficial nem aliases independentes. https://zolotube.com/watch?v=wqoUI0tbBiQ https://zolotube.com/channel?id=UCQn6wzk1TibcW1kZHpmkK9w https://book.qidian.com/booklist/detail/655415/ https://www.biquge151.com/chapter/61376129/007015412.html https://www.biquge151.com/book/61376129/","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"ATRF93qjSn0","title":"Peaceful Camping Life in Another World","aliases":["Healing Life Through Camping in Another World","이세계 캠핑으로 힐링 라이프"],"evidence":"Identificação pela descrição indexada do vídeo de ID exato em https://zolotube.com/watch?v=ATRF93qjSn0: descrição identifica Chef Kanghyun e informa Part 1 00:00:00, Part 2 02:13:04; título descreve acampamento em outro mundo e comida atraindo elfos e monstros. Fonte oficial WEBTOON identifica Lee Kanghyun (Ganghyeon Lee na edição inglesa), chef que acampa em outro mundo e atrai habitantes com sua comida. Correspondência específica de personagem, profissão e premissa, não apenas duração ou título promocional. Oficial: https://m.webtoons.com/id/fantasy/peaceful-camping-life-in-another-world/list?title_no=7428 e https://m.webtoons.com/en/fantasy/peaceful-camping-life-in-another-world/list?title_no=6674. Alias inglês e coreano corroborados em https://mangakatana.com/manga/healing-life-through-camping-in-another-world.27303. Descrição acessível pelo índice de busca; abertura direta do espelho e YouTube retornou Cache miss. Timestamps são marcadores de partes da descrição, não cenas assistidas; não houve transcrição ou comparação visual.","reviewed_at":"2026-11-04","confirmado":True},
{"video_id":"3qlDmanLZBM","title":"Zombie Apocalypse, I Died Right at the Start","aliases":["丧尸末日，我开局即死","丧尸吃人，我吃丧尸"],"evidence":"Identificação pela narrativa preservada do vídeo, não por novo acesso: YouTube 31:19–31:39 mostra Simon/Su Shen com poder de lealdade, líder a 100% e pontuações de Skye/Lily. A sequência chinesa correspondente em Dailymotion 53:00–54:28 identifica Ji Chuan, Su Shen, Gu Yunxi e Lin Lulu. O capítulo 26 (可怕的忠诚) de 丧尸吃人，我吃丧尸, autor 罪恶原始袋, corresponde especificamente: habilidade 忠诚; Gu Yunxi/Lin Lulu inicialmente 75, novatos 20, após combate 70; transferência pela mão e lealdade do usuário ao líder 100%, seguida de pontuações individuais 87/80. Texto do capítulo disponível no índice de busca; abertura direta expirou. NovelUpdates e WTR-LAB atestam título inglês/chinês, mesmo autor e Ji Chuan traído por Su Wanwan/Liu Hao na própria vila, transformação em zumbi consciente e consumo de núcleos, correspondentes à abertura preservada 00:00–03:44. Nomes ingleses do recap são localizados; grafias chinesas anteriores eram ASR. https://www.youtube.com/watch?v=3qlDmanLZBM&t=1879s https://www.dailymotion.com/video/x9xf3o2 https://m.shuhaige.net/374060/129147090.html https://m.shuhaige.net/shu_374060.html https://www.novelupdates.com/series/zombie-apocalypse-i-died-right-at-the-start/ https://wtr-lab.com/en/novel/12255/zombie-apocalypse-i-died-right-at-the-start","reviewed_at":"2026-11-03","confirmado":True},
{'video_id': 'hBOCjqTS_28', 'title': 'The Level 1 Hunter with Infinite Titles', 'aliases': ['無限称号のレベル1ハンター'], 'evidence': 'Transcrição nativa pública: 00:18 Kotake Takeru passou dez anos no nível 1; 02:19–03:17 ganho microscópico de XP ao caçar goblins; 03:40 chefe inesperado Goblin Warrior; 00:00 título Weakest Hero ativa todos os títulos. A publicação oficial Kakao Piccoma identifica 神武 猛 (こうたけ たける), ganho de 1/100000 de XP, dez anos caçando goblins, chefe inesperado, XP máximo sem subir de nível e título 最弱の英雄 que mantém todos os títulos ativos. Título inglês atestado em Thunderscans; japonês na fonte oficial. Não houve comparação visual de capítulo; Arai, dívida de 400 milhões e Goblin Predator observados no vídeo mas não usados como confirmação independente. Piccoma direto restrito ao Japão; não contornado. https://www.youtube.com/watch?v=hBOCjqTS_28&t=18s https://www.youtube.com/watch?v=hBOCjqTS_28&t=220s https://prtimes.jp/main/html/rd/p/000000964.000003707.html https://en-thunderscans.com/comics/the-level-1-hunter-with-infinite-titles/', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'tH8qKW4qoXU', 'title': '我的学习群里全是真大佬', 'aliases': [], 'evidence': '{"video_url": "https://www.youtube.com/watch?v=tH8qKW4qoXU", "video_evidence_location": "Expanded video description, observed 2026-10-29T04:21:09Z; no transcript available and no timestamp claimed", "specific_matches": ["Senior student joins Azure Dragon Study Group / 青龙学习小组 hoping to improve grades, initially believes members are roleplayers.", "Same group scientists Newton, Galileo, Gauss, Faraday and Einstein.", "Newton rewards the protagonist with Focus / 专注力+1 after receiving modern scientific advice. Publisher chapter 1 explicitly shows a one-hour reward and the realization that members are real historical scientists."], "sources": [{"url": "https://www.hongxiu.com/bookquery/pehvrhjdenur", "chapter": "第1章 牛顿的感谢", "observed_at": "2026-10-29T04:23:48Z", "access": "Cloud browser loaded full chapter and publisher title/author; earlier web fetch returned403"}, {"url": "https://www.qidian.com/chapter/1047956575/885879589/", "chapter": "第1章 牛顿的感谢", "access": "Official chapter link observed on Hongxiu; not separately opened"}], "name_difference": "YouTube description localizes protagonist as Leo Dawson; publisher uses 李东. Confirmation rests on specific group/mechanism/character matches, not protagonist name."}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': 'C6w4nCR7Zc8', 'title': 'Outrageous! I Opened a Training Class for Empresses', 'aliases': ['Lipu! Wo Kaile Nvdi Peixun Ban', '离谱！我开了女帝培训班', '离谱！我真没想开女帝培训班！'], 'evidence': '{"video_url": "https://www.youtube.com/watch?v=C6w4nCR7Zc8", "evidence": [{"source": "native YouTube Show transcript DOM", "timestamps": {"00:00–00:34": "cultivator dream, tribulation and evil spirit, wakes at9", "00:43": "Lu Li is ordinary teacher running late", "01:00–03:03": "pregnant hostage in bank, LuLi throws stone severing robber arm", "04:35–04:51": "female disciple Yiqing, Shadow Alliance assassin leader", "05:00–05:17": "JiangLu richest woman, offers20billion to acquire Wen family", "05:24–05:40": "miracle doctor HuaYou, teacher LuLi calls"}}, {"url": "https://manhuatop.org/manhua/outrageous-i-opened-a-training-class-for-empresses-series/", "match": "synopsis explicitly identifies amnesiac teacher LuLi and three female students: killer queen, medical queen, business queen; ancient immortal identity. Specific name plus three distinct occupations match native transcript.", "aliases_verified": true}, {"url": "https://www.rumanhua.org/news/510383", "match": "Chinese title and synopsis name 陆离, amnesiac teacher with three female students in same three professions; author七兔漫画;chapter1小事情，放着老师来 and chapter2您的补习班老师来电", "chapter_panels_inspected": false}]}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': 'cFzt9WsrKrY', 'title': 'I Am Really Not the Son of Providence', 'aliases': ['I Am Really Not a Child of Luck', "I'm Not the Son of Luck", 'Wo Zhen De Bushi Qi Yun Zhi Zi', '我真的不是气运之子'], 'evidence': '{"youtube_url": "https://www.youtube.com/watch?v=cFzt9WsrKrY", "evidence": [{"source": "YouTube native Show transcript (cloud browser tab 2)", "url": "https://www.youtube.com/watch?v=cFzt9WsrKrY&t=29s", "timestamp": "00:29–00:52", "observations": "Shen Tian (ASR varies Shanten/Shentenne) has mother Lanfe dying of dystocia; firebird drowns in imperial garden; valuable plant uprooted by child; academy destroyed.", "external_url": "https://novelfull.com/i-am-really-not-the-son-of-providence/chapter-1-i-must-be-a-fake-mc.html", "external_chapter": 1, "match": "Shen Tian/Concubine Lan, fatal childbirth, drowned Flaming Bird, uprooted Purple Epiphyllum. Academy scene differs: recap says burned down, source says collapsed; not relied on."}, {"source": "YouTube native transcript", "url": "https://www.youtube.com/watch?v=cFzt9WsrKrY&t=125s", "timestamp": "02:05–03:19", "observations": "Eunuch has green halo; prince requests mirror, admires handsome sixteen-year-old face, discovers own dark halo.", "external_url": "https://novelfull.com/i-am-really-not-the-son-of-providence/chapter-1-i-must-be-a-fake-mc.html", "external_chapter": 1, "match": "Eunuch Gui green halo; mirror reveals Shen Tian handsome at16 and pitch-black halo."}, {"source": "AniList search-index result", "url": "https://anilist.co/manga/161475/Wo-Zhen-De-Bushi-Qi-Yun-Zhi-Zi", "observations": "English title, native/romanized titles and two English synonyms above are catalogued for Chinese manga adapted from web novel.", "access_note": "Search returned full catalog fields; direct web.open returned403. No retry or bypass."}]}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': '7r19-JAUZn0', 'title': 'One Skill Point Per Second! I Turn the Fireball Into a Forbidden Spell', 'aliases': ['一秒一个技能点，我把火球变禁咒', 'I Can Gain One Skill Point Per Second'], 'evidence': '{"video_url": "https://www.youtube.com/watch?v=7r19-JAUZn0", "evidence": [{"video_timestamps": ["00:13–00:48", "03:34"], "observed_paraphrase": "Mage awakens SSS God\'s Gift granting one skill point every second; fireball upgrades into tier-seven Heavenly Flame Dragon Breath.", "external_url": "https://www.novelupdates.com/series/one-skill-point-per-second-i-turn-the-fireball-into-a-forbidden-spell/", "external_location": "Description and Associated Names", "external_paraphrase": "Lin Yi obtains ordinary fireball and SSS Gift of Gods yielding one point each second; 100,000 points unlock seventh-tier Sky Flame Dragon Breath. Catalog gives original Chinese title and author."}, {"video_timestamps": ["30:01–30:55"], "observed_paraphrase": "Undead Knight Rivendell is identified by Eye of Omniscience: unexpectedly level200 rather than60,10millionHP,weaknessHolyLight; passive reduces nonHolyLight damage50%,caps9999perhit,regenerates5000HP/s.", "external_url": "https://novelfull.net/i-can-gain-one-skill-point-per-second/chapter-18-aberrant-death-knight-the-advantage-zone-of-wind-attribute-magic.html", "external_location": "Chapter18", "external_paraphrase": "Same named boss, identification skill, changed level and all three passive numerical effects."}, {"video_timestamps": ["34:07–34:30"], "observed_paraphrase": "Rivendell killed, rewards2.2millionXP plus1.5millionbonus,2000boundpoints and5scrolls worth20each; advancement missioncomplete.", "external_url": "https://fynovel.org/book/i-can-gain-one-skill-point-per-second/20.html", "external_location": "Chapter20", "external_paraphrase": "Same boss kill and exact reward quantities; validates alternate English title."}, {"video_timestamps": ["46:05–46:21"], "observed_paraphrase": "Eye of Omniscience reveals a shadow spider roughly500meters in abyss,20levels stronger than mutatedRivendell.", "external_url": "https://novelkeep.com/novel/i-can-gain-one-skill-point-per-second/chapter-31-divine-fire-celestial-expedition-annihilating-all/", "external_location": "Chapter31", "external_paraphrase": "LinYi sees500–600meter ShadowDemonSpider LV220,20levels aboveRivendell."}], "access_notes": ["Exact-ID web search no results; cloud YouTube watch accessible. Expanded description alone generic, not used as confirmation.", "exportYouTubeTranscript twice returned unavailable; rendered Show transcript UI subsequently exposed full Hindi transcript. Evidence taken from live DOM transcript buttons, not fabricated export.", "NovelUpdates opened successfully; chapter18/20/31 narrative corroboration from websearch-returned page excerpts. Subsequent direct open chapter31 andFicool cache-miss, no browser workaround."]}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': 'i7wa7Mspnqw', 'title': 'The World’s Strongest Fist Fighter', 'aliases': ['World’s Strongest Straight Punch', '정권으로 세계최강'], 'evidence': '{"video_url": "https://www.youtube.com/watch?v=i7wa7Mspnqw", "evidence": [{"source": "Native YouTube Show transcript in cloud browser", "url": "https://www.youtube.com/watch?v=i7wa7Mspnqw&t=16s", "timestamps": ["00:16–00:38"], "observations": "Jinmu tells children the legendary technique has a ridiculous bright-eye/rooster name; children ridicule its constantly changing name.", "external_url": "https://en-thunderscans.com/the-worlds-strongest-fist-fighter-chapter-1/", "external_location": "Chapter 1 opening dojo sequence; browser-rendered panels visually inspected", "match": "Chapter opens with corpse-strewn battlefield and then Chorongtae Fist joke, children complaining that technique name changes every day. Native English ASR uses translated/phonetic wording, not exact romanization."}, {"source": "Native YouTube Show transcript", "url": "https://www.youtube.com/watch?v=i7wa7Mspnqw&t=312s", "timestamps": ["05:12–05:55", "06:29–08:23"], "observations": "Jin-gwon, rendered Jinuan/Guan by ASR, trains alone in mountains ten years to avenge father, emerges age20 and encounters guilds, armored knight and witch. Village is a modern city; gate conflict transformed Murim into hunter and magical skill society.", "external_url": "https://mangavyvy.net/manga/the-worlds-strongest-regime", "external_location": "Series synopsis", "match": "Named Jin-kwon, ten years secluded training for father revenge, descent into vanished Murim replaced by skill-dominated fantasy society, bare fists and martial uniform."}, {"url": "https://mangavyvy.net/manga/the-worlds-strongest-regime", "external_location": "Title/native title and Duplicated Manga section", "match": "The World’s Strongest Fist Fighter, Korean 정권으로 세계최강, and duplicate World’s Strongest Straight Punch listed."}, {"url": "https://m.series.naver.com/comic/moreNotiDetail.series?productNo=14319936", "external_location": "Official Naver series publication notice surfaced by web search", "match": "Original title 정권으로 세계최강 validated, weekly Saturday serialization."}], "access_notes": ["Description generic; not used as story evidence.", "Native Show transcript DOM successful, no export attempt needed.", "Chapter1 accessible with advertisement popup dismissed; inspected rendered panels in ordinary cloud browser, no hidden state or access circumvention.", "External catalogs obtained by web search; chapter1 panels visually inspected directly."]}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': 'zzD5l62FPow', 'title': 'Goblin Corporation', 'aliases': ['Goblin Inc.', '고블린 주식회사'], 'evidence': '{"youtube_url": "https://www.youtube.com/watch?v=zzD5l62FPow", "sources": [{"url": "https://series.naver.com/comic/detail.series?productNo=14440638", "type": "official", "match": "Official 고블린 주식회사 synopsis identifies ordinary office worker Manager Oh displaced during commute into demon realm, becoming goblin lord of territory near destruction. Specific named protagonist, occupation, transit displacement, realm and lord role match."}, {"url": "https://hivetoons.org/series/goblin-inc", "type": "external_alias_catalog", "match": "Lists Goblin Corporation, Goblin Inc, 고블린 주식회사 together and same Manager Oh premise."}], "evidence": "Transcrição nativa00:49–01:19 gerente Oh,33anos,três meses de horas extras,adormece no metrô e desperta em trono;01:27–02:18 goblins o celebram como lorde;03:08–03:50 Wiki,Red Rock Valley,47súditos,contagem de guerra. Fonte oficial https://series.naver.com/comic/detail.series?productNo=14440638 identifica gerente Oh deslocado ao reino demoníaco como lorde goblin à beira da ruína. Aliases https://hivetoons.org/series/goblin-inc .", "transcript_evidence": [{"timestamps": "00:16–01:19", "summary": "Office manager Oh Hyunman,33, exhausted by three months overtime; subway line9 near Yeouido; falls asleep and wakes on stone throne."}, {"timestamps": "01:27–02:18", "summary": "Green goblins celebrate him as lord; red-scarfed goblin offers fruit."}, {"timestamps": "03:08–03:50", "summary": "Wiki display: lord of Red Rock Valley,47 subjects, territory war countdown4days3hours; demon realm."}]}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': '6bv2q_0iafY', 'title': 'My Girlfriend Returned as a Dragon', 'aliases': ['My Dragon Girlfriend Has Returned', 'The Dragon Girlfriend Has Returned', '드래곤 여친이 귀환했다'], 'evidence': '{"video_url": "https://www.youtube.com/watch?v=6bv2q_0iafY", "transcript_evidence": [{"timestamps": "00:00–00:49", "summary": "Girlfriend swallowed by a gate; one year later Minjun (ASR Minjin) visits her grave and a crimson rift appears on anniversary."}, {"timestamps": "02:01–02:18; 03:52–04:28; 05:32–06:05", "summary": "Woman identifies herself as Jong Sia; died in portal flames, reincarnated as red dragon in another realm, returned one year late; reunited with Minjun."}, {"timestamps": "21:59–22:22; 23:03–24:08", "summary": "Dragon elder calls Sia Shasha and says she is 2,500 years old. Her draconic energy consumes Minjun; only survival is fully mastering draconic power."}], "external_evidence": [{"url": "https://series.naver.com/comic/detail.series?productNo=14757265", "type": "official publisher", "support": "Korean title, authors LICO/세칸 and artist 뚠딴; synopsis names Sia and Minjun, Gate Break presumed death, return after one year as dragon, intimacy threatens his life, mastering dragon power necessary."}, {"url": "https://m.comic.naver.com/webtoon/list?titleId=855153&week=wed", "type": "official webtoon", "support": "Same title/names/plot; chapter1–11 listing. Chapters not individually read."}, {"url": "https://divascans.org/series/comic/my-dragon-girlfriend-has-returned", "type": "translation catalog", "support": "English alias My Dragon Girlfriend Has Returned with same Minjun/Sia/Gate Break/year/draconic power synopsis."}, {"url": "https://comix.to/title/gm28k-the-dragon-girlfriend-has-returned?cm_id=11434897", "type": "catalog search result", "support": "Lists My Girlfriend Returned as a Dragon / The Dragon Girlfriend Has Returned / 드래곤 여친이 귀환했다 aliases."}], "evidence_note": "Transcrição nativa: 00:00–00:49 namorada morta em Gate Break e retorno no primeiro aniversário; 02:01 Jong Sia e Minjun (ASR Minjin); 03:52–04:28 renasce dragão vermelho; 05:32–06:05 retorno após um ano; 21:59–22:22 tem 2.500 anos; 23:03–24:08 energia dracônica ameaça vida de Minjun, que deve dominá-la. Corresponde à sinopse oficial Naver https://series.naver.com/comic/detail.series?productNo=14757265 e https://m.comic.naver.com/webtoon/list?titleId=855153&week=wed. Alias inglês confirmado em https://divascans.org/series/comic/my-dragon-girlfriend-has-returned .", "limits": ["No chapter panels inspected; exact character and specific plot matches with official synopsis plus transcript are sufficient."]}', 'reviewed_at': '2026-10-29', 'confirmado': True},
{'video_id': 'fuolp1o_-Wk', 'title': '被女仆买下后，寿命论系统来了？', 'aliases': [], 'evidence': '{"evidence": [{"url": "https://www.youtube.com/watch?v=fuolp1o_-Wk&t=14s", "timestamps": "00:14–01:42", "method": "Previously captured public native transcript, not fresh video access", "detail": "Elian/Elen ASR; elf at80, revived undead140, skeleton19th wedding530, elf bedside13080 with one year left; hot porridge quest awakens Origin Seed.", "source_note": "/user_notes/long_form/momo_tracker_state_delta_20261030_0715.json"}, {"url": "https://www.szzrlb.com/bqgsz/23916276967/", "method": "Live web search index, work-specific synopsis and chapter directory", "observed_at": "2026-11-02T07:24:51Z", "detail": "Title and author explicit. 伊莱安 matches ASR. Same ages80/140/530 nineteenth wedding/13080 elf with one year left; same porridge reward Origin Seed. Directory includes chapter1 公主殿下，我也要喊他主人吗？ and chapter6 系统，给我觉醒，让我看看寿命论的极限！.", "access": "Direct open cache miss; no direct chapter read claimed"}], "limits": ["No primary publisher identity verified", "No direct chapter reading or fresh video access", "No English alias invented"]}', 'reviewed_at': '2026-11-02', 'confirmado': True},
{'video_id': 'eBm_qlVJoIc', 'title': 'Baby Lynx of the Tiger Family', 'aliases': ['Baby Wildcat of the Tiger Clan', 'Baby Cat from the Tiger Family', '호랑이 가문의 아기 살쾡이'], 'evidence': 'Transcrição pública nativa: 00:24–01:35 Barriya nascida entre hienas Mariner, sete anos de abuso, mãe foge/sacrifica-se e três anos de fuga; 04:02–04:54 família tigre Kaliph/Califf, Sirka/Circa e Baiden/Boden, hienas desejam terras quentes e ricas; 05:49–06:06 sopa de carne contrasta com pão seco. Capítulo 3 (linhas 8–18, 142–147 e 180–183 na leitura) reproduz os nomes e os detalhes de clã/terras/alimentação. Não se afirma ordem integral idêntica: o romance traz leite antes da sopa. Título coreano oficial no Kakao; aliases ingleses atestados em CompleteNovel. https://www.youtube.com/watch?v=eBm_qlVJoIc&t=24s https://www.youtube.com/watch?v=eBm_qlVJoIc&t=242s https://exnovels.com/series/baby-wildcat-of-the-tiger-clan/chapter-3 https://page.kakao.com/content/66981502 https://page.kakao.com/content/71032383 https://completenovel.com/baby-lynx-of-the-tiger-family/', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'FaTCyXv28m8', 'title': 'The Magic Genius of the Marquis', 'aliases': ['The Magic Genius of the Marquis House', "The Marquis's Family Magical Genius", "The Marquis' Magic Genius", '후작가의 마법 천재'], 'evidence': 'Transcrição nativa pública: 00:13–01:37 Kyle Seltion/Seltarion, personagem sem mana destinado a morrer antes dos 20, recebe a alma de jogador experiente; conhece a futura rebelião de Adolf e desperta talentos ocultos/mana. 02:42–03:04 o guarda relata que Kyle resistiu à intenção assassina e meditou seis horas. A sinopse do arquivo coreano KMAS identifica Lee Hyun-woo em Kyle Seltarion, incapaz de magia/aura, doença terminal, má reputação e despertar de mana. O capítulo 5 indexado descreve o guarda relatando a Remton que Kyle resistiu à aura e sorriu; a tradução usa Leopold, enquanto o vídeo diz Leon Hart. Título coreano confirmado no Kakao; aliases ingleses atestados no catálogo Thunderscans, sem alegar edição oficial inglesa. Comentário do YouTube apenas suplementar. https://www.youtube.com/watch?v=FaTCyXv28m8&t=13s https://www.youtube.com/watch?v=FaTCyXv28m8&t=162s https://kmas.or.kr/archive/comics/2024023825 https://wuxia.click/chapter/the-magical-genius-of-the-marquis-family-mtl-5 https://webtoon.kakao.com/content/%ED%9B%84%EC%9E%91%EA%B0%80%EC%9D%98-%EB%A7%88%EB%B2%95-%EC%B2%9C%EC%9E%AC/4215 https://en-thunderscans.com/comics/the-magic-genius-of-the-marquis/', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'R1ivBXoJMzU', 'title': '死亡亿次，我复制天赋杀穿万族！', 'aliases': ['After Billions of Deaths: I Copy Talents and Slaughter All Races!', 'After dying billions of times, I copied my talents and killed all races!'], 'evidence': 'Transcrição nativa 00:48–01:38: retorno após invasão dos gigantes; mestre sem memória pergunta sobre três destinos, primeiros dois concluídos; terceiro é tribo Sky Eye para obter talento SSS que identifica outros SSS. Sequência corresponde ao cap.80. Intro 00:00–00:23 também confirma diário futuro, EX Death Copy, colega com rewind exato de 12h e traição (cap.3). Canônico e autor no Fanqie; aliases ingleses são MTL atestados. Título visual nos últimos segundos NÃO verificado. https://www.youtube.com/watch?v=R1ivBXoJMzU&t=48s https://www.fanmtl.com/novel/after-dying-billions-of-times-i-copied-my-talents-and-killed-all-races_80.html https://fanqienovel.com/reader/7285397530123829795 https://fanqienovel.com/reader/7274785095520059963 https://fanqienovel.com/page/7274774422865579069 https://wtr-lab.com/en/novel/9943/after-billions-of-deaths-i-copy-talents-and-slaughter-all-races', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': '924LAZ5wVKE', 'title': "A Regressor's Tale of Cultivation", 'aliases': ['회귀수선전(回歸修仙傳)', '회귀수선전', '回歸修仙傳'], 'evidence': 'Native transcript visible in public YouTube UI despite transcript export reporting unavailable. 00:08–00:40 girl brings food to old soap maker; fifty years since company workshop journey and landslide; giant fox and two-headed snake. 01:18–01:56 Director Kim remains with him then buys martial manual after six months. 02:29–02:44 soap-making method stolen. 03:15–03:53 death and first regression. Exact sequence matches prologue (labeled Chapter1 by PYG-KIT). 04:09–06:43 boss Jeon blaming driver after forcing overtime and substituting him as driver matches novel Chapter1. Official Naver lists canonical Korean title, author 엄청난 and Seo Eun-hyun. Fontes: ["https://www.youtube.com/watch?v=924LAZ5wVKE&t=8s", "https://www.pyg-kit.com/en/books/a-regressors-tale-of-cultivation/chapters/255518", "https://asurascans.com/novels/a-regressors-tale-of-cultivation/chapter/1", "https://m.series.naver.com/novel/detail.series?productNo=9807283"]', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': 'rYCmagsOYBw', 'title': 'Revenge of the Baskerville Bloodhound', 'aliases': [], 'evidence': 'Public native transcript 00:08–00:34 false accusation, guillotine, regression to newborn Baskerville. 01:28–02:31 infant crawls through sword maze to Styx, remains underwater, Hugo retrieves him; 03:39 Vikir named. Novel Chapter1 Hell Hound matches execution after demon war, Hugo\'s illegitimate son, infant not crying, Cradle of Blades sword maze and Styx blessing. Seven-minute underwater detail observed in video but not independently verified from Chapter1. Official Yen Press and Tapas establish exact title. Uploader also names title in description and pinned comment, supplemental only. Fontes: ["https://www.youtube.com/watch?v=rYCmagsOYBw&t=88s", "https://curspe.com/novels/revenge-of-the-baskerville-bloodhound/chapter-1-hell-hound-%EF%BC%91/", "https://yenpress.com/titles/9798400904547-revenge-of-the-baskerville-bloodhound-vol-1", "https://tapas.io/series/revenge-of-the-baskerville-bloodhound/info", "https://www.youtube.com/watch?v=rYCmagsOYBw&lc=Ugx8bVdlvKTEx81yYSx4AaABAg"]', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': '47Dc_SwnwI8', 'title': '解密地球是宇宙飞船，我成国士了', 'aliases': [], 'evidence': 'A transcrição pública nativa usa Leo Lynwood em vez de Lin Yuan, mas reproduz a sequência específica do capítulo 7: de 31:27 a 31:51, um aplicativo quântico simula geografia, clima e desastres da época anterior à dinastia Qin durante uma transmissão. De 32:54 a 33:22, cita mais de 200 terremotos, 149 enchentes e 235 secas, reduzidos após a Grande Muralha. De 34:40 a 34:56, a simulação acelera dez vezes, com resistores e capacitores na muralha e 20 mil espectadores. De 35:52 a 36:17, cita tijolos de 6 a 7 kg queimados a 1.000 °C e argamassa de cal, arroz glutinoso e composto desconhecido. Correspondência exata com o capítulo 7 oficial no Fanqie. Nenhum alias inglês validado. Fontes: ["https://www.youtube.com/watch?v=47Dc_SwnwI8&t=1887s", "https://www.youtube.com/watch?v=47Dc_SwnwI8&t=1974s", "https://fanqienovel.com/reader/7323411359763268158", "https://fanqienovel.com/keyword/7331328564584777768"]', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': '6FR7MQUy-q0', 'title': 'Monster’s Streamer Star', 'aliases': ['Monster Streaming Star', 'Monster Livestream Star', '몬스터의 인방스타'], 'evidence': 'Transcrição pública nativa: 00:46–01:18, slime sem visão recebe conceitos do sistema e apelido Squishy. 01:26–02:14, Noblesse Fire insulta o truque de slime streaming e não recebe resposta porque o protagonista não lê; Gothic Luxury Bone defende o iniciante e depois percebe que é um slime. Sequência e nomes correspondem ao capítulo 1. Descrição anuncia capítulos 1–8, mas cobertura integral não foi verificada. Fontes: ["https://www.youtube.com/watch?v=6FR7MQUy-q0&t=46s", "https://www.youtube.com/watch?v=6FR7MQUy-q0&t=86s", "https://asurascans.com/novels/monster-s-streamer-star/chapter/1", "https://www.novelupdates.com/series/monsters-streamer-star/"]', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': 'oupdKnZYGyA', 'title': 'Helmut', 'aliases': ['Helmut: The Forsaken Child', '헬무트'], 'evidence': 'Revisão +3h substantiva concluída com Show transcript nativo público. 02:49–03:37, Helmut caça coelho; Elaga extrai núcleo, explica força/longevidade, impede o garoto de comer, pega o núcleo e explica que o transformaria em criatura demoníaca incapaz de sair da floresta. Sequência exata do capítulo 2 oficial Tapas. Trecho 00:00–01:28 com Asuka, professor Dwayne, exame de dez estágios e centopeia foi observado, mas não comparado a fonte externa e não fundamenta sozinho a confirmação. Fontes: ["https://www.youtube.com/watch?v=oupdKnZYGyA&t=169s", "https://tapas.io/episode/3444875", "https://tapas.io/series/helmut/info", "https://asuranovel.com/novels/helmut-the-forsaken-child/"]', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': 'gv6YVGxUmHY', 'title': 'The Reincarnated Master Craftsman', 'aliases': ['神級クラフトの転生者', 'The Reincarnation Of God Level Crafting', 'Divine-Grade Craft Reincarnator', 'Kami-Kyuu Crafter no Tenseisha', 'Reincarnated Master Craftsman'], 'evidence': 'Transcrição nativa: 00:16–00:49, Allen escolhe Crafter e cria rifle. 00:53–01:18, entrega armas aos aldeões; diante do receio de tiro amigo, demonstra disparando contra um aldeão sem feri-lo e ganha XP. Comparação visual do capítulo 1 Kayn: páginas 15/20 mostram aldeões contra goblins; 31, crafter tratado como lixo; 37, entrega das armas; 38, dúvida sobre fogo amigo, restrição incorporada e disparo de Allen; 39, aldeão assustado; 40, retomada do combate. Allen/crafter/armas modernas corroborados pela sinopse oficial LINE. Sinopse LINE lida via web antes de navegador indicar Japão-only; nenhum contorno tentado. Fontes: ["https://www.youtube.com/watch?v=gv6YVGxUmHY&t=53s", "https://kaynscans.com/series/comic/the-reincarnation-of-god-level-crafting/chapter/1", "https://kaynscans.com/series/comic/the-reincarnation-of-god-level-crafting", "https://manga.line.me/product/periodic?id=S160155"]', 'reviewed_at': '2026-10-22', 'confirmado': True},
{'video_id': '0vZ2eg7qnMw', 'title': 'Martial Evolution: The Beast King Awakens', 'aliases': ['高武进化：从觉醒怪兽之王开始', 'Martial Evolution: Start by Awakening the King of Monsters', 'Gao Wujin Hua: Cong Juexing Guaishou Zhi Wang Kaishi'], 'evidence': 'Transcrição nativa: 00:52–01:09, Yi He perdeu os pais há dois anos e abandona o treino. 01:47–02:33, recebe injeção indolor enquanto colegas sofrem; Infinite Monster Template, Godzilla A-rank 3%, rugido derruba colegas e uma menina espuma e desmaia. Sequência corresponde ao capítulo 1 textual externo. Menina Wang Xing no vídeo versus Wang Tongtong no texto: diferença preservada, sem normalização inferida. WebComics oficial corrobora título, Yi He, genes e Legendary Godzilla. Não houve comparação visual de painéis. Fontes: [{"url": "https://www.youtube.com/watch?v=0vZ2eg7qnMw&t=107s", "kind": "native public transcript"}, {"url": "https://www.webnovel.com/book/high-martial-arts-evolution-start-by-awakening-godzilla-physique_35914685400544105/monster-template-%5Blegendary-godzilla%5D!_96420330289036899", "kind": "user publication, not official; chapter-specific textual comparison"}, {"url": "https://webcomicsapp.com/en/action/martial-evolution-the-beast-king-awakens/6a02ccc162661d533f19c945", "kind": "official title and synopsis"}, {"url": "https://anilist.co/manga/191902/Gao-Wujin-Hua-Cong-Juexing-Guaishou-Zhi-Wang-Kaishi", "kind": "indexed aliases; direct open returned 403, not bypassed"}]', 'reviewed_at': '2026-10-23', 'confirmado': True},
{'video_id': 'tlHhY2KJAkk', 'title': 'The Knight King Who Returned with a God', 'aliases': ['The Knight King Who Returned with God', 'The Knight King Returns with God', '300年ぶりに神と帰還した騎士王'], 'evidence': 'Transcrição nativa 00:21–00:58: portal negro, equipe da Associação, Han Hari e Kim Jinsu. 02:15–02:45: Leon se ofende com insulto a Lionheart, quebra vidro reforçado no interrogatório; Hari pede desculpas pela diferença cultural. Mesma sequência do capítulo 3, The Lionhearted King. Naver 809618 abriu sem texto; nenhum alias coreano validado. Fontes: ["https://www.youtube.com/watch?v=tlHhY2KJAkk&t=42s", "https://www.youtube.com/watch?v=tlHhY2KJAkk&t=135s", "https://freewebnovel.com/novel/the-knight-king-who-returned-with-god/chapter-3", "https://manhwatracker.com/comics/the-knight-king-who-returned-with-a-god-317", "https://www.the-giga.com/project/jp-the-knight-king-returns-with-god/"]', 'reviewed_at': '2026-10-23', 'confirmado': True},
{'video_id': '6Rot-lU8dTM', 'title': 'The Tale of Cultivation and Demon Extermination', 'aliases': ['Tale of Cultivation and Demon Extermination', 'Cultivation and Exorcism Story', 'Chronicles of the Demon Slayer', 'Chronicles Of The Demon-Slaying Cultivator', 'Suseon-gwa Toema Iyagi', '수선과 퇴마 이야기', '멸귀수도전'], 'evidence': 'Transcrição 00:00–00:35: menino de dez anos mata demônio com lança de bambu e expõe a cabeça no portão. 00:44–01:37: Mongryeon oferece mingau. 01:44: menino se escondeu no armário durante massacre. Capítulo 1 nomeia Yise/Mongryeon e reproduz a mesma sequência. Aliases documentados no índice Asura. Fontes: ["https://www.youtube.com/watch?v=6Rot-lU8dTM&t=27s", "https://asurascans.com/novels/the-tale-of-cultivation-and-demon-extermination/chapter/1", "https://asurascans.com/novels/the-tale-of-cultivation-and-demon-extermination"]', 'reviewed_at': '2026-10-23', 'confirmado': True},
{'video_id': '3_fxYK5RO7k', 'title': 'Martial Evolution: The Beast King Awakens', 'aliases': [], 'evidence': 'Transcrição nativa finalmente acessível. Vídeo 1:10: terceiro ano, turma 7. 5:05: injeção no pescoço, correspondente ao painel 50 do capítulo 1 oficial. 5:43: Infinite Monster Template, painel 58. 6:39–6:56: rank A DiMora, Flame Lord com desbloqueio 100% e compatibilidade 3%, painel 71. Correspondência específica independente, não apenas comentário antigo. Sem aliases adicionais confirmados. Fontes: ["https://www.youtube.com/watch?v=3_fxYK5RO7k&t=305s", "https://www.youtube.com/watch?v=3_fxYK5RO7k&t=399s", "https://www.webnovel.com/comic/martial-evolution-the-beast-king-awakens_33218244100363701/chapter-1-doesn\'t-that-make-me-the-king-of-beasts!_89232737818436153"]', 'reviewed_at': '2026-10-24', 'confirmado': True},
{'video_id': 'pKuVO5WsikI', 'title': 'The Art of Reincarnation', 'aliases': ['Standard of Reincarnation'], 'evidence': 'Transcrição nativa: 03:19 derrota prévia em 21 duelos; 04:03 facada pelas costas após vitória; 04:36 santa salva; 05:03 acusação de sacrificar 300 crianças; 05:18 tendões cortados e mana selada; 07:28 Vincent Adenka. Correspondência detalhada com capítulo 1 externo e sinopse oficial Tapas, que liga Daven e Kazin à reencarnação em Vincent Adenka. Não baseada apenas no comentário do uploader. Fontes: ["https://www.youtube.com/watch?v=pKuVO5WsikI&t=199s", "https://www.youtube.com/watch?v=pKuVO5WsikI&t=303s", "https://www.youtube.com/watch?v=pKuVO5WsikI&t=448s", "https://www.webnovel.com/book/standard-of-reincarnation_27614358300946405/chapter-1_74126788887893741", "https://tapas.io/series/the-art-of-reincarnation"]', 'reviewed_at': '2026-10-24', 'confirmado': True},
{'video_id': 'ns3xvpKDNJs', 'title': 'Sandmancer of the Scorched Desert', 'aliases': ['Sand Mage of the Scorched Desert', '불탄 사막의 모래술사'], 'evidence': 'Transcrição nativa 00:00–00:49: Terra desertificada; Zeon no ônibus para minas; Neo Soul/Neo Seoul. 28:56–30:21: Deodin diz Zeon não usa nem 1%; Zeon testa raio de 5 m, endurece solo mas gasta mana, concentra mana nas pernas e depois move areia apenas sob os pés. Capítulo 8 externo nomeia Zeon/Deioden e reproduz a sequência das três tentativas, 1%, raio de 5 m e areia sob pés. Thunder confirma título inglês/coreano e sinopse de Zeon único mago de areia após oceanos evaporarem. Não baseada apenas no título, thumbnail ou comentário. Fontes: ["https://www.youtube.com/watch?v=ns3xvpKDNJs&t=25s", "https://www.youtube.com/watch?v=ns3xvpKDNJs&t=1736s", "https://beastnovels.com/series/sandmancer-of-the-scorched-desert/8", "https://en-thunderscans.com/comics/sand-mage-of-the-scorched-desert/"]', 'reviewed_at': '2026-10-24', 'confirmado': True},
{'video_id': 'VKTAPTRRweo', 'title': 'The Nine Heavens Swordmaster', 'aliases': ['Heavenly Inquisition Sword', 'Nine Heavens Swordmaster', '구천구검', 'Gucheongugeom'], 'evidence': 'Transcrição nativa pública: 00:26–00:45 pai recluso há seis anos após morte da segunda esposa; primeira esposa maltrata o menino. 06:48–07:19 após morte do pai, menino é trancado no depósito com os pertences descartados. 07:54–08:18 encontra espelho ornamentado e reflexo move a cabeça sozinho. 08:33–09:32 duplo demonstra espada de madeira, menino imita e cai. 11:25–12:27 escrita divina no espelho, Nine Heavens Sword Art herdada do pai, treino por dez anos. Conjunto específico corresponde à sinopse oficial Tapas: Yeon Jeokha, filho da segunda esposa, abuso pela primeira, espírito no espelho ensina arte criada pelo pai e treino por uma década. Nome é transcrito com variantes fonéticas Jioka/Gioka; não normalizado isoladamente. Descrição e comentário fixado do uploader corroboram canônico e Heavenly Inquisition Sword. Alias coreano/romanizado e título sem The atestados no catálogo externo Specter Scans. Episódio 1 oficial foi aberto visualmente, mas seus painéis NÃO foram usados para afirmar correspondência capítulo a capítulo. Fontes: ["https://www.youtube.com/watch?v=VKTAPTRRweo&t=474s", "https://www.youtube.com/watch?v=VKTAPTRRweo&t=685s", "https://tapas.io/series/the-nine-heavens-swordmaster/info", "https://specterscans.com/series/nine-heavens-swordmaster", "https://www.youtube.com/watch?v=VKTAPTRRweo&lc=Ugx8RIwEwjtzfbjZKil4AaABAg"]', 'reviewed_at': '2026-10-24', 'confirmado': True},
{'video_id': 'MTcB9eFi_r4', 'title': 'Monster’s Streamer Star', 'aliases': ['Monster Streaming Star', '몬스터의 인방스타'], 'evidence': 'Transcrição nativa pública: 0:00–0:42, dragão vermelho no vulcão assiste a streams há 600 anos e encontra o canal \'I want to see\'. 0:59–1:59, slime verde nasce de mana na caverna; o sistema reconhece inteligência, concede streaming/chat e injeta conhecimento porque ele ainda é cego; escolhe Malang. 2:38–3:18, Bone Dragon entra e discute com Fire Dragon. 4:21–6:15, Free Spirit procura Slime Queen e pergunta sobre a visão dos recém-nascidos. O conjunto específico corresponde ao capítulo 1 da novel e à ficha da adaptação manhwa com Mallangi, Slime Queen, lich, Arachne e Fenrir. Comentário aponta o nome, usado somente como pista. Aliases atestados em NovelUpdates e na ficha Genz. Fontes: ["https://www.youtube.com/watch?v=MTcB9eFi_r4&t=42s", "https://www.youtube.com/watch?v=MTcB9eFi_r4&t=65s", "https://genztoons.org/chapter/65e37a2837e-65e37ac9b0a/", "https://genztoons.org/series/monsters-streamer-star/", "https://www.novelupdates.com/series/monsters-streamer-star/"]', 'reviewed_at': '2026-10-24', 'confirmado': True},
{'video_id': 'XjiIVna3hrc', 'title': 'Is This Hero for Real?', 'aliases': [], 'evidence': 'Transcrição nativa 00:08–00:25: turma transportada a Fantasia, desejos atendidos após derrotar Demon King. 00:34–01:21: Hansoo recusa ser herói, pede voltar aos pais, ninguém acompanha, colegas enviam recados aos familiares. 01:29–01:36: portal o abandona entre monstros que o chamam de carne. Correspondência específica com capítulo 1 textual e sinopse oficial Tapas. 02:11–02:43 Hero curse traduz inimigos, não fadas; 03:14–03:47 Assa/lone wolf e bênção observados como corroboradores, não comparados externamente neste round. Descrição/comentário nomeiam a obra mas são pistas suplementares; título completado não usado para alegar cobertura integral. Fontes: ["https://www.youtube.com/watch?v=XjiIVna3hrc&t=34s", "https://www.youtube.com/watch?v=XjiIVna3hrc&t=81s", "https://wuxia.click/chapter/is-this-hero-for-real-1", "https://tapas.io/series/is-this-hero-for-real/info"]', 'reviewed_at': '2026-10-25', 'confirmado': True},
{'video_id': 'VuYuPBHujuk', 'title': 'I Became a Married Man in Another World', 'aliases': ['How I Became a Married Man in Another World', '이세계서 유부남된 썰'], 'evidence': 'Transcrição pública nativa: 00:07–00:39, Juhan/Juan dá dinheiro a velho vestido de Santa; desejo inicial de ganhar na loteria é rejeitado como mentira; admite querer família, esposa e filha. 00:54–01:09, dorme em trem e desperta em carroça/cela. 01:17–01:48, está nu, ouve língua desconhecida e toma roupas de cadáver para sobreviver ao frio. Sequência específica corresponde ao capítulo 1 da novel, que identifica Kim Joo-hwan. Sinopse oficial Naver corrobora desejo de esposa/filha a Santa e transporte a outro mundo. Comentário fixado e comentários com título serviram só de pistas. Foram lidos trechos adicionais sobre Lizzie e filha, mas não usados como evidência externa de identidade. Nenhum intervalo completo de capítulos ou último capítulo verificado. Título inglês/alias atestados em catálogos secundários, não foi estabelecida licença inglesa oficial. Fontes: [{"url": "https://www.youtube.com/watch?v=VuYuPBHujuk&t=7s", "type": "native public transcript"}, {"url": "https://www.youtube.com/watch?v=VuYuPBHujuk&t=69s", "type": "native public transcript"}, {"url": "https://nyxscans.com/series/i-became-a-married-man-in-another-world-novel/chapter-1", "type": "external chapter-specific translated novel"}, {"url": "https://m.series.naver.com/novel/detail.series?productNo=6630750", "type": "official original novel title/synopsis"}, {"url": "https://arenascan.com/manga/i-became-a-married-man-in-another-world/", "type": "secondary English title and alias catalog"}, {"url": "https://rinkocomics.com/comic/i-became-a-married-man-in-another-world/", "type": "secondary English/Korean title catalog"}, {"url": "https://m.comic.naver.com/webtoon/list?titleId=850103", "type": "official manhwa linked from original novel; same Korean title and Santa/wife/daughter synopsis"}] [\'No video visual-panel match claimed.\', \'No sign-in, CAPTCHA or access bypass.\', \'No external write or message.\', \'Comments about chapter30 endpoint not independently checked and excluded.\']', 'reviewed_at': '2026-10-26', 'confirmado': True},
{'video_id': 'JVtIJ37tx3I', 'title': 'Debtbound by Blood', 'aliases': ['Private Debtors', 'Loan Shark Ties', 'Debt-Bound Classroom', 'The Loan Shark Teacher', "The Devil's Classroom", '사채지간'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=JVtIJ37tx3I&t=0s", "observed_at": "2026-10-26T16:21:28Z", "method": "native cloud browser transcript screenshot", "timestamps": "00:00–00:10", "detail": "Kim Ayan falls from school roof; brother Kim Sangan is debt collector and enters her classroom as new teacher to find who drove her to death."}, {"url": "https://www.youtube.com/watch?v=JVtIJ37tx3I&t=34s", "observed_at": "2026-10-26T16:22:05Z", "timestamps": "00:34", "detail": "Sang enters gambling debtors\' basement alone to ask for payment."}, {"url": "https://m.comic.naver.com/webtoon/list?titleId=846114", "type": "official primary", "detail": "사채지간; loan shark Kim Sang-an becomes homeroom teacher of students whose bullying caused his teacher sister\'s suicide."}, {"url": "https://asurascans.com/comics/debtbound-by-blood-11fe7da3", "type": "external alias source", "chapters": "1 Loan Shark Kim Sang-an;2 Teacher Kim Sang-an(1)", "detail": "Same named protagonist, sister and teacher revenge; explicit English aliases and Korean title."}]', 'reviewed_at': '2026-10-26', 'confirmado': True},
{'video_id': 'r453L33Cads', 'title': 'Streaming My Second Life', 'aliases': ["Reincarnator's Stream", 'Reincarnated Streamer', 'Tensei Streamer', '転生ストリーマー', '환생자의 스트리밍'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=r453L33Cads&t=0s", "method": "cloud browser transcript UI", "observed_at": "2026-10-26T16:26:37Z", "timestamps": "00:00;01:57;03:11;01:01:39–01:02:31", "detail": "Rank1 betrayed with team; Subaru at death; twenty years later reincarnates in weak Subaru Hosoy; streamer Subaru wraps body with lightning to power meridians."}, {"url": "https://asurascans.com/comics/reincarnators-stream-3ec3b16f", "detail": "Narukami Subaru Master of Lightning, betrayal during tower raid, reincarnation20years later, livestreaming; lists Korean/Japanese aliases."}, {"url": "https://tapas.io/series/streaming-my-second-life/info", "type": "official primary", "detail": "Streaming My Second Life original title 환생자의 스트리밍 by B.ain/NEXT LEVEL Studio; Lee Suhyeok is localized name; betrayed20years earlier, weakbody level1, stream powers stats."}, {"url": "https://piccoma.com/web/product/175783", "status": "geoblocked", "detail": "Japan-only notice; not bypassed; not used as directly read synopsis."}]', 'reviewed_at': '2026-10-26', 'confirmado': True},
{'video_id': 'fDpTQrEnXbY', 'title': 'I Can See the Success Rate', 'aliases': ['我能看到成功率', 'Wo Neng Kan Dao Cheng Gong Lu', 'Odds Are in My Favor'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=fDpTQrEnXbY&t=40s", "observed_at": "2026-10-26T19:20:01Z", "method": "native cloud browser transcript UI", "timestamps": "00:40–00:47;02:01–02:48;03:24–04:49", "detail": "Bai Woo failed writer of Starting today I raise slimes; chooses11scratchcards ten100% one0%; later wins20420yuan; percentages can exceed100 and adjust with amount questioned."}, {"url": "https://www.scribblehub.com/read/1323942-i-can-see-the-success-rate/chapter/1323944/", "chapter": 1, "detail": "Exact Bai Wu failed slime novel,11cards ten100% one0%,next tickets total20420yuan. Specific sequence establishes match."}, {"url": "https://www.kuaikanmanhua.com/web/topic/5917/", "type": "official publisher", "detail": "我能看到成功率 by纳沐,白武 gains success-rate sight. Confirms original title and protagonist."}, {"url": "https://donotaku.com/en/manga/wo-neng-kan-dao-cheng-gong-lu", "type": "alias catalog", "detail": "Lists I Can See the Success Rate/Odds Are in My Favor/Chinese/pinyin."}]', 'reviewed_at': '2026-10-26', 'confirmado': True},
{'video_id': 'TNkytpdeTiQ', 'title': '我每周获得一个新人设', 'aliases': ['I Get a New Persona Every Week'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=TNkytpdeTiQ&t=124s", "observed_at": "2026-10-26T19:20:51Z", "timestamps": "00:00–00:53;02:04–04:45", "detail": "Morgan Hail polishedpersona, Camellia literaryneighbor,Vera makeover. Joins readersgroup searching bonuschapter, author AilingCicada writes4000/day,discussion3heroines; cannot locate girl amongmembers;waitsVera class1 whileboys hostile. Native transcript."}, {"url": "https://www.qidian.com/chapter/1049395605/909556574/", "chapter": 22, "title": "第22章 好人一生平安", "observed_at": "2026-10-26T19:22:20Z", "method": "native cloud browser accessibility UI", "detail": "Exact sequence QQgroup admission,missingbonus,memechat,author病蝉4000words/day versus10–20k,threeheroines;张朝暮 seeks段婵儿 inmembers;waits陈真真 class1,boys hostility,joke she first would attack him. Independent source match despite localized Englishnames."}, {"url": "https://www.qidian.com/chapter/1049395605/907173638/", "chapter": 1, "observed_at": "2026-10-26T19:21:58Z", "detail": "Freshly reread official chapter polishedpersona,instinctivehaircut,literaryneighbor; agrees opening recap."}, {"url": "https://daosearch.io/qidian/book/1049395605/i-get-a-new-persona-every-week", "detail": "English translated alias and Chinese original/Qidianbook1049395605."}]', 'reviewed_at': '2026-10-26', 'confirmado': True},
{'video_id': 'hflWMkK5pc4', 'title': 'Resurrection Boy', 'aliases': [], 'evidence': '[{"url": "https://www.youtube.com/watch?v=hflWMkK5pc4&t=5s", "method": "native cloud browser transcript UI", "observed_at": "2026-10-26T22:15:35Z", "timestamps": "00:00–03:42", "detail": "Gio living skeleton; mutated heart gives immortality; kidnapped age7 and experimented10years including organ removal. Escapes, lives alley withdogs, needsfood forregeneration. Girl Songhi/Hedgi/Sunhedi (ASRvariants) helps, feeds and clothes him; Kim Jio explicitly named2:39. Arm falls off2:24 and reattaches, makeup onbones2:32."}, {"url": "https://www.webtoons.com/id/action/resurrection-boy/list?title_no=10865", "method": "official publisher synopsis", "observed_at": "2026-10-26T22:16:56Z", "detail": "Resurrection Boy byRYU. Named Kim Jio escapes10year laboratory experimentation involving heartmutants,poisons and organtransplants,looks living skeleton; Song Hyeji treats him as human. Specific character and plot match, not title similarity."}]', 'reviewed_at': '2026-10-26', 'confirmado': True},
{'video_id': 'x_wo5ww4BKE', 'title': 'The Low-Level Knight, Unrivaled by Forbidden Flames', 'aliases': ['The Low-Level Knight, Unrivaled by Forbidden Flames', '底辺騎士、禁忌の炎で無双する'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=x_wo5ww4BKE&t=0", "observed_at": "2026-10-27T04:19:22Z", "detail": "Native transcript now available. 0:00–0:41 sole survivor Luca/Lick sent to orphanage; divine knights use oath ritual. 1:10 purple chalice liquid;1:19 arm cut;2:36 drinks before oath, transforms;3:24 arm regrown;3:52 female commander Arthur;5:02–5:10 power without vow."}, {"url": "https://manga.line.me/product/periodic?id=S153994", "observed_at": "2026-10-27T04:20:32Z", "detail": "Primary publisher direct read confirms Japanese title and Luca/Ryuka, destroyed hometown, Divine Law Knights, monster interrupts oath ritual, forbidden flame without offering. Listed chapters1Awakening,2Power of Oaths,3Knights custody. No chapter panels inspected."}, {"url": "https://tateyomi-award.natalie.mu/vote_domestic.html", "detail": "Indexed editorial snippet for exact title cites commander Arthur; direct open403, no bypass."}, {"url": "https://mangabaka.org/manga/384014/The-Low-Level-Knight-Unrivaled-by-Forbidden-Flames", "detail": "Indexed title mapping English/Japanese; direct open cache miss."}, {"url": "https://manhwaz.com/webtoon/the-low-level-knight-unrivaled-by-forbidden-flames", "detail": "Indexed English title and specific same synopsis; direct open timeout."}]', 'reviewed_at': '2026-10-27T04:20:32Z', 'confirmado': True},
{'video_id': 'baNnI837y1g', 'title': 'The Regressor and the Blind Saintess', 'aliases': ['The Regressor and the Blind Saintess', 'The Regressionist and the Blind Saintess', 'Hoegwijawa Maengin Seongnyeo', '회귀자와 맹인 성녀'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=baNnI837y1g", "observed_at": "2026-10-27T07:24:30Z", "finding": "Direct cloud browser navigation redirected to Google sorry unusual traffic/reCAPTCHA. No video title, description, scenes or transcript observed. Challenge neither solved nor bypassed."}, {"kind": "public_index_search", "query": "\\"baNnI837y1g\\"", "observed_at": "2026-10-27T07:24:47Z", "finding": "No results"}, {"url": "https://www.youtube.com/watch?v=baNnI837y1g&t=330s", "kind": "native_transcript", "observed_at": "2026-10-27T13:18:32Z", "detail": "1:08-1:31 villain cursed by heroes three years after Demon King defeat;2:33 blind silver-haired woman;3:04 rare Holy Kingdom platinum rosary;3:54-4:22 saint publicly thought dead;5:30-5:37 Renee/Vera identified."}, {"url": "https://anilist.co/manga/217902/Hoegwijawa-Maengin-Seongnyeo/", "kind": "external_indexed_synopsis", "detail": "Vera cursed, blind Renée declared dead shelters him in gutter; after her death he regresses to protect her. Native title and English alias. Direct open403; indexed text substantive."}, {"url": "https://www.manganato.gg/manga/the-regressionist-and-the-blind-saintess", "kind": "external_indexed_catalog", "detail": "Same specific character/plot and verified aliases; direct open cache miss."}, {"url": "https://www.webtoonguide.com/ko/db/content-info/5624264", "kind": "external_indexed_catalog", "detail": "Korean synopsis confirms Vera/Renee, declared-dead blind saint, curse and regression."}]', 'reviewed_at': '2026-10-27', 'confirmado': True},
{'video_id': 'uKI9M9Sh8-U', 'title': '奶爸系统觉醒', 'aliases': ['奶爸系统觉醒'], 'evidence': '[{"kind": "public_index_search", "query": "\\"uKI9M9Sh8-U\\"", "observed_at": "2026-10-27T07:24:47Z", "finding": "No results"}, {"url": "https://www.youtube.com/watch?v=uKI9M9Sh8-U&t=14s", "kind": "native_hindi_transcript", "detail": "0:14-2:11 Xu Mengyao-like ASR arrives with daughter after3years, left university abroad after drugged encounter, doctor warned only pregnancy, biological-daughter system;17:14 Lin Chen;28:33-29:07 bumper cars grant system skill;39:08 pen name Lin Yu;41:33 Tongxin website editor."}, {"url": "https://fanqienovel.com/page/7406130681077582873", "kind": "official_source_novel_opened", "detail": "奶爸系统觉醒 by女帝666; Lin Chen, Xu Mengyao, Xixi,3year reunion, parenting skill rewards. Chapter24 Lin Yu stories;chapter12 Tongxin contract."}, {"url": "https://fanqienovel.com/reader/7406130905938412057", "kind": "official_chapter_opened", "chapter": "1", "detail": "Exact initial reunion, former university rent, drugged Xu Mengyao left abroad, only viable pregnancy, child recognizes dad/system activation, suitcase and cash. Source font glyphs partly garbled but names and scene sequence readable."}]', 'reviewed_at': '2026-10-27', 'confirmado': True},
{'video_id': '9aTma1WiXYc', 'title': 'Global Awakening: The Synthesis Master Starts with an Undead Army', 'aliases': ['Global Awakening: The Synthesis Master Starts with an Undead Army', 'Everyone Start with Synthesizing the Undead Army', '全民：合成师，开局合成亡灵大军', 'National Class: Fusion Master — Starting by Synthesizing an Undead Army', 'Worldwide: Synthesizer · Starting with Synthesizing an Undead Army', 'Starting with Synthesizing the Undead Army', 'Global Composite Master: Compositing an Undead Army from the Start'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=9aTma1WiXYc&t=64s", "kind": "native_transcript", "observed_at": "2026-10-27T13:18:50Z", "detail": "1:04 protagonist identifies as Chen Mo; 1:11 transmigrated three years ago; 5:02 awakens two-star Skeleton Mage; 6:06 merged souls allow second class; 6:23 hidden divine Infinite Synthesizer; 6:32 combined seven stars; 7:02-7:31 otherworld claws target five-star girl while his class stays hidden."}, {"url": "https://www.youtube.com/watch?v=9aTma1WiXYc&lc=UgxaCTEOWrkSGIdjJ854AaABAg", "kind": "pinned_comment_lead", "detail": "Pinned commenter names exact Global Awakening title. Independently matched rather than accepted alone."}, {"url": "https://reimanga.net/manga/everyone-start-with-synthesizing-the-undead-army-109744", "kind": "external_catalog_opened", "observed_at": "2026-10-27T13:19:03Z", "detail": "Chen Mo, rare hidden Fusion Master, synthesizes and evolves skeletons and wraiths into undead army; aliases listed in record match this specific character and mechanism."}, {"url": "https://jikuukanmanga.com/v5-global-awakening-the-synthesis-master-starts-with-an-undead-army~.html", "kind": "external_indexed_summary", "observed_at": "2026-10-27T13:18:55Z", "detail": "Search result crawled today identifies exact Global Awakening title, Chen Mo, hidden Synthesizer, fusion/evolution of undead legion. Direct open timed out; indexed evidence used with independently opened ReiManga."}]', 'reviewed_at': '2026-10-27', 'confirmado': True},
{'video_id': 'Ls90fiBKgv0', 'title': 'Creation: From the Low-End Prehistoric to the Daluo Myth', 'aliases': ['Creation: From the Low-End Prehistoric to the Daluo Myth', 'Creation: From the low-end flood to the latitude of the Daluo myth', '创世：从低端洪荒升纬大罗神话'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=Ls90fiBKgv0&t=77s", "kind": "native_transcript", "observed_at": "2026-10-27T13:19:43Z", "detail": "0:12 fifteen years after transmigration; 0:21 Daxia; 1:17 teacher Liu Yingjiao; 1:35 Li Ming student1526 receives Divine Source; 3:48 Li family Tianhai; 3:55 Su Zhou; 4:19-5:08 empty Chaos World judged dead-end; 6:36 Pangu and 3000 godfiends; 7:00 Daluo Primordial World."}, {"url": "https://www.fanmtl.com/novel/creation-from-the-low-end-flood-to-the-latitude-of-the-daluo-myth_001.html", "kind": "external_chapter_opened", "chapter": "001", "observed_at": "2026-10-27T13:19:54Z", "detail": "Exact scene sequence: three days before Awakening,15years,Daxia,Liu Yingjiao distributing Divine Source to Li Ming1526,Li family Tianhai,Chaos World judged waste. Machine translation varies protagonist Su Xiao/Day/Yang, but official synopsis identifies Su Zhou."}, {"url": "https://www.fanmtl.com/novel/creation-from-the-low-end-flood-to-the-latitude-of-the-daluo-myth.html", "kind": "external_catalog_opened", "detail": "Author见楼,Su Zhou awakens supposedly useless chaos realm; title variant verified."}, {"url": "https://www.fanmtl.com/novel/creation-from-the-low-end-prehistoric-to-the-daluo-myth_70.html", "kind": "external_chapter_indexed", "chapter": "70", "detail": "Alternate English title and same Su Zhou/Pangu/Daluo mythology."}, {"url": "https://wap.faloo.com/new_1111618.html", "kind": "official_catalog", "detail": "Original 创世：从低端洪荒升纬大罗神话 by见楼; Su Zhou苏昼 awakens chaos dismissed as useless; chapter1 chaos,chapter2 Pangu egg,chapter3 3000 gods/Daos."}]', 'reviewed_at': '2026-10-27', 'confirmado': True},
{'video_id': 'nyDV_MLmtag', 'title': 'Level 1 Player', 'aliases': ['Level 1 Player', '1레벨 플레이어'], 'evidence': '[{"timestamp": "00:00–01:06", "detail": "Construction worker supports hospitalized unconscious father; mother and sister also work. Awakens as level1 Choi Hyunseong (ASR Chro Hyansung), low stats and Sell/Buy abilities."}, {"timestamp": "01:53–02:12", "detail": "Shop medicine and books raise strength and grant skills."}, {"timestamp": "02:19–03:34", "detail": "Spending points ages him; selling used console to other-world shopper restores youth, points are lifespan."}] Fontes: [{"url": "https://www.youtube.com/watch?v=nyDV_MLmtag&t=49s", "role": "Public native transcript, name and abilities"}, {"url": "https://www.youtube.com/watch?v=nyDV_MLmtag&t=113s", "role": "Stats through purchased items"}, {"url": "https://www.youtube.com/watch?v=nyDV_MLmtag&t=192s", "role": "Interdimensional sale and age restoration"}, {"url": "https://www.youtube.com/watch?v=nyDV_MLmtag&lc=UgxzvG9NNJgA6-kxnKl4AaABAg", "role": "Uploader pinned comment explicitly names Level 1 Player; expanded description same"}, {"url": "https://tapas.io/series/level-1-player/info", "role": "Official publisher synopsis: Choi Hyunseong, family hardship, cannot level up, interdimensional trading and stat-raising purchases. Exact character and mechanism match."}, {"url": "https://mangalist.com/series/level-1-player/", "role": "Catalog Korean alias 1레벨 플레이어 with HyunSung and Sell/Purchase synopsis"}]', 'reviewed_at': '2026-10-27', 'confirmado': True},
{'video_id': 'OB4HG60j_jw', 'title': 'I Became the Crazy Emperor', 'aliases': ['I Became the Mad Emperor', '미친 황제가 되어버렸다'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=OB4HG60j_jw&t=204s", "timestamp": "03:24–05:19", "details": "Author of Great War of Humans Against Demons contacts devoted reader Ban Kuan, expends final magic to reincarnate him to save world."}, {"url": "https://www.youtube.com/watch?v=OB4HG60j_jw&t=395s", "timestamp": "06:35–07:55", "details": "Wakes as Emperor Exeltrion, dragon blood descendent with madness and murderous voices, villain killed by knight Carl."}, {"url": "https://tapas.io/series/i-became-the-crazy-emperor", "details": "Official synopsis: Park Gwangseok office worker and webnovel reader; author of Great Demon War asks him to save world; wakes on throne as Emperor Axeltrion; murderous urges. Also directly verified via cloud browser official synopsis01:18:01UTC."}, {"url": "https://inkstory.net/content/i-became-the-mad-emperor", "details": "Synopsis same Bang Gwang Suk, novel Human-Demon war, Exceltrion; English/Korean aliases listed. Search excerpt read; directopen cache miss."}]', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'sQmnW0euhyo', 'title': 'The Genius Prismatic Mage', 'aliases': ['Genius Prismatic Mage', 'Genius Wizard who sees Rainbows', 'The Genius Magician Who Sees Rainbows', '무지개를 보는 천재 마법사'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=sQmnW0euhyo&t=12s", "timestamp": "00:12–01:57", "details": "Ray silver-haired orphan in ruined Sector50 trades junk to golem for food, called ghost of17thStreet, sees Ron lies."}, {"url": "https://www.youtube.com/watch?v=sQmnW0euhyo&t=200s", "timestamp": "03:20–04:00", "details": "Ray unable to feel anger or pain, sees mana as colors and emotion vessels in people\'s chests."}, {"url": "https://m.webtoons.com/en/fantasy/the-genius-prismatic-mage/list?title_no=7863", "details": "Official title and Ray orphanSector50, emotionless with mana-color sight."}, {"url": "https://nirvanatales.com/genius-wizard-who-sees-rainbows-chapter-1/", "chapter": 1, "details": "Exact scrap for food golem trade; GhostRay17thStreet and Ron lies; absent anger."}, {"url": "https://www.novellist.co/novels/genius-wizard-who-sees-rainbows", "details": "English and Korean aliases."}]', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'LDDVIOZcFv4', 'title': 'Pick Up a Grimoire, Become a Mage', 'aliases': ['I Picked Up a Grimoire and Became a Wizard', 'Picked Up a Grimoire and Became a Mage', '마도서를 줍다 마법사가 되다'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=LDDVIOZcFv4&t=51s", "timestamps": "00:51–02:17", "method": "Native public YouTube transcript, cloud browser", "details": "Orphan college philosophy major faces expensive textbooks; professor calls him beggar; regrets not studying Arabic; visits used bookstore."}, {"url": "https://www.youtube.com/watch?v=LDDVIOZcFv4&t=155s", "timestamps": "02:35–03:35", "details": "Heavy black iron book, Latin De Vermis Mysteriis rendered as Diverse Mysterious by auto-transcript, changes title into mysteries of insects; crusader held captive in Damascus; owner commands Invisible Vampire."}, {"url": "https://www.youtube.com/watch?v=LDDVIOZcFv4&t=254s", "timestamps": "04:14–05:43", "details": "Yoan pushed by man accompanying girlfriend; wishes him dead; invisible creature raises and tears stranger apart, protagonist flees."}, {"url": "https://www.davarscans.com/novels/pick-up-a-grimoire-become-a-mage/chapter-1", "chapter": 1, "source_type": "Secondary English novel translation", "access": "Direct public chapter text read through cloud browser04:18:47; web open cache miss did not prevent normal browser reading", "details": "Exact sequence: orphan philosophy student, expensive34000won textbook, professor insult, choosing philosophy instead Arabic; secondhand store, iron De Vermis Mysteriis translating to Mysteries of the Worm; Ninth Crusade survivor captivity Damascus, Invisible Vampire familiar; stranger with girlfriend shoves Yohan, death wish, invisible mutilation, escapes into alley. Opening Gyges ring analogy also matches recap00:00–00:33."}, {"url": "https://comic.naver.com/webtoon/list?titleId=855671", "source_type": "Official Korean webtoon publisher", "access": "Direct cloud browser04:18:47", "details": "Official Korean title, creators Seobi53, Mumyeong, original Bangguseok Waryong; synopsis college student finds grimoire at old bookstore, contracts invisible vampire that tears people apart, hides identity and grows as magician."}, {"url": "https://www.novelupdates.com/series/i-picked-up-a-grimoire-and-became-a-wizard/", "source_type": "Secondary catalog", "access": "Indexed search excerpt04:18 only; direct web open04:19 returned403 Forbidden, not bypassed", "details": "I Picked Up a Grimoire and Became a Wizard; associated names Picked Up a Grimoire and Became a Mage, Pick Up a Grimoire Become a Mage, Korean original."}] [\'Identity only; no chapter coverage or final chapter assertion, despite uploader label1-9.\', \'English title and aliases attested in translation/catalog, not claimed licensed English edition.\', \'Video narrative read via native transcript; no independent audio or recap frame comparison.\', \'RoyalRoad indexed synopsis was supplementary only; direct web open404. Naver web parser empty but cloud direct text succeeded.\']', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'PXYb0yST5IA', 'title': '人气至上，我扮演超级天才', 'aliases': ['Popularity Above All: I Play the Role of a Super Genius'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=PXYb0yST5IA&t=15s", "timestamps": "00:15–00:40", "details": "Native public transcript: Miracle selects Thousand Faces; masked Blank challenged, punch breaks mask revealing woman Verse replacing dead brother; victory yields five-star card."}, {"url": "https://www.qidian.com/chapter/1049020186/908709969/", "chapter": 71, "source_type": "Official original publisher; live cloud browser", "details": "Qi Ji/崎寂 punches Su Shi/诉世; mask breaks revealing girl hiding gender; Thousand Faces family, fire wall hides her, fox mask repaired. Matches current video brief recapitulation, not inferred from prior upload."}, {"url": "https://www.qidian.com/chapter/1049020186/908711866/", "chapter": 72, "source_type": "Official original publisher; live cloud browser", "details": "Su Shi loses to Qi Ji and feels she failed dead brother whose life/name she took; livestream reveals sibling backstory. Specific match with current00:24–00:40."}, {"url": "https://completenovel.com/popularity-above-all-i-play-the-role-of-a-super-genius/", "source_type": "Secondary novel catalog", "details": "English alias linked explicitly to Chinese title and author桂月熬糖; popularity system, Qi Ji, anime/live-stream setting. Not asserted licensed English title."}] [\'Native transcript opening and selected first-hour segments inspected; not full3h04 video, no frames or independent audio.\', \'Original publisher chapters71/72 identify opening recap; no chapter coverage or final chapter claimed.\', \'Uploader continuation links are corroboration only. No historical linked videos re-investigated.\']', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': '5VpDjsdeM-M', 'title': 'The Knight King Who Returned with a God', 'aliases': ['신과함께 돌아온 기사왕님'], 'evidence': '[{"url": "https://www.youtube.com/watch?v=5VpDjsdeM-M&t=70s", "timestamps": "01:10–02:16", "source_type": "Native public YouTube transcript in cloud browser", "observed_at": "2026-10-28T07:23:13Z", "summary": "Former Earth orphan dies of overwork; reborn noble Leon. Trains with Gordic (ASR Gothic) at8; leaves16; Arianna chooses him20; king35 after prior king killed by archdemon; emperor\'s sacrifice of3million; last resistance121; destroys last demon gate256; fights until300."}, {"url": "https://www.youtube.com/watch?v=5VpDjsdeM-M&t=154s", "timestamps": "02:34–02:59", "summary": "Black gate in Seoul, Korean Hunters Association ordered in, Han Hari and Kim Jin Su discuss survivor Leon."}, {"url": "https://www.youtube.com/watch?v=5VpDjsdeM-M&t=3493s", "timestamps": "58:13–59:00; 1:00:58–1:01:33", "summary": "Yappy machine interrogates demon with15L holy water; Beatrice Aligiere Spero queen requests Leon kill general. Supplemental character context, not independently chapter-matched."}, {"url": "https://noveltune.net/book/the-knight-king-who-returned-with-a-god-2/1.html", "chapter": "1: You\'re Stuck With Me", "source_type": "Secondary novel translation mirror, not official publisher", "observed_at": "2026-10-28T07:23:48Z", "summary": "Exact sequence: overworked orphan reincarnated Dragonia noble; Gordic tutor8, leaves16, Arianna20, becomes Lionheart king35 after previous king killed by Great Demon; emperor sacrifices3million; final resistance121; last gate destroyed256; meets Earthlings and Hari300. Specific chain confirms work beyond comment/title."}, {"url": "https://series.naver.com/comic/detail.series?productNo=9763831", "source_type": "Official Korean publisher", "observed_at": "2026-10-28T07:24:02Z", "summary": "Canonical Korean title 신과함께 돌아온 기사왕님; author 사람살려., art 전천후마검사; synopsis returning to Earth after300years demon hunting, not alone."}, {"url": "https://asurascans.com/comics/the-knight-king-who-returned-with-a-god-11fe7da3", "source_type": "Secondary English scanlation catalog", "summary": "English title attested. No licensed English edition claimed."}, {"url": "https://manhwatracker.com/comics/the-knight-king-who-returned-with-a-god-317", "source_type": "Secondary catalog", "summary": "Links official Korean series and lists Leon Dragonia Lionheart, Han Hari, Beatrice Aligiere Spero, Yakt Spinner; English title."}] [\'Partial native transcript only (first500 of3377 segments exposed); no full-video claim.\', \'No independent audio/frame comparison.\', \'Novel chapter1 confirms identity, not manhwa coverage or last chapter.\', \'Uploader comment calls it The Knight Who Returned With a God without King; not added as alias solely on uploader authority.\', \'Sheet readback delegated to parent.\']', 'reviewed_at': '2026-10-28', 'confirmado': True},
{'video_id': 'lBqhK53Krc4', 'title': 'My Avatar Is Becoming the Final Boss', 'aliases': ['My Avatar Is Becoming the Final Boss', '我的化身正在成为最终BOSS'], 'evidence': '[{"video_timestamp": "01:24–02:53", "external_chapter": 2, "match": "Infinite Split Game; index finger as cursor; dream and reality option; one initial skill point; C-rated avatar with black restraints and secret family; chooses gray route to escape lab."}, {"video_timestamp": "02:59–03:35", "external_chapter": 3, "match": "No.5 school, wealthy friend invitation at summer break, overlooking city/orphanage, newly created person inserted into history, power persists under suppressant."}] Fontes: ["https://www.youtube.com/watch?v=lBqhK53Krc4&t=84", "https://www.fanmtl.com/novel/6989321_2.html", "https://www.fanmtl.com/novel/6989321_3.html", "https://en-thunderscans.com/comics/my-avatar-is-becoming-the-final-boss/", "https://book.qidian.com/fansrank/1042464636"] English scanlation title, not asserted official; Chinese title corroborated by Qidian indexed author/title page. Video anglicizes Ji Minghuan/Gu Wenyu/Li Qingping as Felix/Julian/Chase; exact ordered scenes establish identity, not assumed name equivalence alone.', 'reviewed_at': '2026-10-26', 'confirmado': True},
{
  "video_id": "hsvLaKV-gy8",
  "title": "The Shepherd Wizard",
  "aliases": [
    "양치기 마법사",
    "Shepherd Wizard"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=hsvLaKV-gy8. [{\"url\":\"https://www.youtube.com/watch?v=hsvLaKV-gy8&t=72s\",\"timestamps\":[\"01:12\",\"01:47\",\"03:19\",\"04:08\",\"04:22\",\"04:36\",\"05:11\",\"05:19\"],\"summary\":\"Shepherd Theo hides magic. Village elder tried to confiscate his sheep after his mother died. Huge black leopard kills elder. Commands Die and Stop fail; shepherd magically strengthens and accelerates a sling stone. Power awakened eight years earlier at age ten; mother ordered secrecy.\"},{\"url\":\"https://www.webnovel.com/ru/book/35534130500905905/95397949831432227\",\"chapter\":\"Prologue\",\"source_type\":\"community translation, not official publisher\",\"summary\":\"Turan on Hisaril Hill; Labus elder formerly tried to seize his sheep after mother died. Rob reports house-sized black leopard. Labus is killed; Turan's Die/Stop commands fail, then a magically hardened and accelerated sling stone kills beast. Ordered scene chain matches video despite localized names.\"},{\"url\":\"https://www.webnovel.com/book/the-shepherd-wizard_35534130500905905/chapter-1_95397946744426496\",\"chapter\":\"Chapter 1\",\"summary\":\"Turan awakened magic at ten, eight years earlier; mother warned him to hide it. Matches video 05:11–05:19.\"},{\"url\":\"https://www.webtoons.com/en/fantasy/the-shepherd-wizard/list?page=3&title_no=10039\",\"source_type\":\"official English publisher\",\"summary\":\"Official title The Shepherd Wizard; protagonist Turan, a shepherd hiding magic on mother's instruction in a world where magic establishes social rank.\"},{\"url\":\"https://www.novelupdates.com/series/shepherd-wizard/\",\"summary\":\"Title and Korean original alias cross-check.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "p2rvqBjf2Jk",
  "title": "直播：开局解密氧气有剧毒",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=p2rvqBjf2Jk. [{\"url\":\"https://www.youtube.com/watch?v=p2rvqBjf2Jk&t=7s\",\"timestamps\":[\"00:07\",\"00:14\",\"00:30\",\"01:29\",\"04:37\",\"05:02\",\"05:54\",\"19:26\"],\"summary\":\"Moon once 50,000 km away and alien observation base; WorldSplitter project took it after 108,000 years of war, pushed it away as meteor shield. ProfessorsClark/Bennett at KeyProjectsInstitute, astronomerQuentyn argues 360,000 km distance. Names localized; main presenterTheo.\"},{\"url\":\"https://m.lrts.me/book/67900348\",\"source_type\":\"official audiobook listing published by 飞卢小说\",\"summary\":\"Title直播：开局解密氧气有剧毒, author飞天揽月, protagonist秦牧. Science TV presenter reveals oxygen toxicity, Shanhaijing as ancient technology manual, mythic Nuwa/Pangu as technological constructs.\"},{\"url\":\"https://www.jpxs123.com/book/7237/40.html\",\"chapter\":\"Text chapters 53–54 (site part 40)\",\"summary\":\"Qin Mu explains Pangu project moved Moon to 360,000 km; Moon was an alien observation base 210 million years ago. Professors 班东临 and 孙智清 at 重点项目研究所 question plan. Nuwa previously cooled Earth’s magma. Specific linked setting matches recap.\"},{\"url\":\"https://www.jpxs123.com/book/7237/41.html\",\"chapter\":\"Text chapters 55–56 (site part 41)\",\"summary\":\"Professors ask why push Moon rather than simply conquer it; answer is Pangu's main purpose: intercept extinction-causing meteorites. Alien lunar observation base and oxygen research recur.\"},{\"url\":\"https://www.jpxs123.com/book/7237/42.html\",\"chapter\":\"Text chapters 56–57 (site part 42)\",\"summary\":\"Pangu's second step is repositioning Moon as Earth's shield against incoming meteors; familiar side faces Earth, cratered side shields it. Matches opening recap 00:14.\"},{\"url\":\"https://www.jpxs123.com/book/7237/43.html\",\"chapter\":\"Text chapters 58–59 (site part 43)\",\"summary\":\"Ancient civilization launches Pangu plan 200 million years ago. War conquering alien Moon base lasts exactly 108,000 years; Pangu represents many people, not one deity. Exact numerical and scene correspondence to video 00:14–00:30.\"},{\"url\":\"https://www.jpxs123.com/book/7237/139.html\",\"chapter\":\"Text chapter 127 (site part 139)\",\"summary\":\"Later callback explicitly states ancient Moon 50,000 km away, Pangu pushed it away, astronomer钱云天 published lunar-origin/Pangu paper. Supports distinctive setting and Quentyn adaptation.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "SMlECRKgbyA",
  "title": "Bloodbath of the Fallen: The Reborn Hero Gron",
  "aliases": [
    "A Mountain of Corpses, A Sea of Blood",
    "尸山血海"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=SMlECRKgbyA. [{\"source\":\"https://www.youtube.com/watch?v=SMlECRKgbyA\",\"method\":\"cloud browser visible transcript\",\"timestamps\":{\"00:00-00:08\":\"Five heroes fight Demon Emperor Samuels; Gron is named among them.\",\"02:44-02:52\":\"Gron defeats emperor; five years later demons honor fallen emperor.\",\"03:21-03:37\":\"Captive awakens and is called a weak demon.\",\"05:55\":\"Gron explicitly realizes he reincarnated as a demon.\",\"07:53\":\"Original body belonged to weak snake-blooded demon.\",\"12:55\":\"Ancient serpent bloodline.\",\"14:14\":\"Serpent Molt enables evolution at next seal.\"}},{\"source\":\"https://tapas.io/episode/3950566\",\"type\":\"official English publisher page, synopsis publicly readable\",\"summary\":\"English title and synopsis match hero dying fighting Demon Emperor, rebirth five years later as weak demon, ancient Serpent God power. Episode 36 content itself not unlocked or inspected.\"},{\"source\":\"https://www.kuaikanmanhua.com/web/topic/26440/\",\"type\":\"official Chinese catalog\",\"summary\":\"尸山血海 names 格隆/Gron, death with Demon Emperor, five-year interval, weakest demon body, ancient snake-god evolution.\"},{\"source\":\"https://en-thunderscans.com/comics/a-mountain-of-corpses-a-sea-of-blood/\",\"type\":\"secondary translation listing\",\"summary\":\"Alias A Mountain of Corpses, A Sea of Blood and exact Gron/premise correspondence.\"}] Confirmado pela transcrição: Gron enfrenta o imperador Samuels (00:00–00:08); após a morte, passam cinco anos (02:44–02:52); renasce no corpo de um demônio fraco (03:21–03:37;05:55) com linhagem de serpente antiga (07:53;12:55). Coincide com sinopses oficiais Tapas e Kuaikan (Gron/格隆, cinco anos, corpo demoníaco e evolução do deus-serpente). Fontes: https://tapas.io/episode/3950566 ; https://www.kuaikanmanhua.com/web/topic/26440/ ; alias inglês adicional em https://en-thunderscans.com/comics/a-mountain-of-corpses-a-sea-of-blood/ . Revisado17/10/2026UTC.",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "L-dHqdQaLEg",
  "title": "贵族游戏",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=L-dHqdQaLEg. [{\"source\":\"https://www.youtube.com/watch?v=L-dHqdQaLEg\",\"method\":\"cloud browser visible Hindi transcript\",\"timestamps\":{\"00:00\":\"Elite academy rule: nobles eat fish cheek meat; back meat marks poor impostors.\",\"00:08-00:24\":\"Four wealthy families select 50 poor students to pretend nobility for one month; exposed students must work without pay 50 years.\",\"00:32-00:55\":\"Delivery boy joins to pay for bedridden mother; entrance with luxury suitcase.\",\"03:19-04:22\":\"Fake blackcard discarded; only three allegedly exist.\",\"04:31-05:09\":\"Names localized Brian and Lucas Sterling.\",\"35:44-37:38\":\"Delivery photographs expose him at party, four heirs defend him; midnight 5 million reward ends story.\"}},{\"source\":\"https://www.998ys.com/video/DLoG4G.html\",\"method\":\"web search retrieved full synopsis; direct open returned Cache miss\",\"summary\":\"Title贵族游戏; exact opening fish cheek rule,50 poor students,four heirs,50 years service,bedridden mother,luxury suitcase.\"},{\"source\":\"https://www.wmlia.com/vod/39017612\",\"method\":\"web search retrieved full synopsis and title\",\"summary\":\"Title贵族游戏, 2026 Chinese urban short drama; same entire distinctive opening sequence.\"},{\"source\":\"https://search.bilibili.com/all?keyword=%E8%B4%B5%E6%97%8F%E4%B9%8B%E5%A3%B0%2F\",\"method\":\"web search index; live web open redirected to unsupported-browser notice\",\"summary\":\"Indexed video title explicitly begins 贵族游戏 and matches fish-cheek rule; uploader 右电2516, duration 1:53:14, date 04-02. Specific video URL not resolved.\"}] Identificação por correspondência específica do enredo, publicada como curta/漫剧 贵族游戏. Transcrição Hindi:00:00 regra de comer somente a bochecha do peixe;00:08–00:24 quatro famílias selecionam50pobres para fingirem nobreza porum mês, com50anos de trabalho gratuito se descobertos;00:32–00:55 entregador participa pela mãe acamada e chega com mala de luxo. Essa sequência coincide com as fichas https://www.998ys.com/video/DLoG4G.html e https://www.wmlia.com/vod/39017612 . Nomes do recap são localizados(Lucas Sterling etc.); autor e alias inglês não confirmados. Revisado17/10/2026UTC.",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "ba9dPSH-Fys",
  "title": "病恋女友",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=ba9dPSH-Fys. [{\"timestamp\":\"00:00–00:38\",\"detail\":\"Delivery worker and nighttime barbecue seller supports terminally ill girlfriend; Rolls-Royce convoy retrieves her as wealthy family's daughter; she calls him caretaker; later he marries her enemy and ex kidnaps him.\"},{\"timestamp\":\"02:51–03:26\",\"detail\":\"Demands 598000 yuan repayment and receives 600000 with 2000 extra.\"},{\"timestamp\":\"05:02–06:06\",\"detail\":\"Barbecue stand outside university; rich woman orders five mutton skewers and ten lamb kidneys.\"},{\"timestamp\":\"38:37–38:46\",\"detail\":\"Marries Liu Ruoyan; ex sentenced to ten years for kidnapping.\"}] [{\"url\":\"https://dj.1dfx.com/v/list.php?book_id=7610625812907183166\",\"method\":\"Indexed full synopsis in web search; direct open failed\",\"match\":\"童景辰 supports 夏知念 with daytime delivery and nighttime barbecue; rich family retrieves her; she calls him caretaker; he reunites with 柳如烟; ex retaliates; lost wealthy-heir identity revealed.\"},{\"url\":\"https://www.youtube.com/watch?v=1qvLGXYVFs8\",\"method\":\"Public indexed Chinese uploader title, published 2026-05-18\",\"match\":\"Explicit title 病恋女友, 夏知念 terminal illness, daytime deliveries, nighttime barbecue, rich cars and illegitimate heiress.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "yWKFmhPfiK4",
  "title": "I Become a God in Twelve Days, and the Whole World Is Hunting Me",
  "aliases": [
    "十二天后成神，我被全世界追杀"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=yWKFmhPfiK4. [{\"timestamp\":\"00:00–00:16\",\"kind\":\"direct YouTube transcript\",\"observation\":\"Ryan Quinn is a nineteen-year-old orphan, bound to a twelve-talisman system. Surviving twelve days brings godhood; hourly location broadcasts expose him, and whoever kills him personally inherits the system.\",\"external_match\":\"The official Qidian synopsis names 林羽, transported to a world without supernatural powers, gaining a talisman for each day survived. Twelve talismans yield godhood. The system announces him globally, reveals coordinates each hour, and transfers talisman power to his personal killer.\",\"strength\":\"Very distinctive rule-set match\"},{\"timestamp\":\"00:16–00:32\",\"kind\":\"direct YouTube transcript\",\"observation\":\"Escape by turning into a bird, citywide special-agent spraying and use of a soldier's hazmat suit while invisible; at midnight on day three he receives the pig talisman's laser power.\",\"external_match\":\"Qidian synopsis explicitly places pig-talisman laser eyes on day three. Its public catalog includes preceding citywide nerve-agent spraying, monkey-talisman escape, and midnight talisman-fusion chapters.\",\"strength\":\"Specific power plus exact day and matching preceding sequence\"},{\"timestamp\":\"00:32–01:19\",\"kind\":\"direct YouTube transcript\",\"observation\":\"Commanders arrange missile destruction of Bayshore/Beayshore City, other countries object and eventually consent, and special teams are told to withdraw.\",\"external_match\":\"Qidian catalog chapter 27 concerns requesting missile bombardment and the necessity of killing 林羽; chapter 28 immediately follows with pig-talisman laser-eye killing.\",\"strength\":\"Current video opening matches public chapter sequence\"},{\"timestamp\":\"01:19–02:44\",\"kind\":\"direct YouTube transcript\",\"observation\":\"Streamer Luna, addressed as Miss Sloan, is evacuated by bodyguards. They end her stream and tell her the city will be hit by an intercontinental missile in fifteen minutes.\",\"external_match\":\"Supporting specific narrative detail captured for future comparison. This run did not independently verify the original Chinese name of Luna.\",\"strength\":\"Direct narrative evidence; not an independently matched name\"},{\"timestamp\":\"01:51–02:21\",\"kind\":\"direct YouTube transcript\",\"observation\":\"The snake talisman provides invisibility, the monkey talisman shape-shifting, and the new pig talisman laser beams.\",\"external_match\":\"Official synopsis independently confirms snake invisibility and day-three pig laser eyes; official catalog explicitly includes monkey talisman and subsequent laser-eye chapters.\",\"strength\":\"Distinctive named powers\"},{\"timestamp\":\"04:17–04:38\",\"kind\":\"direct YouTube transcript\",\"observation\":\"After two days hiding, Ryan retaliates before leaving, firing red eye lasers with the pig talisman at elite soldiers.\",\"external_match\":\"The publisher's day-three synopsis says the protagonist has hidden for two days and now demonstrates pig-talisman laser eyes; public chapter 28 is specifically about that attack.\",\"strength\":\"Near scene-level correspondence beyond generic premise\"},{\"timestamp\":\"55:03\",\"kind\":\"direct YouTube transcript\",\"observation\":\"The ending announces a new unfamiliar host and satellite coordinates after the twelve-talisman aftermath.\",\"external_match\":\"Recorded as video evidence only. No claim that this ending or adaptation completion matches the source novel's present publication state.\",\"strength\":\"Direct closing narrative only\"}] Fonte oficial: https://www.qidian.com/book/1050573847/. English title is a translation/catalog label, not a verified licensed edition.",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "U-k_Mr8q1sk",
  "title": "Global Beast Tamer: I Can See Evolution Paths",
  "aliases": [
    "Global Beast Tamer: I Can See the Path of Evolution",
    "Beast Taming: I Can See the Evolution Paths",
    "全球御兽：我能看见进化路线"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=U-k_Mr8q1sk. [{\"time\":\"00:00–00:14\",\"seconds\":0,\"url\":\"https://www.youtube.com/watch?v=U-k_Mr8q1sk&t=0s\",\"observation\":\"Teacher announces tomorrow’s beastmaster qualification exam, advises rest and preparation, then dismisses class.\",\"matches\":\"Official WebComics chapter 1 opening classroom scene.\"},{\"time\":\"00:30–00:38\",\"seconds\":30,\"url\":\"https://www.youtube.com/watch?v=U-k_Mr8q1sk&t=30s\",\"observation\":\"A student targets an average beastmaster academy, admitting a top-tier school is beyond him.\",\"matches\":\"Official chapter 1 visually repeats this distinctive sequence; its localized city name is Northvale.\"},{\"time\":\"02:23–02:31\",\"seconds\":143,\"url\":\"https://www.youtube.com/watch?v=U-k_Mr8q1sk&t=143s\",\"observation\":\"Classmates mock Little Snowball and suggest its owner sell ice cream.\",\"matches\":\"Snowball is the supposedly useless initial beast in both official summaries.\"},{\"time\":\"03:30–04:39\",\"seconds\":210,\"url\":\"https://www.youtube.com/watch?v=U-k_Mr8q1sk&t=210s\",\"observation\":\"Snowball has 23.48% growth. Hidden giant and queen routes appear; queen leads through ice crystal spirit toward king rank.\",\"matches\":\"The novel listing explicitly identifies the queen route, king-level potential and ice-crystal evolution.\"},{\"time\":\"07:52–08:25\",\"seconds\":472,\"url\":\"https://www.youtube.com/watch?v=U-k_Mr8q1sk&t=472s\",\"observation\":\"Snowball becomes a small blue humanoid, gains ice skills, and can next evolve into a snow maiden.\",\"matches\":\"Official summaries connect Snowball to Ice Queen; the novel lists the intermediate ice-crystal and snow-girl forms.\"},{\"time\":\"10:24–10:47\",\"seconds\":624,\"url\":\"https://www.youtube.com/watch?v=U-k_Mr8q1sk&t=624s\",\"observation\":\"Guan Ning is named as a prominent student and the protagonist’s cousin.\",\"matches\":\"The same titled novel names Guan Ning and Lin Ze as its main characters.\"}] [{\"type\":\"official_english_listing\",\"url\":\"https://webcomicsapp.com/en/fantasy/global-beast-tamer-i-can-see-evolution-paths/6939144c62661d0fdb443f85\",\"verified_via\":\"web search/open\",\"finding\":\"Names the work Global Beast Tamer: I Can See Evolution Paths and credits Copy Lemon + Manga Fish. Synopsis specifically joins transmigration, a supposedly unevolvable Snowball, a system revealing hidden evolution routes, and Ice Queen.\"},{\"type\":\"official_original_listing\",\"url\":\"https://www.kuaikanmanhua.com/web/topic/24602/\",\"verified_via\":\"web open\",\"finding\":\"Confirms native title and original-story/art credits. Chinese synopsis independently links 小雪球 (Little Snowball), hidden evolutionary routes, and 冰雪女皇 (Ice/Snow Queen).\"},{\"type\":\"official_chapter_direct_visual\",\"url\":\"https://webcomicsapp.com/en/fantasy/global-beast-tamer-i-can-see-evolution-paths/1/6939144c62661d0fdb443f85\",\"verified_via\":\"cloud browser screenshots\",\"finding\":\"Chapter 1 visibly contains the teacher advising students to rest and prepare for good results, followed by a student boasting that an average academy is achievable while a top-tier academy is not; a subsequent panel introduces the impending beast-tamer qualification assessment. These ordered opening scenes match the video transcript.\",\"caveat\":\"Official English city naming is localized (Northvale), unlike the transcript’s phonetically rendered name. No exact name equivalence is asserted.\"},{\"type\":\"independent_bibliographic_listing\",\"url\":\"https://anilist.co/manga/192159/\",\"verified_via\":\"web search\",\"finding\":\"Maps the preferred English title and I Can See the Path of Evolution alias to the same Chinese title; identifies the adaptation as Chinese manga/manhua with web-novel source.\"},{\"type\":\"secondary_novel_listing\",\"url\":\"https://wtr-lab.com/en/novel/29147/global-beast-tamer-i-can-see-the-path-of-evolution\",\"verified_via\":\"web open\",\"finding\":\"Identifies Lin Ze and Guan Ning as the main characters. Describes queen-route king-level potential and the chain from Little Snowball through Ice Crystal Soul, Snow Girl and later queen forms. Used for character/mechanics corroboration, not as the sole title authority.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "5RlOBNv7c6U",
  "title": "The Evil Alchemist Can't Handle His Own Experiment",
  "aliases": [
    "The Evil Alchemist Can't Handle His Own Experimental Subject"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=5RlOBNv7c6U. [{\"timestamp\":\"00:27\",\"seconds\":27,\"url\":\"https://www.youtube.com/watch?v=5RlOBNv7c6U&t=27s\",\"observation_paraphrase\":\"The protagonist, auto-transcribed as Isa, is the last heir of an alchemist lineage and plans to create an exceptional biological weapon.\",\"matches\":[\"Isao/Aesop, alchemist descendant\",\"biochemical weapon creation\"]},{\"timestamp\":\"02:39\",\"seconds\":159,\"url\":\"https://www.youtube.com/watch?v=5RlOBNv7c6U&t=159s\",\"observation_paraphrase\":\"Isao explains that saving an injured woman serves his plan to create a supreme biological weapon, then implants unusual materials into her.\",\"matches\":[\"Experiment using injured woman as the base\",\"Ultimate Calamity premise\"]},{\"timestamp\":\"06:00\",\"seconds\":360,\"url\":\"https://www.youtube.com/watch?v=5RlOBNv7c6U&t=360s\",\"observation_paraphrase\":\"The rat companion is named Cheese.\",\"matches\":[\"Named rat companion Cheese\"]},{\"timestamp\":\"11:23\",\"seconds\":683,\"url\":\"https://www.youtube.com/watch?v=5RlOBNv7c6U&t=683s\",\"observation_paraphrase\":\"The high-risk experimental subject associated with the black plague is named Lucille. At 11:38–11:53, Isao says a newly created disaster has replaced her as his strongest subject.\",\"matches\":[\"Lucille as Dark Plaguebreed experimental subject\",\"Lucille formerly strongest subject before Cole\"]}] [{\"url\":\"https://manga.bilibili.com/m/detail/mc34355\",\"title\":\"邪恶炼金术士搞不定自己的实验体\",\"type\":\"official publisher/platform catalog\",\"verification\":\"Successfully opened in the cloud browser on 2026-10-17 at approximately 19:17:49–19:18:02 UTC.\",\"supports\":\"Native title, creator credits 云海鲸歌文化 / 犁墨刀, alchemist-created biochemical weapon premise, and Lucille extra chapter 番外-露西尔.\"},{\"url\":\"https://dragontea.ink/novel/the-evil-alchemist-cant-handle-his-own-experimental-subject/\",\"title\":\"The Evil Alchemist Can’t Handle His Own Experimental Subject\",\"type\":\"English title and synopsis reference\",\"verification\":\"Public web result and direct page open succeeded.\",\"supports\":\"Aesop, descendant of Persilade alchemist family, attempts to create Ultimate Calamity and the experiment fails. Aesop and Isao are translation variants; the independently matching premise and Lucille remove ambiguity.\"},{\"url\":\"https://the-evil-alchemist-cant-handle-his-own-experiment.fandom.com/wiki/Lucille\",\"title\":\"Lucille | The Evil Alchemist Can’t Handle His Own Experiment Wiki\",\"type\":\"specific character reference\",\"verification\":\"Search result returned the character entry text. Direct web open returned an internal error, so the character content is search-index evidence.\",\"supports\":\"Lucille is a human mutant created by Isao Persilarde, Dark Plaguebreed, and was his strongest experimental subject until Cole.\"},{\"url\":\"https://www.wmanhua.com/comic/2634.html\",\"title\":\"邪恶炼金术士搞不定自己的实验体\",\"type\":\"native-language synopsis reference\",\"verification\":\"Public web result returned synopsis.\",\"supports\":\"伊索 of 佩尔西拉德 creates 最终灾厄; same alchemist lineage and weapon premise.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "SDe-jgaZ9As",
  "title": "A Regressor's Tale of Cultivation",
  "aliases": [
    "회귀수선전(回歸修仙傳)",
    "回歸修仙傳",
    "Regressor’s Tale of Cultivation",
    "ARTOC",
    "RToC"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=SDe-jgaZ9As. [{\"timestamp\":\"00:30\",\"seconds\":30,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=30s\",\"observation_paraphrase\":\"The protagonist has spent fifty years in a martial-arts world after traveling to a company workshop with Director Kim and colleagues.\",\"matches\":[\"Company workshop group\",\"Fifty-year first life\"]},{\"timestamp\":\"00:37\",\"seconds\":37,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=37s\",\"observation_paraphrase\":\"A landslide struck their vehicle before they awakened in a supernatural cultivation world.\",\"matches\":[\"Landslide transporting company coworkers\"]},{\"timestamp\":\"01:23\",\"seconds\":83,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=83s\",\"observation_paraphrase\":\"The immortals take the talented coworkers while the protagonist and Director Kim remain behind. Director Kim later becomes an exceptional martial artist.\",\"matches\":[\"Seo Eun-hyun and Kim Young-hoon left behind\",\"Kim Young-hoon’s martial talent\"]},{\"timestamp\":\"03:26–04:07\",\"seconds\":206,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=206s\",\"observation_paraphrase\":\"After dying, the hero wakes young beside his original coworkers and realizes that his ability returns him to that point after death.\",\"matches\":[\"Death triggers regression to first arrival\"]},{\"timestamp\":\"04:56–05:12\",\"seconds\":296,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=296s\",\"observation_paraphrase\":\"The transcript renders the protagonist’s name as Seong An Hun / Sean Hune and describes his hostile department head.\",\"matches\":[\"Seo Eun-hyun, with auto-transcription variation\"]},{\"timestamp\":\"08:10–08:27\",\"seconds\":490,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=490s\",\"observation_paraphrase\":\"Director Kim intervenes after the fight; the protagonist recalls that he will become a top martial artist. The auto-transcript varies his name as Kim and Hong / Kim Hyun.\",\"matches\":[\"Kim Young-hoon and his exceptional martial development\"]}] [{\"url\":\"https://server.haksanpub.co.kr/bbs/board.php?bo_table=m03_04&wr_id=149\",\"title\":\"회귀수선전\",\"type\":\"official publisher synopsis\",\"verification\":\"Public web search returned full publisher synopsis. Direct web and cloud-browser open failed; browser showed 502 Bad Gateway.\",\"supports\":\"Seven colleagues are caught in a landslide on a company workshop trip; Seo Eun-hyun receives no special po…42228 tokens truncated… 'comparação de painéis ou capítulo final confirmado. '
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


REVIEWED.append({'video_id': '5cmZ9dfEUv8',
 'title': 'Solo Glitch Player',
 'aliases': ['Solo Bug Player', 'Bug Player', '나 홀로 버그로 꿀빠는 플레이어'],
 'evidence': 'Manhwa identificado pela transcrição pública deste vídeo, lida na interface do '
             'YouTube em 14/10/2026, pela sinopse oficial e por sequência específica do '
             'episódio 2 oficial da Tapas, Demon Spirit Isabella. Em 0:16–2:04, o jogador '
             'Taepung Shin desperta como o obeso Jared dentro de Paradiso e planeja explorar '
             'seu conhecimento dos bugs; nomes e situação correspondem à sinopse licenciada. '
             'A legenda automática varia Shintaong/Shinte Pong e Paradise, e chama Jared de '
             'rei onde a sinopse diz senhor; essas variantes não são aliases. Em 5:24–6:40, '
             'Jared pede o olho espiritual para ler atributos e recrutar pessoas; Isabella '
             'exige o que ele tem de mais precioso, ameaça devorar sua família e aplica uma '
             'maldição que toma aquilo em que ele pensa. Seus lábios se embeicam e Jared '
             'explica ter pensado no primeiro beijo. No episódio 2 da Tapas, inspecionado '
             "visualmente em acesso público, Mind's Eye mostra atributos/disposição, Jared o "
             'usa para gerir seu território e recrutar talentos, Isabella exige a coisa mais '
             'importante, ameaça comer sua família, e a maldição que lê seu pensamento é '
             'seguida pelos lábios embeicados e pela explicação de Jared sobre explorar o '
             'contrato. A combinação e a ordem dessas cenas confirmam a obra além da '
             'premissa. Solo Glitch Player é o título inglês oficial licenciado na Tapas; o '
             'original coreano é atestado em resultado indexado da KakaoPage. Solo Bug Player '
             'e Bug Player são aliases atestados em catálogos, usados somente para variantes, '
             'não como prova da identificação ou licença. Comparação da transcrição com '
             'painéis oficiais externos; sem frames do próprio recap, escuta independente ou '
             'capítulo final confirmado. Episódio oficial aberto sem login ou desbloqueio. '
             'https://www.youtube.com/watch?v=5cmZ9dfEUv8&t=16s '
             'https://www.youtube.com/watch?v=5cmZ9dfEUv8&t=324s '
             'https://tapas.io/series/solo-glitch-player/info '
             'https://tapas.io/episode/2174217 https://page.kakao.com/content/54748024 '
             'https://www.novellist.co/novels/bug-player https://atsu.moe/manga/twmm0',
 'reviewed_at': '2026-10-14',
 'confirmado': True})


REVIEWED.append({'video_id': 'tU3BtM7NAoI',
 'title': '玄幻：女帝退婚，我反手夺她机缘',
 'aliases': [],
 'evidence': 'Novel chinesa identificada pela transcrição nativa do vídeo exato, lida na '
             'interface do YouTube em 14/10/2026, e por múltiplas sequências específicas dos '
             'capítulos 1, 2, 7 e 30, lidos diretamente no leitor secundário Novel543. Em '
             '0:00–0:45 e 1:15–2:43, Bai Ruoxue pede a certidão de casamento e oferece '
             'pílulas no portão externo da Cloud Heaven Sect; Song Qing, filho do grande '
             'ancião, carrega um leque. Su Jiuge, filho do Príncipe de Yan, começou a '
             'cultivar aos oito e enfrenta expulsão após dez anos como discípulo externo; o '
             'noivado protegeu Bai depois de uma disputa política contra sua família. A ordem '
             'e os detalhes correspondem ao capítulo 1. Em 4:45–5:19, Su diz que a certidão '
             'está na propriedade paterna, recebe o frasco, reconhece no fundo o brasão da '
             'própria família e vai ao mercado, como no capítulo 2. Em 5:35–6:39 e 7:04–7:27, '
             'recusa sangue de serpente quase de segundo nível por três pedras, compra cinco '
             'frascos de sangue comum mais um osso por seis pedras e rouba a oportunidade do '
             'Osso do Imperador de Bai: recompensa de 10.000 vezes, Osso Supremo com Mão dos '
             'Céus, também no capítulo 2. Em 16:43–18:26, afasta Ye Feng da biblioteca, '
             'encontra uma folha quase transparente no manual de condução dos cinco elementos '
             'e obtém o fragmento de absorção estelar, convertido por recompensa de 1.000 '
             'vezes na arte de devorar espírito de Taotie; retira um manual comum como '
             'disfarce, por uma pedra para três dias, como no capítulo 7. O recap situa a '
             'folha na encadernação; a fonte, numa página em camadas. Em 1:19:28–1:23:06, Su '
             'supera Bai nos degraus de jade; Fang Yuan ganha as apostas dos anciãos após '
             'cinco sinos; oito superam Xiao Shiyi, nove espantam o mestre Ye Teng durante o '
             'chá e o décimo consagra Su, como no capítulo 30. As legendas automáticas '
             'apresentam variantes fonéticas; os nomes foram normalizados pelo texto chinês, '
             'sem tratá-las como aliases. Título original e autoria de 青山与浊酒 são atestados em '
             'fonte secundária; nenhuma página oficial detalhada da obra nem edição inglesa '
             'licenciada foi verificada. O rótulo inglês do WTR-LAB é tradução automática, '
             'não título licenciado, e foi omitido dos aliases. Comparação de transcrição com '
             'capítulos externos: sem frames utilizáveis do próprio vídeo, escuta '
             'independente ou capítulo final confirmado. '
             'https://www.youtube.com/watch?v=tU3BtM7NAoI&t=0s '
             'https://www.youtube.com/watch?v=tU3BtM7NAoI&t=285s '
             'https://www.youtube.com/watch?v=tU3BtM7NAoI&t=335s '
             'https://www.youtube.com/watch?v=tU3BtM7NAoI&t=1003s '
             'https://www.youtube.com/watch?v=tU3BtM7NAoI&t=4768s '
             'https://www.novel543.com/1016606165/ '
             'https://www.novel543.com/1016606165/8096_1.html '
             'https://www.novel543.com/1016606165/8096_2.html '
             'https://www.novel543.com/1016606165/8096_2_2.html '
             'https://www.novel543.com/1016606165/8096_7.html '
             'https://www.novel543.com/1016606165/8096_30.html '
             'https://www.novel543.com/1016606165/8096_30_2.html '
             'https://wtr-lab.com/en/novel/44267/fantasy-the-empress-breaks-off-the-engagement-i-turn-the-tables-and-seize-her-opportunity',
 'reviewed_at': '2026-10-14',
 'confirmado': True})


REVIEWED.append({'video_id': 'e2UKl3SoGmA',
 'title': 'Error D Echo',
 'aliases': ['Error: The Echo', 'Error The Echo', 'Error de Echo', '에러 디 에코'],
 'evidence': 'Manhwa identificado pela transcrição nativa deste vídeo, lida na interface '
             'do YouTube em 14/10/2026, e por sequência específica de painéis do capítulo '
             '2, inspecionados diretamente na Thunderscans. A descrição do próprio vídeo '
             'fornece Error: The Echo / Error de Echo. Em 3:51–4:06, uma mulher de luvas '
             'resgata o protagonista e cobre sua boca; ele reconhece a semelhança com '
             'Seline/Celine. Em 4:06–4:27, ela lança uma pedra para desviar o monstro, '
             'pede que ele se afaste e explica que a criatura não tem olhos e caça pelo '
             'som. Os painéis do capítulo 2 mostram, na mesma ordem, o protagonista '
             'chamando-a de C-CELINE, a mão enluvada sobre sua boca, a pedra arremessada, '
             'a criatura seguindo o ruído, o pedido para ele se afastar e a explicação de '
             'que ela rastreia pelo som e não tem olhos. A combinação específica confirma '
             'a obra além da premissa. O título coreano 에러 디 에코 e a autoria de 순수 são '
             'atestados na editora Naver e no cartão do capítulo. Error D Echo é o título '
             'da scanlation; Error: The Echo e Error de Echo são variantes da descrição do '
             'canal; Error The Echo é título de catálogo atestado em resultado indexado do '
             'AniList, cuja abertura direta falhou. Não foi estabelecida edição inglesa '
             'oficial licenciada. Comparação de transcrição real com painéis externos; o '
             'player do recap não forneceu frames utilizáveis. Sem escuta independente ou '
             'capítulo final da compilação confirmado. '
             'https://www.youtube.com/watch?v=e2UKl3SoGmA&t=231s '
             'https://www.youtube.com/watch?v=e2UKl3SoGmA&t=246s '
             'https://en-thunderscans.com/comics/error-d-echo/ '
             'https://en-thunderscans.com/error-d-echo-chapter-2/ '
             'https://m.comic.naver.com/webtoon/list?titleId=854335&week=fri '
             'https://anilist.co/manga/217286/Error-The-Echo/',
 'reviewed_at': '2026-10-14',
 'confirmado': True})


REVIEWED.append({'video_id': 's1FgEmcxJ8U',
 'title': 'Necromancer, the Ultimate Scourge!',
 'aliases': ['Disastrous Necromancer', 'Catastrophic Necromancer'],
 'evidence': 'Manhua identificado pela transcrição nativa deste vídeo, lida na interface '
             'do YouTube em 14/10/2026, e por sequência específica de painéis do episódio '
             '1 oficial da WEBTOON. Em 0:08–0:24, a narração nomeia Lin Moyu e descreve '
             'seu teste de ataque concluído em 0,1 segundo. Em 0:34–1:14, a cerimônia '
             'passa por profissões de fazendeiro e cozinheiro, Gao Yang como cavaleiro de '
             'espada e escudo, Xia Xue como maga elemental rara e Lin despertando como '
             'necromante de profissão oculta e única, sob nuvens escuras, raios e '
             'manifestação de mortos-vivos. Nos painéis oficiais inspecionados, Xia Xue é '
             'nomeada e ganha a profissão rara de maga elemental; em seguida há tempestade '
             'e manifestação de morto-vivo, e os diálogos identificam Lin Moyu com '
             'profissão oculta e única, o único necromante desse mundo. Nomes, classes e '
             'ordem do despertar confirmam a correspondência além da premissa genérica. '
             'Variações automáticas Lin/Lynn e Shashia/Xia Xue não são aliases. '
             'Necromancer, the Ultimate Scourge! é o título inglês oficial da WEBTOON, '
             'creditado a Kuaikan Comics. Disastrous Necromancer e Catastrophic '
             'Necromancer são variantes atestadas em resultado indexado do catálogo '
             'AniList; a abertura direta desse catálogo falhou. Catastrophic Necromancer '
             'também é o título oficial da edição francesa da WEBTOON, cuja sinopse nomeia '
             'Lin Moyu. A transcrição obtida é parcial, de 0:00 a 1:03:18 de um recap de '
             '14:20:40; player preto/carregando, sem frames utilizáveis nem escuta '
             'independente. Comparação com o episódio 1 da edição WEBTOON, sem equiparar '
             'numerações de outras edições, confirmar capítulo 185 ou o capítulo final da '
             'compilação. https://www.youtube.com/watch?v=s1FgEmcxJ8U&t=8s '
             'https://www.youtube.com/watch?v=s1FgEmcxJ8U&t=34s '
             'https://www.webtoons.com/en/action/necromancer-the-ultimate-scourge/list?title_no=9767 '
             'https://www.webtoons.com/en/action/necromancer-the-ultimate-scourge/episode-1/viewer?episode_no=1&title_no=9767 '
             'https://anilist.co/manga/167372 '
             'https://www.webtoons.com/fr/action/catastrophic-necromancer/list?title_no=6587',
 'reviewed_at': '2026-10-14',
 'confirmado': True})


REVIEWED.append({'video_id': 'dYGhHtY-IiU',
 'title': "A Regressor's Tale of Cultivation",
 'aliases': ['회귀수선전', '回歸修仙傳'],
 'evidence': 'Identificação pela transcrição nativa do vídeo exato, lida na interface do '
             'YouTube em 15/10/2026, e por sequência específica do capítulo 2 do '
             'romance-base. Em 5:05–6:15, Seo oferece o próprio braço a uma raposa para '
             'proteger os colegas; espera que cultivadores cheguem em dois dias para curá-lo, '
             'usa ervas analgésicas preparadas e recebe sete dias de abrigo. No capítulo '
             'externo, Seo Eun-hyun entrega o braço esquerdo, calcula a mesma chegada em dois '
             'dias, mastiga ervas previamente colhidas e obtém sete noites de permanência; '
             'Diretor Kim o socorre. A ordem e os detalhes confirmam a obra além da premissa '
             'de regressão. A edição inglesa oficial da WEBTOON estabelece o título A '
             "Regressor's Tale of Cultivation e os créditos KIM MuHyeon e Amazing. O título "
             'coreano 회귀수선전 foi lido na página oficial NAVER; 回歸修仙傳 consta como variante nos '
             'metadados secundários de Thunderscans/NovelUpdates. A transcrição cobre '
             '0:00–1:41:55 de um vídeo de 1:42:05 e contém erros fonéticos nos nomes. O '
             'player permaneceu em 0:00: sem frames reproduzíveis nem escuta independente. A '
             'correspondência com capítulos do romance não estabelece capítulos da adaptação; '
             'a alegação 1–33 do uploader e o capítulo final do recap permanecem não '
             'verificados. https://www.youtube.com/watch?v=dYGhHtY-IiU&t=305s '
             'https://wetriedtls.com/series/a-regressors-tale-of-cultivation/chapter-2 '
             'https://www.webtoons.com/en/action/a-regressors-tale-of-cultivation/list?title_no=8795 '
             'https://comic.naver.com/webtoon/list?titleId=839827 '
             'https://en-thunderscans.com/comics/a-regressors-tale-of-cultivation/ '
             'https://www.novelupdates.com/series/a-regressors-tale-of-cultivation/',
 'reviewed_at': '2026-10-15',
 'confirmado': True})


REVIEWED.append({'video_id': '02K93Sf5l2g',
 'title': 'By Changing One Word in My Skills, I Broke Everything',
 'aliases': ['I Turn Skills Into Broken Ones With a Single Word', '技能改一个字，他们被我玩坏了'],
 'evidence': 'Manhua identificado pela descrição e transcrição nativas deste vídeo exato, '
             'lidas na interface do YouTube em 15/10/2026, por fontes externas e pelo início '
             'do capítulo 1. A descrição informa I Turn Skills Into Broken Ones With a Single '
             'Word. Em 0:08–0:17, o protagonista regressa ao dia do despertar num ônibus com '
             'concluintes; a cidade tem dois anos e meio restantes. Em 1:09–1:40, Rewrite '
             'altera um caractere em habilidades ou equipamentos; poderosos o exploram e '
             'aprisionam, um dragão de nível 96 o ataca e Revive vira Rebirth, levando-o aos '
             'dezoito anos. Jiang Yan é nomeado em 2:22; desperta Repairman F em 2:43–2:57 e '
             'Farmer F em 3:07–3:16. As fichas do manhua em Elf Toon e Raven Scans atestam os '
             'títulos inglês e chinês, Jiang Yan, exploração e regressão. A ficha MTL do '
             'romance-base no WTR-LAB confirma a combinação rara das duas profissões F, '
             'alteração textual e monstro de nível 96. Os rótulos de habilidades diferem: o '
             'recap usa Revive→Rebirth e Growth Boost→Regeneration; isso não cria novos '
             'aliases. As imagens 1/16 e 2/16 do leitor Elf Toon foram inspecionadas: título '
             'chinês, alunos concluintes de Nanrong no dia do despertar, ônibus e '
             'protagonista surpreso. O recap traduz o lugar como Southgrove. Transcrição '
             'obtida até 1:46:20 de um vídeo de 1:46:25. Comparação de transcrição com '
             'painéis externos, sem correspondência pixel a pixel com frames do recap, escuta '
             'independente ou capítulo final confirmado. Contadores do leitor e divisões da '
             'transcrição não estabelecem paginação ou cobertura de capítulos. O título MTL '
             'da novel não foi adotado como alias do quadrinho. '
             'https://www.youtube.com/watch?v=02K93Sf5l2g&t=8s '
             'https://www.youtube.com/watch?v=02K93Sf5l2g&t=69s '
             'https://www.youtube.com/watch?v=02K93Sf5l2g&t=142s '
             'https://www.youtube.com/watch?v=02K93Sf5l2g&t=163s '
             'https://www.youtube.com/watch?v=02K93Sf5l2g&t=187s '
             'https://elftoon.net/series/comic/by-changing-one-word-in-my-skills-i-broke-everything '
             'https://elftoon.net/series/comic/by-changing-one-word-in-my-skills-i-broke-everything/chapter/1 '
             'https://ravenscans.org/manga/i-turn-skills-into-broken-ones-with-a-single-word/ '
             'https://wtr-lab.com/en/novel/75862/i-changed-one-word-in-the-skill-and-they-were-ruined-by-me',
 'reviewed_at': '2026-10-15',
 'confirmado': True})


REVIEWED.append({'video_id': 'FBaT88GUuaI',
 'title': "Goblin's Ascent: From Loser to Winner",
 'aliases': ['From Goblin to Goblin God',
             "Goblin's Life Simulator",
             'Cong Ge Bu Lin Dao Ge Bu Lin Shen',
             '从哥布林到哥布林神'],
 'evidence': 'Manhua identificado pela transcrição nativa do vídeo exato, lida no YouTube em '
             '15/10/2026, e por painéis do capítulo 1 oficial da WebComics. Em 0:38–1:05, '
             'após a morte do chefe, goblins disputam a sucessão mordendo narizes, avançam '
             'contra a cativa e são repelidos por seu protetor armado. A mesma abertura '
             'ordenada aparece nas imagens 1–18 do leitor oficial. Em 2:11–3:06, um cavaleiro '
             'muito forte ataca a garota, o protagonista a protege e uma mulher interrompe o '
             'golpe com barreira dourada. Nos painéis oficiais inspecionados, o goblin '
             'estranha o poder do cavaleiro, cogita um engano devido à escuridão e a mulher '
             'manda Rodell esperar enquanto surge a barreira. São correspondências narrativas '
             'específicas, além da premissa genérica de reencarnação. A WebComics publica o '
             "título Goblin's Ascent: From Loser to Winner e localiza o protagonista como "
             'Jace Hurley e o cavaleiro como Rodell; o recap usa Lin Tian/Lintian e '
             'Loder/Loader. ManhuaPlus e a ficha previamente verificada de Anime-Planet '
             'atestam os aliases inglês, romanizado e chinês. A transcrição cobre '
             '0:00–4:39:00; player indica 4:39:05 e a planilha 4:39:06. Não houve frames '
             'utilizáveis do próprio recap nem escuta independente. Números de imagens são '
             'posições do leitor, não páginas editoriais. O comentário fixado do uploader não '
             'é a base da confirmação. A comparação adicional do final com o romance, '
             'capítulos 141–142 na tradução Etude, não estabelece capítulo final nem '
             'intervalo do quadrinho. https://www.youtube.com/watch?v=FBaT88GUuaI&t=38s '
             'https://www.youtube.com/watch?v=FBaT88GUuaI&t=131s '
             'https://webcomicsapp.com/en/fantasy/goblin-s-ascent-from-loser-to-winner/1/67e20b7662661d12a148fa62 '
             'https://webcomicsapp.com/en/fantasy/goblin-s-ascent-from-loser-to-winner/67e20b7662661d12a148fa62 '
             'https://manhuaplus.org/manga/from-goblin-to-goblin-god '
             'https://www.anime-planet.com/manga/goblins-ascent-from-loser-to-winner '
             'https://etudetranslations.com/novel/from-goblin-to-goblin-god/chapter-141/ '
             'https://etudetranslations.com/novel/from-goblin-to-goblin-god/chapter-142/',
 'reviewed_at': '2026-10-15',
 'confirmado': True})


REVIEWED.append({'video_id': 'UrS-eHTg72g',
 'title': '死亡亿次，我复制天赋杀穿万族！',
 'aliases': ['After Billions of Deaths: I Copy Talents and Slaughter All Races!',
             'After dying billions of times, I copied my talents and killed all races!'],
 'evidence': 'Romance identificado pela descrição expandida do vídeo exato, lida no YouTube '
             'em 15/10/2026, e por correspondências específicas com capítulos externos. O '
             'diário enviado pelo próprio protagonista dez anos no futuro, a habilidade EX '
             'Death Copy e um colega que concede retorno exato de doze horas correspondem ao '
             'início e ao capítulo 3 do original; Book of Wisdom corresponde ao capítulo 7. '
             'A descrição também reúne morte por uma raposa com controle mental, Eye of '
             'Truth, Healing Light, Super Senses, controle elemental e linhagem, combinação '
             'encontrada no capítulo 31 do espelho público Wuxiaspot. O preview oficial do '
             'capítulo 31 confirma somente controle mental por voz ou olhar e o despertar de '
             'Su Mu na cama; a lista posterior de poderes é atribuída ao espelho, não a esse '
             'preview parcial. Nate é o nome localizado usado na descrição, enquanto o '
             'original usa Su Mu; a equivalência é inferida pelo conjunto narrativo '
             'específico, não por nomes idênticos. O título chinês canônico e o autor 一年一更 '
             'foram verificados na editora original Fanqie. Os dois aliases ingleses são '
             'títulos MTL atestados em WTR-LAB e Wuxiaspot; não foi verificada edição '
             'inglesa licenciada. Evidência do lado do vídeo restrita à descrição atual: sem '
             'transcrição obtida, frames utilizáveis, escuta independente ou timestamps de '
             'cenas. As referências a capítulos do romance servem para identificar a obra; '
             'não estabelecem cobertura nem capítulo final do recap. '
             'https://www.youtube.com/watch?v=UrS-eHTg72g '
             'https://fanqienovel.com/page/7274774422865579069 '
             'https://fanqienovel.com/reader/7274774461499310648 '
             'https://fanqienovel.com/reader/7274785095520059963 '
             'https://fanqienovel.com/reader/7275144026620658234 '
             'https://fanqienovel.com/reader/7277841898881385016 '
             'https://www.wuxiaspot.com/novel/after-dying-billions-of-times-i-copied-my-talents-and-killed-all-races_31.html '
             'https://wtr-lab.com/en/novel/9943/after-billions-of-deaths-i-copy-talents-and-slaughter-all-races',
 'reviewed_at': '2026-10-15',
 'confirmado': True})


REVIEWED.append({'video_id': 'RJOtZX94A6A',
 'title': 'Steel Covenant',
 'aliases': ['钢铁契约'],
 'evidence': 'Manhua identificado pela transcrição nativa do vídeo exato, lida no YouTube em '
             '15/10/2026, e por comparação narrativa com painéis externos do capítulo 1. Em '
             '0:00–0:19, um comboio militar cruza o deserto, o radar detecta objetos não visíveis, '
             'o capitão ordena preparação e um verme emerge junto aos veículos. Os painéis '
             'externos inspecionados mostram a mesma sequência específica. Em 2:44–3:00, '
             'Qiao/Chiao An é identificado como aluno da Combat Armor Academy; em 3:40, inicia um '
             'pacto envolto em energia azul, também presente nos painéis; em 4:05, surge a '
             'armadura White Tiger. Em 5:39, são citados três séculos desde a descoberta do vírus '
             'metálico; em 22:14, o protagonista é designado à classe de logística. O catálogo '
             'MangaBaka atesta Steel Covenant / 钢铁契约, Qiao An, academia, reprovação por '
             'compatibilidade, logística, dívida e múltiplas armaduras. O anúncio oficial do '
             'criador Motor Nuclear confirma a IP 钢铁契约 e o lançamento na Tencent; Steel Covenant '
             'aparece também na arte original de abertura e em catálogos/scanlation, sem edição '
             'inglesa licenciada verificada. Grafias dos nomes variam na transcrição automática. '
             'Foi obtida transcrição parcial; não houve inspeção de frames do próprio recap nem '
             'escuta independente. Comparação entre transcrição e painéis externos, sem '
             'correspondência pixel a pixel. As referências ao capítulo 1 identificam a obra e não '
             'estabelecem o intervalo nem o capítulo final do vídeo. '
             'https://www.youtube.com/watch?v=RJOtZX94A6A&t=0s '
             'https://www.youtube.com/watch?v=RJOtZX94A6A&t=164s '
             'https://www.youtube.com/watch?v=RJOtZX94A6A&t=220s '
             'https://www.youtube.com/watch?v=RJOtZX94A6A&t=245s '
             'https://www.youtube.com/watch?v=RJOtZX94A6A&t=339s '
             'https://www.youtube.com/watch?v=RJOtZX94A6A&t=1334s '
             'https://komiku.org/steel-covenant-chapter-1/ '
             'https://image3.komiku.to/upload5/steel-covenant/1/2025-05-27/2_part4.jpg '
             'https://image4.komiku.to/upload5/steel-covenant/1/2025-05-27/2_part5.jpg '
             'https://image5.komiku.to/upload5/steel-covenant/1/2025-05-27/3_part1.jpg '
             'https://img.komiku.org/upload5/steel-covenant/1/2025-05-27/7_part4.jpg '
             'https://mangabaka.org/manhua/2867/Steel-Covenant https://www.mdhtoy.com/new/57.html',
 'reviewed_at': '2026-10-15',
 'confirmado': True})


REVIEWED.extend([{'title': 'All People Scramble for the Tower, I Cleared 999 Floors in Advance',
  'aliases': ['全民抢塔：我提前通关999层', 'Quanmin Qiang Ta: Wo Tiqian Tongguan 999 Ceng'],
  'evidence': 'Confirmado por transcrição nativa do vídeo: 00:00–03:54 vitória no andar 999, '
              'morte, despertar em escola e conta reiniciada com relógio de todas as coisas; '
              '04:11–07:10 melhoria de equipamentos e venda de receitas de vinho à taverna. '
              'KuaiKan oficial confirma Su Bai/苏白 e 万物时钟: '
              'https://www.kuaikanmanhua.com/web/topic/25842/ . Painéis iniciais do capítulo 1 '
              'mostram a transmissão do desafio e o chefe do andar 999: '
              'https://www.kuaikanmanhua.com/webs/comic-next/802213 . Inglês atestado em '
              'catálogo/scanlation, não licença oficial inglesa. Nome chinês e romanização '
              'vinculados no AniList: '
              'https://anilist.co/manga/209234/Quanmin-Qiang-Ta-Wo-Tiqian-Tongguan-999-Ceng/staff '
              '. Capítulo final não verificado. https://www.youtube.com/watch?v=qpyaAr9aJTw',
  'reviewed_at': '2026-10-15T16:21:25Z',
  'confirmado': True,
  'video_id': 'qpyaAr9aJTw'},
 {'video_id': 'PbeNjemNfG8',
  'title': 'The Rebel of the Apocalypse Academy',
  'aliases': ['Rebel of the Doomsday Academy', '終末学院の反逆者'],
  'evidence': 'Transcrição nativa do vídeo 00:00–00:19 corresponde à abertura visual do capítulo '
              '1: escolhido, jovem de casaco branco diante de máquina circular luminosa, futuro do '
              'mundo e ordem de morrer. Kanata, órfãos superdotados, dispositivo aos 18 anos, '
              'traição, portal, ônibus 30 e diretor Shirogane também correspondem à sinopse '
              'específica. Título inglês atestado em scanlation; original japonês no desenho do '
              'capítulo 1. Sem confirmação de licença inglesa ou capítulo final. '
              'https://www.youtube.com/watch?v=PbeNjemNfG8 '
              'https://en-thunderscans.com/the-rebel-of-the-apocalypse-academy-chapter-1/ '
              'https://en-thunderscans.com/comics/the-rebel-of-the-apocalypse-academy/ '
              'https://mgread.io/manga/rebel-of-the-doomsday-academy/ Foram consultados trechos de '
              'abertura, meio e final da transcrição; não uma transcrição integral nem frames do '
              'próprio recap.',
  'reviewed_at': '2026-10-15',
  'confirmado': True}])

REVIEWED.append({'title': 'The Regressor and the Blind Saint',
 'aliases': ['The Regressor and the Blind Saintess',
             'The Regressionist and the Blind Saintess',
             '회귀자와 맹인 성녀'],
 'evidence': 'Confirmado pela transcrição nativa do vídeo de 27 segundos (00:00–00:27): santa cega '
             'cuida de um assassino moribundo apesar dos crimes, ele a encontra morta na chuva, '
             'promete viver por ela, regressa e passa a treinar para ser paladino. Sinopse oficial '
             'do webtoon RIDI confirma a sequência de Vera/베라 e Renée/르네: '
             'https://ridibooks.com/books/6344000001 . Título inglês: '
             'https://asurascans.com/comics/the-regressor-and-the-blind-saint-1bb35e56 ; aliases: '
             'https://comix.to/title/d1y8g-the-regressor-and-the-blind-saintess . É trecho '
             'narrativo identificável, não mero anúncio. Frames ficaram carregando; identidade não '
             'depende de imagem, título ou comentário. A descrição menciona 1–20, mas cobertura de '
             'capítulos não foi verificada. Título inglês e aliases atestados em '
             'catálogo/scanlation; licença oficial inglesa do quadrinho não verificada. '
             'https://www.youtube.com/watch?v=hEvsUBhTXqw',
 'reviewed_at': '2026-10-15T19:17:53Z',
 'confirmado': True,
 'video_id': 'hEvsUBhTXqw'})


REVIEWED.append({'video_id': 'YOhSbA3Gw9o',
 'title': "I'm Really Not the Demon God's Lackey",
 'aliases': ["I'm Really Not the Evil God's Lackey", '我真不是邪神走狗'],
 'evidence': 'Transcrição nativa do vídeo: 00:39–02:13, tempestade e caçadora ferida '
             'entram na sequência da livraria do cap. 1 da novel; 05:06–05:40, '
             'Confessions de Rousseau aparece como Blood and the Beast e ensina controle '
             'do sangue de feras, correspondendo aos caps. 2–3; 06:32–07:20, água '
             'fervente, guarda-chuva, empréstimo de um mês + sete dias e nomes Ji '
             'Zhixu/Ji Bonong/Lin Jie confirmam a mesma cena. Fontes: '
             'https://www.youtube.com/watch?v=YOhSbA3Gw9o&t=306s '
             'https://novelfull.com/im-really-not-the-demon-gods-lackey/chapter-1-welcome.html '
             'https://www.sonicmtl.com/novel/im-really-not-the-demon-gods-lackey/chapter-2/ '
             'https://www.sonicmtl.com/novel/im-really-not-the-demon-gods-lackey/chapter-3/ '
             'Título e alias atestados: '
             'https://manhuaus.com/manga/im-really-not-the-demon-gods-lackey/ Identidade '
             'confirmada, sem inferir cobertura completa ou capítulo final. Foram '
             'inspecionados trechos da transcrição inicial até cerca de 07:47, não o '
             'vídeo inteiro de 15:32:51. Sem comparação de frames do recap com painéis. '
             'Os capítulos 1–3 da novel identificam a história, sem estabelecer '
             'capítulos inicial ou final do manhua adaptado. Inglês e aliases atestados '
             'em índice de terceiros; licença inglesa atual não verificada.',
 'reviewed_at': '2026-10-16T01:18:48Z',
 'confirmado': True})


REVIEWED.append({'video_id': '28RRbqRucW0',
 'title': '与十年后的我连线中',
 'aliases': ['Accidental Video to My Future Self', '與十年後的我連線中'],
 'evidence': 'Transcrição nativa Hindi do vídeo corresponde ao conto 與十年後的我連線中, com '
             'nomes/gêneros trocados (Jordan/Avery/Mike por 沈輕麥/遲晝/溫迎). 03:59–06:14: KTV, '
             'música 晴天, tremor e áudio do futuro tocado por engano (001 p2, §§3–4). '
             '08:38–10:41: selfies, falsa identidade futura, casamentos ambíguos e pergunta '
             'sobre felicidade (p4, §§6–7). 17:41–20:44: perguntas de fanfic, detector '
             'apitando durante confissão verdadeira, controle escondido do amigo, diário e '
             'foto do casamento (p6, §§9–10). 21:53–22:14: despedida das quatro versões e '
             'desaparecimento futuro (p7, §11). O vídeo altera gravidez e detalhes '
             'secundários. https://www.oop.tw/areada/a31602502a/a25199_2a.html '
             'https://www.oop.tw/areada/a31602502a/a25199_4a.html '
             'https://www.oop.tw/areada/a31602502a/a25199_6a.html '
             'https://www.oop.tw/areada/a31602502a/a25199_7a.html Alias inglês atestado: '
             'https://fullnovels.com/accidental-video-to-my-future-self/',
 'reviewed_at': '2026-10-16',
 'confirmado': True})


REVIEWED.append({'video_id': 'FvD39N9jJx8',
 'title': 'Monster’s Streamer Star',
 'aliases': ['Monster Streaming Star',
             'Monster Livestream Star',
             'The Slime’s Livestream Star',
             "Monster's Internet Broadcast Star",
             'Monster-ui Inbang Star',
             '몬스터의 인방스타'],
 'evidence': 'Transcrição pública do vídeo: 00:57 slime recém-nascido na caverna tem inteligência '
             'detectada e recebe sistema de transmissão; 01:36 escolhe Mauling/Malang; 02:01 '
             'dragão Noble Fire; 18:28 treinador de cabeçadas; 26:16 Queen Maul Kang alerta sobre '
             'caçadores humanos; 27:17 mentora aracnídea com filhotes; 45:10 lich Konjuki. A '
             'sinopse oficial Naver855923 identifica 말랑이, 말캉여왕 e 깐죽이, além de Arachne/Fenrir, e a '
             'mesma sequência conceitual caverna, inteligência, transmissão e evolução. Conjunto '
             'específico de personagens/enredo confirma a obra; grafias das legendas automáticas '
             'variam e não são aliases. Título coreano oficial e aliases ingleses atestados nos '
             'catálogos abaixo, sem alegar edição inglesa oficial. Intervalo de capítulos não '
             'estabelecido. https://www.youtube.com/watch?v=FvD39N9jJx8 '
             'https://m.comic.naver.com/webtoon/list?titleId=855923&week=tue '
             'https://www.novelupdates.com/series/monsters-streamer-star/ '
             'https://mgread.io/manga/monsters-streamer-star/ '
             'https://en-thunderscans.com/comics/the-slimes-livestream-star/ '
             'https://toonz.to/manhwa/monsters-internet-broadcast-star',
 'reviewed_at': '2026-10-22',
 'confirmado': True})


REVIEWED.append({'video_id': 'FdlZuKNFcQk',
 'title': 'The Regressed Doctor Just Wanted to Live Quietly',
 'aliases': [],
 'evidence': 'Exact-video comment names the work. Official WEBTOON title and synopsis corroborate '
             'the identification, as reviewed in the tracker research. Sources: '
             'https://www.youtube.com/watch?v=FdlZuKNFcQk&lc=Ugz2yr7YodrbMB5VT2Z4AaABAg '
             'https://www.webtoons.com/en/fantasy/the-regressed-doctor-just-wanted-to-live-quietly/list?title_no=8196 '
             '. No direct video frame comparison claimed.',
 'reviewed_at': '2026-11-04',
 'confirmado': True})

REVIEWED.append({'video_id': 'unfeWGso2sw',
 'title': "The Extra's Academy Survival Guide",
 'aliases': [],
 'evidence': "Full description of the exact video explicitly identifies The Extra's Academy "
             'Survival Guide. Source: https://www.youtube.com/watch?v=unfeWGso2sw . No direct '
             'video frame comparison claimed.',
 'reviewed_at': '2026-11-04',
 'confirmado': True})


REVIEWED.append({'video_id': 'ndMBcKZXmZk',
 'title': 'The Ruined World Was Mistaken for a Game',
 'aliases': [],
 'evidence': 'Exact-video viewer comment names the work. Opening transcript at 0:00–1:26 mentions '
             'Kim Jin-woo, Arsilan, erosion and the game premise; this distinctive combination '
             'matches the external series synopsis. Sources: '
             'https://www.youtube.com/watch?v=ndMBcKZXmZk&lc=UgyUIvbOenmHOubm72d4AaABAg '
             'https://arenascan.com/manga/the-ruined-world-was-mistaken-for-a-game/ . No direct '
             'frame comparison or complete chapter coverage claimed.',
 'reviewed_at': '2026-11-04',
 'confirmado': True})


REVIEWED.append({'video_id': 'dnCG095au_4',
 'title': 'All People: All Summons Have SSS-Level Talents',
 'aliases': ['全民：召唤物全是SSS级天赋'],
 'evidence': 'Novel source identified, not a confirmed manhwa adaptation. Exact-video description '
             'has rare GREEDY GLUTTONY, black wolf and abandoned school. Novel chapter 3 has the '
             'black wolf eating mutant meat, growing over two meters after half an hour, and '
             'protagonist stats rising by 10, matching the distinctive sequence. Official Fanqie '
             'listing establishes original title. Sources: '
             'https://www.youtube.com/watch?v=dnCG095au_4 '
             'https://www.fanmtl.com/novel/all-people-all-summons-have-sss-level-talents_3.html '
             'https://fanqienovel.com/page/7319733993400699966 . No direct frame comparison or '
             'complete chapter coverage claimed.',
 'reviewed_at': '2026-11-04',
 'confirmado': True})


REVIEWED.append({
    "video_id": "4X3uc8MAdVM",
    "title": "Miss Lu Turned Her Back, Her Six Brothers Begged for Forgiveness",
    "aliases": ["陆小姐独美后，六个哥哥跪求原谅"],
    "evidence": (
        "Confirmed original novel source by 红十三; this video is a renamed, gender-swapped "
        "retelling, not a verified licensed comic adaptation. Video: "
        "https://www.youtube.com/watch?v=4X3uc8MAdVM . Fresh native transcript at "
        "01:11–01:56 gives thesis theft, second sibling's false testimony, third sibling's "
        "forced kidney operation, siblings 4–6 expelling the protagonist from an international "
        "team, forged medical records, expulsion from home, failed revenge and asylum torture. "
        "At 02:13–04:01, rebirth is three years earlier at the driver's child's adoption banquet; "
        "a false pool accusation leads to sinking, belated rescue by the second sibling, and "
        "the protagonist swimming away using a skill learned in the prior life. Shuqi chapter 1 "
        "independently contains this same ordered, distinctive sequence with Lu Ning, six "
        "brothers and Qin Xiang: https://t.shuqi.com/v2/query/9058439/895127.html . "
        "The video's Ye Chen/six sisters/driver's son are changed identities. A reader explicitly "
        "names the source and explains the gender/name changes: "
        "https://www.youtube.com/watch?v=4X3uc8MAdVM&lc=Ugxi0B089FL8Bw6ZkRx4AaABAg . "
        "This ordinary comment is corroboration, not the sole identification basis. "
        "English title and Chinese original are linked by Novel Updates: "
        "https://www.novelupdates.com/series/miss-lu-turned-her-back-her-six-brothers-begged-for-forgiveness/ . "
        "The English chapter also matches the pool opening: "
        "https://noicetranslations.com/manga/miss-lu-turned-her-back-her-six-brothers-begged-for-forgiveness/chapter-1/ . "
        "The video opening's Thailand/coming-of-age addition was not matched to this source. "
        "No opening-frame match is claimed: cloud playback remained black and buffering at 00:05."
    ),
    "reviewed_at": "2026-11-05",
    "confirmado": True,
})


REVIEWED.append({
  "video_id": "9gsvfXt4_Mc",
  "title": "Demon King of the Royal Class",
  "aliases": [
    "The Demon Prince Goes to the Academy",
    "마왕은 학원에 간다"
  ],
  "evidence": "Full target description checked; it gives no series title, only a comments pointer and claimed chapters 1–80. Public exact-video comments name Demon King of the Royal Class and The Demon Prince Goes to the Academy: https://www.youtube.com/watch?v=9gsvfXt4_Mc&lc=UgxujjaGs472GWHDLm14AaABAg and https://www.youtube.com/watch?v=9gsvfXt4_Mc&lc=UgzlU7cc8QG7bx0eD2R4AaABAg.AcobVz7xxYOAconx6Mclfz . These are ordinary viewers, not creator replies. A separate viewer points to the sin of abandoned stories at 01:36: https://www.youtube.com/watch?v=9gsvfXt4_Mc&lc=UgzXh65OjZMxqdEoYot4AaABAg . Directly inspected public YouTube storyboard opening previews at 10-second intervals from 00:00–02:50: novel writer at computer and hostile reader comment near 01:10–01:20; afterlife female official near 01:40; Valier Junior's Demon King's Castle Escape Plan and human camouflage near 02:10. Official Tapas synopsis identifies the dead novelist, The Demon King Is Dead, rebirth as Baalier Junior and Royal Class in Gradias Temple: https://tapas.io/series/demon-king-of-the-royal-class/info . Licensed Wuxiaworld novel chapter 1 independently gives death from hate-comment-induced hypertension, punishment for repeatedly abandoning novels, rebirth as the demon king's son and escape from the conquered castle: https://www.wuxiaworld.com/novel/demon-king-of-the-royal-class/dkrc-chapter-0 . Alternate English and Korean titles corroborated by https://www.novelupdates.com/series/the-demon-prince-goes-to-the-academy/ . 32 public comments/replies sampled from displayed count 37; no full-comment census claimed. No native transcript was available. Preview images, not full-resolution decoded playback; no reverse-image search needed after specific comment/plot confirmation. Chapter coverage and cancellation status are not independently asserted.",
  "reviewed_at": "2026-11-05",
  "confirmado": True
})


REVIEWED.append({'video_id': 'fAKmEIeQ9nA',
 'title': '我的学习群里全是真大佬',
 'aliases': [],
 'reviewed_at': '2026-11-05',
 'confirmado': True,
 'evidence': '{"video_url": "https://www.youtube.com/watch?v=fAKmEIeQ9nA", "source_type": "Novel '
             'by 胖胖的小橘; no verified official English alias", "creator_evidence": {"location": '
             '"Expanded description and pinned uploader comment", "url": '
             '"https://www.youtube.com/watch?v=fAKmEIeQ9nA&lc=UgybJGH1O6S6n64GFjJ4AaABAg&pp=0gcJCUsANpG00pGi", '
             '"observations": "Both explicitly label linked tH8qKW4qoXU as Part1; title labels '
             'this recap (2). Uploader says original novel name appears in last 10 seconds, but '
             'title card was not successfully observed and is not relied on."}, "matches": '
             '[{"video_timestamp": "00:00–00:29", "observations": "Leo Dawson attends River City '
             'No. 7 High senior class 2, joins Azure Dragon Study Group with Newton, Joule, '
             'Einstein and Gauss, receives exclusive red envelopes and stats.", "external_url": '
             '"https://www.hongxiu.com/bookquery/peurnjosdyzf", "external_location": "Publisher '
             'title/author, synopsis and chapter 1 indexed text only; direct fetch returned 403 '
             'and was not bypassed", "external_match": "Original 李东, 江城第七中学高三（2）班, 青龙学习小组, same '
             'scientist members and red-envelope reward mechanism. Names localized in recap."}, '
             '{"video_timestamp": "00:38–02:22", "observations": "To let Mendeleev beat Franklin, '
             'protagonist searches Wright flyer diagrams, early biplane aerodynamics and '
             'internal-combustion aviation. Logic 0.1 and memory 0.1 help him distill Bernoulli '
             'wing principles, three-axis control and a lightweight engine into a heavier-than-air '
             'aircraft PDF. Franklin cries cheating; da Vinci realizes fixed wings, rather than '
             'flapping ornithopters, are key.", "external_url": '
             '"https://www.bixiange.top/dsyq/23567/index/29.html", "external_location": "Chapter '
             '24, 作弊有没有人管了？, on section 29; direct public chapter read, lines 114–204", '
             '"external_match": "Exact same ordered technical details, PDF, three scientists and '
             'reactions, verified against directly opened public chapter."}], "limitations": '
             '["Native transcript observed through UI; transcript export returned a nonexistent '
             'file path.", "No full-video review claimed. Video remained thumbnail after play/seek '
             'attempt, so no usable story frame/title card and no reverse-image search.", "Creator '
             'pinned comment and one reply inspected plus initial twenty displayed top-level '
             'comments; no full comments census claimed."]}'})

# Reviewed 2026-11-05: newest eligible recap uploads.
REVIEWED.extend([{'video_id': 'DsW28iTAN6s',
  'title': 'Monster Summoner: Dungeon Domination with the Demon King’s Army',
  'aliases': ['The Demon King’s Monster-Summoning Adventurer', '魔物召喚でダンジョン無双\u3000魔王軍と契約した最強冒険者'],
  'reviewed_at': '2026-11-05',
  'confirmado': True,
  'evidence': 'Native public YouTube transcript: 03:08–03:54, Yuki and Saki grew up in an '
              'orphanage destroyed by a dungeon break two years ago; 08:30–11:00, demon king '
              'offers Yuki a Monster Tamer contract to conquer other dungeons and protect his '
              'subjects; 16:35–17:21 identifies the demon king as Liber during the summoning. '
              'Official Japanese BOOK WALKER synopsis independently identifies Yuki, loss of '
              'family to dungeon collapse, strongest dungeon boss Libel/Liber, and Monster Tamer '
              'contract; its chapter 1 title is Contract: The Weakest Human and the Strongest '
              'Demon King. Thunderscans and Vortex map the English titles to the same Japanese '
              'work and matching synopsis. Expanded description contains only generic channel '
              'text. Ordinary viewer comment suggests Monster Tamer or I Can Summon Anything, not '
              'used as canonical titles or creator attribution. Video stayed at thumbnail/0:00 '
              'after playback attempts; no usable opening story frame or reverse-image result, and '
              'no full-video review claimed. Sources: '
              'https://www.youtube.com/watch?v=DsW28iTAN6s&t=188s ; '
              'https://www.youtube.com/watch?v=DsW28iTAN6s&t=510s ; '
              'https://www.youtube.com/watch?v=DsW28iTAN6s&t=995s ; '
              'https://bookwalker.jp/series/591142/ ; '
              'https://en-thunderscans.com/comics/monster-summoner-dungeon-domination-with-the-demon-kings-army/ '
              '; https://vortexscans.org/series/the-demon-king%27s-monster-summoning-adventurer ; '
              'https://www.youtube.com/watch?v=DsW28iTAN6s&lc=UgzsgLY8fn_8uaPvqD54AaABAg'},
 {'video_id': 'hm6SdKaFkYU',
  'title': 'God of Learning',
  'aliases': ['我真不想当学神'],
  'reviewed_at': '2026-11-05',
  'confirmado': True,
  'evidence': 'Public native YouTube transcript: 00:00–00:39 He Liang faces expulsion near college '
              'entrance exams after falling from top student to bottom student over three months; '
              '01:08 Chen Mang Tong, former deskmate, offers study materials; 01:47 Guo Lin, class '
              '122 biology representative, mocks him; 02:18 God of Learning system finishes '
              'bonding. MangaBaka maps God of Learning to 我真不想当学神 by 17K漫画 and repeats the '
              'distinctive He Liang/three-month fall/exam/expulsion/system sequence, linking '
              'original Tencent comic 655871. Official iQIYI adaptation synopsis independently '
              'names He Liang and explains illness causing headaches when reading/writing, '
              'academic decline and expulsion threat. Expanded YouTube description gives no source '
              'title. Only one visible comment at inspection, First person to comment, supplied no '
              'title. The original Tencent URL was identified, but its full comic text was not '
              'accessible in the final direct check. Transcript export unavailable but visible '
              'Show transcript panel worked. Player buffered; no panel match/reverse image search '
              'or full-video review claimed. Sources: '
              'https://www.youtube.com/watch?v=hm6SdKaFkYU&t=0s ; '
              'https://www.youtube.com/watch?v=hm6SdKaFkYU&t=138s ; '
              'https://mangabaka.org/manhua/93537/God-of-Learning ; '
              'https://ac.qq.com/Comic/comicInfo/id/655871 ; '
              'https://www.iqiyi.com/a_18o1cq19zh9.html ; '
              'https://www.youtube.com/watch?v=hm6SdKaFkYU&lc=UgzWQWdse8jEH2H1bx54AaABAg'},
 {'video_id': 'nWor-IbgBJ8',
  'title': 'Zombie Apocalypse, I Died Right at the Start',
  'aliases': ['丧尸末日，我开局即死', '丧尸吃人，我吃丧尸', '我在末日当丧尸王。'],
  'reviewed_at': '2026-11-05',
  'confirmado': True,
  'evidence': 'Expanded description and pinned uploader link identify this as Part 2 of video '
              '3qlDmanLZBM. Native public transcript 00:57–01:14 compares a flying ant becoming '
              'queen and sacrificing wings/brain/body with the body-swapped leader avoiding '
              'monster transformation, matching the official Fanqie chapter 108 preview; '
              '01:54–02:10 discusses soul contracts being safer than loyalty and Blackie warning '
              'of an awakened woman core spirit, matching chapter 111; 05:43–05:59 Serena '
              'melts/shrinks Axel and moves toward Travis before Arya intervenes, matching chapter '
              '114. Fanqie currently lists 我在末日当丧尸王。 by 罪恶原始袋, 547 chapters. NovelUpdates and '
              'WTR-LAB map the existing English Part 1 title to 丧尸末日，我开局即死 and 丧尸吃人，我吃丧尸 with the '
              'same author, 547 chapters, and Ji Chuan/blood-moon/betrayal/zombie-king synopsis. '
              'Official Fanqie chapter 26, 可怕的忠诚, and the alternate-title Shuhaige chapter 26 have '
              'identical openings: Gu Yunxi releases Ji Chuan, blushes, and supports Geng Mao '
              'after he used leaf blades to save her. This establishes alternate titles of the '
              'same work rather than a conflicting new identification; existing Part 1 title and '
              'aliases are preserved. No title-change chronology or official English edition is '
              'asserted. Primary chapter evidence is from public previews, not a full-novel read. '
              'Other comments provided no additional identification. Player buffered with no '
              'usable opening panels, so no panel match or reverse-image result is claimed. '
              'Sources: https://www.youtube.com/watch?v=nWor-IbgBJ8&t=57s ; '
              'https://www.youtube.com/watch?v=nWor-IbgBJ8&t=114s ; '
              'https://www.youtube.com/watch?v=nWor-IbgBJ8&t=343s ; '
              'https://www.youtube.com/watch?v=3qlDmanLZBM ; '
              'https://fanqienovel.com/page/7444764077718506558 ; '
              'https://fanqienovel.com/reader/7456803518372905496 ; '
              'https://fanqienovel.com/reader/7457499247089287742 ; '
              'https://fanqienovel.com/reader/7457905386704601625 ; '
              'https://fanqienovel.com/reader/7446993807914041918 ; '
              'https://m.shuhaige.net/374060/129147090.html ; '
              'https://www.novelupdates.com/series/zombie-apocalypse-i-died-right-at-the-start/ ; '
              'https://wtr-lab.com/en/novel/12255/zombie-apocalypse-i-died-right-at-the-start ; '
              'https://ixdzs8.com/read/592891/'}])


# Reviewed 2026-11-05: correct source despite a mismatched video description.
REVIEWED.append({
  "video_id": "BfWjyBT7wP8",
  "title": "The Grand Duke of the North's Crazy Son-in-Law",
  "aliases": [
    "The Northern Grand Duke's Crazy Son-in-Law",
    "The Northern Grand Duke's Mad Son-in-Law",
    "북부 대공의 미친 데릴사위"
  ],
  "reviewed_at": "2026-11-05",
  "confirmado": True,
  "evidence": "The expanded video description incorrectly labels this The Regressor and the Blind Saintess; that title is rejected because the observed story is different. Native public transcript 00:00–01:51 identifies rookie James at the Intelligence Bureau, Galahad teaching mana compression, three-day recovery, a magical flower, the marry-the-Empire joke and his fourth-circle/youngest-graduate status. At 02:08–03:54, Galahad is assigned to marry the northern duke's swordmaster daughter, learns his father arranged it, smokes with the deputy director and receives candy/chocolate advice from the assistant. This distinctive ordered opening matches novel chapter 1. Official Naver webtoon synopsis independently names Galahad, the political marriage, the daughter as the key to defeating the Demon King and her mana-burning touch. Asura maps the English and Korean titles. Pinned uploader comment, its one viewer reply and the other visible comment were inspected; none names the work. Playback stayed at the thumbnail/00:00 after play/seek attempts, so no opening-panel match, reverse-image result or complete-video review is claimed. Sources: https://www.youtube.com/watch?v=BfWjyBT7wP8 ; https://www.youtube.com/watch?v=BfWjyBT7wP8&lc=UgyN-4yFvnxam0HnpDp4AaABAg ; https://noveltl.com/the-northern-grand-dukes-crazy-son-in-law-chapter-1/ ; https://comic.naver.com/webtoon/list?titleId=855360 ; https://asurascans.com/comics/the-grand-duke-of-the-norths-crazy-son-in-law-ab39de10 ; https://series.naver.com/novel/detail.series?productNo=11008859"
})

# Reviewed 2026-11-06: comments and opening exam corroborated by official comic.
REVIEWED.append({
  "video_id": "b_BIqP6Lzlg",
  "title": "The Martial Unity",
  "aliases": [],
  "reviewed_at": "2026-11-06",
  "confirmado": True,
  "evidence": "Expanded description contains generic tags and no source title. A public viewer comment by @MightyTwitchEnjoyer says 'name is the martial unity' and repeats the title in a reply. Native visible transcript at 00:08 names Rui (transcribed as Rui Corer/Louie); at 00:38–02:38 he resists the senior's fear-inducing aura during the academy entrance test and receives his pass. The indexed chapter 12 excerpt of The Martial Unity specifically names applicant Rui Quarrier, his resistance to the senior's fear, the second-round pass and his unusual black hair/eyes, matching the ordered opening despite comic adaptation differences. Official WebNovel comic page verifies The Martial Unity, WebNovel Comics & SOUKAI STUDIO, and protagonist Rui, a reincarnated martial-arts researcher. Playback stayed at the thumbnail after play attempts, so no opening-panel match, reverse-image result or full-video review is claimed. Sources: https://www.youtube.com/watch?v=b_BIqP6Lzlg&lc=Ugyr1sop6yAE47LWuJF4AaABAg ; https://www.youtube.com/watch?v=b_BIqP6Lzlg&lc=Ugziq3PEvtu7PDOsPHd4AaABAg.Acr-P-mYiT9Acr0oiPFc4t ; https://www.youtube.com/watch?v=b_BIqP6Lzlg&t=8s ; https://www.youtube.com/watch?v=b_BIqP6Lzlg&t=38s ; https://www.webnovel.com/comic/the-martial-unity_34539956608002301 ; https://forum.3ptechies.com/files/martial-unity-12-pdf.253899/"
})

# Reviewed 2026-11-06: explicit description, transcript and comment corroborated.
REVIEWED.append({
  "video_id": "hIUCnhssyMs",
  "title": "The Grand Duke of the North's Crazy Son-in-Law",
  "aliases": [
    "The Northern Grand Duke's Crazy Son-in-Law",
    "The Northern Grand Duke's Mad Son-in-Law",
    "북부 대공의 미친 데릴사위"
  ],
  "reviewed_at": "2026-11-06",
  "confirmado": True,
  "evidence": "Expanded public video description explicitly names The Northern Grand Duke’s Crazy Son-in-Law and identifies mage Galahad, warrior Adriana, arranged northern marriage and defeating the Demon King. Native visible transcript at 03:09 names Galahad; 03:46–03:55 describes marrying the Grand Duke's eldest daughter; 04:51 names father Count Abertton as arranging the marriage. An ordinary viewer reply by @shippai000 beneath Name please directly supplies the same title. External Toonz and Kakamanga listings corroborate the elite intelligence mage Galahad, political northern marriage and daughter needed to defeat the Demon King. Canonical spelling and aliases retained consistently with previously verified video BfWjyBT7wP8 for the same work; no filled cells overwritten. No opening-panel match, reverse-image result or full-video review claimed; direct identification and character/plot corroboration establish identity. Sources: https://www.youtube.com/watch?v=hIUCnhssyMs ; https://www.youtube.com/watch?v=hIUCnhssyMs&t=189s ; https://www.youtube.com/watch?v=hIUCnhssyMs&t=226s ; https://www.youtube.com/watch?v=hIUCnhssyMs&t=291s ; https://www.youtube.com/watch?v=hIUCnhssyMs&lc=UgwhYM0axulHpKm6yuZ4AaABAg.Acgq84aMA8HAcgtTS3lPaO ; https://toonz.to/manhwa/the-crazy-son-in-law-of-the-northern-duke ; https://www.kakamanga.com/manga/the-crazy-son-in-law-of-the-grand-duke-of-the-north ; https://comic.naver.com/webtoon/list?titleId=855360"
})

# Reviewed 2026-11-06: retained Naruto story matched to primary chapters.
REVIEWED.append({
  "video_id": "B4ptL64KCv4",
  "title": "火影：开局既然成了鸣人的大哥？",
  "aliases": [
    "Naruto: How Did I End Up Being Naruto’s Older Brother from the Start?"
  ],
  "reviewed_at": "2026-11-06",
  "confirmado": True,
  "evidence": "Exact ordered primary-source chapter match, not merely Naruto themes. Native visible YouTube transcript 00:00–01:43: Ye Tian (ASR Yien/Yetien) works three days straight, dies after a 3 a.m. bicycle/dumptruck collision, wakes beside infant Naruto, gains touch-copying with three choices and one use per person, then perfect Ten-Tails, Wood Style/Deep Forest Emergence and Multi Shadow Clone rewards. Official Fanqie chapter 1 matches this distinctive sequence and names 叶天. Transcript 03:32–04:43 matches Fanqie chapter 3: inheritance demand, chakra chars desk and snaps bookshelf, four ANBU intervene, one-third cash demand and threat of banners about Fourth Hokage’s children eating garbage; Hiruzen cites postwar reconstruction. Fanqie chapter 4 calls him six years old. Canonical Chinese title is from Fanqie chapter headings; 17moon corroborates title/author 虾仁跑路. English alias is an independently indexed MTL-Novel listing, not asserted official translation. Expanded video description only generic tags. 100 loaded top-level comments inspected, no canonical title; one corroborates touch/three-choice copying. Playback remained black/buffering after play and seek attempts, so no opening-panel match, reverse-image result or full-video review claimed. MTL-Novel direct chapter returned 403 and was not retried. Sources: https://www.youtube.com/watch?v=B4ptL64KCv4&t=0s ; https://www.youtube.com/watch?v=B4ptL64KCv4&t=64s ; https://www.youtube.com/watch?v=B4ptL64KCv4&t=212s ; https://www.youtube.com/watch?v=B4ptL64KCv4&lc=UgzVyZLXL8dv8g9PyLV4AaABAg ; https://fanqienovel.com/reader/7669807859189678617 ; https://fanqienovel.com/reader/7669808123976106521 ; https://fanqienovel.com/reader/7669808363798348313 ; https://www.17moon.com/book/fZL/ ; https://mtl-novel.com/novel/naruto-how-did-i-end-up-being-narutos-older-brother-from-the-start/"
})

# Reviewed 2026-11-09: requested missing-name pass for rows 1–45.
REVIEWED.extend([
  {
    "video_id": "eO8D0v-bqQ4",
    "title": "Mr. Kim Strikes It Rich with Auto-Hunting",
    "aliases": [
      "Mr. Kim Is Living the Good Life with Auto-Hunting",
      "노가다 김씨, 자동사냥으로 꿀 빱니다"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Exact-video pinned comment by uploader @Manhwa_Fresh explicitly names Mr Kim Strikes Rich with Autohunting. Independent catalogs map the normalized English title, alias and Korean title, and describe a hunter replacing dangerous work with auto-hunting. Chapter coverage 1–28 is stated by the uploader, not independently verified. Sources: https://www.youtube.com/watch?v=eO8D0v-bqQ4&lc=UgwgXt6xxvdjDg58q9N4AaABAg ; https://mizumanga.org/manhwa/mr-kim-strikes-it-rich-with-auto-hunting ; https://www.manganami.com/manga/mr-kim-strikes-it-rich-with-auto-hunting . No video-frame or full-video review claimed."
  },
  {
    "video_id": "gCKFp2yQ4rI",
    "title": "The Weakest Awakened Rises Through Slime Synthesis",
    "aliases": [
      "The Ultimate Farmer with Slime Fusion",
      "最弱覚醒者はスライム合成で成り上がる"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Native public transcript inspected: 00:00–01:01 Saku combines liquids/slimes; 01:19–02:45 rank-one awakener Saku, stuck for three years on a tutorial quest to make mana fruit juice from self-grown crops; 02:52–03:35 sells potions in Akihabara to Ritsu; 02:07:34 familiar Corin is a gluttony demon/slime. Independent series listings name Jindai Saku, the stagnant tutorial quest, dungeon mutation, second awakening Slime Lord and farming/wealth/monster companions, corroborating the specific protagonist and mechanics. Vortex maps alternate English title to the same Japanese title. No explicit creator identification found in description/comments. Sources: https://www.youtube.com/watch?v=gCKFp2yQ4rI&t=79 ; https://weebcentral.live/manga/the-weakest-awakened-rises-through-slime-synthesis ; https://vortexscans.org/series/the-ultimate-farmer-with-slime-fusion . No video-frame match or complete chapter coverage claimed."
  },
  {
    "video_id": "x-43OWM78dY",
    "title": "The Strongest Swordsman Rising from a Bottom-Tier Job",
    "aliases": [
      "Everyone's Switching Classes! Who Dares Say the Swordsman Is a Trash Class?"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Exact-video public viewer comment @EviI-monkey names both titles and is pinned by uploader @stilesmanhwafresh; commenter is not asserted to be creator. Native transcript 00:03 Rush monster event and magical profession dominance; 00:19 lowest-rank swordsman; 00:58 protagonist rendered Tatsumo Amari, transmigrant raised by poor commoner couple. Independent series page names Tatsuma Emori, adoptive father's sword and D-rank swordsman and explicitly maps the alternate title, corroborating specific character and premise. Sources: https://www.youtube.com/watch?v=x-43OWM78dY&lc=UgwJR3UvWqqcD09Raex4AaABAg ; https://www.youtube.com/watch?v=x-43OWM78dY&t=58 ; https://manhuasite.com/the-strongest-swordsman-rising-from-a-bottom-tier-job . No full-video or panel comparison claimed."
  },
  {
    "video_id": "dTkl5dj_VyQ",
    "title": "Starting Life from Moss in Another World",
    "aliases": [
      "Koke kara Hajimaru Isekai Life",
      "苔から始まる異世界ライフ"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Native exact-video transcript 00:00 names Hikaru Tendo, orphaned at five; 00:09 factory worker dies of overwork; 00:37 Astartina grants reincarnation; 01:09 choice of race and skills. Manga Republic listing independently names twenty-year-old factory worker Hikaru Tendo accidentally reincarnated as moss. MangaBaka confirms Japanese/English titles plus moss evolution and Additional Skill Acquisition. The distinctive protagonist, occupation, death and moss reincarnation corroborate identity beyond generic recap headline. Sources: https://www.youtube.com/watch?v=dTkl5dj_VyQ&t=0 ; https://www.youtube.com/watch?v=dTkl5dj_VyQ&t=37 ; https://manga-republic.com/product/product_page_2069487.html ; https://mangabaka.org/manga/367798/Starting-Life-from-Moss-in-Another-World . No complete video, chapter-coverage or panel-comparison claim."
  }
])

REVIEWED.append({
  "video_id": "1fOHaVcbq7A",
  "title": "Full-Time Hunter: I Hunt the World!",
  "aliases": [
    "Global Hunter: I Hunt the World",
    "全职猎人：我狩猎世界！"
  ],
  "reviewed_at": "2026-11-09",
  "confirmado": True,
  "evidence": "Exact-video public viewer reply by @monoa1770 explicitly names the work, corroborated by native transcript: 00:00 thirty-seventh Hunter Awakening Ceremony at Clear Sky Town, Cloudwalking Province; 01:42 Lu Shu transmigrated into Hunting World; 01:57 humans occupy one percent, phantom beasts the rest; 02:14–02:35 classes Knowledge/Pride, Weapon/Wrath, Element/Sloth, Gourmet/Gluttony, Phantom Beast/Lust. Thunderscans identifies canonical English/Chinese titles and the distinctive Weapon/Gourmet/Knowledge hunter-world premise; Komascans maps alternate English title. Comment is not asserted to be creator or pinned. Sources: https://www.youtube.com/watch?v=1fOHaVcbq7A&lc=Ugzdp2DfQExOjvhNzi14AaABAg.AczvLBryamKAd-6-CWGuhI ; https://www.youtube.com/watch?v=1fOHaVcbq7A&t=102 ; https://www.youtube.com/watch?v=1fOHaVcbq7A&t=134 ; https://en-thunderscans.com/comics/full-time-hunter-i-hunt-the-world/ ; https://komascans.com/en/series/full-time-hunter-i-hunt-the-world . No frame match or complete coverage claim."
})

REVIEWED.append({
  "video_id": "w8UzOg00je0",
  "title": "World-Saving Is a Skill",
  "aliases": [
    "The Return of the World Savior",
    "The One Who Saved a World Before Will Be Best at Saving Another",
    "A Hero Who Knows His Stuff",
    "세상도 구해본 놈이 잘 구한다"
  ],
  "reviewed_at": "2026-11-09",
  "confirmado": True,
  "evidence": "Exact-video creator @MrManhwas01 directly answers World-Saving Is a Skill in a public comment reply. Native transcript 00:00–00:20 Hyeonseok spent twenty years fighting other-world monsters, returns to Earth, exhausts his severance and becomes a paid Hunter. External series listing corroborates Hyeonseok/Chanseok, twenty years, return reward, Earth's Erosion Points and hunter work for money. Catalogs map aliases and Korean title. Sources: https://www.youtube.com/watch?v=w8UzOg00je0&lc=UgziDZ0F9VkTcJ1JZoR4AaABAg.Aczw3M5L2htAd-FI9Ljgzk ; https://www.youtube.com/watch?v=w8UzOg00je0&t=0 ; https://arenascancomics.com/manga/world-saving-is-a-skill/ ; https://phmanga.com/title/world-saving-is-a-skill-11de45ec ; https://ravenscans.org/manga/world-saving-is-a-skill/ . No full-video or frame-match claim."
})

# Reviewed 2026-11-09: second requested missing-name batch.
REVIEWED.extend([
  {
    "video_id": "ukT91_8oHzo",
    "title": "Return of the Adopted Child in a World of Bloodline Supremacy",
    "aliases": [
      "Redoing My Life as the Adopted Son of a Bloodline-Supremacist House",
      "血統至上主義名家の養子のやり直し",
      "Kettou Shijou Shugi Meika no Youshi no Yarinaoshi"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Exact-video public viewer @Positively_Pretty names the work. Native transcript corroborates slave arena versus the Butcher at 00:00; Colin Hall as last surviving human at 00:46; only nobles use magic at 01:17; forbidden book lets anyone learn at 01:33; his blood awakens book at 03:00; book offers regression and magic teaching at 03:19. External synopsis identifies Colin, enslaved swordsman, demon extinction, forbidden book and five-year regression. Qimanga maps Japanese title and aliases. Original Piccoma was Japan-restricted and not bypassed. Sources: https://www.youtube.com/watch?v=ukT91_8oHzo&lc=UgwwGNF2Hv0l-MkDXtN4AaABAg ; https://www.youtube.com/watch?v=ukT91_8oHzo&t=46 ; https://erascans.com/series/return-of-the-adopted-child-in-a-world-of-bloodline-supremacy/ ; https://qimanga.com/series/return-of-the-adopted-child-in-a-world-of-bloodline-supremacy ; https://jp.piccoma.com/web/product/190565 . No full-video or chapter-coverage claim."
  },
  {
    "video_id": "zhNjhPNhPaY",
    "title": "饥荒，我的物品能升级",
    "aliases": [
      "Don't Starve, My Items Can Be Upgraded"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Novel by 左耳听天, not asserted to be a published manhwa. Exact-video expanded description localizes Yang Chen as Jace and Peng Min as Wren: vitality-converted Hexflux upgrades rusty nailgun with Never-Miss, then Arm Fusion/Zero Recoil; crystallized marrow, storage/Spatial Quake sphere and refuge migration. Chinese chapter-one excerpt names Yang Chen, item-enhancing 妖衍/衍气, rusty tube nail launcher and Peng Min after breakup of their team. Publisher-family synopsis explicitly corroborates arm fusion and no recoil; source table of contents orders chapter12 crystallized marrow,13 stone beast,15 awakening,16 breakthrough,20 如意震空珠. English title is a verified translation alias, not asserted official. Sources: https://www.youtube.com/watch?v=zhNjhPNhPaY ; https://www.rongshuxia.com/bookquery/qbzfcldyvxbp ; https://www.xxsy.net/baike/axdj3tev46bt ; https://www.fanmtl.com/novel/6981335.html ; https://wtr-lab.com/en/novel/10411/dont-starve-my-items-can-be-upgraded . No frame match or complete chapter coverage claimed."
  },
  {
    "video_id": "y_JHzvkR4S4",
    "title": "My Path to Killing Gods in Another World",
    "aliases": [
      "My Way of Killing Gods in Another World",
      "Assassin in Another World",
      "我在异界的弑神之路"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Native exact-video transcript inspected: 01:33–02:34 protagonist plays Cosmos VR to impress classmate, receives headset, lightning strikes house and transports him from bedroom; 02:50–03:39 spawns in desert, cannot contact friend or log out, system reboots to survive for infinity hours; 04:59–05:43 desert wolf encounter and backstory as youngest sixth-dan kendo student; 01:11 opening teaser names chaos element. Official Kuaikan series identifies genius student playing to pursue a girl, lightning transport, monsters and gods. Chinese/English catalogs name Chen Zhiliao/Chen Zhi Le and kendo talent. Independently indexed Chinese adaptation description of same title gives episode1 Welcome to COSMOS,23 Release of Chaos Element and matching character/transport premise. This distinctive combination corroborates identity despite ASR rendering names as Shenzel/Chen. Sources: https://www.youtube.com/watch?v=y_JHzvkR4S4&t=93 ; https://www.youtube.com/watch?v=y_JHzvkR4S4&t=170 ; https://www.youtube.com/watch?v=y_JHzvkR4S4&t=299 ; https://www.kuaikanmanhua.com/web/topic/11031/ ; https://dragontea.ink/novel/my-path-to-killing-gods-in-another-world/ ; https://www.youtube.com/watch?v=MIhoO3yalZU ; https://m.dm5.com/manhua-wozaiyijiedeshishenzhilu/ . Description contains no source title. No frame comparison or complete chapter coverage claimed."
  },
  {
    "video_id": "4qlV6PTIY5Y",
    "title": "The World’s Strongest Fist Fighter",
    "aliases": [
      "World's Strongest Straight Punch",
      "Conquering the World with a Single Punch",
      "World's Strongest With Bare Fists",
      "The World's Strongest Regime",
      "정권으로 세계최강"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Uploader @FuriosToon own pinned comment explicitly names World's Strongest Straight Punch. Native transcript 00:17 four disciples murder father,00:29 trains one punch ten years,00:49 traitors became Four Heavenly Kings,03:29 protagonist Jin Guan and inherited limitless fist manual. Independent catalogs corroborate Jin-gwon's ten-year secluded training for his father's revenge and Murim transformed to skills society. Canonical primary retained consistently with previously confirmed i7wa7Mspnqw in this catalog; names are established aliases of 정권으로 세계최강. Sources: https://www.youtube.com/watch?v=4qlV6PTIY5Y&lc=Ugxvc4Gcafl_aH8rkb54AaABAg ; https://www.youtube.com/watch?v=4qlV6PTIY5Y&t=29 ; https://comick.dev/comic/the-worlds-strongest-regime ; https://ravenscans.org/manga/worlds-strongest-straight-punch/ ; https://comic.naver.com/webtoon/list?titleId=851800 . No full-video or panel-match claim."
  },
  {
    "video_id": "-seaUuYO4pw",
    "title": "Warrior of the Soulblade",
    "aliases": [
      "Warrior of the Mind Sword",
      "Warrior of the Sword Heart",
      "Soulblade Warrior",
      "심검의 용사"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Exact-video public viewer comment names The warrior of the mind sword; chapter1–62 claim is commenter-stated, not independently verified. Native transcript corroborates emotions creating mind swords at01:43, Heith's hatred of demons01:52, boy Ellen02:16, king's ten swords and qualification exam01:10. External catalog maps official-English title Warrior of the Soulblade, aliases and Korean title, and gives WEBTOON synopsis naming Allen, soul swords, purity and exams controlled by the king's ten swords. Sources: https://www.youtube.com/watch?v=-seaUuYO4pw&lc=UgyrXZ3dQX6v2xVLSRx4AaABAg ; https://www.youtube.com/watch?v=-seaUuYO4pw&t=70 ; https://www.youtube.com/watch?v=-seaUuYO4pw&t=103 ; https://hwa.so/series/warrior-of-the-sword-heart-mu-3869456704 . No video-frame match or full-video review claimed."
  },
  {
    "video_id": "utRmIhmyQkc",
    "title": "After Severing Our Ties, All My Summons Became Dark Creatures",
    "aliases": [
      "After Breaking Off Relations, My Summoned Beasts Are All Dark Creatures",
      "断绝关系后，我的召唤兽全是黑暗生物"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Two exact-video public viewer comments name the series. Native transcript 00:29 Gu Chen betrayed during final monster battle;01:58 foster parents died, biological father takes him home, blond younger brother abuses and murders him;03:14 monster revives. Official Kuaikan synopsis names Gu Chen, brother's backstab, return to eighteen before awakening, Demon King's Blood, severing family and Dark Summoner. AniList corroborates English/Chinese identity. Chapter1–20 is a viewer claim, not independently checked coverage. Sources: https://www.youtube.com/watch?v=utRmIhmyQkc&lc=UgxGacPtapa0AWXV4Mh4AaABAg ; https://www.youtube.com/watch?v=utRmIhmyQkc&lc=UgzVrSykfqv2lrkQ4fF4AaABAg ; https://www.youtube.com/watch?v=utRmIhmyQkc&t=29 ; https://www.kuaikanmanhua.com/web/topic/27690/ ; https://anilist.co/manga/218623/Duanjue-Guanxi-Hou-Wo-De-Zhaohuan-Shou-Quan-Shi-Heian-Shengwu/ . No full-video or panel-match claim."
  },
  {
    "video_id": "NWKoM60_sfM",
    "title": "The Dark Mage's Return to Enlistment",
    "aliases": [
      "Returned to the Day I Joined the Army",
      "I Returned, But It Was the Day Before My Enlistment",
      "귀환했는데 입대 전날이다"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Exact-video viewer comment explicitly names the series. Native transcript 00:00 Kim Minjun smashes dungeon redstone;00:39 saint summons him to Isgard as dark mage;01:24 saves world, wants games and fried chicken;01:39 removes restraint and returns;02:06 two years passed on Earth and enlistment notice;02:19 must enlist tomorrow. Official Indonesian WEBTOON confirms English title and Kim Minjun/Isgard/home monsters/military requirement. Korean and aliases mapped by external catalog. Commenter chapter count111+ refers to claimed availability, not video coverage and not relied on. Sources: https://www.youtube.com/watch?v=NWKoM60_sfM&lc=Ugw7saClaHxjSZi8P0p4AaABAg ; https://www.youtube.com/watch?v=NWKoM60_sfM&t=39 ; https://www.youtube.com/watch?v=NWKoM60_sfM&t=126 ; https://m.webtoons.com/id/action/the-dark-mages-return-to-enlistment/list?title_no=5663 ; https://ravenscans.org/manga/the-dark-mages-return-to-enlistment/ . No full-video or frame-match claim."
  }
])

# Reviewed 2026-11-09: independently corroborated shelter sequel.
REVIEWED.extend([
  {
    "video_id": "PpHE_n8CXbc",
    "title": "末世天灾：从打造避难所开始",
    "aliases": [
      "Apocalyptic Disasters: Starting by Building a Shelter"
    ],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Creator's pinned comment links Part1 0vtHQxQ1Hag, already confirmed for this novel. Independent native transcript corroboration beyond linkage:00:10 Cade Walker with end-of-world survival system and three-level backyard shelter;00:18 hydroponic/protein farms and automated engineering crew;00:25 seven-million resource deal with authorities;00:50 detection radar on micro-excavator;01:58 Rocky database helper;02:15 survival-point-upgraded large cargo truck;05:05 Riverford subchannel. Same localized Su Wu/Cade Walker and Jianghe/Riverford, survival-point engineering upgrades and shelter established against original chapters1 and3 in prior verified Part1. Novel by 夏天的葡萄, not asserting separate adaptation title. Creator says title appears in last ten seconds, but video stayed black/buffering and that card was NOT observed. Sources: https://www.youtube.com/watch?v=PpHE_n8CXbc&lc=UgyoviItIO1GYK-4oad4AaABAg ; https://www.youtube.com/watch?v=PpHE_n8CXbc&t=10s ; https://www.youtube.com/watch?v=0vtHQxQ1Hag ; https://www.biquge321.com/zhangjie/024424/502751095.html ; https://www.biquge321.com/zhangjie/024424/602351095.html ; https://shanghaifantasy.com/novel/apocalyptic-disasters-starting-by-building-a-shelter/ . No full-video or chapter-coverage claim."
  }
])

# Reviewed missing names requested on 2026-11-09: Gave Greek-mythology novel.
REVIEWED.extend([
  {
    "video_id": "AOyMn2g7jP0",
    "title": "女神今晚留下来",
    "aliases": [],
    "reviewed_at": "2026-11-09",
    "confirmado": True,
    "evidence": "Novel by 紫夜弦歌; no verified English alias or separately published manhwa adaptation asserted. Native exact-video transcript:00:01 Helen/希伦 reincarnated with Pandora grandmother and Prometheus grandfather;00:10 Zeus abducts him to Olympus, stories win Hera's favor;00:17 Eris becomes Spear of Heaven's Wrath;00:25 returns to Crete after Athena's ten-year absence, facing sea catastrophe;02:47–04:36 Pallas defends Knossos with labyrinth projection while Helen attacks sea monster's divine core. Independent Qidian-hosted review corroborates ordered sequence through Crete, missing Athena, catastrophe and Pallas. Title/author independently verified from readable novel directory. Hongxiu indexed publisher-family synopsis also confirms Hera's Juno disguise, nightly stories, Eris and Pandora's demand for Hera's divine blood, matching linked first-part description. Creator pinned comment explicitly links Part1 wqoUI0tbBiQ. Qidian and Hongxiu support from indexed text only; direct requests returned403 and were not bypassed. Sources: https://www.youtube.com/watch?v=AOyMn2g7jP0&t=1s ; https://www.youtube.com/watch?v=AOyMn2g7jP0&t=167s ; https://www.youtube.com/watch?v=AOyMn2g7jP0&lc=UgyRMGNyb7-KzTgvsOt4AaABAg ; https://www.youtube.com/watch?v=wqoUI0tbBiQ ; https://book.qidian.com/booklist/detail/634557/ ; https://m.hongxiu.com/kolquery/vxbpurlw ; https://44xw.com/a/197/196064/ . No final title-card observation, full-video review or exact chapter-boundary claim."
  }
])


# Reviewed 2026-11-09: exact-video metadata and official named-character match.
REVIEWED.extend([
{
  "video_id": "lD-gDmrt_g4",
  "title": "Barbarian's Adventure in a Fantasy World",
  "aliases": [
    "판타지 세계 속 바바리안으로 살아가기"
  ],
  "reviewed_at": "2026-11-09",
  "confirmado": True,
  "evidence": "Exact-video public metadata mirrored at https://salda.ws/video.php?id=lD-gDmrt_g4 explicitly identifies the work and character Ketal in its title and description hashtags. Its outgoing video link resolves to https://youtube.com/watch?v=lD-gDmrt_g4, with Gacha reactrift channel and 00:41:41 duration matching the current Sheet ID. Official English publisher https://tapas.io/series/barbarians-adventure-in-a-fantasy-world/info independently names Ketal the Barbarian and provides the English and original Korean titles. The publisher describes his emergence from the monster-filled White Tundra; this synopsis establishes the distinctive named character, not a claimed frame or transcript match. This is a Gacha reaction video explicitly about that work, not asserted to be a conventional chapter recap. Direct YouTube retrieval was throttled, so no direct comments, playback, frames, transcript, chapter coverage, or reverse-image review is claimed. FameX indexed channel listing corroborated the same title and duration but was not needed for the exact-ID confirmation."
}
])


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


# Reviewed 2026-11-10: native transcript and official named-character match.
REVIEWED.append({
  "video_id": "RW7GtvBs67k",
  "title": "The Veteran Healer Is Overpowered",
  "aliases": [
    "The Late Game Healer Is Way Too Strong",
    "The Overpowered Veteran Healer",
    "고인물 힐러가 너무 강하다"
  ],
  "reviewed_at": "2026-11-10",
  "confirmado": True,
  "evidence": "Exact-video public viewer comments explicitly name the series. Native transcript: 00:00–00:19 healer Minsu spent one hundred years in the demon realm and returns with a demon in his stomach after only ten Earth years; 01:16 Min Siwu; 01:24 Frey and dimensional orb; 02:31 Korea 2037 and hundred-year/ten-year time difference. Official French WEBTOON synopsis independently names Min Siwoo, a century in another world, return with Pré after ten Earth years and erased disciples. English/Korean aliases corroborated by Thunderscans. Expanded video description contained tags, not a source title; twenty public comments inspected. Sources: https://www.youtube.com/watch?v=RW7GtvBs67k&lc=UgxTyWIr5ZeGGUxSeYh4AaABAg ; https://www.youtube.com/watch?v=RW7GtvBs67k&lc=UgwzfPZunrjeaweuJRR4AaABAg ; https://www.youtube.com/watch?v=RW7GtvBs67k&t=76 ; https://www.youtube.com/watch?v=RW7GtvBs67k&t=151 ; https://www.webtoons.com/fr/action/the-veteran-healer-is-overpowered/list?title_no=8261 ; https://en-thunderscans.com/comics/the-late-game-healer-is-way-too-strong/ . No video-frame comparison, reverse image search, full-video review or exact chapter-coverage claim."
})


# Reviewed 2026-11-10: Vikir transcript and official publisher confirmation.
REVIEWED.append({
  "video_id": "uZ43s8gEJi4",
  "title": "Revenge of the Baskerville Bloodhound",
  "aliases": [
    "Revenge of the Iron-Blooded Sword Hound"
  ],
  "reviewed_at": "2026-11-10",
  "confirmado": True,
  "evidence": "Two exact-video public viewer comments explicitly name Revenge of the Iron-Blooded Sword Hound. Native transcript: 00:40 Vikir wins written examination; 01:21–01:42 Vikir Van Baskerville accused of treason, killed on his father's orders and returns to birth; 01:42 Hugo; 02:40 cradle of swords; 02:48 River Styx; 03:19 John Barrymore. Official Tapas identifies Vikir, illegitimate son executed by his father, reborn with memories to seek revenge; official Google Play Books series independently names Vikir van Baskerville and newborn regression. Canonical English title retained consistently with existing catalog and Sheet identification. Expanded video description claims chapters 1–90; coverage is uploader-stated, not independently verified. Sources: https://www.youtube.com/watch?v=uZ43s8gEJi4&lc=UgxXKK21tNW4zLwJKBZ4AaABAg ; https://www.youtube.com/watch?v=uZ43s8gEJi4&lc=UgwWQpelnzghWWn3wvB4AaABAg ; https://www.youtube.com/watch?v=uZ43s8gEJi4&t=81 ; https://www.youtube.com/watch?v=uZ43s8gEJi4&t=199 ; https://tapas.io/series/revenge-of-the-baskerville-bloodhound/info ; https://play.google.com/store/books/series?id=7ZWQHAAAABB8iM . No video-frame comparison, reverse image search or full-video review claimed."
})


# Reviewed 2026-11-10: distinctive transcript sequence and chapter-one match.
REVIEWED.append({
  "video_id": "ekxadHjvwZI",
  "title": "The Ruler of Darkness",
  "aliases": [
    "Ruler of the Dark Age",
    "제암진천경",
    "암흑기의 지배자"
  ],
  "reviewed_at": "2026-11-10",
  "confirmado": True,
  "evidence": "Native exact-video transcript inspected in the cloud browser: 00:10–00:51 Lu Yong/Lu Yang Sword Clan and prisoner deprived of limbs, tongue and eyes; 01:34–02:13 two sisters killed and fratricidal war after he left to become a son-in-law; 02:20–02:37 at age four he condensed hundreds of martial treatises into twenty-five, at five gave agricultural advice to the emperor, and at six predicted a drought; 05:16–05:55 book made of human skin, blood text and tendon stitching, with pact with darkness; 06:28 heir rendered Sohin by transcript, later Sohyun and Medicine King. Independently read chapter 1 reproduces captivity, mutilations, sisters and the precise age-four/five/six and twenty-five-books sequence. Nine Heavens identifies Yeon So-hyeon and the skin/blood/tendon book; Asura corroborates the English title, aliases, doomed star, destroyed family and dark pact. Official Kakao page confirms Korean title 제암진천경 and creators TenaZ/유과. Expanded description was generic; two inspected comments supplied no title and were not the identification basis. Sources: https://www.youtube.com/watch?v=ekxadHjvwZI&t=10 ; https://www.youtube.com/watch?v=ekxadHjvwZI&t=140 ; https://www.youtube.com/watch?v=ekxadHjvwZI&t=316 ; https://wuxiaworld.eu/chapter/the-ruler-of-darkness-1 ; https://nineheavens.org/novels/the-ruler-of-darkness/ ; https://asurascans.com/comics/the-ruler-of-darkness-f212c582 ; https://webtoon.kakao.com/content/%EC%A0%9C%EC%95%94%EC%A7%84%EC%B2%9C%EA%B2%BD/4898 . No frame comparison, reverse image search, full-video review or exact chapter-coverage claim."
})


# Reviewed 2026-11-10: explicit creator linkage to confirmed prehistoric-game Part 1.
REVIEWED.append({
  "video_id": "8OVdsQ90-PQ",
  "title": "史前生物哪家强？恐怖直立猿称王",
  "aliases": [],
  "reviewed_at": "2026-11-10",
  "confirmado": True,
  "evidence": "Exact-video expanded description explicitly links Part 1 https://youtu.be/odfuzkICaOo. Uploader @Gave-k8y own pinned comment independently links the same Part 1 and says season 1 is complete. The linked first video is already specifically confirmed in this catalog as the novel by 七七霖: Yang Chen localized as Ethan Dawson, Earth Online national Civilization Observer, Ancestral Ground Ape, shoulder/collarbone/tendon adaptation for throwing rocks at sabertooth cats and a switch from fruit to meat. Newly rechecked external catalog search results corroborate the original title/author and the distinctive chapter sequence: 5 Ancestral Ground Ape, 17 Throwing, 18 Shoulder Modification/Biological Slingshot, 19 rocks, 21 sabertooth and 23 fruit to meat. A public comment on this sequel describes the ape leader hit by a stone and permanently marked, consistent with the linked continuity; this viewer comment alone is not the identification basis. Sources: https://www.youtube.com/watch?v=8OVdsQ90-PQ ; https://www.youtube.com/watch?v=8OVdsQ90-PQ&lc=UgzNWK1x4Q4Ijuh0dtZ4AaABAg ; https://www.youtube.com/watch?v=odfuzkICaOo ; https://www.xs.cn/bookquery/pelwgtkgtuen ; https://www.xxsy.net/bookquery/pelwgtrhxaen ; https://www.youtube.com/watch?v=8OVdsQ90-PQ&lc=UgxapbVp0CkvBz5THG14AaABAg . Identification relies on explicit uploader sequel linkage plus the previously detailed Part 1 source match, not the thumbnail. Twenty comments and one reply inspected. No available transcript; attempted end-frame playback did not load beyond thumbnail, so no title-card, scene, frame comparison, reverse image search, full-video review or exact chapter-coverage claim. No verified English alias."
})


# Reviewed 2026-11-10: exact EXP-system sequence, chapter-one match and official novel identity.
REVIEWED.append({
  "video_id": "NfUJfvvuFUg",
  "title": "高武：成神从一亿经验值开始无敌",
  "aliases": [
    "High Martial Arts: Becoming a God Starts with 100 Million Experience Points and Becomes Invincible"
  ],
  "reviewed_at": "2026-11-10",
  "confirmado": True,
  "evidence": "Native exact-video transcript inspected in the cloud browser: 00:24 protagonist rendered Lu Chang/Lu Cheng; 01:13 vitality 0.6 versus Old Wang 0.8; 01:59 mission to kill ten living beings within twenty-four hours; 03:11 fire ants; 03:41 boiling water poured into the colony; 04:15 one hundred thousand deaths and system error; 04:41 system disabled; 05:08 one hundred million EXP awarded; 05:16 remaining functions kill to gain EXP and spend EXP to level up. Independently read novel chapter 1 reproduces this precise numeric and causal sequence. Direct official Fanqie page confirms original title and author 馒头馅儿饺子. English alias is WTR-LAB's documented machine-translated title, not an official English edition. Expanded video description names Lu Cheng and the premise; twenty inspected comments supplied no source title. Official chapter index 144–146 mentions Mount Gongwang rising/walking, consistent with the description's late moving-mountain premise but not proof of video chapter boundaries. Sources: https://www.youtube.com/watch?v=NfUJfvvuFUg&t=73 ; https://www.youtube.com/watch?v=NfUJfvvuFUg&t=119 ; https://www.youtube.com/watch?v=NfUJfvvuFUg&t=221 ; https://www.youtube.com/watch?v=NfUJfvvuFUg&t=308 ; https://fanqienovel.com/page/7644416447938038846 ; https://wtr-lab.com/en/novel/83808/high-martial-arts-becoming-a-god-starts-with-100-million-experience-points-and-becomes-invincible/chapter-1 . No frame comparison, reverse image search, full-video review or exact chapter-coverage claim."
})


# Cloud review 2026-11-10 16:15 UTC
REVIEWED.extend([
  {
    "video_id": "UHSNLC7Vh5U",
    "title": "全民选择进化，我选孢子产氧气",
    "aliases": [],
    "evidence": "Exact-video expanded description and uploader @Gave-k8y pinned comment explicitly link Part 2 sfUeECfxfRo and Part 1 u9IO65gb4To. Part 2 is already specifically confirmed in this catalog. New native transcript independently matches Su Bai (ASR Sububai), Evolution Frenzy and the distinctive ordered choices: 00:00–00:19 photosynthetic spore, zero attack/defense/mobility, all points to oxygen and 99.2% anaerobic extinction; 00:29–00:38 fish develops lungs before ocean hypoxia; 00:42–00:57 burrowing mouse survives asteroid/nuclear winter; 01:04–01:20 primates use spears, stone tools and fire. Fresh external catalog results identify author 何时能起飞, title, Su Bai, oxygen-producing spore and evolution-game extinction mechanics. Sources: https://www.youtube.com/watch?v=UHSNLC7Vh5U ; https://www.youtube.com/watch?v=UHSNLC7Vh5U&lc=UgyGKpBg_XKab22EFWB4AaABAg ; https://www.youtube.com/watch?v=UHSNLC7Vh5U&t=4 ; https://www.youtube.com/watch?v=UHSNLC7Vh5U&t=42 ; https://www.youtube.com/watch?v=sfUeECfxfRo ; https://www.readnovel.com/bqx/sknjosamlw ; https://www.rongshuxia.com/bqx/qbjdzfamamiq . Catalog search results were readable; direct web opens returned 403. Fourteen top-level public comments inspected. Only selected transcript opening inspected, no full-video, frame comparison, reverse-image search or chapter-coverage claim. No verified English alias.",
    "reviewed_at": "2026-11-10",
    "confirmado": True
  }
])


# Cloud review 2026-11-11: distinctive transcript scene and official novel identity.
REVIEWED.append({
  "video_id": "ui7WIFC4w1c",
  "title": "只剩三个月命，他们来求我原谅！",
  "aliases": [],
  "reviewed_at": "2026-11-11",
  "confirmado": True,
  "evidence": "Exact-video native transcript opened through Show transcript and read from the rendered page in the cloud browser. Export helper returned unavailable, but the visible transcript was present and saved. 00:00–00:29: nineteen-year-old terminal stomach-cancer patient, three months left, parents attend younger sister's meeting instead. 00:41–01:31: former neighbor Mr. Wallace collides with Ethan and blames him; Ethan pays for the objects, takes them and throws them into a trash can, saying payment makes them his property. Chapter 1 independently reproduces this distinctive ordered scene with Chen Shu (陈殊) and neighbor 刘叔叔. 03:20–03:46: doctor tells mother Linda the terminal diagnosis; chapter 2 matches mother's discovery. 06:21–06:28: Ethan rescued Lauren from drowning; chapters 4 and 6 identify Chen Shu as Lan Xinyu's real rescuer, while she mistakes Li Zhennan for the rescuer. 07:07–07:25: protagonist refuses to continue tutoring the hostile friend; chapter 4 matches. Official Fanqie confirms title, author 月幻瞳, Chen Shu and the three-month prognosis. Recap names are localized; description calls protagonist Chen Xiaoyu, not the canonical original name. Viewer comment UgzMiYmt610Qm0TQhaV4AaABAg suggests an unverified English title, which was not used as canonical title or alias. Sources: https://www.youtube.com/watch?v=ui7WIFC4w1c ; https://fanqienovel.com/page/7243466617948998659 ; https://m.ilwxs.com/shu/115737/159630304.html ; https://m.ilwxs.com/shu/115737/159630305.html ; https://m.ilwxs.com/shu/115737/159630307.html ; https://m.ilwxs.com/shu/115737/159630309.html . Source identified as a Chinese web novel; no official English edition or specific comic adaptation verified. Player stayed black/loading at 0:00. Selected transcript passages inspected, not full-video viewing, frame comparison, reverse-image search or exact chapter-coverage verification."
})

# Cloud review 2026-11-11: native transcript and distinctive chapter-one scene match.
REVIEWED.append({
  "video_id": "J9d38r_UIJI",
  "title": "The King of Snow",
  "aliases": [
    "Frozen Apocalypse: No Chance of Survival",
    "Icebound Doom: No Way Out",
    "冰封末日：绝无生还之路"
  ],
  "reviewed_at": "2026-11-11",
  "confirmado": True,
  "evidence": "Exact-video public comment by @earcham explicitly names The King of Snow. Full expanded description contains generic tags, not title. Native YouTube transcript opening independently matches chapter 1 source panels inspected in the cloud browser: 00:24-00:37 protagonist scavenges in frozen city and recognizes earthquake; source image 6 shows goggled winter-clad protagonist and EARTHQUAKE dialogue. 01:01-01:19 ice collapse buries him; source image 12 visually shows falling ice and engulfing collapse, viewed at fit scale. 02:09-02:22 girlfriend Maisie complains that he brought only one chocolate bar; source image 20 enlarged shows ONLY ONE dialogue and opened chocolate bar. This ordered sequence is a specific scene match, not merely the snow-apocalypse premise. Recap names may be localized; no source-name equivalence claimed. MangaRead and Vortex pair the English title with original 冰封末日：绝无生还之路; MangaRead lists author/artist 漫潮社 and alias Frozen Apocalypse: No Chance of Survival. Icebound Doom: No Way Out is mapped by Onisaga indexed catalog; later direct fetch returned 403, so no direct-page verification claimed for that alias. Sources: https://www.youtube.com/watch?v=J9d38r_UIJI&lc=UgyOBGLb4xRrw9yKLLV4AaABAg ; https://www.youtube.com/watch?v=J9d38r_UIJI&t=24 ; https://www.youtube.com/watch?v=J9d38r_UIJI&t=61 ; https://www.youtube.com/watch?v=J9d38r_UIJI&t=129 ; https://www.mangaread.org/manga/the-king-of-snow/chapter-1/ ; https://www.mangaread.org/manga/the-king-of-snow/ ; https://vortexscans.org/series/the-king-of-snow-6201p9fx ; https://onisaga.com/title/icebound-doom-no-way-out . Top-sorted loaded comments inspected, not all replies/newest census. Source chapter panels were visually checked against native video transcript, not actual video frames. No full-video review, reverse-image search or exact chapter-coverage claim. Catalog/translation title, not asserted official English publication title."
})

# Cloud review 2026-11-11: fresh native transcript and official plot match.
REVIEWED.append({
  "video_id": "1L4Efjs4eoU",
  "title": "Rebirth in the Apocalypse: Rising to Power Through Loot Boxes",
  "aliases": [
    "Rebirth in the End Times: I Reached the Top by Opening Boxes",
    "Rebirth in the Apocalypse: Rising to Power Through Blind Boxes",
    "末世重生：我靠开箱子问鼎巅峰"
  ],
  "reviewed_at": "2026-11-11",
  "confirmado": True,
  "evidence": "Fresh exact-video native YouTube transcript independently matches official Tappytoon detailed plot: 00:00 introduces shelter leader Shiaoyong/Xiao Yong (phonetic ASR, surname not heard in sampled passage); 00:16-00:49 trusted woman admits enemies, zombies kill him and he wakes before apocalypse; 00:57 says one month; 01:06 introduces supply-box and physical-upgrade system; 04:16-04:38 he commissions a costly fortified factory; 06:34-07:06 bulk supplies and a mystery-box storage ring. Tappytoon names Jiang Xiaoyong, beloved woman's betrayal, death and one-month regression, loot-box survival system, expensive fortress and stockpiling. This specific character/event combination goes beyond uploader attribution. Pinned @MamoruManhwa comment names Reached the Top By Opening Boxes; expanded description is generic contact/tags. Official Tapas maps English title to original Chinese title and credits Penstyle Comics. MangaRead verifies End Times alias; WebComics verifies Blind Boxes alias. Publisher discrepancy retained: Tapas, WebComics and MangaRead say one year, whereas Tappytoon and exact-video transcript say one month. No chapter-panel match claimed: Tapas Episode 1 panel-image fetches returned 403 and were not bypassed. No full-video, frame comparison, reverse-image search or exact chapter-coverage claim. Sources: https://www.youtube.com/watch?v=1L4Efjs4eoU ; https://www.youtube.com/watch?v=1L4Efjs4eoU&lc=UgyUF2czvG2RS-ss5Md4AaABAg ; https://www.youtube.com/watch?v=1L4Efjs4eoU&t=16 ; https://www.youtube.com/watch?v=1L4Efjs4eoU&t=57 ; https://www.youtube.com/watch?v=1L4Efjs4eoU&t=66 ; https://www.youtube.com/watch?v=1L4Efjs4eoU&t=256 ; https://www.tappytoon.com/en/book/rebirth-in-the-apocalypse-rising-to-power-through-loot-boxes ; https://tapas.io/series/rebirth-in-the-apocalypse-rising-to-power-through-loot-boxes/info ; https://www.mangaread.org/manga/rebirth-in-the-end-times-i-reached-the-top-by-opening-boxes/ ; https://webcomicsapp.com/en/fantasy/rebirth-in-the-apocalypse-rising-to-power-through-blind-boxes/68fb1e4462661d2530656c92 ."
})

# Cloud review 2026-11-11: named opponent matches official serialized chapter.
REVIEWED.append({
  "video_id": "zFekpO4waK0",
  "title": "欠陥剣士は覇者になる",
  "aliases": [
    "The Flawed Swordsman Becomes a Conqueror",
    "Kekkan Kenshi wa Hasha ni Naru"
  ],
  "reviewed_at": "2026-11-11",
  "confirmado": True,
  "evidence": "Exact-video native Show transcript UI was readable although transcript export reported unavailable. 00:44 names Hundred Blade Grand Melee; 02:32-02:42 winner can have any wish granted and all 100 places are filled; 05:33 impostor David Evo calls himself Demon Blade Slayer; 14:23-14:39 special entrant blade 101 is Shu, the real Demon Blade Slayer; 20:44-20:53 and 27:03 name Simeon Valdar, Red Death, blade 66. Official LINE Manga serial synopsis independently identifies Shu, the Kadin Kingdom's hundred-fighter wish-prize tournament and Demon Blade Slayer challenger. Its named chapter 5 VS『赤き死』シメオン・ヴァルダル specifically matches the video's named opponent, establishing serial identity beyond the generic premise. Official title 欠陥剣士は覇者になる with creators 九岡望, SORAJIMA, vertwo, 卯太郎. Comicatch directly pairs the Japanese title with established English and romanized aliases; no claim of official English edition. Viewer comment suggests Sovereign of a Hundred Blades: Heir to the Strongest Style, but publisher separately catalogs 百刃の覇者〜最強の流派を継ぐ者〜 as a one-shot; do not silently merge it as a serial alias. Description generic tags, 7 top comments rendered out of 8 indicated. Transcript passages sampled, not full-video, visual panel comparison, reverse-image search or exact chapter-coverage review. Sources: https://www.youtube.com/watch?v=zFekpO4waK0 ; https://www.youtube.com/watch?v=zFekpO4waK0&t=44 ; https://www.youtube.com/watch?v=zFekpO4waK0&t=152 ; https://www.youtube.com/watch?v=zFekpO4waK0&t=863 ; https://www.youtube.com/watch?v=zFekpO4waK0&t=1244 ; https://www.youtube.com/watch?v=zFekpO4waK0&t=1623 ; https://manga.line.me/product/periodic?id=S163576 ; https://comicatch.com/title/58-the-flawed-swordsman-becomes-a-conqueror ; https://sorajimatoon.com/comics/01KQ6CG8R63WEVFR6K7XK4AFQS ; https://www.youtube.com/watch?v=zFekpO4waK0&lc=Ugz8h2I-xUS6LeiDMLJ4AaABAg ."
})


# Cloud review 2026-11-12: named protagonist and distinctive elf relationship.
REVIEWED.append({'video_id': 'rgMGoad5uqs',
 'title': 'Eldmia Ega, the Reincarnated Avenger',
 'aliases': ['Never touch Eldmia Egga', 'Absolutely Do Not Touch Eldmia Egga', '復讐の転生者エルドミア・エガ', '절대 엘드미아 에가를 건드리지 마라'],
 'reviewed_at': '2026-11-12',
 'confirmado': True,
 'evidence': 'Exact-video native YouTube transcript: 03:18 protagonist introduces himself as Elmia Ega (phonetic ASR); '
             "00:14 and 08:02 demon king's army destroys his village and family; 00:22 and 10:58 captive elf becomes "
             'his older-sister figure and magic teacher; 00:28 a hidden noble girl enters the story. Independently '
             'opened Kenmei catalog names Eldmia Ega/Eldomia and specifically joins a hometown destroyed by a demonic '
             'army, the elven mage as sister and master, and a girl from a fallen noble house. This distinctive name '
             'and character-role sequence confirms the series beyond the generic revenge premise. Elf is Ailia in ASR '
             'versus Alicie in Kenmei; no exact spelling equivalence claimed. Kenmei directly lists the English, '
             'Japanese and Korean aliases. English title is a catalog/translation title, not an asserted licensed '
             'English edition. Expanded description says name in comments and chapters 1-43 but supplies no title; all '
             'three visible Top comments lack identification. Eight-year contract is video-only; intro wording and '
             'three-years-earlier flashback differ, and no elapsed-time claim is used for confirmation. Player stayed '
             'black/buffering at 0:00, so no visual panel comparison, reverse-image search, full-video or exact '
             'chapter-coverage claim. Sources: https://www.youtube.com/watch?v=rgMGoad5uqs ; '
             'https://www.youtube.com/watch?v=rgMGoad5uqs&t=14 ; https://www.youtube.com/watch?v=rgMGoad5uqs&t=22 ; '
             'https://www.youtube.com/watch?v=rgMGoad5uqs&t=198 ; https://www.youtube.com/watch?v=rgMGoad5uqs&t=482 ; '
             'https://www.youtube.com/watch?v=rgMGoad5uqs&t=658 ; '
             'https://www.kenmei.co/series/eldmia-ega-the-reincarnated-avenger .'})

# Cloud review 2026-11-12: transcript matches official English and Korean synopsis.
REVIEWED.append({
  "video_id": "SGs6MCHfckc",
  "title": "The Zero-Mana Genius Assassin",
  "aliases": [
    "마력 제로 천재 암살자의 두번째 기회"
  ],
  "reviewed_at": "2026-11-12",
  "confirmado": True,
  "evidence": "Exact-video native YouTube transcript 00:34 names Van Krueger (ASR variation of official Ban Kruger); 00:41-01:12 magicless assassin helps his prince/friend take the throne, is betrayed, his family massacred, returns ten years into the past and enters the academy. 02:08-02:37 his family is alive again; the mana-less clan's physical strength and magical undetectability are emphasized. Official English WEBTOON synopsis identifies magicless Gerudi assassin Ban Kruger and the same enthronement/betrayal/massacre/regression/royal-academy sequence. Official Korean Naver synopsis names Ban and prince Heinz, ten-year regression and magicless academy ambition. These named character and plot matches establish identity beyond generic regression. Korean alias from official Naver. Video title age14 versus English synopsis fifteenth birthday is not used as exact match. Description and sampled comments lack title. No creator attribution because source credits differ; no full-video or visual-panel comparison claim. Sources: https://www.youtube.com/watch?v=SGs6MCHfckc&t=34s ; https://www.youtube.com/watch?v=SGs6MCHfckc&t=41s ; https://www.youtube.com/watch?v=SGs6MCHfckc&t=128s ; https://sg-m.webtoons.com/en/fantasy/the-zero-mana-genius-assassin/list?title_no=11445 ; https://m.comic.naver.com/webtoon/list?titleId=853831&week=dailyPlus ."
})

# Cloud review 2026-11-12: named protagonist and distinctive evolution sequence.
REVIEWED.append({
  "video_id": "6y7kvm2Kb-A",
  "title": "全民选择进化，我选孢子产氧气",
  "aliases": [],
  "reviewed_at": "2026-11-12",
  "confirmado": True,
  "evidence": "Exact-video native YouTube transcript 00:00-00:27 identifies Su Bai (ASR Subai), seven consecutive victories, oxygen spore and Great Oxidation killing 99.2% of anaerobic life, lunged fish escaping ocean hypoxia, and burrowing mouse/dormant crocodile surviving asteroid nuclear winter. 02:23-02:40 Su Bai orders species longevity jellyfish, shark, crocodile, human. 2:24:21-2:24:36 describes his steam-engine industrial foundation: mine pump, blast furnace, standardized parts, trained workers and safety valves. External Readnovel search-retrieved title/author/synopsis names 苏白, 单细胞孢子, photosynthesis and oxygen mass extinction; catalog chapters 7, 10-14, 18-25, 77-78 and 93-106 match the distinctive evolution sequence, seven-version settlement, trivia and industrial development. MTL-Novel independently lists same Chinese title and author 何时能起飞 as a secondary catalog. External sources retrieved through web search; direct opens returned 403/timeout, so no primary editorial page or chapter-reader access claimed. Description and pinned uploader comment link earlier parts, but continuity alone is not identity proof. Sampled native transcript only, no full-video or visual panel match. No alias inferred from uploader's English title. Sources: https://www.youtube.com/watch?v=6y7kvm2Kb-A&t=0 ; https://www.youtube.com/watch?v=6y7kvm2Kb-A&t=143 ; https://www.youtube.com/watch?v=6y7kvm2Kb-A&t=8661 ; https://m.readnovel.com/bookquery/zfiqskfoenur ; https://www.readnovel.com/bqx/sknjosamlw ; https://mtl-novel.com/novel/everyone-chooses-evolution-i-choose-spores-to-produce-oxygen/ ."
})


# Cloud review 2026-11-12: newly available transcript matches official Tapas.
REVIEWED.append({
  "video_id": "yVHqcn1b1Ik",
  "title": "The Return of the 8th Class Mage",
  "aliases": [
    "Return of the 8th Class Magician"
  ],
  "reviewed_at": "2026-11-12",
  "confirmado": True,
  "evidence": "Native YouTube transcript newly available: 01:39–02:21 names Ian, only eighth-class mage at age42, close friend Emperor Ragnar poisons him fearing his power; Ian uses a time-magic dagger and returns to age12. 03:08 names Green River capital. Official Tapas comic synopsis identifies Ian Paige, eighth-class mage serving Emperor Ragnar of Greenriver, poisoning and time magic returning thirty years into past. This specific named character and event sequence confirms identity. Top comments name Return of the 8th Class Magician; indexed independent discussion ties this alias to Ian, Ragnar and time dagger. Expanded description gives chapters1–62 but no title. Seventeen top-level comments observed of22 indicated; replies not exhaustive. Initial 00:00–03:16 and final 03:19:56–03:22:07 transcript sampled. No full-video viewing, actual scene-frame/panel comparison or exact chapter coverage verified. ASR names Ian, surname from official synopsis. Sources: https://www.youtube.com/watch?v=yVHqcn1b1Ik&t=99s ; https://tapas.io/series/the-return-of-the-8th-class-mage/info ; https://www.youtube.com/watch?v=yVHqcn1b1Ik&lc=UgzYz9wwniHAa63d8gp4AaABAg ; https://www.reddit.com/r/manhwa/comments/oeyuzq ."
})


# Cloud review 2026-11-13: native transcript matches official LINE Manga.
REVIEWED.append({
  "video_id": "0Qp_jDJPfmE",
  "title": "100 Million Years Later: The Ultimate Weapon’s Return",
  "aliases": [
    "最終兵器、1億年後に無双する",
    "The Ultimate Weapon, Overpowered 100 Million Years Later",
    "The Ultimate Weapon Returns After 100 Million Years"
  ],
  "reviewed_at": "2026-11-13",
  "confirmado": True,
  "evidence": "Native YouTube transcript 01:46–02:55 describes protagonist made into a weapon through human experiments, humanity nearly extinct and sleep lasting 100 million years. At 1:37:38–1:37:46 he introduces himself as Shido Jyn, matching official LINE Manga protagonist 祠堂仁（シドウ ジン）, Jin Shido. LINE official synopsis independently confirms named protagonist, experiments, Corruptors, near-extinction and awakening after 100 million years; SORAJIMA official catalog confirms Japanese original title. Scythe catalog associates English title and aliases with same original and story; English title is not claimed as official licensed edition. Specific named character and event sequence confirm identity, not uploader title alone. Sampled native transcript only; no full-video or visual panel comparison. Percentages differ in narration, not used as exact match. Piccoma Japan territorial restriction was not bypassed. Sources: https://www.youtube.com/watch?v=0Qp_jDJPfmE&t=106s ; https://www.youtube.com/watch?v=0Qp_jDJPfmE&t=5858s ; https://manga.line.me/product/periodic?id=S164684 ; https://sorajimatoon.com/comics/01KK0EHX9Y0969ZCDFSFC1SWGP ; https://scythescans.com/manga/100-million-years-later-the-ultimate-weapons-return/ ."
})


# Cloud review 2026-11-13: distinctive grave and school-regression scenes.
REVIEWED.append({
  "video_id": "0Kk18kUTX1Q",
  "title": "校花倒追我不要，我只爱小同桌",
  "aliases": [
    "校花别追了，爷的深情你不配",
    "爱上软萌小同桌，校花哭晕了"
  ],
  "reviewed_at": "2026-11-13",
  "confirmado": True,
  "evidence": "Native YouTube transcript 00:08–02:57: man dies driving to his school crush's wedding; shy deskmate visits his grave with a glass jar of surplus folded paper stars, opens hidden love notes, sticks them on the gravestone and dies beside it. His spirit cannot touch her and wishes for rebirth. Chapter 1 她的心願 reproduces this distinctive ordered scene. At 03:04–03:55 he asks his chubby friend the date, September 22, 2008; friend brought a camera for his 999th confession, but he refuses and clears his desk for the deskmate who will otherwise transfer next class. Chapter 2 重回高中 matches date, count and actions. Video localizes 叶林 / 兰呦呦 / 凌飞雪 as Ethan / Grace / Vivian; specific event sequence establishes identity, not assumed name equivalence alone. Source novel by 榴莲味的西瓜; exact animated adaptation version and official English title not established. Native transcript sampled 00:00–15:00; no full-video viewing or actual frame comparison. Secondary chapter/catalog sources, not claimed official publisher. Sources: https://www.youtube.com/watch?v=0Kk18kUTX1Q&t=38s ; https://www.youtube.com/watch?v=0Kk18kUTX1Q&t=184s ; https://m.wfxs.tw/xiaoshuo/2572003/79911397/ ; https://m.wfxs.tw/xiaoshuo/2572003/79911398/ ; https://www.uudwc.com/book/228640/ ; https://www.duanjubaike.net/xiaoshuo/info-7288544802038090812.html ."
})

