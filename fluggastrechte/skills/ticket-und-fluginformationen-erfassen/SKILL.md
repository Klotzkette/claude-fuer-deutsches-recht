---
name: ticket-und-fluginformationen-erfassen
description: "Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestaetigungen Boardingpaesse PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankunftszeit Tarifklasse Passagiernamen ausfuehrendes Luftfahrtunternehmen (Operating Carrier) vermarktendes (Code-Share). Ergaenzt manuell die Ist-Zeiten (taktsaechliche Abflug- und Ankunftszeit) und das Stoerungsereignis (Annullierung Verspaetung Nichtbefoerderung Umbuchung). Erzeugt Fallakte."
---

# Ticket- und Fluginformationen erfassen

## Eingaben

Was hochgeladen werden kann:

- **Buchungsbestätigung** als PDF / E-Mail.
- **E-Ticket** mit IATA-Standard-Konfiguration.
- **Boardingpass** Foto oder PDF.
- **Störungsbenachrichtigung** von der Airline.
- **Korrespondenz** mit der Airline (E-Mail-Verlauf).
- **Pauschalreiseunterlagen** falls Buchung über Reiseveranstalter.

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
    rolle: minderjährig

buchungscode: ABC123  # PNR
buchung-bei: Lufthansa  # vermarktende Airline
buchungsdatum: 2026-04-12

flug:
  flugnummer: LH 1234  # Code des operating carrier
  operating-carrier: Lufthansa
  marketing-carrier: Lufthansa
  abflughafen: MUC (München)
  zielflughafen: LIS (Lissabon)
  geplante-abflugzeit: 2026-05-12T08:25:00+02:00
  geplante-ankunftszeit: 2026-05-12T11:00:00+01:00
  tatsaechliche-abflugzeit: null
  tatsaechliche-ankunftszeit: null
  flugklasse: economy
  distanz-km: 2280  # Skill `distanz-und-ausgleich-berechnen`

stoerung:
  art: annullierung  # annullierung / verspätung / nichtbefoerderung / umbuchung / abweichender-flug
  bekanntgabe-am: 2026-05-12T06:30:00+02:00
  bekanntgabe-wie: SMS  # SMS / E-Mail / Schalter-Mitteilung
  begruendung-airline: technischer Defekt
  ersatzangebot: Flug am 13.05.2026 LH 1234
  ersatz-tatsaechlich-genutzt: ja

belege:
  - typ: buchungsbestätigung
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
- Bei Foto-Belegen OCR; bei Konfidenz unter 90 Prozent Prüfer-Flag für manuelle Bestätigung.
- IATA-Codes (LH BA AF AZ) und Flughafen-Codes (FRA MUC CDG MAD) gegen Standardlisten validieren.

## Datenabgleich öffentliche Quellen

- **Flugplandaten** geplante Zeiten aus Buchungsbestätigung — autoritativ.
- **Ist-Zeiten** können Sie aus Boardingpass-Stempel SMS / E-Mail mit Verspätungs-Hinweis Flughafen-Anzeigetafel-Foto oder Airline-Verspätungs-API entnehmen.
- Verbraucher-relevante öffentliche Datenquellen sind regelmäßig **zahlungspflichtig oder nicht autoritativ** (FlightAware FlightRadar24 etc.); im Streit beweisbedeutsam ist die **Eingangsbestätigung der Airline** und die offizielle **Verspätungs-/Annullierungsmeldung** der Airline.
- Bei strittiger Ist-Zeit: Empfehlung **eigenhändige Dokumentation am Tag des Ereignisses** (Fotos Anzeigentafel SMS-Eingaenge) als späterer Beweis.

## Leitentscheidungen Informationserfassung

- EuGH, Urt. v. 22.12.2008 — C-549/07 (Wallentin-Hermann), NJW 2009, 347 — Vollstaendigkeit der Fluginformationen; Gericht prueft alle relevanten Umstaende; Beweislast liegt bei Airline fuer aussergewoehnliche Umstaende.
- BGH, Urt. v. 30.04.2019 — X ZR 75/18, NJW 2019, 2158 — Dokumentationspflicht des Passagiers; Buchungsbestaetigung und PNR genuegen; keine weiteren Nachweise erforderlich.
- EuGH, Urt. v. 04.05.2017 — C-315/15 (Pepicova), NJW 2017, 1954 — Buchungsnachweis; gescanntes Ticket gilt als Beweis; Airline darf nicht aus formalen Gruenden Anspruch verweigern.

## Kommentarliteratur

- Staudinger/Arnold VO 261/2004 Art. 3 Rn. 1-30 (Anwendungsbereich, Erfassung)

## Ausgabe

- `fallakte.yaml` mit allen Stammdaten.
- `belegliste.md` mit Prüfer-Flags für fehlende Belege.
- `naechste-schritte.md` Empfehlung auf nächsten Skill (`annullierung-oder-verspaetung-einordnen`).

## Mehrere Passagiere

Pro Flug wird **ein** Anspruchsfall mit mehreren Passagieren erfasst. Jeder Passagier hat aber einen **eigenen Ausgleichsanspruch** (Art. 7 VO 261/2004 ist persönlich). Daher bei der Klage je Passagier eigener Antrag (Streitgenossenschaft möglich). Vollmacht der Mitreisenden falls einer für alle vorgeht — Skill `vollmacht-familienmitglieder`.
