---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Aktenauszug Gerichtsverfahren** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aktenauszug-strukturpruefung-akzg-bauleiter-vertraulichkeit` — Aktenauszug Strukturpruefung Akzg Bauleiter Vertraulichkeit
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt-anwaltsschriftsatz` — Akzg Zeitstrahl Anlagenverzeichnis Extrakt Anwaltsschriftsatz
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anwaltsschriftsatz-beweislast-beweismittel-interessen` — Anwaltsschriftsatz Beweislast Beweismittel Interessen
- `arbeitsgerichtsverfahren-modus-terminkalender` — Arbeitsgerichtsverfahren Modus Terminkalender
- `beweismittel-gegenueberstellung-einleitungssatz-generator` — Beweismittel Gegenueberstellung Einleitungssatz Generator
- `erstellen-fristennotiz-gerichtsverfahren-verfahrensgeschichte` — Erstellen Fristennotiz Gerichtsverfahren Verfahrensgeschichte
- `gegenueberstellung-parteivortraege-rechtsargumente` — Gegenueberstellung Parteivortraege Rechtsargumente
- `parteivortrag-gegenueberstellung-rechtsargumente` — Parteivortrag Gegenueberstellung Rechtsargumente
- `sachverhaltschronologie-textbausteine-schnelle-stilrichtlinie` — Sachverhaltschronologie Textbausteine Schnelle Stilrichtlinie
- `schwerpunktthemen-identifikation-akten-aktenauszug` — Schwerpunktthemen Identifikation Akten Aktenauszug
- `strukturierter-strafprozess-modus-verwaltungsprozess-modus` — Strukturierter Strafprozess Modus Verwaltungsprozess Modus
- `verfahrensidentifikation-verfahrenszusammenfassung-absatz` — Verfahrensidentifikation Verfahrenszusammenfassung Absatz
- `verfahrensidentifikation-verfahrenszusammenfassung-rechtsweg` — Verfahrensidentifikation Verfahrenszusammenfassung Rechtsweg

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Aktenauszug Gerichtsverfahren-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Mandant.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
