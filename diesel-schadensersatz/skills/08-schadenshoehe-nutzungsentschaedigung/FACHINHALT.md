---
name: 08-schadenshoehe-nutzungsentschaedigung
description: "Für Bezifferung, Nutzung, Restwert, Differenzschaden und Wirtschaftlichkeit. Rechnet großen Schadensersatz oder den Rahmen von 5 bis 15 Prozent samt Vorteilsausgleich und Aufzehrung. Benötigt belegte Stichtagswerte."
---

# Schadenshöhe und Nutzungsentschädigung

## Zweck und Anwendungsfall

Dieser Skill rechnet den Schaden für beide Linien getrennt und nachvollziehbar. Großer Schadensersatz: Kaufpreis abzüglich Nutzungsentschädigung, Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs. Differenzschaden: objektiver Minderwert, geschätzt nach § 287 ZPO auf 5 bis 15 Prozent des Kaufpreises vor Vorteilsausgleich. Nutzungsvorteile und objektiver Restwert werden angerechnet, soweit ihre Summe den tatsächlichen Fahrzeugwert bei Erwerb übersteigt; vollständige Aufzehrung ist möglich. Das Rechenblatt trägt Anspruchsschreiben (Skill 09), Klage (Skills 14, 15) und Vergleichsbewertung (Skill 18).

## Bedienmodus

Arbeite für Diesel-Geschädigte und ihre Berater. Liefere zuerst die Schadensrechnung mit Ampel, präziser Lückenliste und genau einem nächsten Schritt; höchstens drei ergebnisrelevante Fragen. Tabelle nur bei mindestens drei vergleichbaren Rechenwerten oder wiederkehrenden Feldern, sonst vollständige Rechenabsätze oder kurze Liste. Schwierige Rechtsfragen an eine Rechtsanwältin oder einen Rechtsanwalt eskalieren; Anwaltszwang und RDG-Grenzen wahren.

## Erste Antwort

Die erste Antwort liefert je freigegebener Anspruchslinie sofort eine vorläufige, aber vollständig ausformulierte Schadensrechnung mit Eingaben, Quellen, Formel, Zwischenschritten, Stichtag und Ergebnis. Tabelle nur bei mindestens drei vergleichbaren Werten oder Methoden, sonst Rechenabsätze. Jeder fehlende Wert erscheint als präzise Lücke mit benötigtem Beleg und gesperrtem Teilergebnis, nie als leere Zelle. Verboten sind Theorie- und Menütexte, Werkzeug-Fehlersuche und mehr als drei Rückfragen. Bei Werkzeugausfall ohne Meldungslärm manuell rechnen.

## Schnelllauf und Übergabe

Verbindlich ist [Promptketten-Schnelllauf](../../references/promptketten-schnelllauf.md). Bei validem Arbeitsstand direkt starten, nur aktiven Skill und nötige Fachreferenz laden und Erledigtes nicht neu herleiten.

Höchstens zwei unabhängige Vorprüfungen parallel. Tabelle nur ab drei vergleichbaren Werten oder wiederkehrenden Feldern. Übergabe als Delta aus Fakten-IDs/Fundstellen, Konflikt-/Gate-Änderungen, Rechtsankern und genau einem nächsten Skill; Fach-, Frist-, Freigabe- und Versandgates sowie die Trennung 21/16 bleiben bestehen.

## Eingaben

- Zahlungs- und Nutzungstabelle aus Skill 02 (Kaufpreis, gefahrene Kilometer, Kilometerstandsjournal).
- Anspruchslinie aus Skill 06 (großer Schadensersatz, Differenzschaden oder beides hilfsweise).
- Restwertangaben, Weiterverkaufserlös, Update-Folgeschäden aus Skill 05, soweit vorhanden.

## Ablauf / Checkliste

