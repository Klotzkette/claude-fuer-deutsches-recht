---
name: grosskanzlei-corporate-ma-tabellenreview-3d-datenraum
description: "3D-Tabellenreview M&A-Datenraum: Dokumente Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft verbinden: Anwendungsfall Deal-Team prüft Datenraum-Dokumente systematisch mit internem Review-Cube nach mehreren Workstream-Perspektiven. SPA Due Diligence. Prüfraster Spaltenprompts für Datenpunkte, Zeilendefinition als Dokumente oder Cluster, Blaetter für Legal/Tax/Finance-Perspektive. Output 3D-Review-Matrix mit workstreamspezifischen Befunden und Luecken. Abgrenzung zum freistehenden Tabellenreview-Skill und zu DD-Reporting."
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Qualitaetssicherung
- Human-in-the-loop bei allen hochrisikorelevanten Ausgaben
- Dokumentation: Datum, Bearbeiter, Freigabe durch Senior
