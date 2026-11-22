# Skills Lexicon pilot, grounded run: message 12 of 13 (chunk 11, 6 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "11", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-11.jsonl`. Otherwise send one code block marked `jsonl` holding the 6 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 6: Mathematics (`v2tu54uao9`)

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
[
 {
  "title": "Mathematics",
  "revision_id": "1377221419",
  "matched_by": "api-title-or-redirect",
  "text": "Mathematics is a field of knowledge concerned with abstract concepts such as numbers, geometric shapes, sets, functions, and probabilities. It uses logical reasoning and proof to study and establish their properties, often expressed as theorems, formulas, and equations. Mathematics is widely used to model and solve problems in science, engineering, technology, economics, and everyday life.\n\nThere are many areas of mathematics, including number theory (the study of integers and their properties), algebra (the study of operations and the structures they form), geometry (the study of shapes and spaces that contain them), analysis (the quantitative study of approximation and convergence), and set theory (presently used as a foundation for all mathematics).\n\nMathematics involves the description and manipulation of abstract objects that are either abstractions from nature or purely abstract entities that are stipulated to have certain properties, called axioms. Mathematics uses pure reason to prove the properties of objects through proofs, which consist of a succession of applications of deductive rules to already established results. These results, called theorems, include previously proved theorems, axioms, and—in case of abstraction from nature—some basic properties that are considered true starting points of the theory under consideration.\n\nMathematics is essential in science and engineering; it is widely used in every field of knowledge and in everyday life, as soon as data are manipulated, shapes, patterns, and structures are studied, and logical reasoning is needed. Although mathematics is widely used to model empirical phenomena, its results are established by deductive proof rather than by experiment. The relationship between mathematical truth, logic, and reality is a subject of philosophical debate. Some areas of mathematics, such as game theory, are developed in close correlation with their applications and are often grouped under applied mathematics. Other areas are developed independently from any application but often find practical applications later.\n\nMathematical written records first appeared in Ancient Egypt and Mesopotamia, but the concept of proof and its associated mathematical rigor began in ancient Greek mathematics, exemplified in Euclid's Elements. Mathematics was primarily divided into geometry and arithmetic until the 16th and 17th centuries, when algebra and infinitesimal calculus evolved into new fields. Since then, the interaction between mathematical innovations and scientific discoveries has led to a correlated increase in the development of both. At the end of the 19th century, the foundational crisis of mathematics led to the systematic use of the axiomatic method, which heralded a dramatic increase in the number of mathematical areas and their fields of application. The contemporary Mathematics Subject Classification lists more than 60 first-level areas of mathematics.\n\nAreas of mathematics\n\nBefore the Renaissance, mathematics was divided into two main areas: arithmetic, regarding the study and manipulation of numbers, and geometry, regarding the study of shapes. Some types of pseudoscience, such as numerology and astrology, were not then clearly distinguished from mathematics.\n\nBeginning with the Renaissance, two more areas became predominant. New mathematical notation led to modern algebra which, roughly speaking, begins with the study and manipulation of algebraic expressions. Calculus, consisting of the two subfields differential calculus and integral calculus, originated with geometry but evolved into the study of continuous functions, which model the typically nonlinear relationships between varying quantities, as represented by variables. This division into four main areas—arithmetic, geometry, algebra, and calculus—endured until the end of the 19th century. Other areas that were previously studied by mathematicians, such as celestial mechanics and solid mechanics, are now considered to belong to physics. The subject of combinatorics has been studied for much of recorded history, yet did not become a separate branch of mathematics until the 17th century.\n\nAt the end of the 19th century, the foundational crisis in mathematics and the systematic use of the axiomatic method led to an explosion of new areas of mathematics. The 2020 Mathematics Subject Classification contains no fewer than 63 first-level areas. Some of these areas correspond to the older division, as is true regarding number theory (the modern name for higher arithmetic) and geometry. Several other first-level areas have \"geometry\" in their names or are otherwise commonly considered part of geometry. Algebra and calculus do not appear as first-level areas but are split into several first-level areas. Other first-level areas emerged during the 20th century or had not previously been considered as mathematics, such as mathematical logic and foundations.\n\nNumber theory\n\nNumber theory evolved from the manipulation of numbers, that is, natural numbers and later expanded to integers and rational numbers Number theory was once called arithmetic, but nowadays this term is mostly used for numerical calculations. The study of numbers arguably dates back to ancient Babylon and probably China, but developed into a distinct discipline in ancient Greece. Two prominent early number theorists were Euclid and Diophantus of Alexandria. The modern study of number theory in its abstract form is largely attributed to Pierre de Fermat and Leonhard Euler. The field came to full fruition with the contributions of Adrien-Marie Legendre and Carl Friedrich Gauss.\n\nMany easily stated number problems have solutions that require sophisticated methods, often from across mathematics. A prominent example is Fermat's Last Theorem. This conjecture was stated in 1637 by Pierre de Fermat, but it was proved only in 1994 by Andrew Wiles, who used tools including scheme theory from algebraic geometry, category theory, and homological algebra. Another example is Goldbach's conjecture, which asserts that every even integer greater than 2 is the sum of two prime numbers. Stated in 1742 by Christian Goldbach, it remains unproven despite considerable effort.\n\nNumber theory includes several subareas, including analytic number theory, algebraic number theory, geometry of numbers (method oriented), Diophantine analysis, and transcendence theory (problem oriented).\n\nGeometry\n\nGeometry is one of the oldest branches of mathematics. It started with empirical recipes concerning shapes, such as lines, angles, and circles, which were developed mainly for the needs of surveying and architecture, but has since blossomed into many other subfields.\n\nA fundamental innovation was the ancient Greeks' introduction of the concept of proofs, which require that every assertion must be proved. For example, it is not sufficient to verify by measurement that, say, two lengths are equal; their equality must be proven via reasoning from previously accepted results (theorems) and a few basic statements. The basic statements are not subject to proof because they are self-evident (postulates), or are part of the definition of the subject of study (axioms). This principle, foundational for all mathematics, was first elaborated for geometry, and was systematized by Euclid around 300 BC in his book Elements.\n\nThe resulting Euclidean geometry is the study of shapes and their arrangements constructed from lines, planes and circles in the Euclidean plane (plane geometry) and the three-dimensional Euclidean space.\n\nEuclidean geometry was developed without change of methods or scope until the 17th century, when René Descartes introduced what is now called Cartesian coordinates. This constituted a major change of paradigm: Instead of defining real numbers as lengths of line segments (see number line), it allowed the representation of points using their coordinates, which are numbers. Algebra (and later, calculus) can thus be used to solve geometrical problems. Geometry was split into two new subfields: synthetic geometry, which uses purely geometrical methods, and analytic geometry, which uses coordinates systematically.\n\nAnalytic geometry allows the study of curves unrelated to circles and lines. Such curves can be defined as the graph of functions, the study of which led to differential geometry. They can also be defined as implicit equations, often polynomial equations (which spawned algebraic geometry). Analytic geometry also makes it possible to consider Euclidean spaces of higher than three dimensions.\n\nIn the 19th century, mathematicians discovered non-Euclidean geometries, which do not follow the parallel postulate. By questioning that postulate's truth, this discovery has been viewed as joining Russell's paradox in revealing the foundational crisis of mathematics. This aspect of the crisis was solved by systematizing the axiomatic method and adopting the view that the truth of the chosen axioms is not a mathematical problem. In turn, the axiomatic method allows for the study of various geometries obtained either by changing the axioms or by considering properties that do not change under specific transformations of the space.\n\nToday's subareas of geometry include:\n\nProjective geometry, introduced in the 16th century by Girard Desargues, extends Euclidean geometry by adding points at infinity at which parallel lines intersect. This simplifies many aspects of classical geometry by unifying the treatments for intersecting and parallel lines.\n\nAffine geometry, the study of properties relative to parallelism and independent of the concept of length.\n\nDifferential geometry, the study of curves, surfaces, and their generalizations, which are defined using differentiable functions.\n\nManifold theory, the study of shapes that are not necessarily embedded in a larger space.\n\nRiemannian geometry, the study of distance properties in curved spaces.\n\nAlgebraic geometry, the study of curves, surfaces, and their generalizations, which are defined using polynomials.\n\nTopology, the study of properties that are kept under continuous deformations.\n\nAlgebraic topology, the use in topology of algebraic methods, mainly homological algebra.\n\nDiscrete geometry, the study of finite configurations in geometry.\n\nConvex geometry, the study of convex sets, which takes its importance from its applications in optimization.\n\nComplex geometry, the geometry obtained by replacing real numbers with complex numbers.\n\nAlgebra\n\nAlgebra is the art of manipulating equations and formulas. Diophantus (3rd century) and al-Khwarizmi (9th century) were the two main precursors of algebra. Diophantus solved some equations involving unknown natural numbers by deducing new relations until he obtained the solution. Al-Khwarizmi introduced systematic methods for transforming equations, such as moving a term from one side of an equation to the other side. The term algebra is derived from the Arabic word al-jabr, meaning 'the reunion of broken parts', which he used for naming one of these methods in the title of his main treatise.\n\nAlgebra became an area in its own right only with François Viète (1540–1603), who introduced the use of variables for representing unknown or unspecified numbers. Variables allow mathematicians to describe the operations that have to be done on the numbers represented using mathematical formulas.\n\nUntil the 19th century, algebra consisted mainly of the study of linear equations (presently linear algebra), and polynomial equations in a single unknown, which were called algebraic equations (a term still in use, although it may be ambiguous). During the 19th century, mathematicians began to use variables to represent things other than numbers (such as matrices, modular integers, and geometric transformations), on which generalizations of arithmetic operations are often valid. The concept of algebraic structure addresses this, consisting of a set whose elements are unspecified, of operations acting on the elements of the set, and rules that these operations must follow. The scope of algebra thus grew to include the study of algebraic structures. This object of algebra was called modern algebra or abstract algebra, as established by the influence and works of Emmy Noether,\nand popularized by Van der Waerden's book Moderne Algebra.\n\nSome types of algebraic structures have useful and often fundamental properties in many areas of mathematics. Their study became autonomous parts of algebra, and it includes the following:\n\ngroup theory\n\nfield theory\n\nvector spaces, whose study is essentially the same as linear algebra\n\nring theory\n\ncommutative algebra, which is the study of commutative rings, includes the study of polynomials, and is a foundational part of algebraic geometry\n\nhomological algebra\n\nLie algebra and Lie group theory\n\nBoolean algebra, which is widely used for the study of the logical structure of computers\n\nThe study of types of algebraic structures as mathematical objects is the purpose of universal algebra and category theory. The latter applies to every mathematical structure (not only algebraic ones). At its origin, it was introduced, together with homological algebra, to allow the algebraic study of non-algebraic objects such as topological spaces; this particular area of application is called algebraic topology.\n\nCalculus and analysis\n\nCalculus, formerly called infinitesimal calculus, was introduced independently and simultaneously by 17th-century mathematicians Newton and Leibniz. It is fundamentally the study of the relationship between variables that depend continuously on each other. Calculus was expanded in the 18th century by Euler with the introduction of the concept of a function and many other results. Presently, \"calculus\" refers mainly to the elementary part of this theory, and \"analysis\" is commonly used for advanced parts.\n\nAnalysis is further subdivided into real analysis, where variables represent real numbers, and complex analysis, where variables represent complex numbers. Analysis includes many subareas shared by other areas of mathematics, which include:\n\nMultivariable calculus\n\nFunctional analysis, where variables represent varying functions\n\nIntegration, measure theory and potential theory, all strongly related with probability theory on a continuum\n\nOrdinary differential equations\n\nPartial differential equations\n\nNumerical analysis, mainly devoted to the computation of solutions of ordinary and partial differential equations that arise in many applications\n\nDiscrete mathematics\n\nDiscrete mathematics, broadly speaking, is the study of individual, countable mathematical objects. An example is the set of all integers. Because the objects of study here are discrete, the methods of calculus and mathematical analysis do not directly apply. Algorithms—especially their implementation and computational complexity—play a major role in discrete mathematics.\n\nThe four color theorem and optimal sphere packing were two major problems of discrete mathematics solved in the second half of the 20th century. The P versus NP problem, which remains open to this day, is also important for discrete mathematics, since its solution would potentially impact a large number of computationally difficult problems.\n\nDiscrete mathematics includes:\n\nCombinatorics, the art of enumerating mathematical objects that satisfy some given constraints. Originally, these objects were elements or subsets of a given set; this has been extended to various objects, which establishes a strong link between combinatorics and other parts of discrete mathematics. For example, discrete geometry includes counting configurations of geometric shapes.\n\nGraph theory and hypergraphs\n\nCoding theory, including error correcting codes and a part of cryptography\n\nMatroid theory\n\nDiscrete geometry\n\nDiscrete probability distributions\n\nGame theory (although continuous games are also studied, most common games, such as chess and poker, are discrete)\n\nDiscrete optimization, including combinatorial optimization, integer programming, constraint programming\n\nMathematical logic and set theory\n\nThe two subjects of mathematical logic and set theory have belonged to mathematics since the end of the 19th century. Before this period, sets were not considered to be mathematical objects, and logic, although used for mathematical proofs, belonged to philosophy and was not specifically studied by mathematicians.\n\nBefore Cantor's study of infinite sets, mathematicians were reluctant to consider actually infinite collections, and considered infinity to be the result of endless enumeration. Cantor's work offended many mathematicians not only by considering actually infinite sets but by showing that this implies different sizes of infinity, per Cantor's diagonal argument. This led to the controversy over Cantor's set theory. In the same period, various areas of mathematics concluded that the former intuitive definitions of the basic mathematical objects were insufficient for ensuring mathematical rigor.\n\nThis became the foundational crisis of mathematics. It was eventually solved in mainstream mathematics by systematizing the axiomatic method inside a formalized set theory. Roughly speaking, each mathematical object is defined by the set of all similar objects and the properties that these objects must have. For example, in Peano arithmetic, the natural numbers are defined by \"zero is a number\", \"each number has a unique successor\", \"each number but zero has a unique predecessor\", and some rules of reasoning. This mathematical abstraction from reality is embodied in the modern philosophy of formalism, as founded by David Hilbert around 1910.\n\nThe \"nature\" of the objects defined this way is a philosophical problem that mathematicians leave to philosophers, even if many mathematicians have opinions on this nature, and use their opinion—sometimes called \"intuition\"—to guide their study and proofs. The approach allows considering \"logics\" (that is, sets of allowed deducing rules), theorems, proofs, etc. as mathematical objects, and to prove theorems about them. For example, Gödel's incompleteness theorems assert, roughly speaking, that in every consistent formal system that contains the natural numbers, there are theorems that are true (that is, provable in a stronger system), but not provable inside the system. This approach to the foundations of mathematics was challenged during the first half of the 20th century by mathematicians led by Brouwer, who promoted intuitionistic logic (which explicitly lacks the law of excluded middle).\n\nThese problems and debates led to a wide expansion of mathematical logic, with subareas such as model theory (modeling some logical theories inside other theories), proof theory, type theory, computability theory and computational complexity theory. Although these aspects of mathematical logic were introduced before the rise of computers, their use in compiler design, formal verification, program analysis, proof assistants and other aspects of computer science contributed in turn to the expansion of these logical theories.\n\nComputational mathematics\n\nComputational mathematics is the study of mathematical problems that are typically too large for human computing capacity. \n\nPart of computational mathematics involves numerical analysis, which is devoted to computation with approximations of real numbers (floating-point arithmetic). Numerical analysis provides methods for problems in analysis using functional analysis and approximation theory. Numerical analysis broadly includes the study of approximation and discretization, with special focus on rounding errors. Numerical analysis and, more broadly, scientific computing, also study non-analytic topics of mathematical science, especially algorithmic-matrix-and-graph theory. \n\nAnother area of computational mathematics is computer algebra, which consists mainly of the manipulation of mathematical formulas on a computer.\n\nAutomated theorem proving, which includes proof assistants and proof checkers, is another area of computational mathematics that is used for formal verification and allows formal proof of difficult theorems of mathematics such as the Feit–Thompson theorem on finite groups.\n\nAlgorithmics, a large part of discrete mathematics, and public key cryptography are also often considered as a part of computational mathematics.\n\nHistory\n\nEtymology\n\nThe word mathematics comes from the Ancient Greek word máthēma (μάθημα), meaning 'something learned, knowledge, mathematics', and the derived expression mathēmatikḗ tékhnē (μαθηματικὴ τέχνη), meaning 'mathematical science'. It entered the English language during the Late Middle English period through French and Latin. \n\nTraditionally, one of the two main schools of thought in Pythagoreanism was known as the mathēmatikoi (μαθηματικοί)—which at the time meant \"learners\" rather than \"mathematicians\" in the modern sense. The Pythagoreans were likely the first to constrain the use of the word to just the study of arithmetic and geometry. By the time of Aristotle (384–322 BC), this meaning was fully established.\n\nIn Latin and English, until around 1700, the term mathematics more commonly meant \"astrology\" (or sometimes \"astronomy\") rather than \"mathematics\"; the meaning gradually changed to its present one from about 1500 to 1800. This change"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q395",
  "label": "mathematics",
  "description": "field of study",
  "aliases": [
   "math",
   "maths"
  ],
  "claims": {
   "P31": [
    "Q11862829",
    "Q4671286"
   ],
   "P279": [
    "Q7991"
   ],
   "P361": [
    "Q1881523",
    "Q816264",
    "Q475023"
   ],
   "P527": [
    "Q12479",
    "Q8087",
    "Q3968",
    "Q217413",
    "Q12482",
    "Q12483",
    "Q5862903",
    "Q42989",
    "Q7754",
    "Q76592",
    "Q1166618",
    "Q11205"
   ],
   "P460": [
    "Q4387017"
   ]
  },
  "revision_id": "2563997639",
  "value_labels": {
   "Q11862829": "academic discipline",
   "Q4671286": "academic major",
   "Q7991": "natural science",
   "Q1881523": "science, technology, engineering, and mathematics",
   "Q816264": "formal science",
   "Q475023": "exact science",
   "Q12479": "number theory",
   "Q8087": "geometry",
   "Q3968": "algebra",
   "Q217413": "category theory",
   "Q12482": "set theory",
   "Q12483": "statistics",
   "Q5862903": "probability theory",
   "Q42989": "topology",
   "Q7754": "mathematical analysis",
   "Q76592": "combinatorics",
   "Q1166618": "mathematical logic",
   "Q11205": "arithmetic",
   "Q4387017": "mathematical sciences"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1952935",
  "label": "Mathematics",
  "description": "1985 studio album by Melissa Manchester",
  "aliases": [
   "Ma+hematics"
  ],
  "claims": {
   "P31": [
    "Q482994"
   ],
   "P361": [
    "Q115274341"
   ]
  },
  "revision_id": "2506481133",
  "value_labels": {
   "Q482994": "album",
   "Q115274341": "Melissa Manchester's albums in chronological order"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q50816266",
  "label": "Mathematics",
  "description": "Academic journal published by MDPI AG , covering the subjects: Science: Mathematics",
  "aliases": [],
  "claims": {
   "P31": [
    "Q737498",
    "Q773668"
   ]
  },
  "revision_id": "2568611667",
  "value_labels": {
   "Q737498": "academic journal",
   "Q773668": "open-access journal"
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
  "ancestor_of": "Q395",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4671286",
  "label": "academic major",
  "description": "focus of academic study leading to a degree",
  "aliases": [
   "main speciality of study",
   "main field of study",
   "speciality of study",
   "field of study",
   "main discipline",
   "major discipline",
   "university discipline",
   "major concentration",
   "major",
   "university major"
  ],
  "claims": {
   "P279": [
    "Q11862829"
   ],
   "P460": [
    "Q2267705"
   ]
  },
  "revision_id": "2541824123",
  "ancestor_of": "Q395",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7991",
  "label": "natural science",
  "description": "branch of science that uses empirical evidence to describe, explain, and test phenomena and regularities in the natural world",
  "aliases": [
   "natural sciences",
   "natural history",
   "science"
  ],
  "claims": {
   "P31": [
    "Q2465832",
    "Q11862829"
   ],
   "P279": [
    "Q336"
   ],
   "P527": [
    "Q7094",
    "Q420",
    "Q2329",
    "Q8008",
    "Q188847",
    "Q864928",
    "Q413",
    "Q1195766"
   ],
   "P460": [
    "Q113976585"
   ],
   "P1889": [
    "Q484591",
    "Q8027727"
   ]
  },
  "revision_id": "2567754437",
  "ancestor_of": "Q395",
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
  "ancestor_of": "Q395",
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
  "ancestor_of": "Q395",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2465832",
  "label": "branch of science",
  "description": "field of scientific study",
  "aliases": [
   "discipline of science",
   "field of science",
   "branches of science",
   "subdivision of science",
   "scientific field",
   "research area",
   "type of science"
  ],
  "claims": {
   "P31": [
    "Q110402867"
   ],
   "P279": [
    "Q1047113"
   ],
   "P460": [
    "Q11862829",
    "Q2267705"
   ],
   "P1889": [
    "Q3242580"
   ]
  },
  "revision_id": "2563543766",
  "ancestor_of": "Q395",
  "level": 2,
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
  "ancestor_of": "Q395",
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
  "ancestor_of": "Q1952935",
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
  "ancestor_of": "Q1952935",
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
  "ancestor_of": "Q1952935",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q737498",
  "label": "academic journal",
  "description": "peer-reviewed periodical relating to an academic discipline",
  "aliases": [
   "scholarly journal",
   "journal",
   "learned journal",
   "academic review",
   "peer-reviewed journal",
   "refereed journal"
  ],
  "claims": {
   "P31": [
    "Q21114848"
   ],
   "P279": [
    "Q685935",
    "Q1002697",
    "Q49850"
   ],
   "P361": [
    "Q5246046"
   ],
   "P527": [
    "Q18918145"
   ],
   "P1889": [
    "Q5633421"
   ]
  },
  "revision_id": "2556595743",
  "ancestor_of": "Q50816266",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q773668",
  "label": "open-access journal",
  "description": "journal meant to have no access barriers (such as cost) for readers",
  "aliases": [
   "open access journal",
   "OAJ",
   "OA journal",
   "OA journals",
   "gold open access",
   "Gold Open Access",
   "gold OA",
   "OA academic journal"
  ],
  "claims": {
   "P279": [
    "Q737498",
    "Q1327300",
    "Q1293664"
   ],
   "P1889": [
    "Q5253501"
   ]
  },
  "revision_id": "2549457733",
  "ancestor_of": "Q50816266",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21114848",
  "label": "magazine genre",
  "description": "type of genre",
  "aliases": [
   "genre of magazine",
   "periodicals genre",
   "journal genre"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q483394"
   ]
  },
  "revision_id": "2567686963",
  "ancestor_of": "Q50816266",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q685935",
  "label": "trade magazine",
  "description": "periodical dedicated to a particular field",
  "aliases": [
   "professional magazine",
   "trade rag",
   "trade journal",
   "trade publication"
  ],
  "claims": {
   "P31": [
    "Q21114848"
   ],
   "P279": [
    "Q41298"
   ],
   "P361": [
    "Q1391420"
   ],
   "P1889": [
    "Q55630524",
    "Q918727"
   ]
  },
  "revision_id": "2523496555",
  "ancestor_of": "Q50816266",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1002697",
  "label": "periodical",
  "description": "publication type, serial publication that appears in a new edition on a regular schedule",
  "aliases": [
   "periodical publication",
   "periodical literature",
   "periodicals"
  ],
  "claims": {
   "P31": [
    "Q121132955",
    "Q39725049",
    "Q110452794"
   ],
   "P279": [
    "Q2217301",
    "Q340169"
   ],
   "P527": [
    "Q28869365",
    "Q1238720"
   ]
  },
  "revision_id": "2567619481",
  "ancestor_of": "Q50816266",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q49850",
  "label": "journal",
  "description": "written medium (duplicate item)",
  "aliases": [],
  "claims": {
   "P31": [
    "Q17362920"
   ],
   "P279": [
    "Q1261026",
    "Q1002697"
   ],
   "P361": [
    "Q11030"
   ],
   "P460": [
    "Q41298"
   ],
   "P1889": [
    "Q361785"
   ]
  },
  "revision_id": "2516833327",
  "ancestor_of": "Q50816266",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1327300",
  "label": "electronic journal",
  "description": "magazine published in digital format",
  "aliases": [
   "e-journal",
   "ejournal",
   "electronical serial"
  ],
  "claims": {
   "P279": [
    "Q15938550",
    "Q41298"
   ],
   "P460": [
    "Q3428753",
    "Q847906",
    "Q1153191"
   ]
  },
  "revision_id": "2567576229",
  "ancestor_of": "Q50816266",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1293664",
  "label": "open content",
  "description": "content that is openly accessible and modifiable to others",
  "aliases": [
   "free content"
  ],
  "claims": {
   "P279": [
    "Q1260632"
   ],
   "P361": [
    "Q2251455"
   ],
   "P460": [
    "Q14075"
   ]
  },
  "revision_id": "2482211679",
  "ancestor_of": "Q50816266",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-06009822-n",
  "lemmas": [
   "mathematics",
   "math",
   "maths"
  ],
  "gloss": "a science (or group of related sciences) dealing with the logic of quantity and shape and arrangement",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06008975-n"
   ],
   "hyponym": [
    "oewn-06013012-n",
    "oewn-06027371-n"
   ]
  },
  "relation_targets": {
   "oewn-06008975-n": "science, scientific discipline",
   "oewn-06013012-n": "pure mathematics",
   "oewn-06027371-n": "applied mathematics, applied math"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 6: Spanish (`de8aeltv9z`)

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
[
 {
  "title": "Spanish language",
  "revision_id": "1378284919",
  "matched_by": "redirect",
  "text": "Spanish (español) or Castilian (castellano) is a Romance language of the Indo-European language family that evolved from the Vulgar Latin spoken on the Iberian Peninsula of Europe. It originated in the Kingdom of Castile, a kingdom in north-central Iberia. Today, it is a global language with 519 million native speakers, mainly in the Americas and Spain, and about 636 million speakers total, including second-language speakers. Spanish is the official language of 21 countries, as well as one of the six official languages of the United Nations. Spanish is the world's second-most spoken native language after Mandarin Chinese; the world's fourth-most spoken language overall after English, Mandarin Chinese, and Hindustani (Hindi-Urdu); and the world's most widely spoken Romance language. The country with the largest population of native speakers is Mexico, with 130M speakers, almost triple that of the United States of America. \n\nSpanish is part of the Ibero-Romance language group, which evolved from several dialects of Vulgar Latin in Iberia after the collapse of the Western Roman Empire in the 5th century. The oldest Latin texts with traces of Spanish come from mid-northern Iberia in the 9th century, and the first systematic written use of the language happened in Toledo, a prominent city of the Kingdom of Castile, in the 13th century. Spanish colonialism in the early modern period spurred the introduction of the language to overseas locations, most notably to the Americas.\n\nAs a Romance language, Spanish is a descendant of Latin. About 75% of modern Spanish vocabulary is Latin in origin, including Latin borrowings from Ancient Greek. Alongside English and French, it is also one of the most taught foreign languages throughout the world. Spanish is well represented in the humanities and social sciences. Spanish is also the third most used language on the internet by number of users after English and Chinese and the second most used language by number of websites after English.\n\nSpanish is used as an official language by many international organizations, including the United Nations, European Union, Organization of Ibero-American States, Organization of American States, Union of South American Nations, Community of Latin American and Caribbean States, African Union, and others.\n\nName of the language and etymology\n\nName of the language\n\nIn Spain and some other parts of the Spanish-speaking world, Spanish is called not only español but also castellano (Castilian), the language from the Kingdom of Castile, contrasting it with other languages spoken in Spain such as Galician, Basque, Asturian, Catalan/Valencian, Aragonese, Occitan and other minor languages.\n\nThe Spanish Constitution of 1978 uses the term castellano to define the official language of the whole of Spain, in contrast to las demás lenguas españolas (lit. 'the other Spanish languages'). Article III reads as follows:\n\nEl castellano es la lengua española oficial del Estado. ... Las demás lenguas españolas serán también oficiales en las respectivas Comunidades Autónomas...\n\nCastilian is the official Spanish language of the State. ... The other Spanish languages shall also be official in their respective Autonomous Communities...\n\nThe Royal Spanish Academy (Real Academia Española), on the other hand, currently uses the term español in its publications. However, from 1713 to 1923, it called the language castellano.\n\nThe Diccionario panhispánico de dudas (a language guide published by the Royal Spanish Academy) states that, although the Royal Spanish Academy prefers to use the term español in its publications when referring to the Spanish language, both terms—español and castellano—are regarded as synonymous and equally valid.\n\nEtymology\n\nThe term castellano is related to Castile (Castilla or archaically Castiella), the kingdom where the language was originally spoken. The name Castile, in turn, is usually assumed to be derived from castillo ('castle').\n\nIn the Middle Ages, the language spoken in Castile was generically referred to as Romance and later also as Lengua vulgar. Later in the period, it gained geographical specification as Romance castellano (romanz castellano, romanz de Castiella), lenguaje de Castiella, and ultimately simply as castellano (noun).\n\nDifferent etymologies have been suggested for the term español (Spanish). According to the Royal Spanish Academy, español derives from the Occitan word espaignol and that, in turn, derives from the Vulgar Latin *hispaniolus ('of Hispania'). Hispania was the Roman name for the entire Iberian Peninsula.\n\nThere are other hypotheses apart from the one suggested by the Royal Spanish Academy. Spanish philologist Ramón Menéndez Pidal suggested that the classic hispanus or hispanicus took the suffix -one from Vulgar Latin, as happened with other words such as bretón (Breton) or sajón (Saxon).\n\nHistory\n\nLike the other Romance languages, the Spanish language evolved from Vulgar Latin, which was brought to the Iberian Peninsula by the Romans during the Second Punic War, beginning in 210 BC. Several pre-Roman languages (also called Paleohispanic languages)—some distantly related to Latin as Indo-European languages, and some that are not related at all—were previously spoken in the Iberian Peninsula. These languages included Proto-Basque, Iberian, Lusitanian, Celtiberian and Gallaecian.\n\nThe first documents to show traces of what is today regarded as the precursor of modern Spanish are from the 9th century. Throughout the Middle Ages and into the modern era, the most important influences on the Spanish lexicon came from neighboring Romance languages—Mozarabic (Andalusi Romance), Navarro-Aragonese, Leonese, Catalan/Valencian, Portuguese, Galician, Occitan, and later, French and Italian. Spanish also borrowed a considerable number of words from Andalusi Arabic, and a few from Basque. In addition, many more words were borrowed from Latin through the influence of written language and the liturgical language of the Church. The loanwords were taken from both Classical Latin and Renaissance Latin, the form of Latin in use at that time.\n\nAccording to the theories of Ramón Menéndez Pidal, local sociolects of Vulgar Latin evolved into Spanish, in the north of Iberia, in an area centered in the city of Burgos, and this dialect was later brought to the city of Toledo, where the written standard of Spanish was first developed, in the 13th century. In this formative stage, Spanish developed a strongly differing variant from its close cousin, Leonese, and, according to some authors, was distinguished by a heavy Basque influence (see Iberian Romance languages). This distinctive dialect spread to southern Spain with the advance of the Reconquista, and meanwhile gathered a sizable lexical influence from the Arabic of Al-Andalus, much of it indirectly, through the Romance Mozarabic dialects (some 4,000 Arabic-derived words, make up about 8% of the language today). The written standard for this new language was developed in the cities of Toledo, in the 13th to 16th centuries, and Madrid, from the 1570s.\n\nThe development of the Spanish sound system from that of Vulgar Latin exhibits most of the changes that are typical of Western Romance languages, including lenition of intervocalic consonants (thus Latin vīta > Spanish vida). The diphthongization of Latin stressed short e and o—which occurred in open syllables in French and Italian, but not at all in Catalan or Portuguese—is found in both open and closed syllables in Spanish, as shown in the following table:\n\nSpanish is marked by palatalization of the Latin double consonants (geminates) nn and ll (thus Latin\nannum > Spanish año, and Latin anellum > Spanish\nanillo).\n\nThe consonant written u or v in Latin and pronounced [w] in Classical Latin had probably \"fortified\" to a bilabial fricative /β/ in Vulgar Latin. In early Spanish (but not in Catalan or Portuguese) it merged with the consonant written b (a bilabial with plosive and fricative allophones). In modern Spanish, there is no difference between the pronunciation of orthographic b and v.\n\nTypical of Spanish (as also of neighboring Gascon extending as far north as the Gironde estuary, and found in a small area of Calabria), attributed by some scholars to a Basque substratum was the mutation of Latin initial f into h- whenever it was followed by a vowel that did not diphthongize. The h-, still preserved in spelling, is now silent in most varieties of the language, although in some Andalusian and Caribbean dialects, it is still aspirated in some words. Because of borrowings from Latin and neighboring Romance languages, there are many f-/h- doublets in modern Spanish: Fernando and Hernando (both Spanish for \"Ferdinand\"), ferrero and herrero (both Spanish for \"smith\"), fierro and hierro (both Spanish for \"iron\"), and fondo and hondo (both words pertaining to depth in Spanish, though fondo means \"bottom\", while hondo means \"deep\"); additionally, hacer (\"to make\") is cognate to the root word of satisfacer (\"to satisfy\"), and hecho (\"made\") is similarly cognate to the root word of satisfecho (\"satisfied\").\n\nCompare the examples in the following table:\n\nSome consonant clusters of Latin also produced characteristically different results in these languages, as shown in the examples in the following table:\n\nIn the 15th and 16th centuries, Spanish underwent a dramatic change in the pronunciation of its sibilant consonants, known in Spanish as the reajuste de las sibilantes, which resulted in the distinctive velar [x] pronunciation of the letter ⟨j⟩ and—in a large part of Spain—the characteristic interdental [θ] (\"th-sound\") for the letter ⟨z⟩ (and for ⟨c⟩ before ⟨e⟩ or ⟨i⟩). See History of Spanish (Modern development of the Old Spanish sibilants) for details.\n\nThe Gramática de la lengua castellana, written in Salamanca in 1492 by Elio Antonio de Nebrija, was the first grammar written for a modern European language. According to a popular anecdote, when Nebrija presented it to Queen Isabella I, she asked him what was the use of such a work, and he answered that language is the instrument of empire. In his introduction to the grammar, dated 18 August 1492, Nebrija wrote that \"... language was always the companion of empire.\"\n\nFrom the 16th century onwards, the language was taken to the Spanish-discovered America and the Spanish East Indies via Spanish colonization of America. Miguel de Cervantes, author of Don Quixote, is such a well-known reference in the world that Spanish is often called la lengua de Cervantes (\"the language of Cervantes\").\n\nIn the 20th century, Spanish was introduced to Equatorial Guinea and the Western Sahara, and to areas of the United States that had not been part of the Spanish Empire, such as Spanish Harlem in New York City. For details on borrowed words and other external influences upon Spanish, see Influences on the Spanish language.\n\nGeographical distribution\n\nSpanish is the primary language in 20 countries worldwide. As of 2025, it is estimated that about 519 million people speak Spanish as a native language, making it the second most spoken language by number of native speakers. An additional 117 million speak Spanish as a second or foreign language, making it the fourth most spoken language in the world overall after English, Mandarin Chinese, and Hindi with a total number of 636 million speakers. Spanish is also the third most used language on the Internet, after English and Chinese.\n\nEurope\n\nSpanish is the official language of Spain. Upon the emergence of the Castilian Crown as the dominant power in the Iberian Peninsula by the end of the Middle Ages, the Romance vernacular associated with this polity became increasingly used in instances of prestige and influence, and the distinction between \"Castilian\" and \"Spanish\" started to become blurred. Hard policies imposing the language's hegemony in an intensely centralising Spanish state were established from the 18th century onward.\n\nOther European territories in which it is also widely spoken include Gibraltar and Andorra.\n\nSpanish is also spoken by immigrant communities in other European countries, such as the United Kingdom, France, Italy, and Germany. Spanish is the most widely studied Romance language in Europe. According to Eurostat data, about 27% of secondary school students in the European Union study Spanish, making it the second most taught foreign language after English and the most studied Romance language on the continent. Spanish is an official language of the European Union.\n\nAmericas\nHispanic America\n\nToday, the majority of the Spanish speakers live in Hispanic America. Nationally, Spanish is the official language—either de facto or de jure—of Argentina, Bolivia (co-official with 36 indigenous languages), Chile, Colombia, Costa Rica, Cuba, Dominican Republic, Ecuador, El Salvador, Guatemala, Honduras, Mexico (co-official with 63 indigenous languages), Nicaragua, Panama, Paraguay (co-official with Guaraní), Peru (co-official with Quechua, Aymara, and \"the other indigenous languages\"), Puerto Rico (co-official with English), Uruguay, and Venezuela.\n\nUnited States\n\nThe Spanish language has a long history in the territory of the current-day United States dating back to the 16th century. In the wake of the 1848 Guadalupe Hidalgo Treaty, hundreds of thousands of Spanish speakers became a minoritized community in the United States. The 20th century saw further massive growth of Spanish speakers in areas where they had been hitherto scarce.\n\nAccording to the 2020 census, over 60 million people of the U.S. population were of Hispanic or Hispanic American by origin. In turn, 41.8 million people in the United States aged five or older speak Spanish at home, or about 13% of the population. Spanish predominates in the unincorporated territory of Puerto Rico, where it is also an official language along with English.\n\nSpanish is by far the most common second language in the country, with over 50 million total speakers if non-native or second-language speakers are included. While English is the de facto national language of the country, Spanish is often used in public services and notices at the federal and state levels. Spanish is also used in administration in the state of New Mexico. The language has a strong influence in major metropolitan areas such as those of Los Angeles, San Diego, Miami, San Antonio, New York, San Francisco, Dallas, Tucson and Phoenix of the Arizona Sun Corridor, as well as more recently, Chicago, Las Vegas, Boston, Denver, Houston, Indianapolis, Oklahoma City, Philadelphia, Cleveland, Salt Lake City, Atlanta, Nashville, Orlando, Tampa, Raleigh and Baltimore-Washington, D.C. due to 20th- and 21st-century immigration.\n\nRest of the Americas\n\nAlthough Spanish has no official recognition in the former British colony of Belize (known until 1973 as British Honduras) where English is the sole official language, according to the 2022 census, 54% of the total population are able to speak the language.\n\nDue to its proximity to Spanish-speaking countries and small existing native Spanish speaking minority, Trinidad and Tobago has implemented Spanish language teaching into its education system. The Trinidadian and Tobagonian government launched the Spanish as a First Foreign Language (SAFFL) initiative in March 2005.\n\nSpanish has historically had a significant presence on the Dutch Caribbean islands of Aruba, Bonaire and Curaçao (ABC Islands) throughout the centuries and in present times. The majority of the populations of each island (especially Aruba) speak Spanish at varying although often high degrees of fluency. The local language Papiamentu (or Papiamento in Aruba) is heavily influenced by Venezuelan Spanish.\n\nIn addition to sharing most of its borders with Spanish-speaking countries, the creation of Mercosur in the early 1990s induced a favorable situation for the promotion of Spanish language teaching in Brazil. In 2005, the National Congress of Brazil approved a bill, signed into law by the President, making it mandatory for schools to offer Spanish as an alternative foreign language course in both public and private secondary schools in Brazil. In September 2016 this law was revoked by Michel Temer after the impeachment of Dilma Rousseff. In many border towns and villages along Paraguay and Uruguay, a mixed language known as Portuñol is spoken.\n\nAfrica\nSub-Saharan Africa\n\nEquatorial Guinea is the only Spanish-speaking country located entirely in Africa, with the language introduced during the Spanish colonial period. Enshrined in the constitution as an official language (alongside French and Portuguese), Spanish features prominently in the Equatoguinean education system and is the primary language used in government and business. Spanish is spoken as a native language by a small minority in Equatorial Guinea, primarily in larger cities. The Instituto Cervantes estimates that 87.7% of the population is fluent in Spanish. The proportion of proficient Spanish speakers in Equatorial Guinea exceeds the proportion of proficient speakers in other West and Central African nations of their respective colonial languages.\n\nSpanish is spoken by very small communities in Angola due to Cuban influence from the Cold War and in South Sudan among South Sudanese natives that relocated to Cuba during the Sudanese wars and returned for their country's independence.\n\nNorth Africa and Macaronesia\n\nSpanish is also spoken in the integral territories of Spain in Africa, namely the cities of Ceuta and Melilla and the Canary Islands, located in the Atlantic Ocean some 100 km (62 mi) off the northwest of the African mainland. The Spanish spoken in the Canary Islands traces its origins back to the Castilian conquest in the 15th century, and, in addition to a resemblance to Western Andalusian speech patterns, it also features strong influence from the Spanish varieties spoken in the Americas, which in turn have also been influenced historically by Canarian Spanish. The Spanish spoken in North Africa by native bilingual speakers of Arabic or Berber who also speak Spanish as a second language features characteristics involving the variability of the vowel system.\n\nWhile far from its heyday during the Spanish protectorate in Morocco, the Spanish language has some presence in northern Morocco, stemming for example from the availability of certain Spanish-language media. According to a 2012 survey by Morocco's Royal Institute for Strategic Studies (IRES), penetration of Spanish in Morocco reaches 4.6% of the population. Many northern Moroccans have rudimentary knowledge of Spanish, with Spanish being particularly significant in areas adjacent to Ceuta and Melilla. Spanish also has a presence in the education system of the country (through either selected education centers implementing Spain's education system, primarily located in the North, or the availability of Spanish as foreign language subject in secondary education).\n\nIn Western Sahara, formerly Spanish Sahara, a primarily Hassaniya Arabic-speaking territory, Spanish was officially spoken as the language of the colonial administration during the late 19th and 20th centuries. Today, Spanish is present in the partially-recognized Sahrawi Arab Democratic Republic as its secondary official language, and in the Sahrawi refugee camps in Tindouf (Algeria), where the Spanish language is still taught as a second language, largely by Cuban educators.\n\nSpanish is also an official language of the African Union.\n\nAsia\n\nSpanish was an official language of the Philippines from the beginning of Spanish administration in 1565 to a constitutional change in 1973. During Spanish colonization, it was the language of government, trade, and education, and was spoken as a first language by Spaniards and educated Filipinos (Ilustrados). Despite a public education system set up by"
 },
 {
  "title": "Spanish (goat breed)",
  "revision_id": "1372690872",
  "matched_by": "title-minus-qualifier",
  "text": "The Spanish goat is an American breed of domestic goat. It derives from European goats brought to the Americas in the sixteenth century by the conquistadores.\n\nIt is kept both for meat and for vegetation management, and is used mainly for clearing brush and other undesirable plant species from pasture land. Both it and cross-breeds deriving from it may also be known as 'brush', 'scrub' or 'woods' goats.\n\nHistory\n\nEuropean goats were brought to the Americas in the sixteenth century by the conquistadores and were soon introduced to the areas that later became parts of the United States and Mexico.\n\nBoth purebred stock of Spanish descent and cross-bred animals of indeterminate origin may at times be referred to as Spanish goats. The Spanish has been cross-bred with imported goat breeds both for cashmere and for meat production; most cross-bred goats show hybrid vigor, but cross-breeding may reduce the number of purebred stock. The conservation status of the breed is listed by the Livestock Conservancy as 'recovering', its lowest level of concern. \n\nCharacteristics\n\nThe Spanish goat has the ability to breed out of season. It is hardy and able to survive and thrive under adverse conditions, making it well suited for rangeland management.\n\nBlack coats are common, but any color or pattern is accepted.\n\nReferences"
 },
 {
  "title": "Spanish (song)",
  "revision_id": "1332329514",
  "matched_by": "title-minus-qualifier",
  "text": "\"Spanish\" is a song by British singer Craig David. It was written by David, Trevor Henry, and Anthony Marshall for his second album, Slicker Than Your Average (2002), with production helmed by the latter. The song was released as the album's fourth single and became a tenth top ten hit on the UK Singles Chart, peaking at number 8 and spending six weeks inside the top 75. \"Spanish\" saw David incorporate Spanish elements into his music for the first time, including a feature by Spanish rapper Duke One. In Australia, \"Spanish\" was skipped and \"World Filled with Love\" was released there as the fourth single instead.\n\nMusic video\n\nA video for \"Spanish\" was directed by directing team Calabazitaz.\n\nTrack listing\n\nNotes\n\n signifies an additional producer\n\nCharts\n\nRelease history\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q1321",
  "label": "Spanish",
  "description": "Romance language originating in the Iberian Peninsula",
  "aliases": [
   "Castilian",
   "Spanish language",
   "Castilian language"
  ],
  "claims": {
   "P31": [
    "Q33742",
    "Q34770",
    "Q1288568",
    "Q20162172"
   ],
   "P279": [
    "Q71924",
    "Q1377152"
   ],
   "P527": [
    "Q7162990",
    "Q56649449",
    "Q1006465",
    "Q820569",
    "Q5840069",
    "Q1115875",
    "Q8778504"
   ],
   "P1889": [
    "Q16775638",
    "Q241649"
   ]
  },
  "revision_id": "2572875287",
  "value_labels": {
   "Q33742": "natural language",
   "Q34770": "language",
   "Q1288568": "modern language",
   "Q20162172": "human language",
   "Q71924": "Castilian",
   "Q1377152": "West Iberian",
   "Q7162990": "Peninsular Spanish",
   "Q56649449": "Latin American Spanish",
   "Q1006465": "Philippine Spanish",
   "Q820569": "Equatoguinean Spanish",
   "Q5840069": "Saharan Spanish",
   "Q1115875": "Colombian Spanish",
   "Q8778504": "",
   "Q16775638": "Español",
   "Q241649": "Spanish"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3492674",
  "label": "Spanish",
  "description": "North American breed of goat",
  "aliases": [
   "brush goat",
   "scrub goat"
  ],
  "claims": {
   "P31": [
    "Q15622387"
   ],
   "P279": [
    "Q2934"
   ]
  },
  "revision_id": "2538636364",
  "value_labels": {
   "Q15622387": "goat breed",
   "Q2934": "goat"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7573131",
  "label": "Spanish",
  "description": "song by Craig David",
  "aliases": [
   "Spanish (song)"
  ],
  "claims": {
   "P31": [
    "Q134556"
   ],
   "P1889": [
    "Q3492565"
   ]
  },
  "revision_id": "2502357291",
  "value_labels": {
   "Q134556": "single",
   "Q3492565": "Spanish"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q33742",
  "label": "natural language",
  "description": "language naturally spoken or signed by humans, as opposed to \"constructed\" and \"formal\" languages",
  "aliases": [
   "ordinary language",
   "natlang"
  ],
  "claims": {
   "P31": [
    "Q20829075",
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q20162172"
   ],
   "P1889": [
    "Q20162172",
    "Q57159190"
   ]
  },
  "revision_id": "2565434281",
  "ancestor_of": "Q1321",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q34770",
  "label": "language",
  "description": "particular system of communication, often named for the region or peoples that use it",
  "aliases": [
   "idiom",
   "particular language",
   "lang",
   "languages",
   "idioms",
   "human language"
  ],
  "claims": {
   "P31": [
    "Q28923954"
   ],
   "P279": [
    "Q17376908",
    "Q3622126"
   ],
   "P361": [
    "Q315"
   ],
   "P460": [
    "Q10485156",
    "Q20162172",
    "Q337968"
   ],
   "P1889": [
    "Q2395542",
    "Q9614",
    "Q315",
    "Q257716",
    "Q192161",
    "Q113374538",
    "Q4113741"
   ]
  },
  "revision_id": "2569999028",
  "ancestor_of": "Q1321",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1288568",
  "label": "modern language",
  "description": "language in current use",
  "aliases": [
   "living language",
   "modern languages"
  ],
  "claims": {
   "P31": [
    "Q20829075"
   ],
   "P279": [
    "Q20162172"
   ],
   "P460": [
    "Q1942036"
   ]
  },
  "revision_id": "2567707150",
  "ancestor_of": "Q1321",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20162172",
  "label": "human language",
  "description": "set of all languages currently or formerly spoken, written, or signed by humans (excluding computer languages and mathematical/logically-formal languages)",
  "aliases": [
   "human languages"
  ],
  "claims": {
   "P31": [
    "Q28923954",
    "Q20829075"
   ],
   "P279": [
    "Q34770"
   ],
   "P460": [
    "Q34770"
   ],
   "P1889": [
    "Q33742"
   ]
  },
  "revision_id": "2552502910",
  "ancestor_of": "Q1321",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q71924",
  "label": "Castilian",
  "description": "branch of West Iberian languages",
  "aliases": [
   "Castilic languages",
   "Castilian languages",
   "Castilic"
  ],
  "claims": {
   "P31": [
    "Q25295"
   ],
   "P279": [
    "Q1377152"
   ],
   "P527": [
    "Q1321",
    "Q30007",
    "Q36196",
    "Q72256",
    "Q2655227",
    "Q2982964"
   ]
  },
  "revision_id": "2560198729",
  "ancestor_of": "Q1321",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1377152",
  "label": "West Iberian",
  "description": "branch of the Ibero-Romance languages",
  "aliases": [
   "West Ibero-Romance languages",
   "West Iberian languages",
   "West Ibero-Romance",
   "Western Iberian",
   "Western Iberian languages",
   "Western Ibero-Romance",
   "Western Ibero-Romance languages",
   "Western Iberian Romance",
   "Western Iberian Romance languages",
   "West Iberian Romance",
   "West Iberian Romance languages"
  ],
  "claims": {
   "P31": [
    "Q25295"
   ],
   "P279": [
    "Q749533"
   ]
  },
  "revision_id": "2560160836",
  "ancestor_of": "Q1321",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20829075",
  "label": "type of language",
  "description": "Wikidata metaclass of langoid in linguistic typology",
  "aliases": [
   "language type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q28923954",
    "Q96251598"
   ]
  },
  "revision_id": "2562082474",
  "ancestor_of": "Q1321",
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
  "ancestor_of": "Q1321",
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
  "ancestor_of": "Q1321",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q28923954",
  "label": "languoid class",
  "description": "e.g. dialect, language, macrolanguage, language subfamily, family, or superfamily; each instance of these is a subclass of languoid",
  "aliases": [],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q4120621"
   ]
  },
  "revision_id": "2572259393",
  "ancestor_of": "Q1321",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q17376908",
  "label": "languoid",
  "description": "language, variety of a language, or group of languages",
  "aliases": [],
  "claims": {
   "P31": [
    "Q28923954"
   ],
   "P279": [
    "Q141152464"
   ]
  },
  "revision_id": "2572259528",
  "ancestor_of": "Q1321",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3622126",
  "label": "conceptual system",
  "description": "system composed of non-physical objects, i.e. ideas or concepts",
  "aliases": [
   "non-physical system"
  ],
  "claims": {
   "P31": [
    "Q96116695"
   ],
   "P279": [
    "Q58778",
    "Q16686448",
    "Q7048977"
   ]
  },
  "revision_id": "2572683027",
  "ancestor_of": "Q1321",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q25295",
  "label": "language family",
  "description": "group of languages related through descent from a common ancestor",
  "aliases": [
   "linguistic groups",
   "language groups",
   "linguistic family",
   "language group",
   "linguistic group",
   "family of languages",
   "language families",
   "families of languages",
   "linguistic families"
  ],
  "claims": {
   "P31": [
    "Q28923954",
    "Q140353512"
   ],
   "P279": [
    "Q17376908",
    "Q941501",
    "Q140353528"
   ],
   "P361": [
    "Q25521366",
    "Q949344"
   ],
   "P527": [
    "Q11820611"
   ],
   "P1889": [
    "Q839463"
   ]
  },
  "revision_id": "2565179738",
  "ancestor_of": "Q1321",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q749533",
  "label": "Iberian Romance",
  "description": "Romance languages developed on the Iberian Peninsula",
  "aliases": [
   "Ibero-Romance languages",
   "Iberian languages",
   "Iberian Romance languages",
   "Southwestern Shifted Romance",
   "Ibero-Romance",
   "Southwestern Shifted Romance languages"
  ],
  "claims": {
   "P31": [
    "Q25295"
   ],
   "P279": [
    "Q954321",
    "Q85380120",
    "Q2714388"
   ],
   "P527": [
    "Q1377152",
    "Q599958",
    "Q5886715"
   ]
  },
  "revision_id": "2569286778",
  "ancestor_of": "Q1321",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15622387",
  "label": "goat breed",
  "description": "",
  "aliases": [],
  "claims": {
   "P31": [
    "Q24017414"
   ],
   "P279": [
    "Q38829"
   ]
  },
  "revision_id": "2548999922",
  "ancestor_of": "Q3492674",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2934",
  "label": "goat",
  "description": "domesticated mammal raised for its meat and milk",
  "aliases": [
   "domestic goat",
   "goats",
   "Capra hircus",
   "C. hircus",
   "Capra aegagrus hircus",
   "C. aegagrus hircus",
   "C. a. hircus"
  ],
  "claims": {
   "P31": [
    "Q16521"
   ],
   "P279": [
    "Q57814795",
    "Q1797813"
   ],
   "P527": [
    "Q82025",
    "Q133105",
    "Q1105926",
    "Q7362",
    "Q7364",
    "Q60960"
   ],
   "P1889": [
    "Q24824197",
    "Q120920482"
   ]
  },
  "revision_id": "2567829570",
  "ancestor_of": "Q3492674",
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
  "ancestor_of": "Q3492674",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q38829",
  "label": "breed",
  "description": "group of domestic animals with a distinctive phenotype",
  "aliases": [
   "animal breed",
   "breed of animals",
   "domestic animal breed",
   "pedigreed animal",
   "pedigree animal",
   "pedigreed pet"
  ],
  "claims": {
   "P31": [
    "Q5962346",
    "Q631147",
    "Q12812139"
   ],
   "P279": [
    "Q21871294",
    "Q55983715"
   ],
   "P361": [
    "Q227675"
   ],
   "P1889": [
    "Q765421",
    "Q227675"
   ]
  },
  "revision_id": "2567779488",
  "ancestor_of": "Q3492674",
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
  "ancestor_of": "Q3492674",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q57814795",
  "label": "domesticated mammal",
  "description": "",
  "aliases": [],
  "claims": {
   "P279": [
    "Q57812611",
    "Q622852",
    "Q110551885"
   ]
  },
  "revision_id": "2550718831",
  "ancestor_of": "Q3492674",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1797813",
  "label": "productive animal",
  "description": "animal that is used by the people economically",
  "aliases": [
   "farm animal",
   "economically useful animal",
   "productive livestock",
   "utility animal",
   "farmed animal"
  ],
  "claims": {
   "P31": [
    "Q135106502",
    "Q55983715"
   ],
   "P279": [
    "Q57812559",
    "Q28877",
    "Q622852"
   ],
   "P460": [
    "Q622852"
   ]
  },
  "revision_id": "2563301391",
  "ancestor_of": "Q3492674",
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
  "ancestor_of": "Q7573131",
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
  "ancestor_of": "Q7573131",
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
  "ancestor_of": "Q7573131",
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
  "ancestor_of": "Q7573131",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-06979499-n",
  "lemmas": [
   "Spanish",
   "Spanish language"
  ],
  "gloss": "the Romance language spoken in most of Spain and the countries colonized by Spain",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06976693-n"
   ],
   "hyponym": [
    "oewn-06979859-n",
    "oewn-06979956-n",
    "oewn-06980102-n"
   ]
  },
  "relation_targets": {
   "oewn-06976693-n": "Romance, Romance language, Latinian language",
   "oewn-06979859-n": "Castilian, Castilian language",
   "oewn-06979956-n": "Judeo-Spanish, Ladino",
   "oewn-06980102-n": "Mexican Spanish"
  }
 },
 {
  "synset": "oewn-09752657-n",
  "lemmas": [
   "Spanish",
   "Spanish people"
  ],
  "gloss": "the people of Spain",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-08183451-n"
   ]
  },
  "relation_targets": {
   "oewn-08183451-n": "nation, land, country"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 6: Bachelor's in Nursing (`n7a094bha6`)

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

## Concept 4 of 6: Bachelor of Science in Nursing (`c4tp7yji9k`)

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
[
 {
  "title": "Bachelor of Science in Nursing",
  "revision_id": "1368112065",
  "matched_by": "title",
  "text": "The Bachelor of Science in Nursing (BSN, BScN) also known in some countries as a Bachelor of Nursing (BN) or Bachelor of Science (BS) with a Major in Nursing is an academic degree in the science and principles of nursing, granted by an accredited tertiary education provider. The course of study is typically three or four years. The difference in degree designation may relate to the amount of basic science courses required as part of the degree, with BScN and BSN degree curriculums requiring completion of more courses on math and natural sciences that are more typical of BSc degrees (e.g. calculus, physics, chemistry, biology) and BN curriculums more focused on nursing theory, nursing process, and teaching versions of general science topics that are adapted to be more specific and relevant to nursing practice.Nursing school students are generally required to take courses in social and behavioral sciences and liberal arts, including nutrition, anatomy, chemistry, mathematics, and English. In addition to those courses, experience in physical and social sciences, communication, leadership, and critical thinking is required for a bachelor's degree. BSN programs typically last 2–4 years. Someone who holds a BSN can work in private or public medical and surgical hospitals, physician's offices, home health care services, and nursing facilities. Having a BSN can result in more opportunities and better salary than just an associate degree.\n\nThe bachelor's degree prepares nurses for a wide variety of professional roles and graduate study. Course work includes nursing science, research, leadership, and related areas that inform the practice of nursing. It also provides the student with general education in math, humanities and social sciences. An undergraduate degree affords opportunities for greater career advancement and higher salary options. It is often a prerequisite for teaching, administrative, consulting and research roles.\n\nA Bachelor of Science in Nursing is not currently required for entry into professional nursing in all countries. In the US, there has been an effort for it to become the entry-level degree since 1964, when the American Nurses Association (ANA) advanced the position that the minimum preparation for beginning professional nursing practice should be a baccalaureate degree education in nursing. The Institute of Medicine (IOM) affirmed in 2010 that nurses should achieve higher levels of education and training through an improved education system that promotes seamless academic progression.\n\nIn the United States\n\nAccreditation\n\nThe Commission on Collegiate Nursing Education (CCNE) and the Accreditation Commission for Education in Nursing (ACEN) are the accreditation bodies for Bachelor of Science in Nursing programs in the United States. Both Commissions are officially recognized as national accreditation agencies that ensure quality standards for undergraduate to graduate nursing programs by the United States Secretary of Education.\n\nAccelerated BSN programs\n\nAccelerated Bachelor of Science in Nursing programs allow those who already have a bachelor's degree in a non-nursing field to obtain their nursing degree at an accelerated rate, which is why they are also commonly referred to as \"Second Degree Nursing Programs.\" These programs usually have strict prerequisites because the program coursework focuses solely on nursing. Accelerated BSN programs are typically anywhere from 12 to 24 months.\n\nBSN Completion or \"RN to BSN\" Programs\n\nThese programs are intended specifically for nurses with a diploma or associate degree in nursing who wish to \"top-up\" their current academic qualifications to a Bachelor of Science in nursing. A majority of these RN to BSN programs are offered online through colleges, universities, or other e-learning providers. In order to keep the programs up-to-date and relevant to the current healthcare system, the course material is updated regularly with feedback from registered nurses, nurse managers, healthcare professionals and even patients.\n\nBSN entry level into nursing in the future\n\nIn 2011, The Institute of Medicine recommended that by 2020, 80 percent of RNs hold a Bachelor of Science in nursing (BSN) degree. This was also noted in a report titled: Institute of Medicine's report on the Future of Nursing, and has been followed by a campaign to implement its recommendations. In this report a 2nd recommendation was made to focus on increasing the proportion of registered nurses (RNs) with a baccalaureate degree to 80% by 2020. Towards that effort the report recommends that educational associations, colleges, delivery organizations, governmental organizations, and funders develop the resources necessary to support this goal. These recommendations are consistent with other policy initiatives currently underway; for example, legislation requiring that nurses receive a baccalaureate degree within 10 years of initial licensure has been considered in New York, New Jersey, and Rhode Island.\n\nMany of these recommendations are being driven by recent studies regarding patient outcomes and nursing education. Hospitals employing higher percentages of BSN-prepared nurses have shown an associated decrease in morbidity, mortality, and failure-to-rescue rates. Increasing the percentage of BSN nurses employed decreases by 10 percent the 30-day inpatient mortality and failure-to-rescue rates. Studies that provide this type of evidence-based practice encompass the ultimate purpose of a higher level of educated nurse workforce. It adds to support the ultimate mission of the Texas Board of Nursing (BON or Board), which is to protect and promote the welfare of the people of Texas by ensuring that each person holding a license as a nurse in this state is competent to practice safely.\n\nMany healthcare leaders and institutions have increased expectations for evidence-based practice (EBP). The Institute of Medicine (IOM) aim was for 90% of clinical decisions to be evidence-based by 2020 (IOM, 2010).\n\nIn China\n\nIn China, the Bachelor of Science in Nursing (BSN) is a four-year undergraduate degree offered at public medical universities and select general universities. The curriculum combines classroom instruction in nursing theory, anatomy, physiology, and pharmacology with clinical rotations at affiliated teaching hospitals. Upon completion, graduates must pass the National Nursing Licensure Examination administered by the National Medical Examination Center to become a registered nurse.\n\nSee also"
 },
 {
  "title": "Body area network",
  "revision_id": "1378653895",
  "matched_by": "redirect-minus-qualifier",
  "text": "A body area network (BAN), also referred to as a wireless body area network (WBAN), a body sensor network (BSN) or a medical body area network (MBAN), is a wireless network of wearable computing devices. BAN devices may be embedded inside the body as implants or pills, may be surface-mounted on the body in a fixed position, or may be accompanied devices which humans can carry in different positions, such as in clothes pockets, by hand, or in various bags.\n\nDevices are becoming smaller, especially in body area networks. These networks include multiple small body sensor units (BSUs) and a single central unit (BCU). Despite this trend, decimeter (tab and pad) sized smart devices still play an important role. They act as data hubs or gateways and provide a user interface for viewing and managing BAN applications on the spot.\n\nThe development of WBAN technology started around 1995 around the idea of using wireless personal area network (WPAN) technologies to implement communications on, near, and around the human body. About six years later, the term \"BAN\" came to refer to systems where communication is entirely within, on, and in the immediate proximity of a human body. A WBAN system can use WPAN wireless technologies as gateways to reach longer ranges. Through gateway devices, it is possible to connect the wearable devices on the human body to the internet. This way, medical professionals can access patient data online using the internet independent of the patient location.\n\nConcept\n\nThe rapid growth in physiological sensors, low-power integrated circuits, and wireless communication has enabled a new generation of wireless sensor networks, now used for purposes such as monitoring traffic, crops, infrastructure, and health. The body area network field is an interdisciplinary area which could allow inexpensive and continuous health monitoring with real-time updates of medical records through the Internet. A number of intelligent physiological sensors can be integrated into a wearable wireless body area network, which can be used for computer-assisted rehabilitation or early detection of medical conditions. This area relies on the feasibility of implanting very small biosensors inside the human body that are comfortable and that don't impair normal activities. The implanted sensors in the human body will collect various physiological changes in order to monitor the patient's health status no matter their location. The information will be transmitted wirelessly to an external processing unit. This device will instantly transmit all information in real time to the doctors throughout the world. If an emergency is detected, the physicians will immediately inform the patient through the computer system by sending appropriate messages or alarms. Currently, the level of information provided and energy resources capable of powering the sensors are limiting. While the technology is still in its primitive stage it is being widely researched and once adopted, is expected to be a breakthrough invention in healthcare, leading to concepts like telemedicine and MHealth becoming real.\n\nApplications\n\nInitial applications of BANs are expected to appear primarily in the healthcare domain, especially for continuous monitoring and logging vital parameters of patients with chronic diseases such as diabetes, asthma and heart attacks.\n\nA BAN in place on a patient can alert the hospital, even before they have a heart attack, through measuring changes in their vital signs.\n\nA BAN on a patient with diabetes could auto inject insulin through a pump, as soon as their blood-sugar levels increase.\n\nA BAN can be used, to learn the underlying health state transitions and dynamics of a disease\n\nOther applications of this technology include sports, military, or security. Extending the technology to new areas could also assist communication by seamless exchanges of information between individuals, or between individuals and machines.\n\nStandards\n\nThe latest international standard for BANs is the IEEE 802.15.6 standard.\n\nComponents\n\nA typical BAN or BSN requires vital sign monitoring sensors, motion detectors (through accelerometers) to help identify the location of the monitored individual and some form of communication, to transmit vital sign and motion readings to medical practitioners or care givers. A typical body area network kit will consist of sensors, a Processor, a transceiver and a battery. Physiological sensors, such as ECG and SpO2 sensors, have been developed. Other sensors such as a blood pressure sensor, EEG sensor and a PDA for BSN interface are under development.\n\nWireless communication in the U.S.\n\nThe FCC has approved the allocation of 40 MHz of spectrum bandwidth for medical BAN low-power, wide-area radio links at the 2360–2400 MHz band. This will allow off-loading MBAN communication from the already saturated standard Wi-Fi spectrum to a standard band.\n\nThe 2360–2390 MHz frequency range is available on a secondary basis. The FCC will expand the existing Medical Device Radiocommunication (MedRadio) Service in Part 95 of its rules. MBAN devices using the band will operate under a 'license-by-rule' basis which eliminates the need to apply for individual transmitter licenses. Usage of the 2360–2390 MHz frequencies are restricted to indoor operation at health-care facilities and are subject to registration and site approval by coordinators to protect aeronautical telemetry primary usage. Operation in the 2390–2400 MHz band is not subject to registration or coordination and may be used in all areas including residential.\n\nChallenges\n\nProblems with the use of this technology could include:\n\nData quality: Data generated and collected through BANs can play a key role in the patient care process. It is essential that the quality of this data is of a high standard to ensure that the decisions made are based on the best information possible\n\nData management: As BANs generate large volumes of data, the need to manage and maintain these datasets is of utmost importance.\n\nSensor validation: Pervasive sensing devices are subject to inherent communication and hardware constraints including unreliable wired/wireless network links, interference and limited power reserves. This may result in erroneous datasets being transmitted back to the end user. It is of the utmost importance especially within a healthcare domain that all sensor readings are validated. This helps to reduce false alarm generation and to identify possible weaknesses within the hardware and software design.\n\nData consistency: Data residing on multiple mobile devices and wireless patient notes need to be collected and analysed in a seamless fashion. Within body area networks, vital patient datasets may be fragmented over a number of nodes and across a number of networked PCs or Laptops. If a medical practitioner's mobile device does not contain all known information then the quality of patient care may degrade.\n\nSecurity: Considerable effort would be required to make WBAN transmission secure and accurate. It would have to be made sure that the patient secure data is only derived from each patient's dedicated WBAN system and is not mixed up with other patient's data. Further, the data generated from WBAN should have secure and limited access. Although security is a high priority in most networks, little study has been done in this area for WBANs. As WBANs are resource-constrained in terms of power, memory, communication rate and computational capability, security solutions proposed for other networks may not be applicable to WBANs. Confidentiality, authentication, integrity, and freshness of data together with availability and secure management are the security requirements in WBAN. The IEEE 802.15.6 standard, which is latest standard for WBAN, tried to provide security in WBAN. However, it has several security problems. Researchers have studied using physiological signal-based security for BANs.\n\nInteroperability: WBAN systems would have to ensure seamless data transfer across standards such as Bluetooth, Zigbee etc. to promote information exchange, plug and play device interaction. Further, the systems would have to be scalable, ensure efficient migration across networks and offer uninterrupted connectivity.\n\nSystem devices: The sensors used in WBAN would have to be low on complexity, small in form factor, light in weight, power efficient, easy to use and reconfigurable. Further, the storage devices need to facilitate remote storage and viewing of patient data as well as access to external processing and analysis tools via the Internet.\n\nEnergy vs. accuracy: Sensors' activation policy should be determined to optimizing the trade-off between the BAN's power consumption versus the probability of patient's health state mis-classification. High power consumption often results in more accurate observations on the patient's health state and vice versa.\n\nPrivacy: People might consider the WBAN technology as a potential threat to freedom if the applications go beyond \"secure\" medical usage. Social acceptance would be key to this technology finding a wider application.\n\nInterference: The wireless link used for body sensors should reduce the interference and increase the coexistence of sensor node devices with other network devices available in the environment. This is especially important for large scale implementation of WBAN systems.\n\nCost: Today's consumers expect low cost health monitoring solutions which provide high functionality. WBAN implementations will need to be cost optimized to be appealing alternatives to health conscious consumers.\n\nConstant monitoring: Users may require different levels of monitoring, for example those at risk of cardiac ischemia may want their WBANs to function constantly, while others at risk of falls may only need WBANs to monitor them while they are walking or moving. The level of monitoring influences the amount of energy required and the life cycle of the BAN before the energy source is depleted.\n\nConstrained deployment: The WBAN needs to be wearable, lightweight and non intrusive. It should not alter or encumber the user's daily activities. The technology should ultimately be transparent to the user i.e., it should perform its monitoring tasks without the user realising it.\n\nConsistent performance: The performance of the WBAN should be consistent. Sensor measurements should be accurate and calibrated, even when the WBAN is switched off and switched on again. The wireless links should be robust and work under various user environments.\n\nSee also"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q4838827",
  "label": "Bachelor of Science in Nursing",
  "description": "undergraduate degree in nursing",
  "aliases": [
   "BSN",
   "BScN",
   "Bachelor of Science with a Major in Nursing",
   "B.S.N."
  ],
  "claims": {
   "P279": [
    "Q787674"
   ]
  },
  "revision_id": "2381091284",
  "value_labels": {
   "Q787674": "Bachelor of Science"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q890056",
  "label": "body area network",
  "description": "wireless network of wearable computing devices, either implants, surface-mounted on the body, or accompanied devices carried in pockets, in hand, or in bags",
  "aliases": [
   "BAN",
   "Intra-body Communication",
   "wireless body area network",
   "WBAN",
   "body sensor network",
   "BSN",
   "medical body area network",
   "MBAN"
  ],
  "claims": {
   "P279": [
    "Q1301371"
   ]
  },
  "revision_id": "2514072258",
  "value_labels": {
   "Q1301371": "computer network"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q18033540",
  "label": "BSN",
  "description": "protein-coding gene in the species Homo sapiens",
  "aliases": [
   "ZNF231",
   "bassoon presynaptic cytomatrix protein"
  ],
  "claims": {
   "P31": [
    "Q7187"
   ],
   "P279": [
    "Q20747295"
   ]
  },
  "revision_id": "2571727263",
  "value_labels": {
   "Q7187": "gene",
   "Q20747295": "protein-coding gene"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q787674",
  "label": "Bachelor of Science",
  "description": "type of bachelor's degree",
  "aliases": [
   "Bc.",
   "BS",
   "B Sc",
   "S.B",
   "SB",
   "Sc.B.",
   "Scientiæ Baccalaureus",
   "S.B.",
   "Bachelor's of Science",
   "Bachelor of Science degree",
   "Bachelors of Science",
   "S.I.P.",
   "BSc."
  ],
  "claims": {
   "P31": [
    "Q1622058"
   ],
   "P279": [
    "Q163727"
   ]
  },
  "revision_id": "2568400407",
  "ancestor_of": "Q4838827",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1622058",
  "label": "academic degree",
  "description": "general term for a degree at an higher educational organization not necessarily with an exam",
  "aliases": [],
  "claims": {
   "P279": [
    "Q3529618",
    "Q3412758"
   ],
   "P1889": [
    "Q849697",
    "Q189533"
   ]
  },
  "revision_id": "2543209621",
  "ancestor_of": "Q4838827",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q163727",
  "label": "bachelor's degree",
  "description": "undergraduate academic degree lasting from three to seven years",
  "aliases": [
   "bachelor degree",
   "baccalaureate degree",
   "bachelors degree",
   "BA degree",
   "bachelor",
   "bacc. art."
  ],
  "claims": {
   "P31": [
    "Q4218455",
    "Q18189",
    "Q11659512",
    "Q189533"
   ],
   "P279": [
    "Q3529618",
    "Q4218455",
    "Q16628973"
   ],
   "P527": [
    "Q1765120",
    "Q787674",
    "Q2878189",
    "Q13948235",
    "Q798137",
    "Q4838815",
    "Q798129",
    "Q2878277",
    "Q4838780"
   ],
   "P460": [
    "Q1054679",
    "Q3238020",
    "Q749020"
   ],
   "P1889": [
    "Q1901305",
    "Q749020"
   ]
  },
  "revision_id": "2569863817",
  "ancestor_of": "Q4838827",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1301371",
  "label": "computer network",
  "description": "network that allows computers to share resources and communicate with each other",
  "aliases": [
   "computer network technologies and services",
   "network",
   "computer networks",
   "computer communication networks"
  ],
  "claims": {
   "P279": [
    "Q1068715"
   ],
   "P527": [
    "Q5747224"
   ],
   "P460": [
    "Q12828494"
   ],
   "P1889": [
    "Q3962217"
   ]
  },
  "revision_id": "2550653445",
  "ancestor_of": "Q890056",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1068715",
  "label": "telecommunications network",
  "description": "network for communications over distance",
  "aliases": [],
  "claims": {
   "P279": [
    "Q13425103",
    "Q9350592"
   ],
   "P527": [
    "Q798444"
   ]
  },
  "revision_id": "2543056036",
  "ancestor_of": "Q890056",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7187",
  "label": "gene",
  "description": "basic physical and functional unit of heredity",
  "aliases": [
   "genes"
  ],
  "claims": {
   "P31": [
    "Q111972893"
   ],
   "P279": [
    "Q863908",
    "Q50365914",
    "Q3771876"
   ],
   "P361": [
    "Q37748",
    "Q7020",
    "Q1501261"
   ],
   "P1889": [
    "Q1449",
    "Q7020"
   ]
  },
  "revision_id": "2568084548",
  "ancestor_of": "Q18033540",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q20747295",
  "label": "protein-coding gene",
  "description": "type of a gene",
  "aliases": [
   "protein coding gene"
  ],
  "claims": {
   "P31": [
    "Q131679239"
   ],
   "P279": [
    "Q7187"
   ]
  },
  "revision_id": "2566835221",
  "ancestor_of": "Q18033540",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q111972893",
  "label": "type of structure",
  "description": "Wikidata metaclass of arrangement and organization of interrelated elements in an object or system",
  "aliases": [
   "structure type"
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
  "revision_id": "2561704900",
  "ancestor_of": "Q18033540",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q863908",
  "label": "nucleic acid sequence",
  "description": "succession of letters that indicate the order of nucleotides within a DNA (using GACT) or RNA (GACU) molecule",
  "aliases": [
   "base sequence",
   "nucleotide sequence",
   "Nucleic acid sequence",
   "nucleic acid primary structure"
  ],
  "claims": {
   "P279": [
    "Q37500013",
    "Q3771876",
    "Q141543245"
   ]
  },
  "revision_id": "2556398578",
  "ancestor_of": "Q18033540",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q50365914",
  "label": "biological region",
  "description": "sequence region defined by its disposition to be involved in a biological process",
  "aliases": [],
  "claims": {
   "P279": [
    "Q219858"
   ]
  },
  "revision_id": "2184498222",
  "ancestor_of": "Q18033540",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3771876",
  "label": "nucleic acid structure",
  "description": "organization of DNA and RNA molecules at different scales",
  "aliases": [
   "nucleic acid part"
  ],
  "claims": {
   "P279": [
    "Q15712714"
   ],
   "P1889": [
    "Q863908"
   ]
  },
  "revision_id": "2549811286",
  "ancestor_of": "Q18033540",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q131679239",
  "label": "type of gene",
  "description": "metaclass for genes with different structural or functional characteristics",
  "aliases": [
   "gene type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ],
   "P1889": [
    "Q106016",
    "Q5532959"
   ]
  },
  "revision_id": "2552517149",
  "ancestor_of": "Q18033540",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 5 of 6: Class B commercial driver's license (`zkn14vnicf`)

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

## Concept 6 of 6: CCNA Security (`tp5pvtb8jm`)

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
[
 {
  "title": "Cisco certifications",
  "revision_id": "1377607952",
  "matched_by": "redirect",
  "text": "Cisco certifications are the list of the certifications offered by Cisco. There are four to five (path to network designers) levels of certification: Associate (CCNA/CCDA), Professional (CCNP/CCDP), Expert (CCIE/CCDE), and recently, Architect (CCAr: CCDE previous), as well as nine different paths for the specific technical field; Routing & Switching, Design, Industrial Network, Network Security, Service Provider, Service Provider Operations, Storage Networking, Voice, Datacenter, and Wireless. There are also a number of specialist technicians, sales, business, data center certifications, and CCAI certified instructors (Cisco Academy Instructor).\n\nPaths to Certification\n\nThe table below shows the different paths and levels for Cisco Certifications. All Certifications, except for CCAr, requires the passing of one or more theoretical exams offered by Pearson VUE. CCIE Certifications also require a hands-on exam administered at special labs around the world.\n\nAs of October 1, 2023, Cisco has altered their certification structure. \n\n2 entry level certificates: CCST\n\n3 associate level certificates: CCNA, Cisco Certified DevNet Associate, and Cisco Certified CyberOps Associate.\n\n7 professional level certificates : Cisco Certified DevNet Professional, CCNP Enterprise, CCNP Collaboration, CCNP Data Center, CCNP Security, CCNP Service Provider, and Cisco Certified CyberOps Professional\n\n8 expert level certificates : CCIE Collaboration, CCIE Data Center, DevNet Expert, CCDE, CCIE Enterprise Infrastructure, CCIE Enterprise Wireless, CCIE Security, CCIE Service Provider\n\nAs of February 24, 2020, Cisco altered their certification structure.\n\n1 entry level certificate: CCT\n\n3 associate level certificates: CCNA, CC DevNet Associate, and CC CyberOps Associate.\n\n7 professional level certificates : CCNP DevNet, CCNP Enterprise, CCNP Collaboration, CCNP Data Center, CCNP Security, CCNP Service Provider, and CC CyberOps Professional\n\n7 expert level certificates : CCDE, CCIE Infrastructure, CCIE Enterprise Wireless, CCIE Collaboration, CCIE Data Center, CCIE Security, and CCIE Service provider.\n\nPrimary Certifications\n\nCisco Certified Entry Networking Technician (CCENT)\n\nCisco Certified Entry Networking Technician {CCENT} represents the lowest level of certification which covers basic networking knowledge. Until its introduction, CCNA represented the first level of the certification program. It has appropriate use for an entry-level network support position. CCENT certified staff can install, manage and troubleshoot a small enterprise network, including basic network security. The first step towards a CCNA certification must start by having a CCENT. \nIn 2017, Cisco introduced new ICND1 and ICND2 exams (needed for the new CCNA Routing and Switching). ICND1: 100-105 (Interconnecting Cisco Networking Devices Part 1 v3.0) became the new exam required for CCENT. With this change, CCENT became a sufficient pre-requirement for CCNA Security, CCNA Voice and CCNA Wireless.\n\nIt is valid for 3 years.\n\nCisco Certified Technicians (CCT)\n\nAs of September 2024, there were 3 domains available for CCT certification:\n\nCCT Collaboration - valid for 3 years.\n\nCCT Routing and Switching - valid for 3 years.\n\nCCT Data Center - valid for 3 years.\n\nAssociate Certifications\nCCNA Routing and Switching\n\nThe CCNA Routing and Switching certification covered skills necessary to administer devices on small or medium-sized networks. This certification required the ICND1 100-105 and ICND2 200-105 exams.\n\nPearson VUE test centers conduct these exams.\n\nAll CCNA-certified individuals specialize by technology. Previously, specialized tracks required passing and maintaining a CCNA certification, but with the expiration of the 640 series tests this is no longer the case. As of autumn 2015, the CCNA Certification has no prerequisites.\n\nStarting 24 February 2020, all CCNA specializations were consolidated. The 200-301 Cisco Certified Network Associate exam is now the only exam available at CCNA-level.\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nCCDA\n\nCisco-Certified Design Associate (CCDA) certified engineers can design switched or routed networks of LANs, WANs and broadband services. The CCDA exam (200-310 DESGN) requires a CCENT at a minimum, though either CCNA or CCIE will serve as a prerequisite, as well SWITCH-level knowledge of Cisco-based LANs.\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nCCNA Cloud\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nCCNA Collaboration\n\nThe Cisco Certified Collaboration Associate certification is for Cisco engineers who specialize in Cisco's Unified Communications (UC) products. Collaboration engineers focus on the deployment and support of voice, video, and live text communication solutions across IP networks.\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nCCNA CyberOps\n\nThe CCNA Cyber Ops certification prepares candidates to begin a career working with associate-level cybersecurity analysts within security operations centers.\n\nValid for 3 years.\n\nRetired on May 28, 2020 \n\nCCNA Industrial\n\nThe Cisco Certified Network Associate Industrial (CCNA Industrial) certification was valid for 3 years.\n\nRetired on February 23, 2020 \n\nCCNA Security\n\nCCNA Security validates knowledge of security infrastructure, threats, and vulnerabilities to networks and threat mitigation. Required skills include installation, troubleshooting and monitoring of network devices to maintain the integrity, confidentiality, and availability of data and devices. To earn this certification one must pass the 210-260 IINS (Implementing Cisco IOS Network Security) exam, as well as hold a current CCNA certification. The CCNA-Security is a prerequisite to the CCNP Security certification. It represents the required exam to earn the certification and for continuing the security certification path to the CCNP.\n\nNote: The CCNA Security courseware holds compliance with the NSA and CNSS training standard of CNSS 4011. By remaining compliant, the CCNA Security program provides the required training for network security professionals who assist private sector entities and federal agencies of the United States, protects their information and aid in the defense of the United States IT infrastructure. Candidates who have passed the CCNA Security will receive a letter of recognition acknowledging they have met the CNSS 4011 training requirements.\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nCCNA Service Provider\n\nPart 1 is a 5-day instructor-led course that provides the basic knowledge and skills necessary to support a service provider network. The course provides knowledge of the major network components and helps learners to understand how service provider networks function. The course introduces IP Next-Generation Network (IP NGN) architecture. The course also includes remote labs that help gain practical skills for deploying basic Cisco IOS / IOS XE and Cisco IOS XR software features. Part 2 is a 5-day instructor-led course that provides knowledge of network construction and IP NGN architecture. The course includes additional remote labs.\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nCCNA Wireless\n\nThe CCNA Wireless certification covers wireless LANs, including networking associates/administrators, wireless support specialists, and WLAN project managers. The certification validates skills in the configuration, implementation, and support of wireless LANs. 200-355 WIFUND (Implementing Cisco Wireless Networking Essentials) is the required exam.\n\nValid for 3 years.\n\nRetired on February 23, 2020 \n\nProfessional Certifications\n\nCisco Certified Network Professional (CCNP) Certifications validate knowledge and skills required to install, configure, and troubleshoot converged local- and wide-area networks with 100 to 500 or more end-devices. One needs a valid CCNA certification to obtain a CCNP certification.\n\nCCNP Routing and Switching\n\nThe CCNP validates the ability to plan, implement, verify, and troubleshoot local and wide-area enterprise networks and work collaboratively with specialists on advanced security, voice, wireless, and video solutions. In addition to CCNA Exams, professionals must pass three separate professional-level exams. The certification track changed in July 2010, with various migration paths available for those that had begun, but not completed, the CCNP certification process. In July 2014, Cisco released version 2.0 of the CCNP exams and training courses, \"to reflect the alignment with changing industry job roles and the addition of new study materials.\" 29 January 2015 was the last day to test using the v1.0 exams. As of 30 January 2015, only the v2.0 exam is offered.\n\nRequired exams (v1.0):\n\n642-902 ROUTE: Implementing Cisco IP Routing (ROUTE)\n\n642-813 SWITCH: Implementing Cisco IP Switched Networks (SWITCH)\n\n642-832 TSHOOT: Troubleshooting and Maintaining Cisco IP Networks (TSHOOT)\n\nRequired exams (v2.0):\n\n300-101 ROUTE: Implementing Cisco IP Routing (ROUTE)\n\n300-115 SWITCH: Implementing Cisco IP Switched Networks (SWITCH)\n\n300-135 TSHOOT: Troubleshooting and Maintaining Cisco IP Networks (TSHOOT)\n\nRetired on February 23, 2020 \nCheck CCNP Enterprise Architecture.\n\nCCDP\n\nWith a CCDP certification, a network professional can discuss, design, and create advanced addressing and routing, security, network management, data center, and IP multicast enterprise architectures that include virtual private networking and wireless domains. An active CCDA certification acts as a prerequisite for this certification.\n\nRequired exams:\n\n300-101 ROUTE: Implementing Cisco IP Routing (ROUTE)\n\n300-115 SWITCH: Implementing Cisco IP Switched Networks (SWITCH)\n\n300-320 ARCH: Designing Cisco Network Service Architecture\n\nNote that CCDP requires 300-101 ROUTE and 300-115 SWITCH. After passing CCNP and CCDA, CCDP requires only 300-320 ARCH.\n\nRetired on February 23, 2020 \n\nCCNP Collaboration\n\nYou are required to pass these four exams:\n300-070 CIPTV1 Implementing Cisco IP Telephony and Video, Part 1 (CIPTV1)\n300-075 CIPTV2 Implementing Cisco IP Telephony and Video, Part 2 (CIPTV2)\n300-080 CTCOLLAB Troubleshooting Cisco IP Telephony and Video (CTCOLLAB)\n300-085 CAPPS Implementing Cisco Collaboration Applications (CAPPS)\n\nCCNP Data Center\n\nCCNP Data Center validates knowledge of data center design, equipment installation, and maintenance.\n\nFive required exams:\n\n300-175 DCUCI Implementing Cisco Data Center Unified Computing (DCUCI)\n\n300-165 DCII Implementing Cisco Data Center Infrastructure (DCII)\n\n300-170 DCVAI Implementing Cisco Data Center Virtualization and Automation (DCVAI)\n\n300-160 DCID Designing Cisco Data Center Infrastructure (DCID)\n\nOR\n\n300-180 DCIT Troubleshooting Cisco Data Center Infrastructure (DCIT)\nCCNP Security\n\nFormerly Cisco Certified Security Professional (CCSP).\n\nThe CCNP Security certification program aligns to the job role of the Cisco Network Security Engineer, who has responsibility for security in routers, switches, networking devices, and appliances, as well as choosing, deploying, supporting, and troubleshooting firewalls, VPNS, and IDS/IPS solutions for their networking environments. The CCNP Security certification no longer requires CCNA Security or any other Certification. The CCNP has no prerequisites, but Cisco recommends three to five years of experience.\n\nCCNP Service Provider\n\nThe CCNP Service Provider certification replaced the retiring CCIP certification.\n\nRequired exams:\n\n642-883 SPROUTE: Deploying Cisco Service Provider Network Routing\n\n642-885 SPADVROUTE: Deploying Cisco Service Provider Advanced Routing\n\n642-887 SPCORE: Implementing Cisco Service Provider Next-Generation Core Network Services\n\n642-889 SPEDGE: Implementing Cisco Service Provider Next-Generation Edge Network Services\nCCNP Wireless\n\nCCNP Wireless covers all aspects of wireless networking principles and theory. This certification requires four tests, covering Wireless Site Survey, Wireless Voice Networks, Wireless Mobility Services, and Wireless Security. The prerequisite acts as a valid CCNA Wireless certification.\n\nRequired exams:\n\n642-732 CUWSS: Conducting Cisco Unified Wireless Site Survey (CUWSS)\n\n642-742 IUWVN: Implementing Cisco Unified Wireless Voice Networks (IUWVN)\n\n642-747 IUWMS: Implementing Cisco Unified Wireless Mobility Services (IUWMS)\n\n642-737 IAUWS: Implementing Advanced Cisco Unified Wireless Security (IAUWS)\n\nRetired on February 23, 2020 \n\nExpert-level Certifications\n\nCisco Certified Internetwork Expert represents Cisco's highest certification, comprising seven tracks at present, tracks are updated and retired frequently and are aligned to the latest industry technologies and trends. As of October 6, 2010, 25,810 people held active CCIE Certifications. CertMag, voted it as the most technically advanced IT certification and statistics generally report it as the highest salaried certification in IT salary surveys.\n\nCCIE began in 1993, originally with a two-day lab, later changing to a one-day format. Fewer than 3% of Cisco-certified individuals attain CCIE certification and, on average, spend thousands of dollars and 18 months studying before passing. Many candidates build training labs at home using old equipment, then sell it to other candidates after passing. Alternatively, candidates may rent \"rack time\" online. The CCIE consists of a written exam and a \"lab\" exam (in each track). The written exam acts as a prerequisite of the lab exam and has a cost of $400 per attempt. The written exam consists of 100 questions that must be completed within 2 hours. Upon passing the written exam, the candidate has eighteen months to take the lab exam. The candidate has three years after passing the written exam to successfully complete the lab. The lab is an eight-hour, hands-on exam designed to demonstrate that the candidate knows Internetworking theory and demonstrates advanced hands-on mastery. Candidates that do not pass the CCIE lab in that interval must re-pass the written exam before again attempting the CCIE lab exam. The minimum waiting time between attempts is one month.\n\nAs of July 2014, the CCIE Lab costs $1600 per attempt and ten Cisco locations offer it worldwide. Some of these locations do not offer all CCIE tracks. According to a Cisco survey, $9050 represents the average cost to prepare for CCIE certification as of April 2006, which gets spent mostly on practice equipment and study material. No formal prerequisites currently exist for the CCIE written exam, but Cisco recommends at least 3–5 years networking experience. CCIE exists as the first Cisco Certified qualification and no other Certifications have existed previously. The associate and professional Certifications recognized the fact that CCIE is overkill for many networking personnel. Cisco has chosen not to make lower level Certifications prerequisites for the CCIE certification.\n\nOne may have the knowledge to hold multiple CCIE Certifications. Adam McCombs cited this qualification as \"essentially a PhD in the internet\" in Season 1 Episode 10 of Shark Tank.\n\nUpon successful completion of the lab exam, Cisco awards a CCIE number to a new CCIE. The first CCIE number allocated (in 1993) started at 1,024 and increased thereafter. As of August 2011, the highest CCIE number allocated reached just over 30,000. The first number they allocated to the first CCIE lab location, rather than to an individual, and featured as a plaque at the entrance to the lab. They awarded Number 1025 to Stuart Biggs, who created the first written exam and first lab exam. The first person to pass both CCIE written and lab exams, known as Terry Slattery, consulted at Cisco when the lab began development. Slattery held the first CCIE who did not work for Cisco. Each CCIE retains their number regardless of how many Certifications he or she receives. Every two years a CCIE has to take a written test to retain the certification. If not done, the certification becomes suspended. After one further year without passing, the certification becomes revoked. One can then only regain the certification by starting from scratch. Re-certification can occur up to 2 years before the expiration date. After certification/re-certification, a CCIE must wait 6 months before re-certifying.\n\nCCIE Lab Exams are administered only at special CCIE Lab Test Centers around the world. However, all the tracks for testing may not be available at a lab location.\n\nCCAr\n\nThe Cisco Certified Architect (CCAr) certification program trains students to meet the responsibilities of the Cisco Certified Architect:\n\nLead creation and evolution of enterprise architecture\n\nAnalyze technology and industry market trends\n\nEstablish governing principles for Enterprise networks\n\nSelection of technology and products\n\nIdentification of organization resource needs\n\nLead the development of communication and education plan for enterprise network architecture\nCCIE Routing and Switching\n\nRouting and Switching seem by far the most popular track, with 35,272 worldwide certified individuals as of May 18, 2012. The certification covers a variety of networking concepts and protocols.\n\nRetired. Check CCIE Enterprise Infrastructure \n.\n\nCCDE\n\nCCDE runs in parallel with the more established CCIE program, in some areas providing a higher skill-set than CCIE. Specifically, CCDE identifies network professionals who have expert network design skills. Network design translates business requirements into end-to-end network designs and a solutions approach to network expansion and integration. CCDE focuses on network architecture and does not cover implementation and operations. CCDE supplies a vendor-neutral curriculum, testing business requirements analysis, design, planning, and validation practices. The course came about because employers needed a way to identify experienced network designers and architects who could address all aspects of existing and new networking technologies and trends. While engineers (including many CCIEs) had fulfilled this role, certification had not advanced beyond the CCDP certification. CCDE numbering adopts a different format than CCIE and appears split into a year and number within that year. It uses the same CCIE tools to verify qualified status. CCDE certified individuals can use CCIE qualification exams to re-certify and vice versa. CCDE provides advanced network infrastructure design principles and fundamentals for large networks. A CCDE can demonstrate an ability to develop solutions which address planning, design, integration, optimization, operations, security, and ongoing support focused at the infrastructure level.\n\nCCIE Collaboration\n\nThe Voice track covers advanced topics in subjects such as Quality of Service, MGCP, Cisco Call Manager (Cisco's VoIP PBX), Cisco Unity Connection (Cisco's Voice Messaging platform), Unity Express, Unified Contact Center Express, Cisco Unified Presence Server, Cisco's HWIC-4ESW, and the 3750-24PS. Most candidates pass after three or four lab attempts, but some have required more than six. Many have reputed that the lab exam seems as much a test of time management and planning as of technical expertise. The widely dissimilar platforms used sets the Voice lab exam apart from other CCIE lab exams. One must make configurations on the Windows Server environment, a CallManager web-based GUI, and the IOS command line. As such, it involves a lot of back-and-forth fine tuning between the numerous platforms.\n\nIn May 2013, Cisco announced it will retire the CCIE Voice track and introduce the new CCIE Collaboration track, including new topics such as virtualization, Jabber instant messaging and video. After protest from current and aspirant CCIE Voice holders, whom argued that the differences remain too few to warrant retiring the track with no option to transition to the new track, Cisco offered a transition path for existing Voice holders. The Collaboration written exam may have availability starting from November 21, 2013. The lab exam will transition from Voice to Collaboration on February 14, 2014.\n\nCCIE Data Center\n\nCisco has announced the September availability of a CCIE Data Center certification, which certifies the expert-level skills required to plan, prepare, operate, monitor, and troubleshoot complex data center networks. The CCIE Data Center written exam will be available Sept. 3, 2012; the lab exam should have availability in October.\n\nCCIE Security\n\nThe Security track covers advanced topics in subjects such as ASA, FirePower, IOS security, Wireless Security, Content Security, Antimalware Protection and many others.\n\nCCIE Service Provider\n\nThe Cisco CCIE Service Provider (CCIE SP) certification validates expert level skills, required of a Network Engineer to configure, build, troubleshoot, and optimize a complex Service Provider IP NGN core infrastructure. Candidates, preparing for CCIE SP certification, possess thorough knowledge in IP core, aggregation/edge, and remote access technologies, Layer 2 and 3 VPNs, plus managed services traversing an IP core network.\n\nCCIE Wireless\n\nCCIE Wireless certification exams assess candidates on theoretical knowledge of wireless networking and an understanding of wireless local area networking (WLAN) technologies from Cisco.\n\nRetired. Check CCIE Enterprise Wireless\n\nSpecialist Certification\n\nIn addition to the vast amount of Certifications above, Cisco also provides Meraki Specialist Certifications. \nThe exams for these Certifications are often focused on some specific technology and generally targeted at members of the Cisco Partner Program, including those selling, designing, or supporting Cisco products and services. By combining various exams, a Cisco partner can gain specialty status and thus qualify for additional partner benefits.\n\nSpecializations can be held at Express, Advanced and Master levels, reflecting the depth of a partners skills across certain"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q17992617",
  "label": "Cisco certifications",
  "description": "certifications offered by Cisco Systems",
  "aliases": [
   "Cisco Career Certifications"
  ],
  "claims": {
   "P31": [
    "Q21484471"
   ]
  },
  "revision_id": "2327726938",
  "value_labels": {
   "Q21484471": "Wikimedia article covering multiple topics"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q21484471",
  "label": "Wikimedia article covering multiple topics",
  "description": "article in Wikimedia which mixes multiple separate topics. Use P921 (\"main subject\"), NOT P527 (\"has part(s)\"), to list topics covered by the article",
  "aliases": [
   "Wikimedia compound page",
   "Wikimedia pages covering multiple topics",
   "Wikimedia pages conflating two topics",
   "Wikimedia pages conflating multiple topics",
   "Wikimedia page covering multiple topics",
   "Wikimedia articles on two separate topics",
   "Wikimedia articles covering multiple topics",
   "Wikimedia article describing multiple topics",
   "Wikimedia article that covers multiple topics",
   "Wikipedia article covering multiple topics",
   "Wikimedia page covering multiple items"
  ],
  "claims": {
   "P279": [
    "Q15138389"
   ],
   "P460": [
    "Q122754124"
   ],
   "P1889": [
    "Q4167410",
    "Q20136634",
    "Q134972145"
   ]
  },
  "revision_id": "2564572328",
  "ancestor_of": "Q17992617",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q15138389",
  "label": "Wikimedia article page",
  "description": "article in the main space of a Wikimedia site (note: various wikis, do NOT use this together with \"instance of\")",
  "aliases": [
   "Wikimedia article"
  ],
  "claims": {
   "P279": [
    "Q15633587",
    "Q191067"
   ],
   "P1889": [
    "Q50081413"
   ]
  },
  "revision_id": "2549822805",
  "ancestor_of": "Q17992617",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[]

Draft the entry for this concept. Return the JSON object only.
~~~~
