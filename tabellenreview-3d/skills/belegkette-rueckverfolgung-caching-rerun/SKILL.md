---
name: belegkette-rueckverfolgung-caching-rerun
description: "Belegkette Rueckverfolgung Caching Rerun: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Belegkette Rueckverfolgung Caching Rerun

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Belegkette Rueckverfolgung Caching Rerun** im Plugin Tabellenreview 3D. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `belegkette-rueckverfolgung` | Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output: Belegketten-Übersicht. Abgrenzung: nicht Excel-Export. |
| `caching-und-teil-rerun` | Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten und neu verarbeiteten Zeilen. Abgrenzung: nicht vollständiger Neustart. |
| `dokumentstapel-aufnehmen` | Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output: Dokumentenstapel-Inventar. Abgrenzung: nicht Einzeldokument-Prüfung. |

## Arbeitsweg

Im Plugin Tabellenreview 3D gilt für **Belegkette Rueckverfolgung Caching Rerun**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `belegkette-rueckverfolgung`

**Fokus:** Belegkette für Forderungen und Zahlungen zurückverfolgen: Originalbeleg, Buchung, Zahlung. Normen: §§ 238 257 HGB, §§ 174 ff. InsO. Prüfraster: Belegverknuepfung, fehlende Belege, Doppelbuchungen. Output: Belegketten-Übersicht. Abgrenzung: nicht Excel-Export.

# /tabellenreview-3d:belegkette-rueckverfolgung


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Eine Tabellenzelle die behauptet etwas zu sagen ohne dass man die Stelle im Dokument findet ist wertlos. Schlimmer: gefährlich. Dieser Skill macht jede Zellaussage rückverfolgbar.

## Komponenten der Belegkette

1. **Antwort** — was in der Zelle steht
2. **Woertliches Zitat** — in Anführungszeichen, exakter Wortlaut aus dem Dokument
3. **Fundstelle** — Datei-ID, Seite, Absatz, ggf. Ziffer und Buchstabe
4. **Datei-Hash** — SHA-256 der Quelldatei zum Zeitpunkt der Befuellung
5. **OCR-Konfidenz** — bei gescannten Dokumenten, für die Seite der Fundstelle
6. **Prompt-Version** — welcher Spaltenprompt zur Befuellung verwendet wurde

## Prüfung gegen Original

Beim Erstellen oder beim späteren Audit:

- **Hash-Prüfung:** ist der Datei-Hash der Quelldatei noch derselbe wie beim Befuellzeitpunkt? Wenn nein: `hash-bruch` im `audit-trail-protokoll`.
- **Volltext-Suche:** ist das wörtliche Zitat noch im Volltext der Datei auffindbar? Wenn nein: `zitat-nicht-mehr-im-original`.
- **Seitenkonsistenz:** existiert die angegebene Seite überhaupt in der Datei? Wenn nein: `fundstelle-außerhalb-dokument`.

## Umgekehrte Suche

Frage: 'Welche Zellen zitieren aus Seite 14 von Vertrag-042?' — der Index erlaubt diese Suche in beide Richtungen.

Anwendungsfälle:
- Vertrag wird geändert: welche Zellen müssen neu geprüft werden?
- Prüfer findet Fehler in Zelle X: welche anderen Zellen könnten aus derselben Stelle abgeleitet sein?
- Dokument wird nachgereicht: gibt es bereits Zellen die diese Stelle hatten?

## Pflichtanhang zur Mandatsübergabe

`belegkette.csv` mit Spalten:

```
zelle-id, arbeitsblatt, zeile, spalte, antwort, woertliches-zitat, datei-id, datei-hash, seite, absatz, ocr-konfidenz, prompt-version
```

Diese Datei MUSS bei jeder Mandatsübergabe mitgehen. Sie ist die Reproduzierbarkeits-Bescheinigung des Würfels.

## Grenzen

