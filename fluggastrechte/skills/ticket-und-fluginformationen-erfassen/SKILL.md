---
name: ticket-und-fluginformationen-erfassen
description: Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestaetigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankunftszeit Tarifklasse Passagiernamen ausfuehrendes Luftfahrtunternehmen (Operating Carrier) vermarktendes (Code-Share). Ergaenzt manuell die Ist-Zeiten (taktsaechliche Abflug- und Ankunftszeit) und das Stoerungsereignis (Annullierung Verspaetung Nichtbefoerderung Umbuchung). Erzeugt Fallakte.
---

# Ticket- und Fluginformationen erfassen

## Eingaben

Was hochgeladen werden kann:

- **Buchungsbestaetigung** als PDF / E-Mail.
- **E-Ticket** mit IATA-Standard-Konfiguration.
- **Boardingpass** Foto oder PDF.
- **Stoerungsbenachrichtigung** von der Airline.
- **Korrespondenz** mit der Airline (E-Mail-Verlauf).
- **Pauschalreiseunterlagen** falls Buchung ueber Reiseveranstalter.

## Pflichtfelder

Zu jedem Flugabschnitt:

```yaml
fall-id: FG-2026-0042
reisedatum: 2026-05-12
passagiere:
  - name: Mueller, Hans
    geburtsdatum: 1972-08-15
    rolle: hauptbuchender
  - name: Mueller, Eva
    geburtsdatum: 1975-03-22
    rolle: ehepartner
  - name: Mueller, Lea
    geburtsdatum: 2010-06-18
    rolle: minderjaehrig

buchungscode: ABC123  # PNR
buchung-bei: Lufthansa  # vermarktende Airline
buchungsdatum: 2026-04-12

flug:
  flugnummer: LH 1234  # Code des operating carrier
  operating-carrier: Lufthansa
  marketing-carrier: Lufthansa
  abflughafen: MUC (Muenchen)
  zielflughafen: LIS (Lissabon)
  geplante-abflugzeit: 2026-05-12T08:25:00+02:00
  geplante-ankunftszeit: 2026-05-12T11:00:00+01:00
  tatsaechliche-abflugzeit: null
  tatsaechliche-ankunftszeit: null
  flugklasse: economy
  distanz-km: 2280  # Skill `distanz-und-ausgleich-berechnen`

stoerung:
  art: annullierung  # annullierung / verspaetung / nichtbefoerderung / umbuchung / abweichender-flug
  bekanntgabe-am: 2026-05-12T06:30:00+02:00
  bekanntgabe-wie: SMS  # SMS / E-Mail / Schalter-Mitteilung
  begruendung-airline: technischer Defekt
  ersatzangebot: Flug am 13.05.2026 LH 1234
  ersatz-tatsaechlich-genutzt: ja

belege:
  - typ: buchungsbestaetigung
    pfad: belege/2026-05-12/buchung-LH1234.pdf
  - typ: boardingpass
    pfad: belege/2026-05-12/boardingpass-mueller.pdf
  - typ: stoerungsbenachrichtigung
    pfad: belege/2026-05-12/sms-annullierung.png
  - typ: ersatzboardingpass
    pfad: belege/2026-05-13/boardingpass-mueller-ersatz.pdf
```

## OCR / PDF-Extraktion

- Bei PDF-Tickets automatische Extraktion von PNR Flugnummer Datum und Flughaefen.
- Bei Foto-Belegen OCR; bei Konfidenz unter 90 Prozent Pruefer-Flag fuer manuelle Bestaetigung.
- IATA-Codes (LH BA AF AZ) und Flughafen-Codes (FRA MUC CDG MAD) gegen Standardlisten validieren.

## Datenabgleich oeffentliche Quellen

- **Flugplandaten** geplante Zeiten aus Buchungsbestaetigung — autoritativ.
- **Ist-Zeiten** koennen Sie aus Boardingpass-Stempel SMS / E-Mail mit Verspaetungs-Hinweis Flughafen-Anzeigetafel-Foto oder Airline-Verspaetungs-API entnehmen.
- Verbraucher-relevante oeffentliche Datenquellen sind regelmaessig **zahlungspflichtig oder nicht autoritativ** (FlightAware FlightRadar24 etc.); im Streit beweisbedeutsam ist die **Eingangsbestaetigung der Airline** und die offizielle **Verspaetungs-/Annullierungsmeldung** der Airline.
- Bei strittiger Ist-Zeit: Empfehlung **eigenhaendige Dokumentation am Tag des Ereignisses** (Fotos Anzeigentafel SMS-Eingaenge) als spaeterer Beweis.

## Ausgabe

- `fallakte.yaml` mit allen Stammdaten.
- `belegliste.md` mit Pruefer-Flags fuer fehlende Belege.
- `naechste-schritte.md` Empfehlung auf naechsten Skill (`annullierung-oder-verspaetung-einordnen`).

## Mehrere Passagiere

Pro Flug wird **ein** Anspruchsfall mit mehreren Passagieren erfasst. Jeder Passagier hat aber einen **eigenen Ausgleichsanspruch** (Art. 7 VO 261/2004 ist persoenlich). Daher bei der Klage je Passagier eigener Antrag (Streitgenossenschaft moeglich). Vollmacht der Mitreisenden falls einer fuer alle vorgeht — Skill `vollmacht-familienmitglieder`.
