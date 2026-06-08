---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Normenkontrolle Bauleitplanung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abwaegungsgebot-1-abs-7-baugb` — Abwaegungsgebot 1 Abs 7 Baugb
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `normenkontrolle-satzungsnormenkontrolle-47-vwgo` — Allgemeine Satzungsnormenkontrolle 47 Vwgo
- `allgemeine-satzungsnormenkontrolle-anpassungsgebot` — Allgemeine Satzungsnormenkontrolle Anpassungsgebot
- `anfechtung-antragsbefugnis-red-antragstellervertretung` — Anfechtung Antragsbefugnis Red Antragstellervertretung
- `anpassungsgebot-flaechennutzungsplan` — Anpassungsgebot Flaechennutzungsplan
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis Eigentuemer Nachbar
- `artenschutz-naturschutz-aufstellungsbeschluss-bekanntmachung` — Artenschutz Naturschutz Aufstellungsbeschluss Bekanntmachung
- `artenschutz-naturschutz-planung` — Artenschutz Naturschutz Planung
- `aufstellungsbeschluss-bekanntmachung` — Aufstellungsbeschluss Bekanntmachung
- `aufstellungsbeschluss-mandantenentscheidung-bauleitplanung` — Aufstellungsbeschluss Mandantenentscheidung Bauleitplanung
- `bayvgh-bekanntmachung-beweislast-eilantrag-abs` — Bayvgh Bekanntmachung Beweislast Eilantrag Abs
- `bebauungsplaenen-kommunalabgaben-beitragssatzungen` — Bebauungsplaenen Kommunalabgaben Beitragssatzungen
- `benutzungssatzung-kommunale-einrichtung` — Benutzungssatzung Kommunale Einrichtung

## Arbeitsweg

- Ergebnis sichten: Welche Normenkontrolle Bauleitplanung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Normenkontrolle Bauleitplanung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
