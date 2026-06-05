---
name: verwr-folgenbeseitigung-planfeststellung
description: "Verwr Folgenbeseitigung Planfeststellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verwr Folgenbeseitigung Planfeststellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verwr Folgenbeseitigung Planfeststellung** im Plugin Fachanwalt Verwaltungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verwr-folgenbeseitigung-spezial` | Spezialfall Folgenbeseitigungsanspruch: Grundlage Art. 20 Abs. 3 GG, Voraussetzungen rechtswidriger Eingriff, fortdauernde Beeintraechtigung, Wiederherstellungsmoeglichkeit. Pruefraster fuer Klage. |
| `verwr-planfeststellung-grossvorhaben-spezial` | Spezialfall Planfeststellung Grossvorhaben: §§ 72 ff. VwVfG, oeffentliche Auslegung, Einwendungen, Aboerterungstermin, Planfeststellungsbeschluss. Pruefraster fuer Einwender. |
| `verwr-vorlaeufiger-rechtsschutz-leitfaden` | Leitfaden vorlaeufiger Rechtsschutz VwGO: § 80 Abs. 5 Antrag, § 123 einstweilige Anordnung. Pruefraster Eilbeduerftigkeit und Anordnungsanspruch. Mustertext Eilantrag. |

## Arbeitsweg

Im Plugin Fachanwalt Verwaltungsrecht gilt für **Verwr Folgenbeseitigung Planfeststellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verwr-folgenbeseitigung-spezial`

**Fokus:** Spezialfall Folgenbeseitigungsanspruch: Grundlage Art. 20 Abs. 3 GG, Voraussetzungen rechtswidriger Eingriff, fortdauernde Beeintraechtigung, Wiederherstellungsmoeglichkeit. Pruefraster fuer Klage.

# VerwR: Folgenbeseitigung

## Spezialwissen: VerwR: Folgenbeseitigung
- **Spezialgegenstand:** VerwR: Folgenbeseitigung / verwr folgenbeseitigung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 20, GG, BGH.
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

## 2. `verwr-planfeststellung-grossvorhaben-spezial`

**Fokus:** Spezialfall Planfeststellung Grossvorhaben: §§ 72 ff. VwVfG, oeffentliche Auslegung, Einwendungen, Aboerterungstermin, Planfeststellungsbeschluss. Pruefraster fuer Einwender.

# VerwR: Planfeststellung

## Spezialwissen: VerwR: Planfeststellung
- **Spezialgegenstand:** VerwR: Planfeststellung / verwr planfeststellung grossvorhaben spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VwVfG, BGH, BVerfG.
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

## 3. `verwr-vorlaeufiger-rechtsschutz-leitfaden`

**Fokus:** Leitfaden vorlaeufiger Rechtsschutz VwGO: § 80 Abs. 5 Antrag, § 123 einstweilige Anordnung. Pruefraster Eilbeduerftigkeit und Anordnungsanspruch. Mustertext Eilantrag.

# VerwR: Vorlaeufiger Rechtsschutz

## Aufgabe
Leitfaden vorlaeufiger Rechtsschutz VwGO: § 80 V VwGO (Anfechtungssituationen mit aufschiebender Wirkung), § 80a VwGO (Drittwiderspruch), § 123 VwGO (einstweilige Anordnung in allen anderen Faellen). Pruefraster Eilbeduerftigkeit, Anordnungsanspruch/Anordnungsgrund. Verhaeltnis zu Art. 19 IV GG.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

### Variante 1: § 80 V VwGO (aufschiebende Wirkung)

- **Statthaftigkeit:** Anfechtungssituation, in der die aufschiebende Wirkung von Widerspruch/Klage entfallen ist (§ 80 II 1 Nr. 1-4 VwGO: Abgaben/Kosten, Polizei-/Ordnungsbehoerden, gesetzlich angeordnet, sofortige Vollziehung nach § 80 II 1 Nr. 4 VwGO).
- **Antrag:** Anordnung (Nr. 1-3) bzw. Wiederherstellung (Nr. 4) der aufschiebenden Wirkung.
- **Antragsbefugnis** § 42 II VwGO analog.
- **Vorheriger Behoerdenantrag** § 80 VI VwGO bei Abgaben.
- **Begruendetheit:** Interessenabwaegung — Aussetzungsinteresse Antragsteller vs. Vollziehungsinteresse Behoerde; Hauptsacheprognose als wichtigstes Kriterium. Bei offensichtlicher Rechtswidrigkeit des VA Aussetzung; bei offensichtlicher Rechtmaessigkeit Ablehnung.
- **Sofortige Vollziehung § 80 II 1 Nr. 4 VwGO** zusaetzlich Begruendungsanforderungen (§ 80 III VwGO).

### Variante 2: § 80a VwGO (Drittanfechtung)

- Begehren des Dritten: Anordnung der aufschiebenden Wirkung seines Widerspruchs gegen begunstigenden VA an Adressaten (z. B. Baugenehmigung des Nachbarn).
- Pruefung nach Massgabe drittschuetzender Normen.

### Variante 3: § 123 VwGO (einstweilige Anordnung)

- **Statthaftigkeit:** subsidiaer zu § 80 V VwGO; bei Verpflichtungs-, Leistungs-, Feststellungsbegehren, vorbeugenden Unterlassungsbegehren.
- **Anordnungsanspruch** — materieller Anspruch (§ 920 II ZPO analog), glaubhaft zu machen (§ 920 II ZPO, § 294 ZPO).
- **Anordnungsgrund** — Eilbeduerftigkeit, wesentliche Nachteile drohen.
- **Sicherungsanordnung** § 123 I 1 VwGO (Erhalt status quo) vs. **Regelungsanordnung** § 123 I 2 VwGO.
- **Vorwegnahme der Hauptsache** ausnahmsweise zulaessig bei drohenden irreversiblen Nachteilen und hoher Erfolgsaussicht in der Hauptsache.

## Praxisfallen

- **Fristen:** Eilantrag nicht fristgebunden, aber Hauptsachefrist (Widerspruch § 70 VwGO, Klage § 74 VwGO) muss separat gewahrt werden — Eilantrag schuetzt nicht vor Bestandskraft.
- **Begruendung der Sofortvollziehung** § 80 III VwGO formelhaft = Fehler, fuehrt regelmaessig zur Aussetzung.
- **Schutznormtheorie** § 42 II VwGO analog: nicht jeder Nachbarstoer hat Antragsbefugnis.
- **Abwaegung bei drohender Vollstreckung** (Abrissverfuegung, Abschiebung): Hauptsacheprognose und Gewichtung Folgen.

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
