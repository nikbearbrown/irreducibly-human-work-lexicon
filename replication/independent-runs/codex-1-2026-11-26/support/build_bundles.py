import collections, glob, json, pathlib, sys
d=pathlib.Path(__file__).parent
sys.path.insert(0,str(d/'scripts'))
from assemble_bundles import neighbors, broad_class
rows=[k.split('\t') for k in pathlib.Path('queue.tsv').read_text().splitlines()]
entries=[json.loads(f.read_text()) for f in sorted((pathlib.Path(sys.argv[3])).glob('*.json'))]
by_id={e['id']:e for e in entries}
by_name=collections.defaultdict(list)
for e in entries:
    for n in [e['preferred_name'],*[v['label'] for v in e.get('variants',[])]]:
        by_name[n.lower()].append(e['id'])
def bundle(row):
    cid,name,_=row
    e=by_id[cid]
    assert name==e['preferred_name']
    c=dict(id=cid,preferred_name=name,kind=e['kind'],broad_class=broad_class(e['kind']),
      variants=[{k:v[k] for k in ('label','needs_context','ambiguous') if k in v} for v in e.get('variants',[])],
      relations=[dict(type=r['type'],target=r['target'],target_name=by_id.get(r['target'],{}).get('preferred_name')) for r in e.get('relations',[])])
    return dict(concept_id=cid,concept=c,neighbors=neighbors(e,entries,by_id,by_name,[],'',n=20),wikipedia=[],wikidata=[],wordnet=[],examples=[])
start,end=map(int,sys.argv[1:3])
dest=pathlib.Path(f'bundles-{start+1:04d}-{end:04d}.jsonl')
with dest.open('x') as f:
    for row in rows[start:end]:
        f.write(json.dumps(bundle(row),ensure_ascii=False)+'\n')
print(dest)
