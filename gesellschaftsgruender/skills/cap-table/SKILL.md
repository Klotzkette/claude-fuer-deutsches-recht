---
name: cap-table
description: "Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle mit Anteilsuebersicht und Verwässerungsrechnung. Abgrenzung: nicht Gründungsprotokoll oder Handelsregisteranmeldung im Gesellschaftsgruender: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Cap Table

## Arbeitsbereich

Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle mit Anteilsuebersicht und Verwässerungsrechnung. Abgrenzung: nicht Gründungsprotokoll oder Handelsregisteranmeldung. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Cap Table` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

| Gesellschafter | Klasse | Anteile | Nennwert (EUR) | % | Stimmen | Liq.Pref. | Vesting bis |
|-------------------|--------|---------|---------------|-------|---------|-----------|-------------|
| [NAME GRUENDER 1] | Common | [N] | [N] | [X] % | [X] % | - | [DATUM] |
| [NAME GRUENDER 2] | Common | [N] | [N] | [X] % | [X] % | - | [DATUM] |
| [INVESTOR A] | A | [N] | [N] | [X] % | [X] % | 1x np | - |
| ESOP-Pool | Common | [N] | reserviert | [X] % | - | - | - |
| Gesamt | | [N] | [BETRAG] | 100 % | 100 % | | |

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gesellschafterliste nicht aktualisiert: Haftung GF; gutglaeubiger Erwerb durch Dritte moeglich (§ 16 GmbHG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- ESOP-Optionen ohne Satzungs-/Hauptversammlungsbeschluss: Kapitalerhoehung nicht vollziehbar

## Quellen und Vertiefung

- § 40 GmbHG (Gesellschafterliste), § 16 GmbHG (Legitimationswirkung)
- § 15 GmbHG (Abtretung), § 34 GmbHG (Einziehung), § 55 GmbHG (Kapitalerhoehung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Uebergabe an andere Skills

- `gesellschaftsgruender-share-classes-a-b-c` — bei mehreren Klassen
- `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` — Verwässerung und neue Runde
- `gesellschaftsgruender-genehmigtes-kapital` — Vorrats-Beschluss fuer ESOP
- `gesellschaftsgruender-notar-vorbereitung` — Gesellschafterliste fuer Anmeldung
