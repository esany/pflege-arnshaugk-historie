# pflege-arnshaugk-historie / Histo-Orla

Arbeitsrepository für historische Forschung zur Pflege Arnshaugk/Orla und für die Entwicklung einer **transdisziplinären historischen Forschungsassistenz**.

Ziel ist ein **funktionierendes, dauerhaft nutzbares Forschungswerkzeug**, das belastbare Quellenarbeit, fachliche Problemübersetzung, regionalisierte Expertise, transdisziplinäre Analyse und einen nachvollziehbaren, restartbaren Forschungszustand unterstützt.

## Pflicht-Bootstrap / Handoff

Vor substantieller Arbeit am Projekt zuerst lesen:

1. **`AGENTS.md`** – bindende repo-weite Arbeits-, Persistenz- und Handoff-Regeln
2. **`PROJECT_STATE.md`** – aktueller phasenübergreifender Projektstand
3. diesen `README.md`
4. zuständiges Work-Owner-Issue
5. dessen kanonische Artefakte

> **Chat ist Werkstatt. GitHub ist Projektgedächtnis.**

Kein für die Fortsetzung notwendiger Forschungs-, Requirements-, Architektur-, Entwicklungs- oder Entscheidungsstand darf ausschließlich in einem Chat oder Modellzustand verbleiben.

## Präzedenz

```text
konkreter Forschungsauftrag / Nutzer-Pain
→ führende Fachdomäne(n)
→ wissenschaftliche Standards / Methoden / Evidenzbedarf
→ State of the Art + internes Prior Art
→ validierte Needs / Capabilities / Quality Attributes
→ Requirements + Acceptance Criteria
→ Architektur / Design
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
→ Architecture Contracts / Invariants
→ reversible technische/integrative Spikes
→ Thin Vertical Slice
→ Architekturvarianten / Trade-offs
→ ADRs
→ MVP-Schnitt
→ Development / Verification
```

Aktueller Architecture Execution Owner: **#48**.

### Aktive Architektur-/Technik-Workstreams

- **#48** – Architecture Execution Control
- **#49** – Zotero ↔ OneDrive ↔ Histo-Orla Integration, read-first
- **#50** – Canonical Research State / Source Identity / providerunabhängige Invarianten

Weitere eigenständig testbare technische Work Packages aus dem Gate werden unter #48 geführt.

### Laufende Live Research Cases

- **#46** – U2 Knau/Orlagau, weiterhin `in-research / working-research`
- **#47** – U1 Orlagau Teich-/Feuchtkulturlandschaft, weiterhin `in-research / working-research`

Die Cases sind nicht abgeschlossen. Sie laufen parallel als reale Forschung und Falsifikation der allgemeinen Architekturannahmen. Sie blockieren die Architektur nicht pauschal, können aber neue generalisierbare Invarianten aufdecken.

## Kanonische Artefakte

### Foundational Research Design

`docs/research-design/transdisziplinaerer-literaturassistent.md`

Status/Präzedenz dazu:

`docs/research-design/README.md`

Das Design-Dokument bleibt foundational, ist aber nach #28–#43 **nicht mehr alleiniger aktueller Operations-/Requirements-/Architecture-State**.

### Research Governance / Ablage

- `docs/research/README.md`
- `docs/research/source-identity-protocol.md`
- Issue **#45** – Research-/Evidence-Protokoll

### Discovery / SOTA / Synthese

- `docs/research/discovery/`
- `docs/research/sota/`
- `docs/research/synthesis/risks-constraints.md`
- `docs/research/synthesis/capability-map.md`
- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/architecture-readiness.md`

### Architecture

- `docs/architecture/contracts/canonical-research-state.md` – #50

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
  Discrepancies, Validation, Provenienz-/Findspot-Bezug
```

Physischer Pfad, Zotero-Key oder OneDrive-ID ersetzen nicht still die wissenschaftliche Source-/Instance-Identität.

## Governing Principles

- **Wissenschaft vor Convenience:** Fachstandards dürfen nicht durch Nutzerformulierung, Technik, UI oder Vermittlungsziele abgeschwächt werden.
- **Human-in-the-loop + Auditierbarkeit:** Routinearbeit darf automatisiert werden; consequential work muss erklärbar, anfechtbar, korrigierbar und fachlich überprüfbar bleiben.
- **Kein Wissensmonopol:** Repo muss jederzeit handoff-fähig sein.
- **Research → Delivery:** Research/Requirements dienen der Entwicklung eines funktionierenden Systems.
- **Technische Subsidiarität:** vorhandene Werkzeuge vor Eigenentwicklung; deterministische/spezialisierte Verfahren vor GenAI, wo sie geeigneter sind.
- **Provider-Unabhängigkeit des Research State:** externe Dienste dürfen kuratiertes Forschungswissen nicht monopolisieren.
- **Forschung ≠ Vermittlung:** Vermittlung ist nachgelagert und darf nicht in den Research State zurückschreiben.

## Issue Ownership

Wichtige Steuerungs-/Governance-Owner:

- **#1** – Gesamtstand / Zielbild
- **#9** – Governance, HITL, Transparenz, kein Wissensmonopol
- **#10** – Research-to-Delivery-Prozess
- **#22** – Kompetenzlandkarte
- **#23** – Issue Ownership / Traceability
- **#24** – Software-/Systemkompetenzen / technische Arbeitsteilung
- **#44** – ausschließlich echte Decisions / Dependencies / externe Validierung
- **#45** – Research-/Evidence-Protokoll
- **#48** – aktuelle Architecture Execution

Abgeschlossene Phase:

- **#27** – Execution Control bis Architecture Readiness
- **#28–#43** – Discovery → SOTA → Risk → Capability → Requirements → Gate

Regel:

```text
Issue
= Work Owner / Scope / Status / Dependencies / kurze Synthese / nächste Aktion

versioniertes Artefakt
= substantieller kanonischer Research-/Architecture-/Decision-Inhalt

Code
= konkrete technische Umsetzung oder begrenzter diskriminierender Prototyp
```

Neue Issues nur für eigenständige Work Packages, testbare Spikes/Hypothesen, Decisions/ADRs oder Audits – nicht für jedes Finding.

## Interne Referenzprojekte

- **#12 `paleo-type`** – Prior Art für Governance, Evidence/Provenance, HITL, Restartability, Quality und technische Subsidiarität.
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

Wenn das nicht möglich ist, ist der Projektstand **handoff-incomplete**.

## Leitformeln

> **Der Nutzer darf unsauber fragen; das System muss wissenschaftlich sauber arbeiten.**

> **Die Rückübersetzung vereinfacht die Sprache, nicht die Wissenschaft.**

> **Fachdomänen führen. Technologie dient.**

> **Dev informiert Requirements; Dev besitzt sie nicht.**

> **Kein Handoff hängt vom Gedächtnis eines Chats ab.**