# C1 – Quellen-/Archivlogik, Provenienz, Überlieferung und Fundstellen

**Work Owner:** #31  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** Archivistik, Registraturkunde, Diplomatik, Editionswissenschaft/Textkritik.  
**Controlling competencies:** RDM/Provenienz, Bibliographie/Informationswissenschaft, Landes-/Verwaltungsgeschichte, regionale Archivkunde.

## 1. Research Questions

Diese Analyse beantwortet primär RQ-C1-01 bis RQ-C1-04 aus `docs/research/discovery/research-questions.md`:

1. Welche Provenienz-/Kontextprinzipien sind fachlich notwendig?
2. Wie lässt sich Archive Routing aus historischer Verwaltung/Herrschaft ableiten?
3. Welche Unterscheidungen braucht Histo-Orla zwischen Quelle, Überlieferungsstufe, Edition/Regest und digitaler Instanz?
4. Welche minimale Fundstelleninformation braucht ein überprüfbarer Befund?

## 2. Search Scope / Boundary

Geprüft wurden:

- aktuelle internationale Archivbeschreibungsstandards und fachnahe Standards;
- archivwissenschaftliche Beschreibung von Records/Creators/Instantiations;
- regionale Findmittel und Archivbeschreibungen für Thüringen/Arnshaugk als U1-Probe;
- konkrete Findmittelbefunde zu Teich-/Fischerei-/Amtssachen im 16. Jahrhundert;
- Hinweise auf Retrokonversion, Pertinenzordnung und Überlieferungsverluste als Grenzen von Online-Recherche.

Nicht beansprucht wird:

- vollständige Bestandsaufnahme aller Archive für Arnshaugk/Orla/Vogtland;
- Einsicht der gefundenen Archivalien selbst;
- abschließende Entscheidung für RiC, DACS, EAD, TEI oder ein Datenmodell.

## 3. Authoritative / inspected sources

### International / archival description

- International Council on Archives, **Records in Contexts – Foundations of Archival Description**: https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-foundations-of-archival-description/
- ICA, **RiC-O 1.0.2**: https://www.ica.org/standards/RiC/RiC-O_1-0-2.html
- ICA, **RiC Application Guidelines**: https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-application-guidelines/
- Society of American Archivists, **Describing Archives: A Content Standard (DACS)**: https://www2.archivists.org/groups/technical-subcommittee-on-describing-archives-a-content-standard-dacs/describing-archives-a-content-standard-dacs-second-

### Regional / direct archival discovery

- Stadtarchiv Neustadt an der Orla: https://www.archive-in-thueringen.de/de/archiv/view/id/79
- Landesarchiv Thüringen, Ernestinisches Gesamtarchiv, Reg. Ff (Ämter und Ortschaften): https://www.archive-in-thueringen.de/de/findbuch/view/bestand/24618/systematik/145373
- Landesarchiv Thüringen, Ernestinisches Gesamtarchiv, Reg. Aa (Finanzangelegenheiten), Teich-/Fischereisachen: https://www.archive-in-thueringen.de/de/findbuch/view/searchterm/Eilenburg/submit/submit/page/11/bestand/24613/systematik/260374
- Reg. Aa, „Anrichtung, Ausführung und Besserung der Teiche und Teichstädte“: https://www.archive-in-thueringen.de/en/findbuch/view/searchterm/Eilenburg/submit/submit/page/41/bestand/24613/systematik/260374/archivgut/5490225/searchall/Eilenburg
- Ernestinisches Gesamtarchiv, Reg. Bb (Rechnungen): https://www.archive-in-thueringen.de/de/findbuch/view/searchall/Rechnung%2Bamt%2Bborna/bestand/24614/systematik/165332
- Geheimes Archiv Altenburg – Retrokonversion noch laufend: https://www.archive-in-thueringen.de/de/findbuch/view/bestand/21699
- Stadtarchiv Eisenach – dokumentierte Kriegsverluste: https://www.archive-in-thueringen.de/de/archiv/view/id/221

