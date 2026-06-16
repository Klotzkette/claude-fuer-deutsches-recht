---
name: ticket-und-reisedaten-erfassen
description: "Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestaetigungen Reservierungen Foto-Belegen für Fahrgastrechte-Mandate. Extrahiert Buchungscode (PNR) Auftragsnummer Reisetag Strecke Operating EVU Ticketart (Flexpreis Sparpreis Super Sparpreis BC100 Deutschlandticket Zeitkarte) Klasse Preis..."
---

# Ticket- und Reisedaten erfassen

## Eingaben

Typische Belege:

- **Buchungsbestätigung** der DB / FlixTrain / ÖBB als PDF / E-Mail
- **E-Ticket** mit IATA-/UIC-Barcode (Foto, PDF)
- **Sitzplatzreservierung** (separat oder integriert)
- **Reservierungsbestätigung** (Bahn-App-Screenshot, ausgedrucktes Ticket)
- **Verspätungs- oder Annullierungsbenachrichtigung** der DB (SMS, E-Mail, App-Push)
- **Korrespondenz** mit DB Servicecenter Fahrgastrechte
- **Belege zu Auslagen** (Hotel, Taxi, Verpflegung) — Kassenbon, Rechnung
- **DB Navigator-Screenshots** mit Verspätungs-Anzeigen

## Pflichtfelder

```yaml
fall-id: FGR-2026-0042
reisedatum: 2026-05-12
reisende:
  - name: Mueller, Hans
    geburtsdatum: 1972-08-15
    rolle: hauptbuchender
  - name: Mueller, Eva
    geburtsdatum: 1975-03-22
    rolle: ehepartner
  - name: Mueller, Lea
    geburtsdatum: 2010-06-18
    rolle: minderjährig

buchungscode: ABC123          # PNR / Auftragsnummer
buchung-bei: DB Vertrieb GmbH # Verkaufender Vertriebsweg (bahn.de, DB Reisezentrum, Reisebüro)
buchungsdatum: 2026-04-12

ticket:
  art: sparpreis              # flexpreis | sparpreis | super-sparpreis | bahncard-100 | deutschlandticket | zeitkarte | reisepass-tarif
  klasse: 2                   # 1 oder 2
  preis-eur: 79.00            # tatsächlich gezahlter Preis
  zugbindung: ja              # bei sparpreis/super-sparpreis grundsätzlich ja
  bahncard: BC50              # null | BC25 | BC50 | BC100

verbindung-gebucht:
  abfahrt:
    bahnhof: Berlin Hbf
    iata-uic: 8011160
    planmaessig: 2026-05-12T08:25:00+02:00
  ziel:
    bahnhof: Muenchen Hbf
    iata-uic: 8000261
    planmaessig: 2026-05-12T13:20:00+02:00
  zuege:
    - nr: ICE 503
      operating-evu: DB Fernverkehr AG
      abschnitt: Berlin Hbf - Muenchen Hbf
  einheitliche-pnr: ja        # → Durchgangsfahrkarte nach Art. 12 VO

verbindung-tatsaechlich:
  abfahrt-ist: 2026-05-12T08:45:00+02:00   # +20 Min
  ankunft-ist: 2026-05-12T15:05:00+02:00   # +1h 45 Min am Endziel
  zug-tatsaechlich: ICE 503                # ggf. anderer Zug bei Umbuchung
  umsteige-bahnhoefe: []
  endziel-verspaetung-min: 105             # ≥ 60 Min → 25 % Anspruch (ab 120: 50 %)

stoerung:
  art: verspaetung            # verspaetung | zugausfall | anschlussverlust | vorverlegung | nichtbefoerderung
  ursache-laut-db: technischer Defekt
  bekanntgabe-am: 2026-05-12T07:50:00+02:00
  bekanntgabe-wie: app        # app | sms | email | aushang | schalter
  ersatz-angebot: ja
  ersatz-detail: Ersatzfahrt im selben ICE 503 mit Verspätung
  hilfeleistung-erhalten:
    verpflegung: nein
    hotel: nein
    transport: nein

auslagen:
  taxi-eur: 0
  hotel-eur: 0
  verpflegung-eur: 12.50
  belege: [belege/2026-05-12/kassenbon-bahnhofsimbiss.pdf]

belege:
  - typ: buchungsbestaetigung
    pfad: belege/2026-05-12/buchung-ICE503.pdf
  - typ: e-ticket
    pfad: belege/2026-05-12/e-ticket-mueller.pdf
  - typ: stoerungsmeldung
    pfad: belege/2026-05-12/db-navigator-verspaetung.png
  - typ: ankunft-anzeigetafel
    pfad: belege/2026-05-12/foto-anzeigetafel-muenchen.jpg
  - typ: kassenbon
    pfad: belege/2026-05-12/kassenbon-bahnhofsimbiss.pdf
```

