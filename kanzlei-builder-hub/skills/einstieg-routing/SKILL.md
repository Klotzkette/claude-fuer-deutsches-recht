---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Kanzlei-Builder-Hub (Plugins/Skills): ordnet Rolle (Kanzleiinhaber, IT-Verantwortlicher, Mitarbeitende), markiert Frist (keine harten Fristen), wählt Norm (BRAO § 43e KI-Einsatz, DSGVO, KI-VO) und Zuständigkeit (RAK), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Kanzlei Builder Hub** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `anschluss-router` — Anschluss Router
- `automatischer-aktualisierer` — Automatischer Aktualisierer
- `builder-zahlen-schwellen-und-berechnung` — Builder Zahlen Schwellen und Berechnung
- `community-leistungsmatrix-fristennotiz` — Community Leistungsmatrix Fristennotiz
- `daten-red-team-und-qualitaetskontrolle` — Daten RED Team und Qualitaetskontrolle
- `deaktivieren` — Deaktivieren
- `deinstallieren` — Deinstallieren
- `deployment-eigenen-einsteiger` — Deployment Eigenen Einsteiger
- `eigenen-formular-portal-und-einreichung` — Eigenen Formular Portal und Einreichung
- `einsteiger-mandantenkommunikation-entscheidungsvorlage` — Einsteiger Mandantenkommunikation Entscheidungsvorlage
- `findet-gate-installiert` — Findet Gate Installiert
- `fristen-risikoampel-mandantenkommunikation` — Fristen Risikoampel Mandantenkommunikation
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Kanzlei Builder Hub sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Kanzlei-Builder-Hub (Plugins/Skills) typische Eskalationsstufen: Plugin-Skizze, Skill-Entwurf, Validierungsbericht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
