---
name: anschluss-routing
description: "Anschluss-Routing für Fachanwalt Bank- und Kapitalmarktrecht: wählt den nächsten Spezial-Skill nach Engpass (Widerrufsfrist Verbraucherdarlehen 14 Tage § 355 BGB, Darlehensvertrag, Wertpapierorder, Beratungsprotokoll), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Bank Kapitalmarktrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `anlageberatung-fehlerhaft-cybertrading` — Anlageberatung Fehlerhaft Cybertrading
- `anlageberatungsfehler-bankrecht-akkreditiv` — Anlageberatungsfehler Bankrecht Akkreditiv
- `bankaufsicht-erlaubnis-emissionsprospekt` — Bankaufsicht Erlaubnis Emissionsprospekt
- `bankrecht-buergschaft-aval-garantieabruf` — Bankrecht Buergschaft Aval Garantieabruf
- `bankrecht-privatbuergschaft-regress-bk` — Bankrecht Privatbuergschaft Regress BK
- `bausparvertrag-zinsanpassung-bgh-xi-zr-78-22` — Bausparvertrag Zinsanpassung BGH XI ZR 78 22
- `beratungshaftung-haftung-beweislast-bk-cum` — Beratungshaftung Haftung Beweislast BK CUM
- `bk-bankenfehlberatung-grundzuege-einfuehrung` — BK Bankenfehlberatung Grundzuege Einfuehrung
- `bk-mifid-bk-prip-erstgespraech-mandatsannahme` — BK Mifid BK Prip Erstgespraech Mandatsannahme
- `cum-ex-beihilfe-bgh-1-str-519-20` — CUM EX Beihilfe BGH 1 STR 519 20
- `dispokredit-zinsanpassung-bgh-xi-zr-78-08` — Dispokredit Zinsanpassung BGH XI ZR 78 08
- `fa-bank-kapitalmarkt-bk-bafin-chronologie` — FA Bank Kapitalmarkt BK Bafin Chronologie
- `fa-bank-kapitalmarkt-fristen-risiko-mandant` — FA Bank Kapitalmarkt Fristen Risiko Mandant
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Bank Kapitalmarktrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Bank- und Kapitalmarktrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
