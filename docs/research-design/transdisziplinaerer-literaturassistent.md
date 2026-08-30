# Transdisziplinärer Literatur- und Quellenassistent für Pflege Arnshaugk

## Zweck

Dieses Dokument beschreibt eine methodische und technische Architektur für einen Forschungsassistenten, der die Literatur- und Quellenarbeit im Projekt *Pflege Arnshaugk* unterstützt. Ziel ist ausdrücklich nicht nur ein PDF-Chat oder eine semantische Suche, sondern ein provenance-first System, das Forschungsfragen, Begriffe, Forschungstraditionen, Quellen, Claims, Evidenz, Widersprüche und Synthesen nachvollziehbar miteinander verknüpft.

## Ausgangspunkt

Transdisziplinäre historische Forschung kombiniert häufig sehr unterschiedliche Wissensformen: Geschichtswissenschaft, historische Geographie, Archäologie, Umweltgeschichte, Hydrologie, Ökologie, Forstgeschichte, Rechtsgeschichte, Besitz- und Verwaltungsgeschichte, Kartographiegeschichte, Ortsnamenforschung, Regionalgeschichte und gegebenenfalls naturwissenschaftliche Rekonstruktionen. Diese Felder verwenden unterschiedliche Begriffe, Skalen, Evidenztypen und Qualitätskriterien.

Ein Assistenzsystem darf diese Unterschiede nicht durch ein einheitliches Relevanz- oder Evidenzranking verwischen. Seine Aufgabe sollte vielmehr darin bestehen, die Unterschiede explizit zu machen, Übersetzungen zwischen Fachsprachen vorzuschlagen und jede Synthese auf ihre Quellen und methodischen Voraussetzungen zurückführbar zu halten.

## Methodisches Rückgrat

### 1. Scoping Review

Zu Beginn wird der Forschungsraum möglichst breit kartiert. Ziel ist nicht sofortige Evidenzbewertung, sondern die Erfassung von Disziplinen, Begriffsfamilien, Quellentypen, Zeiträumen, Räumen, Akteuren und Forschungsnarrativen.

### 2. Meta-Narrative Review

Die Meta-Narrative Review eignet sich besonders für Gegenstände, die in verschiedenen Forschungstraditionen unterschiedlich konzeptualisiert werden. Der Assistent sollte daher rekonstruieren:

- welche Forschungstraditionen einen Gegenstand untersuchen,
- welche Begriffe und Definitionen sie verwenden,
- welche Theorien und Modelle zugrunde liegen,
- welche Methoden als legitim gelten,
- welche Quellen oder Datentypen bevorzugt werden,
- wie sich diese Traditionen historisch entwickelt haben,
- wo sie miteinander übereinstimmen oder in Konflikt geraten.

Zentrale Prinzipien sind Pragmatismus, Pluralismus, Historizität, Kontestation und Reflexivität.

### 3. Critical Interpretive Synthesis

CIS dient dazu, aus heterogener Literatur analytische Konzepte zu entwickeln, statt nur Ergebnisse zu aggregieren. Dies ist für historische Raum- und Landschaftsrekonstruktionen wichtig, weil Begriffe wie Teich, Sumpf, Hutung, Trift, Gemeinheit, Flur, Gehölz, Forst, Grenze, Nutzung oder Besitz je nach Zeit und Quellengattung unterschiedliche Bedeutungen haben können.

### 4. Realist Reasoning

Wo kausale oder funktionale Fragen auftreten, sollte der Assistent Context–Mechanism–Outcome-artig arbeiten: Unter welchen Bedingungen wirkt ein Prozess, durch welchen Mechanismus und mit welchem Ergebnis? Dies verhindert zu einfache Aussagen wie „Teiche entstanden wegen Fischwirtschaft“, wenn Besitzrecht, Relief, Wasserführung, Herrschaft, Arbeitsorganisation und Markt gleichzeitig relevant sein können.

### 5. Claim–Evidence Mapping

Jede belastbare Aussage sollte in atomare Claims zerlegt werden. Jeder Claim erhält Verknüpfungen zu:

- Quelle,
- genauer Fundstelle,
- Evidenztyp,
- räumlicher Gültigkeit,
- zeitlicher Gültigkeit,
- Unsicherheit,
- unterstützenden Claims,
- widersprechenden Claims,
- abgeleiteten Schlussfolgerungen.

Damit kann später geprüft werden, welche Aussagen direkt auf Primärquellen beruhen und welche nur sekundär tradiert werden.

## Wissenschaftliche Assistenzoperationen

### Problem Framing

