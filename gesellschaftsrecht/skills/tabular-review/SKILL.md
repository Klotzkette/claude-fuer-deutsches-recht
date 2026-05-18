---
name: tabular-review
description: >
  Tabellarisches Vertragsreview im Rahmen der M&A Due Diligence — eine Zeile pro
  Dokument, eine Spalte pro Datenpunkt, jede Zelle mit Quellenangabe. Geeignet für
  Massenreviews (Change-of-Control-Klauseln, Abtretungsverbote, MAC-Klauseln in 200
  Zielgesellschaftsverträgen) und jeden anderen Stapeldurchlauf, der eine strukturierte
  Tabelle als Ergebnis erfordert. Lädt bei „tabellarisches Review", „Review-Raster",
  „Raster aufbauen", „Felder aus Verträgen extrahieren", „Dokumente auf X, Y, Z prüfen",
  „Tabelle erstellen" oder bei Verweis auf einen Dokumentenordner mit Vergleichsauftrag.
language: de
triggers:
  - "tabellarisches Review"
  - "Review-Raster"
  - "Due Diligence Tabelle"
  - "Verträge auf Klauseln prüfen"
  - "Change-of-Control Review"
  - "Massenreview"
  - "Vertragsmatrix"
  - "Felder extrahieren"
  - "Batch-Review"
---

# Tabellarisches Vertragsreview (M&A Due Diligence)

## Zweck

Sie haben einen Stapel Dokumente und eine Liste von Fragen, die konsistent für jedes Dokument beantwortet werden müssen. Eine Due-Diligence-Anforderungsliste. Ein Vendor-Vertragsaudit. Eine Mietportfolioprüfung. Das Ergebnis ist eine Tabelle: Dokumentenzeilen, Datenpunktspalten, und jede Zelle rückverfolgbar bis auf die exakten Wörter im Quelltext.

Dies ist keine Problemerkennung. `/Due-Diligence-Extraktion` findet die 30 Probleme, die in 2.000 Dokumenten stecken. Dieser Skill beantwortet dieselben 15 Fragen für alle 2.000 Dokumente. Beides ist legitim; beide beantworten unterschiedliche Fragen.

Dies ist auch kein Ersatz dafür, das Dokument selbst zu lesen. Jede von diesem Skill erzeugte Zelle ist ein **Hinweis, der der Verifikation bedarf**, kein Befund. Das Ergebnis soll die Verifikation beschleunigen, nicht überspringen.

## Eingaben

- Dokumentenquelle: Datenraum-Ordner, lokaler Pfad, SharePoint-Bibliothek
- Schema (entweder beschrieben oder als `.review-schema.yaml` hochgeladen)
- Ausgabeformat: Excel (`.xlsx`) oder CSV — nach Wahl des Nutzers
- Praxisprofil (CLAUDE.md) → Due-Diligence-Struktur, Wesentlichkeitsschwellen, Hausformat

## Rechtlicher Rahmen

**M&A Due Diligence allgemein:**
§§ 311 Abs. 2, 241 Abs. 2 BGB (vorvertragliche Aufklärungspflichten); §§ 443, 444 BGB (Garantien, Haftungsausschluss); § 442 BGB (Kenntnis des Käufers, Ausschluss der Gewährleistung). BGH, Urt. v. 27.03.2009 – V ZR 30/08, NJW 2009, 2064 Rn. 25 (Due-Diligence-Pflicht des Käufers; Kenntnis von Mängeln).

**Change-of-Control-Klauseln:**
BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18 (Auslegung einer Change-of-Control-Klausel; Kündigung bei mittelbarem Kontrollwechsel); BGH, Urt. v. 10.11.2016 – I ZR 193/15, NJW-RR 2017, 877 Rn. 14 (Vertragsübernahme ohne Zustimmung des Schuldners).

**Vertragliche Abtretungsverbote:**
§ 399 BGB (Abtretungsausschluss durch Parteivereinbarung); § 354a HGB (Abtretungsverbot im Handelsverkehr zwischen Kaufleuten; Unwirksamkeit im kaufmännischen Kontext); BGH, Urt. v. 14.11.1991 – IX ZR 31/91, NJW 1992, 1026 (Abtretungsverbot; Rechtsfolgen).

**MAC-Klauseln (Material Adverse Change):**
§§ 313, 314 BGB (Wegfall der Geschäftsgrundlage; außerordentliche Kündigung) als gesetzlicher Hintergrund; MAC-Klauseln im SPA regeln vertraglich den Rücktritt/Closing-Verweigerungsrecht des Käufers bei wesentlicher Verschlechterung.

