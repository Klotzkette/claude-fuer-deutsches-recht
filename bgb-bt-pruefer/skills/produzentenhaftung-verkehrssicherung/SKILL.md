---
name: produzentenhaftung-verkehrssicherung
description: "Produzentenhaftung Verkehrssicherung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Produzentenhaftung Verkehrssicherung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Produzentenhaftung Verkehrssicherung** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `produzentenhaftung-und-verkehrssicherung` | Produzentenhaftung § 823 BGB und Produkthaftungsgesetz: Fehler, Kausalität, Verkehrssicherungspflichten. |
| `schadensrecht-paragraphen-249-253` | Schadensrecht §§ 249-253 BGB: Naturalrestitution, Schadensberechnung, Vermögensschaden, Schmerzensgeld. |
| `geschaeftsbesorgung-auftrag-mandat` | Prüft entgeltliche Geschäftsbesorgung § 675 BGB, Anwalts- und Steuerberaterauftrag und Haftung für Beratungsfehler. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Produzentenhaftung Verkehrssicherung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `produzentenhaftung-und-verkehrssicherung`

**Fokus:** Produzentenhaftung § 823 BGB und Produkthaftungsgesetz: Fehler, Kausalität, Verkehrssicherungspflichten.

# Produzentenhaftung und Verkehrssicherung

## Fachkern: Produzentenhaftung und Verkehrssicherung
- **Spezialgegenstand:** Produzentenhaftung und Verkehrssicherung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Produzentenhaftung nach § 823 Abs. 1 BGB und dem Produkthaftungsgesetz (ProdHaftG) prüfen: Produktfehler, Kausalität, Beweislast und Abgrenzung zur allgemeinen Verkehrssicherungspflicht.

## Normanker

- § 823 Abs. 1 BGB: Deliktische Haftung für Rechtsgutsverletzungen (Produzentenverantwortung)
- §§ 1 ff. ProdHaftG: Gefährdungshaftung für fehlerhafte Produkte
- § 3 ProdHaftG: Produktfehler (Konstruktionsfehler, Fabrikationsfehler, Instruktionsfehler)
- § 4 ProdHaftG: Hersteller, Quasi-Hersteller, Importeur
- § 8 ProdHaftG: Haftungsausschlüsse
- Amtliches BGB: https://www.gesetze-im-internet.de/bgb/

## Intake

- Wer ist Hersteller (Produzent, Quasi-Hersteller, Importeur, Händler)?
- Welcher Fehlertyp liegt vor (Konstruktion, Fabrikation, Instruktion, Produktbeobachtungspflicht)?
- Welcher Schaden ist entstanden (Körperschaden, Sachschaden, reiner Vermögensschaden)?
- Ist das Produkt in Verkehr gebracht worden?
- Ist der Entwicklungsrisikobehalt nach § 1 Abs. 2 Nr. 5 ProdHaftG relevant?

## Prüfraster

1. Anspruchsgrundlage wählen: § 823 Abs. 1 BGB (Verschuldenshaftung) oder ProdHaftG (Gefährdungshaftung) oder beide
2. Produkt-Begriff nach § 2 ProdHaftG: bewegliche Sache (auch als Teil eines anderen Produkts) oder Strom
3. Fehlertypen nach § 3 ProdHaftG: Konstruktionsfehler, Fabrikationsfehler, Instruktionsfehler
4. Produktbeobachtungspflicht nach Inverkehrbringen (§ 823 BGB: weitergehend als ProdHaftG)
5. Inverkehrbringen: Zeitpunkt und Rechtsfolgen (§ 1 Abs. 2 Nr. 1 bis 3 ProdHaftG)
6. Kausalität zwischen Fehler und Schaden: Anscheinsbeweis bei Produzentenhaftung
7. Hersteller-Beweislast beim ProdHaftG: Hersteller muss Fehlerfreiheit oder Ausschlussgründe beweisen
8. Haftungsausschlüsse nach § 1 Abs. 2 ProdHaftG: Entwicklungsrisiko, zwingende Rechtsnormen
9. Haftungsbegrenzungen: § 10 ProdHaftG (Höchstgrenzen), § 9 ProdHaftG (Mitverschulden)

## Fallstricke

