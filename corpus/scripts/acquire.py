#!/usr/bin/env python3
"""Download reviewed assets, verify pinned checksums, then atomically install them."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def safe_path(root, relative):
    p = (root / relative).resolve()
    if not p.is_relative_to(root.resolve()):
        raise ValueError('Path escapes corpus: ' + relative)
    return p


def verify_bytes(asset, data):
    if len(data) != asset['bytes']:
        raise ValueError('Size mismatch: ' + asset['id'])
    if asset.get('sha256') and hashlib.sha256(data).hexdigest() != asset['sha256']:
        raise ValueError('SHA-256 mismatch: ' + asset['id'])
    upstream = asset.get('upstream_checksum')
    if upstream and hashlib.new(upstream['algorithm'], data).hexdigest() != upstream['value']:
        raise ValueError('Upstream checksum mismatch: ' + asset['id'])
    if not asset.get('sha256') and not upstream:
        raise ValueError('Unpinned asset: ' + asset['id'])
    if asset['kind'] == 'facsimile' and not data.startswith(b'%PDF-'):
        raise ValueError('Expected PDF: ' + asset['id'])
    if asset['kind'] in {'ocr', 'transcription'}:
        data.decode('utf-8')
        if b'<html' in data[:500].lower():
            raise ValueError('HTML instead of text: ' + asset['id'])


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'TwinsOfXibalbaCorpus/1.0'})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def download(asset, root=ROOT):
    target = safe_path(root, asset['path'])
    if target.exists():
        verify_bytes(asset, target.read_bytes())
        return 'already verified'
    if not asset.get('url'):
        raise ValueError('Generated file; reproduce using its OCR instructions')
    urls = [asset['url']]
    error = None
    # IA's public front end sometimes returns 503. Resolve its current storage
    # server through the public item API; never persist that server as the sole URL.
    for attempt in range(3):
        try:
            data = fetch(urls[-1])
            verify_bytes(asset, data)
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as tmp:
                staging = Path(tmp.name)
                tmp.write(data)
            try:
                staging.replace(target)
            finally:
                staging.unlink(missing_ok=True)
            return 'downloaded and verified'
        except Exception as exc:
            error = exc
            if attempt == 0 and asset['url'].startswith('https://archive.org/download/'):
                _, rest = asset['url'].split('/download/', 1)
                item, name = rest.split('/', 1)
                try:
                    metadata = json.loads(fetch('https://archive.org/metadata/' + item))
                    urls.append('https://' + metadata['d1'] + metadata['dir'] + '/' + name)
                except Exception:
                    pass
    raise RuntimeError(str(error))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--id', action='append', default=[], help='Asset ID; repeatable')
    parser.add_argument('--all', action='store_true', help='All remote assets (large download)')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    assets = json.loads((ROOT / 'metadata/assets.json').read_text())
    rights = {r['source_id']: r for r in json.loads((ROOT / 'metadata/rights.json').read_text())}
    if args.list or not (args.id or args.all):
        for a in assets:
            print(a['id'], a['status'], a['bytes'], a['path'])
        return 0
    unknown = set(args.id) - {a['id'] for a in assets}
    if unknown:
        parser.error('Unknown asset IDs: ' + ', '.join(sorted(unknown)))
    failures = 0
    for a in assets:
        if not (args.all or a['id'] in args.id):
            continue
        if rights[a['source_id']]['status'] not in {'public_domain', 'CC0-1.0'}:
            print('BLOCKED by rights manifest:', a['id'], file=sys.stderr)
            failures += 1
            continue
        try:
            print(a['id'] + ': ' + download(a))
        except Exception as exc:
            print(a['id'] + ': FAILED: ' + str(exc), file=sys.stderr)
            failures += 1
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
