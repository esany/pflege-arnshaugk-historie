# Histo-Orla – Value / Decision / Delivery / Feedback Assurance Spine

**Status:** `working technical contract / v0.1`  
**Work Owner:** #63  
**Upstream:** #28 Problem/Need/Pain, #42 Requirements, #9 Governance  
**Technical Lead / Delivery:** #48 / #59  
**Related Assurance:** #62 Requirements Assurance, #54 Invariants, #61 Handoff/Conformance

## 1. Problem

Formale Requirements-QA allein garantiert noch nicht, dass technische Entscheidungen und Implementierungen dauerhaft auf den eigentlichen Forschungsnutzen rückführbar bleiben.

Histo-Orla braucht eine durchgängige, KI-unabhängige Traceability:

```text
Goal / Need / Pain
→ accepted Requirement / Constraint
→ technische Entscheidung / begründete Nicht-Entscheidung
→ Implementation
→ Verification
→ reale Nutzung / Owner-Feedback
→ bestätigt | Pain bleibt | Regression | neuer Need | Requirement-Delta
```

Issues und Markdown bleiben Work Owner bzw. menschenlesbare kanonische Semantik. Formal geklärte Beziehungen und Schutzregeln werden zusätzlich maschinenprüfbar projiziert.

## 2. Leitprinzip

> **Code darf weder die fachliche Bedeutung noch Nutzerbedürfnisse erfinden. Code muss aber erzwingen können, dass materielle technische Arbeit ihre gültige Begründungs-, Governance-, Verification- und Feedback-Kette nicht verliert.**

Ein formaler PASS bedeutet nur `traceability/conformance for implemented rules`, nicht fachliche oder wissenschaftliche Richtigkeit.

## 3. Responsibility Split

- `#28/#46/#47/#60` besitzen Problem-, Pain-, Research- und Method-Truth.
- `#42` besitzt accepted Requirements und ihren Lifecycle.
- `#9/AGENTS.md` besitzen bindende Governance.
- `#48` besitzt technische Derivation und reversible technische Entscheidungen.
- `#59` besitzt Implementation/Verification.
- `#63` besitzt nur die deterministische Traceability-/Non-Regression-QA zwischen diesen Ebenen.
- Der Research Owner besitzt Ziel-/Nutzenpriorität und tatsächliches Nutzerfeedback; Feedback ist Evidence für Produkt-/Workflow-Fit, nicht automatisch wissenschaftliche Evidence.

## 4. Machine-readable Projections

V0.1 führt nur formale Referenzen/Status, keine zweite inhaltliche Wahrheit:

### A. Governance Registry

Stabile IDs für bindende/controlling Regeln, z. B. `GOV-AGENTS`, `GOV-NONREG`, `GOV-RESEARCH-QA`, `GOV-SOURCE-ID`.

### B. Decision / Delivery Records

Materielle technische Entscheidung oder Implementierung:

```text
id
kind = decision | implementation
status
materiality
requirement_refs[]
driver_refs[]       # G-* / N-* / P-*
governance_refs[]
decision_refs[]     # implementation -> decision, wenn materiell nötig
implementation_files[]
verification_refs[]
owner_decision_ref  # wenn Scope/Qualität/Normativität betroffen
notes
```

### C. Feedback Records

Reale Nutzung / Research-Owner-Feedback:

```text
id
kind = feedback
status
source_ref
requirement_refs[]
driver_refs[]
implementation_refs[]
outcome = confirms | pain-persists | regression | new-pain | new-need | requirement-change | no-change
requires_delta = true | false
delta_refs[]
notes
```

Feedback darf weder Requirement Truth noch Code still ändern. Ein materieller Delta geht kontrolliert zurück an #42 bzw. bei Ziel-/Owner-Entscheidungen an den zuständigen Owner.

## 5. Deterministic Rules v0.1

### Value / Requirement Trace

- jeder `decision`-/`implementation`-Record referenziert mindestens ein accepted `REQ-*`;
- jeder materielle technische Record referenziert mindestens einen validen `G-* | N-* | P-*` Driver oder bezieht diesen transitiv aus einem strukturierten Requirement-Record;
- referenzierte Requirement-/Driver-IDs müssen existieren;
- `requirement_refs` dürfen nicht auf unbekannte/entfernte IDs zeigen.

### Governance

- jeder technische Decision-/Implementation-Record enthält die global verpflichtenden Governance-Refs;
- tag-/scope-spezifische Governance kann durch Policy-Regeln zusätzlich verlangt werden;
- eine materielle Scope-/Qualitätsreduktion braucht explizite Owner-/Decision-Referenz; Lean/Agile ist niemals implizite Reduktionsbegründung.

### Decision / Implementation

- `implementation` mit `materiality=material` braucht einen `decision_ref` oder eine explizite `decision_not_required_reason` für rein mechanische/reversible Arbeit;
- `implemented/verified` darf nicht ohne Implementation-/Verification-Referenz behauptet werden;
- technische Dateien können in CI gegen `implementation_files` geprüft werden; neue produktive Codepfade ohne Trace-Record sind Fehler, sobald ihr Pfad unter dem kontrollierten Technical Scope liegt.

