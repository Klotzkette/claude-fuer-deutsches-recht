---
name: bwa-fehlerquellen-haeufig
description: "Typische Fehlerquellen in der BWA. Anwendungsfall Qualitaetsprüfung BWA durch Berufstraeger interne Stichprobe Fehler in Periodenabgrenzung Buchungsfehler Bestandsveraenderung Lohnbuchungen. Methodik Checkliste Plausibilitaetsprüfung. Output Fehlerprotokoll Korrekturmassnahmen Schulungsbedarf Que..."
---

# Typische BWA-Fehlerquellen und Plausibilitaetspruefung

## Fachlicher Anker

- **Normen:** § 6a, § 238 HGB, § 146 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

BWA-Fehler sind nicht nur Schoenheitsmaengel — sie verfaelschen die Steuerung, können Krisensignale verdecken und im Streit mit dem Mandanten haftungsrelevant werden. Der Steuerberater muss systematisch die typischen Fehlerquellen abpruefen, bevor die BWA versendet wird. Dieser Skill ist Pflicht-Checkliste für Sachbearbeiter und Berufstraeger.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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
| Verrechnungskonto offen | Saldo nicht null im Verrechnungs-/Geldtransit-Konto (z. B. SKR 03 1590/1599) | Buchung nicht zugeordnet | Klärung mit Mandant; Kontonummer in DATEV-Kontenrahmen SKR 03/04 prüfen (DATEV-Kontenrahmen jaehrlich aktualisiert) |
| USt-Voranmeldung uneinheitlich | USt-Konto-Saldo passt nicht | USt-Schlüssel falsch | Buchung prüfen |
| Sonderzahlungen Personal | Monatsausschlag Lohn | Tantieme einmalig | Im Erläuterungstext erwaehnen |
| Abschreibungen nicht aktualisiert | AfA monatlich konstant trotz Investition | Anlagenbuchhaltung nicht synchron | AfA aktualisieren |
| Skonti-Buchung | Erloese zu hoch | Skonti nicht erloesschmaelernd gebucht | Erloesschmaelerung im richtigen Erloeskontenbereich (vgl. DATEV-Kontenrahmen aktuelle Fassung, SKR 03 typisch 8730er bzw. SKR 04 4730er-Bereich) |
| Provisionserloese | DB falsch | Aufwand statt Erloesschmaelerung | Buchung umstellen |

### Phase 3 — Plausibilitaetsquoten

| Quote | Branchentypisch | Auffaellig wenn |
|---|---|---|
| Materialquote Industrie | 30-50 Prozent | < 25 oder > 60 Prozent |
| Materialquote Handel | 60-80 Prozent | < 50 oder > 90 Prozent |
| Personalkostenquote DL | 35-55 Prozent | < 25 oder > 70 Prozent |
| Mietquote | 3-10 Prozent | > 15 Prozent |
| Kfz-Kosten | 1-5 Prozent | > 10 Prozent (Privatanteil prüfen) |
| Versicherungen | 0,5-2 Prozent | > 3 Prozent (Doppelbuchung) |

### Phase 4 — Lohnbuchungs-Konsistenz

- Lohnsumme BWA muss mit dem Bruttolohn aus dem Lohnprogramm uebereinstimmen (Konten Loehne/Gehaelter SKR 03 4120/4130 bzw. SKR 04 6020/6030 — DATEV-Kontenrahmen aktuelle Fassung).
- SV-AG-Anteil-Konto-Saldo gegen den AG-Anteil aus der Lohnabrechnung prüfen (Daumenregel: ca. 20-21 Prozent vom Bruttolohn; massgebliche Beitragssaetze KV 14,6 Prozent allgemein (Stand 2025), RV 18,6 Prozent, PV 3,6 Prozent, AV 2,6 Prozent — aktuelle Werte aus der Sozialversicherungs-Rechengroessenverordnung abrufen).
- Berufsgenossenschaft monatlich anteilig gebucht (Konto SKR 03 4140 bzw. SKR 04 6140 — Konkretisierung im aktuellen DATEV-Kontenrahmen prüfen).
- Pauschalsteuer für Aushilfen über das jeweils passende Steueraufwandskonto buchen (z. B. SKR 03 4148 für Lohnsteuer 2 Prozent Pauschal — konkrete Kontonummer in der aktuellen DATEV-Kontenrahmen-Dokumentation nachschlagen).

### Phase 5 — Spezial-Prüfungen

- Bei GmbH: Geschäftsführer-Gehalt vollstaendig erfasst? Verdeckte Gewinnausschuettung-Risiko?
- Bei Holding: Erloese aus Beteiligung sauber erfasst (steuerfrei nach § 8b KStG)?
- Bei Personenunternehmen: Privatentnahmen nicht in BWA, sondern in Kapitalkonto.
- USt-konsistenz mit USt-Voranmeldung.

### Phase 6 — Fehlerprotokoll und Korrektur

- Fehlerliste mit Datum, Konto, Buchungssatz, Korrektur.
- Korrektur-Buchung mit Verweis im Buchungstext (z.B. "Korrektur BWA-Prüfung Q2/2026").
- Bei wesentlichen Fehlern: BWA neu erstellen und versenden.
- Mandant informieren bei Auswirkungen auf vorgelegte Reports.

## Strategie und Praxis-Tipps

- Standardisierte Prüfliste vor jedem BWA-Versand abarbeiten — auch bei Routine-Mandanten.
- 4-Augen-Prinzip: Sachbearbeiter prüft selbst, Berufstraeger stichprobenartig.
- Bei wiederholten Fehlern beim gleichen Sachbearbeiter: Schulung erforderlich.
- DATEV-Tipp: Auswertung "Konten mit ungewoehnlichem Saldo" als monatliche Pflichtpruefung.
- Honoraranknuepfung: Fehlerprotokoll als Teil der Qualitaetssicherung, kein Extra-Honorar.
- Bei Buchungsfehlern aus Vorperiode: Vorperiode korrigieren oder Erläuterungstext mit Hinweis.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 257.
- AO §§ 146, 147.
- StBerG §§ 33, 57.
- BMF v. 28.11.2019 zu GoBD.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 1 bestaetigt (SV-Beitragssaetze Stand 2025 eingesetzt), 2 ersetzt (DATEV-Kontonummern-Hinweise ohne Marker neu formuliert) -->
