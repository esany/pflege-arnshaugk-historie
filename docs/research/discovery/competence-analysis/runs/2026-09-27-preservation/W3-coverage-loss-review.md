# W3 — Coverage & Loss Auditor

**Run ID:** `competence-analysis-preservation-2026-09-27-v1`  
**Work Owner:** #150  
**Execution PR:** #152  
**Worker:** W3  
**Status:** `REVISE / S2 representation defects / return to W2`  
**Review date:** 2026-09-29  
**Review mode:** fresh semantic coverage/loss review; no W2 author rationale used; no expected verdict supplied.

## 1. Bound input set and independence

This W3 review used only the canonical W3 semantic inputs named by the frozen packet:

| Input | Path / binding |
|---|---|
| Source of Meaning | `docs/research/discovery/competence-analysis/inputs/owner-confirmed-analysis-2026-09-27.md` |
| Frozen Source Lock blob | `85d3b7cd38dd14c8f23af8350b4c585828934018` |
| W1 inventory | `docs/research/discovery/competence-analysis/runs/2026-09-27-preservation/W1-inventory.md` |
| W1 blob | `289fc4d9859f87ad2e56519b8dd586419eb068d7` |
| W2 draft | `docs/research/discovery/competence-analysis/analysis-baseline-2026-09-27.md` |
| W2 blob | `1f0c6109345b45272f5d5488bd00976a365b4f5c` |
| Assurance Contract / Coverage Oracles | `docs/research/discovery/competence-analysis/planning/assurance-contract-2026-09-27.md` |
| Assurance blob | `b752ce10a6497163941a88cdce08359bd53bbe0e` |
| W3 packet | `docs/research/discovery/competence-analysis/planning/work-packets/W3-coverage-loss-review.md` |
| W3 packet blob | `f5b76b8b66701cc38a46c6a1655c954aba9ac9e3` |
| Exact pre-W3 execution head | `4e0f7d3d4237d3ad78e32bc0f68dd8cbb9e618a2` |

Forbidden override inputs were not used as semantic inputs. This review does not perform scientific-truth, Domain-SOTA, Method-Truth, Requirement or Architecture review.

## 2. Verdict

`REVISE`

The W2 draft preserves almost all enumerated W1 material, but it does **not** satisfy the frozen W3 PASS condition.

Two bounded S2 representation defects remain:

1. **INV-078 is only PARTIAL.** The P6a section preserves diplomatic scope and the warning against inferring authenticity/function from edition text, but it drops the source-backed interface relation that Diplomatics may require archival provenance/material inspection and may constrain, without itself deciding, downstream domain interpretation.
2. **Profile-depth/Open coverage is not reconstructable profile-by-profile.** §3 reproduces the 26 generic coverage questions and §5 contains compact profile summaries, but the frozen Operational-Competence/Profile Oracles require each profile to carry its source-supported operational dimensions **or explicitly mark unsupported dimensions `OPEN / NOT YET ESTABLISHED`**. The current per-profile `OPEN` lines do not cover all omitted OC dimensions, and the generic §3 question list does not say which dimensions are intentionally open for which profile. This is a QC-05 material representation defect, not a request to add SOTA knowledge.

No S3 authority, provenance or promotion defect was found. The defects are deterministic and source-bounded, so the correct transition is `REVISE → W2`, not STOP.

## 3. Row-by-row W1 coverage/loss matrix

Classification is against the actual W2 representation, allowing distributed representation only where the source meaning remains fully reconstructable.

| INV_ID | W2 location | Coverage | Severity | Correction |
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
| INV-078 | §5 P6a (diplomatic scope/status present; source-backed archival/material/domain-interface relation absent) | PARTIAL | S2 | Add the INV-078 interface meaning to P6a: archival provenance/material inspection may be required; diplomatic status may constrain but does not itself decide downstream domain interpretation. |
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

## 4. Coverage-Oracle findings beyond the INV row check

| Finding | Oracle/QC | Verdict | Severity | Evidence in W2 | Required correction |
|---|---|---|---|---|---|
| O-01 — per-profile OC state is not explicit | E2 Operational-Competence Meta-Oracle; E3 Profile-Level Oracle; QC-05 | FAIL | S2 | §3 lists OC-01…26 generically; §5 profile blocks do not state, for each profile, which source-supported OC dimensions are represented and which are `OPEN / NOT YET ESTABLISHED`. | In §5, add a compact per-profile OC coverage/status block for P1–P15/P6a/P6b. Populate only from Source Lock/W1; where those inputs do not support a profile-specific value, write `OPEN / NOT YET ESTABLISHED`. Do not import SOTA/model knowledge. |
| O-02 — source-backed P6a interface relation lost | E4 Interface Oracle; QC-02; QC-06; INV-078 | FAIL | S2 | §5 P6a has no archival/material-inspection or downstream-domain-control relation. Generic §6 cannot reconstruct this P6a-specific relation. | Add the INV-078 relation to §5 P6a, preserving the no-master-authority boundary. |
| O-03 — activation model | E5 Activation Oracle; QC-07 | PASS | — | §4 and §7 preserve non-pipeline, material/question/claim/evidence dependence, initial-vs-claim-driven depth and the “not every charter immediately” rule. | — |
| O-04 — open-state/non-promotion | QC-04; QC-08; OS-03…OS-08 | PASS | — | Status header, §§8–10 preserve analysis/scoping, unresolved states, SOTA/profile/validation debt and downstream owner gates. | — |
| O-05 — P6 reversibility | QC-18 | PASS | — | §5 keeps P6a/P6b distinct and `retain | split | merge | reframe` open; neither 15 nor 16 is ontologized. | — |
| O-06 — negative evidence/dependency | QC-15 | PASS | — | P1/P7/P12/P13/P14 preserve Detectability/Search Boundary, `not found ≠ absent`, and independence/triangulation limits. | — |
| O-07 — no master-domain | QC-16 | PASS | — | §4, P14 and P15 explicitly deny epistemic superauthority. | — |
| O-08 — case vs general | QC-17 | PASS | — | §8 retains case-derived activation/stress role and prohibits historical-finding promotion. | — |

