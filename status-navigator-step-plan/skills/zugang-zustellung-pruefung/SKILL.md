---
name: zugang-zustellung-pruefung
description: "Erfasst den Versendungs- und Zustellungsstatus aller zugangsbeduerftigen Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Mahnungen. Markiert, wo der Zugang unklar ist oder noch nachzuweisen waere. Trifft keine rechtliche Bewertung des Zugangs."
---

# Zugang und Zustellung pruefen

## Rolle und Fokus
Erfasst den Versendungs- und Zustellungsstatus aller zugangsbeduerftigen Willenserklaerungen. Markiert, wo der Zugang unklar ist oder nachzuweisen waere. Keine rechtliche Bewertung des Zugangs.

## Vorgehen

1. **Zugangsbeduerftige Erklaerungen aus Reiter 2 extrahieren** — Skill `dokumententyp-erklaerungen` liefert die Vorauswahl.
2. **Versand-Mittel pro Erklaerung erfassen** — Einschreiben mit Rueckschein, Einwurf-Einschreiben, Bote, einfacher Brief, E-Mail, Fax, Zustellungsurkunde.
3. **Zugangs-Beweisspur dokumentieren** — Rueckschein, Sendungsverfolgung, Botenversicherung, Lesebestaetigung, Faxprotokoll, eEB.
4. **§ 130 BGB-Voraussetzungen pro Erklaerung listen** — Empfangsmoeglichkeit zur ueblichen Zeit, Vertreter, Empfangsbote vs. Erklaerungsbote.
5. **Klassifizierung** — `zugegangen` (mit Nachweis), `verschickt, Zugang ungenau`, `Zugang fehlt`.

## Anwendungsbeispiel
LausitzStorage Zugangsspuren: Drawstop-Schreiben NordCap vom 22.05.2026 ging per E-Mail ohne Empfangsbestaetigung an Bauernfeind, Zugang ungenau — § 130 BGB Voraussetzungen unklar fuer Empfangsmoeglichkeit, da Bauernfeind zu der Zeit auf Dienstreise; LEAG-Kuendigungsdrohung vom 19.05.2026 als E-Mail-Thread an mehrere Mitarbeiter, Zugangs-Beweisspur uneinheitlich; Faelligstellungs-Vorbereitung wuerde Boten-Zustellung erfordern.

## Output-Module
- Zugangs-Beweisplan je Erklaerung
- Markierung der Erklaerungen ohne sichere Zustellung in Reiter 3
- Empfehlung Boten-Zustellung fuer kritische Folge-Erklaerungen
