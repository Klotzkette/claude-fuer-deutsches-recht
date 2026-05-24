---
name: corporate-kanzlei-automation-monitoring
description: "Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugaenge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben."
---

# Automationen und Monitoring

## Zweck

Entwirft Monitore für Datenraum-Neuzugänge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben.

## Arbeitsmodus

- Nur Vorschläge für Automationen machen, keine vertraulichen Daten ungefragt beobachten.
- Monitoringziel, Frequenz, Quelle, Owner und Output definieren.
- Eskalationsregeln und Stoppschwellen festlegen.
- Automationsvorschlaege mit Deal-PMO verknuepfen.

## Rote Schwellen

- Unklarer Datenzugriff.
- Monitoring von Insiderinformationen ohne Freigabe.
- Automatische Außenkommunikation.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `corporate-kanzlei-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/monitoring-automation-plan.md
- assets/templates/deal-pmo-weekly.md
