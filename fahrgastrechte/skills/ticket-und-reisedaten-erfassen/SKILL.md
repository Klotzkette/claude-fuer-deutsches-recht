---
name: ticket-und-reisedaten-erfassen
description: "Für Ticket- und Reisedaten erfassen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
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
  einheitliche-pnr: ja        # Beweisanzeichen; Kaufvorgang und Vorabinformation prüfen
  einzige-transaktion: ja
  verkauft-durch: eisenbahnunternehmen
  kombination-durch-verkaeufer: nein
  hinweis-getrennte-vertraege-vor-kauf: nicht-belegt
  hinweis-reproduzierbar: nicht-belegt

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

Buchungscodes entscheiden nicht allein über eine Durchgangsfahrkarte. Beim Erwerb einer oder mehrerer Fahrkarten in einer einzigen geschäftlichen Transaktion bei einem Eisenbahnunternehmen gilt Artikel 12 Absatz 3 VO (EU) 2021/782; vorbehaltlich Absatz 5 haftet es bei Anschlussverlust nach Artikeln 18 bis 20. Bei einer Durchgangsfahrkarte zählt die Gesamtverspätung am Endziel. Den Anschlussverlust unter `umsteige-bahnhoefe` erfassen.

Kombiniert ein Fahrkartenverkäufer oder Reiseveranstalter die Tickets auf eigene Initiative in einer einzigen geschäftlichen Transaktion, schuldet er bei Anschlussverlust nach Artikel 12 Absatz 4 die Erstattung des gesamten Transaktionspreises zuzüglich 75 Prozent dieses Betrags. Eine ausdrücklich versprochene Anschlussgarantie ist dafür nicht erforderlich. Nach Absatz 5 entfällt die Haftung aus Absatz 3 oder 4 nur bei Information vor dem Kauf über getrennte Beförderungsverträge und einem zur späteren Verwendung reproduzierbaren Hinweis. Den Informationsnachweis trägt nach Absatz 6 der jeweilige Anbieter. Bestellansicht, Bestätigung, Zahlbeleg und damaligen Hinweis sichern.

Erst wenn diese Tatbestände ausgeschlossen oder die Ausnahme nachgewiesen sind, die getrennten Verträge jeweils für sich bewerten; zusätzliche vertragliche Garantien gesondert prüfen. Die Verkäuferhaftung und die Fahrpreisentschädigung gegen das Eisenbahnunternehmen sind unterschiedliche Ansprüche.

## Operating EVU prüfen

- DB-Vertrieb verkauft auch Konkurrenz-Tickets. Bei NWB-, ÖBB-, FlixTrain-Strecken im DB-Vertriebssystem: **Operating EVU ist das tatsächlich fahrende Unternehmen** — nicht DB Fernverkehr.
- Den Anspruchsgegner anhand der Anspruchsgrundlage bestimmen: Artikel 19 betrifft das haftende Eisenbahnunternehmen; Artikel 12 Absatz 4 kann den Verkäufer oder Reiseveranstalter verpflichten. Vertrieb und tatsächliche Beförderung nicht gleichsetzen.
- Bei DB Regio: häufig Auftrag durch Bundesländer; passivlegitimiert bleibt DB Regio.
- Bei FlixTrain: FlixTrain GmbH, Friedenheimer Brücke 16, 80639 München.

## Pauschalreise-Konstellation

Wenn die Bahnreise Teil einer Pauschalreise (Reiseveranstalter) ist, ergänzen sich Ansprüche aus VO 2021/782 (gegen EVU) und §§ 651a ff. BGB (gegen Reiseveranstalter). Mitteilung an `verspaetung-und-anschlussverlust-einordnen` und ggf. Verweisung auf `prozessrecht` oder `verbraucherschutzrecht-pruefer`.

## Ausgabe

- `fallakte.yaml` mit allen Stammdaten.
- `belegliste.md` mit Prüfer-Flags für fehlende Belege.
- `naechste-schritte.md` Empfehlung auf nächsten Skill (`verspaetung-und-anschlussverlust-einordnen` oder direkt `entschaedigung-berechnen` bei klarer Faktenlage).

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Leitentscheidungen Datenerfassung

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
