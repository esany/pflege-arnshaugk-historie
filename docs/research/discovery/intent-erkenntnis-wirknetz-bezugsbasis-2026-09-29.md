# Histo-Orla – Intent–Erkenntnis–Wirknetz-Bezugsbasis

**Stand:** 2026-09-29  
**Work Owner:** #154  
**Status:** `working-reconciled-reading-view / Human-meaning + current-system assessment / no Requirement or Architecture promotion`  
**Predecessor:** `docs/research/discovery/intent-bestandsaufnahme-2026-09-24.md`  
**Project-state basis:** `main@8dd82427019d4faeb476a10191345a128abc0607`  
**Cross-repo Human-meaning / prior-art evidence:** `esany/Wissensarbeit` #53, especially comments `5831348317` and `5833820505`

> This artifact is the current Histo-Orla reading view for Owner intent, Erkenntnis, Information Space and their relation to the existing system state. It does not create Requirement, Method Truth, Architecture, Generic-Fit or implementation authority.

---

## 1. Purpose and boundary

This artifact reconciles the read-only intent inventory from 2026-09-24 with later Human-primary and Human-confirmed corrections from 2026-09-25.

It exists because the 2026-09-24 inventory correctly preserved many Owner signals but still treated parts of `Intent ↔ Erkenntnislücke` as open modelling questions and retained a stronger Gap-oriented framing than the later Human correction supports.

The reconciliation must preserve five boundaries:

1. Human wording is not AI wording.
2. Human confirmation is not automatic confirmation of every downstream implication.
3. Human meaning is not the same authority layer as accepted Requirements.
4. Repository/system observations are not evidence of Human cognition or acceptance.
5. Unresolved representation and implementation questions remain unresolved.

This artifact does **not** overwrite the 2026-09-24 inventory. That file remains historical evidence of the then-current reconstruction.

---

## 2. Source-role and authority rules

### 2.1 Evidence roles for Human meaning

This artifact uses the following roles:

- `HP` — Human Primary Evidence: verbatim Human Owner wording is preserved.
- `HC` — Human Confirmation / Correction: explicit Human acceptance, rejection or correction of an interpretation.
- `HPP` — Human-feedback paraphrase: repository evidence reports Owner feedback but the original Human wording is not retained in the same artifact.
- `OBS` — repository observation: directly inspectable project state, artifact, code, status, issue, PR, test or behavior.
- `AI-A` — AI analysis: analytic derivation from evidence.
- `AI-S` — AI synthesis: integrative formulation created by AI.
- `EXT` — external / prior-art evidence.

An AI paraphrase must never later be presented as Human wording.

### 2.2 Authority remains separate

For Histo-Orla project truth the repository precedence remains binding:

`governance / accepted Requirements / ADRs → canonical artifacts → current Work Owner → PROJECT_STATE → older concepts → chat`.

For Human meaning, however, accepted Requirements do not automatically prove the current Human Intent. Conversely, a Human statement does not itself mutate an accepted Requirement.

If current Human meaning and current project representation diverge, the divergence is recorded. It is not silently reconciled by either direction.

### 2.3 Cross-repo boundary

`esany/Wissensarbeit` #53 is used here because it contains Owner-primary and Owner-confirmed wording about the Histo-Orla problem and the later Wirknetz / Erkenntnis / Informationsraum correction.

It is **not** Histo-Orla Requirement, Method or Architecture authority.

---

## 3. Human Evidence Ledger

The entries below are material to the current reference basis. They are not an exhaustive archive of every Owner statement.

### HP-01 — Erkenntnislücke hinter dem Intent

**Source:** Owner-primary wording preserved in Wissensarbeit #53 comment `5831348317`; Histo project-context evidence.  
**Role:** `HP`

> “Ich kann mir intents aber auch vorschlagen lassen und dann justieren
> 
> - die Bedürfnisse sind ja schon da.. bzw. Das ganze netz. Was noch
> eine grösse wäre: erkenntnislücke hinter dem intent”

Later Owner clarification recorded in the same evidence:

- “Das ganze netz” in this statement referred to the existing Need/Requirement network in Histo-Orla, not to an Information Space.

**Meaning supported:** Intent has an epistemic dimension not exhausted by the already-modelled Need/Requirement network.

