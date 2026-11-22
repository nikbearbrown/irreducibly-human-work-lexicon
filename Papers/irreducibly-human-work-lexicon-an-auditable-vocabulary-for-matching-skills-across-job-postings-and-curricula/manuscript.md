**Irreducibly Human Work Lexicon**

*An auditable vocabulary for matching skills across job postings and curricula*

*Rough manuscript v0.1 | 20 November 2026 | Not for submission*

**Abstract**

Job postings and course syllabi can refer to the same capability with different words, or use the same words for different concepts. A normalization system must decide which labels identify the same concept without treating every source mention as proof of a skill or its prevalence. We describe the Irreducibly Human Work Lexicon, an open vocabulary that separates stable concept identifiers, surface forms, and claim-level provenance. We audited a pinned GitHub snapshot and examined a separate syllabus-mining exercise as an example of how new evidence can enter the review process. The snapshot contained 3,754 concepts, including 1,988 in the broad skill class, and 17,229 individual assertions. Of those assertions, 1,455 (8.45%) met the repository’s backing rule; no entry had reached independently reviewed status. In the syllabus exercise, 43 available documents across 22 course topics yielded 334 page-located observations. These supported drafts for 32 concepts and supplied additional evidence for 16 existing concepts. The provisional syllabus additions were not merged. The audit establishes what the resource represents and what evidence a reviewer can inspect. It does not establish extraction accuracy, market demand, or student proficiency.

**Introduction**

A posting that asks for Postgres and a syllabus that teaches PostgreSQL can point to the same platform. A posting that asks for an Oracle certification and a syllabus that teaches relational database design are different: one requests a credential, while the other describes knowledge or practice. String matching alone does not preserve those distinctions. The ambiguity gets sharper when the same short form has different meanings in different fields, or when an emerging method has several unofficial names.

Occupational classifications offer stable reference points. O\*NET describes work and worker requirements and publishes occupational ratings [1]; ESCO supplies multilingual labels and links between occupations and skills [2]. SkillSpan provides annotated job-ad text for evaluating span extraction [3]. Zhang and colleagues evaluate linking fine-grained skill mentions to ESCO [4], while SkiLLens addresses emerging skills and their mapping to ESCO [5]. These projects establish that extraction, linking, and candidate discovery are distinct tasks, each with existing methods. The contribution examined here is narrower: how a vocabulary records and reviews the decision that a label, definition, or relation belongs to a concept, especially when evidence comes from different institutions or source types. W3C PROV-O supplies a broader model for exchanging provenance [6]. We use provenance in that general sense and do not claim PROV-O conformance.

This paper asks whether a versioned vocabulary can keep three claims separately inspectable: that a source used a label, that the label refers to a given concept, and that the concept or its classification is sufficiently supported for a downstream use. We report the implemented representation, a descriptive audit of the published inventory, and a small application to syllabus-based candidate discovery. The next empirical question is whether this representation reduces false equivalence on unseen sources compared with simpler matching. The present audit does not test that hypothesis.

**Methods**

**Concept representation**

Each concept record has a stable identifier, a preferred name, and a fine-grained kind. The lexicon derives a broader class from the kind. In particular, the broad skill class includes some named technologies, methods, and standards alongside developed capabilities; the class total therefore does not equal the number of distinct human skills. Knowledge, abilities, languages, and credentials are separate broad classes. An abbreviation can be stored as a variant with a case or context condition. A relation such as broader, part of, related, or contrast connects two concepts without declaring their labels interchangeable. Whether mentions of a narrower concept also count toward a broader one is an explicit choice.

A concept can contain several assertions, including its definition, kind, variants, and relations. The data model records drafting, checks, and source matches for particular assertions rather than assigning a blanket credibility label to the whole entry. For this audit, a claim was counted as backed if it had a supporting human check or a supporting source match verified by reading the source or checking the pinned dump. Agreement among models and a search-result snippet did not meet that rule. A reviewed entry is a stricter status requiring named review, backing for its claims, and no unresolved contradiction under the repository’s rules. These are operational rules of the resource and not independent estimates of factual accuracy.

**Repository audit**

The unit of inventory was the canonical JSON record at commit 0ed105b51e7f2a1837f51c4379afa50c27e00aed. The repository’s summary script [7] was used to count records by class and status and to count distinct claims and qualifying backing. The primary denominator for backing was the number of individual claims in that commit. We did not combine this denominator with counts from other branches or candidate queues. Occupational ratings in the O\*NET-derived tables were counted separately from concept records and claim evidence. An occupation’s level rating is neither an assessment of an individual nor a count of job ads.

