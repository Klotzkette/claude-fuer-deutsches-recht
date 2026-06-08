---
name: dokumentstapel-aufnehmen
description: "Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output: Dokumentenstapel-Inventar. Abgrenzung: nicht Einzeldokument-Prüfung."
---

# /tabellenreview-3d:dokumentstapel-aufnehmen

## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Bevor der Reviewlauf startet muss der Dokumentenstapel sauber sein — kein Dokument doppelt kein Dokument vergessen kein Dokument falsch klassifiziert. Dieser Skill ist die Eingangsphase der Zeilenachse.

## Eingabequellen

- **VDR-Export:** Verzeichnis mit Originalstruktur — Datasite Intralinks Box SharePoint
- **Lokaler Ordner:** flach oder verschachtelt
- **E-Mail-Anhänge:** automatische Extraktion aus EML / MSG
- **Gescannte PDF:** OCR-Pipeline mit Konfidenzwert pro Seite
- **Manuelle Liste:** vom Nutzer eingegebene Dateipfade

## Ablauf

1. **Inventarisierung:** alle Dateien rekursiv erfassen, kanonischen Pfad bilden.
2. **Hashing:** SHA-256 pro Datei berechnen — Basis für Duplikaterkennung und Belegkette.
3. **Klassifikation:** Dokumenttyp aus Dateiname Mimetype und Inhalt (z. B. Vertrag-Kunde / Vertrag-Lieferant / NDA / Bankvereinbarung / Lizenzvertrag / Personalakte / Grundbuchauszug / Mietvertrag / Gesellschaftsvertrag).
4. **Sprache:** Sprachidentifikation pro Dokument (Deutsch / Englisch / sonstige).
5. **OCR bei Scans:** OCR ausführen, Konfidenz protokollieren. Konfidenz unter 90 Prozent = `prüferflag`.
6. **Duplikatprüfung:** Hash-Identität erkennt exakte Duplikate. Ähnlichkeit (z. B. Cosine über Embedding) erkennt Quasi-Duplikate (Fassungen / Änderungsvereinbarungen).
7. **Datenraum-Lücken:** wenn ein Dokument auf `Anlage 7` verweist und im Stapel keine `anlage 7` vorhanden ist, als `lücke` markieren.
8. **Zeilen-Inventar schreiben:** `zeilen-inventar.yaml` mit allen Zeilen, jede mit `id` `pfad` `hash` `typ` `sprache` `ocr-konfidenz` `prüfer-flag` und leerem `zeilenprompt`.

## Pflichtfelder pro Zeile

```yaml
- id: z-0042
 pfad: "vdr/kunden/042-rahmenvertrag-mueller-gmbh-2023.pdf"
 hash: "sha256:a1b2..."
 typ: "rahmenvertrag-kunde"
 sprache: "de"
 seitenzahl: 47
 ocr-konfidenz: 0.97
 pruefer-flag: null
 zeilenprompt: ""
 datenraum-luecken: []
```

## Ausgabe

- `zeilen-inventar.yaml` — vollständige Zeilenachse
- `duplikatreport.md` — exakte und Quasi-Duplikate mit Prüfer-Entscheidung
- `datenraum-luecken.md` — referenzierte aber nicht vorhandene Dokumente

## Grenzen

Klassifikation ist heuristisch. Bei Konfidenz unter 80 Prozent fragt der Skill zurück. OCR-Qualität hängt vom Scan ab. Belegkette ist nur so gut wie die OCR-Konfidenz.
