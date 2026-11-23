# Contributing to the Irreducibly Human Work Lexicon

We welcome contributors from education, workforce research, software, and the trades. You do not need repository access or a large proposal to get started. One well-evidenced correction is enough.

## Pick a contribution

| If you want to… | Start here |
| --- | --- |
| Check a definition, class, or synonym | Open a [GitHub issue](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/issues/new) with the entry ID, the exact claim, and a source that supports or contradicts it. |
| Supply evidence or suggest a missing concept | Link to a source you may cite, give a page or section if possible, and explain what it shows and what it does not. A syllabus assignment can describe intended practice; it cannot establish student proficiency or employer demand. |
| Improve the paper or evaluate the method | Read the [rough manuscript](Papers/irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/manuscript.md). Flag a specific claim, test whether a result reproduces, or propose a baseline, annotation rule, or difficult example for a held-out evaluation. |
| Improve the tools or documentation | Reproduce an issue using public or synthetic inputs. Explain what should change and how to verify it. |

For manuscript contributions, please open an issue first if you plan a substantial rewrite or evaluation. The paper is a rough draft. If you hope to be an author, read [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors) first.

You can share this [copyable contributor invitation](Papers/irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/contributor-invitation-email.txt) with someone who might want to help.

## Make a focused pull request

1. Edit one entry or a small related set under `entries/`. Follow the [entry format](docs/ENTRY-FORMAT.md) and [schema and evidence rules](docs/SCHEMAS.md).
2. Explain the proposed change and link to evidence for the specific claim. Use original sources where possible. Link and paraphrase rather than copying source text or uploading a dataset.
3. If you are correcting an ambiguous or disputed match, explain the competing interpretations. A synonym must mean the same thing in the stated context. A related concept needs a separate record, not an alias. Roll-up is opt-in.
4. Keep model-drafted material provisional and disclose relevant model use. Do not mark your own work `reviewed`; independent review records the evidence and reviewer.
5. Run the checks and include the results:

   ```sh
   python3 -I tools/lexicon.py validate
   python3 -I tests/test_lexicon.py
   python3 -I tests/test_provenance.py
   python3 -I tests/test_schema.py
   ```

Do not upload private syllabi, resumes, personal records, restricted job ads, or any material whose redistribution rights are unclear. See the [source rules](docs/SOURCES.md) and [third-party notices](THIRD-PARTY-NOTICES.md).

## Credit and what we expect from authors

We follow [Yale's guidance on authorship](https://provost.yale.edu/policies/academic-integrity/guidance-authorship-scholarly-or-scientific-publications). Under it, an author has done **all four** of these:

1. **Contributed to a component of the work:** its conception, design, conduct, analysis, or interpretation of at least part of the results.
2. **Helped write the paper:** drafted part of it, or revised it for substance, not just copy edits.
3. **Approved the final version** before submission.
4. **Agreed to be accountable** for the work, including helping answer questions about its accuracy or integrity.

Some contributions are valuable but don't by themselves make someone an author: one corrected entry or one source, helping collect or assemble data, or reviewing a finished draft to offer suggestions. Everyone who contributes that way is thanked by name in the acknowledgments, unless they ask not to be. To be an author, take on a component, such as testing whether a result reproduces, building a baseline or a held-out evaluation, writing annotation rules, or reviewing a whole set of entries in your field, and then do the writing, approval and accountability steps too.

If you want to be an author, we expect you to:

- **Read the whole paper,** not just your section. You're putting your name on all of it.
- **Think about it, then give feedback.** Does the method answer the question? Are the comparisons fair? Do the figures show what the text claims, and would a different figure show it better? Do the numbers in the text match the tables, figures and entry counts?
- **Suggest changes when they matter.** Don't make a suggestion just to have made one. If you find nothing to change, say so; that's a useful answer. A real problem, raised clearly with a proposed fix, is the most valuable thing you can give.
- **Disclose AI assistance** in your writing and analysis, as the pull-request rules ask for entries. AI tools are fine for code and drafting, but say where you used them. You stay accountable for everything you contribute.
- **Keep a record of what you did:** what, when, and where it lives (issue, pull request, commit, figure). The paper's contribution statement is drawn from it and lists each author's [CRediT roles](https://credit.niso.org/).
- **Sign off only when you can stand behind it.** Before submission, every author confirms in writing that they have read the full paper, agree with it, and accept accountability for it. If something is wrong or unclear, say so before approval, not after publication.

Raise authorship early, and we'll revisit it as roles change. Author order follows contribution. If you think your work merits authorship and it isn't reflected, say so before the final draft. A GitHub contribution does not by itself settle authorship.
