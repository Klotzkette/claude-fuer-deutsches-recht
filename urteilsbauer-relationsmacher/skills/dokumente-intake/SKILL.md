---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Urteilsbauer Relationsmacher** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aktenintake-zivil` — Aktenintake Zivil
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amts-aktenintake-zivil-anspruchsgrundlagen` — Amts Aktenintake Zivil Anspruchsgrundlagen
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen Prüfen
- `berufungsfest-beschluss-bauen-beweisbeschluss-vorbereiten` — Berufungsfest Beschluss Bauen Beweisbeschluss Vorbereiten
- `berufungsfest-pruefen` — Berufungsfest Prüfen
- `beschluss-bauen-zpo` — Beschluss Bauen Zpo
- `beweisbeschluss-vorbereiten` — Beweisbeschluss Vorbereiten
- `beweiswuerdigung-mit-richter-input` — Beweiswuerdigung Mit Richter Input
- `beweiswuerdigung-richter-cisg-dsgvo-rechtswidriges` — Beweiswuerdigung Richter Cisg Dsgvo Rechtswidriges
- `cisg-pruefen` — Cisg Prüfen
- `dokumente-rendern-urteil-docx` — Dokumente Rendern Urteil Docx
- `dsgvo-rechtswidriges-produkt` — Dsgvo Rechtswidriges Produkt
- `entscheidungsgruende-redaktion-familienrichter-input` — Entscheidungsgruende Redaktion Familienrichter Input

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Urteilsbauer Relationsmacher-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: ZPO — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Richter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
