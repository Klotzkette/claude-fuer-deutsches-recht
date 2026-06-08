---
name: dokumente-intake
description: "Dokumentenintake für Arbeitszeugnis-Analyse: sortiert Erstes Zeugnis, Berichtigungszeugnis, Zwischenzeugnis, prüft Datum, Absender, Frist und Beweiswert (Leistungsbeurteilungen, E-Mail-Verkehr HR); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Arbeitszeugnis Analyse** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `ampelsystem-tabellenausgabe` — Ampelsystem Tabellenausgabe
- `arbeitszeugnis-ampelsystem-dokumentenmatrix-lueckenliste` — Arbeitszeugnis Ampelsystem Dokumentenmatrix Lueckenliste
- `arbeitszeugnis-codeworte-compliance-dokumentation-aktenvermerk` — Arbeitszeugnis Codeworte Compliance Dokumentation Aktenvermerk
- `arbeitszeugnis-deutscher-tatbestandsmerkmale-beweisfragen` — Arbeitszeugnis Deutscher Tatbestandsmerkmale Beweisfragen
- `arbeitszeugnis-geheimcodes-schriftsatz-brief-memo-bausteine` — Arbeitszeugnis Geheimcodes Schriftsatz Brief Memo Bausteine
- `arbeitszeugnis-gruen-behoerden-gerichts-registerweg` — Arbeitszeugnis Gruen Behoerden Gerichts Registerweg
- `arbeitszeugnis-negative-zahlen-schwellenwerte-berechnung` — Arbeitszeugnis Negative Zahlen Schwellenwerte Berechnung
- `arbeitszeugnis-orange-risikoampel-gegenargumente` — Arbeitszeugnis Orange Risikoampel Gegenargumente
- `arbeitszeugnis-schaufenster-verhandlung-vergleich-eskalation` — Arbeitszeugnis Schaufenster Verhandlung Vergleich Eskalation
- `arbeitszeugnis-zeugnisanalyse-wortlaut-codes` — Arbeitszeugnis Zeugnisanalyse Wortlaut Codes
- `aufforderungsschreiben-arbeitgeber` — Aufforderungsschreiben Arbeitgeber
- `azubi-zeugnis-analyse` — Azubi Zeugnis Analyse
- `bereichs-drift-detektor` — Bereichs Drift Detektor
- `einstieg-routing` — Einstieg Routing
- `output-waehlen` — Output Waehlen

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
