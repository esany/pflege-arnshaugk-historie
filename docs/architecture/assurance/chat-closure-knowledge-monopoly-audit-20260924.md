# Histo-Orla – Chat Knowledge-Monopoly / Handoff Reconciliation Audit

**Date:** 2026-09-24  
**Scope:** continuation-critical claims from the conversation “Research Rebuild Handoff Integration” and its supplied predecessor context.  
**Work Owner / persistence:** #63 Value-/Decision-/Delivery-/Feedback Traceability, with #42 interface for any future Requirement question; #92/#PROJECT_STATE only for rebuild handoff/re-entry.  
**Status:** `completed / audit-and-reconciliation / no new Requirement, Method, Architecture, Selection or Product authority`

## 1. Audit result

The current repository already contains the governing facts needed to continue without this chat:

- #28 owns the Goal/Need/Pain/Risk/Constraint discovery baseline;
- #41 owns the capability synthesis;
- #42 is the sole owner of accepted Requirement Truth and its accepted extensions;
- acceptance/verification responsibilities are separated in the Requirements Structure and downstream assurance;
- #63 owns the durable Goal/Need/Pain → Requirement → Decision → Delivery → Feedback trace;
- `selection-open` is the current work-selection state;
- Sachenbacher is integrated reference/test evidence, not `selected-current`;
- WP1 and bounded rebuild execution are already integrated/verified within their stated scopes;
- the current workflow concern is owner usefulness, not a license to start a historical case automatically.

The one material handoff ambiguity found in the current state was the wording “exact next executable action” for the Sachenbacher workflow test alongside `selection-open`. This audit reconciles that wording in `PROJECT_STATE.md`: explicit pilot-source/work authorization comes first; only then may the bounded excerpt-centered test run. This does not select Sachenbacher and does not create a new research priority.

## 2. Semantic-network clarification

The conversation’s “Netz” mental model is compatible with the existing repository only if it is read as a many-to-many semantic and traceability network, not as a mandatory linear lifecycle or a new ontology.

The current canonical homes remain:

| Node / relation family | Canonical owner |
|---|---|
| project purpose, discovery Goals/Needs/Pains/Risks/Constraints and open questions | #28 / `docs/research/discovery/problem-baseline.md` |
| capabilities and quality attributes | #41 / `docs/research/synthesis/capability-map.md` |
| accepted Requirements, accepted Constraints, Acceptance/Verification structure | #42 / Requirements artefacts |
| technical derivation, architecture and implementation | #48/#59, traced by #63 |
| real-use feedback and disposition | #63 / trace records and feedback path |
| current work-selection state | explicit Research/Product-Owner authorization, reconciled in `PROJECT_STATE.md` and the selection-reconciliation artefact |

The relation “Goal/Need/Pain → Capability → Requirement → Acceptance” is a frequent derivation path, not the only valid relation. Feedback may confirm, refine, specialize, overlap, contradict, or require re-opening a prior interpretation; a later finding may sharpen an earlier one without superseding it. No relation vocabulary below is promoted here to an ontology, Requirement Truth, or implementation contract:

`refines | specializes | generalizes | overlaps | supersedes | confirms | contradicts | merge-candidate | unresolved`.

## 3. Reconciliation of the examples

- **N-005 → CAP-04 → REQ-SRC-001/002:** intended vertical derivation (Need → Capability → accepted Requirement), not a duplicate.
- **REQ-STATE-001 → REQ-STATE-003:** later specialization/strengthening of restartability with research-ready evidence availability or an explicit blocker; not an automatic replacement.
- **REQ-UX-001 ↔ REQ-UX-003:** partial overlap plus progressive-disclosure refinement; both retain independent acceptance meaning.
- **CAP-08 ↔ REQ-EPI-006:** evidence-layering capability and explicit distinguishable research-state roles are related generalization/specialization; neither silently replaces the other.
- **old module concept → source-/claim-/excerpt-centered work:** corrective reframing/supersession of the static module framing for that workflow idea; the older artifact/history remains provenance and must not be reactivated as current product truth.
- **FB-20260923-004:** the initial “smallest visual derived view” reading was superseded as too narrow by the later owner clarification toward an excerpt-centered, provenance-bound workflow. The current state correctly treats visualization as derived, not as the research product or a second truth store.

These are audit dispositions and trace vocabulary. They are not a new schema or a demand to rewrite accepted Requirements.

## 4. Intent and Erkenntnislücke

The 2026-09-24 intent inventory is the current canonical read-only source for the newest Owner signals:

`docs/research/discovery/intent-bestandsaufnahme-2026-09-24.md`.

It explicitly distinguishes Owner wording, AI-derived interpretation, repository observation and uncertainty. It records that the current formal chain is strong from G/N/P onward but that “Intent” and the “Erkenntnislücke hinter dem Intent” are not yet consistently relationed across the repository.

Disposition:

- **Intent is not confirmed as a first-class canonical node type.**
- **Erkenntnislücke is not promoted to a new Requirement or ontology type.**
- This remains an unresolved modeling/owner-language gap and a candidate for future owner clarification or bounded analytical testing.
- The “network” metaphor is not evidence for graph technology, universal object types, or a product-agent architecture.

## 5. Chat claims not promoted

The conversation also contained useful but non-canonical interpretations: a complete duplicate inventory, a universal relation model, an automatic Sachenbacher next step, and any claim that a chat summary itself validates scientific or technical truth. They are not persisted as facts unless backed by the owner issues and repository artefacts above. The supplied prior-chat preview was treated as untrusted context; the repository and fresh GitHub owner state controlled this audit.

## 6. Handoff completion

A fresh chat must:

1. read `AGENTS.md → PROJECT_STATE.md → README.md`;
2. read #28, #41, #42, #48, #59, #61, #62, #63, #92 and the linked canonical artefacts;
3. preserve `selection-open`; do not infer selection from integration, resumability, CI, active ownership, roadmap order or test-candidate status;
4. obtain/verify explicit pilot-source/work authorization before running the bounded excerpt-centered test; Sachenbacher is not automatic;
5. treat the semantic network as many-to-many and use the reconciliation labels above only as audit vocabulary;
6. keep Intent/Erkenntnislücke unresolved as modeling questions unless an authorized owner decision changes that status;
7. persist any new continuation-critical state in its canonical owner/artefact, with #42 required for accepted Requirement changes.

## 7. Verification boundary

This audit changes only a versioned assurance artefact and the handoff wording in `PROJECT_STATE.md`. It does not alter accepted Requirements, research findings, Method Truth, selection authority, product architecture, WP2–WP5 admission or historical case state.
