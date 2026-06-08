---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Verkehrsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-verk-unfallregulierung-workflow-chronologie` — Allgemein Verk Unfallregulierung Chronologie
- `autonom-bezuege-fachanwalt` — Autonom Bezuege Fachanwalt
- `bussgeld-unfall-haftungsquote-vkr-totalschaden` — Bussgeld Unfall Haftungsquote Vkr Totalschaden
- `erstgespraech-mandatsannahme-verkehr-autonom-fahrerlaubnis` — Erstgespraech Mandatsannahme Verkehr Autonom Fahrerlaubnis
- `fahrerlaubnis-kanzlei-personen` — Fahrerlaubnis Kanzlei Personen
- `mandat-triage-schriftsatzkern-substantiierung-315c` — Mandat Triage Schriftsatzkern Substantiierung 315c
- `mpu-vorbereitung-orientierung-regulierungsanforderung` — Mpu Vorbereitung Orientierung Regulierungsanforderung
- `pflvg-quoten-sonderfall-stgb` — Pflvg Quoten Sonderfall Stgb
- `stvg-verkehr-fristennotiz-vkr-blitzer` — Stvg Verkehr Fristennotiz Vkr Blitzer
- `stvo-unfallregulierung-beweislast-verkehrsrecht` — Stvo Unfallregulierung Beweislast Verkehrsrecht
- `tempo-messung-unfallregulierung-quoten-versicherer` — Tempo Messung Unfallregulierung Quoten Versicherer
- `verk-fahrerlaubnisrecht-leitfaden-fahrtenbuch-anordnung` — Verk Fahrerlaubnisrecht Leitfaden Fahrtenbuch Anordnung
- `verkehrsstrafrecht-interessen-verkehrsunfall` — Verkehrsstrafrecht Interessen Verkehrsunfall
- `vkr-bussgeldverfahren-bussgeld-einspruch-bussgeldbescheid` — Vkr Bussgeldverfahren Bussgeld Einspruch Bussgeldbescheid

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Verkehrsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Verkehrsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 67 OWiG
- § 69a StGB
- § 7 StVG
- § 18 StVG
- § 115 VVG
- § 69 StGB
- § 4 StVG
- § 33 OWiG
- § 24a StVG
- § 17 StVG
- § 55 OWiG
- § 26 StVG

### Leitentscheidungen

- BGH VI ZR 12/24
- BGH VI ZR 280/22
- BGH VI ZR 253/22
- BGH VI ZR 239/22
- BGH VI ZR 24/25

