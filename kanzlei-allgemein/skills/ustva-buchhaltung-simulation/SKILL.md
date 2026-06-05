---
name: ustva-buchhaltung-simulation
description: "Kanzlei Allgemein Ustva Buchhaltung, Kanzlei Allgemein Ustva Simulation: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Kanzlei Allgemein Ustva Buchhaltung, Kanzlei Allgemein Ustva Simulation

## Arbeitsbereich

Dieser Skill bündelt **Kanzlei Allgemein Ustva Buchhaltung, Kanzlei Allgemein Ustva Simulation** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `kanzlei-allgemein-ustva-buchhaltung` | Sammelt Rechnungsdaten und Belege für die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen für ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG UStVA-Pflicht § 14 UStG Rechnungspflichtangaben GoBD-Aufbewahrung. Prüfraster Ausgangsrechnungen Eingangsrechnungen Betriebsausgaben Vorsteuer Umsatzsteuer Zahlungsstatus Belegprüfung. Output UStVA-Vorbereitung mit strukturierter Belegsammlung ELSTER-Übergabepaket oder Steuerkanzlei-Paket ohne stille Abgabe. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-simulation. |
| `kanzlei-allgemein-ustva-simulation` | Fallback bei ELSTER-Stoerung oder fehlendem Steuersoftware-Zugang für UStVA-Simulation. Anwendungsfall ELSTER-Verbindung funktioniert nicht oder UStVA muss ohne Fachsoftware simuliert werden. Normen § 18 Abs. 1 UStG Abgabefrist § 149 AO Verlaengerungsantrag. Prüfraster ELSTER-Simulation manuelle Eingabe XML-Upload ZUGFeRD-Prüfung Steuerberater-Paket Fehlerdiagnose Übertragungsprotokoll. Output Simulations-Protokoll mit Fehlerdiagnose Lösungsoptionen und vollständigem UStVA-Datenpaket ohne echte Abgabe. Abgrenzung zu kanzlei-allgemein-ustva-buchhaltung (Datensammlung) und kanzlei-allgemein-buchhaltung-konten. |

## Arbeitsweg

Für **Kanzlei Allgemein Ustva Buchhaltung, Kanzlei Allgemein Ustva Simulation** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `kanzlei-allgemein` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `kanzlei-allgemein-ustva-buchhaltung`

**Fokus:** Sammelt Rechnungsdaten und Belege für die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen für ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG UStVA-Pflicht § 14 UStG Rechnungspflichtangaben GoBD-Aufbewahrung. Prüfraster Ausgangsrechnungen Eingangsrechnungen Betriebsausgaben Vorsteuer Umsatzsteuer Zahlungsstatus Belegprüfung. Output UStVA-Vorbereitung mit strukturierter Belegsammlung ELSTER-Übergabepaket oder Steuerkanzlei-Paket ohne stille Abgabe. Abgrenzung zu kanzlei-allgemein-rechnung und kanzlei-allgemein-ustva-simulation.

# UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung


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
- § 147 AO — Aufbewahrungspflicht 10 Jahre fuer Buchungsbelege
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

## 2. `kanzlei-allgemein-ustva-simulation`

**Fokus:** Fallback bei ELSTER-Stoerung oder fehlendem Steuersoftware-Zugang für UStVA-Simulation. Anwendungsfall ELSTER-Verbindung funktioniert nicht oder UStVA muss ohne Fachsoftware simuliert werden. Normen § 18 Abs. 1 UStG Abgabefrist § 149 AO Verlaengerungsantrag. Prüfraster ELSTER-Simulation manuelle Eingabe XML-Upload ZUGFeRD-Prüfung Steuerberater-Paket Fehlerdiagnose Übertragungsprotokoll. Output Simulations-Protokoll mit Fehlerdiagnose Lösungsoptionen und vollständigem UStVA-Datenpaket ohne echte Abgabe. Abgrenzung zu kanzlei-allgemein-ustva-buchhaltung (Datensammlung) und kanzlei-allgemein-buchhaltung-konten.

# UStVA- und ELSTER-Simulation


