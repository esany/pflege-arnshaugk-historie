# Ranis Pilot – Product-/System-Learning

**Status:** `pilot observation / not historical evidence / not automatic requirement delta`  
**Work Owner:** #85  
**Related audit:** #64

Dieses Dokument enthält **keine historischen Findings**. Es hält ausschließlich beobachtete Friktionen und mögliche System-/Workflow-Learnings aus dem Ranis-Pilot fest. Promotion in Requirements/Architecture erfolgt nur über die bestehenden Owner-Prozesse.

## Repo-Audit vor Pilotstart

Frisch geprüft wurden:

- vollständiger Repository-Baum auf `main` als Struktur-/Ownership-Audit;
- `AGENTS.md`, `PROJECT_STATE.md`, Root-`README.md`;
- `docs/research/README.md`;
- `docs/research/source-identity-protocol.md`;
- Canonical Research State / Identity Contract;
- relevante Owner-Issues #45, #46, #60, #64 samt Owner-Feedback;
- `docs/research/cases/orla-saale-region-longue-duree-research-framework.md`;
- vorhandener, inzwischen supersedierter Ranis-lastiger Sachenbacher-Clean-Room-Slice.

**Auditgrenze:** Der gesamte Baum wurde enumeriert und die für Research Governance, Ownership und Ranis-Scope kanonischen Artefakte wurden frisch eingelesen. Nicht jede Zeile jedes technischen Validators/Tests wurde erneut gelesen, weil der Pilot keine technische Implementierung ändert. Diese Grenze ist bewusst dokumentiert statt als „komplettes Repo inhaltlich gelesen“ überhöht zu werden.

## Learning 1 – Synthese darf räumliche Evidenz nicht erfinden

### Beobachtung

Im Live-Dialog wurde aus publizierten Grabungs-/Stratigraphieinformationen eine anschauliche Höhlengrafik generiert. Dabei entstanden nicht publizierte Kammernamen, Geometrien, Lagebeziehungen und ein scheinbar maßstäblicher Plan.

### Failure

Die Visualisierung sah evidenziell aus, obwohl Teile Modellfantasie waren. Bei Archäologie/Topographie ist dies ein schwerer epistemischer Fehler.

### Pilotregel

```text
Originalplan / Vermessung / publizierte Rekonstruktion
→ darf quellengetreu referenziert/annotiert werden

fehlende Geometrie
→ bleibt fehlend

freie didaktische Rekonstruktion
→ nur ausdrücklich als hypothetisch/schematisch und nie als Quellenplan
```

### Möglicher späterer Systembedarf

Ein Guard für `spatial reconstruction / scientific diagram` könnte verlangen, dass jede geometrisch relevante Linie entweder an eine Source/Figure gebunden oder explizit `hypothetical` markiert ist. **Noch kein Requirement.**

---

## Learning 2 – OCR-Glättung zerstört seltene historische Begriffe

### Beobachtung

Bei Börners Frakturdruck wurden schlechte OCR-Lesungen zu scheinbar plausiblen modernen Wörtern/Namen geglättet. Nutzerkorrektur machte sichtbar, dass z. B. seltene Bezeichnungen gerade der Forschungsgegenstand sind.

### Failure

`OCR candidate → semantisch plausible Normalisierung → als Urtext ausgegeben`.

### Pilotregel

Für historische Drucke:

```text
Facsimile
→ diplomatische Lesung
→ Unsicherheitsmarkierung
→ optional getrennte Normalisierung/Interpretation
```

Nie:

```text
OCR → stille Normalisierung → Primärquellenzitat
```

### Möglicher späterer Systembedarf

Bei consequential philological claims sollte OCR-/HTR-Derivatstatus sichtbar bleiben und seltene Tokens/Proper Names eine Faksimile-Prüfung triggern. **Noch kein Requirement.**

---

## Learning 3 – Zugriffstiefe muss claim-seitig sichtbar bleiben

### Beobachtung