**Relation to later evidence:** `refined` by HP-07/HP-08 and HC-01; not superseded.

---

### HP-02 — Erkenntnis remains cognitive

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “Und die letzte erkenntnislücke passiert in meinem kopf, weil das
> System mir einen informationsraum bietet in dem ich all meine
> erkenisdlücken schließen kann, weil sie passfähigkeit zu meinen
> Kompetenzen schaffen”

**Meaning supported:** The system may create conditions for Human understanding, but the final epistemic change occurs in the Human, not as a software state.

**Current limit:** The wording does not itself define a technical Information-Space representation or a measurable closure metric.

---

### HP-03 — scientific safeguards are not opposed to Owner needs

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “Unsicherheit, provienz standards an fachliche wissenschaftlichkeit
> und evidenz ist keine widersprüche zu meinen Bedürfnissen.”

**Meaning supported:** Human accessibility / usefulness must not be interpreted as permission to remove uncertainty, provenance or scientific evidence standards.

**Relation:** `unchanged`; reinforced by current Requirements such as REQ-EPI-004/005, REQ-SYN-002 and REQ-UX-001/003.

---

### HP-04 — Motorraum vs Human-facing result

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “Die Agenten erstellen die logik das System und managen es, das ist
> der ganze technologische wie auch der domainspezifische part
> aber!!!!!! Das ist der Motorraum, in den ich schon auch reinschauen
> kann, das Ergebnis muss aber ein informationsraum für mich sein.
> Und der motorraum braucht echtes Development”

**Meaning supported:** Domain and technical complexity belong primarily in the system/development layer; the Human should be able to inspect relevant foundations but should not be forced to operate the whole motor room as the primary research experience.

**Unresolved:** `Agenten` here does not by itself establish a product Multi-Agent architecture or runtime topology.

---

### HP-05 — foundations inspectable; representation not limited to UI

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “Versteh mich nicht falsch, ich will dennoch eine gewisse Kontrolle
> über die fundamente. Kein ui, das ich hinbekommen mus und dann
> wieder selbst hermetisch ist und nicht mehr pflegbar. Auch
> wissensstrukturen können schon der erste informationsraum sein, oder
> entsprechend aufbereitetes wissen.. eine karte statt Koordinaten..
> wir sind noch im bauen und da ganz am Anfang und die Baustelle steht
> im Morast..”

**Meaning supported:** The Human needs meaningful control/inspectability of foundations; Information Space is not synonymous with a finished UI; structured knowledge or prepared knowledge can already form an Information Space.

**Unresolved:** exact technical mechanisms for control, inspectability and maintenance.

---

### HP-06 — intent-relative completeness

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “Aber hier muss sich der agent doch beweisen und es kompatibel für
> mich machen? Ich prüfe und schaue auf Vollständigkeit”

Owner clarification in the same evidence:

- `Vollständigkeit` means completeness against the Intent, not graph completeness.

**Meaning supported:** The Human may validly judge whether the result materially covers what the Intent requires.

---

### HP-07 — Generic Gap rejected

**Source:** Wissensarbeit #53 comment `5831348317`; current-chat Owner-primary evidence preserved there.  
**Role:** `HP`

> “Gap - ist zu schwach - du verflachst das immer wieder, es ist nicht irgendeine Lücke, sondern mir geht es hier um Erkenntislücken - andere Lücken beziehen sich auf andere systematische Logiken - es geht hier auch um semantische relationen .. was muss verstandern werden, was muss ich verstehen als übergeordnete Denkstruktur und Prüfinstanz .. was verstehe ich jetzt nicht und was kann ich nach dem DONE verstehen.”

**Meaning supported:** `Erkenntnislücke` is epistemically specific. A generic Gap superclass is too weak when it erases the different logic of system, capability, authority, requirement or other open conditions.

**Disposition:** Earlier generic-Gap semantics remain historical candidate material, not the current Human-meaning reference for this Histo slice.

---