## 4. Findings

### F-C1-01 – Provenienz und Kontext sind fachliche Kernanforderungen, nicht bloße Metadatenoptionen

RiC modelliert archivalische Beschreibung ausdrücklich kontextuell und unterscheidet Record Resources von ihren **Instantiations**. Ein Record kann mehrere Instantiations gleichzeitig oder über die Zeit besitzen; eine Instantiation kann von einer anderen abgeleitet sein. Das stützt direkt die Histo-Orla-Trennung:

```text
historische Quellen-/Record-Identität
≠
konkreter Überlieferungsträger / Instantiation
≠
digitales Derivat
```

DACS ist zugleich bewusst **output-neutral** und beschreibt sowohl Archivgut als auch dessen creators. Das ist für Histo-Orla wichtiger als ein bestimmtes Encoding: Zuerst muss der fachliche Kontext erhalten werden; die technische Repräsentation kann später gewählt werden.

**Implikation:** Histo-Orla braucht eine Capability, archivalischen/bibliographischen Gegenstand und konkret inspizierte Instanz auseinanderzuhalten. RiC/DACS sind SOTA-Referenzen, aber noch keine Architekturentscheidung.

### F-C1-02 – Aktuelle RiC-Dokumentation zeigt selbst, dass Standards versions- und reifestatussensibel behandelt werden müssen

Die ICA-Seite zu RiC-FAD bezeichnet die ersten drei Teile FAD/CM/O als stabile 1.0-Fassung von 2023 und erwähnt Application Guidelines. Die aktuelle eigene RiC-AG-Seite führt RiC-AG 0.1 jedoch als **Draft** und lädt zur Community-Rückmeldung ein.

**Implikation:** Standards dürfen nicht nur nach Namen übernommen werden; Version, Reifestatus und konkret verwendeter Teil müssen provenance-seitig mitgeführt werden. Für Histo-Orla reicht in dieser Phase der methodische Befund: Kontext/Records/Agents/Instantiations/Relations sind fachlich relevante Unterscheidungen.

### F-C1-03 – Regionales Archive Routing muss Provenienz- UND Pertinenzgeschichte kennen

Das Stadtarchiv Neustadt an der Orla dokumentiert, dass neben städtischer Provenienz auch Unterlagen des **Amtes Arnshaugk** und des späteren Neustädtischen Kreises in das Historische Archiv eingingen. Um 1840 wurde der Aktenbestand nach dem **Pertinenzprinzip** in 25 Kapitel geordnet.

Das ist für Histo-Orla ein harter regionaler Befund:

- heutiger Verwahrort ≠ ursprünglicher Registraturbildner;
- heutige Systematik kann eine ältere Pertinenzordnung sein;
- eine Suche nur nach modernem Archiv-/Bestandsnamen reicht nicht;
- historische Verwaltung und spätere Archivordnung müssen gemeinsam rekonstruiert werden.

**Capability implication:** Archive Routing muss mindestens `historischer Akteur/Institution → Funktion/Zuständigkeit → mögliche Registratur/Bestände → heutige Verwahrorte/Ordnungen` unterstützen.

### F-C1-04 – U1 bestätigt, dass serielle/verwaltungskontextuelle Recherche viel ergiebiger ist als „alte Karten suchen“

Im Ernestinischen Gesamtarchiv sind in verschiedenen systematischen Gruppen direkte Arnshaugk-/Teichbefunde erschlossen. Wichtig: Dies sind **Findmittelbefunde, keine gelesenen Quelleninhalte**.

Beispiele:

