# Persönlicher Archivar und transdisziplinäre Forschungsassistenz

**Status:** aktueller Konzept- und Arbeitsstand, noch keine finale Architektur

**Letzte grundlegende Überarbeitung:** 2026-08-30

**Zentrale Issues:** #1, #2, #9, #10

---

## 1. Zweck dieses Dokuments

Dieses Dokument konsolidiert den aktuellen Denkstand für eine Forschungsumgebung im Projekt *Pflege Arnshaugk*.

Das Zielbild hat sich gegenüber dem ersten Entwurf präzisiert: Gesucht wird nicht primär ein „KI-Literaturassistent“ oder ein großer Knowledge Graph, sondern zunächst ein **persönlicher Archivar für den realen historischen Forschungsalltag**. Auf einer belastbar erschlossenen Literatur- und Quellenbasis soll später eine methodisch anspruchsvolle, transdisziplinäre Forschungsassistenz aufbauen können.

Wichtig ist die Trennung zwischen:

- **Nutzerzielen und tatsächlichen Forschungsbedarfen**,
- **wissenschaftlichen Qualitätsanforderungen**,
- **Capabilities**, die ein späteres System braucht,
- **Hypothesen über mögliche technische Lösungen**,
- **validierten Entscheidungen und Requirements**.

Frühere Fassungen dieses Dokuments haben plausible Lösungsansätze teilweise zu früh als Architektur oder MVP formuliert. Diese Überarbeitung korrigiert das.

---

## 2. Aktuelles Zielbild

### 2.1 Persönlicher Archivar

Der persönliche Archivar soll grundlegende Literatur- und Quellenarbeit deutlich erleichtern.

Er soll insbesondere helfen:

- Literatur, Editionen und Quellen wiederzufinden,
- bildbasierte Editionen, Regesten und Scans per OCR oder vorhandenem Volltext zu erschließen,
- relevante Volltextauszüge schnell zu finden,
- konkrete Fundstellen mit Seite, Blatt oder Regestnummer auszugeben,
- bibliographische Verwaltung mit Zotero zu koppeln,
- historische Namen, Schreibweisen, Synonyme und Fachbegriffe zu berücksichtigen,
- wiederkehrende Schritte perspektivisch zu automatisieren,
- zentrale Funktionen möglichst unabhängig von einem einzelnen KI-Anbieter verfügbar zu halten.

Der Archivar soll ausdrücklich **keine bloße „Chat mit PDFs“-Oberfläche** sein. Ein Quellenbefund muss auf überprüfbare Literatur/Quelle und konkrete Fundstelle zurückführbar bleiben.

### 2.2 Langfristige transdisziplinäre Forschungsassistenz

Auf dem erschlossenen Bestand soll perspektivisch eine wissenschaftliche Assistenzschicht aufbauen, die bei komplexen Forschungsfragen unterstützt:

- Forschungsfragen strukturieren,
- Forschungstraditionen und disziplinäre Perspektiven unterscheiden,
- historische und fachsprachliche Terminologien aufeinander beziehen,
- Claims und Evidenzbezüge sichtbar machen,
- Widersprüche und Kontestationen analysieren,
- räumliche und zeitliche Gültigkeit von Aussagen differenzieren,
- Suchlücken von Evidenzlücken unterscheiden,
- nachvollziehbare Synthesen unterstützen.

Diese Funktionen sind **strategisches Ziel**, aber Methodik, Datenmodell und technische Form sind noch zu untersuchen.

---

## 3. Methodisches Vorgehen der Konzeptentwicklung

Die zentrale Korrektur des bisherigen Arbeitsstands lautet:

> Nicht von einer früh erfundenen Architektur rückwärts auf den Forschungsprozess schließen, sondern vom realen Zielbild und Problemraum vorwärts zu Capabilities, Rollen und erst danach zu Architektur und Implementation arbeiten.

Vorgehensmodell:

