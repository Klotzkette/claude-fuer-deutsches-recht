---
name: memorandums-ersteller-mandantenkommunikation-redteam
description: "Mandantenkommunikation Redteam: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenkommunikation Redteam

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenkommunikation Redteam** im Plugin Memorandum-Ersteller. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin memorandums-ersteller: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin memorandums-ersteller: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `memo-fristen-sofortmassnahmen` | Fristen und Sofortmassnahmen vor dem juristischen Inhalt: ein Memo beginnt mit 'Frist zuerst', wenn sich aus dem Sachverhalt erkennbare Termine ergeben (z. B. Klagefrist Kuendigungsschutzgesetz, Einspruch Strafbefehl). Output: Frist-Box am Anfang. |

## Arbeitsweg

Im Plugin Memorandum-Ersteller gilt für **Mandantenkommunikation Redteam**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin memorandums-ersteller: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieser Prüffeld übersetzt die rechtliche Bewertung des Memos in eine knappe, entscheidungsorientierte Nachricht an den Mandanten (Geschäftsführung, Vorstand, Inhouse-Counsel oder externe Stakeholder).

## Memo-Cover für Mandant
- **Adressat-spezifisch:** Geschäftsführung -- knapp, Risiko/Empfehlung; Vorstand/Aufsichtsrat -- mit Governance-Bezug; Investor -- mit Auswirkung auf Deal; Behörde -- ohne werbendes Element.
- **Standard-Aufbau:**
 1. Anliegen in einem Satz.
 2. Kurzantwort (Ja/Nein/Bedingt) -- nicht mehr als zwei Sätze.
 3. Empfehlung mit Begründung in 3-5 Sätzen.
 4. Risiken / Restunsicherheiten ausdrücklich (rechtlich, faktisch, prozessual, reputativ).
 5. Nächste Schritte mit Verantwortlichkeit und Frist.
 6. Hinweis auf vollständiges Memo (Anlage).

## Sprachregeln
- Aktive Verben statt Nominalstil ("Sie sollten X tun" statt "Eine Tätigung von X wäre angezeigt").
- Quantifizieren wo möglich (Umsatzschwelle, Zeitraum, Wahrscheinlichkeit).
- Empfehlung erkennbar als solche, nicht in Konjunktiv versteckt.
- Vertraulichkeitsvermerk im Footer ("Privileged & confidential / attorney-client privilege"; Reichweite des EU-/US-Privilegs beachten).

## Anti-Muster
- "Im Ergebnis lässt sich festhalten, dass die Rechtslage zumindest nicht eindeutig in eine bestimmte Richtung tendiert." -- Mandant lernt nichts.
- Risiken am Ende verstecken statt prominent benennen.

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

**Fokus:** Red-Team Qualitygate im Plugin memorandums-ersteller: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieser Prüffeld prüft das fertige Memo vor Versand auf typische Schwächen: Halluzinationen, fehlende Gegenargumente, übersehene Sondernormen, schwache Subsumtion, unklare Empfehlung, fehlender Vertraulichkeitsvermerk.

## Red-Team-Punkte Memo
- **Halluzinations-Scan:** Jede zitierte Entscheidung mit echtem Az.? "Ständige Rspr." mit konkretem Az. belegt? Kommentar-/Aufsatzfundstellen mit Quelle?
- **Anspruchsgrundlagen vollständig?** Reihenfolge Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung (vgl. CLAUDE.md / `references/methodik-buergerliches-recht.md`).
- **Subsumtion sauber?** Obersatz - Definition - Tatsachen - Schluss; keine Sprung-Subsumtion; keine Zirkelschlüsse.
- **Gegenargumente / Mindermeinung gewürdigt?** Wenn entscheidungserheblich.
- **Sondernormen geprüft?** AGB-Recht (§§ 305 ff. BGB), Verbraucherschutz (§§ 13, 14, 312 ff. BGB), DSGVO, Sektorengesetze (KWG, ZAG, GWG, etc.).
- **Auslegung erklärt?** Vier Auslegungsmethoden zzgl. verfassungs-/unionsrechtskonform.
- **Empfehlung klar?** Eine Linie, mit Begründung; Alternativen mit Trade-off.
- **Risikoanalyse?** Restrisiken benannt; "Cone of uncertainty".
- **Form:** Kurzantwort am Anfang, Quellenverzeichnis am Ende, Privileged & confidential.
- **Sprache:** Gutachtenstil bei Memo-Hauptteil; Cover-Letter mandantengerecht.
- Falle: Memo nur aus Mandantenperspektive -- bedenke immer auch die Sicht der Gegenseite / der Behörde / des Gerichts.

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

## 3. `memo-fristen-sofortmassnahmen`

**Fokus:** Fristen und Sofortmassnahmen vor dem juristischen Inhalt: ein Memo beginnt mit 'Frist zuerst', wenn sich aus dem Sachverhalt erkennbare Termine ergeben (z. B. Klagefrist Kuendigungsschutzgesetz, Einspruch Strafbefehl). Output: Frist-Box am Anfang.

# Memo: Fristen und Sofortmassnahmen

## Spezialwissen: Memo: Fristen und Sofortmassnahmen
- **Spezialgegenstand:** Memo: Fristen und Sofortmassnahmen / memo fristen sofortmassnahmen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
