# Histo-Orla – Domain Method Profile Contract

**Status:** `working-contract / method-research v0.1`  
**Work Owner:** #60  
**Governing Research Protocol:** #45  
**Vision/Competence Inputs:** #16, #19, #22  
**Accepted Requirement Input:** #42 `REQ-EPI-001`  
**Stand:** 2026-08-31

## 1. Zweck

Ein `Domain Method Profile` operationalisiert eine konkrete fachwissenschaftliche Kompetenz für priorisierte Problem- und Quellentypen.

Es ist **keine Rollenbeschreibung** und kein Prompt. Es muss nachweisen, wie die betreffende Fachdomäne nach ihrem State of the Art tatsächlich arbeitet, welche Evidenz sie benötigt, welche Schlüsse zulässig sind und woran fehlerhafte Anwendung erkennbar ist.

Leitfrage:

> Kann ein fachkundiger Dritter anhand dieses Profils nachvollziehen, warum ein bestimmter Befund erhoben, eine bestimmte Quelle gesucht, ein bestimmter Schluss zugelassen oder verweigert und eine bestimmte Unsicherheit offengelassen wurde?

---

## 2. Statusstufen

Ein Profil muss einen expliziten Status besitzen:

- `scoping` – Fachgrenze und SOTA-Suchraum werden erst bestimmt;
- `method-candidate` – plausible, belegte Methodenbausteine vorhanden, noch nicht ausreichend am Live Case geprüft;
- `working-method` – SOTA-belegt und an realen Fällen getestet; für laufende Forschung einsetzbar, aber revidierbar;
- `validated-method` – zusätzlich fachlich adversarial/extern qualifiziert geprüft, soweit Konsequenz/Fachstandard dies verlangt;
- `deprecated` – ersetzt oder fachlich verworfen, mit Nachfolger/Grund.

Nur `working-method` oder höher darf als domänenspezifische operative Methodik in consequential Research gelten.

---

## 3. Pflichtteile eines Profils

### A. Identität / Geltungsbereich

```text
profile_id
status
work_owner
domain
subdiscipline
problem_types
source_or_material_types
period_scope
regional_scope
leading_when
controlling_when
not_responsible_for
interfaces
```

Die Profilgrenze muss fachlich begründet sein. Zu breite Labels wie `Mediävistik` sind zu vermeiden, wenn darunter unterschiedliche Methoden-/Evidenzlogiken fallen.

### B. Fachbegriffe / Gegenstandsmodelle

Dokumentieren:

- historische Quellenterminologie;
- moderne analytische Begriffe;
- regional/institutionell spezielle Terminologie;
- zentrale Entitäten, Rollen, Relationen und Prozesse, die das Fach unterscheidet;
- konkurrierende Modelle;
- zeitliche/räumliche/institutionelle Geltungsgrenzen;
- problematische, anachronistische oder überholte Gleichsetzungen.

Jeder zentrale Begriff muss erkennen lassen, ob er:

`source term | contemporary institutional term | editorial/archive term | modern analytic term | historiographic term | search variant` ist.

### C. Quellen- / Materialmodell

Für jede relevante Evidenzklasse:

```text
source_material_class
historical_function / formation process
what_it_can_observe
what_it_systematically_misses
transmission / preservation risks
source criticism required
negative-evidence conditions
relevant comparanda
```

Beispiele für verschiedene Profile können Urkunden, Kopiare, Rechnungen, Bauphasen, Keramik, Sedimente, Karten, Flurnamen, Nekrologe usw. sein. Sie dürfen nicht auf eine gemeinsame Evidenzlogik reduziert werden.

### D. Methodisches Playbook

Der Kern eines Profils ist ein **ausführbares fachliches Verfahren**, nicht eine Liste von Themen.

Für jeden priorisierten Problem-/Quellentyp mindestens:

```text
trigger / research question
preconditions
inputs
step-by-step procedure
observations to preserve
controls / comparisons
entity/time/space resolution rules
uncertainty handling
scope-expansion triggers
stop rule
outputs
```

Das Playbook muss so konkret sein, dass es an einem echten Fall geprüft werden kann.

### E. Inferenzvertrag

Explizit dokumentieren:

| Evidenz / Beobachtung | Zulässiger Schluss | Nicht zulässiger Schluss ohne Zusatzbeleg | Zusatzbeleg / Kontrolle |
|---|---|---|---|
| … | … | … | … |

Zusätzlich:

- Regeln für Kausalität;
- Regeln für Korrelation/Ko-Präsenz;
- Regeln für Identität/Normalisierung;
- Regeln für Negativbefunde;
- Regeln für zeitliche Projektion;
- Regeln für Vergleich/Analogie;
- typische Overclaims;
- `unresolved` / `not-assessable`-Bedingungen.

### F. Evidence Appetite / Retrieval

Ein Profil muss sagen, **welche Evidenz es braucht und wie sie fachlich gesucht wird**:

```text
question_type
needed evidence classes
historical vocabulary
latin / vernacular variants
archive / registry vocabulary
bibliographic vocabulary
expected archives / fonds / source series
editions / regesta / catalogues / infrastructures
regional expansion logic
international/comparative expansion logic
search boundaries
saturation/stop indicators
```

Das ist keine vollständige Quellenliste, sondern eine fachlich begründete Suchlogik.

### G. SOTA / Methodenevidenz

Keine Methodik allein aus Modellwissen.

Mindestnachweis:

- maßgebliche aktuelle Methodenliteratur / Handbücher / Fachstandards;
- prägende ältere Methoden-/Forschungstraditionen, wenn sie noch Begriffe oder Praxis bestimmen;
- neuere Kritik/Revision/Kontroverse;
- regional relevante Methodentradition, wo nötig;
- konkrete Volltext-/Seiten-/Kapitelbelege bei consequential methodischen Aussagen;
- persistente Identifikatoren/Links entsprechend `source-identity-protocol.md`.

Zu jedem Methodenfinding mindestens:

```text
method_finding
source / exact reference
what_it_supports
scope / limitations
current-status / controversy
profile implication
```

### H. Qualitäts- und Validierungsregeln

Zusätzlich zum gemeinsamen #45-Check:

```text
domain-specific QA
minimum evidence threshold
typical failure modes
preservation / detectability checks
counterexample strategy
adversarial check
external validation trigger
publication-level trigger
```

### I. Transdisziplinäre Schnittstellen

Nicht nur „auch Archäologie relevant“.

Für jede wichtige Schnittstelle:

```text
triggering observation
outbound domain
question handed over
what evidence is requested
what the other domain may confirm/refute/limit
incommensurabilities / terminology mismatch
return contract
```

Die Koordination darf keine der Domänen zur Master-Perspektive machen.

### J. Automation-/AI-Grenze

Jeder methodische Schritt wird nach Möglichkeit klassifiziert:

- `human scholarly judgment`;
- `external specialist validation`;
- `deterministic rule/validator`;
- `specialized algorithm/ML`;
- `LLM heuristic assistance`;
- `external authoritative system`.

Für LLM-Heuristik zusätzlich:

```text
allowed assistance
required source grounding
failure modes
human review point
cannot-promote-without
```

Ein Rollenprompt ist niemals Ersatz für das Profil oder die Methodenquellen.

---

## 4. Quellenerschließung: Pflichtkern vs. Domain Lens

Jedes Profil muss unterscheiden zwischen dem **gemeinsamen Erschließungskern** und seinen eigenen fachlichen Zusatzbeobachtungen.

### Gemeinsamer Pflichtkern

Über #45 + Source Identity:

- Quelle/Instanz/Überlieferungsstatus;
- exakte Fundstelle;
- ausreichend Kontext;
- historischer Wortlaut vs. editorische Intervention;
- explizite Akteure/Rollen/Handlungen/Objekte/Rechte/Pflichten;
- explizite Gründe/Motive;
- Unklarheiten/Alternativen;
- Search-/Inspection Boundary.

### Domain Lens

Das Profile ergänzt nur die Beobachtungen, die seine Fachmethode für spätere Arbeit erhalten muss.

Beispielhafte Form:

```text
notice_if
preserve_span_or_feature
annotation_type
why_methodologically_relevant
not_yet_a_claim
scope_trigger_if
```

Damit wird verhindert, dass jede Quelle durch eine universelle 100-Felder-Matrix gezwungen wird.

---

