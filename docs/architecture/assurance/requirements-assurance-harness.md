# Requirements Assurance Harness – deterministische Quality Assurance

**Status:** `working technical contract / v0.1`  
**Work Owner:** #62  
**Requirements Truth / Lifecycle:** #42  
**Technical Lead:** #48  
**Development / Verification:** #59  
**Related:** #54 deterministic invariants, #61 conformance/handoff, #60 Domain Method Truth

## 1. Zweck

Die Requirements-Regeln in `docs/research/synthesis/requirements-structure.md` und der Responsibility-/Dependency-Map sollen nicht dauerhaft nur durch Chat-/Prompt-Compliance eingehalten werden.

Der **Requirements Assurance Harness** operationalisiert ausschließlich die bereits formal geklärten Teile als deterministische Qualitätssicherung.

Leitregel:

> **Schema prüft Form. Validator prüft formale Beziehungen und Governance-Invarianten. Fachreview prüft Bedeutung. Skill/LLM erklärt und schlägt vor – es darf keinen Pass erfinden.**

Der Harness ist kein Requirement-Owner, keine Fachmethode und keine Architekturentscheidung.

## 2. Schichten

```text
kanonische Requirement-Semantik (#42, Markdown)
        ↓
machine-readable QA-/Traceability-Projektion
        ↓
JSON Schema
        ↓
projektunabhängige / projektspezifische deterministische Rules
        ↓
CLI / Script
        ↓
Fixtures / Regression Tests
        ↓
GitHub Workflow / lokal / Agent-Tooling
        ↓
PASS | WARN | FAIL mit Rule-ID und Begründung
```

Ein späterer Skill darf denselben CLI-Ausgang lesen, erklären und Reparatur-Candidates erzeugen. Er ist keine Enforcement-Schicht.

## 3. Warum kein Skill als primärer Guard

Ein Skill/Prompt ist nützlich für:

- Requirement-Record vorbereiten;
- fehlende Authority/Dependency-Fragen erklären;
- Validatorfehler in normale Sprache übersetzen;
- mögliche Korrektur als Candidate vorschlagen.

Er ist ungeeignet als alleiniger Guard, weil Modell-Compliance probabilistisch ist und ein Modell nicht selbst attestieren darf, dass es die formalen Regeln eingehalten hat.

## 4. Warum JSON Schema + kleiner Validator

### JSON Schema Draft 2020-12

Geeignet für:

- erforderliche Felder;
- Datentypen;
- Enums / kontrollierte Vokabulare;
- ID-Pattern;
- conditional required fields;
- lokale Strukturvalidierung.

Nicht ausreichend für:

- Cross-Record-Referenzintegrität;
- Graphzyklen;
- Vergleich mit Requirement-Markdown und Delivery Ledger;
- Symmetrie/Inverse von Relationen;
- projektbezogene Lifecycle-Regeln.

### Python-Validator

Ein kleiner deterministischer Validator ergänzt genau diese Cross-Record-/Repo-Regeln. Python wird als Implementationsmittel gewählt, weil der aktuelle Scope klein, offline ausführbar und ohne Policy-Engine lösbar ist. Die Wahl ist reversibel; das Contract-/Rule-Modell bleibt wichtiger als die Sprache.

### Kein OPA/CUE v0.1

OPA/Rego und CUE sind legitime Policy-/Constraint-Werkzeuge. Für den aktuellen privaten Histo-Orla-Scope würden sie jedoch zusätzliche DSL-/Runtime-Komplexität einführen, ohne dass die benötigten Rules den kleinen lokalen Validator überfordern. Neu bewerten, wenn Rule-Komplexität, mehrere Consumer oder externe Policy-Verteilung dies real verlangen.

## 5. Canonical vs. Projection

