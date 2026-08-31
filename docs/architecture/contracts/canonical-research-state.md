# Histo-Orla – Canonical Research State / Identity Contract

**Status:** `working-architecture / v0.1`  
**Work Owner:** #50  
**Parent:** #48 Architecture Execution Control  
**Inputs:** #42, #43, #45, `docs/research/source-identity-protocol.md`, #3/#49, #31/#35/#38/#39/#40, #60/#61  
**Scope:** case-unabhängiger Architekturvertrag; keine Datenbank- oder Frameworkentscheidung.

## 1. Zweck

Dieses Artefakt übersetzt die bereits validierten wissenschaftlichen Source-/Provenienz-/Research-State-Invarianten in einen **technologieunabhängigen Architekturvertrag**. Es definiert, welche Identitäten und Zustandsgrenzen Histo-Orla unabhängig von Zotero, OneDrive, OCR/HTR-Engine, Search-Index, AI-Provider und konkretem historischen Case erhalten muss.

Es ist ausdrücklich **kein physisches Datenbankschema** und keine Festlegung auf SQL, Graph, JSON/YAML, Files oder einen bestimmten Stack.

## 2. Verbindliche Trennung der Identitätsebenen

Aus #42 und dem bindenden Source-Identity-Protokoll folgt mindestens:

```text
Source / Work / Archival Unit
→ Representation / Edition / Regest / Reproduction
→ Digital or Physical Instance actually used
→ Derivative / OCR / HTR / Transcription / Normalization
→ Findspot / Excerpt / Observation
→ Finding
→ Claim / Interpretation / Synthesis
```

Keine Ebene darf durch Convenience still eine andere Ebene ersetzen.

### 2.1 Source Identity

Beschreibt die bibliographische bzw. archivalische Identität des Werkes, Records oder Überlieferungsträgers.

Mögliche externe Referenzen: Archivsignatur, DOI, URN, ARK, Handle, PURL, bibliographische Werk-ID, Zotero Item Key.

**Invariante:** Externer Identifier oder Zotero-Key kann referenziert werden, ist aber nicht automatisch Histo-Orlas interne kanonische Identität.

### 2.2 Representation

Edition, Regest, Katalogrecord, Digitalisat oder andere Repräsentation einer Source.

**Invariante:** `Regest != Urkunde`, `Katalogrecord != inspizierte Quelle`, `Edition != Original`.

### 2.3 Inspected Instance

Die konkrete digitale oder physische Instanz, auf die eine Forschungsbeobachtung tatsächlich zurückgeht.

Mindestens muss rekonstruierbar sein:

- welche Repräsentation/Source sie instanziiert;
- welcher Inspection Status vorlag;
- welche externen Locator/Identifier damals bekannt waren;
- bei lokalen/remote Bytes: welche Version/Hash-Information vorhanden war;
- wann sie für consequential research relevant inspiziert wurde.

**Invariante:** Dateipfad, URL oder Cloud-Locator allein ist keine dauerhafte Instance Identity.

### 2.4 Derivative

OCR, HTR, Textlayer, Transkription, Korrektur, Normalisierung, Layout-/Page-Extrakt, Index oder anderer Verarbeitungsoutput.

**Invarianten:**

- Parentage muss erhalten bleiben;
- Processor/Version/Parameter müssen proportional zur Konsequenz rekonstruierbar sein;
- Original-/Inspection-Status wird nicht geerbt;
- regenerierbare Derivate dürfen vom kuratierten Research State getrennt werden.

### 2.5 Findspot / Excerpt / Observation

Fundstelle verbindet einen Research-Befund mit der präzisesten verfügbaren Stelle der verwendeten Instanz/Repräsentation.

Mögliche Koordinaten:

- Seite / Folio / Urkunden- oder Regestnummer;
- Zeile / Abschnitt;
- Scan-/Viewer-Seite;
- Region/Bounding Box bei Layoutquellen;
- stabiler Canvas-/Image-Link, soweit vorhanden.

**Invariante:** Fundstelle muss den Round-trip zur tatsächlich verwendeten Instanz ermöglichen, soweit das Quellmedium dies zulässt.

### 2.6 Finding / Claim / Interpretation

Diese Ebenen gehören zum wissenschaftlichen Research State und nicht zu Zotero, OneDrive oder dem Search-Index.

**Invarianten:**

