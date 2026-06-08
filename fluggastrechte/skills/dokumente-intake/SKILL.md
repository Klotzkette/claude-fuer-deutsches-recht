---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fluggastrechte** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abtretung-an-fluggastportal-spezial` — Abtretung An Fluggastportal Spezial
- `airline-bonitaet-und-vollstreckung` — Airline Bonitaet Und Vollstreckung
- `airline-standardausreden-annullierung-verspaetung-anschlussflug` — Airline Standardausreden Annullierung Verspaetung Anschlussflug
- `airline-standardausreden-pruefen` — Airline Standardausreden Prüfen
- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `annullierung-oder-verspaetung-einordnen` — Annullierung Oder Verspaetung Einordnen
- `anschlussflug-und-reiseplan` — Anschlussflug Und Reiseplan
- `ausnahmen-aussergewoehnliche-aussergewoehnliche-umstaende` — Ausnahmen Aussergewoehnliche Aussergewoehnliche Umstaende
- `ausnahmen-aussergewoehnliche-umstaende-pruefen` — Ausnahmen Aussergewoehnliche Umstaende Prüfen
- `aussergewoehnliche-distanz-interessen-erfassen` — Aussergewoehnliche Distanz Interessen Erfassen
- `aussergewoehnliche-umstaende-strikt` — Aussergewoehnliche Umstaende Strikt
- `distanz-und-ausgleich-berechnen` — Distanz Und Ausgleich Berechnen
- `flug-anschlussflug-codeshare-anspruch-uebersicht` — Flug Anschlussflug Codeshare Anspruch Uebersicht
- `flug-anschlussflug-codeshare-spezial` — Flug Anschlussflug Codeshare Spezial

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fluggastrechte-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.


## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)
## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Fluggast.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
