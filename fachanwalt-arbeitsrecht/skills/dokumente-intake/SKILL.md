---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Arbeitsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-ar-kuendigungspruefung-fazugang-arbeitgeber` — Allgemein Ar Kuendigungspruefung Fazugang Arbeitgeber
- `ar-aufhebungsvertrag-konkurrenzklausel-fachanwalt-arbeitsrecht` — Ar Aufhebungsvertrag Konkurrenzklausel Fachanwalt Arbeitsrecht
- `ar-betriebsuebergang-ar-einfuehrung-ar-leiharbeit` — Ar Betriebsuebergang Ar Einfuehrung Ar Leiharbeit
- `arbeitsgericht-abrechnung-vergleichsverhandlung-strategie-zugang` — Arbeitsgericht Abrechnung Vergleichsverhandlung Strategie Zugang
- `befristung-fao-unwirksam-fristennotiz` — Befristung Fao Unwirksam Fristennotiz
- `befristung-tzbfg-bem-verfahren-fazugang-kuendigungsfrist` — Befristung Tzbfg Bem Verfahren Fazugang Kuendigungsfrist
- `beteiligung-betriebsrat-erstgespraech-mandatsannahme-fachanwalt` — Beteiligung Betriebsrat Erstgespraech Mandatsannahme Fachanwalt
- `betriebsrat-betrvg-datum` — Betriebsrat Betrvg Datum
- `entgtranspg-fachanwalt-kschg` — Entgtranspg Fachanwalt Kschg
- `fachanwalt-arbeitsrecht-bag-betriebsratsanhoerung` — Fachanwalt Arbeitsrecht Bag Betriebsratsanhoerung
- `fachanwalt-arbeitsrecht-freistellungsklausel-sonderfall-ar` — Fachanwalt Arbeitsrecht Freistellungsklausel Sonderfall Ar
- `fachanwalt-arbeitsrecht-hinschg-kuendigungsschutzklage` — Fachanwalt Arbeitsrecht Hinschg Kuendigungsschutzklage
- `fazugang-arbeitnehmerverteidigung-fazugang-schriftform` — Fazugang Arbeitnehmerverteidigung Fazugang Schriftform
- `fazugang-einwurf-einschreiben-zugang-urlaub-inhalt-umschlags` — Fazugang Einwurf Einschreiben Zugang Urlaub Inhalt Umschlags

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Arbeitsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: AGG, BetrVG, EntgTranspG, KSchG, TzBfG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Arbeitnehmer.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
