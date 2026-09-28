# Competence-analysis preservation assurance contract

**Status:** `P0 assurance freeze / analysis-preservation QA / no domain-method promotion`  
**Work Owner:** #150  
**Applies to:** W1–W7 bounded preservation run  
**Source of meaning:** frozen owner-confirmed Source Lock  
**Non-status:** not Method Truth, not historical evidence, not Requirement, not Architecture.

# D. Corrected Quality Contract

## D1. Severity- und Verdict-Semantik

- **S0** – rein redaktionell; keine Bedeutungs-/Status-/Authority-Auswirkung.
- **S1** – lokale, eindeutig korrigierbare semantische Ungenauigkeit; kein Owner-Urteil nötig.
- **S2** – materieller Verlust, Flattening, Statusverschiebung oder ungesicherte Addition; Gate FAIL, bounded Revision erforderlich.
- **S3** – Authority-/Promotion-/Provenienz-/Source-of-Meaning-Verletzung oder nicht-deterministisch lösbarer Bedeutungsstreit; sofortiger STOP.

- **PASS** – positive Bedingung erfüllt und adversarialer Failure nicht vorhanden.
- **FAIL** – nachweisbarer Verstoß; nur bei explizit erlaubter, deterministischer Reparatur `REVISE`, sonst STOP.
- **UNRESOLVED** – aus zugelassenen Inputs nicht entscheidbar; niemals durch Plausibilität in PASS umwandeln.

## D2. QC-Matrix

| ID | Name | Protected Meaning / Why | Failure Prevented | Positive Acceptance | Adversarial Negative Test | PASS / FAIL / UNRESOLVED | Severity / Review | Checker(s) | Owner Trigger / Auto-Repair / STOP |
|---|---|---|---|---|---|---|---|---|---|
| QC-01 | Semantic Fidelity | Owner-bestätigter Analyse-Sinn; Source Lock ist semantische Basis | fluente „Verbesserung“ verändert Intent/Analyse | jede materiale Aussage ist semantisch äquivalent zum Source Lock oder als redaktionell markiert | `analysis hypothesis` wird zu „historische Methode erfordert“ | PASS=keine Bedeutungsverschiebung; FAIL=material shift; UNRESOLVED=mehrere plausible Source-Lesarten | S2, bei Source-Ambiguität S3 / semantic | W3 primary, W5 independent | Owner nur bei Source-Ambiguität; deterministische lokale Rückformulierung erlaubt; STOP-SEMANTIC bei unentscheidbar |
| QC-02 | Material Completeness | alle action-relevanten Analyseelemente | Detailverlust trotz formal vollständigem Text | jedes W1-/Oracle-Element `FULL` oder explizit dispositioniert | Profilname bleibt, Detectability/Inferenz/Handoff verschwinden | PASS=100% material coverage; FAIL=partial/missing; UNRESOLVED=Materialität selbst unklar | S2 / semantic+coverage | W3 primary, W5 challenge | Auto-Repair via W2 bei exaktem Missing; STOP-LOSS wenn nicht verlustfrei integrierbar |
| QC-03 | No Flattening | handlungsrelevante Unterschiede | Generalisierung löscht unterschiedliche nötige Aktionen | Source/Edition/Instance, Diplomatik/Textkritik, Evidence/Inference etc. bleiben unterscheidbar | „Dokumentprüfung“ ersetzt Diplomatik+Edition+Archivistik | PASS=Unterscheidungen action-relevant erhalten; FAIL=merged semantics; UNRESOLVED=Boundary wirklich offen | S2 / semantic | W3, W5 | bei offener Profilgrenze nicht entscheiden; STOP-SEMANTIC/LOSS wenn Zusammenführung nicht reversibel |
| QC-04 | Epistemic Status Fidelity | `analysis/scoping/no-promotion` | Persistenz wird als Method Truth/Requirement/Finding gelesen | Status und Non-Statuses explizit in Baseline/README/Issues | „Best Practice ist …“ ohne SOTA, oder `method-candidate` durch guten Text | PASS=kein höherer Status; FAIL=promotion; UNRESOLVED=Statusquelle kollidiert | S3 / epistemic-status | W3, W4, W5 | keine Auto-Promotion; STOP-PROMOTION |
| QC-05 | Profile Depth | Kompetenz > Fachlabel | Profiles werden wieder zu Namen/Abstracts | jedes Profil trägt vorhandene Wissens-/Material-/Operation-/Inference-/QA-/Interface-Semantik oder `OPEN` | `Onomastik = Namen untersuchen` | PASS=Oracle-Dimensionen repräsentiert; FAIL=material detail loss; UNRESOLVED=Source trägt Feld nicht → `OPEN`, nicht FAIL | S2 / semantic+coverage | W3, W5 | Auto-Repair nur aus Source/W1; STOP-LOSS bei fehlendem Source-Material |
| QC-06 | Interface Integrity | Handoffs als methodische Objekte | „consult X“ ersetzt bounded fachliche Frage/Return | Trigger, outbound domain, question, evidence, uncertainty, requested return und return status vorhanden | nur Pfeil `→ Geographie` | PASS=Return-contract rekonstruierbar; FAIL=flattened handoff; UNRESOLVED=Source sagt nur Relevanz, keine Frage | S2 / semantic | W3, W5 | fehlende Source-Details als OPEN; keine Erfindung; STOP-SEMANTIC bei scheinbar nötiger Ergänzung |
| QC-07 | Activation Fidelity | material-/frage-/claim-/evidenzabhängige Aktivierung | vier Schichten werden lineare Pipeline/fixe Agentenkette | initial vs claim-driven Aktivierung und leading/controlling sichtbar | `A→B→C→D` als Pflichtworkflow | PASS=keine feste Reihenfolge; FAIL=pipeline hardening; UNRESOLVED=konkrete Aktivierung caseabhängig | S2 / semantic | W3, W5 | deterministische Textkorrektur möglich; wiederholter Fehler STOP-REPEATED-FAILURE |
| QC-08 | Uncertainty / Open-State Preservation | `candidate`, `competing`, `unresolved`, Widerspruch | Persistenz schließt Fragen künstlich | offene SOTA/Profile-/Validation-Fragen explizit; unknown fields `OPEN` | wahrscheinlichste Ortsidentität wird „confirmed“ | PASS=Open states erhalten; FAIL=false closure; UNRESOLVED selbst zulässig | S2 / semantic+status | W3, W5 | kein Auto-Close; STOP-PROMOTION/SEMANTIC bei Zwangsauflösung |
| QC-09 | Provenance / Source-Role Fidelity | Owner-confirmed synthesis ≠ disciplinary evidence; PRs ≠ source | Source-/Authority-Laundering | Source Lock, #147/#148, Repo-Governance mit Rollen beschrieben | PR147 wird „Quelle des Kompetenzmodells“ oder Owner-Bestätigung „Fachbeleg“ | PASS=Rollen korrekt; FAIL=falsche Source Role; UNRESOLVED=Provenienz unklar | S3 / provenance | W4 primary, W5 | keine Auto-Inferenz; STOP-PROVENANCE |
| QC-10 | Owner / Canonical-Home Fit | #22/#60/#45/#42/#23 Grenzen | Preservation Issue wird neuer Fachowner / zweite Wahrheit | jeder Inhalt hat genau einen kanonischen Ort; Issue nur Work Owner | README/Issue enthält Vollprofile parallel zur Baseline | PASS=Owner und Home eindeutig; FAIL=authority/duplication; UNRESOLVED=echter Owner-Konflikt | S3 / structural+authority | W4, W6, W5 | Routine-Referenzkorrektur erlaubt; echter Konflikt STOP-AUTHORITY/CONFLICT |
| QC-11 | Bounded Persistence / No Duplicate Truth | kleinste dauerhafte Struktur | Run erzeugt parallele Vollspeicher | Vollinhalt Baseline, Planung in Planning-Artefakten, Issue/README dünn | Profile vollständig in Baseline + Issue + README | PASS=kein manuelles Spiegeln; FAIL=second truth; UNRESOLVED=Artefaktrolle unklar | S2 / structural | W4, W6 | Auto-Repair durch Pointer statt Kopie; STOP-STRUCTURE wenn neue Struktur nötig scheint |
| QC-12 | Restartability | Fortsetzung ohne Chat | Handoff bleibt chatabhängig | W7 rekonstruiert Status/Owner/Open/Next aus Repo-Pfad | W7 braucht „was war im Chat gemeint?“ | PASS=Restart Oracle bestanden; FAIL=navigation/semantic restart failure; UNRESOLVED=benötigte Quelle nicht verfügbar | S2, bei semantischem Escape S3 / empirical | W7 | navigation-only REVISE→W6; semantic escape STOP-ASSURANCE-ESCAPE |
| QC-13 | Challengeability | Review muss scheitern können | Checkliste wird Selbstbestätigung | W3/W5 haben adversariale Fälle und echte FAIL/STOP-Verzweigungen | „gut formatiert = PASS“ | PASS=Reviewer kann S2/S3 feststellen; FAIL=criteria circular/non-discriminating; UNRESOLVED=independence fehlt | S2/S3 / assurance | W5 independent | fehlende Independence STOP-INDEPENDENCE |
| QC-14 | No Unauthorized Promotion | keine Downstream-Authority | Baseline ändert Requirements/Architecture/Methodstatus | explizite Non-Promotions; keine #42/#48 Promotion | Baseline erzeugt Requirement-Delta als accepted oder Architecture choice | PASS=no promotion; FAIL=material promotion; UNRESOLVED=Authority unklar | S3 / authority | W4, W5 | nie automatisch reparieren durch „wahrscheinliche“ Authority; STOP-PROMOTION/AUTHORITY |
| QC-15 | Evidence Dependency / Negative-Evidence Discipline | Abhängigkeit, Silence, Detectability | Treffer-/Nichttreffer-/Mehrquellen-Fehlschlüsse | abhängige Quellen ≠ independent; negative claims nur mit boundary | zehn abhängige Sekundärquellen als zehn Bestätigungen; „nicht gefunden=existierte nicht“ | PASS=Abhängigkeit/Boundary erhalten; FAIL=overclaim; UNRESOLVED=dependency unbekannt | S2 / semantic | W3, W5 | Textrepair aus Source erlaubt; keine neue Evidenzforschung; STOP-SCOPE wenn Nachweis nötig |
| QC-16 | No Master-Domain / Authority Smearing | Fachdomänen führen je Problem; Routing koordiniert | Coordinator/Epistemology wird Super-Expertise | leading/controlling getrennt, Routing besitzt keine Evidenzautorität | „Research Coordinator entscheidet endgültig“ | PASS=keine epistemische Superdomain; FAIL=authority smearing; UNRESOLVED=leadership case-specific | S2/S3 / semantic+authority | W5 primary, W3 | deterministische Korrektur möglich; echte Authority-Frage STOP-AUTHORITY |
| QC-17 | Case-vs-General Separation | Herrmann nur stress/activation example | case observation wird generische Methode/Finding | Beispiele als `case-derived analysis example / not historical finding` markiert | Hirschberg-Lesung wird generische Fachregel oder aktueller historischer Befund | PASS=case role klar; FAIL=generalization/promotion; UNRESOLVED=Source role unklar | S3 / semantic+provenance | W3, W5 | STOP-PROVENANCE/PROMOTION bei Rollenvermischung |
| QC-18 | Profile-Boundary Reversibility | heutige 15/16-Struktur bleibt hypothesenhaft | Persistenz macht Profilzuschnitt zur Ontologie | P6a/P6b adressierbar; `retain|split|merge|reframe` offen | „es gibt 16 endgültige Kompetenzen“ oder Datei-pro-Profil impliziert Finalität | PASS=reversibility explicit; FAIL=hardening; UNRESOLVED=Boundary offen ist erwarteter Zustand | S2 / semantic | W5 primary, W3 | keine automatische Boundary-Entscheidung; STOP-SCOPE wenn SOTA nötig |

