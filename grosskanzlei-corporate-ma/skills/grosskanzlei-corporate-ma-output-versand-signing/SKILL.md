---
name: grosskanzlei-corporate-ma-output-versand-signing
description: "Output, Signing und Versand: Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand."
---

# Output, Signing und Versand

## Zweck

Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand.

## Arbeitsmodus

- Ausgabeformat und Empfängerkreis prüfen.
- Clean-Version, Markup, PDF, Excel und Anlagen konsistent benennen.
- Signatur-, Notar-, beA-, Kurier- und Datenraum-Uploads protokollieren.
- Versand nur mit Freigabekarte.

## Rote Schwellen

- Falscher Empfängerkreis.
- Nicht freigegebene Version.
- Signing-Dokument ohne finale Anlagen.

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

- assets/templates/signing-ceremony-checklist.md
- assets/templates/closing-deliverables-register.md
