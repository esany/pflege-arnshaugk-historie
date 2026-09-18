# Anno II., Richeza und St. Peter und Paul Saalfeld – Quellen-, Beobachtungs- und Relationsnetz

**Status:** `exploratory / observation-first / method-debt`  
**Work Owner:** #103  
**Research Governance:** #45 + `docs/research/source-identity-protocol.md`  
**Method Owner:** #60  
**Stand:** 2026-09-18

## 1. Arbeitsmodus

Dieses Artefakt sammelt zunächst **wertfrei und dynamisch**:

`Quelle / konkrete Instanz → Fundstelle / Exzerpt → atomare Beobachtung → typisierte Relation → offene Anschlussfrage`

Es enthält **keine vorgezogene Gesamtsynthese**. Begriffe wie `Gründung`, `Eigenkloster`, `Reformkloster`, `Reichsabtei`, `Fürstabtei`, `Freundschaft`, `Konflikt` oder `Netzwerkzentrum` werden nicht als Ergebnis vorausgesetzt. Sie dürfen erst später als klar gekennzeichnete Interpretationen diskutiert werden, wenn die zugrunde liegenden Beobachtungen und Relationen ausreichend dicht dokumentiert sind.

### Statusklassen

- `source-identified` – Quelle/Instanz ist identifiziert, Inhalt noch nicht hinreichend inspiziert.
- `observation` – quellennahe atomare Aussage aus einer benannten Fundstelle.
- `reported-by-secondary` – Aussage ist bislang nur in Sekundärliteratur erfasst.
- `relation-candidate` – zwei Entitäten werden durch mindestens eine Quelle miteinander verbunden; Relationstyp noch nicht abschließend bestimmt.
- `unresolved` – offen; keine positive oder negative Schlussfolgerung.
- `interpretation-later` – mögliche Deutung, bewusst nicht Teil dieses Arbeitsstands.

## 2. Entitätenregister v0.1

### Personen

- Anno II., Erzbischof von Köln
- Richeza / Rycheza
- Hermann II., Erzbischof von Köln
- Siegfried I., Erzbischof von Mainz
- Gunther, Bischof von Bamberg
- Lampert von Hersfeld

### Institutionen / Orte

- Kölner Erzstift / Erzbistum Köln
- Mainz / Erzbistum Mainz
- Saalfeld
- St. Peter und Paul, Saalfeld
- Siegburg / Michaelsberg
- St. Pantaleon, Köln
- Brauweiler
- St. Maria ad Gradus, Köln
- Bamberg / Dom / Domschule
- Kloster Michelsberg / St. Michael, Bamberg
- Coburg
- Klotten

Weitere Entitäten werden nur ergänzt, wenn sie in einer Quelle tatsächlich auftreten oder für Source Identity nötig sind.

## 3. Atomare Beobachtungen

Die Tabelle ist **kein chronologischer Narrativtext**, sondern ein wachsendes Register. Ein Ereignis darf mehrfach auftauchen, wenn verschiedene Quellen es unterschiedlich überliefern.