**Syllabus case study**

The second unit of analysis was a page-located syllabus observation. The collection covered a 22-topic Northeastern Software Engineering and Information Systems portfolio from spring and fall 2026. Public archive records were reconciled with the Dynamic Schedule [8]; artifacts with conflicting or missing identifiers were kept provisional or excluded from section-specific assertions. Five PDF links were unavailable, and no course practice was inferred from those sections.

The review distinguished material named in an outline from planned practice such as a lab, assignment, project, or explicit performance objective. For each observation, the model-assisted process paraphrased the basis, recorded the archive term and section reference and PDF page, and screened labels against the main inventory and relevant candidate queues. An observation could support a proposed entry, add evidence about an existing concept, or remain in the review queue. Repeated copies of a syllabus were not treated as independent corroboration. The exercise was a model-assisted descriptive pass, with no blinded annotation study and no estimate of missed skills or agreement.

**Results**

**Inventory and evidence backing**

| **Broad class**                          | **Canonical concepts** |
| ---------------------------------------- | ---------------------- |
| Skill including technologies and methods | 1,988                  |
| Credentials                              | 859                    |
| Knowledge                                | 550                    |
| Languages                                | 290                    |
| Abilities                                | 67                     |
| **Total**                                | **3,754**              |

Table 1. Canonical concepts at the pinned repository snapshot. These are inventory counts, not measures of demand or competence.

The repository recorded 3,555 entries as machine-drafted and 199 as proposed; none was marked reviewed. The 1,455 backed assertions represented 8.45% of 17,229 claims. The reported source-backed total comprised 238 O\*NET assertions and 1,217 Wikipedia-derived descriptions. A source-backed description did not change the review status of its entry or establish the correctness of its other assertions. The O\*NET integration retained occupational level tables for 52 abilities, 35 skills, and 33 knowledge areas, each covering the same 894 occupations with ratings in the repository export. The two concepts named Mathematics show why a shared surface form should not erase the distinction between a skill in applying mathematics and knowledge of mathematics.

**Syllabus candidate discovery**

The collection yielded 334 observations from 38 archive records across all 22 topics. Of those, 60 were linked to the 32 proposed entries; a further 36 linked to 16 existing entries. The remaining 238 observations were retained for triage. Observations, source records, and concepts are different units, so these totals should not be read as coverage or prevalence rates.

The exercise produced examples at different levels of specificity. A planned lab on bounding a tool-calling loop supported a proposed AI agent loop design entry. A GraphRAG project supplied candidate evidence for graph-based retrieval as a method rather than a synonym for all retrieval-augmented generation. Prompt engineering and Slurm-related practice pointed to existing concept records and did not require new entries. The archive associates a prompt engineering document with a Fall section, but the document does not print its term or section identifier. Its human approval gate and Model Context Protocol exercises supply course-level evidence, not confirmed evidence for that particular section. The 32 drafts and the observations did not change the published main inventory.

**Discussion**

The audit shows why provenance has to attach to individual assertions. An instructor’s assignment can show that a capability was intended to be practiced. It cannot, on its own, show that an employer asks for it, that someone acquired it, or that a proposed label is equivalent to one already in the lexicon. Likewise, a model’s proposed definition is useful review material but cannot stand in for independent validation. A system that preserves these boundaries can show where a reviewer has enough evidence to act and where a decision should remain pending.

Narrower concepts should enter the vocabulary only when they help answer a concrete question. Graph-based retrieval can matter to curriculum comparison even if a broad inventory groups it under retrieval-augmented generation. Counting both as independent observations would inflate totals. The current design keeps specific claims and broader relations available without making that roll-up automatic. It also leaves room for disagreement about how much specificity to retain.

The Service Orientation record illustrates a concrete failure: its O\*NET-linked classification concerns helping other people, but its attributed reference description concerns software architecture [9]. The description satisfies the automated backing rule because the source match was recorded; it is still wrong for this sense. Backing coverage is an audit measure, not an accuracy measure. The source record lets a reviewer locate this error. It does not prevent it.

The inventory was assembled from heterogeneous inputs and is not representative of the labor market. Automated matches can conflate nearby senses, derived sources can repeat a claim, and a course archive can contain stale or mislabeled documents. The syllabus case is from one institutional portfolio and cannot be generalized to other institutions or programs. No job-to-course matching accuracy, reduction in false positives, adoption, or benefit to users was measured. The repository is suitable for inspecting evidence and planning evaluations, not yet for reporting authoritative skill counts or judging individual candidates.

**Planned Evaluation**

