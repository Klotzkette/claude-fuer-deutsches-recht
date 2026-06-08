---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Strafzumessung: ordnet Rolle (Angeklagter, Verteidiger, Staatsanwaltschaft), markiert Frist (Revision 1 Woche/1 Monat § 341 StPO), wählt Norm (§ 46 StGB, §§ 47-50 StGB Strafmilderung/-schärfung, BGH-Strafzumessungsleitlinien) und Zuständigkeit (Strafgericht (Amts-/Landgericht)), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Strafzumessung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `153a-stpo-iii-bewaehrung-stgb` — 153a STPO III Bewaehrung STGB
- `besonders-formular-portal-und-einreichung` — Besonders Formular Portal und Einreichung
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung 56 STGB Positive Sozialprognose
- `bewaehrung-auflagen-bewaehrungswiderruf-56f` — Bewaehrung Auflagen Bewaehrungswiderruf 56F
- `bewaehrung-interessen-deutschem` — Bewaehrung Interessen Deutschem
- `bewaehrungswiderruf-56f-stgb` — Bewaehrungswiderruf 56F STGB
- `deutschem-tatbestand-beweis-und-belege` — Deutschem Tatbestand Beweis und Belege
- `freiheitsstrafe-compliance-dokumentation-und-akte` — Freiheitsstrafe Compliance Dokumentation und Akte
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Freiheitsstrafe Ohne Bewaehrung Vollstreckung
- `freiheitsstrafe-strafmass-geldstrafe` — Freiheitsstrafe Strafmass Geldstrafe
- `geldstrafe-grossen-rechtsmittel` — Geldstrafe Grossen Rechtsmittel
- `geldstrafe-tagessatzanzahl-bestimmen` — Geldstrafe Tagessatzanzahl Bestimmen
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Geldstrafe VS Freiheitsstrafe 47 STGB
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 56 StGB Bewährungszeit 2–5 Jahre, § 57 StGB 2/3-Reststrafenaussetzung, § 57a StGB lebenslange Freiheitsstrafe nach 15 Jahren.
- Fachpfad wählen: zentrale Anker im Strafzumessung sind StGB §§ 46, 46a, 46b, 47, 49, 56, 57, 57a, 64, JGG §§ 17, 18, 21, BtMG § 31. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Tatrichter, Verteidiger, Staatsanwaltschaft, Bewährungshelfer, Vollstreckungsbehörde.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Strafzumessung typische Eskalationsstufen: Strafzumessungs-Memo, Plädoyer, Revisionsbegründung Strafzumessung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
