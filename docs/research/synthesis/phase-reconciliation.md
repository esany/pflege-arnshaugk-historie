# Histo-Orla – Phase Reconciliation: content-driven Research, Requirements & Technical Delivery

**Status:** `owner-resolved / active / 2026-08-31`  
**Requirements Owner:** #42  
**Technical Lead:** #48  
**Development / Verification:** #59  
**Domain Method Research:** #60  
**Live Research:** #46/#47

## 1. Owner-Entscheidung

Histo-Orla ist ein privates, leanes und agiles Forschungssystem. `MVP` wird **nicht mehr als kanonische Projektphase oder zusätzliche Requirement-Schicht verwendet**.

Die bisher erarbeiteten wissenschaftlichen, funktionalen, technischen, Governance- und Quality-Anforderungen bleiben vollständig wirksam. Live-/Domain-Research präzisiert und ergänzt sie. Die zentrale Frage ist nicht „Was gehört in den MVP?“, sondern:

> **Welche Anforderungen gelten, was ist fachlich bereits hinreichend verstanden, und mit welchen möglichst einfachen, hochwertigen und reversiblen Mitteln erfüllen wir sie?**

## 2. Aktuelle Arbeitslogik

```text
Live Research / reale Problem- und Quellenarbeit (#46/#47)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↕
Accepted Requirements + Extensions (#42)
        ↕
Technical Lead: SOTA / Best Practice / Existing Tools / Umsetzung (#48)
        ↕
Development & Verification (#59)
        ↓
reale Nutzung
        ↺
Findings / Method-/Requirement-/Technical Deltas
```

Es gibt kein monatelanges Vorab-Gate, aber auch keine künstliche Delivery-Phase, die die fachliche Arbeit verdrängt.

## 3. Was hart gilt

- Source / Representation / inspected Instance / Derivative / Findspot / Finding / Interpretation nicht still verschmelzen;
- AI output ist keine Evidenz und keine unabhängige Fachvalidierung;
- Unsicherheit / unresolved / contradiction sind zulässige Zustände;
- Fundstellen und Provenienz bleiben erhalten;
- formal prüfbare Invarianten werden deterministisch abgesichert, sobald ihre Semantik geklärt ist;
- kuratierter Research State ist chat-/providerunabhängig, exportierbar und restartbar;
- exakte/auditierbare Retrieval-Baseline funktioniert ohne LLM;
- Rights/Privacy/External Processing bleiben explizit;
- Research und Mediation bleiben getrennt;
- Domain Method Truth bleibt Eigentum der Fachdomäne (#60), nicht des Dev-Stacks;
- SOTA und Best Practice sind Basis der wissenschaftlichen und technischen Mittelwahl.

## 4. Requirements

Kanonisch:

- `docs/research/synthesis/requirements-baseline.md`;
- `docs/research/synthesis/requirements-extensions.md`;
- bindende Governance-/Source-/Evidence-/Rights-/Handoff-/Quality-Constraints.

Neue Domain-/Case-Befunde können Requirements präzisieren oder ergänzen. Sie reduzieren bestehende Requirements nicht still.

## 5. Technical Lead #48

#48 besitzt die technische Einordnung, Priorisierung und Umsetzung **unter** den akzeptierten Requirements.

### Darf / soll

- aktuelle technische SOTA-/Best-Practice-/Existing-Tool-Landschaft für konkrete Anforderungen prüfen;
- Anforderungen nach Dependency, Risiko, fachlichem Nutzen und Reversibilität in umsetzbare Inkremente schneiden;
- reversible Technologieentscheidungen selbstständig treffen und refactoren;
- Feasibility-Spikes/Benchmarks einsetzen, wenn sie reale Unknowns diskriminieren;
- technische Architecture/Contracts nur so tief vorziehen, wie für Integrität, Reversibilität, Sicherheit und Wartbarkeit erforderlich;
- Umsetzung und Tests eng an realen #46/#47-Fällen verifizieren.

### Darf nicht

- Fachsemantik/Method Truth erfinden;
- Requirements still abschwächen oder streichen;
- wissenschaftliche Unsicherheit durch technische Convenience eliminieren;
- Infrastruktur auf Vorrat aufbauen;
- irreversible/teure/lock-in-/rights-relevante Entscheidungen ohne explizite Begründung/ADR treffen.

## 6. Technical Delivery ist kein eigener Wissensowner

#59 implementiert und verifiziert akzeptierte Requirements. Es ist kein eigener Produkt-Scope und keine Phase, die #46/#47/#60 ersetzt.

Technische Arbeit beginnt dort, wo ein Requirement-/Constraint-Cluster hinreichend klar ist. Noch offene fachliche Semantik bleibt bei #60/#42 sichtbar und wird nicht technisch erfunden.

## 7. Just-in-time Architecture

Architekturarbeit findet laufend statt. Ein expliziter ADR unter #58 ist nur nötig, wenn eine Entscheidung materiell/schwer reversibel ist, z. B.:

- Persistenz-/Datenmodell-Lock-in;
- Cloud-/Provider-/Kosten-/Privacy-Lock-in;
- bedeutende Migration;
- Security-/Rights-Konsequenz;
- Optionen mit materiell unterschiedlichen wissenschaftlichen Verlusten.

Reversible Library-/Framework-/UI-Details brauchen keine große Vorab-Zeremonie.

## 8. Inhaltlicher Stand / nächste Prioritäten

### Domain / Research

1. #46/#47 reale Forschung fortführen.
2. #60: erster SOTA-Block Diplomatik/Urkundenlehre + Editionswissenschaft/Textkritik an realen NHUB-Fällen.
3. danach Archivistik/Provenienz/Registraturkunde und historische Philologie/Semantik.
4. neue fachlich belastbare Systembedarfe direkt unter #42 als Requirement Extensions führen.

### Technical parallel

5. #48 mappt aktive Requirements auf technische SOTA/Best Practice und vorhandene Werkzeuge.
6. #49 Zotero↔OneDrive read-first als konkrete Integrationsfrage weiter prüfen.
7. #50/#51 Source/Instance/Findspot/Provenienz technisch so einfach wie hinreichend absichern.
8. #53 Exact Search und #55 Audit früh dort umsetzen, wo sie reale Forschung unmittelbar tragen.
9. #57 Restartability/Research-ready Availability mit frischem Kontext testen.

## 9. Leitformeln

> **Requirements führen den Systemumfang; Lean/Agile optimiert die Mittel.**

> **Fachdomänen führen. Technologie dient.**

> **Dev informiert und implementiert Requirements; Dev besitzt Method Truth nicht.**

> **State of the Art und Best Practice sind Basis der Mittelwahl.**