- AI output ist keine Evidenz;
- Finding verweist auf Source/Excerpt-Provenienz;
- unresolved / disputed / hypothesis sind legitime Zustände;
- editorische oder analystische Normalisierung überschreibt Beobachtung nicht;
- Promotion in consequential state erfolgt kontrolliert.

## 3. Externe Systeme: Rollen statt Ownership

### Zotero

Rolle: bevorzugte bibliographische/archivische Verwaltungs- und Referenzschicht.

Kann liefern:
- Item-/Attachment Keys;
- bibliographische Metadaten;
- Collections/Tags/Notes;
- Attachment-Referenzen;
- ggf. indexierten Volltext als Derivat-/Retrieval-Input.

Darf nicht allein besitzen:
- inspected-instance truth;
- Findings/Claims/Discrepancies;
- wissenschaftlichen Validation State.

### OneDrive

Rolle: Source of Bytes / physischer Dateiablage- und Sync-Dienst nach Owner Constraint.

Kann liefern:
- Dateibytes;
- Locator/Pfad;
- driveItem-/Version-/eTag-ähnliche Provider-Metadaten;
- Change Tracking.

Darf nicht allein besitzen:
- bibliographische Source Identity;
- wissenschaftliche Instance Identity;
- Research State.

### Git/GitHub

Rolle: versioniertes Projekt-/Research-/Architecture-Gedächtnis gemäß §14.

Nicht automatisch Speicher für alle Quellbytes, OCR-Volltexte oder regenerierbare Indizes.

## 4. Interne Identifier – vorläufiger Contract

Histo-Orla benötigt providerunabhängige interne Identitäten mindestens für:

```text
source_id
digital_or_physical_instance_id
derivative_id
excerpt_id
finding_id
```

Weitere IDs (claim, entity, relation, discrepancy, processing run, method profile/application, work order, handoff/review) werden nur aufgenommen, wenn die jeweiligen Architekturpakete dies benötigen.

### Regeln

1. IDs sind opaque/stabil und enthalten keine fachliche Wahrheit im Identifier selbst.
2. Externe IDs werden als Referenzen/Locators geführt, nicht in die interne ID eingebrannt.
3. Rename/Move einer Datei ändert nicht automatisch Source Identity.
4. Byteänderung unter demselben Locator muss als Änderung erkannt werden und darf eine früher inspizierte Instance nicht still überschreiben.
5. Merge/Split von Source-/Entity-Identitäten braucht nachvollziehbare Promotion/Correction-Provenienz.

## 5. Canonical vs. Regenerable State

### Canonical / curated

Mindestens:
- interne Identitäten und ihre Beziehungen;
- bibliographische/archivalische Kernidentität soweit kuratiert;
- Inspection Status;
- relevante externe Identifier/Locators mit Provenienz;
- Findspots/Excerpts;
- Findings/Claims/Discrepancies/Validation State;
- relevante Rights-/Processing-Admissibility-Information;
- consequential Processing Provenance, soweit notwendig;
- für consequential Research die methodische/arbeitsbezogene Provenienz, die #61 als notwendig bestätigt (insbesondere Work Owner/Scope, angewandtes Domain Method Profile samt Version/Status, Method Application und Review-/Validation-Bezug).

### Regenerable / cache/index

Kandidaten:
- Suchindex;
- Embeddings;
- temporäre Downloads;
- derived thumbnails;
- rekonstruierbare OCR-Zwischenformate;
- API caches;
- aus kanonischem Work-/Method-State erneut erzeugbare Prompt-/Context-Pakete.

**Regel:** Verlust regenerierbarer Schichten darf den kuratierten Forschungszustand nicht epistemisch zerstören.

## 6. State-/Promotion-Grenzen

Mindestens folgende Zustände müssen unabhängig vom konkreten Case darstellbar sein:

```text
candidate
working / inspected
validated / promoted proportional to consequence
rejected / superseded / demoted
unresolved
external-validation-required
```

Nicht jede Objektklasse braucht exakt dieselbe State Machine. Der gemeinsame Contract lautet:

- Generative/spezialisierte Verfahren können Candidates erzeugen;
- deterministisch prüfbare Invarianten werden softwareseitig geprüft;
- wissenschaftliche Promotion folgt Fachmethode und Konsequenz;
- unabhängige Fachvalidierung ist explizit von AI-/Internal Review getrennt;
- Correction/Demotion zerstört die Research History nicht.

