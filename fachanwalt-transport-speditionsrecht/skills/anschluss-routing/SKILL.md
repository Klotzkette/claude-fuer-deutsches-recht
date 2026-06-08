---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Transport Speditionsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `autonome-lkw-cmr-schadensregulierung-speditionshaftung-hgb` — Autonome Lkw Cmr Schadensregulierung Speditionshaftung Hgb
- `cmr-haftung-ladungsschaden-frachtfuehrerhaftung` — Cmr Haftung Ladungsschaden Frachtfuehrerhaftung
- `cotif-fachanwalt-haager` — Cotif Fachanwalt Haager
- `hgb-kabotage-beweislast-kanzlei-red` — Hgb Kabotage Beweislast Kanzlei Red
- `lieferverzug-orientierung-mandat-triage` — Lieferverzug Orientierung Mandat Triage
- `marktzugang-sonderfall-montrealer-spezial-pruefen` — Marktzugang Sonderfall Montrealer Prüfen
- `regeln-interessen-schnittstelle-spedition` — Regeln Interessen Schnittstelle Spedition
- `reklamationsschreiben-cmr-schriftsatzkern-substantiierung-adsp` — Reklamationsschreiben Cmr Schriftsatzkern Substantiierung Adsp
- `speditionsrecht-tio-schiedsgericht-frachtvertrag` — Speditionsrecht Tio Schiedsgericht Frachtvertrag
- `trans-cmr-frachtbrief-hgb-spedition-kabotage-marktzugang` — Trans Cmr Frachtbrief Hgb Spedition Kabotage Marktzugang
- `trans-multimodaler-transr-cmr-transr-multimodaler` — Trans Multimodaler Transr Cmr Transr Multimodaler
- `trans-transport-visby` — Trans Transport Visby
- `transr-einfuehrung-rechtsquellen` — Transr Einfuehrung Rechtsquellen

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Transport Speditionsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Transport- und Speditionsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 1d StVG
- § 1g StVG
- § 7 StVG
- § 1 ProdHaftG
- § 1h StVG
- § 1f StVG
- § 18 StVG
- § 12 StVG
- § 86 VVG
- § 3 ProdHaftG
- § 1 PflVG
- § 29 VwVfG
