# 1. Prüfung der Warendorfer Vertiefung

## 1.1. Umfang und Aktenstand

Die Akte enthält 43 Originaldateien. Die 30 bisherigen Originale wurden nicht geändert. Ergänzt wurden vier DOCX, drei PDF, drei EML und drei XLSX. Damit stehen fünf Excel-Arbeitsmappen zur Verfügung. Der Aktenstichtag bleibt der 25. September 2026 um 16:00 Uhr. Spätere Lieferungen, Zahlungen, Prüfungen oder Freigaben werden ausschließlich als geplante oder noch offene Vorgänge beschrieben.

Das Gesamt-PDF enthält 83 Seiten. Die 43 Einzel-PDFs enthalten für die 13 neuen Originale zusammen 21 Seiten: zehn Belegseiten und elf Seiten für die drei neuen Arbeitsmappen. Das Originalformat-ZIP enthält 45 Einträge, nämlich 43 Originale, das Gesamt-PDF und die obligatorische README.txt. Das Einzel-PDF-ZIP enthält 44 Einträge einschließlich README.txt. Beide Archive liegen flach unter `/tmp/bauwirtschaft-vertiefung-20261006/dist`.

## 1.2. Belegverbindungen

1. Die Herstellerinformation 31 konkretisiert die Lieferfortschreibung 07. Rückfrage 32 und Vorprüfung 33 unterscheiden verfügbares Ersatzmodul, Funktionsprüfung, Transport und elektrische Anschlussfreigabe. Die rechnerische Leistungsdifferenz ist kein Nachweis der Eignung für Anlaufströme.
2. Ergänzungsangebot 34 trennt Personenstunden, Sicherungswache, zusätzlichen Betriebsstoff, Schallschutz und Mietverlängerung. Anfrage 35 ist bis zum Stichtag unbeantwortet. Freigabevermerk 36 erlaubt vorbereitende Rückfragen und nimmt die Angebote nicht an.
3. Schreiben 40 bestätigt die verwendeten regulären Terminansätze als Planannahmen, beschreibt eine bedingte Beschleunigung und nennt die noch fehlenden Maschinenservicekosten. Die Abendvariante bleibt in der Kostenmappe ohne diesen Preis unvollständig.
4. Vermerk 37 verbindet Rechnung 22, Leistungsfeststellung 23, Buchungen 11 und Bankbestand 24/30. Eine Vorverlagerung der Reserve ist keine Bankzahlung. Die fortgeführte Datumsplanung erfasst den Septemberabschlag nur einmal.
5. Angebot 38 und Schnittstellenantwort 39 vertiefen den unbestellten Druckluftansatz aus 13. Die Zahlungsmappe berechnet die Differenz zwischen neuem Angebot und bisherigem Ansatz aus zwei Eingabewerten. Sie addiert nicht den vollständigen neuen Angebotspreis zum unveränderten Grundplan.

## 1.3. Excelprüfung

Die drei neuen Arbeitsmappen wurden mit `@oai/artifact-tool` erstellt. Jede Mappe hat zwei Blätter. Die Formelzahlen betragen 7, 13 und 40. Eingaben, Quellen, Einheiten, fehlende Werte und Fortführungsschritte sind sichtbar beschrieben. Die historischen Mappen 09 und 10 bleiben unverändert; README und neue Mappen erläutern deren Abgrenzung.

Alle Mappen wurden mit der gebündelten LibreOffice-Laufzeit neu berechnet und mit gespeicherten Ergebnissen ausgeliefert. Vor der Neuberechnung werden Formelcaches entfernt, damit die Mutationstests nicht unveränderte Altwerte prüfen. Die Prüfung verwendet ausschließlich temporäre Kopien und stellt die unveränderte Ausgangsvariante bereit.

Nach dem Office-Speichern setzt das Prüfskript den Autor Klotzkette und die Sprache de-DE erneut in allen drei neuen Arbeitsmappen. Es liest die beiden Eigenschaften anschließend zurück und prüft, dass ausschließlich `docProps/core.xml` geändert wurde. Alle übrigen Dateiteile einschließlich Formeln, gespeicherter Ergebnisse und Drucklayout bleiben bytegleich zum geprüften nativen Ergebnis.

30 positive und negative Mutationstests sind bestanden. Sie betreffen spätere Energietermine, Teil- und Vollfreigaben, fehlende oder negative Dauern, die inaktive Abendannahme, unbekannten und ausdrücklich kostenfreien Service, bepreiste Abendleistung, zusätzliche Mietwochen, Überschreitung des Angebotsrahmens, fehlende Sätze, Septemberreserve, Einplanung der Mobilversorgung, gesonderte Zahlungsfreigabe, fehlende Daten und Preise, doppelte IDs, einen neuen Datensatz, die obere Zeitgrenze, negative Beträge, Abendleistung ohne Service, einen ungültigen Planschalter, fehlende Umsatzsteuer und ein geändertes Druckluftangebot. Vier dieser Negativfälle prüfen den Variantenwert in 41, Termine!B11: leer, Text, 3 und 1,5. Energie, Versuchsdauer und Freigabestatus melden jeweils „Variante prüfen“; Anlauf Linie 1 und Vollbetrieb melden „Eingabe offen“.

