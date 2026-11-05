# Data contract (version 1)

All JSON is UTF-8. Metadata paths are relative to `corpus/`; adaptation paths are relative to the repository root. JSON arrays are used rather than an application-specific database. The executable validator is the dependency-free schema and integrity checker.

- **Source:** `id`, `title`, `publication_year` (integer or null), `contributors`, `languages` (ISO codes), `kind`, `catalog_urls`, `notes`, `acquisition_status`, `text_quality`, `review_date`, `asset_ids`. Manuscript creation date is separate from publication date.
- **Asset:** `id`, `source_id`, `path`, `url` (null only for generated output), `kind`, `quality`, `tracked` (boolean), `review_date`, `status`, `bytes`, and `sha256` or `upstream_checksum`. Generated files also identify `generated_from`. SHA-256 is required for committed files. A facsimile is not a transcription.
- **Rights:** `source_id`, `jurisdiction`, `status`, `publication_year`, `contributors`, `basis`, `evidence`, `components`, `international`, `limitations`, `review_date`. Status is `public_domain`, `CC0-1.0` or `copyrighted_reference_only`. Linked visuals without assets instead carry their own `image_rights` and pending state in the catalog; acquisition requires a rights record.
- **Relationship:** `id`, `from`, `to`, `relationship`, `certainty` (`verified` or `qualified`), `evidence`, `note`. The arrow points from a derived edition toward its witness.
- **Character:** `id`, `name` (editorial display label), `variants` with edition-specific spelling, `source_id` and verification note. Display names are not etymological claims.
- **Event:** `id`, `label`, `character_ids`, `status`. IDs identify editorial research topics, not alleged ancient chapter numbers.
- **Passage:** `id`, `event_ids`, `witnesses`, `adaptation_refs`, `uncertainty`, `alignment_level`, `editorial_status`. Witnesses identify a source, section, printed pages (or null), local line range and excerpt SHA-256 when mapped. `unmapped` records have no invented locator. These initial records align episodes, not individual sentences.
- **Installment:** `id`, `source_id`, `volume`, `issue`, `date` (YYYY-MM), inclusive printed `pages`, `text_asset_id`, `facsimile_asset_id`, `catalog_url`, `verification`, `ocr_method`, `ends_mid_page`.

`acquired` assets are committed. `download_verified` scans were fully downloaded and hashed during this build but omitted from Git. `remote_manifest_verified` scans have provider metadata and a checksum but were not downloaded. Edition-level acquisition states distinguish text-plus-scan recipes, manuscript facsimile-only, incomplete translation coverage, pending acquisition and linked-only modern references. The inventory must not collapse these into a single “complete” flag.

Line-anchor hashes use SHA-256 of UTF-8 text joined with LF, without a trailing newline, after Python `splitlines()`. Whole-file hashes cover exact bytes, including original line endings. IDs remain stable as coverage improves; do not repurpose an existing ID for a different episode.
