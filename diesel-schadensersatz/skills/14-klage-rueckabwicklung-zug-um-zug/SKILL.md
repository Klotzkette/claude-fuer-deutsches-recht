---
name: 14-klage-rueckabwicklung-zug-um-zug
description: "Für eine freigegebene Klage auf großen Schadensersatz und Rückabwicklung Zug um Zug. Erstellt Rubrum, Anträge, Sachverhalt, Subsumtion, Beweise und Anlagen vollständig. Nicht für bloßen Differenzschaden."
---

# Klage auf Rückabwicklung Zug um Zug

## Zweck und Anwendungsfall

Dieser Skill erstellt die Klage der Vorsatzlinie: großer Schadensersatz nach § 826 BGB i.V.m. § 31 BGB bei Prüfstandserkennung (insbesondere EA189). Antrag ist die Zahlung Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs, ergänzt um die Feststellung des Annahmeverzugs — die spätere Vollstreckung braucht beides. Die Klage wird vollständig ausformuliert geliefert: Rubrum, Anträge, Sachverhalt, rechtliche Begründung, Beweisangebote, Anlagen.

## Bedienmodus

Arbeite ergebnisorientiert für Diesel-Geschädigte und ihre Berater. Liefere Fachprodukt, knappe Ampel- und Lückenbewertung und genau einen nächsten Schritt. Tabellen nur bei mindestens drei vergleichbaren Werten oder wiederkehrenden Feldern; sonst vollständige Sätze. Schwierige Rechts- oder RDG-Punkte gehen an eine Rechtsanwältin oder einen Rechtsanwalt und bleiben ohne anwaltliche Verantwortung ungeklärt.

## Erste Antwort

Die erste Antwort liefert sofort eine vorläufige, aber vollständig ausformulierte Klage mit nummerierten Anträgen, Zug-um-Zug-Rechnung samt Rechenweg sowie chronologischem Sachverhalt. Offene Punkte werden an ihrer konkreten Textstelle benannt, insbesondere fehlende FIN, aktueller Kilometerstand, Erwerbs- oder Zugangsdatum und zugehöriger Beleg (`[FIN]`, `[aktueller Kilometerstand]`, `[Datum TT.MM.JJJJ]`, `[Anlage]`); ein Stichwort-Skelett ist auch als erste Antwort unzulässig.

Verboten in der ersten Antwort: Theorie-Vorträge zu § 826 BGB, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche, mehr als drei Rückfragen sowie jede Rückfrage, wenn ein vorläufiger Entwurf mit klar markierten Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Fehlt ein Rechen- oder Rechercheskript, wird ohne Meldungslärm manuell gerechnet und formuliert; ein Werkzeugfehler blockiert nie den Klageentwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Klagewegvermerk aus Skill 13 (Gericht, Streitwert, Klageform).
- Schadenstabelle aus Skill 08, Betroffenheitsnachweis aus Skill 04/05, Chronologie aus Skill 03.
- Anspruchsschreiben und Zustellprotokoll aus Skill 09 (Verzug, Zug-um-Zug-Angebot).
- Verjährungsbefund aus Skill 07 — ohne ihn keine Klage in Altfällen.

## Ablauf / Checkliste

