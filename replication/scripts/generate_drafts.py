#!/usr/bin/env python3
"""Generate Irreducibly Human Work Lexicon draft entries for one batch of source bundles.

Usage: python3 generate_drafts.py SYSTEM_PROMPT.txt USER_TEMPLATE.txt BUNDLES.jsonl DRAFTS.jsonl [--ungrounded] [--workers N]

Each draft is one call to headless Claude Code (`claude -p`) on the plan the machine is signed in to.
No API key is used. The call has no tools (it can only write the draft), its answer must match the
draft's JSON schema, and it runs from an empty folder so no project files or memory leak in.

Environment (all optional):
  LEXICON_MODEL   model id (default claude-opus-5-5)
  LEXICON_EFFORT  low | medium | high | xhigh | max (default high)
  PROMPT_VERSION  recorded in every draft's _meta (default unset)
  CLAUDE_BIN      path to the claude binary (default: newest Claude desktop bundle, else `claude` on PATH)
  CLEAN_DIR       empty working folder for the calls (default: ./work/.clean)

--ungrounded empties wikipedia, wikidata and wordnet in every bundle (the pilot's comparison run).
Skips concepts already present in DRAFTS.jsonl, so an interrupted batch can be rerun.
Stops cleanly, writing nothing for the concept in hand, if the plan's usage limit is reached.
"""
import argparse
import datetime
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from verify_drafts import load_jsonl, ungrounded, verify

FIELDS = {
    "{concept_json}": "concept",
    "{neighbors_json}": "neighbors",
    "{examples_json}": "examples",
    "{wikipedia_json}": "wikipedia",
    "{wikidata_json}": "wikidata",
    "{wordnet_json}": "wordnet",
}

BASIS = {"type": "string", "enum": ["source", "model_knowledge"]}
POINTERS = {"type": "array", "items": {"type": "string"}}
NULLABLE = {"type": ["string", "null"]}
LINK = {"type": "object", "additionalProperties": False, "required": ["choice", "reason"],
        "properties": {"choice": NULLABLE, "reason": {"type": "string"}}}
SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["concept_id", "work_sense", "links", "definition", "variants", "relations", "flags"],
    "properties": {
        "concept_id": {"type": "string"},
        "work_sense": {"type": "string"},
        "links": {"type": "object", "additionalProperties": False,
                  "required": ["wikipedia", "wikidata", "wordnet"],
                  "properties": {"wikipedia": LINK, "wikidata": LINK, "wordnet": LINK}},
        "definition": {"type": "object", "additionalProperties": False,
                       "required": ["text", "basis", "pointers"],
                       "properties": {"text": {"type": "string"}, "basis": BASIS, "pointers": POINTERS}},
        "variants": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["text", "condition", "basis", "pointers"],
            "properties": {"text": {"type": "string"}, "condition": NULLABLE, "basis": BASIS, "pointers": POINTERS}}},
        "relations": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["type", "target_label", "target_id", "proposed_new", "basis", "pointers", "note"],
            "properties": {
                "type": {"type": "string", "enum": ["synonym", "hypernym", "hyponym", "meronym", "holonym",
                                                    "uses", "requires", "certifies", "contrast"]},
                "target_label": {"type": "string"}, "target_id": NULLABLE,
                "proposed_new": {"type": "boolean"}, "basis": BASIS, "pointers": POINTERS, "note": NULLABLE}}},
        "flags": {"type": "array", "items": {"type": "string"}},
    },
}

# Variables the Claude desktop app sets for its own session; a drafting call must not inherit them.
DROP_ENV = ("CLAUDE_CODE_USER_EMAIL", "CLAUDE_CODE_SESSION_ID", "CLAUDE_CODE_HOST_SESSION_ID",
            "CLAUDE_CODE_CHILD_SESSION", "CLAUDE_CODE_CHILD_NOTES_DIR", "CLAUDE_CODE_MESSAGING_SOCKET",
            "CLAUDE_CODE_MESSAGING_TOKEN", "CLAUDE_CODE_SESSION_ATTENDED", "CLAUDE_CODE_TERMINAL_MCP_TOOLS",
            "CLAUDE_CODE_REPORT_FINDINGS", "CLAUDE_CODE_ENABLE_ASK_USER_QUESTION_TOOL", "CLAUDE_PID", "CLAUDECODE")
