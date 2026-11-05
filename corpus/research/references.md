# References and consultation record

Consulted 2026-11-04. Locators below refer to the named edition's pagination or manuscript foliation, not browser line numbers. The source inventory and asset manifest remain authoritative for downloaded bytes and rights. No modern translation or modern transcription is imported as a source asset.

## Primary and historical witnesses

- **Francisco Ximénez, manuscript associated with his K’iche’ transcription and Spanish translation**, Newberry Library, Ayer MS 1515, volume 2. [LOC digital item](https://www.loc.gov/item/2021668226/); [viewer](https://www.loc.gov/resource/gdcwdl.wdl_19995/). The inspected object is the checksum-pinned `ximenez-pdf`. Selected foliation and column observations are in [the folio map](../metadata/ximenez-folios.json); scope and access limitations are in [the method](manuscript-method.md).
- **Carl Scherzer, ed., 1857**, *Las historias del origen de los indios de esta provincia de Guatemala*, Spanish Ximénez witness. [LOC catalog](https://www.loc.gov/item/05009885/). Selected narrative pp. 29–44 and 75–79; exact local OCR anchors in the existing passage IDs. The version relationship to the surviving bilingual manuscript is qualified, not assumed identical.
- **Charles-Étienne Brasseur de Bourbourg, 1861**, *Popol Vuh. Le livre sacré et les mythes de l’antiquité américaine*. [LOC catalog](https://www.loc.gov/item/05009887/). Part II, chapters i–v and xiii–xiv; pp. 68–105 and 190–193 are especially relevant. Facing K’iche’ and French are separate editorial layers. French notes on pp. 101, 105 and 192–193 must not be attributed to the underlying narrator.
- **Kenneth Sylvan Guthrie, 1905–1906**, “Popol Vuh,” *The Word*. February 1906 II.ii–iii, March II.iii–iv and May II.xiv (p. 111). Exact issue files and page spans: [installment register](../metadata/guthrie-installments.json). May p. 111 was visually checked; other new line anchors identify local OCR passages and do not certify every character.
- **Lewis Spence, 1908**, *The Popol Vuh: The Mythic and Heroic Sagas of the Kichés of Central America*. [Gutenberg 56550](https://www.gutenberg.org/ebooks/56550). “The Second Book”; local `spence-txt` lines are the reliable anchors until original pagination is collated. This is a retelling.
- **Noah Elieser Pohorilles, 1913**, *Popol Wuh: Das heilige Buch der Quiché-Indianer von Guatemala*. [OSU-hosted historical scan](https://u.osu.edu/mayanarchives/files/2016/06/Noah-Elieser-Pohorilles-2l9b6c0.pdf). Chapters XXVII–XXVIII, printed pp. 63–64, PDF spreads 40–41. Printed p. 64 visually checked. Its rearrangement of the grandmother episode is evidence of editorial intervention, not a manuscript variant. Other German OCR references in the dossiers remain provisional.

## Modern scholarship: consulted, not reproduced

**Allen J. Christenson, *Popol Vuh: Sacred Book of the Quiché Maya People*, Mesoweb electronic edition, 2007.** [Publisher-hosted PDF](https://www.mesoweb.com/publications/Christenson/PopolVuh.pdf). Relevant checkpoints are pp. 114–115, note 276 (alternative lexical readings in the skull discourse) and pp. 176–177, note 449 (ancestral scene and ascent). This contemporary K’iche’-informed treatment is a comparator; agreement with it does not independently authenticate this project's paleography. Brief paraphrases are confined to the two linked discussions in [Xquic](xquic-conception-and-escape.md) and [ascension](ancestors-and-ascension.md).

**Christenson, *Popol Vuh: Original Text Transcription*.** [Publisher-hosted PDF](https://www.mesoweb.com/publications/Christenson/PV-Original.pdf), f. 32v. Consulted for comparison of the ascent construction. This is a modern edited transcription, not the image itself; its spelling and segmentation have not been pasted into the diplomatic assets.

**Sam Colop, *Popol Wuj: Versión poética k’iche’*, 1999, p. 68, note 165.** Indirect reference only, as reported in Christenson's note 276. Direct consultation remains outstanding. No claim here to have inspected Colop's edition or independently established his textual argument.

**Newberry Library, “Popol Vuh” research guide.** [Institutional guide](https://www.newberry.org/collection/research-guide/popol-vuh). Consulted for custodial context and the work's continuing literary tradition. Physical custody, digital hosting, manuscript production and the older narrative's history are separate questions. This guide does not license treating colonial or European editorial explanations as culturally definitive.

## Recovery and review

Start with a dossier's passage ID in [passages.json](../indexes/passages.json). Resolve its `asset_id` through [assets.json](../metadata/assets.json), then use its inclusive one-based `lines` and excerpt checksum. Image witnesses instead resolve `manuscript.folio_map_id` through the folio map. Three transcription witnesses resolve their `transcription_id` through [transcriptions.json](../metadata/transcriptions.json). All public facsimiles remain recoverable through the existing acquisition tool without this research session or any private service.

The modern consultation is deliberately limited. Direct comparison with additional contemporary K’iche’ scholarship, a full discourse analysis of 32r–32v and independent paleographic review are still required before declaring the difficult readings settled.
