# W3 — Coverage & Loss Auditor — fresh re-review after bounded W2 repair

**Run ID:** `competence-analysis-preservation-2026-09-27-v1`  
**Work Owner:** #150  
**Execution PR:** #152  
**Worker:** W3  
**Status:** `STOP / repeated S2 profile-depth status defect after the single allowed W2 repair cycle`  
**Review date:** 2026-09-29  
**Review mode:** fresh semantic coverage/loss re-review; no W2 author rationale used; no expected verdict supplied.

## 1. Bound input set and independence

This re-review used only the canonical W3 semantic inputs named by the frozen packet plus the repository-persisted first-W3 return/repair state explicitly allowed for this re-review:

| Input | Path / binding |
|---|---|
| Source of Meaning | `docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md` |
| Frozen Source Lock blob | `85d3b7cd38dd14c8f23af8350b4c585828934018` |
| W1 inventory | `docs/research/discovery/competence-analysis/runs/2026-09-27-preservation/W1-inventory.md` |
| W1 blob | `289fc4d9859f87ad2e56519b8dd586419eb068d7` |
| Repaired W2 draft | `docs/research/discovery/competence-analysis/analysis-baseline-2026-09-27.md` |
| Repaired W2 blob | `b686ffdccb5997a4690777e1a53a004956850809` |
| Assurance Contract / Coverage Oracles | `docs/research/discovery/competence-analysis/planning/assurance-contract-2026-09-27.md` |
| Assurance blob | `b752ce10a6497163941a88cdce08359bd53bbe0e` |
| W3 packet | `docs/research/discovery/competence-analysis/planning/work-packets/W3-coverage-loss-review.md` |
| W3 packet blob | `f5b76b8b66701cc38a46c6a1655c954aba9ac9e3` |
| Persisted first-W3 return / bound repair state | `docs/research/discovery/competence-analysis/runs/2026-09-27-preservation/W3-coverage-loss-review.md` |
| First-W3 evidence blob | `66b6615ad3733ec729783cf345876f6f71dd4204` |
| Exact pre-re-review execution head | `3fff3cc5b0dca605e609d295fd3dd8477c4e793a` |

The first-W3 artifact was used only to bind the prior defects, `R-01…R-03`, the consumed repair-cycle state and the repeated-failure transition. It was not used to replace fresh source/draft comparison.

Forbidden override inputs were not used as semantic inputs: no W2 author rationale, no expected `PASS`, and PR #147/#148 were not used as sources of competence meaning. This re-review does not perform scientific-truth, Domain-SOTA, Method-Truth, Requirement or Architecture review.

## 2. Verdict

`STOP`

The bounded W2 repair closes the prior `INV-078` interface loss and remains file-scope bounded, but the material profile-depth/Open-state defect recurs inside `R-01` itself.

`R-01` correctly creates a 26-dimension partition for every profile row, but its own declared semantics are not faithful to Source Lock/W1: it defines `OPEN / NOT YET ESTABLISHED` as meaning that the frozen analysis carries **no profile-specific answer** for that OC dimension, while multiple rows mark `OC-01 — Problem-/Claimtypen` as `OPEN` although Source Lock/W1 explicitly carry profile-specific problem/scope statements.

Clear examples include:

- **P1:** `OC-01` is marked `OPEN`, while W1 `INV-049` explicitly says P1 evaluates formation, function, perspective, selection, transmission and assertion potential/limits.
- **P3:** `OC-01` is marked `OPEN`, while `INV-059` explicitly says P3 treats scholarship itself historically.
- **P6a:** `OC-01` is marked `OPEN`, while `INV-074` explicitly enumerates the diplomatic problem/scope set (genesis, form, function, issuer/recipient, chancery/formula, dating, authentication, witnesses, transmission status).
- **P6b:** `OC-01` is marked `OPEN`, while `INV-079` explicitly enumerates witness, edition basis, variants, apparatus, editorial supplements, regest and identification.
- **P7:** `OC-01` is marked `OPEN`, while `INV-084` explicitly enumerates provenance, registry/fonds formation, order/rearrangement, appraisal/destruction/loss, repertories and signature history.

