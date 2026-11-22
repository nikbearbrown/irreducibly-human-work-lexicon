# Skills Lexicon pilot, grounded run: message 11 of 13 (chunk 10, 3 concepts)

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
`"_meta": {"model": "<your model and version>", "run": "grounded", "chunk": "10", "attempts": 1}`.
If you can make files, send a file named `drafts-grounded-10.jsonl`. Otherwise send one code block marked `jsonl` holding the 3 lines and nothing else. A script will check them afterwards.

---

## Concept 1 of 3: Deductive Reasoning (`wclhs8ljcp`)

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
[
 {
  "title": "Deductive reasoning",
  "revision_id": "1374177180",
  "matched_by": "title",
  "text": "Deductive reasoning is the process of drawing valid inferences. An inference is valid if its conclusion follows logically from its premises, meaning that it is impossible for the premises to be true and the conclusion to be false. For example, the inference from the premises \"all men are mortal\" and \"Socrates is a man\" to the conclusion \"Socrates is mortal\" is deductively valid. An argument is sound if it is valid and all its premises are true. One approach defines deduction in terms of the intentions of the author: they have to intend for the premises to offer deductive support to the conclusion. With the help of this modification, it is possible to distinguish valid from invalid deductive reasoning: it is invalid if the author's belief about the deductive support is false, but even invalid deductive reasoning is a form of deductive reasoning. \n\nDeductive logic studies under what conditions an argument is valid. According to the semantic approach, an argument is valid if there is no possible interpretation of the argument whereby its premises are true and its conclusion is false. The syntactic approach, by contrast, focuses on rules of inference, that is, schemas of drawing a conclusion from a set of premises based only on their logical form. There are various rules of inference, such as modus ponens and modus tollens. Invalid deductive arguments, which do not follow a rule of inference, are called formal fallacies. Rules of inference are definitory rules and contrast with strategic rules, which specify what inferences one needs to draw in order to arrive at an intended conclusion.\n\nDeductive reasoning contrasts with non-deductive or ampliative reasoning. For ampliative arguments, such as inductive or abductive arguments, the premises offer weaker support to their conclusion: they indicate that it is most likely, but they do not guarantee its truth. They make up for this drawback with their ability to provide genuinely new information (that is, information not already found in the premises), unlike deductive arguments.\n\nA branch of cognitive psychology, the psychology of reasoning, investigates the mental processes responsible for deductive reasoning. One of its topics concerns the factors determining whether people draw valid or invalid deductive inferences. One such factor is the form of the argument: for example, people draw valid inferences more successfully for arguments of the form modus ponens than of the form modus tollens. Another factor is the content of the arguments: people are more likely to believe that an argument is valid if the claim made in its conclusion is plausible. A general finding is that people tend to perform better for realistic and concrete cases than for abstract cases. Psychological theories of deductive reasoning aim to explain these findings by providing an account of the underlying psychological processes. Mental logic theories hold that deductive reasoning is a language-like process that happens through the manipulation of representations using rules of inference. Mental model theories, on the other hand, claim that deductive reasoning involves models of possible states of the world without the medium of language or rules of inference. According to dual-process theories of reasoning, there are two qualitatively different cognitive systems responsible for reasoning.\n\nThe problem of deduction is relevant to various fields and issues. Epistemology tries to understand how justification is transferred from the belief in the premises to the belief in the conclusion in the process of deductive reasoning. Probability logic studies how the probability of the premises of an inference affects the probability of its conclusion. The controversial thesis of deductivism denies that there are other correct forms of inference besides deduction. Natural deduction is a type of proof system based on simple and self-evident rules of inference. In philosophy, the geometrical method is a way of philosophizing that starts from a small set of self-evident axioms and tries to build a comprehensive logical system using deductive reasoning.\n\nDefinition\n\nDeductive reasoning is the psychological process of drawing deductive inferences. An inference is a set of premises together with a conclusion or the psychological process starts from the premises and reasons to a conclusion based on and supported by these premises. If deductive reasoning is done correctly, it results in a valid inference, in which the truth of the premises ensures the truth of the conclusion. For example, in the syllogistic argument \"all frogs are amphibians; no cats are amphibians; therefore, no cats are frogs\" the conclusion is true because its two premises are true. But even arguments with wrong premises can be deductively valid if they obey this principle, as in \"all frogs are mammals; no cats are mammals; therefore, no cats are frogs\". If the premises of a valid argument are true, then it is called a sound argument.\n\nThe relation between the premises and the conclusion of a deductive argument is usually referred to as \"logical consequence\". According to Alfred Tarski, logical consequence has 3 essential features: it is necessary, formal, and knowable a priori. It is necessary in the sense that the premises of valid deductive arguments necessitate the conclusion: it is impossible for the premises to be true and the conclusion to be false, independent of any other circumstances. Logical consequence is formal in the sense that it depends only on the form or the syntax of the premises and the conclusion. This means that the validity of a particular argument does not depend on the specific contents of this argument. If it is valid, then any argument with the same logical form is also valid, no matter how different it is on the level of its contents. Logical consequence is knowable a priori in the sense that no empirical knowledge of the world is necessary to determine whether a deduction is valid. So it is not necessary to engage in any form of empirical investigation. Some logicians define deduction in terms of possible worlds: A deductive inference is valid if and only if, there is no possible world in which its conclusion is false while its premises are true. This means that there are no counterexamples: the conclusion is true in all such cases, not just in most cases.\n\nIt has been argued against this and similar definitions that they fail to distinguish between valid and invalid deductive reasoning, i.e. they leave it open whether there are invalid deductive inferences and how to define them. Some authors define deductive reasoning in psychological terms in order to avoid this problem. According to Mark Vorobey, whether an argument is deductive depends on the psychological state of the person making the argument: \"An argument is deductive if, and only if, the author of the argument believes that the truth of the premises necessitates (guarantees) the truth of the conclusion\". A similar formulation holds that the speaker claims or intends that the premises offer deductive support for their conclusion. This is sometimes categorized as a speaker-determined definition of deduction since it depends also on the speaker whether the argument in question is deductive or not. For speakerless definitions, on the other hand, only the argument itself matters independent of the speaker. One advantage of this type of formulation is that it makes it possible to distinguish between good or valid and bad or invalid deductive arguments: the argument is good if the author's belief concerning the relation between the premises and the conclusion is true, otherwise it is bad. One consequence of this approach is that deductive arguments cannot be identified by the law of inference they use. For example, an argument of the form modus ponens may be non-deductive if the author's beliefs are sufficiently confused. That brings with it an important drawback of this definition: it is difficult to apply to concrete cases since the intentions of the author are usually not explicitly stated.\n\nDeductive reasoning is studied in logic, psychology, and the cognitive sciences. Some theorists emphasize in their definition the difference between these fields. On this view, psychology studies deductive reasoning as an empirical mental process, i.e. what happens when humans engage in reasoning. But the descriptive question of how actual reasoning happens is different from the normative question of how it should happen or what constitutes correct deductive reasoning, which is studied by logic. This is sometimes expressed by stating that, strictly speaking, logic does not study deductive reasoning but the deductive relation between premises and a conclusion known as logical consequence. But this distinction is not always precisely observed in the academic literature. One important aspect of this difference is that logic is not interested in whether the conclusion of an argument is sensible. So from the premise \"the printer has ink\" one may draw the unhelpful conclusion \"the printer has ink and the printer has ink and the printer has ink\", which has little relevance from a psychological point of view. Instead, actual reasoners usually try to remove redundant or irrelevant information and make the relevant information more explicit. The psychological study of deductive reasoning is also concerned with how good people are at drawing deductive inferences and with the factors determining their performance. Deductive inferences are found both in natural language and in formal logical systems, such as propositional logic.\n\nConceptions of deduction\n\nDeductive arguments differ from non-deductive arguments in that the truth of their premises ensures the truth of their conclusion. There are two important conceptions of what this exactly means. They are referred to as the syntactic and the semantic approach. According to the syntactic approach, whether an argument is deductively valid depends only on its form, syntax, or structure. Two arguments have the same form if they use the same logical vocabulary in the same arrangement, even if their contents differ. For example, the arguments \"if it rains then the street will be wet; it rains; therefore, the street will be wet\" and \"if the meat is not cooled then it will spoil; the meat is not cooled; therefore, it will spoil\" have the same logical form: they follow the modus ponens. Their form can be expressed more abstractly as \"if A then B; A; therefore B\" in order to make the common syntax explicit. There are various other valid logical forms or rules of inference, like modus tollens or the disjunction elimination. The syntactic approach then holds that an argument is deductively valid if and only if its conclusion can be deduced from its premises using a valid rule of inference. One difficulty for the syntactic approach is that it is usually necessary to express the argument in a formal language in order to assess whether it is valid. This often brings with it the difficulty of translating the natural language argument into a formal language, a process that comes with various problems of its own. Another difficulty is due to the fact that the syntactic approach depends on the distinction between formal and non-formal features. While there is a wide agreement concerning the paradigmatic cases, there are also various controversial cases where it is not clear how this distinction is to be drawn.\n\nThe semantic approach suggests an alternative definition of deductive validity. It is based on the idea that the sentences constituting the premises and conclusions have to be interpreted in order to determine whether the argument is valid. This means that one ascribes semantic values to the expressions used in the sentences, such as the reference to an object for singular terms or to a truth-value for atomic sentences. The semantic approach is also referred to as the model-theoretic approach since the branch of mathematics known as model theory is often used to interpret these sentences. Usually, many different interpretations are possible, such as whether a singular term refers to one object or to another. According to the semantic approach, an argument is deductively valid if and only if there is no possible interpretation where its premises are true and its conclusion is false. Some objections to the semantic approach are based on the claim that the semantics of a language cannot be expressed in the same language, i.e. that a richer metalanguage is necessary. This would imply that the semantic approach cannot provide a universal account of deduction for language as an all-encompassing medium.\n\nRules of inference\n\nDeductive reasoning usually happens by applying rules of inference. A rule of inference is a way or schema of drawing a conclusion from a set of premises. This happens usually based only on the logical form of the premises. A rule of inference is valid if, when applied to true premises, the conclusion cannot be false. A particular argument is valid if it follows a valid rule of inference. Deductive arguments that do not follow a valid rule of inference are called formal fallacies: the truth of their premises does not ensure the truth of their conclusion.\n\nIn some cases, whether a rule of inference is valid depends on the logical system one is using. The dominant logical system is classical logic and the rules of inference listed here are all valid in classical logic. But so-called deviant logics provide a different account of which inferences are valid. For example, the rule of inference known as double negation elimination, i.e. that if a proposition is not not true then it is also true, is accepted in classical logic but rejected in intuitionistic logic.\n\nProminent rules of inference\nModus ponens\n\nModus ponens (also known as \"affirming the antecedent\" or \"the law of detachment\") is the primary deductive rule of inference. It applies to arguments that have as first premise a conditional statement () and as second premise the antecedent () of the conditional statement. It obtains the consequent () of the conditional statement as its conclusion. The argument form is listed below:\n\n  (First premise is a conditional statement)\n\n  (Second premise is the antecedent)\n\n  (Conclusion deduced is the consequent)\n\nIn this form of deductive reasoning, the consequent () obtains as the conclusion from the premises of a conditional statement () and its antecedent (). However, the antecedent () cannot be similarly obtained as the conclusion from the premises of the conditional statement () and the consequent (). Such an argument commits the logical fallacy of affirming the consequent.\n\nThe following is an example of an argument using modus ponens:\n\nIf it is raining, then there are clouds in the sky.\n\nIt is raining.\n\nThus, there are clouds in the sky.\nModus tollens\n\nModus tollens (also known as \"the law of contrapositive\") is a deductive rule of inference. It validates an argument that has as premises a conditional statement (formula) and the negation of the consequent () and as conclusion the negation of the antecedent (). In contrast to modus ponens, reasoning with modus tollens goes in the opposite direction to that of the conditional. The general expression for modus tollens is the following:\n\n. (First premise is a conditional statement)\n\n. (Second premise is the negation of the consequent)\n\n. (Conclusion deduced is the negation of the antecedent)\n\nThe following is an example of an argument using modus tollens:\n\nIf it is raining, then there are clouds in the sky.\n\nThere are no clouds in the sky.\n\nThus, it is not raining.\nHypothetical syllogism\n\nA hypothetical syllogism is an inference that takes two conditional statements and forms a conclusion by combining the hypothesis of one statement with the conclusion of another. Here is the general form:\n\nTherefore, .\n\nIn there being a subformula in common between the two premises that does not occur in the consequence, this resembles syllogisms in term logic, although it differs in that this subformula is a proposition whereas in Aristotelian logic, this common element is a term and not a proposition.\n\nThe following is an example of an argument using a hypothetical syllogism:\n\nIf there had been a thunderstorm, it would have rained.\n\nIf it had rained, things would have gotten wet.\n\nThus, if there had been a thunderstorm, things would have gotten wet.\n\nFallacies\n\nVarious formal fallacies have been described. They are invalid forms of deductive reasoning. An additional aspect of them is that they appear to be valid on some occasions or on the first impression. They may thereby seduce people into accepting and committing them. One type of formal fallacy is affirming the consequent, as in \"if John is a bachelor, then he is male; John is male; therefore, John is a bachelor\". This is similar to the valid rule of inference named modus ponens, but the second premise and the conclusion are switched around, which is why it is invalid. A similar formal fallacy is denying the antecedent, as in \"if Othello is a bachelor, then he is male; Othello is not a bachelor; therefore, Othello is not male\". This is similar to the valid rule of inference called modus tollens, the difference being that the second premise and the conclusion are switched around. Other formal fallacies include affirming a disjunct, denying a conjunct, and the fallacy of the undistributed middle. All of them have in common that the truth of their premises does not ensure the truth of their conclusion. But it may still happen by coincidence that both the premises and the conclusion of formal fallacies are true.\n\nDefinitory and strategic rules\n\nRules of inferences are definitory rules: they determine whether an argument is deductively valid or not. But reasoners are usually not just interested in making any kind of valid argument. Instead, they often have a specific point or conclusion that they wish to prove or refute. So given a set of premises, they are faced with the problem of choosing the relevant rules of inference for their deduction to arrive at their intended conclusion. This issue belongs to the field of strategic rules: the question of which inferences need to be drawn to support one's conclusion. The distinction between definitory and strategic rules is not exclusive to logic: it is also found in various games. In chess, for example, the definitory rules state that bishops may only move diagonally while the strategic rules recommend that one should control the center and protect one's king if one intends to win. In this sense, definitory rules determine whether one plays chess or something else whereas strategic rules determine whether one is a good or a bad chess player. The same applies to deductive reasoning: to be an"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q484284",
  "label": "deductive reasoning",
  "description": "method of reasoning by which premises understood to be true produce logically certain conclusions",
  "aliases": [
   "deductive logic",
   "deduction",
   "deductive methods",
   "deductive inference"
  ],
  "claims": {
   "P31": [
    "Q1047113",
    "Q126723190"
   ],
   "P279": [
    "Q1156402",
    "Q408386"
   ],
   "P361": [
    "Q8078"
   ]
  },
  "revision_id": "2572863441",
  "value_labels": {
   "Q1047113": "field of study",
   "Q126723190": "type of reasoning",
   "Q1156402": "reasoning",
   "Q408386": "inference",
   "Q8078": "logic"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q51942564",
  "label": "Deductive reasoning",
  "description": "scientific article published in January 1999",
  "aliases": [],
  "claims": {
   "P31": [
    "Q13442814"
   ]
  },
  "revision_id": "2510017513",
  "value_labels": {
   "Q13442814": "scholarly article"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q85899967",
  "label": "Deductive reasoning",
  "description": "scientific article published on December 30, 2009",
  "aliases": [],
  "claims": {
   "P31": [
    "Q13442814",
    "Q871232"
   ]
  },
  "revision_id": "2472865341",
  "value_labels": {
   "Q13442814": "scholarly article",
   "Q871232": "editorial"
  },
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
  "ancestor_of": "Q484284",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q126723190",
  "label": "type of reasoning",
  "description": "Wikidata metaclass for reasoning or inference",
  "aliases": [
   "type of inference"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257",
    "Q125161275"
   ]
  },
  "revision_id": "2484566331",
  "ancestor_of": "Q484284",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1156402",
  "label": "reasoning",
  "description": "type of thought and capacity of consciously making sense of things, applying logic, and adapting or justifying practices, institutions, and beliefs based on new or existing information",
  "aliases": [],
  "claims": {
   "P279": [
    "Q7048977",
    "Q9420",
    "Q1799072",
    "Q11398090"
   ]
  },
  "revision_id": "2562551290",
  "ancestor_of": "Q484284",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q408386",
  "label": "inference",
  "description": "act or process of deriving logical conclusions from premises known or assumed to be true",
  "aliases": [],
  "claims": {
   "P31": [
    "Q104637420",
    "Q116505632"
   ],
   "P279": [
    "Q3249551"
   ],
   "P527": [
    "Q484284",
    "Q484511"
   ],
   "P1889": [
    "Q12259609"
   ]
  },
  "revision_id": "2559484289",
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q484284",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q125161275",
  "label": "type of intelligence",
  "description": "Wikidata metaclass for intelligence or cleverness",
  "aliases": [
   "intelligence type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2552317421",
  "ancestor_of": "Q484284",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7048977",
  "label": "intangible entity",
  "description": "entity that does not have a physical existence, including abstract objects and properties",
  "aliases": [
   "abstractum",
   "non-physical entity",
   "abstract entity",
   "intangible",
   "intangible object",
   "intangible thing"
  ],
  "claims": {
   "P31": [
    "Q23958852"
   ],
   "P279": [
    "Q35120",
    "Q142208834",
    "Q142208511"
   ],
   "P361": [
    "Q18205125"
   ],
   "P1889": [
    "Q15706911",
    "Q18706315",
    "Q123139280"
   ]
  },
  "revision_id": "2572642570",
  "ancestor_of": "Q484284",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q9420",
  "label": "thought",
  "description": "mental activity involving an individual's subjective consciousness",
  "aliases": [
   "thinking skill",
   "thinking",
   "think"
  ],
  "claims": {
   "P279": [
    "Q781413"
   ],
   "P361": [
    "Q77468620",
    "Q20984829"
   ],
   "P527": [
    "Q1129066",
    "Q1123855"
   ],
   "P460": [
    "Q349047"
   ],
   "P1889": [
    "Q7784616"
   ]
  },
  "revision_id": "2572575384",
  "ancestor_of": "Q484284",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q1799072",
  "label": "method",
  "description": "planned path to reaching an objective",
  "aliases": [
   "methods",
   "dul:Method"
  ],
  "claims": {
   "P31": [
    "Q1047113",
    "Q2267705"
   ],
   "P279": [
    "Q12774177",
    "Q141439861"
   ],
   "P361": [
    "Q104637332"
   ],
   "P460": [
    "Q2695280"
   ],
   "P1889": [
    "Q351682"
   ]
  },
  "revision_id": "2566702915",
  "ancestor_of": "Q484284",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q11398090",
  "label": "creation",
  "description": "intentional activity during which something comes into being and gains its characteristics",
  "aliases": [
   "creating",
   "formation",
   "forming",
   "process of forming",
   "act of forming",
   "production",
   "generation",
   "apparition",
   "making",
   "creation"
  ],
  "claims": {
   "P31": [
    "Q1914636"
   ],
   "P279": [
    "Q52948"
   ],
   "P460": [
    "Q36492844",
    "Q739302"
   ]
  },
  "revision_id": "2572666739",
  "ancestor_of": "Q484284",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q104637420",
  "label": "sourcing circumstance",
  "description": "base class for P1480 qualifier values",
  "aliases": [],
  "claims": {
   "P31": [
    "Q1969448"
   ],
   "P279": [
    "Q19798642",
    "Q21281405"
   ]
  },
  "revision_id": "2572672538",
  "ancestor_of": "Q484284",
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
  "ancestor_of": "Q51942564",
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
  "ancestor_of": "Q51942564",
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
  "ancestor_of": "Q51942564",
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
  "ancestor_of": "Q51942564",
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
  "ancestor_of": "Q51942564",
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
  "ancestor_of": "Q85899967",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q871232",
  "label": "editorial",
  "description": "journalism genre",
  "aliases": [
   "leading article",
   "leader"
  ],
  "claims": {
   "P31": [
    "Q4894405"
   ],
   "P279": [
    "Q59908",
    "Q267628"
   ],
   "P1889": [
    "Q3719255",
    "Q651270",
    "Q2085381",
    "Q630790",
    "Q2136117"
   ]
  },
  "revision_id": "2552162628",
  "ancestor_of": "Q85899967",
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
  "ancestor_of": "Q85899967",
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
  "ancestor_of": "Q85899967",
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
  "ancestor_of": "Q85899967",
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
  "ancestor_of": "Q85899967",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q4894405",
  "label": "journalism genre",
  "description": "various journalism styles, fields or separate genres, in writing accounts of events",
  "aliases": [
   "form of journalism",
   "type of journalism"
  ],
  "claims": {
   "P31": [
    "Q140354262"
   ],
   "P279": [
    "Q483394"
   ],
   "P1889": [
    "Q2469603"
   ]
  },
  "revision_id": "2557690639",
  "ancestor_of": "Q85899967",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q59908",
  "label": "opinion piece",
  "description": "article that reflects the author's opinion about the subject",
  "aliases": [
   "opinion article",
   "commentary"
  ],
  "claims": {
   "P31": [
    "Q4894405",
    "Q4263830"
   ],
   "P279": [
    "Q5707594"
   ],
   "P361": [
    "Q156035",
    "Q11032"
   ]
  },
  "revision_id": "2496183174",
  "ancestor_of": "Q85899967",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q267628",
  "label": "column",
  "description": "recurring piece or article in a periodical",
  "aliases": [],
  "claims": {
   "P31": [
    "Q4894405"
   ],
   "P279": [
    "Q59908"
   ],
   "P361": [
    "Q1002697"
   ],
   "P527": [
    "Q108970988",
    "Q112692334"
   ],
   "P1889": [
    "Q17628188",
    "Q30849",
    "Q5707594"
   ]
  },
  "revision_id": "2568959671",
  "ancestor_of": "Q85899967",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-05782126-n",
  "lemmas": [
   "deduction",
   "deductive reasoning",
   "synthesis"
  ],
  "gloss": "reasoning from the general to the particular (or from cause to effect)",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-05780353-n"
   ],
   "hyponym": [
    "oewn-05787113-n"
   ]
  },
  "relation_targets": {
   "oewn-05780353-n": "reasoning, logical thinking, abstract thought",
   "oewn-05787113-n": "syllogism"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 2 of 3: Statistics (`ecoz6ylymx`)

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
[
 {
  "title": "Statistics",
  "revision_id": "1375223024",
  "matched_by": "title",
  "text": "Statistics (from German: Statistik, orig. \"description of a state, a country\") is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data. In applying statistics to a scientific, industrial, or social problem, it is conventional to begin with a statistical population or a statistical model to be studied. Populations can be diverse groups of people or objects such as \"all people living in a country\" or \"every atom composing a crystal\". Statistics deals with every aspect of data, including the planning of data collection in terms of the design of surveys and experiments. Statistics is deeply related to subjects like physics, chemistry, geography, geopolitics, and especially mathematics.\n\nWhen census data (comprising every member of the target population) cannot be collected, statisticians collect data by developing specific experiment designs and survey samples. Random sampling assures that inferences and conclusions can reasonably extend from the sample to the population as a whole. An experimental study involves taking measurements of the system under study, manipulating the system, and then taking additional measurements using the same procedure to determine if the manipulation has modified the values of the measurements. In contrast, an observational study does not involve experimental manipulation.\n\nTwo main statistical methods are used in data analysis: descriptive statistics, which summarize data from a sample using indexes such as the mean or standard deviation, and inferential statistics, which draw conclusions from data that are subject to random variation (e.g., observational errors, sampling variation). Descriptive statistics are most often concerned with two sets of properties of a distribution (sample or population): central tendency (or location) seeks to characterize the distribution's central or typical value, while dispersion (or variability) characterizes the extent to which members of the distribution depart from its center and each other. Inferences made using mathematical statistics employ the framework of probability theory, which deals with the analysis of random phenomena.\n\nA standard statistical procedure involves the collection of data leading to a test of the relationship between two statistical data sets, or a data set and synthetic data drawn from an idealized model. A hypothesis is proposed for the statistical relationship between the two data sets, an alternative to an idealized null hypothesis of no relationship between two data sets. Rejecting or disproving the null hypothesis is done using statistical tests that quantify the sense in which the null can be proven false, given the data that are used in the test. Working from a null hypothesis, two basic forms of error are recognized: Type I errors (null hypothesis is rejected when it is in fact true, giving a \"false positive\") and Type II errors (null hypothesis fails to be rejected when it is in fact false, giving a \"false negative\"). Multiple problems have come to be associated with this framework, ranging from obtaining a sufficient sample size to specifying an adequate null hypothesis.\n\nStatistical measurement processes are also prone to error with regard to the data they generate. Many of these errors are classified as random (noise) or systematic (bias), but other types of errors (e.g., blunder, such as when an analyst reports incorrect units) can also occur. The presence of missing data or censoring may result in biased estimates, and specific techniques have been developed to address these problems.\n\nIntroduction\n\n\"Statistics is both the science of uncertainty and the technology of extracting information from data.\" - featured in the International Encyclopedia of Statistical Science.\nStatistics is the discipline that deals with data, facts and figures with which meaningful information is inferred. Data may represent a numerical value, in form of quantitative data, or a label, as with qualitative data. Data may be collected, presented and summarised, in one of two methods called descriptive statistics. Two elementary summaries of data, singularly called a statistic, are the mean and dispersion. Whereas inferential statistics interprets data from a population sample to induce statements and predictions about a population.\n\nStatistics is regarded as a body of science or a branch of mathematics. It is based on probability, a branch of mathematics that studies random events. Statistics is considered the science of uncertainty. This arises from the ways to cope with measurement and sampling error as well as dealing with uncertanties in modelling. Although probability and statistics were once paired together as a single subject, they are conceptually distinct from one another. The former is based on deducing answers to specific situations from a general theory of probability, meanwhile statistics induces statements about a population based on a data set. Statistics serves to bridge the gap between probability and applied mathematical fields.\n\nSome consider statistics to be a distinct mathematical science rather than a branch of mathematics. While many scientific investigations make use of data, statistics is generally concerned with the use of data in the context of uncertainty and decision-making in the face of uncertainty. Statistics is indexed at 62, a subclass of probability theory and stochastic processes, in the Mathematics Subject Classification. Mathematical statistics is covered in the range 276-280 of subclass QA (science > mathematics) in the Library of Congress Classification.\n\nThe word statistics ultimately comes from the Latin word Status, meaning \"situation\" or \"condition\" in society, which in late Latin adopted the meaning \"state\". Derived from this, political scientist Gottfried Achenwall, coined the German word statistik (a summary of how things stand). In 1770, the term entered the English language through German and referred to the study of political arrangements. The term gained its modern meaning in the 1790s in John Sinclair's works. In modern German, the term statistik is synonymous with mathematical statistics. The term statistic, in singular form, is used to describe a function that returns its value of the same name.\n\nStatistical data\n\nData collection\nSampling\n\nWhen census data cannot be collected, statisticians collect sample data by developing specific experiment designs and survey samples. Statistics itself also provides tools for prediction and forecasting through statistical models.\n\nTo use a sample as a guide to an entire population, it is important that it truly represents the overall population. Representative sampling ensures that inferences and conclusions can safely be extended from the sample to the population as a whole. A major problem lies in determining the extent to which the chosen sample is actually representative. Statistics offers methods to estimate and correct for any bias in the sample and data collection procedures. There are also methods of experimental design that can lessen these issues at the outset of a study, strengthening its ability to discern truths about the population.\n\nSampling theory is part of the mathematical discipline of probability theory. Probability is used in mathematical statistics to study the sampling distributions of sample statistics and, more generally, the properties of statistical procedures. The use of any statistical method is valid only if the system or population under consideration satisfies the assumptions of the method. The difference in point of view between classic probability theory and sampling theory is, roughly, that probability theory starts with the given parameters of a total population to deduce probabilities that pertain to samples. Statistical inference, however, moves in the opposite direction—inductively inferring from samples to the parameters of a larger or total population.\n\nExperimental and observational studies\n\nA common goal for a statistical research project is to investigate causality, and in particular to draw a conclusion on the effect of changes in the values of predictors or independent variables on dependent variables. There are two major types of causal statistical studies: experimental studies and observational studies. In both types of studies, the effect of differences of an independent variable (or variables) on the behavior of the dependent variable are observed. The difference between the two types lies in how the study is actually conducted. Each can be very effective. An experimental study involves taking measurements of the system under study, manipulating the system, and then taking additional measurements with different levels using the same procedure to determine if the manipulation has modified the values of the measurements. In contrast, an observational study does not involve experimental manipulation. Instead, data are gathered and correlations between predictors and response are investigated. While the tools of data analysis work best on data from randomized studies, they are also applied to other kinds of data—like natural experiments and observational studies—for which a statistician would use a modified, more structured estimation method (e.g., difference in differences estimation and instrumental variables, among many others) that produce consistent estimators.\n\nExperiments\n\nThe basic steps of a statistical experiment are:\n\nPlanning the research, including finding the number of replicates of the study, using the following information: preliminary estimates regarding the size of treatment effects, alternative hypotheses, and the estimated experimental variability. Consideration of the selection of experimental subjects and the ethics of research is necessary. Statisticians recommend that experiments compare (at least) one new treatment with a standard treatment or control, to allow an unbiased estimate of the difference in treatment effects.\n\nDesign of experiments, using blocking to reduce the influence of confounding variables, and randomized assignment of treatments to subjects to allow unbiased estimates of treatment effects and experimental error. At this stage, the experimenters and statisticians write the experimental protocol that will guide the performance of the experiment and which specifies the primary analysis of the experimental data.\n\nPerforming the experiment following the experimental protocol and analyzing the data following the experimental protocol.\n\nFurther examining the data set in secondary analyses, to suggest new hypotheses for future study.\n\nDocumenting and presenting the results of the study.\n\nExperiments on human behavior have special concerns. The famous Hawthorne study examined changes to the working environment at the Hawthorne plant of the Western Electric Company. The researchers were interested in determining whether increased illumination would increase the productivity of the assembly line workers. The researchers first measured the productivity in the plant, then modified the illumination in an area of the plant and checked if the changes in illumination affected productivity. It turned out that productivity indeed improved (under the experimental conditions). However, the study is heavily criticized today for errors in experimental procedures, specifically for the lack of a control group and blindness. The Hawthorne effect refers to finding that an outcome (in this case, worker productivity) changed due to observation itself. Those in the Hawthorne study became more productive not because the lighting was changed but because they were being observed.\n\nObservational study\n\nAn example of an observational study is one that explores the association between smoking and lung cancer. This type of study typically uses a survey to collect observations about the area of interest and then performs statistical analysis. In this case, the researchers would collect observations of both smokers and non-smokers, perhaps through a cohort study, and then look for the number of cases of lung cancer in each group. A case-control study is another type of observational study in which people with and without the outcome of interest (e.g. lung cancer) are invited to participate and their exposure histories are collected.\n\nTypes of data\n\nVarious attempts have been made to produce a taxonomy of levels of measurement. The psychophysicist Stanley Smith Stevens defined nominal, ordinal, interval, and ratio scales. Nominal measurements do not have meaningful rank order among values, and permit any one-to-one (injective) transformation. Ordinal measurements have imprecise differences between consecutive values, but have a meaningful order to those values, and permit any order-preserving transformation. Interval measurements have meaningful distances between measurements defined, but the zero value is arbitrary (as in the case with longitude and temperature measurements in Celsius or Fahrenheit), and permit any linear transformation. Ratio measurements have both a meaningful zero value and the distances between different measurements defined, and permit any rescaling transformation.\n\nBecause variables conforming only to nominal or ordinal measurements cannot be reasonably measured numerically, sometimes they are grouped together as categorical variables, whereas ratio and interval measurements are grouped together as quantitative variables, which can be either discrete or continuous, due to their numerical nature. Such distinctions can often be loosely correlated with data type in computer science, in that dichotomous categorical variables may be represented with the Boolean data type, polytomous categorical variables with arbitrarily assigned integers in the integral data type, and continuous variables with the real data type involving floating-point arithmetic. But the mapping of computer science data types to statistical data types depends on which categorization of the latter is being implemented.\n\nOther categorizations have been proposed. For example, Mosteller and Tukey (1977) distinguished grades, ranks, counted fractions, counts, amounts, and balances. Nelder (1990) described continuous counts, continuous ratios, count ratios, and categorical modes of data. (See also: Chrisman (1998), van den Berg (1991).)\n\nThe issue of whether it is appropriate to apply different kinds of statistical methods to data obtained from different kinds of measurement procedures is complicated by issues concerning the transformation of variables and the precise interpretation of research questions. \"The relationship between the data and what they describe merely reflects the fact that certain kinds of statistical statements may have truth values that are not invariant under some transformations. Whether a transformation is sensible to contemplate depends on the question one is trying to answer.\"\n\nMethods\n\nDescriptive statistics\n\nA descriptive statistic (in the count noun sense) is a summary statistic that quantitatively describes or summarizes features of a collection of information, while descriptive statistics in the mass noun sense is the process of using and analyzing those statistics. Descriptive statistics is distinguished from inferential statistics (or inductive statistics), in that descriptive statistics aims to summarize a sample, rather than use the data to learn about the population that the sample of data is thought to represent.\n\nInferential statistics\n\nStatistical inference is the process of using data analysis to deduce properties of an underlying probability distribution. Inferential statistical analysis infers properties of a population, for example by testing hypotheses and deriving estimates. It is assumed that the observed data set is sampled from a larger population. Inferential statistics can be contrasted with descriptive statistics. Descriptive statistics is solely concerned with properties of the observed data, and it does not rest on the assumption that the data come from a larger population.\n\nTerminology and theory of inferential statistics\nStatistics, estimators and pivotal quantities\n\nConsider independent identically distributed (IID) random variables with a given probability distribution: standard statistical inference and estimation theory defines a random sample as the random vector given by the column vector of these IID variables. The population being examined is described by a probability distribution that may have unknown parameters.\n\nA statistic is a random variable that is a function of the random sample, but not a function of unknown parameters. The probability distribution of the statistic, though, may have unknown parameters. Consider now a function of the unknown parameter: an estimator is a statistic used to estimate such function. Commonly used estimators include sample mean, unbiased sample variance and sample covariance.\n\nA random variable that is a function of the random sample and of the unknown parameter, but whose probability distribution does not depend on the unknown parameter is called a pivotal quantity or pivot. Widely used pivots include the z-score, the chi square statistic and Student's t-value.\n\nBetween two estimators of a given parameter, the one with lower mean squared error is said to be more efficient. Furthermore, an estimator is said to be unbiased if its expected value is equal to the true value of the unknown parameter being estimated, and asymptotically unbiased if its expected value converges at the limit to the true value of such parameter.\n\nOther desirable properties for estimators include: UMVUE estimators that have the lowest variance for all possible values of the parameter to be estimated (this is usually an easier property to verify than efficiency) and consistent estimators which converges in probability to the true value of such parameter.\n\nThis still leaves the question of how to obtain estimators in a given situation and carry the computation, several methods have been proposed: the method of moments, the maximum likelihood method, the least squares method and the more recent method of estimating equations.\n\nNull hypothesis and alternative hypothesis\n\nInterpretation of statistical information can often involve the development of a null hypothesis which is usually (but not necessarily) that no relationship exists among variables or that no change occurred over time. The alternative hypothesis is the name of the hypothesis that contradicts the null hypothesis.\n\nThe best illustration for a novice is the predicament encountered by a criminal trial. The null hypothesis, H0, asserts that the defendant is innocent, whereas the alternative hypothesis, H1, asserts that the defendant is guilty. The indictment comes because of suspicion of the guilt. The H0 (the status quo) stands in opposition to H1 and is maintained unless H1 is supported by evidence \"beyond a reasonable doubt\". However, \"failure to reject H0\" in this case does not imply innocence, but merely that the evidence was insufficient to convict. So the jury does not necessarily accept H0 but fails to reject H0. While one can not \"prove\" a null hypothesis, one can test how close it is to being true with a power test, which tests for type II errors. The null hypothesis cannot be proven true because it is already assumed to be true when the test is being conducted.\n\nError\n\nWorking from a null hypothesis, two broad categories of error are recognized:\n\nType I errors where the null hypothesis is falsely rejected, giving a \"false positive\".\n\nType II errors where the null hypothesis fails to be rejected and an actual difference between populations is missed, giving a \"false negative\".\n\nStandard deviation refers to the extent to which individual observations in a sample differ from a central value, such as the sample or population mean, while Standard error refers to an estimate of difference between sample mean and population mean.\n\nA statistical error is the amount by which an observation differs from its expected value. A residual is the amount an observation differs from the value the estimator of the expected value assumes on a given sample (also called prediction).\n\nMean squared error is used for obtaining efficient estimators, a widely used class of estimators. Root mean square error is simply the square root of mean squared error.\n\nMany statistical methods seek to minimize the residual sum of squares, and these are called \"methods of least squares\" in contrast to Least absolute deviations."
 },
 {
  "title": "Statistical inference",
  "revision_id": "1364302166",
  "matched_by": "redirect",
  "text": "Statistical inference is the process of using data analysis to infer properties of an underlying probability distribution. Inferential statistical analysis infers properties of a population, for example by testing hypotheses and deriving estimates. It is assumed that the observed data set is sampled from a larger population.\n\nInferential statistics can be contrasted with descriptive statistics. Descriptive statistics is solely concerned with properties of the observed data, and it does not rest on the assumption that the data come from a larger population. In machine learning, the term inference is sometimes used instead to mean \"make a prediction, by evaluating an already trained model\"; in this context inferring properties of the model is referred to as training or learning (rather than inference), and using a model for prediction is referred to as inference (instead of prediction); see also predictive inference.\n\nIntroduction\n\nStatistical inference makes propositions about a population, using data drawn from the population with some form of sampling. Given a hypothesis about a population, for which we wish to draw inferences, statistical inference consists of (first) selecting a statistical model of the process that generates the data and (second) deducing propositions from the model.\n\nKonishi and Kitagawa state \"The majority of the problems in statistical inference can be considered to be problems related to statistical modeling\". Relatedly, Sir David Cox has said, \"How [the] translation from subject-matter problem to statistical model is done is often the most critical part of an analysis\".\n\nThe conclusion of a statistical inference is a statistical proposition. Some common forms of statistical proposition are the following:\n\na point estimate, i.e. a particular value that best approximates some parameter of interest;\n\nan interval estimate, e.g. a confidence interval (or set estimate). A confidence interval is an interval constructed using data from a sample, such that if the procedure were repeated over many independent samples (mathematically, by taking the limit), a fixed proportion (e.g., 95% for a 95% confidence interval) of the resulting intervals would contain the true value of the parameter, i.e., the population parameter;\n\na credible interval, i.e. a set of values containing, for example, 95% of posterior belief;\n\nrejection of a hypothesis;\n\nclustering or classification of data points into groups.\n\nModels and assumptions\n\nAny statistical inference requires some assumptions. A statistical model is a set of assumptions concerning the generation of the observed data and similar data. Descriptions of statistical models usually emphasize the role of population quantities of interest, about which we wish to draw inference. Descriptive statistics are typically used as a preliminary step before more formal inferences are drawn.\n\nDegree of models/assumptions\n\nStatisticians distinguish between three levels of modeling assumptions:\n\nFully parametric: The probability distributions describing the data-generation process are assumed to be fully described by a family of probability distributions involving only a finite number of unknown parameters. For example, one may assume that the distribution of population values is truly Normal, with unknown mean and variance, and that datasets are generated by 'simple' random sampling. The family of generalized linear models is a widely used and flexible class of parametric models.\n\nNon-parametric: The assumptions made about the process generating the data are much less than in parametric statistics and may be minimal. For example, every continuous probability distribution has a median, which may be estimated using the sample median or the Hodges–Lehmann–Sen estimator, which has good properties when the data arise from simple random sampling.\n\nSemi-parametric: This term typically implies assumptions 'in between' fully and non-parametric approaches. For example, one may assume that a population distribution has a finite mean. Furthermore, one may assume that the mean response level in the population depends in a truly linear manner on some covariate (a parametric assumption) but not make any parametric assumption describing the variance around that mean (i.e. about the presence or possible form of any heteroscedasticity). More generally, semi-parametric models can often be separated into 'structural' and 'random variation' components. One component is treated parametrically and the other non-parametrically. The well-known Cox model is a set of semi-parametric assumptions.\n\nImportance of valid models/assumptions\n\nWhatever level of assumption is made, correctly calibrated inference, in general, requires these assumptions to be correct; i.e. that the data-generating mechanisms really have been correctly specified.\n\nIncorrect assumptions of 'simple' random sampling can invalidate statistical inference. More complex semi- and fully parametric assumptions are also cause for concern. For example, incorrectly assuming the Cox model can in some cases lead to faulty conclusions. Incorrect assumptions of Normality in the population also invalidates some forms of regression-based inference. The use of any parametric model is viewed skeptically by most experts in sampling human populations: \"most sampling statisticians, when they deal with confidence intervals at all, limit themselves to statements about [estimators] based on very large samples, where the central limit theorem ensures that these [estimators] will have distributions that are nearly normal.\" In particular, a normal distribution \"would be a totally unrealistic and catastrophically unwise assumption to make if we were dealing with any kind of economic population.\" Here, the central limit theorem states that the distribution of the sample mean \"for very large samples\" is approximately normally distributed, if the distribution is not heavy-tailed.\n\nApproximate distributions\n\nGiven the difficulty in specifying exact distributions of sample statistics, many methods have been developed for approximating these.\n\nWith finite samples, approximation results measure how close a limiting distribution approaches the statistic's sample distribution: For example, with 10,000 independent samples the normal distribution approximates (to two digits of accuracy) the distribution of the sample mean for many population distributions, by the Berry–Esseen theorem. Yet for many practical purposes, the normal approximation provides a good approximation to the sample-mean's distribution when there are 10 (or more) independent samples, according to simulation studies and statisticians' experience. Following Kolmogorov's work in the 1950s, advanced statistics uses approximation theory and functional analysis to quantify the error of approximation. In this approach, the metric geometry of probability distributions is studied; this approach quantifies approximation error with, for example, the Kullback–Leibler divergence, Bregman divergence, and the Hellinger distance.\n\nWith indefinitely large samples, limiting results like the central limit theorem describe the sample statistic's limiting distribution if one exists. Limiting results are not statements about finite samples, and indeed are irrelevant to finite samples. However, the asymptotic theory of limiting distributions is often invoked for work with finite samples. For example, limiting results are often invoked to justify the generalized method of moments and the use of generalized estimating equations, which are popular in econometrics and biostatistics. The magnitude of the difference between the limiting distribution and the true distribution (formally, the 'error' of the approximation) can be assessed using simulation. The heuristic application of limiting results to finite samples is common practice in many applications, especially with low-dimensional models with log-concave likelihoods (such as with one-parameter exponential families).\n\nRandomization-based models\n\nFor a given dataset that was produced by a randomization design, the randomization distribution of a statistic (under the null-hypothesis) is defined by evaluating the test statistic for all of the plans that could have been generated by the randomization design. In frequentist inference, the randomization allows inferences to be based on the randomization distribution rather than a subjective model, and this is important especially in survey sampling and design of experiments. Statistical inference from randomized studies is also more straightforward than many other situations. In Bayesian inference, randomization is also of importance: in survey sampling, use of sampling without replacement ensures the exchangeability of the sample with the population; in randomized experiments, randomization warrants a missing at random assumption for covariate information.\n\nObjective randomization allows properly inductive procedures. Many statisticians prefer randomization-based analysis of data that was generated by well-defined randomization procedures. (However, it is true that in fields of science with developed theoretical knowledge and experimental control, randomized experiments may increase the costs of experimentation without improving the quality of inferences.) Similarly, results from randomized experiments are recommended by leading statistical authorities as allowing inferences with greater reliability than do observational studies of the same phenomena. However, a good observational study may be better than a bad randomized experiment.\n\nThe statistical analysis of a randomized experiment may be based on the randomization scheme stated in the experimental protocol and does not need a subjective model.\n\nHowever, at any time, some hypotheses cannot be tested using objective statistical models, which accurately describe randomized experiments or random samples. In some cases, such randomized studies are uneconomical or unethical.\n\nModel-based analysis of randomized experiments\n\nIt is standard practice to refer to a statistical model, e.g., a linear or logistic models, when analyzing data from randomized experiments. However, the randomization scheme guides the choice of a statistical model. It is not possible to choose an appropriate model without knowing the randomization scheme. Seriously misleading results can be obtained analyzing data from randomized experiments while ignoring the experimental protocol; common mistakes include forgetting the blocking used in an experiment and confusing repeated measurements on the same experimental unit with independent replicates of the treatment applied to different experimental units.\n\nModel-free randomization inference\n\nModel-free techniques provide a complement to model-based methods, which employ reductionist strategies of reality-simplification. The former combine, evolve, ensemble and train algorithms dynamically adapting to the contextual affinities of a process and learning the intrinsic characteristics of the observations.\n\nFor example, model-free simple linear regression is based either on:\n\na random design, where the pairs of observations are independent and identically distributed (iid),\n\nor a deterministic design, where the variables are deterministic, but the corresponding response variables are random and independent with a common conditional distribution, i.e., , which is independent of the index .\n\nIn either case, the model-free randomization inference for features of the common conditional distribution relies on some regularity conditions, e.g. functional smoothness. For instance, model-free randomization inference for the population feature conditional mean, , can be consistently estimated via local averaging or local polynomial fitting, under the assumption that is smooth. Also, relying on asymptotic normality or resampling, we can construct confidence intervals for the population feature, in this case, the conditional mean, .\n\nParadigms for inference\n\nDifferent schools of statistical inference have become established. These schools—or \"paradigms\"—are not mutually exclusive, and methods that work well under one paradigm often have attractive interpretations under other paradigms.\n\nBandyopadhyay and Forster describe four paradigms: The classical (or frequentist) paradigm, the Bayesian paradigm, the likelihoodist paradigm, and the Akaikean-Information Criterion-based paradigm.\n\nFrequentist inference\n\nThis paradigm calibrates the plausibility of propositions by considering (notional) repeated sampling of a population distribution to produce datasets similar to the one at hand. By considering the dataset's characteristics under repeated sampling, the frequentist properties of a statistical proposition can be quantified—although in practice this quantification may be challenging.\n\nExamples of frequentist inference\n\np-value\n\nConfidence interval\n\nNull hypothesis significance testing\nFrequentist inference, objectivity, and decision theory\n\nOne interpretation of frequentist inference (or classical inference) is that it is applicable only in terms of frequency probability; that is, in terms of repeated sampling from a population. However, the approach of Neyman develops these procedures in terms of pre-experiment probabilities. That is, before undertaking an experiment, one decides on a rule for coming to a conclusion such that the probability of being correct is controlled in a suitable way: such a probability need not have a frequentist or repeated sampling interpretation. In contrast, Bayesian inference works in terms of conditional probabilities (i.e. probabilities conditional on the observed data), compared to the marginal (but conditioned on unknown parameters) probabilities used in the frequentist approach.\n\nThe frequentist procedures of significance testing and confidence intervals can be constructed without regard to utility functions. However, some elements of frequentist statistics, such as statistical decision theory, do incorporate utility functions. In particular, frequentist developments of optimal inference (such as minimum-variance unbiased estimators, or uniformly most powerful testing) make use of loss functions, which play the role of (negative) utility functions. Loss functions need not be explicitly stated for statistical theorists to prove that a statistical procedure has an optimality property. However, loss-functions are often useful for stating optimality properties: for example, median-unbiased estimators are optimal under absolute value loss functions, in that they minimize expected loss, and least squares estimators are optimal under squared error loss functions, in that they minimize expected loss.\n\nWhile statisticians using frequentist inference must choose for themselves the parameters of interest, and the estimators/test statistic to be used, the absence of obviously explicit utilities and prior distributions has helped frequentist procedures to become widely viewed as 'objective'.\n\nBayesian inference\n\nThe Bayesian calculus describes degrees of belief using the 'language' of probability; beliefs are positive, integrate into one, and obey probability axioms. Bayesian inference uses the available posterior beliefs as the basis for making statistical propositions. There are several different justifications for using the Bayesian approach.\n\nExamples of Bayesian inference\n\nCredible interval for interval estimation\n\nBayes factors for model comparison\nBayesian inference, subjectivity and decision theory\n\nMany informal Bayesian inferences are based on \"intuitively reasonable\" summaries of the posterior. For example, the posterior mean, median and mode, highest posterior density intervals, and Bayes Factors can all be motivated in this way. While a user's utility function need not be stated for this sort of inference, these summaries do all depend (to some extent) on stated prior beliefs, and are generally viewed as subjective conclusions. (Methods of prior construction which do not require external input have been proposed but not yet fully developed.)\n\nFormally, Bayesian inference is calibrated with reference to an explicitly stated utility, or loss function; the 'Bayes rule' is the one which maximizes expected utility, averaged over the posterior uncertainty. Formal Bayesian inference therefore automatically provides optimal decisions in a decision theoretic sense. Given assumptions, data and utility, Bayesian inference can be made for essentially any problem, although not every statistical inference need have a Bayesian interpretation. Analyses which are not formally Bayesian can be (logically) incoherent; a feature of Bayesian procedures which use proper priors (i.e. those integrable to one) is that they are guaranteed to be coherent. Some advocates of Bayesian inference assert that inference must take place in this decision-theoretic framework, and that Bayesian inference should not conclude with the evaluation and summarization of posterior beliefs.\n\nLikelihood-based inference\n\nLikelihood-based inference is a paradigm used to estimate the parameters of a statistical model based on observed data. Likelihoodism approaches statistics by using the likelihood function, denoted as , quantifies the probability of observing the given data , assuming a specific set of parameter values . In likelihood-based inference, the goal is to find the set of parameter values that maximizes the likelihood function, or equivalently, maximizes the probability of observing the given data.\n\nThe process of likelihood-based inference usually involves the following steps:\n\nFormulating the statistical model: A statistical model is defined based on the problem at hand, specifying the distributional assumptions and the relationship between the observed data and the unknown parameters. The model can be simple, such as a normal distribution with known variance, or complex, such as a hierarchical model with multiple levels of random effects.\n\nConstructing the likelihood function: Given the statistical model, the likelihood function is constructed by evaluating the joint probability density or mass function of the observed data as a function of the unknown parameters. This function represents the probability of observing the data for different values of the parameters.\n\nMaximizing the likelihood function: The next step is to find the set of parameter values that maximizes the likelihood function. This can be achieved using optimization techniques such as numerical optimization algorithms. The estimated parameter values, often denoted as , are the maximum likelihood estimates (MLEs).\n\nAssessing uncertainty: Once the MLEs are obtained, it is crucial to quantify the uncertainty associated with the parameter estimates. This can be done by calculating standard errors, confidence intervals, or conducting hypothesis tests based on asymptotic theory or simulation techniques such as bootstrapping.\n\nModel checking: After obtaining the parameter estimates and assessing their uncertainty, it is important to assess the adequacy of the statistical model. This involves checking the assumptions made in the model and evaluating the fit of the model to the data using goodness-of-fit tests, residual analysis, or graphical diagnostics.\n\nInference and interpretation: Finally, based on the estimated parameters and model assessment, statistical inference can be performed. This involves drawing conclusions about the population parameters, making predictions, or testing hypotheses based on the estimated model.\n\nAIC-based inference\n\nThe Akaike information criterion (AIC) is an estimator of the relative quality of statistical models for a given set of data. Given a collection of models for the data, AIC estimates the quality of each model, relative to each of the other models. Thus, AIC provides a means for model selection.\n\nAIC is founded on information theory: it offers an estimate of the relative information lost when a given model is used to represent the process that generated the data. (In doing so, it deals with the trade-off between the goodness of fit of the model and the simplicity of the model.)\n\nOther paradigms for inference\nMinimum description length\n\nThe minimum description length (MDL) principle has been developed from ideas in information theory and the theory of Kolmogorov complexity. The (MDL) principle selects statistical models that maximally compress the data; inference proceeds without assuming counterfactual or non-falsifiable \"data-generating mechanisms\" or probability models for the data, as might be done in frequentist or Bayesian approaches.\n\nHowever, if a \"data generating mechanism\" does exist in reality, then according to Shannon's source coding theorem it provides the MDL description of the data, on average and asymptotically. In minimizing description length (or descriptive complexity), MDL estimation is similar to maximum likelihood estimation and maximum a posteriori estimation (using maximum-entropy Bayesian priors). However, MDL avoids assuming that the underlying probability model is known; the MDL principle can also be applied without assumptions that e.g. the data arose from independent sampling.\n\nThe MDL principle has been applied in communication-coding theory in information theory, in linear regression, and in data mining.\n\nThe evaluation of MDL-based inferential procedures often uses techniques or criteria from computational complexity theory.\n\nFiducial inference\n\nFiducial inference was an approach to statistical inference based on fiducial probability, also known as a \"fiducial distribution\". In subsequent work, this approach has been called ill-defined, extremely limited in applicability, and even fallacious. However this argument is the same as that which shows that a so-called confidence distribution is not a valid probability distribution and, since this has not invalidated the application of confidence intervals, it does not necessarily invalidate conclusions drawn from"
 },
 {
  "title": "Statistics (song)",
  "revision_id": "1369714227",
  "matched_by": "title-minus-qualifier",
  "text": "\"Statistics\" is an R&B/soul song performed and released by Chester Lyfe Jennings who also co-wrote the song with Tyler Williams. Released in 2010, it was the first track on the artists, self-proclaimed, fourth and final album,I Still Believe. On June 22, 2010, “Statistics,” was released as a single where it reached 19 on the Billboard R&B/Hip-Hop songs list on September 4, 2010.\n\nThe song was inspired by Steve Harvey’s book, \"Act Like a Lady, Think Like a Man:What Men Really Think About Love, Relationships, Intimacy, and Commitment,\" and belts out statistics such as, \n\n\"25% of all men are unstable,\n\n25% of all men can't be faithful\n\n30% of them don't mean what they say\n\nAnd 10% of the remaining 20 is gay\n\nThat leaves you a 10% chance of ever finding your man\"\n\nThis is sung to a “lullaby-like piano melody”. The song also offers advice on keeping that good one, once he is found. \n\n\"Tell him that you're celibate\n\nAnd if he wants some of your goodies he gon' have to work for it\"\n\nPromotion\n\n\"Lyfe\" interviewed with Mo'Nique of \"The \"Mo'Nique\" show. The show aired on the network BET in June 2010. Following the interview on his career and his personal life, \"Lyfe\" performed the song \"Statistics\".\n\n\"Essence\" magazine was allowed a behind the scenes interview and rights to release the music video for \"Statistics\" on their website \"Essence.com\"\n\n\"Lyfe\" sat down for a \"round table\" interview with the R&B lifestyle magazine \"SingersRoom\". During the interview, he discussed \"unstable\" and \"cheating\" men, as well as \"Statistics\" and his reason for writing the song. The interview debuted on the SingersRoom website in August 2010.\n\nMusic video\n\nJennings premiered the “Statistics” video on the internet as part of an interview for Essence Magazine. The exclusive, début, was uploaded on July 13, 2010 on the essence.com website. It was released for sale on July 28, 2010.\nThere are two different videos. Both versions are similar and include an opening scene of a close up of the face of Jennings singing in the parlando style, the words:\n\n“Alright, alright, alright\n\ny’all settle down settle down settle down.\n\nIf you don't know where you are this is Statistics 101\n\nand I’m your teacher Lyfe Jennings in the flesh baby.\n\nBooks out, let’s go.”.\n\nThe second version includes an introduction, which feature eleven women talking about their prior abusive or unhealthy relationships. This introduction is the only deviation in the two videos.\n\nCharts\n\nReferences"
 }
]

Wikidata candidates and their ancestors (ancestor_of names the candidate each ancestor belongs to):
[
 {
  "qid": "Q12483",
  "label": "statistics",
  "description": "study of the collection, analysis, interpretation, and presentation of data",
  "aliases": [
   "stats",
   "statistical sciences"
  ],
  "claims": {
   "P31": [
    "Q4671286"
   ],
   "P279": [
    "Q395",
    "Q816264"
   ],
   "P361": [
    "Q395",
    "Q8134"
   ],
   "P527": [
    "Q380344",
    "Q28873772"
   ],
   "P1889": [
    "Q1949963"
   ]
  },
  "revision_id": "2570012060",
  "value_labels": {
   "Q4671286": "academic major",
   "Q395": "mathematics",
   "Q816264": "formal science",
   "Q8134": "economics",
   "Q380344": "descriptive statistics",
   "Q28873772": "inferential statistics",
   "Q1949963": "statistic"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q938438",
  "label": "statistical inference",
  "description": "process of deducing properties of an underlying probability distribution by analysis of data",
  "aliases": [
   "inference",
   "probabilistic reasoning"
  ],
  "claims": {
   "P31": [
    "Q126723190"
   ],
   "P279": [
    "Q408386"
   ],
   "P1889": [
    "Q7604398"
   ]
  },
  "revision_id": "2539094623",
  "value_labels": {
   "Q126723190": "type of reasoning",
   "Q408386": "inference",
   "Q7604398": "statistical interference"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q7604424",
  "label": "Statistics",
  "description": "single by Lyfe Jennings",
  "aliases": [],
  "claims": {
   "P31": [
    "Q134556"
   ]
  },
  "revision_id": "2481595516",
  "value_labels": {
   "Q134556": "single"
  },
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
  "ancestor_of": "Q12483",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
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
  "ancestor_of": "Q12483",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q816264",
  "label": "formal science",
  "description": "field of study concerned with formal systems, abstract structures, and deductions derived from their definitions and rules",
  "aliases": [],
  "claims": {
   "P31": [
    "Q2465832"
   ],
   "P279": [
    "Q475023"
   ],
   "P527": [
    "Q395",
    "Q8078",
    "Q12483",
    "Q44455",
    "Q269699",
    "Q21198",
    "Q336"
   ]
  },
  "revision_id": "2551249191",
  "ancestor_of": "Q12483",
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
  "ancestor_of": "Q12483",
  "level": 2,
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
  "ancestor_of": "Q12483",
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
  "ancestor_of": "Q12483",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q475023",
  "label": "exact science",
  "description": "sciences that admit of absolute precision in their results",
  "aliases": [
   "exact sciences",
   "exact mathematical sciences"
  ],
  "claims": {
   "P31": [
    "Q2465832"
   ],
   "P279": [
    "Q336"
   ]
  },
  "revision_id": "2551575216",
  "ancestor_of": "Q12483",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q126723190",
  "label": "type of reasoning",
  "description": "Wikidata metaclass for reasoning or inference",
  "aliases": [
   "type of inference"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257",
    "Q125161275"
   ]
  },
  "revision_id": "2484566331",
  "ancestor_of": "Q938438",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q408386",
  "label": "inference",
  "description": "act or process of deriving logical conclusions from premises known or assumed to be true",
  "aliases": [],
  "claims": {
   "P31": [
    "Q104637420",
    "Q116505632"
   ],
   "P279": [
    "Q3249551"
   ],
   "P527": [
    "Q484284",
    "Q484511"
   ],
   "P1889": [
    "Q12259609"
   ]
  },
  "revision_id": "2559484289",
  "ancestor_of": "Q938438",
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
  "ancestor_of": "Q938438",
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
  "ancestor_of": "Q938438",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q125161275",
  "label": "type of intelligence",
  "description": "Wikidata metaclass for intelligence or cleverness",
  "aliases": [
   "intelligence type"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21146257"
   ],
   "P1889": [
    "Q110403031"
   ]
  },
  "revision_id": "2552317421",
  "ancestor_of": "Q938438",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q104637420",
  "label": "sourcing circumstance",
  "description": "base class for P1480 qualifier values",
  "aliases": [],
  "claims": {
   "P31": [
    "Q1969448"
   ],
   "P279": [
    "Q19798642",
    "Q21281405"
   ]
  },
  "revision_id": "2572672538",
  "ancestor_of": "Q938438",
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
  "ancestor_of": "Q938438",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q3249551",
  "label": "process",
  "description": "series of events which occur over an extended period of time",
  "aliases": [
   "bfo:Process",
   "prov:Activity",
   "event"
  ],
  "claims": {
   "P31": [
    "Q124711104",
    "Q142077035"
   ],
   "P279": [
    "Q67518978",
    "Q1190554",
    "Q141182775",
    "Q141257229"
   ],
   "P361": [
    "Q2377160",
    "Q133250"
   ],
   "P527": [
    "Q1190554",
    "Q529711",
    "Q27956567",
    "Q12769393"
   ],
   "P1889": [
    "Q24905",
    "Q224423",
    "Q3406372",
    "Q1914636",
    "Q46270982",
    "Q141609028",
    "Q141620495",
    "Q142215789"
   ]
  },
  "revision_id": "2572268752",
  "ancestor_of": "Q938438",
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
  "ancestor_of": "Q7604424",
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
  "ancestor_of": "Q7604424",
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
  "ancestor_of": "Q7604424",
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
  "ancestor_of": "Q7604424",
  "level": 2,
  "fetched_utc": "2026-11-20"
 }
]

WordNet senses for the concept's name and variants:
[
 {
  "synset": "oewn-06027814-n",
  "lemmas": [
   "statistics"
  ],
  "gloss": "a branch of applied mathematics concerned with the collection and interpretation of quantitative data and the use of probability theory to estimate population parameters",
  "examples": [],
  "relations": {
   "hypernym": [
    "oewn-06027371-n"
   ],
   "part_meronym": [
    "oewn-06030086-n"
   ],
   "hyponym": [
    "oewn-06040778-n",
    "oewn-06043631-n",
    "oewn-06051131-n",
    "oewn-92447150-n"
   ]
  },
  "relation_targets": {
   "oewn-06027371-n": "applied mathematics, applied math",
   "oewn-06030086-n": "statistical method, statistical procedure",
   "oewn-06040778-n": "correlation, correlational statistics",
   "oewn-06043631-n": "nonparametric statistics",
   "oewn-06051131-n": "biometrics, biometry, biostatistics",
   "oewn-92447150-n": "estimation theory"
  }
 }
]

Draft the entry for this concept. Return the JSON object only.
~~~~

## Concept 3 of 3: Mathematics (`so9zp6tzyh`)

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
[
 {
  "title": "Mathematics",
  "revision_id": "1378649367",
  "matched_by": "title",
  "text": "Mathematics is a field of knowledge concerned with abstract concepts such as numbers, geometric shapes, sets, functions, and probabilities. It uses logical reasoning and proof to study and establish their properties, often expressed as theorems, formulas, and equations. Mathematics is widely used to model and solve problems in science, engineering, technology, economics, and everyday life.\n\nThere are many areas of mathematics, including number theory (the study of integers and their properties), algebra (the study of operations and the structures they form), geometry (the study of shapes and spaces that contain them), analysis (the quantitative study of approximation and convergence), and set theory (presently used as a foundation for all mathematics).\n\nMathematics involves the description and manipulation of abstract objects that are either abstractions from nature or purely abstract entities that are stipulated to have certain properties, called axioms. Mathematics uses pure reason to prove the properties of objects through proofs, which consist of a succession of applications of deductive rules to already established results. These results, called theorems, include previously proved theorems, axioms, and—in case of abstraction from nature—some basic properties that are considered true starting points of the theory under consideration.\n\nMathematics is essential in science and engineering; it is widely used in every field of knowledge and in everyday life, as soon as data are manipulated, shapes, patterns, and structures are studied, and logical reasoning is needed. Although mathematics is widely used to model empirical phenomena, its results are established by deductive proof rather than by experiment. The relationship between mathematical truth, logic, and reality is a subject of philosophical debate. Some areas of mathematics, such as game theory, are developed in close correlation with their applications and are often grouped under applied mathematics. Other areas are developed independently from any application but often find practical applications later.\n\nMathematical written records first appeared in Ancient Egypt and Mesopotamia, but the concept of proof and its associated mathematical rigor began in ancient Greek mathematics, exemplified in Euclid's Elements. Mathematics was primarily divided into geometry and arithmetic until the 16th and 17th centuries, when algebra and infinitesimal calculus evolved into new fields. Since then, the interaction between mathematical innovations and scientific discoveries has led to a correlated increase in the development of both. At the end of the 19th century, the foundational crisis of mathematics led to the systematic use of the axiomatic method, which heralded a dramatic increase in the number of mathematical areas and their fields of application. The contemporary Mathematics Subject Classification lists more than 60 first-level areas of mathematics.\n\nAreas of mathematics\n\nBefore the Renaissance, mathematics was divided into two main areas: arithmetic, regarding the study and manipulation of numbers, and geometry, regarding the study of shapes. Some types of pseudoscience, such as numerology and astrology, were not then clearly distinguished from mathematics.\n\nBeginning with the Renaissance, two more areas became predominant. New mathematical notation led to modern algebra which, roughly speaking, begins with the study and manipulation of algebraic expressions. Calculus, consisting of the two subfields differential calculus and integral calculus, originated with geometry but evolved into the study of continuous functions, which model the typically nonlinear relationships between varying quantities, as represented by variables. This division into four main areas—arithmetic, geometry, algebra, and calculus—endured until the end of the 19th century. Other areas that were previously studied by mathematicians, such as celestial mechanics and solid mechanics, are now considered to belong to physics. The subject of combinatorics has been studied for much of recorded history, yet did not become a separate branch of mathematics until the 17th century.\n\nAt the end of the 19th century, the foundational crisis in mathematics and the systematic use of the axiomatic method led to an explosion of new areas of mathematics. The 2020 Mathematics Subject Classification contains no fewer than 63 first-level areas. Some of these areas correspond to the older division, as is true regarding number theory (the modern name for higher arithmetic) and geometry. Several other first-level areas have \"geometry\" in their names or are otherwise commonly considered part of geometry. Algebra and calculus do not appear as first-level areas but are split into several first-level areas. Other first-level areas emerged during the 20th century or had not previously been considered as mathematics, such as mathematical logic and foundations.\n\nNumber theory\n\nNumber theory evolved from the manipulation of numbers, that is, natural numbers and later expanded to integers and rational numbers Number theory was once called arithmetic, but nowadays this term is mostly used for numerical calculations. The study of numbers arguably dates back to ancient Babylon and probably China, but developed into a distinct discipline in ancient Greece. Two prominent early number theorists were Euclid and Diophantus of Alexandria. The modern study of number theory in its abstract form is largely attributed to Pierre de Fermat and Leonhard Euler. The field came to full fruition with the contributions of Adrien-Marie Legendre and Carl Friedrich Gauss.\n\nMany easily stated number problems have solutions that require sophisticated methods, often from across mathematics. A prominent example is Fermat's Last Theorem. This conjecture was stated in 1637 by Pierre de Fermat, but it was proved only in 1994 by Andrew Wiles, who used tools including scheme theory from algebraic geometry, category theory, and homological algebra. Another example is Goldbach's conjecture, which asserts that every even integer greater than 2 is the sum of two prime numbers. Stated in 1742 by Christian Goldbach, it remains unproven despite considerable effort.\n\nNumber theory includes several subareas, including analytic number theory, algebraic number theory, geometry of numbers (method oriented), Diophantine analysis, and transcendence theory (problem oriented).\n\nGeometry\n\nGeometry is one of the oldest branches of mathematics. It started with empirical recipes concerning shapes, such as lines, angles, and circles, which were developed mainly for the needs of surveying and architecture, but has since blossomed into many other subfields.\n\nA fundamental innovation was the ancient Greeks' introduction of the concept of proofs, which require that every assertion must be proved. For example, it is not sufficient to verify by measurement that, say, two lengths are equal; their equality must be proven via reasoning from previously accepted results (theorems) and a few basic statements. The basic statements are not subject to proof because they are self-evident (postulates), or are part of the definition of the subject of study (axioms). This principle, foundational for all mathematics, was first elaborated for geometry, and was systematized by Euclid around 300 BC in his book Elements.\n\nThe resulting Euclidean geometry is the study of shapes and their arrangements constructed from lines, planes and circles in the Euclidean plane (plane geometry) and the three-dimensional Euclidean space.\n\nEuclidean geometry was developed without change of methods or scope until the 17th century, when René Descartes introduced what is now called Cartesian coordinates. This constituted a major change of paradigm: Instead of defining real numbers as lengths of line segments (see number line), it allowed the representation of points using their coordinates, which are numbers. Algebra (and later, calculus) can thus be used to solve geometrical problems. Geometry was split into two new subfields: synthetic geometry, which uses purely geometrical methods, and analytic geometry, which uses coordinates systematically.\n\nAnalytic geometry allows the study of curves unrelated to circles and lines. Such curves can be defined as the graph of functions, the study of which led to differential geometry. They can also be defined as implicit equations, often polynomial equations (which spawned algebraic geometry). Analytic geometry also makes it possible to consider Euclidean spaces of higher than three dimensions.\n\nIn the 19th century, mathematicians discovered non-Euclidean geometries, which do not follow the parallel postulate. By questioning that postulate's truth, this discovery has been viewed as joining Russell's paradox in revealing the foundational crisis of mathematics. This aspect of the crisis was solved by systematizing the axiomatic method and adopting the view that the truth of the chosen axioms is not a mathematical problem. In turn, the axiomatic method allows for the study of various geometries obtained either by changing the axioms or by considering properties that do not change under specific transformations of the space.\n\nToday's subareas of geometry include:\n\nProjective geometry, introduced in the 16th century by Girard Desargues, extends Euclidean geometry by adding points at infinity at which parallel lines intersect. This simplifies many aspects of classical geometry by unifying the treatments for intersecting and parallel lines.\n\nAffine geometry, the study of properties relative to parallelism and independent of the concept of length.\n\nDifferential geometry, the study of curves, surfaces, and their generalizations, which are defined using differentiable functions.\n\nManifold theory, the study of shapes that are not necessarily embedded in a larger space.\n\nRiemannian geometry, the study of distance properties in curved spaces.\n\nAlgebraic geometry, the study of curves, surfaces, and their generalizations, which are defined using polynomials.\n\nTopology, the study of properties that are kept under continuous deformations.\n\nAlgebraic topology, the use in topology of algebraic methods, mainly homological algebra.\n\nDiscrete geometry, the study of finite configurations in geometry.\n\nConvex geometry, the study of convex sets, which takes its importance from its applications in optimization.\n\nComplex geometry, the geometry obtained by replacing real numbers with complex numbers.\n\nAlgebra\n\nAlgebra is the art of manipulating equations and formulas. Diophantus (3rd century) and al-Khwarizmi (9th century) were the two main precursors of algebra. Diophantus solved some equations involving unknown natural numbers by deducing new relations until he obtained the solution. Al-Khwarizmi introduced systematic methods for transforming equations, such as moving a term from one side of an equation to the other side. The term algebra is derived from the Arabic word al-jabr, meaning 'the reunion of broken parts', which he used for naming one of these methods in the title of his main treatise.\n\nAlgebra became an area in its own right only with François Viète (1540–1603), who introduced the use of variables for representing unknown or unspecified numbers. Variables allow mathematicians to describe the operations that have to be done on the numbers represented using mathematical formulas.\n\nUntil the 19th century, algebra consisted mainly of the study of linear equations (presently linear algebra), and polynomial equations in a single unknown, which were called algebraic equations (a term still in use, although it may be ambiguous). During the 19th century, mathematicians began to use variables to represent things other than numbers (such as matrices, modular integers, and geometric transformations), on which generalizations of arithmetic operations are often valid. The concept of algebraic structure addresses this, consisting of a set whose elements are unspecified, of operations acting on the elements of the set, and rules that these operations must follow. The scope of algebra thus grew to include the study of algebraic structures. This object of algebra was called modern algebra or abstract algebra, as established by the influence and works of Emmy Noether,\nand popularized by Van der Waerden's book Moderne Algebra.\n\nSome types of algebraic structures have useful and often fundamental properties in many areas of mathematics. Their study became autonomous parts of algebra, and it includes the following:\n\ngroup theory\n\nfield theory\n\nvector spaces, whose study is essentially the same as linear algebra\n\nring theory\n\ncommutative algebra, which is the study of commutative rings, includes the study of polynomials, and is a foundational part of algebraic geometry\n\nhomological algebra\n\nLie algebra and Lie group theory\n\nBoolean algebra, which is widely used for the study of the logical structure of computers\n\nThe study of types of algebraic structures as mathematical objects is the purpose of universal algebra and category theory. The latter applies to every mathematical structure (not only algebraic ones). At its origin, it was introduced, together with homological algebra, to allow the algebraic study of non-algebraic objects such as topological spaces; this particular area of application is called algebraic topology.\n\nCalculus and analysis\n\nCalculus, formerly called infinitesimal calculus, was introduced independently and simultaneously by 17th-century mathematicians Newton and Leibniz. It is fundamentally the study of the relationship between variables that depend continuously on each other. Calculus was expanded in the 18th century by Euler with the introduction of the concept of a function and many other results. Presently, \"calculus\" refers mainly to the elementary part of this theory, and \"analysis\" is commonly used for advanced parts.\n\nAnalysis is further subdivided into real analysis, where variables represent real numbers, and complex analysis, where variables represent complex numbers. Analysis includes many subareas shared by other areas of mathematics, which include:\n\nMultivariable calculus\n\nFunctional analysis, where variables represent varying functions\n\nIntegration, measure theory and potential theory, all strongly related with probability theory on a continuum\n\nOrdinary differential equations\n\nPartial differential equations\n\nNumerical analysis, mainly devoted to the computation of solutions of ordinary and partial differential equations that arise in many applications\n\nDiscrete mathematics\n\nDiscrete mathematics, broadly speaking, is the study of individual, countable mathematical objects. An example is the set of all integers. Because the objects of study here are discrete, the methods of calculus and mathematical analysis do not directly apply. Algorithms—especially their implementation and computational complexity—play a major role in discrete mathematics.\n\nThe four color theorem and optimal sphere packing were two major problems of discrete mathematics solved in the second half of the 20th century. The P versus NP problem, which remains open to this day, is also important for discrete mathematics, since its solution would potentially impact a large number of computationally difficult problems.\n\nDiscrete mathematics includes:\n\nCombinatorics, the art of enumerating mathematical objects that satisfy some given constraints. Originally, these objects were elements or subsets of a given set; this has been extended to various objects, which establishes a strong link between combinatorics and other parts of discrete mathematics. For example, discrete geometry includes counting configurations of geometric shapes.\n\nGraph theory and hypergraphs\n\nCoding theory, including error correcting codes and a part of cryptography\n\nMatroid theory\n\nDiscrete geometry\n\nDiscrete probability distributions\n\nGame theory (although continuous games are also studied, most common games, such as chess and poker, are discrete)\n\nDiscrete optimization, including combinatorial optimization, integer programming, constraint programming\n\nMathematical logic and set theory\n\nThe two subjects of mathematical logic and set theory have belonged to mathematics since the end of the 19th century. Before this period, sets were not considered to be mathematical objects, and logic, although used for mathematical proofs, belonged to philosophy and was not specifically studied by mathematicians.\n\nBefore Cantor's study of infinite sets, mathematicians were reluctant to consider actually infinite collections, and considered infinity to be the result of endless enumeration. Cantor's work offended many mathematicians not only by considering actually infinite sets but by showing that this implies different sizes of infinity, per Cantor's diagonal argument. This led to the controversy over Cantor's set theory. In the same period, various areas of mathematics concluded that the former intuitive definitions of the basic mathematical objects were insufficient for ensuring mathematical rigor.\n\nThis became the foundational crisis of mathematics. It was eventually solved in mainstream mathematics by systematizing the axiomatic method inside a formalized set theory. Roughly speaking, each mathematical object is defined by the set of all similar objects and the properties that these objects must have. For example, in Peano arithmetic, the natural numbers are defined by \"zero is a number\", \"each number has a unique successor\", \"each number but zero has a unique predecessor\", and some rules of reasoning. This mathematical abstraction from reality is embodied in the modern philosophy of formalism, as founded by David Hilbert around 1910.\n\nThe \"nature\" of the objects defined this way is a philosophical problem that mathematicians leave to philosophers, even if many mathematicians have opinions on this nature, and use their opinion—sometimes called \"intuition\"—to guide their study and proofs. The approach allows considering \"logics\" (that is, sets of allowed deducing rules), theorems, proofs, etc. as mathematical objects, and to prove theorems about them. For example, Gödel's incompleteness theorems assert, roughly speaking, that in every consistent formal system that contains the natural numbers, there are theorems that are true (that is, provable in a stronger system), but not provable inside the system. This approach to the foundations of mathematics was challenged during the first half of the 20th century by mathematicians led by Brouwer, who promoted intuitionistic logic (which explicitly lacks the law of excluded middle).\n\nThese problems and debates led to a wide expansion of mathematical logic, with subareas such as model theory (modeling some logical theories inside other theories), proof theory, type theory, computability theory and computational complexity theory. Although these aspects of mathematical logic were introduced before the rise of computers, their use in compiler design, formal verification, program analysis, proof assistants and other aspects of computer science contributed in turn to the expansion of these logical theories.\n\nComputational mathematics\n\nComputational mathematics is the study of mathematical problems that are typically too large for human computing capacity. \n\nPart of computational mathematics involves numerical analysis, which is devoted to computation with approximations of real numbers (floating-point arithmetic). Numerical analysis provides methods for problems in analysis using functional analysis and approximation theory. Numerical analysis broadly includes the study of approximation and discretization, with special focus on rounding errors. Numerical analysis and, more broadly, scientific computing, also study non-analytic topics of mathematical science, especially algorithmic-matrix-and-graph theory. \n\nAnother area of computational mathematics is computer algebra, which consists mainly of the manipulation of mathematical formulas on a computer.\n\nAutomated theorem proving, which includes proof assistants and proof checkers, is another area of computational mathematics that is used for formal verification and allows formal proof of difficult theorems of mathematics such as the Feit–Thompson theorem on finite groups.\n\nAlgorithmics, a large part of discrete mathematics, and public key cryptography are also often considered as a part of computational mathematics.\n\nHistory\n\nEtymology\n\nThe word mathematics comes from the Ancient Greek word máthēma (μάθημα), meaning 'something learned, knowledge, mathematics', and the derived expression mathēmatikḗ tékhnē (μαθηματικὴ τέχνη), meaning 'mathematical science'. It entered the English language during the Late Middle English period through French and Latin. \n\nTraditionally, one of the two main schools of thought in Pythagoreanism was known as the mathēmatikoi (μαθηματικοί)—which at the time meant \"learners\" rather than \"mathematicians\" in the modern sense. The Pythagoreans were likely the first to constrain the use of the word to just the study of arithmetic and geometry. By the time of Aristotle (384–322 BC), this meaning was fully established.\n\nIn Latin and English, until around 1700, the term mathematics more commonly meant \"astrology\" (or sometimes \"astronomy\") rather than \"mathematics\"; the meaning gradually changed to its present one from about 1500 to 1800. This change"
 },
 {
  "title": "Mathematics (producer)",
  "revision_id": "1371715483",
  "matched_by": "title-minus-qualifier",
  "text": "Ronald Maurice Bean, better known professionally as Mathematics (also known as Allah Mathematics) (born October 21, 1971), is a hip hop producer and DJ for the Wu-Tang Clan and its solo and affiliate projects. He designed the Wu-Tang Clan logo.\n\nBiography\n\nAs well as using rappers from Mathematics' home borough of Queens, Eyes-Low and Buddah Bless, Love Hell Or Right had appearances from all the Wu-Tang Clan members except GZA and the then-imprisoned Ol' Dirty Bastard. Mathematics soon signed to the popular independent hip hop label Nature Sounds (home to Wu-Tang colleague Masta Killa as well as MF Doom) and released his second album The Problem in 2005. On this album the entire Wu-Tang Clan appeared, including a posthumous appearance from Ol' Dirty Bastard. As well as working on his solo albums, Mathematics has continued to contribute beats to many Wu-Tang releases, including the first albums by Masta Killa and Streetlife. In January 2012 he was to release a sequel to The Problem entitled The Answer, entirely produced by him with Wu-Tang members such as Raekwon, GZA, Method Man, Cappadonna, Masta Killa, Ol' Dirty Bastard, Ghostface Killah. Other artists include Redman and artists he is developing such as Ali Vegas, Eyeslow and Bad Luck.\n\nIn August 2017, it was confirmed that Wu-Tang Clan will release a new album, Wu-Tang: The Saga Continues, which was entirely produced by Mathematics and was released on October 13, 2017. The first track off the album is titled \"People Say\" and features Redman.\n\nDiscography\n\nAlbums\n\nProduction credits\n\nAmerica Is Dying Slowly - Red Hot AIDS Benefit Series, Red Hot Organization, Smoke One Productions\n\nNFL Jams - \"Fast Life\"\n\nThe Pillage - \"Oh Donna\"\n\nWu-Tang Killa Bees: The Swarm - \"Cobra Clutch\", \"Punishment\", \"Fatal Sting\"\n\nDirty Weaponry - \"Galactics\", \"Bastard Swordsman\"\n\nSlam: The Soundtrack - \"I Can See\"\n\nTical 2000: Judgement Day - \"Snuffed Out\"\n\nWu-Syndicate - \"Pointin' Fingers\", \"Muzzle Toe\"\n\nBeneath the Surface - \"Amplified Sample\", \"High Price Small Reward\", \"Publicity\", \"Feel Like an Enemy\", \"Mic Trippin’\"\n\nUncontrolled Substance - \"Uncontrolled Substance\"\n\nBlackout! - \"Dat's Dat Shit\", \"Fire Ina Hole\"\n\nNext Friday (Original Motion Picture Soundtrack) - \"Shaolin Worldwide\"\n\nBlack Knights - \"Street War\"\n\nThe W - \"Do You Really (Thang Thang)\"\n\nSupreme Clientele - \"Mighty Healthy\", \"Wu-Banga 101\"\n\nDigital Bullet - \"Must Be Bobby\", \"Cousins\"\n\nHow High The Soundtrack - \"Who Wanna Rap\"\n\nIron Flag - \"Rules\"\n\nBulletproof Wallets - \"Theodore\", \"Strawberry\"\n\nLegend of the Liquid Sword - \"Fam (Members Only)\"\n\nTera Iz Him - \"Roll with the Rush\"\n\nBobby Digital Presents Northstar - \"Duckie\", \"We Got It\"\n\nNo Said Date - \"Last Drink\", \"Do That Dance\", \"Whatever\"\n\nStreet Education - \"FANZ\", \"Who Want to Rap?\", \"Sweetest Pain\"\n\nWu-Tang Meets the Indie Culture - \"Cars on the Interstate\"\n\n4:21... The Day After - \"Dirty Mef\", \"Everything\"\n\nI - \"Two Missed Calls\"\n\n8 Diagrams - \"Stick Me for My Riches\"\n\nPro Tools - \"Pencil\"\n\nBlackout! 2 - \"BO2 (Intro)\"\n\nOnly Built 4 Cuban Linx... Pt. II - \"Mean Streets\"\n\nPollen: The Swarm - \"Assed Out\"\n\nWu-Massacre - \"Meth vs. Chef Part II\", \"Miranda\", \"Dangerous\"\n\nHeaven Razah - \"Raised in Hell\"\n\nShaolin vs. Wu-Tang - \"Dart School\"\n\nGold Cobra - \"Middle Finger\", \"Combat Jazz\"\n\nSelling My Soul - \"Intro\", \"Part 2\", \"All Natural\", \"Wisdom\"\n\nThe Saga Continues - entire album\n\nThe Meth Lab - \"The Pledge\"', \"2 Minutes of Your Time\"\n\nSlime Wave - \"Ghost of Camay\"\n\nBlack Samson, the Bastard Swordsman - entire album\n\nReferences"
 },
 {
  "title": "Mathematics (Mos Def song)",
  "revision_id": "1296958011",
  "matched_by": "title-minus-qualifier",
  "text": "\"Mathematics\" is a b-side single from Mos Def's solo debut album, Black on Both Sides. It contains lyrics about various social issues and asks the listener to add them up and come to conclusions about them. Many references to numbers are found in this song and at times, Mos Def rhymes statistics in numerical order.\n\nBackground\n\nThe song highlights the differences between the White and African-American citizens of the US and uses the lyrics \"Do your math...\" - telling young African-Americans to 'do their maths' so they can avoid being part of the numerous degrading statistics he raps about in the opening and third verses of the song. The song is produced by DJ Premier whose famous scratch samples make up the song's bridge. Premier has called it one of his favorite beats.\n\nPremier also revealed that Scarface originally wanted the beat. He was recording his album The Last of a Dying Breed and wanted Premier to produce a song on it. However, Mos Def took the track and recorded something to it. Scarface later met up with Mos Def to tell him that he really wanted the track.\n\nSamples\n\nThe bridge of \"Mathematics\" contains DJ Premier's signature scratched vocals from various hip hop songs. The lyrics of those samples as well as information about their origin can be found below:\n\n\"The Mighty Mos Def...\" (from Mos Def's \"Body Rock\"),\n\n\"It's simple mathematics\" (from Fat Joe's \"John Blaze\"),\n\n\"Check it out\" (from \"Look Alive\" by Big C from Arista Records)\n\n\"I revolve around science...\" (Ghostface Killah's vocals from Raekwon's \"Criminology\"),\n\n\"What are we talking about here?\" (Art Seigner of Flying Dutchman Records interviewing Angela Davis),\n\n\"Do your math..\" (from Erykah Badu's \"On & On\"), and\n\n\"One, two, three, four\" (from James Brown's \"Funky Drummer\")\n\nThe instrumental from \"Baby I'm-a Want You\" by The Fatback Band is also sampled.\n\nIn popular culture\n\n\"Mathematics\" can be found on the soundtrack of Madden NFL 2002. The song is also played briefly in the CSI: Crime Scene Investigation episode \"Crate 'n' Burial\".\n\nSingle track list\n\nVinyl 12\"\n\nA-Side\n\nMs. Fat Booty (Clean)\n\nMs. Fat Booty (Dirty)\n\nMs. Fat Booty (Instrumental)\n\nMs. Fat Booty (A Capella)\n\nB-Side\n\nMathematics (Clean)\n\nMathematics (Dirty)\n\nMathematics (Instrumental)\n\nMathematics (A Capella)\n\nCD/Maxi single\n\nMs. Fat Booty (4:08)\n\nMs. Fat Booty (Instrumental) (4:06)\n\nMathematics (4:08)\n\nReferences"
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
  "qid": "Q1908348",
  "label": "Mathematics",
  "description": "rap music producer",
  "aliases": [
   "Ronald Bean",
   "Ronald M. Bean"
  ],
  "claims": {
   "P31": [
    "Q5"
   ]
  },
  "revision_id": "2563781286",
  "value_labels": {
   "Q5": "human"
  },
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q6786884",
  "label": "Mathematics",
  "description": "1999 single by Mos Def",
  "aliases": [],
  "claims": {
   "P31": [
    "Q134556"
   ]
  },
  "revision_id": "2481463734",
  "value_labels": {
   "Q134556": "single"
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
  "qid": "Q5",
  "label": "human",
  "description": "any single member of Homo sapiens, unique extant species of the genus Homo",
  "aliases": [
   "human being",
   "people",
   "nonfictional human",
   "non-fictional human",
   "individual Homo sapiens",
   "modern human",
   "person"
  ],
  "claims": {
   "P31": [
    "Q55983715"
   ],
   "P279": [
    "Q2250224",
    "Q164509",
    "Q154954",
    "Q5891007",
    "Q215627"
   ],
   "P361": [
    "Q8425",
    "Q1156970",
    "Q42762",
    "Q16334295"
   ],
   "P527": [
    "Q23852"
   ],
   "P1889": [
    "Q2472587",
    "Q95074",
    "Q215627",
    "Q114353657",
    "Q124542004"
   ]
  },
  "revision_id": "2570778784",
  "ancestor_of": "Q1908348",
  "level": 1,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q55983715",
  "label": "organisms known by a particular common name",
  "description": "organisms which have been assigned common names in addition to their taxon name",
  "aliases": [
   "organisms known by a particular vernacular name",
   "taxon known by a particular common name",
   "organism known by a particular common name"
  ],
  "claims": {
   "P31": [
    "Q19478619"
   ],
   "P279": [
    "Q21871294"
   ],
   "P1889": [
    "Q502895",
    "Q25376990",
    "Q913170"
   ]
  },
  "revision_id": "2557671777",
  "ancestor_of": "Q1908348",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q2250224",
  "label": "individual person",
  "description": "",
  "aliases": [],
  "claims": {
   "P279": [
    "Q215627",
    "Q795052",
    "Q141164427"
   ],
   "P460": [
    "Q31090402"
   ]
  },
  "revision_id": "2568776218",
  "ancestor_of": "Q1908348",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q164509",
  "label": "omnivore",
  "description": "animal capable of consuming a variety of foods, usually including both plants and animals as diet",
  "aliases": [],
  "claims": {
   "P279": [
    "Q72638",
    "Q729"
   ]
  },
  "revision_id": "2563001970",
  "ancestor_of": "Q1908348",
  "level": 2,
  "fetched_utc": "2026-11-20"
 },
 {
  "qid": "Q154954",
  "label": "natural person",
  "description": "real human being as opposed to a non-human legal person",
  "aliases": [
   "physical person",
   "natural entity"
  ],
  "claims": {
   "P31": [
    "Q2135465",
    "Q10541491",
    "Q134601860",
    "Q111360549"
   ],
   "P279": [
    "Q3778211",
    "Q5891007"
   ],
   "P460": [
    "Q215627"
   ],
   "P1889": [
    "Q155076",
    "Q7885249",
    "Q7451779",
    "Q31090402"
   ]
  },
  "revision_id": "2571112188",
  "ancestor_of": "Q1908348",
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
  "ancestor_of": "Q6786884",
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
  "ancestor_of": "Q6786884",
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
  "ancestor_of": "Q6786884",
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
  "ancestor_of": "Q6786884",
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
