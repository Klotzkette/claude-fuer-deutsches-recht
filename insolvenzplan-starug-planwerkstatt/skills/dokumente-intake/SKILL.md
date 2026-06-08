---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Insolvenzplan Starug Planwerkstatt** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abstimmung-anlagen-interessen-cram` — Abstimmung Anlagen Interessen Cram
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `down-red-gestaltender-gruppen` — Down Red Gestaltender Gruppen
- `insolvenzplan-intake-klassen` — Insolvenzplan Intake Klassen
- `ips-abstimmung-ips-anlagenpaket-ips-asset` — Ips Abstimmung Ips Anlagenpaket Ips Asset
- `ips-cramdown-ips-datenraum-ips-gestaltender` — Ips Cramdown Ips Datenraum Ips Gestaltender
- `ips-gerichtliche-ips-ips-steuern` — Ips Gerichtliche Ips Ips Steuern
- `ips-gruppen-ips-architektur-ips-integrierte` — Ips Gruppen Ips Architektur Ips Integrierte
- `ips-ips-sanierungskonzept-ips-sicherheiten` — Ips Ips Sanierungskonzept Ips Sicherheiten
- `ips-kaltstart-interview` — Ips Kaltstart Interview
- `ips-minderheitenschutz-ips-planbetroffene-ips-planvollzug` — Ips Minderheitenschutz Ips Planbetroffene Ips Planvollzug
- `ips-stabilisierung-ips-stakeholder-ips-plan` — Ips Stabilisierung Ips Stakeholder Ips Plan
- `ips-verfahrenswahl-restrukturierungsplan-ips-darstellender` — Ips Verfahrenswahl Restrukturierungsplan Ips Darstellender
- `ips-vergleichsrechnung-ipsplan-cram-ipsplan-gruppenbildung` — Ips Vergleichsrechnung Ipsplan Cram Ipsplan Gruppenbildung

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Insolvenzplan Starug Planwerkstatt-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: StaRUG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Schuldnerunternehmen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
