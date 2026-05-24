---
name: kanzlei-allgemein-ustva-buchhaltung
description: "Sammelt Ausgangsrechnungen Eingangsrechnungen Betriebsausgaben Vorsteuer Umsatzsteuer Zahlungsstatus und Belege für die monatliche UStVA. Übergibt an ELSTER Steuerkanzlei Buchhaltung oder UStVA-Simulation ohne stille Abgabe."
---

# UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung

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
