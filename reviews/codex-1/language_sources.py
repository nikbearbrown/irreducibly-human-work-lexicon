"""Independent candidate joins to Glottolog 5.3. No fuzzy joins or dialect collapsing."""
import collections, csv, hashlib, json, pathlib, unicodedata
root=pathlib.Path(__file__).resolve().parent
path=root/'sources/glottolog-5.3.csv'
def norm(s): return unicodedata.normalize('NFC',s.strip()).casefold()
with path.open(encoding='utf-8',newline='') as f:
    data=list(csv.DictReader(f))
by_id={r['ID']:r for r in data}
index=collections.defaultdict(list)
for x in data: index[norm(x['Name'])].append(x)
result={}
collisions={}
for row in json.loads((root/'inventory.json').read_text())['entries']:
    if row['original_kind']!='human-language': continue
    hits=index[norm(row['label'])]
    if not hits: continue
    if len(hits)!=1 or hits[0]['Level']!='language':
        collisions[row['id']]=[dict(name=h['Name'],code=h['ID'],level=h['Level']) for h in hits]
        continue
    h=hits[0]
    fam=by_id.get(h['Family_ID'],{}).get('Name')
    result[row['id']]=dict(match='unique-exact-label-type',glottocode=h['Glottocode'],catalog_name=h['Name'],
                          iso639_3=h['ISO639P3code'] or None,macroarea=h['Macroarea'] or None,
                          catalog_family=fam,ref='https://glottolog.org/resource/languoid/id/'+h['Glottocode'],
                          evidence_scope='catalog identity and fields only; not an audit of the independent definition or example')
out=dict(version='5.3',source='https://github.com/glottolog/glottolog-cldf/releases/tag/v5.3',
         author='Harald Hammarström, Robert Forkel, Martin Haspelmath, and Sebastian Bank (2026)',license='CC BY 4.0',sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
         matches=result,ambiguous_or_nonlanguage=collisions)
p=root/'sources'/'human-language-links.json'
tmp=p.with_suffix('.tmp')
tmp.write_text(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
tmp.replace(p)
print('Unique exact language name links:',len(result),'ambiguous or non-language records:',len(collisions))
