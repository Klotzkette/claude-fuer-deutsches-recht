---
name: dfg-software-veroeffentlichung-tieforschung
description: "Software Veroeffentlichung Tieforschung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Software Veroeffentlichung Tieforschung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Software Veroeffentlichung Tieforschung** im Plugin DFG-Förderantrag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dfg-software-veroeffentlichung-spezial` | Spezialfall Software als Forschungsergebnis: DFG-Hinweise zur Open-Source-Veroeffentlichung, Lizenzwahl (MIT, BSD, Apache-2.0, GPL), Zenodo-DOI, Reproducibility. Pruefraster und Mustertext fuer Software-Sektion im Arbeitsprogramm. |
| `dfg-tieforschung-ethik-pflichten` | Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchsantrag bei der Behoerde parallel zur DFG. DFG-Senatskommission fuer tierexperimentelle Forschung. Ethik-Sektion im Antrag, Belastungsstufen, alternative Methoden. Routet in dfg-ki-ethik-forschungsdaten fuer parallele Daten- und KI-Fragen. |
| `dfg-wiedereinreichung-nach-ablehnung` | DFG-Ablehnung, Gutachten und Entscheidung auswerten: tragende Kritik extrahieren, Verteidigungsreflex vermeiden, Wiedereinreichung planen, Antrag umbauen, Anschreiben und Änderungsmatrix erstellen. |

## Arbeitsweg

