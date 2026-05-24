---
name: dokumente-rendern-docx-pdf
description: "Rendert Referentenentwuerfe, Kabinettsvorlagen, Formulierungshilfen, BT-Drucksachen-Layout, Synopsen und Lesefassungen als DOCX (und optional PDF) im offiziellen Erscheinungsbild der Bundesregierung bzw. des Bundestages nach Handbuch der Rechtsfoermlichkeit (HdR). Verwendet python-docx, das mitgelieferte Stylesheet und die Vorlagen im assets-Ordner. Beachtet Schriftart, Seitenrand, Kopf- und Fusszeile, Sperrsatz fuer Ueberschriften, Artikel- und Paragraphennummerierung, Aenderungsbefehle in Kursivsatz mit Anfuehrungszeichen, A-F-Vorblattgliederung, Begruendung Teil A und Teil B, Spaltensynopsen, Nationaler Normenkontrollrat-Stellungnahme, Anschreiben des Bundeskanzlers, korrekte Fusszeile mit Drucksachennummer und Wahlperiode."
---

# Dokumente rendern - DOCX und PDF im offiziellen HdR-Layout

## Wann verwenden

Dieser Skill wird **am Ende** des Legistik-Workflows aufgerufen, wenn aus den strukturierten Markdown-Bausteinen der vorgelagerten Skills (Auftrag, Normentext, Begründung, Synopse) ein **lieferfähiges Dokument** im offiziellen Erscheinungsbild erstellt werden soll.

Drei Hauptformate:

1. **Referentenentwurf** (ministeriell, serifenlos Arial 11pt, "der Bundesregierung" im Kopf, Bearbeitungsstand-Hinweis, A-F-Vorblatt, Artikelgesetz, Begründung Teil A und B)
2. **Gesetzesentwurf der Bundesregierung** (BT-Drucksachen-Look, Times New Roman 11pt, "Drucksache XX/YYYY", "Deutscher Bundestag - XX. Wahlperiode", Sperrsatz-Überschriften, Anschreiben des Bundeskanzlers)
3. **Formulierungshilfe der Bundesregierung** (kuerzer, ohne Drucksachen-Mantel, eingerueckter Änderungstext)

Plus Hilfsformate:

4. **Spaltensynopse** dreispaltig (geltend / Änderung / Begründung)
5. **Lesefassung konsolidiert** (Artikelgesetz nach Inkrafttreten)
6. **Kabinettsmappe-Deckblatt**

## Vorgehen

1. **Eingangsbausteine sammeln**: Die strukturierten Markdown-Dateien aus den vorgelagerten Skills (`vorblatt.md`, `gesetzestext.md`, `begruendung-allgemein.md`, `begruendung-besonders.md`, `synopse.csv`) müssen vorliegen.
2. **Format wählen** (siehe oben 1-6) abhängig vom Adressaten:
   - federführendes Ressort intern -> Referentenentwurf
   - Kabinett -> Kabinettsmappe + Referentenentwurf
   - Bundestag aus Mitte des Hauses -> Formulierungshilfe
   - Bundestag von Bundesregierung -> BT-Drucksachen-Layout
3. **Skript aufrufen**: `python3 skills/dokumente-rendern-docx-pdf/assets/render.py --format referentenentwurf --eingabe /pfad/zum/projekt/ --ausgabe /pfad/zum/projekt/output/`
4. **Visuelle Prüfung** des DOCX: Schriftart, Sperrsatz, Änderungsbefehle kursiv, Vorblatt-Gliederung, Kopf-/Fußzeile.
5. **Optional PDF**: Konvertierung via LibreOffice headless (Skript läuft, wenn `soffice` verfügbar) oder Pandoc.

## Layout-Eckdaten nach Handbuch der Rechtsförmlichkeit

### Referentenentwurf (ministerieller Hausstil)

- Schrift: **Arial 11pt** (serifenlos)
- Zeilenabstand 1.15
- Rand: links 2.5 cm, rechts 2.0 cm, oben/unten 2.0 cm
- Seitenkopf: zentriert `- N -` (Seitennummer in Gedankenstrichen)
- Fußzeile: leer oder Bearbeitungsstand-Datum
- Kopfzeile Seite 1: rechtsbuendig "Bearbeitungsstand: TT.MM.JJJJ HH:MM"
- Titel zentriert fett: "Referentenentwurf"
- Untertitel zentriert: "des Bundesministeriums für ..."
- Haupttitel zentriert fett: "Entwurf eines Gesetzes zur ..."
- Kurztitel in Klammern: "(Kurzbezeichnung - Abkürzung)"
- Datumsplatzhalter "Vom ..."

