# Histo-Orla – Current Work Selection Reconciliation 2026-09-10

**Status:** `work-control reconciliation / current-main / no selection authority`  
**Architecture / technical consumers:** #48/#59/#61/#63  
**Research owners:** #46/#47; Method Truth #60  
**Re-Baseline context:** #92 / merged PR #94  
**Inspected main:** `c77bfd377f4cc9f39bed4bdc55cd40195ff463b4`

## 1. Zweck und Authority-Grenze

Dieses Artefakt reconciliiert ausschließlich die Frage, was aus dem aktuellen Repository als **Current Work Selection** abgeleitet werden darf.

Es ist weder Selection Registry noch Selection Authority und entscheidet keine historische Priorität.

```text
Research scope / historical meaning  -> jeweiliger Research Owner (#46/#47)
Method Truth                         -> #60
Requirements                         -> #42
Technical architecture / delivery    -> #48/#59
Current Work Selection               -> explizite Research/Product-Owner-Autorisierung
```

`selected-current` darf insbesondere nicht aus einem gültigen Work Order, offenem oder gemergtem PR, grünem CI, technischer Resumability, aktiver Issue-Ownership oder einer Architecture Roadmap hergeleitet werden.

## 2. Reconciliation gegenüber 2026-09-04

Der alte PR #83 enthielt einen weiterhin richtigen Grundbefund, aber einen inzwischen veralteten konkreten Zustand: PR #76 / Sachenbacher war damals noch als `branch-candidate` beschrieben.

Seitdem ist PR #76 gemergt. Der Merge selbst hält ausdrücklich fest, dass er keine Requirement-, Architecture-, Workflow- oder Method-Promotion erzeugt und die Sachenbacher-Arbeit als begrenzte Reconciliation-/Reference-Evidenz behandelt.

Daraus folgt:

```text
PR #76 merged/integrated
!=
Sachenbacher selected-current
```

Die alte Disposition `branch-candidate` wird daher **nicht** fortgeschrieben.

## 3. Aktuelle Work-Control-Disposition

| Work Object | aktueller Zustand | Selection-Aussage | Disposition für Handoff |
|---|---|---|---|
| #46 / Sachenbacher / gemergter PR #76 | integrierte begrenzte Research-/Reconciliation-Evidenz; offene fachliche Fragen bleiben im zuständigen Research-Kontext | keine explizite aktuelle Auswahl gefunden | `integrated-not-selected` |
| #46 / Lampe 420 / `WO-U2-LAMPE-420-001` | valider/resumable bounded Work Order | keine explizite aktuelle Auswahl gefunden | `resumable-not-selected` |
| #47 Teich-/Wasserlandschaft | aktiver eigenständiger Research Owner | aktiver Owner bedeutet keine globale Auswahl | `active-independent-not-selected` |
| #60 Domain Method Work | aktive cross-cutting Method Truth | Method Work wählt keinen historischen Slice | `supporting` |
| #92 / Re-Baseline | Architecture-/Roadmap-Arbeit; PR #94 gemergt | Architekturfreigabe ist keine Research Selection | `architecture-supporting` |
| Gesamt | mehrere valide/aktive/resumable Arbeitsobjekte | im inspizierten kanonischen State keine explizite `selected-current`-Autorisierung gefunden | `selection-open` |

Die Bezeichnungen in dieser Tabelle sind **lokale Reconciliation-Beschreibungen**, keine neue universelle Lifecycle-Taxonomie.

## 4. Bindende Minimalregel für technische Consumer

Context-/Resume-/Audit-/Roadmap-Mechanismen dürfen Current Work nur dann als `selected-current` darstellen, wenn eine explizite autorisierte Auswahl referenzierbar ist.

Fehlt sie, ist die sichere Ausgabe:

```text
Current Work Selection: selection-open
```

Dabei dürfen separat sichtbare Zustände wie `resumable`, `integrated`, `active owner` und `supporting` erhalten bleiben, ohne Priorität zu behaupten.

## 5. Verhältnis zur Architecture Re-Baseline

Die unter #92 / PR #94 etablierte Re-Baseline ordnet Product Capabilities, Domain/Research, Operational Support, Piloten und Dependencies. Sie darf **keinen** Research Slice durch ihre technische Reihenfolge auswählen.

Insbesondere gilt für R5:

```text
Architecture-ready Vertical Slice candidate
+
explicit Research/Product Owner selection of a real task/source
=
allowed real Research Vertical Slice
```

Ohne den zweiten Teil darf nur technische Enabler-/Capability-Arbeit fortgesetzt werden.

## 6. Handoff-Akzeptanz

Ein frischer Bearbeiter muss aus dem Repo korrekt rekonstruieren können:

- Current Work Selection ist `selection-open`;
- Lampe 420 ist resumable, aber nicht selected-current;
- Sachenbacher/PR #76 ist integriert, aber nicht selected-current;
- #47 ist ein aktiver eigener Research Owner, aber nicht dadurch global ausgewählt;
- #60 ist supporting Method Truth;
- #92/#94 autorisiert Architektur-/Delivery-Reconciliation, nicht historische Research Selection.

Fail ist jede Ableitung von `selected-current` aus Merge-Status, CI, Resumability, Issue-Aktivität oder Roadmap-Reihenfolge.

## 7. Disposition der alten PRs #83/#84

- PR #83 ist durch dieses aktuelle Reconciliation-Artefakt semantisch superseded und soll nicht mehr gemergt werden.
- PR #84 darf nicht unverändert übernommen werden, weil es noch `PR #76 -> branch-candidate` in `PROJECT_STATE.md` schreiben würde.
- `PROJECT_STATE.md` soll in einem separaten, minimalen Handoff-Update **nach Integration dieses Artefakts** auf `selection-open` plus die aktuellen Dispositionen gebracht werden.

Keine Requirement-, Method-, Historical-, Architecture- oder Selection-Promotion durch dieses Dokument.