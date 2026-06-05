---
name: recherche-strategie-tools-marktuebersicht
description: "Recherche Strategie Tools Marktuebersicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Recherche Strategie Tools Marktuebersicht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Recherche Strategie Tools Marktuebersicht** im Plugin Patentrecherche (FTO, Validity). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `recherche-strategie-keywords-und-klassen` | Recherche-Strategie Keywords und Klassifikationen: Boolesche Operatoren, Wildcards, Stopp-Woerter, Variantenpruefung, Trunkierung, Synonyme. CPC und IPC mit Co-Klassen, Klassenwanderung Updates. Strukturierte Vorbereitung von Suchprofilen. Mustertabelle. |
| `recherche-tools-marktuebersicht` | Marktuebersicht Recherche-Tools: kostenlose Quellen (Espacenet, DEPATIS, Google Patents, Lens, USPTO PatFT/AppFT, J-PlatPat), kostenpflichtige (Derwent, Orbit, PatBase, Minesoft, IPCheckUp, Patsnap). Pro Tool: Staerken, Schwaechen, Lizenzmodell, Eignung. |
| `recherchebericht-erstellen` | Formaler Recherchebericht für den Mandanten oder die Akte. Bringt Auftrag Methodik durchsuchte Datenbanken verwendete Suchstrings Klassen Schlagworte Zeitraum Trefferzahlen Treffertabelle und Bewertungen aus Skills neuheit-prüfen erfinderische-tätigkeit-prüfen freedom-to-operate-recherche und patentfamilien-analyse zusammen. Strukturierter Aufbau mit Deckblatt Auftragsbeschreibung Methodik Trefferdokumentation Bewertung Empfehlung Anhang (Suchstrings Klassen Quellenliste). Disclaimer Vorrecherche keine amtliche Recherche mehrfach im Bericht. Output als Markdown-Dokument das die Patentanwaeltin in Word oder PDF weiterverarbeiten kann. |

## Arbeitsweg

Im Plugin Patentrecherche (FTO, Validity) gilt für **Recherche Strategie Tools Marktuebersicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `recherche-strategie-keywords-und-klassen`

**Fokus:** Recherche-Strategie Keywords und Klassifikationen: Boolesche Operatoren, Wildcards, Stopp-Woerter, Variantenpruefung, Trunkierung, Synonyme. CPC und IPC mit Co-Klassen, Klassenwanderung Updates. Strukturierte Vorbereitung von Suchprofilen. Mustertabelle.

# Recherche-Strategie

## Spezialwissen: Recherche-Strategie
- **Spezialgegenstand:** Recherche-Strategie / recherche strategie keywords und klassen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** CPC, IPC.
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

## 2. `recherche-tools-marktuebersicht`

**Fokus:** Marktuebersicht Recherche-Tools: kostenlose Quellen (Espacenet, DEPATIS, Google Patents, Lens, USPTO PatFT/AppFT, J-PlatPat), kostenpflichtige (Derwent, Orbit, PatBase, Minesoft, IPCheckUp, Patsnap). Pro Tool: Staerken, Schwaechen, Lizenzmodell, Eignung.

# Recherche-Tools: Marktuebersicht

## Spezialwissen: Recherche-Tools: Marktuebersicht
- **Spezialgegenstand:** Recherche-Tools: Marktuebersicht / recherche tools marktuebersicht. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DEPATIS, USPTO.
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

## 3. `recherchebericht-erstellen`

**Fokus:** Formaler Recherchebericht für den Mandanten oder die Akte. Bringt Auftrag Methodik durchsuchte Datenbanken verwendete Suchstrings Klassen Schlagworte Zeitraum Trefferzahlen Treffertabelle und Bewertungen aus Skills neuheit-prüfen erfinderische-tätigkeit-prüfen freedom-to-operate-recherche und patentfamilien-analyse zusammen. Strukturierter Aufbau mit Deckblatt Auftragsbeschreibung Methodik Trefferdokumentation Bewertung Empfehlung Anhang (Suchstrings Klassen Quellenliste). Disclaimer Vorrecherche keine amtliche Recherche mehrfach im Bericht. Output als Markdown-Dokument das die Patentanwaeltin in Word oder PDF weiterverarbeiten kann.

