# Skills Lexicon pilot, grounded run: message 4 of 13 (chunk 03, 2 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "03", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-03.jsonl`. Otherwise send one code block marked `jsonl` holding the 2 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 2: C (`a0h79b66kq`)

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
[
 {
  "title": "C",
  "revision_id": "1378214665",
  "matched_by": "title",
  "text": "C (minuscule: c) is the third letter of the Latin alphabet, used in the modern English alphabet, the alphabets of other western European languages and others worldwide. Its name in English is cee (pronounced /ˈsiː/ ), plural cees.\n\nHistory\n\n\"C\" comes from the same letter as \"G\". The Semites named it gimel. The sign is possibly adapted from an Egyptian hieroglyph for a staff sling, which may have been the meaning of the name gimel. Another possibility is that it depicted a camel, the Semitic name for which was gamal. Barry B. Powell, a specialist in the history of writing, states \"It is hard to imagine how gimel = \"camel\" can be derived from the picture of a camel (it may show his hump, or his head and neck!)\".\n\nIn the Etruscan language, plosive consonants had no contrastive voicing, so the Greek 'Γ' (Gamma) was adopted into the Etruscan alphabet to represent /k/. Already in the Western Greek alphabet, Gamma first took a '' form in Early Etruscan, then '' in Classical Etruscan. In Latin, it eventually took the 'c' form in Classical Latin. In the earliest Latin inscriptions, the letters 'c k q' were used to represent the sounds /k/ and /ɡ/ (which were not differentiated in writing). Of these, 'q' was used to represent /k/ or /ɡ/ before a rounded vowel, 'k' before 'a', and 'c' elsewhere. During the 3rd century BC, a modified character was introduced for /ɡ/, and 'c' itself was retained for /k/. The use of 'c' (and its variant 'g') replaced most usages of 'k' and 'q'. Hence, in the classical period and after, 'g' was treated as the equivalent of Greek gamma, and 'c' as the equivalent of kappa; this shows in the romanization of Greek words, as in 'ΚΑΔΜΟΣ', 'ΚΥΡΟΣ', and 'ΦΩΚΙΣ' came into Latin as 'cadmvs', 'cyrvs' and 'phocis', respectively.\n\nOther alphabets have letters homoglyphic to 'c' but not analogous in use and derivation, like the Cyrillic letter Es (С, с) which derives from the lunate sigma.\n\nLater use\n\nWhen the Roman alphabet was introduced into Britain, ⟨c⟩ represented only /k/, and this value of the letter has been retained in loanwords to all the insular Celtic languages: in Welsh, Irish, and Gaelic, ⟨c⟩ represents only /k/. The Old English Latin-based writing system was learned from the Celts, apparently of Ireland; hence, ⟨c⟩ in Old English also originally represented /k/; the Modern English words kin, break, broken, thick, and seek all come from Old English words written with ⟨c⟩: cyn, brecan, brocen, þicc, and séoc. However, during the course of the Old English period, /k/ before front vowels (/e/ and /i/) was palatalized, having changed by the tenth century to [tʃ], though ⟨c⟩ was still used, as in cir(i)ce, wrecc(e)a. On the continent, meanwhile, a similar phonetic change before the same two vowels had also been going on in almost all of the Romance languages (for example, in Italian).\n\nIn Vulgar Latin, /k/ became palatalized to [tʃ] in Italy and Dalmatia; in France and the Iberian Peninsula, it became [ts]. Yet for these new sounds, ⟨c⟩ was still used before the letters ⟨e⟩ and ⟨i⟩. The letter thus represented two distinct values. Subsequently, the Latin phoneme /k/ (spelled ⟨qv⟩) de-labialized to /k/, meaning that the various Romance languages had /k/ before front vowels. In addition, Norman used the letter ⟨k⟩ so that the sound /k/ could be represented by either ⟨k⟩ or ⟨c⟩, the latter of which could represent either /k/ or /ts/ depending on whether it preceded a front vowel letter or not. The convention of using both ⟨c⟩ and ⟨k⟩ was applied to the writing of English after the Norman Conquest, causing a considerable re-spelling of the Old English words. Thus, while Old English candel, clif, corn, crop, and cú, remained unchanged, cent, cǣᵹ (cēᵹ), cyng, brece, and sēoce, were now (without any change of sound) spelled Kent, keȝ, kyng, breke, and seoke; even cniht ('knight') was subsequently changed to kniht, and þic ('thick') was changed to thik or thikk. The Old English ⟨cw⟩ was also at length displaced by the French ⟨qu⟩ so that the Old English cwēn ('queen') and cwic ('quick') became Middle English quen and quik, respectively.\n\nThe sound [tʃ], to which Old English palatalized /k/ had advanced, also occurred in French, chiefly from Latin /k/ before ⟨a⟩. In French, it was represented by the digraph ⟨ch⟩, as in champ (from Latin camp-um), and this spelling was introduced into English: the Hatton Gospels, written c. 1160, have in Matt. i-iii, child, chyld, riche, and mychel, for the cild, rice, and mycel of the Old English version whence they were copied. In these cases, the Old English ⟨c⟩ gave way to ⟨k⟩, ⟨qu⟩ and ⟨ch⟩; on the other hand, ⟨c⟩ in its new value of /ts/ appeared largely in French words like processiun, emperice, and grace and was also substituted for ⟨ts⟩ in a few Old English words, as miltse, bletsien, in early Middle English milce, blecien. By the end of the thirteenth century, both in France and England, this sound /ts/ was de-affricated to /s/; and from that time, ⟨c⟩ has represented /s/ before front vowels either for etymological reasons, as in lance, cent, or to avoid the ambiguity due to the \"etymological\" use of ⟨s⟩ for /z/, as in ace, mice, once, pence, defence.\n\nThus, to show etymology, English spelling has advise, devise (instead of *advize, *devize), while advice, device, dice, ice, mice, twice, etc., do not reflect etymology; example has extended this to hence, pence, defence, etc., where there is no etymological reason for using ⟨c⟩. Former generations also wrote sence for sense. Hence, today, the Romance languages and English have a common feature inherited from Vulgar Latin spelling conventions where ⟨c⟩ takes on either a \"hard\" or \"soft\" value depending on the following letter.\n\nUse in writing systems\n\nEnglish\n\nIn English orthography, ⟨c⟩ generally represents the \"soft\" value of /s/ before the letters ⟨e⟩ (including the Latin-derived digraphs ⟨ae⟩ and ⟨oe⟩, or the corresponding ligatures ⟨æ⟩ and ⟨œ⟩), ⟨i⟩, and ⟨y⟩, and a \"hard\" value of /k/ before any other letters or at the end of a word. However, there are a number of exceptions in English: \"soccer\", \"celt\" and \"sceptic\" are words that have /k/ where /s/ would be expected. The \"soft\" ⟨c⟩ may represent the /ʃ/ sound in the digraph ⟨ci⟩ when this precedes a vowel, as in the words 'delicious' and 'appreciate', and also in the word \"ocean\" and its derivatives.\n\nThe digraph ⟨ch⟩ most commonly represents /tʃ/, but can also represent /k/ (mainly in words of Greek origin) or /ʃ/ (mainly in words of French origin). For some dialects of English, it may also represent /x/ in words like loch, while other speakers pronounce the final sound as /k/. The trigraph ⟨tch⟩ always represents /tʃ/. The digraph ⟨ck⟩ is often used to represent the sound /k/ after short vowels, like in \"wicket\".\n\nC is the twelfth most frequently used letter in the English language (after E, T, A, O, I, N, S, H, R, D, and L), with a frequency of about 2.8% in words.\n\nOther languages\n\nIn the Romance languages French, Spanish, Italian, Romanian, Catalan, and Portuguese, ⟨c⟩ generally has a \"hard\" value of /k/ and a \"soft\" value whose pronunciation varies by language. In French, Portuguese, Catalan, and Spanish from Latin America and some places in Spain, the soft ⟨c⟩ value is /s/ as it is in English. In the Spanish spoken in most of Spain, the soft ⟨c⟩ is a voiceless dental fricative /θ/. In Italian and Romanian, the soft ⟨c⟩ is [t͡ʃ].\n\nGermanic languages usually use ⟨c⟩ for Romance loans or digraphs, such as ⟨ch⟩ and ⟨ck⟩, but the rules vary across languages. Of all the Germanic languages, only English uses the initial ⟨c⟩ in native Germanic words like come. Other than English, Dutch uses ⟨c⟩ the most, for most Romance loans and the digraph ⟨ch⟩. German uses ⟨c⟩ in the digraphs ⟨ch⟩ and ⟨ck⟩, and the trigraph ⟨sch⟩, but by itself only in unassimilated loanwords and proper names. Danish keeps soft ⟨c⟩ in Romance words but changes hard ⟨c⟩ to ⟨k⟩. Swedish has the same rules for soft and hard ⟨c⟩ as Danish, and also uses ⟨c⟩ in the digraph ⟨ck⟩ and the very common word och, \"and\". Norwegian, Afrikaans, and Icelandic are the most restrictive, replacing all cases of ⟨c⟩ with ⟨k⟩ or ⟨s⟩, and reserving ⟨c⟩ for unassimilated loanwords and names.\n\nAll Balto-Slavic languages that use the Latin alphabet, as well as Albanian, Hungarian, Pashto, several Sami languages, Esperanto, Ido, Interlingua, and Americanist phonetic notation (and those aboriginal languages of North America whose practical orthography derives from it), use ⟨c⟩ to represent /t͡s/, the voiceless alveolar or voiceless dental sibilant affricate. In Hanyu Pinyin, the standard romanization of Mandarin Chinese, the letter represents an aspirated version of this sound, /t͡s/.\n\nAmong non-European languages that have adopted the Latin alphabet, ⟨c⟩ represents a variety of sounds. Yup'ik, Indonesian, Malay, and a number of African languages such as Hausa, Fula, and Manding share the soft Italian value of /t͡ʃ/. In Azeri, Crimean Tatar, Kurmanji Kurdish, and Turkish, ⟨c⟩ stands for the voiced counterpart of this sound, the voiced postalveolar affricate /d͡ʒ/. In Yabem and similar languages, such as Bukawa, ⟨c⟩ stands for a glottal stop /ʔ/. Xhosa and Zulu use this letter to represent the click /ǀ/. In some other African languages, such as Berber languages, ⟨c⟩ is used for /ʃ/. In Fijian, ⟨c⟩ stands for a voiced dental fricative /ð/, while in Somali it has the value of /ʕ/.\n\nThe letter ⟨c⟩ is also used as a transliteration of Cyrillic ⟨ц⟩ in the Latin forms of Serbian, Macedonian, and sometimes Ukrainian, along with the digraph ⟨ts⟩.\n\nOther systems\n\nAs a phonetic symbol, lowercase ⟨c⟩ is the International Phonetic Alphabet (IPA) and X-SAMPA symbol for the voiceless palatal plosive, and capital ⟨C⟩ is the X-SAMPA symbol for the voiceless palatal fricative.\n\nDigraphs\n\nThere are several common digraphs with ⟨c⟩, the most common being ⟨ch⟩, which in some languages (such as German) is far more common than ⟨c⟩ alone. ⟨ch⟩ takes various values in other languages.\n\nAs in English, ⟨ck⟩, with the value /k/, is often used after short vowels in other Germanic languages such as German and Swedish (other Germanic languages, such as Dutch and Norwegian, use ⟨kk⟩ instead). The digraph ⟨cz⟩ is found in Polish and ⟨cs⟩ in Hungarian, representing /t͡ʂ/ and /t͡ʃ/ respectively. The digraph ⟨sc⟩ represents /ʃ/ in Old English, Italian, and a few languages related to Italian (where this only happens before front vowels, while otherwise it represents /sk/). The trigraph ⟨sch⟩ represents /ʃ/ in German.\n\nOther uses\n\nIn the hexadecimal (base 16) numbering system, C is a number that corresponds to the number 12 in decimal (base 10) counting.\n\nIn the Roman numeral system, C represents 100.\n\nUnit prefix c, meaning one hundredth.\n\nRelated characters\n\nAncestors, descendants and siblings\n\n⟨𐤂⟩ : Semitic letter Gimel, from which the following symbols originally derive:\n\n⟨Γ⟩ ⟨γ⟩ : Greek letter Gamma, from which ⟨C⟩ derives\n\n⟨G⟩ ⟨g⟩ : Latin letter ⟨G⟩, which is derived from Latin ⟨C⟩\n\n⟨Ȝ⟩ ⟨ȝ⟩ : Latin letter Yogh, which is derived from Latin ⟨G⟩\n\nPhonetic alphabet symbols related to ⟨C⟩:\n\n⟨ɕ⟩ : Small ⟨c⟩ with curl\n\n⟨ʗ⟩ : Stretched ⟨c⟩\n\n⟨𝼏⟩ : Stretched ⟨c⟩ with curl – Used by Douglas Beach for a nasal click in his phonetic description of Khoekhoe.\n\n⟨𝼝⟩ : Small letter ⟨c⟩ with retroflex hook – Para-IPA version of the IPA retroflex tʂ.\n\n⟨ꟲ⟩ : Modifier letter capital ⟨c⟩ – Used to mark tone for the Chatino orthography in Oaxaca, Mexico; used as a generic transcription for a falling tone; also used in para-IPA notation.\n\n⟨ᶜ⟩ : Modifier letter small c\n\n⟨ᶝ⟩ : Modifier letter small ⟨c⟩ with curl\n\n⟨ᴄ⟩ : Small capital ⟨c⟩ is used in the Uralic Phonetic Alphabet.\n\n⟨Ꞔ⟩ ⟨ꞔ⟩ : ⟨C⟩ with palatal hook, used for writing Mandarin Chinese using the early draft version of pinyin romanization during the mid-1950s.\n\n⟨C⟩ with diacritics: Ć ć Ĉ ĉ Č č Ċ ċ Ḉ ḉ Ƈ ƈ C̈ c̈ Ȼ ȼ Ç ç Ꞔ ꞔ Ꞓ ꞓ\n\n⟨Ↄ⟩ ⟨ↄ⟩ : Claudian letters\n\nDerived ligatures, abbreviations, signs and symbols\n\n© : copyright symbol\n\n°C : degree Celsius\n\n¢ : cent\n\n₡ : colón (currency)\n\n₢ : Brazilian cruzeiro (currency)\n\n₵ : Ghana cedi (currency)\n\n₠ : European Currency Unit CE\n\n : blackboard bold C, denoting the complex numbers\n\nℭ : blackletter C\n\nꜾ ꜿ : Medieval abbreviation for Latin syllables con- and com-, and Portuguese -us and -os.\n\n𝾐: Historical mathematical symbol for the cube of the unknown (U+1DF90 𝾐 LATIN SMALL LETTER C WITH LOW SLASH)\n\n𝾑: Historical mathematical symbol for the square of the unknown (U+1DF91 𝾑 LATIN SMALL LETTER C WITH LOOPED CEDILLA)\n\n𝾒: Historical mathematical symbol for the cube of the unknown (U+1DF92 𝾒 LATIN SMALL LETTER C WITH RIGHT LOOP)\n\nOther representations\n\nComputing \n\nThe Latin letters ⟨C⟩ and ⟨c⟩ have Unicode encodings U+0043 C LATIN CAPITAL LETTER C and U+0063 c LATIN SMALL LETTER C. These are the same code points as those used in ASCII and ISO 8859. There are also precomposed character encodings for ⟨C⟩ and ⟨c⟩ with diacritics, for most of those listed above; the remainder are produced using combining diacritics.\n\nVariant forms of the letter have unique code points for specialist use: the alphanumeric symbols set in mathematics and science, voiceless palatal sounds in linguistics, and halfwidth and fullwidth forms for legacy CJK font compatibility. The Cyrillic homoglyph of the Latin ⟨C⟩ has a separate encoding: U+0421 С CYRILLIC CAPITAL LETTER ES.\n\nOther\n\nSee also"
 },
 {
  "title": "C (programming language)",
  "revision_id": "1378277749",
  "matched_by": "title",
  "text": "C is a general-purpose programming language created in 1972 by Dennis Ritchie. By design, C gives programmers relatively direct access to the features of typical CPU architectures, customized for the target instruction set. It has been and continues to be used to implement operating systems (especially kernels), device drivers, and protocol stacks, though its use in application software is decreasing. C is used on computers ranging from supercomputers to microcontrollers and embedded systems.\n\nC was initially developed as a successor to the B programming language at Bell Labs by Ritchie between 1972 and 1973. Its initial purpose was to construct utilities running on Unix, and was later applied to re-implementing the kernel of the Unix operating system. During the 1980s, C gradually gained popularity, leading to it becoming one of the most widely used programming languages, with C compilers available for practically all modern computer architectures and operating systems. The book The C Programming Language, co-authored by the original language designer, served for many years as the de facto standard for the language. C has been standardized since 1989 by the American National Standards Institute (ANSI) and, subsequently, jointly by the International Organization for Standardization (ISO) and the International Electrotechnical Commission (IEC).\n\nC is an imperative procedural language, supporting structured programming, lexical variable scope, and recursion, with a static type system. It was designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. Despite its low-level capabilities, the language was designed to encourage cross-platform programming. A standards-compliant C program written with portability in mind can be compiled for a wide variety of computer platforms and operating systems with few changes to its source code.\n\nAlthough neither C nor its standard library provide some popular features found in other languages, it is flexible enough to support them. For example, object orientation and garbage collection are provided by external libraries GLib Object System and Boehm garbage collector, respectively.\n\nSince 2000, C has typically ranked as the most or second-most popular language in the TIOBE index.\n\nCharacteristics\n\nC is an imperative, procedural language with a free-form source layout. Statements are terminated by semicolons and grouped into blocks using curly braces. All executable code is contained in functions rather than top-level statements. The language has a relatively small number of keywords, and user-defined identifiers are not distinguished from keywords by any sigil.\n\nParameters are passed by value; pass-by-reference is achieved with pointers. A function's return value may be ignored, and while a function cannot normally be nested inside another function, some translators support this. C supports recursion, and run-time polymorphism may be achieved using function pointers. Control flow is provided through constructs such as if, for, do, while, and switch. The language offers arithmetic; bitwise; and logical operators including +, +=, ++, &, ||, and multiple assignments may be performed in a single statement. A variable declared inside a block is accessible only within that block and only below its declaration.\n\nData typing is weakly enforced and static, with implicit conversion between primitive types. User-defined types allow aliasing of type specifiers. Arrays are defined and accessed with square-bracket notation, for example month[11]. User-defined structure types let related data elements be passed and copied as a unit, though two structures cannot be compared without custom code to compare each field. Unions support overlapping members, allowing multiple data types to share the same memory location, and enumeration types support aliasing integer values. C lacks a dedicated string type but provides syntax for null-terminated strings, with associated handling in its standard library.\n\nThe language supports low-level access to computer memory via pointers, procedure-like constructs in the form of functions returning void, and dynamic memory allocation through standard library functions. It includes the C preprocessor for macro definition, source-file inclusion, and conditional compilation. Modularity is supported by processing files separately, with visibility controlled through the static and extern attributes. Functionality is minimized in the core language, with relatively complex features such as I/O, string manipulation, and mathematical functions being provided through standard libraries. The resulting compiled code has relatively straightforward requirements of the underlying platform, making C desirable for operating and embedded systems.\n\n\"Hello, world\" example\n\nThe \"Hello, World!\" program example that appeared in the first edition of K&R has become the model for an introductory program in most programming textbooks. The program prints \"hello, world\" to the standard output.\n\nThe original version was:\n\nmain()\n{\n printf(\"hello, world\\n\");\n}\n\nA more modern version is:\n\n#include <stdio.h>\n\nint main(void)\n{\n printf(\"hello, world\\n\");\n}\n\nThe first line is a preprocessor directive, indicated by #include, which causes the preprocessor to replace that line of code with the text of the stdio.h header file, which contains declarations for input and output functions including printf. The angle brackets around stdio.h indicate that the header file can be located using a search strategy that selects header files provided with the compiler over files with the same name that may be found in project-specific directories.\n\nThe next code line declares the entry point function main. The run-time environment calls this function to begin program execution. The type specifier int indicates that the function returns an integer value. The void parameter list indicates that the function consumes no arguments. The run-time environment actually passes two arguments (typed int and char *[]), but this implementation ignores them. The ISO C standard (section 5.1.2.2.1) requires syntax that either is void or these two arguments – a special treatment not afforded to other functions.\n\nThe opening curly brace indicates the beginning of the code that defines the function.\n\nThe next line of code calls (diverts execution to) the C standard library function printf with the address of the first character of a null-terminated string specified as a string literal. The text \\n is an escape sequence that denotes the newline character which when output in a terminal results in moving the cursor to the beginning of the next line. Even though printf returns an int value, it is silently discarded. The semicolon ; terminates the call statement.\n\nThe closing curly brace indicates the end of the main function. Prior to C99, an explicit return 0; statement was required at the end of main function, but since C99, the main function (as being the initial function call) implicitly returns 0 upon reaching its final closing curly brace.\n\nHistory\n\nEarly developments\n\nThe origin of C is closely tied to the development of the Unix operating system, originally implemented in assembly language on a PDP-7 by Dennis Ritchie and Ken Thompson, incorporating several ideas from colleagues. Eventually, they decided to port the operating system to a PDP-11. The original PDP-11 version of Unix was also developed in assembly language.\n\nB\n\nThompson wanted a programming language for developing utilities for the new platform. He first tried writing a Fortran compiler, but he soon gave up the idea and instead created a cut-down version of the recently developed systems programming language called BCPL. The official description of BCPL was not available at the time, and Thompson modified the syntax to be less 'wordy' and similar to a simplified ALGOL known as SMALGOL. He called the result B, describing it as \"BCPL semantics with a lot of SMALGOL syntax\". Like BCPL, B had a bootstrapping compiler to facilitate porting to new machines. Ultimately, few utilities were written in B because it was too slow and could not take advantage of PDP-11 features such as byte addressability.\n\nUnlike BCPL's // comment marking comments up to the end of the line, B adopted /* comment */ as the comment delimiter, more akin to PL/1, and allowing comments to appear in the middle of lines. (BCPL's comment style would be reintroduced in C++.)\n\nNew B and first C release\n\nIn 1971, Ritchie started to improve B, to use the features of the more-powerful PDP-11. A significant addition was a character data type. He called this New B (NB). Thompson started to use NB to write the Unix kernel, and his requirements shaped the direction of the language development.\n\nThrough to 1972, richer types were added to the NB language. NB had arrays of int and char, and to these types were added pointers, the ability to generate pointers to other types, arrays of all types, and types to be returned from functions. Arrays within expressions were effectively treated as pointers. A new compiler was written, and the language was renamed C.\n\nThe C compiler and some utilities made with it were included in Version 2 Unix, which is also known as Research Unix.\n\nStructures and Unix kernel re-write\n\nAt Version 4 Unix, released in November 1973, the Unix kernel was extensively re-implemented in C. By this time, the C language had acquired some powerful features such as struct types.\n\nThe preprocessor was introduced around 1973 at the urging of Alan Snyder and also in recognition of the usefulness of the file-inclusion mechanisms available in BCPL and PL/I. Its original version provided only included files and simple string replacements: #include and #define of parameterless macros. Soon after that, it was extended, mostly by Mike Lesk and then by John Reiser, to incorporate macros with arguments and conditional compilation.\n\nUnix was one of the first operating system kernels implemented in a language other than assembly. Earlier instances include the Multics system (which was written in PL/I) and Master Control Program (MCP) for the Burroughs B5000 (which was written in ALGOL) in 1961. In and around 1977, Ritchie and Stephen C. Johnson made further changes to the language to facilitate portability of the Unix operating system. Johnson's Portable C Compiler served as the basis for several implementations of C on new platforms.\n\nK&R C\n\nIn 1978, Brian Kernighan and Dennis Ritchie published the first edition of The C Programming Language. Known as K&R from the initials of its authors, the book served for many years as an informal specification of the language. The version of C that it describes is commonly referred to as \"K&R C\". As this was released in 1978, it is now also referred to as C78. The second edition of the book covers the later ANSI C standard, described below.\n\nK&R introduced several language features:\n\nStandard I/O library\n\nlong int data type\n\nunsigned int data type\n\nCompound assignment operators of the form =op (such as =-) were changed to the form op= (that is, -=) to remove the semantic ambiguity created by constructs such as i=-10, which had been interpreted as i =- 10 (decrement i by 10) instead of the possibly intended i = -10 (let i be −10).\n\nEven after the publication of the 1989 ANSI standard, for many years K&R C was still considered the \"lowest common denominator\" to which C programmers restricted themselves when maximum portability was desired, since many older compilers were still in use, and because carefully written K&R C code can be legal Standard C as well.\n\nAlthough later versions of C require functions to have an explicit type declaration, K&R C only requires functions that return a type other than int to be declared before use. Functions used without prior declaration were presumed to return int.\n\nFor example:\n\nlong long_function();\n\ncalling_function()\n{\n long longvar;\n register intvar;\n longvar = long_function();\n if (longvar > 1)\n intvar = 0;\n else\n intvar = int_function();\n return intvar;\n}\n\nThe declaration of long_function() (on line 1) is required since it returns long; not int. Function int_function can be called (line 11) even though it is not declared since it returns int. Also, variable intvar does not need to be declared as type int since that is the default type for register keyword.\n\nSince function declarations did not include information about arguments, type checks were not performed, although some compilers would issue a warning if different calls to a function used different numbers or types of arguments. Tools such as Unix's lint utility were developed that (among other things) checked for consistency of function use across multiple source files.\n\nIn the years following the publication of K&R C, several features were added to the language, supported by compilers from AT&T (in particular PCC) and other vendors. These included:\n\nvoid functions; functions returning no value\n\nFunctions returning struct or union types\n\nAssignment for struct variables\n\nEnumerated types\n\nThe popularity of the language, lack of agreement on standard library interfaces, and lack of compliance to the K&R specification, led to standardization efforts.\n\nANSI C and ISO C\n\nDuring the late 1970s and 1980s, versions of C were implemented for a wide variety of mainframe computers, minicomputers, and microcomputers, including the IBM PC, as its popularity increased significantly.\n\nIn 1983 the American National Standards Institute (ANSI) formed a committee, X3J11, to establish a standard specification of C. X3J11 based the C standard on the Unix implementation; however, the non-portable portion of the Unix C library was handed off to the IEEE working group 1003 to become the basis for the 1988 POSIX standard. In 1989, the C standard was ratified as ANSI X3.159-1989 \"Programming Language C\". This version of the language is often referred to as ANSI C, Standard C, or sometimes C89.\n\nIn 1990 the ANSI C standard (with formatting changes) was adopted by the International Organization for Standardization (ISO) as ISO/IEC 9899:1990, which is sometimes called C90. Therefore, the terms \"C89\" and \"C90\" refer to the same programming language.\n\nANSI, like other national standards bodies, no longer develops the C standard independently, but defers to the international C standard, maintained by the working group ISO/IEC JTC1/SC22/WG14. National adoption of an update to the international standard typically occurs within a year of ISO publication.\n\nOne of the aims of the C standardization process was to produce a superset of K&R C, incorporating many of the subsequently introduced unofficial features. The standards committee also included several additional features such as function prototypes (borrowed from C++), void pointers, support for international character sets and locales, and preprocessor enhancements. Although the syntax for parameter declarations was augmented to include the style used in C++, the K&R interface continued to be permitted, for compatibility with existing source code.\n\nC89 is supported by current C compilers, and most modern C code is based on it. Any program written only in Standard C and without any hardware-dependent assumptions will run correctly on any platform with a conforming C implementation, within its resource limits. Without such precautions, programs may compile only on a certain platform or with a particular compiler, due, for example, to the use of non-standard libraries, such as GUI libraries, or to a reliance on compiler- or platform-specific attributes such as the exact size of data types and byte endianness.\n\nIn cases where code must be compilable by either standard-conforming or K&R C-based compilers, the __STDC__ macro can be used to split the code into Standard and K&R sections to prevent the use on a K&R C-based compiler of features available only in Standard C.\n\nAfter the ANSI/ISO standardization process, the C language specification remained relatively static for several years. In 1995, Normative Amendment 1 to the 1990 C standard (ISO/IEC 9899/AMD1:1995, known informally as C95) was published, to correct some details and to add more extensive support for international character sets.\n\nC99\n\nThe C standard was further revised in the late 1990s, leading to the publication of ISO/IEC 9899:1999 in 1999, which is commonly referred to as \"C99\". It has since been amended three times by Technical Corrigenda.\n\nC99 introduced several new features, including inline functions, several new data types (including long long int and a complex type to represent complex numbers), variable-length arrays and flexible array members, improved support for IEEE 754 floating point, support for variadic macros (macros of variable arity), and support for one-line comments beginning with //, as in BCPL or C++. Many of these had already been implemented as extensions in several C compilers.\n\nC99 is for the most part backward compatible with C90, but is stricter in some ways; in particular, a declaration that lacks a type specifier no longer has int implicitly assumed. A standard macro __STDC_VERSION__ is defined with value 199901L to indicate that C99 support is available. GCC, Solaris Studio, and other C compilers now support many or all of the new features of C99. The C compiler in Microsoft Visual C++, however, implements the C89 standard and those parts of C99 that are required for compatibility with C++11.\n\nIn addition, the C99 standard requires support for identifiers using Unicode in the form of escaped characters (e.g. \\u0040 or \\U0001f431) and suggests support for raw Unicode names.\n\nC11\n\nWork began in 2007 on another revision of the C standard, informally called \"C1X\" until its official publication of ISO/IEC 9899:2011 on December 8, 2011. The C standards committee adopted guidelines to limit the adoption of new features that had not been tested by existing implementations.\n\nThe C11 standard adds numerous new features to C and the library, including type generic macros, anonymous structures, improved Unicode support, atomic operations, multi-threading, and bounds-checked functions. It also makes some portions of the existing C99 library optional, and improves compatibility with C++. The standard macro __STDC_VERSION__ is defined as 201112L to indicate that C11 support is available.\n\nC17\n\nC17 is an informal name for ISO/IEC 9899:2018, a standard for the C programming language published in June 2018. It introduces no new language features, only technical corrections, and clarifications to defects in C11. The standard macro __STDC_VERSION__ is defined as 201710L to indicate that C17 support is available.\n\nC23\n\nC23 is an informal name for the current major C language standard revision. It was known as \"C2X\" through most of its development. It builds on past releases, introducing features like new keywords, additional meaning for auto to provide type inference when declaring variables, new types including nullptr_t and _BitInt(N), and expansions to the standard library.\n\nC23 was published in October 2024 as ISO/IEC 9899:2024. The standard macro __STDC_VERSION__ is defined as 202311L to indicate that C23 support is available.\n\nC29\n\nC29 (C2Y) are informal names for the next major C language standard revision, after C23 (C2X), that is hoped to be released no later in the 2020s, hence the '2' in \"C2Y\". An early working draft of C2Y was released in February 2024 as N3220 by the working group ISO/IEC JTC1/SC22/WG14.\n\nEmbedded C\n\nHistorically, embedded C programming requires non-standard extensions to the C language to support exotic features such as fixed-point arithmetic, multiple distinct memory banks, and basic I/O operations.\n\nIn 2008, the C Standards Committee published a technical report extending the C language to address these"
 },
 {
  "title": "Cardinality of the continuum",
  "revision_id": "1369454080",
  "matched_by": "redirect",
  "text": "In set theory, the cardinality of the continuum is the cardinality or \"size\" of the set of real numbers , sometimes called the continuum. It is an infinite cardinal number and is denoted by (lowercase Fraktur \"c\") or \n\nThe real numbers are more numerous than the natural numbers . Moreover, has the same number of elements as the power set of . Symbolically, if the cardinality of is denoted as , the cardinality of the continuum is\n\nThis was proven by Georg Cantor in his uncountability proof of 1874, part of his groundbreaking study of different infinities. The inequality was later stated more simply in his diagonal argument in 1891. Cantor defined cardinality in terms of bijective functions: two sets have the same cardinality if, and only if, there exists a bijective function between them.\n\nBetween any two real numbers a < b, no matter how close they are to each other, there are always infinitely many other real numbers, and Cantor showed that they are as many as those contained in the whole set of real numbers. In other words, the open interval (a,b) is equinumerous with , as well as with several other infinite sets, such as any n-dimensional Euclidean space (see space filling curve). That is,\n\nThe smallest infinite cardinal number is (aleph-null). The second smallest is (aleph-one). The continuum hypothesis, which asserts that there are no sets whose cardinality is strictly between and , means that . This hypothesis is independent of the widely used Zermelo–Fraenkel set theory with axiom of choice (ZFC); that is, ZFC can neither prove that it is true nor that it is false.\n\nProperties\n\nUncountability\n\nGeorg Cantor introduced the concept of cardinality to compare the sizes of infinite sets. He famously showed that the set of real numbers is uncountably infinite. That is, is strictly greater than the cardinality of the natural numbers, :\n\nIn practice, this means that there are strictly more real numbers than there are integers. Cantor proved this statement in several different ways. For more information on this topic, see Cantor's first uncountability proof and Cantor's diagonal argument.\n\nCardinal equalities\n\nA variation of Cantor's diagonal argument can be used to prove Cantor's theorem, which states that the cardinality of any set is strictly less than that of its power set. That is, (and so that the power set of the natural numbers is uncountable). In fact, the cardinality of , by definition , is equal to . This can be shown by providing one-to-one mappings in both directions between subsets of a countably infinite set and real numbers, and applying the Cantor–Bernstein–Schroeder theorem according to which two sets with one-to-one mappings in both directions have the same cardinality. In one direction, reals can be equated with Dedekind cuts, sets of rational numbers, or with their binary expansions. In the other direction, the binary expansions of numbers in the half-open interval , viewed as sets of positions where the expansion is one, almost give a one-to-one mapping from subsets of a countable set (the set of positions in the expansions) to real numbers, but it fails to be one-to-one for numbers with terminating binary expansions, which can also be represented by a non-terminating expansion that ends in a repeating sequence of 1s. This can be made into a one-to-one mapping by that adds one to the non-terminating repeating-1 expansions, mapping them into . Thus, we conclude that\n\nThe cardinal equality can be demonstrated using cardinal arithmetic:\n\nBy using the rules of cardinal arithmetic, one can also show that\n\nwhere n is any finite cardinal ≥ 2 and\n\nwhere is the cardinality of the power set of R, and .\n\nAlternative explanation for 𝔠 = 2\n\nEvery real number has at least one infinite decimal expansion. For example,\n\n1/2 = 0.50000...\n1/3 = 0.33333...\nπ = 3.14159....\n\n(This is true even in the case the expansion repeats, as in the first two examples.)\n\nIn any given case, the number of decimal places is countable since they can be put into a one-to-one correspondence with the set of natural numbers . This makes it sensible to talk about, say, the first, the one-hundredth, or the millionth decimal place of π. Since the natural numbers have cardinality each real number has digits in its expansion.\n\nSince each real number can be broken into an integer part and a decimal fraction, we get:\n\nwhere we used the fact that\n\nOn the other hand, if we map to and consider that decimal fractions containing only 3 or 7 are only a part of the real numbers, then we get\n\nand thus\n\nBeth numbers\n\nThe sequence of beth numbers is defined by setting and . So is the second beth number, beth-one:\n\nThe third beth number, beth-two, is the cardinality of the power set of (i.e. the set of all subsets of the real line):\n\nThe continuum hypothesis\n\nThe continuum hypothesis asserts that is also the second aleph number, . In other words, the continuum hypothesis states that there is no set whose cardinality lies strictly between and \n\nThis statement is now known to be independent of the axioms of Zermelo–Fraenkel set theory with the axiom of choice (ZFC), as shown by Kurt Gödel and Paul Cohen. That is, both the hypothesis and its negation are consistent with these axioms. In fact, for every nonzero natural number n, the equality = is independent of ZFC (case being the continuum hypothesis). The same is true for most other alephs, although in some cases, equality can be ruled out by König's theorem on the grounds of cofinality (e.g. ). In particular, could be either or , where is the first uncountable ordinal, so it could be either a successor cardinal or a limit cardinal, and either a regular cardinal or a singular cardinal.\n\nSets with cardinality of the continuum\n\nA great many sets studied in mathematics have cardinality equal to . Some common examples are the following:\n\nthe real numbers \nany (nondegenerate) closed or open interval in (such as the unit interval )\nthe irrational numbers\nthe transcendental numbers\n\nThe set of real algebraic numbers is countably infinite (assign to each formula its Gödel number.) So the cardinality of the real algebraic numbers is . Furthermore, the real algebraic numbers and the real transcendental numbers are disjoint sets whose union is . Thus, since the cardinality of is , the cardinality of the real transcendental numbers is . A similar result follows for complex transcendental numbers, once we have proved that .\nthe Cantor set\nEuclidean space \nthe complex numbers \n\nPer Cantor's proof of the cardinality of Euclidean space, . By definition, any can be uniquely expressed as for some . We therefore define the bijection\n\nthe power set of the natural numbers (the set of all subsets of the natural numbers)\nthe set of sequences of integers (i.e. all functions , often denoted )\nthe set of sequences of real numbers, \nthe set of all continuous functions from to \nthe Euclidean topology on (i.e. the set of all open sets in )\nthe Borel σ-algebra on (i.e. the set of all Borel sets in ).\nthe abelian quotient group , assuming the Axiom of Choice\n\nSets with greater cardinality\n\nSets with cardinality greater than include:\n\nthe set of all subsets of (i.e., power set )\n\nthe set 2 of indicator functions defined on subsets of the reals (the set is isomorphic to  – the indicator function chooses elements of each subset to include)\n\nthe set of all functions from to \n\nthe Lebesgue σ-algebra of , i.e., the set of all Lebesgue measurable sets in .\n\nthe set of all Lebesgue-integrable functions from to \n\nthe set of all Lebesgue-measurable functions from to \n\nthe Stone–Čech compactifications of , , and \n\nthe set of all automorphisms of the (discrete) field of complex numbers.\n\nThese all have cardinality (beth two).\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q9820",
  "label": "C",
  "description": "3rd letter of the basic Latin alphabet",
  "aliases": [
   "cee",
   "Charlie",
   "cˈsiː",
   "letter C",
   "charlie",
   "C/c"
  ],
  "claims": {
   "P31": [
    "Q19776628"
   ],
   "P279": [
    "Q19776628",
    "Q3841820"
   ],
   "P361": [
    "Q5974462",
    "Q606972",
    "Q754673",
    "Q607188",
    "Q76228",
    "Q1095058",
    "Q1187758",
    "Q622712",
    "Q637405",
    "Q550383",
    "Q755124",
    "Q18691434",
    "Q994407",
    "Q384749",
    "Q2839543",
    "Q912243",
    "Q1193493",
    "Q163296"
   ],
   "P527": [
    "Q87496163",
    "Q87496274"
   ],
   "P1889": [
    "Q28006",
    "Q179873",
    "Q15777"
   ]
  },
  "revision_id": "2571672454",
  "value_labels": {
   "Q19776628": "Latin-script letter",
   "Q3841820": "consonant letter",
   "Q5974462": "ISO basic Latin alphabet",
   "Q606972": "Polish alphabet",
   "Q754673": "English alphabet",
   "Q607188": "Esperanto alphabet",
   "Q76228": "Czech alphabet",
   "Q1095058": "Romanian alphabet",
   "Q1187758": "Slovak alphabet",
   "Q622712": "Vietnamese alphabet",
   "Q637405": "Turkish alphabet",
   "Q550383": "Italian alphabet",
   "Q755124": "French alphabet",
   "Q18691434": "Finnish alphabet",
   "Q994407": "African reference alphabet",
   "Q384749": "Africa Alphabet",
   "Q2839543": "Benin National Alphabet",
   "Q912243": "German alphabet",
   "Q1193493": "Latvian alphabet",
   "Q163296": "Upper Sorbian alphabet",
   "Q87496163": "C",
   "Q87496274": "c",
   "Q28006": "",
   "Q179873": "С",
   "Q15777": "C"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15777",
  "label": "C",
  "description": "general-purpose programming language",
  "aliases": [
   "C programming language",
   "C language"
  ],
  "claims": {
   "P31": [
    "Q21562092",
    "Q28922885",
    "Q28920117",
    "Q651794",
    "Q9143",
    "Q66747126",
    "Q12772052"
   ],
   "P279": [
    "Q28922885"
   ],
   "P1889": [
    "Q9820"
   ]
  },
  "revision_id": "2572485791",
  "value_labels": {
   "Q21562092": "imperative programming language",
   "Q28922885": "procedural programming language",
   "Q28920117": "structured programming language",
   "Q651794": "compiled language",
   "Q9143": "programming language",
   "Q66747126": "computer science term",
   "Q12772052": "multi-paradigm programming language",
   "Q9820": "C"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q22952648",
  "label": "cardinality of the continuum",
  "description": "cardinality of the set of real numbers",
  "aliases": [
   "beth one",
   "beth-one",
   "cardinality of the real numbers",
   "beth 1",
   "beth-1",
   "cardinality of ℝ",
   "cardinality of R"
  ],
  "claims": {
   "P31": [
    "Q163875",
    "Q831092",
    "Q908627"
   ],
   "P361": [
    "Q831092"
   ],
   "P460": [
    "Q2832673"
   ]
  },
  "revision_id": "2570419256",
  "value_labels": {
   "Q163875": "cardinal number",
   "Q831092": "beth number",
   "Q908627": "aleph number",
   "Q2832673": "aleph one"
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
  "ancestor_of": "Q9820",
  "level": 1,
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
  "ancestor_of": "Q9820",
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
  "ancestor_of": "Q9820",
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
  "ancestor_of": "Q9820",
  "level": 2,
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28920117",
  "label": "structured programming language",
  "description": "type of programming language",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2552001011",
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
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
  "ancestor_of": "Q15777",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q163875",
  "label": "cardinal number",
  "description": "finite or infinite number that measures cardinality (size) of sets",
  "aliases": [
   "cardinal",
   "cardinals"
  ],
  "claims": {
   "P31": [
    "Q47460393"
   ],
   "P279": [
    "Q191780"
   ],
   "P361": [
    "Q112278968"
   ],
   "P1889": [
    "Q1329258",
    "Q45722",
    "Q223402",
    "Q21199"
   ]
  },
  "revision_id": "2567607672",
  "ancestor_of": "Q22952648",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q831092",
  "label": "beth number",
  "description": "ordered sequence of transfinite numbers used to represent the cardinality (or size) of continuous sets",
  "aliases": [
   "BET SYMBOL",
   "ℶ",
   "bet number",
   "beth symbol",
   "ℶ-number"
  ],
  "claims": {
   "P31": [
    "Q29654788",
    "Q10376408"
   ],
   "P279": [
    "Q163875",
    "Q1069891"
   ],
   "P1889": [
    "Q15049"
   ]
  },
  "revision_id": "2558637581",
  "ancestor_of": "Q22952648",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q908627",
  "label": "aleph number",
  "description": "alef symbol (U+2135) or aleph, written left-to-right as the mathemical symbol ‹ℵ› for the first transfinite cardinal (countable); ordered sequence of transfinite numbers used to represent the cardinality (or size) of infinite countable sets",
  "aliases": [
   "ALEF SYMBOL",
   "ℵ",
   "aleph symbol",
   "alef number"
  ],
  "claims": {
   "P31": [
    "Q29654788",
    "Q10376408"
   ],
   "P279": [
    "Q163875",
    "Q1069891"
   ],
   "P1889": [
    "Q16725860"
   ]
  },
  "revision_id": "2553948266",
  "ancestor_of": "Q22952648",
  "level": 1,
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
  "ancestor_of": "Q22952648",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q191780",
  "label": "ordinal number",
  "description": "mathematical concept generalizing ordinal numerals to extend enumeration to infinite sets",
  "aliases": [
   "ordinal",
   "ordinal numbers"
  ],
  "claims": {
   "P31": [
    "Q47460393"
   ],
   "P279": [
    "Q11563",
    "Q309314"
   ],
   "P1889": [
    "Q923933"
   ]
  },
  "revision_id": "2567609955",
  "ancestor_of": "Q22952648",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q29654788",
  "label": "Unicode character",
  "description": "type of code point used to encode a character in the Universal Character Set (UCS) defined by the Unicode and ISO/IEC 10646 standards",
  "aliases": [
   "character in Unicode",
   "character (Unicode)",
   "Unicode characters",
   "characters in Unicode",
   "characters (Unicode)"
  ],
  "claims": {
   "P31": [
    "Q2352616",
    "Q109613493"
   ],
   "P279": [
    "Q3241972",
    "Q109615047"
   ],
   "P361": [
    "Q8819",
    "Q777955"
   ],
   "P1889": [
    "Q109615173",
    "Q109615332"
   ]
  },
  "revision_id": "2555481145",
  "ancestor_of": "Q22952648",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q10376408",
  "label": "mathematical symbol",
  "description": "symbol used in mathematics",
  "aliases": [],
  "claims": {
   "P279": [
    "Q80071",
    "Q3241972",
    "Q6498784"
   ],
   "P361": [
    "Q1140046",
    "Q6498784"
   ],
   "P1889": [
    "Q1401551"
   ]
  },
  "revision_id": "2568221914",
  "ancestor_of": "Q22952648",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1069891",
  "label": "transfinite number",
  "description": "number larger than all finite numbers",
  "aliases": [],
  "claims": {
   "P31": [
    "Q47460393"
   ],
   "P279": [
    "Q11563"
   ]
  },
  "revision_id": "2554105750",
  "ancestor_of": "Q22952648",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-13736596-n",
  "lemmas": [
   "degree centigrade",
   "degree Celsius",
   "C"
  ],
  "gloss": "a degree on the centigrade scale of temperature",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-13736289-n"
   ],
   "hyponym": [
    "oewn-13737229-n"
   ]
  },
  "relation_targets": {
   "oewn-13736289-n": "degree",
   "oewn-13737229-n": "standard temperature"
  }
 },
 {
  "synset": "oewn-15117865-n",
  "lemmas": [
   "vitamin C",
   "C",
   "ascorbic acid"
  ],
  "gloss": "a vitamin found in fresh fruits (especially citrus fruits) and vegetables; prevents scurvy",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-15114212-n",
    "oewn-14748824-n"
   ]
  },
  "relation_targets": {
   "oewn-15114212-n": "water-soluble vitamin",
   "oewn-14748824-n": "antioxidant"
  }
 },
 {
  "synset": "oewn-14853935-n",
  "lemmas": [
   "deoxycytidine monophosphate",
   "C",
   "dCMP",
   "deoxycytidylic acid",
   "deoxycytidylate"
  ],
  "gloss": "nucleotide derived from cytosine with a deoxyribose sugar and a phosphate group",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-14988729-n"
   ]
  },
  "relation_targets": {
   "oewn-14988729-n": "nucleotide, base"
  }
 },
 {
  "synset": "oewn-14852681-n",
  "lemmas": [
   "cytosine",
   "C"
  ],
  "gloss": "a base found in DNA and RNA and derived from pyrimidine; pairs with guanine",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-15024480-n"
   ]
  },
  "relation_targets": {
   "oewn-15024480-n": "pyrimidine"
  }
 },
 {
  "synset": "oewn-14657384-n",
  "lemmas": [
   "carbon",
   "C",
   "atomic number 6"
  ],
  "gloss": "an abundant nonmetallic tetravalent element occurring in three allotropic forms: amorphous carbon and graphite and diamond; occurs in all organic compounds",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-14651424-n"
   ],
   "hyponym": [
    "oewn-14646319-n",
    "oewn-14658034-n",
    "oewn-14709333-n",
    "oewn-14709457-n",
    "oewn-14817703-n",
    "oewn-14820529-n",
    "oewn-14820745-n",
    "oewn-14858733-n"
   ]
  },
  "relation_targets": {
   "oewn-14651424-n": "nonmetal",
   "oewn-14646319-n": "fullerene",
   "oewn-14658034-n": "radiocarbon, carbon 14",
   "oewn-14709333-n": "char",
   "oewn-14709457-n": "charcoal, wood coal",
   "oewn-14817703-n": "carbon black, lampblack, soot",
   "oewn-14820529-n": "activated carbon, activated charcoal",
   "oewn-14820745-n": "graphite, black lead, plumbago",
   "oewn-14858733-n": "diamond, adamant"
  }
 },
 {
  "synset": "oewn-13772555-n",
  "lemmas": [
   "hundred",
   "100",
   "C",
   "century",
   "one C"
  ],
  "gloss": "ten 10s",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-13767560-n"
   ]
  },
  "relation_targets": {
   "oewn-13767560-n": "large integer"
  }
 },
 {
  "synset": "oewn-13658127-n",
  "lemmas": [
   "coulomb",
   "C",
   "ampere-second"
  ],
  "gloss": "a unit of electrical charge equal to the amount of charge transferred by a current of 1 ampere in 1 second",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-13654422-n"
   ],
   "part_holonym": [
    "oewn-13658345-n",
    "oewn-13658468-n"
   ]
  },
  "relation_targets": {
   "oewn-13654422-n": "charge unit, quantity unit",
   "oewn-13658345-n": "abcoulomb",
   "oewn-13658468-n": "ampere-minute"
  }
 },
 {
  "synset": "oewn-06915472-n",
  "lemmas": [
   "C"
  ],
  "gloss": "a general-purpose programing language closely associated with the UNIX operating system",
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
  "synset": "oewn-06879382-n",
  "lemmas": [
   "C"
  ],
  "gloss": "(music) the keynote of the scale of C major",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06870776-n"
   ]
  },
  "relation_targets": {
   "oewn-06870776-n": "tonic, keynote"
  }
 },
 {
  "synset": "oewn-06844441-n",
  "lemmas": [
   "C",
   "c"
  ],
  "gloss": "the 3rd letter of the Roman alphabet",
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
  "synset": "oewn-03070747-n",
  "lemmas": [
   "coke",
   "blow",
   "nose candy",
   "snow",
   "C"
  ],
  "gloss": "street names for cocaine",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-03064297-n"
   ]
  },
  "relation_targets": {
   "oewn-03064297-n": "cocaine, cocain"
  }
 },
 {
  "synset": "oewn-15309503-n",
  "lemmas": [
   "speed of light",
   "light speed",
   "c"
  ],
  "gloss": "the speed at which light travels in a vacuum; the constancy and universality of the speed of light is recognized by defining it to be exactly 299,792,458 meters per second",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-15307914-n",
    "oewn-13606632-n"
   ]
  },
  "relation_targets": {
   "oewn-15307914-n": "speed, velocity",
   "oewn-13606632-n": "constant"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 2: C++ (`qb4qnsutxp`)

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
[
 {
  "title": "C++",
  "revision_id": "1375333877",
  "matched_by": "title",
  "text": "C++ is a high-level, general-purpose programming language created by Danish computer scientist Bjarne Stroustrup. First released in 1985 as an extension of the C programming language, adding object-oriented (OOP) functionality and later expanding significantly with the addition of functional programming features. It supports low-level memory manipulation for systems like microcomputers and has been used for the creation and maintenance of Microsoft Windows. C++ has also added support for generic programming through the use of templates. It is usually implemented as a compiled language, and many vendors provide C++ compilers, including the Free Software Foundation, LLVM, Microsoft, Intel, Embarcadero, Oracle, and IBM.\n\nC++ was designed with systems programming and embedded, resource-constrained software and large systems in mind, with performance, efficiency, and flexibility of use as its design highlights. C++ has also been found useful in many other contexts, with key strengths being software infrastructure and resource-constrained applications, including desktop applications, video games, servers (e.g., e-commerce, web search, or databases), and performance-critical applications (e.g., telephone switches or space probes).\n\nC++ is standardized by the International Organization for Standardization (ISO), with the latest standard version ratified and published by ISO in October 2024 as ISO/IEC 14882:2024 (informally known as C++23). The C++ programming language was initially standardized in 1998 as ISO/IEC 14882:1998, which was then amended by the C++03, C++11, C++14, C++17, and C++20 standards. The next C++23 standard superseded these with new features and an enlarged standard library. Before the initial standardization in 1998, C++ was developed by Stroustrup at Bell Labs since 1979 as an extension of the C language; he wanted an efficient and flexible language similar to C that also provided high-level features for program organization. Since 2012, C++ has been on a three-year release schedule with C++29 as the next planned standard.\n\nHistory\n\nIn 1979, Bjarne Stroustrup, a Danish computer scientist, began work on \"C with Classes\", the predecessor to C++. Initially, Stroustrup's \"C with Classes\" added features to the C compiler, Cpre, including classes, derived classes, strong typing, inlining, and default arguments.\n\nIn 1982, Stroustrup began designing a cleaned-up and extended successor to C with Classes, using traditional compiler technology. The language was briefly called C84 before the name C++ was adopted; the name was suggested by Rick Mascitti and refers to C's ++ increment operator. The resulting language included virtual functions, function and operator overloading, references, const, improved type checking, user-controlled free-store memory allocation (new/delete), and BCPL-style single-line // comments. Stroustrup also designed and implemented Cfront, the C++ compiler front end, between spring 1982 and summer 1983.\n\nIn 1985, the first edition of The C++ Programming Language was released, which became the definitive reference for the language, as there was not yet an official standard. The first commercial implementation of C++ was released in October of the same year.\n\nIn 1989, C++ 2.0 was released, followed by the updated second edition of The C++ Programming Language in 1991. New features in 2.0 included multiple inheritance, abstract classes, static member functions, const member functions, and protected members. In 1990, The Annotated C++ Reference Manual was published. This work became the basis for the future standard. Later feature additions included templates, exceptions, namespaces, new casts, and a Boolean type.\n\nIn 1998, C++98 was released, standardizing the language, and a minor update (C++03) was released in 2003.\n\nAfter C++98, C++ evolved relatively slowly until, in 2011, the C++11 standard was released, adding numerous new features, enlarging the standard library further, and providing more facilities to C++ programmers. After a minor C++14 update released in December 2014, various new additions were introduced in C++17. After becoming finalized in February 2020, a draft of the C++20 standard was approved on 4 September 2020, and officially published on 15 December 2020.\n\nOn January 3, 2018, Stroustrup was announced as the 2018 winner of the Charles Stark Draper Prize for Engineering, \"for conceptualizing and developing the C++ programming language\".\n\nIn December 2022, C++ ranked third on the TIOBE index, surpassing Java for the first time in the history of the index. As of November 2024, the language ranks second after Python, with Java being in third.\n\nIn March 2025, Stroustrup issued a call for the language community to defend it. Since the language allows manual memory management, bugs that represent security risks such as buffer overflow may be introduced in programs when inadvertently misused by the programmer.\n\nEtymology\n\nAccording to Stroustrup, \"the name signifies the evolutionary nature of the changes from C.\" This name is credited to Rick Mascitti (mid-1983) and was first used in December 1983. When Mascitti was questioned informally in 1992 about the naming, he indicated that it was given in a tongue-in-cheek spirit. The name comes from C's ++ operator (which increments the value of a variable) and a common naming convention of using \"+\" to indicate an enhanced computer program.\n\nDuring C++'s development period, the language had been referred to as \"new C\" and \"C with Classes\" before acquiring its final name.\n\nPhilosophy\n\nThroughout C++'s life, its development and evolution has been guided by a set of principles:\n\nIt must be driven by actual problems and its features should be immediately useful in real world programs.\n\nEvery feature should be implementable (with a reasonably obvious way to do so).\n\nProgrammers should be free to pick their own programming style, and that style should be fully supported by C++.\n\nAllowing a useful feature is more important than preventing every possible misuse of C++.\n\nIt should provide facilities for organizing programs into separate, well-defined parts, and provide facilities for combining separately developed parts.\n\nNo implicit violations of the type system (but allow explicit violations; that is, those explicitly requested by the programmer).\n\nUser-created types need to have the same support and performance as built-in types.\n\nUnused features should not negatively impact created executables (e.g. in lower performance).\n\nThere should be no language beneath C++ (except assembly language).\n\nC++ should work alongside other existing programming languages, rather than fostering its own separate and incompatible programming environment.\n\nIf the programmer's intent is unknown, allow the programmer to specify it by providing manual control.\n\nStandardization\n\nC++ is standardized by an ISO working group known as JTC1/SC22/WG21. The working group holds three week-long meetings each year. So far, it has published seven revisions of the C++ standard and is currently working on the next revision, C++26.\n\nIn 1998, the ISO working group standardized C++ for the first time as ISO/IEC 14882:1998, which is informally known as C++98. In 2003, it published a new version of the C++ standard called ISO/IEC 14882:2003, which fixed problems identified in C++98.\n\nThe next major revision of the standard was informally referred to as \"C++0x\", but it was not released until 2011. C++11 (14882:2011) included many additions to both the core language and the standard library.\n\nIn 2014, C++14 (also known as C++1y) was released as a small extension to C++11, featuring mainly bug fixes and small improvements. The Draft International Standard ballot procedures completed in mid-August 2014.\n\nAfter C++14, a major revision C++17, informally known as C++1z, was completed by the ISO C++ committee in mid July 2017 and was approved and published in December 2017.\n\nAs part of the standardization process, ISO also publishes technical reports and specifications:\n\nISO/IEC TR 18015:2006 on the use of C++ in embedded systems and on performance implications of C++ language and library features,\n\nISO/IEC TR 19768:2007 (also known as the C++ Technical Report 1) on library extensions mostly integrated into C++11,\n\nISO/IEC TR 29124:2010 on special mathematical functions, integrated into C++17,\n\nISO/IEC TR 24733:2011 on decimal floating-point arithmetic,\n\nISO/IEC TS 18822:2015 on the standard filesystem library, integrated into C++17,\n\nISO/IEC TS 19570:2015 on parallel versions of the standard library algorithms, integrated into C++17,\n\nISO/IEC TS 19841:2015 on software transactional memory,\n\nISO/IEC TS 19568:2015 on a new set of library extensions, some of which are already integrated into C++17,\n\nISO/IEC TS 19217:2015 on the C++ concepts, integrated into C++20,\n\nISO/IEC TS 19571:2016 on the library extensions for concurrency, some of which are already integrated into C++20,\n\nISO/IEC TS 19568:2017 on a new set of general-purpose library extensions,\n\nISO/IEC TS 21425:2017 on the library extensions for ranges, integrated into C++20,\n\nISO/IEC TS 22277:2017 on coroutines, integrated into C++20,\n\nISO/IEC TS 19216:2018 on the networking library,\n\nISO/IEC TS 21544:2018 on modules, integrated into C++20,\n\nISO/IEC TS 19570:2018 on a new set of library extensions for parallelism\n\nISO/IEC TS 23619:2021 on new extensions for reflective programming (reflection),\n\nISO/IEC TS 9922:2024 on new set of concurrency extensions, and\n\nISO/IEC TS 19568:2024 on another new set of library extensions.\n\nMore technical specifications are in development and pending approval.\n\nLanguage\n\nThe C++ language has two main components: a direct mapping of hardware features provided primarily by the C subset, and zero-overhead abstractions based on those mappings. Stroustrup describes C++ as \"a light-weight abstraction programming language [designed] for building and using efficient and elegant abstractions\"; and \"offering both hardware access and abstraction is the basis of C++. Doing it efficiently is what distinguishes it from other languages.\"\n\nC++ inherits most of C's syntax. A hello world program that conforms to the C standard is also a valid C++ hello world program. The following is adapted from Bjarne Stroustrup's version of the Hello world program that uses the C++ Standard Library stream facility to write a message to standard output:\n\n#include <iostream>\n\nint main() {\n std::cout << \"Hello, world!\\n\";\n}\n\nSince C++23, with the introduction of std::print functions and module std, this can be expressed less verbosely as:\n\nimport std;\n\nint main() {\n std::println(\"Hello, world!\");\n}\n\nStandard library\n\nThe C++ standard specifies both the core language and the standard library. The library clauses describe the contents of the library, how a well-formed C++ program uses it, and the requirements placed on conforming implementations.\n\nThe standard library is organized into areas such as language support, diagnostics, memory management, metaprogramming, general utilities, containers, iterators, ranges, algorithms, strings, text processing, numerics, time, input/output, and concurrency support. It also provides the facilities of the C standard library through C++ headers such as <cstdio> and <cstdlib>; except for names defined as macros in C, these declarations are placed in namespace std.\n\nLibrary facilities are traditionally made available by including standard headers, for example #include <vector>. Since C++20, importable standard library headers may also be imported as header units. C++23 added the named standard library modules std and std.compat: std exports declarations in namespace std, while std.compat also exports corresponding global namespace declarations for C library facilities.\n\nA major influence on the standard library was the Standard Template Library (STL), a generic programming library proposed to the C++ standards committee by Alexander Stepanov and Meng Lee in 1994. Its model of containers, iterators, and generic algorithms became part of the Standard C++ Library, although the standard library also includes many other facilities, such as input/output, localization, diagnostics, and the C library subset.\n\nC++ Core Guidelines\n\nThe C++ Core Guidelines are an initiative led by Stroustrup and Herb Sutter, the convener and chair of the C++ ISO Working Group, to help programmers write 'Modern C++' by using best practices for the language standards C++11 and newer, and to help developers of compilers and static checking tools to create rules for catching bad programming practices. The main aim is to efficiently and consistently write type and resource safe C++. Despite this, the guidelines are not endorsed by the ISO C++ standards committee and do not represent the consensus of the committee.\n\nThe Core Guidelines were announced in the opening keynote at CPPCon 2015.\n\nThe Guidelines are accompanied by the Guideline Support Library (GSL), a header-only library of types and functions to implement the Core Guidelines and static checker tools for enforcing Guideline rules. One of the largest implementations of this is Microsoft's implementation. Many of the existing features in the GSL have been later integrated into the language, such as std::byte, smart pointers, and std::span.\n\nCompatibility\n\nTo give compiler vendors greater freedom, the C++ standards committee decided not to dictate the implementation of name mangling, exception handling, and other implementation-specific features. The downside of this decision is that object code produced by different compilers is expected to be incompatible. There are, however, attempts to standardize compilers for particular machines or operating systems. For example, the Itanium C++ ABI is processor-independent (despite its name) and is implemented by GCC and Clang.\n\nWith C\n\nC++ is often considered to be a superset of C but this is not strictly true. Most C code can easily be made to compile correctly in C++ but there are a few differences that cause some valid C code to be invalid or behave differently in C++. For example, C allows implicit conversion from void* to other pointer types but C++ does not (for type safety reasons). Also, C++ defines many new keywords, such as new and class, which may be used as identifiers (for example, variable names) in a C program.\n\nSome incompatibilities have been removed by the 1999 revision of the C standard (C99), which now supports C++ features such as line comments (//) and declarations mixed with code. On the other hand, C99 introduced a number of new features that C++ did not support that were incompatible or redundant in C++, such as variable-length arrays, native complex-number types (however, the std::complex class in the C++ standard library provides similar functionality, although not code-compatible), designated initializers, compound literals, and the restrict keyword. Some of the C99-introduced features were included in the subsequent version of the C++ standard, C++11 (out of those which were not redundant). However, the C++11 standard introduces new incompatibilities, such as disallowing assignment of a string literal to a character pointer, which remains valid C.\n\nTo intermix C and C++ code, any function declaration or definition that is to be called from/used both in C and C++ must be declared with C linkage by placing it within an extern \"C\" {/*...*/} block. Such a function may not rely on features depending on name mangling (i.e., function overloading).\n\nInline assembly\n\nPrograms developed in C or C++ often use inline assembly to take advantage of its low-level functionalities, greater speed, and enhanced control compared to high-level programming languages when optimizing for performance is essential. C++ provides support for embedding assembly language using asm declarations, but the compatibility of inline assembly varies significantly between compilers and architectures. Unlike high-level language features such as Python or Java, assembly code is highly dependent on the underlying processor and compiler implementation.\n\nVariations across compilers\n\nDifferent C++ compilers implement inline assembly in distinct ways.\n\nGCC (GNU Compiler Collection) and Clang: Both compilers use the GCC extended inline assembly syntax, using the __asm__ keyword instead of asm when writing code that can be compiled with -ansi and -std options, which allows specifying input/output operands and clobbered registers. This approach is also adopted elsewhere, including by Intel and IBM compilers.\n\nMSVC (Microsoft Visual C++): The inline assembler is built into the compiler. Previously supported inline assembly via the __asm keyword, but this support has been removed in 64-bit mode, requiring separate .asm modules instead.\n\nTI ARM Clang and Embedded Compilers: Some embedded system compilers, like Texas Instruments' TI Arm Clang, allow inline assembly but impose stricter rules to avoid conflicts with register conventions and calling conventions.\nInteroperability between C++ and Assembly\n\nC++ provides two primary methods of integrating ASM code: standalone assembly files, where assembly code is written separately and linked with C++ code. And inline assembly, where assembly code is embedded within C++ code using compiler-specific extensions.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q2407",
  "label": "C++",
  "description": "general-purpose programming language",
  "aliases": [],
  "claims": {
   "P31": [
    "Q9143",
    "Q899523",
    "Q12772052",
    "Q28922885",
    "Q3839507",
    "Q28923026",
    "Q5499621",
    "Q651794"
   ],
   "P279": [
    "Q651794"
   ],
   "P527": [
    "Q1022270"
   ]
  },
  "revision_id": "2567497996",
  "value_labels": {
   "Q9143": "programming language",
   "Q899523": "object-based language",
   "Q12772052": "multi-paradigm programming language",
   "Q28922885": "procedural programming language",
   "Q3839507": "functional programming language",
   "Q28923026": "generic programming language",
   "Q5499621": "free-form language",
   "Q651794": "compiled language",
   "Q1022270": "C++ Standard Library"
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28923026",
  "label": "generic programming language",
  "description": "programming language supporting generic programming",
  "aliases": [],
  "claims": {
   "P31": [
    "Q116481801"
   ],
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "2362182605",
  "ancestor_of": "Q2407",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q5499621",
  "label": "free-form language",
  "description": "programming language in which the positioning of characters on the page in program text is insignificant",
  "aliases": [],
  "claims": {
   "P279": [
    "Q9143"
   ]
  },
  "revision_id": "1949794283",
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
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
  "ancestor_of": "Q2407",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