## 5. Testvertrag an Live Cases

Ein Profil wird an realen Quellen/Befunden geprüft.

Pro Testfall:

```text
test_case_id
source / finding
question
expected domain-relevant observations
known trap / overclaim
profile steps executed
observations captured
observations missed
forbidden inference prevented?
research hook generated?
scope expansion justified?
method friction
result: pass | partial | fail
required profile change
```

Mindestens:

1. **positiver Fall** – relevante fachliche Signale müssen erkannt werden;
2. **Overclaim-/Counterexample-Fall** – Profil muss einen typischen Fehlschluss verhindern.

Optional dritte Klasse:

3. **evidence-starved Fall** – Profil muss korrekt `not-assessable/unresolved` erzeugen statt Plausibilität zu füllen.

---

## 6. Beispiel für die richtige Granularität

Nicht ausreichend:

> `Diplomatik: Prüfe Quelle, Aussteller, Siegel, Formeln.`

Erforderlich ist beispielsweise ein testbares Verfahren dafür, wie bei einer edierten mittelalterlichen Urkunde:

- Überlieferungsstufe und Editionsbasis bestimmt werden;
- Regest, Editionstext, Apparat und spätere Rückvermerke getrennt werden;
- diplomatische Teile/Formeln funktional eingeordnet werden;
- individuelle Narratio von Formularbestand unterschieden wird;
- Datierungs-/Authentizitätsprobleme erkannt und abgestuft werden;
- Zeugen-/Beglaubigungsfunktion nicht überinterpretiert wird;
- Edition/Original/Kopiar-Konstellationen die zulässige Aussage verändern;
- der Befund mit präziser Fundstelle und Methodenbasis persistiert wird.

**Aber auch diese Punkte sind zunächst nur der Profilauftrag.** Der konkrete methodische Inhalt muss durch die fachliche SOTA-Arbeit unter #60 belegt werden.

---

## 7. Promotion

Ein Profil wird nicht durch guten Text promoviert.

### `scoping → method-candidate`

- Scope klar;
- maßgebliche Methodenquellen identifiziert;
- erstes Playbook und Inferenzregeln belegt.

### `method-candidate → working-method`

- SOTA-/Kontroversenlage hinreichend erfasst;
- Quellen-/Methodenbelege fundstellenfähig;
- Live-Case-Tests einschließlich Counterexample bestanden;
- #45 Domain/Evidence/Inference/Terminology/Provenance/Falsification fit bestanden;
- offene Grenzen sichtbar.

### `working-method → validated-method`

Nur falls benötigt:

- unabhängige qualifizierte fachliche Prüfung bzw. domänenübliche Validierung;
- dokumentierte Disposition der Review-Befunde.

---

## 8. Verhältnis zu Requirements und Architektur

Ein Method Profile ist **keine Systemanforderung**.

Es kann zeigen, dass eine bestehende Requirement-Acceptance zu schwach ist oder eine neue Capability benötigt wird. Dann gilt:

```text
method finding / live pain
→ requirement candidate
→ Cross-Use-Case-/SOTA-/Risk-Prüfung
→ gezielte Entscheidung unter #42
→ falls accepted: technische Allocation/Architektur #48ff
```

Beispiel: Wenn mehrere valide Profiles zeigen, dass fachliches Routing zwingend eigene Evidence Appetite, Inferenzregeln und QA benötigt, kann daraus eine Schärfung von `REQ-EPI-001` folgen. Bis zur Promotion bleibt es Candidate.

---

## 9. Handoff-Anforderung

Jedes Profile muss ohne Chatkenntnis erkennen lassen:

- Was ist fachlich belegt?
- Welche Methodentradition trägt es?
- Was ist noch Hypothese/Candidate?
- Welche realen Fälle wurden getestet?
- Wo scheitert die Methode?
- Was ist der nächste diskriminierende Arbeitsauftrag?
- Welche Systemanforderung wird möglicherweise beeinflusst, aber noch nicht verändert?

---

## 10. Leitformel

> **Ein Fachlabel routet Aufmerksamkeit. Ein Domain Method Profile operationalisiert Fachwissenschaft. Erst ein an SOTA und realer Evidenz geprüftes Profile darf consequential Research führen.**
