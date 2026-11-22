# Irreducibly Human Work Lexicon pilot, grounded run: message 3 of 13 (chunk 02, 2 concepts)

Everything you need is in this message. Don't fetch, search or look anything up. Draft only from what is here and what you already know.

**Independence.** Several models are drafting these same 36 entries separately so Nik Bear Brown can compare them. Don't read, search for or ask for any other model's drafts, including Claude's. The material below is source material only (the lexicon's record, candidate neighbors, posting snippets, Wikipedia, Wikidata and WordNet candidates); it holds no one's drafts.

**How to work.** Treat each concept on its own, as if you had never seen the others: don't carry a decision, a wording or a relation from one concept to the next. This is the **grounded** run: each concept comes with its candidate Wikipedia articles, Wikidata items and WordNet senses.

**Instructions for every concept** (use them exactly as written):

~~~~text
You draft entries for the Irreducibly Human Work Lexicon, a WordNet-style lexical database of work concepts (skills, knowledge areas, abilities, languages, and credentials) used to match job postings with course syllabi. You receive one concept and a bundle of source material. You return one JSON object.

Your job is to record what the sources support, not to complete a template. An empty relation list is a correct answer. A plausible relation you cannot support is an error.

Work through these steps in order.

1. Work sense. Read the concept record and the usage examples. Write one sentence saying what the concept means as a job requirement or learning outcome. Every later decision is about this sense.

2. Source links. For Wikipedia, Wikidata, and WordNet separately, pick the single candidate that matches the work sense, or abstain by setting choice to null. Abstain when no candidate matches, when the candidates describe a different sense, or when you cannot tell. Give a one-sentence reason either way. You may cite only sources you linked, plus Wikidata ancestors of the item you linked.

3. Definition. Write one to three sentences in your own words describing the concept as it appears in postings and syllabi. Never reuse more than eight consecutive words from any source. Cite the pointers that support it.

4. Variants. List surface forms that name this concept: abbreviations, alternate spellings, historical names. If a form names the concept only in some contexts, state the condition (for example, "when it labels a skill, role, or team, not the experience itself").

5. Relations. Use only these types, and include a relation only if its test passes with the actual names filled in:
   - synonym: the target can replace the concept in a posting or syllabus without changing what is asked for or taught.
   - hypernym: "[concept] is a kind of [target]" is true.
   - hyponym: "[target] is a kind of [concept]" is true.
   - meronym: practicing or knowing the concept routinely includes the target as a component.
   - holonym: the concept is routinely a component of the target.
   - uses: the concept is typically practiced with the target, which is a tool, runtime, framework, or other technology rather than a component.
   - requires: the target must be learned before the concept can be practiced.
   - certifies: only when the concept is a credential; the credential attests to the target.
   - contrast: the target is often confused with the concept but differs from it. Use this for false-equivalence risks, including look-alike names.
   Do not record antonyms or pertainyms. Work concepts almost never have them.

6. Basis. Give every definition, variant, and relation a basis:
   - "source": the provided material states it, and you give at least one pointer that identifies the exact statement, synset relation, passage, or example.
   - "model_knowledge": you believe it, but the provided material does not state it. This is allowed. Never label model knowledge as source, and never invent a pointer.

7. Targets. If a relation's target matches a concept in lexicon_neighbors, set target_id to that concept's id. Otherwise set target_id to null and proposed_new to true.

