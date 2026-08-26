# DBA-Länderprüfung: A-B

Diese Datei wird nur geladen, wenn der konkrete Vorgang in diese Fallgruppe fällt.

## DBA-Ländermatrix 2026

Auswahlsignal: Wenn es um DBA-Ländermatrix 2026 in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### DBA-Ländermatrix 2026

#### Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DBA-Ländermatrix 2026` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

#### Einstieg

1. Welche Staaten sind beteiligt?
2. Welcher Veranlagungszeitraum oder Zahlungszeitpunkt?
3. Welche Einkunftsart?
4. Natürliche Person, Kapitalgesellschaft, Personengesellschaft, Stiftung, Fonds oder Betriebsstätte?
5. Geht es um Quellensteuer, Veranlagung, Lohnsteuer, Erbschaftsteuer, Amtshilfe oder Streitbeilegung?
6. Gibt es EU/EWR-Bezug, MLI, Russland/Belarus/VAE-Status oder Alt-DBA?
7. Muss das DBA nur eine nationale Steuerbarkeit begrenzen oder ist die DBA-Zuweisung selbst Tatbestandsbaustein in § 49 Abs. 1 Nr. 4 Buchst. a Satz 2 EStG?

#### Workflow

1. Matrix öffnen und Staat zuordnen.
2. Prüfen, ob bereits länderspezifischer Skill existiert.
3. Falls ja: diesen laden und mit Matrix gegenprüfen.
4. Falls nein: `stb-dba-regionenrouter-nichteu` und `stb-dba-all-country-memo-generator` verwenden.
5. Bei Quellensteuer zusätzlich `stb-dba-quellensteuer-atlas-weltweit`.
6. Bei Doppelbesteuerung trotz DBA zusätzlich `stb-dba-map-eu-streitbeilegung`.
7. Bei beschränkt Steuerpflichtigen mit § 49-EStG-Inlandsanknüpfung zusätzlich `dba-49-estg-brueckentatbestand-nationalrecht` laden, wenn Art. 13 Abs. 4 OECD-MA, Art. 15 OECD-MA, Homeoffice-Tage oder Immobiliengesellschaften den Fall tragen.

#### Quellenpflicht

Keine Quellensteuersätze, Grenzgängergrenzen, Pensionsschwellen oder MLI-Wirkungen aus dem Gedächtnis. Immer DBA-Text und BMF/BZSt/OECD-Status prüfen.

DBA-Matrix nie als Steuerbegründung verwenden. Für jede beschränkte Steuerpflicht zuerst den nationalen Hook nennen: etwa § 49 Abs. 1 Nr. 2 Buchst. e Doppelbuchst. cc EStG bei real-estate-rich-Anteilen oder § 49 Abs. 1 Nr. 4 Buchst. a Satz 2 EStG bei Homeoffice-/Auslandstätigkeitstagen, für die das konkrete DBA Deutschland ein Besteuerungsrecht zuweist.

#### Praktiker-Tipps "Schnell zum Bescheid"

- **Matrix als Ausgangspunkt, DBA-Text als Endpunkt**: nie eine Mandantenanfrage allein auf Basis der Matrix beantworten — DBA-Text in der BGBl-II-Fundstelle ist verbindlich. Im Memo immer BGBl-Stelle nennen.
- **Schnellnavigation auf bundesfinanzministerium.de**: "Internationales Steuerrecht > Doppelbesteuerung > Liste der Staaten mit DBA" — pro Land PDF zum Originaltext + Änderungsprotokolle + Konsultationsvereinbarungen.
- **MLI-Status getrennt zum DBA prüfen**: OECD-MLI-Matching-Database (oecd.org/tax/treaties/mli-matching-database.htm) zeigt, welche Klauseln des MLI bei einem konkreten DBA durchschlagen. Wirksamkeitsdatum pro Norm separat.
- **Russland-Suspendierung 30.12.2023**: bis auf weiteres keine BZSt-Entlastung; Memo entsprechend kennzeichnen (siehe `stb-dba-russland-suspendierung-2024`).
- **VAE und Saudi-Arabien**: kein umfassendes DBA (kuendigung VAE 31.12.2021; Saudi-Arabien nicht im Einkommensteuer-DBA-Netz). Nur Spezialabkommen prüfen.
- **Belarus / Iran / Syrien**: Sanktionsrechtliche Beschraenkungen (EU-Sanktionsregimes) gehen DBA vor — prüfen.
- **Ehemalige UdSSR-Staaten**: einzelne DBA mit Fortwirkung (Russland, Ukraine, Belarus, Kasachstan, Usbekistan, Aserbaidschan etc.); prüfen, ob nationales Recht der Fortwirkung folgt.
- **Ehemalige Jugoslawien-Staaten**: Fortwirkung Jugoslawien-DBA für Bosnien-Herzegowina, Nordmazedonien, Kosovo; eigene DBA für Slowenien, Kroatien, Serbien-Montenegro, Albanien — Fortgeltung im Einzelfall.

