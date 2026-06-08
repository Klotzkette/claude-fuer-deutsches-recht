---
name: ustva-buchhaltung-simulation
description: "Sammelt Rechnungsdaten und Belege für die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen für ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG UStVA-Pflicht § 14 UStG Rechnungspflichtangaben GoBD-Aufbewahrung. Prüfraster Ausgangsrechnungen Eingangsrechnungen Betriebsausgaben Vorsteuer Umsatzsteuer Zahlungsstatus Belegprüfung. Output UStVA-Vorbereitung mit strukturierter Belegsammlung ELSTER-Übergabepaket oder Steuerkanzlei-Paket ohne stille Abgabe. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-simulation im Kanzlei Allgemein: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung

## Arbeitsbereich

Sammelt Rechnungsdaten und Belege für die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen für ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG UStVA-Pflicht § 14 UStG Rechnungspflichtangaben GoBD-Aufbewahrung. Prüfraster Ausgangsrechnungen Eingangsrechnungen Betriebsausgaben Vorsteuer Umsatzsteuer Zahlungsstatus Belegprüfung. Output UStVA-Vorbereitung mit strukturierter Belegsammlung ELSTER-Übergabepaket oder Steuerkanzlei-Paket ohne stille Abgabe. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-simulation. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welcher Meldezeitraum ist betroffen (Monat oder Quartal) und liegt eine Dauerfristverlängerung vor?
2. Sind alle Ausgangsrechnungen und Eingangsrechnungen des Zeitraums vollstaendig erfasst?
3. Gibt es ungeklärte Buchungsposten oder fehlende Belege, die vor der UStVA-Vorbereitung geklaert werden muessen?
4. Soll die Uebergabe an ELSTER, Steuerkanzlei oder an eine Buchhaltungssoftware erfolgen?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 18 UStG — Voranmeldungspflicht; Abgabefrist 10. des Folgemonats
- § 14 UStG — Pflichtangaben auf Rechnungen; Vorsteuerabzug
- § 147 AO — Aufbewahrungspflicht 10 Jahre für Buchungsbelege
- § 152 AO — Verspaetungszuschlag bei verspaeteter Abgabe

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
