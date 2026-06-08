---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Miet Wohnungseigentumsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-abschlusskontrolle-weg-anschluss-router` — Allgemein Abschlusskontrolle Weg Anschluss Router
- `antennen-satellitenschuessel-aufrechnung-zurueckbehaltung` — Antennen Satellitenschuessel Aufrechnung Zurueckbehaltung
- `bauliche-veraenderung-betriebskosten-schnellscan-workflow` — Bauliche Veraenderung Betriebskosten Schnellscan Workflow
- `baurecht-schnittstelle-belegeinsicht-betriebskosten-berliner` — Baurecht Schnittstelle Belegeinsicht Betriebskosten Berliner
- `beschlussanfechtung-abrechnungsfrist-nachforderung-erhalt` — Beschlussanfechtung Abrechnungsfrist Nachforderung Erhalt
- `betrkv-interessen-bgb-co2kostenaufteilung-diskriminierung-agg` — Betrkv Interessen Bgb Co2kostenaufteilung Diskriminierung Agg
- `dokumentenstapel-sortieren-first-year-fotobeweis-mangel-workflow` — Dokumentenstapel Sortieren First Year Fotobeweis Mangel Workflow
- `eigenbedarf-personenkreis-energieausweis-mietrecht-erhaltung-vs` — Eigenbedarf Personenkreis Energieausweis Mietrecht Erhaltung Vs
- `fachanwalt-miet-wohnungseigentumsrecht-mieterhoehung-weg` — Fachanwalt Miet Wohnungseigentumsrecht Mieterhoehung Weg
- `fachanwalt-steuer-schnittstelle-erstgespraech-mandatsannahme` — Fachanwalt Steuer Schnittstelle Erstgespraech Mandatsannahme
- `gartenpflege-baumfaellung-gewerberaum-betriebspflicht` — Gartenpflege Baumfaellung Gewerberaum Betriebspflicht
- `geg-waermepumpe-gerichtstermin-vorbereitung-gewerberaum-intake` — Geg Waermepumpe Gerichtstermin Vorbereitung Gewerberaum Intake
- `gewerberaum-umsatzmiete-gewerberaummiete-glasfaser-kabel` — Gewerberaum Umsatzmiete Gewerberaummiete Glasfaser Kabel
- `heizkostenverordnung-heizung-warmwasser-indexmiete-anpassung` — Heizkostenverordnung Heizung Warmwasser Indexmiete Anpassung

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Miet Wohnungseigentumsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: GEG, WEG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Mieter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
