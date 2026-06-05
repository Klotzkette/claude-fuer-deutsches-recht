---
name: tausch-schenkung-unechte-goa
description: "Tausch Schenkung Unechte GOA: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Tausch Schenkung Unechte GOA

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Tausch Schenkung Unechte GOA** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tausch-und-schenkung` | Tausch § 480 BGB und Schenkung §§ 516-534 BGB: Unentgeltlichkeit, Form, Widerruf, Notbedarfseinrede. |
| `unechte-goa-paragraph-687` | Unechte GoA § 687 BGB: eigenmächtige Durchführung eines fremden Geschäfts als eigenes. |
| `verbrauchsgueterkauf-digitales` | Verbrauchsgüterkauf §§ 474 ff. BGB und digitale Elemente: Beweislastumkehr, zwingende Normen, §§ 327 ff. BGB. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Tausch Schenkung Unechte GOA**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tausch-und-schenkung`

**Fokus:** Tausch § 480 BGB und Schenkung §§ 516-534 BGB: Unentgeltlichkeit, Form, Widerruf, Notbedarfseinrede.

# Tausch und Schenkung §§ 480 und 516 ff. BGB

## Fachkern: Tausch und Schenkung §§ 480 und 516 ff. BGB
- **Spezialgegenstand:** Tausch und Schenkung §§ 480 und 516 ff. BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Tauschvertrag nach § 480 BGB und Schenkungsrecht (§§ 516 ff. BGB) prüfen: Unentgeltlichkeit, Schenkungsversprechen (Form), Schenkungsvollzug, Widerruf und Notbedarfseinrede.

## Normanker

- § 480 BGB: Tauschvertrag (Kaufrecht gilt entsprechend)
- § 516 BGB: Begriff der Schenkung (Zuwendung aus eigenem Vermögen, Unentgeltlichkeit)
- § 518 BGB: Form des Schenkungsversprechens (notarielle Beurkundung)
- § 519 BGB: Einrede des Notbedarfs
- § 528 BGB: Rückforderung wegen Verarmung des Schenkers
- § 530 BGB: Widerruf der Schenkung wegen groben Undanks
- § 531 BGB: Widerruf nur durch Erklärung gegenüber dem Beschenkten

## Intake

- Liegt Tausch (gegenseitig entgeltliche Übertragungen) oder Schenkung (unentgeltliche Zuwendung) vor?
- Was ist der Gegenstand der Schenkung (bewegliche Sache, Grundstück, Geldbetrag)?
- Wurde ein Schenkungsversprechen notariell beurkundet oder ist die Schenkung bereits vollzogen?
- Wird Widerruf wegen groben Undanks oder Rückforderung wegen Verarmung geltend gemacht?
- Besteht eine Auflage (§ 525 BGB)?

## Prüfraster

1. Abgrenzung Schenkung (unentgeltlich) und Tausch (beiderseitig entgeltlich) sowie gemischte Schenkung
2. Tausch nach § 480 BGB: Kaufrecht anwendbar; Austausch von Sachen statt Sache gegen Geld
3. Schenkungsbegriff: Zuwendung aus eigenem Vermögen (§ 516 BGB), Unentgeltlichkeit, Einigung
4. Form des Schenkungsversprechens: notarielle Beurkundung nach § 518 BGB; Heilung durch Vollzug
5. Schenkung unter Auflage (§ 525 BGB): Auflage ist keine Gegenleistung aber Nebenleistungspflicht
6. Notbedarfseinrede (§ 519 BGB): Schenker kann Erfüllung verweigern, solange er selbst bedürftig ist
7. Rückforderungsrecht bei Verarmung (§ 528 BGB): fünf Jahre nach Vollzug, nur noch vorhandene Bereicherung
8. Widerruf bei grobem Undank (§ 530 BGB): schwerwiegende Verfehlung gegen Schenker oder nahe Angehörige

## Fallstricke

- Vollzug der Schenkung heilt Formmangel des Schenkungsversprechens (§ 518 Abs. 2 BGB).
- Gemischte Schenkung (teils entgeltlich, teils unentgeltlich): komplexe Rechtsfolgen.
- Widerruf nach § 530 BGB setzt schwerwiegende Verfehlung voraus; bloße Undankbarkeit reicht nicht.
- Rückforderung nach § 528 BGB: Beschenkter muss nur noch vorhandene Bereicherung herausgeben.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einordnungsmatrix (Schenkung, Tausch, gemischte Schenkung)
- Formprüfung (Versprechen vs. Vollzug)
- Rückforderungs- und Widerrufsrechte-Übersicht
- Handlungsempfehlung

## Qualitätsregeln

