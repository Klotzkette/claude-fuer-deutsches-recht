---
name: einstieg-routing
description: "Einstieg, Triage und Routing für JVEG-Kostenprüfer: ordnet Rolle (Sachverständiger, Gericht, Bezirksrevisor), markiert Frist (Entschädigungsantrag binnen 3 Monaten), wählt Norm (JVEG, ZPO §§ 91 ff.) und Zuständigkeit (Gericht), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Jveg Kostenpruefer** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aktenstripper` — Aktenstripper
- `anspruchsberechtigung-antragsgenerator` — Anspruchsberechtigung Antragsgenerator
- `antragsgenerator` — Antragsgenerator
- `belegfeste-formular-portal-und-einreichung` — Belegfeste Formular Portal und Einreichung
- `beschwerde-dolmetscher-sonderfall` — Beschwerde Dolmetscher Sonderfall
- `dolmetscher-sonderfall-und-edge-case` — Dolmetscher Sonderfall und Edge Case
- `dolmetscher-uebersetzer` — Dolmetscher Übersetzer
- `dolmetscher-uebersetzer-fahrtkosten` — Dolmetscher Übersetzer Fahrtkosten
- `dolmetscherkosten-zahlen-schwellen-und-berechnung` — Dolmetscherkosten Zahlen Schwellen und Berechnung
- `fahrtkosten` — Fahrtkosten
- `fahrtkosten-festsetzung-interessen` — Fahrtkosten Festsetzung Interessen
- `festsetzung-beschwerde` — Festsetzung Beschwerde
- `festsetzung-mehrparteien-konflikt-und-interessen` — Festsetzung Mehrparteien Konflikt und Interessen
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Jveg Kostenpruefer sind JVEG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
