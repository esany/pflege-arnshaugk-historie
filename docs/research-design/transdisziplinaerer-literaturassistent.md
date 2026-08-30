# Histo-Orla – transdisziplinäre historische Forschungsassistenz

**Status:** kanonischer, menschenlesbarer Konzept- und Arbeitsstand; noch keine finale Zielarchitektur  
**Letzte grundlegende Konsolidierung:** 2026-08-30  
**Kanonische Issues:** #1, #9, #10, #12–#16, #19–#25

---

## 1. Zweck und Zielzustand

Histo-Orla soll ein **funktionierendes, dauerhaft nutzbares Forschungssystem** für transdisziplinäre historische Arbeit werden. Es ist kein Selbstzweckprojekt für KI, Datenmodelle oder Softwarearchitektur.

Das System soll einen fachlich interessierten Research Owner ohne vorausgesetzte Spezialausbildung dabei unterstützen,

- belastbare Quellen und Forschungsliteratur zu finden und zu erschließen,
- unscharfe Beobachtungen in fachwissenschaftlich präzise Probleme zu übersetzen,
- die richtigen Fachbegriffe, Gegenstandsmodelle, Methoden und Quellenlogiken zu aktivieren,
- regionale Befunde mit territorialen, reichsweiten und europäischen Zusammenhängen zu verbinden,
- Befund, Interpretation, Kontroverse, Unsicherheit und Evidenzgrenze sichtbar zu halten,
- wiederkehrende mechanische Arbeit sinnvoll zu automatisieren,
- und einen nachvollziehbaren, restartbaren wissenschaftlichen Forschungszustand zu erzeugen.

Der frühere Begriff **„persönlicher Archivar“** bleibt als wichtige Spezialkompetenz bestehen. Er ist aber weder das Gesamtziel noch eine epistemische Oberinstanz.

Leitformel:

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

---

## 2. Präzedenz: Fachdomänen führen, Technologie dient

Die fachwissenschaftlichen Domänen bestimmen, welche Begriffe, Methoden, Evidenzanforderungen und zulässigen Schlussarten für ein Problem gelten. Technologie setzt diese Anforderungen um; sie darf sie nicht umdefinieren.

Kanonische Reihenfolge:

```text
konkreter Forschungsauftrag / Nutzer-Pain
→ einschlägige Fachdomäne(n)
→ wissenschaftliche Standards / Methoden / Evidenzbedarf
→ fachlicher + technischer State of the Art
→ internes Prior Art als Challenge/Input
→ validierte Needs / Capabilities / Quality Attributes
→ belastbare Requirements + Acceptance Criteria
→ Architektur / Design
→ Development / Integration
→ technische + wissenschaftliche Verifikation
→ reales MVP / Nutzung
→ Evaluation / Iteration
```

### Development

Development ist eine **verbindliche Umsetzungsdisziplin**, kein optionaler Nachsatz. Es ist verantwortlich dafür, validierte Requirements in ein tragfähiges, wartbares und nutzbares Werkzeug zu übersetzen.

Dev wird bereits in Discovery und State of the Art beteiligt, um:

- technische Machbarkeit zu beurteilen,
- bestehende Werkzeuge und Standards realistisch einzuschätzen,
- Integrations-, Migrations- und Wartungsrisiken früh zu erkennen,
- Architekturfolgen von Anforderungen sichtbar zu machen,
- mit kleinen Prototypen Unsicherheit zu reduzieren.

Aber:

> **Dev informiert Requirements; Dev besitzt sie nicht.**

Fachliche Anforderungen dürfen nicht aus technischer Convenience abgeschwächt werden.

---

## 3. Lean als zentrales Mantra

Lean bedeutet nicht „möglichst wenig Software“. Lean bedeutet:

> **so wenig unnötige technische Komplexität wie möglich, aber so viel funktionierendes System wie nötig, um validierte Nutzer- und Forschungsanforderungen hochwertig zu erfüllen.**

Daraus folgen:

- vorhandene Werkzeuge, Standards und Forschungsinfrastrukturen vor Eigenentwicklung prüfen;
- keine Infrastruktur „für später“ ohne beobachteten Bedarf oder klaren Trigger;
- keine formale Repräsentation komplexer als fachlich erforderlich;
- keine Automatisierung ohne reale wiederkehrende Friktion oder Qualitätsgewinn;
- keine KI, wenn deterministische oder spezialisierte Verfahren die Aufgabe besser, transparenter oder reproduzierbarer lösen;
- keine Optimierung für hypothetische Skalierung vor realem Bottleneck;
- kleine, verständliche und ersetzbare Komponenten bevorzugen;
- jede zusätzliche Abhängigkeit gegen konkreten Nutzer-/Forschungswert rechtfertigen.

**Lean gilt für Entwicklung, nicht für Inhaltsarbeit.** Fachliche Komplexität wird nicht reduziert, um Technik einfacher zu machen.

### Technischer Admission Test

Vor einer materiellen neuen technischen Komponente ist mindestens zu beantworten:

1. Welchen konkreten Nutzer-Pain oder wissenschaftlichen Qualitätsmangel adressiert sie?
2. Welche Fachdomäne oder welches validierte Requirement begründet sie?
3. Was ist die kleinste hinreichende Lösung?
4. Welcher mess- oder prüfbare Gewinn entsteht gegenüber dem Status quo?
5. Welche neue Komplexität, Abhängigkeit oder Wartungslast entsteht?
6. Kann derselbe Nutzen mit vorhandenen Werkzeugen oder einfacheren Mitteln erreicht werden?
7. Kann die Komponente später ersetzt/entfernt werden, ohne Forschungswissen zu verlieren?

Ohne überzeugende Antwort: **nicht bauen / nicht einführen**.

Kanonische Vertiefung: #24.

---

## 4. Forschungsziel und fachlicher Scope

### 4.1 Geschichte als transdisziplinäres Querschnittsthema

Relevante Perspektiven umfassen problemabhängig insbesondere:

- Archivistik / Registraturkunde / Provenienz
- Diplomatik / Quellenkunde
- Paläographie
- Editionswissenschaft / Textkritik
- historische Philologie / Sprachgeschichte / Lexikographie
- Mediävistik
- Landes-, Territorial-, Herrschafts- und Verfassungsgeschichte
- Frühneuzeitforschung
- Sozialgeschichte
- Wirtschafts- und Agrargeschichte
- Adels-, Hof-, Residenz- und Patronageforschung
- Reichs- und Territorialgeschichte
- Diplomatiegeschichte
- Rechts- und Verwaltungsgeschichte
- Kirchen-/Konfessionsgeschichte
- Militär-/Kriegsgeschichte
- historische Geographie / Kulturlandschaft
- Siedlungs-, Landschafts- und Mittelalterarchäologie
- Umweltgeschichte / historische Ökologie / Hydrologie / Geoarchäologie
- Volkskunde / Europäische Ethnologie
- historische Anthropologie / Sachkulturforschung
- Onomastik / Toponymie
- historische Kartographie / Historical GIS / Spatial Humanities
- historische Demographie
- Bau-/Architekturgeschichte und Denkmalpflege bei Bedarf
- Prosopographie / historische Netzwerkforschung
- Mobilitäts-, Reise-, Universitäts- und Bildungsgeschichte
- Connected / Entangled / Transregional History
- New Diplomatic History, Ordens-/Kreuzzugsgeschichte und weitere Spezialfelder bei konkretem Bedarf.

### 4.2 Zeitlicher Horizont

Schwerpunkte reichen vom Früh-/Hochmittelalter über Spätmittelalter und Frühe Neuzeit bis in Transformationsprozesse/Sattelzeit und Übergänge zur Moderne.

### 4.3 Regional verankert, europäisch verflochten

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

Kernräume sind Ostthüringen/Orla, Vogtland, Saalfeld und angrenzende thüringische Räume, Sachsen/Kursachsen, Franken, Egerland und Lausitz/Bautzen. Weitere Räume werden aktiviert, wenn reale Personen-, Herrschafts-, Quellen-, Bildungs-, Hof-, Kriegs-, Ordens- oder Diplomatieverflechtungen dies erfordern.

> **Regionaler Fokus für Tiefenschärfe – europäischer Horizont für Erklärung.**

Kanonische Vertiefung: #13, #14, #16.

---

## 5. Governing Principles

### 5.1 Wissenschaftliche Standards stehen über Nutzerformulierung und Technik

Jede aktivierte Disziplin arbeitet nach ihren eigenen einschlägigen wissenschaftlichen Standards, Terminologien, Quellenkritiken, Methoden und Evidenzregeln.

Diese Standards dürfen nicht abgeschwächt werden durch:

- unscharfe oder unwissenschaftliche Nutzerformulierungen,
- Wunsch nach einer einfachen Geschichte,
- Vermittlungsziele,
- UI-/Darstellungsanforderungen,
- Datenmodelle,
- Retrieval-/RAG-/Agentenlogik,
- Automatisierungs- oder Implementierungsvereinfachungen.

Technik und Nutzereingabe werden an die Wissenschaft übersetzt; die Wissenschaft wird nicht an Convenience angepasst.

### 5.2 Human-in-the-loop ohne Micromanagement

Der Research Owner muss nicht Repo-Engineer, Archivar, Paläograph, Methodensupervisor oder Entwickler werden.

Routine-Methodik, Repository-Mechanik, Recherchevorbereitung, deterministische Ableitungen, Synchronisation und andere klar delegierbare Arbeit dürfen Assistenz/Software übernehmen.

Konsequenzielle Arbeit muss zugleich:

- erklärbar,
- überprüfbar,
- anfechtbar,
- stoppbar,
- korrigierbar

bleiben.

Der Research Owner kontrolliert insbesondere Forschungsinteresse, Prioritäten, normative/materiale Systemänderungen, nicht ableitbare Rechteentscheidungen und folgenschwere Publikations-/Nutzungsentscheidungen.

### 5.3 Progressive Disclosure / Human Readability

Menschliche Lesbarkeit bedeutet nicht methodische Vereinfachung.

Eine Ausgabe kann verständlich beginnen und bei Bedarf bis zu Fachbegriffen, Methoden, Quelle, Fundstelle, Alternativen und Entscheidungspfad aufgeklappt werden.

Sinngemäßer Pfad:

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

### 5.4 Kein Wissensmonopol im Chat oder Modell

Chat ist Werkstatt. GitHub ist dauerhaftes Projektgedächtnis.

Nicht jeder Gesprächssatz muss archiviert werden. Aber ein neuer kompetenter Bearbeiter muss aus kontrolliertem Repo-Zustand rekonstruieren können:

- was das Ziel ist,
- welche Pains/Needs relevant sind,
- welche Leitplanken und Requirements gelten und warum,
- welche Fragen/Hypothesen offen sind,
- welche Evidenz und welches Prior Art tatsächlich geprüft wurden,
- wo Unsicherheit/Research Debt liegt,
- wer/was kanonischer Owner ist,
- und was als Nächstes zu tun ist.

Unverzichtbare Begründungen dürfen nicht ausschließlich in Chat-Historie, verborgenem Modellzustand oder Agentenkommunikation existieren.

### 5.5 Methodenkonforme KI ≠ unabhängige Expertenvalidierung

Eine KI kann methodengeleitet arbeiten, Quellen referenzieren und Fachliteratur einbeziehen. Das ist nicht automatisch unabhängige qualifizierte Fachvalidierung.

Validierungsstärke skaliert mit Konsequenz.

Kanonische Vertiefung: #9, #12, #15.

---

## 6. Forschungsebenen und Evidenz sauber trennen

Mindestens folgende Ebenen müssen unterscheidbar bleiben:

```text
Originalquelle / materieller Befund
→ digitale Instanz / Scan
→ OCR / HTR / Transkription / Derivat
→ fachliche Beobachtung / Befund
→ Normalisierung / Identifikation
→ Claim
→ fachliche Interpretation
→ transdisziplinäre Synthese
```

Spätere Ebenen dürfen frühere nicht stillschweigend umschreiben.

Beispiele:

- ein Regest ist nicht die Urkunde;
- OCR ist nicht das Original;
- eine normalisierte Person ist nicht die gelesene Namensform;
- eine Katalogbeschreibung ist nicht automatisch inspizierter Quellentext;
- eine Suchtrefferseite/Abstract ist Discovery, nicht automatisch Evidenz;
- eine plausible historische Erklärung ist nicht der Quellenbefund;
- AI-Ausgabe ist keine eigene Evidenzkategorie.

### Proportionale Validierung

Exploration, Working Research und publikations-/entscheidungsnahe Aussagen benötigen unterschiedliche Validierungsstärken.

Grundsatz aus `paleo-type`:

> Ein ungelöstes Ergebnis kann wissenschaftlich korrekt sein; ein unbelegt „gelöstes“ Ergebnis nicht.

---

## 7. Assistenz- und Kompetenzsystem

### 7.1 Research Owner

Gibt Erkenntnisinteresse, Prioritäten, Relevanz und Forschungsrichtung vor.