These are not requests for SOTA completion. They are already-present Source-Lock/W1 profile semantics. Therefore the new `OPEN` assertions are unsupported representation/status claims and the repaired package still fails the same material class identified by the first W3 finding `O-01 / QC-05`: profile-specific `REPRESENTED` versus genuinely `OPEN` state is not faithfully encoded.

The single automatic W2 repair cycle is already consumed. Under the frozen W3 packet, recurrence of the same material failure is `STOP`, not a second `REVISE` cycle. W4 is not admitted.

No S3 authority/provenance/promotion defect was detected.

## 3. Repair-set verification

| Repair | Re-review | Severity | Finding |
|---|---|---|---|
| `R-01` — profile OC coverage status | **FAIL / repeated material defect** | S2 | Structurally complete 26/26 partition, but false `OPEN` dispositions contradict existing Source Lock/W1 profile semantics; repeated `QC-05` defect. |
| `R-02` — restore `INV-078` | **PASS** | — | P6a now preserves archival-provenance/material-inspection dependency and the bounded downstream-domain constraint without granting diplomatic master authority. |
| `R-03` — mapping/editorial bookkeeping | **PASS** | — | Repair commit confines bookkeeping to mapping/editorial return framing; no new domain-method rule detected. |

Git delta check from first-W3 evidence head `34c55304d4b67fd8f2d792d3dfe137ad238e9f17` to repaired head `3fff3cc5b0dca605e609d295fd3dd8477c4e793a`: exactly one Git file changed, `docs/research/discovery/competence-analysis/analysis-baseline-2026-09-27.md` (`+44/-8`). No unrelated file loss was introduced.

## 4. Row-by-row W1 coverage/loss matrix

The repaired prose retains all 163 W1 inventory items, including the repaired `INV-078`. The STOP finding arises from contradictory/unsupported R-01 coverage-status assertions beyond mere row presence; the packet requires both full coverage **and** no unsupported additions/status drift.

