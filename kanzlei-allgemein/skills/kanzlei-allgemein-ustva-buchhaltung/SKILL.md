---
name: kanzlei-allgemein-ustva-buchhaltung
description: "Sammelt Rechnungsdaten und Belege fuer die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen fuer ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG UStVA-Pflicht § 14 UStG Rechnungspflichtangaben GoBD-Aufbewahrung. Pruefraster Ausgangsrechnungen Eingangsrechnungen Betriebsausgaben Vorsteuer Umsatzsteuer Zahlungsstatus Belegpruefung. Output UStVA-Vorbereitung mit strukturierter Belegsammlung ELSTER-Uebergabepaket oder Steuerkanzlei-Paket ohne stille Abgabe. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-simulation."
---

# UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung


## Triage zu Beginn
1. Welcher Meldezeitraum ist betroffen (Monat oder Quartal) und liegt eine Dauerfristverlängerung vor?
2. Sind alle Ausgangsrechnungen und Eingangsrechnungen des Zeitraums vollstaendig erfasst?
3. Gibt es ungeklärte Buchungsposten oder fehlende Belege, die vor der UStVA-Vorbereitung geklaert werden muessen?
4. Soll die Uebergabe an ELSTER, Steuerkanzlei oder an eine Buchhaltungssoftware erfolgen?

## Aktuelle Rechtsprechung
- BFH, Urt. v. 24.06.2020 - X R 23/18, BStBl. II 2021, 170 — GoBD-konforme Belegführung: alle Buchungsbelege muessen unveraenderbar und zeitgerecht archiviert werden; nachtraeglich erstellte Belege koennen abgelehnt werden.
- BFH, Urt. v. 20.10.2021 - XI R 38/19, BStBl. II 2022, 342 — Vorsteuerabzug erfordert ordnungsgemaesse Rechnung nach § 14 UStG; fehlende Pflichtangaben schliessen Vorsteuerabzug aus.
- BFH, Urt. v. 25.09.2019 - XI R 34/17, BStBl. II 2020, 122 — Dauerfristverlaengerung setzt 1/11-Sondervorauszahlung voraus; Versaeumnis begruendet Spaetverzugsfolgen.
- FG Muenchen, Urt. v. 23.06.2022 - 14 K 2131/21, EFG 2023, 201 — UStVA-Abgabefrist 10. des Folgemonats (mit Dauerfristverlaengerung: 10. des uebernnaechsten Monats); Verpaetung fuehrt zu Verspaetungszuschlag nach § 152 AO.

## Zentrale Normen
- § 18 UStG — Voranmeldungspflicht; Abgabefrist 10. des Folgemonats
- § 14 UStG — Pflichtangaben auf Rechnungen; Vorsteuerabzug
- § 147 AO — Aufbewahrungspflicht 10 Jahre fuer Buchungsbelege
- § 152 AO — Verspaetungszuschlag bei verspaeteter Abgabe

## Kommentarliteratur
- Tipke/Lang Steuerrecht, 24. Aufl. 2021, § 17 Rn. 1-50 (Umsatzsteuer-Voranmeldung: Pflichten und Verfahren)
- Beck'scher Online-Kommentar Steuerrecht/Weymans § 18 UStG Rn. 1-40 (Voranmeldung: Frist und Inhalt)

## Zweck

Dieser Skill bereitet die monatliche Umsatzsteuer-Voranmeldung und die Belegsammlung der Kanzlei vor. Er gibt keine Steuerberatung, bucht nicht verbindlich und übermittelt nichts ohne Freigabe.

## Datenquellen

- Ausgangsrechnungen und E-Rechnungen.
- Eingangsrechnungen: Miete, Strom, Telefon, Internet, Cloud, KI-Anbieter, beA-Token, E-Akte, DMS, Fachliteratur, Reisekosten, Fortbildung, Porto, Büromaterial.
- Kontoauszüge.
- Offene-Posten- und Zahlungseingangsregister aus `kanzlei-allgemein-buchhaltung-konten`.
- Kreditkartenabrechnungen.
- Kassenbelege.
- Storno, Gutschriften und Korrekturrechnungen.
- Zahlungsstatus.

