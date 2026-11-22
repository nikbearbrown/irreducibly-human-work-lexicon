# Contributing to the Irreducibly Human Work Lexicon

We welcome contributors from education, workforce research, software, and the trades. You do not need repository access or a large proposal to get started. One well-evidenced correction is enough.

## Pick a contribution

| If you want to… | Start here |
| --- | --- |
| Check a definition, class, or synonym | Open a [GitHub issue](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/issues/new) with the entry ID, the exact claim, and a source that supports or contradicts it. |
| Supply evidence or suggest a missing concept | Link to a source you may cite, give a page or section if possible, and explain what it shows and what it does not. A syllabus assignment can describe intended practice; it cannot establish student proficiency or employer demand. |
| Improve the paper or evaluate the method | Read the [rough manuscript](Papers/irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/manuscript.md). Flag a specific claim, test whether a result reproduces, or propose a baseline, annotation rule, or difficult example for a held-out evaluation. |
| Improve the tools or documentation | Reproduce an issue using public or synthetic inputs. Explain what should change and how to verify it. |

For manuscript contributions, please open an issue first if you plan a substantial rewrite or evaluation. The paper is a rough draft, and a GitHub contribution does not by itself determine authorship.

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
