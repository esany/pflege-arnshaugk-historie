# Source Ledger – Anno II., Richeza, Saalfeld, Siegburg und Bamberg

**Status:** `working-source-ledger / preliminary`  
**Work Owner:** #103  
**Protocol:** `docs/research/source-identity-protocol.md`  
**Stand:** 2026-09-18

Dieses Ledger trennt Werk/Quelle, konkrete digitale Instanz, Inspektionsstatus und Forschungsnutzung. Ein Webfund ist keine Primärquelleninspektion.


## Usage note – observation-first

Die vorhandenen Felder `supports` / `supports_when_inspected` sind in diesem frühen Arbeitsstand **nur als Discovery-/Relevanzhinweise** zu lesen, nicht als promotete Findings oder Synthese. Bei weiterer Bearbeitung werden sie schrittweise durch quellennahe Einträge ersetzt:

`exact findspot → excerpt/claim as stated by source → atomic observation → relation candidate`

Widersprechende Quellen werden nebeneinander geführt. Zotero-Metadaten, Tags und Collections sind Bibliotheks-/Discovery-State und werden nicht als historische Evidenz behandelt.

## ARS-001 – Anno II., Portal Rheinische Geschichte

- **source_id:** `ARS-001`
- **source_type:** modern scholarly biographical article
- **creator:** Matthias Koch
- **work_title:** Anno II. von Köln
- **provider:** LVR / Portal Rheinische Geschichte
- **landing_page:** https://rheinische-geschichte.lvr.de/Persoenlichkeiten/anno-ii.-von-koeln/DE-2086/lido/57adb0c19ebe38.75500234
- **inspection_status:** `full webpage inspected`
- **supports:** Bamberg-Ausbildung und Leitung der Domschule; Kölner Erzstuhl 1056; Gründungs-/Reformkontext Siegburg/Saalfeld
- **limits:** moderne Synthese; konkrete mittelalterliche Rechtsakte müssen an Editionen geprüft werden

## ARS-002 – Richeza, Portal Rheinische Geschichte

- **source_id:** `ARS-002`
- **source_type:** modern scholarly biographical article
- **work_title:** Richeza
- **provider:** LVR / Portal Rheinische Geschichte
- **landing_page:** https://rheinische-geschichte.lvr.de/Persoenlichkeiten/richeza/DE-2086/lido/57cd1e9ba1e476.83090871
- **inspection_status:** `full webpage inspected`
- **supports:** ezzonisches Erbe; Konfliktkontext mit Anno; Saalfeld/Coburg/Orla-Übertragung mit Nutzungsreservat; Tod in Saalfeld; Bestattung in Maria ad Gradus; Fälschungs-/Echtheitsproblem im Klotten-Komplex
- **limits:** Urkundenidentität und einzelne Echtheitsurteile auf zugrunde liegende Edition/Forschung zurückzuführen

## ARS-003 – Richeza, Neue Deutsche Biographie / Deutsche Biographie

- **source_id:** `ARS-003`
- **source_type:** scholarly reference biography
- **canonical_citation:** Richeza, in: Neue Deutsche Biographie / Deutsche Biographie
- **landing_page:** https://www.deutsche-biographie.de/sfz30920.html
- **inspection_status:** `full webpage inspected`
- **supports:** Alleinerbin seit 1047; Saalfeld als später Aufenthaltsort; Übertragung Saalfeld/Coburg 1056 unter lebenslänglicher Nutzung; Bestattung durch Anno in Maria ad Gradus
- **limits:** der Onlineeintrag integriert auch ältere ADB-Passagen; Aussagen sind nach Autor-/Abschnitt zu unterscheiden

## ARS-004 – Mainzer Urkundenbuch I

