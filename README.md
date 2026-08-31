# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk/Orla und für die Entwicklung einer **transdisziplinären historischen Forschungsassistenz**.

Ziel ist ein **funktionierendes, dauerhaft nutzbares Forschungswerkzeug**, das belastbare Quellenarbeit, fachliche Problemübersetzung, regionalisierte Expertise, transdisziplinäre Analyse und einen nachvollziehbaren, restartbaren Forschungszustand unterstützt.

## Pflicht-Bootstrap / Handoff

Vor substantieller Arbeit am Projekt zuerst lesen:

1. **`AGENTS.md`** – bindende repo-weite Arbeits-, Work-Context-, Persistenz- und Handoff-Regeln
2. **`PROJECT_STATE.md`** – aktueller phasenübergreifender Projektstand
3. diesen `README.md`
4. zuständiges Work-Owner-Issue
5. dessen kanonische Artefakte

> **Chat ist Werkstatt. GitHub ist Projektgedächtnis.**

Kein für die Fortsetzung notwendiger Forschungs-, Requirements-, Architektur-, Entwicklungs- oder Entscheidungsstand darf ausschließlich in einem Chat oder Modellzustand verbleiben.

Für substantielle Arbeit gilt zusätzlich der bindende Work-Context-Vertrag aus `AGENTS.md` §13: primäre Funktion, Work Owner, bounded Scope/Exclusions, fachlicher Method-/Quality-Frame, Authority-Grenzen, Stop/Handoff, Return Condition und kanonischer Persistenzort müssen aus dem Repository rekonstruierbar sein.

## Präzedenz

```text
konkreter Forschungsauftrag / Nutzer-Pain
→ führende Fachdomäne(n)
→ wissenschaftliche Standards / Domain Method / Evidenzbedarf
→ State of the Art + internes Prior Art
→ validierte Needs / Capabilities / Quality Attributes
→ Requirements + Acceptance Criteria
→ Architektur / Assurance / Design
→ Development / Integration
→ technische + wissenschaftliche Verifikation
→ reales MVP / Nutzung
→ Evaluation / Iteration
```

**Fachdomänen führen. Technologie dient.**  
**Dev informiert Requirements; Dev besitzt sie nicht.**

Lean bedeutet: **so wenig unnötige technische Komplexität wie möglich, aber so viel funktionierendes System wie nötig**, um validierte Nutzer- und Forschungsanforderungen hochwertig zu erfüllen.

## Aktuelle Phase

Discovery, SOTA, Risk/Constraints, Capability-/Quality-Synthese, Requirements und Architecture Readiness wurden in **#28–#43 abgeschlossen**.

Gate-Ergebnis #43:

**`architecture-ready-with-bounded-research-debt`**

Aktuelle Phase:

```text
Requirements
→ Architecture Contracts / Invariants / Assurance
→ reversible technische/integrative Spikes
→ Thin Vertical Slice
→ Architekturvarianten / Trade-offs
→ ADRs
→ MVP-Schnitt
→ Development / Verification
```

Aktueller Architecture Execution Owner: **#48**.

### Aktive fachliche Research-Workstreams

- **#46** – U2 Knau/Orlagau, historische Live-Forschung / Falsifikation
- **#47** – U1 Orlagau Teich-/Feuchtkulturlandschaft, historische Live-Forschung / Falsifikation
- **#60** – Domain Method Profiles: SOTA-basierte fachwissenschaftliche Method Truth / Operationalisierung

#60 ist die methodische Mittelschicht zwischen Vision/Kompetenzlandkarte und Requirements. Ein Domain Method Profile ist kein Prompt und keine Agentenrolle; es muss Fach-SOTA, Quellenlogik, Playbook, Inferenzvertrag, Evidence Appetite, QA/Falsifikation, Interfaces und AI-/Automation-Grenzen nachweisen und an realen Fällen getestet werden.

### Aktive Architektur-/Technik-/Assurance-Workstreams

