---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Prozessrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher Zpo Proz Bauleiter Eilverfahren
- `anspruchstabelle` — Anspruchstabelle
- `anspruchstabelle-gegenseite-interessen-mahnbescheid` — Anspruchstabelle Gegenseite Interessen Mahnbescheid
- `beweissicherung-chronologie-einstweilige-verfuegung` — Beweissicherung Chronologie Einstweilige Verfuegung
- `gegenseite-status-mahnbescheid-mahnschreiben-aufnahme` — Gegenseite Status Mahnbescheid Mahnschreiben Aufnahme
- `mahnschreiben-entwurf-anwaltsgeheimnis` — Mahnschreiben Entwurf Anwaltsgeheimnis
- `mahnschreiben-erhalten-aktualisierung-aufnahme` — Mahnschreiben Erhalten Aktualisierung Aufnahme
- `mandat-briefing-mandat-schliessen-portfolio-status` — Mandat Briefing Mandat Schliessen Portfolio Status
- `mandat-mandate-prozessrecht` — Mandat Mandate Prozessrecht
- `proz-beweismittel-leitfaden-mediationsklage-guete` — Proz Beweismittel Leitfaden Mediationsklage Guete
- `prozessrecht-kaltstart-interview` — Prozessrecht Kaltstart Interview
- `prozessrecht-mandat-arbeitsbereich-abschnitt` — Prozessrecht Mandat Arbeitsbereich Abschnitt
- `prozessrechtliche-schriftsaetze-status` — Prozessrechtliche Schriftsaetze Status

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Prozessrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Mandant.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
