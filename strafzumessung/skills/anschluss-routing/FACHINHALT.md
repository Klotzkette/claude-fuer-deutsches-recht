---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Strafzumessung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Strafzumessung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `153a-stpo-iii-bewaehrung-stgb` — 153a STPO III Bewaehrung STGB
- `besonders-formular-portal-und-einreichung` — Besonders Formular Portal und Einreichung
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung 56 STGB Positive Sozialprognose
- `bewaehrung-auflagen-bewaehrungswiderruf-56f` — Bewaehrung Auflagen Bewaehrungswiderruf 56F
- `bewaehrung-interessen-deutschem` — Bewaehrung Interessen Deutschem
- `bewaehrungswiderruf-56f-stgb` — Bewaehrungswiderruf 56F STGB
- `deutschem-tatbestand-beweis-und-belege` — Deutschem Tatbestand Beweis und Belege
- `freiheitsstrafe-compliance-dokumentation-und-akte` — Freiheitsstrafe Compliance Dokumentation und Akte
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Freiheitsstrafe Ohne Bewaehrung Vollstreckung
- `freiheitsstrafe-strafmass-geldstrafe` — Freiheitsstrafe Strafmass Geldstrafe
- `geldstrafe-grossen-rechtsmittel` — Geldstrafe Großen Rechtsmittel
- `geldstrafe-tagessatzanzahl-bestimmen` — Geldstrafe Tagessatzanzahl Bestimmen
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Geldstrafe VS Freiheitsstrafe 47 STGB
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Strafzumessung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 56 StGB Bewährungszeit 2–5 Jahre, § 57 StGB 2/3-Reststrafenaussetzung, § 57a StGB lebenslange Freiheitsstrafe nach 15 Jahren), notwendige Dokumente (Bewährungsauflage, Tatumstandskatalog, Vorstrafenregisterauszug, Sachverständigengutachten, Schuldfähigkeitsbeurteilung), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Tatrichter, Verteidiger, Staatsanwaltschaft, Bewährungshelfer, Vollstreckungsbehörde oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