## D3. Abdeckung zusätzlicher Schutzdimensionen

- **Source-role relationality** ist durch QC-01, QC-03, QC-09 geschützt.
- **leading/controlling separation** ist durch QC-05, QC-07, QC-16 geschützt.
- **handoff/return-contract preservation** ist durch QC-06 geschützt.
- **source/representation/instance/findspot distinction** ist durch QC-03, QC-09 und Source-Identity-Bootstrap geschützt.

Daher keine zusätzlichen QC-IDs nötig.

---

# E. Corrected Coverage Oracle

## E1. Cross-cutting Oracle

| ID | Semantic object | Must-preserve meaning | Forbidden flattening | Source anchor/type | Representation class | QC | Verification |
|---|---|---|---|---|---|---|---|
| CO-01 | relationale Quellenrolle | Primär/Sekundär ist frage- und claimgbezogen, nicht rein absolute Dokumenteigenschaft | starres Dokumentlabel | owner-confirmed shared concept | shared principle | 01,03,09 | W1 mapping + W3 compare |
| CO-02 | Quellentypfaktoren | Materialart × Entstehungsfunktion × Überlieferungs-/Repräsentationsstufe × Forschungsfrage × Claim unterscheidbar | nur „Dokumenttyp“ | shared concept | relation model | 01,03 | W3 semantic comparison |
| CO-03 | Forschungsdarstellung als Repräsentation | Karte/Tabelle/Rekonstruktion in Forschungsliteratur zunächst Autor-/Forschungsprodukt | als unabhängige historische Evidenz behandeln | shared concept | source-role rule | 09,17 | adversarial case W5 |
| CO-04 | Quellenrouter | Fußnoten/Bibliographie/Archiv-/Editionshinweise routen, ersetzen aber Quellprüfung nicht | Router=Evidence | shared concept | retrieval/provenance rule | 03,09,15 | W3/W5 |
| CO-05 | Source chain | historische Quelle ≠ Edition/Reproduktion ≠ Forschungsdarstellung ≠ Instanz ≠ Fundstelle ≠ Interpretation | ein `source`-Objekt für alles | owner-confirmed + binding source identity | identity/provenance invariant | 03,09 | W4 + W5 |
| CO-06 | Kompetenz ≠ Fachlabel | Operationalität verlangt eigene Modelle/Logiken/Operationen/QA/Interfaces | Disziplinname genügt | owner-confirmed meta-analysis | meta-competence principle | 05 | profile oracle |
| CO-07 | Wissensbasis | Kompetenz besitzt fachlich spezifische knowledge base | generisches „historisches Wissen“ | meta-analysis | profile dimension | 05 | W3 |
| CO-08 | Material-/Quellenmodell | relevante Evidenzarten + Formation + Grenzen | Quellenliste ohne Formation | meta-analysis | profile dimension | 05,15 | W3 |
| CO-09 | Observability/Detectability | was beobachtbar/nicht beobachtbar und unter welchen Erhaltungsbedingungen | Silence=Absence | meta-analysis | inference condition | 05,15 | W3/W5 |
| CO-10 | fachliche Operationen | Kompetenz muss konkrete Operationen ausführen können | Themenliste | meta-analysis | profile dimension | 05 | W3 |
| CO-11 | Evidence Appetite | Suchsprache/Evidenzbedarf domänenspezifisch | generische Websuche | meta-analysis | retrieval dimension | 05 | W3 |
| CO-12 | erlaubte Inferenzen | Evidence→Claim-Grenzen explizit | Plausibilität=Schluss | meta-analysis | inference dimension | 05,15 | W3/W5 |
| CO-13 | verbotene Inferenzen | ohne Zusatzbeleg unzulässige Schlüsse sichtbar | nur positive Regeln | meta-analysis | inference boundary | 05,15 | W3/W5 |
| CO-14 | Failure Modes | Overclaims/Fehlwege Teil der Kompetenz | nur „best practice“ | meta-analysis | QA dimension | 05,13 | W3/W5 |
| CO-15 | Unsicherheit | candidate/competing/unresolved/Widerspruch gültig | Zwangssynthese | meta-analysis | status dimension | 08 | W3/W5 |
| CO-16 | leading/controlling/not responsible | Zuständigkeit ist problem-/claimabhängig | jede aktivierte Domäne entscheidet alles | meta-analysis | routing dimension | 07,16 | W5 |
| CO-17 | vier Schichten | Analyseordnung A–D, keine Pipeline/Ontologie | Step 1–4 | owner-confirmed architecture finding | analysis map | 07,18 | W5 |
| CO-18 | dynamische Aktivierung | Material, Frage, Claim, Evidenz bestimmen Aktivierung | fixe Agentenkette | owner-confirmed | activation rule | 07 | W5 |
| CO-19 | Schnittstellen | fachliche Übergaben sind eigene methodische Objekte | „consult X“ | owner-confirmed | interface model | 06 | interface oracle |
| CO-20 | Handoff contract | Trigger, Frage, Evidence/Context, Unsicherheit, requested return | bloße Referenz | owner-confirmed | interface contract | 06 | W3/W5 |
| CO-21 | Inkommensurabilität | Terminologien/Evidenzlogiken dürfen bei Handoff nicht still vereinheitlicht werden | Universalvokabular | owner-confirmed | interface constraint | 03,06 | W5 |
| CO-22 | kein Master-Domain | Routing koordiniert, keine epistemische Oberhoheit | Coordinator=Truth | owner-confirmed + #45 | authority rule | 16 | W5 |
| CO-23 | erste Erschließung | wissenschaftlichen Aufsatz kompetent erschließen ≠ sofort jeden Primärbeleg verifizieren | Totalverifikation als Startpflicht | owner-confirmed | activation/scope rule | 07 | activation oracle |
| CO-24 | claim-driven depth | Vertiefung nach Claim: Urkunde, Lesung, Name, Überlieferung, Raum, Material, Gesamtinferenz | alle Profile immer aktiv | owner-confirmed | activation rule | 07 | W3/W7 |
| CO-25 | Evidence dependency | mehrere abhängige Publikationen ≠ unabhängige Bestätigung | Trefferzählung | profile P1/P14 | inference rule | 15 | W3/W5 |
| CO-26 | negative findings | `kein Treffer`/Schweigen nur mit Search-/Detectability Boundary | absence claim ohne boundary | P1/P7/P13/P14 | inference rule | 15 | W3/W5 |
| CO-27 | epistemische Kette | Claim→Evidence→Method→Inference→Scope→Confidence/uncertainty→competing explanation→falsifier | nur Claim+Quelle | P4/P14 | integration model | 05,13 | W3/W5 |
| CO-28 | Case role | Herrmann-Beispiele dienen Activation/Stress, keine historischen Findings | Case→Truth | owner-confirmed | case role | 17 | W3/W5 |
| CO-29 | Profilgrenzen offen | heutiger Zuschnitt ist scoping; split/merge/reframe/retain offen | finale Taxonomie | owner-confirmed + #60 | boundary status | 18 | W5 |
| CO-30 | spätere SOTA/Validation | Methodenliteratur, Standards, Counterexamples, fachliche Validation erst unter #60 | Analyse=Method Truth | owner-confirmed + #60 | research debt | 04,14,18 | W4/W7 |
| CO-31 | AI/Automation Grenze | Assistenz/Mechanisierung erzeugt weder Evidenz noch Fachurteil/Authority | AI output=Evidence | owner-confirmed + #45 | authority/automation rule | 14,16 | W5 |
| CO-32 | Persistenz ≠ Promotion | Sicherung schließt Persistence/Representation, nicht fachliche Erkenntnis/Methodik | Datei existiert=Gap closed | owner-confirmed + material_state | lifecycle rule | 04,08,14 | W7 |

## E2. Operational-Competence Meta-Oracle – 26 Dimensionen

| ID | Must-preserve question | Erwartete Behandlung im Baseline-Artefakt |
|---|---|---|
| OC-01 | Welche Problemtypen? | pro Profil benennen oder `OPEN / NOT YET ESTABLISHED`; keine erfundene Fachbreite |
| OC-02 | Wann leading? | explizit, soweit Analyse trägt |
| OC-03 | Wann controlling? | explizit, soweit Analyse trägt |
| OC-04 | Wofür nicht zuständig? | Boundary/Handoff statt Superkompetenz |
| OC-05 | Welche Begriffe/Gegenstandsmodelle? | material vorhandene Modelle nennen; keine SOTA-Ergänzung |
| OC-06 | Welche Quellen-/Materialtypen? | profileigen, nicht universalisiert |
| OC-07 | Wie entstehen sie? | Formation/Entstehungsfunktion, soweit analysiert |
| OC-08 | Was ist beobachtbar? | positive Beobachtungsgrenze |
| OC-09 | Was ist systematisch nicht beobachtbar? | Limits sichtbar; kein Silence overclaim |
| OC-10 | Preservation/Detectability? | Erhaltung/Suchbarkeit als Bedingung negativer Schlüsse |
| OC-11 | Welche Operationen? | konkrete Analyseoperationen statt Themenliste |
| OC-12 | Welche Evidenz trägt welchen Claim? | Evidence→Claim fit, Mindestschwellen ggf. OPEN |
| OC-13 | Welche Inferenzen erlaubt? | explizite erlaubte Schlussklasse, soweit Source trägt |
| OC-14 | Welche ohne Zusatzbeleg verboten? | explizite Verbote/Overclaims |
| OC-15 | Failure Modes? | profiltypische Fehlwege/Overclaims |
| OC-16 | Unsicherheit/Widerspruch/unresolved? | offene Zustände bleiben gültig |
| OC-17 | Counterevidence/Kontrollen? | bekannte Kontrolllogik; sonst OPEN |
| OC-18 | Search language/Evidence Appetite? | fachliche Suchsprache/Evidenzbedarf; nicht allgemeine Websuche |
| OC-19 | Wann andere Kompetenz? | Handoff trigger |
| OC-20 | Welche Handoff-Frage? | bounded question, soweit vorhanden |
| OC-21 | Welcher Return? | requested evidence/assessment/status |
| OC-22 | Terminologie-/Evidenz-Inkommensurabilitäten? | explizit oder OPEN, nicht still normalisieren |
| OC-23 | Methodenliteratur/Standards/Traditionen? | als spätere #60-Recherchefrage; keine Modellkenntnis ergänzen |
| OC-24 | Was technisch/regelbasiert unterstützbar? | nur bereits analysierte Grenzen; sonst OPEN |
| OC-25 | Was bleibt fachliches Urteil? | explizite Judgment Boundary; keine AI-Authority |
| OC-26 | Wann externe qualifizierte Validation? | Trigger bleibt OPEN, wenn nicht analysiert; nie durch Modellreview simulieren |

