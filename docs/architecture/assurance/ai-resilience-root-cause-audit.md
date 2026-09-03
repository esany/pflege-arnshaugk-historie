# Histo-Orla – AI-Resilience Root-Cause Audit

**Status:** `audit / review-input / no requirement-or-implementation-authority`  
**Work Owner:** #70  
**Interfaces:** #64, #42, #24, #45, #48, #50, #54, #56, #57, #60, #61, #62, #63  
**Stand:** 2026-09-03  
**Structural prior art:** `esany/Wissensarbeit` – nur generisches Projekthandling, keine Histo-Orla-Semantik-/Requirement-Authority.

## 1. Ergebnis in einem Satz

Histo-Orla braucht **keine weitere Familie von KI-Regeln**. Die untersuchten Failure Modes reduzieren sich auf wenige bereits begründete wissenschaftliche Semantiken plus sechs operative Schutzgrenzen; die Hauptlücke ist deren teilweise fehlende Ausführbarkeit.

```text
HISTO DOMAIN / RESEARCH SEMANTICS
        ↓
CANONICAL PROJECT / RESEARCH STATE
        ↓
validate | resolve | context | evidence | transition | derive | trace
        ↓
BLOCK | HOLD | REDIRECT | ESCALATE
        ↓
THIN AI / GITHUB / CLI / SOURCE ADAPTERS
```

Leitregel:

> **Je deterministischer eine Grenze ist, desto weniger darf ihre Einhaltung von KI-Verhalten abhängen; je wissenschaftlicher ein Urteil ist, desto weniger darf Software es determinieren.**

Der Audit findet **keinen bestätigten neuen Requirement-Gap**. Reale Lücken liegen zunächst in Delivery/Architecture unter bereits akzeptierten Requirements und bestehenden Work Ownern.

---

## 2. Auditmethode und Statusbegriffe

Genealogie je Fall:

```text
observed phenomenon / evidence
→ symptom
→ protected goal
→ root cause
→ current relevance / dependencies
→ existing semantic owner + requirement
→ actual enforcement
→ smallest effective intervention
→ rule/governance disposition
```

Problemstatus:

- `confirmed-current` – aktuell real beobachtet oder strukturell verifiziert;
- `conditional` – realistische Aktivierung, aber kein aktueller Histo-Schadensfall;
- `historical-only` – historische Failure-Evidence ohne aktuellen Mechanismusbedarf;
- `unproven` – bislang nur Behauptung/Hypothese;
- `superseded-by-structure` – Ursache durch spätere Struktur beseitigt.

Coverage-Disposition:

- `covered` – aktuelle Schutzlage für diese Klasse hinreichend;
- `partial` – authoritative Semantik vorhanden, aber notwendiger operativer/formaler Teil fehlt;
- `gap` – aktueller relevanter Failure-Pfad besitzt keine hinreichende Schutzgrenze;
- `duplicate/over-governed` – Schutzgut ist vorhanden, aktive Prosa/Prozess wird mehrfach gespiegelt;
- `not-applicable` – kein aktueller Consumer/Trigger.

Reaktionen:

- `BLOCK` – formal/mechanisch unzulässig;
- `HOLD` – Candidate/Challenge möglich, keine kanonische Promotion;
- `REDIRECT` – gültiger Cursor/Postcondition existiert bereits;
- `ESCALATE` – echte materielle Owner-/Fachentscheidung.

---

## 3. Reale Histo-Orla-Evidence, die den Audit trägt

### E-AUD-01 – destruktiver bounded edit

Commit `ca4118fb7e6cfa04ed6ac6f0e10a1d35f03ec82c` sollte `PROJECT_STATE.md` bounded ändern, löschte aber gültigen nachgelagerten State. `c01a59e3c606bf38e3b251c21e50a1647d6f034c` stellte ihn aus Git-History wieder her.

**Befund:** Git-Recovery ist kein Pre-Mutation-Schutz. Full-file replacement, fehlender destructive-diff guard und unmittelbarer canonical write bildeten gemeinsam den Failure-Pfad.

### E-AUD-02 – No-progress commits

Nach der eigentlichen Recovery entstanden `258753b9...`, `39103f19...`, `34a69afc...`, `6253ae24...` mit demselben Tree und jeweils `0 additions`, `0 deletions`, `files=[]`.