| INV_ID | Re-review location | Coverage | Severity | Correction |
|---|---|---|---|---|
| INV-001 | §§1, 8–10 | FULL | — | — |
| INV-002 | §§1, 8–10 | FULL | — | — |
| INV-003 | §§1, 8–10 | FULL | — | — |
| INV-004 | §§1, 8–10 | FULL | — | — |
| INV-005 | §§1, 8–10 | FULL | — | — |
| INV-006 | §§1, 8–10 | FULL | — | — |
| INV-007 | §§1, 8–10 | FULL | — | — |
| INV-008 | §§1, 8–10 | FULL | — | — |
| INV-009 | §2 | FULL | — | — |
| INV-010 | §2 | FULL | — | — |
| INV-011 | §2 | FULL | — | — |
| INV-012 | §2 | FULL | — | — |
| INV-013 | §2 | FULL | — | — |
| INV-014 | §2 | FULL | — | — |
| INV-015 | §2 | FULL | — | — |
| INV-016 | §2 | FULL | — | — |
| INV-017 | §2 | FULL | — | — |
| INV-018 | §3 | FULL | — | — |
| INV-019 | §3 | FULL | — | — |
| INV-020 | §3 | FULL | — | — |
| INV-021 | §3 | FULL | — | — |
| INV-022 | §3 | FULL | — | — |
| INV-023 | §3 | FULL | — | — |
| INV-024 | §3 | FULL | — | — |
| INV-025 | §3 | FULL | — | — |
| INV-026 | §3 | FULL | — | — |
| INV-027 | §3 | FULL | — | — |
| INV-028 | §3 | FULL | — | — |
| INV-029 | §3 | FULL | — | — |
| INV-030 | §3 | FULL | — | — |
| INV-031 | §3 | FULL | — | — |
| INV-032 | §3 | FULL | — | — |
| INV-033 | §3 | FULL | — | — |
| INV-034 | §3 | FULL | — | — |
| INV-035 | §3 | FULL | — | — |
| INV-036 | §3 | FULL | — | — |
| INV-037 | §3 | FULL | — | — |
| INV-038 | §3 | FULL | — | — |
| INV-039 | §3 | FULL | — | — |
| INV-040 | §3 | FULL | — | — |
| INV-041 | §3 | FULL | — | — |
| INV-042 | §3 | FULL | — | — |
| INV-043 | §3 | FULL | — | — |
| INV-044 | §4 | FULL | — | — |
| INV-045 | §4 | FULL | — | — |
| INV-046 | §4 | FULL | — | — |
| INV-047 | §4 | FULL | — | — |
| INV-048 | §4 | FULL | — | — |
| INV-049 | §5 P1 | FULL | — | — |
| INV-050 | §5 P1 | FULL | — | — |
| INV-051 | §5 P1 | FULL | — | — |
| INV-052 | §5 P1 | FULL | — | — |
| INV-053 | §5 P1 | FULL | — | — |
| INV-054 | §5 P2 | FULL | — | — |
| INV-055 | §5 P2 | FULL | — | — |
| INV-056 | §5 P2 | FULL | — | — |
| INV-057 | §5 P2 | FULL | — | — |
| INV-058 | §5 P2 | FULL | — | — |
| INV-059 | §5 P3 | FULL | — | — |
| INV-060 | §5 P3 | FULL | — | — |
| INV-061 | §5 P3 | FULL | — | — |
| INV-062 | §5 P3 | FULL | — | — |
| INV-063 | §5 P3 | FULL | — | — |
| INV-064 | §5 P4 | FULL | — | — |
| INV-065 | §5 P4 | FULL | — | — |
| INV-066 | §5 P4 | FULL | — | — |
| INV-067 | §5 P4 | FULL | — | — |
| INV-068 | §5 P4 | FULL | — | — |
| INV-069 | §5 P5 | FULL | — | — |
| INV-070 | §5 P5 | FULL | — | — |
| INV-071 | §5 P5 | FULL | — | — |
| INV-072 | §5 P5 | FULL | — | — |
| INV-073 | §5 P5 | FULL | — | — |
| INV-074 | §5 P6a | FULL | — | — |
| INV-075 | §5 P6a | FULL | — | — |
| INV-076 | §5 P6a | FULL | — | — |
| INV-077 | §5 P6a | FULL | — | — |
| INV-078 | §5 P6a | FULL | — | — |
| INV-079 | §5 P6b | FULL | — | — |
| INV-080 | §5 P6b | FULL | — | — |
| INV-081 | §5 P6b | FULL | — | — |
| INV-082 | §5 P6b | FULL | — | — |
| INV-083 | §5 P6b | FULL | — | — |
| INV-084 | §5 P7 | FULL | — | — |
| INV-085 | §5 P7 | FULL | — | — |
| INV-086 | §5 P7 | FULL | — | — |
| INV-087 | §5 P7 | FULL | — | — |
| INV-088 | §5 P7 | FULL | — | — |
| INV-089 | §5 P8 | FULL | — | — |
| INV-090 | §5 P8 | FULL | — | — |
| INV-091 | §5 P8 | FULL | — | — |
| INV-092 | §5 P8 | FULL | — | — |
| INV-093 | §5 P8 | FULL | — | — |
| INV-094 | §5 P9 | FULL | — | — |
| INV-095 | §5 P9 | FULL | — | — |
| INV-096 | §5 P9 | FULL | — | — |
| INV-097 | §5 P9 | FULL | — | — |
| INV-098 | §5 P9 | FULL | — | — |
| INV-099 | §5 P10 | FULL | — | — |
| INV-100 | §5 P10 | FULL | — | — |
| INV-101 | §5 P10 | FULL | — | — |
| INV-102 | §5 P10 | FULL | — | — |
| INV-103 | §5 P10 | FULL | — | — |
| INV-104 | §5 P11 | FULL | — | — |
| INV-105 | §5 P11 | FULL | — | — |
| INV-106 | §5 P11 | FULL | — | — |
| INV-107 | §5 P11 | FULL | — | — |
| INV-108 | §5 P11 | FULL | — | — |
| INV-109 | §5 P12 | FULL | — | — |
| INV-110 | §5 P12 | FULL | — | — |
| INV-111 | §5 P12 | FULL | — | — |
| INV-112 | §5 P12 | FULL | — | — |
| INV-113 | §5 P12 | FULL | — | — |
| INV-114 | §5 P13 | FULL | — | — |
| INV-115 | §5 P13 | FULL | — | — |
| INV-116 | §5 P13 | FULL | — | — |
| INV-117 | §5 P13 | FULL | — | — |
| INV-118 | §5 P13 | FULL | — | — |
| INV-119 | §5 P14 | FULL | — | — |
| INV-120 | §5 P14 | FULL | — | — |
| INV-121 | §5 P14 | FULL | — | — |
| INV-122 | §5 P14 | FULL | — | — |
| INV-123 | §5 P14 | FULL | — | — |
| INV-124 | §5 P15 | FULL | — | — |
| INV-125 | §5 P15 | FULL | — | — |
| INV-126 | §5 P15 | FULL | — | — |
| INV-127 | §5 P15 | FULL | — | — |
| INV-128 | §5 P15 | FULL | — | — |
| INV-129 | §5 Offene P6-Grenze | FULL | — | — |
| INV-130 | §5 Offene P6-Grenze | FULL | — | — |
| INV-131 | §5 Offene P6-Grenze | FULL | — | — |
| INV-132 | §6 | FULL | — | — |
| INV-133 | §6 | FULL | — | — |
| INV-134 | §6 | FULL | — | — |
| INV-135 | §6 | FULL | — | — |
| INV-136 | §6 | FULL | — | — |
| INV-137 | §6 | FULL | — | — |
| INV-138 | §6 | FULL | — | — |
| INV-139 | §6 | FULL | — | — |
| INV-140 | §6 | FULL | — | — |
| INV-141 | §6 | FULL | — | — |
| INV-142 | §7 | FULL | — | — |
| INV-143 | §7 | FULL | — | — |
| INV-144 | §7 | FULL | — | — |
| INV-145 | §7 | FULL | — | — |
| INV-146 | §7 | FULL | — | — |
| INV-147 | §7 | FULL | — | — |
| INV-148 | §7 | FULL | — | — |
| INV-149 | §7 | FULL | — | — |
| INV-150 | §7 | FULL | — | — |
| INV-151 | §7 | FULL | — | — |
| INV-152 | §7 | FULL | — | — |
| INV-153 | §7 | FULL | — | — |
| INV-154 | §8 | FULL | — | — |
| INV-155 | §8 | FULL | — | — |
| INV-156 | §8 | FULL | — | — |
| INV-157 | §8 | FULL | — | — |
| INV-158 | §8 | FULL | — | — |
| INV-159 | §8 | FULL | — | — |
| INV-160 | §§8–10 | FULL | — | — |
| INV-161 | §§8–10 | FULL | — | — |
| INV-162 | §§8–10 | FULL | — | — |
| INV-163 | §§8–10 | FULL | — | — |

