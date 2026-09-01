# Histo-Orla – Requirements Responsibility & Dependency Map

**Status:** `active derived traceability view / incremental completion`  
**Canonical Requirements Owner:** #42  
**Requirement Truth:** `requirements-baseline.md` + `requirements-extensions.md`  
**Structure Contract:** `requirements-structure.md`  
**Technical consumer:** #48/#59  

## 1. Zweck

Diese Datei ist eine **abgeleitete Responsibility-/Dependency-Sicht**. Sie ist keine zweite Requirement Truth.

Sie beantwortet für jedes accepted Requirement bzw. zunächst jeden Requirement-Cluster:

1. welche Fach-/Regelkompetenz die **Bedeutung** besitzt;
2. welche technische Kompetenz die **Umsetzung** verantwortet;
3. welche Verification Authority benötigt wird;
4. welche anderen Requirements logisch/fachlich/technisch vorausgesetzt oder begrenzt werden;
5. welche Wechselwirkungen für Architektur und Delivery relevant sind.

Fehlende Zuordnung bedeutet niemals automatisch `keine`.

Pflichtregel für accepted Requirements:

```text
domain_authority / controlling_competence = explizit
technical_delivery_competence = explizit oder not-applicable
verification_authority = explizit
dependencies = typisiert oder none-known | unresolved
interactions / constraints = explizit, wenn materiell
```

#42 besitzt den Lifecycle des Requirements. Fachliche Authority und technische Delivery Authority bleiben davon getrennt.

## 2. Kompetenzklassen

### Fach-/Regelkompetenzen

- Research Owner / User Value / Research Pain
- Research Integrity / Scholarly Requirements Engineering
- Diplomatik / Urkundenlehre
- Editionswissenschaft / Textkritik
- Archivistik / Registraturkunde
- RDM / Provenienz / Forschungsdatenmanagement
- historische Philologie / Semantik / Onomastik
- jeweilige historische Fachdomäne
- historische Geographie / Raumgeschichte
- Prosopographie / Personenidentifikation
- Historiographie / Quellenkritik
- OCR/HTR/DH + quellentypspezifische Paläographie
- Informationswissenschaft / IR
- Rights / Privacy / Security
- Research UX / Human Factors

### Technische Kompetenzen nach #24

- Software Architecture / Modular Systems Design
- Domain Modeling
- Data Engineering / Lifecycle
- Storage / Persistence
- Search / Information Retrieval Engineering
- Workflow / Pipeline Engineering
- Provenance / Audit
- Validation / Invariant Enforcement
- Test / Verification Engineering
- Interoperability / API Engineering
- Security / Access / Privacy
- Reliability / Recovery / Observability
- Local-first / Portability
- AI Integration Engineering
- spezialisierte OCR/HTR-/NLP-/Matching-Verfahren

## 3. Cluster-Mapping

