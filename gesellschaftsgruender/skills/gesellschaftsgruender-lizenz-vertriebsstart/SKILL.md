---
name: gesellschaftsgruender-lizenz-vertriebsstart
description: "Lizenz Vertriebsstart: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lizenz Vertriebsstart

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Lizenz Vertriebsstart** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-kommandocenter` | Navigationszentrum für alle Gründungs-Skills: Fortschrittsanzeige, Delegierung an Fachinhalte, Status. Normen: GmbHG, AktG, HGB. Prüfraster: aktueller Gründungsstand, offene Schritte, Notartermin, Eintragungsstatus. Output: Statusuebersicht Gründungsprozess mit Naechste-Schritte-Liste. Abgrenzung: kein inhaltlicher Gründungs-Skill. |
| `gesellschaftsgruender-lizenz-und-vertriebsstart` | Erstellt rechtliche Startliste für erste Kundenverträge, AGB, Datenschutz, IP und Gewährleistung. |
| `gesellschaftsgruender-lohn-payroll-start` | Prüft erste Beschäftigte, Minijob, SV-Meldung, Lohnkonto, BG und Arbeitsverträge. |
| `gesellschaftsgruender-mandantenbrief-naechste-schritte` | Schreibt verständlichen Gründerbrief mit Entscheidungen, Risiken, To-dos, Kosten und Zeitplan. |
| `gesellschaftsgruender-minderjaehrige-gesellschafter` | Prüft Minderjährige in Gesellschaften: Vertretung, Familiengericht, Haftung und Genehmigungen. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Lizenz Vertriebsstart**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-kommandocenter`

**Fokus:** Navigationszentrum für alle Gründungs-Skills: Fortschrittsanzeige, Delegierung an Fachinhalte, Status. Normen: GmbHG, AktG, HGB. Prüfraster: aktueller Gründungsstand, offene Schritte, Notartermin, Eintragungsstatus. Output: Statusuebersicht Gründungsprozess mit Naechste-Schritte-Liste. Abgrenzung: kein inhaltlicher Gründungs-Skill.

# Kommandocenter Gesellschaftsgründung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kommandocenter Gesellschaftsgründung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre beim Erstgespräch

1. Welche Rechtsform ist geplant oder noch offen — GmbH, UG, GbR (eGbR), KG, GmbH & Co. KG, PartGmbB, gGmbH?
2. Wie viele Gründer und ist Investoren-Aufnahme in den nächsten 24 Monaten wahrscheinlich?
3. Zeitrahmen — wann soll die Gesellschaft operativ tätig sein? Ist ein Notartermin bereits gebucht?
4. Liegt eine Sacheinlage vor (Werthaltigkeit prüfen, Sachgründungsbericht)?
5. Genehmigungspflichtiger Unternehmensgegenstand (Bank, Versicherung, Spielhalle)?
6. Internationale Gesellschafter oder grenzüberschreitende Tätigkeit (Sanktionsrecht, FDI)?

## Zentrale Normen

- **§§ 2, 5, 7 GmbHG** — Beurkundung, Stammkapital, Anmeldevoraussetzungen.
- **§ 5a GmbHG** — UG-Sondervariante; Thesaurierungspflicht 25 %.
- **§§ 15 ff. HGB / § 8 HGB** — Handelsregisterpflicht und Wirkung der Eintragung.
- **§ 19 GwG** — Transparenzregistermeldepflicht; wirtschaftlich Berechtigte.
- **§§ 14-15 GewO** — Gewerbeanmeldungspflicht; sofort nach Geschäftsaufnahme.
- **§ 138 AO** — Steuerliche Erfassung beim Finanzamt innerhalb eines Monats.
- **§ 15a InsO** — Insolvenzantragspflicht ab Gründung; GF-Pflicht kennen.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Gründungsphasen-Übersicht