Row-presence result: `163 FULL / 0 PARTIAL / 0 MISSING`. This alone is insufficient for W3 PASS because R-01 adds materially wrong per-profile coverage-status assertions.

## 5. Coverage-Oracle findings beyond the INV row check

| Finding | Oracle/QC | Verdict | Severity | Evidence in repaired W2 | Consequence |
|---|---|---|---|---|---|
| O-01R — R-01 per-profile OC state remains semantically wrong | E2 Operational-Competence Meta-Oracle; E3 Profile-Level Oracle; QC-01; QC-02; QC-05 | FAIL | S2 / repeated | R-01 defines `OPEN` as “no profile-specific answer” but marks source-supported `OC-01` OPEN for multiple profiles, including P1/INV-049, P3/INV-059, P6a/INV-074, P6b/INV-079, P7/INV-084. | Same material profile-depth/Open-state failure recurs after the only repair cycle → STOP-REPEATED-FAILURE. |
| O-02R — INV-078 P6a interface relation | E4 Interface Oracle; QC-02; QC-06 | PASS | — | §5 P6a now carries archival/material-inspection dependency plus bounded downstream-domain constraint. | Prior O-02 closed. |
| O-03R — activation model | E5 Activation Oracle; QC-07 | PASS | — | §4/§7 remain non-pipeline and retain initial-vs-claim-driven depth. | — |
| O-04R — open-state/non-promotion | QC-04; QC-08; OS-03…OS-08 | PASS | — | SOTA/profile/validation debt and downstream owner gates remain open. | — |
| O-05R — P6 reversibility | QC-18 | PASS | — | `retain | split | merge | reframe` remains open; no 15/16 ontology. | — |
| O-06R — negative evidence/dependency | QC-15 | PASS | — | Detectability/Search Boundary and independence limits remain visible. | — |
| O-07R — no master-domain | QC-16 | PASS | — | Routing/integration retain no evidence/truth superauthority. | — |
| O-08R — case vs general | QC-17 | PASS | — | Case material remains activation/stress example only. | — |

