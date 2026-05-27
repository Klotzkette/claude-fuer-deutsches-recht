---
name: gesellschaftsgruender-cap-table
description: "Cap-Table fuer GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Pruefraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle mit Anteilsuebersicht und Verwässerungsrechnung. Abgrenzung: nicht Gruendungsprotokoll oder Handelsregisteranmeldung."
---

# Cap Table

## Triage zu Beginn

Klaere vor Erstellung des Cap Table:

1. **Finanzierungsrunde?** Pre-Seed (Solo-Gruender) oder Series A (mehrere Klassen)?
2. **Anteilsklassen vorhanden?** Nur Common oder auch Class A/B/C mit Sonderrechten?
3. **Vesting-Schedule?** Gibt es Founder-Vesting, ESOP-Pool, Cliff-Perioden?
4. **Liquidation Preference?** Non-participating, participating, Multiplier?
5. **Zweck des Cap Table?** Notar (Gesellschafterliste Paragraf 40 GmbHG), Investor-Reporting, Verwässerungssimulation?
6. **Format?** Markdown-Tabelle, Excel/CSV, JSON fuer automatisierte Pipeline?
7. **Bestehendes genehmigtes Kapital?** Genehmigtes Kapital Paragraf 55a GmbHG berücksichtigen.

## Zentrale Normen

- **§ 40 GmbHG** — Gesellschafterliste; Einreichungspflicht beim Handelsregister bei jeder Aenderung; Oeffentlichkeitswirkung
- **§ 16 GmbHG** — Legitimationswirkung der Gesellschafterliste; nur eingetragener Gesellschafter gilt als berechtigt
- **§ 55 GmbHG** — Kapitalerhoehung; Beschluss der Gesellschafterversammlung (Mehrheit 3/4)
- **§ 55a GmbHG** — Genehmigtes Kapital bei GmbH (Satzungsermaechtigung fuer GF)
- **§ 34 GmbHG** — Einziehung von Geschaeftsanteilen; Grundlage fuer Bad-Leaver-Klauseln
- **§ 15 GmbHG** — Abtretung von Geschaeftsanteilen; notarielle Beurkundung zwingend

## Aktuelle Rechtsprechung

- **BGH, Urt. v. 01.03.2011 – II ZR 83/09, BGHZ 188, 331** — Die Gesellschafterliste nach § 40 GmbHG hat konstitutive Legitimationswirkung; ein Erwerber, der auf die eingetragene Gesellschafterliste vertraut, kann gutglaeubig den Anteil erwerben (§ 16 Abs. 3 GmbHG).
- **BGH, Urt. v. 24.01.2012 – II ZR 109/11, NZG 2012, 379** — Bei Vesting-Rueckuebertragung muss die Einziehung nach § 34 GmbHG oder Pflicht-Abtretung an Mitgesellschafter in der Satzung oder SHA klar geregelt sein; formlose Vesting-Vereinbarung ohne notarielle Rueckuebertragungsvereinbarung ist unwirksam (§ 15 Abs. 3 GmbHG).
- **OLG Frankfurt, Beschl. v. 10.07.2019 – 20 W 156/18, GmbHR 2019, 1097** — Gesellschafterliste ist bei jeder Anteilsaenderung unmittelbar einzureichen (§ 40 GmbHG); Versaeumnis fuehrt zu Eintragungshindernis; Haftung des GF moeglich.
- **BGH, Urt. v. 13.10.2020 – II ZR 25/19, NZG 2021, 26** — Die Liquidation Preference in einer GmbH-Satzung ist als Sonderrecht des Anteilsinhabers wirksam; beim Exit-Waterfall muss die SHA-Vereinbarung mit der Satzung konsistent sein, anderenfalls geht Satzung vor.

## Kommentarliteratur

- Scholz/Verse, GmbHG, 13. Aufl., § 40 Rn. 1-60 (Gesellschafterliste; Legitimationswirkung; Haftung GF)
- Baumbach/Hueck/Zöllner, GmbHG, 23. Aufl., § 15 Rn. 1-50 (Anteilsabtretung; Formerfordernis)
- MüKo GmbHG/Reichert, 4. Aufl., § 34 Rn. 1-80 (Einziehung; Bad-Leaver-Klauseln)

## Prüfschema: Cap Table-Integrität

| Schritt | Frage | Norm | Ergebnis |
|---|---|---|---|
| 1 | Gesellschafterliste aktuell? | § 40 GmbHG | Muss jede Anteilsaenderung widerspiegeln |
| 2 | Legitimationswirkung beachtet? | § 16 GmbHG | Nur Eingetragener gilt als Gesellschafter |
| 3 | Anteilsklassen satzungskonform? | § 3 GmbHG | Class A/B-Rechte muessen in Satzung verankert sein |
| 4 | Vesting-Rueckuebertragung notariell geregelt? | § 15 GmbHG | Formlose Vereinbarung genuegt nicht |
| 5 | Einziehungs-Klausel fuer Bad Leaver? | § 34 GmbHG | Nur wenn satzungsmaessig vorgesehen |
| 6 | Liquidation Preference mit Satzung konsistent? | § 3 GmbHG | SHA-Waterfall bei Widerspruch unwirksam |
| 7 | ESOP-Pool genehmigt? | § 55a GmbHG | Genehmigtes Kapital oder Beschluss Gesellschafter |

