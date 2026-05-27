---
name: mittelstand-corporate-ma-tabellenreview-3d-datenraum
description: "3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft."
---

# 3D-Tabellenreview im Datenraum

## Zweck

Dieser Skill bleibt als M&A-Datenraum-Variante erhalten und nutzt ausschließlich interne Vorlagen dieses Plugins. Für den generischen freistehenden Review-Würfel steht zusätzlich `grosskanzlei-ma-tabellenreview` bereit.

## Arbeitsmodus

- Spaltenprompts für Datenpunkte formulieren.
- Zeilen als Dokumente oder Vertragscluster definieren.
- Blätter für Legal, Tax, Finance, ESG, Regulatory und PMI anlegen.
- Kreuzblatt-Widersprüche, fehlende Anlagen und Belegketten ausgeben.
- Ergebnisse in Q&A, Red-Flag-Report, Disclosure Schedules und SPA Issues überführen.

## Rote Schwellen

- Keine Belegkette.
- Formel- oder CSV-Export nicht nachvollziehbar.
- Materiality-Schwellen uneinheitlich.
- Clean-Room-Daten werden mit offenem Datenraum vermischt.

## Standardausgabe

- Review-Setup mit Zeilen, Spalten, Blättern und Materiality.
- Review Grid mit Belegstelle, Risiko, Owner und Follow-up.
- Liste der Widersprüche und fehlenden Dokumente.
- Übergabe an `grosskanzlei-ma-tabellenreview` bei großen Tabellenläufen.

## Vorlagen

- assets/templates/tabellenreview-3d-ma-setup.md
- assets/templates/tabellenreview-workbook.md
- assets/templates/tabellenreview-column-prompts.md
- assets/templates/tabellenreview-row-prompts.md
- assets/templates/data-quality-gate.md

## Rechtliche Einbettung und Praxiswissen

### Normen und Quellen im M&A-Kontext
- § 43a BRAO — anwaltliche Pflichten: Sorgfalt, Vollstaendigkeit, Unabhaengigkeit
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung
- § 17 GeschGehG — Schutz von Geschaeftsgeheimnissen; gilt fuer alle Mandatsinhalte
- Art. 17 MAR — bei boersennotierten Zielobjekten: Ad-hoc-Pflicht und Vertraulichkeit

### Leitsaetze aus der Rechtsprechung
- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — anwaltliche Sorgfaltspflicht: vollstaendige Information des Mandanten auch bei Zeitdruck
- BGH, Urt. v. 14.03.2003 - V ZR 64/02, NJW 2003, 1811 — Offenbarungspflicht: wesentliche Risiken sind ungefragt zu benennen
- OLG Frankfurt, Urt. v. 22.02.2021 - 23 U 70/19, NZG 2021, 680 — Beraterhaftung bei M&A: auch bei eingeschraenktem Zeitrahmen muessen wesentliche Risiken erkannt und kommuniziert werden

### Kommentarliteratur
- Picot, Unternehmenskauf, Kapitel 1 (M&A-Prozess, Transaktionsmanagement), 5. Auflage
- Schramm/Alexander, BRAO, § 43a Rn. 1-50

### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior
