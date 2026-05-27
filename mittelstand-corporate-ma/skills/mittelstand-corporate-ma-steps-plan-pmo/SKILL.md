---
name: mittelstand-corporate-ma-steps-plan-pmo
description: "Deal-PMO und Steps Plan: Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing."
---

# Deal-PMO und Steps Plan

## Zweck

Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing.

## Arbeitsmodus

- Pflichten, Fristen, Bedingungen und Deliverables aus Dokumenten ziehen.
- Owner, Status, Beleg und Eskalation zuweisen.
- Woechentliche Deal-PMO-Ansicht erzeugen.
- Entscheidungen und Annahmen dokumentieren.

## Rote Schwellen

- Pflicht ohne Frist.
- Keine Eskalation für rote Punkte.
- Plan nicht mit Vertragsversion verknuepft.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/deal-pmo-weekly.md
- assets/templates/signing-closing-steps-plan.md

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
