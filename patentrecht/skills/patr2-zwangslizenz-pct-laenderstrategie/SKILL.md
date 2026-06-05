---
name: patr2-zwangslizenz-pct-laenderstrategie
description: "Patr2 Zwangslizenz PCT Laenderstrategie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Patr2 Zwangslizenz PCT Laenderstrategie

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Patr2 Zwangslizenz PCT Laenderstrategie** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `patr2-zwangslizenz-spezial` | Spezialfall Zwangslizenz § 24 PatG und FRAND-Verteidigung: Voraussetzungen, EuGH Huawei / ZTE, kartellrechtliche Aspekte. Pruefraster fuer SEP-Inhaber und Implementer. |
| `pct-laenderstrategie-und-nationalphasen` | Plant PCT-Anmeldungen und Nationalphasen: Priorität, ISA/IPEA-Bericht, Länderbudget, Übersetzungen, Eintrittsfristen, Schutzrechtsmix und Abbruchentscheidungen. |
| `pruefungsbescheid-dpma-epa-erwiderung` | Bereitet Erwiderungen auf Prüfungsbescheide von DPMA oder EPA vor: Beanstandungen, Entgegenhaltungen, Anspruchsänderungen, Argumentation zu Neuheit/erfinderischer Tätigkeit und Mandantenrückfragen. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Patr2 Zwangslizenz PCT Laenderstrategie**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `patr2-zwangslizenz-spezial`

**Fokus:** Spezialfall Zwangslizenz § 24 PatG und FRAND-Verteidigung: Voraussetzungen, EuGH Huawei / ZTE, kartellrechtliche Aspekte. Pruefraster fuer SEP-Inhaber und Implementer.

# PatR2: Zwangslizenz FRAND

## Spezialwissen: PatR2: Zwangslizenz FRAND
- **Spezialgegenstand:** PatR2: Zwangslizenz FRAND / patr2 zwangslizenz spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** PatG, FRAND, ZTE, SEP.
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

## 2. `pct-laenderstrategie-und-nationalphasen`

**Fokus:** Plant PCT-Anmeldungen und Nationalphasen: Priorität, ISA/IPEA-Bericht, Länderbudget, Übersetzungen, Eintrittsfristen, Schutzrechtsmix und Abbruchentscheidungen.

# PCT und Nationalphasen

## Aufgabe

Internationale Anmeldestrategie über Paris/PCT mit Budget-, Markt- und Fristenlogik.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Prioritätsanmeldung und Veröffentlichungsrisiken sichern.**
2. **PCT-Route gegenüber Direktanmeldungen abwägen.**
3. **ISR/IPRP für Länderentscheidung auswerten.**
4. **Nationalphasen-Fristen, Übersetzungen und Vertreterbedarf erfassen.**
5. **Go/Kill/Delay-Entscheidung mit Budgetwirkungen formulieren.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- PCT Country Decision Matrix.
- National Phase Calendar.
- Budget Ampel.
- Mandantenmail.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.

## 3. `pruefungsbescheid-dpma-epa-erwiderung`

**Fokus:** Bereitet Erwiderungen auf Prüfungsbescheide von DPMA oder EPA vor: Beanstandungen, Entgegenhaltungen, Anspruchsänderungen, Argumentation zu Neuheit/erfinderischer Tätigkeit und Mandantenrückfragen.

# Prüfungsbescheid DPMA/EPA

## Vorgehen

1. Frist, Amt, Aktenzeichen und Verfahrensstand erfassen.
2. Jede Beanstandung einzeln aus dem Bescheid extrahieren.
3. Entgegenhaltungen mit Volltext und Fundstellen sichern.
4. Anspruchsfassung vor/nach Bescheid vergleichen.
5. Pro Beanstandung entscheiden: argumentieren, ändern, teilen, aufgeben, Rücksprache.
6. Anspruchsänderungen auf Stütze in ursprünglicher Offenbarung prüfen.
7. Mandantenrisiken und kommerziell wichtige Ausführungsformen abgleichen.

## Tabellenformat

| Beanstandung | Amtliche Begründung | Antwortlinie | Anspruchsänderung | Risiko |
| --- | --- | --- | --- | --- |

## Output

- Entwurf einer Erwiderungsstruktur.
- Änderungsvorschläge für Ansprüche.
- Argumentationsbausteine.
- Rückfragen an Mandant/Erfinder.
- Fristen- und Anlagencheck.

## Warnungen

Keine Anspruchsänderung vorschlagen, wenn Stütze in ursprünglicher Anmeldung unklar ist. Keine Entgegenhaltung nur aus dem Abstract bewerten.

## Pflicht-Normen und Praxis-Tipps

- **§ 44 PatG Prüfungsantrag:** Beim DPMA Prüfungsantrag binnen 7 Jahren ab Anmeldung; sonst gilt Anmeldung als zurückgenommen. EPA: Prüfungsantrag binnen 6 Monaten nach Veröffentlichung des europäischen Recherchenberichts (Art. 94 EPÜ).
- **§ 45 PatG Bescheid:** Prüfungsbescheid mit Frist (idR 4 Monate, verlängerbar); auf Bescheid nicht antworten = Zurückweisung (§ 48 PatG).
- **Neuheit § 3 PatG / Art. 54 EPÜ:** Eine Entgegenhaltung muss alle Merkmale UNMITTELBAR UND EINDEUTIG offenbaren. Bei Implizität sehr enger Maßstab.
- **Erfinderische Tätigkeit § 4 PatG / Art. 56 EPÜ:** EPA-Problem-Lösung-Ansatz (Problem-Solution Approach): nächstliegender Stand der Technik, technisches Problem, Lösung naheliegend?
- **Klarheit Art. 84 EPÜ:** Klarheit kann im EPA-Verfahren als Beanstandung kommen; im DE-Verfahren § 34 PatG.
- **Anspruchsänderung:** Stütze in ursprünglicher Offenbarung lückenlos belegen (Seite, Zeile, Anspruch); intermediate generalisation ist Hauptangriffspunkt im Einspruch.
- **Anschlussstrategie:** Teilanmeldung § 39 PatG / Art. 76 EPÜ bei breitem Schutz; Beschränkung § 64 PatG; PCT-Eintritt § 184c PatG.
- **Praxisreaktion:** Auch bei argumentativer Erwiderung Hilfsantrag mit beschränktem Anspruch nachreichen (Rückzugsposition).
- Falle: Stand-der-Technik-Dokumente aus dem PCT-Recherchebericht ignorieren — die kommen im Erteilungsverfahren häufig zurück.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