**Kanonische fachliche Requirement Truth bleibt:**

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`

Die machine-readable Records unter `tools/requirements/data/` enthalten **nur operationalisierte QA-/Traceability-Metadaten**, z. B. Authority, Dependency-Typ, Architecture Significance und Verification-Klasse. Sie dürfen Statement/Rationale/SOTA nicht zu einer zweiten fachlichen Wahrheit duplizieren.

Der Validator prüft, dass jeder strukturierte Record auf eine tatsächlich existierende Requirement-ID verweist.

## 6. Rule-Klassen

### A. `HARD-DETERMINISTIC`

Darf Build/Workflow mit Exit Code != 0 stoppen.

Beispiele:

- `REQ001 duplicate-id` – Requirement-ID mehrfach definiert;
- `REQ002 coverage-drift` – accepted Requirement fehlt im Delivery Ledger oder umgekehrt;
- `REQ003 unknown-target` – Dependency verweist auf unbekannte Requirement-ID;
- `REQ004 self-dependency` – unzulässige Relation auf sich selbst;
- `REQ005 requires-cycle` – Zyklus in als azyklisch definierter `requires`-Relation;
- `REQ006 invalid-enum/schema` – Record verletzt Schema;
- `REQ007 active-without-structure` – implementation-signifikantes Requirement besitzt keinen hinreichenden strukturierten QA-Record;
- `REQ008 verified-without-evidence` – `verified` ohne Verification-Evidence/Referenz;
- `REQ009 owner-deferred-without-decision` – `owner-deferred` ohne explizite Owner-Decision;
- `REQ010 invalid-lifecycle-owner` – accepted Requirement besitzt nicht #42 als Lifecycle-Owner;
- `REQ011 invalid-authority-boundary` – erforderliche Domain/Delivery/Verification Authority fehlt;
- `REQ012 stale-record` – QA-Record verweist auf nicht mehr accepted/definierte Requirement-ID.

### B. `ADVISORY-DETERMINISTIC`

Deterministisch feststellbar, aber zunächst Warnung, weil Projektmigration/Interpretation noch nicht vollständig formalisiert ist.

Beispiele:

- Dependency-Status `unresolved` bei noch nicht implementiertem Requirement;
- `related_to` obwohl möglicherweise stärkere Relation sinnvoll wäre;
- architecture-significant Requirement ohne Derivation Card;
- `conflicts_with` nicht symmetrisch erfasst, solange Zielrecord noch Legacy ist.

### C. `HEURISTIC-ADVISORY`

Darf niemals allein PASS/FAIL entscheiden.

Beispiele:

- möglicher Solution Leakage anhand Technologiebegriffen im Statement;
- möglicherweise nicht atomare Requirement-Formulierung;
- möglicherweise schwaches Acceptance-Kriterium.

LLM/regelbasierte Heuristik darf hier Findings erzeugen, aber nur als Review Candidate.

### D. `HUMAN/DOMAIN REVIEW`

Nicht automatisierbar als wissenschaftlicher Wahrheitsentscheid:

- fachliche Richtigkeit der Motivation/Evidence;
- Eignung der Domain Authority;
- historische oder methodische Interpretation;
- Suffizienz eines Arguments jenseits formal definierter Gates;
- unabhängige Fachvalidierung.

Der Harness kann nur prüfen, dass erforderliche Review-/Validation-Klasse dokumentiert ist.

## 7. Incremental Gate

Keine Big-Bang-Migration.

V0.1 gilt:

1. Requirement-IDs aus Baseline + Extensions werden vollständig extrahiert;
2. Delivery Ledger muss exakt denselben accepted ID-Raum abdecken;
3. QA-Records dürfen nur auf accepted IDs verweisen;
4. für `in-progress | implemented | verified | partial | blocked | owner-deferred` ist ein strukturierter QA-Record Pflicht;
5. für `not-started | research-needed` darf die Struktur zunächst Legacy/fehlend bleiben, wird aber als Migration Debt sichtbar;
6. `verified` verschärft die Rules zusätzlich.

Damit schützt das Tool aktive technische Arbeit sofort, ohne Research durch Dokumentenmigration zu blockieren.

## 8. CLI-Vertrag

Vorgesehener Entry Point:

```bash
python tools/requirements/validate.py
python tools/requirements/validate.py --json
python tools/requirements/validate.py --strict-warnings
```

Exit Codes:

- `0` – keine Hard Errors;
- `1` – mindestens ein Hard Error;
- `2` – Tool-/Config-/Parse-Fehler.

Jedes Finding enthält mindestens:

```text
rule_id
severity
requirement_id (falls zutreffend)
message
source/path
```

## 9. Workflow / CI

GitHub Actions soll bei Änderungen an folgenden Bereichen laufen:

- `docs/research/synthesis/requirements-*.md`;
- `docs/development/requirements-coverage.md`;
- `tools/requirements/**`;
- Assurance-/Derivation-Contracts.

Für direkten Main-Workflow liefert CI zunächst post-commit einen reproduzierbaren Status. Falls später PR-/Branch-Schutz real genutzt wird, kann derselbe Check als Required Check dienen; dafür ist keine neue Validatorlogik nötig.

## 10. Skill-/Agent-Integration später

Ein späterer `requirements-assurance` Skill darf:

1. aktuellen Repo-State lesen;
2. Requirement-Candidate/Record vorbereiten;
3. Validator ausführen;
4. Findings erklären;
5. deterministic auto-fixes nur für eindeutig mechanische Fälle anwenden;
6. fachliche/Owner-Entscheidungen als Handoff ausweisen.

Er darf nicht:

- Validatorergebnis ohne tatsächlichen Lauf behaupten;
- Domain Authority erfinden;
- `unresolved` in plausible Gewissheit umschreiben;
- fachliches Review durch Modellselbstprüfung ersetzen.

## 11. Quality-Szenarien v0.1

### QS-01 – neuer aktiver Requirement-Record ohne Domain Authority

**Erwartung:** FAIL, bevor Implementation/Verification als valide weitergeführt wird.

### QS-02 – Dependency auf unbekannte ID

**Erwartung:** FAIL mit Ziel-ID und Quellrecord.

### QS-03 – neues Requirement fehlt im Delivery Ledger

**Erwartung:** FAIL `coverage-drift`.

### QS-04 – `verified` ohne Verification Evidence

**Erwartung:** FAIL.

### QS-05 – Requirement fachlich möglicherweise schlecht begründet, aber formal vollständig

**Erwartung:** Harness darf keinen wissenschaftlichen PASS behaupten; höchstens `formal-conformance: pass`, Domain Review separat.

## 12. Promotion / Scope

Ein Harness-PASS bedeutet ausschließlich:

> **formal requirements conformance for the implemented rule set**

Es bedeutet nicht:

- wissenschaftlich korrekt;
- fachlich vollständig;
- architecture-fit;
- independent validated;
- vollständig implementiert.

Diese semantische Grenze muss in CLI/CI-Ausgabe sichtbar bleiben.
