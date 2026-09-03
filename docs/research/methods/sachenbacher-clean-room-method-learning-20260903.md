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

- Sachenbachers Modell als Wahrheit übernimmt;
- aus `slawischer Keramik` unmittelbar ethnische Identität ableitet;
- `Orlagau` als stabile Ontologie statt als quellen-/historiographieabhängigen Raumbegriff behandelt;
- Ortsname, Siedlung, Herrschaft, Kirche und Bevölkerung verschmilzt;
- `Knau`-Treffer aus dem Altenburger Land in den Orla-Kontext verschiebt;
- aus `kein Treffer` historische Abwesenheit macht;
- Literaturrouter so zusammenfasst, dass die nächste Fachperspektive keinen Zugriff mehr auf Originalpassage, Fußnote und Quellenidentität hat.

---

## 3. Methodenkandidat: Sekundärwerks-Integration als Research Slice

### 3.1 Minimaler Ablauf

```text
0. Repo-Bootstrap lesen
1. Source-/Instance-Identität der Publikation anlegen
2. Bauart des Werkes rekonstruieren
3. Relevante Histo-Frage gegen bestehenden Research-State bestimmen
4. Ersten diskriminierenden Research Slice wählen
5. Pro Sachenbacher-Befund A–J prüfen
6. Fachperspektiven substantiell aktivieren
7. Bestehende Findings dispositionieren
8. Source-/Literatur-/Suchhooks sichern
9. Methodenlearning statusklar nach #60 zurückspielen
10. Handoff-Check durchführen
```

### 3.2 Bauartrekonstruktion ist Pflicht, aber nicht Endprodukt

Für Überblickswerke muss zuerst geklärt werden:

- Gesamtfrage und zentrale Modelle;
- räumlich-zeitlicher Zuschnitt;
- welche Disziplin welche Argumentteile trägt;
- wo Primärquelle, Edition, Grabung, Onomastik, ältere Forschung oder eigene Synthese vorliegt;
- welche Kontroversen und ältere Begriffe mitschwingen;
- welche Teile den aktuellen Research-State tatsächlich berühren.

Diese Analyse allein genügt nicht. Sie muss in einen ausgeführten Slice übergehen, der den bestehenden Research-State ändert, begrenzt, bestätigt oder offen lässt.

### 3.3 Claim-Prüfung A–J

Der Test bestätigt die vom Nutzer vorgegebene A–J-Struktur als praktikables Gate:

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

Methodisch wichtig: B und D dürfen nicht nur formal ausgefüllt werden. Wenn die Fußnote nicht vollständig auflösbar ist, bleibt der Referenzstatus `unresolved`, selbst wenn die Synthese plausibel wirkt.

---

## 4. Domain-Aktivierung: nicht Rolle, sondern Evidenzlogik

Im Sachenbacher-Slice genügte keine Rollenprosa. Jede aktivierte Fachperspektive musste eine andere Evidenzachse kontrollieren:

| Fachperspektive | Führt/kontrolliert | Darf behaupten | Darf nicht behaupten |
|---|---|---|---|
| Archäologie / Mittelalterarchäologie | Fundkontext, Stratigraphie, Keramik, Bau-/Wallanlage, Datierung, Grabungslücke | materielle Präsenz, Datierungsrahmen, Befund-/Fundtyp | Ethnie, Ortsname, politische Herrschaft oder Kontinuität ohne Zusatzbeleg |
| Diplomatik / Mediävistik | Urkunde, Regest, Edition, Datierung, Rechtsgeschäft, Zeugen, Überlieferung | quellenförmige Personen-/Rechts-/Herrschaftsbeziehung | Gründung, Bevölkerung, Siedlungsanfang oder materielle Nutzung ohne Zusatzbeleg |
| Herrschafts-/Ministerialitätsgeschichte | Dienstmannschaft, Sitz-/Herkunftsname, lokale Machtträger, Saalfeld/Köln | soziale/personelle Beziehung und institutionelle Einordnung | territoriale Zuständigkeit über alle Nachbarorte ohne Beleg |
| Kirchengeschichte | Archidiakonat, Sedessprengel, Pfarrei, Inkorporation, Patrozinien, Kirchenbau | kirchliche Organisationsachsen und Rechte | vollständige Christianisierung aller lokalen Gruppen |
| Onomastik | historische Namensform, Sprachschicht, Deutung, Varianten | sprachliche Herkunft/Deutung mit Unsicherheit | Ethnizität, Gründungsdatum, Ortskontinuität oder Herrschaft |
| Historische Geographie | Raumbegriff, Wege, Lage, Grenzen, Zentralort/Umland | raumbezogene Hypothesen und Kontrollfragen | Raumontologie ohne Quellen-/Kartierungsbasis |