1. Kontrollpunkte vor dem Entwurf: Verjährung, damalige Informationslage und Herstellerverhalten geprüft; konkrete prüfstands- und täuschungsbezogene Vorsatzspur belegt; Betroffenheit, Zuständigkeit und Anwaltszwang geklärt. Ein Kauf nach öffentlicher Verhaltensänderung ist ein erhebliches §-826-Risiko, aber kein undifferenzierter Kalender-Stopp für andere Anspruchsspuren. Bei Fiat/Ducato vor jeder §-826-Klage die konkrete KBA-/MIT-Chronologie und `VIa ZR 314/24` als mögliche Sperre prüfen.
2. Rubrum bauen: Landgericht, Parteien mit ladungsfähiger Anschrift (Hersteller, nicht Händler), Prozessbevollmächtigte, Streitwert.
3. Anträge formulieren: Zahlung des bezifferten Betrags nebst Prozesszinsen Zug um Zug gegen Rückgabe und Übereignung des im Antrag exakt bezeichneten Fahrzeugs (FIN); Feststellung des Annahmeverzugs; vorgerichtliche Rechtsanwaltskosten, soweit einschlägig. Keine Deliktszinsen beantragen.
4. Sachverhalt in Chronologie erzählen: Kauf, Betroffenheit (Motorcode, Rückrufcode), Update-Einladung/-Installation/-Funktion, Kenntnisverlauf, Anspruchsschreiben mit Zugang und Fristablauf — jede Tatsache mit Anlage. Ursprüngliche Manipulation und spätere Update-Handlung nicht in einem Ereignis verschleifen.
5. Anspruch begründen: konkrete prüfstandsbezogene Umschaltlogik, objektive Sittenwidrigkeit, Vorsatz, Täuschungs-/Erwerbskausalität und Zurechnung nach § 31 BGB; Nutzungsvorteile mit aktuellem Kilometerstand rechnen. Dem Heilungseinwand mit `VI ZR 452/19` begegnen: Das Update macht den ungewollten Vertragsschluss nicht rückwirkend gewollt. Update-bedingte weitere Schäden können nach `VIa ZR 419/21` Teil der ursprünglichen Kausalkette sein; einen hilfsweise eigenständigen Update-Anspruch als anderen Streitgegenstand, mit eigener Verjährung und ohne Doppelkompensation abtrennen.
   Behördliche Vorgänge nur soweit für Täuschung, Kenntnis oder Entlastung tatsächlich relevant behandeln. Eine jahrelange Rechtmäßigkeitsbewertung der zuständigen Typgenehmigungsbehörde trotz offengelegter Gegenposition kann im konkret vergleichbaren Fiat/MIT-Sachverhalt § 826 BGB ausschließen; die §-823-Abs.-2-Spur davon ausdrücklich abtrennen.
6. Beweise direkt an den Tatsachen anbieten: Urkunden (Kaufvertrag, Rückrufschreiben), Sachverständigengutachten zur Umschaltlogik, Zeugen; sekundäre Darlegungslast des Herstellers zur Software-Funktionsweise ausdrücklich aktivieren.
7. Anlagen K1 bis Kn aus der Belegmatrix (Skill 02) übernehmen; Annahmeverzugs-Baustein aus dem dokumentierten Rückgabeangebot bauen.
8. Ausformulierungskontrolle: vollständige Sätze, dezimale Gliederung, Urteilsstil; danach Skill `21-bea-versandfertig-schriftsatz-anlagen` für Endfassung, Anlagen, Stempel und Versandpaket. Erst dessen grüne Übergabe geht an Skill 16.

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Eine entscheidungsreife Klage der Vorsatzlinie schreiben, in der Tatsachen, Beweise, §-826-Subsumtion und Zug-um-Zug-Rechnung lückenlos ineinandergreifen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Keine Klage ohne tragfähige Vorsatzspur, bezifferte Nutzung, ordnungsgemäßes Rückgabeangebot und anlagengebundene Beweisangebote.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Grundsatzentscheidung: Einbau der Umschaltlogik (EA189) ist sittenwidrige vorsätzliche Schädigung; Rückabwicklung Zug um Zug abzüglich Nutzungsentschädigung, Zurechnung über § 31 BGB. | Bestätigt |
| BGH, Urt. v. 18.05.2021 - VI ZR 452/19 | Ein späteres Software-Update macht den ungewollten Vertragsschluss nicht rückwirkend gewollt und beseitigt den Erwerbsschaden nicht. | Amtlich geprüft |
| BGH, Beschl. v. 29.09.2021 - VII ZR 126/21 | Prüfstandsbezogene Manipulationssoftware indiziert die arglistige Täuschung der Genehmigungsbehörde. | Bestätigt |
| EuGH, Urt. v. 01.08.2025 - C-666/23 | C-666/23 betrifft die Fahrlässigkeitsentlastung; die besondere §-826-Spur nur anhand konkreten Bescheids, vollständiger Information und Herstellerkenntnis würdigen. | Amtlich geprüft |
| BGH, Beschl. v. 30.06.2026 - VIa ZR 314/24 | Die Fiat/MIT-Linie kann im konkret vergleichbaren Sachverhalt § 826 BGB sperren; technische Konfiguration, Behördenkenntnis und Zeitachse bestreiten und § 823 Abs. 2 BGB ausdrücklich abtrennen. | Amtlich geprüft |
| BGH, Urt. v. 30.07.2020 - VI ZR 354/19; VI ZR 397/19 | Deliktszinsen § 849 BGB nicht beantragen; Zinsantrag auf Verzugs- und Prozesszinsen beschränken. | Bestätigt |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine für die Klageanträge

