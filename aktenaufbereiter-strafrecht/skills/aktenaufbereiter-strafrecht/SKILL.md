---
name: aktenaufbereiter-strafrecht
description: Strukturierte Aufbereitung strafrechtlicher Akten fuer die Verteidigung. Erzeugt sechs Uebersichten — Aktenvorblatt mit Blattangaben; Personenverzeichnis mit Rolle und Erstnennung; Tatkomplex- und Vorwurfsverzeichnis mit einschlaegigen Normen; Beziehungsverzeichnis der Beteiligten; Chronologie aller relevanten Ereignisse; Fristen- und Terminverzeichnis. Alle Tabellen Excel-faehig mit Band- und Blattangabe als Fundstelle. Fortlaufend ergaenzbar bei Aktennachlieferungen mit Markierung der Neuzugaenge. Erkennt Widersprueche zwischen Vernehmungen und Kontounterlagen. Nimmt KEINE rechtliche Bewertung vor. OCR auf Scans ist Pflicht. Geeignet fuer Wirtschaftsstrafverfahren BtM-Verfahren Vermoegensdelikte und komplexe Strafverfahren.
---

# Aktenaufbereiter Strafrecht

## Leitidee

Quod non est in actis non est in mundo. Wer die Akte nicht
beherrscht beherrscht den Fall nicht. Strafakten umfassen hunderte
bis zehntausende Seiten. Der Skill übernimmt die mechanische
Erfassungs- und Strukturierungsarbeit — die manchmal wissenschaftliche
Mitarbeiter oder Referendare leisten — und liefert Tabellen die in
Excel weiterverwendbar sind.

Der Skill ersetzt NICHT die eigene Aktenlektüre. Er ist kein
agentisches System das selbständig verteidigt. Er ist ein Werkzeug
das die mechanische Vorarbeit beschleunigt und dabei Widersprüche
und Lücken sichtbar macht die beim Durchblaettern leicht übersehen
werden.

## Inputs

- Digitalisierte Aktenbestandteile (PDF mit OCR Word maschinenlesbar)
- Optional: vorhandene Excel-Tabelle zur Fortschreibung
- Optional: Anklageschrift gesondert (für Abgleich)
- Optional: Vorlage-Excel mit Wunsch-Spalten

## OCR-Pflicht

Gescannte Dokumente OHNE Texterkennung werden nicht verlaesslich
verarbeitet. Der Skill weist darauf hin. Manche Systeme lesen
auch ohne OCR aus Bildern — Ergebnisse sind aber deutlich
fehleranfälliger und nicht empfehlenswert.

## Sechs Übersichten

### 1. Aktenvorblatt und Inhaltsverzeichnis

Spalten: Nr — Blatt — Datum — Vorgang — Essentialia — Anmerkung
Kanzlei — Anmerkung Mandant.

Blattangaben müssen mit der tatsächlichen Paginierung
übereinstimmen. Bei fehlender Paginierung wird so gut wie möglich
gearbeitet und die Lücke markiert. Unvollständige Paginierung ist
besser als gar keine.

### 2. Personenverzeichnis

Spalten: Nr — Name (Nachname Vorname) — Adresse — Prozessrolle —
Blatt der Erstnennung — Anmerkung Kanzlei — Anmerkung Mandant.

Prozessrollen: Beschuldigter Zeuge Geschaedigter Sachverständiger
Polizeibeamter Richter Staatsanwalt Verteidiger Nebenkläger
sonstiger Beteiligter.

Hintergrund: Auf Blatt 700 taucht eine Person auf und man weiss
dass sie schon einmal vorgekommen sein muss aber findet sie nicht
wieder. Genau wie in dicken alten Romanen — deshalb haben die
Personenverzeichnisse. Und deshalb braucht man sie auch für
Strafakten.

### 3. Tatkomplex- und Vorwurfsverzeichnis

Spalten: Tatkomplex (I II III ...) — Tatvorwurf und Norm —
Tatzeitraum von bis — Betroffene Personen (Beschuldigte
Geschaedigte) — Beweismittel (Urkunden Zeugen
Sachverständigengutachten).

Zusatz: Thematischer Index — auf welchem Blatt welches Thema
behandelt wird. Beispiel: Komplex Kontofaelschung Bl. 125-189
Band I und Bl. 45-72 Band III. Zeugenaussagen zum Untreue-Vorwurf
Bl. 312 Bl. 455 Bl. 678-690.

### 4. Beziehungsverzeichnis

Spalten: Person 1 — Beziehung — Person 2 — Fundstelle (Band
Blatt) — Bemerkungen.

Beziehungstypen: Verwandtschaft Geschäftspartner Kontakt per Chat
Telefonat E-Mail Mitarbeiter Vorgesetzter. Auf Wunsch
Netzwerkdiagramm als Graph — sonst bleibt es bei der Tabelle.

### 5. Chronologie

Spalten: Nr — Datum — Blatt — Beteiligte — Vorgang — Anmerkung
Kanzlei — Anmerkung Mandant.

Lückenlos chronologisch geordnet. Zentrales Arbeitsinstrument
für Hauptverhandlung Mandantengespräch und Verständigung mit
der Staatsanwaltschaft.

### 6. Fristen- und Terminverzeichnis

Spalten: Art (HV-Termin Frist Adresse) — Datum oder Frist —
Beschreibung — Fundstelle (Band Blatt).

Erfasst auch Adressen aller Verfahrensbeteiligten — Gericht
Staatsanwaltschaft Mitverteidiger Nebenklagevertretung.

## Methodik

1. Aktenbestandteile inventarisieren — pro Datei Typ Umfang
   OCR-Status
