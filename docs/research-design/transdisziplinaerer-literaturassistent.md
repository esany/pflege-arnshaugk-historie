# Histo-Orla – transdisziplinäre historische Forschungsassistenz

**Status:** aktueller konsolidierter Konzept- und Arbeitsstand; noch keine finale Architektur  
**Letzte grundlegende Überarbeitung:** 2026-08-30  
**Zentrale Issues:** #1, #9, #10, #13–#16, #19–#21

---

## 1. Zweck

Dieses Dokument ist der versionierte, menschenlesbare Konzeptstand für die Forschungsumgebung im Projekt *Pflege Arnshaugk / Histo-Orla*.

Die ursprüngliche Idee eines „persönlichen Archivars“ wurde erweitert und korrigiert. Der Archivar bleibt eine wichtige Spezialkompetenz für Bestand, Provenienz, Erschließung, Fundstellen und Recherche – er ist aber **nicht das gesamte Zielsystem und keine epistemische Oberinstanz**.

Das Ziel ist eine transdisziplinäre historische Forschungsassistenz, die einen historisch interessierten Research Owner ohne vorausgesetzte Spezialausbildung dabei unterstützt,

- belastbare Quellen und Forschungsliteratur zu finden und zu erschließen,
- fachwissenschaftliche Probleme überhaupt erst präzise zu formulieren,
- die richtigen Begriffe, Gegenstandsmodelle, Methoden und Quellenlogiken der beteiligten Disziplinen zu aktivieren,
- regionale Befunde in territorialen, reichsweiten und europäischen Zusammenhängen zu erklären,
- Befund, Interpretation, Kontroverse, Unsicherheit und Evidenzgrenze sichtbar zu halten,
- und einen dauerhaft nachvollziehbaren wissenschaftlichen Forschungszustand zu erzeugen.

**Leitgedanke:**

> Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.

---

## 2. Forschungsziel und Scope

### 2.1 Geschichte als transdisziplinäres Querschnittsthema

Der Forschungsgegenstand ist nicht auf eine einzelne Epoche oder Disziplin begrenzt. Relevante Perspektiven umfassen insbesondere:

- Sozialgeschichte
- Wirtschafts- und Agrargeschichte
- Herrschafts-, Adels-, Hof- und Verwaltungsgeschichte
- Reichs- und Territorialgeschichte
- Diplomatie-, Netzwerk-, Mobilitäts- und Reisegeschichte
- Kirchengeschichte / Konfessionsgeschichte
- historische Geographie und Kulturlandschaft
- Umweltgeschichte / historische Ökologie / Hydrologie
- Archäologie, Siedlungs- und Landschaftsarchäologie
- Volkskunde / Europäische Ethnologie
- historische Anthropologie und Sachkulturforschung
- Onomastik / Toponymie
- historische Kartographie
- Bau- und Architekturgeschichte / Denkmalpflege bei Bedarf
- historische Demographie und Rechtsgeschichte bei Bedarf

Zeitlich reicht der Horizont vom Früh-/Hochmittelalter über Spätmittelalter und Frühe Neuzeit bis in Übergänge zur Moderne.

### 2.2 Regional verankert, europäisch verflochten

Der regionale Raum ist **Anker, nicht analytische Grenze**.

```text
Mikro / Ort / Gut / Familie
        ↓↑
Region / Herrschaft / Territorium
        ↓↑
Reich / dynastische und konfessionelle Räume
        ↓↑
Europa / Höfe / Universitäten / Diplomatie / Militär / Reisen
```

Leitformel:

> **Regionaler Fokus für Tiefenschärfe – europäischer Horizont für Erklärung.**

Kernräume sind Ostthüringen/Orla, Vogtland, Saalfeld und angrenzende thüringische Räume, Sachsen/Kursachsen, Franken, Egerland, Lausitz/Bautzen; weitere Räume werden aktiviert, wenn reale historische Verflechtungen sie erfordern.

---

## 3. Research-first statt Architektur-first

Technische Architektur wird aus nachgewiesenen Forschungsbedarfen abgeleitet, nicht umgekehrt.

