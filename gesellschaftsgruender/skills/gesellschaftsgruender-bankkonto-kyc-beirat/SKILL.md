---
name: gesellschaftsgruender-bankkonto-kyc-beirat
description: "Bankkonto KYC Beirat: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bankkonto KYC Beirat

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Bankkonto KYC Beirat** im Plugin Gesellschaftsgründung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gesellschaftsgruender-bankkonto-kyc-paket` | Erstellt Bankkonto-Unterlagenpaket für Gründung und Kapitalerhöhung. |
| `gesellschaftsgruender-beirat-advisory-board` | Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen: §§ 45 52 GmbHG, §§ 95 ff. AktG analog. Prüfraster: Kompetenzen, Verguetung, Haftung, Abberufung, Datenschutz. Output: Beiratssatzung oder Advisory-Board-Charter. Abgrenzung: nicht Gesellschafterversammlung oder Aufsichtsrat. |
| `gesellschaftsgruender-bilinguale-dokumente` | Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA. Normen: §§ 2 3 GmbHG, HGB. Prüfraster: rechtliche Verbindlichkeit der deutschen Fassung, Abweichungsregelung, Notareignung. Output: Bilinguale Dokumentenvorlage Deutsch-Englisch. Abgrenzung: nicht reine Übersetzung ohne Inhaltsprüfung. |
| `gesellschaftsgruender-board-pack-erste-100-tage` | Erstellt Board-/Beiratsunterlagen für die ersten 100 Tage nach Gründung. |
| `gesellschaftsgruender-cap-table` | Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle mit Anteilsuebersicht und Verwässerungsrechnung. Abgrenzung: nicht Gründungsprotokoll oder Handelsregisteranmeldung. |

## Arbeitsweg

Im Plugin Gesellschaftsgründung gilt für **Bankkonto KYC Beirat**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gesellschaftsgruender-bankkonto-kyc-paket`

**Fokus:** Erstellt Bankkonto-Unterlagenpaket für Gründung und Kapitalerhöhung.

# Bankkonto und KYC-Paket

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bankkonto und KYC-Paket` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

Satzung, Gesellschafterliste, Ausweise, UBO, Geschäftsmodell, Mittelherkunft.

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

## 2. `gesellschaftsgruender-beirat-advisory-board`

**Fokus:** Beirat oder Advisory Board für GmbH oder UG einrichten: Satzungsregelung, Bestellungsverfahren, Beratungsvertrag. Normen: §§ 45 52 GmbHG, §§ 95 ff. AktG analog. Prüfraster: Kompetenzen, Verguetung, Haftung, Abberufung, Datenschutz. Output: Beiratssatzung oder Advisory-Board-Charter. Abgrenzung: nicht Gesellschafterversammlung oder Aufsichtsrat.

# Beirat / Advisory Board

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Beirat / Advisory Board` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Triage zu Beginn

Klaere vor Ausarbeitung der Beiratsstruktur:

1. **Rechtsform?** GmbH (freiwillig, Paragraf 52 GmbHG), AG (Aufsichtsrat Pflicht Paragraf 95 AktG), mitbestimmte GmbH (Pflicht-Aufsichtsrat ab 500 AN)?
2. **Aufgabentyp?** Rein beratend (Advisory Board ohne Entscheidungsbefugnis) oder mit echten Zustimmungsrechten (Beirat mit Vetomacht)?
3. **Vergütung?** Cash (Mittelstand), ESOP/Optionen (Startup), rein ehrenamtlich?
4. **Besetzung?** Externe Experten, Investoren-Vertreter, Familienmitglieder, unabhängige Dritte?
5. **Schlichtungsfunction gewuenscht?** Gesellschafter-Konflikt vorgebeugt durch Beirat als Mediator?
6. **D&O-Versicherung?** Bei echten Zustimmungsrechten empfohlen.

## Zentrale Normen

- **§ 52 GmbHG** — Verweis auf AktG-Vorschriften bei freiwilligem Aufsichtsrat / Beirat mit Kontrollbefugnissen
- **§ 95 AktG** — Pflicht-Aufsichtsrat bei AG; Zusammensetzung und Amtszeit
- **§ 111 AktG** — Aufgaben des Aufsichtsrats; analog fuer Beirat mit echter Kontrolle
- **§ 116 AktG** — Sorgfaltspflicht und Verschwiegenheit der AR-Mitglieder; analog Beirat
- **§§ 1, 4 DrittelbG / §§ 1, 7 MitbestG** — Pflicht-Aufsichtsrat bei GmbH ab 500 / 2.000 Arbeitnehmern
- **§§ 133, 157 BGB** — Auslegung der Beiratsordnung und -klauseln in der Satzung
- **§ 43 GmbHG** — Haftungsstandard; gilt analog fuer Beirat mit Zustimmungsrechten

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema: Beirat-Einrichtung

| Schritt | Frage | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Rechtsform und Pflicht | GmbH: Beirat freiwillig; AG: AR Pflicht; DrittelbG/MitbestG? | Klaren ob AR-Pflicht besteht |
| 2 | Aufgabenprofil | Beratend, kontrollierend, schlichterisch? | Festlegt Tiefe der Satzungs-Klausel |
| 3 | Satzungs-Klausel | Beirat in Satzung verankert? Befugnisse definiert? | Ohne Satzungs-Klausel kein Zustimmungsvorbehalt |
| 4 | Beiratsordnung | Detailregelungen ausgelagert (Meeting-Rhythmus, Vergütung, Quorum)? | Aenderungen ohne Notar moeglich |
| 5 | Besetzung | Anzahl Mitglieder, Wahlmodus, Amtszeit, Wiederwahl | Satzung oder Beiratsordnung regelt |
| 6 | Vergütung | Cash / Optionen / ehrenamtlich; Reisekostenerstattung | Steuerlich relevant; ESOP bei Startup |
| 7 | D&O-Versicherung | Bei Zustimmungsrechten empfohlen | Keine gesetzliche Pflicht; Gestaltung |
| 8 | Schlichtungs-Klausel | Anrufungspflicht vor Klage? Bindungs-Wirkung? | Nicht bindend, aber Verfahrenspflicht möglich |

