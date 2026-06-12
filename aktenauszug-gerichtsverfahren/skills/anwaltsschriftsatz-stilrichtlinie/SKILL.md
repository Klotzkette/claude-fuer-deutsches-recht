---
name: anwaltsschriftsatz-stilrichtlinie
description: "Stilrichtlinie für den juristisch sauberen neutralen und für Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln für alle Bausteine des Aktenauszugs. Maßstab §§ 130 131 ZPO im Aktenauszug Geri..."
---

# Anwaltsschriftsatz-Stilrichtlinie

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: StPO § 147 Akteneinsicht im Ermittlungsverfahren auf Antrag, § 385 Abs. 3 Nebenkläger, ZPO § 299 jederzeit für Parteien, Bearbeitung i.d.R. 2-4 Wochen.
- Tragende Normen verifizieren: ZPO §§ 299, 299a, StPO §§ 147, 385, 406e, VwGO § 100, SGG § 120, FamFG § 13, BORA § 19 (Akteneinsicht), Aktenordnung (AktO), AnwGH-Bescheinigungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Anwalt, Geschäftsstelle, Verteidiger, Nebenklägervertreter, Beigeordneter, ggf. Sachverständiger.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Akteneinsichtsantrag, Aktenauszug (chronologisch), Aktenvermerk, Aktenspiegel, Beweismittelübersicht, Zeitachse, Vollmacht — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Normhintergrund — Schriftsatz-Anforderungen

- § 130 ZPO — Pflichtinhalt anwaltlicher Schriftsätze (Bezeichnung der Partei, Antraege, Tatsachen, Beweismittel)
- § 131 ZPO — Beizufügende Schriftstücke und Anlagen
- § 253 Abs. 2 ZPO — Klageschrift: bestimmter Antrag, Sachverhalt, Benennung Gericht
- § 520 Abs. 3 ZPO — Berufungsbegründung: Bezeichnung der Angriffspunkte, neues Vorbringen
- § 551 Abs. 3 ZPO — Revisionsbegründung: Angabe der Revisionsgründe

## Rechtsprechung zum Schriftsatzstil und Schriftsatz-Anforderungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sprache

### Allgemeine Grundsätze

- **Sachlich und präzise:** Jeder Satz transportiert eine Information. Füllphrasen vermeiden.
- **Juristisch korrekt:** Rechtsbegriffe werden in ihrer gesetzlichen oder gefestigten dogmatischen Bedeutung verwendet.
- **Neutral:** Keine Wertungen, keine Erfolgsprognosen (→ Skill `neutralitaetspruefung`).
- **Aktiv bevorzugen:** "Die Klägerin macht geltend" — nicht "Es wird geltend gemacht".

### Verbotene Begriffe

Keine Begriffe aus dem Bereich kommerzieller Textverarbeitungssoftware oder Assistenzsysteme. Keine Formulierungen wie "basierend auf meiner Analyse" oder "nach meiner Einschätzung". Keine Ich-Form.

### Parteibezeichnungen

- Konsistente Verwendung im gesamten Aktenauszug
- Zulässig: vollständiger Name, Kurzname, Parteibezeichnung (die Klägerin)
- Nicht mischen: nicht "Klägerin" in einem Abschnitt und "Frau Müller" im nächsten
- Abkürzungen (Kl., Bekl.) nur in Tabellen, nicht in Fließtext

### Normen und Paragraphen

- Vollständige Angabe bei erster Nennung: § 634 Nr. 4 i.V.m. § 280 Abs. 1 BGB
- Abkürzung bei Wiederholung möglich: § 634a Abs. 1 Nr. 1 BGB (Verjährung)
- Gesetze stets mit Kurzbezeichnung: BGB, ZPO, StPO, VwGO, ArbGG, SGG, KSchG, GKG

## Gliederung

### Überschriften-Hierarchie

```
### Aktenauszug — [Aktenzeichen] (H1 — nur einmal)

## Verfahrensidentifikation (H2 — Bausteine)
### Parteien (H3 — Unterabschnitte)
#### Klägerseite (H4 — bei Bedarf)
```

### Abschnittstrennungen

Jeder Baustein beginnt auf einer neuen Hierarchieebene. Zwischen Bausteinen eine Leerzeile.

## Tabellen

### Formatierung

- Markdown-Tabellen mit Pipes und Trennzeile
- Spaltenbreite nicht fixieren (Markdown passt sich an)
- Spaltenköpfe fett oder als Header-Zeile

### Tabellenstil

| Gut | Nicht gut |
|---|---|
| Klägerin / Beklagte als Spaltenköpfe | Kl. / Bekl. |
| Kurze präzise Zellinhalte | Lange Fließtextabsätze in Zellen |
| Fundstellen in separater Spalte | Fundstellen ohne Quelle |

## Datumsformat

- Vollständig: TT.MM.JJJJ (z. B. 15.03.2021)
- Kein ISO-Format (2021-03-15) im Aktenauszug-Body
- Monats-/Jahresangaben: März 2021 (nicht 03/2021)

## Beträge

- Immer mit EUR-Präfix: EUR 45.000
- Keine Tausenderpunkte in Zahlen: EUR 45000 oder EUR 45.000 (Punkt als Tausendertrenner ist im Deutschen üblich)
- Keine Abkürzung T€ oder TEUR im Aktenauszug (ausgeschrieben)

## Aktenzeichen

Format: [Gericht-Kürzel] [Senats-/Kammernummer] [Verfahrensart] [Laufnummer]/[Jahr]

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Markdown-Besonderheiten

- Fettdruck (`**Text**`) für Daten in Chronologien
- Kursiv (`*Text*`) sparsam — für Gesetzesbegriffe oder Fremdwörter
- Code-Blöcke (` ``` `) für Musterformulierungen und Vorlagen
- Fristenboxen hervorheben (Tabelle oder Blockquote mit ⚠️)

## Qualitätscheck Stil

- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteibezeichnungen konsistent?
- [ ] Normen vollständig angegeben?
- [ ] Datumsformat einheitlich TT.MM.JJJJ?
- [ ] Beträge mit EUR-Präfix?
- [ ] Überschriften-Hierarchie korrekt?
- [ ] Schriftsatz erfüllt Mindestanforderungen §§ 130-131 ZPO?

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
- VII ZR 248/12 (BGH): ersatzlos entfernt (NOT_FOUND auf dejure.org; kein Urteil vom 06.11.2013 nachweisbar)
- VII ZR 126/02 (BGH): ersatzlos entfernt (WRONG_TOPIC: tatsaechliches Thema ist Werkvertragsrecht/Verputzungsfehler/§ 421 BGB, nicht Prozessrecht; Quelle: https://dejure.org/2003,299)
- Aktenzeichen-Formatbeispiele sind frei erfunden und dürfen nicht als Rechtsprechungszitate verwendet werden.