**Kommentarliteratur:**
Westermann, in: MüKoBGB, 9. Aufl. 2022, § 453 Rn. 12 (Unternehmenskauf, Due Diligence); Bayer, in: Lutter/Hommelhoff, GmbHG, 21. Aufl. 2023, § 15 Rn. 5 (Abtretung GmbH-Anteile, Due Diligence); Hopt, in: Baumbach/Hopt, HGB, 41. Aufl. 2024, § 354a Rn. 1 (Abtretungsverbot im Handelsverkehr).

## Ablauf

### Schritt 0: Was und Wo

Klären:
1. **Dokumente.** Wo liegen sie? Datenraum-MCP (Box, Datasite, SharePoint), lokaler Ordner oder Dateiliste. Wie viele? Bei > 200 Dokumenten: Warnung, dass dies Zeit braucht; Angebot, mit einem wesentlichkeitsgefilterten Teilbestand zu beginnen.
2. **Schema.** Welche Spalten? Zwei Wege:
   - Nutzer wählt Vorlage aus `references/` (Standard: M&A Due Diligence)
   - Nutzer beschreibt Spalten in natürlicher Sprache, die dann in das getypte Schema überführt werden
3. **Ausgabe.** Excel (`.xlsx`) oder CSV — fragen, nicht raten. CSV und Markdown werden immer als Fallback geschrieben.

### Schritt 1: Schema aufbauen und bestätigen

Spaltenliste des Nutzers in ein strukturiertes Schema überführen. Für jede Spalte: eine stabile `id`, ein menschlicher `label`, ein `typ`, ein `prompt` (die Frage, die ein Reviewer beim Lesen stellen würde), und für `klassifizieren`-Spalten eine `optionen`-Liste.

Schema als `.review-schema.yaml` neben der Ausgabe speichern. Dem Nutzer zeigen und vor dem Durchlauf bestätigen.

**Spaltentypensystem:**

