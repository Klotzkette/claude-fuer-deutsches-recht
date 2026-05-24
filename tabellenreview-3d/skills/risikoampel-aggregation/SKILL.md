---
name: risikoampel-aggregation
description: "Konsolidiert die Ampel-Wertungen entlang aller drei Wuerfelachsen — pro Zelle (atomisch) pro Zeile (Dokument-Gesamtampel) pro Spalte (Datenpunkt-Hotspots) pro Arbeitsblatt (Perspektiven-Gesamtampel) und pro Gesamtwuerfel (Projekt-Ampel). Verwendet Schweregrad-Boden — eine rote Zelle macht die Zeile mindestens orange. Erkennt Hotspots (Spalten mit ueberproportional vielen roten Zellen). Erzeugt `ampel-aggregat.md` und Heatmap-Daten fuer Excel-Export. Pflichtschritt vor `pruefer-uebergabe-paket`."
---

# /tabellenreview-3d:risikoampel-aggregation

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
