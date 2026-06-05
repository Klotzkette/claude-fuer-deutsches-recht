---
name: forschungszulage-antragstellung-fz-koordinierung-zwei
description: "FZ Koordinierung Zwei: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# FZ Koordinierung Zwei

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **FZ Koordinierung Zwei** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fz-koordinierung-zwei-foerderwege` | Koordinierung Forschungszulage mit anderen Foerderwegen: keine Doppelfoerderung derselben Kosten, aber Kombination ueber Modulgrenze hinweg (ZIM, IGF, Horizon Europe, Landesfoerderung). Pruefraster fuer Kostentrennung, Buchhaltung, Bescheinigungslogik. Vermeidung von Anrechnungsrisiken. |
| `fz-kumulierung-beihilfen-agvo` | Kumulierung Forschungszulage mit anderen Förderungen und Beihilfen sauber prüfen: AGVO Art. 25, EU/EWR-Auftragsforschung, ZIM, BMBF-Programme, Landesprogramme, De-minimis-Nähe, Horizon, Doppelförderung, Nachweis- und Abzugslogik. Mit Kumulierungstabelle je Projekt und Höchstintensitäten je Kategorie. |
| `fz-personalkosten-und-stundennachweis` | Foerderfaehige Personalkosten der Forschungszulage: Bruttoarbeitslohn plus Arbeitgeberanteile, Stundenpauschale 70 Euro Eigenunternehmer, Auftragsforschung 60 Prozent (KMU 70 Prozent). Stundennachweissystem: tagesgenau, Aufgabenbezug, Plausibilitaet. Typische Pruefungsfeststellungen des Finanzamts und Abwehr. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **FZ Koordinierung Zwei**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fz-koordinierung-zwei-foerderwege`

**Fokus:** Koordinierung Forschungszulage mit anderen Foerderwegen: keine Doppelfoerderung derselben Kosten, aber Kombination ueber Modulgrenze hinweg (ZIM, IGF, Horizon Europe, Landesfoerderung). Pruefraster fuer Kostentrennung, Buchhaltung, Bescheinigungslogik. Vermeidung von Anrechnungsrisiken.

# FZ: Foerderkoordinierung

## Spezialwissen: FZ: Foerderkoordinierung
- **Spezialgegenstand:** FZ: Foerderkoordinierung / fz koordinierung zwei foerderwege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZIM, IGF, FZ.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `fz-kumulierung-beihilfen-agvo`

**Fokus:** Kumulierung Forschungszulage mit anderen Förderungen und Beihilfen sauber prüfen: AGVO Art. 25, EU/EWR-Auftragsforschung, ZIM, BMBF-Programme, Landesprogramme, De-minimis-Nähe, Horizon, Doppelförderung, Nachweis- und Abzugslogik. Mit Kumulierungstabelle je Projekt und Höchstintensitäten je Kategorie.

# Kumulierung und Beihilfen (AGVO)

## Worum geht es

Die Forschungszulage ist eine staatliche Beihilfe nach Art. 25 AGVO (Verordnung (EU) 651/2014 — vom Antragsteller mit konsolidierter Fassung zu prüfen). Sie kann grundsätzlich mit anderen Förderungen kumuliert werden, aber nur bis zu den AGVO-Höchstintensitäten je Vorhaben und Beihilfe-Kategorie. Dieser Skill liefert die Kumulierungslogik, die Höchstintensitäten und das Kumulierungsblatt je Projekt.

## Wann dieses Modul hilft

- Wenn der Mandant bereits ZIM, BMBF, Land oder Horizon-Förderung erhält.
- Vor Eingang des BSFZ-Antrags, um die Kumulierungslage zu klären.
- Bei der Finanzamt-Antragsvorbereitung (Anlage Kumulierungsblatt).
- Bei einer Außenprüfung, weil AGVO-Verstöße Rückforderungsrisiken auslösen.

## Sachrahmen — die AGVO-Höchstintensitäten

AGVO Art. 25 unterscheidet die Förderkategorien und legt für jede eine Beihilfehöchstintensität fest (in Prozent der beihilfefähigen Kosten). Die Werte sind vom Antragsteller mit der konsolidierten AGVO-Fassung zu verifizieren — typische Größenordnungen:

| Kategorie | Großunternehmen | Mittlere | Kleine |
| --- | --- | --- | --- |
| Grundlagenforschung | 100 Prozent | 100 Prozent | 100 Prozent |
| Industrielle Forschung | 50 Prozent | 60 Prozent | 70 Prozent |
| Industrielle Forschung mit Bonus (Konsortium / Veröffentlichung) | bis 65 Prozent | bis 75 Prozent | bis 80 Prozent |
| Experimentelle Entwicklung | 25 Prozent | 35 Prozent | 45 Prozent |
| Experimentelle Entwicklung mit Bonus | bis 40 Prozent | bis 50 Prozent | bis 60 Prozent |

**Kumulierungsregel:** alle staatlichen Beihilfen für dasselbe Vorhaben (oder dieselben förderfähigen Kosten) zusammen dürfen die Höchstintensität nicht überschreiten.

## Praxisleitfaden — die häufigsten Konflikte

### ZIM (Zentrales Innovationsprogramm Mittelstand) + FZulG

- ZIM und FZulG sind beide AGVO-Art.-25-Beihilfen.
- Wenn ZIM eine Förderquote von z. B. 45 Prozent gewährt, bleibt für FZulG nur die Differenz bis zur Höchstintensität.
- **Konsequenz:** sauber pro Kostenposten trennen, ZIM-geförderte Kosten getrennt von den FZulG-Kosten anlegen, sonst Doppelförderung.

### BMBF-Programm + FZulG

- BMBF-Programme variieren stark. Quote, Antragsbasis und förderfähige Kosten unterscheiden sich.
- **Trick:** dieselben Personalkosten dürfen nicht in beiden Bemessungsgrundlagen stehen. Stundenaufzeichnung muss eine eindeutige Zuordnung haben.

### Landesförderung + FZulG

- Länderprogramme greifen oft nur regional und nur für bestimmte Branchen.
- Auch hier AGVO-Höchstintensität beachten.

### EU/Horizon + FZulG

- Horizon Europe ist EU-Mittel, kann aber im AGVO-Sinne als staatliche Beihilfe kumuliert werden, wenn nicht direktverwaltet als Unions-Beihilfe.
- Im Zweifel mit dem Horizon-Förderbescheid prüfen, ob Kumulierung möglich.

### De-minimis (Verordnung (EU) 2023/2831)

- De-minimis ist nicht beschränkt auf FuE.
- Es gilt eine Obergrenze pro 3-Jahres-Zeitraum (vom Antragsteller mit aktueller Verordnung zu prüfen).
- De-minimis und AGVO können in der Regel kumuliert werden, soweit sie nicht denselben Kostenposten betreffen und die Höchstintensität nicht überschritten wird.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| FZulG vor ZIM vs. ZIM vor FZulG | FZulG zuerst, dann ZIM-Restquote | ZIM zuerst, dann FZulG-Restquote | meist FZulG zuerst, weil rückwirkend möglich |
| Kombinieren vs. Trennen | gemeinsames Vorhaben | separate Vorhaben | Trennen bei klaren Teilprojekten |
| Bonuskriterien nutzen | höhere Quote bei Konsortium | einfacheres Verfahren ohne | Bonus bei Forschungsverbund |
| Verbund vs. solo | höhere Förderintensität | weniger Komplexität | Verbund nur, wenn Partner stabil |

## Schritt für Schritt — das Kumulierungsblatt

1. Alle laufenden und beantragten Förderungen für das Vorhaben sammeln.
2. Pro Förderung: Höhe, Quote, förderfähige Kosten, Bewilligungszeitraum.
3. Förderfähige Kosten je Förderung pro Kostenart aufschlüsseln (Personal, Auftrag, Material).
4. Höchstintensität nach AGVO-Kategorie ermitteln.
5. Kumulierte Förderintensität rechnen.
6. Falls Überschreitung droht: FZulG-Bemessungsgrundlage kürzen oder Vorhaben trennen.
7. Kumulierungsblatt als Anlage zum Finanzamt-Antrag beifügen.

## Mustertexte / Vorlagen

**Kumulierungsblatt je Vorhaben (Vorlage):**

| Förderung | Quelle | Kategorie | Quote | Beihilfewert | Förderfähige Kosten | Beihilfeintensität |
| --- | --- | --- | --- | --- | --- | --- |
| FZulG | Finanzamt | Art. 25 | 25 Prozent (oder 35 Prozent KMU) | | | |
| ZIM | BAFA | Art. 25 | 45 Prozent | | | |
| Landesförderung | Land | Art. 25 | 20 Prozent | | | |
| Horizon Europe | EU | Art. 25 | | | | |
| Summe | | | | | | sollte unter Höchstintensität liegen |

