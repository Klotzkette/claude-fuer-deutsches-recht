---
name: patentverletzung-claim-patr2
description: "Patentverletzung Claim Patr2: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Patentverletzung Claim Patr2

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Patentverletzung Claim Patr2** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patentverletzung-claim-chart` | Erstellt Claim Charts für Patentverletzung oder Nichtverletzung: Anspruchsmerkmale, Produkt-/Verfahrensbelege, Fundstellen, Beweisqualität, Lücken, Äquivalenz und Ergebnisampel. |
| `patr2-arbeitnehmererfindung-leitfaden` | Leitfaden Arbeitnehmererfindergesetz ArbnErfG: Meldepflicht, Inanspruchnahme, Verguetung, Schiedsstelle. Pruefraster fuer Arbeitgeber und Erfinder. |
| `patr2-patentverletzungsklage-spezial` | Spezialfall Patentverletzungsklage: aequivalente Verletzung, Unterlassung, Auskunft, Schadensersatz, Anspruchsberechnung Lizenzanalogie. Pruefraster fuer Klaeger und Beklagter. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Patentverletzung Claim Patr2**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `patentverletzung-claim-chart`

**Fokus:** Erstellt Claim Charts für Patentverletzung oder Nichtverletzung: Anspruchsmerkmale, Produkt-/Verfahrensbelege, Fundstellen, Beweisqualität, Lücken, Äquivalenz und Ergebnisampel.

# Claim Chart

## Input

- geltender Patentanspruch.
- Produktdaten, Fotos, Handbuch, CAD, Stückliste, Prüfbericht, Quellcode, Prozessbeschreibung.
- Registerstand und Territory.
- Ziel: Angriff, Verteidigung, FTO oder Vergleich.

## Tabelle

| Merkmal | Anspruchswortlaut | Produkt-/Verfahrensbefund | Beleg | Bewertung |
| --- | --- | --- | --- | --- |

Bewertung: erfüllt, nicht erfüllt, unklar, nur äquivalent denkbar, Beleg fehlt.

## Zusatzprüfungen

- Anspruchsauslegung: Begriffe aus Beschreibung/Figuren verstehen.
- Äquivalenz: gleiche Wirkung, Auffindbarkeit, Gleichwertigkeit; Gegenargumente.
- Beweisqualität: Mandantenangabe, Foto, Test, reverse engineering, Zeuge, Sachverständiger.
- Geheimhaltungs-/GeschG-Risiko bei technischen Unterlagen beachten.

## Output

- vollständiger Claim Chart.
- Lückenliste.
- Beweisanforderungen.
- Kurzfazit für Mandant oder Schriftsatz.

## Auslegungs- und Äquivalenz-Pflichtkern

- **§ 14 PatG / Art. 69 EPÜ und Auslegungsprotokoll:** Schutzbereich bestimmt sich nach den Ansprüchen; Beschreibung und Zeichnungen zur Auslegung; Mittelweg zwischen Wortsinn und Inhaltsidee.
- **Wortsinngemäße Verletzung:** Jedes Merkmal muss vollständig im angegriffenen Produkt/Verfahren erfüllt sein. Lückenfreiheit zwingend; einzelnes fehlendes Merkmal verhindert Wortsinn-Verletzung.
- **Äquivalenz (BGH "Schneidmesser" GRUR 2002, 511 / BGH X ZR 168/00):** Drei Voraussetzungen kumulativ:
 1. **Gleiche Wirkung** des Austauschmittels.
 2. **Auffindbarkeit** für den Fachmann mit dem Anspruch als Vorbild.
 3. **Gleichwertigkeit aus dem Anspruch** — Auswahlpflicht.
- **Mittelbare Verletzung § 10 PatG:** Lieferung wesentlicher Erfindungsmittel; sowohl objektives Element (Bezug auf wesentliches Mittel) als auch subjektives Element (Wissen/Erkennbarkeit).
- **Einwendungen:** Vorbenutzungsrecht § 12 PatG, Erschöpfung § 9 S. 2 PatG, Lizenz, Versuchsprivileg § 11 Nr. 2 PatG, Bolar-Klausel.
- **Beweisqualität:** Mandantenangabe < Foto/Video < Demonstration vor Notar/Sachverständigen < Marktproduktprüfung im Labor < unabhängiger Sachverständiger.
- **Geheimnisschutz:** Bei Reverse Engineering § 23 GeschGehG beachten; In-camera-Verfahren UPC oder §§ 16-20 GeschGehG.
- Falle: Claim Chart ohne Anspruchsversion und Stand-Verifikation (DPMA/EPA-Register-Abrufdatum) — bei Einspruch/Beschränkung kann sich der maßgebliche Anspruchstext ändern.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `patr2-arbeitnehmererfindung-leitfaden`

**Fokus:** Leitfaden Arbeitnehmererfindergesetz ArbnErfG: Meldepflicht, Inanspruchnahme, Verguetung, Schiedsstelle. Pruefraster fuer Arbeitgeber und Erfinder.

# PatR2: Arbeitnehmererfindung

## Spezialwissen: PatR2: Arbeitnehmererfindung
- **Spezialgegenstand:** PatR2: Arbeitnehmererfindung / patr2 arbeitnehmererfindung leitfaden. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ArbnErfG.
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

## 3. `patr2-patentverletzungsklage-spezial`

**Fokus:** Spezialfall Patentverletzungsklage: aequivalente Verletzung, Unterlassung, Auskunft, Schadensersatz, Anspruchsberechnung Lizenzanalogie. Pruefraster fuer Klaeger und Beklagter.

# PatR2: Patentverletzungsklage

## Spezialwissen: PatR2: Patentverletzungsklage
- **Spezialgegenstand:** PatR2: Patentverletzungsklage / patr2 patentverletzungsklage spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
