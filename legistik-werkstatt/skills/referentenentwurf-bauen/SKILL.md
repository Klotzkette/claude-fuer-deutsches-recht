---
name: referentenentwurf-bauen
description: "Vollstaendigen Referentenentwurf des Bundes oder Landes aufbauen. Anwendungsfall legistischer Auftrag ist aufgenommen Normebene ist bestimmt Entwurfstext und Begruendung muessen nach HdR erstellt werden. Format HdR Deckblatt Vorblatt A Problem und Ziel B Loesung C Alternativen D Haushalt E Erfuellungsaufwand F Kosten G Folgen H Gleichstellung. Entwurfstext Artikel Paragrafen Strukturen Definition Hauptregel Ausnahmen Sanktionen. GGO- und HdR-Pruefliste. Output Volltext-Entwurf bereit zur Ressortabstimmung. Anschluss begruendung-allgemein-und-besonders synopse-erstellen."
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

## Aktuelle Rechtsprechung & Leitsätze

- BVerfG, Urt. v. 14.07.1959 — 2 BvF 1/58, BVerfGE 10, 20 Rn. 35 — Referentenentwurf als Ausdruck der Gesetzgebungs-Initiative; GGO-Format als Garant der Transparenz und parlamentarischen Kontrolle
- BVerwG, Urt. v. 23.03.2016 — 6 C 14.15, NVwZ 2016, 943 — Ressortabstimmungs-Pflicht nach GGO ist formell; Verletzung fuehrt nicht zur Nichtigkeit aber kann parlamentarische Kontrolle beeintraechtigen; GGO als Innenrecht der Bundesregierung
- BVerfG, Beschl. v. 14.03.2017 — 2 BvR 157/12, BVerfGE 145, 106 Rn. 60 — Aenderungsbefehle im Referentenentwurf muessen praezise sein; unpraezise Aenderungen fuehren zu Auslegungsproblemen; Normklarheit verlangt klare Aenderungs-Formulierungen (HdR-Standard)

## Zentrale Normen (Paragrafenkette)

§§ 40-62 GGO (Referentenentwurf, Ressortabstimmung) — Art. 76 Abs. 1 GG (Einbringungsrecht Bundesregierung) — §§ 1-10 HdR (Handbuch der Rechtsfoermlichkeit, Aenderungsbefehle) — Art. 80 Abs. 1 Satz 3 GG (Citatum in Verordnungen)

## Kommentarliteratur

- Schneider, Gesetzgebung, 3. Aufl. 2002, §§ 10-15 Rn. 1 ff. (Referentenentwurf-Format, Artikelstruktur, Aenderungsbefehle)
- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020, § 21 Rn. 5 ff. (Gesetzgebungsverfahren Bundesebene, GGO)

## Ausgabe

Markdown-Datei mit dem kompletten Entwurfstext, bereit für Ressortabstimmung.

## Anschluss

- `begruendung-allgemein-und-besonders`
- `synopse-erstellen`
- `xml-paralleldarstellung`
- `dokumente-rendern-docx-pdf` (am Ende, erzeugt lieferfertiges DOCX und PDF im offiziellen HdR-Layout)
