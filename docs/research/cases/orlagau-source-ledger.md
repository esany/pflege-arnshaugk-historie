# Orlagau – gemeinsames Source Ledger

**Status:** `working-research / source-identity-ledger`  
**Work Owner:** #46 / #47  
**Protokoll:** `docs/research/source-identity-protocol.md`  
**Stand:** 2026-09-03

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

## SRC-ED-0004 – Urkundenbuch der Deutschordensballei Thüringen, Band 1

- **source_type:** wissenschaftliche Edition / Urkundenbuch
- **canonical_citation:** Karl H. Lampe (Hg.), *Urkundenbuch der Deutschordensballei Thüringen. Erster Band*, Thüringische Geschichtsquellen 10 = N. F. 7, Jena: Gustav Fischer, 1936.
- **edition_scope:** erster Band; laut Vorwort Abschluss mit dem Jahr 1311; XVI, 808 S. laut THULB-Metadaten.
- **bibliographic_identity_status:** `verified from inspected title page, preface and THULB object metadata`
- **historical source represented:** mittelalterliche Urkunden und weitere Überlieferungen zur Deutschordensballei Thüringen; jede Urkunde behält eigenen Überlieferungsstatus und Apparatsnachweis.
- **digital_instance_id:** `DI-THULB-HISBEST-00021244`
- **source_instance_status:** `public scholarly-edition scan inspected; page images visually inspected`
- **provider / portal:** Thüringer Universitäts- und Landesbibliothek Jena, Digitale Sammlungen / Thuringica
- **digital_object_landing_page:** `https://collections.thulb.uni-jena.de/receive/HisBest_cbu_00021244`
- **persistent_URN:** `urn:nbn:de:urmel-ba67ebf9-1fe1-4cfe-ba81-aa4d4879f62e6`
- **URN_resolver:** `https://nbn-resolving.org/urn:nbn:de:urmel-ba67ebf9-1fe1-4cfe-ba81-aa4d4879f62e6`
- **MyCoRe_object_id:** `HisBest_cbu_00021244`
- **digital_derivate_id:** `HisBest_derivate_00005363`
- **IIIF_manifest:** `https://collections.thulb.uni-jena.de/api/iiif/presentation/v2/HisBest_derivate_00005363/manifest`
- **catalogue identifiers:** K10plus PPN print `136299725`; electronic edition `736099891`.
- **THULB shelfmark:** `8 Sax.III,18 :10.N.F.7`
- **extent / scan completeness:** THULB metadata `XVI, 808 S.`; IIIF manifest exposes 828 canvases. Completeness beyond the target pages was not independently collated in this pass.
- **rights / licence statement:** THULB landing page displays `CC BY-NC-SA 4.0` for the digital object.
- **access_date:** `2026-09-02`
- **title/imprint verification:** title page visually inspected at scan 5: title, editor, volume, Jena, Gustav Fischer, 1936.
- **target_findspot_verified:** Lampe Nr. 420, printed pp. 360–361 = IIIF images/scans 378–379.
- **target_canvas_labels:** p. 360 `360 - urn:nbn:de:urmel-ba67ebf9-1fe1-4cfe-ba81-aa4d4879f62e6-00005363-3781`; p. 361 `361 - urn:nbn:de:urmel-ba67ebf9-1fe1-4cfe-ba81-aa4d4879f62e6-00005363-3796`.
- **target_image_services:** `https://collections.thulb.uni-jena.de/api/iiif/image/v2/HisBest_derivate_00005363%2FThG_136299725_Thueringische-Geschichtsquellen_1936_10_0378.tif`; `https://collections.thulb.uni-jena.de/api/iiif/image/v2/HisBest_derivate_00005363%2FThG_136299725_Thueringische-Geschichtsquellen_1936_10_0379.tif`.
- **local_derivative_status:** temporary JPEG renditions used only for visual inspection; not canonical and not committed.
- **temporary_rendition_SHA256:** scan 378 `e6cf5afe0af9664d86f963f9eed5526f53b9bdc9ef0ba0224a1ba10b11b9d552`; scan 379 `1dff421b2e27b9f8aa45ae2250fc802879ec520dcc2d8e074d488cdf899ea77a`.
- **edition_caveat:** Lampe's editorial regest identifies `villa in Grune` as Mönchgrün and supplies ordinal numbers `[IV.]` and `[XI.]` for Otto and Hartmann. These are editorial identifications, not words in the charter text. The original and copies cited in the apparatus were not inspected in this pass.
- **next verification:** Resolve the modern archive concordance for historical `HSA Dresden, Orig. No. 1104`; inspect the original or a digital reproduction and the two cited copies if available; collate Schmidt/Alberti/Dobenecker and the relevant personal/place index entries before any broader synthesis.

