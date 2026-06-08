---
name: einstieg-routing
description: "Einstieg, Triage und Routing für WEG/Hausverwaltung: ordnet Rolle (WEG-Eigentümer, Verwalter, Mehrheit/Minderheit), markiert Frist (§ 44 WEG Beschlussanfechtung 1 Mon.), wählt Norm (WEG §§ 18/19/20/23-28/44/45, HeizkostenV, BetrKV) und Zuständigkeit (Amtsgericht Belegenheit), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Weg Hausverwaltung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `abrechnung-ist-plan-mieterschnittstelle` — Abrechnung IST Plan Mieterschnittstelle
- `anwalt-amtsgericht-gewerbe-restaurant` — Anwalt Amtsgericht Gewerbe Restaurant
- `bad-umbau-barrierefreie-einladung-bauliche` — BAD Umbau Barrierefreie Einladung Bauliche
- `bad-umbau-bodengleiche-dusche-sondereigentum` — BAD Umbau Bodengleiche Dusche Sondereigentum
- `barrierefreie-einladung-protokoll-versammlung` — Barrierefreie Einladung Protokoll Versammlung
- `bauliche-veraenderung-aufzug-treppenlift-20` — Bauliche Veraenderung Aufzug Treppenlift 20
- `bauliche-veraenderungen-20-weg` — Bauliche Veraenderungen 20 WEG
- `bauliche-veraenderungen-beirat-controlling` — Bauliche Veraenderungen Beirat Controlling
- `beirat-controlling-verwalter` — Beirat Controlling Verwalter
- `beschlussanfechtung-risiko` — Beschlussanfechtung Risiko
- `beschlusssammlung-betriebskosten-interessen` — Beschlusssammlung Betriebskosten Interessen
- `beschlusssammlung-protokoll` — Beschlusssammlung Protokoll
- `beschlusssammlung-protokoll-beschlussvorlagen` — Beschlusssammlung Protokoll Beschlussvorlagen
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 24 Abs. 4 S. 2 WEG Ladung 3 Wochen, § 28 Abs. 2 WEG Jahresabrechnung 6 Monate nach Wirtschaftsjahr, § 45 WEG Beschlussanfechtung 1 Monat.
- Fachpfad wählen: zentrale Anker im WEG-Hausverwaltung sind WEG §§ 9a, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 44, 45, 46, 47, BGB §§ 535 ff., HOAI, BetrKV. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Verwalter, Eigentümergemeinschaft, Verwaltungsbeirat, AG der Belegenheit, Handwerker, Vorverwalter.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei WEG/Hausverwaltung typische Eskalationsstufen: Beschlussklage, Beschlussersetzungsklage, Verwalter-Memo.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