Die Basiswerte wurden unabhängig abgeglichen: 2. November als bedingter Anlauf von Linie 1, 7. Dezember als bedingter Vollbetrieb, 36.000 EUR netto für die Tagesvariante, 12.852 EUR brutto Vorauszahlung bei Annahme und 124.860 EUR Endbestand des unveränderten Zahlungsumfangs. Einplanung und Freigabe lösen keine tatsächliche Bankzahlung aus.

## 1.4. Formate und Sichtprüfung

Alle vier neuen DOCX wurden über den kanonischen `render_docx.py` gerendert und vollständig seitenweise geprüft. Die Schrift ist Times New Roman mit 11 Punkt; dezimale Überschriften erhalten einen Leerabsatz. E-Mails haben vollständige Absender-, Empfänger-, Datums-, Nachrichten- und Transportheader. Neue Kontaktadressen verwenden reservierte `.example`-Domains mit entsprechendem Hinweis und Prüfmarker im README.

Alle sechs neuen Tabellenblätter und sämtliche 21 Seiten ihrer finalen Einzel-Lesefassungen einschließlich der zehn neuen Belege wurden visuell geprüft. Die Tabellen nutzen A4 quer und wiederholen ihre Kopfzeilen. Ergebnis- und Quellenspalten der ersten beiden Mappen sind durch eine Leerspalte getrennt. Nach der Sichtprüfung wurden Zeilenhöhen und Zahlenabstände korrigiert; die betroffenen Fassungen wurden erneut gerendert.

Die zentralen Exportfunktionen und Einzelarchiv-Validatoren prüfen vollständige Dateimengen, flache Archive, kollisionsfreie Namen, intakte PDF-Dateien und den unveränderten zweisprachigen Hinweis am Anfang der README.txt. Die PDFs enthalten keinen Warntext. Die Position des Hinweises im Akten-README wurde mit `missing_notice_positions(..., case_readme=True)` geprüft. Die Veröffentlichung und zentrale Release-Verlinkung erfolgen außerhalb dieses Teilauftrags.

## 1.5. Amtliche Quellen

Am 6. Oktober 2026 wurden die amtlichen Fassungen von [Paragraf 12 Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__12.html) und [Paragraf 13b Absatz 2 Nummer 4 sowie Absatz 5 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html) abgerufen. Nach einem Timeout des Browsers wurde die zweite amtliche Einzelnorm direkt vom selben Server gelesen. Die HTML-Datei ist im temporären Prüfverzeichnis erhalten. Der Sachverhalt geht von einer inländischen Bauherrin aus, die Präzisionsteile herstellt und keine nachhaltigen Bauleistungen erbringt. Neue Belege übernehmen die ausgewiesenen Steuerbeträge. Die Ergänzung löst weder die Verantwortlichkeit für den Lieferverzug noch die Zulässigkeit der angefragten Abendzeiten vorab.

## 1.6. Reproduktion

Die folgenden Befehle werden im Repository ausgeführt. Sie verändern ausschließlich die Warendorfer Akte, die vier isolierten Builder und die Warendorfer temporären Prüfdateien. PyYAML liegt tasklokal, nicht in der verwalteten Laufzeit.

```sh
WAR_PY=/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3
WAR_NODE=/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node
export AKTEN_NODE_MODULES=/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules
export PYTHONPATH=/tmp/bauwirtschaft-vertiefung-20261006/python-deps
export SOFFICE=/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/soffice
"$WAR_PY" scripts/vertiefung_warendorf_20261006.py
"$WAR_NODE" scripts/vertiefung_warendorf_20261006_workbooks.mjs
"$WAR_PY" scripts/vertiefung_warendorf_20261006_pruefen.py
"$WAR_PY" scripts/vertiefung_warendorf_20261006_export.py
```

Der Export ruft die zentralen Builder gezielt und ihre vorhandenen `build_single`-Funktionen auf. Er erstellt keine Sammelarchive und ändert keine zentralen Dateien. Maschinenlesbare Nachweise liegen unter `/tmp/bauwirtschaft-vertiefung-20261006/warendorf`: `originale_sha256.json`, `native_mutationstests.json` und `exportbericht.json`. Die visuellen Prüfbilder werden dort getrennt von den auszuliefernden Aktenstücken gehalten.