### DI-IA-THRINGISCHEGES10 – bereitgestellte PDF-Instanz (Pilot 2)

- **digital_instance_id:** `DI-IA-THRINGISCHEGES10`
- **instance relation:** zweite Reproduktion derselben bibliographischen Edition `SRC-ED-0004`; nicht als dieselbe Datei oder derselbe institutionelle Derivatbaum wie die THULB-Instanz behandelt.
- **local_or_uploaded_filename:** `1936-Lampe-ThGQu NF 7.pdf`
- **source_instance_status:** `user-provided PDF inspected; public provenance indicated by embedded metadata, landing page not independently verified in this pass`
- **embedded metadata:** Creator/Producer `Internet Archive`; Keywords nennen `https://archive.org/details/thringischeges10vereuoft`; PDF-Erzeugung laut Metadaten 2024-07-22.
- **checksum_sha256:** `49fd56bf291f520ef6c518bc1a933deab666c2c2c0bd79d0057e374307c14ff5`
- **technical extent:** 64,219,328 Bytes; 832 PDF-Seiten; PDF 1.5; nicht verschlüsselt; keine Formulare oder JavaScript.
- **scan/text layer:** bildbasierter Farb-/Graustufenscan mit eingebettetem OCR-Textlayer. 824 von 832 PDF-Seiten lieferten Text; die Seiten 1–4, 14, 829–830 und 832 lieferten keinen Text. OCR ist für Discovery nützlich, enthält aber erkennbare Fehler und ersetzt die Bildkontrolle nicht (`Lohdehurg`, `E artmann`, `quantitato`, Zeichen-/Spaltenfehler im Register).
- **completeness inspection:** Titelblätter, Vorwort-/Verzeichnisbereich, Beginn des Urkundenteils, Stichproben im Hauptteil, Namenweiser und `Zusätze und Berichtigungen` bis Druckseite 808 wurden inspiziert. Die PDF enthält zusätzlich vordere/hintere Bibliotheks- und Leerseiten. Damit ist der publizierte Umfang `XVI, 808 S.` plausibel vollständig repräsentiert; keine blattweise Kollation gegen ein physisches Exemplar vorgenommen.
- **printed_page_to_pdf_mapping:** im Hauptteil konstant `PDF-Seite = Druckseite + 20`; Kontrollfall Druckseiten 360–361 = PDF-Seiten 380–381.
- **relation_to_THULB_instance:** Druckseiten 360–361 stimmen visuell und textlich mit dem in Pilot 1 inspizierten Editionsinhalt überein. Die THULB-Zuordnung lautet Scan 378–379, die PDF-Zuordnung 380–381; die Differenz entsteht durch zwei zusätzliche Vorsatz-/Bibliotheksseiten der PDF. Dies belegt Inhaltskonkordanz am Kontrollpunkt, nicht Bitidentität oder gemeinsame Scanprovenienz.
- **availability / restartability:** der Uploadpfad ist temporär und kein kanonischer Byte-Speicher. Restartability beruht derzeit auf Checksumme, Dateiname, dokumentierter Instanzidentität und dem weiterhin öffentlich erreichbaren THULB-Objekt; eine dauerhafte autorisierte Ablage/Attachment-Referenz ist noch offen.
- **access_date:** `2026-09-02`
- **rights statement:** im PDF nicht als belastbare Lizenzangabe verifiziert; die THULB-Lizenz darf nicht still auf diese Instanz übertragen werden.

## SRC-LIT-0001 – Peter Sachenbacher, Thüringen östlich der Saale im Mittelalter

