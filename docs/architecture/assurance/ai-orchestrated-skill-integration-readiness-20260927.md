# Histo-Orla – AI-orchestrierte externe Capability-Integration: Pilot Readiness

**Stand:** 2026-09-28  
**Status:** `OWNER-ADMITTED BOUNDED TECHNICAL PILOT / IMPLEMENTATION PENDING / NO OPERATIONAL ADMISSION`  
**Work Owner:** #48  
**Development / Verification:** #59  
**Work Context / Handoff:** #61  
**Requirements:** #42 unchanged  
**Restartability:** #57  
**Traceability:** #63  
**Histo planning basis:** PR #149  
**Pilot upstream:** `esany/Wissensarbeit` PR #51 @ `f3726c962807b311e8a2a7df63f738e11790fbed`

> Dieser Stand autorisiert den ausdrücklich vom Human Owner gebundenen technischen Pilot. Er erzeugt keine Requirement-/Method-/Architecture-Promotion, keine fachliche Research Selection, kein Generic Fit, keine Operational Admission und keinen Merge.

---

## 1. Outcome Anchor

Der Workstream soll nicht eine Skill-Registry oder Preservation-Plattform bauen. Er soll erstmals den folgenden technischen Capability-Pfad real nachweisen:

```text
external capability exists
→ fresh Histo context can identify exact relevant basis
→ Histo binds task / authority / STOP
→ AI can use the capability without Human Owner relaying skill/prompt/context
→ result returns under Histo authority
→ state remains restartable
→ upstream delta / unavailability remain explicit
```

Der Pilot ist erst aussagekräftig, wenn diese Kette tatsächlich ausgeführt und falsifiziert werden kann.

---

## 2. Owner problem

Histo-Orla braucht technische Grundstrukturen, durch die die KI externe/evolvierende Capabilities selbständig, aktuell, authority-sauber, restartbar und ressourceneffizient nutzen und orchestrieren kann.

Der Human Owner soll nicht zum Router für:

- Skills;
- Versionen;
- Chats;
- Prompts;
- Work Context;
- Ausführungsmodi;
- Folge-Reviews

werden.

Das Systembild ist das übergeordnete Warum. Dieser Workstream bleibt **foundational technical enablement**.

---

## 3. Final reconciliation of review evidence

### Broad independent review

Beibehalten:

- `upstream reviewed` ≠ `local trial admitted` ≠ `local operationally admitted`;
- fresh upstream resolution statt pseudo-current persistent state;
- kein generischer Binding-/Registry-/Compatibility-Core;
- isolated filesystem/Git implementation surface;
- realer bounded Trial;
- no-cascade Authority.

### Closure review

Der Closure Review des revidierten Plans bestätigte die konkrete Availability-Derivative-Richtung und fand einen einzigen blocking Planungsfehler:

> Die generische E0/P0-Create-Target-Erweiterung ist nicht notwendig.

Disposition:

- **E0/P0 entfernt**;
- keine Änderung von `execution_order.py`, Work-Order-Schema oder bounded-execution Contract;
- exact new-file creation wird ausschließlich im konkreten Pilot über Owner Authority / Work Context + isolierte Git-Surface gebunden;
- vorhandene Git-Blob-Revalidation wird später für die lokalen Runtime-Dateien wiederverwendet;
- Availability wird auf recoverable Skill/source-package basis begrenzt;
- die drei Dateien werden aus exact reviewed-package fidelity erhalten.

Kanonische Evidence:

- `ai-orchestrated-skill-integration-independent-review-findings-20260928.md`
- `ai-orchestrated-skill-integration-closure-review-findings-20260928.md`
- `ai-orchestrated-capability-planning-process-learning-20260928.md`

---

## 4. Unsicherheit / `unresolved`

Verbindliche Owner-Korrektur für diesen Workstream:

> Unsicherheit soll transparent gemacht und zugelassen werden. Sie darf nicht mit Interpretation gefüllt werden, nur damit eine Lösung oder ein vollständiger Plan präsentiert werden kann.

Daher gilt:

```text
unknown / uncertainty
→ source and scope visible
→ competing interpretations preserved where relevant
→ unresolved allowed
→ claim / action scope limited accordingly
→ further resolution only through evidence or explicit authority
```

Ein offener Punkt ist nur dann Pre-Implementation-Blocker, wenn sein Offenlassen den nächsten Versuch unaussagekräftig macht oder einen nicht akzeptablen irreversiblen/Authority-/Rights-/Security-/State-Loss-Schaden erzeugen kann.

Andere offene Fragen werden sichtbar in den Pilot getragen.

---

## 5. Exact upstream basis

Fresh revalidation am 2026-09-28:

- Wissensarbeit #43: `R2-closed / #46-owner-authorized`;
- #46: frozen trial head, Trials laufend, Generic Fit nicht etabliert;
- PR #51: `open / unmerged`, exact head `f3726c962807b311e8a2a7df63f738e11790fbed`.

Exact reviewed runtime package:

| Source file | Git blob SHA |
|---|---|
| `skills/system-analysis-deep-research/skill.md` | `845f5cfa9d224384f7d81c79fd7829b8d26cbf06` |
| `skills/system-analysis-deep-research/references/core-method.md` | `4a1aa371e0a7da30e7f98834cee58aa03ccc4821` |
| `skills/system-analysis-deep-research/references/execution-profiles/chatgpt-deep-research.md` | `77fa8cfc31fdace2a928f3b936a21687d81de297` |

Diese Maturity ist externe Evidence. Sie erzeugt keine Histo-Orla-Authority.

---

## 6. Smallest admitted technical increment