```text
Zielbild / Forschungsalltag
        ↓
Problem- und Workflow-Map
        ↓
Leane State-of-the-Art-Analyse
        ↓
Capability Map
        ↓
Expertise-/Kompetenzprofile
        ↓
Transdisziplinäres Assistenzkonzept
        ↓
validierte Architekturentscheidungen
        ↓
Requirements / MVP / Implementation
```

### Technische Subsidiarität

Keine Datenbank, Agentenarchitektur, Ontologie, RAG-Schicht, Knowledge Graph, HTR-Pipeline oder eigene Anwendung wird eingeführt, nur weil sie technisch plausibel ist.

Eine technische Komponente muss ein belegtes Forschungs-, Qualitäts-, Auditierbarkeits- oder Wiederholungsproblem lösen.

**Lean gilt für Entwicklung, nicht für Inhaltsarbeit.** Fachliche Komplexität darf nicht reduziert werden, um die Technik einfacher zu machen.

---

## 4. Governing Principles

### 4.1 Wissenschaftliche Standards stehen über Nutzerformulierung und Technik

Jede aktivierte Disziplin arbeitet nach ihren eigenen einschlägigen wissenschaftlichen Standards, Terminologien, Quellenkritiken, Methoden und Evidenzregeln.

Diese Standards dürfen **nicht abgeschwächt** werden durch:

- unscharfe oder unwissenschaftliche Nutzerformulierungen,
- Wunsch nach einer einfachen Geschichte,
- Vermittlungsziele,
- UI- oder Darstellungsanforderungen,
- Datenmodelle,
- Retrieval-/RAG-/Agentenlogik,
- Automatisierungs- oder Implementierungsvereinfachungen.

Technik und Nutzereingabe werden an wissenschaftliche Anforderungen übersetzt; wissenschaftliche Anforderungen werden nicht an Convenience angepasst.

### 4.2 Human-in-the-loop ohne Nutzer-Micromanagement

Human-in-the-loop bedeutet nicht ständige Bestätigung jeder Routinehandlung.

Die Assistenz soll Routine-Methodik, Repository-Mechanik, Recherchevorbereitung, deterministische Ableitungen und Synchronisation soweit möglich selbst übernehmen. Konsequenzielle Arbeit muss aber erklärbar, überprüfbar, anfechtbar, stoppbar und korrigierbar bleiben.

Der Research Owner kontrolliert insbesondere:

- Forschungsinteresse und Prioritäten,
- normative/materiale Systemänderungen,
- Zugang/Rechte, die nur er klären kann,
- folgenschwere Publikations-/Nutzungsentscheidungen,
- echte wissenschaftliche Urteile, die unabhängige menschliche Fachprüfung erfordern.

### 4.3 Progressive Disclosure / maximale menschliche Lesbarkeit

Menschliche Lesbarkeit bedeutet nicht methodische Vereinfachung.

Eine Ausgabe kann verständlich beginnen und bei Bedarf bis zu Fachbegriffen, Methoden, Quelle, Fundstelle, Alternativen und Entscheidungspfad aufgeklappt werden.

Konsequenzielle Schritte sollen sinngemäß rekonstruierbar sein als:

```text
Problem
→ fachliche Anforderung / Evidenz
→ angewandte Kompetenz / Methode
→ Quelle / Fundstelle
→ Befund
→ Interpretation
→ Unsicherheit / Alternative
→ Konsequenz / nächster Schritt
```

### 4.4 Kein Wissensmonopol im Chat oder Modell

Chat ist Werkstatt. GitHub ist dauerhaftes Projektgedächtnis.

Konsequenzielle Zielbilder, Research-Befunde, offene Fragen, Hypothesen, Entscheidungen, verworfene Ansätze und methodische Änderungen müssen aus Repository/Quellen rekonstruierbar sein.

Unverzichtbare Begründungen dürfen nicht nur in Chat-Historie, verborgenem Modellzustand oder Agentenkommunikation existieren.

### 4.5 Methodenkonforme KI ≠ unabhängige Expertenvalidierung

