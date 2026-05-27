---
name: corporate-kanzlei-matter-file
description: "Transaktionsakte strukturieren und verwalten fuer Corporate/M&A-Mandate: Anwalt benoetigt Dokument-Klassifizierung, Versionskontrolle, Zugriffsrechteverwaltung und Aufbewahrungsplanung. Normen: §§ 257 HGB, 147 AO (Aufbewahrungspflichten), BRAO § 50 (Aktenaufbewahrung). Pruefraster: Dokumententypen, Versionierung, Vernichtungsfristen, DSGVO-Archivierung. Output Matter-File-Struktur, Versionierungsprotokoll, Aufbewahrungskalender. Abgrenzung: Closing Bible am Ende siehe closing-bible-archiv; Datenraum-Aufbau siehe datenraum-aufbau."
---

# Matter File und Aktenstruktur

## Triage — klaere vor Aufbau

1. Welche Akte wird angelegt: neues Mandat, bestehende Akte erweiternd, Post-Closing-Archiv?
2. Welche Workstreams haben eigene Unterakten: Legal, Tax, Financial, Regulatory?
3. Zugriffsrechte: Need-to-know; Insider-Schutz; Partner-freigabe?
4. Aufbewahrungsfristen: 6 Jahre (Handelsbriefe), 10 Jahre (steuerliche Unterlagen), oder laenger (Warranties)?
5. Elektronisch oder physisch? (GoBD-konforme Archivierung bei elektronischer Akte)

## Zentrale Normen

- **§ 50 BRAO** — Aktenausgabe; Mandant hat Anspruch auf Herausgabe der fuer ihn erstellten Schriftstuecke
- **§§ 257 f. HGB** — Aufbewahrungspflicht Handelsbuecher 10 Jahre; Handelsbriefe 6 Jahre
- **§ 147 AO** — Steuerliche Aufbewahrungspflicht bis 10 Jahre
- **§ 199 BGB** — Verjährung; Warranty-Ansprueche; Fristen in Akte dokumentieren
- **GoBD** — unveraenderbare elektronische Archivierung; revisionssicher

## Aktuelle Rechtsprechung

- BGH, Urt. v. 09.04.2019 - II ZR 289/17, NJW 2019, 2218 — Dokumentationspflicht: Anwalt muss Akte so fuehren, dass Mandant bei Streit alle relevanten Tatsachen nachvollziehen kann
- BGH, Urt. v. 07.12.2017 - IX ZR 101/17, NZI 2018, 131 — Aktenherausgabe (§ 50 BRAO): Mandant hat Herausgabeanspruch; Kanzlei darf Rueckbehaltungsrecht nur fuer eigene Honoraransprueche geltend machen

## Kommentarliteratur

- Henssler/Pruestell BRAO § 50 Rn. 1 ff. — Aktenrecht und Herausgabepflicht

## Matter-File-Struktur: Corporate M&A

```
MATTER: [DEAL-CODENAME] — Matter-Nr.: [NR.]
Aktenverantwortliche: [Partner Name]

ROOT
├── 01_Mandate & Compliance
│   ├── Mandatsvertrag
│   ├── Conflict-Check-Protokoll
│   ├── GwG-CDD-Bogen
│   └── Insider-Log
├── 02_Transaktionsdokumente
│   ├── Term Sheet / LOI
│   ├── NDA
│   ├── SPA / APA (Versionen)
│   └── Disclosure Letter
├── 03_Due Diligence
│   ├── IRL
│   ├── DD-Workstream-Reports (Legal, Tax, FIN, COM)
│   ├── Red-Flag-Memo
│   └── Q&A-Log
├── 04_Regulatory
│   ├── Kartellrecht (Anmeldung, Freigabe)
│   └── FDI (AWG/AWV-Korrespondenz)
├── 05_Closing
│   ├── CP-Tracker
│   ├── Closing-Checkliste
│   ├── Closing-Bible
│   └── Handelsregister-Anmeldungen
├── 06_Post-Closing
│   ├── PMI-Plan
│   ├── §613a-Informationsschreiben
│   └── Organschaft-Dokumente
└── 07_Korrespondenz
    ├── E-Mail-Archive (wichtige Threads)
    └── Externe Berater-Korrespondenz
```

## Schritt-fuer-Schritt-Workflow

1. **Akte eroffnen** — Matter-Nummer vergeben; Kanzlei-System anlegen; Zugriffsrechte setzen
2. **Grundstruktur anlegen** — Unterordner wie oben; Zugriffsebenen festlegen
3. **Compliance-Docs ablegen** — Conflict Check, GwG-CDD, NDA als erstes
4. **Versions-Disziplin einhalten** — Dokumente nie ueberschreiben; v1, v2, FINAL, EXECUTION
5. **Zugriffsrechte pruefen** — Need-to-know; Insider-Mitglieder bekommen nur ihre Unterordner
6. **Fristen-Kalender einpflegen** — Warranty-Verjährung; Aufbewahrungsfristen; Organschaft-Fristen
7. **Archivierung post-Closing** — GoBD-konform; revisionssicher; 10 Jahre Aufbewahrung

## Output-Template Aktennotiz (kurz)

```
AKTENNOTIZ
Mandat: [DEAL-NAME]
Datum: [DATUM]
Erstellt von: [NAME]
Thema: [THEMA]

SACHVERHALT:
[Kurzbeschreibung des Sachverhalts / Gespraechs / Ereignisses]

RECHTLICHE EINSCHAETZUNG:
[Einschaetzung in 2-3 Saetzen]

EMPFEHLUNG / NAECHSTE SCHRITTE:
[Konkrete Handlung mit Owner und Datum]

VERTRAULICH — MANDATSGEHEIMNIS (§ 43a BRAO)
```

## Rote Schwellen

- Akte ohne Versions-Disziplin → Unterschiede zwischen FINAL und EXECUTION unklar; Signing-Risiko
- Aufbewahrungsfrist unterschaetzt → § 199 BGB Warranty-Verjährung; nach 2-3 Jahren bereits Ansprueche
- Zugriffsrechte nicht gesetzt → Insider-Log-Verletzung; Vertraulichkeitsbruch
- GoBD-Archivierung nicht revisionssicher → steuerliche Pruefung scheitert

## Quellen

- § 50 BRAO; §§ 257 f. HGB; § 147 AO; § 199 BGB; GoBD
- BGH II ZR 289/17 (Dokumentationspflicht); BGH IX ZR 101/17 (§ 50 BRAO Herausgabe)
- Henssler/Pruestell BRAO § 50