#### Trade-off-Tabelle

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| Allgemeiner Skill (dieser) vs. Landeseinzel-Skill | Routing über Matrix; Hinweis auf live Prüfung | Detail-Skill mit Subsumtion | bei vorhandenem Landeseinzel-Skill immer diesen vorziehen |
| Drittstaat ohne aktuellen DBA-Text | Memo mit "kein DBA / DBA suspendiert" prüfen | Fachmodul (Russland, Belarus, VAE) | bei Sonderlagen Fachmodul nutzen |
| MLI-modifiziertes DBA vs. unmodifizierter DBA-Text | OECD-MLI-Synopse abrufen | nur DBA-Text | bei Veranlagungszeitraum ab 2019/2020 stets MLI-Synopse abrufen |

#### Was Reviewer/Prüfer triggert

- **Memo schreibt "DBA gilt", ohne BGBl-Stelle zu nennen**.
- **MLI-Status nicht erwaehnt**, obwohl beide Staaten ratifiziert haben und Wirksamkeitsdatum erreicht ist.
- **Fortwirkungs-DBA (UdSSR/Jugoslawien) nicht geprueft** bei Nachfolgestaaten.
- **Suspendierung Russland uebersehen** für Veranlagungszeitraeume ab 2024.
- **Sanktionsrecht (EU, US-OFAC, BAFA) nicht beruecksichtigt** bei Iran, Belarus, Russland.
- **Erbschaftsteuer-DBA mit Einkommensteuer-DBA verwechselt** — getrennte Abkommensreihen.
- **EU/EWR-Status falsch**: Norwegen/Island/Liechtenstein sind EWR, aber nicht EU — MTRL/ZinsLizenzRL gelten nicht direkt.

#### Routing-Beispiel (Mustertabelle)

| Mandanten-Frage | Staat | Einkunftsart | Empfohlener Skill (Hauptpfad) | Querverweis |
|---|---|---|---|---|
| GmbH zahlt Dividende an US-Holding | USA | Dividenden | `stb-dba-usa-1989-protokoll-2006` | `stb-dba-dividenden-quellensteuer-art-10`, `stb-dba-quellensteuer-erstattung-bzst-50c-estg` |
| Grenzgaenger CH mit 70 Home-Office-Tagen | Schweiz | Arbeitslohn | `stb-dba-grenzgaenger-schweiz-60-tage-rueckkehr` | `stb-dba-home-office-pandemie-folgeregelung` |
| Lizenz von DE an irische Konzerngesellschaft | Irland | Lizenzen | `stb-dba-irland` | `stb-dba-lizenzgebuehren-art-12-bzst` |
| Rente Wohnsitz Portugal NHR | Portugal | Pensionen | `stb-dba-portugal` | `stb-dba-rentner-pensionen-art-18` |
| BS-Bauausfuehrung Tuerkei | Tuerkei | Unternehmensgewinn | `stb-dba-tuerkei-2011` | `stb-dba-betriebsstaette-art-5-musterabkommen` |
| Drittland ohne Fachmodul (z.B. Mexiko) | Mexiko | Diverse | `stb-dba-regionenrouter-nichteu` + `stb-dba-all-country-memo-generator` | DBA-Text bundesfinanzministerium.de |
| Beschränkt steuerpflichtiger Share Deal an deutscher Immobiliengesellschaft | DBA-Staat des Veräußerers | Veräußerungsgewinn | `dba-49-estg-brueckentatbestand-nationalrecht` | Art. 13 Abs. 4 OECD-MA, § 49 Abs. 1 Nr. 2 Buchst. e Doppelbuchst. cc EStG |
| Homeoffice-Tage im Ansässigkeitsstaat mit deutschem Besteuerungsrecht | DBA-Staat des Arbeitnehmers | Arbeitslohn | `dba-49-estg-brueckentatbestand-nationalrecht` | `stb-dba-home-office-pandemie-folgeregelung`, Art. 15 OECD-MA |

#### Output (erweitert)

- **DBA-Routingblatt**: Staat, Zeitraum, Abkommensart, BGBl-Stelle, MLI-Status, Fortwirkung.
- **Liste der anzuwendenden Artikel** mit Verweis auf Originaltext.
- **Noch live zu prüfende Punkte**: BMF-Schreiben, MLI-Notifications, Konsultationsvereinbarungen.
- **Empfohlene Folgeskills** (Hauptpfad + Querskill).
- **Warnhinweis** bei Sanktionsrechts-Bezug, Suspendierung, Fortgeltung.

#### Konkretes Routingbeispiel: Verfahrensweg pro Konstellation