Eine KI kann methodengeleitet arbeiten, Quellen korrekt referenzieren und Fachliteratur einbeziehen. Das ist nicht automatisch gleichbedeutend mit unabhängiger qualifizierter Fachvalidierung.

Stärkere Validierung wird proportional zur Konsequenz einer Aussage erforderlich.

---

## 5. Forschungsebenen strikt trennen

Mindestens folgende Ebenen müssen unterscheidbar bleiben:

```text
Originalquelle / materieller Befund
→ digitale Instanz / OCR / Transkription
→ fachliche Beobachtung / Befund
→ Normalisierung / Identifikation
→ Claim
→ fachliche Interpretation
→ transdisziplinäre Synthese
```

Spätere Ebenen dürfen frühere nicht stillschweigend umschreiben.

Ein Regest ist nicht die Urkunde; OCR ist nicht das Original; eine normalisierte Person ist nicht die gelesene Namensform; eine plausible historische Erklärung ist nicht der Quellenbefund.

---

## 6. Persönlicher Archivar als Spezialkompetenz

Der Archivar / Quellen- und Bestandsspezialist unterstützt insbesondere:

- Literatur, Editionen und Quellen wiederfinden,
- Archive, Bestände und Findmittel erschließen,
- Provenienz und Registraturbildner rekonstruieren,
- Quellenarten und Überlieferungsstufen unterscheiden,
- Scans, Editionen und Regesten erschließen,
- exakte Fundstellen bereitstellen,
- historische Suchbegriffe und Archivsprache nutzen,
- bibliographische Referenzen und ggf. Zotero koppeln.

Er steht **nicht** über den anderen Disziplinen.

---

## 7. Assistenz-Ökosystem und Expertise Routing

### 7.1 Rollenlogik

#### Research Owner

Gibt Erkenntnisinteresse, Prioritäten, Relevanz und Forschungsrichtung vor. Muss nicht Spezialist für Archivistik, Paläographie, Mediävistik, Datenmodellierung oder Software sein.

#### Research Coordinator

Übersetzt Fragen, zerlegt Probleme, aktiviert relevante Kompetenzen und integriert Ergebnisse. Er ist Orchestrator, **keine epistemische Oberinstanz**.

#### Spezialkompetenzen / Fachassistenten

Problemabhängig werden z. B. aktiviert:

- Archivistik / Diplomatik / Quellenkunde
- Paläographie / HTR
- Editionswissenschaft / historische Philologie
- Mediävistik / Landes- und Herrschaftsgeschichte
- Frühneuzeitforschung
- Sozial-, Wirtschafts- und Agrargeschichte
- Adels-, Hof- und Diplomatiegeschichte
- Reichs- und Territorialgeschichte
- Archäologie / Siedlungs-/Landschaftsarchäologie
- historische Geographie / Kulturlandschaft
- Umweltgeschichte / Geoarchäologie / Hydrologie
- Volkskunde / Europäische Ethnologie / historische Anthropologie
- Onomastik / Toponymie
- Prosopographie / historische Netzwerkforschung
- Bibliographie / Information Retrieval
- Forschungsdaten / Provenienz
- technische Spezialkompetenzen wie OCR, IR, GIS, Automation, NLP

Ob daraus technisch mehrere Agents, ein Modell mit Kompetenzprofilen, Fachretrieval, Tools, Services oder eine andere Architektur werden, bleibt offen.

**Fachliche Modularität ist Requirement; Multi-Agent-Technik ist nur eine Hypothese.**

### 7.2 Fachliche Problemübersetzung

Eine Kernfähigkeit lautet:

```text
Laienbeobachtung / unscharfe Frage
→ mögliche fachliche Problembegriffe
→ konkurrierende Begriffsmodelle
→ historische / regionale Terminologie
→ moderne analytische Begriffe
→ Quellengattungen / Archivsprache
→ einschlägige Methoden
→ relevante Disziplinen
→ Fallstricke
→ Rechercheansätze
```

Die Rückübersetzung für den Nutzer vereinfacht die Sprache, **nicht die Wissenschaft**.

---

## 8. Expertise Profiles: was echte Fachkompetenz ausmacht