**Mustertext für Anlage zum Finanzamt-Antrag:**

"Anlage Kumulierung gemäß AGVO Art. 8

Für das geförderte Vorhaben [Titel] wurden folgende staatlichen Beihilfen gewährt: [Aufzählung]. Die kumulierte Beihilfeintensität beträgt [Wert] Prozent. Die für die Kategorie [industrielle Forschung / experimentelle Entwicklung] zulässige Höchstintensität von [Wert] Prozent wird nicht überschritten."

## Typische Fehler

- Personalkosten doppelt angesetzt (in ZIM-Kostenplan und in FZulG-Berechnung).
- Höchstintensität ohne Bonuskriterien gerechnet, obwohl Bonus möglich wäre.
- De-minimis verwechselt mit AGVO-Beihilfe.
- Kumulierungsblatt fehlt im Finanzamt-Antrag.
- Verbundene Unternehmen nicht als Einheit betrachtet.
- Unterschiedliche Bewilligungszeiträume nicht beachtet: ZIM läuft über 24 Monate, FZulG je Wirtschaftsjahr — die Zuordnung der Kostenposten je Periode ist sorgfältig zu führen.
- Untervergaben des Auftragnehmers nicht geprüft — Subunternehmer außerhalb EU/EWR können die Auftragsforschung kippen.

## Praxis-Trick — frühzeitiger Kontakt mit dem Zuwendungsgeber

Bei laufenden Förderprogrammen (ZIM, BMBF, Land) lohnt sich ein frühzeitiger Hinweis an den Zuwendungsgeber, dass parallel FZulG beantragt wird. Damit ist später bei der Mittelverwendungsprüfung dokumentiert, dass die Kumulierung von Anfang an offen gelegt war. Stillschweigende Doppelförderung führt regelmäßig zu Rückforderungen.

## Sanity-Check vor Einreichung

Vor jedem Finanzamt-Antrag:

1. Kumulierungsblatt aktualisiert?
2. Höchstintensität nach AGVO-Kategorie korrekt?
3. Keine doppelt angesetzten Kostenposten?
4. Auftragnehmer-Sitznachweis EU/EWR vorhanden?
5. Subunternehmerkette mitgeprüft?

## Output

- Fördermittel-Synopse aller laufenden und beantragten Förderungen.
- Kosten-Deduplizierung je Kostenart.
- Beihilfen-Risikoampel.
- Formulierung für Antrag und Prüferakte.
- Anlage Kumulierungsblatt zum Finanzamt-Antrag.

## Querverweise

- `fz-bemessungsgrundlage-2026` für die Personalkosten und die FZulG-Quote.
- `fz-finanzamt-festsetzung-auszahlung` zur Anlage Kumulierungsblatt.
- `fz-dokumentationspaket-betriebspruefung` für die Belegfähigkeit.
- `fz-ablehnung-nachbesserung-einspruch` falls Finanzamt wegen Kumulierung kürzt.

## Quellen Stand 05/2026

- AGVO Verordnung (EU) 651/2014 (insbesondere Art. 8, Art. 25; vom Antragsteller mit konsolidierter Fassung zu prüfen).
- De-minimis Verordnung (EU) 2023/2831 (Antragsteller live zu prüfen).
- BSFZ Wachstumschancengesetz: https://www.bescheinigung-forschungszulage.de/wachstumschancengesetz
- BMF-Hinweise zur Forschungszulage.

## 3. `fz-personalkosten-und-stundennachweis`

**Fokus:** Foerderfaehige Personalkosten der Forschungszulage: Bruttoarbeitslohn plus Arbeitgeberanteile, Stundenpauschale 70 Euro Eigenunternehmer, Auftragsforschung 60 Prozent (KMU 70 Prozent). Stundennachweissystem: tagesgenau, Aufgabenbezug, Plausibilitaet. Typische Pruefungsfeststellungen des Finanzamts und Abwehr.

# FZ: Personal und Stundennachweis

## Spezialwissen: FZ: Personal und Stundennachweis
- **Spezialgegenstand:** FZ: Personal und Stundennachweis / fz personalkosten und stundennachweis. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KMU, FZ.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
