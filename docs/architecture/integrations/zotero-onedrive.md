# Zotero ↔ OneDrive – read-first Capability Slice

**Status:** `more-test`  
**Scope:** #49 / Zotero Local API read capability + AQ-ZO-02 legacy compatibility  
**Test date:** 2026-09-10

## Tested environment

- Zotero Desktop `10.0.1`
- Existing Zotero skill helper, using `http://127.0.0.1:23119`
- Local profile detected; no account credentials or API keys read or persisted

## Actual observations

The Connector endpoint `/connector/ping` returned HTTP `200` (`Zotero is running`). The initial and repeated Local API probes returned HTTP `403` with `Local API is not enabled` for `/api/`, `/api/schema`, item types, collections, tags, items, searches, groups, and full-text version metadata.

The required local authorization boundary is the Zotero Desktop preference “Allow other applications on this computer to communicate with Zotero” (Settings → Advanced). It was not enabled in the observed run (`local_api_enabled_pref: null`), so no library data could be read. No preference file was manipulated by this test.

## Read/write boundary

After manual activation, inventory, collections, tags, representative item records, item-level tags, note metadata, and note contents were read successfully through the Local API in bounded read-only tests. The note contents were technically read to verify capability but were not copied into the test report or repository.

No Zotero mutation was performed. Write capabilities remain untested and no write authorization was requested. In particular, no item, collection, tag, note, import, attachment, or write-back operation occurred.

Attachment/file/full-text and OneDrive/Web-API boundaries remain separate from the bibliographic metadata/notes capability. The legacy linked-file compatibility checks below do not define the target workflow.

## Architecture disposition

The Local API is empirically sufficient as a read-only bibliographic adapter candidate for item representations, collections, tags, item tags, and Zotero note content. This supports the existing canonical-state contract role for Zotero as bibliographic/archival management and reference input; it does not make Zotero the canonical owner of Histo-Orla research state.

AQ-ZO-02 remains unresolved as a target workflow question. The existing Zotero skill is sufficient for the tested local read capabilities; no custom adapter is justified by these tests. Provider keys, attachment keys, paths, and future OneDrive IDs remain external references/locators under #50 and the canonical research-state contract.

Disposition: `more-test`.

## Read-only verification after manual activation

The user manually enabled the Local API preference. A subsequent run of the existing skill verified:

- Local API enabled; HTTP `200`; Zotero Desktop `10.0.1`, API v3, schema v44.
- Connector remained reachable with HTTP `200`.
- Inventory: **182 top-level items**.
- Collections: **24**.
- Tags: **752**.
- Five representative metadata records were readable, including Zotero and generated BibTeX keys:

| Title | Creator(s) | Year | Zotero key | BibTeX key |
|---|---|---:|---|---|
| Nr. 3064 [Kf. Johann] an [Martin Luther], [Justus Jonas], [Hans von Dolzig] [Hans von Gräfendorf] | Kf. Johann; Martin Luther; Hans von Dolzig; Hans von Gräfendorf; Justus Jonas | 1525 | `VFR8QKJK` | `kf_johann__1525` |
| Nr. 688 [Dekan Konrad Gerhart], [Senior und Kapitel des Georgenstifts zu Altenburg] an [Kf. Friedrich] | Konrad Gerhart; Kf. Friedrich | 1518 | `3PI4FHYK` | `konrad_gerhart__1518` |
| Schumann, August: Vollständiges Staats-, Post- und Zeitungs-Lexikon von Sachsen. 5 … | — | — | `I3728QZX` | `noauthor_schumann_nodate` |
| (1168–1189, vielleicht 1188 Dezember), (Saalfeld) – Friedrich erwirbt … | — | 1188 | `UJEBQGAJ` | `noauthor_11681189_1188` |
| 1071 Erzbischof Anno von Cöln stiftet … im Orlagau … | Schultes | 1071 | `2EB69PNX` | `schultes_1071_1071` |

Only item metadata and BibTeX representations for these five items were read in this first verification. No write authorization was requested.

## Item metadata, tags, and notes read-capability slice

A later bounded read-only test explicitly checked whether the Local API can expose richer item representations, item tags, and Zotero note content. No attachment paths, file bytes, PDF content, full-text endpoints, OneDrive, Zotero Web API, or write operations were part of this test.

### Test boundary

Three top-level items were inspected:

- `VFR8QKJK`
- `3PI4FHYK`
- `I3728QZX`

Two Zotero notes were inspected for capability. Their full note contents were not copied into the returned report or persisted in Git.

### Full item representation

The complete Local API item representation was readable for all three tested items. Observed top-level sections were:

- `key`
- `version`
- `library`
- `links`
- `meta`
- `data`

Observed `data` fields across the three examples included:

- `key`
- `version`
- `itemType`
- `title`
- `date`
- `url`
- `accessDate`
- `creators`, including `creatorType`
- `tags`
- `collections`
- `relations`
- `dateAdded`
- `dateModified`
- `archiveLocation`
- `rights`
- item-specific `letterType`

Observed additional metadata included:

- `meta.creatorSummary`
- `meta.parsedDate`
- `meta.numChildren`
- library ID and library name
- self/alternate links