## 6. QC verdicts required by W3

| QC | Verdict | Severity / reason |
|---|---|---|
| QC-01 Semantic Fidelity | **FAIL** | S2: R-01 states that Source Lock/W1 have no profile-specific answer where they demonstrably do. |
| QC-02 Material Completeness | **FAIL** | S2: the profile-level Oracle is materially mis-dispositioned even though all 163 W1 rows remain present in prose. |
| QC-03 No Flattening | PASS | Core source/representation/instance, evidence/inference and P6a/P6b distinctions remain distinguishable. |
| QC-04 Epistemic Status Fidelity | PASS | No Method Truth, historical finding, Requirement or Architecture promotion detected. |
| QC-05 Profile Depth | **FAIL — repeated** | S2: R-01 does not faithfully distinguish source-supported profile dimensions from genuinely `OPEN` dimensions. This is the same material failure class as first-W3 O-01. |
| QC-06 Interface Integrity | PASS | R-02 restores the previously lost P6a interface relation. |
| QC-07 Activation Fidelity | PASS | No fixed pipeline; initial and claim-driven activation remain distinct. |
| QC-08 Uncertainty / Open-State Preservation | PASS | Genuine candidate/competing/unresolved and SOTA/profile/validation debt remain open; the R-01 false-OPEN problem is accounted under QC-01/QC-05. |
| QC-15 Evidence Dependency / Negative-Evidence Discipline | PASS | Dependency, Search Boundary and Detectability conditions remain visible. |
| QC-16 No Master-Domain / Authority Smearing | PASS | Routing/integration have no evidence/truth superauthority. |
| QC-17 Case-vs-General Separation | PASS | Case material remains stress/activation example only. |
| QC-18 Profile-Boundary Reversibility | PASS | P6 split/merge/reframe remains unresolved and reversible. |

## 7. Required adversarial checks

| W3 adversarial check | Result | Evidence |
|---|---|---|
| Lost inference boundary | PASS | Existing hard inference boundaries remain intact; R-02 does not widen them. |
| Unsupported but sensible rule / addition | **FAIL at representation-status level** | No new Domain-SOTA/method rule was added, but R-01 adds unsupported negative coverage-status assertions (`OPEN = no profile-specific answer`) where Source Lock/W1 already contain such profile-specific meaning. |
| `unresolved` → likely answer | PASS | No forced preferred substantive answer detected. |
| P6 hardening | PASS | P6a/P6b remain analytically distinct but taxonomically unresolved. |
| Interface reduced to generic consultation | PASS | R-02 restores the P6a-specific bounded interface relation; generic §6 is no longer the sole carrier. |

## 8. W3 return

```text
verdict: STOP
matrix_ref: docs/research/discovery/competence-analysis/runs/2026-09-27-preservation/W3-coverage-loss-rereview.md
coverage: 163 FULL / 0 PARTIAL / 0 MISSING at W1-row-presence level; R-01 contains repeated S2 profile-depth/status misrepresentation
QC_verdicts: QC-01 FAIL(S2); QC-02 FAIL(S2); QC-03 PASS; QC-04 PASS; QC-05 FAIL(S2, repeated); QC-06 PASS; QC-07 PASS; QC-08 PASS; QC-15 PASS; QC-16 PASS; QC-17 PASS; QC-18 PASS
repair_set: none — single automatic W2 repair cycle already consumed
source_ambiguity: none detected by this re-review
unsupported_substantive_additions: R-01 false-OPEN coverage-status assertions; no new Domain-SOTA/method rule detected
S3_findings: none
next_allowed_transition: Human / Work Owner under frozen STOP contract
W4_allowed: no
automatic_repair_cycle_remaining: 0
```

## 9. Non-conclusions / frozen stop boundary

This re-review is representation assurance only. It does not establish or change historical findings, disciplinary SOTA, Method Truth, final profile taxonomy, Requirements, Architecture or product/runtime design.

The first W3's `INV-078`/interface defect is closed by R-02. The remaining failure is the repeated material R-01 profile-depth/Open-state representation defect. Because the single automatic repair cycle has been consumed, this W3 worker does not issue a second patch set and does not alter W2. The frozen packet requires STOP/Human at this point.

W4 is **not admitted** from this return.