```text
Zielbild / Forschungsalltag
        ↓
Problem- und Workflow-Map
        ↓
Leane State-of-the-Art-Analyse
        ↓
Capability Map
        ↓
Rollen- / Kompetenzmodell
        ↓
Transdisziplinäres Gesamtkonzept
        ↓
validierte Architekturentscheidungen
        ↓
Requirements / MVP / Implementation
```

Details siehe Issue #10.

### Warum „leaner State of the Art“?

Ziel ist kein enzyklopädischer Marktüberblick. Für jede Problemklasse sollen die stärksten, relevantesten und wiederverwendbaren Ansätze identifiziert werden:

1. Welches Problem lösen sie?
2. Aus welcher wissenschaftlichen oder technischen Tradition stammen sie?
3. Wie reif sind sie?
4. Sind sie offen, automatisierbar und integrierbar?
5. Welche Provenienz- und Datenmodelle nutzen sie?
6. Welche Lock-ins erzeugen sie?
7. Wie gut passen sie zu heterogenen historischen Quellen?
8. Wie werden Qualität und Fehler gemessen?
9. Was kann übernommen werden, statt neu gebaut zu werden?
10. Welche Lücke bleibt für das eigene Konzept?

---

## 4. Wissensgovernance

**Chat ist Werkstatt; GitHub ist Projektgedächtnis.**

Wichtige Erkenntnisse sollen nicht ausschließlich in einem Chatverlauf verbleiben. Zielbilder, offene Fragen, Hypothesen, Research-Befunde, Entscheidungen und verworfene Ansätze werden in Issues oder versionierten Dokumenten festgehalten.

Siehe Issue #9.

### Issue-/Artefakttypen

- Zielbild
- Problem / Pain Point
- Research Question
- Hypothese / Lösungsansatz
- State of the Art
- Capability
- Role / Competency
- Decision / ADR
- Requirement
- Implementation

Wichtig ist, dass diese Typen nicht miteinander verwechselt werden. Ein Brainstorming-Vorschlag ist noch keine Anforderung; eine plausible Architektur ist noch keine Entscheidung.

---

## 5. Belastbare Nutzerbedarfe

### 5.1 OCR und Volltexterschließung

Benötigt wird eine robuste Erschließung von:

- born-digital Texten,
- PDFs mit vorhandenem Textlayer,
- Bild-PDFs,
- Scans und Seitenbildern,
- Editionen und Regesten,
- perspektivisch ggf. Handschriften/HTR.

Wissenschaftliche Mindestanforderungen:

- Seiten-/Blatt-/Regestbezug bleibt erhalten,
- OCR wird als OCR gekennzeichnet,
- Roh-OCR, Korrektur und Transkription bleiben unterscheidbar,
- historische Orthographie wird nicht still normalisiert,
- Fehler bei Orts-/Personennamen sind besonders zu berücksichtigen,
- jede relevante Textstelle ist zur Fundstelle rückführbar.

### 5.2 Volltextsuche und Quellenexperte

Benötigt werden:

- exakte Suche,
- Kontexttreffer,
- historische Schreibvarianten,
- Namenvarianten,
- kontrollierte Synonym-/Begriffsexpansion,
- Filter auf bibliographische und inhaltliche Kontexte,
- fundstellengenaue Ausgabe.

Semantische Suche, Embeddings oder RAG sind mögliche Ergänzungen, aber derzeit **keine festgelegten Anforderungen**.

### 5.3 Zotero-Kopplung

Der Nutzer möchte die fachliche Literatur-/Quellenkopplung eher über Zotero als direkt über den physischen Dateispeicher führen.

Daraus entsteht die starke Hypothese, Zotero als zentrale bibliographische Referenzschicht zu nutzen. Zu prüfen sind u. a.:

- Item-/Attachment-Referenzen,
- lokale/Web-APIs,
- Collections und Tags,
- Volltextzugriff,
- Better-BibTeX-/Plugin-Ökosystem,
- Umgang mit nicht-klassischen Quellen und archivalischen Einheiten.

