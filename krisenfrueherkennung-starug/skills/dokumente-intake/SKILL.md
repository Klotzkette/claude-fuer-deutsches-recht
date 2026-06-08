---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Krisenfrueherkennung Starug** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `berater-drohende-fruehwarnsystem` — Berater Drohende Fruehwarnsystem
- `drohende-zahlungsunfaehigkeit-fortbestehensprognose-zweistufig` — Drohende Zahlungsunfaehigkeit Fortbestehensprognose Zweistufig
- `integrierte-interessen-kennzahlenset-mandantenentscheidung` — Integrierte Interessen Kennzahlenset Mandantenentscheidung
- `integrierte-planung-kennzahlenset-ampelsystem-kfe` — Integrierte Planung Kennzahlenset Ampelsystem Kfe
- `kfe-krisenstab-cross-class-dokumentationspflicht-protokollierung` — Kfe Krisenstab Cross Class Dokumentationspflicht Protokollierung
- `kfe-restrukturierungsbeauftragter-stabilisierungsanordnung` — Kfe Restrukturierungsbeauftragter Stabilisierungsanordnung
- `krisenfrueherkennung-krisenmanagement-monats` — Krisenfrueherkennung Krisenmanagement Monats
- `krisenstadien-fristennotiz-starug-gf-haftung` — Krisenstadien Fristennotiz Starug Gf Haftung
- `mandantenbrief-warnung-paragraph-starug-warnpflicht` — Mandantenbrief Warnung Paragraph Starug Warnpflicht
- `pflicht-planung-restrukturierungsplan` — Pflicht Planung Restrukturierungsplan
- `pflichtenkollision-shift-restructuring-lounge` — Pflichtenkollision Shift Restructuring Lounge
- `restrukturierungsplan-architektur-rollierende` — Restrukturierungsplan Architektur Rollierende
- `stabilisierungsanordnung-vollstreckungssperre` — Stabilisierungsanordnung Vollstreckungssperre

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Frühwarnsystem-Bericht, Restrukturierungsanzeige, Restrukturierungsplan, Sanierungsmoderation-Antrag, Stabilisierungsanordnung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Krisenfrüherkennung und StaRUG-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: StaRUG §§ 1, 29, 31, 39, 49–55, 84, 102, InsO §§ 15a, 17, 18, 19, HGB § 252, IDW S 11 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Geschäftsführer, Aufsichtsrat, Restrukturierungsbeauftragter, Restrukturierungsgericht (LG) prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Geschäftsführung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