## E3. Profil-Level Oracle

**Gemeinsamer Status aller folgenden Profile:** `analysis/scoping / no Method Truth / no final taxonomy`.  
**Regel:** Wo der owner-bestätigte Analysebestand keine hinreichende profilbezogene Aussage trägt, steht ausdrücklich `OPEN / NOT YET ESTABLISHED`; es wird nichts aus Modellwissen ergänzt.

### P1 – Quellenkritik / historische Quellenkunde
- **Problem / Claim Types:** Entstehung, Funktion, Perspektive, Überlieferung, Aussagepotenzial und Aussagegrenze eines Materials; Abhängigkeit zwischen Quellen; negative evidence.
- **Leading when:** bevor ein historischer oder wissenschaftlicher Beleg sachlich interpretiert wird und sein Quellenstatus/Aussagewert die Schlussfähigkeit bestimmt.
- **Controlling when:** bei Claims, die von Quellenfunktion, Selektionslogik, Abhängigkeit oder Schweigen abhängen.
- **Not responsible for:** konkrete Textgestalt/Lesung, Urkundenauthentizität, Archivtektonik, fachhistorische Sachdeutung – dafür Handoff.
- **Knowledge base:** Quellengattungen, Entstehungs-/Kommunikationsfunktion, Perspektive, Selektions-/Überlieferungsbedingungen, Quellenabhängigkeit.
- **Core principles:** Quelle ≠ neutraler Faktenbehälter; Aussagewert fragebezogen; Schweigen nur bei Detectability; abhängige Publikationen ≠ unabhängige Bestätigung.
- **Object/terminology model:** Quelle, Darstellung, Aussage, Beobachtung, Überlieferung, Abhängigkeit, Perspektive; genaue spätere Fachterminologie OPEN.
- **Material model:** historische Quellen und Forschungsliteratur als funktional entstandene/überlieferte Materialien.
- **Formation:** Entstehungsfunktion und Überlieferungsweg sind Teil der Evidenzlogik.
- **Observable:** explizite Aussagen, Form/Funktion/Perspektive/Überlieferungsmerkmale soweit Material/Metadaten tragen.
- **Systematically non-observable:** nicht dokumentierte Vorgänge; Schweigen ohne Detectability darf nicht als Abwesenheit gelten.
- **Preservation/Detectability:** zwingend bei Negativbefunden.
- **Operations:** Quellentyp/Funktion/Perspektive/Überlieferung/Aussagegrenze bestimmen; Abhängigkeiten prüfen.
- **Minimum evidence:** claim-proportionate Source-/Context-Evidence; exakte Schwelle **OPEN**.
- **Evidence appetite / search language:** zusätzliche unabhängige Überlieferung/Quellenwege, wenn Abhängigkeit oder Schweigen entscheidend ist; detailliertes Vokabular **OPEN**.
- **Allowed inference:** nur innerhalb geklärter Aussagebedingungen.
- **Forbidden inference:** Silence→absence ohne detectability; source count→independence; spätere Darstellung→unmittelbarer Primärbefund.
- **Uncertainty:** competing reading/limits/unresolved explizit.
- **Counterevidence/control:** unabhängige Quelle, abweichende Überlieferung, Kontext, alternative Entstehungsfunktion.
- **Failure modes:** source laundering, false independence, negative-evidence overclaim, perspective flattening.
- **Observable proper application:** Bearbeiter kann begründen, warum dasselbe Material je Frage unterschiedlichen Evidenzwert hat und wo es nicht reicht.
- **Interfaces:** Diplomatik, Archivistik, Philologie, Historiographie, Sachdomänen, Epistemologie.
- **Handoff trigger/question:** z. B. „Trägt Authentizität/Textgestalt/Provenienz/Semantik den Claim?“
- **Required return:** Befund + Grenzen + uncertainty + welche Aussage dadurch bestätigt/begrenzt wird.
- **Incommensurabilities:** Quellengattungen besitzen unterschiedliche Evidenzlogiken; keine Universalmetrik.
- **Automation/AI boundary:** Struktur-/Metadatenhilfe möglich; fachliche Aussagegrenze bleibt Urteil. Details OPEN.
- **External validation:** Trigger **OPEN / #60**.
- **Open questions:** SOTA, Methodenliteratur, positive/negative/adversariale Cases.
- **Non-conclusion:** keine validierte universelle Quellenkritikmethode aus diesem Analyseprofil.

### P2 – Bibliographie / Source Identity / Publikationskompetenz
- **Problem / Claim Types:** eindeutige Identifikation von Werk, Ausgabe, Auflage, Reihe/Band, Beitrag, Instanz, Digitalisat, Fundstelle.
- **Leading when:** Reproduzierbarkeit/Zitation/Version die Basis eines Claims bildet.
- **Controlling when:** unterschiedliche Ausgaben/Instanzen den Wortlaut oder Fundstellenbezug verändern können.
- **Not responsible for:** historischen Wahrheitsgehalt oder editorische Textentscheidung.
- **Knowledge base:** bibliographische Identität, Editions-/Versionsgeschichte, Reihen/Periodika, Kataloge/Normdaten, persistente Identifier.
- **Core principles:** Werk ≠ Ausgabe ≠ Auflage ≠ Beitrag ≠ Instanz ≠ Fundstelle; filename/url ≠ identity.
- **Object model:** `Werk → Ausgabe → Auflage → Band/Reihe → Beitrag → Instanz → Digitalisat → Fundstelle`.
- **Material model:** Publikationen, Katalogdatensätze, Digitalisate, PDFs/Reprints/OCR als verschiedene Repräsentationen/Instanzen.
- **Formation:** Publikations-/Versions-/Digitalisierungsprozess relevant.
- **Observable:** bibliographische/instanzbezogene Merkmale, Seiten-/Scanrelationen, IDs.
- **Non-observable:** historische Wahrheit aus bibliographischer Identität allein.
- **Detectability:** fehlende IDs/Versionen als `unknown/not verified`, nicht ergänzen.
- **Operations:** Identifizieren, disambiguieren, zitieren, Versionen/Instanzen/Fundstellen koppeln.
- **Minimum evidence:** reproduzierbare Identitäts- und Fundstellenangabe; exakter fachlicher Schwellenstandard später prüfen.
- **Evidence appetite:** Kataloge, Normdaten, Editions-/Publikationsmetadaten, persistente IDs.
- **Allowed inference:** Identitäts-/Versionsaussagen aus verifizierten Metadaten.
- **Forbidden inference:** URL/Dateiname als Werkidentität; gleiche Titel als gleiche Edition.
- **Uncertainty:** Metadatenkonflikte sichtbar.
- **Counterevidence:** alternative Katalog-/Ausgabenangabe, Seiten-/Versionsabweichung.
- **Failure modes:** instance laundering, version conflation, citation non-reproducibility.
- **Proper application:** Dritte finden dieselbe benutzte Instanz/Fundstelle wieder.
- **Interfaces:** Editionswissenschaft, Archivistik, Retrieval, RDM, Historiographie.
- **Handoff:** bei wortlaut-/editionsrelevanten Unterschieden an P6b.
- **Return:** eindeutige Identität, Version/Instanz, Fundstelle, unresolved metadata.
- **Incommensurabilities:** Werk-/Instanz-/Archividentität folgen unterschiedlichen Praktiken.
- **Automation/AI:** Identifier-/Metadatenabgleich unterstützbar; semantische Identität bei Konflikt bleibt Urteil.
- **External validation:** OPEN.
- **Open:** fachliche Standards/SOTA für verschiedene Publikations-/Archivtypen.
- **Non-conclusion:** keine bibliographische Identität beweist historische Faktizität.

### P3 – Historiographie / Forschungsgeschichte
- **Problem / Claim Types:** Forschung als historisches Produkt; Begriffe, Modelle, Paradigmen, regionale Traditionen, Rezeption.
- **Leading when:** ältere/zeitgebundene Forschungsliteratur selbst Erkenntnisobjekt oder Grundlage historischer Rekonstruktion ist.
- **Controlling when:** moderne Analyse unbeabsichtigt ältere Modelle/Kategorien übernimmt.
- **Not responsible for:** direkte Primärquellenkritik oder aktuellen SOTA ohne Recherche.
- **Knowledge base:** Geschichte der Geschichtswissenschaft, Begriffsgeschichte, Fachdebatten, Rezeptionsgeschichte.
- **Core principles:** Autorenbeobachtung ≠ Autoreninterpretation ≠ zeitgenössisches Forschungsmodell ≠ spätere Rezeption ≠ aktueller Stand; älter kann empirisch nützlich und theoretisch überholt sein.
- **Object model:** Autor, Beobachtung, Interpretation, Modell, Schule/Tradition, Rezeption, Revision, heutiger Forschungsstand.
- **Material model:** Fachpublikationen, Debatten, Handbücher/Reviews, Forschungstraditionen.
- **Formation:** wissenschaftliche Aussagen entstehen in disziplinären/zeitlichen Kontexten.
- **Observable:** explizite Argumente/Begriffe/Quellenverwendung/Modellbezüge.
- **Non-observable:** heutiger Konsens allein aus einer historischen Publikation.
- **Detectability:** spätere Revision erfordert gezielte SOTA-/Rezeptionssuche.
- **Operations:** Schichten trennen, Modelle historisieren, Revisionen/Traditionen markieren.
- **Minimum evidence:** Publikation + Kontext; für „heutiger Stand“ zusätzliche aktuelle SOTA-Evidence.
- **Evidence appetite:** spätere Kritik/Reviews, konkurrierende Schulen, regionale Traditionen.
- **Allowed inference:** historische Aussage über Forschungspraxis, wenn text-/kontextgestützt.
- **Forbidden:** Autorposition als aktueller Konsens; neu=automatisch richtig; alt=automatisch falsch.
- **Uncertainty:** current status unresolved bis SOTA geprüft.
- **Counterevidence:** spätere Revision, alternative zeitgenössische Position.
- **Failure modes:** historiographic category laundering, presentism, latest-is-best.
- **Proper application:** sauber markierte Ebenen Autorbeobachtung/Modell/Rezeption/heutiger Status.
- **Interfaces:** Hermeneutik, Philologie/Begriffsgeschichte, Sachdomänen, SOTA-Research.
- **Handoff:** aktuelle Kontroversenlage unbekannt → #60/SOTA Research.
- **Return:** zeit-/traditionsgebundener Status + offene Aktualitätsfrage.
- **Incommensurabilities:** historische Fachbegriffe vs heutige analytische Kategorien.
- **Automation/AI:** Literaturchronologie/Begriffscluster heuristisch; historiographische Bewertung Fachurteil.
- **External validation:** OPEN.
- **Open:** profilbezogene SOTA-/Methodenliteratur.
- **Non-conclusion:** kein aktueller Fachkonsens ohne SOTA.

