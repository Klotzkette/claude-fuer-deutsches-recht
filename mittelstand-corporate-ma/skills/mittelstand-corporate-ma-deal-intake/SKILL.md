---
name: mittelstand-corporate-ma-deal-intake
description: "Deal-Intake: Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung."
---

# Deal-Intake

## Zweck

Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung.

## Arbeitsmodus

- Parteien, Zielgesellschaft, Deal-Typ, Jurisdiktionen, Zeitplan, Vertraulichkeit und erste rote Flaggen extrahieren.
- Konfliktcheck, Sanktionen, Insider-/Clean-Room-Fragen und Mandatsumfang anstoßen.
- Fehlende Kerninformationen als kurze IRL anlegen.
- Akte und Deal-Namen vorschlagen.

## Rote Schwellen

- Keine Konfliktprüfung.
- Insiderinformation oder Marktgeruecht in offenem Kanal.
- Datenraumzugang ohne NDA oder Need-to-know.

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

- assets/templates/deal-intake-sheet.md
- assets/templates/matter-opening-checklist.md
