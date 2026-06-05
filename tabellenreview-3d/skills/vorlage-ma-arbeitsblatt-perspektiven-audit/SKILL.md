---
name: vorlage-ma-arbeitsblatt-perspektiven-audit
description: "Vorlage MA Arbeitsblatt Perspektiven Audit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vorlage MA Arbeitsblatt Perspektiven Audit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vorlage MA Arbeitsblatt Perspektiven Audit** im Plugin Tabellenreview 3D. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vorlage-ma-due-diligence` | Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für M-und-A-Transaktionen. Abgrenzung: nicht allgemeines M-und-A-Skill. |
| `arbeitsblatt-perspektiven-definieren` | Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster, Gläubigerstellung. Output: Perspektivendefinition als Grundlage für Wuerfel-Aufbau. Abgrenzung: nicht Prüfungsdurchführung. |
| `audit-trail-protokoll` | Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output: Audit-Trail-Protokoll. Abgrenzung: nicht inhaltliche Prüfung (Zweck: Nachvollziehbarkeit). |

## Arbeitsweg

Im Plugin Tabellenreview 3D gilt für **Vorlage MA Arbeitsblatt Perspektiven Audit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vorlage-ma-due-diligence`

**Fokus:** Vorlagetabelle für M-und-A-Due-Diligence im 3D-Format: Forderungen, Verbindlichkeiten, Rechtsrisiken. Normen: GmbHG, AktG, HGB, InsO. Prüfraster: Vertragsrisiken, Haftungsuebernahme, steuerliche Lasten. Output: Due-Diligence-Tabelle für M-und-A-Transaktionen. Abgrenzung: nicht allgemeines M-und-A-Skill.

# /tabellenreview-3d:vorlage-ma-due-diligence

## Zweck

M&A-DD bei einem Vertragsstapel der Zielgesellschaft. Die Standardfragen sind bekannt — diese Vorlage liefert sie fix und fertig: Spaltenprompts mit BGH-Verankerung, vier Arbeitsblatt-Perspektiven, Ampel-Schwellen praxisbewährt.

## Spalten (18 Datenpunkte)

1. **Vertragsart** — Rahmenvertrag / Einzelvertrag / NDA / Lizenz / Lieferung / Werk
2. **Laufzeit und Beginn** — Vertragsdatum + Festlaufzeit / unbefristet
3. **Kündigungsfrist** — ordentliche / außerordentliche / Sondertatbestände
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
5. **MAC-Klausel** — Wesentlichkeitsdefinition / Rechtsfolge (BGB Paragraph 313 / 314)
6. **Abtretungsverbot** — BGB Paragraph 399 / HGB Paragraph 354a / Vertragsübernahme
7. **Haftungsbegrenzung** — pro Fall / pro Jahr / Ausschluss Vorsatz und grobe Fahrlaessigkeit
8. **Garantien** — beschaffenheitsbezogen / verschuldensunabhängig / Haftungsausschluss BGB Paragraph 444
9. **Vertragsstrafe** — Höhe / Deckelung / Verschuldensanknuepfung
10. **Service-Level** — Reaktionszeit / Verfügbarkeit / Wiederherstellungszeit
11. **Datenschutz-AVV** — DSGVO Artikel 28 / Drittlandtransfer / SCC / TIA
12. **Geheimhaltung** — Dauer / Carve-Outs / Rückgabe / Sanktionen
13. **Vergütung** — Festpreis / Stundensatz / Erfolg / Schwellen
14. **Preisanpassung** — Indexbindung / Schwellen / Kündigungsrecht der Gegenseite
15. **Schriftform** — Änderungsvorbehalt / Sprengsatz (BGB Paragraph 125 Satz 2)
16. **Gerichtsstand** — vereinbarter Gerichtsstand / Kaufmannsklausel (ZPO Paragraph 38)
17. **Schiedsklausel** — Schiedsgericht / Sitz / Sprache / Verfahrensordnung
18. **Anwendbares Recht** — Rechtswahl / kollisionsrechtliche Wirkungen

## Arbeitsblatt-Perspektiven (4)

### Recht (Anwaltsperspektive)

- Zusatzspalten: AGB-Wirksamkeit (BGB Paragraph 305 ff.) / Klauselverbote (BGB Paragraph 308 / Paragraph 309) / Verjährungsverkürzung
- Prüfer: M&A-Lead-Counsel
- Materialität rot: unwirksame Klausel mit Hauptleistungsbezug

### Steuer (Steuerberater)

- Zusatzspalten: Umsatzsteuer-Behandlung / Reverse-Charge / verdeckte Gewinnausschuettung bei Konzernverträgen (KStG)
- Prüfer: Steuerberater
- Materialität rot: USt-Risiko mehr als 100k EUR

### Wirtschaft (Buyside)

- Zusatzspalten: Vertragsvolumen pro Jahr / Top-Kunde-Konzentration / Working-Capital-Effekt / Verlängerungsoption
- Prüfer: Deal-Lead
- Materialität rot: Vertrag > 10 Prozent Umsatz UND Kündigungsrecht der Gegenseite < 12 Monate

### Datenschutz (DSGVO)

- Zusatzspalten: Datenkategorien / Rechtsgrundlage Artikel 6 / Drittlandtransfer / Auftragsverarbeitung / Joint-Controller
- Prüfer: Datenschutzbeauftragter
- Materialität rot: Auftragsverarbeitung ohne AVV oder Drittlandtransfer ohne SCC

## BGH-Leitsätze (Auswahl)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabe

Würfel-Schema fix und fertig in `wuerfel-schema.yaml` mit allen drei Achsen. Direkt einsatzbereit für `review-durchfuehren`.

## 2. `arbeitsblatt-perspektiven-definieren`

**Fokus:** Drei Prüfperspektiven (Spalten) für den 3D-Tabellenreview definieren: Forderung, Prüfung, Stellung nach §§ 174 ff. InsO. Normen: §§ 174 ff. InsO, ZPO. Prüfraster: Forderungsaufstellung, Prüfungsraster, Gläubigerstellung. Output: Perspektivendefinition als Grundlage für Wuerfel-Aufbau. Abgrenzung: nicht Prüfungsdurchführung.

# /tabellenreview-3d:arbeitsblatt-perspektiven-definieren

## Zweck

Excel kann mehrere Tabellenblaetter nebeneinander. Der 3D-Würfel übernimmt dieses Bild: dieselben Dokumente (Zeilen) werden mehrfach geprüft, jedes Mal aus einer anderen Perspektive (Arbeitsblatt). Die Spalten sind je Arbeitsblatt zum Teil deckungsgleich (vergleichbare Datenpunkte) und zum Teil arbeitsblattspezifisch.

## Triage zu Beginn

1. Wie viele Perspektiven sind erforderlich? (Recht / Steuer / Wirtschaft / Datenschutz / IT)
2. Muss jede Perspektive von einem anderen Pruefer verantwortet werden?
3. Gibt es GwG-Compliance-Anforderungen? → Separate Compliance-Perspektive (LkSG / GwG / IDW PS 980)
4. Ist ein M&A-Closing-Datum bekannt? → Fristen der Arbeitsblaetter entsprechend konfigurieren

## Rechtliche Grundlagen fuer Pruefer-Perspektiven

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Standard-Perspektiven

### Recht (Anwaltsperspektive)

- Spalten: AGB-Wirksamkeit Haftungsregime Verjährungsverkürzung Gerichtsstand Schiedsklausel Schriftformklausel
- Materialität: rot bei Klauseln die nach BGB Paragraph 307 unwirksam sind
- Prüfer: zugelassener Rechtsanwalt

### Steuer (Steuerberater)

- Spalten: Umsatzsteuer-Behandlung Rechnungspflichtangaben UStG Paragraph 14 grenzüberschreitend ja / nein Reverse-Charge ja / nein
- Materialität: rot bei UStG-Compliance-Risiken
- Prüfer: Steuerberater oder Wirtschaftsprüfer

### Wirtschaft (Buyside-Analyst)

- Spalten: Vertragsvolumen Laufzeit Kündigungsdatum Preisanpassungsmechanik Working-Capital-Effekt
- Materialität: rot bei Top-5-Kunden-Konzentration über 60 Prozent
- Prüfer: Deal-Lead / Corp-Dev

### Datenschutz (DSGVO-Beauftragter)

- Spalten: Datenkategorien Rechtsgrundlage Auftragsverarbeitung-Pflicht AVV vorhanden Drittlandtransfer SCC vorhanden
- Materialität: rot bei fehlender AVV trotz Auftragsverarbeitung (DSGVO Artikel 28)
- Prüfer: Datenschutzbeauftragter

### IT (Architekt)

- Spalten: Hosting-Modell Verschlüsselungs-Standard Lock-in-Risiko Schnittstellen-Dokumentation Exit-Daten-Format
- Materialität: rot bei nicht standardisierten Datenformaten ohne Exit-Pflicht
- Prüfer: IT-Architekt

### Betrieb (Operations)

- Spalten: Service-Level Reaktionszeit Wiederherstellungszeit Eskalationsstufen Vertretungsregelung
- Materialität: rot bei SLA-Reaktionszeit über 4 Stunden bei produktionskritischen Services
- Prüfer: Operations-Lead

### Compliance (GwG / LkSG)

- Spalten: Wirtschaftlich Berechtigter bekannt Sanktionslisten-Prüfung Lieferketten-Risiko-Region nach LkSG
- Materialität: rot bei Sanktionslisten-Treffer
- Prüfer: Compliance-Officer

## Pflichtfelder pro Arbeitsblatt

```yaml
- id: recht
 titel: "Rechtliche Perspektive"
 perspektive: "anwalt"
 pruefer-rolle: "rechtsanwalt"
 eigene-spalten-zusaetze:
 - id: agb-wirksamkeit
 prompt: "Sind die AGB-Klauseln nach BGB Paragraph 305 ff. wirksam?"
 auslassungen:
 - umsatzsteuer # Steuerblatt; hier nicht zuständig
 ampel-regel:
 rot: "Unwirksame Klausel BGB Paragraph 307"
 gelb: "AGB-Wirksamkeit zweifelhaft"
 gruen: "Wirksam oder Individualvereinbarung"
