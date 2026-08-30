# Histo-Orla – Risk / Constraint / Rights / Failure Review v1

**Work Owner:** #40  
**Status:** `completed-synthesis / v1`  
**Inputs:** #28–#39, #9/#12/#20/#24/#45.  
**Leading competencies:** Research Integrity, Risk/Failure Analysis, Quality Engineering, Legal/Rights/Data Governance, RDM/Provenienz.  
**Controlling competencies:** jeweilige Fachdomänen, RSE/Security/Privacy.

## 1. Purpose

Dieses Artefakt konsolidiert Risiken **nach wissenschaftlicher Konsequenz**, nicht nach technischer Auffälligkeit. Es unterscheidet:

- Prevention – wie wird ein Failure möglichst verhindert?
- Detection – wie erkennen wir ihn?
- Validation/Test – wie prüfen wir die Gegenmaßnahme?
- Residual Risk – was bleibt offen?
- Owner – welche Kompetenz besitzt die Regel?

Severity:

- `critical` – kann wissenschaftliche Evidenz/kanonischen Zustand unbemerkt verfälschen oder rechtlich problematische Verarbeitung auslösen;
- `high` – kann zentrale Findings/Research Workflow erheblich verzerren;
- `medium` – relevante Qualitäts-/Nutzungs-/Wartbarkeitswirkung, meist begrenzbar.

## 2. Current legal / rights evidence boundary

Diese Analyse ist **keine individuelle Rechtsberatung**. Sie dokumentiert architecture-driving Constraints und die Notwendigkeit source-/service-spezifischer Rechteprüfung.

Direkt geprüft:

- §44b UrhG Text und Data Mining: https://www.gesetze-im-internet.de/urhg/__44b.html
- §60d UrhG TDM wissenschaftliche Forschung: https://www.gesetze-im-internet.de/urhg/__60d.html
- §68 UrhG Vervielfältigungen gemeinfreier visueller Werke: https://www.gesetze-im-internet.de/urhg/__68.html
- EU DSM Directive 2019/790, Art. 3/4: https://eur-lex.europa.eu/eli/dir/2019/790/oj/deu
- GDPR, Recital 27: https://eur-lex.europa.eu/legal-content/DE-FR-EN/TXT/?uri=CELEX%3A32016R0679
- Landesarchiv Thüringen, Benutzungsantrag 2024 – Nutzer verpflichtet sich, Persönlichkeits-/Urheberrechte und berechtigte Interessen Dritter zu beachten: https://landesarchiv.thueringen.de/media/landesarchiv/5Standorte/Rudolstadt/Oeffnungszeiten_und_Benutzung/2024-08-02_Benutzungsantrag_2024.pdf
- Thüringer Archivgesetz / Schutzfristen und Veröffentlichung: https://landesarchiv.thueringen.de/media/landesarchiv/1Ueber_uns/Rechtsgrundlagen/tharchivg_gvbl_nr_8_2018_s_308-312_2_.pdf

### Rights findings relevant to architecture

1. `lawful access` ist zentrale Voraussetzung für TDM-Ausnahmen.
2. §44b erlaubt TDM-Kopien rechtmäßig zugänglicher Werke, sofern kein wirksamer Rechtevorbehalt besteht; Kopien sind zu löschen, wenn sie für TDM nicht mehr erforderlich sind.
3. §60d erweitert TDM für wissenschaftliche Forschung; einzelne nichtkommerziell Forschende sind umfasst. Die spezielle langfristige Aufbewahrungsregel in §60d(5) nennt jedoch Forschungsorganisationen und Kulturerbe-Einrichtungen, nicht pauschal jeden individuellen Forscher. Eine dauerhafte persönliche Corpus-Kopie kann daher **nicht allein** aus „wissenschaftliche Forschung“ als generell freigegeben abgeleitet werden; konkrete Schutzdauer/Lizenz/Vertrags-/Schrankenbasis muss bekannt sein.
4. §68 betrifft verwandte Schutzrechte an Vervielfältigungen **gemeinfreier visueller Werke**, aber nicht automatisch jeden Scan/jedes Dokument und nicht andere vertragliche/Archivnutzungsbedingungen.
5. GDPR Recital 27: GDPR gilt nicht für personenbezogene Daten Verstorbener; historische Materialien können jedoch Informationen über **lebende** Personen enthalten, insbesondere bei neueren Quellen.
6. Archivzugang/Benutzung kann neben Urheberrecht auch Schutzfristen, Persönlichkeitsrechte, berechtigte Interessen und konkrete Nutzungsbedingungen enthalten.
7. Daraus folgt keine globale „Cloud verboten/erlaubt“-Regel. Histo-Orla braucht `rights status + processing purpose + service terms → admission decision`.

