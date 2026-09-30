---
name: 03-chronologie-rueckruf-fristen
description: "Für ungeklärte Zeitfolge, Zugänge, Rückruf-, Update- oder Verfahrensdaten. Erstellt eine fundstellengebundene Chronologie und Fristenkarte. Materielle Verjährungsfragen gehen an Skill 07."
---

# Chronologie, Rückruf und Fristen

## Zweck und Anwendungsfall

Dieser Skill baut die beleggebundene Zeitfolge des Falls auf: vom Kauf über das Bekanntwerden des Skandals (Herbst 2015), den KBA-Rückruf und das Software-Update bis zu Kenntnis, Anspruchsschreiben und Klage. Die Chronologie trägt den Sachverhaltsvortrag der Klage und liefert die Fristenkarte, an der Skill `07-verjaehrung-restschadensersatz` die Verjährung rechnet.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst Zeitfolge und Fristenbewertung mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei ergebnisrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Ereignissen oder wiederkehrenden Feldern, sonst vollständige Absätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort liefert sofort eine vorläufige, aber vollständig ausformulierte Chronologie und Fristenkarte mit getrennter ursprünglicher Hersteller- und Update-Handlung, durchgerechneter Jahresende-Regel nach §§ 195, 199 BGB und Zehnjahres-Kontrolle nach § 852 BGB. Ab mindestens drei Ereignissen werden Datum, Bedeutung, Beleg, Fristwirkung und nächster Schritt tabellarisch verglichen; bei ein oder zwei Ereignissen genügen getrennte vollständige Absätze. Jeder unklare Kenntniszeitpunkt erscheint als begründete Spanne und präzise Lücke mit benötigtem Beleg und Auswirkung auf das Fristende, nie als leere Zeile.

Verboten in der ersten Antwort: Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen. Python-Werkzeuge sind Beschleuniger: Sind sie nicht verfügbar oder schlagen sie fehl, wird die Chronologie ohne Meldungslärm manuell gerechnet; ein Werkzeugfehler blockiert nie die Fristenkarte.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Kaufakte und Belegmatrix aus Skills 01 und 02.
- KBA-Rückrufschreiben, Update-Einladung, Werkstattauftrag/-bestätigung, Softwarebeschreibung und Korrespondenz mit Datum und Zugang.
- Angaben zur Kenntnis: Wann erfuhr die Geschädigte erstmals von ursprünglicher Betroffenheit, konkreter Update-Funktion und einem etwaigen Update-Schaden?

## Ablauf / Checkliste

1. Ereignisse sammeln und datieren: Kauf, Erstzulassung, Bekanntwerden der ursprünglichen Manipulation, Rückrufschreiben, Update-Einladung, Installation/Version, erstmals bemerkte Folgen, Erkenntnis zur Update-Funktion, Presse-/Behördeninformation, Anspruchsschreiben, Antworten und Klage. Ursprüngliche Herstellerhandlung und spätere Update-Handlung erhalten getrennte Zeilen.
2. Chronologie führen: Jedes Ereignis erhält Datum oder begründete Datumsspanne, tatsächliche Bedeutung, Beleg und Fundstelle, Fristwirkung sowie den daraus folgenden Schritt. Ab mindestens drei Ereignissen diese Angaben in einer ausgefüllten Tabelle vergleichen; bei weniger Ereignissen vollständig ausformulieren. Kein unbekanntes Datum durch eine leere Zeile ersetzen.

