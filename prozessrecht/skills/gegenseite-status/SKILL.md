---
name: gegenseite-status
description: Erstellt wöchentliche Statusanfrage-E-Mail-Entwürfe an externe Bevollmächtigte (Sozietät/Korrespondenzanwalt) für alle aktiven Prozessmandate im Portfolio — Markdown-Entwurf je Mandat, optional Outlook-Entwurf bei verfügbarer MCP-Integration. Lädt, wenn der Nutzer Statusanfragen an externe Bevollmächtigte erstellen, wöchentliche Rückfragen bei der Außensozietät generieren oder mandatsbezogene Anfragen-E-Mails aus dem Portfolio-Protokoll heraus entwerfen möchte.
language: de
when_to_use: |
  Trigger phrases and example requests:
  - Statusanfrage externe Bevollmächtigte
  - Korrespondenzanwalt anfragen
  - wöchentliche OC-Rückfrage
  - Außensozietät Status
  - Sachstandsanfrage Prozess
  - Stand bei Gegenbevollmächtigten
  - externe Anwälte abfragen
  - Sozietät anfragen
---

# Statusabfrage Externe Bevollmächtigte

## Zweck

Jede Woche dieselbe Statusanfrage an externe Bevollmächtigte für 5–15 Prozessmandate zu schreiben ist mechanische Routinearbeit. Inhalt je Mandat ist wiederkehrend (Stand, ausstehende Entscheidungen, Budgetkontrolle). Die Adressaten sind gleich (Partneranwalt der mandatierten Sozietät). Der Ton ist einheitlich (gemäß der im Kanzleiprofil hinterlegten Direktive für externe Bevollmächtigte). Dieser Skill erstellt alle Entwürfe; der Anwalt prüft und versendet.

## Eingaben

- **Mandatsprotokoll `_log.yaml`**: Filterquelle und Feldquelle
- **`akte.md` und `verlauf.md`** je Mandat: Mandatskontext und aktuelle Entwicklungen
- **Kanzleikonfiguration `CLAUDE.md`**: Direktive für externe Bevollmächtigte (Tonvorgabe), Unterzeichner, Budgethaltung
- **Flags** (optional): `--alle`, `--slug=[bezeichnung]`, `--kein-outlook`

## Rechtlicher Rahmen

### Kernvorschriften

- **§ 43a Abs. 4 BRAO** — Anwaltliche Fortbildungs- und Berichterstattungspflicht gegenüber dem Mandanten; regelmäßige Rückmeldung der externen Bevollmächtigten ist Teil der ordnungsgemäßen Mandatsführung.
- **§ 667 BGB** — Auskunftspflicht des Beauftragten; der externe Bevollmächtigte hat dem Auftraggeber auf Verlangen Auskunft zu erteilen; die wöchentliche Statusanfrage ist Ausfluss dieses Anspruchs.
- **§ 43a Abs. 2 BRAO** — Vertraulichkeit; die Statuskorrespondenz mit externen Bevollmächtigten ist durch die gemeinsame Verschwiegenheitspflicht geschützt.
- **§ 49b BRAO; §§ 2 ff. RVG** — Vergütung; Budgetanfragen und Kostenkontrollen im Statusschreiben orientieren sich am vereinbarten Honorar und etwaigen Vergütungsrahmen.

### Leitentscheidungen

- **BGH, Urt. v. 08.11.2007 – IX ZR 58/06, NJW 2008, 224 Rn. 18 ff.** — Auskunfts- und Rechenschaftspflicht des Rechtsanwalts gegenüber dem Mandanten; regelmäßige schriftliche Berichterstattung als Teil der Sorgfaltspflicht.
- **BGH, Urt. v. 19.01.2006 – IX ZR 232/04, NJW 2006, 1579 Rn. 12** — Haftung des Rechtsanwalts bei unterlassener Information über veränderte Prozesslage; Kommunikationspflichten im laufenden Prozessmandat.
- **BGH, Urt. v. 06.06.2013 – IX ZR 204/12, NJW 2013, 2747 Rn. 14** — Pflicht zur Unterrichtung des Mandanten über drohende Kostenrisiken; Relevanz für Budgetabfragen in Statusschreiben.

### Kommentarliteratur

