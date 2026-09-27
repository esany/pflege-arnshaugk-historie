# Histo-Orla – Chat-Audit: Quellenerschließung, Kompetenzprofile, Intent- und Requirements-Analyse

**Stand:** 2026-09-27  
**Status:** `analysis / requirements-analysis / research-scoping / no-promotion`  
**Basis:** aktueller Chat vom Herrmann-Upload bis zum Auftrag vom 2026-09-27; frisch revalidiert gegen `main@cd2c06fc17095c2c6d430287734e92061d434173`  
**Primärer Analyse-Owner:** #22 – Kompetenzlandkarte / Research Workframe  
**Method-Routing:** #60 – Domain Method Profiles / Method Truth  
**Requirements-Routing:** #42 – accepted Requirements / Lifecycle  
**Research-Quality:** #45 + `docs/research/source-identity-protocol.md`  
**Historischer Live-Case:** #46 nur als Kontext/Stressfall; keine Herrmann-Findings werden durch dieses Audit reaktiviert.

## 0. Zweck und harte Statusgrenze

Dieses Artefakt auditiert den gesamten aktuellen Chat als **User-/Workflow-Analyse, Kompetenzanalyse, Requirements-Analyse und methodisches Research-Scoping**. Es sichert die darin entstandenen belastbaren Analysebefunde so, dass kein Fortsetzungswissen im Chat verbleibt.

Es ist ausdrücklich **keine**:

- historische Erschließung des Herrmann-Aufsatzes;
- Promotion historischer Findings;
- `method-candidate`- oder `working-method`-Promotion;
- akzeptierte Requirement-Änderung;
- Architektur- oder Implementierungsentscheidung.

Der frühere konkrete Herrmann-Research-Slice aus PR #145 bleibt vollständig zurückgenommen; PR #146 und die RETRACTED-Kommentare in #46 bleiben maßgeblich. Aus PR #145 wird hier **kein historischer Forschungsstand** wiederhergestellt.

Der offene PR #147 wird in diesem Audit nur als nicht gemergter Arbeitsinput betrachtet. Sein Inhalt ist höchstens `analysis/scoping`; er besitzt keine Method-Truth-Authority.

---

## 1. Rekonstruktion des Nutzer-Intents im Chat

Der Chat zeigt eine wichtige Verschiebung bzw. Präzisierung des Auftrags:

1. Ausgangspunkt war ein konkreter wissenschaftlicher Aufsatz als Material.
2. Die Formulierung „systematisch methodische Erschließung der Quelle“ wurde vom Assistenten fälschlich als Auftrag verstanden, den konkreten Herrmann-Aufsatz umfassend historisch zu erschließen und dafür neue Research-Artefakte anzulegen.
3. Der Nutzer korrigierte diese Scope-Ausweitung ausdrücklich: Gemeint war die **systematisch-methodische Erschließungsweise** – also welche fachlichen Operationen, Kompetenzen, Wissensgrundlagen, Qualitätsregeln und Schnittstellen ein Historiker beim Erschließen einer solchen Quelle benötigt.
4. Danach wurde der Intent weiter generalisiert: nicht Herrmann-spezifisch, sondern **quellentyp- und problemübergreifend** sollte geklärt werden, welche Kompetenzen existieren, welche Prinzipien und Wissensbereiche hinter ihnen stehen, woran Fachkompetenz erkennbar ist und wie die Schnittstellen funktionieren.
5. Der Nutzer verlangte anschließend ausdrücklich, diese Profile **zunächst als Analysebefund in den Issues** zu sichern – also noch nicht als fertige Methodenprofile.
6. Der aktuelle Auftrag schärft dies erneut: Der ganze Chat soll als **Analysephase / Anforderungsanalyse / Research-Input** auditiert und vollständig gesichert werden.

### 1.1 Zentrales Intent-Finding

Der Nutzer wollte nicht primär „mehr historische Fakten“, sondern die **fachwissenschaftliche Arbeitsfähigkeit hinter Quellenerschließung verstehen und für Histo-Orla operationalisierbar machen**.

Daraus folgt als Analysebefund:

> Eine quellenbezogene Nutzerformulierung kann auf unterschiedlichen Arbeitsebenen liegen: konkrete historische Forschung, Quellenmethodik, Kompetenzanalyse, Requirements-Analyse oder Systemdesign. Das System darf die tiefere/konsequentere Ebene nicht allein aus sprachlicher Plausibilität auswählen.

Diese Beobachtung passt zur bestehenden Intent-/Erkenntnislücken-Bestandsaufnahme: Intent ist im aktuellen System noch nicht durchgängig als first-class, relationierte Ebene modelliert. Dieses Chat-Ereignis ist ein konkreter Realfall dafür, keine automatische Requirement-Promotion.