### P4 – Hermeneutik / Argumentations- und Evidenzanalyse
- **Problem / Claim Types:** Behauptung, Beleg, Prämisse, Zwischenschluss, Alternative, Kausalität/Analogie/Abduktion.
- **Leading when:** Argumentstruktur einer Quelle/Forschungspublikation rekonstruiert werden muss.
- **Controlling when:** komplexe Synthese oder Schlussketten auf impliziten Prämissen beruhen.
- **Not responsible for:** Quellenauthentizität, Wortlesung oder fachdomänenspezifische Prämissen allein.
- **Knowledge base:** Hermeneutik, Argumentation, Begründungs-/Inferenzstrukturen.
- **Core principles:** Aussage ≠ Beleg ≠ Schluss; Plausibilität ≠ Evidenz.
- **Object model:** `Evidence | inference | assumptions | alternatives | confidence`.
- **Material model:** Texte/Argumente mit expliziten/impliziten Prämissen.
- **Formation:** Argumente entstehen durch Auswahl/Verknüpfung von Evidenz und Modellen.
- **Observable:** explizite Claims/Belege; inferentielle Beziehungen teilweise rekonstruierbar.
- **Non-observable:** unausgesprochene Intentionen nicht sicher ohne Evidence.
- **Detectability:** implizite Prämissen als Rekonstruktion, nicht Autorwortlaut.
- **Operations:** Argument zerlegen; Evidence-Mapping; Alternativen/Counterarguments; confidence/limits.
- **Minimum evidence:** genaue Text-/Evidence-Anker für jeden tragenden Schritt; Schwelle domänenspezifisch OPEN.
- **Evidence appetite:** zusätzliche Quellen/Methoden nur soweit einzelne Prämissen tragen.
- **Allowed:** explizit markierte, quellen-/methodengebundene Inferenz.
- **Forbidden:** Zitat trägt mehr als Kontext; mehrstufige Schlusskette als „Fakt“.
- **Uncertainty:** Alternativen/Assumptions/confidence sichtbar.
- **Counterevidence:** konkurrierende Erklärung, widersprechender Beleg, ungültige Prämisse.
- **Failure modes:** evidence laundering, circular reasoning, hidden assumptions, narrative smoothing.
- **Proper application:** jeder tragende Schluss lässt sich auf Evidence+Assumptions+Alternatives zurückführen.
- **Interfaces:** P1, P3, P5, P8, P14.
- **Handoff:** sach-/sprach-/quellenkritische Prämisse unklar → zuständige Domäne.
- **Return:** geklärte/präzisierte Prämisse oder begrenzte Aussage.
- **Incommensurabilities:** argumentative Plausibilität vs domänenspezifische Evidenzstärke.
- **Automation/AI:** Strukturierung heuristisch möglich; valide Inferenz bleibt method-/domainabhängig.
- **External validation:** OPEN.
- **Open:** Methodenliteratur, domänenspezifische Inferenznormen.
- **Non-conclusion:** keine universelle Logik ersetzt Fachmethodik.

### P5 – historische Philologie / Semantik
- **Problem / Claim Types:** historische Wortformen, Lesung, Normalisierung, Übersetzung, Bedeutungsbereich, moderne analytische Kategorie.
- **Leading when:** Wortlaut/Bedeutung eines historischen Terms den Claim trägt.
- **Controlling when:** moderne Kategorie auf historischen Ausdruck projiziert wird.
- **Not responsible for:** paläographische Zeichenentscheidung ohne Bild/Schriftkompetenz; institutionelle Sachbedeutung allein.
- **Knowledge base:** historische Sprachentwicklung, Semantik, Sprach-/Begriffsgeschichte, philologische Normalisierung/Übersetzung.
- **Core principles:** keine zeitlose Wörterbuchbedeutung; Original→Normalisierung→Übersetzung→Analysebegriff getrennt.
- **Object model:** `source term | contemporary institutional term | editorial term | modern analytic term | historiographic term | search variant`.
- **Material model:** historische Texte/Editionen/Varianten und Übersetzungen.
- **Formation:** sprachliche Bedeutung zeitlich, regional, institutionell, pragmatisch gebunden.
- **Observable:** Wortformen/Kontext/Varianten soweit Textgrundlage trägt.
- **Non-observable:** eindeutige historische Bedeutung ohne Kontext/Belegserie.
- **Detectability:** Lesungs-/Überlieferungsunsicherheit muss erhalten bleiben.
- **Operations:** Lesung/Normalisierung/Übersetzung/semantische Range trennen; Kontextvergleich.
- **Minimum evidence:** textnaher Kontext + ggf. Varianten/Parallelbelege; genaue Schwelle OPEN.
- **Evidence appetite:** historische Sprachbelege, Varianten, institutionelle/regionale Kontexte.
- **Allowed:** begrenzte Bedeutungsoptionen/Range aus Kontext/Belegserie.
- **Forbidden:** moderne Definition rückprojizieren; Normalisierung=Original.
- **Uncertainty:** alternative Lesung/Bedeutung als competing/unresolved.
- **Counterevidence:** Parallelbeleg, Variantenapparat, anderer zeitgenössischer Gebrauch.
- **Failure modes:** anachronism, normalization laundering, timeless-dictionary fallacy.
- **Proper application:** Originalform, editorische/normalisierte Form und analytische Kategorie bleiben unterscheidbar.
- **Interfaces:** P6b, P11, P10, P8, P3.
- **Handoff:** unsichere Zeichen/Hand → P11; institutionelle Bedeutung → P8; Name → P10.
- **Return:** mögliche Lesungen/Bedeutungsgrenzen + confidence/unresolved.
- **Incommensurabilities:** source term vs modern analytic vocabulary.
- **Automation/AI:** Varianten-/Vokabelsuche heuristisch; historische Semantik Fachurteil.
- **External validation:** OPEN.
- **Open:** SOTA/Standards, mittellateinische/regionale Spezialisierung.
- **Non-conclusion:** keine bestätigte semantische Identität aus Ähnlichkeit allein.

### P6a – Diplomatik / Urkundenlehre
- **Boundary status:** analytisch von P6b unterscheidbar, endgültiger Split **OPEN**.
- **Problem / Claim Types:** Genese, Form, Funktion, Aussteller/Empfänger, Datierung, Beglaubigung, Kanzlei, Zeugen, Original/Kopie/Transsumpt/Fälschungs-/Authentizitätsfragen.
- **Leading when:** Urkundenstatus/Entstehungs- und Beglaubigungslogik den Claim trägt.
- **Controlling when:** edierter Urkundentext als unmittelbares Original behandelt wird.
- **Not responsible for:** konkrete Editionstext-/Variantenentscheidung allein (P6b), paläographische Zeichenentscheidung (P11).
- **Knowledge base:** diplomatische Genese/Form/Funktion/Authentizität – heutige Analyseannahme; konkrete SOTA **OPEN**.
- **Core principles:** Urkunde/Regest/Edition/Kopie nicht gleichsetzen; Beglaubigungs-/Formmerkmale funktional statt ornamental lesen.
- **Object model:** Aussteller, Empfänger, Formular/Teile, Datierung, Beglaubigung, Zeugen, Überlieferungsstatus.
- **Material model:** Original, Kopie, Transsumpt, edierte Urkunde, Regest als unterschiedliche Stufen.
- **Formation:** administrative/rechtliche Herstellung und spätere Überlieferung getrennt.
- **Observable:** diplomatische Merkmale soweit Original/Edition/Apparat zugänglich.
- **Non-observable:** Originalmerkmale aus Regest allein.
- **Detectability:** Editions-/Überlieferungsstufe begrenzt Prüfung.
- **Operations:** Genese/Form/Funktion/Authentizitäts-/Datierungsprobleme prüfen; Überlieferungsstatus bestimmen.
- **Minimum evidence:** geeignete Urkundenrepräsentation + Überlieferungs-/Editionsangaben; fachliche Schwelle OPEN.
- **Evidence appetite:** Original/Kopie/Edition/Apparat/Parallelüberlieferung; detaillierte Fachsuche OPEN.
- **Allowed:** gestufte Aussagen über Urkundenstatus/Funktion soweit Evidenz trägt.
- **Forbidden:** Regest=Urkunde; Edition=Original; Zeugenliste automatisch Präsenz-/Sozialbeweis ohne Methodenkontext.
- **Uncertainty:** Authentizität/Datierung/Überlieferung kann unresolved bleiben.
- **Counterevidence:** abweichende Zeugen/Datierungen/Kopien/Formularvergleich, Apparathinweise.
- **Failure modes:** authenticity overclaim, original/edition collapse, formula overinterpretation.
- **Proper application:** erklärt, welche Aussage die konkrete Überlieferungsstufe zulässt.
- **Interfaces:** P6b, P7, P11, P5, P8.
- **Handoff:** Textvariante/editorischer Eingriff → P6b; Schrift/Material → P11; Provenienz → P7.
- **Return:** Urkunden-/Überlieferungsstatus, prüfbare diplomatische Grenzen, unresolved.
- **Incommensurabilities:** diplomatische Genese vs editorische Textkonstitution.
- **Automation/AI:** Form-/Metadatenunterstützung möglich; Authentizitäts-/Funktionsurteil fachlich.
- **External validation:** OPEN/#60.
- **Open:** SOTA, konkrete Playbooks, Split/Merge mit P6b, positive/adversariale Cases.
- **Non-conclusion:** kein working-method.

