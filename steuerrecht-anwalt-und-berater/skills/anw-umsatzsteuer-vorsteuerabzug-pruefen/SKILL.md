---
name: anw-umsatzsteuer-vorsteuerabzug-pruefen
description: "Workflow-Skill zu anw umsatzsteuer vorsteuerabzug pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

# Umsatzsteuer-Vorsteuerabzug prüfen

## Zweck

Vorsteuerabzug § 15 UStG ist ein zentrales Element der USt-Mandanten-Beratung — bei Fehlern Berichtigung mit Zins-Folgen, im schlimmsten Fall Strafverfahren.

## Schritt 1 — Voraussetzungen § 15 Abs. 1 UStG

### 1. Unternehmer-Eigenschaft § 2 UStG

- **Selbstständige Tätigkeit**
- **Nachhaltige Einnahmen-Erzielung**
- **Auch bei steuerfreien Umsätzen** Unternehmer
- Bei Holding ohne aktive Geschäfts-Tätigkeit problematisch

### 2. Leistung von Unternehmer

- **Rechnungsgeber** ebenfalls Unternehmer
- USt-IdNr. überprüfbar (qualifizierte Bestätigungsanfrage BZSt)

### 3. Für sein Unternehmen ausgeführt

- **Mindestens 10 Prozent** unternehmerische Nutzung § 15 Abs. 1 Satz 2 UStG
- Bei Pkw-Sondernorm
- Bei Gemischt-Nutzung Vorsteuerabzug anteilig

### 4. Ordnungsgemäße Rechnung § 14 UStG

Pflichtangaben § 14 Abs. 4 UStG:
- **Name und Anschrift Rechnungssteller**
- **Name und Anschrift Leistungs-Empfänger**
- **Steuer-Nummer oder USt-IdNr.**
- **Ausstellungs-Datum**
- **Rechnungs-Nummer** fortlaufend einmalig
- **Menge und Art** der Lieferung / Leistung
- **Zeitpunkt** der Lieferung / Leistung
- **Entgelt** netto pro Steuer-Satz
- **Steuer-Betrag** mit angewandtem Satz
- **Im Fall Steuerbefreiung** Hinweis auf Befreiungs-Vorschrift
- **Bei Reverse-Charge** Hinweis "Steuerschuldnerschaft des Leistungs-Empfängers"

### 4a. eRechnung-Pflicht ab 1.1.2025 (Wachstumschancengesetz)

**B2B-eRechnung** durch Wachstumschancengesetz (WtcG, 27.3.2024) in § 14 UStG eingefuehrt — Pflicht seit **1.1.2025** mit gestaffelten Uebergangsfristen:

- **Empfangs-Pflicht**: Seit 1.1.2025 muss jeder inländische Unternehmer für inländische B2B-Umsätze eRechnungen empfangen können.
- **Ausstellungs-Pflicht** (gestaffelt):
  - bis 31.12.2026: Papier-/PDF-Rechnung mit Zustimmung des Empfaengers weiterhin zulaessig (Übergang)
  - bis 31.12.2027: nur fuer Unternehmer mit Vorjahresumsatz ≤ 800 000 EUR Papier-Erleichterung
  - ab 1.1.2028: vollständige eRechnungspflicht für alle B2B-Inlands-Umsätze
- **Format**: strukturiertes, maschinenlesbares Format nach EN 16931 (z. B. **XRechnung** oder **ZUGFeRD ab Profil EN-16931**); reines PDF ohne strukturierte XML-Daten ist KEINE eRechnung.
- **Folge fehlerhafter Rechnung**: Vorsteuerabzug nach § 15 Abs. 1 UStG kann verweigert werden, wenn Rechnungspflicht eRechnung verletzt ist (BMF-Schreiben vom 15.10.2024 zur eRechnung).
- **Ausnahmen**: Kleinbetragsrechnungen ≤ 250 EUR § 33 UStDV; Fahrausweise § 34 UStDV; Umsätze an Endverbraucher (B2C) bleiben außerhalb.

## Schritt 2 — Ausschluss § 15 Abs. 2 UStG

### Steuerfreie Umsätze mit Vorsteuerabzugs-Ausschluss

- **§ 4 Nr. 8 UStG** Geld- Bank-Geschäfte
- **§ 4 Nr. 9 a UStG** Grundstücks-Umsätze
- **§ 4 Nr. 10 UStG** Versicherungs-Umsätze
- **§ 4 Nr. 12 UStG** Wohnungs-Vermietung
- **§ 4 Nr. 14 UStG** ärztliche Heilbehandlungen
- **§ 4 Nr. 19 UStG** Schulen und Hochschulen

### Ausnahmen § 15 Abs. 3 UStG (trotz Steuerfreiheit Abzug)

- **Ausfuhr-Lieferung** § 4 Nr. 1 a iVm § 6 UStG
- **Innergemeinschaftliche Lieferung** § 4 Nr. 1 b iVm § 6a UStG
- **Hilfsumsatz-Konstellation**

## Schritt 3 — Spezielle Konstellationen

### Pkw

- **Vorsteuerabzug** möglich bei mindestens 10 Prozent unternehmerische Nutzung
- **Anteilig** bei gemischt-Nutzung
- **Eigenleistung Privatnutzung** als Wertabgabe steuerbar § 3 Abs. 9a UStG

### Bewirtungs-Aufwendungen

- Bei Bewirtungs-Beleg mit Pflichtangaben § 4 Abs. 5 Nr. 2 EStG Vorsteuer-Abzug zulässig
- 70-Prozent-Beschränkung gilt nur für ESt nicht USt
- Voller Vorsteuerabzug bei Bewirtungs-Aufwendungen