---

# 3. Prioritized Risk Register

## RISK-01 – Source Laundering

- **Severity:** critical
- **Failure:** Findmittel, Snippet, Regest, OCR, KI-Zusammenfassung oder Sekundärzitat erscheint wie direkt inspizierte Quelle.
- **Affected:** U1–U4; C1/C6/C8.
- **Prevention:** Evidence/representation status; find-aid discovery ≠ inspected evidence; source/derivative chain.
- **Detection:** Audit view zeigt Source Type/Instantiation/inspection status; invariant tests.
- **Test:** U1 Arnshaugk-Teich-Findmittel darf nicht als „Quelle gelesen“ erscheinen.
- **Residual:** menschliche Fehlklassifikation möglich.
- **Owner:** Archivistik/Diplomatik/Research Integrity.

## RISK-02 – Findspot Loss

- **Severity:** critical
- **Failure:** Finding/Quote kann nicht zuverlässig zu Seite/Folio/Regest/Archivalieneinheit zurückgeführt werden.
- **Prevention:** C1/C7 findspot-preserving derivative chain.
- **Detection:** canonical finding without resolvable findspot where source permits one.
- **Test:** OCR/Export/Search round-trip on U4 Gold PDFs.
- **Residual:** Quellen ohne stabile interne Paginierung; Transformationen können Regionmapping verlieren.
- **Owner:** Quellenkunde/RDM + software invariant.

## RISK-03 – OCR/HTR Critical Token Corruption

- **Severity:** high/critical by use
- **Failure:** Name, Ort, Zahl, Datum, Fachterminus falsch erkannt und downstream als Fakt genutzt.
- **Prevention:** raw derivative retained; model/material benchmark; critical-token QA.
- **Detection:** CER/WER + named/number/layout loss checks; confidence/review flags.
- **Test:** U1–U4 representative pages.
- **Owner:** OCR/HTR + Fachdomäne/Paläographie.

## RISK-04 – Retrieval Blind Spot

- **Severity:** high
- **Failure:** historische Schreib-/Namens-/Archivvarianten führen zu systematisch fehlenden relevanten Quellen.
- **Prevention:** C2/C7 layered query expansion; regional/archival terms.
- **Detection:** Gold Query recall; known-item tests.
- **Test:** U1 Teich/Fischerei/Hutung; U2 Namen/lateinische Termini.
- **Owner:** IR + Fachphilologie/Fachdomäne.

## RISK-05 – False Equivalence / Anachronism

- **Severity:** critical
- **Failure:** historische/regionale Begriffe werden fälschlich synonym/modernisiert.
- **Prevention:** C2 terminology layers, validity, competing concepts.
- **Detection:** domain Gold Cases with near-but-wrong concepts.
- **Test:** U2 Vogtei/Ministerialität/Lehen/Grundherrschaft etc.
- **Owner:** jeweilige Fachdomäne + historische Semantik.

## RISK-06 – False Corroboration

- **Severity:** critical
- **Failure:** abhängige Überlieferungen werden als mehrere unabhängige Belege gezählt.
- **Prevention:** C6 claim-specific dependency/independence state.
- **Detection:** source lineage audit before corroboration.
- **Test:** Urkunde→Regest→Edition→spätere Literatur chain.
- **Owner:** Quellenkritik/Diplomatik/Textkritik.

## RISK-07 – Premature Harmonization of Contradictions

- **Severity:** high
- **Failure:** unterschiedliche Zeitstände/Perspektiven/echte Widersprüche werden zu einer glatten Wahrheit zusammengezogen.
- **Prevention:** C6 discrepancy diagnostic; `genuine contradiction/unresolved` states.
- **Detection:** compare source states; audit alternative dispositions.
- **Test:** U1 Karten/Schriftbefund; U3 Self/Fremdzeugnisse.
- **Owner:** jeweilige Fachdomäne + Research Integrity.

## RISK-08 – False Entity Merge

- **Severity:** critical
- **Failure:** Personen/Orte/Institutionen werden falsch vereinigt.
- **Prevention:** candidate resolution; time/region/identifier/evidence checks; no LLM direct merge.
- **Detection:** collision/contradiction rules; domain review for ambiguous cases.
- **Test:** same-name U2/U3 persons and historical places.
- **Owner:** Fachdomäne/Prosopographie/Onomastik + deterministic promotion.

