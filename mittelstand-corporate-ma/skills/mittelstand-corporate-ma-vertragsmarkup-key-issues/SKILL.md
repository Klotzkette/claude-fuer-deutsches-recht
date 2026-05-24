---
name: mittelstand-corporate-ma-vertragsmarkup-key-issues
description: "Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschlaege nach Parteiperspektive."
---

# Markup und Key Issues

## Zweck

Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive.

## Arbeitsmodus

- Änderungen nach wirtschaftlicher Relevanz und Rechtsrisiko clustern.
- Position Buy-side/Sell-side transparent halten.
- Rote Linien, Konzessionen und Verhandlungsstrategie trennen.
- Gegenentwurf nur als Vorschlag mit Review-Status ausgeben.

## Rote Schwellen

- Gegenseitenmarkup falsch gelesen.
- Marktüblichkeit ohne eigene Präzedenz- oder Quellenbasis behauptet.
- Risk shift ohne Mandantenentscheidung.

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

- assets/templates/key-issues-list.md
- assets/templates/markup-response-sheet.md
