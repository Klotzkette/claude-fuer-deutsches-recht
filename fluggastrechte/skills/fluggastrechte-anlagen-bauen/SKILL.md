---
name: fluggastrechte-anlagen-bauen
description: "Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Mahnung Klage) die Belege Buchungsbestätigung Boardingpass Annullierungsbestätigung E-Mail-Verkehr Quittungen. Konvertiert alles nach PDF nummeriert in der Reihenfolge der ersten Erwaehnung im Schriftsatz stempelt oben rechts Anlage K 1 in Arial 12 fett und benennt beA-tauglich. Liefert Einzel-PDFs Konvolut-PDF Anlagenverzeichnis und optional ein Schriftsatz-mit-Anlagen-Bundle als ein PDF."
---

# Fluggastrechte — Anlagen bauen

## Zweck

Im Fluggastrechte-Mandat sammelt der Mandant typischerweise einen bunten Strauß an Belegen: Buchungsbestätigung als PDF, Boardingpass als Screenshot, E-Mails der Airline mit Annullierungsbestätigung, Restaurant-Quittungen vom Flughafen als Foto, Taxiquittungen, Hotelrechnungen. Dieser Skill macht aus diesem Material ein einheitliches, gerichtsfestes Anlagenkonvolut.

Der Skill wird **automatisch** von den Schreiben-Skills (`forderungsschreiben-erste-stufe`, `forderungsschreiben-mahnung`, `klage-amtsgericht-fluggast`) angestoßen, sobald dort ein Schriftsatz fertig ist und Belege im Mandantenordner liegen. Er kann auch manuell aufgerufen werden, etwa wenn nur die Belege geordnet werden sollen.

## Eingaben

- **Schriftsatz** (PDF oder DOCX) — das vom vorhergehenden Skill erzeugte Forderungsschreiben, die Mahnung oder die Klage.
- **Belege-Ordner** mit den Beweisstücken in beliebigem Format:
  - PDF (Buchungsbestätigung, Annullierungsbestätigung, Tickets)
  - DOCX (eigene Aufzeichnungen, Mandanten-Sachverhaltsdarstellung)
  - JPG / PNG (Boardingpass-Foto, Anzeigetafel-Foto, Quittungs-Foto)
  - EML / MSG (E-Mail-Korrespondenz mit der Airline)
- **Zielordner** für das Ergebnis (wird angelegt).
- **Bundle-Option** (`--bundle`): zusätzlich ein einziges PDF `Schriftsatz_mit_Anlagen.pdf` mit dem Schriftsatz vorne und allen Anlagen dahinter.

## Workflow

### Schritt 1 — Belege konvertieren

Alle Belege werden zunächst nach PDF normalisiert:

| Eingang | Verfahren |
|---|---|
| PDF | unverändert übernommen |
| JPG / PNG | Pillow legt das Bild auf eine A4-Seite mit 150 dpi |
| DOCX / EML / MSG / ODT / RTF / TXT / HTML | LibreOffice headless konvertiert nach PDF |

Fehlt LibreOffice oder Pillow, gibt der Skill eine konkrete Installations-Anweisung aus und lässt den Beleg in der Eingangsliste mit Warnung stehen.

### Schritt 2 — Anlagen aus dem Schriftsatz lesen

Der Skill liest den Schriftsatz und extrahiert alle Bezugnahmen vom Muster "Anlage K 1", "Anlage K2", "Anlage K 3a". Reihenfolge: die der **ersten Erwähnung im Schriftsatz** (BGH-Stil, nicht chronologisch). Wenn der Schriftsatz noch keine Anlagen-Nummern enthält, wird alphabetisch durchnummeriert — dann sollte der Schreiben-Skill in einem zweiten Lauf die Bezeichnungen im Schriftsatz nachtragen.

### Schritt 3 — Stempel oben rechts (Arial 12 fett)

Auf der ersten Seite jeder Anlage wird ein dezenter, aber deutlicher Stempel gesetzt:

- Position: rechter oberer Rand, ca. 1,5 cm vom oberen Seitenrand, ca. 1,5 cm vom rechten Seitenrand.
- Schrift: Arial 12 pt **fett** (in der reportlab-Basisschrift Helvetica-Bold).
- Format: `Anlage K 1`, `Anlage K 7`, `Anlage K 3a`.

Mehrseitige Anlagen erhalten den Stempel nur auf Seite 1.

### Schritt 4 — beA-konforme Dateinamen

Jede Einzelanlage wird unter einem Dateinamen abgelegt, der beA-kompatibel ist:

```
Anlage_K-01_Buchungsbestaetigung.pdf
Anlage_K-02_Boardingpass.pdf
Anlage_K-03_Email-Airline-Annullierung.pdf
Anlage_K-04_Quittung-Restaurant-Flughafen.pdf
Anlage_K-05_Taxiquittung.pdf
```