8. Final check. Before returning, review every claim. Remove any relation whose test fails when read with the real names, any pointer that does not say what you claim, and anything you added only because a slot was empty. Put any concern a reviewer should see (conflicting sources, unclear sense, a likely error in the lexicon's existing record) in flags.

Pointer formats:
- Wikidata statement: wd:QID#PID=VALUE_QID (for example, wd:Q100#P279=Q200)
- Wikidata label or alias: wd:QID#alias=TEXT
- WordNet lemma: wn:SYNSET_ID#lemma=TEXT
- WordNet relation: wn:SYNSET_ID#RELATION=TARGET_SYNSET_ID, where RELATION is hypernym, hyponym, part_meronym, part_holonym, member_meronym, or member_holonym
- Wikipedia passage: wp:REVISION_ID#quote=TEXT, where TEXT is copied exactly from the provided article and is at most 20 words
- Usage example: ex:EXAMPLE_ID

Return only this JSON object, with no preamble and no code fences:

{
  "concept_id": "string",
  "work_sense": "string",
  "links": {
    "wikipedia": {"choice": "REVISION_ID or null", "reason": "string"},
    "wikidata": {"choice": "QID or null", "reason": "string"},
    "wordnet": {"choice": "SYNSET_ID or null", "reason": "string"}
  },
  "definition": {"text": "string", "basis": "source or model_knowledge", "pointers": ["string"]},
  "variants": [
    {"text": "string", "condition": "string or null", "basis": "source or model_knowledge", "pointers": ["string"]}
  ],
  "relations": [
    {"type": "one of the nine types above", "target_label": "string", "target_id": "string or null", "proposed_new": false, "basis": "source or model_knowledge", "pointers": ["string"], "note": "string or null"}
  ],
  "flags": ["string"]
}
~~~~

**Before you answer**, check every draft against this list and fix what fails (one pass of fixes, no more):

- `links.wikipedia`, `links.wikidata` and `links.wordnet` each have a `choice`, and each is null or one of that concept's candidates below.
- The definition, each variant and each relation has `basis` `source` or `model_knowledge`, and every `source` claim has at least one pointer.
- Every pointer resolves in the material below: `wd:` names the linked item or one of its ancestors and the statement or alias is really there; `wn:` names the linked synset and the lemma or relation is really there; `wp:` names the linked article's revision id and quotes at most 20 words that appear word for word; `ex:` names an example below.
- Only the nine relation types. A `target_id` must be one of that concept's neighbors.
- `certifies` only when the concept's `kind` is `credential`.
- The definition shares no run of 9 or more consecutive words with any Wikipedia text below.

**What to send back.** One JSON object per concept, one per line, in the order below, each with one extra field:
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "02", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-02.jsonl`. Otherwise send one code block marked `jsonl` holding the 2 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 2: Java (`ls6hrpynv0`)

~~~~text
Concept record:
{
 "id": "ls6hrpynv0",
 "preferred_name": "Java",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Java (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "lak4led9d2",
  "name": "HotJava"
 },
 {
  "id": "hj8i6mh3zz",
  "name": "Chinese"
 },
 {
  "id": "iryd1t5hx3",
  "name": "Indonesian"
 },
 {
  "id": "c6s0kc7cs8",
  "name": "Arabic"
 },
 {
  "id": "h60l8olauw",
  "name": "JavaScript"
 },
 {
  "id": "wmeomhwzf1",
  "name": "Sundanese"
 },
 {
  "id": "v17l7v4fgv",
  "name": "Administrative"
 },
 {
  "id": "qb4qnsutxp",
  "name": "C++"
 },
 {
  "id": "eon43rmtrr",
  "name": "Greek"
 },
 {
  "id": "vphlc8dpfb",
  "name": "Mandarin"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "oxms4xxazw",
  "name": "WSDL2Java"
 },
 {
  "id": "yl4tfx5kdt",
  "name": "Visual Basic for Applications"
 },
 {
  "id": "x80b957frq",
  "name": "Ada"
 },
 {
  "id": "xiiyhhzd8l",
  "name": "ABAP"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "rqi69qjjr4",
  "name": "Java Communications API"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "t5qatususg",
  "name": "Julia"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 },
 {
  "id": "ivq3fs6epa",
  "name": "Lua"
 },
 {
  "id": "d7zsm83o61",
  "name": "SAS"
 },
 {
  "id": "oeixkjthc3",
  "name": "R"
 },
 {
  "id": "eaovn4ljeo",
  "name": "D"
 },
 {
  "id": "a0h79b66kq",
  "name": "C"
 },
 {
  "id": "wjye9vcd5l",
  "name": "Pascal"
 },
 {
  "id": "ru39hxzmz4",
  "name": "MATLAB"
 },
 {
  "id": "k8pcmxo14a",
  "name": "Ada 95"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:12",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Tech Lead Full-Stack Rails Engineer. software development|api|css|docker|elasticsearch|fullstack|html|javascript|kubernetes|postgresql|react|ror|ruby/rails|ai/ml|cad|advertising|redis|es6|web applications|mysql|nlp|fintech|micro services|github|system architecture|communication|excel|java|sql|git|llm|ai|go|ml"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:34",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: RPA Developer. [\"RPA\", \"UI Path\", \".Net\", \"Java\", \"C++\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:3",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Software Engineer - Innovation Lab. …ion BS in Computer Science or Computer Engineering. 2-4 years of experience as a software engineer. Strong development experience in C, C , Java. Developing systems applications on Linux/Android. Comfortable in Python language. Experience or knowledge in Artificial Intelligence Ability to take ideas…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:84",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "Javascript, PHP, Java"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:130",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: SAP Cloud Developer - Trainee. Java,JavaScript,Python,C Programming,C++ Programming,"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Java",
  "revision_id": "1376782458",
  "matched_by": "title",
  "text": "Java is one of the Greater Sunda Islands in the South East Asian country of Indonesia. It is bordered by the Indian Ocean to the south and the Java Sea (a part of Pacific Ocean) to the north. Java is the world's most populous island, home to an estimated 159.2 million people; about 56% of the Indonesian population, while constituting only 7% of the country's land area. Indonesia's capital city, Jakarta, is located on Java's northwestern coast.\n\nMany of the best known events in Indonesian history took place on Java. It was the centre of powerful Hindu-Buddhist empires, the Islamic sultanates, and the core of the colonial Dutch East Indies. Java was also the center of the Indonesian struggle for independence during the 1930s and 1940s. Java dominates Indonesia politically, economically, and culturally. Five of Indonesia's ten UNESCO world heritage sites are located in Java: Ujung Kulon National Park, Borobudur Temple, Prambanan Temple, Yogyakarta, and Sangiran Early Man Site.\n\nJava was formed by volcanic eruptions due to geologic subduction of the Australian Plate under the Sunda Plate. It is the 13th largest island in the world and the fifth largest in Indonesia by landmass, at about 132,644.29 square kilometres (51,214.25 mi) (including Madura's 5,408.35 square kilometres (2,088.18 mi) and smaller offshore islands). A chain of volcanic mountains is the east–west spine of the island.\n\nFour main languages are spoken on the island: Javanese, Sundanese, Madurese, and Betawi. Javanese and Sundanese are the most spoken. The ethnic groups native to the island are the Javanese in the central and eastern parts and Sundanese in the western parts. The Madurese in the Eastern salient of Java are migrants from Madura Island (which is part of East Java Province in administrative terms), while the Betawi in the capital city of Jakarta are hybrids from various ethnic groups in Indonesia. \n\nMost residents are bilingual, speaking Indonesian (the official language of Indonesia) as their first or second language. While the majority of the people of Java are Muslim, Java's population comprises people of diverse religious beliefs, ethnicities, and cultures.\n\nJava is divided into four administrative provinces: Banten, West Java, Central Java, and East Java, and two special regions, Jakarta and Yogyakarta.\n\nEtymology\n\nThe origins of the name \"Java\" are not clear. Java may have been named after the jawa (foxtail millet) plant, derived from the Proto-Austronesian root *zawa. The historian Michael Laffan argued that the vernacular form jawa is more likely to have derived from an older form *yaba, based on the directionality of sound changes. \n\nIn the early nineteenth century, the British scholar Stamford Raffles suggested that another possible source for Java's name is the word jauh (which he spelled jaú), a Malay word meaning \"beyond\" or \"distant\". It has been suggested that another possible root is *awa or *yawa, meaning \"home\", related to the Polynesian words awaʻi (awaiki) or hawaʻi (hawaiki), but these roots are not universally accepted as Proto-Austronesian. None of these alternative hypotheses has found broad support among scholars, so the jawa (millet) theory remains the generally accepted one. \n\nThe toponym Java first appears in foreign literary works around the turn of the Common Era. In Sanskrit texts like the Ramayana, Java is referred to as Yavadvīpa, with dvīpa meaning \"island\" and yava meaning \"barley\". Java is mentioned in the ancient Tamil epic Maṇimēkalai (spelled Shavakam) and also in the Pāli scripture Mahāniddesa (likely pre-1st century BCE) as a place to be reached by boats. \n\nThe Greek term Iabadiu mentioned in Claudius Ptolemy's Geographia (150 CE), composed during the height of the Roman Empire, possibly derives from a Middle Indo-Aryan language and seems to be a synonym of the Sanskrit Yāvadvīpa. \n\nChinese sources render the toponym Java, as 葉調 Yèdiào (Late Middle Chinese pronunciation: [jiap dɛwh]) and 耶婆提 Yépótí (Late Middle Chinese pronunciation: [jia ba dɛj]) in the early first millennium CE. Subsequently, there emerged a new Chinese toponym 闍婆 Shépó (Late Middle Chinese pronunciation: [d͡ʑia bwa]), as found in the court chronicles Book of Song (late 5th century) and Book of Liang (7th century). From the Yuan Dynasty (1271–1368) onwards, Java began to be called 爪哇 (Zhǎowā), the present-day name in Mandarin Chinese. \n\nIn the later Middle Ages, Muslim writers began to refer to the islands of Indonesia by the term al-Zabaj (Arabic: الزابج). The Arabic usage of the word Zabaj was very broad, often incorporating either Sumatra or Java or both. It is the Arabic term Zabaj, rather than the ancient Greek term Iabadiu, that had the greater influence on late medieval Europeans.\n\nGeography\n\nJava lies between Sumatra to the west and Bali to the east. Borneo lies to the north, and Christmas Island is to the south. It is the world's 13th largest island. Java is surrounded by the Java Sea to the north, the Sunda Strait to the west, the Indian Ocean to the south and Bali Strait and Madura Strait in the east.\n\nJava is almost entirely of volcanic origin; it contains 38 mountains forming an east–west spine that have at one time or another been active volcanoes. There are 112 volcanoes in all, 35 of which are active. The highest volcano in Java is Mount Semeru, 3,676 metres (12,060 ft). The most active volcano in Java and also in Indonesia is Mount Merapi, 2,930 metres (9,610 ft).\n\nJava's mountains and highlands split the interior into a series of relatively isolated regions suitable for wet-rice cultivation; the rice lands of Java are among the richest in the world. Java was the first place where Indonesian coffee was grown, beginning in 1699. Today, coffea arabica is grown on the Ijen Plateau by small-holders and larger plantations.\n\nThe area of Java is about 132,598.77 square kilometres (51,196.67 mi) (including Madura's 5,408.45 square kilometres (2,088.21 mi) and minor offshore islands). It is about 1,000 km (620 mi) long and up to 210 km (130 mi) wide. The island's longest river is the 600 km long Solo River. The river rises from its source in central Java at the Lawu volcano, then flows north and eastward to its mouth in the Java Sea near the city of Surabaya. Other major rivers are Brantas, Citarum, Cimanuk and Serayu.\n\nThe average temperature ranges from 22 °C (72 °F) to 29 °C (84 °F); average humidity is 75%. The northern coastal plains are normally hotter, averaging 34 °C (93 °F) during the day in the dry season. The south coast is generally cooler than the north, and highland areas inland are even cooler. The wet season begins in November and ends in April. During that time, rain falls mostly in the afternoons and intermittently during other parts of the year. The wettest months are January and February.\n\nWest Java is wetter than East Java, and mountainous regions receive much higher rainfall. The Parahyangan highlands of West Java receive over 4,000 millimetres (160 in) annually, while the north coast of East Java receives 900 millimetres (35 in) annually.\n\nNatural environment\n\nJava is an island with a large amount of biodiversity. The natural environment of Java is tropical rainforest, with ecosystems ranging from coastal mangrove forest on the north coast, rocky coastal cliffs on the southern coast, and low-lying tropical forest to high altitude rainforest on the slopes of mountainous volcanic regions in the interior. The Javan environment and climate gradually alters from west to east; from wet and humid dense rainforest in western parts, to a dry savanna environment in the east, corresponding to the climate and rainfall in these regions.\n\nJavan wildlife originally supported a rich biodiversity, where numbers of endemic species of flora and fauna flourished; such as the Javan rhinoceros, Javan banteng, Javan warty pig, Javan silvery gibbon, Javan lutung, Java mouse-deer, Javan rusa, and Javan leopard. With over 450 bird species and 37 endemic species including the Javan green magpie, Java sparrow, Javan hawk-eagle, Javan peafowl, and Javan blue-banded kingfisher, Java is a birdwatcher's paradise. There are about 130 freshwater fish species in Java. There are also several endemic amphibian species in Java, including 5 species of tree frogs.\n\nSince ancient times, people have opened the rainforest, altered the ecosystem, shaped the landscapes and created rice paddy and terraces to support the growing population. Javan rice terraces have existed for more than a millennium and had supported ancient agricultural kingdoms. The growing human population has put severe pressure on Java's wildlife, as rainforests were diminished and confined to highland slopes or isolated peninsulas. Some of Java's endemic species are now critically endangered, with some already extinct; Java used to have Javan tigers and Javan elephants, but both have been rendered extinct. Today, several national parks exist in Java that protect the remnants of its fragile wildlife, such as Ujung Kulon, Mount Halimun-Salak, Gede Pangrango, Baluran, Meru Betiri, Bromo Tengger Semeru and Alas Purwo.\n\nSurveys conducted by a team led by EcoVerde Global Consulting on the live bats trade in Java showed an ongoing long-term trade of large fruit bats for traditional medicine in all the major cities including Jakarta, Surabaya, Bekasi, Bandung and Yogyakarta.  Hundreds of animals are being offered for sale with higher numbers per capita in economically less affluent areas and more bats in cities with larger Christian populations\n\nHistory\n\nHomo erectus presence\n\nFossilised remains of Homo erectus, popularly known as the \"Java Man\", dating back 1.3 million years were found along the banks of the Bengawan Solo River.\n\nH. erectus arrived in Eurasia approximately 1.8 million years ago, in an event considered to be the first African exodus. There is evidence that the Java population of H. erectus lived in an ever-wet forest habitat. More specifically the environment resembled a savannah, but was likely regularly inundated (\"hydromorphic savanna\"). The plants found at the Trinil excavation site included grass (Poaceae), ferns, Ficus, and Indigofera, which are typical of lowland rainforest.\n\nH. e. soloensis was the last population of a long occupation history of the island of Java by H. erectus, beginning 1.51 to 0.93 million years ago at the Sangiran site, continuing 540 to 430 thousand years ago at the Trinil site, and finally 117 to 108 thousand years ago at Ngandong. If the date is correct for Solo Man, then they would represent a terminal population of H. erectus which sheltered in the last open-habitat refuges of East Asia before the rainforest takeover. Before the immigration of modern humans, Late Pleistocene Southeast Asia was also home to H. floresiensis endemic to the island of Flores, Indonesia, and H. luzonensis endemic to the island of Luzon, the Philippines. Genetic analysis of present-day Southeast Asian populations indicates the widespread dispersal of the Denisovans (a species currently recognisable only by their genetic signature) across Southeast Asia, whereupon they interbred with immigrating modern humans 45.7 and 29.8 thousand years ago. A 2021 genomic study indicates that, aside from the Denisovans, modern humans never interbred with any of these endemic human species, unless the offspring were unviable or the hybrid lineages have since died out.\n\nJudging by the sheer number of specimens deposited at Ngandong at the same time, there may have been a sizeable population of H. e soloensis before the volcanic eruption which resulted in their interment, but population is difficult to approximate with certainty. This site is quite far from the north coast of Java Island, and it is not always easy to determine the position of the coastline in prehistoric times because of significant geographical changes.\n\nThe southern coastline and estuary of the Bengawan Solo River at that time may have been different from what it is today, due to geological factors such as sedimentation, erosion, and changes in sea level over time. Currently, the estuary of the Bengawan Solo is in the Java Sea, but in prehistoric times, the river flow and estuary location may have changed. Geological and paleogeographic studies are often used to understand these changes.\n\nAfter the arrival of modern humans\n\nThe island's exceptional fertility and rainfall allowed the development of wet-field rice cultivation, which required sophisticated levels of cooperation between villages. Out of these village alliances, small kingdoms developed. The chain of volcanic mountains and associated highlands running the length of Java kept its interior regions and peoples separate and relatively isolated. Before the advent of Islamic states and European colonialism, the rivers provided the main means of communication, although Java's many rivers are mostly short. Only the Brantas river and Solo river could provide long-distance communication and this way their valleys supported the centers of major kingdoms. A system of roads, permanent bridges, and toll gates is thought to have been established in Java by at least the mid-17th century. Local powers could disrupt the routes as could the wet season and road use was highly dependent on constant maintenance. Consequently, communication between Java's population was difficult.\n\nAccording to Javanese legends circulating from the 18th century onwards, the emergence of civilization on the island of Java is associated with the arrival of Aji Saka (\"the Saka king\") in 78 CE. Aji Saka, as a \"mythic founder of the social and religious order\", is credited with establishing the key elements of Javanese civilization, such as eliminating demons, establishing the first kingdom, and introducing literacy.\n\nForeign sources around the beginning of the Common Era (see Names of Java), such as Valmiki's Ramayana, attest to Java's wealth and political organization at that time:\n\"Yavadvipa is decorated with seven kingdoms, gold and silver islands, rich in gold mines, and there is Śiśira (cold) Mountain that touches the sky with its peak.\"\n\nThe Greek geographer Ptolemy called the island Iabadiu or Sabadibai (Ancient Greek: Ιαβαδίου or Σαβαδίβαι). Ptolemy said that the name meant the \"Island of Barley\" and produced a lot of grain and gold, adding that its metropolis was called Argyre (Ἀργυρῆ) meaning silver in Greek.\n\nAccording to Chinese record Míng Shǐ, the Javanese kingdom was founded in 65 BCE.\n\nHindu-Buddhist (Classic) period\n\nThe period between the 5th and 15th century in Java is often referred to as the Hindu-Buddhist period, while in the broader context of Southeast Asia it is also referred to as the Classic period. The Taruma kingdom of western Java existed from the 5th to the 7th centuries, while the Heling kingdom sent embassies to China starting in 640. \n\nThe first state to leave a substantial historical record was the Mataram kingdom that was founded in central Java at the beginning of the 8th century. The rulers of Mataram patronised both Hindu and Buddhist institutions, including Java's earliest Hindu temples on the Dieng Plateau. In the second half of the 8th century, these rulers described themselves as members of the Sailendra dynasty, which strongly supported Mahayana Buddhism. Monumental temple complexes such as Borobudur (late 8th century) and Prambanan (mid-9th century) in central Java were constructed at this time.\n\nIn the late 920s, the center of power shifted from central to eastern Java. The eastern Javanese kingdoms of Kediri (c. 1100–1222), Singhasari (1222–1292) and Majapahit (1293–c. 1520s) were mainly dependent on rice agriculture, yet also pursued trade within the Indonesian archipelago, and with China and India. Majapahit was established by King Wijaya in 1293, and by the end of the reign of Hayam Wuruk (c. 1390s) it claimed suzerainty over most of the present-day Indonesian archipelago, although its direct control was likely limited to Java, Bali, and Madura. Hayam Wuruk's prime minister, Gajah Mada, led many of the kingdom's territorial conquests. For most of the 15th century, Majapahit continued to be the dominant power in eastern Java. This last period of Majapahit history coincides with the first emergence of Islamic kingdoms in Java.\n\nSpread of Islam and rise of Islamic sultanates\n\nIslam gradually became the dominant religion in Java throughout the 16th century. The port-cities of the north coast like Surabaya, Gresik, Demak and Cirebon were the first Javanese polities to adopt Islam, thanks to their interactions with foreign Muslim traders and clerics. Demak was the first Muslim kingdom to achieve a degree of hegemony in Java during the early 16th century, extending the reach of Muslim kingdoms westward to Cirebon and defeating the remnants of the Majapahit kingdom. After the mid-16th century, Demak gave way to other Muslim coastal kingdoms such as Cirebon and Banten in the west, and Surabaya in the east.\n\nAt the turn of the 17th century, the inland kingdom of Mataram became the dominant power of central and eastern Java. The rule of Sultan Agung of Mataram (r. 1613–1646) was crucial in establishing military hegemony and a \"mystic synthesis\" that harmonised Islam with pre-existing Javanese cultural attitudes. The coastal principalities of Surabaya and Cirebon were subjugated in the course of the early 17th century, leaving Mataram and Banten to face the emerging Dutch colonial power in Batavia.\n\nColonial periods\n\nJava's contact with the European colonial powers began in 1522 with a treaty between the Sunda kingdom and the Portuguese in Malacca. After its failure, the Portuguese presence was confined to Malacca and to the eastern islands.\nIn 1596, a four-ship expedition led by Cornelis de Houtman was the first Dutch contact with Indonesia. By the end of the 18th century the Dutch had extended their influence over the sultanates of the interior through the Dutch East India Company in Indonesia. The Dutch repeatedly intervened in wars between rival Mataram claimants to the Javanese throne. When the side they supported inevitably won due to their industrialised weapons, the Dutch forced land concessions from the side they supported. The Dutch whittled down the Mataram kingdoms until most of the island was conquered. Internal conflict prevented the Javanese from forming effective alliances against the Dutch. In the 1750s, the Javanese Sultan Mangkubumi tried to restore Mataram's control, but the Dutch divided the kingdom. Remnants of the Mataram survived as the Surakarta (Solo) and Yogyakarta principalities. Javanese kings claimed to rule with divine authority and the Dutch helped them to preserve remnants of a Javanese aristocracy by confirming them as regents or district officials within the colonial administration.\n\nJava's major role during the early part of the colonial period was as a producer of rice. In spice-producing islands like Banda, rice was regularly imported from Java, to supply the deficiency in means of subsistence.\n\nDuring the Napoleonic Wars in Europe, the Netherlands fell to France, as did its colony in the East Indies. During the short-lived Daendels administration, as French proxy rule on Java, the construction of the Great Post Road was commenced in 1808. The road, spanning from Anyer in Western Java to Panarukan in East Java,"
 },
 {
  "title": "Java (programming language)",
  "revision_id": "1375186425",
  "matched_by": "title",
  "text": "Java is a high-level, general-purpose, memory-safe, object-oriented programming language. It is intended to let programmers write once, run anywhere (WORA), meaning that compiled Java code can run on all platforms that support Java without the need to recompile. Java applications are usually compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture. The syntax of Java is similar to C and C++, but has fewer low-level facilities than either of them. The Java runtime provides dynamic abilities (such as reflective programming (reflection) and runtime code modification) usually unavailable in traditional compiled languages.\n\nJava gained popularity shortly after its release, and has been a popular programming language since then. Java was the third most popular programming language in 2022 according to GitHub. Although still widely popular, there has been a gradual decline in use of Java in recent years with other languages using JVM gaining popularity.\n\nJava was designed by James Gosling at Sun Microsystems. It was released in May 1995 as a core component of Sun's Java platform. The original and reference implementation Java compilers, virtual machines (VMs), and class libraries were released by Sun under proprietary licenses. As of May 2007, in compliance with the specifications of the Java Community Process, Sun had relicensed most of its Java technologies under the GPL-2.0-only license. Oracle, which bought Sun in 2010, offers its own HotSpot Java virtual machine. However, the official reference implementation is the OpenJDK JVM, which is open-source software used by most developers and is the default JVM for almost all Linux distributions.\n\nAs of March 2026, Java 26 is the current version.\n\nHistory\n\nJames Gosling, Mike Sheridan, and Patrick Naughton initiated the Java language project in June 1991. The language was initially called Oak after an oak tree that stood outside Gosling's office. Later the project went by the name Green and was finally renamed Java, from Java coffee, a type of coffee from Indonesia. Gosling designed Java with a C/C++-style syntax that system and application programmers would find familiar.\n\nSun Microsystems released the first public implementation as Java 1.0 in 1996. It promised write once, run anywhere (WORA) functionality, providing no-cost run-times on popular platforms. Fairly secure and featuring configurable security, it allowed network- and file-access restrictions. Major web browsers soon incorporated the ability to run Java applets within web pages, and Java quickly became popular. The Java 1.0 compiler was re-written in Java by Arthur van Hoff to comply strictly with the Java 1.0 language specification. With the advent of Java 2 (released initially as J2SE 1.2 in December 1998 – 1999), new versions had multiple configurations built for different types of platforms. J2EE included technologies and APIs for enterprise applications typically run in server environments, while J2ME featured APIs optimized for mobile applications. The desktop version was renamed J2SE. In 2006, for marketing purposes, Sun renamed new J2 versions as Java EE, Java ME, and Java SE, respectively.\n\nIn 1997, Sun Microsystems approached the ISO/IEC JTC 1 standards body and later the Ecma International to formalize Java, but it soon withdrew from the process. Java remains a de facto standard, controlled through the Java Community Process. At one time, Sun made most of its Java implementations available without charge, despite their proprietary software status. Sun generated revenue from Java through the selling of licenses for specialized products such as the Java Enterprise System.\n\nOn November 13, 2006, Sun released much of its Java virtual machine (JVM) as free and open-source software (FOSS), under the terms of the GPL-2.0-only license. On May 8, 2007, Sun finished the process, making all of its JVM's core code available under free software/open-source distribution terms, aside from a small portion of code to which Sun did not hold the copyright.\n\nSun's vice-president Rich Green said that Sun's ideal role with regard to Java was as an evangelist. Following Oracle Corporation's acquisition of Sun Microsystems in 2009–10, Oracle has described itself as the steward of Java technology with a relentless commitment to fostering a community of participation and transparency. This did not prevent Oracle from filing a lawsuit against Google shortly after that for using Java inside the Android SDK (see the Android section).\n\nOn April 2, 2010, James Gosling resigned from Oracle.\n\nIn January 2016, Oracle announced that Java run-time environments based on JDK 9 will discontinue the browser plugin.\n\nJava software runs on most devices from laptops to data centers, game consoles to scientific supercomputers.\n\nOracle (and others) highly recommend uninstalling outdated and unsupported versions of Java, due to unresolved security issues in older versions.\n\nPrinciples\n\nThere were five primary goals in creating the Java language:\n\nIt must be simple, object-oriented, and familiar.\n\nIt must be robust and secure.\n\nIt must be architecture-neutral and portable.\n\nIt must execute with high performance.\n\nIt must be interpreted, threaded, and dynamic.\n\nVersions\n\nAs of June 2026, Java 8, 11, 17, 21, and 25 are supported as long-term support (LTS) versions.\n\nOracle released the last zero-cost public update for the legacy version Java 8 LTS in January 2019 for commercial use, although it will otherwise still support Java 8 with public updates for personal use indefinitely. Other vendors such as Adoptium continue to offer free builds of OpenJDK's long-term support (LTS) versions. These builds may include additional security patches and bug fixes.\n\nMajor release versions of Java, along with their release dates:\n\nEditions\n\nSun has defined and supports four editions of Java targeting different application environments and segmented many of its APIs so that they belong to one of the platforms. The platforms are:\n\nJava Card for smart-cards.\n\nJava Platform, Micro Edition (Java ME) – targeting environments with limited resources.\n\nJava Platform, Standard Edition (Java SE) – targeting workstation environments.\n\nJava Platform, Enterprise Edition (Java EE) – targeting large distributed enterprise or Internet environments.\n\nThe classes in the Java APIs are organized into separate groups called packages. Each package contains a set of related interfaces, classes, subpackages and exceptions.\n\nSun also provided an edition called Personal Java that has been superseded by later, standards-based Java ME configuration-profile pairings.\n\nExecution system\n\nJava JVM and bytecode\n\nOne design goal of Java is portability, which means that programs written for the Java platform must run similarly on any combination of hardware and operating system with adequate run time support. This is achieved by compiling the Java language code to an intermediate representation called JVM bytecode, instead of directly to architecture-specific machine code. JVM bytecode instructions are analogous to machine code, but they are intended to be executed by a virtual machine (VM) written specifically for the host hardware. End-users commonly use a Java Runtime Environment (JRE) installed on their device for standalone Java applications or a web browser for Java applets.\n\nStandard libraries provide a generic way to access host-specific features such as graphics, threading, and networking.\n\nThe use of universal bytecode makes porting simple. However, the overhead of interpreting bytecode into machine instructions made interpreted programs almost always run more slowly than native executables. Just-in-time (JIT) compilers that compile byte-codes to machine code during runtime were introduced from an early stage. Java's Hotspot compiler is actually two compilers in one, with GraalVM (included in e.g. Java 11, but removed as of Java 16) allowing tiered compilation. Java itself is platform-independent and is adapted to the particular platform it is to run on by a Java virtual machine (JVM), which translates the JVM bytecode into the platform's machine language.\n\nPerformance\n\nPrograms written in Java have a reputation for being slower and requiring more memory than those written in C++. However, Java programs' execution speed improved significantly with the introduction of just-in-time compilation in 1997/1998 for Java 1.1, the addition of language features supporting better code analysis (such as inner classes, the StringBuilder class, optional assertions, etc.), and optimizations in the Java virtual machine, such as HotSpot becoming Sun's default JVM in 2000. With Java 1.5, the performance was improved with the addition of the java.util.concurrent package, including lock-free implementations of the ConcurrentMaps and other multi-core collections, and it was improved further with Java 1.6.\n\nNon-JVM\n\nSome platforms offer direct hardware support for Java; there are micro controllers that can run JVM bytecode in hardware instead of a software Java virtual machine, and some ARM-based processors could have hardware support for executing JVM bytecode through their Jazelle option, though support has mostly been dropped in current implementations of ARM.\n\nAutomatic memory management\n\nJava uses an automatic garbage collector to manage memory in the object lifecycle. The programmer determines when objects are created, and the Java runtime is responsible for recovering the memory once objects are no longer in use. Once no references to an object remain, the unreachable memory becomes eligible to be freed automatically by the garbage collector. Something similar to a memory leak may still occur if a programmer's code holds a reference to an object that is no longer needed, typically when objects that are no longer needed are stored in containers that are still in use. If methods for a non-existent object are called, a null pointer exception is thrown.\n\nOne of the ideas behind Java's automatic memory management model is that programmers can be spared the burden of having to perform manual memory management. In some languages, memory for the creation of objects is implicitly allocated on the stack or explicitly allocated and deallocated from the heap. In the latter case, the responsibility of managing memory resides with the programmer. If the program does not deallocate an object, a memory leak occurs. If the program attempts to access or deallocate memory that has already been deallocated, the result is undefined and difficult to predict, and the program is likely to become unstable or crash. This can be partially remedied by the use of smart pointers, but these add overhead and complexity. Garbage collection does not prevent logical memory leaks, i.e. those where the memory is still referenced but never used.\n\nGarbage collection may happen at any time. Ideally, it will occur when a program is idle. It is guaranteed to be triggered if there is insufficient free memory on the heap to allocate a new object; this can cause a program to stall momentarily. Explicit memory management is not possible in Java, however it is possible to manually request that the JVM do garbage collection.\n\nJava does not support C/C++ style pointer arithmetic, where object addresses can be arithmetically manipulated (e.g. by adding or subtracting an offset). This allows the garbage collector to relocate referenced objects and ensures type safety and security.\n\nAs in C++ and some other object-oriented languages, variables of Java's primitive data types are either stored directly in fields (for objects) or on the stack (for methods) rather than on the heap, as is commonly true for non-primitive data types (but see escape analysis). This was a conscious decision by Java's designers for performance reasons.\n\nJava contains multiple types of garbage collectors. Since Java 9, HotSpot uses the Garbage First Garbage Collector (G1GC) as the default. However, there are also several other garbage collectors that can be used to manage the heap, such as the Z Garbage Collector (ZGC) introduced in Java 11, and Shenandoah GC, introduced in Java 12 but unavailable in Oracle-produced OpenJDK builds. Shenandoah is instead available in third-party builds of OpenJDK, such as Eclipse Temurin. For most applications in Java, G1GC is sufficient. In prior versions of Java, such as Java 8, the Parallel Garbage Collector was used as the default garbage collector.\n\nHaving solved the memory management problem does not relieve the programmer of the burden of handling properly other kinds of resources, like network or database connections, file handles, etc., especially in the presence of exceptions.\n\nSyntax\n\nThe syntax of Java is largely influenced by C++ and C. Unlike C++, which combines the syntax for structured, generic, and object-oriented programming, Java was built almost exclusively as an object-oriented language. All code is written inside classes, and every data item is an object, with the exception of the primitive data types, (i.e. integers, floating-point numbers, boolean values, and characters), which are not objects for performance reasons.\n\nUnlike C++, Java does not support operator overloading or multiple inheritance for classes, though multiple inheritance is supported for interfaces.\n\nJava uses comments similar to those of C++. There are three different styles of comments: a single line style marked with two slashes (//), a multiple line style opened with /* and closed with */, and the Javadoc commenting style opened with /** and closed with */. The Javadoc style of commenting allows the user to run the Javadoc executable to create documentation for the program and can be read by some integrated development environments (IDEs) such as Eclipse to allow developers to access documentation within the IDE.\n\nHello world\n\nThe following is an example of a \"Hello, World!\" program in the traditional Java syntax:\n\npublic class HelloWorld {\n public static void main(String[] args) {\n System.out.println(\"Hello World!\");\n }\n}\n\nJava 25 introduced a simplified syntax for the main class and main method, which enables users to write small Java programs succinctly:\n\nvoid main() {\n IO.println(\"Hello World!\");\n}\n\nSpecial classes\n\nApplet\n\nJava applets were programs embedded in other applications, mainly in web pages displayed in web browsers. The Java applet API was deprecated with the release of Java 9 in 2017.\n\nServlet\n\nJava servlet technology provides Web developers with a simple, consistent mechanism for extending the functionality of a Web server and for accessing existing business systems. Servlets are server-side Java EE components that generate responses to requests from clients. Most of the time, this means generating HTML pages in response to HTTP requests, although there are a number of other standard servlet classes available, for example for WebSocket communication.\n\nThe Java servlet API has to some extent been superseded (but still used under the hood) by two standard Java technologies for web services:\n\nthe Java API for RESTful Web Services (JAX-RS 2.0) useful for AJAX, JSON and REST services, and\n\nthe Java API for XML Web Services (JAX-WS) useful for SOAP Web Services.\n\nTypical implementations of these APIs on Application Servers or Servlet Containers use a standard servlet for handling all interactions with the HTTP requests and responses that delegate to the web service methods for the actual business logic.\n\nJavaServer Pages\n\nJavaServer Pages (JSP) are server-side Java EE components that generate responses, typically HTML pages, to HTTP requests from clients. JSPs embed Java code in an HTML page by using the special delimiters <% and %>. A JSP is compiled to a Java servlet, a Java application in its own right, the first time it is accessed. After that, the generated servlet creates the response.\n\nSwing application\n\nSwing is a graphical user interface library for the Java SE platform. It is possible to specify a different look and feel through the pluggable look and feel system of Swing. Clones of Windows, GTK+, and Motif are supplied by Sun. Apple also provides an Aqua look and feel for macOS. Where prior implementations of these looks and feels may have been considered lacking, Swing in Java SE 6 addresses this problem by using more native GUI widget drawing routines of the underlying platforms.\n\nJavaFX application\n\nJavaFX is a software platform for creating and delivering desktop applications, as well as rich web applications that can run across a wide variety of devices. JavaFX is intended to replace Swing as the standard graphical user interface (GUI) library for Java SE, but since JDK 11 JavaFX has not been in the core JDK and is instead available as a separate module. JavaFX has support for desktop computers and web browsers on Microsoft Windows, Linux, and macOS. JavaFX does not have support for native OS look and feels.\n\nGenerics\n\nIn 2004, generics were added to the Java language, as part of J2SE 5.0. Prior to the introduction of generics, each variable declaration had to be of a specific type. For container classes, for example, this is a problem because there is no easy way to create a container that accepts only specific types of objects. Either the container operates on all subtypes of a class or interface, usually Object, or a different container class has to be created for each contained class. Generics allow compile-time type checking without having to create many container classes, each containing almost identical code. In addition to enabling more efficient code, certain runtime exceptions are prevented from occurring, by issuing compile-time errors. If Java prevented all runtime type errors (ClassCastExceptions) from occurring, it would be type safe.\n\nIn 2016, the type system of Java was proven unsound in that it is possible to use generics to construct classes and methods that allow assignment of an instance of one class to a variable of another unrelated class. Such code is accepted by the compiler, but fails at run time with a class cast exception.\n\nCriticism\n\nCriticisms directed at Java include the implementation of generics, speed, the handling of unsigned numbers, the implementation of floating-point arithmetic, and a history of security vulnerabilities in the primary Java VM implementation HotSpot.\nDevelopers have criticized the complexity and verbosity of the Java Persistence API (JPA), a standard part of Java EE. This has led to increased adoption of higher-level abstractions like Spring Data JPA, which aims to simplify database operations and reduce boilerplate code. The growing popularity of such frameworks suggests limitations in the standard JPA implementation's ease-of-use for modern Java development.\n\nClass libraries\n\nThe Java Class Library is the standard library, developed to support application development in Java. It is controlled by Oracle in cooperation with others through the Java Community Process program. Companies or individuals participating in this process can influence the design and development of the APIs. This process has been a subject of controversy during the 2010s. The class library contains features such as:\n\nThe core libraries, which include:\n\nInput/output (I/O or IO) and non-blocking I/O (NIO), or IO/NIO\n\nNetworking (new user agent (HTTP client) since Java 11)\n\nReflective programming (reflection)\n\nConcurrent computing (concurrency)\n\nGenerics\n\nScripting, Compiler\n\nFunctional programming (Lambda, streaming)\n\nCollection libraries that implement data structures such as lists, dictionaries, trees, sets, queues and double-ended queue, or stacks\n\nXML Processing (Parsing, Transforming, Validating) libraries\n\nSecurity\n\nInternationalization and localization libraries\n\nThe integration libraries, which allow the application writer to communicate with external systems. These libraries include:\n\nThe Java Database Connectivity (JDBC) API for database access\n\nJava Naming and Directory Interface (JNDI) for lookup and discovery\n\nJava remote method invocation (RMI) and Common Object Request Broker Architecture (CORBA) for distributed application development\n\nJava Management Extensions (JMX) for managing and monitoring applications\n\nUser interface libraries, which include:\n\nThe (heavyweight, or native) Abstract Window"
 },
 {
  "title": "Sun Microsystems",
  "revision_id": "1378120628",
  "matched_by": "redirect",
  "text": "Sun Microsystems, Inc., often known as Sun for short, was an American technology company that existed from 1982 to 2010 which developed and sold computers, computer hardware, software, and information technology services. Sun contributed significantly to the evolution of several key computing technologies, among them Unix, RISC processors, thin client computing, and virtualized computing. At its height, Sun's headquarters were in Santa Clara, California (part of Silicon Valley), on the former west campus of the Agnews Developmental Center.\n\nSun products included computer servers and workstations built using Motorola 680x0 processors, then later their own RISC-based SPARC processor architecture, as well as on x86-based AMD Opteron and Intel Xeon processors. Sun also developed its own storage systems and a suite of software products, including the Unix-based SunOS and later Solaris operating systems, developer tools, Web infrastructure software, and identity management applications. Technologies that Sun created include the Java programming language, the Java platform and Network File System (NFS).\n\nIn general, Sun was a proponent of open systems, particularly Unix. It was also a major contributor to open-source software, as evidenced by its $1 billion purchase, in 2008, of MySQL, an open-source relational database management system. Other notable Sun acquisitions include Cray Business Systems Division, Storagetek, and Innotek GmbH, creators of VirtualBox. On April 20, 2009, it was announced that Oracle would acquire Sun for US$7.4 billion, or US$5.6 billion net of Sun's cash and debt. The deal was completed on January 27, 2010.\n\nHistory\n\nThe initial design for what became Sun's first Unix workstation, the Sun-1, was conceived by Andy Bechtolsheim when he was a graduate student at Stanford University in Palo Alto, California. Bechtolsheim originally designed the SUN workstation for the Stanford University Network communications project as a personal CAD workstation. It was designed around the Motorola 68000 processor with an advanced memory management unit (MMU) to support the Unix operating system with virtual memory support. He built the first examples from spare parts obtained from Stanford's Department of Computer Science and Silicon Valley supply houses.\n\nOn February 24, 1982, Scott McNealy, Andy Bechtolsheim, and Vinod Khosla, all Stanford graduate students, founded Sun Microsystems. Bill Joy of Berkeley, a primary developer of the Berkeley Software Distribution (BSD), joined soon after and is counted as one of the original founders. The company was the second, after rival Apollo Computer, to specialize in workstations. The name \"Sun\" is derived from the initials of the Stanford University Network (SUN). McNealy focused on operations; Fortune described him as \"notoriously cheap\". Sun was profitable from its first quarter in July 1982.\n\nBy 1983, Sun was known for producing 68k-based systems with high-quality graphics that were the only computers other than DEC's VAX to run 4.2BSD. It licensed the computer design to other manufacturers, which typically used it to build Multibus-based systems running Unix from UniSoft. Wall Street was an important early market, as were CAD/CAM, CAE, CASE, and other technical markets. By 1989, InfoWorld described Sun as \"the unqualified leader in the workstation arena\", and target of DEC and Hewlett-Packard (HP)'s own products.\n\nSun's initial public offering was in 1986 under the stock symbol SUNW, for Sun Workstations (later Sun Worldwide). The symbol was changed in 2007 to JAVA; Sun stated that the brand awareness associated with its Java platform better represented the company's current strategy.\n\nSun's logo, which features four interleaved copies of the word sun in the form of a rotationally symmetric ambigram, was designed by professor Vaughan Pratt, also of Stanford. The initial version of the logo was orange and had the sides oriented horizontally and vertically, but it was subsequently rotated to stand on one corner and re-colored purple, and later blue.\n\nDot-com bubble and aftermath\n\nDuring the dot-com bubble, Sun began making more money, with its stock rising as high as $250 per share. It also began spending much more, hiring workers and building itself out. Some of this was because of genuine demand, but much was from web start-up companies anticipating business that would never happen. In 2000, the bubble burst. Sales in Sun's important hardware division went into freefall as customers closed shop and auctioned high-end servers.\n\nSeveral quarters of steep losses led to executive departures, rounds of layoffs, and other cost cutting. In December 2001, the stock fell to the 1998, pre-bubble level of about $100. It continued to fall, faster than many other technology companies. A year later, it had reached below $10 (a tenth of what it was in 1990), but it eventually bounced back to $20. In mid-2004, Sun closed its Newark, California, factory and consolidated all manufacturing to Hillsboro, Oregon and Linlithgow, Scotland. In 2006, the rest of the Newark campus was put on the market.\n\nPost-crash focus\n\nIn 2004, Sun canceled two major processor projects which emphasized high instruction-level parallelism and operating frequency. Instead, the company chose to concentrate on processors optimized for multi-threading and multiprocessing, such as the UltraSPARC T1 processor (codenamed \"Niagara\"). The company also announced a collaboration with Fujitsu to use the Japanese company's processor chips in mid-range and high-end Sun servers. These servers were announced on April 17, 2007, as the M-Series, part of the SPARC Enterprise series.\n\nIn February 2005, Sun announced the Sun Grid, a grid computing deployment on which it offered utility computing services priced at US$1 per CPU/hour for processing and per GB/month for storage. This offering built upon an existing 3,000-CPU server farm used for internal R&D for over 10 years, which Sun marketed as being able to achieve 97% utilization. In August 2005, the first commercial use of this grid was announced for financial risk simulations which were later launched as its first software as a service product.\n\nIn January 2005, Sun reported a net profit of $19 million for fiscal 2005 second quarter, for the first time in three years. This was followed by net loss of $9 million on GAAP basis for the third quarter 2005, as reported on April 14, 2005. In January 2007, Sun reported a net GAAP profit of $126 million on revenue of $3.337 billion for its fiscal second quarter. Shortly following that news, it was announced that Kohlberg Kravis Roberts (KKR) would invest $700 million in the company.\n\nSun had engineering groups in Bangalore, Beijing, Dublin, Grenoble, Hamburg, Prague, St. Petersburg, Tel Aviv, Tokyo, Canberra and Trondheim.\n\nIn 2007–2008, Sun posted revenue of $13.8 billion and had $2 billion in cash. First-quarter 2008 losses were $1.68 billion; revenue fell 7% to $12.99 billion. Sun's stock lost 80% of its value November 2007 to November 2008, reducing the company's market value to $3 billion. With falling sales to large corporate clients, Sun announced plans to lay off 5,000 to 6,000 workers, or 15–18% of its work force. It expected to save $700 million to $800 million a year as a result of the moves, while also taking up to $600 million in charges.\n\nAcquisition by Oracle\n\nOn September 3, 2009, the European Commission opened an in-depth investigation into the proposed takeover of Sun Microsystems by Oracle. On November 9, 2009, the Commission issued a statement of objections relating to the acquisition. Finally, on January 21, 2010, the European Commission approved Oracle's acquisition of Sun. The Commission's investigation showed that another open database, PostgreSQL, was considered by many users of this type of software as a credible alternative to MySQL and could to some extent replace the competitive strength that the latter currently represents in the database market.\n\nSun was sold to Oracle Corporation in 2009 for $5.6 billion.\n\nSun's staff were asked to share anecdotes about their experiences at Sun. A website containing videos, stories, and photographs from 27 years at Sun was made available on September 2, 2009.\n\nIn October, Sun announced a second round of thousands of employees to be laid off, blamed partially on delays in approval of the merger.\n\nThe transaction was completed in early 2010.\n\nIn January 2011, Oracle agreed to pay $46 million to settle charges that it submitted false claims to US federal government agencies and paid \"kickbacks\" to systems integrators.\n\nIn February 2011, Sun's former Menlo Park, California, campus of about 1,000,000 square feet (93,000 m) was sold, and it was announced that it would become headquarters for Facebook. The sprawling facility, built around an enclosed courtyard, was nicknamed \"Sun Quentin\" by Facebook's employees. Notably, Facebook founder Mark Zuckerberg did not change the sign in the front of the campus, he simply had it turned around and the company's logo put on the other side. The remains of the old Sun logo was left as a reminder of \"what happens when you take your eye off the ball.\"\n\nOn September 1, 2011, Sun India legally became part of Oracle. It had been delayed due to legal issues in Indian court.\n\nSun acquisitions\n\n1987: Trancept Systems, a high-performance graphics hardware company\n\n1987: Sitka Corp, networking systems linking the Macintosh with IBM PCs\n\n1987: Centram Systems West, maker of networking software for PCs, Macs and Sun systems\n\n1988: Folio, Inc., developer of intelligent font scaling technology and the F3 font format\n\n1991: Interactive Systems Corporation's Intel/Unix OS division, from Eastman Kodak Company\n\n1992: Praxsys Technologies, Inc., developers of the Windows emulation technology that eventually became Wabi\n\n1994: Thinking Machines Corporation hardware division\n\n1996: Lighthouse Design, Ltd.\n\n1996: Cray Business Systems Division, from Silicon Graphics\n\n1996: Integrated Micro Products, specializing in fault tolerant servers\n\n1996: Thinking Machines Corporation software division\n\nFebruary 1997: LongView Technologies, LLC\n\nAugust 1997: Diba, technology supplier for the Information Appliance industry\n\nSeptember 1997: Chorus Systèmes SA, creators of ChorusOS\n\nNovember 1997: Encore Computer Corporation's storage business\n\n1998: RedCape Software\n\n1998: i-Planet, a small software company that produced the \"Pony Espresso\" mobile email client—its name (sans hyphen) for the Sun-Netscape software alliance\n\nJune 1998: Dakota Scientific Software, Inc.—development tools for high-performance computing\n\nJuly 1998: NetDynamics—developers of the NetDynamics Application Server\n\nOctober 1998: Beduin, small software company that produced the \"Impact\" small-footprint Java-based Web browser for mobile devices.\n\n1999: Star Division, German software company and with it StarOffice, which was later released as open source under the name OpenOffice.org\n\n1999: MAXSTRAT Corporation, a company in Milpitas, California selling Fibre Channel storage servers.\n\nOctober 1999: Forté Software, an enterprise software company specializing in integration solutions and developer of the Forte 4GL\n\n1999: TeamWare\n\n1999: NetBeans, produced a modular IDE written in Java, based on a student project at Charles University in Prague\n\nMarch 2000: Innosoft International, Inc. a software company specializing in highly scalable MTAs (PMDF) and Directory Services.\n\nJuly 2000: Gridware, a software company whose products managed the distribution of computing jobs across multiple computers\n\nSeptember 2000: Cobalt Networks, an Internet appliance manufacturer for $2 billion\n\nDecember 2000: HighGround, with a suite of Web-based management solutions\n\n2001: LSC, Inc., an Eagan, Minnesota company that developed Storage and Archive Management File System (SAM-FS) and Quick File System QFS file systems for backup and archive\n\nMarch 2001: InfraSearch, a peer-to-peer search company based in Burlingame.\n\nMarch 2002: Clustra Systems\n\nJune 2002: Afara Websystems, developed SPARC processor–based technology\n\nSeptember 2002: Pirus Networks, intelligent storage services\n\nNovember 2002: Terraspring, infrastructure automation software\n\nJune 2003: Pixo, added to the Sun Content Delivery Server\n\nAugust 2003: CenterRun, Inc.\n\nDecember 2003: Waveset Technologies, identity management\n\nJanuary 2004 Nauticus Networks\n\nFebruary 2004: Kealia, founded by original Sun founder Andy Bechtolsheim, developed AMD-based 64-bit servers\n\nJanuary 2005: SevenSpace, a multi-platform managed services provider\n\nMay 2005: Tarantella, Inc. (formerly known as Santa Cruz Operation (SCO)), for $25 million\n\nJune 2005: SeeBeyond, a Service-Oriented Architecture (SOA) software company for $387m\n\nJune 2005: Procom Technology, Inc.'s NAS IP Assets\n\nAugust 2005: StorageTek, data storage technology company for $4.1 billion\n\nFebruary 2006: Aduva, software for Solaris and Linux patch management\n\nOctober 2006: Neogent\n\nApril 2007: SavaJe, the SavaJe OS, a Java OS for mobile phones\n\nSeptember 2007: Cluster File Systems, Inc.\n\nNovember 2007: Vaau, Enterprise Role Management and identity compliance solutions\n\nFebruary 2008: MySQL AB, the company offering the open source database MySQL for $1 billion.\n\nFebruary 2008: Innotek GmbH, developer of the VirtualBox virtualization product\n\nApril 2008: Montalvo Systems, x86 microprocessor startup acquired before first silicon\n\nJanuary 2009: Q-layer, a software company with cloud computing solutions\n\nMajor stockholders\n\nAs of May 11, 2009, the following shareholders held over 100,000 common shares of Sun and at $9.50 per share offered by Oracle, they received the amounts indicated when the acquisition closed.\n\nHardware\n\nFor the first decade of Sun's history, the company positioned its products as technical workstations, competing successfully as a low-cost vendor during the Workstation Wars of the 1980s. It then shifted its hardware product line to emphasize servers and storage. High-level telecom control systems such as Operational Support Systems service predominantly used Sun equipment.\n\nMotorola-based systems\n\nSun originally used Motorola 68000 family central processing units for the Sun-1 through Sun-3 computer series. The Sun-1 employed a 68000 CPU, the Sun-2 series, a 68010. The Sun-3 series was based on the 68020, with the later Sun-3x using the 68030.\n\nSPARC-based systems\n\nIn 1987, the company began using SPARC (Scalable Processor ARChitecture), a RISC processor architecture of its own design, in its computer systems, starting with the Sun-4 line. SPARC was initially a 32-bit architecture (SPARC V7) until the introduction of the SPARC V9 architecture in 1995, which added 64-bit extensions.\n\nSun developed several generations of SPARC-based computer systems, including the SPARCstation, Ultra, and Sun Blade series of workstations, and the SPARCserver, Netra, Enterprise, and Sun Fire line of servers.\n\nIn the early 1990s the company began to extend its product line to include large-scale symmetric multiprocessing servers, starting with the four-processor SPARCserver 600MP. This was followed by the 8-processor SPARCserver 1000 and 20-processor SPARCcenter 2000, which were based on work done in conjunction with Xerox PARC. In 1995 the company introduced Sun Ultra series machines that were equipped with the first 64-bit implementation of SPARC processors (UltraSPARC). In the late 1990s the transformation of product line in favor of large 64-bit SMP systems was accelerated by the acquisition of Cray Business Systems Division from Silicon Graphics. Their 32-bit, 64-processor Cray Superserver 6400, related to the SPARCcenter, led to the 64-bit Sun Enterprise 10000 high-end server (otherwise known as Starfire or E10K).\n\nIn September 2004, Sun made available systems with UltraSPARC IV which was the first multi-core SPARC processor. It was followed by UltraSPARC IV+ in September 2005 and its revisions with higher clock speeds in 2007. These CPUs were used in the most powerful, enterprise class high-end CC-NUMA servers developed by Sun, such as the Sun Fire E15K and the Sun Fire E25K.\n\nIn November 2005, Sun launched the UltraSPARC T1, notable for its ability to concurrently run 32 threads of execution on 8 processor cores. Its intent was to drive more efficient use of CPU resources, which is of particular importance in data centers, where there is an increasing need to reduce power and air conditioning demands, much of which comes from the heat generated by CPUs. The T1 was followed in 2007 by the UltraSPARC T2, which extended the number of threads per core from 4 to 8. Sun has open sourced the design specifications of both the T1 and T2 processors via the OpenSPARC project.\n\nIn 2006, Sun ventured into the blade server (high density rack-mounted systems) market with the Sun Blade (distinct from the Sun Blade workstation).\n\nIn April 2007, Sun released the SPARC Enterprise server products, jointly designed by Sun and Fujitsu and based on Fujitsu SPARC64 VI and later processors. The M-class SPARC Enterprise systems include high-end reliability and availability features. Later T-series servers have also been badged SPARC Enterprise rather than Sun Fire.\n\nIn April 2008, Sun released servers with UltraSPARC T2 Plus, which is an SMP capable version of UltraSPARC T2, available in 2 or 4 processor configurations. It was the first CoolThreads CPU with multi-processor capability and it made possible to build standard rack-mounted servers that could simultaneously process up to massive 256 CPU threads in hardware (Sun SPARC Enterprise T5440), which is considered a record in the industry.\n\nSince 2010, all further development of Sun machines based on SPARC architecture (including new SPARC T-Series servers, SPARC T3 and T4 chips) is done as a part of Oracle Corporation hardware division.\n\nx86-based systems\n\nIn the late 1980s, Sun also marketed an Intel 80386–based machine, the Sun386i; this was designed to be a hybrid system, running SunOS but at the same time supporting DOS applications. This only remained on the market for a brief time. A follow-up \"486i\" upgrade was announced but only a few prototype units were ever manufactured.\n\nSun's brief first foray into x86 systems ended in the early 1990s, as it decided to concentrate on SPARC and retire the last Motorola systems and 386i products, a move dubbed by McNealy as \"all the wood behind one arrowhead\". Even so, Sun kept its hand in the x86 world, as a release of Solaris for PC compatibles began shipping in 1993.\n\nIn 1997, Sun acquired Diba, Inc., followed later by the acquisition of Cobalt Networks in 2000, with the aim of building network appliances (single function computers meant for consumers). Sun also marketed a Network Computer (a term popularized and eventually trademarked by Oracle); the JavaStation was a diskless system designed to run Java applications.\n\nAlthough none of these business initiatives were particularly successful, the Cobalt purchase gave Sun a toehold for its return to the x86 hardware market. In 2002, Sun introduced its first general purpose x86 system, the LX50, based in part on previous Cobalt system expertise. This was also Sun's first system announced to support Linux as well as Solaris.\n\nIn 2003, Sun announced a strategic alliance with AMD to produce x86/x64 servers based on AMD's Opteron processor; this was followed shortly by Sun's acquisition of Kealia, a startup founded by original Sun founder Andy Bechtolsheim, which had been focusing on high-performance AMD-based servers.\n\nThe following year, Sun launched the Opteron-based Sun Fire V20z and V40z servers, and the Sun Java Workstation W1100z and W2100z workstations.\n\nIn September 2005 Sun unveiled a new range of Opteron-based servers: the Sun Fire X2100, X4100 and X4200 servers. These were designed from scratch by a team led by Bechtolsheim to address heat and power consumption issues commonly faced in data centers. In July 2006, the Sun Fire X4500 and X4600 systems were introduced, extending a line of x64 systems that support not only Solaris, but also Linux and Microsoft Windows.\n\nIn January 2007 Sun announced a broad strategic alliance with Intel. Intel endorsed Solaris as a mainstream operating system and as its mission critical Unix for its Xeon processor–based systems, and contributed engineering resources to OpenSolaris. Sun began using the Intel Xeon processor in its x64 server line, starting with the Sun Blade X6250 server"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q3757",
  "label": "Java",
  "description": "island of Indonesia",
  "aliases": [
   "Pulau Jawa",
   "Jawa Island",
   "Java Island",
   "Pulau Java",
   "Jawa",
   "Java island",
   "Java, Indonesia",
   "Ява"
  ],
  "claims": {
   "P31": [
    "Q23442"
   ],
   "P361": [
    "Q165481"
   ],
   "P1889": [
    "Q297675",
    "Q1100132",
    "Q251",
    "Q2089134",
    "Q124377739"
   ]
  },
  "revision_id": "2571925305",
  "value_labels": {
   "Q23442": "island",
   "Q165481": "Greater Sunda Islands",
   "Q297675": "Jawa",
   "Q1100132": "Java",
   "Q251": "Java",
   "Q2089134": "Java",
   "Q124377739": "Jawa"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q251",
  "label": "Java",
  "description": "object-oriented programming language",
  "aliases": [
   "java programming language"
  ],
  "claims": {
   "P31": [
    "Q56062429",
    "Q7397",
    "Q12772052",
    "Q9143"
   ],
   "P279": [
    "Q9143"
   ],
   "P361": [
    "Q1713118"
   ],
   "P1889": [
    "Q1713118",
    "Q2005",
    "Q2089134",
    "Q3757"
   ]
  },
  "revision_id": "2572516227",
  "value_labels": {
   "Q56062429": "JVM language",
   "Q7397": "software",
   "Q12772052": "multi-paradigm programming language",
   "Q9143": "programming language",
   "Q1713118": "Java platform",
   "Q2005": "JavaScript",
   "Q2089134": "Java",
   "Q3757": "Java"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q14647",
  "label": "Sun Microsystems",
  "description": "defunct American computer hardware and software company",
  "aliases": [
   "Sun Microsystems, Inc.",
   "Sun",
   "Stanford University Network"
  ],
  "claims": {
   "P31": [
    "Q1058914",
    "Q891723",
    "Q4830453",
    "Q110080207"
   ],
   "P361": [
    "Q19900"
   ]
  },
  "revision_id": "2571971155",
  "value_labels": {
   "Q1058914": "software company",
   "Q891723": "public company",
   "Q4830453": "business",
   "Q110080207": "academic spin-off",
   "Q19900": "Oracle Corporation"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q23442",
  "label": "island",
  "description": "piece of sub-continental land completely surrounded by water",
  "aliases": [
   "isle",
   "islands"
  ],
  "claims": {
   "P31": [
    "Q25894868"
   ],
   "P279": [
    "Q271669",
    "Q205895",
    "Q2221906",
    "Q17334923"
   ],
   "P1889": [
    "Q9380282",
    "Q2301527"
   ]
  },
  "revision_id": "2568806950",
  "ancestor_of": "Q3757",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q25894868",
  "label": "type of environment",
  "description": "type of environment or place (instances: marine environment, space, ground, …)",
  "aliases": [
   "environment type",
   "place or environment type",
   "place type"
  ],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q137015716"
   ],
   "P460": [
    "Q137018865"
   ]
  },
  "revision_id": "2567536305",
  "ancestor_of": "Q3757",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q271669",
  "label": "landform",
  "description": "natural or anthropogenic land feature on the solid surface of the Earth or other planetary body; geomorphological unit in the Earth sciences",
  "aliases": [
   "geographic feature",
   "land form"
  ],
  "claims": {
   "P31": [
    "Q12046615"
   ],
   "P279": [
    "Q12766313",
    "Q618123",
    "Q141737655"
   ],
   "P361": [
    "Q186131",
    "Q107425"
   ]
  },
  "revision_id": "2571291417",
  "ancestor_of": "Q3757",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q205895",
  "label": "landmass",
  "description": "contiguous area of land surrounded by ocean; large continuous area of land, either surrounded by sea or contiguous with another landmass",
  "aliases": [
   "land mass"
  ],
  "claims": {
   "P279": [
    "Q20719696",
    "Q82794"
   ],
   "P361": [
    "Q1349417"
   ],
   "P460": [
    "Q11081619"
   ],
   "P1889": [
    "Q15063765",
    "Q18941711"
   ]
  },
  "revision_id": "2559236097",
  "ancestor_of": "Q3757",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2221906",
  "label": "geographic location",
  "description": "point, line or area on or near Earth",
  "aliases": [
   "place",
   "geographical location",
   "setting",
   "location"
  ],
  "claims": {
   "P31": [
    "Q96253971",
    "Q137015716"
   ],
   "P279": [
    "Q27096213",
    "Q17334923",
    "Q141149247"
   ],
   "P361": [
    "Q1349417"
   ],
   "P460": [
    "Q98929991"
   ],
   "P1889": [
    "Q82794",
    "Q618123",
    "Q17334923",
    "Q22664",
    "Q1503302"
   ]
  },
  "revision_id": "2569947170",
  "ancestor_of": "Q3757",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q56062429",
  "label": "JVM language",
  "description": "programming language whose main compiler produces Java bytecode that runs in the Java virtual machine",
  "aliases": [
   "JVM programming language",
   "Español"
  ],
  "claims": {
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2540995155",
  "ancestor_of": "Q251",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7397",
  "label": "software",
  "description": "non-tangible executable component of a computer",
  "aliases": [
   "computer software",
   "computational tool",
   "dghed",
   "SW"
  ],
  "claims": {
   "P31": [
    "Q63981612",
    "Q123588392"
   ],
   "P279": [
    "Q17537576",
    "Q47461344",
    "Q12774177",
    "Q2424752"
   ],
   "P361": [
    "Q68",
    "Q1194864"
   ],
   "P527": [
    "Q40056",
    "Q494756"
   ],
   "P1889": [
    "Q2297604",
    "Q104851"
   ]
  },
  "revision_id": "2570277370",
  "ancestor_of": "Q251",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12772052",
  "label": "multi-paradigm programming language",
  "description": "programming language type",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2552000821",
  "ancestor_of": "Q251",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9143",
  "label": "programming language",
  "description": "language for communicating instructions to a machine",
  "aliases": [
   "computer language",
   "computer programming language",
   "coding language",
   "computer programming"
  ],
  "claims": {
   "P31": [
    "Q66747126",
    "Q137527772"
   ],
   "P279": [
    "Q629206"
   ],
   "P361": [
    "Q68"
   ],
   "P527": [
    "Q1152399",
    "Q25346349",
    "Q1199356",
    "Q865760"
   ],
   "P1889": [
    "Q4117406",
    "Q173341",
    "Q189224",
    "Q629206",
    "Q77654221"
   ]
  },
  "revision_id": "2570899010",
  "ancestor_of": "Q251",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9143",
  "label": "programming language",
  "description": "language for communicating instructions to a machine",
  "aliases": [
   "computer language",
   "computer programming language",
   "coding language",
   "computer programming"
  ],
  "claims": {
   "P31": [
    "Q66747126",
    "Q137527772"
   ],
   "P279": [
    "Q629206"
   ],
   "P361": [
    "Q68"
   ],
   "P527": [
    "Q1152399",
    "Q25346349",
    "Q1199356",
    "Q865760"
   ],
   "P1889": [
    "Q4117406",
    "Q173341",
    "Q189224",
    "Q629206",
    "Q77654221"
   ]
  },
  "revision_id": "2570899010",
  "ancestor_of": "Q251",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q63981612",
  "label": "product category",
  "description": "group of related products",
  "aliases": [
   "category of product",
   "type of product (group)",
   "group of type of product",
   "product type group",
   "kind of product (group)"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414",
    "Q29028649"
   ],
   "P279": [
    "Q16887380",
    "Q96251598"
   ],
   "P1889": [
    "Q128889633",
    "Q13443840"
   ]
  },
  "revision_id": "2551402811",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q123588392",
  "label": "type of tool",
  "description": "Wikidata metaclass for tool, equipment, instrument and appliance including physical, virtual, and abstract objects",
  "aliases": [
   "kind of tool",
   "tool-type",
   "class of tool",
   "tool class"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q96251598"
   ]
  },
  "revision_id": "2561091899",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17537576",
  "label": "creative work",
  "description": "artistic creation",
  "aliases": [
   "artwork",
   "work of art",
   "creative works",
   "work",
   "works"
  ],
  "claims": {
   "P31": [
    "Q133449656"
   ],
   "P279": [
    "Q15621286",
    "Q141524128"
   ],
   "P1889": [
    "Q8253",
    "Q838948",
    "Q15621286",
    "Q386724",
    "Q111955339"
   ]
  },
  "revision_id": "2568033210",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q47461344",
  "label": "written work",
  "description": "any work expressed in writing, such as inscriptions, manuscripts, documents or maps",
  "aliases": [
   "creative written work",
   "written delivery"
  ],
  "claims": {
   "P31": [
    "Q133449656"
   ],
   "P279": [
    "Q15621286"
   ],
   "P361": [
    "Q504952"
   ],
   "P460": [
    "Q20058025",
    "Q131377954"
   ],
   "P1889": [
    "Q571",
    "Q3331189",
    "Q7725634",
    "Q20058025"
   ]
  },
  "revision_id": "2563801972",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116481801",
  "label": "type of programming language",
  "description": "Wikidata metaclass",
  "aliases": [
   "kind of programming language",
   "programming language type",
   "programming language category",
   "category of programming languages"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257",
    "Q137527772"
   ]
  },
  "revision_id": "2555835128",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q66747126",
  "label": "computer science term",
  "description": "technical term; word or phrase that is part of computer science terminology",
  "aliases": [
   "computer science concept",
   "computer term",
   "informatics term"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q137426749",
    "Q137429456"
   ],
   "P279": [
    "Q12812139",
    "Q999234",
    "Q151885"
   ],
   "P361": [
    "Q3457057"
   ]
  },
  "revision_id": "2547355639",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q137527772",
  "label": "type of computer language",
  "description": "metaclass",
  "aliases": [],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q20829075"
   ]
  },
  "revision_id": "2558752535",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q629206",
  "label": "computer language",
  "description": "formal language used in communication with a computer",
  "aliases": [
   "computing language"
  ],
  "claims": {
   "P31": [
    "Q20829075"
   ],
   "P279": [
    "Q192161",
    "Q15621286",
    "Q235557",
    "Q3247505",
    "Q1371819"
   ],
   "P1889": [
    "Q9143",
    "Q1122600"
   ]
  },
  "revision_id": "2563920475",
  "ancestor_of": "Q251",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1058914",
  "label": "software company",
  "description": "company that develops software",
  "aliases": [
   "software development company",
   "software house",
   "computer software company",
   "tech company",
   "software enterprise",
   "tech enterprise"
  ],
  "claims": {
   "P279": [
    "Q4830453",
    "Q783794",
    "Q18388277"
   ],
   "P527": [
    "Q183888"
   ]
  },
  "revision_id": "2566455962",
  "ancestor_of": "Q14647",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q891723",
  "label": "public company",
  "description": "company that offers its securities for sale to the general public",
  "aliases": [
   "publicly traded company",
   "publicly held company",
   "listed company",
   "publicly listed company",
   "public corporation"
  ],
  "claims": {
   "P31": [
    "Q10541491",
    "Q17197366"
   ],
   "P279": [
    "Q6881511",
    "Q134161"
   ],
   "P1889": [
    "Q17990971",
    "Q4539",
    "Q7257717",
    "Q327333"
   ]
  },
  "revision_id": "2532581830",
  "ancestor_of": "Q14647",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4830453",
  "label": "business",
  "description": "organization undertaking commercial, industrial, or professional activity",
  "aliases": [
   "businesses"
  ],
  "claims": {
   "P31": [
    "Q2135465",
    "Q1047113",
    "Q17197366"
   ],
   "P279": [
    "Q43229",
    "Q155076"
   ],
   "P527": [
    "Q6881511",
    "Q8187769",
    "Q3477367",
    "Q636109",
    "Q165687"
   ],
   "P460": [
    "Q21980538",
    "Q6881511",
    "Q783794"
   ],
   "P1889": [
    "Q19862406",
    "Q419342",
    "Q11418769",
    "Q1489930",
    "Q783794"
   ]
  },
  "revision_id": "2569461997",
  "ancestor_of": "Q14647",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110080207",
  "label": "academic spin-off",
  "description": "concept in innovation management and term to describe a spin-off related to academic institution",
  "aliases": [
   "scientific spin-off",
   "academic spin-off company",
   "science spin-off company"
  ],
  "claims": {
   "P31": [
    "Q1969448",
    "Q151885"
   ],
   "P279": [
    "Q129238",
    "Q7896797"
   ]
  },
  "revision_id": "2514941390",
  "ancestor_of": "Q14647",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q783794",
  "label": "company",
  "description": "legal entity representing an association of people, whether natural, legal or a mixture of both, with a specific objective",
  "aliases": [
   "firm",
   "co."
  ],
  "claims": {
   "P31": [
    "Q17197366",
    "Q10541491"
   ],
   "P279": [
    "Q3778211",
    "Q21980538",
    "Q43229"
   ],
   "P527": [
    "Q2366457"
   ],
   "P460": [
    "Q4830453"
   ],
   "P1889": [
    "Q19862406",
    "Q4830453",
    "Q6881511"
   ]
  },
  "revision_id": "2567109551",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q18388277",
  "label": "technology company",
  "description": "company specializing in technology",
  "aliases": [
   "tech company",
   "IT company",
   "IT firm"
  ],
  "claims": {
   "P279": [
    "Q6881511"
   ]
  },
  "revision_id": "2505060809",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q10541491",
  "label": "legal form",
  "description": "type of legal entity within certain legal system",
  "aliases": [],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q141403457"
   ],
   "P1889": [
    "Q1938208"
   ]
  },
  "revision_id": "2561066038",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17197366",
  "label": "type of organization",
  "description": "form of social organization defined by the structure of the relationship between its members, or between other organizations",
  "aliases": [
   "type of an organization",
   "org type",
   "type of organisation"
  ],
  "claims": {
   "P31": [
    "Q24017414",
    "Q151885"
   ],
   "P279": [
    "Q96251598"
   ]
  },
  "revision_id": "2568747981",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q6881511",
  "label": "enterprise",
  "description": "organizational unit producing goods or services, which benefits from a certain degree of autonomy in decision-making, especially for the allocation of its current resources",
  "aliases": [
   "company",
   "firm",
   "undertaking",
   "business enterprise",
   "enterprises",
   "companies",
   "firms",
   "undertakings",
   "business enterprises",
   "enterprise company",
   "enterprise firm"
  ],
  "claims": {
   "P31": [
    "Q3409269"
   ],
   "P279": [
    "Q4830453",
    "Q783794"
   ],
   "P460": [
    "Q4830453"
   ],
   "P1889": [
    "Q1125649",
    "Q19862406",
    "Q218846",
    "Q783794"
   ]
  },
  "revision_id": "2572957753",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q134161",
  "label": "joint-stock company",
  "description": "business entity which is owned by shareholders",
  "aliases": [
   "stock company",
   "stock corporation",
   "joint-stock corporation",
   "JSC"
  ],
  "claims": {
   "P31": [
    "Q1269299"
   ],
   "P279": [
    "Q33685"
   ],
   "P460": [
    "Q166280"
   ],
   "P1889": [
    "Q1480166"
   ]
  },
  "revision_id": "2570176600",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2135465",
  "label": "legal term or legal concept",
  "description": "lexeme with a specific meaning in jurisprudence",
  "aliases": [
   "legal notion",
   "legal concepts",
   "legal notions",
   "legal terms",
   "law term",
   "legalese",
   "liole",
   "legal concept",
   "legal term"
  ],
  "claims": {
   "P31": [
    "Q137429456"
   ],
   "P279": [
    "Q151885",
    "Q1969448"
   ],
   "P361": [
    "Q382995",
    "Q4932206",
    "Q1713997"
   ],
   "P1889": [
    "Q1713997"
   ]
  },
  "revision_id": "2568301846",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1047113",
  "label": "field of study",
  "description": "field limited to a specific area of ​​knowledge; specialization in an occupation or branch of learning; a specific use",
  "aliases": [
   "subject area",
   "domain",
   "special field",
   "specialism",
   "subdiscipline",
   "sub-discipline",
   "specialized field of study",
   "specialty",
   "special branches"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q105948247",
    "Q110403031",
    "Q26256810",
    "Q21040055"
   ],
   "P361": [
    "Q9081"
   ],
   "P1889": [
    "Q123286730",
    "Q2267705"
   ]
  },
  "revision_id": "2562271253",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q43229",
  "label": "organization",
  "description": "social entity established to meet needs or pursue goals",
  "aliases": [
   "organisation",
   "organizations",
   "organisations",
   "institution"
  ],
  "claims": {
   "P31": [
    "Q134602570",
    "Q151885",
    "Q96116695"
   ],
   "P279": [
    "Q106559804",
    "Q106668099",
    "Q1639378",
    "Q854457",
    "Q131085629"
   ],
   "P361": [
    "Q16334295",
    "Q24229398"
   ],
   "P527": [
    "Q10756188",
    "Q5",
    "Q105764136"
   ],
   "P1889": [
    "Q36993249",
    "Q2029841",
    "Q106668099",
    "Q13226383",
    "Q10387680",
    "Q40397",
    "Q141195772",
    "Q141249139"
   ]
  },
  "revision_id": "2566532090",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1969448",
  "label": "term",
  "description": "word, compound word, or expression that in specific contexts is given specific meanings",
  "aliases": [
   "broad term"
  ],
  "claims": {
   "P279": [
    "Q48937186",
    "Q3695082"
   ],
   "P361": [
    "Q1391494"
   ],
   "P1889": [
    "Q12812139",
    "Q151885"
   ]
  },
  "revision_id": "2572498855",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q151885",
  "label": "concept",
  "description": "semantic unit understood in different ways, e.g. as mental representation, ability or abstract object (philosophy)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q7048977",
    "Q15916540",
    "Q2145290",
    "Q1347367",
    "Q141756718"
   ],
   "P460": [
    "Q131841",
    "Q595523",
    "Q1923256",
    "Q25540110"
   ],
   "P1889": [
    "Q1969448",
    "Q595523",
    "Q17087406",
    "Q142226904"
   ]
  },
  "revision_id": "2572760103",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q129238",
  "label": "startup company",
  "description": "company initiated by an entrepreneur to develop a scalable economic model",
  "aliases": [
   "startup",
   "start-up",
   "startups",
   "start-ups",
   "Startuptale",
   "start up firm",
   "start up company",
   "start-up company",
   "start up firms"
  ],
  "claims": {
   "P31": [
    "Q11541386"
   ],
   "P279": [
    "Q4830453",
    "Q783794"
   ],
   "P460": [
    "Q16181358"
   ]
  },
  "revision_id": "2565526911",
  "ancestor_of": "Q14647",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-06913829-n",
  "lemmas": [
   "Java"
  ],
  "gloss": "a platform-independent object-oriented programming language",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06913460-n"
   ]
  },
  "relation_targets": {
   "oewn-06913460-n": "object-oriented programming language, object-oriented programing language"
  }
 },
 {
  "synset": "oewn-07945759-n",
  "lemmas": [
   "coffee",
   "java"
  ],
  "gloss": "a beverage consisting of an infusion of ground coffee beans",
  "examples": [
   "he ordered a cup of coffee"
  ],
  "relations": {
   "hypernym": [
    "oewn-07897775-n"
   ],
   "hyponym": [
    "oewn-07747098-n",
    "oewn-07935681-n",
    "oewn-07935812-n",
    "oewn-07935905-n",
    "oewn-07936027-n",
    "oewn-07936134-n",
    "oewn-07936292-n",
    "oewn-07936589-n",
    "oewn-07936780-n",
    "oewn-07936903-n",
    "oewn-07937112-n",
    "oewn-07937479-n",
    "oewn-07946180-n",
    "oewn-92413955-n"
   ]
  },
  "relation_targets": {
   "oewn-07897775-n": "beverage, drink, drinkable",
   "oewn-07747098-n": "coffee substitute",
   "oewn-07935681-n": "Irish coffee",
   "oewn-07935812-n": "cafe au lait",
   "oewn-07935905-n": "cafe noir, demitasse",
   "oewn-07936027-n": "decaffeinated coffee, decaf",
   "oewn-07936134-n": "drip coffee",
   "oewn-07936292-n": "espresso",
   "oewn-07936589-n": "cappuccino, cappuccino coffee, coffee cappuccino",
   "oewn-07936780-n": "iced coffee, ice coffee",
   "oewn-07936903-n": "instant coffee",
   "oewn-07937112-n": "mocha, mocha coffee",
   "oewn-07937479-n": "Turkish coffee",
   "oewn-07946180-n": "cafe royale, coffee royal",
   "oewn-92413955-n": "Vienna coffee"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 2: JavaScript (`h60l8olauw`)

~~~~text
Concept record:
{
 "id": "h60l8olauw",
 "preferred_name": "JavaScript",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Javascript (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "xuaqr3xw13",
  "name": "ABC JavaScript Renderer"
 },
 {
  "id": "uflky7mun1",
  "name": "JavaScript engine"
 },
 {
  "id": "btu0ssr6y6",
  "name": "JavaScriptCore"
 },
 {
  "id": "xg6thfg29w",
  "name": "JScript"
 },
 {
  "id": "ff38barlkn",
  "name": "NativeScript"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "ayuiek7so7",
  "name": "ActionScript"
 },
 {
  "id": "x4397709dt",
  "name": "CSS"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "k5f5yj60ou",
  "name": "Ajax"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "jvqv4lupvf",
  "name": "ECMAScript 2015"
 },
 {
  "id": "gcx7x5tes5",
  "name": "LiveScript"
 },
 {
  "id": "y37j4kl3jo",
  "name": "TypeScript"
 },
 {
  "id": "ty7glckkcx",
  "name": "PostScript"
 },
 {
  "id": "nnn6b9rv8c",
  "name": "PureScript"
 },
 {
  "id": "xiiyhhzd8l",
  "name": "ABAP"
 },
 {
  "id": "vp6szkok86",
  "name": "Dart"
 },
 {
  "id": "pjhm4fma0a",
  "name": "Scratch"
 },
 {
  "id": "haj4l71a2q",
  "name": "PARI/GP"
 },
 {
  "id": "piarz4pc6x",
  "name": "CoffeeScript"
 },
 {
  "id": "p1pplzvq0f",
  "name": "Swift"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "pkld3bgf9n",
  "name": "Prototype JavaScript Framework"
 },
 {
  "id": "jkc0zoht0i",
  "name": "WinJS"
 },
 {
  "id": "x80b957frq",
  "name": "Ada"
 },
 {
  "id": "d7zsm83o61",
  "name": "SAS"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:12",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Tech Lead Full-Stack Rails Engineer. software development|api|css|docker|elasticsearch|fullstack|html|javascript|kubernetes|postgresql|react|ror|ruby/rails|ai/ml|cad|advertising|redis|es6|web applications|mysql|nlp|fintech|micro services|github|system architecture|communication|excel|java|sql|git|llm|ai|go|ml"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:37",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "…3 و Processors هایی مانند LESS یا SASSتسلط به Responsive Designبینش Mobile-Firstبینش Data-Drivenدانش عميق و تجربه کافی نسبت به TypeScript و Javascript و ES6/ES7تسلط عمیق به React و Context API و Hooks API و Redux و Axios و Rematchتجربه‌ی کار با ابزارهای Automation و Task Runner همچون Vite و Webpack …"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:84",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: .NET Development Engineer Biết Tiếng Trung. [\".Net\", \"JavaScript\", \"jQuery\", \"SQL\", \"Tiếng Trung\"]"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:6",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Junior WordPress Developer. PHP,HTML,CSS,JavaScript,"
 },
 {
  "id": "dev122/internshala-jobs-dataset@v1/JobData.csv:5",
  "source": "kaggle:dev122/internshala-jobs-dataset (CC0: Public Domain), column Description",
  "text": "Job title: Website Operation Intern. …Work on testing to go-live 6. Onboard new clients and manage existing clients 7. Work closely with the design, development, and sales team. JavaScript , WordPress"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "JavaScript",
  "revision_id": "1378180047",
  "matched_by": "title",
  "text": "JavaScript (JS) is a programming language and core technology of the Web, alongside HTML and CSS. Created by Brendan Eich in 1995, it is maintained by Ecma International's TC39 technical committee, with related Web APIs maintained by W3C and WHATWG. As of 2025, JavaScript is the most widely used programming language on GitHub. However, TypeScript, which is a version of JavaScript that is strict about types and is statically typed, overtook JavaScript on GitHub by August 2025. \n\nWeb browsers have a dedicated JavaScript engine that executes the client code. These engines are also utilized in some servers and a variety of apps. The most popular runtime system for non-browser usage is Node.js.\n\nJavaScript is a high-level, often just-in-time–compiled language that conforms to the ECMAScript standard. It has dynamic typing, prototype-based object-orientation, and first-class functions. It is multi-paradigm, supporting event-driven, functional, and imperative programming styles. It has application programming interfaces (APIs) for working with text, dates, regular expressions, standard data structures, and the Document Object Model (DOM).\n\nThe ECMAScript standard does not include any input/output (I/O), such as networking, storage, or graphics facilities. In practice, the web browser or other runtime system provides JavaScript APIs for I/O.\n\nAlthough Java and JavaScript are similar in name and syntax, the two languages are distinct and differ greatly in design.\n\nHistory\n\nCreation at Netscape\n\nThe first popular web browser with a graphical user interface, Mosaic, was released in 1993. The lead developers of Mosaic then founded the Netscape corporation, which released a more polished browser, Netscape Navigator, in 1994. This quickly became the most-used.\n\nDuring these formative years of the Web, web pages could only be static, lacking the capability for dynamic behavior after the page was loaded in the browser. There was a desire in the flourishing web development scene to remove this limitation, so in 1995, Netscape decided to add a programming language to Navigator. They pursued two routes to achieve this: collaborating with Sun Microsystems to embed the Java language, while also hiring Brendan Eich to embed the Scheme language.\n\nThe goal was a \"language for the masses\", \"to help nonprogrammers create dynamic, interactive Web sites\". Netscape management soon decided that the best option was for Eich to devise a new language, with syntax similar to Java and less like Scheme or other extant scripting languages. Although the new language and its interpreter implementation were called LiveScript when first shipped as part of a Navigator beta in September 1995, the name was changed to JavaScript for the official release in December.\n\nThe choice of the JavaScript name has caused confusion, implying that it is directly related to Java. At the time, the dot-com boom had begun and Java was a popular new language, so Eich considered the JavaScript name a marketing ploy by Netscape.\n\nAdoption by Microsoft\n\nMicrosoft debuted Internet Explorer in 1995, leading to a browser war with Netscape. On the JavaScript front, Microsoft created its own interpreter called JScript.\n\nMicrosoft first released JScript in 1996, alongside initial support for CSS and extensions to HTML. Each of these implementations was noticeably different from their counterparts in Netscape Navigator. These differences made it difficult for developers to make their websites work well in both browsers, leading to widespread use of \"best viewed in Netscape\" and \"best viewed in Internet Explorer\" logos for several years.\n\nThe rise of JScript\n\nBrendan Eich later said of this period: \"It's still kind of a sidekick language. It's considered slow or annoying. People do pop-ups or those scrolling messages in the old status bar at the bottom of your old browser.\"\n\nIn November 1996, Netscape submitted JavaScript to Ecma International, as the starting point for a standard specification that all browser vendors could conform to. This led to the official release of the first ECMAScript language specification in June 1997.\n\nThe standards process continued for a few years, with the release of ECMAScript 2 in June 1998 and ECMAScript 3 in December 1999. Work on ECMAScript 4 began in 2000.\n\nHowever, the effort to fully standardize the language was undermined by Microsoft gaining an increasingly dominant position in the browser market. By the early 2000s, Internet Explorer's market share reached 95%. This meant that JScript became the de facto standard for client-side scripting on the Web.\n\nMicrosoft initially participated in the standards process and implemented some proposals in its JScript language, but eventually it stopped collaborating on ECMA work. Thus ECMAScript 4 was mothballed.\n\nGrowth and standardization\n\nDuring the period of Internet Explorer dominance in the early 2000s, client-side scripting was stagnant. This started to change in 2004, when the successor of Netscape, Mozilla, released the Firefox browser. Firefox was well received by many, taking significant market share from Internet Explorer.\n\nIn 2005, Mozilla joined ECMA International, and work started on the ECMAScript for XML (E4X) standard. This led to Mozilla working jointly with Macromedia (later acquired by Adobe Systems), who were implementing E4X in their ActionScript 3 language, which was based on an ECMAScript 4 draft. The goal became standardizing ActionScript 3 as the new ECMAScript 4. To this end, Adobe Systems released the Tamarin implementation as an open source project. However, Tamarin and ActionScript 3 were too different from established client-side scripting, and without cooperation from Microsoft, ECMAScript 4 never reached fruition.\n\nMeanwhile, very important developments were occurring in open-source communities not affiliated with ECMA work. In 2005, Jesse James Garrett released a white paper in which he coined the term Ajax and described a set of technologies, of which JavaScript was the backbone, to create web applications where data can be loaded in the background, avoiding the need for full page reloads. This sparked a renaissance period of JavaScript, spearheaded by open-source libraries and the communities that formed around them. Many new libraries were created, including jQuery, Prototype, Dojo Toolkit, and MooTools.\n\nGoogle debuted its Chrome browser in 2008, with the V8 JavaScript engine that was faster than its competition. The key innovation was just-in-time compilation (JIT), so other browser vendors needed to overhaul their engines for JIT.\n\nIn July 2008, these disparate parties came together for a conference in Oslo. This led to the eventual agreement in early 2009 to combine all relevant work and drive the language forward. The result was the ECMAScript 5 standard, released in December 2009.\n\nReaching maturity\n\nAmbitious work on the language continued for several years, culminating in an extensive collection of additions and refinements being formalized with the publication of ECMAScript 6 in 2015.\n\nThe creation of Node.js in 2009 by Ryan Dahl sparked a significant increase in the usage of JavaScript outside of web browsers. Node combines the V8 engine, an event loop, and I/O APIs, thereby providing a stand-alone JavaScript runtime system. As of 2018, Node had been used by millions of developers, and npm had the most modules of any package manager in the world.\n\nThe ECMAScript draft specification is currently maintained openly on GitHub, and editions are produced via regular annual snapshots. Potential revisions to the language are vetted through a comprehensive proposal process. Now, instead of edition numbers, developers check the status of upcoming features individually.\n\nThe current JavaScript ecosystem has many libraries and frameworks, established programming practices, and substantial usage of JavaScript outside of web browsers. Plus, with the rise of single-page applications and other JavaScript-heavy websites, several transpilers have been created to aid the development process.\n\nAs of 2025, the overwhelming majority of websites (98.9%) use JavaScript for client side webpage behavior.\n\nTrademark\n\n\"JavaScript\" is a trademark of Oracle Corporation in the United States. The trademark was originally issued to Sun Microsystems on 6 May 1997, and was transferred to Oracle when they acquired Sun in 2009.\n\nA letter was circulated in September 2024, spearheaded by Ryan Dahl, calling on Oracle to free the JavaScript trademark. Brendan Eich, the original creator of JavaScript, was among the over 14,000 signatories who supported the initiative.\n\nWebsite client-side usage\n\nJavaScript is the dominant client-side scripting language of the Web, with 99% of all websites using it for this purpose. Scripts are embedded in or included from HTML documents and interact with the DOM.\n\nAll major web browsers have a built-in JavaScript engine that executes the code on the user's device.\n\nExamples of scripted behavior\n\nLoading new web page content without reloading the page, via Ajax or a WebSocket. For example, users of social media can send and receive messages without leaving the current page.\n\nWeb page animations, such as fading objects in and out, resizing, and moving them.\n\nPlaying browser games.\n\nControlling the playback of streaming media.\n\nGenerating pop-up ads or alert boxes.\n\nValidating input values of a web form before the data is sent to a web server.\n\nLogging data about the user's behavior then sending it to a server. The website owner can use this data for analytics, ad tracking, and personalization.\n\nRedirecting a user to another page.\n\nStoring and retrieving data on the user's device, via the storage or IndexedDB standards.\n\nLibraries and frameworks\n\nOver 80% of websites use a third-party JavaScript library or web framework as part of their client-side scripting.\n\njQuery is by far the most-used. Other notable ones include Angular, Bootstrap, Lodash, Modernizr, React, Underscore, and Vue. Multiple options can be used in conjunction, such as jQuery and Bootstrap.\n\nHowever, the term \"Vanilla JS\" was coined for websites not using any libraries or frameworks at all, instead relying entirely on standard JavaScript functionality.\n\nOther usage\n\nThe use of JavaScript has expanded beyond its web browser roots. JavaScript engines are now embedded in a variety of other software systems, both for server-side website deployments and non-browser applications.\n\nInitial attempts at promoting server-side JavaScript usage were Netscape Enterprise Server and Microsoft's Internet Information Services, but they were small niches. Server-side usage eventually started to grow in the late 2000s, with the creation of Node.js and other approaches.\n\nElectron, Cordova, React Native, and other application frameworks have been used to create many applications with behavior implemented in JavaScript. Other non-browser applications include Adobe Acrobat support for scripting PDF documents and GNOME Shell extensions written in JavaScript.\n\nOracle used to provide Nashorn, a JavaScript interpreter, as part of their Java Development Kit (JDK) API library along with jjs a command line interpreter as of JDK version 8. It was removed in JDK 15. As a replacement Oracle offered GraalJS which can also be used with the OpenJDK which allows one to create and reference Java objects in JavaScript code and add runtime scripting in JavaScript to applications written in Java.\n\nJavaScript has been used in some embedded systems, usually by leveraging Node.js.\n\nExecution\n\nJavaScript engine\n\nThe first JavaScript engines were interpreters of the source code, but modern engines use just-in-time compilation to improve performance. JavaScript engines are typically developed by web browser vendors, and every major browser includes one. In a browser, the JavaScript engine runs in concert with the rendering engine via the Document Object Model and Web IDL bindings. However, the use of JavaScript engines is not limited to browsers; For example, the V8 engine is a core component of the Node.js runtime system. They are also called ECMAScript engines, after the official name of the specification. With the advent of WebAssembly, some engines can also execute this code in the same sandbox as regular JavaScript code.\n\nRuntime system\n\nA JavaScript engine must be embedded within a runtime system (such as a web browser or a standalone system) to enable scripts to interact with the broader environment. The runtime system includes the necessary APIs for input/output operations, such as networking, storage, and graphics, and provides the ability to import scripts.\n\nJavaScript is a single-threaded language. The runtime processes messages from a queue one at a time, and it calls a function associated with each new message, creating a call stack frame with the function's arguments and local variables. The call stack shrinks and grows based on the function's needs. When the call stack is empty upon function completion, JavaScript proceeds to the next message in the queue. This is called the event loop, described as \"run to completion\" because each message is fully processed before the next message is considered. However, the language's concurrency model describes the event loop as non-blocking: program I/O is performed using events and callback functions. This means, for example, that JavaScript can process a mouse click while waiting for a database query to return information.\n\nThe notable standalone runtimes are Node.js, Deno, and Bun.\n\nFeatures\n\nThe following features are common to all conforming ECMAScript implementations unless explicitly specified otherwise. The number of cited reserved words including keywords is 50–60 and varies depending on the implementation.\n\nImperative and structured\n\nJavaScript supports much of the structured programming syntax from C (e.g., if statements, while loops, switch statements, do while loops, etc.). One partial exception is scoping: originally JavaScript only had function scoping with var; block scoping was added in ECMAScript 2015 with the keywords let and const. Like C, JavaScript makes a distinction between expressions and statements. One syntactic difference from C is automatic semicolon insertion, which allow semicolons (which terminate statements) to be omitted.\n\nWeakly typed\n\nJavaScript is weakly typed, which means certain types are implicitly cast depending on the operation used.\n\nThe binary + operator casts both operands to a string unless both operands are numbers. This is because the addition operator doubles as a concatenation operator\n\nThe binary - operator always casts both operands to a number\n\nBoth unary operators (+, -) always cast the operand to a number. However, + always casts to Number (binary64) while - preserves BigInt (integer)\n\nValues are cast to strings as follows:\n\nStrings are left as-is\n\nNumbers are converted to their string representation\n\nArrays have their elements cast to strings after which they are joined by commas (,)\n\nOther objects are converted to the string [object Object] where Object is the name of the constructor of the object\n\nValues are cast to numbers by casting to strings and then casting the strings to numbers. These processes can be modified by defining toString and valueOf functions on the prototype for string and number casting respectively.\n\nJavaScript has received criticism for the way it implements these conversions as the complexity of the rules can be mistaken for inconsistency. For example, when adding a number to a string, the number will be cast to a string before performing concatenation, but when subtracting a number from a string, the string is cast to a number before performing subtraction.\n\nOften also mentioned is {} + [] resulting in 0 (number). This is misleading: the {} is interpreted as an empty code block instead of an empty object, and the empty array is cast to a number by the remaining unary + operator. If the expression is wrapped in parentheses - ({} + []) – the curly brackets are interpreted as an empty object and the result of the expression is \"[object Object]\" as expected.\n\nDynamic\n\nTyping\n\nJavaScript is dynamically typed like most other scripting languages. A type is associated with a value rather than an expression. For example, a variable initially bound to a number may be reassigned to a string. JavaScript supports various ways to test the type of objects, including duck typing.\n\nRun-time evaluation\n\nJavaScript includes an eval function that can execute statements provided as strings at run-time.\n\nObject-orientation (prototype-based)\n\nPrototypal inheritance in JavaScript is described by Douglas Crockford as:\n\nYou make prototype objects, and then ... make new instances. Objects are mutable in JavaScript, so we can augment the new instances, giving them new fields and methods. These can then act as prototypes for even newer objects. We don't need classes to make lots of similar objects... Objects inherit from objects. What could be more object oriented than that?\n\nIn JavaScript, an object is an associative array, augmented with a prototype (see below); each key provides the name for an object property, and there are two syntactical ways to specify such a name: dot notation (obj.x = 10) and bracket notation (obj[\"x\"] = 10). A property may be added, rebound, or deleted at run-time. Most properties of an object (and any property that belongs to an object's prototype inheritance chain) can be enumerated using a for...in loop.\n\nPrototypes\n\nJavaScript uses prototypes where many other object-oriented languages use classes for inheritance, but it's still possible to simulate most class-based features with the prototype system. Additionally, ECMAScript version 6 (released June 2015) introduced the keywords class, extends and super, which serve as syntactic sugar to abstract the underlying prototypal inheritance system with a more conventional interface. Constructors are declared by specifying a method named constructor, and all classes are automatically subclasses of the base class Object, similarly to Java. class Person {\n constructor(name) {\n this.name = name;\n }\n}\n\nclass Student extends Person {\n constructor(name, id) {\n super(name);\n this.id = id;\n }\n}\n\nconst bob = new Student(\"Robert\", 12345);\nconsole.log(bob.name); // Robert\n\nThough the underlying object mechanism is still based on prototypes, the newer syntax is similar to other object oriented languages. Private variables are declared by prefixing the field name with a number sign (#), and polymorphism is not directly supported, although it can be emulated by manually calling different functions depending on the number and type of arguments provided.\nFunctions as object constructors\n\nFunctions double as object constructors, along with their typical role. Prefixing a function call with new will create an instance of a prototype, inheriting properties and methods from the constructor (including properties from the Object prototype). ECMAScript 5 offers the Object.create method, allowing explicit creation of an instance without automatically inheriting from the Object prototype (older environments can assign the prototype to null). The constructor's prototype property determines the object used for the new object's internal prototype. New methods can be added by modifying the prototype of the function used as a constructor.// This code is completely equivalent to the previous snippet\nfunction Person(name) {\n this.name = name;\n}\n\nfunction Student(name, id) {\n Person.call(this, name);\n this.id = id;\n}\n\nvar bob = new Student(\"Robert\", 12345);\nconsole.log(bob.name); // Robert\n\nJavaScript's built-in classes, such as Array and Object, also have prototypes that can be modified. However, it's generally considered bad practice to modify built-in objects, because third-party code may use or inherit methods and properties from these objects, and may not expect the prototype to be modified.\nFunctions as methods\n\nUnlike in many object-oriented languages, in JavaScript there is no distinction between a function definition and a method definition. Rather, the distinction occurs during function calling. When a function is called as a method of an object, the function's local this keyword is bound to that object for that invocation.\n\nFunctional\n\nJavaScript functions are first-class; a function"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q2005",
  "label": "JavaScript",
  "description": "high-level programming language",
  "aliases": [],
  "claims": {
   "P31": [
    "Q187432",
    "Q28920810",
    "Q21562092",
    "Q3839507",
    "Q28920813",
    "Q241317",
    "Q1993334",
    "Q12772052",
    "Q9143",
    "Q28923017",
    "Q211496",
    "Q180868",
    "Q1051282",
    "Q193076",
    "Q275596",
    "Q30267",
    "Q1135914"
   ],
   "P279": [
    "Q28922885"
   ],
   "P460": [
    "Q553514"
   ],
   "P1889": [
    "Q259138",
    "Q5924007",
    "Q251",
    "Q16963446",
    "Q879704",
    "Q137396574"
   ]
  },
  "revision_id": "2566877768",
  "value_labels": {
   "Q187432": "scripting language",
   "Q28920810": "prototype-based programming language",
   "Q21562092": "imperative programming language",
   "Q3839507": "functional programming language",
   "Q28920813": "event-driven programming language",
   "Q241317": "computing platform",
   "Q1993334": "interpreted language",
   "Q12772052": "multi-paradigm programming language",
   "Q9143": "programming language",
   "Q28923017": "strict programming language",
   "Q211496": "high-level programming language",
   "Q180868": "prototype-based programming",
   "Q1051282": "generic programming",
   "Q193076": "functional programming",
   "Q275596": "imperative programming",
   "Q30267": "aspect-oriented programming",
   "Q1135914": "event-driven programming",
   "Q28922885": "procedural programming language",
   "Q553514": "JScript",
   "Q259138": "ECMAScript",
   "Q5924007": "JavaScript format",
   "Q251": "Java",
   "Q16963446": "LiveScript",
   "Q879704": "Javanese script",
   "Q137396574": "Głównie JavaScript"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q187432",
  "label": "scripting language",
  "description": "programming language for run-time events",
  "aliases": [
   "script language",
   "extension language",
   "embedded language",
   "embeddable language",
   "glue language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2561823546",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28920810",
  "label": "prototype-based programming language",
  "description": "programming language",
  "aliases": [],
  "claims": {
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2362182527",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21562092",
  "label": "imperative programming language",
  "description": "programming language implementing the imperative programming paradigm",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2552001049",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3839507",
  "label": "functional programming language",
  "description": "programming language that uses functional programming principles",
  "aliases": [
   "functional language",
   "functional languages"
  ],
  "claims": {
   "P31": [
    "Q116481801",
    "Q11862829",
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2547798441",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28920813",
  "label": "event-driven programming language",
  "description": "kind of programming language",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2362182530",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q241317",
  "label": "computing platform",
  "description": "environment in which a piece of software is executed",
  "aliases": [
   "platform",
   "digital platform",
   "computing environment",
   "app layer",
   "execution environment"
  ],
  "claims": {
   "P279": [
    "Q2424752",
    "Q994895"
   ]
  },
  "revision_id": "2552001373",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1993334",
  "label": "interpreted language",
  "description": "programming language for which most of its implementations execute instructions directly",
  "aliases": [
   "interpreted programming language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2517136679",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12772052",
  "label": "multi-paradigm programming language",
  "description": "programming language type",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2552000821",
  "ancestor_of": "Q2005",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116481801",
  "label": "type of programming language",
  "description": "Wikidata metaclass",
  "aliases": [
   "kind of programming language",
   "programming language type",
   "programming language category",
   "category of programming languages"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257",
    "Q137527772"
   ]
  },
  "revision_id": "2555835128",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9143",
  "label": "programming language",
  "description": "language for communicating instructions to a machine",
  "aliases": [
   "computer language",
   "computer programming language",
   "coding language",
   "computer programming"
  ],
  "claims": {
   "P31": [
    "Q66747126",
    "Q137527772"
   ],
   "P279": [
    "Q629206"
   ],
   "P361": [
    "Q68"
   ],
   "P527": [
    "Q1152399",
    "Q25346349",
    "Q1199356",
    "Q865760"
   ],
   "P1889": [
    "Q4117406",
    "Q173341",
    "Q189224",
    "Q629206",
    "Q77654221"
   ]
  },
  "revision_id": "2570899010",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11862829",
  "label": "academic discipline",
  "description": "field of study organized around a distinct body of knowledge, theories, methods, or subject matter",
  "aliases": [
   "branch (academic)",
   "discipline",
   "academic field",
   "academic branch",
   "academic specialty",
   "academic specialism",
   "research field",
   "field of research",
   "field of study",
   "sub-discipline"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q1047113"
   ],
   "P460": [
    "Q2465832",
    "Q2267705",
    "Q627436",
    "Q362165"
   ],
   "P1889": [
    "Q3242580",
    "Q1166828",
    "Q1391009",
    "Q82957"
   ]
  },
  "revision_id": "2562020019",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1047113",
  "label": "field of study",
  "description": "field limited to a specific area of ​​knowledge; specialization in an occupation or branch of learning; a specific use",
  "aliases": [
   "subject area",
   "domain",
   "special field",
   "specialism",
   "subdiscipline",
   "sub-discipline",
   "specialized field of study",
   "specialty",
   "special branches"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q105948247",
    "Q110403031",
    "Q26256810",
    "Q21040055"
   ],
   "P361": [
    "Q9081"
   ],
   "P1889": [
    "Q123286730",
    "Q2267705"
   ]
  },
  "revision_id": "2562271253",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2267705",
  "label": "field of study",
  "description": "field of study leading to a specific degree",
  "aliases": [
   "field of education",
   "area of study"
  ],
  "claims": {
   "P279": [
    "Q1047113"
   ],
   "P527": [
    "Q13442814"
   ],
   "P460": [
    "Q11862829",
    "Q2465832",
    "Q4671286"
   ],
   "P1889": [
    "Q1047113"
   ]
  },
  "revision_id": "2544362366",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2424752",
  "label": "product",
  "description": "anything that can be offered to a market",
  "aliases": [
   "goods",
   "merchandise"
  ],
  "claims": {
   "P31": [
    "Q29028649",
    "Q96251598"
   ],
   "P279": [
    "Q488383"
   ],
   "P460": [
    "Q28877",
    "Q11270824"
   ],
   "P1889": [
    "Q1485500",
    "Q2897903",
    "Q1796457",
    "Q542929"
   ]
  },
  "revision_id": "2562572650",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q994895",
  "label": "technical system",
  "description": "system created through engineering",
  "aliases": [
   "technology system",
   "engineered system",
   "designed system",
   "artificial system",
   "manmade system"
  ],
  "claims": {
   "P31": [
    "Q96116695"
   ],
   "P279": [
    "Q2424752",
    "Q58778",
    "Q16686448"
   ],
   "P527": [
    "Q811909",
    "Q110558466"
   ],
   "P1889": [
    "Q26839523"
   ]
  },
  "revision_id": "2565080467",
  "ancestor_of": "Q2005",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