Im Plugin DFG-Förderantrag gilt für **Software Veroeffentlichung Tieforschung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dfg-software-veroeffentlichung-spezial`

**Fokus:** Spezialfall Software als Forschungsergebnis: DFG-Hinweise zur Open-Source-Veroeffentlichung, Lizenzwahl (MIT, BSD, Apache-2.0, GPL), Zenodo-DOI, Reproducibility. Pruefraster und Mustertext fuer Software-Sektion im Arbeitsprogramm.

# DFG: Software-Veroeffentlichung

## Spezialwissen: DFG: Software-Veroeffentlichung
- **Spezialgegenstand:** DFG: Software-Veroeffentlichung / dfg software veroeffentlichung spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DFG, MIT, BSD, GPL, DOI.
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

## 2. `dfg-tieforschung-ethik-pflichten`

**Fokus:** Tierversuchsethik-Pflichten in DFG-Antraegen: 3R-Prinzip (Replace, Reduce, Refine), TierSchG, TierSchVersV, Tierversuchsantrag bei der Behoerde parallel zur DFG. DFG-Senatskommission fuer tierexperimentelle Forschung. Ethik-Sektion im Antrag, Belastungsstufen, alternative Methoden. Routet in dfg-ki-ethik-forschungsdaten fuer parallele Daten- und KI-Fragen.

# Tierforschungs-Ethikpflichten

## Spezialwissen: Tierforschungs-Ethikpflichten
- **Spezialgegenstand:** Tierforschungs-Ethikpflichten / dfg tieforschung ethik pflichten. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DFG, TierSchG, TierSchVersV, KI.
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

## 3. `dfg-wiedereinreichung-nach-ablehnung`

**Fokus:** DFG-Ablehnung, Gutachten und Entscheidung auswerten: tragende Kritik extrahieren, Verteidigungsreflex vermeiden, Wiedereinreichung planen, Antrag umbauen, Anschreiben und Änderungsmatrix erstellen.

# Wiedereinreichung nach Ablehnung

## Worum geht es

Eine Ablehnung ist nicht das Ende, sondern **Material**. Die Gutachten enthalten typischerweise sehr konkrete Hinweise, wo der Antrag schwach war — und die Wiedereinreichung kann diese Hinweise produktiv nutzen. Dieser Skill trennt die verletzende Tonlage von der tragenden Kritik, baut daraus eine bessere Fassung und ergänzt eine Stellungnahme, die nicht defensiv, sondern konstruktiv-souverän auftritt.

**Alte-Hasen-Faustregel:** Die meisten gescheiterten Wiedereinreichungen scheitern daran, dass der Antragsteller die Kritik **inhaltlich überlesen** und stattdessen **textuell überspielt** hat. Wer in der Stellungnahme nur sagt "das war ein Missverständnis", wird wieder abgelehnt. Wer drei konkrete strukturelle Änderungen zeigt, hat hohe Wiedereinreichungschancen.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen diesen Skill, wenn:

- Eine Ablehnung der DFG (mit Gutachten) vorliegt.
- Sie zwischen Wiedereinreichung, neuer Programmschiene oder Aufgabe entscheiden müssen.
- Eine Stellungnahme zu den Gutachten verfasst werden soll.
- Eine substanzielle Überarbeitung der Projektbeschreibung ansteht.

Kaltstartfragen:

1. **Wie viele Gutachten liegen vor?** Eines, zwei, drei?
2. **Tenor der Gutachten:** alle ablehnend, gemischt, knapp negativ?
3. **Tragende Kritikpunkte:** identifizierbar? Wiederholt in mehreren Gutachten?
4. **Fatale Kritik vs. reparierbare Kritik:** klar trennbar?
5. **Wiedereinreichungs-Sperrfrist:** vorhanden? (vom Antragsteller in der DFG-Verfahrensordnung des Bescheids zu prüfen — bei Sachbeihilfe typischerweise keine starre Sperre, aber bei einigen Programmen 12-Monats-Sperre).
6. **Ressourcen für Überarbeitung:** Zeit, Mitarbeiter, ggf. neue Vorarbeiten?

## Programm- bzw. Sachrahmen

**DFG-Praxis nach Ablehnung.** Die DFG schickt das Ablehnungsschreiben mit Gutachten (anonymisiert). Antragsteller können:

1. **Wiedereinreichung als Neuantrag** mit Stellungnahme zu den Vorgutachten. Das ist der Standardweg. Die DFG kann die Vorgutachten dem neuen Gutachterkreis bekanntmachen — Stellungnahme wird daher mit Bedacht formuliert.
2. **Anderer Förderpfad** — kleineres Programm, anderes Programm, oder Zwischenschritt (Vorstudie, Drittmittel-Pilot).
3. **Aufgabe oder Pause** — bei konzeptionell tiefer Kritik manchmal die ehrlichste Option.

**Sperrfristen.** Bei Sachbeihilfe gibt es typischerweise keine starre Sperrfrist. Bei einigen Karriereprogrammen (z. B. Emmy Noether) und bei wiederholt abgelehnten Anträgen kann es Empfehlungen oder Beschränkungen geben. **Vom Antragsteller in der DFG-Verfahrensordnung des Bescheids zu prüfen.**

**Stellungnahme zu Vorgutachten.** Wird typischerweise als **eigene Anlage** beigefügt (nicht als Teil der Projektbeschreibung). Form: tabellarisch oder narrativ. Empfehlung: tabellarisch, weil scanbar.

**Kommunikation mit DFG-Geschäftsstelle.** Bei substanzieller Ablehnung und vor Wiedereinreichung anrufen — die Geschäftsstelle gibt Hinweise, ob die Kritik durch Überarbeitung adressierbar ist oder ob der Antrag in eine andere Schiene gehört.

## Praxisleitfaden

**Kritik-Triage.**

Schritt 1: Gutachten **anonymisiert** auswerten (mit zeitlichem Abstand — nicht am Tag des Bescheids).

Schritt 2: Kritik **kategorisieren** in vier Eimer:

- **Fatal-konzeptionell:** das Projekt ist nicht förderfähig im DFG-Sinne (z. B. nicht grundlagenorientiert, nicht innovativ, falsches Programm). Wiedereinreichung sinnlos — anderer Pfad.
- **Methodisch reparierbar:** Methodendetails fehlen, Statistik unklar, Stichprobengröße zu klein. Reparierbar.
- **Vorarbeiten / Profil-Kritik:** zu dünn, nicht einschlägig genug. Brauchbar mit zusätzlichen Vorarbeiten oder Co-Antragstellern.
- **Missverständnis / Tonlage:** Reviewer hat etwas nicht verstanden oder unfair formuliert. Vorsichtig damit umgehen — solche Kritik wird oft nicht beim Wort genommen.

Schritt 3: Wiederholungen erkennen. Wenn drei Gutachter dasselbe sagen, ist es nicht "Missverständnis" sondern Antragsschwäche.

**Was schnelle Genehmigung der Wiedereinreichung produziert.**

- **Klare Änderungsmatrix.** Jede Kritik mit konkretem "wir haben geändert: [Seite X, Abschnitt Y]".
- **Strukturelle Änderungen sichtbar.** Reviewer schätzt, wenn der Antrag erkennbar umgebaut wurde — nicht nur Kosmetik.
- **Stellungnahme nicht defensiv.** "Wir danken den Gutachtern für die hilfreichen Hinweise" ist Standardeinleitung. Dann sachlich Punkt für Punkt.
- **Auch unfaire Kritik produktiv aufnehmen.** Wenn ein Gutachter unverhältnismäßig hart war: nicht streiten, sondern die Kritik präzisieren ("Wir verstehen den Gutachter X so, dass [konkrete Aussage]. Hierzu: [unsere Antwort mit konkretem Beleg]").
- **Neue Vorarbeiten ergänzen** — in der Zwischenzeit Publiziertes oder zur Publikation eingereichtes Material einbringen.

**Was Reviewer in der Wiedereinreichung triggert.**

- **"Antrag wirkt unverändert"** — wenn die Stellungnahme nur kosmetische Änderungen verspricht.
- **"Verteidigungsreflex"** — wenn der Antragsteller Kritik abwehrt, statt sie aufzunehmen.
- **"Gleiche Vorarbeiten wie vor 12 Monaten"** — wenn keine neuen Publikationen.
- **"Sie haben den Hinweis [X] nicht aufgegriffen"** — wenn ein Punkt aus dem Vorgutachten ignoriert wurde.

**Sprache der Stellungnahme.**

- **Nicht:** "Der Gutachter hat unsere Methodik nicht verstanden." → defensiv.
- **Stattdessen:** "Wir haben die Methodikbeschreibung präzisiert und in AP2 die Stichprobenberechnung explizit dargestellt (S. 9)." → konstruktiv.

- **Nicht:** "Diese Kritik teilen wir nicht, weil..." → konfrontativ.
- **Stattdessen:** "Den Hinweis nehmen wir auf, sehen aber [konkrete Begründung mit Beleg], dass [unsere Position]. Im Antrag haben wir die Stelle entsprechend erweitert (S. 12)." → sachlich.

**Trade-off Wiedereinreichung vs. anderer Pfad.**

| Kritik-Typ | Wiedereinreichung sinnvoll? | Alternative |
| --- | --- | --- |
| Methodendetails fehlen | Ja | n/a |
| Vorarbeiten dünn | Ja, mit neuen Vorarbeiten | Vorstudie als Vorarbeiten-Generator |
| Konzeptionell unklar | Nur mit substanzieller Überarbeitung | Programmwechsel, anderer Pfad |
| Falsches Programm | Nein | Anderes Programm |
| "Eher Sachbeihilfe als Koselleck" | Programmwechsel | Sachbeihilfe |
| Drei Gutachter sehr negativ | Nein, eher anderer Pfad | Pause, anderer Pfad, Kooperation |
| Ein Gutachten unfair | Ja | n/a |
| Vision nicht überzeugend | Schwer, wenn fundamental | Anderer Pfad oder Kooperation |

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Wiedereinreichung schnell vs. überlegt | nach 3 Monaten | nach 9-12 Monaten | Überlegt — wenn dazwischen Vorarbeit publizierbar |
| Stellungnahme tabellarisch vs. narrativ | Tabelle | Fließtext | Tabelle — Reviewer scannt schneller |
| Verteidigen vs. aufnehmen | streiten | konstruktiv aufnehmen | Aufnehmen, immer |
| Programm wechseln vs. wiedereinreichen | anderes Programm | gleiches Programm | Je nach Kritik-Typ |
| Solo wiedereinreichen vs. Kooperation | allein | mit Co-PI | Kooperation kann methodische Kritik entschärfen |
| Mit Anschreiben an DFG vs. ohne | Deckblatt-Notiz | nichts | Stellungnahme als Anlage, kein separates Anschreiben außer in Sonderfällen |

## Schritt für Schritt

1. **Gutachten anonymisiert auswerten** (1 Woche Abstand zum Bescheid einplanen).
2. **Kritik kategorisieren** in fatal-konzeptionell / methodisch reparierbar / Vorarbeiten / Missverständnis.
3. **Wiederholungen erkennen** — was sagen zwei oder drei Gutachter gleichermaßen?
4. **Entscheiden:** Wiedereinreichung, Programmwechsel, Pause.
5. **Falls Wiedereinreichung:** Änderungsmatrix bauen (Kritik — Änderung — Seite).
6. **Neue Vorarbeiten beschaffen** (Publikationen einreichen, Pilot-Daten generieren).
7. **Antrag strukturell überarbeiten** — nicht nur kosmetisch.
8. **Stellungnahme verfassen** (tabellarisch, sachlich-konstruktiv).
9. **Vor Wiedereinreichung Geschäftsstelle anrufen** (Antragsteller).
10. **Red-Team neuen Entwurf** (`dfg-reviewer-red-team`).

## Mustertexte / Vorlagen

**Stellungnahme-Tabelle** (Vorlage, als Anlage zur Wiedereinreichung):

| Nr. | Hinweis aus Vorgutachten | Unsere Antwort und Änderung | Seite im neuen Antrag |
| --- | --- | --- | --- |
| 1 | Gutachten A: "Methodische Triangulation in AP2 nicht hinreichend begründet." | Wir haben in AP2 die Triangulation aus qualitativer und quantitativer Erhebung mit Bezug auf [Methodenautor X] ausführlich begründet und die Verknüpfung der Datenströme dargestellt. | S. 9-10 |
| 2 | Gutachten A, B: "Stichprobengröße in AP3 nicht begründet." | Wir haben eine Power-Analyse durchgeführt (für Effektgröße d = 0.4, Power = 0.85, alpha = 0.05) und kommen auf n = 120. AP3 wurde entsprechend erweitert. | S. 11 |
| 3 | Gutachten B: "Eigene Vorarbeiten zur Hauptthese eher dünn." | Wir können seit dem Erstantrag drei zusätzliche referierte Volltexte einbringen ([Zitate]). Die Vorarbeiten-Tabelle wurde aktualisiert. | S. 6 |
| 4 | Gutachten C: "Antrag konzeptionell unklar bezüglich Mehrwert für Feld." | Wir haben das Kapitel "Mehrwert / Auswirkungen" deutlich erweitert (drei Ebenen: wissenschaftlich, methodisch, gesellschaftlich) und die theoretische Konsequenz der Erkenntnisse explizit ausgearbeitet. | S. 17-18 |

**Einleitung der Stellungnahme** (Vorlage):

> "Wir danken den Gutachtern und der Geschäftsstelle für die sorgfältige Begutachtung und die hilfreichen Hinweise. Die folgende Stellungnahme adressiert die zentralen Kritikpunkte tabellarisch. Wesentliche Änderungen sind: Die methodische Begründung in AP2 und AP3 wurde substanziell erweitert (Stichprobenberechnung, Triangulation, statistische Analyse). Drei zusätzliche referierte Vorarbeiten sind aufgenommen. Der Mehrwert des Vorhabens wurde theoretisch und methodisch ausgearbeitet. Punkte, an denen wir nach erneuter Prüfung in der Sache bei unserer Position bleiben, sind in der Tabelle mit Begründung markiert (Nr. [X])."

**Umgang mit unfairer Kritik** (Vorlage, in Tabelle):

> "Hinweis: 'Die Methode X ist für die Fragestellung ungeeignet.'
>
> Antwort: Wir nehmen den Hinweis ernst, sehen jedoch in der Forschungsliteratur ([Belegquellen]) klare Begründung dafür, dass Methode X für Fragestellungen dieses Typs verbreitet und valide eingesetzt wird. Um den Hinweis dennoch konstruktiv aufzunehmen, haben wir in AP2 die methodische Begründung erweitert und drei Validierungsschritte ergänzt (S. 9). Eine Methodenkombination mit Methode Y zur Triangulation ist zusätzlich vorgesehen (AP2.3)."

**Kurzanschreiben (bei Bedarf, optional)** (Vorlage):

> "Sehr geehrte Damen und Herren,
>
> hiermit reichen wir den Antrag [Titel] in überarbeiteter Fassung erneut ein. Wesentliche Änderungen gegenüber dem Erstantrag vom [Datum] (Az.: [Vorgängerantrag]):
>
> 1. Strukturelle Überarbeitung der Arbeitspakete AP2 und AP3 mit erweiterter Methodik und Stichprobenberechnung.
> 2. Aufnahme von drei zusätzlichen referierten Vorarbeiten.
> 3. Ausarbeitung des Mehrwert-Kapitels.
>
> Die detaillierte Stellungnahme zu den Vorgutachten findet sich in Anlage [X].
>
> Mit freundlichen Grüßen
> [Antragsteller]"

## Typische Fehler

- Gutachten unmittelbar nach Bescheid auswerten — emotional verfälschte Wahrnehmung.
- Verteidigungsreflex in Stellungnahme — Reviewer-2 sieht das und ist verstimmt.
- Nur kosmetische Änderungen — Reviewer-2 erkennt das und merkt es an.
- Vorarbeiten nicht aktualisiert — Antrag wirkt zeitlich eingefroren.
- Wiedereinreichung nach 3 Wochen ohne strukturelle Überarbeitung.
- Stellungnahme als langer Fließtext — schwer lesbar.
- Streiten mit Gutachtern in der Stellungnahme.
- Hinweise aus Gutachten ignoriert.
- Falsche Programmschiene beibehalten, obwohl Gutachten "passt eher in [anderes Programm]" sagt.
- Geschäftsstelle nicht angerufen vor Wiedereinreichung.

## Output

- **Gutachten-Synopse** mit Kritik-Kategorisierung.
- **Reparaturplan** mit konkreten Änderungen und Seitenverweisen.
- **Neue Antragsthese** (falls strukturelle Überarbeitung).
- **Stellungnahme tabellarisch.**
- **Kurzanschreiben** falls sinnvoll.
- **"Nicht mehr diskutieren"-Liste:** Punkte, die besser durch Textänderung als durch Verteidigung gelöst werden.
- **Entscheidungsvorlage** Wiedereinreichung vs. Programmwechsel vs. Pause.

## Querverweise

- Programmwechsel-Optionen: `dfg-foerderstrategie-schnell-oder-gross`
- Antrag strukturell überarbeiten: `dfg-projektbeschreibung-arbeitsprogramm`
- Vor Wiedereinreichung red-teamen: `dfg-reviewer-red-team`
- Formalia neue Einreichung: `dfg-sachbeihilfe-elan-formalia`

## Quellen Stand 05/2026

- DFG-FAQ zur Begutachtung und zu Wiedereinreichungen: dfg.de
- DFG-Hinweise zur Antragstellung (Wiedereinreichung): dfg.de
- DFG-Verfahrensordnung (Sperrfristen, Wiedereinreichungsregeln): dfg.de — am Tag des Bescheids und vor Wiedereinreichung live prüfen.

Sperrfristen und Verfahrensregeln zur Wiedereinreichung sind programmabhängig und ändern sich — vor Wiedereinreichung in der aktuellen Verfahrensordnung verifizieren.
