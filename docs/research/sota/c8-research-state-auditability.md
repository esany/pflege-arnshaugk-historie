# C8 – Human-readable Research State, Progressive Disclosure und wissenschaftliche Auditability

**Work Owner:** #38  
**Status:** `sufficient-for-current-decision / sota-v0.1`  
**Leading competencies:** Human Factors, Research UX, Information Architecture, Research Integrity.  
**Controlling competencies:** Digital Humanities/Visualization, Accessibility, Provenienz/RDM, jeweilige Fachdomänen.

## 1. Research Questions

RQ-C8-01 bis RQ-C8-04:

1. Wie kann ein kanonischer komplexer Research State verständlich und tief auditierbar dargestellt werden?
2. Welche Challenge-/Review-Aktionen braucht Research Owner/Fachprüfer?
3. Wie werden Unsicherheit/Kontroverse sichtbar, ohne Scheingenauigkeit?
4. Wie bleiben Research Views von adressatenspezifischer Vermittlung getrennt?

## 2. Search Scope / Boundary

Geprüft wurden:

- Digital-Humanities-Forschung zur interaktiven Provenienzdarstellung historischer Records;
- W3C PROV als domänenagnostische Referenz für Entity/Activity/Agent/Derivation/Responsibility/Revision;
- Human-AI-Interaction-Guidelines zu Erklärung, Korrektur, Unsicherheit und Kontrolle;
- DH-Arbeiten zu genuiner Unsicherheit und Grenzen digitaler Exaktheit;
- historische Visualisierungsarbeit, die bekannte/unbekannte Daten und Transformationen sichtbar macht;
- #9/#12/#20 als internes Prior Art.

Nicht beansprucht wird ein finales UI-Design oder eine bestimmte Visualisierungsbibliothek.

## 3. Inspected sources

- Vancisin et al., 2023, **Provenance visualization: Tracing people, processes, and practices through a data-driven approach to provenance**, Digital Scholarship in the Humanities: https://academic.oup.com/dsh/article/38/3/1322/7140400
- W3C, **PROV Model Primer**: https://www.w3.org/TR/prov-primer/
- W3C, **PROV Overview**: https://www.w3.org/TR/prov-overview/
- Microsoft Research, **Guidelines for Human-AI Interaction**: https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- Tarte, **Digitizing the act of papyrological interpretation: negotiating spurious exactitude and genuine uncertainty**: https://academic.oup.com/dsh/article/26/3/349/1141364
- Vancisin et al., 2025/26, **Representing provenance and track changes of cultural heritage metadata in RDF: a survey of existing approaches**: https://academic.oup.com/dsh/article/41/Supplement_1/i196/8219704
- AHR, **Historical Research in a Digital Age: Reflections from the Mapping the Republic of Letters Project**: https://academic.oup.com/ahr/article-pdf/122/2/400/13162549/zah400.pdf

## 4. Findings

### F-C8-01 – Provenienz darf nicht auf eine versteckte „About“-Seite ausgelagert werden

Die 2023er DSH-Studie zur provenance-driven visualization historischer Records zeigt, dass Transformations- und Kurationsschritte in digitalen Interfaces leicht unsichtbar werden. Eine interaktive Provenienzdarstellung kann Transparenz und kritischere Interpretation fördern, hat aber auch Kosten/Komplexität.

Für Histo-Orla folgt:

> Provenienz ist kein administrativer Zusatz, sondern Teil des interpretierbaren Research State und muss **am relevanten Finding/Source/Derivative zugänglich** sein.

Das heißt nicht, dass alle Details immer eingeblendet werden müssen – gerade hier ist Progressive Disclosure sinnvoll.

### F-C8-02 – Ein kanonischer Zustand kann mehrere Sichten haben, sofern die Views abgeleitet sind

W3C PROV ist als methodische Referenz nützlich: Entity, Activity, Agent, derivation, revision und responsibility können getrennt beschrieben werden. Entscheidend für Histo-Orla ist nicht PROV als Pflichtschema, sondern die Trennung:

```text
Research object / finding / source
→ welche Activities/Transformations?
→ welche Agents/Tools?
→ wovon abgeleitet?
→ welche Version/Revision?
```

Aus diesem einen nachvollziehbaren Zustand können verschiedene **Views** entstehen, ohne den Inhalt manuell doppelt zu pflegen.

### F-C8-03 – Progressive Disclosure soll Wissenschaft zugänglich machen, nicht ausblenden

Für Histo-Orla ist ein geeignetes View-Modell schichtenweise:

#### Level 0 – Answer / Orientation

- kurze Antwort/Synthese;
- Evidenzstatus in verständlicher Sprache;
- wichtigste Unsicherheit/Kontroverse;
- nächste sinnvolle Aktion.

#### Level 1 – Findings / Reasons

- zentrale Befunde/Claims;
- „warum diese Antwort?“;
- Quellen/Fundstellen;
- alternative Interpretation(en).

#### Level 2 – Source / Provenance Audit

- Source Identity;
- exact instance/findspot;
- original/edition/regest/OCR status;
- Transformationen/Derivate;
- Search Boundary / source dependence.

