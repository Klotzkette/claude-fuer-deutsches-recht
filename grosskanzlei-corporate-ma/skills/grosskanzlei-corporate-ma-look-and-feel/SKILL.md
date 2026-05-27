---
name: grosskanzlei-corporate-ma-look-and-feel
description: "Corporate-Deal-Workspace Darstellung und Ausgabeformat: Anwendungsfall alle sichtbaren Outputs sollen im einheitlichen M&A-Kanzleistil erscheinen — ruhig, edel, deal-informationsdicht ohne Marketing-Ton. Big-Law-Standard, Partnerqualitaet. Pruefraster Statuskarten-Format, Ampelfarben, Deal-Phasenlayout, Risikokategorien, Owner-Matrix-Darstellung. Output konsistente visuelle Arbeitsoberflaeche fuer Partner, Counsel, Associate und Mandant. Abgrenzung zu Ausgabe-Versand-Signing fuer tatsaechlichen Versand und zu Schreibcanvas fuer inhaltliche Qualitaet."
---

# Corporate-Cowork-Look

## Zweck

Definiert die sichtbare Oberfläche: sehr ruhig, edel, bläulich-silbern mit warmem Orange für Entscheidungspunkte, dichte Deal-Information statt Marketing.

## Arbeitsmodus

- Jede sichtbare Ausgabe als Arbeitsfläche für Partner, Counsel, Associates und Mandanten denken.
- Statuskarten für Dealphase, Risiko, Workstream, Owner, Deadline und Freigabe verwenden.
- Keine verspielten Texte; kurze, belastbare Beschriftungen.
- Bei komplexen Workflows Tabs für Deal, Datenraum, DD, SPA, Closing und PMI verwenden.

## Rote Schwellen

- Text überlappt Tabellen oder Karten.
- Ampel- oder Freigabestatus fehlt.
- Unerklärte Farben oder dekorative Flächen verdecken Risiko.

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

- assets/templates/cowork-ma-designsystem.md
- assets/templates/cowork-ma-dashboard.md
- assets/templates/workflow-statuskarte.md

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
