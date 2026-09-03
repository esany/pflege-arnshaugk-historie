# #60 Method Learning – Sachenbacher Clean-Room-Test 2026-09-03

**Status:** `method_hypothesis / live-test-supported / not-promoted`  
**Work Owner:** #60  
**Related historical owner:** #46  
**Protocol:** #45, `docs/research/source-identity-protocol.md`, `docs/research/methods/domain-method-profile-contract.md`  
**Stand:** 2026-09-03  
**Branch:** `research/sachenbacher-clean-room-20260903`

---

## 1. Warum dieses Methodenlearning existiert

Der Clean-Room-Test prüfte nicht nur eine historische Frage, sondern eine Fähigkeit: Ein domänenfremder Research Owner soll komplexe historische Quellen und Literatur bereitstellen können, ohne selbst die nötigen Disziplinen, Begriffe, Methoden, Evidenztypen und Aussagegrenzen vorzugeben.

Der Test mit Peter Sachenbachers *Thüringen östlich der Saale im Mittelalter* zeigt eine konkrete Methodenkandidatur für #60: **Integration eines interdisziplinären Überblickswerks in einen laufenden quellenkritischen Research-State**.

Dieses Dokument ist kein neues validiertes Domain Method Profile. Es ist ein live-use-case-basiertes Methodenlearning und muss vor Promotion gegen SOTA und weitere Fälle geprüft werden.

---

## 2. Beobachteter Failure Mode

Ein interdisziplinäres Überblickswerk erzeugt schnell plausible Synthesen. Für Histo-Orla ist das gefährlich, wenn die KI:

- das Modell der Publikation als historische Wahrheit übernimmt;
- aus `slawischer Keramik` unmittelbar ethnische Identität ableitet;
- `Orlagau` als stabile Ontologie statt als quellen-/historiographieabhängigen Raumbegriff behandelt;
- Ortsname, Siedlung, Herrschaft, Kirche, Bevölkerung und Wüstung verschmilzt;
- einen Einzelort wie Ranis zum primären Erkenntniszentrum macht, obwohl der Research Owner das Gesamtmodell prüfen will;
- `Knau`-Treffer aus dem Altenburger Land in den Orla-Kontext verschiebt;
- aus `kein Treffer` historische Abwesenheit macht;
- Literaturrouter so zusammenfasst, dass die nächste Fachperspektive keinen Zugriff mehr auf Originalpassage, Druckseite, Fußnote und Quellenidentität hat.

---

## 3. Methodenkandidat: Sekundärwerksintegration in zwei Arbeitsmodi

### 3.1 Claim-/Slice-Modus

Der erste Durchlauf zeigte einen sinnvollen Minimalmodus für begrenzte Befundprüfung:

```text
0. Repo-Bootstrap lesen
1. Source-/Instance-Identität der Publikation anlegen
2. Bauart des Werkes rekonstruieren
3. Relevante Histo-Frage gegen bestehenden Research-State bestimmen
4. diskriminierenden Research Slice wählen
5. Pro Sachenbacher-Befund A–J prüfen
6. Fachperspektiven substantiell aktivieren
7. Bestehende Findings dispositionieren
8. Source-/Literatur-/Suchhooks sichern
9. Methodenlearning statusklar nach #60 zurückspielen
10. Handoff-Check durchführen
```

Dieser Modus ist nützlich, wenn ein einzelner Befundkomplex bearbeitet werden soll. Er kann aber den Schwerpunkt falsch setzen, wenn ein Überblickswerk selbst ein kausales/chronologisches Gesamtmodell anbietet.

### 3.2 Model-Check-Modus

Die Owner-Korrektur zeigt einen zweiten, für interdisziplinäre Synthesen notwendigen Modus:

```text
Sekundärmodell
→ Modellannahmen
→ erwartbare Evidenzmuster
→ von der Publikation selbst mobilisierte Orts-/Raum-/Quellenmatrix
→ Passung / Widerspruch / Lücke
→ konkurrierende Erklärung
→ konkrete Source-Resolution-Aufträge
→ Disposition des bestehenden Histo-Research-State
```

Dieser Modus ist für Sachenbachers Orlagau-Kapitel geeigneter als ein einzelner Ranis-Slice, weil das Erkenntnisinteresse nicht ein Ort, sondern die Prüfbarkeit des Landesausbaumodells gegen sein Orts-, Raum- und Evidenzmaterial ist.

### 3.3 Bauartrekonstruktion bleibt Pflicht, aber nicht Endprodukt

Für Überblickswerke muss zuerst geklärt werden:

- Gesamtfrage und zentrale Modelle;
- räumlich-zeitlicher Zuschnitt;
- welche Disziplin welche Argumentteile trägt;
- wo Primärquelle, Edition, Grabung, Onomastik, ältere Forschung oder eigene Synthese vorliegt;
- welche Kontroversen und ältere Begriffe mitschwingen;
- welche Teile den aktuellen Research-State tatsächlich berühren.

Danach muss entweder ein Claim-/Slice-Modus oder ein Model-Check-Modus ausgeführt werden. Eine reine Publikationsanalyse ist nicht ausreichend.

---

## 4. Claim-Prüfung A–J bleibt als lokale Prüfung gültig

A. Was sagt die Publikation genau?  
B. Exakte Druckseite und Fußnote?  
C. Eigener Befund, Synthese, Modell, Übernahme oder Interpretation?  
D. Welche Primärquelle, Edition, Grabungspublikation oder Fachliteratur nennt sie?  
E. Ist diese Referenz identifiziert und möglichst direkt überprüft?  
F. Welche Fachkompetenz beurteilt welchen Teil?  
G. Was erlaubt die Evidenz tatsächlich zu behaupten?  
H. Was wäre Overclaim?  
I. Gibt es konkurrierende Modelle oder neueren Forschungsstand?  
J. Was ändert sich im bestehenden Histo-Research-State?

Im Model-Check-Modus wird A–J nicht nur auf Einzelpassagen, sondern auf Modellannahmen angewandt. Besonders B, C, D und E verhindern, dass eine Sekundärsynthese unbemerkt Primärquellenstatus erhält.

---

## 5. Domain-Aktivierung: nicht Rolle, sondern Evidenzlogik

Im Sachenbacher-Modellcheck genügt keine Rollenprosa. Jede aktivierte Fachperspektive kontrolliert eine andere Evidenzachse:

| Fachperspektive | Führt/kontrolliert | Darf behaupten | Darf nicht behaupten |
|---|---|---|---|
| Archäologie / Mittelalterarchäologie | Fundkontext, Stratigraphie, Keramik, Bau-/Wallanlage, Datierung, Grabungslücke, Altfundqualität | materielle Präsenz, Datierungsrahmen, Befund-/Fundtyp, funktionale Hypothesen | Ethnie, Ortsname, politische Herrschaft oder Kontinuität ohne Zusatzbeleg |
| Diplomatik / Mediävistik | Urkunde, Regest, Edition, Datierung, Rechtsgeschäft, Grenzbeschreibung, Zeugen, Überlieferung | quellenförmige Personen-, Rechts-, Besitz-, Herrschafts- oder Raumbeziehung | Gründung, Bevölkerung, Siedlungsanfang, tatsächliche Grenzgeometrie oder materielle Nutzung ohne Zusatzbeleg |
| Herrschafts-/Rechts-/Ministerialitätsgeschichte | Dienstrecht, Pfalz/Burg/Kloster, Dienstmannschaft, lokale Machtträger, Saalfeld/Köln/Mainz/Staufer/Lobdeburg/Vögte | institutionelle und rechtliche Einordnung mit Reichweite der jeweiligen Quelle | territoriale Zuständigkeit über alle Nachbarorte oder Bevölkerungskontrolle ohne Beleg |
| Kirchengeschichte | Archidiakonat, Sedessprengel, Pfarrei, Inkorporation, Patrozinien, Kirchenbau, Klosterlandschaft | kirchliche Organisationsachsen und Rechte | vollständige Christianisierung, Ortsgründung oder Pfarreigrenze ohne Quellenbasis |
| Onomastik | historische Namensform, Sprachschicht, Deutung, Varianten, Lokatoren-/Gewässernamen | sprachliche Herkunft/Deutung mit Unsicherheit | Ethnizität, Gründungsdatum, Ortskontinuität oder Herrschaft |
| Historische Geographie | Raumbegriff, Wege, Lage, Gewässer, Grenzpunkte, Zentralort/Umland, Siedlungsgunst | raumbezogene Hypothesen und Suchraumbegründung | zeitlose Polygon-Grenze oder einheitliche Raumontologie ohne Quellen-/Kartierungsbasis |

---

## 6. Model-Check-Schutzmatrix für Siedlungs- und Raumgeschichte

Für die Orla-/Knau-Forschung muss bei jedem Befund getrennt bleiben:

```text
archäologische Präsenz
≠ materielle Kultur
≠ ethnische oder sprachliche Zuschreibung
≠ Ortsnamenschicht
≠ politische Herrschaft
≠ kirchliche Organisation
≠ Siedlungsplatz
≠ Ortskontinuität
≠ urkundliche Ersterwähnung
≠ Wüstung / Nutzungsende
```

Der Sachenbacher-Modellcheck liefert konkrete Testfälle:

- Saalfeld: frühe Zentralität ≠ pauschale Kontrolle jedes späteren Orlagau-Ortes.
- Grenzbeschreibung 1071: spätere Kopie/Fälschungsdiskussion ≠ unmittelbare zeitgenössische Polygon-Grenze.
- Weltwitz: mittelslawische Keramik + slawisch gedeuteter Ortsname ≠ slawische politische Autonomie oder Siedlungskontinuität.
- Kirchenorganisation: 1071 genannte Pfarrkirchen/Inkorporation ≠ vollständige Christianisierung jeder lokalen Gruppe.
- Zwackau/Chursdorf: späte Ersterwähnung ≠ spätes Bestehen; Kirchen-/Ortsformdaten separat prüfen.
- Knau: Treffer `Knau, Ot. von Zetscha` ≠ Knau bei Neustadt/Orla.

---

## 7. Lossless-by-reference Übergaben

Für interdisziplinäre Weiterarbeit darf die KI keine Flüsterpost erzeugen. Jeder Fachblick benötigt weiterhin Zugriff auf:

- Originalpassage oder exakte publizierte Fundstelle;
- Druckseite und Fußnote;
- Modellbaustein oder Einzelclaim;
- Quellen-/Literaturidentität;
- Überlieferungs-/Instanzstatus;
- Suchboundary und Unsicherheit;
- konkurrierende Deutungen;
- Disposition vorhandener Histo-Findings.

Praktische Struktur des Model-Checks:

```text
Sachenbacher model passage
→ print page / footnote
→ model assumption
→ expected historical pattern
→ place/evidence row
→ fit/gap/contradiction
→ competing explanation
→ #46 finding disposition
→ source/source-ledger hook
→ method-learning candidate (#60)
```

---

## 8. Promotionsblocker für #60

Dieser Methodenkandidat darf noch nicht als `working-method` gelten, weil:

1. Die relevanten Spezialstudien und Primär-/Editionsquellen wurden nur teilweise identifiziert und noch nicht direkt kollationiert.
2. Die DDE/OATbyCO-HTML-Instanz zeigt nicht in allen Passagen alle Seitenumbrüche/Footnote-Texte so, dass externe Druckzitation ohne Bild-/Druckkontrolle sicher wäre.
3. Für Archäologie, Onomastik, historische Raumrekonstruktion und Kirchengeschichte fehlen noch vollständige Domain Method Profiles mit SOTA-gestützten Inferenzverträgen.
4. Der Modellcheck ist ein Einzelfall; weitere Sekundärwerke, echte Primärquellen und Gegenbeispiele müssen folgen.
5. Die Orts-/Chronologiematrix ist noch ein `bounded systematic pass`, keine vollständige wissenschaftliche Gazetteer-/Prosopographie-/Archäologiedatenbank.

Status bleibt daher:

```text
method_hypothesis / live-test-supported / not-promoted
```

---

## 9. Konkrete nächste Methodenarbeit

1. Ein Domain Method Profile `Siedlungsgeschichte / historische Raumrekonstruktion` entwerfen, aber erst nach SOTA-Check.
2. Ein Profil oder Subprofil `Archäologische Sachkultur und Ethnizität im Mittelalter` gegen Brather und neuere Debatte prüfen.
3. Ein Profil `Kirchenorganisation / Pfarrorganisation / Patrozinien / Archidiakonate` anhand Bünz und einschlägiger Kirchenverfassungsgeschichte prüfen.
4. Ein Profil `Onomastik als Evidenzachse` mit strikter Trennung von Namendeutung, Siedlungsphase, Ethnizität und Herrschaft ausarbeiten.
5. Ein Methodenbaustein `Sekundärliterarische Kausalmodelle prüfen` entwickeln: Modell → erwartbares Muster → Ort/Evidenz → Passung/Widerspruch/Lücke → konkurrierende Erklärung.
6. Für Raumbegriffe ein Terminology-Provenance-Template operationalisieren: `source term | source-defined relation | historiographical reconstruction | research search space`.

---

## 10. Übergabe an #46

Die historische Ausführung dieses Methodenlearning liegt in:

- `docs/research/cases/u2-sachenbacher-2022-landesausbau-model-check.md` – aktueller Schwerpunkt: Landesausbaumodell, Orlagau-Raumbegriffe, Orts-/Chronologiematrix.
- `docs/research/cases/u2-sachenbacher-2022-clean-room-slice.md` – erster, Ranis-lastiger Testlauf; weiterhin Referenz, aber nicht mehr primäre Leseführung.
- `docs/research/cases/orlagau-source-ledger-sachenbacher-2022-delta.md` – Source-/Literature-Ledger-Delta.

Dieses Methodenlearning darf nicht allein als historischer Befund gelesen werden. Historische Truth bleibt bei #46 und dessen Research-Artefakten.