---

## 5. Siedlungsgeschichtliche Schutzmatrix

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
```

Der Sachenbacher-Slice liefert dafür konkrete Testfälle:

- Ranis: Urkundliche Person `Ekkehardus de Ranis` im 12. Jahrhundert ≠ Gründung Ranis; singuläre 9.-Jh.-Keramik ≠ sicherer dauerhafter Stützpunkt.
- Weltwitz: mittelslawische Keramik + slawisch gedeuteter Ortsname ≠ slawische politische Autonomie oder Siedlungskontinuität.
- Kirchenorganisation: 1071 genannte Pfarrkirchen/Inkorpation ≠ vollständige Christianisierung jeder lokalen Gruppe.
- Knau: Treffer `Knau, Ot. von Zetscha` ≠ Knau bei Neustadt/Orla.

---

## 6. Lossless-by-reference Übergaben

Für interdisziplinäre Weiterarbeit darf die KI keine Flüsterpost erzeugen. Jeder Fachblick benötigt weiterhin Zugriff auf:

- Originalpassage oder exakte publizierte Fundstelle;
- Druckseite und Fußnote;
- Quellen-/Literaturidentität;
- Überlieferungs-/Instanzstatus;
- Suchboundary und Unsicherheit;
- konkurrierende Deutungen;
- Disposition vorhandener Histo-Findings.

Praktische Struktur aus dem Test:

```text
Sachenbacher passage
→ print page / footnote
→ source-ledger delta
→ disciplinary A–J check
→ #46 finding disposition
→ search/source hook
→ method-learning candidate (#60)
```

---

## 7. Promotionsblocker für #60

Dieser Methodenkandidat darf noch nicht als `working-method` gelten, weil:

1. Die relevanten Spezialstudien und Primär-/Editionsquellen wurden nur teilweise identifiziert und noch nicht direkt kollationiert.
2. Die DDE/OATbyCO-HTML-Instanz zeigt nicht in allen Passagen alle Seitenumbrüche/Footnote-Texte so, dass externe Druckzitation ohne Bild-/Druckkontrolle sicher wäre.
3. Für Archäologie, Onomastik und Kirchengeschichte fehlen noch vollständige Domain Method Profiles mit SOTA-gestützten Inferenzverträgen.
4. Der Test ist ein Einzelfall; weitere Sekundärwerke und echte Primärquellen müssen folgen.

Status bleibt daher:

```text
method_hypothesis / live-test-supported / not-promoted
```

---

## 8. Konkrete nächste Methodenarbeit

1. Ein Domain Method Profile `Siedlungsgeschichte / historische Raumrekonstruktion` entwerfen, aber erst nach SOTA-Check.
2. Ein Profil oder Subprofil `Archäologische Sachkultur und Ethnizität im Mittelalter` gegen Brather und neuere Debatte prüfen.
3. Ein Profil `Kirchenorganisation / Pfarrorganisation / Patrozinien / Archidiakonate` anhand Bünz und einschlägiger Kirchenverfassungsgeschichte prüfen.
4. Ein Profil `Onomastik als Evidenzachse` mit strikter Trennung von Namendeutung, Siedlungsphase, Ethnizität und Herrschaft ausarbeiten.
5. Für Sekundärwerksintegration ein maschinenlesbares Evidence-Route-Schema entwickeln: Sekundärbehauptung → Fußnote → referenzierte Quelle/Literatur → Prüfstatus → erlaubte Aussage → Overclaim.

---

## 9. Übergabe an #46

Die historische Ausführung dieses Methodenlearning liegt in:

- `docs/research/cases/u2-sachenbacher-2022-clean-room-slice.md`
- `docs/research/cases/orlagau-source-ledger-sachenbacher-2022-delta.md`

Dieses Methodenlearning darf nicht allein als historischer Befund gelesen werden. Historische Truth bleibt bei #46 und dessen Research-Artefakten.
