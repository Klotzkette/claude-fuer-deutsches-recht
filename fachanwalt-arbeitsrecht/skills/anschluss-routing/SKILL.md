---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Arbeitsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-ar-kuendigungspruefung-fazugang-arbeitgeber` — Allgemein Ar Kuendigungspruefung Fazugang Arbeitgeber
- `ar-aufhebungsvertrag-konkurrenzklausel-fachanwalt-arbeitsrecht` — Ar Aufhebungsvertrag Konkurrenzklausel Fachanwalt Arbeitsrecht
- `ar-betriebsuebergang-ar-einfuehrung-ar-leiharbeit` — Ar Betriebsuebergang Ar Einfuehrung Ar Leiharbeit
- `arbeitsgericht-abrechnung-vergleichsverhandlung-strategie-zugang` — Arbeitsgericht Abrechnung Vergleichsverhandlung Strategie Zugang
- `befristung-fao-unwirksam-fristennotiz` — Befristung Fao Unwirksam Fristennotiz
- `befristung-tzbfg-bem-verfahren-fazugang-kuendigungsfrist` — Befristung Tzbfg Bem Verfahren Fazugang Kuendigungsfrist
- `beteiligung-betriebsrat-erstgespraech-mandatsannahme-fachanwalt` — Beteiligung Betriebsrat Erstgespraech Mandatsannahme Fachanwalt
- `betriebsrat-betrvg-datum` — Betriebsrat Betrvg Datum
- `entgtranspg-fachanwalt-kschg` — Entgtranspg Fachanwalt Kschg
- `fachanwalt-arbeitsrecht-bag-betriebsratsanhoerung` — Fachanwalt Arbeitsrecht Bag Betriebsratsanhoerung
- `fachanwalt-arbeitsrecht-freistellungsklausel-sonderfall-ar` — Fachanwalt Arbeitsrecht Freistellungsklausel Sonderfall Ar
- `fachanwalt-arbeitsrecht-hinschg-kuendigungsschutzklage` — Fachanwalt Arbeitsrecht Hinschg Kuendigungsschutzklage
- `fazugang-arbeitnehmerverteidigung-fazugang-schriftform` — Fazugang Arbeitnehmerverteidigung Fazugang Schriftform
- `fazugang-einwurf-einschreiben-zugang-urlaub-inhalt-umschlags` — Fazugang Einwurf Einschreiben Zugang Urlaub Inhalt Umschlags

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Arbeitsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Arbeitsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 102 BetrVG
- § 17 KSchG
- § 4 KSchG
- § 14 TzBfG
- § 1 KSchG
- § 17 TzBfG
- § 15 AGG
- § 22 AGG
- § 5 KSchG
- § 66 ArbGG
- § 54 ArbGG
- § 23 KSchG

### Leitentscheidungen

- EuGH C-134/24
- EuGH C-518/20