Fields such as `publicationTitle`, `bookTitle`, `volume`, `issue`, `pages`, `publisher`, `place`, `language`, `DOI`, `ISBN`, `ISSN`, `abstractNote`, `extra`, `archive`, and `callNumber` were not delivered in these three concrete item representations. This is **not** evidence that the Local API cannot expose those fields. The capability boundary is:

```text
API representation/field model readable
!=
field populated on a particular item
```

Likewise, an empty or absent field in one tested item must not be generalized to all Zotero item types or records.

### Item tags

Item → tags was readable deterministically through `data.tags`. The tested item-tag objects exposed the `tag` value. No additional tag type/metadata was observed in these item-tag objects.

Representative observed tag values included:

- `1525`
- `editiert`
- `Hans-von-Dolzig`
- `Konrad-Gerhart`
- `von-Knau`

The test did not dump or inspect all 752 library tags.

### Zotero notes

Two notes were found and their note content was technically readable through the Local API. The content was represented as an HTML string, including `<div>`/`<p>` markup and `data-schema-version="9"`.

For the tested notes, the following note metadata was readable:

- note key
- `version`
- `itemType`
- `parentItem` for child-note relation
- `dateAdded`
- `dateModified`
- `relations`
- `tags`
- `meta.numChildren`
- library information and links

Note tags were readable; both tested notes had an empty tag list.

Capability result:

```text
Zotero item representation  = readable, read-only
Item tags                    = readable, read-only
Zotero note metadata         = readable, read-only
Zotero note content          = readable, read-only
Full note content in Git     = no
Zotero write capability      = untested / unauthorized
```

### Functional significance

The bounded tests now empirically support the following local read capabilities for Histo-Orla integration:

- resolve/read Zotero item records and their complete API representation;
- read bibliographic/item metadata as actually populated in Zotero;
- read collections and library-level tags;
- read tags attached to individual items;
- identify and read child-note relationships;
- read Zotero note metadata and note content;
- use Zotero item/note keys and versions as external provider references/metadata, not as Histo-Orla canonical scientific identity.

Important constraints:

- "complete API representation" does not mean every possible bibliographic field is present on every item;
- Zotero notes are readable provider content, but are not automatically Histo-Orla findings, evidence, or validated research state;
- no tested read capability implies permission to write back to Zotero;
- this local test says nothing yet about Web API/device-independent availability;
- attachment/file/full-text access and OneDrive byte availability remain separate capabilities.

## Attachment metadata slice

For the representative parent item `VFR8QKJK`, the skill’s child read returned two children: one attachment and one note. The attachment metadata request for `39IPCF2Q` returned HTTP `200`:

- Parent item key: `VFR8QKJK`
- Attachment key: `39IPCF2Q`
- Attachment type: `attachment`
- Title/label: `Digitale Edition`
- Link mode: `linked_url`
- Content type/MIME: empty in the returned metadata
- Filename: not present in the returned metadata
- Attachment child count: `0`
- API metadata also included an external `url`, access date, charset, tags, relations, and modification timestamps; the URL was not resolved or opened.

This proves deterministic parent → attachment navigation and metadata retrieval. It does not prove access to a concrete file or inspected byte instance.

## Open questions explicitly outside these slices

These tests do not establish Zotero Web API or account/API-key access, device-independent Zotero availability, OneDrive/Graph access, OneDrive byte access, rename/move behavior, byte-change detection, cross-device behavior, Zotero full-text endpoint behavior, OCR, or write-back safety.

Attachment/file behavior remains independently scoped. The local `linked_file` checks below are legacy compatibility evidence only.

## Linked-file resolver slice (legacy compatibility capability; not target workflow)

Owner clarification for #49: PDFs/source bytes remain in a normal, human-readable OneDrive folder structure; Zotero is not the file store. Existing `linked_file` attachments are legacy inventory. The following observations therefore document compatibility only and do not define the target architecture.

Search boundary: top-level local items were inspected in title order until the first qualifying child; 39 parent items and 100 child records were checked. The first real `linked_file` attachment found was:

- Parent item: `LMTFTRHS`
- Attachment: `HG8CHSUV`
- Title/label: `Held - 1999 - Christoph von Carlowitz.pdf`
- Link mode: `linked_file`
- Content type: `application/pdf`
- Attachment path metadata: `attachments:Held - 1999 - Christoph von Carlowitz.pdf`

The Local API file resolver returned a local `file://` reference for this attachment. The absolute user-specific path is intentionally not persisted here. The file URL was not opened, and no existence check, byte read, hash, PDF/full-text read, or other processing was performed.

This proves locator exposure only: `file:// reference obtained` does not establish file existence, byte availability, or a verified Histo-Orla inspected instance.

## Filesystem reachability slice (legacy compatibility capability; not target workflow)

For the same attachment `HG8CHSUV`, the already exposed `file://` locator was resolved internally and checked with filesystem metadata operations only. The target exists, is a regular file entry, and the local filesystem permission check indicated readable. The absolute path was not persisted. No file descriptor was opened and no byte was read.

This establishes filesystem-entry reachability only. It does not establish that all bytes are locally hydrated or available without provider action, and it does not verify an inspected instance.

## Next action

Discriminate AQ-ZO-03/AQ-ZO-04 with a separate read-only remote/device-independent slice: Zotero synced/web metadata plus OneDrive metadata/resolution, without relying on Zotero `linked_file` or local absolute paths. Further byte/hydration tests for `HG8CHSUV` are stopped for now.