### BT-Drucksachen-Layout (Gesetzentwurf der Bundesregierung)

- Schrift: **Times New Roman 11pt** (Serife)
- Zeilenabstand 1.15
- Seitenkopf wechselnd (gerade/ungerade): links/rechts "Drucksache XX/YYYY" bzw. "Deutscher Bundestag - XX. Wahlperiode", Mitte `- N -`
- Sperrsatz für Hauptüberschriften: `I n h a l t s u e b e r s i c h t`
- Anschreiben Bundeskanzler in Briefkopf-Format
- Anlagen: Begründung (Anlage 1), Stellungnahme NKR (Anlage 2), Stellungnahme Bundesrat (Anlage 3), Gegenaeusserung (Anlage 4)

### Gemeinsame Strukturen

- Vorblatt: A. Problem und Ziel - B. Lösung - C. Alternativen - D. Haushaltsausgaben ohne Erfüllungsaufwand - E. Erfüllungsaufwand (E.1 Bürger - E.2 Wirtschaft - E.3 Verwaltung) - F. Weitere Kosten
- Artikelgesetz: "Artikel 1 (Änderung des XYZ-Gesetzes)" fett, Einleitungssatz mit Stammgesetz + letzte Änderung BGBl-Fundstelle
- Gliederungsebenen: 1. / 2. / 3. -> a) b) c) -> aa) bb) cc) -> aaa) bbb) ccc)
- Änderungsbefehle: Anführungszeichen kursiv: *"... wird durch ... ersetzt"*
- Absatzbezeichnung in Klammern: (1), (2), (3)
- Begründung Teil A (Allgemeiner Teil) Roemisch I-VII: I. Zielsetzung und Notwendigkeit - II. Wesentlicher Inhalt - III. Alternativen - IV. Gesetzgebungskompetenz - V. Vereinbarkeit mit EU-Recht - VI. Gesetzesfolgen - VII. Befristung und Evaluierung
- Begründung Teil B (Besonderer Teil): "Zu Artikel X" - "Zu Nummer Y" - "Zu Buchstabe Z"

## Eingabeschema

Der Eingabeordner enthält:

```
projekt/
  metadaten.yaml      # Titel, Kurztitel, Federfuehrung, Bearbeitungsstand, Drucksachennummer, Wahlperiode
  vorblatt.md         # A bis F mit den ueblichen Abschnitten
  gesetzestext.md     # Artikel 1 ... Artikel N (Inkrafttreten)
  begruendung-a.md    # I bis VII
  begruendung-b.md    # Zu Artikel X / Zu Nummer Y
  synopse.csv         # Spalten: geltend | aenderung | begruendung
  anlagen/            # NKR, Bundesrat, Gegenaeusserung (optional, als md)
```

## Beispielaufruf

```bash
python3 skills/dokumente-rendern-docx-pdf/assets/render.py \
  --format referentenentwurf \
  --eingabe testakten/legistik-pflichtpostfach/ \
  --ausgabe testakten/legistik-pflichtpostfach/output/
```

Ausgabe: `Referentenentwurf-Pflichtpostfachgesetz.docx` (und `.pdf` wenn `soffice` installiert).

## Qualitätsprüfung vor Abgabe

- Schriftart und -groesse korrekt
- Sperrsatz nur für Hauptüberschriften ("Inhaltsübersicht", "Begründung")
- Änderungsbefehle durchgaengig kursiv und in Anführungszeichen
- Vorblatt vollständig A-F
- Begründung Teil A vollständig I-VII
- Kopf-/Fußzeile auf jeder Seite
- Keine überschießenden Begriffe in der Sache (Goldplating siehe Skill goldplating-vermeiden)
- Keine Mehrwert-Steuer-Komma-Zahlen im Fliesstext - immer Punkt verwenden oder ausschreiben

## Verwandte Skills

- `referentenentwurf-bauen` - liefert die Markdown-Bausteine für das Vorblatt und den Artikeltext
- `gesetzesentwurf-kabinett` - liefert die Kabinettsmappe als zusätzliches Deckblatt
- `formulierungshilfe-bauen` - liefert die Kurzform für die Mitte des Hauses
- `synopse-erstellen` - liefert die dreispaltige CSV für die Synopse
- `begruendung-allgemein-und-besonders` - liefert die Begründung Teil A und Teil B
