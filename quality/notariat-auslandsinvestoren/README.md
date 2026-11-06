# 1. Prüfung der Auslandsinvestorenakten

## 1.1. Gegenstand

Prüfstand: 6. November 2026. Die beiden offenen Notariatsakten enthalten 30 beziehungsweise 28 native Unterlagen. Der Prüfstand umfasst die tatsächlich erzeugten Dateien, die Texte des betroffenen Auslandsurkunden-Skills sowie Werkstatt-, Mini- und Master-Prompt. Zwei zusätzliche synthetische Ergebnisprüfaufträge sind vorbereitet; ein Live-Modelllauf oder eine erfolgreiche automatische Skillauswahl wird nicht behauptet.

## 1.2. Native Dateien und Layout

Zwei vollständige Builderläufe erzeugten alle 58 nativen Dateien byteidentisch. [Native Prüfsummen](native-bestand.json) und [Prüfergebnis je Akte](qa-ergebnis.json) dokumentieren diesen Stand. Die zwölf Worddateien verwenden A4 und Times New Roman 11 pt. Sämtliche Seiten der gerenderten Worddateien, der 31 nativen PDFs und der zwei Tabellen sowie beide Screenshots wurden visuell geprüft: insgesamt 49 Dokumentseiten und zwei Bildansichten. Die gerenderten Worddateien enthalten nachweislich die tatsächliche Times-New-Roman-Familie. Kopf- und Fußzeilen wurden dem jeweiligen Aussteller zugeordnet.

Für den lokalen Office-Export wurde ausschließlich die gebündelte LibreOffice-Laufzeit verwendet. Fontconfig wurde auf die legitim vorhandenen Systemschriften unter `/System/Library/Fonts/Supplemental` eingestellt. Schriftdateien werden nicht mitgeliefert. Der native Builder bricht ab, wenn keine echte Times New Roman verfügbar ist; eine andere Schrift wird nicht umbenannt oder unter ihrem Namen eingebunden.

## 1.3. Lesefassungen und Archive

Die zentralen Werkzeuge erzeugten die Gesamt-PDFs mit 55 Seiten für Mumbai und 52 Seiten für Dubai. Die zusätzlichen Seiten gegenüber den nativen Unterlagen entstehen insbesondere durch die getrennten Dateiabschnitte. Die Originalformat-ZIPs enthalten die nativen Unterlagen und das jeweilige Gesamt-PDF; die Einzel-PDF-ZIPs enthalten genau 30 beziehungsweise 28 Dokument-PDFs. Beide ZIP-Typen bleiben flach und enthalten zuerst die vorgeschriebene README.txt. Warntexte stehen außerhalb der PDFs.

Der Komponentenbuilder prüft die Einzelakten mit den unveränderten zentralen Builder- und Validatorfunktionen. Er baut kein Sammelarchiv aller übrigen Repository-Akten. Der lokale Releasebau erzeugte zwölf Dateien und verifizierte deren tatsächliche Archivmitglieder. `release-bestand.json` und `checksums-sha256.txt` werden aus diesen Dateien erzeugt, nicht aus angenommenen oder nachträglich erfundenen Prüfsummen.

## 1.4. Quellen und fachliche Grenzen

Der [Quellenvermerk](../../notariat-alltag/references/auslandsinvestoren-urkundenverkehr.md) unterscheidet den bilateralen Apostille-Status, eingestellte Legalisation, möglichen Amtshilfeweg und echte Legalisationsvariante. Die Organbestellung wird von einer transaktionsbezogenen Ermächtigung zum Signingzeitpunkt getrennt. Für die gerichtliche Listenprüfung wurde BGH, Beschluss vom 18. März 2025 – II ZB 11/24, Randnummern 33 bis 38, am über DNotI zugänglichen Originaltext geprüft; der direkte BGH-PDF-Abruf war gesperrt.

Die vorhandenen anwaltlichen Eingaben sind Aktenstoff. Sie bestimmen weder den richtigen Rechtsbehelf noch das Ergebnis. Die Beispiele entscheiden nicht abschließend über ausländisches Gesellschaftsrecht, Genehmigung, Rechtsschein oder die Wirksamkeit des konkreten Erwerbs. Behördenkennung, Unternehmen, Personen und Vorgänge der Arbeitsakten sind erfunden.

## 1.5. Repository-Prüfungen

Marketplace-Import, YAML-Frontmatter, Pluginstruktur und Gesamt-PDF-Prüfung bestanden; letzterer Lauf erfasste 606 Akten. Downloadhinweise und Root-Übersicht bestanden. Notariatswerkstatt: zwölf Tests bestanden. Prompt-Einstiege, Routing, Frontmatter und das Qualitätsaudit bestanden; vier nicht betroffene Altprofile behalten ihren dokumentierten Status `needs_review`. Eine neue behauptete Ergebnisbewertung dieser Altprofile erfolgte nicht.

Beim Hinzufügen der zwei Akten verschob die dynamische alphabetische Aufteilung zwei schon veröffentlichte Akten über die Grenze des ersten Begleitreleases. Die vier bestehenden ZIP-Downloads für Großbach und Jänschwalde/Peitz wurden deshalb ausdrücklich auf ihre vorhandenen Assets in `akten-v445.35.3` festgelegt. Die Veröffentlichung dieser vier Assets wurde über die GitHub-Release-Metadaten bestätigt. Ihre Dateien und Tags bleiben unverändert.