- **#48** – Architecture Execution Control
- **#49** – Zotero ↔ OneDrive ↔ Histo-Orla Integration, read-first
- **#50** – Canonical Research State / Source Identity / Method-/Work-/Review-Provenienz
- **#51** – Document-/Findspot-Pipeline
- **#52** – OCR/HTR Contract + Benchmark
- **#53** – Historical Retrieval Baseline
- **#54** – Candidate→Review→Promotion + deterministische Transition-/Invariant-Grenzen
- **#55** – Human-readable Research Audit View
- **#56** – Rights Admission / Credentials / External Processing
- **#57** – Provider Removal / Export / fresh-context Restartability
- **#61** – Executable Work-Context / Method-Conformance / Handoff Assurance
- **#58** – Architekturvarianten / ADR / MVP Cut
- **#59** – MVP Development & Verification; aktuell downstream von #58

## Method Truth vs. Method Conformance

Aktuell verbindliche Trennung:

```text
METHOD TRUTH
Was ist fachlich ein zulässiges Vorgehen?
→ #60 / Fachdomäne / docs/research/methods/

METHOD CONFORMANCE
Wurde diese Methode in diesem konkreten Work Context korrekt referenziert,
angewandt, geprüft und nur durch erlaubte Übergänge promoted?
→ #61 + #50/#54/#55/#57
```

Leitregel:

> **Exploration darf offen sein. Promotion ist fail-closed gegenüber fehlender Method-/Evidence-/Validation-Grundlage.**

Ein `method-candidate` darf explorative Forschung unterstützen. Consequential operative Fachmethodik benötigt `working-method` oder höher. Software darf formal prüfbare Preconditions/Transitions erzwingen; sie darf historische Wahrheit nicht simulieren.

## Kanonische Artefakte

### Foundational Research Design

- `docs/research-design/transdisziplinaerer-literaturassistent.md`
- `docs/research-design/README.md` – Status/Präzedenz

Das Design-Dokument bleibt foundational, ist aber nach #28–#43 **nicht mehr alleiniger aktueller Operations-/Requirements-/Architecture-State**.

### Research Governance / Fachmethodik / Quellen

- `docs/research/README.md`
- `docs/research/source-identity-protocol.md`
- `docs/research/methods/README.md`
- `docs/research/methods/domain-method-profile-contract.md`
- Issue **#45** – Research-/Evidence-Protokoll
- Issue **#60** – Domain Method Profiles

### Discovery / SOTA / Synthese

- `docs/research/discovery/`
- `docs/research/sota/`
- `docs/research/synthesis/risks-constraints.md`
- `docs/research/synthesis/capability-map.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/architecture-readiness.md`

### Architecture / Assurance

- `docs/architecture/README.md`
- `docs/architecture/contracts/canonical-research-state.md` – #50
- `docs/architecture/assurance/method-conformance-work-context.md` – #61

Weitere Architekturartefakte entstehen nur bei realem Inhalt; keine Future-Proof-Leerstruktur.

## Aktuelle Verantwortungstrennung für Quellen

Research-Owner-Constraint:

```text
OneDrive
= Source of Bytes / primärer physischer Speicher der Quellen- und Literaturdateien

Zotero
= bibliographische/archivische Verwaltung, Collections, Tags, Notes,
  Attachment-Referenzen

Histo-Orla
= wissenschaftlicher Research State: Evidenz, Findings, Claims,
  Discrepancies, Validation, Provenienz-/Findspot-/Method-Application-Bezug
```

Physischer Pfad, Zotero-Key oder OneDrive-ID ersetzen nicht still die wissenschaftliche Source-/Instance-Identität.

## Verantwortungs- und Handoff-Topologie

```text
Domain / Source Research (#46/#47)
→ bei fachmethodischer Friktion: #60
→ bei generalisierbarem Systembedarf: Domain Review / Requirements #42
→ bei accepted technical need: Architecture #48ff
→ bounded Development #59
→ technische Verification
→ scholarly adequacy return
→ Research NEXT ACTION
```

Cross-cutting:

- **#9 / `AGENTS.md`** besitzt Governance, Authority/Handoff und Anti-Wissensmonopol;
- **#60** besitzt fachliche Method Truth;
- **#42** ist einziger Owner akzeptierter Requirements;
- **#50** besitzt Canonical-State-Responsibilities;
- **#54/#61** besitzen formal prüfbare Transition-/Conformance-Enforcement, nicht Fachwahrheit;
- **#55** rendert Audit aus demselben State;
- **#57** prüft tatsächliche fresh-context Fortsetzbarkeit;
- **#48** koordiniert Architektur;
- unabhängige qualifizierte Fachvalidierung bleibt ein eigener Review-Typ, nicht AI-Selbstreview.