| Typ | Was er zurückgibt | Verwendung |
|---|---|---|
| `wörtlich` | Exaktes Zitat aus dem Dokument, zeichengenau | Definitionen, operative Klauselformulierungen, alles wo die Worte zählen |
| `klassifizieren` | Ein Wert aus einer von Ihnen definierten festen Liste | Ja/Nein, vorhanden/nicht vorhanden, Klauselvarianten (z.B. „alleiniges Zustimmungsrecht" / „Zustimmung nicht ohne sachlichen Grund zu versagen" / „keine Regelung") |
| `datum` | ISO-Datum | Abschlussdatum, Ablauf, Kündigungsfrist |
| `dauer` | Zahl + Einheit | Vertragslaufzeit, Kündigungsfrist, Überlebensfrist |
| `betrag` | Zahl + Währungscode | Haftungsobergrenzen, Schwellenwerte, Honorare |
| `zahl` | Bloße Zahl | Anzahlen, Prozentsätze, Seitenverweise |
| `frei` | Kurze Freitextzusammenfassung | Sparsam verwenden — dies ist der Typ, der Inkonsistenz erzeugt. Nur wenn die anderen wirklich nicht passen. |

**Die Wörtlichkeitsregel:** Jede Nicht-`wörtlich`-Spalte erfasst auch das exakte Quellzitat, das die Antwort stützt, als Begleitfeld. Die Antwort in der Zelle ist die Interpretation; das Zitat ist der Beweis.

### Schritt 2: Probedurchlauf

Nicht 200 Dokumente mit einem ungeprüften Schema durchlaufen. Erst 3–5 Dokumente prüfen. Zeilen dem Nutzer zeigen. Folgendes beachten:
- Spalten, bei denen die meisten Antworten `unklar` sind — Prompt ist mehrdeutig, umformulieren
- `klassifizieren`-Spalten, bei denen Antworten nicht in die Optionen passen — Optionen ergänzen oder zu `frei` wechseln
- `wörtlich`-Spalten, die Paraphrasen zurückgeben — auf zeichengenaue Zitierweise bestehen

Schema anpassen, Probedurchlauf wiederholen, bestätigen. Dies verhindert einen vollständigen Durchlauf, der verworfen werden muss.

### Schritt 3: Vollständiger Durchlauf

Ein Unteragent pro Dokument, parallel. Jeder Unteragent:

1. Liest das gesamte Dokument (kein RAG-Chunk — der vollständige Text).
2. Findet für jede Spalte die relevante Bestimmung.
3. Gibt eine strukturierte Zeile zurück: für jede Spalte `{wert, zustand, zitat, fundstelle}`.
   - `wert` ist die getypte Antwort (oder null, wenn `zustand` nicht `beantwortet` ist)
   - `zustand` ist `beantwortet | nicht_vorhanden | unklar | pruefung_erforderlich`
   - `zitat` ist der wörtliche Begleittext (exakt, keine Paraphrase, kein Auslassungszeichen innerhalb eines Satzes — beim Kürzen auf Satzgrenzen kürzen und markieren)
   - `fundstelle` ist wo das Zitat im Dokument steht (Abschnittsnummer, Überschrift, Seite)

**Die Wörtlichkeitsregel ist mechanisch, keine Empfehlung.** Jeder Unteragent muss alle folgenden Punkte erfüllen, bevor er eine Zelle mit `zustand: beantwortet` zurückgibt:

- Das `zitat` MUSS eine zeichengenaue Kopie zusammenhängenden Texts aus dem Quelldokument sein, abrufbar an der genannten `fundstelle`. NICHT aus Abschnittsüberschrift plus erwartetem Standardtext zusammensetzen. NICHT paraphrasieren und als wörtlich bezeichnen. NICHT ein Zitat aus der Erinnerung rekonstruieren, wie solche Klauseln „üblicherweise" lauten. NICHT Lücken durch Auslassungszeichen zwischen nicht zusammenhängendem Text überbrücken.
- Die `fundstelle` muss spezifisch genug sein, dass der Normalisierungsdurchgang das Dokument an derselben Stelle wieder öffnen und denselben Abschnitt lesen kann.
- Falls der Unteragent den exakten Text nicht finden und kopieren kann (Quelle abgeschnitten, OCR-Fehler, Bestimmung impliziert aber nicht geschrieben, Abschnittsüberschrift sichtbar aber Text nicht geladen): Zellzustand ist `pruefung_erforderlich`, `wert` ist null, und `notizen` MUSS `zitat_nicht_verfügbar: <Grund>` enthalten.

### Schritt 4: Normalisierung

Nach dem Durchlauf die gesamte Tabelle spaltenweise lesen. Dies ist der Durchgang, der das Hauptversagen jedes tabellarischen Review-Tools aufdeckt: dieselbe Klausel, inkonsistent über Dokumente hinweg interpretiert.

Für jede `klassifizieren`-Spalte:
- Prüfen, ob jeder `beantwortet`-Wert in der Optionsliste steht. Ausreißer neu klassifizieren oder auf `pruefung_erforderlich` setzen.
- Auf Häufungen prüfen: Wenn 180 Dokumente `zustimmungserforderlich` und 20 `keine_regelung` sagen, ist das wahrscheinlich real. Wenn 195 `zustimmungserforderlich` und 5 `frei_übertragbar` sagen, die 5 prüfen.

Für jede `datum`/`dauer`/`betrag`-Spalte:
- Formatkonsistenz prüfen und normalisieren.
- Unplausible Werte (`99`-jährige Laufzeit, 1-EUR-Haftungsdeckelung) als `pruefung_erforderlich` flaggen.

Für Quellzitate — Stichprobe: bei mindestens 3–5 Zeilen pro Spalte (oder 10 %, je nachdem was größer ist) das Quelldokument an der genannten `fundstelle` wieder öffnen und das gespeicherte `zitat` zeichengenau mit dem Quelltext vergleichen. Bei Abweichung: Zelle auf `pruefung_erforderlich` setzen mit `zitat_abweichung` in Notizen, und ganze Spalte auf weiteren Spot-Check ausweiten.

### Schritt 5: Ausgabe

**Markdown** (immer, für sitzungsinterne Prüfung):
```markdown
| Dokument | Gegenpartei | Wirksamkeitsdatum | Change of Control | Abtretung | ⚠️ Flags |
|---|---|---|---|---|---|
| Lieferanten-MSA — Alpha | Alpha GmbH | 2023-04-01 | zustimmungserforderlich | zustimmungserforderlich | — |
| Rahmenvertrag — Beta | Beta KG | 2021-11-15 | ⚠️ unklar | keine_regelung | CoC unklar § 14.2 |
```

**CSV** (`.csv`, immer):
Eine Datei für die Werte, eine Begleitdatei für Zitate und Fundstellen (`_quellen.csv`). Hält die Hauptdatei übersichtlich und die Beweiskette vollständig.

**Excel** (`.xlsx`) oder **CSV** — je nach Wahl des Nutzers. Im Tabellenformat:
- Jede Datenspalte ist mit einer verdeckten Quellspalte gepaart, die Zitat und Fundstelle enthält. Zellenkommentare (Excel) oder Notizen zeigen das Zitat beim Überfahren.
- Farbkodierung nach Zustand: weiß = beantwortet, gelb = unklar oder pruefung_erforderlich, grau = nicht_vorhanden.
- Eine `Geprüft`-Spalte pro Datenspalte, standardmäßig leer. Der Reviewer markiert sie. Dies ist das Prüf-/Flag-Muster, das die Tabelle prüfbar macht.
- Ein `_Schema`-Tabellenblatt mit den Spaltendefinitionen, damit die Datei selbstdokumentierend ist.

Arbeitsergebnis-Kopfzeile aus CLAUDE.md als oberste Zeile einfügen. Dazu einen Verteilungshinweis:

> Dieses Review basiert auf Quelldokumenten, die privilegiert, vertraulich oder beides sein können. Es teilt den Schutzstatus der Quellen — die Verteilung über den Vertraulichkeitskreis hinaus kann das Mandatsgeheimnis (§ 43a Abs. 2 BRAO) beeinträchtigen. Mit den privilegierten Unterlagen des Mandats aufbewahren und Verteilungsentscheidungen bewusst treffen.

### Schritt 6: Zusammenfassung

Nach Fertigstellung der Tabelle eine kompakte Übersicht ausgeben:
- Dokumentenanzahl, Spaltenanzahl, abgeschlossene Zeilen
- Anzahl von `nicht_vorhanden`, `unklar`, `pruefung_erforderlich` pro Spalte — das ist die Verifikationsarbeit
- Spalten, bei denen der Normalisierungsdurchgang > 10 % der Zeilen flaggte
- Speicherort der Ausgabedateien
- Hinweis: Jede Zelle ist ein Hinweis, kein Befund. Verifikation erforderlich, bevor dies eine Gewährleistung, einen Anhang oder einen Vermerk informiert.

## Ausgabeformat

Strukturierte Tabelle (Markdown in Sitzung, Excel/CSV als Dateien) + Schema-YAML + Zusammenfassungs-Einseiter. Arbeitsergebnis-Kopfzeile und Verteilungshinweis oben.

## Beispiel

**Szenario:** GmbH-Anteilskauf, 80 Zielgesellschaftsverträge im Datenraum. Aufgabe: Change-of-Control-Klauseln, Abtretungsverbote und Mindestvertragslaufzeit extrahieren.

Nach Probedurchlauf (5 Dokumente): Schema angepasst (CoC-Optionen um „Kündigung bei mittelbarem Kontrollwechsel" ergänzt, wie in BGH KZR 2/07 relevant). Vollständiger Durchlauf: 80 Zeilen, 12 Verträge mit CoC-Klauseln (davon 3 unklare Formulierungen → `pruefung_erforderlich`), 15 Abtretungsverbote, 7 unter § 354a HGB-Vorbehalt.

## Risiken und typische Fehler

- **Dokumente überspringen.** Jedes vom Nutzer angegebene Dokument bekommt eine Zeile. Ein nicht lesbares Dokument bekommt eine Zeile `pruefung_erforderlich` mit Notiz.
- **Paraphrase als Zitat ausgeben.** Die Beweiskette ist der Kernwert. Wörtlichkeitsregel mechanisch umsetzen.
- **Schema nicht probetesten.** Ein Vollständigkeitsdurchlauf mit einem fehlerhaften Schema wird verworfen. Immer 3–5 Dokumente zuerst.
- **Konfidenzwerte ausgeben.** Kein numerischer Konfidenzwert. Stattdessen: `unklar`/`pruefung_erforderlich`-Zustände und verbatim-Zitate sind das Konfidenz-Signal.
- **§ 354a HGB ignorieren.** Abtretungsverbote zwischen Kaufleuten können nach § 354a HGB unwirksam sein — diese Besonderheit in den Schema-Notizen und Normalisierungskommentaren vermerken.

## Quellenpflicht

Alle rechtlichen Beurteilungen im Schema-Aufbau und in der Normalisierung mit Norm belegen:
- Abtretungsverbote: `§ 399 BGB`, `§ 354a HGB`
- Change-of-Control: `BGH, Urt. v. 29.04.2008 – KZR 2/07, NJW 2008, 3055 Rn. 18`
- Due-Diligence-Pflichten: `BGH, Urt. v. 27.03.2009 – V ZR 30/08, NJW 2009, 2064 Rn. 25`
- Kommentare: `Baumbach/Hopt, HGB, 41. Aufl. 2024, § 354a Rn. 1`

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
