# pilot-test: a small run for trying out the AI judge instructions

- **Concepts:** the 35 in `concepts.tsv`. These are the 13 trap concepts that both editions drafted, plus 22 seeded (20261123) shared non-pilot concepts: 13 skills, 5 knowledge areas, 2 languages and 2 abilities.
- **Editions:** `grok` (ungrounded), `grok-grounded` (the 13 trap concepts only), `sonnet` (`claude-sonnet-5-5`), and `reference` (the lexicon at `91312fec`). The trap concepts get all 6 pairs and the others get 3, so there are 144 definition pairs (stage P2 only).
- **Judges:** pre-registered in `judges.json`, with each judge's packets in `packets/<id>/` (self-exclusion already applied). Kickoff messages are in [../../judging/START-HERE-AI-JUDGE.md](../../judging/START-HERE-AI-JUDGE.md).
- **Not here on purpose:** `keys/`, `canonical/`, `tables/` and `coverage.csv` (see `../.gitignore`). They name the editions. The operator keeps them privately.

Rebuilt with:

```bash
python3 replication/scripts/agreement.py run replication/agreement/pilot-test --private-dir <PRIVATE>/pilot-test \
  --concepts replication/agreement/pilot-test/concepts.tsv --lexicon <lexicon@91312fec> --with-reference \
  --edition grok=gen-v2:<grok>/full-run-grok-bot-20261122/drafts-full.jsonl,<grok>/lex-pilot-grok-bot-20261122/drafts-ungrounded.jsonl \
  --edition grok-grounded=gen-v2:<grok>/lex-pilot-grok-bot-20261122/drafts-grounded.jsonl \
  --edition sonnet=sonnet-edition:<sonnet>/entries.jsonl
# then register each judge (operator only; needs --keys <PRIVATE>/pilot-test/keys/anon.jsonl)
```

A rebuild draws a new request-id secret, so its ids won't match the committed ones. Rebuild only to start a fresh run.
