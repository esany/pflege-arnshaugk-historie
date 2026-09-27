# Author Self-Review – AI-orchestrierte Skill-Integration

**Stand:** 2026-09-27  
**Status:** `same-session adversarial self-review / not independent / no implementation authority`  
**Review target before this commit:** PR #149 planning artifacts  

> Dieser Review ist bewusst **keine unabhängige Prüfung** und darf den fresh-review Gate nicht erfüllen. Er soll vermeidbare Planungsfehler vor dem teureren unabhängigen Review sichtbar machen.

---

## 1. Ergebnis

Gesamturteil:

**`REVISE / CLARIFY BEFORE INDEPENDENT PASS`**

Die Grundrichtung bleibt plausibel: vorhandener Operational Core, kein Agent-/Workflow-Framework, ein realer frozen upstream Skill als Pilot, fail-closed Maturity/Compatibility und AI-owned Orchestration. Vier Punkte müssen im Review besonders hart geprüft bzw. vor Implementation Admission präzisiert werden.

---

## 2. Findings

### ASR-01 — MAJOR — Future implementation write surface is not strict enough

**Plan element:** Branch/PR + local mutation safety are named, but the execution plan still leaves the exact implementation write adapter as runtime choice.

**Existing evidence:** #70 closure proved that direct GitHub Connector/Contents writes bypass `tools/operational/mutation.py`; `main` remains unprotected under #44 `DD-20260903-001`.

**Risk:** A correctly planned work package could still create a critical state through the wrong write surface.

**Required refinement:**

For code implementation packages P0/P1, admission should require an execution surface with an isolated checkout/worktree or equivalent branch-scoped filesystem/Git diff where:

- exact branch is established before mutation;
- current basis SHA is revalidated;
- local bounded/no-op guards can run where applicable;
- tests execute against the same checkout;
- changes are reviewed as Git diff;
- no direct Contents-API write to `main` is used.

If the available execution surface only exposes direct remote file replacement and cannot provide equivalent bounded diff/recovery, implementation is `BLOCKED`, not silently downgraded.

**Disposition:** `refine`.

---

### ASR-02 — MAJOR — `last_observed_*` must not become a second current-upstream truth

**Plan element:** P1 candidate record includes `last_observed_ref/status/maturity`.

**Risk:** A persisted observation can look like the current upstream state even after it becomes stale. This would contradict the requirement to re-read source repositories freshly when material.

**Required refinement:**

Separate three roles explicitly:

1. **tracking identity** — where to inspect current upstream;
2. **local reviewed/admitted basis** — exact ref and local disposition used by Histo;
3. **observation evidence** — dated evidence of what was observed during a specific check.

`current upstream` is never inferred from a persisted `last_observed` field. Every material use freshly resolves tracking identity. Persist observation only when it is needed as audit evidence of a material reconciliation; label it as historical observation with timestamp/ref.

**Disposition:** `refine`.

---

### ASR-03 — MAJOR — deterministic core must not manufacture semantic compatibility

**Plan element:** P1 names `compatibility_state` and a provider-neutral evaluator.

**Risk:** A clean deterministic API might encourage deriving `compatible` from ref/path/schema equality, although semantic/maturity compatibility is judgement-heavy.

**Required refinement:**

Core may deterministically produce only states such as:

- `unchanged-against-reviewed-basis`;
- `delta-review-required`;
- `source-unavailable`;
- `binding-invalid`;
- `lineage-invalid`;
- `stale/unresolved`.

A positive semantic `compatible/admitted` disposition must point to the applicable Histo review/admission evidence. It is not a SHA-comparison result.

**Disposition:** `refine`.

---

### ASR-04 — MAJOR — P2 real-use task is under-specified

**Plan element:** P2 says a real Histo task must be selected later and explicitly avoids automatic Research Selection.

**Risk:** Full plan could reach code-complete P1 and then discover that real-use acceptance still needs an unplanned Owner research choice, causing an avoidable loop.

