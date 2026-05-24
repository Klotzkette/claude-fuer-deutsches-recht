---
name: corporate-kanzlei-outside-in-target-screening
description: "Outside-in Target Screening: Erstellt fruehe Zielobjekt- und Pipeline-Analysen aus oeffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen."
---

# Outside-in Target Screening

## Zweck

Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen.

## Arbeitsmodus

- Anforderungsprofil des Kaufinteressenten erfassen.
- Zielunternehmen nach Markt, Produkt, Kunden, IP, Compliance, Risiko und Synergie scoren.
- Warnsignale für spätere Due Diligence markieren.
- Keine vertraulichen Daten fingieren; Quellenstatus klar trennen.

## Rote Schwellen

- Quelle nicht verifizierbar.
- Bewertung basiert nur auf Modellannahmen.
- Marktmissbrauchs- oder Insiderrechtsrisiko bei börsennotierten Zielen.

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

- assets/templates/outside-in-assessment.md
- assets/templates/target-pipeline.md
