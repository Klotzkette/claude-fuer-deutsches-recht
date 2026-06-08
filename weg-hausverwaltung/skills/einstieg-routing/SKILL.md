---
name: einstieg-routing
description: "Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Weg Hausverwaltung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abrechnung-ist-plan-mieterschnittstelle` — Abrechnung Ist Plan Mieterschnittstelle
- `anwalt-amtsgericht-gewerbe-restaurant-grossakte` — Anwalt Amtsgericht Gewerbe Restaurant Grossakte
- `bad-umbau-barrierefreie-einladung-bauliche-veraenderung` — Bad Umbau Barrierefreie Einladung Bauliche Veraenderung
- `bad-umbau-bodengleiche-dusche-sondereigentum-gemeinschaft` — Bad Umbau Bodengleiche Dusche Sondereigentum Gemeinschaft
- `barrierefreie-einladung-protokoll-versammlung` — Barrierefreie Einladung Protokoll Versammlung
- `bauliche-veraenderung-aufzug-treppenlift-20-abs-2-weg` — Bauliche Veraenderung Aufzug Treppenlift 20 Abs 2 Weg
- `bauliche-veraenderungen-20-weg` — Bauliche Veraenderungen 20 Weg
- `bauliche-veraenderungen-beirat-controlling-beschlussanfechtung` — Bauliche Veraenderungen Beirat Controlling Beschlussanfechtung
- `beirat-controlling-verwalter` — Beirat Controlling Verwalter
- `beschlussanfechtung-risiko` — Beschlussanfechtung Risiko
- `beschlusssammlung-betriebskosten-interessen` — Beschlusssammlung Betriebskosten Interessen
- `beschlusssammlung-protokoll` — Beschlusssammlung Protokoll
- `beschlusssammlung-protokoll-beschlussvorlagen-erstellen` — Beschlusssammlung Protokoll Beschlussvorlagen Erstellen
- `beschlussvorlagen-erstellen` — Beschlussvorlagen Erstellen

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
