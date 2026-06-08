---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Erbrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `berater-interessen-beweislast-darlegungslast` — Berater Interessen Beweislast Darlegungslast
- `erb-einfuehrung-erb-erstgespraech-erb-internationales` — Erb Einfuehrung Erb Erstgespraech Erb Internationales
- `erb-nachlassinventar-erb-pflichtteilsanspruch-erb` — Erb Nachlassinventar Erb Pflichtteilsanspruch Erb
- `erbengemeinschaft-blockade-erstgespraech-mandatsannahme` — Erbengemeinschaft Blockade Erstgespraech Mandatsannahme
- `erbfall-eu-mandat-triage-pflichtteil-auskunft` — Erbfall Eu Mandat Triage Pflichtteil Auskunft
- `erbfall-intake-erbrecht-erbschein` — Erbfall Intake Erbrecht Erbschein
- `erbschein-antrag-orientierung-pflichtteilsberechnung` — Erbschein Antrag Orientierung Pflichtteilsberechnung
- `fachanwalt-kanzlei-livecheck` — Fachanwalt Kanzlei Livecheck
- `krypto-wallet-erbschaftsteuer-steuerrecht` — Krypto Wallet Erbschaftsteuer Steuerrecht
- `pflichtteil-berechnen-schriftsatzkern-substantiierung-sonderfall` — Pflichtteil Berechnen Schriftsatzkern Substantiierung Sonderfall
- `pflichtteil-progressionsoptimierung-spezial-schnittstellen` — Pflichtteil Progressionsoptimierung Schnittstellen
- `pflichtteilsergaenzung-frist-fachanwalt-erbrecht` — Pflichtteilsergaenzung Frist Fachanwalt Erbrecht
- `pflichtteilsergaenzung-testamentsvollstreckung-mediation` — Pflichtteilsergaenzung Testamentsvollstreckung Mediation

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

