---
name: 09-anspruchsschreiben-zugangsnachweis
description: "Für ein vorprozessuales, beziffertes Anspruchsschreiben an den Hersteller. Erstellt vollständigen Text, bestimmte Frist, gegebenenfalls Rückgabeangebot und Zugangsnachweis. Nicht für eine Klage oder prozessuale Replik."
---

# Anspruchsschreiben und Zugangsnachweis

## Zweck und Anwendungsfall

Dieser Skill erledigt das Vorprozessuale in einem Zug: Er formuliert das Anspruchsschreiben an den Hersteller vollständig aus und sichert dessen beweisfesten Zugang. Verzug oder Annahmeverzug treten nicht allein durch Übersendung eines Schreibens ein; Forderung, Fälligkeit, Mahnung oder Frist, Rückgabeangebot und Zugang müssen die gesetzlichen Voraussetzungen erfüllen. Deshalb gehören Schreiben, stichtagsbezogene Rechnung und Zugangsnachweis zusammen.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort ein Arbeitsprodukt: den vollständigen Entwurf des Anspruchsschreibens mit ausformulierten Kernabsätzen (Forderung mit Berechnung, Fristsetzung mit Klageandrohung) und klar markierten Platzhaltern für fehlende Falldaten, dazu ein vorläufiges, aber vollständig ausformuliertes Zustellprotokoll für den gewählten Zugangsweg. Als konkrete Lücken werden nur noch nicht belegte Versand- und Zugangsdaten benannt, insbesondere Versanddatum, Sendungsnummer oder Botenperson, Einlieferungs- und Auslieferungsbeleg sowie Fristablauf.
Verboten in der ersten Antwort sind Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen; eine Rückfrage unterbleibt, wenn ein Entwurf mit Platzhaltern möglich ist. Werkzeuge (Python-Skripte) sind Beschleuniger: Sind sie nicht verfügbar oder schlagen sie fehl, wird ohne Meldungslärm manuell weitergearbeitet; ein Werkzeugfehler blockiert nie den Schreibensentwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Anspruchslinie und Strategiekarte aus Skill 06, Schadenstabelle aus Skill 08.
- Kaufakte mit FIN, Kaufdatum, Kaufpreis (Skill 01/02); Betroffenheitsnachweis (Skill 04/05).
- Anschrift der Rechtsabteilung oder Zustellungsbevollmächtigten des Herstellers.

## Ablauf / Checkliste

1. Vollständigkeit sichern: FIN, Kaufdatum, Kaufpreis, Betroffenheit und Bezifferung müssen feststehen; sonst zurück an die liefernde Station mit konkreter Lücke.
2. Schreiben aufbauen: Anrede und Bezug (Kaufvertrag über das Fahrzeug mit der FIN), Sachstand (Betroffenheit, Motorcode, Einrichtungstyp), Anspruchsgrundlage, bezifferte Forderung mit stichtagsbezogener Berechnung, bei großem Schadensersatz ein erfüllbares Zug-um-Zug-Angebot der Rückgabe, angemessene Frist mit Kalenderdatum, Ankündigung gerichtlicher Schritte, Unterschrift mit Vertretungsverhältnis. Das Angebot nicht an eine unberechtigte oder deutlich überhöhte Gegenforderung knüpfen.
3. Vollständig ausformulieren: ganze Sätze, Urteilsstil-Nähe, dezimale Gliederung; kein Stichworttext.
4. Zinshinweis richtig setzen: keine Deliktszinsen; Verzugszinsen ab Fristablauf ankündigen.
5. Zugangsweg wählen und dokumentieren: Bote mit Inhalts- und Einwurfprotokoll, dokumentierte Zustellung oder Einwurf-Einschreiben mit Einlieferungs- und Auslieferungsbeleg. E-Mail nur mit gesichertem Empfängerbezug und zusätzlicher Zugangs-/Inhaltsdokumentation als allein tragenden Nachweis erwägen.
6. Zustellprotokoll führen: Versanddatum, Zugangsart, Zugangsdatum, Beleg (Einlieferungs- und Statusbeleg, Botenprotokoll), Fristablaufdatum.
7. Wiedervorlagen setzen: vor Fristablauf (Reaktion prüfen) und vor drohender Verjährung (Klageentscheidung erzwingen); Termine an Skill 03 zurückmelden.
8. Nach Fristablauf routen: Antwort des Herstellers an Skill `18-vergleich-abfindung-nachzahlung` (bei Angebot) oder an Skill `13-klageweg-streitwert-zustaendigkeit` (bei Ablehnung oder Schweigen).

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Ein bestimmtes, beweisbares und taktisch belastbares Anspruchsschreiben erzeugen, das keine spätere Klageposition verschenkt.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Forderung, Anspruchsgrund, Tatsachenkern, Anlagen, Frist und Zugangsnachweis sind konsistent und freigegeben.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 17.01.2023 - VI ZR 316/20 | Ein Rückgabeangebot begründet Annahmeverzug nicht automatisch: Es darf nicht an eine unberechtigte oder deutlich überhöhte Gegenforderung geknüpft sein; Forderung und Angebot sind stichtagsbezogen zu rechnen. | Amtlich geprüft |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Beim Thermofenster wird der Differenzschaden mit der Quote nach § 287 ZPO beziffert; das Fahrzeug wird behalten. | Bestätigt |
| BGH, Urt. v. 30.07.2020 - VI ZR 354/19; VI ZR 397/19 | Keine Deliktszinsen fordern; Verzugszinsen erst ab Fristablauf. | Bestätigt |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Kernabsatz Forderung mit Berechnung (großer Schadensersatz):**