- **source_id:** `ARS-004`
- **source_type:** scholarly source edition
- **creator/editor:** Manfred Stimming
- **work_title:** Mainzer Urkundenbuch. Bd. 1: Die Urkunden bis zum Tode Erzbischof Adalberts I. (1137)
- **publication_place:** Darmstadt
- **publication_year:** 1932
- **provider:** dilibri / Landesbibliothekszentrum Rheinland-Pfalz
- **landing_page:** https://www.dilibri.de/rlb/content/titleinfo/2028
- **persistent_identifier:** `urn:nbn:de:0128-1-69286`
- **target_findspot:** Nr. 331, S. 223–226 (1071), Saalfeld
- **inspection_status:** `digital edition identified; target no. 331 not yet fully inspected in this work pass`
- **supports_when_inspected:** Rollen/Rechte von Anno II. von Köln und Siegfried I. von Mainz; Gründungs-/Umwandlungsakt; Besitz-/Kirchenrechte
- **limits:** editorischer Überlieferungsstatus und Kopien-/Bestätigungsabhängigkeit müssen vor Finding-Promotion dokumentiert werden

## ARS-005 – Lampert von Hersfeld, Annales, Jahr 1071

- **source_id:** `ARS-005`
- **source_type:** medieval narrative source; inspected through modern English edition/translation preview
- **historical_creator:** Lampert von Hersfeld
- **modern_editor/translator:** I. S. Robinson
- **work_title:** The Annals of Lampert of Hersfeld
- **publication_year:** 2015
- **target_findspot:** annal for 1071, modern edition pp. 152–154
- **publisher_preview:** https://api.pageplace.de/preview/DT0400.9781526112606_A40541557/preview-9781526112606_A40541557.pdf
- **inspection_status:** `relevant translated passage and editorial notes inspected; Latin critical edition instance still to bind`
- **supports:** canons→monks transition; monks from Siegburg and St. Pantaleon; Lampert's own visit and evaluation of observance
- **limits:** narrative rhetoric and Lampert's anti-novelty position; `expulsion` wording is challenged by editorial note/other tradition

## ARS-006 – Lampert von Hersfeld, Deutsche Biographie

- **source_id:** `ARS-006`
- **source_type:** scholarly reference biography
- **landing_page:** https://www.deutsche-biographie.de/gnd10095135X.html
- **inspection_status:** `full webpage inspected`
- **supports:** 1071 information journey to Saalfeld/Siegburg; critical evaluation of reform; later relation to Mainz/Hasungen
- **limits:** secondary synthesis

## ARS-007 – Gunther von Bamberg, Deutsche Biographie

- **source_id:** `ARS-007`
- **source_type:** scholarly reference biography
- **canonical_citation:** Emil E. Ploß, „Gunther“, NDB 7 (1966), S. 323 f.
- **landing_page:** https://www.deutsche-biographie.de/sfz69963.html
- **inspection_status:** `full webpage inspected`
- **supports:** Bishop Bamberg 1057–1065; alignment with Anno; Anno as former leader of Bamberg cathedral school; pilgrimage with Siegfried of Mainz
- **limits:** older biographical synthesis; precise interaction episodes need primary/charter corroboration

## ARS-008 – Dieter J. Weiss, Kloster Michelsberg und Stadt Bamberg

- **source_id:** `ARS-008`
- **source_type:** scholarly secondary study
- **creator:** Dieter J. Weiss
- **work_title:** Das Kloster Michelsberg und die Stadt Bamberg
- **container:** Das Bistum Bamberg in der Welt des Mittelalters
- **publication_year:** 2007
- **provider:** Universität Bamberg
- **digital_instance:** https://www.uni-bamberg.de/fileadmin/zemas/PDF-Dateien/BIMS_VV_1_Weiss.pdf
- **inspection_status:** `relevant early-history and reform passages inspected`
- **supports:** Michelsberg as early Bamberger episcopal monastery; source-critical warning on forged foundation tradition; Hirsau reform under Abbot Wolfram from 1112
- **limits:** no direct Michelsberg→Saalfeld relation found in inspected passages; absence claim bounded to this and linked searches