- § 823 BGB setzt Verschulden voraus; ProdHaftG ist Gefährdungshaftung ohne Verschulden.
- Instruktionsfehler oft übersehen: mangelhafte Gebrauchsanleitung kann Fehler begründen.
- Entwicklungsrisiko-Einwand nach § 1 Abs. 2 Nr. 5 ProdHaftG: Hersteller muss Exkulpation beweisen.
- Bei reinen Vermögensschäden hilft ProdHaftG nicht; dann nur § 823 BGB oder § 826 BGB.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Fehler-Typen-Analyse (Konstruktion, Fabrikation, Instruktion)
- Anspruchsgrundlagen-Matrix (§ 823 BGB vs. ProdHaftG)
- Haftungsausschluss-Prüfung
- Schadensersatz-Berechnung und Obergrenzen

## Qualitätsregeln

- § 823 BGB und ProdHaftG immer nebeneinander prüfen; unterschiedliche Beweislasten.
- Produktbeobachtungspflicht auch nach Inverkehrbringen mitprüfen.
- Entwicklungsrisiko-Einwand sachverhaltsnah bewerten.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- delikt-organisationspflicht
- delikt-verkehrspflicht-digital
- schadensrecht-paragraphen-249-253


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/prodhaftg/
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024L2853
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `schadensrecht-paragraphen-249-253`

**Fokus:** Schadensrecht §§ 249-253 BGB: Naturalrestitution, Schadensberechnung, Vermögensschaden, Schmerzensgeld.

# Schadensrecht §§ 249-253 BGB

## Fachkern: Schadensrecht §§ 249-253 BGB
- **Spezialgegenstand:** Schadensrecht §§ 249-253 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Schadensersatzansprüche nach §§ 249-253 BGB vollständig ausarbeiten: Grundsatz der Naturalrestitution, Differenzhypothese, Schmerzensgeld und Sonderprobleme wie Vorteilsausgleichung und Mitverschulden.

## Normanker

- § 249 BGB: Art und Umfang des Schadensersatzes (Naturalrestitution)
- § 250 BGB: Schadensersatz in Geld nach Fristsetzung
- § 251 BGB: Schadensersatz in Geld ohne Fristsetzung
- § 252 BGB: Entgangener Gewinn
- § 253 BGB: Immaterieller Schaden (Schmerzensgeld)
- § 254 BGB: Mitverschulden des Geschädigten
- § 255 BGB: Herausgabe von Ersatz bei Übernahme der Schadensersatzpflicht

## Intake

- Welche Anspruchsgrundlage liegt vor (§ 280 BGB, § 823 BGB, § 831 BGB, Gefährdungshaftung)?
- Welche Schadensposten werden geltend gemacht (Sachschaden, Vermögensschaden, Schmerzensgeld)?
- Besteht ein Mitverschulden des Geschädigten?
- Liegt ein Vorteil vor, der auszugleichen wäre (Vorteilsausgleichung)?
- Wurde Naturalrestitution verlangt oder ist Geldersatz erforderlich?

## Prüfraster

1. Schadensentstehung und Kausalität: Adäquanzkausalität und Schutzzweck der Norm
2. Naturalrestitution nach § 249 BGB: Wiederherstellung des ursprünglichen Zustands als Primärform
3. Geldersatz nach §§ 250 und 251 BGB: bei Unmöglichkeit oder unverhältnismäßigem Aufwand
4. Vermögensschaden: Differenzhypothese (Vergleich des tatsächlichen mit dem hypothetischen Vermögen)
5. Entgangener Gewinn nach § 252 BGB: wahrscheinlicher Gewinn nach normalem Lauf der Dinge
6. Immaterieller Schaden: § 253 BGB setzt eine der dort genannten Anspruchsgrundlagen voraus
7. Schmerzensgeld-Bemessung: Ausgleich und Genugtuung; Genugtuungsfunktion bei vorsätzlichen Taten
8. Mitverschulden nach § 254 BGB: Quotenbildung, Verursachungsbeiträge und Obliegenheitsverletzungen
9. Vorteilsausgleichung: schadenmindernde Vorteile, die durch das schädigende Ereignis entstanden sind

## Fallstricke

- § 253 BGB setzt gesetzliche oder vertragliche Anspruchsgrundlage voraus; kein allgemeines Schmerzensgeld.
- Vorteilsausgleichung darf nicht zur sachwidrigen Entlastung des Schädigers führen; Grenzen beachten.
- Entgangener Gewinn muss wahrscheinlich sein, nicht sicher; aber bloße Möglichkeit reicht nicht.
- Mitverschulden nach § 254 BGB: auch Obliegenheitsverletzung bei der Schadensabwendung (§ 254 Abs. 2 BGB).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Schadensposten-Übersicht (Sachschaden, Vermögensschaden, Schmerzensgeld, entgangener Gewinn)
- Naturalrestitution vs. Geldersatz-Analyse
- Mitverschuldens-Quote
- Gesamtschadensberechnung