Die Anträge sind Standardformeln der Rückabwicklungslinie; sie werden vollständig übernommen und nur mit Falldaten gefüllt.

Antrag 1 (Zahlung Zug um Zug):

„1. Die Beklagte wird verurteilt, an die Klägerin [Betrag in EUR] nebst Zinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz seit Rechtshängigkeit zu zahlen, Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs [Hersteller und Modell] mit der Fahrzeug-Identifizierungsnummer [FIN]."

Antrag 2 (Feststellung des Annahmeverzugs):

„2. Es wird festgestellt, dass sich die Beklagte mit der Annahme des in Ziffer 1 bezeichneten Fahrzeugs in Annahmeverzug befindet."

Antrag 3 (vorgerichtliche Rechtsanwaltskosten, nur wenn einschlägig):

„3. Die Beklagte wird verurteilt, die Klägerin von vorgerichtlichen Rechtsanwaltskosten in Höhe von [Betrag in EUR] gegenüber [Name der Kanzlei] freizustellen."

Baustein Nutzungsentschädigung (Begründungsabsatz):

„Die Klägerin lässt sich die gezogenen Nutzungsvorteile anrechnen. Die Nutzungsentschädigung errechnet sich aus dem Kaufpreis, multipliziert mit den seit dem Erwerb gefahrenen Kilometern, geteilt durch die im Erwerbszeitpunkt zu erwartende Restlaufleistung. Bei einem Kaufpreis von [Betrag in EUR], einer Fahrleistung von [gefahrene km] Kilometern seit dem Erwerb und einer Restlaufleistung von [Restlaufleistung km] Kilometern ergibt sich eine Nutzungsentschädigung von [Betrag in EUR]; der Zahlungsantrag beläuft sich danach auf [Betrag in EUR]. Der Kilometerstand wird zur mündlichen Verhandlung aktualisiert. Deliktszinsen nach § 849 BGB werden nicht geltend gemacht."

### Rechenbeispiel Kaufpreis abzüglich Nutzungsentschädigung

1 Ausgangswerte

Kaufpreis 32.500,00 EUR (Neuwagen), Kilometerstand beim Kauf 0 km, aktueller Kilometerstand 98.400 km, erwartete Gesamtlaufleistung 250.000 km; die Restlaufleistung beim Kauf entspricht damit 250.000 km. Beim Gebrauchtwagen gilt stattdessen: Restlaufleistung gleich erwartete Gesamtlaufleistung minus Kilometerstand beim Kauf.

2 Nutzungsentschädigung

32.500,00 EUR mal 98.400 km geteilt durch 250.000 km gleich 12.792,00 EUR.

3 Zahlungsantrag

32.500,00 EUR minus 12.792,00 EUR gleich 19.708,00 EUR, Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs.

4 Kontrollvariante 300.000 km

Setzt das Gericht eine Gesamtlaufleistung von 300.000 km an, sinkt die Nutzungsentschädigung auf 32.500,00 EUR mal 98.400 km geteilt durch 300.000 km gleich 10.660,00 EUR; der Antrag stiege auf 21.840,00 EUR. Beide Varianten werden im Vermerk ausgewiesen, beantragt wird die anwaltlich freigegebene Variante.

5 Ergebnis-Satz

Der Klageantrag zu 1 lautet auf Zahlung von 19.708,00 EUR Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs; die Rechnung ist zur mündlichen Verhandlung mit dem dann aktuellen Kilometerstand fortzuschreiben.