---

## 2. Self-Audit des Assistenten

### 2.1 Fehler 1 – Scope-Eskalation in konkrete historische Forschung

Der Assistent hat aus einem methodischen Auftrag eigenmächtig einen konkreten Herrmann-Research-Slice gemacht, neue Research-Dateien erzeugt und PR #145 gemergt. Das war außerhalb des Nutzerauftrags.

Korrektur:

- PR #145 wurde vollständig durch PR #146 zurückgenommen;
- die zugehörigen #46-Kommentare wurden `RETRACTED` markiert;
- kein daraus abgeleiteter Research-Cursor, Finding-Status oder Methodenstatus gilt fort.

**Root-cause als Analysehypothese:** Der Assistent behandelte das Wort „Quelle“ und den vorliegenden Text als dominante Task-Klasse und prüfte die vom Nutzer gemeinte Abstraktions-/Authority-Ebene nicht ausreichend.

### 2.2 Fehler 2 – zu frühe Artifact-/Methoden-Nähe bei PR #147

Nach der Korrektur wurde zwar der Status `scoping / not-a-working-method` eingehalten, aber dennoch vor der ausdrücklich gewünschten Issue-first-Analyse ein umfangreiches Artefakt im Methodenpfad als PR #147 angelegt.

Das ist weniger gravierend als PR #145, aber weiterhin eine Prozessfriktion:

- der fachliche Inhalt war noch nicht SOTA-validiert;
- der Nutzer wollte die Profile zunächst als **Analysebefund**, nicht als faktisch schon angelegten Methodenbestand;
- die Ablage unter `docs/research/methods/` kann trotz Statuslabel methodische Reife suggerieren.

### 2.3 Prozess-Learning

Vor einer konsequenziellen Repository-Mutation müssen deshalb mindestens vier Ebenen explizit aufeinander passen:

```text
Nutzerintent / Erkenntnislücke
→ Task-/Abstraktionsebene
→ erlaubter epistemischer Status des Outputs
→ erlaubte Persistenz-/Promotionsebene
```

Wenn die Formulierung mehrere Ebenen zulässt, muss das System den Kontext heranziehen oder bei consequential Promotion fail-closed bleiben. „Unscharf fragen dürfen“ bedeutet nicht, dass das System still den weitesten Scope wählen darf.

---

## 3. Quellentyp: generalisierter Analysebefund

Der konkrete Ausgangsgegenstand ist ein wissenschaftlicher historischer Fachaufsatz. Für historische Rekonstruktion ist ein solcher Text typischerweise **Forschungsliteratur / Sekundärliteratur**. Für eine historiographiegeschichtliche Frage kann derselbe Text dagegen **Primärquelle für die Geschichte der Forschung** sein.

Der zentrale generalisierte Befund lautet daher:

```text
Quellenrolle
= Material-/Dokumenttyp
× Entstehungsfunktion
× Überlieferungs-/Repräsentationsstufe
× Forschungsfrage
× beabsichtigter Claim
```

Daraus folgen Analyseprinzipien:

- `Primärquelle | Sekundärliteratur` ist keine vollständig absolute Dokumenteigenschaft, sondern fragebezogen.
- Karte, Tabelle, Diagramm oder Rekonstruktion in einer Forschungspublikation ist zunächst ein Autor-/Forschungsprodukt und nicht automatisch unabhängige Evidenz für das historische Phänomen.
- Fußnoten, Bibliographien, Regesten- und Archivhinweise können **Quellenrouter** sein; sie ersetzen die Prüfung der referenzierten Quelle/Edition nicht.
- Historische Quelle, Edition, Forschungsdarstellung, digitale Instanz, konkrete Fundstelle und heutige Interpretation bleiben getrennte Ebenen.

**Status:** `analysis finding / method-scoping input`; kein fertig validierter Quellentyp-Standard.

---

## 4. Was eine historische Kompetenz überhaupt ausmacht

Ein Fachlabel wie `Diplomatik`, `Archivistik`, `Kirchengeschichte` oder `historische Geographie` ist noch keine operationalisierte Kompetenz.

Eine belastbare Kompetenz muss mindestens beantworten können:

1. Für welche Problemtypen ist sie zuständig?
2. Wann führt sie, wann kontrolliert sie nur, wann ist sie nicht zuständig?
3. Welche Fachbegriffe und Gegenstandsmodelle unterscheidet sie?
4. Welche Quellen-/Materialtypen versteht sie?
5. Wie entstehen diese Evidenztypen und was können sie systematisch nicht beobachten?
6. Welche fachlichen Operationen führt sie aus?
7. Welche Evidenz benötigt sie für welche Aussage?
8. Welche Inferenzen sind zulässig bzw. ohne Zusatzbeleg verboten?
9. Welche typischen Failure Modes/Overclaims kennt sie?
10. Wie behandelt sie Unsicherheit, Widerspruch, `unresolved` und Negativbefunde?
11. Welche Gegenbelege/Kontrollen können einen Befund schwächen oder falsifizieren?
12. Welche eigene Evidence Appetite und fachliche Suchsprache besitzt sie?
13. Wann aktiviert sie eine andere Kompetenz?
14. Welche konkrete Frage, Evidenz und Unsicherheit werden beim Handoff übergeben?
15. Was muss von der empfangenden Kompetenz zurückkommen?
16. Welche Methodenliteratur, Standards und Forschungstraditionen müssen ein späteres Profil tragen?
17. Was ist regelbasiert/technisch unterstützbar und was bleibt Fachurteil?
18. Wann ist externe qualifizierte Fachvalidierung nötig?

Das deckt sich in wesentlichen Teilen mit dem bestehenden Domain-Method-Profile-Contract; der Chat schärft besonders **Schnittstellen/Handoffs, relationale Quellenrolle und task-layer/intent fidelity**.

---

## 5. Kompetenzarchitektur als Analysebefund

Die im Chat herausgearbeitete Struktur ist **keine technische Agentenarchitektur** und keine starre Pipeline. Sie dient als Kompetenz-/Research-Map.

### Schicht A – Identität und Überlieferung

- Quellenkunde / historische Quellenkritik
- Bibliographie / Source Identity / wissenschaftliche Publikationskompetenz
- Diplomatik / Urkundenlehre
- Editionswissenschaft / Textkritik
- Archivistik / Provenienz / Registratur- und Überlieferungsgeschichte
- Paläographie / Kodikologie / materielle Textkompetenz

### Schicht B – Text, Bedeutung und Forschung

- historische Philologie / Sprachgeschichte / Semantik
- Terminologie- und Begriffskritik
- Hermeneutik
- Argumentations- und Evidenzanalyse
- Historiographie / Geschichte der historischen Forschung

### Schicht C – historische Gegenstandsdomänen

Problemabhängig u. a.:

- Herrschafts-/Verfassungsgeschichte
- Rechtsgeschichte
- Landes-/Territorialgeschichte
- Kirchen-/Kloster-/Ordensgeschichte
- Sozialgeschichte
- Adels-/Ministerialitätsforschung
- Familien-/Verwandtschafts-/Gendergeschichte
- Wirtschafts-/Agrar-/Ressourcengeschichte
- Prosopographie / Netzwerkforschung
- historische Geographie / historische Kartographie / Kartenkritik
- Onomastik / Toponymie
- Archäologie / materielle Cross-Evidence

**Regionalkompetenz** wirkt als Querschnitt: Archive, Forschungstraditionen, historische Räume, Terminologie und Überlieferung gehören dazu, nicht nur Faktenwissen.

### Schicht D – Suche und epistemische Integration

- historische Heuristik / fachliches Information Retrieval
- historische Epistemologie / Inferenzkontrolle / Forschungsdesign
- transdisziplinäres Expertise Routing / Research Coordination

**Leitregel:** Welche Kompetenz führt, hängt von Forschungsfrage, Materialtyp, Problemklasse und Evidenzlage ab.

---

## 6. Analyseprofile der 15 Kompetenzfamilien

Die folgenden Profile sind `analysis/scoping`; sie sind **keine** SOTA-validierten Domain Method Profiles.

### CP-01 – Quellenkunde / historische Quellenkritik

**Mandat:** Entstehung, Funktion, Perspektive, Selektions- und Überlieferungsbedingungen sowie Aussagepotenzial eines Materials bestimmen.  
**Wissensbasis:** Quellengattungen, Kommunikationssituationen, institutionelle Funktionen, Überlieferung, Bias, Quellenabhängigkeit, innere/äußere Kritik.  
**Kernprinzipien:** Quelle ≠ neutraler Faktenbehälter; Schweigen nur unter geklärten Detectability-/Überlieferungsbedingungen als Negativbefund; abhängige Quellen ≠ unabhängige Bestätigung.  
**QA:** Entstehung/Funktion/Perspektive/Überlieferung/Aussagegrenze explizit.  
**Schnittstellen:** Diplomatik, Archivistik, Philologie, Historiographie, Sachdomänen, Epistemologie.

### CP-02 – Bibliographie / Source Identity / Publikationskompetenz

