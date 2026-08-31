# Histo-Orla – Source Identity, Zitier- und Digitalisat-Protokoll

**Status:** `binding-research-protocol / v0.1`  
**Work Owner:** #45  
**Anwendung:** alle Live-Research- und SOTA-Artefakte; insbesondere #46 und #47  
**Stand:** 2026-08-31

## 1. Grundsatz

Histo-Orla dokumentiert Quellen nicht als bloße Literaturhinweise oder URLs. Für jede tragende Quelle werden **Werk/Überlieferung, konkrete digitale oder physische Instanz, Fundstelle und Forschungsnutzung getrennt** erfasst.

```text
historische Quelle / Überlieferungsträger
→ Edition / Katalog / Reproduktion
→ konkrete digitale Instanz / Digitalisat
→ exakte Fundstelle
→ Exzerpt / Beobachtung
→ Finding / Interpretation
```

Eine URL allein ist keine Quellenidentität. Ein Titel allein ist keine Fundstelle. Ein Digitalisat ist nicht mit dem historischen Original gleichzusetzen.

## 2. Wo wird dokumentiert?

### Issue

Das zuständige Issue ist **Work Owner**. Dort stehen:

- Research Question und Scope;
- Status;
- führende Fachdomänen;
- Arbeitsreihenfolge / nächste Aktionen;
- Blocker / Entscheidungen;
- Links auf die kanonischen Research-Artefakte;
- kurze Ergebniszusammenfassung.

**Nicht** im Issue gespiegelt werden vollständige Quellenapparate, lange Exzerpte oder wachsende Source Ledgers.

### Source Ledger

Jede verwendete oder ernsthaft geprüfte Quelleninstanz erhält eine stabile interne `source_id`. Das Source Ledger ist der kanonische Ort für bibliographische, archivalische und digitale Identität.

### Exzerptregister

Jedes relevante Textstück erhält eine eigene `excerpt_id` und verweist auf `source_id`. Dort stehen Wortlaut, Fundstelle, Kontext und quellenkritische Beobachtung.

### Findings

Historische Findings verweisen auf `excerpt_id`/`source_id`. Ein Finding darf nicht nur mit einer nackten URL oder einer unspezifischen Literaturangabe belegt werden.

## 3. Pflichtfelder – Source Identity

Je nach Quellentyp sind mindestens folgende Felder zu prüfen und, soweit vorhanden, zu erfassen:

```text
source_id
source_type
canonical_citation
work_title
creator / author / editor
series / volume
publication_place
publisher
publication_year
edition / version
archive_institution
fonds / collection
series
current_shelfmark
historical_shelfmark_if_relevant
record_title
record_date_or_range
original_copy_status
language
```

Fehlende Informationen werden als `unknown`, `not yet verified` oder `not assigned` markiert – niemals ergänzt oder erraten.

## 4. Persistente Identifikatoren und Verweise

Für jede Quelle/Digitalisatinstanz werden systematisch geprüft:

```text
URN
DOI
Handle
ARK
PURL / persistent permalink
IIIF manifest URL
IIIF canvas / image reference if useful
archive catalogue persistent record URL
library catalogue record / authority ID if useful
ISBN / ISSN (bibliographic identifier, kein Ersatz für persistenten Digitalisatlink)
VD16 / VD17 / VD18 / GW / ISTC / sonstige fachliche Werk-ID, wenn einschlägig
```

Regeln:

1. **Vorhandene URN/DOI/Handle/ARK/PURL werden bevorzugt vor flüchtigen Session-/Viewer-URLs dokumentiert.**
2. Eine URN wird nur eingetragen, wenn sie an der Quelle oder im Katalog tatsächlich verifiziert wurde.
3. Gibt es keinen persistenten Identifier, wird `not found in checked instance` dokumentiert, einschließlich der geprüften Plattform.
4. Bei mehreren Identifikatoren werden sie nebeneinander bewahrt; keiner wird still zum alleinigen „richtigen“ Identifier erklärt.

## 5. Digitalisat-Instanz

Eine digitale Reproduktion erhält eine eigene Instanzbeschreibung:

```text
digital_instance_id
provider / portal
landing_page_url
persistent_url_or_urn
viewer_url_if_needed
direct_file_url_if_stable
IIIF_manifest
access_date
rights / licence statement
scan_completeness
scan_quality_notes
colour / grayscale if relevant
pagination_in_scan
printed_page_to_scan_page_mapping
local_or_uploaded_filename
local_derivative_status
checksum_sha256_if_locally_available
```

Wichtig:

- **Landing Page + persistenter Identifier** sichern, nicht nur einen PDF-Downloadlink.
- Viewer-Seitenzahl und gedruckte Seiten-/Foliozählung werden getrennt gehalten.
- Bei einem Upload ohne bekannte öffentliche Provenienz wird dies ausdrücklich als `user-provided digital instance; public source unresolved` vermerkt.
- OCR/HTR/Textlayer ist ein Derivat und bekommt eigenen Status; er ersetzt die Bildseite nicht.

