# Histo-Orla – Capability Map + Quality Attribute Catalogue v1

**Work Owner:** #41  
**Status:** `completed-synthesis / v1`  
**Inputs:** #28–#40; fachlicher Scope #9/#13–#16/#19/#20; Software-/Allocation-Guardrails #24; Live-Research-Stressfälle #46 (U2) und #47 (U1).  
**Methodik:** Scholarly Requirements Engineering + fachgebundene Quality-Synthese gemäß #45.  
**Leitregel:** Capabilities beschreiben, **was** das Forschungssystem leisten muss. Sie enthalten keine vorweggenommene Technologiearchitektur.

---

## 1. Promotion-Regel

Ein Capability Candidate wird in dieser Baseline nur `validated` oder `working-validated`, wenn mindestens gilt:

1. nachvollziehbarer Need/Pain/Goal aus #28/#29;
2. fachliche Begründung/SOTA aus mindestens einem Strang #31–#39;
3. wissenschaftliche Invariante oder klarer Nutzerwert;
4. Failure-/Risk-Bezug aus #40;
5. prüfbarer Acceptance-/Evaluation-Ansatz;
6. kein bloßes Produkt-/Technologiefeature.

Live-Research-Candidates aus #46/#47 sind zusätzliche Falsifikations-/Stressbefunde. Ein Einzelbeispiel darf keine Architektur erzwingen.

Prioritäten:

- **P0** – wissenschaftlich/operativ fundamental, cross-cutting oder Voraussetzung für andere Capabilities;
- **P1** – zentral für anspruchsvolle historische Analyse, auf P0 aufbauend;
- **P2** – wichtig, aber nach einem belastbaren Kern iterativ vertiefbar.

---

# 2. Capability Map v1

## CAP-01 – Professional Problem Translation & Concept Discovery

**Statement:** Das System kann eine unscharfe Beobachtung in mehrere fachlich plausible Problembegriffe, konkurrierende Gegenstandsmodelle, Terminologieebenen, relevante Quellen-/Recherchelogiken und diskriminierende Folgefragen übersetzen, ohne bloße Synonymie mit fachlicher Gleichheit zu verwechseln.

