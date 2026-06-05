---
name: foerderstrategie-schnell-grossgeraete-cluster
description: "Foerderstrategie Schnell Grossgeraete Cluster: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Foerderstrategie Schnell Grossgeraete Cluster

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Foerderstrategie Schnell Grossgeraete Cluster** im Plugin DFG-Förderantrag. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dfg-foerderstrategie-schnell-oder-gross` | Strategischer DFG-Router: entscheidet zwischen kleiner schneller Sachbeihilfe, normalem Antrag über 200.000 Euro, Koselleck ab 500.000 Euro oder anderem DFG-Programm. Enthält Spatz-in-der-Hand-Logik, Kürzungsrisiko, Begutachtungsdichte und Zeitstrategie. |
| `dfg-grossgeraete-und-cluster-antrag` | Grossgeraete und Cluster-Geraete in DFG-Antrag: Geraete ab 50.000 Euro mit zusaetzlicher Wirtschaftlichkeit, Auslastungsplan, technische Anschlussbedingungen, Wartungsvertrag, Folgekosten. Eigene Geraetekommission der DFG. Pruefraster fuer Beschaffungsbegruendung und Marktrecherche. |
| `dfg-grundsystem-foerderlinien` | Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, GRK, Forschergruppen, Schwerpunktprogramme. Pro Linie: Zielgruppe, Hoehe, Dauer, Antragsweg, Begutachtungsstil. Fuer Erstantragsteller mit Entscheidungshilfe zur passenden Linie. Routet in dfg-foerderstrategie-schnell-oder-gross fuer konkrete Auswahl. |

## Arbeitsweg

Im Plugin DFG-Förderantrag gilt für **Foerderstrategie Schnell Grossgeraete Cluster**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dfg-foerderstrategie-schnell-oder-gross`

**Fokus:** Strategischer DFG-Router: entscheidet zwischen kleiner schneller Sachbeihilfe, normalem Antrag über 200.000 Euro, Koselleck ab 500.000 Euro oder anderem DFG-Programm. Enthält Spatz-in-der-Hand-Logik, Kürzungsrisiko, Begutachtungsdichte und Zeitstrategie.

# DFG-Förderstrategie: schnell, schlank oder groß?

## Worum geht es

Dieser Skill verhindert den typischen Erstantragsfehler, aus jedem guten Forschungsprojekt sofort einen zu großen Antrag zu machen. Er liefert die strategische Wegentscheidung: Welche Programmschiene passt zur Projektreife, zum Karrierestand und zum Zeithorizont? Was ist der schnellste belastbare Förderweg, der wissenschaftlich nicht zu klein denkt?

**Alte-Hasen-Faustregel:** Der Spatz in der Hand ist die schnelle Sachbeihilfe mit klarer Kernfrage. Die Taube auf dem Dach ist der Großantrag, der nach 9 Monaten gekürzt zurückkommt oder ganz scheitert. Wer DFG-frisch ist, sollte zunächst eine bewilligte Sachbeihilfe vorweisen können, bevor er Koselleck oder SPP-Initiierung anstrebt.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen diesen Skill, wenn die Programmroute noch offen ist, wenn der Antragsteller schwankt zwischen "kleinem schnellen Antrag" und "großem Wurf", oder wenn das Vorhaben zu groß für Sachbeihilfe und zu wenig visionär für Koselleck wirkt.

Kaltstartfragen:

1. **Karrierestand exakt:** Promotionsjahr, Habilitationsstand, Berufung, frühere DFG-Bewilligungen.
2. **Projektreife:** Wie viele referierte Vorarbeiten zur Frage gibt es bereits? Stand 0, Stand "Pilot vorhanden", Stand "in einschlägigen Journalen publiziert"?
3. **Geldbedarf realistisch:** Welche Summe reicht für eine publikationsfähige Antwort (Minimalvariante)? Was ist die Ausbauvariante?
4. **Zeitdruck:** Stelle läuft aus? Datenfenster? Gerätebeschaffung?
5. **Profilstärke:** Wie sieht der Track Record im Verhältnis zur eingespielten Konkurrenz im Fach aus?

## Programm- bzw. Sachrahmen

**Sachbeihilfe** ist die themenoffene Einzelförderung — jederzeit einreichbar, ein bis drei Jahre Laufzeit (Verlängerung möglich), Module nach Bedarf kombinierbar. Die Mehrheit aller DFG-Anträge läuft hier.

**Walter Benjamin** richtet sich an Postdocs in der frühen Phase, eigene Stelle plus Sachmittel, auch im Ausland.

**Emmy Noether** ist die Nachwuchsgruppenleitung für die frühe Postdoc-Phase — 6 Jahre, eigene Stelle plus Personal — verlangt aber besondere Selbstständigkeit und meist Auslandserfahrung.

**Heisenberg-Programm** ist die Brücke nach der Habilitation bis zur Lebenszeitprofessur, 5 Jahre eigene Stelle plus Forschungsmittel.

**Reinhart-Koselleck-Projekt** ist die Risiko-Vision-Schiene: 500.000 bis 1.250.000 Euro, 5 Jahre, in Stufen von 250.000 Euro, für herausragende Forschende mit besonders innovativen oder positiv risikobehafteten Vorhaben. Mehrere erfolgreich abgeschlossene DFG-Projekte sind ein starkes Praxisindiz für den nötigen Vertrauensvorschuss, aber nicht als starre formale Eingangsschwelle behaupten.

**Schwerpunktprogramm (SPP)** und **Sonderforschungsbereich (SFB)** sind Verbundinstrumente mit langer Vorlaufzeit — eigenes Spielfeld, nicht durch diesen Skill abgedeckt.

## Praxisleitfaden

**Begutachtungsdichte und Zeit zur Genehmigung.** Faustwerte aus der Praxis (Stand 2025/26, abhängig vom Fachkollegium):

- Sachbeihilfe unter 200.000 Euro: 1 bis 2 Gutachten, Bescheid in 5 bis 7 Monaten.
- Sachbeihilfe über 200.000 Euro: 2 bis 4 Gutachten, Bescheid in 6 bis 9 Monaten.
- Koselleck: regelmäßig 3 bis 4 Gutachten plus Hauptausschuss-Logik, Bescheid in 9 bis 12 Monaten.
- SPP-Initiierung: 12 bis 18 Monate Vorlauf bis Programmstart.
- ENP-Einzelanträge (innerhalb SPP): typisch 6 Monate Bescheid.

**Was schnelle Genehmigung produziert.** Programmroute matchen zur Projektreife. Wer eine Pilotstudie und zwei referierte Vorarbeiten hat, soll keinen Koselleck-Antrag stellen — die Begutachter erwarten dort etablierte Spitzenposition. Wer dagegen vier hochrangige Vorarbeiten und eine prüfbare Großthese hat, der sollte nicht in der schmalen Sachbeihilfe verkrümmen.

**Was Reviewer triggert beim Programm-Mismatch.** "Antrag passt eher in [anderes Programm]" — fatal, der Antrag wandert nicht automatisch um. "Größenordnung nicht angemessen" — passiert, wenn 600.000-Euro-Sachbeihilfe ohne Großantragsbegründung kommt. "Antragsteller könnte Koselleck wählen" — wenn ein etablierter Profilantragsteller sich in die Sachbeihilfe quetscht, wirkt das wie Risikoaversion.

**Schreiben passend zum Programm.** Sachbeihilfe verlangt ein **machbares** Arbeitsprogramm mit klar definierten Meilensteinen. Koselleck verlangt eine **Vision**, deren Machbarkeit nicht detailliert ausgewiesen sein muss — aber das Risiko muss produktiv beschrieben sein, nicht als Management-Risiko. Walter Benjamin verlangt ein **persönliches Entwicklungsnarrativ** — was lernt der Antragsteller, das ihm später hilft? Emmy Noether verlangt eine **Gruppen-Vision** — eigene Linie plus Nachwuchsführung.

