#!/usr/bin/env python3
"""Build source bundles for a list of concepts, all on this machine (pilot version: no cluster job).

Usage:
  python3 assemble_bundles.py CONCEPTS.tsv LEXICON_REPO OUT.jsonl \
      --kaggle KAGGLE_DIR --allowlist kaggle-allowlist.tsv --observations OBS.jsonl \
      --wordnet english-wordnet-2025.xml.gz [--cache DIR]

CONCEPTS.tsv    one concept per line: id <tab> preferred_name <tab> variants separated by |
LEXICON_REPO    a checkout of skills-lexicon (entries/, data/wikipedia-match/20261001/)
KAGGLE_DIR      <owner>/<dataset>/v<version>/dataset.zip for the allow-listed datasets
OBS.jsonl       the Kaggle evidence branch's observations.jsonl (which rows mention which concept)

Where each field comes from (the bundle contract in GENERATION_GUIDE.md, Part 2):
  concept     the entry file, with broad_class worked out from kind as tools/lexicon.py does
  neighbors   up to 30 lexicon concepts: existing relations both ways, look-alike and similar names,
              and lexicon concepts whose name matches a Wikidata ancestor or WordNet hypernym in the bundle
  examples    up to 5 job-posting snippets, one per dataset, allow-listed datasets only, postings only
  wikipedia   up to 3 non-disambiguation candidates from data/wikipedia-match/20261001 (dump revision ids);
              concepts with no match row get a title/redirect lookup of the revision current on 2026-10-01
  wikidata    up to 3 items (enwiki sitelinks of the Wikipedia candidates first, then exact English label
              or alias matches), six properties only, plus P31/P279 ancestors to two levels; public API
  wordnet     noun senses of the name and each variant from the pinned OEWN 2025 file, via the wn package
"""
import argparse
import collections
import csv
import difflib
import glob
import hashlib
import html
import html.parser
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile

csv.field_size_limit(sys.maxsize)
UA = "skills-lexicon-pilot/0.1 (research vocabulary project; https://github.com/nikbearbrown/skills-lexicon)"
PIDS = ("P31", "P279", "P361", "P527", "P460", "P1889")
LANGUAGE_KINDS = {"programming-language", "markup-language", "style-language", "modeling-language", "human-language"}
WN_MAP = {"hypernym": "hypernym", "hyponym": "hyponym", "mero_part": "part_meronym", "holo_part": "part_holonym",
          "mero_member": "member_meronym", "holo_member": "member_holonym"}
CUTOFF = "2026-10-01T00:00:00Z"
STOP_HEADINGS = {"references", "see also", "external links", "notes", "further reading", "bibliography",
                 "sources", "citations", "footnotes"}
TEXT_COLUMNS = ("description", "job description", "full_description", "job_summary", "requirements",
                "jobdescription", "job_description")
CACHE = None


def broad_class(kind):
    return ("ability" if kind == "ability" else "knowledge" if kind == "knowledge" else
            "certification" if kind == "credential" else "language" if kind in LANGUAGE_KINDS else "skill")


def get_json(url, params):
    """GET with a polite pause and an on-disk cache keyed by the full URL."""
    full = url + "?" + urllib.parse.urlencode(params)
    path = os.path.join(CACHE, hashlib.sha256(full.encode()).hexdigest() + ".json")
    if os.path.exists(path):
        return json.load(open(path))
    for tries in range(5):
        try:
            req = urllib.request.Request(full, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
            json.dump(data, open(path, "w"))
            time.sleep(0.3)
            return data
        except Exception as e:  # network hiccup or 429: back off and retry
            time.sleep(5 * (tries + 1))
            err = e
    raise RuntimeError(f"{full}: {err}")


# ---------- Wikipedia ----------

class TextOut(html.parser.HTMLParser):
    """Plain text from rendered article HTML: paragraphs, list items and headings; no tables,
    references, infoboxes, navboxes or hatnotes; stops at References / See also / External links."""
    SKIP_TAGS = {"table", "style", "script", "sup", "figure", "math", "noscript"}
    SKIP_CLASS = re.compile(r"navbox|hatnote|infobox|reflist|references|mw-references|thumb|sidebar|"
                            r"metadata|shortdescription|mw-editsection|noprint|reference|toc|gallery")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.stack, self.stopped, self.heading = [], 0, [], False, None

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "hr", "meta", "link", "wbr", "input"):
            return
        cls = dict(attrs).get("class", "") or ""
        skip = tag in self.SKIP_TAGS or bool(self.SKIP_CLASS.search(cls))
        self.stack.append(skip)
        self.skip += skip
        if tag in ("h2", "h3") and not self.skip:
            self.heading = []
        if tag in ("p", "li", "h2", "h3", "dd") and not self.skip:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("br", "img", "hr", "meta", "link", "wbr", "input"):
            return
        if self.stack:
            self.skip -= self.stack.pop()
        if tag in ("h2", "h3") and self.heading is not None:
            if "".join(self.heading).strip().lower() in STOP_HEADINGS:
                self.stopped = True
            self.heading = None

    def handle_data(self, data):
        if self.skip or self.stopped:
            return
        if self.heading is not None:
            self.heading.append(data)
        self.out.append(data)

    def text(self):
        t = re.sub(r"[ \t]+", " ", "".join(self.out))
        return re.sub(r"\n\s*\n+", "\n\n", t).strip()


