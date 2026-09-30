# 1. Unabhängige Sichtprüfung des Gesamt-PDFs

Prüfung: 30.09.2026. Read-only; keine Änderung am PDF oder an Repository-Dateien.

PDF: `testakten/gesellschaftsgruender-topf-tacheles-berlin/gesamt-pdf/gesellschaftsgruender-topf-tacheles-berlin_gesamt.pdf`

SHA-256 vor und nach der Prüfung: `9574a190162ed9346fcaf39973693f6d149b6dab282a40481f4f85091ed77a96`

Umfang: **22 PDF-Seiten**. Rendering mit Poppler `pdftoppm -r 105 -png`; alle 22 gerenderten Seiten wurden tatsächlich einzeln über `view_image` betrachtet. Der Renderer gab einen Fontconfig-Hinweis aus, beendete den Lauf aber erfolgreich. Die tatsächlichen Renderings zeigen keine fehlenden Glyphen oder Ersatzzeichen.

## 1.1. Ergebnis

**Bestanden für die visuelle Prüfung.** Keine abgeschnittenen Zeilen, überlappenden Elemente, zerfallenen Tabellen oder unleserlichen JPG-Datenfelder festgestellt. Alle sieben Datenkarten zeigen deutlich, dass sie keine Ausweise oder Identitätsnachweise sind. Die gewünschten Namenslücken und als OFFEN bezeichneten Entscheidungsfelder sind sichtbar und lesbar; sie sind im Auftrag ausdrücklich vorgesehen und kein Renderingfehler.

Die Datei enthält die 15 Originalstücke: einen Chat auf einer Seite, vier E-Mails auf je einer Seite, sieben Datenkarten auf je einer Seite sowie drei DOCX mit zwei, drei und zwei Originalseiten. Zusätzlich stehen vor den drei Word-Dokumenten drei klar bezeichnete Trennblätter (PDF-Seiten 13, 16 und 20). Damit ergeben sich 19 Inhaltsseiten und drei Trennblätter, zusammen 22 Seiten. Die Word-Originalseiten behalten ihre jeweilige eigene Seitennummerierung; die Trennblätter sind keine versehentlichen Leerblätter. Die Reihenfolge folgt den Formatgruppen des zentralen Builders und nicht allein der Dateinummer.

Diese Prüfung betrifft die sichtbare Darstellung und Dateigrenzen. Sie ersetzt keine rechtliche Inhaltsprüfung oder gesonderte Kontrolle der ZIP-Pakete. Die JPGs sind im PDF Bildinhalte; ihre Personendaten werden vom einfachen PDF-Textextraktor nicht als Text geliefert. Eine Aussage, sämtliche Bildinhalte seien OCR-durchsuchbar, wird daher nicht getroffen.

## 1.2. Tatsächlich gesehene Seiten

| PDF-Seite | Inhalt | Konkrete Sichtprüfung |
| --- | --- | --- |
| 1 | Kurzer Gründerchat | Alle 14 Nachrichten vollständig sichtbar; letzte Nachricht und Fußzeile ohne Kollision. |
| 2 | Auftrag Frieda | E-Mail-Kopftabelle und Auftrag vollständig lesbar; keine abgeschnittenen Zeilen. |
| 3 | Mehrheiten-Rückfrage | Kopftabelle, Zitat und offene Rückfragen sauber umbrochen. |
| 4 | Notariat Terminvorbereitung | Dateiname und E-Mail-Tabelle passen; Dokument endet vor der freien unteren Fläche. |
| 5 | Letzter Stand | Vollständiger Text; klare Abgrenzung zur folgenden Bildanlage. |
| 6 | Datenkarte P01 Frieda Kowalski | Alle sechs Datenfelder und Hinweis KEIN AUSWEIS klar lesbar; Karte vollständig abgebildet. |
| 7 | Datenkarte P02 Leopold Nguyen | Vollständiger Vorname Leopold sichtbar; alle Felder und Fiktionskennzeichnung lesbar. |
| 8 | Datenkarte P03 Hatice Rosenkranz | Name, Geburtsdatum und Anschrift vollständig; keine Beschnitt- oder Kontrastprobleme. |
| 9 | Datenkarte P04 Nepomuk Krümel | Umlaut in Krümel korrekt; alle Datenfelder und Kennzeichnungen lesbar. |
| 10 | Datenkarte P05 Amina Yilmaz | Alle Daten und Kennzeichnungen gut lesbar; vollständige Karte. |
| 11 | Datenkarte P06 Bruno Buxbaum | Geburtsort Nürnberg mit Umlaut korrekt; keine abgeschnittenen Angaben. |
| 12 | Datenkarte P07 Zoe Funk | Alle Daten und Kennzeichnungen gut lesbar; vollständige Karte. |
| 13 | Trennblatt Vorüberlegungen und Anteilsplan | Dateiname vollständig, klare Dateigrenze; absichtlich sonst weitgehend leeres Trennblatt. |
| 14 | Vorüberlegungen, Originalseite 1 | Anteilstabelle mit sieben Personen passt auf die Seite; lange Zelle P07 sauber zweizeilig; Zahlen rechts lesbar. |
| 15 | Vorüberlegungen, Originalseite 2 | Dezimale Abschnitte und Fließtext vollständig, Fußzeile mit Originalseitennummer 2. |
| 16 | Trennblatt Satzung | Dateiname vollständig und lesbar; klare Dateigrenze. |
| 17 | Satzung, Originalseite 1 | Sieben Namensfelder und Nennbeträge in Tabelle vollständig sichtbar; offener Zahlungsplan lesbar. |
| 18 | Satzung, Originalseite 2 | Offene Vertretungs- und Betragsfelder korrekt umbrochen; keine Text- oder Fußzeilenkollision. |
| 19 | Satzung, Originalseite 3 | Felder für Prozentsatz, Bezugsbasis und Gründungsaufwand vollständig sichtbar; letzte Klausel mit ausreichendem Abstand zur Fußzeile. |
| 20 | Trennblatt Gesellschaftervereinbarung | Auch der lange Dateiname passt auf die Seite; klare Dateigrenze. |
| 21 | Gesellschaftervereinbarung, Originalseite 1 | P01–P07 mit vollständigen beschrifteten Eingabefeldern; Mitarbeit und Vergütung ohne Beschnitt. |
| 22 | Gesellschaftervereinbarung, Originalseite 2 | Offene Entscheidungsfelder und Schlussabsätze vollständig; Text endet deutlich vor der Fußzeile. |