LIMIT_WORDS = re.compile(r"usage limit|limit reached|rate.?limit|weekly limit|out of (usage|credits)|429|"
                         r"hit your .{0,20}limit|5-hour limit|exceeded", re.I)
STOP_AFTER = os.environ.get("STOP_AFTER")        # local time HH:MM; no new drafts start after it
LIMIT_WAIT_HOURS = float(os.environ.get("LIMIT_WAIT_HOURS", "0"))  # wait for a usage window to reset, then go on
RESUME_BEFORE = os.environ.get("RESUME_BEFORE")  # local HH:MM; after a limit, open no new window at or after it
# (a window opened at RESUME_BEFORE resets five hours later, so 02:30 keeps the plan free from 07:30)


class LimitReached(Exception):
    pass


def claude_bin():
    if os.environ.get("CLAUDE_BIN"):
        return os.environ["CLAUDE_BIN"]
    found = glob.glob(os.path.expanduser(
        "~/Library/Application Support/Claude/claude-code/*/*/claude.app/Contents/MacOS/claude"))
    key = lambda p: [int(x) for x in re.findall(r"claude-code/([\d.]+)/", p)[0].split(".")]
    return sorted(found, key=key)[-1] if found else shutil.which("claude")


def fill(template, b):
    for placeholder, key in FIELDS.items():
        template = template.replace(placeholder, json.dumps(b.get(key, []), indent=1, ensure_ascii=False))
    return template


