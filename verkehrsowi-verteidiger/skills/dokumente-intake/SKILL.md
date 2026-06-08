---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Verkehrsowi Verteidiger** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `alkohol-drogen-beweisverwertung-standardisiert-verkehrsowi` — Alkohol Drogen Beweisverwertung Standardisiert Verkehrsowi
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren-geschwindigkeit` — Anhörung Verkehrsowi Einspruch Messverfahren Geschwindigkeit
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `hauptverhandlung-sonderfall-messakte-messung-fahrverbot` — Hauptverhandlung Sonderfall Messakte Messung Fahrverbot
- `punkte-rotlicht-verkehrsowi` — Punkte Rotlicht Verkehrsowi
- `simulation-training-verjaehrung-zustellung-zeugen-polizei` — Simulation Training Verjährung Zustellung Zeugen Polizei
- `verkehrsowi-haertefall-fahrverbot-hauptverhandlung-amtsgericht` — Verkehrsowi Haertefall Fahrverbot Hauptverhandlung Amtsgericht
- `verkehrsowi-punkte-fahrverbot-rechtsbeschwerde-rotlicht-abstand` — Verkehrsowi Punkte Fahrverbot Rechtsbeschwerde Rotlicht Abstand
- `verteidiger-beweislast-verkehrsowi-aktenanlage-akteneinsicht` — Verteidiger Beweislast Verkehrsowi Aktenanlage Akteneinsicht
- `vowi-akteneinsicht` — Vowi Akteneinsicht
- `vowi-bussgeldbescheid-verkehrsowi-quality-gate` — Vowi Bussgeldbescheid Verkehrsowi Quality Gate
- `vowi-handyverstoss-akteneinsicht-alkohol` — Vowi Handyverstoss Akteneinsicht Alkohol

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Verkehrsowi Verteidiger-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Betroffener.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
