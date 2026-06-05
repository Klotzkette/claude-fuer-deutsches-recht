---
name: bgb-bt-kaufrecht-abweichungsvereinbarung-objektive-beweislast
description: "Kaufrecht Abweichungsvereinbarung Objektive Beweislast: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kaufrecht Abweichungsvereinbarung Objektive Beweislast

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kaufrecht Abweichungsvereinbarung Objektive Beweislast** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kaufrecht-abweichungsvereinbarung-objektive-anforderungen-476` | Prüft Abweichungsvereinbarungen von objektiven Anforderungen § 476 BGB beim Verbrauchsgüterkauf. |
| `kaufrecht-beweislast-verjaehrung-digitale-elemente` | Prüft Beweislastumkehr § 477 BGB, Verjährung § 438 BGB und Besonderheiten bei digitalen Elementen. |
| `kaufrecht-dauerhafte-bereitstellung-digitaler-elemente-475c` | Prüft dauerhafte Bereitstellungspflicht digitaler Elemente § 475c BGB und Folgen bei Pflichtverletzung. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Kaufrecht Abweichungsvereinbarung Objektive Beweislast**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kaufrecht-abweichungsvereinbarung-objektive-anforderungen-476`

**Fokus:** Prüft Abweichungsvereinbarungen von objektiven Anforderungen § 476 BGB beim Verbrauchsgüterkauf.

# Kaufrecht: Abweichungsvereinbarung objektive Anforderungen § 476 BGB

## Fachkern: Kaufrecht: Abweichungsvereinbarung objektive Anforderungen § 476 BGB
- **Spezialgegenstand:** Kaufrecht: Abweichungsvereinbarung objektive Anforderungen § 476 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Abweichungsvereinbarungen von den objektiven Anforderungen an die Kaufsache nach § 476 BGB beim Verbrauchsgüterkauf prüfen: Voraussetzungen, Transparenz und Zulässigkeit.

## Normanker

- § 434 BGB: Sachmangel und objektive Anforderungen
- § 476 BGB: Abweichungen von den objektiven Anforderungen beim Verbrauchsgüterkauf
- § 475 BGB: Verbrauchsgüterkauf (Grundnorm)
- § 477 BGB: Beweislastumkehr beim Verbrauchsgüterkauf
- §§ 305–310 BGB: AGB-Kontrolle

## Intake

- Handelt es sich um einen Verbrauchsgüterkauf nach § 474 BGB?
- Wurde ausdrücklich und gesondert vereinbart, dass die Sache bestimmte objektive Anforderungen nicht erfüllen muss?
- Wurde der Verbraucher bei Vertragsschluss über die Abweichung informiert und hat er sie ausdrücklich akzeptiert?
- Liegt ein individualvertraglich ausgehandelter Ausschluss oder eine AGB-Klausel vor?

## Prüfraster

1. Verbrauchsgüterkauf nach § 474 BGB: Unternehmer verkauft bewegliche Sache an Verbraucher
2. Objektive Anforderungen nach § 434 Abs. 3 BGB: Eignung für gewöhnliche Verwendung, übliche Beschaffenheit
3. Abweichungsvereinbarung nach § 476 BGB: ausdrücklich, gesondert, Information des Verbrauchers
4. Ausdrückliche Kenntnisnahme des Verbrauchers von der Abweichung bei Vertragsschluss
5. AGB-Konformität: § 476 BGB schließt stillschweigende Abbedingung über AGB aus
6. Abgrenzung: individualvertragliche Abweichung (zulässig) vs. AGB-Abweichung (unzulässig)
7. Rechtsfolge: wirksame Abweichung schließt Sachmangel bezüglich des abweichenden Merkmals aus
8. Beweislast: Unternehmer muss wirksame Abweichungsvereinbarung beweisen

## Fallstricke

- Pauschal-Klauseln „verkauft wie besichtigt" oder „unter Ausschluss jeder Gewährleistung" sind bei Verbrauchsgüterkauf nach § 476 BGB unzulässig.
- Abweichungsvereinbarung muss gesondert und ausdrücklich erfolgen; bloße Erwähnung im Vertrag genügt nicht.
- Informationspflicht über die Abweichung muss vor Vertragsschluss erfüllt werden.
- § 477 BGB-Beweislastumkehr bleibt trotz wirksamer Abweichungsvereinbarung bestehen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Wirksamkeitsprüfung der Abweichungsvereinbarung
- AGB-Konformitätsprüfung
- Beweislastmatrix
- Handlungsempfehlung für Vertragsgestaltung

