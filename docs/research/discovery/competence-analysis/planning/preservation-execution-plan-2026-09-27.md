# Competence-analysis preservation execution plan

**Status:** `P0 planning freeze / bounded preservation execution contract / no W1 yet`  
**Work Owner:** #150  
**Content Owner:** #22  
**Domain Method Truth:** #60  
**Research Quality:** #45  
**Requirements Authority:** #42  
**Source Lock:** `docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md`  
**Source Lock Blob SHA:** `85d3b7cd38dd14c8f23af8350b4c585828934018`  
**Assurance:** `docs/research/discovery/competence-analysis/planning/assurance-contract-2026-09-27.md`  
**Manifest:** `docs/research/discovery/competence-analysis/planning/execution-manifest-2026-09-27.json`

## Purpose and bounded intent

Preserve the owner-confirmed detailed competence-analysis/scoping state losslessly, reviewably and restartably without silently changing its meaning or promoting it to Method Truth, accepted Requirement, Architecture, or historical finding.

P0 freezes source, plan and assurance. P0 does not execute the preservation run.

## Authority boundary

- #22 owns which competencies / competence boundaries are needed.
- #60 owns later SOTA-based domain-method operationalization and Method Truth.
- #45 owns cross-cutting Research/Evidence quality.
- #42 remains the only owner of accepted Requirements.
- #150 owns only this bounded preservation/assurance work package.
- Workers and the controller gain no independent scholarly, requirement, architecture or priority authority.

# C. Preserved Planning Decisions

| Entscheidung | Disposition | Begründung |
|---|---|---|
| P0 Planning Freeze vor W1 | **KEEP** | Contract, Source, Oracle und Reviewmaßstab müssen vor günstiger Ausführung eingefroren sein. |
| Zwei Phasen: P0 Freeze → Execution Run | **KEEP** | verhindert Vermischung von Planfreigabe und Ergebnisakzeptanz. |
| Source Lock = `owner-confirmed workshop synthesis` | **KEEP** | Project-analysis meaning, keine Domain Evidence/Method Truth. |
| PR #147/#148 = prior derivative / provenance / reconciliation object | **KEEP** | verhindert retroaktive Authority-Laundering. |
| vollständige datierte Analyse-Baseline + dünnes README | **KEEP** | eine kanonische Vollrepräsentation, Navigation getrennt. |
| keine 15/16 Profil-Dateien im P0 | **KEEP** | Dateistruktur darf offene Profilgrenzen nicht ontologisieren. |
| `CA-*` IDs nur lokale Adressierbarkeit | **KEEP** | keine Ontologie/DB-/Graph-Verpflichtung. |
| Quality/Coverage/Open-State/Restart in einer Assurance-Datei | **KEEP** | kleinste hinreichende Struktur; semantische Kapitel bleiben getrennt. |
| W0–W7 als bounded Work Packets | **KEEP + COMPLETE** | Grenzen bleiben, Contracts werden in G vollständig normalisiert. |
| W5 fresh stronger independent context | **KEEP** | complete-looking-but-wrong kann sonst durch formale Coverage unentdeckt bleiben. |
| W1–W4/W6/W7 lower-cost nur quality-equivalent | **KEEP + COMPLETE** | keine feste Modellzuweisung; H spezifiziert Kontrolllogik. |
| maximal 1 automatischer Revision-Zyklus je Gate | **KEEP** | verhindert autonome Loops. |
| eigener dünner Preservation Work Owner | **KEEP** | eigener Scope/DoD/Review/Restart-Gate erfüllt #23; besitzt nicht die Kompetenzsemantik. |
| minimaler PROJECT_STATE-Pointer sobald Preservation Owner aktiv ist | **KEEP** | handoff-relevante aktive Ownership/Next Action muss zentral auffindbar sein; keine Detailduplikation. |
| `Gap Contract` als generische Taxonomie | **CORRECT** | wird durch relationalen Open-State/Closure Contract ersetzt; frischere #53/#54-Semantik. |
| Profilzahl als „15“ | **CORRECT** | heutige Karte bleibt als 15-Familien-Derivat nachvollziehbar, P6 Diplomatik/Textkritik aber analytisch unterscheidbar; finaler Zuschnitt offen. |
| Source Lock Commit/Blob-SHA | **KEEP** | exakte unveränderliche Ausführungsbasis; Blob-SHA bevorzugt. |
| Originaler Planungs-Prompt als P0-Acceptance-Provenienz | **ADD** | nach diesem Audit continuation-critical; ermöglicht künftige Vollständigkeitsprüfung ohne Chat. |