- **source_type:** wissenschaftliche Monographie / Sekundärliteratur / Synthese- und Quellenroutingquelle
- **canonical_citation:** Peter Sachenbacher, *Thüringen östlich der Saale im Mittelalter. Archäologisch, mediävistisch, onomastisch, ethnografisch und philosophisch vergleichende Studie zum früh- und hochmittelalterlichen Landesausbau in Territorien der Germania Slavica Thuringiae*, Darmstadt: wbg Academic / Wissenschaftliche Buchgesellschaft, 2022.
- **bibliographic_identity_status:** `verified from inspected imprint text in user-provided PDF instance; public catalogue/persistent identifiers not yet verified`
- **source_instance_status:** `user-provided converted PDF inspected in bounded slices; not a complete citable publication instance`
- **uploaded/local filename:** `2022- Thüringen östlich der Saale im Mittelalter .pdf`
- **publication_place:** `Darmstadt`
- **publisher / imprint:** `wbg Academic / Wissenschaftliche Buchgesellschaft`
- **publication_year:** `2022`
- **ISBN print:** `978-3-534-40649-4`
- **ISBN eBook PDF:** `978-3-534-40650-0`
- **work_genesis:** überarbeitete und aktualisierte Fassung der 2013 an der Friedrich-Schiller-Universität Jena vorgelegten Habilitationsschrift; Habilitationsverfahren 2014 abgeschlossen.
- **digital_instance_id:** `DI-UP-SACHENBACHER-2022-20260903`
- **technical instance notes:** lokal inspizierte Datei im Chat-/Arbeitskontext; PDF-Metadaten der vorliegenden Instanz: PDF 1.3, Creator `Typora`, Producer `macOS Version 26.6.2 (Build 25G83) Quartz PDFContext`, CreationDate `D:20260902173458Z00'00'`; 153 PDF-Seiten; 1,197,267 Bytes; SHA256 `f74c04368acb8a5abb849f56f5d06a1fb9117d20cd8378bddcf7bd1e36ce08bb`.
- **rights / licence statement in inspected imprint:** Text laut Impressum Open Access unter `CC BY International 4.0`; Abbildungen/Buchumschlag ausgenommen.
- **public full-text landing page:** `not yet verified`
- **DNB / library catalogue record:** `not yet verified`
- **URN / DOI / Handle / ARK / PURL:** `not yet verified`
- **IIIF:** `not expected from current uploaded converted PDF; not yet verified for any public instance`
- **pagination / instance caveat:** Die bereitgestellte PDF ist eine konvertierte/reflowartige Arbeitsinstanz, keine Bildseiten-Reproduktion des Buches. PDF-Seiten sind nicht identisch mit Druckseiten. Im Text erscheinen interne Druckseitenmarken, aber nicht jede Druckseiten-Grenze ist in der Textlage sauber auflösbar. Für jedes Exzerpt ist daher `Druckseite laut sichtbarer Marke` von `PDF-Seite der benutzten Instanz` zu trennen; unklare Binnen-Grenzen bleiben `unresolved`.
- **footnote/bibliography caveat:** Im laufenden Text sind Fußnotenziffern sichtbar; die aktuelle PDF-Instanz endet jedoch nach Impressum und den Überschriften `Quelleneditionen` / `Literatur`, ohne die zugehörigen Apparats- und Literaturverzeichnisse zugänglich zu machen. Fußnoten können in dieser Instanz deshalb nur als Ziffern-/Routingmarker genutzt werden. Vollständige Literatur- und Editionsauflösung muss über eine vollständige publizierte Instanz oder andere Katalog-/Bibliothekswege nachgezogen werden.
- **direct_inspection_scope:** In diesem Pass direkt inspiziert: TOC/Impressum, II.5/II.6-relevante PDF-Seiten 62–69 sowie die Titeldaten-/Lizenzstelle auf PDF-Seite 153. Cited sources inside footnotes were not directly inspected.
- **research-use status:** Sekundärquelle, Synthese, Orientierungs- und Quellenroutingquelle; keine Primärquelle und keine automatische historische Wahrheit.
- **current U2 cursor:** II.5 `Die slawische Besiedlung des späteren Orlagaues` page-level/source-routing pass begonnen; erste Slice-Auswertung in `u2-sachenbacher-2022-orlagau-auswertung.md`.
- **next verification:** Vollständige offizielle PDF-/Print- oder Bibliotheksinstanz mit Fußnoten, Quelleneditionen und Literaturverzeichnis sichern; öffentliche bibliographische Identifikatoren und persistente Landingpage verifizieren; danach die in II.5 genannten Fußnoten 101–130 vollständig zu Werken/Editionen/Primärquellen routen.

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
