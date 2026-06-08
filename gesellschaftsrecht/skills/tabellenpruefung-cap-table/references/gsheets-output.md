# Google-Sheets-Ausgabeformat

Für Teams, die Google Workspace nutzen. Gleiche Struktur wie das Excel-Ausgabeformat, andere technische Umsetzung. Wenn sowohl Excel- als auch Sheets-Pfad verfügbar sind, fragen Sie den Benutzer nach seiner Präferenz — raten Sie nicht anhand der Umgebung.

## Vorgehensweise

Drei Wege, in Präferenzreihenfolge:

1. **Google Sheets MCP** (wenn ein `gdrive`- oder `gsheets`-MCP mit Schreib-/Erstellungsfunktion verbunden ist). Tabelle erstellen, Tabellenblätter schreiben, Formatierung über die API setzen.
2. **Google Sheets API über ADC** (wenn der Benutzer `gcloud auth application-default login --enable-gdrive-access` eingerichtet hat und Python `google-api-python-client` verfügbar ist). `sheets.spreadsheets().create()` und `batchUpdate` für die Formatierung verwenden.
3. **Fallback: CSV + manueller Import.** CSV-Dateien schreiben, den Benutzer über den Import in Sheets informieren. Außerdem eine `formatierungshinweise.md` erstellen, damit er die Farbkodierung und Datenvalidierung manuell anwenden kann.

Nehmen Sie keinen Schreibzugriff an, den Sie nicht verifiziert haben. Erst prüfen, dann graceful fallback.

## Arbeitsmappenstruktur

Spiegelt die Excel-Spezifikation exakt wider — gleiche Tabellenblätter, gleiche Semantik, Sheets-native Umsetzung:

**Tabellenblatt: `Prüfung`** (das Hauptraster)
- Zeile 1: Arbeitsprodukt-Kopfzeile (zusammengeführte Zelle)
- Zeile 2: Spaltenbezeichnungen
- Ab Zeile 3: eine Zeile pro Dokument
- Spalte A: Dokumentname / Link (wenn Quelldokumente in Drive liegen, als Hyperlink zur Datei verknüpfen — dies ist ein Vorteil von Sheets gegenüber Excel)
- Ab Spalte B: eine Spalte pro Schema-Spalte
- **Quellzitate in Zellnotizen ablegen** (Sheets-Notizen, nicht Kommentare — Notizen sind dauerhafte Anmerkungen, Kommentare sind Kollaborations-Threads). Notizen erscheinen beim Überfahren mit der Maus und werden beim Export als `.xlsx` zu Kommentaren.
- Zellfüllung nach Status: Standard = `beantwortet`, hellgelb = `unklar` oder `prüfen`, hellgrau = `nicht_vorhanden`. `repeatCell` mit `userEnteredFormat.backgroundColor` in `batchUpdate` verwenden.
- Eine `Geprüft`-Spalte nach jeder Gruppe: standardmäßig leer, Datenvalidierungs-Dropdown `✓ | ✗ | ?` über `setDataValidation`.

**Tabellenblatt: `Hinweise`**
- Wie die Excel-Spezifikation. Eine Zeile pro markierter Zelle.

**Tabellenblatt: `_schema`**
- Spaltendefinitionen aus `.review-schema.yaml`.

**Tabellenblatt: `_zusammenfassung`**
- Anzahlen, markierte Spalten, Verifizierungserinnerung.

## Sheets-spezifische Vorteile nutzen

- **Hyperlinks zu Quelldokumenten.** Wenn die geprüften Dokumente in Drive liegen (üblich bei VDR-Exporten und internen Repositories), sollte der Dokumentname in jeder Zeile ein Hyperlink zur Datei sein. Dies ist das Click-to-Source-Muster, das Sheets nativ unterstützt.
- **Geteilte Prüfung.** Sheets verarbeitet gleichzeitige Prüfungen besser als eine lokale `.xlsx`. Wenn das Deal-Team die Verifizierungsarbeit aufteilen möchte, ist dies das geeignete Format.
- **Benannte Bereiche für das Schema.** Definieren Sie für jede Spalte einen benannten Bereich, damit nachgelagerte Formeln (Pivot-Tabellen, bedingte Zählungen) lesbar sind.
- **Bedingte Formatierung über Statusspalte.** Wenn Sie eine ausgeblendete `_status`-Spalte pro Datenspalte schreiben, können Sie die Farbkodierung daraus mit Regeln für bedingte Formatierung steuern — sauberer als zellenweise Formatierung und überlebt das Sortieren.

## Sheets-spezifische Fallstricke

- **Notizen sind pro Zelle und im Druck unsichtbar.** Wenn die Ausgabe für ein Partner-Meeting gedruckt oder als PDF erstellt wird, die Zitate auch in das `Hinweise`-Tabellenblatt schreiben, damit sie erhalten bleiben.
- **Sheets hat ein Limit von 10 Millionen Zellen.** Bei einer juristischen Prüfung wird dieses Limit nicht erreicht. Wenn jedoch jemand 50.000 Dokumente mit 30 Spalten plus Quellspalten zu einem Raster zusammenfassen möchte, darauf hinweisen.
- **Freigabe-Standardeinstellungen.** Gemäß dem Plugin-Praxisprofil handelt es sich um anwaltliches Arbeitsprodukt. Die Tabelle mit eingeschränkter Freigabe erstellen (nur Eigentümer), und den Benutzer auffordern, sie bewusst freizugeben. Nicht standardmäßig auf "Jeder mit dem Link" setzen.
- **Formel-Maskierung.** Wenn ein wörtliches Zitat mit `=`, `+`, `-` oder `@` beginnt, ein einfaches Anführungszeichen (`'`) voranstellen, damit Sheets es nicht als Formel interpretiert. Dies ist ein realer Fehlerfall: Eine Vertragsklausel, die mit "- Die Parteien vereinbaren..." beginnt, führt ohne die Maskierung zu einem Formelfehler.

## Was zu vermeiden ist

Wie in der Excel-Spezifikation: Keine Konfidenzprozentsätze, keine abgeschnittenen Zitate, keine zusammengeführten Zellen im Datenbereich, und immer die Tabellenblätter `_schema` und `_zusammenfassung` schreiben.


## Schutz vor Formel-Injection

Vor dem Schreiben einer Zelle in Excel-, Sheets- oder CSV-Ausgabe sind Formel-Injections zu neutralisieren. Texte der Gegenseite (Vertragsauszüge, Parteinamen, Daten aus dem Handelsregister, CLM-Exporte) sind potenziell angreiferkontrolliert. Eine Zelle, die mit `=`, `+`, `-`, `@`, `\t`, `\r` oder `\n` beginnt, wird als Formel interpretiert oder bricht die Zeilenstruktur auf.

- **Voranstellen eines einfachen Anführungszeichens:** `'=SUMME(A1:A10)` → `=SUMME(A1:A10)` (wird als Text angezeigt, nicht ausgeführt)
- **Gilt für jede Zelle, die Text aus einem Dokument, einem Werkzeugergebnis oder einer Benutzereingabe enthält.** Von Ihnen selbst verfasste Spaltenüberschriften und selbst berechnete Werte sind sicher.
- **CSV: Eingebettete Kommas, doppelte Anführungszeichen und Zeilenumbrüche ebenfalls maskieren** (RFC 4180-Maskierung).
- Dies ist nicht optional. Eine Tabelle, die der Benutzer in Excel öffnet und die ein Makro auslöst oder Daten über DDE ausleitet, ist ein Supply-Chain-Angriff auf den Benutzer.
