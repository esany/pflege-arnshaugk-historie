# Requirements Assurance Harness

Work Owner: #62  
Requirements Owner: #42  
Technical Lead: #48

Dieser Ordner enthält die **deterministische formale QA** für Histo-Orla-Requirements.

Er prüft keine historische Wahrheit und ersetzt weder Domain Method Review (#60) noch Owner-/Fachentscheidungen.

## Komponenten

- `requirement-record.schema.json` – JSON Schema Draft 2020-12 für strukturierte QA-/Traceability-Records;
- `data/records.json` – inkrementelle machine-readable QA-Projektion aktiv bearbeiteter Requirements;
- `validate.py` – Cross-Record-/Repo-Validator;
- `requirements.txt` – kleine Python-Abhängigkeit für JSON Schema;
- `tests/` – positive/negative Fixtures und Regressionstests.

Kanonischer fachlicher Requirement-Text bleibt in:

- `docs/research/synthesis/requirements-baseline.md`
- `docs/research/synthesis/requirements-extensions.md`

Der strukturierte Record dupliziert nicht Statement/Rationale/SOTA, sondern hält operationalisierte QA-Metadaten wie Authorities, Dependencies und Verification-Klassen.

## Lokal ausführen

```bash
python -m pip install -r tools/requirements/requirements.txt
python tools/requirements/validate.py
```

Maschinenlesbar:

```bash
python tools/requirements/validate.py --json
```

Warnungen ebenfalls als Gate behandeln:

```bash
python tools/requirements/validate.py --strict-warnings
```

## Bedeutungsgrenze des Ergebnisses

`PASS` bedeutet ausschließlich:

> formal requirements conformance for the implemented deterministic rules

Es bedeutet ausdrücklich **nicht**:

- fachwissenschaftlich korrekt;
- fachlich vollständig;
- unabhängig validiert;
- vollständig implementiert;
- automatisch architecture-fit.

## Incremental Migration

Der Validator extrahiert bereits alle accepted Requirement-IDs aus Baseline + Extensions und vergleicht sie vollständig mit `docs/development/requirements-coverage.md`.

Ein reich strukturierter QA-Record ist v0.1 zwingend, sobald der Delivery-Status eines Requirements einer der folgenden ist:

```text
in-progress
implemented
verified
partial
blocked
owner-deferred
```

Für `not-started` und `research-needed` ist ein fehlender Record zunächst Warnung/Migration Debt, kein Hard Error.

Dadurch wird aktive technische Arbeit abgesichert, ohne vorab alle Legacy-Requirements umzuschreiben.

## Neue Rule hinzufügen

1. prüfen, ob die Regel **formal/deterministisch** ist;
2. Rule-ID vergeben und im Assurance Contract dokumentieren;
3. Regel im Validator oder Schema implementieren;
4. mindestens einen negativen Fixture/Test hinzufügen;
5. sicherstellen, dass die Rule keine fachliche Wahrheit simuliert;
6. bei materieller Scope-/Semantikänderung zurück an #42/#60 statt im Validator erfinden.

## Skill / AI

Ein Skill/LLM darf den Validator aufrufen, Findings erklären und mechanische Fix-Candidates erzeugen. Es darf niemals einen Validatorlauf behaupten, der nicht stattgefunden hat, oder einen formalen PASS als fachwissenschaftliche Validierung ausgeben.
