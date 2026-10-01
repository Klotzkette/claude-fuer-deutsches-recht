# 1. Layoutprüfung Berliner Bildungsrecht

Prüfdatum: 2. Oktober 2026. Prüfung durch den Akten- und Layoutagenten, getrennt von der Erstellung der Werkstatttexte und ihrer finalen Renderläufe.

## 1.1 Umfang und Verfahren

Die beiden finalen Werkstatt-DOCX wurden mit dem Dokumentenrenderer und der gebündelten Headless-LibreOffice-Laufzeit in PDF und einzelne Seitenbilder umgewandelt. Die PDF-Dateien unter `assets/` haben normalisierte Metadaten und daher andere Dateihashes als die Render-PDFs. Für alle 69 Seiten wurden identische dekodierte Seiteninhaltsströme bestätigt; Zeichen, Schriftnamen und Zeichenpositionen stimmen vollständig überein, letztere innerhalb von 0,00001 pt Rundungstoleranz. Alle Seiten wurden einzeln in lesbarer Größe geöffnet und unmittelbar visuell geprüft; kleine Kontaktbögen wurden nicht als Ersatz für die Seitenprüfung verwendet. Nach der letzten Überschriftenänderung im Hochschulband und der Ergänzung zum Berliner Verwaltungsverfahrensrecht im Schulband wurden beide finalen Bände vollständig erneut angesehen.

| Werkstatt | Final geprüfte Seiten | Ergebnis |
| --- | ---: | --- |
| Berliner Hochschulrecht aus Professorensicht | 1–32, vollständig | Kein offener Layoutbefund |
| Berliner Kita- und Schulrecht aus Eltern- und Schülersicht | 1–37, vollständig | Kein offener Layoutbefund |

Damit umfasst die finale Werkstattprüfung 69 Seiten. Geprüft wurden Satzspiegel, Schriftbild, Abstände, Überschriften und Umbrüche, Fußzeilen, Seitenzahlen, Sonderzeichen und lange Quellenadressen. Kein sichtbarer Textverlust, keine Überlagerung, kein Randüberlauf und keine isoliert am Seitenende stehende Überschrift wurden festgestellt. Der ergänzte §-6-Absatz im Schulband auf Seite 27 fügt sich ohne Layoutfehler ein. Die Renderprotokolle nennen Times New Roman 11 pt, 1,5-fachen Zeilenabstand und keine manuell eingefügten Seitenumbrüche.

## 1.2 Gesamtakten-PDFs

Alle sechs Gesamtakten wurden auf jeweils sämtlichen 28 Seiten unmittelbar visuell geprüft: insgesamt 168 Seiten. Die Prüfung erfasst TXT- und EML-Wiedergaben, E-Mail-Kopfzeilen, Anlagennamen, Trennblätter, Arbeitsblätter und übernommene Word-Seiten. Die 48 nativen Word-Einzeldokumente waren zuvor bereits mit sämtlichen 48 gerenderten Seiten geprüft worden; diese Vorprüfung wird nicht zusätzlich in die 168 Gesamtaktenseiten eingerechnet.

Die Gesamtakten enthalten jeweils zwei TXT-Seiten, sieben EML-Seiten, ein XLSX-Trennblatt, zwei Arbeitsblattseiten sowie acht Word-Dokumente mit ihren Trennblättern. Nach dem gezielten Tabellenneubau wurden alle zwölf geänderten Arbeitsblattseiten in den aktualisierten Gesamtakten erneut direkt angesehen. Die übrigen Aktenstücke wurden bei der Drucklayoutkorrektur nicht neu erzeugt; die bereits vollständig geprüften Seiten behalten ihre Prüfdeckung.

| Akte | Gesamtseiten | Tabellen im Gesamt-PDF | Ergebnis |
| --- | ---: | --- | --- |
| `berlin-kita-sonnenkringel` | 1–28 | Seiten 11–12, A4 quer | Kein offener Layoutbefund |
| `berlin-professur-berufungszusage` | 1–28 | Seiten 11–12, A4 quer | Kein offener Layoutbefund |
| `berlin-professur-forschungslabor` | 1–28 | Seiten 11–12, A4 quer | Kein offener Layoutbefund |
| `berlin-professur-lehrdeputat` | 1–28 | Seiten 11–12, A4 quer | Kein offener Layoutbefund |
| `berlin-schule-klassenchat` | 1–28 | Seiten 11–12, A4 quer | Kein offener Layoutbefund |
| `berlin-schulplatz-siebte-klasse` | 1–28 | Seiten 11–12, A4 quer | Kein offener Layoutbefund |

## 1.3 Tabellenbefund und Nachprüfung

Die erste Gesamt-PDF-Prüfung zeigte bei elf der zwölf Arbeitsblattseiten eine zu starke Druckverkleinerung; die Schrift fiel überwiegend auf etwa 5,3 bis 7 pt. Der freigegebene Eingriff beschränkte sich auf den aktenbezogenen JavaScript-Tabellenbuilder, die sechs XLSX-Dateien und das Auffrischen der in der Kita-E-Mail eingebetteten XLSX-Anlage. Die Spaltenbreiten wurden für A4 angepasst, Zeilen passend umgebrochen und A4-Querformat mit definierten Druckrändern im OOXML gesetzt. Die Schrift bleibt nativ bei 10 pt.