In Sachen [Name der Anspruchstellerin] gegen [Name des Herstellers] zu dem Kaufvertrag über das Fahrzeug [Hersteller, Modell] mit der FIN [FIN] machen wir Schadensersatzansprüche wegen einer unzulässigen Abschalteinrichtung geltend. Die Anspruchstellerin hat das Fahrzeug am [Datum TT.MM.JJJJ] zum Kaufpreis von [Betrag in EUR] erworben; die Betroffenheit ist durch [KBA-Rückrufbescheid / Herstellerschreiben vom Datum TT.MM.JJJJ] belegt.
Der Kilometerstand beträgt zum Stichtag [Datum TT.MM.JJJJ] [Zahl] Kilometer. Unter Zugrundelegung einer erwarteten Restlaufleistung von [Zahl] Kilometern im Erwerbszeitpunkt ergibt sich eine anzurechnende Nutzungsentschädigung von [Betrag in EUR] (Kaufpreis multipliziert mit den gefahrenen Kilometern, geteilt durch die erwartete Restlaufleistung).
Wir fordern Sie daher auf, an die Anspruchstellerin [Betrag in EUR] zu zahlen, Zug um Zug gegen Rückgabe und Übereignung des vorbezeichneten Fahrzeugs. Die Rückgabe und Übereignung des Fahrzeugs wird hiermit ausdrücklich angeboten; das Angebot wird nicht von weiteren Bedingungen oder Gegenforderungen abhängig gemacht.

**Baustein 2 — Kernabsatz Fristsetzung mit Klageandrohung:**

Zur Zahlung des vorgenannten Betrags und zur Erklärung über die Rücknahme des Fahrzeugs setzen wir Ihnen eine Frist bis zum [Datum TT.MM.JJJJ] (Eingang der Zahlung beziehungsweise Ihrer Erklärung). Nach fruchtlosem Ablauf dieser Frist befinden Sie sich mit der Zahlung in Verzug (§ 286 BGB); ab diesem Zeitpunkt werden Verzugszinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz (§ 288 Abs. 1 BGB) sowie die weiteren Kosten der Rechtsverfolgung geltend gemacht. Wir kündigen bereits jetzt an, dass nach fruchtlosem Fristablauf ohne weitere Vorankündigung Klage erhoben und zugleich die Feststellung des Annahmeverzugs beantragt wird.

**Baustein 3 — Kernabsatz Forderung Differenzschaden (Fahrzeug bleibt):**

Die Anspruchstellerin behält das Fahrzeug und macht den Differenzschaden geltend. Dieser wird nach § 287 ZPO auf [Zahl] Prozent des Kaufpreises von [Betrag in EUR], mithin [Betrag in EUR], geschätzt; maßgeblich sind das Gewicht des Verstoßes gegen § 6 Abs. 1, § 27 Abs. 1 EG-FGV und das Risiko behördlicher Nutzungsbeschränkungen. Nutzungsvorteil und Restwert sind zum Stichtag [Datum TT.MM.JJJJ] berücksichtigt; die Berechnung liegt diesem Schreiben als Anlage bei. Wir fordern Sie auf, [Betrag in EUR] an die Anspruchstellerin zu zahlen.