---

# H. Full Routing / Quality-Equivalence Matrix

| Worker | Task character | Semantic risk / consequence if wrong | Detectability / reversibility / reviewability | Independence | Required capabilities / context | Minimum sufficient reasoning | Preferred execution class | Why cheaper route safe/unsafe | Downstream control | Escalation trigger |
|---|---|---|---|---|---|---|---|---|---|---|
| W0 | deterministic transition control | low semantic, high authority-risk if it improvises | highly detectable; fully reversible before next step; manifest-reviewable | no semantic independence needed | exact manifest parse, evidence existence, state counter | minimal/deterministic | rule-based/minimal executor | safe only because it may not interpret content | manifest + STOP on non-determinism | >1 possible transition, missing evidence, retry exceeded |
| W1 | long-source semantic inventory | medium; omission can poison all later completeness | omission detectable by W3/W5 and Oracle; reversible | no, but frozen source mandatory | long-context exact reading, stable anchors, structured output | medium | lower-cost reliable long-context worker | safe because it authors no target meaning and is independently audited | W3 full mapping + W5 challenge | source ambiguity, repeated omissions, context capacity insufficient |
| W2 | editorial semantic transformation | medium-high; fluent drift possible | W3 source comparison + W5 adversarial; reversible before merge | author context | long-form writing, exact mapping, status control | medium to high depending context | lower-cost/medium if fidelity benchmark acceptable | conditionally safe due frozen inputs + exact coverage/review; unsafe if model compresses nuance | W3/W5 | repeated semantic drift or long-context loss → stronger worker |
| W3 | coverage/loss audit | medium-high; false PASS allows loss | exact source+inventory matrix; reversible; highly reviewable | **fresh required** | compare long source, inventory, draft | medium/high | fresh lower-cost/medium if comparison quality sufficient | safe only if Oracle is detailed and all rows explicit | W5 independent | inability to compare all items, ambiguous materiality, false negatives observed |
| W4 | repo reconciliation | medium; wrong owner/provenance could create parallel truth | current repo refs make errors reviewable; mostly reversible | fresh repo read required, not author-independent | GitHub/repo inspection, governance classification | medium | lower-cost/medium with connector | safe because no content meaning is decided; material conflict stops | W5 + owner boundaries | binding conflict, stale state ambiguity, permissions missing |
| W5 | independent adversarial semantic review | **high**; complete-but-wrong is core failure | qualitative; not fully deterministic; review evidence preserved | **mandatory fresh independent** | frozen artifacts, strong reasoning, repo evidence inspection | strongest available needed | strongest reasonable reasoning context | cheaper route unsafe when semantic shift/authority laundering may look fluent and complete | independent verdict itself | independence compromised, material disagreement non-deterministic |
| W6 | accepted-delta integration | low-medium; risk of unreviewed „improvement“ | exact accepted finding map; reversible | no | repo editing/integration, pointer hygiene | low/medium | lower-cost reliable executor | safe because no new meaning allowed and W7 tests result | W7 | integration needs semantic choice/new structure |
| W7 | fresh restart comprehension | medium; false PASS hides chat dependency | empirical, source-path backed, reversible navigation fixes | **mandatory fresh** | fresh repo browsing, comprehension, no hidden chat | medium | fresh lower-cost/medium | deliberately should not need strongest model; if only strongest can reconstruct, handoff itself is weak | fixed oracle | semantic misunderstanding, missing current source, need for chat |