„Zotero ist Source of Truth“ ist aktuell **Hypothese**, keine abgeschlossene Architekturentscheidung.

### 5.4 Automatisierung und KI-Unabhängigkeit

Belastbare Zielvorgaben sind:

- wiederkehrende Schritte automatisieren,
- Kernfunktionen perspektivisch auch per Skript ausführen,
- keine Abhängigkeit von einem einzelnen KI-/Cloud-Anbieter,
- KI nur dort einsetzen, wo sie zusätzlichen Nutzen bringt.

Daraus folgt die zu prüfende Architekturhypothese „script-first / local-first / AI-optional“.

Konkrete Vorschläge wie Python CLI, SQLite, FTS5, `.local/`, Embeddings oder Befehle wie `archivar sync` bleiben bis zur State-of-the-Art-Prüfung technische Kandidaten.

---

## 6. Wissenschaftliche Leitplanken

Unabhängig von der späteren Architektur gelten bereits einige wichtige Forschungsprinzipien.

### Quellenbefund vor Interpretation

Eine generierte Zusammenfassung darf nicht wie ein Quellenbefund erscheinen. Fundstelle, Textbefund und Interpretation müssen unterscheidbar bleiben.

### OCR ersetzt niemals die Quelle

OCR ist eine Erschließungsschicht und kann fehlerhaft sein. Besonders historische Eigennamen, Flurnamen, Rechtsbegriffe und seltene Schreibweisen sind kritisch.

### Provenienz

Relevante Befunde sollen möglichst zurückführbar sein auf:

- Werk / Quelle,
- konkrete Fundstelle,
- Herkunft des Textes,
- ggf. Verarbeitungsschritte,
- Korrekturen und Unsicherheit.

### Keine naive universelle Evidenzhierarchie

Historische Quellen, Karten, archäologische Befunde, naturwissenschaftliche Messungen und moderne Fachliteratur haben unterschiedliche Qualitätskriterien. Eine transdisziplinäre Assistenz darf sie nicht unreflektiert in ein einziges Ranking pressen.

### Kontestation statt vorschneller Auflösung

Widersprüche können aus unterschiedlichen Definitionen, Zeiten, Räumen, Skalen, Methoden oder tatsächlichen empirischen Konflikten entstehen. Das System soll diese Unterschiede sichtbar machen.

### Human-in-the-loop

Bei wissenschaftlich relevanten Transformationen und Interpretationen bleibt menschliche Kontrolle zentral.

---

## 7. Zu untersuchende State-of-the-Art-Felder

Die geplante Analyse soll mindestens folgende Bereiche abdecken:

### Literatur- und Wissensmanagement

- Zotero und Plugin-Ökosystem
- Personal Knowledge Management
- Research Knowledge Management
- bibliographische Standards und Citation Workflows

### Digitale Quellenerschließung

- Digital Humanities
- OCR historischer Drucke
- Fraktur-OCR
- HTR / Handschriftenerkennung
- Layout-/Seitenformate wie ALTO, hOCR, PAGE XML
- Korpusaufbereitung

### Information Retrieval

- Volltextsuche
- Fuzzy Search
- linguistische Suche
- historische Query Expansion
- Named Entity Recognition für historische Daten
- Hybrid Search
- semantische Suche / RAG

### Forschungsdaten und Provenienz

- Forschungsdatenmanagement
- FAIR-Prinzipien
- Provenienzmodelle
- Versionierung
- Reproduzierbarkeit
- Data Lineage

### Wissenschaftliche Synthese

Als methodische Kandidaten, nicht als festgelegte Kette:

- Scoping Review
- Meta-Narrative Review
- Critical Interpretive Synthesis
- Realist Review / Reasoning
- Claim–Evidence Mapping
- bibliometrische Exploration
- Citation Chaining
- Knowledge Organization / Ontologien / Knowledge Graphs

### Automatisierung

- lokale Research Toolchains
- CLI-/Pipeline-Design
- Workflow-Orchestrierung
- idempotente Datenverarbeitung
- KI-Provider-Abstraktion
- Offline-/Local-AI-Optionen

