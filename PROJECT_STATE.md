# Histo-Orla – Project State / Handoff

**Status:** active handoff snapshot  
**Stand:** 2026-09-23  
**State Owner:** #1; Governance #9/#23  
**Arbeitsregel:** `AGENTS.md` zuerst lesen.

> Diese Datei ist die zentrale Navigations-/Handoff-Sicht. Kanonische Detailwahrheit liegt in Requirements-, Research-, Method-, Architecture- und Development-Artefakten.

## 1. Aktueller Projektmodus

Histo-Orla ist ein privates, leanes und agiles Forschungssystem.

`MVP` wird **nicht mehr als kanonische Projektphase oder zusätzliche Requirement-Schicht verwendet**.

### Aktuelle strukturelle Review-/Audit-Inputs

- **#64 / PR #125** – die wiederholten Systemanalysen sind punktweise reconciliiert. Frühere Sammeldiagnosen wurden gesplittet/abgeschwächt; insbesondere sind Loss-Boundary-Formalisierung und Readiness/Admission eigenständige positive bzw. separate Mechanismen. PR #125 ist die aktuelle Dispositionssicht, nicht neue Requirement-/Architecture-Authority.
- **#92 / PR #94** – die bestehende Architecture/Product-Re-Baseline bleibt Prior Art / frühere Lösungshypothese. `Research Reconciliation = COMPLETE`; `Rebuild Re-entry = READY`; die Fresh Rebuild Conception ist abgeschlossen. WP1 `Canonical Research State Spine v0 + derived audit roundtrip` ist über PR #132 als bounded Increment **IMPLEMENTED + TECHNICALLY VERIFIED**; `IMP-STATE-SPINE-001` ist verified. Owner-/Workflow-Nutzen bleibt separat offen. `selection-open` bleibt unverändert; kein WP2/WP3/WP4/WP5 ist dadurch admitted.

### Aktuelles Analysis→Research→Rebuild Gate

Für den aktuell untersuchten Umbau gilt verbindlich die Reihenfolge:

```text
Systemanalyse / aktuelle Findings
→ problemgetriebener Deep Research
→ Reconciliation je Finding
   strengthen | weaken | split | reframe | falsify | unresolved
→ erst dann neue Umbaukonzeption unter #48/#42/#59
→ Implementation nur nach expliziter Selection / Admission
```

**Historischer Pre-Reconciliation-Stand (vor D4; nicht mehr aktiv):**

Bis zum Abschluss der Research-Reconciliation galt:

- #92 war `hold-for-research-reconciliation`;
- die bestehende Roadmap und PR #119 waren bereits **Prior Art / Planungshypothesen**, nicht Default-Next-Action;
- kein Shared Runtime/Product Package, Read Model, Skill/MCP/UI, Owner-/Handoff-Redesign oder fixes Research-Workflow-Modell wird aus der alten Roadmap weitergezogen;
- bereits etablierte Loss-Boundaries und settled Invariants (#50/#51, Source/Instance/Derivative/Findspot, `unresolved`, Readiness/Admission) bleiben gültig;
- eigenständig Requirement-backed technische Arbeit ist dadurch nicht verboten, benötigt aber weiterhin explizite Auswahl und darf nicht als „Umbaufortsetzung“ interpretiert werden.

Detailbegründung: `docs/architecture/assurance/repeated-system-audits-project-implications-20260922.md` / PR #125. Der vorbereitete Research-Handoff liegt in `docs/research/audits/problem-driven-deep-research-prompt-20260922.md`.

Der externe Research-Lauf D4 ist als `docs/research/audits/d4-problem-driven-external-research-20260922.md` persistiert. Seine punktweise projektseitige Disposition und Gate-Entscheidung liegt in `docs/architecture/assurance/d4-project-reconciliation-rebuild-reentry-20260923.md`: `Research Reconciliation = COMPLETE`, `Rebuild Re-entry = READY`. PR #125 und #126 sind in `main` integriert; `REPO-INTEGRATION-PENDING` ist nicht mehr aktiv. Diese Entscheidung ist keine Architecture-/Implementation-Authority und reaktiviert R4–R8 nicht.

Die daraus frisch abgeleitete Zielkonzeption liegt in `docs/architecture/fresh-rebuild-conception-20260923.md`. Der erste Kandidat WP1 ist inzwischen bounded implementiert und technisch verifiziert: minimale Identity/Role/`canonical_ref`-Registry, read-only Resolver, realer #51/#46→#55-Audit-Roundtrip ohne manuell assemblierte zweite Real-State-Projektion sowie AT-01..AT-10/NT-01..NT-10. Das verifiziert nur den Coverage Ceiling von WP1; Provider Availability, Retrieval, Workplace/UI, Method/Promotion und Owner-Akzeptanz bleiben offen.

Verbindlich gilt:

- die gesamte bereits akzeptierte Requirements-/Quality-/Governance-Basis bleibt aktiv;
- Live-/Domain-Research und reale Owner-/Nutzererfahrung präzisieren und ergänzen diese Requirements;
- Lean/Agile optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value, nicht den Anspruch;
- State of the Art und Best Practice sind Basis wissenschaftlicher und technischer Entscheidungen;
- technische Umsetzung läuft parallel, sobald ein Requirement-/Constraint-Cluster hinreichend klar ist, ersetzt aber nicht die fachliche Arbeit;
- formal geklärte Requirements-, Governance- und Traceability-Regeln werden deterministisch geprüft statt dauerhaft nur Prompt-/Chat-Compliance zu bleiben;
- technische Arbeit bleibt bis zu Goals/Needs/Pains bzw. expliziten Constraints rückführbar; reale Nutzung/Owner-Feedback schließt die Delivery-Schleife;
- externe Pilot-/Prior-Art-Befunde sind Review Input und erhalten erst nach Histo-Orla-eigener Authority-/Lifecycle-Disposition Requirement-, Method- oder Implementation Authority.

Kanonisch:

- `docs/research/discovery/problem-baseline.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`
- `docs/architecture/requirements-derivation.md`
- `docs/architecture/fresh-rebuild-conception-work-context-20260923.md`
- `docs/architecture/fresh-rebuild-conception-20260923.md`
- `docs/development/canonical-research-state-spine-v0-implementation-admission-20260923.md`
- `docs/architecture/rebaseline-roadmap.md`
- `docs/architecture/operational-execution-architecture.md`
- `docs/architecture/prior-art-development-inputs.md`
- `docs/architecture/assurance/work-selection-reconciliation-20260910.md`
- `docs/architecture/assurance/requirements-assurance-harness.md`
- `docs/architecture/assurance/value-decision-delivery-assurance.md`
- `docs/architecture/assurance/d4-project-reconciliation-rebuild-reentry-20260923.md`
- `docs/architecture/assurance/chat-closure-knowledge-monopoly-audit-20260923.md`
- `docs/governance/lean-agile-non-regression.md`
- `docs/development/requirements-coverage.md`
- `docs/research/synthesis/phase-reconciliation.md`

Aktueller Arbeitsfluss:

```text
Goals / Needs / Pains / reale Research-Friktion (#28, #46/#47, Owner Feedback)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↕
Accepted Requirements + Extensions (#42)
        ↕
Requirement Structure / Authority / Dependencies (#42)
        ↕
Deterministic Requirements QA (#62)
        ↕
Technical Derivation: Concerns / SOTA / Options (#48)
        ↓
Decision / Implementation Trace gegen Requirements + G/N/P + Governance (#63)
        ↓
Development & Verification (#59)
        ↓
reale Nutzung / Owner-Feedback (#63)
        ↺
Pain bestätigt | Pain bleibt | Regression | neuer Need | Requirement-/Method-/Decision-Delta
```

## 2. Requirements / Non-Regression

Aktive Systemanforderungen bestehen mindestens aus:

1. 39 accepted Requirements/Constraints in `requirements-baseline.md`;
2. 14 accepted Extensions aus `requirements-extensions.md`;
3. bindenden Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints;
4. späteren explizit akzeptierten Deltas unter #42.

Neu cross-cutting akzeptiert ist `REQ-TRACE-001`: materielle Systemarbeit bleibt von Goals/Needs/Pains über Requirement, technische Entscheidung, Implementation und Verification bis zu realer Nutzung/Owner-Feedback rückführbar. Feedback ist Product-/Workflow-Evidence, nicht historische/wissenschaftliche Evidenz.

### Innere Requirement-Struktur

Kanonischer Arbeitsvertrag:

`docs/research/synthesis/requirements-structure.md`

Für neue oder materiell geänderte Requirements werden mindestens auseinandergehalten:

```text
Requirement Identity / Role
Motivation / Driver
Origin / Source / Evidence
Domain Authority / Acceptance Authority / Delivery / Verification Authority
Scope / Exclusions
Dependencies / Relations
Criticality
Architecture Significance
Acceptance / Verification
Risks / Forbidden Loss
Status
```

Wichtig:

- `Source` = konkrete Herkunft/Begründung des Requirements;
- `Domain Authority` = Kompetenz, die seine fachliche Bedeutung besitzt;
- `#42` = kanonischer Requirements-Lifecycle-Owner;
- `#48/#59` = technische Ableitung/Umsetzung, nicht fachliche Semantik;
- `Criticality` ≠ `Delivery Priority`;
- Delivery-Reihenfolge wird dynamisch nach Nutzen, Dependencies, Risiko, Reversibilität und aktuellem Research-Pain bestimmt.

Responsibility-/Dependency-Sicht:

`docs/research/synthesis/requirements-responsibility-dependency-map.md`

Keine Big-Bang-Migration: bestehende Requirements werden clusterweise nachgezogen, sobald sie technisch/fachlich aktiv bearbeitet werden.

### Deterministic Requirements Assurance – #62

#62 besitzt die formale Quality-Assurance-Schicht für bereits geklärte Requirements-Regeln.

Bausteine:

- `tools/requirements/requirement-record.schema.json` – JSON Schema Draft 2020-12;
- `tools/requirements/data/records.json` – machine-readable QA-/Traceability-Projektion, keine zweite fachliche Requirement Truth;
- `tools/requirements/validate.py` – deterministischer Cross-Record-/Repo-Validator;
- `tools/requirements/tests/` – positive/negative Regressionstests;
- `.github/workflows/project-assurance.yml` – konsolidierter automatischer Assurance-Check;
- `docs/architecture/assurance/requirements-assurance-harness.md` – Rule-/Scope-Vertrag.

Harte Grenze:

```text
Schema / Validator
= Form, Referenzintegrität, Authority-/Dependency-/Coverage-/Lifecycle-Invarianten

Domain / Fachreview
= Bedeutung, fachliche Richtigkeit, wissenschaftliche Suffizienz
```

Ein Harness-PASS bedeutet nur `formal requirements conformance for the implemented rule set`, niemals wissenschaftliche Validierung.

Aktuelle Realtests 2026-09-03:

- Requirements-/Trace-/Operational-Assurance ist nach der #62-Reconciliation wieder vollständig grün;
- PR #73 / Run `33764679014`: `REQ-WF-001` besitzt nun den von #62 verlangten strukturierten QA-Record für den weiterhin sachlich korrekten Status `partial`;
- PR #72 / Run `33765119632`: D1 Safe Mutation / Progress bestand Requirements-, Assurance- und Operational-Regressionen sowie beide formalen Validatoren;
- PR #74 / Run `33766069328`: Admission-Prep bestand dieselbe vollständige Assurance-Kette;
- PR #77 / Run `33786277613`: D2 Current Context / Resume bestand Requirements-, Assurance- und Operational-Regressionen sowie beide formalen Validatoren;
- PR #79 / Run `33787734297`: der reale #46/Lampe-420-Fresh-Context-Slice bestand inklusive Git-Blob-Basis-Revalidation, vollständigem Resume-Contract und beiden formalen Validatoren;
- PR #71 / Run `33789468211`: der abgeschlossene #70-Audit-Snapshot bestand nach Abschluss von D1/D2 und realem Slice die aktuelle vollständige Project-Assurance-Kette;
- `REQ-TRACE-001` bleibt in Coverage und strukturiertem Requirement-Record erfasst.

### Operational Integration – #48/#59

Der gemeinsame Integrationsschnitt ist inkrementell erweitert:

- `tools/operational/enforcement-map.json` projiziert Requirements referenzbasiert auf Enforcement-Klassen, Contracts, Rule-IDs, Capabilities, Fixtures, Status und fachliche Review-Grenzen; sie dupliziert keine Requirement-Semantik;
- `tools/operational/core.py` stellt gemeinsame mechanische Loader-/JSON-Schema-Infrastruktur für die bestehenden #62/#63-Commands bereit;
- `tools/operational/mutation.py` ergänzt den lokalen Pre-write-/Progress-Guard: bounded replacement aus fresh state, destructive mismatch `blocked`, bereits erfüllter Zustand `NO_CHANGE`, expliziter Full-Replacement-Typ und atomarer lokaler Write-Adapter. **Restgrenze:** direkte GitHub-Connector-/Contents-API-Writes umgehen diesen lokalen Guard, sofern sie ihn nicht explizit konsumieren; dies wurde im #70-Closure-Lauf real reproduziert und an #48/#59 geroutet;
- `tools/operational/context.py` ergänzt den transienten Current-Context-/Resume-Core: `ready | unresolved | blocked`, Work-Order-Identität, führende Domänen, Method-/Quality-Frame, Required Evidence, Prerequisite-Basis-Fingerprint/Revalidation und Cursor-`continue | redirect` ohne eigene Priority-/Fachauthority;
- `tools/operational/context_spec.py` lädt einen kanonischen JSON-Work-Order ohne Markdown-Semantik zu erraten und prüft deklarierte Git-Blob-Basis; stale PASS wird `unresolved / revalidation required`;
- `docs/research/cases/u2-lampe-420-work-order.json` ist der erste reale bounded Work Order; Source/Excerpt/Finding-Inhalt bleibt referenziert in seinen bestehenden kanonischen Häusern;
- `tools/requirements/validate.py` und `tools/assurance/validate.py` bleiben kompatible Wrapper/Commands; kein Big-Bang-Rewrite;
- `Project Assurance` prüft Map-/Requirements-/Trace-/Operational-Regeln und läuft seit PR #74 auf jedem Pull Request; Push-Pfadfilter bleiben zur Lärmbegrenzung bestehen;
- wissenschaftliche/Methoden-/Owner-Urteile bleiben explizite Review-Grenzen und werden nicht als Validator-PASS determinisiert;
- repo-weite GitHub-Admission ist noch nicht vollständig: direct writes nach `main` bleiben bis zur serverseitigen Required-PR/Protection-Konfiguration außerhalb des lokalen D1-Adapters.

Kanonischer Architektur-/Trade-off-Ort: `docs/architecture/operational-execution-architecture.md`. Implementations-/Verification-Trace liegt in `tools/assurance/data/trace-records.json`; D1/D2 und Lampe-420-Acceptance sind unter #48/#59/#61/#46 geroutet. Der historische AI-Resilience-Audit ist als `docs/architecture/assurance/ai-resilience-root-cause-audit.md` auf `main` erhalten; #70 ist abgeschlossen. GitHub-Admission bleibt #44 (`DD-20260903-001`).

### Value / Decision / Delivery / Feedback Assurance – #63

#63 schützt die formale Kette:

```text
Goal / Need / Pain / Constraint
→ accepted Requirement
→ Decision bzw. begründete reversible Direktumsetzung
→ Implementation
→ Verification
→ reale Nutzung / Owner-Feedback
→ Delta
```

Bausteine:

- `tools/assurance/trace-record.schema.json`;
- `tools/assurance/governance-registry.json`;
- `tools/assurance/policy.json`;
- `tools/assurance/data/trace-records.json`;
- `tools/assurance/validate.py`;
- `tools/assurance/tests/`;
- `.github/workflows/project-assurance.yml`;
- `docs/architecture/assurance/value-decision-delivery-assurance.md`.

Der Changed-Code-Guard prüft kontrollierte technische Pfade gegen einen **aktuellen** Implementation-Trace. Ein alter `verified` Record schaltet einen Pfad nicht dauerhaft frei. Materielle technische Records müssen auf accepted Requirements, `G/N/P`-Driver und bindende Governance rückführbar sein.

Owner-/Nutzerfeedback wird als eigener Product-/Workflow-Evidence-Typ geführt. Negative Outcomes wie `pain-persists`, `regression`, `new-pain`, `new-need` oder `requirement-change` müssen einen offenen Delta-Pfad erzeugen. `owner-workflow-acceptance` kann nicht durch technische Selbsttests ersetzt werden.

`FB-20260902-003` persistiert das reale Owner-Feedback nach dem Lampe-PDF-Pilot: Der wissenschaftliche State ist zunehmend korrekt, der operative Forschungsarbeitsplatz bleibt aber zu stark manuell/chat-orchestriert und textlastig. Bestehende `REQ-UX-001/002`, `REQ-WF-001`, `REQ-STATE-001`, `REQ-LEAN-001` decken das Ziel bereits; der offene Delta ist primär Delivery-/Architecture-Priorisierung hin zu strukturiertem Research State, automatischem Context/Trace/Derive und daraus erzeugten menschenlesbaren Sichten.

Materielle Scope-/Qualitätsänderungen benötigen weiterhin ein explizites Requirement-/Decision-Delta. Neue Buzzwords, Tools, Frameworks oder Phasenbegriffe ändern keinen akzeptierten Scope implizit.

Delivery-/Verification-Status wird in `docs/development/requirements-coverage.md` geführt.

### Wissensarbeit-Pilot-Rückfluss – #65

`esany/Wissensarbeit` hat Histo-Orla als realen Pilot verwendet und den generischen Pilot am 2026-09-02 geschlossen. Projektspezifische Erkenntnisse wurden korrekt als #65 nach Histo-Orla zurückgegeben: `external pilot review input / candidate / no implementation authority`.

Der generische Pilot hat sechs ausführbare Learnings abgesichert:

- materieller State darf nicht nur im Chat bleiben (`conversation harvesting`);
- generierte/komprimierte Contexts brauchen Fidelity gegen materielle Referenzen und `unresolved`-Zustände;
- Token-/Kontextreduktion ist nur nach `lossless-by-reference` zulässig;
- Co-Creation/Elicitation geht Requirement-/Decision-Promotion voraus;
- ein erfolgreicher Case ändert generische Mechanismen erst nach Generic-Fit;
- Case-Isolation verhindert, dass Pilotsemantik in generische Core-Strukturen ausläuft.

Kanonische technische Einordnung: `docs/architecture/prior-art-development-inputs.md`. #65 selbst bleibt Candidate-Review-Input und wird nur bei realer Relevanz über die zuständigen Histo-Orla-Owner einzeln dispositioniert.

## 3. Baselines und Präzedenz

- #28 Problem-/Need-/Pain-Baseline v0.1 – completed, weiterhin upstream Value-/Problem-Basis
- #29 Workflows U1–U4 v0.1 – completed
- #30 Research Questions – completed
- #31–#39 SOTA C1–C9 – completed für damalige Entscheidungen
- #40 Risks/Constraints – completed
- #41 Capability/Quality – completed
- #42 Requirements Baseline + accepted Extensions + Requirements Structure – aktiver Requirements Owner
- #43 historisches Architecture-Readiness-Gate; kein aktuelles Blocking-Gate
- #70 AI-Resilience Root-Cause-Audit – **completed / retire-active**; historischer Snapshot `docs/architecture/assurance/ai-resilience-root-cause-audit.md`, keine Requirement-/Implementation-Authority. D1/D2 und realer Lampe-420-Slice sind an bestehende Owner überführt; kein neuer Requirement-Gap. Der im Closure-Lauf erneut belegte Connector-write-Restpunkt liegt bei #48/#59, serverseitige Admission bei #44.
- #92 Architecture/Product Re-Baseline – Roadmap via PR #94 integriert; R0–R3 und die frühere R4–R8-Sequenz bleiben Prior Art / frühere Lösungshypothese. **Aktiver Re-entry-Status:** `fresh-rebuild-conception-complete / wp1-implemented-and-technically-verified / owner-workflow-evidence-pending`. Kein Folgepaket ist automatisch admitted; Candidate WP2 bleibt Proposal bis zu eigener #48/#59/#42/#63-Admission.

Die Baselines bleiben gültig und werden durch reale Research-, Methoden- und Nutzungsbefunde präzisiert.

## 4. Aktive fachliche Work Owner

### Current Work Selection

`selection-open` — Im aktuell reconciliierten kanonischen State ist **nichts explizit owner-authorized als `selected-current` ausgewählt**. Dies ist eine abgeleitete Handoff-Sicht, keine Selection Authority oder Selection Registry.

Aktuelle Dispositionen ohne Prioritätsableitung:

- #46 / Lampe 420 / `WO-U2-LAMPE-420-001` → `resumable-not-selected`;
- #46 / Sachenbacher / gemergter PR #76 → `integrated-not-selected`;
- #47 → `active-independent-not-selected`;
- #103 → `active-independent-not-selected` – user-requested Research zu Anno II., Richeza und St. Peter und Paul Saalfeld; eigener Work Owner, keine Selection Authority;
- #60 → `supporting` Method Truth;
- #92/#94 → `architecture-supporting / fresh-rebuild-conception-complete / wp1-implemented-verified / owner-use-pending`; keine Research Selection und keine automatische Ausweitung auf WP2+.

`selected-current` entsteht nur durch explizite Research/Product-Owner-Autorisierung. Reconciliation-Anker: `docs/architecture/assurance/work-selection-reconciliation-20260910.md` / PR #97. Weder ein resumable Work Order noch ein gemergter/offener PR, grünes CI, ein aktiver Work Owner, Method Work oder die Architecture Roadmap erzeugt eine Current-Work-Auswahl.

### #46 – U2 Knau/Orlagau

`in-research / live-use-case / working-research`

Aktueller historischer Scope: mittelalterliche Quellen-, Herrschafts-, Siedlungs- und Beziehungsräume im Orla-Grenzraum; konkrete Findings, Search Boundaries und Quellenexzerpte unter `docs/research/cases/`. `WO-U2-LAMPE-420-001` bleibt ein valider, `resumable` bounded Work Order, ist aber **keine globale Current-Work-Auswahl**. Sachenbacher/PR #76 ist als begrenzte Reconciliation-/Research-Evidenz integriert und ebenfalls nicht `selected-current`. Offene Fallfragen bleiben bei #46 und werden erst nach expliziter Research-Owner-Auswahl wieder als aktueller Slice ausgeführt.

### #47 – U1 Teich-/Feuchtkulturlandschaft

`in-research / working-research`

Aktiver eigenständiger Research Owner mit eigener Quellenlogik; aus aktivem Ownership folgt keine globale Current-Work-Auswahl.

### #103 – Anno II., Richeza und St. Peter und Paul Saalfeld

`in-research / exploratory-working-research / active-independent-not-selected`

Eigenständiger, vom Nutzer angestoßener Research Owner für die Relation Richeza–Anno II., die zweistufige Institutionalisierung Saalfelds (Kanonikerstift → Benediktinerkloster), Köln-/Mainz-/Siegburg-Rechte und -Netzwerke sowie die zu prüfende Bamberg-/Michelsberg-Verbindung. Kanonisch: `docs/research/cases/anno-richeza-saalfeld-netzwerk.md` und `docs/research/cases/anno-richeza-saalfeld-source-ledger.md`. Der Fall läuft wegen noch nicht hinreichend operationalisierter einschlägiger #60-Domain-Profile als `working-research / method-debt`; der direkte Michelsberg-Bamberg→Saalfeld-Link ist innerhalb der bisher geprüften Search Boundary `unresolved / not evidenced`. Aktuelle nächste Aktion: MUB I Nr. 331 und Lampert 1071 text-/überlieferungsnah exzerpieren und erst danach die Rechtslabel `Eigenkloster | Reichsabtei | Fürstabtei` bewerten.

### #60 – Domain Method Profiles

`in-research / cross-cutting-method-work-package`

Besitzt Method Truth, nicht Systemarchitektur. Im Current-Work-Handoff ist #60 `supporting`; Method Truth wählt keinen historischen Current Slice aus.

Aktuelle Priorität innerhalb des Method-Work-Package:

1. Diplomatik / Urkundenlehre + Editionswissenschaft/Textkritik;
2. Archivistik / Provenienz / Registraturkunde;
3. historische Philologie / mittellateinische Semantik / Hermeneutik;
4. weitere Profile problemgetrieben aus #46/#47.

## 5. Requirements Owner #42

#42 ist einziger Owner akzeptierter Systemanforderungen und ihres Lifecycles.

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`
- `docs/research/synthesis/requirements-structure.md`
- `docs/research/synthesis/requirements-responsibility-dependency-map.md`

Neue fachlich belastbare Systembedarfe aus #46/#47/#60 sowie belastbare Product-/Workflow-Deltas aus realer Nutzung gehen als Requirement-Deltas dorthin. Fachmethodische Wahrheit selbst bleibt #60-Eigentum; Research-Owner-Feedback besitzt Ziel/Nutzen/Pain, nicht historische Wahrheit.

#62 prüft die formalisierten Requirement-Strukturen deterministisch. #63 prüft formale Value-/Decision-/Delivery-/Feedback-Traceability. Beide besitzen weder Requirement Truth noch Domain Authority.

## 6. Technical Lead #48

#48 besitzt:

- technische SOTA-/Best-Practice-/Existing-Tool-Einordnung;
- technische Priorisierung nach Requirement, Dependency, Risiko, fachlichem Nutzen und Reversibilität;
- reversible technische Entscheidungen und Refactoring;
- Integrations-/Feasibility-Spikes;
- evolutionäre Architektur;
- technische Acceptance-/Regression-/Invariant-Tests;
- Rückgabe fachlicher/Requirements-Fragen an #42/#60.

Kanonischer Ableitungsvertrag:

`docs/architecture/requirements-derivation.md`

Technische Ableitung erfolgt nicht direkt `Requirement → Technologie`, sondern:

```text
Requirement / Cluster
→ upstream Goal/Need/Pain verstehen
→ System Responsibility
→ Architecture Concern / Quality Attribute
→ Technical Research Question
→ Existing Tools / Standards / Patterns
→ Candidate Approach
→ Trade-off / Risk / Reversibility
→ Decision / Implementation Trace (#63)
→ Implementation / Verification
→ reale Nutzung / Feedback
```

Zusätzliche aktuelle Prior-Art-/Operational-Inputs:

- `docs/architecture/rebaseline-roadmap.md`;
- `docs/architecture/operational-execution-architecture.md`;
- `docs/architecture/prior-art-development-inputs.md`;
- `esany/paleo-type` und `esany/Wissensarbeit` werden bei direkt relevanten materiellen Entscheidungen frisch als Prior Art gelesen, niemals als fremde Requirement-/Semantik-Authority.

#48 besitzt nicht historische Findings, Method Truth, Scope-Reduktion akzeptierter Requirements oder das Recht, fachliche Unsicherheit technisch wegzumodellieren.

## 7. Development & Verification #59

#59 implementiert und verifiziert akzeptierte Requirements. Es ist keine eigene Produktphase und kein Scope-Owner.

Delivery Coverage:

`docs/development/requirements-coverage.md`

Status je Requirement:

`not-started | in-progress | implemented | verified | partial | blocked | research-needed | owner-deferred`.

Technische Arbeit beginnt dort, wo ein Requirement-/Constraint-Cluster hinreichend klar ist; noch offene Fachsemantik bleibt sichtbar und wird nicht von Dev erfunden.

Bei materieller technischer Arbeit gelten #62/#63 als reproduzierbare formale QA-Schichten. `verified` braucht weiterhin zusätzlich die inhaltlich passende Verification Authority/Evidenz; bei `owner-workflow-acceptance` reale bestätigende Owner-/Nutzererfahrung.

## 8. Technische Teilpakete

- #49 – Zotero ↔ OneDrive, read-first Integration/Feasibility
- #50 – Canonical Research State / Source Identity
- #51 – Document-/Findspot-Pipeline
- #52 – OCR/HTR Benchmark/Integration
- #53 – Historical Retrieval
- #54 – Promotion / deterministic invariants
- #55 – Human-readable Audit
- #56 – Rights / Credentials / External Processing
- #57 – Provider Removal / Export / Restartability
- #58 – just-in-time ADRs bei materiellen/schwer reversiblen Entscheidungen
- #61 – Work-Context / Method-Conformance / Handoff Technical Research
- #62 – Requirements Assurance Harness / deterministische Requirements-QA
- #63 – Goal/Need/Pain → Requirement → Decision → Delivery → Feedback Assurance Spine

### Historical Re-Baseline W1 — Prior Art / frühere Lösungshypothese, nicht aktiver kritischer Pfad

Die frühere Sequenz

```text
#50 semantic Source/Instance contract
-> #49 reliable read-only source/byte resolution
-> #51 document/findspot runtime proof
-> #53 retrieval against inspected source
-> #55 derived human-readable research view
-> #57 availability/restartability proof
-> reale Owner-Workflow-Akzeptanz
```

bleibt als **historische Dependency-/Lösungshypothese** nachvollziehbar, ist aber nach der D4-Reconciliation **kein aktueller kritischer Product Path und keine Ausführungsreihenfolge**.

Insbesondere gilt aktuell nicht automatisch:

- #49 ist der nächste technische Enabler;
- #51/#53/#55/#57 folgen aus Sequenz;
- ein R5-/Vertical-Slice muss als nächster Rebuild-Schritt ausgewählt werden;
- alte W1-/R4–R8-Arbeit ist parallel zur frischen Umbaukonzeption auszuführen.

Die frische Umbaukonzeption muss diese Elemente aus accepted Requirements + aktueller Repo-Realität + F1–F14 + D4 erneut als `RETAIN | ADAPT | REJECT | DEFER | TEST` disponieren.

## 9. Source / Storage Responsibility

```text
OneDrive  = Source of Bytes
Zotero    = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Provider-ID, Pfad oder Zotero-Key ersetzen nicht Source-/Instance-Identität.

## 10. Aktuelle nächste Aktion

### Rebuild

**Fresh Rebuild Conception = COMPLETE.**  
**WP1-STATE-SPINE-V0 = IMPLEMENTED + TECHNICALLY VERIFIED + INTEGRATED.**  
**Owner-/Workflow-Feedback = PAIN PERSISTS for the research-facing workflow.**

Kanonische Basis / Delivery:

- Conception: `docs/architecture/fresh-rebuild-conception-20260923.md`
- Admission/Work Order: `docs/development/canonical-research-state-spine-v0-implementation-admission-20260923.md`
- Implementation: PR #132 → `d33828441c5333341af2794574d2a31dda47845b`
- #63 Trace: `DEC-STATE-SPINE-001` / `IMP-STATE-SPINE-001=verified`
- Owner feedback: `FB-20260923-004`; initial comment #63/5802074059, refined by #63/5802389782

WP1 bleibt als technischer Unterbau bestätigt: provider-neutrale Identität, exakte Owner-/Findspot-Auflösung, explizites `unresolved` und regenerierbarer Auditpfad funktionieren innerhalb des Coverage Ceiling.

Der reale Fresh-Context-/Owner-Test zeigt aber zwei Ebenen:

1. **Audit/Provenienz allein ist zu maschinenorientiert als Forschungsarbeitsfläche.**
2. Die anschließende Verkürzung auf eine bloße „visuelle Zusammenstellung“ war ebenfalls zu eng.

Die bereits bestehende fachliche/technische Arbeitsteilung bleibt leitend:

```text
Zotero
= bibliographische/archivische Verwaltung + Attachment-Referenz

Source-/Byte-Layer
= konkrete Datei / exakte inspizierte Instanz / Derivate

Histo-Orla Research State
= Findspot / Excerpt / Finding / Interpretation / Unsicherheit /
  methodische und evidenzielle Provenienz

Owner-facing View
= abgeleitete Darstellung dieses Research State
```

Für Quellenarbeit ist der relevante wissenschaftliche Arbeitsgegenstand deshalb **nicht eine Summary Card**, sondern ein **provenienzgebundenes Exzerpt/Fundstellen-Paket**:

- Originalausschnitt bzw. vollständige visuelle Evidenzeinheit;
- textlicher Exzerpt-/Transkriptionsinhalt soweit vorhanden;
- exakte Source/Representation/Instance/Derivative/Findspot-Rückbindung;
- bibliographische/archivische Referenz aus der zuständigen Verwaltungsschicht;
- Finding/Beobachtung getrennt vom Exzerpt;
- Interpretation getrennt vom Finding;
- Unsicherheit, Widerspruch und Aussagegrenze sichtbar;
- Method-/Review-Status proportional zur Konsequenz;
- daraus ableitbare visuelle/vergleichende Sichten ohne neue Wahrheitsschicht.

Für den Sachenbacher-Pilot bedeutet das: Karte + relevante Textstellen müssen als prüfbare, auf die exakte PDF-Instanz rückführbare Exzerpte/Fundstellen zusammenspielen. Eine freie Zusammenfassung oder bloße Locator-Kette erfüllt den Forschungsworkflow nicht.

Das Feedback ist Product-/Workflow-Evidence, keine historische Evidenz. Es ändert weder #42-Requirements noch #60-Method Truth und invalidiert WP1 nicht.

**Exakt nächste ausführbare Rebuild-Aktion:**

> **Unter #48/#49/#50/#51/#55/#63 einen bounded excerpt-zentrierten Research-Workflow-Test für den Sachenbacher-Fall ableiten: Zotero-/Bibliographie-Referenz, exakte Instance/Findspots, visuelle Evidenz und Text-Exzerpte zu einem wissenschaftlich transparenten, prüfbaren Owner-View zusammenführen, ohne die Ebenen zu verschmelzen.**

Der Test soll zuerst zeigen:

- ob der Owner von der Quelle/Exzerpt-Ebene aus sinnvoll arbeiten kann;
- ob Provenienz und exakte Instanz ohne technische Dominanz jederzeit prüfbar bleiben;
- ob Finding/Interpretation/Unsicherheit sauber getrennt und nachvollziehbar sind;
- ob Zotero seine Verwaltungsrolle behält, ohne Research State zu besitzen;
- ob die Ansicht vollständig regenerierbar bleibt und kein zweiter Truth Store entsteht.

Vor einer Implementation ist zu klären, ob der Test mit vorhandenen Artefakt-/Derived-View-Mitteln ausführbar ist oder eine kleine eigene Admission benötigt. **Kein breiter WP4-/UI-Stack ist dadurch admitted.**

Verbindliche Grenzen:

- keine freie Zusammenfassung als Ersatz für ein Exzerpt;
- keine unstrukturierte Forschungsfragen-Sammeldatei als primäre Research-Truth;
- #51s vollständige publizierte Karte bleibt die visuelle Evidenzeinheit; Highlights/Ausschnitte sind regenerierbare Derived Views;
- keine Verschmelzung von Source, Instance, Derivative, Findspot, Excerpt, Finding und Interpretation;
- keine neue historische Interpretation allein aus der Darstellung;
- `R51-06`, fehlende Method Application und fehlende Alternatives bleiben sichtbar;
- `selection-open` bleibt bestehen;
- Candidate WP2, WP3, WP4 und WP5 bleiben ohne eigene Admission nicht implementierungsautorisiert.

### Andere bestehende Owner

#46/#47/#60 sowie #49–#63 behalten ihren jeweiligen kanonischen Scope. Das Feedback routet die Workflow-/Darstellungsfrage nun ausdrücklich auch an #49/#50/#51, weil die Owner-Nützlichkeit von der vollständigen Arbeitsteilung zwischen Bibliographie, Bytes, Exzerpt/Research State und Derived View abhängt. Falls daraus ein echter Requirement-Delta entsteht, geht er separat an #42.

Der frühere Fresh-Rebuild-Startkontext bleibt als Provenienz erhalten:

`docs/architecture/fresh-rebuild-conception-work-context-20260923.md`

Chat-Closure-/Wissensmonopol-Audit:

`docs/architecture/assurance/chat-closure-knowledge-monopoly-audit-20260923.md`

## 11. Blocker / Decisions

#44 bleibt Register für echte Blocker und Owner-Entscheidungen.

Aktuell aktiv:

- `DD-20260903-001` – **GitHub Required-PR / Branch-Protection Admission**: D1 schützt den lokalen Operational-Write-Pfad und PR #74 bereitet `Project Assurance` als globalen Required Check vor. `main` ist jedoch weiterhin unprotected, Rulesets sind leer und der aktuell autorisierte GitHub-Connector besitzt keine Ruleset-/Branch-Protection-Schreibfunktion. Empfohlene Auflösung durch Repository-Admin: Required Pull Request für `main` + Required Status Check `Project Assurance`. Danach End-to-End-Negativtest unter #59: direct main write muss abgewiesen werden; normaler PR mit grünem Check bleibt zulässig.

Der Blocker betrifft nur die repo-weite GitHub-Prevention. WP1 ist trotz dieses bestehenden serverseitigen Restpunkts über Branch/PR + Project Assurance technisch verifiziert integriert; daraus folgt keine Aussage, dass Direct-Main-Prevention gelöst wäre. #46/#47 Live Research sowie #49–#63 behalten ihren jeweiligen Owner-Scope. Der direkte Connector-write-Restpunkt bleibt B1-Delivery-Gap unter #48/#59; serverseitige Required-PR/Required-Check-Admission bleibt #44. `FB-20260902-003` bleibt Product-/Workflow-Evidence, keine historische Evidenz.

## 12. Handoff-Test

Ein neuer Chat muss nach

`AGENTS.md → PROJECT_STATE.md → README.md → Work Owner → kanonisches Artefakt`

ohne alten Chat erkennen können:

- **Current Work Selection ist `selection-open`; `resumable`, `integrated`, aktiver Work Owner, Method Work, PR-/CI-Status oder Architecture Roadmap begründen keine Auswahl;**
- welche Arbeit `governing/project`, `domain/research`, `product capability`, `operational support`, `pilot/testfixture` oder `superseded/archive` ist;
- dass `src/histo_orla/` aktuell nicht eingeführt ist und Product-Code-Struktur bedarfsgetrieben aus realer Runtime-Produktlogik entstehen muss;
- dass der frühere W1-Pfad `#50 -> #49 -> #51 -> #53 -> #55 -> #57 -> Owner Acceptance` **nur Historical Prior Art / frühere Lösungshypothese** ist und kein aktueller kritischer Pfad; WP1 ist implementiert/technisch verifiziert; aktuell offen ist der separate Owner-/Workflow-Nutzencheck; Candidate WP2 ist nur Proposal und nicht automatisch admitted;
- aktuelle historische und methodische Arbeit;
- vollständige aktive Requirements;
- Motivation/Origin/Authority/Scope/Dependencies eines aktiv bearbeiteten Requirements;
- welche Regeln deterministisch durch #62/#63 geprüft werden und welche Fach-/Owner-Review bleiben;
- von welchem Goal/Need/Pain eine materielle technische Änderung getragen wird;
- welche Decision/Implementation/Verification sie realisiert;
- welche reale Nutzung/Owner-Rückmeldung vorliegt oder noch fehlt;
- dass #65 externer Pilot-Review-Input ohne automatische Promotion ist;
- welche Prior-Art-Learnings bei materiellen technischen Entscheidungen zu challengen sind, einschließlich Context Fidelity, Generic-Fit und Case Isolation;
- primäre Funktion/Authority;
- Method-/Evidence-Status;
- technischen Delivery-/Verification-Status;
- offene Debt/Blocker;
- nächste Aktion und Persistenzort.

> **Fachdomänen führen. Technologie dient.**

> **Needs/Pains/Goals begründen das Warum; Requirements operationalisieren das Was; Technik entscheidet das Wie; reale Nutzung schließt die Schleife.**

> **Schema prüft Form; Validator prüft formale Invarianten; Fach-/Owner-Review prüft Bedeutung und Nutzen.**

> **Criticality ist nicht Delivery-Reihenfolge.**

> **State of the Art und Best Practice sind Basis der Mittelwahl.**
