# Owner-confirmed competence-analysis working state

```yaml
title: Owner-confirmed competence-analysis working state
date: 2026-09-27
status: owner-confirmed-analysis-input
epistemic_status: analysis / competence-scoping / no-promotion
source_role: owner-confirmed workshop synthesis
authorship_note: >
  Mixed workshop synthesis. The Human Owner explicitly confirmed this detailed
  state as the semantic basis for continuation. Confirmation establishes intended
  project-analysis meaning, not disciplinary truth.
semantic_authority:
  for_current_analysis_baseline: owner-confirmed
  for_domain_method_truth: none
  for_historical_truth: none
  for_requirements: none
  for_architecture: none
downstream_owners:
  competence_inventory: "#22"
  domain_method_research: "#60"
prior_derivatives:
  - "PR #147 — historical unmerged working derivative"
  - "PR #148 — merged prior chat-audit derivative; reconciliation target"
must_not:
  - import additions from prior derivatives
  - SOTA-correct the source
  - create historical findings
  - promote method status
  - infer final profile taxonomy
```

> This file is the frozen semantic input for the bounded preservation run. It records intended project-analysis meaning, not disciplinary truth.

## N4.2 Must-preserve Gesamtthese

> Historische Quellenerschließung wird als dynamischer Verbund voneinander abgegrenzter Fachkompetenzen verstanden, deren wissenschaftliche Leistungsfähigkeit nicht durch Disziplinlabels, sondern durch Gegenstands- und Quellenmodelle, Wissensgrundlagen, fachliche Operationen, Evidence Appetite, Inferenzgrenzen, Qualitäts- und Failure-Logik sowie explizite interdisziplinäre Handoff-/Return-Beziehungen bestimmt wird; welche Kompetenz führt oder kontrolliert, ist material-, frage-, claim- und evidenzabhängig. Der gegenwärtige Stand ist detailliertes Kompetenz-Scoping und muss profilweise gegen den jeweiligen fachlichen State of the Art sowie an positiven, negativen und adversarialen Fällen geprüft werden, bevor daraus Method Truth entstehen darf.

## N4.3 Relationale Quellenrolle

Der gleiche wissenschaftliche Aufsatz kann unterschiedliche Quellenrollen besitzen:

- für die Rekonstruktion mittelalterlicher Verhältnisse typischerweise Forschungsliteratur/Sekundärliteratur;
- für die Geschichte der Geschichtswissenschaft seiner Entstehungszeit selbst Primärquelle;
- Karte, Tabelle oder Rekonstruktion innerhalb des Aufsatzes zunächst Forschungsdarstellung, nicht automatisch unabhängige historische Evidenz;
- Fußnoten, Bibliographie, Editions- und Archivverweise als Quellen-/Retrieval-Router, nicht Ersatz für die referenzierte Evidenz.

Must-preserve relation:

`Quellenrolle = Material-/Dokumenttyp × Entstehungsfunktion × Überlieferungs-/Repräsentationsstufe × Forschungsfrage × beabsichtigter Claim`

Daraus folgt die Prüffrage: `Sekundärquelle wofür? Primärquelle wofür?`

Quelle, Edition/Reproduktion, konkrete Instanz/Digitalisat, Fundstelle, Beobachtung/Exzerpt und Finding/Interpretation bleiben getrennt.

## N4.4 Was eine operationalisierte Kompetenz beantworten können muss

Die aktuelle Analyse verlangt mindestens folgende 26 Dimensionen; sie sind Coverage-Fragen, noch keine SOTA-validierten Antworten:

1. Welche Problem-/Claimtypen bearbeitet sie?
2. Wann führt sie?
3. Wann kontrolliert sie?
4. Wofür ist sie nicht zuständig?
5. Welche Begriffe/Gegenstandsmodelle unterscheidet sie?
6. Welche Quellen-/Materialtypen versteht sie?
7. Wie entstehen diese Materialien/Evidenzen?
8. Was können sie beobachten?
9. Was können sie systematisch nicht beobachten?
10. Welche Preservation-/Detectability-Bedingungen gelten?
11. Welche fachlichen Operationen führt sie aus?
12. Welche Evidenz trägt welchen Claim?
13. Welche Inferenzen sind zulässig?
14. Welche Inferenzen sind ohne Zusatzbeleg verboten?
15. Welche Failure Modes/Overclaims kennt sie?
16. Wie behandelt sie Unsicherheit, Widerspruch und `unresolved`?
17. Welche Counterevidence/Kontrollen können schwächen oder falsifizieren?
18. Welche Search Language / Evidence Appetite besitzt sie?
19. Wann muss eine andere Kompetenz aktiviert werden?
20. Welche bounded Handoff-Frage geht hinaus?
21. Welcher Return / welche Evidenz muss zurückkommen?
22. Welche Terminologie-/Evidenz-Inkommensurabilitäten bestehen?
23. Welche Methodenliteratur/Standards/Forschungstraditionen müssen später tragen?
24. Was ist regelbasiert/technisch unterstützbar?
25. Was bleibt fachliches Urteil?
26. Wann ist externe qualifizierte Fachvalidierung erforderlich?