3. Kaufzeitpunkt gegen die Ad-hoc-Mitteilung vom 22.09.2015 stellen: Bei EA189 kann ein späterer Erwerb die konkrete §-826-Täuschungslinie ausschließen oder schwächen. Andere Motorfamilien, später bekannt gewordene Funktionen und der Differenzschaden bleiben getrennt zu prüfen.
4. Kenntnis anspruchsbezogen einordnen: Kenntnis der EA189-Umschaltlogik, der konkreten Fahrzeugbetroffenheit, einer später installierten Update-Funktion und eines dadurch verursachten eigenen Schadens sind nicht dasselbe. Die VW-Mitteilung vom 22.09.2015 ist nicht ohne Weiteres Kenntnis einer damals noch nicht installierten oder offengelegten Update-Funktion.
5. Update-Dreispur markieren: `Bestandsschaden` (keine rückwirkende Heilung), `Folgeschaden in ursprünglicher Kausalkette` oder `eigenständige Update-Handlung mit eigenem Schaden`. Die dritte Spur geht nur bei konkreter Handlung, Funktion, Schaden und Kausalität an Skill 07; sie ist kein Neubeginn des ursprünglichen Anspruchs.
6. Zugangsdaten sichern: Für jedes eigene Schreiben Zugangsart und -datum (Einwurf-Einschreiben, Bote, Zeuge) festhalten; Lücken an Skill 09 melden.
7. Fristenkarte mit Wiedervorlagen ausgeben: Verjährungsstichtage, gesetzte Fristen, gerichtliche Fristen; jede Frist mit Anspruchsspur, Quelle und Folge des Ablaufs.
8. Ampel setzen: rot bei laufender oder abgelaufener kritischer Frist, gelb bei ungeklärtem Kenntniszeitpunkt, grün bei vollständiger Zeitfolge. Übergabe an Skill `06-anspruchstriage-fallstrategie` oder `07-verjaehrung-restschadensersatz`.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Eine beweisgebundene Ereigniskette erstellen, die Zugang, Kenntnis, Hemmung und Fristfolge nicht vermischt.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Jedes fristauslösende oder -hemmende Ereignis besitzt Datum, Beleg, Zugangsstatus, Rechtsfolge und Gegenhypothese.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Der Kaufzeitpunkt und die damalige Informationslage prägen besonders die §-826-Spur; sie müssen tagesgenau in die Chronologie. | Bestätigt |
| BGH, Urt. v. 17.12.2020 - VI ZR 739/20 | Für den EA189-Fall hat der BGH die Zumutbarkeit der Klage bei Kenntnis der konkreten Fahrzeugbetroffenheit geprüft; Kenntnisereignisse sind anspruchs- und modellbezogen zu datieren, nicht pauschal zu übertragen. | Amtlich geprüft |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | Verursacht eine erst per Software-Update installierte unzulässige Einrichtung einen Schaden, muss ein Anspruch eröffnet sein; Installations-, Funktions- und Schadensdatum gehören in die Chronologie. | Amtlich geprüft |
| BGH, Urt. v. 06.02.2023 - VIa ZR 419/21 | Update-Folgen können Teil der ursprünglichen Kausalkette sein; diese Spur setzt die Verjährung des Erwerbsschadens nicht neu in Gang. | Amtlich geprüft |
| BGH, Urt. v. 02.06.2022 - VII ZR 283/20; Beschl. v. 09.03.2021 - VI ZR 889/20 | Eine eigenständige Update-Haftung ist als anderer Streitgegenstand mit eigenem Kenntnisverlauf zu führen; für § 826 reichen Unzulässigkeit und negative Folgen allein nicht. | Amtlich geprüft |
| OVG Schleswig, Urt. v. 25.09.2025 - 4 LB 36/23 (amtliche Pressemitteilung) | Die EA189-Updategenehmigung wurde im konkreten Verwaltungsverfahren beanstandet; Temperatur-/Höhenparameter als Kontext erfassen, aber nicht als automatischen Zivilhaftungs- oder EA288-Beweis verwenden. | Amtlicher Kontextanker; Volltext live prüfen |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

Baustein 1 — Chronologie-Ergebnissatz zur Zeitfolge:

„Die Klägerin erwarb das Fahrzeug [Hersteller und Modell] mit der FIN [FIN] am [Datum TT.MM.JJJJ] zum Kaufpreis von [Betrag in EUR] (Anlage K1). Das Kraftfahrt-Bundesamt ordnete den Rückruf an; das Rückrufschreiben des Herstellers ging der Klägerin am [Datum TT.MM.JJJJ] zu (Anlage K[Nummer]). Das Software-Update wurde am [Datum TT.MM.JJJJ] installiert (Anlage K[Nummer])."

Baustein 2 — Chronologie-Ergebnissatz Kenntnis:

„Kenntnis der anspruchsbegründenden Umstände im Sinne des § 199 Abs. 1 Nr. 2 BGB von der konkreten Betroffenheit gerade ihres Fahrzeugs erlangte die Klägerin frühestens mit Zugang des Rückrufschreibens am [Datum TT.MM.JJJJ]; die allgemeine Berichterstattung ab dem 22.09.2015 vermittelte diese fahrzeugbezogene Kenntnis nicht. Von der erst mit dem Update installierten Funktion [Bezeichnung der Funktion] konnte sie vor dem [Datum TT.MM.JJJJ] keine Kenntnis haben, weil [Grund, zum Beispiel fehlende Offenlegung der Funktionsweise]."

Baustein 3 — Chronologie-Ergebnissatz Fristwirkung:

„Die regelmäßige Verjährungsfrist von drei Jahren (§ 195 BGB) begann mit dem Schluss des Jahres [JJJJ] (§ 199 Abs. 1 BGB) und endete mit Ablauf des 31.12.[JJJJ]. Hemmungstatbestände, insbesondere eine Anmeldung zur Musterfeststellungsklage (§ 204 Abs. 1 Nr. 1a BGB a.F.) oder Verhandlungen (§ 203 BGB), sind mit Datum, Dauer und Beleg gesondert auszuweisen; ohne belegte Hemmung bleibt es bei dem genannten Fristende."

### Rechenbeispiel: Fristenlauf bei Kauf 2014 und Rückruf 2016

Ausgangswerte: Kauf und Zahlung am 15.03.2014; Ad-hoc-Mitteilung vom 22.09.2015; Zugang des Rückrufschreibens mit konkreter Fahrzeugbetroffenheit am 10.06.2016; Software-Update am 08.05.2017; Mandatierung am 20.01.2026.

1. Anspruchsentstehung

   Der Erwerbsschaden entsteht mit dem ungewollten Vertragsschluss und der Zahlung, hier am 15.03.2014 (§ 199 Abs. 1 Nr. 1 BGB).

2. Kenntnis

   Kenntnis der konkreten Betroffenheit im Sinne des § 199 Abs. 1 Nr. 2 BGB liegt hier mit Zugang des Rückrufschreibens am 10.06.2016 vor. Ob bereits die Berichterstattung des Jahres 2015 genügte, ist als Gegenhypothese in einer eigenen Zeile zu führen.

3. Jahresende-Regel

   Die Frist beginnt mit dem Schluss des Jahres der Kenntnis, also mit Ablauf des 31.12.2016, und läuft drei Jahre (§ 195 BGB): Fristende mit Ablauf des 31.12.2019. In der Gegenhypothese Kenntnis schon 2015 endet die Frist bereits mit Ablauf des 31.12.2018.

4. Zehnjahres-Kontrolle nach § 852 BGB

   Der Restschadensersatzanspruch verjährt in zehn Jahren von seiner Entstehung an, hier also mit Ablauf des 15.03.2024. Das Update vom 08.05.2017 setzt keine dieser Fristen neu in Gang; nur eine eigenständige Update-Spur mit eigenem Schaden hätte einen eigenen Kenntnis- und Fristenlauf.

Ergebnis-Satz: Ohne belegten Hemmungstatbestand ist der Erwerbsanspruch seit dem 01.01.2020 und der Restschadensersatz seit dem 16.03.2024 verjährt; zu prüfen bleiben eine Hemmung durch Anmeldung zur Musterfeststellungsklage (§ 204 Abs. 1 Nr. 1a BGB a.F.) und eine eigenständige Update-Spur, deren Rechnung Skill `07-verjaehrung-restschadensersatz` führt.

