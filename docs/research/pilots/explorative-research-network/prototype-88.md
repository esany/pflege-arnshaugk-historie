# Prototype #88 – minimaler Ranis-Test des vorhandenen Research State

**Status:** `prototype-complete / candidate / branch-isolated / no-main-authority`  
**Work Owner:** #88  
**Pilot Owner:** #86  
**Review Gate:** #87 → `reframe`  
**Owner-Entscheidung:** 2026-09-07 → Variante A: kleinen realen Ranis-Test durchführen  
**Branch:** `pilot/explorative-research-network-20260907`  
**Testdatum:** 2026-09-07

## 1. Zweck und Grenze

Dieser Prototyp testet **nicht** ein neues `Research Module`-Modell. Er prüft die nach #87 verbleibende engere Frage:

> Reichen die vorhandenen Histo-Orla-Mechanismen aus, um dieselbe reale Evidenz unter zwei wechselnden Forschungsfragen/Work Contexts provenance-sicher wiederzuverwenden, einen begründeten Scale Shift zu erzeugen und daraus unterschiedliche Views abzuleiten, ohne Evidenz zu kopieren oder neue historische Beziehungen zu erfinden?

Nicht Teil dieses Tests:

- kein neuer Research-Module-Datentyp;
- keine Pflichtausführung von `split | fuse | reframe | supersede | defer`;
- keine neue Relationstaxonomie;
- keine neue archäologische Method Truth;
- keine Requirement-/Architecture-Promotion;
- keine Änderung von `main`;
- keine Behauptung einer historischen Kontinuität zwischen Ranis und anderen Orlatal-Fundstellen.

## 2. Bindende vorhandene Mechanismen

Der Test verwendet nur bereits vorhandene Zustände und Schutzregeln:

- #45 + `docs/research/source-identity-protocol.md` – Quelle, Instanz, Fundstelle, Evidenz und Finding getrennt;
- #50 / `canonical-research-state.md` – stabile providerunabhängige IDs und Source → Representation → Instance → Findspot/Observation → Finding → Interpretation/Synthesis;
- #60 – Method Truth bleibt fachdomänenspezifisch und SOTA-gebunden;
- #61 – Work Context, leading/controlling domains, Method Debt und fail-closed Promotion;
- `REQ-EPI-006` – semantische Forschungszustände getrennt;
- `REQ-RSCH-001..004` – Research Hooks, Evidence Demand und Multi-Domain-Grenzen;
- `REQ-STATE-003` – research-ready Evidence Availability;
- `REQ-SPAT-001` / CAP-13 – kontrollierter Scale Shift;
- `REQ-UX-003` / CAP-17 – Views aus demselben State statt zweiter Wahrheit.

Die in #63 dokumentierte Owner-Korrektur bleibt leitend:

`Quelle → Aussage → Reichweite → Unsicherheit → Anschlussfrage → nächste Prüfspur`

und **nicht** `Quelle → Modul → Routing → Suchhaken`.

## 3. Reales Testmaterial

### 3.1 Reused Source Identity

Der Prototyp übernimmt **referenziell**, nicht als neue Wahrheit, die branch-lokale Source Identity aus #85:

- **source_id:** `RANIS-SRC-002`
- **Quelle:** Geoff M. Smith et al., “The ecology, subsistence and diet of ~45,000-year-old Homo sapiens at Ilsenhöhle in Ranis, Germany”, *Nature Ecology & Evolution* 8 (2024), 564–577.
- **DOI:** `10.1038/s41559-023-02303-6`
- **#85 Fixture:** `docs/research/cases/ranis-pilot/evidence-ledger.md`
- **#85 Fixture Commit:** `ffef72e40b6e769f74e4131f7971d3d37c7fcec2`
- **Authority:** `working/candidate`; keine Promotion des #85-Branches nach `main`.

### 3.2 Representation / inspected instance

Für diesen Test wurde die Open-Access-Version-of-Record am 2026-09-07 erneut direkt über die Nature/DOI-Seite inspiziert.

- **representation:** Nature Ecology & Evolution, Version of Record, HTML/PDF, veröffentlicht 2024-01-31
- **inspected_instance_id:** `RANIS-INS-002-NATURE-HTML-20260907`
- **locator:** `https://www.nature.com/articles/s41559-023-02303-6`
- **access:** direkt im aktuellen autorisierten Research Context geöffnet
- **availability:** `available / directly inspectable`
- **rights note:** Open-Access-Artikel; für diesen Prototyp werden nur bibliographische Daten, paraphrasierte Beobachtungen und Fundstellen gespeichert, keine Volltextkopie.

