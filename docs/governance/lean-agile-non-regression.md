# Histo-Orla – Lean/Agile Non-Regression & Quality Contract

**Status:** `binding governance / owner-clarified 2026-08-31`  
**Governance Owner:** #9  
**Requirements / Acceptance Owner:** #42  
**Technical Delivery Owner:** #48 / #59

## 1. Zweck

Dieses Dokument verhindert eine wiederholt sichtbare Fehlinterpretation: Begriffe wie `lean`, `agil`, `privat`, `MVP`, `Walking Skeleton`, `Greenfield` oder `build now` dürfen **nicht** als Signal verstanden werden, bereits erarbeitete Anforderungen, wissenschaftliche Qualität, technische Qualität oder State-of-the-Art-/Best-Practice-Verpflichtungen zurückzusetzen.

> **Lean optimiert Mittel, Reihenfolge, Reversibilität und Time-to-Value – nicht die fachlichen oder technischen Akzeptanzmaßstäbe.**

## 2. Non-Regression-Regel

Die bereits akzeptierte Requirements-/Quality-/Governance-Basis bleibt gültig, bis sie **explizit und nachvollziehbar** geändert, ersetzt oder vom Owner aus dem Scope genommen wird.

Für den privaten MVP gilt als Acceptance-Basis mindestens die Vereinigung aus:

1. `docs/research/synthesis/requirements-baseline.md` / #42;
2. `docs/research/synthesis/mvp-acceptance.md`;
3. bindenden Governance-, Source-Identity-, Evidence-, Handoff-, Rights- und Quality-Constraints;
4. den vom Owner akzeptierten Systemanforderungen aus Domain-/Live-Research und Domain-Method-Arbeit (#46/#47/#60), sobald sie als Systemanforderung formuliert sind;
5. späteren explizit akzeptierten Acceptance-Deltas unter #42.

Ein neuer Begriff, eine neue Projektphase, ein Tool, Framework, Architekturpattern oder Prozessmodell **superseded diese Baseline niemals implizit**.

Materielle Scope-/Qualitätsreduktion benötigt:

```text
konkretes betroffenes Requirement / Acceptance Criterion
→ Grund
→ Konsequenz / wissenschaftlicher oder technischer Verlust
→ Alternative
→ explizite Owner-Entscheidung
→ Traceability im kanonischen Requirements-/Decision-State
```

Ohne diesen Pfad gilt die bestehende Anforderung fort.

## 3. Lean / Agile – verbindliche Bedeutung

### Lean bedeutet

- kleinste **hinreichende** Lösung statt maximaler Infrastruktur;
- bestehende Tools, Standards und Libraries vor Eigenbau;
- keine Funktion/Komponente ohne realen Requirement-/Acceptance-Bezug;
- kurze diskriminierende Research-/Spike-Schritte statt monatelanger Voranalyse;
- reversible Entscheidungen früh treffen, teure Lock-ins spät;
- unnötige Duplikation, Parallel-Truth-Stores und Future-Proof-Komplexität vermeiden;
- technische und organisatorische Verschwendung reduzieren.

### Lean bedeutet ausdrücklich nicht

- halbe wissenschaftliche Standards;
- reduzierte Evidenz-/Provenienzqualität;
- Weglassen akzeptierter Systemfähigkeiten, nur weil sie schwierig sind;
- `happy path only`, wenn Failure-/Uncertainty-Verhalten Teil der Acceptance ist;
- Prototypqualität als fertigen MVP ausgeben;
- SOTA-/Best-Practice-Prüfung überspringen;
- fachliche Unklarheit durch technische Vereinfachung auflösen.

### Agil bedeutet

- kleine vertikale Inkremente;
- reale Nutzung früh;
- Anforderungen durch reale Forschung weiter schärfen;
- kontinuierliches Refactoring und technische Debt-Steuerung;
- kontinuierliche Verification gegen Acceptance Criteria;
- Architecture/Research just in time dort vertiefen, wo eine konkrete Entscheidung es braucht.

### Agil bedeutet ausdrücklich nicht

- Anforderungen beliebig verändern;
- ohne Traceability neu interpretieren;
- Qualität auf später verschieben, wenn sie für den aktuellen Slice relevant ist;
- jeden neuen Impuls zum Phasen-/Architekturreset machen.

## 4. Qualitätsregel für Inkremente

Ein frühes Inkrement darf **klein in der Breite**, aber nicht falsch in der Tiefe sein.

Beispiel:

- ein erster Slice muss noch nicht OCR, alle Domain Profiles und alle Integrationen besitzen;
- wenn er aber `Source → inspected Instance → Findspot → Observation` behauptet, müssen diese Ebenen im Slice korrekt getrennt, persistiert und auditierbar sein;
- wenn eine Fähigkeit noch fehlt, wird sie sichtbar als `not implemented / partial / unavailable / research-debt` geführt und nicht durch vereinfachte Semantik simuliert.

Daraus folgt:

```text
small scope
+ full correctness for claimed scope
+ explicit missing scope
+ no hidden epistemic/technical loss
= acceptable early increment
```

`MVP complete` ist erst erreicht, wenn die gesamte aktive private MVP-Acceptance erfüllt ist.

## 5. State of the Art / Best Practice

Wissenschaftliche und technische Entscheidungen basieren auf dem jeweils einschlägigen **State of the Art und Best Practice**, proportional zur Tragweite der Entscheidung.

Das bedeutet:

- Fachmethodik: einschlägige Fach-SOTA, Methodenliteratur, Standards und reale Quellenvalidierung;
- Software/Architektur: aktuelle etablierte Patterns, Standards, Libraries/Tools, Security-/Testing-/Data-/IR-/AI-Best-Practices;
- Integration: offizielle APIs/Contracts und Providergrenzen prüfen;
- kritische Unknowns: benchmarken/spiken statt raten;
- reversible Detailentscheidungen: kurze, zielgerichtete Prüfung statt Vollstudie;
- schwer reversible/teure/rights-/lock-in-relevante Entscheidungen: vertiefter Vergleich / ADR.

> **Just-in-time Research reduziert Vorlauf, nicht Qualitätsanspruch.**

## 6. Verantwortung des Technical Lead (#48)

#48 führt Delivery **gegen den vollständigen akzeptierten Scope**, nicht nur gegen den aktuell bequemsten Slice.

Er muss:

1. den vollständigen Acceptance-/Requirements-Scope kennen;
2. ihn in einen priorisierten technischen Backlog übersetzen;
3. Dependencies, Risiko und kleinste nutzbare Verticals bestimmen;
4. pro technischer Entscheidung geeigneten SOTA/Best Practice prüfen;
5. vorhandene Lösungen vor Eigenbau bewerten;
6. reversible Entscheidungen selbstständig treffen und später refactoren;
7. wissenschaftliche/technische Acceptance-Tests mitliefern;
8. fehlende/noch nicht implementierte Kriterien sichtbar halten;
9. Fach-/Requirements-Fragen an ihre Owner zurückgeben statt sie zu erfinden;
10. keine Acceptance still streichen, vertagen oder abschwächen.

### Pflichtstatus je Acceptance Criterion

Der Delivery-State muss für jedes aktive Kriterium mindestens unterscheiden können:

```text
not-started
in-progress
implemented
verified
partial
blocked
research-needed
owner-deferred
```

`owner-deferred` darf nur nach expliziter Owner-Entscheidung verwendet werden. `nicht jetzt` aus technischer Priorisierung bedeutet **nicht** `nicht MVP`.

## 7. Schutz gegen semantischen Reset / Buzzword Drift

Neue Formulierungen des Nutzers werden zunächst **kompatibel mit dem bestehenden kanonischen State interpretiert**.

Beispiel:

```text
"lean und agil"
```

bedeutet bei bestehender hoher Qualitätsbaseline:

```text
bestehende Anforderungen vollständig erhalten
+ Umsetzung priorisieren
+ kleine Verticals
+ bestehende Tools bevorzugen
+ Reversibilität maximieren
+ Research/Architecture just in time
```

und **nicht**:

```text
Requirements zurücksetzen
oder
Qualitätsmaßstab reduzieren
oder
nur Minimalfunktion liefern
```

Wenn eine neue Nutzeräußerung tatsächlich im Konflikt mit bestehender Acceptance steht, wird der Konflikt **explizit benannt** und als Scope-/Decision-Delta behandelt; es erfolgt kein stiller Reset.

## 8. Verhältnis Domain ↔ Requirements ↔ Dev

```text
Owner-Vision / bisher accepted System Needs
        ↓
Domain Research + Method SOTA
        ↕
#42 Requirements / MVP Acceptance
        ↓
#48 Technical Lead: leanste hochwertige Umsetzung
        ↓
#59 Implementierung / Verification
        ↕
reale Nutzung #46/#47
        ↓
Acceptance-Delta / Verbesserung
```

- Domain besitzt Fachwahrheit/Method Truth, nicht den Stack.
- #42 besitzt Requirements/Acceptance, nicht Fachwahrheit oder Implementierung.
- #48/#59 besitzen technische Mittel, Priorisierung und Umsetzung, nicht Scope-Reduktion oder fachliche Semantik.
- Der Owner darf Scope/Acceptance ändern; materielle Reduktionen werden explizit dokumentiert.

## 9. Handoff / Restartability

Ein neuer Dev-/Architecture-Chat muss ohne alte Chat-Historie erkennen können:

- vollständige aktive MVP-Acceptance;
- aktuellen Slice;
- was bereits `implemented/verified` ist;
- was noch fehlt und warum;
- welche Anforderungen aktuell nur später priorisiert, aber **nicht gestrichen** sind;
- welche SOTA-/ADR-/Research-Fragen für die nächste Entscheidung nötig sind.

## 10. Leitformeln

> **Lean heißt kleinste hinreichende Lösung – nicht kleinster Anspruch.**

> **Agil heißt inkrementell vollständig werden – nicht Anforderungen vergessen.**

> **Ein Slice darf klein sein; seine behauptete Wissenschaft und Technik müssen stimmen.**

> **State of the Art und Best Practice sind Basis der Mittelwahl, nicht optionale Veredelung.**

> **Neue Buzzwords ändern keinen akzeptierten Scope ohne explizites Delta.**