## Triage zu Beginn
1. Warum steht ELSTER nicht zur Verfuegung: Systemfehler, fehlende Registrierung, fehlende Software, Testzweck?
2. Soll eine vollstaendige ELSTER-Eingabeliste, ein Steuerberater-Paket oder ein XML-Upload-Check erstellt werden?
3. Wurden alle Belege fuer den Simulationszeitraum korrekt anonymisiert (Datenschutz)?
4. Soll der Simulationslauf als Trainings- oder Testprotokoll gespeichert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 18 UStG — Abgabepflicht der UStVA: keine Entbindung durch technischen Ausfall
- § 87a AO — Elektronische Kommunikation mit Behoerden: Form und Authentifizierungsanforderungen
- § 150 Abs. 6 AO — Datenfernuebertragung als Abgabeform; entsprechende technische Standards
- § 152 AO — Verspaetungszuschlag bei Nichtabgabe

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill greift, wenn die Umsatzsteuer-Voranmeldung vorbereitet ist, aber ELSTER, Buchhaltung, XML-Upload oder Fachsoftware nicht angeschlossen ist oder scheitert. Er bietet einen realistischen Übungslauf und sichere Fallbacks, ohne eine echte steuerliche Übermittlung zu behaupten.

## Grundsatz

ELSTER ist kein Ablageort für beliebige Dokumente. Eine UStVA wird in Mein ELSTER im Formular erfasst oder über geeignete Software beziehungsweise passende XML-Daten übertragen. Ein PDF, eine Markdown-Datei oder ein gewöhnliches Tabellenblatt ist kein UStVA-Upload. Wenn XML genutzt wird, muss die Datei zum ELSTER/ERiC-Datensatz passen und technisch geprüft sein.

## Startfrage

> UStVA ist vorbereitet, aber ELSTER oder die Fachsoftware ist nicht angeschlossen. Soll ich den Ablauf simulieren, eine manuelle ELSTER-Eingabeliste erzeugen, ein Steuerberater-Paket bauen oder eine XML-Upload-Prüfung vorbereiten?

## Modi

### Modus A: ELSTER-Online-Simulation

- Formularauswahl simulieren.
- Zeitraum, Steuernummer, Besteuerungsart und Dauerfristverlängerung abfragen.
- Kennzahlen mit Beträgen aus dem Vorbereitungsblatt befüllen.
- Plausibilitätsfehler simulieren.
- Abgabe-Haltepunkt setzen.
- Simuliertes Übertragungsprotokoll nur als Übung markieren.

### Modus B: Manuelle ELSTER-Eingabeliste

- Feld-für-Feld-Eingabebogen erzeugen.
- Beträge, Quellen und Unsicherheiten daneben ausweisen.
- Keine Abgabe behaupten.
- Nach echter Übermittlung Übertragungsprotokoll anfordern.

### Modus C: XML-Upload-Prüfung

- Klären, ob eine Fachsoftware oder ein validierter Export vorhanden ist.
- Keine freie XML-Datei erfinden.
- Wenn ein XML vorliegt: Schema, Datenart, Zeitraum, Steuernummer, Summen und Plausibilität prüfen oder `Validierung offen` markieren.
- Upload nur als Nutzerhandlung oder Fachsoftwareprozess beschreiben.

### Modus D: Steuerberater- oder Buchhaltungspaket

- Summenblatt, Eingangsrechnungen, Ausgangsrechnungen, offene Reverse-Charge-Fragen und Belegliste bündeln.
- Rückfrage an Steuerberater formulieren.
- Keine elektronische Abgabe behaupten.

### Modus E: Fehlerdiagnose

Typische Probleme strukturiert abfragen:

- ELSTER-Zertifikat fehlt oder abgelaufen.
- Falsche Steuernummer oder falscher Mandant.
- Formular nicht gefunden.
- Zeitraum falsch.
- Dauerfristverlängerung unklar.
- XML wird abgelehnt.
- Plausibilitätsfehler.
- Übertragungsprotokoll fehlt.

## Stoppschilder

Immer anhalten bei:

- echter Abgabe,
- Korrekturmeldung,
- Dauerfristverlängerung,
- Sondervorauszahlung,
- Reverse Charge,
- Auslandssachverhalten,
- unklarer Vorsteuer,
- fehlender Steuernummer,
- fehlendem Übertragungsprotokoll.

## Ausgabe

- `assets/templates/ustva-elster-simulation.md`.
- `assets/templates/ustva-elster-eingabebogen.md`.
- `assets/templates/ustva-xml-upload-pruefung.md`.
- `assets/templates/ustva-steuerberater-paket.md`.
