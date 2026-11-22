# Skills Lexicon pilot, grounded run: message 9 of 13 (chunk 08, 3 concepts)

Everything you need is in this message. Don't fetch, search or look anything up. Draft only from what is here and what you already know.

**Independence.** Several models are drafting these same 36 entries separately so Nik Bear Brown can compare them. Don't read, search for or ask for any other model's drafts, including Claude's. The material below is source material only (the lexicon's record, candidate neighbors, posting snippets, Wikipedia, Wikidata and WordNet candidates); it holds no one's drafts.

**How to work.** Treat each concept on its own, as if you had never seen the others: don't carry a decision, a wording or a relation from one concept to the next. This is the **grounded** run: each concept comes with its candidate Wikipedia articles, Wikidata items and WordNet senses.

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "08", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-08.jsonl`. Otherwise send one code block marked `jsonl` holding the 3 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 3: Application programming interface (`xe2d2jfa1r`)

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
[
 {
  "title": "API",
  "revision_id": "1374263741",
  "matched_by": "title",
  "text": "An application programming interface (API) is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software. A document or standard that describes how to build such a connection or interface is called an API specification. A computer system that meets this standard is said to implement or expose an API. The term API may refer either to the specification or to the implementation.\n\nIn contrast to a user interface, which connects a computer to a person, an application programming interface connects computers or pieces of software to each other. It is not intended to be used directly by a person (the end user) other than a computer programmer who is incorporating it into software. An API is often made up of different parts which act as tools or services that are available to the programmer. A program or a programmer that uses one of these parts is said to call that portion of the API. The calls that make up the API are also known as subroutines, methods, requests, or endpoints. An API specification defines these calls, meaning that it explains how to use or implement them.\n\nOne of the main purpose of APIs is to hide the internal details of how a system works, exposing only those parts a programmer will find useful and keeping them consistent even if the internal details later change. An API may be custom-built for a particular pair of systems, or it may be a shared standard allowing interoperability among many systems.\n\nThe term API is often used to refer to web APIs, which allow communication between computers that are joined by the internet. There are also APIs for programming languages, software libraries, computer operating systems, and computer hardware. APIs originated in the 1940s, though the term did not emerge until the 1960s and 70s.\n\nPurpose\n\nAn API opens a software system to interactions from the outside. It allows two software systems to communicate across a boundary — an interface — using mutually agreed-upon signals. In other words, an API connects software entities together. Unlike a user interface, an API is typically not visible to users. It is an \"under the hood\" portion of a software system, used for machine-to-machine communication.\n\nA well-designed API exposes only objects or actions needed by software or software developers. It hides details that have no use. This abstraction simplifies programming.\n\nBuilding software using APIs has been compared to using building-block toys, such as Lego bricks. Software services or software libraries are analogous to the bricks; they may be joined together via their APIs, composing a new software product. The process of joining is called integration.\n\nAs an example, consider a weather sensor that offers an API. When a certain message is transmitted to the sensor, it will detect the current weather conditions and reply with a weather report. The message that activates the sensor is an API call, and the weather report is an API response. A weather forecasting app might integrate with a number of weather sensor APIs, gathering weather data from throughout a geographical area.\n\nAn API is often compared to a contract. It represents an agreement between parties: a service provider who offers the API and the software developers who rely upon it. If the API remains stable, or if it changes only in predictable ways, developers' confidence in the API will increase. This may increase their use of the API.\n\nHistory of the term\n\nThe term API initially described an interface only for end-user-facing programs, known as application programs. This origin is still reflected in the name \"application programming interface.\" Today, the term is broader, including also utility software and even hardware interfaces.\n\nThe idea of the API is much older than the term itself. British computer scientists Maurice Wilkes and David Wheeler worked on a modular software library in the 1940s for EDSAC, an early computer. The subroutines in this library were stored on punched paper tape organized in a filing cabinet. This cabinet also contained what Wilkes and Wheeler called a \"library catalog\" of notes about each subroutine and how to incorporate it into a program. Today, such a catalog would be called an API (or an API specification or API documentation) because it instructs a programmer on how to use each subroutine that the programmer needs.\n\nWilkes and Wheeler's book The Preparation of Programs for an Electronic Digital Computer contains the first published API specification. Joshua Bloch considers that Wilkes and Wheeler \"latently invented\" the API, because it is more of a concept that is discovered than invented.\n\nThe term \"application program interface\" (without an -ing suffix) is first recorded in a paper called Data structures and techniques for remote computer graphics presented at an AFIPS conference in 1968. The authors of this paper use the term to describe the interaction of an application—a graphics program in this case—with the rest of the computer system. A consistent application interface (consisting of Fortran subroutine calls) was intended to free the programmer from dealing with idiosyncrasies of the graphics display device, and to provide hardware independence if the computer or the display were replaced.\n\nThe term was introduced to the field of databases by C. J. Date in a 1974 paper called The Relational and Network Approaches: Comparison of the Application Programming Interface. An API became a part of the ANSI/SPARC framework for database management systems. This framework treated the application programming interface separately from other interfaces, such as the query interface. Database professionals in the 1970s observed these different interfaces could be combined; a sufficiently rich application interface could support the other interfaces as well.\n\nThis observation led to APIs that supported all types of programming, not just application programming. By 1990, the API was defined simply as \"a set of services available to a programmer for performing certain tasks\" by technologist Carl Malamud.\n\nThe idea of the API was expanded again with the dawn of remote procedure calls and web APIs. As computer networks became common in the 1970s and 80s, programmers wanted to call libraries located not only on their local computers, but on computers located elsewhere. These remote procedure calls were well supported by the Java language in particular. In the 1990s, with the spread of the internet, standards like CORBA, COM, and DCOM competed to become the most common way to expose API services.\n\nRoy Fielding's dissertation Architectural Styles and the Design of Network-based Software Architectures at UC Irvine in 2000 outlined Representational state transfer (REST) and described the idea of a \"network-based Application Programming Interface\" that Fielding contrasted with traditional \"library-based\" APIs. XML and JSON web APIs saw widespread commercial adoption beginning in 2000 and continuing as of 2021. The web API is now the most common meaning of the term API.\n\nThe Semantic Web proposed by Tim Berners-Lee in 2001 included \"semantic APIs\" that recast the API as an open, distributed data interface rather than a software behavior interface. Proprietary interfaces and agents became more widespread than open ones, but the idea of the API as a data interface took hold. Because web APIs are widely used to exchange data of all kinds online, API has become a broad term describing much of the communication on the internet. When used in this way, the term API has overlap in meaning with the term communication protocol.\n\nTypes\n\nLibraries and frameworks\n\nThe interface to a software library is one type of API. The API describes and prescribes the \"expected behavior\" (a specification) while the library is an \"actual implementation\" of this set of rules.\n\nA single API can have multiple implementations (or none, being abstract) in the form of different libraries that share the same programming interface.\n\nThe separation of the API from its implementation can allow programs written in one language to use a library written in another. For example, because Scala and Java compile to compatible bytecode, Scala developers can take advantage of any Java API.\n\nAPI use can vary depending on the type of programming language involved.\nAn API for a procedural language such as Lua could consist primarily of basic routines to execute code, manipulate data or handle errors while an API for an object-oriented language, such as Java, would provide a specification of classes and its class methods. Hyrum's law states that \"With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.\" Meanwhile, several studies show that most applications that use an API tend to use a small part of the API.\n\nLanguage bindings are also APIs. By mapping the features and capabilities of one language to an interface implemented in another language, a language binding allows a library or service written in one language to be used when developing in another language. Tools such as SWIG and F2PY, a Fortran-to-Python interface generator, facilitate the creation of such interfaces.\n\nAn API can also be related to a software framework: a framework can be based on several libraries implementing several APIs, but unlike the normal use of an API, the access to the behavior built into the framework is mediated by extending its content with new classes plugged into the framework itself.\n\nMoreover, the overall program flow of control can be out of the control of the caller and in the framework's hands by inversion of control or a similar mechanism.\n\nOperating systems\n\nAn API can specify the interface between an application and the operating system. POSIX, for example, specifies a set of common APIs that aim to enable an application written for a POSIX conformant operating system to be compiled for another POSIX conformant operating system.\n\nLinux and Berkeley Software Distribution are examples of operating systems that implement the POSIX APIs.\n\nMicrosoft has shown a strong commitment to a backward-compatible API, particularly within its Windows API (Win32) library, so older applications may run on newer versions of Windows using an executable-specific setting called \"Compatibility Mode\". How much Microsoft developers' access to the company's operating systems' internal APIs is an advantage is unclear. Richard A. Shaffer of Technologic Computer Letter in 1987 compared the situation to a baseball game in which \"Microsoft owns all the bats and the field\", and large vendors like Lotus Development and Ashton-Tate reportedly received information about MS-DOS 5.0 that smaller software developers did not. Ed Esber of Ashton-Tate said in a 1987 interview, however, that Bill Gates told him that his developers sometimes had to rewrite software based on early APIs. Gates noted in the interview that Microsoft's Apple Macintosh applications were more successful than those for MS-DOS, because his company did not have to also devote resources to Mac OS.\n\nAn API differs from an application binary interface (ABI) in that an API is source code based while an ABI is binary based. For instance, POSIX provides APIs while the Linux Standard Base provides an ABI.\n\nRemote APIs\n\nRemote APIs allow developers to manipulate remote resources through protocols, specific standards for communication that allow different technologies to work together, regardless of language or platform.\nFor example, the Java Database Connectivity API allows developers to query many different types of databases with the same set of functions, while the Java remote method invocation API uses the Java Remote Method Protocol to allow invocation of functions that operate remotely, but appear local to the developer.\n\nTherefore, remote APIs are useful in maintaining the object abstraction in object-oriented programming; a method call, executed locally on a proxy object, invokes the corresponding method on the remote object, using the remoting protocol, and acquires the result to be used locally as a return value.\n\nA modification of the proxy object will also result in a corresponding modification of the remote object.\n\nWeb APIs\n\nWhen used in the context of web development, an API is typically defined as a set of specifications, such as Hypertext Transfer Protocol (HTTP) request messages, along with a definition of the structure of response messages, usually in an Extensible Markup Language (XML) or JavaScript Object Notation (JSON) format. An example might be a shipping company API that can be added to an eCommerce-focused website to facilitate ordering shipping services and automatically include current shipping rates, without the site developer having to enter the shipper's rate table into a web database. While \"web API\" historically has been virtually synonymous with web service, the recent trend (so-called Web 2.0) has been moving away from Simple Object Access Protocol (SOAP) based web services and service-oriented architecture (SOA) towards more direct representational state transfer (REST) style web resources and resource-oriented architecture (ROA). Part of this trend is related to the Semantic Web movement toward Resource Description Framework (RDF), a concept to promote web-based ontology engineering technologies. Web APIs allow the combination of multiple APIs into new applications known as mashups.\nIn the social media space, web APIs have allowed web communities to facilitate sharing content and data between communities and applications. In this way, content that is created in one place can be dynamically posted and updated to multiple locations on the web. For example, Twitter's REST API allows developers to access core Twitter data and the Search API provides methods for developers to interact with Twitter Search and trends data.\n\nDesign\n\nThe design of an API has significant impact on its usage. The principle of information hiding describes the role of programming interfaces as enabling modular programming by hiding the implementation details of the modules so that users of modules need not understand the complexities inside the modules. Thus, the design of an API attempts to provide only the tools a user would expect. The design of programming interfaces represents an important part of software architecture, the organization of a complex piece of software.\n\nRelease policies\n\nAPIs are one of the more common ways technology companies integrate. Those that provide and use APIs are considered as being members of a business ecosystem.\n\nThe main policies for releasing an API are:\n\nPrivate: The API is for internal company use only.\n\nPartner: Only specific business partners can use the API. For example, vehicle for hire companies such as Uber and Lyft allow approved third-party developers to directly order rides from within their apps. This allows the companies to exercise quality control by curating which apps have access to the API, and provides them with an additional revenue stream.\n\nPublic: The API is available for use by the public. For example, Microsoft makes the Windows API public, and Apple releases its API Cocoa, so that software can be written for their platforms. Not all public APIs are generally accessible by everybody. For example, Internet service providers like Cloudflare or Voxility, use RESTful APIs to allow customers and resellers access to their infrastructure information, DDoS stats, network performance or dashboard controls. Access to such APIs is granted either by \"API tokens\", or customer status validations.\n\nPublic API implications\n\nAn important factor when an API becomes public is its \"interface stability\". Changes to the API—for example adding new parameters to a function call—could break compatibility with the clients that depend on that API.\n\nWhen parts of a publicly presented API are subject to change and thus not stable, such parts of a particular API should be documented explicitly as \"unstable\". For example, in the Google Guava library, the parts that are considered unstable, and that might change soon, are marked with the Java annotation @Beta.\n\nA public API can sometimes declare parts of itself as deprecated or rescinded. This usually means that part of the API should be considered a candidate for being removed, or modified in a backward incompatible way. Therefore, these changes allow developers to transition away from parts of the API that will be removed or not supported in the future.\n\nClient code may contain innovative or opportunistic usages that were not intended by the API designers. In other words, for a library with a significant user base, when an element becomes part of the public API, it may be used in diverse ways.\nOn February 19, 2020, Akamai published their annual \"State of the Internet\" report, showcasing the growing trend of cybercriminals targeting public API platforms at financial services worldwide. From December 2017 through November 2019, Akamai witnessed 85.42 billion credential violation attacks. About 20%, or 16.55 billion, were against hostnames defined as API endpoints. Of these, 473.5 million have targeted financial services sector organizations.\n\nAPI documentation\n\nAPI documentation describes what services an API offers and how to use those services, aiming to cover everything a client would need to know for practical purposes.\n\nDocumentation is crucial for the development and maintenance of applications using the API.\nAPI documentation is traditionally found in documentation files but can also be found in social media such as blogs, forums, and Q&A websites.\n\nTraditional documentation files are often presented via a documentation system, such as Javadoc or Pydoc, that has a consistent appearance and structure. However, the types of content included in the documentation differs from API to API.\n\nIn the interest of clarity, API documentation may include a description of classes and methods in the API as well as typical usage scenarios, code snippets, design rationales, performance discussions, and contracts, but implementation details of the API services themselves are usually omitted. It can take a number of forms, including instructional documents, tutorials, and reference works. It'll also include a variety of information types, including guides and functionalities.\n\nRestrictions and limitations on how the API can be used are also covered by the documentation. For instance, documentation for an API function could note that its parameters cannot be null, that the function itself is not thread safe. Because API documentation tends to be comprehensive, it is a challenge for writers to keep the documentation updated and for users to read it carefully, potentially yielding bugs.\n\nAPI documentation can be enriched with metadata information like Java annotations. This metadata can be used by the compiler, tools, and by the run-time environment to implement custom behaviors or custom handling.\n\nIt is possible to generate API documentation in a data-driven manner. By observing many programs that use a given API, it is possible to infer the typical usages, as well the required contracts and directives. Then, templates can be used to generate natural language from the mined data.\n\nDispute over copyright"
 },
 {
  "title": "Apis (deity)",
  "revision_id": "1377560696",
  "matched_by": "title-minus-qualifier",
  "text": "In ancient Egyptian religion, Apis or Hapis, alternatively spelled Hapi-ankh, was a sacred bull or multiple sacred bulls worshiped in the Memphis region, identified as the son of Hathor, a primary deity in the pantheon of ancient Egypt. Initially, he was assigned a significant role in her worship, being sacrificed and reborn. Later, Apis also served as an intermediary between humans and other powerful deities (originally Ptah, later Osiris, then Atum).\n\nThe Apis bull was an important sacred animal to the ancient Egyptians. As with the other sacred beasts, Apis' importance increased over the centuries. During colonization of the conquered Egypt, Greek and Roman authors had much to say about Apis, the markings by which the black calf was recognized, the manner of his conception by a ray from heaven, his house at Memphis (with a court for his deportment), the mode of prognostication from his actions, his death, the mourning at his death, his costly burial, and the rejoicings throughout the country when a new Apis was found. Auguste Mariette's excavation of the Serapeum of Saqqara revealed the tombs of more than sixty animals, ranging from the time of Amenhotep III to the end of the Ptolemaic dynasty. Originally, each animal was buried in a separate tomb with a chapel built above it. From Ramesses II onward, bulls were interred in interconnected underground galleries.\n\nHistory of worship\n\nWorship of an Apis bull, experienced by ancient Egyptians as holy, has been known since the First Dynasty in Memphis, while worship of the Apis as a proper god, at least according to Manetho's Aegyptiaca, seems to be a later adoption, purportedly started during the reign of king Kaiechos (possibly Nebra) of the Second Dynasty.\n\nApis is named on very early monuments, but little is known of the divine animal before the New Kingdom. Ceremonial burials of bulls indicate that ritual sacrifice was part of the worship of the early cow deities, Hathor and Bat, and a bull might represent her offspring, a king who became a deity after death. He was entitled \"the renewal of the life\" of the Memphite deity Ptah: but after death, he became Osorapis, i.e. the Osiris Apis, just as dead humans were assimilated to Osiris, the ruler of the underworld. This Osorapis was identified with Serapis of the late Hellenistic period and may well be identical with him. Creating parallels to their own religious beliefs, ancient Greek writers identified Apis as an incarnation of Osiris, ignoring the connection with Ptah.\n\nApis was the most popular of three great bull cults of ancient Egypt, the others being the cults of Mnevis and Buchis. All are related to the worship of Hathor or Bat, similar primary goddesses separated by region until unification that eventually merged as Hathor. The worship of Apis was continued by the Greeks and after them by the Romans, and lasted until almost 400 CE.\n\nHerald of Ptah\n\nThis animal was chosen because it symbolized the courageous heart, great strength, and fighting spirit of the king. Apis came to be considered a manifestation of the king, as bulls were symbols of strength and fertility, qualities that are closely linked with kingship. \"Strong bull of his mother Hathor\" was a common title for Egyptian gods and male kings, being unused for women serving as king, such as Hatshepsut.\n\nAs early as the time of the Narmer Palette, the king is depicted with a bovine tail on one side, and a bull is seen knocking down the walls of a city on the other.\n\nOccasionally, Apis was pictured with the sun-disk symbol of his mother, Hathor, between his horns, being one of few deities ever associated with her symbol. When the disk was depicted on his head with his horns below and the triangular marking on his forehead, an ankh was suggested. That symbol always was closely associated with Hathor.\n\nEarly on, Apis was the herald (wḥm) of Ptah, the chief deity in the area around Memphis. As a manifestation of Ptah, Apis also was considered to be a symbol of the king, embodying the qualities of kingship. In the region where Ptah was worshiped, cattle exhibited white patterning on their mainly black bodies, and so a belief grew up that the Apis calf had to have a certain set of markings suitable to its role. It was required to have a white triangular marking upon its forehead, a white Egyptian vulture wing outline on its back, a scarab mark under its tongue, a white crescent moon shape on its right flank, and double hairs on his tail.\n\nThe calf that matched these markings was selected from the herds, brought to a temple, given a harem of cows, and worshiped as an aspect of Ptah. The cow who was his mother was believed to have conceived him by a flash of lightning from the heavens, or from moonbeams. She also was treated specially, and given a special burial. At the temple, Apis was used as an oracle, his movements being interpreted as prophecies. His breath was believed to cure disease and his presence to bless those around with strength. A window was created in the temple through which he could be viewed and, on certain holidays, he was led through the streets of the city, bedecked with jewelry and flowers.\n\nBurial\n\nDetails of the mummification ritual of the sacred bull are written within the Apis papyrus. Sometimes the body of the bull was mummified and fixed in a standing position on a foundation made of wooden planks.\n\nBy the New Kingdom period, the remains of the sacred bulls were interred at the cemetery of Saqqara. The earliest known burial in Saqqara was performed in the reign of Amenhotep III by his son Thutmose; afterward, seven more bulls were buried nearby. Ramesses II initiated Apis burials in what now is known as the Serapeum, an underground complex of burial chambers at Saqqara for the sacred bulls, a site used throughout the rest of Ancient Egyptian history into the reign of Cleopatra.\n\nKhaemweset, the priestly son of Ramesses II (c. 1300 BCE), excavated a great gallery to be lined with the tomb chambers; another similar gallery was added by Psamtik I. The careful documentation of the ages of the animals in the later instances, with the regnal dates for their birth, enthronement, and death have thrown much light on the chronology from the Twenty-second Dynasty onward. The name of the mother cow and the place of the calf's birth are often recorded. The sarcophagi are of immense size and the burial must have entailed enormous expense. It is remarkable, therefore, that the ancient religious leaders contrived to bury one of the animals in the fourth year of Cambyses II.\n\nThe Apis was a protector of the deceased and linked to the pharaoh. Horns embellish some of the tombs of ancient pharaohs and Apis often was depicted on private coffins as a powerful protector. As a form of Osiris, ruler of the underworld, it was believed that to be under the protection of Apis would give the person control over the four winds in the afterlife.\n\nFrom animal to human\n\nAccording to Arrian, Apis was one of the Egyptian deities Alexander the Great propitiated by offering a sacrifice during his seizure of Ancient Egypt from the Persians. After Alexander's death, his general Ptolemy I Soter made efforts to integrate Egyptian religion with that of the new Hellenic rulers. Ptolemy's policy was to find a deity that might win the reverence of both groups, despite the curses of the Egyptian religious leaders against the deities of the previous foreign rulers (i.e. Set, lauded by the Hyksos). Without success, Alexander had attempted to use Amun for this purpose, but that deity was more prominent in Upper Egypt and not for those in Lower Egypt, where the Greeks had stronger influence. Since the Greeks had little respect for animal-headed deities, a Greek statue was created as an idol and proclaimed as an anthropomorphic equivalent of the highly popular Apis. It was named Aser-hapi (i.e. Osiris-Apis), which became Serapis, and later was said to represent Osiris fully, rather than just his Ka.\n\nThe earliest mention of a Serapis is in the authentic death scene of Alexander, from the royal diaries. Here, Serapis has a temple at Babylon, and is of such importance that he alone is named as being consulted on behalf of the dying Alexander. The presence of this temple in Babylon radically altered perceptions of the mythologies of this era, although it has been discovered that the unconnected Babylonian deity Ea was entitled Serapsi, meaning king of the deep, and it is Serapsi who is referred to in the diaries, not Serapis. The significance of this Serapsi in the Hellenic psyche, however, due to its involvement in Alexander's death, also may have contributed to the choice of Osiris-Apis as the chief Ptolemaic deity during their occupation of Ancient Egypt.\n\nAccording to Plutarch, Ptolemy stole the statue from Sinope, having been instructed in a dream by the Unknown God to bring the statue to Alexandria, where the statue was pronounced to be \"Serapis\" by two religious experts. Among those experts was one of the Eumolpidae, the ancient family from which the hierophant of the Eleusinian Mysteries traditionally had been chosen since before any historical records. The other expert supposedly was the scholarly Egyptian priest Manetho, which increased acceptability from both the Egyptians and the Greeks.\n\nPlutarch may not be correct, however, as some Egyptologists assert that the Sinope in Plutarch's report is the hill of Sinopeion, a name given to the site of an existing Serapeum at Memphis. Also, according to Tacitus, Serapis (i.e. Apis explicitly identified as Osiris in full) had been the tutelary deity of the village of Rhacotis, before it suddenly expanded into the great capital of \"Alexandria\".\n\nBeing introduced by the Greeks, understandably, the statue depicted a fully human figure resembling Hades or Pluto, both being kings of the Greek underworld. The figure was enthroned with the modius, which is a basket or a grain-measure, on his head, a Greek symbol for the land of the dead. He also held a sceptre, indicating rulership, and Cerberus, gatekeeper of the underworld, rested at his feet. It also had what appeared to be a serpent at its base, fitting the Egyptian symbol of sovereignty, the uraeus.\n\nWith his (i.e., Osiris') wife, Isis, and their son (at this point in history) Horus (in the form of Harpocrates), Serapis won an important place in the Greek world, reaching Ancient Rome, with Anubis being identified as Cerberus.\n\nSee also"
 },
 {
  "title": "Apis (Greek mythology)",
  "revision_id": "1341913692",
  "matched_by": "title-minus-qualifier",
  "text": "Apis (/ˈeɪpɪs/; Ancient Greek: Ἄπις derived from apios \"far-off\" or \"of the pear-tree\") is the name of a figure, or several figures, appearing in the earliest antiquity according to Greek mythology and historiography. It is uncertain exactly how many figures of the name Apis are to be distinguished, particularly due to variation of their genealogies. A common element is that an Apis was an early king in the Peloponnesus that had a territory named after himself and that Apis was often, but not always, ascribed an Egyptian origin. For the sake of convenience, the variant myths are presented here as if they dealt with separate characters.\n\nApis, king of Argos. He was a son of Phoroneus by the nymph Teledice, and brother of Niobe. During his reign, he established a tyrannical government and called the Peloponnesus after his own name Apia, but was eventually killed in a conspiracy headed by Thelxion, king of Sparta, and Telchis.\n\nApis, king of Sicyon and son of Telchis.\n\nApis, according to Aeschylus was a seer and healer and a son of Apollo. In The Suppliants, the Argive king Pelasgus, son of Palaechthon, relates that Apis once came from Naupactus and freed Argos from throngs of snakes, which \"Earth, defiled by the pollution of bloody deeds of old, had caused to spring up\" and plague the country. Apis \"worked the cure by sorcery and spells to the content of the Argive land.\" To commemorate his deed, the relieved territory was henceforth referred to as \"the Apian land\" (Apia khōra) after his name. Note that \"the Apian land\" appears to comprise not just Argos: Pelasgus describes his kingdom as stretching so far as the northernmost boundaries of Greece, and comprising the territories of Paeonia and Dodona.\n\nApis, son of Jason, was a native of Pallantium, Arcadia. He participated in the funeral games of Azan and was accidentally killed by Aetolus, who ran him over with the chariot. For the murder, Aetolus was sent into exile by the children of Apis. Apollodorus relates the same of Apis, son of Phoroneus, apparently confounding the two mythological namesakes.\n\nNotes"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q165194",
  "label": "application programming interface",
  "description": "software interface between computers and/or programs",
  "aliases": [],
  "claims": {
   "P31": [
    "Q66747126",
    "Q11862829",
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q23808",
    "Q241317",
    "Q132364",
    "Q142174244"
   ]
  },
  "revision_id": "2569848557",
  "value_labels": {
   "Q66747126": "computer science term",
   "Q11862829": "academic discipline",
   "Q1047113": "field of study",
   "Q2267705": "field of study",
   "Q23808": "computer interface",
   "Q241317": "computing platform",
   "Q132364": "communication protocol",
   "Q142174244": "programming interface"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q208150",
  "label": "Apis",
  "description": "sacred bull in Egyptian mythology",
  "aliases": [
   "Hapis",
   "Hapi-ankh"
  ],
  "claims": {
   "P31": [
    "Q146083"
   ],
   "P361": [
    "Q447131"
   ],
   "P1889": [
    "Q225246"
   ]
  },
  "revision_id": "2566530936",
  "value_labels": {
   "Q146083": "Ancient Egyptian deity",
   "Q447131": "religion of ancient Egypt",
   "Q225246": "Apis"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3620609",
  "label": "Apis",
  "description": "set of mythological Greek characters",
  "aliases": [],
  "claims": {
   "P31": [
    "Q26214208"
   ],
   "P527": [
    "Q618662",
    "Q38366",
    "Q618664",
    "Q14590069"
   ],
   "P1889": [
    "Q225246"
   ]
  },
  "revision_id": "2195142205",
  "value_labels": {
   "Q26214208": "set of mythological Greek characters",
   "Q618662": "Apis",
   "Q38366": "Apis",
   "Q618664": "Apis",
   "Q14590069": "Apis",
   "Q225246": "Apis"
  },
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
  "ancestor_of": "Q165194",
  "level": 1,
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
  "ancestor_of": "Q165194",
  "level": 1,
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
  "ancestor_of": "Q165194",
  "level": 1,
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
  "ancestor_of": "Q165194",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q23808",
  "label": "computer interface",
  "description": "concept of computer science; point of interaction between two things",
  "aliases": [
   "software interface",
   "interface"
  ],
  "claims": {
   "P279": [
    "Q110558466",
    "Q1129239"
   ],
   "P361": [
    "Q21198"
   ],
   "P1889": [
    "Q64830866",
    "Q2384798"
   ]
  },
  "revision_id": "2567811964",
  "ancestor_of": "Q165194",
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
  "ancestor_of": "Q165194",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q132364",
  "label": "communication protocol",
  "description": "system for exchanging messages between computing systems",
  "aliases": [
   "computer protocol",
   "protocol",
   "computer communication protocol",
   "computer communications protocol"
  ],
  "claims": {
   "P279": [
    "Q317623",
    "Q6046311"
   ],
   "P361": [
    "Q67080166"
   ],
   "P527": [
    "Q1163115",
    "Q15836568"
   ]
  },
  "revision_id": "2565189976",
  "ancestor_of": "Q165194",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q142174244",
  "label": "programming interface",
  "description": "",
  "aliases": [],
  "claims": {},
  "revision_id": "2569812335",
  "ancestor_of": "Q165194",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q19478619",
  "label": "metaclass",
  "description": "class which has instances that are all themselves classes",
  "aliases": [
   "Wikidata metaclass",
   "Wikidata metaclasses"
  ],
  "claims": {
   "P31": [
    "Q151885",
    "Q19868531",
    "Q115490628"
   ],
   "P279": [
    "Q16889133"
   ],
   "P361": [
    "Q324254"
   ],
   "P1889": [
    "Q19828331",
    "Q123369568",
    "Q1924819",
    "Q24017414"
   ]
  },
  "revision_id": "2559895276",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q137426749",
  "label": "type of term",
  "description": "metaclass for term",
  "aliases": [],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q21146257",
    "Q5962346"
   ]
  },
  "revision_id": "2537740123",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q137429456",
  "label": "type of concept",
  "description": "metaclass for concepts",
  "aliases": [
   "concept type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ]
  },
  "revision_id": "2552482529",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q12812139",
  "label": "specialized term",
  "description": "word or expression with a technical definition",
  "aliases": [
   "jargon",
   "term of art",
   "specialised term",
   "technical term"
  ],
  "claims": {
   "P31": [
    "Q137426749"
   ],
   "P279": [
    "Q1969448"
   ],
   "P361": [
    "Q1391494"
   ],
   "P1889": [
    "Q14943987",
    "Q1969448"
   ]
  },
  "revision_id": "2551807057",
  "ancestor_of": "Q165194",
  "level": 2,
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
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q105948247",
  "label": "knowledge system",
  "description": "systems of knowledge produced over time through interactions with other human beings",
  "aliases": [
   "knowledge systems"
  ],
  "claims": {
   "P31": [
    "Q96116695"
   ],
   "P279": [
    "Q3622126"
   ],
   "P527": [
    "Q9081"
   ]
  },
  "revision_id": "2522085818",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110403031",
  "label": "knowledge type",
  "description": "Wikidata metaclass",
  "aliases": [
   "type of knowledge"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q140458154"
   ],
   "P1889": [
    "Q110402867",
    "Q125161275"
   ]
  },
  "revision_id": "2548067834",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q26256810",
  "label": "topic",
  "description": "topic or area addressed by a work or set of works",
  "aliases": [
   "issue",
   "subject",
   "theme",
   "topic of a work",
   "subject matter of a work",
   "matter",
   "main subject",
   "main topic",
   "subject matter",
   "gum:SubjectMatter"
  ],
  "claims": {
   "P279": [
    "Q11028",
    "Q12488383",
    "Q16514889"
   ],
   "P460": [
    "Q1053916",
    "Q200801"
   ],
   "P1889": [
    "Q14095863",
    "Q9340580"
   ]
  },
  "revision_id": "2567187301",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q110558466",
  "label": "interface",
  "description": "point of interaction of two items, not necessarily physical",
  "aliases": [],
  "claims": {
   "P31": [
    "Q96251598",
    "Q137430548"
   ],
   "P279": [
    "Q488383"
   ],
   "P361": [
    "Q2048825"
   ]
  },
  "revision_id": "2552527349",
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1129239",
  "label": "controller",
  "description": "computing device that interfaces with a more peripheral device",
  "aliases": [
   "interface controller",
   "CU",
   "control unit"
  ],
  "claims": {
   "P31": [
    "Q3966"
   ],
   "P279": [
    "Q2384798"
   ],
   "P361": [
    "Q68"
   ],
   "P1889": [
    "Q165678"
   ]
  },
  "revision_id": "2557406759",
  "ancestor_of": "Q165194",
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
  "ancestor_of": "Q165194",
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
  "ancestor_of": "Q165194",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q146083",
  "label": "Ancient Egyptian deity",
  "description": "deities in the Ancient Egyption religion",
  "aliases": [
   "ancient Egyptian deities",
   "ancient Egyptian god",
   "ancient Egyptian goddess"
  ],
  "claims": {
   "P279": [
    "Q178885"
   ],
   "P361": [
    "Q205740",
    "Q108092253"
   ]
  },
  "revision_id": "2567814003",
  "ancestor_of": "Q208150",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q178885",
  "label": "deity",
  "description": "natural or supernatural god or goddess, divine being",
  "aliases": [
   "god",
   "goddess",
   "God",
   "deities"
  ],
  "claims": {
   "P279": [
    "Q4271324",
    "Q28855038"
   ],
   "P460": [
    "Q17398299",
    "Q190"
   ],
   "P1889": [
    "Q13397408",
    "Q386933",
    "Q131786385"
   ]
  },
  "revision_id": "2572865073",
  "ancestor_of": "Q208150",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q26214208",
  "label": "set of mythological Greek characters",
  "description": "set of mythological Greek characters which don't have any connection to each other",
  "aliases": [],
  "claims": {
   "P279": [
    "Q15623926"
   ],
   "P1889": [
    "Q28061975"
   ]
  },
  "revision_id": "2370025004",
  "ancestor_of": "Q3620609",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15623926",
  "label": "Wikimedia set index article",
  "description": "list article about a set of items of a specific type that share the same (or similar) name",
  "aliases": [
   "set index article",
   "sia",
   "SIA",
   "Wikimedia set index",
   "set index",
   "set indices",
   "set index page",
   "Wikimedia set index page",
   "Wikipedia set index article"
  ],
  "claims": {
   "P279": [
    "Q13406463",
    "Q138717185"
   ],
   "P460": [
    "Q4167410"
   ],
   "P1889": [
    "Q4167410",
    "Q13406463",
    "Q26884324",
    "Q80096233"
   ]
  },
  "revision_id": "2563577296",
  "ancestor_of": "Q3620609",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 3: Amazon Web Services (`h00skqgqmn`)

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
[
 {
  "title": "Amazon Web Services",
  "revision_id": "1376822161",
  "matched_by": "title",
  "text": "Amazon Web Services, Inc. (AWS) is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered, pay-as-you-go basis.\n\nClients often use this in combination with autoscaling (a process that allows a client to use more computing in times of high application usage, and then scale down to reduce costs when there is less traffic). These cloud computing web services provide various services related to networking, compute, storage, middleware, IoT and other processing capacity, as well as software tools via AWS server farms. This frees clients from managing, scaling, and patching hardware and operating systems.\n\nOne of the foundational services is Amazon Elastic Compute Cloud (EC2), which allows users to have at their disposal a virtual cluster of computers, with extremely high availability, which can be interacted with over the Internet via REST APIs, a CLI or the AWS console. AWS's virtual computers emulate most of the attributes of a real computer, including hardware central processing units (CPUs) and graphics processing units (GPUs) for processing; local/RAM memory; hard-disk (HDD)/SSD storage; a choice of operating systems; networking; and pre-loaded application software such as web servers, databases, and customer relationship management (CRM).\n\nAWS services are delivered to customers via a network of AWS server farms located throughout the world. Fees are based on a combination of usage (known as a \"Pay-as-you-go\" model), hardware, operating system, software, and networking features chosen by the subscriber requiring various degrees of availability, redundancy, security, and service options. Subscribers can pay for a single virtual AWS computer, a dedicated physical computer, or clusters of either. Amazon provides select portions of security for subscribers (e.g. physical security of the data centers) while other aspects of security are the responsibility of the subscriber (e.g. account management, vulnerability scanning, patching). AWS operates from many global geographical regions, including nine in North America.\n\nAmazon markets AWS to subscribers as a way of obtaining large-scale computing capacity more quickly and cheaply than building an actual physical server farm. All services are billed based on usage, but each service measures usage in varying ways. As of 2023 Q1, AWS has 31% market share for cloud infrastructure while the next two competitors Microsoft Azure and Google Cloud have 25%, and 11% respectively, according to Synergy Research Group. AWS was the first cloud provider to build infrastructure specifically for U.S. government with respect to security and compliance requirements (2011; launched AWS GovCloud), accredited to support classified workloads (2014; launched AWS Top Secret), and achieve accreditation across all U.S. government data classifications (2017; launched AWS Secret).\n\nServices\n\nAs of 2025 AWS comprises over 200 products and services including computing, storage, networking, database, analytics, application services, deployment, management, machine learning, mobile, developer tools, RobOps and tools for the Internet of Things. The most popular include Amazon Elastic Compute Cloud (EC2), Amazon Simple Storage Service (Amazon S3), Amazon Connect, and AWS Lambda (a serverless function that can perform arbitrary code written in any language that can be configured to be triggered by hundreds of events, including HTTP calls).\n\nServices expose functionality through APIs for clients to use in their applications. These APIs are accessed over HTTP, using the REST architectural style and SOAP protocol for older APIs and exclusively JSON for newer ones. Clients can interact with these APIs in various ways, including from the AWS console (a website), by using SDKs written in various languages (such as Python, Java, and JavaScript), or by making direct REST calls.\n\nHistory\n\nFounding (2000–2005)\n\nThe genesis of AWS came in the early 2000s. After building Merchant.com, Amazon's e-commerce-as-a-service platform that offers third-party retailers a way to build their own web-stores, Amazon pursued service-oriented architecture as a means to scale its engineering operations, led by then CTO Allan Vermeulen.\n\nAround the same time frame, Amazon was frustrated with the speed of its software engineering, and sought to implement various recommendations put forth by Matt Round, an engineering leader at the time, including maximization of autonomy for engineering teams, adoption of REST, standardization of infrastructure, removal of gate-keeping decision-makers (bureaucracy), and continuous deployment. He also called for increasing the percentage of the time engineers spent building the software rather than doing other tasks. Amazon created \"a shared IT platform\" so its engineering organizations, which were spending 70% of their time on \"undifferentiated heavy-lifting\" such as IT and infrastructure problems, could focus on customer-facing innovation instead. Besides, in dealing with unusual peak traffic patterns, especially during the holiday season, by migrating services to commodity Linux hardware and relying on open source software, Amazon's Infrastructure team, led by Tom Killalea, Amazon's first CISO, had already run its data centers and associated services in a \"fast, reliable, cheap\" way.\n\nIn July 2002 Amazon.com Web Services, managed by Colin Bryar, launched its first web services, opening up the Amazon.com platform to all developers. Over one hundred applications were built on top of it by 2004. This unexpected developer interest took Amazon by surprise and convinced them that developers were \"hungry for more\".\n\nBy the summer of 2003, Andy Jassy had taken over Bryar's portfolio at Rick Dalzell's behest, after Vermeulen, who was Bezos' first pick, declined the offer. Jassy subsequently mapped out the vision for an \"Internet OS\" made up of foundational infrastructure primitives that alleviated key impediments to shipping software applications faster. By fall 2003, databases, storage, and compute were identified as the first set of infrastructure pieces that Amazon should launch.\n\nJeff Barr, an early AWS employee, credits himself, Vermeulen, Jassy, Bezos, and a few others for coming up with the idea that would evolve into EC2, S3, and RDS; Jassy recalls the idea was the result of brainstorming for about a week with \"ten of the best technology minds and ten of the best product management minds\" on about ten different Internet applications and the most primitive building blocks required to build them. Werner Vogels cites Amazon's desire to make the process of \"invent, launch, reinvent, relaunch, start over, rinse, repeat\" as fast as it could was leading them to break down organizational structures with \"two-pizza teams\" and application structures with distributed systems; and that these changes ultimately paved way for the formation of AWS and its mission \"to expose all of the atomic-level pieces of the Amazon.com platform\". According to Brewster Kahle, co-founder of Alexa Internet, which was acquired by Amazon in 1999, his start-up's compute infrastructure helped Amazon solve its big data problems and later informed the innovations that underpinned AWS.\n\nJassy assembled a founding team of 57 employees from a mix of engineering and business backgrounds to kick-start these initiatives, with a majority of the hires coming from outside the company. They included Jeff Lawson, the Twilio CEO; Adam Selipsky, the Tableau CEO; and Mikhail Seregine, a co-founder at Outschool.\n\nIn late 2003, the concept for compute, which would later launch as EC2, was reformulated when Chris Pinkham and Benjamin Black presented a paper internally describing a vision for Amazon's retail computing infrastructure that was completely standardized, completely automated, and would rely extensively on web services for services such as storage and would draw on internal work already underway. Near the end of their paper, they mentioned the possibility of selling access to virtual servers as a service, proposing the company could generate revenue from the new infrastructure investment. Thereafter Pinkham, Willem van Biljon, and lead developer Christopher Brown developed the Amazon EC2 service, with a team in Cape Town, South Africa.\n\nIn October 2004, Amazon released Alexa Web Information Service (AWIS) as beta. In November 2004, AWS launched its first infrastructure service, as beta: Simple Queue Service (SQS)., and officially launched in July 2006.\n\nS3, EC2, and other first-generation services (2006–2010)\n\nOn March 14, 2006, AWS launched Amazon S3 cloud storage, and that was the first AWS' IaaS that was generally available, followed by EC2 in August 2006. Pi Corporation, a startup Paul Maritz co-founded, was the first beta-user of EC2 outside of Amazon, while Microsoft was among EC2's first enterprise customers. Later that year SmugMug, one of the early AWS adopters, attributed savings of around US$400,000 in storage costs to S3. According to Vogels, S3 was built with 8 microservices when it launched in 2006 and had over 300 microservices by 2022.\n\nIn September 2007, AWS announced its annual Start-up Challenge, a contest with prizes worth $100,000 for entrepreneurs and software developers in the US using AWS services such as S3 and EC2 to build their businesses. The first edition saw participation from Justin.tv, which Amazon later acquired in 2014. Ooyala, an online media company, was the eventual winner.\n\nAWS offers, as of June 16, 2022, two block-storage options: the EC2 Instance Store and the Elastic Block Store (EBS). Some Amazon EBS features that help with data management, backups, and performance tuning include:\n\nEBS volume tagging to allow the user to find and filter EBS resources on the Amazon Console and CLI.\n\nSoftware-level RAID arrays to enable creation of groups of EBS volumes with high performance network throughput between them, using the standard RAID protocol.\n\nAdditional AWS services from this period include SimpleDB, Mechanical Turk, Elastic Beanstalk, Relational Database Service, DynamoDB, CloudWatch, Simple Workflow, CloudFront, and Availability Zones.\n\nGrowth (2010–2015)\n\nIn November 2010, it was reported that all of Amazon.com's retail sites had migrated to AWS. Prior to 2012, AWS was considered a part of Amazon.com and so its revenue was not delineated in Amazon financial statements. In that year industry watchers for the first time estimated AWS revenue to be over $1.5 billion.\n\nOn November 27, 2012, AWS hosted its first major annual conference, re:Invent with a focus on AWS's partners and ecosystem, with over 150 sessions. The three-day event was held in Las Vegas because of its relatively cheaper connectivity with locations across the United States and the rest of the world. Andy Jassy and Werner Vogels presented keynotes, with Jeff Bezos joining Vogels for a fireside chat. AWS opened early registrations at US$1,099 per head for their customers from over 190 countries. On stage with Andy Jassy at the event which saw around 6000 attendees, Reed Hastings, CEO at Netflix, announced plans to migrate 100% of Netflix's infrastructure to AWS.\n\nTo support industry-wide training and skills standardization, AWS began offering a certification program for computer engineers, on April 30, 2013, to highlight expertise in cloud computing. Later that year, in October, AWS launched Activate, a program for start-ups worldwide to leverage AWS credits, third-party integrations, and free access to AWS experts to help build their business.\n\nIn 2014, AWS launched its partner network, AWS Partner Network (APN), which is focused on helping AWS-based companies grow and scale the success of their business with close collaboration and best practices.\n\nIn October 2014, Amazon Aurora was launched.\n\nIn January 2015, Amazon Web Services acquired Annapurna Labs, an Israel-based microelectronics company for a reported US$350–370M.\n\nIn April 2015, Amazon.com reported AWS was profitable, with sales of $1.57 billion in the first quarter of the year and $265 million of operating income. Founder Jeff Bezos described it as a fast-growing $5 billion business; analysts described it as \"surprisingly more profitable than forecast\". In October, Amazon.com said in its Q3 earnings report that AWS's operating income was $521 million, with operating margins at 25 percent. AWS's 2015 Q3 revenue was $2.1 billion, a 78% increase from 2014's Q3 revenue of $1.17 billion. 2015 Q4 revenue for the AWS segment increased 69.5% y/y to $2.4 billion with a 28.5% operating margin, giving AWS a $9.6 billion run rate. In 2015, Gartner estimated that AWS customers are deploying 10x more infrastructure on AWS than the combined adoption of the next 14 providers.\n\nSince 2016\n\nIn 2016 Q1, revenue was $2.57 billion with net income of $604 million, a 64% increase over 2015 Q1 that resulted in AWS being more profitable than Amazon's North American retail business for the first time. Jassy was thereafter promoted to CEO of the division. Around the same time, Amazon experienced a 42% rise in stock value as a result of increased earnings, of which AWS contributed 56% to corporate profits.\n\nAWS had $17.46 billion in annual revenue in 2017. By the end of 2020, the number had grown to $46 billion. Reflecting the success of AWS, Jassy's annual compensation in 2017 hit nearly $36 million.\n\nIn January 2018, Amazon launched a unified autoscaling service on AWS. This new service unifies and builds on AWS existing, service-specific, scaling features like EC2 Auto Scaling groups, that was launched in August 2006.\n\nIn November 2018, AWS announced customized ARM cores for use in its servers. Also in November 2018, AWS announced AWS Ground Stations to communicate with customers' satellites.\n\nIn 2019, AWS reported 37% yearly growth and accounted for 12% of Amazon's revenue (up from 11% in 2018).\n\nIn April 2021, AWS reported 32% yearly growth and accounted for 32% of $41.8 billion cloud market in Q1 2021.\n\nIn January 2022, AWS joined the MACH Alliance, a non-profit enterprise technology advocacy group.\n\nIn June 2022, it was reported that in 2019 Capital One had not secured their AWS resources properly, and was subject to a data breach by a former AWS employee. The employee was convicted of hacking into the company's cloud servers to steal customer data and use computer power to mine cryptocurrency. The ex-employee was able to download the personal information of more than 100 million Capital One customers.\n\nIn June 2022, AWS announced they had launched the AWS Snowcone, a small computing device, to the International Space Station on the Axiom Mission 1.\n\nIn September 2023, AWS announced it would become AI startup Anthropic's primary cloud provider. Amazon has committed to investing up to $4 billion in Anthropic and will have a minority ownership position in the company. AWS also announced the GA of Amazon Bedrock, a fully managed service that makes foundation models (FMs) from leading AI companies available through a single application programming interface (API)\n\nIn April 2024, AWS announced a new service called Deadline Cloud, which lets customers set up, deploy and scale up graphics and visual effects rendering pipelines on AWS cloud infrastructure.\n\nIn July 2024, AWS won a $1.3 billion (A$2 billion) contract with Australia's government to build a top-secret cloud service. The service included a partnership with the Australian Signals Directorate (ASD). The ASD director general Rachel Noble said the service would \"provide a state-of-the-art collaborative space for our intelligence and defense community to store and access top-secret data”.\n\nIn December 2024, AWS announced Amazon Nova, its own family of foundation models. These models, offered through Amazon Bedrock, are designed for various tasks including content generation, video understanding, and building agentic applications. They are available in six different sizes. At the end of 2024, AWS announced Project Rainier, a massive one-of-a-kind machine \"designed to usher in the next generation of AI.\"\n\nIn February 2026, India's National Informatics Centre (NIC), a department under the Ministry of Electronics and Information Technology, announced deployment of AWS Outposts within its data centers as part of the government's Meghraj 2.0 hybrid cloud initiative, working with Indian data center provider Yotta Data Services. The deployment enables sensitive government workloads to remain within NIC's physical infrastructure while accessing AWS cloud services including Amazon EKS, Amazon RDS, and Amazon S3.\n\nIn March and April of 2026, during the 2026 Iran War, Iranian drone and missile strikes damaged AWS data centers in the United Arab Emirates (me-central-1) and Bahrain (me-south-1) regions, in the first deliberate military targeting of a commercial data center. Iran claimed the data centers hosted US military workloads. AWS advised customers to migrate to other regions.\n\nOn 30 June 2026, AWS Secret Cloud for Industry (ASCI) was made generally available. It holds a Provisional Authorization at Impact Level 6 from the Defense Information Systems Agency and uses the same Defense Counterintelligence and Security Agency (DCSA) compliance framework that cleared defense contractors already use for on-premises classified systems. Northrop Grumman was the first defense contractor to deploy classified workloads on ASCI. To speed up the migration and to attract customers AWS launched ASCI Accelerator Initiative. The U.S. Intelligence Community (IC) launched IC Accelerated Modernization Framework (ICAMF) which subsidizes transfer to AWS from on-site systems. ASCI provides physically and logically isolated environment purpose-built to meet the most demanding security and compliance requirements. They also created AWS Forward Deployed Engineering (FDE) organization. It embeds AWS frontier teams—working with purpose-built agents—directly inside customer teams (business, engineering, and security teams) to build and deploy production AI systems with their data, governance, and processes.\n\nCustomer base\n\nIn October 2013, AWS was awarded a $600M contract with the CIA.\n\nBy 2019, it was reported that more than 80% of Germany's listed DAX companies used AWS. In August 2019, the U.S. Navy said it moved 72,000 users from six commands to an AWS cloud system as a first step toward pushing all of its data and analytics onto the cloud.\n\nIn January 2021, Amazon announced that it would suspend Parler from Amazon Web Services, stating Parler hosted “violent content” that violates its terms of service. Later in 2021, DISH Network announced it would develop and launch its 5G network on AWS. It was also reported that spy agencies and government departments in the UK, such as GCHQ, MI5, MI6, and the Ministry of Defence, contracted AWS to host their classified materials.\n\nIn 2022, Amazon shared a $9 billion contract from the United States Department of Defense for cloud computing with Google, Microsoft, and Oracle.\n\nAWS won a $581 million contract from the U.S. Air Force in January 2026 to provide cloud services and specific Amazon data centers as part of the Cloud One Program, the Air Force's enterprise cloud environment. \n\nMultiple financial services firms have shifted to AWS in some form. Notable customers include NASA and the Obama presidential campaign of 2012.\n\nSignificant service outages\n\nOn April 20, 2011, AWS suffered a major outage. Parts of the Elastic Block Store service became \"stuck\" and could not fulfill read/write requests. It took at least two days for the service to be fully restored.\n\nOn June 29, 2012, several websites that rely on Amazon Web Services were taken offline due to a severe storm in Northern Virginia, where AWS's largest data center cluster is located.\n\nOn October 22, 2012, a major outage occurred, affecting many sites including Reddit, Foursquare, and Pinterest. The cause was a memory leak bug in"
 },
 {
  "title": "AWS (band)",
  "revision_id": "1374282403",
  "matched_by": "title-minus-qualifier",
  "text": "AWS (pronounced ah-vi-esh) is a Hungarian post-hardcore band formed in early November 2006 by Örs Siklósi (September 4, 1991 – February 5, 2021), Bence Brucker, Dániel Kökényes, Soma Schiszler and Áron Veress. Their music is characterized by diversity, powerful performances, and sudden changes, which utilizes metal, psychedelic rock, alternative and post-rock styles. Up to now, they have released five studio albums, two live albums and fourteen video clips. Their music videos often have juxtapositions of images of violence and celebrities in order to bring light to problems that the world faces, exhibiting what they call being \"anti-celebrity\". They represented Hungary at the Eurovision Song Contest 2018 in Portugal with the song \"Viszlát nyár\".\n\nCareer\n\nThe band played Sziget Festival in 2010 and have toured across Europe, in Austria, England, the Netherlands, Romania, Slovenia, and Spain. They won the MTV Brand award for New Winning Band. They have toured with Blind Myself.\n\nAt the beginning of 2017, Soma Schiszler joined the team. On 6 December 2017, it was announced that AWS would compete in A Dal 2018, the Hungarian national selection process for the Eurovision Song Contest 2018. Their song \"Viszlát Nyár\" (Goodbye Summer) won the competition and as a result, represented Hungary in the Eurovision Song Contest 2018. They qualified from the 2nd semifinal, and ended in 21st place in the final with 93 points.\n\nDuring their stint at Eurovision Song Contest it was announced that AWS were invited to play at Wacken Open Air in August 2018. In October the same year AWS released their fourth full-length studio record called Fekete Részem which charted at no. 2 at Hungarian Albums Charts a week later.\n\nLead singer Örs Siklósi died on 5 February 2021 from leukaemia at the age of 29. The band announced his death on Instagram the following day.\n\nOn 16 January 2023, the band introduced the new vocalist, Tamás Stefán.\n\nMusical style\n\nAccording to an interview with the German-language Hungarian newspaper Budapester Zeitung the musicians came in contact with rock and metal music during their childhoods. Bands like Nirvana, Metallica and several Hungarian metal bands were the first ones they listened to. The musicians named Linkin Park, Pantera, System of a Down, and Korn, as well as Hungarian acts Superbutt, Subscribe and Isten Háta Mögött as their personal musical influences.\n\nThe band's lyrics on their debut record Fata Morgana were mostly written in English but they decided to write song lyrics in Hungarian for future songs. For Fata Morgana, the band wrote the lyrics in Hungarian first and later translated them into English. The lyrical themes deal with personal experiences as well as societal and economic themes.\n\nTheir sound has been described as having catchy melodies, a clear Hungarian character, vocal harmonies and a decent groove. Some songs were described to be mass appealing, modern metal.\n\nDiscography\n\nStudio albums\n\nLive albums\n\nExtended plays\n\nSingles\n\nNotes"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q456157",
  "label": "Amazon Web Services",
  "description": "subsidiary of Amazon that provides on-demand cloud computing platforms on a metered pay-as-you-go basis",
  "aliases": [
   "aws.amazon.com"
  ],
  "claims": {
   "P31": [
    "Q241317",
    "Q1210425",
    "Q1153767",
    "Q117350903",
    "Q4830453"
   ],
   "P527": [
    "Q2593067",
    "Q4033880",
    "Q4033875",
    "Q2072356",
    "Q56358285",
    "Q733115",
    "Q18754151",
    "Q15731832",
    "Q48843359",
    "Q110643724",
    "Q1628791",
    "Q28035268",
    "Q65045028",
    "Q4740866",
    "Q21462856",
    "Q110644167",
    "Q621753",
    "Q17012109",
    "Q110658259",
    "Q110658289",
    "Q22908871",
    "Q110659313",
    "Q110705475",
    "Q110644154",
    "Q16992245",
    "Q65203360",
    "Q110705619",
    "Q110705675",
    "Q456090",
    "Q110705906",
    "Q110705945",
    "Q110720922",
    "Q110644161",
    "Q110720930",
    "Q110731414",
    "Q88461433",
    "Q30681184",
    "Q74235852",
    "Q104861519",
    "Q110772254",
    "Q110644152",
    "Q110658215",
    "Q110644150",
    "Q110943975",
    "Q114603215",
    "Q124052638",
    "Q133457878",
    "Q120979360"
   ]
  },
  "revision_id": "2564898932",
  "value_labels": {
   "Q241317": "computing platform",
   "Q1210425": "internet hosting service",
   "Q1153767": "platform as a service",
   "Q117350903": "hyperscaler",
   "Q4830453": "business",
   "Q2593067": "Amazon S3",
   "Q4033880": "Amazon Simple Queue Service",
   "Q4033875": "Amazon Simple Email Service",
   "Q2072356": "Amazon Elastic Compute Cloud",
   "Q56358285": "Amazon Kinesis",
   "Q733115": "Amazon Mechanical Turk",
   "Q18754151": "Amazon Aurora",
   "Q15731832": "Amazon DynamoDB",
   "Q48843359": "Amazon Neptune",
   "Q110643724": "Amazon Braket",
   "Q1628791": "Amazon CloudFront",
   "Q28035268": "Amazon ElastiCache",
   "Q65045028": "Amazon SageMaker",
   "Q4740866": "Amazon Route 53",
   "Q21462856": "AWS Lambda",
   "Q110644167": "Amazon Elastic Transcoder",
   "Q621753": "Amazon Relational Database Service",
   "Q17012109": "Amazon Redshift",
   "Q110658259": "Amazon Timestream",
   "Q110658289": "AWS Global Accelerator",
   "Q22908871": "Amazon Simple Notification Service",
   "Q110659313": "Amazon GuardDuty",
   "Q110705475": "AWS Shield",
   "Q110644154": "AWS Ground Station",
   "Q16992245": "Amazon Elastic Block Store",
   "Q65203360": "Amazon Athena",
   "Q110705619": "AWS CodeBuild",
   "Q110705675": "Amazon Managed Blockchain",
   "Q456090": "Amazon CloudWatch",
   "Q110705906": "Amazon MQ",
   "Q110705945": "Amazon CodeGuru",
   "Q110720922": "AWS CodePipeline",
   "Q110644161": "Amazon Comprehend",
   "Q110720930": "Amazon Connect",
   "Q110731414": "AWS Fargate",
   "Q88461433": "Amazon Elastic Container Registry",
   "Q30681184": "Amazon Lex",
   "Q74235852": "Amazon Rekognition",
   "Q104861519": "AWS Glue",
   "Q110772254": "Amazon MemoryDB",
   "Q110644152": "Amazon Quantum Ledger Database",
   "Q110658215": "Elastic Load Balancing",
   "Q110644150": "AWS Wavelength",
   "Q110943975": "AWS Activate",
   "Q114603215": "AWS WAF",
   "Q124052638": "Amazon Bedrock",
   "Q133457878": "AWS Key Management Service",
   "Q120979360": "Amazon Trust Services"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q16516316",
  "label": "AWS",
  "description": "Hungarian post-hardcore band",
  "aliases": [],
  "claims": {
   "P31": [
    "Q215380"
   ]
  },
  "revision_id": "2553333806",
  "value_labels": {
   "Q215380": "musical group"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q846837",
  "label": "automatic weather station",
  "description": "set of sensors that record and provide physical measurements and meteorological parameters without any human intervention",
  "aliases": [
   "AWS"
  ],
  "claims": {
   "P31": [
    "Q130741448"
   ],
   "P279": [
    "Q190107"
   ]
  },
  "revision_id": "2554592420",
  "value_labels": {
   "Q130741448": "automated science",
   "Q190107": "weather station"
  },
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
  "ancestor_of": "Q456157",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1210425",
  "label": "internet hosting service",
  "description": "service that runs Internet servers, allowing organizations and individuals to serve content to the Internet",
  "aliases": [
   "hosting provider",
   "hosting",
   "hosting service"
  ],
  "claims": {
   "P31": [
    "Q130303173",
    "Q43229",
    "Q4830453"
   ],
   "P279": [
    "Q1668024"
   ],
   "P1889": [
    "Q115772193"
   ]
  },
  "revision_id": "2571681533",
  "ancestor_of": "Q456157",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1153767",
  "label": "platform as a service",
  "description": "category of cloud computing services",
  "aliases": [
   "PaaS",
   "application platform as a service",
   "aPaaS"
  ],
  "claims": {
   "P31": [
    "Q268592"
   ],
   "P279": [
    "Q1382299",
    "Q483639",
    "Q241317"
   ],
   "P1889": [
    "Q136910740"
   ]
  },
  "revision_id": "2558756936",
  "ancestor_of": "Q456157",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q117350903",
  "label": "hyperscaler",
  "description": "a large provider of datacenter infrastructure and cloud services",
  "aliases": [
   "cloud provider"
  ],
  "claims": {
   "P279": [
    "Q241317"
   ]
  },
  "revision_id": "2467999538",
  "ancestor_of": "Q456157",
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
  "ancestor_of": "Q456157",
  "level": 1,
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
  "ancestor_of": "Q456157",
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
  "ancestor_of": "Q456157",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q130303173",
  "label": "service type",
  "description": "Wikidata metaclass for service or provision of service",
  "aliases": [
   "type of service",
   "category of service"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q29028649"
   ],
   "P279": [
    "Q21146257"
   ],
   "P1889": [
    "Q2635669"
   ]
  },
  "revision_id": "2566594679",
  "ancestor_of": "Q456157",
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
  "ancestor_of": "Q456157",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1668024",
  "label": "service on Internet",
  "description": "technical ability afforded by the Internet",
  "aliases": [
   "online service",
   "service on the Internet",
   "Internet service"
  ],
  "claims": {
   "P279": [
    "Q1273271",
    "Q1640628",
    "Q340169"
   ],
   "P361": [
    "Q75"
   ],
   "P460": [
    "Q19967801"
   ],
   "P1889": [
    "Q1472399"
   ]
  },
  "revision_id": "2514001130",
  "ancestor_of": "Q456157",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q268592",
  "label": "industry",
  "description": "group of firms that produce a closely related set of raw materials, goods, or services",
  "aliases": [
   "economic industry",
   "industrial branch",
   "industry (economics)",
   "industries",
   "industrial sector"
  ],
  "claims": {
   "P31": [
    "Q29028649"
   ],
   "P279": [
    "Q16887380"
   ],
   "P361": [
    "Q3958441"
   ],
   "P527": [
    "Q783794"
   ],
   "P1889": [
    "Q8148",
    "Q3958441",
    "Q8187769"
   ]
  },
  "revision_id": "2559779969",
  "ancestor_of": "Q456157",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1382299",
  "label": "as a service",
  "description": "the delivery of solutions, applications, products, tools or technologies to a customer as a service",
  "aliases": [
   "*aaS",
   "everything as a service",
   "aaS",
   "anything as a service"
  ],
  "claims": {
   "P31": [
    "Q187931",
    "Q80096233"
   ],
   "P279": [
    "Q7406919"
   ]
  },
  "revision_id": "2556335596",
  "ancestor_of": "Q456157",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q483639",
  "label": "cloud computing",
  "description": "form of Internet-based computing, whereby shared resources, software and information are provided to computers and other devices",
  "aliases": [
   "cloud platform",
   "cloud",
   "utility computing",
   "network cloud"
  ],
  "claims": {
   "P279": [
    "Q771906",
    "Q241317",
    "Q1668024"
   ]
  },
  "revision_id": "2572545662",
  "ancestor_of": "Q456157",
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
  "ancestor_of": "Q456157",
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
  "ancestor_of": "Q456157",
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
  "ancestor_of": "Q456157",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q215380",
  "label": "musical group",
  "description": "musical ensemble which performs music",
  "aliases": [
   "music band",
   "musical project",
   "group",
   "band",
   "music group",
   "musical band",
   "musical ensemble"
  ],
  "claims": {
   "P279": [
    "Q2088357"
   ],
   "P460": [
    "Q2088357"
   ],
   "P1889": [
    "Q127334927",
    "Q16887380",
    "Q275186"
   ]
  },
  "revision_id": "2557689248",
  "ancestor_of": "Q16516316",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2088357",
  "label": "musical ensemble",
  "description": "group of people who perform instrumental and/or vocal music, with the ensemble typically known by a distinct name",
  "aliases": [
   "ensemble",
   "music ensemble",
   "music group",
   "musical group"
  ],
  "claims": {
   "P279": [
    "Q32178211",
    "Q105815710",
    "Q60557909"
   ],
   "P527": [
    "Q639669"
   ],
   "P460": [
    "Q215380"
   ],
   "P1889": [
    "Q29881657",
    "Q2250943"
   ]
  },
  "revision_id": "2564746459",
  "ancestor_of": "Q16516316",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q130741448",
  "label": "automated science",
  "description": "research conducted by machine",
  "aliases": [],
  "claims": {
   "P279": [
    "Q336"
   ]
  },
  "revision_id": "2329429574",
  "ancestor_of": "Q846837",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q190107",
  "label": "weather station",
  "description": "set of sensors that record and provide physical measurements and meteorological parameters",
  "aliases": [
   "meteorological station",
   "meteorological observation post",
   "meteorological observatory",
   "bureau station",
   "bureau of meteorology",
   "meteorological bureau"
  ],
  "claims": {
   "P279": [
    "Q1924376"
   ],
   "P527": [
    "Q3743695"
   ],
   "P1889": [
    "Q206542",
    "Q65007050",
    "Q3497441"
   ]
  },
  "revision_id": "2568580789",
  "ancestor_of": "Q846837",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q336",
  "label": "science",
  "description": "systematic study of the world through testable explanations, empirical evidence, and independent verification",
  "aliases": [
   "sciences",
   "general science",
   "scientific knowledge",
   "empirical sciences"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q8027727"
   ],
   "P279": [
    "Q105948247",
    "Q9081",
    "Q221173",
    "Q9471",
    "Q42240",
    "Q105606485"
   ],
   "P361": [
    "Q1881523"
   ],
   "P527": [
    "Q12132639",
    "Q7991",
    "Q34749",
    "Q816264",
    "Q5769081",
    "Q1665984",
    "Q6045936",
    "Q42240",
    "Q12042160",
    "Q133897036"
   ],
   "P460": [
    "Q43096377"
   ],
   "P1889": [
    "Q15854878",
    "Q1294710",
    "Q968451",
    "Q8027727"
   ]
  },
  "revision_id": "2567492224",
  "ancestor_of": "Q846837",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1924376",
  "label": "monitoring station",
  "description": "facility type for monitoring",
  "aliases": [
   "observation station",
   "monitoring facility",
   "monitoring site"
  ],
  "claims": {
   "P31": [
    "Q134496690"
   ],
   "P279": [
    "Q811979",
    "Q13226383"
   ]
  },
  "revision_id": "2550956883",
  "ancestor_of": "Q846837",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 3: Communication (`gisypzf6gf`)

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
[
 {
  "title": "Communication",
  "revision_id": "1376050739",
  "matched_by": "title",
  "text": "Communication is commonly defined as the transmission of information. Its precise definition is disputed and there are disagreements about whether unintentional or failed transmissions are included and whether communication not only transmits meaning but also creates it. Models of communication are simplified overviews of its main components and their interactions. Many models include the idea that a source uses a coding system to express information in the form of a message. The message is sent through a channel to a receiver who has to decode it to understand it. The main field of inquiry investigating communication is called communication studies.\n\nA common way to classify communication is by whether information is exchanged between humans, members of other species, or non-living entities such as computers. For human communication, a central contrast is between verbal and non-verbal communication. Verbal communication involves the exchange of messages in linguistic form, including spoken and written messages as well as sign language. Non-verbal communication happens without the use of a linguistic system, for example, using body language, touch, and facial expressions. Another distinction is between interpersonal communication, which happens between distinct persons, and intrapersonal communication, which is communication with oneself. Communicative competence is the ability to communicate well and applies to the skills of formulating messages and understanding them.\n\nNon-human forms of communication include animal and plant communication. Researchers in this field often refine their definition of communicative behavior by including the criteria that observable responses are present and that the participants benefit from the exchange. Animal communication is used in areas like courtship and mating, parent–offspring relations, navigation, and self-defense. Communication through chemicals is particularly important for the relatively immobile plants. For example, maple trees release so-called volatile organic compounds into the air to warn other plants of a herbivore attack. Most communication takes place between members of the same species. The reason is that its purpose is usually some form of cooperation, which is not as common between different species. Interspecies communication happens mainly in cases of symbiotic relationships. For instance, many flowers use symmetrical shapes and distinctive colors to signal to insects where nectar is located. Humans engage in interspecies communication when interacting with pets and working animals.\n\nHuman communication has a long history and how people exchange information has evolved over time. These changes were usually triggered by the development of new communication technologies. Examples are the invention of writing systems, the development of mass printing, the use of radio and television, and the invention of the internet. The technological advances also led to new forms of communication, such as the exchange of data between computers.\n\nDefinitions\n\nThe word communication has its root in the Latin verb communicare, which means 'to share' or 'to make common'. Communication is usually understood as the transmission of information: a message is conveyed from a sender to a receiver using some medium, such as sound, written signs, bodily movements, or electricity. Sender and receiver are often distinct individuals but it is also possible for an individual to communicate with themselves. In some cases, sender and receiver are not individuals but groups like organizations, social classes, or nations. In a different sense, the term communication refers to the message that is being communicated or to the field of inquiry studying communicational phenomena.\n\nThe precise characterization of communication is disputed. Many scholars have raised doubts that any single definition can capture the term accurately. These difficulties come from the fact that the term is applied to diverse phenomena in different contexts, often with slightly different meanings. The issue of the right definition affects the research process on many levels. This includes issues like which empirical phenomena are observed, how they are categorized, which hypotheses and laws are formulated as well as how systematic theories based on these steps are articulated.\n\nSome definitions are broad and encompass unconscious and non-human behavior. Under a broad definition, many animals communicate within their own species and flowers communicate by signaling the location of nectar to bees through their colors and shapes. Other definitions restrict communication to conscious interactions among human beings. Some approaches focus on the use of symbols and signs while others stress the role of understanding, interaction, power, or transmission of ideas. Various characterizations see the communicator's intent to send a message as a central component. In this view, the transmission of information is not sufficient for communication if it happens unintentionally. A version of this view is given by philosopher Paul Grice, who identifies communication with actions that aim to make the recipient aware of the communicator's intention. One question in this regard is whether only successful transmissions of information should be regarded as communication. For example, distortion may interfere with and change the actual message from what was originally intended. A closely related problem is whether acts of deliberate deception constitute communication.\n\nAccording to a broad definition by literary critic I. A. Richards, communication happens when one mind acts upon its environment to transmit its own experience to another mind. Another interpretation is given by communication theorists Claude Shannon and Warren Weaver, who characterize communication as a transmission of information brought about by the interaction of several components, such as a source, a message, an encoder, a channel, a decoder, and a receiver. The transmission view is rejected by transactional and constitutive views, which hold that communication is not just about the transmission of information but also about the creation of meaning. Transactional and constitutive perspectives hold that communication shapes the participant's experience by conceptualizing the world and making sense of their environment and themselves. Researchers studying animal and plant communication focus less on meaning-making. Instead, they often define communicative behavior as having other features, such as playing a beneficial role in survival and reproduction, or having an observable response.\n\nModels of communication\n\nModels of communication are conceptual representations of the process of communication. Their goal is to provide a simplified overview of its main components. This makes it easier for researchers to formulate hypotheses, apply communication-related concepts to real-world cases, and test predictions. Due to their simplified presentation, they may lack the conceptual complexity needed for a comprehensive understanding of all the essential aspects of communication. They are usually presented visually in the form of diagrams showing the basic components and their interaction.\n\nModels of communication are often categorized based on their intended applications and how they conceptualize communication. Some models are general in the sense that they are intended for all forms of communication. Specialized models aim to describe specific forms, such as models of mass communication.\n\nOne influential way to classify communication is to distinguish between linear transmission, interaction, and transaction models. Linear transmission models focus on how a sender transmits information to a receiver. They are linear because this flow of information only goes in a single direction. This view is rejected by interaction models, which include a feedback loop. Feedback is needed to describe many forms of communication, such as a conversation, where the listener may respond to a speaker by expressing their opinion or by asking for clarification. Interaction models represent the process as a form of two-way communication in which the communicators take turns sending and receiving messages. Transaction models further refine this picture by allowing representations of sending and responding at the same time. This modification is needed to describe how the listener can give feedback in a face-to-face conversation while the other person is talking. Examples are non-verbal feedback through body posture and facial expression. Transaction models also hold that meaning is produced during communication and does not exist independently of it.\n\nAll the early models, developed in the middle of the 20th century, are linear transmission models. Lasswell's model, for example, is based on five fundamental questions: \"Who?\", \"Says what?\", \"In which channel?\", \"To whom?\", and \"With what effect?\". The goal of these questions is to identify the basic components involved in the communicative process: the sender, the message, the channel, the receiver, and the effect. Lasswell's model was initially only conceived as a model of mass communication, but it has been applied to other fields as well. Some communication theorists, like Richard Braddock, have expanded it by including additional questions, like \"Under what circumstances?\" and \"For what purpose?\".\n\nThe Shannon–Weaver model is another influential linear transmission model. It is based on the idea that a source creates a message, which is then translated into a signal by a transmitter. Noise may interfere with and distort the signal. Once the signal reaches the receiver, it is translated back into a message and made available to the destination. For a landline telephone call, the person calling is the source and their telephone is the transmitter. The transmitter translates the message into an electrical signal that travels through the wire, which acts as the channel. The person taking the call is the destination and their telephone is the receiver. The Shannon–Weaver model includes an in-depth discussion of how noise can distort the signal and how successful communication can be achieved despite noise. This can happen by making the message partially redundant so that decoding is possible nonetheless. Other influential linear transmission models include Gerbner's model and Berlo's model.\n\nThe earliest interaction model was developed by communication theorist Wilbur Schramm. He states that communication starts when a source has an idea and expresses it in the form of a message. This process is called encoding and happens using a code, i.e. a sign system that is able to express the idea, for instance, through visual or auditory signs. The message is sent to a destination, who has to decode and interpret it to understand it. In response, they formulate their own idea, encode it into a message, and send it back as a form of feedback. Another innovation of Schramm's model is that previous experience is necessary to be able to encode and decode messages. For communication to be successful, the fields of experience of source and destination have to overlap.\n\nThe first transactional model was proposed by communication theorist Dean Barnlund in 1970. He understands communication as \"the production of meaning, rather than the production of messages\". Its goal is to decrease uncertainty and arrive at a shared understanding. This happens in response to external and internal cues. Decoding is the process of ascribing meaning to them and encoding consists in producing new behavioral cues as a response.\n\nHuman\n\nThere are many forms of human communication. A central distinction is whether language is used, as in the contrast between verbal and non-verbal communication. A further distinction concerns whether one communicates with others or with oneself, as in the contrast between interpersonal and intrapersonal communication. Forms of human communication are also categorized by their channel or the medium used to transmit messages. The field studying human communication is known as anthroposemiotics.\n\nVerbal\n\nVerbal communication is the exchange of messages in linguistic form, i.e., by means of language. In colloquial usage, verbal communication is sometimes restricted to oral communication and may exclude writing and sign language. However, in academic discourse, the term is usually used in a wider sense, encompassing any form of linguistic communication, whether through speech, writing, or gestures. Some of the challenges in distinguishing verbal from non-verbal communication come from the difficulties in defining what exactly language means. Language is usually understood as a conventional system of symbols and rules used for communication. Such systems are based on a set of simple units of meaning that can be combined to express more complex ideas. The rules for combining the units into compound expressions are called grammar. Words are combined to form sentences.\n\nOne hallmark of human language, in contrast to animal communication, lies in its complexity and expressive power. Human language can be used to refer not just to concrete objects in the here-and-now but also to spatially and temporally distant objects and to abstract ideas. Humans have a natural tendency to acquire their native language in childhood. They are also able to learn other languages later in life as second languages. However, this process is less intuitive and often does not result in the same level of linguistic competence. The academic discipline studying language is called linguistics. Its subfields include semantics (the study of meaning), morphology (the study of word formation), syntax (the study of sentence structure), pragmatics (the study of language use), and phonetics (the study of basic sounds).\n\nA central contrast among languages is between natural and artificial or constructed languages. Natural languages, like English, Spanish, and Japanese, developed naturally and for the most part unplanned in the course of history. Artificial languages, like Esperanto, Quenya, C++, and the language of first-order logic, are purposefully designed from the ground up. Most everyday verbal communication happens using natural languages. Central forms of verbal communication are speech and writing together with their counterparts of listening and reading. Spoken languages use sounds to produce signs and transmit meaning while for writing, the signs are physically inscribed on a surface. Sign languages, like American Sign Language and Nicaraguan Sign Language, are another form of verbal communication. They rely on visual means, mostly by using gestures with hands and arms, to form sentences and convey meaning.\n\nVerbal communication serves various functions. One key function is to exchange information, i.e. an attempt by the speaker to make the audience aware of something, usually of an external event. But language can also be used to express the speaker's feelings and attitudes. A closely related role is to establish and maintain social relations with other people. Verbal communication is also used to coordinate one's behavior with others and influence them. In some cases, language is not employed for an external purpose but only for entertainment or personal enjoyment. Verbal communication further helps individuals conceptualize the world around them and themselves. This affects how perceptions of external events are interpreted, how things are categorized, and how ideas are organized and related to each other.\n\nNon-verbal\n\nNon-verbal communication is the exchange of information through non-linguistic modes, like facial expressions, gestures, and postures. However, not every form of non-verbal behavior constitutes non-verbal communication. Some theorists, like Judee Burgoon, hold that it depends on the existence of a socially shared coding system that is used to interpret the meaning of non-verbal behavior. Non-verbal communication has many functions. It frequently contains information about emotions, attitudes, personality, interpersonal relations, and private thoughts.\n\nNon-verbal communication often happens unintentionally and unconsciously, like sweating or blushing, but there are also conscious intentional forms, like shaking hands or raising a thumb. It often happens simultaneously with verbal communication and helps optimize the exchange through emphasis and illustration or by adding additional information. Non-verbal cues can clarify the intent behind a verbal message. Using multiple modalities of communication in this way usually makes communication more effective if the messages of each modality are consistent. However, in some cases different modalities can contain conflicting messages. For example, a person may verbally agree with a statement but press their lips together, thereby indicating disagreement non-verbally.\n\nThere are many forms of non-verbal communication. They include kinesics, proxemics, haptics, paralanguage, chronemics, and physical appearance. Kinesics studies the role of bodily behavior in conveying information. It is commonly referred to as body language, even though it is, strictly speaking, not a language but rather non-verbal communication. It includes many forms, like gestures, postures, walking styles, and dance. Facial expressions, like laughing, smiling, and frowning, all belong to kinesics and are expressive and flexible forms of communication. Oculesics is another subcategory of kinesics in regard to the eyes. It covers questions like how eye contact, gaze, blink rate, and pupil dilation form part of communication. Some kinesic patterns are inborn and involuntary, like blinking, while others are learned and voluntary, like giving a military salute.\n\nProxemics studies how personal space is used in communication. The distance between the speakers reflects their degree of familiarity and intimacy with each other as well as their social status. Haptics examines how information is conveyed using touching behavior, like handshakes, holding hands, kissing, or slapping. Meanings linked to haptics include care, concern, anger, and violence. For instance, handshaking is often seen as a symbol of equality and fairness, while refusing to shake hands can indicate aggressiveness. Kissing is another form often used to show affection and erotic closeness.\n\nParalanguage, also known as vocalics, encompasses non-verbal elements in speech that convey information. Paralanguage is often used to express the feelings and emotions that the speaker has but does not explicitly state in the verbal part of the message. It is not concerned with the words used but with how they are expressed. This includes elements like articulation, lip control, rhythm, intensity, pitch, fluency, and loudness. For example, saying something loudly and in a high pitch conveys a different meaning on the non-verbal level than whispering the same words. Paralanguage is mainly concerned with spoken language but also includes aspects of written language, like the use of colors and fonts as well as spatial arrangement in paragraphs and tables. Non-linguistic sounds may also convey information; crying indicates that an infant is distressed, and babbling conveys information about infant health and well-being.\n\nChronemics concerns the use of time, such as what messages are sent by being on time versus late for a meeting. The physical appearance of the communicator, such as height, weight, hair, skin color, gender, clothing, tattooing, and piercing, also carries information. Appearance is an important factor for first impressions but is more limited as a mode of communication since it is less changeable. Some forms of non-verbal communication happen using such artifacts as drums, smoke, batons, traffic lights, and flags.\n\nNon-verbal communication can also happen through visual media like paintings and drawings. They can express what a person or an object looks like and can also convey other ideas and emotions. In some cases, this type of non-verbal communication is used in combination with verbal communication, for example, when diagrams or maps employ labels to include additional linguistic information.\n\nTraditionally, most research focused on verbal communication. However, this paradigm began to shift in the 1950s when research interest in non-verbal communication increased and emphasized its influence. For example, many judgments about the nature and behavior of other people"
 },
 {
  "title": "Communication (Hitomi Takahashi song)",
  "revision_id": "1350315297",
  "matched_by": "redirect",
  "text": "\"Communication\" is Hitomi Takahashi's 4th single under the Sony Records (gr8! records) label. The single was released in only one format on July 12, 2006, nearly eight months after her last single Aozora no NAMIDA.\n\nOverview\n\n\"Communication (コミュニケイション, Komyunikeishon)\" is Hitomi's fourth single, and, as of now, is her least successful single. \"Communication\", the a-side, was being used as the ending theme song for the Japanese TV show \"MUSIC FIGHTER\" during the month of July 2006. Like her past single \"evergreen\", this single has failed to enter the Daily Top 20 on the Oricon Charts and even failed to enter the Weekly Top 30, its position being a weak #60. Most fans blame this on the lack of promotion Sony gave this single; an example being that there were no TV performances. However, it ranked #6 on the \"This Week's Sony Music, CD Chart! Best 10!!!\" for the week of 7/10~7/16.\n\nThis single marks Takahashi's beginning partnership with ex-Judy and Mary member Takuya, who produced and arranged the first two tracks on the single. The 3rd track is a cover of the song that was originally sung by the Magokoro Brothers. The entire single is described as a \"new breed rock\", which includes the genres of rock, emo, punk, and reggae. Lyrically, the a-side song deals with the notion that communication is extremely important in any kind of relationship, hence the title \"Communication\". The musical aspect of the song showcases Takahashi's quick change from singing pop/rock music to punk/rock music.\n\nSample of the translated lyrics:\n\nI want to laugh with you, I want to trust you, and I don't care if it hurts\n\nI want to understand you more - I can't hold back this communication\n\nIt's not enough, everything's not enough, I want to keep going\n\nAs I take the first step, the scenery changes, just start the communication\n\nMusic video\n\n The PV, promotional video, for \"Communication\" aired on the channel MO-N SAKIDORI on June 29, 2006, at midnight. Like her last two PVs, this PV was directed by AT, and was filmed at Saitama University. In this PV, which is much more simple than her previous PVs, both Hitomi and her band are showcased in a white room with glass windows in the background. The first half of the PV has Hitomi singing in front of a microphone with large speakers behind her; the camera is constantly switching its view on Hitomi. The next half of the PV shows Hitomi singing around many light bulbs, with the band playing behind her. From there, the PV switches scenes from the white room to the darkroom with light bulbs surrounding Hitomi.\n\nTrack listing\n\n\"Communication (コミュニケイション)\" - 5:14 Lyrics by Hitomi Takahashi & Akiko Watanabe Music and arrangement by Takuya \n\n\"sunshine\" - 5:15 Lyrics by April pool Music and arrangement by Takuya \n\n\"Subarashiki Kono Sekai (素晴らしきこの世界)\" - 7:18 Lyrics and music by Youichi Kuramochi Arrangement by Koji Igarashi \n\n\"コミュニケイション -Instrumental-\" - 5:14\n\nPersonnel\n\nHitomi Takahashi - vocals (All tracks) & harp (Track #3)\n\nTAKUYA - guitars (Tracks #1 & #2)\n\nKoji Igarashi - keyboards (Tracks #1, #2, & #3)\n\nNinji - bass (Track #1)\n\nTakashi Furuta - drums (Tracks #1 & #2)\n\nHiroshi Udagawa - bass (Track #2)\n\nKazuyoshi Baba - guitars (Track #3)\n\nMichitarou - bass (Track #3)\n\nKeiji Masuoka - drums (Track #3)\n\nProduction\n\nProducer - TAKUYA\n\nDirectors - Kazuma Jo, Taku Sugawara\n\nA&R - Naoki Yoshitake\n\nA&R Chief - Takashi Nakamura\n\nCharts\n\nOricon Sales Chart (Japan)\n\nReferences"
 },
 {
  "title": "Communication (Karl Bartos album)",
  "revision_id": "1378914490",
  "matched_by": "title-minus-qualifier",
  "text": "Communication released in 2003, is the first solo album of German electronic musician Karl Bartos.\n\nAccording to Karl Bartos, the album is a concept album about electronic media: \n»Communication« is about the way images shape our view of the world and how electronic media is going to change the contents of our culture\"\n— Karl Bartos in 2003, \n\nRelease\n\nSome editions of the CD come in a special Burgopak-Case, which is unusual in that the CD tray and booklet both emerge sliding out from opposite sides of the case and must be opened together.\n\nThe limited edition was issued as CD Extra and contains the video clip for \"I'm the Message\" as well as a download link for two remixes of the song by Felix Da Housecat and Orbital.\n\nThe album was re-released on March 25, 2016, on CD and Vinyl, including remastered tracks and the bonus song \"Camera Obscura\".\n\nReception\n\nSean Carruthers of AllMusic likened Communication to the mid-1980s electro-pop of Orchestral Manoeuvres in the Dark and the Pet Shop Boys, adding that \"It would be easy to dismiss the album if it weren't so catchy: no matter how cheeseball and dated a lot of the material here sounds, it sticks in your head.\"\n\nTrack listing\n\nAll tracks are written by Karl Bartos, except where noted.\n\nPersonnel\n\nKarl Bartos – production, vocals, electronic instruments\n\nMathias Black – mixing, mastering\n\nCharts\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q11024",
  "label": "communication",
  "description": "act of conveying intended meaning",
  "aliases": [
   "expression",
   "expressing",
   "to express",
   "transmition of a message"
  ],
  "claims": {
   "P31": [
    "Q1413287",
    "Q921513",
    "Q116505632",
    "Q123345464",
    "Q11862829"
   ],
   "P279": [
    "Q6031064",
    "Q52948",
    "Q141344358"
   ],
   "P361": [
    "Q451967",
    "Q2305441"
   ],
   "P527": [
    "Q1066689",
    "Q1434121"
   ]
  },
  "revision_id": "2571689743",
  "value_labels": {
   "Q1413287": "social skill",
   "Q921513": "social behavior",
   "Q116505632": "type of process",
   "Q123345464": "type of interaction",
   "Q11862829": "academic discipline",
   "Q6031064": "information exchange",
   "Q52948": "interaction",
   "Q141344358": "planned act",
   "Q451967": "intentional human activity",
   "Q2305441": "social process",
   "Q1066689": "human communication",
   "Q1434121": "animal communication"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5154085",
  "label": "Communication",
  "description": "single",
  "aliases": [],
  "claims": {
   "P31": [
    "Q134556"
   ]
  },
  "revision_id": "2481312634",
  "value_labels": {
   "Q134556": "single"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1121530",
  "label": "Communication",
  "description": "2003 studio album by Karl Bartos",
  "aliases": [],
  "claims": {
   "P31": [
    "Q482994"
   ],
   "P361": [
    "Q113500566"
   ]
  },
  "revision_id": "2206291884",
  "value_labels": {
   "Q482994": "album",
   "Q113500566": "Karl Bartos's albums in chronological order"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1413287",
  "label": "social skill",
  "description": "any competence facilitating interaction and communication with others where social rules and relations are created, communicated, and changed in verbal and nonverbal ways",
  "aliases": [
   "interpersonal skill"
  ],
  "claims": {
   "P31": [
    "Q2015382"
   ],
   "P279": [
    "Q205961",
    "Q527091"
   ],
   "P361": [
    "Q77468620"
   ]
  },
  "revision_id": "2551948850",
  "ancestor_of": "Q11024",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q921513",
  "label": "social behavior",
  "description": "behavior among two or more organisms, typically from the same species",
  "aliases": [
   "social behaviour",
   "сollective behavior",
   "demeanor"
  ],
  "claims": {
   "P31": [
    "Q2996394"
   ],
   "P279": [
    "Q2990593",
    "Q22294683",
    "Q2305441"
   ],
   "P361": [
    "Q77468620"
   ],
   "P527": [
    "Q106667104",
    "Q610757",
    "Q3733713"
   ]
  },
  "revision_id": "2556398585",
  "ancestor_of": "Q11024",
  "level": 1,
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
  "ancestor_of": "Q11024",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q123345464",
  "label": "type of interaction",
  "description": "Wikidata metaclass for interaction in various contexts",
  "aliases": [],
  "claims": {
   "P31": [
    "Q19478619",
    "Q24017414"
   ],
   "P279": [
    "Q116505632"
   ]
  },
  "revision_id": "2551511463",
  "ancestor_of": "Q11024",
  "level": 1,
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
  "ancestor_of": "Q11024",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q6031064",
  "label": "information exchange",
  "description": "transfer of information between entities",
  "aliases": [
   "exchange of information",
   "information sharing",
   "Communication Networks",
   "communication"
  ],
  "claims": {
   "P31": [
    "Q123345464"
   ],
   "P279": [
    "Q125506646"
   ]
  },
  "revision_id": "2552838796",
  "ancestor_of": "Q11024",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q52948",
  "label": "interaction",
  "description": "kind of action that occurs as two or more objects have an effect upon one another",
  "aliases": [
   "interacting"
  ],
  "claims": {
   "P31": [
    "Q33104279",
    "Q116505632"
   ],
   "P279": [
    "Q3249551",
    "Q141641947"
   ],
   "P361": [
    "Q58778",
    "Q930933",
    "Q111931734"
   ],
   "P1889": [
    "Q352720",
    "Q118193027",
    "Q141134051",
    "Q11083766",
    "Q141000779",
    "Q1665869"
   ]
  },
  "revision_id": "2556555775",
  "ancestor_of": "Q11024",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q141344358",
  "label": "planned act",
  "description": "act in which at least one agent plays a causative role and which is prescribed by some directive information content entity held by at least one of the agents",
  "aliases": [
   "intentional act"
  ],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q141336142",
    "Q104637332",
    "Q141751569"
   ]
  },
  "revision_id": "2569961428",
  "ancestor_of": "Q11024",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2015382",
  "label": "competence",
  "description": "set of demonstrable characteristics and skills that enable, and improve the efficiency or performance of a job",
  "aliases": [
   "job competency",
   "competence"
  ],
  "claims": {
   "P279": [
    "Q527091"
   ],
   "P361": [
    "Q5467169"
   ]
  },
  "revision_id": "2556596246",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q205961",
  "label": "skill",
  "description": "learned ability and competence to carry out an action",
  "aliases": [
   "athletic ability"
  ],
  "claims": {
   "P31": [
    "Q110403031"
   ],
   "P279": [
    "Q1347367",
    "Q9081"
   ],
   "P527": [
    "Q7535186",
    "Q15910354",
    "Q2480597"
   ],
   "P460": [
    "Q460693",
    "Q1813993",
    "Q7535186",
    "Q121788669"
   ],
   "P1889": [
    "Q21767554"
   ]
  },
  "revision_id": "2567571464",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q527091",
  "label": "competence",
  "description": "ability and skill to solve problems and a willingness to do so",
  "aliases": [
   "competence (education)",
   "key competence"
  ],
  "claims": {
   "P31": [
    "Q151885"
   ],
   "P279": [
    "Q205961",
    "Q5034466"
   ]
  },
  "revision_id": "2535348068",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2996394",
  "label": "biological process",
  "description": "process specifically pertinent to the functioning of integrated living units",
  "aliases": [
   "life processes",
   "physiological process",
   "single-organism process",
   "single organism process",
   "biological processes",
   "biological process class",
   "class of biological process",
   "biological phenomenon",
   "biological phenomena"
  ],
  "claims": {
   "P31": [
    "Q116505632",
    "Q151885"
   ],
   "P279": [
    "Q64732777",
    "Q17320256",
    "Q141435481",
    "Q13878858"
   ],
   "P361": [
    "Q30336093"
   ],
   "P527": [
    "Q1823478",
    "Q22299142"
   ],
   "P1889": [
    "Q104637332"
   ]
  },
  "revision_id": "2557488341",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2990593",
  "label": "animal behavior",
  "description": "internally coordinated responses (actions or inactions) of animals (individuals or groups) to internal or external stimuli, via a mechanism that involves nervous system activity",
  "aliases": [
   "animal behaviour",
   "behavioural response to stimulus",
   "behaviour",
   "Behavior, Animal",
   "behavioral response to stimulus",
   "single-organism behavior"
  ],
  "claims": {
   "P31": [
    "Q2267705",
    "Q1047113",
    "Q4671286"
   ],
   "P279": [
    "Q9332",
    "Q22299433"
   ],
   "P1889": [
    "Q3769299"
   ]
  },
  "revision_id": "2551658035",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q22294683",
  "label": "biological process involved in intraspecies interaction between organisms",
  "description": "process in which an organism has an effect on an organism of the same species",
  "aliases": [
   "GO:0051703",
   "intraspecies interaction with other organisms",
   "intraspecies interaction between organisms"
  ],
  "claims": {
   "P31": [
    "Q2996394"
   ],
   "P279": [
    "Q22269697",
    "Q2996394"
   ]
  },
  "revision_id": "2481775811",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2305441",
  "label": "social process",
  "description": "way of interaction between individuals and groups",
  "aliases": [
   "interpersonal process"
  ],
  "claims": {
   "P31": [
    "Q116505632"
   ],
   "P279": [
    "Q3249551",
    "Q483247"
   ],
   "P527": [
    "Q11024"
   ]
  },
  "revision_id": "2565172817",
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q19478619",
  "label": "metaclass",
  "description": "class which has instances that are all themselves classes",
  "aliases": [
   "Wikidata metaclass",
   "Wikidata metaclasses"
  ],
  "claims": {
   "P31": [
    "Q151885",
    "Q19868531",
    "Q115490628"
   ],
   "P279": [
    "Q16889133"
   ],
   "P361": [
    "Q324254"
   ],
   "P1889": [
    "Q19828331",
    "Q123369568",
    "Q1924819",
    "Q24017414"
   ]
  },
  "revision_id": "2559895276",
  "ancestor_of": "Q11024",
  "level": 2,
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
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q142077035",
  "label": "type of perdurant",
  "description": "instances are classes of perdurant",
  "aliases": [
   "perdurant type",
   "event universal",
   "gufo:EventType",
   "ufo:PerdurantType"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q141439648"
   ],
   "P1889": [
    "Q141750103",
    "Q108586636"
   ]
  },
  "revision_id": "2570481579",
  "ancestor_of": "Q11024",
  "level": 2,
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
  "ancestor_of": "Q11024",
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
  "ancestor_of": "Q11024",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q134556",
  "label": "single",
  "description": "type of music release",
  "aliases": [
   "music single"
  ],
  "claims": {
   "P31": [
    "Q106043376"
   ],
   "P279": [
    "Q108346082",
    "Q7302866"
   ],
   "P527": [
    "Q108352496"
   ],
   "P1889": [
    "Q347210",
    "Q421718",
    "Q12776075",
    "Q110910355",
    "Q110910359",
    "Q908826"
   ]
  },
  "revision_id": "2557337424",
  "ancestor_of": "Q5154085",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106043376",
  "label": "music release type",
  "description": "Wikidata metaclass; type of music release",
  "aliases": [
   "type of music release",
   "music release form",
   "form of music release"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q1437361"
   ],
   "P279": [
    "Q16889133",
    "Q59913930"
   ]
  },
  "revision_id": "2547724282",
  "ancestor_of": "Q5154085",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q108346082",
  "label": "release group",
  "description": "group of similar audio releases typically of different formats (digital, CD, etc.)",
  "aliases": [
   "group of audio releases",
   "group of music releases",
   "master release"
  ],
  "claims": {
   "P279": [
    "Q16887380",
    "Q140007694"
   ],
   "P527": [
    "Q115669410"
   ]
  },
  "revision_id": "2552400352",
  "ancestor_of": "Q5154085",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7302866",
  "label": "audio track",
  "description": "track on an audio release",
  "aliases": [
   "record track",
   "CD track",
   "music track",
   "track audio",
   "track"
  ],
  "claims": {
   "P31": [
    "Q59913930"
   ],
   "P279": [
    "Q3302947",
    "Q17537576",
    "Q2188189",
    "Q140007694",
    "Q49017950",
    "Q115669410"
   ],
   "P361": [
    "Q482994",
    "Q134556",
    "Q169930",
    "Q2031291"
   ],
   "P460": [
    "Q134556",
    "Q7366"
   ],
   "P1889": [
    "Q351303",
    "Q141499417",
    "Q3302947",
    "Q2442307"
   ]
  },
  "revision_id": "2558882534",
  "ancestor_of": "Q5154085",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q482994",
  "label": "album",
  "description": "grouping of album releases by an artist usually released at the same time with the same title and tracks but in different formats for consumption (digital, CD, LP)",
  "aliases": [
   "audio album",
   "music album",
   "record album",
   "full album",
   "full-length album"
  ],
  "claims": {
   "P31": [
    "Q106043376"
   ],
   "P279": [
    "Q108346082"
   ],
   "P527": [
    "Q108352648",
    "Q141554387"
   ]
  },
  "revision_id": "2561514303",
  "ancestor_of": "Q1121530",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q106043376",
  "label": "music release type",
  "description": "Wikidata metaclass; type of music release",
  "aliases": [
   "type of music release",
   "music release form",
   "form of music release"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q1437361"
   ],
   "P279": [
    "Q16889133",
    "Q59913930"
   ]
  },
  "revision_id": "2547724282",
  "ancestor_of": "Q1121530",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q108346082",
  "label": "release group",
  "description": "group of similar audio releases typically of different formats (digital, CD, etc.)",
  "aliases": [
   "group of audio releases",
   "group of music releases",
   "master release"
  ],
  "claims": {
   "P279": [
    "Q16887380",
    "Q140007694"
   ],
   "P527": [
    "Q115669410"
   ]
  },
  "revision_id": "2552400352",
  "ancestor_of": "Q1121530",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-06262268-n",
  "lemmas": [
   "communication",
   "communicating"
  ],
  "gloss": "the activity of communicating; the activity of conveying information",
  "examples": [
   "they could not act without official communication from Moscow"
  ],
  "relations": {
   "hypernym": [
    "oewn-00030657-n"
   ],
   "hyponym": [
    "oewn-06261911-n",
    "oewn-06262873-n",
    "oewn-06264605-n",
    "oewn-06270774-n",
    "oewn-06275051-n",
    "oewn-07019235-n",
    "oewn-07152793-n",
    "oewn-07154408-n",
    "oewn-07154581-n",
    "oewn-07211681-n",
    "oewn-07259785-n",
    "oewn-07260346-n",
    "oewn-07261402-n",
    "oewn-07293990-n",
    "oewn-07294158-n"
   ]
  },
  "relation_targets": {
   "oewn-00030657-n": "act, deed, human action",
   "oewn-06261911-n": "transmission",
   "oewn-06262873-n": "intercommunication",
   "oewn-06264605-n": "medium",
   "oewn-06270774-n": "channel, communication channel, line",
   "oewn-06275051-n": "mail, mail service, postal service",
   "oewn-07019235-n": "dramaturgy, dramatic art, dramatics",
   "oewn-07152793-n": "discussion, treatment, discourse",
   "oewn-07154408-n": "exhortation",
   "oewn-07154581-n": "expression, verbal expression, verbalism",
   "oewn-07211681-n": "examination, exam, test",
   "oewn-07259785-n": "persuasion, suasion",
   "oewn-07260346-n": "dissuasion",
   "oewn-07261402-n": "expostulation, remonstrance, remonstration",
   "oewn-07293990-n": "contact, touch",
   "oewn-07294158-n": "traffic"
  }
 },
 {
  "synset": "oewn-00033319-n",
  "lemmas": [
   "communication"
  ],
  "gloss": "something that is communicated by or to or between people or groups",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-00002137-n"
   ],
   "hyponym": [
    "oewn-06263820-n",
    "oewn-06293036-n",
    "oewn-06293304-n",
    "oewn-06360590-n",
    "oewn-06611268-n",
    "oewn-06612774-n",
    "oewn-06804229-n",
    "oewn-06806088-n",
    "oewn-06810027-n",
    "oewn-06886302-n",
    "oewn-06900776-n",
    "oewn-07080699-n",
    "oewn-07096217-n",
    "oewn-07123727-n",
    "oewn-07125323-n",
    "oewn-07270459-n",
    "oewn-07292402-n",
    "oewn-13424504-n",
    "oewn-01104341-n"
   ]
  },
  "relation_targets": {
   "oewn-00002137-n": "abstraction, abstract entity",
   "oewn-06263820-n": "message",
   "oewn-06293036-n": "contagion, infection",
   "oewn-06293304-n": "language, linguistic communication",
   "oewn-06360590-n": "written communication, written language, black and white",
   "oewn-06611268-n": "message, content, subject matter",
   "oewn-06612774-n": "didacticism",
   "oewn-06804229-n": "signal, signaling, sign",
   "oewn-06806088-n": "sign",
   "oewn-06810027-n": "indication, indicant",
   "oewn-06886302-n": "visual communication",
   "oewn-06900776-n": "display",
   "oewn-07080699-n": "expressive style, style",
   "oewn-07096217-n": "paralanguage, paralinguistic communication",
   "oewn-07123727-n": "auditory communication",
   "oewn-07125323-n": "voice, vocalization, vocalisation",
   "oewn-07270459-n": "psychic communication, psychical communication, anomalous communication",
   "oewn-07292402-n": "voice",
   "oewn-13424504-n": "document",
   "oewn-01104341-n": "publication"
  }
 },
 {
  "synset": "oewn-13815054-n",
  "lemmas": [
   "communication"
  ],
  "gloss": "a connection allowing access between persons or places",
  "examples": [
   "how many lines of communication can there be among four people?",
   "a secret passageway provided communication between the two rooms"
  ],
  "relations": {
   "hypernym": [
    "oewn-13813601-n"
   ],
   "hyponym": [
    "oewn-90000051-n"
   ]
  },
  "relation_targets": {
   "oewn-13813601-n": "connection, connexion, connectedness",
   "oewn-90000051-n": "Twitter"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~
