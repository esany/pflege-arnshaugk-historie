# Histo-Orla – AI-orchestrierte externe Capability: T1/V1 Pilot Evidence

**Stand:** 2026-09-29  
**Status:** `T1 COMPLETE / V1 PARTIAL / DISPOSITION ADAPT / NO OPERATIONAL ADMISSION / NO GENERIC FIT / NO MERGE`  
**Technical Work Owner:** #48  
**Development / Verification:** #59  
**Parent / Authority:** PR #149, Human-Owner-GO vom 2026-09-28  
**Admitted planning basis:** `5a5151b650cc9285f54cbda46b4ec7ce02272c8a`  
**E1 implementation evidence:** PR #153 @ `4beb1af8694282c0943b54234fe703bfe0789924`  

> Dieses Artefakt ist bounded Pilot-/Falsification-Evidence. Es erzeugt keine Requirement-, Method-, Architecture-, Generic-Fit-, Operational-Admission-, Research-Selection- oder Merge-Authority.

---

## 1. Zweck

T1/V1 prüft nicht, ob Histo-Orla bereits eine generische Skill-Plattform besitzt. Geprüft wird der im PR #149 gebundene minimale technische Capability-Pfad:

```text
external capability exists
→ Histo kann exact Basis aus Repo-State identifizieren
→ Currentness / Authority / STOP werden getrennt rekonstruiert
→ AI lädt und nutzt die Capability ohne manuellen Skill-/Prompt-Relay des Owners
→ Ergebnis bleibt unter Histo-Authority
→ Restart-/Delta-/Unavailability-Grenzen werden falsifiziert
→ STOP vor Operational Admission / Generic Fit / Solution Development
```

---

## 2. Fresh basis

### Histo-Orla

- aktuelles `main` frisch beobachtet: `8dd82427019d4faeb476a10191345a128abc0607`;
- `main` ist seit dem admitted PR-#149-Basisstand durch den unabhängigen Merge von PR #151 weitergelaufen;
- für diesen Pilot bleibt die explizit owner-admitted Planning-Basis `5a5151b650cc9285f54cbda46b4ec7ce02272c8a` maßgeblich;
- E1 liegt als Draft PR #153 genau einen Commit darüber: `4beb1af8694282c0943b54234fe703bfe0789924`;
- E1-Diff: genau vier neue Snapshot-Dateien, keine bestehende Datei verändert;
- GitHub Project Assurance auf dem exakten E1-Commit: Run `36491256776` / #453 → `success`.

### Fresh Upstream

`esany/Wissensarbeit`:

- #43: `R2-closed / #46-owner-authorized`;
- #46: owner-authorized, frozen trial baseline, Trials laufend, Generic Fit nicht etabliert;
- PR #51: `open / unmerged`, Head unverändert `f3726c962807b311e8a2a7df63f738e11790fbed`.

### Histo-local capability basis

Local Snapshot in PR #153:

```text
docs/development/external-capability-snapshots/
  wissensarbeit-system-analysis-deep-research/
    f3726c962807b311e8a2a7df63f738e11790fbed/
```

Revalidierte Runtime-Blobs:

- `skill.md` → `845f5cfa9d224384f7d81c79fd7829b8d26cbf06`
- `references/core-method.md` → `4a1aa371e0a7da30e7f98834cee58aa03ccc4821`
- `references/execution-profiles/chatgpt-deep-research.md` → `77fa8cfc31fdace2a928f3b936a21687d81de297`

`PROVENANCE.json` hält u. a. fest:

- `artifact_role = immutable-availability-derivative`;
- `fresh_upstream_resolution_required = true`;
- `authority_effect = none`;
- `semantic_compatibility_effect = none`;
- local edit requires a new explicit derivative.

---

## 3. T1 Work Context

**PRIMARY FUNCTION**  
Architecture / Development / Research Software Engineering system analysis under #48.

**CURRENT TASK**  
T1 bounded technical capability-use trial from PR #149.

**INVESTIGATION OBJECT**  
The current Histo-Orla mechanism for consuming one externally developed AI capability through PR #149 / PR #153, including identity, availability derivative, authority/currentness separation, capability loading, owner-routing burden and restartability boundaries.

**SCOPE**

Included:

- PR #149 authority / planning / trial contract;
- PR #153 exact E1 delta;
- current #48 operational context;
- current upstream #43/#46/PR #51 state;
- local preserved Skill package;
- capability use and bounded external research;
- restart / delta / source-unavailable falsification questions.

Excluded:

- historical/domain research;
- target architecture;
- implementation planning;
- generic capability registry/platform design;
- Generic Fit;
- Operational Admission;
- Requirement-/Method-Promotion;
- merge.

**METHOD / QUALITY FRAME**  
Histo-local `system-analysis-deep-research` snapshot from E1, including mandatory `core-method.md`; prior audits/process learning are treated as prior interpretation, not current truth.

