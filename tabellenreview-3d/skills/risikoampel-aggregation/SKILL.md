---
name: risikoampel-aggregation
description: "Risikoampeln fuer alle geprueften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Pruefraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht. Abgrenzung: nicht Kreuzblatt-Konsistenzpruefung."
---

# /tabellenreview-3d:risikoampel-aggregation


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


## Zweck

4000 Zellen einzeln zu sichten ist nicht praktikabel. Diese Aggregation reduziert die Sicht ohne Information zu verlieren — wer reinzoomen will klickt durch.

## Aggregationsstufen

### Zellen-Ampel (atomisch)

Aus `review-durchfuehren`. Vier Werte: grün / gelb / rot / prüfer-flag.

### Zeilen-Ampel (Dokument)

Konsolidierung über alle Zellen einer Zeile (also über alle Spalten aller Arbeitsblätter):
- mindestens 1 rote Zelle = Zeile **rot**
- keine rote aber mindestens 2 gelbe = Zeile **gelb**
- nur grün = Zeile **grün**
- mindestens 1 Prüfer-Flag = `prüfer-flag` zusätzlich

### Spalten-Ampel (Datenpunkt-Hotspot)

Anzahl roter Zellen über alle Zeilen über alle Arbeitsblätter pro Spalte. Top-5-Spalten mit höchstem Rot-Anteil = Hotspot-Spalten. Beispiel: 'Change of Control' rot in 42 von 87 Verträgen = Hotspot.

### Arbeitsblatt-Ampel (Perspektive)

Anteil roter Zeilen je Arbeitsblatt. Erlaubt Aussage: 'aus Datenschutzsicht ist das Portfolio kritisch, aus Wirtschaftssicht passabel'.

### Würfel-Ampel (Gesamtprojekt)

Worst-of-Worst-Konsolidierung: wenn irgendein Arbeitsblatt rot ist und irgendeine Zeile rot ist und Prüfer noch nicht abgenommen hat = **rot blockierend**.

## Schweregrad-Boden

Wenn ein Skill ein Finding mit einem Schweregrad produziert und ein anderer Skill (z. B. `kreuzblatt-konsistenzpruefung`) ihn ändern will, gilt der vorgelagerte Schweregrad als BODEN — eine rote Zelle kann nicht still nach gelb verschoben werden, nur dokumentiert überschrieben.

## Ausgabe

- `ampel-aggregat.md` mit:
  - Würfel-Ampel (gesamt)
  - Arbeitsblatt-Ampeln (eine je Perspektive)
  - Spalten-Hotspots (Top-N)
  - Zeilen-Ampel-Liste (sortiert nach Schwere)
- `heatmap.json` mit Daten für Excel-Heatmap-Visualisierung

## Hinweis zur Prüfer-Abnahme

Vor Mandatsabnahme müssen ALLE Zellen mit `prüfer-flag` durch den Prüfer abgehakt sein. Ohne Prüfer-Abnahme darf das Aggregat nicht an Mandanten gehen.