| Phase | Inhalt | Dauer (ca.) | Fachmodul |
|---|---|---|---|
| 0 — Rechtsformwahl | GmbH, UG, GbR, KG, GmbH & Co. KG, PartGmbB, gGmbH abwägen | Woche 1 | `gesellschaftsgruender-rechtsformwahl` |
| A — Vorbereitung | Firmencheck, Sitz, Gegenstand, Stammkapital, Gesellschafterstruktur | Woche 2-3 | `gesellschaftsgruender-gmbh-vorbereitung` |
| B — Verträge | Satzung/GV, Gesellschaftervereinbarung, GF-Anstellungsvertrag | Woche 3-4 | `gesellschaftsgruender-gesellschaftsvertrag-gmbh` |
| C — Notar | Beurkundung; alternativ Online-Gründung (DiRUG) | Woche 4-5 | `gesellschaftsgruender-notar-vorbereitung` |
| D — Behörden | HR, Gewerbe, Finanzamt, Transparenzregister, IHK, BG | Woche 5-6 | `gesellschaftsgruender-handelsregister-anmeldung` |
| E — Operativer Start | Geschäftskonto, Stammkapital einzahlen, Buchhaltung, GF-Pflichten | Woche 6-8 | `gesellschaftsgruender-stammkapital-einzahlung` |

## Fristen-Matrix

| Pflicht | Frist | Konsequenz bei Versäumnis | Norm |
|---|---|---|---|
| Gewerbeanmeldung | unverzüglich nach Geschäftsaufnahme | Bußgeld bis 1.000 EUR | § 14 GewO |
| Steuerliche Erfassung (FA) | innerhalb 1 Monat | Schätzung; Säumniszuschläge | § 138 AO |
| Berufsgenossenschaft | binnen 1 Woche | Bußgeld | § 192 SGB VII |
| Transparenzregister | unverzüglich (sobald wirtschaftlich Berechtigter feststeht) | bis 150.000 EUR | § 56 GwG |
| Insolvenzantragspflicht GF | 6 Wochen (Überschuldung) / 3 Wochen (ZU) | persönliche Haftung § 15b InsO | § 15a InsO |
| Erste Umsatzsteuervoranmeldung | bis Ende des Folgemonats | Säumnis | § 18 UStG |

## Kostentabelle nach Rechtsform

| Rechtsform | Notar | Handelsregister | Sonstige | Gesamt ca. |
|---|---|---|---|---|
| eK | — | 70 EUR | IHK | < 200 EUR |
| eGbR (MoPeG) | nur bei Wahl | 80-150 EUR | — | < 300 EUR |
| UG (Musterprotokoll) | 250-450 EUR | 150 EUR | IHK | < 800 EUR |
| GmbH (Musterprotokoll) | 400-600 EUR | 150 EUR | IHK | ca. 800-1.000 EUR |
| GmbH (individuelle Satzung) | 800-1.500 EUR | 150 EUR | IHK+StB | 1.500-3.000 EUR |
| GmbH & Co. KG | 1.500-3.000 EUR | 300 EUR | IHK+StB | 3.000-5.000 EUR |
| AG | 3.000-8.000 EUR | 300 EUR | HV-Vorbereitung | > 10.000 EUR |

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen oben beantworten; Rechtsform provisorisch festlegen.
2. **Intake** — strukturierte Eingangsabfrage aller Gründungsdaten → `gesellschaftsgruender-gruender-intake`.
3. **Rechtsformwahl** — finale Entscheidung mit Abwägungsdokumentation → `gesellschaftsgruender-rechtsformwahl`.
4. **Vorbereitung** — Firmencheck, Stammkapital, Gesellschafterstruktur, Holding-Frage.
5. **Verträge** — Satzung/GV, SHA, GF-Anstellungsvertrag parallel vorbereiten.
6. **Notartermin** — Unterlagen-Checkliste abarbeiten; Stammpkapital bereitstellen.
7. **HR-Anmeldung** — Notar reicht ein; Eintragung abwarten (2-4 Wochen).
8. **Behörden** — Gewerbeamt, Finanzamt, Transparenzregister, IHK, BG parallel anmelden.
9. **Operativer Start** — Geschäftskonto, Stammkapital einzahlen, GF-Pflichten aufnehmen.
10. **Nachsorge** — erstes GF-Meeting protokollieren; Buchführung starten; SV-Status klären.

