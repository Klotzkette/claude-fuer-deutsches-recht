---
name: klausel-bibliothek-kuendigungsklauseln
description: "Klauselbibliothek mit ueber 60 fertigen Bausteinen für deutsche Wirtschaftsvertraege. Sortiert nach Bereichen: Praeambel Definitionen Leistung Verguetung Verzug Gewaehrleistung Haftung Kuendigung Vertragsstrafe Force Majeure Geheimhaltung Datenschutz IP Aenderungen Sprachklausel Schriftform Salvatorisch Gerichtsstand Rechtswahl Schiedsklausel Mediation. Jeder Baustein mit Verwendungshinweis (B2B oder B2C), AGB-Risikohinweis, Alternativen mild und scharf, und bilingualer deutsch-englischer Variante im Word Legal Ai Plugin And Skill For German Lawyers."
---

# Klauselbibliothek-Katalog

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Klauselbereich (z. B. "Vertragsstrafe", "Aufrechnung", "Gerichtsstand")
- Vertragstyp (Liefervertrag, Dienstvertrag, SaaS, M&A, etc.)
- Vertragspartner (B2B oder B2C)
- Verhandlungsstrategie (mild oder scharf)
- Sprache (deutsch oder bilingual)

## Querverweis zum Asset

Die vollstaendige Klauselbibliothek liegt im Plugin unter `references/klausel-bibliothek.md`. Sie enthaelt ueber 60 Bausteine in der oben beschriebenen Struktur. Dieser Skill ist die Bedienungsanleitung.

## Ablauf / Checkliste

1. Bestimmen Sie den Klauselbereich.
2. Schlagen Sie in `references/klausel-bibliothek.md` nach.
3. Pruefen Sie das Verwendungsfeld (B2B / B2C / beides).
4. Pruefen Sie die AGB-Ampel. Bei rot: AGB-Skill `agb-konforme-klauseln-305-310-bgb` konsultieren.
5. Wählen Sie mild oder scharf je nach Verhandlungsstrategie.
6. Passen Sie die Variablen an (Fristen, Betraege, Parteien).
7. Pruefen Sie die Konsistenz mit anderen Klauseln (Definitionen, Querverweise).

## Beispielbausteine

### Verzug B2B

**Gruene Ampel, mild:**

> ### § X Verzug, Verzugszinsen
>
> (1) Befindet sich eine Partei mit der Erbringung einer Geldleistung in Verzug, schuldet sie der anderen Partei Verzugszinsen in Hoehe von neun Prozentpunkten ueber dem jeweiligen Basiszinssatz (§ 247 BGB) gemaess § 288 Abs. 2 BGB.
>
> (2) Die Geltendmachung eines weiteren Schadens bleibt vorbehalten. Auf den Verzugsschaden ist der Verzugszins anzurechnen.
>
> (3) Bei Zahlungsverzug schuldet die Schuldnerin zusaetzlich die Verzugspauschale gemaess § 288 Abs. 5 BGB in Hoehe von 40 EUR.

**Englisch:**

> ### Section X Default, Default Interest
>
> (1) If a party defaults on a payment obligation, it shall pay default interest to the other party at a rate of nine percentage points above the base rate (Section 247 BGB), pursuant to Section 288 (2) BGB.
>
> (2) The right to claim further damages remains reserved. The default interest shall be credited against any damages.
>
> (3) In the event of payment default, the debtor shall additionally pay a flat default fee of EUR 40 pursuant to Section 288 (5) BGB.

### Haftungsbegrenzung B2B

**Gelbe Ampel (in AGB pruefen), Standardformulierung:**

> ### § X Haftung
>
> (1) Die Parteien haften einander für Schaeden, die auf Vorsatz oder grober Fahrlaessigkeit beruhen, unbegrenzt.
>
> (2) Fuer Schaeden aus der Verletzung des Lebens, des Koerpers oder der Gesundheit haftet jede Partei unbegrenzt.
>
> (3) Im Uebrigen haftet jede Partei nur bei Verletzung wesentlicher Vertragspflichten (Kardinalpflichten), die für die Erreichung des Vertragszwecks unverzichtbar sind und auf deren Einhaltung die andere Partei regelmaessig vertrauen darf; in diesem Fall ist die Haftung der Hoehe nach auf den vertragstypischen und vorhersehbaren Schaden begrenzt.
>
> (4) Die Haftung nach Abs. 3 ist je Schadensereignis auf einen Betrag von EUR [...] begrenzt; die Haftung im Vertragsjahr ist insgesamt auf einen Betrag von EUR [...] begrenzt.
>
> (5) Eine Haftung für entgangenen Gewinn und mittelbare Schaeden ist im Rahmen der Begrenzung nach Abs. 3 und 4 ausgeschlossen.
>
> (6) Die Haftung nach dem Produkthaftungsgesetz bleibt unberuehrt.