## Begriffliche Klarheit

### Beirat (deutsch)
- Beratungs- und/oder Kontrollorgan
- Freiwillig bei GmbH
- Befugnisse in Satzung / Beiratsordnung festgelegt

### Advisory Board
- Beratung ohne echte Entscheidungsbefugnis
- Typisch in Startups
- Ehrenamtlich oder gegen Optionen

### Aufsichtsrat
- Bei AG Pflicht (Paragraf 95 AktG)
- Bei mitbestimmter GmbH ab 500 / 2.000 Beschaeftigten Pflicht (DrittelbG, MitbestG)
- Pflicht-Aufgaben: Bestellung Vorstand, Prüfung Jahresabschluss

## Aufgaben (typisch)

### Beratung
- Strategie-Diskussion
- Markt-Trends, Branchen-Expertise
- Personal-Empfehlungen (insbesondere C-Level)

### Aufsicht
- Prüfung Jahresabschluss vor GV
- Risiko-Bewertung
- Compliance-Monitoring
- Bewertung der Geschäftsführer-Leistung

### Schlichtung
- Bei Gesellschafter-Konflikten
- Bei GF-Konflikten
- Vor Anfechtungsklage

### Repraesentation
- Externe Wahrnehmung (PR-Wert)
- Reputations-Traeger (z.B. Branchen-Promis)

## Schritt-fuer-Schritt-Workflow

1. **Triage:** Aufgabe und Rechtsform klaeren; Pflicht-AR pruefen (DrittelbG/MitbestG)
2. **Konzept:** Aufgabenprofil, Besetzungswunsch, Verguetungsmodell festlegen
3. **Satzungs-Klausel entwerfen:** Minimalklausel oder detaillierte Klausel; Notar-Termin einplanen
4. **Beiratsordnung entwerfen:** Meeting-Rhythmus, Quorum, Beschlussfaehigkeit, Protokoll-Pflicht
5. **Beiratsvertraege:** Vertraulichkeit, Verguetung, D&O-Versicherung, Wettbewerbsverbot
6. **Besetzung:** Mitglieder ansprechen, Beschluss der Gesellschafterversammlung herbeiführen
7. **Konstituierende Sitzung:** Vorsitzenden waehlen, Beiratsordnung verabschieden
8. **Monitoring:** Jaehrliche Beirats-Evaluation; Anpassung Beiratsordnung wenn noetig

## Output-Template: Satzungs-Klausel Beirat

**Adressat:** Gesellschaftsvertrag / Satzung GmbH — Tonfall rechtspraezise

```
§ [X] Beirat

(1) Die Gesellschaft hat einen Beirat. Er besteht aus mindestens 3,
hoechstens 7 Mitgliedern.

(2) Die Mitglieder des Beirats werden von der Gesellschafterversammlung
mit einfacher Mehrheit fuer eine Amtszeit von 3 Jahren bestellt.
Wiederbestellung ist zulaessig.

(3) Der Beirat hat folgende Aufgaben:
a) Beratung der Geschaeftsfuehrung in strategischen Fragen,
b) Pruefung des Jahresabschlusses vor Vorlage in der
 Gesellschafterversammlung,
c) Empfehlungen zu Investitionen ueber [SCHWELLENWERT] EUR,
d) Vorabschlichtung bei Gesellschafter-Konflikten.

(4) Folgende Geschaefte beduerfen der Zustimmung des Beirats:
a) Aufnahme von Krediten ueber [BETRAG] EUR,
b) Veraeusserung wesentlicher Aktiva (> 20 % der Bilanzsumme),
c) Eingehung von Joint Ventures,
d) Anstellung und Abberufung von Geschaeftsfuehrern.

(5) Das Naehere regelt die Beiratsordnung, die von der
Gesellschafterversammlung mit [MEHRHEIT] beschlossen wird.

(6) Die Mitglieder des Beirats haften der Gesellschaft gegenueber
bei Verletzung ihrer Pflichten analog § 43 GmbHG.
Zur Absicherung schliessen sie eine D&O-Versicherung ab,
deren Praemie die Gesellschaft traegt.
```

## Output-Template: Beiratsordnung (Kernauszug)

**Adressat:** Interne Beiratsordnung — Tonfall sachlich-juristisch

