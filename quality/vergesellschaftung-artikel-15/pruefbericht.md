# Prüfbericht Vergesellschaftung nach Artikel 15 GG

## 1. Stand und Umfang

Prüfdatum: 28.09.2026. Neun eigenständige Skills, lokale Navigation, handverfasste Werkstatt und eigenständig nutzbarer Schnellstart. Der Schnellstart umfasst 7.489 UTF-8-Bytes und liegt damit auch unter der Grenze von 7.500 Zeichen. Das Eval-Profil enthält fünf auftrags- und aktenbezogene Fälle einschließlich Antwortfortsetzung, Quellenreichweiten und redaktioneller SHA-256-Werte für beide Prompts.

Elf native Einzelunterlagen: drei DOCX, drei PDF, zwei EML, zwei CSV und eine TXT. Es wurden keine Musterlösung oder Qualitätsdatei als Aktenstück angelegt. Die CSV-Dateien sind Rohdatenexporte, keine Excel-Rechenmodelle. Die geplante Neuordnung wird in den Belegen als Arbeitsstand beschrieben, nicht als geltendes Landesgesetz.

## 2. Ausgeführte Prüfungen

`python3 scripts/test-vergesellschaftung-artikel-15.py`: 9 Tests bestanden. Enthalten sind lokale Manifest-/Skillstruktur, Eval-Schema und redaktionelle Hashes, vollständiger Bestand, Abgleich der nativen Inhalte mit der Fixture, EML-Header/Datum/Byteidentität, finanzielle Überleitungen, DOCX-Schriftdefinitionen, Kontaktdomains, Sprachregel und lokale Links.

`python3 scripts/test-prompt-publication-profiles.py`: 9 Tests bestanden. Das ist der vorhandene isolierte Publikationsregressionstest, kein globaler Generatorlauf.

Der zusätzliche lokale Manifestvalidator wurde bestanden. Die Integrationsprüfung gleicht die Manifestversionen mit der jeweiligen Marketplace-Version ab.

Es wurde kein Live-Modelllauf durchgeführt. Die fünf Eval-Fälle sind vorbereitete ausführbare Bewertungsfälle, keine behaupteten erfolgreichen Modellantworten. Die automatischen Prüfungen ersetzen die nachstehende Sichtkontrolle nicht.

## 3. Native Sichtkontrolle

Alle 12 Seiten der sechs paginierten Originale wurden als PNG einzeln geöffnet und visuell geprüft:

| Original | Seiten | Renderpfad unter `/tmp/vergesellschaftung-artikel-15-qa/` |
| --- | --- | --- |
| 02 Arbeitsfassung | 1–3 | `02/page-1.png` bis `02/page-3.png` |
| 03 Begründung | 1–2 | `03/page-1.png` bis `03/page-2.png` |
| 05 Beteiligungen und Titelangaben | 1–2 | `05-1.png`, `05-2.png` |
| 06 Eigentümerstellungnahme | 1–2 | `06-1.png`, `06-2.png` |
| 07 Betriebskonzept | 1–2 | `07/page-1.png`, `07/page-2.png` |
| 09 Finanzierungsindikation | 1 | `09-1.png` |

Im ersten DOCX-Render wurden eine geerbte blaue Titellinie und eine themenabhängige abweichende Überschriftenschrift gefunden. Der lokale Builder entfernt diese Vorgaben und setzt auch die Überschriften ausdrücklich in Times New Roman 11 pt. Alle sieben DOCX-Seiten wurden danach erneut gerendert und einzeln angesehen. Ein falscher interner Abschnittsverweis in der Arbeitsfassung wurde vor dem letzten Render von 6 auf 3 berichtigt.

Endbefund: keine abgeschnittenen Zeilen, keine Überlagerung von Kopf-/Fußzeilen und Text, keine fehlenden Umlaute und keine überlaufenden Überschriften. Die fünf PDF-Seiten sind ebenfalls lesbar und vollständig. EML, CSV und TXT sind ungegliederte native Quellformate ohne feste Seitenzahl; sie wurden strukturell und inhaltlich, nicht als vorgetäuschte feste PDF-Seiten geprüft. Die spätere Gesamt-PDF-/ZIP-Konvertierung benötigt ihre eigene Integrationskontrolle.

## 4. Reproduktion

Nur die Originale dieser Akte bauen, vom Repository-Wurzelverzeichnis aus:

```bash
python3 scripts/build-vergesellschaftung-artikel-15-akte.py
```

