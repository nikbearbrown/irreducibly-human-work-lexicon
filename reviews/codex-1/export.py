"""Build shareable Codex 1 archive after all expected records have a packet."""
import argparse, csv, hashlib, io, json, pathlib, sys, zipfile
ROOT=pathlib.Path(__file__).resolve().parent
def load(p): return json.loads((ROOT/p).read_text())
def safe_cell(v):
    v=str(v or '')
    return "'"+v if v.lstrip().startswith(('=','+','-','@','\t','\r')) else v
def main():
    p=argparse.ArgumentParser()
    p.add_argument('output',type=pathlib.Path)
    args=p.parse_args()
    s=load('verification.json')
    e=load('entries.json')
    assert s['pending']==0 and len(e)==s['entry_packets']==2895 and len({x['id'] for x in e})==len(e)
    assert len({x['key'] for x in e})==len(e)
    assert all(x['entry_text'] for x in e)
    temp=args.output.with_suffix('.tmp')
    assert not args.output.exists() and not temp.exists()
    fields=['id','key','label','broad_class','original_kind','entry_text_kind','entry_text','example','verification','source_urls','sense_note']
    f=io.StringIO(newline='')
    w=csv.DictWriter(f,fieldnames=fields,lineterminator="\n");w.writeheader()
    for x in e:
        v={k:x.get(k,'') for k in fields}
        v['source_urls']=' | '.join(dict.fromkeys([y.get('url') or y.get('ref') for y in x.get('sources',[])] +
                                                  x.get('sense_proposal',{}).get('refs',[]) +
                                                  ([x['catalog_identity_evidence']['ref']] if x.get('catalog_identity_evidence') else [])))
        w.writerow({k:safe_cell(y) for k,y in v.items()})
    with zipfile.ZipFile(temp,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in ['README.md','DRAFTING.md','inventory.py','assemble.py','language_sources.py','export.py','entries.json','verification.json','review-queue.json','inventory.json']:
            z.write(ROOT/p,'codex-1/'+p)
        for kind in ('batches','drafts','review','sources'):
            for p in sorted((ROOT/kind).iterdir()):
                if p.is_file() and p.suffix in {'.json','.md','.csv','.tsv'}:
                    z.write(p,'codex-1/'+str(p.relative_to(ROOT)))
        z.writestr('codex-1/entries.csv',f.getvalue().encode('utf-8-sig'))
        summary=['# Codex 1 coverage and evidence','','Frozen main: `'+s['snapshot']+'`.',
                 'The entries are an independent working set, not changes to canon or human-reviewed claims.','',
                 '| Class | Concept packets | Definitions | Proposed source text | Disambiguation records |',
                 '|---|---:|---:|---:|---:|']
        for cl,c in sorted(s['coverage'].items()):
            summary.append(f"| {cl} | {c['inventory']} | {c.get('definitions',0)} | {c.get('source-proposed-definition_text',0)} | {c.get('disambiguation_text',0)} |")
        summary += ['',f"Exactly {len(e):,} distinct IDs, with {s['credentials_outside_listed_classes']:,} credentials outside the four requested classes.",
                    'Entries use the original stable ID but preserve the independent text and separately record source evidence.',
                    'A checked sample does not establish accuracy across the corpus. Read verification.json and the per-claim scope.',
                    'Catalog identity links are not definition verification. A disambiguation row documents why a single definition was not asserted.',
                    'Start with entries.csv or the individual entries JSON files.']
        z.writestr('codex-1/SUMMARY.md','\n'.join(summary)+'\n')
        for x in e:
            key=x['key']
            assert '/' not in key and '\\' not in key and key not in ('.','..')
            z.writestr('codex-1/entries/'+key+'.json',json.dumps(x,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    with zipfile.ZipFile(temp) as z:
        assert z.testzip() is None
        individual=[n for n in z.namelist() if n.startswith('codex-1/entries/')]
        assert len(individual)==len(e)
        assert set(x['id'] for x in e)=={json.loads(z.read(n))['id'] for n in individual}
    temp.replace(args.output)
    print(args.output, args.output.stat().st_size, hashlib.sha256(args.output.read_bytes()).hexdigest())
if __name__=='__main__': sys.exit(main())