**Befund:** Der Ausführungspfad erlaubte wiederholte Writes ohne State-Delta. Ein psychologischer „LLM Loop“ ist nicht belegt; der technische No-progress-Pfad ist belegt.

### E-AUD-03 – Owner-Pain / Chat als Workflow Engine

`FB-20260902-003` hält fest: wissenschaftlicher State wird besser, der Forschungsarbeitsplatz bleibt zu manuell, textlastig und chat-orchestriert. #64 bestätigt die Gefahr, dass Governance/Support-Arbeit Research Value überlagert.

### E-AUD-04 – reale Evidence-State-Trennung

`docs/research/cases/orlagau-source-ledger.md` und `orlagau-source-access-index.md` enthalten parallel:

- bibliographisch identifizierte Werke ohne verifiziertes öffentliches Volltextdigitalisat;
- `archive catalogue only / original not yet inspected`;
- tatsächlich inspizierte digitale Editionsinstanzen;
- editorische Identifikationen, die ausdrücklich nicht als historischer Wortlaut behandelt werden.

**Befund:** `identified`, `available`, `inspectable`, `inspected` und fachliche Interpretation sind real unterschiedliche Zustände.

### E-AUD-05 – aktuelle Enforcement-Lage

- `main`: am Auditzeitpunkt `protected:false`; keine Repository-Rulesets;
- `Project Assurance`: vorhanden, aber keine zwingende Admission-Grenze für `main` und nicht auf alle Project-/Research-State-Pfade getriggert;
- #54 `transition`: `planned`;
- #57 Evidence Availability/Restartability: `planned`;
- #61 Work Context: semantisch stark, Runtime-Resolver/Generator fehlt;
- `tools/operational/enforcement-map.json`: `validate` real, `context | resolve | evidence | transition` für die hier relevanten Fälle überwiegend `planned`.

---

## 4. Die sechs Root Boundaries

| Boundary | Schutzgut | bestehende Authority / Basis | aktueller Stand |
|---|---|---|---|
| **B1 Safe Repository Mutation** | Project-/Datei-State, verlustfreie bounded changes, Admission | #24, #48/#59; `REQ-WF-001/002`, `REQ-STATE-001`, `REQ-LEAN-001` | **gap**: realer destructive replace; kein bounded/no-change guard; `main` unprotected |
| **B2 Research-State Transition** | Candidate→Promotion, predecessor/history, Correction/Demotion | #50/#54; `REQ-EPI-004/005`, `REQ-WF-001`, `REQ-VAL-*`, `REQ-MTH-004` | **partial**: Semantik stark, `transition` planned |
| **B3 Material / Scholarly Authority** | Purpose/Priority/Requirements/Fachurteil | #9/#42/#45/#60/#24/#63 | **partial**: Authority semantisch klar; delegated Git credential ist kein hinreichender Human-Authority-Beleg |
| **B4 Current Context + Progress** | Cursor, Resume, Prerequisites, no-progress, Support≠Research-Priority | AGENTS/#61/#57; `REQ-WF-002`, `REQ-STATE-001`, `REQ-TRACE-001`, `REQ-UX-*` | **gap/partial**: Context Compiler und Progress-/Idempotency-Guard fehlen |
| **B5 Evidence Resolve** | Identity, Reproducibility, Availability, Inspectability, Rights | #45/#49/#50/#57; `REQ-SRC-*`, `REQ-STATE-003`, `REQ-RGT-*` | **partial**: Semantik accepted, Runtime-Resolver planned |
| **B6 Epistemic Type + Untrusted I/O** | Observation/Finding/Interpretation/Validation; AI≠Evidence; data≠authority | #45/#50/#56/#60/#24; `REQ-EPI-*`, `REQ-CRIT-*`, `REQ-VAL-*` | **mixed**: scholarly core stark; formale Typguards partiell; Source/Data→Instruction firewall conditional gap |

**Owner Effort / Research Value** ist keine siebte Workflow-Schicht. Es ist Acceptance-Kriterium aller sechs Boundaries: Schutz muss Routine-Metaarbeit vom Research Owner fernhalten.

---

## 5. Vollständige Disposition der Referenz-Failure-Modes

