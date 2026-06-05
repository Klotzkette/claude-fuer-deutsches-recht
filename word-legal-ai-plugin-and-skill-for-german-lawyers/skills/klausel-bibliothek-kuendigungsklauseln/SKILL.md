---
name: klausel-bibliothek-kuendigungsklauseln
description: "Klausel Bibliothek Kuendigungsklauseln: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klausel Bibliothek Kuendigungsklauseln

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Klausel Bibliothek Kuendigungsklauseln** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klausel-bibliothek-katalog` | Klauselbibliothek mit ueber 60 fertigen Bausteinen fuer deutsche Wirtschaftsvertraege. Sortiert nach Bereichen: Praeambel Definitionen Leistung Verguetung Verzug Gewaehrleistung Haftung Kuendigung Vertragsstrafe Force Majeure Geheimhaltung Datenschutz IP Aenderungen Sprachklausel Schriftform Salvatorisch Gerichtsstand Rechtswahl Schiedsklausel Mediation. Jeder Baustein mit Verwendungshinweis (B2B oder B2C), AGB-Risikohinweis, Alternativen mild und scharf, und bilingualer deutsch-englischer Variante. |
| `kuendigungsklauseln-und-vertragsbeendigung` | Drafting und Prüfung von Kündigungsklauseln. Ordentliche Kündigung mit Frist und Form, außerordentliche Kündigung aus wichtigem Grund nach § 314 BGB mit Abmahnung und Frist nach Kenntnis, Zugang nach § 130 BGB sowie Form nach §§ 126 (Schriftform), 126a (elektronische Form) und 126b BGB (Textform). Behandelt die Folgewirkungen auf Boilerplate (Geheimhaltung, Schiedsklausel, Gerichtsstand wirken fort) und liefert Mustertexte für ordentliche und außerordentliche Kündigung. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Klausel Bibliothek Kuendigungsklauseln**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klausel-bibliothek-katalog`

**Fokus:** Klauselbibliothek mit ueber 60 fertigen Bausteinen fuer deutsche Wirtschaftsvertraege. Sortiert nach Bereichen: Praeambel Definitionen Leistung Verguetung Verzug Gewaehrleistung Haftung Kuendigung Vertragsstrafe Force Majeure Geheimhaltung Datenschutz IP Aenderungen Sprachklausel Schriftform Salvatorisch Gerichtsstand Rechtswahl Schiedsklausel Mediation. Jeder Baustein mit Verwendungshinweis (B2B oder B2C), AGB-Risikohinweis, Alternativen mild und scharf, und bilingualer deutsch-englischer Variante.

# Klauselbibliothek-Katalog

## Zweck

Dieser Skill ist ein abrufbarer Katalog fertiger Klauselbausteine fuer deutsche Wirtschaftsvertraege. Er ersetzt nicht das Drafting, sondern beschleunigt es: Stelle nicht jeden Vertrag bei null auf, sondern starte mit getesteten Bausteinen und passe sie an die konkrete Mandatsfrage an.