- `Dittmann, in: Henssler/Prütting, BRAO, 5. Aufl. 2023, § 43a Rn. 120` — Unterrichtungspflichten des Anwalts; Reichweite der Berichterstattungspflicht gegenüber Mandanten und bei Korrespondenzmandat.
- `Römermann, in: BeckOK BRAO, 21. Ed. (Stand 01.03.2024), § 49b Rn. 8` — Vergütungsabrechnungen; Transparenz im Mandatsverhältnis.

## Ablauf

### Schritt 1: Mandate filtern

**Standardfilter:**

- `status != geschlossen`
- `externe_bevollmaechtigte.sozietaet != null` UND `externe_bevollmaechtigte.partner != null`
- Entweder: letzte Aktualisierung vor mehr als 10 Tagen ODER `naechste_frist` innerhalb von 21 Tagen

Übersprungen werden: Mandate mit Update in den letzten 10 Tagen (kein erneutes Anschreiben erforderlich) sowie Mandate ohne hinterlegte E-Mail-Adresse des externen Bevollmächtigten (Markdown-Entwurf wird trotzdem erstellt; Outlook-Entwurf nicht).

**Flags:**
- `--alle` → Entwurf für alle aktiven Mandate, unabhängig von der Aktualität
- `--slug=[bezeichnung]` → Entwurf nur für ein Mandat (Ad-hoc-Anfrage)
- `--kein-outlook` → kein Outlook-Entwurf, auch wenn MCP verfügbar

### Schritt 2: Je Mandat — E-Mail-Entwurf erstellen

Jede E-Mail folgt demselben Grundgerüst; Inhalt ist mandatsspezifisch.

**Betreff:** gemäß Kanzleidirektive (Fallback: `[Mandat: [Bezeichnung]] — Wöchentlicher Sachstand`)

**Rumpf-Gerüst:**

```
[Vorname des Partneranwalts],

[Ein einleitender Satz — natürlich, entspricht dem Kanzleiston.]

Kurze Rückmeldung zu [Mandatsbezeichnung] erbeten. Einige Punkte:

1. **Sachstand seit [Datum der letzten Aktualisierung aus verlauf.md]** — Was hat sich bewegt, was ist noch offen? Gab es Schriftsätze, Termine, Korrespondenz oder Telefonate seit unserem letzten Austausch?

2. **Bevorstehende Fristen** — Ich vermerke [naechste_frist aus Protokoll + etwaige Fristen aus akte.md]. Bitte Abdeckungsplan bestätigen und ggf. weitere Termine mitteilen.

3. **Ausstehende Entscheidungen** — [offene Fragen aus akte.md, die externen Input erfordern; entfällt, falls keine vorhanden — umnummerieren]

4. **Budget** — [monatlich / quartalsweise / auf Anfrage gemäß Kanzleikonfiguration]. Wo stehen wir gegenüber [Budgetrahmen aus akte.md]? Gibt es Abweichungen?

[Falls wesentlich und relevant: 5. Konkrete Bitte — z. B. „Bitte Entwurf des Schriftsatzes vor [Datum] übersenden" — aus offenen Punkten in akte.md.]

[Grußformel — Name, Funktion, Kontakt. Aus Kanzleikonfiguration.]
```

Ton wird der Kanzleidirektive angepasst — einige Kanzleien schreiben förmlich, andere per Vorname und Stichpunkte. Die Direktive hat Vorrang.

### Schritt 3: Ausgabe erstellen

### Schritt 4: Abschicken-Schranke

Jedem Entwurf wird folgender Hinweis angefügt (vor dem Versenden entfernen):

> Dies ist ein Entwurf zur anwaltlichen Prüfung vor dem Versand an externe Bevollmächtigte. Prüfen Sie auf privilegierte Inhalte, die nicht aus dem Mandatsverhältnis herausgegeben werden sollten, sachliche Richtigkeit, Ton und Budgethaltung. Auch routinemäßige Wochenanfragen können Strategie, Positionierungen oder unbeabsichtigte Zugeständnisse enthalten.

## Ausgabeformat

### Markdown-Entwürfe

Datei: `gegenseite-status/[JJJJ-MM-TT]/[slug].md`

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

# [Mandatsbezeichnung] — Statusanfrage externe Bevollmächtigte — [JJJJ-MM-TT]

**An:** [externe_bevollmaechtigte.email] ([Partner], [Sozietät])
**Von:** [Unterzeichner Name/E-Mail aus Kanzleikonfiguration]
**Betreff:** [Betreffzeile]