Eine Fachrolle ist kein Rollenprompt wie „Du bist Mediävist“.

Zieldefinition:

```text
Expertise
= Fachgebiet
× Epoche
× Region
× Fachsprache
× Begriffs-/Gegenstandsmodelle
× Quellentyp / Überlieferungslogik
× Methodik
× Forschungsstand
× Qualitätsregeln
× transdisziplinäre Schnittstellen
```

Für jede priorisierte Kompetenz muss #10 mindestens untersuchen:

1. Problemklassen / Geltungsbereich
2. Fachsprache und zentrale Begriffe
3. historische, regionale und archivische Terminologie
4. Begriffs- und Gegenstandsmodelle
5. typische Primärquellen und Überlieferung
6. Methoden / Playbooks
7. zulässige Schlussarten
8. fachliche Qualitäts-/Falsifikationskriterien
9. typische Fehlschlüsse
10. aktuelle Forschung und wichtige Kontroversen
11. relevante Handbücher, Lexika, Bibliographien, Journals
12. Editionen, Regesten, Datenbanken und Forschungsinfrastrukturen
13. regionale Archive / Bestände / Findmittel
14. historische Suchterminologie / Schreibvarianten / lateinische Begriffe
15. transdisziplinäre Schnittstellen
16. Grenzen von AI/Automation
17. Trigger für unabhängige Spezialistenvalidierung

### Beispiele für sprachliche Präzision

- `Ministeriale` ist nicht synonym mit „Adliger“ oder „Beamter“.
- `Regest` ist eine editorische/erschließende Repräsentation, nicht die Quelle selbst.
- `Vogtei`, `Lehnswesen`, `Grundherrschaft`, `Patronat`, `Amt` und `Herrschaft` dürfen nicht ineinander geschoben werden.
- Begriffe wie `Ostsiedlung`, `Landesausbau` oder `Territorialisierung` benötigen Historiographie- und Begriffskritik.

Das System soll ein **fachliches Begriffsnetz** statt bloßer Synonymlisten unterstützen: Ober-/Unterbegriffe, historische ↔ analytische Begriffe, regionale/zeitliche Gültigkeit, konkurrierende Modelle, Archivterminologie und überholte Forschungsbegriffe.

---

## 9. Regionalisierte Spitzenexpertise

Regionaler Fokus ist mehr als ein Filter.

Eine belastbare Fachrolle soll wissen:

- wie sich Territorien, Herrschaften und Verwaltungsräume historisch verändern,
- welche regionalen Forschungs- und Landesgeschichtstraditionen existieren,
- welche Archive, Bestände, Serien und Findmittel einschlägig sind,
- welche Editions- und Regestenwerke vorhanden sind,
- welche regionalen Zeitschriften/Jahrbücher/Bibliographien relevant sind,
- welche Quellengattungen regional typischerweise überliefert oder verloren sind,
- welche historischen Suchbegriffe und Schreibweisen in der Region vorkommen,
- welche Nachbar- oder Vergleichsräume methodisch sinnvoll sind,
- wann ein regionaler Befund nur durch reichsweite oder europäische Verflechtung erklärbar wird.

„Absolute Expertise“ ist ein Zielniveau, keine Behauptung von KI-Unfehlbarkeit. Sie muss durch qualifiziertes Retrieval, aktuelle Forschung, kontrollierte Referenzen, methodische Regeln und ggf. echte externe Fachprüfung abgesichert werden.

---

## 10. Historische Akteure: Erklärung statt bloßer Netzwerkknoten

Ein zukünftiges Akteursmodell darf Personen nicht nur als Knoten und Beziehungen speichern.

Zunächst zu untersuchende historische Erklärungscapability:

```text
Akteur in konkreter historischer Situation
→ soziale / institutionelle Position
→ belegte Beziehungen und Abhängigkeiten
→ Ressourcen
→ Informationshorizont
→ zeitgenössisch mögliche Handlungsoptionen
→ Zwänge / Risiken / Anreize
→ beobachtete Handlung
→ mögliche Motive / Erklärungen
→ alternative Erklärungen
→ Quellenbasis / Aussagegrenzen
```