def article_text(rev_id, max_words=3000):
    d = get_json("https://en.wikipedia.org/w/api.php", {
        "action": "parse", "oldid": rev_id, "prop": "text", "format": "json", "formatversion": 2,
        "disableeditsection": 1, "disabletoc": 1})
    if "parse" not in d:  # e.g. nosuchrevid: the matched revision was deleted after the October match run
        return None
    p = TextOut()
    p.feed(d["parse"]["text"])
    words = p.text().split(" ")
    return " ".join(words[:max_words])


def revision_at_cutoff(title):
    """Title or redirect lookup; the newest revision at or before the 2026-10-01 dump date."""
    d = get_json("https://en.wikipedia.org/w/api.php", {
        "action": "query", "titles": title, "redirects": 1, "prop": "revisions|pageprops",
        "rvprop": "ids|timestamp", "rvlimit": 1, "rvstart": CUTOFF, "rvdir": "older",
        "format": "json", "formatversion": 2})
    for page in d.get("query", {}).get("pages", []):
        if page.get("missing") or not page.get("revisions"):
            continue
        if "disambiguation" in (page.get("pageprops") or {}):
            continue
        return page["title"], page["revisions"][0]["revid"]
    return None


def wikipedia_candidates(concept, names, match_rows, cand_pages):
    seen, out = set(), []
    row = match_rows.get(concept["id"])
    if row:
        for c in row.get("candidates", []):
            page = cand_pages.get(c["page_id"])
            if not page or page["page_id"] in seen or page.get("disambiguation"):
                continue
            seen.add(page["page_id"])
            out.append((page["title"], page["rev_id"], c.get("how")))
            if len(out) == 3:
                break
    else:  # concepts added after the October match run
        for n in names:
            hit = revision_at_cutoff(n)
            if hit and hit[0] not in seen:
                seen.add(hit[0])
                out.append((hit[0], hit[1], "api-title-or-redirect"))
            if len(out) == 3:
                break
    result = []
    for t, r, how in out:
        text = article_text(r)
        if text is None:  # revision gone: look the title up again at the cutoff; skip the page if that fails too
            hit = revision_at_cutoff(t)
            if hit and hit[1] != r:
                t, r, how = hit[0], hit[1], f"{how}; revision re-resolved (matched revision deleted)"
                text = article_text(r)
        if text is None:
            continue
        result.append({"title": t, "revision_id": str(r), "matched_by": how, "text": text})
    return result


# ---------- Wikidata ----------

def wd_entities(ids):
    out = {}
    ids = [i for i in dict.fromkeys(ids) if i]
    for k in range(0, len(ids), 50):
        d = get_json("https://www.wikidata.org/w/api.php", {
            "action": "wbgetentities", "ids": "|".join(ids[k:k + 50]), "props": "labels|descriptions|aliases|claims|info",
            "languages": "en", "format": "json"})
        out.update(d.get("entities", {}))
    return out


def wd_record(e):
    claims = {}
    for pid in PIDS:
        vals = []
        for st in e.get("claims", {}).get(pid, []):
            v = st.get("mainsnak", {}).get("datavalue", {}).get("value")
            if isinstance(v, dict) and v.get("id", "").startswith("Q"):
                vals.append(v["id"])
        if vals:
            claims[pid] = vals
    return {"qid": e["id"], "label": e.get("labels", {}).get("en", {}).get("value", ""),
            "description": e.get("descriptions", {}).get("en", {}).get("value", ""),
            "aliases": [a["value"] for a in e.get("aliases", {}).get("en", [])],
            "claims": claims, "revision_id": str(e.get("lastrevid", ""))}


