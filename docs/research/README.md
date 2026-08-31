# Histo-Orla – Ablage- und Ownership-Regeln für Research-Ergebnisse

**Projekt-Bootstrap:** `/AGENTS.md` → `/PROJECT_STATE.md` → `/README.md`  
**Research Governance:** #45  
**Issue Ownership:** #23

## Zweck

Dieses Verzeichnis ist der kanonische Ort für substantielle, versionierte Research-Artefakte sowie historische Live-Research-Fälle.

```text
Issue
= Work Owner / Scope / Status / Dependencies / nächste Aktion

Research-Datei
= substantieller kanonischer Forschungsinhalt

Chat
= Werkstatt / transient

Code
= technische Umsetzung oder begrenzter diskriminierender Prototyp
```

> **Chat ist Werkstatt; GitHub ist Projektgedächtnis.**

## One fact / one canonical home

Wenn ein substanzielles Artefakt existiert:

- Datei = ausführlicher kanonischer Inhalt;
- Issue = Work Owner + Status + Kurzsynthese + offene Punkte + Verweis;
- `PROJECT_STATE.md` = phasenübergreifende Navigations-/Handoff-Sicht;
- Chat = transient;
- Views/Reports = abgeleitete Darstellung.

## Bindendes Source-Identity-Protokoll

`docs/research/source-identity-protocol.md` unter #45 trennt mindestens:

```text
historische Source / Überlieferung
→ Edition / Katalog / Reproduktion
→ konkrete digitale/physische Instanz
→ Derivat / OCR / HTR / Transkription
→ exakte Fundstelle / Exzerpt
→ Finding / Interpretation
```

URL, Viewer-Seite oder Dateipfad allein sind keine Quellenidentität.

## Kanonische Struktur

```text
docs/research/
  README.md
  source-identity-protocol.md

  discovery/
    problem-baseline.md
    workflows.md
    research-questions.md

  sota/
    c1-quellen-archiv-provenienz.md
    c2-problemuebersetzung-terminologie.md
    c3-expertise-routing.md
    c4-regionalitaet-multiscale.md
    c5-akteurs-handlungslogik.md
    c6-source-dependence-discrepancy.md
    c7-ocr-htr-retrieval.md
    c8-research-state-auditability.md
    c9-capability-allocation.md

  synthesis/
    risks-constraints.md
    capability-map.md
    requirements-baseline.md
    requirements-extensions.md
    architecture-readiness.md
    phase-reconciliation.md

  methods/
    README.md
    domain-method-profile-contract.md
    ... reale Profile erst bei tatsächlichem Research

  cases/
    u2-knau-orlagau-quellenbefunde.md
    u2-orlagau-suchraum-quellenexzerpte.md
    u1-orlagau-grenzraum-teichlandschaft.md
    orlagau-source-ledger.md
    ... weitere reale Case-Artefakte
```

Keine Future-Proof-Leerstruktur.

## Zuordnung zu Work Ownern

| Issue | Work Owner | kanonisches Artefakt / Bereich |
|---|---|---|
| #28 | Problem-/Need-/Pain-Baseline | `discovery/problem-baseline.md` |
| #29 | Workflows U1–U4 | `discovery/workflows.md` |
| #30 | Research-Question-Portfolio | `discovery/research-questions.md` |
| #31–#39 | SOTA C1–C9 | `sota/` |
| #40 | Risk/Constraint Review | `synthesis/risks-constraints.md` |
| #41 | Capability/Quality Synthesis | `synthesis/capability-map.md` |
| #42 | Accepted Requirements | `synthesis/requirements-baseline.md` + `synthesis/requirements-extensions.md` |
| #43 | historischer Architecture-Readiness-Stand | `synthesis/architecture-readiness.md` |
| #45 | Research-/Evidence-/Source-Protokoll | `source-identity-protocol.md` + Issue-Protokoll |
| #46 | Live Research U2 Knau/Orlagau | `cases/u2-knau-orlagau-quellenbefunde.md`, `cases/u2-orlagau-suchraum-quellenexzerpte.md` |
| #47 | Live Research U1 Teich-/Feuchtlandschaft | `cases/u1-orlagau-grenzraum-teichlandschaft.md` |
| #46/#47 | gemeinsamer Source Ledger | `cases/orlagau-source-ledger.md` |
| #60 | Domain Method Profiles / Method Truth | `methods/README.md`, `methods/domain-method-profile-contract.md`, reale Profiles |

Technische Artefakte ab #48ff werden über `docs/architecture/README.md` und `docs/development/requirements-coverage.md` indexiert.

## Method Truth vs. Requirements

```text
Vision / Need
→ relevante Fachkompetenz
→ #60 fachlicher SOTA / Domain Method Profile
→ reale Quellen-/Case-Tests #46/#47
→ Requirement Candidate / Delta
→ #42 accepted Requirement
→ #48/#59 technische Umsetzung / Verification
```

Methodik darf nicht aus Prompt-/Modellplausibilität zur bindenden Fachmethode werden. Umgekehrt ist ein akzeptiertes Systemrequirement kein technischer Lösungsvorschlag.

## Live Research Cases

Live Cases sind echte historische Forschung und zugleich Failure-/Adequacy-Tests für das System. Sie dürfen Capability-/Quality-/Requirement-Candidates erzeugen. Ein Einzelfall allein erzwingt keine Technologie.

Aktuell laufen #46 und #47 `in-research / working-research`.

## Handoff-Check für Research

Vor `reviewable/completed` oder einem materiellen Chat-Handoff:

1. substantieller Stand im kanonischen Artefakt?
2. Issue-Status und nächste Aktion aktuell?
3. Quellen/Fundstellen/Provenienz ausreichend sichtbar?
4. Search Boundaries und Unsicherheit dokumentiert?
5. Method-/Requirement-Status korrekt getrennt?
6. echte Blocker in #44?
7. `PROJECT_STATE.md` nachgezogen, wenn phasenübergreifender State/Ownership/Dependency materiell geändert wurde?
8. kann ein neuer Bearbeiter ohne Chat fortsetzen?

Wenn nein: Handoff ist nicht vollständig.