| Sachverhaltstyp | Erste Anlaufstelle (Skill) | Querverweis |
|---|---|---|
| Quellensteuer-Erstattung | `stb-dba-quellensteuer-erstattung-bzst-50c-estg` | `stb-dba-dividenden-quellensteuer-art-10`, `stb-dba-lizenzgebuehren-art-12-bzst` |
| BS im Ausland | `stb-dba-betriebsstaette-art-5-musterabkommen` | Land-Skill, `stb-dba-anrechnung-vs-freistellung-methodenartikel-freistellung` |
| Wegzug § 6 AStG | `stb-dba-ansaessigkeit-tie-breaker-rules` | Land-Skill, `stb-dba-rentner-pensionen-art-18` |
| Doppelbesteuerung trotz DBA | `stb-dba-map-eu-streitbeilegung` | `stb-dba-grundprinzip-oecd-musterabkommen` |
| Hybridgesellschaft (LLC, LP) | `stb-dba-edge-cases-playbook` | Land-Skill, `stb-dba-grundprinzip-oecd-musterabkommen` |
| Home-Office-Grenzgaenger | `stb-dba-home-office-pandemie-folgeregelung` | Land-Grenzgaenger-Skill |
| § 49-EStG-Brückentatbestand / DBA zuerst im nationalen Tatbestand | `dba-49-estg-brueckentatbestand-nationalrecht` | Art. 13 Abs. 4 OECD-MA, Art. 15 OECD-MA, § 49 Abs. 1 Nr. 2 Buchst. e Doppelbuchst. cc EStG, § 49 Abs. 1 Nr. 4 Buchst. a Satz 2 EStG |
| Kuenstler/Sportler-Auftritt | `stb-dba-kuenstler-sportler-art-17-ma` | `stb-dba-quellensteuer-erstattung-bzst-50c-estg` |
| Drittstaat ohne Fachmodul | `stb-dba-regionenrouter-nichteu` + `stb-dba-all-country-memo-generator` | `stb-dba-quellensteuer-atlas-weltweit` |

#### Vorgehen bei nicht gefundenen Fachmodule

1. **Matrix abrufen** und Staat eintragen.
2. **DBA-Text** über bundesfinanzministerium.de beziehen.
3. **MLI-Status** über OECD-Matching-Database prüfen.
4. **Regionenrouter-Skill** als Pfad B nutzen.
5. **All-Country-Memo-Generator** für das Memo selbst.
6. **Querverweis auf relevante Querschnitts-Skills** (Methodenartikel, Quellensteuer, MAP).
## DBA Deutschland-Belgien

Auswahlsignal: Wenn es um DBA Deutschland-Belgien in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### DBA Deutschland-Belgien

#### Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DBA Deutschland-Belgien` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

#### Kernsachverhalt

Das DBA-Belgien regelt unter anderem die deutschsprachige Gemeinschaft (Eupen, Malmedy, St. Vith) und ihre besondere Pendler-Konstellation. Praxisrelevant sind Lohneinkuenfte, Beteiligungs- und Lizenzeinkuenfte, sowie die Holdingaktivitaeten belgischer Gesellschaften (DBI-Regelung in Belgien als Äquivalent zur deutschen Schachtelprivilegierung).

#### Kaltstart-Rueckfragen

1. Welcher Wohnsitzstaat, welche Einkunftsart?
2. Arbeitnehmer mit belgischem Wohnsitz oder deutsch-belgische Doppel-Ansaessigkeit?
3. Tage-Zaehlung 183-Tage-Regelung?
4. Bei Beteiligung: Höhe, Holding-Substanz?
5. Bauausfuehrung welcher Dauer?
6. Liegt belgische Ansaessigkeitsbescheinigung vor (Form 276)?
7. Pension aus belgischer Pensionskasse? Öffentlich oder privat?
8. MLI-Anpassungen relevant?

#### Rechtlicher Rahmen

##### Primaernormen

- **DBA Deutschland-Belgien vom 11.04.1967** (BGBl. 1969 II S. 17/18), Zusatzabkommen 05.11.2002 (BGBl. 2003 II S. 1616), Änderungsprotokoll 21.01.2010 (BGBl. 2010 II S. 1279).
- **OECD-MA 2017** als Auslegungshilfe.
- **§§ 34c, 32b, 50d EStG**, § 20 AStG.
- **MLI**: Deutschland und Belgien sind Unterzeichnerstaaten — konkrete Notification-Listen beim OECD-MLI-Status-Portal prüfen.

##### Leitentscheidungen und BMF-Schreiben

- Aktuelle BFH-Rechtsprechung zu DBA-Belgien in freier amtlicher Quelle abrufen.
- BMF-Schreiben zu DBA Belgien — aktuellen Stand im BMF-Veroeffentlichungsverzeichnis prüfen.

#### Land-spezifisches

##### Ansaessigkeit (Art. 4)

- Tie-Breaker.
- Konstellation Bruessel-Beamte (EU-Bedienstete) gesondert: Wohnsitz in Belgien aber EU-Protokoll bestimmt Steuerbefreiungen.

