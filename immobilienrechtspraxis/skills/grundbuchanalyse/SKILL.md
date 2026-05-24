---
name: grundbuchanalyse
description: Strukturierte Auswertung grosser Mengen Grundbuchdaten — Grundbuchauszuege Flurkarten Baulastenverzeichnis Altlastenkataster. Extrahiert pro Objekt Eigentuemerkette Belastungen in Abteilung II und III Rang Loeschungserleichterungen Grunddienstbarkeiten Reallasten Vorkaufsrechte sowie offene Briefgrundschulden. Erzeugt Risikomatrix und Portfoliosicht ueber alle Objekte. Geeignet fuer Due-Diligence-Portfolios Bestandsaufnahme nach Erwerb Refinanzierungs-Vorbereitung und laufende Asset-Management-Kontrolle. Akzeptiert PDF-Scans mit OCR und konsumiert Tabellen aus XML oder CSV des Grundbuchamtes.
---

# Grundbuchanalyse

## Leitidee

Grundbuchdaten kommen in der Praxis als Stapel von PDF-Auszügen, oft
gescannt, mit dazwischengewürfelten Baulastenverzeichnissen, Flurkarten
und Altlastenausweisen. Der Skill normalisiert alles auf eine
Objekttabelle und ein einheitliches Risikoschema.

## Inputs

- Grundbuchauszüge (.pdf, gescannt oder digital)
- Optional: Baulastenverzeichnis-Ausdrucke
- Optional: Altlastenkataster-Auskuenfte
- Optional: Flurkarten und Lageprüfungen
- Objektliste als .xlsx oder .csv

## Methodik

1. OCR auf gescannten PDFs
2. Pro Auszug Identifikation Bestandsverzeichnis Abteilung I II III
3. Strukturierte Extraktion:
   - Bestandsverzeichnis: Gemarkung Flur Flurstück Wirtschaftsart
     Größe
   - Abteilung I: Eigentümerkette mit Erwerbsgrund
   - Abteilung II: Lasten und Beschraenkungen (Dienstbarkeiten
     Reallasten Vorkaufsrechte Nacherbenvermerk Sanierungsvermerk)
   - Abteilung III: Grundpfandrechte mit Rang Betrag Gläubiger
     Löschungserleichterung Brieftyp
4. Querverweis mit Baulastenverzeichnis (Baulasten existieren NICHT
   im Grundbuch)
5. Risikobewertung pro Objekt und Aggregation auf Portfolio
6. Generierung Risikomatrix Excel-Tabelle und Memo

## Output

- `Grundbuch_Portfolio.xlsx` — eine Zeile pro Flurstück, Spalten je
  Risikofeld
- `Risikomatrix.md` mit Ampel pro Objekt und Aggregat-Statistik
- `Auffaelligkeiten.md` — Objekte mit ungewöhnlichen Vermerken
  (Insolvenzvermerk Zwangsversteigerungsvermerk Nacherbenvermerk
  Sanierungsvermerk § 144 BauGB Vorkaufsrecht nach BauGB)

## Typische Risikofelder

- Briefgrundschuld ohne Löschungsbewilligung
- Rangverhältnis Abteilung III nicht eindeutig
- Dienstbarkeit zugunsten unbekannter Dritter (Leitungsrechte
  Wegerechte)
- Vorkaufsrecht der Gemeinde nach §§ 24 ff. BauGB
- Sanierungsvermerk § 144 BauGB — Genehmigung erforderlich
- Nacherbenvermerk § 2113 BGB
- Insolvenz- oder Zwangsversteigerungsvermerk
- Baulast nicht im Grundbuch aber gegen Eigentümer wirksam
- Altlastenverdachtsfläche und mietminderungsrelevante Schadstoffe

## Beispielformulierungen

- "Werte alle Grundbuchauszüge aus diesem Ordner aus. Erzeuge
  Portfoliosicht und markiere Objekte mit Sanierungsvermerk."
- "Ich habe 87 PDF-Auszüge. Zeig mir Objekte mit offenen
  Briefgrundschulden und Baulasten."
- "Prüfe diese 15 Objekte auf Vorkaufsrechte der Gemeinde nach
  Paragraph 24 BauGB."

## Grenzen

Der Skill ersetzt nicht die Prüfung durch einen Immobilienjuristen.
Er liefert Vorstrukturierung und Risiko-Heatmap, damit der Mensch
seine Zeit dort einsetzt, wo es wirklich brennt.
