# Pilot #86 – Shared Research State unter wechselnden Forschungsfragen

**Status:** `reframed / owner-accepted / prototype-88-complete / branch-isolated / no-main-authority`  
**Branch:** `pilot/explorative-research-network-20260907`  
**Work Owner:** #86  
**Independent Review:** #87 → `reframe`  
**Prototype:** #88 → minimaler Falsifikationstest durchgeführt  
**Evaluation:** #89 → nächster Gate  
**Owner-Entscheidung:** 2026-09-07 → kleinen realen Ranis-Test weiterführen

## Aktueller Zweck

Der Pilot prüft jetzt **kein neues „exploratives Forschungsnetz“ und kein persistentes `Research Module`-Modell mehr**.

Nach Review #87 lautet die verbleibende, engere Frage:

> Reicht der bereits vorhandene Histo-Orla-Research-State aus, wenn dieselbe Evidenz unter wechselnden Forschungsfragen/Work Contexts wiederverwendet wird, Analyse und Synthese rekursiv arbeiten, der Maßstab kontrolliert wechselt und unterschiedliche Views aus demselben State abgeleitet werden?

Der reale Stressfall bleibt Ranis/Orlatal. Der Pilot bleibt ergebnisoffen und darf insbesondere als Erfolg ergeben, dass **keine neue Struktur nötig ist**.

## Aktueller Kern

```text
provenance-sicherer Canonical Research State
        ↕
aktuelle Research Questions / Work Contexts
        ↕
Source-/Instance-/Observation-/Finding-Arbeit
        ↕
Method-/Competence Routing
        ↕
Analyse / Synthese / Research Hooks
        ↕
kontrollierter Scale Shift
        ↕
abgeleitete Views
```

Eine Forschungsfrage referenziert Evidenz; sie besitzt sie nicht. Dafür wird im aktuellen Pilot **kein eigener Research-Module-Datentyp** benötigt.

## Review- und Prototype-Ergebnis

### #87 – unabhängiges Review

Kanonisch:

[`review-87.md`](review-87.md)

Verdict: `reframe`.

Insbesondere:

- vorhandene Histo-Orla-Mechanismen decken den Kern weitgehend;
- persistente `Research Modules` sind nicht belegt und stehen in Spannung zum jüngeren #63-Owner-Feedback;
- eigene `split | fuse | reframe | supersede | defer`-Semantik bleibt `defer`;
- neue Relationsschichten werden nicht promoted;
- Ranis bleibt als realer heterogener Stresstest sinnvoll.

### #88 – minimaler realer Ranis-Test

Kanonisch:

[`prototype-88.md`](prototype-88.md)

Ergebnis:

`PASS – existing mechanisms sufficient for this slice`.

Der Test verwendet eine direkt erneut inspizierte wissenschaftliche Ranis-Quelle und zeigt:

- Source/Instance/Findspot/Observation/Finding bleiben getrennt;
- dieselbe Evidence-ID wird in zwei unterschiedlichen Work Contexts referenziert, ohne Kopie;
- ein source-lokales Finding erzeugt einen Synthese-Candidate und eine nächste Prüfspur;
- der Scale Shift erzeugt Evidence Demand, keine historische Regionalbeziehung;
- Method Debt bleibt sichtbar;
- zwei Views referenzieren denselben State;
- ein eigenes `Research Module` oder eine Question-State-Machine war nicht nötig.

Zusätzlicher realer Negativtest: Die unter #85 dokumentierten Museumsfotos besitzen bekannte Metadaten, ihre Bildbytes sind im frischen Context aber nicht direkt verfügbar. Das ist ein `REQ-STATE-003`-Availability-Blocker, kein neuer Requirement-Gap.

## Authority / Präzedenz innerhalb dieses Pilotordners

Bei Widerspruch gilt für den aktuellen Pilotstand:

1. #86 aktueller Work-Owner-Status und Owner-Entscheidung;
2. [`review-87.md`](review-87.md);
3. [`prototype-88.md`](prototype-88.md);
4. dieser README;
5. ältere Pilot-Design-Dokumente (`model.md`, `workflows.md`, `stress-case-ranis-orlatal.md`, `review-and-eval.md`, `learnings.md`, `handoff.md`) als **pre-review candidate history**.

Die älteren Dokumente werden nicht rückwirkend als aktuelle Semantik gelesen, wenn sie `Research Modules`, alle fünf Question Operations oder eine Relations-Taxonomie als Zielmodell voraussetzen.

## Aktuelle Nicht-Ziele

- keine Master-Forschungsfrage erzwingen;
- kein Research-Module-Datentyp;
- keine neue Question-State-Machine;
- keine neue Relationsontologie;
- keine Graph-/DB-/Agentenarchitektur aus diesem Pilot ableiten;
- keine historische Kontinuität zwischen ko-lokalen Schichten behaupten;
- keine Method Truth aus AI/Pilotplausibilität erzeugen;
- keine Requirement-/Architecture-/`main`-Promotion vor #89 + Owner-Disposition.

## Nächster Gate

#89 evaluiert den **reframed** Pilot in frischem Kontext. `aktive Module` sind dabei als aktuelle `Research Questions / Work Contexts` zu lesen.

Danach entscheidet #86 nur noch über:

`archive pilot | keep case-specific | gezielt vorhandene Delivery-Friktion routen`.

Eine Promotion neuer wissenschaftlicher Struktur ist nach #87/#88 derzeit nicht begründet.