Wichtige Schutzregel: keine nachträglich elegante „innere Logik“ erfinden.

Motive, Interessen, Wissen oder Loyalitäten sind nur soweit formulierbar, wie Quellen und fachliche Methode sie tragen. Dieselbe Handlung kann aus adelsgeschichtlicher, sozialhistorischer, reichspolitischer, konfessioneller, wirtschaftlicher oder diplomatiegeschichtlicher Perspektive unterschiedlich erklärt werden.

Diese Perspektiven bleiben zunächst sichtbar getrennt, bevor eine begründete Synthese erfolgt.

---

## 11. Discrepancy Reasoning

Unterschiedliche Quellen/Befunde werden nicht vorschnell als einfacher Konflikt behandelt.

```text
zwei Aussagen unterscheiden sich
→ echter Widerspruch?
→ anderer Zeitstand?
→ andere Quellengattung / Überlieferungsstufe?
→ anderer institutioneller Blickwinkel / Zweck?
→ andere Begrifflichkeit?
→ abhängige Quellen?
→ anderer räumlicher Maßstab?
→ unterschiedliche Interessen der Akteure?
→ historiographische Differenz?
→ erst danach bewerten
```

Ein Widerspruch kann real bleiben. Ziel ist keine Harmonisierung, sondern methodisch saubere Diagnose der Differenz.

---

## 12. Quellen, OCR, Retrieval und persönliches Forschungsarchiv

### 12.1 Grundpipeline

```text
Quelle finden
→ übernehmen / referenzieren
→ Original erhalten
→ Volltext/OCR/HTR erzeugen
→ bibliographisch/provenienzseitig erfassen
→ durchsuchen
→ lesen / annotieren
→ zitieren
→ analysieren / synthetisieren
```

### 12.2 OCR / HTR

Mindestanforderungen:

- Originalbild/-datei unverändert halten
- OCR/HTR als Derivat kennzeichnen
- Roh-OCR von korrigierter/normalisierter Transkription unterscheiden
- Seiten-/Blatt-/Regeststruktur erhalten
- historische Orthographie nicht still normalisieren
- Personen-/Orts-/Flurnamen besonders evaluieren
- jede Textstelle zur Quelle/Fundstelle zurückführen

Formate/Tools wie ALTO, hOCR, PAGE XML, OCRmyPDF, Kraken, OCR4all oder Transkribus sind Prüfgegenstände, keine Vorentscheidung.

### 12.3 Retrieval

Benötigt werden:

- exakte lexikalische Suche
- Kontexttreffer
- historische Schreib- und Namenvarianten
- kontrollierte Query Expansion
- Filter nach Werk, Zeitraum, Quellentyp, Sammlung, Tags
- exakte Fundstellen
- transparente Suchstrategie

Semantische Suche, Embeddings, RAG oder Knowledge Graph bleiben Hypothesen.

### 12.4 Zotero

Zotero als zentrale bibliographische Kopplung ist eine starke Hypothese, keine Entscheidung. Zu prüfen sind Desktop/Web API, Fulltext-Zugriff, Collections/Tags, Attachment-Referenzen, Pyzotero, Better BibTeX und Eignung für archivalische/nichtklassische Quellen.

---

## 13. Wissenschaftlicher Forschungszustand vs. Vermittlung

Histo-Orla endet beim belastbaren, menschenlesbar erklärbaren **Forschungszustand**.

```text
Quelle
→ Befund
→ Evidenzstatus
→ Claim
→ Relation
→ fachliche Interpretation
→ Kontroverse / Alternative
→ Unsicherheit / Aussagegrenze
→ transdisziplinär integrierter Forschungszustand
```

Vermittlung ist nachgelagert:

```text
Forschungszustand
→ Kontext
→ Adressat
→ Zweck
→ Medium
→ Auswahl
→ Sprache / Tiefe
→ Dramaturgie / Darstellung
```

Eine Vermittlungsaussage darf den Forschungszustand **nicht rückwirkend verändern**.