1. **Reg. Ff, Archivalien-Signatur 9a, Bestand 6-11-0032, 1556–1557:** Verhandlungen mit Melchior Holzer und Adam von Stein in Moderwitz wegen Anlage eines neuen Teiches „in der wolchen und auf der pleten“ im Amt Arnshaugk.
2. **Reg. Aa, nach 1517:** Bericht über neue Teiche in den Ämtern Arnshaugk und Weida.
3. **Reg. Aa, 1525:** Verzeichnis der Besetzung der Teiche im Amt Arnshaugk.
4. **Reg. Aa, 1536–1537:** Verzeichnis des Fischmeisters über die Besetzung der Teiche im Amt Arnshaugk.
5. **Reg. Aa, 1569:** Ankauf eines „in der Blotte im Amt Arnshaugk“ gelegenen Teiches und zweier Teichlein daneben.
6. **Reg. Bb, 1533–1535:** Fischrechnungen, darunter Rechnungen eines Teichs vor der Heide bei Triptis im Amt Arnshaugk.
7. Zusätzlich im selben archivischen Umfeld: Hut-/Triftstreitigkeiten, Fronbücher, Amts-/Finanz- und Fischereiserien.

**Methodische Bedeutung:** Die ursprüngliche U1-Frage nach historischen Teichen führt fachlich nicht primär zu einem Kartentyp, sondern zu mehreren administrativen Funktionsserien: Bau/Anlage, Finanzierung, Besetzung/Fischerei, Rechnungen, Besitz, Streit, Amtshandeln, Grenz-/Nutzungsfragen.

**Nächste U1-Forschungsaktion:** Die genannten Findmittelpositionen sind konkrete Bestell-/Einsichtskandidaten. Ihre Inhalte dürfen erst nach tatsächlicher Einsicht als historische Evidenz verwendet werden.

### F-C1-05 – Online-Nichtfinden ist kein Bestands-/Quellen-Negativbeweis

Das Geheime Archiv Altenburg weist 2025 ausdrücklich darauf hin, dass die Retrokonversion eines handschriftlichen Behördenverzeichnisses **noch läuft** und online nur Teile enthalten sind. Das Stadtarchiv Eisenach dokumentiert erhebliche Verluste durch Kriegseinwirkung.

Daraus folgen zwei getrennte Failure Modes:

```text
nicht online erschlossen
≠
nicht im Archiv vorhanden

nicht überliefert
≠
historisch nicht existent
```

**Requirement implication:** Negative Findings brauchen eine Search Boundary inklusive Online-Erschließungsgrad, konsultierter Findmittel und bekannter Überlieferungsverluste.

### F-C1-06 – Die minimale Provenienz-/Fundstelleninformation hängt vom Quellentyp ab, besitzt aber einen gemeinsamen Kern

Aus den Standards und U1–U4 ergibt sich als **fachliche Mindestmenge**, noch ohne technisches Schema:

#### Archivalische Quelle

- Archiv / Repository
- Bestand / Fonds bzw. aktueller Beschreibungskontext
- Signatur / Identifier der Archivalieneinheit
- Titel/Verzeichnungstext soweit vorhanden
- Datierung
- konkrete Fundstelle innerhalb der Einheit, sobald eingesehen: Blatt/Folio/Seite/Teil/Einlage o. ä.
- Überlieferungs-/Repräsentationsstatus, soweit relevant
- exakt inspizierte digitale/physische Instanz bzw. Zugriffskontext
- bei digitalem Derivat: Ableitung/Verarbeitung getrennt

#### Edition / Regestenwerk / gedruckte Quelle

- bibliographische Identität / Ausgabe
- Band/Teil/Auflage, soweit nötig
- Seite/Regest-/Dokumentnummer
- editorischer Status (Edition/Regest/Transkription etc.)
- konkret verwendete digitale/physische Instanz

#### Bild-/OCR-Derivat

- Parent Source/Instance
- Seite/Folio/Region
- Derivattyp und Erzeugungsweg
- OCR/HTR-Version bzw. Verarbeitung, wenn consequential
- Korrektur-/Normalisierungsstatus

**Wichtig:** Ein persistenter Identifier, eine Archivsignatur oder URL ersetzt nicht die Information, welche konkrete Instanz tatsächlich geprüft wurde; umgekehrt ersetzt ein Datei-Hash nicht die institutionelle/bibliographische Identität.

## 5. Archive-Routing-Heuristik v0.1

Für konkrete historische Recherche soll Histo-Orla nicht nur Sachbegriffe expandieren, sondern diese Kette erzeugen können:

```text
historische Frage / Objekt
→ Zeitfenster
→ historische Herrschaft / Amt / Gut / Institution / Funktion
→ mögliche record creators / Registraturzusammenhänge
→ einschlägige Funktionsserien und Quellengattungen
→ spätere Verwaltungs-/Territorialtransformationen
→ mögliche heutige Archive / Fonds / Pertinenzbestände
→ Online-Findmittel + ältere/analoge Findmittel
→ konkrete Archivalienkandidaten
→ Search Boundary / Überlieferungsgrenzen
```

U1-Beispiel „Teich“:

```text
Teich / Gewässerstruktur
→ Amt Arnshaugk / Guts-/Kirchen-/Gemeindezuständigkeit
→ Finanz-/Fischerei-/Bau-/Besitz-/Grenz-/Hutungs-/Mühlenfunktion
→ Reg. Aa / Reg. Bb / Reg. Ff / lokale Amts- oder Stadtüberlieferung / weitere Provenienzen
→ konkrete Verzeichnungseinheiten
```

## 6. Source / Transmission Distinction Matrix v0.1

| Ebene | Beispiel | Darf als historische Primärevidenz behandelt werden? |
|---|---|---|
| Archivalische Original-/zeitgenössische Überlieferung | Amtsakte, Rechnung, Karte | nach Quellenkritik: ja |
| zeitgenössische Abschrift/Kopialüberlieferung | Kopialbuch | eigene Überlieferungsstufe; nicht identisch mit verlorener Vorlage |
| wissenschaftliche Edition | Urkundenedition | qualifizierte Repräsentation, nicht Originalinstanz |
| Regest | Regestenwerk | erschließende Zusammenfassung, nicht vollständiger Quellenwortlaut |
| Findmittel/Katalog | Archivportal-Eintrag | Discovery-/Metadatenbeleg, kein Beleg für den Inhalt der Akte |
| Digitalisat/Scan | Seitenbild | Instantiation/Repräsentation der Quelle; Qualität/Vollständigkeit prüfen |
| OCR/HTR | Textderivat | Such-/Arbeitsderivat, nicht Originalbefund |
| normalisierter/korrigierter Text | Forschungsderivat | getrennt vom Raw OCR/Quellentext |
| KI-Zusammenfassung | Assistenzoutput | keine Evidenzklasse |

## 7. Challenge des internen Prior Art

### `paleo-type`

Bestätigt wurden fachlich:

- Original/Derivat/Interpretation trennen;
- Persistent Identifier ≠ exact inspected file;
- Evidence Status statt Source Laundering;
- „nicht gefunden“ nur mit Search Boundary.

**Nicht übernommen:** konkrete Tabellen, IDs, RiC-/TEI-Strukturen oder Corpus-Gates.

### RGK

Claim/Evidence/Interpretation und projektbezogene Quellenfunktion bleiben plausible Muster, werden aber nicht aus C1 als Datenmodell abgeleitet. C1 bestätigt nur, dass Überlieferungs-/Beschreibungskontext und tatsächlicher Research Use getrennt werden müssen.

## 8. Capability Candidates

- `CAP-SOURCE-IDENTITY`: Quelle/Record, Repräsentation/Instantiation und Forschungsderivat unterscheiden.
- `CAP-ARCHIVE-ROUTING`: aus historischem Verwaltungs-/Funktionskontext Archive/Fonds/Serien ableiten.
- `CAP-FINDSPOT`: Findings zuverlässig auf konkrete Fundstellen/Instanzen zurückführen.
- `CAP-SEARCH-BOUNDARY`: Reichweite/Erfassungsgrad einer Archiv-/Portalrecherche dokumentieren.
- `CAP-TRANSMISSION-CONTEXT`: Überlieferungsstufe und Ableitungsbeziehungen sichtbar halten.

