---
name: corporate-kanzlei-kg-personengesellschaften
description: "KG und Personengesellschaften: Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register."
---

# KG und Personengesellschaften

## Zweck

Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register.

## Arbeitsmodus

- Gesellschaftsvertrag, Handelsregister und Gesellschafterliste auswerten.
- Zustimmungen, Vinkulierung, Drag/Tag, Abfindung, Nachhaftung und Haftsumme prüfen.
- Steuerliche und wirtschaftliche Sonderthemen an Tax/Finance übergeben.
- Register- und Notarschritte dokumentieren.

## Rote Schwellen

- Haftsumme/Registerstand unklar.
- Kommanditistenwechsel ohne Zustimmungskette.
- Kapital-/Steuerkonto nicht berücksichtigt.

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

- assets/templates/kg-gmbh-co-kg-checkliste.md
- assets/templates/handelsregister-corporate-housekeeping.md
