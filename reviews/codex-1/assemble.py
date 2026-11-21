import argparse, collections, csv, hashlib, json, pathlib, re, sys
ROOT=pathlib.Path(__file__).resolve().parent
OFFICIAL='https://www.onetcenter.org/dl_files/database/db_30_2_text/Content%20Model%20Reference.txt'
DICT='https://www.onetcenter.org/dictionary/30.2/text/content_model_reference.html'
def load(p): return json.loads((ROOT/p).read_text())
def save(path,data):
    p=ROOT/path
    tmp=p.with_name(p.name+'.tmp')
    tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    tmp.replace(p)
def norm(text): return ' '.join(text.split())
def onet_matches(row, onet):
    return [onet[c] for c in row['onet_codes'] if c in onet and onet[c]['kind']==row['original_kind'] and onet[c]['name'].casefold()==row['label'].casefold()]
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--require-complete',action='store_true')
    ap.add_argument('--require-coverage',action='store_true')
    args=ap.parse_args()
    inv=load('inventory.json')
    rows={e['id']:e for e in inv['entries'] if e['broad_class']!='credential'}
    onet=load('sources/onet-30.2.json')
    language_data=load('sources/human-language-links.json') if (ROOT/'sources/human-language-links.json').exists() else {'matches':{},'ambiguous_or_nonlanguage':{}}
    proposals={}
    for name in ('language','skill'):
        proposals_file=ROOT/f'sources/{name}-sense-proposals.json'
        if not proposals_file.is_file(): continue
        for p in json.loads(proposals_file.read_text()):
            assert p['id'] not in proposals and p['id'] in rows and p['label']==rows[p['id']]['label'], p
            assert p['ambiguity_note'] and p['refs'] and all(ref.startswith('https://') for ref in p['refs']), p
            proposals[p['id']]=p
    official={}
    source_sha=None
    source=ROOT/'sources/onet-30.2-official.tsv'
    if source.is_file():
        payload=source.read_bytes()
        source_sha=hashlib.sha256(payload).hexdigest()
        for line in payload.decode('utf-8-sig').splitlines():
            fields=line.split('\t',2)
            if len(fields)==3 and re.fullmatch(r'[0-9](?:\.[0-9A-Za-z]+)*',fields[0]):
                assert fields[0] not in official, fields[0]
                official[fields[0]]=fields[1:]
        assert len(official)>=600, len(official)
    work_styles={norm(v[0]).casefold():(k,v[0]) for k,v in official.items() if k.startswith('1.D.') and k.count('.')==3}
    defs={}
    reviews={}
    finding_files=sorted((ROOT/'review').glob('*.json'))
    for p in finding_files:
        data=json.loads(p.read_text())
        for a in data:
            assert a['id'] in rows and a['id'] not in reviews, (p,a)
            assert a['result'] in {'supports','partial','contradicts','unconfirmed'}, (p,a)
            assert a.get('ref','').startswith('https://') and a.get('note'), (p,a)
            reviews[a['id']]=dict(a,packet=p.name)
    for k,row in rows.items():
        matches=onet_matches(row,onet)
        if len(matches)!=1: continue
        m=matches[0]
        code=m['element_id']
        if official:
            val=official[code]
            assert norm(val[0])==norm(m['name']) and norm(val[1])==norm(m['definition']), (code,val,m)
        defs[k]=dict(definition=m['definition'],example=None,sense_note=None,
                     origin='onet-30.2-source-definition',verification='official-exact' if official else 'pinned-export-exact',
                     sources=[dict(url=OFFICIAL if official else DICT,element_id=code,release='30.2',snapshot_path=m['path'],
                                   license='CC BY 4.0',attribution='U.S. Department of Labor, Employment and Training Administration')])
    expected_batch_ids=set()
    complete_batches=[]
    missing_batches=[]
    for p in sorted((ROOT/'batches').glob('*.json')):
        ids=[x['id'] for x in json.loads(p.read_text())]
        assert not (set(ids)&expected_batch_ids)
        assert not set(ids)&set(defs), p.name
        expected_batch_ids.update(ids)
        draft=ROOT/'drafts'/p.name
        if not draft.is_file():
            missing_batches.append(p.name)
            continue
        data=json.loads(draft.read_text())
        assert [x['id'] for x in data]==ids, p.name
        complete_batches.append(p.name)
        for a in data:
            assert set(a)=={'id','definition','example','sense_note'}, (p.name,a)
            for f in ('definition','example','sense_note'):
                assert a[f] is None or (isinstance(a[f],str) and a[f].strip()==a[f] and a[f] and len(a[f])<=1300), (p.name,a)
            assert a['definition'] is not None or a['sense_note'], (p.name,a)
            key=a['id']
            r=reviews.get(key)
            verification={'supports':'source-checked','partial':'partially-supported','contradicts':'contradicted','unconfirmed':'not-confirmed'}.get(r['result'],'draft-unchecked') if r else 'draft-unchecked'
            defs[key]=dict(definition=a['definition'],example=a['example'],sense_note=a['sense_note'],
                           origin='codex-1-independent-draft',batch=p.name,verification=verification,sources=[r] if r else [])
    assert set(rows)==expected_batch_ids|{k for k,v in defs.items() if v['origin']=='onet-30.2-source-definition'}
    assert set(reviews)<=set(defs)
    coverage=collections.defaultdict(collections.Counter)
    entries=[]
    duplicates=collections.defaultdict(list)
    for key,row in sorted(rows.items(),key=lambda pair:(pair[1]['broad_class'],pair[1]['key'])):
        d=defs.get(key)
        c=coverage[row['broad_class']]
        c['inventory']+=1
        if not d:
            c['pending']+=1; continue
        c[d['verification']]+=1
        c['definitions' if d['definition'] else 'unresolved']+=1
        if d['definition']:
            duplicates[norm(d['definition']).casefold()].append(key)
        entry=dict(row,**d,run='Codex 1',canonical_snapshot=inv['commit'],review_status='not-human-reviewed')
        if key in language_data['matches']:
            entry['catalog_identity_evidence']=language_data['matches'][key]
            c['catalog_identity_links']+=1
            ident=entry['catalog_identity_evidence']
            code=f" (ISO 639-3: {ident['iso639_3']})" if ident['iso639_3'] else ''
            family=f" under the {ident['catalog_family']} grouping" if ident['catalog_family'] else ''
            entry['catalog_description']=f"Glottolog catalogs {ident['catalog_name']}{code} as a language{family}."
        if key in language_data['ambiguous_or_nonlanguage']:
            entry['catalog_identity_candidates']=language_data['ambiguous_or_nonlanguage'][key]
        if key in proposals:
            entry['sense_proposal']=proposals[key]
        if row['broad_class']=='ability' and norm(row['label']).casefold() in work_styles:
            code,name=work_styles[norm(row['label']).casefold()]
            entry['classification_check']=dict(result='alternate-category-in-source',source_category='O*NET Work Styles',
                                                name=name,element_id=code,url=OFFICIAL,
                                                note='Exact label in a different source category. Check whether the intended sense is a work style or a distinct ability.')
        entry['entry_text']=d['definition']
        entry['entry_text_kind']='definition' if d['definition'] else 'disambiguation'
        if not d['definition']:
            if key in proposals and proposals[key]['proposed_definition']:
                entry['entry_text']=proposals[key]['proposed_definition']
                entry['entry_text_kind']='source-proposed-definition'
            elif key in proposals:
                entry['entry_text']=proposals[key]['ambiguity_note']
            else:
                entry['entry_text']=d['sense_note']
        assert entry['entry_text']
        c[entry['entry_text_kind']+'_text']+=1
        entries.append(entry)
    ids={p['id']:p for p in entries}
    for key,kind,code in [('v2tu54uao9','skill','2.A.1.e'),('so9zp6tzyh','knowledge','2.C.4.a'),('thsmk1q1kl','skill','2.B.1.f')]:
        x=ids[key]
        assert x['broad_class']==kind and x['sources'][0]['element_id']==code, x
    assert ids['v2tu54uao9']['definition']!=ids['so9zp6tzyh']['definition']
    assert 'help people' in ids['thsmk1q1kl']['definition'].lower()
    save('entries.json',entries)
    stats=dict(snapshot=inv['commit'],run='Codex 1',coverage={k:dict(v) for k,v in coverage.items()},
               entry_packets=len(entries),definitions=sum(c['definitions'] for c in coverage.values()),
               unresolved=sum(c['unresolved'] for c in coverage.values()),pending=sum(c['pending'] for c in coverage.values()),
               credentials_outside_listed_classes=inv['counts']['credential'],
               complete_batches=complete_batches,missing_batches=missing_batches,source_sha256=source_sha,
               identical_definition_groups=[ids for ids in duplicates.values() if len(ids)>1])
    save('verification.json',stats)
    duplicate_ids={i for ids in stats['identical_definition_groups'] for i in ids}
    save('review-queue.json',[{k:e.get(k) for k in ('id','key','label','broad_class','definition','sense_note','verification','catalog_identity_evidence','catalog_identity_candidates','sense_proposal','classification_check')}
                             | {'priority':'unresolved' if not e['definition'] else 'duplicate-definition' if e['id'] in duplicate_ids else 'sense-or-source'}
                             for e in entries if not e['definition'] or e['sense_note'] or e['id'] in duplicate_ids or e['verification']=='contradicted' or e.get('classification_check')])
    print(json.dumps({k:v for k,v in stats.items() if k not in ('complete_batches','missing_batches','identical_definition_groups')},indent=2))
    if args.require_coverage and stats['pending']:
        return 2
    if args.require_complete and (stats['pending'] or stats['unresolved'] or not source_sha):
        return 2
    return 0
if __name__=='__main__':sys.exit(main())