## ARS-009 – Thüringen östlich der Saale im Mittelalter, DDE

- **source_id:** `ARS-009`
- **source_type:** digital scholarly/regional synthesis
- **work_title:** Thüringen östlich der Saale im Mittelalter
- **provider:** ULB TU Darmstadt / DDE
- **landing_page:** https://exist.ulb.tu-darmstadt.de/2/v/pa000017-0007
- **inspection_status:** `relevant Saalfeld section inspected`
- **supports:** ezzonische Besitzfolge; 1056 transfer; 1063 canonry; 1071 conversion to Benedictine monastery; Cologne's regional possession
- **limits:** one cited Coburg cartulary description is itself flagged as probably forged; individual claims need source-level control

## ARS-010 – Saalfeld archaeology / DGAMN article

- **source_id:** `ARS-010`
- **source_type:** scholarly archaeological article
- **work_title:** Saalfeld/Thüringen: Ein Werkplatz im Areal des ...
- **provider:** Heidelberg Journals / DGAMN
- **digital_instance:** https://journals.ub.uni-heidelberg.de/index.php/mitt-dgamn/article/view/17141/10956
- **inspection_status:** `discovery/relevant section only`
- **supports:** material/topographic development from earlier complex to Benedictine St. Peter und Paul; economic/mint context
- **limits:** complete article metadata and full argument still to log before consequential use

## ARS-011 – Siegburg institutional history

- **source_id:** `ARS-011`
- **source_type:** institutional historical presentation
- **work_title:** Gründung der Abtei
- **provider:** Förderverein Michaelsberg e.V., Siegburg
- **landing_page:** https://www.foerderverein-michaelsberg.de/abteigeschichten/gruendung-der-abtei
- **inspection_status:** `webpage inspected`
- **supports:** Siegburg as Annos reform centre; institutional memory of Saalfeld 1071 and Grafschaft 1072 as foundations from Siegburg
- **limits:** institutional presentation; use as orientation, not sole evidence for legal status

## ARS-012 – Vita Annonis minor, image witness

- **source_id:** `ARS-012`
- **source_type:** medieval hagiographical manuscript / later memorial witness
- **work_title:** Vita Annonis minor
- **date:** ca. 1183
- **repository:** Universitäts- und Landesbibliothek Darmstadt
- **shelfmark:** Hs 945
- **findspot:** fol. 1v
- **digital_discovery_instance:** LVR Portal Rheinische Geschichte, ARS-001
- **inspection_status:** `image/discovery inspected; manuscript context not yet directly inspected`
- **supports:** late-12th-century Anno memoria representing five foundations including Saalfeld and Siegburg
- **limits:** canonization-era hagiographical/memorial source, not contemporary legal proof of foundation status

## Open source-identity work

- Exact edition/instance and transmission note for Richeza's 1056 Saalfeld disposition.
- Full MUB I Nr. 331 text and apparatus.
- Latin critical Lampert edition for the 1071 passage.
- 1124/1125 papal/Mainz confirmations and exact relation to 1071 rights.
- Later royal/papal privileges relevant to `Reichsabtei` / immunity / abbatial rights.
- Michelsberg archival/necrological/personnel sources only if a positive Bamberg→Saalfeld hook emerges.


## ARS-013 – Ezzo, Portal Rheinische Geschichte

- **source_id:** `ARS-013`
- **source_type:** modern scholarly biographical article
- **creator:** Matthias Koch
- **work_title:** Ezzo
- **provider:** LVR / Portal Rheinische Geschichte
- **landing_page:** https://rheinische-geschichte.lvr.de/Persoenlichkeiten/ezzo-/DE-2086/lido/57c6a72fc81e80.76712142
- **inspection_status:** `full webpage inspected`
- **relevance:** marriage to Mathilde; modern synthesis names Coburg, Salz and Orlamünde as dowry; conflict with Heinrich II over Mathilde/Otto III inheritance; later grant of Kaiserswerth, Duisburg and Saalfeld as free property; Ezzo's death at Saalfeld
- **limits:** the three-place dowry list is a modern synthesis, not an explicit list in the inspected contemporary Thietmar passage; Salz has separate scholarly/source-critical support, while the status of Coburg and especially Orlamünde requires further primary-source checking

