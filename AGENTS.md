# Research and writing guidance

Preserve the existing poem, nine-line stanza form, site files and publication workflow unless the task specifically authorizes literary or site changes. The research corpus lives under `corpus/`.

- Prioritize primary K’iche’ text and reliable historical witnesses. Distinguish a manuscript reading from an editor’s transcription, a translation and an interpretation.
- Never invent citations, quotations, passages, printed pages, folios or exact alignments. Unknown locators stay null or unmapped.
- Cite source edition, section and printed page wherever verified; otherwise cite the pinned asset and line range. PDF sequence and printed page numbers differ.
- Preserve provenance for factual claims. Inspect source files before relying on metadata summaries. OCR is provisional; check the facsimile before making a consequential textual claim.
- Do not silently merge translations, normalize spelling or remove an author’s interpretive parentheses. Record disagreements and omissions explicitly.
- Respect source-specific rights in `corpus/metadata/rights.json`; the project’s CC0 dedication does not relicense third-party material. Modern translations are linked-only unless separately authorized.
- Distinguish original creative material from historical witnesses. Do not attribute the poem’s inventions to the Popol Vuh.
- Dependent translations are not independent corroboration. Discuss disputed readings and the uncertainty of proposed identifications.
- Consult `corpus/README.md`, `corpus/DATA_MODEL.md` and `corpus/BACKLOG.md`. Preserve raw files; put editorial corrections into separate derivatives with transformation provenance.
- Run `python3 corpus/scripts/validate.py` and `python3 -m unittest discover -s corpus/scripts -p 'test_*.py'` after changes. Do not commit large cached scans, credentials or unreviewed rights material.