The next study will test whether concept identifiers with explicit ambiguity and provenance controls reduce false equivalence at useful coverage. The primary evaluation unit will be the observed span in context, with canonical concept and relation annotations when they are justified. A second evaluation will ask whether reviewers can independently retrieve and verify the evidence offered for a claim. Sampling should include postings and syllabi, abbreviations, near-neighbor concepts, emerging technology labels, and deliberate negative examples. Separate related source families across train and test partitions to avoid treating duplicates as new evidence.

Compare normalized exact matching, alias-and-context matching, and a policy that can abstain when evidence is insufficient. Use two independent annotators with adjudication and permit an ambiguous or insufficient-evidence outcome. Report link precision and recall, false-equivalence rates, agreement before adjudication, and a coverage-versus-error curve. Report source-specific and pooled results; use uncertainty intervals that respect document or source-family clustering. Define the adjudication policy, the primary comparison, and the performance tradeoff before looking at the test outcomes. No results for this evaluation are claimed here.

**Conclusion**

The Irreducibly Human Work Lexicon provides a versioned vocabulary and a record of why particular assertions were proposed or supported. The audit identifies a sizeable review queue and shows how syllabi can expand it without being mistaken for evidence of skill attainment or employer demand. The next step is a held-out evaluation that tests whether these distinctions improve decisions about concept identity.

**Data and Reproducibility**

The public repository, audited commit, and inventory script are listed in the references. Recount the public snapshot in a clean checkout using python3 -I scripts/summary_stats.py rather than combining it with candidate branches or a working tree. The syllabus analysis was prepared separately as a patch and an observation table. Its source pointers and page locators support inspection; no syllabus PDFs are redistributed with this manuscript. Confirm the provenance and reuse terms for any additional materials before releasing the study supplement. O\*NET 30.2 data are credited to the U.S. Department of Labor, Employment and Training Administration, and distributed under CC BY 4.0 where applicable. The lexicon transforms those data into vocabulary entries and occupational tables; the transformed outputs are not an official O\*NET release.

**References**

[1] National Center for O\*NET Development. O\*NET Database 30.2: Content Model Reference. U.S. Department of Labor, Employment and Training Administration. [Source](https://www.onetcenter.org/dictionary/30.2/excel/content_model_reference.html)

[2] European Commission. ESCO v1.2.1: Skills and competences. [Source](https://esco.ec.europa.eu/en/classification/skills)

[3] Zhang, M., Jensen, K., Sonniks, S., and Plank, B. 2022. SkillSpan: Hard and Soft Skill Extraction from English Job Postings. Proceedings of NAACL-HLT, 4962–4984. [Source](https://doi.org/10.18653/v1/2022.naacl-main.366)

[4] Zhang, M., van der Goot, R., and Plank, B. 2024. Entity Linking in the Job Market Domain. Findings of ACL: EACL, 410–419. [Source](https://doi.org/10.18653/v1/2024.findings-eacl.28)

[5] De Santo, A., Malandri, L., Mercorio, F., Mezzanzanica, M., and Nobani, N. 2026. SkiLLens: Recognising and Mapping Novel Skills from Millions of Job Ads Across Europe Using Language Models. EACL Industry Track, 877–885. [Source](https://doi.org/10.18653/v1/2026.eacl-industry.65)

[6] Lebo, T., Sahoo, S., and McGuinness, D., eds. 2013. PROV-O: The PROV Ontology. W3C Recommendation, 30 April. [Source](https://www.w3.org/TR/2013/REC-prov-o-20130430/)

[7] Irreducibly Human Work Lexicon (formerly Skills Lexicon). Repository snapshot 0ed105b51e7f2a1837f51c4379afa50c27e00aed and inventory recount script. [Source](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/blob/0ed105b51e7f2a1837f51c4379afa50c27e00aed/scripts/summary_stats.py)

[8] Northeastern University. Public Dynamic Schedule and Newton syllabus archive, Spring and Fall 2026. [Source](https://bnrordsp.neu.edu/ssb-prod/NEUCLSS.p_disp_dyn_sched)

[9] Irreducibly Human Work Lexicon (formerly Skills Lexicon). Service Orientation concept record, pinned repository snapshot. [Source](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/blob/0ed105b51e7f2a1837f51c4379afa50c27e00aed/entries/service-orientation.json)

**Notes for the Next Revision**

Freeze the syllabus observation table and attach a release identifier if it is cleared for public reuse. Confirm authorship and the contribution statement, funding, competing interests, and any ethics review or exemption questions before submission. Treat the document-only audit as the completed study. If the held-out evaluation is run, report its annotation protocol, exclusions, baseline results, and uncertainty before revising the abstract or making performance claims.