## H1. Quality-equivalence rule

A lower-cost route is permitted only when all four are true:
1. bounded source/authority is frozen;
2. material error classes are explicit;
3. errors are independently detectable downstream;
4. failure does not silently create authority before review.

A stronger route is mandatory when semantic error can survive formal completeness and cannot be reliably reconstructed by deterministic comparison. In this plan that is primarily W5; W2/W3 may also be escalated empirically if first execution shows repeated fidelity loss.

**Current technical automation boundary:** this chat does not possess a tool that programmatically spawns guaranteed-fresh independent Work chats with a chosen model/effort. Therefore the plan freezes semantic routing and next packets; actual fresh-context launch may remain a manual transport action. Manual launch must require no new planning or interpretation.

---

# N2. Preserved Core Contracts: Source Lock, STOP Taxonomy, Automation Boundary

## N2.1 Source-Lock Specification

Planned path:

`docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md`

Planned metadata:

```yaml
title: Owner-confirmed competence-analysis working state
date: 2026-09-27
status: owner-confirmed-analysis-input
epistemic_status: analysis / competence-scoping / no-promotion
source_role: owner-confirmed workshop synthesis
authorship_note: >
  Mixed workshop synthesis. The Human Owner explicitly confirmed this detailed
  state as the semantic basis for continuation. Confirmation establishes intended
  project-analysis meaning, not disciplinary truth.
semantic_authority:
  for_current_analysis_baseline: owner-confirmed
  for_domain_method_truth: none
  for_historical_truth: none
  for_requirements: none
  for_architecture: none
downstream_owners:
  competence_inventory: "#22"
  domain_method_research: "#60"
prior_derivatives:
  - "PR #147 — historical unmerged working derivative"
  - "PR #148 — merged prior chat-audit derivative; reconciliation target"
must_not:
  - import additions from prior derivatives
  - SOTA-correct the source
  - create historical findings
  - promote method status
  - infer final profile taxonomy
```

**Content rule:** The body is assembled from the owner-confirmed detailed analysis state without substantive paraphrastic reduction. Editorial normalization is allowed only where meaning cannot change. Material ambiguity is a STOP, not an invitation to improve wording.

**Lock rule:** after P0 merge, record the exact Git blob SHA of this file as `source_lock_ref` for W1–W7. The merge/Blob freezes execution input; it does not promote domain truth.

## N2.2 STOP Taxonomy

| STOP | Trigger | Why not auto-repaired | Required evidence on return | Handoff / needed decision | State that remains unchanged |
|---|---|---|---|---|---|
| STOP-SEMANTIC | material Source meaning has >1 plausible reading | any repair would choose Human meaning | passage, competing readings, affected INV/QC | Human/Owner clarification | last accepted Source Lock / artifacts |
| STOP-CONFLICT | fresh binding repo state materially conflicts with plan/source status or owner | precedence/authority judgement needed | both refs, exact conflict, impacted plan section | applicable Owner/Governance | no planned mutation or worker continuation |
| STOP-PROMOTION | continuation would create Method/Requirement/Architecture/Historical promotion | different authority required | proposed promotion, current status, required owner | #60/#42/#48/etc as applicable | analysis/scoping status |
| STOP-LOSS | material element cannot be represented losslessly | no legitimate editorial reduction known | missing element, attempted mappings, why loss unavoidable | Steering/Human | last passed baseline |
| STOP-REVIEW-DISAGREEMENT | W5 S2/S3 finding has no deterministic correction | reviewer must not silently become author/owner | finding, Source evidence, artifact evidence, alternatives | Human/Steering | reviewed artifact frozen |
| STOP-AUTHORITY | material decision requires Owner/Acceptance authority not in packet | executor cannot manufacture authority | decision question, owners, consequence | current canonical authority | scope/status/priority unchanged |
| STOP-CAPABILITY | required source/repo operation/independent context unavailable | result cannot be genuinely verified | missing capability/access, affected gate | Human chooses environment/access | current step remains open |
| STOP-SCOPE | worker would need historical research, Domain SOTA or new concept work | outside preservation authorization | exact question/research hook | appropriate research owner | preservation packet unchanged |
| STOP-STRUCTURE | completion appears to require unplanned durable structure/ontology/runtime | architectural choice beyond plan | need, simpler alternatives, affected acceptance | Human/owner | no new structure created |
| STOP-PROVENANCE | source role/origin cannot be determined without invention | false traceability risk | object, competing provenance, current refs | Human/owner if necessary | object not promoted/imported |
| STOP-INDEPENDENCE | W5/W7 cannot meet fresh-context separation | review evidence would be overstated | contamination/constraint, affected review | Human chooses new independent context | no PASS claim |
| STOP-REPEATED-FAILURE | same material QC failure remains after one allowed revision | loop indicates non-deterministic or inadequate repair | first+second finding, attempted repair | Steering | last accepted pre-repair state |
| STOP-ASSURANCE-ESCAPE | W7 discovers material semantic error that W3/W5 should have caught | assurance design itself may be inadequate | wrong reconstruction, affected QC, missed gates | Steering / assurance redesign | no DONE/closeout |
| STOP-CONTROLLER-NONDETERMINISM | W0 cannot derive exactly one transition | controller has no authority to choose | current state, candidate edges, missing condition | Steering / manifest correction | current step/result frozen |

