---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Urheber Medienrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Urheber Medienrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abmahnung-sonderfall-edge-case` — Abmahnung Sonderfall Bild Eigenen
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme Fachanwalt
- `workflow-mandantenkommunikation` — FA Urheber Medien Mandant Redteam Gate
- `einstieg-schnelltriage-fallrouting` — FA Urheber Medien Start Chronologie Fristen
- `erstpruefung-und-mandatsziel` — Fachanwalt Gewerblicher Kanzlei
- `filesharing-stoererhaftung` — Filesharing Stoererhaftung
- `filmrecht-paragraf-89-urhg` — Filmrecht Paragraf 89 Urhg
- `gegendarstellung-fehlerkatalog` — Gegendarstellung Fehlerkatalog
- `gegendarstellung-presse` — Gegendarstellung Presse Mandat Triage
- `gegendarstellung-presse` — Gegendarstellung Presse MOD Erklaerung
- `link-haftung-paragraf-7-tmg` — Link Haftung Paragraf 7 TMG
- `medienrecht-fristen-form-und-zustaendigkeit` — Medienrecht Lizenzvertrag Urhmr
- `medienstaatsvertrag-quellenkarte` — Medienstaatsvertrag Quellenkarte
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Urheber Medienrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