- Bei geänderten Dokumenten (Vertragsversion 2 überschreibt Version 1) erhält die Belegkette die alte Fassung — der Prüfer entscheidet ob neu zu rechnen ist.
- Bei OCR-Fehlern (Zitat hat OCR-Wortwahl die im Original anders steht) kann die Volltextsuche fehlschlagen — das ist ein bekannter OCR-Falschalarm, kein Belegkette-Bruch.

## 2. `caching-und-teil-rerun`

**Fokus:** Zwischenergebnisse des 3D-Tabellenreviews cachen und Teilbereiche erneut ausführen ohne Vollneustart. Normen: technisch. Prüfraster: Cache-Status, verarbeitete Zeilen, Fehlerpunkte. Output: Rerun-Bericht mit gecachten und neu verarbeiteten Zeilen. Abgrenzung: nicht vollständiger Neustart.

# /tabellenreview-3d:caching-und-teil-rerun


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Ein 25.000-Zellen-Würfel komplett neu zu berechnen weil ein einziger Spaltenprompt um drei Worte präziser wurde ist verschwenderisch. Dieser Skill macht den Würfel inkrementell.

## Cache-Key

Pro Zelle ein deterministischer Hash:

```
sha256(spaltenprompt-version + zeilenprompt-version + dokument-hash + arbeitsblatt-perspektive + modell-version)
```

Wenn irgendeine dieser Komponenten sich ändert wird der Cache-Eintrag invalidiert.

## Invalidierungsregeln

- **Patch-Änderung am Spaltenprompt:** Cache bleibt gültig (siehe `prompt-versionierung`)
- **Minor-Änderung am Spaltenprompt:** Cache wird auf `nachprüfen` gesetzt — Prüfer entscheidet ob neu rechnen
- **Major-Änderung am Spaltenprompt:** Cache invalidiert, betroffene Zellen müssen neu berechnet werden
- **Zeilenprompt geändert:** nur die betroffene Zeile invalidiert, über alle Arbeitsblätter
- **Arbeitsblatt-Perspektive geändert:** alle Zellen dieses Arbeitsblatts invalidiert
- **Dokument-Hash geändert (z. B. neue Version):** alle Zellen dieser Zeile invalidiert
- **Modell-Version geändert:** Vorgehen wählbar — komplett neu / Stichprobe prüfen / Cache übernehmen mit Hinweis

## Quasi-Duplikate

Ein Vertrag-Cousin (sehr ähnlich) kann Cache-Treffer vom geprüften Originalvertrag übernehmen — als VORSCHLAG nicht als Befund. Schwelle: Cosine-Ähnlichkeit über 95 Prozent UND derselbe Dokumenttyp UND derselbe Vertragspartner-Stamm. Prüfer-Flag automatisch. Prüfer bestätigt oder verwirft.

## Kostenschätzung

Vor jedem Teil-Rerun schaetzt der Skill:
- Anzahl zu berechnender Zellen
- erwartete Laufzeit
- erwartete Token-/Kosten-Aufnahme
- Auswirkung auf Audit-Trail

Prüfer kann Rerun beauftragen / ablehnen / nur Stichprobe rechnen lassen.

## Ausgabe

- `cache.parquet` — alle Zellen mit Cache-Key Antwort Belegkette Ampel
- `rerun-vorschlag.md` — pro Änderung welche Zellen invalidiert sind und Kostenschätzung
- Eintrag in `audit-trail-protokoll`

## Grenzen

Caching ist ein Effizienzwerkzeug nicht ein Beweismittel. Wer auf gerichtsfeste Reproduzierbarkeit angewiesen ist (z. B. Verfahrenseingabe) sollte einen kompletten Lauf ohne Cache machen und das Ergebnis hashen.

## 3. `dokumentstapel-aufnehmen`

**Fokus:** Dokumentenstapel für 3D-Tabellenreview einlesen: PDFs, Excel-Dateien, Word-Dokumente aufnehmen. Normen: §§ 174 ff. InsO. Prüfraster: Dateiformat-Kompatibilitaet, Metadaten, Importfehler. Output: Dokumentenstapel-Inventar. Abgrenzung: nicht Einzeldokument-Prüfung.

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
