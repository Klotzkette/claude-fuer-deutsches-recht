---
name: anschluss-routing
description: "Anschluss-Routing für Immobilienrechtspraxis: wählt den nächsten Spezial-Skill nach Engpass (Vormerkung, Notarvertrag, Grundbuchauszug, Energieausweis), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Immobilienrechtspraxis** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `betriebskostenabrechnung-erstellen-asset-management` — Betriebskostenabrechnung Erstellen Asset Management
- `betriebskostenabrechnung-pruefen-asset-management` — Betriebskostenabrechnung Pruefen Asset Management
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

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Immobilienrechtspraxis.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 45 WEG
- Art. 28 DSGVO
- § 144 BauGB
- § 20 WEG
- § 28 WEG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

