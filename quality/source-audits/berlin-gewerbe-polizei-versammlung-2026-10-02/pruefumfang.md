# 1. Prüfungsumfang der drei neuen Berliner Plugins

Stand: 2. Oktober 2026. Die fachlichen Quellenprotokolle und die unabhängige Gegenprüfung stehen daneben. Die Prüfung betrifft diese drei neuen Plugins; daraus folgt keine Neubewertung sämtlicher älterer Rechtsgebiete im Repository.

## 1.1. Tatsächliche Anwendungsproben

Ein zuvor nicht an der Erstellung beteiligter Agent hat drei vollständige Antworten erstellt: den Gewerbe-Mini-Prompt mit der Abendfuchs-Akte, den ASOG-Hauptskill mit der Lastenradakte und die Versammlungswerkstatt mit dem Kiezcamp. Bewertungsrubriken und fremde Prüfberichte wurden dabei nicht gelesen. Die tatsächlichen Ausgaben und die Provenienz liegen unter `anwendungsproben/`; sie sind Evaluatorunterlagen und kein Teil der Akten- oder Plugin-Downloads.

Beobachtet wurden vollständige Behördenentwürfe und konkrete Rückfragen. Die Bearbeitung erkannte insbesondere den Feiertag am Samstag, 3. Oktober, die zeitliche Kollision zwischen Lastenradabholung und erster Lieferung sowie die unvereinbaren Abholangaben im Campmaterial. Unbekannte Toilettenmaße und noch fehlende Nachtbegründung wurden nicht erfunden. Kein Versand oder gerichtlicher Schritt fand statt.

Diese drei qualitativen Einzelanwendungen fanden in einer Agentensitzung statt. Die Prompts enthalten teilweise sehr ähnliche Fallbeispiele. Das ist keine statistische Modellbewertung und insbesondere keine unabhängige Prüfung der Übertragbarkeit auf ungesehene Fälle. Die Abschluss-Hashes der Eingaben werden von tatsächlich erfassten Erstlektüre-Hashes unterschieden; während der Prüfung vorgenommene reine Tabellenformatkorrekturen wurden gegen die Zellwerte und Formeln abgeglichen.

## 1.2. Dokumente und Lesefassungen

Neun Akten enthalten 162 native Arbeitsdateien. Die neun Gesamt-PDFs umfassen 252 Seiten; 162 Einzel-PDFs enthalten 171 Seiten. Alle finalen PDF-Seiten wurden lesbar visuell geprüft, wobei bereits geprüfte identische Seiten nur nach belegter Pixelidentität dedupliziert wurden. Befunde zu Spaltenabständen und Uhrzeitdarstellung wurden in den Originaltabellen und PDF-Ausgaben korrigiert und nachgeprüft. Die drei Werkstatt-Lesefassungen umfassen 30, 39 und 36 Seiten; auch sie wurden vollständig visuell geprüft. Die Nachweise unter `visuelle-pruefung/` enthalten Hashes; die dort als lokale Prüfartefakte bezeichneten PNGs gehören nicht zum Repository-Download.

Die Excel-Erzeugung prüft gespeicherte Ergebniswerte und gezielte Eingabeänderungen. Tatsächliche MIME-Anlagen werden gegen ihre Originale abgeglichen. Testaktenhinweise stehen auf den Downloadseiten und in den ZIP-READMEs, nicht in den PDF-Dokumenten. Das ASOG-Hauptproblem erhielt bei der Integration vier dezimale Abschnittsüberschriften; der fachliche Inhalt blieb dabei unverändert, der Hash wurde nachgeführt.

## 1.3. Technische Freigabe

Alle 106 technischen Prüfbefehle sind im finalen Stand bestanden; die anfänglichen Integrationsbefunde und ihre erneute Prüfung sind in `technische-pruefungen.json` getrennt vermerkt. Die Repository-Validatoren prüfen Struktur, Frontmatter, Versionen, Navigation, Promptgrenzen, Paketinhalt und Aktenexport. Solche Prüfungen sind keine rechtliche Richtigkeitsgarantie. Die redaktionellen Fallkriterien bleiben gesondert und werden nicht durch einen bestandenen technischen Durchlauf als fachlich bestanden ausgegeben. Nach der endgültigen Zusammenführung werden Downloadarchive mit dem veröffentlichten Quellstand und den öffentlich erreichbaren Assets abgeglichen.
