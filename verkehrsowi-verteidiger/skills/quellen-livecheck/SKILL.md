---
name: quellen-livecheck
description: "Quellen-Live-Check für Verkehrs-OWi-Verteidigung: prüft Normen (OWiG, StVO, StVG, BKatV) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Bußgeldbehörde und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Verkehrsowi Verteidiger** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `abstand-quellenkarte` — Abstand Quellenkarte
- `akteneinsicht-internationaler-bezug-und-schnittstellen` — Akteneinsicht Internationaler Bezug und Schnittstellen
- `alkohol-compliance-dokumentation-und-akte` — Alkohol Compliance Dokumentation und Akte
- `alkohol-drogen-beweisverwertung` — Alkohol Drogen Beweisverwertung
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren` — Anhoerung Verkehrsowi Einspruch Messverfahren
- `bussgeldbescheid-tatbestand-beweis-und-belege` — Bussgeldbescheid Tatbestand Beweis und Belege
- `drogen-mehrparteien-konflikt-und-interessen` — Drogen Mehrparteien Konflikt und Interessen
- `einspruch-dokumentenmatrix-und-lueckenliste` — Einspruch Dokumentenmatrix und Lueckenliste
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `geschwindigkeit-verhandlung-vergleich-und-eskalation` — Geschwindigkeit Verhandlung Vergleich und Eskalation
- `handy-zahlen-schwellen-und-berechnung` — Handy Zahlen Schwellen und Berechnung
- `hauptverhandlung-sonderfall-messakte-messung` — Hauptverhandlung Sonderfall Messakte Messung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Verkehrsowi Verteidiger (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
