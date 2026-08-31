# Histo-Orla – Lean/Agile Non-Regression & Quality Contract

**Status:** `binding governance / owner-clarified 2026-08-31`  
**Governance Owner:** #9  
**Requirements Owner:** #42  
**Technical Lead / Development:** #48 / #59

## 1. Zweck

Begriffe wie `lean`, `agil`, `privat`, `Greenfield`, `Vertical Slice`, neue Tools oder neue Architekturpatterns dürfen **nicht** als Signal verstanden werden, bereits erarbeitete Anforderungen, wissenschaftliche Qualität, technische Qualität oder State-of-the-Art-/Best-Practice-Verpflichtungen zurückzusetzen.

> **Lean optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value – nicht die fachlichen oder technischen Akzeptanzmaßstäbe.**

## 2. Non-Regression

Die akzeptierte Requirements-/Quality-/Governance-Basis bleibt gültig, bis sie explizit und nachvollziehbar geändert, ersetzt oder vom Owner aus dem Scope genommen wird.

Aktive Systemanforderungen bestehen mindestens aus:

1. `docs/research/synthesis/requirements-baseline.md`;
2. `docs/research/synthesis/requirements-extensions.md`;
3. bindenden Governance-, Source-Identity-, Evidence-, Handoff-, Rights- und Quality-Constraints;
4. späteren explizit akzeptierten Deltas unter #42.

Ein neuer Begriff, eine neue Projektphase, ein Tool, Framework, Architekturpattern oder Prozessmodell superseded diese Basis niemals implizit.

Materielle Scope-/Qualitätsreduktion benötigt:

```text
konkretes betroffenes Requirement
→ Grund
→ Konsequenz / wissenschaftlicher oder technischer Verlust
→ Alternative
→ explizite Owner-Entscheidung
→ Traceability im kanonischen Requirements-/Decision-State
```

## 3. Lean / Agile – verbindliche Bedeutung

### Lean bedeutet

- kleinste **hinreichende** Lösung statt maximaler Infrastruktur;
- bestehende Tools, Standards und Libraries vor Eigenbau;
- keine technische Komponente ohne realen Requirement-/Quality-Bezug;
- kurze diskriminierende Research-/Spike-Schritte statt unnötiger Voranalyse;
- reversible Entscheidungen früh, teure Lock-ins spät;
- Duplikation und Parallel-Truth-Stores vermeiden.

### Lean bedeutet ausdrücklich nicht

- halbe wissenschaftliche Standards;
- reduzierte Evidenz-/Provenienzqualität;
- Weglassen akzeptierter Fähigkeiten, nur weil sie schwierig sind;
- Prototyp-/Happy-Path-Qualität als Erfüllung ausgeben;
- SOTA-/Best-Practice-Prüfung überspringen;
- fachliche Unklarheit durch technische Vereinfachung auflösen.

### Agil bedeutet

- kleine, fachlich korrekte Inkremente;
- reale Nutzung früh;
- Anforderungen durch reale Forschung weiter schärfen;
- kontinuierliches Refactoring und Debt-Steuerung;
- kontinuierliche Verification gegen Requirements;
- Architecture/Research just in time dort vertiefen, wo eine konkrete Entscheidung es braucht.

### Agil bedeutet ausdrücklich nicht

- Anforderungen beliebig verändern oder vergessen;
- ohne Traceability neu interpretieren;
- Qualität auf später verschieben, wenn sie für den aktuellen Umfang relevant ist;
- jeden neuen Impuls zum Phasen-/Architekturreset machen.

## 4. Qualitätsregel für Inkremente

Ein frühes Inkrement darf klein in der Breite, aber nicht falsch in der Tiefe sein.

Wenn ein Inkrement z. B. `Source → inspected Instance → Findspot → Observation` unterstützt, müssen diese Ebenen innerhalb dieses Umfangs fachlich korrekt, persistent und auditierbar sein. Fehlende Fähigkeiten werden als `not-started | partial | blocked | research-needed` sichtbar gehalten und nicht durch vereinfachte Semantik simuliert.

```text
small scope
+ full correctness for claimed scope
+ explicit missing scope
+ no hidden epistemic/technical loss
= acceptable increment
```

## 5. State of the Art / Best Practice

Wissenschaftliche und technische Entscheidungen basieren auf dem jeweils einschlägigen **State of the Art und Best Practice**, proportional zur Tragweite der Entscheidung.

- Fachmethodik: einschlägige Fach-SOTA, Methodenliteratur, Standards und reale Quellenvalidierung;
- Software/Architektur: aktuelle etablierte Patterns, Standards, Libraries/Tools, Security-/Testing-/Data-/IR-/AI-Best-Practices;
- Integration: offizielle APIs/Contracts und Providergrenzen;
- kritische Unknowns: benchmarken/spiken statt raten;
- reversible Detailentscheidungen: kurze zielgerichtete Prüfung;
- schwer reversible/teure/rights-/lock-in-relevante Entscheidungen: vertiefter Vergleich / ADR.

> **Just-in-time Research reduziert Vorlauf, nicht Qualitätsanspruch.**

## 6. Verantwortung des Technical Lead (#48)

#48 führt technische Arbeit gegen den vollständigen akzeptierten Requirement-Scope. Er priorisiert Mittel und Reihenfolge, nicht den fachlichen Anspruch.

Er muss:

1. vollständige Requirements-Coverage kennen und sichtbar halten;
2. technischen Backlog nach fachlichem Nutzen, Risiko und Dependency ordnen;
3. pro konkreter Entscheidung geeigneten SOTA/Best Practice prüfen;
4. bestehende Lösungen vor Eigenbau bewerten;
5. reversible Entscheidungen selbstständig treffen und refactoren;
6. Acceptance-/Regression-/Invariant-Tests mitliefern;
7. fehlende Kriterien sichtbar halten;
8. Fach-/Requirements-Fragen an ihre Owner zurückgeben statt erfinden.

Delivery-Status je Requirement:

`not-started | in-progress | implemented | verified | partial | blocked | research-needed | owner-deferred`.

`owner-deferred` benötigt explizite Owner-Entscheidung.

## 7. Schutz gegen semantischen Reset

Neue Nutzerformulierungen werden zunächst kompatibel mit dem bestehenden kanonischen State interpretiert. Bei echtem Konflikt wird ein explizites Requirement-/Decision-Delta erzeugt; kein stiller Reset.

## 8. Verantwortlichkeiten

```text
Owner-Vision / Needs
        ↓
Domain Research + Method SOTA
        ↕
#42 Requirements
        ↓
#48 Technical Lead: leanste hochwertige Mittel
        ↓
#59 Implementierung / Verification
        ↕
reale Nutzung #46/#47
        ↓
Requirement-/Method-Delta
```

- Domain besitzt Fachwahrheit/Method Truth, nicht den Stack.
- #42 besitzt akzeptierte Systemanforderungen, nicht Fachwahrheit oder Implementierung.
- #48/#59 besitzen technische Mittel, Priorisierung und Umsetzung, nicht Scope-Reduktion oder fachliche Semantik.

## 9. Leitformeln

> **Lean heißt kleinste hinreichende Lösung – nicht kleinster Anspruch.**

> **Agil heißt inkrementell vollständig werden – nicht Anforderungen vergessen.**

> **Ein Inkrement darf klein sein; seine behauptete Wissenschaft und Technik müssen stimmen.**

> **State of the Art und Best Practice sind Basis der Mittelwahl.**