1. Rechengrundlagen sichern: Kaufpreis (belegt), Kilometerstand bei Kauf und zum Stichtag, Nutzungsdauer, durchschnittliche Jahresfahrleistung, Fahrzeugart sowie erwartete Gesamt- bzw. Restlaufleistung (häufig 200.000 bis 300.000 km, aber fahrzeugbezogen zu begründen; Ansatz offenlegen und als streitanfällig kennzeichnen).
2. Nutzungsmethoden prüfen: Die lineare Kilometermethode als Standardszenario mit Kaufpreis mal gefahrenen Kilometern geteilt durch erwartete Restlaufleistung rechnen. Bei atypisch geringer Fahrleistung, insbesondere Wohnmobilen oder Sammlerfahrzeugen, zusätzlich eine zeitanteilige Schätzung und nötigenfalls eine weitere begründete Methode als Sensitivität ausweisen. `VIa ZR 549/24` billigt die Zeitmethode im konkreten §-287-Einzelfall, schreibt aber keine Universalmethode vor. Methode, Tatsachenbasis und Ergebnisunterschied transparent begründen.
3. Großen Schadensersatz beziffern: Kaufpreis abzüglich Nutzungsentschädigung, Zug um Zug gegen Rückgabe und Übereignung; Antrag auf Feststellung des Annahmeverzugs vormerken.
4. Differenzschaden in vier Schritten rechnen: Bruttoquote von 5, 10 und 15 Prozent ausweisen; fallbezogene Quote anhand Gewicht des Verstoßes und Risikos behördlicher Nutzungsbeschränkung begründen; Nutzungsvorteile plus objektiven Restwert ermitteln; diese Summe dem tatsächlichen Fahrzeugwert bei Erwerb gegenüberstellen. Nur der positive Überhang wird auf den Brutto-Differenzschaden angerechnet. Den Vorteilsausgleich nach `VIa ZR 335/21`, `VIa ZR 159/22`, `VIa ZR 87/24` und `VIa ZR 613/24` anwenden. Mehrere Einrichtungen erhöhen die Quote nicht automatisch. Vollständige Aufzehrung ist als Nullszenario auszuweisen.
5. Sonderfälle rechnen: Bei Weiterverkauf den tatsächlichen Erlös als Ausgangspunkt erfassen. Vor Verkauf Händlerangebote oder Plattformvergleiche mit Datum, Region, Laufleistung, Ausstattung und Zustand sichern; Kaufangebot, Inserat, Kommunikation, Vertrag, Zahlung und Übergabe archivieren. Der Hersteller beweist einen höheren marktgerechten Wert, während der Käufer Erlös, Zustand, Umstände und Recherche sekundär darlegt. `VIa ZR 473/24` verlangt grundsätzlich kein Gutachten und keine starre Zehnprozentregel. Fahrzeuguntergang, Leasing und Update-Folgeschäden getrennt rechnen.
6. Update-Schaden kontrollieren: Jede Position erhält Ereignis, Vorher-nachher-Differenz, Betrag, Beleg, technische/haftungsrechtliche Kausalität und Anspruchsspur. Erwerbsschaden, Folge in ursprünglicher Kausalkette und eigenständiger Update-Schaden dürfen alternativ begründet, aber nicht kumulativ doppelt kompensiert werden. Reparatur oder Mehrverbrauch nur soweit zusätzlich und nicht bereits im Minderwert/Vorteilsausgleich enthalten.
7. Zinsen richtig ansetzen: Deliktszinsen nach § 849 BGB werden nicht geschuldet; Verzugszinsen ab Fristablauf und Prozesszinsen (§§ 286, 288, 291 BGB) gehören ins Blatt.
8. Rechenbefund je freigegebener Linie ausgeben: Kaufpreis, Kilometer, Restlaufleistung, gegebenenfalls Nutzungsdauer und Jahresfahrleistung, Nutzungsentschädigung, Brutto- und Nettoergebnis, Nutzungsvorteil, Restwert, Stichtag und Zinsen jeweils mit Wert, Quelle, Formel und Begründung. Zeitmethode nur bei sachlichem Anlass; Update-Schaden nur mit Ereignis, Differenzhypothese und Doppelkompensationscheck. Tabelle nur bei mindestens drei Werten oder mehreren Methoden. Fehlende Werte als präzise Beleglücke mit gesperrter Rechnung benennen; keine leeren Zellen.

9. Ampel setzen und übergeben: an Skill 09 (Anspruchsschreiben) oder direkt an Skill 14/15 (Klage).

## Juristische Schreib- und Argumentationsnorm
<!-- BEGIN juristische-argumentation (autogen) -->
**Intention:** Schaden und Vorteilsausgleich als auditierbare Rechnung mit Stichtag, Eingaben, Formel und Sensitivität darstellen.
**Argumentationskern:** Entscheidungssatz zum Tatbestandsmerkmal; Akten-Tatsache, Vortrag, Indiz und Hypothese trennen; Beleg und Fundstelle sowie Beweisangebot zuordnen; Subsumtion und stärkstes Gegenargument ausformulieren; mit Ergebnis, Lücke und nächstem Schritt schließen.
**Freigabegate:** Bruttoquote, Nutzung, Restwert, Erlös und Nettoergebnis sind getrennt; unbekannte Werte sperren die Forderungsfreigabe.
**Arbeitsnorm:** [juristische-schreib-und-argumentationsarchitektur.md](../../references/juristische-schreib-und-argumentationsarchitektur.md)
<!-- END juristische-argumentation (autogen) -->

## Rechtsprechungs-Anker

<!-- BEGIN rechtsprechungs-anker (autogen) -->

Aktiver Satz mit höchstens sechs Ankern. Die vollständige Zuordnung bleibt in `references/gepruefte-anker-dieselgate.md` und im Fünfjahreskorpus; vor externer Verwendung Volltext, Status, Randnummer und Folgeentwicklung live prüfen.

