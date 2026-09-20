# Cross-Pilot Saalfeld 1056–1071 – empirischer Reuse-/Modelltest

**Status:** `empirical cross-pilot / product-system-learning / no requirement-method-architecture authority`  
**Stand:** 2026-09-20  
**System-/Product-Review Owner:** #64  
**Historische Work Owner:** #46 und #103  
**Research Governance:** #45 + `docs/research/source-identity-protocol.md`  
**Method Truth:** #60  
**Requirements Authority:** #42  
**Architecture Authority:** #48 / #50

## 1. Zweck und Authority-Grenze

Dieser Versuch prüft an einem kleinen realen historischen Evidenzbestand die Working Hypotheses aus:

- `docs/research/discovery/problem-baseline.md` (post-baseline Owner/User-Research Synthesis),
- `docs/research-design/transdisziplinaerer-literaturassistent.md` (Working User-Research Hypothesis),
- `docs/architecture/assurance/shared-research-state-audit-20260919.md` samt späterem Caution-Hinweis,
- `docs/architecture/assurance/chat-operationalization-self-audit-20260920.md`.

Er erzeugt **keine** neue Ontologie, kein universelles Research-State-Modell, kein Requirement, keine Method Truth und keine Architecture Decision.

Die drei Ebenen bleiben getrennt:

```text
historische Ebene:
Source / Evidence → Observation → Finding → Interpretation/Synthesis

Product-/Workflow-Learning:
beobachtete Friktion/Fähigkeit → User-/Workflow-Observation → Hypothese/Gegenhypothese

System-Learning:
wiederholbar belegter Need → ggf. Requirement Candidate → #42
technische Diskriminationsfrage → #48/#50
Method Truth → #60
```

## 2. Fresh Bootstrap und Slice-Wahl

Vor dem Versuch wurden frisch gelesen:

1. Root `AGENTS.md`
2. Root `PROJECT_STATE.md`
3. Root `README.md`
4. #46 und #103 als historische Work Owner
5. #45 und `docs/research/source-identity-protocol.md`
6. #42, #48, #50, #60, #64, #92
7. aktuelle Requirements- und Architecture-Verträge
8. die vier oben genannten Self-Audit-/User-Research-Artefakte
9. die einschlägigen Case-Artefakte beider historischen Work Owner

Der Versuch **ändert keine Current-Work-Selection**. Er wird aufgrund des expliziten Owner-Auftrags dieses Cross-Pilot-Tests durchgeführt; daraus folgt kein `selected-current` für #46 oder #103.

### 2.1 Geprüfte Kandidaten