##### Betriebsstaette (Art. 5)

- Bauausfuehrung **12 Monate** Standard.

##### Aktive Einkuenfte

- Loehne (Art. 15): 183-Tage-Regel.
- Achtung: Es gab in den 1960er-DBA für Belgien eine **echte Grenzgaengerregelung** in den Grenzbezirken (Aachen, Eupen, Malmedy). Diese wurde durch Änderungsprotokolle abgeschafft und durch eine Sonderregelung in den Grenzgemeinden ersetzt — aktuellen Protokoll-Stand im konsolidierten DBA-Text prüfen.

##### Passive Einkuenfte

- **Dividenden** (Art. 10): typ. 5/15 Prozent — massgebend ist Art. 10 DBA-Belgien in der jeweils geltenden Fassung.
- **Zinsen** (Art. 11): typ. 0/15 Prozent — massgebend ist Art. 11 DBA-Belgien in der jeweils geltenden Fassung.
- **Lizenzgebuehren** (Art. 12): typ. 0 Prozent — massgebend ist Art. 12 DBA-Belgien in der jeweils geltenden Fassung.

##### Vermeidungs-Methode (Art. 23)

- Freistellung mit Progressionsvorbehalt bei aktiven Einkuenften.
- Anrechnung bei passiven Einkuenften.

##### Besonderheiten

- **Pensionen**: Sonderregelung in DBA, **konkret prüfen**.
- **Sportler**: gesonderte Art. 17 — Quellensteuer beim Auftrittsort.
- **EU-Bedienstete**: Privileg des Protokolls 7 EUV bzw. EU-Bedienstetengesetz; Wohnsitz vor Dienstantritt zaehlt fiktiv weiter — § 14 EU-BeamtenStG.

#### Workflow

##### Phase 1 — DBA-Anwendbarkeit
1. Anwendbares DBA und Protokollstand.

##### Phase 2 — Ansaessigkeit klären
1. Bei EU-Beamten: Sonderfiktion beachten.

##### Phase 3 — Einkunftsart einordnen
1. Lohn Pension Beteiligung.

##### Phase 4 — Verteilungs- und Methodenartikel
1. 183-Tage-Prüfung; Quellensteuer-Hoechstsatz.

##### Phase 5 — Erstattung / Erklaerung
1. BZSt-Antrag bei Beteiligungseinkuenften.
2. Anlage AUS / N-AUS / R-AUS.

#### Strategie und Praxis-Tipps

- DBA-Belgien war fruehe Generation; Begriffe entsprechen nicht in allen Punkten dem OECD-MA 2017 — Protokolle vollstaendig durchgehen.
- Belgische DBI (Definitief Belaste Inkomsten) ist nationales Äquivalent zur Schachtelprivilegierung — Verhältnis zu deutscher § 8b KStG-Befreiung beachten.
- Pensionen Art. 18 DBA-Belgien: Spezialregelung in einigen Fallgruppen vom OECD-Standard abweichend — aktuellen DBA-Text und BMF-Schreiben prüfen.
- 183-Tage-Regelung: Kalenderjahr oder 12-Monatszeitraum — DBA-Text konkret prüfen, weicht historisch ab.
- Bruessel-EU-Beamte: Wohnsitzfiktion erhaelt deutsche Steueransaessigkeit; deutsche Steuerpflicht greift weiter, EU-Bezuege sind frei nach EU-Protokoll.

#### Praktiker-Tipps der alten Hasen

##### Erstattungsverfahren belgische Vorsteuer (Roerende Voorheffing / Precompte Mobilier)

- **Zuständigkeit**: belgische Erstattung durch **Service Public Federal Finances** (FOD/SPF Finances), Centre de Perception/Inningscentrum. Aktuelle Zuständigkeit auf **finance.belgium.be** prüfen.
- **Antragsformulare**: belgische Formulare **276 Div.** (Antrag Erstattung Mobiliar-Steuer für Ausländer) bzw. Schachtel-Bescheinigung — Bezeichnungen vom Anwender mit aktuellem Stand auf finance.belgium.be zu verifizieren.
- **Frist**: nach belgischem Steuerrecht regelmaessig **fuenf Jahre** ab dem Steuerjahr — vergleichsweise grosszuegig.
- **Bearbeitungsdauer**: 6-24 Monate; bei strittigen Faellen oft Jahre.
- **Online-Portal**: **MyMinfin** (myminfin.be) für belgische Steuerangelegenheiten.

##### Lokaler Steuerberater-Kontakt

- **Empfehlung**: bei EU-Beamten-Konstellationen (Bruessel), bei Sportler-/Kuenstlerauftritten in Belgien, bei Pensionsfaellen aus belgischer Pensionskasse. Bruesseler Kanzleien mit DE-Mandanten-Erfahrung.

##### Sprachen-Falle

