---
name: ustva-buchhaltung-simulation
description: "Für UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welcher Meldezeitraum ist betroffen (Monat oder Quartal) und liegt eine Dauerfristverlängerung vor?
2. Sind alle Ausgangsrechnungen und Eingangsrechnungen des Zeitraums vollstaendig erfasst?
3. Gibt es ungeklärte Buchungsposten oder fehlende Belege, die vor der UStVA-Vorbereitung geklaert werden müssen?
4. Soll die Übergabe an ELSTER, Steuerkanzlei oder an eine Buchhaltungssoftware erfolgen?

## Zentrale Normen
- § 18 UStG — Voranmeldungspflicht; Abgabefrist 10. des Folgemonats
- § 14 UStG — Pflichtangaben auf Rechnungen; Vorsteuerabzug
- § 147 AO — Aufbewahrungspflicht 10 Jahre für Buchungsbelege
- § 152 AO — Verspaetungszuschlag bei verspaeteter Abgabe

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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