**Mandat:** Werk, Ausgabe, Auflage, Reihe/Band, Beitrag, konkrete Instanz, Digitalisat und Fundstelle trennen.  
**Wissensbasis:** Bibliographie, Zeitschriften/Reihen, Editions-/Versionsgeschichte, Kataloge, Normdaten, persistente Identifikatoren, Reprints/Digitalisate.  
**Kernprinzipien:** Dateiname ≠ Werkidentität; URL ≠ Quellenidentität; Ausgabe ≠ konkrete Instanz ≠ Fundstelle.  
**QA:** reproduzierbare Zitation und Instanz-/Fundstellenidentität.  
**Schnittstellen:** Editionswissenschaft, Archivistik, Retrieval, RDM.

### CP-03 – Historiographie / Forschungsgeschichte

**Mandat:** Forschung selbst historisieren: Begriffe, Paradigmen, Schulen, regionale Traditionen, Revisionen und Rezeptionsgeschichte.  
**Wissensbasis:** Wissenschaftsgeschichte, Geschichte der Geschichtswissenschaft, Begriffsgeschichte, Fachdebatten.  
**Kernprinzipien:** ältere Forschung kann empirisch wertvoll und theoretisch überholt zugleich sein; neu ≠ automatisch richtig.  
**QA:** Autorenbeobachtung, Autoreninterpretation, zeitgenössisches Forschungsmodell, spätere Rezeption und heutiger Stand getrennt.  
**Schnittstellen:** Hermeneutik, Philologie/Begriffsgeschichte, Sachdomänen, SOTA-Research.

### CP-04 – Hermeneutik / Argumentations- und Evidenzanalyse

**Mandat:** Claims, Belege, Prämissen, inferentielle Zwischenschritte, Alternativen und Grenzen eines Arguments rekonstruieren.  
**Wissensbasis:** Hermeneutik, Argumentationsanalyse, Kausalität, Analogie, Induktion, Abduktion, historische Kontextualisierung.  
**Kernprinzip:** `Aussage ≠ Beleg ≠ Schluss`.  
**QA:** Claim-Evidence-Mapping; implizite Prämissen sichtbar; Gegenargumente/Counterexamples erhalten.  
**Schnittstellen:** Quellenkritik, Philologie, Historiographie, Sachdomänen, Epistemologie.

### CP-05 – historische Philologie / Semantik / Terminologiekritik

**Mandat:** historische Wortbedeutungen, Sprachstufen, Schreibvarianten, Übersetzungen und semantische Verschiebungen bestimmen.  
**Wissensbasis:** historische Sprachwissenschaft, Mittellatein/historische Volkssprachen, Lexikographie, Syntax, Pragmatik, Fach-/Formelsprache.  
**Kernprinzip:** `historische Form → Lesung → Normalisierung → Übersetzung → moderne analytische Kategorie` sind getrennte Schritte.  
**QA:** Originalform erhalten; Mehrdeutigkeit/Unsicherheit nicht glätten; Begriffstyp markieren (`source term | contemporary institutional term | editorial/archive term | modern analytic term | historiographic term | search variant`).  
**Schnittstellen:** Diplomatik, Onomastik, Rechts-/Kirchen-/Herrschaftsgeschichte, Historiographie.

### CP-06 – Diplomatik + Editionswissenschaft/Textkritik

**Mandat:** Überlieferungsstufe, Authentizität, Textgestalt, Formular, Beglaubigung, Datierung, Editionsbasis und editorische Eingriffe kontrollieren.  
**Wissensbasis:** Urkundenlehre, Kanzlei/Formular, Original/Kopie/Transsumpt/Kopiar, Fälschung/Interpolation, kritische Edition, Variantenapparat, Regesten.  
**Kernprinzipien:** `Regest ≠ Urkunde`; `Edition ≠ Original`; `editorische Ergänzung ≠ historischer Wortlaut`; `Registeridentifikation ≠ historische Identität`.  
**QA:** Wortlaut, Apparat, Regest, Editoridentifikation und eigene Normalisierung getrennt.  
**Schnittstellen:** Archivistik, Paläographie, Philologie, Rechtsgeschichte, Quellenkritik.

### CP-07 – Archivistik / Provenienz / Überlieferungsgeschichte

**Mandat:** Entstehungs-/Registraturzusammenhang und spätere Archivierungs-/Bestandsbildung rekonstruieren.  
**Wissensbasis:** Provenienzprinzip, Archivtektonik, Registraturbildung, Fonds/Bestände, Aktenbildung, Kassation, Umlagerung, Repertorien, Signaturgeschichte.  
**Kernprinzip:** Archivüberlieferung ist Resultat historischer Verwaltungs- und Selektionsprozesse.  
**QA:** historischer Registraturzusammenhang ≠ spätere Bestandsbildung ≠ heutiger Bestand ≠ heutige Signatur ≠ historische Editionssignatur.  
**Schnittstellen:** Diplomatik, institutionelle Geschichte, Bibliographie/Source Identity.