def ask(system, prompt, clean_dir):
    """One headless call. Returns (draft dict or None, raw text, usage record)."""
    cmd = [claude_bin(), "-p", "--model", os.environ.get("LEXICON_MODEL", "claude-opus-5-5"),
           "--effort", os.environ.get("LEXICON_EFFORT", "high"),
           "--setting-sources", "", "--strict-mcp-config", "--disable-slash-commands",
           "--system-prompt", system, "--tools", "", "--no-session-persistence",
           "--output-format", "json", "--json-schema", json.dumps(SCHEMA)]
    env = {k: v for k, v in os.environ.items() if k not in DROP_ENV}
    for tries in range(3):
        started = time.time()
        p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=clean_dir, env=env, timeout=1800)
        try:
            out = json.loads(p.stdout)
        except json.JSONDecodeError:
            out = {"is_error": True, "result": (p.stdout or p.stderr or "no output")[-2000:]}
        usage = {"seconds": round(time.time() - started, 1), "cost_usd_notional": out.get("total_cost_usd"),
                 **{k: (out.get("usage") or {}).get(k) for k in
                    ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")}}
        if not out.get("is_error"):
            draft = out.get("structured_output")
            text = out.get("result") or ""
            if draft is None and LIMIT_WORDS.search(text):  # the plan's limit can come back as a normal reply
                raise LimitReached(text[:500])
            if draft is None:
                try:
                    draft = json.loads(re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip()))
                except json.JSONDecodeError:
                    draft = None
            return draft, text, usage
        msg = str(out.get("result", ""))
        if LIMIT_WORDS.search(msg):
            raise LimitReached(msg[:500])
        time.sleep(30 * (tries + 1))
    return None, msg, usage


def draft_one(system, template, b, clean_dir):
    """Draft one entry; on verifier errors, retry once with the errors as feedback."""
    first = fill(template, b)
    prompt, usages = first, []
    for attempt in (1, 2):
        entry, text, usage = ask(system, prompt, clean_dir)
        usages.append(usage)
        try:
            if entry is None:
                raise ValueError(f"no draft object returned: {text[:300]}")
            errs, _ = verify(entry, b)
        except (ValueError, AttributeError, KeyError, TypeError) as e:
            entry, errs = None, [f"output was not a valid draft object: {e}"]
        if not errs or attempt == 2:
            return entry, attempt, errs, usages
        prompt = (first + "\n\nYour previous draft was:\n" + json.dumps(entry, ensure_ascii=False)
                  + "\n\nThe verifier rejected this draft:\n- " + "\n- ".join(errs)
                  + "\nFix only these problems. Drop any claim you cannot support rather than "
                    "inventing a pointer. Return the corrected JSON object only.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("system"); ap.add_argument("template"); ap.add_argument("bundles"); ap.add_argument("drafts")
    ap.add_argument("--ungrounded", action="store_true")
    ap.add_argument("--workers", type=int, default=3)
    a = ap.parse_args()
    system, template = open(a.system).read(), open(a.template).read()
    bundles = load_jsonl(a.bundles)
    if a.ungrounded:
        bundles = {cid: ungrounded(b) for cid, b in bundles.items()}
    done = load_jsonl(a.drafts) if os.path.exists(a.drafts) else {}
    todo = [(cid, b) for cid, b in bundles.items() if cid not in done]
    clean_dir = os.environ.get("CLEAN_DIR", os.path.join(os.path.dirname(os.path.abspath(a.drafts)), ".clean"))
    os.makedirs(clean_dir, exist_ok=True)
    version = subprocess.run([claude_bin(), "--version"], capture_output=True, text=True).stdout.strip()
    lock, stop = threading.Lock(), threading.Event()
    print(f"{len(todo)} to draft, {len(done)} already done; {a.workers} at a time; {version}", flush=True)

    def past_stop_time():
        return bool(STOP_AFTER) and time.strftime("%H:%M") >= STOP_AFTER and time.strftime("%H:%M") < "12:00"

    def past_resume_cutoff():
        now = time.strftime("%H:%M")
        return bool(RESUME_BEFORE) and RESUME_BEFORE <= now < "12:00"

    def work(cid, b):
        if stop.is_set():
            return
        if past_stop_time():
            stop.set()
            print(f"STOPPED: past {STOP_AFTER}, no new drafts ({cid} not drafted)", flush=True)
            return
        started = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        deadline = time.time() + LIMIT_WAIT_HOURS * 3600
        while True:
            try:
                entry, attempts, errs, usages = draft_one(system, template, b, clean_dir)
                break
            except LimitReached as e:
                if time.time() + 600 > deadline or stop.is_set() or past_stop_time():
                    stop.set()
                    print(f"STOPPED at the usage limit ({cid} not drafted): {e}", flush=True)
                    return
                print(f"usage limit reached; waiting 10 minutes ({cid}): {str(e)[:120]}", flush=True)
                time.sleep(600)
                if stop.is_set() or past_stop_time() or past_resume_cutoff():  # a reset may come too late
                    stop.set()
                    print(f"STOPPED after waiting at the usage limit: past {STOP_AFTER} or {RESUME_BEFORE} "
                          f"({cid} not drafted)", flush=True)
                    return
        entry = entry or {"concept_id": cid}
        entry["concept_id"] = cid
        entry["_meta"] = {"model": os.environ.get("LEXICON_MODEL", "claude-opus-5-5"),
                          "effort": os.environ.get("LEXICON_EFFORT", "high"),
                          "via": f"headless Claude Code ({version}), no tools, JSON schema",
                          "prompt_version": os.environ.get("PROMPT_VERSION", "unset"),
                          "run": "ungrounded" if a.ungrounded else "grounded",
                          "attempts": attempts, "unresolved_errors": errs, "usage": usages,
                          "started_utc": started,
                          "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
        with lock, open(a.drafts, "a") as out:
            out.write(json.dumps(entry, ensure_ascii=False) + "\n")
        name = b["concept"].get("preferred_name", cid)
        print(f"{cid} {name}: {'ok' if not errs else 'needs review'} after {attempts} attempt(s)", flush=True)

    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        for f in as_completed([pool.submit(work, cid, b) for cid, b in todo]):
            f.result()
    sys.exit(3 if stop.is_set() else 0)


if __name__ == "__main__":
    main()