Der Assistent hilft, Forschungsgegenstand, Erkenntnisinteresse, Raum, Zeitraum und relevante Skalen explizit zu formulieren.

### Question Decomposition

Forschungsfragen werden in deskriptive, kausale, chronologische, räumliche, rechtliche, funktionale und interpretative Teilfragen zerlegt.

### Epistemic Scoping

Der Assistent schlägt relevante Disziplinen und Forschungstraditionen vor, auch wenn deren Terminologie von der Ausgangsfrage abweicht.

### Begriffsexpansion und historische Terminologie

Zu jedem Kernbegriff werden moderne Synonyme, historische Schreibweisen, ältere Rechts- und Verwaltungsbegriffe, regionale Varianten, lateinische bzw. fremdsprachige Entsprechungen und angrenzende Begriffe verwaltet.

Beispiel für historische Gewässer- und Nutzungsforschung: Teich, Weiher, Hälter, Fischbehälter, Wasser, Lache, Sumpf, Bruch, Ried, Moor, Graben, Mühlgraben, Wehr, Damm, Teichstatt, Teichwiese, Hutung, Trift, Gemeinheit, Anger, Holz, Gehölz, Forst, Schlag, Grenze, Rain, Malbaum, Flur, Hufe, Vorwerk.

### Search Expansion

Suchstrategien werden versioniert und aus Begriffsfamilien zusammengesetzt. Suchläufe werden mit Datum, Katalog/Archiv/Datenbank, Query und Ergebnisumfang gespeichert.

### Citation Chaining

Backward und Forward Citation Chaining sowie bibliographische Kopplung helfen, Forschungsschulen, Standardwerke und isolierte Literaturcluster zu erkennen.

### Quellen- und Evidenztypisierung

Der Assistent unterscheidet mindestens:

- archivalische Primärquelle,
- historische Karte/Riss,
- Urkunde,
- Amtsbuch/Rechnung/Register,
- Flurbuch/Kataster,
- Chronik/Beschreibung,
- archäologischer Befund,
- naturwissenschaftliche Messung,
- Modellierung,
- Sekundärliteratur,
- Review,
- unbelegte Traditionsaussage.

### Methodenspezifische Qualitätsprüfung

Es gibt keine universelle Evidenzhierarchie. Eine historische Karte wird nach Entstehungszweck, Maßstab, Vermessungspraxis, Generalisierung und Provenienz beurteilt; eine archivalische Beschreibung nach Überlieferungskontext und Interessenlage; naturwissenschaftliche Daten nach Messdesign und Unsicherheit. Die Qualitätsprüfung erfolgt innerhalb des jeweiligen Evidenztyps.

### Kontestationsanalyse

Widersprüche werden nicht automatisch „aufgelöst“. Der Assistent klassifiziert mögliche Ursachen:

- unterschiedliche Definitionen,
- unterschiedliche Zeitpunkte,
- unterschiedliche räumliche Skalen,
- verschiedene Quellengattungen,
- abweichende Methoden,
- tatsächlicher empirischer Widerspruch,
- Tradierung eines Fehlers.

### Synthese

Synthesen unterscheiden zwischen:

1. innerhalb einer Forschungstradition gut gestützten Aussagen,
2. traditionsübergreifend konvergierenden Aussagen,
3. plausiblen, aber indirekten Rekonstruktionen,
4. offenen Kontroversen,
5. echten Forschungslücken.

## Git als Forschungsprovenienz

Git sollte nicht primär als Speicher für PDFs verstanden werden, sondern als Provenienzsystem für den Forschungsprozess. Änderungen an Forschungsfragen, Begriffen, Suchstrategien, Bewertungen und Synthesen werden versioniert.

Vorgeschlagene Struktur:

```text
research/
├── questions/
├── concepts/
├── traditions/
├── search/
│   ├── queries/
│   └── runs/
├── corpus/
├── sources/
├── claims/
├── evidence/
├── contradictions/
├── places/
├── chronology/
├── synthesis/
└── decisions/
```

Zusätzlich:

```text
docs/
├── research-design/
├── methods/
└── source-guides/
```

## Epistemic Literature Graph

Kernobjekte:

```text
ResearchQuestion
  ├── Subquestion
  ├── Concept
  ├── Place
  ├── TimeRange
  └── ResearchTradition

ResearchTradition
  ├── Concept
  ├── Theory
  ├── Method
  └── QualityCriterion

Claim
  ├── asserted_by -> Source
  ├── supported_by -> Evidence
  ├── contradicts -> Claim
  ├── applies_to -> Place
  ├── applies_to -> TimeRange
  └── derived_into -> Synthesis
```

