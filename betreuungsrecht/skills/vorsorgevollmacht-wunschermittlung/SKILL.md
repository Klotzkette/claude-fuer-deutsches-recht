---
name: vorsorgevollmacht-wunschermittlung
description: "Vorsorgevollmacht Wunschermittlung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vorsorgevollmacht Wunschermittlung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vorsorgevollmacht Wunschermittlung** im Plugin Betreuungsrecht (§§ 1814 ff. BGB). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vorsorgevollmacht-pruefen` | Vorsorgevollmacht pruefen: § 1820 BGB, Reichweite, Form (Schriftform fuer Bank/Personalsorge), Beglaubigung, Hinterlegung im Zentralen Vorsorgeregister. Vorrang vor Betreuung. Pruefraster fuer den Vergleich Vollmacht/Betreuungsbedarf. |
| `wunschermittlung-unterstuetzte-entscheidung` | Wunschermittlung und unterstützte Entscheidung nach § 1821 BGB: hilft Betreuern, Wünsche, frühere Präferenzen, mutmaßlichen Willen, Kommunikationshilfen und Schutzgrenzen sauber zu dokumentieren, ohne die betreute Person zu entmündigen. |
| `zwangsbehandlung-1832-bgb` | Zwangsbehandlung § 1832 BGB: Voraussetzungen, Genehmigung Betreuungsgericht, Verfahren § 312 FamFG. BVerfG-Linien zu Patientenautonomie (BVerfG 2 BvR 882/09). Output: Antragsentwurf an Gericht. |

## Arbeitsweg

Im Plugin Betreuungsrecht (§§ 1814 ff. BGB) gilt für **Vorsorgevollmacht Wunschermittlung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vorsorgevollmacht-pruefen`

**Fokus:** Vorsorgevollmacht pruefen: § 1820 BGB, Reichweite, Form (Schriftform fuer Bank/Personalsorge), Beglaubigung, Hinterlegung im Zentralen Vorsorgeregister. Vorrang vor Betreuung. Pruefraster fuer den Vergleich Vollmacht/Betreuungsbedarf.

# Vorsorgevollmacht pruefen

## Spezialwissen: Vorsorgevollmacht pruefen
- **Spezialgegenstand:** Vorsorgevollmacht pruefen / vorsorgevollmacht pruefen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
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

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `wunschermittlung-unterstuetzte-entscheidung`

**Fokus:** Wunschermittlung und unterstützte Entscheidung nach § 1821 BGB: hilft Betreuern, Wünsche, frühere Präferenzen, mutmaßlichen Willen, Kommunikationshilfen und Schutzgrenzen sauber zu dokumentieren, ohne die betreute Person zu entmündigen.

# Wunschermittlung und unterstützte Entscheidung

## Zweck

Betreuung beginnt nicht mit “Was ist vernünftig?”, sondern mit “Was will die betreute Person?”. Dieser Skill hilft, Wünsche und Präferenzen praktisch zu erfassen und gerichtstauglich zu dokumentieren.

## Prüfpfad

1. **Aktueller Wunsch:** Was sagt oder zeigt die betreute Person jetzt?
2. **Verstehen ermöglichen:** Brille, Hörgerät, Dolmetscher, leichte Sprache, vertraute Umgebung, Pausen, Bilder, Angehörige als Kommunikationshilfe.
3. **Frühere Wünsche:** Patientenverfügung, Vorsorgevollmacht, Betreuungsverfügung, Briefe, Gewohnheiten, Lebensstil.
4. **Konkrete Entscheidung:** Geht es um Wohnen, Gesundheit, Geld, Kontakt, Vertrag, Gericht, Behörde?
5. **Risiko:** Droht erhebliche Selbstschädigung oder Fremdgefährdung?
6. **Milderes Mittel:** Kann der Wunsch sicherer umgesetzt werden?
7. **Dokumentation:** Wer war dabei, was wurde gefragt, was wurde verstanden, welche Alternative wurde erklärt?

## Wunschvermerk

```text
Wunsch-/Entscheidungsvermerk

Datum/Uhrzeit:
Ort:
Anwesende:
Thema:

Wunsch der betreuten Person:

Wie wurde der Wunsch ermittelt?

Welche Informationen/Alternativen wurden erklärt?

Risiken:

Entscheidung des Betreuers:

Warum entspricht die Entscheidung dem Wunsch oder warum ausnahmsweise nicht?
```

## Red Flags

- Entscheidung wird nur mit “das ist besser für sie” begründet.
- Angehörige sprechen über die betreute Person hinweg.
- Heim/Bank/Behörde drängt auf schnelle Unterschrift.
- Frühere klare Wünsche werden ignoriert.
- Kommunikationshindernisse werden als fehlender Wille missverstanden.

## Normanker

- § 1821 BGB: Unterstützung, Wunschbefolgung, mutmaßlicher Wille.
- § 1814 BGB: Betreuung nur erforderlich, wenn andere Hilfen nicht ausreichen.
- UN-BRK Art. 12 als Leitbild unterstützter Rechts- und Handlungsfähigkeit; konkrete Umsetzung erfolgt über deutsches Betreuungsrecht.

## 3. `zwangsbehandlung-1832-bgb`

**Fokus:** Zwangsbehandlung § 1832 BGB: Voraussetzungen, Genehmigung Betreuungsgericht, Verfahren § 312 FamFG. BVerfG-Linien zu Patientenautonomie (BVerfG 2 BvR 882/09). Output: Antragsentwurf an Gericht.

# Zwangsbehandlung § 1832 BGB

## Spezialwissen: Zwangsbehandlung § 1832 BGB
- **Spezialgegenstand:** Zwangsbehandlung § 1832 BGB / zwangsbehandlung 1832 bgb. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, FamFG, BVerfG.
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

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

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

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