## RISK-09 – Co-presence / Proxy Overclaim

- **Severity:** high
- **Failure:** gleiche Quelle/Ort/Zeit/Membership wird als soziale/politische Beziehung promoted.
- **Prevention:** C4/C5 proxy relation status; explicit extraction rule.
- **Detection:** historical relation without evidence beyond co-presence.
- **Test:** U3 Hof-/Universitäts-/Reise-Co-Presence.
- **Owner:** historische Netzwerk-/Akteursmethodik.

## RISK-10 – Presentist Motive Psychology / Hindsight

- **Severity:** critical for interpretive claims
- **Failure:** Position/Netzwerk/Konfession oder späteres Wissen wird als inneres Motiv behandelt.
- **Prevention:** C5 motive layers + information horizon + alternative explanations.
- **Detection:** strong motive claim lacking contemporaneous/appropriate evidence.
- **Test:** U3 actor situation Gold Case.
- **Owner:** Fachdomäne; L2/L3 validation as needed.

## RISK-11 – Regional Container Bias

- **Severity:** high
- **Failure:** heutige Region/Territorium begrenzt Quellen/Erklärung künstlich.
- **Prevention:** C4 relation-triggered Scale Shift.
- **Detection:** historical relation/administration crosses current scope but research does not.
- **Test:** U2/U3 cross-territorial links.
- **Owner:** Landesgeschichte/historische Geographie.

## RISK-12 – Scale Creep / Context Accumulation

- **Severity:** medium
- **Failure:** „europäischer Horizont“ expandiert ohne diskriminierenden Nutzen und überlastet Forschung.
- **Prevention:** explicit Scale-Shift Trigger + return to question.
- **Detection:** new scope has no source/relation/comparison trigger.
- **Owner:** Research Strategy + leading domain.

## RISK-13 – Simulated Expertise / False Consensus

- **Severity:** critical
- **Failure:** Rollenprompt oder mehrere korrelierte LLM-Antworten erscheinen als Fachkonsens.
- **Prevention:** C3 evidence-based expertise profiles; Validation Levels; AI ≠ L3.
- **Detection:** expertise claim without method/source/reference basis; multiple AI voices counted as independent validation.
- **Owner:** Research Integrity + Fachdomäne.

## RISK-14 – Domain Flattening in Data Model

- **Severity:** critical
- **Failure:** technisches Schema erzwingt fachlich falsche Gleichheiten oder entfernt Unsicherheit/Kontroversen.
- **Prevention:** requirements before data model; representation derives from domain distinctions.
- **Detection:** architecture review against C1–C6 invariants.
- **Test:** can U2 competing concepts/U3 motive layers/U1 source types coexist without forced collapse?
- **Owner:** Fachdomäne + Requirements/Architecture review.

## RISK-15 – Semantic Search Replaces Evidence Retrieval

- **Severity:** high
- **Failure:** embedding/RAG answer seems relevant but exact lexical/fundstellen evidence becomes invisible.
- **Prevention:** C7 lexical baseline; semantic layer additive/benchmark-admitted.
- **Detection:** semantic hit cannot resolve source/findspot or worsens exact-name recall.
- **Test:** Gold Query benchmark.
- **Owner:** IR + Research Integrity.

## RISK-16 – GenAI Canonical Mutation

- **Severity:** critical
- **Failure:** LLM hallucination/proposal silently changes source identity, relation, claim, status or validation.
- **Prevention:** C9 AI-negative core; deterministic mutation API; candidate promotion.
- **Detection:** audit log; state transitions must name actor/method.
- **Test:** adversarial invalid candidate cannot promote.
- **Owner:** Software invariants + scholarly owner.

## RISK-17 – Provider / Format / Service Lock-in

- **Severity:** high
- **Failure:** curated research state disappears/becomes unusable if vendor/model/plugin changes.
- **Prevention:** portable canonical state; open/exportable formats; replaceable processors; backups.
- **Detection:** restore/export/provider-removal tests.
- **Owner:** RSE/RDM.

## RISK-18 – Silent Model / Processor Change

- **Severity:** high
- **Failure:** updated OCR/embedding/LLM changes outputs without revalidation.
- **Prevention:** processor/model/version provenance; regression Gold Cases; material-change control.
- **Detection:** version change triggers benchmark requirement where consequential.
- **Owner:** RSE/Quality + domain owner.

## RISK-19 – Non-reproducible Query/Processing State

