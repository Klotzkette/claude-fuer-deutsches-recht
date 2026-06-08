---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Berufsrecht Ki Vertragspruefung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `ai-act-rollen-kanzlei-provider-deployer-api` — Ai Act Rollen Kanzlei Provider Deployer Api
- `br-ki-vertragspruefung-brki-rollout-chronologie` — Allgemein Brki Rollout Chronologie
- `anbietern-belehrung-sonderfall-edge` — Anbietern Belehrung Sonderfall Edge
- `art-50-ki-vo-schriftsatz-marketing-chatbot` — Art 50 Ki Vo Schriftsatz Marketing Chatbot
- `avv-grenzpruefung-brki-anbieter-brki-eu` — Avv Grenzpruefung Brki Anbieter Brki Eu
- `avv-grenzpruefung-datenschutz` — Avv Grenzpruefung Datenschutz
- `berufsrecht-ki-vertragspruefung-kaltstart-interview` — Berufsrecht Ki Vertragspruefung Kaltstart Interview
- `berufsrechtliche-bnoto-interessen-brao` — Berufsrechtliche Bnoto Interessen Brao
- `brki-anbieter-due-diligence` — Brki Anbieter Due Diligence
- `brki-eu-us-dpf-transferpruefung` — Brki Eu Us Dpf Transferpruefung
- `brki-rag-bro-grundlagen-cloud-act` — Brki Rag Bro Grundlagen Cloud Act
- `brki-rag-vertraulichkeit-spezial` — Brki Rag Vertraulichkeit Spezial
- `brki-rollout-trainings-workflow` — Brki Rollout Trainings Workflow
- `bro-grundlagen-ki-einsatz` — Bro Grundlagen Ki Einsatz

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Berufsrecht Ki Vertragspruefung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: § 203 StGB, Consumer, § 43e BRAO, — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Anwalt/Kanzlei.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
