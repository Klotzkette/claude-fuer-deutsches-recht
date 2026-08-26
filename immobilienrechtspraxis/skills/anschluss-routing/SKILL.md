---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Immobilienrechtspraxis."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Immobilienrechtspraxis** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `betriebskostenabrechnung-erstellen-asset-management` — Betriebskostenabrechnung Erstellen Asset Management
- `betriebskostenabrechnung-pruefen-asset-management` — Betriebskostenabrechnung Prüfen Asset Management
- `case-gegen-grundbuchanalyse` — Case Gegen Grundbuchanalyse
- `case-management-grundbuchanalyse-immo` — Case Management Grundbuchanalyse Immo
- `gegen-verhandlung-vergleich-und-eskalation` — Gegen Verhandlung Vergleich und Eskalation
- `grundbuchanalyse` — Grundbuchanalyse
- `grundbuchanalyse-zahlen-schwellen-und-berechnung` — Grundbuchanalyse Zahlen Schwellen und Berechnung
- `immo-aufteilungsplan-weg` — Immo Aufteilungsplan WEG
- `immo-bauliche-veraenderung-energieausweis` — Immo Bauliche Veraenderung Energieausweis
- `immo-bauvertrag-vob-kaufvertrag-grundstueck` — Immo Bauvertrag VOB Kaufvertrag Grundstueck
- `immo-energieausweis` — Immo Energieausweis
- `immo-gewerbliche-mieter-konkurs` — Immo Gewerbliche Mieter Konkurs
- `immo-grundschuld-bestellung-makler-honorar` — Immo Grundschuld Bestellung Makler Honorar
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Immobilienrechtspraxis-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