| Requirement-Cluster | Domain Authority / controlling competence | Technical competence | zentrale Dependency-/Interaction-Typen |
|---|---|---|---|
| `REQ-EPI-*` | jeweilige Fachdomäne + Research Integrity; historische Semantik bei Terminologie | Domain Modeling; Validation/Invariant; Audit/UX; AI Integration begrenzt | beeinflusst Method/Validation/Synthesis; constrained durch Source/Evidence-Provenienz |
| `REQ-SRC-*` | Archivistik + Diplomatik + Editionswissenschaft + RDM | Domain Modeling; Data/Persistence; Provenance; Integration/API | Basis für OCR, Retrieval, Audit, Claims; Findspot verlangt Source/Instance-Trennung |
| `REQ-OCR-*` | OCR/HTR/DH + RDM + quellentypspezifische Fachkompetenz | spezialisierte OCR/HTR-Verfahren; Pipeline; Provenance; Benchmark/Test | requires Source/Instance/Derivative + Findspot; liefert Derivate an Retrieval |
| `REQ-RET-*` | IR + historische Philologie/Onomastik + jeweilige Fachdomäne | Search/IR Engineering; Query Logging; ggf. spezialisierte NLP-Verfahren | requires indexierbare Derivate/State; Varianten dürfen Entity Identity nicht vorwegnehmen |
| `REQ-CRIT-*` | Diplomatik/Textkritik/Historiographie + Fachdomäne | Provenance/Audit; Domain Modeling | depends on Source lineage; constrains Corroboration/Synthesis |
| `REQ-ENT-*` | Onomastik/Prosopographie/Fachdomäne + Research Integrity | Candidate/Promotion State; Matching/ER; Validation | depends on variants/context/provenance; constrains Relations/Networks |
| `REQ-REL-*` | jeweilige Fachdomäne + Quellenkritik | Domain Modeling; Audit; ggf. Graphalgorithmen nur als Analyse | requires Entity/Source context; co-presence must not become asserted relation |
| `REQ-SPAT-*` | historische Geographie + regionale Fachdomäne | Domain Modeling; Gazetteer/Geospatial Integration | depends on temporal entity resolution; interacts with Scale/Context/Synthesis |
| `REQ-ACT-*` | Sozial-/Herrschafts-/Politik-/Institutionengeschichte je Fall + Research Integrity | Domain Modeling; Audit/UX | depends on evidence, relations, temporal context; motive ≠ observed action |
| `REQ-SYN-*` | mehrere führende Fachdomänen + Research Integrity | Audit/UX; State composition; AI höchstens assistiv | depends on preserved evidence axes, discrepancy, method provenance |
| `REQ-UX-*` | Research Integrity + Research UX/Human Factors + Fachdomänen | UI/UX; Audit rendering; Query/State navigation | cross-cutting; must expose Source/Method/Uncertainty without back-write |
| `REQ-VAL-*` | Fachdomäne + Research Integrity; ggf. unabhängige Spezialisten | Validation/Invariant; Audit/Workflow | depends on Method/Evidence status; cannot be satisfied by correlated AI reviews |
| `REQ-WF-*` | Research Integrity + RSE | Workflow/Pipeline; Validation; Test; Reliability | enforces already-defined invariants; must not invent scholarly truth |
| `REQ-STATE-*` | RDM + Research Integrity | Persistence; Data Lifecycle; Portability; Recovery | cross-cutting prerequisite for restartability, audit, provider removal |
| `REQ-INT-*` | RDM/Interoperability + jeweilige externe Fach-/Owner-Grenze | API/Adapter; Integration; Portability | constrained by Source Identity, Rights, Availability, Provider removal |
| `REQ-LEAN-*` | Product/Research Owner + Software Architecture | Architecture/Maintainability | constrains means, never reduces accepted scientific/technical scope |
| `REQ-RGT-*` | Rights/Privacy/Security + Owner | Security/Access/Secrets; Policy/Admission | constrains external processing, integration and storage choices |
| `REQ-BND-*` | Research Integrity + Mediation Owner | Architecture boundaries; Authorization; State separation | constrains UI/export/write paths; Research State must not be back-written by mediation |
| `REQ-MTH-*` | jeweilige Fachdomäne + #60 + Research Integrity | Domain Modeling; Provenance; Validation; Handoff/Assurance | depends on REQ-EPI-001/VAL/WF; method status constrains promotion, not exploration |
| `REQ-RSCH-*` | jeweilige Fachdomäne + #60 + Research Integrity | State/Domain Modeling; Audit/Handoff | depends on Source/Method/Uncertainty; routes Evidence Demand across domains |
| `REQ-TRACE-*` | Research Owner für Goal/Nutzen/Pain + Research Integrity/Requirements Engineering | Software Architecture/RSE; Provenance/Audit; Validation; Test; CI/Automation | requires WF/LEAN/STATE; verbindet upstream G/N/P mit Decision/Delivery/Verification und realem Feedback; Owner-Feedback ≠ wissenschaftliche Evidence |

## 4. Bereits explizit bekannte Requirement-Abhängigkeiten

### Source / Findspot / OCR

```text
REQ-SRC-001 Source ≠ Representation
    ↓
REQ-SRC-002 inspected Instance
    ↓
REQ-SRC-004 Findspot Roundtrip
    ↑
REQ-OCR-001 Derivative Parentage
    +
REQ-OCR-002 Page/Folio/Region Mapping
```

`REQ-SRC-004` ist damit cross-cutting und kann nicht isoliert als UI-Zitierfeature behandelt werden.

### Method / Promotion / Validation

```text
REQ-EPI-001 Domain owns method/evidence
    ↓
REQ-MTH-001/002 Method Profile + fachliche Expressivität
    ↓
REQ-MTH-003 Method Version/Application
    ↓
REQ-MTH-004 method/evidence-bound Promotion
    ↔
REQ-VAL-001 consequence-based validation
    +
REQ-WF-001 deterministic formal invariants
```

`REQ-WF-001` darf nur den formal geklärten Teil erzwingen; es ist kein Ersatz für Domain Method Truth.

### Retrieval / Entity / Relation

```text
REQ-EPI-003 Terminologieebenen
    ↓
REQ-RET-002 kontrollierte Varianten
    ↓ candidate support
REQ-ENT-001 Entity Candidate/Promotion
    ↓
REQ-REL-001 Relation/Proxy-Trennung
```

Search Variants dürfen weder Entity Identity noch historische Relation automatisch behaupten.

### State / Integration / Restartability

```text
REQ-STATE-001 portable chat/provider-independent State
    +
REQ-STATE-002 curated vs regenerable
    +
REQ-INT-001 integration escape hatch
    ↓
REQ-STATE-003 research-ready Evidence Availability
    ↔
REQ-INT-002 Zotero / OneDrive / Histo-Orla boundaries
```

Identifizierbarkeit, Portabilität und tatsächliche Quellenverfügbarkeit bleiben getrennte Qualitätsdimensionen.

### Evidence / Criticism / Synthesis

