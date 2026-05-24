---
name: mittelstand-corporate-ma-kaltstart
description: "Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpraeferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln."
---

# Deal-Kaltstart

## Zweck

Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln.

## Arbeitsmodus

- Deal-Playbook abfragen: Buy-side/Sell-side, PE/Strategic, Private/Public, Distressed, Carve-out.
- Standard-Schwellen erfassen: Materiality, red flag, escalation, W&I, board reporting.
- Datenquellen erfassen: VDR, Excel, HRB, Bundesanzeiger, Kapitalmarkt, interne Präzedenzfälle.
- Ergebnis als Deal-Profil ablegen.

## Rote Schwellen

- Keine Mandatsannahme oder Konfliktprüfung.
- Keine Festlegung, welche Daten in KI-Werkzeuge duerfen.
- Unklare Rollen zwischen Recht, Tax, Finance, ESG und Commercial.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/deal-kaltstart-profil.md
- assets/templates/authority-matrix.md
