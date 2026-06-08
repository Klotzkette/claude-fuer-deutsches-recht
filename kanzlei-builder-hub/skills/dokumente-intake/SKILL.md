---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Kanzlei Builder Hub** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `community-leistungsmatrix-fristennotiz-automatischer` — Community Leistungsmatrix Fristennotiz Automatischer
- `deployment-eigenen-einsteiger` — Deployment Eigenen Einsteiger
- `findet-gate-installiert` — Findet Gate Installiert
- `fundstellenglattzieher` — Fundstellenglattzieher
- `grosskanzlei-rollout-thema-prozesse-abbilden` — Grosskanzlei Rollout Thema Prozesse Abbilden
- `kanzlei-builder-hub-kaltstart-interview` — Kanzlei Builder Hub Kaltstart Interview
- `kanzleiumgebung-khub-sonderfall-livecheck-interessen` — Kanzleiumgebung Khub Sonderfall Livecheck Interessen
- `khub-kanzlei-coi-onboarding-bauleiter-leistungsmatrix-mandanten` — Khub Kanzlei Coi Onboarding Bauleiter Leistungsmatrix Mandanten
- `khub-mandantenkonferenz-paralegal-rollen-rentier-rechtsanwalt` — Khub Mandantenkonferenz Paralegal Rollen Rentier Rechtsanwalt
- `playbook-aus-eigenen-daten` — Playbook Aus Eigenen Daten
- `playbook-qualitaetspruefung-beweislast-review` — Playbook Qualitaetspruefung Beweislast Review
- `qa-kanzleiweit-templating-praxis-verwalter` — Qa Kanzleiweit Templating Praxis Verwalter
- `qualitaetspruefung-builder-daten-red` — Qualitaetspruefung Builder Daten Red

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Kanzlei Builder Hub-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Kanzleiinhaber.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