- **DBA-Text DE/FR/NL** dreisprachig — die franzoesische und niederlaendische Fassung sind gleichberechtigt verbindlich. Bei Auslegungsstreit alle drei Fassungen prüfen.
- Belgischer Bescheid je nach Region in FR (Wallonien, Bruessel), NL (Flandern) oder DE (Eupen-Malmedy) — Sprache der Korrespondenz prüfen.

#### Trade-off-Tabelle

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| Schachteldividende belgische SA an DE-Mutter über DBA vs. EU-MTRL | DBA Art. 10 (5/15 Prozent) | EU-MTRL § 43b EStG: 0 Prozent bei mind. 10 Prozent Beteiligung und 12 Monate | § 43b EStG immer vorzugswuerdig — antragsweise an belgische Quelle |
| EU-Beamten-Bezuege (Protokoll 7 EUV) vs. private Einkuenfte | EU-Bezuege steuerfrei in DE und BE | private Einkuenfte (z.B. Vermietung Wohnung Bruessel) regulaer | klare Trennung in Steuererklaerung — Doppelbescheinigung von EU-Institution |
| Sportler-/Kuenstlerauftritt in BE vs. Tournee-Strukturierung | Quellenstaat BE besteuert (Sondersystem) | Holding-Struktur "Loan-Out-Company" | je nach Honorarvolumen — Substanztest zwingend |

#### Edge Cases — was Prüfer triggert

- **Sondersystem für Sportler/Kuenstler**: Belgien hat eigenes System für auftretende Kuenstler/Sportler (haeufig 18 Prozent Pauschalsteuer); DBA Art. 17 sieht Quellenstaat-Besteuerung vor — bei Tournees genau dokumentieren.
- **EU-Beamten-Konstellation**: deutscher EU-Beamter mit Wohnsitz Bruessel — § 14 EU-BeamtenStG iVm Protokoll 7 EUV bewirkt **Wohnsitzfiktion** Deutschland; trotz physischem Aufenthalt BE bleibt deutsche Steueransaessigkeit erhalten. EU-Gehalt steuerfrei in beiden Staaten.
- **Eupen-Malmedy-Pendler**: deutschsprachige Gemeinschaft Belgiens; klassische Grenzgaengerregelung der 1960er-Generation wurde durch Änderungsprotokolle ersetzt — aktuellen Stand prüfen.
- **DBI-Mismatch**: belgische Holding mit deutscher Quelle — belgische DBI gewaehrt Schachtelbefreiung im Empfaengerstaat; § 8b KStG-Befreiung in DE; bei Hybriden § 4k EStG.
- **183-Tage-Zaehlung**: aelteres DBA-Belgien definiert ggf. abweichend (Kalenderjahr vs. 12-Monatszeitraum) — sorgfaeltig prüfen.

#### Berechnungsbeispiel — Schachteldividende BE-SA an DE-Holding

> Belgische SA (Bruessel) schuettet 600.000 EUR Dividende an deutsche Holding (Beteiligung 60 Prozent, Haltedauer 4 Jahre).
>
> Schritt 1: EU-MTRL (§ 43b EStG) vorrangig: 0 Prozent belgische Mobiliarsteuer — vorab Freistellungs-Bescheinigung an die belgische Quelle.
>
> Schritt 2: Ohne Freistellung: 30 Prozent belgische Mobiliarsteuer (Roerende Voorheffing/Precompte Mobilier nationaler Standardsatz) = 180.000 EUR; Erstattung von 25 Prozent (Differenz zum DBA-Schachtel 5 Prozent) über Formular 276 Div. an SPF Finances.
>
> Schritt 3: In DE: § 8b KStG-Befreiung 95 Prozent, 5 Prozent fiktive nichtabziehbare BA; verbleibende belgische Quellensteuer (sofern nicht 0) auf deutsche KSt teilweise anrechenbar.
>
> Anmerkung: aktuelle Quellensteuersaetze und Formularnummern auf finance.belgium.be verifizieren.

#### Berechnungsbeispiel — EU-Beamter Bruessel mit Vermietungsobjekt

> Deutscher EU-Beamter, Wohnsitz Bruessel (rein dienstlich), Vermietung einer Wohnung in Koeln, Mieteinnahme 18.000 EUR p.a.
>
> Schritt 1: EU-Bezuege steuerfrei nach Protokoll 7 EUV — werden nicht steuerlich erfasst.
>
> Schritt 2: Wohnsitzfiktion DE wegen § 14 EU-BeamtenStG — deutsche Steueransaessigkeit erhalten.
>
> Schritt 3: Mieteinkuenfte Koeln: deutsche Belegenheit (Art. 6 DBA), Veranlagung in DE wie ordinaerer DE-Steuerpflichtiger.
>
> Schritt 4: keine belgische Steuerpflicht auf deutsche Mieteinnahmen.

#### Quellen und Updates