### CP-08 – Sachhistorische Domain-Expertise

**Mandat:** fachhistorische Institutionen, Relationen und Prozesse mit eigenem Gegenstandsmodell beurteilen.  
**Wissensbasis:** je Problem u. a. Herrschaft/Verfassung, Recht, Kirche, Adel/Ministerialität, Sozialstruktur, Familie, Wirtschaft/Ressourcen.  
**Kernprinzip:** `Besitz`, `Grundherrschaft`, `Lehen`, `Vogtei`, `Gericht`, `Patronat`, `Abgabe`, `Amt`, `Territorialherrschaft`, `kirchliche Jurisdiktion` dürfen nicht als generische „Kontrolle“ verschmolzen werden.  
**QA:** Relationstyp, Zeitbezug, institutionelle Bedeutung und passende Evidenzklasse explizit.  
**Schnittstellen:** Diplomatik, Philologie, Geographie, Prosopographie, Archäologie.

### CP-09 – historische Geographie / Kartenkritik

**Mandat:** historische Räume, Grenzen, Übergangszonen und kartographische Repräsentationen quellenkritisch rekonstruieren.  
**Wissensbasis:** historische Geographie, Territorial-/Grenzgeschichte, historische Topographie, Kartographiegeschichte, Maßstab/Generalisierung.  
**Kernprinzip:** historischer Raum ≠ automatisch moderne flächig geschlossene Verwaltungseinheit; Grenzen können punktuell, zonal, umstritten oder funktional verschieden sein.  
**QA:** `directly attested | reconstructed | interpolated | candidate | unresolved` unterscheidbar.  
**Schnittstellen:** Herrschaftsgeschichte, Onomastik, Archäologie, GIS/Kartographie.

### CP-10 – Onomastik / Toponymie

**Mandat:** Personen-/Ortsnamen identifizieren, ohne Namensähnlichkeit als Identität zu behandeln.  
**Wissensbasis:** Laut-/Schreibentwicklung, Dialekte, lateinische/volkssprachliche Formen, Namenbildung, regionale Belegserien.  
**Kernprinzip:** Identifikation benötigt mindestens Form + Chronologie + Raum + Kontext + Belegserie + Prüfung konkurrierender Homonyme.  
**QA:** `confirmed | candidate | competing candidates | unresolved | rejected` als zulässige Zustände.  
**Schnittstellen:** Philologie, Geographie, Prosopographie, Editionswissenschaft.

### CP-11 – Paläographie / Kodikologie / materielle Textkompetenz

**Mandat:** Schrift, Abbreviaturen, Hände, Material, Layout und materielle Textschichten beurteilen.  
**Wissensbasis:** Schriftentwicklung, Abkürzungen, Hände, Schreibmaterial, Wasserzeichen/Lagen soweit relevant, Nachträge, Rasuren, Marginalien.  
**Kernprinzip:** `OCR ≠ Transkription ≠ Bildseite`.  
**QA:** unsichere Lesungen markieren; Bildfundstelle und materielle Schichten erhalten.  
**Schnittstellen:** Diplomatik, Textkritik, Archivistik, Philologie.

### CP-12 – Archäologie / materielle Cross-Evidence

**Mandat:** materielle Evidenz als eigene Evidenzlogik zur Kontrolle/Ergänzung schriftlicher Rekonstruktion verwenden.  
**Wissensbasis:** Stratigraphie, Fundkontext, Typologie, Datierung, Taphonomie, Siedlungs-/Landschaftsarchäologie.  
**Kernprinzipien:** `Ersterwähnung ≠ Entstehung`; `kein Fund ≠ Nichtvorhandensein`.  
**QA:** schriftliche und materielle Evidenz zunächst getrennt bewahren; Preservation-/Detectability-Bedingungen explizit.  
**Schnittstellen:** historische Geographie, Siedlungsgeschichte, Umweltgeschichte, Onomastik.

### CP-13 – historische Heuristik / fachliches Information Retrieval

**Mandat:** fachlich bestimmen, wo, mit welchem Vokabular und in welchen Quellen-/Bestandsräumen eine Frage überprüfbar ist.  
**Wissensbasis:** Editionen, Regesten, Archive/Bestände, Bibliographien, historische Schreibvarianten, Fach- und Archivsprache, Citation Chaining.  
**Kernprinzipien:** `Treffer ≠ Evidenz`; `kein Treffer ≠ historische Abwesenheit`; Negativbefunde brauchen Search Boundaries.  
**QA:** Query-/Varianten-/Corpus-/Zugriffsgrenzen dokumentiert.  
**Schnittstellen:** Jede Fachdomäne besitzt eigene Evidence Appetite; Retrieval ist nicht fachneutral.