- Unentgeltlichkeit als Kernmerkmal der Schenkung sorgfältig prüfen; auch wirtschaftliche Betrachtung.
- Formheilung durch Vollzug (§ 518 Abs. 2 BGB) immer prüfen, bevor Formmangel bejaht wird.
- Grobem Undank hohe Anforderungen anlegen.

## Anschluss-Skills

- kaufvertrag-grundschema-paragraph-433
- bereicherungsrecht-leistungskondiktion
- vertragstypen-mischvertrag-router


## Quellen

- https://www.gesetze-im-internet.de/bgb/__516.html
- https://www.gesetze-im-internet.de/bgb/__518.html
- https://www.gesetze-im-internet.de/bgb/__530.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `unechte-goa-paragraph-687`

**Fokus:** Unechte GoA § 687 BGB: eigenmächtige Durchführung eines fremden Geschäfts als eigenes.

# Unechte GoA § 687 BGB

## Fachkern: Unechte GoA § 687 BGB
- **Spezialgegenstand:** Unechte GoA § 687 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Unechte Geschäftsführung ohne Auftrag nach § 687 BGB prüfen: § 687 Abs. 1 (Geschäftsanmaßung) und § 687 Abs. 2 (wissentliche Eigengeschäftsführung) und ihre Rechtsfolgen.

## Normanker

- § 687 Abs. 1 BGB: Irrtümliche Eigengeschäftsführung (kein Auftrag, kein GoA-Regime)
- § 687 Abs. 2 BGB: Wissentliche Behandlung eines fremden Geschäfts als eigenes (Geschäftsanmaßung)
- § 687 Abs. 2 S. 1 BGB: Herausgabepflicht und Schadensersatz nach § 678 BGB
- § 687 Abs. 2 S. 2 BGB: Geschäftsherr kann Genehmigung erklären
- §§ 677 ff. BGB: Echte GoA als Ausgangspunkt für Abgrenzung

## Intake

- Hat der Handelnde gewusst, dass das Geschäft ein fremdes ist (§ 687 Abs. 2 BGB)?
- Oder handelte er irrtümlich in der Annahme, ein eigenes Geschäft zu führen (§ 687 Abs. 1 BGB)?
- Welches Ergebnis hat die Geschäftsführung erbracht (Erlös, Nutzungen, Schaden)?
- Hat der Geschäftsherr die Geschäftsführung genehmigt?
- Sind Schadensersatzansprüche nach § 678 BGB im Raum?

## Prüfraster

1. Echte GoA (§§ 677 ff. BGB) abgrenzen: Fremdgeschäftsführungswille und -bewusstsein vorhanden?
2. § 687 Abs. 1 BGB: Handelnder hält irrtümlich fremdes Geschäft für eigenes; kein GoA-Regime, normale Regeln
3. § 687 Abs. 2 BGB: Handelnder weiß, dass es fremdes Geschäft ist, behandelt es aber als eigenes
4. Rechtsfolge § 687 Abs. 2 S. 1 BGB: Herausgabepflicht nach §§ 681 und 667 BGB; Schadensersatz nach § 678 BGB
5. Genehmigung nach § 687 Abs. 2 S. 2 BGB: Geschäftsherr kann GoA-Regime nachträglich anerkennen
6. Aufwendungsersatz: bei § 687 Abs. 2 BGB kein Aufwendungsersatz für den Handelnden

## Fallstricke

- § 687 Abs. 1 BGB ist eigentlich kein GoA-Fall; Handelnder haftet nach normalen Regeln (Delikt, Bereicherung).
- § 687 Abs. 2 BGB: Wissen über Fremdheit ist subjektives Tatbestandsmerkmal; genaue Prüfung nötig.
- Genehmigung nach § 687 Abs. 2 S. 2 BGB kann Aufwendungsersatzanspruch des Handelnden entstehen lassen.
- Abgrenzung zu § 678 BGB: dieser gilt bei echter GoA gegen den Willen des Geschäftsherrn.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einordnungsmatrix (echte GoA vs. § 687 Abs. 1 und 2 BGB)
- Herausgabe- und Schadensersatz-Analyse
- Genehmigungsoption für den Geschäftsherrn
- Risikoampel

## Qualitätsregeln

- Kenntnis der Fremdheit als Schlüsselmerkmal für § 687 Abs. 2 BGB immer sachverhaltsnah prüfen.
- Aufwendungsersatz bei § 687 Abs. 2 BGB ausdrücklich ausschließen.
- § 687 Abs. 1 BGB nicht mit echter GoA verwechseln.

## Anschluss-Skills

- goa-grundschema-paragraph-677
- goa-entgegenstehender-wille-paragraphen-678-679
- bereicherungsrecht-leistungskondiktion


## Quellen

