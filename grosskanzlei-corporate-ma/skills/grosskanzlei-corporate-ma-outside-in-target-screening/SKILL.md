---
name: grosskanzlei-corporate-ma-outside-in-target-screening
description: "Zielobjekt-Screening und Pipeline-Analyse aus öffentlichen Quellen: Anwendungsfall Mandant oder Deal-Team sucht geeignete Akquisitionsziele und muss fruehe Analyse aus Registern, Finanzdaten, Nachrichten und Branchenhinweisen erstellen. §§ 14-17 GWB Marktabgrenzung, MAR Insiderinformationen. Prüfraster Anforderungsprofil, Markt-Fit, IP-Status, Compliance-Risiken, Synergien, Warnsignale. Output Ziel-Screening-Report mit Scorecard, Pipeline-Rangliste und DD-Vorabhinweisen. Abgrenzung zu DD-Legal/Commercial für formale Due Diligence und zu Transaktionsstruktur."
---

# Outside-in Target Screening

## Zweck

Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen.

## Arbeitsmodus

- Anforderungsprofil des Kaufinteressenten erfassen.
- Zielunternehmen nach Markt, Produkt, Kunden, IP, Compliance, Risiko und Synergie scoren.
- Warnsignale für spätere Due Diligence markieren.
- Keine vertraulichen Daten fingieren; Quellenstatus klar trennen.

## Rote Schwellen

- Quelle nicht verifizierbar.
- Bewertung basiert nur auf Modellannahmen.
- Marktmissbrauchs- oder Insiderrechtsrisiko bei börsennotierten Zielen.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/outside-in-assessment.md
- assets/templates/target-pipeline.md

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
