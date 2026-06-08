---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Tabellenreview 3d** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `aggregation-spaltenprompts-definieren-arbeitsblatt` — Aggregation Spaltenprompts Definieren Arbeitsblatt
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `arbeitsblatt-perspektiven-definieren` — Arbeitsblatt Perspektiven Definieren
- `audit-trail-protokoll` — Audit Trail Protokoll
- `belegkette-rueckverfolgung` — Belegkette Rueckverfolgung
- `belegkette-rueckverfolgung-caching-rerun-dokumentstapel` — Belegkette Rueckverfolgung Caching Rerun Dokumentstapel
- `caching-und-teil-rerun` — Caching Und Teil Rerun
- `datenpunkt-dokument-excel-beweislast` — Datenpunkt Dokument Excel Beweislast
- `dokumentstapel-aufnehmen` — Dokumentstapel Aufnehmen
- `excel-multi-kreuzblatt-konsistenzpruefung-pdf-bericht` — Excel Multi Kreuzblatt Konsistenzpruefung Pdf Bericht
- `excel-multi-sheet-export` — Excel Multi Sheet Export
- `gestapelt-immobilien-massenpruefung-interessen` — Gestapelt Immobilien Massenpruefung Interessen
- `kreuzblatt-konsistenzpruefung` — Kreuzblatt Konsistenzpruefung
- `mehrblatt-sonderfall-onboarding-perspektiven` — Mehrblatt Sonderfall Onboarding Perspektiven

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Tabellenreview 3D-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Datenverantwortlicher.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
