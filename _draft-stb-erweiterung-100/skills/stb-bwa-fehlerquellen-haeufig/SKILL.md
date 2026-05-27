---
name: stb-bwa-fehlerquellen-haeufig
description: "Typische Fehlerquellen in der BWA. Anwendungsfall Qualitaetspruefung BWA durch Berufstraeger interne Stichprobe Fehler in Periodenabgrenzung Buchungsfehler Bestandsveraenderung Lohnbuchungen. Methodik Checkliste Plausibilitaetspruefung. Output Fehlerprotokoll Korrekturmassnahmen Schulungsbedarf Querverweis stb-bwa-aufbau-grundlagen."
---

# Typische BWA-Fehlerquellen und Plausibilitaetspruefung

## Kernsachverhalt

BWA-Fehler sind nicht nur Schoenheitsmaengel — sie verfaelschen die Steuerung, koennen Krisensignale verdecken und im Streit mit dem Mandanten haftungsrelevant werden. Der Steuerberater muss systematisch die typischen Fehlerquellen abpruefen, bevor die BWA versendet wird. Dieser Skill ist Pflicht-Checkliste fuer Sachbearbeiter und Berufstraeger.

## Kaltstart-Rueckfragen

1. Wer hat die BWA erstellt — interner Sachbearbeiter, ausgelagerte Buchhaltung, automatisch?
2. Welches Buchhaltungs-System — DATEV, Addison, Sage, BuchhaltungsButler?
3. Sind Lohnbuchungen aus separatem Lohnprogramm integriert?
4. Wurde eine OPOS-Pflege vor BWA-Erstellung durchgefuehrt?
5. Liegt eine Zwischeninventur oder Warenroll vor?
6. Hat sich am Kontenrahmen oder an der BWA-Konfiguration etwas geaendert?
7. Welche Periode wird ausgewertet — Monat, Quartal, kumuliert?
8. Gibt es Sondereffekte, die separat ausgewiesen werden sollten?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — ordnungsgemaesse Buchfuehrung.

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit, Richtigkeit.

**§ 257 HGB / § 147 AO** — Aufbewahrung.

**§ 33 StBerG** — StB-Aufgabenkreis; Sorgfaltspflicht.

**§ 57 StBerG** — Gewissenhaftigkeit.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480 (Erstellung).
- BGH IX ZR 285/14 — Hinweispflicht bei erkannten Buchhaltungsfehlern.

## Workflow

### Phase 1 — Konsistenzpruefung BWA gegen SuSa

- BWA-Endsalden Erfolgskonten = SuSa-Salden? (Differenz = Fehler.)
- BWA-Block-Summen = Kontensummen? (Konfigurationsfehler bei BWA-Form?)
- Bestaendsveraenderung in BWA = Anfangs-/Endbestand-Differenz aus SuSa?

### Phase 2 — Typische Fehlerklassen

| Fehlerklasse | Symptom | Ursache | Korrektur |
|---|---|---|---|
| Periodenabgrenzung fehlt | Sprunghafte Aufwendungen | RAP nicht gebucht | RAP nachbuchen |
| Bestandsveraenderung falsch | Wareneinsatz unplausibel | Inventur fehlt, Schaetzung schlecht | Zwischeninventur oder Warenroll |
| Lohnbuchungen verzoegert | Personalkosten zu niedrig | Lohnprogramm nicht synchron | Buchung aus Lohnprogramm uebernehmen |
| Verrechnungskonto offen | Saldo > 0 in 1590/1599 | Buchung nicht zugeordnet | Klaerung mit Mandant |
| USt-Voranmeldung uneinheitlich | USt-Konto-Saldo passt nicht | USt-Schluessel falsch | Buchung pruefen |
| Sonderzahlungen Personal | Monatsausschlag Lohn | Tantieme einmalig | Im Erlaeuterungstext erwaehnen |
| Abschreibungen nicht aktualisiert | AfA monatlich konstant trotz Investition | Anlagenbuchhaltung nicht synchron | AfA aktualisieren |
| Skonti-Buchung | Erloese zu hoch | Skonti nicht erloesschmaelernd gebucht | Konto 8730/4730 nutzen |
| Provisionserloese | DB falsch | Aufwand statt Erloesschmaelerung | Buchung umstellen |

### Phase 3 — Plausibilitaetsquoten

| Quote | Branchentypisch | Auffaellig wenn |
|---|---|---|
| Materialquote Industrie | 30-50 Prozent | < 25 oder > 60 Prozent |
| Materialquote Handel | 60-80 Prozent | < 50 oder > 90 Prozent |
| Personalkostenquote DL | 35-55 Prozent | < 25 oder > 70 Prozent |
| Mietquote | 3-10 Prozent | > 15 Prozent |
| Kfz-Kosten | 1-5 Prozent | > 10 Prozent (Privatanteil pruefen) |
| Versicherungen | 0,5-2 Prozent | > 3 Prozent (Doppelbuchung) |

### Phase 4 — Lohnbuchungs-Konsistenz

- Lohnsumme BWA = Bruttolohn Lohnprogramm (Konto 4120/4130 oder 6020/6030).
- SV-AG-Anteil Konto = Konto Lohnabrechnung (durchschnittlich rund 21 Prozent vom Brutto).
- Berufsgenossenschaft monatlich anteilig gebucht (Konto 4140/6140).
- Pauschalsteuer Aushilfen Konto 4148/6148 oder vergleichbar.

### Phase 5 — Spezial-Pruefungen

- Bei GmbH: Geschaeftsfuehrer-Gehalt vollstaendig erfasst? Verdeckte Gewinnausschuettung-Risiko?
- Bei Holding: Erloese aus Beteiligung sauber erfasst (steuerfrei nach § 8b KStG)?
- Bei Personenunternehmen: Privatentnahmen nicht in BWA, sondern in Kapitalkonto.
- USt-konsistenz mit USt-Voranmeldung.

### Phase 6 — Fehlerprotokoll und Korrektur

- Fehlerliste mit Datum, Konto, Buchungssatz, Korrektur.
- Korrektur-Buchung mit Verweis im Buchungstext (z.B. "Korrektur BWA-Pruefung Q2/2026").
- Bei wesentlichen Fehlern: BWA neu erstellen und versenden.
- Mandant informieren bei Auswirkungen auf vorgelegte Reports.

## Output

- Fehlerprotokoll mit Korrekturmassnahmen.
- Korrigierte BWA.
- Ggf. Schulungsmemo fuer Sachbearbeiter.

## Strategie und Praxis-Tipps

- Standardisierte Pruefliste vor jedem BWA-Versand abarbeiten — auch bei Routine-Mandanten.
- 4-Augen-Prinzip: Sachbearbeiter prueft selbst, Berufstraeger stichprobenartig.
- Bei wiederholten Fehlern beim gleichen Sachbearbeiter: Schulung erforderlich.
- DATEV-Tipp: Auswertung "Konten mit ungewoehnlichem Saldo" als monatliche Pflichtpruefung.
- Honoraranknuepfung: Fehlerprotokoll als Teil der Qualitaetssicherung, kein Extra-Honorar.
- Bei Buchungsfehlern aus Vorperiode: Vorperiode korrigieren oder Erlaeuterungstext mit Hinweis.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-monatsabschluss-routine` — Monatsabschluss.
- `stb-susa-formfehler-pruefen` — SuSa-Fehler.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 257.
- AO §§ 146, 147.
- StBerG §§ 33, 57.
- BMF v. 28.11.2019 zu GoBD.
- BGH IX ZR 285/14, NJW 2017, 1611.
