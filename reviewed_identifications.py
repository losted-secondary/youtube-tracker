"""Identificações revisadas: chave por vídeo, nunca pelo número de linha."""
import re

import confirmacao

REVIEWED = [
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
  "evidence": "Vídeo: https://www.youtube.com/watch?v=SDe-jgaZ9As. [{\"timestamp\":\"00:30\",\"seconds\":30,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=30s\",\"observation_paraphrase\":\"The protagonist has spent fifty years in a martial-arts world after traveling to a company workshop with Director Kim and colleagues.\",\"matches\":[\"Company workshop group\",\"Fifty-year first life\"]},{\"timestamp\":\"00:37\",\"seconds\":37,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=37s\",\"observation_paraphrase\":\"A landslide struck their vehicle before they awakened in a supernatural cultivation world.\",\"matches\":[\"Landslide transporting company coworkers\"]},{\"timestamp\":\"01:23\",\"seconds\":83,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=83s\",\"observation_paraphrase\":\"The immortals take the talented coworkers while the protagonist and Director Kim remain behind. Director Kim later becomes an exceptional martial artist.\",\"matches\":[\"Seo Eun-hyun and Kim Young-hoon left behind\",\"Kim Young-hoon’s martial talent\"]},{\"timestamp\":\"03:26–04:07\",\"seconds\":206,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=206s\",\"observation_paraphrase\":\"After dying, the hero wakes young beside his original coworkers and realizes that his ability returns him to that point after death.\",\"matches\":[\"Death triggers regression to first arrival\"]},{\"timestamp\":\"04:56–05:12\",\"seconds\":296,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=296s\",\"observation_paraphrase\":\"The transcript renders the protagonist’s name as Seong An Hun / Sean Hune and describes his hostile department head.\",\"matches\":[\"Seo Eun-hyun, with auto-transcription variation\"]},{\"timestamp\":\"08:10–08:27\",\"seconds\":490,\"url\":\"https://www.youtube.com/watch?v=SDe-jgaZ9As&t=490s\",\"observation_paraphrase\":\"Director Kim intervenes after the fight; the protagonist recalls that he will become a top martial artist. The auto-transcript varies his name as Kim and Hong / Kim Hyun.\",\"matches\":[\"Kim Young-hoon and his exceptional martial development\"]}] [{\"url\":\"https://server.haksanpub.co.kr/bbs/board.php?bo_table=m03_04&wr_id=149\",\"title\":\"회귀수선전\",\"type\":\"official publisher synopsis\",\"verification\":\"Public web search returned full publisher synopsis. Direct web and cloud-browser open failed; browser showed 502 Bad Gateway.\",\"supports\":\"Seven colleagues are caught in a landslide on a company workshop trip; Seo Eun-hyun receives no special powers, dies after fifty difficult years, and returns to the workshop day with infinite regression.\"},{\"url\":\"https://series.naver.com/novel/detail.series?productNo=9807283\",\"title\":\"회귀수선전(回歸修仙傳)\",\"type\":\"official original-novel catalog\",\"verification\":\"Public web search returned catalog and full synopsis.\",\"supports\":\"Names Seo Eun-hyun (서은현), the sole member of seven seemingly without awakened ability, and identifies infinite regression; credits 엄청난.\"},{\"url\":\"https://m.comic.naver.com/webtoon/list?titleId=839827\",\"title\":\"회귀수선전\",\"type\":\"official webtoon catalog\",\"verification\":\"Public web search returned title, creator credits, premise and chapter titles.\",\"supports\":\"The manhwa adaptation by 김무현 / 엄청난; talentless first life begins endless regressions; early chapter titles identify the director as a martial genius.\"},{\"url\":\"https://www.novelupdates.com/series/a-regressors-tale-of-cultivation/\",\"title\":\"A Regressor’s Tale of Cultivation\",\"type\":\"English/native title bridge and synopsis reference\",\"verification\":\"Public web direct open succeeded.\",\"supports\":\"English title maps to 회귀수선전 / 回歸修仙傳. Synopsis independently specifies the company workshop car trip, talented colleagues joining cultivation sects, fifty ordinary years and regression.\"},{\"url\":\"https://www.yoonseul.app/post/novel/24/32\",\"title\":\"서은현 (0~4회차) - 회귀수선전 해석\",\"type\":\"specific character/early-plot reference\",\"verification\":\"Public web search returned detailed Korean analysis.\",\"supports\":\"Names Seo Eun-hyun and Kim Young-hoon; company-workshop landslide, remaining behind while colleagues ascend, Kim’s martial genius, and regression after the first life.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "w_Nw_1MWZAg",
  "title": "The Necromancer Who Spares No Expense",
  "aliases": [
    "Damn Necromancer"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=w_Nw_1MWZAg. [{\"timestamp\":\"0:00\",\"seconds\":0,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=0s\",\"observation\":\"Kim Minu is the level-one protagonist attempting a dungeon clear. Transcript spelling corresponds to external Kim Min-woo / Kim Minwoo.\"},{\"timestamp\":\"0:07\",\"seconds\":7,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=7s\",\"observation\":\"Sword Peak Seo Yarim challenges the attempt. External glossary lists Seo Ye-rim.\"},{\"timestamp\":\"0:23\",\"seconds\":23,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=23s\",\"observation\":\"Dungeon named Osiris’s tomb.\"},{\"timestamp\":\"0:32\",\"seconds\":32,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=32s\",\"observation\":\"Cedric leads the skeleton army as a dragon knight. Death Lord boosts undead, halves summon mana cost, and provides a daily revival; matches external EX-rank Death Lord mechanics.\"},{\"timestamp\":\"1:21\",\"seconds\":81,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=81s\",\"observation\":\"Dungeon cleared in 2 hours 10 minutes; he conceals the speed by remaining inside.\"},{\"timestamp\":\"1:50\",\"seconds\":110,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=110s\",\"observation\":\"VR game explicitly called Gate Hunter.\"},{\"timestamp\":\"2:18\",\"seconds\":138,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=138s\",\"observation\":\"Player alias rendered Cuckaroo Ping Pong; external novel lists Kukurupingpong.\"},{\"timestamp\":\"2:42\",\"seconds\":162,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=162s\",\"observation\":\"Kim Minu is the eldest son of Ilsung Group; at 2:48 his character has five-star difficulty and a swordsman class.\"},{\"timestamp\":\"9:56\",\"seconds\":596,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=596s\",\"observation\":\"Final stage / phase 6 unlocks.\"},{\"timestamp\":\"11:25\",\"seconds\":685,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=685s\",\"observation\":\"Stage six is real, with only one life.\"},{\"timestamp\":\"11:49\",\"seconds\":709,\"url\":\"https://www.youtube.com/watch?v=w_Nw_1MWZAg&t=709s\",\"observation\":\"Player consciousness merges into Kim Minu’s body; at 12:56 he realizes he has possessed the Gate Hunter character.\"}] [{\"url\":\"https://page.kakao.com/content/70842032/?tab_type=about\",\"type\":\"official_primary_publisher\",\"access\":\"Direct cloud browser; about tab and expanded synopsis read successfully. Web fetch failed but ordinary browser page loaded.\",\"matches\":\"Official original title 돈지랄 네크로맨서; credited 백연발 (writing), 서민성 (art), 키보드만세 (original). Synopsis names Gate Hunter and Kim Woojin, Stage 6 becoming reality, possession of a wealthy talentless chaebol heir, and using money to equip necromancer summons.\"},{\"url\":\"https://qimanga.com/series/the-necromancer-who-spares-no-expense\",\"type\":\"external_title_catalog\",\"access\":\"Opened successfully via web tool.\",\"matches\":\"Places The Necromancer Who Spares No Expense beside 돈지랄 네크로맨서 and repeats the distinctive Gate Hunter / stage-six / wealthy untalented heir / necromancer premise.\"},{\"url\":\"https://asurascans.com/comics/the-necromancer-who-spares-no-expense-1bb35e56\",\"type\":\"external_english_series_page\",\"access\":\"Opened successfully via web tool.\",\"matches\":\"English title The Necromancer Who Spares No Expense, manhwa, KeyboardCheers; same Gate Hunter / Kim Woojin / stage-six / chaebol heir premise.\"},{\"url\":\"https://www.novellist.co/novels/damn-necromancer/glossary\",\"type\":\"external_character_glossary\",\"access\":\"Search index content read; direct web fetch cache miss.\",\"matches\":\"Damn Necromancer with native title 돈지랄 네크로맨서. Character list includes Kim Min-woo, Seo Ye-rim, Cedric, Osiris, Park Si-woo and Woo-jin.\"},{\"url\":\"https://helioscans.com/chapter/8d6e9837063-c9d2db55b53/\",\"type\":\"external_novel_chapter_5\",\"access\":\"Search index excerpt read; direct web fetch returned 403. No bypass attempted.\",\"matches\":\"Damn Necromancer: level-one Kim Minwoo, Death Lord (EX), undead daily revival, +50% stats, -50% mana cost, and Chairman Kim supporting the Ilsung heir.\"},{\"url\":\"https://paitohkwarna.org/novelpaito/damn-necromancer-2/chapter-1\",\"type\":\"external_novel_chapter_1\",\"access\":\"Search index content read.\",\"matches\":\"Kukurupingpong login, character lineup with Seo Yerim, five-star Kim Minwoo as eldest son of Ilsung Group, Dragon Lord goal and stage-six transition.\"},{\"url\":\"https://exnovels.com/series/damn-necromancer\",\"type\":\"external_alias_catalog\",\"access\":\"Search index content read; direct web fetch unavailable.\",\"matches\":\"Explicitly joins Damn Necromancer, 돈지랄 네크로맨서 and The Necromancer Who Spares No Expense.\"}]",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "ny5AUrrnEkg",
  "title": "A Painter Who Draws Dungeons",
  "aliases": [
    "The Painter Who Draws Dungeons",
    "The Dungeon Painter",
    "The Artist Who Paints Dungeons"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=ny5AUrrnEkg. [{\"url\":\"https://ridibooks.com/books/6305000001\",\"source\":\"RIDI official original webtoon page\",\"verified_by\":\"Public web open at 2026-10-17T22:16:57Z\",\"title\":\"던전을 그리는 화가\",\"summary\":\"Official synopsis names art teacher Seo Jio (서지오), his death in a sudden fire, absorption into a portrait, and powers to create life and open dimensional gates.\",\"source_role\":\"Primary original-title and story-identity confirmation\",\"creators\":{\"art\":\"글리\",\"story\":\"오솟\",\"original_story\":\"취미글주의\"}},{\"url\":\"https://anilist.co/manga/213942/Dungeon-eul-Geurineun-Hwaga/\",\"source\":\"AniList indexed entry\",\"verified_by\":\"Search result at 2026-10-17T22:16:18Z; direct open later returned 403\",\"title\":\"Dungeon-eul Geurineun Hwaga\",\"summary\":\"Lists native title 던전을 그리는 화가, English aliases A Painter Who Draws Dungeons / The Artist Who Paints Dungeons / The Dungeon Painter, protagonist Ji-O Seo, and supporting character Bisabeol.\",\"source_role\":\"Romanization, English-title aliases, and character corroboration\"},{\"url\":\"https://mangatime.net/catalog/the-painter-who-draws-dungeons/\",\"source\":\"MangaTime catalog search result\",\"verified_by\":\"Public web search at 2026-10-17T22:16:18Z\",\"title\":\"The Painter Who Draws Dungeons\",\"summary\":\"Lists the same native title and romanization; synopsis matches art teacher Seo Jio, fire, portrait world, and creation powers.\",\"source_role\":\"Alternative common English title corroboration\"}] [{\"timestamp\":\"00:00\",\"seconds\":0,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=0\",\"kind\":\"YouTube visible transcript\",\"summary\":\"Transcript names Gio and Siangun and describes a chained young mermaid.\"},{\"timestamp\":\"00:14\",\"seconds\":14,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=14\",\"kind\":\"YouTube visible transcript\",\"summary\":\"A young painter runs through a burning school toward the art classroom.\"},{\"timestamp\":\"00:24–00:40\",\"seconds\":24,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=24\",\"kind\":\"YouTube visible transcript\",\"summary\":\"His favorite painting shines amid the fire; he enters its green world and finds the cottage he had drawn.\"},{\"timestamp\":\"01:02\",\"seconds\":62,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=62\",\"kind\":\"YouTube visible transcript\",\"summary\":\"Painted apples become tangible and fall from the canvas; the power also works for tools, flowers, and trees.\"},{\"timestamp\":\"01:18–01:34\",\"seconds\":78,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=78\",\"kind\":\"YouTube visible transcript\",\"summary\":\"A frame lets Gio see the outside world. More than thirty years have elapsed since the fire, and hunters now fight monsters.\"},{\"timestamp\":\"04:38\",\"seconds\":278,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=278\",\"kind\":\"YouTube visible transcript\",\"summary\":\"An S-class hunter and guild owner with appraisal powers appears; the transcript renders his name as Bisabiel.\"},{\"timestamp\":\"11:31\",\"seconds\":691,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=691\",\"kind\":\"YouTube visible transcript\",\"summary\":\"An employee reports that the figure in the painting gave his name as Seo Gio.\",\"exact_name\":\"Seo Gio\"},{\"timestamp\":\"12:57\",\"seconds\":777,\"url\":\"https://www.youtube.com/watch?v=ny5AUrrnEkg&t=777\",\"kind\":\"YouTube visible transcript\",\"summary\":\"The transcript again identifies the portrait as belonging to Seo Gio.\"}] Direct transcript uniquely combines Seo Gio, the school fire, entering his own painting, and creations becoming real. RIDI identifies Seo Jio and the same unusual plot under the original Korean webtoon title. AniList supplies matching title aliases. Spelling differences in the visible transcript are treated as transcription variants, not independent characters.",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "ittAzN3CNDk",
  "title": "I Became the Berserker of the World I Created",
  "aliases": [
    "I Became a Barbarian in the World I Created",
    "내가 만든 세계 속 광전사가 되었다",
    "俺が創った世界の狂戦士になった"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=ittAzN3CNDk. [{\"at\":\"00:00–00:16\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=0s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"Opening introduces Attilla, Floran, lack of magic and barbarian survival.\"},{\"at\":\"00:24–00:48\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=24s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"A system identifies Charles Einhard as the scenario protagonist and strongest warrior; his opponent is the original author reincarnated as an extra.\"},{\"at\":\"02:02–02:26\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=122s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"Sato Shoda is a novelist whose 400-chapter heroic-sovereign saga will become a game; a contract precedes his fall from a building.\"},{\"at\":\"03:43–04:09\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=223s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"The stranger sends the writer into the world he created; a system welcomes him to his own novel's world.\"},{\"at\":\"06:04–07:57\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=364s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"A woman recognizes Attilla; the system profile gives age 16; memories reveal his death during a coming-of-age bear hunt caused by a conspiracy.\"},{\"at\":\"08:31–09:16\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=511s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"They reach the Black Wolf tribe. His father, rendered Munuk/Munzuk in the automatic transcript, is its chief and legendary warrior.\"},{\"at\":\"2:31:45–2:32:26\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=9105s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"At night camp the party sleeps in a tent while the hunter sits at a fire, thinking about Botri and her lost observer.\"},{\"at\":\"2:32:33–2:32:57\",\"url\":\"https://www.youtube.com/watch?v=ittAzN3CNDk&t=9153s\",\"type\":\"timestamped transcript\",\"paraphrase\":\"A hooded visitor sits by the campfire; the protagonist demands the news; the visitor warns that their leader has made a move. The cue cuts off mid-sentence immediately before video end.\"}] [{\"url\":\"https://m.comic.naver.com/webtoon/list?titleId=845644\",\"kind\":\"official publisher comic listing\",\"title\":\"내가 만든 세계 속 광전사가 되었다\",\"verified\":\"Opened through public web tool.\",\"supports\":[\"Official Korean series identity\",\"Novelist enters his own novel as Attila\",\"Father is tribal chief Munjuk\",\"Original protagonist Charles\",\"Comic chapter 40 exists\"],\"notes\":\"Current official listing shows 48 chapters. This is catalog availability, not evidence that the recap covers chapter 48.\"},{\"url\":\"https://manga.line.me/product/periodic?id=S155841\",\"kind\":\"official Japanese publisher/distributor listing\",\"title\":\"俺が創った世界の狂戦士になった\",\"verified\":\"Opened through public web tool.\",\"supports\":[\"Japanese title alias\",\"Same Attila/Munjuk/Charles synopsis\",\"Mercistar and studio author credits\"],\"notes\":\"Listing displayed a 40-episode collection; used for identity corroboration, not as sole endpoint evidence.\"},{\"url\":\"https://mangatime.net/catalog/i-became-the-berserker-of-the-world-i-created/\",\"kind\":\"English catalog search result\",\"title\":\"I Became the Berserker of the World I Created\",\"verified\":\"Search result indexed title, Korean/Japanese aliases and matching synopsis; direct open returned internal error.\",\"supports\":[\"English title bridge to official Korean/Japanese titles\"]},{\"url\":\"https://www.novelupdates.com/series/i-became-a-barbarian-in-the-world-i-created/?grr=1\",\"kind\":\"novel catalog\",\"title\":\"I Became a Barbarian in the World I Created\",\"verified\":\"Public search result.\",\"supports\":[\"Alternative English novel title\",\"Same Korean title\",\"Adapted-to-manhwa classification\"]},{\"url\":\"https://www.webnovel.com/book/34361046000997705/92260134637598525\",\"kind\":\"public English novel-text result\",\"title\":\"I Became a Barbarian in the World I Created, chapter 7\",\"verified\":\"Public search result with chapter text.\",\"supports\":[\"Attila\",\"Charles Ainheart spelling variant\",\"Bawang Hero Chronicle\",\"Munjuk and Black Wolf tribe\"],\"notes\":\"Secondary corroboration only; official publisher synopsis and direct video transcript drive identity.\"},{\"url\":\"https://vortexscans.org/series/i-became-the-berserker-of-the-world-i-created/chapter-40\",\"kind\":\"public English chapter reader\",\"title\":\"I Became the Berserker of the World I Created Chapter 40\",\"verified\":\"Opened in cloud browser; chapter label and final panels visually inspected.\",\"supports\":[\"Exact English comic title\",\"Independent chapter-40 ending match\"],\"visual_evidence\":[{\"reader_page_indicator\":\"35/36\",\"observation\":\"Dark-haired muscular protagonist and hooded, stubbled visitor sit by a campfire at night.\"},{\"reader_page_indicator\":\"35/36\",\"observation\":\"Protagonist demands that the visitor explain his news.\"},{\"reader_page_indicator\":\"35–36/36\",\"observation\":\"Visitor says the commander has started making his move; final suspense bubble begins to identify his target.\"}],\"comparison\":\"Matches video transcript at 2:32:33–2:32:57, beyond the generic barbarian premise.\"}]",
  "reviewed_at": "2026-10-18",
  "confirmado": True
},
{
  "video_id": "drQuFnCqj8E",
  "title": "My Brother Is a Mad Dog",
  "aliases": [
    "My Brother Is A Mad Dog",
    "My Brother is a Vicious Dog",
    "Wo de Gege Shi E Quan",
    "My Brother is a Fierce Dog"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=drQuFnCqj8E. {\"accessMethod\":\"Expanded the public YouTube description, clicked Show transcript, and read timestamped transcript buttons in the cloud browser accessibility tree.\",\"transcriptAvailable\":true,\"transcriptLanguageObserved\":\"English text\",\"transcriptAutomaticStatus\":\"Not verified; spellings of names vary substantially within the displayed transcript.\",\"reviewScope\":\"Read opening identity-establishing material through 12:55, plus observed later transcript availability. This was identification research, not a claim of watching or reviewing the entire 76-minute video.\",\"anchors\":[{\"start\":\"00:00\",\"end\":\"00:25\",\"seconds\":0,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=0s\",\"observedNarrative\":\"A timid younger brother is repeatedly bullied; his older brother is an exceptional street fighter reportedly able to defeat more than 100 thugs. The premise asks what happens when the brothers exchange identities.\"},{\"start\":\"00:37\",\"end\":\"01:22\",\"seconds\":37,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=37s\",\"observedNarrative\":\"An Ran wants only to study and avoid the school's factions. He is bullied, feels abandoned by his family, and decides to run away.\"},{\"start\":\"04:00\",\"end\":\"04:24\",\"seconds\":240,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=240s\",\"observedNarrative\":\"The rescuer, whose name appears in several phonetic variants of Jin Yansheng, was adopted by Old Jin, an auto-repair-shop owner. He is a local street fighter known as Mad Dog.\"},{\"start\":\"05:23\",\"end\":\"05:34\",\"seconds\":323,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=323s\",\"observedNarrative\":\"The older twin earns money so that his adoptive father Old Jin can receive treatment for his legs.\"},{\"start\":\"05:50\",\"end\":\"06:42\",\"seconds\":350,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=350s\",\"observedNarrative\":\"After the rescue, the boys discover their identical faces. An Ran explains that his twin was presumed dead after a hospital fire shortly after birth, although the body was never found.\"},{\"start\":\"06:51\",\"end\":\"07:52\",\"seconds\":411,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=411s\",\"observedNarrative\":\"An Ran offers the fighter one million yuan to attend school in his place and confront the bullies, warning him about powerful families and criminal connections and requiring that he avoid school disciplinary action. The offer itself occurs at 06:58.\"},{\"start\":\"08:00\",\"end\":\"08:37\",\"seconds\":480,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=480s\",\"observedNarrative\":\"They agree to a complete identity exchange. An Ran will stay in the fighter's neighborhood and pretend to be ill; Jin Yansheng enters the elite school as An Ran the next morning.\"},{\"start\":\"10:20\",\"end\":\"11:24\",\"seconds\":620,\"url\":\"https://www.youtube.com/watch?v=drQuFnCqj8E&t=620s\",\"observedNarrative\":\"On a camera-free school rooftop, the disguised older twin stops pretending to be helpless and fights the bully and his followers with a fly swatter. This additional distinctive incident was read directly in the transcript.\"}]} [{\"source\":\"Tencent Comics official listing\",\"url\":\"https://ac.qq.com/Comic/comicInfo/id/657728\",\"access\":\"Direct cloud-browser success; mobile URL redirected to this desktop listing.\",\"observedUTC\":\"2026-10-18T19:17:22Z\",\"facts\":[\"Page title and H1 name 我的哥哥是恶犬.\",\"Author field names 番奇动漫.\",\"Synopsis names 安然 and 金炎生 and explicitly describes long-separated twin brothers exchanging identities: the older enters the elite school; An Ran must survive the slums under his brother's fearsome nickname.\",\"Listing is marked ongoing and exclusive; chapter 37 was dated 2026.10.16.\",\"The original-work title, both named protagonists, twin relationship, identity swap and contrasting school/slum settings align with the direct video transcript.\"],\"role\":\"Primary identity confirmation\"},{\"source\":\"ReiManga title listing\",\"url\":\"https://reimanga.net/manga/my-brother-is-a-mad-dog-109068\",\"access\":\"Public web search and successful page retrieval\",\"observedUTC\":\"2026-10-18T19:17:22Z\",\"facts\":[\"Heading uses My Brother Is A Mad Dog with native title 我的哥哥是恶犬.\",\"Summary names An Ran and Jin Yan Sheng and describes the same school/slum twin-identity swap.\",\"Summary prose also uses the variant My Brother is a Fierce Dog.\"],\"role\":\"Secondary English title and spelling corroboration\"},{\"source\":\"AniList indexed catalogue listing\",\"url\":\"https://anilist.co/manga/214496/Wo-de-Gege-Shi-E-Quan/stats\",\"access\":\"Search-index content available; direct web retrieval returned 403 and cloud browser displayed Cloudflare access block.\",\"observedUTC\":\"2026-10-18T19:17:02Z\",\"facts\":[\"Romanized title Wo de Gege Shi E Quan; native title 我的哥哥是恶犬.\",\"Indexed synonyms My Brother is a Vicious Dog and My Brother Is A Mad Dog.\",\"Indexed synopsis names An Ran and Jin Yansheng and attributes its translated synopsis to Tencent.\"],\"role\":\"Secondary alias evidence only; direct-page access was not successful\"}] The direct video supplies both protagonists, the older twin's dog nickname, their childhood separation, and the full elite-school/slum identity exchange. The official Tencent synopsis independently names both protagonists and this same distinctive arrangement. This is a character-and-plot match supported by a primary publisher listing, not a title/thumbnail guess.",
  "reviewed_at": "2026-10-18",
  "confirmado": True
},
{
  "video_id": "U19JW2uFGhY",
  "title": "The Reborn Prodigy of the Ducal Family",
  "aliases": [
    "Dukedom’s Legendary Prodigy"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=U19JW2uFGhY. Direct video transcript gives Dale’s prior life as Earth resistance commander, forced summoning and imperial servitude, Brandenburg’s betrayal, the reincarnation stone, and rebirth as Duke Saxon’s son. Official WEBTOON independently matches Hanseong, Earth resistance, imperial enslavement, the stone, Dale and revenge. Naver’s Korean catalogue independently matches Hanseong and Dale of the Saxen ducal family. Kakao’s official manhwa catalogue confirms the Korean title and creators, consistent with WEBTOON. Novel Updates links the English alternate title with the same Korean original and plot. [{\"timestamp\":\"00:00–00:15\",\"start_seconds\":0,\"url\":\"https://www.youtube.com/watch?v=U19JW2uFGhY&t=0s\",\"summary\":\"Dale is introduced as a reincarnated mage prodigy before age ten.\"},{\"timestamp\":\"01:11–01:53\",\"start_seconds\":71,\"url\":\"https://www.youtube.com/watch?v=U19JW2uFGhY&t=71s\",\"summary\":\"Earth in 2045 faces monsters; Hanung is commander of humanity’s last resistance.\"},{\"timestamp\":\"02:03–03:22\",\"start_seconds\":123,\"url\":\"https://www.youtube.com/watch?v=U19JW2uFGhY&t=123s\",\"summary\":\"Mages summon and restrain him, forcing him to serve the Empire and defeat demon king Valdor.\"},{\"timestamp\":\"04:23–05:35\",\"start_seconds\":263,\"url\":\"https://www.youtube.com/watch?v=U19JW2uFGhY&t=263s\",\"summary\":\"Brandenburg betrays him; the reincarnation stone saves him as Duke Saxon’s son in Necropolis; he plans revenge.\"},{\"timestamp\":\"06:30–06:46\",\"start_seconds\":390,\"url\":\"https://www.youtube.com/watch?v=U19JW2uFGhY&t=390s\",\"summary\":\"Eight years after rebirth as Dale, his mother reminds Saxon not to teach their son necromancy.\"},{\"timestamp\":\"08:16–09:01\",\"start_seconds\":496,\"url\":\"https://www.youtube.com/watch?v=U19JW2uFGhY&t=496s\",\"summary\":\"Blue Tower elf water-magic teacher Sephia arrives; the mother’s marriage condition explains the dark-magic prohibition.\"}] [\"https://www.youtube.com/watch?v=U19JW2uFGhY\",\"https://www.webtoons.com/en/action/the-reborn-prodigy-of-the-ducal-family/list?title_no=9719\",\"https://webtoon.kakao.com/content/%EA%B3%B5%EC%9E%91%EA%B0%80%EC%9D%98-%EC%97%AD%EB%8C%80%EA%B8%89-%EC%8B%A0%EB%8F%99/4665\",\"https://m.series.naver.com/novel/detail.series?bannerChanged=false&productNo=8423892\",\"https://www.novelupdates.com/series/dukedoms-legendary-prodigy/\"] Confirmed via direct YouTube transcript: 01:45 Earth resistance commander; 02:03–03:22 summoned/enslaved by Empire; 04:23–05:35 Brandenburg betrayal, reincarnation stone, Duke Saxon’s son. Matches official WEBTOON synopsis (title_no=9719), Naver original (productNo=8423892), and Kakao original title 공작가의 역대급 신동. Alias: Dukedom’s Legendary Prodigy (Novel Updates).",
  "reviewed_at": "2026-10-18",
  "confirmado": True
},
{
  "video_id": "6m8Q5iL1RtU",
  "title": "The Berserker’s Second Playthrough",
  "aliases": [
    "The Berserker’s Second Playthrough in the Game"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=6m8Q5iL1RtU. [{\"timestamp\":\"00:23–01:42\",\"summary\":\"Kadim, warrior of Atala, travels with Melissa, Gale, Cyril and Gordon. A modern man trapped in the game must help the chosen hero defeat the great demon.\",\"url\":\"https://www.youtube.com/watch?v=6m8Q5iL1RtU&t=23s\"},{\"timestamp\":\"01:51–03:16\",\"summary\":\"Blood Berserker gains power by drinking demon blood, risking sanity. Melissa stops his frenzy.\",\"url\":\"https://www.youtube.com/watch?v=6m8Q5iL1RtU&t=111s\"},{\"timestamp\":\"03:45–05:07\",\"summary\":\"Defeats the archdemon and enters the exit expecting home, but discovers New Game Plus.\",\"url\":\"https://www.youtube.com/watch?v=6m8Q5iL1RtU&t=225s\"},{\"timestamp\":\"05:53–06:08\",\"summary\":\"Awakens chained with his old body and lost strength.\",\"url\":\"https://www.youtube.com/watch?v=6m8Q5iL1RtU&t=353s\"},{\"timestamp\":\"14:44–16:29\",\"summary\":\"Merchant does not recognize companions, reveals roughly 300 years elapsed, and locates Melissa’s mage tower in Vistana, eastern Free City Alliance.\",\"url\":\"https://www.youtube.com/watch?v=6m8Q5iL1RtU&t=884s\"},{\"timestamp\":\"1:27:38–1:28:40\",\"summary\":\"Kadim and Duncan confront a regenerating two-tailed snake and hooded Nazarin.\",\"url\":\"https://www.youtube.com/watch?v=6m8Q5iL1RtU&t=5258s\"}] [{\"url\":\"https://series.naver.com/novel/detail.series?productNo=9877375\",\"type\":\"Official original novel\",\"supports\":\"Original Korean title, author 인생망했음, possessed berserker defeats the archdemon and discovers New Game+.\"},{\"url\":\"https://www.webnovel.com/book/34881114700660105/93650952287999071\",\"type\":\"Secondary translation, chapter 4, not verified official\",\"supports\":\"Kadim and Duncan Wheeled; Lucaonia became an empire, about 300 years elapsed, Melissa’s magic tower in Vesta and companions Gale, Gordon, Cyril.\"},{\"url\":\"https://www.webnovel.com/book/the-berserker%E2%80%99s-second-playthrough_34715177600132105/chapter-1_93202322687065417\",\"type\":\"Secondary translation, chapter 1, not verified official\",\"supports\":\"Kadim’s demon-blood berserker ability, companions and archdemon exit.\"}] [\"Original comic link https://comic.naver.com/webtoon/list?titleId=846173 redirected to Naver login; no sign-in or restriction bypass attempted.\",\"Automatic transcript spells some names differently. Identification rests on the combined character group and distinctive sequential plot, not title similarity.\"]",
  "reviewed_at": "2026-10-18",
  "confirmado": True
},
{
  "video_id": "kh6LSXGwPII",
  "title": "I Incarnate the Undead Scourge",
  "aliases": [
    "技能无冷却？我化身亡灵天灾！",
    "With a No-Cooldown Cheat, I Can Transform Into an Undead Calamity!",
    "No Cooldown: Undead Catastrophe",
    "No Skill Cooldown? I've Become the Undead Scourge!",
    "No Skill Cooldowns? I Am the Undead Calamity!"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=kh6LSXGwPII. [{\"url\":\"https://ac.qq.com/Comic/comicInfo/id/657540\",\"type\":\"primary_publisher_catalog\",\"access\":\"Live cloud-browser UI\",\"verified\":\"Exact native title, creator 初格文化, ongoing manhua and original chapter catalogue.\",\"caveat\":\"No recap chapter span inferred.\"},{\"url\":\"https://www.readnovel.com/bookquery/wzamoszflw\",\"type\":\"primary_publisher_original_novel_excerpt\",\"access\":\"Search engine full indexed excerpt; subsequent direct web-tool open had cache error\",\"verified\":\"Original opening names 陆然 and 秦舞瑶, explicitly gives 130 and 104 points, ordinary necromancer versus SSS 空间行者, and the zero-cooldown trait.\"},{\"url\":\"https://m.hongxiu.com/bookquery/qbclfoenamfo\",\"type\":\"primary_publisher_original_novel_excerpt\",\"access\":\"Search indexed excerpt; direct web-tool open returned 403 and was not bypassed\",\"verified\":\"Yuewen copyright notice, exact native title and 寨子的明星; Lu Ran necromancer, new traits every five levels, zero cooldown and damage redirected to summons.\"},{\"url\":\"https://www.webnovel.com/book/undead-mage-with-no-skill-cooldown_33082124308863105/chapter-2-we%E2%80%99re-not-from-the-same-world_90932821836755427\",\"type\":\"secondary_translation_unverified_license\",\"access\":\"Web tool full chapter text\",\"verified\":\"Lu Ran, Wang Yujiao, Liang Shaoyu and Qin Wuyao; breakup, Magic Archer, financed leveling, three recruitment places and 130 spiritual power.\",\"caveat\":\"English novel title Undead Mage with No Skill Cooldown is a secondary translation title; not treated as official manhua title.\"},{\"url\":\"https://mangabaka.org/manhua/600178/I-Incarnate-the-Undead-Scourge\",\"type\":\"secondary_catalog\",\"access\":\"Live cloud browser including title-alias popup\",\"verified\":\"English title, listed aliases, original native title, creator 初格文化, and direct Original Webtoon link to Tencent comic id 657540.\"}] [{\"timestamp_start\":\"00:17\",\"timestamp_end\":\"01:06\",\"url\":\"https://www.youtube.com/watch?v=kh6LSXGwPII&t=17s\",\"summary\":\"Lu Ran trained for three years, achieved 130 points, but awakened an ordinary necromancer class.\"},{\"timestamp_start\":\"01:22\",\"timestamp_end\":\"01:30\",\"url\":\"https://www.youtube.com/watch?v=kh6LSXGwPII&t=82s\",\"summary\":\"The student president, transcribed inconsistently as Chinua/Chin Wa, has 104 points and SSS Space Walker.\"},{\"timestamp_start\":\"02:16\",\"timestamp_end\":\"05:30\",\"url\":\"https://www.youtube.com/watch?v=kh6LSXGwPII&t=136s\",\"summary\":\"Wang Yujiao, a rare magic archer, ends the relationship; Liang Shaoyu boasts about family-funded leveling; recruitment has three academy places, one already effectively reserved.\"},{\"timestamp_start\":\"11:30\",\"timestamp_end\":\"11:43\",\"url\":\"https://www.youtube.com/watch?v=kh6LSXGwPII&t=690s\",\"summary\":\"Lu Ran unlocks cooldown elimination, reducing class-skill cooldowns to zero.\"},{\"timestamp_start\":\"15:20\",\"timestamp_end\":\"17:09\",\"url\":\"https://www.youtube.com/watch?v=kh6LSXGwPII&t=920s\",\"summary\":\"Traits develop every five levels; he obtains corpse explosion and damage transfer, redirecting 100% of damage to a chosen summon.\"},{\"timestamp_start\":\"1:09:53\",\"timestamp_end\":\"1:10:32\",\"url\":\"https://www.youtube.com/watch?v=kh6LSXGwPII&t=4193s\",\"summary\":\"A mercenary's wound transfers to a skeleton; buried skeletons immobilize two attackers, then explode as Lu Ran leaves.\"}] Confirmado em 19/10/2026 via transcrição nativa do vídeo e fontes chinesas. 00:17–01:30: Lu Ran tem 130 pontos, mas desperta necromante comum; Qin Wuyao tem 104 e recebe Space Walker SSS. 02:16–05:30: Wang Yujiao, arqueira mágica, rompe com ele e acompanha Liang Shaoyu. 11:30: cooldown zerado. 16:55–17:09: transferência de 100% do dano para invocações. O texto original da Readnovel/Yuewen repete os nomes e os números; Tencent confirma o título chinês e 初格文化. Fonte original: https://ac.qq.com/Comic/comicInfo/id/657540 . Enredo original: https://www.readnovel.com/bookquery/wzamoszflw . I Incarnate the Undead Scourge e demais aliases ingleses são variantes de catálogo secundário: https://mangabaka.org/manhua/600178/I-Incarnate-the-Undead-Scourge . Não foi inferido intervalo de capítulos.",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "0bOi9R_3TRg",
  "title": "重生之我觉醒天赋技能无限复制",
  "aliases": [
    "Reborn: I Awakened Talent Skills with Unlimited Copying"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=0bOi9R_3TRg. [{\"url\":\"https://fanqienovel.com/page/7396229726274063385\",\"type\":\"primary_original_publisher\",\"access\":\"Web tool official catalog\",\"verified\":\"Exact Chinese title, author 千尘书书, protagonist 林万江, prior betrayal and death, rebirth, unlimited copying and copying immortality first.\"},{\"url\":\"https://fanqienovel.com/reader/7396229729679852057\",\"type\":\"primary_original_chapter\",\"access\":\"Web tool public chapter text\",\"verified\":\"Opening scene matches the phone date/time September22 Year38 at 7:44am, five-year regression, ambush, Five Elements Academy, 8am closing, and the old opposite-sex-attraction ability.\",\"caveat\":\"Some extracted glyphs are substituted by the site's display font; surrounding readable Chinese and precise scene sequence establish the match without accessing hidden resources.\"},{\"url\":\"https://fanqienovel.com/reader/7398050547678331417\",\"type\":\"primary_original_chapter\",\"access\":\"Web tool public chapter text\",\"verified\":\"徐言 awakens 不死之身; Liu Hui and Li Mu are named, Yan Rushuang has beast taming, and the chapter is titled 觉醒技能：无限复制.\"},{\"url\":\"https://daosearch.io/fanqie/book/7396229726274063385/reborn-i-awakened-talent-skills-with-unlimited-copying\",\"type\":\"secondary_machine_translated_catalog\",\"access\":\"Live cloud-browser UI\",\"verified\":\"English alias and native title on same page, author and exact Fanqie book link; Lin Wanjiang's copying/immortality premise.\",\"caveat\":\"Page explicitly labels the catalog translation as machine-translated; no official/licensed English edition claimed.\"}] [{\"timestamp_start\":\"00:00\",\"timestamp_end\":\"00:47\",\"url\":\"https://www.youtube.com/watch?v=0bOi9R_3TRg&t=0s\",\"summary\":\"Narrator awakens after his fiancée killed him, sees September 22, Year 38, at 7:44am, realizes he returned five years, and races to the Five Elements Academy before 8am after a blow previously caused him to miss awakening.\"},{\"timestamp_start\":\"02:45\",\"timestamp_end\":\"03:15\",\"url\":\"https://www.youtube.com/watch?v=0bOi9R_3TRg&t=165s\",\"summary\":\"In the prior life he instead awakened on March 21; his useless ability increased attraction from the opposite sex.\"},{\"timestamp_start\":\"05:15\",\"timestamp_end\":\"07:24\",\"url\":\"https://www.youtube.com/watch?v=0bOi9R_3TRg&t=315s\",\"summary\":\"Yan Rushuang addresses him as Lin Wanjiang. His former fiancée has Beast Taming, exploited his inheritance and finally killed him.\"},{\"timestamp_start\":\"16:13\",\"timestamp_end\":\"17:18\",\"url\":\"https://www.youtube.com/watch?v=0bOi9R_3TRg&t=973s\",\"summary\":\"Another student awakens Immortality; the prior known holder is supreme leader Lin Xiangtian.\"},{\"timestamp_start\":\"22:40\",\"timestamp_end\":\"25:27\",\"url\":\"https://www.youtube.com/watch?v=0bOi9R_3TRg&t=1360s\",\"summary\":\"Lin awakens Infinite Copy and hidden Spirit Sight; he can copy abilities and essence crystals but not living organisms.\"},{\"timestamp_start\":\"28:35\",\"timestamp_end\":\"28:51\",\"url\":\"https://www.youtube.com/watch?v=0bOi9R_3TRg&t=1715s\",\"summary\":\"He pats Xu Yan on the shoulder and successfully copies Immortality.\"}] Confirmado em 19/10/2026 por transcrição nativa e original oficial Fanqie, sem depender de comentários. 00:00–00:47: Lin Wanjiang volta cinco anos, encontra no telefone 22/09, ano 38, 7h44, e corre para a Academia dos Cinco Elementos antes das 8h. 05:15–07:24: Yan Rushuang é a ex-noiva que o matou. 22:40: desperta Infinite Copy; 28:45: copia Immortality de Xu Yan. O capítulo inicial oficial repete a sequência singular, data e horário: https://fanqienovel.com/reader/7396229729679852057 . Catálogo original e autor 千尘书书: https://fanqienovel.com/page/7396229726274063385 . Alias inglês de catálogo secundário com tradução automática: Reborn: I Awakened Talent Skills with Unlimited Copying, https://daosearch.io/fanqie/book/7396229726274063385/reborn-i-awakened-talent-skills-with-unlimited-copying . A origem em novel está confirmada; edição manhua separada e edição inglesa licenciada não estabelecidas. Não foi inferido intervalo de capítulos.",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "AjzLbOLZORQ",
  "title": "신입 공무원은 빌런 잡고 퇴근합니다",
  "aliases": [
    "The Newbie Civil Servant Hunts Villains Before Going Home"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=AjzLbOLZORQ. Confirmado pela transcrição nativa do YouTube e por fontes externas da obra. 00:00–01:15: funcionário de cabelo preto preso e cicatrizes cobra folga médica prevista no contrato, lembra morte por excesso de trabalho e mata o chefe com uma caneta. 02:41–03:34: lê recrutamento da Black Eagle e leva uma cabeça decepada ao processo seletivo. 03:42–06:40: entrevista sobre Shin Dae-ho, histórico de empregos de vilões e visitas hospitalares. 08:40–11:52: revela sequelas de experimentos, usa sombras para neutralizar homens com explosivos e é aceito na equipe. Os capítulos 1–3 da tradução do romance correspondem à sequência; nomes na transcrição estão corrompidos e foram normalizados somente a partir das fontes externas (Seo Hyun-yul/Seo Hyeon-yul, Oh Haeryeon, Shin Dae-ho). O capítulo 1 oficial da Naver também confirma visualmente os termos do contrato: saída no horário, férias legais e licença médica remunerada. Título coreano original e créditos confirmados na Naver; título inglês documentado por Novel Updates e DavarScans, sem edição inglesa oficial confirmada. Não foi inferido de comentários nem só do título do recap. Fontes: https://www.youtube.com/watch?v=AjzLbOLZORQ&t=59s https://comic.naver.com/webtoon/detail?titleId=856191&no=1&week=mon https://comic.naver.com/webtoon/list?tab=mon&titleId=856191 https://www.webnovel.com/book/the-newbie-civil-servant-hunts-villains-before-going-home-(novel)_37116784400316605/chapter-1.-do-you-offer-the-four-major-insurances_99652940914024361 https://www.webnovel.com/book/the-newbie-civil-servant-hunts-villains-before-going-home_37114987008159605/chapter-2_99701143466206878 https://www.webnovel.com/book/the-newbie-civil-servant-hunts-villains-before-going-home_37114987008159605/chapter-3_99701148163822792 https://www.novelupdates.com/series/the-newbie-civil-servant-hunts-villains-before-going-home/",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "L9FHatqBu7U",
  "title": "新世纪忧郁战士",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=L9FHatqBu7U. [{\"url\":\"https://www.xs8.cn/bookquery/osqbycnjycsk\",\"accessed_at_utc\":\"2026-10-19T10:17:03Z\",\"method\":\"web search indexed page\",\"title\":\"TheJinFu完结小说_《新世纪忧郁战士》\",\"evidence\":\"Search result reproduced chapter 1 opening with 雷野, 希尔流斯 and 王之威严; exact growth-through-holding-laughter mechanic. This was discovery evidence, subsequently checked through live publisher pages.\"},{\"url\":\"https://www.xs8.cn/bookquery/osqbycnjycnj\",\"accessed_at_utc\":\"2026-10-19T10:17:40Z\",\"method\":\"live cloud-browser page accessibility text\",\"title\":\"TheJinFu最新书_《新世纪忧郁战士》\",\"publisher\":\"言情小说吧 / Yuewen\",\"source_link_observed\":\"https://www.qidian.com/chapter/1050313347/920166554/\",\"facts\":\"Live title and author; light-novel/original-fantasy category; synopsis gives no-laugh power, demon woman killing protagonist, goddess, and freely returning ten years to rescue girls from traumatic childhoods. Chapter 1 text gives dwarf 高山, mithril shield, Guardian unable to learn magic, and her trust because 雷野 alone does not laugh at dwarves. Live page listed 75 chapters and 360k Chinese characters; updated 2026-10-18 18:52 (site timezone unspecified).\",\"access_result\":\"read succeeded without CAPTCHA\"},{\"url\":\"https://www.qidian.com/chapter/1050313347/920178626/\",\"accessed_at_utc\":\"2026-10-19T10:18:04Z\",\"method\":\"normal cloud-browser free-chapter accessibility read\",\"title\":\"第3章 .负责引路的女神在第三章才出场是不是太晚了点？\",\"publisher\":\"起点中文网 / Qidian\",\"chapter\":3,\"site_publication_display\":\"2026年08月08日 08:00; site timezone not asserted\",\"facts\":\"Title/author linkage, hero 雷野, Hezi 禾紫, goddess 哈蒂丝. Goddess asks him to rescue Hezi, whose power is tied to childhood pain. Ability sends him exactly ten years backward; first sleep returns to altered present; later death can rewind again. Black AW hoodie and lightning affinity also align with video clues.\",\"access_result\":\"Full chapter text was already returned by initial normal accessibility read, alongside a security-verification CAPTCHA iframe. No CAPTCHA interaction, completion, dismissal, retry, or alternate-route bypass occurred. Stopped further Qidian interaction.\"}] [{\"video_anchor\":\"00:00–00:21\",\"video_url\":\"https://www.youtube.com/watch?v=L9FHatqBu7U&t=0s\",\"direct_evidence\":\"Hero cannot laugh without impairing growth.\",\"external_source\":\"XS8 live chapter 1\",\"match\":\"王之威严 grants increasing strength while 雷野 keeps a straight face.\"},{\"video_anchor\":\"01:17–02:27\",\"video_url\":\"https://www.youtube.com/watch?v=L9FHatqBu7U&t=77s\",\"direct_evidence\":\"Summit is a dwarf Guardian with a mithril tower shield and no spellcasting.\",\"external_source\":\"XS8 live chapter 1\",\"match\":\"高山 is a dwarf, 守护者 (Guardian), has a fully mithril shield, and the class cannot learn magic.\"},{\"video_anchor\":\"03:42–04:14\",\"video_url\":\"https://www.youtube.com/watch?v=L9FHatqBu7U&t=222s\",\"direct_evidence\":\"Summit trusts him because he never laughs at dwarves.\",\"external_source\":\"XS8 live chapter 1\",\"match\":\"高山 explicitly says she watched 雷野 and chose him because he alone does not join the mockery of dwarves.\"},{\"video_anchor\":\"20:35–22:56\",\"video_url\":\"https://www.youtube.com/watch?v=L9FHatqBu7U&t=1235s\",\"direct_evidence\":\"Goddess Hades asks protagonist to save her follower Violet.\",\"external_source\":\"Qidian chapter 3 rendered text\",\"match\":\"哈蒂丝 asks 雷野 to rescue 禾紫, her faithful follower, whose childhood suffering feeds her power.\"},{\"video_anchor\":\"23:30–23:54\",\"video_url\":\"https://www.youtube.com/watch?v=L9FHatqBu7U&t=1410s\",\"direct_evidence\":\"Exactly ten years backward; sleeping returns to altered present.\",\"external_source\":\"Qidian chapter 3 rendered text\",\"match\":\"Explicit fixed ten-year rewind plus first-sleep return to present and death-to-rewind again.\"},{\"video_anchor\":\"20:13 comment and later black hoodie/lightning clues\",\"video_url\":\"https://www.youtube.com/watch?v=L9FHatqBu7U&t=1213s\",\"direct_evidence\":\"Alan Walker shirt observed by viewer; black hoodie/lightning discussed in retained ending.\",\"external_source\":\"Qidian chapter 3 rendered text\",\"match\":\"Opening specifically describes black hoodie bearing AW. Ending grants lightning affinity. This is corroboration, not independent frame evidence.\"}]",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "miZ0y8bI1JI",
  "title": "我有无限金色词条",
  "aliases": [
    "I Have Infinite Golden Traits",
    "My Golden Traits Can Evolve Infinitely"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=miZ0y8bI1JI. [{\"source_type\":\"official_original_publisher\",\"publisher\":\"Tencent Animation and Comics\",\"url\":\"https://ac.qq.com/Comic/comicInfo/id/657667\",\"title\":\"我有无限金色词条\",\"access_method\":\"Public web page, successfully opened via reference; original link also discovered on catalog.\",\"supports\":\"Official title and creator. Synopsis names 陈夕 (Chen Xi), exceptional mental power, 阴影法师 (Shadow Mage), golden-trait talent, zero cooldown and limitless undead summoning.\",\"source_locator\":\"Title/creator and synopsis, extracted lines 41–54; confirmed again at 13:23 UTC.\"},{\"source_type\":\"English_title_and_synopsis\",\"publisher\":\"Dragon Tea\",\"url\":\"https://dragontea.ink/novel/i-have-infinite-golden-traits/\",\"title\":\"I Have Infinite Golden Traits\",\"access_method\":\"Public web search and opened page.\",\"supports\":\"English title; same named Chen Xi, Shadow Mage, golden trait, no-cooldown skills and undead legions.\"},{\"source_type\":\"catalog_alias\",\"publisher\":\"MangaBaka\",\"url\":\"https://mangabaka.org/manhua/588991/My-Golden-Traits-Can-Evolve-Infinitely\",\"title\":\"My Golden Traits Can Evolve Infinitely\",\"access_method\":\"Public web search and opened page.\",\"supports\":\"Exact Chinese title, creator, matching synopsis and original Tencent link.\"}] [{\"timestamp\":\"0:54\",\"seconds\":54,\"observation\":\"Protagonist awakens the unpopular Shadow Mage class.\"},{\"timestamp\":\"1:37\",\"seconds\":97,\"observation\":\"Mental-strength test was 150, so he expected a special class.\"},{\"timestamp\":\"1:46\",\"seconds\":106,\"observation\":\"Status identifies protagonist as Chen Xi.\"},{\"timestamp\":\"5:56\",\"seconds\":356,\"observation\":\"Summon Undead costs ten mana and creates two zombies or fighter skeletons.\"},{\"timestamp\":\"6:06–6:27\",\"seconds\":366,\"observation\":\"Golden affix Arcane Grace appears; one golden affix every five levels; effect removes all skill cooldowns.\"},{\"timestamp\":\"7:01–7:31\",\"seconds\":421,\"observation\":\"Repeated casts produce twenty undead and fill his room, demonstrating a growing undead army.\"}] Named protagonist plus his specific class, exceptional mental stat, golden-affix zero-cooldown mechanic and undead army independently agree with the official Tencent synopsis. This is not inferred from the promotional YouTube headline alone.",
  "reviewed_at": "2026-10-21",
  "confirmado": True
},
{
  "video_id": "LEftxAxgbmU",
  "title": "我每周获得一个新人设",
  "aliases": [
    "I Get a New Persona Every Week"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=LEftxAxgbmU. [{\"source_type\":\"official_original_chapter\",\"publisher\":\"Qidian\",\"url\":\"https://www.qidian.com/chapter/1049395605/907173638/\",\"title\":\"第1章 废柴的我和邻家的文学少女 — 我每周获得一个新人设\",\"access_method\":\"Directly opened and read native cloud-browser accessibility UI; exact URL verified via tab.url().\",\"supports\":\"Chapter names Zhang Chaomu/张朝暮 and Duan Chaner/段婵儿. It matches 6:30 wake and 9:00 school, polished persona, dirty room, instinctive haircut, saving AC money for internet, brand-new optional uniform, literary neighbor, her toast/fried egg and his beef noodles plus two eggs. Chen Zhenzhen/陈真真 is met at the noodle shop.\"},{\"source_type\":\"publisher_network_title_and_synopsis\",\"publisher\":\"言情小说吧\",\"url\":\"https://www.xs8.cn/kolquery/ycnjhvbp\",\"title\":\"我每周获得一个新人设(张朝暮、段婵儿)\",\"access_method\":\"Public search succeeded; direct browser page read and URL verified.\",\"supports\":\"Exact Chinese title and author. Synopsis mirrors opening role sequence: polished/refined, scholar, fitness enthusiast, chuunibyou, cat. Links directly to the Qidian first chapter.\"},{\"source_type\":\"English_title_catalog\",\"publisher\":\"DaoSearch\",\"url\":\"https://daosearch.io/qidian/book/1049395605/i-get-a-new-persona-every-week\",\"title\":\"I Get a New Persona Every Week\",\"access_method\":\"Public search and opened page.\",\"supports\":\"English title, exact Chinese original, Qidian ID and author. Its translated synopsis matches the same unusual persona sequence.\"}] [{\"timestamp\":\"0:00–0:30\",\"seconds\":0,\"observation\":\"Second-year high-school boy Morgan Hail/Hale acquires a polished persona; later weekly roles include top student, fitness buff, chuunibyou and cat.\"},{\"timestamp\":\"0:38\",\"seconds\":38,\"observation\":\"Wakes at 6:30 on the first school day; class starts at nine.\"},{\"timestamp\":\"1:09–1:39\",\"seconds\":69,\"observation\":\"Dirty clothes, instant-noodle leftovers and bedding prompt cleaning; acquires hair-cutting skill without learning it.\"},{\"timestamp\":\"2:25\",\"seconds\":145,\"observation\":\"Avoids air conditioning to save electricity money for internet access.\"},{\"timestamp\":\"3:19\",\"seconds\":199,\"observation\":\"Newbrook Number One High requires uniform only for major events; his uniform is unused.\"},{\"timestamp\":\"4:56–6:42\",\"seconds\":296,\"observation\":\"Literary-gifted neighbor Camellia Dayne compliments haircut and uniform; she ate toast and a fried egg.\"},{\"timestamp\":\"8:31–8:46\",\"seconds\":511,\"observation\":\"Orders beef rice noodles with two eggs, then greets childhood friend Vera.\"}] The native video translates/localizes the original novel’s opening scene with numerous distinctive details in the same order. Exact first-chapter correspondence resolves the Westernized video names; this is stronger than headline similarity.",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "U6PnVpjIrjY",
  "title": "좀비가 날 물지 않아",
  "aliases": [
    "The Zombie Won’t Bite Me",
    "Zombies Don’t Bite Me",
    "Immune to Zombies"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=U6PnVpjIrjY. [{\"source_type\":\"official_original_webtoon\",\"publisher\":\"KakaoPage\",\"url\":\"https://page.kakao.com/content/65994315\",\"title\":\"좀비가 날 물지 않아\",\"access_method\":\"Public web search and opened page.\",\"supports\":\"Canonical Korean webtoon title and credits Jeff, 백지운, The eun. Official Kakao Webtoon also lists the same title and credits.\",\"additional_official_url\":\"https://webtoon.kakao.com/content/%EC%A2%80%EB%B9%84%EA%B0%80-%EB%82%A0-%EB%AC%BC%EC%A7%80-%EC%95%8A%EC%95%84/4434\"},{\"source_type\":\"official_original_novel_synopsis\",\"publisher\":\"KakaoPage\",\"url\":\"https://page.kakao.com/content/51509604?tab_type=about\",\"title\":\"좀비가 날 물지 않아\",\"access_method\":\"Public indexed page.\",\"supports\":\"The eun’s original novel names Yi-hwan, ignored by zombies, unusual strength, one red eye and hunger at blood.\"},{\"source_type\":\"independent_review_with_specific_opening_scene\",\"publisher\":\"Tistory reviewer 잔망탱이\",\"url\":\"https://feel0622.tistory.com/43\",\"title\":\"[리뷰] 좀비가 날 물지않아[The eun_현대판타지_1부 완결]\",\"published_date\":\"2019-05-11\",\"access_method\":\"Public search and opened full page.\",\"supports\":\"Names funeral-company worker 강이환 (Kang Yi-hwan). Describes collecting adult-and-child bodies supposedly from a road accident, oddly uninjured child, mouth/tooth injury, fever and collapse, then waking with a red eye and zombies ignoring him. Later searches for older sister.\"},{\"source_type\":\"independent_reader_identification\",\"publisher\":\"Reddit r/ManhwaRealm\",\"url\":\"https://www.reddit.com/r/ManhwaRealm/comments/1o32jmf/cant_find_this_manhwawebtoon/\",\"title\":\"Can’t find this manhwa/webtoon\",\"access_method\":\"Public search page.\",\"supports\":\"Reader describes the hospital-morgue girl’s tooth scratch/collapse, zombie immunity, convenience-store rescue and search for sister; answer identifies The Zombie Won’t Bite Me. Used as corroboration, not sole proof.\"},{\"source_type\":\"English_alias_synopsis\",\"publisher\":\"Raven Scans / Yomiru\",\"url\":\"https://ravenscans.org/manga/the-zombie-wont-bite-me/\",\"title\":\"The Zombie Won’t Bite Me\",\"access_method\":\"Successful public search extraction; a later direct open timed out.\",\"supports\":\"Lists The Zombie Won’t Bite Me, Zombies Don’t Bite Me, Immune to Zombies and exact Korean title; synopsis matches one red eye, strength and blood hunger. Yomiru names Kang I-hwan.\",\"additional_url\":\"https://www.yomiru.live/series/immune-to-zombies\"}] [{\"timestamp\":\"0:00–1:26\",\"seconds\":0,\"observation\":\"Scientists test injected substance on an adult and child; experiment apparently fails.\"},{\"timestamp\":\"4:24–6:07\",\"seconds\":264,\"observation\":\"Funeral worker Kang visits hospital for adult-and-child bodies supposedly killed in a car accident; girl appears unexpectedly uninjured.\"},{\"timestamp\":\"6:22–8:19\",\"seconds\":382,\"observation\":\"While cleaning girl’s mouth, her tooth scratches his finger; he collapses as virus enters his bloodstream.\"},{\"timestamp\":\"11:14–11:23\",\"seconds\":674,\"observation\":\"Girl ignores him after waking; five days have elapsed.\"},{\"timestamp\":\"14:29\",\"seconds\":869,\"observation\":\"He experiences extreme unexplained hunger.\"},{\"timestamp\":\"17:15–17:59\",\"seconds\":1035,\"observation\":\"Zombified coworker passes him; zombies do not pay attention to him.\"},{\"timestamp\":\"19:00–19:16\",\"seconds\":1140,\"observation\":\"Missed calls and message from sister reveal she and her daughter are safe.\"},{\"timestamp\":\"27:57\",\"seconds\":1677,\"observation\":\"Narration explicitly describes his eye glowing red without him noticing.\"}] Highly specific mortuary-workplace opening, adult/child accident story, tooth scratch and collapse match an independent Korean review of the exact title; red eye, blood hunger and zombie nonaggression match official original-novel synopsis. Official webtoon title/creators and English alias catalog establish title linkage.",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "v455srQ6mqY",
  "title": "The Dragon Slayer's Regression on Another Level",
  "aliases": [
    "A Dragonslayer's Peerless Regression",
    "Dragonslayer's Class Regression"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=v455srQ6mqY. [{\"url\":\"https://tapas.io/series/the-dragon-slayers-regression-on-another-level/info\",\"source_type\":\"official English publisher\",\"access_method\":\"web search and direct open\",\"observed_at_bounds\":[\"2026-10-19T16:16:39Z\",\"2026-10-19T16:17:24Z\"],\"finding\":\"Tapas explicitly gives the English title and the Korean original title, with copyright EXTEN STUDIO, Hecto / Dreamtoon and publication by TAPAS ENTERTAINMENT. Its synopsis matches Zeke Draker, the family's first failed Awakening, his expulsion, the Phantom of the North identity, an emperor's ancient relic, death by imperial forces, and awakening at age twelve in the Cradle.\",\"supports\":[\"official_english_title\",\"official_original_title\",\"specific_story_identity\"]},{\"url\":\"https://www.novelupdates.com/series/dragonslayers-class-regression/?grr=1\",\"source_type\":\"secondary bibliographic source for original web novel\",\"access_method\":\"web search and direct open\",\"observed_at_bounds\":[\"2026-10-19T16:16:43Z\",\"2026-10-19T16:17:24Z\"],\"finding\":\"Entry headed Dragonslayer’s Class Regression lists A Dragonslayer's Peerless Regression and 용살자의 클래스가 다른 회귀 as associated names. Its description matches Zeke Draker, healer talent, failed awakening, elder-dragon power, and regression twenty years earlier.\",\"supports\":[\"documented_aliases\",\"original_story_continuity\"],\"limitation\":\"This is the original novel's entry, not proof of an official English manhwa title.\"},{\"url\":\"https://comick.dev/comic/a-dragonslayers-peerless-regression\",\"source_type\":\"secondary manhwa catalogue search result\",\"access_method\":\"web search\",\"observed_at_bounds\":[\"2026-10-19T16:16:43Z\",\"2026-10-19T16:16:51Z\"],\"finding\":\"Manhwa entry places The Dragon Slayer's Regression on Another Level and A Dragonslayer's Peerless Regression together, and lists Dragonslayer's Class Regression and the matching Korean title among alternatives.\",\"supports\":[\"alias_mapping_to_manhwa\"],\"limitation\":\"Search-index evidence; secondary source, not a publisher.\"}] [{\"time\":\"00:08\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=8s\",\"kind\":\"native YouTube transcript\",\"paraphrase\":\"Protagonist named Zeke Draker; unable to wield aura.\"},{\"time\":\"00:52–01:17\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=52s\",\"kind\":\"native YouTube transcript\",\"paraphrase\":\"Northern Phantom pursued in the mountains over an ancient relic sought by the emperor.\"},{\"time\":\"01:30–01:47\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=90s\",\"kind\":\"native YouTube transcript and visibly selected timestamp\",\"paraphrase\":\"Zeke is the dragon-slayer Draker household's first failed awakener.\"},{\"time\":\"02:38–03:11\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=158s\",\"kind\":\"native YouTube transcript\",\"paraphrase\":\"After stealing the emperor's relic and facing death, elder-dragon power activates.\"},{\"time\":\"03:27–03:34\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=207s\",\"kind\":\"native YouTube transcript\",\"paraphrase\":\"He awakens as a child in the Cradle, the Draker training institution.\"},{\"time\":\"04:28–04:36\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=268s\",\"kind\":\"native YouTube transcript\",\"paraphrase\":\"Status window lists rare healer class and a draconian ability requiring ten points.\"},{\"time\":\"05:46–06:21\",\"url\":\"https://www.youtube.com/watch?v=v455srQ6mqY&t=346s\",\"kind\":\"native YouTube transcript\",\"paraphrase\":\"Servant Decker arrives; Composed Mind calms Zeke before the evaluation.\"}] An exact protagonist and family name plus the failed awakening, Northern Phantom identity, emperor/relic pursuit, elder-dragon activation, and return to the named Cradle form a distinctive multi-point match. Tapas supplies the authoritative title pair. Identification does not rely on the YouTube thumbnail, recap title, generic tags, comments, or unsupported translated titles.",
  "reviewed_at": "2026-10-19",
  "confirmado": True
},
{
  "video_id": "SKiK2hI1NiA",
  "title": "World-Saving is a Skill",
  "aliases": [
    "A Hero Who Knows His Stuff",
    "세상도 구해본 놈이 잘 구한다"
  ],
  "evidence": "Direct native YouTube transcript 06:00: Yu Chan-seok, civilian hunter applicant. 12:36–13:39: Paradox Flame consumes fatigue; duel with Lee Se-eun lasts exactly 4h17min, then lollipop and team-3 partner hunter card. Novel chapter 4 independently matches characters, ability and this exact sequence. Source: https://www.webnovel.com/book/34697984800932305/93162400160735831 . Title/aliases: https://asurascans.com/comics/world-saving-is-a-skill-11fe7da3 https://www.mangaread.org/manga/world-saving-is-a-skill/ . Video: https://www.youtube.com/watch?v=SKiK2hI1NiA&t=756s . No complete chapter-range or visual-panel-match claim.",
  "reviewed_at": "2026-10-21",
  "confirmado": True
},
{
  "video_id": "YI7WMvmw_Rg",
  "title": "Dungeon Porter",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=YI7WMvmw_Rg. Direct native transcript identifies Nagi, the lowest white-rank porter with a magic storage bag, ambition to fight, ingenious item/trap combinations, unfair 50 versus 10 gold pay and party equipment packed in the bag. Official WEBTOON synopsis corroborates protagonist, mistreatment, magic bag, ingenuity and hierarchy. Confirmation is not based on pinned comment alone. [[\"0:00\",\"Naggi\"],[\"0:07\",\"Magic storage bag\"],[\"0:13–0:30\",\"Nagi, lowest white-rank porter wants to be a fighting adventurer\"],[\"0:33\",\"Items, traps and combinations\"],[\"0:41\",\"Agnesa\"],[\"2:07\",\"White porcelain rank\"],[\"2:32–3:06\",\"Paid 50 gold versus ordinary 10\"],[\"3:13–3:29\",\"Packs party backpacks into magic bag\"],[\"4:53–5:24\",\"Produces meals and bathtub\"]] [\"https://www.webtoons.com/en/fantasy/dungeon-porter/list?title_no=7914\"] Playback stalled on a 15-second advertisement, but native transcript was independently accessible. Official chapter 1 showed only introductory panels, with remaining panels blank; no full panel match or part endpoint coverage is claimed.",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "MMxvbHNYKVE",
  "title": "凡人老祖：圣女千里寻夫",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=MMxvbHNYKVE. [{\"url\":\"https://www.douyin.com/video/7678215514249841930\",\"role\":\"Main external title-and-plot correspondence\",\"retrieval\":\"Search-indexed text only; direct web opening returned an internal error and cloud browser a generic server error.\",\"uploader\":\"漫界暴走团\",\"publication_display\":\"2026-08-26 13:57\",\"publication_timezone\":\"Not established\",\"authorship_and_rights_verified\":false},{\"url\":\"https://kuaikaw.cn/browse/1648-1652/110\",\"role\":\"Corroboration only\",\"retrieval\":\"Indexed synopsis includes 万剑仙宗 and 太初圣女. Current paginated page changed and no longer contains the entry.\",\"current_page_contains_entry\":false},{\"url\":\"https://www.bilibili.com/video/BV1RYh36METG/\",\"role\":\"Chinese title corroboration only; does not establish aliases or official provenance.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "H9t_zVATGvA",
  "title": "O Retorno do Primeiro Patriarca: Renasci Mil Anos Depois Como Meu Próprio Descendente",
  "aliases": [
    "Return of the First Patriarch: The Strongest Reincarnates into His Descendant 1000 Years Later"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=H9t_zVATGvA. [{\"url\":\"https://br.comikey.com/comics/o-retorno-do-primeiro-patriarca-renasci-mil-anos-d-webtoon/979/\",\"role\":\"Licensed Portuguese edition\",\"specifics\":\"Gilfas Eldragon reincarnates as Zeke Eldragon in his own lineage after a thousand years, under a law of the strongest.\"},{\"url\":\"https://sorajimatoon.com/comics/01K583PA0B17KNAW8XP5CEHZ2J\",\"role\":\"Official Japanese source\"},{\"url\":\"https://qimanga.com/series/return-of-the-first-generation%3A-the-strongest-in-history-reincarnates-as-his-descendant-1000-years-later\",\"role\":\"Secondary English alias source\"}] Video evidence: [{\"timestamp\":\"00:07–00:31\",\"details\":\"Defeats a dragon and eats a golden fruit.\"},{\"timestamp\":\"00:47–01:26\",\"details\":\"Dies old with his son present.\"},{\"timestamp\":\"01:26–02:13\",\"details\":\"Reborn as a baby.\"},{\"timestamp\":\"02:35–04:28\",\"details\":\"Servants test dragon blood on a goblin and then babies.\"},{\"timestamp\":\"05:02\",\"details\":\"Zeke, formerly Gilfus.\"},{\"timestamp\":\"05:59–06:24\",\"details\":\"Bastard son in his own patriarchal family a thousand years later; strongest-survival rule.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "_IT7iUHwK8w",
  "title": "都觉醒恶魔法则了，你契约蚂蚁？",
  "aliases": [],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=_IT7iUHwK8w. [{\"url\":\"https://fanqienovel.com/page/7517195003517488190\",\"role\":\"Official title and author\"},{\"url\":\"https://fanqienovel.com/reader/7517940027930709054\",\"role\":\"Chapter 55 public preview read in browser\",\"specifics\":\"Poison destroys the body through pores; infernal spear and 雷狮 flee; 蝠翼飞虫 bombs with precise tracking, in the same sequence as video 00:45–01:05.\"},{\"url\":\"https://fanqienovel.com/reader/7517940024583654462\",\"role\":\"Chapter 54 public preview also read\"},{\"url\":\"https://www.youtube.com/watch?v=_IT7iUHwK8w&lc=UgwUsbkmGMgFe2qQjJR4AaABAg\",\"role\":\"Uploader link to previously applied Part 1 xP18d9gnXR0; supporting, not sole basis\"}] Video evidence: [{\"timestamp\":\"00:07–00:34\",\"details\":\"Lake Isle, legendary core, Bureau 11, Shadow Sovereign, Batwing Bomber and Capital Third High recap, consistent with official chapter index 21, 35, 41, 44, 45 and 53–55.\"},{\"timestamp\":\"00:45–01:05\",\"details\":\"Distinctive poison, spear, thunder lion and bomber sequence matches chapter 55 preview.\"},{\"timestamp\":\"01:05\",\"details\":\"Ten elite cores feed the bomber.\"},{\"timestamp\":\"01:18–02:12\",\"details\":\"Dean Price, director Merrick and Capital Third High dean speaking of Lucas; translated names not used as sole identity proof.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "A_bQG3SfH-8",
  "title": "Climbing the Tower that Even the Regressor Couldn't",
  "aliases": [
    "Conquering the Tower Even Regressors Couldn't",
    "I Will Climb the Tower That Even Regressors Couldn't Conquer"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=A_bQG3SfH-8. [{\"url\":\"https://www.wuxiaworld.com/novel/conquering-the-tower-even-regressors-couldnt/cterc-chapter-2\",\"role\":\"Primary chapter 2\",\"details\":\"Kwon Su-Hyeok and Ha Hee-Jeong; exact three instructions and silenced regressor holding up three fingers.\"},{\"url\":\"https://spa-prod.wuxiaworld.com/novel/conquering-the-tower-even-regressors-couldnt/cterc-chapter-1\",\"role\":\"Primary prologue\",\"details\":\"Breakup and bar setting.\"},{\"url\":\"https://manhuatop.org/manhua/climbing-the-tower-that-even-the-regressor-couldnt/\",\"role\":\"Secondary alias source\"}] Video evidence: [{\"timestamp\":\"00:34–01:03\",\"details\":\"After a breakup, protagonist listens to his regressor friend.\"},{\"timestamp\":\"01:12–01:48\",\"details\":\"Refuse the status window; avoid gods on tutorial floors 1–5 and accept the most modest one afterward; awaken holding sword, axe or spear, not a staff.\"},{\"timestamp\":\"01:58–02:23\",\"details\":\"One million selected people; silenced friend holds up three fingers.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "xQcqy_EEoDU",
  "title": "Ghost King",
  "aliases": [
    "Phantom Spirit King",
    "Demonic Spirit King",
    "King of Ghosts"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=xQcqy_EEoDU. [{\"url\":\"https://www.webtoons.com/en/action/ghost-king/list?title_no=4005\",\"role\":\"Official title and synopsis\",\"details\":\"Murim police university and search for a missing father.\"},{\"url\":\"https://www.webtoons.com/en/action/ghost-king/episode-1/viewer?episode_no=1&title_no=4005\",\"role\":\"Official episode 1, visually inspected\",\"details\":\"Red-jacketed man interrogated by masked man amid defeated men confesses distribution under the Black Death Sect manager; masked man leaves and police arrive late; second-year Jiho Yu.\"},{\"url\":\"https://asurascans.com/comics/demonic-spirit-king-05c7df14\",\"role\":\"Secondary aliases\"},{\"url\":\"https://1668manga.com/manga/phantom-spirit-king/\",\"role\":\"Secondary aliases\"}] Video evidence: [{\"timestamp\":\"00:00–00:40\",\"details\":\"Exact opening interrogation, Black Death Sect confession and late police arrival sequence matches official episode 1.\"},{\"timestamp\":\"02:12–03:15\",\"details\":\"Top student looks at his father's photograph, matching missing-father premise.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "r5PFNazIdng",
  "title": "World’s Strongest Survivor",
  "aliases": [
    "서바이벌로 세계 최강"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=r5PFNazIdng. [{\"url\":\"https://beastnovels.com/series/worlds-strongest-survivor/1\",\"role\":\"Chapter 1 narrative correspondence\",\"details\":\"Jin Seowoon, Royal Ground, Escrow/Chiron, capital, top-ten rewards, exclusion below top ninety, Argas Eye descent and spaced houses for equipment; also Kaile.\"},{\"url\":\"https://ravenscans.org/manga/worlds-strongest-survivor/\",\"role\":\"Title, Korean title and synopsis\",\"details\":\"Jin Seowoon, Cloyd Survival and top ten.\"}] Video evidence: [{\"timestamp\":\"03:01–03:44\",\"details\":\"Jin Seowoon is ex-military and plays Royal Ground.\"},{\"timestamp\":\"06:17–06:30\",\"details\":\"Escrow/Chiron, transcribed as Eskrow/Khairon.\"},{\"timestamp\":\"06:41–07:14\",\"details\":\"Capital, top-ten rewards, exclusion below top ninety in future games and Argas Eye descent.\"},{\"timestamp\":\"08:07–08:23\",\"details\":\"Spaced houses for equipment.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "LW6D48DgPV4",
  "title": "The Strongest at Level 0: Absolute Domination with the Analysis Skill",
  "aliases": [
    "The Strongest Level 0 Absolute Supremacy Through Analysis Skills",
    "Absolute Domination at Level 0 Using My Analysis Skill"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=LW6D48DgPV4. [{\"url\":\"https://publishing.unext.co.jp/news/2z61QeAp4Ut8N1PVLHwJCL\",\"role\":\"Official publisher\",\"details\":\"Tenma Itsuki orphaned by Disaster Beasts, level zero, analysis and unlimited attributes; authors Rain/Liezao.\"},{\"url\":\"https://manga.line.me/product/periodic?id=S157028\",\"role\":\"Official listing synopsis, with reader comment mentioning 雷鳴波\",\"details\":\"Same premise; Thunderwave comment corroborative only.\"},{\"url\":\"https://arenascan.com/manga/the-strongest-level-0-absolute-supremacy-through-analysis-skills/\",\"role\":\"English circulation title variants, not verified licensed English edition\"}] Video evidence: [{\"timestamp\":\"00:00–00:25\",\"details\":\"Disaster Beasts and Itsuki.\"},{\"timestamp\":\"02:09–02:33\",\"details\":\"Rare class, zero attributes and skill learning.\"},{\"timestamp\":\"02:57–03:32\",\"details\":\"Analyzes electric attack, learns Thunderwave and increases attributes.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "AE1bhcRRPgU",
  "title": "The Rebel of the Tyrant Noble House — Aster",
  "aliases": [
    "The Rebel of the Tyrant Noble Family",
    "Boukun Meika no Hangyakusha -Aster-",
    "暴君名家の反逆者-Aster-",
    "Aster: Um Rebelde Entre os Tiranos"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=AE1bhcRRPgU. [{\"url\":\"https://sorajimatoon.com/comics/01KG1PW0PMBM162DB8SMXGBQES\",\"role\":\"Official publisher\",\"details\":\"Orphan Ash, adoptive father, betrayal and stolen 七翼 power.\"},{\"url\":\"https://qimanga.com/series/the-rebel-of-the-tyrant-noble-house-aster\",\"role\":\"English title/aliases and synopsis\"},{\"url\":\"https://kaynscans.com/series/comic/the-rebel-of-the-tyrant-s-noble-house-aster\",\"role\":\"Portuguese circulation title and aliases\"}] Video evidence: [{\"timestamp\":\"01:03–01:20\",\"details\":\"Aster, Elmheim house and adoptive father Duke Rodrik.\"},{\"timestamp\":\"01:36–01:44\",\"details\":\"Wingless with no mana.\"},{\"timestamp\":\"03:34–03:46\",\"details\":\"Rodrik wanted to steal seven wings.\"},{\"timestamp\":\"04:26–05:32\",\"details\":\"Returns as a baby beside his dead mother in snow while Rodrik's soldiers search.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "DrfS47iG-14",
  "title": "Job Change: Master – Starting by Controlling the School Beauty to Give Me a Massage While Wearing Black Stockings",
  "aliases": [
    "转职主人，开局控制校花黑丝按摩",
    "最废双E？抱歉SSS全是我女仆",
    "Job Change to Master, Start by Controlling the School Beauty in Black Stockings and Giving Her a Massage"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=DrfS47iG-14. [{\"url\":\"https://shanghaifantasy.com/job-change-master-starting-by-controlling-the-school-beauty-to-give-me-a-massage-while-wearing-black-stockings-chapter-1/\",\"role\":\"Indexed chapter 1 narrative\",\"details\":\"Lanjiang No. 3 school, breakup, classes and characters match. Full indexed excerpts obtained; opening returned Cache miss.\"},{\"url\":\"https://shanghaifantasy.com/job-change-master-starting-by-controlling-the-school-beauty-to-give-me-a-massage-while-wearing-black-stockings-chapter-3/\",\"role\":\"Indexed chapter 3 narrative\",\"details\":\"Data God SS, Master E and distinctive skills match; direct opening Cache miss.\"},{\"url\":\"https://www.biquge.tw/book/7898978.html\",\"role\":\"Opened catalog confirming title, author and alias\"},{\"url\":\"https://www.biquge.tw/book/6170099/\",\"role\":\"Index corroborating He Wanying and Chu Jianghe\"},{\"url\":\"https://wtr-lab.com/en/novel/32670/job-change-to-master-start-by-controlling-the-school-beauty-in-black-stockings-and-giving-her-a-massage\",\"role\":\"Title and author\"}] Video evidence: [{\"timestamp\":\"00:24–02:12\",\"details\":\"Lu Sheng dumped by Qin Yanran, Holy Light Priest A; he is Scout E, with Basic Appraisal of name/age once daily.\"},{\"timestamp\":\"05:09–05:17\",\"details\":\"He Wanying, Massage Therapist E.\"},{\"timestamp\":\"12:06–12:49\",\"details\":\"Master, Be My Son, Talent and Sweat, and Scout changing to Data God SS.\"}]",
  "reviewed_at": "2026-10-20",
  "confirmado": True
},
{
  "video_id": "Hlr_D8_La5g",
  "title": "人气至上，我扮演超级天才",
  "aliases": [
    "Popularity Above All: I Play the Role of a Super Genius"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=Hlr_D8_La5g. [{\"url\":\"https://www.readnovel.com/bookquery/zfiqycbpendy?source=m_jump\",\"chapter\":1,\"details\":\"崎寂 chooses 千面, divided into 27 parts, with a 5 million popularity mortgage/debt; matches video 00:14–00:26.\"},{\"url\":\"https://www.qidian.com/chapter/1049020186/901791399/\",\"chapter\":1,\"details\":\"Primary chapter link exposed by the readnovel text.\"},{\"url\":\"https://www.qidian.com/chapter/1049020186/908709969/\",\"chapter\":71,\"details\":\"Matches video 01:48–06:05: Blank's mask breaks; Miracle raises a fire wall to hide the crying feminine face, gathers two halves of a fox mask, repairs it with ice and replaces it. Characters 崎寂 and 诉世.\"},{\"url\":\"https://www.qidian.com/chapter/1049020186/909548594/\",\"chapter\":79,\"details\":\"Matches video 47:43–49:47: falls asleep on Iris's shoulder with white butterfly blossom scent; she moves his head onto Lily's shoulder. Lily recalls her engagement to Blank; Iris uses the bell and substitute teacher's lesson to pull her away. Original names include 崎寂, 琉璃, 白蝶花, 白理理, 诉世 and 静老师.\"},{\"url\":\"https://completenovel.com/popularity-above-all-i-play-the-role-of-a-super-genius/\",\"details\":\"English alias, Chinese title and author.\"}]",
  "reviewed_at": "2026-10-21",
  "confirmado": True
},
{
  "video_id": "I9_Ysze26Rc",
  "title": "It All Starts With A Group Of Primitive People",
  "aliases": [
    "Starting With a Group of Primitive Men",
    "Kaiju Yiqun Yuanshi Ren",
    "Kāijú Yīqún Yuánshǐ Rén",
    "开局一群原始人"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=I9_Ysze26Rc. [{\"url\":\"https://www.mangaread.org/manga/it-all-starts-with-a-group-of-primitive-people/\",\"details\":\"Title and aliases.\"},{\"url\":\"https://www.mangaread.org/manga/it-all-starts-with-a-group-of-primitive-people/chapter-1/\",\"details\":\"Chapter 1 panels 5/6 match video 00:58–01:14: tied red-haired protagonist, bald and long-haired captors, red mission window; video 03:54–04:11 matches survive 12 hours, one attribute point and survival package. Video 01:29–01:36 remembers capture. Panel dialogue includes Hello! Where are we? and I remembered.\"},{\"url\":\"https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_6353bab0c2885/6060e08cf143a6d53b1e6496c97b9ffd/5.jpeg\",\"details\":\"Specific chapter 1 visual match.\"},{\"url\":\"https://www.mangaread.org/wp-content/uploads/WP-manga/data/manga_6353bab0c2885/6060e08cf143a6d53b1e6496c97b9ffd/6.jpeg\",\"details\":\"Specific chapter 1 visual match.\"}]",
  "reviewed_at": "2026-10-21",
  "confirmado": True
},
{
  "video_id": "_yJPC7epHwk",
  "title": "Monster’s Streamer Star",
  "aliases": [
    "Monster Streaming Star",
    "몬스터의 인방스타",
    "Monster-ui Inbang Star"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=_yJPC7epHwk. [{\"url\":\"https://toonz.to/manhwa/monsters-streamer-star\",\"details\":\"Title and aliases.\"},{\"url\":\"https://asurascans.com/novels/monster-s-streamer-star\",\"details\":\"Title and novel.\"},{\"url\":\"https://asurascans.com/novels/monster-s-streamer-star/chapter/1\",\"details\":\"Chapter 1 matches video 00:30–00:46 bored 600-year dragon finds I want to see livestream; 01:32–02:06 newborn blind slime receives knowledge and starts streaming; 02:14–03:14 Noblesse Fire and Gothic Luxury Bone enter and interact; 04:10–04:18 decide to consult Slime Queen.\"}]",
  "reviewed_at": "2026-10-21",
  "confirmado": True
},
{
  "video_id": "dSMML8WWdFM",
  "title": "Ode of the Brave",
  "aliases": [
    "The Warrior's Ballad"
  ],
  "evidence": "Vídeo: https://www.youtube.com/watch?v=dSMML8WWdFM. [{\"url\":\"https://asurascans.com/novels/ode-of-the-brave/chapter/2\",\"details\":\"Video 00:51–01:24: Ricky/Ricard visits mother's memorial on death anniversary, brother fetches him for a hunt; question about his future and mother's arms giving everything. Video 02:48–03:51: hunter freezes before boar, Ricky takes spear and kills it, father runs over. Chapter has Ricard/Riki, Graut/Bilter, Stormhertz and Butch's spear, matching the sequence.\"},{\"url\":\"https://asurascans.com/novels/ode-of-the-brave/chapter/3\",\"details\":\"Video 04:48–07:00 matches family conversation, father proposing sword practice, Grout attacking/training, protagonist refusing to fight and falling.\"},{\"url\":\"https://www.webtoons.com/en/action/the-warriors-ballad/list?title_no=11210\",\"details\":\"Official alias and authors Street Bard, namwoong and Dodongpa; Ricardt reborn after 100 years.\"},{\"url\":\"https://genztoons.org/series/ode-of-the-brave-2/\",\"details\":\"Ode of the Brave title and Ricky/Steel Reaper.\"}]",
  "reviewed_at": "2026-10-21",
  "confirmado": True
},
{
  "video_id": "94cAXKeg4gI",
  "title": "Killer Peter",
  "aliases": [
    "Killer Pietro"
  ],
  "evidence": "YouTube transcript read in cloud browser: 00:30 aging assassin abandoned by new boss after cancer; 00:40 Pietro opens bookstore; 00:59 schoolgirl ambush; 02:51 collapses in rainy park; 03:04 wakes with youthful vitality. Official WEBTOON synopsis independently matches retired Glory Club killer Peter, used bookstore, ambush by former organization and teenage rejuvenation. Uploader description playlist explicitly names killer pietro; viewer name comment only secondary corroboration. No claim to have watched frames or reviewed every chapter. Sources: https://www.youtube.com/watch?v=94cAXKeg4gI&t=40s https://www.youtube.com/watch?v=94cAXKeg4gI&t=184s https://www.webtoons.com/en/action/killer-peter/list?title_no=5816 https://www.youtube.com/playlist?list=PLu5dX6gmxYJ53NjJrKhsZz8BnZ2a3v5y8",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
{
  "video_id": "sblNZi8oHBs",
  "title": "A Cadet Becomes a Prophet?!",
  "aliases": [],
  "evidence": "YouTube transcript read in cloud browser: 00:16–00:29 Fernan Pelenberg heir values money and reads earnings with Hyde; 00:38–00:54 lightning and intruder tries to seize consciousness but Fernan repels it, receiving future visions; 02:04 Ain Armian entering academy; 02:31 return of 72 demons and future hero; 03:35–03:52 gives injured hero high-grade potion as investment. Official WEBTOON8950 synopsis independently identifies Fernan Fallenberg, wealthy Imperial Academy prodigy obsessed with money, lightning, rejected mind invader and Book of Prophecies predicting world end. Pelenberg/Pellenberg/Fallenberg are translation variants. Description claims chapters1–30 but endpoint not independently verified. Sources: https://www.youtube.com/watch?v=sblNZi8oHBs&t=16s https://www.youtube.com/watch?v=sblNZi8oHBs&t=38s https://www.webtoons.com/en/fantasy/a-cadet-becomes-a-prophet/list?title_no=8950",
  "reviewed_at": "2026-10-17",
  "confirmado": True
},
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