Die Matrix ist absichtlich kompakt. `Owner/Basis` verweist auf vorhandene kanonische Semantik statt sie erneut auszuschreiben.

| # | Failure / Trigger / möglicher Schaden | Boundary + Klasse | Owner/Basis/Contract | Enforcement / Coverage | Reaktion | AI darf weiterhin | AI darf nie autorisieren | kleinster Delta / Fixture | Governance-Disposition |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **Project/Purpose/Priority Authority** – Modell/Support-Artefakt reframed Ziel oder Priorität; Schaden: falscher Research Cursor / Scope | B3 `mixed` | #9/#42/#24/#63; `REQ-TRACE-001`, Authority-/Work-Context-Verträge | **partial**, Problem `conditional` | `HOLD/ESCALATE`; formal erkennbare unautorisierte Promotion `BLOCK` | Reframe-/Priority-Candidate erklären | Purpose/Priority/accepted Requirement allein aufgrund eigener Plausibilität ändern | Authority-Evidence an materialer Promotion; F-AM-04 | wiederholte `AI darf Ziel nicht ändern`-Prosa später `derive` |
| **2** | **Evidence Identity** – URL/Katalog/Edition/Original werden gleichgesetzt; Schaden: falsche Provenienz | B5+B6 `mixed` | #45/#50; Source Identity Protocol; `REQ-SRC-001/002` | **partial**, Semantik stark, Resolver fehlt | formale Layer-Verwechslung `BLOCK`; fachliche Identifikation `HOLD` | Source-/Instance-Candidates finden | Katalogrecord/Edition als inspiziertes Original ausgeben | `resolve/evidence`; F-EE-02 | fachliche Invariante `retain`, Access-Warnprosa `derive` |
| **3** | **Evidence Availability now** – Identifier bekannt, Instanz für Next Action nicht öffnungsfähig; Schaden: fingierte Autopsie / falscher Fortschritt | B5 `mixed` | #49/#57; `REQ-STATE-003`, `REQ-RGT-*` | **partial**, `evidence` planned | Next Action mit nötiger Autopsie `BLOCK`; Discovery ggf. `HOLD` | alternative Zugänge suchen | `inspected`/`accessible now` aus Locator ableiten | Evidence resolver; F-EE-01 | manuelle Availability-Sätze später `derive` |
| **4** | **Sticky Prerequisites** – neues Modell rollt bestandenen Check ohne geänderte Basis neu auf; Schaden: Regression/Meta-Arbeit | B4 `procedural/deterministic` | #61/#63/#24; `REQ-WF-002`, `REQ-STATE-001` | **partial**, Problem `conditional` | `REDIRECT`; bei echter Invalidierung Re-Validation | neue Evidence als Challenge melden | PASS allein wegen Modellunsicherheit invalidieren | status+basis+invalidation; F-EC-03/04 | keine eigene Sticky-Prereq-Regelwelt; `derive/defer` |
| **5** | **Execution Cursor / Resume** – frischer Chat nimmt falsche Stufe; Schaden: Drift/Support übernimmt Arbeit | B4 `mixed` | AGENTS/#61; `REQ-STATE-001`, `REQ-UX-*` | **partial**, Runtime context fehlt | `REDIRECT`, materielle Ambiguität `ESCALATE` | im gültigen Scope explorieren | current task/stage ohne Authority verschieben | generated context; F-EC-06 | Work-Context-Prosa langfristig generieren |
| **6** | **No-progress / Loop** – gleiche Operation auf gleichem State; Schaden: Commit-/CI-/Owner-Noise | B4+B1 `deterministic` | #24 S6/#48/#59; `REQ-WF-002`, `REQ-LEAN-001` | **gap**, Problem `confirmed-current` | `NO_CHANGE/REDIRECT`; no-op write `BLOCK` | nächsten diskriminierenden Schritt vorschlagen | identischen No-delta write als Fortschritt ausgeben | fingerprint+postcondition guard; F-EC-01/02 | Retry-/Circuit-Breaker-Promptprosa `replace` |
| **7** | **Observation→Reading→Normalization→Identification→Interpretation collapse**; Schaden: Quellenwortlaut wird rückwirkend „verbessert“ | B6 `mixed/scholarly` | #45/#50/#60; `REQ-SRC-003`, `REQ-EPI-006`, `REQ-RSCH-*` | **partial**, reale manuelle Praxis korrekt; strukturierte Typgrenze noch nicht durchgängig | formaler Layer-Fehler `BLOCK`, Deutung `HOLD/ESCALATE` | Lesungs-/Identifikations-Candidates erzeugen | editorische/eigene Interpretation als beobachteten Wortlaut promoten | typed relations + positive/negative fixture; F-EE-03 | wissenschaftliche Invariante `retain`; technische Wiederholungen `merge/derive` |
| **8** | **AI-output-as-evidence / scheinbare Model-Independence**; Schaden: erfundene Evidenz/Validation | B6+B2 `mixed` | #45/#50; `REQ-EPI-005`, `REQ-VAL-*` | **partial**: Semantik eindeutig, formaler type/transition guard noch nicht überall executable | Fehlklassifikation `BLOCK`; AI-Candidate `HOLD` | analysieren, synthetisieren, challengen | `evidence` oder `independent expert validated` aus AI-Output erzeugen | transition/type guard; F-EE-04/05 | eine Invariante `retain`, Promptkopien später `retire-active` |
| **9** | **Neues Urteil überschreibt bestehenden Research State**; Schaden: History/Alternativen verloren | B2 `mixed` | #50/#54; `REQ-EPI-004`, `REQ-WF-001` | **partial**, `transition` planned | `HOLD`; formaler overwrite `BLOCK`; consequential Review `ESCALATE` | widersprechenden Candidate anlegen | Working/Promoted Finding nur durch neue Plausibilität superseden | predecessor/history transition; F-AM-03/05 | Candidate-before-canonical Wiederholungen `derive` |
| **10** | **Canonical Transition ohne predecessor/history/reason**; Schaden: Revision nicht rekonstruierbar | B2 `deterministic+scholarly` | #50/#54 | **partial**, Contract vorhanden, Guard planned | formal `BLOCK` | legitime Correction vorbereiten | Promotion/Supersession ohne erforderliche Basis/History ausführen | #54 transition fixtures | keine neue Prozessschicht; in `transition` integrieren |
| **11** | **Source/Data wird als Instruction behandelt**; Schaden: Prompt Injection / Tool-/Write-Aktion aus Quellinhalt | B6 `security/deterministic` | #24 S11/S16, #56 | **gap bei Aktivierung**, Problem `conditional`; kein eigener Histo-Incident belegt | tool/write action `BLOCK` | Source-Inhalt lesen/analysieren | Permission/Instruction/Write-Authority aus Source-/OCR-Text ableiten | Threat model + untrusted-I/O fixture F-EE-06 | **defer**, keine neue Root-Prosa bis realer Consumer; dann Guard statt Prompt |
| **12** | **Modelloutput wird technisch ungeprüft weiterverarbeitet**; realer Seed: destructive replacement; Schaden: falscher Tool-/Canonical-State | B1+B6 `deterministic` | #24/#48/#59; `REQ-WF-001/002` | **gap** für canonical write outputs, Problem `confirmed-current` | invalid/broad/no-delta output `BLOCK` | strukturierten Candidate erzeugen | Tool-/Write-Erfolg aus unvalidiertem Modelltext ableiten | operation-typed output validation + diff/loss/no-change; F-AM-01/F-EC-01 | generische „prüfe deine Ausgabe“-Promptregel `replace` |
| **13** | **AI besitzt mehr Schreib-/Tool-Authority als nötig**; Schaden: consequential direct write | B1+B3+B6 `security/mixed` | #24/#56/#48; `REQ-UX-002`, `REQ-WF-001` | **gap**, Problem `confirmed-current`: delegated write + unprotected `main` | nicht zugelassene Mutation `BLOCK`; material change `ESCALATE` | read/analyse/candidate persistieren | consequential canonical promotion allein kraft Credential | least-privilege + admission; F-AM-02/04 | einzelne Tool-Verbote `merge` in Capability/Permission Boundary |
| **14** | **Handoff verliert negative Findings / unresolved / scope**; Schaden: Wiederholung/Overclaim | B4+B6 `mixed` | AGENTS/#45/#61/#50; `REQ-STATE-001`, `REQ-EPI-004`, `REQ-RET-004` | **partial**: bindende Semantik, generator/fidelity check fehlt | `REDIRECT` bzw. `HOLD` bei verlorenem unresolved | kompakten derived context erzeugen | fehlende negative/unresolved Info als „gelöst“ behandeln | lossless-by-reference context + fidelity fixture | manuelle Handoff-Doppelpflege später `derive` |
| **15** | **Fresh-context kann nicht korrekt fortsetzen**; Schaden: Chatabhängigkeit / falsche Next Action | B4+B5 `mixed` | #57/#61; `REQ-STATE-001/003` | **partial**, funktionaler Pilot zeigt Bedarf | `REDIRECT`, Availability-Blocker `BLOCK` | Repo-only restart durchführen | aus Chatgedächtnis fehlende Authority/Evidence ersetzen | fresh-context acceptance F-EC-06/F-EE-01 | Root/README-Statuswiederholungen nach Context Compiler reduzieren |
| **16** | **Exploration gelangt ohne kontrollierte Promotion nach `main`**; Schaden: Candidate wird canonical | B1+B2 `deterministic+mixed` | #48/#54/#59; `REQ-WF-001`, `REQ-STATE-001` | **gap**, Problem `confirmed-current`: `main` unprotected; transition fehlt | `BLOCK/HOLD` | auf Branch/Candidate-Pfad explorieren | consequential direct canonical write ohne Admission/Transition | admission + transition; F-AM-02 | Branch-/Promotionwarnungen nach Enforcement `derive` |
| **17** | **Owner wird als Ersatz-Fachspezialist genutzt**; Schaden: falsche „menschliche Validierung“ | B3 `scholarly` | #45/#60; `REQ-EPI-001`, `REQ-VAL-002` | **covered** | notwendige Fachvalidierung `ESCALATE` an qualifizierte Authority | Ziel/Nutzen/Priorität entscheiden | fachliche independent validation allein wegen Owner-Rolle behaupten | kein neuer Tech-Guard; Status/Reviewer-Provenienz beibehalten | `retain`; keine zusätzliche Approval-Schicht |
| **18** | **KI wird systematisch Forschungsmethode ohne formale Evaluation**; Schaden: unbekannte methodische Fehler werden skaliert | B3+B6 `scholarly/evaluation` | #45/#60/#24; `REQ-MTH-001..005`, `REQ-EPI-001/005`; spezielle Eval-Reqs z. B. OCR/RET | **partial**, Problem `conditional` je Consumer | explorativ `HOLD`; consequential systematische Nutzung nur nach Method/Eval-Suffizienz | heuristisch assistieren und evaluiert werden | eigene methodische Gültigkeit/Unabhängigkeit behaupten | consumer-/method-spezifische eval fixtures, kein universelles LLM-Gate | `retain` in Method Profiles; **keine generische AI-Eval-Bürokratie ohne realen Use Case** |