## OCR / PDF-Extraktion

- Bei PDF-Tickets automatische Extraktion von PNR / Auftragsnummer, Zugnummer, Datum, Bahnhöfen.
- Bei Foto-Belegen OCR; bei Konfidenz unter 90 Prozent Prüfer-Flag für manuelle Bestätigung.
- DB-Auftragsnummern haben das Format einer 12-stelligen alphanumerischen ID (Bahn-App) oder einer 6-stelligen PNR (klassischer Vertrieb).
- UIC-Stationscodes (8011160 Berlin Hbf, 8000261 München Hbf) prüfen — frei verfügbar bei DB Open Data.

## Beweis-Sicherung der tatsächlichen Ankunftszeit

Maßgeblich ist die **Türöffnung am Zielbahnhof** (Art. 3 Nr. 18 VO 2021/782). Beweiswege:

1. **DB Navigator** speichert die tatsächliche Ankunftszeit unter "Verbindungs-Details" — Screenshot zeitnah sichern.
2. **Fahrgastrechte-Formular der DB Bahn**: Wird die Verspätung bei der DB beantragt, generiert das System eine **Verspätungsbestätigung mit DB-eigenen Daten**. Diese ist im Streit das stärkste Beweismittel.
3. **Schalter-Stempel** auf der Fahrkarte bei Annullierung / Verspätung (älterer Weg).
4. **Foto der Bahnhofs-Anzeigetafel** mit Uhrzeit und tatsächlich angezeigter Ankunftszeit (Beweis im Bestreitensfall).
5. **Zeugen** — Mitreisende.

## DB-Zugverfolgung (intern bei DB)

Die DB verfügt über interne Aufzeichnungen aller Zugbewegungen (Betriebsdatenbank LeiDis-NK / DiRail). Im Klageverfahren kann die Vorlage beantragt werden (§§ 421 ff. ZPO Urkundenbeweis). Vorprozessuale Auskunft über § 242 BGB (sekundäre Darlegungslast).

## Mehrere Reisende

Pro Reise wird **ein** Anspruchsfall mit mehreren Reisenden erfasst. **Jeder Reisende hat einen eigenen Anspruch** (Art. 19 VO ist persönlich); Mindestbetrag 4 EUR ebenfalls pro Fahrkarte. Bei Klage je Reisender eigener Antrag (Streitgenossenschaft möglich nach § 60 ZPO). Vollmacht über `vollmacht-mitreisende`.

## Anschlussverlust unter Durchgangsfahrkarte

Wenn die Buchung mehrere Züge mit **einer PNR** enthält (Art. 12 Abs. 3 VO 2021/782), ist die **Gesamtverspätung am Endziel** maßgeblich — nicht die Verspätung eines einzelnen Etappenzuges. Der Anschlussverlust ist im Yaml unter `umsteige-bahnhoefe` zu erfassen.

Bei **mehreren separat gebuchten Tickets** (eigenständige PNRs) ist jeder Vertrag getrennt zu betrachten — Anschluss-Garantie greift nicht, außer Fahrkartenverkäufer / Reiseveranstalter hat sie ausdrücklich versprochen (Art. 12 Abs. 4 VO).

## Operating EVU prüfen

- DB-Vertrieb verkauft auch Konkurrenz-Tickets. Bei NWB-, ÖBB-, FlixTrain-Strecken im DB-Vertriebssystem: **Operating EVU ist das tatsächlich fahrende Unternehmen** — nicht DB Fernverkehr.
- Anspruchsgegner ist immer das **ausführende EVU** (Art. 19 Abs. 1 VO).
- Bei DB Regio: häufig Auftrag durch Bundesländer; passivlegitimiert bleibt DB Regio.
- Bei FlixTrain: FlixTrain GmbH, Friedenheimer Brücke 16, 80639 München.

## Pauschalreise-Konstellation

Wenn die Bahnreise Teil einer Pauschalreise (Reiseveranstalter) ist, ergänzen sich Ansprüche aus VO 2021/782 (gegen EVU) und §§ 651a ff. BGB (gegen Reiseveranstalter). Mitteilung an `verspaetung-und-anschlussverlust-einordnen` und ggf. Verweisung auf `prozessrecht` oder `verbraucherschutzrecht-pruefer`.

## Ausgabe

- `fallakte.yaml` mit allen Stammdaten.
- `belegliste.md` mit Prüfer-Flags für fehlende Belege.
- `naechste-schritte.md` Empfehlung auf nächsten Skill (`verspaetung-und-anschlussverlust-einordnen` oder direkt `entschaedigung-berechnen` bei klarer Faktenlage).

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Leitentscheidungen Datenerfassung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
