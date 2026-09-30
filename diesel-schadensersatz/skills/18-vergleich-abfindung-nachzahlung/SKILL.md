---
name: 18-vergleich-abfindung-nachzahlung
description: "Für Vergleich, Abfindung oder Zahlung nach Klage. Rechnet Nettoergebnis, Kosten und Prozessfolge und formuliert bei Freigabe den Vergleich vollständig. Keine automatische Erledigung oder Klagerücknahme."
---

# Vergleich, Abfindung und Nachzahlung

## Zweck und Anwendungsfall

Der Skill verarbeitet Abfindungsangebote, Prozessvergleiche und Zahlungen nach Klageeinreichung. Er vergleicht sie mit dem gerichtlich erzielbaren Betrag, formuliert titulierbare Texte und steuert den Kostenpfad — ohne automatische Rücknahme.

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Nutze kurze Prüffragen, Ampel, Lückenliste und einen nächsten Schritt. Schwierige Punkte gehen an einen Rechtsanwalt; Anwaltszwang und RDG-Grenzen bleiben gewahrt.

## Erste Antwort

Die erste Antwort liefert sofort ein Arbeitsprodukt: die Entscheidungsvorlage mit zerlegtem Angebot, durchgerechnetem Wirtschaftlichkeitsvergleich (Angebot gegen erwarteten Nettoerlös aus Quote, Beweisrisiko und Kosten) und Ampel-Empfehlung; fehlende Werte stehen als klar markierte Platzhalter mit Nachlieferungsauftrag. Verboten in der ersten Antwort sind Theorie-Vorträge, Skill- oder Menü-Aufzählungen, Werkzeug-Fehlersuche und mehr als drei Rückfragen; eine Rückfrage unterbleibt, wenn eine vorläufige Rechnung mit Platzhaltern möglich ist. Werkzeuge sind Beschleuniger: Sind sie nicht verfügbar oder schlagen sie fehl, wird ohne Meldungslärm manuell gerechnet; ein Werkzeugfehler blockiert nie Bewertung oder Vergleichstext-Entwurf.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Angebot des Herstellers (Schreiben, Vergleichsvorschlag, Zahlungseingang) mit Datum.
- Schadenstabelle aus Skill 08 (eigener Zielwert beider Linien), Verfahrensstand (vor oder nach Rechtshängigkeit).
- Kostenstand: Gerichtskosten, Anwaltskosten, Sachverständigenkosten.

## Ablauf / Checkliste

1. Angebot zerlegen: Betrag und Quote in Prozent des Kaufpreises, Fahrzeug behalten oder zurückgeben, Anrechnung der Nutzungsentschädigung, Kostenregelung, Verzichts- und Abgeltungsklauseln, Titulierbarkeit.
2. Benchmark rechnen: Beim Differenzschaden Bruttoquote und Ergebnis nach Nutzung-/Restwertausgleich ausweisen; bei Rückabwicklung den aktuellen Zug-um-Zug-Saldo. Bei verkauftem oder verkaufsreifem Fahrzeug tatsächlichen Erlös, Zustand und dokumentierte Marktrecherche nach `VIa ZR 473/24` einbeziehen; ein ungesicherter Verkauf unter Marktwert ist ein Kürzungsrisiko. Beweis-, Verjährungs-, Herstellerrollen-, Aufzehrungs-, Kosten- und Dauerrisiko getrennt bepreisen. Kanzlei-Entscheidungslisten sind nur Vergleichsmaterial.
3. Entscheidungsvorlage mit Angebot, eigener Berechnung, Differenz und begründeter Empfehlung ausformulieren.

