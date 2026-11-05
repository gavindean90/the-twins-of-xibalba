# Research findings and reconnaissance

## Repository

Base: `61811a8` on `main`. Inspected README, LICENSE, seven Markdown books, matching HTML publication files, static assets, JavaScript/CSS and the Xquic SVG. The two remote editorial branches contain no source corpus. No corpus, research directory or existing AGENTS.md was present. No tracked GitHub Actions workflow was present. All poem, site and artwork bytes are preserved; only a corpus pointer and license-scope clarification were appended to the root README.

The approximate eleven-book expansion is a planning goal, not an implemented new book structure. This assignment does not renumber books or dictate a new outline.

## Bibliographic corrections and limitations

- **Ximénez:** physical holder is the Newberry, not LOC. LOC provides the WDL digital surrogate. Ayer MS 1515 is the holding identifier; LCCN 2021668226 and WDL 19995 identify the digital record. Its date fields and namesake authority are inconsistent; the edition record preserves the discrepancy. Older provenance transfers need archival verification.
- **Scherzer:** 1857, not Spence’s erroneous 1856 reference. Original LOC catalog and scan metadata agree on 1857.
- **Brasseur:** K’iche’/French, 1861. Full original volume includes a long introduction, notes and index. OCR combines these with the primary text; search results from the introduction must not be mistaken for passages of the K’iche’ work.
- **Guthrie:** 14 located installments, October 1905–November 1906, not a demonstrated run through 1907. Two introductory installments precede the translation. The December 1905 article begins on printed p. 163; noisy index OCR reads 168. The October 1906 article begins p. 59; index OCR can read 69. Bound-volume page headings and article boundaries were inspected. Volume 4 p. 124 explicitly prints “THE END”; it finishes Part IV chapter XI, while Brasseur continues with chapter XII and the final genealogies (beginning p. 337). Thus the located serial is complete as published in that run, but its translation is incomplete relative to Brasseur. Independent IA issue OCR is retained unmodified, including other journal articles.
- **Spence:** 1908 abridgment/retelling with commentary, not a full translation. Its claim that no English translation had appeared is itself a historical claim requiring correction in light of Guthrie. The Gutenberg release date is not the original publication date.
- **Pohorilles:** Noah Elieser Pohorilles, 1913; title page confirms publisher J. C. Hinrichs’sche Buchhandlung. His preface describes a French-based draft revised using other linguistic materials. Original orthography is retained in scans; OCR remains noisy.
- **Raynaud:** original BnF record `FRBNF31183123`, not a modern facsimile record. Gallica item `bpt6k329096x` identified; access attempts returned 403. BnF’s source-language “quechua” is a catalog error, not evidence of an Andean source.
- **Villacorta/Rodas:** 1927 original confirmed by Smithsonian and Google Books; do not confuse with their 1934 printing or the separate Asturias/González de Mendoza Spanish translation of Raynaud. Contributor given-name expansions vary in catalogs; the record preserves the Smithsonian identification rather than silently substituting “Juan”.

## Ascension: a concrete warning against conflation

Spence’s Second Book ends with language attaching the sun and moon to father and uncle. Guthrie’s May 1906 installment, p. 111, explicitly inserts “(their fathers)”; Brasseur p. 193 inserts “(leurs pères)”. These are related historical interpretive choices, not three independent confirmations of a manuscript reading. The existing poem explicitly leaves the father below while the brothers play across the heavens. The concordance records all of this without rewriting the poem or deciding the K’iche’ reading. This is a useful first case for a careful manuscript-and-modern-scholarship comparison.

## Acquisition record

Archive front-end 503 responses were resolved for Brasseur and four Guthrie issue texts using Internet Archive’s public metadata-provided storage server. Canonical public item URLs remain the acquisition authority. Both nineteenth-century scans and OCR match provider SHA-1; all committed source bytes receive SHA-256. Full Ximénez and Pohorilles PDFs were downloaded and hashed. Journal PDF recipes are pinned to upstream SHA-1 but those independent microfilm PDFs were not all downloaded; bound-volume IAPSOP scans were used locally for verification and are excluded from the repository.

No generic OCR was applied to Ximénez’s handwriting. There is no verified machine-readable manuscript transcription in this initial corpus. The Brasseur K’iche’ OCR is a printed edited witness, not a substitute for one.

Research URLs and rights evidence are attached to the individual edition and visual records. No modern translation text was imported. No AI artwork was generated.