## Output-Template Gründungs-Ablaufplan

**Adressat:** Mandant/Gründer — Tonfall verständlich-erklärend
```
GRÜNDUNGS-ABLAUFPLAN
Mandant: [Name(n) der Gründer]
Rechtsform: [GmbH / UG / KG / etc.]
Firma: [Firmenname]
Stammkapital: [EUR]
Erstellt: [Datum]

MEILENSTEINE
| Meilenstein | Geplantes Datum | Owner | Status |
|------------|----------------|-------|--------|
| Firmencheck abgeschlossen | [Datum] | [Name] | offen |
| Satzungsentwurf fertig | [Datum] | [Name] | offen |
| Notartermin | [Datum] | [Name] | offen |
| Stammkapital eingezahlt | [Datum] | [Name] | offen |
| Handelsregister-Eintragung | [Datum] | [Name] | offen |
| Gewerbeanmeldung | [Datum] | [Name] | offen |
| Finanzamt-Erfassung | [Datum] | [Name] | offen |
| Transparenzregister | [Datum] | [Name] | offen |
| Operativer Start | [Datum] | [Name] | offen |

FRISTEN-ALARM
[ ] Gewerbeanmeldung bis: [Datum]
[ ] Finanzamt-Fragebogen bis: [Datum]
[ ] Berufsgenossenschaft bis: [Datum]
[ ] Transparenzregister bis: [Datum]

BETEILIGTE
Notar: [Name, Ort]
Steuerberater: [Name]
Gesellschafter: [Namen]
Geschäftsführer: [Namen]
```

## Rote Schwellen

- Sacheinlage ohne Sachgründungsbericht → HR verweigert Eintragung; persönliche Differenzhaftung (§ 9 GmbHG).
- Geschäfte vor HR-Eintragung ohne Gesellschafter-Genehmigung → GF-Handelndenhaftung (§ 11 GmbHG).
- Genehmigungspflichtiger Gegenstand ohne Genehmigung → Eintragung gesperrt.
- Insolvenzantragspflicht (§ 15a InsO) schon in Gründungsphase ausgelöst (z.B. Überschuldung durch Vorbelastung) → sofortige anwaltliche Beratung.
- Transparenzregister-Meldung vergessen → Bußgeld bis 150.000 EUR (§ 56 GwG).

## Quellen und Vertiefung

- §§ 2, 5, 7, 9, 11 GmbHG (Gründung, Vorgesellschaft, Anmeldung)
- §§ 14-15 GewO (Gewerbeanmeldung)
- § 138 AO (Steuerliche Erfassung)
- §§ 19, 56 GwG (Transparenzregister)
- § 15a InsO (Insolvenzantragspflicht)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Emmerich, GmbHG, § 11 Rn. 1-40

## Übergabe an andere Skills

- `gesellschaftsgruender-rechtsformwahl` — Rechtsformwahl-Entscheidung
- `gesellschaftsgruender-gruender-intake` — strukturierte Eingangsabfrage
- `gesellschaftsgruender-gmbh-vorbereitung` — GmbH-Vorbereitung
- `gesellschaftsgruender-notar-vorbereitung` — Notarsitzung
- `gesellschaftsgruender-handelsregister-anmeldung` — HR-Eintragung
- `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` — GF-Pflichten ab Tag 1

## 2. `gesellschaftsgruender-lizenz-und-vertriebsstart`

**Fokus:** Erstellt rechtliche Startliste für erste Kundenverträge, AGB, Datenschutz, IP und Gewährleistung.

