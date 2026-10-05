# 1. Prüfstand Kommunale Haftpflicht

Stand: 5. Oktober 2026. Die Prüfebenen sind getrennt dokumentiert; weder eine korrekte Dateistruktur noch eine einzelne Modellprobe belegt allgemeine juristische Fehlerfreiheit.

## 1.1. Erstprüfung der drei ursprünglichen Akten

[Quellenprüfung](quellenpruefung.md) und [maschinell lesbarer Nachweis](quellenpruefung.json) erfassen zwölf amtliche BGH-Entscheidungen mit konkreten Passagen, Übertragungsgrenzen und Quellenhashes sowie die gezielt geprüften Normen. Eine zweite fachliche Lektüre umfasste die zehn Skills, alle drei Prompts, die Referenzen, die 34 Aktenoriginaltexte und beide Tabellen.

## 1.2. Ursprüngliche native Akten und PDFs

[Aktenprüfung](akten-pruefung.json) dokumentiert die drei Akten mit insgesamt 36 Originaldateien, sieben identischen MIME-Anlagen, neun nativ neu berechneten Formelergebnissen, zwei zusätzlichen Eingabevarianten und vollständigem Inhaltsabgleich. Alle unterschiedlichen Druckseiten wurden visuell geprüft; reine RGB-Duplikate sind gesondert ausgewiesen. Die Lesezeichen wurden an den tatsächlichen Dokumentanfängen geprüft. Die dort aufgeführten lokalen Evidenzpfade bezeichnen das Buildprotokoll, keine öffentlichen Downloadlinks.

## 1.3. Reproduzierbare Prüfungen

`scripts/test-kommunale-haftpflicht.py` prüft Originalinventar, vollständige Word-Absätze, E-Mail-Header und bytegleiche MIME-Anlagen, echte Formeln und gespeicherte Rechenergebnisse, kleine Kernbestände, PDF-Lesezeichen und mit `KOMMUNALE_HAFTPFLICHT_ZIPS` beide ZIP-Fassungen. Alle sieben Prüfungen einschließlich Archive wurden ausgeführt und bestanden. ZIPs enthalten die kanonische zweisprachige README; PDFs enthalten keinen solchen Vorspruch.

Zusätzlich bestanden Marketplace-Import, YAML, Pluginstruktur, sämtliche Gesamt-PDF-Bestände, Dokumentqualität, der zentrale README- und Downloadabgleich, Navigation, Promptprofile und Schwerpunktabdeckung. Die strukturelle Prüfung der Testakten meldet keine technischen Fehler; noch nicht ausgeführte juristische Bewertungsfälle bleiben ausdrücklich offen.

## 1.4. Grenzen

Die Akten sind vollständig erfunden. Reale AKHA-Bedingungen, Mitgliedschaften, Rückdeckungsquoten und Deckungssummen wurden nicht unterstellt. Vorführung und fachliche Prüfung einer Rohakte sind von einer realen Schadenregulierung getrennt. Eine Modellprobe wird gesondert dokumentiert und ersetzt weder die Quellenlektüre noch die Prüfung eines wirklichen Vertragsbestands.

## 1.5. Erweiterung um die Geburtsschadenakte

Die [ergänzende Quellenprüfung](geburtsschaden-quellenpruefung.json) betrifft den Klinikworkflow und die vierte Akte. Zwei weitere BGH-Originale wurden direkt heruntergeladen und an den angegebenen Randnummern gelesen: VI ZR 186/08, Rn. 18–21, zur Erwerbsprognose bei früh geschädigten Kindern und VI ZR 377/17, Rn. 14, zur Angehörigenpflege. Die Erweiterung berücksichtigt § 1643 Abs. 5 BGB, die konkrete Elternvertretung und den Standard im Behandlungszeitpunkt. Öffentliche AKHA-/KSA-Darstellungen belegen nur die beschriebene Struktur; sämtliche Vertragswerte der Testakte sind erfunden.

