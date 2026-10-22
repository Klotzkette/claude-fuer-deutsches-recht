# Qualitätsnachweis Testakten Nordlicht und Havelberg

Stand: 22. Oktober 2026

## 1. Prüfumfang

Geprüft wurden ausschließlich die erweiterten Abschlussmodule der Testakten `insolvenzverwaltung-nordlicht-handels-kiel` und `insolvenzverwaltung-moebelwerk-havelberg-regelverfahren`. Der Prüfumfang erfasst Zwischenbericht, Schlussbericht, Schlussrechnung, Schlussverzeichnis, Quotenrechnung, Freigaben, gerichtliche Korrespondenz, Zahlungsvollzug, Aufhebung und die getrennten Übungszweige einer möglichen Nachtragsverteilung.

## 2. Fachliche Rechenkontrolle

Nordlicht weist festgestellte Forderungen von 509.842,00 EUR und eine Teilungsmasse von 120.462,00 EUR aus. Die ungerundete Rechenquote beträgt 23,6273198363 Prozent; auf sechs Dezimalstellen gerundet sind es 23,627320 Prozent. Die centgenauen Einzelbeträge summieren sich auf 120.462,00 EUR.

Havelberg weist festgestellte Forderungen von 862.900,00 EUR und eine Teilungsmasse von 289.790,00 EUR aus. Die ungerundete Rechenquote beträgt 33,5832657318 Prozent; auf sechs Dezimalstellen gerundet sind es 33,583266 Prozent. Die centgenauen Einzelbeträge summieren sich auf 289.790,00 EUR. Der Sicherheitenzufluss und die Auskehrung an die Havelbank werden als erfolgsneutraler Durchlauf getrennt von der freien Masse dargestellt. Der ungesicherte Ausfall von 136.500,00 EUR wird nur einmal in der Forderungsbasis berücksichtigt.

Die Arbeitsmappen wurden mit LibreOffice in PDF gerendert. Beide Cockpits zeigen eine Differenz von 0,00 EUR und den Kontrollstatus `OK`. In den gerenderten Tabellen wurden keine Fehlerwerte, Gitterzeichen oder Sperrkennzeichen gefunden.

## 3. Dokumentkontrolle

Alle DOCX-Dateien beider Akten ließen sich mit `python-docx` öffnen. Alle EML-Dateien ließen sich mit dem Standardparser einlesen und enthalten Absender, Empfänger und Betreff. Die lokalen Links in beiden README-Dateien verweisen auf vorhandene Dateien. Veraltete Dateinamen mit `pruefvermerk` sowie das frühere Nordlicht-Datum `20-08-2024` sind nicht mehr vorhanden.

Ausgewählte Schlussberichte, Zwischenberichte, Freigaben, Vollzugsnachweise und Nachtragsunterlagen wurden mit der gebündelten LibreOffice-Runtime in PDF gesetzt. Die erste Seite der beiden Arbeitsmappen und die neuen Sachstandsnotizen wurden als PNG gerendert und visuell kontrolliert. Tabellen, Kernwerte, Überschriften und Freigabestatus sind lesbar und nicht abgeschnitten.

## 4. Gesamtakten

Der vorhandene Gesamtakten-Builder wurde für beide Akten erfolgreich ausgeführt:

| Testakte | Quelldateien | Seiten im Gesamt-PDF | Inhaltsprüfung |
| --- | ---: | ---: | --- |
| Nordlicht Handels GmbH | 53 | 76 | ohne Fehler |
| Möbelwerk Havelberg GmbH | 44 | 118 | ohne Fehler |

Die frühere Nordlicht-Sammelakte mit 294 Seiten enthielt überholte Abschlusswerte und ist deshalb weder Quelldokument noch Teil eines Releasepakets. Die hier ausgewiesenen, bereinigten Lesefassungen werden reproduzierbar aus genau einem Einzel-PDF je führendem Quelldokument erzeugt. Die Gesamt-PDFs sind nicht leer, enthalten die neuen Abschlussprodukte und bestehen aus A4-Seiten im Hoch- und Querformat. `pdf_content_errors` meldet für beide Dateien keine Beanstandung.

## 5. Technische Prüfungen

Folgende gezielte Prüfungen liefen erfolgreich:

1. `python3 scripts/build-insolvenzverwaltung-abschlussakten.py`
2. `python3 scripts/build-testakte-gesamt-pdf.py insolvenzverwaltung-nordlicht-handels-kiel insolvenzverwaltung-moebelwerk-havelberg-regelverfahren`
3. DOCX-, EML-, README-Link-, XLSX-Summen- und PDF-Inhaltsprüfung für genau diese beiden Akten
4. LibreOffice-PDF-Export und Textkontrolle beider XLSX-Arbeitsmappen
5. `python3 -m py_compile scripts/build-insolvenzverwaltung-abschlussakten.py`
6. `git diff --check`

Die repositoryweiten Testaktenvalidatoren wurden nicht als Abnahmenachweis herangezogen, weil der Arbeitsbaum nur einen Teil des sehr großen Testaktenbestands enthält. Stattdessen wurden dieselben entscheidenden Eigenschaften gezielt für die beiden bearbeiteten Akten geprüft.

Eine anschließende unabhängige Read-only-Gegenprüfung endete mit null Fehlern. Sie öffnete 60 DOCX-Dateien, parsierte 13 EML-Dateien, prüfte die drei XLSX-Arbeitsmappen einschließlich LibreOffice-Neuberechnung, kontrollierte alle lokalen README-Verweise und untersuchte alle zwölf neu gerenderten Einzel-PDFs textuell sowie seitenweise im Kontaktbogen. Abgeschnittene Kernwerte, Formel- oder Darstellungsfehler wurden nicht festgestellt.
