# Instructions for AI judges

**For:** Codex (OpenAI); Claude Code running Claude Fable, Sonnet or Opus; Grok; and any later model asked to judge. **Not for:** an agent running a human judge's session. That agent follows [INTERVIEWER-PROTOCOL.md](INTERVIEWER-PROTOCOL.md).

You are one judge on a panel. Each item shows you two (or more) anonymous entries for the same work concept, written independently by different language models. You decide how far they **mean** the same thing. You do not decide which one is right. The study is described in [../AGREEMENT-METHOD.md](../AGREEMENT-METHOD.md). Read sections 4.1 to 4.4 there once before your first batch.

All judging runs through the subscription plan in your harness. Never call a paid API.

## 0. Slots and versioned judge ids

Two names matter:

- **Slot:** the seat you fill on the panel, which also names your packet folder. The `pilot-test` slots are `codex`, `claude-fable`, `claude-opus`, `claude-sonnet` and `grok-bot`.
- **Judge id:** who you are, **including your exact model version**: `<provider>-<model name>-<version>`, for example `anthropic-claude-fable-5-2` or `openai-codex-5-3`. Results, branch and commits all use the judge id. The script builds it for you (1.1), and you never type it by hand.

**The version is required.** Take it from your harness or system information (for example `/model`, `/status`, or the model line in your session information), exactly as stated. **Never guess or infer it.** If you cannot see your exact version, say so with `--version-unknown`. Your judge id then ends in `-version-unknown`, and your results are **flagged**: reported separately and kept out of the primary panel until the operator confirms the version.

## 1. Register (operator only)

**For `pilot-test`, every slot is already registered.** Your packets are waiting in `RUN_DIR/packets/<slot>/`, so skip to 1.1. Registering a new slot needs the private key file, so only the operator does it:

```bash
python3 replication/scripts/agreement.py register RUN_DIR --type model --judge-id <slot> \
  --harness <codex | claude-code | ...> --drafted "<editions this model drafted, or empty>" --keys <PRIVATE>/keys/anon.jsonl
```

### 1.1 First session: record your model and version, then switch to your branch

`RUN_DIR` is the run folder you were given, for example `replication/agreement/pilot-test`.

```bash
git fetch origin && git switch --detach origin/grok-agreement-method
python3 replication/scripts/agreement.py confirm-model RUN_DIR --slot <slot> \
  --provider <openai | anthropic | xai | ...> --model-name "<model name, e.g. claude-fable>" \
  --version "<exact version, e.g. 5.2>" \
  --model-reported "<the model string exactly as your harness shows it>" \
  --harness-version "<codex --version | claude --version>"
# if you cannot see your exact version, replace  --version "..."  with  --version-unknown  (never guess)
# it prints:  judge id: anthropic-claude-fable-5-2   (and the branch name)
git switch judging/<judge_id> 2>/dev/null || git switch -c judging/<judge_id>
```

- `confirm-model` writes `RUN_DIR/results/<judge_id>/judge.json`. Every header line and result line must then carry the same `provider`, `model_name`, `model_version` and `model_reported`, and the validator checks this.
- **Later sessions:** run the same `confirm-model` command again. With the same model and version, it prints the same judge id and changes nothing. Then switch to that existing branch, `git switch judging/<judge_id>` (after `git fetch origin`, if the branch is only on the remote).
- If it says a different model or version is already recorded, you are a different judge. Stop and tell the operator. Don't use `--force`.
- Make sure the slot fits you. Claude Sonnet takes `claude-sonnet`, Claude Opus `claude-opus`, Codex `codex`, and so on. If the slot you were given doesn't match the model you are, stop and say so.

## 2. Self-exclusion (mandatory)

**You never judge an item that involves an edition you drafted.**

- Grok drafted the `grok` edition. Register Grok with `--drafted grok`.
- Claude Sonnet 5.5 drafted the `claude-sonnet-5-5` edition. Most of the reference lexicon (`reference`) was also written by Sonnet 5.5. The `claude-sonnet` slot is registered with `--drafted sonnet,reference`, on the assumption that the judge is Sonnet 5.5. If your version is not 5.5, say so in your report: the operator may re-register the slot with more items.
- Claude Fable and Claude Opus did not draft an edition. They register with no `--drafted`. They come from the same family as a drafter, so the analysis checks them for self-preference (AGREEMENT-METHOD.md 4.4). That is not your job: just judge blind.
- A future model that drafts an edition adds that edition's name to `--drafted`.
- Registration removes every item whose hidden key includes an edition you drafted, so your packets contain only items you may judge. If you ever recognise your own writing in an item anyway, label it `UNSURE`, put `"self_recognised": true` in `fields`, and move on.
- Self-judgment probe: Bear may run a drafter on its own edition's items **as a separate probe**, in a separate slot (for example `claude-sonnet-selfprobe`), to measure self-preference directly. Probe results are never part of the panel label.