### P6b – Editionswissenschaft / Textkritik
- **Boundary status:** analytisch von P6a unterscheidbar, endgültiger Split **OPEN**.
- **Problem / Claim Types:** Textzeuge, Editionsbasis, Varianten, Apparate, editorische Ergänzungen, Regest, editorische Identifikation.
- **Leading when:** konkrete Textgestalt/Variante/Editoreneingriff den Claim trägt.
- **Controlling when:** Editionstext oder Regest als historischer Originalwortlaut gelesen wird.
- **Not responsible for:** Urkundengenese/Authentizität allein (P6a), Schriftlesung ohne Material (P11).
- **Knowledge base:** Edition/Textkritik, Witness/Variant/Apparatus – konkrete SOTA OPEN.
- **Core principles:** `Regest ≠ Urkunde`; `Edition ≠ Original`; `editorische Ergänzung ≠ historischer Wortlaut`; `Register-ID ≠ Source-ID`.
- **Object model:** Textzeuge, Editionstext, Apparat, Variante, Ergänzung, Regest, editorische Identifikation.
- **Material model:** Original/Kopie/Abschrift/Edition/Regest/Apparat.
- **Formation:** editorische Auswahl/Normalisierung/Rekonstruktion ist eigene Repräsentationsstufe.
- **Observable:** Varianten/editorische Zeichen/Quellenbasis soweit Edition/Apparat trägt.
- **Non-observable:** Originalwortlaut ohne geeigneten Zeugen.
- **Detectability:** fehlender/verkürzter Apparat begrenzt textkritische Aussage.
- **Operations:** Zeugnisse/Varianten/Ergänzungen/Regest/Identifikation trennen; Editionsbasis bestimmen.
- **Minimum evidence:** konkrete Edition + Apparat/Zeugenangabe soweit claimrelevant; Schwelle OPEN.
- **Evidence appetite:** weitere Textzeugen/Editionen/Apparat/Facsimile.
- **Allowed:** textkritisch gestufte Aussagen aus verifizierter Editionsbasis.
- **Forbidden:** editorische Rekonstruktion als sicherer Quellwortlaut.
- **Uncertainty:** Variante/Lesung/Ergänzung explizit.
- **Counterevidence:** anderer Textzeuge/Edition/Apparat.
- **Failure modes:** editorial laundering, variant loss, regest conflation.
- **Proper application:** Leser erkennt historisches Textmaterial vs editorische Intervention.
- **Interfaces:** P6a, P11, P5, P2, P7.
- **Handoff:** Zeichenlesung → P11; diplomatische Genese → P6a; bibliographische Edition → P2.
- **Return:** Textstatus, Varianten, editorial layers, confidence.
- **Incommensurabilities:** editorische vs diplomatische Kategorien.
- **Automation/AI:** Variantendarstellung unterstützbar; Textkonstitution/Fachurteil nicht automatisch.
- **External validation:** OPEN.
- **Open:** SOTA, Playbook, Profilgrenze mit P6a.
- **Non-conclusion:** keine finale separate Kompetenzdatei impliziert.

### P7 – Archivistik / Provenienz / Registraturkunde
- **Problem / Claim Types:** Provenienz, Registratur-/Bestandsbildung, Fonds/Serie, Kassation/Verlust, Umlagerung, Signaturgeschichte.
- **Leading when:** Überlieferungszusammenhang/Archivstruktur die Auffindbarkeit oder Aussage über Abwesenheit trägt.
- **Controlling when:** heutiger Bestand als direkte Abbildung der Vergangenheit gelesen wird.
- **Not responsible for:** historische Sachinterpretation allein.
- **Knowledge base:** Provenienz-/Registratur-/Bestandsbildung; konkrete Fach-SOTA OPEN.
- **Core principles:** Archiv ≠ Vergangenheit; heutiger Bestand ≠ ursprüngliche Registratur; `not found ≠ never existed`.
- **Object model:** Provenienzbildner, Registratur, Bestand/Fonds, Serie, Einheit, Signatur, Verlust/Kassation/Umlagerung.
- **Material model:** Archivgut, Findmittel, Kataloge, Editions-/Alt-Signaturen.
- **Formation:** Verwaltungs-/Registraturbildung plus spätere Archivierung/Ordnung/Verlust.
- **Observable:** vorhandene Bestands-/Findmittelstruktur, Provenienzangaben, Signaturgeschichte soweit dokumentiert.
- **Non-observable:** vollständige historische Registratur bei Verlust/Kassation.
- **Detectability:** Findmittel-/Bestandsgrenzen zentral.
- **Operations:** Provenienz/Bestand/Serie/Signatur/Verlustgeschichte rekonstruieren; Suchraum bestimmen.
- **Minimum evidence:** Findmittel/Bestandsbeschreibung/Archivmetadaten; Schwelle OPEN.
- **Evidence appetite:** Fonds/Serien/Findbücher/Alt-Signaturen/Parallelbestände.
- **Allowed:** Aussagen über nachweisbare Bestands-/Überlieferungslage.
- **Forbidden:** nicht gefunden=nie existiert; heutige Signatur=historische Ablage.
- **Uncertainty:** `not yet verified`, `unresolved`.
- **Counterevidence:** Altfindbuch, Parallelbestand, Editionsnachweis, Verlusthinweis.
- **Failure modes:** archival absence fallacy, provenance flattening, shelfmark laundering.
- **Proper application:** Search Boundary und Bestandsgeschichte werden bei negativen Ergebnissen sichtbar.
- **Interfaces:** P2, P1, P6a/b, P13.
- **Handoff:** inhaltliche Sachdeutung → P8; Dokumentstatus → P6.
- **Return:** Provenienz-/Bestandskontext, Search Boundary, unresolved/loss risk.
- **Incommensurabilities:** historische Registratur vs heutige Archivtektonik.
- **Automation/AI:** Katalog-/Signaturabgleich unterstützbar; Provenienz-/Verlustinterpretation Fachurteil.
- **External validation:** OPEN.
- **Open:** SOTA/regionale Archivtraditionen.
- **Non-conclusion:** fehlender Archivtreffer beweist keine historische Abwesenheit.

### P8 – sachhistorische Domain-Expertise
- **Problem / Claim Types:** institutionelle, rechtliche, soziale, kirchliche, territoriale, ökonomische historische Relationen.
- **Leading when:** Claim über historische Sachverhältnisse/Institutionen/Relationen geht.
- **Controlling when:** andere Profile Begriffe/Identitäten liefern, deren historische Bedeutung nur Sachdomäne klären kann.
- **Not responsible for:** Quellen-/Text-/Archivstatus allein.
- **Knowledge base:** problemabhängige Subdisziplin; „Mediävistik“ als alleinige Superkompetenz zu grob.
- **Core principles:** `Besitz ≠ Grundherrschaft ≠ Gericht ≠ Lehen ≠ Vogtei ≠ Patronat ≠ Abgabe ≠ Amt ≠ Territorialhoheit`; Beziehungen sind zeitlich/institutionell typisiert.
- **Object model:** Akteure, Institutionen, Rechte, Pflichten, Besitz-/Herrschafts-/Amtsrelationen, Zeit/Geltung.
- **Material model:** je Subdomäne verschieden; keine Universal-Evidenzlogik.
- **Formation:** je Institution/Quellentyp **OPEN / #60**.
- **Observable:** explizite Rechte/Rollen/Handlungen/Beziehungen; weitergehende Struktur nur mit fachgerechter Evidenz.
- **Non-observable:** umfassende Territorial-/Herrschaftsstruktur aus Einzelnachweis ohne Zusatzbelege.
- **Detectability:** quellen-/institutionenspezifisch OPEN.
- **Operations:** Relationen typisieren, zeitlich/räumlich/institutionell einordnen, konkurrierende Modelle prüfen.
- **Minimum evidence:** relation-specific; genaue Schwellen OPEN.
- **Evidence appetite:** problemabhängige Domain-Quellen, Vergleichs-/Forschungsliteratur; Profil-spezifisch OPEN.
- **Allowed:** eng evidenzgebundene Relation/Statusaussagen.
- **Forbidden:** relationale Gleichsetzungen; spätere Territorialität rückprojizieren.
- **Uncertainty:** zeitliche/terminologische Geltung unresolved zulässig.
- **Counterevidence:** abweichende Rechts-/Besitz-/Amtsbelege, andere zeitliche Phase.
- **Failure modes:** relation collapse, anachronistic state model, domain overreach.
- **Proper application:** Claim benennt genaue Relation und Zeit statt vager „Herrschaft“.
- **Interfaces:** P1/P3/P5/P9/P10/P12/P14.
- **Handoff:** Name/Raum/Material/Textstatus an Spezialprofile.
- **Return:** institutionell/historisch typisierte Konstellation + Grenzen.
- **Incommensurabilities:** gleiche Wörter können verschiedene rechtlich-institutionelle Relationen meinen.
- **Automation/AI:** Relationsextraktion heuristisch; fachliche Typisierung/Judgement menschlich/qualifiziert.
- **External validation:** domänenspezifisch OPEN.
- **Open:** notwendige Unterprofile/Splits, SOTA, Evidence thresholds.
- **Non-conclusion:** kein einheitliches „Domain History“-Method Profile bewiesen.

### P9 – historische Geographie / Kartenkritik
- **Problem / Claim Types:** historische Räume, Grenzen, Ortsrelationen, räumliche Rekonstruktionen/Karten.
- **Leading when:** räumliche Kompatibilität/Abgrenzung den Claim trägt.
- **Controlling when:** moderne Verwaltungsflächen oder Kartenrekonstruktionen auf historische Räume projiziert werden.
- **Not responsible for:** Namensidentität allein (P10), institutionelle Rechtsbeziehung allein (P8).
- **Knowledge base:** historische Raumkonzepte/Kartographie; konkrete SOTA OPEN.
- **Core principles:** historische Räume ≠ moderne administrative Flächen; Grenzen können linear, zonal, umstritten, funktional, saisonal, punktuell belegt sein.
- **Object model:** Ort, Raum, Grenze, Zone, Funktion, Punktbeleg; Status `directly attested | reconstructed | interpolated | candidate | unresolved`.
- **Material model:** Karten, Textbelege, Orts-/Grenzangaben, spätere Rekonstruktionen.
- **Formation:** Karten sind Forschungs-/Darstellungsprodukte mit eigener Auswahl/Generalisation.
- **Observable:** belegte Punkte/Relationen/zeitgebundene Raumangaben.
- **Non-observable:** präzise geschlossene Grenzlinie aus punktuellen Belegen.
- **Detectability:** Quellen-/Kartenauflösung begrenzt Genauigkeit.
- **Operations:** räumlich-chronologische Kompatibilität; Kartenkritik; Status der Rekonstruktion kennzeichnen.
- **Minimum evidence:** claimabhängig; direkte vs rekonstruierte Evidence unterscheiden.
- **Evidence appetite:** weitere zeitnahe Raum-/Grenz-/Ortsbelege, Kartenprovenienz.
- **Allowed:** gestufte räumliche Kompatibilitäts-/Rekonstruktionsaussage.
- **Forbidden:** Karte epistemisch präziser als Evidenz; moderne Grenze rückprojizieren.
- **Uncertainty:** candidate/interpolated/unresolved.
- **Counterevidence:** widersprechende Orts-/Grenzbelege, andere Zeitlage.
- **Failure modes:** cartographic reification, boundary overprecision, modern-container bias.
- **Proper application:** räumliche Aussage trägt Status/Zeitraum/Belegart.
- **Interfaces:** P10, P8, P12, P13, P14.
- **Handoff:** Namensidentität → P10; Institutionen → P8; Materialbefund → P12.
- **Return:** räumliche/chronologische Kompatibilität + Rekonstruktionsstatus.
- **Incommensurabilities:** textuelle Raumbegriffe vs kartographische Geometrie.
- **Automation/AI:** GIS/Mapping kann darstellen, nicht Evidenzsicherheit erhöhen.
- **External validation:** OPEN.
- **Open:** SOTA, Methoden-/Kartographieprofile, regionale Traditionsfragen.
- **Non-conclusion:** keine historische Grenzgeometrie ohne passende Evidenz.

