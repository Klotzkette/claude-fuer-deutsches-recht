---
name: dokumentstruktur-makroebene-vertrag-und-schriftsatz
description: "Makrostruktur juristischer Dokumente sauber bauen. Vertrag mit Rubrum/Parteien, Praeambel, Definitionen, Hauptleistungspflichten, Nebenpflichten, Bedingungen, Beendigung, Boilerplate, Anlagen. Schriftsatz nach § 253 Abs. 2 ZPO mit Rubrum, Antraegen, Sachverhalt, rechtlicher Wuerdigung, Beweisangeboten, Schlussformel, Anlagenverzeichnis. Mit Strukturbaeumen je Dokumenttyp als Tabelle."
---

# Dokumentstruktur Makroebene: Vertrag und Schriftsatz

## Zweck

Juristisches Drafting beginnt mit der Architektur, nicht mit dem Klauseltext. Wer einen Vertrag ohne Inhaltsverzeichnis schreibt, baut ein Haus ohne Statik. Dieser Skill liefert die Standard-Makrostruktur fuer die beiden wichtigsten Dokumenttypen: Vertrag und Schriftsatz. Daneben kurz: Memo, Anwaltsschreiben, AGB.

Die Struktur ist Konvention, keine Mode. Gerichte erwarten sie. Geschaeftsleitung erwartet sie. Wer abweicht, soll wissen warum.

Der Skill liefert je Dokument einen Strukturbaum als Tabelle und ein Skelett. Klauseltext entsteht in den Spezial-Skills.

## Eingaben

- Dokumenttyp und Untertyp (Kaufvertrag, Lieferantenvertrag, Klage, Klageerwiderung, Antrag)
- Komplexitaetsgrad (einfach, mittel, M&A-Niveau)
- Parteien und Rollen
- Vorliegende Vorentwuerfe oder Term Sheet

## Rechtlicher und methodischer Rahmen

- § 253 Abs. 2 ZPO: Pflichtbestandteile der Klageschrift.
- § 130 ZPO: Allgemeiner Schriftsatz-Inhalt.
- § 311b BGB: Beurkundungspflicht fuer bestimmte Vertraege (Grundstueck, GmbH-Geschaeftsanteile).
- § 126 BGB, § 126a BGB, § 126b BGB: Schriftform, elektronische Form, Textform.
- § 305 Abs. 1 BGB: AGB-Begriff. Vertraege mit AGB-Anteil brauchen zusaetzliche Strukturelemente.

## Ablauf / Checkliste

1. **Dokumenttyp wahlen.** Vertrag, Klage, Klageerwiderung, AGB, Memo, Anwaltsschreiben.
2. **Standardstruktur waehlen.** Siehe Tabellen unten.
3. **Anpassen.** Streichen Sie nicht benoetigte Bloecke, ergaenzen Sie Sonderkapitel.
4. **Nummerierung festlegen.** § (Paragraph) oder Ziffer. M&A-Vertraege ueblich mit Ziffern, BGB-Vertraege ueblich mit Paragraphen.
5. **Inhaltsverzeichnis automatisch erzeugen.** Word-Skill `word-formatvorlagen-querverweise-track-changes` nutzen.
6. **Querverweise vorbereiten.** Siehe `verweis-und-querverweis-technik`.

### Strukturbaum Vertrag (Standardfall)

| Block | Inhalt | Optional |
|---|---|---|
| Rubrum | Bezeichnung der Parteien mit Anschrift, ggf. Handelsregister, Vertretung | nein |
| Praeambel | Hintergrund, Anlass, Zweck. Auch "Whereas-Klauseln" | im Standardvertrag entbehrlich, im M&A ueblich |
| Definitionen | alphabetisch oder thematisch gegliedert | bei kurzem Vertrag inline |
| Vertragsgegenstand | Hauptleistungspflicht in einer Klausel | nein |
| Hauptleistungspflichten | Pflichten der Parteien im Detail | nein |
| Nebenpflichten | Mitwirkung, Information, Schutz | je nach Vertragstyp |
| Verguetung | Hoehe, Faelligkeit, Zahlweise, Verzug | nein, wenn entgeltlich |
| Maengelhaftung | Pflichten bei Mangel, Fristen, Rechte | je nach Vertragstyp |
| Haftung | Begrenzung, Ausschluss, Versicherung | siehe `haftungsausschluss-und-haftungsbegrenzung` |
| Geheimhaltung | NDA-Baustein oder Verweis auf NDA | je nach Mandat |
| Laufzeit und Beendigung | Erstlaufzeit, Verlaengerung, ordentliche und ausserordentliche Kuendigung | nein |
| Boilerplate | Schriftform, Salvatorisch, Gerichtsstand, Rechtswahl, Erfuellungsort | siehe `boilerplate-klauseln-katalog` |
| Unterschriften | Ort, Datum, Unterzeichner mit Funktion | nein |
| Anlagen | Anlagenverzeichnis, durchnummeriert | wenn vorhanden |

