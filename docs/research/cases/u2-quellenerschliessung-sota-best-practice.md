# U2 / Orlagau – SOTA und Best Practice der quellenzentrierten Erschließung

**Status:** `working-research / method-sota / requirement-candidate-source`  
**Work Owner:** #46  
**Methodische Owner/Schnittstellen:** #45 Research Protocol, #22 Kompetenzlandkarte  
**Requirements-Schnittstelle:** #41/#42; keine automatische Promotion aus einem Einzel-Live-Fall  
**Stand:** 2026-08-31

## 1. Ausgangsfrage

Für Histo-Orla ist die erste Aufgabe bei einer Quelle nicht, sofort eine vollständige historische Erklärung zu bauen. Die erste Aufgabe lautet:

> **Was steht in der Quelle, welche quellennahe Beobachtung lässt sich daraus erheben, welche analytischen Anschlussmöglichkeiten eröffnet sie, und welche davon rechtfertigen erst anschließend eine Erweiterung des Research Scope?**

Die Quelle wird deshalb nicht als „Faktencontainer“, aber ebenso wenig als fertige Lebenswelt-Rekonstruktion behandelt. Sie ist ein historisch erzeugtes Kommunikations-/Handlungsobjekt mit Wortlaut, Form, Funktion, Akteuren, Rollen, Voraussetzungen, Auslassungen und Überlieferungskontext. Spätere Fachanalysen dürfen daran anknüpfen, ohne ihre Interpretation rückwirkend in den Quellentext einzuschreiben.

## 2. SOTA-Synthese für die Zielsetzung von Histo-Orla

Es gibt keinen einzelnen universellen Standard, der Quellenkritik, Diplomatik, historische Hermeneutik, Digital Scholarly Editing, Annotation, Wissensmodellierung und Argumentationsprovenienz vollständig vereint. Der belastbare State of the Art ist vielmehr **kompositional**:

1. **klassische/neuere Quellenkritik und Diplomatik** sichern Entstehung, Form, Funktion, Überlieferung, Rechts-/Sozialhandlung, Akteure und Dokumentkontext;
2. **Pragmatik/pragmatische Schriftlichkeit** behandelt Schrift nicht nur als Informationsspeicher, sondern als Teil zweckgerichteten gesellschaftlichen Handelns;
3. **Digital Scholarly Editing / TEI** hält Text, editorische Intervention, Identifikation, Unsicherheit, Verantwortlichkeit und analytische Annotation unterscheidbar; Stand-off Annotation erlaubt überlappende und später ergänzbare Analyseschichten;
4. **W3C Web Annotation / IIIF** trennt die konkrete Zielstelle im Text/Bild vom Inhalt und Zweck einer Annotation und erlaubt, Annotationen später zu ergänzen, auszutauschen oder anders zu gruppieren;
5. **event-/kontextorientierte Cultural-Heritage-Modelle wie CIDOC CRM** integrieren heterogene Befunde über Ereignisse, Akteure, Orte, Dinge und Zeit, ohne aus bloßer Ko-Präsenz bereits Kausalität zu machen;
6. **Argumentations-/Inference-Modelle wie CRMinf** unterscheiden beobachtete bzw. vorausgesetzte Aussagen, Schlusslogik und daraus abgeleitete Überzeugungen/Claims und machen Revisionsabhängigkeiten nachvollziehbar.

Für Histo-Orla folgt daraus **nicht**, dass all diese Standards technisch sofort implementiert werden müssen. Sie bilden den methodischen Referenzrahmen, gegen den die kleinste hinreichende Forschungs- und Datenpraxis geprüft wird.

## 3. Zentraler Grundsatz: hidden layers sind analytische Potentiale, keine versteckten Wahrheiten

Im Text liegen oft mehr nutzbare Signale als der aktuelle Forschungsauftrag zunächst abfragt: Rollen, Abhängigkeiten, Handlungsvoraussetzungen, Ressourcen, räumliche Bezüge, religiöse Semantik, Familienbezüge, Konfliktindikatoren, normative Sprache, institutionelle Interessen oder Gattungsbias.

