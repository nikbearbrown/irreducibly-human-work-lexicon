import collections, io, json, pathlib, subprocess, tarfile
ROOT=pathlib.Path(__file__).resolve().parent
REPO=ROOT.parent.parent
REV='91312fec957388afe4d1dfbdb4aff2707588b9a1'
SOURCES={'abilities/onet-abilities.json':('abilities','ability'),
         'onet-skills/onet-skills.json':('skills','skill'),
         'onet-knowledge/onet-knowledge.json':('knowledge','knowledge')}
LANG={'human-language','programming-language','markup-language','style-language','modeling-language'}
SKILL={'skill','work-activity','tool','platform','framework','library','method','standard'}
def write(path,data):
    f=ROOT/path
    payload=json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if f.exists():
        assert f.read_text()==payload, f
    else:
        f.write_text(payload)
def main():
    archive=subprocess.check_output(['git','-C',str(REPO),'archive',REV,'entries',*SOURCES])
    inventory=[]
    onet={}
    with tarfile.open(fileobj=io.BytesIO(archive)) as t:
        for p,(group,kind) in SOURCES.items():
            for x in json.load(t.extractfile(p))[group]:
                onet[x['element_id']]=dict(x,kind=kind,path=p,release='30.2')
        for row in sorted(t.getmembers(),key=lambda x:x.name):
            if not row.isfile() or not row.name.startswith('entries/') or not row.name.endswith('.json'): continue
            e=json.load(t.extractfile(row))
            kind=e['kind']
            c='language' if kind in LANG else 'skill' if kind in SKILL else kind
            assert c in {'ability','knowledge','language','skill','credential'}, (c,row.name)
            ids=[x for x in e.get('identifiers',[]) if x.get('scheme')=='onet-element']
            inventory.append(dict(id=e['id'],key=pathlib.PurePath(row.name).stem,label=e['preferred_name'],original_kind=kind,broad_class=c,onet_codes=[x['code'] for x in ids]))
    assert len(inventory)==len({x['id'] for x in inventory})==3754
    counts=dict(collections.Counter(x['broad_class'] for x in inventory))
    assert counts=={'ability':67,'knowledge':550,'language':290,'skill':1988,'credential':859}, counts
    write('inventory.json',dict(commit=REV,counts=counts,entries=inventory))
    write('sources/onet-30.2.json',onet)
    covered=set()
    for kind in ('ability','knowledge','language','skill'):
        rows=[x for x in inventory if x['broad_class']==kind]
        keep=[]
        for x in rows:
            matches=[onet[c] for c in x['onet_codes'] if c in onet and onet[c]['kind']==x['original_kind'] and onet[c]['name'].casefold()==x['label'].casefold()]
            if len(matches)==1: covered.add(x['id'])
            else: keep.append(x)
        for i in range(0,len(keep),40):
            write(f'batches/{kind}-{i//40+1:03d}.json',keep[i:i+40])
    print(counts,'exact O*NET links:',len(covered))
if __name__=='__main__': main()
