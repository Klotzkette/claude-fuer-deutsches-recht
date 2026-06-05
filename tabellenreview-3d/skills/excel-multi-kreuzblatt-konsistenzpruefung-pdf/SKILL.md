---
name: excel-multi-kreuzblatt-konsistenzpruefung-pdf
description: "Excel Multi Kreuzblatt Konsistenzpruefung PDF: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Excel Multi Kreuzblatt Konsistenzpruefung PDF

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Excel Multi Kreuzblatt Konsistenzpruefung PDF** im Plugin Tabellenreview 3D. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `excel-multi-sheet-export` | 3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei Multisheet-Struktur. Abgrenzung: nicht PDF-Bericht. |
| `kreuzblatt-konsistenzpruefung` | Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege. Output: Konsistenz-Prüfbericht mit Fehlerliste. Abgrenzung: nicht Risikoampel-Aggregation. |
| `pdf-bericht-erzeugen` | 3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Prüfraster: Vollständigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview. Abgrenzung: nicht Excel-Export. |

## Arbeitsweg

Im Plugin Tabellenreview 3D gilt für **Excel Multi Kreuzblatt Konsistenzpruefung PDF**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `excel-multi-sheet-export`

**Fokus:** 3D-Review-Ergebnis als Excel-Datei mit mehreren Arbeitsblaettern exportieren: je Perspektive ein Sheet. Normen: HGB, InsO. Prüfraster: Formatvorgaben, Zellenformatierung, Formelkonsistenz. Output: Excel-Exportdatei Multisheet-Struktur. Abgrenzung: nicht PDF-Bericht.

# /tabellenreview-3d:excel-multi-sheet-export


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Excel ist das Lingua Franca der Mandatsübergabe. Der 3D-Würfel wird in Excel nativ abgebildet: jedes Arbeitsblatt ist ein Tabellenreiter — genau das was die dritte Dimension visuell darstellt.

## Aufbau der Excel-Datei

### Reiter 1 bis N — Pro Arbeitsblatt-Perspektive

Jede Tabelle hat dieselbe Struktur:
- Zeilen: Dokumente aus `zeilen-inventar.yaml`
- Spalten: aus `spaltenprompts.yaml` plus Arbeitsblatt-spezifische Zusatzspalten
- Zellinhalt: Antwort + wörtliches Zitat + Fundstelle (Datei-ID + Seite + Absatz)
- Zell-Hintergrundfarbe: rot / gelb / grün aus Ampel
- Zell-Kommentar: Prüfer-Flag (falls gesetzt) und Prompt-Version

### Reiter 'Übersicht'

- Würfel-Gesamtampel oben
- Arbeitsblatt-Ampel pro Reiter
- Spalten-Hotspots (Top-N)
- Prüfer-Flag-Anzahl

### Reiter 'Hotspots'

Pro Spalte: Anzahl rot / gelb / grün über den Stapel. Sortiert absteigend nach Rot-Anteil.

### Reiter 'Widersprüche'

Aus `kreuzblatt-konsistenzpruefung`. Spalten: Zeile-ID, Spalte, Arbeitsblatt-A-Antwort, Arbeitsblatt-B-Antwort, Konflikt-Klassifikation, empfohlene Aktion.

### Reiter 'Prüfer-Flags'

Liste aller Zellen mit Prüfer-Flag. Spalten: Zeile, Arbeitsblatt, Spalte, Grund (OCR-Konfidenz / Mehrdeutigkeit / Hash-Bruch / Konflikt), Antwortvorschlag, Prüfer-Entscheidung (leer).

### Reiter 'Belegkette'

Tabelle aller Dokumente mit: Datei-ID, Pfad, SHA-256-Hash, Seitenzahl, OCR-Konfidenz. Damit ist jede Fundstelle im Würfel rückverfolgbar auf den exakten Dateistand.

### Reiter 'Prompt-Versionen'

Spalten-Prompts und Zeilen-Prompts mit jeweiliger Version-ID und Änderungsdatum (aus `prompt-versionierung`). Damit ist jede Zelle reproduzierbar.

### Reiter 'Audit-Trail'

Reviewlauf-Zeitstempel, verwendete Modell-Version, Laufdauer, Anzahl Zellen, Anzahl Cache-Treffer, Prüfer-Abnahme-Status. Aus `audit-trail-protokoll`.