**Kürzungsrisiko-Logik.** Großanträge werden häufiger gekürzt als kleine. Wenn die Begutachter "im Prinzip ja, aber..." schreiben, kürzt der Hauptausschuss gerne 20 bis 40 Prozent — was beim Großantrag eine Stelle weniger bedeutet, beim Kleinantrag dagegen kaum spürbar ist. Daraus folgt: **Wenn eine Arbeitspaketstreichung tödlich wäre, ist der Antrag entweder zu groß angesetzt oder die Pakete sind nicht modular gedacht.**

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Schnell vs. groß | Sachbeihilfe unter 200k, 1 Gutachten möglich | Sachbeihilfe über 200k oder Koselleck | Bei DFG-Erstantrag Pfad A; nach erstem Erfolg Pfad B |
| Programm-Karrierestand-Match | Sachbeihilfe (jeder mit Promotion) | Karriereprogramm (Walter Benjamin, Emmy Noether, Heisenberg, Koselleck) | Match exakt prüfen — Programmverwechslung kostet Monate |
| Solo vs. SPP-Andocken | Einzelantrag Sachbeihilfe | SPP-Einzelantrag (ENP) | Wenn passendes SPP läuft, Andocken — bessere Begutachtungs-Logik |
| Erstantrag vs. Großvision | Erstantrag schlank | Vision-Antrag groß | Vor erstem DFG-Erfolg keinen Koselleck |
| Großantrag jetzt vs. zwei kleine | Ein 800k-Antrag | Zwei aufeinanderfolgende 300k-Anträge | Bei methodischer Stufung zwei kleine — bessere Lernkurve und Resilienz |

## Entscheidungsmotor

Wenn die Nutzerseite mehrere Wege will, immer drei Varianten nebeneinanderlegen:

| Variante | Frage | Typischer Nutzen |
| --- | --- | --- |
| **Minimal förderfähig** | Was ist die kleinste wissenschaftlich ehrliche Antwort? | schnell, kürzungsfest, gut für Erstantrag |
| **Optimal wissenschaftlich** | Was wäre fachlich am stärksten, wenn Zeit und Profil reichen? | besserer Erkenntnisgewinn, mehr Risiko |
| **Prestige / Vision** | Ist das Vorhaben wirklich jenseits normaler Planung? | Koselleck/SPP/SFB nur bei Profil und Vorlauf |

Danach eine klare Empfehlung ausgeben, nicht alle Wege gleichwertig nebeneinander stehen lassen. Wenn ein Weg eitel, aber unklug ist, höflich klar sagen.

## Schritt für Schritt

1. **Karrierestand und Vorprojekte erfassen.** GEPRIS-Suche nach allen DFG-Vorhaben des Antragstellers.
2. **Projektreife einstufen:** Pilot, einschlägige Publikation, Spitzenpublikation.
3. **Minimal- und Idealvariante rechnen.** Was kostet die Antwort auf die Kernfrage minimal? Was wäre ideal?
4. **Programmroute matchen** mit der Trade-off-Matrix.
5. **Begutachtungsdichte und Zeit zum Bescheid budgetieren.** Stellt der Antragsteller die Stelle in 6 Monaten an? Dann Pfad A.
6. **Empfehlung mit drei Alternativen ausformulieren** (siehe Output unten).
7. **Vor Einreichung: Telefonat mit DFG-Geschäftsstelle** durch Antragsteller, nicht durch Sie.

## Mustertexte / Vorlagen

**Routing-Empfehlung an Antragsteller** (Vorlage):

> "Nach Sichtung Ihres Profils [drei Sätze Profil: Karrierestand, Vorarbeiten, Methodenstärke] empfehle ich folgende Förderstrategie:
>
> **Empfehlung A (schnellster tragfähiger Weg):** Sachbeihilfe mit Volumen [Zahl] Euro, 3 Jahre, Begutachtung absehbar [Monate]. Risiko: gering, Kürzungstoleranz: hoch.
>
> **Empfehlung B (wissenschaftlich ideale Ausbaustufe):** [Sachbeihilfe größer / Koselleck / SPP-Andocken] mit Volumen [Zahl] Euro, [Laufzeit]. Voraussetzung: [zusätzliche Vorarbeit / zweites Drittmittelprojekt / Beratungsschleife mit Geschäftsstelle].
>
> **Empfehlung C (was wir gerade nicht tun):** [Großantrag / Koselleck], weil [Profilstärke / Vorarbeitenlage / fehlende Vorprojekte] aktuell gegen Vertrauensvorschuss spricht.
>
> Vorgehensvorschlag: Wir starten Pfad A in den nächsten 10 Arbeitstagen — Skizze, dann Volltext. Falls Sie auf Pfad B drängen, lege ich die Risikoampel offen."

**Begutachtungsrisiko-Ampel:**

