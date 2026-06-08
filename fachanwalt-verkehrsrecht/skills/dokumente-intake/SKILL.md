---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Verkehrsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-verk-unfallregulierung-workflow-chronologie` — Allgemein Verk Unfallregulierung Chronologie
- `autonom-bezuege-fachanwalt` — Autonom Bezuege Fachanwalt
- `bussgeld-unfall-haftungsquote-vkr-totalschaden` — Bussgeld Unfall Haftungsquote Vkr Totalschaden
- `erstgespraech-mandatsannahme-verkehr-autonom-fahrerlaubnis` — Erstgespraech Mandatsannahme Verkehr Autonom Fahrerlaubnis
- `fahrerlaubnis-kanzlei-personen` — Fahrerlaubnis Kanzlei Personen
- `mandat-triage-schriftsatzkern-substantiierung-315c` — Mandat Triage Schriftsatzkern Substantiierung 315c
- `mpu-vorbereitung-orientierung-regulierungsanforderung` — Mpu Vorbereitung Orientierung Regulierungsanforderung
- `pflvg-quoten-sonderfall-stgb` — Pflvg Quoten Sonderfall Stgb
- `stvg-verkehr-fristennotiz-vkr-blitzer` — Stvg Verkehr Fristennotiz Vkr Blitzer
- `stvo-unfallregulierung-beweislast-verkehrsrecht` — Stvo Unfallregulierung Beweislast Verkehrsrecht
- `tempo-messung-unfallregulierung-quoten-versicherer` — Tempo Messung Unfallregulierung Quoten Versicherer
- `verk-fahrerlaubnisrecht-leitfaden-fahrtenbuch-anordnung` — Verk Fahrerlaubnisrecht Leitfaden Fahrtenbuch Anordnung
- `verkehrsstrafrecht-interessen-verkehrsunfall` — Verkehrsstrafrecht Interessen Verkehrsunfall
- `vkr-bussgeldverfahren-bussgeld-einspruch-bussgeldbescheid` — Vkr Bussgeldverfahren Bussgeld Einspruch Bussgeldbescheid

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Verkehrsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: PflVG, StVG, VVG, §§ 315c 316 StGB — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Betroffener/Geschädigter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
