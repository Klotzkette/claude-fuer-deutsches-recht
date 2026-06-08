---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Geldwäscheprävention AML/KYC: ordnet Rolle (Verpflichteter (Bank, Anwalt, Notar), Kunde, FIU), markiert Frist (Verdachtsmeldung unverzüglich § 43 GwG), wählt Norm (GwG, FATF 40 Recommendations, EU-AMLD VI) und Zuständigkeit (FIU), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Geldwaeschepraevention Aml Kyc** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


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
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Geldwaeschepraevention Aml Kyc sind GwG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Geldwäscheprävention AML/KYC typische Eskalationsstufen: KYC-Dossier, SAR-Entwurf, Risikoklassifizierung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
