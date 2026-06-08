---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Einfache Leichte Sprache Jura** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `leichte-sprache-jura-ls-bescheid-chronologie` — Allgemein Ls Bescheid Chronologie
- `einfache-elsj-bescheidmodus-elsj` — Einfache Elsj Bescheidmodus Elsj
- `elsj-aufenthaltsrecht-mandant` — Elsj Aufenthaltsrecht Mandant
- `elsj-aufenthaltsrecht-mandant-betreuung-vormundschaft-einfache` — Elsj Aufenthaltsrecht Mandant Betreuung Vormundschaft Einfache
- `elsj-bescheidmodus` — Elsj Bescheidmodus
- `elsj-betreuung-vormundschaft` — Elsj Betreuung Vormundschaft
- `elsj-einfache-sprache` — Elsj Einfache Sprache
- `elsj-familienrecht-erstgespraech` — Elsj Familienrecht Erstgespraech
- `elsj-familienrecht-erstgespraech-juristische-sicherung` — Elsj Familienrecht Erstgespraech Juristische Sicherung
- `elsj-juristische-sicherung` — Elsj Juristische Sicherung
- `elsj-kommandocenter` — Elsj Kommandocenter
- `elsj-kommunikation-mandant` — Elsj Kommunikation Mandant
- `elsj-leichte-sprache` — Elsj Leichte Sprache
- `elsj-leichte-sprache-mietrecht-kuendigungserklaerung` — Elsj Leichte Sprache Mietrecht Kuendigungserklaerung

## Arbeitsweg

- Ergebnis sichten: Welche Einfache Leichte Sprache Jura-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?


## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21
## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Einfache/Leichte Sprache Jura.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