---

## 8. Vorläufige Capability Map

Diese Liste ist ein **Arbeitsentwurf**, der aus #10 validiert und vervollständigt werden muss.

### Acquisition / Referencing

- Literatur und Quellen identifizieren
- bibliographisch eindeutig referenzieren
- vorhandene Bestände/Collections nutzen

### Textualization

- Volltext erkennen
- OCR/HTR auslösen oder integrieren
- Seiten-/Regeststruktur bewahren
- Korrekturen nachvollziehbar halten

### Retrieval

- exakte Suche
- Varianten-/Fuzzy-Suche
- historische Begriffsexpansion
- Filter und Kontext
- ggf. semantische/hybride Suche

### Provenance

- Quelle und Fundstelle verbinden
- Transformationen kennzeichnen
- Forschungsentscheidungen dokumentieren

### Research Assistance

- Fragen strukturieren
- Suchstrategien entwickeln
- Forschungstraditionen unterscheiden
- Evidenz und Widersprüche analysieren
- Synthesen unterstützen

### Automation

- wiederholbare Verarbeitung
- Änderungs-/Sync-Erkennung
- reproduzierbare Such-/Processing-Runs
- KI optionierbar halten

---

## 9. Vorläufige Rollen- und Kompetenzkandidaten

Rollen werden erst nach der Capability-/State-of-the-Art-Analyse belastbar definiert. Derzeit relevant erscheinen:

- **Historiker / Domänenforscher:** Fragestellung, Quellenkritik, Kontext, fachliche Validierung
- **Archivar / Informationswissenschaft:** Erschließung, Provenienz, Findmittel, Quellengattungen
- **Bibliotheks-/Literaturmanagement-Kompetenz:** Zotero, Metadaten, Identifier, Zitationsworkflows
- **Digital Humanities:** digitale Editionen, Korpora, Text-/Quellenmodelle
- **OCR/HTR-Kompetenz:** historische Drucke, Fraktur, Handschriften, Qualitätsmessung
- **Information Retrieval / NLP:** Suche, Query Expansion, Entity Recognition, Ranking
- **Knowledge Organization / Ontologie:** Begriffsmodelle, kontrollierte Vokabulare, semantische Beziehungen
- **Research Methods / Evidence Synthesis:** Reviewmethoden, transdisziplinäre Synthese, Kontestationen
- **Forschungsdatenmanagement:** FAIR, Provenienz, Reproduzierbarkeit, Lizenzierung
- **Software Engineering:** Automatisierung, APIs, CLI, Integration, Tests
- **Data/Search Engineering:** Indexierung, lokale Datenhaltung, Performance
- **AI/LLM Engineering:** optionale KI-Funktionen, Provider-Abstraktion, Evaluation
- **Urheberrecht/Datenschutz:** öffentliche vs. private Volltexte, Lizenzen
- **UX für Forschung:** Interaktion mit Fundstellen, Suche und wissenschaftlicher Kontrolle

Diese Rollen können später als menschliche Verantwortungsbereiche, technische Module oder ggf. spezialisierte Agenten umgesetzt werden. Diese Ebenen sollen nicht vorschnell vermischt werden.

---

## 10. Historischer Anwendungskontext Pflege Arnshaugk

Das Konzept muss nicht nur moderne Fachliteratur, sondern heterogene historische Quellengruppen berücksichtigen.

Relevante Kandidaten sind beispielsweise:

- Forst-, Flur-, Hutungs- und Grenzrisse,
- Jagd- und Forstkarten,
- Guts- und Rittergutsvermessungen,
- Teich- und Wasserrechtsakten,
- Grenzstreitigkeiten,
- Hutungs- und Triftstreitigkeiten,
- Gemeinheitsteilungen und Separation,
- Kataster- und Flurbücher,
- Lehnsakten und Besitzregister,
- Amtsrechnungen,
- Fischerei- und Teichrechnungen,
- Mühlen- und Wasserbauakten,
- Orts- und Landesbeschreibungen,
- ältere topographische Karten und Meilenblätter,
- historische Luftbilder,
- Geländemodelle/LiDAR als moderne Vergleichsebene.