def wikidata_candidates(names, wp, fetched_on):
    qids = []
    titles = [w["title"] for w in wp]
    if titles:
        d = get_json("https://www.wikidata.org/w/api.php", {
            "action": "wbgetentities", "sites": "enwiki", "titles": "|".join(titles), "props": "info", "format": "json"})
        qids += [q for q, e in d.get("entities", {}).items() if q.startswith("Q") and "missing" not in e]
    label_hits, alias_hits = [], []
    for n in names:
        d = get_json("https://www.wikidata.org/w/api.php", {
            "action": "wbsearchentities", "search": n, "language": "en", "uselang": "en", "type": "item",
            "limit": 10, "format": "json"})
        for s in d.get("search", []):
            m = s.get("match", {})
            if m.get("language") == "en" and m.get("text", "").lower() == n.lower():
                (label_hits if m.get("type") == "label" else alias_hits).append(s["id"])
    qids = list(dict.fromkeys(qids + label_hits + alias_hits))[:3]
    if not qids:
        return []
    ents = wd_entities(qids)
    cands = [wd_record(ents[q]) for q in qids if q in ents]
    # English labels for every QID a candidate's statements point at, so a reader can tell what they are.
    vals = [v for c in cands for vs in c["claims"].values() for v in vs]
    lab = wd_entities(vals)
    for c in cands:
        c["value_labels"] = {v: lab[v].get("labels", {}).get("en", {}).get("value", "")
                             for vs in c["claims"].values() for v in vs if v in lab}
    out = [dict(c, fetched_utc=fetched_on) for c in cands]
    for c in cands:
        lvl1 = (c["claims"].get("P31", []) + c["claims"].get("P279", []))[:8]
        e1 = wd_entities(lvl1)
        lvl2 = []
        for q in lvl1:
            if q in e1:
                r = wd_record(e1[q])
                lvl2 += (r["claims"].get("P31", []) + r["claims"].get("P279", []))[:4]
        lvl2 = [q for q in dict.fromkeys(lvl2) if q not in lvl1 and q != c["qid"]][:12]
        e2 = wd_entities(lvl2)
        for q in lvl1 + lvl2:
            src = e1.get(q) or e2.get(q)
            if src:
                out.append(dict(wd_record(src), ancestor_of=c["qid"], level=1 if q in lvl1 else 2,
                                fetched_utc=fetched_on))
    return out


# ---------- WordNet ----------

def wordnet_senses(w, names, cap=15):
    seen, out = set(), []
    for n in dict.fromkeys(x for name in names for x in (name, name.lower())):
        for s in w.synsets(n, pos="n"):
            if s.id in seen:
                continue
            seen.add(s.id)
            rels, targets = {}, {}
            for k, v in s.relations().items():
                if k in WN_MAP:
                    rels[WN_MAP[k]] = [t.id for t in v]
                    for t in v:
                        targets[t.id] = ", ".join(t.lemmas()[:3])
            out.append({"synset": s.id, "lemmas": s.lemmas(), "gloss": s.definition() or "",
                        "examples": s.examples(), "relations": rels, "relation_targets": targets})
            if len(out) == cap:
                return out
    return out


# ---------- Job postings ----------

class Postings:
    def __init__(self, root, allow):
        self.root, self.allow, self.cache = root, allow, {}

    def rows(self, ref, version, member):
        key = (ref, version, member)
        if key not in self.cache:
            z = zipfile.ZipFile(os.path.join(self.root, ref, f"v{version}", "dataset.zip"))
            name = next((n for n in z.namelist() if n == member or n.endswith("/" + member)), member)
            with z.open(name) as f:
                self.cache[key] = list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace",
                                                                       newline="")))
        return self.cache[key]

    def snippet(self, row, column, forms):
        cols = {k.lower().strip(): k for k in row if k}
        title_col = next((cols[c] for c in cols if "title" in c or c in ("position", "role", "job")), None)
        text_col = next((cols[c] for c in TEXT_COLUMNS if c in cols and (row[cols[c]] or "").strip()), None)
        title = (row.get(title_col) or "").strip() if title_col else ""
        body = (row.get(text_col) if text_col else row.get(column)) or ""
        body = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).strip()
        pos = -1
        for f in forms:
            m = re.search(r"(?<![\w+#])" + re.escape(f) + r"(?![\w+#])", body, re.I)
            if m:
                pos = m.start()
                break
        if pos < 0:  # the label sits in the skills field, not the description: show that field
            body = re.sub(r"\s+", " ", row.get(column) or "").strip()
            pos = 0
        start = max(0, pos - 140)
        text = ("…" if start else "") + body[start:start + 300] + ("…" if start + 300 < len(body) else "")
        return (f"Job title: {title}. " if title else "") + text, text_col or column

    def available(self, o):
        return o["ref"] in self.allow and os.path.exists(
            os.path.join(self.root, o["ref"], f"v{o['version']}", "dataset.zip"))

    def examples(self, obs, forms, limit=5):
        obs = [o for o in obs if self.available(o)]  # allow-listed and copied here; nothing else
        ranked = sorted(obs, key=lambda o: (not any(c.lower() in TEXT_COLUMNS for c in
                                                     self.allow[o["ref"]]["columns"].split("|")), -o["records"]))
        out, used = [], set()
        for o in ranked:
            if o["ref"] in used:
                continue
            rows = self.rows(o["ref"], o["version"], o["member"])
            for rec in o["csv_records"]:
                if 0 <= rec - 2 < len(rows):
                    text, col = self.snippet(rows[rec - 2], o["column"], forms + o["labels"])
                    # No '#' or '=' in an id: the pointer ex:<id> is split on those characters.
                    out.append({"id": f"{o['ref']}@v{o['version']}/{o['member']}:{rec}",
                                "source": f"kaggle:{o['ref']} ({self.allow[o['ref']]['licence']}), column {col}",
                                "text": text})
                    used.add(o["ref"])
                    break
            if len(out) == limit:
                break
        return out


