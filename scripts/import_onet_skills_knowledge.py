"""Bring in O*NET's 35 skills and 33 knowledge areas, the way the 52 abilities came in.

    python3 -I scripts/import_onet_skills_knowledge.py extract PATH/TO/db_30_2_text
    python3 -I scripts/import_onet_skills_knowledge.py entries

`extract` reads three files of the O*NET 30.2 text database (Content Model Reference.txt, Skills.txt, Knowledge.txt) and
writes, for skills in `onet-skills/` and for knowledge in `onet-knowledge/`:
  - the elements (element id, name, definition, category, subcategory), as `onet-abilities.json` does for abilities;
  - the level (`LV`) ratings for every occupation, with the same 15 columns as
    `abilities/onet-ability-ratings-all-occupations.csv`. Values stay as O*NET writes them; Y/N become true/false.
Nothing is recalculated, rounded, filtered or filled in. The importance (`IM`) rows are left out, as they are for abilities.

`entries` reads those two JSON files and, for each element:
  - skips it if an entry already carries its `onet-element` identifier (so the script can be run again);
  - if an entry of the same kind already has the O*NET name as its preferred name or a variant (case ignored), adds the
    identifier and a `matched_source` record for `kind` to that entry. Its drafted definition is kept; whether to take
    O*NET's wording instead is a person's call, so the O*NET definition goes in the note, not in the claim;
  - otherwise writes a new entry, `proposed`, with O*NET's definition, and `matched_source` records for `kind` and
    `definition` (`dump-match`, since the data is the O*NET database file itself).
Where a new entry's name is already another kind's name (O*NET has Mathematics as both a skill and a knowledge area),
both entries are marked `name_ambiguous`, so an extractor reports the clash instead of picking one.

O*NET 31.0 keeps the same element ids and the same element definitions; it splits Skills into Essential Skills and
Transferable Skills and rewords the group descriptions. The claims here cite 30.2, the release the abilities cite.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import ingest as I  # noqa: E402
import lexicon as L  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RUN, DATE, VERSION = "2026-11-13-onet-skills-knowledge-import", "2026-11-13", "30.2"
ORG = {"name": "O*NET, U.S. Department of Labor, Employment and Training Administration", "url": "https://www.onetcenter.org/",
       "type": "government", "country": "US"}
NOTICE = ("This is a selection and reformatting of O*NET data. USDOL/ETA has not approved, endorsed or tested these changes. "
          "O*NET(R) is a trademark of USDOL/ETA.")
SETS = {   # O*NET file, our folder and file stem, lexicon kind, O*NET's top-level heading
    "skill": ("Skills.txt", "onet-skills", "onet-skill", "Skills"),
    "knowledge": ("Knowledge.txt", "onet-knowledge", "onet-knowledge", "Knowledge"),
}
COLS = ["soc_code", "element_id", "element_name", "category", "subcategory", "scale_id", "data_value", "n", "standard_error",
        "lower_ci", "upper_ci", "recommend_suppress", "not_relevant", "date_updated", "domain_source"]
SRC_COLS = ["O*NET-SOC Code", "Element ID", "Element Name", "Scale ID", "Data Value", "N", "Standard Error", "Lower CI Bound",
            "Upper CI Bound", "Recommend Suppress", "Not Relevant", "Date", "Domain Source"]


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if rows and set(SRC_COLS) - set(rows[0]) and "Description" not in rows[0]:
        raise SystemExit(f"{path}: unexpected columns {list(rows[0])}")
    return rows


def id_order(eid):
    return [(0, int(p), "") if p.isdigit() else (1, 0, p) for p in eid.split(".")]


def groups(eid, cm):
    """O*NET's grouping above an element: for 2.A.1.a that is Basic Skills > Content; for 2.C.6 there is none below Knowledge."""
    parts = eid.split(".")
    up = [".".join(parts[:k]) for k in range(2, len(parts))]   # 2.A, 2.A.1 for 2.A.1.a; 2.C for 2.C.1.a
    names = [cm[u]["Element Name"] for u in up if u in cm]
    if names and names[0] == "Knowledge":                        # 2.C is the heading itself, not a group
        names = names[1:]
    return (names + [None, None])[:2]


def yn(v):
    return {"Y": "true", "N": "false"}.get(v, v)


def extract(src):
    src = Path(src)
    cm = {r["Element ID"]: r for r in read_tsv(src / "Content Model Reference.txt")}
    for kind, (fname, folder, stem, heading) in SETS.items():
        rows = read_tsv(src / fname)
        lv = [r for r in rows if r["Scale ID"] == "LV"]
        ids = sorted({r["Element ID"] for r in rows}, key=id_order)
        out = ROOT / folder
        out.mkdir(exist_ok=True)
        elements = []
        for eid in ids:
            cat, sub = groups(eid, cm)
            elements.append({"element_id": eid, "name": cm[eid]["Element Name"], "definition": cm[eid]["Description"].strip(),
                             "category": cat, "subcategory": sub})
        doc = {"source": f"O*NET {VERSION} {heading}, U.S. Department of Labor, Employment and Training Administration (USDOL/ETA)",
               "license": "CC BY 4.0, https://creativecommons.org/licenses/by/4.0/", "notice": NOTICE,
               "o_net_url": "https://www.onetcenter.org/", "database_release": "https://www.onetcenter.org/db_releases.html",
               "fields": (f"element_id is the O*NET content-model id; name and definition are O*NET's text from Content Model "
                          f"Reference.txt; category and subcategory are the O*NET groups above the element (null where there is none)."),
               "count": len(elements), f"{kind}s" if kind == "skill" else "knowledge": elements}
        (out / f"{stem}{'s' if kind == 'skill' else ''}.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", "utf-8")
        by_id = {e["element_id"]: e for e in elements}
        with open(out / f"{stem}-ratings-all-occupations.csv", "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\r\n")
            w.writerow(COLS)
            for r in lv:
                e = by_id[r["Element ID"]]
                w.writerow([r["O*NET-SOC Code"], r["Element ID"], r["Element Name"], e["category"] or "", e["subcategory"] or "",
                            r["Scale ID"], r["Data Value"], r["N"], r["Standard Error"], r["Lower CI Bound"], r["Upper CI Bound"],
                            yn(r["Recommend Suppress"]), yn(r["Not Relevant"]), r["Date"], r["Domain Source"]])
        print(f"{kind}: {len(elements)} elements, {len(lv)} LV rows of {len(rows)}, "
              f"{len({r['O*NET-SOC Code'] for r in lv})} occupations -> {folder}/")


