---
name: gruender-intake
description: "Ersterfassung des Gründungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschäftszweck. Normen: GmbHG, AktG, HGB. Prüfraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output: Gründungsintake-Bogen. Abgrenzung: nicht detaillierte Rechtsformberatung (eigener Skill) im Gesellschaftsgruender."
---

# Gründer-Intake

## Aktenstart statt Formularstart

Wenn zu **Gruender Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gesellschaftsgruender** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gründer-Intake` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor der strukturierten Abfrage

1. Ist die Rechtsform bereits entschieden oder noch offen? Wenn offen: zunächst `gesellschaftsgruender-rechtsformwahl` aufrufen.
2. Liegen bereits ein Term Sheet oder ein Investor-Letter of Intent vor?
3. Sind alle Gründer natürliche Personen, oder hält mindestens einer über eine Holding-GmbH?
4. Gibt es genehmigungspflichtige Tätigkeiten (BaFin, Glücksspiel, Apotheke, Bewachung)?
5. Ist der Gründungstermin zeitkritisch (< 4 Wochen)?

## Zentrale Normen

- **§§ 2, 5 GmbHG** — Beurkundungspflicht; Stammkapital; Mindestanteil 1 EUR.
- **§ 8b Abs. 2 KStG** — Steuerfreier Exit über Holding-GmbH (95 % Steuerfreiheit); Holding vor operativer GmbH gründen.
- **§ 47 GmbHG** — Stimmrecht: Stimmbindungsvereinbarungen möglich (SHA), aber nur schuldrechtliche Wirkung.
- **§§ 34, 15 GmbHG** — Einziehung von Geschäftsanteilen (Vesting / Bad-Leaver).
- **§ 19 GwG** — Transparenzregister: wirtschaftlich Berechtigte melden.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Frageleitfaden (9 Blöcke)

### Block 1 — Gründer

- Anzahl Gründer (natürliche Personen)?
- Pro Gründer: Vollständiger Name, Geburtsdatum, Anschrift, Staatsangehörigkeit.
- Funktion in der Gesellschaft (CEO, CTO, COO, nur Investor)?
- Persönliches Halten oder über Holding-GmbH?
 - Holding bereits gegründet? Falls nein: vor operativer GmbH gründen (§ 8b KStG-Vorteil).
- Ausländische Gesellschafter → Sanktionsrecht prüfen, GwG-Identifikation.

### Block 2 — Anteilsverteilung

- Stammkapital gesamt (GmbH: Minimum 25.000 EUR; UG: Minimum 1 EUR)?
- Pro Gründer: Anteil in EUR und in Prozent.
- 50/50-Struktur: Patt-Risiko bei Streit → entweder 51/49 oder Dead-Lock-Klausel in SHA.
- Class-Shares (A/B/C) jetzt oder erst nach Investor-Runde?

### Block 3 — Investor-Roadmap

- Pre-Money-Bewertung geplant?
- Finanzierungsrunden: Seed, Series A, ...?
- Bestehendes Term Sheet?
- Genehmigtes Kapital (§ 55a GmbHG) vorsehen?
- Vesting für Gründer: Cliff 12 Monate Standard, Vesting 4 Jahre?

### Block 4 — Geschäftsmodell

- Branche, B2B/B2C, internationale Tätigkeit.
- Lizenz-/Genehmigungspflicht?
- Reputationsbedürfnis (UG vs. GmbH)?

### Block 5 — Firma und Sitz

- Wunschfirma (inkl. Rechtsformzusatz).
- Alternativfirmen falls Beanstandung.
- Sitz (Stadt), Geschäftsadresse.
- Domain gesichert? Markensuche DPMA durchgeführt?

### Block 6 — Geschäftsführung

- Anzahl GF; Gesellschafter-GF oder Fremd-GF?
- Einzel- oder Gesamtvertretung?
- § 181 BGB Befreiung gewünscht?
- SV-Status klären → `gesellschaftsgruender-gf-sozialversicherungs-status`.
- Anstellungsvertrag: Gehalt, Wettbewerbsverbot, Karenz?

### Block 7 — SHA / Gesellschaftervereinbarung

- Vesting / Leaver-Regelungen (Good/Bad)?
- Vorkaufsrechte, Drag-Along, Tag-Along?
- Konsortialabrede / Stimmbindung?

### Block 8 — Beirat / Advisory Board

- Beirat geplant → `gesellschaftsgruender-beirat-advisory-board`?
- Aufgaben, Mitgliederzahl, Vergütung?

### Block 9 — Spezialthemen

- Golden Share / StaRUG-Vetorecht → `gesellschaftsgruender-golden-share-und-vetorechte`?
- Bilinguale Dokumente Deutsch/Englisch?
- gGmbH (gemeinnützig)?

## Schritt-für-Schritt-Workflow

1. **Triage** — 5 Triage-Fragen beantworten; Rechtsform klären.
2. **Blöcke 1-9 abarbeiten** — systematisch alle Daten abfragen; offene Punkte als TODO kennzeichnen.
3. **Datenblatt erstellen** — alle Eckdaten strukturiert zusammenstellen (siehe Output-Template).
4. **Cap Table initial** — Anteile, Quoten, Holding-Struktur → `gesellschaftsgruender-cap-table`.
5. **Routenliste** — welche Fachmodule sollen als nächstes laufen.
6. **Fristen-Vorschau** — Notartermin, Stammkapital-Einzahlung, Behörden-Fristen.
7. **Stoppschilder identifizieren** — wann ist zwingend Anwalt/Steuerberater/Notar erforderlich.

## Output-Template Datenblatt Gründung

**Adressat:** Internes Dossier / Notar-Vorbereitung — Tonfall sachlich-präzise
```
DATENBLATT GRÜNDUNG
Erstellt: [Datum]
Mandant/Gründer: [Name(n)]