Für Domain Method Profiles gilt zusätzlich die unter #60 definierte fachliche Statusfolge `scoping → method-candidate → working-method → validated-method | deprecated/revised`. Die technische Transition Enforcement gehört #54/#61 und darf den fachlichen Promotionsentscheid nicht selbst erfinden.

## 7. Rights / Processing Admission Contract

Ein Source-/Instance-Record muss externe Verarbeitung grundsätzlich von der bloßen Existenz der Datei trennen können.

Mindestens separat prüfbar:

```text
access
copy / local retention
TDM / computational processing
external/cloud processing
publication / sharing
privacy / personal-data constraint
```

`unknown` ist ein gültiger Zustand. External processing kann bei `restricted/unknown` blockiert werden, ohne lokale Lesbarkeit des Research State zu verhindern.

## 8. Adapter Contract

Externe Systeme werden hinter austauschbaren Ports/Adaptern betrachtet.

Mindestens erwartete abstrakte Operationen:

### Bibliographic adapter
- resolve external item reference
- read metadata
- list attachments
- read/update selected metadata only after authorization

### Byte/source adapter
- resolve locator/provider ID
- read bytes or expose local file safely
- return provider version/change metadata
- detect unavailable/changed source

### Processor adapter
- accept admitted instance/derivative
- produce versioned derivative + processing metadata
- no canonical mutation outside promotion boundary

### Search adapter
- exact/filter baseline without LLM
- reproducible query/log parameters
- return source/derivative/findspot references

Die konkrete API/Programmiersprache bleibt offen.

## 9. Case-unabhängige Acceptance Tests

Diese Tests können mit synthetischen Fixtures oder beliebigen Quellenobjekten entwickelt werden; reale U1–U4-Fälle bleiben spätere Falsifikation.

1. **Layer separation:** Regest kann nicht als Original-Instanz promoted werden.
2. **Locator independence:** Rename/Move eines Locators ändert interne Source ID nicht.
3. **Byte mutation:** gleicher Locator + geänderte Bytes erzeugt Change/Version-Ereignis statt stiller Überschreibung.
4. **Derivative parentage:** OCR ohne Parent Instance ist ungültig.
5. **Findspot round-trip:** Excerpt verweist eindeutig auf Instance/Derivative + Seitenkoordinate.
6. **AI non-evidence:** AI Candidate kann ohne Evidenzlink keinen evidenziellen Status erhalten.
7. **Provider removal:** Entfernen von Zotero/OneDrive-/AI-Adapter lässt kuratierten State lesbar/exportierbar.
8. **Rights guard:** external processing wird bei unbekannt/restricted blockierbar.
9. **Research history:** Demotion/Supersession löscht frühere Provenienz nicht.
10. **Unknown preservation:** fehlende Metadaten bleiben `not yet verified/unknown`, nicht erfunden.
11. **Method traceability:** consequential Finding/Claim kann auf Work Order/Scope + angewandtes Method Profile/Version/Status + Method Application + Review/Validation zurückgeführt werden.
12. **Method-status guard:** `method-candidate` darf exploratory Output erzeugen, aber keinen consequential-validierten Status vortäuschen.
13. **Handoff traceability:** materieller Domain→Requirements→Dev- oder Dev→Domain-Handoff verliert Established/Unresolved/Evidence/Non-goals/Return Condition nicht.
14. **Prompt non-authority:** Verlust/Änderung des ursprünglichen Prompts zerstört weder Method Truth noch die rekonstruierbare Method Application.
15. **Fresh-context method resume:** neuer autorisierter Context kann aus kuratiertem State seine Aufgabe, Authority Boundary, anwendbare Methode und nächste Aktion ohne alten Chat bestimmen.

## 10. Architekturfragen, die weiterhin offen bleiben

Diese Fragen sind absichtlich **nicht** durch diesen Contract entschieden:

- Datei-/SQL-/Dokument-/Graph-Persistenz;
- SQLite/FTS, PostgreSQL, Search Engine oder andere konkrete Produkte;
- Serialisierungsformat;
- UI;
- Event Sourcing vs. Snapshot/History-Modell;
- konkrete Repräsentation von Method Profile / Work Order / Method Application / Handoff;
- JSON Schema / eigene Validatorlogik / Policy-as-Code / andere Enforcement-Technik;
- PROV/RO-Crate als internes Modell vs. Export-/Interchange-Schicht;
- Zotero Web vs. Local API als primärer Laufzeitpfad;
- OneDrive Graph vs. lokale Sync-Bridge;
- konkrete Hash-/Versionierungsstrategie;
- OCR-/HTR-Engine;
- semantische Suche/RAG;
- Multi-Agent.