- **Severity:** high
- **Failure:** search/result cannot be reconstructed because expansions/filters/model/corpus changed.
- **Prevention:** Query Provenance, corpus boundary, processing logs.
- **Detection:** reproducibility test.
- **Owner:** IR/RSE/RDM.

## RISK-20 – Rights-invalid Copy / Cloud Processing

- **Severity:** critical
- **Failure:** source/scan/text is stored, mined, uploaded or shared without adequate rights/permission.
- **Prevention:** Rights Status + lawful-access/purpose/service-term admission before processing; source-specific constraints.
- **Detection:** no external processing when rights status `unknown` and policy requires resolution.
- **Test:** protected licensed PDF vs public-domain/self-created/open material routing.
- **Residual:** legal interpretation can be fact-specific; escalate when consequential.
- **Owner:** Legal/Rights/Data Governance + Research Owner.

## RISK-21 – Mistaking Research Exception for General Storage Right

- **Severity:** high
- **Failure:** personal permanent corpus copies are justified merely by „scientific research“ without checking applicable copyright/license basis.
- **Prevention:** distinguish access/TDM/retention/publication rights; keep rights provenance.
- **Detection:** retention without documented basis for protected material.
- **Owner:** Legal/Rights.

## RISK-22 – Living-person Personal Data in Historical/Modern Materials

- **Severity:** high depending corpus
- **Failure:** GDPR/privacy duties ignored because project is „historical“.
- **Prevention:** temporal/material screening; deceased-only assumption not global; privacy flags.
- **Detection:** named modern living persons/sensitive sources trigger review.
- **Owner:** Data Protection/Legal.

## RISK-23 – Research UX Hides Epistemic Differences

- **Severity:** high
- **Failure:** understandable answer removes source status, uncertainty, controversy or transformation context.
- **Prevention:** C8 progressive epistemic views; challengeability.
- **Detection:** expert audit cannot reconstruct answer from Research State.
- **Test:** U1–U4 view audits.
- **Owner:** Research UX + Fachdomäne.

## RISK-24 – Visualization Rhetoric / Proxy Concealment

- **Severity:** medium-high
- **Failure:** graph/map layout creates perceived relation/certainty not supported by data.
- **Prevention:** coverage/proxy/filter/uncertainty disclosure; view is derived.
- **Detection:** inspectable mapping from view element to source/research state.
- **Owner:** DH/Visualization + Fachdomäne.

## RISK-25 – Mediation Back-write

- **Severity:** critical
- **Failure:** simplified narrative/public-history state overwrites research findings.
- **Prevention:** #20 hard boundary; one-way controlled handoff; separate write ownership.
- **Detection:** mediation system cannot mutate canonical Research State without normal research promotion.
- **Owner:** Governance/RSE.

## RISK-26 – User Micromanagement Burden

- **Severity:** high for product success
- **Failure:** Research Owner must supervise OCR, filenames, provenance, specialist-method routine and technical recovery.
- **Prevention:** operational ownership; automation for mechanical work; transparent exception handling.
- **Detection:** workflow observation/time-on-routine; repeated manual recovery.
- **Owner:** Human Factors/RSE.

## RISK-27 – Over-automation of Scholarly Judgment

- **Severity:** critical
- **Failure:** attempt to reduce user burden removes necessary scholarly/independent review.
- **Prevention:** C3 validation levels + C9 allocation.
- **Detection:** consequential promotion path has only automated generative checks.
- **Owner:** Research Integrity/Fachdomäne.

## RISK-28 – Premature Architecture / Infrastructure

- **Severity:** high
- **Failure:** ontology/KG/multi-agent/vector DB becomes requirement before validated need.
- **Prevention:** #42 solution-neutral Requirements; #43 Admission Gate.
- **Detection:** component cannot trace to requirement/acceptance test.
- **Owner:** Requirements/Architecture Governance.

## RISK-29 – Overengineering QA / Governance

- **Severity:** medium-high
- **Failure:** generic checklists and state machinery become more complex than the actual research process.
- **Prevention:** #45 six-check baseline + domain-specific additions only where needed; consequence-based validation.
- **Detection:** process step has no risk/quality benefit.
- **Owner:** Research Strategy/Lean Governance.

## RISK-30 – Research Artifact / Issue Duplication

- **Severity:** medium-high
- **Failure:** conflicting full truths in issue comments and Markdown.
- **Prevention:** §14 one fact / one canonical home.
- **Detection:** issue mirrors substantial file content and diverges.
- **Owner:** Governance/RDM.

---

# 4. Hard Constraints v1