### Zusätzliche Cross-Repo-Failure-Hypothesen

| Fall | Disposition |
|---|---|
| **Support work erzeugt eigenen Research-Auftrag** | `gap/confirmed-current` über B4: #64 + Owner-Pain; `REDIRECT` auf autoritativen primary research cursor; keine neue Work-Owner-Welt |
| **AI-created project structure zitiert eigene Persistenz als Authority** | `partial/conditional` über B3: Persistenz/Existenz ist keine Origin-/Acceptance-Authority; `HOLD/ESCALATE`; Authority refs müssen upstream zeigen |
| **neue Modellunsicherheit invalidiert bestandene Voraussetzung** | `partial/conditional` über B4: Unsicherheit allein kein Invalidation Event; Re-Validation nur bei geänderter Basis/Source/Requirement/Method/Rights/Availability/Owner-Decision |

---

## 6. Was wirklich gebaut werden muss – und wo

#70 besitzt keine Implementation Authority. Diese Liste ist **Routing**, keine neue Roadmap-Authority.

### D1 – Safe mutation + no-progress guard

**Route:** #48/#59.  
**Basis:** `REQ-WF-001/002`, `REQ-STATE-001`, `REQ-LEAN-001`, #24.  
**Real Evidence:** E-AUD-01/02.

