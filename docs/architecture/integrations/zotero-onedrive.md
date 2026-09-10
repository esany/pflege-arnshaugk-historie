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

No inventory, collection, tag, or example-item read succeeded. Consequently no item titles, creators, years, Zotero keys, or BibTeX keys are reported. Attachments, local paths, PDFs, full text, Web API, OneDrive/Graph, and remote paths were not tested.

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

## Open questions explicitly outside this slice

This slice does not establish attachment resolution, OneDrive byte access, Web API or account/API-key access, rename/move behavior, byte-change detection, cross-device behavior, OCR/full text, remote paths, or write-back safety.

## Next action

After the user enables the Local API preference in Zotero Desktop, rerun the existing skill’s `status`, `inventory`, `collections`, and `tags` commands, then inspect at most five representative item metadata records. Do not request write authorization.
