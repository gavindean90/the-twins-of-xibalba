# Public-domain Popol Vuh research corpus

A working source collection for *The Twins of Xibalba*, reviewed **2026-11-04** under United States copyright law. Historical witnesses, translations, retellings and the original poem remain distinct. Nothing in this corpus changes the seven published books or their literary form.

## Start here

1. Read [the source inventory](INVENTORY.md), then open a record in [the source index](indexes/sources.json).
2. Read searchable historical texts in `sources/transcriptions/` and `sources/ocr/`. OCR is provisional, not a verified K’iche’ transcription.
3. Inspect [rights](metadata/rights.json) and [asset provenance/checksums](metadata/assets.json) before reusing a file.
4. Use [passages](indexes/passages.json), [events](indexes/events.json) and [characters](indexes/characters.json) as a seed concordance. Most manuscript and stanza mappings remain deliberately unmapped.
5. Download scans when needed with the commands below. No personal account, hosted database or private service is required.

## Commands

Run from the repository root with Python 3.10 or newer; validation and downloading use only the standard library:

```sh
python3 corpus/scripts/validate.py
python3 -m unittest discover -s corpus/scripts -p 'test_*.py'
python3 corpus/scripts/acquire.py --list
python3 corpus/scripts/acquire.py --id ximenez-pdf --id scherzer-pdf --id brasseur-pdf
python3 corpus/scripts/acquire.py --id word-1906-05-pdf
# Optional: all eligible remote assets; several hundred megabytes
python3 corpus/scripts/acquire.py --all
```

Downloads are atomic, hash checked and retained under `sources/scans/`, which Git ignores. The script refuses to overwrite a mismatching local file. Each failed download is reported; other requested assets continue. An Internet Archive fallback resolves its current storage server from the public metadata API. A provider changing bytes requires review and a new checksum, not bypassing verification. SHA-256 identifies every committed source file and every locally verified scan; archive SHA-1 additionally pins remote issue scans not downloaded in this build. `remote_manifest_verified` means the provider advertised that file and hash, **not** that we downloaded it.

Use the public catalog link in the edition record if a download host is unavailable. Scans are not stored through Git LFS; keeping original downloads outside Git avoids adding roughly 170 MB of already-verified large PDFs plus hundreds of MB of journal issues to every clone.

Example programmatic comparison:

```python
import json
from pathlib import Path
c = Path('corpus')
passages = json.loads((c / 'indexes/passages.json').read_text())
assets = {a['id']: a for a in json.loads((c / 'metadata/assets.json').read_text())}
p = next(p for p in passages if p['id'] == 'pv-ascension')
for witness in p['witnesses']:
    if witness.get('asset_id'):
        lines = (c / assets[witness['asset_id']]['path']).read_text().splitlines()
        first, last = witness['lines']
        print(witness['source_id'], '\n'.join(lines[first-1:last]))
print(p['uncertainty'])
```

## What the files mean

| Location | Contents |
| --- | --- |
| `sources/editions/*.json` | One bibliographic record per edition, including pending and modern linked-only sources |
| `sources/transcriptions/` | Unchanged Gutenberg text, including its notices |
| `sources/ocr/` | Uncorrected archive OCR and separately labeled local OCR |
| `sources/scans/` | Download destination for pinned original facsimiles; PDFs ignored by Git |
| `metadata/assets.json` | File URL, source ID, size, checksum, quality and acquisition state |
| `metadata/rights.json` | Component-specific rights analysis, evidence and review date |
| `metadata/relationships.json` | Directional edition dependencies and confidence |
| `metadata/guthrie-installments.json` | 14 issue/date/page records; issue text includes unrelated articles |
| `metadata/ximenez-image-sequence.json` | LOC image order and original image URLs; not manuscript foliation |
| `images/catalog.json` | Visual references, provenance and image-specific rights |
| `indexes/` | Stable editorial IDs and initial episode-level concordance |

See [the data contract](DATA_MODEL.md), [rights assessment](RIGHTS.md), [research findings](RESEARCH_NOTES.md) and [precise outstanding tasks](BACKLOG.md). [Validation results](VALIDATION.md) document what was actually checked.

## Citation and text quality

Cite edition, part/chapter, printed page where verified, and scan or local text locator. Text lines are one-based, inclusive and bound to the pinned asset bytes; PDF sequence numbers are **not** printed page numbers. An episode match is not an exact translation alignment. Parentheses added by translators are not words from the K’iche’ manuscript.

The ascension record deliberately preserves the parenthetical “fathers” reading in Brasseur and Guthrie and the related wording in Spence, alongside the poem’s different choice. Resolving that reading requires primary K’iche’ collation and modern scholarship; majority voting among dependent translations is not evidence of independent agreement.

Historical introductions include speculative, colonial and racialized interpretations. Preserve them as historical source material, without treating them as present-day scholarly conclusions. K’iche’ traditions belong to a living community; public-domain status does not make a nineteenth-century commentator authoritative over that community.

## Contributing

Add a stable source ID and rights record first. Establish the exact edition, distinguish old content from new editorial additions, download to a temporary file and verify its format and completeness. Preserve downloaded bytes and record SHA-256, URL, review date and transformation history. Keep corrections in a separate derivative with its own provenance; do not silently replace OCR or historical spelling. Add accurate acquisition states even when blocked. For passage work, include explicit uncertainty, edition-specific locators and anchors; leave unknown fields null.

Run validation and the regression tests before committing. Changes to source bytes require deliberate anchor review. Do not edit poem or site files as a side effect of corpus maintenance.

German OCR can be regenerated separately with `scripts/ocr_pohorilles.py`; see [OCR provenance](metadata/ocr-runs.json). It requires Poppler, Tesseract, Pillow and a German trained-data file. Reproducibility means the documented method and pinned input are available; different OCR versions can produce different bytes. Review a new output before replacing a stored artifact.