#### Level 3 – Method / Competency Audit

- führende Fachdomäne;
- Methode/Inference Rule;
- Begriffsschichten/Geltungsgrenzen;
- Neighbor Disciplines;
- Qualitäts-/Falsifikationscheck.

#### Level 4 – Research History / Decision Audit

- Hypothesen/Alternativen;
- verworfene Ansätze;
- Validation Level;
- Versionen/Entscheidungen/Research Debt.

Nicht jeder Nutzerblick braucht Level 4. Aber kein Level 0 darf eine fachliche Unsicherheit in falsche Eindeutigkeit umschreiben.

### F-C8-04 – Challengeability ist eine Kernfunktion, nicht bloß Erklärtext

Microsofts Human-AI-Guidelines stützen allgemeine Interaktionsprinzipien:

- Korrektur muss leicht sein;
- bei Unsicherheit Scope begrenzen/disambiguieren;
- erklären, warum das System gehandelt hat;
- globale Kontrolle und transparente Updates.

Für wissenschaftliche Forschung werden daraus konkrete Challenge-Aktionen:

- **Warum?** → welche Befunde/Inference tragen die Aussage?
- **Quelle?** → zur konkreten Source/Findspot-Ansicht.
- **Welche Methode/Fachperspektive?**
- **Alternative?** → konkurrierende Interpretation/Erklärung.
- **Was fehlt?** → Evidence Gaps / Search Boundary / Research Debt.
- **Wie sicher/validiert?** → Evidence/Validation Status statt bloßer Prozentwert.
- **Was würde die Aussage widerlegen?** → Falsification/Discriminating Action.
- **Korrigieren / zurückstufen / als Hypothese markieren.**

Das Research UI muss damit **operative Kontrolle** erlauben, nicht nur passive Transparenz.

### F-C8-05 – Unsicherheit darf nicht durch digitale Präzision verschwinden

Tartes Arbeit zur digitalen Papyrologie ist methodisch übertragbar: Digitale Repräsentation kann „spurious exactitude“ erzeugen, obwohl Interpretation tatsächlich unsicher ist.

Histo-Orla sollte daher keine scheinpräzise einheitliche Confidence-Zahl als Standard verwenden. Besser sind fachlich lesbare Statusdimensionen:

- direct / indirect evidence;
- source/derivative status;
- interpretation/hypothesis;
- dependence/independence known/unknown;
- disputed/contested;
- validation level;
- unresolved identity;
- search/coverage boundary.

Quantitative Scores sind nur dort sinnvoll, wo das Fachverfahren sie trägt (z. B. OCR confidence), und dürfen nicht in „historische Wahrheit 87 %“ umgerechnet werden.

### F-C8-06 – Visualisierung kann unbekannte/fehlende Daten sichtbar machen, darf aber nicht zum neuen epistemischen Owner werden

Mapping-the-Republic-of-Letters-Arbeiten zeigen Nutzen von Visualisierungen für bekannte und unbekannte Mengen in historischen Datensätzen. Gleichzeitig sind Visualisierungen interpretative Konstruktionen.

Für Histo-Orla gilt:

- Timeline, Karte, Netzwerk, Provenance Graph können **Research Views** sein;
- jede View muss Dataset/Filter/Proxy-Regeln und Uncertainty zeigen können;
- Visual Layout/Closeness ist kein Beleg für historische Beziehung;
- View ist regenerierbare Darstellung des Research State, nicht dessen Wahrheitsspeicher.

### F-C8-07 – Research Owner und Fachprüfer brauchen unterschiedliche Default-Tiefen, aber denselben Zustand

#### Research Owner default

- verständliche Frage/Antwort;
- Fachbegriffe mit Erklärung;
- wichtige Befunde + Quellen;
- Unsicherheit/Kontroverse;
- was das System getan hat;
- nächste sinnvolle Aktion;
- einfache Challenge-Aktionen.

#### Fachprüfer default

- exact source/findspot;
- Evidenz-/Überlieferungsstatus;
- Fachmethodik/inference;
- Search Boundary;
- alternatives/discrepancies;
- dependency/provenance;
- Validation History.

Beide Views greifen auf denselben Research State zu. Keine manuelle „Laienversion“ als parallele Wahrheit.

### F-C8-08 – Forschung ↔ Vermittlung bleibt harte Grenze

Eine Research-Owner-View erklärt denselben wissenschaftlichen Zustand verständlich. Eine Public-History-/Museums-/Storytelling-/Social-Media-View hat dagegen andere Ziele (Auswahl, Dramaturgie, Zielgruppe, Medium).

Deshalb:

```text
canonical Research State
→ Research/Audit Views innerhalb Histo-Orla
→ kontrollierte Übergabe
→ mediation/application views (z. B. RGK)
```

Kein downstream narrative back-write.

## 5. Research View Model v0.1

