---
name: agentische-datenbank-recherche
description: "Agentische Patentdatenbank-Recherche: Suchauftrag in natuerlicher Sprache mit Erfindungsmaterial (Anspruchsentwurf, Beschreibung, Skizzen) wird automatisch in Suchstrings für Espacenet, Google Patents, DPMAregister, DEPATISnet, EPO Register, WIPO PATENTSCOPE und USPTO uebersetzt. Normen: § 3 PatG (Neuheit), Art. 54 EPUe, § 4 PatG (erfinderische Tätigkeit). Prüfraster: Datenbankspezifische Syntax, Patentfamilien-Deduplizierung, Trefferliste mit Veröffentlichungsnummer, Anmelder, Datum, Klassen. Output Strukturierte Trefferliste. Abgrenzung: Klassifikation vorher siehe klassifikation-cpc-ipc; Berichte siehe recherchebericht-erstellen."
---

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
