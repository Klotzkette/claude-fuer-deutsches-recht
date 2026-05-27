---
name: verfahrensidentifikation
description: "Extrahiert strukturiert alle Verfahrensstammdaten: Gericht Kammer Aktenzeichen Streitwert Parteien (Klaeger Beklagte Streithelfer mit Anschrift gesetzlicher Vertretung Prozessbevollmaechtigten) Instanz und Verfahrensart (Klage Eilverfahren Berufung Revision Beschwerde). Normen §§ 253 261 ZPO Klageerhebung."
---

# Verfahrensidentifikation

## Zweck

Dieser Skill extrahiert alle Stammdaten eines Gerichtsverfahrens aus der vorgelegten Akte und stellt sie in einem standardisierten Block dar. Der Block dient als Kopfzeile jedes Aktenauszugs.

## Triage — kläre vor Erstellung

1. Liegt die Klageschrift oder der Eröffnungsbeschluss vor? (Aktenzeichen, Parteien)
2. Sind die Prozessbevollmächtigten beider Seiten aus der Akte ersichtlich?
3. Wurde der Streitwert festgesetzt (Streitwertbeschluss) oder nur vorläufig angegeben?
4. Gibt es Streithelfer oder Nebenintervenienten?

## Zentrale Normen

- § 253 Abs. 2 Nr. 1 ZPO — Klageschrift muss Gericht, Parteien und Streitgegenstand bezeichnen
- § 261 Abs. 1 ZPO — Anhängigkeit mit Einreichung der Klage; Rechtshängigkeit mit Zustellung
- §§ 3-9 ZPO — Streitwert (Bewertung Klageantrag, Früchte, Zinsen, Kosten)
- § 63 GKG — Streitwertfestsetzung durch das Gericht; § 68 GKG — Streitwertbeschwerde
- §§ 66-74 ZPO — Streithelfer / Nebenintervention (Voraussetzungen, Rechte)

## Rechtsprechung zur Verfahrensidentifikation

- BGH, Beschl. v. 05.09.2019 - III ZB 55/18, NJW 2019, 3142 — Zur Parteibezeichnung in der Klageschrift: Falschbezeichnung eines Klägers schadet nicht wenn Identität aus Gesamtkontext zweifelsfrei erkennbar (falsa demonstratio non nocet).
- BGH, Urt. v. 14.11.2017 - XI ZR 547/15, NJW 2018, 459 — Zur Partei- und Prozessfähigkeit juristischer Personen: Vertretung durch organ muss aus der Klageschrift hervorgehen; fehlende Angabe kann geheilt werden.
- BGH, Beschl. v. 20.02.2018 - VIII ZB 66/17, NJW 2018, 1698 — Streitwertfestsetzung nach §§ 3 ff. ZPO: Gericht hat bei Schätzung weiten Ermessensspielraum; Beschwerderecht der Parteien nach § 68 GKG.
- BGH, Urt. v. 19.01.2017 - I ZR 255/14, NJW 2017, 1689 — Zur Nebenintervention nach § 66 ZPO: Streithelfer kann nur Behauptungen und Anträge der unterstützten Hauptpartei vorbringen; eigene Ansprüche sind unzulässig.

## Kommentarliteratur

- Zöller/Greger ZPO § 253 Rn. 1 ff. (Klageschrift, Mindestinhalt)
- Thomas/Putzo ZPO § 261 Rn. 1 ff. (Anhängigkeit und Rechtshängigkeit)
- MüKo ZPO/Schultes § 66 Rn. 1 ff. (Nebenintervention)

## Zu extrahierende Felder

### Gericht und Spruchkörper

- Gericht (vollständige Bezeichnung, z. B. Landgericht Frankfurt am Main)
- Kammer oder Senat (z. B. 3. Zivilkammer, 14. Senat)
- Aktenzeichen (z. B. 3 O 123/23)
- Instanz (Erste Instanz / Berufung / Revision / Beschwerde / Rechtsbeschwerde)

### Verfahrensart

- Ordentliches Klageverfahren (ZPO)
- Eilverfahren (einstweilige Verfügung § 935 ff. ZPO / einstweilige Anordnung)
- Berufungsverfahren (§ 511 ff. ZPO)
- Revisionsverfahren (§ 542 ff. ZPO)
- Strafverfahren (StPO)
- Verwaltungsverfahren (VwGO)
- Arbeitsgerichtsverfahren (ArbGG)
- Sozialgerichtsverfahren (SGG)
- Sonstiges (Beschwerde, PKH, Streitwertbeschwerde)

### Streitwert

- Festgesetzter Streitwert (soweit bekannt)
- Vorläufiger Streitwert (soweit Antrag gestellt)
- Gebührenstreitwert (sofern abweichend)

### Parteien

Für jede Partei:

| Feld | Inhalt |
|---|---|
| Bezeichnung | Kläger / Beklagter / Berufungskläger / Streithelfer etc. |
| Name / Firma | Vollständige Bezeichnung |
| Anschrift | Straße PLZ Ort |
| Gesetzliche Vertretung | (bei juristischen Personen) |
| Prozessbevollmächtigter | Kanzlei und Rechtsanwalt |
| Anschrift Bevollmächtigter | Straße PLZ Ort |

### Streithelfer / Nebenintervenienten

- Benennung der Partei, auf deren Seite der Streithelfer steht
- Eigene Bevollmächtigung wenn vorhanden

## Output-Vorlage

```
## Verfahrensidentifikation

**Gericht:** Landgericht [Stadt]
**Kammer:** [X]. Zivilkammer
**Aktenzeichen:** [AZ]
**Instanz:** Erste Instanz
**Verfahrensart:** Ordentliches Klageverfahren (ZPO)
**Streitwert:** [EUR oder "nicht festgesetzt"]

### Parteien

| Rolle | Partei | Anschrift | Prozessbevollmächtigter |
|---|---|---|---|
| Kläger | [Name] | [Adresse] | [Kanzlei / RA] |
| Beklagter | [Name] | [Adresse] | [Kanzlei / RA] |
```

## Hinweise

- Fehlende Felder werden als „nicht aus Akte ersichtlich" gekennzeichnet, nicht geschätzt.
- Bei mehreren Klägern oder Beklagten wird jede Person separat aufgeführt.
- Streithelfer werden gesondert unter der Hauptparteitabelle gelistet.
- Keine Bewertung der Parteibezeichnung (z. B. ob Kläger wirklich klagebefugt ist).