## N4.5 Vier analytische Schichten – keine Pipeline

**A – Identität / Überlieferung:** Bibliographie/Source Identity; Archivistik; Diplomatik und Editions-/Textkritik; Paläographie/Materialität.

**B – Text / Bedeutung / Forschung:** Quellenkritik; historische Philologie/Semantik; Hermeneutik/Argument; Historiographie.

**C – historische Realität / Gegenstandsdomänen:** problemabhängige Sachgeschichte; historische Geographie/Kartenkritik; Onomastik; Archäologie/material evidence.

**D – Suche / epistemische Integration:** historische Heuristik/IR; historische Epistemologie/Research Design; transdisziplinäres Expertise Routing.

Eintritt und Führung sind material-, frage-, claim- und evidenzabhängig. Keine Schicht ist ein fixer Workflow-Schritt oder epistemische Oberinstanz.

## N4.6 Aktuelle Analyseprofile

- **P1 Quellenkritik:** Entstehung, Funktion, Perspektive, Selektion, Überlieferung, Aussagepotenzial/-grenze; Schweigen nur bei begründeter Detectability; abhängige Publikationen/Quellen nicht als unabhängige Bestätigung zählen.
- **P2 Bibliographie / Source Identity:** `Werk → Ausgabe → Auflage → Band/Reihe → Beitrag → konkrete Instanz → Digitalisat → Fundstelle`; Dateiname/URL ≠ Identität; reproduzierbare konkrete Ausgabe/Instanz.
- **P3 Historiographie:** Autorenbeobachtung ≠ Autoreninterpretation ≠ damaliges Forschungsmodell ≠ spätere Rezeption ≠ heutiger Stand; ältere Forschung kann empirisch wertvoll und theoretisch überholt zugleich sein.
- **P4 Hermeneutik / Argument:** Aussage ≠ Beleg ≠ Schluss; Inferenzketten zerlegen; `Evidence | inference | assumptions | alternatives | confidence` getrennt halten.
- **P5 historische Philologie / Semantik:** keine zeitlose Wörterbuchbedeutung; historische Form/Lesung → Normalisierung → Übersetzung → moderner analytischer Begriff getrennt; Term-Rollen `source | contemporary institutional | editorial/archive | analytic | historiographic | search variant`.
- **P6a Diplomatik:** Genesis, Form, Funktion, Aussteller/Empfänger, Kanzlei/Formular, Datierung, Beglaubigung, Zeugen, Original/Kopie/Transsumpt/Fälschungsfragen; keine Authentizitäts-/Funktionsbehauptung aus Editionstext allein.
- **P6b Editionswissenschaft / Textkritik:** Textzeuge, Editionsbasis, Varianten, Apparat, editorische Ergänzungen, Regest/Identifikation; `Regest ≠ Urkunde`, `Edition ≠ Original`, `editorische Ergänzung ≠ historischer Wortlaut`, Register-ID ≠ Source-ID.
- **P7 Archivistik / Provenienz:** Provenienz, Registratur-/Bestandsbildung, Fonds, Ordnung/Umlagerung, Kassation/Verlust, Repertorien/Signaturgeschichte; Archivbestand ≠ Vergangenheit; `nicht gefunden ≠ nie vorhanden`.
- **P8 sachhistorische Domain-Expertise:** kein Sammellabel `Mediävistik` als Methode; jeweilige Gegenstands-/Relationsmodelle müssen unterscheiden, z. B. `Besitz ≠ Grundherrschaft ≠ Gericht ≠ Lehen ≠ Vogtei ≠ Patronat ≠ Abgabe ≠ Amt ≠ Territorialhoheit`; zeit- und evidenztypisierte Relationen.
- **P9 historische Geographie / Kartenkritik:** historischer Raum ≠ moderne Verwaltungsfläche; Grenzen können linear, zonal, strittig, funktional, saisonal oder nur punktuell belegt sein; `direkt belegt | rekonstruiert | interpoliert | candidate | unresolved`; Karte ist selbst quellenkritisch zu prüfen.
- **P10 Onomastik / Toponymie:** Namensähnlichkeit ≠ Identität; Form + Chronologie + Raum + institutioneller Kontext + Belegserie + konkurrierende Homonyme; `confirmed | candidate | competing | unresolved | rejected` möglich.
- **P11 Paläographie / Kodikologie / materielle Textanalyse:** `OCR ≠ Transkription ≠ Bild`; Schrift, Abbreviaturen, Hände, Material, Layout, Nachträge/Rasuren/Marginalien/Wasserzeichen und unsichere Zeichen müssen bewahrt werden.
- **P12 Archäologie / materielle Cross-Evidence:** `Ersterwähnung ≠ Entstehung`; `kein Fund ≠ Nichtvorhandensein`; Stratigraphie/Fundkontext/Typologie/Datierung/Taphonomie und Untersuchungs-/Erhaltungsbedingungen; materielle und schriftliche Evidenz zunächst getrennte Linien.
- **P13 historische Heuristik / IR:** fragen, wo etwas auffindbar wäre, wenn eine Hypothese zuträfe; Editionen/Regesten/Archive/Bibliographien/Schreibvarianten/Citation Chaining; `Treffer ≠ Evidenz`, `kein Treffer ≠ Abwesenheit`; negative Aussagen brauchen Search Boundary und domain-spezifische Evidence Appetite.
- **P14 historische Epistemologie / Inferenzkontrolle:** Unabhängigkeit, Triangulation, negative Evidenz, Kausalität/Abduktion/Vergleich, Uncertainty/Falsifikation; `Claim → Evidence → Method → Inference → Scope → Confidence/uncertainty → competing explanation → falsifier`; Widerspruch darf `unresolved` bleiben.
- **P15 Expertise Routing / Research Coordination:** Problem zerlegen, führende/kontrollierende Kompetenz erkennen, bounded Fragen routen, Konflikte/Unsicherheiten erhalten und zurückintegrieren; besitzt keine eigene historische Evidence-/Truth-Superauthority.

