---
name: quellen-livecheck
description: "Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Kanzlei Builder Hub** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

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

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Kanzlei Builder Hub (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
