# Live Pilot System Analysis – Chat/Work-Context 2026-08-31

**Status:** `working-pilot-evidence / requirement-candidate-input`  
**Work Owner:** #61  
**Requirements Owner:** #42  
**Domain Method Owner:** #60  
**Live Research Context:** #46/#47  
**Stand:** 2026-08-31

## 1. Zweck

Dieser Pilot behandelt den aktuellen Chat selbst als reales Systemexperiment. Er fragt nicht, ob die historische Forschung inhaltlich schon richtig ist, sondern welche **Systemanforderungen, Assurance-Regeln und Failure Modes** beim Versuch sichtbar werden, aus einer unscharfen Nutzer-Vision wissenschaftlich belastbare Arbeit zu machen.

Der Pilot ist **keine neue accepted Requirements Baseline**. Er liefert Evidence und Requirement Candidates für #42 sowie Testfälle für #61/#54/#55/#57.

## 2. Beobachteter Live-Fall

Der Nutzer formuliert die Forschungsvision in Alltagssprache und erwartet zugleich domänenspezifische wissenschaftliche Präzision. Im Pilot entstand zunächst das Risiko, diese Vision durch plausibel klingende, aber noch nicht SOTA-validierte Methodenprosa zu operationalisieren.

Die anschließende Korrektur führte zur Trennung:

```text
Nutzer-Vision / Pain
→ fachliche Problemübersetzung
→ Domain Method Research (#60)
→ Method Conformance / Work Context (#61)
→ Requirement Candidate
→ accepted Requirement nur unter #42
→ Architektur/Dev erst downstream
```

Damit ist der Pilot gleichzeitig **Live Research**, **Method-Stresstest** und **Systemanalyse-Fall**.

## 3. Pilot-Findings für die Systemanalyse

### P-SA-001 – Nutzerformulierung darf nicht still zu Methode oder Requirement werden

**Observation:** Der Nutzer kann Ziel, Pain oder Vision fachlich unscharf formulieren. Das System muss die fachliche Operationalisierung selbst recherchieren und darf weder Methodik noch Requirement aus sprachlicher Plausibilität erfinden.

**Existing requirement coverage:** `REQ-EPI-001`, `REQ-EPI-002`; #60.

**System implication:** Work Context muss den Status einer Aussage als `vision | work_order | observation/finding | historical_hypothesis | method_hypothesis | requirement_candidate | accepted_requirement | architecture_choice` explizit führen oder zuverlässig ableiten können.

**Status:** existing requirement strengthened by pilot evidence; kein neues Requirement nötig.

### P-SA-002 – Fachmethodik und konkrete Methodenanwendung müssen getrennte Objekte sein

**Observation:** Ein gutes Method Profile allein beweist nicht, dass es im konkreten Chat korrekt angewandt wurde.

**Existing requirement coverage:** `REQ-EPI-001`, `REQ-WF-001`, `REQ-UX-001`; #61.

**System implication:** `Method Profile` und `Method Application` müssen getrennt auditierbar sein, einschließlich Profile-Version/Status, Work Order, ausgeführter Gates, `not-assessable`, Outputs und Review-Ziel.

**Status:** existing requirement operationalization; Testfall für #61/#54/#55.

### P-SA-003 – Exploration muss möglich bleiben, Promotion muss bei Method Debt fail-closed sein

**Observation:** Historische Exploration soll nicht blockieren, nur weil ein Domain Method Profile noch `method-candidate` ist. Das System darf daraus aber keinen consequential/validated State erzeugen.

**Existing requirement coverage:** `REQ-EPI-001`, `REQ-WF-001`, `REQ-EPI-004`.

**System implication:** `method-candidate` erlaubt Exploration/Hypothesen; consequential Promotion verlangt `working-method` oder höher sowie passende Evidence/Review-Gates.

**Status:** existing requirement operationalization; harter Negativtest.

### P-SA-004 – Der Nutzer darf nicht zum Requirements-/Methoden-Administrator werden

**Observation:** Der Nutzer soll weder Domain Labels, Profile-IDs, Work-Owner-Taxonomie noch vollständige Übergabeformulare kennen müssen, um wissenschaftlich korrekt arbeiten zu können.

**System implication:** Soweit deterministisch aus Repo-State und Auftrag ableitbar, muss das System `primary_function`, Work Owner, Scope, relevante Domain Profiles, Evidence Context, Stop/Handoff und Persistence Target selbst rekonstruieren. Rückfragen nur bei materieller Ambiguität.

**Existing coverage:** #61 MC-01; `AGENTS.md` §13; `REQ-STATE-001` und `REQ-EPI-002` indirekt.

**Requirement assessment:** **Candidate RC-SA-01** – prüfen, ob die bestehende Baseline diese *low-burden automatic work-context composition* stark genug als Nutzer-/Workflow-Anforderung ausdrückt. Noch nicht accepted.

### P-SA-005 – Live-Nutzung ist selbst Requirements-Evidence

**Observation:** Der aktuelle Pilot hat eine reale Lücke sichtbar gemacht: Vision und Kompetenzkarte waren vorhanden, domänenspezifische Method Operationalization jedoch nicht. Diese Lücke wäre bei reiner Dokumentanalyse leichter übersehen worden.

**System implication:** Reale Nutzung muss Friktionen/Fails/Overclaims als tracebare Systemanalyse-Evidence aufnehmen können:

```text
live observation / pain
→ affected workflow/capability/requirement
→ existing coverage | gap | ambiguity
→ candidate
→ validation/generalization
→ #42 promotion decision
```

Das System darf Live-Pain weder automatisch zum Requirement machen noch als bloßen Chat verlieren.

**Existing coverage:** Prozessregel #10/#42, `AGENTS.md` Persistenzpflicht; in Requirements Baseline nicht als eigenständige funktionale Anforderung klar isoliert.

**Requirement assessment:** **Candidate RC-SA-02 – Live-use requirement feedback loop**. Zu prüfen gegen bestehende Workflow-/Audit-/State-Requirements und U1–U4, bevor #42 geändert wird.

### P-SA-006 – Systemanalyse braucht negative Tests gegen plausible KI-Selbstlegitimation

**Observation:** Ein LLM kann plausibel erklären, warum eine Methode sinnvoll sei, und dadurch methodische Autorität vortäuschen.

**System implication:** Negativtests müssen mindestens verhindern:

1. Rollenprompt/Disziplinlabel als Method Truth;
2. `method-candidate` als `working-method`;
3. AI-Output als Evidence;
4. Finding ohne Source/Findspot;
5. Requirement/Architecture-Promotion aus einem einzelnen Live-Fall ohne Generalisierungsprüfung;
6. Dev-Scope-Erweiterung ohne accepted Requirement/Owner Constraint;
7. Erzwungene Aussage statt `unresolved/not-assessable`.

**Existing coverage:** `REQ-EPI-001`, `REQ-EPI-004`, `REQ-EPI-005`, `REQ-WF-001`, #61/#54.

**Status:** existing requirement coverage; pilot-derived acceptance/negative tests.

### P-SA-007 – Fresh-context Restartability ist funktionaler Test, nicht Dokumentexistenz

**Observation:** Dieser Chat konnte erst nach erneutem Repo-Bootstrap verlässlich bestimmen, welche Methodik, Requirements und Work Owner aktuell gelten.

**System implication:** Ein neuer autorisierter Work Context muss aus Repository + verfügbarer Evidence korrekt rekonstruieren können: Aufgabe, Authority, Method Status, Evidence, erlaubte nächste Aktion, Handoff und Persistence Target.

**Existing requirement coverage:** `REQ-STATE-001`, #57, #61 MC-07, `AGENTS.md`.

**Status:** existing requirement strengthened by pilot evidence.

## 4. Requirement-Delta-Entscheidung des Piloten

Der Pilot rechtfertigt **noch keine direkte Änderung der accepted Requirements Baseline**.

Bereits ausreichend abgedeckt erscheinen:

- Method-/Domain-Traceability;
- deterministic invariant boundary;
- auditability;
- uncertainty / unresolved;
- AI ≠ Evidence / independent validation;
- restartable canonical state.

Als echte **Requirement Candidates** bleiben nur:

- **RC-SA-01 – Low-burden Work-Context Composition:** Das System soll aus Nutzerauftrag + kanonischem Repo-State den notwendigen Work Context soweit möglich automatisch komponieren, statt den Nutzer mit interner Method-/Owner-/Authority-Taxonomie zu belasten.
- **RC-SA-02 – Live-use Requirement Feedback Loop:** Das System soll relevante Friktionen/Failures aus realer Nutzung tracebar als Systemanalyse-Evidence erfassen und kontrolliert in Capability-/Requirement-Candidates überführen können, ohne automatische Promotion.

Beide bleiben `candidate / research-needed`, bis sie gegen bestehende Requirements, mehrere Use Cases und Failure Modes geprüft sind.

## 5. Pilot-Acceptance für #61

Der aktuelle Chat-Pilot gilt erst dann als bestanden, wenn ein frischer Work Context ohne Chatgedächtnis:

1. #60 als Method-Truth-Owner und #61 als Method-Conformance-Owner erkennt;
2. die Nutzerformulierung als Vision/Pain statt fertige Methode behandelt;
3. passende Method Profiles mit Status referenziert;
4. bei fehlendem `working-method` Exploration erlaubt, Promotion aber blockiert;
5. Source/Evidence/Findspot und AI-Output nicht verwechselt;
6. relevante Friktion als Systemanalyse-Evidence persistiert;
7. Requirement Candidates an #42 routet, ohne die Baseline eigenmächtig umzuschreiben;
8. dem Nutzer die interne Governance nicht als Verwaltungsaufgabe aufbürdet.

## 6. Handoff

- **#60:** fachliche Method Profiles und ihre SOTA-/Inference-Semantik erarbeiten.
- **#61:** diesen Pilot als Work-Context-/Conformance-/Audit-/Restartability-Test verwenden.
- **#54:** Negativtests aus P-SA-003/P-SA-006 in Transition-/Invariant-Fixtures übernehmen.
- **#55:** Auditpfad muss Vision/Pain → Work Order → Method Application → Finding/Claim → Review/History lesbar machen.
- **#57:** Fresh-context Pilot ohne alten Chat wiederholen.
- **#42:** RC-SA-01/02 erst nach Cross-Use-Case-/Baseline-Gap-Prüfung entscheiden.

## 7. Leitregel

> **Ein Live-Pilot darf Requirements entdecken, aber nicht selbst akzeptieren. Er muss Friktion in tracebare Evidence verwandeln, statt sie als Chat-Erinnerung oder KI-Plausibilität zu verlieren.**
