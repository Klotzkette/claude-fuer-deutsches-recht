---
name: stand-technik-patr2-anmeldeverfahren
description: "Stand Technik Patr2 Anmeldeverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Stand Technik Patr2 Anmeldeverfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Stand Technik Patr2 Anmeldeverfahren** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stand-der-technik-recherche-workflow` | Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin. |
| `patr2-anmeldeverfahren-bauleiter` | Bauleiter Patentanmeldeverfahren DPMA und EPA: Pruefverfahren, Einspruch, Beschwerde. Pruefraster fuer Erfinder und Patentanwalt. |
| `rechtsabteilung-upc-eilverfahren-und-deutsche-parallelstrategie` | Rechtsabteilungs-Fachmodul für UPC-Eilverfahren und deutsche Parallelstrategie: PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Stand Technik Patr2 Anmeldeverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stand-der-technik-recherche-workflow`

**Fokus:** Plant eine Stand-der-Technik-Recherche: Suchbegriffe, CPC/IPC-Klassen, Datenbanken, Suchstrings, Trefferbewertung und Übergabe an das Patentrecherche-Plugin.

# Stand-der-Technik-Recherche — Workflow

## Wann nutzen?

- vor eigener Anmeldung.
- zur Prüfung eines Anspruchsentwurfs.
- nach Abmahnung oder Prüfungsbescheid.
- für Einspruch/Nichtigkeitsangriff.
- für Investor-/FTO-Vorrecherche.

## Rechercheauftrag erzeugen

1. Erfindung in Merkmale und technische Wirkung zerlegen.
2. Deutsche und englische Begriffe bilden.
3. Oberbegriffe, Synonyme, Herstellerjargon und Funktionsbegriffe ergänzen.
4. CPC/IPC-Kandidaten bestimmen.
5. Datenbanken und Länder auswählen.
6. Suchstrings dokumentieren.
7. Treffer in Clustern bewerten: hoch, mittel, niedrig, nur Kontext.

## Übergabe an `patentrecherche`

Wenn konkrete Datenbankrecherche nötig ist, schlage vor:

- `patentrecherche/klassifikation-cpc-ipc`
- `patentrecherche/agentische-datenbank-recherche`
- `patentrecherche/stand-der-technik-recherche`
- `patentrecherche/recherchebericht-erstellen`

## Output

- Suchprofil.
- Suchstrings.
- Datenbankplan.
- Trefferbewertungsschema.
- Dokumentationsvorlage für spätere Nachvollziehbarkeit.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `patr2-anmeldeverfahren-bauleiter`

**Fokus:** Bauleiter Patentanmeldeverfahren DPMA und EPA: Pruefverfahren, Einspruch, Beschwerde. Pruefraster fuer Erfinder und Patentanwalt.

# PatR2: Anmeldeverfahren

## Spezialwissen: PatR2: Anmeldeverfahren
- **Spezialgegenstand:** PatR2: Anmeldeverfahren / patr2 anmeldeverfahren bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DPMA, EPA, BGH, BVerfG.
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

## 3. `rechtsabteilung-upc-eilverfahren-und-deutsche-parallelstrategie`

**Fokus:** Rechtsabteilungs-Fachmodul für UPC-Eilverfahren und deutsche Parallelstrategie: PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption.

# Rechtsabteilung: UPC-Eilverfahren und deutsche Parallelstrategie

## Spezialkern: Rechtsabteilung: UPC-Eilverfahren und deutsche Parallelstrategie

- **Konkretes Problem:** PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen.
- **Norm-/Quellenanker:** PatG, EPÜ, UPCA/UPC-Verfahrensordnung, ArbNErfG, ZPO/Eilrechtsschutz, Lizenzvertragsrecht und FRAND/SEP-Linien.
- **Entscheidende Weiche:** Tatbestand, Dokumentenbeweis, Zuständigkeit, Frist, Rechtsfolge, Gegenargument und Eskalationsweg getrennt entscheiden; keine bloße To-do-Liste liefern.
- **Arbeitsprodukt:** Rechtsabteilungsfähige Kurzentscheidung mit Ampel, Originalbelegen, offener-Tatsachen-Liste, Formulierungsvorschlag und nächstem Owner.

## Norm- und Rechtsprechungsanker

EPÜ, EPGÜ, UPC Rules; nationale PatG-Verfahren

## Sofortprüfung

1. Geschäftsvorfall präzise benennen: Vertrag, Produkt, Organentscheidung, Behördenschreiben, Claim, Krise oder Prozess.
2. Dokumente sichern: Vertrag, Nachträge, E-Mails, Beschlussvorlagen, Logs, Rechnungen, Kundenkommunikation und interne Freigaben.
3. Rechtsfolge trennen: Unwirksamkeit, Schadensersatz, Bußgeld, Unterlassung, Rückabwicklung, Organhaftung oder Meldepflicht.
4. Beweisproblem markieren: Wer weiß was, welches Dokument trägt, welche Quelle ist nur Behauptung?
5. Entscheidungsvorlage ausgeben: Ampel, Optionen, Frist, Owner, Eskalation und Formulierungsvorschlag.

## Fachlicher Zuschnitt

PI-Antrag, Schutzschrift, Bifurcation und Forumstrategie werden abgewogen.

## Output für die Rechtsabteilung

- One-page legal memo mit Risikoampel und klarer Empfehlung.
- Belegmatrix mit Originalquelle, Datum, Verantwortlichem und Lücke.
- Entwurf für interne Weisung, Vorstandsvorlage, Gegenanwaltsschreiben oder Behördenantwort.
- Liste der passenden Nachbarskills aus diesem Plugin und angrenzenden Plugins.

## Quellenhygiene

Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei erreichbarer Quelle verwenden. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Wenn eine Fundstelle nicht live verifizierbar ist, wird sie als zu verifizieren markiert und nicht als tragender Beleg ausgegeben.