## N2.3 Automation / Technical Feasibility

### A — Semantically automatable
After P0, the following are fully prebound:
- next valid packet after PASS;
- exact allowed repair route after REVISE;
- required evidence;
- retry limit;
- global STOPs;
- completion condition.

No new fachliche planning decision is needed between ordinary PASS transitions.

### B — Technically automatable where an execution environment exposes the required primitives
A suitable environment may be able to:
- read repo artifacts;
- execute a bounded packet;
- write branch/PR artifacts;
- validate structured returns;
- select the exact manifest edge.

This is environment capability, not product architecture or guaranteed behavior.

### C — Prepared but possibly manual transport
The current Chat context does not expose a primitive for programmatically spawning guaranteed-fresh independent Work chats or selecting a specific model/effort for each one. Therefore a Human may need to start the named next fresh context. The only Human action is transport: point the new context at the frozen repo packet. No re-planning or prompt rewriting should be required.

### D — Intentionally non-automatable
- material Human meaning clarification;
- authority/promotion decisions;
- non-deterministic semantic review disputes;
- disciplinary Method Truth / external specialist validation;
- changes outside frozen P0 scope.

**Automation verdict:** semantic orchestration is complete; technical fresh-context spawning is not assumed. This limitation does not block P0 because the deterministic manual-transport fallback preserves quality and boundedness.

---

# L. Persistence / Canonical-Home Matrix

