---
name: corporate-kanzlei-distressed-ma
description: "Distressed M&A: Führt Unternehmenskauf in Krise, vorlaeufiger Insolvenz, Insolvenzplan oder Asset Deal aus der Insolvenz."
---

# Distressed M&A

## Zweck

Führt Unternehmenskauf in Krise, vorläufiger Insolvenz, Insolvenzplan oder Asset Deal aus der Insolvenz.

## Arbeitsmodus

- Status der Krise und Verfahrensstand erfassen.
- Asset Deal/Share Deal/Planlösung vergleichen.
- Sicherheiten, Eigentum, Arbeitnehmerübergang, Anfechtung und Massefragen markieren.
- Closing-Fähigkeit und Zustimmungserfordernisse prüfen.

## Rote Schwellen

- Insolvenzrechtlicher Status unklar.
- Eigentum oder Sicherheiten nicht belegt.
- Betriebsübergang/Arbeitnehmerinformation offen.

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

- assets/templates/distressed-ma-timeline.md
- assets/templates/insolvenzplan-ma-checklist.md