### CP-14 – historische Epistemologie / Inferenzkontrolle / Forschungsdesign

**Mandat:** zulässige Gesamtinterpretation aus heterogenen Einzelbefunden kontrollieren.  
**Wissensbasis:** Evidenzabhängigkeit, Kausalität, Abduktion, Hypothesenprüfung, Vergleich, Triangulation, Negativbefunde, Unsicherheit, Falsifikation.  
**Kernprinzipien:** abhängige Belege ≠ unabhängige Bestätigung; Übereinstimmung ≠ automatisch gemeinsame Ursache; Widerspruch muss nicht aufgelöst werden; `unresolved` ist valider Zustand.  
**QA:** `Claim → Evidence → Method → Inference → Scope → uncertainty/confidence → competing explanation → falsifier`.  
**Schnittstellen:** alle führenden Domänen; keine Ersatzdomäne für deren Fachurteil.

### CP-15 – transdisziplinäres Expertise Routing / Research Coordination

**Mandat:** Problem zerlegen, passende Fachkompetenzen aktivieren, Authority-Grenzen bewahren und Konflikte/Unsicherheiten sichtbar integrieren.  
**Kernprinzip:** Koordination ist keine epistemische Superdomäne.  
**QA:** Handoffs sind bounded; Fachurteile werden nicht still geglättet; konkurrierende Ergebnisse dürfen parallel bleiben.  
**Schnittstellen:** alle Profile; Routing anhand konkreter triggering observations und Fragestellungen.

---

## 7. Schnittstellen sind eigener methodischer Gegenstand

Ein wesentlicher Chat-Befund ist, dass „andere Disziplin konsultieren“ nicht als Schnittstellenbeschreibung genügt.

Ein belastbarer Handoff sollte mindestens bewahren:

```text
triggering observation
outbound domain
bounded question
evidence/context handed over
terminology already used
uncertainties preserved
what evidence is requested
what the receiving domain may confirm/refute/limit
incommensurabilities / terminology mismatch
return contract
```

Beispiel einer generischen Evidenz-/Kompetenzkette:

```text
historische Philologie
→ mögliche Lesungen / Bedeutungsräume

Onomastik
→ Identitätskandidaten

historische Geographie
→ räumlich/chronologische Kompatibilität

Sachdomäne
→ institutionelle/historische Kompatibilität

epistemische Integration
→ confirmed | candidate | competing candidates | unresolved
```

Keine dieser Domänen wird dadurch Master-Perspektive.

---

## 8. Cross-cutting Qualitätsbefund

Zusätzlich zu domänenspezifischen Regeln gelten als bestehender Mindestkontrollrahmen aus #45:

- Domain Fit
- Evidence Fit
- Inference Fit
- Terminology Fit
- Provenance Fit
- Falsification / Challenge

Der Chat legt als **Analyse-/Scopingkandidaten** zusätzlich nahe:

- dependency awareness;
- temporal fit;
- spatial fit;
- source-function fit;
- representation/instance fit;
- uncertainty preservation;
- handoff integrity;
- negative-evidence discipline;
- no silent normalization;
- no false consensus through correlated evidence.

Diese Zusatzpunkte sind noch keine neuen bindenden Requirements oder universellen Fachstandards.

---

## 9. Requirements-Analyse: Abdeckung und mögliche Lücke

### 9.1 Bereits stark abgedeckte Chat-Befunde

| Chat-/Analysebefund | Bestehende Authority |
|---|---|
| Fachdomäne besitzt Methode/Evidenzmaßstab | `REQ-EPI-001` |
| unscharfe Nutzerfrage fachlich übersetzen | `REQ-EPI-002` |
| Terminologieebenen getrennt halten | `REQ-EPI-003` |
| Unsicherheit / `unresolved` zulassen | `REQ-EPI-004` |
| AI-Ausgabe ist keine Evidenz/independent validation | `REQ-EPI-005` |
| semantische Research States unterscheiden | `REQ-EPI-006` |
| Source/Representation/Instance/Derivative trennen | `REQ-SRC-001` bis `REQ-SRC-004` |
| Domain Method Profiles als eigene Fachobjekte | `REQ-MTH-001` |
| Profile müssen Scope, Materialmodell, Playbook, Inferenz, Evidence Appetite, QA, Handoffs ausdrücken | `REQ-MTH-002` |
| Method Status/Version/Application nachvollziehbar | `REQ-MTH-003` |
| Exploration offen, Promotion fail-closed | `REQ-MTH-004` |
| Counterexample-/Overclaim-Schutz | `REQ-MTH-005` |
| Fachdomänen erzeugen Evidence Demand | `REQ-RSCH-002` |
| Multi-Domain-Handoffs bewahren Evidenz-/Inferenzgrenzen | `REQ-RSCH-004` |
| technische/systemische Arbeit bleibt auf G/N/P und Feedback rückführbar | `REQ-TRACE-001` |

