"""Regenerate paper SVGs from a lexicon summary_stats.py JSON recount."""
from html import escape
from pathlib import Path
import json
import sys

stats = json.loads(Path(sys.argv[1]).read_text())
out = Path(__file__).resolve().parent / "figures"
out.mkdir(exist_ok=True)

def svg(name, h, title, desc, layers):
    body = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{h}" viewBox="0 0 1040 {h}" role="img" aria-labelledby="title desc">\n'
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>\n'
            f'<rect width="1040" height="{h}" fill="#fff"/>\n'
            '<g font-family="Arial, sans-serif" fill="#202a37">\n' + "\n".join(layers) + '</g></svg>\n')
    (out / name).write_text(body)

def line(x, y, val, size=25, bold=False, color="#202a37"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{700 if bold else 400}">{escape(str(val))}</text>'

def box(x,y,w,h,color,stroke="none"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{color}" stroke="{stroke}"/>'

def join_arrow(x1,y,x2):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-7}" y2="{y}" stroke="#164f64" stroke-width="3"/>'
            f'<polygon points="{x2},{y} {x2-9},{y-6} {x2-9},{y+6}" fill="#164f64"/>')

workflow = [line(34,47,"From a label to a reviewable claim",34,True)]
for x, title, a, b in [
    (34,"1. Source mention","A posting asks for","Postgres."),
    (370,"2. Concept candidate","Postgres may name","the PostgreSQL database."),
    (706,"3. Claim decision","Check the alias in context;","record the source and result.")
]:
    workflow += [box(x,85,300,128,"#edf5f6","#61929b"), line(x+16,120,title,24,True), line(x+16,158,a,21),line(x+16,186,b,21)]
workflow += [join_arrow(339,148,364),join_arrow(675,148,700),line(34,264,"If the context does not resolve the meaning, leave the match undecided.",23),
             line(34,297,"A verified alias is not proof of proficiency, prevalence, or a reviewed entry.",23,True)]
svg("claim-workflow.svg",327,"From a label to a reviewable claim","Illustrative pipeline from source mention to candidate concept to claim-level review; ambiguity can remain undecided.",workflow)

classes = [(label,stats["classes"][key]) for label,key in [("Skills","skill"),("Credentials","certification"),("Knowledge","knowledge"),("Languages","language"),("Abilities","ability")]]
claim = stats["claims"]
backed, total = claim["backed"], claim["total"]
assert sum(n for _,n in classes) == stats["entries"]
assert backed <= total
audit = [line(34,48,"Inventory and evidence use different denominators",33,True),
         line(34,100,f"A. Canonical concepts (n = {stats['entries']:,})",25,True)]
for i,(label,n) in enumerate(classes):
    y = 123 + i*41
    w = n / 2000 * 495
    audit += [line(34,y+23,label,21),box(210,y,round(w,2),28,"#226680"),line(round(225+w,2),y+22,f"{n:,}",20,True)]
audit += [line(34,378,f"B. Recorded assertions (n = {total:,})",25,True),
          box(34,400,968,36,"#dbe2e6"),box(34,400,round(968*backed/total,2),36,"#226680"),
          line(34,476,f"Backed: {backed:,} ({100*backed/total:.2f}%)",23,True),
          line(471,476,f"Not backed under the rule: {total-backed:,}",23),
          line(34,523,f"{stats['statuses']['reviewed']} independently reviewed entries; no human-backed assertions.",22)]
svg("inventory-audit.svg",556,"Canonical concepts and claim backing","Five concept class counts, then one bar for qualifying evidence across assertions. No entry was independently reviewed.",audit)
