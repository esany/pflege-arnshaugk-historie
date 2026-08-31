# Orlagau – gemeinsames Source Ledger

**Status:** `working-research / source-identity-ledger`  
**Work Owner:** #46 / #47  
**Protokoll:** `docs/research/source-identity-protocol.md`  
**Stand:** 2026-08-31

## Zweck

Dieses Ledger führt die bibliographische, archivalische und digitale Identität aller Quellen, die in #46/#47 ernsthaft verwendet oder geprüft werden. Es ist **nicht** das Exzerptregister und **nicht** die Findings-Datei.

Jeder Eintrag erhält eine stabile interne `source_id`. Exzerpte und Findings verweisen auf diese ID.

---

## SRC-ED-0001 – Urkundenbuch des Hochstifts Naumburg, Teil 2

- **source_type:** wissenschaftliche Edition / Urkundenbuch
- **canonical_citation:** Hans K. Schulze (Hg.), auf der Grundlage der Vorarbeiten von Felix Rosenfeld und Walter Möllenberg, bearbeitet von Hans Patze und Josef Dolle, *Urkundenbuch des Hochstifts Naumburg. Teil 2 (1207–1304)*, Quellen und Forschungen zur Geschichte Sachsen-Anhalts 2, Köln/Weimar/Wien: Böhlau, 2000.
- **bibliographic_identity_status:** `verified from inspected title and imprint pages of the user-provided instance`
- **source_instance_status:** `user-provided digital instance; scholarly edition inspected`
- **uploaded/local filename:** `UB Naumburg 2-2000.pdf`
- **series:** `Quellen und Forschungen zur Geschichte Sachsen-Anhalts ; Bd. 2`
- **ISBN-10:** `3-412-14499-1` — verified from imprint page
- **ISBN-13:** `978-3-412-14499-9` — verified independently in publisher/library catalogues
- **K10plus PPN:** `1152991957`
- **verified permanent bibliographic record:** `https://katalog.ub.uni-heidelberg.de/titel/65118363`
- **publisher record:** `https://www.vandenhoeck-ruprecht-verlage.com/themen-entdecken/buecher-zum-sonderpreis/41414/urkundenbuch-des-hochstifts-naumburg`
- **SLUB catalogue discovery:** SLUB catalogue contains a record for volume 2; exact public full-text digital object for this 2000 volume has not yet been verified as the canonical online instance.
- **public full-text digital provider:** `not yet verified`
- **public full-text landing page:** `not yet verified`
- **URN:** `not yet verified`
- **DOI / Handle / ARK / PURL:** `not yet verified`
- **IIIF:** `not yet verified`
- **scan/page mapping:** `mandatory per excerpt; PDF image page and printed page must be distinguished`
- **rights/licence:** `not yet verified for a public digital full-text instance`
- **edition_scope_caveat:** The introduction explicitly states that documents in which the institutions/persons relevant to the edition occur **only through witness mention** are no longer included. Therefore a negative result in NHUB II does **not** establish absence from contemporary witness lists or from medieval documentary transmission generally.
- **editorial_history_caveat:** The introduction documents substantial incompleteness in earlier Rosenfeld/Möllenberg material, later autopsy and supplementation by Patze/Dolle, more than 50 archives/libraries consulted, 188 newly added charter numbers and more than 85 substantially supplemented/newly transcribed texts. Historical archive shelfmarks in the apparatus may be obsolete and must be concorded where a present-day archival claim is made.
- **notes:** Edition contains regesta, full texts, archival/transmission apparatus, place/person index, subject index and seal apparatus. Editorial place identifications are recorded as editorial evidence, not silently converted into source wording.
- **next verification:** Resolve a trustworthy public full-text instance, if one exists; capture persistent digital-object identifier/URN/IIIF where published; maintain printed-page ↔ scan-page mapping for each excerpt.

## SRC-ED-0002 – Codex diplomaticus Saxoniae I/B 1