Jeder Baustein hat:
- **Verwendungshinweis** (B2B / B2C / beides)
- **AGB-Risiko** (gruen / gelb / rot)
- **Alternative mild** (verhandlungsoffen)
- **Alternative scharf** (Verhandlungsmaximum)
- **Englische Fassung** fuer bilinguale Vertraege

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
5. Waehlen Sie mild oder scharf je nach Verhandlungsstrategie.
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
> (1) Die Parteien haften einander fuer Schaeden, die auf Vorsatz oder grober Fahrlaessigkeit beruhen, unbegrenzt.
>
> (2) Fuer Schaeden aus der Verletzung des Lebens, des Koerpers oder der Gesundheit haftet jede Partei unbegrenzt.
>
> (3) Im Uebrigen haftet jede Partei nur bei Verletzung wesentlicher Vertragspflichten (Kardinalpflichten), die fuer die Erreichung des Vertragszwecks unverzichtbar sind und auf deren Einhaltung die andere Partei regelmaessig vertrauen darf; in diesem Fall ist die Haftung der Hoehe nach auf den vertragstypischen und vorhersehbaren Schaden begrenzt.
>
> (4) Die Haftung nach Abs. 3 ist je Schadensereignis auf einen Betrag von EUR [...] begrenzt; die Haftung im Vertragsjahr ist insgesamt auf einen Betrag von EUR [...] begrenzt.
>
> (5) Eine Haftung fuer entgangenen Gewinn und mittelbare Schaeden ist im Rahmen der Begrenzung nach Abs. 3 und 4 ausgeschlossen.
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
> (2) Bei einem Dauerverstoss ist die Vertragsstrafe fuer jeden angefangenen Monat des Verstosses gesondert zu zahlen, hoechstens jedoch sechsmal je Pflichtverletzung.
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
> (1) Die Empfangende Partei verpflichtet sich, Vertrauliche Informationen vertraulich zu behandeln, nicht ohne vorherige schriftliche Zustimmung der Offenlegenden Partei an Dritte weiterzugeben und ausschliesslich fuer die in diesem Vertrag genannten Zwecke zu verwenden.
>
> (2) Die Empfangende Partei darf Vertrauliche Informationen nur solchen Mitarbeitern, Beratern und Vertragspartnern zugaenglich machen, die fuer die Vertragsdurchfuehrung notwendigerweise davon Kenntnis haben muessen ("need to know") und die in vergleichbarer Weise zur Geheimhaltung verpflichtet sind.
>
> ### § 3 Ausnahmen
>
> Die Geheimhaltungspflicht gilt nicht fuer Informationen, die:
>
> a) der Empfangenden Partei zum Zeitpunkt der Offenlegung bereits rechtmaessig bekannt waren;
> b) ohne Verschulden der Empfangenden Partei der Oeffentlichkeit zugaenglich werden;
> c) von der Empfangenden Partei selbststaendig und ohne Verwendung Vertraulicher Informationen entwickelt wurden;
> d) aufgrund einer gesetzlichen oder behoerdlichen Anordnung offenzulegen sind; in diesem Fall wird die Empfangende Partei die Offenlegende Partei vor Offenlegung unverzueglich benachrichtigen, soweit gesetzlich zulaessig.
>
> ### § 4 Dauer
>
> Die Geheimhaltungspflicht beginnt mit Unterzeichnung dieses Vertrages und besteht fuer eine Dauer von fuenf Jahren nach Beendigung des Hauptvertrages oder, falls kein Hauptvertrag geschlossen wird, fuenf Jahre ab Unterzeichnung dieses Vertrages. Fuer Geschaeftsgeheimnisse im Sinne des § 2 GeschGehG gilt die Geheimhaltungspflicht zeitlich unbegrenzt fort, solange die gesetzlichen Voraussetzungen vorliegen.

### Force Majeure

**Gruene Ampel, mild:**

> ### § X Hoehere Gewalt
>
> (1) Keine Partei haftet fuer die Nichterfuellung oder verspaetete Erfuellung ihrer Verpflichtungen aus diesem Vertrag, soweit die Nichterfuellung oder Verspaetung auf einem Ereignis hoeherer Gewalt beruht.
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
> (2) Ausschliesslicher Gerichtsstand fuer alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag ist der Sitz der Auftraggeberin. Die Auftraggeberin ist berechtigt, die Auftragnehmerin auch an deren allgemeinem Gerichtsstand zu verklagen.

### Schriftformklausel mit Ausnahme der Schriftformklausel

**Gruene Ampel, Standard:**

> ### § X Aenderungen, Schriftform
>
> (1) Aenderungen und Ergaenzungen dieses Vertrages beduerfen der Schriftform. Dies gilt auch fuer die Aufhebung oder Aenderung dieser Schriftformklausel.
>
> (2) Die Schriftform ist gewahrt durch eine eigenhaendig oder mittels qualifizierter elektronischer Signatur unterzeichnete Vertragsurkunde, die in einem einheitlichen Dokument oder in mehreren gleichlautenden Ausfertigungen vorliegt.
>
> (3) Muendliche Nebenabreden bestehen nicht.

## Pflege

Die Bibliothek wird regelmaessig aktualisiert. Aenderungen in der Gesetzgebung (z. B. Verbraucherschutzgesetze, AGB-Novellen) erfordern Anpassungen. Stand der Klauseln ist im Dateikopf von `references/klausel-bibliothek.md` vermerkt.

## Querverweise

- `agb-konforme-klauseln-305-310-bgb` fuer AGB-Pruefung
- `boilerplate-klauseln-katalog` fuer Standardklauseln-Drafting
- `bilingual-drafting-deutsch-englisch` fuer Uebersetzungen
- `defensive-drafting-fallen-erkennen` fuer Verteidigungsformulierungen
- `vertragsstrafe-339-bgb` fuer Pruefung der Vertragsstrafe
- `haftungsausschluss-und-haftungsbegrenzung` fuer Haftungsklauseln

## Quellen (Stand 05/2026)

