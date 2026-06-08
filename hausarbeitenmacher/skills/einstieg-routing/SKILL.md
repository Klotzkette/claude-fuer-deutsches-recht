---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Jura-Hausarbeiten: ordnet Rolle (Studierender, Korrektor), markiert Frist (Hausarbeits-Abgabefrist), wählt Norm (BGB AT/BT, StGB AT/BT, GG, ZPO/StPO/VwGO) und Zuständigkeit (Universitäre Prüfungsämter), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Hausarbeitenmacher** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `adressaten-formular-portal-und-einreichung` — Adressaten Formular Portal und Einreichung
- `aufgabenstellung-erfassen-fachgebiet` — Aufgabenstellung Erfassen Fachgebiet
- `ausfluegen-didaktisches-durch` — Ausfluegen Didaktisches Durch
- `bearbeitungsplan-erstellen` — Bearbeitungsplan Erstellen
- `behutsame-frech-haeufige-fehler` — Behutsame Frech Haeufige Fehler
- `didaktisches-erstpruefung-und-mandatsziel` — Didaktisches Erstpruefung und Mandatsziel
- `durch-schriftsatz-brief-und-memo-bausteine` — Durch Schriftsatz Brief und Memo Bausteine
- `europarecht-anwendbarkeit-hausarbeiten` — Europarecht Anwendbarkeit Hausarbeiten
- `europarecht-interessen-fertigen-sonderfall` — Europarecht Interessen Fertigen Sonderfall
- `fachgebiet-routing-zivil-oeffentlich-straf` — Fachgebiet Routing Zivil Oeffentlich Straf
- `fertigen-sonderfall-und-edge-case` — Fertigen Sonderfall und Edge Case
- `fuehrt-risikoampel-und-gegenargumente` — Fuehrt Risikoampel und Gegenargumente
- `gliederung-mit-tiefenstruktur` — Gliederung mit Tiefenstruktur
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Hausarbeitenmacher sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Jura-Hausarbeiten typische Eskalationsstufen: Gutachten im Gutachtenstil, Literaturverzeichnis, Gliederung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