### Rechenbeispiel: Frist- und Verzugsrechnung zum Schreiben

Grundlage ist die Schadenstabelle aus Skill 08: Forderung 19.708,00 EUR Zug um Zug (Kaufpreis 32.500,00 EUR abzüglich Nutzungsentschädigung 12.792,00 EUR bei 98.400 gefahrenen Kilometern und 250.000 Kilometern erwarteter Restlaufleistung). Versand des Schreibens als Einwurf-Einschreiben am Montag, 07.09.2026; dokumentierter Zugang laut Auslieferungsbeleg am 09.09.2026; gesetzte Frist 21 Tage ab Zugang, also bis zum 30.09.2026. Ergebnis-Satz: Mit fruchtlosem Ablauf des 30.09.2026 tritt Verzug ein; Verzugszinsen nach § 288 Abs. 1 BGB laufen ab dem 01.10.2026, Deliktszinsen nach § 849 BGB werden nicht gefordert. Kontrollsatz: Die Forderung ist stichtagsbezogen; bei Klageerhebung ist die Nutzungsentschädigung mit dem dann aktuellen Kilometerstand neu zu rechnen.

### Entscheidungstabelle: Zugangsnachweis-Weiche

| Zugangsweg | Beweiswert | Risiko | Empfehlung |
| --- | --- | --- | --- |
| Bote mit Inhalts- und Einwurfprotokoll | hoch: Zeuge für Inhalt, Kuvertierung und Einwurf | Organisationsaufwand; Protokoll muss Inhalt und Zeitpunkt exakt festhalten | Standard bei fristkritischen Schreiben |
| Einwurf-Einschreiben mit Einlieferungs- und Auslieferungsbeleg | mittel bis hoch: Belegkette trägt den Zugang, aber nicht den Inhalt | Inhaltsnachweis fehlt; Belegkette lückenlos archivieren | Standard im Regelfall, Inhalt per Doppel und Aktenvermerk sichern |
| Übergabe-Einschreiben | schwankend: bei Nichtabholung nur Benachrichtigungsschein | Zugang scheitert bei Annahmeverweigerung oder Nichtabholung | vermeiden |
| einfacher Brief | gering: kein Zugangsbeleg | Zugang bestreitbar | nur als Zweitweg neben einem Nachweisweg |
| E-Mail an die Rechtsabteilung | gering bis mittel: nur mit gesichertem Empfängerbezug und Lese- oder Antwortnachweis | Zugangszeitpunkt und Empfängerzuständigkeit streitig | nur ergänzend, nie als allein tragender Nachweis |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Anspruchsaussagen nur aus `references/gepruefte-anker-dieselgate.md` mit Live-Verifikation vor Übernahme in das Schreiben. Keine erfundenen Aktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Vollständig ausformuliertes Anspruchsschreiben (Standardstruktur: Bezug, Sachstand, Forderung, Frist, nächste Schritte, Unterschrift) plus Zustellprotokoll und Fristenkontrolle. Skelette, Halbsätze und reine Aufzählungen sind als Endprodukt verboten; fehlende Falldaten als klar markierte Platzhalter.

## Beispiele

- Eingang: EA189-Fall mit fertiger Schadenstabelle. Kernbefund: Rückabwicklungsforderung 12.052,80 EUR Zug um Zug ist stichtagsfest. Arbeitsprodukt der ersten Antwort: vollständiges Anspruchsschreiben nach Baustein 1 und 2 mit Frist von 21 Tagen als Kalenderdatum plus vorläufiges, aber vollständig ausformuliertes Zustellprotokoll für das Einwurf-Einschreiben; offen bleiben Sendungsnummer, Einlieferungs- und Auslieferungsbeleg.
- Eingang: Thermofenster-Fall, Fahrzeug wird behalten. Kernbefund: Differenzschadensforderung mit Quotenbegründung nach § 287 ZPO. Arbeitsprodukt: Schreiben nach Baustein 3 mit beigefügter Berechnung und Platzhalter für den Restwertbeleg.
- Eingang: Hersteller schweigt nach Fristablauf. Kernbefund: Verzug eingetreten, Zustellprotokoll lückenlos. Arbeitsprodukt: abgeschlossenes Zustellprotokoll mit Verzugsdatum und Übergabevermerk an Skill 13 zur Klagevorbereitung.