Stand: 05/2026. DBA-Belgien 11.04.1967 (BGBl. 1969 II S. 17/18), Zusatzabk. 05.11.2002 (BGBl. 2003 II S. 1616), Aend.-Prot. 21.01.2010 (BGBl. 2010 II S. 1279). MLI-Notifications beim OECD-Portal prüfen. Aktuelle Quellensteuer-Saetze und Pensionsregelung im konsolidierten DBA-Text prüfen.
## DBA Deutschland-Bulgarien (2010)

Auswahlsignal: Wenn es um DBA Deutschland-Bulgarien (2010) in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### DBA Deutschland-Bulgarien (2010)

#### Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DBA Deutschland-Bulgarien (2010)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

#### Kernsachverhalt

Das DBA-Bulgarien vom 25.01.2010 (BGBl. 2010 II S. 1286) ersetzte das DBA von 1987 und folgt OECD-MA 2008. Ein Änderungsprotokoll vom 21.07.2022 ist am 13.12.2023 in Kraft getreten (BGBl. 2023 II Nr. 213). Praxisrelevant sind IT-Outsourcing (niedrige Lohnstuffe), Holding-Strukturen (bulgarische KSt 10 Prozent), Pflege-Arbeitnehmer. Bulgarien ist EU-Mitglied (Beitritt 01.01.2007).

#### Kaltstart-Rueckfragen

1. Konstellation?
2. Beteiligungshoehe?
3. Pflege-Arbeitnehmer?
4. IT-Outsourcing: Verträge, Substanz?
5. CFC-Prüfung wegen niedriger KSt?
6. MLI-Anpassungen?
7. Pensionen?
8. Ansaessigkeitsbescheinigung?

#### Rechtlicher Rahmen

##### Primaernormen
- **DBA Deutschland-Bulgarien vom 25.01.2010**, in Kraft 21.12.2010, anwendbar ab 01.01.2011 (BGBl. 2010 II S. 1286; Bekanntmachung BGBl. 2011 II S. 584).
- **Änderungsprotokoll vom 21.07.2022**, in Kraft 13.12.2023 (BGBl. 2023 II Nr. 213; Bekanntmachung BGBl. 2024 II Nr. 139).
- **OECD-MA**.
- **§§ 34c, 32b, 50d EStG**, § 7 ff. AStG.
- **MTRL** (§ 43b EStG), **ZinsLizenzRL** (§ 50g EStG).
- **MLI**: Deutschland und Bulgarien sind MLI-Unterzeichner; das DBA-Bulgarien ist Stand 01.01.2026 nicht als Covered Tax Agreement im deutschen BEPS-MLI-Anwendungsgesetz gelistet; aktuellen Stand beim BMF prüfen.

##### Leitentscheidungen und BMF-Schreiben
- Spezifische BFH-Entscheidungen zum DBA-Bulgarien sind selten; bei Substanzfragen einschlaegig sind die allgemeinen BFH-Entscheidungen zu § 50d Abs. 3 EStG (vgl. `stb-dba-quellensteuer-erstattung-bzst-50c-estg`).
- BMF-Schreiben zur Anwendung § 43b EStG / Mutter-Tochter-RL und § 50g EStG / Zins-Lizenzgebuehren-RL (aktuelle Fassungen beim BMF abrufbar).

#### Land-spezifisches

##### Ansaessigkeit (Art. 4)
- OECD-Tie-Breaker.

##### Betriebsstaette (Art. 5)
- Bauausfuehrung **12 Monate**.

##### Aktive Einkuenfte
- Loehne Art. 14/15: 183-Tage-Regel.

##### Passive Einkuenfte
- **Dividenden** (Art. 10): 5 Prozent bei direkter Beteiligung von mindestens 10 Prozent am Kapital (ausser Personengesellschaften und REIT); 15 Prozent in allen anderen Faellen. EU-MTRL Schachtel 0 Prozent.
- **Zinsen** (Art. 11): 5 Prozent des Bruttobetrags im Quellenstaat.
- **Lizenzgebuehren** (Art. 12): 5 Prozent des Bruttobetrags im Quellenstaat. EU-ZinsLizenzRL bei verbundenen Unternehmen 0 Prozent.

##### Vermeidungs-Methode (Art. 22)
- Anrechnungsmethode ueberwiegend.

##### Besonderheiten
- **KSt Bulgarien 10 Prozent** — eine der niedrigsten EU-Saetze — CFC und Pillar Two relevant.
- **Pflege-Arbeitnehmer**: Sozialversicherung A1.

#### Workflow

Standard-Prüfungsraster (siehe `stb-dba-grundprinzip-oecd-musterabkommen`):

