---
name: anschluss-routing
description: "Anschluss-Routing für Zwangsverwaltung ZVG: wählt den nächsten Spezial-Skill nach Engpass (Beschwerde gegen Anordnung, Anordnungsbeschluss, Verwalterbericht, Mietsachen-Akte), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Zwangsverwaltung Zvg** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `aktenanlage-objektcockpit` — Aktenanlage Objektcockpit
- `berichte-beschlagnahme-mietverwaltung-besitz` — Berichte Beschlagnahme Mietverwaltung Besitz
- `berichtswesen-besitzuebernahme-bestellung` — Berichtswesen Besitzuebernahme Bestellung
- `beschlagnahme-fristen-form-und-zustaendigkeit` — Beschlagnahme Fristen Form und Zustaendigkeit
- `beschlagnahme-mietverwaltung-start` — Beschlagnahme Mietverwaltung Start
- `beschlagnahme-oeffentliche-lasten` — Beschlagnahme Oeffentliche Lasten
- `besitz-dokumentenmatrix-und-lueckenliste` — Besitz Dokumentenmatrix und Lueckenliste
- `besitzuebernahme` — Besitzuebernahme
- `bestellung-beschlagnahme` — Bestellung Beschlagnahme
- `betriebskosten-hausgeld-bieterangebot` — Betriebskosten Hausgeld Bieterangebot
- `bieterangebot-bewertung` — Bieterangebot Bewertung
- `bieterangebote-mieten-oeffentliche` — Bieterangebote Mieten Oeffentliche
- `gate-fehlerkatalog` — Gate Fehlerkatalog
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Zwangsverwaltung Zvg-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Zwangsverwaltung ZVG.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
