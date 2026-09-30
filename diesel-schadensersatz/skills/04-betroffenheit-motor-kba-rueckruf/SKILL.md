---
name: 04-betroffenheit-motor-kba-rueckruf
description: "Für offene Fahrzeug-, Motor-, FIN-, KBA-, Typgenehmigungs- oder Maßnahmenzuordnung. Klärt den konkreten Betroffenheitsbezug und seine Beleggrenzen. Keine Haftungsannahme allein aus Motorfamilie oder Modell."
---

# Betroffenheit: Motor, Modell und KBA-Rückruf

## Zweck und Anwendungsfall

Dieser Skill klärt die Kernfrage jedes Dieselfalls: Ist dieses Fahrzeug betroffen? Er ordnet Motorcode und Baureihe der Skandal-Landschaft zu (EA189, EA288, OM651, BMW- und Fiat/Iveco-Motoren), prüft KBA-Rückrufstatus mit Rückrufcode, Typgenehmigung und Pflicht-Update. Ergebnis ist die Betroffenheitsmatrix, auf der Skill 05 die Abschalteinrichtung einordnet und Skill 06 die Anspruchsgrundlage wählt.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst den fahrzeugbezogenen Betroffenheitsbefund mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei einstufungsrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Merkmalen oder wiederkehrenden Feldern, sonst vollständige Absätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort liefert sofort einen vorläufigen, aber vollständig ausformulierten Betroffenheitsbefund mit ehrlicher Einstufung (`amtlich zugeordnet`, `technisch substantiiert`, `greifbare Anhaltspunkte` oder `offen`), Ampel und präziser Lückenliste. Jede Lücke nennt das fehlende Fahrzeugmerkmal oder Behördenbeleg, den Beschaffungsweg und die Folge für die Einstufung. Ab mindestens drei vergleichbaren Merkmalen oder wiederkehrenden Feldern wird der Befund tabellarisch dargestellt; sonst genügen vollständige Absätze oder eine kurze Liste. Leere Matrixzellen sind unzulässig. Verboten sind Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen. Das Abfragewerkzeug ist Beschleuniger; fehlt es oder schlägt es fehl, entsteht derselbe Befund ohne Meldungslärm aus den Belegen.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- FIN, Motorcode, Modell, Baujahr, Euro-Norm sowie Papier-CoC oder elektronischer CoC-Datensatz aus der Kaufakte (Skill 01).
- KBA-Rückrufschreiben, Werkstatthistorie, Software-Update-Nachweis.
- Herstellerauskünfte und Rückrufdatenbank-Auszüge, soweit vorhanden.

## Ablauf / Checkliste

1. Motorcode sicherstellen: aus Fahrzeugpapieren, Werkstatthistorie oder Typenschild-Foto; bei Unsicherheit konkreten Beschaffungsweg benennen (Autohaus, Herstellerauskunft zur FIN).
2. Motorfamilie zuordnen: EA189 mit passendem Pflichtrückruf/Prüfstandserkennung ist die gesicherte Fallgruppe der Vorsatzlinie. Beim EA288 liefern 131 veröffentlichte Entscheidungen zahlreiche Suchanker, aber keinen Serienbeweis. OM651, BMW- und Fiat/Iveco-Motoren bleiben fahrzeug- und funktionsbezogen zu prüfen.
3. Für jede Motorfamilie die konkrete Variante bestimmen: Motorkennbuchstabe, Abgasnorm, Leistung, Typgenehmigung, Abgasnachbehandlung (SCR/NOx-Speicherkatalysator), Softwarestände vor und nach Update. Bei Fiat/Ducato zusätzlich CoC-Baumuster, Hubraum und Leistung als Identitätskette erfassen; eine abweichende Verkaufsbezeichnung widerlegt die technische Identität nicht ohne Prüfung. Seit 05.07.2026 bereitgestellte elektronische CoC-Daten im Originalformat mit Abrufquelle, Abrufzeit und Hash sichern; ein Ausdruck ist nur Kontrollansicht. Die FIN allein trägt keine verlässliche Motorkennung; fehlende Kerndaten sind Beleglücke, kein Betroffenheitsnachweis.
4. KBA-Rückrufdatenbank und KBA-/GovData-Datensatz mit den konkreten Merkmalen prüfen; Suchdatum, Suchparameter, Treffer, Rückrufcode sowie Pflicht- oder freiwilliges Update dokumentieren. Ein Treffer ist im ausgewiesenen Umfang starkes Indiz; kein Treffer beweist weder Unbetroffenheit noch Rechtmäßigkeit.
5. Typgenehmigung und jeden behaupteten Behördenvorgang erfassen: Behörde, Datum, Aktenzeichen, Fahrzeug-/Typbezug, offengelegte Funktion, Prüfungen, Rechtsauffassung und Softwarestand. Typgenehmigungs-, Herstellungs-, Erstzulassungs-, Kauf- und Updatezeitpunkt bestimmen die zu prüfende Normfassung. VO (EU) 2018/858 gilt seit 01.09.2020, erhält aber nach Art. 89 ältere Genehmigungen; spätere Euro-7-Regeln sind kein rückwirkender Betroffenheitsbeweis. Bei italienischer Fiat-Typgenehmigung die KBA-/MIT-Kommunikation 2016 bis 2022 als eigene Chronologie führen. Die Genehmigung schließt Haftung nicht automatisch aus; `VIa ZR 314/24` begrenzt im vergleichbaren Fiat/MIT-Sachverhalt nur die §-826-Spur, nicht die §-823-Abs.-2-Spur.
6. Betroffenheitsbefund ausgeben: Motorcode, Motorfamilie oder Fallgruppe, KBA-Rückrufcode, Software-Update mit Pflichtstatus und Datum, Typgenehmigung sowie das Gesamtergebnis jeweils mit konkretem Wert, Quelle samt Fundstelle und begründeter Bewertung nennen. Ein unbekanntes Merkmal wird als präziser Lückensatz mit Beschaffungsweg und Auswirkung auf die Einstufung ausformuliert. Ab mindestens drei vergleichbaren Merkmalen kann eine vollständig befüllte Matrix verwendet werden; leere Zellen oder reine Überschriften sind unzulässig.

