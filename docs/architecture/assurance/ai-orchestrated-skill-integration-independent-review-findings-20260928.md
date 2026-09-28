# Histo-Orla – Independent Review Findings zu PR #149

**Stand:** 2026-09-28  
**Status:** `independent-review-evidence / disposition-complete / no-implementation-authority`  
**Review target:** PR #149, reviewed planning head `81e9b4ff562460e79672a8e9cd7c6f57f0027510`  
**Work Owner:** #48  
**Source role:** fresh independent adversarial review supplied by the Human Owner after execution in a separate normal Chat context  

> Dieses Artefakt erhält die tatsächlichen Findings des unabhängigen Reviews getrennt vom ursprünglichen Review-Auftrag und vom Author-Self-Review. Der Review ist Evidence gegen den Plan, keine selbständige Requirement-, Architecture- oder Implementation-Authority.

## 1. Review boundary

Der Reviewer arbeitete read-only und meldete:

- Histo-Orla `main@00891652761d479cc98d0752ea8d11a2ac61dcc3`;
- Wissensarbeit `main@9b16601c3550bde37ed4410eec3cec3bd6aa6846`;
- Wissensarbeit PR #51 weiterhin `open / unmerged` auf `f3726c962807b311e8a2a7df63f738e11790fbed`;
- keine Repository-Mutation durch den Review.

Der Review erzeugt keine Implementation Admission, Requirement-/Method-Promotion, Research Selection oder Merge-Authority.

## 2. Findings und projektseitige Disposition

### F-01 — zirkuläre lokale Admission-Semantik

**Review severity:** `blocking`  
**Disposition:** `confirm / refine`  

Der alte Plan ließ `locally_reviewed_basis_ref` bis P2 unreviewed, während P2 den Skill bereits real nutzen sollte. Das vermischte upstream Review mit lokaler Execution-Erlaubnis.

Korrektur:

```text
UPSTREAM REVIEWED BASIS
→ LOCALLY TRIAL-ADMITTED BASIS
→ real bounded trial
→ LOCALLY OPERATIONALLY ADMITTED BASIS
```

`trial-admitted` erlaubt exakt einen gebundenen Histo-Pilot; es behauptet weder generische Compatibility noch operative Dauerzulassung. Operational Admission kann erst aus Trial + Review folgen.

### F-02 — ursprünglicher P1 Binding-Core war nicht als Minimum bewiesen

**Review severity:** `major / blocking`  
**Disposition:** `confirm / shrink`  

Der alte Candidate `Contract + JSON Schema + Evaluator + Registry/Binding JSON` wird verworfen/deferred.

Minimalitätsvergleich:

1. Existing Work Context / bounded Work Order kann bereits Owner, Scope, external refs, exact frozen basis, required context/evidence, MAY/MUST NOT, STOP, persistence und delta-only return binden.
2. Fresh upstream state bleibt eine zur Laufzeit neu zu lesende Observation; dafür ist kein lokaler `current upstream`-Store nötig.
3. Positive semantische Compatibility bleibt Judgement/Admission und wird nicht deterministisch aus Ref-Gleichheit erzeugt.
4. Der reference-only Ansatz scheitert nur an der separaten Anforderung, eine lokal zugelassene execution-sufficient Basis auch ohne aktuellen Upstreamzugriff wieder verfügbar zu haben.

Kleinster verbleibender Zusatz ist deshalb **kein generischer Binding-Core**, sondern eine konkrete immutable Availability-Derivation des realen Pilotpakets mit Provenienz.

### F-03 — P0 war logisch verfrüht

**Review severity:** `major / blocking`  
**Disposition:** `confirm / conditionalize; condition now resolved true for the revised pilot`  

P0 ist kein erster Produkt-/Architekturschritt. Es existiert nur, wenn der minimal verbleibende problem-closing Slice legitime neue Dateien braucht.

Nach F-02/F-04 ist diese Bedingung für den realen Pilot erfüllt: die recoverable Availability-Derivation besteht aus neuen immutable Snapshot-Dateien. Der aktuelle Execution Contract kann neue exact paths nicht deklarieren. P0 bleibt daher als **conditional enabling delta**, dessen Bedingung nun evidenzbasiert erfüllt ist.

### F-04 — Durable Identity war als Durable Availability überclaimt

**Review severity:** `major / blocking`  
**Disposition:** `confirm / reframe to recoverable basis`  

Der korrigierte Plan trennt:

```text
identified
→ trackable
→ retrievable now
→ execution-available now
→ recoverable without current upstream
```

Der Problem-Closure-Slice verlangt die letzte Stufe für einen lokal trial-/operational zugelassenen Basisstand. Das folgt aus dem Owner-Problem (funktionierenden lokalen Stand bei Upstream-Evolution nicht verlieren) zusammen mit der vorhandenen #57-Restartability-/Provider-Removal-Richtung.