# recherchebericht-erstellen

## Zweck

Erzeugt das **formale Ausgabedokument** der Recherche. Wird je nach Mandat:

- Dem Mandanten als Recherchebericht ausgehändigt
- In die Mandatsakte gelegt
- Als Anlage zu einem Patentanwaltsgutachten verwendet
- Bei FTO-Recherchen als Risiko-Memorandum dokumentiert

## Aufbau

### 1. Deckblatt

```
Recherchebericht
================

Mandant: [Mandantenname]
Aktenzeichen: [Aktenzeichen]
Recherchezweck: [Stand der Technik / Neuheit / FTO / Monitoring / Bescheidantwort]
Stichtag: [Datum des Berichts]
Erstellt durch: [Patentanwältin / Patentanwalt]
 [Kanzlei]
```

### 2. Auftragsbeschreibung

- Mandant
- Erfindung / Produkt / Verfahren (in einem Absatz)
- Recherchezweck (in einem Absatz)
- Rechtsraum / Zielmarkt
- Stichtag

### 3. Methodik

- Welche Datenbanken durchsucht wurden (Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE, USPTO)
- Welche Klassen (CPC, IPC) — über `klassifikation-cpc-ipc`
- Welche Schlagwörter
- Welcher Zeitraum (Anmelde- / Veröffentlichungstag)
- Sprache der Recherche (DE, EN, FR; Maschinenübersetzungen für JP, CN, KR)
- Welche Bezahl-Datenbanken **nicht** mit eingeschlossen wurden
- Welche Nicht-Patent-Literatur einbezogen wurde (Scholar, Lens, arXiv, etc.)

### 4. Trefferdokumentation

Strukturierte Treffertabelle mit Spalten: Veröff.-Nr., Anmelder, Anmeldetag, Klasse, Titel, Status, Recherchezeichen (X/Y/A/P/E) oder Ampel (rot/gelb/grün), Pinpoint, Link.

Pro besonders relevantem Treffer ein **Dossier** auf einer halben Seite mit Pinpoint und Merkmals-Tabelle (übernommen aus `neuheit-pruefen` / `freedom-to-operate-recherche`).

### 5. Patentfamilien

Wenn relevante Treffer Familienmitglieder haben: Familientabelle pro Treffer mit Validierungsstaaten und Rechtsstand. Übernommen aus `patentfamilien-analyse` und `rechtsstand-pruefen`.

### 6. Bewertung

- Bei **Stand-der-Technik-Recherche:** Wie viele X / Y / A / P / E? Welche Beschränkung des Anspruchs ist erforderlich, um Neuheit und erfinderische Tätigkeit zu wahren?
- Bei **Neuheit-Prüfung:** Pro relevantem Anspruch — neu oder nicht neu?
- Bei **Erfinderische-Tätigkeit-Prüfung:** Problem-Solution-Approach, Ergebnis pro Anspruch.
- Bei **FTO-Recherche:** Wie viele Rot / Gelb / Grün? Welche Schutzrechte blockieren den Markteintritt? Wo besteht Handlungsbedarf?
- Bei **Bescheid-Vorbereitung:** Entwurf der Eingabe als Anhang.

### 7. Empfehlung

In drei bis fünf Sätzen — was sollte die Mandantin tun?

- Anmeldung wie geplant einreichen
- Anmeldung mit beschränktem Anspruch einreichen
- Anmeldung nicht einreichen (Gebrauchsmuster prüfen, Geheimhaltung erwägen)
- Markteintritt frei
- Markteintritt nur mit Umgehungsdesign / Lizenz
- Einspruch einlegen — Frist [Datum]
- Nichtigkeitsklage erwägen
- Konkurrenten weiter überwachen
- Weitere Recherche im Bezahl-Datenbankenkreis erforderlich

### 8. Disclaimer (prominent)

