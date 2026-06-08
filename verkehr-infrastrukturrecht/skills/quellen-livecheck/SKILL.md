---
name: quellen-livecheck
description: "Quellen-Live-Check für Verkehr-Infrastrukturrecht: prüft Normen (FStrG, AEG, PBefG, BFStrG, VwVfG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Eisenbahn-BBundesamt und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Verkehr Infrastrukturrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anschluss-router` — Anschluss Router
- `autonomous-driving` — Autonomous Driving
- `autonomous-driving-interessen-grossprojekt` — Autonomous Driving Interessen Grossprojekt
- `autonomous-driving-strassenrecht` — Autonomous Driving Strassenrecht
- `buergerentscheid-strassenbahn-spezial` — Buergerentscheid Strassenbahn Spezial
- `driving-mehrparteien-konflikt-und-interessen` — Driving Mehrparteien Konflikt und Interessen
- `foerderung-vergabe-ladeinfrastruktur` — Foerderung Vergabe Ladeinfrastruktur
- `grossprojekt-zahlen-schwellen-und-berechnung` — Grossprojekt Zahlen Schwellen und Berechnung
- `infrastruktur-foerderung-nachhaltige` — Infrastruktur Foerderung Nachhaltige
- `infrastrukturrecht-intake-ladeinfrastruktur` — Infrastrukturrecht Intake Ladeinfrastruktur
- `intake-mandantenkommunikation-entscheidungsvorlage` — Intake Mandantenkommunikation Entscheidungsvorlage
- `ladeinfrastruktur` — Ladeinfrastruktur
- `ladeinfrastruktur-behoerden-gericht-und-registerweg` — Ladeinfrastruktur Behoerden Gericht und Registerweg
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Verkehr Infrastrukturrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