**MAY**  
Reconstruct, analyse, identify findings/protective mechanisms, form competing explanations, derive a Research Agenda, conduct bounded external research, reconnect evidence, preserve `unresolved`.

**MUST NOT**  
Select architecture/tools, propose roadmap/implementation, promote requirements/method, infer Owner acceptance, claim Generic Fit/Operational Admission, merge.

**STOP**  
Before solution development.

---

## 4. Capability Admission

Available in the executing normal Chat:

- fresh GitHub repository inspection;
- exact PR/commit/file/blob inspection;
- current web research with source citations;
- enough source inspection for the bounded standards/practice questions below;
- canonical persistence to the Histo planning branch.

Material limitations:

- this is **not an independently fresh ChatGPT conversation**; the model can deliberately reconstruct from repository state, but prior conversational exposure cannot be proven absent;
- isolated shell GitHub/DNS access is unavailable in this Chat;
- no real upstream outage occurred during T1;
- no real upstream-head/status delta occurred during T1;
- Deep Research product mode was not required: the generated Research Agenda remained bounded Tier-B standards/practice research and ordinary multi-source web research was adequate. No Tier-A completion claim is made.

---

## 5. Current-state / evidence reconstruction before prior interpretation

Directly observed current evidence:

1. PR #149 binds one exact pilot basis, one local trial authority and explicit STOP boundaries.
2. PR #153 contains exactly the four admitted E1 files and no modification to existing Histo files.
3. All three local runtime files have exactly the expected frozen upstream Git blob IDs.
4. Full Project Assurance passed on the exact persisted E1 commit.
5. The executor-local same-surface full Project Assurance did not run; that execution fact remains explicit.
6. Current upstream PR #51 remains open/unmerged at the frozen reviewed head; #46 remains ongoing; Generic Fit remains unestablished.
7. In this T1 execution, the AI located and loaded `skill.md`, mandatory Core and the ChatGPT execution profile from the Histo repository state. The Owner did not paste or relay those capability files.
8. `main` has advanced independently through PR #151; the admitted pilot basis remains explicit and distinguishable from current main.

Prior interpretation consulted only after this reconstruction:

- `ai-orchestrated-capability-planning-process-learning-20260928.md`;
- the broad independent review and closure-review evidence.

Their diagnoses were not treated as current facts merely because they were previously recorded.

---

## 6. Material findings and competing explanations

### T1-F01 – Repo-self-loading of the external capability works for this bounded case

**Observed:** the executing AI identified PR #149, the exact E1 commit, local snapshot path and all three required runtime files from repository state, then loaded them without Owner relay of Skill text, version or prompt.

**Status:** `current / positive mechanism / partial fresh-context proof`.

**Competing explanation:** success may be helped by conversational prior exposure even though the execution was freshly reconstructed from repo state. A genuinely independent context has not yet been observed.

**Uncertainty:** independent-fresh-context reproducibility remains unresolved.

### T1-F02 – Exact blob identity establishes package-byte fidelity, not generalized trust or currentness

**Observed:** local runtime Git blob IDs equal the frozen upstream IDs exactly.

**Status:** `current / strengthened with external evidence`.

**Competing explanation:** a matching Git object identity could be overread as supply-chain trust, compatibility or approval.

**Boundary:** exact identity does not establish trusted producer/builder, semantic compatibility, current upstream state or host admission.

### T1-F03 – Authority and Currentness remain explicitly separated from preservation

**Observed:** `PROVENANCE.json` grants no authority or compatibility and requires fresh upstream resolution; PR #149 separately binds only local trial authority.

**Status:** `current / protective mechanism / strengthened`.

**Counter-risk:** AI-owned orchestration could otherwise be misread as AI-owned authority.

### T1-F04 – Owner-relay burden is reduced at capability-use time, but not fully eliminated across the whole pilot

**Observed:** T1 required no manual Skill/prompt/version relay. However the preceding E1 executor was a separate isolated environment, and the Human Owner did relay its compact execution report into this Chat even though the Draft PR existed.

**Status:** `mixed / partial`.

**Competing explanations:**

- the residual relay is a product/tool-capability limitation rather than an integration-architecture defect;
- future direct repo-state continuation may eliminate that burden without new platform structure;
- one successful T1 cannot establish general owner-burden reduction.

### T1-F05 – The current delivery path is now a genuinely small empirical increment

**Observed:** E1 is one commit, exactly four new files, with automated CI feedback; T1 then exercises the preserved package rather than extending generic infrastructure.

**Status:** `current / positive mechanism / externally supported with limited transferability`.

**Boundary:** software-delivery evidence does not replace scholarly/Research-Integrity gates.

### T1-F06 – Restartability is demonstrated only to the current branch/commit boundary

