---
name: deliktsrecht-sonstiges-tierhalter-gebaeude
description: "Deliktsrecht Sonstiges Tierhalter Gebaeude: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Deliktsrecht Sonstiges Tierhalter Gebaeude

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Deliktsrecht Sonstiges Tierhalter Gebaeude** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `deliktsrecht-sonstiges-recht` | Prüft sonstige Rechte nach § 823 Abs. 1 BGB: allgemeines Persönlichkeitsrecht, Recht am Gewerbebetrieb und Immaterialgüterrechte. |
| `deliktsrecht-tierhalter-und-gebaeude` | Prüft Tierhalterhaftung § 833 BGB, Haftung des Tieraufsehers § 834 BGB und Gebäudehaftung § 836–838 BGB. |
| `gesamtschuld-und-regress-bgb-bt` | Prüft Gesamtschuld §§ 421 ff. BGB, Innenausgleich nach § 426 BGB und Regress im Schuldrecht BT. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Deliktsrecht Sonstiges Tierhalter Gebaeude**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `deliktsrecht-sonstiges-recht`

**Fokus:** Prüft sonstige Rechte nach § 823 Abs. 1 BGB: allgemeines Persönlichkeitsrecht, Recht am Gewerbebetrieb und Immaterialgüterrechte.

# Deliktsrecht: Sonstiges Recht

## Fachkern: Deliktsrecht: Sonstiges Recht
- **Spezialgegenstand:** Deliktsrecht: Sonstiges Recht; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Sonstige absolute Rechte nach § 823 Abs. 1 BGB prüfen: allgemeines Persönlichkeitsrecht (APR), Recht am eingerichteten und ausgeübten Gewerbebetrieb und Immaterialgüterrechte.

## Normanker

- § 823 Abs. 1 BGB: sonstige Rechte (Auffangtatbestand für absolute Rechte)
- Art. 1 Abs. 1 und Art. 2 Abs. 1 GG: allgemeines Persönlichkeitsrecht als Verfassungsgrundlage
- § 12 BGB: Namensrecht
- § 1004 BGB analog: quasi-negatorischer Unterlassungsanspruch
- UrhG, MarkenG, PatG: spezialgesetzliche Deliktsregeln, die § 823 BGB verdrängen können
- BGH-Linie zum APR: nur nach Live-Prüfung zitieren

## Intake

- Welches Recht ist verletzt: APR, Recht am Gewerbebetrieb, Urheberrecht, Marke?
- Ist das betroffene Recht ein sonstiges Recht im Sinne des § 823 Abs. 1 BGB?
- Greift eine spezialgesetzliche Regelung (UrhG, MarkenG), die § 823 BGB verdrängt?
- Ist ein immaterieller Schaden entstanden (APR-Verletzung: Geldentschädigung)?
- Besteht ein Unterlassungsanspruch nach § 1004 BGB analog?

## Prüfraster

1. Einordnung: absolutes Recht, das den Charakter eines sonstigen Rechts hat
2. APR-Verletzung: Eingriff in Kernbereich der Persönlichkeit, Abwägung mit anderen Grundrechten
3. Recht am Gewerbebetrieb: unmittelbarer betriebsbezogener Eingriff erforderlich (restriktiv)
4. Immaterialgüterrechte: Abgrenzung zu spezialgesetzlichen Haftungsregeln (UrhG, MarkenG)
5. Rechtswidrigkeit: Güter- und Interessenabwägung bei APR besonders relevant
6. Verschulden: Vorsatz oder Fahrlässigkeit
7. Schadensersatz: materielle Schäden und Geldentschädigung bei schwerwiegender APR-Verletzung
8. Unterlassungsanspruch nach § 1004 BGB analog

## Fallstricke

- Reiner Vermögensschaden (z.B. entgangener Gewinn ohne Betriebseingriff) ist kein sonstiges Recht.
- Recht am Gewerbebetrieb ist subsidiär; spezialgesetzliche Regelungen haben Vorrang.
- APR-Verletzung erfordert erheblichen Eingriff; geringfügige Beeinträchtigungen reichen nicht.
- Geldentschädigung wegen APR-Verletzung ist keine Schadenshöhe, sondern eigenständige Anspruchsvoraussetzung.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Rechtsguts-Einordnung (absolutes Recht, sonstiges Recht)
- APR-Abwägungsmatrix
- Schadensberechnung (materiell und immateriell)
- Unterlassungsanspruch und einstweiliger Rechtsschutz