Diese Ebenen sind aber nicht automatisch bereits „Befunde“ oder „Erklärungen“.

Zu trennen sind mindestens:

```text
Quellenwortlaut / sichtbares Merkmal
→ quellennahe Beobachtung
→ Normalisierung / Identifikation
→ analytische Annotation / research hook
→ Hypothese / konkurrierende Deutung
→ cross-source Finding
→ Claim / Synthese
```

Eine gute Erschließung bewahrt genügend Material, damit spätere Fachfragen möglich bleiben, ohne beim ersten Lesen jede denkbare Fachinterpretation vorwegzunehmen.

Leitformel:

> **Minimum notwendiger Vorinterpretation, Maximum an späterer Wiederverwendbarkeit und Revidierbarkeit.**

## 4. Best-Practice-Workflow: source-local first, scope expansion second

### Pass A – Quellen- und Instanzsicherung

Zuerst wird eindeutig geklärt:

- welche Quelle / Überlieferungsstufe / Edition vorliegt;
- welche konkrete Instanz inspiziert wurde;
- exakte Fundstelle;
- Text-/Bild-/Seitenbezug;
- Original, Kopie, Edition, Regest, editorischer Apparat;
- relevante editorische Eingriffe.

Kanonisch: `docs/research/source-identity-protocol.md`.

### Pass B – quellennahe Erschließung

Der relevante Abschnitt wird so weit gelesen, dass seine dokumentarische Funktion und sein Sinnzusammenhang nicht zerstört werden. Erhoben werden nur Dinge, die am Stück selbst beobachtbar oder als editorische Information explizit vorhanden sind.

Mögliche Beobachtungslinsen – **nicht als Pflichtformular, sondern als Notice Checklist**:

- Text-/Formebene: Gattung, Aufbau, Formel, Narratio, Dispositio, Sanktion, Zeugen, Datierung;
- Akteure/Rollen: Aussteller, Empfänger, Begünstigte, Zustimmende, Vermittler, Zeugen, erwähnte Gruppen;
- Handlung: schenken, verkaufen, verzichten, bestätigen, streiten, schlichten, versetzen, versorgen, gründen, verlegen usw.;
- Rechte/Pflichten/Ressourcen: Besitz, Abgaben, Dienste, Zehnt, Patronat, Gericht, Vogtei, Mühle, Wasser, Wald, Wiese, Wege etc.;
- Beziehungshinweise: Ehe, Verwandtschaft, Haushalt, Lehen, Amt, geistliche Zugehörigkeit, Memorialbezug;
- Raum/Zeit: Orte, räumliche Relationen, Grenzen, Wege, Verlagerungen, zeitliche Sequenzen;
- soziale/religiöse/pragmatische Signale: Bedürftigkeit, Schutz, Memoria, Frömmigkeit, Konflikt, Zustimmung, Zwang, Gegenleistung, Versorgung;
- Quellengattungs-Bias: wessen Stimme wird dokumentiert, wessen Praxis vermutlich nicht, was ist formelhaft, was ungewöhnlich?

Wichtig: Ein leeres Feld ist kein Defizit. Wenn ein Aspekt in der Quelle nicht vorkommt oder nicht beurteilt werden kann, bleibt er `not-assessable`.

### Pass C – Status jeder Annotation

Jede substantielle Annotation soll erkennen lassen, was sie epistemisch ist:

```text
source-explicit
editorial-explicit
source-structural / source-implied
normalization-candidate
identification-candidate
research-question
hypothesis-hook
interpretive-hypothesis
```

Interpretation und Hypothese dürfen nicht denselben Status wie beobachteter Wortlaut erhalten.

### Pass D – Anschlusswert / Expertise Routing

Erst danach wird gefragt:

> Wer kann mit dieser Beobachtung später fachlich etwas anfangen?

Eine Beobachtung kann mehrere Anschlussdomänen haben, z. B.:

- `nimia paupertas` → Diplomatik/Formelprüfung; Kloster-/Kirchengeschichte; Wirtschafts-/Versorgungsgeschichte; Sozial-/Gendergeschichte; historische Geographie; ggf. Umwelt-/Krisengeschichte;
- eine Zeugenliste → Prosopographie/Netzwerk; Herrschafts-/Ministerialitätsgeschichte; Mobilität; Diplomatik;
- `uxor`, `consensu uxoris`, Dotal-/Erbklausel → Familien-/Gender-/Rechts-/Besitzgeschichte;
- `molendinum`, `aqua`, `piscaria`, `pratum` → Wirtschafts-/Agrar-/Umwelt-/Landschaftsgeschichte.

Das Routing erzeugt zunächst **research hooks**, nicht automatisch einen neuen Voll-Scope.

### Pass E – agile Scope-Entscheidung

Scope wird erweitert, wenn mindestens eines gilt:

1. eine neue Beobachtung ist für die Kernfrage diskriminierend;
2. eine aktivierte Fachdomäne kann eine relevante konkurrierende Erklärung prüfen;
3. der Befund wiederholt sich seriell und könnte ein Muster bilden;
4. eine Widersprüchlichkeit oder Unsicherheit verlangt Kontrollüberlieferung;
5. ein materieller/räumlicher/archäologischer Befund könnte eine textliche Deutung bestätigen oder falsifizieren.

Dann entsteht ein gezielter Folgeauftrag. **Nicht jede denkbare Disziplin wird bei jeder Quelle voll ausgerollt.**

### Pass F – iteratives Re-Reading

Neue Quellen, Literatur oder materielle Befunde dürfen frühere Texte erneut relevant machen. Deshalb muss die Erschließung erweiterbar sein:

```text
Quelle
→ erste Annotationen
→ neue Hypothese / Fachfrage
→ Rückkehr zur Quelle
→ zusätzliche Annotation
```

Die frühere Annotation bleibt mit Autor/Verantwortung, Status und Zeitpunkt nachvollziehbar; sie wird nicht still überschrieben.

## 5. Kernmodell für eine einzelne quellennahe Annotation

Das methodisch minimale, aber leistungsfähige Modell ist nicht eine riesige Faktentabelle, sondern eine **zielstellengebundene, typisierte Annotation**.

```text
annotation_id
target_excerpt_or_span
source_id / excerpt_id
annotation_type
observation_or_note
status
responsible_agent
method_or_lens
certainty / unresolved state
source_or_editor_basis
related_entity_candidates
related_question_or_hypothesis (optional)
downstream_disciplines (optional)
created / revised
```

Für Bildquellen/Karten/Handschriften muss `target_excerpt_or_span` auch eine Seiten-/Bildregion sein können.

### Warum Stand-off statt „alles in den Text schreiben“?

Mehrere Fachlesarten können dieselbe Passage überlappend analysieren. Beispielsweise kann dieselbe Klausel zugleich eine Rechts-, Gender-, Ressourcen- und Memoriarelevanz besitzen. Stand-off Annotation hält diese Lesarten getrennt, ohne den Quellentext zu verändern oder auf eine einzige Taxonomie festzulegen.

## 6. Was beim ersten Lesen bewusst NICHT verlangt werden sollte

Nicht Best Practice sind:

- sofortige Vollrekonstruktion der Lebenswelt aus einem Einzeltext;
- Pflichtbefüllung einer riesigen transdisziplinären Matrix bei jeder Quelle;
- Hypothesen als Textmerkmale zu speichern;
- jede mögliche Fachdomäne präventiv zu aktivieren;
- einen einmal festgelegten Scope als endgültig zu behandeln;
- stillschweigend aus `nicht erwähnt` → `nicht vorhanden` zu schließen;
- aus Formularsprache unmittelbar individuelle Motivation abzuleiten;
- eine spätere Interpretation zurück in die Transkription/Edition zu schreiben.

## 7. Was beim ersten Lesen sehr wohl bewahrt werden sollte

Für die Zielsetzung von Histo-Orla ist das optimale Verhältnis:

### Pflichtkern