Die Vermittlung kann an ein nachgelagertes System wie `rgk-main-ssot` übergeben werden. Eine technische Schnittstelle ist noch nicht festgelegt. Später ist ein schlanker, menschenlesbarer Übergabevertrag zu untersuchen, der Aussage, Quellen/Fundstellen, Status, Aussagegrenzen, Kontroversen und Rückverfolgbarkeit bewahrt.

Histo-Orla muss keine Besucherdramaturgie, Social-Media-Sprache oder Ausstellungserzählung optimieren.

---

## 14. Internes Prior Art

### 14.1 `paleo-type`

`paleo-type` ist internes Referenzmodell für Forschungsgovernance und methodische Strenge.

Übertragbare Prinzipien:

- Forschungsergebnis vor Systementwicklung
- Governing Objective / klare Präzedenz
- technische Subsidiarität
- kein Wissensmonopol im Chat
- one fact, one canonical owner
- Original / Derivat / Interpretation trennen
- persistenter Identifier ≠ exakt inspizierte Datei
- Research Question → Evidence → Method → Claim
- Kompetenzen problemabhängig aktivieren
- Aktivität ≠ wissenschaftlicher Reifegrad
- AI-Provenienz nur bei konsequenzieller Nutzung
- Validierung proportional zur Konsequenz
- AI-as-method → Evaluation verpflichtend
- operational ownership + explainability + challengeability
- progressive disclosure
- methodenkonforme AI ≠ independent expert validation
- materielle Systemänderungen: Analyse → Requirements → Konzept → Owner-Zulassung → Umsetzung → Tests/Loss Checks → Result Review

Nicht automatisch übertragen werden konkrete Schemas, Projektgrenzen, G1–G6-Gates oder paläographiespezifische Strukturen.

### 14.2 `rgk-main-ssot`

RGK ist internes Prior Art für relationale Forschungslogik und die Forschung↔Vermittlung-Grenze.

Belegt sind u. a.:

- Darstellung folgt Modell, nicht umgekehrt
- neutrale Identitäten
- Claim → Evidence → Interpretation
- projektbezogene Quellenfunktionen
- Abweichungen als Erkenntnisobjekte
- mehrere Sichten auf denselben Wissenszustand
- Provenienz vor Wirkung
- Lean Development ≠ Inhaltsreduktion

Reichere alte Working Notes (`relationales_befund_vermittlungsmodell...`, `durchlauf_logik...` u. a.) sind im historischen Handoff-Manifest dokumentiert, im aktuellen `main` aber nicht unmittelbar vorhanden. Inhalte daraus gelten bis zur Rekonstruktion/Lektüre nicht als gesichertes Prior Art.

Transferklassifikation: `inherit | adapt | research | reject`.

Siehe #21.

---

## 15. State-of-the-Art-Programm (#10)

Die Recherche muss zwei große Ebenen gleichberechtigt abdecken.

### A. Forschungsinfrastruktur / technische und methodische Unterstützung

- Archiv-/Informationswissenschaft
- Zotero / Literaturmanagement / PKM/RKM
- Digital Humanities
- OCR / HTR
- Korpuslinguistik / Information Retrieval
- historische NER / NLP
- Knowledge Organization / Ontologien / Knowledge Graphs
- RAG / Hybrid Retrieval / AI-Assistance
- Forschungsdaten / Provenienz / FAIR / Reproduzierbarkeit
- Review-/Evidence-Synthesis-Methoden
- Research Software Engineering / Automation
- Evaluation / Human-in-the-loop

### B. Fachwissenschaftliche Forschungstraditionen und Expertise

- historische Quellenkritik / Historiographie
- Landes-/Regionalgeschichte
- Mittelalterforschung
- Archäologie / Siedlungs-/Landschaftsarchäologie
- historische Geographie / Kulturlandschaft
- Umweltgeschichte / Geoarchäologie
- Volkskunde / Europäische Ethnologie
- Sozial-, Wirtschafts-, Agrargeschichte
- Adel / Herrschaft / Hof
- Recht / Verwaltung
- Dreißigjähriger Krieg / Militärgeschichte
- Reichs-/Territorialgeschichte
- Onomastik / Kartographie / Baugeschichte / Demographie nach Bedarf
- Connected / Entangled / Transregional History
- historische Netzwerkforschung / Prosopographie
- Diplomatie / New Diplomatic History
- Mobilitäts-/Reisegeschichte
- Universitäts-/Bildungsgeschichte
- Konfessions-, Ordens- und Kreuzzugsgeschichte bei Bedarf
- Spatial History / Spatial Humanities

