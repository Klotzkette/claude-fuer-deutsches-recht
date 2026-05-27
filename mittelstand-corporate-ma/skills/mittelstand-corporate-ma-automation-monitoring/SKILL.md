---
name: mittelstand-corporate-ma-automation-monitoring
description: "Mandant oder Kanzlei will Deal-Aktivitaeten automatisch tracken: Datenraum-Neuzugaenge Fristen Q&A MAR-Signale PMI-Aufgaben. Normen MAR VO 596/2014 §§ 35-44 GWB Insiderlisten. Pruefraster Datenraum-Monitor CP-Deadline-Kalender Register-Update-Check News-Screening PMI-Task-Tracking. Output Monitoring-Protokoll Alert-Regeln Ampel-Dashboard. Abgrenzung zu mittelstand-ma-fristen-cp-kalender (Fristen-only) und mittelstand-corporate-ma-deal-intake (Eingang)."
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

- Komplexe Eingänge zuerst an `mittelstand-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/monitoring-automation-plan.md
- assets/templates/deal-pmo-weekly.md

## Rechtliche Einbettung und Praxiswissen

### Zentrale Normen
- § 43a BRAO — anwaltliche Pflichten: vollstaendige Mandatsfuehrung; Sorgfaltspflichten gelten auch fuer automatisierte Prozesse
- §§ 675, 280 BGB — Beraterhaftung bei Pflichtverletzung; gilt auch fuer Organisation und Monitoring
- § 49b BRAO — Honorarvereinbarung: Abrechnungsmodalitaeten muessen transparent und schriftlich vereinbart sein
- §§ 93, 116 AktG; § 43 GmbHG — Business Judgment Rule: Entscheidung auf ausreichender Informationsgrundlage; Dokumentationspflicht

### Leitsaetze
- BGH, Urt. v. 21.04.1997 - II ZR 175/95, BGHZ 135, 244 — Business Judgment Rule: Geschaeftsfuehrer handelt pflichtgemaess, wenn er bei einer unternehmerischen Entscheidung vernuenftigerweise annehmen durfte, zum Wohl der Gesellschaft zu handeln; Informationsgrundlage muss angemessen sein
- BGH, Urt. v. 15.03.2012 - IX ZR 35/11, NJW 2012, 1800 — Beraterhaftung: vollstaendige Information des Mandanten ist Kernpflicht; Luecken koennen Schadensersatz ausloesen

### Kommentarliteratur
- MueKo GmbHG/Fleischer, § 43 Rn. 1-80 (Geschaeftsfuehrerhaftung, Business Judgment Rule)
- Schaub, Arbeitsrechts-Handbuch, § 12 (Mandate, Vollmachten, Honorare)

### Qualitaetssicherung
- Human-in-the-loop bei allen automatisierten Ausgaben
- Dokumentation: Datum, Methodik, Human-Check-Protokoll