### HP-08 — one systemic whole, not a second epistemic subsystem

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “puh, du machst schon wieder eine zweite logik auf und zerstückelst den ansatz .. Die Erkenntnislücke steht nicht isoliert im Raum .. Meine Denkfigur war doch immer etwas systemisches ganzheitliches .. Intent - Erkenntnislücke - Pain - Ziel - BEdürfnisse - Anforderungen - Rahmenbedingungen - Capabilities - Ergebnis schafft Informationsraum der Erkenntnis ermöglicht .. Informationsraum kann versch. Reifegrade haben. Erkenntnis ist etwas kognitives, es kann sich nicht in der Software materialisieren”

**Meaning supported:** Intent, Erkenntnis, Pain, Goal, Need, Requirement, Constraint, Capability and Result belong to one relational whole; epistemic questions must not be split into a detached second system; Human Erkenntnis remains cognitive.

---

### HP-09 — implicit Intent/epistemic frame and explicit work perspectives

**Source:** Wissensarbeit #53 comment `5831348317`.  
**Role:** `HP`

> “es geht ja aber gerade um den systemischen punkt zwischen der Intent-Erkenntnisklammer, was ja oft eher meta und nur implizit kommuniziert wird, oder gar nicht und den offensichtlichen Ausdrücken des Nutzers in ziel - pain - Bedüfrnis, anforderung, Rahmenbedingungen, Capabilities, Ergebnis - ist das greifbare um das Ziel zu erreichen .. alle punkte beantworten versch. Perspektiven in der Problemanalyse / -konzeption / - entwurf .. / development .. und das sind systemische relationale wirknetzt
> 
> .. also hier greift wieder user reserach, menschenzentrierte technikgestaltung, Behavior driven development ..”

**Meaning supported:** The Intent–Erkenntnis frame may remain implicit while Goals/Pains/Needs/Requirements/Capabilities/Results express different concrete perspectives on the same systemic problem and development context.

**Limit:** The named disciplines are orientation, not automatic Method Truth for this artifact.

---

### HC-01 — owner-confirmed Wirknetz / Erkenntnis / Information-Space baseline

**Source:** Wissensarbeit #53 comment `5833820505`.  
**Role:** `HC`

The Human explicitly corrected the direction and confirmed the current conceptual baseline.

Material protected meanings include:

- one systemic relational Wirknetz;
- Intent and relevant Erkenntnis/Erkenntnislücke belong together;
- Erkenntnislücke is specifically epistemic, not a universal label for bugs/capabilities/authority/requirements;
- Pain, Goal, Need, Constraint, Requirement, Capability, Behavior and Result remain distinct perspectives/functions;
- results may create or organize an Information Space;
- Human cognition/decision remains distinct from artifact/software state;
- Information Space is evaluated relative to Intent and relevant Erkenntnis/decision rather than representation type;
- Human use/judgement/learning may revise Intent and downstream project understanding;
- representation remains deliberately open.

This confirmation does **not** create an accepted Histo Requirement, ontology or Architecture decision.

---

### HC-02 — representation stays late-bound

**Source:** Wissensarbeit #53 comment `5833820505`.  
**Role:** `HC`

> “die frage der Repräsentation des informationsraumes würde ich jetzt erstmal aussen vor lassen, das ist aktuell bewusst offen und flexibel - eher, wie muss es bezogen auf die Erkenntnis beschaffen sein..”

**Meaning supported:** Do not currently select UI, graph, dashboard, report, view, data model or storage structure as the definition of Information Space.

---

### HC-03 — Histo-Orla must not be narrowed to one knowledge case

**Source:** Wissensarbeit #53 comment `5833820505`.  
**Role:** `HC`

> “Horst orla ist überhaupt keine begrenzung auf einen wissensfall, dann hast du nur ersten Piloten gelesen - oder gar nicht ins repo geschaut - die informationsraumfrage ist aus meiner Sicht 1:1 übertragbar”

**Meaning supported:** Current Histo-Orla intent cannot be reconstructed from a single pilot or narrow knowledge case.

**Limit:** This is Human design meaning, not external scientific Generic-Fit proof.

---

## 4. Chronological reconciliation

### 4.1 Earlier Histo baseline

The canonical problem baseline already protected important parts of the current intent:

- G-001: a durable functioning transdisciplinary research system, not a concept paper or AI demonstrator;
- G-002: the Research Owner may ask imprecisely; the system performs professional problem translation;
- G-003: domain standards and evidence rules lead;
- G-004/G-006: source/findspot traceability and epistemic layer separation;
- G-007: automate recurring mechanical work where it reduces real friction or improves quality;
- G-008: restartable/provider-independent canonical Research State;
- G-009: scientific complexity understandable to the Research Owner and auditable by specialists;
- G-011/G-012: Development serves validated Needs/Requirements; Lean reduces unnecessary complexity, not scientific depth.

These remain materially compatible with the later Human correction.

### 4.2 Real workflow corrections before 2026-09-24

Repository feedback before the intent inventory already showed a repeated non-equivalence:

`formal/technical correctness != Owner-effective research quality`.

Observed examples include:

- excessive Chat/Markdown/context orchestration despite existing requirements;
- rejection of a static module model even though it was structurally coherent;
- owner feedback that a technically correct audit/provenance path was too cryptic and machine-oriented;
- rejection of the first reaction that reduced the solution to a smallest visual Derived View.

These are not proofs of one technical solution. They are evidence that artifact existence, formal structure and technical verification are insufficient quality measures for the Owner intent.

### 4.3 2026-09-24 inventory

`intent-bestandsaufnahme-2026-09-24.md` was a necessary and largely source-conscious reconstruction. It identified several intent lines, preserved selected Owner wording and introduced a working Information-Space view.

Its limit is chronological: the later 2026-09-25 correction further rejects Generic Gap flattening, explicitly protects the Wirknetz semantics and keeps Information-Space representation late-bound.

Disposition:

- 2026-09-24 artifact = historical predecessor / useful evidence and analysis;
- this artifact = current Histo reading view for the reconciled Human meaning;
- accepted Requirements remain separately owned by #42.

---

## 5. Current conceptual reference — AI synthesis constrained by Human evidence

The following is `AI-S`, not Human wording and not an accepted ontology:

```text
SYSTEM / DOMAIN / DEVELOPMENT
           │
           │ produces / organizes
           ▼
   INFORMATION SPACE
externally available and inspectable
           │
           │ meets
           ▼
Human + Intent + prior understanding
           │
           ▼
    EPISTEMIC SPACE
what thereby becomes epistemically possible
           │
        use / thinking
           ▼
     HUMAN ERKENNTNIS
           │
           ▼
 judgement / decision / learning
           │
           └──────────────↺ relational feedback network
```

This synthesis must be read together with these non-flattening rules:

- Intent != Goal;
- Intent != Need;
- Pain != Cause;
- Pain != Erkenntnislücke;
- Erkenntnislücke != Capability Defect;
- Erkenntnislücke != Authority Gate;
- Need != Requirement;
- Requirement != Capability;
- Capability != Behavior;
- Result != Human Erkenntnis;
- Verification != Human Validation;
- Human Validation != factual/domain correctness;
- Relation != mere Trace Link.

The network is recursive and revisable, not a mandatory one-way pipeline.

---

## 6. Two separate completeness criteria

### 6.1 Relation correctness

A complete-looking semantic or trace graph may still be wrong.

Therefore:

> `relation correctness > relation/graph completeness`

Practical meaning:

- do not invent a Requirement→Intent relation because it looks plausible;
- do not infer Owner acceptance from a passing test;
- do not infer Human understanding from a generated explanation;
- preserve candidate/unresolved relations when evidence is insufficient.

### 6.2 Intent-relative completeness / coverage

Separately, the Human may validly ask whether the result covers the material aspects required by the Intent.

This is not graph completeness.

A scientifically careful but materially incomplete Information Space may still be insufficient for the Intent.

This makes intent-relative coverage a real quality question while preserving incomplete-but-correct semantic state.

---

## 7. What must become understandable / judgeable for Histo-Orla

The following is `AI-A`, derived from the Human evidence plus accepted Histo Requirements. It is a working epistemic reference, not a new Requirement set.

For real historical work the Information Space should, where relevant to the Intent, make it possible to inspect and relate:

1. what is directly evidenced and by which Source/Representation/Instance/Findspot;
2. what the evidence can and cannot support;
3. which transformation/editorial/analytical layers intervene;
4. which interpretations or explanations are current candidates;
5. which alternatives, contradictions or unresolved states remain;
6. which domain methods/evidence rules constrain the inference;
7. which source dependencies prevent false corroboration;
8. what important evidence is still missing;
9. what could discriminate among competing explanations;
10. what relevant system or method limitation currently blocks the work;
11. how the current answer/research state can be challenged and traced back to its foundations;
12. what next action is meaningful without forcing the Human to reconstruct the motor room first.

