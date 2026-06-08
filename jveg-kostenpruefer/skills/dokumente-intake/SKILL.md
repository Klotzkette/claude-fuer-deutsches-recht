---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Jveg Kostenpruefer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `beschwerde-dolmetscher-sonderfall-dolmetscherkosten` — Beschwerde Dolmetscher Sonderfall Dolmetscherkosten
- `fahrtkosten-festsetzung-interessen-freistehender` — Fahrtkosten Festsetzung Interessen Freistehender
- `gate-beweislast-jveg-quality` — Gate Beweislast Jveg Quality
- `jveg-anspruchsberechtigung-antragsgenerator-dolmetscher` — Jveg Anspruchsberechtigung Antragsgenerator Dolmetscher
- `jveg-dolmetscher-uebersetzer-fahrtkosten-festsetzung-beschwerde` — Jveg Dolmetscher Uebersetzer Fahrtkosten Festsetzung Beschwerde
- `jveg-gate-rechenblatt-sachverstaendigenrechnung` — Jveg Gate Rechenblatt Sachverstaendigenrechnung
- `jveg-gerichtsschreiben-jveg-kuerzung-wegfall` — Jveg Gerichtsschreiben Jveg Kuerzung Wegfall
- `jveg-sonstige-aufwendungen-uebernachtung-aufwand` — Jveg Sonstige Aufwendungen Uebernachtung Aufwand
- `jveg-vorschuss-kostenrisiko-zeugenentschaedigung` — Jveg Vorschuss Kostenrisiko Zeugenentschaedigung
- `jveg-zeugenentschaedigung-sachverstaendigengutachten-ki` — Jveg Zeugenentschaedigung Sachverstaendigengutachten Ki
- `uebernachtung-verdienstausfall-vorschuss` — Uebernachtung Verdienstausfall Vorschuss
- `uebersetzer-fristennotiz-jveg-sachverstaendigenrechnung` — Uebersetzer Fristennotiz Jveg Sachverstaendigenrechnung
- `zeugenentschaedigung` — Zeugenentschaedigung

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Jveg Kostenpruefer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: JVEG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Sachverständiger.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
