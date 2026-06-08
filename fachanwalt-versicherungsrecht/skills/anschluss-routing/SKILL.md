---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Versicherungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `cyber-loesegeld-versr-cyber-deckungsanfrage` — Cyber Loesegeld Versr Cyber Deckungsanfrage
- `deckungsklage-interessen-deckungspruefung-obliegenheiten` — Deckungsklage Interessen Deckungspruefung Obliegenheiten
- `do-deckungsabwehr-lebensversicherung-rueckkauf` — Do Deckungsabwehr Lebensversicherung Rueckkauf
- `erstgespraech-mandatsannahme-berufsunfaehigkeit-klage` — Erstgespraech Mandatsannahme Berufsunfaehigkeit Klage
- `fachanwalt-kanzlei-krankenversicherung` — Fachanwalt Kanzlei Krankenversicherung
- `klage-versicherer-triage-versicherungsrecht-schriftsatzkern` — Klage Versicherer Triage Versicherungsrecht Schriftsatzkern
- `lebens-leistungsablehnung-international-obliegenheitsverletzung` — Lebens Leistungsablehnung International Obliegenheitsverletzung
- `ombudsmann-gdv-orientierung-regress-abwehr` — Ombudsmann Gdv Orientierung Regress Abwehr
- `private-spezial-pruefen-rechtsschutz-beweislast` — Private Prüfen Rechtsschutz Beweislast
- `rentenversicherung-sachversicherung-schnittstelle` — Rentenversicherung Sachversicherung Schnittstelle
- `themen-fristennotiz-versr-rechtsschutz-versr` — Themen Fristennotiz Versr Rechtsschutz Versr
- `versicherungsrecht-vergleichsverhandlung-strategie-versr-bafin` — Versicherungsrecht Vergleichsverhandlung Strategie Versr Bafin
- `versr-bu-anerkennt-leistungspruefung-nachpruefung-anerkenntnis` — Versr Bu Anerkennt Leistungspruefung Nachpruefung Anerkenntnis

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Versicherungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Versicherungsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 28 VVG
- § 14 VVG
- § 19 VVG
- § 81 VVG
- § 215 VVG
- § 86 VVG
- § 1 VVG
- § 261 StGB
- § 43 GmbHG
- § 203 VVG
- § 21 VVG
- § 84 VVG

### Leitentscheidungen

- BGH IV ZR 32/24
- BGH IV ZR 70/25
- BGH IV ZR 86/24
- BGH IV ZR 153/20