The required depth and representation may differ by Intent and case.

---

## 8. Current Histo-Orla Information Spaces — repository observations

Histo-Orla already produces several forms of Information Space. They are not absent; they are fragmented and differently mature.

### 8.1 Research dossiers / excerpts

Case artifacts such as the U2 Deutschorden / Mönchgrün excerpt dossier already combine:

- Source and inspected digital instance;
- exact printed/scan findspots;
- historical wording;
- editorial interventions;
- source-explicit observations;
- statement limits;
- working findings;
- unresolved questions;
- historical hypotheses;
- research hooks.

This is a strong positive example of an evidence-near Information Space.

It does not establish that long Markdown dossiers are the correct general Human representation.

### 8.2 Source ledgers / access indices

These provide strong identity, provenance, availability and restartability support.

They are highly valuable motor-room / grounding mechanisms.

A Source Ledger alone is not equivalent to the complete Human epistemic task.

### 8.3 Audit / Trace / Handoff spaces

Histo has comparatively mature formal mechanisms for:

- Requirement structure and assurance;
- Goal/Need/Pain → Requirement → Decision → Delivery → Feedback traceability;
- Work Context and restartability;
- bounded execution/handoff;
- source/findspot auditability.

These are protective and reconstructible but can become machine-oriented if presented directly as the main Human research experience.

### 8.4 Semantic-fidelity / preservation spaces

The competence-analysis preservation run under #150 is current positive evidence that complex Owner-confirmed meaning can be inventoried, represented, independently checked and sent back for revision without promoting it to Method Truth/Requirement/Architecture.

W1 preserved broad material coverage; W2 authored a baseline; a genuinely fresh W3 review returned `REVISE / return to W2` rather than manufacturing PASS.

This is a strong semantic-fidelity mechanism.

It also shows residual workflow burden: a fresh-context review required manual transport/routing.

### 8.5 External capability loading

PR #149 provides bounded evidence that Histo can discover and load one preserved external capability from repository state without the Owner relaying Skill text, prompt or version at use time.

The final pilot disposition is `ADAPT`, not Operational Admission or Generic Fit.

This reduces one motor-room burden but does not demonstrate general orchestration autonomy.

---

## 9. Current intent-relative coverage assessment

The following table is `AI-A`. It summarizes current observable coverage and deliberately does not infer Human cognition from system state.

| Area | Current assessment | Basis / limit |
|---|---|---|
| Scientific provenance / Source Identity | strong | mature requirements and bounded real implementations |
| Uncertainty / alternatives / unresolved | strong conceptual protection | broad operational coverage still incomplete |
| Requirements / Decision / Verification traceability | strong formal layer | Human meaning upstream is only partially represented |
| Restartability / repo handoff | strong but not frictionless | fresh-context/manual routing remains in some workflows |
| Evidence-near research dossiers | materially present | fragmented, case/document oriented |
| Professional problem translation | specified, operationally incomplete | delivery coverage not generally verified |
| Expertise / Domain Method routing | specified / research-needed | #60 and related delivery incomplete |
| OCR/HTR | largely undelivered | delivery coverage mostly not-started |
| Historical retrieval | largely undelivered | exact/auditable general search not delivered |
| Cross-domain synthesis | specified, not generally delivered | current research can synthesize manually/AI-assisted, not established system capability |
| Human-readable progressive Information Space | partial | REQ-UX-001/002/003 not generally delivered |
| Human-effective Erkenntnis/decision support | weakly evidenced | technical verification cannot substitute Owner validation; prior negative feedback exists |
| Low Human orchestration/routing burden | improved but incomplete | capability self-loading helps; manual review/handoff routing persists |
| Intent → Erkenntnis → G/N/P → Requirement genealogy | semantically incomplete | formal assurance begins mainly at G/N/P |

---

## 10. Reconciliation against Goals / Needs / Requirements / Capabilities

### 10.1 Strongly aligned existing system semantics

The later Human correction does **not** invalidate the accepted Histo basis.