| Anker | Aussage für diesen Skill | Status |
| --- | --- | --- |
| BGH, Urt. v. 25.05.2020 - VI ZR 252/19 (BGHZ 225, 316) | Großer Schadensersatz: Kaufpreis abzüglich Nutzungsentschädigung, Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs. | Bestätigt |
| BGH, Urt. v. 26.06.2023 - VIa ZR 335/21 (BGHZ 237, 245); VIa ZR 533/21; VIa ZR 1031/22 | Differenzschaden: 5 bis 15 Prozent des Kaufpreises vor Vorteilsausgleich; Nutzungsvorteile und objektiven Restwert anrechnen, soweit ihre Summe den tatsächlichen Fahrzeugwert bei Erwerb übersteigt. | Bestätigt |
| EuGH, Urt. v. 01.08.2025 - C-666/23 (Rn. 97 bis 107) | C-666/23 erlaubt Nutzungsanrechnung und eine 15-Prozent-Begrenzung, sofern die Wiedergutmachung im Einzelfall angemessen ist. | Amtlich geprüft |
| BGH, Beschl. v. 02.09.2025 - VIa ZR 87/24; Beschl. v. 16.12.2025 - VIa ZR 613/24 | Der BGH lässt vollständige Aufzehrung durch Nutzungsvorteile und Restwert zu; Kilometerstand, Gesamtlaufleistung, Restwert und Stichtag früh rechnen. | Amtlich geprüft |
| BGH, Urt. v. 04.03.2026 - VIa ZR 473/24 | Beim Verkauf ist der tatsächliche Erlös Ausgangspunkt; Marktvergleich, Zustand und Verkaufsumstände vor Veräußerung beweissicher dokumentieren. | Amtlich geprüft |
| BGH, Beschl. v. 21.07.2026 - VIa ZR 549/24 | Bei atypisch geringer Fahrleistung kann eine zeitanteilige Nutzungsschätzung innerhalb des §-287-Ermessens liegen; Kilometer- und Zeitmethode als Sensitivität rechnen, keine Universalmethode behaupten. | Amtlich geprüft |

<!-- END rechtsprechungs-anker (autogen) -->

## Arbeitsmaterial

### Formulierungsbausteine

**Baustein 1 — Ergebnis-Satz großer Schadensersatz:**

Der Anspruchstellerin steht gegen [Name des Herstellers] ein Anspruch auf Zahlung von [Betrag in EUR] zu, Zug um Zug gegen Rückgabe und Übereignung des Fahrzeugs mit der FIN [FIN]; der Betrag ergibt sich aus dem Kaufpreis von [Betrag in EUR] abzüglich einer Nutzungsentschädigung von [Betrag in EUR] zum Stichtag [Datum TT.MM.JJJJ]. Zusätzlich ist die Feststellung des Annahmeverzugs zu beantragen.

**Baustein 2 — Ergebnis-Satz Differenzschaden mit Quote und Vorteilsausgleich:**

Der Differenzschaden wird nach § 287 ZPO auf [Zahl] Prozent des Kaufpreises, mithin [Betrag in EUR], geschätzt; maßgeblich sind das Gewicht des Verstoßes und das Risiko behördlicher Nutzungsbeschränkungen, hier [Begründung]. Nutzungsvorteil und Restwert von zusammen [Betrag in EUR] übersteigen den tatsächlichen Fahrzeugwert bei Erwerb von [Betrag in EUR] um [Betrag in EUR]; nur dieser Überhang wird angerechnet, sodass [Betrag in EUR] verbleiben.

### Rechenbeispiel: komplettes Rechenwerk

Grunddaten: Neuwagenkauf für 32.500,00 EUR, Kilometerstand bei Kauf 0, am Stichtag 98.400, erwartete Gesamtlaufleistung 250.000 km (fahrzeugbezogen begründet; bei langlebigen Motoren die 300.000-km-Variante als Sensitivität ausweisen).

1 Nutzungsentschädigung

Formel: Kaufpreis mal gefahrene Kilometer geteilt durch erwartete Restlaufleistung beim Kauf. Rechnung: 32.500,00 EUR mal 98.400 geteilt durch 250.000 gleich 12.792,00 EUR; Sensitivität 300.000 km: 10.660,00 EUR.

2 Großer Schadensersatz

32.500,00 EUR abzüglich 12.792,00 EUR gleich 19.708,00 EUR. Ergebnis-Satz: Der große Schadensersatz beträgt zum Stichtag 19.708,00 EUR, zahlbar Zug um Zug gegen Rückgabe und Übereignung; in der 300.000-km-Variante 21.840,00 EUR.

3 Differenzschaden-Korridor