4. Bei Annahmeempfehlung den Vergleichstext vollständig ausformulieren: Zahlungsbetrag mit Fälligkeit, Fahrzeugregelung, Kostenquote, Abgeltungsumfang eng fassen (keine unbedachten Verzichte auf Update-Folgeschäden), Vollstreckbarkeit bei gerichtlichem Prozessvergleich nach § 794 Abs. 1 Nr. 1 ZPO.
5. Zahlung nach Klageeinreichung verarbeiten: Ereignis datieren (vor oder nach Rechtshängigkeit), Kostenpfad-Matrix bauen und die Wege prüfen — übereinstimmende Erledigung, einseitige Erledigung, Klagerücknahme mit Kostenantrag (§ 269 Abs. 3 S. 3 ZPO), § 91a ZPO; keine automatische Rücknahme, bei Unsicherheit rote Ampel.
6. Teilzahlungen nach Tilgungsbestimmung und § 367 BGB prüfen, offenen Rest und Kostenfolge ausweisen. Nur nachverhandeln, wenn der realistische Nettoerwartungswert nach Aufzehrungs- und Prozessrisiko das Angebot trägt; eine Bruttoquote allein genügt nicht.
7. Ergebnis routen: angenommener Vergleich und Kostenregelung an Skill `19-kosten-vollstreckung-monitoring`; gescheiterte Verhandlung zurück in den Prozesspfad (Skill 17).

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Ein Angebot nicht an der Bruttoforderung, sondern an beweisbarem Nettoanspruch, Kosten, Dauer, Vollstreckung und Mandantenziel messen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Empfehlung und Vollmacht reichen nur so weit wie Vergleichsbetrag, Kostenregelung, Erledigungsumfang und Zahlungsmechanik geprüft sind.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Die gerichtliche Quote von 5 bis 15 Prozent des Kaufpreises ist der Maßstab, an dem jedes Herstellerangebot gemessen wird. | Bestätigt |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Bei tragfähiger Vorsatzlinie ist der Vergleichsmaßstab die volle Rückabwicklung abzüglich Nutzungsentschädigung. | Bestätigt |
| BGH, Urt. v. 30.07.2020 - VI ZR 354/19; VI ZR 397/19 | Zinspositionen im Vergleich an §§ 286, 288, 291 BGB messen; § 849 BGB spielt keine Rolle. | Bestätigt |
| EA288-Instanzsammlung: 131 Entscheidungen, references/ea288-rechtsprechung-instanzen.md | Das EA288-Betragsspektrum ist nur Vergleichsmaterial; Angebot zusätzlich gegen aktuelle Aufzehrungsrechnung, Kosten und Beweisrisiko messen. | Nutzermaterial, live prüfen |
| BGH, Urt. v. 04.03.2026 - VIa ZR 473/24 | Bei verkauftem oder verkaufsreifem Fahrzeug Marktsondierung, Erlös und Zustandsbelege in den Vergleichswert einstellen; ein Verkauf unter Markt kann den Anspruch kürzen. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Prozessvergleich mit Widerrufsvorbehalt und Kostenregelung (titulierbar nach § 794 Abs. 1 Nr. 1 ZPO):**

1

Die Beklagte zahlt an die Klagepartei zur Abgeltung der streitgegenständlichen Ansprüche einen Betrag von [Betrag in EUR], zahlbar binnen 14 Tagen nach Ablauf der Widerrufsfrist auf das Konto [IBAN, Kontoinhaber].

2

Die Klagepartei behält das Fahrzeug mit der FIN [FIN]. Bei vereinbarter Rückgabe gilt stattdessen: Die Zahlung erfolgt Zug um Zug gegen Übergabe und Übereignung des Fahrzeugs mit der FIN [FIN] nebst Schlüsseln und Fahrzeugpapieren am [Übergabeort].

3

Von den Kosten des Rechtsstreits und dieses Vergleichs tragen die Beklagte [Anteil in Prozent] und die Klagepartei [Anteil in Prozent]. Bei hälftiger Einigung gilt stattdessen: Die Kosten des Rechtsstreits und dieses Vergleichs werden gegeneinander aufgehoben.

4

Mit der Erfüllung dieses Vergleichs sind die streitgegenständlichen Ansprüche der Klagepartei gegen die Beklagte wegen der in dem Fahrzeug mit der FIN [FIN] verbauten [Abschalteinrichtung oder Motorsteuerungsfunktion] abgegolten. Nicht erfasst sind Ansprüche wegen künftiger Software-Updates, künftiger behördlicher Maßnahmen oder erst nach Vergleichsschluss bekannt werdender weiterer Funktionen.

5

Jede Partei kann diesen Vergleich durch Schriftsatz gegenüber dem Gericht bis zum [Datum TT.MM.JJJJ] widerrufen; bei fristgerechtem Widerruf gilt der Vergleich als nicht geschlossen und der Rechtsstreit wird fortgesetzt.