## Qualitätsregeln

- § 476 BGB gilt nur beim Verbrauchsgüterkauf; B2B-Verträge unterliegen anderen Regeln.
- Informationspflicht muss vor und nicht erst bei Vertragsschluss erfüllt sein.
- Niemals pauschale Gewährleistungsausschlüsse beim Verbrauchsgüterkauf empfehlen.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- verbrauchsgueterkauf-digitales
- kaufrecht-beweislast-verjaehrung-digitale-elemente
- schnittstelle-bgb-at-methodenlehre-agb


## Quellen

- https://www.gesetze-im-internet.de/bgb/__476.html
- https://www.gesetze-im-internet.de/bgb/__434.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0771
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `kaufrecht-beweislast-verjaehrung-digitale-elemente`

**Fokus:** Prüft Beweislastumkehr § 477 BGB, Verjährung § 438 BGB und Besonderheiten bei digitalen Elementen.

# Kaufrecht: Beweislast, Verjährung und digitale Elemente

## Fachkern: Kaufrecht: Beweislast, Verjährung und digitale Elemente
- **Spezialgegenstand:** Kaufrecht: Beweislast, Verjährung und digitale Elemente; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Beweislastumkehr nach § 477 BGB, Verjährungsfristen nach § 438 BGB und besondere Regeln für Ware mit digitalen Elementen (§§ 475b ff. BGB) prüfen.

## Normanker

- § 438 BGB: Verjährung der Mängelansprüche
- § 477 BGB: Beweislastumkehr beim Verbrauchsgüterkauf
- §§ 475a–475e BGB: Besondere Vorschriften für Verträge über digitale Produkte
- § 475b BGB: Ware mit digitalen Elementen
- § 475c BGB: dauerhafte Bereitstellung digitaler Elemente
- §§ 327 ff. BGB: Verträge über digitale Produkte (Grundregeln)

## Intake

- Ist der Mangel innerhalb von einem Jahr nach Gefahrübergang aufgetreten (§ 477 BGB-Frist)?
- Handelt es sich um Ware mit digitalen Elementen; gilt § 475b oder § 475c BGB?
- Wann wurde der Mangel entdeckt und wann wurden Gewährleistungsansprüche geltend gemacht?
- Liegt Verjährung nach § 438 BGB vor?
- Hat der Verkäufer den Beweis erbracht, dass kein Mangel bei Gefahrübergang vorlag?

## Prüfraster

1. Verbrauchsgüterkauf nach § 474 BGB: Voraussetzung für § 477 BGB
2. Beweislastumkehr nach § 477 BGB: Mangel innerhalb von einem Jahr nach Gefahrübergang vermutet
3. Widerlegung der Vermutung: Verkäufer muss beweisen, dass kein Mangel bei Übergabe bestand
4. Ausnahme: Beweislastumkehr passt nicht mit Art der Sache oder Art des Mangels zusammen
5. Verjährung nach § 438 Abs. 1 BGB: Regelfrist zwei Jahre, fünf Jahre bei Bauwerken, 30 Jahre bei arglistig verschwiegenem Mangel
6. Ware mit digitalen Elementen nach § 475b BGB: Updatepflichten und längere Mängelprüfung
7. Dauerhafte Bereitstellung digitaler Elemente nach § 475c BGB: Verjährung besonders berechnen
8. Verjährungsbeginn: Ablieferung der Sache

## Fallstricke

- § 477 BGB-Frist wurde 2022 von sechs Monaten auf ein Jahr verlängert; altes Recht nicht anwenden.
- Beweislastumkehr schlägt nicht durch, wenn Art des Mangels mit Mängel-bei-Gefahrübergang unvereinbar ist.
- Digitale Elemente mit Updatepflicht verlängern effektiv die Mängelhaftungsphase.
- Arglistig verschwiegener Mangel: dreißigjährige Verjährungsfrist nach § 438 Abs. 3 BGB.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Beweislastverteilung (Käufer/Verkäufer)
- Verjährungskalender mit Fristberechnung
- Digitale-Elemente-Sonderfragen
- Risikoampel

## Qualitätsregeln

