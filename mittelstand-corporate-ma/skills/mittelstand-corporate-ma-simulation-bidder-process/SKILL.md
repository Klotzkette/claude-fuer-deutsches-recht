---
name: mittelstand-corporate-ma-simulation-bidder-process
description: "Bieterprozess-Simulation: Simuliert einen beschleunigten achtstuendigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call."
---

# Bieterprozess-Simulation

## Zweck

Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call.

## Arbeitsmodus

- Szenario, Rolle und Geschwindigkeit festlegen.
- Datenraumereignisse, Bieterfragen, Markups und Freigaben simulieren.
- Nutzer durch Entscheidungen führen.
- Am Ende Lessons Learned und offene Punkte ausgeben.

## Rote Schwellen

- Simulation wird als echter Rechtsrat missverstanden.
- Keine Trennung zwischen Dummy-Daten und echten Daten.
- Rote Schwellen werden im Spielmodus ignoriert.

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

- assets/templates/deal-simulation-day.md
- assets/templates/workflow-deal-kommandocenter.md