## 5. QC verdicts required by W3

| QC | Verdict | Severity / reason |
|---|---|---|
| QC-01 Semantic Fidelity | PASS | No material meaning shift detected in represented content. |
| QC-02 Material Completeness | FAIL | S2: INV-078 is partial; generic OC list does not make per-profile omitted/open state reconstructable. |
| QC-03 No Flattening | PASS | Core source/representation/instance, evidence/inference, P6a/P6b and layer distinctions remain distinguishable. |
| QC-04 Epistemic Status Fidelity | PASS | No Method Truth, historical finding, Requirement or Architecture promotion. |
| QC-05 Profile Depth | FAIL | S2: profile-specific operational dimensions are neither fully represented nor explicitly OPEN profile-by-profile. |
| QC-06 Interface Integrity | FAIL | S2: INV-078 P6a-specific interface meaning is absent; generic §6 is insufficient for that relation. |
| QC-07 Activation Fidelity | PASS | No fixed pipeline; initial and claim-driven activation remain distinct. |
| QC-08 Uncertainty / Open-State Preservation | PASS | `candidate/competing/unresolved` and SOTA/profile/validation debt remain open. |
| QC-15 Evidence Dependency / Negative-Evidence Discipline | PASS | Dependency, Search Boundary and Detectability conditions remain visible. |
| QC-16 No Master-Domain / Authority Smearing | PASS | Routing/integration have no evidence/truth superauthority. |
| QC-17 Case-vs-General Separation | PASS | Case material remains stress/activation example only. |
| QC-18 Profile-Boundary Reversibility | PASS | P6 split/merge/reframe remains unresolved and reversible. |

## 6. Required adversarial checks

| W3 adversarial check | Result | Evidence |
|---|---|---|
| Lost inference boundary | PASS for enumerated W1 inference-boundary items | W2 retains the explicit hard distinctions for silence/detectability, dependence, edition/original, relation bundles, maps, names, OCR, first mention/material absence, retrieval and triangulation. |
| Unsupported but sensible rule | PASS | No unmarked substantive W2 claim was found that requires external SOTA/model knowledge to stand as competence semantics. Representation-only headings/OPEN labels/mapping and assurance-state framing do not promote domain meaning. |
| `unresolved` → likely answer | PASS | Candidate/competing/unresolved states remain explicit; no forced preferred answer was found. |
| P6 hardening | PASS | P6a/P6b remain analytically distinct but taxonomically unresolved. |
| Interface reduced to generic consultation | FAIL in one source-backed profile relation | INV-078 is not reconstructable from §5 P6a; this is O-02 / QC-06 S2. |

## 7. Exact bounded repair set for W2

`R-01 — Profile OC coverage status`

For every §5 profile block (`P1`–`P15`, with `P6a` and `P6b` separately addressable), add a compact operational-coverage status that accounts for **OC-01…OC-26**. For each dimension:

- use only Source Lock/W1-supported profile meaning when present;
- otherwise write `OPEN / NOT YET ESTABLISHED`;
- do not infer SOTA, thresholds, terminology, automation suitability, validation triggers or handoff detail from model knowledge;
- keep current profile boundaries reversible.

This may be a compact table/reference structure; it need not duplicate prose already present. The result must let a fresh reader tell the difference between “represented here” and “not established by the frozen analysis”.

`R-02 — Restore INV-078 in §5 P6a`

Add a source-bounded interface statement equivalent to:

> Diplomatic assessment may require archival provenance and material inspection. Its status/function findings may constrain downstream subject-domain interpretation, but do not themselves decide that subject-domain claim.

Do not expand this into new archival, material or subject-domain method rules.

`R-03 — Mapping/editorial bookkeeping`

Update §11/§12 only as needed so the added OC status markers and INV-078 repair are traceable as representation work rather than new domain semantics.

No other W2 semantic change is authorized by this W3 return.

## 8. W3 return

```text
verdict: REVISE
matrix_ref: docs/research/discovery/competence-analysis/runs/2026-09-27-preservation/W3-coverage-loss-review.md
coverage: 162 FULL / 1 PARTIAL (INV-078); plus QC-05 profile-depth/Open-state representation defect
QC_verdicts: QC-01 PASS; QC-02 FAIL(S2); QC-03 PASS; QC-04 PASS; QC-05 FAIL(S2); QC-06 FAIL(S2); QC-07 PASS; QC-08 PASS; QC-15 PASS; QC-16 PASS; QC-17 PASS; QC-18 PASS
repair_set: R-01..R-03
source_ambiguity: none detected by W3
unsupported_substantive_additions: none detected
S3_findings: none
next_allowed_transition: W2
automatic_repair_cycle_remaining: one, per W3 packet
```

## 9. Non-conclusions / stop boundary

This W3 result is representation assurance only. It does not establish or change historical findings, disciplinary SOTA, Method Truth, final profile taxonomy, Requirements, Architecture or product/runtime design.

W4 is **not** allowed from this return. The next allowed transition is the bounded W2 repair cycle. If the same material defect recurs after that cycle, or repair would require choosing a new meaning not present in the allowed source inputs, the packet's STOP/Human path applies.