**Observed:** the capability can be loaded from exact Histo commit `4beb1af...` without rereading upstream package bytes.

**Status:** `partial / unresolved beyond current ref availability`.

**Unresolved:** no real upstream outage occurred; the E1 snapshot is in an unmerged Draft PR, so durable availability after branch/ref removal or long-term repository evolution is not established by this trial.

### T1-F07 – No evidence from this first consumer requires a generic capability registry/evaluator

**Observed:** one bounded consumer could discover identity, exact basis, authority and currentness through existing repo/PR/Work-Context conventions plus the explicit snapshot.

**Status:** `current bounded case / positive for minimality`.

**Unresolved:** discoverability and maintenance with multiple independent capabilities has not been tested. Absence of current need is not proof that no future generalization will be useful.

### T1-F08 – Verification currently spans two execution surfaces

**Observed:** local mutation surface could not run full Project Assurance; GitHub CI ran the full suite successfully on the exact persisted commit.

**Status:** `current execution limitation / non-blocking for this read-only T1 after explicit delta review`.

**Uncertainty retained:** same-surface full-assurance behavior was not observed and is not claimed.

---

## 7. Finding-derived Research Agenda

### RQ-01 — What do content-addressed identity and software provenance actually establish?

**Anchor:** T1-F02.  
**Need:** avoid conflating exact byte identity with provenance trust, currentness or compatibility.  
**Depth:** Tier B.  
**Counterevidence target:** standards showing that digest equality alone is insufficient for stronger provenance/authenticity claims.

### RQ-02 — Is the explicit Scope / third-party / human-oversight separation consistent with current AI assurance guidance?

**Anchor:** T1-F03/T1-F04.  
**Need:** challenge whether AI-owned orchestration with retained Owner authority is a defensible control boundary rather than merely a local convention.  
**Depth:** Tier B.  
**Counterevidence target:** guidance requiring materially different oversight/third-party controls for this class of use.

### RQ-03 — Does the shift from repeated planning/review handoffs to a small executable increment align with evidence on software feedback loops?

**Anchor:** T1-F05.  
**Need:** challenge the earlier assumption that more pre-execution review necessarily lowers overall delivery risk.  
**Depth:** Tier B / contextual.  
**Counterevidence target:** evidence that small-batch/fast-feedback findings are inapplicable or unsafe in governed technical environments.

### Search Boundary

Searched 2026-09-29, English-language primary/authoritative sources, bounded to:

- Git official documentation;
- SLSA current specification v1.2;
- NIST AI RMF / AIRC;
- DORA capability/research guidance.

No claim of exhaustive academic literature coverage is made. The external research is standards/practice-oriented and limited to the three finding-derived questions above.

---

## 8. External research and analytical reconnection

### RQ-01 — Git identity / provenance

Sources:

- Git object model: https://git-scm.com/docs/git
- Git hash transition / security boundary: https://git-scm.com/docs/hash-function-transition
- SLSA v1.2 Provenance: https://slsa.dev/spec/v1.2/provenance
- SLSA v1.2 Verifying artifacts: https://slsa.dev/spec/v1.2/verifying-artifacts

External evidence:

- Git is a content-addressable filesystem; object names identify content and support integrity checking.
- Git's own current documentation also warns that SHA-1 is not a complete modern cryptographic trust story; hardened Git SHA-1 remains useful for object identity/integrity while Git is transitioning toward SHA-256.
- SLSA defines provenance as verifiable information about where/when/how an artifact came from.
- SLSA explicitly separates existence of provenance from verification: stronger authenticity claims require checking provenance against expectations/roots of trust and, where applicable, signatures/subject digests.

**Reconnection to T1-F02:** `strengthened + reframed`.

The exact three Git blob IDs are strong evidence that Histo preserved the reviewed runtime bytes. They do **not** by themselves establish trusted producer identity, semantic compatibility, currentness or Operational Admission. The current Histo provenance claims are appropriately narrower than SLSA-style supply-chain attestation.

### RQ-02 — AI scope / oversight / third-party capability use

Sources:

- NIST AI RMF Core: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- NIST AI RMF / Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

External evidence:

- NIST calls for targeted application scope based on capability/context;
- human oversight processes should be defined and documented;
- risks and controls for third-party software/AI components should be identified and documented;
- GAI contexts may require differing human-AI configurations rather than one universal oversight model.

**Reconnection to T1-F03/F04:** `strengthened / conditional`.

The Histo split `AI initiative/orchestration` vs. `Owner material authority` is compatible with current risk-management principles. External guidance does not imply that the Owner must manually route every Skill/version/context. It also does not justify removing Owner/host authority boundaries. The appropriate amount of oversight remains context/risk-dependent.

### RQ-03 — small batches / feedback vs. review accumulation

Sources:

- DORA Working in small batches: https://dora.dev/capabilities/working-in-small-batches/
- DORA Continuous delivery: https://dora.dev/capabilities/continuous-delivery/
- DORA Continuous integration: https://dora.dev/capabilities/continuous-integration/

External evidence:

- DORA describes small batches as enabling faster feedback and hypothesis testing;
- handoffs create fixed costs and large batches delay feedback;
- automated testing and CI provide fast feedback and reduce the cost of identifying regressions;
- continuous delivery is explicitly framed as reducing risk through testing, automation and observability rather than by accumulating large pre-release batches.

**Counterboundary:** DORA studies software delivery, not historical scholarship or Research-Integrity promotion. These findings cannot justify weakening scientific evidence/method/authority gates.

**Reconnection to T1-F05:** `strengthened with limited transferability`.

For the technical enablement slice, moving from repeated pre-implementation review cycles to one small E1 + real T1 feedback loop is externally consistent with software-delivery evidence. This says nothing about relaxing consequential scholarly validation.

---

## 9. T1 result

`VALID BOUNDED T1 / REPO-SELF-LOADING PASS / INDEPENDENT-FRESH-CONTEXT PROOF UNRESOLVED / STOP OBSERVED`

What was actually demonstrated:

- exact Histo-local capability basis discovered from repo state;
- fresh upstream state independently resolved;
- local vs. upstream vs. authority states kept distinct;
- Skill + mandatory Core + environment profile loaded from the Histo snapshot without Owner file/prompt relay;
- bounded system analysis executed;
- findings generated before external research;
- external research remained finding-derived;
- counterevidence/transfer boundaries retained;
- uncertainty remained visible;
- execution stopped before architecture/solution/implementation work.

Not demonstrated:

- truly independent fresh-chat execution with zero prior conversational exposure;
- real upstream outage;
- real upstream head/status delta;
- long-term availability after branch/ref removal;
- multi-capability scaling;
- Operational Admission or Generic Fit.

---

## 10. V1 falsification matrix

| V1 check | Result | Evidence / limit |
|---|---|---|
| 1. fresh context reconstructs basis / lineage / authority / STOP from repo only | `PARTIAL` | repo sufficiency demonstrated by fresh reconstruction; independently fresh chat not available in this execution |
| 2. local runtime files revalidate against bound Git blobs | `PASS` | all three local blob SHAs equal frozen upstream expected IDs |
| 3. upstream head/status delta becomes visible and never auto-upgrades | `PARTIAL / NOT TRIGGERED` | fresh upstream resolution performed; current head/status unchanged, so live delta path not exercised |
| 4. upstream unavailable still permits local package load; currentness remains unavailable/unresolved | `PARTIAL / NOT TRIGGERED` | local package loaded without needing upstream bytes after discovery; no real upstream outage occurred |
| 5. snapshot does not claim currentness or compatibility | `PASS` | `fresh_upstream_resolution_required=true`; `semantic_compatibility_effect=none` |
| 6. Skill STOP prevents solution development | `PASS` | T1 terminates here before architecture/solution/roadmap/implementation |
| 7. trial success does not produce Operational Admission | `PASS` | no such promotion made or authorized |
| 8. open questions remain explicit rather than interpretation-filled | `PASS` | fresh-context, outage, delta, durability and scale remain explicit |
| 9. Human Owner did not route Skill/context/version among workers | `PARTIAL` | T1 itself required no Skill/prompt/version relay; earlier isolated E1 report was manually relayed into Chat |
| 10. increment yields a real new technical capability rather than only a stored artifact | `PASS` | Histo-local preserved Skill was actually loaded and used for bounded analysis/research |

---

## 11. Pilot disposition

**Disposition:** `ADAPT`

Meaning for this evidence state only:

- the minimal pattern is empirically useful enough to keep testing;
- E1 is more than dead storage because T1 loaded and executed the preserved capability;
- no evidence from this case requires restoring the rejected generic Registry/Compatibility/E0 infrastructure;
- the pilot has not yet falsified independent fresh-context restart, actual upstream-delta handling, actual upstream outage, long-term ref durability or multi-capability scaling;
- these remain explicit bounded unknowns, not inferred successes and not automatic blockers for recording the value already demonstrated.

`ADAPT` is not an implementation authorization. It is the bounded result of this T1/V1 evidence.

---

## 12. Final STOP

STOP before:

- target architecture;
- generic Skill/Capability platform design;
- new registry/evaluator/schema;
- implementation roadmap;
- Operational Admission;
- Generic Fit;
- merge;
- Requirement-/Method-/Architecture promotion;
- fachliche Research Selection.

Any downstream action requires its own applicable existing authority/gate. Open uncertainty remains visible as `partial`, `not triggered` or `unresolved` rather than being filled by interpretation.