1. Persoenliche Anwendbarkeit (Art. 1, 4) — Ansaessigkeit nach BG-Recht und DE-Recht; Tie-Breaker.
2. Sachliche Anwendbarkeit (Art. 2) — erfasste Steuern.
3. Einkunftsart (Art. 6-21) — typische Mandanten-Konstellation: IT-Outsourcing/Holding-Dividenden/Pflege-A1.
4. Vermeidungsmethode (Art. 22) — Anrechnung ueberwiegend.
5. Innerstaatliche Umsetzung — § 34c EStG; bei Beteiligungen § 8b KStG / § 43b EStG; bei Lizenzen § 50g EStG; § 7 ff. AStG / Pillar Two wegen 10-Prozent-KSt.

BZSt-Verfahren: Freistellungsbescheinigung § 50c Abs. 2 EStG vorab; Erstattung § 50c Abs. 3 EStG nachtraeglich (Frist vier Jahre nach Ablauf des Kalenderjahres der Steuerentstehung); Antraege über BZSt-Online-Portal (BOP). Anlage: bulgarische Ansaessigkeitsbescheinigung der NRA (National Revenue Agency).

#### Strategie und Praxis-Tipps

- Niedrigste EU-KSt 10 Prozent: CFC-Hinzurechnung praktisch immer prüfen.
- Pillar Two: Top-Up-Tax für bulgarische Subholdings.
- IT-Outsourcing: Substanztest § 50d Abs. 3 EStG.
- Pflege-Arbeitnehmer: A1 und 183-Tage-Regel.
- EU-MTRL Schachtel vorrangig.

#### Praktiker-Tipps der alten Hasen

- **Erstattungsverfahren BG → DE-Mandant**: Antrag bei der NRA (Natsionalna agentsiya za prihodite, Nationale Steueragentur); Online-Portal der NRA (vom Anwender mit aktuellem Stand des bulgarischen Online-Portals zu verifizieren). Ansaessigkeitsbescheinigung der NRA als Anlage.
- **Sprache des DBA**: Authentische Textfassungen Deutsch, Bulgarisch und Englisch (DBA-Bulgarien 2010 als modernes DBA trilingual; bei strittiger Auslegung Englisch als praktische Pivot-Sprache).
- **Lokaler Berater**: Bei bulgarischer EOOD (GmbH-Äquivalent) oder OOD mit deutschem Anteilseigner empfiehlt sich Hinzuziehung eines bulgarischen "danachen konsultant" wegen niedriger KSt 10 Prozent und einfacherer Prüfungspraxis; aber: Substanznachweis für DE-Erstattung wird streng geprueft.
- **Apostille**: nicht erforderlich zwischen EU-Mitgliedstaaten (BG seit 2007 EU).

#### Edge Cases und Was-Prüfer-Triggert

- **BG-KSt 10 Prozent — niedrigste EU-Rate**: zwingend unter AStG-Niedrigsteuerschwelle 15 Prozent — CFC-Hinzurechnung bei passiven Einkuenften.
- **Pillar Two Top-Up**: BG hat EU-Pillar-Two-RL umgesetzt; multinational über 750 Mio EUR Umsatz unterliegen Top-Up auf 15 Prozent — für KMU bleibt 10-Prozent-Vorteil.
- **Änderungsprotokoll 2022/2023**: zum 13.12.2023 in Kraft getreten — Neuerungen prüfen, insbesondere Anti-Missbrauch und Schiedsverfahren.
- **Pflege-Arbeitnehmer aus Bulgarien in DE**: oft Konstruktion über bulgarische Service-Gesellschaft mit Entsendung nach DE; Lohnsteuer-Prüfung nach 183-Tage-Regel; A1-Bescheinigung nach EU-VO 883/2004.
- **IT-Outsourcing-Substanz**: Prüfer hinterfragt bei reinen Off-the-Shelf-Holdings ohne Personal in BG.
- **Bulgarische Sondersteuern**: zusaetzlich zur 10-Prozent-KSt erhebt BG diverse lokale Abgaben (Gewerbeflaechensteuer, Tourismussteuer), die durch DBA NICHT erfasst sind.

#### Trade-offs

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| BG-Holding 10 Prozent vs. CFC-Hinzurechnung | BG-Tochter operativ aktiv: 10 Prozent KSt-Vorteil | DE-CFC bei passiven Einkuenften: Hinzurechnung mit DE-Steuersatz | bei aktivem Geschäft Aktivitaetskatalog § 8 AStG prüfen; bei passiver Holding fast immer CFC |
| EU-MTRL vs. DBA-Schachtel | EU-MTRL: 0 Prozent ab 10 Prozent | DBA-BG: 5 Prozent ab 10 Prozent | EU-MTRL vorrangig (§ 43b EStG) |
| Pflege-Service mit BG-Gesellschaft vs. direkte AUe | BG-Werkvertrag-Service nach DE: keine deutsche Lohnsteuer bei korrekter Werksvertragsgestaltung | direkte Arbeitnehmerueberlassung nach AUeG mit Erlaubnis | bei korrektem Service-Vertrag (Werkvertrag, Selbständigkeit der BG-Gesellschaft) Steuerprivileg; aber Vorsicht: BAG-Rechtsprechung qualifiziert oft AUe — Beratungsbedarf |

