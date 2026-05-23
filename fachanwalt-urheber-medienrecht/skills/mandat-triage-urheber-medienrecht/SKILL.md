---
name: mandat-triage-urheber-medienrecht
description: Strukturierte Eingangs-Abfrage fuer urheber- und medienrechtliche Mandate. Klaert Sachgebiet (Urheberrecht inkl. Filesharing Foto-Lizenz Software-Lizenz Persoenlichkeitsrecht Presserecht Aeusserungsrecht KUG Recht am eigenen Bild Rundfunk Streaming Plattformhaftung DSA DDG Verlags- und Buchrecht Filmrecht Musikrecht GEMA VG WORT VG BildKunst) Mandantenrolle (Urheber Werknutzer Plattform Verlag Medienhaus Privatperson Betroffener) Sofort-Fristen Abmahnungsfrist Gegendarstellung Frist § 11 LPG. Eskalation Telefon-Sofort bei einstweiliger Verfuegung. Routing zu urheber-abmahnung-pruefen.
---

# Mandat-Triage Urheber- und Medienrecht

## Zweck

Medien- und Urheberrecht spaltet sich auf — Urheberrecht (Werknutzung) vs. Persönlichkeitsrecht (Ehre Privatsphäre Bild) vs. Presserecht (Berichterstattung) vs. Internet-Plattformen (DSA DDG). Triage ordnet zu.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Urheber / Schöpfer
- Lizenz-Inhaber / Verwerter / Verlag
- Werknutzer ohne Lizenz (Beklagter)
- Persönlichkeitsrechts-Betroffener (Foto Aussage Privatsphäre)
- Medienhaus / Verlag / Sender (Beklagter Berichterstattung)
- Plattform-Betreiber (Hosting Provider)
- Filesharing-Beschuldigter

### Frage 2 — Sachgebiet?

- Urheberrecht Werknutzung
- Filesharing
- Foto-/Software-Lizenz
- Verlags- und Buchrecht (Verlagsvertrag)
- Musikrecht (GEMA Tantiemen Tonträger)
- Filmrecht (Produktion Verleih Streaming)
- Persönlichkeitsrecht (KUG Recht am eigenen Bild §§ 22 23 KUG; Ehrenschutz § 823 BGB iVm Art. 1 Art. 2 GG)
- Presserecht (Berichterstattung Pressestrafrecht)
- Rundfunk Streaming Plattform
- DSA DDG Plattformhaftung
- Verwertungsgesellschaften
- Datenschutz medial

### Frage 3 — Akute Eilbedürftigkeit?

- Einstweilige Verfügung droht / wurde erlassen
- Berichterstattung in zwei Tagen — Verbot dringend
- Filesharing-Abmahnung mit Frist Tage
- DSA-Anordnung Behörde
- Bild im Netz dringend zu löschen

### Frage 4 — Stand?

- Beratungsbedarf vor Klage (Lizenzgestaltung Verlagsvertrag)
- Außergerichtliche Abmahnung erhalten
- Außergerichtliche Abmahnung gegen Dritten geplant
- Einstweilige Verfügung beantragt / erhalten
- Hauptsacheverfahren
- Berufung Revision
- Verfassungsbeschwerde Meinungsfreiheit

### Frage 5 — Verletzungshandlung?

- Bei Urheberrecht Werk Verletzungs-URL Datum
- Bei KUG Foto wo veröffentlicht
- Bei Aussage Wortlaut Kontext
- Bei Filesharing IP-Adresse und Datum

### Frage 6 — Frist?

- **Urheberrechtliche Verjährung** drei / zehn Jahre § 195 199 BGB § 102 UrhG
- **Gegendarstellung** je nach LPG (typisch zwei Wochen)
- **Abmahnungsfrist** wie gesetzt
- **Einstweilige Verfügung** Dringlichkeit ein Monat ab Kenntnis (Münchener Rechtsprechung)
- **Hauptsacheklage nach EV** § 926 ZPO Aufforderung
- **DSA-Beschwerde Art. 16 DSA** (NetzDG aufgehoben 14.05.2024)

### Frage 7 — Wirtschaftliche Verhältnisse?

- Berufshaftpflicht Medienhaus
- Rechtsschutz Versicherung
- Streitwert hoch bei Boulevard-Verleger
- Bei Privat-Filesharing typisch EUR 1000 nach § 97a Abs. 3 UrhG

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Urheber-Abmahnung Verteidigung | `urheber-abmahnung-pruefen` |
| Urheber-Anspruch Aktivseite | `urheber-abmahnung-pruefen` (Aktivlegitimation) |
| Foto-Lizenz Streit | `urheber-abmahnung-pruefen` plus MFM-Diskussion |
| Software-Lizenz Open-Source-Compliance | weiter an `gewerblicher-rechtsschutz` Skill `open-source-pruefung` |
| Persönlichkeitsrecht / KUG | (Skill kug-aeusserungsrecht — perspektivisch) |
| Presserecht Gegendarstellung | (Skill gegendarstellung — perspektivisch) |
| Plattform DSA DDG | (Skill plattform-haftung — perspektivisch) |
| Verlagsvertrag-Beratung | (Skill verlagsvertrag — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — bei Medienhaus / Berichterstatter-Konstellation streng
- **Streitwert** Persönlichkeitsrecht bei Boulevard hoch EUR 30000 plus
- **Rechtsschutz-Deckung** bei Privat-Filesharing prüfen
- **Komplexität** bei Verlagsvertrag und Lizenzketten

## Eskalation

- **Telefon-Sofort** Einstweilige Verfügung erlassen
- **Binnen einer Stunde** Berichterstattung in zwei Tagen — Verbot
- **Heute** Schutzschrift Gegendarstellungs-Verlangen Abmahnungs-Antwort
- **Diese Woche** Klage-Erstentwurf Verlagsvertrag-Entwurf

## Ausgabe

- `triage-protokoll-urheber-medien.md`
- Aktenanlage
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill
- Bei Eilfall Antrag oder Schutzschrift-Entwurf

## Quellen

- UrhG §§ 1 ff. 97 97a 102
- KUG §§ 22 23
- BGB §§ 823 1004
- LPG (jeweils landesrechtlich)
- DSA DDG (DDG seit 14.05.2024 ersetzt TMG; NetzDG aufgehoben)
- BGH I. Zivilsenat VI. Zivilsenat
- Schricker/Loewenheim UrhG
- Soehring/Hoehne Presserecht
