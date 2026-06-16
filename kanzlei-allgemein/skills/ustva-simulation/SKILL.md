---
name: ustva-simulation
description: "Fallback bei ELSTER-Stoerung oder fehlendem Steuersoftware-Zugang für UStVA-Simulation. Anwendungsfall ELSTER-Verbindung funktioniert nicht oder UStVA muss ohne Fachsoftware simuliert werden. Normen § 18 Abs. 1 UStG Abgabefrist § 149 AO Verlaengerungsantrag. Prüfraster ELSTER-Simulation manuelle..."
---

# UStVA- und ELSTER-Simulation

## Arbeitsbereich

Fallback bei ELSTER-Stoerung oder fehlendem Steuersoftware-Zugang für UStVA-Simulation. Anwendungsfall ELSTER-Verbindung funktioniert nicht oder UStVA muss ohne Fachsoftware simuliert werden. Normen § 18 Abs. 1 UStG Abgabefrist § 149 AO Verlaengerungsantrag. Prüfraster ELSTER-Simulation manuelle Eingabe XML-Upload ZUGFeRD-Prüfung Steuerberater-Paket Fehlerdiagnose Übertragungsprotokoll. Output Simulations-Protokoll mit Fehlerdiagnose Lösungsoptionen und vollständigem UStVA-Datenpaket ohne echte Abgabe. Abgrenzung zu kanzlei-allgemein-ustva-buchhaltung (Datensammlung) und kanzlei-allgemein-buchhaltung-konten. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Warum steht ELSTER nicht zur Verfuegung: Systemfehler, fehlende Registrierung, fehlende Software, Testzweck?
2. Soll eine vollstaendige ELSTER-Eingabeliste, ein Steuerberater-Paket oder ein XML-Upload-Check erstellt werden?
3. Wurden alle Belege für den Simulationszeitraum korrekt anonymisiert (Datenschutz)?
4. Soll der Simulationslauf als Trainings- oder Testprotokoll gespeichert werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 18 UStG — Abgabepflicht der UStVA: keine Entbindung durch technischen Ausfall
- § 87a AO — Elektronische Kommunikation mit Behörden: Form und Authentifizierungsanforderungen
- § 150 Abs. 6 AO — Datenfernuebertragung als Abgabeform; entsprechende technische Standards
- § 152 AO — Verspaetungszuschlag bei Nichtabgabe

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