```
HINWEIS ZUR RECHERCHE

Diese Patentrecherche ist eine KI-gestützte Vorrecherche und KEINE
amtliche Recherche im Sinne einer DPMA- oder EPA-Recherche. Vollständigkeit
kann nicht garantiert werden, insbesondere:

- Treffer in nicht durchsuchten Sprachen (JP, CN, KR, RU usw.) können verfehlt werden;
- Geheime ältere Anmeldungen (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPUe) sind erst
 18 Monate nach Prioritaetstag öffentlich;
- Bezahl-Datenbanken (PatBase, STN, Orbit, Questel u. a.) sind in diese Recherche
 nicht eingeflossen, sofern nicht ausdrücklich vermerkt;
- Nicht-Patent-Literatur ist nur über Standard-Schnittstellen (Google Scholar,
 Lens.org, arXiv, PubMed) erfasst.

Die finale Bewertung der Patentierbarkeit, der Verletzungsfreiheit und des Rechts-
stands muss durch eigenständige Prüfung der Patentanwältin / des Patentanwalts
abgesichert werden. Dieser Bericht ersetzt nicht die anwaltliche Prüfung und ist
keine Rechtsberatung gegenüber dem Endmandanten außerhalb der zuständigen Kanzlei.
```

### 9. Anhang

- Liste der Suchstrings pro Datenbank
- CPC- und IPC-Klassen mit Definitionen
- Quellenliste mit Datum des Abrufs
- Glossar (X/Y/A/P/E, INPADOC, Pinpoint)

## Ablauf

### Schritt 1: Sammelt Inputs

Aus den Vorgänger-Skills:

- `patentrecherche-kaltstart-interview` → Kanzlei, Mandant
- `klassifikation-cpc-ipc` → Klassen
- `agentische-datenbank-recherche` → Trefferlisten und Suchstrings
- `stand-der-technik-recherche` → X/Y/A/P/E-Bewertungen
- `neuheit-pruefen` → Merkmalsanalyse
- `erfinderische-taetigkeit-pruefen` → PSA-Argumentation
- `freedom-to-operate-recherche` → Ampelbewertungen
- `patentfamilien-analyse` → Familientabellen
- `rechtsstand-pruefen` → Rechtsstandsdaten

### Schritt 2: Erzeugt Markdown-Dokument

Strukturiert wie oben, mit allen Tabellen und Dossiers.

### Schritt 3: Disclaimer-Block prüfen

Disclaimer **dreimal** im Bericht (Deckblatt-Vermerk, Methodik, eigener Abschnitt 8) — das Plugin lässt ihn nicht weg.

### Schritt 4: Output-Format

Markdown-Datei `recherchebericht_<aktenzeichen>_<datum>.md` im Arbeitsverzeichnis. Patentanwältin kann sie in Word oder PDF konvertieren — die Konvertierung erfolgt durch externes Werkzeug (z. B. Pandoc, MS Word "Aus Markdown öffnen").

## Hinweise

- **Verständlich für den Mandanten.** Wenn der Mandant kein Patentanwalt ist: Erläuterungstexte zu X/Y/A, Anspruchsmerkmalen, Schutzbereich.
- **Vertraulichkeit.** Berichte enthalten Mandanten-Erfindung — Verschwiegenheitspflicht nach § 39a PAO und § 203 StGB ist zu wahren. Berichte nur über zugelassene Kanäle ausliefern.
- **Versionierung.** Bei Folgerecherchen das Aktenzeichen und Stichtag im Dateinamen variieren — nicht überschreiben.

## Disclaimer

> Wie im Bericht selbst.

## Triage-Fragen vor Recherchebericht-Erstellung

Bevor der Bericht formatiert wird, klaere:
1. Sind alle Rechercheergeb-nisse aus den vorangegangenen Skills (neuheit-pruefen, erfinderische-taetigkeit, FTO) vollstaendig?
2. Ist der Adressat des Berichts identifiziert (Mandant, Patentanwalt, Gericht)?
3. Sind alle drei Disclaimer-Bloecke im Bericht enthalten (Deckblatt, Methodik, Abschluss)?
4. Ist der Stichtag der Recherche im Dateinamen und im Bericht korrekt vermerkt?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **DPMA, Bekanntmachung 2022 (Verwertungsberichte):** Im Zusammenhang mit Patentbewertungen und Recherchen fuer IP-Portfoliokauf erwartet das DPMA vollstaendige Angaben ueber bekannte Wettbewerber-Rechte; ein Bericht, der bekannte Kollisionspunkte nicht nennt, kann als unvollstaendige Auskunft und Berufspflichtverletzung angesehen werden.
