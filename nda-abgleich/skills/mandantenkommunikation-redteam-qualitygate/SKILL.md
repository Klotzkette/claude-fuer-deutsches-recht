---
name: mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation, Redteam Qualitygate, Nda Anwendbares Recht Gerichtsstand: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Mandantenkommunikation, Redteam Qualitygate, Nda Anwendbares Recht Gerichtsstand

## Arbeitsbereich

Dieser Skill bündelt **Mandantenkommunikation, Redteam Qualitygate, Nda Anwendbares Recht Gerichtsstand** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin nda-abgleich: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin nda-abgleich: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `nda-anwendbares-recht-gerichtsstand` | Anwendbares Recht und Gerichtsstand bei NDA: Empfehlung deutsches Recht + LG Sitz des Discloser; Schiedsklausel (DIS Regeln) ab hoeherer Bedeutung. Pruefraster: internationale NDAs vs. nationale, Verbraucherbeteiligung. |

## Arbeitsweg

Für **Mandantenkommunikation, Redteam Qualitygate, Nda Anwendbares Recht Gerichtsstand** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `nda-abgleich` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin nda-abgleich: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin nda-abgleich: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin nda-abgleich: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin nda-abgleich: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `nda-anwendbares-recht-gerichtsstand`

**Fokus:** Anwendbares Recht und Gerichtsstand bei NDA: Empfehlung deutsches Recht + LG Sitz des Discloser; Schiedsklausel (DIS Regeln) ab hoeherer Bedeutung. Pruefraster: internationale NDAs vs. nationale, Verbraucherbeteiligung.

# NDA: Recht und Gerichtsstand

## Spezialwissen: NDA: Recht und Gerichtsstand
- **Spezialgegenstand:** NDA: Recht und Gerichtsstand / nda anwendbares recht gerichtsstand. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** NDA, LG, DIS.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Fachpruefraster Anwendbares Recht und Gerichtsstand

### Rechtswahl (Rom I-VO bei Schuldvertraegen, Rom II-VO bei aussevertraglichen Anspruechen)

- **Rom I-VO Art. 3:** Vertragsparteien koennen frei das anwendbare Recht waehlen. Bei NDA in B2B-Konstellation: deutsches Recht ist Marktstandard.
- **Rom I-VO Art. 6 (Verbrauchervertraege):** Bei NDA mit Verbraucher dessen Aufenthaltsrecht zwingend; Schutz nicht entziehbar.
- **Rom I-VO Art. 9 (Eingriffsnormen):** Bestimmte zwingende Vorschriften des Forum-Staates greifen unabhaengig von der Rechtswahl (z.B. Kartellrecht).
- **GeschGehG:** Anwendbarkeit haengt vom anwendbaren Recht ab; Schutzwirkung ist europarechtlich harmonisiert (RL 2016/943), aber konkrete Anspruchsdurchsetzung folgt nationalem Recht.

### Gerichtsstand (Brüssel Ia-VO 1215/2012)

- **Art. 25 Brüssel Ia-VO:** Gerichtsstandsvereinbarung im B2B grundsaetzlich frei; Schriftform oder schriftform-gleichwertige Form erforderlich.
- **Art. 17 ff. Brüssel Ia-VO:** Bei Verbrauchervertraegen: nur Klage am Wohnsitz des Verbrauchers; Gerichtsstandsklauseln zugunsten des Unternehmers regelmaessig unwirksam.
- **Ausschliesslicher vs. nicht-ausschliesslicher Gerichtsstand:** Marktstandard ist ausschliesslich. Bei Asymmetrie (Klagende Partei waehlt, Beklagte muss am eigenen Sitz klagen) Vorsicht: kann nach Rechtsprechung problematisch sein.
- **Commercial Courts:** Seit Inkrafttreten des Gesetzes zur Staerkung der Gerichte in Wirtschaftsstreitigkeiten gibt es spezialisierte Commercial Courts an deutschen OLG (z.B. Hamburg, Stuttgart, Frankfurt) mit Englisch als Verfahrenssprache. Fuer hochwertige internationale Vertraege empfehlenswert.

### Einstweiliger Rechtsschutz

- **§ 935, § 940 ZPO:** Einstweilige Verfuegung ist haeufig wichtigste Durchsetzungsform bei NDA-Verletzung (Unterlassungsanspruch).
- **Eilbeduerftigkeit:** Bei NDA-Verletzung regelmaessig binnen 4-6 Wochen nach Kenntnis Antrag stellen, sonst Dringlichkeitsvermutung gefaehrdet (OLG-Rechtsprechung uneinheitlich).
- **Gerichtsstandsklausel:** Schliesst grundsaetzlich nicht den allgemeinen Gerichtsstand fuer einstweilige Massnahmen aus (Art. 35 Brüssel Ia-VO erlaubt Massnahmen am Ort der Vollziehung).

### Schiedsklausel (ICC, DIS, LCIA)

- **Pro:** Vertraulichkeit des Verfahrens (Schiedsgerichtsverfahren passen besonders zu NDA), internationale Anerkennung (New Yorker Uebereinkommen 1958), Expertise.
- **Contra:** Hoehere Kosten, Verzoegerung bei einstweiligem Rechtsschutz (sofern nicht explizit zugelassen).
- **Marktstandard:** DIS (Deutsche Institution fuer Schiedsgerichtsbarkeit) Schiedsregeln 2018; Sitz Frankfurt am Main; Verfahrenssprache Deutsch oder Englisch.

### Praxis-Empfehlung Standardklausel

- **Rein nationale Beziehung B2B:** deutsches Recht, ausschliesslicher Gerichtsstand am Sitz der offenlegenden Partei.
- **Internationale Beziehung B2B:** deutsches Recht, ICC- oder DIS-Schiedsgerichtsbarkeit am neutralen Sitz, einstweiliger Rechtsschutz vor staatlichen Gerichten zulaessig.

### Mustertext

> Auf diesen Vertrag findet ausschliesslich deutsches Recht Anwendung unter Ausschluss des UN-Kaufrechts (CISG) und der Kollisionsnormen. Ausschliesslicher Gerichtsstand fuer alle Streitigkeiten aus oder im Zusammenhang mit diesem Vertrag ist [Sitz der offenlegenden Partei]. Jede Partei ist berechtigt, einstweilige Massnahmen auch bei einem nach den allgemeinen Vorschriften zustaendigen Gericht zu beantragen.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `nda-abgleich`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