**Baustein 2 — Ablehnung eines Abfindungsangebots mit Gegenvorschlag:**

Das mit Schreiben vom [Datum TT.MM.JJJJ] unterbreitete Abfindungsangebot über [Betrag in EUR] nimmt die Anspruchstellerin nicht an. Das Angebot entspricht lediglich [Quote in Prozent] des Kaufpreises von [Betrag in EUR] und bleibt damit hinter dem Erwartungswert zurück, der sich aus der Schätzbandbreite von 5 bis 15 Prozent des Kaufpreises nach § 287 ZPO (BGH, Urt. v. 26.06.2023 - VIa ZR 335/21), der Beweislage und dem Kostenrisiko ergibt; eine Kostenregelung enthält das Angebot nicht. Die Anspruchstellerin ist zur einvernehmlichen Erledigung bereit, wenn Sie bis zum [Datum TT.MM.JJJJ] die Zahlung von [Betrag in EUR] zuzüglich der entstandenen Rechtsverfolgungskosten anbieten. Nach fruchtlosem Fristablauf wird Klage erhoben beziehungsweise das anhängige Verfahren fortgesetzt.

**Baustein 3 — Annahmeerklärung mit Klarstellung der Zahlungsmechanik:**

Die Anspruchstellerin nimmt das Angebot vom [Datum TT.MM.JJJJ] über [Betrag in EUR] an, verbunden mit folgender Klarstellung: Die Zahlung ist bis zum [Datum TT.MM.JJJJ] fällig; sie erfolgt ohne Anrechnungs- oder Verrechnungsvorbehalt auf das Konto [IBAN]. Die Abgeltung beschränkt sich auf die in dem Schreiben bezeichneten Ansprüche wegen der [Abschalteinrichtung oder Motorsteuerungsfunktion] des Fahrzeugs mit der FIN [FIN]; Ansprüche wegen künftiger Software-Updates oder behördlicher Maßnahmen bleiben ausgenommen. Die entstandenen Rechtsverfolgungskosten in Höhe von [Betrag in EUR] sind zusätzlich auszugleichen. Kommt die Zahlung nicht fristgerecht ein, gilt die Annahme als hinfällig und die gerichtliche Durchsetzung wird ohne weitere Ankündigung eingeleitet oder fortgesetzt.

### Rechenbeispiel: Wirtschaftlichkeitsvergleich Angebot gegen erwarteten Nettoerlös

Ausgangswerte: Kaufpreis 32.500,00 EUR, Differenzschadensspur, Angebot des Herstellers 1.950,00 EUR (6 Prozent des Kaufpreises) ohne Kostenregelung, Verfahren noch nicht rechtshängig.

Schritt 1 — Benchmark aus der Quote: Bandbreite nach § 287 ZPO 5 bis 15 Prozent des Kaufpreises, also 1.625,00 EUR bis 4.875,00 EUR; mittlere Quote 10 Prozent ergibt 3.250,00 EUR. Die Aufzehrungskontrolle (Nutzungsvorteil nach der Kilometermethode: 32.500,00 EUR mal 98.400 gefahrene Kilometer geteilt durch 250.000 Kilometer erwartete Restlaufleistung beim Kauf gleich 12.792,00 EUR, zuzüglich Restwert) läuft gesondert über die Schadenstabelle aus Skill 08.

Schritt 2 — Beweisrisiko: Die Erfolgswahrscheinlichkeit wird nach Beleglage mit 70 Prozent angesetzt; erwarteter Erlös 0,70 mal 3.250,00 EUR gleich 2.275,00 EUR.

Schritt 3 — Kostenrisiko: Bei vollständigem Unterliegen beträgt das Kostenrisiko laut Kostenaufstellung der Akte 1.700,00 EUR (Wert aus der Akte, vor Entscheidung konkret nach RVG und GKG beziffern); erwartete Kostenlast 0,30 mal 1.700,00 EUR gleich 510,00 EUR.

Schritt 4 — Erwarteter Nettoerlös: 2.275,00 EUR abzüglich 510,00 EUR gleich 1.765,00 EUR, ohne Bewertung von Verfahrensdauer und Vollstreckungsaufwand.