## 6. Archivquellen

Für Archivgut werden möglichst dokumentiert:

```text
archive_institution
fonds / provenance body
classification / series
current_shelfmark
old_shelfmark / edition concordance
unit_title
inclusive_dates
material / seals / physical description if relevant
digital_catalogue_record
persistent_record_url
digital_object_url / IIIF if available
access_status
```

Eine Editionsangabe wie „HStA Dresden O.U.“ wird nicht still als aktuelle Signatur behandelt. Historische Editionssignatur und heutige Archivsignatur werden getrennt.

## 7. Editionen und Urkundenbücher

Für Editionsbelege zusätzlich:

```text
edition_source_id
charter_or_regest_number
document_date
place_of_issue
page
folio
line_or_section_if_available
editorial_regest
editorial_identification
apparatus_notes_relevant_to_claim
original_or_copy_reference_given_by_edition
prints / regesta / concordances
```

Bei einer Urkunde werden **historischer Wortlaut, editorische Ergänzung, Regest, editorische Ortsidentifikation und eigene Normalisierung** ausdrücklich getrennt.

## 8. Exakte Fundstelle

Ein tragender Textbeleg soll, soweit die Instanz es ermöglicht, mindestens besitzen:

```text
source_id
excerpt_id
Urkunden-/Regestnummer oder archivalische Einheit
Druckseite / Folio
Zeile / Abschnitt, wenn vorhanden
Scan-/Viewer-Seite
stabiler Seiten-/Bildlink, wenn verfügbar
```

Damit soll ein anderer Forscher den Befund ohne Chat und ohne Suchraten wiederfinden können.

## 9. Zitierregel

Die kanonische Zitierung folgt der Fachpraxis des jeweiligen Quellentyps. Histo-Orla speichert zusätzlich maschinen- und menschenlesbare Identität.

Beispielhafte Hierarchie:

```text
Edition vollständig zitieren
→ Urk.-Nr. / Regest-Nr.
→ Datum
→ Seite/Folio/Zeile
→ Überlieferungsnachweis der Edition
→ Digitalisatprovider + URN/PURL/Handle/DOI
→ stabiler Digitalisat-/Kataloglink
→ Zugriff am YYYY-MM-DD
```

Bei Archivgut:

```text
Archiv, Bestand, Signatur, Einheit/Folio
→ Katalogtitel nur als Metadatum
→ persistenter Findbuch-/Kataloglink
→ Digitalisat-/IIIF-Link, falls vorhanden
```

## 10. Quellenkritische Instanztrennung

Jeder Forschungsbeleg erhält einen Status, z. B.:

- `original inspected`
- `digital reproduction of original inspected`
- `scholarly edition inspected`
- `critical apparatus inspected`
- `archive catalogue only`
- `secondary citation only`
- `snippet/discovery only`
- `user-provided scan; public provenance unresolved`

Diese Status dürfen nicht miteinander gleichgesetzt werden.

## 11. Prüfroutine vor Promotion eines Findings

Ein Finding wird nicht als belastbar promoted, bevor geprüft ist:

- [ ] Quellenwerk bibliographisch/archivalisch eindeutig identifiziert?
- [ ] konkrete benutzte Instanz dokumentiert?
- [ ] URN/DOI/Handle/ARK/PURL bzw. persistenter Kataloglink geprüft, soweit die Plattform solche Identifikatoren anbietet?
- [ ] Digitalisat-Landingpage und nicht nur flüchtiger Viewer-/Downloadlink gesichert?
- [ ] exakte Fundstelle mit Seiten-/Folio-/Urkundennummer?
- [ ] Printseite ↔ Scanseite nachvollziehbar?
- [ ] Überlieferungsstatus Original/Kopie/Edition/Katalog getrennt?
- [ ] editorische Ergänzungen und Identifikationen sichtbar?
- [ ] Exzerpt wortlautnah und kontextausreichend?
- [ ] Finding verweist auf konkrete `excerpt_id`/`source_id`?

## 12. Keine falsche Vollständigkeit

`URN not found`, `Digitalisat not found` oder `current shelfmark unresolved` ist nur dann zulässig, wenn die geprüften Portale/Kataloge dokumentiert sind. Ohne definierte Suchgrenze lautet der Status `not yet verified`.

## 13. Anwendung in #46 / #47

Für die Orlagau-Live-Fälle gilt ab jetzt:

- gemeinsame bibliographische/archivalische Quellenidentität im `orlagau-source-ledger.md`;
- textnahe Volltext- und Kontextexzerpte im U2-Exzerptregister bzw. landschaftsspezifischen Artefakt;
- Findings in den jeweiligen Case-Artefakten;
- Issues #46/#47 nur als Work Owner, Status- und Routingebene.