def load_observations(path, ids):
    per = collections.defaultdict(list)
    for line in open(path):
        o = json.loads(line)
        if o.get("id") not in ids:
            continue
        ob = o["observation"]
        per[o["id"]].append({"ref": ob["source_family"], "version": ob["dataset_version"], "member": ob["member"],
                             "column": ob["extraction"]["column"], "records": ob["counts"]["records"],
                             "csv_records": [e["csv_record"] for e in ob["examples"]],
                             "labels": sorted({m["observed_label"] for m in ob.get("matched_forms", [])})})
    return per


# ---------- Neighbors ----------

def words(s):
    return set(re.findall(r"[a-z0-9+#]+", s.lower()))


def mentioned(text, entries, me, limit=12):
    """Lexicon concepts named in the source text (Wikipedia candidate, posting snippets), most frequent first.
    Names of 3+ characters only; names of 3 characters must match case exactly (SQL, PHP), longer ones ignore case."""
    low, counts = text.lower(), collections.Counter()
    for other in entries:
        if other["id"] == me:
            continue
        for f in [other["preferred_name"]] + [v["label"] for v in other.get("variants", [])]:
            if len(f) < 3 or (f.lower() not in low):
                continue
            pat = r"(?<![\w+#])" + re.escape(f) + r"(?![\w+#])"
            hits = len(re.findall(pat, text)) if len(f) == 3 else len(re.findall(pat, text, re.I))
            if hits:
                counts[other["id"]] += hits
    return [oid for oid, _ in counts.most_common(limit)]


def neighbors(e, entries, by_id, by_name, extra_names, source_text, n=30):
    me = e["id"]
    picked = collections.OrderedDict()
    for r in e.get("relations", []):
        if r.get("target") in by_id:
            picked[r["target"]] = 9.0
    for other in entries:
        if any(r.get("target") == me for r in other.get("relations", [])):
            picked.setdefault(other["id"], 9.0)
    for name in extra_names:  # Wikidata ancestors and WordNet hypernyms that the lexicon also has
        for oid in by_name.get(name.lower(), []):
            if oid != me:
                picked.setdefault(oid, 8.0)
    for oid in mentioned(source_text, entries, me):
        picked.setdefault(oid, 7.0)
    forms = [e["preferred_name"]] + [v["label"] for v in e.get("variants", [])]
    fw = set().union(*(words(f) for f in forms))
    scores = []
    for other in entries:
        if other["id"] == me or other["id"] in picked:
            continue
        oforms = [other["preferred_name"]] + [v["label"] for v in other.get("variants", [])]
        best = 0.0
        for a in forms:
            al = a.lower()
            for b in oforms:
                bl = b.lower()
                s = difflib.SequenceMatcher(None, al, bl).ratio()
                if len(al) >= 3 and len(bl) >= 3 and (al in bl or bl in al):
                    s += 0.35
                if al != bl and (bl.startswith(al) or al.startswith(bl)) and min(len(al), len(bl)) <= 3:
                    s += 0.25  # look-alikes such as C / C++ / C#, R / Rust, Go / Golang
                best = max(best, s)
        ow = set().union(*(words(f) for f in oforms))
        if fw and ow:
            best = max(best, len(fw & ow) / len(fw | ow) + 0.1)
        scores.append((best, other["id"]))
    for s, oid in sorted(scores, reverse=True):
        if len(picked) >= n:
            break
        picked[oid] = s
    return [{"id": oid, "name": by_id[oid]["preferred_name"]} for oid in list(picked)[:n]]