Ergebnis-Satz: Das Angebot von 1.950,00 EUR liegt über dem erwarteten Nettoerlös von 1.765,00 EUR und ist damit wirtschaftlich annahmefähig; nachzuverhandeln ist allein die fehlende Übernahme der Rechtsverfolgungskosten, denn ohne Kostenregelung schmilzt der Vorsprung des Angebots auf beziehungsweise unter den Erwartungswert.

### Entscheidungstabelle: Kernweiche Angebot, Zahlung, Prozesspfad

| Befund | Rechtsfolge / Pfad | Begründung | Nächster Skill |
| --- | --- | --- | --- |
| Angebot erreicht oder übersteigt den erwarteten Nettoerlös und enthält eine Kostenregelung | Annahme empfehlen, Vergleichstext vollständig ausformulieren | Titulierbarkeit nach § 794 Abs. 1 Nr. 1 ZPO bei Prozessvergleich; enger Abgeltungsumfang sichern | 19 |
| Angebot erreicht den erwarteten Nettoerlös, aber ohne Kostenregelung oder mit weiter Abgeltungsklausel | Nachverhandeln mit Baustein 3, Frist setzen | Kostenlast und unbedachte Verzichte auf Update-Folgeschäden entwerten das Angebot | 18 (Schleife), dann 19 |
| Angebot unterschreitet den erwarteten Nettoerlös deutlich | Ablehnung mit Gegenvorschlag (Baustein 2) | Quote, Beweislage und Kostenrisiko tragen die Fortsetzung | 17 |
| Vollzahlung nach Rechtshängigkeit | Erledigungslage: übereinstimmende Erledigung, einseitige Erledigung oder § 91a ZPO prüfen; keine automatische Rücknahme | Kostenpfad entscheidet über die Kostenlast; § 269 Abs. 3 S. 3 ZPO nur mit Kostenantrag | 19 |
| Teilzahlung ohne Tilgungsbestimmung | Verrechnung nach § 367 BGB, offenen Rest ausweisen und weiterverfolgen | Gesetzliche Reihenfolge Kosten, Zinsen, Hauptforderung | 19 |
| Fahrzeug verkauft oder verkaufsreif | Erlös, Zustand und Marktrecherche in den Vergleichswert einstellen | Ungesicherter Verkauf unter Marktwert ist Kürzungsrisiko (`VIa ZR 473/24`) | 08, dann 18 |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Benchmarks aus der geprüften Anker- und Obergerichtsmatrix; EA288-Betragsvergleiche vor Verwendung am Volltext und auf technische Vergleichbarkeit prüfen. Kostenrecht mit aktuellem Normanker (§§ 91a, 269 ZPO); Teilzahlungen nach § 367 BGB.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Bewertung mit Entscheidungsvorlage, vollständig ausformulierter Vergleichstext und Kostenpfad-Matrix. Skelette und Halbsatz-Klauseln sind als Endprodukt verboten.

## Beispiele

- Eingang: Abfindungsangebot 1.500 EUR bei 24.500 EUR Kaufpreis (rund 6 Prozent), keine Kostenregelung. Kernbefund: Angebot unter dem erwarteten Nettoerlös. Erste Antwort: Entscheidungsvorlage mit Wirtschaftlichkeitsrechnung und ausformuliertem Gegenvorschlag auf Basis der 10-Prozent-Quote zuzüglich Kosten.
- Eingang: gerichtlicher Vergleichsvorschlag mit Fahrzeugrückgabe. Kernbefund: Zug-um-Zug-Saldo trägt die Annahme, Abgeltungsklausel zu weit. Erste Antwort: titulierbarer Vergleichstext mit Zug-um-Zug-Formel, Fälligkeit, Kostenquote, engem Abgeltungsumfang und Widerrufsvorbehalt.
- Eingang: Hersteller zahlt nach Rechtshängigkeit den vollen Betrag. Kernbefund: Erledigungslage, keine automatische Rücknahme. Erste Antwort: Kostenpfad-Matrix mit Empfehlung übereinstimmende Erledigung und vorbereitetem Kostenantrag.