Der Builder verwendet `scripts/fixtures/vergesellschaftung-artikel-15/case.json` und schreibt ausschließlich die elf dort benannten Originale in den Aktenordner. Mit `--output /tmp/vergesellschaftung-artikel-15-rebuild` ist ein separater Vergleichsbuild möglich. `--font-dir` kann ein Verzeichnis mit den beiden Times-New-Roman-Schriften angeben; ohne Angabe greift die vorhandene portable Schriftwahl.

DOCX-Renderbeispiel; entsprechend für 03 und 07 ausgeführt:

```bash
python3 "$AKTEN_DOCX_RENDERER" testakten/vergesellschaftung-energienetz-hessen/02_Arbeitsfassung_Netzgesetz_20260914.docx --output_dir /tmp/vergesellschaftung-artikel-15-qa/02 --emit_pdf
```

PDF-Renderbeispiel; entsprechend für 06 und 09 ausgeführt:

```bash
pdftoppm -r 120 -png testakten/vergesellschaftung-energienetz-hessen/05_Beteiligungen_und_Titelangaben_20260917.pdf /tmp/vergesellschaftung-artikel-15-qa/05
```

## 5. Amtliche Quellen und Prüfgrenzen

Die vollständige quellenbezogene Reichweitenprüfung steht in `vergesellschaftung-artikel-15/references/vergesellschaftung-quellen.md`. Verifiziert wurden insbesondere [Artikel 15 GG](https://www.gesetze-im-internet.de/gg/art_15.html), [Artikel 72 GG](https://www.gesetze-im-internet.de/gg/art_72.html), [Artikel 74 GG](https://www.gesetze-im-internet.de/gg/art_74.html), die [Hessische Verfassung in der amtlichen Ausgabe April 2026](https://hessischer-landtag.de/sites/default/files/dateien/2026-05/HL_Verfassung_Apr2026_final_web_2.pdf), [Artikel 142 GG](https://www.gesetze-im-internet.de/gg/art_142.html), [Artikel 94 GG](https://www.gesetze-im-internet.de/gg/art_94.html), [Paragraf 7 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__7.html), [Paragraf 46 EnWG](https://www.gesetze-im-internet.de/enwg_2005/__46.html) und die amtlichen [Essent-Leitsätze](https://eur-lex.europa.eu/legal-content/DE/SUM/?uri=celex%3A62012CJ0105).

Die konkreten Aussagen von BVerfG vom 06.12.2016 und 15.10.1997 sowie EuGH Essent werden nicht als unmittelbar bestätigende Artikel-15-Rechtsprechung ausgegeben. Technische Direktabrufgrenzen bei zwei Entscheidungstexten sind im Quellenvermerk ausdrücklich dokumentiert; amtliche Leitsätze beziehungsweise indexierte amtliche Entscheidungspassagen wurden abgeglichen. Historische Durchführungsgesetze, konkrete Grundbuchtitel und sämtliche Konzessions-/Kreditverträge wurden nicht abschließend untersucht. Der Fall lässt diese Belege als realistische Nachforderungen offen.

Ein eigenständiger Digital-Omnibus-Exkurs wurde auf Wunsch entfernt. Betriebsbezogene Leittechnik- und Datenzugangsfragen bleiben ausschließlich soweit sie in der Akte tatsächlich vorkommen.

## 6. Geänderte Pfade und Integration

Fachlicher Lieferumfang: `vergesellschaftung-artikel-15/`, `testakten/vergesellschaftung-energienetz-hessen/`, `scripts/fixtures/vergesellschaftung-artikel-15/case.json`, `scripts/build-vergesellschaftung-artikel-15-akte.py`, `scripts/test-vergesellschaftung-artikel-15.py`, `quality/evals/vergesellschaftung-artikel-15.json` und dieser Prüfbericht. Die globale Integration wird zusätzlich geprüft.

Die zentrale Integration erzeugt Gesamt-PDF, Originalformat-ZIP, Einzel-PDF-ZIP und Downloadlinks. In beide ZIP-Wurzeln gehört die unveränderte zweisprachige `README.txt`; weder Warnseiten noch Bewertungsunterlagen gehören in die PDFs. Die technische Rubrik erwartet das Gesamt-PDF erst nach diesem Schritt. Das Originalinventar umfasst exakt die elf in der Fixture benannten Dateien, nicht README, Rubrik, Quellen, Fixtures oder Qualitätsprofil.

Werkstatt und Schnellstart sind handkuratiert und zentral gegen Überschreiben geschützt. Die redaktionellen Hashes dürfen nur nach neuer Prüfung geändert werden.
