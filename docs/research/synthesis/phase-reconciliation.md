# Histo-Orla – Phase Reconciliation: Research/Requirements ↔ Technical Discovery

**Status:** `active-reassessment / 2026-08-31`  
**Work Owner:** #43 Architecture Readiness Reassessment  
**Requirements Owner:** #42  
**Technical Discovery / Engineering Advisory:** #48  
**Domain Method Research:** #60  
**Live Research:** #46/#47

## 1. Anlass

Der ursprüngliche Durchlauf #28–#43 hat in kurzer Folge aus dem damaligen Konzeptstand eine Discovery-/SOTA-/Requirements-Baseline v0.1 und anschließend das Gate `architecture-ready-with-bounded-research-debt` erzeugt.

Der danach vertiefte Live-Case #46 hat jedoch eine zuvor nicht hinreichend operationalisierte fachwissenschaftliche Mittelschicht sichtbar gemacht: Kompetenzlabels und cross-cutting Research-Regeln genügen nicht, um für konkrete Quellentypen die Fachmethodik, Inferenzgrenzen, Evidence Appetite, QA und transdisziplinären Handoffs nach dem State of the Art der jeweiligen Disziplin auszuführen. Diese Lücke ist jetzt Work Scope von #60.

Damit ist eine zentrale Aussage des ursprünglichen #43-Gates – dass keine versteckte fachliche Unklarheit in Architektur verschoben wurde – **falsifiziert bzw. mindestens erneut prüfpflichtig**. Das invalidiert nicht automatisch alle Requirements aus #42; es invalidiert aber die Annahme, dass die Requirements-/Methodenbasis bereits hinreichend vollständig für eine Zielarchitektur-/MVP-Entscheidung sei.

## 2. Was aus #28–#43 weiterhin belastbar ist

Weiterhin als starke cross-cutting Invarianten/accepted baseline behandeln, solange kein neuer Befund sie widerlegt:

- Source / Representation / inspected Instance / Derivative / Findspot / Finding / Interpretation nicht still verschmelzen;
- AI output ist keine Evidenz und keine unabhängige Fachvalidierung;
- Unsicherheit / unresolved / contradiction sind zulässige Zustände;
- Findspots und Provenienz müssen erhalten bleiben;
- formal prüfbare Invarianten sollen deterministisch erzwungen werden;
- kuratierter Research State soll chat-/providerunabhängig, exportierbar und restartbar sein;
- exakte/auditierbare Retrieval-Baseline darf nicht von LLM abhängen;
- Rights/Privacy/External Processing müssen getrennt admission-fähig sein;
- Research und Mediation bleiben getrennt.

Diese Punkte sind Architektur-Constraints/Requirements, aber noch keine Zielarchitektur.

## 3. Was neu als nicht ausreichend geklärt gilt

### 3.1 Problem-/Workflow-Discovery

#28/#29 sind v0.1-Synthesen aus dem damaligen Projektstand. Sie bleiben wertvoll, sind aber nicht mit umfassender empirischer Nutzer-/Workflow-Discovery gleichzusetzen. Insbesondere reale heutige Arbeitsabläufe, Häufigkeiten, Toolfriktionen, Quellenzugänge und Prioritäten sind teilweise weiterhin `observation-needed`.

### 3.2 Fachwissenschaftliche Operationalisierung

#60 zeigt, dass zwischen Kompetenzlandkarte (#22) und accepted Requirements (#42) eine eigene Schicht benötigt wird:

`Domain Method Profiles / Method Truth`.

Solange priorisierte Profile noch `scoping/method-candidate` sind, darf daraus kein endgültiges System-/Daten-/Workflowmodell abgeleitet werden.

### 3.3 Requirements Coverage

#42 bleibt eine accepted Baseline **v0.1**, aber ist erneut offen für Coverage-/Acceptance-Reconciliation aus #46/#47/#60. Neue Erkenntnisse sind zunächst Requirement Candidates; bestehende Requirements werden nur gezielt geändert, wenn Evidenz/Generalisierbarkeit dies trägt.

### 3.4 Softwaretechnologischer Stand

Das Repository ist technisch Greenfield:

- kein Anwendungscode / produktiver MVP;
- kein gewählter Runtime-/UI-/Backend-Stack;
- keine Persistenztechnologie entschieden;
- keine Search-/OCR-/Workflow-Technologie entschieden;
- keine empirisch validierte Zielarchitektur;
- keine belastbaren Performance-/Scale-SLOs.

Vorhanden sind technische Prinzipien, Research Questions und einzelne Integrations-/Assurance-Hypothesen. C9/#24 liefern Allocation- und Qualitätsprinzipien, keine fertige Architektur.

## 4. Korrigierte Phasenklassifikation

Aktuell nicht:

`Architecture Execution → MVP`.

Sondern:

```text
Live Research / Problem Discovery (#46/#47)
        ↕
Domain Method SOTA / Operationalisierung (#60)
        ↓
Problem-/Capability-/Requirement Reconciliation (#42)
        ↕
Technical Discovery / Engineering Advisory (#48)
        ↓
Architecture Readiness Re-Gate (#43)
        ↓ nur bei PASS
Architecture Variants / ADR / MVP Cut (#58)
        ↓
Development (#59)
```

Technische Discovery darf parallel laufen, aber nur als **Advisory / Research / Feasibility**, nicht als stiller Requirement- oder Architecture-Owner.

## 5. Führender Dev-/Engineering-Owner: Verantwortung und Grenzen

#48 soll bis zum Re-Gate als führender `Technical Discovery / Research Software Engineering Advisory` Work Owner arbeiten.

### Darf / soll

- technische SOTA-/Best-Practice-Landschaft problembezogen untersuchen;
- existierende Tools/Standards/Integrationen vor Eigenbau prüfen;
- technische Unknowns, Risiken, Abhängigkeiten und Kosten sichtbar machen;
- Machbarkeit und Migrations-/Lock-in-Risiken bewerten;
- kleine reversible Spikes/Benchmarks ausführen, wenn sie eine konkrete Research-/Requirement-Frage diskriminieren;
- technische Konsequenzen als `feasibility finding`, `architecture hypothesis` oder `requirement candidate` zurückgeben;
- technischen Backlog priorisieren nach Nutzer-/Research-Wert, Risiko, Dependency und Reversibilität;
- technische Komplexität aktiv begrenzen.

### Darf nicht

- aus technischer Convenience Fachsemantik definieren;
- `method-candidate` in Systemwahrheit überführen;
- neue Requirements akzeptieren;
- ohne Re-Gate Zielarchitektur, produktiven Stack oder MVP-Schnitt festlegen;
- Datenmodell/Workflow auf hypothetische Vollständigkeit ausbauen;
- Greenfield mit Framework-/Agent-/KG-/RAG-/Workflow-Plattform füllen, bevor ein demonstrierter Need dies trägt.

## 6. Technical Intake / Priorisierung

Jede substantielle technische Arbeit wird vor Admission mindestens klassifiziert über:

```text
PROBLEM / OBSERVED FRICTION
DOMAIN / WORK OWNER
EVIDENCE / REAL FIXTURE
CURRENT STATUS: need | method finding | requirement candidate | accepted requirement | owner constraint
TECHNICAL QUESTION
SOTA / EXISTING TOOL OPTIONS
SMALLEST DISCRIMINATING TEST
WHAT MAY BE LEARNED
WHAT MAY NOT BE DECIDED YET
RETURN TARGET
```

Priorität:

### NOW – parallel zur Domain-/Case-Arbeit

1. technische SOTA/Best-Practice und vorhandene Werkzeuge für die tatsächlich sichtbaren Kernprobleme untersuchen;
2. read-only Zotero/OneDrive feasibility (#49) als Integration Research;
3. Source/Instance/Findspot-/Portability-Invarianten als technologieunabhängige Hypothesen/Tests weiter prüfen (#50/#51/#57), soweit sie bereits durch accepted Requirements getragen sind;
4. kleine synthetische Validator-/Transition-Experimente nur als Feasibility Evidence, nicht als fertige Workflowarchitektur;
5. neue #60-Befunde auf technische Konsequenz prüfen, aber nicht direkt implementieren.

### HOLD UNTIL REQUIREMENTS / RE-GATE

- Zielarchitekturvarianten und ADR-Entscheidung (#58);
- produktiver Stack / Frameworkwahl;
- MVP-Schnitt und Development (#59);
- endgültiges Method-Conformance-/Workflowmodell;
- systemweite Knowledge-Graph-/Agent-/RAG-/Policy-/Workflow-Platform-Entscheidungen.

## 7. Re-Gate-Kriterien #43

Architecture Readiness darf erneut PASS erhalten, wenn mindestens:

1. #60 die für den ersten realen Thin Slice notwendigen Domain-Methoden hinreichend operationalisiert hat oder ihre Restschuld nachweislich nicht architecture-driving ist;
2. #42 die aus #46/#47/#60 entstandenen Requirement Candidates dispositioniert hat;
3. Problem-/Workflow-Lücken, die MVP-Scope oder Architektur materiell ändern können, geklärt oder explizit bounded sind;
4. #48 eine technische SOTA-/Feasibility-Sicht liefert, die vorhandene Tools und echte Greenfield-Optionen statt vorgezogener Lösungsauswahl vergleicht;
5. erst dann ein Architecture Question Set mit realen, diskriminierbaren Alternativen aktualisiert wird.

## 8. Leitregel

> **Fachliche und produktbezogene Ungewissheit wird nicht durch Architekturfortschritt kompensiert. Dev exploriert früh, entscheidet aber spät.**

> **Greenfield bedeutet technische Freiheit – nicht Freiheit, fachliche Semantik zu erfinden.**
