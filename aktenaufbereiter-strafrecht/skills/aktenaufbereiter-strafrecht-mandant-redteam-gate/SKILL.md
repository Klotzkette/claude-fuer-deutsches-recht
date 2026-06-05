---
name: aktenaufbereiter-strafrecht-mandant-redteam-gate
description: "Mandant Redteam Gate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandant Redteam Gate

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandant Redteam Gate** im Plugin Strafrechtliche Aktenarbeit. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin aktenaufbereiter-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin aktenaufbereiter-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `chronologie-strafverfahren` | Chronologie aller Verfahrensschritte: Tatzeitpunkt, Anzeige, Vernehmungen, Durchsuchungen, Festnahme, U-Haft-Befehle, Anklage, Hauptverhandlungstermine, Urteile, Rechtsmittel. Datum, Zeit, Behoerde/Gericht, Art, Beleg in der Akte (Aktenblatt). Zeigt Luecken und unplausible Reihenfolgen. |

## Arbeitsweg

Im Plugin Strafrechtliche Aktenarbeit gilt für **Mandant Redteam Gate**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin aktenaufbereiter-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin aktenaufbereiter-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Strafakte-Mandantenkommunikation Bausteine
- **Aktenstand-Brief an Mandant** strukturiert:
 - Stand der Ermittlungen (Anklage erhoben / Eroeffnungsbeschluss / Hauptverhandlung anberaumt / Urteil verkuendet).
 - Tatvorwurf in Kurzfassung.
 - Beweislage (Indizien fuer / gegen Mandant; staerkste Belastungsbeweise und Entlastungsindizien).
 - Strafmasserwartung (Bandbreite, nicht ein Wert).
 - Entscheidungsoffene Punkte (Verstaendigung, Gestaendnis, Beweisantraege).
- **Pflicht-Hinweise:**
 - **Mandantengeheimnis** § 43a Abs. 2 BRAO, § 203 StGB; § 53 I Nr. 2 StPO Verteidiger-Zeugnisverweigerung.
 - **Schweigerecht** Mandant § 136 I 2 StPO; nie ohne Vorbereitung gegenueber Polizei aussagen.
 - **Aussagebegrenzungen Familie** § 52 StPO Zeugnisverweigerung Angehoeriger; § 55 StPO bei drohender Selbstbelastung.
- **Strategie-Freigabe** schriftlich:
 - Akteneinsicht-Anmeldung.
 - Stellungnahme zur Anklage.
 - Beweisantraege.
 - Verstaendigung § 257c StPO.
 - Gestaendnisbereitschaft.
 - Rechtsmittelverzicht / -einlegung / -ruecknahme.
- **Kostenhinweis RVG:** Grundgebuehr VV 4100; Verfahrensgebuehr VV 4106 ff. je nach Verfahrensstufe; Terminsgebuehr VV 4108 ff.; Pflichtverteidigergebuehren als Verfahrenskosten zu tragen vom Mandant bei Verurteilung.
- **Notfall-Kontakt** bei U-Haft / Polizeivernehmung Mandant: 24/7-Erreichbarkeit; Vollmacht inklusive § 138 StPO.
- **Inhaftiert-Korrespondenz:** Verteidigerpost unueberwacht § 148 StPO (Ausnahme: §§ 129a, 129b StGB-Verdacht).

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin aktenaufbereiter-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin aktenaufbereiter-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Strafakte-Red-Team-Checks
- **Halluzinations-Check:** Keine erfundenen BGH-/BVerfG-Az; Fundstellen mit Datum, Gericht und Az pruefen oder als "staendige Rspr."/"BGH-Linie" markieren.
- **Frist-Re-Check:** Berufung § 314 StPO (1 Woche), Revision §§ 341, 345 StPO (1 Woche / 1 Monat), Strafbefehl-Einspruch § 410 StPO (2 Wochen), Wiedereinsetzung § 44 StPO (1 Woche ab Wegfall); Postzustellungsdatum verifizieren.
- **Zustaendigkeits-Re-Check:** GVG - Strafrichter § 25 (bis 2 Jahre Freiheitsstrafe), Schoeffengericht § 28 (bis 4 Jahre), Schwurgericht § 74 GVG (Toetungsdelikte), grosse Strafkammer § 76 GVG (ueber 4 Jahre, schwere Wirtschaftskriminalitaet). Verfahrenshandlung Falschadressiert?
- **Belehrungs-Check** § 136 StPO (Beschuldigtenrechte), § 52 StPO (Zeugnisverweigerung Angehoeriger), § 55 StPO (Auskunftsverweigerung wegen Selbstbelastung): in der Akte protokolliert?
- **Beweisverwertungs-Check:** § 136a StPO (verbotene Vernehmungsmethoden), § 252 StPO (Aussageverweigerung Hauptverhandlung), § 261 StPO Beweiswuerdigungslueckchen, Belehrungsfehler in Beschuldigtenvernehmung.
- **Ton-/Stil-Check:** keine wertende Vorverurteilung; klare Trennung Fakten / Bewertung; Mandantengeheimnis § 43a Abs. 2 BRAO, § 203 StGB.
- **Vollstaendigkeits-Check Anklageschrift § 200 StPO:** Beschuldigter, Tat (Zeit, Ort, gesetzliche Merkmale), Beweismittel, anzuwendende Strafvorschriften.

## 3. `chronologie-strafverfahren`

**Fokus:** Chronologie aller Verfahrensschritte: Tatzeitpunkt, Anzeige, Vernehmungen, Durchsuchungen, Festnahme, U-Haft-Befehle, Anklage, Hauptverhandlungstermine, Urteile, Rechtsmittel. Datum, Zeit, Behoerde/Gericht, Art, Beleg in der Akte (Aktenblatt). Zeigt Luecken und unplausible Reihenfolgen.

# Chronologie Strafverfahren

## Spezialwissen: Chronologie Strafverfahren
- **Spezialgegenstand:** Chronologie Strafverfahren / chronologie strafverfahren. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