- **source_type:** wissenschaftliche Edition / Urkundenbuch
- **canonical_citation:** Hubert Ermisch (Hg.), *Urkunden der Markgrafen von Meißen und Landgrafen von Thüringen 1381–1395*, Codex diplomaticus Saxoniae regiae, I. Hauptteil, Abteilung B, Bd. 1, Leipzig 1899.
- **source_instance_status:** `user-provided digital instance; scholarly edition inspected`
- **uploaded/local filename:** `cds1b1-Ermisch-1899.pdf`
- **authoritative online edition / project:** Institut für Sächsische Geschichte und Volkskunde (ISGV), Codex diplomaticus Saxoniae
- **verified band landing page:** `https://codex.isgv.de/codex.php?band=cds1b1`
- **verified page-addressing pattern:** individual printed pages can be addressed through the ISGV edition, e.g. `https://codex.isgv.de/codex.php?a=b&band=cds1b1&s=379`; exact page links must be captured per excerpt rather than inferred globally.
- **Sächsische Akademie project/publication record:** `https://www.saw-leipzig.de/de/forschung/projekte/codex-diplomaticus-saxoniae/publikationen` — lists CDS I/B 1 as an online volume.
- **Qucosa / repository object:** project context indicates online digital availability, but the exact persistent Qucosa object identifier for this volume has not yet been verified in this ledger.
- **URN:** `not yet verified`
- **DOI / Handle / ARK / PURL:** `not yet verified`
- **IIIF:** `not yet verified`
- **scan/page mapping:** `to record per excerpt; ISGV printed-page address preferred where stable`
- **rights/licence:** `not yet verified for underlying page-image object`
- **notes:** The ISGV online edition is a strong reproducible access point for page-level checking. It must still be distinguished from the 1899 printed edition and from the user-provided PDF instance.
- **next verification:** Resolve exact repository/digital-object identifier behind the online page images, including URN/PURL/IIIF if published; verify title/imprint/series directly in the uploaded scan before final bibliographic normalization.

## SRC-ED-0003 – Lehnbuch Friedrichs des Strengen 1349/1350

- **source_type:** wissenschaftliche Edition / Lehnbuch
- **canonical_citation:** Woldemar Lippert und Hans Beschorner (Hg.), *Das Lehnbuch Friedrichs des Strengen. Markgrafen von Meissen und Landgrafen von Thüringen 1349/1350*, Aus den Schriften der Sächsischen Kommission für Geschichte 8, Leipzig: B. G. Teubner, 1903.
- **bibliographic_identity_status:** `verified against SLUB catalogue; title/imprint of the user-provided scan still to be visually concorded`
- **source_instance_status:** `user-provided image-based scan; text layer insufficient for systematic search`
- **uploaded/local filename:** `Das Lehnbuch Friedrichs des Strengen ... 1349/1350`
- **verified public provider:** `SLUB Dresden`
- **verified catalogue record:** `https://katalog.slub-dresden.de/id/0-165495571X`
- **catalogue details:** Leipzig: Teubner 1903; online edition Dresden: SLUB 2016; series `Aus den Schriften der Sächsischen Kommission für Geschichte ; 8`; original SLUB shelfmark reported in the catalogue as `35.8.7744`.
- **ISGV/HOV bibliographic corroboration:** ISGV bibliographic apparatus identifies Lippert/Beschorner and the 1903 edition; exact persistent ISGV record URL to be captured if used as a citation route.
- **public digital-object landing page:** `not yet captured separately from catalogue record`
- **URN:** `not yet verified`
- **DOI / Handle / ARK / PURL:** `not yet verified`
- **IIIF:** `not yet verified`
- **scan/page mapping:** `mandatory during visual register/page pass`
- **rights/licence:** `not yet verified`
- **manuscript_relation:** The printed edition must not be conflated with the surviving chancery/copial manuscript tradition. Sächsisches Staatsarchiv online records for Bestand 10004 Kopiale provide relevant manuscript context; each manuscript witness must receive its own source_id if directly used.
- **notes:** Register- and page-level work must be performed visually on the scan. No completeness claim from OCR/full-text search is admissible.
- **next verification:** Open the SLUB digital object from the catalogue, record the persistent object URL, URN and IIIF manifest if exposed; visually verify title/imprint in the uploaded scan; establish scan ↔ printed-page mapping.