- ausreichender Wortlaut/Kontext;
- genaue Fundstelle;
- dokumentarische Funktion/Quellengattung;
- explizite Akteure, Rollen, Handlung, Objekte/Rechte/Pflichten;
- explizite Begründungen/Motive;
- auffällige Formeln oder ungewöhnliche Formulierungen;
- editorische Eingriffe/Identifikationen;
- Unklarheiten und Alternativen.

### leichte Anschlussannotation

- `relevant_for`: Fachdomänen/Fragen;
- `research_hook`: warum diese Stelle später wichtig sein könnte;
- `scope_trigger`: ja/nein/noch unklar;
- `next_discriminating_source`: falls unmittelbar erkennbar.

Damit bleibt die Erstaufnahme schlank, aber sie verliert die später wichtigen Türen nicht.

## 8. Beispiel Triptis 1212

Die quellennahe Erschließung von `ob nimiam paupertatem, quam patiebantur ibidem` soll zunächst nur sichern:

- Wortlaut und Fundstelle;
- `nimia paupertas` als explizite Begründung der Verlegung;
- der Konvent ist von dieser Armut betroffen;
- Verlegung Triptis → Zwickau;
- neue kirchliche Einkünfte dienen der `sustentatio`;
- beteiligte weltliche/kirchliche Akteure und ihre Rollen;
- Gattung/Formel-/Überlieferungskontext.

Dann werden Research Hooks angelegt:

```text
FORMULA?        Ist `nimia paupertas` individuell oder gattungstypisch?
ECONOMY?        Welche konkrete Ausstattung/Versorgung fehlte?
INSTITUTION?    Welche Rechts-/Ordensform hatte der Konvent?
GENDER/SOCIAL?  Welche Versorgungs- und Familienlogiken betrafen die Frauen?
SPACE?          Welche Standort-/Markt-/Ressourcenbedingungen unterschieden Triptis und Zwickau?
CRISIS?         Gibt es überhaupt unabhängige Hinweise auf lokale Krise/Umweltstress?
POLITICS?       Welche Interessen hatte der Markgraf an der Verlegung?
```

Keine dieser Fragen ist durch die Klausel selbst beantwortet. Sie begründen nur mögliche iterative Scope-Erweiterungen.

## 9. Anschluss an einschlägige Standards / Best Practices

### TEI P5

Die aktuellen TEI-P5-Guidelines unterstützen genau die für Histo-Orla wichtigen Trennungen:

- `standOff` für verknüpfte Daten, Kontextinformationen und Stand-off-Annotationen;
- `cert` / `certainty` für Unsicherheit;
- `resp` für Verantwortlichkeit;
- `source` für die Grundlage einer Annotation/Intervention;
- strukturierte Personen-/Orts-/Organisationsdaten und Relationen;
- explizite Annotationselemente in Anlehnung an das Web Annotation Data Model.

Referenz: TEI P5 4.12.0, insbesondere Kapitel 14, 17 und 22.  
https://www.tei-c.org/release/doc/tei-p5-doc/en/html/

### W3C Web Annotation

Das Modell trennt `target` (worauf bezieht sich die Annotation?) von `body` (was wird darüber gesagt?) und führt `motivation`, `creator`, Lifecycle und selektierbare Segmente. Das ist konzeptionell sehr passend für source-bound Findings, Fragen, Identifikationen und Fachannotation.

https://www.w3.org/TR/annotation-model/

### IIIF Presentation API

Für bildbasierte Quellen erlaubt IIIF Annotationen auf ganze Seiten/Canvases oder konkrete Regionen. OCR/Transkription kann als abgeleitete/supplementierende Ressource mit dem Bild verbunden werden, ohne mit ihm gleichgesetzt zu werden.

https://iiif.io/api/presentation/3.0/

### CIDOC CRM

CIDOC CRM ist ein event-zentrierter Integrationsstandard für heterogene kulturhistorische Information. Relevant ist besonders die Möglichkeit, Ereignisse, Akteure, Orte, Dinge und Zeit zu verbinden, ohne aus Beteiligung automatisch eine Kausalbeziehung abzuleiten.

https://cidoc-crm.org/

