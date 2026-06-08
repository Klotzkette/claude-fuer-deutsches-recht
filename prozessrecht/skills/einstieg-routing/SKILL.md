---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Prozessrecht (ZPO/VwGO/StPO/SGG): ordnet Rolle (Mandant, Gegner, Gericht), markiert Frist (Berufung 1 Mon. § 517 ZPO), wählt Norm (ZPO, VwGO, StPO, SGG, FGO, FamFG) und Zuständigkeit (Erste Instanz / Rechtsmittelgerichte), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Prozessrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher ZPO Proz Bauleiter Eilverfahren
- `anspruchstabelle-beweislast` — Anspruchstabelle Beweislast
- `anspruchstabelle-gegenseite-interessen` — Anspruchstabelle Gegenseite Interessen
- `anwaltsgeheimnis-pruefung` — Anwaltsgeheimnis Pruefung
- `argumentationsverbesserung-red-team` — Argumentationsverbesserung RED Team
- `beweissicherung-einstweilige-verfuegung` — Beweissicherung Einstweilige Verfuegung
- `chronologie` — Chronologie
- `eilverfahren-risikoampel-und-gegenargumente` — Eilverfahren Risikoampel und Gegenargumente
- `einstweilige-verfuegung` — Einstweilige Verfuegung
- `gegenseite-mehrparteien-konflikt-und-interessen` — Gegenseite Mehrparteien Konflikt und Interessen
- `gegenseite-status-mahnbescheid-mahnschreiben` — Gegenseite Status Mahnbescheid Mahnschreiben
- `kaltstart-interview` — Kaltstart Interview
- `mahnbescheid` — Mahnbescheid
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Prozessrecht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Prozessrecht (ZPO/VwGO/StPO/SGG) typische Eskalationsstufen: Klage, Klageerwiderung, Beweisantrag.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