### Salvatorische Klausel

**Gruene Ampel, Standard:**

> ### § X Salvatorische Klausel
>
> (1) Sollten einzelne Bestimmungen dieses Vertrages ganz oder teilweise unwirksam, undurchfuehrbar oder nichtig sein oder werden, bleibt die Wirksamkeit der uebrigen Bestimmungen davon unberuehrt.
>
> (2) An die Stelle der unwirksamen, undurchfuehrbaren oder nichtigen Bestimmung tritt diejenige wirksame Bestimmung, die dem von den Parteien verfolgten wirtschaftlichen Zweck am naechsten kommt. Gleiches gilt im Fall einer Regelungsluecke.

**Englisch:**

> ### Section X Severability
>
> (1) Should any individual provision of this Agreement be or become invalid, unenforceable or void in whole or in part, this shall not affect the validity of the remaining provisions.
>
> (2) The invalid, unenforceable or void provision shall be replaced by such valid provision as comes closest to the commercial purpose pursued by the parties. The same shall apply in the case of a gap in the provisions.

### Vertragsstrafe B2B

**Gelbe Ampel (AGB-Pruefung), mild:**

> ### § X Vertragsstrafe
>
> (1) Bei schuldhafter Verletzung der Geheimhaltungspflicht gemaess § Y schuldet die verletzende Partei der anderen Partei eine Vertragsstrafe in Hoehe von EUR 25.000 pro Einzelverstoss.
>
> (2) Bei einem Dauerverstoss ist die Vertragsstrafe für jeden angefangenen Monat des Verstosses gesondert zu zahlen, hoechstens jedoch sechsmal je Pflichtverletzung.
>
> (3) Die Geltendmachung eines weitergehenden Schadensersatzes bleibt vorbehalten. Die Vertragsstrafe ist auf den Schadensersatzanspruch anzurechnen.

### Geheimhaltung NDA Standalone

**Gruene Ampel, B2B-Standalone, mild:**

> ### § 1 Vertrauliche Informationen
>
> (1) "Vertrauliche Informationen" sind alle Informationen, die einer Partei (die "Empfangende Partei") von der anderen Partei (die "Offenlegende Partei") im Rahmen der Vertragsverhandlungen oder der Vertragsdurchfuehrung in muendlicher, schriftlicher, elektronischer oder anderer Form zugaenglich gemacht werden, einschliesslich Geschaefts-, Betriebs- oder Berufsgeheimnissen im Sinne des § 2 GeschGehG.
>
> (2) Vertrauliche Informationen sind insbesondere: technische Informationen, Geschaeftsplaene, Finanzdaten, Kunden- und Lieferantenlisten, Personaldaten, Vertragsbedingungen, Quellcode und Algorithmen.
>
> ### § 2 Geheimhaltungspflicht
>
> (1) Die Empfangende Partei verpflichtet sich, Vertrauliche Informationen vertraulich zu behandeln, nicht ohne vorherige schriftliche Zustimmung der Offenlegenden Partei an Dritte weiterzugeben und ausschliesslich für die in diesem Vertrag genannten Zwecke zu verwenden.
>
> (2) Die Empfangende Partei darf Vertrauliche Informationen nur solchen Mitarbeitern, Beratern und Vertragspartnern zugaenglich machen, die für die Vertragsdurchfuehrung notwendigerweise davon Kenntnis haben muessen ("need to know") und die in vergleichbarer Weise zur Geheimhaltung verpflichtet sind.
>
> ### § 3 Ausnahmen
>
> Die Geheimhaltungspflicht gilt nicht für Informationen, die:
>
> a) der Empfangenden Partei zum Zeitpunkt der Offenlegung bereits rechtmaessig bekannt waren;
> b) ohne Verschulden der Empfangenden Partei der Oeffentlichkeit zugaenglich werden;
> c) von der Empfangenden Partei selbststaendig und ohne Verwendung Vertraulicher Informationen entwickelt wurden;
> d) aufgrund einer gesetzlichen oder behoerdlichen Anordnung offenzulegen sind; in diesem Fall wird die Empfangende Partei die Offenlegende Partei vor Offenlegung unverzueglich benachrichtigen, soweit gesetzlich zulaessig.
>
> ### § 4 Dauer
>
> Die Geheimhaltungspflicht beginnt mit Unterzeichnung dieses Vertrages und besteht für eine Dauer von fuenf Jahren nach Beendigung des Hauptvertrages oder, falls kein Hauptvertrag geschlossen wird, fuenf Jahre ab Unterzeichnung dieses Vertrages. Fuer Geschäftsgeheimnisse im Sinne des § 2 GeschGehG gilt die Geheimhaltungspflicht zeitlich unbegrenzt fort, solange die gesetzlichen Voraussetzungen vorliegen.

