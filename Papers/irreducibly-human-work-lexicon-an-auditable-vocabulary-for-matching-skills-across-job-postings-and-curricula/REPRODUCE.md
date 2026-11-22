# Audit and figures

The inventory audit reads the public Lexicon at commit `3cd82a454877e83d3f7eb989136de1d234e9944e`. The two later contributor-guide edits do not modify the inventory. The denominators are separate: 3,754 canonical entries and 17,229 distinct entry–claim pairs.

Run this from a clean checkout of that SHA:

```sh
python3 -I tools/lexicon.py validate
python3 -I scripts/summary_stats.py > inventory-recount.json
```

Run `python3 generate_figures.py inventory-recount.json` next to the supplied script. It writes two SVGs. The workflow example is illustrative; the other graphic reads the audit counts directly from the JSON. The survey is a descriptive count of a fixed Git tree, not a probability sample.

Scope caveat: the pinned recount uses the key `rollup` for its `rollup_enabled` metric, while the schema uses `rolls_up`. The figure, study table, and discussion do not use the erroneous summary metric. A separate inspection found one relation with `rolls_up: true`.
