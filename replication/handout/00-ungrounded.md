# Skills Lexicon pilot, ungrounded run: message 1 of 13 (chunk 00, 36 concepts)

Everything you need is in this message. Don't fetch, search or look anything up. Draft only from what is here and what you already know.

**Independence.** Several models are drafting these same 36 entries separately so Nik Bear Brown can compare them. Don't read, search for or ask for any other model's drafts, including Claude's. The material below is source material only (the lexicon's record, candidate neighbors, posting snippets); it holds no one's drafts.

**How to work.** Treat each concept on its own, as if you had never seen the others: don't carry a decision, a wording or a relation from one concept to the next. This is the **ungrounded** run: the Wikipedia, Wikidata and WordNet lists are empty on purpose.

**Instructions for every concept** (use them exactly as written):

~~~~text
You draft entries for Skills Lexicon, an open vocabulary of skills, knowledge areas, abilities, languages, and credentials used to match job postings with course syllabi. You receive one concept and a bundle of source material. You return one JSON object.

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
`"_meta": {"model": "<your model and version>", "run": "ungrounded", "chunk": "00", "attempts": 1}`.
If you can make files, send a file named `drafts-ungrounded-00.jsonl`. Otherwise send one code block marked `jsonl` holding the 36 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 36: PostgreSQL (`sh6x1wmacn`)

