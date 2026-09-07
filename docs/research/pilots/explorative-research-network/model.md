# Arbeitsmodell – gemeinsamer Forschungszustand + modulare Fragen

## 1. Leitidee

Der Pilot behandelt Forschungsarbeit als **dynamisches Netz aus Material, Evidenz, Fragen, Relationen, Findings und Views**. Die Ordnung darf sich ändern; epistemische Identität und Provenienz sollen stabil bleiben.

Die Forschungsfrage ist eine **Linse / Arbeitsmodul**, kein Evidenzcontainer.

## 2. Ebenen

### A. Corpus / Material State
Was liegt vor oder ist als relevant identifiziert?

Beispiele: Publikation, Archivquelle, Edition, Digitalisat, Foto, Museumslabel, Karte, Objektaufnahme, Feldbeobachtung, Baustellendokumentation, älterer Forschungsbericht.

Diese Ebene sagt noch nicht, welchen wissenschaftlichen Schluss das Material trägt.

### B. Evidence / Research State
Was wurde aus einer konkreten Instanz beobachtet oder mit benannter Methode als Befund gestützt?

Mindestens getrennt halten:

`source/representation → observation → finding → interpretation/claim → hypothesis → synthesis/view`

Spätere Ebenen dürfen frühere nicht umschreiben.

### C. Research Modules
Ein Research Module ist ein temporärer, nachvollziehbarer Zuschnitt auf den gemeinsamen Forschungszustand.

Minimaler Candidate-Record:

- `id`
- `question`
- `scope` – räumlich, zeitlich, sachlich; Search Boundary falls relevant
- `trigger_refs` – welches Material/Problem ließ die Frage entstehen?
- `input_refs` – verwendete Quellen/Observations/Findings
- `leading_competence`
- `controlling_competences`
- `method_status` – validated profile | working-method | specialist-needed
- `inference_limits`
- `status` – open | working | answered | reframed | superseded | deferred
- `outputs` – Findings/Hypothesen/Unresolved/New Questions
- `relations_to_questions`

Das ist **kein vorgeschlagenes generisches Datenmodell**, sondern eine Pilot-Checkliste für Restartability.

### D. Relations
Relationen müssen ihren epistemischen Typ behalten. Eine Relation darf nicht aus gemeinsamer Darstellung oder Ko-Lokalität implizit historisiert werden.

Mindestens unterscheiden:

1. **Source/Transmission Relations** – Reproduktion von, Edition von, zitiert, abgeleitet aus.
2. **Material/Collection Relations** – gleiche Vitrine, gleiche Sammlung, gleiche Fundstelle, gleiche Grabung.
3. **Spatial/Temporal Relations** – gleicher Raum, Nähe, Überlappung, zeitliche Folge; noch keine Kausalbeziehung.
4. **Historical Relations** – Akteurs-, Funktions-, Besitz-, Nutzungs-, Ereignisrelationen; Evidenz erforderlich.
5. **Research Relations** – supports, challenges, compares-with, relevant-to-question, possible-analogy.
6. **Question Relations** – split-from, fused-from, reframes, supersedes, depends-on, discriminates-between.

Working vocabulary darf im Pilot angepasst werden; keine Relationstaxonomie wird durch diese Datei auf `main` promoted.

### E. Views / Synthesen
Views sind **Projektionen** über Research State, keine neuen Truth Stores.

Beispiele:

- Site-Dossier Ranis
- Orlatal-Paläolithikum
- Chronologie
- räumliche Fundstellenansicht
- Forschungsgeschichte
- Bauphasen-/Torhausansicht
- Provenienz-/Source-Graph
- offene Widersprüche

Eine View muss auf kanonische Referenzen zurückführen können und rebuildable sein.

## 3. Question Operations

Fragen dürfen sich verändern, ohne den zugrunde liegenden Research State zu verlieren.

- `split` – eine zu breite Frage wird in diskriminierende Teilfragen zerlegt.
- `fuse` – getrennte Fragen erweisen sich als ein gemeinsames Problem.
- `reframe` – Problemformulierung ändert sich aufgrund neuer Evidenz oder Methodik.
- `supersede` – eine frühere Frage wird durch eine präzisere ersetzt; historische Spur bleibt.
- `defer` – sinnvoll, aber aktuell nicht bearbeitbar.
- `reject` – falsche Voraussetzung/ungeeigneter Zuschnitt.

Bei jeder Operation soll nachvollziehbar bleiben: **warum**, auf Basis welcher neuen Beobachtung/Finding/Methodenprüfung und mit welchem Effekt auf Scope/Inputs.

## 4. Kompetenzen

Kompetenz wird **pro Research Module** geroutet.

Beispiele:

- Zechsteinriff/Höhlenentstehung → Geologie/Geomorphologie/Karst; Geoarchäologie kontrollierend je Frage.
- Ranis/Kniegrotte → Prähistorische Archäologie; ggf. Taphonomie, Zooarchäologie, Archäogenetik, Isotope als methodenspezifische Kompetenzen.
- Burg/Torhaus → Mittelalterarchäologie, Bauforschung/Bauarchäologie, Denkmalpflege/Restaurierung.
- Börner/Sage → historische Philologie, Wissenschaftsgeschichte, Erzählforschung je konkretem Claim.
- Museumsbeschriftung → Sammlungs-/Museumsgeschichte; historische Aussage des Labels ist zunächst Ausstellungsbefund, nicht aktueller Fachkonsens.

`leading` bedeutet methodische Führung für die konkrete Frage, nicht epistemische Oberhoheit über den Gesamtbestand.

## 5. Invarianten

1. **Source identity first** – konkrete Quelle/Instanz/Überlieferungsstufe bleibt unterscheidbar.
2. **One fact / one canonical home** – Module und Views referenzieren; sie duplizieren keine Wahrheit.
3. **Observation is not interpretation** – sichtbares/lesbares Material bleibt von Einordnung getrennt.
4. **Co-location is not continuity** – gleiche Landschaft/Fundkarte/Vitrine begründet keine historische Beziehung.
5. **Persistence is not promotion** – Pilot-State bleibt Candidate, bis Authority entscheidet.
6. **Question is not ontology** – Research Questions schneiden Arbeit; sie definieren nicht die Weltstruktur.
7. **Synthesis is reversible-by-reference** – jede Synthese bleibt auf Details/Evidenz rückführbar.
8. **Unresolved is valid** – Widerspruch, Mehrdeutigkeit und offene Provenienz dürfen bestehen bleiben.
9. **Scale shift requires justification** – Objekt→Fundstelle→Ranis→Orlatal→Region ist ein analytischer Schritt, keine automatische Kontextakkumulation.
10. **Method truth is external to prompt** – Fachmethode folgt #60/#45 und SOTA, nicht dem sprachlichen Modell.

## 6. Was dieser Pilot ausdrücklich nicht entscheidet

- technische Speicherungform;
- Graphdatenbank vs. Dateien vs. anderes Backend;
- universelle Ontologie;
- finale Relationstaxonomie;
- UI;
- neue accepted Requirements;
- neue historische Findings.

Diese Entscheidungen dürfen erst aus beobachteter Friktion und Review entstehen.