- §§ 247, 257, 288, 305-310, 339 BGB; §§ 2 GeschGehG; CISG.
- Klauseln basieren auf gaengiger Vertragspraxis in deutschen Kanzleien und sind vom Nutzer fallbezogen zu pruefen.
- Zitierweise: `references/zitierweise.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `kuendigungsklauseln-und-vertragsbeendigung`

**Fokus:** Drafting und Prüfung von Kündigungsklauseln. Ordentliche Kündigung mit Frist und Form, außerordentliche Kündigung aus wichtigem Grund nach § 314 BGB mit Abmahnung und Frist nach Kenntnis, Zugang nach § 130 BGB sowie Form nach §§ 126 (Schriftform), 126a (elektronische Form) und 126b BGB (Textform). Behandelt die Folgewirkungen auf Boilerplate (Geheimhaltung, Schiedsklausel, Gerichtsstand wirken fort) und liefert Mustertexte für ordentliche und außerordentliche Kündigung.

# Kündigungsklauseln und Vertragsbeendigung

## Zweck

Dieser Skill unterstützt Sie beim Aufbau und der Prüfung von Beendigungsregelungen in Dauerschuldverhältnissen. Eine saubere Beendigungsklausel definiert Voraussetzungen, Erklärungsweg, Zugang und Folgen für den Vertrag und seine Boilerplate. Schlechtes Drafting führt regelmäßig zu unklarer Beendigung, Streit über den Zeitpunkt der Beendigung und Verlust durchsetzbarer Folgepflichten.

## Eingaben

- Vertragstyp (Dauerschuldverhältnis, Werkvertrag, Dienstvertrag, Lizenz, Lieferrahmenvertrag).
- Laufzeit (befristet, unbefristet, mit Verlängerungsmechanismus).
- Parteien (B2B, B2C, Arbeitsverhältnis).
- Gewünschte Beendigungsgründe (ordentlich, außerordentlich, Sonderkündigung bei Change of Control, Insolvenz).
- Erwartete Folgepflichten (Rückgabe, Geheimhaltung, Wettbewerbsverbot, Lizenzlauf).

## Rechtlicher und methodischer Rahmen

- **Ordentliche Kündigung:** Beim unbefristeten Dauerschuldverhältnis grundsätzlich zulässig, Frist nach Vertrag oder Gesetz (z. B. §§ 580a, 621, 622 BGB).
- **Außerordentliche Kündigung:** § 314 BGB als allgemeine Norm für Dauerschuldverhältnisse. Voraussetzungen: wichtiger Grund, Unzumutbarkeit der Fortsetzung, regelmäßig Abmahnung (§ 314 II BGB) und Kündigung in angemessener Frist nach Kenntnis (§ 314 III BGB).
- **Form:** § 125 BGB Folge des Formmangels (Nichtigkeit). § 126 BGB Schriftform mit eigenhändiger Unterschrift; § 126a BGB qualifizierte elektronische Signatur; § 126b BGB Textform (lesbare Erklärung, dauerhafter Datenträger, Person erkennbar). Bei doppelter Schriftformklausel zusätzlich beachten: Aufhebung der Schriftform durch konkludente Praxis ist trotz Klausel möglich, soweit die Klausel selbst formfrei abdingbar ist.
- **Zugang:** § 130 I BGB Wirksamwerden mit Zugang. Bei Streit Beweislast beim Kündigenden. Übermittlungswege regeln (Einschreiben, Kurier, Bote, beA).
- **Folgen:** Beendigung wirkt für die Zukunft (ex nunc bei § 314 BGB). Rücktritt nach §§ 323, 324, 326 BGB unterscheiden (ex tunc). Boilerplate-Klauseln wie Geheimhaltung, Schiedsabrede und Gerichtsstand bleiben in Kraft, sofern dies klargestellt ist.
- **Sonderregeln:** Verbraucherkredit (§ 500 BGB), Wohnraummiete (§§ 568 ff. BGB), Arbeitsverhältnisse (KSchG), Versicherungsverträge (VVG).

## Ablauf / Checkliste

1. Vertragstyp und Laufzeit klären; befristete Verträge nur außerordentlich kündbar, soweit nicht ausnahmsweise zugelassen.
2. Ordentliche Kündigungsfristen festlegen; Symmetrie der Parteien prüfen (in AGB einseitige Verkürzungen kritisch).
3. Außerordentliche Kündigungstatbestände beispielhaft auflisten, dabei "insbesondere"-Katalog wählen, damit § 314 BGB nicht abgeschnitten wird.
4. Abmahnungspflicht regeln; bei besonderem Vertrauensbruch Verzicht klarstellen (vgl. § 314 II 3 BGB).
5. Frist nach Kenntnis (§ 314 III BGB) im Mandat dokumentieren; vertraglich ggf. Zeitfenster setzen.
6. Form festlegen: § 126 BGB Schriftform, § 126b BGB Textform oder § 126a BGB qualifizierte elektronische Signatur. Kein Mischmasch.
7. Zugangsweg definieren (Adresse, beA, definierte Mailadresse). Mitteilungs- und Wohnsitzwechselpflicht regeln.
8. Folgen der Beendigung adressieren: Rückgabe, Datenlöschung, Geheimhaltung, Lizenzauslauf, Restzahlungen.
9. Survival-Klausel formulieren: welche Bestimmungen überleben die Beendigung (Geheimhaltung, Schiedsklausel, Rechtswahl, Gerichtsstand, Haftungsregeln, IP-Bestimmungen).
10. Sonderkündigungsrechte prüfen (Change of Control, Insolvenz; § 119 InsO beachten: Insolvenzklauseln teils unwirksam).

## Typische Drafting-Fehler

- Schriftform- und Textformklausel kombiniert ohne Hierarchie: unklar, welches Formerfordernis gilt.
- Ausschluss der außerordentlichen Kündigung in AGB: unwirksam, weil § 314 BGB nicht abdingbar ist (h. M.).
- Fehlende Survival-Klausel: Geheimhaltung läuft mit der Vertragsbeendigung aus.
- Fristbeginn nicht definiert: Streit über Zugang und Fristberechnung.
- "Mit sofortiger Wirkung" ohne wichtigen Grund: Risiko der Umdeutung in ordentliche Kündigung mit längerer Frist.
- Doppelte Schriftformklausel ohne Rücksicht auf § 305b BGB: Individualabrede geht vor.
- Insolvenzklauseln ohne Berücksichtigung von § 119 InsO und der BGH-Rechtsprechung zu Lösungsklauseln.

## Ausgabeformat

- Klauselentwurf für ordentliche und außerordentliche Kündigung in Urteilsstil.
- Survival-Klausel als eigener Absatz.
- Mustertext für Kündigungserklärung mit Datum, Bezug, Begründung (außerordentlich), Frist, Unterschrift.
- Risikohinweise zu Form, Zugang und Beweislast.

## Beispiele

Mustertext (Vertragsklausel, B2B-Dauerschuldverhältnis):

> § X Laufzeit und Beendigung
> (1) Der Vertrag wird auf unbestimmte Zeit geschlossen. Er kann von jeder Partei mit einer Frist von drei Monaten zum Ende eines Kalenderquartals ordentlich gekündigt werden.
> (2) Das Recht zur außerordentlichen Kündigung aus wichtigem Grund (§ 314 BGB) bleibt unberührt. Ein wichtiger Grund liegt insbesondere vor, wenn eine Partei eine wesentliche Vertragspflicht trotz schriftlicher Abmahnung mit angemessener Frist nicht erfüllt oder über das Vermögen einer Partei das Insolvenzverfahren eröffnet wird, soweit dies gesetzlich zulässig ist.
> (3) Jede Kündigung bedarf der Schriftform (§ 126 BGB). Die elektronische Form (§ 126a BGB) ist ausgeschlossen.
> (4) Folgende Regelungen gelten über das Vertragsende hinaus fort: § Y (Geheimhaltung), § Z (Rechtswahl und Gerichtsstand), § A (Haftung), § B (IP).

Mustertext (außerordentliche Kündigungserklärung):

> Sehr geehrte Damen und Herren,
> in Sachen Rahmenliefervertrag vom ... kündige ich namens und in Vollmacht der ... GmbH den Vertrag außerordentlich aus wichtigem Grund mit sofortiger Wirkung. Der wichtige Grund liegt in der mit Schreiben vom ... abgemahnten und seither nicht behobenen Nichtlieferung gemäß Abruf ... Hilfsweise erkläre ich die ordentliche Kündigung zum nächstmöglichen Termin.

## Querverweise

- `boilerplate-klauseln-katalog` – Survival-, Schriftform- und Gerichtsstandsklausel.
- `geheimhaltung-nda-vertraulichkeit` – Fortwirkung der Geheimhaltung nach Vertragsende.
- `schriftform-und-textform-bgb` (Plugin gleichen Namens) – Vertiefung zu §§ 126, 126a, 126b BGB.
- `vertragsstrafe-339-bgb` – Strafversprechen mit Bezug auf Kündigung.

## Quellen (Stand 05/2026)

- §§ 125, 126, 126a, 126b, 130, 314, 580a, 621, 622, 305b BGB.
- § 119 InsO (Beschränkung von Lösungsklauseln).
- BGH-Rechtsprechung zu doppelten Schriftformklauseln und zu Lösungsklauseln in der Insolvenz ist vom Nutzer fundstellengenau zu verifizieren.
- Zitierweise: `references/zitierweise.md`.
