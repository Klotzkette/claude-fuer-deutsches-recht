# 1. Prüfstand Kommunale Haftpflicht

Stand: 5. Oktober 2026. Die Prüfebenen sind getrennt dokumentiert; weder eine korrekte Dateistruktur noch eine einzelne Modellprobe belegt allgemeine juristische Fehlerfreiheit.

## 1.1. Fachliche Quellen- und Inhaltsprüfung

[Quellenprüfung](quellenpruefung.md) und [maschinell lesbarer Nachweis](quellenpruefung.json) erfassen zwölf amtliche BGH-Entscheidungen mit konkreten Passagen, Übertragungsgrenzen und Quellenhashes sowie die gezielt geprüften Normen. Eine zweite fachliche Lektüre umfasste die zehn Skills, alle drei Prompts, die Referenzen, die 34 Aktenoriginaltexte und beide Tabellen.

## 1.2. Native Akten und PDFs

[Aktenprüfung](akten-pruefung.json) dokumentiert die drei Akten mit insgesamt 36 Originaldateien, sieben identischen MIME-Anlagen, neun nativ neu berechneten Formelergebnissen, zwei zusätzlichen Eingabevarianten und vollständigem Inhaltsabgleich. Alle unterschiedlichen Druckseiten wurden visuell geprüft; reine RGB-Duplikate sind gesondert ausgewiesen. Die Lesezeichen wurden an den tatsächlichen Dokumentanfängen geprüft. Die dort aufgeführten lokalen Evidenzpfade bezeichnen das Buildprotokoll, keine öffentlichen Downloadlinks.

## 1.3. Reproduzierbare Prüfungen

`scripts/test-kommunale-haftpflicht.py` prüft Originalinventar, vollständige Word-Absätze, E-Mail-Header und bytegleiche MIME-Anlagen, echte Formeln und gespeicherte Rechenergebnisse, kleine Kernbestände, PDF-Lesezeichen und mit `KOMMUNALE_HAFTPFLICHT_ZIPS` beide ZIP-Fassungen. Alle sieben Prüfungen einschließlich Archive wurden ausgeführt und bestanden. ZIPs enthalten die kanonische zweisprachige README; PDFs enthalten keinen solchen Vorspruch.

Zusätzlich bestanden Marketplace-Import, YAML, Pluginstruktur, sämtliche Gesamt-PDF-Bestände, Dokumentqualität, der zentrale README- und Downloadabgleich, Navigation, Promptprofile und Schwerpunktabdeckung. Die strukturelle Prüfung der Testakten meldet keine technischen Fehler; noch nicht ausgeführte juristische Bewertungsfälle bleiben ausdrücklich offen.

## 1.4. Grenzen

Die Akten sind vollständig erfunden. Reale AKHA-Bedingungen, Mitgliedschaften, Rückdeckungsquoten und Deckungssummen wurden nicht unterstellt. Vorführung und fachliche Prüfung einer Rohakte sind von einer realen Schadenregulierung getrennt. Eine Modellprobe wird gesondert dokumentiert und ersetzt weder die Quellenlektüre noch die Prüfung eines wirklichen Vertragsbestands.