### 7.2 Research Coordinator / Expertise Routing

Hilft bei:

- Problemzerlegung,
- Erkennen fehlender Fachbegriffe,
- Auswahl notwendiger Kompetenzen,
- Folgefragen,
- transdisziplinärer Integration.

Der Coordinator ist **Orchestrator, keine epistemische Oberinstanz**.

### 7.3 Persönlicher Archivar als Spezialkompetenz

Zuständig insbesondere für:

- Literatur, Editionen und Quellen wiederfinden,
- Archive, Bestände und Findmittel erschließen,
- Provenienz / Registraturbildner rekonstruieren,
- Quellenarten und Überlieferungsstufen unterscheiden,
- Scans, Editionen, Regesten und Volltexte erschließen,
- exakte Fundstellen liefern,
- historische und archivische Suchterminologie nutzen,
- bibliographische Referenzen/Zotero koppeln,
- Quellenerwerb/Übernahme/Verarbeitung nachvollziehbar halten.

Er interpretiert einen Befund nicht automatisch mediävistisch, sozialhistorisch, archäologisch oder anderweitig fachlich.

### 7.4 Fachkompetenzen

Jede Kompetenz braucht mindestens:

```text
Fachsprache / Vokabular
+ Begriffs- und Gegenstandsmodelle
+ historische / regionale / archivische Terminologie
+ Quellengattungen und Überlieferungslogik
+ Rechercheheuristiken
+ Methoden / Playbooks
+ zulässige Schlussarten
+ Qualitäts- und Evidenzregeln
+ Forschungsstand / Kontroversen
+ regionale / zeitliche Spezialisierung
+ transdisziplinäre Schnittstellen
+ Eskalations-/Validierungsgrenzen
```

Ein Rollenprompt wie „Du bist Mediävist“ reicht nicht.

### 7.5 Epistemischer Vertrag je Kompetenz

Eine priorisierte Fachkompetenz muss perspektivisch beschreiben:

1. Welche Problemtypen kann sie bearbeiten?
2. Welche Fachsprache/Begriffe verwendet sie?
3. Welche Begriffs-/Gegenstandsmodelle setzt sie voraus?
4. Welche Quellen/Evidenztypen kann sie beurteilen?
5. Welche Methoden nutzt sie?
6. Welche Schlussarten sind zulässig?
7. Welche typischen Fehlschlüsse muss sie vermeiden?
8. Welche regionalen/zeitlichen Grenzen gelten?
9. Welche Kontroversen existieren?
10. Welche Nachbardisziplinen müssen bei bestimmten Problemen mitarbeiten?
11. Wann reicht automatisierte/KI-Unterstützung nicht?
12. Wann ist unabhängige qualifizierte menschliche Fachvalidierung angezeigt?

Kanonische Vertiefung: #15, #16, #19.

---

## 8. Fachliche Problemübersetzung: Nutzer muss Fachsprache nicht kennen

Eine Kernfähigkeit ist:

```text
Laienbeobachtung / unscharfe Frage
→ mögliche fachliche Problembegriffe
→ konkurrierende Begriffsmodelle
→ historische Quellenbegriffe / Schreibvarianten
→ moderne analytische Begriffe
→ ältere / umstrittene Historiographiebegriffe
→ Archiv-/Findbuchsprache
→ relevante Quellengattungen
→ einschlägige Disziplinen
→ Methoden / Fallstricke
→ Rechercheansätze
```

Die Rückübersetzung für den Research Owner vereinfacht die Sprache, **nicht die Wissenschaft**.

Wichtige Unterscheidungen:

- historischer Quellenbegriff
- zeitgenössische institutionelle/rechtliche Bezeichnung
- moderner analytischer Fachbegriff
- archivischer Erschließungsbegriff
- regionale Sonderterminologie
- ältere historiographische Kategorie
- heute umstrittener/überholter Begriff
- lateinische/fremdsprachige Entsprechung, wenn relevant.

Beispiele:

- `Ministeriale` ≠ einfach „Adliger“ oder „Beamter“;
- `Regest` ≠ Quelle selbst;
- `Vogtei` kann unterschiedliche institutionelle/rechtliche Bedeutungen haben;
- `Ostsiedlung`, `Landesausbau`, `Territorialisierung`, `Konfessionalisierung` usw. brauchen ggf. Begriffsgeschichte und Historiographiekritik.

Das System braucht daher ein **fachliches Begriffsnetz**, nicht nur Query-Synonyme. Die technische Form – Glossar, Concept Cards, Thesaurus, kontrolliertes Vokabular, Ontologie, Graph – bleibt eine spätere, problemabhängige Entscheidung.

---

## 9. Regionalisierte Expertise

Regionalkompetenz ist mehr als ein Ortsfilter.

Eine belastbare Fachrolle soll kennen bzw. gezielt erschließen können:

- historische Territorien/Herrschaften/Verwaltungsräume und ihre Veränderungen,
- regionale Forschungs- und Landesgeschichtstraditionen,
- relevante Archive, Bestände, Serien, Findmittel,
- Editionen, Regesten, Urkundenbücher,
- regionale Zeitschriften/Jahrbücher/Reihen/Bibliographien,
- Quellengattungen und typische Überlieferungslücken,
- historische/archivische Suchbegriffe und Schreibvarianten,
- territoriale Synonyme und ggf. Latein,
- naturräumliche / kulturlandschaftliche Bedingungen,
- Nachbar-/Vergleichsräume,
- relevante nationale/internationale Archive bei realen Verflechtungen,
- aktuelle regionale Kontroversen und ältere Narrative.

„Spitzenexpertise“ ist ein Zielniveau, keine Behauptung von KI-Unfehlbarkeit. Tiefe muss durch qualifiziertes Retrieval, aktuelle Fachliteratur, Referenzwerke, Quellenkompetenz, Methoden und ggf. externe Spezialistenprüfung abgesichert werden.

---

## 10. Historische Akteurs- und Handlungslogik

Personen sollen nicht nur als Knoten eines Netzwerks modelliert werden.

Zunächst zu untersuchende Erklärungscapability:

```text
Akteur in konkreter historischer Situation
→ soziale / institutionelle Position
→ belegte Beziehungen / Abhängigkeiten
→ Ressourcen
→ Informationshorizont
→ zeitgenössisch mögliche Handlungsoptionen
→ Zwänge / Risiken / Anreize
→ beobachtete Handlung
→ mögliche Motive / Erklärungen
→ alternative Erklärungen
→ Quellenbasis / Aussagegrenzen
```

Schutzregeln:

- keine retrospektiv elegante „innere Logik“ erfinden;
- keine Motivpsychologie ohne Evidenz;
- Ko-Präsenz / gleiche Universität / gleicher Hof ≠ belegte Beziehung;
- Interessen, Loyalitäten und Wissen nur soweit behaupten, wie Quelle und Fachmethode tragen;
- unterschiedliche adels-, sozial-, reichs-, konfessions-, wirtschafts-, diplomatie- oder militärgeschichtliche Erklärungen zunächst getrennt sichtbar halten.

Eine konkrete Datenstruktur ist noch nicht entschieden.

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
→ Quellenabhängigkeit?
→ anderer räumlicher Maßstab?
→ unterschiedliche Interessen der Akteure?
→ historiographische Differenz?
→ erst danach bewerten
```

Ein Widerspruch darf real bleiben. Ziel ist methodische Diagnose, nicht Harmonisierung.

---

## 12. Quellenarchiv, OCR/HTR, Retrieval und Provenienz

### 12.1 Grundpipeline

```text
Quelle / Literatur finden
→ übernehmen / referenzieren
→ exakte digitale Instanz kontrollieren
→ Original unverändert erhalten
→ OCR / HTR / Volltext / Transkription erzeugen
→ bibliographisch / archivalisch / provenance-seitig erfassen
→ indexieren / durchsuchen
→ lesen / annotieren
→ Fundstelle / Claim sichern
→ analysieren / synthetisieren
```

### 12.2 OCR / HTR

Mindestanforderungen:

- Original unverändert erhalten;
- OCR/HTR als Derivat kennzeichnen;
- Roh-OCR, korrigierten Text, Normalisierung und manuelle Transkription unterscheiden;
- Seiten-/Blatt-/Regeststruktur bewahren;
- historische Orthographie nicht still modernisieren;
- Eigennamen, Orts-/Flurnamen, Zahlen, Marginalien, Tabellen etc. als besondere Fehlerrisiken behandeln;
- jede relevante Textstelle zur konkreten Quelle/Fundstelle zurückführen;
- systematische OCR/HTR-Nutzung mit geeigneten Goldfällen/Metriken evaluieren.

Tools/Formate wie OCRmyPDF, Tesseract, OCR4all, Kraken, Transkribus, ALTO, hOCR, PAGE XML oder PDF-Textlayer sind Prüfgegenstände, keine Vorentscheidungen.

### 12.3 Retrieval

Validierte Bedürfnisse:

- exakte lexikalische Suche;
- Kontexttreffer;
- historische Schreib-/Namensvarianten;
- kontrollierte Query Expansion;
- Filter nach Werk, Zeitraum, Quellentyp, Collection/Tag etc.;
- Seiten-/Blatt-/Regest-genaue Fundstellen;
- transparente und reproduzierbare Suchstrategie.

Semantische Suche, Embeddings, RAG und Knowledge Graph bleiben Hypothesen und müssen Zusatznutzen belegen.

### 12.4 Zotero

Zotero ist eine starke bibliographische Kopplungshypothese, keine endgültige Source-of-Truth-Entscheidung. Zu prüfen sind u. a. Desktop/Web API, Fulltext-Zugriff, Collections/Tags, Attachment-Referenzen, Pyzotero/Better BibTeX, archivalische/nichtklassische Quellentypen und Verhältnis zu lokalem Such-/Forschungszustand.

### 12.5 Provenienz

Zu unterscheiden sind u. a.:

- archivalische/bibliographische Identität,
- persistent identifier / Signatur / URL,
- exakte inspizierte digitale Instanz,
- Hash/Byte-Identität,
- Derivat / OCR / Extrakt,
- kuratierter Forschungsbefund,
- regenerierbarer Index/Cache.

Ein Hash ersetzt keine Archivsignatur; eine Archivsignatur ersetzt nicht den Nachweis der konkret inspizierten Datei.

Kanonische Vertiefung: #2–#6, #12, #24.

---

## 13. Forschungszustand vs. Vermittlung

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

Eine Vermittlungsaussage darf den Forschungszustand nicht rückwirkend verändern.

Ein nachgelagertes System wie `rgk-main-ssot` kann Vermittlungs-/Anwendungskontext sein. Die technische Schnittstelle ist offen. Zu prüfen ist später ein leaner Übergabevertrag mit Aussage, Quellen/Fundstellen, Evidenzstatus, Aussagegrenzen, Kontroversen und Rückverfolgbarkeit.

Histo-Orla muss keine Besucherdramaturgie, Social-Media-Sprache oder Ausstellungserzählung optimieren.

Kanonischer Owner: #20.

---

## 14. Interne Referenzprojekte / Prior Art

Interne Referenzprojekte sind **Input und Challenge**, keine automatische Requirement- oder Architekturquelle.

### 14.1 `paleo-type` – #12

Schwerpunkt:

- Governing Objective / Präzedenz
- Forschungsgovernance
- Evidenzstatus / Provenienz
- Source identity vs. exact digital instantiation
- Original / Derivat / Interpretation
- METHOD / CORPUS / PROJECT
- Human-in-the-loop / Operational Ownership
- Explainability / Challengeability
- Progressive Disclosure
- Restartability
- one fact / one canonical owner
- proportionale Validierung
- adversariale Qualität / Falsifikation
- methodenkonforme AI ≠ unabhängige Fachvalidierung
- AI-Provenienz bei consequential use
- AI/HTR-as-method → Evaluation
- material research-system change admission
- Lean / technische Subsidiarität.

Tatsächlich substanziell inspiziert wurden die zentralen Governance-/Methodendateien, darunter `README.md`, `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `DECISIONS.md` sowie zentrale Dateien unter `methodology/` zu AI Governance, Evidence, Source/Provenance, Historical Workflow, Gates, Quality/Learning, Maintenance und Project Lifecycle. Ein Exhaustiv-Audit des gesamten Repositories wird **nicht** behauptet; weitere Bereiche wie `requirements/`, `tests/`, `tools/`, `templates/`, `projects/` usw. können später zusätzlichen Erkenntnisgewinn liefern.

### 14.2 `rgk-main-ssot` – #21

Schwerpunkt:

- Modellhierarchie Forschung/Interpretation/Vermittlung/Darstellung;
- Modell führt Darstellung, nicht umgekehrt;
- neutrale/stabile Identitäten;
- Claim → Evidence → Interpretation;
- Source Roles / projektbezogene Quellenfunktionen;
- Provenienz vor Wirkung;
- Abweichungen als Erkenntnisobjekte;
- mehrere Views auf einen Zustand;
- Zeit-/Raum-/Akteursbezug;
- Forschung↔Vermittlung.