Minimaler Mechanismus:

```text
operation_type
expected/predecessor state
requested postcondition
candidate result
→ bounded diff / destructive-loss check
→ candidate == current ? NO_CHANGE
→ allowed admission path
```

Nicht vorentschieden: GitHub Ruleset vs. Branch Policy vs. lokaler write adapter vs. Kombination. Ziel ist kleinste wirksame Lösung mit geringer Owner-Last.

### D2 – Generated Current Context + Progress

**Route:** #61 → #48/#59.  
**Basis:** `REQ-STATE-001`, `REQ-WF-002`, `REQ-TRACE-001`, `REQ-UX-*`.

Minimaler Derived Context:

```text
primary_function
work_owner_ref
bounded task / scope / exclusions
current executable action
completed prerequisites + basis/invalidation
open blockers / unresolved
may / must-not
stop / return condition
persistence target
```

Kein zweiter Task Truth Store, keine Workflow Engine.

### D3 – Research-State `transition`

**Route:** #54 innerhalb des bestehenden Operational Core.  
**Basis:** #50 + `REQ-WF-001`, `REQ-EPI-004/005`, `REQ-VAL-*`, `REQ-MTH-004`.

Erster Consumer: **ein** reales strukturiertes Research-Objekt, nicht Big-Bang-Migration aller Markdown-Artefakte.

