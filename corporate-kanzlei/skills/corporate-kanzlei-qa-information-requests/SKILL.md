---
name: corporate-kanzlei-qa-information-requests
description: "Q&A und Information Requests: Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität."
---

# Q&A und Information Requests

## Zweck

Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität.

## Arbeitsmodus

- Aus DD-Lücken gezielte Fragen ableiten.
- Fragen nach Workstream, Prioritaet, Owner und Deal-Auswirkung sortieren.
- Antworten gegen Datenraumbelege prüfen.
- Unzureichende Antworten nachfassen.

## Rote Schwellen

- Frage verraet Strategie unnoetig.
- Antwort ohne Beleg wird als erledigt markiert.
- Q&A enthält Clean-Room-Information in offenem Bereich.

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

- assets/templates/qa-register.md
- assets/templates/information-request-list.md