It is strongly aligned with existing elements such as:

- G-002 / N-001 / CAP-01 — imprecise question → professional problem translation;
- N-002/N-003 / CAP-02 — expertise routing;
- N-014 / REQ-EPI-004 / CAP-10 — unresolved, contradiction and uncertainty remain valid states;
- REQ-EPI-005 — AI output is not evidence or independent validation;
- REQ-SYN-001/002 / CAP-15/16 — preserve evidence axes and alternatives;
- REQ-UX-001/002/003 / CAP-17 — auditability, challengeability and progressive disclosure;
- CAP-19 — automate repeatable mechanical work without silently automating judgement;
- CAP-20 / REQ-STATE-* — portable/restartable state;
- REQ-TRACE-001 — real Owner feedback closes the delivery loop.

### 10.2 Where current representation begins too late

The formal project loop is currently expressed primarily as:

`Goal / Need / Pain → Requirement → Decision → Delivery → Feedback`.

This is valuable and accepted.

But the Human evidence now makes visible an upstream/around-it frame:

`Intent ↔ what must be understood/judged ↔ current epistemic limit`.

That does not imply a mandatory new schema or Requirement.

It means only that G/N/P/REQ are **not sufficient evidence by themselves** to reconstruct the current Human Intent and epistemic task.

### 10.3 False traceability guard

A Requirement may be canonical and correct while its relation to a specific current Owner Intent remains unproven.

The correct state in such a case is not to delete the Requirement and not to fabricate the relation.

It is to keep the Requirement authority and the Human-meaning evidence separate until the relation is supported.

---

## 11. Protective mechanisms that must not be confused with the problem

Current friction does not justify removing the following safeguards:

- Source / Representation / Instance / Derivative / Findspot separation;
- AI != evidence;
- uncertainty and unresolved as legitimate states;
- method/evidence/authority separation;
- independent/fresh review where consequence requires it;
- formal invariant enforcement where deterministically checkable;
- restartability without chat memory;
- owner-workflow acceptance separate from technical verification;
- no silent Requirement or quality reduction by Development.

These mechanisms directly support the Human statement that scientific uncertainty, provenance and evidence are not contradictions to the Owner needs.

The problem occurs when their operation or representation becomes the Human's primary workload rather than the motor room supporting the Information Space.

---

## 12. Material tensions / unresolved relations

### U-01 — Information-Space representation

`unresolved / intentionally late-bound`

No current authority selects UI, dashboard, graph, report, knowledge structure, application or view as the generic representation.

### U-02 — exact representation of Erkenntnisinteresse / Erkenntnislücke

`unresolved`

The conceptual meaning is sufficiently bounded for this reading view, but no canonical persistent object/schema is selected.

### U-03 — Human competence fit

`supported as Human intent / operational measure unresolved`

The Human wants an Information Space compatible with their competencies. Exact measurable dimensions and interaction design remain open.

### U-04 — control over foundations

`supported as Human intent / concrete mechanisms unresolved`

The Owner wants meaningful control/inspectability and rejects hermetic systems. The exact mix of transparency, repairability, configuration, export or direct manipulation is not yet established.

### U-05 — agent language

`Human wording supported / architecture implication unresolved`

The Human uses agent/system language for motor-room autonomy. This does not prove a runtime Multi-Agent architecture.

### U-06 — Human-effective closure

`must not be inferred`

A result, explanation, view, CI PASS or capability output cannot establish that a Human epistemic/decision burden is closed. Appropriate Human validation is required where closure is claimed.

---

## 13. Current material problem formulations — no solution selection

The following are `AI-A` problem implications only.

### PI-01 — Human-meaning reconciliation lag

Histo-Orla's currently referenced intent-reading view predates the 2026-09-25 owner-confirmed Wirknetz correction.

This artifact closes that **reading-view** lag without changing Requirements.

### PI-02 — Information-Space integration gap

Histo has strong scientific safeguards and several useful information artifacts, but they are not yet integrated into a generally demonstrated intent-relative Information Space for the Owner.

### PI-03 — Human-effectiveness evidence gap

Technical/formal verification is substantially stronger than evidence that the Owner's understanding, judgement and orchestration burden has materially improved.

### PI-04 — motor-room burden remains

