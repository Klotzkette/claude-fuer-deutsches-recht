---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Mietrecht (Wohnraum/Gewerbe): ordnet Rolle (Mieter, Vermieter, Hausverwaltung), markiert Frist (§ 573c BGB Kündigung 3 Mon.), wählt Norm (BGB §§ 535/536/543/558/573 ff., WEG, BetrKV) und Zuständigkeit (Amtsgericht Belegenheit), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Mietrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `amtlichen-amtsgericht-sonderfall` — Amtlichen Amtsgericht Sonderfall
- `amtsgericht-sonderfall-und-edge-case` — Amtsgericht Sonderfall und Edge Case
- `ausschliesslich-dokumentenmatrix-und-lueckenliste` — Ausschliesslich Dokumentenmatrix und Lueckenliste
- `betriebskostenabrechnung-belege-und-formelpruefer` — Betriebskostenabrechnung Belege und Formelpruefer
- `bundesland-datenerhebung-grossstadt` — Bundesland Datenerhebung Grossstadt
- `datenerhebung-zahlen-schwellen-und-berechnung` — Datenerhebung Zahlen Schwellen und Berechnung
- `eigenbedarfskuendigung-erstellen` — Eigenbedarfskuendigung Erstellen
- `erstellung-fehlerkatalog` — Erstellung Fehlerkatalog
- `grossstadt-mietspiegel-und-kappung` — Grossstadt Mietspiegel und Kappung
- `klageentwurf-amtsgericht-miet-gewerbemiete` — Klageentwurf Amtsgericht Miet Gewerbemiete
- `klageentwurf-beweislast-und-darlegungslast` — Klageentwurf Beweislast und Darlegungslast
- `lage-ausstattung-mahnung-zahlungsverzug` — Lage Ausstattung Mahnung Zahlungsverzug
- `mahnung-zahlungsverzug-mieter` — Mahnung Zahlungsverzug Mieter
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 573c BGB Kündigung 3 Monate, § 558b BGB Zustimmung Mieterhöhung Ende 2. Folgemonat, § 24 Abs. 4 WEG Ladung 3 Wochen, § 556 BGB Nebenkostenabrechnung 12 Monate.
- Fachpfad wählen: zentrale Anker im Mietrecht und WEG-Recht sind BGB §§ 535, 536, 543, 558, 558a, 558b, 573, 573c, 574, 556, 556a, 556b, BetrKV, WEG §§ 24, 25, 27. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Vermieter, Mieter, Hausverwaltung, WEG-Verwaltung, Amtsgericht der Belegenheit, Mieterverein, Eigentümergemeinschaft.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Mietrecht (Wohnraum/Gewerbe) typische Eskalationsstufen: Kündigungsschreiben, Mietminderungserklärung, Klage AG.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
