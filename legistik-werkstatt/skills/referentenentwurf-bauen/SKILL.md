---
name: referentenentwurf-bauen
description: "Erstellt einen vollstaendigen Referentenentwurf des Bundes oder Landes. Format gemaess HdR. Deckblatt Bezeichnung Inhaltsuebersicht A Problem und Ziel B Loesung C Alternativen D Haushaltsausgaben E Erfuellungsaufwand F weitere Kosten G weitere Folgen H Gleichstellungspolitische Bedeutung. Entwurfstext mit Artikeln und Paragrafen. Strukturen bei Sachverhalten Definition Hauptregel Ausnahmen Sanktionen Uebergang. Inkrafttretensregelung. Pruefliste gegen GGO und HdR. Endet mit Volltext-Entwurf bereit zur Ressortabstimmung. Anschluss `begruendung-allgemein-und-besonders` und `synopse-erstellen`."
---

# Referentenentwurf bauen

> Das Kernformat der ministeriellen Rechtssetzung.

## Aufbau eines Referentenentwurfs

### Vorblatt

Das Vorblatt vor dem eigentlichen Entwurfstext. Sieben bis acht Abschnitte (alphabetisch in der GGO geregelt):

- **A. Problem und Ziel** - was ist das Problem, was soll erreicht werden
- **B. Lösung** - die im Entwurf gewählte Lösung in drei Sätzen
- **C. Alternativen** - welche Alternativen wurden erwogen, warum verworfen
- **D. Haushaltsausgaben ohne Erfüllungsaufwand** - was kostet es den Haushalt
- **E. Erfüllungsaufwand** - Bürger, Wirtschaft, Verwaltung (Bund / Land / Gemeinde)
- **F. Weitere Kosten** - z.B. Preiseffekte
- **G. Weitere Folgen** - oekologisch, sozial, demografisch, gleichstellungspolitisch
- **H. Befristung** und Evaluierung

### Eingangsformel

"Der Bundestag hat das folgende Gesetz beschlossen:" (bei Bundesgesetz, regulaer)
Bei zustimmungspflichtigen Gesetzen: "Der Bundestag hat mit Zustimmung des Bundesrates das folgende Gesetz beschlossen:"

### Artikel und Paragrafen

Bei Änderungsgesetzen: Artikel 1, Artikel 2, Artikel 3 ...
Pro Artikel je ein Stammgesetz, das geändert wird.
Innerhalb des Artikels:
- "Paragraf X wird wie folgt geändert:"
- "1. Absatz 2 wird wie folgt gefasst: ..."
- "2. Folgender Absatz wird angefügt: ..."

Bei Stammgesetzen (neuen Vollgesetzen): Paragraf 1, Paragraf 2 etc.

### Änderungsbefehle - Standardformulierungen

- "wird wie folgt geändert"
- "wird durch folgenden Satz ersetzt"
- "wird folgender Satz angefügt"
- "wird folgender Paragraf eingefügt"
- "wird aufgehoben"
- "wird gestrichen"
- "wird die Angabe ... durch die Angabe ... ersetzt"

### Inkrafttretensregel

Letzter Artikel. Standardformel:
"Dieses Gesetz tritt am ... in Kraft."
Oder gestaffeltes Inkrafttreten:
"Artikel 1 tritt am ... in Kraft. Artikel 2 tritt am ... in Kraft."

### Schlussformel

"Berlin, den ... Der Bundespräsident ... Die Bundeskanzlerin ... Der Bundesminister ..."

## Inhaltliche Standardstruktur eines Paragrafen

1. **Anwendungsbereich / Definition**
2. **Grundregel** (Pflicht, Erlaubnis, Verbot)
3. **Ausnahmen**
4. **Sanktionen / Rechtsfolgen** bei Verstoß (oder Verweis ins Bußgeldrecht)
5. **Verfahren** (Antrag, Bescheid, Rechtsmittel)
6. **Übergangsregelung** in eigenem Paragrafen am Ende des Stammgesetzes

## Prüfliste

- [ ] Vorblatt vollständig (alle Abschnitte A bis H)
- [ ] Eingangsformel passt zum Gesetz (Zustimmungserfordernis korrekt)
- [ ] Änderungsbefehle in Standardform
- [ ] Inkrafttreten klar geregelt
- [ ] Schlussformel passend
- [ ] HdR-Spruchregeln eingehalten (siehe `hdr-stilcheck`)
- [ ] Keine Verweisschleife (siehe `zirkelschluss-pruefen`)
- [ ] Terminologie konsistent (siehe `terminologie-konsistenz`)

## Ausgabe

Markdown-Datei mit dem kompletten Entwurfstext, bereit für Ressortabstimmung.

## Anschluss

- `begruendung-allgemein-und-besonders`
- `synopse-erstellen`
- `xml-paralleldarstellung`
- `dokumente-rendern-docx-pdf` (am Ende, erzeugt lieferfertiges DOCX und PDF im offiziellen HdR-Layout)