## Spezifische Relevanz für Pflege Arnshaugk

Für die historische Landschafts- und Raumanalyse sollte der Assistent nicht nur wissenschaftliche Literatur, sondern auch archivalische Quellengattungen aktiv erschließen. Besonders relevant sind:

- Forst-, Flur-, Hutungs- und Grenzrisse,
- Jagd- und Forstkarten,
- Guts- und Rittergutsvermessungen,
- Teich- und Wasserrechtsakten,
- Grenzstreitigkeiten,
- Hutungs- und Triftstreitigkeiten,
- Gemeinheitsteilungen,
- Flurbereinigungs- und Separationsunterlagen,
- Kataster- und Flurbücher,
- Lehnsakten und Besitzregister,
- Amtsrechnungen,
- Fischerei- und Teichrechnungen,
- Mühlenakten,
- Wasserbauakten,
- Orts- und Landesbeschreibungen,
- ältere topographische Karten und Meilenblätter,
- historische Luftbilder,
- Geländemodelle und LiDAR als moderne Vergleichsebene.

Für jede Quellengattung sollte eine eigene Suchterminologie hinterlegt werden, da Archive diese Bestände häufig nicht nach heutigen Sachbegriffen erschließen.

## Assistenzfragen, die das System beantworten sollte

- Welche Literaturcluster habe ich mit meiner bisherigen Terminologie wahrscheinlich übersehen?
- Welche historischen Begriffe könnten denselben Gegenstand bezeichnen?
- Welche Aussagen beruhen nur auf Sekundärliteratur?
- Welche Primärquelle wird immer wieder zitiert, ohne neu geprüft zu werden?
- Wo widersprechen sich Quellen tatsächlich und wo nur scheinbar?
- Welche Forschungstraditionen betrachten denselben Raum mit unterschiedlichen Methoden?
- Welche räumlichen und zeitlichen Gültigkeitsbereiche werden in einer Aussage vermischt?
- Wo existieren nur Kartennachweise, aber keine schriftlichen Belege – oder umgekehrt?
- Welche Schlussfolgerungen hängen an einer einzigen Quelle?
- Welche offenen Fragen sind echte Evidenzlücken und welche bloß Suchlücken?

## Technische Bausteine

Bestehende Open-Source-Komponenten können integriert oder als Vorbild genutzt werden:

- OpenAlex als offener scholarly graph,
- ASReview für Human-in-the-loop Screening,
- litsearchr für Suchbegriffsexpansion,
- revtools für Review-Workflows,
- Open Knowledge Maps/Headstart für explorative Wissenskarten,
- Citation-Network-Werkzeuge für Forward-/Backward-Chaining.

Die eigentliche Innovation für dieses Projekt ist jedoch die methodologische Schicht darüber: Traditionsmodellierung, Begriffsgeschichte, Quellenkritik, Claim–Evidence-Provenienz, Kontestationsanalyse und reflexive Synthese.

## MVP

Ein erster MVP sollte fünf Dinge zuverlässig können:

1. Forschungsfragen und Unterfragen versioniert verwalten.
2. Begriffe und historische Synonyme als kontrolliertes, erweiterbares Vokabular führen.
3. Quellen/Literatur mit Provenienz und Fundstellen erfassen.
4. Atomare Claims mit Evidenz, Ort, Zeit und Unsicherheit verknüpfen.
5. Offene Widersprüche, Suchlücken und Forschungsentscheidungen sichtbar machen.

## Leitprinzipien

- Human-in-the-loop statt vollautomatischer Review.
- Quellenbeleg vor generierter Zusammenfassung.
- Unsicherheit explizit statt implizit.
- Keine universelle Evidenzhierarchie.
- Historische Terminologie als eigenes Forschungsobjekt.
- Raum und Zeit als First-Class-Entities.
- Jede Synthese muss auf Claims und Quellen rückführbar sein.
- Git-Commits dokumentieren Änderungen des Forschungsstands und der Forschungsentscheidungen.

## Nächste Umsetzungsschritte

1. Datenmodell für Question, Concept, Tradition, Source, Claim, Evidence, Place und TimeRange definieren.
2. YAML/JSON-Schemas für die Kernobjekte anlegen.
3. kontrolliertes Vokabular für die ersten Forschungsfragen aufbauen.
4. Archiv- und Literatur-Suchprotokoll definieren.
5. Claim–Evidence-Workflow an einem konkreten Fall (z. B. historische Teiche/Gewässerstrukturen) testen.
6. danach automatisierte Hilfen für Query Expansion, Citation Chaining und Widerspruchserkennung ergänzen.
