---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Bank Kapitalmarktrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Bank Kapitalmarktrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `anlageberatung-fehlerhaft` — Anlageberatung Fehlerhaft Cybertrading
- `anlageberatungsfehler-pruefen` — Anlageberatungsfehler Bankrecht Akkreditiv
- `bankaufsicht-erlaubnis-und-vertrieb` — Bankaufsicht Erlaubnis Emissionsprospekt
- `bankrecht-buergschaft-aval-garantie-routing` — Bankrecht Buergschaft Aval Garantieabruf
- `bankrecht-privatbuergschaft-sittenwidrigkeit` — Bankrecht Privatbuergschaft Regress BK
- `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` — Bausparvertrag Zinsanpassung BGH XI ZR 78 22
- `beratungshaftung-zahlen-schwellen-und-berechnung` — Beratungshaftung Haftung Beweislast BK CUM
- `bk-bankenfehlberatung-grundzuege` — BK Bankenfehlberatung Grundzuege Einfuehrung
- `bk-mifid-suitability-spezial` — BK Mifid BK Prip Erstgespraech Mandatsannahme
- `cum-ex-beihilfe-bgh-1-str-519-20` — CUM EX Beihilfe BGH 1 STR 519 20
- `dispokredit-zinsanpassung-bgh-xi-zr-78-08` — Dispokredit Zinsanpassung BGH XI ZR 78 08
- `einstieg-schnelltriage-fallrouting` — FA Bank Kapitalmarkt BK Bafin Chronologie
- `workflow-fristen-und-risikoampel` — FA Bank Kapitalmarkt Fristen Risiko Mandant
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Bank Kapitalmarktrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
