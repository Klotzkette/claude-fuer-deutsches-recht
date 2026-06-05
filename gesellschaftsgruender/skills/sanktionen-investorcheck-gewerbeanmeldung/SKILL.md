---
name: sanktionen-investorcheck-gewerbeanmeldung
description: "Sanktionen Investorcheck Gewerbeanmeldung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sanktionen Investorcheck Gewerbeanmeldung

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Sanktionen Investorcheck Gewerbeanmeldung** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-sanktionen-investorcheck` | Prüft Investoren und Gesellschafter auf Sanktions-, Geldwäsche- und Außenwirtschaftsrisiken. |
| `gesellschaftsgruender-gewerbeanmeldung-finanzamt` | Gewerbeanmeldung und steuerliche Ersterfassung nach GmbH-Gründung vorbereiten: Fragebogen Finanzamt, Gewerbeamt. Normen: § 14 GewO, AO, UStG. Prüfraster: Steuerklassen, USt-Voranmeldung, Betriebsstaette, Umsatzsteuer-ID. Output: Ausfuell-Checkliste Gewerbeanmeldung und Finanzamt-Fragebogen. Abgrenzung: nicht Handelsregisteranmeldung HRB. |
| `gesellschaftsgruender-gf-sozialversicherungs-status` | Sozialversicherungsrechtlichen Status des GmbH-Geschäftsführers klaeren: Pflichtversicherung vs. Befreiung bei beherrschendem Gesellschafter-GF. Normen: § 7 SGB IV, §§ 1 ff. SGB VI. Prüfraster: Beteiligungshoehe, Weisungsabhaengigkeit, BSG-Rechtsprechung. Output: Statusbewertung GF-Sozialversicherung mit Handlungsempfehlung. Abgrenzung: nicht Einkommensteueraspekte. |
| `gesellschaftsgruender-gruender-intake` | Ersterfassung des Gründungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschäftszweck. Normen: GmbHG, AktG, HGB. Prüfraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output: Gründungsintake-Bogen. Abgrenzung: nicht detaillierte Rechtsformberatung (eigener Skill). |
| `gesellschaftsgruender-holdingmodell` | Prüft Holding vor operativer Gesellschaft, Beteiligungen, Steuer-/Haftungs- und Governancefragen. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Sanktionen Investorcheck Gewerbeanmeldung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-sanktionen-investorcheck`

**Fokus:** Prüft Investoren und Gesellschafter auf Sanktions-, Geldwäsche- und Außenwirtschaftsrisiken.

# Sanktions- und Investorencheck

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanktions- und Investorencheck` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Keine Transaktion ohne Identität, UBO, Mittelherkunft, Sanktionslistenprüfung.

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

## 2. `gesellschaftsgruender-gewerbeanmeldung-finanzamt`

**Fokus:** Gewerbeanmeldung und steuerliche Ersterfassung nach GmbH-Gründung vorbereiten: Fragebogen Finanzamt, Gewerbeamt. Normen: § 14 GewO, AO, UStG. Prüfraster: Steuerklassen, USt-Voranmeldung, Betriebsstaette, Umsatzsteuer-ID. Output: Ausfuell-Checkliste Gewerbeanmeldung und Finanzamt-Fragebogen. Abgrenzung: nicht Handelsregisteranmeldung HRB.

# Gewerbeanmeldung und Finanzamt-Erfassung

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gewerbeanmeldung und Finanzamt-Erfassung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre vor den Anmeldungen

1. Wann wurde / wird die gewerbliche Tätigkeit aufgenommen — Gewerbeanmeldung unverzüglich danach (§ 14 GewO)?
2. Handelt es sich um eine juristische Person (GmbH, UG, AG) — dann immer Regelbesteuerung, kein Kleinunternehmer.
3. Ist B2B-Geschäft oder B2C mit ausländischen Kunden geplant — dann USt-IdNr. sofort beantragen.
4. Gibt es größere Investitionsausgaben im ersten Jahr (Büro, IT, Fuhrpark) — dann Regelbesteuerung empfehlenswert wegen Vorsteuerabzug.
5. Liegt ein genehmigungspflichtiger Gegenstand vor (§ 34a GewO, § 2 GastG, BaFin) — dann Genehmigung vor Anmeldung sicherstellen.
6. Ist ein Steuerberater eingeschaltet — Empfehlung: ja, wegen Vorauszahlungsschätzung und USt-Wahl.

## Zentrale Normen

- **§ 14 GewO** — Gewerbeanmeldungspflicht: unverzüglich nach Aufnahme der gewerblichen Tätigkeit; zuständig: örtliches Gewerbeamt.
- **§ 146 Abs. 2 GewO** — Bußgeld bei Versäumnis: bis 1.000 EUR.
- **§ 138 AO** — Steuerliche Erfassungspflicht: Gewerbetreibende müssen Finanzamt innerhalb eines Monats nach Aufnahme informieren.
- **§ 18 UStG** — USt-Voranmeldung: monatlich oder quartalsweise über ELSTER; bis 10. des Folgemonats.
- **§ 19 UStG** — Kleinunternehmer-Regelung: Jahresumsatz ≤ 22.000 EUR Vorjahr und voraussichtlich ≤ 50.000 EUR aktuelles Jahr; kein Vorsteuerabzug.
- **§ 41a EStG** — Lohnsteuer-Anmeldung: monatlich oder quartalsweise; bis 10. des Folgemonats.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anmeldungs-Matrix

| Behörde | Pflicht | Frist | Kosten | Konsequenz Versäumnis |
|---|---|---|---|---|
| Gewerbeamt | § 14 GewO | unverzüglich | 20-60 EUR | Bußgeld bis 1.000 EUR |
| Finanzamt (ELSTER) | § 138 AO | 1 Monat | — | Schätzung; Säumniszuschläge |
| USt-IdNr. (BZSt) | Bei B2B/EU | Sofort beantragen | — | Innergemeinschaftliche Geschäfte scheitern |
| Lohnsteuer-Anmeldung | Bei Mitarbeitern | 10. Folgemonat | — | §§ 34, 69 AO GF-Haftung |
| Umsatzsteuer-Voranmeldung | § 18 UStG | 10. Folgemonat | — | Säumniszuschlag |
| KSt-Vorauszahlung | § 19 KStG | 10.3./6./9./12. | — | Säumniszuschlag |
| GewSt-Vorauszahlung | § 19 GewStG | 15.2./5./8./11. | — | Säumniszuschlag |

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen beantworten; Steuerberater einschalten.
2. **Gewerbeanmeldung** — örtliches Gewerbeamt; Personalausweis, HR-Auszug, ggf. Genehmigungen; Kosten 20-60 EUR.
3. **ELSTER-Zugang** — Steuerberater oder Gesellschaft registriert sich bei elster.de; Zertifikat beantragen.
4. **Fragebogen steuerliche Erfassung** — über ELSTER; ggf. Steuerberater beauftragt; USt-Wahl treffen.
5. **USt-IdNr.** — bei B2B oder EU-Geschäft sofort beim Bundeszentralamt für Steuern beantragen.
6. **Steuernummer abwarten** — Finanzamt teilt Steuernummer mit (ca. 2-4 Wochen).
7. **USt-Voranmeldung einrichten** — monatlich oder quartalsweise; Termin im Kalender.
8. **Lohnsteuer-Anmeldung** (bei Mitarbeitern) — monatlich; vor 10. Folgemonat.
9. **KSt/GewSt-Vorauszahlungen** — quartalsweise; Termine einplanen.

## Output-Template Anmeldungs-Checkliste

**Adressat:** Mandant/Gründer — Tonfall verständlich-anleitend
```
ANMELDUNGS-CHECKLISTE GEWERBEANMELDUNG + FINANZAMT
Gesellschaft: [Firmenname] GmbH / UG
HR-Eintragung: [Datum]
Aufnahme Geschäftsbetrieb: [Datum]

GEWERBEAMT
Zuständiges Gewerbeamt: [Behörde, Ort]
Anmeldung erledigt bis: [Datum HR + unverzüglich]
Anmeldedatum tatsächlich: [ ] ausstehend / [Datum]
Kosten bezahlt: [ ] Ja / [ ] Nein

FINANZAMT
ELSTER-Zugang: [ ] Vorhanden / [ ] Beantragt
Fragebogen eingereicht bis: [Datum HR + 1 Monat]
Fragebogen tatsächlich eingereicht: [ ] ausstehend / [Datum]
USt-Wahl: [ ] Regelbesteuerung / [ ] Kleinunternehmer (§ 19 UStG)
USt-IdNr. beantragt: [ ] Ja / [ ] Nicht erforderlich

STEUERNUMMER
Steuernummer zugewiesen: [ ] ausstehend / [Steuernummer]
USt-IdNr. zugewiesen: [ ] ausstehend / [DE-Nummer]

VORANMELDUNGS-TURNUS
USt-Voranmeldung: [ ] Monatlich / [ ] Quartalsweise
Lohnsteuer-Anmeldung: [ ] Monatlich / [ ] Quartalsweise / [ ] Nicht erforderlich
KSt-Vorauszahlung: 10.03. / 10.06. / 10.09. / 10.12.
GewSt-Vorauszahlung: 15.02. / 15.05. / 15.08. / 15.11.
```

## Kleinunternehmer vs. Regelbesteuerung

| Merkmal | Kleinunternehmer § 19 UStG | Regelbesteuerung |
|---|---|---|
| Umsatzgrenze | ≤ 22.000 EUR Vorjahr + ≤ 50.000 EUR aktuell | Keine Grenze |
| Vorsteuerabzug | Kein | Ja |
| Rechnungsausweis | Keine USt | USt ausweisen |
| B2B-Eignung | Eingeschränkt (Kunde verliert Vorsteuer) | Standard |
| Jurist. Person (GmbH) | Nicht möglich | Immer |
| Bindungsdauer bei Verzicht | 5 Jahre (§ 19 Abs. 2 UStG) | — |

## Rote Schwellen

- Gewerbeanmeldung verzögert → Bußgeld bis 1.000 EUR; kein Mildungsgrund bei Erstgründung.
- Fragebogen nicht eingereicht → Finanzamt schätzt; Schätzung oft höher als tatsächliche Steuerlast.
- Kleinunternehmer bei GmbH gewählt → unzulässig; GmbH immer Regelbesteuerung.
- USt-IdNr. fehlt bei EU-B2B-Geschäft → Reverse-Charge nicht anwendbar; Doppelbelastung.
- Lohnsteuer nicht abgeführt → GF persönlich haftbar (§§ 34, 69 AO).

## Quellen und Vertiefung

- §§ 14, 146 GewO (Gewerbeanmeldung, Bußgeld)
- § 138 AO (steuerliche Erfassung)
- §§ 18, 19 UStG (USt-Voranmeldung, Kleinunternehmer)
- § 41a EStG (Lohnsteuer-Anmeldung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Tipke/Lang, Steuerrecht, § 17 Rn. 1-40

## Übergabe an andere Skills

- `gesellschaftsgruender-kommandocenter` — Master-Gründung
- `gesellschaftsgruender-ihk-und-berufsgenossenschaft` — weitere Pflichtmeldungen
- `gesellschaftsgruender-transparenzregister` — GwG-Pflicht
- `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` — laufende Steuerpflichten

## 3. `gesellschaftsgruender-gf-sozialversicherungs-status`

**Fokus:** Sozialversicherungsrechtlichen Status des GmbH-Geschäftsführers klaeren: Pflichtversicherung vs. Befreiung bei beherrschendem Gesellschafter-GF. Normen: § 7 SGB IV, §§ 1 ff. SGB VI. Prüfraster: Beteiligungshoehe, Weisungsabhaengigkeit, BSG-Rechtsprechung. Output: Statusbewertung GF-Sozialversicherung mit Handlungsempfehlung. Abgrenzung: nicht Einkommensteueraspekte.

# Sozialversicherungs-Status des Geschäftsführers

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sozialversicherungs-Status des Geschäftsführers` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage — kläre bei jedem neuen GF

1. Ist der GF Gesellschafter oder Fremd-GF (kein Gesellschafter)?
2. Bei Gesellschafter-GF: wie hoch ist die Beteiligungsquote (> 50 %, = 50 %, < 50 %)?
3. Existiert eine Sperrminorität durch Sondervetorecht in Satzung oder SHA?
4. Wurde der Gesellschafter-Anstellungsvertrag vor Beginn der Tätigkeit abgeschlossen?
5. Wurde ein Statusfeststellungsantrag (§ 7a SGB IV) beantragt?
6. Droht rückwirkende Beitragspflicht — hat der GF bereits ohne Statusklärung angefangen?

## Zentrale Normen

- **§ 7 SGB IV** — Abhängige Beschäftigung: weisungsgebunden, in fremde Betriebsorganisation eingegliedert, kein unternehmerisches Risiko.
- **§ 7a SGB IV** — Statusfeststellungsverfahren: bindende Feststellung durch Clearingstelle der DRV Bund.
- **§ 25 SGB IV** — Verjährung der Beitragspflicht: 4 Jahre; bei vorsätzlicher Vorenthaltung: 30 Jahre.
- **§§ 28a, 28d SGB IV** — Meldepflichten des Arbeitgebers; bei pflichtiger Beschäftigung: An- und Abmeldung.
- **§ 14 SGB IV** — Arbeitsentgelt; Sachbezüge; Grundlage der Beitragsberechnung.

## Aktuelle Rechtsprechung (BSG-Linie)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## BSG-Statusmatrix Geschäftsführer

| GF-Typ | Quote | Vetorecht | SV-Status | Empfehlung |
|---|---|---|---|---|
| Solo-GF (100 %) | 100 % | Ja (allein) | Frei | Statusfeststellung optional |
| Mehrheits-GF | > 50 % | In der Regel | Frei | Statusfeststellung empfohlen |
| Hälfte-GF | = 50 % | Unklar | Strittig | Statusfeststellung zwingend |
| Minderheits-GF mit Sperrminorität | < 50 % | Ja (vertraglich) | Frei (wenn umfassend) | Statusfeststellung zwingend |
| Minderheits-GF ohne Veto | < 50 % | Nein | Pflichtig | Anmeldung sofort |
| Fremd-GF | 0 % | — | Pflichtig | Anmeldung sofort |

## Statusfeststellungsantrag § 7a SGB IV

### Was ist das?

Formelle, **bindende Feststellung** des Sozialversicherungsstatus durch die Clearingstelle der Deutschen Rentenversicherung Bund. Bindet alle Sozialversicherungsträger.

### Wann beantragen?

- Vor Aufnahme der GF-Tätigkeit (rückwirkende Freistellung bei rechtzeitigem Antrag möglich).
- Bei Änderung der Beteiligungsquote oder Vetorechte.
- Bei Zweifelsfällen (50 %-GF, Minderheits-GF mit Vetorecht).

### Unterlagen

- Formular V0027 (DRV Bund).
- Gesellschaftsvertrag / Satzung.
- Geschäftsführer-Anstellungsvertrag.
- Gesellschafterliste.
- Nachweis über Sondervetorecht (ggf. SHA).

### Dauer

- Bearbeitungszeit: 3-6 Monate (DRV Bund ist oft ausgelastet).
- In der Zwischenzeit: Einzug von Beiträgen zur Sicherheit empfohlen.

## Schritt-für-Schritt-Workflow

1. **Triage** — 6 Triage-Fragen beantworten; GF-Typ und Beteiligungsquote feststellen.
2. **Statusmatrix** — in Tabelle oben einsortieren; vorläufigen Status bestimmen.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Statusfeststellungsantrag** — bei Zweifelsfällen und Mehrheits-GF: Antrag stellen; Formular V0027.
5. **Bis Bescheid** — SV-Beiträge sicherheitshalber einziehen (rückwirkende Gutschrift möglich).
6. **Bei Pflichtstatus** — Anmeldung bei Krankenkasse; GKV oder PKV-Wahl des GF.
7. **Lohnabrechnung einrichten** — bei Fremd-GF: Lohnbuchhaltung mit SV-Beitragsabzug.
8. **Folgeprüfung bei Strukturänderung** — Beteiligungsänderung → neuer Statusfeststellungsantrag.

