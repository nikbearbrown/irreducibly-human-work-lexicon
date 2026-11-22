# Irreducibly Human Work Lexicon pilot, grounded run: message 13 of 13 (chunk 12, 2 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "12", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-12.jsonl`. Otherwise send one code block marked `jsonl` holding the 2 lines and nothing else. A script will check them afterwards.

**This is the last chunk.** After the drafts, add a short note headed `RUN.md` with: your model and version and any reasoning or effort setting; when you started chunk 00 and finished this one (date and time, with time zone); and anything you did differently from these instructions, with the reason.

---

## Concept 1 of 2: Salesforce (`url3hq4jid`)

~~~~text
Concept record:
{
 "id": "url3hq4jid",
 "preferred_name": "Salesforce",
 "kind": "platform",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Salesforce.Com"
  },
  {
   "label": "Salesforce CRM"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "ib7s2w06na",
  "name": "Market capitalization"
 },
 {
  "id": "kli63uvu2s",
  "name": "Platform as a service"
 },
 {
  "id": "rm0k01pcl6",
  "name": "Software as a service"
 },
 {
  "id": "enjwt6y9ws",
  "name": "Tableau"
 },
 {
  "id": "ed3v3ccr0e",
  "name": "Apex"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "duizwpkp0n",
  "name": "Net zero"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "s00v9m81ez",
  "name": "Customer success"
 },
 {
  "id": "mhqjaq3kyx",
  "name": "Salesforce Datorama"
 },
 {
  "id": "rvakw702hv",
  "name": "Salesforce Social Studio"
 },
 {
  "id": "yitddfndv7",
  "name": "Use of force"
 },
 {
  "id": "wcgrarya9l",
  "name": "Sinhala"
 },
 {
  "id": "z3in4qbkv2",
  "name": "Sales journal"
 },
 {
  "id": "pwau7gon42",
  "name": "Resorcerer"
 },
 {
  "id": "hte4e69ldf",
  "name": "Maltese"
 },
 {
  "id": "j8bl0xzopw",
  "name": "Version control"
 },
 {
  "id": "gtxd0h0n8y",
  "name": "AtScale"
 },
 {
  "id": "gb10qwtibo",
  "name": "Brute-force search"
 },
 {
  "id": "bh53jfisdj",
  "name": "Candidate sourcing"
 },
 {
  "id": "r9w5fxlhk3",
  "name": "Pathlore"
 },
 {
  "id": "nprk9hwd27",
  "name": "Assamese"
 },
 {
  "id": "g32rgj6uc5",
  "name": "Goal-oriented"
 },
 {
  "id": "b01cze4ssf",
  "name": "Security Check (SC) clearance"
 },
 {
  "id": "njlcvlg504",
  "name": "Causal reasoning"
 },
 {
  "id": "wmeomhwzf1",
  "name": "Sundanese"
 },
 {
  "id": "f1mc7yrkqz",
  "name": "SAP Fiori"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:20",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Enterprise Account Executive. sales|director|full-time|communication|salesforce|git|ai|go|ml"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:242",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Sales Associate – South Indian Language Support. …ies to achieve targets and increase revenue 2. Provide sales support to customers and address any inquiries or concerns promptly 3. Utilize Salesforce to track sales activities and customer interactions 4. Communicate effectively with customers and team members to ensure smooth operations 5. Profici…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:14",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: CSM Ops Analyst. Analyst, Data analysis, ERP, Automation, MIS, Analytical, Salesforce.com, Macros"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:12",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Director Sales Enablement. …n events such as annual sales achiever club Sales Operations – Drives excellence in the use of sales applications and processes centered on Salesforce.com, and ensuring quality in the opportunity management process. Drives efficiency and standardization across all regions on Salesforce.com use and r…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:928",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: E-Commerce Creative & Website Manager. Website management, Basic graphic design principles, Optimizing product pages, Visual merchandising, Experience working in the beauty industry, Salesforce, Merchandising, AI tools proficiency, Shopify, Digital brand management, Mid-level, E-commerce website design, E-commerce, Email marketing experi…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "Salesforce",
  "revision_id": "1375823027",
  "matched_by": "title",
  "text": "Salesforce, Inc. is an American enterprise software company headquartered in San Francisco, California. It is best known for customer relationship management software and related applications, which the corporation delivers through a software as a service subscription business model. It also provides software for sales, customer service, marketing automation, e-commerce, data analytics, artificial intelligence, agentic AI, and application development.\n\nFounded by former Oracle executive Marc Benioff in March 1999, Salesforce experienced rapid growth in the sector in which it competed, debuting its initial public offering in 2004. Its major acquisitions included Tableau and Slack. As of March 2026, Salesforce has a market capitalization of approximately US$186 billion. For fiscal year 2026 (ending January 31, 2026), the company reported record annual revenue of $41.5 billion. The company is a component of the Dow Jones Industrial Average (since 2020) and the S&P 500.\n\nHistory\n\nSalesforce was founded on March 8, 1999, by former Oracle executive Marc Benioff, together with Parker Harris, Dave Moellenhoff, and Frank Dominguez as a software-as-a-service (SaaS) company. The first prototype of Salesforce was launched in November 1999.\n\nTwo of Salesforce's earliest investors were Larry Ellison, the co-founder and first CEO of Oracle, and Halsey Minor, the founder of CNET.\n\nSalesforce was severely affected by the dot-com bubble bursting at the beginning of the new millennium, resulting in the company laying off 20% of its workforce. Despite its losses, Salesforce held up during the early 2000s. Salesforce also gained notability during this period for its \"the end of software\" tagline and marketing campaign, and even hired actors to hold up signs with its slogan outside a Siebel Systems conference. Salesforce's revenue continued to increase, moving from $5.4 million in 2000 to $22.4 million in 2001.\n\nIn 2003, Salesforce held its first annual Dreamforce conference in San Francisco. There were around 1,300 attendees and 50 exhibitors at the conference.\n\nIn June 2004, the company had its initial public offering on the New York Stock Exchange (under the stock symbol CRM) and raised US$110 million. In 2006, Salesforce launched Idea Exchange, a platform that allows customers to connect with company product managers.\n\nIn 2009, Salesforce passed $1 billion in annual revenue. Also, in 2009, the company launched Service Cloud, an application that helps companies manage service conversations about their products and services.\n\nIn 2014, the company released Trailhead, a free online learning platform for its products. In October 2014, Salesforce announced the development of its Customer Success Platform. In September 2016, Salesforce announced the launch of Einstein, an artificial intelligence platform that supports several of Salesforce's cloud services. Salesforce licensed the right to use Albert Einstein's image and likeness from the Einstein Estate under a 20-year agreement for $20 million, restricted to business software applications.\n\nSalesforce acquired the visual analytics and business intelligence software platform Tableau in August 2019 for $15.7 billion.\n\nIn 2020, Salesforce joined the Dow Jones Industrial Average, replacing energy giant and Standard Oil-descendant ExxonMobil. Salesforce's ascension to the Dow Jones was concurrent with that of Amgen and Honeywell. Because the Dow Jones factors its components by market price, Salesforce was the largest technology component of the index at its accession.\n\nSalesforce experienced significant leadership transitions between 2020 and 2021; Keith Block stepped down as co-CEO in February 2020, leaving Marc Benioff as sole chairman and CEO. In February 2021, Weaver, previously the chief legal officer, became CFO, where she served until stepping down in August 2024. Former CFO Mark Hawkins announced that he would be retiring in October. In November 2021, Bret Taylor was named vice chair and co-CEO of the company alongside Benioff.\n\nIn December 2020, Salesforce announced its acquisition of Slack for $27.7 billion, the largest in company history; the deal closed in July 2021. The purchase price represented a 54% premium over Slack's closing market capitalization at the announcement date, valued at approximately $18 billion. Salesforce justified the premium based on anticipated synergies from integrating Slack's messaging platform with its CRM services.\n\nSalesforce launched the Sustainability Cloud (Net Zero Cloud as of 2022), which is used by companies to track progress towards achieving their net zero emissions goals.\n\nIn April 2022, \"Salesforce.com, Inc.\" changed its legal name to \"Salesforce, Inc.\"\n\nIn August 2022, Salesforce surpassed SAP in total revenue and market capitalization to become the world's largest enterprise applications software company, according to industry analysis.\n\nThe next month, Salesforce announced a partnership with Meta Platforms. The deal called for Meta's consumer application WhatsApp to integrate Salesforce's Customer 360 platform to allow consumers to communicate with companies directly.\n\nIn November 2022, Salesforce announced it would terminate some employees from its sales team. That same month, Salesforce announced its co-CEO and vice chair, Bret Taylor, would be stepping down from his roles at the end of January 2023, with Benioff continuing to run the company and serve as board chair. Within the week, former Tableau CEO Mark Nelson and former Slack CEO Stewart Butterfield also announced their departures. When asked about departures, Benioff stated, \"people come and people go.\" Following these executive transitions, Salesforce's stock declined significantly, with market analysts attributing the decline to concerns about leadership stability and strategic continuity.\n\nIn January 2023, the company announced a layoff of about 10%, or approximately 8,000 positions. According to Benioff, the company hired too aggressively during the COVID-19 pandemic and the increase in working from home led to the layoff. The company also reduced office space as part of the restructuring plan. The same month brought an announcement from activist investor Elliott Management that it would acquire a \"big stake\" in the company.\n\nIn January 2024, Salesforce announced it was laying off 700 of its global staff.\n\nIn October 2025, Salesforce CEO Marc Benioff declared his avid support of Donald Trump and urged him to deploy the National Guard to San Francisco as Trump was deploying federal troops to other cities. The comments generated significant controversy for Benioff and Salesforce, including push-back from San Francisco mayor Daniel Lurie and District Attorney Brooke Jenkins and the resignation of Ron Conway from the Salesforce Foundation board. Benioff subsequently apologized for his National Guard comments. That same month, Salesforce pitched the Trump administration on ways that Salesforce's AI tools could help Immigration and Customs Enforcement (ICE) triple its staff to support the administration's mass deportation campaign. The company had previously contracted for ICE under the Obama and Biden administrations.\n\nServices\n\nSalesforce offers several customer relationship management (CRM) services for enterprises and small businesses, including Sales Cloud, Service Cloud, Marketing Cloud,Commerce Cloud and Platform. Additional technologies include Slack.Salesforce also offers a free CRM for small teams of up to two people.\n\nOther services include app creation, data integration and visualization, and training.\n\nSalesforce launched a suite of features called Salesforce Foundations in September 2024, bundling connected functionality across department-specific Sales Cloud and Service Cloud products.\n\nSalesforce introduced Headless 360 at its annual TDX developer conference in April 2026. Headless 360 exposes the Saleforce platform's data, workflows, and governance controls as APIs, MCP servers, and CLI commands, so tasks can be completed without browser interaction.\n\nArtificial intelligence\n\nLaunched at Dreamforce in 2016, Salesforce Einstein was the company's first artificial intelligence product.\n\nIn March 2023, Salesforce announced ChatGPT integration in Slack was available to any organization, and the launch of Einstein GPT, a generative AI service.\n\nIn March 2024, Salesforce launched Einstein Copilot: Health Actions, an assistant based on its earlier artificial intelligence platform Einstein. It can be used to assist in making appointments, referrals, and gathering patient information. In July, Salesforce released an AI agent with the ability to perform customer service actions, like enabling product returns or refunds.\n\nIn September and October 2024, the company deployed Agentforce (succeeding Salesforce Einstein), an agentic AI. This enables the use of chatbots within its software.In June 2026, Salesforce integrated autonomous shopping agents natively into its stack through Commerce Cloud.\n\nSalesforce CEO Marc Benioff said in a June 2025 interview that artificial intelligence performed between 30% and 50% of internal work at Salesforce, including functions such as software engineering, customer service, marketing, and analytics.\n\nSalesforce Platform\n\nSalesforce Platform (formerly known as Force.com) is a platform as a service (PaaS) that allows developers to add applications to the main Salesforce.com application. These applications are hosted on Salesforce.com infrastructure.\n\nForce.com applications are built using Apex, a proprietary Java-like programming language, to generate HTML originally via the \"Visualforce\" framework. Beginning in 2015, the \"Lightning Components\" framework has been supported. The Apex language and compiler were initially designed by Craig Weissman.\n\nAs of 2014, the Force.com platform had 1.5 million registered developers according to Salesforce.\n\nAppExchange\n\nLaunched in 2005, the Salesforce AppExchange is an online app store that allows users to sell third-party applications and consulting services.\n\nTrailhead\n\nLaunched in 2014, Trailhead is a free online learning platform with courses focused on Salesforce technologies.\n\nDiscontinued\n\nDesk.com was a SaaS help desk and customer support product acquired by Salesforce for $50 million in 2011, and consolidated with other services into Service Cloud Essentials in March 2018.\n\nDo.com was a cloud-based task management system for small groups and businesses, introduced in 2011, and discontinued in 2014.\n\nAcquisitions\n\n2006–2019\n\nIn 2006, Salesforce acquired Sendia, a mobile web service firm, for $15 million and Kieden, an online advertising company. In 2007, Koral, a content management service, was acquired. In 2008, Salesforce acquired Instranet for $31.5 million. In 2010, Salesforce acquired multiple companies, including Jigsaw, a cloud-based data service provider, for $142 million, Heroku, a Ruby application platform-as-a-service, for $212 million, and Activa Live Chat, a live chat software provider. \nIn 2011, Salesforce acquired Dimdim, a web conferencing platform, for $31 million, Radian6, a social media tracking company, for $340 million, and Rypple, a performance management software company. Rypple became known as Work.com in 2012. In 2012, Salesforce acquired Buddy Media, a social media marketer, for $689 million, and GoInstant, a browser collaboration startup, for $70 million.\n\nIn 2013, Salesforce acquired ExactTarget, an email marketer, for $2.5 billion. In 2014, Salesforce acquired RelateIQ, a data company, for $390 million. In 2015, Salesforce acquired multiple companies for undisclosed sums, including Toopher, a mobile authentication company, Tempo, an AI calendar app, and MinHash, an AI platform. The company also acquired SteelBrick, a software company, for $360 million.\n\nIn 2016, Salesforce acquired Demandware, a cloud-based provider of e-commerce services, for $2.8 billion and Quip, a word processing app, for $750 million. In 2017, the company acquired Sequence, a user experience design agency. In 2018, Salesforce acquired several companies, including MuleSoft, a cloud service company, for $6.5 billion, as well as Rebel, an email services provider, and Datorama, an AI marketing platform.\n\nIn 2019, Salesforce completed its acquisition of analytics software company Tableau for $15.7 billion. Salesforce also acquired ClickSoftware for $1.35 billion in 2019.\n\n2020–present\n\nSlack Technologies was acquired for $27.7 billion in 2021. Salesforce also made smaller acquisitions between 2020 and 2021, including consulting firm Acumen Solutions for $570 million, CRM firm Vlocity for $1.33 billion, privacy compliance startup Phennecs for $16.5 million, and robotic process automation firm Servicetrace.\n\nSalesforce's acquired Slack-bot maker Troops.ai in July 2022.\n\nIn September 2023, Salesforce acquired Airkit.ai, a creator of AI-powered customer service applications and experiences. In December 2023, Salesforce acquired Spiff, an automated commission management platform.\n\nIn September 2024, Salesforce acquired data management firm Own for $1.9 billion, and enterprise management platform Zoomin. Salesforce has also acquired PredictSpring and Tenyx in 2024.\n\nIn June 2025, Salesforce announced plans to acquire data management platform Informatica for approximately $8 billion. The deal strengthens Salesforce's data integration and governance capabilities across its platform ecosystem. Prior negotiations in 2024 failed due to disagreements over valuation and deal structure.\n\nIn November 2025, Salesforce announced the successful completion of its acquisition of Informatica for approximately $8 billion in equity value. The deal was completed ahead of the original early-2026 target. By February 2026, Salesforce reported that Informatica had already begun contributing significantly to its financial results, including nearly $400 million in revenue during the fourth quarter of fiscal year 2026.\n\nIn June 2026, Salesforce announced the acquisition of Contentful for a reported sum of $1.5 billion. The acquisition was completed on September 1, 2026. \n\nIn June 2026, Salesforce announced that it had signed a definitive agreement to acquire m3ter, a London-based metering and rating platform for consumption-based billing.\n\nAlso in June 2026, Salesforce announced an agreement to acquire Fin, an artificial intelligence customer-service platform, for approximately $3.6 billion. The transaction was expected to close in the fourth quarter of Salesforce's fiscal year.\n\nOperations\n\nSalesforce is headquartered in San Francisco in the Salesforce Tower. Salesforce has 110 offices, including offices in Hong Kong, Tel Aviv, London, Paris, Sydney and Tokyo.\n\nStandard & Poor's added Salesforce to the S&P 500 Index in September 2008. In August 2020, S&P Dow Jones Indices announced that Salesforce would replace ExxonMobil in the Dow Jones Industrial Average.\n\nCulture\n\nAccording to Marc Benioff, Salesforce corporate culture is based on 'Ohana,' a Hawaiian concept emphasizing family and community. Benioff has described this philosophy as prioritizing employee well-being and broader stakeholder relationships.\n\nIn 2021, Cynthia Perry, a design research senior manager, publicly resigned from Salesforce alleging workplace discrimination related to diversity and inclusion practices and posting her resignation letter on LinkedIn.\n\nOn September 10, 2021, Benioff tweeted that the company is prepared to help any employee who wishes to move out of the state of Texas, following abortion legislation in Texas, announced on September 1, 2021.\n\nFinances\n\nSalesforce ranked 126th on the 2022 Fortune 500 list of the largest United States companies by revenue.\n\nIT infrastructure\n\nIn 2008, Salesforce migrated from Sun Fire E25K servers with SPARC processors running Solaris, to Dell servers with AMD processors, running Linux.\n\nIn 2012, Salesforce announced plans to build a data center in the UK to handle European citizens' personal data. The center opened in 2014.\n\nIn 2013, Salesforce and Oracle announced a nine-year partnership focusing on applications, platforms, and infrastructure.\n\nIn 2016, Salesforce announced that it will use Amazon Web Services hosting for countries with restrictive data residency requirements and where no Salesforce data centers are operating.\n\nCybersecurity incidents\n\n2007 Phishing attack\n\nIn November 2007, a phishing attack compromised contact information on a number of Salesforce customers. Some customers then received phishing emails that appeared to be invoices from Salesforce. A Salesforce employee's credentials were stolen through social engineering. Salesforce stated the incident resulted from human manipulation rather than a software vulnerability in its platform.\n\n2022 Heroku OAuth token theft (Salesforce subsidiary)\n\nOn April 13, 2022, GitHub notified Heroku of unauthorized access to its systems through a compromised OAuth token. Heroku immediately revoked all affected tokens and notified customers to update their credentials.\n\n2025-2026 ShinyHunters targeted campaigns against Salesforce\n\nShinyHunters has conducted several widespread data theft and extortion campaigns against Salesforce and thousands of its customers as noted by Google's Threat Intelligence Group/Mandiant, Salesforce, and the FBI.\n\nUNC6040 Modified Data Loader / Vishing - ShinyHunters threat actors executed a social engineering (security) campaign in which employees were persuaded to install a tampered version of Salesforce Data Loader. The Trojan horse (computing) client functioned as a malware dropper, enabling credential theft, unauthorized access, and large-scale data exfiltration, which was subsequently used for extortion against multiple organizations. Salesforce confirmed the campaign abused user trust and vishing techniques, clarifying that no vulnerability in the Salesforce platform itself was exploited.\n\nShinyHunters/UNC6395 threat actors compromised OAuth and refresh tokens through the Salesloft-Drift integration, enabling unauthorized access to Salesforce customer instance. In response, Salesforce and Salesloft revoked all affected Drift tokens and removed the application software from AppExchange pending investigation.\n\nShinyHunters/UNC6395 threat actors compromised another OAuth and refresh tokens through Gainsight integration, enabling unauthorized access to Salesforce customer instances. In response, Salesforce and Gainsight revoked all their integration apps pending further investigation.\n\nSalesforce released another major security advisory linking a \"known threat group\", believed to be ShinyHunters, to exploiting misconfigurations in their Salesforce Experience Cloud software. The hacking group claimed responsibility for these data theft attacks and issued a warning to affected Salesforce customers to pay up or their data would be leaked. The hacking group claimed to have breached about 400 companies.\n\nControversies\n\n‘Meatpistol’ presenters fired at Def Con\n\nIn 2017, two Salesforce security engineers were fired after giving a presentation at DEF CON discussing a Salesforce pentesting framework called MEATPISTOL. MEATPISTOL was a Salesforce-developed exploit framework similar to (and named after) Metasploit. Salesforce had previously planned to open source the framework, but changed plans just before the presentation, and fired them immediately afterward The presenters were sent a message half an hour before the presentation telling them to cancel the talk, but they did not see the message until afterward. The terminated employees called on the company to open-source the software after being dismissed.\n\nRAICES donation refusal\n\nIn 2018, the not-for-profit organization Refugee and Immigrant Center for Education and Legal Services (RAICES) rejected a US$250,000 donation from Salesforce unless the company ended its technology services to U.S. Customs and Border Protection. RAICES claimed accepting funds from a company which supported immigration enforcement conflicted with its mission to advocate for immigrant and refugee rights. Salesforce declined to end their relationship with US Customs, and issued a statement saying the company did not support separating migrant families. Salesforce offered to donate $1 million to help families who were separated.\n\n2018 taxes\n\nAccording to an Institute on Taxation and Economic Policy analysis published in December 2019, Salesforce paid no federal income tax on its 2018 profits, achieving a 0% effective tax rate. The report attributed this to provisions in the 2017 Tax Cuts and Jobs Act of 2017 and available tax credits and deductions. These findings were published in a report based on the 379 Fortune 500 companies that declared a profit in 2018.\n\nSex-trafficking lawsuit\n\nIn March 2019, Salesforce faced a lawsuit by 50 anonymous women claiming to be victims and survivors of sex trafficking, abuse, and rape, alleging the company profited from and helped build technology that facilitated sex trafficking on the now-defunct Backpage.com. In March 2021, a judge granted partial dismissal of the case, dismissing charges of negligence and conspiracy, but allowed the case to proceed regarding charges of sex trafficking. In March 2024, the case was dismissed without prejudice, meaning the plaintiffs could potentially refile their claims in the future. In September 2024, the US Court of Appeals for the Ninth Circuit denied a motion to reverse the dismissal.\n\nDisability discrimination lawsuit in Japan\n\nIn July 2021, a former Salesforce Japan employee sued the company in Tokyo District Court, alleging discrimination based on disabilities (autism and ADHD), including denial of reasonable workplace accommodations. At that time,"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q941127",
  "label": "Salesforce",
  "description": "American cloud-based software company",
  "aliases": [
   "Salesforce.com, Inc.",
   "SFDC",
   "salesforce.com"
  ],
  "claims": {
   "P31": [
    "Q4830453",
    "Q1058914",
    "Q6881511",
    "Q891723",
    "Q18388277",
    "Q183888"
   ],
   "P361": [
    "Q242345",
    "Q1546793",
    "Q180816"
   ]
  },
  "revision_id": "2570721250",
  "value_labels": {
   "Q4830453": "business",
   "Q1058914": "software company",
   "Q6881511": "enterprise",
   "Q891723": "public company",
   "Q18388277": "technology company",
   "Q183888": "software developer",
   "Q242345": "S&P 500",
   "Q1546793": "S&P 100",
   "Q180816": "Dow Jones Industrial Average"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q115602131",
  "label": "Salesforce",
  "description": "Suite of cloud-based applications, including CRM, sales, artificial intelligence, analytics, and API software.",
  "aliases": [],
  "claims": {
   "P31": [
    "Q95988573",
    "Q1143070",
    "Q1318054",
    "Q787422",
    "Q1665471",
    "Q5135601",
    "Q1358071",
    "Q141113981",
    "Q48997925",
    "Q7100437"
   ]
  },
  "revision_id": "2562559942",
  "value_labels": {
   "Q95988573": "customer relationship management software",
   "Q1143070": "software suite",
   "Q1318054": "enterprise software",
   "Q787422": "automation technology",
   "Q1665471": "integration platform",
   "Q5135601": "cloud-based integration",
   "Q1358071": "virtual agent",
   "Q141113981": "Freemium software",
   "Q48997925": "customer data platform",
   "Q7100437": "Order management system"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110262554",
  "label": "Salesforce",
  "description": "Dedicated Stack Exchange community site for Salesforce administrators, implementation experts, developers, and customers.",
  "aliases": [],
  "claims": {
   "P31": [
    "Q110256698"
   ]
  },
  "revision_id": "2395030803",
  "value_labels": {
   "Q110256698": "Stack Exchange forum site"
  },
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
  "ancestor_of": "Q941127",
  "level": 1,
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
  "ancestor_of": "Q941127",
  "level": 1,
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
  "ancestor_of": "Q941127",
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
  "ancestor_of": "Q941127",
  "level": 1,
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
  "ancestor_of": "Q941127",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q183888",
  "label": "software developer",
  "description": "person or company concerned with facets of the software development process",
  "aliases": [
   "software development engineer",
   "software developers",
   "software studio"
  ],
  "claims": {
   "P31": [
    "Q28640",
    "Q4164871",
    "Q108300140",
    "Q12737077"
   ],
   "P279": [
    "Q1709010",
    "Q108289400"
   ],
   "P460": [
    "Q5482740"
   ],
   "P1889": [
    "Q115641904",
    "Q125251322",
    "Q140466775"
   ]
  },
  "revision_id": "2556172704",
  "ancestor_of": "Q941127",
  "level": 1,
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
  "ancestor_of": "Q941127",
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
  "ancestor_of": "Q941127",
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
  "ancestor_of": "Q941127",
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
  "ancestor_of": "Q941127",
  "level": 2,
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
  "ancestor_of": "Q941127",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3409269",
  "label": "statistical unit",
  "description": "in statistics, anything that can be described and considered separately",
  "aliases": [
   "item",
   "entity"
  ],
  "claims": {
   "P31": [
    "Q595523"
   ],
   "P279": [
    "Q2198779"
   ],
   "P361": [
    "Q1172284"
   ],
   "P1889": [
    "Q112052376"
   ]
  },
  "revision_id": "2548372336",
  "ancestor_of": "Q941127",
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
  "ancestor_of": "Q941127",
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
  "ancestor_of": "Q941127",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28640",
  "label": "profession",
  "description": "occupation requiring specialized training",
  "aliases": [
   "craft"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q12737077"
   ],
   "P1889": [
    "Q12737077",
    "Q4164871",
    "Q828803",
    "Q192581"
   ]
  },
  "revision_id": "2569515027",
  "ancestor_of": "Q941127",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4164871",
  "label": "position",
  "description": "social role with a set of powers and responsibilities within an organization",
  "aliases": [
   "office",
   "function",
   "post",
   "officeholder",
   "station",
   "mantle",
   "title",
   "occupational role",
   "occupation role"
  ],
  "claims": {
   "P279": [
    "Q141749534",
    "Q141523012"
   ],
   "P361": [
    "Q192581"
   ],
   "P460": [
    "Q11488158",
    "Q480319"
   ],
   "P1889": [
    "Q480319",
    "Q12737077",
    "Q28640",
    "Q11348",
    "Q192581"
   ]
  },
  "revision_id": "2564400349",
  "ancestor_of": "Q941127",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q108300140",
  "label": "occupation group according to ISCO-08",
  "description": "group of occupations in the ISCO 08 classification of the International Labour Organisation",
  "aliases": [
   "ISCO occupation group"
  ],
  "claims": {
   "P31": [
    "Q828962"
   ],
   "P279": [
    "Q140287352"
   ]
  },
  "revision_id": "2570249158",
  "ancestor_of": "Q941127",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12737077",
  "label": "occupation",
  "description": "label applied to a person based on an activity they participate in",
  "aliases": [
   "occupations",
   "non-professional work activities",
   "non-professional work activity",
   "job",
   "profession",
   "work"
  ],
  "claims": {
   "P31": [
    "Q151885",
    "Q937228"
   ],
   "P279": [
    "Q1807498",
    "Q24902509",
    "Q141250146"
   ],
   "P527": [
    "Q656365"
   ],
   "P1889": [
    "Q28640",
    "Q4164871",
    "Q25475921",
    "Q1914636",
    "Q192581",
    "Q627436",
    "Q214339",
    "Q188686",
    "Q189533"
   ]
  },
  "revision_id": "2566756161",
  "ancestor_of": "Q941127",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q95988573",
  "label": "customer relationship management software",
  "description": "software application that enables management of an organization's relationships with its current and prospective customers",
  "aliases": [
   "CRM software",
   "customer relationship management tool",
   "CRM tool",
   "customer relationship management application",
   "CRM application",
   "CRM system",
   "CRM app"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q1391080"
   ]
  },
  "revision_id": "2558638321",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1143070",
  "label": "software suite",
  "description": "set of interrelated software packages developed with a broader intent",
  "aliases": [
   "application suite",
   "suite",
   "software collection",
   "software set",
   "software group",
   "software tool set",
   "software tool kit",
   "software toolkit",
   "suite of programs"
  ],
  "claims": {
   "P279": [
    "Q7397"
   ],
   "P527": [
    "Q40056"
   ],
   "P1889": [
    "Q1995545"
   ]
  },
  "revision_id": "2492919043",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1318054",
  "label": "enterprise software",
  "description": "software targeted towards corporations/organisations",
  "aliases": [
   "Enterprise Application Software",
   "EAS"
  ],
  "claims": {
   "P279": [
    "Q7397"
   ],
   "P1889": [
    "Q66086501"
   ]
  },
  "revision_id": "2318589620",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q787422",
  "label": "automation technology",
  "description": "interdisciplinary branch of engineering and engineering science",
  "aliases": [
   "technology of automation",
   "automatic control"
  ],
  "claims": {
   "P31": [
    "Q1047113",
    "Q112057532"
   ],
   "P361": [
    "Q11023"
   ]
  },
  "revision_id": "2548152267",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1665471",
  "label": "integration platform",
  "description": "software which integrates different applications and services",
  "aliases": [],
  "claims": {},
  "revision_id": "2420577914",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5135601",
  "label": "cloud-based integration",
  "description": "systems integration delivered as a cloud computing service",
  "aliases": [
   "integration platform as a service",
   "iPaaS"
  ],
  "claims": {},
  "revision_id": "2070723145",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1358071",
  "label": "virtual agent",
  "description": "characters in a virtual environment equipped with artificial intelligence",
  "aliases": [
   "intelligent virtual agent"
  ],
  "claims": {},
  "revision_id": "2337590703",
  "ancestor_of": "Q115602131",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q141113981",
  "label": "Freemium software",
  "description": "Wikimedia category",
  "aliases": [],
  "claims": {
   "P31": [
    "Q4167836"
   ]
  },
  "revision_id": "2532606355",
  "ancestor_of": "Q115602131",
  "level": 1,
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
  "ancestor_of": "Q115602131",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1391080",
  "label": "business software",
  "description": "software program used to perform various business functions",
  "aliases": [
   "specialist application",
   "specialized application",
   "business application"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q166142"
   ],
   "P460": [
    "Q135494458"
   ]
  },
  "revision_id": "2564315413",
  "ancestor_of": "Q115602131",
  "level": 2,
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
  "ancestor_of": "Q115602131",
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
  "ancestor_of": "Q115602131",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q112057532",
  "label": "type of technology",
  "description": "Wikidata metaclass, used as \"instance of\" for every \"subclass of\" technology",
  "aliases": [
   "technology type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ]
  },
  "revision_id": "2542124180",
  "ancestor_of": "Q115602131",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4167836",
  "label": "Wikimedia category",
  "description": "use with 'instance of' (P31) for Wikimedia category",
  "aliases": [
   "project category",
   "Project:Categorization",
   "Project:Category",
   "category page",
   "Wikimedia category page",
   "Wikipedia category",
   "wmcat",
   "category",
   "cat",
   "p31cat",
   "catp31",
   "category (Wikimedia)",
   "WM category",
   "Wikinews:Categories",
   "Categories",
   "wiki cat",
   "Commons category"
  ],
  "claims": {
   "P31": [
    "Q56005592",
    "Q4656150"
   ],
   "P279": [
    "Q12139612",
    "Q17442446",
    "Q118555179"
   ],
   "P361": [
    "Q118559258"
   ],
   "P1889": [
    "Q42104522",
    "Q64549097",
    "Q15647814",
    "Q59541917",
    "Q118559258",
    "Q224414",
    "Q4989342"
   ]
  },
  "revision_id": "2572760714",
  "ancestor_of": "Q115602131",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110256698",
  "label": "Stack Exchange forum site",
  "description": "site belonging to the Stack Exchange network of forums",
  "aliases": [],
  "claims": {
   "P279": [
    "Q168210",
    "Q1076547",
    "Q7265244"
   ],
   "P361": [
    "Q3495447"
   ]
  },
  "revision_id": "2549281679",
  "ancestor_of": "Q110262554",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q168210",
  "label": "Internet forum",
  "description": "online discussion site",
  "aliases": [
   "message board",
   "forum",
   "bulletin board",
   "discussion group",
   "discussion board",
   "web forum",
   "online bulletin board",
   "discussion space",
   "discussion site",
   "Internet bulletin board",
   "discussion forum",
   "online forum",
   "electronic discussion groups"
  ],
  "claims": {
   "P31": [
    "Q6055843",
    "Q134995802"
   ],
   "P279": [
    "Q35127",
    "Q1668024",
    "Q6576792",
    "Q202833"
   ]
  },
  "revision_id": "2561154136",
  "ancestor_of": "Q110262554",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1076547",
  "label": "knowledge market",
  "description": "mechanism for distributing knowledge resources",
  "aliases": [],
  "claims": {
   "P279": [
    "Q11016",
    "Q37654"
   ],
   "P460": [
    "Q7265244",
    "Q17077007"
   ]
  },
  "revision_id": "2515893691",
  "ancestor_of": "Q110262554",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7265244",
  "label": "question-and-answer site",
  "description": "genre of information website",
  "aliases": [
   "question-and-answer website",
   "Q&A site",
   "Q&A website"
  ],
  "claims": {
   "P31": [
    "Q134995802"
   ],
   "P279": [
    "Q35127"
   ],
   "P527": [
    "Q189756"
   ],
   "P460": [
    "Q1076547"
   ],
   "P1889": [
    "Q50988419"
   ]
  },
  "revision_id": "2539432209",
  "ancestor_of": "Q110262554",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 2: User experience design (`sixghka9vw`)

