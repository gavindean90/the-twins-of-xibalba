# Facsimile cache

Run `python3 corpus/scripts/acquire.py --list` from the repository root, then select an asset with `--id`. PDFs are intentionally ignored by Git. Exact public URLs, sizes, rights and expected hashes are in `metadata/assets.json` and `metadata/rights.json` (relative to the corpus root).

Downloaded source files are never modernized. A successful checksum verifies bytes, not scholarly completeness or correctness. The manuscript’s image order must still be mapped to folios; the Guthrie issue PDFs include unrelated journal content.