Die endgültigen Gesamt-PDFs wurden zusätzlich mit pdfplumber geprüft: Alle zwölf Arbeitsblattseiten messen rund 841,89 × 595,30 pt und enthalten durchgehend 10,006-pt-Schrift. Die anschließende direkte Sichtprüfung bestätigt lesbare Tabellen, vollständige Zelltexte und Zahlen, saubere Datumsdarstellung und genügend Innenabstand. Es verbleibt kein offener Tabellenbefund.

Die Erhaltungsprüfung bestätigt 377 unveränderte Zellinhalte einschließlich 35 Formeln mit ihren gespeicherten Ergebnissen und Zelltypen. Die 107 übrigen Original- und README-Dateien blieben bei dieser Reparatur bytegleich; ausgenommen waren die sechs XLSX und die bewusst aufgefrischte Kita-E-Mail. Alle acht eingebetteten MIME-Dateianlagen stimmen bytegenau mit den zugehörigen Originaldateien überein. Die kanonischen README-Downloadlinks wurden durch den Eingriff nicht überschrieben.

## 1.4 Identität der geprüften Werkstattfassungen

Alle folgenden SHA-256-Werte wurden nach der finalen Sichtprüfung aus den Repository-Dateien ermittelt. Die Quellhashes stimmen mit den jeweiligen abschließenden Renderprotokollen überein.

### 1.4.1 berliner-hochschulrecht-professoren

- `berliner-hochschulrecht-professoren/berliner-hochschulrecht-professoren-werkstatt.md`  
  SHA-256: `62bba69ba6a4824d8d6248e6f2002e435e914d033b8d3a5351b06aec3ed95ebd`
- `berliner-hochschulrecht-professoren/assets/berliner-hochschulrecht-professoren-werkstatt.docx`  
  SHA-256: `cbf36ec6daffe58749725ec1cf0f2f93c6aee81a88e07563100793958c4fd522`
- `berliner-hochschulrecht-professoren/assets/berliner-hochschulrecht-professoren-werkstatt.pdf`  
  SHA-256: `c7fbce3d70dec49f34daa361324a138d314a70c32142dcacbc9a9c0f7c3c96a4`

### 1.4.2 berliner-schulrecht-eltern-schueler

- `berliner-schulrecht-eltern-schueler/berliner-schulrecht-eltern-schueler-werkstatt.md`  
  SHA-256: `a6a0d294f7ed989a35a58e20e3ece6bbe893dba02d3de6cbb75d14a3b4205869`
- `berliner-schulrecht-eltern-schueler/assets/berliner-schulrecht-eltern-schueler-werkstatt.docx`  
  SHA-256: `3383488f6fb33aee42ac2c4b97a5b8d736740d1e234b7a802778590b7a80806d`
- `berliner-schulrecht-eltern-schueler/assets/berliner-schulrecht-eltern-schueler-werkstatt.pdf`  
  SHA-256: `ee978d1b9066cca3b40df792025d274437611f4c5047d186fa6778ee3b0ab374`

## 1.5 Identität der geprüften Gesamtakten

- `testakten/berlin-kita-sonnenkringel/gesamt-pdf/berlin-kita-sonnenkringel_gesamt.pdf` — 28 Seiten  
  SHA-256: `cf50757a98ebd47b3f7bf4d1e9a58688e2dda059696aac276b3d9a8a1e17c36a`
- `testakten/berlin-professur-berufungszusage/gesamt-pdf/berlin-professur-berufungszusage_gesamt.pdf` — 28 Seiten  
  SHA-256: `d0df319916f7b207d9e9a62028ca3652cb7d52a4ebba9fafd4361de9c980faae`
- `testakten/berlin-professur-forschungslabor/gesamt-pdf/berlin-professur-forschungslabor_gesamt.pdf` — 28 Seiten  
  SHA-256: `c693769ab77a59db8f9d49d3a9aa37e377528382937d4abf97e505b10f80955a`
- `testakten/berlin-professur-lehrdeputat/gesamt-pdf/berlin-professur-lehrdeputat_gesamt.pdf` — 28 Seiten  
  SHA-256: `f24882a78a4a81745470979e3dca1ee6fce6c411b37daa7e4bc95c32469afabb`
- `testakten/berlin-schule-klassenchat/gesamt-pdf/berlin-schule-klassenchat_gesamt.pdf` — 28 Seiten  
  SHA-256: `3f1987d7b65665028789334851e204e1b43282e6a92f86454912bd5b7f5e9df0`
- `testakten/berlin-schulplatz-siebte-klasse/gesamt-pdf/berlin-schulplatz-siebte-klasse_gesamt.pdf` — 28 Seiten  
  SHA-256: `2c11faa3e7b98846d043ecf36892e745a8f280b0bfeaec679ae1f2de607097a0`

## 1.6 Reichweite des Ergebnisses

Das Ergebnis belegt die visuelle Lesbarkeit und die oben beschriebenen technischen Erhaltungsprüfungen der festgehaltenen Dateien. Es ist keine erneute vollständige juristische Quellenprüfung und kein Nachweis für Modellverhalten oder Plugin-Funktionalität. Die Layoutprüfung erforderte nach der Tabellenkorrektur keine weiteren Änderungen an Rohakten oder Werkstatttexten.