## 3. Read a packet

Each line of `packets/<slot>/batch-NNNN.jsonl` holds:

```json
{"request_id": "r-…", "stage": "P2", "concept_id": "…", "prompt_version": "agree-v1", "prompt_sha256": "…",
 "system": "<the judge system prompt>", "user": "<this item's question>"}
```

- Treat `system` as your instructions and `user` as the item. Answer the `user` text as `system` directs.
- Answer **each line on its own**. Don't look back at earlier lines or compare items with each other, and keep no running tallies.
- Open **only your own** `packets/<slot>/` and `results/<judge_id>/`. Don't open `requests/`, other judges' packets or `judges.json` beyond your own entry: comparing what other judges were given can reveal which editions an item pairs.
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

For `packets/<slot>/batch-0007.jsonl`, write `results/<judge_id>/P2/batch-0007.jsonl` (using the request's stage). Start with **one header line**:

```json
{"_batch": "batch-0007", "judge_id": "anthropic-claude-fable-5-2", "provider": "anthropic", "model_name": "claude-fable",
 "model_version": "5.2", "model_reported": "<exactly as in judge.json>", "harness": "claude-code",
 "harness_version": "<claude --version>", "effort": "<reasoning effort or null>", "plan": "<plan name>",
 "started_at": "2026-12-01T10:00:00-05:00"}
```

Then write one line per request, in packet order, following [judgment.schema.json](judgment.schema.json):

```json
{"judgment_id": "anthropic-claude-fable-5-2-r-0a1b2c3d4e5f-0", "request_id": "r-0a1b2c3d4e5f", "stage": "P2", "concept_id": "sh6x1wmacn",
 "field": "definition", "judge": {"id": "anthropic-claude-fable-5-2", "type": "model", "provider": "anthropic",
 "model_name": "claude-fable", "model_version": "5.2", "model_reported": "…", "harness": "claude-code", "judge_version": 1},
 "run_index": 0, "order_seed": null, "prompt_version": "agree-v1", "prompt_sha256": "<copied from the request>",
 "label": "A_NARROWER", "fields": {"same_sense": true, "genus_a": "relational database system",
 "genus_b": "database software", "conflicts": [], "confidence": 4, "rationale": "…"},
 "notes": null, "confirmed": null, "valid": true, "attempts": 1, "raw_sha256": null,
 "created_at": "2026-12-01T10:03:00-05:00"}
```

- Copy `request_id`, `stage`, `concept_id` and `prompt_sha256` from the request. `run_index` is 0 for the first run and 1 or 2 for repeat runs (the operator tells you which).
- `judgment_id` is `<judge_id>-<request_id>-<run_index>`. `judge.provider`, `model_name`, `model_version` (null only if you recorded `--version-unknown`) and `model_reported` are copied from `results/<judge_id>/judge.json`.
- End the file with the header line again, adding `"finished_at"`. The validator rejects a batch without it, and it also rejects a batch that leaves any packet request unanswered.
- If a reply doesn't fit the schema, fix it once. If it still doesn't fit, write `"label": "UNSURE", "valid": false`.

## 6. Validate

```bash
python3 replication/scripts/agreement.py validate RUN_DIR --judge-id <judge_id>
```

Fix every error it reports. The common errors: a label not allowed for that stage, a `request_id` that isn't in your packets, a duplicate, or a provider, model name, version or `model_reported` that differs from `judge.json`. A `WARNING FLAGGED` line means you recorded `--version-unknown`. That's allowed, and it's reported as such. **A batch that fails validation is not handed in.** If your reported model changed since you registered, stop and tell the operator. Don't edit the registration yourself.

## 7. Commit and push

```bash
git switch judging/<judge_id>        # the branch from 1.1
git add RUN_DIR/results/<judge_id>/   # your batches plus judge.json
git commit -m "Judge <judge_id>: batch NNNN (<stage>), validated"
git push -u origin judging/<judge_id>
```

- Stage only your own `results/<judge_id>/`. Never stage `keys/`, packets or anyone else's files.
- Commit as the operator unless told otherwise: `git -c user.name=nikbearbrown -c user.email=610338+nikbearbrown@users.noreply.github.com commit ...`. Never push to `main`, never force-push, and never open or merge a pull request.

## 8. Rate limits and resuming

If your plan's usage limit stops you mid-batch, keep what you have written. Then, in the next session, **start the batch again from its first line** in a fresh file. A half-finished batch must not be handed in. `manifest.json` (or the operator) tracks which batches are done.