### 3.3 Fundstellen

- **excerpt/findspot_id `RANIS-EXC-002-A`:** Abstract – Materialumfang, dominante Tiergruppen, Karnivoreneintrag, schwankende menschliche Präsenz und source-authored Interpretation kurzer Aufenthalte.
- **excerpt/findspot_id `RANIS-EXC-002-B`:** Results → `Find densities` – Verteilung von Knochen-/Lithikfunden und source-authored Differenzierung zwischen stärkerer menschlicher Nutzung in Layer 8 und ephemererem menschlichem Input in anderen Schichten.
- **excerpt/findspot_id `RANIS-EXC-002-C`:** Discussion – source-authored Einordnung der geringen LRJ-Signatur als kleine, mobile Gruppen mit kurzen Aufenthalten sowie Hinweis auf weiteren Vergleichsbedarf mit gut kontextualisierten LRJ-Plätzen.

Diese Fundstellen sind absichtlich text-/abschnittsbezogen. Eine Figure-/Panel-Aussage wird hier nicht benötigt und daher nicht rekonstruiert.

## 4. Einmalig gespeicherte Observations

### `RANIS-OBS-002-01`

**Observation:** Smith et al. berichten für die Ausgrabungen 2016–2022 einen Bestand von 1.754 piece-plotted Knochenresten und kombinieren morphologische, zooarchäologische/palaeoproteomische, sediment-aDNA- und Isotopenanalysen. Im publizierten Befund treten starker Karnivoreneintrag und nur vergleichsweise wenige Schnitt-/Brandspuren zusammen auf.

- **source:** `RANIS-SRC-002`
- **instance:** `RANIS-INS-002-NATURE-HTML-20260907`
- **findspots:** `RANIS-EXC-002-A`, `RANIS-EXC-002-B`
- **status:** `observation / source-report`
- **scope:** publizierter Befund der Ilsenhöhle, nicht Orlatal allgemein

### `RANIS-OBS-002-02`

**Observation:** Die Autoren interpretieren die geringe archäologische LRJ-Signatur und die Schichtverteilung als schwankende bzw. teils ephemere menschliche Präsenz; ihre Synthese favorisiert kurze, zweckgebundene Aufenthalte kleiner mobiler Gruppen, während der Platz in erheblichem Maß auch von Karnivoren genutzt wurde.

- **source:** `RANIS-SRC-002`
- **instance:** `RANIS-INS-002-NATURE-HTML-20260907`
- **findspots:** `RANIS-EXC-002-A`, `RANIS-EXC-002-B`, `RANIS-EXC-002-C`
- **status:** `observation / source-authored interpretation`
- **scope:** source-lokal; keine unabhängige Histo-Orla-Fachvalidierung dieser Interpretation

Die Observation wird **einmal** gespeichert. Die folgenden Work Contexts referenzieren nur ihre ID.

## 5. Zwei Work Contexts über dieselbe Evidenz

### WC-88-A – Detail / site use

**Frage:** Welche publizierten Evidenzachsen tragen bei Smith et al. die Deutung einer schwankenden/kurzzeitigen menschlichen Nutzung der Ilsenhöhle im LRJ?

- **primary function:** Domain / Source Research, exploratory
- **scope:** Smith et al. 2024; Ilsenhöhle; source-local claim chain
- **evidence refs:** `RANIS-OBS-002-01`, `RANIS-OBS-002-02`
- **leading competence:** Paläolithische Archäologie / Zooarchäologie
- **controlling competence:** Taphonomie; Stratigraphie/Chronologie; biomolekulare Archäologie soweit die jeweilige Evidence-Achse betroffen ist
- **method status:** `method-debt / exploratory`; kein für diese konkrete Problemklasse nach #60 bereits als Histo-Orla-`working-method` validiertes Domain Method Profile nachgewiesen
- **must not:** source-authored Interpretation als unabhängige Fachvalidierung ausgeben

### WC-88-B – Scale Shift / Vergleichsbedarf

**Frage:** Welche Vergleichsdaten müssten für andere Fundstellen geprüft werden, bevor der Ranis-Befund in eine Orlatal-/inter-site-Synthese zu Nutzungsintensität oder Platzfunktion eingehen darf?