- https://www.gesetze-im-internet.de/bgb/__687.html
- https://www.gesetze-im-internet.de/bgb/__677.html
- https://www.gesetze-im-internet.de/bgb/__678.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `verbrauchsgueterkauf-digitales`

**Fokus:** Verbrauchsgüterkauf §§ 474 ff. BGB und digitale Elemente: Beweislastumkehr, zwingende Normen, §§ 327 ff. BGB.

# Verbrauchsgüterkauf und Digitales §§ 474 ff. BGB

## Fachkern: Verbrauchsgüterkauf und Digitales §§ 474 ff. BGB
- **Spezialgegenstand:** Verbrauchsgüterkauf und Digitales §§ 474 ff. BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Verbrauchsgüterkauf nach §§ 474 ff. BGB und seine Schnittstellen zu §§ 327 ff. BGB für digitale Produkte prüfen: zwingende Normen, Beweislastumkehr, Updatepflichten.

## Normanker

- § 474 BGB: Verbrauchsgüterkauf (Verbraucher kauft von Unternehmer)
- § 475 BGB: Abweichende Vereinbarungen (Verbot der Benachteiligung des Verbrauchers)
- § 476 BGB: Abweichende Vereinbarungen bei Ware mit digitalen Elementen
- § 477 BGB: Beweislastumkehr zugunsten des Verbrauchers
- § 478 BGB: Rückgriff des Unternehmers (Lieferkette)
- §§ 327 ff. BGB: Verträge über digitale Inhalte und digitale Dienstleistungen

## Intake

- Liegt ein Verbrauchsgüterkauf vor (Verbraucher kauft von Unternehmer eine bewegliche Sache)?
- Tritt der Mangel innerhalb von 12 Monaten nach Übergabe auf (Beweislastumkehr § 477 BGB)?
- Enthält die Kaufsache digitale Elemente (§ 475b ff. BGB anwendbar)?
- Haben die Parteien abweichende Vereinbarungen getroffen (Zulässigkeit nach § 476 BGB prüfen)?
- Gibt es Rückgriffsansprüche in der Lieferkette (§ 478 BGB)?

## Prüfraster

1. Verbrauchsgüterkauf-Tatbestand: Verbraucher (§ 13 BGB) kauft von Unternehmer (§ 14 BGB) eine bewegliche Sache
2. Zwingende Normen nach § 475 BGB: Vereinbarungen zum Nachteil des Verbrauchers unwirksam
3. Beweislastumkehr nach § 477 BGB: Mangel, der innerhalb von 12 Monaten auftritt, gilt als bei Übergabe vorhanden
4. Ausnahmen: Unvereinbarkeit des Mangels mit dieser Vermutung (z.B. Verschleiß)
5. Ware mit digitalen Elementen: §§ 475b ff. BGB mit Updatepflichten und besonderen Mangelanforderungen
6. Digitale Produkte (kein Kauf): §§ 327 ff. BGB anstelle von Kaufrecht
7. Rückgriff in der Lieferkette nach § 478 BGB: Unternehmer kann Mängelrechte gegenüber Lieferanten geltend machen
8. Verjährung: § 438 Abs. 1 Nr. 3 BGB (2 Jahre); nicht abkürzbar bei Verbrauchsgüterkauf

## Fallstricke

- Beweislastumkehr gilt nur innerhalb von 12 Monaten (nach 2022er Reform; vorher 6 Monate).
- Gebrauchte Sachen: Gewährleistungsfrist kann auf 1 Jahr verkürzt werden (§ 476 Abs. 2 BGB).
- Fehler bei der Abgrenzung digitales Produkt (§ 327 BGB) vs. Ware mit digitalen Elementen (§ 475b BGB).
- Ausschluss oder Beschränkung von Mängelrechten bei Verbrauchsgüterkauf ist nur in den Grenzen von § 476 BGB möglich.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Verbrauchsgüterkauf-Check (Parteien, Gegenstand, Fristen)
- Beweislastumkehr-Analyse (Zeitpunkt, Vermutung, Ausnahmen)
- Digital-Schnittstellen-Übersicht
- Lieferketten-Rückgriffs-Check

## Qualitätsregeln

- Beweislastumkehr-Zeitraum (12 Monate) und Ausnahmen präzise prüfen.
- Abgrenzung digitales Produkt/Ware mit digitalen Elementen immer vor Normauswahl klären.
- § 476 BGB-Zwingendes immer mitprüfen.

## Anschluss-Skills

- kaufrecht-beweislast-verjaehrung-digitale-elemente
- kaufrecht-ware-mit-digitalen-elementen-475b
- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung


## Quellen

- https://www.gesetze-im-internet.de/bgb/__474.html
- https://www.gesetze-im-internet.de/bgb/__477.html
- https://www.gesetze-im-internet.de/bgb/__475b.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