## Qualitätsregeln

- Sonstige Rechte immer restriktiv auslegen; kein Auffangtatbestand für beliebige Schäden.
- APR-Abwägung mit Meinungsfreiheit und Pressefreiheit ausdrücklich vornehmen.
- Spezialgesetze immer auf Vorrang prüfen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- deliktsrecht-paragraph-826-sittenwidrige-schaedigung
- delikt-vertrag-konkurrenz
- workflow-output-gutachten-klage-brief


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__12.html
- https://www.gesetze-im-internet.de/bgb/__1004.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `deliktsrecht-tierhalter-und-gebaeude`

**Fokus:** Prüft Tierhalterhaftung § 833 BGB, Haftung des Tieraufsehers § 834 BGB und Gebäudehaftung § 836–838 BGB.

# Deliktsrecht: Tierhalter und Gebäude

## Fachkern: Deliktsrecht: Tierhalter und Gebäude
- **Spezialgegenstand:** Deliktsrecht: Tierhalter und Gebäude; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Tierhalterhaftung nach §§ 833 und 834 BGB sowie Gebäudehaftung nach §§ 836–838 BGB prüfen: Haltereigenschaft, Gefährdungshaftung und Exkulpationsmöglichkeiten.

## Normanker

- § 833 BGB: Tierhalterhaftung (Gefährdungshaftung bei Luxustieren, Exkulpation bei Nutztieren)
- § 834 BGB: Haftung des Tieraufsehers
- § 836 BGB: Haftung des Grundstücksbesitzers für einstürzende Gebäude oder Anlagen
- § 837 BGB: Haftung des Gebäudebesitzers
- § 838 BGB: Haftung des Gebäudeunterhaltspflichtigen
- § 254 BGB: Mitverschulden des Geschädigten (z.B. Provozierung des Tiers)

## Intake

- Wer ist Tierhalter im Sinne des § 833 BGB (eigene Rechnung und Interesse)?
- Handelt es sich um ein Luxustier (Hund, Pferd) oder ein Nutztier (Hoftier)?
- Kann der Tierhalter bei Nutztieren exkulpieren (§ 833 Satz 2 BGB)?
- Hat das Gebäude eine gefährliche Beschaffenheit und wer ist verantwortlicher Besitzer?
- Liegt ein Mitverschulden des Geschädigten vor?

## Prüfraster

1. Tierhalterhaftung § 833 BGB: Haltereigenschaft (Eigeninteresse und eigene Rechnung)
2. Tiergefahr: hat das typische Tierverhalten den Schaden verursacht?
3. Luxustier oder Nutztier: bei Nutztieren Exkulpation möglich (sorgfältige Beaufsichtigung)
4. Tieraufseher: § 834 BGB, eigene Fahrlässigkeitshaftung mit Exkulpationsmöglichkeit
5. Gebäudehaftung § 836 BGB: fehlerhafte Errichtung oder mangelhafte Unterhaltung; Besitzereigenschaft
6. § 837 BGB: Besitzer eines Bauwerks auf fremdem Grundstück
7. § 838 BGB: Unterhaltungspflichtiger des Gebäudes (auch ohne Besitz)
8. Mitverschulden nach § 254 BGB; Verjährung §§ 195 und 199 BGB

## Fallstricke

- Nutztier-Exkulpation nach § 833 Satz 2 BGB setzt sorgfältige Beaufsichtigung nach den Umständen voraus.
- Gebäudehaftung nach § 836 BGB ist Verschuldenshaftung, aber mit Beweislastumkehr.
- Tierhalter und Tieraufseher können gleichzeitig nach §§ 833 und 834 BGB haften.
- Mitverschulden durch Provokation des Tiers oder unvorsichtiges Verhalten am Gebäude mindern Anspruch.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Haltereigenschafts-Prüfung
- Exkulpations-Checkliste (Tier-/Gebäudehaftung)
- Schadensberechnung mit Mitverschuldensabzug
- Risikoampel

## Qualitätsregeln

- Luxus- vs. Nutztier immer explizit einordnen.
- § 836 BGB-Beweislastumkehr ausdrücklich erwähnen.
- Mitverschulden durch Tierprovokation immer prüfen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- produzentenhaftung-und-verkehrssicherung
- schadensrecht-paragraphen-249-253
- delikt-organisationspflicht