- **primary function:** Cross-disciplinary exploratory research / evidence-demand derivation
- **scope:** nur Ableitung von Vergleichsbedarf; keine Regionalaussage
- **evidence refs:** `RANIS-OBS-002-02`
- **leading competence:** Paläolithische Archäologie / Landschaftsarchäologie als zu prüfende fachliche Kombination
- **controlling competence:** Taphonomie und Chronologie/Stratigraphie
- **method status:** `candidate / method-debt`
- **must not:** Ranis-Befund auf Kniegrotte, Gamsenberg oder andere Plätze übertragen; Ko-Lokalität bzw. gleiche Großregion nicht als gleiche Funktion oder historische Kontinuität lesen

**Rekombinationsbefund:** `RANIS-OBS-002-02` wird in beiden Work Contexts referenziert, ohne Kopie und ohne Umformulierung seiner Evidenzbedeutung.

## 6. Quelle → Finding → Synthese-Candidate → Anschlussfrage

### `RANIS-FND-002-01` – source-bound working finding

**Finding:** Innerhalb des von Smith et al. publizierten Ranis-Datensatzes ist die Interpretation einer episodischen/kurzzeitigen menschlichen LRJ-Nutzung nicht aus einem Einzelmerkmal abgeleitet, sondern aus einer Kombination von Funddichte, Taphonomie/Karnivoreneintrag und mehreren naturwissenschaftlichen Evidence-Achsen. Die Interpretation bleibt eine source-authored archäologische Synthese und wird hier nicht als unabhängig validierte Histo-Orla-Fachwahrheit promoted.

- **supports:** WC-88-A
- **evidence:** `RANIS-OBS-002-01`, `RANIS-OBS-002-02`
- **status:** `working-candidate / source-bound`
- **confidence:** hoch dafür, dass dies die publizierte Argumentation korrekt repräsentiert; fachliche unabhängige Validierung `not performed`
- **limit:** keine Aussage zur Nutzungsart anderer Orlatal-Fundstellen

### `RANIS-SYN-88-01` – Synthese-Candidate

**Candidate:** Für einen späteren regionalen Vergleich sollte `Fundstelle vorhanden` nicht als hinreichend einheitliche Vergleichskategorie behandelt werden. Der Ranis-Fall legt als Research Hook nahe, Nutzungsintensität, menschlichen vs. tierischen Eintrag, stratigraphische Lage, Datierung und Evidenzqualität getrennt zu vergleichen.

- **status:** `synthesis-candidate / research-design hook`
- **nicht behauptet:** dass andere Plätze dieselbe Nutzung aufweisen; dass ein bestimmtes regionales Muster existiert; dass diese Vergleichsachsen bereits eine validierte generische archäologische Methode bilden

### `RANIS-HOOK-88-01` – nächste Prüfspur

**Anschlussfrage:** Für genau einen regionalen Vergleichsplatz – z. B. Kniegrotte oder Gamsenberg – eine direkt zugängliche fachwissenschaftliche/amtliche Quelle identifizieren und prüfen, ob ausreichend vergleichbare Informationen zu Chronologie, Funddichte, Taphonomie, menschlichem/karnivorem Eintrag und Site-Use-Interpretation vorliegen.

**Stop Rule:** Kein Vergleichs-Finding, solange die Vergleichsinstanz nicht direkt verfügbar und ihre fachliche Vergleichbarkeit nicht geprüft ist.

Damit ist die operative Schleife real:

`Quelle → Aussage → Reichweite → Unsicherheit → Anschlussfrage → nächste Prüfspur`.

## 7. Kontrollierter Scale Shift

**Ausgangsmaßstab:** Ilsenhöhle → Schichten/Funddichte/Taphonomie.

**Trigger:** Der source-lokale Befund wirft die Frage auf, ob `menschliche Präsenz` an anderen Fundstellen nach Intensität, Dauer, Agentenmix und Evidenzqualität differenziert werden muss.

**Zielmaßstab:** inter-site / regionaler Vergleich als **Research Question**, nicht als historische Synthese.

**Guard:** Der Scale Shift erzeugt nur Evidence Demand. Er erzeugt keine Beziehung `Ranis ↔ Kniegrotte/Gamsenberg` außer der expliziten analytischen Tatsache, dass sie als mögliche Vergleichsobjekte geprüft werden sollen.

