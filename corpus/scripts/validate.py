#!/usr/bin/env python3
"""Offline structure, relationship, rights, completeness and checksum validation."""
import json
from pathlib import Path
import re
import sys
from acquire import ROOT, safe_path, verify_bytes


def validate(root=ROOT):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    def read(path):
        return json.loads((root / path).read_text(encoding='utf-8'))
    def keyed(rows, key, label, required):
        check(isinstance(rows, list), label + ': expected list')
        result = {}
        for row in rows:
            check(isinstance(row, dict), label + ': expected object')
            check(set(required) <= row.keys(), label + ': missing required fields')
            value = row.get(key)
            check(isinstance(value, str) and bool(value), label + ': invalid ID')
            check(value not in result, label + ': duplicate ID ' + str(value))
            result[value] = row
        return result
    try:
        sources = keyed(read('indexes/sources.json'), 'id', 'sources', ['id','record','status'])
        editions = {}
        for id, source in sources.items():
            d = read(source['record']); editions[id] = d
            check(d.get('id') == id, 'Source record ID mismatch: ' + id)
            for key in ['title','publication_year','contributors','languages','kind','catalog_urls','notes','acquisition_status','text_quality','review_date','asset_ids']:
                check(key in d, id + ': missing ' + key)
            check(d['catalog_urls'] and all(u.startswith('https://') for u in d['catalog_urls']), id + ': invalid catalog URLs')
            check(d['acquisition_status'] == source['status'], id + ': status mismatch')
        visuals = keyed(read('images/catalog.json'), 'id', 'visuals', ['id','title','catalog_url','image_rights','status','asset_id'])
        rights = keyed(read('metadata/rights.json'), 'source_id', 'rights', ['source_id','jurisdiction','status','basis','evidence','components','international','limitations','review_date'])
        for id in editions:
            check(id in rights, 'Missing rights: ' + id)
        for id,r in rights.items():
            check(id in editions or id in visuals, 'Unknown rights source: ' + id)
            check(r['status'] in {'public_domain','copyrighted_reference_only','CC0-1.0'}, 'Unknown rights status: ' + id)
            check(bool(r['evidence']), 'Missing rights evidence: ' + id)
            check(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['review_date'])), 'Bad review date: ' + id)
        assets = keyed(read('metadata/assets.json'), 'id', 'assets', ['id','source_id','path','url','kind','quality','tracked','review_date','status','bytes'])
        paths = set()
        for id,a in assets.items():
            check(a['source_id'] in rights, 'Asset without rights: ' + id)
            check(a['kind'] in {'ocr','transcription','facsimile','image','metadata'}, 'Bad asset kind: ' + id)
            check(type(a['tracked']) is bool, 'tracked must be boolean: ' + id)
            check(a['path'] not in paths, 'Duplicate asset path: ' + id); paths.add(a['path'])
            check(a['status'] in {'acquired','download_verified','remote_manifest_verified'}, 'Bad acquisition state: ' + id)
            check(a['bytes'] > 0, 'Empty asset: ' + id)
            check(bool(a.get('sha256') or a.get('upstream_checksum')), 'Missing checksum: ' + id)
            check(not a['tracked'] or bool(a.get('sha256')), 'Committed asset missing SHA-256: ' + id)
            if a.get('sha256'):
                check(bool(re.fullmatch('[a-f0-9]{64}',a['sha256'])), 'Invalid SHA-256: ' + id)
            check(a['url'] is None or a['url'].startswith('https://'), 'Bad acquisition URL: ' + id)
            if a['url'] is None:
                check(bool(a.get('generated_from')), 'Generated file missing inputs: ' + id)
                for dep in a.get('generated_from',[]):check(dep in assets,'Unknown input: '+dep)
            path = safe_path(root, a['path'])
            check(not a['tracked'] or path.is_file(), 'Missing committed asset: ' + id)
            if path.is_file():
                try: verify_bytes(a, path.read_bytes())
                except Exception as exc: errors.append(str(exc))
        for id,d in editions.items():
            check(set(d['asset_ids']) == {a['id'] for a in assets.values() if a['source_id']==id}, 'Edition asset inventory mismatch: '+id)
            if d['acquisition_status'] in {'pending_acquisition','linked_only'}:
                check(not d['asset_ids'], 'Pending/linked-only edition contains assets: '+id)
            else:
                check(bool(d['asset_ids']), 'Acquired edition has no assets: '+id)
        for id,v in visuals.items():
            if v['asset_id']:
                check(v['asset_id'] in assets, 'Unknown visual asset: '+id)
                check(id in rights, 'Acquired visual lacks rights: '+id)
        chars = keyed(read('indexes/characters.json'),'id','characters',['id','name','variants'])
        events = keyed(read('indexes/events.json'),'id','events',['id','label','character_ids','status'])
        passages = keyed(read('indexes/passages.json'),'id','passages',['id','event_ids','witnesses','adaptation_refs','uncertainty'])
        for character in chars.values():
            for variant in character['variants']:
                check(variant['source_id'] in editions, 'Unknown character variant source')
        for run in read('metadata/ocr-runs.json'):
            check(run['source_id'] in editions, 'Unknown OCR source')
            for key in ['input_asset_id','output_asset_id']:
                if key in run:check(run[key] in assets, 'Unknown OCR asset')
        for e in events.values():
            for id in e['character_ids']:check(id in chars,'Unknown character: '+id)
        for p in passages.values():
            for id in p['event_ids']:check(id in events,'Unknown event: '+id)
            for w in p['witnesses']:
                check(w['source_id'] in editions,'Unknown witness: '+w['source_id'])
                check(w['status'] in {'verified_text_location','unmapped'},'Unknown witness status')
                if w.get('asset_id'):
                    check(w['asset_id'] in assets,'Unknown witness asset')
                    a=assets[w['asset_id']];check(a['source_id']==w['source_id'],'Witness asset/source mismatch')
                    lines=(root/a['path']).read_text().splitlines()
                    start,end=w['lines'];check(1<=start<=end<=len(lines),'Invalid line range')
                    import hashlib
                    check(hashlib.sha256('\n'.join(lines[start-1:end]).encode()).hexdigest()==w['excerpt_sha256'],'Passage anchor checksum mismatch: '+p['id'])
            for a in p['adaptation_refs']:
                file=(root.parent/a['path']).resolve()
                check(file.is_relative_to(root.parent.resolve()) and file.is_file(),'Broken adaptation path')
                if file.is_file():
                    lines=file.read_text().splitlines();start,end=a['lines']
                    check(1<=start<=end<=len(lines),'Invalid adaptation line range')
                    import hashlib
                    check(hashlib.sha256('\n'.join(lines[start-1:end]).encode()).hexdigest()==a['excerpt_sha256'],'Adaptation anchor drift: '+p['id'])
        for r in read('metadata/relationships.json'):
            check(r['from'] in editions and r['to'] in editions,'Unknown edition relationship endpoint')
            check(r['evidence'] and r['certainty'] in {'verified','qualified'},'Missing relationship evidence/certainty')
        installments=keyed(read('metadata/guthrie-installments.json'),'id','installments',['id','source_id','volume','issue','date','pages','text_asset_id','facsimile_asset_id','catalog_url','verification'])
        check(len(installments)==14,'Expected 14 located Guthrie installments')
        for i in installments.values():
            check(i['source_id'] in editions,'Unknown serial source')
            check(i['text_asset_id'] in assets and i['facsimile_asset_id'] in assets,'Unknown installment asset')
            check(i['pages']['start']<=i['pages']['end'],'Invalid installment page range')
        # Local Markdown links, including links in the corpus guide and edition notes.
        for file in root.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)',file.read_text()):
                if '://' in target or target.startswith('#'):continue
                check((file.parent/target.split('#')[0]).exists(),f'Broken local Markdown link: {file}: {target}')
    except (KeyError, ValueError, TypeError, OSError) as exc:
        errors.append('Invalid metadata: ' + str(exc))
    return errors


if __name__ == '__main__':
    errors=validate()
    for error in errors:print('ERROR:',error)
    if not errors:print('PASS: metadata, unique IDs, relationships, rights, checksums, local links and acquisition states')
    sys.exit(bool(errors))
