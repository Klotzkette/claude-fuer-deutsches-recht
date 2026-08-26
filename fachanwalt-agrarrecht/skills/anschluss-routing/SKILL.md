---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Agrarrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Agrarrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `agrar-einfuehrung-rechtsquellen` — Agrar Einfuehrung Rechtsquellen
- `agrar-jagdpacht-streit-spezial` — Agrar Jagdpacht Streit Mandantenfragen
- `agrar-tierhaltung-spezial-tieg` — Agrar Tierhaltung Erstgespraech
- `agrar-wolfsschaden-spezial` — Agrar Wolfsschaden Cross Glozez Foerderung
- `agrarerbe-pflichtteil-paragraf-2316-bgb-hoefeordnung` — Agrarerbe Pflichtteil Paragraf 2316 BGB Hoefeordnung
- `agrarflaeche-erwerbsbeschraenkung-paragraf-9-grdstvg-hofstelle` — Agrarflaeche Erwerbsbeschraenkung Paragraf 9 Grdstvg Hofstelle
- `agrarfoerderung-fid-ablehnung-paragraf-9-invekos` — Agrarfoerderung FID Ablehnung Paragraf 9 Invekos
- `agrarinvest-bonusverwirkung-paragraf-49-vwvfg-grw` — Agrarinvest Bonusverwirkung Paragraf 49 Vwvfg GRW
- `workflow-mandantenkommunikation` — Agrarrecht Mandantenkommunikation Redteam Qualitygate Hoeferecht
- `anerbenrecht-risikoampel-und-gegenargumente` — Anerbenrecht BGB Spezial Compliance
- `cross-zahlen-schwellen-und-berechnung` — Cross Duengeverordnung Interessen Erbrecht
- `direktzahlungen-quellenkarte` — Direktzahlungen Quellenkarte
- `duengeverordnung-rote-gebiete-paragraf-13a-duev-derogation` — Duengeverordnung Rote Gebiete Paragraf 13A Duev Derogation
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Agrarrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