### C. Regionale Expertiseebene

Je Kernfach zusätzlich:

- regionaler Forschungsstand
- relevante Autoren/Forschungstraditionen
- Zeitschriften/Jahrbücher/Reihen/Bibliographien
- Archive und Bestandsgruppen
- Findmittel/Portale
- Editionen/Regesten/Urkundenbücher
- historische/archivische Terminologie
- Quellenverluste und Überlieferungslücken
- Territorial-/Verwaltungschronologie
- sinnvolle Vergleichsräume
- aktuelle regionale Kontroversen

### D. Bewertungskriterien

Jeder Ansatz wird u. a. geprüft auf:

- Forschungsproblem / Kompetenzgewinn
- wissenschaftliche Herkunft / Community
- Reife und Pflege
- Offenheit / Automatisierbarkeit
- Daten-/Provenienzmodell
- Lock-in
- Eignung für heterogene historische Quellen
- Qualitätsmetriken
- Human Auditability
- Fachstandard-Konformität
- Wiederverwendbarkeit
- tatsächliche Lücke für Histo-Orla

---

## 16. Evaluation

### OCR/HTR

- CER / WER
- Fehler bei Namen, Zahlen, historischen Begriffen
- Erhalt physischer/logischer Struktur

### Retrieval

- Recall / Precision
- transparente Query Expansion
- historische Varianten
- Test-/Goldfälle

### Provenienz / Fundstellen

- korrekte Quelle / Edition
- korrekte Seite / Folio / Regest
- keine erfundenen Belege
- Inspektionsstatus klar

### Expertise Routing

- relevante Disziplinen identifiziert?
- passende Fachbegriffe/Modelle aktiviert?
- Quellen- und Methodenlogik korrekt?
- regionale und zeitliche Grenzen erkannt?
- Nachbardisziplinen rechtzeitig aktiviert?

### Expertentiefe

- reale Fachmethoden statt allgemeiner Themenkenntnis
- aktuelle Forschung / Kontroversen
- regionale Archive/Bestände/Literatur
- Fachvokabular korrekt historisiert

### Epistemische Kalibrierung

Unterscheidbar bleiben:

- direkt beobachteter Quellenbefund
- quellenkritisch gut gestützte Rekonstruktion
- verbreitete Forschungsinterpretation
- konkurrierende Forschungsposition
- plausible indirekte Hypothese
- offene Forschungsfrage
- echte Evidenzlücke

### Akteurs-/Netzwerkanalyse

- Beziehung wirklich belegt oder nur Ko-Präsenz?
- Wissensstand/Handlungsoptionen zeitgenössisch plausibel und belegt?
- alternative Erklärungen sichtbar?
- keine Motivpsychologie ohne Evidenz?

### Automation / AI

- Reproduzierbarkeit / Idempotenz
- Failure Modes
- AI-Provenienz bei konsequenzieller Nutzung
- Evaluation bei systematischer Corpus-Level-Automation
- keine Scheinautorität durch Modellkonsens

---

## 17. Aktuelle Hypothesen und Nicht-Entscheidungen

### Validierte Ziele

- wissenschaftlich belastbarer persönlicher Forschungszustand
- fachwissenschaftliche Übersetzung für einen Laien-Research-Owner
- transdisziplinäre Expertise Routing
- regionale Spitzenexpertise mit europäischem Horizont
- Human-in-the-loop / maximale Auditierbarkeit
- kein Wissensmonopol im Chat
- Automatisierbarkeit und möglichst geringe Provider-Abhängigkeit
- Trennung Forschung ↔ Vermittlung

### Starke, aber zu prüfende Hypothesen