| Information | Persist in P0? | Later Execution only? | Historical evidence only? | Canonical home | Must NOT duplicate into |
|---|---:|---:|---:|---|---|
| Original P0 planning prompt | **yes** | no | no | `planning/p0-planning-prompt-2026-09-27.md` | Issue body, PROJECT_STATE, README full copy |
| Repair prompt | no by default | no | chat/process provenance only | Chat artifact; Git history unnecessary once corrected plan contains repair outcome | canonical plan as parallel spec |
| Corrected P0 execution plan | **yes** | no | no | `planning/preservation-execution-plan-2026-09-27.md` | Issue/README full copy |
| Assurance Contract (QC+Coverage+Open-State+Restart) | **yes** | no | no | `planning/assurance-contract-2026-09-27.md` | individual duplicate QA files unless real lifecycle later emerges |
| Execution Manifest | **yes** | no | no | `planning/execution-manifest-2026-09-27.json` | PROJECT_STATE / issue as second roadmap |
| W1–W7 Work Packets | **yes** | no | no | `planning/work-packets/` | chat-only prompts / issue comments |
| W0 semantics | **yes**, inside execution plan/manifest; no separate packet required unless implementation demands | no | no | plan + manifest | product architecture docs |
| Source Lock / owner-confirmed analysis input | **yes** | no | provenance input | `inputs/owner-confirmed-analysis-2026-09-27.md` | baseline, issue, README as verbatim duplicate |
| Thin competence-analysis README / current map | **yes** | updated at execution close | no | `docs/research/discovery/competence-analysis/README.md` | full profiles/source-lock contents |
| Preservation Work Owner | **yes as Issue**, created only after owner authorizes P0 persistence | status updates during run | no | dedicated thin GitHub Issue | substantive analysis, full QC, worker prompts |
| PROJECT_STATE active pointer | **yes if Preservation Issue becomes active** | reconciled/removed or updated after completion | no | root `PROJECT_STATE.md` | execution details |
| W1 inventory | no on P0; generated later | **yes during execution** | after completion material assurance evidence | run artifact, summarized in `run-assurance.md`; detailed history in PR/Git | baseline content body |
| W2 intermediate draft | no | temporary | yes after finalization | PR/Git history only unless needed for a material review finding | main branch as separate permanent truth |
| W3 coverage/loss audit | no | **yes** | assurance evidence | run artifact → `run-assurance.md` material summary | issue full copy |
| W4 repo reconciliation | no | **yes** | assurance/evidence | run artifact → `run-assurance.md` | README full matrix |
| W5 independent adversarial review | no | **yes** | material assurance evidence | run artifact → `run-assurance.md`; detailed review in PR/Git | issue as duplicated review body |
| W6 integration scratch/diff | no | temporary | yes | PR/Git diff | main as separate file unless material reasoning requires it |
| W7 restart evidence | no | **yes** | material assurance evidence | run artifact → `run-assurance.md` | PROJECT_STATE full test output |
| Final analysis baseline | no in P0 | **yes after execution** | no | `analysis-baseline-2026-09-27.md` | Issue/README/#22/#60 comments full copy |
| Final run assurance | no in P0 | **yes** | no while current assurance record | `runs/2026-09-27-preservation/run-assurance.md` | separate permanent W1/W3/W4/W5/W7 files unless necessary |
| #22 pointer | no in P0 unless P0 needs planning pointer; final pointer at execution close | **yes final** | no | short issue comment/status update on #22 | profile content |
| #60 pointer | no in P0 unless planning navigation needed; final pointer at execution close | **yes final** | no | short issue comment/status update on #60 | Method Truth or profile contents |
| PR #147 | already exists | no | **yes** | historical GitHub PR | copied into new baseline |
| PR #148 + chat-audit file | already current repo content | reconciliation during execution | **yes as prior representation once new baseline supersedes it as current analysis view** | existing PR/file; new README points to relation | deleting/re-writing history; importing as source |
| Chat transcript | no | no | transient workshop provenance | Chat only unless specific material statements selected into Source Lock | repo full transcript archive |
| Private model reasoning | no | no | no | nowhere | repository |
| Intermediate editorial drafts | no | temporary | Git history if committed in execution branch | PR/Git history | permanent main clutter |

## L1. Minimal permanent repository structure after successful run

```text
docs/research/discovery/competence-analysis/
├── README.md
├── analysis-baseline-2026-09-27.md
├── inputs/
│   └── owner-confirmed-analysis-2026-09-27.md
├── planning/
│   ├── p0-planning-prompt-2026-09-27.md
│   ├── preservation-execution-plan-2026-09-27.md
│   ├── assurance-contract-2026-09-27.md
│   ├── execution-manifest-2026-09-27.json
│   └── work-packets/
│       ├── W1-material-inventory.md
│       ├── W2-baseline-authoring.md
│       ├── W3-coverage-loss-review.md
│       ├── W4-repository-reconciliation.md
│       ├── W5-independent-adversarial-review.md
│       ├── W6-final-integration.md
│       └── W7-fresh-restart-test.md
└── runs/
    └── 2026-09-27-preservation/
        └── run-assurance.md
```