### P10 – Onomastik / Toponymie
- **Problem / Claim Types:** historische Namensformen, Orts-/Personenidentität, Homonyme, Namensentwicklung.
- **Leading when:** Identifikation eines Namens/Ortes/Benannten den Claim trägt.
- **Controlling when:** Ähnlichkeit oder moderne Normalform als Identität verwendet wird.
- **Not responsible for:** räumliche/Institutionen-Kompatibilität allein.
- **Knowledge base:** Namensformen, Chronologie, Raum, institutioneller Kontext, Belegserien; Fach-SOTA OPEN.
- **Core principles:** Namensähnlichkeit ≠ Identität; Form + Chronologie + Raum + institutioneller Kontext + Belegserie + konkurrierende Homonyme.
- **Object model:** attested form, normalized form, candidate identity, homonym; `confirmed | candidate | competing | unresolved | rejected`.
- **Material model:** historische Namensbelege/Editionen/Karten/Register.
- **Formation:** Schreib-/Sprach-/Überlieferungsvarianten; Details OPEN.
- **Observable:** konkrete belegte Formen/Datierungen/Kontexte.
- **Non-observable:** eindeutige Identität aus einer isolierten Form.
- **Detectability:** Belegserien/Varianten nötig.
- **Operations:** Kandidaten bilden, Varianten/Chronologie/Raum/Kontext vergleichen, Homonyme ausschließen.
- **Minimum evidence:** mehrere kompatible Dimensionen; exakte Schwelle OPEN.
- **Evidence appetite:** weitere Namensbelege, Varianten, Orts-/Institutionskontexte.
- **Allowed:** gestufte Identitätskandidaten.
- **Forbidden:** similarity→identity; moderne Namensform=historische Identität.
- **Uncertainty:** candidate/competing/unresolved.
- **Counterevidence:** inkompatible Chronologie/Raum/Institution, alternatives Homonym.
- **Failure modes:** name conflation, normalization bias, false certainty.
- **Proper application:** mehrere Kandidaten können offen bleiben; Ausschlussgründe sichtbar.
- **Interfaces:** P5, P9, P8, P13.
- **Handoff:** Philologie liefert Lesung/Varianten; Geographie Kompatibilität; Domain History Institution.
- **Return:** Kandidaten/Ausschlüsse/confidence/unresolved.
- **Incommensurabilities:** sprachliche Formähnlichkeit vs historische Identität.
- **Automation/AI:** fuzzy matching heuristisch; Identitätsentscheidung fachlich.
- **External validation:** OPEN.
- **Open:** SOTA/Methodenliteratur/regionale Namenskunde.
- **Non-conclusion:** kein auto-merge von Entities.

### P11 – Paläographie / Kodikologie / materielle Textanalyse
- **Problem / Claim Types:** Schrift, Abbreviaturen, Hände, Material, Layout, Wasserzeichen/Schichten, Nachträge/Rasuren/Marginalien.
- **Leading when:** Zeichenlesung oder materielle Textschicht Claim trägt.
- **Controlling when:** OCR/Transkription als Originalbild behandelt wird.
- **Not responsible for:** historische Semantik nach sicherer Lesung (P5), diplomatische Funktion allein (P6a).
- **Knowledge base:** historische Schriften, Abbreviaturen, Hands, Materialität; SOTA OPEN.
- **Core principles:** `OCR ≠ transcription ≠ image`; unsichere Zeichen/Handwechsel sichtbar.
- **Object model:** Zeichen, Abbreviatur, Hand, Lage/Material, Layout, Ergänzung/Schicht.
- **Material model:** Original-/Bildrepräsentationen, Transkriptionen, OCR/HTR-Derivate.
- **Formation:** physische Herstellung und spätere Einträge/Schichten.
- **Observable:** visuelle/materiale Merkmale bei geeigneter Reproduktion.
- **Non-observable:** sichere Lesung aus schlechtem OCR ohne Bild.
- **Detectability:** Bildqualität/Materialzugang begrenzt.
- **Operations:** Zeichen-/Hand-/Material-/Layeranalyse; uncertain readings markieren.
- **Minimum evidence:** geeignete Bild-/Materialrepräsentation; exakte Schwelle OPEN.
- **Evidence appetite:** bessere Images, Vergleichshände, Material-/Wasserzeichenvergleich, wenn relevant.
- **Allowed:** gestufte Lesungs-/Schichtaussage.
- **Forbidden:** OCR output als historische Textgestalt; unsichere Zeichen normalisieren.
- **Uncertainty:** uncertain sign/reading explizit.
- **Counterevidence:** bessere Aufnahme/Parallelstelle/andere Handanalyse.
- **Failure modes:** OCR laundering, material layer loss, false reading certainty.
- **Proper application:** Bild/Transkription/OCR getrennt, unsichere Zeichen erhalten.
- **Interfaces:** P5, P6a/b, P2.
- **Handoff:** Lesung→P5; diplomatische Funktion→P6a; edition layer→P6b.
- **Return:** mögliche Lesung(en), Material-/Handbefund, uncertainty.
- **Incommensurabilities:** visuelle Evidenz vs normalisierter Text.
- **Automation/AI:** OCR/HTR/spezialisierte Verfahren Assistenz; fachliche Lesung/Materialurteil bleibt Kontrolle.
- **External validation:** OPEN.
- **Open:** SOTA, Bildqualitäts-/Validationstandards.
- **Non-conclusion:** kein OCR als Evidenzersatz.

### P12 – Archäologie / materielle Cross-Evidence
- **Problem / Claim Types:** materielle Chronologie, Siedlungs-/Nutzungsnachweis, Stratigraphie/Fundkontext, Verhältnis Schrift↔Material.
- **Leading when:** materielle Evidenz historische Entstehung/Nutzung/Chronologie trägt.
- **Controlling when:** `Ersterwähnung = Entstehung` oder `kein Fund = Nichtvorhandensein` behauptet wird.
- **Not responsible for:** Text-/Urkundenstatus allein.
- **Knowledge base:** Stratigraphie, Fundkontext, Typologie/Datierung, Taphonomie; konkrete SOTA OPEN.
- **Core principles:** `Ersterwähnung ≠ Entstehung`; `kein Fund ≠ Nichtvorhandensein`; Preservation/Investigation Conditions.
- **Object model:** Fund, Kontext, Stratigraphie, Datierung, Nutzungs-/Siedlungsphase, negative investigation result.
- **Material model:** materielle Befunde als eigenständige Evidenzlinie.
- **Formation:** materielle Entstehungs-/Ablagerungs-/Erhaltungsprozesse.
- **Observable:** untersuchte materielle Befunde/Schichten.
- **Non-observable:** nicht erhaltene/nicht untersuchte Materialität.
- **Detectability:** Taphonomie und Untersuchungsintensität zentral.
- **Operations:** materielle Chronologie/Context prüfen, getrennt von schriftlicher Evidence; Cross-Evidence erst danach.
- **Minimum evidence:** fachgerecht dokumentierter Fund-/Kontext; Schwelle OPEN.
- **Evidence appetite:** weitere Befunde/Datierungen/Untersuchungsgrenzen.
- **Allowed:** materielle Evidenz kann schriftliche Hypothese stützen/begrenzen/widerlegen.
- **Forbidden:** first mention=foundation; no find=absence.
- **Uncertainty:** dating range/absence unresolved.
- **Counterevidence:** abweichende Datierung/Stratigraphie, unzureichende Survey Boundary.
- **Failure modes:** textual primacy, archaeological silence overclaim, evidence-line fusion.
- **Proper application:** schriftliche und materielle Linien zunächst getrennt, dann explizit integriert.
- **Interfaces:** P8, P9, P14, P13.
- **Handoff:** institutionelle Interpretation→P8; Raum→P9.
- **Return:** materielle Evidence + Datierungs-/Detectability-Grenzen.
- **Incommensurabilities:** Textdatum vs materielle Datierungsrange.
- **Automation/AI:** Mess-/GIS-/Klassifikationssupport möglich; archäologisches Urteil fachlich.
- **External validation:** OPEN.
- **Open:** SOTA/profile boundaries.
- **Non-conclusion:** keine materielle Evidenz aus fehlender Evidenz.

### P13 – historische Heuristik / Information Retrieval
- **Problem / Claim Types:** wo/wie suchen, wenn Hypothese wahr wäre; Suchvokabular, Quellenserien, Citation Chaining, negative search results.
- **Leading when:** Evidence erst gefunden/abgegrenzt werden muss.
- **Controlling when:** Trefferzahl oder fehlender Treffer als Beweis verwendet wird.
- **Not responsible for:** Bewertung der gefundenen Evidence als historischen Claim allein.
- **Knowledge base:** historische Schreibvarianten, Fach-/Archiv-/Bibliographiesuche, Retrievalstrategien; konkrete SOTA OPEN.
- **Core principles:** `Treffer ≠ Evidenz`; `kein Treffer ≠ Abwesenheit`; Evidence Appetite domänenspezifisch.
- **Object model:** query, variant, corpus/catalogue/archive, result, search boundary, citation path.
- **Material model:** Editionen, Regesten, Archive, Bibliographien, Kataloge, Volltexte.
- **Formation:** Index-/Katalog-/OCR-/Metadatenprozesse beeinflussen Findbarkeit.
- **Observable:** Treffer in definierten Suchräumen.
- **Non-observable:** Gesamtbestand außerhalb Search Boundary.
- **Detectability:** Retrieval-/OCR-/Katalogcoverage zentral.
- **Operations:** Suchräume/vocabulary/variants/citation chaining; boundaries dokumentieren.
- **Minimum evidence:** für Negativbefund dokumentierte Search Boundary; für positive Evidence erst Domain-Review.
- **Evidence appetite:** durch aktive Domäne bestimmt.
- **Allowed:** Discovery-/Search claims; keine direkte historische Promotion.
- **Forbidden:** hit=evidence; no hit=absence/completeness.
- **Uncertainty:** incomplete retrieval sichtbar.
- **Counterevidence:** alternative Schreibweise/Katalog/Bestand/OCR.
- **Failure modes:** retrieval blind spot, false completeness, snippet-as-evidence.
- **Proper application:** Search strategy + boundaries reproduzierbar.
- **Interfaces:** alle Domänen, besonders P2/P7/P10/P14.
- **Handoff:** Treffer an zuständige Fachdomäne; negative search result mit boundary.
- **Return:** candidate sources/findspots + search boundary, keine Truth.
- **Incommensurabilities:** Retrieval relevance vs evidential relevance.
- **Automation/AI:** Such-/Fuzzy-/Expansion-Unterstützung; Evidence judgement extern.
- **External validation:** OPEN.
- **Open:** SOTA/benchmarking per historischem Retrieval.
- **Non-conclusion:** Retrieval ist keine Evidenzklasse.