- **Need/Pain:** N-001, P-001; G-002.
- **Use Cases:** U1–U3; U4 bei archivischer/terminologischer Suche.
- **Leading disciplines:** jeweilige historische Fachdomäne; historische Philologie/Semantik; Knowledge Organization.
- **Controlling disciplines:** Historiographie; Archivistik bei Archivsprache.
- **Scientific invariants:** historischer Quellenbegriff ≠ moderner Analysebegriff ≠ Archivsprache ≠ Suchvariante; konkurrierende Modelle bleiben sichtbar; Geltungsbereiche zeitlich/räumlich/institutionell markierbar.
- **Risks:** RISK-04, -05, -11, -13, -14.
- **Quality attributes:** terminologische Präzision; Concept Coverage; Anachronism Control; False-Equivalence-Schutz; Erklärbarkeit.
- **Acceptance seed:** U2 `Vogtei/Ministerialität/Lehen/Grundherrschaft` darf nicht als Synonymliste ausgegeben werden; U1 Beobachtung `alte Feuchtfläche/Teiche` muss u. a. fachliche und archivische Begriffe sowie konkurrierende Erklärungsmodelle erschließen.
- **SOTA:** C2 (#32), C3 (#33), C4 (#36).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-02 – Expertise Routing & Epistemic Competency Profiles

**Statement:** Das System kann für ein Forschungsproblem die benötigten Fachkompetenzen, kontrollierenden Nachbardisziplinen, Methoden-/Quellenzuständigkeiten und Validierungsgrenzen bestimmen und sichtbar machen.

- **Need/Pain:** N-002, N-003, N-013, N-019; P-007/P-008; G-003/G-009.
- **Use Cases:** U1–U4.
- **Leading disciplines:** Research Strategy/Coordination + jeweils geroutete Fachdomäne.
- **Scientific invariants:** Rollenname ist keine Expertise; Fachdomäne besitzt Methode/Evidenzmaßstab; Coordinator ist keine epistemische Oberinstanz; AI/mehrere AI-Stimmen ≠ unabhängige Fachvalidierung.
- **Risks:** RISK-13, -14, -27.
- **Quality attributes:** Domain Fit; Routing Precision/Recall qualitativ gegen Gold Cases; Regional Fit; Eskalationsklarheit.
- **Acceptance seed:** U1 muss historische Geographie/Umwelt-/Agrargeschichte/Archivistik u. a. aktivieren; U2 muss Diplomatik/Mediävistik/Onomastik aktivieren; falsche alleinige Generalistenroute gilt als Fehler.
- **SOTA:** C3 (#33), C4/C5 (#36/#37).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-03 – Source / Archive / Literature Discovery by Provenance and Historical Function

**Statement:** Das System kann relevante Quellen, Bestände, Serien, Editionen und Literatur nicht nur über moderne Sachbegriffe, sondern aus historischem Verwaltungs-, Provenienz-, Funktions- und Überlieferungskontext erschließen.

- **Need/Pain:** N-004, N-020; P-002/P-006; G-004.
- **Use Cases:** U1–U4, besonders U1/U2.
- **Leading disciplines:** Archivistik/Registraturkunde, Diplomatik, Bibliographie/Informationswissenschaft; regionale Fachdomäne.
- **Scientific invariants:** Provenienzkontext ≠ Pertinenzsuche; Katalog-/Findmittelbefund ≠ gelesene Quelle; negative Archivsuche braucht Search Boundary.
- **Risks:** RISK-01, -04, -11, -12.
- **Quality attributes:** Discovery Recall gegen bekannte Bestände; Provenance Context Completeness; Search-Boundary-Transparenz.
- **Acceptance seed:** Arnshaugk-Teichfrage muss nicht nur Karten, sondern Serien wie Rechnungen/Fischerei/Mühlen/Hutung/Grenzen routen können; ein Findbuchtreffer bleibt Discovery Evidence.
- **SOTA:** C1 (#31), C4 (#36).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-04 – Source Identity, Representation Layer & Inspected-Instance Control

**Statement:** Das System kann bibliographische/archivalische Identität, historische Quelle/Record, Überlieferungsstufe, Edition/Regest, konkrete digitale Instanz und daraus erzeugte Forschungsderivate getrennt identifizieren und verknüpfen.

- **Need/Pain:** N-005, N-015; G-004/G-006/G-008.
- **Use Cases:** U1–U4.
- **Leading disciplines:** Archivistik, Diplomatik, Editionswissenschaft, RDM.
- **Scientific invariants:** Regest ≠ Urkunde; Edition ≠ Original; URL/PID/Signatur ≠ exakte inspizierte Datei; Hash ≠ institutionelle Identität; Nutzer-Dokument braucht stabile bibliographische/archivalische Rückführung.
- **Live stress:** RC-U2-01, RC-U2-08 (#46).
- **Risks:** RISK-01, -02, -16, -17, -30.
- **Quality attributes:** Provenance Fidelity; Identity Unambiguity; Layer Preservation; Restartability.
- **Acceptance seed:** U2 `[Stange]`-Ergänzung darf nicht in historischen Wortlaut zurückgeschrieben werden; ein späterer Bearbeiter kann die verwendete Edition ohne Chat identifizieren.
- **SOTA:** C1 (#31), C6 (#34), C7 (#35).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-05 – Findspot-Preserving Derivative / OCR / HTR Management

**Statement:** Das System kann born-digitalen Text, OCR/HTR, Korrekturen und weitere Derivate so erzeugen/verwalten, dass Parentage, Seite/Folio/Regest/Region und Transformationsstatus erhalten bleiben.

- **Need/Pain:** N-006, N-007; P-003/P-004; G-004/G-006.
- **Use Cases:** U1–U4, besonders U4.
- **Leading disciplines:** OCR/HTR/DH, Paläographie/Edieren je Material, RDM/IR.
- **Scientific invariants:** OCR/HTR ist Derivat, nie Original; raw/corrected/transcribed unterscheidbar; historische Orthographie nicht still modernisieren; Fundstellen-Roundtrip.
- **Risks:** RISK-02, -03, -18.
- **Quality attributes:** Findspot Fidelity; Critical-Token Accuracy; Layout/Region Preservation; Transformation Traceability.
- **Acceptance seed:** Quelle → OCR → Suchhit → Exzerpt → Zitat führt auf dieselbe korrekte Seite/Folio zurück; Eigennamen/Zahlen/Fachtermini werden zusätzlich zu CER/WER geprüft.
- **SOTA:** C7 (#35).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-06 – Historical Retrieval & Reproducible Query Expansion

**Statement:** Das System kann exakte und phrasenbasierte Suche als robuste Baseline ausführen und kontrolliert historische Schreibformen, Namenvarianten, fuzzy/linguistische Verfahren und fachlich begründete Concept Expansion ergänzen; Suchentscheidungen bleiben reproduzierbar.

- **Need/Pain:** N-008; P-005; G-004.
- **Use Cases:** U1–U4.
- **Leading disciplines:** IR/Search Engineering + historische Philologie/Onomastik/Fachdomäne.
- **Scientific invariants:** Search Variant ≠ semantische Identität; Exact Retrieval bleibt erhalten; Semantic Search/RAG nur additive, benchmark-admitted Schicht; Query/Filter/Corpus-Kontext rekonstruierbar.
- **Live stress:** RC-U2-03 (#46).
- **Risks:** RISK-04, -05, -15, -19.
- **Quality attributes:** Recall/Precision; Known-item Recall; Expansion Transparency; Reproducibility; Findspot Grounding.
- **Acceptance seed:** U2 moderne Ortsform plus historische/lateinische/editorische Varianten findet bekannte Belege und protokolliert, welche Variante welchen Treffer erzeugte; semantische Schicht darf Exact-name Recall nicht verschlechtern.
- **SOTA:** C2 (#32), C7 (#35).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-07 – Search Boundary & Corpus-Bounded Negative Findings

**Statement:** Das System kann Suchgrenzen (Corpus/Bestände, Zeitraum, Sprachen/Varianten, Suchfelder, Index-/Zugangsstatus) dokumentieren und Negativbefunde strikt auf diese Boundary begrenzen.

- **Need/Pain:** N-004/N-008/N-014; P-005/P-006.
- **Use Cases:** U1–U4.
- **Leading disciplines:** jeweilige Fachdomäne, Archivistik/IR/Research Integrity.
- **Scientific invariants:** `nicht gefunden` ≠ historische Abwesenheit; keine Completeness-Claims ohne definierte Boundary.
- **Live stress:** RC-U2-05; #47 Karten-/Archiv-Negativbefunde.
- **Risks:** RISK-04, -11; Completeness overclaim aus #40.
- **Quality attributes:** Boundary Completeness; Negative-Claim Calibration; Reproducibility.
- **Acceptance seed:** Ein U2-Negativbefund kann nicht zu `working finding` oder höher promoviert werden, wenn Corpus, Suchformen und Zeitraum fehlen.
- **SOTA:** #45, C1 (#31), C7 (#35).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-08 – Evidence Layering: Observation / Finding / Claim / Interpretation / Synthesis

**Statement:** Das System kann Quellenrepräsentation, editorische Eingriffe, Beobachtung/Befund, Normalisierung/Identifikation, Claim, fachliche Interpretation und transdisziplinäre Synthese getrennt führen und miteinander rückverknüpfen.

- **Need/Pain:** N-005/N-013/N-014; G-006.
- **Use Cases:** U1–U4.
- **Leading disciplines:** Research Integrity + jeweilige Fachdomäne; Diplomatik/Editionswissenschaft für Quellenschichten.
- **Scientific invariants:** spätere Ebene schreibt frühere nicht um; AI-Ausgabe ist keine Evidenzklasse; Source/Findspot bleibt erreichbar.
- **Live stress:** RC-U2-01.
- **Risks:** RISK-01, -14, -16, -23, -25.
- **Quality attributes:** Epistemic Layer Fidelity; Traceability; Non-loss; Challengeability.
- **Acceptance seed:** U2 editorische Ergänzung und Ortsidentifikation bleiben als solche sichtbar; U1 retrospektive Rezessinformation darf nicht als direkter Entstehungsbeleg erscheinen.
- **SOTA:** C1/C6/C8 (#31/#34/#38).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-09 – Source Dependence & Corroboration Reasoning

**Statement:** Das System kann Überlieferungs-/Informationsabhängigkeiten claim-spezifisch dokumentieren und verhindern, dass Kopie, Regest, Edition und daraus abhängige Literatur als unabhängige Mehrfachbestätigung zählen.

- **Need/Pain:** N-009; G-006.
- **Use Cases:** U1–U4.
- **Leading disciplines:** Diplomatik, Text-/Editionskritik, Historiographie, jeweilige Fachdomäne.
- **Scientific invariants:** dokumentierte/vermutete/unklare Abhängigkeit darstellbar; Independence ist claim-spezifisch; Transmission Relation ≠ Historical Relation.
- **Risks:** RISK-06.
- **Quality attributes:** Corroboration Integrity; Dependency Transparency.
- **Acceptance seed:** Urkunde → Regest → Edition → Artikel darf nicht als vier unabhängige Belege gewertet werden.
- **SOTA:** C6 (#34).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-10 – Discrepancy, Contradiction, Uncertainty & Controversy Management

**Statement:** Das System kann abweichende Datierungen, Identifikationen, Perspektiven und Interpretationen als diagnostizierbare Discrepancies bzw. echte unresolved contradictions persistieren, ohne sie automatisch zu harmonisieren.

- **Need/Pain:** N-010/N-014; G-006/G-009.
- **Use Cases:** U1–U4.
- **Leading disciplines:** jeweilige Fachdomäne + Quellenkritik/Research Integrity.
- **Scientific invariants:** Differenz wird nach Zeitstand, Quelle/Überlieferung, Zweck, Institution, Maßstab, Terminologie, Interesse und Abhängigkeit geprüft; unresolved ist legitimer Zustand.
- **Live stress:** RC-U2-06 (`1374/1378`).
- **Risks:** RISK-07, -13, -23.
- **Quality attributes:** Uncertainty Preservation; Controversy Visibility; Non-harmonization.
- **Acceptance seed:** beide U2-Datierungen bleiben samt Provenienz/status sichtbar, bis diskriminierende Evidenz vorliegt.
- **SOTA:** C6 (#34), C8 (#38).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-11 – Contextual Historical Entity Resolution with Candidate/Promotion States

**Statement:** Das System kann Personen-, Orts- und Institutionsidentitäten aus Varianten als Kandidaten erzeugen, kontextuell prüfen und erst nach ausreichender Evidenz promoten; Homonyme und unresolved identities bleiben getrennt.

- **Need/Pain:** N-008/N-012/N-014; U2 real observed.
- **Use Cases:** U1–U4, besonders U2/U3.
- **Leading disciplines:** Onomastik/Toponymie, Prosopographie, jeweilige Fachdomäne; softwareseitige Promotion Controls.
- **Scientific invariants:** String-/Embedding-Ähnlichkeit reicht nicht; Zeit/Raum/Quelle/Herrschaft/Relation/editorische Identifikation sind prüfbare Kontextfaktoren; False Merge schwerer als bounded candidate.
- **Live stress:** RC-U2-02; `Knau Altenburg ≠ automatisch Knau Orla`, Bucha/Plottendorf/Lintbach.
- **Risks:** RISK-08, -05, -16.
- **Quality attributes:** Precision high-weighted; Candidate Transparency; Merge Reversibility/Auditability.
- **Acceptance seed:** bekannte Homonyme werden nicht automatisch vereinigt; unsichere Identitäten bleiben `candidate/unresolved`.
- **SOTA:** C2/C4/C9 (#32/#36/#39).
- **Priority:** P0.
- **Status:** `validated` (durch SOTA + Live-Stress weiter erhärtet).

## CAP-12 – Historical Relation / Witness / Context Retrieval without Proxy Overclaim

**Statement:** Das System kann Zeugenreihen, Mitakteure, wiederkehrende Kontexte und relationale Hinweise auffindbar machen und zwischen dokumentierter historischer Relation, Proxy/Ko-Präsenz und analytischem Zusammenhang unterscheiden.

- **Need/Pain:** N-011/N-013; U2/U3.
- **Use Cases:** U2–U3; sekundär U1 institutionelle Netze.
- **Leading disciplines:** Prosopographie/Netzwerkforschung, Diplomatik, Adels-/Hof-/Sozialgeschichte.
- **Scientific invariants:** gleiche Quelle/Ort/Universität/Hof/Zeugenreihe ≠ automatisch Beziehung/Genealogie; Relationspromotion evidenzbasiert.
- **Live stress:** RC-U2-04; Stange/Knewe.
- **Risks:** RISK-09, -10, -24.
- **Quality attributes:** Relation Precision; Proxy Disclosure; Source-backed Edge Traceability.
- **Acceptance seed:** Stange/Knewe wird als Ko-Präsenz/Context findbar, aber nicht automatisch genealogisch verknüpft.
- **SOTA:** C4/C5 (#36/#37), C6 (#34).
- **Priority:** P1.
- **Status:** `working-validated`.

## CAP-13 – Temporal / Multi-Scale Place and Territory Context

**Statement:** Das System kann Orte, Territorien, Herrschaften und Analyse-Scope zeitabhängig behandeln und den Maßstab nur bei historisch begründetem Relation-/Verwaltungs-/Mobilitäts-/Vergleichstrigger erweitern.

- **Need/Pain:** N-003/N-012; G-005.
- **Use Cases:** U1–U3.
- **Leading disciplines:** Landes-/Territorialgeschichte, historische Geographie, Spatial History; jeweilige Fachdomäne.
- **Scientific invariants:** heutige Grenze ≠ historische Grenze; Region = Anker, nicht Container; Scale Shift ist Forschungsentscheidung; Gazetteer Match = Candidate.
- **Live stress:** #46 Orla/Altenburg/Schleiz/Saalfeld; #47 Grenzraum statt heutiger `Teichplatte`.
- **Risks:** RISK-11, -12, -24.
- **Quality attributes:** Temporal Context Accuracy; Scale-Shift Justification; Context Traceability.
- **Acceptance seed:** U1 darf nicht auf heutige Gemeinde-/Teichplatten-Grenze begrenzt werden, wenn Quellen-/Nutzungs-/Herrschaftsbeziehungen nach Schleiz/Ziegenrück/Saalfeld führen.
- **SOTA:** C4 (#36).
- **Priority:** P1.
- **Status:** `validated`.

## CAP-14 – Historical Situation / Actor Analysis

**Statement:** Das System kann Akteurshandeln zeitgebunden über Position/Rollen, Institutionen, Ressourcen, belegte Relationen, Informationshorizont, mögliche Optionen/Zwänge, beobachtete Handlung und alternative Erklärungen untersuchen, ohne innere Motive zu erfinden.

- **Need/Pain:** N-011/N-014; G-006.
- **Use Cases:** U3, sekundär U2.
- **Leading disciplines:** Adels-/Hof-/Politik-/Sozialgeschichte, Mikrogeschichte/historische Anthropologie; Prosopographie.
- **Scientific invariants:** observed action ≠ stated motive ≠ attributed motive ≠ structural incentive ≠ historian explanation; hindsight control; unresolved motive erlaubt.
- **Risks:** RISK-09/-10/-13.
- **Quality attributes:** Temporal Situation Fidelity; Motive Evidence Fit; Alternative Explanation Coverage.
- **Acceptance seed:** Amt+Konfession+Netzwerk ohne Motivaussage darf nicht als validiertes Motiv promoted werden.
- **SOTA:** C5 (#37).
- **Priority:** P1.
- **Status:** `validated`.

## CAP-15 – Multi-Evidence Chronology & Cross-Disciplinary Comparison

**Statement:** Das System kann für ein historisches Problem unterschiedliche Evidenzachsen (z. B. Schrift, Archäologie, Onomastik, Kartographie, Umwelt-/Geomorphologie, Besitz-/Rechtsbefund) getrennt zeitlich und methodisch führen und anschließend vergleichbar synthetisieren.

- **Need/Pain:** N-013/N-014; G-003/G-006.
- **Use Cases:** U1/U2, auch U3 bei heterogenen Quellentypen.
- **Leading disciplines:** jeweils beteiligte Fachdomänen; Research Coordination nur Integration.
- **Scientific invariants:** Evidenztypen behalten eigene Aussagekraft/Grenzen; keine Masterdefinition; `first mention ≠ foundation`; hydrologische Plausibilität ≠ historischer Beleg.
- **Live stress:** RC-U2-07; #47 direkte Wasserbelege vs. retrospektive Rezess-/LiDAR-Hypothesen.
- **Risks:** RISK-07, -14, -23.
- **Quality attributes:** Evidence-type Non-loss; Comparative Transparency; Inference Fit.
- **Acceptance seed:** U2 Siedlungs-Timeline zeigt getrennt schriftliche Ersterwähnung, archäologische Evidenz und Ortsnamenbeleg; U1 direkte Teichquelle und retrospektiver Befund bleiben getrennt.
- **SOTA:** C4/C6/C8 (#36/#34/#38) plus Domain Standards.
- **Priority:** P1.
- **Status:** `working-validated`.

## CAP-16 – Transdisciplinary Synthesis with Alternative Preservation

**Statement:** Das System kann mehrere fachliche Ergebnisse zusammenführen, ohne disziplinäre Begriffe, Evidenzlogiken, Kontroversen und alternative Erklärungen zu glätten.

- **Need/Pain:** N-013/N-014; G-003/G-006/G-009.
- **Use Cases:** U1–U4.
- **Leading disciplines:** beteiligte Fachdomänen; Research Coordination für strukturierte Integration.
- **Scientific invariants:** Synthese referenziert Teilbefunde; inkommensurable/konkurrierende Perspektiven bleiben sichtbar; Confidence nicht pseudo-präzise vereinheitlichen.
- **Risks:** RISK-13/-14/-23.
- **Quality attributes:** Traceable Synthesis; Alternative Preservation; Domain Non-flattening.
- **Acceptance seed:** Synthese kann erklären, welche Perspektive welche Aussage trägt und wo offene Differenzen bestehen.
- **SOTA:** C3/C6/C8 (#33/#34/#38).
- **Priority:** P1.
- **Status:** `validated`.

## CAP-17 – Human-Readable Research State, Audit & Challenge Navigation

**Statement:** Das System kann denselben kanonischen Research State in verständlichen, abgeleiteten Sichten erschließen und Navigation von Orientierung → Finding → Quelle/Fundstelle → Methode/Kompetenz → Kontroverse/Alternative → Research History ermöglichen.

- **Need/Pain:** N-014/N-015/N-019; G-009/G-010.
- **Use Cases:** U1–U4.
- **Leading disciplines:** Research UX/Human Factors + Fachdomänen + RDM.
- **Scientific invariants:** View ist abgeleitet, keine zweite Wahrheit; Challenge-Fragen `Warum? Quelle? Methode? Alternative? Was fehlt? Was würde widerlegen?`; Vermittlung ≠ Research View; kein Back-write.
- **Risks:** RISK-23/-24/-25/-26/-30.
- **Quality attributes:** Human Readability; Auditability; Challengeability; View-to-State Traceability; Cognitive Proportionality.
- **Acceptance seed:** qualifizierter Reviewer kann eine Antwort ohne Chat bis Evidenz/Methode/Unsicherheit zurückverfolgen; Research Owner sieht zunächst Orientierung statt Vollprotokoll.
- **SOTA:** C8 (#38).
- **Priority:** P0.
- **Status:** `validated`.

## CAP-18 – Consequence-Based Validation, Candidate Review & Promotion

**Statement:** Das System kann Kandidaten, Working Research, consequential Findings und unabhängig fachvalidierte Aussagen unterscheiden und Prüf-/Promotionstiefe nach wissenschaftlicher Konsequenz und Domänenstandard steuern.

- **Need/Pain:** N-019/N-017; G-003/G-006.
- **Use Cases:** U1–U4.
- **Leading disciplines:** jeweilige Fachdomäne + Research Integrity/Quality; deterministische Controls für formale Promotionsregeln.
- **Scientific invariants:** AI ≠ independent expert validated; unresolved darf korrekt bleiben; canonical mutation braucht kontrollierten Pfad; nicht jeder Candidate braucht manuelle Routinefreigabe.
- **Risks:** RISK-08/-13/-16/-27.
- **Quality attributes:** Validation Proportionality; Promotion Integrity; Reviewer Independence Visibility.
- **Acceptance seed:** halluciniertes Entity-/Relation-Candidate kann formale/fachliche Promotionsbedingungen nicht umgehen; L3 darf nicht aus AI-Mehrheitscheck entstehen.
- **SOTA:** C3/C9 (#33/#39), #45.
- **Priority:** P0.
- **Status:** `validated`.

## CAP-19 – Reproducible Research Workflow & Mechanical Automation

**Statement:** Das System kann wiederkehrende mechanische Schritte reproduzierbar automatisieren, Processing-/Query-Kontext protokollieren, Fehler sichtbar machen und Wiederaufnahme ermöglichen, ohne fachliches Judgment still zu automatisieren.

- **Need/Pain:** N-017/N-020; P-009; G-007/G-012.
- **Use Cases:** U1–U4, besonders U4.
- **Leading disciplines:** RSE/Workflow Engineering + fachlicher Owner für Grenzen.
- **Scientific invariants:** deterministic where possible; specialized benchmarkable method before GenAI; automation darf epistemische Promotion nicht implizit übernehmen.
- **Risks:** RISK-18/-19/-26/-27/-28/-29.
- **Quality attributes:** Reproducibility; Idempotency where applicable; Recoverability; Observability; Low Routine Burden.
- **Acceptance seed:** wiederholter Import/OCR/Index-/Search-Run kann Inputs/Version/Result rekonstruieren; Partial Failure ist sichtbar und restartbar.
- **SOTA:** C7/C9 (#35/#39), #24.
- **Priority:** P0.
- **Status:** `validated`.

## CAP-20 – Portable / Restartable / Provider-Independent Canonical Research State

**Statement:** Das System kann den kuratierten Forschungszustand so persistieren/exportieren, dass er ohne Chat und ohne einen bestimmten AI-/Tool-/Cloud-Provider verstanden, wiederhergestellt und weiterbearbeitet werden kann.

- **Need/Pain:** N-015/N-017; G-008/G-011/G-012.
- **Use Cases:** U1–U4.
- **Leading disciplines:** RDM/RSE/Governance.
- **Scientific invariants:** kanonischer State ≠ Provider-/Model-State; offene/erklärbare Exportwege; regenerierbare Indizes/Processor Outputs vom kuratierten State unterscheidbar.
- **Live stress:** RC-U2-08 (bereitgestellte Edition muss ohne Chat identifizierbar bleiben).
- **Risks:** RISK-17/-18/-19/-30.
- **Quality attributes:** Portability; Restartability; Interoperability; Recoverability; Maintainability.
- **Acceptance seed:** AI-/OCR-/Search-Provider kann entfernt/ersetzt werden, ohne kuratierte Findings/Provenienz zu verlieren; neuer kompetenter Bearbeiter kann aus Repo/kanonischem State fortsetzen.
- **SOTA:** C9 (#39), C1/C7 (#31/#35), #12/#24.
- **Priority:** P0.
- **Status:** `validated`.

## CAP-21 – Rights / Privacy / Processing Admission Control

**Statement:** Das System kann Rechte-, Zugriffs-, Retentions-, External-Processing-, Veröffentlichungs-/Sharing- und Privacy-Constraints so erfassen, dass eine konkrete Verarbeitung vor Ausführung zugelassen, begrenzt oder zur Entscheidung eskaliert werden kann.

- **Need/Pain:** N-016; G-011/G-012.
- **Use Cases:** U1–U4.
- **Leading disciplines:** Legal/Rights/Data Governance; Research Owner bei nicht ableitbaren normativen Entscheidungen; RSE für Enforcement.
- **Scientific/operational invariants:** lawful access ≠ pauschales Copy/Retention/Cloud/Publication-Recht; unknown/restricted kann Processing blockieren; historische Projekte können Daten lebender Personen enthalten.
- **Risks:** RISK-20/-21/-22.
- **Quality attributes:** Rights Traceability; Least-privilege Processing; Decision Visibility; Privacy Awareness.
- **Acceptance seed:** Material `restricted/unknown rights` wird nicht an einen externen Dienst gesendet, wenn erforderliche Zulassungsbasis fehlt.
- **SOTA/Evidence:** #40 current legal/rights review; C9 (#39).
- **Priority:** P0.
- **Status:** `validated as constraint capability`; konkrete Rechtsentscheidung bleibt fallbezogen.

## CAP-22 – Research / Mediation Boundary

**Statement:** Das System kann wissenschaftlichen Research State und downstream Vermittlungs-/Darstellungszustände getrennt halten und eine kontrollierte Übergabe erlauben, ohne Rückschreiben vereinfachter Narrative in den Forschungszustand.

- **Need/Pain:** G-010; #20.
- **Use Cases:** U1–U4 bei späterer Übergabe.
- **Leading disciplines:** Governance/Research Integrity + RSE; Public History erst downstream.
- **Scientific invariants:** Vermittlung erzeugt keine rückwirkende Evidenz; Research-State-Mutation nur über normalen Forschungs-/Promotionpfad.
- **Risks:** RISK-25.
- **Quality attributes:** Boundary Integrity; Traceability back to research; No Back-write.
- **Acceptance seed:** Änderung eines RGK-/Vermittlungstextes verändert kein Histo-Orla-Finding.
- **SOTA:** C8 (#38), #20/#21.
- **Priority:** P2 für Kern-MVP, aber harte Boundary bereits P0-Constraint.
- **Status:** `validated`.

---

# 3. Capability Dependencies

```text
CAP-01 Problem Translation
   ↓
CAP-02 Expertise Routing
   ↓↘
CAP-03 Discovery ──────────────┐
   ↓                           │
CAP-04 Source/Instance Layers  │
   ↓↘                          │
CAP-05 OCR/Derivatives         │
CAP-06 Retrieval               │
CAP-07 Search Boundaries       │
   ↓                           │
CAP-08 Evidence Layering ◀─────┘
   ↓↘
CAP-09 Dependence      CAP-11 Entity Resolution
CAP-10 Discrepancy     CAP-12 Relation Context
   ↓                    ↓
CAP-13 Multi-Scale   CAP-14 Actor Situation
        ↘             ↙
       CAP-15 Multi-Evidence Comparison
               ↓
       CAP-16 Transdisciplinary Synthesis
               ↓
       CAP-17 Human-readable Audit
               ↕
       CAP-18 Validation/Promotion

Cross-cutting foundations:
CAP-19 Reproducible Workflow
CAP-20 Portable/Restartable State
CAP-21 Rights/Processing Admission
CAP-22 Research/Mediation Boundary
```

Kein technischer Komponentenplan ist daraus abzuleiten; die Grafik beschreibt epistemische/funktionale Abhängigkeit.

---

# 4. Capability ↔ Use-Case Matrix

| Capability | U1 Landschaft | U2 Mittelalter | U3 Akteur | U4 Quellenarchiv |
|---|---:|---:|---:|---:|
| CAP-01 Problem Translation | ★★★ | ★★★ | ★★★ | ★★ |
| CAP-02 Expertise Routing | ★★★ | ★★★ | ★★★ | ★★ |
| CAP-03 Discovery/Archive Routing | ★★★ | ★★★ | ★★ | ★★★ |
| CAP-04 Source/Instance Layers | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-05 OCR/Derivative | ★★ | ★★ | ★★ | ★★★ |
| CAP-06 Historical Retrieval | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-07 Search Boundary | ★★★ | ★★★ | ★★ | ★★★ |
| CAP-08 Evidence Layering | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-09 Dependence | ★★ | ★★★ | ★★★ | ★★★ |
| CAP-10 Discrepancy | ★★★ | ★★★ | ★★★ | ★★ |
| CAP-11 Entity Resolution | ★★ | ★★★ | ★★★ | ★★ |
| CAP-12 Relation Context | ★★ | ★★★ | ★★★ | ★ |
| CAP-13 Multi-Scale | ★★★ | ★★★ | ★★★ | ★ |
| CAP-14 Actor Situation | ★ | ★★ | ★★★ | ★ |
| CAP-15 Multi-Evidence Chronology | ★★★ | ★★★ | ★★ | ★ |
| CAP-16 Synthesis | ★★★ | ★★★ | ★★★ | ★★ |
| CAP-17 Audit/Challenge | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-18 Validation/Promotion | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-19 Workflow/Automation | ★★ | ★★ | ★★ | ★★★ |
| CAP-20 Portable State | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-21 Rights Admission | ★★★ | ★★★ | ★★★ | ★★★ |
| CAP-22 Mediation Boundary | ★★ | ★★ | ★★ | ★★ |

`★★★` kritisch, `★★` relevant, `★` situativ.

---

# 5. Quality Attribute Catalogue v1

## QA-01 – Provenance Fidelity

Jeder consequential Finding/Claim muss auf verwendete Quelle/Repräsentationsstufe und, soweit vorhanden, konkrete inspizierte Instanz zurückführbar sein.

**Loss condition:** Findmittel/OCR/Regest/AI wird als stärkerer Source Status dargestellt.

## QA-02 – Findspot Fidelity

Fundstelle muss Transformationen/Search/Excerpt überleben, soweit die Quelle eine stabile Fundstelle erlaubt.

**Test:** T-RISK-02 Roundtrip.

## QA-03 – Epistemic Layer Fidelity

Original/Record, Instanz, Derivat, editorischer Eingriff, Finding, Normalisierung, Claim, Interpretation, Synthese bleiben unterscheidbar.

## QA-04 – Terminological Precision & Validity

Begriffe behalten zeitlichen, räumlichen, institutionellen und historiographischen Geltungsbereich; nahe Begriffe werden nicht automatisch synonymisiert.

## QA-05 – Evidence / Inference Fit

Eine Aussage darf nur so stark sein wie ihre Evidenz und die zulässige Schlussart der führenden Fachdomäne.

## QA-06 – Dependency / Corroboration Integrity

Abhängige Evidenz darf nicht als unabhängige Mehrfachbestätigung gezählt werden.

## QA-07 – Uncertainty & Controversy Preservation

Unresolved, contradiction, competing interpretation und evidence gap sind zulässige Zustände; keine erzwungene Harmonisierung oder Scheingenauigkeit.

## QA-08 – Entity / Relation Precision

False Merge/False Relation wird stärker gewichtet als ein zunächst offener Candidate. Proxy/Kopräsenz ist sichtbar.

## QA-09 – Retrieval Effectiveness

Exact/Known-item Recall, Precision, historische Varianten und Search-Boundary-Transparenz werden auf repräsentativen Gold Queries geprüft. Semantische Zusatzverfahren müssen messbaren Mehrwert zeigen.

## QA-10 – Critical-Token OCR/HTR Quality

Neben CER/WER müssen Namen, Orte, Zahlen, Daten, Fachtermini, Seiten-/Layoutbezug und research-critical tokens geprüft werden.

## QA-11 – Reproducibility

Wesentliche Such-/Processing-Ergebnisse sind anhand Corpus/Input, Query/Parameter, Processor/Version und Status rekonstruierbar.

## QA-12 – Auditability & Challengeability

Research Owner und Fachreviewer können `warum / Quelle / Methode / Alternative / Missing Evidence / Falsification` nachvollziehen, ohne Chat-Historie zu benötigen.

## QA-13 – Human Readability / Progressive Disclosure

Orientierung ist verständlich, ohne wissenschaftliche Details zu entfernen; Details sind bei Bedarf bis zur Quelle/Methode aufklappbar.

## QA-14 – Domain Non-loss

Technische Repräsentation darf fachliche Unterscheidungen, Unsicherheit, mehrere Zeit-/Raumzustände oder konkurrierende Fachmodelle nicht erzwingen/flatten.

## QA-15 – Validation Proportionality

Prüfintensität skaliert mit Konsequenz und Domänenstandard; `independent expert validated` ist nur bei echter unabhängiger Fachprüfung zulässig.

## QA-16 – Portability / Restartability

Kuratierter Research State überlebt Provider-/Toolwechsel und kann ohne Chat von einem neuen kompetenten Bearbeiter fortgesetzt werden.

## QA-17 – Recoverability / Operational Reliability

Reproduzierbare mechanische Workflows können Fehler/Partial States erkennen und kontrolliert fortsetzen; der Nutzer muss Routine nicht permanent überwachen.

## QA-18 – Rights / Privacy Awareness

Verarbeitung berücksichtigt source-/service-spezifische Rechte- und Privacy-Constraints vor Ausführung.

## QA-19 – Interoperability / Replaceability

Bestehende Werkzeuge/Standards können angebunden oder ersetzt werden, ohne kuratiertes Forschungswissen zu verlieren; konkrete Standards nur bei nachgewiesenem Fit.

## QA-20 – Lean Complexity

Jede zusätzliche technische/organisatorische Schicht muss einen belegten Forschungs-/Qualitätsnutzen besitzen; keine Infrastruktur für hypothetische Zukunft.

---

# 6. Capability ↔ High-Risk Map

| Risk cluster | primäre Capabilities |
|---|---|
| Source Laundering / Findspot Loss | CAP-04, 05, 08, 17 |
| OCR critical token corruption | CAP-05, 18 |
| Retrieval blind spots / semantic displacement | CAP-01, 06, 07 |
| False equivalence / anachronism | CAP-01, 11, 15 |
| False corroboration / premature harmonization | CAP-09, 10 |
| False entity merge | CAP-11, 18 |
| Co-presence / motive overclaim | CAP-12, 14, 18 |
| Regional container / scale creep | CAP-13 |
| Simulated expertise / false consensus | CAP-02, 16, 18 |
| Domain flattening | CAP-08, 15, 16, 17 |
| GenAI canonical mutation | CAP-18, 19, 20 |
| Lock-in / silent processor change | CAP-19, 20 |
| Rights/privacy invalid processing | CAP-21 |
| Research UX hides epistemics | CAP-17 |
| Mediation back-write | CAP-22 |
| User micromanagement / overautomation | CAP-17, 18, 19 |

---

# 7. Evaluation / Acceptance Seed Suite

The following cases must later be executable as architecture/MVP tests:

1. **U1 Archive Routing:** From a landscape question, surface map/riss/rechnung/fishery/mill/grazing/boundary source families and keep find-aid status distinct from inspected source.
2. **U1 Retrospective Evidence:** 19th-century Rezess/LiDAR may suggest earlier structure but cannot become direct 16th-century evidence.
3. **U2 Editorial Layer:** `[Stange]` remains editor addition, not historical name.
4. **U2 Homonym:** Altenburg-Knau and Orla-Knau are not auto-merged.
5. **U2 Variant Retrieval:** query expansion is logged and known historical variants improve recall.
6. **U2 Negative Finding:** no `working finding` from `not found` without boundary.
7. **U2 Discrepancy:** 1374/1378 remains unresolved with competing provenance paths.
8. **U2 Relation:** Knewe/Stange co-presence is retrievable but not genealogy.
9. **U2 Settlement:** first mention, archaeology and onomastics remain separate evidence axes.
10. **U3 Motive:** office/confession/network without motive evidence does not promote a motive claim.
11. **U4 Findspot Roundtrip:** source→OCR→search→excerpt→citation returns correct page/folio.
12. **U4 Provider Removal:** canonical research findings/provenance remain usable after disabling AI/semantic/OCR provider.
13. **Rights Admission:** restricted/unknown material cannot be externally processed when policy requires unresolved authorization.
14. **Research Audit:** Reviewer can navigate answer→finding→source/findspot→method/uncertainty without chat.
15. **Mediation Boundary:** downstream rewrite does not mutate research finding.

---

# 8. Deferred / Not Promoted as Capability Requirements

The following remain **solution hypotheses / architecture choices**, not capabilities:

- Zotero as complete Source of Truth – `adapt / strong integration candidate`, not sole research-state owner;
- SQLite / FTS5 / Elasticsearch / Solr etc. – architecture benchmark choices;
- Embeddings / vector database / RAG – optional, benchmark-admitted;
- Knowledge Graph / large ontology – deferred until a representation need requires it;
- Multi-Agent architecture – not implied by epistemic competency modularity;
- specific OCR/HTR engine – corpus benchmark decision;
- specific UI framework;
- full local-first computation – not required; portable/restartable/user-controlled canonical state is required;
- complete regional gazetteer/territorial database before use – build iteratively by research need.

---

# 9. Parallel Fachanforderungen / Live Research Integration

The parallel live-research stream does **not** change the #40→#43 sequence. It contributes candidates through a controlled promotion path.

Promoted from #46 because corroborated by SOTA/Risk/other use cases:

- RC-U2-01 → CAP-04/CAP-08;
- RC-U2-02 → CAP-11;
- RC-U2-03 → CAP-06;
- RC-U2-04 → CAP-12;
- RC-U2-05 → CAP-07;
- RC-U2-06 → CAP-10;
- RC-U2-07 → CAP-15;
- RC-U2-08 → CAP-04/CAP-20.

#47 currently provides strong **stress evidence** for CAP-03, CAP-07, CAP-13 and CAP-15; its historical hypotheses remain live research, not system requirements.

Any later domain requirement documented in #46/#47 is treated as `domain-input / requirement-candidate` until traced through this Capability Map and #42.

---

# 10. #45 Quality Check

- **Domain fit:** each capability names leading/controlling disciplinary ownership.
- **Evidence fit:** capabilities are synthesized from validated discovery/SOTA/risk, not invented from technology preferences.
- **Inference fit:** live-case observations are promoted only when cross-supported; historical findings themselves are not system requirements.
- **Terminology fit:** Capability, Quality Attribute, Requirement and Technology Hypothesis remain distinct.
- **Provenance fit:** each capability links to Needs/Use Cases/SOTA/Risks or live-case RCs.
- **Falsification/challenge:** every prioritized capability has an Acceptance/Evaluation seed.

## Sättigung

`Sufficient for Requirements Baseline v0.1.`

Additional capability enumeration would currently add granularity more than discriminating value. New capability classes should only be introduced by a distinct unmet Need/Failure/Domain invariant.