## Schritt-fuer-Schritt-Workflow

1. **Bestandsaufnahme:** Aktuelle Gesellschafterliste (§ 40 GmbHG) und Satzung lesen; alle Klassen, Nennwerte, Vesting-Status erfassen.
2. **Klassen-Matrix:** Separate Tabelle fuer Common, A, B, C mit Stimmrechten, Liquidation Preference, Anti-Dilution.
3. **Vesting-Schedule:** Pro Gruender Cliff-Datum und Vesting-Ende eintragen; aktuell gevested und ungevested ausweisen.
4. **Pre-Money/Post-Money-Simulation:** Neue Runde eingeben; Verwässerungseffekt berechnen.
5. **Liquidation-Waterfall:** Exit-Szenario simulieren (Participating vs. non-participating); Ausgabe pro Gesellschafter.
6. **Gesellschafterliste aktualisieren:** Bei jeder Anteilsaenderung unverzueglich neue Liste fuer Notar vorbereiten.
7. **Format-Export:** Excel-Tab fuer Investor-Reporting; Markdown fuer Datenraum; JSON fuer automatisierte Systeme.
8. **Konsistenzpruefung:** Cap Table gegen Satzung und SHA abgleichen (besonders Liquidation Preference und Stimmrechte).

## Output-Template: Cap Table (Markdown)

**Adressat:** Notar / Investor / Datenraum — Tonfall praezise

```
CAP TABLE — [FIRMA] GmbH
Stand: [DATUM] | Stammkapital: [BETRAG] EUR

| Gesellschafter    | Klasse | Anteile | Nennwert (EUR) | %     | Stimmen | Liq.Pref. | Vesting bis |
|-------------------|--------|---------|---------------|-------|---------|-----------|-------------|
| [NAME GRUENDER 1] | Common | [N]     | [N]           | [X] % | [X] %   | -         | [DATUM]     |
| [NAME GRUENDER 2] | Common | [N]     | [N]           | [X] % | [X] %   | -         | [DATUM]     |
| [INVESTOR A]      | A      | [N]     | [N]           | [X] % | [X] %   | 1x np     | -           |
| ESOP-Pool         | Common | [N]     | reserviert    | [X] % | -       | -         | -           |
| Gesamt            |        | [N]     | [BETRAG]      | 100 % | 100 %   |           |             |

Pre-Money: [BETRAG] EUR | Investment: [BETRAG] EUR | Post-Money: [BETRAG] EUR
```

## Output-Template: Liquidation-Waterfall

**Adressat:** Intern / SHA-Verhandlung

```
LIQUIDATION WATERFALL — [FIRMA] GmbH
Exit-Preis: [BETRAG] EUR | Datum: [DATUM]

Schritt 1: Liquidation Preference [INVESTOR B] ([Nx] participating)
  Preference: [BETRAG] EUR
  Verbleibend: [REST] EUR

Schritt 2: Liquidation Preference [INVESTOR A] ([Nx] non-participating)
  Preference: max([BETRAG], [X]% * [REST])
  Gewaehlt: [anteilig/Preference] = [BETRAG] EUR
  Verbleibend: [REST2] EUR

Schritt 3: Restverteilung an Gruender und Beteiligte
  [NAME GRUENDER 1]: [X]% * [REST2] = [BETRAG] EUR
  [NAME GRUENDER 2]: [X]% * [REST2] = [BETRAG] EUR

Gesamt-Checks: Summe aller Auszahlungen = [EXIT-PREIS] EUR
```

## Rote Schwellen

- Vesting-Rueckuebertragung formlos: unwirksam (§ 15 GmbHG; BGH NZG 2012, 379)
- Gesellschafterliste nicht aktualisiert: Haftung GF; gutglaeubiger Erwerb durch Dritte moeglich (§ 16 GmbHG)
- Liquidation Preference in SHA ohne Satzungsverankerung: beim Exit moeglicherweise unwirksam (BGH NZG 2021, 26)
- ESOP-Optionen ohne Satzungs-/Hauptversammlungsbeschluss: Kapitalerhoehung nicht vollziehbar

## Quellen und Vertiefung

- § 40 GmbHG (Gesellschafterliste), § 16 GmbHG (Legitimationswirkung)
- § 15 GmbHG (Abtretung), § 34 GmbHG (Einziehung), § 55 GmbHG (Kapitalerhoehung)
- BGH BGHZ 188, 331 (2011); BGH NZG 2012, 379; OLG Frankfurt GmbHR 2019, 1097; BGH NZG 2021, 26
- Scholz/Verse § 40; Baumbach/Hueck § 15; MüKo GmbHG/Reichert § 34

## Uebergabe an andere Skills

- `gesellschaftsgruender-share-classes-a-b-c` — bei mehreren Klassen
- `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` — Verwässerung und neue Runde
- `gesellschaftsgruender-genehmigtes-kapital` — Vorrats-Beschluss fuer ESOP
- `gesellschaftsgruender-notar-vorbereitung` — Gesellschafterliste fuer Anmeldung