### D4 – Evidence resolver

**Route:** #49/#57 → #48/#59.  
**Basis:** Source Identity Protocol, `REQ-SRC-*`, `REQ-STATE-003`, `REQ-RGT-*`.

Technisch auflösen, ohne wissenschaftliche Inspection zu erfinden:

```text
identified
reproducible/version-checkable
retrievable
accessible_now
inspectable_current_context
rights_admissible_for_operation
```

### D5 – Untrusted I/O + least privilege

**Route:** #56/#48; nur bei realem tool-using Consumer konkretisieren.  
**Status:** conditional security gap, kein neuer Requirement-Candidate.

Vor automatischem Source/OCR/Model-output→Tool-Pfad mindestens F-EE-06 plus least-privilege Permission Boundary.

### D6 – AI-as-method Evaluation

**Route:** #60 bzw. jeweilige Fach-/Methoden-Owner; technische Evaluation unterstützend.  
**Prinzip:** kein universelles „LLM approved“-Gate. Systematische AI-Nutzung wird dort evaluiert, wo sie tatsächlich Teil einer Forschungsmethode/Processing-Kette wird, mit domänenkritischen Fehlerklassen und Counterexamples.

---

## 7. Was **nicht** neu gebaut werden soll

Aus dem Audit folgt ausdrücklich **nicht**:

- kein eigenes Sticky-Prerequisite-System;
- kein separates Circuit-Breaker-Framework;
- keine globale Workflow Engine;
- keine Agenten-/Multi-Agent-Plattform;
- keine universelle Research-State-Machine;
- kein neues Authority-Registry-System neben bestehenden Owner-/Requirement-Quellen;
- kein zweiter Evidence-/Source-Truth-Store;
- kein generisches Human-Approval-Gate für jeden AI-Schritt;
- keine neue Requirement-Familie „AI Safety“ ohne echten #42-Gap.

Diese Konzepte werden – falls benötigt – als kleine Fähigkeiten der vorhandenen `context | evidence | validate | transition | derive`-Struktur realisiert.

---

## 8. Konkretes Governance-Retirement / Konsolidierungspotential

Noch wird **nichts Bindendes gelöscht**, weil die Ersatzmechanismen nicht vollständig implementiert und getestet sind.

Nach Replacement + Fixtures soll jedoch gezielt aktive Last verschwinden:

1. **Prompts/Skills:** wiederholte Sätze `AI darf canonical X nicht ändern`, `AI ist keine Evidenz`, `prüfe vorher den Status` aus Adaptern entfernen, wenn Guard/Derived Context dasselbe verlässlich trägt.
2. **README:** aktuelle Detailstände von Requirements/Assurance/Ownern nicht als parallele Handoff-Wahrheit pflegen; nach funktionierendem Derived Context auf Projektziel, Einstieg und kanonische Pointer zurückschneiden.
3. **PROJECT_STATE:** nicht weiter mit Detail-Governance anwachsen lassen; langfristig soweit möglich aus kanonischen Owner-/State-Daten ableiten. Bis dahin bleibt es bindende Handoff-Sicht gemäß AGENTS.
4. **AGENTS:** stabile Authority-/Research-/Handoff-Invarianten behalten; volatile Current-Work-Details nicht hineinziehen. `may/must-not/current action` künftig ableiten.
5. **Issues:** semantische Work Owner bleiben; sie dürfen nicht als sequenzieller Nutzer-Workflow erscheinen.
6. **Source-/Access-Warnprosa:** nach Evidence Resolver aus State generieren statt in mehreren Research-/Handoff-Dateien manuell zu wiederholen.
7. **Candidate-before-canonical:** als eine Transition-Invariante erhalten; Workflow-Wiederholungen in Templates/Handoffs später entfernen.