**Smaller resolution:** The first real integration-use does not need to select a historical research question. After P1 exists, use the external System-Analysis/Deep-Research Skill on a bounded **#48 technical/system-analysis object**, e.g. the integrated source-binding/orchestration slice itself or another then-current admitted #48 analysis question. This tests actual host integration, STOP/authority behavior and useful system analysis without changing Research Selection.

A later historical/domain consumer remains separate evidence and must not be smuggled into P2.

**Disposition:** `refine`; exact technical pilot object must be frozen in the later Owner Admission/Work Order.

---

### ASR-05 — MODERATE — “available” has more than one durability meaning

**Owner wording:** Skills should be durably linked and available, stay current, and allow local derivation when updates become incompatible.

**Plan interpretation:** Availability is currently interpreted as fresh remote availability by exact ref through an authorised runtime adapter; no local vendored byte-copy is planned.

**Uncertainty:** This does not guarantee offline/provider-independent availability if upstream disappears or access is lost.

**Trade-off:**

- local vendoring/mirroring increases continuity but duplicates Skill bytes and drift responsibility;
- reference/fetch keeps one semantic source and update-awareness but depends on source availability.

**Current recommendation:** keep reference/fresh-fetch as default for the pilot; explicitly test source-unavailable behavior. Only add local byte preservation if real continuity requirements show that exact upstream refs are insufficient.

**Disposition:** `unresolved-nonblocking-for-first-pilot`; independent review should test whether this interpretation still closes the Owner problem.

---

### ASR-06 — MODERATE — Persistent binding can still be too much state

**Counterhypothesis:** A fresh upstream read plus a small local consumer-basis reference inside the existing Work Context may be enough; a standalone binding record/evaluator could become unnecessary operational metadata.

**Why current plan still retains P1 candidate:** The relationship is intended to persist across multiple Histo tasks and must retain exact local basis, upstream owner/maturity, lineage and compatibility review refs without duplicating them into every Work Order.

**Required independent falsification:** Compare:

- no persistent binding;
- reference-only binding;
- P1 record + evaluator.

Choose the smallest option that preserves restartability, maturity and fail-closed update behavior.

**Disposition:** `independent discrimination required`.

---

### ASR-07 — MODERATE — AI-owned orchestration must not depend on heterogeneous subagents

**Plan element:** model-/execution-class routing.

**Risk:** Product/workspace availability changes; requiring subagents could turn the Owner into fallback orchestrator.

**Existing mitigation:** Plan already provides strong-parent + deterministic-tools fallback.

**Refinement:** Acceptance is **AI-owned orchestration**, not „multiple agents exist“. One capable parent performing bounded sequential subwork may PASS if Owner burden, quality and total cost are acceptable.

**Disposition:** `clarify`.

---

### ASR-08 — MINOR — Planning package is intentionally large; workers must not receive it wholesale

**Observation:** Planning artifacts are detailed because they externalize hazards, alternatives and readiness. Passing all artifacts to every cheap worker would defeat context economy.

**Required rule:** Implementation Work Orders compile the smallest sufficient subset by exact references; worker context must not be „all planning docs by default“.

**Disposition:** `confirm existing minimal_context rule / verify in later Work Order`.

---

# 3. Critical additions for later Admission

Before any implementation Work Order is admitted, require:

1. isolated branch/worktree or equivalent safe write environment;
2. no direct-main Contents-API implementation writes;
3. fresh upstream resolution, not persisted-current assumption;
4. deterministic core never declares semantic compatibility without review evidence;
5. P2 technical real-use object frozen before P2 starts;
6. explicit coverage ceiling: remote exact-ref availability ≠ offline durable copy;
7. fresh independent reviewer to falsify whether persistent binding is needed at all.

---

# 4. Readiness impact

This self-review does **not** add a new #44 blocker or Requirement.

It confirms the current status must remain:

**`PARTIAL / INDEPENDENT REVIEW REQUIRED / NO IMPLEMENTATION AUTHORITY`**

The fresh reviewer should receive the original Readiness/Execution artifacts per the independent-review work order. This self-review may be consulted **after** the reviewer has formed its independent findings, to avoid anchoring.

---

# 5. Non-authority

No code, Work Order admission, upstream import, Research Selection, Requirement change, Architecture acceptance or merge is authorized by this self-review.