## Output-Template Status-Dokumentation

**Adressat:** Gesellschaft / Steuerberater intern — Tonfall sachlich-präzise
```
SV-STATUS DOKUMENTATION GESCHÄFTSFÜHRER
Gesellschaft: [Firmenname] GmbH
GF-Name: [Name]
Beginn der GF-Tätigkeit: [Datum]
Erstellt: [Datum]

BETEILIGUNGSSTRUKTUR
Beteiligungsquote: [%]
Stimmrechtsquote: [%]
Sondervetorecht in Satzung: [ ] Ja (§ [X] GV) / [ ] Nein
Sondervetorecht in SHA: [ ] Ja (§ [X] SHA) / [ ] Nein

VORLÄUFIGER STATUS (BSG-Matrix)
Status: [ ] Sozialversicherungsfrei / [ ] Sozialversicherungspflichtig / [ ] Unklar
Begründung: [kurze Erläuterung]

STATUSFESTSTELLUNG § 7a SGB IV
Antrag gestellt: [ ] Ja am [Datum] / [ ] Nein / [ ] Nicht erforderlich
Bescheid erhalten: [ ] ausstehend / [Datum, Ergebnis]

BEI SV-PFLICHT
Zuständige Krankenkasse: [Name]
Anmeldedatum: [Datum]
Beitragssatz gesamt: ca. 40 % des Bruttogehalts (AN + AG je ca. 20 %)

RÜCKWIRKUNGS-RISIKO
Zeitraum ohne Statusklärung: [Monate]
Nachzahlungsrisiko (4 Jahre): [geschätzt EUR]
```

## Rote Schwellen

- GF beginnt Tätigkeit ohne Statusklärung → rückwirkende Beitragspflicht bis 4 Jahre (§ 25 SGB IV).
- Falscher Status angenommen (frei statt pflichtig) → GF und Gesellschaft haften gesamtschuldnerisch.
- Sperrminorität in SHA, nicht in Satzung → BSG erkennt SHA-Vetorecht an, wenn umfassend; sorgfältige Formulierung nötig.
- Änderung der Beteiligungsquote ohne neue Statusprüfung → Status kann sich rückwirkend ändern.
- Vorsätzliche Vorenthaltung der SV-Beiträge → 30-jährige Verjährung; Strafbarkeit § 266a StGB.

## Quellen und Vertiefung

- §§ 7, 7a, 25, 28a SGB IV (Beschäftigungsbegriff, Statusfeststellung, Verjährung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Übergabe an andere Skills

- `gesellschaftsgruender-geschaeftsfuehrervertrag` — GF-Anstellungsvertrag; Gehaltsgestaltung
- `gesellschaftsgruender-geschaeftsfuehrer-pflichten-startphase` — GF-Pflichten nach Eintragung
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Satzung und Vetorecht-Klauseln

## 4. `gesellschaftsgruender-gruender-intake`

**Fokus:** Ersterfassung des Gründungsvorhabens: Rechtsform, Gesellschafterkreis, Kapital, Geschäftszweck. Normen: GmbHG, AktG, HGB. Prüfraster: Intake-Fragen Rechtsformwahl, Haftung, steuerliche Aspekte, Zeitplan. Output: Gründungsintake-Bogen. Abgrenzung: nicht detaillierte Rechtsformberatung (eigener Skill).

# Gründer-Intake

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gründer-Intake` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## 5. `gesellschaftsgruender-holdingmodell`

**Fokus:** Prüft Holding vor operativer Gesellschaft, Beteiligungen, Steuer-/Haftungs- und Governancefragen.

# Holdingmodell Gründer

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Holdingmodell Gründer` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Keine Steuerberatung ersetzen; Strukturfragen und Timing.

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
