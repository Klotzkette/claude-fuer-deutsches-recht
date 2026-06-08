---
name: anschluss-routing
description: "Anschluss-Routing für Fachanwalt Agrarrecht: wählt den nächsten Spezial-Skill nach Engpass (Pachtjahr Kündigungsfristen, Pachtvertrag, GAP-Antrag, Grundbuchauszug), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Agrarrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `agrar-einfuehrung-rechtsquellen` — Agrar Einfuehrung Rechtsquellen
- `agrar-jagdpacht-streit-mandantenfragen` — Agrar Jagdpacht Streit Mandantenfragen
- `agrar-tierhaltung-erstgespraech` — Agrar Tierhaltung Erstgespraech
- `agrar-wolfsschaden-cross-glozez-foerderung` — Agrar Wolfsschaden Cross Glozez Foerderung
- `agrarerbe-pflichtteil-paragraf-2316-bgb-hoefeordnung` — Agrarerbe Pflichtteil Paragraf 2316 BGB Hoefeordnung
- `agrarflaeche-erwerbsbeschraenkung-paragraf-9-grdstvg-hofstelle` — Agrarflaeche Erwerbsbeschraenkung Paragraf 9 Grdstvg Hofstelle
- `agrarfoerderung-fid-ablehnung-paragraf-9-invekos` — Agrarfoerderung FID Ablehnung Paragraf 9 Invekos
- `agrarinvest-bonusverwirkung-paragraf-49-vwvfg-grw` — Agrarinvest Bonusverwirkung Paragraf 49 Vwvfg GRW
- `agrarrecht-mandantenkommunikation-redteam-qualitygate-hoeferecht` — Agrarrecht Mandantenkommunikation Redteam Qualitygate Hoeferecht
- `anerbenrecht-bgb-spezial-compliance` — Anerbenrecht BGB Spezial Compliance
- `cross-duengeverordnung-interessen-erbrecht` — Cross Duengeverordnung Interessen Erbrecht
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

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Agrarrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
