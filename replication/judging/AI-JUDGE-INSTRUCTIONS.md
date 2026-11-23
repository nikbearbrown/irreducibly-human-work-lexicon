# Instructions for AI judges

**For:** Codex (OpenAI); Claude Code running Claude Fable, Sonnet or Opus; Grok; and any later model asked to judge. **Not for:** an agent running a human judge's session. That agent follows [INTERVIEWER-PROTOCOL.md](INTERVIEWER-PROTOCOL.md).

You are one judge on a panel. Each item shows you two (or more) anonymous entries for the same work concept, written independently by different language models. You decide how far they **mean** the same thing. You do not decide which one is right. The study is described in [../AGREEMENT-METHOD.md](../AGREEMENT-METHOD.md). Read sections 4.1 to 4.4 there once before your first batch.

All judging runs through the subscription plan in your harness. Never call a paid API.

## 0. Get the branch

```bash
git fetch origin && git switch -c judging/<judge_id> origin/grok-agreement-method   # or: git switch judging/<judge_id>
```

`RUN_DIR` is the run folder you were given, for example `replication/agreement/pilot-test`.

## 1. Register (once per judge)

**For `pilot-test` you are already registered.** The judges are `codex`, `claude-fable`, `claude-opus`, `claude-sonnet` and `grok-bot`, and your packets are waiting in `RUN_DIR/packets/<judge_id>/`. Skip to 1.1. Registration needs the private key file, so only the operator can register a new model judge, with this command:

```bash
python3 replication/scripts/agreement.py register RUN_DIR --type model \
  --judge-id <codex | claude-fable | claude-sonnet | claude-opus | grok-bot | ...> \
  --harness <codex | claude-code | ...> --model "<the exact model id your harness reports>" \
  --drafted "<comma-separated editions you drafted, or empty>"
```

- `--model` is the model id your harness itself reports, for example from `/model` or your session information, copied exactly. Never guess it, and never leave it to a default.
- Registration writes your work to `RUN_DIR/packets/<judge_id>/batch-NNNN.jsonl` and records you in `RUN_DIR/judges.json`.

### 1.1 First session: record your model (a script command, never a hand edit)

```bash
python3 replication/scripts/agreement.py confirm-model RUN_DIR --judge-id <judge_id> \
  --model "<the exact model id your harness reports>" --harness-version "<codex --version | claude --version>"
```

- This writes `RUN_DIR/results/<judge_id>/judge.json`. Every later header line and result line must carry the same `model_reported`, and the validator checks it.
- Before you run it, make sure the judge id fits you. Claude Sonnet uses `claude-sonnet`, Claude Opus uses `claude-opus`, and so on. If the id you were given doesn't match the model you are, stop and say so.
- If the command says a different model is already recorded, stop and tell the operator. Don't use `--force`.

## 2. Self-exclusion (mandatory)

**You never judge an item that involves an edition you drafted.**

- Grok drafted the `grok` edition. Register Grok with `--drafted grok`.
- Claude Sonnet 5.5 drafted the `claude-sonnet-5-5` edition. Most of the reference lexicon (`reference`) was also written by Sonnet 5.5. If your harness reports Sonnet 5.5, register with `--drafted sonnet,reference`.
- Claude Fable and Claude Opus did not draft an edition. They register with no `--drafted`. They come from the same family as a drafter, so the analysis checks them for self-preference (AGREEMENT-METHOD.md 4.4). That is not your job: just judge blind.
- A future model that drafts an edition adds that edition's name to `--drafted`.
- Registration removes every item whose hidden key includes an edition you drafted, so your packets contain only items you may judge. If you ever recognise your own writing in an item anyway, label it `UNSURE`, put `"self_recognised": true` in `fields`, and move on.
- Self-judgment probe: Bear may run a drafter on its own edition's items **as a separate probe**, under a separate judge id (for example `claude-sonnet-selfprobe`), to measure self-preference directly. Probe results are never part of the panel label.

## 3. Read a packet

Each line of `packets/<judge_id>/batch-NNNN.jsonl` holds:

```json
{"request_id": "r-…", "stage": "P2", "concept_id": "…", "prompt_version": "agree-v1", "prompt_sha256": "…",
 "system": "<the judge system prompt>", "user": "<this item's question>"}
```

- Treat `system` as your instructions and `user` as the item. Answer the `user` text as `system` directs.
- Answer **each line on its own**. Don't look back at earlier lines or compare items with each other, and keep no running tallies.
- Open **only your own** `packets/<judge_id>/` and `results/<judge_id>/`. Don't open `requests/`, other judges' packets or `judges.json` beyond your own entry: comparing what other judges were given can reveal which editions an item pairs.
- Do not open `keys/`, `data/lexicon-parallel/`, the `grok-lexicon-parallel-data` branch, any edition repository, another judge's `results/` or `judging/*` branch, or the drafts. (The key file is not in this repository at all.) Do not search the web. Use only the item and your general knowledge of the concept.
- **One fresh session per batch.** When a batch is finished, end the session.

**`pilot-test` has stage P2 (definition pairs) only:** 144 requests. `codex`, `claude-fable` and `claude-opus` each get 3 batches (50 + 50 + 44). `claude-sonnet` gets 1 batch of 13 and `grok-bot` 1 batch of 35, because self-exclusion removes the rest. The P1 and P3–P6 prompts exist (`prompts/`), but the script doesn't generate those requests yet.

## 4. The judging prompt and rubric (exact)

The system prompt (also in `prompts/system.txt`, and already inside every request):

```
You compare entries from a dictionary of work concepts (skills, tools, knowledge areas, abilities,
languages, credentials) as they appear in job postings and course syllabi. Several anonymous drafters
wrote entries for the same concept independently. You judge whether they MEAN the same thing, not
whether they use the same words. Wording, length, order and style do not matter. A longer or more
fluent text is not better. Do not decide which drafter is right; decide only how their meanings relate.
Use only the texts shown and general knowledge of the concept. Return only the JSON object asked for.
```

The labels for each stage:

| Stage | Question | Labels |
|---|---|---|
| P1 | Group sense statements by referent | `fields.groups` (for example `[["S1","S3"],["S2"]]`), plus `majority_reading`, `ambiguous_name`; label `GROUPS` |
| P2 | Two definitions | `EQUIVALENT`, `A_NARROWER`, `B_NARROWER`, `OVERLAPPING`, `CONFLICTING`, `DIFFERENT_SENSE` |
| P3 | Group variants or relation targets that name the same concept | `fields.groups`; label `GROUPS` |
| P4 | Relation types on one aligned target | `SAME_TYPE`, `COMPATIBLE_TYPE`, `REVERSED`, `CONFLICTING_TYPE` |
| P5 | Conditions on one aligned variant | `SAME_CONDITION`, `COMPATIBLE_CONDITION`, `CONFLICTING_CONDITION` |
| P6 | Two different links | `COMPATIBLE`, `CONFLICTING` |
| any | You cannot tell | `UNSURE` (counted as missing; use it honestly, not to avoid hard items) |

P2 definitions:

- **EQUIVALENT:** same sense, same kind of thing, same essential features; either could replace the other.
- **A_NARROWER** or **B_NARROWER:** same sense, but one's scope lies strictly inside the other's.
- **OVERLAPPING:** same sense, different emphasis; neither contains the other and nothing contradicts.
- **CONFLICTING:** same sense, but a factual claim in one contradicts the other (what it is a kind of, who issues it, what it covers, what it is used for).
- **DIFFERENT_SENSE:** they describe different things (for example service orientation as a software paradigm against service orientation as a customer-service attitude).

The P2 sub-fields go in `fields`: `same_sense`, `genus_a`, `genus_b`, `conflicts` (a list of `{a, b}` spans), `confidence` (1–5) and `rationale` (40 words at most).

Hard cases: two short texts that differ only in length or style are `EQUIVALENT`. "Java" against "JavaScript" is `DIFFERENT_SENSE`, never overlapping. If one definition adds a claim the other simply leaves out, that is `NARROWER` (or `OVERLAPPING`), not `CONFLICTING`. `CONFLICTING` needs a real contradiction.

## 5. Write your results

For `packets/<judge_id>/batch-0007.jsonl`, write `results/<judge_id>/P2/batch-0007.jsonl` (using the request's stage). Start with **one header line**:

```json
{"_batch": "batch-0007", "judge_id": "codex", "harness": "codex", "harness_version": "<codex --version>",
 "model_reported": "<exactly as registered>", "effort": "<reasoning effort or null>", "plan": "<plan name>",
 "started_at": "2026-12-01T10:00:00-05:00"}
```

Then write one line per request, in packet order, following [judgment.schema.json](judgment.schema.json):

```json
{"judgment_id": "codex-r-0a1b2c3d4e5f-0", "request_id": "r-0a1b2c3d4e5f", "stage": "P2", "concept_id": "sh6x1wmacn",
 "field": "definition", "judge": {"id": "codex", "type": "model", "harness": "codex", "model_reported": "…", "judge_version": 1},
 "run_index": 0, "order_seed": null, "prompt_version": "agree-v1", "prompt_sha256": "<copied from the request>",
 "label": "A_NARROWER", "fields": {"same_sense": true, "genus_a": "relational database system",
 "genus_b": "database software", "conflicts": [], "confidence": 4, "rationale": "…"},
 "notes": null, "confirmed": null, "valid": true, "attempts": 1, "raw_sha256": null,
 "created_at": "2026-12-01T10:03:00-05:00"}
```

- Copy `request_id`, `stage`, `concept_id` and `prompt_sha256` from the request. `run_index` is 0 for the first run and 1 or 2 for repeat runs (the operator tells you which).
- `judgment_id` is `<judge_id>-<request_id>-<run_index>`. `judge.model_reported` is the same value you recorded in 1.1.
- End the file with the header line again, adding `"finished_at"`. The validator rejects a batch without it, and it also rejects a batch that leaves any packet request unanswered.
- If a reply doesn't fit the schema, fix it once. If it still doesn't fit, write `"label": "UNSURE", "valid": false`.

## 6. Validate

```bash
python3 replication/scripts/agreement.py validate RUN_DIR --judge-id <judge_id>
```

Fix every error it reports. The common errors: a label not allowed for that stage, a `request_id` that isn't in your packets, a duplicate, or a `model_reported` that differs from your registration. **A batch that fails validation is not handed in.** If your reported model changed since you registered, stop and tell the operator. Don't edit the registration yourself.

## 7. Commit and push

```bash
git switch judging/<judge_id>        # the branch from step 0
git add RUN_DIR/results/<judge_id>/   # your batches plus judge.json
git commit -m "Judge <judge_id>: batch NNNN (<stage>), validated"
git push -u origin judging/<judge_id>
```

- Stage only your own `results/<judge_id>/`. Never stage `keys/`, packets or anyone else's files.
- Commit as the operator unless told otherwise: `git -c user.name=nikbearbrown -c user.email=610338+nikbearbrown@users.noreply.github.com commit ...`. Never push to `main`, never force-push, and never open or merge a pull request.

## 8. Rate limits and resuming

If your plan's usage limit stops you mid-batch, keep what you have written. Then, in the next session, **start the batch again from its first line** in a fresh file. A half-finished batch must not be handed in. `manifest.json` (or the operator) tracks which batches are done.
