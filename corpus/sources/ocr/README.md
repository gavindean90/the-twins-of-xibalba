# Provisional OCR

Scherzer and Brasseur files are unchanged Internet Archive `_djvu.txt` derivatives. Brasseur’s provider identifies ABBYY FineReader 8.0 and an ABBYY-to-hOCR conversion; Scherzer’s provider identifies conversion metadata but not the original OCR engine version. Do not invent the missing version.

`guthrie/` contains independent Internet Archive OCR of 14 **whole journal issues**, not a falsely clean continuous translation. Article boundaries, dates and printed pages are in `metadata/guthrie-installments.json` relative to the corpus root. The final serial installment omits Brasseur’s Part IV chapter XII genealogies despite its printed “THE END”.

Pohorilles is local Tesseract OCR, with separate scan-page/half markers. Exact method and software are in `metadata/ocr-runs.json`. Page halves preserve reading order; printed page labels remain unverified. Long-s, accents, K’iche’ words, footnotes and tables are error-prone. No OCR file has been silently corrected.