### Strukturbaum Klageschrift (§ 253 Abs. 2 ZPO)

| Block | Inhalt | Quelle |
|---|---|---|
| Rubrum | Gericht, Parteien mit gesetzlicher Vertretung, Aktenzeichen | § 253 Abs. 2 Nr. 1 ZPO |
| Antraege | bestimmte Antraege | § 253 Abs. 2 Nr. 2 ZPO |
| Sachverhalt | Tatsachenvortrag, chronologisch oder thematisch | § 253 Abs. 2 Nr. 2 ZPO |
| Rechtliche Wuerdigung | Anspruchsgrundlagen in der Reihenfolge Vertrag, c.i.c., GoA, dinglich, Delikt, Bereicherung | freie Gliederung |
| Beweisangebote | Zeugen, Urkunden, Sachverstaendige, Augenschein | § 130 Nr. 5 ZPO |
| Streitwert | Vorschlag fuer Streitwertfestsetzung | § 61 GKG |
| Schlussformel | Unterschrift des Rechtsanwalts | § 130 Nr. 6 ZPO |
| Anlagenverzeichnis | K1, K2 usw. | freie Konvention |

### Strukturbaum Klageerwiderung

| Block | Inhalt |
|---|---|
| Rubrum | wie Klage, mit Aktenzeichen |
| Antraege | Klageabweisung, ggf. Widerklage |
| Bestreiten | substantiiertes Bestreiten der Klagebehauptungen |
| Eigener Sachverhalt | abweichende Darstellung |
| Rechtliche Wuerdigung | Einwendungen, Einreden |
| Beweisangebote | wie Klage |
| Schlussformel | Unterschrift |

### Strukturbaum Memo (Standardstruktur Repository)

1. Sachverhalt
2. Frage(n)
3. Kurzantwort
4. Rechtliche Bewertung
5. Gesamtergebnis
6. Risiken / offene Punkte
7. Quellenverzeichnis

## Typische Drafting-Fehler

- **Definitionen nach hinten.** Defined Terms gehoeren nach vorne, nicht in den Anhang.
- **Praeambel als Vertrag.** Praeambel ist Auslegungshilfe, nicht Pflicht. Klauseln nicht in Praeambel-Saetze verstecken.
- **Boilerplate vergessen.** Salvatorisch, Schriftform, Gerichtsstand sind Pflicht im B2B-Vertrag.
- **Antraege unbestimmt.** § 253 Abs. 2 Nr. 2 ZPO. Unbestimmter Antrag ist unzulaessig.
- **Sachverhalt vermischt mit Rechtsmeinung.** Sachverhalt ist Faktentafel, kein Schlagabtausch.
- **Anlagen ohne Verzeichnis.** Anlage K7 ohne Verzeichnis ist im Prozess nicht auffindbar.

## Ausgabeformat

- Strukturbaum als Tabelle.
- Skelett-Dokument mit Ueberschriften und Platzhaltern in eckigen Klammern.
- Hinweis auf einschlaegige Spezial-Skills je Block.

## Beispiel

**Skelett Liefer- und Werkvertrag (mittlere Komplexitaet):**

```
RUBRUM
zwischen [Verkaeufer GmbH, Anschrift, HRB] (Lieferant)
und [Besteller AG, Anschrift, HRB] (Besteller)

§ 1 Definitionen
§ 2 Vertragsgegenstand
§ 3 Lieferung und Abnahme
§ 4 Verguetung und Zahlung
§ 5 Eigentumsvorbehalt
§ 6 Maengelhaftung
§ 7 Haftung
§ 8 Geheimhaltung
§ 9 Laufzeit und Kuendigung
§ 10 Schriftform und Aenderungen
§ 11 Salvatorische Klausel
§ 12 Gerichtsstand und Rechtswahl
§ 13 Anlagen

Anlage 1: Leistungsbeschreibung
Anlage 2: Preisliste
Anlage 3: Lieferplan
```

## Querverweise

- `definitionen-klauseln-stringent`
- `boilerplate-klauseln-katalog`
- `haftungsausschluss-und-haftungsbegrenzung`
- `verweis-und-querverweis-technik`
- `klage-drafting-253-zpo`
- `gutachten-memo-internes-drafting`

## Quellen (Stand 05/2026)

- § 253 Abs. 2 ZPO; § 130 ZPO; gesetze-im-internet.de.
- § 311b BGB; § 126 BGB; § 126a BGB; § 126b BGB; § 305 Abs. 1 BGB.
- Memo-Struktur: CLAUDE.md im Repository-Wurzelverzeichnis.
- Vertragsstruktur folgt der Konvention deutscher Wirtschaftskanzleien. Konkrete Klauselmuster vom Nutzer mit aktueller Literatur zu validieren.
