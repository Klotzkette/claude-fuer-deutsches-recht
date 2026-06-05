---
name: jveg-dolmetscher-uebersetzer-fahrtkosten
description: "Dolmetscher Uebersetzer Fahrtkosten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dolmetscher Uebersetzer Fahrtkosten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Dolmetscher Uebersetzer Fahrtkosten** im Plugin JVEG-Kostenprüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jveg-dolmetscher-uebersetzer-spezial` | Spezialfall Dolmetscher- und Uebersetzerverguetung JVEG: Stundenhonorar, Zeilenhonorar, schwierige Texte, Eilauftraege. Pruefraster Auftragsannahme. |
| `jveg-fahrtkosten` | Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Übernachtungskosten. |
| `jveg-festsetzung-beschwerde` | Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output: Beschwerdeschrift JVEG. Abgrenzung: nicht Antragsgenerator (Erstantrag). |

## Arbeitsweg

Im Plugin JVEG-Kostenprüfer gilt für **Dolmetscher Uebersetzer Fahrtkosten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jveg-dolmetscher-uebersetzer-spezial`

**Fokus:** Spezialfall Dolmetscher- und Uebersetzerverguetung JVEG: Stundenhonorar, Zeilenhonorar, schwierige Texte, Eilauftraege. Pruefraster Auftragsannahme.

# JVEG: Dolmetscher Uebersetzer

## Fachkern: JVEG: Dolmetscher Uebersetzer
- **Spezialgegenstand:** JVEG: Dolmetscher Uebersetzer wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `jveg-fahrtkosten`

**Fokus:** Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Übernachtungskosten.

# JVEG-Fahrtkosten

## Fachkern: JVEG-Fahrtkosten
- **Spezialgegenstand:** JVEG-Fahrtkosten wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe geltend gemachte Fahrtkosten auf Normkonformität nach §§ 5–7 JVEG: Verkehrsmittelwahl, Kilometersatz, Wirtschaftlichkeit und Belegpflicht.

## Triage — kläre vor der Prüfung

1. **Verkehrsmittel:** Eigenes Kfz, Bahn, Flug oder sonstiges Verkehrsmittel?
2. **Personengruppe:** Sachverständiger (§ 5 Abs. 1 JVEG) oder Zeuge (§ 5 Abs. 2 JVEG — niedrigerer Kilometersatz)?
3. **Strecke:** Tatsächlich gefahrene Strecke belegt (Routennachweis, Google Maps, Maut)?
4. **Wirtschaftlichkeit:** Wäre ein günstigeres Verkehrsmittel zumutbar gewesen?
5. **Auslandsanreise:** Liegt ein grenzüberschreitender Reiseweg vor (§ 7 JVEG)?

## Speziallogik: Kilometersatz Zeugen
- Sachverständige und Dolmetscher: § 5 Abs. 1 JVEG — 0,42 EUR/km (unveraendert nach KostRAeG 2025; siehe auch dort die Erhoehung der Stundensaetze).
- Zeugen und Dritte: § 5 Abs. 2 JVEG — 0,35 EUR/km.
- Keine Gleichsetzung; Rollenabgrenzung vor Berechnung zwingend.
- Quelle Norm: https://www.gesetze-im-internet.de/jveg/__5.html

## Rechtsstand 2025/2026 — KostRAeG 2025

Mit dem Kosten- und Betreuungsrechtsaenderungsgesetz 2025 (KostRAeG 2025) sind zum 01.06.2025 die Honorarsaetze des JVEG fuer Sachverstaendige in Anlage 1 zu § 9 JVEG pauschal um 9 Prozent erhoeht worden. Die neuen Saetze gelten nur fuer Auftraege ab 01.06.2025; in Altverfahren bleiben die alten Saetze.

- Synopse JVEG 2025: https://ifsforum.de/fileadmin/user_upload/Aktuelles/Synopse_JVEG__2025.pdf
- Praxis-Hinweis Sachverstaendigenverguetung: https://praxis-grundstuecksbewertung.de/wissenswert/gesetzgebung/jveg-verguetung-sachverstaendige/

## Zentrale Normen
- § 5 JVEG (Fahrtkostenersatz: Kfz, Bahn)
- § 6 JVEG (Reisekosten bei Flügen und Fernreisen)
- § 7 JVEG (Auslandsreise)
- § 19 JVEG (Zeugenfahrtkosten — Verweis auf § 5)
- § 23 JVEG (Dreimonatsfrist)
- § 9 JVEG i.V.m. Anlage 1 (Sachverstaendigen-Stundensaetze, KostRAeG 2025)

## Rechtsprechung
- Aktuelle Rechtsprechung zu § 5 JVEG vor Ausgabe ueber https://dejure.org pruefen.
- BGH-Linie Sachverstaendigenverguetung: Senat fuer Anwaltssachen sowie I., VII., IV. Zivilsenat zustaendig je nach Sachgebiet; Aktenzeichen vor Uebernahme verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Fahrtkosten-Position in Rechnung oder Kostenfestsetzungsantrag.

## Arbeitsweise
1. Verkehrsmittel und Personengruppe identifizieren.
2. Kilometersatz nach § 5 Abs. 1 oder Abs. 2 JVEG zuordnen.
3. Strecke und Belege prüfen.
4. Wirtschaftlichkeitsvergleich (Bahn vs. Kfz).
5. Auslandsanteil nach § 7 JVEG gesondert prüfen.

## Output-Template

| Position | Geltend (EUR) | Norm | Befund | Anerkannt (EUR) |
|---|---|---|---|---|
| Kfz [X km × Y EUR] | 00,00 | § 5 Abs. 1/2 JVEG | [Befund] | 00,00 |
| Bahn (Belege) | 00,00 | § 5 Abs. 1 JVEG | [Befund] | 00,00 |
| Parkkosten (Beleg) | 00,00 | § 5 Abs. 1 JVEG | [Befund] | 00,00 |
| Auslandsanteil | 00,00 | § 7 JVEG | [Befund] | 00,00 |
| **Gesamt** | **00,00** | | | **00,00** |

## Ausgabe
Positionsgenaue Fahrtkostenprüfung mit Kilometersatz, Befund und anerkanntem Betrag.

## Leitplanken
- Zeugen-Kilometersatz (§ 5 Abs. 2 JVEG) niedriger als Sachverständigen-Satz.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 3. `jveg-festsetzung-beschwerde`

**Fokus:** Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output: Beschwerdeschrift JVEG. Abgrenzung: nicht Antragsgenerator (Erstantrag).

# JVEG-Festsetzung-Beschwerde

## Fachkern: JVEG-Festsetzung-Beschwerde
- **Spezialgegenstand:** JVEG-Festsetzung-Beschwerde wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Begleite das Verfahren der gerichtlichen Kostenfestsetzung nach § 4 JVEG und bereite Erinnerung oder Beschwerde gegen Kostenfestsetzungsbeschlüsse vor.

## Triage — kläre vor der Prüfung

1. **Ausgangsbeschluss:** Welcher Kostenfestsetzungsbeschluss ist angegriffen — Datum, Gericht, Aktenzeichen?
2. **Beschwer:** Ist der Beschwerdeführer durch den Beschluss beschwert (Mindestbeschwer § 4 Abs. 3 JVEG)?
3. **Frist:** Ist die Zweiwochenfrist für die Beschwerde noch offen?
4. **Angriffsmittel:** Welche konkreten Fehler (Tatbestandsfehler, Ermessensfehler, Normanwendungsfehler) sollen geltend gemacht werden?
5. **Abhilfe:** Kann das erstinstanzliche Gericht abhelfen (§ 4 Abs. 3 S. 2 JVEG)?

## Zentrale Normen
- § 4 JVEG (Festsetzung durch das Gericht)
- § 4 Abs. 3 JVEG (Beschwerde gegen Festsetzungsbeschluss)
- § 4 Abs. 4 JVEG (Zulassung weiterer Beschwerde)
- § 23 JVEG (Dreimonatsfrist — bereits versäumt?)
- § 68 GKG (Erinnerung gegen Kostenansatz, Analogie)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Erhalt eines Kostenfestsetzungsbeschlusses mit Kürzungen oder Ablehnung.

## Arbeitsweise
1. Beschluss auf Tenor und Begründung analysieren.
2. Beschwer ermitteln (Differenz geltend gemachter Betrag vs. festgesetzter Betrag).
3. Frist prüfen und notieren.
4. Angriffsmittel strukturieren (Tatbestand / Ermessen / Norm).
5. Beschwerdeschrift mit konkreten Anträgen formulieren.

## Output-Template

| Prüfpunkt | Befund |
|---|---|
| Festgesetzter Betrag | 00,00 EUR |
| Geltend gemachter Betrag | 00,00 EUR |
| Beschwer | 00,00 EUR |
| Fristende Beschwerde | TT.MM.JJJJ |
| Angriffsmittel | [Tatbestandsfehler / Ermessensfehler / …] |
| Empfehlung | [Beschwerde / Erinnerung / keine Maßnahme] |

**Beschwerdeschrift-Entwurf:**
[Gericht], Az. [X] — Beschwerde gegen Kostenfestsetzungsbeschluss v. [Datum]

## Ausgabe
Beschwerdeschrift-Entwurf mit strukturierten Angriffsmitteln und Antrag.

## Leitplanken
- Beschwerde nur bei positiver Beschwer; Kostenrisiko ansprechen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
