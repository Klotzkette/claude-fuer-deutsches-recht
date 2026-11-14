---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Medizinrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Medizinrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aerzte-quellenkarte` — Aerzte Quellenkarte
- `aerztewerbung-innovative-therapie` — Aerztewerbung Innovative Amnog Millionen
- `anaesthesie-hochrisiko-aufklaerung` — Anaesthesie Hochrisiko Approbation Digitales
- `apothekenrecht-arzneimittel-paragraf-78-amg` — Apothekenrecht Arzneimittel Paragraf 78 AMG
- `apothekenrecht-mehrparteien-konflikt-und-interessen` — Apothekenrecht Interessen Aufklaerung
- `arzthaftung-aufklaerung-bgb` — Arzthaftung Aufklaerung BGB
- `atmp-chain-of-identity` — Atmp Chain Classification
- `atmp-pharmakovigilanz-rmp` — Atmp Pharmakovigilanz Aufklaerungsfehler
- `aufklaerungsfehler` — Aufklaerungsfehler Behandlungsfehler
- `aufklaerungspflicht-paragraf-630e-bgb` — Aufklaerungspflicht Paragraf 630e BGB
- `behandlungsfehler-paragraf-630h-bgb` — Behandlungsfehler Paragraf 630h BGB
- `berufsrecht-verhandlung-vergleich-und-eskalation` — Berufsrecht BGB Einwilligung Sonderfall
- `beweislast-hightech-medizin` — Beweislast Hightech Biobank Consent
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Medizinrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
