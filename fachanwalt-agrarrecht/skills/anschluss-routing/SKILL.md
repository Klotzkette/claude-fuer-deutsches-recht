---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Agrarrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `agrar-einfuehrung-rechtsquellen` — Agrar Einfuehrung Rechtsquellen
- `agrar-jagdpacht-streit-mandantenfragen-typisch-paechterbetrieb` — Agrar Jagdpacht Streit Mandantenfragen Typisch Paechterbetrieb
- `agrar-tierhaltung-erstgespraech-mandatsannahme-duenge` — Agrar Tierhaltung Erstgespraech Mandatsannahme Duenge
- `agrar-wolfsschaden-cross-glozez-foerderung-gap` — Agrar Wolfsschaden Cross Glozez Förderung Gap
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anerbenrecht-bgb-spezial-compliance` — Anerbenrecht Bgb Compliance
- `cross-duengeverordnung-interessen-erbrecht-beweislast` — Cross Duengeverordnung Interessen Erbrecht Beweislast
- `eu-agrarfoerderung-gap-direktzahlungen-hoefe` — Eu Agrarfoerderung Gap Direktzahlungen Hoefe
- `fachanwalt-agrarrecht-landpacht-hoferbfolge-triage` — Fachanwalt Agrarrecht Landpacht Hoferbfolge Triage
- `fachanwalt-forstrecht-red-hoefe-sonderfall` — Fachanwalt Forstrecht Red Hoefe Sonderfall
- `fristennotiz-naechster-pachtvertrag-streitig-pachtvertrag` — Fristennotiz Naechster Pachtvertrag Streitig Pachtvertrag
- `hoefeo-laender-landpachtrecht` — Hoefeo Länder Landpachtrecht
- `orientierung-tierhaltung-genehmigung-landpacht-schlichtung` — Orientierung Tierhaltung Genehmigung Landpacht Schlichtung
- `pflanzenschutz-schnittstelle-mandantenentscheidung-tierschutz` — Pflanzenschutz Schnittstelle Mandantenentscheidung Tierschutz

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Agrarrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Agrarrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
