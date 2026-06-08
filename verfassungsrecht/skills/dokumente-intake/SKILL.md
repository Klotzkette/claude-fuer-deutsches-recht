---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Verfassungsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `materielle-petition-sonderfall-recherche` — Materielle Petition Sonderfall Recherche
- `rechtsprechungsgetrieben-rechtsweg-bverfg-verfahrenssicht` — Rechtsprechungsgetrieben Rechtsweg Bverfg Verfahrenssicht
- `sicht-spezialkanzlei-unter` — Sicht Spezialkanzlei Unter
- `verfassung-beweislast-verfassungsbeschwerde` — Verfassung Beweislast Verfassungsbeschwerde
- `verfassung-grundgesetz-verfassung-organstreitverfahren` — Verfassung Grundgesetz Verfassung Organstreitverfahren
- `verfassung-grundrechte-juristische-uebersicht-eu` — Verfassung Grundrechte Juristische Uebersicht Eu
- `verfassung-konkrete-normenkontrolle-parteiverbot-petition` — Verfassung Konkrete Normenkontrolle Parteiverbot Petition
- `verfassung-staatsorganisation-verfassungsrechtliche` — Verfassung Staatsorganisation Verfassungsrechtliche
- `verfassungsbeschwerde-entwurf-formelle-verfassungsmaessigkeit` — Verfassungsbeschwerde Entwurf Formelle Verfassungsmaessigkeit
- `verfassungsrecht-verfassung-abstrakte-verfassung-bund` — Verfassungsrecht Verfassung Abstrakte Verfassung Bund
- `vfgr-bundestreue-foederalismus-grundrechtspruefung-bauleiter` — Vfgr Bundestreue Foederalismus Grundrechtspruefung Bauleiter

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Verfassungsbeschwerde, Antrag auf einstweilige Anordnung, Annahmebeschluss, BVerfGE-Entscheidung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Verfassungsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: GG Art. 1–19, 20, 28, 33, 38, 79, 93, 100, BVerfGG §§ 13, 23, 31, 32, 90–95a, EMRK Art. 6, 8, 10, 13 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Beschwerdeführer.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
