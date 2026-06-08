---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Nachbarschaftsstreit Prüfer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `anspruchslandkarte-bgb-aufforderungsschreiben-nachbar` — Anspruchslandkarte Bgb Aufforderungsschreiben Nachbar
- `aufforderung-beweise-red-grenzbaum` — Aufforderung Beweise Red Grenzbaum
- `drohender-einsturz-einfriedung-zaun-einstweilige-verfuegung` — Drohender Einsturz Einfriedung Zaun Einstweilige Verfuegung
- `fristennotiz-naechster-ueberbau-akten-grundstuecksaufnahme` — Fristennotiz Naechster Ueberbau Akten Grundstuecksaufnahme
- `grenzbaum-grenzanlage-hammerschlags-leiterrecht-horrorfall` — Grenzbaum Grenzanlage Hammerschlags Leiterrecht Horrorfall
- `hammerschlagsrecht-hecke-immissionen` — Hammerschlagsrecht Hecke Immissionen
- `immissionen-laerm-landesnachbarrecht-nach-grenzbebauung` — Immissionen Laerm Landesnachbarrecht Nach Grenzbebauung
- `klage-beweislast-nachbarrecht-nachbarschaftsstreit` — Klage Beweislast Nachbarrecht Nachbarschaftsstreit
- `nach-laermimmissionen-mediation-vorrang-nachbarrechtsuebersicht` — Nach Laermimmissionen Mediation Vorrang Nachbarrechtsuebersicht
- `nachbarrecht-kaltstart-triage` — Nachbarrecht Kaltstart Triage
- `notweg-ueberhang-sonderfall-edge` — Notweg Ueberhang Sonderfall Edge
- `notweg-zufahrt-selbsthilfe-eskalationsgrenzen-aeste` — Notweg Zufahrt Selbsthilfe Eskalationsgrenzen Aeste
- `ueberbau-ueberhang-aeste-mediation-nachbarschaftsfrieden` — Ueberbau Ueberhang Aeste Mediation Nachbarschaftsfrieden

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Nachbarschaftsstreit Pruefer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Mandant.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
