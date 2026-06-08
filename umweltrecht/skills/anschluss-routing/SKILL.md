---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Umweltrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abfall-anlagen-bimschg` — Abfall Anlagen Bimschg
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `boden-csddd-csrd-sonderfall` — Boden Csddd Csrd Sonderfall
- `diligence-greenwashing-beweislast-klimaklagen-interessen` — Diligence Greenwashing Beweislast Klimaklagen Interessen
- `esg-greenwashing-klimaklagen-verbandsklage-lksg-csddd` — Esg Greenwashing Klimaklagen Verbandsklage Lksg Csddd
- `lieferkettensorgfalt-lksg-red-naturschutz` — Lieferkettensorgfalt Lksg Red Naturschutz
- `stoerfall-anlagen-transaktionen-dd-umweltinformation-uig` — Stoerfall Anlagen Transaktionen Dd Umweltinformation Uig
- `tehg-verfahren-umweltrecht-verfahren` — Tehg Verfahren Umweltrecht Verfahren
- `umwelt-umweltrecht-umwrg` — Umwelt Umweltrecht Umwrg
- `umweltrecht-bussgeld-emissionshandel-tehg-uwr-ets` — Umweltrecht Bussgeld Emissionshandel Tehg Uwr Ets
- `umweltrecht-immissionsschutz-bimschg-naturschutz-artenschutz` — Umweltrecht Immissionsschutz Bimschg Naturschutz Artenschutz
- `uwr-bundesnaturschutzgesetz-uwr-co2-uwr-immissionsschutz` — Uwr Bundesnaturschutzgesetz Uwr Co2 Uwr Immissionsschutz
- `uwr-einfuehrung-rechtsquellen` — Uwr Einfuehrung Rechtsquellen
- `uwr-wasserrechtliche` — Uwr Wasserrechtliche

## Arbeitsweg

- Ergebnis sichten: Welche Umweltrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Umweltrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 BImSchG
- § 70 VwG
- § 10 BImSchG
- § 2 UmwRG
- § 24 BBodSchG
- § 74 VwG
- § 4 BBodSchG
- § 34 BNatSchG
- § 17 BImSchG
- § 47 VwG
- § 44 BNatSchG
- § 4 KrWG

### Leitentscheidungen

- EuGH C-243/15
- BGH I ZR 98/23
- BGH I ZR 142/23

