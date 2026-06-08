---
name: quellen-livecheck
description: "Quellen-Live-Check für Geldwäscheprävention AML/KYC: prüft Normen (GwG, FATF 40 Recommendations, EU-AMLD VI) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt FIU und Quellenhygiene nach references/quellenhygiene.md."
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Geldwaeschepraevention Aml Kyc** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.


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

- Tragende Normen (GwG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Geldwaeschepraevention Aml Kyc (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Output

Quellenkarte mit Primärnormen, Rechtsprechungssuche (Gericht/Datum/Az/Rn), Behördenstand und Zitierform nach `references/zitierweise.md`.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
