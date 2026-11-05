"""Regression tests for the protections that keep the research record trustworthy."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from acquire import ROOT, download, safe_path
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
    def test_existing_corrupt_file_not_overwritten(self):
        a=next(a for a in json.loads((self.root/'metadata/assets.json').read_text()) if a['id']=='spence-txt')
        p=self.root/a['path'];p.write_bytes(b'local changes')
        with self.assertRaises(ValueError):download(a,self.root)
        self.assertEqual(b'local changes',p.read_bytes())

if __name__=='__main__':unittest.main()
