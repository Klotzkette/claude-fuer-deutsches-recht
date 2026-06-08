---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Handels Gesellschaftsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ag-vorstandsvertrag-hgr-aktionsbindungsvertrag-hgr` — Ag Vorstandsvertrag Hgr Aktionsbindungsvertrag Hgr
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `fachanwalt-fao-gesellschafterstreit` — Fachanwalt Fao Gesellschafterstreit
- `geschaeftsfuehrerhaftung-holding-strukturplanung-gmbh-cash` — Geschaeftsfuehrerhaftung Holding Strukturplanung Gmbh Cash
- `gesellschafterstreit-handelsvertreterausgleich-ma-due` — Gesellschafterstreit Handelsvertreterausgleich Ma Due
- `gesellschaftervertrag-geschaeftsfuehrerhaftung-hgr` — Gesellschaftervertrag Geschaeftsfuehrerhaftung Hgr
- `gmbh-beirat-vergleichsverhandlung-strategie` — Gmbh Beirat Vergleichsverhandlung Strategie
- `gmbhg-handels-handelsvertreterausgleich-international` — Gmbhg Handels Handelsvertreterausgleich International
- `hgb-kanzlei-beweislast-mopeg` — Hgb Kanzlei Beweislast Mopeg
- `hgesr-einfuehrung-hgr-due-erstgespraech-mandatsannahme` — Hgesr Einfuehrung Hgr Due Erstgespraech Mandatsannahme
- `hgesr-handelsvertreterausgleich-hgesr-mbg-registerrecht` — Hgesr Handelsvertreterausgleich Hgesr Mbg Registerrecht
- `hgr-dis-gesellschaftsrecht-token-fristennotiz` — Hgr Dis Gesellschaftsrecht Token Fristennotiz
- `orientierung-hgr-dlt-hgesr-grenzueberschreitende` — Orientierung Hgr Dlt Hgesr Grenzueberschreitende
- `partgg-pilotregime-sonderfall-mandantenentscheidung` — Partgg Pilotregime Sonderfall Mandantenentscheidung

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Handels Gesellschaftsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Handels- und Gesellschaftsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