GESELLSCHAFT
Rechtsform: [GmbH / UG / KG / etc.]
Firma (geplant): [Firmenname + Rechtsformzusatz]
Sitz: [Stadt]
Geschäftsadresse: [Adresse]
Unternehmensgegenstand: [Wortlaut]
Stammkapital: [EUR]

GESELLSCHAFTER
| Nr. | Name | Anschrift | Anteil EUR | Quote % | Halten über | Einzahlung |
|----|------|---------|-----------|---------|------------|-----------|
| 1 | [Name] | [Adr.] | [EUR] | [%] | Persönlich / Holding | Bar |

GESCHÄFTSFÜHRUNG
| GF | Gesellschafter? | Vertretung | § 181 befreit | SV-Status |
|----|----------------|-----------|--------------|----------|
| [Name] | Ja/Nein | Einzel/Gesamt | Ja/Nein | Prüfung ausstehend |

INVESTOR-ROADMAP
Erste Finanzierungsrunde: [Seed / Series A / noch offen]
Pre-Money-Bewertung geplant: [EUR oder "offen"]
Term Sheet vorhanden: [Ja / Nein]
Genehmigtes Kapital (§ 55a GmbHG): [vorsehen / nicht erforderlich]

ROUTENLISTE (nächste Skills)
[ ] `gesellschaftsgruender-firmenname-pruefung` — Firmencheck
[ ] `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Satzung
[ ] `gesellschaftsgruender-gesellschaftervereinbarung` — SHA
[ ] `gesellschaftsgruender-geschaeftsfuehrervertrag` — GF-Anstellungsvertrag
[ ] `gesellschaftsgruender-notar-vorbereitung` — Notarsitzung
[ ] `gesellschaftsgruender-cap-table` — Cap Table aufbauen

OFFENE PUNKTE / STOPPSCHILDER
| Nr. | Punkt | Owner | Frist | Eskalation |
|----|-------|-------|-------|------------|
| 1 | [Punkt] | [Name] | [Datum] | [Stufe] |
```

## Rote Schwellen

- Holding-GmbH nicht vor operativer GmbH gegründet → § 8b KStG-Vorteil geht verloren; teurer Fehler.
- 50/50-Gesellschafterstruktur ohne Dead-Lock-Regelung → Pattrisiko; dringend SHA mit Stichentscheid oder Mediationsklausel.
- Ausländischer Gesellschafter aus Sanktionsland → GwG-Prüfung; FDI-Prüfung ggf. erforderlich.
- Genehmigungspflichtiger Gegenstand nicht identifiziert → Eintragung scheitert; Haftungsrisiko.
- Sacheinlage ohne Werthaltigkeitsprüfung → Differenzhaftung (§ 9 GmbHG).

## Quellen und Vertiefung

- §§ 2, 5, 15, 34, 47 GmbHG (Grundlagen Gründung und Anteilsstruktur)
- § 8b KStG (steuerlicher Holding-Vorteil)
- § 19 GwG (Transparenzregister)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Winter, GmbHG, § 15 Rn. 1-30

## Übergabe an andere Skills

- `gesellschaftsgruender-kommandocenter` — Master-nach Intake
- `gesellschaftsgruender-cap-table` — Cap Table aufbauen
- `gesellschaftsgruender-firmenname-pruefung` — Firmencheck
- `gesellschaftsgruender-rechtsformwahl` — falls Rechtsform noch offen
- `gesellschaftsgruender-share-classes-a-b-c` — bei Class-Shares