- Zotero als zentrale bibliographische Kopplung
- script-/local-first / AI-optional
- lokale Such-/Volltextschicht
- kontrollierte Fachvokabulare / Begriffsnetze
- modulare Fachprofile / Retrieval-Kontexte / Tools

### Offen

- konkrete OCR-/HTR-Engine
- Volltextformate
- Datenbank / SQLite / FTS
- RAG / Embeddings / Hybrid Search
- Knowledge Graph / Ontologie
- konkretes Claim-/Evidence-Datenmodell
- konkrete Akteurs-/Event-/Relationsrepräsentation
- echte Multi-Agent-Architektur
- technische Schnittstelle zu RGK/Vermittlung

### Zurückgestuft / superseded

- persönlicher Archivar als gesamte Oberinstanz
- Claim–Evidence Graph zuerst bauen
- YAML-Schemas als erster MVP
- feste Methodenkette Scoping → Meta-Narrative → CIS → Realist → Claim Graph
- Zotero bereits entschieden als Source of Truth
- SQLite/FTS bereits gesetzte Architektur
- Multi-Agent aus Fachrollen ableiten
- Vermittlungsanforderungen in den wissenschaftlichen Kernzustand schreiben

---

## 18. Nächste Arbeit

Noch keine breite Implementation.

1. Zielbild/Pain Points weiter vervollständigen.
2. internes Prior Art `paleo-type` und RGK systematisch extrahieren, aber nicht ungeprüft kopieren.
3. leane, web-basierte State-of-the-Art-Analyse #10 durchführen.
4. Expertise Profiles je priorisierter Fachkompetenz erstellen.
5. Capability Map daraus ableiten/validieren.
6. Human-readable wissenschaftliche Views und fachliche Übersetzung spezifizieren.
7. Akteurs-/Discrepancy-/Multi-Scale-Capabilities gegen Fachmethoden prüfen.
8. Hypothesen accepted/rejected/superseded klassifizieren.
9. erst danach Daten-/Systemarchitektur und MVP bestimmen.

---

## 19. Issue-Landkarte

- #1 – zentraler Research-Design-/Arbeitsstand
- #2 – persönlicher Archivar; inzwischen Spezialrolle statt Gesamtziel
- #3 – Zotero-Hypothese
- #4 – OCR-/Volltexterschließung
- #5 – Retrieval / historische Query Expansion / Fundstellen
- #6 – Git-/Provenienzprinzip
- #7 – langfristige transdisziplinäre Forschungsassistenz
- #8 – Automatisierung / KI-Unabhängigkeit
- #9 – Governance: HITL, Auditierbarkeit, Projektgedächtnis
- #10 – State-of-the-Art → Capabilities → Expertise Profiles → Konzept
- #11 – Concept Audit / Korrekturen
- #12 – internes Prior Art `paleo-type`
- #13 – Geschichte als Querschnitt / Expertise Routing
- #14 – regional verankert, europäisch verflochten
- #15 – Expertenmodell: Tiefe, Kontroversen, Unsicherheit
- #16 – regionalisierte Spitzenexpertise
- #19 – Assistenz-Ökosystem: Fachsprache, Modelle, Methoden
- #20 – Boundary Forschung ↔ Vermittlung / Übergabe an RGK
- #21 – internes Prior Art `rgk-main-ssot`

---

## 20. Leitformeln

> **Der persönliche Archivar ist ein Spezialist im Forschungsteam – nicht das Forschungsteam selbst.**

> **Nicht eine Antwort mit Experten-Ton, sondern fachlich begründete Perspektiven mit sichtbarer Evidenz, Kontroverse und Unsicherheit.**

> **Nicht nur wissen, welches Fach zuständig ist – sondern auf Fachniveau wissen, was die Region dazu hergibt, wo man sucht, wie man prüft und welche anderen Disziplinen widersprechen oder ergänzen müssen.**

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Forschung erzeugt den belastbaren Zustand. Vermittlung erzeugt adressatenspezifische Sichten darauf.**

> **Technik dient der Forschung; sie definiert ihre wissenschaftlichen Standards nicht.**

> **Kein Wissensmonopol im Chat.**