5 Prozent gleich 1.625,00 EUR; 10 Prozent gleich 3.250,00 EUR; 15 Prozent gleich 4.875,00 EUR. Empfohlen werden hier 10 Prozent, weil ein verpflichtender Rückruf vorlag, aber keine Stilllegung drohte.

4 Aufzehrungskontrolle durch Nutzungsvorteil plus Restwert

Fahrzeugwert bei Erwerb: 32.500,00 EUR abzüglich 3.250,00 EUR gleich 29.250,00 EUR. Vorteile: Nutzungsvorteil 12.792,00 EUR plus belegter Restwert 18.500,00 EUR gleich 31.292,00 EUR; anzurechnender Überhang 2.042,00 EUR. Differenzschaden nach Vorteilsausgleich: 3.250,00 EUR abzüglich 2.042,00 EUR gleich 1.208,00 EUR. Kontrollsatz: Ab einem Restwert von 19.708,00 EUR wäre der Differenzschaden vollständig aufgezehrt, weil die Vorteile dann den Kaufpreis erreichen. Ergebnis-Satz: Nach Vorteilsausgleich verbleiben 1.208,00 EUR bei fortlaufender weiterer Aufzehrung; Verzugs- und Prozesszinsen (§§ 286, 288, 291 BGB) kommen hinzu, Deliktszinsen (§ 849 BGB) nicht.

### Entscheidungstabelle: Rechenwegweiche

| Befund | Rechtsfolge / Pfad | Weiter |
| --- | --- | --- |
| Vorsatzlinie freigegeben, Rückabwicklung gewollt | großer Schadensersatz Zug um Zug (VI ZR 252/19); Annahmeverzug vormerken | 09, dann 14 |
| Fahrlässigkeitslinie, Fahrzeug bleibt | Korridor rechnen, Aufzehrung kontrollieren (VIa ZR 335/21) | 09, dann 15 |
| Fahrzeug weiterverkauft | Rechnung auf tatsächlichen Erlös umstellen (VIa ZR 473/24) | Ablauf 5 |
| atypisch geringe Fahrleistung | Zeitmethode als Sensitivität (VIa ZR 549/24) | Ablauf 2 |
| vollständige Aufzehrung erreicht oder absehbar | Nullszenario, keine Forderungsfreigabe (VIa ZR 87/24, VIa ZR 613/24) | zurück an 06 |
| Update-Folgeschaden behauptet | eigene Position mit Differenzhypothese und Doppelkompensationscheck | 05, dann Ablauf 6 |

## Quellenpflicht

Es gilt `references/zitierweise.md`. Jede Zahl mit Quelle und Beleg; Rechtsfolgen nur aus `references/gepruefte-anker-dieselgate.md`. Keine erfundenen Aktenzeichen.

## Ausgabeformat

1. **Kontrollansicht**

   Stelle dem Arbeitsprodukt den kompakten `Kanzlei-Arbeitskopf` mit Status, Ampelgrund, Frist, Quellenstand, Arbeitsprodukt und genau einem `Nächsten Schritt` voran. Er ist eine Kontroll- und Begleitansicht und nie Bestandteil eines Schriftsatzes, einer Anlage oder einer Exportdatei.

2. **Fachprodukt**

   Beleggebundene Schadensrechnung für jede freigegebene Anspruchslinie mit ausgewiesenen Zwischenschritten, Stichtag und Quotenempfehlung in vollständigen, ausformulierten Sätzen. Ab mindestens drei Rechenwerten oder mehreren Methoden kann eine vollständig befüllte Vergleichstabelle verwendet werden; sonst genügen Rechenabsätze. Bloße Stichwortsammlungen und leere Tabellenzellen sind als Endprodukt unzulässig.

## Beispiele

- Eingang: Kaufpreis 27.900 EUR, 142.000 km gefahren, 250.000 km Restlaufleistung, Vorsatzlinie. Kernbefund: Nutzungsentschädigung 15.847,20 EUR. Erste Antwort: Schadenstabelle mit großem Schadensersatz 12.052,80 EUR Zug um Zug und hilfsweisem Korridor 1.395 bis 4.185 EUR samt Ergebnis-Sätzen.
- Eingang: Wohnmobil, 62.000 EUR Kaufpreis, atypisch geringe Jahresfahrleistung. Kernbefund: `VIa ZR 549/24` erlaubt die Zeitmethode als Einzelfallschätzung. Erste Antwort: Schadenstabelle mit Kilometer- und Zeitmethode als Sensitivität; keine Methode automatisch vorrangig.
- Eingang: Fahrzeug 2024 weiterverkauft, Erlösbeleg vorhanden. Kernbefund: tatsächlicher Erlös ist Ausgangspunkt. Erste Antwort: auf den Verkaufserlös umgestellte Rechnung mit offen ausgewiesener Differenz und Platzhalter für den Marktvergleich vor Verkauf.
