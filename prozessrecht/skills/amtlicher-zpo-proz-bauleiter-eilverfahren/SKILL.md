---
name: amtlicher-zpo-proz-bauleiter-eilverfahren
description: "Amtlicher ZPO Proz Bauleiter Eilverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Amtlicher ZPO Proz Bauleiter Eilverfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Amtlicher ZPO Proz Bauleiter Eilverfahren** im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `amtlicher-zpo-verfahrenscheck` | Amtlicher ZPO-Verfahrenscheck: ordnet Zuständigkeit, Schriftsatzform, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung anhand der aktuellen ZPO-Fassung. |
| `proz-zustaendigkeit-bauleiter` | Bauleiter Zustaendigkeit ZPO: sachlich, oertlich, funktionell, internationale Zustaendigkeit. Pruefraster typische Klagearten. |
| `spezial-eilverfahren-risikoampel-und-gegenargumente` | Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin prozessrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Prozessrecht (ZPO/VwGO/StPO/SGG) gilt für **Amtlicher ZPO Proz Bauleiter Eilverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `amtlicher-zpo-verfahrenscheck`

**Fokus:** Amtlicher ZPO-Verfahrenscheck: ordnet Zuständigkeit, Schriftsatzform, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung anhand der aktuellen ZPO-Fassung.

# Amtlicher ZPO-Verfahrenscheck

## Zweck

Dieser Skill ist der prozessuale Faktenanker. Er soll bei jedem ernsthaften ZPO-Output verhindern, dass alte Fristen-, Zustellungs-, Form- oder Vollstreckungsregeln aus dem Bauch verwendet werden.

## Schnellroute

1. Verfahrensphase bestimmen: vorgerichtlich, Klage, Eilrechtsschutz, Beweis, Mahnverfahren, Urteil, Rechtsmittel, Vollstreckung.
2. Zuständigkeit und Vertretung prüfen.
3. Form, Einreichung, Zustellung und Fristen prüfen.
4. Beweis- oder Darlegungslastpfad bestimmen.
5. Output bauen: Klageschrift, Antrag, Fristenvermerk, Beweisantritt, Mahnantrag, Vollstreckungsauftrag.

## Normgruppen

| Phase | Normen |
| --- | --- |
| Wert/Zuständigkeit | §§ 1-11, 12-40 ZPO plus GVG |
| Parteien/Vertretung | §§ 50-90 ZPO |
| Kosten/PKH | §§ 91-127 ZPO |
| Schriftsatz/elektronisch | §§ 129-130e ZPO |
| Vortrag/Gericht | §§ 136-150 ZPO |
| Zustellung | §§ 166-190 ZPO |
| Termine/Fristen/Wiedereinsetzung | §§ 214-238 ZPO; § 222 ZPO i. V. m. §§ 186-193 BGB |
| Klage/Rechtshängigkeit | §§ 253-270 ZPO |
| Vorbereitung/Güte/Termin | §§ 272-285 ZPO |
| Beweis | §§ 286-484 ZPO |
| Selbständiges Beweisverfahren | §§ 485-494a ZPO |
| Mahnverfahren | §§ 688-703d ZPO |
| Vollstreckung | §§ 704 ff. ZPO |
| Forderungspfändung | §§ 828 ff. ZPO |
| Handlung/Unterlassung | §§ 887-890 ZPO |
| Arrest/einstweilige Verfügung | §§ 916-945 ZPO |

## Output

Erzeuge eine Verfahrensmatrix:

| Punkt | Norm | Tatsache | Beleg | Risiko | Handlung |
| --- | --- | --- | --- | --- | --- |

Dann einen unmittelbar verwendbaren Baustein: Antrag, Fristenvermerk, Schriftsatzabschnitt, Mandantenhinweis oder To-do-Liste.

## Referenz

Nutze `references/amtlicher-zpo-normkern.md`. Rechtsprechung nur nach gesondertem Live-Check mit Gericht, Datum, Aktenzeichen und freier/amtlicher Quelle nennen.

## 2. `proz-zustaendigkeit-bauleiter`

**Fokus:** Bauleiter Zustaendigkeit ZPO: sachlich, oertlich, funktionell, internationale Zustaendigkeit. Pruefraster typische Klagearten.

# Proz: Zustaendigkeit Bauleiter

## Spezialwissen: Proz: Zustaendigkeit Bauleiter
- **Spezialgegenstand:** Proz: Zustaendigkeit Bauleiter / proz zustaendigkeit bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, BGH, BVerfG.
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

## 3. `spezial-eilverfahren-risikoampel-und-gegenargumente`

**Fokus:** Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin prozessrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Eilverfahren: Risikoampel, Gegenargumente und Verteidigungslinien / eilverfahren risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Eilverfahren** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
