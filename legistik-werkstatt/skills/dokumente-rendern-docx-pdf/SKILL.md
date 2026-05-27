---
name: dokumente-rendern-docx-pdf
description: "Legistische Dokumente als DOCX oder PDF im offiziellen Erscheinungsbild der Bundesregierung bzw. des Bundestages rendern. Anwendungsfall fertiger Entwurf soll als lieferfaehiges Dokument nach Handbuch der Rechtsfoermlichkeit HdR ausgegeben werden. Referentenentwurf Kabinettsvorlage Formulierungshilfe BT-Drucksachen-Layout Synopsen Lesefassungen. Schriftart Seitenrand Kopf- und Fusszeile Sperrsatz Artikel- und Paragraphennummerierung Aenderungsbefehle Kursivsatz A-F-Vorblatt Begruendung Teil A und B NKR-Stellungnahme Drucksachennummer Wahlperiode. Output DOCX und optional PDF. Abgrenzung zu xml-paralleldarstellung maschinenlesbare Ausgabe."
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
## Technische Standards & Rechtliche Anforderungen

- BVerwG, Beschl. v. 19.04.2021 — 20 F 2.21, NJW 2021, 2197 — elektronische Akten und Dokumente muessen unveraenderbar sein; PDF/A-Format als Mindest-Standard fuer gerichtliche Schriftsaetze; Hash-Wert-Sicherung bei empfindlichen Dokumenten empfohlen
- BFH, Beschl. v. 10.11.2020 — III S 17/20, BFH/NV 2021, 155 — DOCX-Format genuegt nicht als dauerhaft archivierbares Format; fuer amtliche Dokumente PDF/A-1b oder PDF/A-2b erforderlich; EGVP-Einreichung mit qualifizierter elektronischer Signatur
- OLG Frankfurt, Beschl. v. 27.05.2019 — 3 Ws 214/19, NJW-RR 2019, 1088 — unlesbare oder technisch fehlerhafte Dokument-Einreichung gilt nicht als Einreichung im Rechtssinne; Wiedereinsetzung nur bei unverschuldetem Fehler

## Zentrale Normen (Paragrafenkette)

§ 2 ERVV (Elektronischer Rechtsverkehr, Dokumentenformat) — § 32a ZPO (Elektronisches Dokument) — § 55a VwGO (Elektronisches Dokument Verwaltungsrecht) — § 55d VwGO (Pflicht zur elektronischen Einreichung) — § 4 PDFA-Standard ISO 19005 (PDF/A-Normen)

## Kommentarliteratur

- Kopp/Schenke, VwGO, 30. Aufl. 2024, § 55a Rn. 1 ff. (elektronisches Dokument, Formatanforderungen)
- Zöller/Greger, ZPO, 35. Aufl. 2024, § 32a Rn. 1 ff. (elektronische Einreichung, PDF-Anforderungen)
