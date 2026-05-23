---
name: mandat-triage-verwaltungsrecht
description: Strukturierte Eingangs-Abfrage fuer verwaltungsrechtliche Mandate. Klaert Sachgebiet (Bauen Gewerbe Polizei Beamtenrecht Schule Hochschule Subventionen Sozialleistungen Auslaender Asyl Steuerrecht) Behoerdenebene (Bund Land Kommune) Stand des Verfahrens (Antrag Anhoerung Bescheid Widerspruch Klage Eilantrag) Frist-Sofort-Check (Widerspruch ein Monat § 70 VwGO Klage ein Monat § 74 VwGO Untaetigkeitsklage drei Monate § 75 VwGO). Eskalation Telefon-Sofort bei sofortiger Vollziehung drohendem Vollzug. Routing zu widerspruch-oder-klage-erstpruefung.
---

# Mandat-Triage Verwaltungsrecht

## Zweck

Verwaltungsrecht ist hochheterogen — vom Bauantrag bis zur Asylklage. Triage ordnet das Mandat dem richtigen Sachgebiet und dem richtigen Verfahrensschritt zu.

## Ablauf — sieben Fragen

### Frage 1 — Wer und für wen?

- Bürger gegen Behörde
- Unternehmen gegen Behörde
- Behörde (selten — vertretbar nur unter strikter Trennung)
- Verband-Klagebefugnis

### Frage 2 — Sachgebiet?

- **Bau- und Planungsrecht** Baugenehmigung Nachbarklage Bebauungsplan
- **Gewerberecht** Gewerbeerlaubnis Untersagung Gaststätte Spielhalle
- **Polizei- und Ordnungsrecht** polizeiliche Maßnahme Versammlungsrecht
- **Beamten- und Soldatenrecht** Disziplinar Beurteilung Konkurrentenklage
- **Schule und Hochschule** Versetzung Abitur Zulassung
- **Subventionsrecht** Förderbescheid Rückforderung
- **Asyl- und Ausländerrecht** (an `fachanwalt-migrationsrecht` weiter)
- **Sozialrecht** (an `sozialrecht-kanzlei` weiter)
- **Steuerrecht** (an `steuerrecht-kanzlei` weiter)
- **Vergaberecht** (an `fachanwalt-vergaberecht` weiter)
- **Umweltrecht**
- **Versammlungsrecht**
- **Kommunalrecht**

### Frage 3 — Akute Eilbedürftigkeit?

- Sofortige Vollziehung angeordnet
- Vollzug innerhalb Tage angekündigt
- Demonstrationsverbot ein-Tages-Vorlauf
- Räumung droht
- Untersagung erteilt — Geschäftsstillstand
- Bauleitplan-Aufstellung in der Beschlussphase

### Frage 4 — Stand?

- Vor Antragstellung (Beratung)
- Antrag eingereicht — wartet auf Bescheid
- Anhörung läuft § 28 VwVfG
- Bescheid liegt vor (Datum)
- Widerspruchsverfahren läuft
- Klage erhoben (Az VG)
- Berufung / Revision (OVG BVerwG)
- Verfassungsbeschwerde

### Frage 5 — Behörde?

- Bundesbehörde (z.B. BAMF Bundespolizei BfArM)
- Landesbehörde (z.B. Bezirksregierung Landratsamt)
- Kommunalbehörde
- Sondereinrichtung Anstalt öffentlichen Rechts

### Frage 6 — Frist?

- **Widerspruch** ein Monat § 70 VwGO; Bekanntgabe-Fiktion § 41 Abs. 2 VwVfG vier Tage seit 01.01.2025 (PostModG)
- **Klage** ein Monat § 74 VwGO ab Bekanntgabe Widerspruchsbescheid
- **Untätigkeitsklage** § 75 VwGO nach drei Monaten ohne Bescheid
- **Verfassungsbeschwerde** ein Monat § 93 BVerfGG
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr § 58 Abs. 2 VwGO

### Frage 7 — Wirtschaftliche Verhältnisse PKH?

- Prozesskostenhilfe § 166 VwGO iVm §§ 114 ff. ZPO
- Beratungshilfe für außergerichtlich

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Baugenehmigung Nachbarklage | (Skill bau-nachbarklage — perspektivisch) |
| Bauliche Untersagung | `widerspruch-oder-klage-erstpruefung` |
| Gewerbe-Erlaubnis-Streit | `widerspruch-oder-klage-erstpruefung` |
| Beamten-Konkurrentenklage | (Skill konkurrentenklage — perspektivisch) |
| Beurteilung Beamter | (Skill beurteilungsanfechtung — perspektivisch) |
| Schule Versetzung Zulassung | `widerspruch-oder-klage-erstpruefung` |
| Asyl Ausländerrecht | weiter an `mandat-triage-migrationsrecht` |
| Sozialleistung | weiter an `mandat-triage-sozialrecht` |
| Steuerrecht | weiter an `mandat-triage-steuerrecht` |
| Polizei-Maßnahme | (Skill polizei-feststellungs-klage — perspektivisch) |
| Versammlungs-Verbot | `widerspruch-oder-klage-erstpruefung` plus § 80 Abs. 5 VwGO |

## Eilmodus

Bei sofortiger Vollziehung oder akutem Vollzug:

1. Mandantengespräch — Sachverhalt zwanzig Minuten
2. Bescheid einlesen — fünfzehn Minuten
3. Widerspruch einlegen (formloser Schriftsatz) — gleichzeitig
4. Eilantrag § 80 Abs. 5 VwGO oder § 123 VwGO formulieren
5. Bei VG einreichen — Eingang sicherstellen Empfangsbestätigung

## Eskalation

- **Telefon-Sofort** drohender Vollzug binnen Stunden
- **Binnen einer Stunde** Bescheid mit sofortiger Vollziehung
- **Heute** Widerspruchsschrift Eilantrag-Erstentwurf
- **Diese Woche** Klage-Erstentwurf Begründung

## Ausgabe

- `triage-protokoll-verwaltungsrecht.md`
- Frist im Fristenbuch
- Bei Eilmodus: Eilantrag-Entwurf im Anhang
- Mandatsvereinbarung mit Streitwertabschätzung § 52 GKG
- Empfehlung Folge-Skill

## Quellen

- VwGO §§ 42 58 68 70 74 75 80 80a 123
- VwVfG §§ 28 35 41
- GKG § 52
- BVerwGE Std.Spruch
- Kopp/Schenke VwGO
