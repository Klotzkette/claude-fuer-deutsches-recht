---
name: grosskanzlei-corporate-ma-rechtsprechungsrecherche
description: "Corporate-Rechtsprechungsrecherche: Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung."
---

# Corporate-Rechtsprechungsrecherche

## Zweck

Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung.

## Arbeitsmodus

- Amtliche Bundes- und Landesquellen bevorzugen.
- OpenJur/dejure nur ergänzend nutzen und Fundstellen verifizieren.
- Entscheidungen mit Datum, Aktenzeichen, Fundstelle und Randnummer erfassen.
- Verwertungsnotiz für Vertrag, Memo, Board Paper oder Schriftsatz schreiben.

## Rote Schwellen

- Nicht verifizierte Fundstelle.
- Halluziniertes Aktenzeichen.
- Keine Übertragung auf Deal-Kontext.

## Standardausgabe

- Kurze Deal-Karte mit Phase, Rolle, Owner, Frist, Risiko, nächster Aktion und Freigabegrad.
- Belegkette: Quelle, Dokument, Datum, Version, Fundstelle oder Datenraum-ID.
- Offene Punkte als `TODO` mit Owner und Eskalationsstufe.
- Bei hohem Risiko immer Human-in-the-loop und Senior Review verlangen.

## Übergabe an andere Skills

- Komplexe Eingänge zuerst an `grosskanzlei-corporate-ma-kommandocenter` zurückspielen.
- Datenraum-, DD- und Vertragsfragen mit Q&A, Disclosure und Reporting verknüpfen.
- Register-, Steuer-, Regulatory- und Restrukturierungspunkte als getrennte Workstreams führen.

## Vorlagen

- assets/templates/rechtsprechungsrecherche-deal.md
