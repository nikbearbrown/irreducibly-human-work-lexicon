# Irreducibly Human Work Lexicon pilot, grounded run: message 7 of 13 (chunk 06, 2 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "06", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-06.jsonl`. Otherwise send one code block marked `jsonl` holding the 2 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 2: Swift (`p1pplzvq0f`)

~~~~text
Concept record:
{
 "id": "p1pplzvq0f",
 "preferred_name": "Swift",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Swift3"
  },
  {
   "label": "Swift (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "wroqa3tbb6",
  "name": "SWIFT network"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "e0p0dbx59q",
  "name": "Rust"
 },
 {
  "id": "php2tc9p7y",
  "name": "XML"
 },
 {
  "id": "v17l7v4fgv",
  "name": "Administrative"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "oramfb6to9",
  "name": "Correspondent banking"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "xg6thfg29w",
  "name": "JScript"
 },
 {
  "id": "r9tfnc7x3j",
  "name": "CLIST"
 },
 {
  "id": "jzczt8njk2",
  "name": "Forth"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
 },
 {
  "id": "sc1h6sf9t5",
  "name": "Nim"
 },
 {
  "id": "f69xny35zm",
  "name": "SQL"
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
  "id": "qou8ag13js",
  "name": "Simula"
 },
 {
  "id": "kcu5dpjinp",
  "name": "Eiffel"
 },
 {
  "id": "ipwny15jpy",
  "name": "Fantom"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:2337",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Android Developer. [\"Swift\", \"HTML5\", \"Android Development\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:9",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "IOS, Git, Swift, Objective-C"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:714",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Developer Relations Lead. …tware, platform, infrastructure, or developer-tools engineer on production systems. Strong software engineering skills in Python, Go, Rust, Swift, or a similar language. Deep knowledge of macOS and Apple Silicon. You understand processes, services, permissions, code signing, system security, network…"
 },
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:532",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Developer. PDF, Web technologies, XML, Analytical, OOPS, Design development, JSON, Swift"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "SWIFT",
  "revision_id": "1376973213",
  "matched_by": "title",
  "text": "The Society for Worldwide Interbank Financial Telecommunication (SWIFT), legally S.W.I.F.T. SC, is a cooperative established in 1973 in Belgium (French: Société Coopérative) and owned by the banks and other member firms that use its service. SWIFT provides the main messaging network through which international payments are initiated. It also sells software and services to financial institutions, mostly for use on its proprietary \"SWIFTNet\", and assigns ISO 9362 Business Identifier Codes (BICs), popularly known as \"SWIFT codes\".\n\nAs of 2018, around half of all high-value cross-border payments worldwide used the SWIFT network, and in 2015, SWIFT linked more than 11,000 financial institutions in over 200 countries and territories, who were exchanging an average of over 32 million messages per day (compared to an average of 2.4 million daily messages in 1995).\n\nSWIFT is headquartered in La Hulpe near Brussels. It hosts an annual conference, called Sibos, specifically aimed at the financial services industry.\n\nHistory\n\nBefore SWIFT's establishment, international financial transactions were communicated over Telex, a public system involving manual writing and reading of messages. The collapse of the Bretton Woods agreement in 1971, the decoupling of the US dollar's convertibility to gold, a period in economic history now known as the \"Nixon shock\", shifted major currencies to floating exchange rates and increased the volume of cross-border transactions. That in addition to already increasing amounts of international trade made the existing Telex system insufficient. In this novel period of international trade in a floating exchange rate environment, SWIFT was set up out of fear of what might happen if a single private and fully American entity controlled global financial flows – which before was First National City Bank (FNCB) of New York – later Citibank. In response to FNCB's protocol, FNCB's competitors in the US and Europe pushed an alternative \"messaging system that could replace the public providers and speed up the payment process\".\n\nSWIFT was founded in Brussels on 3 May 1973. Individuals who played a key role in its creation included bankers Jan Kraa (at AMRO Bank) and François Dentz (at the Banque de l'Union Parisienne) as well as Carl Reuterskiöld and Bessel Kok, who became respectively its first two chairmen and chief executives. It was initially supported by 239 banks in 15 countries. It soon started to establish common standards for financial transactions and a shared data processing system and worldwide communications network designed by Logica and developed by the Burroughs Corporation. Fundamental operating procedures and rules for liability were established in 1975, and the first message was ceremonially sent by Prince Albert of Belgium on 9 May 1977.\n\nSWIFT's first non-European operations centre was inaugurated by Governor John N. Dalton of Virginia in 1979. In 1989 SWIFT completed a monumental new head office building in La Hulpe, designed by Ricardo Bofill Taller de Arquitectura.\n\nOwnership and governance\n\nSWIFT's shareholding structure is adjusted every three years in proportion to volumes of activity incurred by the members, ensuring that the most active members get the most voice irrespective of geography; additional rules are aimed at ensuring some geographical diversity within the board of directors. The 25 directors are elected by the shareholders, on three-year terms with the renewal of one-third of the board every year; all directors are member representatives.\n\nAs of May 2024, the members directly represented on the board of directors were JPMorgan Chase (chair), Lloyds Bank (deputy chair), Bank of China, BNP Paribas, BPCE, Citi, Clearstream, Commerzbank, Commonwealth Bank, Deutsche Bank, Euroclear, FirstRand, HSBC, ING, Intesa Sanpaolo, KBC, MUFG, NatWest, Nordea, Royal Bank of Canada, Santander, SEB, UBS (2 representatives following the acquisition of Credit Suisse), as well as the Association of Banks in Singapore.\n\nOperations\n\nSWIFT acts as a carrier of the \"messages containing the payment instructions between financial institutions involved in a transaction\". However, the organisation does not manage accounts on behalf of individuals or financial institutions, and it does not hold funds from third parties. It also does not perform clearing or settlement functions. After payment has been initiated, it must be settled through a payment system, such as T2 in Europe. In the context of cross-border transactions, this step often takes place through correspondent banking accounts that financial institutions have with each other.\n\nSWIFT means several things in the financial world: \n\na secure network for transmitting messages between financial institutions;\n\na set of syntax standards for financial messages (for transmission over SWIFTNet or any other network)\n\na set of connection software and services allowing financial institutions to transmit messages over SWIFT network.\n\nUnder 3 above, SWIFT provides turn-key solutions for members, consisting of linkage clients to facilitate connectivity to the SWIFT network and CBTs or \"computer-based terminals\" which members use to manage the delivery and receipt of their messages. Some of the more well-known interfaces and CBTs provided to their members are:\n\nSWIFTNet Link (SNL) software which is installed on the SWIFT customer's site and opens a connection to SWIFTNet. Other applications can only communicate with SWIFTNet through the SNL.\n\nAlliance Gateway (SAG) software with interfaces (e.g., RAHA = Remote Access Host Adapter), allowing other software products to use the SNL to connect to SWIFTNet\n\nAlliance WebStation (SAB) desktop interface for SWIFT Alliance Gateway with several usage options:\n\nadministrative access to the SAG\n\ndirect connection SWIFTNet by the SAG, to administrate SWIFT Certificates\n\nso-called Browse connection to SWIFTNet (also by SAG) to use additional services, for example, the Eurosystem's T2\n\nAlliance Access (SAA) and Alliance Messaging Hub (AMH) are the main messaging software applications by SWIFT, which allow message creation for FIN messages, routing and monitoring for FIN and MX messages. The main interfaces are FTA (files transfer automated, not FTP) and MQSA, a WebSphere MQ interface.\n\nThe Alliance Workstation (SAW) is the desktop software for administration, monitoring and FIN message creation. Since Alliance Access is not yet capable of creating MX messages, Alliance Messenger (SAM) has to be used for this purpose.\n\nAlliance Web Platform (SWP) as new thin-client desktop interface provided as an alternative to the existing Alliance WebStation, Alliance Workstation (soon) and Alliance Messenger.\n\nAlliance Integrator is built on Oracle's Java Caps which enables customer's back-office applications to connect to Alliance Access or Alliance Entry.\n\nAlliance Lite2 is a secure and reliable, cloud-based way to connect to the SWIFT network which is a light version of Alliance Access specifically targeting customers with low volume of traffic.\n\nServices\n\nThere are four key areas that SWIFT services fall under in the financial marketplace: securities, treasury & derivatives, trade services, and payments & cash management.\n\nSWIFT Ref, the global payment reference data utility, is SWIFT's reference data service. SWIFT Ref sources data from central banks, code issuers and banks.\n\nOperations centres\n\nThe SWIFT secure messaging network is run from three data centres, located in the United States, the Netherlands, and Switzerland. These centres share information in near real-time. In case of a failure in one of the data centres, another is able to handle the traffic of the complete network. SWIFT uses submarine communications cables to transmit its data.\n\nShortly after opening its third data centre in Switzerland in 2009, SWIFT introduced a new distributed architecture with two messaging zones, European and Trans-Atlantic, so data from European SWIFT members no longer mirrored the US data centre. European zone messages are stored in the Netherlands and in part of the Swiss operating centre; Trans-Atlantic zone messages are stored in the United States and in another part of the Swiss operating centre that is segregated from the European zone messages. Countries outside of Europe were by default allocated to the Trans-Atlantic zone but could choose to have their messages stored in the European zone.\n\nSWIFTNet network\n\nSWIFT moved to its current IP network infrastructure, known as SWIFTNet, from 2001 to 2005, providing a total replacement of the previous X.25 infrastructure. The process involved the development of new protocols that facilitate efficient messaging, using existing and new message standards. The adopted technology chosen to develop the protocols was XML, which now provides a wrapper around all messages legacy or contemporary. The communication protocols can be broken down into:\n\nSWIFT provides a centralized store-and-forward mechanism, with some transaction management. For bank A to send a message to bank B with a copy or authorization involving institution C, it formats the message according to standards and securely sends it to SWIFT. SWIFT guarantees its secure and reliable delivery to B after the appropriate action by C. SWIFT guarantees are based primarily on high redundancy of hardware, software, and people.\n\nDuring 2007 and 2008, the entire SWIFT network migrated its infrastructure to a new protocol called SWIFTNet Phase 2. The main difference between Phase 2 and the former arrangement is that Phase 2 requires banks connecting to the network to use a Relationship Management Application (RMA) instead of the former bilateral key exchange (BKE) system. According to SWIFT's public information database on the subject, RMA software should eventually prove more secure and easier to keep up-to-date; however, converting to the RMA system meant that thousands of banks around the world had to update their international payment systems to comply with the new standards. RMA completely replaced BKE on 1 January 2009.\n\nStandards\n\nSWIFT has become the industry standard for syntax in financial messages. Messages formatted to SWIFT standards can be read and processed by many well-known financial processing systems, whether or not the message travelled over the SWIFT network. SWIFT cooperates with international organizations to define standards for message format and content. SWIFT is also a registration authority (RA) for the following ISO standards:\n\nISO 9362: 1994 Banking – Banking telecommunication messages – Bank identifier codes\n\nISO 10383: 2003 Securities and related financial instruments – Codes for exchanges and market identification (MIC)\n\nISO 13616: 2003 IBAN Registry\n\nISO 15022: 1999 Securities – Scheme for messages (Data Field Dictionary) (replaces ISO 7775)\n\nISO 20022-1: 2004 and ISO 20022-2:2007 Financial services – Universal Financial Industry message scheme\n\nIn RFC 3615 urn:swift: was defined as Uniform Resource Names (URNs) for SWIFT FIN.\n\nSupervision\n\nSWIFT is not a payment system and thus neither regulated nor supervised as such, but is nevertheless deemed to be systemically important and thus under the \"oversight\" of public authorities. In 1998, the so-called Group of Ten central banks (those of Belgium, Canada, France, Germany, Italy, Japan, the Netherlands, Sweden, Switzerland, the United Kingdom, the Federal Reserve Board and the Federal Reserve Bank of New York for the US and the European Central Bank) started acting as joint overseers, with the National Bank of Belgium (NBB) in a lead role. The oversight focuses primarily on systemic risk, confidentiality, infrastructure security, and business continuity. It is formalized in bilateral documents between the NBB and SWIFT on the one hand, and between the NBB and each of the other G10 central banks on the other hand. In 2018, the International Monetary Fund has recommended that \"the National Bank of Belgium should consider enhancing oversight with additional regulatory and supervisory powers.\"\n\nIn 2012, this framework was complemented by a \"SWIFT Oversight Forum\" including additional central banks. As of 2024, in addition to the G10 central banks, the SWIFT Oversight Forum included the national central banks of Argentina, Australia, Brazil, China, Hong Kong, India, Indonesia, Korea, Mexico, Russia, Saudi Arabia, Singapore, South Africa, Spain, and Turkey. According to SWIFT, the Oversight Forum \"provides a forum for the G-10 central banks to share information on SWIFT oversight activities with a wider group of central banks.\"\n\nAlternatives\n\nCurrent: Purported alternatives to the SWIFT system include:\n\nBRICS Pay: by BRICS member nations\n\nCIPS: sponsored by China, for RMB-related deals. 1467 financial institutions in 111 countries and regions have connected to the system. The actual business covers more than 4,200 banking institutions in 182 countries and regions around the world.\n\nSFMS: sponsored by India\n\nSPFS: developed by the Russian Federation\n\nPix (payment system): developed by Brazil.\n\nFormer\n\nINSTEX: sponsored by the European Union, limited to non-USD transactions for trade with Iran, largely unused and ineffective. Liquidated in March 2023.\n\nLeadership\n\nChair\n\nJohannes Kraa (AMRO Bank, Dutch), 1973–1974\n\nFrançois Dentz (Crédit du Nord, French), 1974–1976\n\nHelmer Hasselblad (Swedish), 1976–1984\n\nW. Robert Moore (Chemical Bank, American), 1984–1989\n\nRichard Fröhlich (Austrian), 1989–1992\n\nEric C. Chilton (Barclays, British), 1992–1996\n\nJean-Marie Weydert (Société Générale, French), 1996–2000\n\nJaap Kamp (ABN AMRO, Dutch), 2000–2006\n\nYawar Shah (JPMorgan then Citi, American), 2006–2022\n\nMark Buitenhek (ING, Dutch), acting 2022–2023\n\nGraeme Munro (JPMorgan, British), since 2023\n\nChief executive officer\n\nCarl Reuterskiöld, 1973–1983\n\nBessel Kok, 1983–1991\n\nJacques Cerveau (interim CEO), 1991\n\nLeonard (Lennie) Schrank, 1992–2007\n\nLazaro Campos, 2007–2012\n\nGottfried Leibbrandt, 2012–2019\n\nJavier Pérez-Tasso, since 2019\n\nControversy\n\nInefficiency\n\nSWIFT has been criticised for inefficiency. In 2018, the London-based Financial Times noted that transfers frequently \"pass through multiple banks before reaching their final destination, making them time-consuming, costly and lacking transparency on how much money will arrive at the other end\". SWIFT has since introduced an improved service called \"Global Payments Innovation\" (GPI), claiming it was adopted by 165 banks and was completing half its payments within 30 minutes. The new standard which included SWIFT Go was supposed to be utilised in receiving and transferring low-value international payments. One of the significant changes was the transaction amount, which would not differ from start to end. However, as of 2023, uptake was mixed. For instance, Alisherov Eraj, Alif Bank Treasury Department SWIFT Transfers & Banking Relationship Expert in the Republic of Tajikistan, describes that the leading cause for the late SWIFT Go adoption in Tajikistan was the Core Banking System itself. To connect to SWIFT Go, he adds, banking system interfaces needed to be upgraded and integrated with their software to be fully compatible; this hindered many banks from adopting the technology earlier.\n\nUS government surveillance\n\nA series of articles published on 23 June 2006 in The New York Times, The Wall Street Journal, and the Los Angeles Times revealed a program, named the Terrorist Finance Tracking Program, which the US Treasury Department, Central Intelligence Agency (CIA), and other United States governmental agencies initiated after the 11 September attacks to gain access to the SWIFT transaction database.\n\nAfter the publication of these articles, SWIFT quickly came under pressure for compromising the data privacy of its customers by allowing governments to gain access to sensitive personal information. In September 2006, the Belgian government declared that these SWIFT dealings with American governmental authorities were a breach of Belgian and European privacy laws.\n\nIn response, and to satisfy members' concerns about privacy, SWIFT began a process of improving its architecture by implementing a distributed architecture with a two-zone model for storing messages .\n\nConcurrently, the European Union negotiated an agreement with the United States government to permit the transfer of intra-EU SWIFT transaction information to the United States under certain circumstances. Because of concerns about its potential contents, the European Parliament adopted a position statement in September 2009, demanding to see the full text of the agreement and asking that it be fully compliant with EU privacy legislation, with oversight mechanisms emplaced to ensure that all data requests were handled appropriately. An interim agreement was signed without European Parliamentary approval by the European Council on 30 November 2009, the day before the Lisbon Treaty—which would have prohibited such an agreement from being signed under the terms of the codecision procedure—formally came into effect. While the interim agreement was scheduled to come into effect on 1 January 2010, the text of the agreement was classified as \"EU Restricted\" until translations could be provided in all EU languages and published on 25 January 2010.\n\nOn 11 February 2010, the European Parliament decided to reject the interim agreement between the EU and the US by 378 to 196 votes. One week earlier, the parliament's civil liberties committee had already rejected the deal, citing legal reservations.\n\nIn March 2011, it was reported that two mechanisms of data protection had failed: EUROPOL released a report complaining that requests for information from the US had been too vague (making it impossible to make judgments on validity) and that the guaranteed right for European citizens to know whether their information had been accessed by US authorities had not been put into practice.\n\nDer Spiegel reported in September 2013 that the National Security Agency (NSA) widely monitors banking transactions via SWIFT, as well as credit card transactions. The NSA intercepted and retained data from the SWIFT network used by thousands of banks to securely send transaction information. SWIFT was named as a \"target\", according to documents leaked by Edward Snowden. The documents revealed that the NSA spied on SWIFT using a variety of methods, including reading \"SWIFT printer traffic from numerous banks\". In April 2017, a group known as the Shadow Brokers released files allegedly from the NSA which indicate that the agency monitored financial transactions made through SWIFT.\n\nSWIFT and sanctions\nIran\n\nIn January 2012, the advocacy group United Against Nuclear Iran (UANI) implemented a campaign calling on SWIFT to end all relations with Iran's banking system, including the Central Bank of Iran. UANI asserted that Iran's membership in SWIFT violated US and EU financial sanctions against Iran as well as SWIFT's own corporate rules.\n\nConsequently, in February 2012, the US Senate Banking Committee unanimously approved sanctions against SWIFT aimed at pressuring it to terminate its ties with blacklisted Iranian banks. Expelling Iranian banks from SWIFT would potentially deny Iran access to billions of dollars in revenue using SWIFT but not from using IVTS. Mark Wallace, president of UANI, praised the Senate Banking Committee.\n\nInitially SWIFT denied that it was acting illegally, but later said that \"it is working with U.S. and European governments to address their concerns that its financial services are being used by Iran to avoid sanctions and conduct illicit business\". Targeted banks would be—amongst others—Saderat Bank of Iran, Bank Mellat, Post Bank of Iran and Sepah Bank. On 17 March 2012, following an agreement two days earlier between all 27 member states of the Council of the European Union and the council's subsequent ruling, SWIFT disconnected all Iranian banks that had been identified as institutions in breach of current EU sanctions from its international network and warned that even more Iranian financial institutions could be disconnected from the network.\n\nIn February 2016, most Iranian banks reconnected to the network following the lift of sanctions due to the Joint Comprehensive Plan of Action. \n\nIn November 2024, Iran implemented a paradigm shift approach to shift the focus from the SWIFT payment system by initiating the concept of bringing ACUMER. ACUMER was coined by Iran as a retaliation to the international sanctions imposed by the United States which has ever since limited Iran's competitive edge in the context of international trade."
 },
 {
  "title": "Swift (programming language)",
  "revision_id": "1379000016",
  "matched_by": "title",
  "text": "Swift is a high-level general-purpose, multi-paradigm, compiled programming language created by Chris Lattner in 2010 for Apple Inc. and maintained by the open-source community. Swift compiles to machine code and uses an LLVM-based compiler. Swift was first released in June 2014 and the Swift toolchain has shipped in Xcode since Xcode version 6, released in September 2014.\n\nApple intended Swift to support many core concepts associated with Objective-C, notably dynamic dispatch, widespread late binding, extensible programming, and similar features, but in a \"safer\" way, making it easier to catch software bugs; Swift has features addressing some common programming errors like null pointer dereferencing and provides syntactic sugar to help avoid the pyramid of doom. Swift supports the concept of protocol extensibility, an extensibility system that can be applied to types, structs and classes, which Apple promotes as a real change in programming paradigms they term \"protocol-oriented programming\" (similar to traits and type classes).\n\nSwift was introduced at Apple's 2014 Worldwide Developers Conference (WWDC). It underwent an upgrade to version 1.2 during 2014 and a major upgrade to Swift 2 at WWDC 2015. It was initially a proprietary language, but version 2.2 was made open-source software under the Apache License 2.0 on December 3, 2015, for Apple's platforms and Linux.\n\nHistory\n\nDevelopment of Swift started in July 2010 by Chris Lattner, with the eventual collaboration of many other programmers at Apple. Swift was motivated by the need for a replacement for Apple's earlier programming language Objective-C, which had been largely unchanged since the early 1980s and lacked modern language features. Swift took language ideas \"from Objective-C, Rust, Haskell, Ruby, Python, C#, CLU, and far too many others to list\". On June 2, 2014, the Apple Worldwide Developers Conference (WWDC) application became the first publicly released app written with Swift. A beta version of the programming language was released to registered Apple developers at the conference, but the company did not promise that the final version of Swift would be source code compatible with the test version. Apple planned to make source code converters available if needed for the full release.\n\nThe Swift Programming Language, a free 500-page manual, was also released at WWDC, and is available on the Apple Books Store and the official website.\n\nSwift reached the 1.0 milestone on September 9, 2014, with the Gold Master of Xcode 6.0 for iOS. Swift 1.1 was released on October 22, 2014, alongside the launch of Xcode 6.1. Swift 1.2 was released on April 8, 2015, along with Xcode 6.3. Swift 2.0 was announced at WWDC 2015, and was made available for publishing apps in the App Store on September 21, 2015.\n\nSwift 3.0 was released on September 13, 2016. Through version 3.0, the syntax of Swift went through significant evolution, with the core team making source stability a focus in later versions.\n\nSwift 4.0, released on September 19, 2017, introduced several changes to some built-in classes and structures. Code written with previous versions of Swift can be updated using the migration functionality built into Xcode. Swift 4.1 was released on March 29, 2018. In the first quarter of 2018, Swift surpassed Objective-C in measured popularity.\n\nSwift 5, released in March 2019, introduced a stable binary interface on Apple platforms, allowing the Swift runtime to be incorporated into Apple operating systems. It is source compatible with Swift 4.\n\nSwift 5.1 was officially released in September 2019. Swift 5.1 builds on the previous version of Swift 5 by extending the stable features of the language to compile-time with the introduction of module stability. The introduction of module stability makes it possible to create and share binary frameworks that will work with future releases of Swift. Swift 5.5, officially announced by Apple at the 2021 WWDC, significantly expands language support for concurrency and asynchronous code, notably introducing a unique version of the actor model. Swift 5.9, was released in September 2023 and includes a macro system, generic parameter packs, and ownership features like the new consume operator. Swift 5.10, released in March 2024, improves the language's concurrency model, allowing for full data isolation to prevent data races.\n\nSwift 6 was released in September 2024. Swift 6.1 was released in March 2025. It includes \"new language enhancements to improve productivity, diagnostics improvements, package traits, and ongoing work to improve data-race safety usability and compile times.\"\n\nSwift won first place for Most Loved Programming Language in the Stack Overflow Developer Survey 2015 and second place in 2016.\n\nOn December 3, 2015, the Swift language, supporting libraries, debugger, and package manager were open-sourced under the Apache 2.0 license with a Runtime Library Exception, and Swift.org was created to host the project. The source code is hosted on GitHub, where it is easy for anyone to get the code, build it themselves, and even create pull requests to contribute code back to the project.\n\nIn December 2015, IBM announced its Swift Sandbox website, which allows developers to write Swift code in one pane and display output in another. The Swift Sandbox was deprecated in January 2018.\n\nDuring the WWDC 2016, Apple announced an iPad exclusive app, named Swift Playgrounds, intended to teach people how to code in Swift. The app is presented in a 3D video game-like interface which provides feedback when lines of code are placed in a certain order and executed.\n\nIn January 2017, Chris Lattner announced his departure from Apple for a new position with Tesla Motors, with the Swift project lead role going to team veteran Ted Kremenek.\n\nDuring WWDC 2019, Apple announced SwiftUI with Xcode 11, which provides a framework for declarative UI structure design across all Apple platforms.\n\nOfficial downloads of the SDK and toolchain for the Ubuntu distribution of Linux have been available since Swift 2.2, with more distros added since Swift 5.2.4, CentOS and Amazon Linux. There is an unofficial SDK and native toolchain package for Android, and in October 2025 Swift's Android workgroup announced a preview release of the official Swift SDK for Android.\n\nPlatforms\n\nThe platforms Swift supports are Apple's operating systems (Darwin, iOS, iPadOS, macOS, tvOS, watchOS), Linux, Windows, WebAssembly, and Android.\n\nA key aspect of Swift's design is its ability to interoperate with the huge body of existing Objective-C code developed for Apple products over the previous decades, such as Cocoa and the Cocoa Touch frameworks. On Apple platforms, it links with the Objective-C runtime library, which allows C, Objective-C, C++ and Swift code to run within one program.\n\nVersion history\n\nFeatures\n\nSwift is a general-purpose programming language that employs modern programming-language theory concepts and strives to present a simple, yet powerful syntax. Swift incorporates innovations and conventions from various programming languages, with notable inspiration from Objective-C, which it replaced as the primary development language on Apple platforms.\n\nSwift was designed to be safe and friendly to new programmers while not sacrificing speed. By default Swift manages all memory automatically and ensures variables are always initialized before use. Array accesses are checked for out-of-bounds errors and integer operations are checked for overflow. Parameter names allow creating clear APIs. Protocols define interfaces that types may adopt, while extensions allow developers to add more function to existing types. Swift enables object-oriented programming with the support for classes, subtyping, and method overriding. Optionals allow nil values to be handled explicitly and safely. Concurrent programs can be written using async/await syntax, and actors isolate shared mutable state in order to eliminate data races.\n\nBasic syntax\n\nSwift's syntax is similar to C-style languages. Code begins executing in the global scope by default. Alternatively, the @main attribute can be applied to a structure, class, or enumeration declaration to indicate that it contains the program's entry point.\n\nSwift's \"Hello, World!\" program is:print(\"Hello, world!\")\n\nThe print(_:separator:terminator:) function used here is included in Swift's standard library, which is available to all programs without the need to import external modules. Statements in Swift don't have to end with a semicolon, however semicolons are required to separate multiple statements written on the same line. Single-line comments begin with // and continue until the end of the current line. Multiline comments are contained by /* and */ characters.\nConstants (variables which cannot be modified) are declared with the let keyword, while variables declared using the var keyword can change. Values must be initialised before they are read. Variables may infer their type based on the type of the provided initial value. If the initial value is set after the value's declaration, a type must be declared explicitly.let highScoreThreshold = 1000 // A constant with type Int. The type was inferred based on the provided value.\n\nvar currentScore = 980 // A variable with type Int.\ncurrentScore = 1200 // The value of variables can change over time.\n\nlet playerMessage: String // A constant with explicit type String.\nif currentScore > highScoreThreshold {\n playerMessage = \"You are a top player!\"\n} else {\n playerMessage = \"Better luck next time.\"\n}\n\nprint(playerMessage) // Prints \"You are a top player!\"\n\nControl flow in Swift is managed with if-else, guard, and switch statements, along with while and for-in loops.\nThe if statements take a Boolean parameter and execute the body of the if statement if the condition is true, otherwise it executes the optional else body. if-let syntax provides syntactic sugar for checking for the existence of an optional value and unwrapping it at the same time.let someNumber = 42\nif someNumber % 2 == 0 { // Use the remainder operator to find the remainder of someNumber divided by 2.\n print(\"\\(someNumber) is even.\")\n} else {\n print(\"\\(someNumber) is odd.\")\n}\n\n// Prints \"42 is even.\"\n\nFunctions are defined with the func keyword. Function parameters may have names which allow function calls to read like phrases. An underscore before the parameter name allows the argument label to be omitted from the call site. Tuples can be used by functions to return multiple pieces of data at once.func constructGreeting(for name: String) -> String {\n return \"Hello \\(name)!\"\n}\n\nlet greeting = constructGreeting(for: \"Craig\")\n\nprint(greeting) // Prints \"Hello Craig!\"\n\nFunctions, and anonymous functions known as closures, can be assigned to properties and passed around the program like any other value.func divideByTwo(_ aNum: Int) -> Int {\n return aNum / 2\n}\n\nfunc multiplyByTwo(_ aNum: Int) -> Int {\n return aNum * 2\n}\n\nlet mathOperation = multiplyByTwo\n\nprint(mathOperation(21)) // Prints \"42\"\n\nguard statements require that the given condition is true before continuing on past the guard statement, otherwise the body of the provided else clause is run. The else clause must exit control of the code block in which the guard statement appears. guard statements are useful for ensuring that certain requirements are met before continuing on with program execution. In particular they can be used to create an unwrapped version of an optional value that is guaranteed to be non-nil for the remainder of the enclosing scope.func divide(numerator: Int?, byDenominator denominator: Int) -> Int? {\n guard denominator != 0 else {\n print(\"Can't divide by 0.\")\n return nil\n }\n\n guard let numerator else {\n print(\"The provided numerator is nil.\")\n return nil\n }\n\n return numerator / denominator\n}\n\nlet result = divide(numerator: 3, byDenominator: 0)\nprint(\"Division result is: \\(result)\")\n\n// Prints:\n// \"Can't divide by 0.\"\n// \"Division result is: nil.\"\n\nswitch statements compare a value with multiple potential values and then executes an associated code block. switch statements must be made exhaustive, either by including cases for all possible values or by including a default case which is run when the provided value doesn't match any of the other cases. switch cases do not implicitly fall through, although they may explicitly do so with the fallthrough keyword. Pattern matching can be used in various ways inside switch statements. Here is an example of an integer being matched against a number of potential ranges:let someNumber = 42\n\nswitch someNumber {\ncase ..<0: \n print(\"\\(someNumber) negative.\")\ncase 0: \n print(\"\\(someNumber) is 0.\")\ncase 1...9:\n print(\"\\(someNumber) greater than 0, but less than 10.\")\ndefault: \n print(\"\\(someNumber) is greater than 9.\")\n}\n\n// Prints \"42 is greater than 9.\"\n\nfor-in loops iterate over a sequence of values:let names = [\"Will\", \"Anna\", \"Bart\"]\nfor name in names {\n print(name)\n}\n// Prints:\n// Will\n// Anna\n// Bart\n\nwhile loops iterate as long as the given Boolean condition evaluates to true:// Add together all the numbers from 1 to 5.\nvar i = 1\nvar result = 0\n\nwhile i <= 5 { // The loop performs its body as long as i is less than or equal to 5. \n result += i // Add i to the current result.\n i += 1 // Increment i by 1.\n}\n\nprint(result) // Prints \"15\"\n\nClosure support\n\nSwift supports closures, which are self-contained blocks of functionality that can be passed around and used in code, and can also be used as anonymous functions. Here are some examples:\n\n// Closure type, defined by its input and output values, can be specified outside the closure:\nlet closure1: (Int, Int) -> Int = { arg1, arg2 in\n return arg1 + arg2\n}\n\n// …or inside it:\nlet closure2 = { (arg1: Int, arg2: Int) -> Int in\n return arg1 + arg2\n}\n\n// In most cases, closure's return type can be inferred automatically by the compiler.\nlet closure3 = { arg1: Int, arg2: Int in\n return arg1 + arg2\n}\n\nClosures can be assigned to variables and constants, and can be passed into other functions or closures as parameters. Single-expression closures may drop the return keyword.\n\nSwift also has a trailing closure syntax, which allows the closure to be written after the end of the function call instead of within the function's parameter list. Parentheses can be omitted altogether if the closure is the function's only parameter:\n\n// This function takes a closure which receives no input parameters and returns an integer,\n// evaluates it, and uses the closure's return value (an Int) as the function's return value.\nfunc foo(closure bar: () -> Int) -> Int {\n return bar()\n}\n\n// Without trailing closure syntax:\nfoo(closure: { return 1 })\n\n// With trailing closure syntax, and implicit return:\nfoo { 1 }\n\nStarting from version 5.3, Swift supports multiple trailing closures:\n\n// This function passes the return of the first closure as the parameter of the second,\n// and returns the second closure's result:\nfunc foo(bar: () -> Int, baz: (Int) -> Int) -> Int {\n return baz(bar())\n}\n\n// With no trailing closures:\nfoo(bar: { return 1 }, baz: { x in return x + 1 })\n\n// With 1 trailing closure:\nfoo(bar: { return 1 }) { x in return x + 1 }\n\n// With 2 trailing closures (only the first closure's argument name is omitted):\nfoo { return 1 } baz: { x in return x + 1 }\n\nSwift will provide shorthand argument names for inline closures, removing the need to explicitly name all of the closures parameters. Arguments can be referred to with the names $0, $1, $2, and so on:let names = [\"Josephine\", \"Steve\", \"Chris\", \"Barbara\"]\n\n// filter calls the given closure for each value in names. \n// Values with a character count less than 6 are kept, the others are dropped.\nlet shortNames = names.filter { $0.count < 6 }\n\nprint(shortNames) // Prints \"[\"Steve\", \"Chris\"]\"\n\nClosures may capture values from their surrounding scope. The closure will refer to this captured value for as long as the closure exists:func makeMultiplier(withMultiple multiple: Int) -> (Int) -> (Int) {\n // Create and return a closure that takes in an Int and returns the input multiplied by the value of multiple.\n return {\n $0 * multiple\n }\n}\n\nlet multiplier = makeMultiplier(withMultiple: 3)\nprint(multiplier(3)) // Prints \"9\"\nprint(multiplier(10)) // Prints \"30\"\n\nString support\n\nThe Swift standard library includes unicode-compliant String and Character types. String values can be initialized with a String literal, a sequence of characters surrounded by double quotation marks. Strings can be concatenated with the + operator:\n\nvar someString = \"Hello,\"\nsomeString += \" world!\"\n\nString interpolation allows for the creation of a new string from other values and expressions. Values written between parentheses preceded by a \\ will be inserted into the enclosing string literal:\nvar currentScore = 980\nprint(\"Your score is \\(currentScore).\")\n\n// Prints \"Your score is 980.\"\n\nA for-in loop can be used to iterate over the characters contained in a string:\nfor character in \"Swift\" {\n print(character)\n}\n// S\n// w\n// i\n// f\n// t\n\nIf the Foundation framework is imported, Swift invisibly bridges the String type to NSString (the String class commonly used in Objective-C).\n\nCallable objects\n\nIn Swift, callable objects are defined using callAsFunction.\n\nstruct CallableStruct {\n var value: Int\n func callAsFunction(_ number: Int, scale: Int) {\n print(scale * (number + value))\n }\n}\nlet callable = CallableStruct(value: 100)\ncallable(4, scale: 2)\ncallable.callAsFunction(4, scale: 2)\n// Both function calls print 208.\n\nAccess control\n\nSwift supports five access control levels for symbols: open, public, internal, fileprivate, and private. Unlike many object-oriented languages, these access controls ignore inheritance hierarchies: private indicates that a symbol is accessible only in the immediate scope, fileprivate indicates it is accessible only from within the file, internal indicates it is accessible within the containing module, public indicates it is accessible from any module, and open (only for classes and their methods) indicates that the class may be subclassed outside of the module.\n\nOptionals and chaining\n\nAn important feature in Swift is option types, which allow references or values to operate in a manner similar to the common pattern in C, where a pointer may either refer to a specific value or no value at all. This implies that non-optional types cannot result in a null-pointer error; the compiler can ensure this is not possible.\n\nOptional types are created with the Optional enum. To make an Integer that is nullable, one would use a declaration similar to var optionalInteger: Optional<Int>. As in C#, Swift also includes syntactic sugar for this, allowing one to indicate a variable is optional by placing a question mark after the type name, var optionalInteger: Int?. Variables or constants that are marked optional either have a value of the underlying type or are nil. Optional types wrap the base type, resulting in a different instance. String and String? are fundamentally different types, the former is of type String while the latter is an Optional that may be holding some String value.\n\nTo access the value inside, assuming it is not nil, it must be unwrapped to expose the instance inside. This is performed with the ! operator:\n\nlet myValue = anOptionalInstance!.someMethod()\n\nIn this case, the ! operator unwraps anOptionalInstance to expose the instance inside, allowing the method call to be made on it. If anOptionalInstance is nil, a null-pointer error occurs, terminating the program. This is known as force unwrapping. Optionals may be safely unwrapped using optional chaining, which first tests whether the instance is nil, and then unwraps it if it is not:\n\nlet myValue = anOptionalInstance?.someMethod()\n\nIn"
 },
 {
  "title": "Swift (bird)",
  "revision_id": "1370191076",
  "matched_by": "title-minus-qualifier",
  "text": "The Apodidae, or swifts, form a family of highly aerial birds. They are superficially similar to swallows but are not closely related to any passerine species. Swifts are placed in the order Apodiformes along with hummingbirds. The treeswifts are closely related to the true swifts but form a separate family, the Hemiprocnidae.\n\nResemblances between swifts and swallows are due to convergent evolution, reflecting similar life styles based on catching insects in flight.\n\nThe family name, Apodidae, is derived from the Greek ἄπους (ápous), meaning \"footless\", a reference to the small, weak legs of these most aerial of birds. The tradition of depicting swifts without feet continued into the Middle Ages, as seen in the heraldic martlet.\n\nTaxonomy\n\nTaxonomists have long classified swifts and treeswifts as relatives of the hummingbirds, a judgment corroborated by the discovery of the Jungornithidae (apparently swift-like hummingbird-relatives) and of primitive hummingbirds such as Eurotrochilus. Traditional taxonomies place the hummingbird family (Trochilidae) in the same order as the swifts and treeswifts (and no other birds); the Sibley-Ahlquist taxonomy treated this group as a superorder in which the swift order was called Trochiliformes.\n\nThe taxonomy of the swifts is complicated, with genus and species boundaries widely disputed, especially amongst the swiftlets. Analysis of behavior and vocalizations is complicated by common parallel evolution, while analyses of different morphological traits and of various DNA sequences have yielded equivocal and partly contradictory results.\n\nThe Apodiformes diversified during the Eocene, at the end of which the extant families were present; fossil genera are known from all over temperate Europe, between today's Denmark and France, such as the primitive swift-like Scaniacypselus (Early–Middle Eocene) and the more modern Procypseloides (Late Eocene/Early Oligocene – Early Miocene). A prehistoric genus sometimes assigned to the swifts, Primapus (Early Eocene of England), might also be a more distant ancestor.\n\nSpecies\n\nThere are around 100 species of swifts, normally grouped into two subfamilies and four tribes.\n\nCypseloidinae\n\nTribe Cypseloidini\n\nApodinae\n\nTribe Collocaliini – swiftlets\n\nTribe Chaeturini – needletails\n\nTribe Apodini – typical swifts\n\nDescription\n\nSwifts are among the fastest of birds in level flight, and larger species like the white-throated needletail have been reported travelling at up to 169 km/h (105 mph). Even the common swift can cruise at a maximum speed of 31 metres per second (112 km/h; 70 mph). In a single year the common swift can cover at least 200,000 km, and in a lifetime, about two million kilometers.\n\nThe wingtip bones of swiftlets are of proportionately greater length than those of most other birds. Changing the angle between the bones of the wingtips and forelimbs allows swifts to alter the shape and area of their wings to increase their efficiency and maneuverability at various speeds. They share with their relatives the hummingbirds a special ability to rotate their wings from the base, allowing the wing to remain rigid and fully extended and derive power on both the upstroke and downstroke. The downstroke produces both lift and thrust, while the upstroke produces a negative thrust (drag) that is 60% of the thrust generated during the downstrokes, but simultaneously it contributes lift that is also 60% of what is produced during the downstroke. This flight arrangement might benefit the bird's control and maneuverability in the air.\n\nThe swiftlets or cave swiftlets have developed a form of echolocation for navigating through dark cave systems where they roost. One species, the three-toed swiftlet, has recently been found to use this navigation at night outside its cave roost too.\n\nDistribution and habitat\n\nSwifts occur on all the continents except Antarctica, but not in the far north, in large deserts, or on many oceanic islands. The swifts of temperate regions are strongly migratory and winter in the tropics. Some species can survive short periods of cold weather by entering torpor, a state similar to hibernation.\n\nMany have a characteristic shape, with a short forked tail and very long swept-back wings that resemble a crescent or a boomerang. The flight of some species is characterised by a distinctive \"flicking\" action quite different from swallows. Swifts range in size from the pygmy swiftlet (Collocalia troglodytes), which weighs 5.4 g and measures 9 cm (3.5 in) long, to the purple needletail (Hirundapus celebensis), which weighs 184 g (6.5 oz) and measures 25 cm (9.8 in) long.\n\nBehaviour\n\nBreeding\n\nThe nest of many species is glued to a vertical surface with saliva, and the genus Aerodramus use only that substance, which is the basis for bird's nest soup. Other swifts select holes and small cavities in walls. The eggs hatch after 19 to 23 days, and the young leave the nest after a further six to eight weeks. Both parents assist in raising the young.\n\nSwifts as a family have smaller egg clutches and much longer and more variable incubation and fledging times than passerines with similarly sized eggs, resembling tubenoses in these developmental factors. Young birds reach a maximum weight heavier than their parents; they can cope with not being fed for long periods of time, and delay their feather growth when undernourished. Swifts and seabirds have generally secure nest sites, but their food sources are unreliable, whereas passerines are vulnerable in the nest but food is usually plentiful.\n\nFeeding\n\nAll swifts eat insects, such as dragonflies, flies, ants, aphids, wasps and bees, as well as aerial spiders. Prey is typically caught in flight using the beak. Some species, like the chimney swift, hunt in mixed species flocks with other aerial insectivores such as members of Hirundinidae (swallows).\n\nStatus\n\nNo swift species has become extinct since 1600, but BirdLife International lists the Atiu, Seychelles, and Mariana swiftlets and the ashy-tailed, American black and chimney swifts as vulnerable; eight other species are near threatened or lack sufficient data for classification.\n\nExploitation by humans\n\nThe hardened saliva nests of the edible-nest swiftlet and the black-nest swiftlet have been used in Chinese cooking for over 400 years, most often as bird's nest soup. Over-harvesting of this expensive delicacy has led to a decline in the numbers of these swiftlets, especially as the nests are also thought to have health benefits and aphrodisiac properties. Most nests are built during the breeding season by the male swiftlet over a period of 35 days. They take the shape of a shallow cup stuck to the cave wall. The nests are composed of interwoven strands of salivary cement and contain high levels of calcium, iron, potassium, and magnesium.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q257597",
  "label": "SWIFT",
  "description": "Belgian payments services society",
  "aliases": [
   "S.W.I.F.T. SCRL",
   "Society for Worldwide Interbank Financial Telecommunication"
  ],
  "claims": {
   "P31": [
    "Q43229",
    "Q986008"
   ]
  },
  "revision_id": "2558131301",
  "value_labels": {
   "Q43229": "organization",
   "Q986008": "payment system"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17118377",
  "label": "Swift",
  "description": "general-purpose, multi-paradigm, compiled programming language",
  "aliases": [
   "Apple Swift",
   "Swift programming language",
   "Swift language",
   "Swift (Apple programming language)",
   "Swiftlang",
   "Swift.org"
  ],
  "claims": {
   "P31": [
    "Q9143",
    "Q341",
    "Q12772052",
    "Q899523",
    "Q28923023"
   ],
   "P527": [
    "Q223490"
   ]
  },
  "revision_id": "2563335624",
  "value_labels": {
   "Q9143": "programming language",
   "Q341": "free software",
   "Q12772052": "multi-paradigm programming language",
   "Q899523": "object-based language",
   "Q28923023": "block-structured programming language",
   "Q223490": "LLVM"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q26617",
  "label": "Apodidae",
  "description": "family of birds",
  "aliases": [
   "swift family",
   "swifts"
  ],
  "claims": {
   "P31": [
    "Q16521"
   ]
  },
  "revision_id": "2567529447",
  "value_labels": {
   "Q16521": "taxon"
  },
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
  "ancestor_of": "Q257597",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q986008",
  "label": "payment system",
  "description": "system used to transfer monetary value, including institutions, instruments, people, rules, procedures, standards, and technologies",
  "aliases": [
   "payments system",
   "form of payment"
  ],
  "claims": {
   "P279": [
    "Q994895",
    "Q1416617"
   ],
   "P1889": [
    "Q1416617"
   ]
  },
  "revision_id": "2567236964",
  "ancestor_of": "Q257597",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q134602570",
  "label": "class of being",
  "description": "collection of entities with agency defined by common characteristics",
  "aliases": [
   "kind of agent",
   "type of agent",
   "agent class",
   "agent kind",
   "agent type",
   "kind of being",
   "type of being",
   "being class",
   "being kind",
   "being type",
   "class of agent"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414",
    "Q24017414"
   ],
   "P279": [
    "Q96251598",
    "Q134602526",
    "Q141439664"
   ],
   "P1889": [
    "Q134602505",
    "Q134602526"
   ]
  },
  "revision_id": "2568277985",
  "ancestor_of": "Q257597",
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
  "ancestor_of": "Q257597",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q96116695",
  "label": "type of system",
  "description": "Wikidata metaclass of sets of interacting or interdependent components",
  "aliases": [
   "form of system",
   "system type",
   "system form"
  ],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q21146257",
    "Q96251598"
   ]
  },
  "revision_id": "2553183990",
  "ancestor_of": "Q257597",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106559804",
  "label": "person or organization",
  "description": "class of agents",
  "aliases": [
   "person or organisation",
   "organisation or person",
   "organization or person",
   "human or organization"
  ],
  "claims": {
   "P279": [
    "Q24229398"
   ]
  },
  "revision_id": "2551510888",
  "ancestor_of": "Q257597",
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
  "ancestor_of": "Q257597",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1416617",
  "label": "financial system",
  "description": "system that allows the transfer of money between savers (and investors) and borrowers",
  "aliases": [],
  "claims": {
   "P31": [
    "Q96116695",
    "Q837171"
   ],
   "P279": [
    "Q1639361"
   ],
   "P1889": [
    "Q986008"
   ]
  },
  "revision_id": "2554598992",
  "ancestor_of": "Q257597",
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
  "ancestor_of": "Q17118377",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q341",
  "label": "free software",
  "description": "software distributed under terms that allow users to freely run, study, change and distribute it and modified versions",
  "aliases": [
   "libre software",
   "Free Software"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q5500964",
    "Q56273712",
    "Q1130645"
   ],
   "P361": [
    "Q1076638"
   ],
   "P460": [
    "Q1130645",
    "Q506883"
   ],
   "P1889": [
    "Q178285",
    "Q5500964",
    "Q1130645",
    "Q3943414"
   ]
  },
  "revision_id": "2572795734",
  "ancestor_of": "Q17118377",
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
  "ancestor_of": "Q17118377",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q899523",
  "label": "object-based language",
  "description": "programming language",
  "aliases": [
   "OOP programming language",
   "OOP",
   "object-oriented programming language",
   "object-oriented language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2515887381",
  "ancestor_of": "Q17118377",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28923023",
  "label": "block-structured programming language",
  "description": "programming language",
  "aliases": [],
  "claims": {
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2510626518",
  "ancestor_of": "Q17118377",
  "level": 1,
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
  "ancestor_of": "Q17118377",
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
  "ancestor_of": "Q17118377",
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
  "ancestor_of": "Q17118377",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17155032",
  "label": "software category",
  "description": "metaclass of software",
  "aliases": [
   "type of software",
   "software type",
   "software categories",
   "software types",
   "types of software",
   "category of software",
   "categories of software"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q16889133",
    "Q63981612",
    "Q483394"
   ]
  },
  "revision_id": "2534148034",
  "ancestor_of": "Q17118377",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5500964",
  "label": "freely redistributable software",
  "description": "software that anyone is free to redistribute",
  "aliases": [
   "FRS"
  ],
  "claims": {
   "P279": [
    "Q7397"
   ],
   "P1889": [
    "Q178285",
    "Q341",
    "Q7048868"
   ]
  },
  "revision_id": "2549515023",
  "ancestor_of": "Q17118377",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q56273712",
  "label": "source-available software",
  "description": "software distributed with its source code",
  "aliases": [],
  "claims": {
   "P279": [
    "Q7397"
   ],
   "P1889": [
    "Q506883",
    "Q1130645"
   ]
  },
  "revision_id": "2550276284",
  "ancestor_of": "Q17118377",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1130645",
  "label": "open-source software",
  "description": "software that anyone is free to use and redistribute in its current state with a permissive licence giving a libre access to its original source code (but not necessarily to modify it)",
  "aliases": [
   "open source software",
   "open-source code software",
   "OSS"
  ],
  "claims": {
   "P279": [
    "Q56273712",
    "Q5500964",
    "Q1293664"
   ],
   "P361": [
    "Q2251455"
   ],
   "P460": [
    "Q341",
    "Q506883"
   ],
   "P1889": [
    "Q39162",
    "Q341",
    "Q1156659",
    "Q506883",
    "Q56273712"
   ]
  },
  "revision_id": "2572055300",
  "ancestor_of": "Q17118377",
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
  "ancestor_of": "Q17118377",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16521",
  "label": "taxon",
  "description": "group of one or more organism(s), which a taxonomist adjudges to be a unit",
  "aliases": [
   "taxa",
   "taxonomic unit"
  ],
  "claims": {
   "P31": [
    "Q24017414",
    "Q115949945"
   ],
   "P279": [
    "Q21871294"
   ]
  },
  "revision_id": "2572889638",
  "ancestor_of": "Q26617",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q24017414",
  "label": "second-order class",
  "description": "metaclass containing as instances all classes of individuals",
  "aliases": [
   "2nd-order class",
   "metaclass of the first order"
  ],
  "claims": {
   "P31": [
    "Q24017465",
    "Q115490628"
   ],
   "P279": [
    "Q23959932",
    "Q19478619"
   ],
   "P1889": [
    "Q21146257",
    "Q19478619",
    "Q16889133",
    "Q23958852"
   ]
  },
  "revision_id": "2570870333",
  "ancestor_of": "Q26617",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q115949945",
  "label": "scientific concept",
  "description": "concept relating to science",
  "aliases": [
   "scientific concepts"
  ],
  "claims": {
   "P31": [
    "Q137429456"
   ],
   "P279": [
    "Q151885"
   ]
  },
  "revision_id": "2572886860",
  "ancestor_of": "Q26617",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21871294",
  "label": "group or class of living things",
  "description": "second-order class of living things",
  "aliases": [
   "group or class of living organisms",
   "group or class of organisms"
  ],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q98119401"
   ],
   "P1889": [
    "Q16334298",
    "Q55597235"
   ]
  },
  "revision_id": "2548867279",
  "ancestor_of": "Q26617",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-01834808-n",
  "lemmas": [
   "swift"
  ],
  "gloss": "a small bird that resembles a swallow and is noted for its rapid flight",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-01834353-n"
   ],
   "hyponym": [
    "oewn-01835134-n",
    "oewn-01835454-n",
    "oewn-01835753-n"
   ]
  },
  "relation_targets": {
   "oewn-01834353-n": "apodiform bird",
   "oewn-01835134-n": "European swift, Apus apus",
   "oewn-01835454-n": "chimney swift, chimney swallow, Chateura pelagica",
   "oewn-01835753-n": "swiftlet, Collocalia inexpectata"
  }
 },
 {
  "synset": "oewn-01683296-n",
  "lemmas": [
   "western fence lizard",
   "swift",
   "blue-belly",
   "Sceloporus occidentalis"
  ],
  "gloss": "common western lizard; seen on logs or rocks",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-01683119-n"
   ]
  },
  "relation_targets": {
   "oewn-01683119-n": "fence lizard"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 2: SQL (`f69xny35zm`)

~~~~text
Concept record:
{
 "id": "f69xny35zm",
 "preferred_name": "SQL",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Sql (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "pmy0yp0e50",
  "name": "NoSQL database"
 },
 {
  "id": "o92byobbda",
  "name": "PL/SQL"
 },
 {
  "id": "sh6x1wmacn",
  "name": "PostgreSQL"
 },
 {
  "id": "g1hfi5qy94",
  "name": "SQL-92"
 },
 {
  "id": "wkoox3i8b0",
  "name": "U-SQL"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "kp84ig38m5",
  "name": "Database design"
 },
 {
  "id": "sai8akfwpi",
  "name": "Database systems"
 },
 {
  "id": "iy9zh0s63e",
  "name": "ISO/IEC 9075 SQL standard"
 },
 {
  "id": "wrn21idyay",
  "name": "Relational database management system"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "h60l8olauw",
  "name": "JavaScript"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "z37uxoynx1",
  "name": "SQL tuning"
 },
 {
  "id": "onzi0v8hlf",
  "name": "PL/pgSQL"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "fu99i0fje4",
  "name": "Shell scripting"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
 },
 {
  "id": "rh3gh6e9pn",
  "name": "Elm"
 },
 {
  "id": "php2tc9p7y",
  "name": "XML"
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
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:44",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Operations Data Development Supervisor. [\"Data Analysis\", \"Process Improvement\", \"Microsoft Power Platform\", \"SQL\", \"Leadership\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:8",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Analytics Engineer. …ience Demonstrated ability to learn and master new technologies Experience transforming data and programming repeatable ETL workflows using SQL Experience delivering business insights from data using pivot tables, advanced excel models, or business intelligence tools such as Tableau or Power BI Know…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:19",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "Back-end, Python, SQL, Django"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:8",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Analyst. bi, data warehousing, sharepoint, dashboards, sql, analytics, change control, oos"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "SQL",
  "revision_id": "1374625236",
  "matched_by": "title",
  "text": "Structured Query Language (SQL) (pronounced /ˌɛsˌkjuˈɛl/ S-Q-L; or alternatively as /ˈsiːkwəl/ \"sequel\") is a domain-specific language used to manage data, especially in a relational database management system (RDBMS). It is particularly useful in handling structured data, i.e., data incorporating relations among entities and variables.\n\nIntroduced in the 1970s, SQL offered two main advantages over older read–write APIs such as ISAM or VSAM. Firstly, it introduced the concept of accessing many records with one single command. Secondly, it eliminates the need to specify how to reach a record, i.e., with or without an index.\n\nOriginally based upon relational algebra and tuple relational calculus, SQL consists of many types of statements, which may be informally classed as sublanguages, commonly: data query language (DQL), data definition language (DDL), data control language (DCL), and data manipulation language (DML).\n\nThe scope of SQL includes data query, data manipulation (insert, update, and delete), data definition (schema creation and modification), and data access control. Although SQL is essentially a declarative language (4GL), it also includes procedural elements.\n\nSQL was one of the first commercial languages to use Edgar F. Codd's relational model. The model was described in his influential 1970 paper, \"A Relational Model of Data for Large Shared Data Banks\". Despite not entirely adhering to the relational model as described by Codd, SQL became the most widely used database language.\n\nSQL became a standard of the American National Standards Institute (ANSI) in 1986 and of the International Organization for Standardization (ISO) in 1987. Since then, the standard has been revised multiple times to include a larger set of features and incorporate common extensions. Despite the existence of standards, virtually no implementations in existence adhere to it fully, and most SQL code requires at least some changes before being ported to different database systems.\n\nHistory\n\nSQL was initially developed at IBM by Donald D. Chamberlin and Raymond F. Boyce after learning about the relational model from Edgar F. Codd in the early 1970s. This version, initially called SEQUEL (Structured English Query Language), was designed to manipulate and retrieve data stored in IBM's original quasirelational database management system, System R, which a group at IBM San Jose Research Laboratory had developed during the 1970s.\n\nChamberlin and Boyce's first attempt at a relational database language was SQUARE (Specifying Queries in A Relational Environment), but it was difficult to use due to subscript/superscript notation. After moving to the San Jose Research Laboratory in 1973, they began work on a sequel to SQUARE. The original name SEQUEL, which is widely regarded as a pun on QUEL, the query language of Ingres, was later changed to SQL (dropping the vowels) because \"SEQUEL\" was a trademark of the UK-based Hawker Siddeley Dynamics Engineering Limited company. The label SQL later became the acronym for Structured Query Language.\n\nAfter testing SQL at customer test sites to determine the usefulness and practicality of the system, IBM began developing commercial products based on their System R prototype, including System/38, SQL/DS, and IBM Db2, which were commercially available in 1979, 1981, and 1983, respectively. IBM's endorsement caused the industry to move to SQL from alternatives like QUEL.\n\nIn the late 1970s, Relational Software, Inc. (now Oracle Corporation) saw the potential of the concepts described by Codd, Chamberlin, and Boyce, and developed their own SQL-based RDBMS with aspirations of selling it to the U.S. Navy, Central Intelligence Agency, and other U.S. government agencies. In June 1979, Relational Software introduced one of the first commercially available implementations of SQL, Oracle V2 (Version2) for VAX computers.\n\nBy 1986, ANSI and ISO standard groups officially adopted the standard \"Database Language SQL\" language definition. New versions of the standard were published in 1989, 1992, 1996, 1999, 2003, 2006, 2008, 2011, 2016 and, most recently, 2023.\n\nInteroperability and standardization\n\nOverview\n\nSQL implementations are incompatible between vendors and do not necessarily completely follow standards. In particular, date and time syntax, string concatenation, NULLs, and comparison case sensitivity vary from vendor to vendor. PostgreSQL and Mimer SQL strive for standards compliance, though PostgreSQL does not adhere to the standard in all cases. For example, the folding of unquoted names to lower case in PostgreSQL is incompatible with the SQL standard, which says that unquoted names should be folded to upper case. Thus, according to the standard, Foo should be equivalent to FOO, not foo.\n\nPopular implementations of SQL commonly omit support for basic features of Standard SQL, such as the DATE or TIME data types. The most obvious such examples, and incidentally the most popular commercial and proprietary SQL DBMSs, are Oracle (whose DATE behaves as DATETIME, and lacks a TIME type) and MS SQL Server (before the 2008 version). As a result, SQL code can rarely be ported between database systems without modifications.\n\nReasons for incompatibility\n\nSeveral reasons for the lack of portability between database systems include:\n\nThe complexity and size of the SQL standard means that most implementers do not support the entire standard.\n\nThe SQL standard does not specify the database behavior in some important areas (e.g., indices, file storage), leaving implementations to decide how to behave.\n\nThe SQL standard defers some decisions to individual implementations, such as how to name a results column that was not named explicitly.\n\nThe SQL standard precisely specifies the syntax that a conforming database system must implement. However, the standard's specification of the semantics of language constructs is less well-defined, leading to ambiguity.\n\nMany database vendors have large existing customer bases; where the newer version of the SQL standard conflicts with the prior behavior of the vendor's database, the vendor may be unwilling to break backward compatibility.\n\nLittle commercial incentive exists for vendors to make changing database suppliers easier (see vendor lock-in).\n\nUsers evaluating database software tend to place other factors such as performance higher in their priorities than standards conformance.\n\nStandardization history\n\nSQL was adopted as a standard by the ANSI in 1986 as SQL-86 and the ISO in 1987. It is maintained by ISO/IEC JTC 1, Information technology, Subcommittee SC 32, Data management and interchange.\n\nUntil 1996, the National Institute of Standards and Technology (NIST) data-management standards program certified SQL DBMS compliance with the SQL standard. Vendors now self-certify the compliance of their products.\n\nThe original standard declared that the official pronunciation for \"SQL\" was an initialism: /ˌɛsˌkjuːˈɛl/ (\"ess cue el\"). Regardless, many English-speaking database professionals (including Donald Chamberlin himself) use the acronym-like pronunciation of /ˈsiːkwəl/ (\"sequel\"), mirroring the language's prerelease development name, \"SEQUEL\". The SQL standard has gone through a number of revisions:\n\nCurrent standard\n\nThe standard is commonly denoted by the pattern: ISO/IEC 9075-n:yyyy Part n: title, or, as a shortcut, ISO/IEC 9075. Interested parties may purchase the standards documents from ISO, IEC, or ANSI. Some old drafts are freely available.\n\nISO/IEC 9075 is complemented by ISO/IEC 13249: SQL Multimedia and Application Packages and some Technical reports.\n\nSyntax\n\nThe SQL language is subdivided into several language elements, including:\n\nClauses, which are constituent components of statements and queries. (In some cases, these are optional.)\n\nExpressions, which can produce either scalar values, or tables consisting of columns and rows of data\n\nPredicates, which specify conditions that can be evaluated to SQL three-valued logic (3VL) (true/false/unknown) or Boolean truth values and are used to limit the effects of statements and queries, or to change program flow.\n\nQueries, which retrieve the data based on specific criteria. This is an important element of SQL.\n\nStatements, which may have a persistent effect on schemata and data, or may control transactions, program flow, connections, sessions, or diagnostics.\n\nSQL statements also include the semicolon (\";\") statement terminator. Though not required on every platform, it is defined as a standard part of the SQL grammar.\n\nInsignificant whitespace is generally ignored in SQL statements and queries, making it easier to format SQL code for readability.\n\nProcedural extensions\n\nSQL is designed for a specific purpose: to query data contained in a relational database. SQL is a set-based, declarative programming language, not an imperative programming language like C or BASIC. However, extensions to Standard SQL add procedural programming language functionality, such as control-of-flow constructs.\n\nIn addition to the standard SQL/PSM extensions and proprietary SQL extensions, procedural and object-oriented programmability is available on many SQL platforms via DBMS integration with other languages. The SQL standard defines SQL/JRT extensions (SQL Routines and Types for the Java Programming Language) to support Java code in SQL databases. Microsoft SQL Server 2005 uses the SQLCLR (SQL Server Common Language Runtime) to host managed .NET assemblies in the database, while prior versions of SQL Server were restricted to unmanaged extended stored procedures primarily written in C. PostgreSQL lets users write functions in a wide variety of languages—including Perl, Python, Tcl, JavaScript (PL/V8) and C.\n\nAlternatives\n\nA distinction should be made between alternatives to SQL as a language, and alternatives to the relational model itself. Below are proposed relational alternatives to the SQL language. See navigational database and NoSQL for alternatives to the relational model.\n\n.QL: object-oriented Datalog\n\n4D Query Language (4D QL)\n\nDatalog: critics suggest that Datalog has two advantages over SQL: it has cleaner semantics, which facilitates program understanding and maintenance, and it is more expressive, in particular for recursive queries.\n\nHTSQL: URL based query method\n\nIBM Business System 12 (IBM BS12): one of the first fully relational database management systems, introduced in 1982\n\nISBL\n\njOOQ: SQL implemented in Java as an internal domain-specific language\n\nJava Persistence Query Language (JPQL): The query language used by the Java Persistence API and Hibernate persistence library\n\nJavaScript: MongoDB implements its query language in a JavaScript API.\n\nLINQ: Runs SQL statements written like language constructs to query collections directly from inside .Net code\n\nObject Query Language\n\nQBE (Query By Example) created by Moshè Zloof, IBM 1977\n\nQUEL introduced in 1974 by the U.C. Berkeley Ingres project, closer to tuple relational calculus than SQL\n\nXQuery\n\nDistributed SQL processing\n\nDistributed Relational Database Architecture (DRDA) was designed by a workgroup within IBM from 1988 to 1994. DRDA enables network-connected relational databases to cooperate to fulfill SQL requests.\n\nAn interactive user or program can issue SQL statements to a local RDB and receive tables of data and status indicators in reply from remote RDBs. SQL statements can also be compiled and stored in remote RDBs as packages and then invoked by package name. This is important for the efficient operation of application programs that issue complex, high-frequency queries. It is especially important when the tables to be accessed are located in remote systems.\n\nThe messages, protocols, and structural components of DRDA are defined by the Distributed Data Management Architecture. Distributed SQL processing ala DRDA is distinctive from contemporary distributed SQL databases.\n\nCriticisms\n\nDesign\n\nSQL deviates in several ways from its theoretical foundation, the relational model and its tuple calculus. In that model, a table is a set of tuples, while in SQL, tables and query results are lists of rows; the same row may occur multiple times, and the order of rows can be employed in queries (e.g., in the LIMIT clause).\nCritics argue that SQL should be replaced with a language that returns strictly to the original foundation: for example, see The Third Manifesto by Hugh Darwen and C.J. Date (2006, ISBN 0-321-39942-0).\n\nOrthogonality and completeness\n\nEarly specifications did not support major features, such as primary keys. Result sets could not be named, and subqueries had not been defined. These were added in 1992.\n\nThe lack of sum types has been described as a roadblock to full use of SQL's user-defined types. JSON support, for example, needed to be added by a new standard in 2016.\n\nNull\n\nThe concept of Null is the subject of some debate. The Null marker indicates the absence of a value, and is distinct from a value of 0 for an integer column or an empty string for a text column. The concept of Nulls enforces the 3-valued-logic in SQL, which is a concrete implementation of the general 3-valued logic.\n\nDuplicates\n\nAnother popular criticism is that it allows duplicate rows, making integration with languages such as Python, whose data types might make accurately representing the data difficult, in terms of parsing and by the absence of modularity. This is usually avoided by declaring a primary key, or a unique constraint, with one or more columns that uniquely identify a row in the table.\n\nImpedance mismatch\n\nIn a sense similar to object–relational impedance mismatch, a mismatch occurs between the declarative SQL language and the procedural languages in which SQL is typically embedded.\n\nSQL data types\n\nThe SQL standard defines three kinds of data types (chapter 4.1.1 of SQL/Foundation):\n\npredefined data types\n\nconstructed types\n\nuser-defined types.\n\nConstructed types are one of ARRAY, MULTISET, REF (reference), or ROW. User-defined types are comparable to classes in object-oriented language with their own constructors, observers, mutators, methods, inheritance, overloading, overwriting, interfaces, and so on. Predefined data types are intrinsically supported by the implementation.\n\nPredefined data types\n\nCharacter types\n\nCharacter (CHAR)\n\nCharacter varying (VARCHAR)\n\nCharacter large object (CLOB)\n\nNational character types\n\nNational character (NCHAR)\n\nNational character varying (NCHAR VARYING)\n\nNational character large object (NCLOB)\n\nBinary types\n\nBinary (BINARY)\n\nBinary varying (VARBINARY)\n\nBinary large object (BLOB)\n\nNumeric types\n\nExact numeric types (NUMERIC, DECIMAL, SMALLINT, INTEGER, BIGINT)\n\nApproximate numeric types (FLOAT, REAL, DOUBLE PRECISION)\n\nDecimal floating-point type (DECFLOAT)\n\nDatetime types (DATE, TIME, TIMESTAMP)\n\nInterval type (INTERVAL)\n\nBoolean\n\nXML (see SQL/XML)\n\nJSON\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q47607",
  "label": "SQL",
  "description": "relational database language that allows to extract from data tables a series of records with selection, sorting and computation criteria, or to update, delete or add records",
  "aliases": [
   "Structural Query Language",
   "sql"
  ],
  "claims": {
   "P31": [
    "Q1144882",
    "Q845739",
    "Q9143",
    "Q691358"
   ],
   "P279": [
    "Q845739"
   ],
   "P1889": [
    "Q62625630"
   ]
  },
  "revision_id": "2567695241",
  "value_labels": {
   "Q1144882": "declarative programming language",
   "Q845739": "query language",
   "Q9143": "programming language",
   "Q691358": "domain-specific language",
   "Q62625630": "Structured Query Language script"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3373000",
  "label": "San Carlos Airport",
  "description": "airport in California, United States",
  "aliases": [
   "SQL",
   "KSQL"
  ],
  "claims": {
   "P31": [
    "Q1248784",
    "Q62447"
   ]
  },
  "revision_id": "2569962806",
  "value_labels": {
   "Q1248784": "airport",
   "Q62447": "aerodrome"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1144882",
  "label": "declarative programming language",
  "description": "type of programming language",
  "aliases": [
   "declarative language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2552532865",
  "ancestor_of": "Q47607",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q845739",
  "label": "query language",
  "description": "computer language used to make queries into databases and information systems such as SQL or XQuery",
  "aliases": [
   "DQLs",
   "DQL",
   "database query language"
  ],
  "claims": {
   "P31": [
    "Q137527772"
   ],
   "P279": [
    "Q629206"
   ]
  },
  "revision_id": "2555417010",
  "ancestor_of": "Q47607",
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
  "ancestor_of": "Q47607",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q691358",
  "label": "domain-specific language",
  "description": "computer language specialized to a particular application domain",
  "aliases": [
   "DSL"
  ],
  "claims": {
   "P31": [
    "Q137527772",
    "Q116481801"
   ],
   "P279": [
    "Q629206"
   ]
  },
  "revision_id": "2511822434",
  "ancestor_of": "Q47607",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q845739",
  "label": "query language",
  "description": "computer language used to make queries into databases and information systems such as SQL or XQuery",
  "aliases": [
   "DQLs",
   "DQL",
   "database query language"
  ],
  "claims": {
   "P31": [
    "Q137527772"
   ],
   "P279": [
    "Q629206"
   ]
  },
  "revision_id": "2555417010",
  "ancestor_of": "Q47607",
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
  "ancestor_of": "Q47607",
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
  "ancestor_of": "Q47607",
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
  "ancestor_of": "Q47607",
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
  "ancestor_of": "Q47607",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1248784",
  "label": "airport",
  "description": "location where aircraft take off and land with extended support facilities, mostly for commercial air transport",
  "aliases": [
   "airports",
   "air port",
   "aerodrome"
  ],
  "claims": {
   "P31": [
    "Q136312010"
   ],
   "P279": [
    "Q62447",
    "Q12819564",
    "Q2516121"
   ],
   "P527": [
    "Q1433344",
    "Q390516"
   ],
   "P460": [
    "Q94993988"
   ],
   "P1889": [
    "Q231740",
    "Q64788077",
    "Q381421",
    "Q695850",
    "Q62447"
   ]
  },
  "revision_id": "2571908442",
  "ancestor_of": "Q3373000",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q62447",
  "label": "aerodrome",
  "description": "location from which aircraft flight operations take place",
  "aliases": [
   "airdrome",
   "airfield",
   "air navigation feature"
  ],
  "claims": {
   "P31": [
    "Q136312010"
   ],
   "P279": [
    "Q811979",
    "Q20977775",
    "Q12819564"
   ],
   "P527": [
    "Q573970",
    "Q449263"
   ],
   "P1889": [
    "Q4688231",
    "Q1248784"
   ]
  },
  "revision_id": "2571907318",
  "ancestor_of": "Q3373000",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q136312010",
  "label": "type of aerodrome",
  "description": "wikimedia metaclass for airports",
  "aliases": [
   "type of airport",
   "airport type",
   "aerodrome type"
  ],
  "claims": {
   "P31": [
    "Q24017414",
    "Q5962346"
   ],
   "P279": [
    "Q134496690"
   ]
  },
  "revision_id": "2548079840",
  "ancestor_of": "Q3373000",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12819564",
  "label": "station",
  "description": "intermediate stopping places along transportation routes",
  "aliases": [
   "transit station",
   "depot (station)",
   "stations",
   "depots (station)",
   "transport station"
  ],
  "claims": {
   "P279": [
    "Q141162639"
   ],
   "P361": [
    "Q18325841"
   ],
   "P527": [
    "Q55488",
    "Q928830",
    "Q2175765",
    "Q953806"
   ],
   "P1889": [
    "Q548662",
    "Q34700",
    "Q1493264",
    "Q2864108",
    "Q25635419"
   ]
  },
  "revision_id": "2553184288",
  "ancestor_of": "Q3373000",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2516121",
  "label": "transport structure",
  "description": "building or construction facilitating movement of people or vehicles",
  "aliases": [
   "traffic structure",
   "transportation building",
   "transport building",
   "transport building or structure",
   "transport building and structure",
   "transportation structure"
  ],
  "claims": {
   "P279": [
    "Q811979",
    "Q376799"
   ],
   "P361": [
    "Q376799"
   ]
  },
  "revision_id": "2567823548",
  "ancestor_of": "Q3373000",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q811979",
  "label": "built structure",
  "description": "human-designed and -made structure",
  "aliases": [
   "designed structure",
   "architectural structures",
   "designed structures",
   "structure in architecture",
   "structures in architecture",
   "structure",
   "structures",
   "structural object",
   "civil engineering structure",
   "architectural structure"
  ],
  "claims": {
   "P31": [
    "Q111972893"
   ],
   "P279": [
    "Q11908691",
    "Q811430",
    "Q386724",
    "Q134301417"
   ],
   "P361": [
    "Q12271",
    "Q1497375"
   ],
   "P460": [
    "Q1322402",
    "Q811463",
    "Q811430"
   ],
   "P1889": [
    "Q13226383",
    "Q3875186",
    "Q12271",
    "Q1322402",
    "Q6671777",
    "Q41176",
    "Q108735920",
    "Q29033082"
   ]
  },
  "revision_id": "2562848577",
  "ancestor_of": "Q3373000",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20977775",
  "label": "air transport infrastructure",
  "description": "facilities and equipment in place to facilitate transportation by air",
  "aliases": [
   "air transport facilitation"
  ],
  "claims": {
   "P279": [
    "Q376799"
   ],
   "P361": [
    "Q1757562"
   ]
  },
  "revision_id": "2534298598",
  "ancestor_of": "Q3373000",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
