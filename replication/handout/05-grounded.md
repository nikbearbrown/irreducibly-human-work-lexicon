# Skills Lexicon pilot, grounded run: message 6 of 13 (chunk 05, 2 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "05", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-05.jsonl`. Otherwise send one code block marked `jsonl` holding the 2 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 2: R (`oeixkjthc3`)

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
[
 {
  "title": "R",
  "revision_id": "1377492700",
  "matched_by": "title",
  "text": "R (minuscule: r) is the eighteenth letter of the Latin alphabet, used in the modern English alphabet, the alphabets of other western European languages and others worldwide. Its name in English is ar (pronounced /ˈɑːr/ ), plural ars.\n\nThe letter ⟨r⟩ is the eighth most common letter in English and the fourth-most common consonant, after ⟨t⟩, ⟨n⟩, and ⟨s⟩.\n\nName\n\nThe name of the letter in Latin was er (/ɛr/), following the pattern of other letters representing continuants, such as ⟨F⟩, ⟨L⟩, ⟨M⟩, ⟨N⟩, and ⟨S⟩. This name is preserved in French and many other languages. In Middle English, the name of the letter changed from /ɛr/ to /ar/, following a pattern exhibited in many other words such as farm (compare French ferme) and star (compare German Stern).\n\nIn Hiberno-English, the letter is called /ɒr/ or /ɔːr/, somewhat similar to oar, ore, orr.\n\nThe letter ⟨R⟩ is sometimes referred to as the littera canīna 'canine letter', often rendered in English as the dog's letter. This Latin term referred to the Latin ⟨R⟩ that was trilled to sound like a growling dog, a spoken style referred to as vōx canīna 'dog voice' (e.g. in Spanish perro 'dog').\n\nHistory\n\nAntiquity\n\nThe letter ⟨R⟩ is believed to derive ultimately from an image of a head, used in Semitic alphabets for the sound /r/ because the word for 'head' was rêš or similar in most Semitic languages. The word became the name of the letter, as an example of acrophony.\n\nIt developed into Greek ⟨Ρ⟩ ῥῶ (rhô) and Latin ⟨R⟩. The descending diagonal stroke develops as a graphic variant in some Western Greek alphabets (writing rho as ⟨⟩), but it was not adopted in most Old Italic alphabets; most Old Italic alphabets show variants of their rho between a ⟨P⟩ and a ⟨D⟩ shape, but without the Western Greek descending stroke.\nIndeed, the oldest known forms of the Latin alphabet itself of the 7th to 6th centuries BC, in the Duenos and the Forum inscription, still write ⟨r⟩ using the ⟨P⟩ shape of the letter.\nThe Lapis Satricanus inscription shows the form of the Latin alphabet around 500 BC. Here, the rounded, closing ⟨Π⟩ shape of the ⟨p⟩ and the ⟨Ρ⟩ shape of the ⟨r⟩ have become difficult to distinguish.\nThe descending stroke of the Latin letter ⟨R⟩ has fully developed by the 3rd century BC, as seen in the Tomb of the Scipios sarcophagus inscriptions of that era. From c. 50 AD, the letter ⟨P⟩ would be written with its loop fully closed, assuming the shape formerly taken by ⟨R⟩.\n\nCursive\n\nThe minuscule form ⟨r⟩ developed through several variations on the capital form.\nAlong with Latin minuscule writing in general, it developed ultimately from Roman cursive via the uncial script of Late Antiquity into the Carolingian minuscule of the 9th century.\n\nIn handwriting, it was common not to close the bottom of the loop but continue into the leg, saving an extra pen stroke. The loop-leg stroke shortened into the simple arc used in the Carolingian minuscule and until today.\n\nA calligraphic minuscule ⟨r⟩, known as r rotunda ⟨ꝛ⟩, was used in the sequence ⟨or⟩, bending the shape of the ⟨r⟩ to accommodate the bulge of the ⟨o⟩ as in ⟨oꝛ⟩, as opposed to ⟨or⟩. Later, the same variant was also used where ⟨r⟩ followed other lower case letters with a rounded loop towards the right, such as with ⟨b⟩, ⟨h⟩, ⟨p⟩, as well as to write the geminate ⟨rr⟩ as ⟨ꝛꝛ⟩. Use of r rotunda was mostly tied to blackletter typefaces, and the glyph fell out of use along with blackletter fonts in English language contexts mostly by the 18th century.\n\nInsular script used a minuscule which retained two downward strokes, but which did not close the loop, known as the Insular r ⟨ꞃ⟩; this variant survives in the Gaelic type popular in Ireland until the mid-20th century, but has become largely limited to a decorative function.\n\nUse in writing systems\n\nEnglish\n\n⟨R⟩ represents a rhotic consonant in English, such as the alveolar approximant (most varieties), alveolar trill (some British varieties), or the retroflex approximant (some varieties in the United States, South West England and Dublin).\n\nIn non-rhotic accents, it is not pronounced in certain positions, but can affect the pronunciation of the vowel that precedes it.\n\nR is the ninth most frequently used letter in the English language.\n\nOther languages\n\n⟨R⟩ represents a rhotic consonant in many languages, as shown in the table below.\n\nOther languages may use the letter ⟨r⟩ in their alphabets (or Latin transliteration schemes) to represent rhotic consonants different from the alveolar trill. In Haitian Creole, it represents a sound so weak that it is often written interchangeably with ⟨w⟩, e.g. 'Kweyol' for 'Kreyol'.\n\nThe doubled ⟨rr⟩ represents a trilled /r/ in Albanian, Aragonese, Asturian, Basque, Catalan and Spanish.\n\nBrazilian Portuguese has a great number of allophones of /ʁ/, such as [χ], [h], [ɦ], [x], [ɣ], [ɹ] and [r]. The latter three ones can be used only in certain contexts ([ɣ] and [r] as ⟨rr⟩; [ɹ] in the syllable coda, as an allophone of /ɾ/ according to the European Portuguese norm and /ʁ/ according to the Brazilian Portuguese norm). Usually at least two of them are present in a single dialect, such as Rio de Janeiro's [ʁ], [χ], [ɦ] and, for a few speakers, [ɣ].\n\nOther systems\n\nThe International Phonetic Alphabet uses several variations of the letter to represent the different rhotic consonants; ⟨r⟩ represents the alveolar trill.\n\nOther uses\n\nAn R rating of the Motion Picture Association film rating system denotes media, such as movies, that are intended for a restricted audience.\n\nRelated characters\n\nDescendants and related characters in the Latin alphabet\n\nR with diacritics: Ŕ ŕ Ɍ ɍ Ř ř Ŗ ŗ Ṙ ṙ Ȑ ȑ Ȓ ȓ Ṛ ṛ Ṝ ṝ Ṟ ṟ Ꞧ ꞧ Ɽ ɽ R̃ r̃ ᵲ ꭨ ᵳ ᶉ\n\nInternational Phonetic Alphabet-specific symbols related to R: 𝼈 ɹ ɺ ɾ ɻ ɽ ʀ ʁ ʶ ˞ ʴ\n\nIPA superscript letters: 𐞦 𐞧 𐞨 𐞩 𐞪\n\nObsolete and nonstandard symbols in the International Phonetic Alphabet: ɼ ɿ\n\nUralic Phonetic Alphabet-specific symbols related to R:\n\nU+1D19 ᴙ LATIN LETTER SMALL CAPITAL REVERSED R\n\nU+1D1A ᴚ LATIN LETTER SMALL CAPITAL TURNED R\n\nU+1D3F ᴿ MODIFIER LETTER CAPITAL R\n\nU+1D63 ᵣ LATIN SUBSCRIPT SMALL LETTER R\n\nTeuthonista phonetic transcription-specific symbols related to R:\n\nU+AB45 ꭅ LATIN SMALL LETTER STIRRUP R\n\nU+AB46 ꭆ LATIN LETTER SMALL CAPITAL R WITH RIGHT LEG\n\nAnthropos phonetic transcription:\n\nU+AB48 ꭈ LATIN SMALL LETTER DOUBLE R\n\nU+AB49 ꭉ LATIN SMALL LETTER R WITH CROSSED-TAIL\n\nU+AB4A ꭊ LATIN SMALL LETTER DOUBLE R WITH CROSSED-TAIL\n\nOtto Bremer's phonetic transcription:\n\nU+AB47 ꭇ LATIN SMALL LETTER R WITHOUT HANDLE\n\nU+AB4B ꭋ LATIN SMALL LETTER SCRIPT R\n\nU+AB4C ꭌ LATIN SMALL LETTER SCRIPT R WITH RING\n\n𝼨 – ⟨R⟩ with mid-height left hook was used by the British and Foreign Bible Society in the early 20th century for romanization of the Malayalam language.\n\nⱹ – A turned ⟨r⟩ with a tail is used in the Swedish Dialect Alphabet\n\nRFE Phonetic Alphabet-specific symbols related to R:\n\nU+1DF57 𝽗 LATIN SMALL LETTER TURNED R WITH MID-HEIGHT LEFT HOOK\n\nU+1DFCD 𝿍 MODIFIER LETTER SMALL TURNED R WITH MID-HEIGHT LEFT HOOK\n\n𝽡 – An ⟨r⟩ with left tie was used in the 1960s and 1970s for the Initial Teaching Alphabet\n\nOther variations of R used for phonetic transcription: 𝼕 𝼖 ʳ ʵ\n\nCalligraphic variants in the Latin alphabet\n\nꝚ ꝛ – R rotunda\n\nꞂ ꞃ – Insular r (Gaelic type)\n\nᫍ – Combining Insular r, as used in the Ormulum\n\nAncestors and siblings in other alphabets\n\n𐤓 – Semitic letter Resh, from which the following letters derive:\n\nΡ ρ – Greek letter Rho, from which the following letters derive:\n\n𐌓 – Old Italic letter R, the ancestor of modern Latin ⟨R⟩\n\nᚱ – Runic letter Raido\n\nР р – Cyrillic letter Er\n\n𐍂 – Gothic letter Reda\n\n mouth, uniliteral R, possibly ancestral to Proto-Sinaitic Pe and its descendants.\n\nⵔ - Libyco-Berber letter R, from which the Tifinagh letter YAR derive.\n\nロ - Katakana letter RO\n\n口 - Chinese mouth, from which the Japanese kanji derive.\n\nAbbreviations, signs and symbols\n\n℟ – symbol for response in liturgy\n\n℞ – Medical prescription\n\n℞ꝵ (ꝶ, Ꝝꝝ) - Medievalist abbreviation for affixes -rum, -rom, re-\n\n® – Registered trademark symbol\n\n₹ – Indian rupee sign\n\n◌͛ (  ͛ ) - Medievalist contraction mark for ꝛ, er, ir\n\nOther representations\n\nComputing \n\nU+0052 R LATIN CAPITAL LETTER R\n\nU+0072 r LATIN SMALL LETTER R\n\nU+FF32 Ｒ FULLWIDTH LATIN CAPITAL LETTER R\n\nU+FF52 ｒ FULLWIDTH LATIN SMALL LETTER R\n\nThere are many precomposed character forms of the letter with various diacritics.\n\nOther\n\nSee also"
 },
 {
  "title": "R (programming language)",
  "revision_id": "1378604952",
  "matched_by": "title",
  "text": "R is a programming language for statistical computing and data visualization. It has been widely adopted in the fields of data mining, bioinformatics, data analysis, and data science.\n\nThe core R language is extended by a large number of software packages, which contain reusable code, documentation, and sample data. Some of the most popular R packages are in the tidyverse collection, which enhances functionality for visualizing, transforming, and modelling data, as well as improves the ease of programming (according to the authors and users).\n\nR is free and open-source software distributed under the GNU General Public License. The language is implemented primarily in C, Fortran, and R itself. Precompiled executables are available for the major operating systems (including Linux, MacOS, and Microsoft Windows).\n\nIts core is an interpreted language with a native command line interface. In addition, multiple third-party applications are available as graphical user interfaces; such applications include RStudio (an integrated development environment), Jupyter (a notebook interface), as well as Termux and Google Colab for mobile devices.\n\nHistory\n\nR was started by professors Ross Ihaka and Robert Gentleman as a programming language to teach introductory statistics at the University of Auckland. The language was inspired by the S programming language, with most S programs able to run unaltered in R. The language was also inspired by Scheme's lexical scoping, allowing for local variables.\n\nThe name of the language, R, comes from being both an S language successor and the shared first letter of the authors, Ross and Robert. In August 1993, Ihaka and Gentleman posted a binary file of R on StatLib — a data archive website. At the same time, they announced the posting on the s-news mailing list. On 5 December 1997, R became a GNU project when version 0.60 was released. On 29 February 2000, the 1.0 version was released.\n\nPackages\n\nR packages are collections of functions, documentation, and data that expand R. For example, packages can add reporting features (using packages such as R Markdown, Quarto, knitr, and Sweave) and support for various statistical techniques (such as linear, generalized linear and nonlinear modeling, classical statistical tests, spatial analysis, time-series analysis, and clustering). Ease of package installation and use have contributed to the language's adoption in data science.\n\nImmediately available when starting R after installation, base packages provide the fundamental and necessary syntax and commands for programming, computing, graphics production, basic arithmetic, and statistical functionality.\n\nAn example is the MASS package, which bundles functions and datasets to support the textbook Modern Applied Statistics with S by Venables and Ripley.\n\nInstalling a package occurs only once. For example, to install the MASS package:\n\n> install.packages(\"MASS\")\n\nTo load the functions, data, and documentation of a package, one calls the library() function. To load the MASS collection, one can execute the following code:\n\n> # The package name can be enclosed in quotes\n> library(\"MASS\")\n\n> # But the package name can also be used without quotes\n> library(MASS)\n\nThe Comprehensive R Archive Network (CRAN) was founded in 1997 by Kurt Hornik and Friedrich Leisch to host R's source code, executable files, documentation, and user-created packages. CRAN's name and scope mimic the Comprehensive TeX Archive Network (CTAN) and the Comprehensive Perl Archive Network (CPAN). CRAN originally had only three mirror sites and twelve contributed packages. As of 30 June 2025, it has 90 mirrors and 22,390 contributed packages. Packages are also available in repositories such as R-Forge, Omegahat, and GitHub.\n\nTo provide guidance on the CRAN web site, its Task Views area lists packages that are relevant for specific topics; sample topics include causal inference, finance, genetics, high-performance computing, machine learning, medical imaging, meta-analysis, social sciences, and spatial statistics.\n\nThe Bioconductor project provides packages for genomic data analysis, complementary DNA, microarray, and high-throughput sequencing methods.\n\nCommunity\n\nThere are three main groups that help support R software development:\n\nThe R Core Team was founded in 1997 to maintain the R source code. In 2026, it was awarded the Rousseeuw Prize for Statistics for its contributions to statistical research and impact on society.\n\nThe R Foundation for Statistical Computing was founded in April 2003 to provide financial support.\n\nThe R Consortium is a Linux Foundation project to develop R infrastructure.\n\nThe R Journal is an open access, academic journal that features short to medium-length articles on the use and development of R. The journal includes articles on packages, programming tips, CRAN news, and foundation news.\n\nThe R community hosts many conferences and in-person meetups. These groups include:\n\nuseR!: an annual international R user conference (website)\n\nDirections in Statistical Computing (DSC) (website)\n\nR-Ladies: an organization to promote gender diversity in the R community (website)\n\nSatRdays: R-focused conferences held on Saturdays (website)\n\nData Science & AI Conferences (website)\n\nposit::conf (formerly known as rstudio::conf) (website)\n\nuRos: an annual conference on the Use of R in Official Statistics (website)\n\nOn social media sites such as Twitter, the hashtag #rstats can be used to follow new developments in the R community.\n\nExamples\n\nHello, World!\n\nThe following is a \"Hello, World!\" program:\n\n> print(\"Hello, World!\")\n[1] \"Hello, World!\"\n\nHere is an alternative version, which uses the cat() function:> cat(\"Hello, World!\")\nHello, World!\n\nBasic syntax\n\nThe following examples illustrate the basic syntax of the language and use of the command-line interface.\n\nIn R, the generally preferred assignment operator is an arrow made from two characters <-, although = can be used in some cases.\n\n> x <- 1:6 # Create a numeric vector in the current environment\n> y <- x^2 # Similarly, create a vector based on the values in x.\n> y # Print the vector’s contents.\n[1] 1 4 9 16 25 36\n\n> z <- x + y # Create a new vector that is the sum of x and y\n> z # Return the contents of z to the current environment.\n[1] 2 6 12 20 30 42\n\n> z_matrix <- matrix(z, nrow = 3) # Create a new matrix that transforms the\n # vector z into a 3x2 matrix object\n> z_matrix \n [,1] [,2]\n[1,] 2 20\n[2,] 6 30\n[3,] 12 42\n\n> 2 * t(z_matrix) - 2 # Transpose the matrix; multiply every element by 2;\n # subtract 2 from each element in the matrix; and\n # then return the results to the terminal.\n [,1] [,2] [,3]\n[1,] 2 10 22\n[2,] 38 58 82\n\n# Create a new dataframe object that contains the data from a transposed\n# z_matrix, with row names 'A' and 'B'\n> new_df <- data.frame(t(z_matrix), row.names = c(\"A\", \"B\")) \n> names(new_df) <- c(\"X\", \"Y\", \"Z\") # Set the column names of the new_df dataframe as X, Y, and Z.\n> new_df # Print the current results.\n X Y Z\nA 2 6 12\nB 20 30 42\n\n> new_df$Z # Output the Z column\n[1] 12 42\n\n> new_df$Z == new_df['Z'] && new_df[3] == new_df$Z # The dataframe column Z can be accessed using the syntax $Z, ['Z'], or [3], and the values are the same. \n[1] TRUE\n\n> attributes(new_df) # Print information about attributes of the new_df dataframe\n$names\n[1] \"X\" \"Y\" \"Z\"\n\n$row.names\n[1] \"A\" \"B\"\n\n$class\n[1] \"data.frame\"\n\n> attributes(new_df)$row.names <- c(\"one\", \"two\") # Access and then change the row.names attribute; this can also be done using the rownames() function\n> new_df\n X Y Z\none 2 6 12\ntwo 20 30 42\n\nStructure of a function\n\nR can create functions that add new functionality and enable code reuse. Objects created within the body of the function (which are enclosed by curly brackets) remain accessible only from within the function, and any data type may be returned. In R, almost all functions and all user-defined functions are closures.\n\nThe following is an example of creating a function to perform an arithmetic calculation:\n\n# The function's input parameters are x and y.\n# The function, named f, returns a linear combination of x and y.\nf <- function(x, y) {\n z <- 3 * x + 4 * y\n\n # An explicit return() statement is optional--it could be replaced with simply `z` in this case.\n return(z)\n}\n\n# As an alternative, the last statement executed in a function is returned implicitly.\nf <- function(x, y) 3 * x + 4 * y\n\nThe following is some output from using the function defined above:\n\n> f(1, 2) # 3 * 1 + 4 * 2 = 3 + 8\n[1] 11\n\n> f(c(1, 2, 3), c(5, 3, 4)) # Element-wise calculation\n[1] 23 18 25\n\n> f(1:3, 4) # Equivalent to f(c(1, 2, 3), c(4, 4, 4))\n[1] 19 22 25\n\nIt is possible to define functions to be used as infix operators by using the special syntax `%name%`, where \"name\" is the function variable name:\n\n> `%sumx2y2%` <- function(e1, e2) {e1 ^ 2 + e2 ^ 2}\n> 1:3 %sumx2y2% -(1:3)\n[1] 2 8 18\n\nSince R version 4.1.0, functions can be written in a short notation (inspired by the lambda calculus), which is useful for passing anonymous functions to higher-order functions: \n\n> sapply(1:5, \\(i) i^2) # here \\(i) is the same as function(i) \n[1] 1 4 9 16 25\n\nNative pipe operator\n\nIn R version 4.1.0, a native pipe operator, |>, was introduced. This operator allows users to chain functions together, rather than using nested function calls.\n\n> nrow(subset(mtcars, cyl == 4)) # Nested without the pipe character\n[1] 11\n\n> mtcars |> subset(cyl == 4) |> nrow() # Using the pipe character\n[1] 11\n\nAn alternative to nested functions is the use of intermediate objects, rather than the pipe operator:\n\n> mtcars_subset_rows <- subset(mtcars, cyl == 4)\n> num_mtcars_subset <- nrow(mtcars_subset_rows)\n> print(num_mtcars_subset)\n[1] 11\n\nWhile the pipe operator can produce code that is easier to read, influential R programmers like Hadley Wickham suggest to chain together at most 10-15 lines of code using this operator and saving them into objects having meaningful names to avoid code obfuscation.\n\nObject-oriented programming\n\nThe R language has native support for object-oriented programming. There are two native frameworks, the so-called S3 and S4 systems. The former, being more informal, supports single dispatch on the first argument, and objects are assigned to a class simply by setting a \"class\" attribute in each object. The latter is a system like the Common Lisp Object System (CLOS), with formal classes (also derived from S) and generic methods, which supports multiple dispatch and multiple inheritance\n\nIn the example below, summary() is a generic function that dispatches to different methods depending on whether its argument is a numeric vector or a factor:\n\n> data <- c(\"a\", \"b\", \"c\", \"a\", NA)\n> summary(data)\n Length Class Mode \n 5 character character \n> summary(as.factor(data))\n a b c NA's \n 2 1 1 1\n\nModeling and plotting\n\nThe R language has built-in support for data modeling and graphics. The following example shows how R can generate and plot a linear model with residuals.\n\n# Create x and y values\nx <- 1:6\ny <- x^2\n\n# Linear regression model: y = A + B * x\nmodel <- lm(y ~ x)\n\n# Display an in-depth summary of the model\nsummary(model)\n\n# Create a 2-by-2 layout for figures\npar(mfrow = c(2, 2))\n\n# Output diagnostic plots of the model\nplot(model)\n\nThe output from the summary() function in the preceding code block is as follows:\n\nResiduals:\n 1 2 3 4 5 6 7 8 9 10\n 3.3333 -0.6667 -2.6667 -2.6667 -0.6667 3.3333\n\nCoefficients:\n Estimate Std. Error t value Pr(>|t|) \n(Intercept) -9.3333 2.8441 -3.282 0.030453 * \nx 7.0000 0.7303 9.585 0.000662 ***\n---\nSignif. codes: 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1\n\nResidual standard error: 3.055 on 4 degrees of freedom\nMultiple R-squared: 0.9583, Adjusted R-squared: 0.9478\nF-statistic: 91.88 on 1 and 4 DF, p-value: 0.000662\n\nMandelbrot set\n\nThis example of a Mandelbrot set highlights the use of complex numbers. It models the first 20 iterations of the equation z = z + c, where c represents different complex constants.\n\nTo run this sample code, it is necessary to first install the package that provides the write.gif() function:\n\ninstall.packages(\"caTools\")\n\nThe sample code is as follows:\n\nlibrary(caTools)\n\njet.colors <-\n colorRampPalette(\n c(\"green\", \"pink\", \"#007FFF\", \"cyan\", \"#7FFF7F\",\n \"white\", \"#FF7F00\", \"red\", \"#7F0000\"))\n\ndx <- 1500 # define width\ndy <- 1400 # define height\n\nC <-\n complex(\n real = rep(seq(-2.2, 1.0, length.out = dx), each = dy),\n imag = rep(seq(-1.2, 1.2, length.out = dy), times = dx)\n )\n\n# reshape as matrix of complex numbers\nC <- matrix(C, dy, dx)\n\n# initialize output 3D array\nX <- array(0, c(dy, dx, 20))\n\nZ <- 0\n\n# loop with 20 iterations\nfor (k in 1:20) {\n\n # the central difference equation\n Z <- Z^2 + C\n\n # capture the results\n X[, , k] <- exp(-abs(Z))\n}\n\nwrite.gif(\n X,\n \"Mandelbrot.gif\",\n col = jet.colors,\n delay = 100)\n\nVersion names\n\nAll R version releases from 2.14.0 onward have codenames that make reference to Peanuts comics and films.\n\nIn 2018, core R developer Peter Dalgaard presented a history of R releases since 1997. Some notable early releases before the named releases include the following:\n\nVersion 1.0.0, released on 29 February 2000, a leap day\n\nVersion 2.0.0, released on 4 October 2004, \"which at least had a nice ring to it\"\n\nThe idea of naming R version releases was inspired by the naming system for Debian and Ubuntu versions. Dalgaard noted an additional reason for the use of Peanuts references in R codenames—the humorous observation that \"everyone in statistics is a P-nut.\"\n\nInterfaces\n\nR is installed with a command line console by default, but there are multiple ways to interface with the language:\n\nIntegrated development environment (IDE):\n\nR.app (OSX/macOS only)\n\nRattle GUI\n\nR Commander\n\nRKWard\n\nRStudio\n\nPositron\n\nTinn-R\n\nGeneral-purpose IDEs:\n\nEclipse via the StatET plugin\n\nVisual Studio via R Tools for Visual Studio.\n\nSource-code editors:\n\nEmacs\n\nVim via the Nvim-R plugin\n\nKate\n\nLyX via Sweave\n\nWinEdt (website)\n\nJupyter (website)\n\nOther scripting languages:\n\nPython (website)\n\nPerl (website)\n\nRuby (source code)\n\nF# (website)\n\nJulia (source code).\n\nGeneral-purpose programming languages:\n\nJava via the Rserve socket server\n\n.NET C# (website)\n\nStatistical frameworks that use R in the background include Jamovi and JASP.\n\nImplementations\n\nThe main R implementation is written primarily in C, Fortran, and R itself. Other implementations include the following:\n\npretty quick R (pqR), by Radford M. Neal, which attempts to improve memory management.\n\nRenjin for the Java Virtual Machine.\n\nCXXR and Riposte written in C++.\n\nOracle's FastR built on GraalVM.\n\nTIBCO Enterprise Runtime for R (TERR) to integrate with Spotfire. (The company also sold S-Plus, a discontinued implementation of the S language.)\n\nMicrosoft R Open (MRO) was an R implementation. As of 30 June 2021, Microsoft began to phase out MRO in favor of the CRAN distribution.\n\nCommercial support\n\nAlthough R is an open-source project, some companies provide commercial support:\n\nOracle provides commercial support for its Big Data Appliance, which integrates R into its other products.\n\nIBM provides commercial support for execution of R within Hadoop.\n\nMicrosoft allows execution of SparkR notebooks in Microsoft Fabric.\n\nSee also"
 },
 {
  "title": "Complex number",
  "revision_id": "1378820439",
  "matched_by": "redirect",
  "text": "In mathematics, a complex number is a number of the form ⁠⁠, where a and b are real numbers, and i is the imaginary unit, a number that satisfies the equation ⁠⁠; the number a is called the real part of ⁠⁠, and b is called the imaginary part.\n\nThe complex numbers form a number system which extends the real numbers and supports the same basic arithmetic operations of addition, subtraction, multiplication, and division, satisfying the same associative, commutative, and distributive laws. This makes the complex numbers a field. The set of complex numbers is denoted by either of the symbols or C.\n\nBecause any nonzero real number, whether positive or negative, squares to a positive number, taking the square root of a negative number was historically considered impossible. When, in the 16th century, such square roots were found helpful for determining the real solutions of cubic equations, they were originally considered a mere symbolic contrivance, and in the 17th century were given the name imaginary numbers. Despite the historical nomenclature, \"imaginary\" numbers are not fictitious: they are no less valid mathematically than real numbers, and they are essential to the scientific description of the physical world.\n\nComplex numbers allow solutions to all non-constant polynomial equations with real or complex coefficients, even those that have no solutions in real numbers, a result known as the fundamental theorem of algebra. The complex numbers also form a real vector space of dimension two, with as a standard basis. Thus each complex number can be uniquely associated to a point with coordinates in a Cartesian plane, called the complex plane. This allows a geometric interpretation of the complex numbers and their operations; in particular, addition by a complex number corresponds to translation of the plane and multiplication by a complex number corresponds to scaling and rotation. Conversely some geometric objects and operations can be expressed in terms of complex numbers, enabling the solution of geometric problems using algebraic methods.\n\nDefinition and basic operations\n\nA complex number is an expression of the form a + bi, where a and b are real numbers, and i is an abstract symbol, the imaginary unit, whose meaning will be explained further below. For example, 2 + 3i is a complex number.\n\nFor a complex number a + bi, the real number a is its real part, and the real number b (not the complex number bi) is its imaginary part. The real part of a complex number z is denoted Re(z), ⁠⁠, or ⁠⁠; the imaginary part is Im(z), ⁠⁠, or ⁠⁠: for example, ⁠⁠, ⁠⁠.\n\nA complex number z can be identified with the ordered pair of real numbers ⁠⁠, which may be interpreted as coordinates of a point in a Euclidean plane with standard coordinates, which is the complex plane or Argand diagram. The horizontal axis is generally used to display the real part, with increasing values to the right, and the imaginary part marks the vertical axis, with increasing values upwards.\n\nA real number a can be regarded as a complex number a + 0i, whose imaginary part is 0. A purely imaginary number bi is a complex number 0 + bi, whose real part is zero. It is common to write a + 0i = a, 0 + bi = bi, and a + (−b)i = a − bi; for example, 3 + (−4)i = 3 − 4i.\n\nThe set of all complex numbers is denoted by (blackboard bold) or C (upright bold).\n\nIn some disciplines such as electromagnetism and electrical engineering, j is used instead of i, as i frequently represents electric current, and complex numbers are written as a + bj or a + jb.\n\nAddition, additive inverse, and subtraction\n\nTwo complex numbers and are added by separately adding their real and imaginary parts. That is to say:\n\nIn particular, the additive inverse of a = x + yi must be −a = (−x) + (−y)i = −x − yi because a + (−a) gives zero by the above addition formula.\nSimilarly, subtraction can be performed as\n\nThe addition can be geometrically visualized as follows: the sum of two complex numbers a and b, interpreted as points in the complex plane, is the point obtained by building a parallelogram from the three vertices O, and the points of the arrows labeled a and b (provided that they are not on a line). Equivalently, calling these points A, B, respectively and the fourth point of the parallelogram X the triangles OAB and XBA are congruent.\n\nMultiplication\n\nThe product of two complex numbers can expanded using the distributive property and the identity ⁠⁠:\n\nFor example,\n\nUsing the sum rule from the previous section and this product rule, the familiar rules for the arithmetic of rational or real numbers continue to hold for complex numbers. Namely, addition and multiplication always satisfy the associative and commutative properties, and multiplication is distributive over addition.\n\nComplex conjugate, absolute value, argument and division\n\nThe complex conjugate of the complex number z = x + yi is defined as\n⁠⁠. It is also denoted by some authors by ⁠⁠. Geometrically, z is the \"reflection\" of z about the real axis. Conjugating twice gives the original complex number: A complex number is real if and only if it equals its own conjugate. The unary operation of taking the complex conjugate of a complex number cannot be expressed by applying only the basic operations of addition, subtraction, multiplication and division. \n\nFor any complex number z = x + yi , the product \n\nis a non-negative real number. This allows to define the absolute value (or modulus or magnitude) of z to be the square root\n\nBy Pythagoras' theorem, is the distance from the origin to the point representing the complex number z in the complex plane. In particular, the circle of radius one around the origin consists precisely of the numbers z such that ⁠⁠, known as the unit complex numbers. If is a real number, then ⁠⁠: its absolute value as a complex number and as a real number are equal. \n\nUsing the conjugate, the reciprocal of a nonzero complex number can be computed to be\n\nEvery complex number ⁠⁠ has an additive inverse ⁠⁠ and every nonzero complex number ⁠⁠ has a multiplicative inverse ⁠⁠; the complex numbers form a field, much as the rational or real numbers do.\n\nMore generally, the division of an arbitrary complex number by a non-zero complex number equals\n\nThis process is sometimes called \"rationalization\" of the denominator (although the denominator in the final expression may be an irrational real number), because it resembles the method to remove roots from simple expressions in a denominator.\n\nThe argument of z, sometimes called the \"phase\", is the angle of the radius Oz measured anticlockwise from the positive real axis. It is written as arg z and is expressed in radians in this article. The angle is defined only up to adding integer multiples of ⁠⁠, since a rotation by (or 360°) around the origin leaves all points in the complex plane unchanged. One possible choice to uniquely specify the argument (also known as choosing a principal value) is to require it to be within the interval ⁠⁠, though there are other possibilities.\nThe argument plays a role with complex logarithms; see below. It can be computed from the rectangular form x + yi by means of the arctan (inverse tangent) function.\n\nPolar form\n\nFor any complex number z, with absolute value and argument ⁠⁠, the equation \n\nholds. This identity is referred to as the polar form of z. It is sometimes written as ⁠⁠ or ⁠⁠. \nIn electronics, one represents a phasor with amplitude r and phase φ in angle notation:\n\nIf two complex numbers are given in polar form, i.e., z1 = r1(cos φ1 + i sin φ1) and z2 = r2(cos φ2 + i sin φ2), the product and division can be computed as \n\n(These are a consequence of the trigonometric identities for the sine and cosine function.)\nIn other words, the absolute values are multiplied and the arguments are added to yield the polar form of the product. The picture at the right illustrates the multiplication of\n\nBecause the real and imaginary part of 5 + 5i are equal, the argument of that number is 45 degrees, or π/4 (in radian). On the other hand, it is also the sum of the angles at the origin of the red and blue triangles are arctan(1/3) and arctan(1/2), respectively. Thus, the formula\n\nholds. As the arctan function can be approximated highly efficiently, formulas like this – known as Machin-like formulas – are used for high-precision approximations of π:\n\nPowers and roots\n\nWhen n is an integer, the n-th power of a complex number can be computed using de Moivre's formula, which is obtained by repeatedly applying the above formula for the product:\n\nFor example, the first few powers of the imaginary unit i are ⁠⁠.\n\nWhen n is a positive integer, the n n-th roots of a complex number z are given by\n\nfor integer k satisfying 0 ≤ k ≤ n − 1 and where is the usual (positive) n-th root of the positive real number r. Because sine and cosine are periodic, other integer values of k do not give additional values. For any ⁠⁠, these n complex n-th roots are distinct. For example, there are 4 fourth roots of 1, namely\n\nFor ⁠⁠, the n-th root is a multivalued function (or specifically, an n-valued function) of z. One of these values can be designated as the principal value, typically via the technique of branch cuts of the complex plane.\n\nFundamental theorem of algebra\n\nThe fundamental theorem of algebra, of Carl Friedrich Gauss and Jean le Rond d'Alembert, states that for any coefficients that are complex numbers a0, ..., an, the equation\n\nhas at least one complex solution z, provided that at least one of the higher coefficients a1, ..., an is nonzero. This property does not hold for the field of rational numbers (the polynomial x − 2 does not have a rational root, because √2 is not a rational number) nor the real numbers (the polynomial x + 4 does not have a real root, because the square of x is positive for any real number x). \n\nBecause of this fact, is an algebraically closed field. It is a cornerstone of various applications of complex numbers, as is detailed further below. \nThere are various proofs of this theorem, by either analytic methods such as Liouville's theorem, or topological ones such as the winding number, or a proof combining Galois theory and the fact that any real polynomial of odd degree has at least one real root.\n\nThe field of complex numbers is defined as the (unique) algebraic extension field of the real numbers later in #Abstract algebraic definitions.\n\nHistory\n\nThe solution in radicals (without trigonometric functions) of a general cubic equation, when all three of its roots are real numbers, contains the square roots of negative numbers, a situation that cannot be rectified by factoring aided by the rational root test, if the cubic is irreducible; this is the casus irreducibilis ('irreducible case'). This conundrum led Italian mathematician Gerolamo Cardano to conceive of complex numbers around 1545 in his Ars Magna, though his understanding was rudimentary; moreover, he later described complex numbers as being \"as subtle as they are useless\". Cardano did use imaginary numbers, but described using them as \"mental torture\". This was prior to the use of the graphical complex plane. Cardano and other Italian mathematicians, notably Scipione del Ferro, in the 1500s created an algorithm for solving cubic equations which generally had one real solution and two solutions containing an imaginary number. Because they ignored the answers with the imaginary numbers, Cardano found them useless.\n\nWork on the problem of general polynomials ultimately led to the fundamental theorem of algebra, which shows that with complex numbers, a solution exists to every polynomial equation of degree one or higher. Complex numbers thus form an algebraically closed field, where any polynomial equation has a root.\n\nMany mathematicians contributed to the development of complex numbers. The rules for addition, subtraction, multiplication, and root extraction of complex numbers were developed by the Italian mathematician Rafael Bombelli. A more abstract formalism for the complex numbers was further developed by the Irish mathematician William Rowan Hamilton, who extended this abstraction to the theory of quaternions.\n\nThe earliest fleeting reference to square roots of negative numbers can perhaps be said to occur in the work of the Greek mathematician Hero of Alexandria in the 1st century AD, where in his Stereometrica he considered, apparently in error, the volume of an impossible frustum of a pyramid to arrive at the term in his calculations, which today would simplify to ⁠⁠. Negative quantities were not conceived of in Hellenistic mathematics and Hero merely replaced the negative value by its positive ⁠⁠.\n\nThe impetus to study complex numbers as a topic in itself first arose in the 16th century when algebraic solutions for the roots of cubic and quartic polynomials were discovered by Italian mathematicians (Niccolò Fontana Tartaglia and Gerolamo Cardano). It was soon realized (but proved much later) that these formulas, even if one were interested only in real solutions, sometimes required the manipulation of square roots of negative numbers. In fact, it was proved later that the use of complex numbers is unavoidable when all three roots are real and distinct. However, the general formula can still be used in this case, with some care to deal with the ambiguity resulting from the existence of three cubic roots for nonzero complex numbers. Rafael Bombelli was the first to address explicitly these seemingly paradoxical solutions of cubic equations and developed the rules for complex arithmetic, trying to resolve these issues.\n\nThe term \"imaginary\" for these quantities was coined by René Descartes in 1637, who was at pains to stress their unreal nature:\n\n... sometimes only imaginary, that is one can imagine as many as I said in each equation, but sometimes there exists no quantity that matches that which we imagine.\n[... quelquefois seulement imaginaires c'est-à-dire que l'on peut toujours en imaginer autant que j'ai dit en chaque équation, mais qu'il n'y a quelquefois aucune quantité qui corresponde à celle qu'on imagine.]\n\nA further source of confusion was that the equation seemed to be capriciously inconsistent with the algebraic identity ⁠⁠, which is valid for non-negative real numbers a and b, and which was also used in complex number calculations with one of a, b positive and the other negative. The incorrect use of this identity in the case when both a and b are negative, and the related identity ⁠⁠, even bedeviled Leonhard Euler. This difficulty eventually led to the convention of using the special symbol i in place of to guard against this mistake. Even so, Euler considered it natural to introduce students to complex numbers much earlier than we do today. In his elementary algebra text book, Elements of Algebra, he introduces these numbers almost at once and then uses them in a natural way throughout.\n\nIn the 18th century complex numbers gained wider use, as it was noticed that formal manipulation of complex expressions could be used to simplify calculations involving trigonometric functions. For instance, in 1730 Abraham de Moivre noted that the identities relating trigonometric functions of an integer multiple of an angle to powers of trigonometric functions of that angle could be re-expressed by the following de Moivre's formula:\n\nIn 1748, Euler went further and obtained Euler's formula of complex analysis:\n\nby formally manipulating complex power series and observed that this formula could be used to reduce any trigonometric identity to much simpler exponential identities.\n\nThe idea of a complex number as a point in the complex plane was first described by Danish–Norwegian mathematician Caspar Wessel in 1799, although it had been anticipated as early as 1685 in Wallis's A Treatise of Algebra.\n\nWessel's memoir appeared in the Proceedings of the Copenhagen Academy but went largely unnoticed. In 1806 Jean-Robert Argand independently issued a pamphlet on complex numbers and provided a rigorous proof of the fundamental theorem of algebra. Carl Friedrich Gauss had earlier published an essentially topological proof of the theorem in 1797 but expressed his doubts at the time about \"the true metaphysics of the square root of −1\". It was not until 1831 that he overcame these doubts and published his treatise on complex numbers as points in the plane, largely establishing modern notation and terminology:\n\nIf one formerly contemplated this subject from a false point of view and therefore found a mysterious darkness, this is in large part attributable to clumsy terminology. Had one not called +1, −1, positive, negative, or imaginary (or even impossible) units, but instead, say, direct, inverse, or lateral units, then there could scarcely have been talk of such darkness.\n\nIn the beginning of the 19th century, other mathematicians discovered independently the geometrical representation of the complex numbers: Buée, Mourey, Warren, Français and his brother, Bellavitis.\n\nThe English mathematician G.H. Hardy remarked that Gauss was the first mathematician to use complex numbers in \"a really confident and scientific way\" although mathematicians such as Norwegian Niels Henrik Abel and Carl Gustav Jacob Jacobi were necessarily using them routinely before Gauss published his 1831 treatise.\n\nAugustin-Louis Cauchy and Bernhard Riemann together brought the fundamental ideas of complex analysis to a high state of completion, commencing around 1825 in Cauchy's case.\n\nThe common terms used in the theory are chiefly due to the founders. Argand called cos φ + i sin φ the direction factor, and the modulus; Cauchy (1821) called cos φ + i sin φ the reduced form (l'expression réduite) and apparently introduced the term argument; Gauss used i for , introduced the term complex number for a + bi, and called a + b the norm. The expression direction coefficient, often used for cos φ + i sin φ, is due to Hankel (1867), and absolute value, for modulus, is due to Weierstrass.\n\nLater classical writers on the general theory include Richard Dedekind, Otto Hölder, Felix Klein, Henri Poincaré, Hermann Schwarz, Karl Weierstrass and many others. Important work (including a systematization) in complex multivariate calculus has been started at beginning of the 20th century. Important results have been achieved by Wilhelm Wirtinger in 1927.\n\nAbstract and algebraic definitions\n\nWhile the above concrete definitions, including the addition and multiplication, accurately describe the complex"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q9852",
  "label": "R/r",
  "description": "18th letter of the basic Latin alphabet",
  "aliases": [
   "ar",
   "Romeo",
   "ʀ",
   "romeo"
  ],
  "claims": {
   "P279": [
    "Q19776628",
    "Q3841820"
   ],
   "P361": [
    "Q606972",
    "Q754673",
    "Q76228",
    "Q607188",
    "Q9147416",
    "Q1187758",
    "Q637405",
    "Q570693",
    "Q550383",
    "Q755124",
    "Q18691434",
    "Q384749",
    "Q994407",
    "Q1493494",
    "Q2839543",
    "Q912243",
    "Q1193493",
    "Q41670"
   ],
   "P527": [
    "Q87496233",
    "Q87496306",
    "Q87496233",
    "Q87496306"
   ],
   "P1889": [
    "Q21068",
    "Q206904",
    "Q118372492",
    "Q131612571",
    "Q131612643",
    "Q8084142"
   ]
  },
  "revision_id": "2548549722",
  "value_labels": {
   "Q19776628": "Latin-script letter",
   "Q3841820": "consonant letter",
   "Q606972": "Polish alphabet",
   "Q754673": "English alphabet",
   "Q76228": "Czech alphabet",
   "Q607188": "Esperanto alphabet",
   "Q9147416": "Breton alphabet",
   "Q1187758": "Slovak alphabet",
   "Q637405": "Turkish alphabet",
   "Q570693": "Azerbaijani Latin alphabet",
   "Q550383": "Italian alphabet",
   "Q755124": "French alphabet",
   "Q18691434": "Finnish alphabet",
   "Q384749": "Africa Alphabet",
   "Q994407": "African reference alphabet",
   "Q1493494": "Pan-Nigerian alphabet",
   "Q2839543": "Benin National Alphabet",
   "Q912243": "German alphabet",
   "Q1193493": "Latvian alphabet",
   "Q41670": "Latin alphabet",
   "Q87496233": "R",
   "Q87496306": "r",
   "Q21068": "",
   "Q206904": "R",
   "Q118372492": "R̥̄",
   "Q131612571": "Ꭱ/ꭱ",
   "Q131612643": "Ꮢ/ꮢ",
   "Q8084142": "Ꞅ/ꞅ"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q206904",
  "label": "R",
  "description": "programming language for statistical analysis",
  "aliases": [
   "GNU R",
   "GNU S",
   "R language",
   "R programming language"
  ],
  "claims": {
   "P31": [
    "Q9143",
    "Q12772052",
    "Q13199995",
    "Q20825628",
    "Q2267705",
    "Q341"
   ],
   "P1889": [
    "Q9852",
    "Q18665344",
    "Q112162285",
    "Q21068",
    "Q113585511"
   ]
  },
  "revision_id": "2562780000",
  "value_labels": {
   "Q9143": "programming language",
   "Q12772052": "multi-paradigm programming language",
   "Q13199995": "statistical package",
   "Q20825628": "GNU package",
   "Q2267705": "field of study",
   "Q341": "free software",
   "Q9852": "R/r",
   "Q18665344": "R",
   "Q112162285": "Rising Auto",
   "Q21068": "",
   "Q113585511": "R"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11567",
  "label": "complex number",
  "description": "number that can be put in the form a + i b, where a and b are real numbers and i is called the imaginary unit",
  "aliases": [],
  "claims": {
   "P31": [
    "Q47460393"
   ],
   "P279": [
    "Q173853",
    "Q11563",
    "Q837414",
    "Q191290"
   ],
   "P361": [
    "Q26851286"
   ],
   "P527": [
    "Q193796",
    "Q12916",
    "Q1156910",
    "Q1341545"
   ],
   "P1889": [
    "Q28006"
   ]
  },
  "revision_id": "2570412106",
  "value_labels": {
   "Q47460393": "type of number",
   "Q173853": "quaternion",
   "Q11563": "number",
   "Q837414": "hypercomplex number",
   "Q191290": "ordered pair",
   "Q26851286": "set of complex numbers",
   "Q193796": "imaginary unit",
   "Q12916": "real number",
   "Q1156910": "real part",
   "Q1341545": "imaginary part",
   "Q28006": ""
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q19776628",
  "label": "Latin-script letter",
  "description": "letter in the Latin script",
  "aliases": [
   "Latin letter",
   "letter of the Latin alphabet"
  ],
  "claims": {
   "P279": [
    "Q9788"
   ],
   "P361": [
    "Q8229"
   ]
  },
  "revision_id": "2546253990",
  "ancestor_of": "Q9852",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3841820",
  "label": "consonant letter",
  "description": "letter in an alphabet, which generally represents a consonantal phoneme",
  "aliases": [
   "consonant"
  ],
  "claims": {
   "P279": [
    "Q9788"
   ],
   "P1889": [
    "Q38035"
   ]
  },
  "revision_id": "2533332370",
  "ancestor_of": "Q9852",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9788",
  "label": "letter",
  "description": "grapheme in an alphabetic system of writing",
  "aliases": [],
  "claims": {
   "P279": [
    "Q2545446",
    "Q28786318"
   ],
   "P361": [
    "Q191494",
    "Q15139721",
    "Q8171"
   ],
   "P527": [
    "Q3841820",
    "Q9398093"
   ],
   "P1889": [
    "Q133492",
    "Q1383557",
    "Q138659"
   ]
  },
  "revision_id": "2569933779",
  "ancestor_of": "Q9852",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q13199995",
  "label": "statistical package",
  "description": "software for statistical analysis",
  "aliases": [
   "statistical software"
  ],
  "claims": {
   "P31": [
    "Q17155032",
    "Q4485156"
   ],
   "P279": [
    "Q1639024"
   ]
  },
  "revision_id": "2505148169",
  "ancestor_of": "Q206904",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20825628",
  "label": "GNU package",
  "description": "name given to free software distributed by the GNU project",
  "aliases": [],
  "claims": {
   "P31": [
    "Q1995545"
   ],
   "P279": [
    "Q341",
    "Q1995545"
   ],
   "P361": [
    "Q7598"
   ],
   "P1889": [
    "Q125242556"
   ]
  },
  "revision_id": "2462049784",
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4485156",
  "label": "software feature",
  "description": "distinguishing characteristic of a program",
  "aliases": [
   "feature",
   "capability",
   "software capability",
   "computer software feature"
  ],
  "claims": {
   "P279": [
    "Q1347367"
   ],
   "P361": [
    "Q7397"
   ],
   "P1889": [
    "Q110224587"
   ]
  },
  "revision_id": "2531346117",
  "ancestor_of": "Q206904",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1639024",
  "label": "mathematical software",
  "description": "software to model, analyze or calculate numeric, symbolic or geometric data",
  "aliases": [],
  "claims": {
   "P31": [
    "Q17155032"
   ],
   "P279": [
    "Q15544757"
   ]
  },
  "revision_id": "2565459327",
  "ancestor_of": "Q206904",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1995545",
  "label": "software package",
  "description": "bundle containing software, data and associated information needed for installation by a package manager",
  "aliases": [
   "package",
   "packaged software"
  ],
  "claims": {
   "P31": [
    "Q1351368",
    "Q7397"
   ],
   "P279": [
    "Q7397"
   ],
   "P527": [
    "Q188860",
    "Q40056"
   ],
   "P1889": [
    "Q1143070"
   ]
  },
  "revision_id": "2569620158",
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
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
  "ancestor_of": "Q206904",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q47460393",
  "label": "type of number",
  "description": "metaclass of classes containing numbers",
  "aliases": [
   "number type",
   "class of number",
   "number class",
   "number classification"
  ],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q21146257",
    "Q246672"
   ],
   "P1889": [
    "Q3054943",
    "Q2297602",
    "Q122653",
    "Q77358734",
    "Q77359186"
   ]
  },
  "revision_id": "2528779236",
  "ancestor_of": "Q11567",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q173853",
  "label": "quaternion",
  "description": "noncommutative extension of the real numbers",
  "aliases": [
   "Hamilton number"
  ],
  "claims": {
   "P279": [
    "Q837414",
    "Q29428373",
    "Q191290",
    "Q743418"
   ],
   "P361": [
    "Q47407672"
   ],
   "P527": [
    "Q12916"
   ]
  },
  "revision_id": "2563474090",
  "ancestor_of": "Q11567",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11563",
  "label": "number",
  "description": "mathematical object used to count, label, and measure",
  "aliases": [
   "numbers"
  ],
  "claims": {
   "P31": [
    "Q24034552"
   ],
   "P279": [
    "Q246672"
   ],
   "P361": [
    "Q3054943"
   ],
   "P460": [
    "Q1289248"
   ],
   "P1889": [
    "Q11755814",
    "Q5576117",
    "Q140598",
    "Q4516286"
   ]
  },
  "revision_id": "2571708819",
  "ancestor_of": "Q11567",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q837414",
  "label": "hypercomplex number",
  "description": "element of a unital algebra over the field of real numbers",
  "aliases": [],
  "claims": {
   "P31": [
    "Q47460393"
   ],
   "P279": [
    "Q11563"
   ],
   "P527": [
    "Q11567"
   ]
  },
  "revision_id": "2509139945",
  "ancestor_of": "Q11567",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q191290",
  "label": "ordered pair",
  "description": "pair of mathematical objects; tuple of specific length (tuple length n=2)",
  "aliases": [
   "(a, b)",
   "couple",
   "double",
   "pair",
   "2-tuple"
  ],
  "claims": {
   "P279": [
    "Q135268494",
    "Q600590"
   ],
   "P361": [
    "Q130901"
   ],
   "P1889": [
    "Q1477744"
   ]
  },
  "revision_id": "2542261846",
  "ancestor_of": "Q11567",
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
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21146257",
  "label": "type",
  "description": "kind or variety of something",
  "aliases": [
   "kind",
   "form",
   "variety"
  ],
  "claims": {
   "P31": [
    "Q19478619",
    "Q115490628"
   ],
   "P279": [
    "Q16889133",
    "Q19478619",
    "Q141444832"
   ],
   "P1889": [
    "Q24017414"
   ]
  },
  "revision_id": "2567136767",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q246672",
  "label": "mathematical object",
  "description": "object or value related to or describable using mathematical concepts or properties",
  "aliases": [
   "entity",
   "abstract mathematical object",
   "object (mathematics)",
   "mathematical entity"
  ],
  "claims": {
   "P31": [
    "Q96251598"
   ],
   "P279": [
    "Q24034552",
    "Q141159005",
    "Q141537802"
   ],
   "P361": [
    "Q7048977",
    "Q30060700"
   ]
  },
  "revision_id": "2563848659",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q29428373",
  "label": "tetrad",
  "description": "concrete group of 4 specific members",
  "aliases": [
   "group of 4",
   "set of 4",
   "set of four",
   "Chinese enumerations of 4",
   "Japanese enumerations of 4",
   "Buddhist enumerations of 4",
   "tetrad",
   "tetrad (concrete)",
   "enumerations of 4",
   "enumeration of 4"
  ],
  "claims": {
   "P31": [
    "Q99469810"
   ],
   "P279": [
    "Q99527517",
    "Q4025884"
   ],
   "P1889": [
    "Q4515008",
    "Q135268496"
   ]
  },
  "revision_id": "2567990811",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q743418",
  "label": "octonion",
  "description": "non-commutative, non-associative algebra of numbers with eight real components",
  "aliases": [
   "Cayley number",
   "octave",
   "octonions",
   "Cayley numbers",
   "octaves"
  ],
  "claims": {
   "P31": [
    "Q2165111",
    "Q2835924"
   ],
   "P279": [
    "Q41205988",
    "Q3927329",
    "Q191290",
    "Q79188",
    "Q837414"
   ],
   "P361": [
    "Q2835924"
   ],
   "P527": [
    "Q173853"
   ]
  },
  "revision_id": "2497650042",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q24034552",
  "label": "mathematical concept",
  "description": "abstract entity in mathematics",
  "aliases": [
   "concept in mathematics",
   "mathematical concepts",
   "math concept",
   "maths concept"
  ],
  "claims": {
   "P31": [
    "Q23958852",
    "Q137429456"
   ],
   "P279": [
    "Q151885"
   ],
   "P460": [
    "Q66786238"
   ]
  },
  "revision_id": "2569587136",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q135268494",
  "label": "group of 2",
  "description": "generic group of 2 things",
  "aliases": [],
  "claims": {
   "P31": [
    "Q2360980"
   ],
   "P279": [
    "Q135268423",
    "Q16887380"
   ],
   "P527": [
    "Q488383"
   ],
   "P1889": [
    "Q29431432"
   ]
  },
  "revision_id": "2537903273",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q600590",
  "label": "𝑛-tuple",
  "description": "finite ordered list of elements",
  "aliases": [
   "tuple",
   "ordered tuplet",
   "ordered list",
   "ordered n-tuple",
   "n-tuple",
   "sumo:List",
   "xwkont-core:ListSequence",
   "gum:OrderedObject",
   "FormalSemantics:Tuple",
   "af-r:Tuple",
   "afr:Tuple"
  ],
  "claims": {
   "P279": [
    "Q133250",
    "Q3054922",
    "Q141447333",
    "Q379825"
   ],
   "P361": [
    "Q203066"
   ],
   "P527": [
    "Q379825"
   ],
   "P460": [
    "Q12362178"
   ],
   "P1889": [
    "Q11748370",
    "Q133250"
   ]
  },
  "revision_id": "2570940453",
  "ancestor_of": "Q11567",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-13667510-n",
  "lemmas": [
   "roentgen",
   "R"
  ],
  "gloss": "a unit of radiation exposure; the dose of ionizing radiation that will produce 1 electrostatic unit of electricity in 1 cc of dry air",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-13656797-n"
   ],
   "part_meronym": [
    "oewn-92467110-n"
   ]
  },
  "relation_targets": {
   "oewn-13656797-n": "radioactivity unit",
   "oewn-92467110-n": "milliroentgen"
  }
 },
 {
  "synset": "oewn-13611282-n",
  "lemmas": [
   "gas constant",
   "universal gas constant",
   "R"
  ],
  "gloss": "(physics) the universal constant in the gas equation: pressure times volume = R times temperature; equal to 8.3143 joules per kelvin per mole",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-13606632-n"
   ]
  },
  "relation_targets": {
   "oewn-13606632-n": "constant"
  }
 },
 {
  "synset": "oewn-06846054-n",
  "lemmas": [
   "R",
   "r"
  ],
  "gloss": "the 18th letter of the Roman alphabet",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06841868-n"
   ],
   "member_holonym": [
    "oewn-06509863-n"
   ]
  },
  "relation_targets": {
   "oewn-06841868-n": "letter, letter of the alphabet, alphabetic character",
   "oewn-06509863-n": "Roman alphabet, Latin alphabet"
  }
 },
 {
  "synset": "oewn-05109363-n",
  "lemmas": [
   "radius",
   "r"
  ],
  "gloss": "the length of a line segment between the center and circumference of a circle or sphere",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-05136466-n"
   ],
   "part_holonym": [
    "oewn-05109077-n"
   ],
   "hyponym": [
    "oewn-05109562-n",
    "oewn-05109840-n"
   ]
  },
  "relation_targets": {
   "oewn-05136466-n": "length",
   "oewn-05109077-n": "diameter, diam",
   "oewn-05109562-n": "semidiameter",
   "oewn-05109840-n": "radius of curvature"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 2: Go (`n29960itit`)

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
[
 {
  "title": "Go (programming language)",
  "revision_id": "1375187723",
  "matched_by": "title",
  "text": "Go (often referred to as Golang) is a high-level, general-purpose programming language that is statically typed and compiled. Originally designed in 2007 by Robert Griesemer, Rob Pike, and Ken Thompson, Go was publicly announced in November 2009, and is developed by Google and community contributors. Go has a simple syntax similar to C++, as well as garbage collection, structural typing, CSP-style concurrency, and a broad standard library.\n\nThere are two major implementations:\n\nThe original, self-hosting compiler toolchain, initially developed inside Google;\n\nA frontend written in C++, called gofrontend, originally a GCC frontend, providing gccgo, a GCC-based Go compiler; later extended to also support LLVM, providing an LLVM-based Go compiler called gollvm.\n\nHistory\n\nGo was designed at Google in 2007 to improve programming productivity in an era of multicore, networked machines and large codebases. The designers wanted to address criticisms of other languages in use at Google, but keep their useful characteristics:\n\nStatic typing and run-time efficiency (like C)\n\nReadability and usability (like Python)\n\nHigh-performance networking and multiprocessing\n\nIts designers were primarily motivated by their shared dislike of C++.\n\nGo was publicly announced in November 2009, and version 1.0 was released in March 2012. Go is widely used in production at Google and in many other organizations and open-source projects.\n\nGo developers implemented runtime support for concurrency in response to the availability of multicore systems:\n\nAlthough the design of most languages concentrates on innovations in syntax, semantics, or typing, Go is focused on the software development process itself. ... The principal unusual property of the language itself—concurrency—addressed problems that arose with the proliferation of multicore CPUs in the 2010s. But more significant was the early work that established fundamentals for packaging, dependencies, build, test, deployment, and other workaday tasks of the software development world, aspects\nthat are not usually foremost in language design.\n\nAs of April 2022, each commit to the Go repository must be approved by two Google employees.\n\nBranding and styling\n\nThe gopher mascot was introduced in 2009 for the open source launch of the language. Renée French, who had designed the rabbit mascot for Plan 9, adapted the gopher from an earlier WFMU T-shirt design. The gopher was originally named Gordon, but it has been nameless since 2010.\n\nIn November 2016, the Go and Go Mono fonts were released by type designers Charles Bigelow and Kris Holmes specifically for use by the Go project. Go is a humanist sans-serif resembling Lucida Grande but with near (not full) metric compatibility with Helvetica and Arial, and Go Mono is monospaced. Both fonts adhere to the WGL4 character set and were designed to be legible with a large x-height and distinct letterforms. Both Go and Go Mono adhere to the DIN 1450 standard by having a slashed zero, lowercase l with a tail, and an uppercase I with serifs.\n\nIn April 2018, the original logo was redesigned by brand designer Adam Smith. The new logo is a modern, stylized GO slanting right with trailing streamlines. The gopher mascot remained the same.\n\nGenerics\n\nThe lack of support for generic programming in initial versions of Go drew considerable criticism. The designers expressed an openness to generic programming and noted that built-in functions were in fact type-generic, but are treated as special cases; Pike called this a weakness that might be changed at some point. The Google team built at least one compiler for an experimental Go dialect with generics, but did not release it.\n\nIn August 2018, the Go principal contributors published draft designs for generic programming and error handling and asked users to submit feedback. However, the error handling proposal was eventually abandoned.\n\nIn June 2020, a new draft design document was published that would add the necessary syntax to Go for declaring generic functions and types. A code translation tool, go2go, was provided to allow users to try the new syntax, along with a generics-enabled version of the online Go Playground.\n\nGenerics were finally added to Go in version 1.18 on March 15, 2022.\n\nVersioning\n\nGo 1 guarantees compatibility for the language specification and major parts of the standard library. All versions up through the current Go 1.26 release have maintained this promise.\n\nGo uses a go1.[major].[patch] versioning format, such as go1.26.0 and each major Go release is supported until there are two newer major releases. Unlike most software, Go calls the second number in a version the major, i.e., in go1.26.0 the 26 is the major version. This is because Go plans to never reach 2.0, prioritizing backwards compatibility over potential breaking changes.\n\nDesign\n\nGo is influenced by C (especially the Plan 9 dialect), but with an emphasis on greater simplicity and safety. It consists of:\n\nA syntax and environment adopting patterns more common in dynamic languages:\n\nOptional concise variable declaration and initialization through type inference (x := 0 instead of var x int = 0; or var x = 0;)\n\nFast compilation\n\nRemote package management (go get) and online package documentation\n\nDistinctive approaches to particular problems:\n\nBuilt-in concurrency primitives: light-weight processes (goroutines), channels, and the select statement\n\nAn interface system in place of virtual inheritance, and type embedding instead of non-virtual inheritance\n\nA toolchain that, by default, produces statically linked native binaries without external Go dependencies\n\nA desire to keep the language specification simple enough to hold in a programmer's head, in part by omitting features that are common in similar languages.\n\n25 reserved words\n\nSyntax\n\nGo's syntax includes changes from C aimed at keeping code concise and readable. A combined declaration/initialization operator was introduced that allows the programmer to write i := 3 or s := \"Hello, world!\", without specifying the types of variables used. This contrasts with C's int i = 3; and char *s = \"Hello, world!\"; (though since C23 type inference has been supported using auto, like C++). Go also removes the requirement to use parentheses in if statement conditions.\n\nSemicolons still terminate statements; but are implicit when the end of a line occurs.\n\nMethods may return multiple values, and returning a result, err pair is the conventional way a method indicates an error to its caller in Go. Go adds literal syntaxes for initializing struct parameters by name and for initializing maps and slices. As an alternative to C's three-statement for loop, Go's range expressions allow concise iteration over arrays, slices, strings, maps, and channels.\n\nKeywords\n\nGo contains the following 25 keywords:\n\nbreak\n\ncase\n\nchan\n\nconst\n\ncontinue\n\ndefault\n\ndefer\n\nelse\n\nfallthrough\n\nfor\n\nfunc\n\ngo\n\ngoto\n\nif\n\nimport\n\ninterface\n\nmap\n\npackage\n\nrange\n\nreturn\n\nselect\n\nstruct\n\nswitch\n\ntype\n\nvar\n\nTypes\n\nGo has a number of built-in types, including numeric ones (byte, int64, float32, etc.), Booleans, and byte strings (string). Strings are immutable; built-in operators and keywords (rather than functions) provide concatenation, comparison, and UTF-8 encoding/decoding. Record types can be defined with the struct keyword.\n\nGo contains the following primitives:\n\nbool\n\nint8\n\nuint8\n\nint16\n\nuint16\n\nint32\n\nuint32\n\nint64\n\nuint64\n\nint\n\nuint\n\nuintptr\n\nfloat32\n\nfloat64\n\ncomplex64\n\ncomplex128\n\nstring\n\nNote that byte is an alias for uint8 and rune is an alias for int32.\n\nFor each type T and each non-negative integer constant n, there is an array type denoted [n]T; arrays of differing lengths are thus of different types. Dynamic arrays are available as \"slices\", denoted []T for some type T (compare to other languages like C/C++ and Java, where instead the arrays are denoted T[]). These have a length and a capacity specifying when new memory needs to be allocated to expand the array. Several slices may share their underlying memory.\n\nPointers are available for all types, and the pointer-to-T type is denoted *T (similar to Rust; compare to other languages like C/C++ and C#, where pointers are denoted T*). Address-taking and indirection use the & and * operators, as in C, or happen implicitly through the method call or attribute access syntax. There is no pointer arithmetic, except via the special unsafe.Pointer type in the standard library.\n\nFor a pair of types K, V, the type map[K]V is the type mapping type-K keys to type-V values, which can be thought of as equivalent to Map<K, V> in other languages. The Go Programming Language specification does not give any performance guarantees or implementation requirements for map types, though it is usually implemented as a hash table (equivalent to HashMap<K, V> in other languages). Hash tables are built into the language, with special syntax and built-in functions. chan T is a channel that allows sending values of type T between concurrent Go processes.\n\nAside from its support for interfaces, Go's type system is nominal: the type keyword can be used to define a new named type, which is distinct from other named types that have the same layout (in the case of a struct, the same members in the same order). Some conversions between types (e.g., between the various integer types) are pre-defined and adding a new type may define additional conversions, but conversions between named types must always be invoked explicitly. For example, the type keyword can be used to define a type for IPv4 addresses, based on 32-bit unsigned integers as follows:\n\ntype ipv4addr uint32\n\nWith this type definition, ipv4addr(x) interprets the uint32 value x as an IP address. Simply assigning x to a variable of type ipv4addr is a type error.\n\nConstant expressions may be either typed or \"untyped\"; they are given a type when assigned to a typed variable if the value they represent passes a compile-time check.\n\nFunction types are indicated by the func keyword; they take zero or more parameters and return zero or more values, all of which are typed. The parameter and return values determine a function type; thus, func(string, int32) (int, error) is the type of functions that take a string and a 32-bit signed integer, and return a signed integer (of default width) and a value of the built-in interface type error.\n\nAny named type has a method set associated with it. The IP address example above can be extended with a method for checking whether its value is a known standard:\n\n// ZeroBroadcast reports whether addr is 255.255.255.255.\nfunc (addr ipv4addr) ZeroBroadcast() bool {\n return addr == 0xFFFFFFFF\n}\n\nDue to nominal typing, this method definition adds a method to ipv4addr, but not on uint32. While methods have special definition and call syntax, there is no distinct method type.\n\n Interface system\n\nGo provides two features that replace class inheritance.\n\nThe first is embedding, which can be viewed as an automated form of composition.\n\nThe second are its interfaces, which provides runtime polymorphism. Interfaces are a class of types and provide a limited form of structural typing in the otherwise nominal type system of Go. An object which is of an interface type is also of another type, much like C++ objects being simultaneously of a base and derived class. The design of Go interfaces was inspired by protocols from the Smalltalk programming language. Multiple sources use the term duck typing when describing Go interfaces. Although the term duck typing is not precisely defined and therefore not wrong, it usually implies that type conformance is not statically checked. Because conformance to a Go interface is checked statically by the Go compiler (except when performing a type assertion), the Go authors prefer the term structural typing.\n\nThe definition of an interface type lists required methods by name and type. Any object of type T for which functions exist matching all the required methods of interface type I is an object of type I as well. The definition of type T need not (and cannot) identify type I. For example, if Shape, Square, and Circle are defined as\n\nimport \"math\"\n\ntype Shape interface {\n Area() float64\n}\n\n// Note: no \"implements\" declaration\ntype Square struct {\n side float64\n}\n\nfunc (sq Square) Area() float64 {\n return sq.side * sq.side\n}\n\n// No \"implements\" declaration here either\ntype Circle struct {\n radius float64\n}\n\nfunc (c Circle) Area() float64 {\n return math.Pi * math.Pow(c.radius, 2)\n}\n\nthen both a Square and a Circle are implicitly a Shape and can be assigned to a Shape-typed variable. In formal language, Go's interface system provides structural rather than nominal typing. Interfaces can embed other interfaces with the effect of creating a combined interface that is satisfied by exactly the types that implement the embedded interface and any methods that the newly defined interface adds.\n\nThe Go standard library uses interfaces to provide genericity in several places, including the input/output system that is based on the concepts of Reader and Writer.\n\nBesides calling methods via interfaces, Go allows converting interface values to other types with a run-time type check. The language constructs to do so are the type assertion, which checks against a single potential type:var shp Shape = Square{5}\nsquare, ok := shp.(Square) // Asserts Square type on shp, should work\nif ok {\n fmt.Printf(\"%#v\\n\", square)\n} else {\n fmt.Println(\"Can't print shape as Square\")\n}\n\nand the type switch, which checks against multiple types:func (sq Square) Diagonal() float64 { return sq.side * math.Sqrt2 }\nfunc (c Circle) Diameter() float64 { return 2 * c.radius }\n\nfunc LongestContainedLine(shp Shape) float64 {\n switch v := shp.(type) {\n case Square:\n return v.Diagonal() // Or, with type assertion, shp.(Square).Diagonal()\n case Circle:\n return v.Diameter() // Or, with type assertion, shp.(Circle).Diameter()\n default:\n return 0 // In practice, this should be handled with errors\n }\n}\n\nThe empty interface interface{} is an important base case because it can refer to an item of any concrete type. It is similar to the Object class in Java or C# or void* in C or Any in C++ and Rust and is satisfied by any type, including built-in types like int. Code using the empty interface cannot simply call methods (or built-in operators) on the referred-to object, but it can store the interface{} value, try to convert it to a more useful type via a type assertion or type switch, or inspect it with Go's reflect package. Because interface{} can refer to any value, it is a limited way to escape the restrictions of static typing, like void* in C but with additional run-time type checks.\n\nThe interface{} type can be used to model structured data of any arbitrary schema in Go, such as JSON or YAML data, by representing it as a map[string]interface{} (map of string to empty interface). This recursively describes data in the form of a dictionary with string keys and values of any type.\n\nInterface values are implemented using pointer to data and a second pointer to run-time type information. Like some other types implemented using pointers in Go, interface values are nil if uninitialized.\n\nGeneric code using parameterized types\n\nSince version 1.18, Go supports generic code using parameterized types.\n\nFunctions and types now have the ability to be generic using type parameters. These type parameters are specified within square brackets, right after the function or type name. The compiler transforms the generic function or type into non-generic by substituting type arguments for the type parameters provided, either explicitly by the user or type inference by the compiler. This transformation process is referred to as type instantiation.\n\nInterfaces now can define a set of types (known as type set) using | (Union) operator, as well as a set of methods. These changes were made to support type constraints in generics code. For a generic function or type, a constraint can be thought of as the type of the type argument: a meta-type. This new ~T syntax will be the first use of ~ as a token in Go. ~T means the set of all types whose underlying type is T.type Number interface {\n ~int | ~float64 | ~float32 | ~int32 | ~int64\n}\n\nfunc Add[T Number](nums ...T) T {\n var sum T\n for _, v := range nums {\n sum += v\n }\n return sum\n}\n\nfunc main() {\n add := Add[int] // Type instantiation\n println(add(1, 2, 3, 4, 5)) // 15\n\n res := Add(1.1, 2.2, 3.3, 4.4, 5.5) // Type Inference\n println(res) // +1.650000e+001\n}\n\nEnumerated types\n\nGo uses the iota identifier to create enumerated constants:\n\ntype ByteSize int\n\nconst (\n _ = iota // ignore first value by assigning to blank identifier; 0\n KB ByteSize = 1 << (10 * iota) // 1 << (10 * 1) == 1 << 10 == 1024; in binary 10000000000\n MB // 1 << (10 * 2) == 1048576; in binary 100000000000000000000\n GB // 1 << (10 * 3) == 1073741824; in binary 1000000000000000000000000000000\n)\n\nPackage system\n\nIn Go's package system, each package has a path (e.g., \"compress/bzip2\" or \"golang.org/x/net/html\") and a name (e.g., bzip2 or html). By default other packages' definitions must always be prefixed with the other package's name. However the name used can be changed from the package name, and if imported as _, then no package prefix is required. Only the capitalized names from other packages are accessible: io.Reader is public but bzip2.reader is not. The go get command can retrieve packages stored in a remote repository and developers are encouraged to develop packages inside a base path corresponding to a source repository (such as example.com/user_name/package_name) to reduce the likelihood of name collision with future additions to the standard library or other external libraries.\n\n Concurrency: goroutines and channels\n\nThe Go language has built-in facilities, as well as library support, for writing concurrent programs. The runtime is asynchronous: program execution that performs, for example, a network read will be suspended until data is available to process, allowing other parts of the program to perform other work. This is built into the runtime and does not require any changes in program code. The go runtime also automatically schedules concurrent operations (goroutines) across multiple CPUs; this can achieve parallelism for a properly written program.\n\nThe primary concurrency construct is the goroutine, a type of green thread. A function call prefixed with the go keyword starts a function in a new goroutine. The language specification does not specify how goroutines should be implemented, but current implementations multiplex a Go process's goroutines onto a smaller set of operating-system threads, similar to the scheduling performed in Erlang and Haskell's Glasgow Haskell Compiler (GHC) runtime implementation.\n\nWhile a standard library package featuring most of the classical concurrency control structures (mutex locks, etc.) is available, idiomatic concurrent programs instead prefer channels, which send messages between goroutines. Optional buffers store messages in FIFO order and allow sending goroutines to proceed before their messages are received.\n\nChannels are typed, so that a channel of type chan T can only be used to transfer messages of type T. Special syntax is used to operate on them; <-ch is an expression that causes the executing goroutine to block until a value comes in over the channel ch, while ch <- x sends the value x (possibly blocking until another goroutine receives the value). The built-in switch-like select statement can be used to implement non-blocking communication on multiple channels; see below for an example. Go has a memory model describing how goroutines must use channels"
 },
 {
  "title": "Go (game)",
  "revision_id": "1377627768",
  "matched_by": "title-minus-qualifier",
  "text": "Go, weiqi, or baduk is an abstract strategy board game for two players in which the aim is to fence off more territory than the opponent. The game was invented in China more than 2,500 years ago and is believed to be the oldest board game continuously played to the present day. A 2016 survey by the International Go Federation's 75 member nations found that there are over 46 million people worldwide who know how to play Go, and over 20 million current players, the majority of whom live in East Asia.\n\nThe playing pieces are called stones. One player uses the white stones and the other black stones. The players take turns placing their stones on the vacant intersections (points) on the board. Once placed, stones may not be moved, but captured stones are immediately removed from the board. A single stone (or connected group of stones) is captured when surrounded by the opponent's stones on all orthogonally adjacent points. The game proceeds until neither player wishes to make another move.\n\nWhen a game concludes, the winner is determined by counting each player's surrounded territory along with captured stones and komi (points added to the score of the player with the white stones as compensation for playing second). Games may also end by resignation.\n\nThe standard Go board has a 19×19 grid of lines, containing 361 points. Beginners often play on smaller 9×9 or 13×13 boards, and archaeological evidence shows that the game was played in earlier centuries on a board with a 17×17 grid. The 19×19 board had become standard by the time the game reached Korea in the 5th century CE and Japan in the 7th century CE.\n\nGo was considered one of the four essential arts of the cultured aristocratic Chinese scholars in antiquity. The earliest written reference to the game is generally recognized as the historical annal Zuo Zhuan (c. 4th century BCE).\n\nDespite its relatively simple rules, Go is extremely complex. Compared to chess, Go has a larger board with more scope for play, longer games, and, on average, many more alternatives to consider per move. The number of legal board positions in Go has been calculated to be approximately 2.1×10, which is far greater than the number of atoms in the observable universe, which is estimated to be on the order of 10.\n\nNames of the game\n\nThe name Go is a short form of the Japanese word igo (囲碁; いご), which derives from earlier wigo (ゐご), in turn from Middle Chinese ɦʉi gi (圍棋, Mandarin: wéiqí, lit. 'encirclement board game' or 'board game of surrounding'). In English, the name Go when used for the game is often capitalized to differentiate it from the common word go. In events sponsored by the Ing Chang-ki Foundation, it is spelled goe.\n\nThe Korean name baduk (바둑) is a native derived term, most likely originally consisting of 밭 (Yale: pàth, 'cultivated field') + *돍〯 (Yale: twǒlk, \"stone\", presumed dialectal variant of Seoul 돓〯 twǒlh, 'stone'). Less plausible etymologies include a derivation of Badukdok, referring to the playing pieces of the game, or a derivation from Chinese páizi (排子), meaning 'to arrange pieces'.\n\nOverview\n\nGo is an adversarial game between two players with the objective of capturing territory: that is, occupying and surrounding a larger total empty area of the board with one's stones than the opponent. As the game progresses, the players place stones on the board, creating stone \"formations\" and enclosing spaces. Once placed, stones are never moved on the board, but when \"captured\" are removed from the board. Stones are linked together into formations by being adjacent along the black lines, not on diagonals (of which there are none). Contests between opposing formations are often extremely complex and may result in the expansion, reduction, or wholesale capture and loss of formations and their enclosed empty spaces (or \"eyes\"). One essential aspect of the game is control of the sente (that is, controlling the offense, so that one's opponent is forced into defensive moves); this usually changes several times during play.\n\nInitially, the board is bare. Players take turns, placing one stone per turn. As the game proceeds, players try to link their stones together into \"living\" formations (meaning that they are permanently safe from capture), while threatening to capture their opponent's stones and formations. Thus, stones have both offensive and defensive characteristics, depending on the situation.\n\nAn essential aspect of the game is that any formation of stones needs to have, or be capable of making, at least two enclosed open points known as eyes, in order to preserve itself from being captured. A formation having two or more eyes cannot be captured, even after it is surrounded by the opponent on the outside, because each eye constitutes a liberty that must be filled by the opponent as the final step in capture. Once surrounded, a formation with a single eye can be captured on the next move, by one's opponent filling the eye and completely surrounding all stones in the formation; however, with two eyes, completely surrounding the formation is impossible, as filling one eye does not capture the formation, and instead would simply sacrifice the stone filling that eye. Thus, a formation having two or more eyes is said to be unconditionally alive, meaning that it can never be captured, while a group that cannot form two eyes is said to be dead and can be captured unless it is subsequently connected to a formation with a second eye.\n\nThe general strategy is to place stones to fence-off territory, attack the opponent's weak groups (trying to kill them so they will be removed), and always stay mindful of the life status of one's own groups. Situations where mutually opposing groups must capture each other or die are called capturing races, or semeai. In a capturing race, the group with more liberties will ultimately be able to capture the opponent's stones. Capturing races and the elements of life or death are the primary challenges of Go.\n\nIn the end game, players may pass rather than place a stone if they think there are no further opportunities for profitable play. The game ends when both players pass or when one player resigns. In general, to score the game, each player counts the number of unoccupied points surrounded by their stones and then subtracts the number of stones that were captured by the opponent. The player with the greater score (after adjusting for handicapping called komi) wins the game.\n\nIn the opening stages of the game, players typically establish groups of stones (or bases) near the corners and around the sides of the board, usually starting on the third or fourth line in from the board edge rather than at the very edge of the board. The edges and corners make it easier to develop groups which have better options for life (self-viability for a group of stones that prevents capture) and establish formations for potential territory. Players usually start near the corners, because establishing territory is easier with the aid of two edges of the board. Established corner opening sequences are called joseki and are often studied independently. However, in the mid-game, stone groups must also reach in towards the large central area of the board to capture more territory.\n\nDame are points that lie in between the boundary walls of black and white, and as such are considered to be of no value to either side. Seki are mutually alive pairs of white and black groups where neither has two eyes.\n\nKo (Chinese and Japanese: 劫) is a potentially indefinitely repeated stone-capture position. The rules do not allow a board position to be repeated. Therefore, any move which would restore the previous board position would not be allowed, and the next player would be forced to play somewhere else. If the play requires a strategic response by the first player, further changing the board, then the second player could \"retake the ko,\" and the first player would be in the same situation of needing to change the board before trying to take the ko back. And so on. Some of these ko fights may be important and decide the life of a large group, while others may be worth just one or two points. Some ko fights are referred to as picnic kos when only one side has a lot to lose. In Japanese, it is called a hanami ko.\n\nPlaying with others usually requires a knowledge of each player's strength, indicated by the player's rank (increasing from 30 kyu to 1 kyu, then 1 dan to 7 dan, then 1 dan pro to 9 dan pro). A difference in rank may be compensated by a handicap—e.g., Black may be allowed to place two or more stones on the board to compensate for White's greater strength. There are different rulesets (Korean, Japanese, Chinese, AGA, etc.), which are almost entirely equivalent, except for certain special-case positions and the method of scoring at the end.\n\nBasic concepts\n\nBasic strategic aspects include the following:\n\nConnection: Keeping one's own stones connected means that fewer groups need to make living shapes, and the player has fewer groups to defend.\n\nCut: Keeping opposing stones disconnected means that the opponent needs to defend and make living shape for more groups.\n\nStay alive: The simplest way to stay alive is to establish a foothold in the corner or along one of the sides. At a minimum, a group must have two eyes (separate open points) to be alive. An opponent cannot fill in either of two (or more) eyes in their opponent's formation, as any such move is suicidal: suicidal plays are prohibited.\n\nMutual life (seki) is better than dying: A situation in which neither player can play on a particular point without then allowing the other player to play at another point to capture. The most common example is that of adjacent groups that share their last few liberties—if either player plays in the shared liberties, they can reduce their own group to a single liberty (putting themselves in atari), allowing their opponent to capture it on the next move.\n\nDeath: A group that lacks living shape is eventually removed from the board as captured.\n\nInvasion: Establishing a new living formation in an area where one's opponent had dominance reduces one's opponent's score in proportion to the area one occupies.\n\nReduction: Placing a stone far enough into the opponent's area of influence to reduce the amount of territory they eventually get, but not so far that it can be cut off from friendly stones outside.\n\nSente: A play that forces one's opponent to respond (gote). A player who can regularly play sente has the initiative and can control the flow of the game.\n\nSacrifice: Allowing a group to die in order to carry out a play, or plan, in a more important area.\n\nThe strategy involved can become very abstract and complex. High-level players spend years improving their understanding of strategy, and a novice may play many hundreds of games against opponents before being able to win regularly.\n\nOne fundamental strategy, and learning technique, is to play one's stones in the position that one's opponent would wish to play their stone. Relatedly, switching positions (white changing to play black, and vice versa) is a useful way to learn how to see one's opponent's opportunities and strategy.\n\nStrategy\n\nStrategy deals with global influence, the interaction between distant stones, keeping the whole board in mind during local fights, and other issues that involve the overall game. It is therefore possible to allow a tactical loss when it confers a strategic advantage.\n\nNovices often start by randomly placing stones on the board, as if it were a game of chance. An understanding of how stones connect for greater power develops, and then a few basic common opening sequences may be understood. Learning the ways of life and death helps in a fundamental way to develop one's strategic understanding of weak groups. A player who both plays aggressively and can handle adversity is said to display kiai, or fighting spirit, in the game.\n\nOpening strategy\n\nIn the opening of the game, players usually play and gain territory in the corners of the board first, as the presence of two edges makes it easier for them to surround territory and establish the eyes they need. From a secure position in a corner, it is possible to lay claim to more territory by extending along the side of the board. The opening is the most theoretically difficult part of the game and takes a large proportion of professional players' thinking time. The first stone played at a corner of the board is generally placed on the third or fourth line from the edge. Players tend to play on or near the 4–4 star point during the opening. Playing nearer to the edge does not produce enough territory to be efficient, and playing further from the edge does not safely secure the territory.\n\nIn the opening, players often play established sequences called joseki, which are locally balanced exchanges; however, the joseki chosen should also produce a satisfactory result on a global scale. It is generally advisable to keep a balance between territory and influence. Which of these gets precedence is often a matter of individual taste.\n\nMiddlegame and endgame\n\nThe middle phase of the game is the most combative, and usually lasts for more than 100 moves. During the middlegame, the players invade each other's territories, and attack formations that lack the necessary two eyes for viability. Such groups may be saved or sacrificed for something more significant on the board. It is possible that one player may succeed in capturing a large weak group of the opponent's, which often proves decisive and ends the game by a resignation. However, matters may be more complex yet, with major trade-offs, apparently dead groups reviving, and skillful play to attack in such a way as to construct territories rather than kill.\n\nThe end of the middlegame and transition to the endgame is marked by a few features. Near the end of a game, play becomes divided into localized fights that do not affect each other, with the exception of ko fights, where previously, the central area of the board related to all parts of it. No large weak groups are still in serious danger. Moves can reasonably be attributed some definite value, such as 20 points or fewer, rather than simply being necessary to compete. Both players set limited objectives in their plans, in making or destroying territory, capturing or saving stones. These changing aspects of the game usually occur at much the same time, for strong players. In brief, the middlegame switches into the endgame when the concepts of strategy and influence need reassessment in terms of concrete final results on the board.\n\nRules\n\nAside from the order of play (alternating moves, Black moves first or takes a handicap) and scoring rules, there are essentially only two rules in Go:\n\nLiberty rule states that every stone remaining on the board must have at least one open point (a liberty) directly orthogonally adjacent (up, down, left, or right), or must be part of a connected group that has at least one such open point (liberty) next to it. Stones or groups of stones which lose their last liberty are removed from the board.\n\nRepetition Rule (the ko rule) states that a stone on the board must never immediately repeat a previous position of a captured stone, thus only a move elsewhere on the board is permitted that turn. Since without this rule such a pattern of the two players repeating their prior moves (capturing stones in same places) could continue indefinitely, this rule prevents a stalemate.\n\nAlmost all other information about how the game is played is heuristic, meaning it is learned information about how the patterns of the stones on the board function, rather than a rule. Other rules are specialized, as they come about through different rulesets, but the above two rules cover almost all of any played game.\n\nAlthough there are some minor differences between rulesets used in different countries, most notably in Chinese and Japanese scoring rules, these differences do not greatly affect the tactics and strategy of the game.\n\nExcept where noted, the basic rules presented here are valid independent of the scoring rules used. The scoring rules are explained separately. Go terms for which there is no ready English equivalent are commonly called by their Japanese names.\n\nBasic rules\n\nThe two players, Black and White, take turns placing stones of their color on the intersections of the board, one stone at a time. The usual board size is a 19×19 grid, but for beginners or for playing quick games, the smaller board sizes of 13×13 and 9×9 are also popular.\nThe board is empty to begin with. Black plays first unless given a handicap of two or more stones, in which case White plays first. The players may choose any unoccupied intersection to play on except for those forbidden by the ko and suicide rules (see below). Once played, a stone can never be moved and can be taken off the board only if it is captured. A player may pass their turn, declining to place a stone, though this is usually only done at the end of the game when both players believe nothing more can be accomplished with further play. When both players pass consecutively, the game ends and is then scored.\n\nLiberties and capture\n\nVertically and horizontally adjacent stones of the same color form a chain (also called a string or group), forming a discrete unit that cannot then be divided. Only stones connected to one another by the lines on the board create a chain; stones that are diagonally adjacent are not connected. Chains may be expanded by placing additional stones on adjacent intersections, and they can be connected together by placing a stone on an intersection that is adjacent to two or more chains of the same color.\n\nA vacant point adjacent to a stone, along one of the grid lines of the board, is called a liberty for that stone. Stones in a chain share their liberties. A chain of stones must have at least one liberty to remain on the board. When a chain is surrounded by"
 },
 {
  "title": "Go (Vertical Horizon album)",
  "revision_id": "1321224941",
  "matched_by": "title-minus-qualifier",
  "text": "Go is the fourth studio album by alternative rock band Vertical Horizon. The album, a follow-up to the band's double platinum Everything You Want, continues to expand upon the band's alternative and pop rock sound while moving into more hard rock directions as well. Recorded in early 2002, the album was ready as early as that August, but was instead delayed extensively due to restructuring at the band's label, RCA Records. The album was released over a year later on September 23, 2003. The singles off the album were \"I'm Still Here\", \"Forever\", and \"When You Cry\".\n\nThe album was well received by critics, who praised the album for being enjoyable despite not being especially inventive, but did not perform well commercially, with it not charting within the top 60 in its first week, and failing to achieve any RIAA certification. The album was later re-released as Go 2.0 in 2005 on Hybrid Recordings, with a new track \"Better When You're Not There\" and rearranged track listing.\n\nBackground\n\nAfter the band's release of their double platinum album Everything You Want in 1999, the band had initially intended to record a follow-up right away. However, the band ended up touring in support of Everything You Want for about two and a half years at request of their label. The band took a break from touring in early 2002 to move to Los Angeles and start recording sessions for Go.\n\nWriting and recording\n\nThe Go sessions began after commencing the two and a half years of touring in support of Everything You Want in early 2002. Despite the band's origins as a duo where Matthew Scannell and Keith Kane split singing and songwriting duties, the band dynamic shifted to Scannell providing the majority of both for Everything You Want, and all of both for Go. The process started with Scannell writing material in solitude, and then presenting his ideas to the rest of the band. How developed song ideas were varied by the track; some, such as \"Underwater\", was only a loose outline of a song, where as the track \"Forever\", was almost fully realized. Once ample ideas were in place, the band would enter the rehearsal space, where the band worked on arranging the album, and either expanding or trimming segments of tracks.\n\nUpon a couple of weeks of rehearsing, the band began recording alongside music producer John Shanks. The band first began by recording bass, drums, and guitars first, and then adding Scannel's vocals. However, the exception to the process was the track \"Forever\", which was added at the last minute in the initial recording sessions; where they started with Scannel's vocals and guitar, and then filled in the drums and bass afterwards. The band recorded a total of 16 songs for the album, but always envisioned paring it down to 11 or 12 for the final release.\n\nAn album's worth of material had been finished by August 2002. However, complications and delays arose due to issues with their record label, RCA Records, which was going through a major restructuring at the time. The band ended up under the jurisdiction the company's new CEO, Clive Davis. Davis did not approve of the band, with Scannell later recounting that \"...it’s safe to say we were not Clive’s favorite band...It was a torturous time.\" The combination of RCA's troubles and Davis's low opinion would delay the album over a year, until September 2003. In that time, Davis also requested the band come up with a stronger first single, so the band continued to work on further material, which resulted in the album's first single \"I'm Still Here\". The album's production was wrapped up with mixing by Ben Grosse and Chris Lord-Alge along with mastering by Ted Jensen.\n\nLyrical themes\n\nThe album's title reflects the band's \"just go for it\" mentality during the recording sessions. Part of the inspiration for this approach were the difficult Everything You Want sessions, where band members stressed out over every little detail of the album.\" The band resolved to go with their instinct rather that worrying excessively, something they felt they had honed through two and a half years of touring since the last time they had recorded in the studio.\" Scannell stated that, while none of the tracks overtly reference the September 11 attacks, the event did influence this mentality as well, having an important effect on his inspiration and emotions during the creation of the album.\"\n\n\"A lot of the themes in these songs are about taking control of your life and living it the way you want to live it, and acting and doing and not just talking and thinking about it. It's really important in the big sense in a post 9/11 world to make sure we all live our life in a way where we feel good about it. There are certainly messages within some of the songs at certain points on the album that deal with feelings of loss and those types of emotions, and also some feelings of, 'Hey, I want to get up and dust myself off and get on with my life. Both of those could be seen as viable and relevant reactions to 9/11.\"\n\nMusical style and composition\n\nThe album's sound is considered to be a continuation of Everything You Want's sound. Go has specifically been described as alternative rock and pop rock. Emphasis is placed on high production values with a highly polished and processed sound. A few tracks, notably \"Sunshine\" and \"One of You\", veer into a heavier, hard rock sound.\n\nMost of the tracks are arranged in a conventional verse-chorus structure, although the track's final chorus typically contain an expanded variation both lyrically and instrumentally. Verses commonly contain acoustic guitar, clean electric guitar tones, and a bass and drum lead beat, while choruses commonly erupt into heavier distorted guitar and heavy bass notes played, commonly creating a loud-soft dynamic. Tracks commonly contain an outro instrumental interlude as well. A few tracks, most notably \"Inside\", prominently feature orchestration in the form of a string section as well.\n\nRelease and promotion\n\nGo was released on September 23, 2003. The band was featured on television on multiple instances during the album's initial week of release, including appearances on CBS Weekend, CNN, Fox News and WGN. The band also performed at the Experience Music Project, which was later aired in October on VH1. The band also promoted the release through a North American tour through mid-November, a South-Eastern tour after that, and then many radio-sponsored performances in December.\n\nDespite the band's efforts, the album had a weak commercial impact, debuting at number 61 on the Billboard 200. The first single, \"I'm Still Here\", only peaked at number 17 on the Adult Top 40 as well. The band cited lack of support from their record label, with Scannell stating:\n\n\"Clive Davis had just taken over RCA Records and we knew he was not a fan of our band and certainly didn’t like me or our music much...We knew this album was going to virtually end up stillborn. I remember walking around to seven different record stores that day and finding only one copy of the new album.\"\n\nOn June 28, 2005, Hybrid Recordings, the label owned by Sony BMG, which bought out RCA in 2004 re-released Go as Go 2.0. The album featured a slightly altered track listing that included a previously unreleased track, \"Better When You're Not There\", and new cover art. After the re-release, \"Forever\" was released as a single; it reached no. 18 in the Billboard Adult Top 40 charts. The third and final single, \"When You Cry\", charted at No. 35. \"Forever\" also made the top 20 of the Billboard Hot AC chart, peaking at #17.\n\nThe album was also released in South Africa through Musketeer Records, where it charted in the top 10 album downloads from iTunes.\n\nReception\n\nReception for the album garnered mixed reactions by critics. AllMusic panned the album for sounding generic, stating it sounded like \"insipid radio filler\" and \"soundtracks for Pottery Barn\" and that it \"reaffirms their status as third-tier imitators\". Conversely, Alternative Addiction strongly praised the album for being \"great from beginning to end, proving that Vertical Horizon is one of the few bands that still not only makes great songs, but great albums...This album might not be \"Everything You Want\" but its still pretty damn good.\" The album's \"layered guitar-work\" was cited as a standout element. The Daily Star similarly praised the album for being \"a brilliant album with varied songs put together, with each of them fitting different occasions and moods.\" The Collegiate Times also praised the album for being \"rock that's not going to scare away the children, but at the same time has enough backbone to satisfy a U2 or Collective Soul fan\" and cited the track \"One of You\" as a standout track for fans of hard rock.\n\nTrack listing\n\nAll tracks are written by Matt Scannell.\n\nPersonnel\n\nTrack numbers correspond to the tracklisting of Go 2.0.\n\nCharts\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q37227",
  "label": "Go",
  "description": "programming language developed by Google and the open-source community",
  "aliases": [
   "Go programming language"
  ],
  "claims": {
   "P31": [
    "Q9143",
    "Q28922885",
    "Q12772052",
    "Q28919943",
    "Q21562092",
    "Q651794",
    "Q899523"
   ],
   "P361": [
    "Q7397"
   ],
   "P1889": [
    "Q28974885",
    "Q3109515"
   ]
  },
  "revision_id": "2567855228",
  "value_labels": {
   "Q9143": "programming language",
   "Q28922885": "procedural programming language",
   "Q12772052": "multi-paradigm programming language",
   "Q28919943": "concurrent programming language",
   "Q21562092": "imperative programming language",
   "Q651794": "compiled language",
   "Q899523": "object-based language",
   "Q7397": "software",
   "Q28974885": "go",
   "Q3109515": "Go!"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11413",
  "label": "go",
  "description": "board game for two players that originated in China more than 2,500 years ago",
  "aliases": [
   "goe",
   "igo",
   "baduk",
   "weiqi",
   "encircling game",
   "surrounding game"
  ],
  "claims": {
   "P31": [
    "Q1188693"
   ],
   "P279": [
    "Q131436",
    "Q18703581",
    "Q7858742"
   ],
   "P361": [
    "Q1751511"
   ],
   "P1889": [
    "Q219221",
    "Q1700280",
    "Q748139"
   ]
  },
  "revision_id": "2571398866",
  "value_labels": {
   "Q1188693": "mind sport",
   "Q131436": "board game",
   "Q18703581": "game on cell board",
   "Q7858742": "two-player game",
   "Q1751511": "four arts of the Chinese scholar",
   "Q219221": "Go",
   "Q1700280": "Ludus latrunculorum",
   "Q748139": "Othello"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5574677",
  "label": "Go",
  "description": "2003 studio album by Vertical Horizon",
  "aliases": [],
  "claims": {
   "P31": [
    "Q482994"
   ],
   "P361": [
    "Q65030734"
   ],
   "P1889": [
    "Q219221"
   ]
  },
  "revision_id": "2213538966",
  "value_labels": {
   "Q482994": "album",
   "Q65030734": "Vertical Horizon's albums in chronological order",
   "Q219221": "Go"
  },
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
  "ancestor_of": "Q37227",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28922885",
  "label": "procedural programming language",
  "description": "type of programming language",
  "aliases": [
   "procedural language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2560861293",
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28919943",
  "label": "concurrent programming language",
  "description": "type of programming language that support concurrent execution",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2362182514",
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q651794",
  "label": "compiled language",
  "description": "a programming language implemented with a compiler that translates source code into a binary executable form",
  "aliases": [
   "compiled",
   "compiled programming language"
  ],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143",
    "Q188267"
   ]
  },
  "revision_id": "2554781751",
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
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
  "ancestor_of": "Q37227",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q188267",
  "label": "programming paradigm",
  "description": "category of programming languages according to what methodology of designing and implementing programs their features support",
  "aliases": [],
  "claims": {
   "P279": [
    "Q28643",
    "Q962139"
   ]
  },
  "revision_id": "2538683798",
  "ancestor_of": "Q37227",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1188693",
  "label": "mind sport",
  "description": "game of skill based on intellectual ability",
  "aliases": [],
  "claims": {
   "P279": [
    "Q2847625",
    "Q50843134",
    "Q31629"
   ],
   "P527": [
    "Q1497658"
   ],
   "P1889": [
    "Q1054898",
    "Q1368898"
   ]
  },
  "revision_id": "2547521462",
  "ancestor_of": "Q11413",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q131436",
  "label": "board game",
  "description": "game that involves counters or pieces moved or placed on a pre-marked surface or \"board\", according to a set of rules",
  "aliases": [
   "boardgame"
  ],
  "claims": {
   "P31": [
    "Q63981612",
    "Q47728"
   ],
   "P279": [
    "Q3244175",
    "Q8205328",
    "Q17351672"
   ],
   "P1889": [
    "Q3244175"
   ]
  },
  "revision_id": "2567661415",
  "ancestor_of": "Q11413",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q18703581",
  "label": "game on cell board",
  "description": "board game which makes use of a grid of cells on which pieces are positioned or marks are made",
  "aliases": [
   "game on grid"
  ],
  "claims": {
   "P31": [
    "Q123563478"
   ],
   "P279": [
    "Q131436"
   ]
  },
  "revision_id": "2551716725",
  "ancestor_of": "Q11413",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7858742",
  "label": "two-player game",
  "description": "multiplayer game that is played by just two players (distinct from a solitaire game, which is played by only one player)",
  "aliases": [],
  "claims": {
   "P279": [
    "Q209075"
   ],
   "P1889": [
    "Q5252671"
   ]
  },
  "revision_id": "2558996553",
  "ancestor_of": "Q11413",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2847625",
  "label": "agility sport",
  "description": "",
  "aliases": [],
  "claims": {
   "P279": [
    "Q349"
   ],
   "P1889": [
    "Q1368898"
   ]
  },
  "revision_id": "2558866826",
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q50843134",
  "label": "intellectual competition",
  "description": "rivalry on an intellectual level between organisms, animals, individuals, groups, etc.",
  "aliases": [
   "academic competition"
  ],
  "claims": {
   "P279": [
    "Q23807345",
    "Q9081"
   ],
   "P1889": [
    "Q1368898"
   ]
  },
  "revision_id": "2283088167",
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q31629",
  "label": "type of sport",
  "description": "specific sport. Do not use with P279 (subclass of)",
  "aliases": [
   "types of sports",
   "sport type",
   "sports type",
   "sport types",
   "sports types"
  ],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q140458154",
    "Q125542526"
   ],
   "P1889": [
    "Q349",
    "Q2312410",
    "Q118498250"
   ]
  },
  "revision_id": "2520582709",
  "ancestor_of": "Q11413",
  "level": 2,
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
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q47728",
  "label": "hobby",
  "description": "regular leisure activity that is done usually for enjoyment",
  "aliases": [
   "public sport",
   "pastime",
   "passtime",
   "hobbies"
  ],
  "claims": {
   "P279": [
    "Q184872",
    "Q12737077"
   ]
  },
  "revision_id": "2516825333",
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3244175",
  "label": "tabletop game",
  "description": "game played on a flat surface",
  "aliases": [
   "table games",
   "tabletop games",
   "board and table game",
   "board and table games",
   "table and board games",
   "board, and table game",
   "board, and table games",
   "table, and board game",
   "table, and board games"
  ],
  "claims": {
   "P279": [
    "Q2424752",
    "Q8205328",
    "Q14947863"
   ],
   "P1889": [
    "Q131436"
   ]
  },
  "revision_id": "2565025761",
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q8205328",
  "label": "artificial physical object",
  "description": "physical object made or shaped by humans",
  "aliases": [
   "artifact",
   "man-made physical object",
   "artefact",
   "human-made physical object",
   "non-natural physical object",
   "physical artefact"
  ],
  "claims": {
   "P31": [
    "Q111360549"
   ],
   "P279": [
    "Q223557",
    "Q16686448",
    "Q386724",
    "Q136490012",
    "Q141756646"
   ],
   "P361": [
    "Q11042"
   ],
   "P1889": [
    "Q220659",
    "Q231515",
    "Q16686448",
    "Q136490012"
   ]
  },
  "revision_id": "2567164850",
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q123563478",
  "label": "board game type by mechanic",
  "description": "",
  "aliases": [],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q66152509"
   ]
  },
  "revision_id": "2421029708",
  "ancestor_of": "Q11413",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q209075",
  "label": "multiplayer game",
  "description": "game with multiple players",
  "aliases": [],
  "claims": {
   "P279": [
    "Q11410"
   ],
   "P1889": [
    "Q6895044"
   ]
  },
  "revision_id": "2493999060",
  "ancestor_of": "Q11413",
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
  "ancestor_of": "Q5574677",
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
  "ancestor_of": "Q5574677",
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
  "ancestor_of": "Q5574677",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-15317305-n",
  "lemmas": [
   "go",
   "spell",
   "tour",
   "turn"
  ],
  "gloss": "a time period for working (after which you will be relieved by someone else)",
  "examples": [
   "it's my go",
   "a spell of work"
  ],
  "relations": {
   "hypernym": [
    "oewn-15317037-n"
   ]
  },
  "relation_targets": {
   "oewn-15317037-n": "shift, work shift, duty period"
  }
 },
 {
  "synset": "oewn-02681592-n",
  "lemmas": [
   "Adam",
   "ecstasy",
   "XTC",
   "go",
   "disco biscuit",
   "cristal",
   "X",
   "hug drug"
  ],
  "gloss": "street names for methylenedioxymethamphetamine",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-03761713-n"
   ]
  },
  "relation_targets": {
   "oewn-03761713-n": "methylenedioxymethamphetamine, MDMA"
  }
 },
 {
  "synset": "oewn-00788715-n",
  "lemmas": [
   "crack",
   "fling",
   "go",
   "pass",
   "whirl",
   "offer"
  ],
  "gloss": "a usually brief attempt",
  "examples": [
   "he took a crack at it",
   "I gave it a whirl"
  ],
  "relations": {
   "hypernym": [
    "oewn-00787849-n"
   ]
  },
  "relation_targets": {
   "oewn-00787849-n": "attempt, effort, endeavor"
  }
 },
 {
  "synset": "oewn-00505336-n",
  "lemmas": [
   "go",
   "go game"
  ],
  "gloss": "a board game for two players who place counters on a grid; the object is to surround and so capture the opponent's counters",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-00503426-n"
   ]
  },
  "relation_targets": {
   "oewn-00503426-n": "board game"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~