### P14 – historische Epistemologie / Inferenzkontrolle
- **Problem / Claim Types:** Evidenzabhängigkeit, Triangulation, Kausalität, Abduktion, negative evidence, Unsicherheit, Falsifikation, Gesamtsynthese.
- **Leading when:** mehrere Evidence-Linien/Methoden zu einer Gesamtinferenz integriert werden.
- **Controlling when:** confidence/independence/alternatives/Falsifier unsichtbar werden.
- **Not responsible for:** fachdomänenspezifische Evidence selbst erzeugen.
- **Knowledge base:** historische Inferenz-/Evidenzlogik; konkrete Fach-SOTA OPEN.
- **Core principles:** independence, triangulation, negative evidence, uncertainty, falsification; Widerspruch darf bleiben.
- **Object model:** `Claim → Evidence → Method → Inference → Scope → Confidence/uncertainty → competing explanation → falsifier`.
- **Material model:** Evidence-Linien aus mehreren Domänen, mit Abhängigkeiten.
- **Formation:** Synthesen sind eigene Inferenzprodukte, keine neue Evidence.
- **Observable:** dokumentierte Evidence/Method/Inference relations.
- **Non-observable:** Wahrheit aus Konsens mehrerer abhängiger AI-/Publikationsaussagen.
- **Detectability:** Independence-/Search-/Method boundaries.
- **Operations:** Abhängigkeit prüfen; Alternativen; confidence; falsifier; unresolved zulassen.
- **Minimum evidence:** claim-proportionate und domänenspezifisch; Schwelle OPEN.
- **Evidence appetite:** discriminating evidence/counterevidence je competing explanation.
- **Allowed:** gestufte Synthese mit expliziter Unsicherheit.
- **Forbidden:** triangulation ohne independence; AI consensus as evidence; unresolved erzwingen.
- **Uncertainty:** zentraler Output.
- **Counterevidence:** ausdrücklich gesucht/integriert.
- **Failure modes:** false triangulation, confidence laundering, synthesis overclaim.
- **Proper application:** Gesamtclaim bleibt auf Evidence/Method/Assumptions/Falsifier zurückführbar.
- **Interfaces:** alle Profile; keine Master-Domain.
- **Handoff:** spezifische Evidence-Frage an führende Domäne; erhält deren bounded return.
- **Return:** integrierte statusklare Inferenz, ggf. competing/unresolved.
- **Incommensurabilities:** unterschiedliche Evidence-Arten werden nicht in eine Scheinscore-Metrik gepresst.
- **Automation/AI:** Trace-/dependency checks unterstützbar; epistemisches Gesamturteil nicht automatisch.
- **External validation:** consequential/publication-level trigger OPEN/#60/#45.
- **Open:** SOTA/Validation/Review independence.
- **Non-conclusion:** kein epistemischer Super-Reviewer über Fachdomänen.

### P15 – Expertise Routing / Research Coordination
- **Problem / Claim Types:** welche Kompetenz führt/kontrolliert; bounded decomposition; fachliche Übergaben; Konflikte/Evidenzlücken sichtbar halten.
- **Leading when:** Problem mehrere Fachdomänen berührt oder Zuständigkeit geklärt werden muss.
- **Controlling when:** generische Assistenz versucht, Fachfragen selbst zu entscheiden.
- **Not responsible for:** Fachstandards überschreiben, historische Wahrheit oder Method Truth selbst festlegen.
- **Knowledge base:** Kompetenzgrenzen, Handoff-Logik, Authority/Quality Frames; kein eigenes historisches Faktenprivileg.
- **Core principles:** keine Super-Wissenschaft; problem-/material-/claimabhängiges Routing; professionelle Handoffs statt „consult X“.
- **Object model:** observation, leading/controlling domain, bounded question, context/evidence, uncertainty, requested return, status.
- **Material model:** Arbeitspakete/Handoffs, nicht eigenständige historische Evidence.
- **Formation:** Koordinationsoutput entsteht aus Problemstruktur + bekannten Kompetenzgrenzen.
- **Observable:** welche Frage/Evidence/Authority an wen übergeben wird und was zurückkommt.
- **Non-observable:** fachliche Antwort ohne Fachdomänenarbeit.
- **Detectability:** fehlende Method Truth/Kompetenzgrenzen müssen als OPEN geroutet werden.
- **Operations:** Problem zerlegen; leading/controlling erkennen; bounded questions formulieren; returns integrieren ohne Flattening.
- **Minimum evidence:** genügend Kontext für richtige Zuständigkeit; exakte Regeln später #60.
- **Evidence appetite:** keine eigene; übernimmt Anforderungen der aktivierten Fachdomäne.
- **Allowed:** Routing-/Handoff-/Statusentscheidung innerhalb gebundener Authority.
- **Forbidden:** fachliche Kontroverse glätten; Kompetenz erzeugen; Authority aus Routing ableiten.
- **Uncertainty:** `unresolved / needs-specialist / not-assessable` legitim.
- **Counterevidence:** Reviewer zeigt falsche/fehlende Domänenaktivierung oder falsche Handoff-Frage.
- **Failure modes:** master-domain, generic synthesis, authority laundering, fixed pipeline.
- **Proper application:** passende Domäne erhält kleine prüfbare Frage; Rückgabe bleibt mit Unsicherheit/Source Role erhalten.
- **Interfaces:** alle Profile, #45/#60/Work Context.
- **Handoff:** selbst ist Handoff-Organisator; bei fehlender Method Truth an #60, bei echter Authority an Owner/#44.
- **Return:** confirmed/candidate/competing/unresolved integration without domain override.
- **Incommensurabilities:** unterschiedliche Fachsprachen/Evidence-Standards bleiben sichtbar.
- **Automation/AI:** Routinghilfe möglich; epistemische Authority extern.
- **External validation:** fachdomänenspezifisch; Routing selbst später evaluiert.
- **Open:** SOTA zu Expertise Routing/Multi-method composition; #60 research questions.
- **Non-conclusion:** kein Agentenorchestrator oder autonome Prioritätsinstanz.

## E4. Interface Oracle

**Pflichtstruktur je materially relevantem Handoff:**

`triggering observation → outbound domain → bounded question → evidence/context passed → terminology passed → preserved uncertainty → requested evidence/assessment → receiver may confirm/refute/limit → incommensurabilities → return contract → downstream status`

**Referenzbeispiel, ausdrücklich nicht als starre Pipeline:**

1. **Philologie** liefert mögliche Lesungen/Varianten/semantische Grenzen.
2. **Onomastik** erhält eine bounded Identitätsfrage; liefert Kandidaten, Ausschlüsse, confidence, unresolved.
3. **Historische Geographie** prüft räumlich-/chronologische Kompatibilität; liefert compatibility/limits, keine Namenswahrheit.
4. **Sachhistorie** prüft institutionelle/historische Konstellation; liefert relationale Kontextgrenzen.
5. **Epistemische Integration** führt nur die returns samt Evidence/Method/Uncertainty zu `confirmed | candidate | competing | unresolved` zusammen.

**FAIL**, wenn eine Übergabe nur „consult X“ lautet oder wenn eine empfangende Domäne rückwirkend die Source Role des Inputs verändert.

## E5. Activation Oracle

### Initiale Aufsatzerschließung – typischer Leading/Controlling-Satz
- Quellenkritik;
- Historiographie;
- Hermeneutik / Argumentationsanalyse;
- relevante sachhistorische Domain;
- historische Geographie **nur**, wenn der Claim räumlich ist.

### Claim-driven Vertiefung
- Urkundenstatus / Editionsproblem → P6a/P6b;
- Lesung → P11/P5;
- Name/Identität → P10;
- Überlieferungsweg / Bestandsfrage → P7;
- Siedlungs-/Materialchronologie → P12;
- Raum/Grenze → P9;
- Gesamtinferenz/Unabhängigkeit/Negativbefund → P14.

### Harte Anti-Pipeline-Regel
> **Erschließen heißt zunächst noch nicht, jede Urkunde nachzuprüfen.**

Erste Erschließung rekonstruiert fachkundig Erkenntnisapparat, Claims, Quellenrouter, Argumente, Begriffe, Evidenzbedarf und offene Verifikationshaken. Tiefe Primärquellenprüfung wird claim-getrieben aktiviert.

---

# F. Corrected Open-State / Closure Contract

