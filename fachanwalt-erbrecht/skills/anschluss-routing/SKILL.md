---
name: anschluss-routing
description: "Anschluss-Routing für Fachanwalt Erbrecht: wählt den nächsten Spezial-Skill nach Engpass (Ausschlagung 6 Wochen § 1944 BGB, Testament/Erbvertrag, Erbschein-Antrag, Nachlassverzeichnis), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Erbrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `berater-interessen-beweislast-darlegungslast` — Berater Interessen Beweislast Darlegungslast
- `bgb` — BGB
- `digitaler-nachlass-facebook-bgh-iii-zr-183-17` — Digitaler Nachlass Facebook BGH III ZR 183 17
- `ehegattentestament-bindungswirkung` — Ehegattentestament Bindungswirkung
- `erb-einfuehrung-erbfolge-erstgespraech` — ERB Einfuehrung Erbfolge Erstgespraech
- `erb-nachlassinventar-pflichtteilsanspruch` — ERB Nachlassinventar Pflichtteilsanspruch
- `erbengemeinschaft-blockade-erstgespraech` — Erbengemeinschaft Blockade Erstgespraech
- `erbfall-eu-mandat-triage-pflichtteil-auskunft` — Erbfall EU Mandat Triage Pflichtteil Auskunft
- `erbfall-intake-erbrecht-erbschein` — Erbfall Intake Erbrecht Erbschein
- `erbrecht-pflichtteilsergaenzung-schenkung` — Erbrecht Pflichtteilsergaenzung Schenkung
- `erbschein-antrag-orientierung` — Erbschein Antrag Orientierung
- `erbschein-einziehung-paragraf-2361-bgb-olg-muenchen-31-wx-275-19` — Erbschein Einziehung Paragraf 2361 BGB OLG Muenchen 31 WX 275 19
- `erbverzicht-pflichtteilsverzicht` — Erbverzicht Pflichtteilsverzicht
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Erbrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Erbrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 363 FamFG
- § 16 ErbStG
- Art. 14 GG
- § 23 EStG
- § 12 ErbStG
- § 30 ErbStG
- § 31 ErbStG
- § 343 FamFG
- § 13 ErbStG
- § 11 ErbStG
- § 12 BewG
- § 29 VwVfG

### Leitentscheidungen

- BGH III ZR 183/17
- BGH IV ZR 249/15
- BGH IV ZR 474/15