## Scientific / epistemic

- **CON-01:** Fachdomäne owns scientific method/evidence/inference rules.
- **CON-02:** Source/derivative/finding/claim/interpretation/synthesis must remain distinguishable.
- **CON-03:** AI output is neither evidence nor independent expert validation.
- **CON-04:** exact findspot/provenance must survive where source permits it.
- **CON-05:** dependent evidence cannot silently count as independent corroboration.
- **CON-06:** unresolved uncertainty/contradiction/identity must be representable.
- **CON-07:** historical and archival terminology may not be overwritten by modern normalization.
- **CON-08:** co-presence/proxy cannot silently become Historical Relation.

## Governance / persistence

- **CON-09:** Chat is not canonical state; §14 applies.
- **CON-10:** mediation cannot back-write outside normal research promotion.
- **CON-11:** material domain/method/model changes are visible/reviewed proportional to consequence.

## Technical

- **CON-12:** deterministically checkable canonical invariants cannot depend solely on LLM judgment.
- **CON-13:** curated Research State must be portable/restartable independent of one AI/provider.
- **CON-14:** processors/services must expose enough provenance/version info for consequential outputs.
- **CON-15:** semantic retrieval cannot replace exact/auditable baseline.

## Rights / privacy

- **CON-16:** lawful access does not by itself imply all forms of copying, retention, cloud processing or publication are permitted.
- **CON-17:** rights/permission/service constraints are checked before external processing of restricted/unclear materials.
- **CON-18:** living-person/privacy risk must remain possible even in a historical project.
- **CON-19:** archive-specific usage/publication conditions remain applicable where relevant.

---

# 5. High-Risk Falsification / Acceptance Tests

### T-RISK-01 Evidence status

Given only a catalog/find-aid entry, system must refuse/promote warning if asked to label claim as `inspected primary source`.

### T-RISK-02 Findspot round trip

Source page → OCR → search hit → excerpt → citation must return same correct page/folio and derivative parent.

### T-RISK-03 Historical terminology

U2 near-concepts must remain separate and produce discriminating questions, not synonym list.

### T-RISK-04 Corroboration lineage

Regest + edition + article from same charter must not become three independent evidence chains.

### T-RISK-05 Actor motive

U3 network/co-presence + office + confession, without motive source, must not produce validated motive claim.

### T-RISK-06 Semantic retrieval

Exact-name known-item recall cannot materially degrade after semantic layer; every semantic hit remains source/findspot-grounded.

### T-RISK-07 GenAI mutation

Hallucinated source/entity/relation candidate must fail promotion without required evidence/invariant checks.

### T-RISK-08 Provider removal

Disable/replace AI/OCR/semantic provider; curated Research State and source provenance remain usable.

### T-RISK-09 Rights admission

Material flagged `restricted/unknown rights` cannot be sent to external service that requires authorization until policy/owner check resolves it.

### T-RISK-10 Research view audit

A qualified reviewer can navigate from answer to evidence/method/uncertainty without chat history.

### T-RISK-11 Mediation boundary

Downstream mediation edit does not mutate canonical Histo-Orla finding.

---

# 6. Residual risks requiring potential Owner Decision later

No current #44 blocker exists. Potential later decisions only if concrete architecture/tool choices produce them:

1. paid/cloud HTR materially outperforms local/open alternatives but introduces cost/rights/privacy trade-off;
2. particular archive/license prohibits desired local retention/cloud processing;
3. publication-level claim needs an external specialist and none is available;
4. two architecture options satisfy scholarship equally but differ materially in cost/maintenance/lock-in;
5. a needed external service cannot provide sufficient export/provenance guarantees.

Until such concrete cases arise, continue autonomously.

## 7. #45 Quality Check

- **Domain fit:** risks derived from C1–C9 scholarly owners; rights from current official EU/German/Thuringian sources.
- **Evidence fit:** legal text is treated as constraint evidence, not individualized legal conclusion.
- **Inference fit:** no blanket claim that research exception authorizes all personal storage/cloud use.
- **Terminology fit:** access/TDM/retention/publication/cloud processing separated.
- **Provenance fit:** source links and SOTA origins retained.
- **Falsification/challenge:** high risks have explicit detection/test; residual decisions isolated.

## 8. Sättigungsbegründung

Risk synthesis is sufficient for Capability/Requirement derivation. Additional risk enumeration without concrete architecture would become speculative. New risks found during #41/#42 are integrated here only if materially distinct; provider-specific legal/security risk is deferred until a provider is actually considered.
