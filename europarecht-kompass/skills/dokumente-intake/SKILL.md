---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Europarecht Kompass** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `beihilfen-drafting-europarecht` — Beihilfen Drafting Europarecht
- `er-vorlageverfahren-eur-kommissionsverfahren-eur-mandant` — Er Vorlageverfahren Eur Kommissionsverfahren Eur Mandant
- `eur-anrufung-eur-state-beihilfen-vergaben` — Eur Anrufung Eur State Beihilfen Vergaben
- `europarecht-delegierte-durchfuehrungsakte-deutscher-denkfehler` — Europarecht Delegierte Durchfuehrungsakte Deutscher Denkfehler
- `europarecht-europarecht-mandantenmemo-quality-gate` — Europarecht Europarecht Mandantenmemo Quality Gate
- `europarecht-grundfreiheiten-binnenmarkt-grundrechte-charta` — Europarecht Grundfreiheiten Binnenmarkt Grundrechte Charta
- `europarecht-richtlinie-umsetzung-simulation-behoerde-verordnung` — Europarecht Richtlinie Umsetzung Simulation Behörde Verordnung
- `gegen-grundfreiheiten-livecheck-sonderfall` — Gegen Grundfreiheiten Livecheck Sonderfall
- `kommissionsverfahren-vorlageverfahren-interessen` — Kommissionsverfahren Vorlageverfahren Interessen
- `nationales-verfahren-vorlageverfahren-art-denkfehler` — Nationales Verfahren Vorlageverfahren Art Denkfehler
- `petitionsausschuss-mandantenentscheidung-richtlinien` — Petitionsausschuss Mandantenentscheidung Richtlinien
- `verordnungen-vorrang-vorrang-unmittelbare` — Verordnungen Vorrang Vorrang Unmittelbare
- `vorrang-unmittelbare-wettbewerb-kartell-anrufung-red` — Vorrang Unmittelbare Wettbewerb Kartell Anrufung Red

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Europarecht Kompass-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Nationale Gerichte.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
