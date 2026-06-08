---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Handels Gesellschaftsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

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

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Handels Gesellschaftsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: AktG, GmbHG, HGB, MoPeG, PartGG, UmwG, § 14i, § 89b HGB — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Gesellschafter/Aktionäre.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
