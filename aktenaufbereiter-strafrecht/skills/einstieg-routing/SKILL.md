---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Strafrechtliche Aktenaufbereitung: ordnet Rolle (Mandant/Beschuldigter, Staatsanwaltschaft, Verletzte/Zeugen), markiert Frist (Anklage-Erwiderungsfrist), wählt Norm (§§ 147 StPO Akteneinsicht, § 200 StPO Anklageschrift, § 397a StPO Nebenklage) und Zuständigkeit (Staatsanwaltschaft), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Aktenaufbereiter Strafrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `aktenaufbereiter-erstpruefung-und-mandatsziel` — Aktenaufbereiter Erstpruefung und Mandatsziel
- `aktenaufbereiter-strafrecht` — Aktenaufbereiter Strafrecht
- `akteneinsicht-uebersicht-aktenvorblatt` — Akteneinsicht Uebersicht Aktenvorblatt
- `aktenlektuere-fristennotiz-und-naechster-schritt` — Aktenlektuere Fristennotiz und Naechster Schritt
- `aktenvorblatt-erstellen` — Aktenvorblatt Erstellen
- `aktenvorblatt-schriftsatz-brief-und-memo-bausteine` — Aktenvorblatt Schriftsatz Brief und Memo Bausteine
- `anklageschrift-zerlegen` — Anklageschrift Zerlegen
- `aussageanalyse-aussagepsychologie` — Aussageanalyse Aussagepsychologie
- `beweismittel-katalog-beweisverwertungsverbote` — Beweismittel Katalog Beweisverwertungsverbote
- `beweisverwertungsverbote-pruefen` — Beweisverwertungsverbote Pruefen
- `beziehungen-spezial-chronologie-ergaenzbar` — Beziehungen Spezial Chronologie Ergaenzbar
- `beziehungsmatrix-personen-taten` — Beziehungsmatrix Personen Taten
- `chronologie-compliance-dokumentation-und-akte` — Chronologie Compliance Dokumentation und Akte
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Aktenaufbereiter Strafrecht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Strafrechtliche Aktenaufbereitung typische Eskalationsstufen: Verteidigungsschrift, Beweisantrag, Plädoyer-Notiz.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