**Knau / 1374–1378 (#46):** wissenschaftlich relevant, aber für diesen Test ungeeignet, weil der aktuelle Konflikt primär innerhalb eines einzelnen Case-/Source-Resolution-Pfads liegt. Ein zweiter unabhängiger Research Context mit demselben kleinen Evidenzkern ist weniger klar.

**Sachenbacher-ID-Kollision (`SRC-LIT-0001` vs. `ARS-009`):** reale und nützliche Reconciliation, aber allein nur ein Dedup-/Identity-Test. Sie wäre als historischer Cross-Pilot zu dünn.

**Gewählter Slice: Saalfeld 1056–1071.**

Der Slice verbindet zwei reale, unterschiedliche Erkenntnisinteressen:

- **#46:** Saalfeld als räumlich-historiographischer Baustein in Sachenbachers Landesausbau-/Orlagau-Modell; Quellenbegriffe, Besitzraum, Zentralitätsmodell, Grenzen der Rückprojektion.
- **#103:** Richeza–Anno–Köln–Mainz–Saalfeld als Besitz-, Akteurs-, Rechts- und Institutionszusammenhang; Kanoniker/Mönche, Siegburg/St. Pantaleon, offene Rechtsakte.

Gemeinsam sind reale Sources/Representations, Saalfeld als historischer Gegenstand, die Richeza/Köln-Überlieferung und Teile des 1071er Evidenzkomplexes. Die Interpretationsziele bleiben verschieden.

## 3. Historischer Research Output – Synopsis

**Kanonische historische Details liegen ausschließlich in den Case-Artefakten:**

- #46: `docs/research/cases/u2-sachenbacher-2022-landesausbau-model-check.md`
- #103: `docs/research/cases/anno-richeza-saalfeld-netzwerk.md`
- #103 Source Ledger: `docs/research/cases/anno-richeza-saalfeld-source-ledger.md`
- gemeinsame Sachenbacher Source Identity: `docs/research/cases/orlagau-source-ledger.md` → `SRC-LIT-0001`

Diese Sektion ist nur eine abgeleitete Cross-Pilot-Synopsis.

### A1 – 1056 und 1057 sind im aktuellen Evidenzstand keine bloß konkurrierenden Datumswerte

Der frühere Arbeitsstand komprimierte die Richeza/Köln-Saalfeld/Coburg-Übertragung häufig auf `1056` oder `1056/1057`.

Neu kontrolliert wurde `ARS-017`, Eduard Hlawitschka, S. 242–243 / PDF S. 22–23. Hlawitschka unterscheidet:

- eine 1056 getroffene Absprache;
- eine endgültige Durchführung im Sommer 1057;
- als Belegkette nennt er die Brauweiler `Fundatio`, Rheinisches Urkundenbuch I Nr. 97 und Oedigers Regesten.

Sachenbachers DDE-Repräsentation formuliert kompatibel `1056 Schenkung → 1057 Bestätigung Annos II.`.

**Status:** `scholarly-source-critical finding / direct-edition-check-open`.

**Nicht behauptet:** welche juristischen Teilakte diplomatisch exakt zu unterscheiden sind. Die direkte Kollation von Brauweiler `Fundatio` und RUB I Nr. 97 bleibt offen.

### A2 – der 1056/1057-Befund ändert auch die Relationsinterpretation

Die bisher grobe Relation `Richeza → reported-transfer-to → Köln` bleibt als Navigation brauchbar, reicht aber für eine rechtshistorisch consequential Aussage nicht aus. Für diesen konkreten Fall müssen mindestens Phasen, Rollen, Gegenstände und Überlieferungskontext erhalten bleiben.

Das ist **kein** Beleg dafür, dass alle historischen Relationen Events oder n-äre Assertions sein müssen. Einfache Relationen wie `Anno II. → office-holder-of → Köln` bleiben im selben Slice fachlich ausreichend.

### A3 – 1071 bleibt quellenmäßig zweigleisig

- Lamperts 1071er Bericht (`ARS-005`) trägt quellennahe Beobachtungen zu Kanonikern und Mönchen aus Siegburg/St. Pantaleon sowie zu Lamperts eigener Erkundung.
- MUB I Nr. 331 (`ARS-004`) ist identifiziert, aber im aktuellen Work Pass noch nicht vollständig atomar exzerpiert und überlieferungskritisch gebunden.

Daher darf die institutionelle Umwandlung 1071 als Arbeitsbefund genutzt werden, während konkrete Rechte, Rollen und Rechtsform des Urkundentexts `source-collation-open` bleiben.

### A4 – Sachenbacher-Identität wurde ohne Claim-Merge reconciliert

`ARS-009` in #103 und `SRC-LIT-0001` in #46 bezeichnen bibliographisch dieselbe Publikation Peter Sachenbachers von 2022. Die DDE-Seite ist eine Representation/Instance dieser Source, nicht eine zweite Source Identity.

Die #103-Alt-ID bleibt als Legacy Alias für Provenienz erhalten; neue Verweise benutzen `SRC-LIT-0001`.

Diese Mutation ändert **keine** historische Aussage. Sie korrigiert Source Identity.

## 4. Cross-Pilot-Reuse-Befund

### 4.1 Tatsächlich gemeinsam wiederverwendbar

| Gegenstand | #46 Nutzung | #103 Nutzung | Reuse-Urteil |
|---|---|---|---|
| `SRC-LIT-0001` Sachenbacher 2022 | Modell-/Raum-/Literaturrouter | regionale Sekundärdarstellung für Saalfeld-Institution/Besitz | **shared Source Identity** |
| DDE-Repräsentation derselben Publikation | Volltextnavigation/Fundstellen | inspizierter Saalfeld-Abschnitt | **shared Representation/Instance**, sofern Inspection-State/Fundstelle erhalten bleibt |
| Saalfeld als historischer Referent | Zentralort-/Raumfrage | Besitz-/Institutions-/Akteursfrage | **shared referent**, aber unterschiedliche fachliche Aussagen |
| Richeza/Köln 1056→1057 | räumlicher Besitzkomplex / Modellanker | Rechts-/Akteurs-/Besitzfolge | **shared evidence, context-specific interpretation** |
| Lampert 1071 `ARS-005` | institutioneller Baustein für Saalfeld-Sequenz | Akteurs-/Kloster-/Reformrelationen | **source-near observations reusable by reference** |
| MUB I Nr. 331 `ARS-004` | Raum-/Kirchen-/Besitzfrage | Rechte/Rollen/Institutionen | **shared source target, not yet shared promoted Finding** |

### 4.2 Was nicht still geteilt werden darf

Nicht als gemeinsame „neutrale Semantik“ behandelt werden können:

- rechtshistorische Bedeutung der 1056/1057-Akte;
- historische-geographische Bedeutung von `in Orla`, `provincia`, `pagus` oder modernem `Orlagau`;
- Sachenbachers Landesausbau-/Zentralitätsmodell;
- Netzwerk-/Beziehungsbedeutung der Akteurskonstellationen;
- institutionelle Labels wie `Gründung`, `Eigenkloster`, `Reformkloster`, `Reichsabtei`;
- Promotions-/Validierungsstatus, wenn unterschiedliche Domain Methods erforderlich sind.

### 4.3 Duplicate Identity, Context Loss, Semantic Drift

**Duplicate Identity – real beobachtet:** `SRC-LIT-0001` vs. `ARS-009`.  
**Disposition:** auf derselben Source Identity reconciliert; Legacy Alias bewahrt frühere Provenienz.

**Context Loss – real beobachtet:** `1056/1057` als flacher Zeitwert verdeckte eine mögliche mehrphasige Rechts-/Überlieferungssituation.  
**Disposition:** getrennte Beobachtungen/Phasen; direkte Quellenprüfung bleibt offen.

**Semantic Drift – real drohend:** `in Orla` → moderner `Orlagau` → zeitlose räumliche Einheit.  
**Disposition:** Quelle/Forschungsterminus und räumliche Rekonstruktion bleiben getrennt.

**Semantic Drift – real drohend:** grobe binäre Transferrelation → definitive juristische Aussage.  
**Disposition:** grobe Relation bleibt nur Navigation; consequential Rechtsinterpretation benötigt zusätzliche Evidenz/Methodik.

## 5. Besondere Prüfbereiche

### 5.1 Zeit – beobachtete Bedeutungen, keine Taxonomie

Im Slice treten mindestens folgende verschiedene zeitliche Rollen auf:

- Datum/Phase eines historischen Rechtsvorgangs: 1056 / Sommer 1057;
- Geltungs-/Lebenszeitbezug: Richezas vorbehaltene lebenslange Nutzung in Sekundärdarstellungen;
- institutionelle Veränderung: 1071;
- Entstehungs-/Überlieferungszeit einer Quelle: mittelalterliche Akte, spätere Überlieferung/Kopie, moderne Edition;
- spätere Memorialisierung: Vita-Annonis-Kontext um 1183;
- analytische Periodisierung: Sachenbachers Phasen `10./11. Jh.`, `12. Jh.` usw.;
- Research-/Revisionsgeschichte: Inspektion und Reconciliation 2026.

Der Pilot zeigt, dass `date` als undifferenzierter Einzelwert unzureichend wäre. Er zeigt **nicht**, dass diese Liste eine universelle Temporalitätstaxonomie ist.

### 5.2 Raum

Beobachtet werden:

- historischer Ort Saalfeld;
- Besitz-/Relationssprache wie `in Orla`;
- historisch variierende Raumbegriffe `provincia Salaveld`, `pagus`, `terra/Land Orla`;
- moderne Forschungsbegriffe wie `Orlagau`;
- rekonstruierte Grenz-/Zentralitätsmodelle.

Historische Ortsidentität, Quellenformulierung, räumlicher Geltungsbereich und forschungsseitige Rekonstruktion dürfen nicht verschmolzen werden. Der Slice benötigt dafür keine vorab festgelegte Geometrie.

### 5.3 Relationen

**Binär ausreichend:** `Anno II. → office-holder-of → Erzbistum Köln`.

**Binär nur als grobe Navigation ausreichend:** `Richeza → transfer → Köln`; der reale Forschungsbedarf fragt zusätzlich nach Phase, Rechtsform, Objektkomplex, Nutzungsreservat, Beteiligten und Quelle.

**Mehrere Relationsebenen gleichzeitig:** Kanoniker in Saalfeld, Mönche aus Siegburg/St. Pantaleon, Anno/Siegfried und institutionelle Umwandlung 1071.

Folgerung: Der Pilot falsifiziert keine binären Relationen. Er falsifiziert aber die stärkere Annahme, **jede** fachlich relevante Beziehung dieses Slices könne ohne Verlust als unqualifizierte binäre Kante behandelt werden.

### 5.4 Quellenkontext

Direkt dokumentierbar:

- Source Identity;
- Representation/Instance;
- Fundstelle;
- Überlieferungs-/Editionsstatus, soweit geprüft;
- wer/was im Quellentext berichtet wird.

Nicht als neutrales Source-Metadatum behandelt werden:

- Annos „Motivation“;
- Richezas strategische Interessen;
- Missions-/Herrschaftsabsicht;
- Diskursfunktion oder Deutungshoheit.

Solche Aussagen sind fachliche Interpretation und benötigen eigene Evidenz/Methodik.

## 6. Modell-Falsifikation H1–H7

| Hypothese | Ergebnis | konkrete Evidenz aus dem Pilot | Grenze / Gegenhypothese |
|---|---|---|---|
| **H1 – gemeinsamer evidenzieller Untergrund** | **partially supported** | `SRC-LIT-0001`, DDE-Repräsentation, `ARS-005`, `ARS-004` und historische Referenten werden von #46/#103 real gemeinsam benötigt. | Der aktuelle Repo-State hatte dieselbe Source doppelt identifiziert; nicht jede Observation/Finding-Atomisierung ist ohne Method Context teilbar. |
| **H2 – perspektivische Transformierbarkeit** | **partially supported** | derselbe Saalfeld-Komplex lässt sich räumlich/historiographisch und akteurs-/institutionsbezogen untersuchen, ohne eine Achse als Grundmodell zu privilegieren. | Einige „Transformationen“ erzeugen neue Interpretation oder neue Assertion und sind dann Mutation statt View. Nur zwei Perspektiven getestet. |
| **H3 – Fachpluralität** | **supported** | Source Identity, Instance, Findspot, source-near Aussage und Unsicherheit können gemeinsam sein; Rechtsdeutung, Raumrekonstruktion, Modellprüfung und Relationssemantik bleiben fachkontextgebunden. | Weitere Domänen könnten eine andere Grenzziehung benötigen. |
| **H4 – Projection vs. Mutation** | **supported** | Auswahl derselben Saalfeld-Evidenz für #46/#103 = Projection; `ARS-009 → SRC-LIT-0001` = Identity-Mutation; 1056/1057 als Rechtssequenz festzulegen wäre Research-Mutation. | Die genaue Product-Grenze zwischen gespeicherter View und neuer Assertion bleibt implementationsoffen. |
| **H5 – Quellen-/Evidenzkontext** | **partially supported** | innerhalb beider Cases sind Source→Fundstelle→Observation und offene Status rekonstruierbar. Die Alias-Korrektur verbessert Round-trip. | inverse Navigation Source→alle Observations/Findings/Fragen über beide Cases ist derzeit manuell und fragmentiert. |
| **H6 – Widerspruch und Pluralität** | **supported** | 1056/1057 = wahrscheinlich Phasen/Überlieferung statt einfacher Widerspruch; 1071er spät/gefälscht diskutierte Grenztradition = Quellenkritik; Sachenbachers Landesausbaumodell = Historiographie, nicht Quellenwiderspruch; Orlamünde-Mitgift bleibt unresolved. | direkte Kollation kann einzelne Dispositionen verändern. |
| **H7 – Forschungsfrage als Research State** | **partially supported** | #46 und #103 besitzen getrennten Scope, offene Knoten, Evidenzbedarf und Synthesestatus, obwohl Evidenz geteilt wird. #103 hält Interpretation bewusst offen. | Daraus folgt noch kein universelles Question-/Answer-Datenmodell; formale Revisions-/Antwortobjekte wurden nicht getestet. |

### 6.1 Explizit challengte stärkere Vorannahmen

Der Pilot **challengt** folgende stärkere Lesarten früherer Meta-Entwürfe:

1. **„Shared State“ bedeutet nicht, dass Findings/Relations vollständig zentralisiert werden müssen.** Der robusteste gemeinsame Kern liegt tiefer: Source/Representation/Instance/Findspot/Provenienz plus referenzierbare source-near Observations, soweit deren Proposition und Method Context wirklich identisch sind.
2. **Observation ist nicht automatisch kontextfrei.** Schon die Entscheidung, was atomar beobachtet wird, hängt an Forschungsfrage, Quelle und Methode. Reuse ist möglich, aber nicht jede Observation muss global canonical sein.
3. **Relation/Event ist keine universelle Grundform.** Im selben Slice genügt einmal eine einfache Relation, während ein anderer Vorgang qualifizierten Kontext benötigt.
4. **Eine Research Question ist nicht nur ein Filter.** Sie besitzt eigenen Scope, offene Punkte, Evidenzbedarf und Revisionsgeschichte. Gleichzeitig ist noch offen, wie viel davon systemweit formalisiert werden muss.

## 7. System-Learning

| Beobachtung | Klassifikation | bestehende Abdeckung / Disposition |
|---|---|---|
| dieselbe Publikation erhielt zwei Source IDs | **observed pain / capability** + **pure reconciliation issue** | REQ-SRC-001/002, REQ-STATE-001 und Source-Identity-Protokoll decken den Bedarf. Reconciliation im Pilot durchgeführt. **Kein neues Requirement.** |
| 1056/1057 wurde als flacher Wert komprimiert | **observed pain** | REQ-EPI-004, REQ-SYN-001/002 und fachliche Source Criticism decken das Bewahren von Alternativen/Phasen. **Method Research needed** für Diplomatik/Rechtsgeschichte; kein universelles Zeitmodell. |
| `in Orla` kann still zu `Orlagau`/Polygon driften | **observed pain** | REQ-SPAT-001 + REQ-SYN-001 bereits einschlägig. **Method Research needed** historische Geographie/Begriffskritik. |
| dieselbe Evidenz muss aus zwei Fragen nutzbar sein | **observed capability** | REQ-STATE-001, REQ-SYN-002, REQ-RSCH-004 und REQ-UX-001 tragen den Bedarf grundsätzlich. **Kein neues Requirement.** |
| Source→alle abhängigen Observations/Findings/Fragen ist cross-case nur manuell navigierbar | **observed pain / product-research-needed** | REQ-UX-001 deckt den vorwärts gerichteten Audit-Roundtrip stark; inverse Cross-Context-Navigation ist dort nicht eindeutig als eigene Acceptance formuliert. **Noch kein Requirement Candidate**: erst in einem weiteren realen Slice prüfen, ob einfache Links/Suche genügen oder ein wiederholbarer Need besteht. |
| komplexer Transfer braucht mehr Kontext als eine unqualifizierte binäre Relation | **Architecture Research Question**, nicht Architecture Decision | #50 muss nur dann konkretisiert werden, wenn reale Implementierung die notwendigen Rollen/Zeiten/Evidenz nicht verlustfrei tragen kann. Kein Event-/Graph-Zwang. |
| Research Questions haben eigenen Scope/Offenstand | **product/user-research finding** | kompatibel mit REQ-RSCH-001–004; formale Question-Objekte sind **unresolved / more research needed**. |
| direkte Kollation von Fundatio, RUB I Nr. 97, MUB I Nr. 331 fehlt | **Method Research needed / historical research debt** | #46/#103 + #60; **keine Systemlücke** allein aus fehlender Facharbeit. |

### 7.1 Keine Requirement-Promotion

Dieser Pilot erzeugt **keinen** neuen akzeptierten Requirement Candidate. Insbesondere werden nicht promoted:

- universelles Question-/Answer-Modell;
- globale Observation-Klasse jenseits bestehender Contract-Invarianten;
- universelle Relation-/Event-Taxonomie;
- Temporalitätstaxonomie;
- globale Entity Registry;
- Knowledge Graph / RDF / Property Graph / SQL / Document Store / Event Sourcing;
- GIS-zentrierte Architektur;
- Vector DB/RAG oder Agentenplattform.

## 8. Adversarialer Review der Generalisierungen

### G1 – „Source Identity sollte geteilt werden“

**Tragende Beobachtung:** exakt dieselbe Sachenbacher-Publikation war `SRC-LIT-0001` und `ARS-009`.  
**Einfachere Erklärung:** rein lokaler Dokumentationsfehler.  
**Gilt in beiden Piloten?** Ja, beide konsumieren dieselbe Publikation.  
**Need oder Lösungsidee?** Need = False-Duplicate vermeiden; globale Registry = nur eine mögliche Lösungsidee.  
**Falsifikator:** wenn geteilte Source Identity keine gemeinsame Provenienz oder keinen Fehler verhindert.  
**Unsicherheit:** Reconciliation-Mechanismus bleibt offen.

### G2 – „Source-near Observations können geteilt werden“

**Tragende Beobachtung:** Lamperts 1071er Aussage zu Kanonikern/Mönchen ist für beide Fragen relevant.  
**Einfachere Erklärung:** beide Cases liegen zufällig sehr nah beieinander.  
**Invariante oder Domänensemantik?** Proposition + Source/Findspot können invariant sein; Auswahl, Atomisierung und fachliche Bedeutung nicht zwingend.  
**Falsifikator:** zweiter Context benötigt andere Textsegmentierung oder widersprechende Editions-/Methodenentscheidung.  
**Unsicherheit:** deshalb H1 nur `partially supported`.

### G3 – „mehrphasige Zeit muss erhalten bleiben“

**Tragende Beobachtung:** 1056→1057.  
**Einfachere Erklärung:** nur dieser Rechtsvorgang ist kompliziert.  
**Need oder Lösung?** Need = keine semantische Glättung; „Temporal Ontology“ wäre Lösungsidee.  
**Falsifikator:** weitere Fälle zeigen zuverlässig nur Einzeltermine und keine Rollenunterscheidung.  
**Unsicherheit:** keine Taxonomie-Promotion.

### G4 – „einige Relationen brauchen Qualifier“

**Tragende Beobachtung:** Richeza/Köln-Transfer verliert bei binärer Kante Phase/Rechtsform/Objekt/Nutzungsreservat.  
**Gegenbeispiel im selben Slice:** `office-holder-of` genügt binär.  
**Folgerung:** flexible Ausdrucksfähigkeit ist plausibel; universelles Event-Modell gerade **nicht** bewiesen.

### G5 – „inverse Navigation ist ein Systembedarf“

**Tragende Beobachtung:** Source→alle abhängigen Fragen/Findings musste durch manuelle Repo-Suche rekonstruiert werden.  
**Einfachere Erklärung:** kleine Markdown-Basis hat noch keine Links gepflegt.  
**Need oder Lösung?** Need = schneller Cross-Context-Audit; Graph/Backlinks/Index = Lösungen.  
**Falsifikator:** ein weiterer Slice zeigt, dass vorhandene Suche/Links den Owner-Workflow ausreichend bedienen.  
**Disposition:** `unresolved / more research needed`.

### G6 – „Question State braucht ein eigenes Datenobjekt“

**Tragende Beobachtung:** #46/#103 besitzen je Scope, Teilfragen, Evidenzbedarf, offenen Stand und Revision.  
**Einfachere Erklärung:** diese Information kann in Work-Owner-/Case-Dokumenten bleiben.  
**Disposition:** das User-Research-Signal ist bestätigt; ein universelles Question-Objekt ist **nicht** bestätigt.

## 9. SOTA-/Repräsentations-Gegencheck ohne Technologiepromotion

Der Pilot wurde gegen zwei etablierte Referenzrahmen gespiegelt, ausschließlich um vorschnelle Generalisierung zu challengen:

- **W3C PROV-O** kann Provenienz über `Entity / Activity / Agent` und qualifizierte Rollen ausdrücken. Das zeigt, dass Histo-Orlas Provenienzbedarf nicht automatisch ein eigenes Speicherparadigma verlangt. PROV löst aber nicht die historische Bedeutung von `in Orla`, Rechtsakten oder Institutionslabels.
- **CIDOC CRM** ist event-zentriert und kann zeitliche/spatiale/akteursbezogene historische Relationen ausdrücken. Das zeigt, dass ein Event-Ansatz für den Richeza-Transfer technisch/fachlich modellierbar wäre. Der Gegenbefund `office-holder-of` im selben Slice zeigt jedoch, dass daraus kein Zwang zur universellen Eventisierung folgt.

Referenzen:

- https://www.w3.org/TR/prov-o/
- https://cidoc-crm.org/sites/default/files/Documents/cidoc_crm_version_7.1.2.html

**SOTA-Disposition:** mehrere Repräsentationen könnten die beobachteten Fähigkeiten liefern. Der Pilot diskriminiert keine Persistence-Technologie.

## 10. Handoff

### 10.1 Was hat sich historisch geändert?

- #103 unterscheidet nun 1056 Absprache/Schenkungstradition und Sommer-1057-Durchführung als quellenkritischen Arbeitsstand; direkte Primärkollation bleibt offen.
- #46 übernimmt diese Präzisierung in den räumlichen Modellcheck, ohne sie zu einer neuen Raum-/Zeitontologie zu machen.
- `ARS-009` ist als Legacy Alias der kanonischen Sachenbacher-Source `SRC-LIT-0001` reconciliert.

### 10.2 Was hat sich im Produktverständnis geändert?

- die schwache Form „gemeinsam referenzierbarer Evidenzuntergrund“ wird gestützt;
- die starke Form „gemeinsame zentralisierte Observation-/Relation-Spine“ wird durch Domänen-/Granularitätsabhängigkeit eingeschränkt;
- Projection und canonical Mutation konnten real unterschieden werden;
- inverse Cross-Context-Navigation bleibt als real beobachtete, aber noch nicht requirement-reife Friktion offen.

### 10.3 Kanonische Orte

- historische #46-Wahrheit: `docs/research/cases/u2-sachenbacher-2022-landesausbau-model-check.md`
- historische #103-Wahrheit: `docs/research/cases/anno-richeza-saalfeld-netzwerk.md`
- #103 Source/Instance State: `docs/research/cases/anno-richeza-saalfeld-source-ledger.md`
- Sachenbacher Source Identity: `docs/research/cases/orlagau-source-ledger.md` → `SRC-LIT-0001`
- Cross-Pilot-/System-Learning: dieses Artefakt unter #64

### 10.4 Offene Punkte

- Brauweiler `Fundatio` direkt kollationieren;
- Rheinisches Urkundenbuch I Nr. 97 direkt kollationieren;
- MUB I Nr. 331 vollständig exzerpieren + Überlieferungsstatus;
- prüfen, ob inverse Source→Question/Findings-Navigation in einem zweiten unabhängigen Slice erneut echte Friktion erzeugt;
- keine Universalisation der Zeit-/Raum-/Relationsbefunde ohne weitere Fälle.

### 10.5 Work-Owner-/PROJECT_STATE-Disposition

- #46 und #103 bleiben ihre jeweiligen historischen Work Owner.
- #64 besitzt dieses Product-/System-Learning.
- #60 bleibt Method Truth.
- #42/#48/#50 erhalten durch diesen Versuch **keine** neue Authority oder Decision.
- **Kein neuer Blocker** für #44.
- **Kein `PROJECT_STATE.md`-Update erforderlich:** der Pilot ändert weder globale Selection, Phase, Owner noch Architecture Gate.

### 10.6 Restartability

Ein neuer kompetenter Bearbeiter kann den Versuch ohne Chat fortsetzen, indem er frisch bootstrapt und anschließend die in 10.3 genannten vier kanonischen Artefakte liest. Offene direkte Quellenkollationen stehen in den Case-Dateien; die H1–H7-Bilanz und System-Learning-Disposition stehen ausschließlich hier.