| Aspekt | Grün | Gelb | Rot |
| --- | --- | --- | --- |
| Vorarbeiten-Match | drei einschlägige Volltexte | zwei Volltexte | nur Konferenzbeiträge |
| Profil-Programm-Match | klar | grenzwertig | Programmverwechslung |
| Budgetlogik | jede Position AP-funktional | eine bis zwei Positionen weich | Wunschliste sichtbar |
| Methodik | Triangulation begründet | Single-Method nicht begründet | Methode nicht spezifiziert |

## Typische Fehler

- "Lieber gleich groß beantragen, dann hat man Puffer für Kürzung" — Reviewer erkennen das und kürzen stärker.
- Koselleck als "größere Sachbeihilfe" verkaufen — Begutachter merken sofort, ob das echte Risiko-Vision-Vorhaben ist oder nur ein normales Großprojekt mit Etikett.
- Walter Benjamin und Emmy Noether parallel beantragen — gilt als unklare Karriereplanung.
- SPP-Andocken ignorieren, obwohl ein passendes Programm läuft — Reviewer fragen explizit nach.
- "Wir warten auf den nächsten Hauptausschuss" — Sachbeihilfe ist jederzeit einreichbar, das Warten kostet Monate.

## Output

- **Empfehlung A** — schnellster tragfähiger Antrag mit Volumen, Modulen, Begutachtungs-Zeitschätzung.
- **Empfehlung B** — wissenschaftlich ideale Ausbaustufe, mit Voraussetzungen.
- **Empfehlung C** — was bewusst nicht gewählt wird und warum.
- **Begutachtungsrisiko-Ampel** für Profilmatch, Vorarbeiten, Budget, Methodik.
- **To-do-Liste 10 Arbeitstage:** Skizze, Vorarbeiten-Tabelle, GEPRIS-Vergleich, Telefonat Geschäftsstelle.

## Querverweise

- Einstieg: `dfg-foerderantrag-allgemein`
- Sachbeihilfe-Detail: `dfg-sachbeihilfe-elan-formalia`
- Kompaktantrag: `dfg-bis-200k-begutachtung-light`
- Koselleck: `dfg-koselleck-500k-125m`

## Quellen Stand 05/2026

- DFG-Programmübersicht (Einzelförderung): dfg.de
- DFG-FAQ Begutachtung (Schwellen-Logik 200k): dfg.de
- DFG-Hinweise Antragstellung: dfg.de
- Reinhart-Koselleck-Seite: dfg.de
- GEPRIS für Karrierestand-Kalibrierung: gepris.dfg.de

Alle Schwellen und Programmregeln **live** an der DFG-Seite zum Einreichtag prüfen — Verfahrensregeln ändern sich.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `dfg-grossgeraete-und-cluster-antrag`

**Fokus:** Grossgeraete und Cluster-Geraete in DFG-Antrag: Geraete ab 50.000 Euro mit zusaetzlicher Wirtschaftlichkeit, Auslastungsplan, technische Anschlussbedingungen, Wartungsvertrag, Folgekosten. Eigene Geraetekommission der DFG. Pruefraster fuer Beschaffungsbegruendung und Marktrecherche.

# DFG: Grossgeraete und Cluster

## Spezialwissen: DFG: Grossgeraete und Cluster
- **Spezialgegenstand:** DFG: Grossgeraete und Cluster / dfg grossgeraete und cluster antrag. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DFG.
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

## 3. `dfg-grundsystem-foerderlinien`

**Fokus:** Grundsystem der DFG-Foerderlinien einfuehrend erklaeren: Sachbeihilfe (Einzelantrag), Emmy Noether, Heisenberg, Reinhart Koselleck, SFB, GRK, Forschergruppen, Schwerpunktprogramme. Pro Linie: Zielgruppe, Hoehe, Dauer, Antragsweg, Begutachtungsstil. Fuer Erstantragsteller mit Entscheidungshilfe zur passenden Linie. Routet in dfg-foerderstrategie-schnell-oder-gross fuer konkrete Auswahl.

# Grundsystem DFG-Foerderlinien

## Spezialwissen: Grundsystem DFG-Foerderlinien
- **Spezialgegenstand:** Grundsystem DFG-Foerderlinien / dfg grundsystem foerderlinien. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DFG, SFB, GRK.
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