### CRMinf

CRMinf ergänzt CIDOC CRM um Argumentation/Inference. Die aktuelle Fassung erlaubt, Schlussfolgerungen auf Prämissen und angewandte Inferenzlogik zurückzuverfolgen; das passt zu der Histo-Orla-Trennung `Observation → Interpretation/Hypothesis → Claim`, ohne dass Histo-Orla CRMinf vollständig übernehmen muss.

https://cidoc-crm.org/crminf/

## 10. Methodische Requirement Candidates aus diesem SOTA-Abgleich

Diese Punkte sind **Candidates**, keine neue Requirements-Baseline:

### RC-U2-19 – Source-bound modular annotation

Quellennahe Beobachtungen müssen an konkrete Text-/Bildsegmente gebunden und als eigenständige, später erweiterbare Annotationen geführt werden können.

### RC-U2-20 – Observation vs research hook

Das System muss beobachteten Quelleninhalt von fachlichem Anschlusswert (`research hook`) und Hypothese unterscheiden können.

### RC-U2-21 – Iterative scope trigger

Ein Quellenbefund muss neue fachliche Fragen bzw. Scope-Erweiterungen auslösen können, ohne den ursprünglichen Research Scope still umzuschreiben.

### RC-U2-22 – Multi-lens without overwrite

Mehrere Fachdomänen müssen dieselbe Passage mit überlappenden, getrennt verantworteten Annotationen analysieren können, ohne eine kanonische Einzelinterpretation zu erzwingen.

### RC-U2-23 – Revision-preserving re-reading

Spätere Re-Readings müssen frühere Annotationen ergänzen, revidieren oder widersprechen können, ohne deren Provenienz und damaligen Status zu verlieren.

### RC-U2-24 – Source-local capture before cross-source synthesis

Der Forschungsworkflow muss die quellennahe Erschließung vor cross-source Pattern-/Motiv-/Lebenswelt-Synthese halten und deren epistemische Stufen sichtbar trennen.

## 11. Praktische Definition of Done für eine erstklassig erschlossene Quelle

Eine Quelle ist für den aktuellen Arbeitsstand hinreichend erschlossen, wenn:

- [ ] Quelle/Instanz/Fundstelle sicher identifiziert sind;
- [ ] ausreichender Original-/Editionskontext erhalten ist;
- [ ] explizite Akteure, Rollen, Handlung, Gegenstände/Rechte/Pflichten und Begründungen erfasst sind, soweit vorhanden;
- [ ] editorische Eingriffe/Normalisierungen sichtbar getrennt sind;
- [ ] wichtige quelleninterne Strukturen/Formeln/Biases zumindest als Notice festgehalten sind;
- [ ] unsichere Identifikationen/Lesarten als solche markiert sind;
- [ ] relevante spätere Fachanschlüsse als Research Hooks markiert werden können;
- [ ] Hypothesen nicht mit Beobachtungen vermischt sind;
- [ ] ein Scope-Trigger begründet werden kann, wenn weitere Recherche nötig ist;
- [ ] ein späterer Forscher die Quelle erneut lesen und zusätzliche Analysen ergänzen kann, ohne den ursprünglichen Befund rekonstruieren zu müssen.

## 12. Konsequenz für den laufenden U2-Quellenlauf

Der aktuelle Live-Fall sollte daher nicht in Richtung einer immer größeren Pflichtmatrix pro Urkunde wachsen. Stattdessen gilt:

```text
sauberes, kontextreiches Exzerpt
+ source-bound Beobachtungen
+ leichte multidisziplinäre Research Hooks
+ explizite Hypothesen-/Scope-Trigger
→ nur bei Bedarf tieferes Situationsdossier / weitere Evidenzklassen
```

Das vorhandene `u2-transdisziplinaere-rekonstruktionsmatrix.md` bleibt für die **zweite Ebene** sinnvoll: wenn ein Befund tatsächlich eine transdisziplinäre Rekonstruktionsfrage eröffnet. Es soll nicht zum Pflichtschema jeder Quellenaufnahme werden.
