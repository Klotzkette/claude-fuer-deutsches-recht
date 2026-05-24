---
name: mittelstand-corporate-ma-datenraum-gap-clean-room
description: "Datenraum-Gap-Analyse und Clean Room: Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Luecken, Widersprueche, Dubletten und Clean-Room-Bedarf."
---

# Datenraum-Gap-Analyse und Clean Room

## Zweck

Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf.

## Arbeitsmodus

- Datenraum gegen IRL und IM abgleichen.
- Referenzierte, aber fehlende Dokumente finden.
- Widersprüche zwischen Legal, Tax, Finance, ESG und Commercial markieren.
- Clean-Room-Zugriffe und kartellrechtliche Sensibilitaet protokollieren.

## Rote Schwellen

- Antitrust-sensible Daten offen zugänglich.
- Wichtige Dokumente nur implizit oder unklar benannt.
- KI-sortierter Datenraum ohne menschliches Gate.

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

- assets/templates/datenraum-gap-analysis.md
- assets/templates/clean-room-access-log.md
- assets/templates/data-quality-gate.md
