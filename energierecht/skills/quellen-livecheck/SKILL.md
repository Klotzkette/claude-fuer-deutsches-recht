---
name: quellen-livecheck
description: "Quellen-Live-Check für Energierecht (EnWG, EEG): prüft Normen (EnWG, EEG, KWKG) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt BNetzA und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Energierecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


## Fachlandkarte dieses Plugins

- `anfrage-mehrparteien-konflikt-und-interessen` — Anfrage Mehrparteien Konflikt und Interessen
- `anschluss` — Anschluss
- `bess-abfall-recycling-rueckbau` — Bess Abfall Recycling Rueckbau
- `bess-abstandsflaechen-baurecht-brandenburg` — Bess Abstandsflaechen Baurecht Brandenburg
- `bess-baurecht-brandenburg` — Bess Baurecht Brandenburg
- `bess-behoerdenstrategie` — Bess Behoerdenstrategie
- `bess-bimschg-und-4-bimschv` — Bess Bimschg und 4 Bimschv
- `bess-brandschutz-co-location-datenschutz` — Bess Brandschutz CO Location Datenschutz
- `bess-co-location-pv-wind` — Bess CO Location PV Wind
- `bess-datenschutz-video-leitwarte` — Bess Datenschutz Video Leitwarte
- `bess-dieselgenerator-notstrom` — Bess Dieselgenerator Notstrom
- `bess-epc-fca-agnes-finanzierung` — Bess EPC FCA Agnes Finanzierung
- `bess-fca-agnes-bnetza` — Bess FCA Agnes BNETZA
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Tragende Normen (EEG, KWKG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Energierecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
