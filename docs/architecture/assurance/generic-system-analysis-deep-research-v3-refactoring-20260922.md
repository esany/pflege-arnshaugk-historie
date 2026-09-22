# Generic System Analysis + Deep Research v3 — Refactoring Diagnosis

**Date:** 2026-09-22  
**Review context:** #121 / #64  
**Research quality:** #45  
**Status:** method/prompt refactor evidence; no project solution, Requirement, Architecture, Method, Selection or Delivery authority.

## 1. Refactoring diagnosis

| Existing area | Keep | Shorten | Move | Restructure | Remove from Core | Reason |
|---|---:|---:|---:|---:|---:|---|
| Purpose / no-solution boundary | ✓ | ✓ |  | ✓ |  | Essential; previously repeated too often |
| Socio-technical scope | ✓ | ✓ |  | ✓ |  | Core analytical symmetry |
| Evidence classes / uncertainty | ✓ | ✓ |  | ✓ |  | Needed for claim discipline; consolidate once |
| Historical reconstruction | ✓ | ✓ |  | ✓ |  | Needed to distinguish current vs historical state |
| Need / Mental Model / Translation analysis | ✓ | ✓ |  | ✓ |  | Central to project-to-system translation |
| Interface analysis | ✓ | ✓ |  | ✓ |  | Keep as phenomenon class, not fixed checklist |
| Error culture / Near Miss / Recovery | ✓ | ✓ |  | ✓ |  | Prevents blame and one-sided failure narratives |
| Complexity typology | ✓ | ✓ |  |  |  | Small discriminating vocabulary is useful |
| Histo-Orla-shaped central question |  |  |  |  | ✓ | Too leading for generic use |
| Long anti-pattern catalogue |  |  | ✓ |  | ✓ | High anchoring / apparent rediscovery risk |
| Large discipline-by-discipline SOTA list |  |  | ✓ | ✓ | ✓ | Useful discovery aid, poor primary research structure |
| Generic external research challenge | ✓ | ✓ |  | ✓ |  | Must become finding-driven |
| Related systems | ✓ | ✓ |  | ✓ |  | Research support, not tool shopping |
| Best Practice | ✓ | ✓ |  | ✓ |  | Retain only as evidence + conditions + transferability |
| Theory / Method distinction | ✓ |  |  | ✓ |  | Previously under-specified; required for epistemic depth |
| Citation chaining / adversarial search / saturation | ✓ | ✓ |  | ✓ |  | Preserve v2 strength without duplication |
| Minimum source portfolio language |  | ✓ |  | ✓ |  | Replace checklist sourcing with proportional tiers |
| Platform-specific Deep Research instructions |  |  | ✓ |  | ✓ | Vendor-neutral Core; separate Execution Profile |
| Multi-repository protocol |  |  | ✓ | ✓ | ✓ | Optional extension, not main path |
| Detailed output mega-outline |  | ✓ |  | ✓ | ✓ | Encourages checkbox compliance; replace with 10-step flow |
| Research Agenda Gate | ✓ |  |  | **new core** |  | Missing bridge between analysis and research |
| Finding→Research coverage | ✓ |  |  | **new core** |  | Prevents both shallow findings and unanchored literature |
| Current/historical finding status | ✓ |  |  | **new core** |  | Prevents stale audits from becoming current truth |

## 2. Change map v2 → v3

### Preserved
- socio-technical analysis across domain, user/work, requirements/product, technology, organization and epistemic architecture;
- empirical history and current-state reconstruction;
- Need→System / interface analysis;
- professional error culture;
- positive counterexamples;
- alternative explanations and counterevidence;
- uncertainty / unresolved;
- proportional external research quality;
- theory, methods, empirical research, related work and best-practice evidence;
- citation chaining, inspection status, transferability, search boundaries and saturation;
- strict stop before solution development.

### Structurally changed
1. **Analysis now generates research.**  
   The mandatory Research Agenda Gate is the routing layer between project findings and external Deep Research.

2. **Research is finding-driven.**  
   Disciplines are discovered per problem cluster; they no longer define the report's primary structure.

3. **Current state is explicit.**  
   Findings receive current/historical/recovery/unresolved status.

