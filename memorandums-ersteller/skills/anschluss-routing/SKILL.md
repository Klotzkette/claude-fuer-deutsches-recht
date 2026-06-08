---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Memorandums Ersteller** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `antworten-interessen-ausfuehrungen-fragen` — Antworten Interessen Ausfuehrungen Fragen
- `due-diligence-ergebnis-handlungsempfehlung-mandant-vs` — Due Diligence Ergebnis Handlungsempfehlung Mandant Vs
- `gliederung-mandantenunterlagen-memorandum` — Gliederung Mandantenunterlagen Memorandum
- `haftungsrisiko-rechtsanwalt-board-pack-vorfall-intern` — Haftungsrisiko Rechtsanwalt Board Pack Vorfall Intern
- `juristisches-questions-fristennotiz-vertragsentscheidung` — Juristisches Questions Fristennotiz Vertragsentscheidung
- `laenge-formate-mandantenfreundliche-fassung-typenuebersicht` — Laenge Formate Mandantenfreundliche Fassung Typenuebersicht
- `mandantenanfrage-schnell-rechtsmittelentscheidung-memorandums` — Mandantenanfrage Schnell Rechtsmittelentscheidung Memorandums
- `optional-beweislast-piercing-sonderfall-rechtliche` — Optional Beweislast Piercing Sonderfall Rechtliche
- `prozessstrategie-klageerhebung-gutachtenstil-quellen-zitierregel` — Prozessstrategie Klageerhebung Gutachtenstil Quellen Zitierregel
- `rechtsfortbildung-bgh-rechtsfragen-formulieren-research-tracking` — Rechtsfortbildung Bgh Rechtsfragen Formulieren Research Tracking
- `rechtsgebietsneutral-sachverhalt-satz` — Rechtsgebietsneutral Sachverhalt Satz
- `sachverhalt-fixieren-vier-teile-grenzueberschreitenden-faellen` — Sachverhalt Fixieren Vier Teile Grenzueberschreitenden Faellen
- `teile-vier-wandelt` — Teile Vier Wandelt

## Arbeitsweg

- Ergebnis sichten: Welche Memorandums Ersteller-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Memorandum-Ersteller.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 203 StGB
- § 31 VVG
- § 29 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

