# Irreducibly Human Work Lexicon pilot, grounded run: message 2 of 13 (chunk 01, 3 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "01", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-01.jsonl`. Otherwise send one code block marked `jsonl` holding the 3 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 3: PostgreSQL (`sh6x1wmacn`)

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
[
 {
  "title": "PostgreSQL",
  "revision_id": "1378290712",
  "matched_by": "title",
  "text": "PostgreSQL (/ˈpoʊstɡrɛskjuˌɛl/ POHST-gres-kew-EL), also known as Postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance. PostgreSQL features transactions with atomicity, consistency, isolation, durability (ACID) properties, automatically updatable views, materialized views, triggers, foreign keys, and stored procedures.\nIt is supported on all major operating systems, including Windows, Linux, macOS, FreeBSD, and OpenBSD, and handles a range of workloads from single machines to data warehouses, data lakes, or web services with many concurrent users.\n\nThe PostgreSQL Global Development Group focuses only on developing a database engine and closely related components.\nThis core is, technically, what comprises PostgreSQL itself, but there is an extensive developer community and ecosystem that provides other important feature sets that might, traditionally, be provided by a proprietary software vendor. These include special-purpose database engine features, like those needed to support a geospatial or temporal database or features which emulate other database products. \nAlso available from third parties are a wide variety of user and machine interface features, such as graphical user interfaces or load balancing and high availability toolsets.\nThe large third-party PostgreSQL support network of people, companies, products, and projects, even though not part of The PostgreSQL Development Group, are essential to the PostgreSQL database engine's adoption and use and make up the PostgreSQL ecosystem writ large.\n\nPostgreSQL was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley. In 1996, the project was renamed PostgreSQL to reflect its support for SQL. After a review in 2007, the development team decided to keep the name PostgreSQL and the alias Postgres.\n\nHistory\n\nIngres and University POSTGRES (1982–1994)\n\nPostgreSQL evolved from the Ingres project at the University of California, Berkeley. In 1982, the leader of the Ingres team, Michael Stonebraker, left Berkeley to make a proprietary version of Ingres. He returned to Berkeley in 1985, and began a post-Ingres project to address the problems with contemporary database systems that had become increasingly clear during the early 1980s. He won the Turing Award in 2014 for these and other projects, and techniques pioneered in them.\n\nThe new project, POSTGRES, aimed to add the fewest features needed to completely support data types. These features included the ability to define types and to fully describe relationships – something used widely, but maintained entirely by the user. In POSTGRES, the database understood relationships, and could retrieve information in related tables in a natural way using rules. POSTGRES used many of the ideas of Ingres, but not its code.\n\nStarting in 1986, published papers described the basis of the system, and a prototype version was shown at the 1988 ACM SIGMOD Conference. The team released version 1 to a small number of users in June 1989, followed by version 2 with a re-written rules system in June 1990. Version 3, released in 1991, again re-wrote the rules system, and added support for multiple storage managers and an improved query engine. By 1993, the number of users began to overwhelm the project with requests for support and features. After releasing version 4.2 on June 30, 1994 – primarily a cleanup – the project ended. Berkeley released POSTGRES under an MIT License variant, which enabled other developers to use the code for any use. At the time, POSTGRES used an Ingres-influenced POSTQUEL query language interpreter, which could be interactively used with a console application named monitor. \n\nPostgres95 (1994–1996)\n\nIn 1994, Berkeley graduate students Andrew Yu and Jolly Chen replaced the POSTQUEL query language interpreter with one for the SQL query language, creating Postgres95. The monitor console was also replaced by psql. Yu and Chen announced the first version (0.01) to beta testers on May 5, 1995. Version 1.0 of Postgres95 was announced on September 5, 1995, with a more liberal license that enabled the software to be freely modifiable.\n\nOn July 8, 1996, Marc Fournier at Hub.org Networking Services provided the first non-university development server for the open-source development effort. With the participation of Bruce Momjian and Vadim B. Mikheev, work began to stabilize the code inherited from Berkeley.\n\nPostgreSQL (1996–present)\n\nIn 1996, the project was renamed to PostgreSQL to reflect its support for SQL. The online presence at the website PostgreSQL.org began on October 22, 1996. The first PostgreSQL release formed version 6.0 on January 29, 1997. Since then developers and volunteers around the world have maintained the software as The PostgreSQL Global Development Group.\n\nThe project continues to make releases available under its free and open-source software PostgreSQL License. Code comes from contributions from proprietary vendors, support companies, and open-source programmers.\n\nPostgreSQL 18, released on September 25, 2025, introduced a new asynchronous I/O (AIO) subsystem, enabling database users to perform concurrent I/O tasks like readahead and sequential scan and demonstrating up to a 3x performance improvement for storage reads in some workloads. The release also added support for planner statistics to persist across major-version upgrades, reducing the performance degradation that previously occurred while statistics were rebuilt after an upgrade. As of mid-2026, PostgreSQL 19 was in beta testing, with a general release anticipated later in the year.\n\nMultiversion concurrency control (MVCC)\n\nPostgreSQL manages concurrency through multiversion concurrency control (MVCC), which gives each transaction a \"snapshot\" of the database, allowing changes to be made without affecting other transactions. This largely eliminates the need for read locks, and ensures the database maintains ACID principles. PostgreSQL offers four levels of transaction isolation: Read Uncommitted, Read Committed, Repeatable Read and Serializable. Because PostgreSQL is immune to dirty reads, requesting a Read Uncommitted transaction isolation level provides read committed instead. PostgreSQL supports full serializability via the serializable snapshot isolation (SSI) method. The PostgreSQL MVCC implementation is prone to performance issues that require tuning when under a heavy write load which updates existing rows.\n\nStorage and replication\n\nReplication\n\nPostgreSQL includes built-in binary replication based on shipping the changes (write-ahead logs (WAL)) to replica nodes asynchronously, with the ability to run read-only queries against these replicated nodes. This allows splitting read traffic among multiple nodes efficiently. Earlier replication software that allowed similar read scaling normally relied on adding replication triggers to the master, increasing load.\n\nPostgreSQL includes built-in synchronous replication that ensures that, for each write transaction, the master waits until at least one replica node has written the data to its transaction log. Unlike other database systems, the durability of a transaction (whether it is asynchronous or synchronous) can be specified per-database, per-user, per-session or even per-transaction. This can be useful for workloads that do not require such guarantees, and may not be wanted for all data as it slows down performance due to the requirement of the confirmation of the transaction reaching the synchronous standby.\n\nStandby servers can be synchronous or asynchronous. Synchronous standby servers can be specified in the configuration which determines which servers are candidates for synchronous replication. The first in the list that is actively streaming will be used as the current synchronous server. When this fails, the system fails over to the next in line.\n\nPostgreSQL's replication can trigger conflicts between the primary and standby servers, particularly whenever tuples are prematurely deleted from the standby server despite ongoing queries accessing them. To address this, PostgreSQL includes a feedback flag where the standby server proactively informs the primary server of any ongoing queries to mitigate this type of conflict.\n\nSynchronous multi-master replication is not included in the PostgreSQL core. Postgres-XC which is based on PostgreSQL provides scalable synchronous multi-master replication. It is licensed under the same license as PostgreSQL. A related project is called Postgres-XL. Postgres-R is yet another fork. Bidirectional replication (BDR) is an asynchronous multi-master replication system for PostgreSQL.\n\nTools such as repmgr make managing replication clusters easier.\n\nSeveral asynchronous trigger-based replication packages are available. These remain useful even after introduction of the expanded core abilities, for situations where binary replication of a full database cluster is inappropriate:\n\nSlony-I\n\nLondiste, part of SkyTools (developed by Skype)\n\nBucardo multi-master replication (developed by Backcountry.com)\n\nSymmetricDS multi-master, multi-tier replication\n\nIndexes\n\nPostgreSQL includes built-in support for regular B-tree and hash table indexes, and four index access methods: generalized search trees (GiST), generalized inverted indexes (GIN), Space-Partitioned GiST (SP-GiST) and Block Range Indexes (BRIN). In addition, user-defined index methods can be created, although this is quite an involved process. Indexes in PostgreSQL also support the following features:\n\nExpression indexes can be created with an index of the result of an expression or function, instead of simply the value of a column.\n\nPartial indexes, which only index part of a table, can be created by adding a WHERE clause to the end of the CREATE INDEX statement. This allows for a smaller index to be created.\n\nThe planner is able to use multiple indexes together to satisfy complex queries, using temporary in-memory bitmap index operations (useful for data warehouse applications for joining a large fact table to smaller dimension tables such as those arranged in a star schema).\n\nk-nearest neighbors (k-NN) indexing (also referred to KNN-GiST) provides efficient searching of \"closest values\" to that specified, useful to finding similar words, or close objects or locations with geospatial data. This is achieved without exhaustive matching of values.\n\nIndex-only scans often allow the system to fetch data from indexes without ever having to access the main table.\n\nBlock Range Indexes (BRIN).\n\nSchemas\n\nPostgreSQL schemas are namespaces, allowing objects of the same kind and name to co-exist in a single database.\nThey are not to be confused with a\ndatabase schema—the abstract, structural, organizational specification which defines how every table's data relates to data within other tables.\nAll PostgreSQL database objects, except for a few global objects such as roles and tablespaces, exist within a schema.\nThey cannot be nested, schemas cannot contain schemas. \nThe permission system controls access to schemas and their content.\nBy default, newly created databases have only a single schema called public but other schemas can be added and the public schema isn't mandatory.\n\nA search_path setting determines the order in which PostgreSQL checks schemas for unqualified objects (those without a prefixed schema). By default, it is set to $user, public ($user refers to the currently connected database user). This default can be set on a database or role level, but as it is a session parameter, it can be freely changed (even multiple times) during a client session, affecting that session only.\n\nNon-existent schemas, or other schemas not accessible to the logged-in user, that are listed in search_path are silently skipped during object lookup.\n\nNew objects are created in whichever valid schema (one that can be accessed) appears first in the search_path.\n\nData types\n\nA wide variety of native data types are supported, including:\n\nBoolean\n\nArbitrary-precision numerics\n\nCharacter (text, varchar, char)\n\nBinary\n\nDate/time (timestamp/time with/without time zone, date, interval)\n\nMoney\n\nEnum\n\nBit strings\n\nText search type\n\nComposite\n\nHStore, an extension enabled key–value store within PostgreSQL\n\nArrays (variable-length and can be of any data type, including text and composite types) up to 1 GB in total storage size\n\nGeometric primitives\n\nIPv4 and IPv6 addresses\n\nClassless Inter-Domain Routing (CIDR) blocks and MAC addresses\n\nXML supporting XPath queries\n\nUniversally unique identifier (UUID)\n\nJavaScript Object Notation (JSON), and a faster binary JSONB (not the same as BSON)\n\nIn addition, users can create their own data types which can usually be made fully indexable via PostgreSQL's indexing infrastructures – GiST, GIN, SP-GiST. Examples of these include the geographic information system (GIS) data types from the PostGIS project for PostgreSQL.\n\nThere is also a data type called a domain, which is the same as any other data type but with optional constraints defined by the creator of that domain. This means any data entered into a column using the domain will have to conform to whichever constraints were defined as part of the domain.\n\nA data type that represents a range of data can be used which are called range types. These can be discrete ranges (e.g. all integer values 1 to 10) or continuous ranges (e.g., any time between 10:00 am and 11:00 am). The built-in range types available include ranges of integers, big integers, decimal numbers, time stamps (with and without time zone) and dates.\n\nCustom range types can be created to make new types of ranges available, such as IP address ranges using the inet type as a base, or float ranges using the float data type as a base. Range types support inclusive and exclusive range boundaries using the [] and () characters respectively. (e.g., [4,9) represents all integers starting from and including 4 up to but not including 9.) Range types are also compatible with existing operators used to check for overlap, containment, right of etc.\n\nUser-defined objects\n\nNew types of almost all objects inside the database can be created, including:\n\nCasts\n\nConversions\n\nData types\n\nData domains\n\nFunctions, including aggregate functions and window functions\n\nIndexes including custom indexes for custom types\n\nOperators (existing ones can be overloaded)\n\nProcedural languages\n\nInheritance\n\nTables can be set to inherit their characteristics from a parent table. Data in child tables will appear to exist in the parent tables, unless data is selected from the parent table using the ONLY keyword, i.e. SELECT * FROM ONLY parent_table;. Adding a column in the parent table will cause that column to appear in the child table.\n\nInheritance can be used to implement table partitioning, using either triggers or rules to direct inserts to the parent table into the proper child tables.\n\nThis feature is not fully supported. In particular, table constraints are not currently inheritable. All check constraints and not-null constraints on a parent table are automatically inherited by its children. Other types of constraints (unique, primary key, and foreign key constraints) are not inherited.\n\nInheritance provides a way to map the features of generalization hierarchies depicted in entity–relationship diagrams (ERDs) directly into the PostgreSQL database.\n\nOther storage features\n\nReferential integrity constraints including foreign key constraints, column constraints, and row checks\n\nBinary and textual large-object storage\n\nTablespaces\n\nPer-column collation\n\nOnline backup\n\nPoint-in-time recovery, implemented using write-ahead logging\n\nIn-place upgrades with pg_upgrade for less downtime\n\nControl and connectivity\n\nForeign data wrappers\n\nPostgreSQL can link to other systems to retrieve data via foreign data wrappers (FDWs).\nThese can take the form of any data source, such as a file system, another relational database management system (RDBMS), or a web service. This means that regular database queries can use these data sources like regular tables, and even join multiple data-sources together.\n\nInterfaces\n\nPostgreSQL supports a binary communication protocol that allows applications to connect to the database server. The protocol is versioned (currently 3.0, as of PostgreSQL 7.4) and has a detailed specification.\n\nThe official client implementation of this communication protocol is a C API, libpq. In addition, the officially supported ECPG tool allows SQL commands to be embedded in C code. Both are part of the standard PostgreSQL distribution.\n\nThird-party libraries for connecting to PostgreSQL are available for many programming languages, including C++, Java, Julia, Python, Node.js, Go, and Rust.\n\nProcedural languages\n\nProcedural languages allow developers to extend the database with custom subroutines (functions), often called stored procedures. These functions can be used to build database triggers (functions invoked on modification of certain data) and custom data types and aggregate functions. Procedural languages can also be invoked without defining a function, using a DO command at SQL level.\n\nLanguages are divided into two groups: Procedures written in safe languages are sandboxed and can be safely created and used by any user. Procedures written in unsafe languages can only be created by superusers, because they allow bypassing a database's security restrictions, but can also access sources external to the database. Some languages like Perl provide both safe and unsafe versions.\n\nPostgreSQL has built-in support for three procedural languages:\n\nPlain SQL (safe). Simpler SQL functions can get expanded inline into the calling (SQL) query, which saves function call overhead and allows the query optimizer to \"see inside\" the function.\n\nProcedural Language/PostgreSQL (PL/pgSQL) (safe), which resembles Oracle's Procedural Language for SQL (PL/SQL) procedural language and SQL/Persistent Stored Modules (SQL/PSM).\n\nC (unsafe), which allows loading one or more custom shared library into the database. Functions written in C offer the best performance, but bugs in code can crash and potentially corrupt the database. Most built-in functions are written in C.\n\nIn addition, PostgreSQL allows procedural languages to be loaded into the database through extensions. Three language extensions are included with PostgreSQL to support Perl, Tcl, and Python. For Python, the current Python 3 is used, and the discontinued Python 2 is no longer supported as of PostgreSQL 15. Both were supported previously, defaulting to Python 2, while old and new versions couldn't be used in the same session. External projects provide support for many other languages, including PL/Java, JavaScript (PL/V8), PL/Julia, PL/R, PL/Ruby, and others.\n\nTriggers\n\nTriggers are events triggered by the action of SQL data manipulation language (DML) statements. For example, an INSERT statement might activate a trigger that checks if the values of the statement are valid. Most triggers are only activated by either INSERT or UPDATE statements.\n\nTriggers are fully supported and can be attached to tables. Triggers can be per-column and conditional, in that UPDATE triggers can target specific columns of a table, and triggers can be told to execute under a set of conditions as specified in the trigger's WHERE clause. Triggers can be attached to views by using the INSTEAD OF condition. Multiple triggers are fired in alphabetical order. In addition to calling functions written in the native PL/pgSQL, triggers can also invoke functions written in other languages like PL/Python or PL/Perl.\n\nAsynchronous notifications\n\nPostgreSQL provides an asynchronous messaging system that is accessed through the NOTIFY, LISTEN and UNLISTEN commands. A session can issue a NOTIFY command, along with the user-specified channel and an optional payload, to mark a particular event occurring. Other sessions are able to detect these events by issuing a LISTEN command, which can listen to a particular channel. This functionality can be used for a wide variety of purposes, such as letting other sessions know when a table has updated or for separate applications to detect when a particular action has been performed. Such a system prevents the need for continuous polling by applications to see if anything has yet changed, and reducing unnecessary overhead. Notifications are fully transactional, in that messages are not sent until the transaction they were sent from is committed. This eliminates the problem of messages being sent for an action being performed which is then rolled back.\n\nMany connectors for PostgreSQL provide support for this notification system (including libpq, JDBC, Npgsql, psycopg and node.js) so it can be used by external applications.\n\nPostgreSQL can act as an effective, persistent \"pub/sub\" server or job server by combining LISTEN with FOR UPDATE SKIP LOCKED.\n\nRules\n\nRules allow the"
 },
 {
  "title": "Pg (Unix)",
  "revision_id": "1346966578",
  "matched_by": "title-minus-qualifier",
  "text": "pg is a terminal pager program on Unix and Unix-like systems for viewing text files. It can also be used to page through the output of a command via a pipe. pg uses an interface similar to vi, but commands are different.\n\nAs of 2018, pg has been removed from the POSIX specification, but is still included in util-linux. Users are expected to use other paging programs, such as more, less or most.\n\nHistory\n\npg is the name of the historical utility on BSD UNIX systems. It was written to address the limit of the historical more command not being able to traverse the input backward. Eventually that ability was added also to more, so both are quite similar.\n\nReferences"
 },
 {
  "title": "PG(3,2)",
  "revision_id": "1357206887",
  "matched_by": "title-minus-qualifier",
  "text": "In finite geometry, PG(3, 2) is the smallest three-dimensional projective space. It can be thought of as an extension of the Fano plane, PG(2, 2).\n\nElements\n\nIt has 15 points, 35 lines, and 15 planes. Each point is contained in 7 lines and 7 planes. Each line is contained in 3 planes and contains 3 points. Each plane contains 7 points and 7 lines.\n\nThese can be summarized in a rank 3 configuration matrix counting points, lines, and planes on the diagonal. The incidences are expressed off diagonal. The structure is self dual, swapping points and planes, expressed by rotating the configuration matrix 180 degrees.\n\nIt has the following properties:\n\nEach plane is isomorphic to the Fano plane.\n\nEvery pair of distinct planes intersects in a line.\n\nA line and a plane not containing the line intersect in exactly one point.\n\nPG(3, 2) has 20160 automorphisms. The number of automorphisms is given by finding the number of ways of selecting 4 points that are not coplanar; this works out to (2-1)(2-2)(2-2)(2-2)/(2-1) = 15⋅14⋅12⋅8.\n\nThe 15 planes can be generated by a block design difference set (0,1,2,4,5,8,10). The 35 lines can be generated by pairwise plane point intersections, each containing 3 points.\n\nRelated affine spaces\n\nIf one plane is removed (and its 7 points and 7 lines), we create the affine space AG(3,2), composed of 7 sets of 2 parallel planes (each K4 graphs). The 8 points and 28 lines alone make a complete graph K8 graph. It has 20160/15 = 1344 automorphisms.\n\nRemoving one point (and its 7 lines and 7 planes) further creates a smaller self dual rank 3 configuration of 7 points, 21 lines and 7 K4 graph planes. Automorphisms reduce to 168 (1344/8).\n\nThis design is 74, and also set complement to fano plane, 73. Since 73 has difference set (1,2,4), 74 planes are the complement set (0,3,5,6). The 21 lines contain 2 points as pairwise intersections of the planes.\n\nConstructions\n\nConstruction from K6\n\nTake a complete graph K6. It has 15 edges, 15 perfect matchings and 20 triangles. Create a point for each of the 15 edges, and a line for each of the 20 triangles and 15 matchings. The incidence structure between each triangle or matching (line) and its three constituent edges (points) induces a PG(3, 2).\n\nConstruction from Fano planes\n\nTake a Fano plane and apply all 5040 permutations of its 7 points. Discard duplicate planes to obtain a set of 30 distinct Fano planes. Pick any of the 30, and pick the 14 others that have exactly one line in common with the first, not 0 or 3. The incidence structure between the 1 + 14 = 15 Fano planes and the 35 triplets they mutually cover induces a PG(3, 2).\n\nRepresentations\n\nTetrahedral depiction\n\nPG(3, 2) can be represented as a tetrahedron. The 15 points correspond to the 4 vertices + 6 edge-midpoints + 4 face-centers + 1 body-center. The 35 lines correspond to the 6 edges + 12 face-medians + 4 face-incircles + 4 altitudes from a face to the opposite vertex + 3 lines connecting the midpoints of opposite edges + 6 ellipses connecting each edge midpoint with its two non-neighboring face centers. The 15 planes consist of the 4 faces + the 6 \"medial\" planes connecting each edge to the midpoint of the opposite edge + 4 \"cones\" connecting each vertex to the incircle of the opposite face + one \"sphere\" with the 6 edge centers and the body center. This was described by Burkard Polster. The tetrahedral depiction has the same structure as the visual representation of the multiplication table for the sedenions.\n\nNumbering the points 0...14 (4 (v)ertices, 6 mid-(e)dges, 4 mid-(f)aces, and 1 (c)entral), the 15 planes and 35 lines of the configuration can be grouped by symmetry positions in the tetrahedron:\n\nSquare representation\n\nPG(3, 2) can be represented as a square. The 15 points are assigned 4-bit binary coordinates from 0001 to 1111, augmented with a point labeled 0000, and arranged in a 4×4 grid. Lines correspond to the equivalence classes of sets of four vertices that XOR together to 0000. With certain arrangements of the vertices in the 4×4 grid, such as the \"natural\" row-major ordering or the Karnaugh map ordering, the lines form symmetric sub-structures like rows, columns, transversals, or rectangles, as seen in the figure. (There are 20160 such orderings, as seen below in the section on Automorphisms.) This representation is possible because geometrically the 35 lines are represented as a bijection with the 35 ways to partition a 4×4 affine space into 4 parallel planes of 4 cells each. This was described by Steven H. Cullinane.\n\nSedenion representation\n\nDoily depiction\n\nThe Doily diagram often used to represent the generalized quadrangle GQ(2, 2) is also used to represent PG(3, 2). This was described by Richard Doily.\n\nKirkman's schoolgirl problem\n\nPG(3, 2) arises as a background in some solutions of Kirkman's schoolgirl problem. Two of the seven non-isomorphic solutions to this problem can be embedded as structures in the Fano 3-space. In particular, a spread of PG(3, 2) is a partition of points into disjoint lines, and corresponds to the arrangement of girls (points) into disjoint rows (lines of a spread) for a single day of Kirkman's schoolgirl problem. There are 56 different spreads of 5 lines each. A packing of PG(3, 2) is a partition of the 35 lines into 7 disjoint spreads of 5 lines each, and corresponds to a solution for all seven days. There are 240 packings of PG(3, 2), that fall into two conjugacy classes of 120 under the action of PGL(4, 2) (the collineation group of the space); a correlation interchanges these two classes.\n\nCoordinates\n\nIt is known that a PG(n, 2) can be coordinatized with (GF(2)), i.e. a bit string of length n + 1. PG(3, 2) can therefore be coordinatized with 4-bit strings.\n\nIn addition, the line joining points (a1, a2, a3, a4) and (b1, b2, b3, b4) can be naturally assigned Plücker coordinates (p12, p13, p14, p23, p24, p34) where pij = aibj − ajbi, and the line coordinates satisfy p12 p34 + p13 p24 + p14 p23 = 0. Each line in projective 3-space thus has six coordinates, and can be represented as a point in projective 5-space; the points lie on the surface p12 p34 + p13 p24 + p14 p23 = 0.\n\nNotes"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q192490",
  "label": "PostgreSQL",
  "description": "free and open-source relational database management system",
  "aliases": [],
  "claims": {
   "P31": [
    "Q3932296",
    "Q114901705",
    "Q341"
   ],
   "P527": [
    "Q2044345",
    "Q4046208",
    "Q4046204",
    "Q4046205"
   ],
   "P1889": [
    "Q141475192"
   ]
  },
  "revision_id": "2572198437",
  "value_labels": {
   "Q3932296": "relational database management system",
   "Q114901705": "SQL server",
   "Q341": "free software",
   "Q2044345": "PL/pgSQL",
   "Q4046208": "PL/Perl",
   "Q4046204": "PL/Python",
   "Q4046205": "PL/Tcl",
   "Q141475192": "Prisma Postgres"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7179836",
  "label": "pg",
  "description": "terminal pager program",
  "aliases": [],
  "claims": {
   "P31": [
    "Q18343316",
    "Q959462"
   ]
  },
  "revision_id": "2492208001",
  "value_labels": {
   "Q18343316": "standard UNIX utility or command",
   "Q959462": "terminal pager"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q63490825",
  "label": "PG(3,2)",
  "description": "smallest 3D projective space",
  "aliases": [],
  "claims": {
   "P31": [
    "Q877775"
   ]
  },
  "revision_id": "2491483261",
  "value_labels": {
   "Q877775": "projective space"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3932296",
  "label": "relational database management system",
  "description": "DBMS that is based on the relational model",
  "aliases": [
   "RDBMS",
   "relational database"
  ],
  "claims": {
   "P279": [
    "Q176165"
   ],
   "P1889": [
    "Q192588"
   ]
  },
  "revision_id": "2485250975",
  "ancestor_of": "Q192490",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q114901705",
  "label": "SQL server",
  "description": "service which answers queries written in SQL",
  "aliases": [
   "SQL endpoint"
  ],
  "claims": {
   "P279": [
    "Q114901571"
   ]
  },
  "revision_id": "2548121311",
  "ancestor_of": "Q192490",
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
  "ancestor_of": "Q192490",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q176165",
  "label": "database management system",
  "description": "software for running databases; computer-software application that interacts with end-users, other applications, and the database itself to capture and analyze data; allows the definition, creation, querying, update, and administration of databases",
  "aliases": [
   "DBMS",
   "database-management system",
   "database",
   "database system",
   "database management systems"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q2429814"
   ],
   "P361": [
    "Q8513",
    "Q868996"
   ],
   "P527": [
    "Q19631771",
    "Q19631768",
    "Q19631769",
    "Q537993"
   ]
  },
  "revision_id": "2531215697",
  "ancestor_of": "Q192490",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q114901571",
  "label": "query server",
  "description": "service which answers queries written in a query language",
  "aliases": [
   "query service"
  ],
  "claims": {
   "P279": [
    "Q1371279"
   ]
  },
  "revision_id": "2430889789",
  "ancestor_of": "Q192490",
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
  "ancestor_of": "Q192490",
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
  "ancestor_of": "Q192490",
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
  "ancestor_of": "Q192490",
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
  "ancestor_of": "Q192490",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q18343316",
  "label": "standard UNIX utility or command",
  "description": "command or utility specified by IEEE Std 1003.1-2008",
  "aliases": [
   "POSIX utility",
   "UNIX utility",
   "UNIX command",
   "POSIX command",
   "POSIX standard utilities",
   "POSIX standard commands",
   "UNIX standard utilities",
   "UNIX standard commands",
   "POSIX standards"
  ],
  "claims": {
   "P31": [
    "Q16887380"
   ],
   "P279": [
    "Q1461523",
    "Q1079196",
    "Q30059018",
    "Q115214659"
   ]
  },
  "revision_id": "2548029445",
  "ancestor_of": "Q7179836",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q959462",
  "label": "terminal pager",
  "description": "console application used to view large amounts of text interactively",
  "aliases": [
   "pager",
   "paging program",
   "paginator",
   "pager program"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q40056",
    "Q1461523"
   ],
   "P1889": [
    "Q656083"
   ]
  },
  "revision_id": "2538888390",
  "ancestor_of": "Q7179836",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16887380",
  "label": "group",
  "description": "well-defined, enumerable collection of discrete entities that form a collective whole",
  "aliases": [
   "group of",
   "group of objects",
   "grouping",
   "object grouping",
   "object group",
   "collection",
   "lineup",
   "branch",
   "group of things",
   "group of entities",
   "thing grouping",
   "thing group",
   "entity grouping",
   "entity group",
   "group of individual things"
  ],
  "claims": {
   "P31": [
    "Q5962346"
   ],
   "P279": [
    "Q28813620"
   ],
   "P527": [
    "Q35120",
    "Q36809769",
    "Q36808958"
   ],
   "P1889": [
    "Q36161",
    "Q12139612",
    "Q133250",
    "Q83306",
    "Q83478",
    "Q2668072",
    "Q1514741",
    "Q63341786",
    "Q16889133",
    "Q111360549",
    "Q824979",
    "Q215380",
    "Q141131708"
   ]
  },
  "revision_id": "2560437842",
  "ancestor_of": "Q7179836",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1461523",
  "label": "console application",
  "description": "computer program designed to be used via a text-only computer interface",
  "aliases": [
   "terminal application",
   "console app",
   "command-line application",
   "command-line app",
   "command line application",
   "CLI app",
   "CLI program",
   "command-line program"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q166142"
   ],
   "P1889": [
    "Q115214659"
   ]
  },
  "revision_id": "2557686323",
  "ancestor_of": "Q7179836",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1079196",
  "label": "command",
  "description": "directive to a computer program",
  "aliases": [
   "directive",
   "operation",
   "instruction"
  ],
  "claims": {
   "P279": [
    "Q1665268",
    "Q12579633"
   ],
   "P361": [
    "Q124590",
    "Q613299"
   ],
   "P1889": [
    "Q115214659",
    "Q122830712"
   ]
  },
  "revision_id": "2572742481",
  "ancestor_of": "Q7179836",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q30059018",
  "label": "operating system component",
  "description": "type of component",
  "aliases": [
   "OS component"
  ],
  "claims": {
   "P279": [
    "Q17176533"
   ],
   "P361": [
    "Q9135"
   ]
  },
  "revision_id": "2382810937",
  "ancestor_of": "Q7179836",
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
  "ancestor_of": "Q7179836",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q40056",
  "label": "computer program",
  "description": "sequence of instructions written in programming language to perform a specified task with a computer",
  "aliases": [
   "program",
   "software program"
  ],
  "claims": {
   "P279": [
    "Q4303335",
    "Q11491547",
    "Q141543245"
   ],
   "P361": [
    "Q1143070",
    "Q7397",
    "Q56822593"
   ],
   "P1889": [
    "Q205663"
   ]
  },
  "revision_id": "2565022818",
  "ancestor_of": "Q7179836",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q877775",
  "label": "projective space",
  "description": "space of 1-dimensional linear subspaces (lines passing through the origin) in a vector space",
  "aliases": [],
  "claims": {
   "P279": [
    "Q1528306",
    "Q129638",
    "Q3554829",
    "Q7248935",
    "Q3554818",
    "Q7249479"
   ]
  },
  "revision_id": "2563729680",
  "ancestor_of": "Q63490825",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1528306",
  "label": "toric variety",
  "description": "algebraic variety containing an algebraic torus as an open dense subset, such that the action of the torus on itself extends to the whole variety, which can be combinatorially encoded via systems of cones (“fans”) or polytopes",
  "aliases": [
   "torus embedding"
  ],
  "claims": {
   "P279": [
    "Q648995"
   ]
  },
  "revision_id": "2474015585",
  "ancestor_of": "Q63490825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q129638",
  "label": "Grassmannian",
  "description": "space of linear subspaces of a fixed vector space",
  "aliases": [
   "Grassmann manifold"
  ],
  "claims": {
   "P31": [
    "Q24034552"
   ],
   "P279": [
    "Q78347520",
    "Q78338964"
   ]
  },
  "revision_id": "2563519724",
  "ancestor_of": "Q63490825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3554829",
  "label": "rational variety",
  "description": "algebraic variety over a field K birationally equivalent to a projective space of some dimension over K",
  "aliases": [],
  "claims": {
   "P279": [
    "Q648995"
   ],
   "P361": [
    "Q180969"
   ]
  },
  "revision_id": "2542238982",
  "ancestor_of": "Q63490825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7248935",
  "label": "Proj construction",
  "description": "scheme constructed from a commutative graded ring, whose points correspond to homogeneous prime ideals that do not contain all of positive-degree elements",
  "aliases": [],
  "claims": {
   "P31": [
    "Q18199114"
   ],
   "P279": [
    "Q36161"
   ],
   "P1889": [
    "Q91443379",
    "Q1154351"
   ]
  },
  "revision_id": "2222818480",
  "ancestor_of": "Q63490825",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 3: Python (`pk7cebmtg6`)

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
[
 {
  "title": "Python (programming language)",
  "revision_id": "1378728329",
  "matched_by": "title",
  "text": "Python is a high-level, general-purpose programming language that emphasizes code readability, simplicity, and ease-of-writing with the use of significant indentation, an extensive (\"batteries-included\") standard library, and garbage collection. Python supports multiple programming paradigms but with an emphasis on object-oriented programming and dynamic typing.\n\nGuido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language. Python 3.0, released in 2008, was a major revision and not completely backward-compatible with earlier versions. Beginning with Python 3.5, capabilities and keywords for typing were added to the language, allowing optional static typing. As of 2026, the Python Software Foundation supports Python 3.11, 3.12, 3.13, and 3.14, following the project's annual release cycle and five-year support policy. Python 3.15.0rc3 (which defaults to UTF-8) is out in preview, a \"surprise third release candidate for Python 3.15.0! .. so this week’s planned 3.15.0 final is postponed until October 9th, 2026\" to allow more users to test it. Earlier versions in the 3.x series have reached end-of-life and no longer receive security updates. \n\nPython is widely taught as an introductory programming language.\n\nHistory\n\nPython was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands. It was designed as a successor to the ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Python implementation began in December 1989. Van Rossum first released it in 1991 as Python 0.9.0. Van Rossum assumed sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his \"permanent vacation\" from responsibilities as Python's \"benevolent dictator for life\" (BDFL); this title was bestowed on him by the Python community to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a five-member Steering Council to lead the project.\n\nThe name Python derives from the British comedy series Monty Python's Flying Circus. (See § Naming.)\n\nPython 2.0 was released on 16 October 2000, featuring many new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 2.7's end-of-life was initially set for 2015, and then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. It no longer receives security patches or updates. While Python 2.7 and older versions are officially unsupported, a different unofficial Python implementation, PyPy, continues to support Python 2, i.e., \"2.7.18+\" (plus 3.11 and 3.12), with the plus signifying (at least some) \"backported security updates\".\n\nPython 3.0 was released on 3 December 2008, and was a major revision and not completely backward-compatible with earlier versions, with some new semantics and changed syntax. Python 2.7.18, released in 2020, was the last release of Python 2. Several releases in the Python 3.x series have added new syntax to the language, and made a few (considered very minor) backward-incompatible changes.\n\nAs of October 2026, Python 3.14.8 an \"expedited security release\" is the latest stable release, and since 3.14 official Android binary releases are available. All older 3.x versions had a security update down to Python 3.10.22. Python 3.11 is, since October 2026, the oldest supported branch. Python 3.15 has release candidate 3 out, it is the final planned release candidate and adds e.g. frozendict and sentinel built-in types, and a new soft keyword, lazy, for lazy imports. Releases receive two years of full support followed by three years of security support.\n\nDesign philosophy and features\n\nPython is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of their features support functional programming and aspect-oriented programming – including metaprogramming and metaobjects. Many other paradigms are supported via extensions, including design by contract and logic programming. Python is often referred to as a ‘glue language’ because it is purposely designed to be able to integrate components written in other languages.\n\nPython uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management. It uses dynamic name resolution (late binding), which binds method and variable names during program execution.\n\nPython's design offers some support for functional programming in the \"Lisp tradition\". It has filter, map, and reduce functions; list comprehensions, dictionaries, sets, and generator expressions. The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.\n\nPython's core philosophy is summarized in the Zen of Python (PEP 20) written by Tim Peters, which includes aphorisms such as these:\n\nExplicit is better than implicit.\n\nSimple is better than complex.\n\nReadability counts.\n\nSpecial cases aren't special enough to break the rules.\n\nAlthough practicality beats purity, errors should never pass silently, unless explicitly silenced.\n\nThere should be one—and preferably only one—obvious way to do it.\n\nHowever, Python has received criticism for violating these principles and adding unnecessary language bloat. Responses to these criticisms note that the Zen of Python is a guideline rather than a rule. The addition of some new features had been controversial: Guido van Rossum resigned as Benevolent Dictator for Life after conflict about adding the assignment expression operator in Python 3.8.\n\nNevertheless, rather than building all functionality into its core, Python was designed to be highly extensible through modules. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and an easily extensible interpreter stemmed from his frustrations with ABC, which represented the opposite approach.\n\nPython claims to strive for a simpler, less-cluttered syntax and grammar, while giving developers a choice in their coding methodology. Python lacks do .. while loops, which Rossum considered harmful. In contrast to Perl's motto \"there is more than one way to do it\", Python advocates an approach where \"there should be one – and preferably only one – obvious way to do it\". In practice, however, Python provides many ways to achieve a given goal. There are at least three ways to format a string literal, with no certainty as to which one a programmer should use. Alex Martelli is a Fellow at the Python Software Foundation and Python book author; he wrote that \"To describe something as 'clever' is not considered a compliment in the Python culture.\"\n\nPython's developers typically prioritize readability over performance. For example, they reject patches to non-critical parts of the CPython reference implementation that would offer increases in speed that do not justify the cost of clarity and readability. Execution speed can be improved by moving speed-critical functions to extension modules written in languages such as C, or by using a just-in-time compiler like PyPy. Also, it is possible to transpile to other languages. However, this approach either fails to achieve the expected speed-up, since Python is a very dynamic language, or only a restricted subset of Python is compiled (with potential minor semantic changes).\n\nPython is meant to be a fun language to use. This goal is reflected in the name – a tribute to the British comedy group Monty Python – and in playful approaches to some tutorials and reference materials. For instance, some code examples use the terms \"spam\" and \"eggs\" (in reference to a Monty Python sketch), rather than the typical terms \"foo\" and \"bar\".\n\nA common neologism in the Python community is pythonic, which has a broad range of meanings related to program style: Pythonic code may use Python idioms well; be natural or show fluency in the language; or conform with Python's minimalist philosophy and emphasis on readability.\n\nEnhancement Proposals\n\nPython Enhancement Proposals are a design document for either providing information to the Python community, or proposal for new feature in Python. PEPs are intended to explain new processes in Python, provide naming conventions or document the processes in the language. PEPs are overseen by Python Steering Council.\n\nThere are 3 kinds of PEPs, with those are being standards track PEP, Informational PEP and Process PEPs which has their own unique meanings. They were firstly introduced in 2000, inspired by other RfCs (requests for comments) and Design Enhancement Proposals. Most known PEPs are PEP – 1, PEP – 8, PEP – 20, PEP – 257 and others.\n\nSyntax and semantics\n\nPython is meant to be an easily readable language. Its formatting is visually uncluttered and often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are allowed but rarely used. It has fewer syntactic exceptions and special cases than C or Pascal.\n\nIndentation\n\nPython uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block. Thus, the program's visual structure accurately represents its semantic structure. This feature is sometimes termed the off-side rule. Some other languages use indentation this way; but in most, indentation has no semantic meaning. The recommended indent size is four spaces.\n\nStatements and control flow\n\nPython's statements include the following:\n\nThe assignment statement, using a single equals sign =\n\nThe if statement, which conditionally executes a block of code, along with else and elif (a contraction of else if)\n\nThe for statement, which iterates over an iterable object, capturing each element to a variable for use by the attached block; the variable is not deleted when the loop finishes\n\nThe while statement, which executes a block of code as long as boolean condition is true\n\nThe try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses (or new syntax except* in Python 3.11 for exception groups); the try statement also ensures that clean-up code in a finally block is always run regardless of how the block exits\n\nThe raise statement, used to raise a specified exception or re-raise a caught exception\n\nThe class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming\n\nThe def statement, which defines a function or method\n\nThe with statement, which encloses a code block within a context manager, allowing resource-acquisition-is-initialization (RAII)-like behavior and replacing a common try/finally idiom Examples of a context include acquiring a lock before some code is run, and then releasing the lock; or opening and then closing a file\n\nThe break statement, which exits a loop\n\nThe continue statement, which skips the rest of the current iteration and continues with the next\n\nThe del statement, which removes a variable—deleting the reference from the name to the value, and producing an error if the variable is referred to before it is redefined\n\nThe pass statement, serving as a NOP (i.e., no operation), which is syntactically needed to create an empty code block\n\nThe assert statement, used in debugging to check for conditions that should apply\n\nThe yield statement, which returns a value from a generator function (and also an operator); used to implement coroutines\n\nThe return statement, used to return a value from a function\n\nThe import and from statements, used to import modules whose functions or variables can be used in the current program. Python 3.15 adds a new functionality to lazily import with a new keyword: \"The lazy keyword works with both import and from ... import statements.\"\n\nThe match and case statements, analogous to a switch statement construct, which compares an expression against one or more cases as a control-flow measure\n\nThe assignment statement (=) binds a name as a reference to a separate, dynamically allocated object. Variables may subsequently be rebound at any time to any object. In Python, a variable name is a generic reference holder without a fixed data type; however, it always refers to some object with a type. This is called dynamic typing—in contrast to statically-typed languages, where each variable may contain only a value of a certain type.\n\nPython does not support tail call optimization or first-class continuations; according to Van Rossum, the language never will. However, better support for coroutine-like functionality is provided by extending Python's generators. Before 2.5, generators were lazy iterators; data was passed unidirectionally out of the generator. From Python 2.5 on, it is possible to pass data back into a generator function; and from version 3.3, data can be passed through multiple stack levels.\n\nExpressions\n\nPython's expressions include the following:\n\nThe +, -, and * operators for mathematical addition, subtraction, and multiplication are similar to other languages, but the behavior of division differs. There are two types of division in Python: floor division (or integer division) //, and floating-point division /. Python uses the ** operator for exponentiation.\n\nPython uses the + operator for string concatenation. The language uses the * operator for duplicating a string a specified number of times.\n\nThe @ infix operator is intended to be used by libraries such as NumPy for matrix multiplication.\n\nThe syntax :=, called the \"walrus operator\", was introduced in Python 3.8. This operator assigns values to variables as part of a larger expression.\n\nIn Python, == compares two objects by value. Python's is operator may be used to compare object identities (i.e., comparison by reference), and comparisons may be chained—for example, a <= b <= c.\n\nPython uses and, or, and not as Boolean operators.\n\nPython has a type of expression called a list comprehension, and a more general expression called a generator expression.\n\nAnonymous functions are implemented using lambda expressions; however, there may be only one expression in each body.\n\nConditional expressions are written as x if c else y. (This is different in operand order from the c ? x : y operator common to many other languages.)\n\nPython makes a distinction between lists and tuples. Lists are written as [1, 2, 3], are mutable, and cannot be used as the keys of dictionaries (since dictionary keys must be immutable in Python). Tuples, written as (1, 2, 3), are immutable and thus can be used as the keys of dictionaries, provided that all of the tuple's elements are immutable. The + operator can be used to concatenate two tuples, which does not directly modify their contents, but produces a new tuple containing the elements of both. For example, given the variable t initially equal to (1, 2, 3), executing t = t + (4, 5) first evaluates t + (4, 5), which yields (1, 2, 3, 4, 5); this result is then assigned back to t—thereby effectively \"modifying the contents\" of t while conforming to the immutable nature of tuple objects. Parentheses are optional for tuples in unambiguous contexts.\n\nPython features sequence unpacking where multiple expressions, each evaluating to something assignable (e.g., a variable or a writable property) are associated just as in forming tuple literal; as a whole, the results are then put on the left-hand side of the equal sign in an assignment statement. This statement expects an iterable object on the right-hand side of the equal sign to produce the same number of values as the writable expressions on the left-hand side; while iterating, the statement assigns each of the values produced on the right to the corresponding expression on the left.\n\nPython has a \"string format\" operator % that functions analogously to printf format strings in the C language—e.g. \"spam=%s eggs=%d\" % (\"blah\", 2) evaluates to \"spam=blah eggs=2\". In Python 2.6+ and 3+, this operator was supplemented by the format() method of the str class, e.g., \"spam={0} eggs={1}\".format(\"blah\", 2). Python 3.6 added \"f-strings\": spam = \"blah\"; eggs = 2; f'spam={spam} eggs={eggs}'.\n\nStrings in Python can be concatenated by \"adding\" them (using the same operator as for adding integers and floats); e.g., \"spam\" + \"eggs\" returns \"spameggs\". If strings contain numbers, they are concatenated as strings rather than as integers, e.g. \"2\" + \"2\" returns \"22\".\n\nPython supports string literals in several ways:\n\nDelimited by single or double quotation marks; single and double quotation marks have equivalent functionality (unlike in Unix shells, Perl, and Perl-influenced languages). Both marks use the backslash (\\) as an escape character. String interpolation became available in Python 3.6 as \"formatted string literals\".\n\nTriple-quoted, i.e., starting and ending with three single or double quotation marks; this may span multiple lines and function like here documents in shells, Perl, and Ruby.\n\nRaw string varieties, denoted by prefixing the string literal with r. Escape sequences are not interpreted; hence raw strings are useful where literal backslashes are common, such as in regular expressions and Windows-style paths. (Compare \"@-quoting\" in C#.)\n\nPython has array index and array slicing expressions in lists, which are written as a[key], a[start:stop] or a[start:stop:step]. Indexes are zero-based, and negative indexes are relative to the end. Slices take elements from the start index up to, but not including, the stop index. The (optional) third slice parameter, called step or stride, allows elements to be skipped or reversed. Slice indexes may be omitted—for example, a[:] returns a copy of the entire list. Each element of a slice is a shallow copy.\n\nIn Python, a distinction between expressions and statements is rigidly enforced, in contrast to languages such as Common Lisp, Scheme, or Ruby. This distinction leads to duplicating some functionality, for example:\n\nList comprehensions vs. for-loops\n\nConditional expressions vs. if blocks\n\nThe eval() vs. exec() built-in functions (in Python 2, exec is a statement); the former function is for expressions, while the latter is for statements\n\nA statement cannot be part of an expression; because of this restriction, expressions such as list and dict comprehensions (and lambda expressions) cannot contain statements. As a particular case, an assignment statement such as a = 1 cannot be part of the conditional expression of a conditional statement.\n\nTyping\n\nPython uses duck typing, and it has typed objects but untyped variable names. Type constraints are not checked at definition time; rather, operations on an object may fail at usage time, indicating that the object is not of an appropriate type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are poorly defined (e.g., adding a number and a string) rather than quietly attempting to interpret them.\n\nPython allows programmers to define their own types using classes, most often for object-oriented programming. New instances of classes are constructed by calling the class, for example, SpamClass() or EggsClass()); the classes are instances of the metaclass type (which is an instance of itself), thereby allowing metaprogramming and reflection.\n\nBefore version 3.0, Python had two kinds of classes, both using the same syntax: old-style and new-style. Current Python versions support the semantics of only the new style.\n\nPython supports optional type annotations. These annotations"
 },
 {
  "title": "Python (codename)",
  "revision_id": "1287107565",
  "matched_by": "redirect",
  "text": "Python was a Cold War contingency plan of the British Government for the continuity of government in the event of nuclear war.\n\nBackground\n\nFollowing the report of the Strath Committee in 1955, the British government developed contingency plans for the continuity of government. This included construction of the underground Central Government War Headquarters (CGWHQ), codenamed \"Burlington\", at Corsham in Wiltshire. As planned, it would have been a \"reserve Whitehall\" where the central government could be moved in an emergency and, hopefully, survive a nuclear attack.\n\nAs nuclear weapons became more powerful and intercontinental ballistic missiles became more of a threat than crewed bombers, the concept of concentrating central government in a single location became flawed. Instead, government would be dispersed around the country with just core functions at CGWHQ. The Cuban Missile Crisis of 1962 prompted a radical rethink of continuity plans. Part of the thinking was that the \"precautionary period\" ahead of nuclear war, or a conventional war in Europe culminating in nuclear war, might only last two or three days rather than the seven days originally planned, so it would not be possible to fully staff CGWHQ with 4,000 people in time.\n\nPython became active on 1 May 1968 and is described in the 1968 update to the Government War Book.\n\nLocations\n\nSites for dispersing government were selected in 1966 based on their existing accommodation, independence from the national power and water grids, nuclear fallout protection and distance from likely targets. The chosen sites were RNAS Culdrose in Cornwall, HMS Osprey in Dorset, Taymouth Castle (then the Civil Defence Corps Training School) in Scotland, and either the helicopter support ship RFA Engadine or royal yacht HMY Britannia which would embark a Python group at Loch Torridon or Oban. Tonfanau Army Camp was temporarily designated as the Python location for Wales with a view to moving the site to the Old College at Aberystwyth University (which housed the university's Department of Physics) as soon as possible. Each dispersed Python group would be supported by dispersed sections of the United Kingdom Supply Agency and the National Air Transport Agency.\n\nIn addition, in 1964 the Secretary of State for Scotland ordered three ships – MV Hebrides, MV Clansman and RMS Columba – which were chartered to David MacBrayne as car ferries but could be converted to floating nuclear bunkers in a very short time. They had heavy steel doors to seal the car deck, airtight external windows and doors, decontamination rooms with showers, and external sprinklers to wash away fallout. One or more of these ships would have accompanied RFA Engadine or HMY Britannia from Oban or Mallaig.\n\nThe Corsham bunker, given the new codename \"Turnstile\" from 1963 and \"Chanticleer\" from 1970, would play an important part in the lead up to war but ceased to have a CGWHQ role other than as a possible aggregation point for Python groups some time after an attack.\n\nGallery\n\nSee also"
 },
 {
  "title": "Python (mythology)",
  "revision_id": "1377073638",
  "matched_by": "title-minus-qualifier",
  "text": "In Greek mythology, Python (Ancient Greek: Πύθων; gen. Πύθωνος) was the serpent, sometimes represented as a medieval-style dragon, living at the center of the Earth, believed by the ancient Greeks to be at Delphi. He was killed by the god Apollo.\n\nMythology\n\nPython, sometimes written Pytho, presided at the Delphic oracle, which existed in the cult center for its mother, Gaia, \"Earth\", Pytho being the place name that was substituted for the earlier Krisa. Greeks considered the site to be the center of the Earth, represented by a stone, the omphalos or navel, which Python guarded.\n\nPython became the chthonic enemy of the later Olympian deity Apollo, who slew it and took over Python's former home and oracle. These were the most famous and revered in the ancient Greek and Roman worlds. Like many monsters, Python was known as Gaia's son. \nIn turn, Apollo had to eliminate him before he could establish a temple in Delphi.\n\nVersions and interpretations\n\nThere are various versions of Python's birth and death at the hands of Apollo. In the Homeric Hymn to Apollo, now thought to have been composed in 522 BC when the archaic period in Greek history was giving way to the Classical period, a small detail is provided regarding Apollo's combat with the serpent, in some sections identified as the deadly drakaina, or her parent. The god searching for a place to establish his shrine, reached Delphi and saw the Python, who was a bane to the people. He slew the serpent and declared himself as the owner of the Oracular shrine.\n\nThe version related by Hyginus holds that when Zeus lay with the goddess Leto, and she became pregnant with Artemis and Apollo, Hera was jealous and sent Python to pursue Leto throughout the lands, to prevent her from giving birth to the twin gods. Thus, when Apollo was born and was four days old he pursued Python, making his way straight for Mount Parnassus where the serpent dwelled and chased it to the oracle of Gaia at Delphi; there he dared to penetrate the sacred precinct and kill it with his arrows beside the rock cleft where the priestess sat on her tripod. Robert Graves, who habitually read into primitive myths a retelling of archaic political and social turmoil, saw in this the capture by Hellenes of a pre-Hellenic shrine. \"To placate local opinion at Delphi,\" he wrote in The Greek Myths, \"regular funeral games were instituted in honor of the dead hero Python, and her priestess was retained in office.\"\n\nAccording to an epigram from 159 BC, it seems that Python in particular meant to rape Leto. Clearchus of Soli wrote that while Python was pursuing them, Leto stepped on a stone and, holding Apollo in her hands, cried ἵε παῖ (híe paî, meaning \"shoot, child\") to him, who was holding a bow and arrows. \n\nThe politics are conjectural, but the myth reports that Zeus ordered Apollo to purify himself for the sacrilege and instituted the Pythian Games, over which Apollo was to preside, as penance for his act.\n\nErwin Rohde wrote that the Python was an earth spirit, who was conquered by Apollo, and buried under the omphalos and that it is a case of one god setting up his temple on the grave of another.\n\nThe priestess of the oracle at Delphi became known as the Pythia, after the place-name Pytho, which Greeks explained as named after the rotting (πύθειν) of the slain serpent's corpse in the strength of Hyperion (day) or Helios (the sun).\n\nKarl Kerenyi notes that in some early accounts Python is conflated with Typhon, the serpentine monster against whom Zeus fought. Other sources confuse him with the female dragon Delphyne; in these accounts, the dragon is said to be dissolved by the sun after its death.\n\nPython was the good daemon (ἀγαθὸς δαίμων) of the temple as it appears in Minoan religion, but she was represented as a dragon, as often happens in Northern European folklore as well as in the East.\n\nThis myth has been described as an allegory for the dispersal of the fogs and clouds of vapor that arise from ponds and marshes (Python) by the rays of the Sun (the arrows of Apollo).\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q28865",
  "label": "Python",
  "description": "general-purpose programming language",
  "aliases": [
   "Python programming language",
   "Python language",
   "Python (language)",
   "Python computer language",
   "Python Programming Language",
   "Python (scripting language)",
   "Python (lang)",
   "Python (programming)",
   "Python (computer language)",
   "Python (software)",
   "Python (Programming Language)",
   "Python (computing)",
   "Python.org"
  ],
  "claims": {
   "P31": [
    "Q899523",
    "Q1268980",
    "Q3839507",
    "Q187432",
    "Q12772052",
    "Q21562092",
    "Q1993334",
    "Q211496",
    "Q9143",
    "Q1004415",
    "Q50843083",
    "Q28923017",
    "Q1130645",
    "Q7397"
   ],
   "P527": [
    "Q13741"
   ],
   "P1889": [
    "Q599384",
    "Q271218"
   ]
  },
  "revision_id": "2566877611",
  "value_labels": {
   "Q899523": "object-based language",
   "Q1268980": "dynamic programming language",
   "Q3839507": "functional programming language",
   "Q187432": "scripting language",
   "Q12772052": "multi-paradigm programming language",
   "Q21562092": "imperative programming language",
   "Q1993334": "interpreted language",
   "Q211496": "high-level programming language",
   "Q9143": "programming language",
   "Q1004415": "run-time system",
   "Q50843083": "off-side rule language",
   "Q28923017": "strict programming language",
   "Q1130645": "open-source software",
   "Q7397": "software",
   "Q13741": "integrated development environment",
   "Q599384": "CPython",
   "Q271218": "Python"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q29467582",
  "label": "PYTHON",
  "description": "British contingency plan for continuity of government",
  "aliases": [],
  "claims": {},
  "revision_id": "1701024206",
  "value_labels": {},
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15721",
  "label": "Python",
  "description": "dragon of Delphi killed by the god Apollo",
  "aliases": [],
  "claims": {
   "P31": [
    "Q16326794",
    "Q22988604",
    "Q7559"
   ],
   "P1889": [
    "Q848562"
   ]
  },
  "revision_id": "2566011377",
  "value_labels": {
   "Q16326794": "mythological serpent",
   "Q22988604": "mythological Greek character",
   "Q7559": "dragon",
   "Q848562": "Pithon"
  },
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
  "ancestor_of": "Q28865",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1268980",
  "label": "dynamic programming language",
  "description": "programming language that supports manipulating program constructs at runtime",
  "aliases": [
   "dynamic language"
  ],
  "claims": {
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2450503730",
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
  "level": 1,
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q211496",
  "label": "high-level programming language",
  "description": "programming language with strong abstraction from details of hardware",
  "aliases": [
   "high-level language",
   "HLL"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2564820107",
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
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
  "ancestor_of": "Q28865",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16326794",
  "label": "mythological serpent",
  "description": "serpent that only appears in myths and legends",
  "aliases": [
   "legendary serpent",
   "mythical serpent",
   "mythical snake",
   "mythological snake",
   "legendary snake",
   "snakes in mythology",
   "snakes (mythology)",
   "snakes in culture"
  ],
  "claims": {
   "P31": [
    "Q20742825"
   ],
   "P279": [
    "Q24334299",
    "Q24895634"
   ],
   "P1889": [
    "Q27229996"
   ]
  },
  "revision_id": "2530418682",
  "ancestor_of": "Q15721",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q22988604",
  "label": "mythological Greek character",
  "description": "individual character in Greek mythology",
  "aliases": [
   "people of Greek mythology",
   "person in Greek mythology",
   "Greek mythological character",
   "Greek mythology character",
   "Greek mythical character",
   "Greek mythological figure",
   "Greek mythical figure",
   "mythical Greek figure",
   "mythical Greek character"
  ],
  "claims": {
   "P279": [
    "Q4271324"
   ],
   "P361": [
    "Q34726"
   ]
  },
  "revision_id": "2515057943",
  "ancestor_of": "Q15721",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7559",
  "label": "dragon",
  "description": "legendary winged, fire-breathing reptile",
  "aliases": [
   "drake"
  ],
  "claims": {
   "P31": [
    "Q24334299"
   ],
   "P279": [
    "Q2239243",
    "Q24334299"
   ],
   "P1889": [
    "Q30170627",
    "Q731434",
    "Q215605",
    "Q94279981",
    "Q126538177",
    "Q42861",
    "Q37493975",
    "Q117233696"
   ]
  },
  "revision_id": "2569686535",
  "ancestor_of": "Q15721",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20742825",
  "label": "cultural depiction",
  "description": "depiction of topic within culture",
  "aliases": [
   "in popular culture",
   "cultural portrayal",
   "popular cultural depiction",
   "cultural views",
   "cultural representation",
   "representation"
  ],
  "claims": {
   "P279": [
    "Q45025858",
    "Q1406161"
   ],
   "P361": [
    "Q11042"
   ]
  },
  "revision_id": "2511739714",
  "ancestor_of": "Q15721",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q24334299",
  "label": "mythical animal",
  "description": "creature in mythology and religion",
  "aliases": [
   "mythic animal",
   "mythic species of animal",
   "mythic taxon of animal",
   "mythical species of animal",
   "mythical taxon of animal",
   "mythological animal",
   "mythological species of animal",
   "mythological taxon of animal",
   "animal from mythology"
  ],
  "claims": {
   "P279": [
    "Q2239243",
    "Q4179933"
   ],
   "P1889": [
    "Q3542731"
   ]
  },
  "revision_id": "2527509993",
  "ancestor_of": "Q15721",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q24895634",
  "label": "human uses of reptiles",
  "description": "overview of humans' uses of reptiles",
  "aliases": [
   "reptiles in culture"
  ],
  "claims": {
   "P279": [
    "Q65090216"
   ],
   "P361": [
    "Q51873806"
   ]
  },
  "revision_id": "2561637907",
  "ancestor_of": "Q15721",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4271324",
  "label": "mythical character",
  "description": "character from mythology",
  "aliases": [
   "mythical figure",
   "mythological character",
   "mythological figure"
  ],
  "claims": {
   "P31": [
    "Q112265308"
   ],
   "P279": [
    "Q24334685",
    "Q115537581",
    "Q21070598",
    "Q95074"
   ],
   "P460": [
    "Q18563354"
   ],
   "P1889": [
    "Q13002315",
    "Q95074",
    "Q64520857",
    "Q115537581"
   ]
  },
  "revision_id": "2558343273",
  "ancestor_of": "Q15721",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2239243",
  "label": "mythical creature",
  "description": "supernatural animal, generally a hybrid, sometimes part human, whose existence cannot be proven, described in legends, myths, fables, folklore",
  "aliases": [
   "legendary creature",
   "mythological creature",
   "mythic creature",
   "fabulous beast",
   "fabulous creature",
   "fantastic animal",
   "fantastic beast",
   "mythical beast",
   "mythical animal"
  ],
  "claims": {
   "P279": [
    "Q24334685",
    "Q7239",
    "Q1274979"
   ],
   "P1889": [
    "Q2593744"
   ]
  },
  "revision_id": "2523693520",
  "ancestor_of": "Q15721",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-83541804-n",
  "lemmas": [
   "Python"
  ],
  "gloss": "a general-purpose, multi-paradigm programming language for computers created by Guido van Rossum",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06911128-n"
   ]
  },
  "relation_targets": {
   "oewn-06911128-n": "programming language, programing language"
  }
 },
 {
  "synset": "oewn-01746246-n",
  "lemmas": [
   "python"
  ],
  "gloss": "large Old World boas",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-01744584-n"
   ],
   "hyponym": [
    "oewn-01746577-n",
    "oewn-01746741-n",
    "oewn-01746911-n",
    "oewn-01747042-n",
    "oewn-01747196-n"
   ]
  },
  "relation_targets": {
   "oewn-01744584-n": "boa",
   "oewn-01746577-n": "carpet snake, Python variegatus, Morelia spilotes variegatus",
   "oewn-01746741-n": "reticulated python, Python reticulatus",
   "oewn-01746911-n": "Indian python, Python molurus",
   "oewn-01747042-n": "rock python, rock snake, Python sebae",
   "oewn-01747196-n": "amethystine python"
  }
 },
 {
  "synset": "oewn-10516512-n",
  "lemmas": [
   "python"
  ],
  "gloss": "a soothsaying spirit or a person who is possessed by such a spirit",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-09568453-n"
   ]
  },
  "relation_targets": {
   "oewn-09568453-n": "spirit, disembodied spirit"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 3: Docker (`g5lqkx80zn`)

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
[
 {
  "title": "Docker",
  "revision_id": "1378724389",
  "matched_by": "title",
  "text": "Look up Docker or docker in Wiktionary, the free dictionary.\n\nDocker most often refers to:\n\nA dockworker, a manual laborer who is involved in loading and unloading ships, also called a longshoreman or stevedore\n\nDocker (software), an open-source software project automating the deployment of applications inside software containers\n\nDocker, Inc., the company promoting Docker software\n\nDocker(s) may also refer to:\n\nPlaces\n\nDocker, Cumbria, a civil parish in England\n\nDocker, Lancashire, a hamlet in England\n\nDocker, Victoria, Australia\n\nDocker River or Kaltukatjara, a place in Northern Territory, Australia\n\nBrands and enterprises\n\nDockers (brand), a brand of men's clothing originally by Levi Strauss & Co.\n\nSports teams\n\nCincinnati Dockers, an American-based Australian rules football team\n\nDrogheda Dockers, a football team in the Australian Rules Football League of Ireland\n\nDuisburg Dockers, baseball and American football teams in Duisburg, Germany\n\nFremantle Football Club, nicknamed the Dockers, an Australian Football League team\n\nHamburg Dockers, a football team in the Australian Football League of Germany\n\nMillwall F.C., formerly nicknamed the Dockers\n\nOther uses\n\nDocker (surname), a surname (including a list of people with the name)\n\nDockers (film), a British television drama film\n\nRoller docker, a baking tool used to perforate dough\n\nSee also"
 },
 {
  "title": "Docker (software)",
  "revision_id": "1378632233",
  "matched_by": "title-minus-qualifier",
  "text": "Docker is a set of products that uses operating system-level virtualization to deliver software in packages called containers. Docker automates the deployment of applications within lightweight containers, enabling them to run consistently across different computing environments.\n\nThe core software that runs and manages these containers is called Docker Engine. Docker was first released in 2013 and continues to be developed by Docker, Inc. The platform includes both free and paid tiers.\n\nHistory\n\nSolomon Hykes started the Docker project in France as an internal project within dotCloud, a platform-as-a-service company.\n\ndotCloud Inc. was founded by Kamel Founadi, Hykes, and Sebastien Pahl during the Y Combinator Summer 2010 startup incubator group and launched in 2011, and renamed to Docker Inc in 2013.\n\nDocker debuted to the public in Santa Clara at PyCon in 2013. It was released as open-source in March 2013. At the time, it used LXC as its default execution environment. One year later, with the release of version 0.9, Docker replaced LXC with its own component, libcontainer, which was written in the Go programming language.\n\nIn 2017, Docker created the Moby project for open research and development. In March 2026, the Communications of the ACM featured Docker as the cover article in a retrospective article of the past decade.\n\nAdoption\n\nSeptember 19, 2013: Red Hat and Docker announced a collaboration around Fedora, Red Hat Enterprise Linux (RHEL), and OpenShift.\n\nOctober 15, 2014: Microsoft announced the integration of the Docker engine into Windows Server, as well as native support for the Docker client role in Windows.\n\nNovember 2014: Docker container services were announced for the Amazon Elastic Compute Cloud (EC2).\n\nNovember 10, 2014: Docker announced a partnership with Stratoscale.\n\nDecember 4, 2014: IBM announced a strategic partnership with Docker that enables Docker to integrate more closely with the IBM Cloud.\n\nJune 22, 2015: Docker and several other companies announced that they were working on a new vendor and operating-system-independent standard for software containers.\n\nDecember 2015: Oracle Cloud added Docker container support after acquiring StackEngine, a Docker container startup.\n\nMarch 2016: Docker for Mac and Windows betas released.\n\nApril 2016: Windocks, an independent software vendor released a port of Docker's open source project to Windows, supporting Windows Server 2012 R2 and Server 2016, with all editions of SQL Server 2008 onward.\n\nMay 2016: analysis showed the following organizations as main contributors to Docker: The Docker team, Cisco, Google, Huawei, IBM, Microsoft, and Red Hat.\n\nJune 8, 2016: Microsoft announced that Docker could now be used natively on Windows 10.\n\nJanuary 2017: An analysis of LinkedIn profile mentions showed Docker presence grew by 160% in 2016.\n\nMay 6, 2019: Microsoft announced the second version of Windows Subsystem for Linux (WSL). Docker, Inc. announced that it had started working on a version of Docker for Windows to run on WSL 2. In particular, this meant Docker could run on Windows 10 Home (previously it was limited to Windows Pro and Enterprise since it used Hyper-V).\n\nAugust 2020: Microsoft announced a backport of WSL2 to Windows 10 versions 1903 and 1909 (previously WSL2 was available only on version 2004) and Docker developers announced availability of Docker for these platforms.\n\nAugust 2021: Docker Desktop for Windows and MacOS was no longer available free of charge for enterprise users. Docker ended free Docker Desktop use for larger business customers and replaced its Free Plan with a Personal Plan. Docker Engine on Linux distributions remained unaffected.\n\nDecember 2023: Docker acquired AtomicJar to expand its testing capabilities.\n\nIn February 2025, Docker Engine 28 was released with security hardening for container networking. The release changed the default bridge networking behavior to prevent unpublished container ports from being unintentionally accessible from local networks under certain host firewall configurations.\n\nIn April 2025, Docker Desktop 4.41 expanded Docker Model Runner with support for Windows, Docker Compose, and Testcontainers, including NVIDIA GPU acceleration on Windows.\n\nIn August 2025, Docker changed the Docker Desktop release cadence from monthly releases to releases every two weeks, beginning with version 4.45.0. The change was intended to deliver new features, bug fixes, and security updates more frequently.\n\nIn November 2025, Docker Engine 29.0.0 was released. The release made the containerd image store the default for fresh installations and deprecated the github.com/docker/docker Go module in favor of github.com/moby/moby/client and github.com/moby/moby/api.\n\nMarch 2026: VisualDock Server, a server-side environment for running and managing Docker containers on Windows Server, was released.\n\nDesign\n\nContainers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. Because all of the containers share the services of a single operating system kernel, they use fewer resources than virtual machines.\n\nDocker can package an application and its dependencies in a virtual container that can, in principle, run on any Linux, Windows, or macOS computer. This enables the application to run in a variety of locations, such as on-premises, in public (see decentralized computing, distributed computing, and cloud computing) or private cloud. When running on Linux, Docker uses the resource isolation features of the Linux kernel (such as cgroups and kernel namespaces) and a union-capable file system (such as OverlayFS) to allow containers to run within a single Linux instance, avoiding the overhead of starting and maintaining virtual machines. Docker on macOS uses a Linux virtual machine to run the containers.\n\nBecause Docker containers are lightweight, a single server or virtual machine can run several containers simultaneously. A 2018 analysis found that a typical Docker use case involves running eight containers per host, and that a quarter of analyzed organizations run 18 or more per host. It can also be installed on a single board computer like the Raspberry Pi.\n\nThe Linux kernel's support for namespaces mostly isolates an application's view of the operating environment, including process trees, network, user IDs and mounted file systems, while the kernel's cgroups provide resource limiting for memory and CPU. Since version 0.9, Docker includes its own component (called libcontainer) to use virtualization facilities provided directly by the Linux kernel, in addition to using abstracted virtualization interfaces via libvirt, LXC and systemd-nspawn.\n\nDocker implements a high-level API to provide lightweight containers that run processes in isolation.\n\nComponents\n\nThe Docker software as a service offering consists of three components:\n\nSoftware\n\nThe Docker daemon, called dockerd, is a persistent process that manages Docker containers and handles container objects. The daemon listens for requests that are sent via the Docker Engine API. The Docker client program, called docker, provides a command-line interface (CLI) that allows users to interact with Docker daemons.\nObjects\n\nDocker objects are various entities used to assemble an application in Docker. The main classes of Docker objects are images, containers, and services.\n\nA Docker container is a standardized, encapsulated environment that runs applications. A container is managed using the Docker API or CLI.\n\nA Docker image is a read-only template used to build containers. Images are used to store and ship applications.\n\nA Docker service allows containers to be scaled across multiple Docker daemons. The result is known as a swarm, a set of cooperating daemons that communicate through the Docker API.\nRegistries\n\nA Docker registry is a repository for Docker images. Docker clients connect to registries to download (\"pull\") images for use or upload (\"push\") images that they have built. Registries can be public or private. The main public registry is Docker Hub. Docker Hub is the default registry where Docker looks for images. Docker registries also allow the creation of notifications based on events.\n\nA Dockerfile is a text file that commonly specifies several aspects of a Docker image: the Linux distribution, installation commands for the programming language runtime environment and application source code.\n\nAn example of a Dockerfile:ARG CODE_VERSION=latest\nFROM ubuntu:${CODE_VERSION}\nCOPY ./examplefile.txt /examplefile.txt\nENV MY_ENV_VARIABLE=\"example_value\"\nRUN apt-get update\n\n# Mount a directory from the Docker volume\n# Note: This is usually specified in the 'docker run' command.\nVOLUME [\"/myvolume\"]\n\n# Expose a port (22 for SSH)\nEXPOSE 22\n\nDocker Compose is a tool for defining and running multi-container Docker applications. It uses YAML files to configure the application's services and performs the creation and start-up process of all the containers with a single command. The docker compose CLI utility allows users to run commands on multiple containers at once; for example, building images, scaling containers, running containers that were stopped, and more. Commands related to image manipulation, or user-interactive options, are not relevant in Docker Compose because they address one container. The docker-compose.yml file is used to define an application's services and includes various configuration options. For example, the build option defines configuration options such as the Dockerfile path, the command option allows one to override default Docker commands, and more. The first public beta version of Docker Compose (version 0.0.1) was released on December 21, 2013. The first production-ready version (1.0) was made available on October 16, 2014.\n\nDocker Swarm provides native clustering functionality for Docker containers, which turns a group of Docker engines into a single virtual Docker engine. In Docker 1.12 and higher, Swarm mode is integrated with Docker Engine. The docker swarm CLI utility allows users to run Swarm containers, create discovery tokens, list nodes in the cluster, and more. The docker node CLI utility allows users to run various commands to manage nodes in a swarm, for example, listing the nodes in a swarm, updating nodes, and removing nodes from the swarm. Docker manages swarms using the Raft consensus algorithm. According to Raft, for an update to be performed, the majority of Swarm nodes need to agree on the update. In addition to the docker swarm CLI, docker stack is a tool designed to manage Swarm services with greater flexibility. It can use a configuration file very similar to a docker-compose.yml, with a few nuances. Using docker stack instead of docker compose offers several advantages, such as the ability to manage a Swarm cluster across multiple machines or the capability to work with docker secret combined with docker context, a feature that allows executing Docker commands on a remote host, enabling remote container management.\n\nDocker Volume facilitates the independent persistence of data, allowing data to remain even after the container is deleted or re-created.\n\nLicensing model\n\nThe Docker Engine is licensed under the Apache License 2.0. Docker Desktop distributes some components that are licensed under the GNU General Public License. Docker Desktop is not free for large enterprises.\n\nThe Dockerfile files can be licensed under an open-source license. The scope of such a license statement is only the Dockerfile and not the container image.\n\nSee also"
 },
 {
  "title": "Docker (surname)",
  "revision_id": "1376990434",
  "matched_by": "title-minus-qualifier",
  "text": "Docker is a locational surname from Docker, Westmoreland, and Docker, Lancashire.\n\nPeople with the surname \"Docker\":-\n\nAdam Docker (born 1985), English-Pakistani association footballer\n\nAdam Docker (born 1991), Australian rugby league player\n\nArthur Docker (1848–1929), Australian cricketer\n\nSir Bernard Docker (1896–1978), English industrialist\n\nLady Docker (1906–1983), English socialite and wife of Sir Bernard\n\nColin Docker (1925–2014), Anglican bishop\n\nDudley Docker (1862–1944), English businessman and cricketer\n\nErnest Brougham Docker (1842–1923), Australian judge\n\nIan Docker (born 1969), English association football player\n\nJoseph Docker (1802–1884), Australian politician\n\nKirk Docker, co-creator of Australian TV series You Can't Ask That\n\nLudford Docker (1860–1940), English businessman and cricketer\n\nMitchell Docker (born 1986), Australian cyclist\n\nRalph Docker (1855–1910), English cricketer\n\nRobert Docker (1918–1992), English composer and arranger\n\nRussell Docker (born 1967), British Paralympic skier\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q910577",
  "label": "Docker",
  "description": "Wikimedia disambiguation page",
  "aliases": [],
  "claims": {
   "P31": [
    "Q4167410"
   ],
   "P1889": [
    "Q16869593"
   ]
  },
  "revision_id": "2538917746",
  "value_labels": {
   "Q4167410": "Wikimedia disambiguation page",
   "Q16869593": "Docker"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15206305",
  "label": "Docker",
  "description": "open-source software for deploying and running of containerized applications",
  "aliases": [
   "Docker software"
  ],
  "claims": {
   "P31": [
    "Q506883",
    "Q7935198",
    "Q167772"
   ],
   "P1889": [
    "Q1537445",
    "Q113469872"
   ]
  },
  "revision_id": "2570343972",
  "value_labels": {
   "Q506883": "free and open-source software",
   "Q7935198": "container runtime",
   "Q167772": "digital container format",
   "Q1537445": "stevedore",
   "Q113469872": "Docker"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16869593",
  "label": "Docker",
  "description": "family name",
  "aliases": [
   "Docker (family name)",
   "Docker (surname)"
  ],
  "claims": {
   "P31": [
    "Q101352"
   ],
   "P1889": [
    "Q910577"
   ]
  },
  "revision_id": "2299223414",
  "value_labels": {
   "Q101352": "family name",
   "Q910577": "Docker"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4167410",
  "label": "Wikimedia disambiguation page",
  "description": "type of wiki page usually in main namespace (article namespace, ns=0) containing links to articles with similar names, and very little details only, use with P31 \"instance of\"",
  "aliases": [
   "disambiguation",
   "disambiguation page",
   "Wiki disambiguation page",
   "dabpage"
  ],
  "claims": {
   "P279": [
    "Q15633587",
    "Q17442446",
    "Q138717185"
   ],
   "P361": [
    "Q52",
    "Q373",
    "Q263",
    "Q369",
    "Q367",
    "Q370",
    "Q1063116",
    "Q15633578"
   ],
   "P460": [
    "Q15623926"
   ],
   "P1889": [
    "Q21484471",
    "Q80096233",
    "Q134972145",
    "Q138717185",
    "Q118521146"
   ]
  },
  "revision_id": "2568773925",
  "ancestor_of": "Q910577",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15633587",
  "label": "MediaWiki main namespace page",
  "description": "page in the main namespace of a wiki, used for \"main\" content specific to the project such as article, lemma, ...",
  "aliases": [
   "(main)"
  ],
  "claims": {
   "P279": [
    "Q15474042"
   ],
   "P361": [
    "Q118552465"
   ],
   "P1889": [
    "Q118552465"
   ]
  },
  "revision_id": "2503396531",
  "ancestor_of": "Q910577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17442446",
  "label": "Wikimedia internal item",
  "description": "instances and/or subclasses of this item are about some Wikimedia-only content and should not refer to real world entities",
  "aliases": [
   "internal item"
  ],
  "claims": {
   "P279": [
    "Q17379835"
   ]
  },
  "revision_id": "2556281869",
  "ancestor_of": "Q910577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q138717185",
  "label": "disambiguation page",
  "description": "type of page common in wikis",
  "aliases": [],
  "claims": {
   "P279": [
    "Q111279923"
   ],
   "P1889": [
    "Q4167410",
    "Q118521146",
    "Q22981376"
   ]
  },
  "revision_id": "2569961906",
  "ancestor_of": "Q910577",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q506883",
  "label": "free and open-source software",
  "description": "software that is both free (as in freedom) and open-source",
  "aliases": [
   "FOSS",
   "free/libre open-source software",
   "FLOSS"
  ],
  "claims": {
   "P279": [
    "Q1130645"
   ],
   "P460": [
    "Q341"
   ],
   "P1889": [
    "Q1130645",
    "Q56273712",
    "Q136757662"
   ]
  },
  "revision_id": "2559215174",
  "ancestor_of": "Q15206305",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7935198",
  "label": "container runtime",
  "description": "software for managing containers",
  "aliases": [
   "container management tool",
   "container orchestration engine"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q312466",
    "Q2622299"
   ],
   "P1889": [
    "Q122307299"
   ]
  },
  "revision_id": "2475171726",
  "ancestor_of": "Q15206305",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q167772",
  "label": "digital container format",
  "description": "metafile format",
  "aliases": [
   "container format",
   "multimedia container format",
   "wrapper",
   "metafile"
  ],
  "claims": {
   "P279": [
    "Q235557"
   ]
  },
  "revision_id": "2570734939",
  "ancestor_of": "Q15206305",
  "level": 1,
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
  "ancestor_of": "Q15206305",
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
  "ancestor_of": "Q15206305",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q312466",
  "label": "utility software",
  "description": "system software designed to help analyze, configure, optimize or maintain a computer",
  "aliases": [
   "software utility",
   "utility"
  ],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q676202",
    "Q40056"
   ],
   "P460": [
    "Q131742246"
   ]
  },
  "revision_id": "2527989218",
  "ancestor_of": "Q15206305",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2622299",
  "label": "software engine",
  "description": "central part of a computer program",
  "aliases": [
   "engine"
  ],
  "claims": {
   "P31": [
    "Q1310239",
    "Q151885"
   ],
   "P279": [
    "Q271680"
   ],
   "P1889": [
    "Q44167"
   ]
  },
  "revision_id": "2564108382",
  "ancestor_of": "Q15206305",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q235557",
  "label": "file format",
  "description": "formalized structure of information stored in a storage medium",
  "aliases": [
   "file type",
   "file formats"
  ],
  "claims": {
   "P31": [
    "Q186157"
   ],
   "P279": [
    "Q494823",
    "Q20819677",
    "Q317623"
   ],
   "P361": [
    "Q26085352"
   ],
   "P1889": [
    "Q174989",
    "Q88864296",
    "Q494823",
    "Q186157"
   ]
  },
  "revision_id": "2566776472",
  "ancestor_of": "Q15206305",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q101352",
  "label": "family name",
  "description": "part of a naming scheme for individuals, used in many cultures worldwide",
  "aliases": [
   "last name",
   "fam name",
   "family surname",
   "surname",
   "clan name"
  ],
  "claims": {
   "P31": [
    "Q121493639"
   ],
   "P279": [
    "Q4116295",
    "Q10856962"
   ],
   "P361": [
    "Q1071027"
   ],
   "P460": [
    "Q4116295",
    "Q61942409"
   ],
   "P1889": [
    "Q8436",
    "Q777342",
    "Q279239",
    "Q211503",
    "Q55408004",
    "Q61942409"
   ]
  },
  "revision_id": "2572971854",
  "ancestor_of": "Q16869593",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q121493639",
  "label": "name particle",
  "description": "part of a name",
  "aliases": [
   "name component",
   "component of a name",
   "name element"
  ],
  "claims": {
   "P279": [
    "Q10856962",
    "Q13196193",
    "Q184943"
   ],
   "P361": [
    "Q115642094"
   ]
  },
  "revision_id": "2571890163",
  "ancestor_of": "Q16869593",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4116295",
  "label": "surname",
  "description": "human name used in combination with given name(s) used to indicate association, often a family name or a name indicating place of origin",
  "aliases": [
   "after-name",
   "last name"
  ],
  "claims": {
   "P31": [
    "Q121493639"
   ],
   "P279": [
    "Q10856962"
   ],
   "P361": [
    "Q1071027"
   ],
   "P460": [
    "Q101352",
    "Q53857984",
    "Q117209596"
   ],
   "P1889": [
    "Q61942409",
    "Q279239"
   ]
  },
  "revision_id": "2572014198",
  "ancestor_of": "Q16869593",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q10856962",
  "label": "anthroponym",
  "description": "name of a person, such as given name (first name) or surname",
  "aliases": [
   "human name",
   "person's name"
  ],
  "claims": {
   "P31": [
    "Q134599141"
   ],
   "P279": [
    "Q60596080"
   ],
   "P1889": [
    "Q1137656"
   ]
  },
  "revision_id": "2555383414",
  "ancestor_of": "Q16869593",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-10674608-n",
  "lemmas": [
   "stevedore",
   "loader",
   "docker",
   "dockhand",
   "dock worker",
   "dockworker",
   "dock-walloper",
   "lumper"
  ],
  "gloss": "a laborer who loads and unloads vessels in a port",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-10260997-n"
   ],
   "hyponym": [
    "oewn-80614089-n",
    "oewn-85123702-n"
   ]
  },
  "relation_targets": {
   "oewn-10260997-n": "laborer, manual laborer, labourer",
   "oewn-80614089-n": "longshoreman",
   "oewn-85123702-n": "longshorewoman"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~