### Feedback Loop

- `owner-workflow-acceptance` kann nicht allein durch technischen Test erfüllt werden;
- `pain-persists | regression | new-pain | new-need | requirement-change` mit `requires_delta=true` braucht sichtbare `delta_refs` oder Status `open/unresolved`;
- Nutzerfeedback darf nicht als wissenschaftliche Evidence etikettiert werden;
- `verified` Systemverhalten bleibt revidierbar, wenn reale Nutzung einen Widerspruch/Regression zeigt.

## 6. Was nicht deterministisch entschieden wird

- ob ein Need/Pain inhaltlich richtig verstanden wurde;
- ob ein Requirement wissenschaftlich hinreichend ist;
- ob eine technische Option fachlich die beste ist;
- ob Nutzerfeedback eine historische Aussage bestätigt;
- welche neue Requirement-Semantik aus Feedback folgt.

Der Validator prüft nur, dass die zuständigen Authority-/Review-/Delta-Pfade benutzt werden.

## 7. Changed-code Guard

Ziel für CI:

```text
relevante technische Datei geändert
→ gehört zu mindestens einem Implementation Record
→ Implementation Record -> accepted Requirement(s)
→ Requirement/Record -> Goal/Need/Pain
→ erforderliche Governance vorhanden
→ Verification/Feedback je Status vorhanden
```

Assurance-Selbstcode und rein dokumentarische Änderungen können explizit ausgenommen oder über einen eigenen bootstrap Record geführt werden. Die kontrollierten technischen Pfade werden in einer kleinen Policy-Datei konfiguriert statt in Prompts versteckt.

## 8. Skill / Agent UX

Ein späterer Skill ist sinnvoll als Bedienoberfläche:

1. Work Context lesen;
2. betroffene Needs/Pains/Requirements ermitteln;
3. Decision-/Implementation-Record vorbereiten;
4. Validator real ausführen;
5. Fehler erklären;
6. eindeutige mechanische Korrekturen anwenden;
7. echte fachliche/Owner-Entscheidungen zurückgeben;
8. nach realer Nutzung Feedback aufnehmen und Delta routen.

Der Skill darf niemals selbst einen Validator-PASS, Owner-Acceptance oder fachliche Validation erfinden.

## 9. Einführung

Keine Big-Bang-Migration.

1. #62 bleibt Requirements-Formal-QA.
2. #63 ergänzt die downstream/upstream Value-/Decision-/Delivery-/Feedback-Traceability.
3. Zuerst werden neue materielle technische Änderungen erfasst.
4. Bestehende historische Decisions/Implementationen werden nur migriert, wenn sie erneut relevant werden.
5. Jede neue Hard Rule braucht Rule-ID + mindestens einen negativen Regressionstest.

## 10. Success Criteria

Der Mechanismus ist nützlich, wenn ein frischer Bearbeiter bzw. CI ohne Chat nachvollziehen kann:

```text
Warum existiert diese Änderung?
Welches Nutzerproblem / Ziel trägt sie?
Welches Requirement legitimiert sie?
Welche Governance begrenzt sie?
Welche Entscheidung führte zur Umsetzung?
Woran wurde sie verifiziert?
Was sagte reale Nutzung?
Welche offenen Deltas folgen daraus?
```

## 11. CI-Hygiene und atomare Änderungsgrenzen

CI soll reale Inkonsistenzen finden, aber nicht durch die Art unserer Repository-Schreibvorgänge künstlich rote Zwischenstände erzeugen.

Verbindlich für gekoppelte Änderungen:

- Dateien, die gemeinsam eine formale Invariante erfüllen müssen (z. B. Requirement + Coverage + strukturierter Record), werden **atomar in einem Commit** aktualisiert oder zunächst auf einem Work Branch vollständig hergestellt und erst als konsistenter Stand gegen `main` geprüft;
- absichtlich inkonsistente Zwischenstände werden nicht auf `main` geschrieben, nur damit der nächste Commit sie wieder repariert;
- negative Fixtures und erwartete Fail-Cases gehören in isolierte Tests, nicht als kurzlebiger kaputter Projektzustand auf `main`;
- Workflow-Scope wird so getrennt, dass Requirements-only-Änderungen primär durch #62 und sonstige technische/Value-Trace-Änderungen primär durch #63 geprüft werden; unnötig doppelte automatische Läufe sind zu vermeiden;
- ein echter CI-Fehler bleibt fail-closed und sichtbar; Benachrichtigungsrauschen ist kein Grund, harte Checks weichzuschalten.

Die E-Mail-/Web-Zustellung von GitHub-Actions-Benachrichtigungen ist eine GitHub-Kontoeinstellung und keine Projekt-Truth. Das Repository minimiert vermeidbare Fehl- und Doppelläufe; ob GitHub erfolgreiche/fehlgeschlagene Läufe per E-Mail meldet, bleibt außerhalb des Repositorys konfigurierbar.

> **Need/Pain/Goal bleiben Produkt- und Forschungsursprung. Requirements operationalisieren das Was. Technik entscheidet nur das Wie. Reale Nutzung schließt die Schleife.**
