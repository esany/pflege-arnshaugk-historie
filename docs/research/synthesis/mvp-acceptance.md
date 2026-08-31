# Histo-Orla – MVP Acceptance Criteria

**Status:** `owner-accepted / active / iterative`  
**Requirements Owner:** #42  
**Technical Delivery:** #48 / #59  
**Domain Method Owner:** #60  
**Owner Decision:** #44 DD-001  
**Scope:** privates, leanes, agiles Forschungssystem

## 1. Bedeutung

Dieses Artefakt ist der kanonische **MVP-Acceptance-Overlay** auf der Requirements Baseline v0.1.

Der Research Owner hat am 31.08.2026 festgelegt:

> **Die im Domain-Research-/Methodenstrang formulierten Systemanforderungen sind Akzeptanzkriterien des MVP.**

Die Kriterien werden inkrementell erfüllt. Ein früher nutzbarer Slice ist ausdrücklich erwünscht; `MVP complete` bedeutet jedoch erst, dass alle hier für den privaten MVP-Scope markierten Kriterien erfüllt sind.

## 2. Produktmodus

### AC-MVP-001 – Private / lean / agile

Das System muss für den privaten Forschungsgebrauch schnell nutzbar werden und darf nicht von monatelanger Vorab-Architektur oder vollständiger Methoden-Enzyklopädie abhängen.

**Pass wenn:** ein real nutzbarer Walking Skeleton früh verfügbar ist und weitere Anforderungen iterativ ergänzt/härtet.

### AC-MVP-002 – Evolutionäre Architektur

Reversible technische Entscheidungen dürfen früh getroffen und später ersetzt werden. Schwer reversible/teure/lock-in-relevante Entscheidungen benötigen explizite Begründung/ADR.

**Pass wenn:** Delivery nicht auf vollständige Architekturfreigabe wartet, aber irreversible Risiken sichtbar kontrolliert werden.

### AC-MVP-003 – Domain Acceptance führt

Dev darf die owner-accepted Domain-Akzeptanzkriterien nicht still aus Convenience abschwächen.

**Pass wenn:** jedes produktive Slice auf konkrete Acceptance Criteria rückführbar ist.

## 3. Wissenschaftliche Zustands- und Evidenztrennung

### AC-EPI-001 – Zustandsarten bleiben unterscheidbar

Mindestens unterscheidbar und auditierbar:

- `vision`
- `work_order`
- `source / representation / inspected_instance / derivative`
- `findspot / excerpt / observation`
- `finding`
- `research_hook`
- `historical_hypothesis`
- `method_hypothesis`
- `domain_method_profile`
- `method_application`
- `requirement_candidate`
- `accepted_requirement`
- `architecture_choice`
- `prompt / model_run`
- `review / validation`

**Fail wenn:** ein Prompt, eine Hypothese, ein Katalogtreffer oder AI-Output still als wissenschaftlicher Befund/Evidenz erscheint.

### AC-EPI-002 – Unsicherheit ist ein gültiger Zustand

`candidate`, `exploratory`, `unresolved`, `not-assessable`, `contradictory`, `rejected`, `superseded` und vergleichbare Zustände müssen ohne Zwang zur erfundenen Auflösung möglich sein.

### AC-EPI-003 – AI ist keine Evidenz

AI-/LLM-Ausgaben dürfen Vorschläge, Extraktionen oder Hypothesen liefern, aber niemals allein Evidenz- oder unabhängigen Validierungsstatus erhalten.

## 4. Quellenidentität, Dateien und Fundstellen

### AC-SRC-001 – Quellenebenen bleiben getrennt

Bindend gemäß `docs/research/source-identity-protocol.md`:

```text
Source
→ Representation / Edition / Catalogue / Reproduction
→ inspected Instance
→ Derivative / OCR / HTR / Transcription
→ Findspot / Excerpt
→ Finding / Interpretation
```

### AC-SRC-002 – Findspot-Roundtrip

Ein Befund/Excerpt muss zur konkret verwendeten Instanz und Seite/Blatt/Regest/Fundstelle zurückführbar sein.

### AC-SRC-003 – OneDrive / Zotero / Histo-Orla Verantwortung

```text
OneDrive = Source of Bytes
Zotero   = bibliographische/archivische Verwaltung + Attachment-Referenz
Histo-Orla = wissenschaftlicher Research State
```

Das System muss diese Schichten integrieren können, ohne Pfad, Zotero-Key oder OneDrive-ID zur alleinigen wissenschaftlichen Identität zu machen.

### AC-SRC-004 – Read-first Integration

Für den MVP genügt zunächst robustes Lesen/Auflösen von Zotero-Metadaten und Source Bytes. Write-back ist nur dort MVP-pflichtig, wo ein realer Nutzerworkflow ihn benötigt.

## 5. Domain Method Profiles – Fachmethodische Mittelschicht

### AC-METHOD-001 – Fachmethode ist kein Rollenprompt

Das System muss Domain Method Profiles als eigenständige, versionierbare fachliche Objekte unterstützen. Ein Fachlabel oder Prompt genügt nicht.