**Simplification decision:** keine separaten dauerhaften `coverage-oracle.md`, `gap-contract.md`, `restart-oracle.md` und keine 15/16 Profil-Dateien. Diese Semantiken sind Kapitel des `assurance-contract` bzw. der finalen Baseline.

---

# N3. Planning Self-Challenge P-F01…P-F15

Der bereits entwickelte Self-Review wird als Teil des korrigierten Assurance-Vertrags beibehalten und gegen die vervollständigte Planung erneut geprüft.

| ID | Risiko | Schutzmechanismus im korrigierten Plan | Residual Risk | Kill-/Simplification-Kriterium |
|---|---|---|---|---|
| P-F01 | Aus einem einmaligen Sicherungsproblem entsteht eine Agentenarchitektur | W0 ist nur deterministische Transition-Semantik; W1–W7 sind Run-Work-Packets; #61-/#52-Grenzen verbieten MAS/Workflow-Engine-Ableitung | spätere Bequemlichkeit könnte den Run verallgemeinern | keine Runtime/Plattform bauen, solange manuelle/deterministische Übergabe genügt; wiederholter realer Bedarf wäre neuer, separat zu autorisierender Scope |
| P-F02 | Planung wird selbst zum „bleiernen Schiff“ | Quality/Coverage/Open-State/Restart werden in einem Assurance-Contract gebündelt; Issue/README bleiben dünn | Assurance-Datei bleibt umfangreich | nach realem Run prüfen, welche Felder tatsächlich diskriminierend waren; nicht wirksame Redundanz streichen |
| P-F03 | künstliche Dateimodularität ohne eigenen Lifecycle | keine einzelnen Profil-Dateien; getrennte Work Packets nur wegen separat ausführbarer/reviewbarer Grenzen | sieben Packet-Dateien können sich als überfein erweisen | Pakete zusammenlegen, wenn reale Ausführung keine unabhängige Transition/Review-Grenze benötigt |
| P-F04 | Source Lock konserviert Fehler als „Wahrheit“ | Source Role = `owner-confirmed analysis input`, nicht Domain Evidence/Method Truth; spätere #60-SOTA darf widersprechen/reframen | zukünftige Leser könnten „confirmed“ überlesen | harte Status-/Non-Promotion-Header + W7-Test; bei wiederholtem Missverständnis Benennung weiter schärfen |
| P-F05 | Owner-Analyse wird als wissenschaftliche Evidenz behandelt | QC-04/QC-09/QC-14; Source Lock besitzt explizit keine Historical-/Method-/Requirement-Authority | semantisch plausible Profilregeln klingen fachlich autoritativ | jede fachliche Gültigkeitsbehauptung ohne SOTA-/Methodenevidenz = FAIL/STOP-PROMOTION |
| P-F06 | QA prüft nur Form statt Bedeutung | W3 prüft Inventory→Draft semantisch; W5 enthält `complete structure / wrong meaning` als adversarial case | ein gemeinsamer Bias könnte Source und Draft gleich falsch lesen | Fresh W5 + Source-Lock-Direktvergleich; W7 Assurance-Escape als zusätzlicher Backstop |
| P-F07 | Reviewer ist nicht wirklich unabhängig | W5/W7 brauchen frischen Kontext, frozen inputs, keine author reasoning narrative/expected verdicts | Produktumgebung kann Freshness nicht technisch garantieren | fehlende Independence = STOP-INDEPENDENCE; Reviewstärke nicht überclaimen |
| P-F08 | günstigere Worker erhalten zu viel Interpretationsmacht | Source Lock + Oracle + Outer Contract + W3/W5; günstige Route nur bei Quality Equivalence | bestimmte Worker könnten wiederholt semantisch driften | wiederholter materieller Drift → diesen Slice stärker routen oder enger schneiden; nicht Qualität gegen Kosten tauschen |
| P-F09 | Automation verschiebt Authority in Controller | W0 darf nur exakt eine Manifestkante wählen; `STOP-CONTROLLER-NONDETERMINISM` | implizite Priorisierung könnte in Transition-Logik rutschen | jede nicht deterministisch ableitbare Wahl stoppt; kein Controller-Code/Planner ohne neuen Requirement-/Owner-Scope |
| P-F10 | `REVISE` erzeugt Endlosschleifen | max. ein automatischer Revision-Zyklus je Gate; gleicher materieller Failure erneut → STOP-REPEATED-FAILURE | unterschiedliche Symptome könnten gleichen Grund verdecken | W5/Steering darf gemeinsamen Root Cause als STOP behandeln; keine offenen autonomen Loops |
| P-F11 | Artefakterzeugung wird mit Erkenntnis-/Capability-Closure verwechselt | Open-State Contract trennt Persistence/Representation von Erkenntnis/SOTA/Validation/Human Understanding/Capability | Begriff „closed“ kann weiterhin missverstanden werden | Closure immer mit Evidence/Authority aus F; Dokumentexistenz allein nie Domain-/Human-/Capability-Closure |
| P-F12 | PR #147/#148 werden heimlich Standard | Forbidden Override Inputs in W1/W2; W4 nur Reconciliation; QC-09 | repo-first Bearbeiter könnten merged #148 intuitiv priorisieren | Current Map/Source Lock muss Source-of-Meaning-Regel explizit machen; W7 testet genau diesen Trap |
| P-F13 | vier Schichten / 15 Profile werden Ontologie | eine Baseline statt Profil-Dateien; P6a/P6b nur adressierbare Analyseunterscheidung; QC-18 | IDs können psychologisch Stabilität suggerieren | `retain | split | merge | reframe` explizit offen; Profil-Split erst bei realem #60-Lifecycle |
| P-F14 | Token-/Kostenoptimierung senkt Qualität | #48-Quality-Equivalence; strongest context für W5/STOP-Auflösung; low-cost nur mit nachgelagerter Erkennbarkeit | Verifizierbarkeit kann überschätzt werden | sobald materieller Fehler nicht unabhängig kontrollierbar ist → stärkere Route; Kosten niemals alleinige Begründung |
| P-F15 | Assurance kostet mehr als geschützter Nutzen | permanente Struktur bleibt klein; Run-Evidence wird in `run-assurance.md` verdichtet; kein neuer Runtime-Bau | einmaliger Preservation Run ist vergleichsweise klein | nach erstem Run Meta-Aufwand gegen vermiedenen Verlust messen; nicht diskriminierende QA/Dateien entfernen oder zusammenführen |