## Monatlicher Ablauf

1. UStVA-Zeitraum festlegen.
2. Steuerpflichtige Umsätze aus Ausgangsrechnungen sammeln.
3. Vereinnahmte oder vereinbarte Entgelte je nach Besteuerungsart markieren.
4. Eingangsrechnungen und Vorsteuer prüfen.
5. Reverse-Charge, Ausland, Kleinunternehmer, steuerfreie Umsätze und Fremdgeld als Unsicherheit markieren.
6. Belege nach GoBD-näher Ablage prüfen.
7. Zahlungseingänge und Ausgangsrechnungen mit offenen Posten abstimmen.
8. Summenblatt erzeugen.
9. Übergabe an ELSTER, Steuerberater oder Buchhaltung vorbereiten.
10. Wenn Bank, Buchhaltung, ELSTER oder Fachsoftware nicht angeschlossen ist oder scheitert: Simulation anbieten.
11. Übertragungsprotokoll nach echter Abgabe anfordern und ablegen.

## UStVA-Leitplanken

- Keine stille elektronische Abgabe.
- Keine Abgabe ohne Steuernummer, Zeitraum, Besteuerungsart, Summenprüfung und Freigabe.
- Bei ELSTER oder Fachsystem: Übertragungsprotokoll speichern.
- Kein beliebiges Dokument als ELSTER-Upload ausgeben. Für Mein ELSTER kann ein Eingabebogen erstellt werden; XML-Upload nur, wenn eine passende Fachsoftware oder ein validierter ELSTER/ERiC-Datensatz vorliegt.
- Wenn ein XML erzeugt oder geprüft werden soll: Schema, Datenart, Zeitraum, Steuernummer, Summen und Plausibilität offen ausweisen.
- Bei Dauerfristverlängerung und Sondervorauszahlung gesondert fragen.
- Wenn Unsicherheit besteht, Steuerberater-Rückfrage formulieren.

## Wenn ELSTER nicht funktioniert

Freundlich anbieten:

1. `ELSTER simulieren`: Übungslauf mit fiktivem Formular und Haltepunkt vor Abgabe.
2. `Eingabebogen erzeugen`: Werte so aufbereiten, dass der Nutzer sie in Mein ELSTER manuell eintragen kann.
3. `XML-Upload prüfen`: vorhandene Fachsoftware-XML gegen Grunddaten und Validierungsstatus prüfen.
4. `Steuerberater-Paket bauen`: Belege, Summen und Rückfragen bündeln.
5. `Fehler diagnostizieren`: Zertifikat, Steuernummer, Zeitraum, Formular, Plausibilität oder Übertragungsprotokoll prüfen.

## Eingangsrechnungen

Für jede Eingangsrechnung erfassen:

- Lieferant.
- Rechnungsdatum.
- Leistungszeitraum.
- Nettobetrag.
- Umsatzsteuerbetrag.
- Steuersatz.
- Bruttobetrag.
- Kategorie.
- Zahlungsstatus.
- Belegdatei.
- Vorsteuerabzug: ja, nein, unklar.
- Besonderheit: Ausland, Reverse Charge, Kleinbetragsrechnung, Bewirtung, gemischt privat.

## Ausgabe

- `assets/templates/eingangsrechnungen-register.md`.
- `assets/templates/ustva-vorbereitungsblatt.md`.
- `assets/templates/ustva-elster-eingabebogen.md`, wenn ELSTER manuell befüllt werden soll.
- `assets/templates/ustva-elster-simulation.md`, wenn nur geübt wird.
- Bei Rechnungen zusätzlich `assets/templates/gobd-rechnungsprotokoll.md`.
- Bei Kontenabgleich zusätzlich `assets/templates/offene-posten-debitoren.md` und `assets/templates/zahlungseingang-matching.md`.