## 9. Quality / Acceptance implications

1. Kein archivischer Claim ohne Repository/Fonds/Signatur bzw. angemessene Quellenidentität.
2. Findmittelbefund darf nicht als gelesener Quelleninhalt promoted werden.
3. Bei eingesehener Quelle muss konkrete Fundstelle/Instanz nachvollziehbar sein, soweit Quelle dies erlaubt.
4. Digital-/OCR-Derivat muss auf Parent Source/Instance zurückführen.
5. Negative Finding muss Search Boundary und bekannte Erschließungs-/Überlieferungsgrenzen nennen.
6. Archive Routing muss historische Zuständigkeiten und spätere Pertinenz-/Bestandsbildung berücksichtigen.

## 10. Requirement Candidates

- REQ-C1-A: System muss Source Identity, inspected instance und derivative getrennt repräsentierbar machen.
- REQ-C1-B: Jeder consequential Finding muss eine nachvollziehbare Source/Findspot-Kette besitzen.
- REQ-C1-C: Archivsuche muss historische Verwaltungs-/Provenienzkontexte als Research Input unterstützen.
- REQ-C1-D: `not found` darf ohne dokumentierte Search Boundary nicht als Vollständigkeits-/Abwesenheitsaussage gelten.
- REQ-C1-E: Discovery-Metadaten (Findmittel) und tatsächlich inspizierte Evidenz müssen verschiedene Status besitzen.

Noch keine Entscheidung über Datenbank, RiC, EAD, TEI, Zotero oder konkrete Persistenzform.

## 11. Offene Fragen / bounded debt

- Vollständige regionale Provenienz-/Archivkarte Arnshaugk/Neustadt/Orla/Vogtland ist noch zu erarbeiten; für Architecture Baseline nicht blockierend.
- Konkrete Einsicht der identifizierten Arnshaugk-Teichakten ist historische U1-Forschung, nicht Voraussetzung für das System-Requirement.
- RiC-AG-Reifestatus ist in aktuellen ICA-Seiten nicht völlig konsistent dargestellt; Histo-Orla stützt sich deshalb derzeit nur auf die stabilen Grundprinzipien, nicht auf AG als verbindliche Implementation Specification.
- Rechte/Bestell-/Digitalisierungsbedingungen werden in #40/#39 tool-/archivspezifisch behandelt.

## 12. #45 Quality Check

- **Domain fit:** Archivistik/Registraturkunde/Diplomatik führen; RDM nur unterstützend.
- **Evidence fit:** Standards und offizielle Archivfindmittel wurden direkt inspiziert; Findmittelbefunde werden als solche gekennzeichnet.
- **Inference fit:** Aus Katalogeinträgen werden keine historischen Sachbehauptungen über Akteninhalt jenseits der Verzeichnung abgeleitet.
- **Terminology fit:** Provenienz/Pertinenz, Record/Instantiation, Edition/Regest/Findmittel werden getrennt.
- **Provenance fit:** Quellenlinks und konkrete Signaturen/Datierungen der relevanten U1-Funde sind dokumentiert.
- **Falsification/challenge:** Konkrete Akten müssen eingesehen werden; alternative/archive routes und unvollständige Online-Erschließung bleiben offen.

## 13. Sättigungsbegründung

Für die aktuelle Capability-/Requirements-Entscheidung ist C1 ausreichend gesättigt: internationale Standards und regionale reale Findmittel bestätigen dieselben Kernbedarfe – Kontext/Provenienz, Source-vs-Instantiation, findspotfähige Referenzierung, Archive Routing und Search Boundaries. Weitere Archivstandards oder zusätzliche U1-Funde würden voraussichtlich die regionale Research Map erweitern, aber die architecture-driving wissenschaftlichen Invarianten nicht wesentlich verändern.
