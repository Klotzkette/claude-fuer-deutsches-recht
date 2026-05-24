---
name: mandat-triage-steuerrecht
description: Strukturierte Eingangs-Abfrage fuer steuerrechtliche Mandate (anders als kaltstart-interview welches die Plugin-Konfiguration befuellt). Klaert Mandantenrolle (Steuerpflichtiger Steuerberater-Kollegen Finanzamt selten) Steuerart (ESt KSt GewSt USt ErbSt SchenkSt GrESt) Vorgang (Festsetzungsbescheid Aenderungsbescheid Schaetzungsbescheid Haftungsbescheid Aussenpruefung Selbstanzeige Aussetzung Vollziehung verbindliche Auskunft Klage Finanzgericht) Sofort-Fristen Einspruchsfrist ein Monat § 355 AO Jahres-Frist bei fehlender Belehrung § 356 AO Klagefrist ein Monat § 47 FGO. Eskalation Telefon-Sofort bei Selbstanzeige-Bedarf Hausdurchsuchung Steuerfahndung Vollziehung droht.
---

# Mandat-Triage Steuerrecht

## Zweck

Steuerrechts-Mandate sind kurzfristig fristgeprägt (Einspruch ein Monat) und sehr unterschiedlich (ESt-Bescheid bis Steuerstrafverfahren). Triage stellt die richtige Spur sicher — ergänzend zum Plugin-Konfigurations-Skill `kaltstart-interview`.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Steuerpflichtiger Privatperson
- Selbstständig
- GmbH / AG / KG
- Steuerberater (Kollegen-Vertretung)
- Steuerstrafverteidigung
- Geschäftsführer-Haftung Steuern § 69 AO
- Erbe (Erbschaftsteuer)
- Beschenkter (Schenkungsteuer)

### Frage 2 — Steuerart?

- Einkommensteuer ESt
- Lohnsteuer LSt
- Körperschaftsteuer KSt
- Gewerbesteuer GewSt
- Umsatzsteuer USt
- Erbschaft- und Schenkungsteuer ErbSt / SchenkSt
- Grunderwerbsteuer GrESt
- Grundsteuer
- Kfz-Steuer
- Investitionszulagen Forschungs- und Entwicklungs-Förderung
- Internationale Besteuerung / DBA
- Steuerstrafrecht / Selbstanzeige

### Frage 3 — Vorgang?

- Steuererklärung erstellen / abgeben
- Festsetzungsbescheid analysieren
- Änderungs-/Berichtigungsbescheid
- Schätzungsbescheid § 162 AO
- Haftungsbescheid § 191 AO
- Vorläufigkeitsvermerk § 165 AO
- Vorbehalt der Nachprüfung § 164 AO
- Einspruchsverfahren
- Klage Finanzgericht
- Außenprüfung
- USt-Sonderprüfung Lohnsteuerprüfung
- Selbstanzeige § 371 AO
- Steuerstrafverfahren
- Aussetzung der Vollziehung AdV
- Stundungs-/Erlass-Antrag § 222 § 227 AO
- Verbindliche Auskunft § 89 Abs. 2 AO
- Verbindliche Zusage § 204 AO
- Internationale Verständigungsverfahren
- Verrechnungspreise

### Frage 4 — Akute Eilbedürftigkeit?

- **Einspruchsfrist** ein Monat § 355 AO läuft
- **Klagefrist** ein Monat § 47 FGO läuft
- **Vollziehung droht** Vollstreckung
- **Hausdurchsuchung Steuerfahndung** akut
- **Selbstanzeige** wegen drohender Tatentdeckung
- **Außenprüfung** Schlussbesprechung morgen
- **Festsetzungsverjährung** läuft ab

### Frage 5 — Stand?

- Steuererklärung in Vorbereitung
- Bescheid liegt vor (Datum Eingang)
- Einspruch eingelegt — wartet auf Einspruchsentscheidung
- Einspruchsentscheidung — Klage erwogen
- Klage erhoben (Az FG)
- Revision BFH
- Beschwerde Nichtzulassung
- BVerfG Verfassungsbeschwerde
- EuGH-Vorlage
- Stundungs-/Erlass-Antrag
- AdV-Antrag

### Frage 6 — Frist?

- **Einspruch** ein Monat § 355 AO
- **Bei fehlender / fehlerhafter Belehrung** ein Jahr § 356 AO
- **Klage FG** ein Monat § 47 FGO
- **Nichtzulassungsbeschwerde** ein Monat § 116 FGO
- **Revisionsbegründung** zwei Monate § 120 FGO
- **Festsetzungsverjährung** vier (zehn bei Hinterziehung) Jahre § 169 AO
- **Antrag schlichte Änderung** ein Monat § 172 AO
- **Wiedereinsetzung** ein Monat § 110 AO

### Frage 7 — Wirtschaftliche Verhältnisse?

- Steuer-Volumen
- Stundungs-/Erlass-Bedarf
- AdV erforderlich
- PKH möglich

### Frage 8 — Steuerstrafrecht-Dimension?

- Tatentdeckung droht / erfolgt
- Selbstanzeige rechtzeitig
- Schadenshöhe Steuer-Verkürzung
- Mehrere Veranlagungs-Zeiträume

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Bescheid analysieren | `steuerbescheid-analyse` |
| Einspruch formulieren | `einspruch-finanzamt` |
| Klage am FG | `klage-finanzgericht` |
| Aussetzung der Vollziehung | `aussetzung-vollziehung` |
| Verbindliche Auskunft | `verbindliche-auskunft` |
| Selbstanzeige | `selbstanzeige-371` |
| Außenprüfung | `aussenpruefung-begleitung` |
| Akteneinsicht | `akteneinsicht-steuerakte` |
| Fristenbuch | `fristenbuch-steuerrecht` |
| Frist-Berechnung Zustellung | (allgemein im Fristenbuch) |
| Betriebsausgaben-Werbungskosten | `betriebsausgaben-werbungskosten-pruefraster` |
| Plugin-Konfiguration | `kaltstart-interview` |
| Erbschaftsteuer | (Skill erbschaftsteuer-prüfen — perspektivisch) |
| Umsatzsteuer-Prüfung | (Skill ust-prüfung — perspektivisch) |
| Verrechnungspreise | (Skill verrechnungspreise — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — Mandant / Vermittler / Kollegen-Mandat
- **Streitwert** Steuer-Betrag bestimmt Streitwert
- **Versicherungs-Deckung** Berufshaftpflicht Steuerberater Anwalt
- **Komplexität** internationale Sachverhalte Verrechnungspreise Konzerne

## Eskalation

- **Telefon-Sofort** Hausdurchsuchung Steuerfahndung Selbstanzeige-Notfall
- **Binnen einer Stunde** Einspruchsfrist heute / morgen AdV bei drohender Vollziehung
- **Heute** Bescheidanalyse Einspruch-Erstentwurf
- **Diese Woche** Klage-Erstentwurf Verteidigungs-Strategie

## Ausgabe

- `triage-protokoll-steuerrecht.md`
- Aktenanlage
- Frist im Fristenbuch (Einspruch / Klage / Festsetzungsverjährung)
- AdV-Antrag-Vorbereitung wenn relevant
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Quellen

- AO §§ 89 110 162 164 165 169 172 191 222 227 355 356 371
- FGO §§ 47 116 120
- EStG KStG GewStG UStG ErbStG GrEStG
- BFH Std.Spruch
- Tipke/Lang Steuerrecht
- Tipke/Kruse AO/FGO