Die vierte Akte enthält 18 Originaldateien. Die bisherige Aktenprüfung und ihre Dateihashes bleiben als abgegrenzter Erststand erhalten. Die zusätzlichen fachlichen Kriterien im Evaluationsprofil behandeln das bereits gezahlte Vergleichskapital, die getrennte Drittregressreserve, die Bezugsgröße der Priorität und die offenen internen Erstattungen. Solche Kriterien sind keine automatisch bestandenen juristischen Modelltests.

Die [ergänzende Aktenprüfung](geburtsschaden-aktenpruefung.json) hält 35 Gesamt-PDF-Seiten und 22 Seiten in 18 Einzel-PDFs fest. Alle 40 unterschiedlichen Druckseiten wurden betrachtet; 17 weitere Seiten sind anhand vollständiger RGB-Pixel identisch. Zwölf Word-Dokumente mit 13 Seiten wurden zusätzlich im Word-Renderer geprüft. Alle 17 Textoriginale wurden vollständig mit den Einzel-PDFs abgeglichen, vier MIME-Anlagen mit ihren Originalen verglichen und die Tabelle in sechs Calc-Szenarien neu berechnet. Die sechs neuen Integritätsprüfungen und die sieben bisherigen einschließlich ZIP-Prüfung bestanden.

## 1.6. Acht zusätzliche kommunale Alltagsakten

Die [ergänzende Quellenprüfung](alltagsakten-quellenpruefung.json) dokumentiert elf amtliche Entscheidungsanker mit gelesenen Passagen, Direktquellen, Dateihashes und konkreten Übertragungsgrenzen. Die Fachgegenprüfung betrifft alle 76 neuen Originaltexte, die neue Werkstatt-Ergänzung ab Abschnitt 1.40 und die drei ergänzten Skills. Frühere Werkstattabschnitte und die beiden kompakten Prompts bleiben unverändert. Bayerischer Straßenhaftungsweg, Genehmigungsverfahren und die seit 01.01.2025 geltende Erweiterung der Verfahrensfreiheit wurden zeitbezogen geprüft; ein Abruf oder eine Zeitschriftenfundstelle von 2026 macht aus einer älteren Entscheidung kein neues Urteil.

Die acht Fälle behandeln Fahrzeugschaden, Glatteis, privatrechtlichen Badbetrieb, fehlerhafte Sondernutzungsbearbeitung, Bauversagung, Beschädigung eines städtischen Kanals, aktive Baumpflege und Schlagloch. Die Rohakten enthalten keine Musterlösung. Pro Akte erlauben vier bis sechs Kernunterlagen einen kleinen Einstieg; neun oder zehn Originale bilden den gesamten Arbeitsbestand.

`scripts/test-kommunale-alltagsakten.py` prüft den vollständigen Originaltext, MIME-Anlagen, Zeitstempel, PDF-Inhalte und Lesezeichen sowie beide flachen ZIP-Varianten. Der [Altbestandsnachweis](alltagsakten-altbestand.json) schützt alle 58 Original-/Gesamt-PDF-Dateien der vier bisherigen Akten gegenüber v445.31.1. Alle sechs neuen Prüfungen einschließlich Archive wurden ausgeführt und bestanden. Die zusätzlichen fachlichen Kriterien sind offene Maßstäbe für spätere Anwendungsprüfungen, kein behaupteter erfolgreicher Modelllauf.

Die [Aktenprüfung der Erweiterung](alltagsakten-aktenpruefung.json) erfasst 119 Gesamt-PDF-Seiten und 76 Einzel-PDF-Seiten. Alle 152 unterschiedlichen Seitenbilder wurden visuell betrachtet, weitere 43 Seiten sind nach vollständigem RGB-Vergleich identisch. Zusätzlich wurden alle 43 Word-Seiten geprüft. 16 echte MIME-Anlagen stimmen mit den separat gespeicherten Originalen überein.
