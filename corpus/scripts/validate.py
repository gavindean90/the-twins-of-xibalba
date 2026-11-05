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
        # Selected manuscript observations are distinct from text anchors.
        sequence = {i['sequence']: i['url'] for i in read('metadata/ximenez-image-sequence.json')['images']}
        folio_doc = read('metadata/ximenez-folios.json')
        check(folio_doc['schema_version'] == 1, 'Unknown folio schema version')
        folios = keyed(folio_doc['records'], 'id', 'folios',
                       ['id','source_id','facsimile_asset_id','image_sequence','image_url',
                        'pdf_page','folio','columns','event_ids','review','uncertainty'])
        seen_images, seen_folios = set(), set()
        review_status = 'agent_image_checked_not_independently_reviewed'
        for id, f in folios.items():
            check(f['source_id'] == folio_doc['source_id'] == 'ximenez-ms', 'Folio source mismatch')
            asset = assets.get(f['facsimile_asset_id'], {})
            check(asset.get('kind') == 'facsimile' and asset.get('source_id') == f['source_id'], 'Invalid folio facsimile')
            n = f['image_sequence']
            check(type(n) is int and n in sequence, 'Unknown manuscript image sequence')
            check(f['image_url'] == sequence.get(n), 'Manuscript image URL/sequence mismatch')
            check(n not in seen_images, 'Duplicate manuscript image'); seen_images.add(n)
            check(type(f['pdf_page']) is int and 1 <= f['pdf_page'] <= len(sequence), 'Invalid manuscript PDF page')
            mark = f['folio']
            check(type(mark['number']) is int and mark['number'] > 0 and mark['side'] in {'r','v'}, 'Invalid folio reference')
            pair = (mark['number'], mark['side'])
            check(pair not in seen_folios, 'Duplicate folio reference'); seen_folios.add(pair)
            check(mark['status'] == 'image_checked' and bool(mark['visible_mark']) and bool(mark['basis']), 'Missing folio observation evidence')
            check(f['columns'] == {'left':'quc','right':'es'}, 'Unexpected manuscript column assignment')
            check(f['review']['status'] == review_status and bool(f['review']['method']), 'Unsupported manuscript review status')
            for event in f['event_ids']:check(event in events, 'Unknown folio event')
        transcriptions = keyed(read('metadata/transcriptions.json'), 'id', 'transcriptions',
                               ['id','source_id','folio_map_id','column','diplomatic_asset_id',
                                'normalized_working_text','transformations','english_research_gloss',
                                'method','reviewer_status','uncertain_readings','region_pdf_points'])
        for id, t in transcriptions.items():
            f = folios.get(t['folio_map_id'], {})
            a = assets.get(t['diplomatic_asset_id'], {})
            check(bool(f) and t['source_id'] == f.get('source_id'), 'Unknown transcription folio/source')
            check(a.get('kind') == 'transcription' and a.get('source_id') == t['source_id'], 'Invalid diplomatic asset')
            check(f.get('facsimile_asset_id') in a.get('generated_from', []), 'Diplomatic input provenance missing')
            check(t['column'] in {'left','right'}, 'Invalid transcription column')
            check(t['reviewer_status'] == review_status, 'Unsupported transcription review status')
            check(bool(t['method']) and bool(t['english_research_gloss']) and isinstance(t['uncertain_readings'], list), 'Incomplete transcription record')
            check(isinstance(t['transformations'], list), 'Invalid normalization transformations')
            if t['normalized_working_text'] is None:
                check(not t['transformations'], 'Transformations without normalized text')
            else:
                check(bool(t['transformations']), 'Normalization without transformation record')
            box = t['region_pdf_points']
            check(len(box) == 4 and all(isinstance(v, (int,float)) for v in box)
                  and 0 <= box[0] < box[2] and 0 <= box[1] < box[3], 'Invalid transcription region')
        for p in passages.values():
            for id in p['event_ids']:check(id in events,'Unknown event: '+id)
            for w in p['witnesses']:
                check(w['source_id'] in editions,'Unknown witness: '+w['source_id'])
                check(w['status'] in {'verified_text_location','verified_image_location','unmapped'},'Unknown witness status')
                if 'alignment_type' in w:
                    check(w['alignment_type'] in {'close_textual','episode','interpretive','unmapped'}, 'Invalid alignment type')
                    check(w.get('confidence') in {'low','medium','high'}, 'Invalid alignment confidence')
                if w['status'] == 'verified_image_location':
                    check(w.get('asset_id') is None, 'Image witness must not masquerade as text asset')
                    f = folios.get(w.get('manuscript', {}).get('folio_map_id'), {})
                    check(bool(f) and f.get('source_id') == w['source_id'], 'Unknown witness folio/source')
                    check(bool(set(p['event_ids']) & set(f.get('event_ids', []))), 'Witness/folio event mismatch')
                    check(w.get('manuscript', {}).get('column') in {'left','right','both'}, 'Invalid witness column')
                if w['status'] == 'verified_text_location':
                    check(bool(w.get('asset_id')), 'Verified text witness missing asset')
                if w.get('transcription_id'):
                    t = transcriptions.get(w['transcription_id'], {})
                    check(bool(t) and t.get('diplomatic_asset_id') == w.get('asset_id'), 'Unknown witness transcription/asset')
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