**Ergebnis:** vorhandene Scale-Shift-/Research-Hook-Semantik reicht für diesen Schritt. Eine neue Relationsklasse ist nicht erforderlich.

## 8. Question Operations

Kein reales `split`, `fuse`, `reframe`, `supersede` oder spezielles `defer` war für diesen Minimaltest erforderlich.

Das ist ein **positiver Minimalitätsbefund**: Die Operationen werden nicht künstlich erzeugt, nur um ein Modell zu demonstrieren. Die zwei aktuellen Fragen sind normale Work Contexts über denselben State.

Disposition für eine eigene persistente Question-Operations-Semantik bleibt daher: `defer`.

## 9. Evidence Availability – Positiv- und Negativfall

### PASS – wissenschaftliche Quelle

`RANIS-SRC-002` / `RANIS-INS-002-NATURE-HTML-20260907` war im frischen autorisierten Context direkt erneut inspizierbar. Die nächste Aktion konnte ohne den Ursprungs-Chat ausgeführt werden.

### BLOCKED – Museumsfotos aus #85

#85 dokumentiert `RANIS-INS-IMG4495–4504` mit den Dateinamen `IMG_4495.jpeg` … `IMG_4504.jpeg`, speichert die Bildbytes aber ausdrücklich nicht in GitHub. Im aktuellen frischen Context sind nur die branch-lokalen Metadaten/Observations verfügbar, nicht die Fotos selbst.

Daher gilt für direkte neue Bildinspektion:

`identity known / metadata available / bytes unavailable → availability blocker`

Die Fotos werden in #88 **nicht** als direkt inspizierte Evidenz verwendet.

**Disposition:** `REQ-STATE-003` deckt den Befund bereits exakt ab. Kein neues Requirement erforderlich.

## 10. Zwei Views aus demselben State

Die Views sind hier bewusst nur Projektionen derselben IDs; sie besitzen keine eigene Evidenzwahrheit.

### View A – Ranis Site-Use Detail

| Feld | Referenz |
|---|---|
| Frage | `WC-88-A` |
| Source | `RANIS-SRC-002` |
| Instance | `RANIS-INS-002-NATURE-HTML-20260907` |
| Evidence | `RANIS-OBS-002-01`, `RANIS-OBS-002-02` |
| Finding | `RANIS-FND-002-01` |
| Method status | `method-debt / exploratory` |
| offene Grenze | keine unabhängige Histo-Orla-Domainvalidierung |

### View B – Regionaler Vergleichsbedarf

| Feld | Referenz |
|---|---|
| Frage | `WC-88-B` |
| reused Evidence | `RANIS-OBS-002-02` |
| source-bound Finding | `RANIS-FND-002-01` |
| Synthesis candidate | `RANIS-SYN-88-01` |
| Next research hook | `RANIS-HOOK-88-01` |
| Scale guard | Vergleichsbedarf ≠ historische Relation |
| offene Grenze | Vergleichsquelle noch nicht inspiziert |

Beide Views referenzieren denselben State. Es existiert keine zweite Kopie von `RANIS-OBS-002-02`.

## 11. Friktionslog

### F-88-01 – Kein neuer Research-Module-Mechanismus nötig

**Beobachtung:** Zwei unterschiedliche Fragen konnten dieselbe Evidence-ID referenzieren, ohne dass ein eigenes `ResearchModule`-Objekt benötigt wurde.

**Disposition:** `existing mechanism reused`.

### F-88-02 – Evidence Availability ist real und bereits abgedeckt

**Beobachtung:** Die user-provided Museumsfotos sind identifiziert und beschrieben, aber im frischen Context nicht direkt inspizierbar.

**Disposition:** `existing requirement / delivery friction`; `REQ-STATE-003` reicht semantisch. Kein Requirement Candidate.

### F-88-03 – Archäologische Method Truth ist für consequential Promotion noch nicht hinreichend operationalisiert

**Beobachtung:** Die Quelle kann korrekt quellengebunden wiedergegeben und als Research Hook genutzt werden; eine unabhängige fachliche Promotion einer archäologischen Synthese würde jedoch ein einschlägiges #60-Method Profile bzw. qualifizierte Fachprüfung benötigen.

**Disposition:** `existing method-debt under #60`; kein neuer Pilotmechanismus.