### Entscheidungstabelle Antragsfassung

| Wenn (Befund) | Dann (Antrag/Pfad) | Begründung | Nächster Schritt |
| --- | --- | --- | --- |
| Fahrzeug noch vorhanden, Rückgabeangebot dokumentiert | Zahlung Zug um Zug plus Feststellung Annahmeverzug | Standardfall der Vorsatzlinie; Vollstreckung braucht beide Aussprüche | Anträge 1 und 2 einsetzen |
| Fahrzeug zwischenzeitlich verkauft | Bezifferter Zahlungsantrag auf den Differenzbetrag, keine Zug-um-Zug-Formel | Rückgabe ist unmöglich; Verkaufserlös wird offen angerechnet | Rechnung offen ausweisen |
| Kein wörtliches Rückgabeangebot vor Klage | Annahmeverzugs-Baustein zurückstellen | Der Annahmeverzug setzt ein dokumentiertes Angebot voraus | Angebot über Skill 09 nachholen |
| Kauf nach öffentlicher Verhaltensänderung Herbst 2015 | §-826-Spur kritisch prüfen, Differenzschaden als Alternative | Erhebliches Kausalitäts- und Sittenwidrigkeitsrisiko der Vorsatzlinie | Skill 15 |
| Fiat/Ducato-Sachverhalt mit KBA-/MIT-Chronologie | Vor jeder §-826-Klage Sperrwirkung prüfen | `VIa ZR 314/24` kann § 826 BGB im vergleichbaren Sachverhalt sperren | Anwaltliche Eskalation, § 823 Abs. 2 BGB abtrennen |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Tragende Anker und Gegenrechtsprechung vor Übernahme live verifizieren. `C-666/23` und `VIa ZR 26/24` sind keine Ersatzbegründung für den bei § 826 eigenständig erforderlichen Vorsatz.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Vollständig ausformulierte Klageschrift mit Rubrum, nummerierten Anträgen, Sachverhalt, rechtlicher Begründung, Beweisangeboten und Anlagenverzeichnis in dezimaler Gliederung. Skelett-Schriftsätze sind als Endprodukt verboten; fehlende Falldaten als klar markierte Platzhalter in vollständigen Sätzen.

Übergabe an Skill 21: Entwurfs-/Freigabestatus, offene Platzhalter und Widersprüche, jede Anlagenbezugnahme mit Textanker sowie die anwaltlich freigegebene Haupt-PDF mit SHA-256 getrennt ausweisen. Ein bloßer Textentwurf darf nicht als freigegebene Endfassung in den Paketauftrag gelangen.

## Beispiele

- Eingang: EA189-Golf VII, Kaufpreis 32.500,00 EUR, 98.400 km gefahren, Rückgabeangebot dokumentiert. Kernbefund: Standardfall der Vorsatzlinie. Erste Antwort: vorläufige, aber vollständig ausformulierte Klage mit Anträgen auf Zahlung von 19.708,00 EUR Zug um Zug gegen Rückgabe und Feststellung des Annahmeverzugs sowie Anlagenliste K1 bis K9; als konkrete Lücke bleibt die FIN im Antrag.
- Eingang: Gebrauchtwagenkauf 2016, Zweiterwerberin ohne Kenntnis. Kernbefund: Gebrauchtwagen-Linie trägt, Restlaufleistung ab Kauf-Kilometerstand zu rechnen. Erste Antwort: vorläufige, aber vollständig ausformulierte Klage mit angepasster Nutzungsrechnung und gesondertem Kenntnisvortrag der Zweiterwerberin; fehlende Kauf- und Kilometerbelege sind an den betroffenen Sätzen benannt.
- Eingang: Fahrzeug während des Mandats verkauft. Kernbefund: Zug-um-Zug-Formel unmöglich. Erste Antwort: vorläufige, aber vollständig ausformulierte Klage mit beziffertem Zahlungsantrag auf den Differenzbetrag und offen ausgewiesener Anrechnung des Verkaufserlöses; offen bleibt nur der konkret bezeichnete Verkaufsbeleg.
