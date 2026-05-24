---
name: gesellschaftsgruender-gruender-intake
description: "Strukturierte Eingangsabfrage Gruender. Wer sind die Gruender natuerliche Personen Holding-GmbH. Wieviele Anteile pro Gruender absolut und prozentual. Class A B C Shares schon jetzt oder erst nach Seed. Geschaeftsmodell und Investor-Roadmap. Sitz Gegenstand Stammkapital. Mit Frageleitfaden Pflichtdaten optional-Daten Ausgabe-Vorlage Datenbasis fuer alle weiteren Skills."
---

# Gründer-Intake

## Zweck

Strukturierter Eingangs-Workflow, der **alle gründungsrelevanten Daten** abfragt, bevor andere Skills (Satzung, SHA, Cap Table, Notar-Vorbereitung) angestoßen werden. Vermeidet spätere Nacharbeit durch fehlende Eckdaten.

## Frageleitfaden

### Block 1 — Gründer

- Wieviele Gründer (natürliche Personen)?
- Pro Gründer:
  - Vollständiger Name, Geburtsdatum, Anschrift
  - Berufliche Funktion in der Gesellschaft (CEO, CTO, Investor, Stiller etc.)
  - Wird der Gründer **persönlich** halten oder über **Holding-GmbH**?
  - Wenn Holding: existiert sie schon, oder ist sie noch zu gründen?
  - Bei Holding: Steuer-Vorteil Paragraf 8b KStG bei späterem Exit — `gesellschaftsgruender-rechtsformwahl` Falle 6

### Block 2 — Anteilsverteilung

- Stammkapital insgesamt (Mindest 25.000 EUR für GmbH, 1 EUR für UG)
- Pro Gründer:
  - Höhe in EUR
  - Anteil in Prozent
- Schon jetzt **Class-Shares (A/B/C)** oder erst nach Seed-Runde?
  - Empfehlung: bei Solo-/Paar-Gründung erstmal **eine Klasse**, Class-Shares später mit Investor einführen
  - Bei Mehrgründer-Konstellation mit absehbarem Investor: schon Class-Shares vorsehen

### Block 3 — Bewertung und Investor-Roadmap

- Vorgesehene **Pre-Money-Bewertung** in absehbarer Zeit
- **Geplante Finanzierungsrunden** (Seed, Series A, ...)?
- Bereits Term Sheet mit Investor?
- **Genehmigtes Kapital** (Paragraf 55a GmbHG) vorsehen? Erleichtert spätere Runden
- **Vesting** für Gründer? Cliff 12 Monate Standard

### Block 4 — Geschäftsmodell

- Branche
- B2B / B2C
- Internationale Aktivität
- Investoren-Tauglichkeit (Tech, Biotech, Greentech?)
- Reputationsbedürftig (B2B wenig vs. B2C oft)
- Lizenz-/Genehmigungspflicht (BaFin? Glücksspiel? Apotheker? Bewachungsgewerbe?)

### Block 5 — Firma und Sitz

- Wunschfirma (mit Rechtsformzusatz)
- Alternative Firmenvorschlaege für Fall der Beanstandung
- Sitz (Stadt)
- Geschäftsadresse (kann abweichen)
- Domain bereits gesichert? Marken-Suche durchgeführt? → `gesellschaftsgruender-firmenname-pruefung`

### Block 6 — Geschäftsführung

- Wieviele GF?
- Einzel- oder Gesamtvertretung?
- Pro GF: Gesellschafter oder Fremd-GF?
- Sozialversicherungs-Status (Mehrheit / Minderheit / Fremd-GF) — `gesellschaftsgruender-gf-sozialversicherungs-status`
- Anstellungsvertrag — Höhe? Wettbewerbsverbot? Karenz? → `gesellschaftsgruender-geschaeftsfuehrervertrag`

### Block 7 — Gesellschaftervereinbarung (SHA)

- Vesting / Leaver-Regelungen? — `gesellschaftsgruender-gesellschaftervereinbarung`
- Vorkaufsrechte
- Drag-Along / Tag-Along
- Pflicht-Korrespondenz SHA <-> Satzung — `gesellschaftsgruender-sha-satzung-stimmverpflichtung`

### Block 8 — Beirat / Advisory Board

- Beirat vorgesehen? → `gesellschaftsgruender-beirat-advisory-board`
- Wenn ja: wieviele Mitglieder? Aufgaben? Pflicht-Themen?

### Block 9 — Spezial-Themen

- Golden Share / Restrukturierungs-Vetorecht? → `gesellschaftsgruender-golden-share-und-vetorechte`
- Bilinguale Dokumente Deutsch/Englisch? → `gesellschaftsgruender-bilinguale-dokumente`
- gGmbH (gemeinnützig)?

## Ausgabe

Am Ende des Intakes liegt vor:

1. **Datenblatt Gründung** mit allen Eckdaten
2. **Cap Table** (initial) → `gesellschaftsgruender-cap-table`
3. **Routen-Liste**: Welche Skills sollen als nächstes laufen?
4. **Fristen-Vorschau**: Notar-Termin, Stammkapital-Einzahlung, Anmeldung
5. **Stoppschilder-Liste**: Wann zwingend Anwalt / Steuerberater / Notar?

## Typische Stolpersteine im Intake

1. **Anteile ohne Begründung**: 50/50 wirkt fair, ist aber Patt-Risiko -> entweder 51/49 oder asymmetrische A/B
2. **Holding-Frage zu spaet**: Wer Steuer-Vorteil will, muss Holding **vor** der operativen GmbH gründen
3. **Investoren-Roadmap ignoriert**: Class-Shares jetzt vorgesehen erspart spätere Satzungsaenderung
4. **Firmenname nicht geprüft**: oft schon vergeben oder markenrechtlich kollidierend
5. **Vesting vergessen**: Gründer ohne Vesting koennen nach 6 Monaten mit voller Anteilshöhe ausscheiden — Demotivation der Verbleibenden

## Anschluss

- `gesellschaftsgruender-cap-table` — Cap Table erzeugen
- `gesellschaftsgruender-firmenname-pruefung` — Firma prüfen
- `gesellschaftsgruender-rechtsformwahl` — falls Rechtsform offen
- `gesellschaftsgruender-share-classes-a-b-c` — bei Class-Shares
- `gesellschaftsgruender-kommandocenter` — Master-Workflow
