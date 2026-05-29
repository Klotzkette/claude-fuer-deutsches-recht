---
name: recherchebericht-erstellen
description: "Formaler Recherchebericht für den Mandanten oder die Akte. Bringt Auftrag Methodik durchsuchte Datenbanken verwendete Suchstrings Klassen Schlagworte Zeitraum Trefferzahlen Treffertabelle und Bewertungen aus Skills neuheit-prüfen erfinderische-tätigkeit-prüfen freedom-to-operate-recherche und patentfamilien-analyse zusammen. Strukturierter Aufbau mit Deckblatt Auftragsbeschreibung Methodik Trefferdokumentation Bewertung Empfehlung Anhang (Suchstrings Klassen Quellenliste). Disclaimer Vorrecherche keine amtliche Recherche mehrfach im Bericht. Output als Markdown-Dokument das die Patentanwaeltin in Word oder PDF weiterverarbeiten kann."
---

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

Mandant:        [Mandantenname]
Aktenzeichen:   [Aktenzeichen]
Recherchezweck: [Stand der Technik / Neuheit / FTO / Monitoring / Bescheidantwort]
Stichtag:       [Datum des Berichts]
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