```
BEIRATSORDNUNG der [FIRMA] GmbH
Stand: [DATUM]

§ 1 Aufgaben und Befugnisse
[wie Satzungs-Klausel Abs. 3 und 4]

§ 2 Zusammensetzung
(1) Der Beirat besteht aus [ANZAHL] Mitgliedern.
(2) Mindestens [N] Mitglieder sind unabhaengig.

§ 3 Sitzungen
(1) Vier regulaere Sitzungen pro Geschaeftsjahr.
(2) Einberufung durch Vorsitzenden mit 1-Wochen-Frist,
 Tagesordnung beifuegen.
(3) Beschlussfaehigkeit: mindestens [N] Mitglieder anwesend.
(4) Beschluesse mit einfacher Mehrheit.

§ 4 Verguetung
(1) Jahresfestbetrag: [BETRAG] EUR fuer Mitglieder,
 [BETRAG] EUR fuer Vorsitzenden.
(2) Sitzungsgeld: [BETRAG] EUR pro Sitzung.
(3) Reisekosten gegen Beleg.

§ 5 Vertraulichkeit
[Klausel: Verschwiegenheit ueber Beratungsgegenstaende]

§ 6 Schlichtungsfunktion
(1) Bei Konflikten zwischen Gesellschaftern ist der Beirat
 vor Klageerhebung anzurufen.
(2) Beirat hat 4 Wochen fuer Schlichtungsvorschlag.
(3) Schlichtungsempfehlung ist nicht bindend.
```

## Output-Template: Advisory Agreement (Startup)

**Adressat:** Advisor (extern) — Tonfall professionell-praegnant

```
ADVISORY AGREEMENT
zwischen [FIRMA] GmbH (Gesellschaft) und [NAME] (Advisor)

Aufgaben:
- Beratung in [BEREICH]
- Vermittlung von Kontakten
- 1 Stunde Call pro Monat; 1 Praesenz-Meeting pro Quartal

Verguetung:
- Option auf [X] % der Anteile (ESOP-Pool)
- Vesting: 25 % nach 12 Monaten Cliff, dann monatlich 1/48
- Bei vorzeitiger Beendigung: nur gevested

Laufzeit: 2 Jahre, Verlaengerung um 1 Jahr automatisch
Kuendigung: 3 Monate vor Ablauf; ausserordentlich aus wichtigem Grund
```

## Rote Schwellen

- Satzungs-Klausel mit Zustimmungsvorbehalten: Notar-Beurkundung der Satzungsaenderung beachten
- Pflicht-Aufsichtsrat bei > 500 AN (DrittelbG) oder > 2.000 AN (MitbestG): nicht durch Beirats-Gestaltung umgehbar
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Zustimmungsvorbehalt entfaltet keine Aussenwirkung gegenüber Dritten (OLG Muenchen 2021)

## Quellen und Vertiefung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- OLG Muenchen, GmbHR 2021, 1056 — Aussenwirkung des Zustimmungsvorbehalts
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 52 GmbHG, §§ 95, 111, 116 AktG, §§ 1, 4 DrittelbG, §§ 1, 7 MitbestG
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsgruender-geschaeftsordnung-gf` — Verzahnung mit GF-Entscheidungskompetenzen
- `gesellschaftsgruender-gesellschaftsvertrag-gmbh` — Satzungs-Klausel Beirat
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Schlichtungs-Funktion vor Eilantrag

<!-- AUDIT 27.05.2026
Geprueft: 3 gemeldete Halluzinationen (task_124.json)
 Behauptetes Thema (Beirat-Vetorechte, Bestellung/Abberufung) entspricht nicht dem Urteilsinhalt.
 Tatsaechliches Thema: Schiedsgericht als Gesellschaftsorgan (Uebertragung von Befugnissen
 der Gesellschafterversammlung), Anfechtungsklage. Quelle: dejure.org/1965,61.
 AZ nicht nachweisbar. Kein Handlungsbedarf in dieser Datei.
 Kein Handlungsbedarf in dieser Datei.
Frontmatter unveraendert. Keine Commit-Aktion.
-->

## 3. `gesellschaftsgruender-bilinguale-dokumente`

**Fokus:** Gesellschaftsrechtliche Dokumente in Deutsch und Englisch erstellen: zweisprachige Satzung, Gesellschafterbeschluss, SHA. Normen: §§ 2 3 GmbHG, HGB. Prüfraster: rechtliche Verbindlichkeit der deutschen Fassung, Abweichungsregelung, Notareignung. Output: Bilinguale Dokumentenvorlage Deutsch-Englisch. Abgrenzung: nicht reine Übersetzung ohne Inhaltsprüfung.

# Bilinguale Dokumente

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bilinguale Dokumente` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Internationale Investoren, ausländische Gesellschafter und grenzüberschreitende M&A-Transaktionen erfordern Gesellschaftsdokumente in zwei Sprachen — regelmäßig Deutsch und Englisch. Dabei gilt im deutschen Rechtsraum: Die deutsche Fassung ist die rechtlich verbindliche; die englische Fassung ist eine "Convenience Translation". Diese Hierarchie muss in jedem Dokument durch eine Sprachvorrang-Klausel ausdrücklich vereinbart werden, sonst drohen Auslegungsstreitigkeiten und Vollstreckungsprobleme.