```

## Stapelung

Die Arbeitsblätter werden in der Excel-Ausgabe als Tabellenreiter nebeneinander dargestellt. Im PDF-Bericht erscheinen sie als aufeinanderfolgende Abschnitte. In `kreuzblatt-konsistenzpruefung` werden Widersprüche zwischen Arbeitsblättern gefunden (z. B. ein Vertrag der rechtlich grün aber wirtschaftlich rot ist — das ist legitim und soll markiert werden).

## Ausgabe

- `arbeitsblaetter.yaml` mit allen Arbeitsblättern, deren Spaltenzusätze, Auslassungen und Prüfer-Rollen
- `arbeitsblatt-matrix.md` als menschenlesbare Übersicht

## 3. `audit-trail-protokoll`

**Fokus:** Audit-Trail aller Review-Schritte protokollieren: wer hat wann was geprüft und geaendert. Normen: §§ 238 257 HGB Buchführungspflichten. Prüfraster: Zeitstempel, Prüfer-ID, Aenderungshistorie, Versionierung. Output: Audit-Trail-Protokoll. Abgrenzung: nicht inhaltliche Prüfung (Zweck: Nachvollziehbarkeit).

# /tabellenreview-3d:audit-trail-protokoll

## Triage zu Beginn

1. Fuer welches Mandat / Projekt wird der Audit-Trail gefuehrt? (M&A-DD / Immobilien / Vendor)
2. Wer ist der verantwortliche Pruefer, der jede Abnahme unterschreiben muss?
3. Muss der Audit-Trail gerichtsfest sein? → Append-only-Format (JSONL) waehlen
4. Gibt es berufsrechtliche Aufbewahrungspflichten? (§ 50 BRAO: 5 Jahre Mandatsakte)

## Rechtliche Grundlagen zur Dokumentationspflicht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Wer mit KI Verträge prüft muss später erklären können wie das Ergebnis zustande kam. Dieser Skill ist die Erklärung — Append-only-Log für den gesamten Lebenszyklus des Würfels.

## Ereignistypen

### Würfel-Lebenszyklus

- `würfel.erstellt` — Würfel-Schema neu angelegt
- `würfel.dimension-erweitert` — Spalte / Zeile / Arbeitsblatt hinzugefügt
- `würfel.dimension-gekuerzt` — Spalte / Zeile / Arbeitsblatt entfernt
- `würfel.archiviert` — Würfel abgeschlossen

### Prompts

- `prompt.erstellt` — neuer Spalten- oder Zeilenprompt definiert
- `prompt.geändert` — Prompt-Wortlaut geändert (Versions-ID erhöht)
- `prompt.deaktiviert` — Prompt aus aktivem Schema genommen

### Reviewlauf

- `lauf.gestartet` — Reviewlauf begonnen, mit Würfel-Snapshot-Hash
- `lauf.beendet` — Reviewlauf beendet, mit Ergebnis-Hash
- `lauf.fehler` — Reviewlauf abgebrochen, mit Fehlermeldung

### Caching

- `cache.treffer` — Zelle aus Cache übernommen, Quell-Zell-ID
- `cache.invalidiert` — Cache-Eintrag verworfen weil Prompt-Version geändert

### Prüfer-Workflow

- `prüferflag.gesetzt` — Zelle braucht menschliche Prüfung, Grund
- `prüferabnahme.eingegeben` — Prüfer hat abgehakt, Prüfer-ID und Entscheidung
- `prüfer.kommentar` — Prüfer-Kommentar zu Zelle

### Belegkette

- `datei.gehasht` — Hash einer Quelldatei berechnet
- `hash-bruch` — Quelldatei-Hash weicht vom registrierten Hash ab (Manipulationsverdacht)

## Pflichtfelder pro Eintrag

```json
{
 "zeitstempel": "2026-05-20T14:23:11Z",
 "aktion": "lauf.beendet",
 "verantwortlicher": "system",
 "würfel-version": "v3",
 "prompt-version": "p12",
 "modell-version": "claude-opus-4-7",
 "eingangs-hash": "sha256:...",
 "ausgangs-hash": "sha256:...",
 "anzahl-zellen": 4176,
 "anzahl-prüferflag": 87,
 "begründung": "Standardlauf nach Schema-Änderung Spalte 'MAC'"
}
```

## Ablage

- `audit-trail.jsonl` — append-only, eine JSON-Zeile pro Ereignis. Nie ändern, nur anhängen.
- `audit-trail.md` — periodisch zu menschenlesbarem Markdown verdichtet (z. B. wochenweise).

## Integritaet

- Jeder Eintrag enthält den Hash des vorherigen Eintrags (Chain-of-Trust). Wer einen Eintrag ändert bricht die Kette.
- Optional: kryptografische Signatur des Prüfers bei Abnahme-Ereignissen.

## Verwendung

- Pflicht vor jeder Mandatsübergabe — der Prüfer signiert den letzten Audit-Stand.
- Bei Beschwerden Aufsicht oder Haftungsfrage rückverfolgbar nachweisen welcher Reviewlauf welchen Output produziert hat.
- Verhindert dass Prompts schleichend geändert werden und alte Zellen `nicht mehr nachvollziehbar` sind.
