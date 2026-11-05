# Manuscript locators and transcription method

## What was inspected

The full LOC PDF was reacquired with the existing downloader and matched its pinned SHA-256 `8954407812e5733b625eac85af2374dca6b2f9203eeaa61f399b76d21e6141b6` (61,753,371 bytes, 134 PDF pages). Individual full-page renderings were visually inspected for the selected episodes; enlarged crops were used for the short readings. No general handwriting OCR was run.

[The folio map](../metadata/ximenez-folios.json) extends, rather than replaces, [the original provider sequence](../metadata/ximenez-image-sequence.json). PDF page, provider sequence and folio are separate fields. The map associates the selected PDF pages with the provider’s corresponding sequence, not by calling the folio the PDF page number. The provider viewer also reports 134 images. Direct JP2 downloads and a fresh IIIF manifest request returned HTTP 403 during this work; individual JP2-to-PDF pixel equivalence was not independently checked. Use the hash-pinned PDF as the inspected authority; viewer and original image links remain provided for recovery.

| LOC/PDF sequence | Visible foliation | Contents checked |
| --- | --- | --- |
| 33–34 | 12r–12v | Family, ballplay and council |
| 35–36 | 13r–13v | Council, summons, equipment and farewell |
| 37–38 | 14r–14v | Descent, humiliations and Dark House |
| 39–40 | 15r–15v | Death, head/tree and Xquic’s encounter |
| 41–42 | 16r–16v | Saliva discourse, conception, discovery and substitute heart |
| 43–44 | 17r–17v | Escape and household/maize test |
| 45 | 18r | Acceptance, birth and childhood |
| 71–72 | 31r–31v | Final victory and restriction of Xibalba |
| 73–74 | 32r–32v | Memorial canes, ancestors and ascent |

The pale foliation annotations occur at upper outer margins on both sides. Their numbering is observed, but their age and authorship are unknown. Recto/verso is checked from the gutter and paired page layout, not asserted to be wording written by Ximénez. The selected runs show no missing page between consecutive inspected leaves. This is **not** a census of missing leaves throughout the codex. The preliminaries and Escolios remain outside this mapping.

Do not apply a constant offset to the whole PDF. The opening narrative appears at sequence 9, and sequence 11 bears 2, whereas the selected later folios have the associations above. The intervening discrepancy must be collated before publishing a global formula. A full foliation audit, including repeated images, inserted leaves and differently numbered surfaces, remains outstanding. Do not manufacture a missing folio to explain the discrepancy.

## Three distinct layers

[Transcription metadata](../metadata/transcriptions.json) describes three short left-column excerpts: the Xquic heading (15v), conception (16r) and ascent (32v). Their diplomatic text files are registered assets with whole-file checksums; concordance anchors have excerpt checksums. Each record contains an approximate crop box in PDF points, reviewer status, method and uncertain readings.

1. **Diplomatic working transcription:** observed historical spelling and lineation, using plain Unicode approximations. Word spacing, punctuation and difficult letters remain subject to review. Excerpt boundaries may cut sentences or words, expressly noted in metadata. They are new readings made against images, not pasted from Brasseur or a modern transcription.
2. **Normalized working text:** null. No normalization has been attempted, so the transformation list is empty. Any future normalization must list substitutions and preserve its diplomatic input.
3. **English research gloss:** a newly prepared cautious sense rendering. It is not a certified translation or a replacement for the source. Explicit antecedents are not inserted into the ascension gloss.

All three excerpts were checked visually by the same AI researcher. None has an independent human, second-reader or K’iche’ specialist verification. “Image checked” must never be displayed as “independently verified.” Broader readings, overwritten text and marginal notes were not exhaustively transcribed. The 15v marginal annotation near the dialogue is deliberately excluded from the heading excerpt.

For a reproducible view, first run `python3 corpus/scripts/acquire.py --id ximenez-pdf`. Open the one-based PDF page recorded in the map. Optional rendering with PyMuPDF uses zero-based `document[pdf_page - 1]`; crop coordinates are top-left PDF points. Rendering is an inspection aid and does not alter historical bytes. All metadata validation remains standard-library-only.