## Governing Principles

- **Wissenschaft vor Convenience:** Fachstandards dürfen nicht durch Nutzerformulierung, Technik, UI oder Vermittlungsziele abgeschwächt werden.
- **Method Truth vor Prompt:** Fachwissenschaftliche Methodik kommt aus Fach-SOTA und validierten Domain Profiles, nicht aus Rollenprompt oder Modellplausibilität.
- **Fail closed on promotion, not exploration:** offene Forschung bleibt möglich; hoher epistemischer Status braucht nachweisbare Method-/Evidence-/Validation-Grundlage.
- **Human-in-the-loop + Auditierbarkeit:** Routinearbeit darf automatisiert werden; consequential work muss erklärbar, anfechtbar, korrigierbar und fachlich überprüfbar bleiben.
- **Kein Wissensmonopol:** Repo muss jederzeit handoff-fähig sein.
- **Research → Delivery:** Research/Requirements dienen der Entwicklung eines funktionierenden Systems.
- **Technische Subsidiarität:** vorhandene Werkzeuge vor Eigenentwicklung; deterministische/spezialisierte Verfahren vor GenAI, wo sie geeigneter sind.
- **Provider-Unabhängigkeit des Research State:** externe Dienste dürfen kuratiertes Forschungswissen nicht monopolisieren.
- **Forschung ≠ Vermittlung:** Vermittlung ist nachgelagert und darf nicht in den Research State zurückschreiben.

## Issue Ownership

Wichtige Steuerungs-/Governance-Owner:

- **#1** – Gesamtstand / Zielbild
- **#9** – Governance, HITL, Transparenz, kein Wissensmonopol, Work Context/Handoff
- **#10** – Research-to-Delivery-Prozess
- **#22** – Kompetenzlandkarte
- **#23** – Issue Ownership / Traceability
- **#24** – Software-/Systemkompetenzen / technische Arbeitsteilung
- **#42** – accepted Requirements
- **#44** – ausschließlich echte Decisions / Dependencies / externe Validierung
- **#45** – Research-/Evidence-Protokoll
- **#48** – Architecture Execution
- **#60** – Domain Method Profiles
- **#61** – Method-Conformance / Work-Context / Handoff Assurance

Regel:

```text
Issue
= Work Owner / Scope / Status / Dependencies / kurze Synthese / nächste Aktion

versioniertes Artefakt
= substantieller kanonischer Research-/Architecture-/Decision-Inhalt

Code / Validator / Test Harness
= konkrete technische Umsetzung oder begrenzter diskriminierender Prototyp
```

Neue Issues nur für eigenständige Work Packages, testbare Spikes/Hypothesen, Decisions/ADRs oder Audits – nicht für jedes Finding.

## Interne Referenzprojekte

- **#12 `paleo-type`** – Prior Art für Governance, Evidence/Provenance, HITL, Restartability, Quality, machine-readable Contracts/Validatoren und technische Subsidiarität.
- **#21 `rgk-main-ssot`** – Prior Art für Claim/Evidence/Interpretation, relationale Muster, Discrepancy Reasoning und Forschung↔Vermittlung.

Prior Art ist Challenge/Input, keine direkte Architekturquelle.

## Handoff-Test

Ein neuer kompetenter Bearbeiter muss nach Lesen von:

```text
AGENTS.md
→ PROJECT_STATE.md
→ README.md
→ zuständiges Owner-Issue
→ kanonisches Artefakt
```

ohne vorherige Chat-Historie produktiv fortsetzen können.

Seit `AGENTS.md` §13 bedeutet das nicht nur „Dateien finden“, sondern auch korrekt rekonstruieren:

- primäre Funktion / Authority Boundary;
- bounded Scope / Exclusions;
- applicable Method/Quality Frame;
- tatsächlich verfügbare Evidenz;
- nächste erlaubte Aktion;
- Stop/Handoff/Return Condition;
- kanonischen Persistenzort.

Wenn das nicht möglich ist, ist der Projektstand **handoff-incomplete**.

## Leitformeln

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Fachdomänen führen. Technologie dient.**

> **Dev informiert Requirements; Dev besitzt sie nicht.**

> **Kein Handoff hängt vom Gedächtnis eines Chats ab.**