Keine Vendor-/Mirror-Plattform wird eingeführt. Für den Pilot genügt eine **immutable, execution-sufficient lokale Kopie genau des frozen Skillpakets**, deren Herkunft, exact upstream commit und Blob-Identitäten erhalten bleiben. Diese Kopie ist Availability Derivative, nicht Upstream Truth und nicht automatisch lokal admitted.

### F-05 — Implementation Write Surface nicht hart genug gebunden

**Review severity:** `major / blocking`  
**Disposition:** `confirm / hard precondition`  

Für die spätere technische Mutation gilt vor Admission:

```text
fresh isolated checkout/worktree or equivalent isolated filesystem surface
→ exact admitted basis verification
→ branch-scoped mutation
→ tests in the same checkout
→ exact changed-file scope validation
→ diff review
→ delta-only return
```

Direkte Contents-API-/Connector-Writes sind kein Ersatz für diese Implementation Surface. Kann die Execution Surface dies nicht gewährleisten, lautet das Ergebnis `BLOCKED`.

### F-06 — Identity, Observation, Maturity und lokale Disposition nicht scharf genug getrennt

**Review severity:** `major / blocking`  
**Disposition:** `confirm / split`  

Korrigierte Trennung:

- **tracking identity:** wo der relevante Upstream frisch resolved wird;
- **dated observation evidence:** was zu einem konkreten Zeitpunkt gesehen wurde;
- **local trial basis:** exact Ref/Snapshot, der für genau einen Histo-Pilot zugelassen wurde;
- **local operational basis:** exact Ref/Snapshot, der nach Trial + Review für einen definierten Einsatz zugelassen wurde;
- **current upstream:** niemals aus persistentem `last_observed_*` behauptet, sondern bei consequential Nutzung frisch gelesen.

Deterministisch zulässig sind nur Aussagen wie `unchanged-against-basis`, `delta-detected`, `stale`, `source-unavailable`, `lineage-invalid`, `review-required`. Positive semantische Compatibility/Admission braucht Review-/Authority-Evidence.

### F-07 — #48-owned P2 Pilot ist legitim

**Review severity:** `observation`  
**Disposition:** `keep / refine`  

Der Pilot benötigt keine historische Research Selection. Der spätere Trial untersucht einen #48-owned System-/Assurance-Gegenstand. Der konkrete Task wird im Trial Work Context eingefroren und respektiert den Skill-STOP vor Solution Development.

## 3. Revised minimality result

Der Independent Review reduziert die technische Hypothese deutlich:

```text
VERWORFEN/DEFERRED
- generische External-Skill Registry
- generisches Binding Schema
- Compatibility Evaluator
- persistierter pseudo-current Upstream State

BEIBEHALTEN
- bestehender Work Context / bounded Work Order für Authority, refs, fresh resolution, STOP
- conditional P0 nur für exact create targets
- konkrete immutable Availability-Derivation des realen Pilotpakets
- realer bounded Trial
- fresh-context / source-unavailable / upstream-delta Falsifikation
```

## 4. Exact pilot source basis

Wissensarbeit frozen reviewed head:

`f3726c962807b311e8a2a7df63f738e11790fbed`

Execution-sufficient runtime files:

| Source path | Git blob SHA |
|---|---|
| `skills/system-analysis-deep-research/skill.md` | `845f5cfa9d224384f7d81c79fd7829b8d26cbf06` |
| `skills/system-analysis-deep-research/references/core-method.md` | `4a1aa371e0a7da30e7f98834cee58aa03ccc4821` |
| `skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md` | `77fa8cfc31fdace2a928f3b936a21687d81de297` |

Upstream review/maturity remains external prior-art state:

- #43: R2 closed, #46 owner-authorized;
- #46: trials ongoing, generic fit not established;
- PR #51: open/unmerged at the exact head above.

No local copy may promote this maturity.

## 5. Remaining gate

All F-01..F-06 findings have a concrete project-side disposition, but the revised plan introduces a materially different **immutable local Availability-Derivation topology** that the independent reviewer did not inspect in this exact form.

Therefore the correct state is:

`PARTIAL / BLOCKING FINDINGS DISPOSITIONED / FRESH CLOSURE REVIEW REQUIRED / NO IMPLEMENTATION AUTHORITY`

A short fresh-context closure review must challenge only the revised delta, especially:

- whether the local snapshot is genuinely the smallest recoverability mechanism;
- whether it avoids a second Skill Truth / vendoring drift;
- whether P0 is now legitimately necessary;
- whether exact snapshot topology and execution-surface guards are sufficient;
- whether any cheaper existing mechanism closes recoverable availability equally well.

No scarce external executor is needed for that review.