## ARS-014 – Ezzo, Neue Deutsche Biographie / Deutsche Biographie

- **source_id:** `ARS-014`
- **source_type:** scholarly reference biography
- **creator:** Mathilde Uhlirz
- **work_title:** Ezzo (Erenfrid)
- **container:** Neue Deutsche Biographie 4 (1959), S. 715–716
- **landing_page:** https://www.deutsche-biographie.de/gnd124283209.html
- **inspection_status:** `full webpage inspected`
- **relevance:** settlement with Heinrich II; Kaiserswerth, Duisburg and Saalfeld as free property; Ezzo's last years in Saalfeld
- **limits:** older scholarly synthesis; documentary chain to be rechecked against editions/regesta

## ARS-015 – Saalfeld, Residenzstädte im Alten Reich

- **source_id:** `ARS-015`
- **source_type:** scholarly digital reference article
- **work_title:** Saalfeld
- **provider:** Niedersächsische Akademie der Wissenschaften zu Göttingen
- **landing_page:** https://adw-goe.de/la/digitale-bibliothek/residenzstaedte-im-alten-reich-1300-1800/id/RESIST-HB1-BD1-ART136
- **inspection_status:** `relevant historical section inspected`
- **relevance:** Saalfeld as royal court/palatine site; transfer to Ezzo in 1013; location at crossing of pass roads and west-east route
- **limits:** concise synthesis; transport significance before 1100 requires separate source/archaeological control

## ARS-016 – Historische Städtelandschaft Franken, Coburg 1056

- **source_id:** `ARS-016`
- **source_type:** scholarly regional historical database entry
- **provider:** Universität Würzburg / Historisches Unterfranken
- **landing_page:** https://www.historisches-unterfranken.uni-wuerzburg.de/staedte/staedte-results.php?jahr_anfang=&jahr_ende=&max_eintraege=10&name=&sache=&stadt=87
- **inspection_status:** `relevant entry inspected`
- **relevance:** records the 1056 joint transfer of Saalfeld and Coburg to Cologne; cites Zeugnisse zur Coburger Geschichte im Mittelalter (1983)
- **limits:** database synthesis, not direct inspection of the underlying charter/tradition


## ARS-017 – Hlawitschka, Königin Richeza von Polen

- **source_id:** `ARS-017`
- **source_type:** scholarly source-critical study
- **creator:** Eduard Hlawitschka
- **work_title:** Königin Richeza von Polen – Enkelin Herzog Konrads von Schwaben, nicht Kaiser Ottos II.?
- **container:** Institutionen, Kultur und Gesellschaft im Mittelalter. Festschrift für Josef Fleckenstein
- **publication_year:** 1984
- **digital_instance:** https://www.mgh-bibliothek.de/dokumente/a/a089482.pdf
- **inspection_status:** `relevant sections on Salz and Richeza property inspected`
- **exact_findspots:** pp. 241–243 in article pagination / PDF pp. 21–23
- **relevance:** distinguishes several components of the royal property complex at Salz; argues that Richeza/Ezzo/Mathilde held only a specific `predium/curtis` there; reads the 1057/58 Würzburg precariae as compatible with Salz having reached Mathilde/Ezzo as marriage equipment; separately recalls the Saalfeld/Coburg donation to Cologne
- **critical_note:** the contemporary Thietmar passage cited by Hlawitschka says only that Otto III gave Ezzo/Mathilde many goods so that Mathilde's high birth would not be diminished; it does not enumerate Coburg, Salz and Orlamünde individually
- **limits:** this study does not by itself verify Orlamünde as a separately enumerated dowry estate