## Qualitätsregeln

- Kausalität und Schutzzweck der Norm immer als Filter für Schadensposten verwenden.
- § 253 BGB-Voraussetzungen (Körperverletzung, Freiheitsentzug, sexuelle Selbstbestimmung) immer prüfen.
- Vorteilsausgleichung aktiv in Schadensberechnung einbauen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- gesamtschuld-und-regress-bgb-bt
- werkvertrag-maengelrechte
- mietrecht-mangel-minderung

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `geschaeftsbesorgung-auftrag-mandat`

**Fokus:** Prüft entgeltliche Geschäftsbesorgung § 675 BGB, Anwalts- und Steuerberaterauftrag und Haftung für Beratungsfehler.

# Geschäftsbesorgung, Auftrag und Mandat

## Fachkern: Geschäftsbesorgung, Auftrag und Mandat
- **Spezialgegenstand:** Geschäftsbesorgung, Auftrag und Mandat; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Entgeltliche Geschäftsbesorgung nach § 675 BGB prüfen: Anwaltsmandat, Steuerberatungsvertrag, Haftung für Beratungsfehler und Herausgabepflichten.

## Normanker

- § 675 BGB: Geschäftsbesorgungsvertrag (entgeltlicher Auftrag)
- §§ 662–674 BGB: Auftragsrecht als Grundlage
- § 280 Abs. 1 BGB: Schadensersatz wegen Schlechtleistung
- BRAO §§ 43 ff.: Anwaltspflichten (als Schutzgesetz im Sinne des § 823 Abs. 2 BGB)
- StBerG: Steuerberaterpflichten
- § 31 BGB: Haftung der Berufsgesellschaft für Organe
- BGH-Linie zu Anwaltshaftung: nur nach Live-Prüfung zitieren

## Intake

- Welcher Aufgabenbereich wurde übertragen: Rechtsberatung, Steuerberatung, Vermögensverwaltung?
- Wurde ein Fehler bei der Beratung oder Interessenwahrnehmung begangen?
- Welcher Schaden ist entstanden (entgangene Frist, falscher Rat, Nichtdurchsetzung)?
- Liegt hypothetisches Alternativverhalten vor (hätte der Mandant bei richtiger Beratung anders gehandelt)?
- Welche Verjährungsfrist gilt?

## Prüfraster

1. Geschäftsbesorgungsvertrag nach § 675 BGB: Entgeltlichkeit und Pflichtenumfang bestimmen
2. Pflichtverletzung: Beratungsfehler, Fristversäumnis, unzulässige Interessenkollision
3. Schadensersatz nach § 280 Abs. 1 BGB: Schuldverhältnis, Pflichtwidrigkeit, Vertretenmüssen
4. Kausalität: hätte der Mandant bei richtiger Beratung einen anderen Entschluss gefasst?
5. Schaden: entgangener Prozessgewinn, gezahlte Steuernachzahlungen, unnötige Kosten
6. Mitverschulden des Mandanten nach § 254 BGB
7. Herausgabepflicht nach § 667 BGB: Unterlagen, Vorschüsse, Erlöse
8. Verjährung: §§ 195 und 199 BGB; Hemmung durch Verhandlungen

## Fallstricke

- Hypothetischer Kausalverlauf bei Beratungsfehlern ist vom Geschädigten darzulegen.
- Interessenkollision kann zur sofortigen Kündigung nach § 627 BGB berechtigen.
- Verjährung beginnt ab Kenntniserlangung vom Fehler (nicht vom Schaden).
- Haftungsfreizeichnungsklauseln in AGB der Berater unterliegen der AGB-Kontrolle.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Pflichtverletzungs-Analyse (Beratungsfehler, Fristversäumnis, Interessenkollision)
- Kausalitätsnachweis (hypothetischer Alternativverlauf)
- Schadensberechnung
- Verjährungskalender

## Qualitätsregeln

- Beratungspflicht und Durchführungspflicht immer getrennt prüfen.
- Hypothetischer Kausalverlauf explizit darstellen.
- Anwaltspflichten aus BRAO immer mit BGB-Pflichten verknüpfen.

## Anschluss-Skills

- auftrag-und-unentgeltliche-taetigkeit
- goa-grundschema-paragraph-677
- maklervertrag-und-provision
- workflow-red-team-gegenseite


## Quellen

- https://www.gesetze-im-internet.de/bgb/__675.html
- https://www.gesetze-im-internet.de/bgb/__662.html
- https://www.gesetze-im-internet.de/bgb/__667.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
