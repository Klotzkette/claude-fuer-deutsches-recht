---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Strafbefehl Verteidiger** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `deal-beweislast-einspruch-einspruchsentscheidung-folgen` — Deal Beweislast Einspruch Einspruchsentscheidung Folgen
- `einstellung-153a-hauptverhandlung-vorbereitung-strafbefehl` — Einstellung 153a Hauptverhandlung Vorbereitung Strafbefehl
- `einstellung-fahrerlaubnis-mandantenentscheidung-hauptverhandlung` — Einstellung Fahrerlaubnis Mandantenentscheidung Hauptverhandlung
- `gegen-strafbefehl-einspruch-strafbefehl-aktenanlage` — Gegen Strafbefehl Einspruch Strafbefehl Aktenanlage
- `nebenfolgen-fahrerlaubnis-strafbefehl-pflichtverteidiger` — Nebenfolgen Fahrerlaubnis Strafbefehl Pflichtverteidiger
- `nebenfolgen-strafbefehl-strafbefehls` — Nebenfolgen Strafbefehl Strafbefehls
- `rechtsmittel-nach-tagessaetze-geldstrafe-strafbefehl` — Rechtsmittel Nach Tagessaetze Geldstrafe Strafbefehl
- `stbv-einspruch-strafbefehl-fahrerlaubnis-auslaendischer-mandant` — Stbv Einspruch Strafbefehl Fahrerlaubnis Auslaendischer Mandant
- `stbv-strafbefehl-abwesenheit-vertretung-akteneinsicht` — Stbv Strafbefehl Abwesenheit Vertretung Akteneinsicht
- `strafbefehl-einlassung-deal-verstaendigung-einspruch` — Strafbefehl Einlassung Deal Verstaendigung Einspruch
- `strafbefehl-quality-gate-akteneinsicht` — Strafbefehl Quality Gate Akteneinsicht
- `tagessaetze-verstaendigung-sonderfall-verteidiger` — Tagessaetze Verstaendigung Sonderfall Verteidiger
- `verteidigung-wiedereinsetzung-zeugenstrategie-interessen` — Verteidigung Wiedereinsetzung Zeugenstrategie Interessen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Strafbefehl Verteidiger-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Beschuldigter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