2. Blatt-für-Blatt-Extraktion mit Quellenverweis
3. Querverweis zwischen den sechs Tabellen — Personen aus
   Personenverzeichnis müssen in Beziehung und Chronologie
   konsistent erscheinen
4. Widerspruchsprüfung — abweichende Datums- oder Sachangaben
   in verschiedenen Vernehmungen werden BEIDE dokumentiert mit
   Fundstelle
5. Lückenprüfung — in der Anklageschrift genannte Zeugen die in
   den Vernehmungsprotokollen fehlen werden markiert
6. Ausgabe als Excel-fähige Tabellen

## Anti-Halluzinations-Regel

- Nur Informationen die in der Akte stehen
- Keine eigenen Vermutungen oder Wertungen
- Jede Information mit Band und Blattangabe wenn identifizierbar
- Widersprüche BEIDE dokumentieren mit Fundstelle
- Unsicherheiten kennzeichnen — Beispiel `[Datum unklar]`
  `[Name nur teilweise lesbar]`
- KEINE rechtliche Bewertung der Vorwuerfe
- KEINE Einschätzung der Erfolgsaussichten der Verteidigung

## Output-Dateien

- `Aktenvorblatt_<Aktenzeichen>.xlsx`
- `Personenverzeichnis_<Aktenzeichen>.xlsx`
- `Tatkomplexe_<Aktenzeichen>.xlsx`
- `Beziehungen_<Aktenzeichen>.xlsx`
- `Chronologie_<Aktenzeichen>.xlsx`
- `Fristen_<Aktenzeichen>.xlsx`

Alternativ ein Sammel-Workbook `Akte_<Aktenzeichen>.xlsx` mit
sechs Tabellenblättern.

Auf Wunsch zusätzlich Markdown-Version der Tabellen für offline
Nutzung bei Gerichtsterminen ohne stabilen Internet-Zugang.

## Fortlaufende Aktualisierung

Bei Nachlieferungen ergänzt der Skill die bestehende Tabelle.
Neuzugänge werden in einer Spalte `Status` mit `NEU` markiert
oder in einer separaten Spalte `Eingang` mit Datum versehen.
Bisherige Einträge werden nicht überschrieben.

Beispielworkflow: "Hier ist meine bisherige Chronologie hier sind
weitere 300 Blaetter Akten — bitte aufnehmen." Der Skill ergänzt
und markiert.

## Spezialisierungen

### Wirtschaftsstrafverfahren

Zusatztabellen: Finanzstroeme Kontoverbindungen
Transaktionschronologien Gesellschaftsverflechtungen.

### BtM-Verfahren

Zusatztabellen: TKUe-Protokolle Observationsberichte Chatverläufe
mit Datum Teilnehmern Inhalt-Zusammenfassung.

### Beweismittelverzeichnis

Separate Tabelle: Beweismittel — Art — Fundstelle in Akte —
Erhebungsgrundlage — Bewertung der Verwertbarkeit. Bewertung
strikt sachlich keine prozesstaktische Empfehlung.

### Anklageschrift-Abgleich

Gegenüberstellung: in der Anklageschrift behauptete Tatsache —
Aktenbefund — Diskrepanz. Markiert wo die Anklage nicht durch die
Akte gedeckt ist.

### Vernehmungsübersicht

Tabelle aller Vernehmungen: Datum — vernehmender Beamter —
vernommene Person — wesentliche Aussageinhalte — Widersprüche
zu früheren Aussagen — Fundstelle.

## Beispielformulierungen

- "Erstelle alle sechs Übersichten zu dieser Strafakte. OCR
  ist gemacht."
- "Hier ist meine bisherige Chronologie und 400 neue Blaetter.
  Bitte aufnehmen mit Markierung der Neuzugänge."
- "Erzeuge zusätzlich das Wirtschaftsstraf-Set mit
  Finanzstroemen und Kontoverbindungen."
- "Gleiche die Anklageschrift mit dem Aktenbefund ab und zeige
  Diskrepanzen."
- "Vernehmungsübersicht mit Widersprüchen zwischen den
  einzelnen Aussagen des Zeugen Mueller."

## Berufsrecht und Datenschutz

Strafakten enthalten hochsensible personenbezogene Daten. Nutzung
nur mit KI-Systemen die DSGVO § 203 StGB und §§ 43a 43e BRAO
vertraglich zusichern und tatsächlich gewährleisten. Verlage
und Gerichtsentscheidungen — § 5 UrhG — genießen keinen
urheberrechtlichen Schutz; rechtswissenschaftliche Literatur der
Verlage hingegen schon — Lizenzsituation prüfen.

## Pragmatismus

Der Skill ist ein Quick Win. Er ersetzt nicht die Welt — er
beschleunigt das bisherige Verfahren. Wer Chronologien in Excel
führt führt sie weiter — nur eben schneller und vollständiger.
Wer im Mandantengespräch präzise auf Blatt 312 zugreifen können
muss findet die Stelle in Sekunden statt in Minuten.

## Werkzeug: `werkzeuge/aktenuebersicht_template.xlsx`

Vorlage für eine strukturierte Aktenübersicht mit drei Sheets:

1. **Beweismittel** — Lfd-Nr., Datum, Aktenfundstelle (Band/Blatt), Vorgang, Beweismittel, Beweisthema, Antrag/Verzicht, Status, Bemerkung. Als Excel-Tabelle formatiert (AutoFilter, Banded Rows).
2. **Fristen** — Akteneinsicht, Hauptverhandlung, Erinnerungen, Status.
3. **Lesehinweise** — Konvention zur Pflege der Aktenübersicht.

Die Vorlage ersetzt nicht die Aktenführung im Kanzleisystem, sondern strukturiert die Verteidigerarbeit beim Lesen der Ermittlungsakte.
