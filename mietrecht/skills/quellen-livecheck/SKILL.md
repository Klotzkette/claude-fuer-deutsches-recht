---
name: quellen-livecheck
description: "Quellen-Live-Check für Mietrecht (Wohnraum/Gewerbe): prüft Normen (BGB §§ 535/536/543/558/573 ff., WEG, BetrKV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht Belegenheit und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Mietrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


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

- Tragende Normen (BGB §§ 535, 536, 543, 558, 558a, 558b, 573, 573c, 574, 556, 556a, 556b, BetrKV, WEG §§ 24, 25, 27) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Mietrecht und WEG-Recht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
