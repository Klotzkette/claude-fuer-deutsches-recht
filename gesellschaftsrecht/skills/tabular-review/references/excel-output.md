# Excel-Ausgabeformat

Die Excel-Datei ist das Ergebnis, das die meisten Deal-Teams tatsächlich öffnen werden. Setzen Sie sie sorgfältig auf.

## Wenn der Claude-in-Excel-/Office-Agent verfügbar ist

Erstellen Sie die Arbeitsmappe direkt in Excel über den Office-Agenten. Dies ist der bevorzugte Weg, da er die Formatierung erhält, den Prüfer in seinem gewohnten Werkzeug arbeiten lässt und das Zellkommentar-Muster nativ unterstützt.

## Andernfalls openpyxl verwenden

Prüfen Sie mit `python3 -c "import openpyxl"`. Falls nicht installiert, bieten Sie die Installation an (`pip3 install openpyxl`) oder weichen Sie auf CSV aus.

## Arbeitsmappenstruktur

**Tabellenblatt 1: `Prüfung`** (das Hauptraster)
- Zeile 1: Arbeitsprodukt-Kopfzeile (zusammengeführte Zelle, die Kopfzeile aus der Plugin-Konfiguration `## Ergebnisse`)
- Zeile 2: Spaltenbezeichnungen
- Ab Zeile 3: eine Zeile pro Dokument
- Spalte A: Dokumentname / Pfad
- Ab Spalte B: eine Spalte pro Schema-Spalte, in Schema-Reihenfolge
- Nach jeder Datenspalte eine ausgeblendete `_quelle`-Spalte mit `[Zitat] | [Fundstelle]`
- Zellkommentar in der Datenspalte = das Zitat und die Fundstelle (erscheint beim Überfahren mit der Maus auch bei ausgeblendeter `_quelle`-Spalte)
- Zellfüllung nach Status: keine Füllung = `beantwortet`, `#FFF2CC` (hellgelb) = `unklar` oder `prüfen`, `#EFEFEF` (hellgrau) = `nicht_vorhanden`
- Eine `Geprüft`-Spalte nach jeder Gruppe aus [Daten + _quelle]: standardmäßig leer; wird vom Prüfer ausgefüllt. Dropdown-Validierung: `✓`, `✗`, `?`.

**Tabellenblatt 2: `Hinweise`**
- Eine Zeile pro Zelle, die als `unklar` oder `prüfen` markiert ist
- Spalten: Dokument, Spalte, Status, Wert (falls vorhanden), Zitat, Fundstelle, Anmerkung
- Dies ist die Prüfungs-Arbeitsliste. Nach Spalte sortieren, damit der Prüfer gleichartige Beurteilungen bündeln kann.

**Tabellenblatt 3: `_schema`**
- Die Spaltendefinitionen aus `.review-schema.yaml`, eine Zeile pro Spalte: id, label, type, options, prompt
- Macht die Datei selbstdokumentierend. Ein Partner, der sie sechs Monate später öffnet, sieht genau, was gefragt wurde.

**Tabellenblatt 4: `_zusammenfassung`**
- Dokumentanzahl, Spaltenanzahl, Ausführungsdatum
- Pro Spalte: Anzahl beantwortet / nicht_vorhanden / unklar / prüfen
- Liste der Spalten, die der Normalisierungsdurchlauf markiert hat
- Der Erinnerungstext zur Verifizierung

## Was zu vermeiden ist

- Keine Konfidenzprozent-Spalte einfügen. Das ist keine Information. Status und Zitat sind das Signal.
- Zitate nicht abschneiden, um in eine Zelle zu passen. Text umbrechen oder das vollständige Zitat im Kommentar ablegen.
- Keine Zellen im Datenbereich zusammenführen. Anwälte werden sortieren und filtern.
- Tabelle nicht ohne die Tabellenblätter `_schema` und `_zusammenfassung` schreiben. Die Selbstdokumentation macht die Datei vertrauenswürdig.


## Schutz vor Formel-Injection

Vor dem Schreiben einer Zelle in Excel-, Sheets- oder CSV-Ausgabe sind Formel-Injections zu neutralisieren. Texte der Gegenseite (Vertragsauszüge, Parteinamen, Daten aus dem Handelsregister, CLM-Exporte) sind potenziell angreiferkontrolliert. Eine Zelle, die mit `=`, `+`, `-`, `@`, `\t`, `\r` oder `\n` beginnt, wird als Formel interpretiert oder bricht die Zeilenstruktur auf.

- **Voranstellen eines einfachen Anführungszeichens:** `'=SUMME(A1:A10)` → `=SUMME(A1:A10)` (wird als Text angezeigt, nicht ausgeführt)
- **Gilt für jede Zelle, die Text aus einem Dokument, einem Werkzeugergebnis oder einer Benutzereingabe enthält.** Von Ihnen selbst verfasste Spaltenüberschriften und selbst berechnete Werte sind sicher.
- **CSV: Eingebettete Kommas, doppelte Anführungszeichen und Zeilenumbrüche ebenfalls maskieren** (RFC 4180-Maskierung).
- Dies ist nicht optional. Eine Tabelle, die der Benutzer in Excel öffnet und die ein Makro auslöst oder Daten über DDE ausleitet, ist ein Supply-Chain-Angriff auf den Benutzer.
