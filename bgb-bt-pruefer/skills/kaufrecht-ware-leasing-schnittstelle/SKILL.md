---
name: kaufrecht-ware-leasing-schnittstelle
description: "Kaufrecht Ware Leasing Schnittstelle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kaufrecht Ware Leasing Schnittstelle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kaufrecht Ware Leasing Schnittstelle** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kaufrecht-ware-mit-digitalen-elementen-475b` | Prüft Kaufvertrag über Ware mit digitalen Elementen § 475b BGB: Mangelfreiheit, Updatepflichten und Verhältnis zu §§ 327 ff. BGB. |
| `leasing-bgb-bt-schnittstelle` | Leasingvertrag im BGB: Finanzierungsleasing, Mietleasing, Gewährleistungskette und Verbraucherschutz. |
| `mietrecht-mangel-minderung` | Mietrechtliche Mängel und Minderung §§ 536 ff. BGB: Anzeigepflicht, Minderungsquote, Schadensersatz, Kündigung. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Kaufrecht Ware Leasing Schnittstelle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kaufrecht-ware-mit-digitalen-elementen-475b`

**Fokus:** Prüft Kaufvertrag über Ware mit digitalen Elementen § 475b BGB: Mangelfreiheit, Updatepflichten und Verhältnis zu §§ 327 ff. BGB.

# Kaufrecht: Ware mit digitalen Elementen § 475b BGB

## Fachkern: Kaufrecht: Ware mit digitalen Elementen § 475b BGB
- **Spezialgegenstand:** Kaufrecht: Ware mit digitalen Elementen § 475b BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Kaufrechtliche Besonderheiten für Ware mit digitalen Elementen nach § 475b BGB prüfen: Anforderungen an Mangelfreiheit, Updatepflichten und Verhältnis zu den §§ 327 ff. BGB.

## Normanker

- § 475b BGB: Ware mit digitalen Elementen (Definition und Sonderregeln)
- § 434 Abs. 3 Nr. 3 BGB: Updatepflicht als Teil der objektiven Anforderungen
- §§ 327–327u BGB: Verträge über digitale Produkte
- § 476 BGB: Abweichungen von Verbrauchsgüterkauf-Anforderungen
- Richtlinie (EU) 2019/771 Art. 7 und 8: Konformitätsanforderungen für Ware mit digitalen Elementen

## Intake

- Welche digitalen Elemente sind in der Ware enthalten (Firmware, App, eingebettete Software)?
- Sind die digitalen Elemente für die Hauptfunktion notwendig oder optional?
- Welche Updatepflichten hat der Verkäufer/Hersteller übernommen?
- Gelten gleichzeitig Regeln aus § 327 BGB für den digitalen Teil?
- Wie ist das Verhältnis von Kaufrecht und digitalem Produktrecht?

## Prüfraster

1. Einordnung: Ware mit digitalen Elementen nach § 475b BGB oder reines digitales Produkt nach § 327 BGB?
2. Mangelfreiheit der physischen Ware und der digitalen Elemente gleichzeitig prüfen
3. Anforderungen an digitale Elemente: § 434 BGB plus spezifische digitale Anforderungen
4. Updatepflichten nach § 475b Abs. 3 BGB: Zeitraum, Umfang, Sicherheitsupdates
5. Integration der digitalen Elemente: dauerhaft integriert oder separat bereitgestellt?
6. Rechtsverhältnis Käufer-Anbieter der digitalen Elemente (Drittanbieter)?
7. Verbraucherschutz: § 476 BGB gilt auch für digitale Elemente der Ware
8. Verjährung und Beweislast beim gemischten Produkt

## Fallstricke

- Für digitale Elemente können gleichzeitig Kaufrecht und §§ 327 ff. BGB gelten; Abgrenzung ist komplex.
- Drittanbieter-Dienste, die mit der Ware verbunden sind, können eigene Mängelansprüche begründen.
- Updatepflicht kann über den Gewährleistungszeitraum hinausgehen.
- Fehlende Integration der digitalen Elemente kann allein Sachmangel begründen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Produkt-Einordnung (Ware mit/ohne digitale Elemente, reines Digitalprodukt)
- Mangelfreiheits-Analyse (physisch und digital)
- Update-Pflichten-Matrix
- Risikoampel für Vertragsgestaltung

## Qualitätsregeln

- § 475b BGB und §§ 327 ff. BGB immer auf ihr Verhältnis zueinander prüfen.
- Digitale Hauptfunktion und analoge Hauptfunktion der Ware getrennt prüfen.
- DSM-Richtlinienrecht auf aktuelle Auslegung prüfen.

## Anschluss-Skills

- kaufrecht-updates-sicherheitsupdates-327f-475b
- kaufrecht-dauerhafte-bereitstellung-digitaler-elemente-475c
- verbrauchsgueterkauf-digitales
- workflow-livequellen-rechtsstand


## Quellen

- https://www.gesetze-im-internet.de/bgb/__475b.html
- https://www.gesetze-im-internet.de/bgb/__327.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0771
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `leasing-bgb-bt-schnittstelle`

**Fokus:** Leasingvertrag im BGB: Finanzierungsleasing, Mietleasing, Gewährleistungskette und Verbraucherschutz.

# Leasing BGB-BT Schnittstelle

## Fachkern: Leasing BGB-BT Schnittstelle
- **Spezialgegenstand:** Leasing BGB-BT Schnittstelle; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Leasingverträge im Zivilrecht einordnen und prüfen: Abgrenzung Finanzierungsleasing und Mietleasing, Gewährleistungsabtretung, Einwendungsdurchgriff und Verbraucherschutz.

## Normanker

- §§ 535 ff. BGB: Mietrecht als Basisrahmen für Mietleasing
- §§ 433 ff. BGB: Kaufrecht für Finanzierungsleasing-Drei-Parteien-Verhältnis
- § 506 BGB: Entgeltliche Finanzierungshilfe (Verbraucherleasingvertrag)
- §§ 358 und 359 BGB: Verbundener Vertrag und Einwendungsdurchgriff
- § 314 BGB: Kündigung aus wichtigem Grund bei Dauerschuldverhältnissen
- Amtliches BGB: https://www.gesetze-im-internet.de/bgb/

## Intake

- Welche Art von Leasingvertrag liegt vor (Finanzierungsleasing, Mietleasing, Sale-and-lease-back)?
- Wer sind die Parteien (Leasinggeber, Leasingnehmer, Lieferant)?
- Ist der Leasingnehmer Verbraucher oder Unternehmer?
- Welches Problem liegt vor (Mangel am Leasingobjekt, Kündigung, Ablauf)?
- Wurde Gewährleistung abgetreten oder steht der Einwendungsdurchgriff zur Verfügung?

## Prüfraster

1. Vertragstyp bestimmen: Finanzierungsleasing (kaufähnlich) oder Mietleasing (mietähnlich)?
2. Drei-Parteien-Verhältnis beim Finanzierungsleasing: Leasinggeber-Lieferant, Leasinggeber-Leasingnehmer
3. Gewährleistungsabtretung: Hat Leasinggeber Mängelrechte gegen Lieferanten an Leasingnehmer abgetreten?
4. Mangelrechte prüfen: Leasingnehmer kann als Zessionar direkt gegen Lieferanten vorgehen
5. Kündigung des Leasingvertrags: ordentliche und außerordentliche Kündigung nach § 314 BGB
6. Verbraucherschutz: § 506 BGB für Verbraucherleasing; Widerruf nach §§ 495 und 355 BGB
7. Einwendungsdurchgriff nach §§ 358 und 359 BGB bei verbundenen Verträgen
8. Haftung bei vorzeitiger Vertragsauflösung: Restwertrisikoverteilung

## Fallstricke

- Beim Finanzierungsleasing hat der Leasinggeber oft keine eigenen Gewährleistungsansprüche; nur abgetretene Rechte.
- Fehlt die Abtretung, ist der Leasingnehmer bei Mängeln rechtlos gestellt.
- Verbraucherleasingvertrag muss Mindestangaben nach § 506 BGB enthalten; Fehler können Nichtigkeit bewirken.
- Kündigung des Leasingvertrags wegen Mangels setzt in der Regel erfolglosen Nacherfüllungsversuch voraus.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einordnungsmatrix (Leasing-Typ, anwendbares Recht)
- Gewährleistungsketten-Übersicht (Leasinggeber, -nehmer, Lieferant)
- Mängelrechte-Analyse für Leasingnehmer
- Verbraucherschutz-Check

## Qualitätsregeln

- Abgrenzung Finanzierungsleasing und Mietleasing bestimmt das anwendbare Recht.
- Gewährleistungsabtretungsklausel im Leasingvertrag immer prüfen.
- § 506 BGB bei Verbraucherleasing immer mitprüfen.

## Anschluss-Skills

- mietvertrag-grundschema-paragraph-535
- darlehen-und-finanzierung
- kaufvertrag-grundschema-paragraph-433
- vertragstypen-mischvertrag-router


## Quellen

- https://www.gesetze-im-internet.de/bgb/__506.html
- https://www.gesetze-im-internet.de/bgb/__535.html
- https://www.gesetze-im-internet.de/bgb/__358.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `mietrecht-mangel-minderung`

**Fokus:** Mietrechtliche Mängel und Minderung §§ 536 ff. BGB: Anzeigepflicht, Minderungsquote, Schadensersatz, Kündigung.

# Mietrecht: Mangel und Minderung §§ 536 ff. BGB

## Fachkern: Mietrecht: Mangel und Minderung §§ 536 ff. BGB
- **Spezialgegenstand:** Mietrecht: Mangel und Minderung §§ 536 ff. BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Mietrechtliche Mängelansprüche vollständig prüfen: Mangelbegriff nach § 536 BGB, Anzeigepflicht, Minderungsrecht, Aufwendungsersatz und fristlose Kündigung wegen Mängeln.

## Normanker

- § 536 BGB: Mietminderung bei Mängeln der Mietsache
- § 536a BGB: Schadensersatz- und Aufwendungsersatzansprüche bei Mängeln
- § 536b BGB: Kenntnis des Mieters bei Vertragsschluss oder Annahme
- § 536c BGB: Anzeigepflicht des Mieters
- § 543 BGB: Außerordentliche Kündigung aus wichtigem Grund
- § 536 BGB a.F./n.F.: Stichtagsprinzip beim Minderungsrecht

## Intake

- Welche Art von Mietverhältnis liegt vor (Wohnraum, Gewerberaum, Pacht)?
- Was ist der konkrete Mangel (Schimmel, Heizungsausfall, Lärm, öffentlich-rechtliche Beschränkungen)?
- Seit wann besteht der Mangel und wann hat der Mieter ihn angezeigt?
- Welche Minderungsquote ist realistisch?
- Was ist das Ziel (Mangelbeseitigung, Minderung, Schadensersatz, Kündigung)?

## Prüfraster

1. Mangelbegriff: Abweichung der tatsächlichen von der vertraglich vereinbarten Istbeschaffenheit
2. Anzeigepflicht nach § 536c BGB: Zeitpunkt und Form der Mängelanzeige; Folgen bei Unterlassen
3. Kenntnis bei Vertragsschluss: § 536b BGB (Mängelrechte ausgeschlossen, wenn Mangel bekannt war)
4. Minderungsquote bestimmen: anteilige Herabsetzung der Miete (BGH-Rechtsprechung zur Minderungsquote)
5. Schadensersatz nach § 536a Abs. 1 BGB: anfänglicher Mangel oder Verschulden des Vermieters
6. Aufwendungsersatz nach § 536a Abs. 2 BGB: Selbstvornahme nur bei Verzug oder dringendem Bedarf
7. Kündigung nach § 543 Abs. 2 Nr. 1 BGB: erhebliche Beeinträchtigung der Gebrauchstauglichkeit
8. Verjährung nach §§ 195 und 548 BGB; Sonderregel § 548 BGB für Ersatzansprüche nach Rückgabe

## Fallstricke

- Fehlende oder verspätete Mängelanzeige nach § 536c BGB kann Schadensersatzpflicht des Mieters begründen.
- Kenntnis des Mieters beim Einzug schließt Minderung nach § 536b BGB aus, wenn kein ausdrücklicher Vorbehalt.
- Minderungsquote nicht aus BGH-Entscheidungen ableiten ohne Sachverhalt-Abgleich; Quoten sind einzelfallabhängig.
- Bei Schimmelschäden Ursachenforschung (Mieter-Lüftungsverhalten vs. Baumangel) entscheidend.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Mangel-Analyse (Istbeschaffenheit vs. Sollbeschaffenheit)
- Minderungsquoten-Empfehlung mit Begründung
- Anspruchsmatrix (Minderung, Schadensersatz, Aufwendungsersatz, Kündigung)
- Risikoampel für Mietpartei

## Qualitätsregeln

- Anzeigepflicht und Kenntnis des Mieters immer vor Minderungsrecht prüfen.
- BGH-Minderungsquoten nur als Orientierung, nie als Automatismus.
- Wohnraum- und Gewerberaummietrecht unterscheiden.

## Anschluss-Skills

- mietvertrag-grundschema-paragraph-535
- workflow-fristen-ruecktritt-kuendigung
- schadensrecht-paragraphen-249-253
- deliktsrecht-paragraph-823-1


## Quellen

- https://www.gesetze-im-internet.de/bgb/__536.html
- https://www.gesetze-im-internet.de/bgb/__536a.html
- https://www.gesetze-im-internet.de/bgb/__543.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