Diese werden durch #48/#49/#61 und spätere reversible Spikes diskriminiert.

## 11. Aktuelle Konsequenz für #48/#49

Das bindende `docs/research/source-identity-protocol.md` reduziert die Unsicherheit von P0-A erheblich: die wissenschaftliche Identitäts-/Provenienztrennung muss nicht aus dem Live-Case neu erfunden werden.

#49 muss deshalb nicht definieren, **was** Source/Instance/Derivative/Findspot wissenschaftlich bedeuten. Es muss empirisch prüfen, wie Zotero-/OneDrive-Identifier, Pfade, Bytes und Versionen auf diesen unabhängigen Contract abgebildet werden können.

Der erste End-to-End-Case-Slice bleibt notwendig, um zu falsifizieren, ob der Contract in realer Forschung vollständig genug ist.

## 12. Method-/Work-Context-/Review-Provenienz – neue explizite Contract-Grenze

Aus `REQ-EPI-001`, `REQ-WF-001`, `REQ-UX-001`, `REQ-VAL-001/002`, `REQ-STATE-001`, #60 und #61 folgt für consequential Research eine zusätzliche Trennung:

```text
Domain Method Profile
= fachlich begründete, versionierte operative Methode

Work Order / Work Context
= konkrete Aufgabe, Scope, Owner, Authority-/Handoff-Grenze

Method Application
= tatsächliche Anwendung eines konkreten Method Profiles auf einen Work Order/Fall

Evidence / Observation / Finding / Claim
= wissenschaftlicher Inhalt mit Source-/Findspot-Provenienz

Review / Validation
= eigener Vorgang mit Validation Level / Reviewer-Klasse / Ergebnis

Prompt / Model / Tool Run
= austauschbarer Ausführungs-/Processing-Kontext; technische Provenienz, keine Method Truth
```

### 12.1 Minimale Relationsinvarianten

Für consequential Research muss rekonstruierbar sein:

- welcher Work Owner / Scope galt;
- welche führenden/controlling Domänen galten;
- welches Domain Method Profile in welcher Version/Statusstufe angewandt wurde;
- welche konkrete Method Application die Evidenz/Findings erzeugte oder prüfte;
- welche Source/Instance/Findspots tatsächlich zugrunde lagen;
- welcher Review-/Validation-Status erreicht wurde;
- welche Unsicherheiten/Alternativen offen blieben;
- welcher Statusübergang anschließend stattfand und wodurch er autorisiert war.

Nicht jeder Explorationsschritt benötigt dieselbe Provenienztiefe. Die Pflicht skaliert mit consequentiality gemäß #45/#42.

### 12.2 Fail-closed Promotion, nicht fail-closed Exploration

Der Contract darf offene Forschung nicht durch fehlende Formalisierung verhindern.

Zulässig:

```text
kein working-method vorhanden
→ exploratory / candidate Research möglich
→ Method Debt / Profile Research unter #60 sichtbar
```

Nicht zulässig:

```text
kein hinreichender Method-/Evidence-/Validation-Bezug
→ Modell erzeugt plausible Synthese
→ consequential / validated Promotion
```

Formal prüfbare Promotionsvoraussetzungen gehören #54/#61. Fachliche Suffizienz/Interpretation bleibt Domain-/Review-Judgement.

### 12.3 Provenance-/Interchange-Referenzrahmen

#61 prüft als State-of-the-Art-/Best-Practice-Referenzen insbesondere:

- W3C PROV für Entity/Activity/Agent sowie Ableitungs-/Revisions-/Attributionsprovenienz;
- RO-Crate / Workflow Run RO-Crate für portable Research Objects und Ausführungsprovenienz;
- schema-/contract-basierte Validierung für strukturelle Completeness/Referenzintegrität;
- Policy-/Transition-Enforcement als Pattern zur Trennung von Regeldefinition und Ausführung.

Der Contract verpflichtet **nicht** auf RDF, RO-Crate, OPA, JSON Schema oder eine Workflow Engine. Der kleinste hinreichende Mechanismus ist empirisch zu wählen.
