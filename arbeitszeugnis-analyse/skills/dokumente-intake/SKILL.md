---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Arbeitszeugnis Analyse** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `ampelsystem-tabellenausgabe` — Ampelsystem Tabellenausgabe
- `aufforderungsschreiben-arbeitgeber` — Aufforderungsschreiben Arbeitgeber
- `azubi-zeugnis-analyse` — Azubi Zeugnis Analyse
- `bereichs-drift-detektor` — Bereichs Drift Detektor
- `branchen-spezifische-formulierungen` — Branchen Spezifische Formulierungen
- `erstgespraech-und-mandatsannahme` — Erstgespraech Und Mandatsannahme
- `geheimcode-katalog` — Geheimcode Katalog
- `gesamtnoten-aggregation` — Gesamtnoten Aggregation
- `gruen-flaggen-katalog` — Gruen Flaggen Katalog
- `klage-strategie-zeugnisberichtigung` — Klage Strategie Zeugnisberichtigung
- `leistungsbeurteilung-analyse` — Leistungsbeurteilung Analyse
- `leitende-positionen-zeugnisse` — Leitende Positionen Zeugnisse
- `mandantenbericht-zeugnisanalyse` — Mandantenbericht Zeugnisanalyse
- `muster-arbeitszeugnis-gemischte-noten` — Muster Arbeitszeugnis Gemischte Noten

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Arbeitszeugnis Analyse-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Mandant/Arbeitnehmer.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