## Technische Hinweise

- Format: `.xlsx`
- Bedingte Formatierung für Ampel-Farben
- Zell-Kommentare für Prüfer-Flags
- Hyperlinks von 'Fundstelle' zur Datei (relativ zum Projektordner)
- Spalte einfrieren (`Zeile-ID`) und Kopfzeile einfrieren

## Ausgabe

- `<projekt>-wuerfel.xlsx` mit allen Reitern
- `<projekt>-würfel-anhang.zip` (optional) mit allen referenzierten Quelldokumenten zur autarken Mandantenübergabe (Achtung: Geheimhaltungs- und DSGVO-Pflichten beachten)

## Grenzen

Excel kann große Stapel handeln; ab 100.000 Zellen sind PDF und CSV pro Reiter zu erwägen (siehe Skill `pdf-bericht-erzeugen`).

## 2. `kreuzblatt-konsistenzpruefung`

**Fokus:** Kreuzblatt-Konsistenzprüfung: Abgleich der drei Dimensionen Forderung-Prüfung-Stellung auf Widerspruchsfreiheit. Normen: §§ 174 ff. InsO. Prüfraster: Betragsabweichungen, Statusinkonsistenzen, fehlende Eintraege. Output: Konsistenz-Prüfbericht mit Fehlerliste. Abgrenzung: nicht Risikoampel-Aggregation.

# /tabellenreview-3d:kreuzblatt-konsistenzprüfung


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Eine Zelle die rechtlich grün aber datenschutzrechtlich rot ist ist nicht automatisch ein Fehler — sie ist eine perspektivische Abweichung. Oft aber ist sie ein Fehler: dieselbe Tatsache wurde in zwei Arbeitsblättern unterschiedlich erfasst. Dieser Skill findet beides.

## Methodik

1. **Achsen-Match:** dieselbe Zeile dieselbe Spalte aber unterschiedliches Arbeitsblatt: vergleichen.
2. **Faktischer Widerspruch:** beide Arbeitsblätter haben das Vertragsdatum extrahiert; das eine sagt 2021-03-15, das andere 2021-03-25. Das ist ein Datenfehler — Prüfer-Flag.
3. **Perspektivischer Widerspruch:** ein Arbeitsblatt sagt 'wirksam' das andere 'unwirksam'. Wenn beide Arbeitsblätter dieselbe Norm benutzen ist es Datenfehler; wenn unterschiedliche Normen (Recht vs Steuer) ist es legitime Abweichung — als `legitim` markieren.
4. **Ampel-Inkonsistenz:** dieselbe Zeile in einem Arbeitsblatt rot in einem gelb in einem grün — Konsolidierungsempfehlung an `risikoampel-aggregation`.
5. **Norm-Bezugs-Widerspruch:** ein Arbeitsblatt verweist auf BGB Paragraph 307, ein anderes auf BGB Paragraph 305c bei derselben Klausel. Beides möglich — Prüfer-Hinweis.

## Konflikt-Klassifikation

- **echter Widerspruch:** beide Antworten beanspruchen dieselbe Tatsache aber unterscheiden sich. Prüfer-Flag rot.
- **legitime perspektivische Abweichung:** Arbeitsblätter haben unterschiedliche Pruefmassstaebe. Vermerk gelb.
- **Datenfehler:** OCR-Konfidenz schwach in einem der Arbeitsblätter — Re-Run dieser Zelle.
- **Klassifikationsfehler:** Dokumenttyp falsch erkannt — Zeile neu klassifizieren.

## Ausgabe

- `widerspruchsbericht.md` mit pro Widerspruch:
 - Zeile (Dokument)
 - Spalte (Datenpunkt)
 - Arbeitsblatt-A und Arbeitsblatt-B mit jeweiliger Antwort
 - Konflikt-Klassifikation
 - Empfohlene Aktion (Re-Run / Prüfer / Konsolidierung)

## Beispiele