- Neue Ein-Jahres-Frist nach § 477 BGB (ab 2022) korrekt anwenden.
- Verjährungsfristen für Bauwerke und digitale Elemente gesondert berechnen.
- Arglistiges Verschweigen immer auf dreißigjährige Frist prüfen.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung
- verbrauchsgueterkauf-digitales
- kaufrecht-ware-mit-digitalen-elementen-475b


## Quellen

- https://www.gesetze-im-internet.de/bgb/__477.html
- https://www.gesetze-im-internet.de/bgb/__438.html
- https://www.gesetze-im-internet.de/bgb/__475b.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `kaufrecht-dauerhafte-bereitstellung-digitaler-elemente-475c`

**Fokus:** Prüft dauerhafte Bereitstellungspflicht digitaler Elemente § 475c BGB und Folgen bei Pflichtverletzung.

# Kaufrecht: Dauerhafte Bereitstellung digitaler Elemente § 475c BGB

## Fachkern: Kaufrecht: Dauerhafte Bereitstellung digitaler Elemente § 475c BGB
- **Spezialgegenstand:** Kaufrecht: Dauerhafte Bereitstellung digitaler Elemente § 475c BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Dauerhaften Bereitstellungspflichten für digitale Elemente nach § 475c BGB prüfen: Pflichten des Verkäufers, Updatepflicht, Mängelhaftung und Abhilfeansprüche des Käufers.

## Normanker

- § 475b BGB: Ware mit digitalen Elementen (Grundnorm)
- § 475c BGB: dauerhafte Bereitstellung digitaler Elemente
- § 475d BGB: besonderer Gewährleistungsausschluss
- § 327 BGB ff.: Verträge über digitale Produkte als Parallelregime
- § 434 Abs. 3 Nr. 3 BGB: Updatepflicht als Bestandteil der Mangelfreiheit

## Intake

- Welche digitalen Elemente sind Bestandteil der Ware (z.B. Betriebssystem, eingebettete Software)?
- Wurde ein dauerhafter Bereitstellungszeitraum vereinbart oder ergibt er sich aus den Umständen?
- Hat der Verkäufer Updates und Sicherheitsupdates rechtzeitig bereitgestellt?
- Wann ist die Bereitstellungspflicht eingestellt worden und wurde der Käufer informiert?

## Prüfraster

1. Ware mit digitalen Elementen nach § 475b BGB: Einordnung des Produkts
2. Dauerhafter Bereitstellungszeitraum nach § 475c BGB: vereinbarter Zeitraum oder normativ bestimmter Zeitraum
3. Updatepflichten: Sicherheitsupdates, Funktionsupdates nach § 434 Abs. 3 Nr. 3 BGB
4. Pflichtverletzung: fehlende, verzögerte oder fehlerhafte Updates
5. Sachmangel bei nicht bereitgestellten Updates: Mängelansprüche nach §§ 437 ff. BGB
6. Informationspflicht gegenüber Käufer bei Einstellung des Supports
7. Ablehnung von Updates durch Käufer: Folgen nach § 475c Abs. 3 BGB
8. Verjährung und Beweislast: § 477 BGB und besondere Fristen bei digitalen Elementen

## Fallstricke

- Sicherheitsupdates müssen bereitgestellt werden, auch wenn keine Funktionserweiterung erfolgt.
- Einstellung des Supports ohne Information des Käufers kann Sachmangel begründen.
- Käufer, der Update verweigert, verliert unter Umständen Mängelansprüche.
- Bereitstellungszeitraum kann länger sein als der kaufrechtliche Gewährleistungszeitraum.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Bereitstellungspflichten-Analyse
- Update-Compliance-Checkliste
- Mängelansprüche bei Update-Pflichtverletzung
- Handlungsempfehlung für Hersteller und Käufer

## Qualitätsregeln

- Ware mit digitalen Elementen immer von reinen Softwareverträgen abgrenzen.
- Sicherheitsupdatepflicht als eigenständige Pflicht herausstellen.
- § 475c Abs. 3 BGB (Update-Verweigerung durch Käufer) nicht vergessen.

## Anschluss-Skills

- kaufrecht-ware-mit-digitalen-elementen-475b
- kaufrecht-updates-sicherheitsupdates-327f-475b
- verbrauchsgueterkauf-digitales
- kaufrecht-beweislast-verjaehrung-digitale-elemente


## Quellen

- https://www.gesetze-im-internet.de/bgb/__475c.html
- https://www.gesetze-im-internet.de/bgb/__327.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0771
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