### Force Majeure

**Gruene Ampel, mild:**

> ### § X Hoehere Gewalt
>
> (1) Keine Partei haftet für die Nichterfuellung oder verspaetete Erfuellung ihrer Verpflichtungen aus diesem Vertrag, soweit die Nichterfuellung oder Verspaetung auf einem Ereignis hoeherer Gewalt beruht.
>
> (2) Ereignisse hoeherer Gewalt sind solche, die ausserhalb des zumutbaren Einflussbereichs der betroffenen Partei liegen und trotz Anwendung der im Verkehr erforderlichen Sorgfalt nicht abgewendet werden konnten, insbesondere: Naturkatastrophen, Epidemien und Pandemien, kriegerische Auseinandersetzungen, Terrorakte, behoerdliche Anordnungen mit Auswirkung auf die Vertragserfuellung, allgemeine Energie- und Rohstoffknappheit, Streiks und Aussperrungen, sofern nicht von der betroffenen Partei verschuldet, sowie Cyber-Angriffe auf wesentliche Infrastruktur.
>
> (3) Die von hoeherer Gewalt betroffene Partei wird die andere Partei unverzueglich nach Kenntniserlangung schriftlich benachrichtigen und nach besten Kraeften versuchen, die Auswirkungen zu beseitigen oder zu mindern.
>
> (4) Dauert ein Ereignis hoeherer Gewalt laenger als 90 zusammenhaengende Kalendertage oder insgesamt 180 Kalendertage innerhalb eines Vertragsjahres, ist jede Partei berechtigt, den Vertrag mit einer Frist von 30 Kalendertagen schriftlich zu kuendigen.

### Gerichtsstand und Rechtswahl (deutsches Recht)

**Gruene Ampel B2B:**

> ### § X Anwendbares Recht und Gerichtsstand
>
> (1) Dieser Vertrag unterliegt ausschliesslich dem Recht der Bundesrepublik Deutschland. Die Anwendung des UN-Kaufrechts (CISG) wird ausgeschlossen.
>
> (2) Ausschliesslicher Gerichtsstand für alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag ist der Sitz der Auftraggeberin. Die Auftraggeberin ist berechtigt, die Auftragnehmerin auch an deren allgemeinem Gerichtsstand zu verklagen.

### Schriftformklausel mit Ausnahme der Schriftformklausel

**Gruene Ampel, Standard:**

> ### § X Aenderungen, Schriftform
>
> (1) Aenderungen und Ergaenzungen dieses Vertrages beduerfen der Schriftform. Dies gilt auch für die Aufhebung oder Aenderung dieser Schriftformklausel.
>
> (2) Die Schriftform ist gewahrt durch eine eigenhaendig oder mittels qualifizierter elektronischer Signatur unterzeichnete Vertragsurkunde, die in einem einheitlichen Dokument oder in mehreren gleichlautenden Ausfertigungen vorliegt.
>
> (3) Muendliche Nebenabreden bestehen nicht.

## Pflege

Die Bibliothek wird regelmaessig aktualisiert. Aenderungen in der Gesetzgebung (z. B. Verbraucherschutzgesetze, AGB-Novellen) erfordern Anpassungen. Stand der Klauseln ist im Dateikopf von `references/klausel-bibliothek.md` vermerkt.

## Quellen (Stand 05/2026)

- §§ 247, 257, 288, 305-310, 339 BGB; §§ 2 GeschGehG; CISG.
- Klauseln basieren auf gaengiger Vertragspraxis in deutschen Kanzleien und sind vom Nutzer fallbezogen zu pruefen.
- Zitierweise: `references/zitierweise.md`.