**P6-Grenze:** Diplomatik und Editions-/Textkritik sind eng gekoppelt, aber nicht identisch. Ob daraus ein oder mehrere spätere Domain Method Profiles entstehen, bleibt explizit `retain | split | merge | reframe` unter #60-SOTA; weder 15 noch 16 wird hier ontologisiert.

## N4.7 Schnittstellen als eigene methodische Objekte

Ein Handoff besteht mindestens aus:

`triggering observation → outbound domain → bounded question → evidence/context → terminology → preserved uncertainty → requested evidence/assessment → what receiver may confirm/refute/limit → incommensurabilities → return contract → downstream status`.

Beispielhafte, nicht-lineare Komposition:

Philologie liefert mögliche Lesungen/Varianten/semantische Grenzen → Onomastik beantwortet eine bounded Identitätsfrage mit Kandidaten/Ausschlüssen/Confidence/unresolved → historische Geographie prüft räumlich-chronologische Kompatibilität → Sachdomäne prüft institutionell-historische Konstellation → epistemische Integration hält `confirmed | candidate | competing | unresolved` auseinander.

Das ist kein fixer Ablauf und kein „consult X“-Pfeil.

## N4.8 Dynamische Aktivierung / Explorationstiefe

Für die erste Erschließung eines Fachaufsatzes sind typischerweise führend/kontrollierend: Quellenkritik, Historiographie, Hermeneutik/Argument, einschlägige Sachdomäne und – nur wenn räumlich relevant – historische Geographie.

Claim-getrieben werden weitere Kompetenzen aktiviert:

- Urkunde/Edition → Diplomatik / Editionskritik;
- Lesung → Paläographie / Philologie;
- Name → Onomastik;
- Überlieferungsweg → Archivistik;
- Siedlung/material → Archäologie;
- Raum → historische Geographie;
- Gesamtinferenz → historische Epistemologie.

Must-preserve Satz: **„Erschließen heißt zunächst noch nicht, jede Urkunde nachzuprüfen.“** Erste Erschließung rekonstruiert kompetent die wissenschaftlichen Operationen, Behauptungen, Evidenzarchitektur und notwendigen Fachprüfungen; tiefere Verifikation ist claim-getrieben.

## N4.9 Case-Rolle / Non-Promotions

Herrmann-/ähnliche konkrete Beispiele dürfen in diesem Source Lock nur als `case-derived competence activation / stress case` dienen, z. B. um zu zeigen, wann Quellenkritik, Historiographie, Hermeneutik, Domain History, Raumkritik, Onomastik, Diplomatik/Edition, Archivistik/Philologie, Archäologie oder Epistemologie aktiviert würden. Sie werden nicht zu historischen Findings reaktiviert.

Nach erfolgreicher Persistenz bleiben ausdrücklich offen:

- Domain-SOTA / Methodenliteratur / Standards;
- Profilgrenzen und Split/Merge/Reframe;
- positive, Counterexample-, evidence-starved und adversariale Methodentests;
- externe qualifizierte Fachvalidierung, wo später fachlich erforderlich;
- jede Requirement-/Architecture-Ableitung bis zum zuständigen Owner-Gate.