Aus der frei verfügbaren Leseprobe zu Pöge-Alder 2024 wurden im Dialog zeitweise Aussagen abgeleitet, die klangen, als seien die nicht frei zugänglichen Ilsa-Seiten gelesen worden.

### Failure

`sample inspected` wurde sprachlich zu `work inspected` aufgebläht.

### Pilotregel

Jede Quelle führt einen Inspection-Status. Eine Behauptung darf nicht mehr Inhalt beanspruchen als die tatsächlich eingesehene Instanz trägt.

### Möglicher späterer Systembedarf

Claim-Promotion könnte den Inspection-Status der tragenden Instanz prüfen. **Bereits in Source-Identity-/Research-State-Invarianten angelegt; noch keine neue Anforderung.**

---

## Learning 4 – Museumsfoto ist eine eigenständige Quelleninstanz

### Beobachtung

Nutzerfotos dokumentieren Vitrinen, Objekte, alte Karten und Interpretationslabels. Sie sind wissenschaftlich wertvoll, aber nicht identisch mit Objektkatalog, Grabungsbericht oder aktuellem Forschungsstand.

### Pilotregel

```text
Foto der Vitrine
→ inspected instance der Ausstellungssituation
→ Transkription/Beobachtung
→ Katalog-/Objekt-Resolution als separater Schritt
```

Eine alte Beschriftung wie `vorchristliche Kultstätte` wird als museumshistorische Aussage erfasst, nicht als heutiges Finding.

---

## Learning 5 – Themenreichtum braucht Queue, nicht Mega-DoD

### Beobachtung

Der Ranis-Dialog sprang produktiv zwischen Paläolithikum, Genetik, Sagenforschung, frühen Ausgrabungen, Mittelalter, Bauforschung und Museumsobjekten. Ein einzelnes „Ranis-Dokument“ würde diese Ebenen schnell vermischen.

### Pilotentscheidung

- eine kurze owner-lesbare Root-Sicht;
- **ein** aktiver Vertical Slice;
- weitere Themen als explizite Slice-Queue;
- Evidence Ledger gemeinsam, aber mit klaren Source-/Instance-Statusgrenzen;
- System-Learning separat.

Dies operationalisiert direkt den #64-Befund, ohne eine neue Governance-Schicht zu erfinden.

---

## Learning 6 – Longue durée braucht Evidenzachsen, keine Kontinuitätsgeschichte

### Beobachtung

Ranis/Orlatal besitzt tatsächlich Fundplätze aus sehr unterschiedlichen Zeiten. Didaktisch entsteht leicht eine attraktive Erzählung „dieselbe Landschaft wurde seit 60.000 Jahren immer wieder gelesen“.

### Risiko

Räumliche Wiederkehr kann fälschlich zu Bevölkerungs-, Kultur- oder Erinnerungs-Kontinuität werden.

### Pilotregel

Longue durée wird nur als **vergleichende Landschaftsfrage** geführt. Jede Zeitphase behält ihre eigene Evidenzachse. Übergänge sind `unresolved`, solange direkte Brücken fehlen.

---

## Was der Pilot bewusst nicht tut

- keine Änderung von `AGENTS.md`, Root-README oder PROJECT_STATE auf `main`;
- keine neue Ontologie/DB-Struktur;
- kein Method Profile aus Modellplausibilität;
- keine Requirement-Erweiterung;
- keine Binärdateiablage der Nutzerfotos in GitHub;
- kein automatischer Merge/PR.

## Reviewfragen an den Owner

1. Ist `README.md` in diesem Pilot innerhalb von ca. fünf Minuten fachlich verständlich, ohne Governance-Vorwissen?
2. Ist die Trennung zwischen historischem Research State und System-Learning praktisch genug?
3. Ist ein aktiver Slice + Queue besser als ein großer Ranis-Mastertext?
4. Reicht das Evidence Ledger, um die Aussagen aus dem Chat ohne Chat wieder zu prüfen?
5. Welche der Queue-Fragen soll nach VS1 als nächster echte Research Slice aktiviert werden?