def main():
    global CACHE
    ap = argparse.ArgumentParser()
    ap.add_argument("concepts"); ap.add_argument("repo"); ap.add_argument("out")
    ap.add_argument("--kaggle", required=True); ap.add_argument("--allowlist", required=True)
    ap.add_argument("--observations", required=True); ap.add_argument("--wordnet", required=True)
    ap.add_argument("--cache", default=None)
    ap.add_argument("--with-record", action="store_true",
                    help="also put the entry's definition and identifiers in the concept record")
    a = ap.parse_args()
    CACHE = a.cache or os.path.join(os.path.dirname(os.path.abspath(a.out)), ".http-cache")
    os.makedirs(CACHE, exist_ok=True)

    import wn
    if not any(l.id == "oewn" and l.version == "2025" for l in wn.lexicons()):
        wn.add(a.wordnet, progress_handler=None)
    w = wn.Wordnet("oewn:2025")

    entries = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(a.repo, "entries", "*.json")))]
    by_id = {e["id"]: e for e in entries}
    by_name = collections.defaultdict(list)
    for e in entries:
        for f in [e["preferred_name"]] + [v["label"] for v in e.get("variants", [])]:
            by_name[f.lower()].append(e["id"])
    wm = os.path.join(a.repo, "data", "wikipedia-match", "20261001")
    match_rows = {m["entry_id"]: m for m in map(json.loads, open(os.path.join(wm, "matches.jsonl")))}
    cand_pages = {c["page_id"]: c for c in map(json.loads, open(os.path.join(wm, "candidates.jsonl")))}
    allow = {r["dataset_ref"]: r for r in csv.DictReader(open(a.allowlist), delimiter="\t")}
    ids = [l.split("\t")[0] for l in open(a.concepts) if l.strip()]
    obs = load_observations(a.observations, set(ids))
    postings = Postings(a.kaggle, allow)
    today = time.strftime("%Y-%m-%d")

    done = set()
    if os.path.exists(a.out):
        done = {json.loads(l)["concept_id"] for l in open(a.out) if l.strip()}
    with open(a.out, "a") as out:
        for cid in ids:
            if cid in done:
                continue
            e = by_id[cid]
            forms = [e["preferred_name"]] + [v["label"] for v in e.get("variants", [])]
            concept = {"id": cid, "preferred_name": e["preferred_name"], "kind": e["kind"],
                       "broad_class": broad_class(e["kind"]),
                       "variants": [{k: v[k] for k in ("label", "needs_context", "ambiguous") if k in v}
                                    for v in e.get("variants", [])],
                       "relations": [{"type": r["type"], "target": r["target"],
                                      "target_name": by_id.get(r["target"], {}).get("preferred_name")}
                                     for r in e.get("relations", [])]}
            if a.with_record:
                # Beyond the guide's contract: the lexicon's own definition and codes (O*NET element and the like).
                # In the pilot this alone fixed the Service orientation and Mathematics (skill) senses.
                concept["definition"] = e.get("definition", "")
                if e.get("identifiers"):
                    concept["identifiers"] = e["identifiers"]
            wp = wikipedia_candidates(concept, forms, match_rows, cand_pages)
            wd = wikidata_candidates(forms, wp, today)
            wns = wordnet_senses(w, forms)
            extra = [i["label"] for i in wd if i.get("ancestor_of")]
            extra += [lem for s in wns for t in s["relations"].get("hypernym", []) for lem in s["relation_targets"].get(t, "").split(", ")]
            ex = postings.examples(obs.get(cid, []), forms)
            source_text = " ".join((wp[0]["text"].split(" ")[:1500] if wp else []) + [x["text"] for x in ex])
            b = {"concept_id": cid, "concept": concept,
                 "neighbors": neighbors(e, entries, by_id, by_name, extra, source_text),
                 "examples": ex, "wikipedia": wp, "wikidata": wd, "wordnet": wns}
            out.write(json.dumps(b, ensure_ascii=False) + "\n")
            out.flush()
            print(f"{cid} {e['preferred_name']}: wp {len(wp)}, wd {sum(1 for i in wd if not i.get('ancestor_of'))}"
                  f"+{sum(1 for i in wd if i.get('ancestor_of'))} anc, wn {len(wns)}, ex {len(ex)}", flush=True)


if __name__ == "__main__":
    main()
