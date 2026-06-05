---
name: taetigkeit-fristennotiz-agentische-datenbank
description: "Taetigkeit Fristennotiz Agentische Datenbank: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Taetigkeit Fristennotiz Agentische Datenbank

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Taetigkeit Fristennotiz Agentische Datenbank** im Plugin Patentrecherche (FTO, Validity). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-taetigkeit-fristennotiz-und-naechster-schritt` | Taetigkeit: Fristennotiz und nächster Schritt im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `agentische-datenbank-recherche` | Agentische Patentdatenbank-Recherche: Suchauftrag in natuerlicher Sprache mit Erfindungsmaterial (Anspruchsentwurf, Beschreibung, Skizzen) wird automatisch in Suchstrings für Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE und USPTO uebersetzt. Normen: § 3 PatG (Neuheit), Art. 54 EPUe, § 4 PatG (erfinderische Tätigkeit). Prüfraster: Datenbankspezifische Syntax, Patentfamilien-Deduplizierung, Trefferliste mit Veröffentlichungsnummer, Anmelder, Datum, Klassen. Output Strukturierte Trefferliste. Abgrenzung: Klassifikation vorher siehe klassifikation-cpc-ipc; Berichte siehe recherchebericht-erstellen. |
| `epo-opposition-strategie` | EPO-Einspruch (Opposition) Strategie: 9-Monatsfrist nach Erteilung, Einspruchsgruende Art. 100 EPC, schriftliches Verfahren, muendliche Verhandlung, Beschwerde Boards of Appeal. Beispieltaktiken und Erfolgsfaktoren. Mustertexte fuer Einspruchsschriftsatz. |

## Arbeitsweg

Im Plugin Patentrecherche (FTO, Validity) gilt für **Taetigkeit Fristennotiz Agentische Datenbank**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-taetigkeit-fristennotiz-und-naechster-schritt`

**Fokus:** Taetigkeit: Fristennotiz und nächster Schritt im Plugin patentrecherche; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Taetigkeit: Fristennotiz und nächster Schritt

## Spezialwissen: Taetigkeit: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Taetigkeit: Fristennotiz und nächster Schritt / taetigkeit fristennotiz und naechster schritt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO/WIPO/USPTO/DPMA sind Patentämter, INPADOC/CPC/IPC/Espacenet/DEPATISnet Recherchedatenbanken, FTO eine Arbeitsmethode — keine Rechtsquellen. Tragende Normen je nach Frage: PatG §§ 1–5 (Schutzfähigkeit, Neuheit), § 4 (erfinderische Tätigkeit), §§ 9, 10 (Schutzwirkung), §§ 34, 35, 37 (Anmeldung, Prioritäten), §§ 81 ff. (Nichtigkeit); EPÜ Art. 52–57 (Patentierbarkeit), Art. 54 (Neuheit), Art. 56 (erfinderische Tätigkeit), Art. 69 (Schutzbereich), Art. 87 ff. (Priorität); PCT Art. 1 ff.; UPCA. Quellen über DPMAregister, EPO Register, USPTO PatFT, WIPO Patentscope und WIPO Lex live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Taetigkeit** prüfen.
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

## 2. `agentische-datenbank-recherche`

**Fokus:** Agentische Patentdatenbank-Recherche: Suchauftrag in natuerlicher Sprache mit Erfindungsmaterial (Anspruchsentwurf, Beschreibung, Skizzen) wird automatisch in Suchstrings für Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE und USPTO uebersetzt. Normen: § 3 PatG (Neuheit), Art. 54 EPUe, § 4 PatG (erfinderische Tätigkeit). Prüfraster: Datenbankspezifische Syntax, Patentfamilien-Deduplizierung, Trefferliste mit Veröffentlichungsnummer, Anmelder, Datum, Klassen. Output Strukturierte Trefferliste. Abgrenzung: Klassifikation vorher siehe klassifikation-cpc-ipc; Berichte siehe recherchebericht-erstellen.

# agentische-datenbank-recherche

## Zweck

Das ist das **Master-Skill** des Plugins: Es führt agentisch durch die wichtigsten Patentdatenbanken. Während das System im Hauptfenster sichtbar durch die Datenbank navigiert, erscheint das Ergebnis strukturiert im Chat.

## Eingaben