~~~~text
Concept record:
{
 "id": "sixghka9vw",
 "preferred_name": "User experience design",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [
  {
   "label": "UX design"
  },
  {
   "label": "user experience"
  },
  {
   "label": "User Experience Design (UX)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "v059qbltq4",
  "name": "Customer experience strategy"
 },
 {
  "id": "s8e0grtfer",
  "name": "Mobile UX design"
 },
 {
  "id": "k6v44yitma",
  "name": "Screen design"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "enec00k7dc",
  "name": "User research"
 },
 {
  "id": "mgli64p2b6",
  "name": "Digital accessibility"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "xrhig81x22",
  "name": "User interface design"
 },
 {
  "id": "c0jc22ifx0",
  "name": "Human factors"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "f2phqfe4e5",
  "name": "Ideation"
 },
 {
  "id": "fl0mme2six",
  "name": "Motion graphics"
 },
 {
  "id": "rv0h309eu3",
  "name": "Psychology"
 },
 {
  "id": "ag3vzgxdjd",
  "name": "Learner experience design"
 },
 {
  "id": "mcht0iu6qf",
  "name": "Google UX Design Professional Certificate"
 },
 {
  "id": "z9o1drq4m4",
  "name": "Color, material and finish design"
 },
 {
  "id": "qx1zxjygen",
  "name": "Printed circuit board design"
 },
 {
  "id": "bzumolh62w",
  "name": "API design"
 },
 {
  "id": "kokxhnhui7",
  "name": "Design of experiments"
 },
 {
  "id": "sno6247mi1",
  "name": "Logo design"
 },
 {
  "id": "r8kn0vxljj",
  "name": "Game design"
 },
 {
  "id": "j95dttpz2w",
  "name": "Chip design"
 },
 {
  "id": "zbpnwo0rf3",
  "name": "Print design"
 },
 {
  "id": "uufvn4ie3x",
  "name": "Voice UI design"
 },
 {
  "id": "afgwin6zn7",
  "name": "Plant design"
 },
 {
  "id": "wyr81cjqol",
  "name": "Business excellence"
 },
 {
  "id": "r6evkrcg5x",
  "name": "Mobile UI design"
 },
 {
  "id": "j6lwkq5kwl",
  "name": "Equipment design"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:17",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: User Experience Designer. User Experience Designer Power is seeking a User Experience Designer to join the team at our HQ office outside of Philadelphia, PA. This designer will have the ability to define how internal users will interact with our homegrown systems. We are looking for a collaborative UX designer, with front en…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:310",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Senior UI UX Designer. [\"UX Design\", \"UI Design\", \"Application Development\", \"Website Design\", \"Product Design\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:15567",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "UI/UX, ux, UX Design"
 },
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:855",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Staff Product Designer. user experience|ai|ml|go"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:2408",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: DCS DeltaV Analyst @ Pune. DeltaV, DCS, UI/UX designer, Analyst, Emerson, User interface designing, UI, UX Design"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[
 {
  "title": "User experience design",
  "revision_id": "1375528842",
  "matched_by": "title",
  "text": "User experience design (UX design, UXD, UED, or XD), upon which is the centralized requirements for \"User Experience Design Research\" (also known as UX Design Research), defines the experience a user would go through when interacting with a company, its services, and its products. User experience design is a user centered design approach because it considers the user's experience when using a product or platform. Research, data analysis, and test results drive design decisions in UX design rather than aesthetic preferences and opinions, for which is known as UX Design Research. Unlike user interface design, which focuses solely on the design of a computer interface, UX design encompasses all aspects of a user's perceived experience with a product or website, such as its usability, usefulness, desirability, brand perception, and overall performance. UX design is also an element of the customer experience (CX), and encompasses all design aspects and design stages that are around a customer's experience.\n\nHistory\n\nUser experience design is a conceptual design discipline rooted in human factors and ergonomics. This field since the late 1940s has focused on the interaction between human users, machines, and contextual environments to design systems that address the user's experience. User experience became a positive insight for designers in the early 1990s with the proliferation of workplace computers. Don Norman, a professor and researcher in design, usability, and cognitive science, coined the term \"user experience\", and brought it to a wider audience that is inside our modernized society. \n\nI invented the term because I thought human interface and usability were too narrow. I wanted to cover all aspects of the person's experience with the system including industrial design graphics, the interface, the physical interaction and the manual. Since then the term has spread widely, so much so that it is starting to lose its meaning.\n— Donald Norman\n\nElements\n\nResearch\n\nUser experience design draws from design approaches like human-computer interaction and user-centered design. It includes elements from similar disciplines like interaction design, visual design, information architecture, user research, and others.\n\nAnother portion of the research is understanding the end-user and the purpose of the application. Though this might seem clear to the designer, stepping back and empathizing with the user will yield the best results.\n\nIt helps to identify and prove or disprove assumptions, find commonalities across target audience members, and recognize their needs, goals, and mental models.\n\nVisual design\n\nVisual design, also commonly known as graphic design, user interface design, communication design, and visual communication, represents the aesthetics or look and feel of the front end of any user interface. Graphic treatment of interface elements is often perceived as the visual design. The purpose of visual design is to use visual elements like colors, images, and symbols to convey a message to its audience. Fundamentals of Gestalt psychology and visual perception give a cognitive perspective on how to create effective visual communication.\n\nInformation architecture\n\nInformation architecture is the art and science of structuring and organizing the information in products and services to support usability and findability.\n\nIn the context of information architecture, information is separate from both knowledge and data, and lies nebulously between them. It is information about objects. The objects can range from websites, to software applications, to images et al. It is also concerned with metadata, or data used to describe and represent content objects such as documents, people, process, and organizations. Information architecture also encompasses how the pages and navigation are structured.\n\nInteraction design\n\nInteraction design is an essential component of user experience (UX) design, that focuses on the interaction between users and products. The primary goal of interaction design is to create a product that produces an efficient and delightful end-user experience by enabling users to achieve their objectives in the best way possible.\n\nThe growing emphasis on user-centered design and the importance of delivering a strong user experience have made interaction designers increasingly important in creating products that meet user expectations while following current UI patterns and design standards.\n\nIn the last few years, the role of interaction designer has shifted from being just focused on specifying UI components and communicating them to the engineers to a situation in which designers have more freedom to design contextual interfaces based on helping meet the user's needs. Therefore, User Experience Design evolved into a multidisciplinary design branch that involves multiple technical aspects from motion graphics design, animation. programming to even service design.\n\nUsability\n\nUsability is the extent to which a product can be used by specified users to achieve specified goals with effectiveness, efficiency and satisfaction in a specified context of use.\n\nUsability is attached to all tools used by humans and is extended to both digital and non-digital devices. Thus, it is a subset of user experience but not wholly contained. The section of usability that intersects with user experience design is related to humans' ability to use a system or application. Good usability is essential to positive user experience but does not alone guarantee it.\n\nAccessibility\n\nAccessibility of a system describes its ease of reach, use, and understanding. In terms of user experience design, it can also be related to the overall comprehensibility of the information and features. It helps shorten the learning curve associated with the system. Accessibility in many contexts can be related to the ease of use for people with disabilities and comes under usability. In addition, accessible design is the concept of services, products, or facilities in which designers should accommodate and consider for the needs of people with disabilities. The Web Content Accessibility Guidelines (WCAG) state that all content must adhere to the four main principles of POUR: Perceivable, Operable, Understandable, and Robust.\n\nWCAG compliance\n\nWeb Content Accessibility Guidelines (WCAG) 2.0 covers a wide range of recommendations for making Web content more accessible. This makes web content more usable to users in general. Making content more usable and readily accessible to all types of users enhances a user's overall user experience.\n\nHuman–computer interaction\n\nHuman–computer interaction is concerned with the design, evaluation and implementation of interactive computing systems for human use and with the study of major phenomena surrounding them.\n\nGetting ready to design\n\nAfter research, the designer uses the modeling of the users and their environments. User modeling or personas are composite archetypes based on behavior patterns uncovered during research. Personas provide designers a precise way of thinking and communicating about how groups of users behave, how they think, what they want to accomplish and why. Once created, personas help the designer to understand the users' goals in specific contexts, which is particularly useful during ideation and for validating design concepts. Other types of models include workflow models, artifact models, and physical models.\n\nDesign\n\nWhen the designer has a solid understanding of the user's needs and goals, they begin to sketch out the interaction framework (also known as wireframes). This stage defines the high-level structure of screen layouts, as well as the product's flow, behavior, and organization. There are many kinds of materials that can be involved during this iterative phase, from whiteboards to paper prototypes. As the interaction framework establishes an overall structure for product behavior, a parallel process focused on the visual and industrial designs. The visual design framework defines the experience attributes, visual language, and the visual style.\n\nOnce a solid and stable framework is established, wireframes are translated from sketched storyboards to full-resolution screens that depict the user interface at the pixel level. At this point, it is critical for the programming team to collaborate closely with the designer. Their input is necessary to create a finished design that can and will be built while remaining true to the concept.\n\nUser research\n\nUser research is the systematic study of target users and their requirements in order to add realistic contexts and insights to the design process. It commonly involves methods such as interviews, surveys, field studies, and contextual inquiry. The data gathered from user research helps designers understand user goals, behaviors, and pain points, which in turn informs design decisions throughout the product lifecycle. By grounding design choices in evidence rather than assumptions, user research reduces the risk of creating products that fail to meet user needs. It also supports the creation of user personas and scenarios, which help maintain a user-centered focus during design and development.\n\nUX deliverables\n\nUX designers perform a number of different tasks and, therefore, use a range of deliverables to communicate their design ideas and research findings to stakeholders. Regarding UX specification documents, these requirements depend on the client or the organization involved in designing a product. The four major deliverables are: a title page, an introduction to the feature, wireframes, and a version history. Depending on the type of project, the specification documents can also include flow models, cultural models, personas, user stories, scenarios, and any prior user research.\n\nThe deliverables that UX designers will produce as part of their job include wireframes, prototypes, user flow diagrams, specification and tech docs, websites and applications, mockups, presentations, personas, user profiles, videos, and, to a lesser degree, reports. Documenting design decisions, in the form of annotated wireframes, gives the developer the necessary information they may need to successfully code the project.\n\nAfter launching a project\n\nRequires:\n\nUser testing/usability testing\n\nA/B testing\n\nInformation architecture\n\nSitemaps and user flows\n\nAdditional wireframing as a result of test results and fine-tuning\n\nPixel perfect\n\nPixel perfect, or pixel-perfect precision, is a term used in web development to describe that a digital product appears accurately as intended by the user interface or user experience designer.\n\nUX stakeholders\n\nA user experience designer is considered a UX practitioner, along with the following job titles: user experience researcher, information architect, interaction designer, human factors engineer, business analyst, consultant, creative director, interaction architect, and usability specialist.\n\nInteraction designers\n\nInteraction designers (IxD) are responsible for understanding and specifying how the product should behave. This work overlaps with the work of both visual and industrial designers in a couple of important ways. When designing physical products, interaction designers must work with industrial designers early on to specify the requirements for physical inputs and to understand the behavioral impacts of the mechanisms behind them. Interaction designers cross paths with visual designers throughout the project. Visual designers guide the discussions of the brand and emotive aspects of the experience, Interaction designers communicate the priority of information, flow, and functionality in the interface.\n\nTechnical communicators\n\nHistorically, technical and professional communication (TPC) has been as an industry that practices writing and communication. However, recently UX design has become more prominent in TPC as companies look to develop content for a wide range of audiences and experiences. It is now an expectation that technical and professional skills should be coupled with UX design. According to Verhulsdonck, Howard, and Tham, \"...it is not enough to write good content. According to industry expectations, next to writing good content, it is now also crucial to design good experiences around that content.\" Technical communicators must now consider different platforms such as social media and apps, as well as different channels like web and mobile. \n\nUX writers\n\nIn a similar manner, coupling TPC with UX design allows technical communicators to garner evidence on target audiences. UX writers, a branch of technical communicators, specialize in crafting content for mobile platforms while executing a user-centered approach. UX writers focus on developing content to guide users through interfaces, applications, and websites. Their responsibilities include maintaining UI text, conducting user research for usability testing, and developing the tone for a product's communication.\n\nUX writers maintain the practices of technical communicators, by developing documentation that establishes consistency in terminology and tone, promoting a cohesive user experience. However, beyond the writing, UX writers maintain UI text by ensuring that microscopy, such as button labels, error messages, and tooltips, remains user-friendly, as well. In doing this, the writers are also tasked with ensuring accessibility—considering issues like screen reader compatibility or providing non-text elements, such as icons. UX writers conduct extensive research to understand the behaviors and preferences of the target audience through user testing and feedback analysis. These methods of research can include user persona creation and user surveys. Lastly, when setting the tone in a product's communication, UX writers highlight factors that affect user engagement and perception. In short, the writers consider the product's emotional impact on the users, and align the tone with brand's personality.\n\nWithin the field of UX design, UX writers bridge the gaps between various fields to create a cohesive and user-centric experience. Their expertise in language and communication work to unify design, development, and user research teams by ensuring that the user interface's content aligns with the broader objectives of the product or service. By focusing on clarity, consistency, and empathy, UX writers contribute to the integration of design elements, technical functionality, and user preferences, while following a design process to ensure products with intuitive, accessible, and responsive behavior to user needs.\n\nUser interface designers\n\nUser interface (UI) design is the process of making interfaces in software or computerized devices with a focus on looks or style. Designers aim to create designs users will find easy to use and pleasurable. UI design typically refers to graphical user interfaces but also includes others, such as voice-controlled ones.\n\nVisual designers\n\nThe visual designer ensures that the visual representation of the design effectively communicates the data and hints at the expected behavior of the product. At the same time, the visual designer is responsible for conveying the brand ideals in the product and for creating a positive first impression; this responsibility is shared with the industrial designer if the product involves hardware. In essence, a visual designer must aim for maximum usability combined with maximum desirability. Visual designer need not be good in artistic skills but must deliver the theme in a desirable manner.\n\nUX design testing\n\nUsability testing is the most common method designers use to test their designs. The basic idea behind conducting a usability test is to check whether the design of a product or brand works well with the target users. Usability testing is about testing whether the product's design is successful and, if not, how it can be improved.\n\nWhile designers conduct tests, they are not testing for the user but for the design. Further, every design is evolving, with both UX design and design thinking moving in the direction of Agile software development. The designers carry out usability testing as early and often as possible, ensuring that every aspect of the final product has been tested.\n\nUsability tests play an important role in the delivery of a cohesive final product; however, a variety of factors influence the testing process. Evaluating qualitative and quantitative methods provides an adequate picture of UX designs, and one of these quantitative methods is A/B testing (see Usability testing). Another key concept in the efficacy of UX design testing is the idea of a persona or the representation of the most common user of a certain website or program, and how these personas would interact with the design in question. At the core of UX design usability testing is the user; however, steps in automating design testing have been made, with Micron developing the Advanced Test Environment (ATE), which automates UX tests on Android-powered smartphones. While quantitative software tools that collect actionable data, such as loggers and mobile agents, provide insight into a user's experience, the qualitative responses that arise from live, user based UX design testing are lost. The ATE serves to simulate a devices movement that affects design orientation and sensor operation in order to estimate the actual experience of the user based on previously collected user testing data.\n\nSee also"
 },
 {
  "title": "User experience",
  "revision_id": "1374010796",
  "matched_by": "title",
  "text": "User experience (UX) is how a user interacts with and experiences a product, system, or service. It includes a person's perceptions of utility, ease of use, and efficiency. Improving user experience is important to most companies, designers, and creators when creating and refining products because negative user experience can diminish the use of the product and, therefore, any desired positive impacts. Conversely, designing toward profitability as a main objective often conflicts with ethical user experience objectives and even causes harm. User experience is subjective. However, the attributes that make up the user experience are objective.\n\nDefinitions\n\nAccording to Nielsen Norman Group, 'user experience' includes all the aspects of the interaction between the end-user with the company, its services, and its products.\n\nThe international standard on ergonomics of human-system interaction, ISO 9241, defines user experience as a \"user's perceptions and responses that result from the use and/or anticipated use of a system, product or service\". According to the ISO definition, user experience includes all the users' emotions, beliefs, preferences, perceptions, physical and psychological responses, behaviors, and accomplishments that occur before, during, and after use. The ISO also lists three factors that influence user experience: the system, the user, and the context of use.\n\nNote 3 of the standard hints that usability addresses aspects of user experience, e.g., \"usability criteria can be used to assess aspects of user experience\". The standard does not go further in clarifying the relation between user experience and usability. Clearly, the two are overlapping concepts, with usability including pragmatic aspects (getting a task done) and user experience focusing on users' feelings stemming from both pragmatic and hedonic aspects of the system. Many practitioners use the terms interchangeably. The term \"usability\" pre-dates the term \"user experience\". Part of the reason the terms are often used interchangeably is that, as a practical matter, a user will, at a minimum, require sufficient usability to accomplish a task, while the feelings of the user may be less important, even to the user themselves. Since usability is about getting a task done, aspects of user experience like information architecture and user interface can help or hinder a user's experience. If a website has \"bad\" information architecture and a user has a difficult time finding what they are looking for, then the user will not have an effective, efficient, and satisfying search.\n\nIn addition to the ISO standard, there exist several other definitions for user experience. Some of them have been studied by various researchers.\n\nHistory\n\nEarly developments in user experience can be traced back to the Machine Age, which includes the 19th and early 20th centuries. Inspired by the machine age intellectual framework, the quest to improve assembly processes and increase production efficiency and output led to the development of major technological advancements, such as the mass production of high-volume goods on moving assembly lines, high-speed printing presses, large hydroelectric power plants, and radio technology, to name a few.\n\nFrederick Winslow Taylor and Henry Ford explored ways to make human labor more efficient and productive. Taylor's research into the efficiency of interactions between workers and their tools is the earliest example that resembles today's user experience fundamentals.\n\nThe term user experience was brought to wider knowledge by Donald Norman in the mid-1990s. He never intended the term \"user experience\" to be applied only to the affective aspects of usage. A review of his earlier work suggests that the term \"user experience\" was used to signal a shift to include affective factors, along with the pre-requisite behavioral concerns, which had been traditionally considered in the field. Many usability practitioners continue to research and attend to affective factors associated with end-users, and have been doing so for years, long before the term \"user experience\" was introduced in the mid-1990s. In an interview in 2007, Norman discusses the widespread use of the term \"user experience\" and its imprecise meaning as a consequence thereof.\n\nSeveral developments contributed to the rise of interest in user experience:\n\nRecent advances in mobile, ubiquitous, social, and tangible computing technologies have moved human-computer interaction into practically all areas of human activity. This has led to a shift away from usability engineering to a much richer scope of user experience, where users' feelings, motivations, and values are given as much, if not more, attention than efficiency, effectiveness, and basic subjective satisfaction (i.e., the three traditional usability metrics)\n\nIn website design, it was important to combine the interests of different stakeholders: marketing, branding, visual design, and usability. Marketing and branding people needed to enter the interactive world where usability was important. Usability people needed to take marketing, branding, and aesthetic needs into account when designing websites. User experience provided a platform to cover the interests of all stakeholders: making websites easy to use, valuable, and effective for visitors. This is why several early user experience publications focus on website user experience.\n\nThe field of user experience represents an expansion and extension of the field of usability to include the holistic perspective of how a person feels about using a system. The focus is on pleasure, value, and performance. The exact definition, framework, and elements of user experience are still evolving.\n\nUser experience of an interactive product or a website is usually measured by a number of methods, including questionnaires, focus groups, observed usability tests, user journey mapping and other methods. A freely available questionnaire (available in several languages) is the User Experience Questionnaire (UEQ). The development and validation of this questionnaire is described in a computer science essay published in 2008.\n\nHigher levels of user experience have been linked to increased effectiveness of digital health interventions targeting improvements in physical activity, nutrition, mental health and smoking.\n\nGoogle Ngram Viewer shows wide use of the term starting in the 1930s. \"He suggested that more follow-up in the field would be welcomed by the user, and would be a means of incorporating the results of the user's experience into the design of new machines.\" Use of the term in relation to computer software also pre-dates Norman.\n\nInfluences on user experience\n\nMany factors can influence a user's experience with a system. To address the variety, factors influencing user experience have been classified into three main categories: the user's state and previous experience, system properties, and the usage context (situation). Understanding representative users, working environments, interactions, and emotional reactions helps in designing the system during User experience design.\n\nMomentary emotion or overall user experience\n\nSingle experiences influence the overall user experience: the experience of a key click affects the experience of typing a text message, the experience of typing a message affects the experience of text messaging, and the experience of text messaging affects the overall user experience with the phone. The overall user experience is not simply a sum of smaller interaction experiences, because some experiences are more salient than others. Overall user experience is also influenced by factors outside the actual interaction episode: brand, pricing, friends' opinions, reports in the media, etc.\n\nOne branch of user experience research focuses on emotions. This includes momentary experiences during interaction: designing effective interaction and evaluating emotions. Another branch is interested in understanding the long-term relationship between user experience and product appreciation. The industry sees a good overall user experience with a company's products as critical for securing brand loyalty and enhancing the growth of the customer base. All temporal levels of user experience (momentary, episodic, and long-term) are important, but the methods to design and evaluate these levels can be very different.\n\nCritiques and ethical debates in user experience\n\nWhile user experience has become an essential part of design and product development, it has also attracted criticism and ethical scrutiny. Focusing on user satisfaction and business goals may lead to harmful design choices, unintentional accessibility gaps, or user manipulation. These conflicts suggest that UX has room to become a more responsible and inclusive practice.\n\nProfit versus people\n\nOne major critique of UX is the conflict between designing for user benefit and designing for business objectives. UX decisions are often shaped by financial incentives rather than users’ well-being. This leads to design choices that prioritize growth over ethics, for example, features that encourage excessive screen time, collect unnecessary personal data (also known as privacy zuckering), or make it difficult for users to unsubscribe from services (also known as forced continuity). While trying to increase profits, it may actually increase economic harm and reduce market efficiency. Critics argue that such practices compromise the foundational goal of UX, which is to improve the user's experience, not exploit it.\n\nCompanies can be held accountable for their design choices by prioritizing user interests. For instance, ensuring price transparency helps users make informed decisions. Organizations can also align design decisions with user well-being by evaluating qualitative outcomes, like how a product contributes to users’ happiness or mental health, instead of relying solely on engagement metrics. By making business success dependent on user trust and satisfaction, rather than engagement metrics alone, organizations can create sustainable products that support both profitability and user well-being.\n\nDark patterns and manipulative design\n\nAnother major ethical concern in UX is the use of dark patterns, interface designs that intentionally mislead or manipulate users into taking actions they might not otherwise choose. Examples include use of checkboxes to opt out rather than opt in (double negatives), confusing cancellation processes, or “confirm” buttons that lead to unintended purchases. Scholars from Princeton and Purdue University have argued that dark patterns represent a misuse of UX principles, using psychological insights and interface design against user interests.\n\nOne proposed solution to the problem of dark patterns is to focus on how to distinguish manipulative patterns from legitimate persuasion. For example, researchers at Princeton suggest using guidelines to evaluate when a design crosses the line into manipulation. Researchers from Purdue University instead argue that ethical awareness cannot rely solely on codes of conduct but should instead focus on the designer’s intent, judgment, and ongoing responsibility. \n\nInclusivity and accessibility gaps\n\nAnother area of criticism concerns accessibility and inclusivity in UX design. Although improving usability is a central aim of UX, many products and services continue to overlook the needs of people with disabilities, older users, or those from different cultural and linguistic backgrounds. This exclusion can occur due to implicit bias in design teams, lack of diverse user testing, or assumptions about “average” users. \n\nTo address these gaps, experts recommend adopting inclusive design principles throughout the development process. This includes conducting accessibility audits, following the Web Content Accessibility Guidelines (WCAG), and involving users with disabilities in usability testing to ensure products meet real-world needs. Expanding user research to include diverse groups can also uncover assumptions and biases early. Additionally, ongoing education about unconscious bias for design teams can help create products that reflect a broader range of user experiences.\n\nDeveloper experience\n\nDeveloper experience (DX) is a user experience from a developer's point of view. It is defined by the tools, processes, and software that a developer uses when interacting with a product or system while in the process of producing another one, such as in software development. DX has had increased attention paid to it, especially in businesses that primarily offer software as a service to other businesses, where ease of use is a key differentiator in the market.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q11248500",
  "label": "user experience design",
  "description": "field of design focusing on the creation of user centered products and services",
  "aliases": [
   "UxD",
   "UX design"
  ],
  "claims": {
   "P31": [
    "Q11862829"
   ],
   "P279": [
    "Q82604"
   ],
   "P361": [
    "Q19602141",
    "Q21198"
   ],
   "P460": [
    "Q3508531"
   ],
   "P1889": [
    "Q3508531"
   ]
  },
  "revision_id": "2524306003",
  "value_labels": {
   "Q11862829": "academic discipline",
   "Q82604": "design",
   "Q19602141": "human-centered design",
   "Q21198": "computer science",
   "Q3508531": "experience design"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1047808",
  "label": "user experience",
  "description": "discipline focused on improving a person’s interaction and experience with a product, system or service",
  "aliases": [
   "UX"
  ],
  "claims": {
   "P279": [
    "Q7451247"
   ],
   "P1889": [
    "Q47146"
   ]
  },
  "revision_id": "2568393854",
  "value_labels": {
   "Q7451247": "sentiment",
   "Q47146": "user interface"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q59667169",
  "label": "User experience design",
  "description": "article; DOI:10.6019/TOL.UX-C.2015.00001.1",
  "aliases": [],
  "claims": {
   "P31": [
    "Q13442814"
   ]
  },
  "revision_id": "2089999630",
  "value_labels": {
   "Q13442814": "scholarly article"
  },
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
  "ancestor_of": "Q11248500",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q82604",
  "label": "design",
  "description": "creation of a plan or convention for the construction of an object or a system; process of creation; act of creativity and innovation",
  "aliases": [
   "styling",
   "planning",
   "plan"
  ],
  "claims": {
   "P31": [
    "Q1047113",
    "Q627436",
    "Q11862829",
    "Q116505632",
    "Q119143679",
    "Q8187769"
   ],
   "P279": [
    "Q1914636",
    "Q104637332",
    "Q1519454"
   ],
   "P361": [
    "Q113129241"
   ],
   "P460": [
    "Q1519454"
   ],
   "P1889": [
    "Q1462272",
    "Q398628"
   ]
  },
  "revision_id": "2567321824",
  "ancestor_of": "Q11248500",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110402867",
  "label": "knowledge classification",
  "description": "Wikidata metaclass",
  "aliases": [
   "knowledge classification system",
   "classification system of knowledge"
  ],
  "claims": {
   "P31": [
    "Q121344523"
   ],
   "P279": [
    "Q5962346"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2569936517",
  "ancestor_of": "Q11248500",
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
  "ancestor_of": "Q11248500",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q627436",
  "label": "field of work",
  "description": "particular area of activity in industry and science",
  "aliases": [],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q1047113",
    "Q451967"
   ],
   "P460": [
    "Q11862829"
   ],
   "P1889": [
    "Q44597158",
    "Q12737077"
   ]
  },
  "revision_id": "2562948765",
  "ancestor_of": "Q11248500",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q116505632",
  "label": "type of process",
  "description": "Wikidata metaclass of process",
  "aliases": [
   "process type"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q142077035"
   ],
   "P361": [
    "Q58778"
   ],
   "P1889": [
    "Q138611570"
   ]
  },
  "revision_id": "2566753342",
  "ancestor_of": "Q11248500",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7451247",
  "label": "sentiment",
  "description": "general thought, feeling, or sense",
  "aliases": [],
  "claims": {
   "P279": [
    "Q160402",
    "Q12558574"
   ],
   "P460": [
    "Q205555",
    "Q3962655"
   ]
  },
  "revision_id": "2552883843",
  "ancestor_of": "Q1047808",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q160402",
  "label": "perception",
  "description": "organization, identification, and interpretation of sensory information in order to represent and understand the environment in the brain",
  "aliases": [
   "human perception",
   "human observation",
   "perceptual process"
  ],
  "claims": {
   "P31": [
    "Q41172303",
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q12047513",
    "Q855395",
    "Q5720030"
   ],
   "P361": [
    "Q77468620",
    "Q4338318",
    "Q21142755"
   ],
   "P527": [
    "Q3955369"
   ],
   "P460": [
    "Q12774262"
   ]
  },
  "revision_id": "2572573971",
  "ancestor_of": "Q1047808",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12558574",
  "label": "point of view",
  "description": "standpoint regarding a topic; opinion, attitude, or judgment upon some matter; way that one looks at something",
  "aliases": [
   "perspective",
   "point of view (philosophy)",
   "POV",
   "point of observation",
   "position",
   "viewpoint",
   "standpoint",
   "view",
   "outlook",
   "Attitude"
  ],
  "claims": {
   "P279": [
    "Q595523",
    "Q2145290"
   ],
   "P361": [
    "Q77468620"
   ],
   "P527": [
    "Q12578182"
   ],
   "P460": [
    "Q109361341",
    "Q3962655",
    "Q12331437"
   ],
   "P1889": [
    "Q117850"
   ]
  },
  "revision_id": "2550955583",
  "ancestor_of": "Q1047808",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q13442814",
  "label": "scholarly article",
  "description": "article in an academic publication, usually peer reviewed",
  "aliases": [
   "article",
   "academic paper",
   "research paper",
   "scientific paper",
   "scholarly paper",
   "academic article",
   "article in science",
   "collection of articles",
   "scientific article",
   "data article"
  ],
  "claims": {
   "P31": [
    "Q133449656",
    "Q39725049"
   ],
   "P279": [
    "Q591041",
    "Q191067",
    "Q10383930",
    "Q12042160",
    "Q30070590"
   ],
   "P1889": [
    "Q18918145",
    "Q23927052",
    "Q97012313",
    "Q223729",
    "Q1266946",
    "Q114613919",
    "Q36774"
   ]
  },
  "revision_id": "2561179091",
  "ancestor_of": "Q59667169",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q133449656",
  "label": "type of work",
  "description": "",
  "aliases": [],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257",
    "Q96251598"
   ]
  },
  "revision_id": "2561225663",
  "ancestor_of": "Q59667169",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q39725049",
  "label": "type of publication",
  "description": "Wikidata metaclass for the characteristics of a publication, e. g. the way in which a work is published",
  "aliases": [
   "form of publication",
   "kind of publication",
   "publication type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q16889133",
    "Q65770524",
    "Q133449656"
   ],
   "P1889": [
    "Q65770524"
   ]
  },
  "revision_id": "2561225548",
  "ancestor_of": "Q59667169",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q591041",
  "label": "scientific publication",
  "description": "publication that reports empirical or theoretical work in the sciences",
  "aliases": [
   "scholarly publication"
  ],
  "claims": {
   "P31": [
    "Q39725049"
   ],
   "P279": [
    "Q732577",
    "Q47461344",
    "Q11826511",
    "Q12042160",
    "Q55915575"
   ],
   "P527": [
    "Q4119870",
    "Q265158",
    "Q1713"
   ]
  },
  "revision_id": "2567595781",
  "ancestor_of": "Q59667169",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q191067",
  "label": "article",
  "description": "written work forming an independent part of a publication such as a journal, newspaper, or magazine",
  "aliases": [
   "periodical article",
   "journal article",
   "serial article",
   "magazine article"
  ],
  "claims": {
   "P31": [
    "Q4263830",
    "Q39725049"
   ],
   "P279": [
    "Q234460",
    "Q47461344",
    "Q732577",
    "Q49848",
    "Q88392887",
    "Q111955339"
   ],
   "P361": [
    "Q732577"
   ],
   "P527": [
    "Q1313396",
    "Q1425760",
    "Q8776414",
    "Q28747765"
   ],
   "P1889": [
    "Q12244562",
    "Q21622417",
    "Q111478",
    "Q123196740",
    "Q123196765",
    "Q123196802",
    "Q123196880",
    "Q18918145"
   ]
  },
  "revision_id": "2566533370",
  "ancestor_of": "Q59667169",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
