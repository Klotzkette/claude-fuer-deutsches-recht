---
name: gesellschaftsgruender-gruender-intake
description: "Ersterfassung des Gruendungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschaeftszweck. Normen: GmbHG, AktG, HGB. Pruefraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output: Gruendungsintake-Bogen. Abgrenzung: nicht detaillierte Rechtsformberatung (eigener Skill)."
---

# Gründer-Intake

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

- BGH, Urt. v. 25.09.2017 - II ZR 174/16, NJW 2018, 298 Rn. 14 — Stimmbindungsvertrag (SHA): wirkt nur schuldrechtlich zwischen den Parteien; kein dinglicher Effekt auf GmbH-Beschlüsse; erzwingbar nur durch Schadensersatz oder einstweilige Verfügung.
- BGH, Urt. v. 19.09.2005 - II ZR 173/04, BGHZ 164, 107 — Bad-Leaver-Einziehung: sachliche Rechtfertigung erforderlich; willkürliche Hinauskündigungsklauseln unwirksam.
- BGH, Urt. v. 11.02.2008 - II ZR 171/06, NJW 2008, 1589 — Vorbelastungshaftung: Holding-GmbH als Gesellschafterin haftet anteilig; Holding muss vor HR-Eintragung zahlungsfähig sein.
- OLG München, Urt. v. 25.10.2017 - 7 U 2378/17, NZG 2018, 224 — Cap Table Streit: fehlerhafte Gesellschafterliste im HR kann Dritterwerb von Anteilen blockieren (§ 16 GmbHG).

## Kommentarliteratur

- Scholz/Winter, GmbHG, § 15 Rn. 1-30 (Abtretung Geschäftsanteile, Vesting)
- Lutter/Hommelhoff, GmbHG, § 34 Rn. 1-25 (Einziehung, Bad-Leaver)
- Baumbach/Hueck, GmbHG, § 47 Rn. 1-20 (Stimmrecht, Stimmbindung)

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
5. **Routenliste** — welche Spezialskills sollen als nächstes laufen.
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
| 1  | [Name] | [Adr.] | [EUR] | [%] | Persönlich / Holding | Bar |

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
| 1  | [Punkt] | [Name] | [Datum] | [Stufe] |
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
- BGH II ZR 174/16, NJW 2018, 298 (Stimmbindung)
- BGH II ZR 173/04, BGHZ 164, 107 (Bad-Leaver)
- Scholz/Winter, GmbHG, § 15 Rn. 1-30

## Übergabe an andere Skills

- `gesellschaftsgruender-kommandocenter` — Master-Workflow nach Intake
- `gesellschaftsgruender-cap-table` — Cap Table aufbauen
- `gesellschaftsgruender-firmenname-pruefung` — Firmencheck
- `gesellschaftsgruender-rechtsformwahl` — falls Rechtsform noch offen
- `gesellschaftsgruender-share-classes-a-b-c` — bei Class-Shares