### Bewirtung von Mitarbeitern

- Voller Vorsteuerabzug
- Keine Werts-Abgabe wenn freiwillig im überwiegend betrieblichen Interesse

### Geschenke

- **Über EUR 35** keine Vorsteuer-Abzugs-Berechtigung
- **Streuwerbe-Artikel** unter EUR 10 ohne Limit

### Reisekosten

- **Vorsteuerabzug** für Hotel Verpflegung Mietwagen bei beleghafter Rechnung
- **Pauschal-Beträge** ohne Vorsteuer-Bezug

### Drittland-Bezug

- **Einfuhr-Umsatzsteuer** als Vorsteuer abzugsfähig § 15 Abs. 1 Satz 1 Nr. 2 UStG
- **Ausland-Umsatzsteuer** nicht in DE abzugsfähig — Vergütungsverfahren

## Schritt 4 — Berichtigung § 15a UStG

### Änderung der Verhältnisse

- Bei Wirtschaftsgütern (typisch Anlagevermögen Immobilien)
- Bei nutzungsspezifischer Änderung des Vorsteuerabzugs-Bezugs

### Berichtigungs-Zeitraum

- **Fünf Jahre** bei beweglichen Wirtschaftsgütern
- **Zehn Jahre** bei Grundstücken / Gebäuden
- Beginnt mit Erstverwendung

### Berechnung

- **Pro Jahr ein Fünftel / ein Zehntel** des ursprünglichen Vorsteuer-Betrags
- Bei Veränderung in einem Jahr Korrektur dieses Anteils

### Beispiel

- Immobilie 2021 mit 100% Vorsteuerabzug, Wert EUR 1 Mio, USt EUR 190.000
- 2024 zur 50% Wohnnutzung umgewidmet
- Berichtigung: EUR 190.000 / 10 Jahre * 50% = EUR 9.500 pro Jahr Berichtigung

## Schritt 5 — Praktische Prüfung Rechnung

### Checkliste

- [ ] Name und Anschrift komplett (auch bei kleinen Beträgen — Klein-Betrag-Rechnung bis EUR 250 § 33 UStDV)
- [ ] Steuer-Nummer / USt-IdNr. richtig
- [ ] Rechnungs-Nummer und Datum vorhanden
- [ ] Leistungs-Beschreibung konkret (nicht "Allgemeine Dienstleistung")
- [ ] Leistungs-Zeitraum genannt
- [ ] Netto-Beträge pro Steuer-Satz separat
- [ ] Steuer-Betrag separat ausgewiesen
- [ ] Rechtsgrundlage bei Reverse-Charge

### Bei Mängeln

- **Berichtigung** erfordern beim Rechnungsstellers
- **Vor-Vorsteuer-Abzug nicht möglich** bis Berichtigung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 6 — Klein-Betrag-Rechnung § 33 UStDV

### Bis EUR 250

- Reduzierte Pflichtangaben
- Aber: Steuer-Satz angegeben
- Anwendbar typisch bei Bewirtungs-Belegen Tankstellen-Rechnungen

## Schritt 7 — Reverse-Charge § 13b UStG

### Anwendungs-Bereiche

- **EU-Vorleistungen** § 13b Abs. 1 UStG
- **Baudienstleistungen** § 13b Abs. 5 Nr. 4 UStG
- **Schrott / Industrieabfall** § 13b Abs. 5 Nr. 6 UStG
- **Telefon-Karten Strom Gas** § 13b Abs. 5 Nr. 6
- **Mobiltelefone Tablet Spielekonsolen** ab EUR 5000 § 13b Abs. 5 Nr. 11

### Vorgehen

- **Empfänger schuldet USt**
- Rechnung ohne USt-Ausweis
- **Hinweis** "Steuerschuldnerschaft des Leistungs-Empfängers"

### Steuer-Schuld und Vorsteuer

- Rechnungs-Empfänger meldet USt und Vorsteuer zugleich
- Bei voll vorsteuerabzugs-berechtigtem Empfänger Null-Effekt

## Schritt 8 — Steuerstraf-Risiken

### Karussell-Geschäfte

- Vorsteuer-Abzug aus Schein-Lieferungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Aufmerksamkeits-Pflicht bei unüblich niedrigen Preisen
- Verpflichtung zur Sorgfalts-Pflicht

### Bei Verdacht

- Sofort Skill `anw-mandat-triage-steuerrecht` Eil-Modus
- Strafanzeige droht

## Schritt 9 — Berichtigungs-Erklärung § 153 AO

### Pflicht zur Korrektur

- Bei Erkennen einer falschen Steuer-Erklärung
- Unverzüglich
- An zuständiges Finanzamt

### Wirkung

- Verhindert Selbstanzeige-Bedarf bei rechtzeitig
- Bei Vorsteuer-Karussell mit Wissen ggf. nicht ausreichend

## Schritt 10 — Bei Außenprüfung

- Stichprobe-Prüfung Rechnungs-Pflichten
- Vorsteuer-Abzug bei mangelnder Sorgfalt korrigiert
- Hinzuschätzung möglich

## Ausgabe

- `vorsteuer-pruefung-{az}.md`
- Rechnungs-Tabelle mit Mängel-Bewertung
- Bei Mangel Korrektur-Anforderung
- Berichtigung-Vorbereitung wenn relevant
- Frist im Fristenbuch (USt-Voranmeldung)

## Quellen

- UStG §§ 1 2 3 4 13b 14 15 15a
- UStDV § 33
- AO § 153
- EStG § 4 Abs. 5
- BFH V. Senat XI. Senat
- BMF-Schreiben Vorsteuerabzug
- Sölch/Ringleb UStG
- Tipke/Lang Steuerrecht