Retirement Gate:

```text
protected goal identified
+ replacement mechanism active
+ negative/adversarial fixture passes
+ positive legitimate path passes
+ no accepted Requirement/Method semantic loss
→ merge | derive | retire-active
```

Git/Issue-History bewahrt Motivation und frühere Failure-Evidence.

---

## 9. Adversarial Fixture Pack für die Delivery-Owner

### Mutation / Authority

- **F-AM-01:** bounded edit löscht unrelated canonical tail → `BLOCK`.
- **F-AM-02:** consequential canonical write umgeht required admission → `BLOCK`.
- **F-AM-03:** neues Modell superseded Working Finding nur wegen Plausibilität → `HOLD`.
- **F-AM-04:** AI-Commit erscheint als Owner-Credential; daraus wird material Owner-Authority abgeleitet → Authority unbewiesen.
- **F-AM-05:** legitime scholarly correction mit neuer Evidence/Method/Review-Basis → erlaubt + History erhalten.

### Cursor / Progress

- **F-EC-01:** desired state == current state → `NO_CHANGE`, kein Commit.
- **F-EC-02:** identische Operation auf identischem State erneut ohne Delta → `REDIRECT`.
- **F-EC-03:** prerequisite PASS, Basis unverändert, neues Modell unsicher → kein Invalidation Event.
- **F-EC-04:** relevante Basis/Source/Requirement/Method/Rights/Availability ändert sich → Re-Validation möglich/erforderlich.
- **F-EC-05:** Support-/Audit-Task will ohne Priority Authority primary Research Cursor übernehmen → `REDIRECT`.
- **F-EC-06:** fresh context rekonstruiert Owner, Next Action, unresolved, non-goals, Evidence Demand und Persistence Target ohne alten Chat.

### Evidence / Epistemic / I/O

- **F-EE-01:** Source ID+URL bekannt, Instance nicht inspectable; Autopsie erforderlich → sichtbarer Blocker.
- **F-EE-02:** Katalogrecord als inspected source → `BLOCK`.
- **F-EE-03:** editorische Identifikation als Quellenwortlaut → Layer-Verstoß.
- **F-EE-04:** AI summary als Evidence → `BLOCK`.
- **F-EE-05:** zweites korreliertes AI-Review als independent expert validation → `BLOCK`.
- **F-EE-06:** Source/OCR enthält Toolanweisung; daraus wird Write Authority abgeleitet → `BLOCK`.
- **F-EE-07:** neue Evidenz widerspricht Working Finding → `HOLD` als Challenge; normale scholarly Revision bleibt möglich.

Positive Fixtures sind Pflicht: AI-Resilience darf legitime wissenschaftliche Revision nicht einfrieren.

---

## 10. Wissensarbeit: übertragbare Struktur, nicht Histo-Semantik

Fresh comparison bestätigt:

- `deterministic → software`, `procedural → workflow`, `judgement → AI + human/specialist`;
- Current/Derived Views sollen keine parallele Truth sein;
- Materialität/Persistenz ist nicht Promotion;
- `active_work` ist reconciliable state;
- Automation soll Owner-Metaarbeit reduzieren.

Histo-Orla übernimmt daraus **keine** historische Source-/Methoden-Semantik und keine universelle Lifecycle-Maschine.

Die passende Zielstruktur bleibt:

```text
Histo scientific semantics
→ canonical state
→ small operational capabilities
→ reactions
→ thin adapters
```

---

## 11. Requirement- und Owner-Disposition

**Kein neuer Requirement-Candidate aus diesem Auditstand.**

Routing:

```text
existing accepted requirement + owner exists
→ implement / validate there

true Requirement gap after concrete consumer/gap check
→ #42

Method gap
→ #60

Technical means / integration
→ #48/#59

Research transition
→ #54

Restart / Evidence Availability
→ #57

Rights / least privilege / untrusted I/O
→ #56/#48

genuine non-derivable Owner decision / blocker
→ #44
```

Aktuell ergibt sich **kein #44-Blocker**.

---

## 12. CI-/Assurance-Nebenbefund

PR #71 löste Project Assurance aus. Regressionstests waren grün; `tools/requirements/validate.py` scheiterte an:

`REQ007 [REQ-WF-001]: Delivery status 'partial' requires a structured QA record`.

Der Fehler bestand bereits auf `main` seit `d52d3d1122d46a7547fb689fc036645933d4c4b7` / Run `33693049140` und wurde an #62 geroutet. Er wird nicht opportunistisch im Audit repariert.

Audit-Relevanz: unprotected `main` kann canonical bleiben, obwohl Push-CI rot ist. Das stützt B1/Failure 16, ist aber keine neue Requirement-Semantik.

---

## 13. Nächster Abnahmeschritt: ein realer Vertical Research Slice

Der Audit ist strukturell erst dann wertvoll, wenn die Schutzgrenzen **im Hintergrund** einer echten Forschungsarbeit wirken.

Empfohlener bestehender Slice, ohne neuen Forschungsauftrag zu erzeugen:

> **#46 / Lampe Nr. 420:** Welche Aussage trägt die tatsächlich inspizierte Editionsinstanz, welche Teile sind editorische Identifikation, welche Archiv-/Originalkonkordanz bleibt unresolved, und kann ein frischer Context exakt bei der nächsten diskriminierenden Aktion fortsetzen?

Warum dieser Slice:

- Source/Representation/Instance/Findspot sind bereits real vorhanden;
- `Grune = Mönchgrün` testet Observation/Editorial Identification/Interpretation;
- moderne Archivkonkordanz ist offen und testet `unresolved` + Evidence Availability;
- zwei digitale Instanzen testen Identity≠Representation≠Availability;
- eine legitime spätere Korrektur testet, dass Transition/History Forschung nicht einfriert;
- fresh-context resume testet B4;
- der Research Owner soll dabei einen **Research Output**, keinen Governance-Report sehen.

Abnahme:

```text
Research question/order
→ concise Research Output
→ source/findspot/evidence/method/history drill-down available
→ next discriminating action explicit
→ fresh context resumes there
→ no repeated prerequisite/no-op work
→ system-learning separately routed after the research result
```

**Erfolg:** weniger Chat-/Governance-Orchestrierung bei mindestens gleicher wissenschaftlicher Sicherheit.  
**Misserfolg:** Owner muss wieder IDs, Owner-Taxonomie, Gate-Status oder interne Assurance manuell verwalten.

---

## 14. Audit-DoD-Status

- [x] 18 Referenz-Failure-Modes dispositioniert;
- [x] reale Beobachtung, conditional risk und wissenschaftliche Dauerinvariante getrennt;
- [x] Root Causes auf sechs Boundaries konsolidiert;
- [x] bestehende Semantic Owner / Requirements / Contracts zugeordnet;
- [x] executable vs. planned vs. scholarly judgement unterschieden;
- [x] adversarial + positive Fixtures abgeleitet;
- [x] kein ungeprüfter Requirement-Delta erzeugt;
- [x] konkrete Consolidation-/Retirement-Liste vorhanden;
- [x] `Wissensarbeit` sauber als generische Strukturreferenz begrenzt;
- [ ] Delivery-Mechanismen unter ihren bestehenden Ownern implementiert und Fixtures grün;
- [ ] realer Vertical Research Slice mit Background-Guards durchgeführt;
- [ ] Research Owner bestätigt geringere Governance-/Orchestrierungslast;
- [ ] erst danach aktive Governance-Doppelungen tatsächlich `retire-active`.

## Stop Rule

Kein neues Meta-Artefakt, Issue, Requirement oder Schutzmechanismus nur deshalb, weil ein Failure Mode benannt werden kann. Ohne aktuellen Root Cause, realen Consumer und nachweisbaren Schutzgewinn bleibt er `conditional | defer | historical evidence`.