The system has reduced some manual relay and restart burden, but fresh-context transport, work routing and interpretation of multiple technical artifacts can still fall to the Human.

### PI-05 — core research capability coverage remains incomplete

Several central capabilities described by accepted Requirements/Capability Map remain `not-started`, `partial` or `research-needed`, especially retrieval, OCR/HTR, Domain Method operationalization, broad synthesis and Human-readable owner-facing flow.

### PI-06 — semantic genealogy is not fully represented by current formal trace

The accepted traceability spine protects G/N/P → Requirement → technical delivery well. It does not by itself reconstruct the Intent–Erkenntnis frame now visible in Human evidence.

No technical remedy follows automatically.

---

## 14. Owner clarification status

For this reference-basis reconstruction:

`NO CURRENT OWNER CLARIFICATION REQUIRED`.

The existing Human-primary and Human-confirmed evidence is sufficient to preserve the current conceptual reading without inventing the unresolved representation details.

Future Owner questions should be raised only when a materially consequential meaning cannot be derived from evidence and competing readings would change the quality target or allowed action.

---

## 15. Non-promotions

This artifact creates no:

- new accepted Requirement;
- Requirement modification;
- architecture choice;
- runtime/Skill contract;
- Information-Space ontology;
- UI/data-model decision;
- Domain Method Truth;
- Generic-Fit claim;
- historical Finding;
- Development priority;
- implementation admission;
- merge authority.

Development and Research implications must still pass their proper owners and gates.

---

## 16. Coverage / omission check

### Considered material

Histo-Orla:

- `AGENTS.md`;
- `PROJECT_STATE.md`;
- `README.md`;
- #28 + `problem-baseline.md`;
- `intent-bestandsaufnahme-2026-09-24.md`;
- #42 Requirements baseline/extensions;
- capability map;
- requirements delivery coverage;
- #45 Research Protocol;
- #48 Technical Lead state including PR #149 T1/V1 handoff;
- #63 value/decision/delivery/feedback assurance;
- current #150 semantic-preservation run evidence;
- selected real Research Case artifacts as observable Information-Space examples.

Wissensarbeit:

- #53 issue body as historical candidate state;
- comment `5831348317` as provenance-corrected owner-primary systemic synthesis input;
- comment `5833820505` as owner-confirmed conceptual baseline and correction.

### Explicitly not performed

- no external scholarly literature review of Information-Space / epistemic-space concepts;
- no complete re-audit of every historical Histo issue/PR;
- no new architecture or technology research;
- no Requirement acceptance review;
- no generic Skill validation across projects.

### Leading-bias controls

- current Requirements were treated as system representation, not as an oracle for Human meaning;
- the 2026-09-24 AI synthesis was not treated as final solely because it was already persisted;
- older Generic-Gap semantics were retained as historical candidate evidence but not used to override later Human correction;
- earlier `visual Derived View` narrowing was not retained as current intent;
- unresolved representation questions were not filled for narrative completeness.

---

## 17. Current reading rule for subsequent work

Until superseded by later Human evidence or a properly accepted project delta, subsequent Histo-Orla analysis should use the following reading discipline:

1. reconstruct relevant Human Intent / correction evidence where material;
2. identify what must be understood/judged relative to that Intent;
3. preserve current epistemic limits rather than rename every open state as a Gap;
4. use Goal/Pain/Need/Constraint/Requirement/Capability/Behavior/Result as distinct perspectives/functions of the same relational Wirknetz;
5. evaluate system output by both semantic relation correctness and material intent-relative coverage;
6. never infer Human Erkenntnis/acceptance solely from artifact or test existence;
7. keep scientific safeguards in the motor room and make their relevant effect inspectable rather than asking the Human to operate them manually;
8. keep Information-Space representation late-bound until evidence supports a more specific form;
9. route any Requirement/Method/Architecture/Development consequence to its existing authority rather than promoting it from this artifact.

---

## 18. Current disposition

`RECONCILED READING BASIS / PERSISTED ON #154 BRANCH / REVIEW + INTEGRATION PENDING`

The material Human-meaning difference identified in the 2026-09-24 → 2026-09-25 chronology is now explicit and restartable.

The next legitimate step is review/integration of this reading view. Only after that should larger Research/Development work be derived against it.