#### Berechnungsbeispiel

DE-Mutter haelt 100 Prozent an bulgarischer EOOD; BG-Gewinn 150.000 EUR, BG-KSt 10 Prozent = 15.000 EUR. Ausschuettung 135.000 EUR an DE-Mutter:

- BG-QSt: 0 Prozent nach EU-MTRL (§ 43b EStG, ab 10 Prozent Schachtel).
- DE: § 8b KStG 95 Prozent steuerfrei; 5 Prozent (6.750 EUR) fiktive nichtabziehbare BA, DE-KSt+SolZ rund 15,825 Prozent = 1.068 EUR; GewSt rund 14 Prozent = 945 EUR. Gesamt DE rund 2.013 EUR.
- Gesamtbelastung: BG-KSt 15.000 + DE 2.013 = 17.013 EUR auf 150.000 EUR = 11,3 Prozent.
- Pillar-Two-Prüfung: Effektive Steuerquote 10 Prozent in BG unter 15 Prozent. Bei Konzern über 750 Mio EUR Umsatz: Top-Up-Tax 5 Prozentpunkte (BG-Gewinn 150.000 EUR x 5 Prozent = 7.500 EUR).
- CFC-Prüfung § 7 ff. AStG: bei aktivem BG-Geschäft keine Hinzurechnung; bei passiven Einkuenften (Lizenzen, Zinsen) Hinzurechnung mit DE-Steuersatz, abzueglich BG-KSt-Anrechnung.

#### Mandatsablauf in der Praxis

1. **Aufnahme**: Konstellation (IT-Outsourcing, EOOD/OOD-Holding, Pflege-Arbeitnehmer).
2. **Strukturierung**: BG-KSt 10 Prozent — CFC-Prüfung obligatorisch; Pillar Two bei Konzern über 750 Mio EUR; bei Holding Substanz § 50d Abs. 3 EStG.
3. **Antraege**: Ansaessigkeitsbescheinigung NRA; EU-MTRL/EU-ZinsLizenzRL-Freistellung BZSt.
4. **Laufende Compliance**: BG-Erklaerung jaehrlich; DE-Erklaerung mit Anrechnung und ggf. CFC-Hinzurechnung.
5. **Audit-Vorbereitung**: BG-Prüfer formal; DE-FA-Prüfung CFC und Substanz; ab Änderungsprotokoll 2022/2023 weitere Anti-Missbrauch.

#### Ausgabeformat für Mandanten-Memo Bulgarien

Empfohlene Struktur für das Mandanten-Memo nach Gutachtenstil (vgl. CLAUDE.md):

1. **Sachverhalt**: Wohnsitze, Konstellation (IT-Outsourcing, Holding, Pflege-Arbeitnehmer), Zeitraum.
2. **Frage(n)**: Besteuerungsrecht, niedrige BG-KSt 10 Prozent, CFC, Pillar Two.
3. **Kurzantwort**: DBA-Bulgarien 2010 Art. X regelt das Besteuerungsrecht; Anrechnungsmethode in DE.
4. **Rechtliche Bewertung**:
 - Persoenliche Anwendbarkeit (Art. 1, 4 DBA-BG 2010).
 - Sachliche Anwendbarkeit (Art. 2).
 - Einkunftsart und Verteilungsartikel; EU-MTRL/EU-ZinsLizenzRL vorrangig.
 - Methodenartikel (Art. 22 — Anrechnung ueberwiegend).
 - § 7 ff. AStG-CFC; Pillar Two bei Konzern über 750 Mio EUR.
 - Innerstaatliche Umsetzung (§§ 32b, 34c, 50d EStG; § 43b EStG).
5. **Gesamtergebnis** mit Berechnungsbeispiel.
6. **Risiken / offene Punkte**: Änderungsprotokoll 2022/2023, § 50d Abs. 3 EStG, Pillar Two, MLI-Status.
7. **Quellenverzeichnis** (gem. references/zitierweise.md).

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

#### Quellenpflicht

Vgl. [`references/zitierweise.md`](../../../../references/zitierweise.md). DBA-Bulgarien 2010 mit Änderungsprotokoll Fundstellen, BMF-Schreiben verbindlich zitieren.

#### Quellen und Updates

Stand: 05/2026. DBA-Bulgarien 25.01.2010, in Kraft 21.12.2010 (BGBl. 2010 II S. 1286). Änderungsprotokoll 21.07.2022 in Kraft 13.12.2023 (BGBl. 2023 II Nr. 213). MLI-Status: nicht als Covered Tax Agreement im deutschen BEPS-MLI-Anwendungsgesetz gelistet (Stand 01.01.2026). Dividenden 5/15 Prozent, Zinsen 5 Prozent, Lizenzen 5 Prozent. Aktuellen Stand im BMF-DBA-Verzeichnis prüfen.
