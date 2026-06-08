---
name: verwr-folgenbeseitigung-planfeststellung
description: "Verwr Folgenbeseitigung Planfeststellung im Plugin Fachanwalt Verwaltungsrecht: prüft konkret Spezialfall Folgenbeseitigungsanspruch, Spezialfall Planfeststellung Grossvorhaben, Leitfaden vorläufiger Rechtsschutz VwGO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Verwr Folgenbeseitigung Planfeststellung

## Arbeitsbereich

**Verwr Folgenbeseitigung Planfeststellung** ordnet den Fall über die tragenden Prüfungslinien: Spezialfall Folgenbeseitigungsanspruch, Spezialfall Planfeststellung Grossvorhaben, Leitfaden vorläufiger Rechtsschutz VwGO. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `verwr-folgenbeseitigung-spezial` | Spezialfall Folgenbeseitigungsanspruch: Grundlage Art. 20 Abs. 3 GG, Voraussetzungen rechtswidriger Eingriff, fortdauernde Beeintraechtigung, Wiederherstellungsmoeglichkeit. Pruefraster für Klage. |
| `verwr-planfeststellung-grossvorhaben-spezial` | Spezialfall Planfeststellung Grossvorhaben: §§ 72 ff. VwVfG, öffentliche Auslegung, Einwendungen, Aboerterungstermin, Planfeststellungsbeschluss. Pruefraster für Einwender. |
| `verwr-vorläufiger-rechtsschutz-leitfaden` | Leitfaden vorläufiger Rechtsschutz VwGO: § 80 Abs. 5 Antrag, § 123 einstweilige Anordnung. Pruefraster Eilbeduerftigkeit und Anordnungsanspruch. Mustertext Eilantrag. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `verwr-folgenbeseitigung-spezial`

**Fokus:** Spezialfall Folgenbeseitigungsanspruch: Grundlage Art. 20 Abs. 3 GG, Voraussetzungen rechtswidriger Eingriff, fortdauernde Beeintraechtigung, Wiederherstellungsmoeglichkeit. Pruefraster für Klage.

### VerwR: Folgenbeseitigung

## Spezialwissen: VerwR: Folgenbeseitigung
- **Normen-/Quellenanker:** Art. 20, GG, BGH.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

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
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `verwr-planfeststellung-grossvorhaben-spezial`

**Fokus:** Spezialfall Planfeststellung Grossvorhaben: §§ 72 ff. VwVfG, öffentliche Auslegung, Einwendungen, Aboerterungstermin, Planfeststellungsbeschluss. Pruefraster für Einwender.

### VerwR: Planfeststellung

## Spezialwissen: VerwR: Planfeststellung
- **Normen-/Quellenanker:** VwVfG, BGH, BVerfG.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

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
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `verwr-vorläufiger-rechtsschutz-leitfaden`

**Fokus:** Leitfaden vorläufiger Rechtsschutz VwGO: § 80 Abs. 5 Antrag, § 123 einstweilige Anordnung. Pruefraster Eilbeduerftigkeit und Anordnungsanspruch. Mustertext Eilantrag.

### VerwR: Vorlaeufiger Rechtsschutz

## Aufgabe
Leitfaden vorläufiger Rechtsschutz VwGO: § 80 V VwGO (Anfechtungssituationen mit aufschiebender Wirkung), § 80a VwGO (Drittwiderspruch), § 123 VwGO (einstweilige Anordnung in allen anderen Faellen). Pruefraster Eilbeduerftigkeit, Anordnungsanspruch/Anordnungsgrund. Verhaeltnis zu Art. 19 IV GG.

## Einstieg
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

### Variante 1: § 80 V VwGO (aufschiebende Wirkung)

- **Statthaftigkeit:** Anfechtungssituation, in der die aufschiebende Wirkung von Widerspruch/Klage entfallen ist (§ 80 II 1 Nr. 1-4 VwGO: Abgaben/Kosten, Polizei-/Ordnungsbehoerden, gesetzlich angeordnet, sofortige Vollziehung nach § 80 II 1 Nr. 4 VwGO).
- **Antrag:** Anordnung (Nr. 1-3) bzw. Wiederherstellung (Nr. 4) der aufschiebenden Wirkung.
- **Antragsbefugnis** § 42 II VwGO analog.
- **Vorheriger Behördenantrag** § 80 VI VwGO bei Abgaben.
- **Begruendetheit:** Interessenabwaegung — Aussetzungsinteresse Antragsteller vs. Vollziehungsinteresse Behörde; Hauptsacheprognose als wichtigstes Kriterium. Bei offensichtlicher Rechtswidrigkeit des VA Aussetzung; bei offensichtlicher Rechtmaessigkeit Ablehnung.
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
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