**Self-Challenge verdict:** kein P-F-Risiko verlangt derzeit eine neue Owner-Entscheidung oder technische Plattform. Die relevanten Risiken bleiben durch reversible, run-lokale Contracts kontrolliert. Das größte verbleibende reale Risiko ist nicht Strukturmangel, sondern semantische Verwechslung von Source Lock, Analyse-Baseline und späterer Method Truth; deshalb bleiben W3/W5/W7 und die Statusgrenzen unverzichtbar.

---

# Execution graph

```text
P0 frozen
→ W1 Material Inventory & Open-State Mapper
→ W2 Baseline Author
→ W3 Coverage & Loss Auditor
   REVISE → W2 (max one automatic material repair cycle)
   PASS → W4
→ W4 Repository Reconciliation
   PASS → W5
→ W5 Independent Adversarial Review
   bounded REVISE → named earlier step
   PASS → W6
→ W6 Final Integration
→ W7 Fresh Restart / Handoff Test
   navigation-only REVISE → W6
   material semantic failure → STOP
→ DONE
```

A repeated material failure, controller ambiguity, semantic ambiguity, authority conflict, provenance failure, scope expansion, independence failure or unauthorized promotion is a STOP.

# P0 merge meaning

P0 merge means only that the Source Lock, execution plan, assurance contract, manifest and work packets are frozen as the bounded execution basis. It does not validate domain methods, historical claims, Requirements, Architecture, final competence taxonomy or any worker output.

After P0 merge, W1 is merely the next permitted action. It still requires explicit execution authorization.
