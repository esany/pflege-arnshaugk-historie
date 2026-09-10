# Zotero ↔ OneDrive – read-first Capability Slice

**Status:** `more-test`  
**Scope:** #49 / AQ-ZO-02 only  
**Test date:** 2026-09-10

## Tested environment

- Zotero Desktop `10.0.1`
- Existing Zotero skill helper, using `http://127.0.0.1:23119`
- Local profile detected; no account credentials or API keys read or persisted

## Actual observations

The Connector endpoint `/connector/ping` returned HTTP `200` (`Zotero is running`). The initial and repeated Local API probes returned HTTP `403` with `Local API is not enabled` for `/api/`, `/api/schema`, item types, collections, tags, items, searches, groups, and full-text version metadata.

The required local authorization boundary is the Zotero Desktop preference “Allow other applications on this computer to communicate with Zotero” (Settings → Advanced). It was not enabled in the observed run (`local_api_enabled_pref: null`), so no library data could be read. No preference file was manipulated by this test.

## Read/write boundary

The initial pre-activation read attempt did not succeed. After manual activation, inventory, collections, tags, five example-item records, and one attachment metadata record were read successfully. Attachments beyond that single metadata record, local paths, PDFs, full text, Web API, OneDrive/Graph, and remote paths were not tested.

No Zotero mutation was performed. Write capabilities remain untested and no write authorization was requested. In particular, no item, collection, tag, note, import, attachment, or write-back operation occurred.

## Architecture disposition

This is a valid non-empty #49 capability record, but AQ-ZO-02 remains unresolved. The existing Zotero skill is sufficient for the next read-only probe; no custom adapter is justified. Provider keys, attachment keys, paths, and future OneDrive IDs remain external references/locators under #50 and the canonical research-state contract.

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

Only item metadata and BibTeX representations for these five items were read. No attachment, path, PDF, full text, Web API, OneDrive/Graph, or write operation was performed; no write authorization was requested.

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

## Open questions explicitly outside this slice

This slice does not establish OneDrive byte access, Web API or account/API-key access, rename/move behavior, byte-change detection, cross-device behavior, OCR/full text, or write-back safety.

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
