"""Regression tests for the protections that keep the research record trustworthy."""
import json
import io
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from acquire import ROOT, download, safe_path, main
from validate import validate

class CorpusChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.repo=Path(self.tmp.name)
        self.root=self.repo/'corpus'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','*.pdf'))
        for p in ROOT.parent.glob('book-*.md'):shutil.copyfile(p,self.repo/p.name)
    def tearDown(self):self.tmp.cleanup()
    def alter(self,path,fn):
        p=self.root/path;data=json.loads(p.read_text());fn(data);p.write_text(json.dumps(data))
    def test_valid_corpus(self):self.assertEqual([],validate(self.root))
    def test_duplicate_id_rejected(self):
        self.alter('indexes/sources.json',lambda rows:rows.append(rows[0]))
        self.assertTrue(any('duplicate' in e for e in validate(self.root)))
    def test_corrupt_text_rejected(self):
        with (self.root/'sources/transcriptions/spence-1908-gutenberg.txt').open('ab') as f:f.write(b'corrupt')
        self.assertTrue(any('mismatch' in e for e in validate(self.root)))
    def test_missing_rights_rejected(self):
        self.alter('metadata/rights.json',lambda rows:rows.pop(0))
        self.assertTrue(any('rights' in e for e in validate(self.root)))
    def test_dangling_witness_rejected(self):
        self.alter('indexes/passages.json',lambda rows:rows[0]['witnesses'][0].update(source_id='nonexistent'))
        self.assertTrue(any('witness' in e.lower() for e in validate(self.root)))
    def test_missing_committed_asset_rejected(self):
        (self.root/'sources/transcriptions/spence-1908-gutenberg.txt').unlink()
        self.assertTrue(validate(self.root))
    def test_false_completeness_rejected(self):
        self.alter('metadata/guthrie-installments.json',lambda rows:rows.pop())
        self.assertTrue(any('14 located' in e for e in validate(self.root)))
    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):safe_path(self.root,'../../escape')
    def test_bad_download_not_installed(self):
        a=next(a for a in json.loads((self.root/'metadata/assets.json').read_text()) if a['id']=='ximenez-pdf')
        with patch('acquire.fetch',return_value=b'<html>error</html>'):
            with self.assertRaises(RuntimeError):download(a,self.root)
        self.assertFalse((self.root/a['path']).exists())
    def test_all_selects_only_remote_assets(self):
        assets=json.loads((self.root/'metadata/assets.json').read_text())
        generated=[a for a in assets if not a['url']]
        self.assertTrue(generated)
        for a in generated:(self.root/a['path']).unlink()
        def remote_only(asset):
            if not asset['url']:
                raise ValueError('Generated file must not be selected by --all')
            return 'downloaded and verified'
        with patch('acquire.ROOT',self.root), patch('sys.argv',['acquire.py','--all']), \
                patch('acquire.download',side_effect=remote_only) as downloader, \
                patch('sys.stdout',new_callable=io.StringIO), patch('sys.stderr',new_callable=io.StringIO):
            self.assertEqual(0,main())
        self.assertEqual(
            [a['id'] for a in assets if a['url']],
            [call.args[0]['id'] for call in downloader.call_args_list])
    def test_explicit_missing_generated_asset_reports_reproduction(self):
        assets=json.loads((self.root/'metadata/assets.json').read_text())
        generated=next(a for a in assets if not a['url'])
        (self.root/generated['path']).unlink()
        with patch('acquire.ROOT',self.root), \
                patch('sys.argv',['acquire.py','--id',generated['id']]), \
                patch('acquire.download',side_effect=lambda a:download(a,self.root)), \
                patch('acquire.fetch') as fetcher, \
                patch('sys.stderr',new_callable=io.StringIO) as stderr:
            self.assertEqual(1,main())
        fetcher.assert_not_called()
        self.assertIn('reproduce using its documented provenance',stderr.getvalue())
    def test_existing_corrupt_file_not_overwritten(self):
        a=next(a for a in json.loads((self.root/'metadata/assets.json').read_text()) if a['id']=='spence-txt')
        p=self.root/a['path'];p.write_bytes(b'local changes')
        with self.assertRaises(ValueError):download(a,self.root)
        self.assertEqual(b'local changes',p.read_bytes())
    def test_manuscript_url_sequence_mismatch_rejected(self):
        self.alter('metadata/ximenez-folios.json',lambda d:d['records'][0].update(image_sequence=34))
        self.assertTrue(any('URL/sequence mismatch' in e for e in validate(self.root)))
    def test_duplicate_folio_rejected(self):
        self.alter('metadata/ximenez-folios.json',lambda d:d['records'][1].update(folio=d['records'][0]['folio']))
        self.assertTrue(any('Duplicate folio' in e for e in validate(self.root)))
    def test_dangling_manuscript_witness_rejected(self):
        def change(rows):
            w=next(w for p in rows for w in p['witnesses'] if w['status']=='verified_image_location')
            w['manuscript']['folio_map_id']='missing'
        self.alter('indexes/passages.json',change)
        self.assertTrue(any('Unknown witness folio' in e for e in validate(self.root)))
    def test_independent_review_cannot_be_asserted_without_schema_extension(self):
        self.alter('metadata/transcriptions.json',lambda rows:rows[0].update(reviewer_status='independently_verified'))
        self.assertTrue(any('Unsupported transcription review' in e for e in validate(self.root)))
    def test_normalization_requires_record(self):
        self.alter('metadata/transcriptions.json',lambda rows:rows[0].update(normalized_working_text='modern spelling'))
        self.assertTrue(any('Normalization without' in e for e in validate(self.root)))
    def test_transcription_requires_facsimile_provenance(self):
        def change(rows):
            next(a for a in rows if a['id']=='ximenez-conception')['generated_from']=['scherzer-txt']
        self.alter('metadata/assets.json',change)
        self.assertTrue(any('Diplomatic input provenance' in e for e in validate(self.root)))
    def test_transcription_anchor_corruption_rejected(self):
        def change(rows):
            w=next(w for p in rows for w in p['witnesses'] if w.get('transcription_id'))
            w['excerpt_sha256']='0'*64
        self.alter('indexes/passages.json',change)
        self.assertTrue(any('Passage anchor checksum mismatch' in e for e in validate(self.root)))
    def test_invalid_alignment_rejected(self):
        def change(rows):
            w=next(w for p in rows for w in p['witnesses'] if w.get('alignment_type'))
            w['alignment_type']='exact_by_guess'
        self.alter('indexes/passages.json',change)
        self.assertTrue(any('Invalid alignment type' in e for e in validate(self.root)))

if __name__=='__main__':unittest.main()