### AC-METHOD-002 – Profilumfang

Ein Domain Method Profile muss mindestens ausdrücken können:

1. Geltungsbereich / Problem- und Quellentypen;
2. Fachbegriffe / Gegenstandsmodelle / konkurrierende Modelle;
3. Quellen-/Materialmodell und typische Biases/Überlieferungsprobleme;
4. ausführbares fachliches Playbook;
5. Inferenzvertrag: zulässige und unzulässige Schlüsse;
6. Evidence Appetite sowie Fach-/Archiv-/Suchvokabular;
7. SOTA-/Methodenliteratur und Kontroversen;
8. QA, typische Fehlschlüsse, Falsifikation/Counterexamples;
9. transdisziplinäre Handoffs / Evidence Routing;
10. Grenze Mensch ↔ Regel ↔ Spezialalgorithmus ↔ GenAI.

### AC-METHOD-003 – Method Status

Profile müssen mindestens als `scoping`, `method-candidate`, `working-method`, `validated-method`, `deprecated/revised` unterscheidbar sein.

### AC-METHOD-004 – Konkrete Anwendung nachvollziehbar

Ein consequential Finding muss nachvollziehbar machen können, welche konkrete Method Application und welche Profilversion/-status verwendet wurde, soweit die Methode bereits operationalisiert ist.

### AC-METHOD-005 – Fail closed on promotion, not exploration

Fehlende/noch nicht ausgereifte Methode darf Exploration nicht blockieren. Sie darf aber keinen höheren epistemischen Status vortäuschen.

**Beispiel:** `method-candidate` → explorative Analyse erlaubt; consequential Promotion → blockiert/bleibt Candidate.

### AC-METHOD-006 – Evidence-starved Verhalten

Fehlt die nötige Evidenz, muss die Methode `unresolved`/`not-assessable` ausgeben können, statt eine plausible Geschichte zu erzeugen.

### AC-METHOD-007 – Overclaim Prevention

Ein Profile gilt erst als belastbar, wenn es neben einem positiven Fall mindestens einen typischen Overclaim/Counterexample korrekt verhindert oder begrenzt.

### AC-METHOD-008 – Erste reale Methodenscheibe

Für den ersten MVP-Scope wird mindestens **Diplomatik/Urkundenlehre + Editionswissenschaft/Textkritik** als reales Domain Method Profile auf U2-/NHUB-Material operationalisiert und im System anwendbar/auditierbar gemacht. Weitere Profile werden problemgetrieben ergänzt.

## 6. Research Hooks, Evidenzbedarf und transdisziplinäre Arbeit

### AC-RESEARCH-001 – Research Hook ≠ Hypothese ≠ Finding

Das System muss einen Research Hook wie „prüfe Ausstattung/Besitzentwicklung“ als offenen Anschlussauftrag speichern können, ohne ihn als historische Hypothese oder Finding zu promoten.

### AC-RESEARCH-002 – Evidence Demand

Aktivierte Fachdomänen/Methoden müssen Evidenzbedarf erzeugen können: relevante Quellen-/Materialklassen, Such-/Archivvokabular, notwendige Vergleiche/Kontrollen und mögliche Falsifikation.

### AC-RESEARCH-003 – Quelle begrenzt nicht den gesamten Scope

Ein einzelner Quellentext darf nicht automatisch bestimmen, welche Ursachen/Erklärungsebenen als ausreichend untersucht gelten. Expliziter Quellenbefund und späterer Erklärungsraum bleiben getrennt.

### AC-RESEARCH-004 – Multi-Method / Multi-Domain Handoff

Beobachtungen müssen gezielt an andere Fachdomänen weitergegeben werden können, ohne deren Evidenz-/Inferenzregeln zu verschmelzen.

### AC-RESEARCH-005 – Konkurrenz von Erklärungen

Mehrere plausible historische Erklärungen/Hypothesen müssen parallel bestehen, durch Evidenz gestützt/challenged und ggf. unresolved bleiben können.

## 7. Retrieval / OCR / Quellenarbeit

### AC-IR-001 – Exakte Suche ohne LLM-Pflicht

Exact Search und nachvollziehbare Filter/Query Logs müssen ohne LLM funktionieren.

### AC-IR-002 – Historische Varianten

Kontrollierte historische Namens-/Schreibvarianten und nachvollziehbare Query Expansion müssen unterstützt werden.

### AC-IR-003 – OCR/HTR bleibt Derivat

OCR/HTR/Transkription darf die konkrete Source Instance nicht ersetzen; Parentage und Findspot-Mapping bleiben erhalten.

### AC-IR-004 – Research-kritische Qualität

OCR/HTR/Recherchequalität wird nicht nur über generische Metriken bewertet, sondern gegen forschungsrelevante Namen, Orte, Zahlen, Begriffe und Fundstellen.

## 8. Audit, Handoff und Chat-Unabhängigkeit

### AC-AUDIT-001 – Human-readable Audit

Für ein Finding/Claim muss ein Mensch nachvollziehen können:

- welche Quelle/Instanz/Fundstelle;
- welcher Evidence Status;
- welche Methode/Method Application;
- welche Unsicherheit/Alternative;
- welche Review-/Validation-Stufe;
- was AI/Automation beigetragen hat;
- welche History/Korrektur vorliegt.

### AC-AUDIT-002 – Kein Wissensmonopol

Continuation-critical State darf nicht im Chat monopolisiert werden. Ein neuer autorisierter Kontext muss aus Repo + kontrollierter Evidenz korrekt weiterarbeiten können.

### AC-AUDIT-003 – Research-ready Availability

Identität/Locator allein genügt nicht. Wenn die nächste Aktion direkte Quelleninspektion verlangt, muss der autorisierte Kontext die benötigte konkrete Instanz tatsächlich öffnen können oder einen expliziten Availability-Blocker sehen.

## 9. Deterministische Schutzschicht

### AC-GUARD-001 – Formal prüfbare Invarianten in Software

Wo formal entschieden, sollen mindestens folgende Fehler reproduzierbar blockierbar sein:

- ungültige Referenz/Parentage;
- Evidence-/Findspot-Pflicht bei entsprechender Promotion;
- AI-Output als Evidence;
- unerlaubte Status-/Authority-Transition;
- History-Verlust bei Correction/Demotion;
- fehlende erforderliche Method-/Review-Grundlage für einen höheren Status.

Die Maschine prüft Formalität/Erlaubtheit, nicht historische Wahrheit.

## 10. Portabilität, Rechte und technische Subsidiarität

### AC-TECH-001 – Portable / restartable Research State

Der kuratierte Forschungszustand darf weder an Chat noch an einen einzelnen AI-/Cloud-Provider gebunden sein und muss exportierbar/restartbar bleiben.

### AC-TECH-002 – Curated vs. regenerable

Kuratierter Forschungszustand und regenerierbare Indizes/Caches/Embeddings/Thumbnails müssen unterscheidbar sein.

### AC-TECH-003 – Rights / Privacy Admission

Externe Verarbeitung muss blockierbar sein, wenn Rechte/Privacy/Policy dies verlangen; Credentials/Secrets gehören nicht in den Research State.

### AC-TECH-004 – Technische Subsidiarität

Bevor Eigenentwicklung/GenAI eingesetzt wird, sind geeignete bestehende Tools, Standards, deterministische Verfahren oder spezialisierte Algorithmen zu prüfen. Die kleinste hinreichende Lösung wird bevorzugt.

## 11. UX / Nutzbarkeit

### AC-UX-001 – Progressive Disclosure

Das System soll einen einfachen Forschungsfluss erlauben, ohne wissenschaftliche Tiefe zu verstecken: Orientierung zuerst, Audit/Methodik/Evidenz bei Bedarf aufklappbar.

### AC-UX-002 – Unscharf fragen, fachlich sauber arbeiten

Der Nutzer muss nicht das richtige historische/archivische Fachvokabular kennen. Das System soll Problemübersetzung, Begriffskandidaten und Evidence Routing anbieten, ohne konkurrierende Fachmodelle still gleichzusetzen.

### AC-UX-003 – Private Workflow zuerst

Der MVP optimiert auf den realen privaten Forschungsworkflow des Owners, nicht auf Multi-Tenant-/Enterprise-/Publikumsplattformanforderungen.

## 12. MVP-Delivery

### Walking Skeleton – erste nutzbare Kette

```text
Zotero Item / Source Metadata
→ OneDrive/Test Source Bytes
→ Source / inspected Instance
→ Findspot / Text-OCR-Derivative
→ Exact/Variant Search
→ Excerpt / Observation
→ Finding / Hypothesis / Research Hook
→ Method-/Evidence-Status
→ Audit / Persistenz / Handoff
```

### MVP complete

`MVP complete` erst wenn:

1. alle für den privaten Scope aktiven Kriterien dieses Artefakts bestanden sind;
2. mindestens ein realer U2-End-to-End-Fall den Workflow nutzt;
3. mindestens ein methodischer Overclaim-/Evidence-starved-Test korrekt fail-closed/unresolved endet;
4. Restartability aus einem frischen Kontext funktioniert;
5. technische Restschulden und noch nicht implementierte spätere Profile sichtbar sind.

## 13. Explizite Non-goals des ersten MVP

Nicht erforderlich, sofern kein realer Pain es erzwingt:

- vollständige historische Methoden-Enzyklopädie;
- Multi-Agent-Plattform;
- Knowledge Graph als Pflichtkern;
- RAG/Vector Search als Basisvoraussetzung;
- Enterprise-Multiuser-/RBAC-/Workflow-Suite;
- umfassende OneDrive-Dateiverwaltung durch Histo-Orla;
- Publikations-/Vermittlungsplattform.

## 14. Leitregel

> **Früh nutzbar, fachlich ehrlich, technisch austauschbar.**

> **Das MVP ist das System, das die Domain-Akzeptanzkriterien im privaten Forschungsworkflow tatsächlich trägt – nicht eine vollständige Plattformvision.**