### F-88-04 – Manuelle Markdown-Komposition bleibt arbeitsaufwendig

**Beobachtung:** Der State ist semantisch ausreichend, wird im Pilot aber noch manuell in menschenlesbare Tabellen/Views komponiert.

**Disposition:** `existing delivery/UX friction`, bereits kompatibel mit #63-Feedback zu manueller/chat-orchestrierter Research-Arbeit sowie #50/#55/#61. Kein neuer fachlicher Requirement Candidate aus diesem Einzeltest.

### F-88-05 – Cross-branch Fixture muss exakt referenziert werden

**Beobachtung:** Die Source Identity `RANIS-SRC-002` stammt aus dem isolierten #85-Branch und ist nicht auf `main` promoted. Für Restartability muss deshalb Branch + Commit sichtbar sein.

**Disposition:** `case-specific test-fixture constraint`; kein neues State-Modell.

## 12. Ergebnis gegen die acht erlaubten #88-Punkte

| Test | Ergebnis | Beleg |
|---|---|---|
| realer Source/Instance/Observation-State | `PASS` | Smith et al. direkt re-inspected; IDs + Findspots getrennt |
| gleiche Evidence-ID in zwei Questions/Work Contexts | `PASS` | `RANIS-OBS-002-02` in `WC-88-A` und `WC-88-B` |
| Quelle → Finding → Synthese-Candidate → Anschlussfrage | `PASS` | `RANIS-FND-002-01` → `RANIS-SYN-88-01` → `RANIS-HOOK-88-01` |
| real auftretender Question Reframe | `NOT NEEDED` | nicht künstlich erzeugt; dedicated lifecycle bleibt `defer` |
| fachlich begründeter Scale Shift | `PASS` | site-local Finding → regionaler Evidence-Demand, kein Regionalclaim |
| Competence-/Method-Routing | `PASS / bounded` | leading/controlling domains sichtbar; Method Debt verhindert Promotion |
| zwei Views aus demselben State | `PASS` | View A + View B referenzieren dieselben IDs |
| Friktionslog | `PASS` | F-88-01..05; keine neue Ontologie als Lösung angenommen |

## 13. Prototype-Verdict

### `PASS – existing mechanisms sufficient for this slice`

Der kleine reale Ranis-Test **falsifiziert den Bedarf nach einem neuen persistierten `Research Module` als Voraussetzung dieses Workflows**.

Für diesen Slice reichen:

`Canonical Research State + Source/Instance/Findspot/Observation/Finding-Trennung + normale Research Questions/Work Contexts + Research Hooks + Method/Competence Routing + Scale Shift + Derived Views`.

Der Prototype beweist **nicht**, dass jede künftige hochvernetzte Forschungsarbeit ohne zusätzliche Struktur auskommt. Er zeigt nur: Der derzeit behauptete zusätzliche Mechanismus ist für diesen realen Fall nicht nötig.

## 14. Disposition für #86

- neues `Research Module`-Modell: `discard for now`
- eigene Question-Operations-State-Machine: `defer`
- neue Relationsontologie: `defer`
- Ranis als realer Stresstest: `keep case-specific`
- bestehende State-/Work-Context-/Scale-/View-Mechanismen: `reuse-existing`
- Requirement Candidate aus #88: **none**
- Generic Learning Candidate für `Wissensarbeit`: **none**; vorhandene generische Mechanismen reichen

## 15. Nächste erlaubte Aktion

#89 kann jetzt den **reframed** Pilot evaluieren. Dabei dürfen `aktive Module` nur als aktuelle `Research Questions / Work Contexts` verstanden werden.

Die Evaluation soll insbesondere prüfen:

1. ob ein frischer Bearbeiter die oben stehende Kette ohne Chat rekonstruieren kann;
2. ob dieselbe Evidence-ID bei einer Detail- und einer Scale-Shift-Aufgabe stabil bleibt;
3. ob der Availability-Blocker der Museumsfotos korrekt erkannt statt überspielt wird;
4. ob keine Regional-/Kontinuitätsaussage aus dem Scale Shift entsteht;
5. ob die Zusatzstruktur tatsächlich klein genug ist, dass `ResearchModule`/Question-State-Machine weiterhin unnötig bleiben.

Keine Promotion nach `main` vor der #89-Evaluation und anschließender Owner-Disposition von #86.
