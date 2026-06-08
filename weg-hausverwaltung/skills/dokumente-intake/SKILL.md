---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Weg Hausverwaltung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abrechnung-ist-plan-mieterschnittstelle` — Abrechnung Ist Plan Mieterschnittstelle
- `anwalt-amtsgericht-gewerbe-restaurant-grossakte` — Anwalt Amtsgericht Gewerbe Restaurant Grossakte
- `bad-umbau-barrierefreie-einladung-bauliche-veraenderung` — Bad Umbau Barrierefreie Einladung Bauliche Veraenderung
- `bad-umbau-bodengleiche-dusche-sondereigentum-gemeinschaft` — Bad Umbau Bodengleiche Dusche Sondereigentum Gemeinschaft
- `barrierefreie-einladung-protokoll-versammlung` — Barrierefreie Einladung Protokoll Versammlung
- `bauliche-veraenderung-aufzug-treppenlift-20-abs-2-weg` — Bauliche Veraenderung Aufzug Treppenlift 20 Abs 2 Weg
- `bauliche-veraenderungen-20-weg` — Bauliche Veraenderungen 20 Weg
- `bauliche-veraenderungen-beirat-controlling-beschlussanfechtung` — Bauliche Veraenderungen Beirat Controlling Beschlussanfechtung
- `beirat-controlling-verwalter` — Beirat Controlling Verwalter
- `beschlussanfechtung-risiko` — Beschlussanfechtung Risiko
- `beschlusssammlung-betriebskosten-interessen` — Beschlusssammlung Betriebskosten Interessen
- `beschlusssammlung-protokoll` — Beschlusssammlung Protokoll
- `beschlusssammlung-protokoll-beschlussvorlagen-erstellen` — Beschlusssammlung Protokoll Beschlussvorlagen Erstellen
- `beschlussvorlagen-erstellen` — Beschlussvorlagen Erstellen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Eigentümerversammlungsprotokoll, Beschlusssammlung, Jahresabrechnung, Wirtschaftsplan, Verwaltervertrag, Teilungserklärung, Gemeinschaftsordnung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die WEG-Hausverwaltung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: WEG §§ 9a, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 44, 45, 46, 47, BGB §§ 535 ff., HOAI, BetrKV — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Verwalter, Eigentümergemeinschaft, Verwaltungsbeirat, AG der Belegenheit, Handwerker, Vorverwalter prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an WEG-Eigentümer.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
