# Validation report

Executed 2026-11-04 against the dedicated `research/public-domain-corpus` branch.

- `python3 corpus/scripts/validate.py`: **PASS**. Checks required fields, unique IDs, edition/asset inventories, source and rights references, character variants, episode witnesses, adaptation anchors, OCR references, installment count, local Markdown links and file checksums.
- `python3 -m unittest discover -s corpus/scripts -p 'test_*.py'`: **12 tests passed**. Includes corrupt source data, missing rights, dangling witnesses, incomplete installment inventory, missing files, path traversal and rejection of bad download responses without replacing user files.
- `python3 -m py_compile corpus/scripts/*.py`: **PASS**.
- Original Scherzer and Brasseur PDF and OCR files match Internet Archive SHA-1. LOC Ximénez, OSU Pohorilles and every committed source asset have SHA-256 pins.
- Live `acquire.py --id word-1906-05-pdf`: **downloaded and verified** independent IA May 1906 facsimile against its advertised size and SHA-1; SHA-256 recorded afterward. Other independent issue PDFs remain remote-manifest verified, not claimed downloaded.
- Download/cache verification succeeded for Ximénez, Scherzer, Brasseur, Pohorilles, Spence and the Cleveland image. Existing scans are ignored by Git; none of the large PDFs are part of the commit.
- All 71 Pohorilles PDF pages processed in two halves (142 OCR segments), including blank cover halves. Title/preface and ending spot-checked; no claim of corrected OCR accuracy.
- Visual inspection confirmed Guthrie’s terminal “THE END” on printed p. 124. Brasseur’s continuation into Part IV chapter XII is recorded as a substantive omission, not an acquisition failure.
- No differences from base `61811a8` in poem Markdown, HTML, CSS, JavaScript, SVG artwork or LICENSE. Root README receives only the corpus pointer and third-party rights clarification.

The validator checks local references and pinned bytes offline. It does **not** continuously check every external URL, prove legal conclusions or certify every OCR word and historical interpretation. Raynaud’s Gallica access is known blocked (403); pending and linked-only sources are valid metadata states, not successful text acquisitions.

## PR review follow-up

The new bulk-acquisition regression test failed against the original implementation with the generated OCR file absent, reproducing the review finding. After restricting `--all` to remote URLs, all 12 tests pass. The test asserts that every remote asset is selected and no generated asset is selected. A second regression test confirms an explicit request for missing generated OCR reports reproduction instructions without making a network request. Full remote acquisition was mocked for these CLI tests; no new claim of downloading all facsimiles is made.
