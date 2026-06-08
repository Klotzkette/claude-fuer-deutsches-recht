---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Bank Kapitalmarktrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `fa-bank-kapitalmarkt-bk-bafin-chronologie` — Allgemein Bk Bafin Chronologie
- `anlageberatung-fehlerhaft-cybertrading-anlagebetrug` — Anlageberatung Fehlerhaft Cybertrading Anlagebetrug
- `anlageberatungsfehler-bankrecht-akkreditiv-buergschaft-erste` — Anlageberatungsfehler Bankrecht Akkreditiv Buergschaft Erste
- `bankaufsicht-erlaubnis-emissionsprospekt-mandantenentscheidung` — Bankaufsicht Erlaubnis Emissionsprospekt Mandantenentscheidung
- `bankrecht-buergschaft-aval-garantieabruf-eilrechtsschutz` — Bankrecht Buergschaft Aval Garantieabruf Eilrechtsschutz
- `bankrecht-privatbuergschaft-bankrecht-regress-bk-aufsicht` — Bankrecht Privatbuergschaft Bankrecht Regress Bk Aufsicht
- `beratungshaftung-haftung-beweislast-bk-cum` — Beratungshaftung Haftung Beweislast Bk Cum
- `bk-bankenfehlberatung-bk-einfuehrung-bk-mandantenrouting` — Bk Bankenfehlberatung Bk Einfuehrung Bk Mandantenrouting
- `bk-mifid-bk-prip-erstgespraech-mandatsannahme` — Bk Mifid Bk Prip Erstgespraech Mandatsannahme
- `fehlerhaft-fristennotiz-kapitalmarktrecht-bk-emissionsprospekt` — Fehlerhaft Fristennotiz Kapitalmarktrecht Bk Emissionsprospekt
- `gesellschaftsrecht-interessen-micar-mifid` — Gesellschaftsrecht Interessen Micar Mifid
- `kreditkuendigung-bgb-mica-stablecoin-ombudsmann-bafin` — Kreditkuendigung Bgb Mica Stablecoin Ombudsmann Bafin
- `mandat-triage-schriftsatzkern-substantiierung-bank` — Mandat Triage Schriftsatzkern Substantiierung Bank
- `orientierung-schufa-eintrag-schufa-loeschungsanspruch` — Orientierung Schufa Eintrag Schufa Loeschungsanspruch

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Bank Kapitalmarktrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Bank- und Kapitalmarktrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