```text
REQ-SRC-* + REQ-EPI-004/005
    ↓
REQ-CRIT-001 Source Dependence
    +
REQ-CRIT-002 Discrepancy before harmonization
    ↓
REQ-SYN-001 Evidence axes distinct
    ↓
REQ-SYN-002 synthesis preserves alternatives
```

### Value / Decision / Delivery / Feedback

```text
G-* / N-* / P-*  (#28)
        ↓ upstream driver
REQ-TRACE-001
    requires REQ-WF-001
    requires REQ-LEAN-001
    requires REQ-STATE-001
        ↓
#48 technical derivation / decision
        ↓
#59 implementation + verification
        ↓
#63 real owner/workflow feedback
        ↺
confirm | pain-persists | regression | new-pain | new-need | requirement-change
```

Wechselwirkungen:

- `REQ-WF-001` liefert das Prinzip der deterministischen Erzwingung; `REQ-TRACE-001` wendet es auf die Wert-/Delivery-Kette an.
- `REQ-LEAN-001` begrenzt die Mittelwahl; `REQ-TRACE-001` verhindert, dass „lean“ vom ursprünglichen Need/Pain oder accepted Scope entkoppelt wird.
- `REQ-STATE-001` stellt sicher, dass die Trace-/Feedback-Kette chat-/providerunabhängig fortsetzbar bleibt.
- `owner-workflow-acceptance` ist Verification Coupling zwischen fachlichem/produktbezogenem Nutzen und technischer Delivery; sie darf nicht durch Unit-/CI-Tests allein erfüllt werden.

## 5. Wechselwirkungen, die #48 explizit prüfen muss

Für architecture-significant Requirements reicht eine lineare Dependency nicht. #48 prüft mindestens:

- **reinforcing:** zwei Requirements unterstützen dieselbe Responsibility;
- **constraint:** ein Requirement begrenzt Lösungsspielraum eines anderen;
- **trade-off:** zwei Qualitätsziele können in Spannung stehen;
- **shared enabler:** eine kleine technische Fähigkeit erschließt mehrere Requirements;
- **shared failure domain:** ein technischer Ausfall verletzt mehrere Requirements gleichzeitig;
- **verification coupling:** mehrere Requirements können mit demselben Fixture/Gold Case geprüft werden;
- **rights/security coupling:** externe Verarbeitung verändert Zulässigkeit anderer Funktionen;
- **domain coupling:** ein technischer State wird von mehreren Fachmethoden unterschiedlich gelesen und darf sie nicht flatten;
- **value coupling:** eine technisch bestandene Funktion kann den zugrunde liegenden Research-Pain trotzdem nicht lösen; reale Nutzung bleibt daher relevante Verification-/Feedback-Ebene.

Beispiele:

- Human readability ↔ strukturierte/transactionale Persistenz: mögliche Spannung, keine automatische Technologieentscheidung.
- Portabilität ↔ Provider-Integration: Adapter/Export müssen Lock-in begrenzen.
- Progressive Disclosure ↔ epistemische Transparenz: UI darf Komplexität reduzieren, nicht Evidenzstatus verstecken.
- Automation ↔ Human Control: mechanische Arbeit automatisieren, epistemische Promotion nicht still automatisieren.
- Retrieval Recall ↔ False Merge Risk: mehr fuzzy Expansion kann Entity-Fehlzusammenführungen erhöhen.
- Technische Testabdeckung ↔ reale Nutzer-/Research-Wirkung: beides ist nötig, wenn die Acceptance tatsächlichen Workflow-Nutzen verlangt.

## 6. Migrationsregel

Die 39 Baseline-Requirements besitzen bereits überwiegend fachliche `Owner`- und Capability-Angaben. Die 14 Extensions besitzen diese Struktur noch nicht vollständig als eigene Felder.

Keine Big-Bang-Umschreibung. Aber **bevor ein Requirement architecture-/implementation-significant bearbeitet oder als verified markiert wird**, müssen mindestens vorhanden sein:

```text
domain_authority / controlling_competence
technical_delivery_competence oder not-applicable
verification_authority
dependencies = typisiert oder none-known | unresolved
material interactions / constraints
```

#48/#59 dürfen fehlende fachliche Authority nicht selbst ergänzen; Rückgabe an #42/#60 bzw. zuständige Fachdomäne. `REQ-TRACE-001` ist bereits vollständig strukturiert und wird durch #62/#63 deterministisch begleitet.

## 7. Leitregel

> **Jedes Requirement hat einen Lifecycle-Owner. Jedes fachlich relevante Requirement hat eine fachliche Authority. Jede technische Umsetzung hat eine Delivery-Kompetenz. Diese drei Rollen sind nicht dasselbe.**

> **Eine fehlende Dependency-Angabe bedeutet unbekannt – niemals automatisch unabhängig.**

> **Technische Erfüllung ist nicht automatisch Nutzer-/Research-Wirkung; wo Acceptance reale Nutzung verlangt, muss der Feedback-Pfad geschlossen werden.**