Regeln: keine Umlaute, kein scharfes ß, keine Leerzeichen, Nummer zweistellig, maximal ca. 90 Zeichen.

### Schritt 5 — Konvolut + Anlagenverzeichnis

Im Zielordner entstehen:

```
konvertiert/    Zwischenstand der konvertierten Belege
gestempelt/     Einzelanlagen mit Stempel, beA-konform benannt
Anlagenkonvolut.pdf       alle Anlagen, mit Lesezeichen pro Anlage
Anlagenverzeichnis.md     tabellarische Übersicht (Anlage / Beschreibung / Seiten)
Anlagenverzeichnis.pdf    gleiche Tabelle als PDF
```

### Schritt 6 — Optional: Schriftsatz-mit-Anlagen-Bundle

Mit `--bundle` legt der Skill **zusätzlich** `Schriftsatz_mit_Anlagen.pdf` an: der Schriftsatz vorne, dann das Konvolut, durchlaufende Lesezeichen. Genau das spart den Mandanten den letzten Schritt der Zusammenstellung, wenn er das Ganze einreichen oder per Post schicken will.

## Werkzeug

`werkzeuge/build_fluggast_anlagen.py`. Aufruf-Beispiel:

```bash
# Forderungsschreiben mit Belegen
python3 werkzeuge/build_fluggast_anlagen.py \
    --belege ./mandat-mueller/belege \
    --schriftsatz ./mandat-mueller/forderungsschreiben.pdf \
    --ausgang ./mandat-mueller/anlagen \
    --titel "Forderungsschreiben Erste Stufe"

# Klage mit gebundeltem Schriftsatz + Anlagen
python3 werkzeuge/build_fluggast_anlagen.py \
    --belege ./mandat-mueller/belege \
    --schriftsatz ./mandat-mueller/klage.pdf \
    --ausgang ./mandat-mueller/anlagen \
    --titel "Klage Amtsgericht Hamburg" \
    --bundle
```

Abhängigkeiten: `pypdf`, `reportlab`, optional `Pillow` (für Bild-Konvertierung), optional LibreOffice (für DOCX/EML).

## Rückfragen, falls etwas fehlt

Der Skill stoppt mit einer klaren Frage zurück an den Mandanten / die Sekretariatskraft, wenn:

- der Belege-Ordner leer ist (Frage: "Welche Belege liegen vor und in welchem Format? Bitte alle in den Ordner kopieren, auch Fotos und E-Mails.");
- der Schriftsatz weder PDF noch DOCX ist (Frage: "Liegt der Schriftsatz als PDF vor? Wenn er noch in der Mahnung-Skill-Vorschau steht, bitte erst dort als PDF exportieren.");
- mehr Anlagen im Schriftsatz benannt sind, als Belege im Ordner liegen (Frage: "Der Schriftsatz nennt Anlage K 5, im Ordner sind aber nur 4 Dateien — welcher Beleg fehlt?");
- ein Beleg im Ordner liegt, der im Schriftsatz nicht erwähnt wird (Hinweis: "Beleg X wird im Schriftsatz nicht zitiert. Soll er trotzdem als zusätzliche Anlage angehängt werden, oder weggelassen?").

## Was dieser Skill bewusst NICHT tut

- **Keine inhaltliche Schwärzung** (Kontonummern, Personalausweis-Daten, fremde Passagierdaten auf Boardingpässen). Wenn die Anlage geschwärzt werden muss, wird das vor diesem Skill manuell erledigt.
- **Keine OCR-Vollerkennung.** Das Werkzeug liest nur den Schriftsatz, um Anlagen-Nummern zu finden — es liest die Belege nicht inhaltlich aus.
- **Keine elektronische Signatur** und **kein automatisches beA-Hochladen.** Das macht der Mandant oder die Kanzlei selbst.
- **Keine Echtheitsprüfung** der Belege.

## Beispiele typischer Nutzerformulierungen, die diesen Skill auslösen

- "Bitte die Belege aus dem Ordner ./belege als Anlagen K 1 bis K 5 zum Forderungsschreiben aufbereiten."
- "Erstelle ein Anlagenkonvolut für die Klage, alles in einem PDF."
- "Stemple meine Belege als Anlagen und benenne sie beA-konform."
- "Mach aus dem Schriftsatz und den Belegen ein einziges PDF zum Einreichen."

## Übergabe

Die Schreiben-Skills (`forderungsschreiben-erste-stufe`, `forderungsschreiben-mahnung`, `klage-amtsgericht-fluggast`) rufen diesen Skill **automatisch** am Ende ihrer Arbeit auf, sobald ein Belege-Ordner im Mandatsverzeichnis vorhanden ist. Der Nutzer kann das mit der Option "Anlagen separat lassen" abwählen.

## Leitentscheidungen Anlagen / Schriftsatz

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