def load_elements():
    for kind, (_, folder, stem, heading) in SETS.items():
        d = json.loads((ROOT / folder / f"{stem}{'s' if kind == 'skill' else ''}.json").read_text("utf-8"))
        for a in d["skills" if kind == "skill" else "knowledge"]:
            yield kind, heading, a


def write(e):
    """Write an entry back, without the loader's own bookkeeping fields (`_file` and the like)."""
    clean = {k: v for k, v in e.items() if not k.startswith("_")}
    (ROOT / "entries" / f"{e['key']}.json").write_text(json.dumps(clean, indent=1, ensure_ascii=False) + "\n", "utf-8")


def entries():
    ents, _ = L.load(ROOT / "entries")
    taken = {x["id"] for x in ents} | {f for x in ents for f in x.get("former_ids", [])}
    keys = {x.get("key") for x in ents}
    have = {(i["scheme"], i["code"]) for e in ents for i in e.get("identifiers", [])}
    by_form = {}
    for e in ents:
        for fm in L.forms(e):
            by_form.setdefault(fm["label"].lower(), []).append(e)
    made, matched, ambiguous = [], [], []
    for kind, heading, a in load_elements():
        eid = a["element_id"]
        if ("onet-element", eid) in have:
            continue
        cats = [heading] + [c for c in (a["category"], a["subcategory"]) if c]
        where = ", ".join(cats)

        def ev(field, note):
            return {"field": field, "by": f"source:onet-{VERSION}", "action": "matched_source", "kind": "onet", "verification": "dump-match",
                    "outcome": "supports", "ref": f"onet:{eid}", "date": DATE, "run": RUN, "note": note[:I.NOTE_MAX], "organization": ORG,
                    "match": {"dataset": f"onet-{VERSION}", "dataset_id": eid, "method": "import", "categories": cats}}

        same = [e for e in by_form.get(a["name"].lower(), []) if L.top_class(e) == kind]
        if len(same) == 1:
            e = same[0]
            e.setdefault("identifiers", []).append({"scheme": "onet-element", "code": eid})
            e["evidence"].append(ev("kind", f"O*NET {VERSION} lists '{a['name']}' under {where}. Drafted definition kept; "
                                            f"O*NET's: {a['definition']}"))
            write(e)
            matched.append((a["name"], e["key"]))
            have.add(("onet-element", eid))
            continue
        if len(same) > 1:
            raise SystemExit(f"{a['name']}: {len(same)} {kind} entries already claim this name; settle that by hand first")
        clash = by_form.get(a["name"].lower(), [])
        base = I.slugify(a["name"], set())
        key = base if base not in keys else I.slugify(f"{a['name']} {kind}", keys)
        keys.add(key)
        new_id = L.new_id(taken)
        taken.add(new_id)
        e = {"id": new_id, "key": key, "preferred_name": a["name"], "kind": kind, "definition": a["definition"],
             "identifiers": [{"scheme": "onet-element", "code": eid}],
             "variants": [], "relations": [], "verbs": [], "status": "proposed",
             "provenance": {"source": f"imported from O*NET {VERSION} {heading} (USDOL/ETA, CC BY 4.0) "
                                      f"{SETS[kind][1]}/, run {RUN}",
                            "date": DATE, "review": "Awaiting taxonomy owner review", "reviewed_by": None},
             "evidence": [ev("kind", f"O*NET {VERSION} lists it under {where}"),
                          ev("definition", f"the definition is O*NET {VERSION}'s text")]}
        if clash:
            e["name_ambiguous"] = True
            for other in clash:
                if not other.get("name_ambiguous") and other["preferred_name"].lower() == a["name"].lower():
                    other["name_ambiguous"] = True
                    write(other)
                ambiguous.append((a["name"], key, other["key"], other["kind"]))
        write(e)
        made.append(key)
        have.add(("onet-element", eid))
        by_form.setdefault(a["name"].lower(), []).append(e)
    print(f"new entries: {len(made)}; existing entries given the O*NET identifier: {len(matched)} {matched}; "
          f"shared names marked ambiguous: {ambiguous}")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "extract" and len(sys.argv) == 3:
        extract(sys.argv[2])
    elif sys.argv[1:] == ["entries"]:
        entries()
    else:
        print(__doc__)
        sys.exit(2)