- **echter Widerspruch:** Kundenvertrag-042. Spalte 'Laufzeit'. Recht: '3 Jahre + 1 Jahr Verlängerung'. Wirtschaft: '4 Jahre Festlaufzeit'. Echter Widerspruch — Wirtschaft hat den Vertrag verkürzt gelesen.
- **legitime Abweichung:** Lizenzvertrag-018. Spalte 'Haftung'. Recht: 'unwirksam BGB Paragraph 309 Nr 7'. Steuer: 'irrelevant — Pauschalhaftungs-Aufwand absetzbar'. Legitim — unterschiedliche Pruefmassstaebe.

## 3. `pdf-bericht-erzeugen`

**Fokus:** 3D-Review-Ergebnis als PDF-Bericht erzeugen: Zusammenfassung, Tabellen, Risikoampeln. Normen: §§ 174 ff. InsO. Prüfraster: Vollständigkeit Berichtinhalte, Layout, Signaturfeld. Output: PDF-Bericht 3D-Tabellenreview. Abgrenzung: nicht Excel-Export.

# /tabellenreview-3d:pdf-bericht-erzeugen


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Mandanten lesen lieber PDF als Excel. Der PDF-Bericht ist die Erzählfassung des Würfels: vom Aggregat über die Perspektiven bis in die Belegkette.

## Struktur

### 1. Deckblatt

- Projektname und kurzer Anlassbezug (z. B. 'M&A-DD Erwerb der X-GmbH zum Stichtag YYYY-MM-DD')
- Mandant und anwaltlicher Prüfer
- Anzahl Dokumente Anzahl Datenpunkte Anzahl Arbeitsblatt-Perspektiven
- Würfel-Gesamtampel
- Prüfer-Abnahme-Status

### 2. Management-Summary (Ein Blatt)

- Würfel-Ampel mit Begründung in drei Sätzen
- Top-5-Hotspots (Datenpunkte mit überproportional vielen roten Zellen)
- Top-5-rote-Zeilen (Dokumente die das größte Risiko tragen)
- Top-3-Widersprüche aus `kreuzblatt-konsistenzpruefung`
- Anzahl Prüfer-Flags und Status der Abnahme

### 3. Pro Arbeitsblatt-Perspektive (ein Abschnitt)

- Perspektive (Recht / Steuer / Wirtschaft / Datenschutz / IT / Betrieb / Compliance)
- Arbeitsblatt-Ampel mit Begründung
- Top-Findings dieser Perspektive (max 10)
- Hinweis auf zuständigen Prüfer (Rechtsanwalt / Steuerberater / DSB usw.)

### 4. Vollständige Tabellen (Anhang A)

Pro Arbeitsblatt eine Tabelle mit allen Zeilen und Spalten. Ampelfarben als Hintergrund. Zell-Inhalt: Antwort plus Fundstelle plus Prüfer-Flag.

### 5. Belegkette (Anhang B)

Alle zitierten Quellen mit:
- Datei-ID
- Pfad
- SHA-256-Hash
- Seitenzahl bei Fundstelle
- OCR-Konfidenz pro Seite (bei gescannten Dokumenten)

### 6. Audit-Anhang (Anhang C)

- Prompt-Versionen (Spalten und Zeilen)
- Verwendete Modell-Version und Konfiguration
- Reviewlauf-Zeitstempel und Laufdauer
- Cache-Trefferquote
- Prüfer-Abnahme-Historie

## Bedingte Formatierung

- Rote Hintergrundfarbe bei roter Ampel
- Gelbe Hintergrundfarbe bei gelber Ampel
- Schwacher Grüner-Ton bei grüner Ampel (sonst zu unruhig)
- Schraffur bei Prüfer-Flag

## Sicherheit

- PDF mit eingebetteten Schriften (kein nachträgliches Ersetzen)
- Optional: Schreibschutz und Signaturfeld für den Prüfer
- Optional: Wasserzeichen 'VERTRAULICH ARBEITSERGEBNIS' bei unsignierter Fassung

## Ausgabe

- `<projekt>-bericht.pdf`
- `<projekt>-bericht-quellen.zip` (optional) — alle in der Belegkette referenzierten Quelldokumente

## Grenzen

Bei sehr großen Würfeln (mehr als 50.000 Zellen) wird der PDF unhandlich. In diesem Fall: PDF nur für Management-Summary und Anhang A pro Arbeitsblatt als separate PDFs. Vollständige Daten weiter in Excel.
