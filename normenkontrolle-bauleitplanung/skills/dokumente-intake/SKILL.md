---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Normenkontrolle Bauleitplanung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abwaegungsgebot-1-abs-7-baugb` — Abwaegungsgebot 1 Abs 7 Baugb
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `normenkontrolle-satzungsnormenkontrolle-47-vwgo` — Allgemeine Satzungsnormenkontrolle 47 Vwgo
- `allgemeine-satzungsnormenkontrolle-anpassungsgebot` — Allgemeine Satzungsnormenkontrolle Anpassungsgebot
- `anfechtung-antragsbefugnis-red-antragstellervertretung` — Anfechtung Antragsbefugnis Red Antragstellervertretung
- `anpassungsgebot-flaechennutzungsplan` — Anpassungsgebot Flaechennutzungsplan
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis Eigentuemer Nachbar
- `artenschutz-naturschutz-aufstellungsbeschluss-bekanntmachung` — Artenschutz Naturschutz Aufstellungsbeschluss Bekanntmachung
- `artenschutz-naturschutz-planung` — Artenschutz Naturschutz Planung
- `aufstellungsbeschluss-bekanntmachung` — Aufstellungsbeschluss Bekanntmachung
- `aufstellungsbeschluss-mandantenentscheidung-bauleitplanung` — Aufstellungsbeschluss Mandantenentscheidung Bauleitplanung
- `bayvgh-bekanntmachung-beweislast-eilantrag-abs` — Bayvgh Bekanntmachung Beweislast Eilantrag Abs
- `bebauungsplaenen-kommunalabgaben-beitragssatzungen` — Bebauungsplaenen Kommunalabgaben Beitragssatzungen
- `benutzungssatzung-kommunale-einrichtung` — Benutzungssatzung Kommunale Einrichtung

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Normenkontrolle Bauleitplanung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: § 47 VwGO vor BayVGH und OVG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Antragsteller (Anwohner/Nachbargemeinde).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