Dieser Skill unterstützt bei der Erstellung, Qualitätssicherung und Konsistenzprüfung bilingualer Gesellschaftsdokumente: Satzung (Articles of Association), Gesellschaftervereinbarung (Shareholder Agreement / SHA), Geschäftsführeranstellungsvertrag (Managing Director's Agreement), Beiratsordnung (Advisory Board Charter), Term Sheet und Convertible Loan Agreement.

## Kaltstart-Rückfragen

1. **Welche Dokumente?** Satzung, SHA, GF-Anstellungsvertrag, Beiratsordnung, Term Sheet, CLA oder andere?
2. **Welche Sprachen?** Standard: Deutsch/Englisch. Andere Sprachen möglich (Französisch, Mandarin)?
3. **Ausländische Beteiligte?** Wer sind die ausländischen Gesellschafter/Investoren und ihre Muttersprache?
4. **Notarielle Beurkundung erforderlich?** Satzungsänderung, Anteilsabtretung, Kapitalerhöhung: Deutsch zwingend (§ 5 BeurkG).
5. **Bestehende Dokumente?** Liegt die deutsche Masterfassung bereits vor oder wird sie parallel erstellt?
6. **Standard-Glossar vorhanden?** Gibt es ein Kanzlei-Glossar für Standardbegriffe (Class A, Liquidation Preference, Vesting)?
7. **Schiedssprache?** Bei DIS-Schiedsklausel: Schiedsverfahrenssprache festlegen (Deutsch oder Englisch).
8. **Zieldatum?** Notartermin und Signing-Datum festlegen — bestimmt Bearbeitungszeit für Übersetzung und Qualitätssicherung.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte

**§ 184 GVG — Amtssprache**
> "Die Gerichtssprache ist deutsch."

Alle gerichtlichen Verfahren in Deutschland werden in deutscher Sprache geführt. Eingaben in anderen Sprachen sind zu übersetzen. Für die Vollstreckung aus einem englischsprachigen Schiedsspruch in Deutschland ist eine beglaubigte Übersetzung erforderlich (§ 1064 Abs. 3 ZPO).

**§ 5 BeurkG — Sprache der Beurkundung**
> "Die Verhandlung soll in deutscher Sprache geführt werden. Beteiligte, die der deutschen Sprache nicht mächtig sind, müssen einen Dolmetscher hinzuziehen."

Bei Beurkundungsverfahren mit ausländischen Beteiligten: Beurkundung auf Deutsch; Dolmetscher bestellen; Beteiligte erhalten Übersetzung der Urkunde. Die englische Fassung des Satzungstextes ist keine Beurkundungsgrundlage.

**§ 1064 Abs. 3 ZPO — Vollstreckung von Schiedssprüchen**
> Bei der Vollstreckung eines ausländischen Schiedsspruchs ist eine beglaubigte Übersetzung des Schiedsspruchs in die deutsche Sprache beizufügen.

**§§ 133, 157 BGB — Auslegungsgrundsätze**
> § 133 BGB: Bei der Auslegung einer Willenserklärung ist der wirkliche Wille zu erforschen und nicht an dem buchstäblichen Sinne des Ausdrucks zu haften.
> § 157 BGB: Verträge sind so auszulegen, wie Treu und Glauben mit Rücksicht auf die Verkehrssitte es erfordern.

Bei zwei Sprachfassungen ohne Vorrang-Klausel: Widersprüche werden nach §§ 133, 157 BGB ausgelegt — mit erheblicher Unsicherheit. Daher: Vorrang-Klausel zwingend.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Bilinguale Dokumente


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Sprachvorrang-Klausel vorhanden? | Jedes Dokument enthält eine Vorrang-Klausel (DE über EN)? | Ohne Klausel: Auslegungsrisiko bei Widersprüchen |
| 2 | Deutsche Masterfassung vollständig? | Deutsche Fassung ist vollständig und rechtsanwaltlich geprüft bevor Übersetzung beginnt | Übersetzung von unvollständiger Fassung = Doppelaufwand |
| 3 | Juristischer Übersetzer? | Übersetzung durch Translator mit deutschem Recht-Background — nicht maschinelle Übersetzung allein | Maschinelle Übersetzung bei Rechtsbegriffen systematisch unzuverlässig |
| 4 | Glossar-Konsistenz | Sind Fachbegriffe über alle Dokumente einheitlich übersetzt? | Satzung und SHA müssen exakt gleiche Begriffe verwenden (z.B. "Class B" nicht in einem Dokument "Series B") |
| 5 | Notarielle Anforderungen geprüft? | Dolmetscher bei Beurkundung mit Ausländern (§ 5 BeurkG)? | Fehlender Dolmetscher → Unwirksamkeit der Beurkundung |
| 6 | Fachbegriffe dual bezeichnet? | Englische Fachbegriffe die im Deutschen keine exakten Äquivalente haben (Liquidation Preference, Drag-Along) als Doppelbezeichnung? | Z.B. "Liquidation Preference (Liquidationsvorrang)" |
| 7 | Rechtsbegriffe korrekt übertragen? | GmbH ≠ "Limited Liability Company"; GF ≠ "CEO"; HV ≠ "Stockholders Meeting" | Falsche Übersetzung kann Rechtsfolgen verändern |
| 8 | Cross-Reading durchgeführt? | Anwalt liest beide Fassungen parallel und prüft Konsistenz? | Schritt-für-Schritt-Abgleich, Abschnitt für Abschnitt |
| 9 | Schiedsklausel-Sprache festgelegt? | DIS-Klausel: Schiedsverfahrenssprache explizit genannt? | Fehlen der Schiedssprache → Streit über Verfahrenssprache |
| 10 | Behördliche Einreichung auf Deutsch? | Handelsregister, Finanzamt, Transparenzregister: Einreichung ausschließlich auf Deutsch | Englische Fassung wird nicht angenommen |
| 11 | Vollstreckungsübersetzung geplant? | Bei englischsprachigem Schiedsspruch: beglaubigte DE-Übersetzung für Vollstreckung vorbereitet? | § 1064 Abs. 3 ZPO: Pflicht bei Vollstreckungsantrag in Deutschland |
| 12 | Standard-Glossar gepflegt? | Mandatsbezogenes Glossar mit allen Fachbegriffen und ihren EN-Äquivalenten angelegt? | Konsistenz über alle Dokumente; bei Anpassungen einfaches Update |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Welche Sprachfassung gilt bei Widerspruch? | Vertragspartei, die sich auf eine bestimmte Fassung beruft | Ohne Vorrang-Klausel: Auslegung nach §§ 133, 157 BGB; mit Vorrang-Klausel: deutsche Fassung gilt |
| Ordnungsgemäße Dolmetscher-Bestellung bei Beurkundung | Notar (Protokollpflicht nach § 36 BeurkG) | Nachweis durch Beurkundungsprotokoll |
| Übersetzungsfehler liegt vor | Derjenige, der sich auf den Übersetzungsfehler beruft | Vergleich beider Sprachfassungen; ggf. Sachverständigengutachten |
| Anwaltshaftung wegen Auslegungsrisiko | Mandant (Nachweis des Schadens) | Beratungsfehler: kein Hinweis auf fehlende Vorrang-Klausel; Kausalität für Schaden |

## Fristen und Verjährung

| Frist | Norm | Inhalt | Folge |
|---|---|---|---|
| Beurkundung nach Entwurfsfertigstellung | Keine gesetzliche Frist; Notartermin-Vorlauf | Praxis: 2–4 Wochen Vorlauf für Notartermin; bei Ausländern länger (Dolmetscher, Übersetzung) | Terminversäumnis verzögert Closing |
| Übersetzung (juristisch) | Keine gesetzliche Frist | Fachübersetzung 20–50 Seiten: 3–10 Werktage bei qualifiziertem Translator | Engpass bei Zeitdruck |
| Anwaltshaftung für Beratungsfehler | §§ 195, 199 BGB | 3 Jahre ab Kenntnis des Mandanten vom Schaden | Verjährung des Haftungsanspruchs wegen fehlendem Vorrang-Klausel-Hinweis |
| Schiedsspruch-Vollstreckung | § 1064 ZPO i.V.m. § 1061 ZPO (New York Convention) | Antrag auf Vollstreckbarerklärung; beglaubigte Übersetzung beizufügen | Ohne Übersetzung: Antrag unzulässig |

## Typische Übersetzungsfallen

### Gesellschaftsrechtliche Rechtsbegriffe

| Deutscher Begriff | Korrekte EN-Übersetzung | Häufiger Fehler |
|---|---|---|
| GmbH | GmbH (in Klammern: Gesellschaft mit beschränkter Haftung) oder "limited liability company under German law" | "LLC" — falsch, weil LLC ein US-amerikanisches Konstrukt ist |
| Geschäftsführer | Managing Director | "CEO", "Director" — nicht rechtsgenau; CEO ist kein Rechtsbegriff |
| Gesellschafterversammlung | Shareholders' Meeting oder General Meeting | "Stockholders Meeting" — US-Terminologie |
| Stammkapital | Share capital | "Stock capital" — ungebräuchlich im englischen GmbH-Kontext |
| Satzung | Articles of Association | "Articles of Incorporation" — US-Terminologie; "Statute" mehrdeutig |
| Einziehung von Anteilen | Redemption of shares | "Cancellation" — Nuance: Einziehung nach § 34 GmbHG ist Sonderfall |
| Gesellschaftervereinbarung | Shareholders' Agreement (SHA) | "Partnership Agreement" — falsch; GmbH ist keine Partnership |
| Handelsregistereintragung | Commercial Register registration | "Corporate filing" — zu unspezifisch |
| Jahresabschluss | Annual financial statements | "Annual report" — zu weit; Annual report umfasst mehr als Jahresabschluss |
| Prokura | Commercial power of attorney / Prokura | Keine exakte EN-Entsprechung; "Prokura" im Klammern behalten |

### Startup-Terminologie

| Begriff | Standard DE | Standard EN | Kommentar |
|---|---|---|---|
| Liquidation Preference | Liquidationsvorrang | Liquidation Preference | Englischer Begriff im deutschen Kontext etabliert; Doppelbezeichnung empfohlen |
| Drag-Along | Mitziehverpflichtung | Drag-Along Obligation | Beide Fassungen verwenden; englischer Begriff als Kurzbezeichnung |
| Tag-Along | Mitveräußerungsrecht | Co-Sale Right oder Tag-Along Right | Co-Sale Right juristisch präziser im Britischen Englisch |
| Anti-Dilution | Verwässerungsschutz | Anti-Dilution Protection | Broad-Based Weighted Average: "gewichteter Mittelwert (breite Basis)" |
| Vesting | Erdienen von Anteilen | Vesting | Cliff: "Cliff-Periode" oder "Anlaufphase"; 1-year cliff: 12-monatige Cliff-Periode |
| Bad Leaver | Schlechter Aussteiger | Bad Leaver | Begriff wird auf Englisch verwendet; DE-Erläuterung im Vertrag |
| ESOP | Mitarbeiterbeteiligungsprogramm | Employee Share Option Plan (ESOP) | VSOP (Virtual Share Option Plan): "virtuelles Mitarbeiterbeteiligungsprogramm" |
| Pre-Money Valuation | Bewertung vor der Finanzierungsrunde | Pre-Money Valuation | Kein übliches deutsches Äquivalent; englischer Begriff |
| Term Sheet | Eckpunktepapier / Term Sheet | Term Sheet | Term Sheet nicht verbindlich (i.d.R.); Letter of Intent (LOI) verbindlicher |
| Cap Table | Beteiligungsübersicht | Capitalisation Table (Cap Table) | Cap Table als Kurzbezeichnung auch auf Deutsch üblich |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Bilinguales Dokument erstellen Deutsch-Englisch | Bilinguale Vorlage nach Vorrang-Klausel-Schema; Template unten |
| Variante A — Nur eine Sprache rechtlich bindend | Monolinguales Kerndokument mit Uebersetzung zur Information |
| Variante B — Fremdrechts-Bezug notwendig Governing Law noetig | Rechtswahl-Klausel und Gerichtsstand explizit regeln |
| Variante C — Mandant will nur interne Verwendung kein Vollzug noetig | Vereinfachte Uebersetzung ohne juristische Bindefassung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Sprachvorrang-Klausel (vollständig, für alle Dokumenttypen)

```
§ [X] Sprache / Language

(1) Diese [Vereinbarung / Satzung / der vorliegende Vertrag] ist in deutscher und
englischer Sprache abgefasst. Bei Widersprüchen oder Auslegungszweifeln zwischen
den beiden Sprachfassungen geht der deutsche Text vor. Soweit eine notarielle
Beurkundung nach § 2 GmbHG oder § 15 GmbHG erforderlich ist, ist allein die deutsche
Fassung Beurkundungsgrundlage; die englische Fassung dient lediglich als
"Convenience Translation".

(2) This [Agreement / Articles of Association / Agreement] is executed in German and
English language. In case of any discrepancies or doubts of interpretation between
the two language versions, the German version shall prevail. Where notarial recording
pursuant to § 2 GmbHG or § 15 GmbHG is required, only the German version shall
constitute the basis of the notarial deed; the English version serves as a
convenience translation only.

Grundlage: § 184 GVG (Amtssprache Deutsch); § 5 BeurkG (Beurkundungssprache);
§ 1064 Abs. 3 ZPO (Vollstreckung).
```

### Baustein 2: Term Sheet bilingual (strukturiertes Muster)

```
TERM SHEET / ECKPUNKTEPAPIER
[Gesellschaft] — Series A Finanzierungsrunde

Dieses Term Sheet ist nicht verbindlich, soweit nicht ausdrücklich anders vermerkt.
This Term Sheet is non-binding, unless expressly stated otherwise.

---------------------------------------------------------------------------
DEUTSCH | ENGLISCH
---------------------------------|--------------------------------------------
Gesellschaft / Company | [Firma] GmbH, [Sitz], HRB [Nr.]
Investor / Investor | [Investor Name], [Adresse]
Investitionsbetrag / | EUR [X]
Investment Amount |
Pre-Money Bewertung / | EUR [Y]
Pre-Money Valuation |
Post-Money Bewertung / | EUR [Y+X]
Post-Money Valuation |
Neue Anteile / New Shares | [N] Class B Geschäftsanteile (Class B Shares)
Anteil Investor / | [Z] %
Investor's Stake |
---------------------------------|--------------------------------------------
RECHTE DES INVESTORS | INVESTOR RIGHTS
Liquidationsvorrang / | 1x non-participating Liquidation Preference
Liquidation Preference |
Verwässerungsschutz / | Weighted Average Broad-Based Anti-Dilution
Anti-Dilution |
Sondervetorechte / | Veto rights on: [Aufzählung / List]
Special Veto Rights |
Drag-Along Schwelle / | 75 % der Stimmrechte / of voting rights
Drag-Along Threshold |
Tag-Along / Co-Sale Right | Pro rata bei Kontrollwechsel / on change of control
---------------------------------|--------------------------------------------
GRÜNDER-RECHTE | FOUNDER RIGHTS
Vesting-Periode / | 48 Monate / months, 12 Monate Cliff / month cliff
Vesting Period |
Bad Leaver: unvested Anteile / | Zum Nennwert / at nominal value
Bad Leaver: unvested shares |
Good Leaver: unvested Anteile / | Zum Verkehrswert / at fair market value
Good Leaver: unvested shares |
---------------------------------|--------------------------------------------
MITARBEITER-POOL / ESOP Pool | 10 % (pre-money) reserviert / reserved
---------------------------------|--------------------------------------------
SONSTIGES / OTHER
Schiedsklausel / Arbitration | DIS, Berlin, Deutsch / German
Anwendbares Recht / | Deutsches Recht / German law
Governing Law |
Exklusivität / Exclusivity | [N] Wochen / weeks ab Unterzeichnung / from signing
Kosten / Costs | Eigene Kosten / own costs

Bei Inkonsistenzen: deutsche Fassung geht vor.
In case of inconsistencies: German version prevails.
```

### Baustein 3: Draaft-Along-Klausel bilingual (vollständiges Muster)

```
§ [Y] Mitziehverpflichtung (Drag-Along) / Drag-Along Obligation

DEUTSCH:
(1) Stimmen Gesellschafter, die zusammen mindestens 75 % der Stimmrechte an der
Gesellschaft halten ("Drag-Along-Initiatoren"), einem Verkauf sämtlicher
Geschäftsanteile an der Gesellschaft an einen Dritten zu, können sie die übrigen
Gesellschafter verpflichten, ihre Anteile zu denselben Bedingungen mitzuveräußern.

(2) Die Mitziehverpflichtung gilt nur, wenn:
a) der Verkaufspreis pro Anteil für alle Gesellschafter gleich ist;
b) der Erwerber kein verbundenes Unternehmen eines Initiators ist;
c) keine Gegenleistung disproportional zugunsten einzelner Initiatoren ist.

(3) Mitzieh-pflichtige Gesellschafter sind schriftlich mit einer Frist von
mindestens 30 Tagen zu informieren.

------

ENGLISH:
(1) If Shareholders holding in aggregate at least 75 % of the voting rights in the
Company ("Drag-Along Initiators") agree to a sale of all shares in the Company to a
third party, they may oblige the remaining Shareholders to co-sell their shares on
the same terms.

(2) The drag-along obligation shall only apply if:
a) the sales price per share is the same for all Shareholders;
b) the purchaser is not an affiliated company of any Initiator;
c) no consideration is disproportionately in favor of individual Initiators.

(3) Drag-bound Shareholders shall be notified in writing with a notice period of
at least 30 days.

------
Bei Widersprüchen geht die deutsche Fassung vor.
In case of discrepancies, the German version shall prevail.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Standard-Glossar (Musterformat für Mandatsakte)

```
STANDARD-GLOSSAR — [Mandant] — [Datum]
Gilt für alle Dokumente in diesem Mandat.

| Deutsch | Englisch | Anmerkung |
|-----------------------------|----------------------------------|-----------|
| Gesellschaft | Company | |
| Geschäftsanteile | Shares / Share capital | |
| Stammkapital | Share capital | Nicht "Stock capital" |
| Stammeinlage | Share contribution | |
| Gesellschafter | Shareholder | Nicht "Stockholder" (US) |
| Gesellschafterversammlung | Shareholders' Meeting | |
| Geschäftsführer | Managing Director | Nicht "CEO" |
| Satzung | Articles of Association | Nicht "Statute" |
| Gesellschaftervereinbarung | Shareholders' Agreement (SHA) | |
| Klasse A Anteile | Class A Shares | |
| Klasse B Anteile | Class B Shares | |
| Liquidationsvorrang | Liquidation Preference | |
| Verwässerungsschutz | Anti-Dilution Protection | |
| Mitziehverpflichtung | Drag-Along Obligation | |
| Mitveräußerungsrecht | Co-Sale Right (Tag-Along) | |
| Vesting-Periode | Vesting Period | |
| Cliff-Periode | Cliff Period | |
| Schlechter Aussteiger | Bad Leaver | |
| Guter Aussteiger | Good Leaver | |
| Bezugsrecht | Pre-emption Right | |
| Beirat | Advisory Board | |
| Jahresabschluss | Annual Financial Statements | |
| Handelsregister | Commercial Register | |
| Transparenzregister | Transparency Register | |
```

## bei bilingualer Erstellung

### Schritt 1: Deutsche Masterfassung

Erstellung der vollständigen deutschen Fassung; rechtsanwaltliche Prüfung und Freigabe.

### Schritt 2: Englische Übersetzung

Durch juristisch versierten Übersetzer mit deutschem Recht-Hintergrund — nicht allein durch maschinelle Übersetzung. Maschinenübersetzung (DeepL, ChatGPT) kann als Rohfassung dienen, aber zwingend qualitätskontrolliert werden.

### Schritt 3: Cross-Reading

Anwalt liest beide Fassungen parallel; Abgleich Abschnitt für Abschnitt. Bei Inkonsistenzen: deutsche Fassung anpassen oder Vorrang-Klausel explizit stärken.

### Schritt 4: Vorrang-Klausel einfügen

Standardklausel (Baustein 1) in alle Dokumente einfügen. Platzierung: § 1 oder letzter Abschnitt vor Unterschriften.

### Schritt 5: Notarielle Beurkundung (soweit erforderlich)

Beurkundung auf Deutsch (§ 5 BeurkG). Bei ausländischen Beteiligten: Dolmetscher beauftragen. Beide Fassungen werden unterzeichnet; deutsche bleibt verbindlich.

### Schritt 6: Glossar-Pflege

Mandatsbezogenes Glossar nach jeder Dokumenterstellung aktualisieren; für alle Folgedokumente konsistent verwenden.

## Behördeneinreichung und Schiedsverfahren

### Behördliche Einreichungen

Handelsregister, Finanzamt, Gewerbeamt, Transparenzregister: **ausschließlich auf Deutsch**. Englische Fassung wird nicht angenommen. Bei automatischen Einreichungstools: Sprache prüfen.

### Schiedsverfahren (DIS)

Bei DIS-Schiedsklausel: Schiedsverfahrenssprache explizit im Vertrag nennen. Standard: Deutsch. Bei Englisch als Schiedssprache: Vollstreckungsübersetzung für Deutschland vorbereiten (§ 1064 Abs. 3 ZPO). DIS-Notschiedsverfahren bei Eilbedarf möglich.

## Streitwert und Kosten

| Leistung | Kostenrahmen | Anmerkung |
|---|---|---|
| Juristische Übersetzung Satzung (15–20 Seiten) | 500–1.500 EUR | Abhängig von Stundensatz des Übersetzers (120–200 EUR/Std.) |
| Juristische Übersetzung SHA (30–60 Seiten) | 1.000–4.000 EUR | Komplexe Klauseln (Liquidation Preference, Anti-Dilution) erhöhen Aufwand |
| Dolmetscher bei Notarbeurkundung | 300–800 EUR (halber Tag) | Vereidigter Dolmetscher; Notargebühren zzgl. |
| Beglaubigte Übersetzung Schiedsspruch | 200–800 EUR | Je nach Seitenumfang; für § 1064 Abs. 3 ZPO erforderlich |
| Anwaltliche Qualitätskontrolle (Cross-Reading) | 500–2.000 EUR | 2–4 Stunden bei 200–400 EUR/Std. |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| US-amerikanischer Investor besteht auf englischsprachigem Dokument | Bilinguale Fassung mit strikter Vorrang-Klausel (DE über EN); US-Investor bekommt Comfort durch englische Fassung, Rechtsicherheit bleibt beim deutschen Text |
| Term Sheet-Verhandlung mit ausländischem VC | Term Sheet bilingual; non-binding, außer explizit markierten Punkten; keine Signing-Kosten durch Notar in diesem Stadium |
| Schiedsverfahren auf Englisch gewünscht | DIS bietet englisches Verfahren an; aber: für Vollstreckung in Deutschland DE-Übersetzung des Schiedsspruchs zwingend (§ 1064 Abs. 3 ZPO) |
| Mandant nutzt Online-Übersetzungstool | DeepL / ChatGPT als Rohfassung akzeptabel; aber zwingend juristische Qualitätskontrolle vor Verwendung; maschinelle Fachterm-Übersetzung bei GmbH-Recht fehlerhaft |
| Konsistenz über mehrere Dokumente hinweg | Standard-Glossar anlegen und für alle Folgedokumente verbindlich machen; Abweichungen dokumentieren |

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template: Vorrang-Klausel (einzusetzen in alle Dokumente)

**Adressat:** Vertrag oder Satzung mit ausländischen Beteiligten — Tonfall praezise-juristisch

```
§ [X] Sprache / Language

(1) Diese [Vereinbarung / Satzung / der vorliegende Vertrag] ist in
deutscher und englischer Sprache abgefasst. Bei Widerspruechen oder
Auslegungszweifeln zwischen den Sprachfassungen geht der deutsche
Text vor. Soweit eine notarielle Beurkundung nach § 2 GmbHG oder
§ 15 GmbHG erforderlich ist, ist allein die deutsche Fassung
Beurkundungsgrundlage; die englische Fassung dient als
"Convenience Translation".

(2) This [Agreement / Articles of Association] is executed in German
and English. In case of discrepancies, the German version prevails.
Where notarial recording pursuant to § 2 GmbHG or § 15 GmbHG is
required, only the German version constitutes the basis of the
notarial deed; the English version serves as a convenience
translation only.
```

## Output-Template: Qualitaetscheckliste fuer bilinguale Dokumente

**Adressat:** Interne Qualitaetskontrolle — Tonfall sachlich

```
QUALITAETS-CHECKLISTE BILINGUALE DOKUMENTE
Mandat: [MANDANT] | Dokument: [TYP] | Datum: [DATUM]

[ ] Vorrang-Klausel eingefuegt (DE ueber EN)
[ ] Deutsche Masterfassung vollstaendig und geprueft
[ ] Uebersetzung durch juristisch versierten Uebersetzer
[ ] Cross-Reading (beide Fassungen parallel gelesen)
[ ] Glossar-Konsistenz geprueft (alle Dokumente einheitlich)
[ ] Notarielle Anforderungen: Dolmetscher bei Auslaendern (§ 5 BeurkG)?
[ ] Behörden-Einreichungen nur auf Deutsch
[ ] Schiedssprache explizit vereinbart (falls DIS-Klausel)
[ ] Vollstreckungsuebersetzung vorgeplant (§ 1064 Abs. 3 ZPO)?
[ ] Mandatsglossar aktualisiert
```

## Rote Schwellen

- Kein Dolmetscher bei Beurkundung mit sprachunkundigen Auslaedern: Nichtigkeit (§ 5 BeurkG; OLG Frankfurt 2019)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Ausschliesslich englischsprachige Einreichung beim Handelsregister, Finanzamt: wird nicht angenommen
- Schiedsspruch auf Englisch ohne Uebersetzung: Vollstreckungsantrag in Deutschland unzulaessig (§ 1064 Abs. 3 ZPO)

## Anschluss-Skills

- `gesellschaftsgruender-klauselkatalog-bilingual` — Volltext-Klauseln DE/EN fuer alle Klauseltypen
- `gesellschaftsgruender-intake-decision-tree` — Workflow-Steuerung mit bilingualer Ausgabe
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — Eilantraege in Deutsch (Gerichtssprache)
- `gesellschaftsgruender-rechtsformwahl` — Rechtsform bestimmt Dokumenttypen

## Quellen und Vertiefung

- § 184 GVG (Amtssprache Deutsch)
- § 5 BeurkG (Beurkundungssprache; Dolmetscher-Pflicht)
- §§ 133, 157 BGB (Auslegungsgrundsaetze)
- § 1064 Abs. 3 ZPO (Vollstreckung auslaendischer Schiedsspruche; Uebersetzungspflicht)
- § 1061 ZPO i.V.m. New York Convention (Anerkennung auslaendischer Schiedsspruche)
- Limmer/Hertel/Frenz/Mayer, Wuerzburger Notarhandbuch, 6. Aufl. 2021, Teil 3 Kap. 2 Rn. 45 ff.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Aktion: Beide Einträge (Leitentscheidungen-Tabelle und Aktuelle Rechtsprechung) gelöscht.
-->

## 4. `gesellschaftsgruender-board-pack-erste-100-tage`

**Fokus:** Erstellt Board-/Beiratsunterlagen für die ersten 100 Tage nach Gründung.

# Board Pack erste 100 Tage

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Board Pack erste 100 Tage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
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

KPIs, Beschlüsse, Risiken, Cash, Hiring, Compliance.

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

## 5. `gesellschaftsgruender-cap-table`

**Fokus:** Cap-Table für GmbH oder UG aufbauen und pflegen: Stammkapital, Gesellschafteranteile, Verwässerungsschutz. Normen: §§ 3 5 14 GmbHG. Prüfraster: aktuelle Anteile, Optionspools, Wandeldarlehen, Vesting-Schedule. Output: Cap-Table-Tabelle mit Anteilsuebersicht und Verwässerungsrechnung. Abgrenzung: nicht Gründungsprotokoll oder Handelsregisteranmeldung.

# Cap Table

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
