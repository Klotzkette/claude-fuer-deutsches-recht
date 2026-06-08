---
name: anschluss-routing
description: "Anschluss-Routing für Geldwäscheprävention AML/KYC: wählt den nächsten Spezial-Skill nach Engpass (Verdachtsmeldung unverzüglich § 43 GwG, KYC-Akte, Risk Assessment, Compliance-Manual), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Geldwaeschepraevention Aml Kyc** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `aml-kryptotransaktionen-mica-spezial` — AML Kryptotransaktionen Mica Spezial
- `aml-kyc-start-chronologie-fristen` — AML KYC Start Chronologie Fristen
- `aml-trade-based-money-laundering-spezial` — AML Trade Based Money Laundering Spezial
- `aml-verdachtsmeldung-fiu-leitfaden` — AML Verdachtsmeldung FIU Leitfaden
- `awareness-zahlen-schwellen-und-berechnung` — Awareness Zahlen Schwellen und Berechnung
- `behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` — Behoerdenverfahren Schriftsatz Brief und Memo Bausteine
- `geldwaesche-audit-internal-datenqualitaet` — Geldwaesche Audit Internal Datenqualitaet
- `geldwaesche-behoerdenverfahren` — Geldwaesche Behoerdenverfahren
- `geldwaesche-bussgeld-reputation` — Geldwaesche Bussgeld Reputation
- `geldwaesche-datenqualitaet-register` — Geldwaesche Datenqualitaet Register
- `geldwaesche-gruppenweite-compliance` — Geldwaesche Gruppenweite Compliance
- `geldwaesche-immobilien-gueterhaendler` — Geldwaesche Immobilien Gueterhaendler
- `geldwaesche-krypto-zahlungsdienstleister` — Geldwaesche Krypto Zahlungsdienstleister
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Geldwaeschepraevention Aml Kyc-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Geldwäscheprävention AML/KYC.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