- **Suchauftrag** in natürlicher Sprache ("Bitte recherchiere zu folgender Erfindung den Stand der Technik in Europa und USA …").
- **Erfindungsmaterial:** Erfindungsbeschreibung, Anspruchsentwurf, Datenblatt, Skizzen, Memo. **Drag-and-Drop oder Datei-Upload.**
- **Klassen** aus dem vorgelagerten Skill `klassifikation-cpc-ipc` (Hauptklasse + Nebenklassen, CPC und IPC).
- **Rechtsraum** aus dem Kaltstart-Interview oder ad hoc gewählt.
- **Recherchezweck** (Stand der Technik / Neuheit / FTO / Monitoring / Bescheid) — bestimmt die Filtersetzung.

## Datenbanken und ihre agentische Bedienung

### 1. Espacenet — `https://worldwide.espacenet.com`

- Betreiber: EPA. ~150 Millionen Patentdokumente weltweit. Volltext bei vielen Dokumenten, Maschinenübersetzung **Patent Translate** für ~30 Sprachen.
- **Smart Search** für freien Volltext: Eingabefeld oben akzeptiert kurze Fragen und ganze Sätze.
- **Advanced Search** für strukturierte Suche: Felder `txt` (Titel/Abstract), `desc` (Beschreibung), `claims`, `cpc`, `ipc`, `ti` (Titel), `ab` (Abstract), `in` (Erfinder), `pa` (Anmelder), `pn` (Publikationsnummer), `pd` (Publikationsdatum), `prd` (Prioritätsdatum), `ap` (Anmelde-Nr.). Boolesche Operatoren `AND`, `OR`, `NOT`, Wildcards `*`, Nachbarschaft `prox/distance<n>` und `prox/unit=sentence`.
- **Familien-Ansicht:** "Family list" und "INPADOC patent family" — wichtig für Dedup.
- **Classification Search:** [Espacenet CPC Browser](https://worldwide.espacenet.com/patent/cpc-browser).
- **Agentische Bedienung:** Smart Search akzeptiert natürlichsprachige Suchaufträge und ganze Texte. Drag-and-Drop des Erfindungsmaterials in das Smart-Search-Feld; das System scrollt durch die Trefferliste, öffnet Treffer in "Family list"-Ansicht, sammelt Metadaten.

### 2. Google Patents — `https://patents.google.com`

- Betreiber: Google. ~120 Millionen Patentdokumente, sehr gute Volltextsuche mit semantischer Erweiterung, Maschinenübersetzung. **Google Scholar Cross-Search** für Nicht-Patent-Literatur (Aufsätze, Konferenz-Proceedings).
- **Suche:** Suchfeld akzeptiert ganze Sätze und Anspruchstext. Filter links: Klasse (CPC), Erfinder, Anmelder, Datum, Patentamt, Sprache, Status.
- **Prior Art Finder:** Bei jedem Treffer Button "Find prior art" — automatische Vorschläge für ähnliche Dokumente.
- **Agentische Bedienung:** Suchauftrag in das Hauptsuchfeld, Filter setzen, Klassen-Filter aus dem CPC-Set, Status-Filter (Granted / Application / Expired) je nach Recherchezweck.

### 3. DPMAregister — `https://register.dpma.de`

- Betreiber: DPMA. **Rechtsstand** deutscher Patente und Gebrauchsmuster: Anmeldetag, Erteilung, Erlöschen, Einspruch, Nichtigkeit, Jahresgebühren bezahlt, Stand offen / erteilt / zurückgenommen / zurückgewiesen / erloschen / nichtig.
- **Recherche nicht stark** — DPMAregister ist die Rechtsstands-Datenbank. Volltextrecherche läuft über DEPATISnet.
- **Agentische Bedienung:** Eingabe Veröffentlichungsnummer oder Anmeldenummer, Direkt-Abruf Rechtsstand. Bei FTO und Einspruch immer DPMAregister hinzuziehen.

### 4. DEPATISnet — `https://depatisnet.dpma.de`

- Betreiber: DPMA. **Recherchedatenbank** mit weltweitem Patentdokumentenbestand (DEPATIS — Datenbankzugang in den Patentinformationszentren).
- **Klassen-Recherche** stark, **deutscher Volltext** vorhanden, Anmelder- und Erfindersuche.
- **Agentische Bedienung:** "Einsteigerrecherche" für natürlichsprachige Eingabe, "Expertenrecherche" mit IKOFAX-Syntax (Befehlsmodus). Für DE-Schwerpunkt sinnvoll.

### 5. EPO Register — `https://register.epo.org`

- Betreiber: EPA. **Rechtsstand** europäischer Patentanmeldungen und EP-Patente. Akteneinsicht teilweise öffentlich nach Veröffentlichung der Anmeldung — Rechercheberichte, Prüfungsbescheide, Antworten, Einspruchsschriften.
- **Agentische Bedienung:** Eingabe Veröffentlichungsnummer (EP …), Direkt-Abruf Rechtsstand und "All Documents". Für Einspruchsstrategie und FTO essenziell.

### 6. WIPO PATENTSCOPE — `https://patentscope.wipo.int`

- Betreiber: WIPO. **PCT-Anmeldungen** (Welt-Anmeldungen WO …), nationale Phasen, ISA-Recherchebericht.
- **Cross-Lingual Expansion:** WIPO Translate für Volltextsuche in mehreren Sprachen.
- **Agentische Bedienung:** Suchfeld für natürlichsprachige Suche, Klassenfilter, Frist-Tracker für die nationalen Phasen.

### 7. USPTO Patent Public Search — `https://ppubs.uspto.gov/pubwebapp/external.html`

- Betreiber: USPTO. **US-Patente** und Anmeldungen. PatFT und AppFT in PPUBS zusammengefasst (ab 2022). Volltext der US-Dokumente, CPC- und USPC-Klassifikation.
- **Agentische Bedienung:** Quick Lookup oder Advanced Search mit Boolescher Syntax, Felder `.TI.`, `.AB.`, `.CLM.`, `.AN.` (Assignee), `.IN.` (Inventor), `.CPC.`, `.APD.` (Filing Date).

## Ablauf

### Schritt 1: Suchauftrag normalisieren

Das System liest den natürlichsprachigen Auftrag, identifiziert:

- Welche Datenbanken sind angesprochen (alle / nur EU / nur DE / Weltreichweite)?
- Welcher Zeitraum (Anmelde- / Veröffentlichungsdatum, vor / nach Stichtag)?
- Welcher Recherchezweck?
- Welche Schlüsselbegriffe (aus dem Material extrahiert)?

### Schritt 2: Such-Strings je Datenbank bauen

Pro Datenbank ein eigener Suchstring — die Syntax unterscheidet sich:

**Espacenet (Advanced Search):**
```
((cpc=H02J3/14 OR cpc=Y02E60/00) AND (txt="lastmanagement" OR txt="demand response") AND pd>=2018)
```

**Google Patents:**
```
(lastmanagement OR demand response) (CPC=H02J3/14 OR CPC=Y02E60/00) after:2018-01-01
```

**DEPATISnet (IKOFAX):**
```
ICB=H02J3/14? UND TI=lastmanagement?
```

**USPTO PPUBS:**
```
(lastmanagement OR (demand ADJ response)).TI,AB,CLM. AND CPC/H02J3/14
```

Die Strings werden **dokumentiert** ausgegeben, damit die Recherche reproduzierbar bleibt.

### Schritt 3: Datenbanken nacheinander ansteuern

Pro Datenbank:

1. URL öffnen.
2. Suchstring eingeben oder bei Smart Search den Erfindungstext einfügen.
3. Trefferzahl notieren (Sanity Check: 5 oder 50.000 Treffer sind beide ein Problem).
4. Bei Überschwemmung: Filter setzen (Klasse, Datum, Anmelder) und Refinement bis Trefferzahl handhabbar (≤200) wird.
5. Trefferliste durchgehen — Titel, Abstract, Hauptanspruch, Klassen, Zeichnungen.
6. Treffer, die zur Erfindung passen: in die Ergebnistabelle übernehmen.

### Schritt 4: Trefferliste zusammenführen

Tabelle mit Spalten:

| Veröff.-Nr. | Anmelder | Anmeldetag (Prio) | CPC / IPC | Titel | Status | Link | Quelldatenbank |

### Schritt 5: Patentfamilien deduplizieren

Über das Skill `patentfamilien-analyse` die INPADOC-Familie jedes Treffers prüfen — wenn ein US-Patent und sein EP-Pendant denselben Prioritätstag haben, gehören sie zur selben Familie und können als ein Treffer (mit Familien-Auflistung) zusammengefasst werden.

### Schritt 6: Maschinenübersetzungen kennzeichnen

Wenn ein Treffer aus JP-, CN-, KR-, RU- oder anderen Nicht-Englisch / Nicht-Deutsch / Nicht-Französisch-Quellen stammt und nur als Maschinenübersetzung lesbar ist: explizit kennzeichnen mit `[MT]` hinter dem Titel.

### Schritt 7: Output

Strukturierte Ergebnisliste mit:

- **Suchstrings** je Datenbank
- **Trefferzahlen** je Datenbank
- **Treffertabelle** (Veröff.-Nr., Anmelder, Anmeldetag, Klassen, Titel, Status, Link, Quelldatenbank)
- **Familien-Cluster** wo dedupliziert
- **Disclaimer** (siehe unten)

## Grenzen der agentischen Recherche

- **Volltextsuche** funktioniert nicht in allen Sprachen gleich gut. JP, CN, KR sind oft nur über Klassen- und Anmelder-/Titel-Suche zuverlässig erreichbar.
- **Bezahl-Datenbanken** (PatBase, STN, Orbit, Questel) werden **nicht** agentisch bedient. Wenn die Kanzlei Zugänge hat: dort selbst recherchieren, Ergebnisse manuell zuführen.
- **Nicht-Patent-Literatur** (NPL) — Aufsätze, Konferenz-Proceedings, Dissertationen, Produkt-Datenblätter, frühere öffentliche Nutzungen. Das Plugin behandelt sie über `stand-der-technik-recherche` ergänzend, nicht innerhalb des Master-Skills.
- **Geheime ältere Anmeldungen** (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPÜ) — diese werden zwar nachträglich publiziert, sind aber bei einer Recherche kurz nach dem Anmeldetag der Mandantin noch nicht öffentlich. Klar kommunizieren, dass ein "Zwischenraum" von 18 Monaten existiert.

## Disclaimer

> **Hinweis zur Recherche.** Diese Recherche ist eine KI-gestützte Vorrecherche und keine amtliche Recherche. Vollständigkeit kann nicht garantiert werden — insbesondere bei Treffern in nicht-deutschen, nicht-englischen und nicht-französischen Sprachen, bei Treffern außerhalb der gewählten Klassen und bei Treffern, die nicht in einer der eingesehenen Datenbanken hinterlegt sind. Die Recherche muss durch eigene Nachrecherche oder durch Überprüfung der Treffer abgesichert werden.

## Übergabe

Die strukturierte Ergebnisliste geht an den passenden Folge-Skill:

- `neuheit-pruefen` — für Neuheitsbewertung
- `erfinderische-taetigkeit-pruefen` — für Problem-Solution-Approach
- `freedom-to-operate-recherche` — für FTO-Bewertung
- `recherchebericht-erstellen` — für formalen Output

## Triage-Fragen vor agentischer Datenbankrecherche

Bevor die Datenbankrecherche gestartet wird, klaere:
1. Was ist das prioritaere Rechercheziel — Neuheitspruefung, FTO oder Stand-der-Technik?
2. Sind alle relevanten Datenbanken zugaenglich (Espacenet, USPTO, Patentscope, J-PlatPat)?
3. Wurden die Schluesselbegriffe und Klassifikationen (CPC/IPC) bereits identifiziert?
4. Gibt es einen Anmeldetag — der bestimmt den massgeblichen Prioritaetszeitpunkt fuer die Neuheit?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> **EPA, Technische Beschwerdekammer, T 1090/12 (Funktionale Merkmale):** Eine Entgegenhaltung nimmt ein funktionales Merkmal vorweg, wenn sie eine Vorrichtung beschreibt, die geeignet ist, die beanspruchte Funktion zu erfuellen; die tatsaechliche Ausfuehrung der Funktion ist nicht erforderlich.

## 3. `epo-opposition-strategie`

**Fokus:** EPO-Einspruch (Opposition) Strategie: 9-Monatsfrist nach Erteilung, Einspruchsgruende Art. 100 EPC, schriftliches Verfahren, muendliche Verhandlung, Beschwerde Boards of Appeal. Beispieltaktiken und Erfolgsfaktoren. Mustertexte fuer Einspruchsschriftsatz.

# EPO-Einspruch: Strategie

## Spezialwissen: EPO-Einspruch: Strategie
- **Spezialgegenstand:** EPO-Einspruch: Strategie / epo opposition strategie. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EPO, Art. 100, EPC.
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