## Quellen

- https://www.gesetze-im-internet.de/bgb/__833.html
- https://www.gesetze-im-internet.de/bgb/__836.html
- https://www.gesetze-im-internet.de/bgb/__837.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `gesamtschuld-und-regress-bgb-bt`

**Fokus:** Prüft Gesamtschuld §§ 421 ff. BGB, Innenausgleich nach § 426 BGB und Regress im Schuldrecht BT.

# Gesamtschuld und Regress BGB BT

## Fachkern: Gesamtschuld und Regress BGB BT
- **Spezialgegenstand:** Gesamtschuld und Regress BGB BT; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Gesamtschuldnerschaft nach §§ 421 ff. BGB prüfen: Entstehungsvoraussetzungen, Wirkungen auf Außen- und Innenverhältnis sowie Regressansprüche.

## Normanker

- § 421 BGB: Gesamtschuld (jeder Schuldner schuldet das Gleiche)
- § 422 BGB: Wirkung der Erfüllung (befreit alle)
- § 423 BGB: Erlass im Außenverhältnis
- § 424 BGB: Gläubigerverzug (wirkt für und gegen alle)
- § 425 BGB: andere Tatsachen (wirken nur für den jeweiligen Schuldner)
- § 426 BGB: Innenausgleich (Ausgleichspflicht untereinander)
- §§ 840 und 840 Abs. 2 BGB: Gesamtschuld im Deliktsrecht und Regress
- § 774 BGB: Legalzession bei Bürgschaft

## Intake

- Wer sind die Gesamtschuldner und welche gemeinsame Schuld besteht?
- Hat einer der Gesamtschuldner geleistet; wie ist die Verteilung im Innenverhältnis?
- Bestehen Einreden einzelner Schuldner, die andere nicht berühren?
- Ist ein Erlass oder Gläubigerverzug eingetreten?
- Gibt es eine vereinbarte oder gesetzliche Innenquote nach § 426 BGB?

## Prüfraster

1. Gesamtschuld entstanden: gleichartige Leistung aus gemeinsamem Rechtsgrund oder getrennten Rechtsgründen?
2. Außenverhältnis: jeder Schuldner haftet auf die ganze Leistung
3. Wirkungen im Außenverhältnis: Erfüllung (§ 422 BGB), Aufrechnung (§ 422 Abs. 2 BGB), Erlass (§ 423 BGB)
4. Tatsachen, die nur einen Schuldner betreffen: § 425 BGB (Verjährung, Mahnung, Urteil)
5. Innenausgleich nach § 426 Abs. 1 BGB: Ausgleichspflicht im Verhältnis der Schuldner zueinander
6. Legalzession nach § 426 Abs. 2 BGB bei Befriedigung des Gläubigers durch einen Schuldner
7. Gesamtschuld im Deliktsrecht: § 840 BGB; Regressverteilung nach Verschuldensbeitrag
8. Verjährung der Ausgleichsansprüche: § 195 BGB

## Fallstricke

- Erlass nur eines Gesamtschuldners befreit die anderen nur dann, wenn Gläubiger dies wollte (§ 423 BGB).
- Verjährung gegen einen Schuldner wirkt nicht gegen die anderen (§ 425 Abs. 2 BGB).
- Innenquote nach § 426 BGB richtet sich nach Veranlassung des Schadens, nicht nach Kopfteilen.
- Legalzession nach § 426 Abs. 2 BGB setzt vollständige Befriedigung des Gläubigers voraus.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gesamtschuldner-Matrix (Außen- und Innenverhältnis)
- Regressberechnung mit Quoten
- Verjährungstabelle
- Handlungsempfehlung und Risikoampel

## Qualitätsregeln

- Außen- und Innenverhältnis immer getrennt prüfen.
- § 423 BGB-Erlass nur mit ausdrücklicher oder konkludenter Befreiungsabsicht des Gläubigers bejahen.
- Innenquote nie pauschal nach Kopfteilen bestimmen.

## Anschluss-Skills

- buergschaft-grundschema-paragraph-765
- schadensrecht-paragraphen-249-253
- deliktsrecht-haftung-fuer-verrichtungen-paragraph-831
- workflow-anspruchslandkarte

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
