# 1. Originalnamen erhalten und Anlagen eindeutig zuordnen

Der Anlagenplan verbindet Dateien im freigegebenen Eingangsordner mit den bereits im Schriftsatz verwendeten Kennungen. Er ist eine interne Produktionshilfe, keine einzureichende Anlage. Aus einer alphabetischen Dateiliste folgt keine Anlagenfolge.

## 1.1. Plan erstellen

Eine UTF-8-CSV mit Semikolon als Trenner und genau diesen vier Spalten verwenden:

```csv
quelle;anlage;beschreibung;auslassen_grund
Scans/Scan_004.pdf;B 7;Kaufvertrag vom 12.06.2026;
Mail vom Bauleiter.eml;B 8;Mitteilung zur Abnahme;
Berechnung Müller.xlsx;B 9;Abrechnung Restarbeiten;
Besprechungsnotiz.txt;;;Interne Abstimmung ohne Anlagenbezug
```

`quelle` ist der vollständige relative Pfad innerhalb des Eingangsordners, einschließlich Unterordnern. Nur `/` als Pfadtrenner verwenden. Keine absoluten Pfade, Verknüpfungen oder übergeordneten Verzeichnisse. Originalnamen dürfen Leerzeichen und Umlaute enthalten; nur die Versandnamen werden vereinheitlicht. Enthält ein Feld ein Semikolon, muss es nach CSV-Regeln in Anführungszeichen stehen.

Jede sichtbare Datei außer Hauptdokument und Plan selbst braucht eine Zeile. Entweder eine Kennung aus dem bestätigten Kreis K, B, AST oder AG oder einen Auslassungsgrund eintragen, niemals beides. Kennungen wie `B 7a` sind möglich; der Buchstabenzusatz bleibt im Versandnamen erhalten. Ein leerer Beschreibungstext verwendet den Originalnamen. Fehlende Quellen, doppelte Zuordnungen und Kennungskollisionen sperren die Freigabe. Auslassungsgründe werden im Prüfbericht dokumentiert.

## 1.2. E-Mail und Signaturen

EML-Anhänge unverändert in den Eingangsordner exportieren. Für jeden Anhang Aufnahme oder Ausschluss im Plan festhalten. Das Werkzeug gleicht die Bytes ab: Eine namensgleiche, aber andere Datei erledigt den Anhang nicht. Eingebettete Bilder können im Textauszug fehlen und erfordern Sichtkontrolle. Der Exportauftrag umfasst nur die ausgewählten Unterlagen, nicht automatisch jede empfangene Datei.

Signierte Anlagen werden nicht automatisch gestempelt. Original und gegebenenfalls abgesetzte Signaturdatei erhalten; die verantwortliche Person legt den zulässigen Einreichungsweg fest. Diese Sonderfälle nicht durch „Drucken als PDF“ oder einen Ausschluss ohne tatsächlichen sachlichen Grund umgehen. Der Anlagenplan ersetzt keine Signaturvalidierung.

## 1.3. Erster Produktionslauf

```bash
python skills/versandmappe-endfertigen/werkzeuge/build_versandmappe.py \
  --eingang ./eingang --ausgang ./ausgang_01 \
  --hauptdokument ./eingang/Klageerwiderung.docx \
  --anlagenplan ./eingang/Anlagenplan.csv --praefix B \
  --gericht "Landgericht Essen" --aktenzeichen "12 O 34/26" \
  --frist "2026-09-30 23:59" \
  --verantwortlich "Rechtsanwalt Jan Müller" --versender "Jan Müller" \
  --signaturweg persoenlich-sicher --strict
```

Eingangs- und Ausgangsordner müssen nebeneinander oder an getrennten Orten liegen, niemals ineinander. Nicht ungefragt `--ueberschreiben` verwenden. Dateien ohne Anlagenplan dürfen weiterhin die vorhandene Namenskonvention `Anlage_B_7_Kaufvertrag.pdf` nutzen; unzugeordnete Dateien bleiben dann Stop-Befunde.

Ein tatsächlich anlagenloser Schriftsatz erhält `--ohne-anlagen`. Das erlaubt keine unbekannten oder fehlenden Dateien. Status 2 bezeichnet einen Eingabe- oder Pfadfehler; Status 3 unter `--strict` bezeichnet einen dokumentierten Freigabestopp. Beim ersten Lauf ist die noch offene Sichtkontrolle erwartbar, nicht als Konvertierungsfehler zu behandeln.

## 1.4. Kontrollieren, ohne die geprüften Dateien zu ersetzen

Nach dem ersten Lauf jede endgültige PDF öffnen, mit der Quelle vergleichen und die einzelnen Befunde erledigen. Sicht- und Signaturprüfung mit Name, Zeitpunkt, Dateiname und SHA-256 im Freigabevermerk dokumentieren. Der ursprüngliche Preflight bleibt als Protokoll des Produktionszeitpunkts erhalten; die spätere Freigabe muss jeden Stop ausdrücklich auflösen. Eine allgemeine Freigabe trotz fehlender Anlage reicht nicht.

`--sichtpruefung-bestaetigt` und `--qes-geprueft` sind Angaben des Bearbeiters, keine Prüfwerkzeuge. Sie dürfen nicht vorsorglich gesetzt werden. Nach jeder Neuproduktion gehören die Kontrollen zu den neu erzeugten Bytes; deshalb nicht allein für einen grünen Programmstatus erneut konvertieren und alte Freigaben übertragen. Bei tatsächlichen Änderungen einen neuen Ausgabeordner erstellen und die betroffenen Ausgaben erneut prüfen.

Bleibt eine Konvertierung hängen oder fehlen passende Schriften, die konkrete Datei als manuell erzeugten PDF-Export anfordern. Keine unveränderten Wiederholungsversuche in Endlosschleife. Hauptdokument und jede Anlage bleiben getrennte Versand-PDFs; das interne Prüfkonvolut ersetzt diese Dateien nicht.