~~~~text
Concept record:
{
 "id": "sh6x1wmacn",
 "preferred_name": "PostgreSQL",
 "kind": "tool",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Postgres"
  },
  {
   "label": "PG",
   "needs_context": [
    "database"
   ]
  }
 ],
 "relations": [
  {
   "type": "broader",
   "target": "f69xny35zm",
   "target_name": "SQL"
  }
 ]
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "f69xny35zm",
  "name": "SQL"
 },
 {
  "id": "onzi0v8hlf",
  "name": "PL/pgSQL"
 },
 {
  "id": "wrn21idyay",
  "name": "Relational database management system"
 },
 {
  "id": "p98xjhlkpu",
  "name": "Ingres"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "sai8akfwpi",
  "name": "Database systems"
 },
 {
  "id": "a9vdp0px7b",
  "name": "Kotlin"
 },
 {
  "id": "ecoz6ylymx",
  "name": "Statistics"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "h00skqgqmn",
  "name": "Amazon Web Services"
 },
 {
  "id": "w9n8sme4x4",
  "name": "B-tree"
 },
 {
  "id": "x4397709dt",
  "name": "CSS"
 },
 {
  "id": "kp84ig38m5",
  "name": "Database design"
 },
 {
  "id": "z5cl5m7b48",
  "name": "Certified Professional Geologist"
 },
 {
  "id": "wpe22ejvkt",
  "name": "Pug"
 },
 {
  "id": "gue4rsxccu",
  "name": "JPEG"
 },
 {
  "id": "evzc8xqwgr",
  "name": "Postorder traversal"
 },
 {
  "id": "setvh9dhil",
  "name": "PostCSS"
 },
 {
  "id": "ll3qkk2jdu",
  "name": "Field-programmable gate array"
 },
 {
  "id": "e6d3w0bi1i",
  "name": "Portuguese"
 },
 {
  "id": "buwx6qk7uh",
  "name": "OpenEdge ABL"
 },
 {
  "id": "bdi5yd5igv",
  "name": "TIBCO Spotfire"
 },
 {
  "id": "v7niczl5ii",
  "name": "nosetests"
 },
 {
  "id": "ja1oge4jc3",
  "name": "Pinterest"
 },
 {
  "id": "f7c96nvfei",
  "name": "Surgery"
 },
 {
  "id": "wnnm0zmdx4",
  "name": "Programmer's Hierarchical Interactive Graphics System"
 },
 {
  "id": "uacnrdn102",
  "name": "MSTest"
 },
 {
  "id": "jzl6qyfnik",
  "name": "Greeks (finance)"
 },
 {
  "id": "wiyjakztr1",
  "name": "Plastic surgery"
 },
 {
  "id": "z5bkl6uo0o",
  "name": "OutSystems"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:265",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Technical Lead (Kotlin/ Java/ Spring ecosystem). [\"Kotlin\", \"Java\", \"GraphQL APIs\", \"PostgreSQL\", \"Leadership\", \"Java\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:857",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "PHP, MySQL, PostgreSQL"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:189",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Data Engineer. …ts and to the appropriate data sources. DRIVIN has a polyglot data model using many cutting-edge data platforms. We are currently using MPP Postgres (Greenplum, Netezza, DBX) as our Data Warehouse, Elastic Search for location based searching, Postgres for transactional data. This candidate should be…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:143",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Software Developer. …p, enhance, and deliver features for our ERP platform across both frontend and backend systems. 2. Work extensively with Java, Spring Boot, PostgreSQL, and React to build scalable solutions that address real-world business challenges. 3. Take end-to-end ownership of assigned features, from requireme…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:73",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Full Stack Java Developer- DHS Clearance. …n front-end technologies such as HTML, CSS, JavaScript, and modern UI frameworks Experience with relational and/or NoSQL databases (Oracle, PostgreSQL, MongoDB) Familiarity with cloud platforms (AWS, Azure, or GCP) and containerization tools (Docker, Kubernetes) Experience working in Agile developme…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 36: Python (`pk7cebmtg6`)

~~~~text
Concept record:
{
 "id": "pk7cebmtg6",
 "preferred_name": "Python",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Python (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "wpvzxxfp8w",
  "name": "ActivePython"
 },
 {
  "id": "swfjde2n0t",
  "name": "Biopython"
 },
 {
  "id": "rtrc1foglt",
  "name": "CPython"
 },
 {
  "id": "e6wzlsvhig",
  "name": "Cython"
 },
 {
  "id": "vk2k09kvlq",
  "name": "IPython"
 },
 {
  "id": "y3lbnh790j",
  "name": "IronPython"
 },
 {
  "id": "wrobx5q3f7",
  "name": "PyMongo"
 },
 {
  "id": "ta8z97c7vx",
  "name": "VPython"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "i0vpvmxbz0",
  "name": "Object-oriented programming"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "h00skqgqmn",
  "name": "Amazon Web Services"
 },
 {
  "id": "bum8cg3i92",
  "name": "Azure DevOps"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "d9sq04v2o1",
  "name": "Extract, transform, load"
 },
 {
  "id": "zceu8ud0dw",
  "name": "Haskell"
 },
 {
  "id": "wi51wbsa9k",
  "name": "wxPython"
 },
 {
  "id": "n9dorj1s29",
  "name": "PHP"
 },
 {
  "id": "n29960itit",
  "name": "Go"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "jzczt8njk2",
  "name": "Forth"
 },
 {
  "id": "ec5sjzxk6h",
  "name": "Dylan"
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
  "id": "qfyv8hdypt",
  "name": "Boo"
 },
 {
  "id": "oeixkjthc3",
  "name": "R"
 },
 {
  "id": "eaovn4ljeo",
  "name": "D"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. …onment. We hope you like it as much as we do. Requirements: 4+ years of experience as a DevOps Engineer At least 3 years of experience with Python or Bash 3+ years of experience with AWS/GCP/Microsoft Azure/Azure DevOps is required Experience in at least 2 commercial projects using Terraform, Kubern…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:20",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Expert, Data Engineer - TechcomLife. [\"Python\", \"Data Engineer\", \"ETL Processes\", \"Debugging\", \"Database Technologies\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:3",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Software Engineer - Innovation Lab. …ence as a software engineer. Strong development experience in C, C , Java. Developing systems applications on Linux/Android. Comfortable in Python language. Experience or knowledge in Artificial Intelligence Ability to take ideas from concept to prototype. Ability to vet technical requirements from …"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:19",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "Back-end, Python, SQL, Django"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:53",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Record To Report Ops Analyst. accounts reconciliation, python, sql, stakeholder management, record to report, data analytics, data management, service operations"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 36: Docker (`g5lqkx80zn`)

~~~~text
Concept record:
{
 "id": "g5lqkx80zn",
 "preferred_name": "Docker",
 "kind": "platform",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "h00skqgqmn",
  "name": "Amazon Web Services"
 },
 {
  "id": "bum8cg3i92",
  "name": "Azure DevOps"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "norpz7ekiw",
  "name": "Cybersecurity"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "h60l8olauw",
  "name": "JavaScript"
 },
 {
  "id": "ihoes4l8q2",
  "name": "Linux systems administration"
 },
 {
  "id": "sh6x1wmacn",
  "name": "PostgreSQL"
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
  "id": "yikd65o35c",
  "name": "Socket 5"
 },
 {
  "id": "xyi17s2fy2",
  "name": "CKEditor"
 },
 {
  "id": "e4ky74p3dr",
  "name": "Rockmelt"
 },
 {
  "id": "d4tfwk03xy",
  "name": "Destoner"
 },
 {
  "id": "z8kpukjtt0",
  "name": "Spock Framework"
 },
 {
  "id": "u0kostamek",
  "name": "Certified Diabetes Care and Education Specialist"
 },
 {
  "id": "tplmkvcg50",
  "name": "Ceros"
 },
 {
  "id": "prkfpz7o8w",
  "name": "Esker"
 },
 {
  "id": "oemj81pym1",
  "name": "jMock"
 },
 {
  "id": "eili48vgqq",
  "name": "Khmer"
 },
 {
  "id": "ae50wmbiia",
  "name": "Keras"
 },
 {
  "id": "eaovn4ljeo",
  "name": "D"
 },
 {
  "id": "mjyk2ua8d3",
  "name": "CDC Cyber"
 },
 {
  "id": "ztfqr0o2n3",
  "name": "IBM POWER7"
 },
 {
  "id": "xvxyocp9rg",
  "name": "Oberon"
 },
 {
  "id": "wmkik8ucw1",
  "name": "SockJS"
 },
 {
  "id": "vanjr7jvuv",
  "name": "Cerner"
 },
 {
  "id": "pwau7gon42",
  "name": "Resorcerer"
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
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:113",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Chuyên Viên Tối Ưu Thiết Kế Hạ Tầng Cloud. [\"Docker\", \"AI\", \"Cloud\", \"Cloud AWS\", \"AI\", \"Docker\", \"Docker\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:58",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "DevOps, Docker, CI/CD, Linux, Gitlab"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:125",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Software Engineer in Test (Big Data/Cloud). …ce with large data processing tools such as Hadoop, HBase, ElasticSearch, RabbitMQ, and Kafka Experience with Python, Java, Tomcat, JS, and Docker is a plus Experience testing network security products, preferably with firewalls and intrusion prevention is a plus BS or MS in computer engineering or …"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:4448",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Azure DevOps Engineer. …dules for infrastructure components like compute, networking, storage, and databases. D. Containers & Orchestration 1. Configure and manage Docker and Kubernetes workloads. 2. Handle deployments, services, ingress configuration, scaling, and troubleshooting of containerized applications. E. Security…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 4 of 36: Java (`ls6hrpynv0`)

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
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 5 of 36: JavaScript (`h60l8olauw`)

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
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 6 of 36: C (`a0h79b66kq`)

~~~~text
Concept record:
{
 "id": "a0h79b66kq",
 "preferred_name": "C",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "C (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "jeai1j8uhz",
  "name": "French"
 },
 {
  "id": "eon43rmtrr",
  "name": "Greek"
 },
 {
  "id": "k8e22lk68i",
  "name": "Writing"
 },
 {
  "id": "y8idko4c9n",
  "name": "Italian"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "de8aeltv9z",
  "name": "Spanish"
 },
 {
  "id": "b53t6y9iys",
  "name": "Catalan"
 },
 {
  "id": "hj8i6mh3zz",
  "name": "Chinese"
 },
 {
  "id": "x09au1cwqd",
  "name": "Danish"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "xzbzidj6js",
  "name": "Japanese"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "j0bdoceeet",
  "name": "Ladder logic"
 },
 {
  "id": "dbxqhrpv38",
  "name": "C#"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
 },
 {
  "id": "qb4qnsutxp",
  "name": "C++"
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
  "id": "ybdv7l9ewb",
  "name": "Hack"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "n29960itit",
  "name": "Go"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "rw1cn65xyv",
  "name": "COBOL"
 },
 {
  "id": "rfrqfpigh3",
  "name": "OCaml"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:877",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Embedded Project Manager (Japanese Or Chinese Speaking). [\"Embedded Software\", \"Japanese Speaking\", \"Project Management\", \"Automotive\", \"C\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:126",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Transportation Modeler/Engineer. …hnical assistance, as required. Qualifications Solid analytical, quantitative, and problem solving skills. Hands-on experience with Python, C, or other programming languages. Knowledge of the principles of traffic engineering, econometrics, statistics, or computer science that is applicable to trans…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:6",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Entry-Level Modeling and Data Analysis Engineer (Electrical, Aerospace, Physics Degree). …cal modeling, simulation, and analysis work. *Software Skills* Experience with one or more of the following is desired: * MATLAB * Python * C/C++ Experience developing engineering scripts, processing technical datasets, or creating analysis and visualization tools through academic projects, internsh…"
 },
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:262",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Risk Reporting Specialist, AS. c++, python, c, investment banking, market risk, matlab, digital marketing, risk management"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 7 of 36: C++ (`qb4qnsutxp`)

~~~~text
Concept record:
{
 "id": "qb4qnsutxp",
 "preferred_name": "C++",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "C++ (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "x09au1cwqd",
  "name": "Danish"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "hzccoii598",
  "name": "Arithmetic"
 },
 {
  "id": "dwchdo7ntf",
  "name": "Assembly language"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "kut5s14k79",
  "name": "Collaboration"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "fa900jy3j1",
  "name": "Floating-point arithmetic"
 },
 {
  "id": "a0h79b66kq",
  "name": "C"
 },
 {
  "id": "dbxqhrpv38",
  "name": "C#"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
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
  "id": "ybdv7l9ewb",
  "name": "Hack"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "n29960itit",
  "name": "Go"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "rw1cn65xyv",
  "name": "COBOL"
 },
 {
  "id": "rfrqfpigh3",
  "name": "OCaml"
 },
 {
  "id": "r9tfnc7x3j",
  "name": "CLIST"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:34",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: RPA Developer. [\"RPA\", \"UI Path\", \".Net\", \"Java\", \"C++\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:3",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Software Engineer - Innovation Lab. Software Development, Infotainment Systems, Augmented Reality (AR), Heads-up Display (HUD), Haptic Devices, Platform Optimization, Cross-functional Collaboration, Proof of Concept (PoC), System Application Development, Linux/Android Development, Programming Languages: C, C++, Java, Python, Artificia…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:714",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "C++, embedded"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:262",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Risk Reporting Specialist, AS. c++, python, c, investment banking, market risk, matlab, digital marketing, risk management"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 8 of 36: C# (`dbxqhrpv38`)

~~~~text
Concept record:
{
 "id": "dbxqhrpv38",
 "preferred_name": "C#",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "C Sharp"
  },
  {
   "label": "C Sharp (Programming Language)"
  },
  {
   "label": "C# (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "tbtzl802aq",
  "name": "ReSharper"
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
  "id": "qb4qnsutxp",
  "name": "C++"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "ly6jzdmqwz",
  "name": "Delphi"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "kcu5dpjinp",
  "name": "Eiffel"
 },
 {
  "id": "iip9ks8y55",
  "name": "Objective-C"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "x80b957frq",
  "name": "Ada"
 },
 {
  "id": "dwchdo7ntf",
  "name": "Assembly language"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "a0h79b66kq",
  "name": "C"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "uct8ix3rbg",
  "name": "Tcl"
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
  "id": "ybdv7l9ewb",
  "name": "Hack"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "n29960itit",
  "name": "Go"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "rw1cn65xyv",
  "name": "COBOL"
 },
 {
  "id": "rfrqfpigh3",
  "name": "OCaml"
 },
 {
  "id": "r9tfnc7x3j",
  "name": "CLIST"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:104",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "ASP.NET Core, Entity Framework, C#, Sql Server"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:479",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Nhân Viên Lập Trình (IT Development). [\"MySQL\", \"C#\", \"VB.NET\", \"HTML\", \"ASP.Net\"]"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:442",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Software Engineer. …cience, or Mathematics • Zero (0) to three (3) years of experience is required. • NAS experience is desired. Required Skills • Knowledge of C#. • Ability to: • Work independently, as well as on a team, in a fast-paced environment. • Navigate complex workflows; research and problem solve; willingness…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1139",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: C# Developer. C#, IT services, SAN, Head Business Development, PDF, SOC, SMS, digital transformation"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 9 of 36: Angular (`fcadn3ihwg`)

~~~~text
Concept record:
{
 "id": "fcadn3ihwg",
 "preferred_name": "Angular",
 "kind": "framework",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "swlrwigph5",
  "name": "Angular CLI"
 },
 {
  "id": "mnlgauzi32",
  "name": "AngularJS"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "y37j4kl3jo",
  "name": "TypeScript"
 },
 {
  "id": "d4xxm6t88j",
  "name": "DevOps"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
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
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "op6iieveb7",
  "name": "Bash"
 },
 {
  "id": "f0c784bzd2",
  "name": "ngAnimate"
 },
 {
  "id": "k87r3b7xk8",
  "name": "Bengali"
 },
 {
  "id": "ciqcmsfd1o",
  "name": "Hungarian"
 },
 {
  "id": "hupkg1mnsj",
  "name": "Aurelia"
 },
 {
  "id": "cxpxcuw3gh",
  "name": "Anaplan"
 },
 {
  "id": "b2291n6joq",
  "name": "Lingala"
 },
 {
  "id": "z199mo1bdd",
  "name": "Fula"
 },
 {
  "id": "vks1qiiz57",
  "name": "Ainu"
 },
 {
  "id": "w8wmeqph17",
  "name": "Manipuri"
 },
 {
  "id": "vphlc8dpfb",
  "name": "Mandarin"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "hth5eczuzx",
  "name": "Gujarati"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "z09tq03hir",
  "name": "Analysis of variance"
 },
 {
  "id": "ynw7yrzobc",
  "name": "Benga"
 },
 {
  "id": "yk1fji8zbq",
  "name": "Associate of Arts in Art"
 },
 {
  "id": "xstca7bdbk",
  "name": "Amazon SageMaker"
 },
 {
  "id": "xayt8bhrdg",
  "name": "AI guardrails"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:121",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "C#, Angular, Sql Server, C#, Angular, Sql Server"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:76",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Chuyên Gia Kiến Trúc Ứng Dụng - Solution Architect - Khối Công Nghệ Thông Tin (2025TD942). [\"Angular\", \"Angular\", \"Angular\", \"Microservice\", \"Oracle\", \"Redis\", \"Spring\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:148",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: L3 SAN Storage Engineer. …patterns affect storage (LUN Q-Depth, multipathing, application IO size, etc…). Development skill sets including: Python, Cloud frameworks, Angular, and a mindset for automation is a plus."
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:4585",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Java Developer. Key Responsibilities: 1. Develop and maintain high-quality software solutions using Java, Spring MVC, Hibernate, Angular 7.0, and MySQL. 2. Collaborate with cross-functional teams to design, develop, and test software applications. 3. Participate in code reviews and provide constructive feedback to …"
 },
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:15",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior DevOps Engineer. devops|.net|android|aws|azure|c|c#|c++|data science|golang|ios|java|javascript|kubernetes|node.js|php|python|react|ruby/rails|scala|shopify|sql|swift|ui/ux|wordpress|blockchain|ai/ml|automation|project management|react native|rust|product management|unity|electron|spring|data analysis|bash|laravel|e…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 10 of 36: AngularJS (`mnlgauzi32`)

~~~~text
Concept record:
{
 "id": "mnlgauzi32",
 "preferred_name": "AngularJS",
 "kind": "framework",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Angular.js"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "fcadn3ihwg",
  "name": "Angular"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "h60l8olauw",
  "name": "JavaScript"
 },
 {
  "id": "bzg3r9ulfm",
  "name": "BIND"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "y37j4kl3jo",
  "name": "TypeScript"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "x4397709dt",
  "name": "CSS"
 },
 {
  "id": "pl9ucmohz5",
  "name": "Express.js"
 },
 {
  "id": "q89d2f20gq",
  "name": "Node.js"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "ojeubzzg6x",
  "name": "Gulp.js"
 },
 {
  "id": "swlrwigph5",
  "name": "Angular CLI"
 },
 {
  "id": "v4wdughw0p",
  "name": "Handlebars.js"
 },
 {
  "id": "k87r3b7xk8",
  "name": "Bengali"
 },
 {
  "id": "d868fdr68x",
  "name": "Scala.js"
 },
 {
  "id": "rnblhw89i9",
  "name": "CanvasJS"
 },
 {
  "id": "f0mg2qvhta",
  "name": "Nuxt"
 },
 {
  "id": "cf2acgxwct",
  "name": "MEAN.JS"
 },
 {
  "id": "f0c784bzd2",
  "name": "ngAnimate"
 },
 {
  "id": "vjw6nn9z7a",
  "name": "CanJS"
 },
 {
  "id": "v00xfjkjpc",
  "name": "Chart.js"
 },
 {
  "id": "hxclrzb8sy",
  "name": "Bacon.js"
 },
 {
  "id": "cvjjttyqe3",
  "name": "Sails.js"
 },
 {
  "id": "xayt8bhrdg",
  "name": "AI guardrails"
 },
 {
  "id": "xwrfu2zstu",
  "name": "NW.js"
 },
 {
  "id": "p98xjhlkpu",
  "name": "Ingres"
 },
 {
  "id": "n3e2gcdwp6",
  "name": "pandas"
 },
 {
  "id": "ciqcmsfd1o",
  "name": "Hungarian"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:963",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: .NET Full Stack Developer. [\"ReactJS\", \"Full Stack Development\", \"C#\", \"AngularJS\", \".NET\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:229",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Big Data Software Engineer. … CentOS, installing, troubleshooting and command-line scripting. Knowledge of restful APIs (creating and consuming) is helpful Knowledge of AngularJS, jQuery, nodeJS is helpful Desire to learn existing and new technologies around the Big Data space Responsibilities Selecting and integrating any Big …"
 },
 {
  "id": "dev122/internshala-jobs-dataset@v1/JobData.csv:11",
  "source": "kaggle:dev122/internshala-jobs-dataset (CC0: Public Domain), column Description",
  "text": "Job title: Angular.js Development Intern (Remote). … day-to-day responsibilities include: 1. Collaborate with the development team to design and implement user-friendly web applications using AngularJS, HTML, CSS, and Redux 2. Write clean, maintainable, and efficient code 3. Utilize Redux for state management within AngularJS applications 4. Develop …"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:4872",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Full Stack Developer. .NET,MongoDB,AngularJS,Node.js,PostgreSQL,Express.js,React,"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:11856",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": ".NET Core, AngularJS, typescript, OOP, Object Oriented, MVC, webservice, SQL"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 11 of 36: R (`oeixkjthc3`)

~~~~text
Concept record:
{
 "id": "oeixkjthc3",
 "preferred_name": "R",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "R (Programming Language)"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "eon43rmtrr",
  "name": "Greek"
 },
 {
  "id": "e6d3w0bi1i",
  "name": "Portuguese"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "k8e22lk68i",
  "name": "Writing"
 },
 {
  "id": "x6bugydux5",
  "name": "English Language"
 },
 {
  "id": "jeai1j8uhz",
  "name": "French"
 },
 {
  "id": "goirkloj73",
  "name": "Gaelic"
 },
 {
  "id": "de8aeltv9z",
  "name": "Spanish"
 },
 {
  "id": "p7j275wpwg",
  "name": "Albanian"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "h00skqgqmn",
  "name": "Amazon Web Services"
 },
 {
  "id": "gmnxfnk0xv",
  "name": "Elixir"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
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
  "id": "vp6szkok86",
  "name": "Dart"
 },
 {
  "id": "s3rdirqwq6",
  "name": "Ruby"
 },
 {
  "id": "gaqvznkz28",
  "name": "Perl"
 },
 {
  "id": "e0p0dbx59q",
  "name": "Rust"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "n29960itit",
  "name": "Go"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "dbxqhrpv38",
  "name": "C#"
 },
 {
  "id": "n2v8jnsgj0",
  "name": "XBRL"
 },
 {
  "id": "jzczt8njk2",
  "name": "Forth"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:8",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Analytics Engineer. …or business intelligence tools such as Tableau or Power BI Knowledge of AWS Tools and Python is a plus Knowledge of analytics tools such as R is a plus Experience working collaboratively on a team with aggressive deadlines Strong project and time management, as well as written and proactive communic…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:1464",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Senior Drug Checking Epidemiologist, Bureau of Alcohol and Drug Use. …or all drug checking data. 2. Extract, clean, manipulate, organize, and analyze data for the bureau’s Drug Checking Program using primarily R, REDCap, Excel and other platforms as needed. 3. Design, conduct, and develop new methods of analyses that will inform future directions of the Drug Checking …"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:2363",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Senior Data Analyst. [\"Data Analysis\", \"SQL\", \"Python\", \"ETL\", \"Statistics\", \"Power BI\", \"R\"]"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:342",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Data Scientist. time series analysis, python, sql coding, machine learning, r, data analytics, data analysis, natural language processing"
 },
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:40860",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: AI-Developer | REMOTE or in Paderborn, Ger | Time Series | R | Start-Up | Full-Time. AI-Developer | REMOTE or in Paderborn, Ger | Time Series | R | Start-Up | Full-Time You are thrilled by Artificial Intelligence? Then we are looking for you! Today we are developing the planning of tomorrow's logistics with intelligent IT solutions more effective than ever before! We are a small tea…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 12 of 36: Go (`n29960itit`)

~~~~text
Concept record:
{
 "id": "n29960itit",
 "preferred_name": "Go",
 "kind": "programming-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Go (Programming Language)"
  },
  {
   "label": "Golang"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "qb4qnsutxp",
  "name": "C++"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "ihoes4l8q2",
  "name": "Linux systems administration"
 },
 {
  "id": "jz619i5060",
  "name": "Logo"
 },
 {
  "id": "e0p0dbx59q",
  "name": "Rust"
 },
 {
  "id": "hzccoii598",
  "name": "Arithmetic"
 },
 {
  "id": "gxe2qfkmua",
  "name": "Branding"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "zc8shpqdop",
  "name": "Lingo"
 },
 {
  "id": "kb3pruwri8",
  "name": "Oz"
 },
 {
  "id": "k29flhnozy",
  "name": "ALGOL"
 },
 {
  "id": "qfyv8hdypt",
  "name": "Boo"
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
  "id": "e4tzaqhrc4",
  "name": "Groovy"
 },
 {
  "id": "xkyic5vgkn",
  "name": "J#"
 },
 {
  "id": "wonwpe2z38",
  "name": "F#"
 },
 {
  "id": "ub71msqw4l",
  "name": "Q#"
 },
 {
  "id": "np8jq1gkrj",
  "name": "F*"
 },
 {
  "id": "dbxqhrpv38",
  "name": "C#"
 },
 {
  "id": "rw1cn65xyv",
  "name": "COBOL"
 },
 {
  "id": "rfrqfpigh3",
  "name": "OCaml"
 },
 {
  "id": "jzczt8njk2",
  "name": "Forth"
 },
 {
  "id": "znqe62lhes",
  "name": "AWK"
 },
 {
  "id": "yl4tfx5kdt",
  "name": "Visual Basic for Applications"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:3",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Customer Support Manager. customer success|midweight|full-time|communication|kubernetes|linux|spark|ops|llm|ai|go"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:91",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Senior Software Engineer Fullstack. [\"Flutter\", \"Golang\", \"NextJs\", \"PYTHON\", \"ReactJs\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:46",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "Golang, Go, SQL, Git"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:174",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Data Engineer. … team members Qualifications 3+ years of development experience focusing around BigData 3+ years of development experience (Java, Scala, C, Golang, R) Experience building and deploying large scale ETL pipelines Degree in Computer Science, Math or equivalent experience Strong understanding of math, a…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:689",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Infrastructure Software Engineering Intern - Summer. …cloud services, or kubernetes. Instead, there is a lot of bare-metal linux, systemd, and single file binaries. You’ll see a lot of rust and go and occasionally some python. What matters most is that you’ve already built real things, you love getting close to the metal, and show strong signs of engin…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 13 of 36: Swift (`p1pplzvq0f`)

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
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 14 of 36: SQL (`f69xny35zm`)

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
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 15 of 36: Machine learning (`flxbx98seh`)

~~~~text
Concept record:
{
 "id": "flxbx98seh",
 "preferred_name": "Machine learning",
 "kind": "method",
 "broad_class": "skill",
 "variants": [
  {
   "label": "ML"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "bpi2rb7akn",
  "name": "CatBoost"
 },
 {
  "id": "ebn7tz5prh",
  "name": "PhD in Machine Learning"
 },
 {
  "id": "wng5g0t68d",
  "name": "Torch (machine learning)"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "r32hw0qken",
  "name": "k-means clustering"
 },
 {
  "id": "ag0hpcesx8",
  "name": "Large language models"
 },
 {
  "id": "tx96mffcus",
  "name": "Neural networks"
 },
 {
  "id": "ecoz6ylymx",
  "name": "Statistics"
 },
 {
  "id": "mi2t4wx6vw",
  "name": "Free Lossless Audio Codec"
 },
 {
  "id": "nw1oyk7q86",
  "name": "Deep learning"
 },
 {
  "id": "r5kwam4bm9",
  "name": "Reinforcement learning"
 },
 {
  "id": "zoh6kna5kw",
  "name": "Retrieval-augmented generation"
 },
 {
  "id": "fcadn3ihwg",
  "name": "Angular"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "hzccoii598",
  "name": "Arithmetic"
 },
 {
  "id": "g9gfriy1ec",
  "name": "scikit-learn"
 },
 {
  "id": "xubhw9lr07",
  "name": "Active Learning"
 },
 {
  "id": "va052jqj8q",
  "name": "UML"
 },
 {
  "id": "php2tc9p7y",
  "name": "XML"
 },
 {
  "id": "oezvmtjgl6",
  "name": "Keyhole Markup Language"
 },
 {
  "id": "z79armevpb",
  "name": "Margin lending"
 },
 {
  "id": "op8cesvddr",
  "name": "Distance learning"
 },
 {
  "id": "w1blu9iu00",
  "name": "Blended learning"
 },
 {
  "id": "r4s8o1u1q1",
  "name": "Active Listening"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "sg1xfslxld",
  "name": "Quick learning"
 },
 {
  "id": "obj0g7i1kl",
  "name": "MQL4"
 },
 {
  "id": "nprxj06a8r",
  "name": "Machine operation"
 },
 {
  "id": "i3i5khm667",
  "name": "MXML"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:7",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior Independent AI Engineer / Architect. …nd orchestration systems Enterprise AI deployments Retrieval, evaluation, and reliability infrastructure LLM-powered workflows and products Machine learning platforms operating at scale You'll work directly with founders, CTOs, and product leaders, helping shape both technical direction and executio…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:6",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Analyst - Angular. Automation, Data management, Performance management, Analytical, Machine learning, Javascript, Workflow, Business intelligence"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:4",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Director, Standards & Strategy. …ends in the Audio/Video content creation and distribution spaces, including AR and VR, and other emerging technology areas such as imaging, machine learning and artificial intelligence Consistent with 1, establish DTS technologies in the technical standards and industry consortia publications that a…"
 },
 {
  "id": "dev122/internshala-jobs-dataset@v1/JobData.csv:29",
  "source": "kaggle:dev122/internshala-jobs-dataset (CC0: Public Domain), column Description",
  "text": "Job title: Artificial Intelligence (AI) Intern (Remote). …laborate with senior AI developers to develop natural language processing and computer vision algorithms 2. Collect and preprocess data for machine learning models 3. Analyze and interpret the results of experiments 4. Document and communicate findings to the team 5. Stay up-to-date with the latest …"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:103",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Senior AI Engineer. …ge Models (LLMs) for domain-specific use cases. 2. Build and maintain Retrieval-Augmented Generation (RAG) pipelines. 3. Develop and expose machine learning models as REST APIs using FastAPI. 4. Design and develop intelligent chatbot systems. 5. Implement agentic AI workflows and multi-step reasonin…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 16 of 36: Natural language processing (`d168utcmjy`)

~~~~text
Concept record:
{
 "id": "d168utcmjy",
 "preferred_name": "Natural language processing",
 "kind": "method",
 "broad_class": "skill",
 "variants": [
  {
   "label": "NLP"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "k2fnt61kzq",
  "name": "Apache OpenNLP"
 },
 {
  "id": "gvwuv6xjpu",
  "name": "Natural language generation"
 },
 {
  "id": "erag95km1k",
  "name": "Natural language processing systems"
 },
 {
  "id": "ivx36sezid",
  "name": "Natural language understanding"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "oxu0hc83pv",
  "name": "Computer science"
 },
 {
  "id": "flxbx98seh",
  "name": "Machine learning"
 },
 {
  "id": "tx96mffcus",
  "name": "Neural networks"
 },
 {
  "id": "hj8i6mh3zz",
  "name": "Chinese"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "ag0hpcesx8",
  "name": "Large language models"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "enx40y6s0v",
  "name": "Speech Recognition"
 },
 {
  "id": "hwaf7og623",
  "name": "Doctor of Nursing Practice"
 },
 {
  "id": "gxbpx9za78",
  "name": "Neonatal Resuscitation Program"
 },
 {
  "id": "gkq7vbv3ql",
  "name": "npm"
 },
 {
  "id": "ap5dyxzh9v",
  "name": "Licensed Practical Nurse"
 },
 {
  "id": "bxl9tjsu5g",
  "name": "Mail processing"
 },
 {
  "id": "n4go9oimdg",
  "name": "spaCy"
 },
 {
  "id": "w49tfjhjw9",
  "name": "Claim processing"
 },
 {
  "id": "hfschl129h",
  "name": "Tulu"
 },
 {
  "id": "xbnzpi95t0",
  "name": "Language teaching"
 },
 {
  "id": "m4rbaj4f3l",
  "name": "Invoice processing"
 },
 {
  "id": "ciqcmsfd1o",
  "name": "Hungarian"
 },
 {
  "id": "b53t6y9iys",
  "name": "Catalan"
 },
 {
  "id": "zvfjqwa8g1",
  "name": "Production and Processing"
 },
 {
  "id": "zb709ig3an",
  "name": "Lisp"
 },
 {
  "id": "y13g58ujg8",
  "name": "Serial Line Internet Protocol"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:65",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Analyst. financial analysis, python, data analysis, data analytics, natural language processing, investment banking, business analysis, analysis"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:18",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Software Engineer. …ng information retrieval, distributed computing, large-scale system design, networking and data storage, security, artificial intelligence, natural language processing, UI design and mobile; the list goes on and is growing every day. As a software engineer, you will work on a specific project critic…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:197",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Senior Business Analyst (Ai/dữ Liệu/smart City). [\"Business Analysis\", \"Product Owner\", \"AI\", \"Embedded\", \"NLP\"]"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:1630",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Senior Manager, Data Science - AI Foundations. …LangChain, Lightning, VectorDBs, and more - to reveal the insights hidden within huge volumes of numeric and textual data. Be the expert in Natural Language Processing (NLP) to harness the power of Large Language Models (LLMs), adapt and finetune them for customer facing applications and features. B…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:18653",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "Python, NLP, Pytorch"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 17 of 36: Extract, transform, load (`d9sq04v2o1`)

~~~~text
Concept record:
{
 "id": "d9sq04v2o1",
 "preferred_name": "Extract, transform, load",
 "kind": "method",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Extraction, Transformation, and Loading (ETL)"
  },
  {
   "label": "ETL"
  },
  {
   "label": "Extraction, Transformation, and Loading"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "uclexd8uv3",
  "name": "Data validation"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "vf02rn80se",
  "name": "Cost accounting"
 },
 {
  "id": "ie3ky4o9l0",
  "name": "Data wrangling"
 },
 {
  "id": "kp84ig38m5",
  "name": "Database design"
 },
 {
  "id": "pmy0yp0e50",
  "name": "NoSQL database"
 },
 {
  "id": "f69xny35zm",
  "name": "SQL"
 },
 {
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "ocy9gvs6bk",
  "name": "Web crawling"
 },
 {
  "id": "php2tc9p7y",
  "name": "XML"
 },
 {
  "id": "ye2k9qi1x3",
  "name": "Certification in Transportation and Logistics"
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
  "id": "ot4pymzomt",
  "name": "Social-emotional learning"
 },
 {
  "id": "kdyyyj7yda",
  "name": "Engineer in Training"
 },
 {
  "id": "uhwnqf48he",
  "name": "Representational State Transfer"
 },
 {
  "id": "ubbk8mnwmv",
  "name": "WebCTRL"
 },
 {
  "id": "i4i1z8400a",
  "name": "Certified in Logistics, Transportation and Distribution"
 },
 {
  "id": "zyx43s2qb5",
  "name": "Air Travel Organisers' Licensing"
 },
 {
  "id": "wy0q8xbf4z",
  "name": "International Computer Driving Licence"
 },
 {
  "id": "uxw4bog89z",
  "name": "Certified Biomedical Equipment Technician"
 },
 {
  "id": "twhbebct5l",
  "name": "HTML"
 },
 {
  "id": "q9s4sj8gqa",
  "name": "Advanced Trauma Life Support"
 },
 {
  "id": "ixojaf13wa",
  "name": "Associate of Applied Science in Animation and CGI Motion"
 },
 {
  "id": "i6xjzm9oyc",
  "name": "Wilderness EMT"
 },
 {
  "id": "i6g7p06d2d",
  "name": "Earth leakage circuit breaker"
 },
 {
  "id": "hfschl129h",
  "name": "Tulu"
 },
 {
  "id": "gaqvznkz28",
  "name": "Perl"
 },
 {
  "id": "fbgyvaz7qh",
  "name": "Scholarship of teaching and learning"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:4",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Senior Independent Software Developer. software development|go|wordpress|chat|apple|testing|catalyst|etl|ai"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:8",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Analytics Engineer. …nsparent, and repeatable solutions. You fluently explain complex ideas to colleagues and customers. Responsibilities Execute data analysis, ETL, and data mining to support customer deployments Configure enterprise analytics platform and tools Work closely with customer delivery teams with mixed back…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:527",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: [Hà Nội, HCM] Chuyên Gia/chuyên Viên Phê Duyệt Tín Dụng Cấp 1-2-3. [\"Azure Data Services\", \"ETL\", \"Khai Thác Dữ Liệu\", \"Phân Tích Dữ Liệu\", \"Quản Trị Dữ Liệu\"]"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:1320",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "تحلیل داده, هوش تجاری, T-SQL, ETL"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1671",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Record To Report Ops Analyst. journal entries, accounting, extract transform load, record to report, etl, service operations, informatica powercenter, forecasting"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 18 of 36: Application programming interface (`xe2d2jfa1r`)

~~~~text
Concept record:
{
 "id": "xe2d2jfa1r",
 "preferred_name": "Application programming interface",
 "kind": "knowledge",
 "broad_class": "knowledge",
 "variants": [
  {
   "label": "API"
  },
  {
   "label": "APIs"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "zwm9kkpnld",
  "name": "Box API"
 },
 {
  "id": "u301ax2wc3",
  "name": "OpenAPI Specification"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "uhwnqf48he",
  "name": "Representational State Transfer"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "twiey8e4zm",
  "name": "Fortran"
 },
 {
  "id": "ztt7xizgr8",
  "name": "Scala"
 },
 {
  "id": "h00skqgqmn",
  "name": "Amazon Web Services"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "kp84ig38m5",
  "name": "Database design"
 },
 {
  "id": "rjc04xak59",
  "name": "Flutter"
 },
 {
  "id": "ivq3fs6epa",
  "name": "Lua"
 },
 {
  "id": "evbr3hj7wv",
  "name": "hapi"
 },
 {
  "id": "bzumolh62w",
  "name": "API design"
 },
 {
  "id": "v7rwb3jmgy",
  "name": "API gateway"
 },
 {
  "id": "lpxeil9yyg",
  "name": "WASAPI"
 },
 {
  "id": "ogt8lrbjfc",
  "name": "API management"
 },
 {
  "id": "ev4fuqqcd5",
  "name": "ASCM certification"
 },
 {
  "id": "q8zepjtla7",
  "name": "Capistrano"
 },
 {
  "id": "j4u2uvtmvj",
  "name": "ReadyAPI"
 },
 {
  "id": "bnjsc5i3bq",
  "name": "eBay API"
 },
 {
  "id": "rivr9g4ool",
  "name": "Accountancy and Passenger Ticket Issuing System"
 },
 {
  "id": "nedtcwz5ap",
  "name": "Vulkan"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "z3rnxbom1d",
  "name": "LinkedIn API"
 },
 {
  "id": "m8l9rs4net",
  "name": "Deal shaping"
 },
 {
  "id": "dp6y03hiq5",
  "name": "Graphics API"
 },
 {
  "id": "aivu2hknkc",
  "name": "apxs"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:127",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Data Engineer. …ure data in warehouses and lakehouses to support reporting and analytics use cases. Integrate data from a wide range of sources: databases, APIs, third-party platforms, and event streams. Ensure data quality, reliability, and observability through testing, monitoring, and alerting. Optimize pipeline…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:319",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: QA Automation Engineer. MS SQL Server,MS-Excel,Scrum,Jira,Effective Communication,APIs,Software Development Life Cycle (SDLC),"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:523",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Solution Architect - Salary Up to $5000. [\"AWS\", \"APIs\", \"Solution Architecture\", \"Technical Architecture\", \"Databases\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:486",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Cloud Management Architect. …he group. This includes building a cloud-native architecture which is microservice based, running in containers, and providing well-defined API based services. We also need full-stack developers who have experience providing the best UX so the adoption by clients is seamless and painless. This is cr…"
 },
 {
  "id": "maminkheneifar/jobinja-job-listings-26k@v1/Jobinja - Processed.csv:2696",
  "source": "kaggle:maminkheneifar/jobinja-job-listings-26k (CC0: Public Domain), column Job Description",
  "text": "باهدف استعدادیابی و جذب علاقه مندان در سطح مقدماتی و حرفه ای پذیرش انجام می شود.توانمندیهای تخصصی:• Flutter• API• Material Design• Gitساعت کاری:تایم اداریمکان فعالیت:باتوجه محل زندگی قابل انتخاب میباشد.شعبه مشهد ، شعبه تهران ، شعبه کیش(اقامتگاه مهیا میباشد)"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 19 of 36: Amazon Web Services (`h00skqgqmn`)

~~~~text
Concept record:
{
 "id": "h00skqgqmn",
 "preferred_name": "Amazon Web Services",
 "kind": "platform",
 "broad_class": "skill",
 "variants": [
  {
   "label": "AWS"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "gzok01cjvc",
  "name": "Amazon EMR"
 },
 {
  "id": "srtz4mtpnt",
  "name": "Amazon SimpleDB"
 },
 {
  "id": "cml6t35xqn",
  "name": "AWS Command Line Interface"
 },
 {
  "id": "lem0uww05d",
  "name": "AWS SDK"
 },
 {
  "id": "kli63uvu2s",
  "name": "Platform as a service"
 },
 {
  "id": "lpsnz8mgp5",
  "name": "Cloud computing"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "xe2d2jfa1r",
  "name": "Application programming interface"
 },
 {
  "id": "uhwnqf48he",
  "name": "Representational State Transfer"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "zvnr5iuxil",
  "name": "Operating systems"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "cfem7cgay7",
  "name": "Agile software development"
 },
 {
  "id": "pp0ifhxwtv",
  "name": "Alexa Internet"
 },
 {
  "id": "s1jyt2h0md",
  "name": "Amazon CloudWatch"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "e7v9azv69k",
  "name": "AWS Elastic Beanstalk"
 },
 {
  "id": "hh5zk4fi3o",
  "name": "AWS IoT"
 },
 {
  "id": "ry245wui4g",
  "name": "AWS Lambda"
 },
 {
  "id": "cmtuyx6c1u",
  "name": "AWS Cloud9"
 },
 {
  "id": "scnorb90o8",
  "name": "AWS big data"
 },
 {
  "id": "n6a28897om",
  "name": "AWS CloudHSM"
 },
 {
  "id": "kazbc7sp8z",
  "name": "AWS Outposts"
 },
 {
  "id": "hqhwu7b5ig",
  "name": "AWS OpsWorks"
 },
 {
  "id": "xstca7bdbk",
  "name": "Amazon SageMaker"
 },
 {
  "id": "lrg2eu09em",
  "name": "AWS CodeBuild"
 },
 {
  "id": "mldj16hibf",
  "name": "AWS CodeCommit"
 },
 {
  "id": "kba5p9by94",
  "name": "AWS CloudTrail"
 },
 {
  "id": "ft1f82qoac",
  "name": "AWS networking"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:6",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Vice President APAC - Customer Service & Support.. customer success|director|full-time|communication|excel|aws|git|ai|go"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:523",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Solution Architect - Salary Up to $5000. [\"AWS\", \"APIs\", \"Solution Architecture\", \"Technical Architecture\", \"Databases\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:104",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Technical Retail Experience Manager. …eferred Experience with managing retail app development 3 plus years of managing app (APK/IOS/Windows) development projects Experience with AWS cloud CMS is plus Experience with digital projects involving multi-devices or multi-screens is a plus Experience with IoT and Artificial Intelligence projec…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:73",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Full Stack Java Developer- DHS Clearance. … and modern UI frameworks Experience with relational and/or NoSQL databases (Oracle, PostgreSQL, MongoDB) Familiarity with cloud platforms (AWS, Azure, or GCP) and containerization tools (Docker, Kubernetes) Experience working in Agile development environments Strong communication skills and ability…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:424",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Marketing Data Scientist & AI Professional. python, microsoft azure, data science, gcp, aws, advance sql, ibm cloud, industry research"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 20 of 36: Communication (`gisypzf6gf`)

~~~~text
Concept record:
{
 "id": "gisypzf6gf",
 "preferred_name": "Communication",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "yzu8eoggb2",
  "name": "Digital communications"
 },
 {
  "id": "aa2ix4mtc5",
  "name": "Nonverbal communication"
 },
 {
  "id": "ybkdpu1cdn",
  "name": "PhD in Communication"
 },
 {
  "id": "kbj9m1t62c",
  "name": "Stakeholder communication"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "z83cabeb9c",
  "name": "Project management"
 },
 {
  "id": "s00v9m81ez",
  "name": "Customer success"
 },
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "ihoes4l8q2",
  "name": "Linux systems administration"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "k8e22lk68i",
  "name": "Writing"
 },
 {
  "id": "x1vemw60f2",
  "name": "Telecommunications"
 },
 {
  "id": "ii8017l1zt",
  "name": "Brand communication"
 },
 {
  "id": "i96jrqh2vb",
  "name": "Communication theories"
 },
 {
  "id": "emumq0l8k3",
  "name": "Communication software"
 },
 {
  "id": "rqi69qjjr4",
  "name": "Java Communications API"
 },
 {
  "id": "d3zbc9cgeu",
  "name": "Corporate communications"
 },
 {
  "id": "gsdsjal4b0",
  "name": "Communications and Media"
 },
 {
  "id": "t58vxk6kj9",
  "name": "Associate of Arts in Communication Studies"
 },
 {
  "id": "nkgddjdag0",
  "name": "Associate of Applied Science in Graphic Communications"
 },
 {
  "id": "jctieiwib0",
  "name": "Behavior change communication"
 },
 {
  "id": "h0rlt8kl2c",
  "name": "Personal Communications Service"
 },
 {
  "id": "z9jwpp35i0",
  "name": "Bachelor's in Mass Communications"
 },
 {
  "id": "ci6q1arnb0",
  "name": "Master's in Communication Studies"
 },
 {
  "id": "jh5x3kr85t",
  "name": "Social and behavior change communication"
 },
 {
  "id": "fgb46izjlv",
  "name": "Telecommunications equipment installation"
 },
 {
  "id": "bprelfo6pk",
  "name": "Immunization"
 },
 {
  "id": "bwerpn2ctr",
  "name": "Registered Communications Distribution Designer"
 },
 {
  "id": "t80fs65far",
  "name": "Community nutrition"
 },
 {
  "id": "yzx7utgq81",
  "name": "Punctuation"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "q1n9huan/global-job-market-postings-dataset@v1/foreign_jobs.release_candidate_v14_enriched.kaggle.csv:3",
  "source": "kaggle:q1n9huan/global-job-market-postings-dataset (CC0: Public Domain), column description",
  "text": "Job title: Customer Support Manager. customer success|midweight|full-time|communication|kubernetes|linux|spark|ops|llm|ai|go"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:50",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Technical Manager In Vietnam. [\"Technical Engineering\", \"Quality System\", \"Textile technology\", \"CAD\", \"Communication\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:278",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Business Analyst. …nd execute entire projects from start to finish including project management, requirements gathering, system analysis, problem solving, and communication of insights and recommendations. Define workflows, use cases, and detailed business logic Identify, vet and manage third party software providers,…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:5469",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Client Service Associate. … 2) Understand client requirements and translate them into clear briefs for designers, writers, and other departments. 3) Manage day-to-day communication with clients and ensure timely responses. 4) Maintain strong client relationships and identify opportunities for upselling or cross-selling. 5) Pr…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1931",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Analyst - Abstractions. Project Management, lease abstraction, lease administration system, Communication, property management, Abstracting, Lease Administration, Leasing"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 21 of 36: Teamwork (`tz7ipk5s96`)

~~~~text
Concept record:
{
 "id": "tz7ipk5s96",
 "preferred_name": "Teamwork",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Team-working"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "kut5s14k79",
  "name": "Collaboration"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "nb236cqujn",
  "name": "Coordination"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "yegnhni99h",
  "name": "Adaptability"
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
  "id": "ls6hrpynv0",
  "name": "Java"
 },
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "mcz3zs6q84",
  "name": "Physics"
 },
 {
  "id": "hjzieo2ohv",
  "name": "React"
 },
 {
  "id": "crm3w31oq7",
  "name": "Team-oriented"
 },
 {
  "id": "hecagq35qn",
  "name": "Nette"
 },
 {
  "id": "g6t643lbht",
  "name": "Microsoft Bot Framework"
 },
 {
  "id": "fnhev4v1dn",
  "name": "Computer networking"
 },
 {
  "id": "ft1f82qoac",
  "name": "AWS networking"
 },
 {
  "id": "y6729eqjad",
  "name": "Red teaming"
 },
 {
  "id": "dv5vi280tf",
  "name": "E-marketing"
 },
 {
  "id": "rdtwc1bnps",
  "name": "Speaking"
 },
 {
  "id": "wkbsvthe6e",
  "name": "Threat modeling"
 },
 {
  "id": "w522rsvq3h",
  "name": "Network peering"
 },
 {
  "id": "t6ptjyq1kp",
  "name": "Time Sharing"
 },
 {
  "id": "a2ymv23g4x",
  "name": "Team leadership"
 },
 {
  "id": "wroqa3tbb6",
  "name": "SWIFT network"
 },
 {
  "id": "rvb4xaqyno",
  "name": "Embalming"
 },
 {
  "id": "npja9s70lb",
  "name": "Repairing"
 },
 {
  "id": "hllkkrms0o",
  "name": "Reporting"
 },
 {
  "id": "dua32jm4h0",
  "name": "Theano"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:8",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Sales Associate/Customer Service Representative (Bilingual/Spanish). Bilingual, Retail sales transactions, Commission pay, Retail customer service procedures, Spanish, Customer communication, Paid training, Teamwork, Received goods storage, Promoting products, Hourly pay, Sales, Customer service, Store closing procedures, Merchandising, Email, Moving, Store opening p…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:90",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Business Development Trainee. Leadership,Team Management,Negotiation,MS-Excel,Coordination,Lead Generation,Teamwork,"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:94",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: AI Engineer (Middle Level) (Thu Nhập 20-30 Triệu). [\"Python\", \"Git\", \"LangChain\", \"Teamwork\", \"AI\", \"AI\"]"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:2435",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Machine Learning Analyst. Java, Python, React, SQL, RESTful API, Soft Skills: Communication, Problem-solving, Teamwork, Adaptability, Education-Related Skills: Java, Python, React, Experience-Related Skills: SQL, RESTful API, Communication, Problem-solving, Teamwork, Adaptability"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:1707",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Education Analyst - Physics. Physics, Edtech, Content Creation, Communication Skills, Content Generation, Artificial Intelligence, Problem Solving, Teamwork"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 22 of 36: Service orientation (`thsmk1q1kl`)

~~~~text
Concept record:
{
 "id": "thsmk1q1kl",
 "preferred_name": "Service orientation",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [
  {
   "label": "Service-Orientation"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "h4ck1veoae",
  "name": "Distributed computing"
 },
 {
  "id": "rscqfs498r",
  "name": "International Standard Book Number"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "y098fizl5l",
  "name": "Object-oriented design"
 },
 {
  "id": "i0vpvmxbz0",
  "name": "Object-oriented programming"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "qmravcc671",
  "name": "Software engineering"
 },
 {
  "id": "hctsy3pwrq",
  "name": "Spatial Orientation"
 },
 {
  "id": "crsg1gr1gz",
  "name": "Response Orientation"
 },
 {
  "id": "z4lqfruwis",
  "name": "Care coordination"
 },
 {
  "id": "n5hfz8pq8g",
  "name": "Price negotiation"
 },
 {
  "id": "k1k1pijmlc",
  "name": "Strategic prioritization"
 },
 {
  "id": "n1iikcimhd",
  "name": "Sales presentation"
 },
 {
  "id": "nb236cqujn",
  "name": "Coordination"
 },
 {
  "id": "zm7sxsrys1",
  "name": "Evidence collection"
 },
 {
  "id": "ic97ot6pm9",
  "name": "Security operations"
 },
 {
  "id": "uxc5mcnmd3",
  "name": "Executive presentations"
 },
 {
  "id": "od5cjk5y0z",
  "name": "Heavy vehicle operation"
 },
 {
  "id": "z5kqswzgmy",
  "name": "Pelvic floor rehabilitation"
 },
 {
  "id": "qlsxg8d6i9",
  "name": "Laser printing"
 },
 {
  "id": "ddfo4ab44g",
  "name": "Security Onion"
 },
 {
  "id": "atdk6aaopa",
  "name": "Big O notation"
 },
 {
  "id": "tou8ocnk8g",
  "name": "System implementation"
 },
 {
  "id": "d9otmo55ix",
  "name": "Resource mobilization"
 },
 {
  "id": "kblgtvd61c",
  "name": "Emergency vehicle operations"
 },
 {
  "id": "dcu238b2o0",
  "name": "Vehicle inspection"
 },
 {
  "id": "y3zi3hsdf6",
  "name": "IT security documentation"
 },
 {
  "id": "vb3ht42xuh",
  "name": "Service level requirement"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:2214",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Systems Administrator. …technology teams. Solid technical knowledge, as well as competencies in areas including infrastructure, data models, requirements analysis, service orientation, monitoring, understanding of enterprise, business process, and application architecture. Ability to grasp technical concepts quickly. Profi…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 23 of 36: Critical Thinking (`b9mkf081yw`)

~~~~text
Concept record:
{
 "id": "b9mkf081yw",
 "preferred_name": "Critical Thinking",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "x67fsx1qco",
  "name": "Feminist theory"
 },
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "ss273uzint",
  "name": "Software testing"
 },
 {
  "id": "xjt0zve4ah",
  "name": "Lean principles"
 },
 {
  "id": "qayw96u2hz",
  "name": "Critical reflection"
 },
 {
  "id": "xq6qu2qcae",
  "name": "Electrical wiring"
 },
 {
  "id": "ibphs8fgxr",
  "name": "Gait training"
 },
 {
  "id": "plyin34jo8",
  "name": "Critical path method"
 },
 {
  "id": "s479attn3c",
  "name": "Surgical incision"
 },
 {
  "id": "q30r29eun4",
  "name": "Surgical suturing"
 },
 {
  "id": "k8wsre0m9r",
  "name": "Technical writing"
 },
 {
  "id": "bfd8vmdbfl",
  "name": "Athletic training"
 },
 {
  "id": "hoz7m36u58",
  "name": "Certificate in Barbering"
 },
 {
  "id": "xramob4558",
  "name": "Nutritional screening"
 },
 {
  "id": "ilwjbw0ewo",
  "name": "Criminal intelligence"
 },
 {
  "id": "jfngdt55mz",
  "name": "Experiential marketing"
 },
 {
  "id": "e23pqgx4dr",
  "name": "Education and Training"
 },
 {
  "id": "b2xq589i0g",
  "name": "Private banking"
 },
 {
  "id": "d86tb3zsu0",
  "name": "Mechanical drafting"
 },
 {
  "id": "ag7qptfyr6",
  "name": "Coastal engineering"
 },
 {
  "id": "a19c10mi46",
  "name": "Digital advertising"
 },
 {
  "id": "zu90aejpyi",
  "name": "Architectural rendering"
 },
 {
  "id": "xme4tqyrgi",
  "name": "Artificial intelligence"
 },
 {
  "id": "osw8xhiaxm",
  "name": "Nutrition care planning"
 },
 {
  "id": "r4s8o1u1q1",
  "name": "Active Listening"
 },
 {
  "id": "irydpvx389",
  "name": "Agent tool use"
 },
 {
  "id": "ai3jtul08z",
  "name": "Certified Technical Trainer"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 24 of 36: Negotiation (`ccexfymw9t`)

~~~~text
Concept record:
{
 "id": "ccexfymw9t",
 "preferred_name": "Negotiation",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "mdcx7ximpo",
  "name": "LESS"
 },
 {
  "id": "c6mr2nxzm3",
  "name": "Problem solving"
 },
 {
  "id": "u9lvovjv7p",
  "name": "Creative problem-solving"
 },
 {
  "id": "jeai1j8uhz",
  "name": "French"
 },
 {
  "id": "sfx0dyxewl",
  "name": "Registered Clinical Exercise Physiologist"
 },
 {
  "id": "n5hfz8pq8g",
  "name": "Price negotiation"
 },
 {
  "id": "jh2rauw9ao",
  "name": "Memorization"
 },
 {
  "id": "vt6xft6d62",
  "name": "Demolition"
 },
 {
  "id": "t2pw81w7vy",
  "name": "Randomization"
 },
 {
  "id": "wv0l8usdcx",
  "name": "Transportation"
 },
 {
  "id": "atdk6aaopa",
  "name": "Big O notation"
 },
 {
  "id": "yzx7utgq81",
  "name": "Punctuation"
 },
 {
  "id": "f2phqfe4e5",
  "name": "Ideation"
 },
 {
  "id": "inxnx41ln3",
  "name": "Certified Perioperative Nurse (CNOR)"
 },
 {
  "id": "y83erk8o1r",
  "name": "Cost estimating"
 },
 {
  "id": "lr5nq6kgnc",
  "name": "Installation"
 },
 {
  "id": "jnssutztq4",
  "name": "Night Vision"
 },
 {
  "id": "bprelfo6pk",
  "name": "Immunization"
 },
 {
  "id": "an7k8us8vm",
  "name": "MicroStation"
 },
 {
  "id": "x4z2f6ku0u",
  "name": "Online demonstration"
 },
 {
  "id": "s95iijd8h1",
  "name": "American Osteopathic Board of Nuclear Medicine certification"
 },
 {
  "id": "rec5tl6jmm",
  "name": "Mongolian"
 },
 {
  "id": "pz26rmdqty",
  "name": "Dictation"
 },
 {
  "id": "kmodo98jyg",
  "name": "NCIDQ Certification"
 },
 {
  "id": "ez2j813g66",
  "name": "Norwegian"
 },
 {
  "id": "ewf1nb7uzl",
  "name": "Needle localization"
 },
 {
  "id": "ipfsxmf9ys",
  "name": "Content curation"
 },
 {
  "id": "jio8nmyohw",
  "name": "Refrigeration"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "z40m891ema",
  "name": "Program optimization"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 25 of 36: Attention to detail (`gdzh66chlx`)

~~~~text
Concept record:
{
 "id": "gdzh66chlx",
 "preferred_name": "Attention to detail",
 "kind": "ability",
 "broad_class": "ability",
 "variants": [
  {
   "label": "Detail Conscious"
  },
  {
   "label": "Detail oriented"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "b9mkf081yw",
  "name": "Critical Thinking"
 },
 {
  "id": "rdtwc1bnps",
  "name": "Speaking"
 },
 {
  "id": "f69xny35zm",
  "name": "SQL"
 },
 {
  "id": "g32rgj6uc5",
  "name": "Goal-oriented"
 },
 {
  "id": "crm3w31oq7",
  "name": "Team-oriented"
 },
 {
  "id": "cd19a0euqf",
  "name": "Residential construction"
 },
 {
  "id": "id244h1e6v",
  "name": "Results-oriented"
 },
 {
  "id": "vlx37w32ol",
  "name": "Email on Acid"
 },
 {
  "id": "z3d8t5kt64",
  "name": "OrientDB"
 },
 {
  "id": "cezarn1svy",
  "name": "Automotive detailing"
 },
 {
  "id": "jnut7g5uci",
  "name": "Email etiquette"
 },
 {
  "id": "c0kd1bmd4t",
  "name": "Dental records"
 },
 {
  "id": "kpy86mibqf",
  "name": "Taxi license"
 },
 {
  "id": "iz17ednjvl",
  "name": "Digital currencies"
 },
 {
  "id": "hctsy3pwrq",
  "name": "Spatial Orientation"
 },
 {
  "id": "xl6126omq1",
  "name": "Dairy science"
 },
 {
  "id": "myqo7j7o11",
  "name": "Label printer"
 },
 {
  "id": "bt632lzc9o",
  "name": "Design consultation"
 },
 {
  "id": "leu6zjs1w7",
  "name": "Traffic collision reconstruction"
 },
 {
  "id": "gov0d8zbms",
  "name": "Resilience"
 },
 {
  "id": "w1fhvynkfa",
  "name": "Associate of Applied Science in Dental Hygiene"
 },
 {
  "id": "kokxhnhui7",
  "name": "Design of experiments"
 },
 {
  "id": "u4n357y1ti",
  "name": "Animal science"
 },
 {
  "id": "ihcdms58ev",
  "name": "Email software"
 },
 {
  "id": "pts4mjn76g",
  "name": "Financial consolidation"
 },
 {
  "id": "znkj1vnxbh",
  "name": "Data center design"
 },
 {
  "id": "oia7a9p9lz",
  "name": "Behavioural science"
 },
 {
  "id": "l39uixm3x0",
  "name": "Bridal consulting"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:3",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Morning Bartender. … Bartender, you will be the first face our guests see, setting the tone for an exceptional dining and drinking experience. Your enthusiasm, attention to detail, and expertise in beverage service will create a welcoming atmosphere that keeps guests coming back. This role offers a fantastic opportunit…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:28",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Human Resources (HR) Associate. MS-Office,MS-Word,Attention to Detail,MS-Excel,English Proficiency (Spoken),English Proficiency (Written),Document Management,"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:305",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Business Analyst. …gnostics results to clearly articulate business opportunities Configure model with limited mentorship from project lead Demonstrates superb attention to detail Demonstrates interest and/or competence in tools needed to deliver project analysis (Excel, Power Pivot, and other analytical tools and soft…"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:1040",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Reverse Data Analyst. [\"Data Analysis\", \"Excel\", \"SQL\", \"BI Tools\", \"Attention To Detail\"]"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:131",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Research Analyst. Critical Thinking, Strategic Thinking, Attention To Detail, Decision Making, Communication Skills, Presentation Skills, Analytical, Public Speaking"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 26 of 36: Deductive Reasoning (`wclhs8ljcp`)

~~~~text
Concept record:
{
 "id": "wclhs8ljcp",
 "preferred_name": "Deductive Reasoning",
 "kind": "ability",
 "broad_class": "ability",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "rv0h309eu3",
  "name": "Psychology"
 },
 {
  "id": "rdtwc1bnps",
  "name": "Speaking"
 },
 {
  "id": "xk73ola6io",
  "name": "Inductive Reasoning"
 },
 {
  "id": "xubhw9lr07",
  "name": "Active Learning"
 },
 {
  "id": "quabg9izgu",
  "name": "Extensive reading"
 },
 {
  "id": "ec2b8ggmp3",
  "name": "Mathematical Reasoning"
 },
 {
  "id": "e23pqgx4dr",
  "name": "Education and Training"
 },
 {
  "id": "pgi48gvql4",
  "name": "Predictive modelling"
 },
 {
  "id": "r4s8o1u1q1",
  "name": "Active Listening"
 },
 {
  "id": "njlcvlg504",
  "name": "Causal reasoning"
 },
 {
  "id": "nw1oyk7q86",
  "name": "Deep learning"
 },
 {
  "id": "pe7v46ydhy",
  "name": "Livestreaming"
 },
 {
  "id": "u9lvovjv7p",
  "name": "Creative problem-solving"
 },
 {
  "id": "mn0kh9q0a1",
  "name": "Substantive testing"
 },
 {
  "id": "isdz1w83kv",
  "name": "ReactiveX"
 },
 {
  "id": "cifv2by5mk",
  "name": "Specimen processing"
 },
 {
  "id": "my2r15ngyp",
  "name": "Spatial-temporal reasoning"
 },
 {
  "id": "qq55sjjp3e",
  "name": "Executive relationship management"
 },
 {
  "id": "w1blu9iu00",
  "name": "Blended learning"
 },
 {
  "id": "uxc5mcnmd3",
  "name": "Executive presentations"
 },
 {
  "id": "flxbx98seh",
  "name": "Machine learning"
 },
 {
  "id": "dz5xjcq45r",
  "name": "Data-driven decision-making"
 },
 {
  "id": "uqjw14p9ev",
  "name": "Executive protection"
 },
 {
  "id": "pt4t1q8cxq",
  "name": "Peachtree Accounting"
 },
 {
  "id": "cezarn1svy",
  "name": "Automotive detailing"
 },
 {
  "id": "agserdgtg7",
  "name": "Tax deduction"
 },
 {
  "id": "l6oh8z1sgb",
  "name": "Interactive storytelling"
 },
 {
  "id": "ydp6a13kjq",
  "name": "AdaBoost"
 },
 {
  "id": "op8cesvddr",
  "name": "Distance learning"
 },
 {
  "id": "hyiokkty1d",
  "name": "Videoconferencing"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 27 of 36: Statistics (`ecoz6ylymx`)

~~~~text
Concept record:
{
 "id": "ecoz6ylymx",
 "preferred_name": "Statistics",
 "kind": "knowledge",
 "broad_class": "knowledge",
 "variants": [
  {
   "label": "statistical analysis"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "ww4glmysl2",
  "name": "Applied statistics"
 },
 {
  "id": "sh75mx00wm",
  "name": "Official statistics"
 },
 {
  "id": "v3yihyzit5",
  "name": "PhD in Statistics"
 },
 {
  "id": "yudz6qpuf8",
  "name": "Statistical software"
 },
 {
  "id": "v2tu54uao9",
  "name": "Mathematics"
 },
 {
  "id": "so9zp6tzyh",
  "name": "Mathematics"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "ww6z5fppct",
  "name": "German"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "mcz3zs6q84",
  "name": "Physics"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "mtmkw6b12m",
  "name": "Data engineering"
 },
 {
  "id": "kokxhnhui7",
  "name": "Design of experiments"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "pk7cebmtg6",
  "name": "Python"
 },
 {
  "id": "wc1h5yr8q7",
  "name": "Chemistry"
 },
 {
  "id": "mwcmyvh54c",
  "name": "Industrial statistics"
 },
 {
  "id": "mcd36zu7px",
  "name": "Engineering statistics"
 },
 {
  "id": "c4n5rzxsre",
  "name": "Master's in Statistics"
 },
 {
  "id": "q7mat9lcyk",
  "name": "Bachelor's in Statistics"
 },
 {
  "id": "u7ui1qw5um",
  "name": "Diagnostic analysis"
 },
 {
  "id": "jfqj25il68",
  "name": "Blast radius analysis"
 },
 {
  "id": "q12fvgzu4o",
  "name": "Qualitative data analysis"
 },
 {
  "id": "nr9nocn8r3",
  "name": "Case analysis"
 },
 {
  "id": "njm2i8ibdr",
  "name": "Operations Analysis"
 },
 {
  "id": "h4v7sfgj5x",
  "name": "Systems Analysis"
 },
 {
  "id": "e7mhl48ny3",
  "name": "PEST analysis"
 },
 {
  "id": "ud1kx8zgr6",
  "name": "Variance analysis"
 },
 {
  "id": "q0idp0h02o",
  "name": "Policy analysis"
 },
 {
  "id": "nohrtfqkb7",
  "name": "ESG analysis"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:28",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Digital Solution Architect - ThingWorx. …ng setting Undergraduate degree (preferably in Computer Science or Information Systems with supplementary experience in Data Science and/or Statistics) Fluency in spoken and written English Strong academic performance: Minimum 3.5 cumulative GPA highly preferred Relevant work experience is highly pr…"
 },
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:6",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Entry-Level Modeling and Data Analysis Engineer (Electrical, Aerospace, Physics Degree). …lectrical Engineering * Aerospace Engineering * Engineering mathematics * Physics * Numerical methods * Data analysis * Signal processing * Statistics and data visualization * Software development Experience in all of these areas is not required. This position is intended for candidates with strong …"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:178",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: BA3 Decision Analyst. , advanced analytics, python, data science, data mining, machine learning, sql, statistics"
 },
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:114",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Data Analysis Senior Officer/Supervisor. [\"Data Analysis\", \"SQL\", \"Excel\", \"Statistical Analysis\", \"Data Engineering\", \"Data Engineering\"]"
 },
 {
  "id": "dev122/internshala-jobs-dataset@v1/JobData.csv:143",
  "source": "kaggle:dev122/internshala-jobs-dataset (CC0: Public Domain), column Description",
  "text": "Job title: Flutter Development Intern. … 1. This will be a manual effort 2. We will guide how to do this. Data Science , MS-Excel , Python , R Programming , Statistical Modeling , Statistics"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 28 of 36: Mathematics (`so9zp6tzyh`)

~~~~text
Concept record:
{
 "id": "so9zp6tzyh",
 "preferred_name": "Mathematics",
 "kind": "knowledge",
 "broad_class": "knowledge",
 "variants": [],
 "relations": [
  {
   "type": "related",
   "target": "hzccoii598",
   "target_name": "Arithmetic"
  },
  {
   "type": "related",
   "target": "ec2b8ggmp3",
   "target_name": "Mathematical Reasoning"
  },
  {
   "type": "related",
   "target": "kgaqqkj85g",
   "target_name": "Engineering mathematics"
  }
 ]
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "hzccoii598",
  "name": "Arithmetic"
 },
 {
  "id": "ec2b8ggmp3",
  "name": "Mathematical Reasoning"
 },
 {
  "id": "kgaqqkj85g",
  "name": "Engineering mathematics"
 },
 {
  "id": "sh1iz9ofy3",
  "name": "Bachelor's in Mathematics"
 },
 {
  "id": "ded87nal6c",
  "name": "Master's in Mathematics"
 },
 {
  "id": "e4f7w0tm86",
  "name": "PhD in Mathematics"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "v2tu54uao9",
  "name": "Mathematics"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "mcz3zs6q84",
  "name": "Physics"
 },
 {
  "id": "ecoz6ylymx",
  "name": "Statistics"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "xhr0najg6f",
  "name": "Visualization"
 },
 {
  "id": "amuzox4pgm",
  "name": "Data visualization"
 },
 {
  "id": "kp84ig38m5",
  "name": "Database design"
 },
 {
  "id": "o691ftsrfr",
  "name": "Google Sheets"
 },
 {
  "id": "eon43rmtrr",
  "name": "Greek"
 },
 {
  "id": "wvycqv51z7",
  "name": "Mathematica"
 },
 {
  "id": "hp26l3foe2",
  "name": "Desmos"
 },
 {
  "id": "ysp84vgjvb",
  "name": "Associate of Science in Mathematics"
 },
 {
  "id": "jj1y0opj8n",
  "name": "Garment alterations"
 },
 {
  "id": "efwtd5psz9",
  "name": "Anthropometrics"
 },
 {
  "id": "uu17w6c03r",
  "name": "Media ethics"
 },
 {
  "id": "psbz3dahyh",
  "name": "Dietetics"
 },
 {
  "id": "tqxd6h55a8",
  "name": "Diploma in Esthetics"
 },
 {
  "id": "v9eefyu589",
  "name": "Gymnastics"
 },
 {
  "id": "nvdcu20iv6",
  "name": "Pathology informatics"
 },
 {
  "id": "m93rwlykrf",
  "name": "MicroStrategy metrics"
 },
 {
  "id": "o7rmvt0viw",
  "name": "Marathi"
 },
 {
  "id": "i6hs4i5v7l",
  "name": "Mosaic art"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:6",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Entry-Level Modeling and Data Analysis Engineer (Electrical, Aerospace, Physics Degree). …fy, and use engineering analysis tools to support model development, data processing, visualization, and V&V. * Apply engineering, physics, mathematics, and numerical methods to solve modeling and simulation problems. * Investigate discrepancies and trends within simulation and engineering datasets.…"
 },
 {
  "id": "mohityd2007/real-world-job-postings-dataset-for-ml-projects@v1/jobs_data.csv:307",
  "source": "kaggle:mohityd2007/real-world-job-postings-dataset-for-ml-projects (Attribution 4.0 International (CC BY 4.0)), column Job Description",
  "text": "Job title: Mathematics Teacher. Budding Mariners is hiring a Mathematics and Aptitude Teaching professional to prepare aspiring mariners for IMU-CET and maritime entrance examinations. The role focuses on delivering engaging mathematics and aptitude training while helping students build strong analytical and problem-solving skills…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:555",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Data Scientist. Data analysis, data science, Machine learning, Programming, Mathematics, data visualization, Statistics, Analytics"
 },
 {
  "id": "meerawks/it-skills-from-jobs@v1/JobsDatasetProcessed.csv:257",
  "source": "kaggle:meerawks/it-skills-from-jobs (Apache 2.0), column Description",
  "text": "Job title: Sales Business Analyst. Data analysis, Market analysis, Database management, Report preparation, Statistical analysis, Marketing trends analysis, Mathematics, Microsoft Office Suite, Order processing systems"
 },
 {
  "id": "jayaantanaath/internship-opportunities-in-india-2025@v1/merged_internships_dataset.csv:5",
  "source": "kaggle:jayaantanaath/internship-opportunities-in-india-2025 (MIT), column Skills",
  "text": "English Proficiency (Spoken), English Proficiency (Written), Google Sheets, Mathematics, MS-Excel, Statistical Modeling, Statistics"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 29 of 36: Mathematics (`v2tu54uao9`)

~~~~text
Concept record:
{
 "id": "v2tu54uao9",
 "preferred_name": "Mathematics",
 "kind": "skill",
 "broad_class": "skill",
 "variants": [],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "so9zp6tzyh",
  "name": "Mathematics"
 },
 {
  "id": "hzccoii598",
  "name": "Arithmetic"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "eon43rmtrr",
  "name": "Greek"
 },
 {
  "id": "mcz3zs6q84",
  "name": "Physics"
 },
 {
  "id": "esk7959e8m",
  "name": "Scheme"
 },
 {
  "id": "rdtwc1bnps",
  "name": "Speaking"
 },
 {
  "id": "e4f7w0tm86",
  "name": "PhD in Mathematics"
 },
 {
  "id": "kgaqqkj85g",
  "name": "Engineering mathematics"
 },
 {
  "id": "ded87nal6c",
  "name": "Master's in Mathematics"
 },
 {
  "id": "sh1iz9ofy3",
  "name": "Bachelor's in Mathematics"
 },
 {
  "id": "wvycqv51z7",
  "name": "Mathematica"
 },
 {
  "id": "hp26l3foe2",
  "name": "Desmos"
 },
 {
  "id": "ysp84vgjvb",
  "name": "Associate of Science in Mathematics"
 },
 {
  "id": "ec2b8ggmp3",
  "name": "Mathematical Reasoning"
 },
 {
  "id": "jj1y0opj8n",
  "name": "Garment alterations"
 },
 {
  "id": "efwtd5psz9",
  "name": "Anthropometrics"
 },
 {
  "id": "uu17w6c03r",
  "name": "Media ethics"
 },
 {
  "id": "psbz3dahyh",
  "name": "Dietetics"
 },
 {
  "id": "tqxd6h55a8",
  "name": "Diploma in Esthetics"
 },
 {
  "id": "v9eefyu589",
  "name": "Gymnastics"
 },
 {
  "id": "ecoz6ylymx",
  "name": "Statistics"
 },
 {
  "id": "nvdcu20iv6",
  "name": "Pathology informatics"
 },
 {
  "id": "m93rwlykrf",
  "name": "MicroStrategy metrics"
 },
 {
  "id": "o7rmvt0viw",
  "name": "Marathi"
 },
 {
  "id": "i6hs4i5v7l",
  "name": "Mosaic art"
 },
 {
  "id": "hte4e69ldf",
  "name": "Maltese"
 },
 {
  "id": "p69ue6ggj9",
  "name": "Schematic diagrams"
 },
 {
  "id": "xiupcoba2m",
  "name": "HTML emails"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 30 of 36: Spanish (`de8aeltv9z`)

~~~~text
Concept record:
{
 "id": "de8aeltv9z",
 "preferred_name": "Spanish",
 "kind": "human-language",
 "broad_class": "language",
 "variants": [
  {
   "label": "Spanish (Language)"
  },
  {
   "label": "Español"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "hj8i6mh3zz",
  "name": "Chinese"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "b53t6y9iys",
  "name": "Catalan"
 },
 {
  "id": "jeai1j8uhz",
  "name": "French"
 },
 {
  "id": "vphlc8dpfb",
  "name": "Mandarin"
 },
 {
  "id": "c6s0kc7cs8",
  "name": "Arabic"
 },
 {
  "id": "e6d3w0bi1i",
  "name": "Portuguese"
 },
 {
  "id": "y8idko4c9n",
  "name": "Italian"
 },
 {
  "id": "eon43rmtrr",
  "name": "Greek"
 },
 {
  "id": "u42in8da9c",
  "name": "Hindi"
 },
 {
  "id": "d168utcmjy",
  "name": "Natural language processing"
 },
 {
  "id": "l54jfkzunm",
  "name": "Programming"
 },
 {
  "id": "d848216rx6",
  "name": "Ladino"
 },
 {
  "id": "n2zf1jjewl",
  "name": "Castilian Spanish"
 },
 {
  "id": "x09au1cwqd",
  "name": "Danish"
 },
 {
  "id": "vicv7ha84e",
  "name": "Polish"
 },
 {
  "id": "qgyuathae3",
  "name": "Pashto"
 },
 {
  "id": "wfw1x8wd7f",
  "name": "Shan"
 },
 {
  "id": "q98sd6zk57",
  "name": "Finnish"
 },
 {
  "id": "lr6v3jj0ke",
  "name": "Swedish"
 },
 {
  "id": "mhqs5zfa2v",
  "name": "Swati"
 },
 {
  "id": "hs6rwa4dqv",
  "name": "Sakha"
 },
 {
  "id": "dupsfn56g9",
  "name": "Sango"
 },
 {
  "id": "xzbzidj6js",
  "name": "Japanese"
 },
 {
  "id": "bak08047ud",
  "name": "Santali"
 },
 {
  "id": "vfbvb6cbta",
  "name": "Somali"
 },
 {
  "id": "nsuvujp7pw",
  "name": "Sindhi"
 },
 {
  "id": "n5gmv1hla7",
  "name": "Tswana"
 },
 {
  "id": "msc664vu47",
  "name": "Nepali"
 },
 {
  "id": "ejc1plwt0s",
  "name": "Samoan"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:8",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Sales Associate/Customer Service Representative (Bilingual/Spanish). *Full-Time Sales Associate – $35K–$55K+ | Hourly + Commission* *Elliott’s Boot Company | Cleveland, TN | Bilingual English/Spanish * *Pay:* Hourly Pay + Commission *Typical Annual Earnings:* $35,000–$55,000+ *Job Type:* Full-Time *Location:* Cleveland, TN *Schedule:* Monday–Saturday | 8–10 hour shif…"
 },
 {
  "id": "priyankamalavade/naukri-jobs-details@v1/naukri_data_analyst_jobs.csv:584",
  "source": "kaggle:priyankamalavade/naukri-jobs-details (MIT), column Description",
  "text": "Job title: Data Scientist. Analytical skills, Data analysis, French, Spanish, Natural language processing, Manager Quality Control, Data mining, Object oriented programming"
 },
 {
  "id": "koti4878m/naukari@v1/naukari.csv:248",
  "source": "kaggle:koti4878m/naukari (CC0: Public Domain), column key_skills",
  "text": "Job title: Spanish - Customer Support. ['Spanish']"
 },
 {
  "id": "promptcloud/jobs-on-naukricom@v1/home/sdf/marketing_sample_for_naukri_com-jobs__20190701_20190830__30k_data.csv:295",
  "source": "kaggle:promptcloud/jobs-on-naukricom (CC0: Public Domain), column Key Skills",
  "text": "Job title: Chinese, Spanish Language Expert (proofcheck Medical Content),. spanish language expert| chinese| spanish| medical"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 31 of 36: Bachelor's in Nursing (`n7a094bha6`)

~~~~text
Concept record:
{
 "id": "n7a094bha6",
 "preferred_name": "Bachelor's in Nursing",
 "kind": "credential",
 "broad_class": "certification",
 "variants": [
  {
   "label": "Bachelor's degree in Nursing"
  },
  {
   "label": "Bachelors degree in Nursing"
  }
 ],
 "relations": [
  {
   "type": "related",
   "target": "c4tp7yji9k",
   "target_name": "Bachelor of Science in Nursing"
  },
  {
   "type": "related",
   "target": "gg2k98nhyp",
   "target_name": "Associate degree in nursing"
  }
 ]
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "c4tp7yji9k",
  "name": "Bachelor of Science in Nursing"
 },
 {
  "id": "gg2k98nhyp",
  "name": "Associate degree in nursing"
 },
 {
  "id": "m1nnmfjsv0",
  "name": "Goal setting"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "q57gehopyn",
  "name": "Onboarding"
 },
 {
  "id": "y0w122f4sc",
  "name": "Outpatient surgery"
 },
 {
  "id": "f7c96nvfei",
  "name": "Surgery"
 },
 {
  "id": "o57rerb7hz",
  "name": "Bachelor's in Nutrition"
 },
 {
  "id": "k02tqo3we4",
  "name": "Bachelor's in Music"
 },
 {
  "id": "q2z0yc5xlh",
  "name": "Bachelor's in Advertising"
 },
 {
  "id": "ohfad0qp5g",
  "name": "Bachelor's in Marketing"
 },
 {
  "id": "k81eciday8",
  "name": "Master's in Nursing"
 },
 {
  "id": "c7wanms4cc",
  "name": "Bachelor's in Accounting"
 },
 {
  "id": "aldzl2915d",
  "name": "Bachelor's in Kinesiology"
 },
 {
  "id": "of4ufj4sc3",
  "name": "Bachelor's in Animation"
 },
 {
  "id": "j1t4ujqb1j",
  "name": "Bachelor's in Sociology"
 },
 {
  "id": "wnjgloor52",
  "name": "Bachelor's in English"
 },
 {
  "id": "q4opda6znq",
  "name": "Bachelor's in Finance"
 },
 {
  "id": "f6fx1supki",
  "name": "Bachelor's in Biology"
 },
 {
  "id": "aongc0kf7s",
  "name": "Bachelor's in Physics"
 },
 {
  "id": "dvubyy51i4",
  "name": "Bachelor's in Industrial Design"
 },
 {
  "id": "zi8c47ejt8",
  "name": "Bachelor's in Entrepreneurship"
 },
 {
  "id": "zed7bmjfiv",
  "name": "Bachelor's in Economics"
 },
 {
  "id": "v9j5yhd5v0",
  "name": "Bachelor's in History"
 },
 {
  "id": "uvjd95mfxg",
  "name": "Bachelor's in Zoology"
 },
 {
  "id": "u62u9fv0kf",
  "name": "Bachelor's in Dietetics"
 },
 {
  "id": "sh1iz9ofy3",
  "name": "Bachelor's in Mathematics"
 },
 {
  "id": "s8zm9ssb31",
  "name": "Bachelor's in Forestry"
 },
 {
  "id": "qd47eah27z",
  "name": "Bachelor's in Ecology"
 },
 {
  "id": "qavkwwt7mh",
  "name": "Bachelor's in Meteorology"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:189",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Director, ASC Clinical Operations. Outpatient surgery experience, Clinical staff performance evaluation, Managed Registered Nurses (RNs), Employee onboarding, Staff performance monitoring, PACU experience, Computer operation, Operational analysis, Nursing, Staff supervision, Strategic goal setting, Strategic management, Program manag…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 32 of 36: Bachelor of Science in Nursing (`c4tp7yji9k`)

~~~~text
Concept record:
{
 "id": "c4tp7yji9k",
 "preferred_name": "Bachelor of Science in Nursing",
 "kind": "credential",
 "broad_class": "certification",
 "variants": [
  {
   "label": "Bachelor Of Science in Nursing (BSN)"
  },
  {
   "label": "BSN"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "n7a094bha6",
  "name": "Bachelor's in Nursing"
 },
 {
  "id": "q4f1jrji2c",
  "name": "Master of Science in Nursing"
 },
 {
  "id": "yjdfn8v7dp",
  "name": "Science"
 },
 {
  "id": "wc1h5yr8q7",
  "name": "Chemistry"
 },
 {
  "id": "v17l7v4fgv",
  "name": "Administrative"
 },
 {
  "id": "uqnp4t4487",
  "name": "Advanced Cardiovascular Life Support"
 },
 {
  "id": "gg2k98nhyp",
  "name": "Associate degree in nursing"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "ek2gamyipw",
  "name": "Biology"
 },
 {
  "id": "kut5s14k79",
  "name": "Collaboration"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "b9mkf081yw",
  "name": "Critical Thinking"
 },
 {
  "id": "e23pqgx4dr",
  "name": "Education and Training"
 },
 {
  "id": "tsdlbd9gt0",
  "name": "English"
 },
 {
  "id": "v9psjv5xcb",
  "name": "dbSNP"
 },
 {
  "id": "zr4o6v40dh",
  "name": "Bachelor of Science in Business"
 },
 {
  "id": "krbuvn8mmn",
  "name": "Associate of Science in Nursing"
 },
 {
  "id": "b7mk8spxib",
  "name": "Bachelor of Science in Pharmacy"
 },
 {
  "id": "kyg8c9ysbl",
  "name": "Bachelor of Science in Business Administration"
 },
 {
  "id": "wbmmkjyuq9",
  "name": "Associate of Science in Nutrition"
 },
 {
  "id": "fxrc7oyx9v",
  "name": "Associate of Science in Marketing"
 },
 {
  "id": "o57rerb7hz",
  "name": "Bachelor's in Nutrition"
 },
 {
  "id": "axybvm0oui",
  "name": "Associate of Science in Kinesiology"
 },
 {
  "id": "sbjwzquv9w",
  "name": "Associate of Science in Pre-Engineering"
 },
 {
  "id": "ljshci25ww",
  "name": "Board support package"
 },
 {
  "id": "rks5hh58sp",
  "name": "Associate of Science in Dental Assisting"
 },
 {
  "id": "q2z0yc5xlh",
  "name": "Bachelor's in Advertising"
 },
 {
  "id": "p4nnmyui39",
  "name": "Associate of Science in Physics"
 },
 {
  "id": "m6sws4wwkb",
  "name": "Associate of Science in Finance"
 },
 {
  "id": "ijkl6150us",
  "name": "Associate of Science in Biology"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "scrapifier/indeed-usa-job-postings@v1/indeed_usa_job_postings.csv:189",
  "source": "kaggle:scrapifier/indeed-usa-job-postings (CC0: Public Domain), column description",
  "text": "Job title: Director, ASC Clinical Operations. … Nurse Managers and ASC clinical staff in collaboration with Human Resources and ASC leadership. Requirements: QUALIFICATIONS: Knowledge: • Bachelor of Science in Nursing (BSN) from an accredited nursing program required; current ACLS certification required. • Minimum of five years of progressive pe…"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 33 of 36: Class B commercial driver's license (`zkn14vnicf`)

~~~~text
Concept record:
{
 "id": "zkn14vnicf",
 "preferred_name": "Class B commercial driver's license",
 "kind": "credential",
 "broad_class": "certification",
 "variants": [
  {
   "label": "CDL Class B License"
  },
  {
   "label": "Class B CDL"
  }
 ],
 "relations": []
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "idkj5utilp",
  "name": "Driver's license"
 },
 {
  "id": "oehr89d61h",
  "name": "Class C commercial driver's license"
 },
 {
  "id": "d7q5p3nh9m",
  "name": "Client access license"
 },
 {
  "id": "wy0q8xbf4z",
  "name": "International Computer Driving Licence"
 },
 {
  "id": "kpy86mibqf",
  "name": "Taxi license"
 },
 {
  "id": "lptn88zmvw",
  "name": "Chauffeur license"
 },
 {
  "id": "nw5dzgyuwi",
  "name": "Real estate broker license"
 },
 {
  "id": "kko9f7t16z",
  "name": "Pharmacist license"
 },
 {
  "id": "fyins3tz6o",
  "name": "Claims modeling"
 },
 {
  "id": "zyx43s2qb5",
  "name": "Air Travel Organisers' Licensing"
 },
 {
  "id": "pkrafh1a5u",
  "name": "Cloud access security broker"
 },
 {
  "id": "llqj4t94kq",
  "name": "Board Certified Specialist in Sports Dietetics"
 },
 {
  "id": "cm0ca8dswq",
  "name": "School bus endorsement"
 },
 {
  "id": "j9834ogpij",
  "name": "Series 53 Municipal Securities Principal"
 },
 {
  "id": "zl7j10mzsp",
  "name": "Associate of Applied Science in Emergency Medical Services"
 },
 {
  "id": "wopopj6ryd",
  "name": "Nurse licensure"
 },
 {
  "id": "ijn2ibts2r",
  "name": "Boating license"
 },
 {
  "id": "m2b1i9wyd7",
  "name": "Data classification"
 },
 {
  "id": "scnorb90o8",
  "name": "AWS big data"
 },
 {
  "id": "of65nuyei7",
  "name": "Real estate salesperson license"
 },
 {
  "id": "jbz6pxzqbx",
  "name": "Series 24 General Securities Principal"
 },
 {
  "id": "ztbqyvr0s2",
  "name": "Social media advertising"
 },
 {
  "id": "towc92tnse",
  "name": "Series 52 Municipal Securities Representative"
 },
 {
  "id": "ipdzyw63rq",
  "name": "ISS Environmental Control and Life Support System"
 },
 {
  "id": "g35t5hixm4",
  "name": "Clean Air Act"
 },
 {
  "id": "f2p6p58eru",
  "name": "Apache Cassandra"
 },
 {
  "id": "dwoqn11jcz",
  "name": "Series 3 National Commodity Futures"
 },
 {
  "id": "oozzdioit7",
  "name": "Social media analytics"
 },
 {
  "id": "btlglc68rv",
  "name": "Tanker endorsement"
 },
 {
  "id": "xb17x3c064",
  "name": "Data as a Service"
 }
]

Usage examples from postings and syllabi:
[]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 34 of 36: CCNA Security (`tp5pvtb8jm`)

~~~~text
Concept record:
{
 "id": "tp5pvtb8jm",
 "preferred_name": "CCNA Security",
 "kind": "credential",
 "broad_class": "certification",
 "variants": [
  {
   "label": "Cisco Certified Network Associate- Security"
  },
  {
   "label": "Cisco Certified Network Associate Security"
  }
 ],
 "relations": [
  {
   "type": "related",
   "target": "aksp1d11ue",
   "target_name": "CCNP Security"
  }
 ]
}

lexicon_neighbors (existing concepts you may use as relation targets):
[
 {
  "id": "aksp1d11ue",
  "name": "CCNP Security"
 },
 {
  "id": "kut5s14k79",
  "name": "Collaboration"
 },
 {
  "id": "norpz7ekiw",
  "name": "Cybersecurity"
 },
 {
  "id": "qo7asa9na4",
  "name": "Troubleshooting"
 },
 {
  "id": "cex5ha398q",
  "name": "Design"
 },
 {
  "id": "gk12ir4ef9",
  "name": "BASIC"
 },
 {
  "id": "lr5nq6kgnc",
  "name": "Installation"
 },
 {
  "id": "hw7zdcqefw",
  "name": "Certified Control Systems Technician"
 },
 {
  "id": "gisypzf6gf",
  "name": "Communication"
 },
 {
  "id": "znkj1vnxbh",
  "name": "Data center design"
 },
 {
  "id": "fjheonyp0m",
  "name": "Monitoring"
 },
 {
  "id": "ic97ot6pm9",
  "name": "Security operations"
 },
 {
  "id": "brj2fpgqpe",
  "name": "Kenna Security"
 },
 {
  "id": "dtlvf3ey43",
  "name": "Azure Security"
 },
 {
  "id": "u1uj3cchu7",
  "name": "Physical security"
 },
 {
  "id": "tnfsxl3lm8",
  "name": "CompTIA Security+"
 },
 {
  "id": "i4lihri92l",
  "name": "Certified Nursing Assistant"
 },
 {
  "id": "oqjr6z2wak",
  "name": "SSL/TLS security"
 },
 {
  "id": "iq07ybp2b0",
  "name": "Security Certified Network Architect"
 },
 {
  "id": "xodwbue4v1",
  "name": "REST API security"
 },
 {
  "id": "ksjlonf3g4",
  "name": "Wi-Fi security"
 },
 {
  "id": "sshjgtnr54",
  "name": "Endpoint security"
 },
 {
  "id": "pjtm4az4zk",
  "name": "Certified Network Defense Architect"
 },
 {
  "id": "lsxf83lrq4",
  "name": "Cloud computing security"
 },
 {
  "id": "wvdtj7lc5u",
  "name": "Citrix Certified Integration Architect"
 },
 {
  "id": "n01lv1fq0t",
  "name": "SACA Certified Industry 4.0 Associate, Basic Operations"
 },
 {
  "id": "qrwo2ay5y4",
  "name": "Oracle Certified Associate"
 },
 {
  "id": "h7harffxrh",
  "name": "Certified Coding Associate"
 },
 {
  "id": "dg5e04q6is",
  "name": "Sun Certified Enterprise Architect"
 },
 {
  "id": "ddfo4ab44g",
  "name": "Security Onion"
 }
]

Usage examples from postings and syllabi:
[
 {
  "id": "vitthnhnguyn138/vietnam-it-job-posts@v1/vietnam_it_job_posts.csv:608",
  "source": "kaggle:vitthnhnguyn138/vietnam-it-job-posts (MIT), column skills",
  "text": "Job title: Cyber Security Engineer (Network Engineer). [\"CCNA Security\", \"CCNP Security\", \"Cybersecurity\", \"Firewall\", \"Network\"]"
 }
]

Wikipedia candidates (each with revision_id and plain text):
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 35 of 36: Salesforce (`url3hq4jid`)

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
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 36 of 36: User experience design (`sixghka9vw`)

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
[]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