Konkret inspizierte, tragende Dateien umfassen u. a. `PROJECT_CONTEXT.md`, `README.md`, `TREE.md`, `archive/handoff_v1/01_MODEL/01_MODEL_KERNEL.md`, `archive/handoff_v1/01_MODEL/03_KNOWLEDGE_AND_PROVENANCE.md` und `archive/handoff_v1/02_PROCESS/01_WORKFLOW.md` sowie die Existenz relevanter Templates/Manifeste.

Reichere alte Working Notes wie `relationales_befund_vermittlungsmodell_rittergut_knau.md` und `durchlauf_logik_befund_vermittlungsmodell_rittergut_knau.md` sind im Handoff-/Manifestkontext nachgewiesen, aber im aktuellen `main` nicht als normal zugängliche Dateien vorhanden. Ihr erinnerter Inhalt gilt **nicht** als gesichertes Prior Art, solange er nicht rekonstruiert und gelesen wurde.

### 14.3 Gemeinsame Analyseschnittstelle

```text
Prior-Art-Befund
→ exakte Herkunft / tatsächlich inspizierte Datei klären
→ Ursprungsproblem bestimmen
→ prüfen, ob Histo-Orla dasselbe Problem hat
→ wissenschaftliche Invariante extrahieren
→ führende Fachdomäne(n) bestimmen
→ externen State of the Art prüfen
→ Risiken Übernahme / Nichtübernahme
→ konkreten Nutzerwert bestimmen
→ inherit / adapt / research / reject
→ Capability / Quality Criterion / Requirement Candidate
→ erst danach technische Option
```

Keine direkte Kante `Referenzprojekt → Implementation`.

Bei Widersprüchen entscheidet:

> **aktueller Forschungsauftrag + führende Fachdomäne(n) + Evidenz + externer State of the Art + nachweisbarer Nutzerwert.**

---

## 15. Kompetenzlandkarte für die Konzeption des Systems

Neben den historischen Laufzeitkompetenzen braucht die Entwicklung von Histo-Orla selbst Meta-/Designkompetenzen. Kanonische Vertiefung: #22.

Wesentliche Felder:

- Research Strategy / wissenschaftliches Forschungsdesign
- Scholarly Requirements Engineering / Business Analysis
- User Research / Human Factors für Forschungsarbeit
- Workflow-/Prozessanalyse
- Wissenschaftstheorie / Epistemologie / Research Integrity
- Historiographie / Wissenschaftsgeschichte
- State-of-the-Art-/Evidence-Synthesis-Kompetenz
- Risikoanalyse / Adversarial Review / Failure Analysis
- Quality Engineering / wissenschaftliche Evaluation
- Decision Architecture / Governance / Change Management
- Systems Thinking
- Research Data Management / Provenienz / Reproduzierbarkeit
- Information Architecture / Knowledge Organization
- Rechte / Lizenzen / Data Governance
- Research Software Engineering / Development
- Information Retrieval / Search Engineering
- OCR/HTR / Document Processing / Digital Humanities
- AI/LLM Engineering + AI Evaluation
- Human-readable Research UX.

Diese Kompetenzen sind **keine Liste technischer Agenten**. Für jede konkrete Aufgabe ist zu entscheiden, welche Kompetenz tatsächlich gebraucht und durch Mensch, vorhandenes Tool, Software, spezialisierten Algorithmus, KI oder externe Fachperson erbracht wird.

---

## 16. Software-/Systemkompetenzen und Arbeitsteilung

Kanonischer Owner: #24.

### 16.1 Verantwortungsarten

Mindestens zu unterscheiden:

1. Research Owner
2. qualifizierter Fachspezialist
3. deterministische Software
4. spezialisierte Algorithmen / IR / OCR / ML
5. generative KI / LLM
6. externe Systeme / Standards / Datenbanken.

### 16.2 Grundsatz der Capability Allocation

```text
formal definierbare Regel / bitgenaue Reproduzierbarkeit
→ deterministische Software / Validator

enges Mustererkennungsproblem mit messbarem Benchmark
→ spezialisiertes Verfahren

offene semantische Exploration / Sprachübersetzung
→ ggf. LLM-assistiert

historische Interpretation
→ Fachmethode + Evidenz; KI nur Assistenz

unabhängige Validierung erforderlich
→ unabhängige Evidenz / echter qualifizierter Spezialist
```

### 16.3 KI-negative Kernzone

Generative KI soll grundsätzlich nicht die alleinige Verantwortung tragen für:

- kanonische Speicherung,
- IDs / Referenzen,
- Hashes / Dateiintegrität,
- Versionshistorie,
- Zugriffsrechte,
- Provenienzlinks,
- bekannte exakte Fundstellen,
- Schema-/Invariant-Prüfung,
- deterministische Konvertierung,
- Status-/Workflow-State,
- Synchronisation,
- Backup/Restore,
- Query-/Processing Logs,
- Reproduzierbarkeitsmetadaten,
- Lizenz-/Policy-Flags.

KI darf diese Informationen lesen, erklären oder Kandidaten erzeugen, aber nicht ihre Verlässlichkeit ersetzen.

### 16.4 KI als Kandidaten-/Vorschlagsmaschine

Bevorzugtes Muster:

```text
Input mit Provenienz
→ KI erzeugt Kandidat / Vorschlag
→ Candidate State
→ deterministische / fachliche Prüfung soweit möglich
→ erst dann Promotion in kanonischen Forschungszustand
```

Beispiele: Entity Merge, Fachbegriff, Relation, OCR-Korrektur, Claim Extraction.

### 16.5 Softwarekompetenzen

Je nach validiertem Bedarf u. a.:

- Modular Software Architecture
- Domain Modeling unter fachlicher Führung
- Data Engineering / Data Lifecycle
- Persistence / Storage
- Search / IR
- Workflow / Pipeline Engineering
- Provenance / Audit / Logging
- Validation / Invariant Enforcement
- Test Engineering / Verification
- Interoperability / API / Standards
- Security / Privacy / Secrets
- Reliability / Observability / Recovery
- Performance/Scale erst bei Trigger
- Dependency / Supply Chain / Maintainability
- Portability / Local-first / Offline, soweit begründet
- AI Integration bewusst nachgeordnet.

---

## 17. Repräsentative reale Design-/Falsifikationsfälle

Die Konzept-/SOTA-/Requirements-Arbeit darf nicht rein abstrakt bleiben. #10 definiert mindestens vier reale Testfamilien.

### U1 Historische Teich-/Niederungs-/Landnutzungsstrukturen vor 1800