| View | Leitfrage | Muss sichtbar halten |
|---|---|---|
| Orientation | Was wissen wir aktuell? | answer, status, uncertainty, next action |
| Finding | Warum sagen wir das? | findings/claims, alternatives, evidence |
| Source Audit | Worauf basiert es genau? | source identity, findspot, derivative/transmission |
| Method Audit | Wie wurde geschlossen? | competency, method, inference, terminology, falsification |
| Controversy | Welche Alternativen/Dispute? | positions, evidence differences, unresolved points |
| Research History | Wie entstand der Stand? | versions, rejected hypotheses, validation, decisions |
| Spatial/Timeline/Network | Welche Muster sind explorierbar? | coverage, proxy rules, temporal validity, uncertainty |

## 6. Human-readable Quality Criteria

Eine Funktion ist nicht ausreichend, wenn der Research Owner nicht beantworten kann:

1. Was ist Befund und was Interpretation?
2. Welche Quelle/Fundstelle trägt die Aussage?
3. Welche Fachperspektive/Methode ist aktiv?
4. Wo liegt Unsicherheit/Nichtwissen/Kontroverse?
5. Warum wurde ein Begriff/Entity/Relation so behandelt?
6. Welche Alternative existiert?
7. Was kann ich korrigieren/hinterfragen?
8. Was wäre der nächste diskriminierende Schritt?

Ein Fachprüfer muss zusätzlich die wesentliche Analyse ohne Chat anhand Research State/Source/Method rekonstruieren können.

## 7. Capability Candidates

- `CAP-RESEARCH-ORIENTATION-VIEW`
- `CAP-FINDING-AUDIT`
- `CAP-SOURCE-PROVENANCE-AUDIT`
- `CAP-METHOD-COMPETENCY-AUDIT`
- `CAP-CONTROVERSY-UNCERTAINTY-VIEW`
- `CAP-CHALLENGEABILITY`
- `CAP-RESEARCH-HISTORY`
- `CAP-DERIVED-RESEARCH-VIEWS` für Karte/Timeline/Netzwerk etc.
- `CAP-MEDIATION-BOUNDARY`

## 8. Quality / Requirement Candidates

- REQ-C8-A: Jeder consequential Output muss von Synthese zu konkreten Findings und Source/Findspots navigierbar sein.
- REQ-C8-B: UI/View darf Source/Derivative/Interpretation/Uncertainty nicht durch Vereinfachung verschmelzen.
- REQ-C8-C: Research Owner muss Challenge-Aktionen für Warum/Quelle/Alternative/Was fehlt/Validation nutzen können.
- REQ-C8-D: Unsicherheit muss als fachlich geeigneter Status darstellbar sein; keine universelle pseudo-präzise Confidence-Zahl.
- REQ-C8-E: Verschiedene Research Views müssen aus einem kanonischen Zustand abgeleitet werden und dürfen nicht separat Wahrheit pflegen.
- REQ-C8-F: Visualisierungen müssen Coverage/Filter/Proxy-/Evidenzregeln auditierbar machen, soweit sie Schlussfolgerungen beeinflussen.
- REQ-C8-G: Research Views und downstream mediation müssen technisch/organisatorisch getrennte Schreibverantwortung besitzen.
- REQ-C8-H: KI-gestützte Vorschläge müssen korrigierbar, zurückstufbar und in ihrem Grund nachvollziehbar sein.

## 9. Challenge interner Prior Art

`paleo-type` Progressive Disclosure und Operational Ownership werden stark bestätigt. C8 konkretisiert aber: nicht „mehr Details aufklappen“ als reine UI-Technik, sondern **epistemische Navigation** Answer→Finding→Evidence→Method→History.

RGK-Multiple-Views wird bestätigt, solange Views derived sind und die Research/Mediation-Grenze bestehen bleibt.

## 10. Open Questions / bounded debt

- konkrete UI-Komponenten/Interaktionsdesigns werden erst nach Architecture/Prototype empirisch getestet;
- Accessibility muss in späteren UI-Requirements konkretisiert werden;
- Visualisierungsformen für komplexe Provenienz/Discrepancy dürfen zunächst einfach textuell/tabellarisch sein – kein Visualisierungssystem aus Selbstzweck.

## 11. #45 Quality Check

- **Domain fit:** Human Factors/Research UX + Research Integrity führen; Visualisierung ist Mittel, nicht Wahrheitsmodell.
- **Evidence fit:** DH-Provenance-Forschung, PROV-Referenz, Human-AI-Studie und Uncertainty-Methodik direkt geprüft.
- **Inference fit:** PROV wird nicht als Pflichtschema und allgemeine HCI-Guidelines nicht als historischer Fachstandard missverstanden.
- **Terminology fit:** Research View, Mediation View, provenance, uncertainty, confidence, validation getrennt.
- **Provenance fit:** Quellen/Transformationen sind explizit Teil des View-Modells.
- **Falsification/challenge:** Challengeability wird selbst zur Acceptance-Anforderung; späterer Prototype-Test kann View-Hypothesen widerlegen.

## 12. Sättigungsbegründung

Für Requirements ist ausreichend geklärt, dass Auditability direkt am Research State und über mehrere abgeleitete Tiefenstufen verfügbar sein muss. Konkretes UI-Design bleibt bewusst experimentell/reversibel und ist kein Grund für weitere Vorab-SOTA.