**Befund:** Der Kompetenz-/Methodenteil des Chats erzeugt derzeit überwiegend **keinen neuen Requirement-Bedarf**, sondern konkretisiert bereits akzeptierte Requirements fachlich und liefert Research-/Acceptance-Input für #60.

### 9.2 Offener Candidate: Intent-/Task-Layer-Fidelity

Das konkrete Scheitern bei PR #145 legt einen bisher nicht hinreichend operationalisierten Need nahe:

> Das System muss den vom Nutzer gemeinten **Arbeits-/Abstraktions- und Promotionslevel** erkennen bzw. bei consequential Unsicherheit explizit offenhalten und darf nicht still von Analyse/Methodenfrage zu konkreter Forschung, Requirement-Promotion, Method Truth oder Architektur eskalieren.

Arbeitsname:

`RC-CHAT-INTENT-001 – Intent-/Task-Layer-Fidelity vor consequential Promotion/Mutation`

**Status:** `requirements-analysis candidate only`.

Mögliche Relation zu bestehender Basis:

- `REQ-EPI-002` deckt fachliche Problemübersetzung ab, aber nicht vollständig die Authority-/Task-Layer-Wahl;
- `REQ-TRACE-001` verlangt Rückführung auf Goal/Need/Pain, verhindert aber nicht allein eine falsche Interpretation des aktuellen Intents;
- `AGENTS.md` Work-Context-Vertrag verlangt Purpose, Scope, Leading Domains, May/Must-not und Persistence Target;
- die Intent-Bestandsaufnahme vom 2026-09-24 identifiziert Intent und Erkenntnislücke bereits als noch nicht first-class relationierte Größen.

**Disposition dieses Audits:** kein neues accepted Requirement. Als realer Evidence-/Pain-Fall an #42 und die offene Intent-/Erkenntnislückenanalyse routen.

### 9.3 Relationale Quellenrolle

Die relationale Einordnung `Primärquelle/Sekundärliteratur` ist vorerst ein **fachmethodischer Analysebefund**. Ob daraus eine explizite Systemanforderung nötig ist, soll erst nach #60-SOTA-/Live-Case-Prüfung entschieden werden. Source Identity allein und Source Role sind nicht identisch.

---

## 10. Research-Scoping für #60

Der Chat bestätigt und schärft den bestehenden Profilvertrag. Für jedes spätere Domain Method Profile müssen fachlich/SOTA-basiert mindestens untersucht werden:

```text
Geltungsbereich / leading-controlling-not-responsible
Fachbegriffe / Gegenstandsmodelle
Quellen-/Materialmodell
Formation / Preservation / Detectability
methodisches Playbook
Inferenzvertrag
Evidence Appetite / Recherchelogik
SOTA / Methodenliteratur / Kontroversen
domänenspezifische QA / Failure Modes / Counterexamples
Transdisziplinäre Handoffs / Return Contracts
Automation-/AI-Grenze
externe Validierungs-/Escalation-Trigger
```

### 10.1 Promotion Debt

Keines der CP-01 bis CP-15 ist durch diesen Chat als `method-candidate` oder `working-method` validiert.

Vor Promotion sind mindestens nötig:

1. bounded SOTA-/Methodenrecherche mit exakten Belegen;
2. fachliche Profilgrenze und relevante Traditionen/Kontroversen;
3. positives Live-Case-Testing;
4. Overclaim-/Counterexample-Test;
5. evidence-starved Test, wo sinnvoll;
6. Disposition `adopt | adapt | reject | remain-case-specific`;
7. ggf. unabhängige qualifizierte Fachvalidierung nach Konsequenz/Fachstandard.

### 10.2 Priorisierung

Der bestehende #60-Prioritätsstand bleibt unberührt. Dieser Chat liefert zusätzlichen Scoping-Input insbesondere für:

- Quellenkritik;
- Bibliographie/Source Identity;
- Historiographie;
- Hermeneutik/Argumentationsanalyse;
- historische Philologie/Semantik;
- Schnittstellen- und Multi-Method-Composition.

Eine neue Prioritätsentscheidung wird hier nicht getroffen.

---

## 11. Research-/Workflow-Findings aus dem negativen Fall

Der Scope-Fehler selbst ist ein wertvoller **User-/Workflow-Research-Fall**:

1. Der Nutzer kann eine konkrete Quelle zeigen, aber eine meta-methodische Erkenntnislücke verfolgen.
2. Ein Assistent kann fälschlich das Material mit dem Arbeitsauftrag gleichsetzen.
3. Hohe fachliche Aktivität kann einen falschen Scope verschärfen statt kompensieren.
4. Persistenz/PR-Mutation macht einen Intent-Fehler consequential.
5. Korrektes Revert löscht den historischen Fehlstand, aber der Prozessfehler selbst muss als Research-/Requirements-Evidence erhalten bleiben.
6. Issue-first Analysis kann bei noch ungeklärter Method Truth besser sein als frühe Methodenartefakte.
7. „Nicht fragen müssen“ und „nicht eigenmächtig entscheiden“ sind gleichzeitig zu erfüllen: deterministisch/kontextuell lösbare Ebenen sollen abgeleitet werden; consequential Ambiguität muss fail-closed bleiben.

---

## 12. Canonical Routing / One fact – one home

| Inhalt | Kanonischer Owner nach diesem Audit |
|---|---|
| Kompetenzinventar / welche Kompetenzen werden benötigt | #22 + dieses Analyseartefakt |
| fachliche Operationalisierung / Method Truth | #60 / `docs/research/methods/` erst nach SOTA/Tests |
| cross-cutting Research Quality | #45, unverändert |
| Source-/Instance-/Findspot-Trennung | `docs/research/source-identity-protocol.md`, unverändert |
| accepted Requirements | #42, unverändert |
| neuer Intent-/Task-Layer-Kandidat | #42 als Requirements-Analyseinput, noch nicht accepted |
| Intent-/Erkenntnislückenmodell | bestehende Discovery-/Intent-Arbeit; dieses Audit liefert einen neuen Realfall |
| Herrmann-spezifische historische Findings | **keine**; PR #145 bleibt reverted |
| #46 | Live-Research-Owner bleibt unverändert; dieses Audit ändert keinen historischen Cursor |

---

## 13. Offene Fragen / nächste discriminating actions

1. Reicht die bestehende Requirement-Basis zusammen mit Work-Context-Governance aus, um `RC-CHAT-INTENT-001` zu tragen, oder ist nach Cross-Case-Prüfung ein Requirement-Delta nötig?
2. Wie soll `source role relative to research question` fachlich in Quellenkritik/Historiographie operationalisiert werden?
3. Welche CP-Profile sind fachlich sinnvoll zu bündeln, welche müssen wegen eigener Evidenz-/Inferenzlogik getrennt bleiben?
4. Wie sehen echte Handoff-/Return-Contracts zwischen zwei Domain Profiles aus, ohne daraus voreilig eine technische Agentenarchitektur zu machen?
5. Welche fachlichen Standards/Methodenwerke tragen die Profile jeweils wirklich?
6. Welche Profile benötigen externe qualifizierte Validierung vor `validated-method`?
7. Welche Teile der Profilanwendung sind regelbasiert prüfbar, welche bleiben Human Scholarly Judgment?

---

## 14. Handoff-Check

### Materielle Änderung dieses Audits

- Der gesamte Chat wird als Analyse-/Research-/Requirements-Input klassifiziert und dauerhaft zusammengeführt.
- Die Kompetenzprofile werden nicht als fertige Methoden, sondern als `analysis/scoping` geführt.
- Der relationale Quellentyp-Befund und die Schnittstellenlogik werden erhalten.
- Der Scope-Fehler PR #145 wird als negativer Workflow-/Intent-Fall ausgewertet, ohne historische Inhalte zu reaktivieren.
- `RC-CHAT-INTENT-001` wird nur als Requirements-Analyse-Candidate formuliert.

### Unverändert

- keine historischen Findings promoted;
- keine akzeptierten Requirements verändert;
- keine Architecture-/Implementation-Authority erzeugt;
- #46-Forschungsstand unverändert;
- #45 und Source-Identity-Protokoll unverändert;
- `PROJECT_STATE.md` benötigt aus diesem Analyseaudit allein keine Änderung.

### Fortsetzbarkeit

Ein neuer Bearbeiter soll nach `AGENTS.md → PROJECT_STATE.md → README.md → #22/#60/#42 → dieses Artefakt` ohne Kenntnis des Chats rekonstruieren können:

- was der Nutzer tatsächlich erarbeiten wollte;
- welche Fehler im Chat passiert sind;
- welche Kompetenz-/Methodenbefunde als Scoping gelten;
- welche Requirements bereits tragen;
- welche mögliche Lücke offen ist;
- welche Inhalte ausdrücklich **nicht** promoted wurden;
- welche nächste fachliche Research-Arbeit nötig ist.
