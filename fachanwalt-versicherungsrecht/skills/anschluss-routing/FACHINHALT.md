---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Versicherungsrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Versicherungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `berufsunfaehigkeit-paragraf-172-vvg` — Berufsunfaehigkeit Paragraf 172 VVG
- `versr-bu-anerkennt-was-spezial` — BU Anerkennt Leistungspruefung
- `cyber-loesegeld-sanktionsrecht` — Cyber Loesegeld Versr Deckungsanfrage
- `versr-d-o-claims-made-ausschluesse` — D O Spezialfall Deckungsklage Leitfaden
- `deckungsklage-mehrparteien-konflikt-und-interessen` — Deckungsklage Interessen Deckungspruefung
- `versr-deckungsprozess-215-vvg-beweislast` — Deckungsprozess VVG Einfuehrung Themen
- `do-deckungsabwehr` — DO Deckungsabwehr Lebensversicherung
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme
- `einstieg-schnelltriage-fallrouting` — FA Versicherungsrecht Start Chronologie Fristen
- `erstpruefung-und-mandatsziel` — Fachanwalt Kanzlei Krankenversicherung
- `fehlerkatalog` — Fehlerkatalog
- `gebaeudeversicherung-paragraf-86-vvg` — Gebaeudeversicherung Paragraf 86 VVG
- `haftpflicht-paragraf-100-vvg` — Haftpflicht Paragraf 100 VVG
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Versicherungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
