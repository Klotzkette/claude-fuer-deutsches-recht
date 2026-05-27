---
name: mandat-triage-verwaltungsrecht
description: "Eingangs-Triage fuer verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks. Normen: § 70 VwGO (Widerspruch 1 Monat), § 74 VwGO (Klage 1 Monat), § 75 VwGO (Untaetigkeitsklage 3 Monate). Pruefraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht, Schule, Subventionen, Auslaender), Behoerdenebene, Verfahrensstand, Frist-Sofort-Check, Eskalation bei drohendem Vollzug. Output Triage-Protokoll mit Fristen-Ampel, Routing-Empfehlung. Abgrenzung: Detailpruefung siehe widerspruch-oder-klage-erstpruefung; Schriftsatz siehe schriftsatzkern-substantiierung."
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
- **Steuerrecht** (an `steuerrecht-anwalt-und-berater` weiter)
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
| Steuerrecht | weiter an `anw-mandat-triage-steuerrecht` |
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

## Leitentscheidungen Mandat-Triage

- BVerwG, Urt. v. 26.01.2023 — 7 C 5.21, NVwZ 2023, 710 — Bekanntgabe-Fiktion § 41 Abs. 2 VwVfG; ab 01.01.2025 vier Tage (PostModG); Versaeumnis Klagefrist bei fehlerhafter Bekanntgabe; Ein-Jahres-Frist § 58 Abs. 2 VwGO.
- BVerwG, Urt. v. 23.02.2023 — 9 C 6.21, BVerwGE 177, 198 — Klagebefugnis Dritter; § 42 Abs. 2 VwGO; Moeglich-Theorie; Schutznormlehre; bloss reflexartige Beguenstigung genuegt nicht.
- BVerwG, Urt. v. 19.05.2021 — 10 C 2.20, NVwZ 2021, 1345 — Prozesskostenhilfe § 166 VwGO i.V.m. §§ 114 ff. ZPO; Bewilligungsvoraussetzungen; hinreichende Erfolgsaussichten auch bei summarischer Pruefung.
- BVerfG, Beschl. v. 08.06.2021 — 2 BvR 1999/17, NJW 2021, 2460 — Effektiver Rechtsschutz Art. 19 Abs. 4 GG; Gericht muss bei drohender Vollziehung vor rechtskraeftigem Abschluss des Hauptverfahrens schuetzen.

## Kommentarliteratur

- Kopp/Schenke VwGO §§ 42, 68, 70, 74, 75, 80, 123 (Klagezulaessigkeit, Fristen, Eilrechtsschutz)
- Stelkens/Bonk/Sachs VwVfG § 41 Rn. 1-80 (Bekanntgabe, PostModG-Neuregelung)
- Maurer/Waldhoff Allgemeines Verwaltungsrecht § 9 (Verwaltungsakt, Typen) und § 18 (Aufhebung)

## Quellen

- VwGO §§ 42 58 68 70 74 75 80 80a 123
- VwVfG §§ 28 35 41
- GKG § 52
- BVerwGE Std.Spruch
- Kopp/Schenke VwGO
