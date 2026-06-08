---
name: aggregation-spaltenprompts-definieren
description: "Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht. Abgrenzung: nicht Kreuzblatt-Konsistenzprüfung im Tabellenreview 3d."
---

# /tabellenreview-3d:risikoampel-aggregation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 2 JVEG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- § 29 VwVfG
- § 1 KSchG
- § 7 KSchG
- § 102 BetrVG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

