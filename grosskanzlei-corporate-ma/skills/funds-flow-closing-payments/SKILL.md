---
name: funds-flow-closing-payments
description: Erstellt Funds-Flow-Tabellen, Zahlungslogik, Escrow-, Payoff- und Sicherheitenfreigabe-Checklisten für Closing-Termine.
---
# Funds Flow und Closing Payments

Nutze diesen Skill für die Zahlungsseite eines Closings: Kaufpreis, Debt Payoff, Escrow, Leakage-Ausgleich, Kosten, Sicherheitenfreigabe und Bestätigungen. Ziel ist ein zahlungsfähiger Ablauf, nicht nur eine Tabelle.

## Kaltstartfragen

1. Welche Beträge sind am Closing Day zu zahlen und in welcher Währung?
2. Wer zahlt an wen: Käufer, Käuferbank, Escrow Agent, Verkäufer, Zielgesellschaft?
3. Welche Payoff Letters, Release Letters oder Kontoangaben fehlen?
4. Gibt es Escrow, Holdback, Set-off oder Closing Accounts Adjustment?
5. Welche Zahlungen sind brutto, netto, mit Quellensteuer oder Kostenabzug?
6. Wer bestätigt Zahlungseingang und wann wird übertragen?

## Funds-Flow-Tabelle

| Zahlung | Schuldner | Empfänger | Betrag | Konto | Bedingung | Nachweis |
| --- | --- | --- | --- | --- | --- | --- |
| Kaufpreis | Käufer | Verkäufer | | | Closing-Freigabe | Zahlungsbeleg |
| Debt Payoff | Käuferbank | Bank | | | Payoff Letter | Release |
| Escrow | Käufer | Escrow Agent | | | Escrow Agreement | Bestätigung |

## Prüfraster

1. SPA-Zahlungsmechanik und Closing Deliverables nebeneinanderlegen.
2. Kontodaten, IBAN, Empfängername, Reference und Cut-off-Zeit prüfen.
3. Zahlungsreihenfolge festlegen: Payoff, Release, Kaufpreis, Escrow, Deliverables.
4. Sicherheitenfreigaben und Registerfolge dokumentieren.
5. Closing-Call-Script vorbereiten: wer bestätigt welchen Schritt?

## Rechtsprechungs- und Normanker

- Paragraf 362 BGB: Erfüllung durch Leistung an den richtigen Gläubiger.
- Paragraf 158 BGB: bedingter Vollzug bei Closing-Mechanik.
- Paragraf 15 und 16 sowie Paragraf 40 GmbHG: Anteilserwerb und Wirksamkeitsnachweise bei GmbH-Share-Deals.
- Paragraf 257 HGB: Belegspur für Zahlungs- und Handelsunterlagen.

## Output

Erzeuge eine Funds-Flow-Tabelle, ein Closing-Call-Script und eine Liste der fehlenden Zahlungsnachweise. Markiere harte Closing-Blocker.