### Entscheidungstabelle

| Wenn (Befund) | Dann (Pfad) | Begründung | Nächster Skill |
| --- | --- | --- | --- |
| Kenntnisjahr plus drei Jahre abgelaufen, keine Hemmung belegt | Ampel rot, Restschadensersatz nach § 852 BGB rechnen | regelmäßige Verjährung nach §§ 195, 199 BGB eingetreten | 07 |
| Kauf nach dem 22.09.2015 (EA189) | rote Markierung der §-826-Täuschungslinie, Triage auf Differenzschaden und Gewährleistung | späterer Erwerb schließt die konkrete Täuschungslinie regelmäßig aus oder schwächt sie | 06 |
| Update installiert eigene Funktion mit eigenem, belegbarem Schaden | eigene Kenntnis- und Fristzeile anlegen, Spur getrennt rechnen | anderer Streitgegenstand mit eigener §§-195/199-BGB-Prüfung | 07 |
| Kritische Frist endet innerhalb der nächsten drei Monate | Ampel rot, verjährungshemmende Maßnahme sofort vorbereiten | Fristablauf vernichtet die Anspruchsspur | 13 und 16 |
| Zugang eines eigenen Schreibens unbelegt | Ampel gelb, Zugangsnachweis beschaffen | ohne Zugangsnachweis keine belastbare Fristwirkung | 09 |
| Zeitfolge vollständig, keine Frist kritisch | Ampel grün, Sachverhaltsvortrag aus den Bausteinen 1 bis 3 freigeben | Chronologie trägt Klage und Triage | 06 |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Daten nur aus Belegen; Kenntniszeitpunkte als Wertung kennzeichnen. Rechtsprechung nur aus `references/gepruefte-anker-dieselgate.md`; keine erfundenen Aktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Beleggebundene Chronologie mit Fristwirkung, Fristenkarte und Wiedervorlagenliste in vollständigen, ausformulierten Sätzen. Ab mindestens drei Ereignissen wird die Chronologie tabellarisch verglichen; sonst werden die Ereignisse in getrennten Absätzen oder einer kurzen Liste dargestellt. Bloße Stichwortsammlungen und leere Tabellenzeilen sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Kauf 2014, Rückruf 2016, Update 2017, Mandat 2026. Kernbefund: regelmäßige Verjährung und Zehnjahresfrist des § 852 BGB nach dem Rechenbeispiel abgelaufen, Hemmung ungeklärt. Erste Antwort: Chronologie-Tabelle mit getrennten Erwerbs- und Update-Zeilen, Fristenkarte mit den Stichtagen 31.12.2019 und 15.03.2024 sowie genau einer Rückfrage nach einer Anmeldung zur Musterfeststellungsklage.
- Eingang: Update 2017, konkretes Thermofenster und zusätzlicher Vermögensschaden erst 2024 belegt. Kernbefund: mögliche eigenständige Update-Spur mit eigenem Kenntnislauf, keine automatische Freigabe. Erste Antwort: gelbe Ampel, eigene Kenntniszeile nach Baustein 2 mit Platzhaltern und Übergabevermerk an Skill 07.
- Eingang: Kauf im Januar 2016, EA189. Kernbefund: Erwerb nach der Ad-hoc-Mitteilung vom 22.09.2015, §-826-Täuschungslinie regelmäßig ausgeschlossen. Erste Antwort: rote Markierung in der Chronologie und Triage-Zeile Richtung Differenzschadens- und Gewährleistungsspur an Skill 06.
- Eingang: Anspruchsschreiben versandt, Zugangsart unbekannt. Kernbefund: Fristwirkung des Schreibens nicht belastbar. Erste Antwort: gelbe Ampel, Fristenkarte mit Vorbehaltsvermerk und Nachweislücke als Auftrag an Skill 09.