Beispielraum: Arnshaugk / Orla / Vogtland / Ostthüringen.

Zu berücksichtigende Quellengruppen u. a.:

- Forst-, Flur-, Hutungs- und Grenzrisse des 17./18. Jahrhunderts
- Jagd-/Forstkarten
- Guts-/Rittergutsvermessungen
- Grenzstreitigkeiten
- Hutungs-/Triftstreitigkeiten
- Teich-/Fischerei-/Wasserrechtsakten
- Mühlen-/Wasserbauakten
- Amtsrechnungen sowie Teich-/Fischereirechnungen
- Lehns-/Besitzregister, Urbare, Sal-/Erbbücher
- Gemeinheitsteilungen / Separation
- Kataster-/Flurbücher
- Orts-/Landesbeschreibungen
- Meilenblätter und ältere Karten
- historische Luftbilder
- LiDAR/DEM und weitere räumliche Vergleichsdaten.

Prüft u. a. Archivterminologie, Provenienz-/Bestandsrouting, Kartenkritik, OCR, Retrieval, historische Geographie, Umwelt-/Agrar-/Besitzgeschichte, Discrepancy Reasoning und Multi-Scale-Arbeit.

### U2 Mittelalterliche Herrschaft / Vogtei / Ministerialität / Siedlung

Eine laienhafte Beobachtung muss konkurrierende Fachmodelle erschließen können: z. B. Vogtei/Kirchen-/Schutzvogtei, Ministerialität, Lehnsbeziehung, Gerichtsherrschaft, Grundherrschaft, Patronat, Territorialisierung.

Prüft Fachübersetzung, Diplomatik/Regestenkompetenz, Quellen-/Begriffsstatus, regionalisierte Mediävistik, Archiv-/Editionsrecherche und anachronismussichere Sprache.

### U3 Frühneuzeitlicher adliger Akteur / Handlungslogik

Akteur um 1600–1640 zwischen regionalem Besitz, Kursachsen, Reich/Kaiserhof, Konfession, Militär, Verwandtschaft, Patronage, Hof und Mobilität.

Prüft Prosopographie, Entity Resolution, Akteurs-/Handlungslogik, Informationshorizont, Optionen/Zwänge, alternative Erklärungen, keine Motivpsychologie ohne Evidenz und regionale↔europäische Maßstabswechsel.

### U4 Persönliches Quellenarchiv / Fundstellenarbeit

Edition/Regestenwerk/Scan übernehmen, OCR-/Volltext-erschließen, exakt durchsuchen und mit Seite/Blatt/Regest auf konkrete Quelle zurückführen.

Prüft Zotero-Hypothese, OCR/HTR, exakte/historische Suche, Provenienz, Derivatstatus, Query Reproducibility und Human-readable Audit View.

Diese Fälle sind **Design-/Falsifikationsfälle**, keine abschließende Featureliste.

---

## 18. State-of-the-Art-Programm

Kanonischer Owner: #10.

### 18.1 Fachwissenschaftlicher SOTA

Pro priorisiertem Problem/Fach zu untersuchen:

- aktuelle Methoden und Standards,
- Fachsprache / Begriffsmodelle,
- Quellenarten / Überlieferungslogik,
- zulässige Schlussarten,
- Kontroversen / ältere Narrative,
- Handbücher/Lexika/Referenzwerke,
- Journals/Bibliographien,
- Editionen/Regesten/Datenbanken,
- Archive/Bestände/Portale,
- regionale Besonderheiten und Vergleichsräume.

### 18.2 Infrastruktur-/Methoden-/Software-SOTA

U. a.:

- Literaturverwaltung / Zotero / PKM-RKM
- Digital Humanities
- OCR / HTR / Layout Processing
- Korpusmanagement / Volltextsuche
- Information Retrieval / fuzzy / Query Expansion / Hybrid Search
- historische NLP / Entity Resolution
- Gazetteers / Authority Data
- Research Data Management / Provenienz / Reproduzierbarkeit
- Knowledge Organization / Thesauri / Ontologien / Knowledge Graphs
- Evidence-/Claim-Modellierung
- Review-/Evidence-Synthesis-Methoden
- Citation Chaining / bibliometrische Exploration
- Workflow/Pipeline Automation
- portable/local Research Tooling
- Softwaretests / wissenschaftliche Quality Gates
- AI/RAG/Agents nur als zu prüfende Optionen
- Human-readable Research UX.

### 18.3 Bewertungsraster

Jeder Ansatz mindestens nach:

1. konkretem Problem/Nutzerbedarf
2. wissenschaftlicher/technischer Community
3. Begriffs-/Gegenstandsmodell
4. Quellen-/Daten-/Evidenzannahmen
5. regionalen/zeitlichen Grenzen
6. Reife/Pflege/praktischer Einsatzfähigkeit
7. Qualitäts-/Evaluationsmetriken
8. Fehler/Bias/Blind Spots
9. Provenienz/Auditierbarkeit
10. Human Readability / Challengeability
11. Lock-in / Dependencies / Rechte
12. Wiederverwendbarkeit statt Eigenbau
13. Passung zu realen Use Cases
14. mess-/prüfbarem Nutzergewinn
15. leanster hinreichender Nutzung/Umsetzung.

State of the Art ist **kein Produktkatalog und kein Selbstzweck**.

---

## 19. Capability Map und Expertise Profiles

Capabilities werden lösungsneutral formuliert. Kandidaten u. a.:

- Literatur/Quellen identifizieren und referenzieren
- Archive/Bestände aus historischer Verwaltung/Provenienz ableiten
- digitale/bildbasierte Quellen erschließen
- Volltexte seiten-/regeststabil durchsuchen
- historische Schreibweisen/Namen/Terminologien expandieren
- unbekanntes Fachvokabular erschließen
- historische/archivische/moderne/historiographische Begriffe unterscheiden
- passende Quellengattungen/Methoden/Fachkompetenzen ableiten
- Fundstellen verlässlich zurückführen
- Befund/Normalisierung/Claim/Interpretation/Synthese trennen
- heterogene Evidenz methodengerecht bewerten
- Discrepancies diagnostizieren
- regionale/europäische Maßstäbe kontrolliert verbinden
- Akteurs-/Handlungssituationen evidenzbasiert rekonstruieren
- Fachperspektiven getrennt prüfen und integrieren
- Kontroversen/Unsicherheit offen halten
- Forschungszustand human-readable/auditierbar darstellen
- wiederkehrende mechanische Arbeit reproduzierbar automatisieren.

### Expertise Profile

Für jede priorisierte Fachkompetenz mindestens:

1. Problemklassen / Scope
2. Epoche / Region
3. Fachsprache / Kernvokabular
4. historische/regionale/archivische Terminologie
5. Begriffs-/Gegenstandsmodelle
6. Kernmethoden / Playbooks
7. Quellenarten / Aussagegrenzen
8. Überlieferungs-/Archivlogik
9. Rechercheheuristiken
10. Archive/Bestände/Sammlungen/Portale
11. Referenzwerke/Lexika/Handbücher/Bibliographien/Journals
12. Editionen/Regesten/Datenbanken
13. Forschungsstand/Kontroversen
14. zulässige Schlussarten
15. Qualitäts-/Falsifikationskriterien
16. typische Fehlschlüsse
17. transdisziplinäre Schnittstellen
18. AI-/Tool-Unterstützung und Grenzen
19. Human Review / Eskalation
20. unabhängiger Validierungsstatus.

---

## 20. Risiko- und Qualitätsmodell

Kanonische Kompetenzabdeckung: #22.

Mindestens zu prüfende Risikofamilien:

- falsche Provenienz
- Source Laundering
- OCR-/HTR-Fehler
- Retrieval Blind Spots
- falsche Entitätsauflösung / False Merge
- Anachronismus / Terminologiefehler
- falscher Expertenkonsens
- Modell-/Agentenabhängigkeit als Scheinevidenz
- unzulässige Synthese inkommensurabler Evidenz
- regionale Container-Biases
- Motivpsychologie ohne Evidenz
- technische Lock-ins
- Rechte-/Lizenzprobleme
- stille Daten-/Schema-/Modellmigration
- unlesbare / nicht auditierbare Zustände
- Automatisierung vor verstandenem Workflow
- Vermittlungsnarrativ schreibt in Forschung zurück.

Erwartete Artefakte:

- Risk Register
- Failure Taxonomy
- Falsification Tests
- Quality/Evaluation Matrix
- Trigger für stärkere Validierung.

---

## 21. Evaluation

### OCR/HTR

- CER/WER
- Fehler bei Namen, Zahlen, historischen Begriffen
- Seiten-/Layout-/Fundstellenerhalt

### Retrieval

- Recall / Precision
- transparente Query Expansion
- historische Varianten
- Gold-/Schwierige Testfälle

### Archiv-/Quellenrecherche

- relevante Provenienzbildner/Bestandsgruppen erkannt?
- historische/archivische Terminologie genutzt?
- Search Boundaries dokumentiert?
- Katalog/Findmittel nicht als gelesene Quelle ausgegeben?

### Provenienz / Fundstellen

- richtige Quelle/Edition/digitale Instanz?
- richtige Seite/Folio/Regest?
- Inspektionsstatus klar?
- keine erfundenen Belege?

### Fachübersetzung

- relevante Fachbegriffe/Alternativmodelle entdeckt?
- historische vs. moderne vs. archivische Sprache getrennt?
- Anachronismen vermieden?

### Expertise Routing

- richtige Disziplinen aktiviert?
- Methoden/Quellenlogiken passend?
- regionale/zeitliche Grenzen erkannt?
- Nachbardisziplinen rechtzeitig zugeschaltet?

### Discrepancy Reasoning

- Zeit, Gattung, Überlieferung, Zweck, Abhängigkeit, Begriff, Maßstab, Interessen und Historiographie geprüft?

### Akteursanalyse

- Beziehung tatsächlich belegt?
- Wissensstand/Optionen zeitgenössisch rekonstruiert?
- Motive als belegt vs. interpretiert gekennzeichnet?
- alternative Erklärungen sichtbar?

### Automation / Software

- Reproduzierbarkeit / Idempotenz
- Invariant Enforcement
- Recovery / Restart
- Migration ohne epistemischen Verlust
- nachvollziehbare Fehlerzustände
- Providerwechsel ohne Verlust kanonischen Forschungswissens.

### AI

- konkreter Zusatznutzen gegenüber einfacheren Verfahren?
- bekannte Failure Modes?
- AI-Provenienz bei consequential use?
- Goldfälle/Evaluation bei systematischer Nutzung?
- kein Modellkonsens als unabhängige Evidenz?

### Restartability

- Kann ein anderer kompetenter Bearbeiter aus Repo + kontrolliertem Material ohne Chat fortsetzen?

---

## 22. Requirements Engineering

Requirements entstehen **vor der Architekturentscheidung** und werden aus validierten Needs, fachlichem SOTA, Capabilities und Qualitätszielen abgeleitet.

Zu unterscheiden sind u. a.:

- Functional Requirement
- Scientific/Epistemic Requirement
- Data/Provenance Requirement
- Quality Attribute
- Human Control / Audit Requirement
- Rights/Security Constraint
- Interoperability/Portability Requirement
- Performance/Scale Requirement nur bei belegtem Bedarf.

Traceability:

```text
Need / Pain
→ fachliche Begründung / SOTA
→ Capability
→ Quality Criterion
→ Requirement
→ Acceptance Test
→ Architekturentscheidung
→ Implementation
→ Evaluation Result
```

Kanonische Vertiefung: #10, #22.

---

## 23. Architektur, Development und MVP

Erst nach belastbaren Requirements werden Architekturvarianten und Trade-offs verglichen.

### Architekturfragen bleiben derzeit offen

- konkrete OCR-/HTR-Engine
- Volltextformate
- Speicher-/Indextechnologie
- Zotero-Rolle im Gesamtdatenmodell
- lokale vs. versionierte Volltexte
- semantische Suche / Embeddings / RAG
- Knowledge Graph / Ontologie
- Claim-/Evidence-Repräsentation
- Akteurs-/Event-/Relationsmodell
- Multi-Agent-Architektur
- UI/Application
- technische Schnittstelle zu RGK.

### Development-Aufgaben

Nach validierten Requirements je nach Bedarf:

- Softwarearchitektur / Domain Modeling
- Daten-/Persistenzlogik
- Integrationen / APIs / Import-Export
- Search / Indexing
- Workflows / Automation
- Validatoren / Invarianten
- Tests / Migration / Recovery / Observability
- Security / Privacy
- Human-readable Research Views
- Integration spezialisierter Verfahren
- begrenzte, evaluierte KI-Integration.

### MVP

MVP ist **kein vorab festgelegtes Featurepaket**. Er wird aus priorisierten validierten Requirements und realen Use Cases abgeleitet.

Ziel des MVP ist nicht nur technische Demonstration, sondern nachweisbarer Forschungsnutzen.

---

## 24. Erwartete Research-/Delivery-Artefakte

Vor bzw. im Verlauf der Umsetzung entstehen mindestens:

- [ ] konsolidierte Need-/Pain-/Goal Map
- [ ] Current-State Research Workflow
- [ ] Open-Question / Constraint Register
- [ ] Risk Register + Failure Taxonomy
- [ ] repräsentative Use Cases / Gold Cases
- [ ] SOTA-Matrix fachwissenschaftlich
- [ ] SOTA-Matrix Infrastruktur/Software
- [ ] regionale SOTA-/Quellen-/Archivmatrix
- [ ] Prior-Art Transfer Matrix `paleo-type`
- [ ] Prior-Art Transfer Matrix RGK
- [ ] Capability Map
- [ ] Competency Coverage Matrix
- [ ] Expertise Profiles
- [ ] Vokabular-/Begriffsmodell-Anforderungen
- [ ] Quality / Evaluation Matrix
- [ ] Requirements Backlog + Traceability
- [ ] Capability Allocation Matrix
- [ ] Architekturvarianten + Trade-offs
- [ ] ADRs
- [ ] priorisiertes MVP
- [ ] funktionierende Implementierung
- [ ] wissenschaftlich-technische Verifikation
- [ ] Evaluation im realen Forschungsalltag
- [ ] Iterations-/Learning-Backlog.

---

## 25. Aktuelle Hypothesen / Nicht-Entscheidungen

### Validierte Ziele / Prinzipien

- funktionierender, wissenschaftlich belastbarer persönlicher Forschungszustand
- fachwissenschaftliche Übersetzung für einen Laien-Research-Owner
- transdisziplinäres Expertise Routing
- regionale Tiefenschärfe + europäischer Horizont
- Human-in-the-loop / Auditierbarkeit / Challengeability
- kein Wissensmonopol im Chat
- Fachdomänen führen, Technologie dient
- Dev realisiert validierte Requirements
- Lean / technische Subsidiarität
- Automatisierbarkeit ohne unnötige KI-Abhängigkeit
- Forschung↔Vermittlung strikt trennen.

### Starke, aber zu prüfende Hypothesen

- Zotero als zentrale bibliographische Kopplung
- script-/local-first / AI-optional
- lokale Such-/Volltextschicht
- kontrollierte Fachvokabulare / Begriffsnetze
- modulare Fachprofile / Retrieval-Kontexte / Tools.

### Offen

- konkrete Architektur und Technology Stack
- OCR-/HTR-Engine
- Datenbank / FTS / Suchindex
- RAG / Embeddings / Hybrid Search
- Knowledge Graph / Ontologie
- konkretes Claim-/Evidence-Datenmodell
- Akteurs-/Event-/Relationsrepräsentation
- echte Multi-Agent-Architektur
- RGK-Übergabeschnittstelle.

### Zurückgestuft / superseded

- persönlicher Archivar als gesamte Oberinstanz
- Claim–Evidence Graph zuerst bauen
- YAML-Schemas als erster MVP
- feste Methodenkette Scoping → Meta-Narrative → CIS → Realist → Claim Graph
- Zotero bereits entschieden als Source of Truth
- SQLite/FTS als gesetzte Architektur
- Multi-Agent aus Fachrollen ableiten
- Vermittlungsanforderungen in Forschungszustand schreiben
- Architektur vor Requirements festlegen.

---

## 26. Nächster methodischer Schritt

Kanonischer Arbeitsplan: #10.

1. Needs / Goals / Pains und reale Research Workflows konsolidieren.
2. Open Questions, Constraints und Risiken erfassen.
3. reale Use Cases/Gold Cases als Falsifikations- und Designfälle schärfen.
4. fachwissenschaftlichen, regionalen und technischen State of the Art recherchieren.
5. internes Prior Art anhand #12/#21 gegen externen SOTA challengen.
6. Capabilities, Expertise Profiles und Quality Criteria ableiten.
7. belastbare Requirements + Acceptance Tests + Traceability formulieren.
8. Capability Allocation und Architekturvarianten vergleichen.
9. ADRs / priorisierten MVP ableiten.
10. Dev setzt die validierte Lösung lean um.
11. technische + wissenschaftliche Verifikation im realen Forschungsalltag.
12. Evaluation und Iteration.

---

## 27. Issue-Landkarte / kanonische Ownership

### Steuerung / Governance

- #1 – aktueller Gesamt-/Research-Design-Stand
- #9 – Governance: HITL, Standards, Auditierbarkeit, kein Wissensmonopol
- #10 – Research/SOTA/Requirements/Delivery-Plan
- #22 – Kompetenzlandkarte / Requirements / Risiko / Evaluation
- #23 – Issue Ownership / Traceability
- #25 – Chat↔Repo-Konsistenzaudit

### Fachlicher Scope / Qualität

- #13 – transdisziplinärer Forschungshorizont / Routing
- #14 – regional verankert, europäisch verflochten
- #15 – fachliche Tiefe / Kontroversen / Unsicherheit
- #16 – regionalisierte Expertise Profiles
- #19 – Fachkompetenz: Sprache, Modelle, Quellen, Methoden
- #20 – Boundary Forschung↔Vermittlung

### Quellen-/Infrastrukturthemen

- #2 – persönlicher Archivar / Spezialrolle
- #3 – Zotero-Hypothese
- #4 – OCR/HTR/Volltext
- #5 – Retrieval / historische Query Expansion / Fundstellen
- #6 – Git/Provenienz
- #8 – Automatisierung / KI-Unabhängigkeit

### Internes Prior Art

- #12 – `paleo-type`
- #21 – `rgk-main-ssot`

### Software / Development

- #24 – Software-/Systemkompetenzen, Arbeitsteilung, Lean Development

### Historische Provenienz / superseded

- #7 – superseded Zielbild
- #11 – abgeschlossener alter Concept Audit
- #17 – superseded Vokabularissue
- #18 – superseded Expertise-/Method-Pack-Issue

---

## 28. Leitformeln

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Fachdomänen führen. Technologie dient.**

> **Dev informiert Requirements; Dev besitzt sie nicht.**

> **Lean hält Entwicklung auf den konkreten Forschungsauftrag und nachweisbaren Nutzerwert fokussiert.**

> **Nicht eine Antwort mit Experten-Ton, sondern fachlich begründete Perspektiven mit sichtbarer Evidenz, Kontroverse und Unsicherheit.**

> **Regionaler Fokus für Tiefenschärfe – europäischer Horizont für Erklärung.**

> **Forschung erzeugt den belastbaren Zustand. Vermittlung erzeugt adressatenspezifische Sichten darauf.**

> **Kein Wissensmonopol im Chat.**