| ID | Datum / Zeitraum | Quelle | Fundstelle | Atomare Beobachtung | Status |
|---|---|---|---|---|---|
| O-001 | 1056 | ARS-002 / ARS-003 | genaue Primärfundstelle noch offen | Sekundärliteratur berichtet eine Übertragung von Saalfeld/Coburg an Köln mit lebenslänglicher Nutzung durch Richeza. | `reported-by-secondary` |
| O-002 | 1056 | ARS-001 | biographischer Abschnitt | Anno II. wird als Erzbischof von Köln für 1056 geführt. | `observation-secondary` |
| O-003 | 1063-03-21 | ARS-002 / ARS-003 | biographische Abschnitte | Richezas Tod wird in Saalfeld lokalisiert. | `observation-secondary` |
| O-004 | nach 1063 | ARS-002 / ARS-003 | biographische Abschnitte | Richezas Bestattung wird mit St. Maria ad Gradus in Köln verbunden. | `observation-secondary` |
| O-005 | 1063/64 | ARS-009 | Saalfeld-Abschnitt | Die regionale Sekundärdarstellung nennt vor 1071 eine Kanonikergemeinschaft / ein Chorherrenstift in Saalfeld. | `reported-by-secondary` |
| O-006 | 1071 | ARS-005 | Annales 1071, moderne Ausgabe/Übersetzung pp. 152–154 | Lampert berichtet im Zusammenhang mit Saalfeld von Kanonikern und von Mönchen aus Siegburg und St. Pantaleon. | `observation` |
| O-007 | 1071 | ARS-005 | Annales 1071 | Lampert berichtet über eigene Anwesenheit / Erkundung im Zusammenhang mit Saalfeld und Siegburg. | `observation` |
| O-008 | 1071 | ARS-004 | MUB I Nr. 331, S. 223–226 | Zielquelle identifiziert; Rollen, Rechtsakte und Wortlaut von Anno/Siegfried noch nicht atomar exzerpiert. | `source-identified` |
| O-009 | 11. Jh. | ARS-001 | biographischer Abschnitt | Anno wird mit Ausbildung bzw. Tätigkeit an der Bamberger Domschule verbunden. | `observation-secondary` |
| O-010 | 1057–1065 | ARS-007 | NDB Gunther | Gunther wird als Bischof von Bamberg geführt; der Artikel verbindet ihn mit Anno. | `observation-secondary` |
| O-011 | 1064/65 | ARS-007 | NDB Gunther | Gunther und Siegfried von Mainz werden in derselben Pilgerfahrt genannt. | `observation-secondary` |
| O-012 | 11./12. Jh. | ARS-008 | relevante Abschnitte | Michelsberg/St. Michael in Bamberg wird als Bamberger Benediktinerkloster behandelt; eine konkrete Saalfeld-Relation wurde in den bislang inspizierten Passagen nicht dokumentiert. | `unresolved / bounded-negative` |
| O-013 | ca. 1183 | ARS-012 | Hs 945, fol. 1v | Eine spätere Vita-Annonis-Überlieferung stellt Saalfeld und Siegburg im Kontext von Annos Stiftungsmemoria dar. | `observation / later-memory` |

## 4. Relation Register

Relationen werden **quellenweise** erfasst. Gleiche Entitäten können mehrere Relationstypen gleichzeitig besitzen.

| Relation-ID | Subjekt | Relationstyp | Objekt | Zeit | Grundlage | Status |
|---|---|---|---|---|---|---|
| R-001 | Richeza | `associated-with-place` | Saalfeld | 1063 | O-003 | `supported-secondary` |
| R-002 | Richeza | `reported-transfer-to` | Kölner Erzstift | 1056 | O-001 | `candidate; primary-source-check-open` |
| R-003 | Anno II. | `office-holder-of` | Erzbistum Köln | ab 1056 | O-002 | `supported-secondary` |
| R-004 | Richeza | `burial-associated-with` | St. Maria ad Gradus | nach 1063 | O-004 | `supported-secondary` |
| R-005 | Saalfelder Kanoniker | `present-at` | Saalfeld | vor/1071 | O-005/O-006 | `supported-multiple` |
| R-006 | Siegburger Mönche | `reported-move-to` | Saalfeld | 1071 | O-006 | `supported-narrative-source` |
| R-007 | St.-Pantaleon-Mönche | `reported-move-to` | Saalfeld | 1071 | O-006 | `supported-narrative-source` |
| R-008 | Lampert von Hersfeld | `reported-presence-at` | Saalfeld | 1071 | O-007 | `supported-narrative-source` |
| R-009 | Lampert von Hersfeld | `reported-presence-at` | Siegburg | 1071 | O-007 | `supported-narrative-source` |
| R-010 | Anno II. | `education-or-office-associated-with` | Bamberg Domschule | 11. Jh. | O-009 | `supported-secondary` |
| R-011 | Gunther | `office-holder-of` | Bistum Bamberg | 1057–1065 | O-010 | `supported-secondary` |
| R-012 | Gunther | `co-travel-associated-with` | Siegfried I. von Mainz | 1064/65 | O-011 | `supported-secondary` |
| R-013 | Michelsberg Bamberg | `relation-to-be-tested` | Saalfeld | 11. Jh. | O-012 | `unresolved` |

