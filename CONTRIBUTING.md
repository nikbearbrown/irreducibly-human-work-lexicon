# Contributing to the Irreducibly Human Work Lexicon

We welcome contributors from education, workforce research, software, and the trades. You do not need repository access or a large proposal to get started. One well-evidenced correction is enough.

## Getting started

Follow these steps in order. Steps 1 to 3 get you access. Steps 4 to 9 take one contribution from start to finish.

1. **Read first.** Read the [README](README.md), then the [rough manuscript](Papers/irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/manuscript.md). Allow about an hour. You don't need to follow every detail, but you should know what the paper claims and what it does not.
2. **Choose one thing to do.** Pick one row from the table under [Pick a contribution](#pick-a-contribution), and narrow it to one section, one source, one case or one result. If you can't decide, review one section of the rough manuscript.
3. **Email Nik** at bear@bearbrown.co with the subject "Irreducibly Human Work Lexicon: contributor". Include:
   - your name and your GitHub username;
   - the contribution you chose and what exactly you will look at;
   - whether you hope to become an author or want to help without authorship.

   Nik will add you to the repository as a collaborator. GitHub then emails you an invitation, which you must accept within seven days.
4. **Claim the work.** Check the [open issues](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/issues) to make sure nobody is already doing it. Then [open an issue](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/issues/new) that says what you are taking on, and assign it to yourself.
5. **Make a branch.** Clone the repository and create a branch named `your-name/short-description`, for example `priya/postgres-synonyms`. Do not commit to `main`. If you don't use git, edit the file on GitHub with the pencil button and choose "Create a new branch" when you save.
6. **Do the work.** Follow what the table asks you to send for the row you chose. Keep one branch to one piece of work.
7. **Open a pull request.** Say what you changed, how you checked it, and where you used an AI tool. Write "Closes #" and your issue's number so the two are linked, and request a review from `nikbearbrown`.
8. **Respond to the review.** Nik or another author will comment. Revise on the same branch until it is agreed, and it will be merged.
9. **Present your work.** Come to Nik's Tuesday meeting or his office hours with a short, clear presentation of what you have done. Cover what you set out to do, what you did, what you found and the evidence for it, and what you will do next or need help with. Do this each time you attend, even when the work is unfinished. Nik will send the meeting details when he adds you.
10. **Keep your record.** Your issues and pull requests are the record of what you did. If you hope to be an author, keep a list of them, because the paper's contribution statement is drawn from it.
11. **Take the next step.** Pick another piece of work. If you want to be an author, tell Nik early and read [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors).

You can also help without access. Anyone can open an issue on this repository without emailing first.

## Pick a contribution

| If you want to… | Start here |
| --- | --- |
| Check a definition, class, or synonym | Open a [GitHub issue](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/issues/new) with the entry ID, the exact claim, and a source that supports or contradicts it. |
| Supply evidence or suggest a missing concept | Link to a source you may cite, give a page or section if possible, and explain what it shows and what it does not. A syllabus assignment can describe intended practice; it cannot establish student proficiency or employer demand. |
| Improve the paper or evaluate the method | Read the [rough manuscript](Papers/irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/manuscript.md). Flag a specific claim, test whether a result reproduces, or propose a baseline, annotation rule, or difficult example for a held-out evaluation. |
| Improve the tools or documentation | Reproduce an issue using public or synthetic inputs. Explain what should change and how to verify it. |
| Recommend a journal Northeastern covers in full | Follow [Recommend a journal](#recommend-a-journal-northeastern-covers-in-full), below. Every contributor does this once. |

For manuscript contributions, please open an issue first if you plan a substantial rewrite or evaluation. The paper is a rough draft. If you hope to be an author, read [Credit and what we expect from authors](#credit-and-what-we-expect-from-authors) first.

You can share this [copyable contributor invitation](Papers/irreducibly-human-work-lexicon-an-auditable-vocabulary-for-matching-skills-across-job-postings-and-curricula/contributor-invitation-email.txt) with someone who might want to help.

## Recommend a journal Northeastern covers in full

Every contributor is asked to do this once. Northeastern's library has agreements with publishers that pay the open-access publishing fee for its authors. The library's page says the agreements are "open to all current Northeastern faculty, students and staff who are corresponding authors." Nik is the corresponding author on this paper, so they apply. Your job is to find a journal that is a good fit for this paper and whose fee is covered in full.

1. **Know the paper.** Read the abstract and the draft, or the plan if there is no draft yet. Note the field, the method, the kind of article (research, review, tool, dataset) and its likely length.
2. **Open the library's list.** Read [Open access publishing at Northeastern](https://library.northeastern.edu/resource_discovery/open-access-publishing/) and use its journal search, [SciFree for Northeastern](https://search.scifree.se/northeastern).
3. **Keep only full coverage.** Some agreements pay 100% of the fee and some only give a discount. A discount does not count. Some publishers also cap the number of articles they cover in a year, so note any cap the page states.
4. **Shortlist three journals** and check each one on the publisher's own site:
   - **Scope:** does the journal's aims and scope cover this paper's question and method?
   - **Article type:** does the journal accept this kind of article, and does the agreement cover that type?
   - **Precedent:** two or three recent papers in the journal that are close to this one, with links.
   - **Preprints and public drafts:** this paper's draft is in a public repository. Does the journal allow that, and is its review double-blind?
   - **Practical limits:** length limit, typical time to a first decision, and any data or code requirements.
5. **Recommend one journal and a runner-up.** [Open an issue](https://github.com/nikbearbrown/irreducibly-human-work-lexicon/issues/new) titled "Venue recommendation: " and the journal's name. Give your reasons, the links you used and the date you checked each fact.

Confirm coverage on the library's page or the publisher's page yourself. Do not rely on memory or on an AI tool's answer, because the agreements and their caps change.

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
