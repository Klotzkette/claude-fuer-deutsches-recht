---
name: dokumente-intake
description: "Dokumentenintake für Prozessrecht (ZPO/VwGO/StPO/SGG): sortiert Klageschrift, Klageerwiderung, Schriftsätze, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Prozessrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher ZPO Proz Bauleiter Eilverfahren
- `anspruchstabelle-beweislast` — Anspruchstabelle Beweislast
- `anspruchstabelle-gegenseite-interessen` — Anspruchstabelle Gegenseite Interessen
- `anwaltsgeheimnis-pruefung` — Anwaltsgeheimnis Pruefung
- `argumentationsverbesserung-red-team` — Argumentationsverbesserung RED Team
- `beweissicherung-einstweilige-verfuegung` — Beweissicherung Einstweilige Verfuegung
- `chronologie` — Chronologie
- `eilverfahren-risikoampel-und-gegenargumente` — Eilverfahren Risikoampel und Gegenargumente
- `einstweilige-verfuegung` — Einstweilige Verfuegung
- `gegenseite-mehrparteien-konflikt-und-interessen` — Gegenseite Mehrparteien Konflikt und Interessen
- `gegenseite-status-mahnbescheid-mahnschreiben` — Gegenseite Status Mahnbescheid Mahnschreiben
- `kaltstart-interview` — Kaltstart Interview
- `mahnbescheid` — Mahnbescheid
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

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