Es gibt nur noch einen technischen Implementierungsschritt vor dem Trial:

### E1 — exact local Availability Derivative

Erzeuge genau einen commit-scoped lokalen, provenance-erhaltenden Snapshot des frozen reviewed Runtime-Pakets:

```text
docs/development/external-capability-snapshots/
  wissensarbeit-system-analysis-deep-research/
    f3726c962807b311e8a2a7df63f738e11790fbed/
      PROVENANCE.json
      skill.md
      references/core-method.md
      references/execution-profiles/chatgpt-deep-research.md
```

Eigenschaften:

- drei Runtime-Dateien byte-identisch zum frozen Upstream;
- exact source commit + per-file blob IDs im Provenance Record;
- `authority_effect = none`;
- `semantic_compatibility_effect = none`;
- local derivative ist weder `current upstream` noch zweite Skill Truth;
- fresh upstream resolution bleibt bei consequential use Pflicht;
- lokale Modification des Snapshots ist nicht erlaubt; Änderung wäre neue Derivation mit eigener Lineage.

### Was ausdrücklich **nicht** gebaut wird

- keine External-Skill Registry;
- kein Binding Schema;
- kein Compatibility Evaluator;
- kein persistent `latest/current compatible` state;
- kein Workflow-/Agenten-Framework;
- kein generischer Create-Target-Mechanismus;
- kein neues Immutability-System.

---

## 7. Safe implementation surface

E1 darf nur auf einer isolierten filesystem/Git-Surface ausgeführt werden:

```text
fresh isolated checkout/worktree or proven equivalent
→ verify exact admitted planning basis
→ create exact four absent paths only
→ fail if any target already exists
→ verify exact upstream commit/status/blob identities
→ copy bytes without normalization/editing
→ verify local blobs
→ exact changed-file-set check
→ same-checkout relevant tests / Project Assurance where available
→ diff review
→ STOP and return delta
```

Nicht zulässig:

- direct write to `main`;
- Contents-/Connector-Writes als Ersatz für diese isolierte Implementation Surface;
- hidden scope expansion;
- Änderung bestehender operational Contracts als Voraussetzung;
- Merge.

Wenn die Surface oder exact Basis nicht hergestellt werden kann: `BLOCKED` und STOP.

---

## 8. Trial authority already bound by Owner GO

Der Human Owner hat am 2026-09-28 ein einzelnes explizites GO erteilt, das die bounded Pilotlinie bindet.

Nach erfolgreichem E1 + Delta Review darf ohne weiteren Owner-Routing-Schritt fortgesetzt werden mit:

```text
LOCAL TRIAL ADMISSION
→ T1 real bounded Skill use
→ V1 restart / upstream-delta / source-unavailable / owner-burden falsification
→ keep | adapt | reject | unresolved
```

Keine Folgeauthority entsteht für:

- Operational Admission;
- Generic Fit;
- Requirement-/Method-/Architecture Promotion;
- fachliche Research Selection;
- Merge;
- weiteren Implementation Scope.

---

## 9. T1 – end-to-end technical capability trial

T1 ist ein #48-owned technischer Pilot, kein historischer Research Case.

Der frische Kontext muss aus Repo-State:

1. die Capability und ihren exact local basis finden;
2. aktuellen Upstream fresh revalidieren;
3. Histo Trial Authority / Scope / STOP rekonstruieren;
4. den Skill + mandatory Core selbst laden;
5. den Skill an einem bounded technischen Systemanalyseobjekt ausführen;
6. den Skill-eigenen STOP vor Solution Development einhalten;
7. Ergebnis / Limitations / `unresolved` nachvollziehbar zurückgeben;
8. keinen manuellen Skill-/Prompt-/Kontexttransport durch den Owner benötigen.

Trial-Erfolg ≠ Operational Admission.

---

## 10. V1 – falsification

Nach T1 mindestens prüfen:

- fresh context kann Basis, Authority, Currentness und STOP aus Repo-State rekonstruieren;
- lokale Runtime-Dateien werden gegen gebundene Git-Blob-Bases revalidiert;
- upstream head/status delta wird sichtbar, nie auto-upgraded;
- source unavailable verhindert nicht das Laden des erhaltenen exact package, aber Current-Upstream-State bleibt `unavailable/unresolved`;
- Snapshot behauptet keine Currentness;
- Skill STOP funktioniert;
- offene Unsicherheiten bleiben offen, statt zur scheinbaren Vollständigkeit interpretiert zu werden;
- Human Owner musste den Workflow nicht zwischen Chats/Skills/Versionen manuell routen.

Ergebnis:

`keep | adapt | reject | unresolved`.

---

## 11. Readiness / admission verdict

**Final planning verdict:**

`READY / OWNER-ADMITTED BOUNDED TECHNICAL PILOT / IMPLEMENTATION PENDING`

Begründung:

- Broad Independent Review abgeschlossen;
- Closure Review abgeschlossen und dispositioniert;
- einziger blocking Closure-Fund E0 wurde subtraktiv entfernt;
- verbleibende Closure-Findings sind non-blocking Refinements und eingearbeitet;
- kein neuer materieller irreversibler/Authority-/Safety-Risikotyp wurde durch diese Subtraktion erzeugt;
- exact Implementierungsscope und Safety Surface sind bekannt;
- Unknowns dürfen transparent `unresolved` bleiben;
- weitere Review-Kaskade ist nicht gerechtfertigt.

Nächste Aktion: genau den gebundenen E1-Implementation-Slice einmal auf isolierter Git-/Filesystem-Surface ausführen und danach den bereits autorisierten technischen Trial fortsetzen.