Diese Vielfalt ist ein Grund, warum Informationswissenschaft, historische Quellenkritik, Digital Humanities, Retrieval und transdisziplinäre Synthesemethoden gemeinsam betrachtet werden müssen.

---

## 11. Evaluation als notwendige Kompetenz

Ein späteres System darf nicht nur „interessant wirken“. Jede Capability braucht passende Qualitätskriterien.

Beispiele:

### OCR

- Character/Word Error Rate
- Fehler bei Namen und historischen Termini
- Erhalt von Seiten-/Regeststruktur

### Retrieval

- Recall
- Precision
- bekannte Testfälle / Goldstandard-Suchen
- Transparenz der Query Expansion

### Fundstellen

- korrekte Referenz auf Werk/Quelle
- korrekte Seite/Regest
- keine erfundenen Belege

### Automatisierung

- Idempotenz
- Reproduzierbarkeit
- Fehlertoleranz
- nachvollziehbare Processing Runs

### Wissenschaftliche Assistenz

- Trennung von Befund und Interpretation
- Provenienz
- Unsicherheitsdarstellung
- fachliche Validität
- tatsächliche Zeitersparnis ohne Qualitätsverlust

---

## 12. Aktuelle Hypothesenliste

### Stark, aber noch zu prüfen

- Zotero als zentrale bibliographische Kopplung
- script-first / local-first / AI-optional
- lokale Volltext-/Suchschicht zusätzlich zu Zotero
- Trennung kuratierter Forschungsdaten von regenerierbaren technischen Daten

### Offen

- SQLite/FTS5
- konkrete OCR-/HTR-Engine
- Volltextformate
- semantische Suche / RAG
- Embeddings
- Knowledge Graph
- Claim–Evidence-Datenmodell
- Umfang der Git-Ablage von Textauszügen
- konkrete CLI-Struktur

### Zurückgestuft / veraltet

- „Claim–Evidence Graph zuerst bauen“
- „YAML-Schemas der Forschungsobjekte als erster MVP“
- „feste Methodenkette Scoping → Meta-Narrative → CIS → Realist → Claim Graph“
- „Zotero ist bereits entschieden der Source of Truth“
- „SQLite/FTS ist bereits gesetzte Zielarchitektur“
- „Phase 1/Phase 2 ist bereits eine verbindliche Implementation Roadmap“

Diese Ansätze bleiben als Forschungs- oder Architekturhypothesen erhalten, müssen aber durch #10 validiert werden.

---

## 13. Nächster Arbeitsstand

Die nächsten Arbeiten sind **Research und Konzeptklärung**, nicht sofortige Implementierung:

1. Zielbild/Pain Points weiter aufnehmen und in Issues dokumentieren.
2. Problem- und Workflow-Map erstellen.
3. Leane State-of-the-Art-Recherche pro Problemklasse durchführen.
4. Capability Map validieren und vervollständigen.
5. Rollen-/Kompetenzmatrix daraus ableiten.
6. Transdisziplinäres Gesamtkonzept formulieren.
7. Bestehende technische Hypothesen bewerten: accepted / rejected / superseded.
8. Erst danach Architekturentscheidungen, Requirements und MVP definieren.

---

## 14. Verknüpfte Issues

- #1 – aktueller Research-Design-/Arbeitsstand
- #2 – Zielbild persönlicher Archivar
- #3 – Zotero-Hypothese
- #4 – OCR-/Volltext-Capability
- #5 – Retrieval-/Fundstellen-Capability
- #6 – Git-Provenienz
- #7 – langfristige transdisziplinäre Forschungsassistenz
- #8 – Automatisierung/KI-Unabhängigkeit
- #9 – Wissensgovernance
- #10 – State-of-the-Art-/Capability-/Rollen-Research-Plan
