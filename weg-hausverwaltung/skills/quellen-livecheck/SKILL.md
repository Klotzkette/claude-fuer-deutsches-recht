---
name: quellen-livecheck
description: "Quellen-Live-Check für WEG/Hausverwaltung: prüft Normen (WEG §§ 18/19/20/23-28/44/45, HeizkostenV, BetrKV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht Belegenheit und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Weg Hausverwaltung** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


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
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (WEG §§ 9a, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 44, 45, 46, 47, BGB §§ 535 ff., HOAI, BetrKV) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im WEG-Hausverwaltung (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