> Der Arbeitsergebnis-Kopf oben gilt für diesen internen Vermerk. Der ausgehende E-Mail-Text unten geht an externe Bevollmächtigte in einem Mandatsverhältnis, das selbst durch Verschwiegenheit (§ 43a Abs. 2 BRAO) geschützt ist — Vertraulichkeitskennzeichnung gemäß Kanzleikonfiguration auf der versendeten E-Mail anbringen (typisch: „Vertraulich — Anwaltskorrespondenz / Mandatsgeheimnis").

---

[Rumpf gemäß Gerüst]
```

### Outlook-Entwürfe (falls MCP verfügbar)

Falls die Outlook-MCP-Integration authentifiziert ist:

- Je Mandat wird ein Entwurf im Outlook-Postfach (Ordner „Entwürfe") angelegt mit `an`, `von`, `betreff` und `text`
- Der Entwurf liegt montags zur Prüfung bereit
- Falls die MCP-Integration nicht verfügbar oder fehlerhaft ist: Rückfall auf Markdown und Hinweis an den Nutzer

### Laufergebnis-Zusammenfassung

Nach Verarbeitung aller Mandate: `gegenseite-status/[JJJJ-MM-TT]/_zusammenfassung.md`

```markdown
# Statusanfrage Externe Bevollmächtigte — Lauf [JJJJ-MM-TT]

**Mandate verarbeitet:** [N]
**Entwürfe erstellt:** [N]
**Outlook-Entwürfe:** [erstellt / übersprungen — Grund]

## Entwurf erstellt für

| Mandat | Externer Partner | Zuletzt aktualisiert | Grund der Aufnahme |
|---|---|---|---|
| [slug] | [Partner] | [Datum] | [veraltet / bevorstehende Frist / --alle / --slug] |

## Übersprungen

| Mandat | Grund |
|---|---|
| [slug] | aktuelles Update (zuletzt bearbeitet [Datum]) |
| [slug] | keine E-Mail des externen Bevollmächtigten im Protokoll — nachtragen mit `/mandat-update [slug]` |

## Auffälligkeiten

- Mandate ohne externe Bevollmächtigte: [Liste — bei hohem/kritischem Risiko gesondert markiert]
- Mandate mit externen Bevollmächtigten, aber ohne E-Mail-Adresse: [Liste]
```

## Beispiel

**Sachverhalt:** Mandat `bauer-ag-berufung-2025`, OLG Hamburg. Letztes Update vor 14 Tagen. Nächste Frist: Berufungserwiderung in 18 Tagen. Externer Partner: RA Dr. Schneider, Schneider & Partner.

**Ergebnis:** Entwurf mit Statusanfrage zu eingereichten Schriftsätzen seit letztem Austausch, Bestätigung der Berufungserwiderungsfrist, Budget-Abfrage gemäß Quartals-Direktive. Gespeichert unter `gegenseite-status/2025-05-12/bauer-ag-berufung-2025.md`.

## Risiken und typische Fehler

- **Vertraulichkeit:** Die Statuskorrespondenz mit externen Bevollmächtigten ist durch § 43a Abs. 2 BRAO geschützt; Entwürfe nicht an Personen außerhalb des Mandatskreises weitergeben.
- **Nicht geprüfte Entwürfe versenden:** Auch kurze Statusanfragen können strategische Hinweise, Budgetkonzessionen oder unbeabsichtigte Zugaben enthalten.
- **Veraltete Kontaktdaten:** Falls die E-Mail des externen Partners nicht im Protokoll hinterlegt ist, wird kein Outlook-Entwurf angelegt; der Nutzer erhält einen Hinweis, die Daten nachzupflegen.
- **Mandatsübergreifende Abfrage:** Nur bei aktivem `Mandatsübergreifender Kontext: an` in der Kanzleikonfiguration darf das System mandatsübergreifend lesen.

## Quellenpflicht

- Gesetzestexte: §§ 43a, 49b BRAO; §§ 2 ff. RVG; § 667 BGB
- Rechtsprechung: BGH, Urt. v. 08.11.2007 – IX ZR 58/06, NJW 2008, 224; BGH, Urt. v. 19.01.2006 – IX ZR 232/04, NJW 2006, 1579
- Kommentare: Dittmann, in: Henssler/Prütting, BRAO, 5. Aufl. 2023, § 43a Rn. 120; Römermann, in: BeckOK BRAO, 21. Ed. 2024, § 49b

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
