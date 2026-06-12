---
name: anschluss-routing
description: "Anschluss-Routing für Phishing-Vorfall-Prüfer: wählt den nächsten Spezial-Skill nach Engpass (Art. 33 DSGVO 72h, Vorfallsbericht, Logs, Bank-Korrespondenz), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Phishing Vorfall Prüfer** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `675u-675w-banking` — 675u 675w Banking
- `675v-quellenkarte` — 675v Quellenkarte
- `675w-zahlen-schwellen-und-berechnung` — 675w Zahlen Schwellen und Berechnung
- `arbeitnehmer-haftung-bgb-675u-phish-ceo` — Arbeitnehmer Haftung BGB 675u Phish CEO
- `aufsicht-bafin-bank-strategie-banking-app` — Aufsicht Bafin Bank Strategie Banking APP
- `banking-behoerden-gericht-und-registerweg` — Banking Behoerden Gericht und Registerweg
- `bankpflichten-beweislast-bgb` — Bankpflichten Beweislast BGB
- `bea-notfall-bgb-675v-erstkontakt-mandant` — BEA Notfall BGB 675v Erstkontakt Mandant
- `beweislast-mandantenkommunikation-entscheidungsvorlage` — Beweislast Mandantenkommunikation Entscheidungsvorlage
- `bgb-schriftsatz-brief-und-memo-bausteine` — BGB Schriftsatz Brief und Memo Bausteine
- `call-interessen-faelle-freistehender` — Call Interessen Faelle Freistehender
- `faelle-abschlussprodukt-und-uebergabe` — Faelle Abschlussprodukt und Übergabe
- `fahrlaessigkeit-fehlerkatalog` — Fahrlaessigkeit Fehlerkatalog
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Phishing Vorfall Prüfer-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 263a StGB
- Art. 33 DSGVO
- § 1 ZAG
- § 31 VVG
- § 55 ZAG
- Art. 34 DSGVO
- § 4 FinDAG
- § 27 ZAG
- § 269 StGB
- § 29 VwVfG
- Art. 15 DSGVO
- § 32 BSIG

### Leitentscheidungen

- BGH XI ZR 91/14