| ID | Exact meaning / relation to Intent | Source role + case example | Owner / Closure authority | Closure evidence | Non-closure | Expected after successful Preservation | Software/Human |
|---|---|---|---|---|---|---|---|
| OS-01 Persistence State | Ist der materiale owner-bestätigte Analysezustand außerhalb dieses Chats dauerhaft und restartbar externalisiert? | Project-continuity state; hier: Source Lock + Baseline + Planning/Assurance fehlen derzeit im Repo | Preservation Work Owner operational; Repo-Governance controls | P0/Execution merged, canonical pointers valid, W7 restart PASS | Chatdatei, offene PR, lokaler Draft allein | **CLOSED** | technisch/operational prüfbar; Merge/Owner-Freigabe menschlich |
| OS-02 Representation Fidelity State | Entspricht die persistierte Repräsentation der bestätigten Bedeutung vollständig? | Semantic representation state; hier: bisheriges #148 framing wurde vom Owner als unzureichend korrigiert | Preservation Owner; semantic source authority = owner-confirmed input | W1 complete inventory + W3 full coverage + W5 adversarial PASS + keine S2/S3 offen | hübscher Text, formale Vollständigkeit, Self-review ohne Source comparison | **CLOSED / VERIFIED FOR PRESERVATION** | AI review möglich; Source-Ambiguität Human |
| OS-03 Erkenntnislücke / fachlich-epistemische offene Frage | Was ist über tatsächliche Fachmethodik, Profilgrenzen, Evidenz-/Inferenzlogik noch nicht hinreichend erkannt/verstanden, um Method Truth zu tragen? Intent-relativ, nicht generischer Gap-Container | Human/project epistemic question; z. B. „welche fachwissenschaftliche Operationalisierung trägt P6a/P6b wirklich?“ | #60 / führende Fachdomäne; ggf. qualifizierte Fachvalidierung | SOTA-/Methodenevidenz, Live-/Counterexample-Tests, nachvollziehbare fachliche Inferenz, ggf. externe Review | Dokumentexistenz, Owner-Bestätigung, AI-Plausibilität, grüner Validator | **OPEN, sichtbar gemacht** | Software kann Evidence/Status anzeigen, Erkenntnis selbst nicht als Boolean schließen; fachliche/Human Beurteilung nötig |
| OS-04 Profile-Boundary Uncertainty | Sind heutige Analyseprofile fachlich richtig geschnitten (`retain|split|merge|reframe`)? | method-scoping question; P6 Diplomatik/Edition explizit offen | #22 inventory + #60 fachliche SOTA-Disposition | vergleichende Fachmethoden-/Fall-Evidence, explizite Disposition | Dateistruktur, Labelzählung 15/16, Modellpräferenz | **OPEN** | nicht rein deterministisch |
| OS-05 Domain-SOTA Research Debt | Welche Methodenliteratur, Standards, Kontroversen, regionale Traditionen fehlen? | research debt, nicht „Gap“-Ontologie | #60 unter #45 | qualifizierte SOTA-Recherche mit Source Identity/Fundstellen, Sättigung/Boundaries | Modellwissen, bloße Trefferliste, Chat-Zusammenfassung | **OPEN** | Research+fachliches Urteil |
| OS-06 Method-Validation Debt | Welche positiven, Overclaim-, evidence-starved und ggf. externen Tests fehlen, bevor working/validated method? | validation state | #60, #45; external specialist where required | Domain Method Contract promotion evidence | eloquentes Profil, ein einzelner Case, AI review allein | **OPEN** | teils testbar; Promotion fachlich/authority-bound |
| OS-07 Human Understanding / Judgement Need | Kann der relevante Human das Problem/Evidence/Unsicherheit hinreichend verstehen/beurteilen? Nicht identisch mit Erkenntnislücke oder Systemdefekt. | Human cognitive state; Ergebnis kann Informationsraum bereitstellen | Human/Owner bzw. zuständige Stakeholder Authority | echte Human-Validation, dass Beurteilungs-/Verständnislast hinreichend reduziert ist | Artefakt existiert; Modell sagt „verständlich“; CI PASS | **nicht automatisch durch Preservation geschlossen** | Software darf Bedingungen schaffen, nicht cognition behaupten |
| OS-08 System / Capability Deficit | Fehlt ein beobachtbares Systemverhalten, das zur Erfüllung des Intents benötigt wird? Nur wenn real belegt. | product/system state; dieser Preservation-Run begründet **keinen allgemeinen Defizit-Claim** | zuständige Requirement-/Technical Owners (#42/#48/#59 in Histo-Orla) | demonstriertes Verhalten gegen accepted acceptance/verification + ggf. Owner feedback | Design/Contract/Code existence allein | **N/A unless separately evidenced** | technisch verifizierbar, Intended outcome/acceptance ggf. Human |

## F1. Relationsschutz

- Intent, Erkenntnislücke, Pain, Goal, Need, Requirement, Constraint, Capability und Result dürfen relationiert werden, sind aber **nicht austauschbar**.
- `Gap` ist **keine** akzeptierte Universalontologie.
- `Information Space` ist höchstens eine Kandidatenfigur dafür, wie Resultate Human-Erkenntnis ermöglichen können; es ist keine P0-Strukturvorgabe.
- Evidence, Verification Result und Stakeholder Validation bleiben getrennt.
- Human Validation beweist weder technische noch fachliche Wahrheit.

---

# I. Independent Review Adversarial Suite

| ID | Injected failure pattern | Expected detector | QC | Severity | Expected verdict |
|---|---|---|---|---|---|
| I-01 | `analysis/scoping` rewritten as „method“ or „best practice“ | status/provenance comparison | 04,14 | S3 | STOP/REVISE before PASS |
| I-02 | PR #147 cited as source of competence meaning | source-role audit | 09 | S3 | STOP-PROVENANCE |
| I-03 | PR #148 treated as definitive current semantic authority because merged | repo/source-role audit | 09,10 | S3 | STOP-PROVENANCE/CONFLICT |
| I-04 | fluent summary loses Detectability/negative-evidence condition | source/inventory coverage | 02,05,15 | S2 | REVISE W2 |
| I-05 | Diplomatik+Textkritik silently collapsed into generic „Dokumentkritik“ | profile-boundary/flattening test | 03,18 | S2 | REVISE |
| I-06 | P6a/P6b presented as final 16-profile taxonomy | boundary status test | 18 | S2 | REVISE |
| I-07 | four layers rendered as mandatory workflow steps | activation test | 07 | S2 | REVISE |
| I-08 | Research Coordination made epistemic final arbiter | authority/domain test | 16 | S3 | STOP-AUTHORITY or REVISE if text-only |
| I-09 | „no result“ becomes historical absence without Search/Detectability Boundary | negative-evidence test | 15 | S2 | REVISE |
| I-10 | multiple dependent publications counted as independent triangulation | dependency test | 15 | S2 | REVISE |
| I-11 | `unresolved` replaced by most plausible candidate | uncertainty test | 08 | S2 | REVISE |
| I-12 | Herrmann example promoted to current historical finding | case/source-role test | 17,09 | S3 | STOP-PROMOTION |
| I-13 | one case observation becomes general Fachregel | case-general test | 17 | S2/S3 | REVISE/STOP-SCOPE |
| I-14 | issue/README duplicates full profiles next to baseline | canonical-home test | 10,11 | S2 | REVISE W6/W4 |
| I-15 | Source Lock described as disciplinary evidence because Owner confirmed it | provenance/epistemic test | 09,04 | S3 | STOP-PROVENANCE |
| I-16 | closed Persistence State described as closing SOTA/Method Validation | false closure test | 08,14 | S3 | STOP-PROMOTION |
| I-17 | Human validation described as proof of technical/domain correctness | Open-State separation test | 08,14 | S2/S3 | REVISE/STOP depending consequence |
| I-18 | interface reduced to „ask Onomastics/Geography“ without question/return | interface oracle | 06 | S2 | REVISE |
| I-19 | normalized term presented as original source wording | source/philology test | 03,05,09 | S2 | REVISE |
| I-20 | source/edition/instance/findspot collapsed into one citation object | source-identity test | 03,09 | S2/S3 | REVISE/STOP if provenance lost |
| I-21 | formal checklist all green but a material INV item has no baseline representation | completeness cross-check | 02,13 | S2 | FAIL; proves formal completeness insufficient |

**W5 PASS condition:** all tests evaluated against the actual package; no S2/S3 finding remains; reviewer explicitly states independence conditions and any limitations.

---

# J. Fresh Restart Oracle

| # | Question | Expected semantic answer / minimum detail | Acceptable uncertainty | Expected canonical source path | Material wrong answer | Failure class / verdict |
|---|---|---|---|---|---|---|
| J-01 | What is current status? | detailed `analysis / competence-scoping / no-promotion` | profile details may still be OPEN | competence-analysis README → baseline | `working-method`, `validated-method` | semantic → STOP |
| J-02 | What is Source Lock? | frozen owner-confirmed workshop synthesis establishing intended project-analysis meaning, not disciplinary truth | authorship mix can be stated | `inputs/owner-confirmed-analysis...` | „primary historical evidence“ | semantic/provenance → STOP |
| J-03 | What are the profiles? | current analysis families, with P6 Diplomatik/Textkritik analytically distinct but final count/boundary unresolved | 15-vs-16 must remain open | baseline Profile section | „final 15“ or „final 16“ | semantic → STOP |
| J-04 | What makes competence operational? | knowledge/object/material models, formation/observability, operations, evidence appetite, inference/QA/failure, leading/controlling, interfaces/validation | fields may be OPEN if source lacked detail | baseline + Assurance meta-oracle | „discipline expertise“ alone | semantic → STOP |
| J-05 | How are profiles activated? | material/question/claim/evidence driven; leading/controlling; no fixed pipeline | case-specific details open | baseline Activation section | A→B→C→D mandatory | semantic → STOP |
| J-06 | What are interfaces? | bounded handoff objects: trigger/question/evidence/uncertainty/requested return/incommensurability | exact receiving method may be OPEN | baseline Interface section | simple „consult X“ | semantic → STOP |
| J-07 | What is source-role rule? | role relational to research question/claim; distinguish source/representation/instance/findspot | exact taxonomy not final Method Truth | baseline Shared Concepts + source protocol | static primary/secondary label | semantic → STOP |
| J-08 | How is uncertainty treated? | candidate/competing/unresolved valid; no forced closure | unresolved expected | baseline QA/Open State | choose most likely | semantic → STOP |
| J-09 | What does #22 own? | competence inventory/boundary analysis | exact future split open | #22 + README | Method Truth | authority → STOP |
| J-10 | What does #60 own? | later SOTA-based operationalization, Method Truth, validation/promotion | none | #60 + methods README | current baseline already Method Truth | authority → STOP |
| J-11 | Role of PR #147? | historical closed-unmerged derivative/prior art | may contain useful comparison | README/provenance | current baseline | provenance → STOP |
| J-12 | Role of PR #148? | merged earlier audit/provenance/reconciliation object, not semantic source of new baseline | remains in history | README/provenance | definitive competence truth | provenance → STOP |
| J-13 | What remains epistemically open? | profile boundaries, Domain SOTA, method literature, thresholds, validation/counterexamples | many fields expected OPEN | Open-State section | „preservation closed method gaps“ | semantic → STOP |
| J-14 | Herrmann role? | case-derived activation/stress examples only; no reactivated findings | exact examples can be absent from restart summary | baseline Case section | current historical research state | provenance → STOP |
| J-15 | Next allowed fachliche work? | profile-/problem-driven SOTA under #60, using real cases and #45; no automatic architecture | priority among profiles may follow #60/current problem | README/next work + #60 | implement agents next | semantic/authority → STOP |
| J-16 | What did Preservation close? | Persistence + Representation Fidelity only | Human understanding may still be open | Open-State + run assurance | Method Truth/SOTA closure | semantic → STOP |
| J-17 | Does initial exploration require checking every charter? | no; first exploration reconstructs claims/method/evidence needs, deep verification claim-driven | consequential claim may trigger deep check | Activation section | „yes, every primary source first“ or „no verification ever needed“ | semantic → STOP |
| J-18 | Can profile depth be reconstructed from labels? | no; baseline preserves per-profile models/limits/interfaces/open fields | exact SOTA absent by design | baseline profile oracle/content | labels sufficient | semantic → STOP |

**Navigation failure** = correct semantics exist, but prescribed entry path does not surface them → `REVISE W6` once.  
**Semantic failure** = fresh reader follows correct paths and reconstructs materially wrong status/meaning → `STOP-ASSURANCE-ESCAPE`.