# Lizenz- und Vertriebsstart

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lizenz- und Vertriebsstart` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Route zu Vertragsrecht/AGB/Datenschutz.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 3. `gesellschaftsgruender-lohn-payroll-start`

**Fokus:** Prüft erste Beschäftigte, Minijob, SV-Meldung, Lohnkonto, BG und Arbeitsverträge.

# Payroll und erste Mitarbeitende

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Payroll und erste Mitarbeitende` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Route zu Arbeitsrecht/Steuer.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 4. `gesellschaftsgruender-mandantenbrief-naechste-schritte`

**Fokus:** Schreibt verständlichen Gründerbrief mit Entscheidungen, Risiken, To-dos, Kosten und Zeitplan.

# Mandantenbrief nächste Schritte

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenbrief nächste Schritte` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Keine Überwältigung; klare Optionen.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.

## 5. `gesellschaftsgruender-minderjaehrige-gesellschafter`

**Fokus:** Prüft Minderjährige in Gesellschaften: Vertretung, Familiengericht, Haftung und Genehmigungen.

# Minderjährige Gesellschafter

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Minderjährige Gesellschafter` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

BGB AT und Familienrecht einbinden.

## Rechts- und Quellenanker

Je nach Rechtsform live prüfen: GmbHG, HGB, BGB-Gesellschaftsrecht nach MoPeG, PartGG, GenG, AktG, GwG, GewO, AO/UStG/EStG sowie Register- und Notarvorgaben.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gründerfreundliche Kurzantwort
- To-do-Liste mit Zuständigen
- Dokumenten- und Lückenliste
- Risikoampel
- passende Anschluss-Skills


## Vertiefter Gründer-Workflow

Arbeite nicht abstrakt, sondern wie eine Gründungsakte mit Notar, Registergericht, Bank, Steuerberater und operativem Start. Führe den Nutzer durch diese Entscheidungspunkte:

1. **Rechtsform und Phase:** Vorgründung, Gründung, Registereintragung, erste Verträge, Änderung, Krise oder Exit. Prüfe, ob GmbH/UG, eGbR, OHG/KG, PartG, Verein, Genossenschaft oder ausländische Struktur betroffen ist.
2. **Dokumente:** Satzung/Gesellschaftsvertrag, Gesellschafterliste, Geschäftsführerbeschluss, Handelsregisteranmeldung, Notarentwurf, Bank-/KYC-Unterlagen, steuerliche Erfassung, Gewerbeanmeldung und wirtschaftlich Berechtigte trennen.
3. **Risikoachsen:** Haftung vor Eintragung, Vertretungsmacht, Kapitalaufbringung, Sacheinlage, verdeckte Sacheinlage, Scheinselbstständigkeit, Erlaubnispflichten, Steuer- und Umsatzsteuerstart, IP-/Lizenzketten, Datenschutz und Geldwäsche.
4. **Praxisentscheidung:** Immer eine Gründeroption, eine konservative Anwaltsoption und eine schnelle Minimaloption darstellen. Bei Kosten-/Zeitkonflikten offen sagen, was schneller ist und welches Risiko bleibt.
5. **Anschlussarbeit:** Am Ende konkrete Folge-Skills aus `gesellschaftsgruender` nennen, etwa Satzung, Register, KYC, Steuerstart, Finanzierung, ESOP/VSOP, regulatorisches Geschäftsmodell oder Red-Team-Gründungspaket.

## Ergebnisqualität

- Liefere eine einseitige Gründer-Kurzfassung und danach eine anwaltliche Prüftabelle.
- Trenne Muss, Sollte, Optional und Später.
- Markiere externe Abhängigkeiten: Notar, Registergericht, Bank, Finanzamt, IHK/HWK, BaFin oder Fachbehörde.
- Keine endgültige Register- oder Steuerbehauptung ohne aktuellen Norm-/Formularcheck; bei Registerfragen die konkrete Zwischenverfügung oder den Notarentwurf als Primärquelle behandeln.