## 5. Offene Knoten / Anschlussfragen

Diese Liste steuert weitere Verdichtung, ohne bereits eine Antwort vorzugeben.

- Welche konkrete Urkunde bzw. Überlieferung liegt der berichteten Saalfeld-/Coburg-Übertragung Richezas zugrunde?
- Welche Personen, Institutionen, Rechte, Güter, Kirchen und Verben nennt MUB I Nr. 331 exakt?
- Welche unterschiedlichen Handlungen werden Anno und Siegfried in derselben oder in verschiedenen Quellen zugeschrieben?
- Welche frühen Belege existieren für St. Peter und Paul als Institution, Patronat, Besitzträger oder Rechtsobjekt?
- Welche Personen sind 1060–1080 zugleich in Bamberg, Mainz, Köln, Siegburg, Saalfeld oder St. Pantaleon belegt?
- Gibt es im Michelsberg-Material Personen-, Memoria-, Besitz-, Handschriften-, Liturgie- oder Reformkontakte zu einem dieser Knoten?
- Welche späteren Quellen verwenden erstmals Bezeichnungen wie `Eigenkloster`, `Reichsabtei` oder `Fürstabtei`, und auf welche Rechtsbeobachtungen stützen sie sich?

## 6. Zotero als Bibliotheks-/Instanzschicht

Zotero wird für #103 als **Discovery- und Verwaltungsquelle** behandelt, nicht als Evidenz.

Zu relevanten Zotero-Einträgen sollen zunächst dokumentiert werden:

`Zotero item key | BibTeX key | Titel | Autor/Herausgeber | Jahr | Item-Typ | Collections | Tags | Attachments | Fulltext-Availability | externe Identifikatoren | möglicher Bezug zu Entitäten/Relationen`

Erst danach wird entschieden, welche konkrete Quelle/Attachment-Instanz inspiziert und als `source_id` in das Source Ledger aufgenommen wird.

**Aktueller Status:** Zotero-Inventar in diesem Chatkontext noch nicht direkt ausgelesen; keine Annahmen über Vollständigkeit oder Relevanz der Bibliothek.

### Geplantes Suchvokabular für Zotero

- Anno / Anno II / Anno von Köln
- Richeza / Rycheza / Rixa
- Saalfeld / Peter und Paul / St. Peter und Paul
- Siegburg / Siegberg / Michaelsberg
- St. Pantaleon
- Bamberg / Michelsberg / St. Michael
- Gunther / Gundachar
- Siegfried / Mainz
- Ezzonen / Ezzo / Brauweiler
- Coburg / Klotten

Zusätzlich werden relevante Tags und Collections **inventarisiert**, nicht nur Schlagwortsuchen ausgeführt.

## 7. Interpretation – bewusst noch nicht begonnen

Dieser Abschnitt bleibt bis zu einer hinreichend verdichteten Beobachtungs- und Relationsbasis leer.

- institutionelle Stellung St. Peter und Paul: `unresolved`
- Verhältnis Anno–Richeza: `unresolved`
- Rolle Siegburgs: `unresolved beyond recorded relations`
- Rolle Bamberg/Michelsberg: `unresolved`
- rechtshistorische Labels: `unresolved`

## 8. Search Boundary

Aktuell umfasst die dokumentierte Basis nur die in
`docs/research/cases/anno-richeza-saalfeld-source-ledger.md`
verzeichneten Quellen und Instanzen.

Nicht als Vollständigkeitsbehauptung zulässig:

- „kein Zusammenhang“
- „direkter Zusammenhang“
- „Gründung durch X“
- „Eigenkloster“
- „Reichsabtei“
- „Reformnetzwerk“

solange diese Aussagen nicht aus einer ausreichend dichten, fundstellenfähigen Relationsbasis abgeleitet und separat als Interpretation ausgewiesen werden.