4. **Theory and method are separated.**  
   The prompt asks both what mechanism explains the phenomenon and how the field empirically knows whether it is present.

5. **Depth is proportional.**  
   Tier A/B/C replaces quasi-exhaustive source collection.

6. **Research returns to the finding.**  
   Each central cluster ends as strengthened/weakened/reframed/contradicted/partial/conditional/unresolved.

7. **Two completion failures are explicit.**  
   Unresearched Major Finding and Unanchored Research.

### Removed from the Core
- Histo-Orla-specific causal chains and named diagnoses;
- long anti-pattern catalogue;
- long academic-field catalogue;
- product-specific Deep Research UI/mode instructions;
- multi-repository procedure;
- repeated no-solution statements;
- repeated evidence-quality rules;
- solution archetypes, capability candidates, target architecture, experiments, roadmap, metrics and operating-contract derivation.

## 3. Conscious trade-offs

### Less recall from pre-seeded labels
v3 is less likely to notice a known anti-pattern merely because it was named in the prompt. This is intentional: it improves independence and reduces anchoring. Optional challenge appendices can restore recall **after** inductive analysis.

### More judgement at the Research Agenda Gate
The model must decide which findings are material and which fields can discriminate competing explanations. This is a real reasoning task rather than checklist execution. The coverage matrix and external challenge make this judgement inspectable.

### Less fixed output structure
v3 gives fewer headings. This reduces compliance overhead but makes report form less uniform across projects. Traceability is preserved through the Research Agenda and final Coverage Matrix.

### No guaranteed product execution mode
The vendor-neutral Core specifies research quality, not how a specific product invokes long-horizon research. This improves portability but requires a separate Execution Profile where the environment needs one.

### No artificial exhaustiveness
Tiering and saturation may leave peripheral topics lightly researched. This is intentional: depth follows explanatory importance rather than source-count optics.

## 4. Elements intentionally outside the Core

### Appendix A — Late Challenge / Completeness Checklist
Used only after Phase A to challenge omissions. It must not generate initial findings.

### Appendix B — Disciplinary Discovery Map
A vocabulary/search aid when the Research Agenda cannot identify suitable fields; not a required report outline.

### Appendix C — Multi-Repository Extension
Used only when cross-case comparison is actually in scope.

### Execution Profiles
Platform-specific activation, source connection and runtime metadata live outside the method. The ChatGPT profile is versioned separately.

## 5. Quality-control result

| Question | Result | Reason |
|---|---|---|
| Can it analyse a project unlike Histo-Orla? | **yes** | central question and findings are neutral; named Histo-Orla failure modes removed |
| Can it conclude the project works well? | **yes** | positive mechanisms/counterexamples and no forced failure output |
| Can it find that more formalization is needed? | **yes** | formalization is not pre-classified as harmful |
| Can it falsify an existing diagnosis? | **yes** | prior reports are hypotheses; adversarial research + reconnection allow contradiction |
| Does system analysis generate the Research Agenda? | **yes** | explicit mandatory gate |
| Is every major research block anchored to a finding? | **yes** | finding-driven organization + Unanchored Research check |
| Are theory and investigation method separated? | **yes** | distinct Theory and Method research components |
| Is counter-research required? | **yes** | competing explanations + adversarial research |
| Can unresolved remain? | **yes** | explicit valid result and final section |
| Does it stop before solutions? | **yes** | one hard boundary at start and final STOP |
| Is it shorter / less redundant than v2? | **yes** | compact 10-step core; lists/modules moved out |
| Is Core vendor-neutral? | **yes** | product activation removed |
| Can a competent model execute without checklist domination? | **yes, with residual risk** | main path is causal and finding-driven; matrix/checks are compact and late |

## 6. Residual risks to test empirically

- Research Agenda Gate could still over-cluster complex findings.
- Tier assignment may be too shallow if the model underestimates a cluster's centrality.
- "Relevant fields / terms" can still anchor search prematurely if not revised during research.
- A model may mechanically fill the coverage matrix without genuine saturation.
- Vendor-neutral Core cannot itself ensure that a platform actually allocates enough research runtime.

These are execution/test questions, not reasons to add more Core rules.
