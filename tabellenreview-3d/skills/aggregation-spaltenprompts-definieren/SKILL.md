---
name: aggregation-spaltenprompts-definieren
description: "Für /tabellenreview-3d:risikoampel-aggregation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# /tabellenreview-3d:risikoampel-aggregation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen


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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