7. Ehrlich einstufen: `amtlich zugeordnet` (passender Rückruf-/Maßnahmentreffer), `technisch substantiiert` (fahrzeugbezogene Funktion durch Unterlage, Auskunft oder Gutachten), `greifbare Anhaltspunkte` (belegte identische Konfiguration/Parallelvortrag) oder `offen` (nur Motorfamilie, Modellliste oder Pressebericht). Haftungsbewertung erst in Skill 05/06.
8. Verwaltungskontext begrenzen: `OVG Schleswig 4 LB 36/23` betrifft die konkrete EA189-Updategenehmigung und relativiert pauschale KBA-Entlastung; daraus weder EA288-Betroffenheit noch zivilrechtlichen Schaden ableiten.
9. Für die aktuelle Gegenprobe höchstens sechs Treffer laden: `python3 "$CLAUDE_PLUGIN_ROOT/tools/diesel-fuenfjahre-query.py" --query "[Motor Funktion]" --arbeitsset --format markdown`. Rang C/D bleibt Suchmaterial.
10. Übergabe: Einordnung der Einrichtung an Skill `05-abschalteinrichtung-thermofenster-update`; bei offener Betroffenheit Beweisstrategie an `17-klageerwiderung-replik-beweis` vormerken; Triage an `06-anspruchstriage-fallstrategie`.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Fahrzeugidentität, Behördenstatus und technische Anhaltspunkte trennen, damit weder ein fehlender Rückruf noch eine bloße Motorfamilie zur Haftungsbehauptung wird.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Die Betroffenheitsaussage ist FIN- und konfigurationsbezogen oder bleibt als offene Prüfspur gekennzeichnet.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| EuGH, Urt. v. 17.12.2020 - C-693/18 | Auch ohne Rückruf kann eine unzulässige Abschalteinrichtung vorliegen; der Rückruf ist Indiz, nicht Tatbestandsmerkmal. | Bestätigt |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | Eine EG-Typgenehmigung oder hypothetische Behördenbestätigung trägt einen daraus hergeleiteten unvermeidbaren Verbotsirrtum nicht; konkrete Behördenvorgänge nur auf vollständiger Informationsgrundlage würdigen. | Amtlich geprüft |
| BGH, Urt. v. 03.09.2025 - VIa ZR 26/24 | Für die Entlastung sind tatsächlicher Rechtsirrtum der maßgeblichen Repräsentanten und Unvermeidbarkeit getrennt darzulegen und zu beweisen. | Amtlich geprüft |
| BGH, Beschl. v. 28.07.2026 - VIa ZR 46/24 | Konkret belegten KBA-Vortrag in der EA288-§-826-Spur erfassen; der Gehörsbeschluss belegt weder Rechtmäßigkeit noch eine §-823-Abs.-2-Entlastung. | Amtlich geprüft |
| BGH, Beschl. v. 30.06.2026 - VIa ZR 314/24 | Die besondere KBA-/MIT-Chronologie ist als eigener §-826-Risikoblock zu erfassen; der Beschluss trägt weder einen allgemeinen Betroffenheitsgegenbeweis noch eine Aussage zur §-823-Abs.-2-Spur. | Amtlich geprüft |
| Fünfjahreskorpus 26.08.2021 bis 26.08.2026: 135 Entscheidungen und Statusakten | Für aktuelle LG-/OLG-/BGH-/EuGH- und Verwaltungsanker den Fünfjahreskorpus mit Quellenrang und Verwendungsgrenze abfragen. | Kuratierter Arbeitskorpus mit Quellenrängen |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

Baustein 1 — Betroffenheitsvortrag bei amtlicher Zuordnung:

„Das Fahrzeug der Klägerin, [Hersteller und Modell], FIN [FIN], ist mit einem Dieselmotor des Typs [Motorcode] ausgestattet und unterliegt dem vom Kraftfahrt-Bundesamt angeordneten verpflichtenden Rückruf mit dem Rückrufcode [Rückrufcode]; das zugehörige Software-Update wurde am [Datum TT.MM.JJJJ] aufgespielt. Beweis: Rückrufschreiben vom [Datum TT.MM.JJJJ] (Anlage K[Nummer]); KBA-Rückrufdatenbank-Auszug, abgerufen am [Datum TT.MM.JJJJ] mit den Suchparametern [Suchparameter] (Anlage K[Nummer]); Werkstattbestätigung (Anlage K[Nummer])."

Baustein 2 — Betroffenheitsvortrag ohne Rückruf (technisch substantiiert):

„Das Fahrzeug ist mit dem Motor [Motorcode], Abgasnorm [Euro-Norm] und der Abgasnachbehandlung [SCR oder NOx-Speicherkatalysator] ausgestattet. Die Motorsteuerung enthält nach [Unterlage oder Gutachten] eine temperaturabhängige Steuerung der Abgasrückführung, die die Abgasrückführungsrate außerhalb des Bereichs von [Wert] bis [Wert] Grad Celsius reduziert. Ein fehlender Rückruf steht dem nicht entgegen, weil der Rückruf Indiz, nicht Tatbestandsmerkmal ist. Beweis: [Unterlage] (Anlage K[Nummer]); Sachverständigengutachten."

### Wenn/Dann-Betroffenheitstabelle

| Wenn (Motorfamilie, Rückruf, Update) | Dann (Einstufung und Pfad) | Nächster Skill |
| --- | --- | --- |
| EA189, passender Pflichtrückrufcode, Update belegt | amtlich zugeordnet, Ampel grün, Baustein 1 | 05 und 06 |
| EA189, Rückrufschreiben fehlt, FIN bekannt | offen halten; KBA- und Herstellerabfrage zur FIN, Suchparameter dokumentieren | 04 (Wiedervorlage) |
| EA288 ohne Pflichtrückruf, konkrete Funktionsunterlage vorhanden | technisch substantiiert, Baustein 2 | 05 |
| Nur Motorfamilie, Parallelentscheidungen oder Presseberichte | höchstens greifbare Anhaltspunkte; Ampel rot, Warnung vor Klage, Identitätskette oder Gutachten beschaffen | 04, Beweisvormerkung an 17 |
| OM651, BMW oder Fiat mit nur freiwilliger Servicemaßnahme | funktionsbezogen prüfen, Indizwert geringer | 05 |
| Rückruftreffer, aber abweichendes Baumuster oder Leistung | Identitätskette aufbauen (CoC-Baumuster, Hubraum, Leistung, Softwarestand); Verkaufsbezeichnung entscheidet nicht | 04 |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Rückrufstatus für produktive Fälle immer amtlich mit dokumentierten Suchparametern prüfen; Trainingsreferenzen sind illustrativ. Den datumsbezogenen Typgenehmigungs- und eCoC-Rahmen aus `references/rechtsstand-2026-gesetzgebung.md` anwenden. Behördenquellen nach `references/behoerden-und-praxisquellen-diesel.md`, aktuelle Gegenlinien nach `references/diesel-rechtsprechung-2021-2026.md`, Leitlinien nach `references/gepruefte-anker-dieselgate.md`; EA288-Kanzleivolltexte bleiben Nutzermaterial.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Fahrzeugbezogener Betroffenheitsbefund mit Ampel, Beleglage und präziser Lückenliste in vollständigen, ausformulierten Sätzen. Ab mindestens drei vergleichbaren Merkmalen oder wiederkehrenden Feldern kann eine vollständig befüllte Matrix verwendet werden; sonst genügen Absätze oder eine kurze Liste. Bloße Stichwortsammlungen und leere Matrixzellen sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Volkswagen EA189 mit Rückrufcode 23R7, Rückrufschreiben und Update-Bestätigung. Kernbefund: amtlich zugeordnet, Ampel grün. Erste Antwort: vollständige Matrix mit Vortrag nach Baustein 1, Übergabe an Skill 06 Richtung großer Schadensersatz.
- Eingang: OM651 ohne Rückruf, Werkstattunterlage zur temperaturabhängigen Abgasrückführung. Kernbefund: technisch substantiiert, Thermofenster-Spur. Erste Antwort: Matrix mit Baustein 2 und Temperaturbereich als Platzhalter, Übergabe an Skill 05.
- Eingang: BMW, Betroffenheit nur aus einem Pressebericht. Kernbefund: offen, kein klagefähiger Vortrag. Erste Antwort: Matrix mit roter Ampel, Warnung vor Klage ohne Befund, Lückenliste mit Herstellerauskunft zur FIN.