---

## Archivalische Quellen – Discovery-Status, Original noch nicht inspiziert

### SRC-AR-0001 – LATh EGA 6-11-0028 Nr. 5855

- **source_type:** Archivale / Rechnung
- **archive_institution:** Landesarchiv Thüringen; exact current repository unit/location to verify from catalogue record
- **current_shelfmark:** `EGA 6-11-0028 Nr. 5855` (working transcription of catalogue form; institutional punctuation/form still to be copied verbatim from the record)
- **record_title:** „Rechnung über die in den Teichen des Amtes Arnshaugk gefangenen Fische von 1536 bis 1540“
- **record_date_or_range:** 1536–1540
- **source_instance_status:** `archive catalogue only / original not yet inspected`
- **catalogue_discovery_url:** `https://www.archive-in-thueringen.de/de/findbuch/view/searchall/Rechnung%2Bamt%2Bborna/bestand/24614/systematik/165332`
- **catalogue_persistence_status:** `stable-looking findbuch route captured; item-level persistent identifier still to verify`
- **digital_object:** `not yet verified`
- **URN / Handle / PURL:** `not yet verified`
- **notes:** Catalogue description mentions Lichtenau and `Treber (Dreba[?])`; the identification Dreba is expressly uncertain in the catalogue context and is not source wording until the archival text is inspected.
- **next verification:** Capture exact item-level catalogue record and provenance; verify digitalisation status; inspect original/digital images; read `Treber` palaeographically and extract account context before any identification is promoted.

### SRC-AR-0002 – LATh EGA 6-11-0032 Nr. 174

- **source_type:** Archivale / Streit-/Mühlenangelegenheit
- **current_shelfmark:** `EGA 6-11-0032 Nr. 174` (Katalogform; vollständig zu verifizieren)
- **record_date_or_range:** 1533
- **working_description:** Volkmannsdorf, Mühlenangelegenheit gegen Amt Ziegenrück
- **source_instance_status:** `archive catalogue only / original not yet inspected`
- **catalogue_persistent_url:** `not yet captured in ledger`
- **persistent_identifier:** `not yet verified`
- **next verification:** vollständigen Katalogtitel, Bestand, Laufzeit, Provenienz und persistenten Datensatz sichern; Quelle inspizieren.

### SRC-AR-0003 – LATh EGA 6-11-0032 Nr. 28

- **source_type:** Archivale / Hutungs-/Triftstreit
- **current_shelfmark:** `EGA 6-11-0032 Nr. 28` (Katalogform; vollständig zu verifizieren)
- **record_date_or_range:** 1555
- **working_description:** Knau/Volkmannsdorf gegen Bucha/Schöndorf wegen Hut/Trift
- **source_instance_status:** `archive catalogue only / original not yet inspected`
- **catalogue_persistent_url:** `not yet captured in ledger`
- **persistent_identifier:** `not yet verified`
- **next verification:** vollständigen Katalogtitel, Bestand, Laufzeit, Provenienz und persistenten Datensatz sichern; Quelle inspizieren.

---

## Regel für neue Einträge

Neue Quellen werden **sofort** mit einer `source_id` angelegt, sobald sie für einen Befund ernsthaft relevant werden. Dabei gilt:

1. Erst bibliographische/archivalische Identität sichern.
2. Dann konkrete Digitalisat-/Nutzungsinstanz dokumentieren.
3. URN/DOI/Handle/ARK/PURL/IIIF und stabilen Katalog-/Landingpage-Link prüfen.
4. Fehlt etwas, `not yet verified` statt Vermutung.
5. Exzerpte referenzieren `source_id`; Findings referenzieren Exzerpt-ID und Source-ID.
6. Katalogbeschreibung, Editionstext, Original und eigene Interpretation bleiben getrennt.
