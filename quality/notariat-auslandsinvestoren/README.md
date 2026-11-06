# 1. Prüfung der Auslandsinvestorenakten

## 1.1. Gegenstand

Prüfstand: 6. November 2026, Komponentenstand 445.35.8. Die beiden offenen Notariatsakten enthalten 36 beziehungsweise 34 native Unterlagen. Hinzugekommen sind je eine ausführliche Anfrage an das Deutsche Notarinstitut und fünf Begleitunterlagen zu den weiter erwogenen Vollmachts- und Nachweiswegen. Die Anfrage-PDFs sind jeweils acht Seiten lang und als alleinige Eingabe eines Prüfauftrags verständlich. Vier synthetische Ergebnisprüfaufträge sind vorbereitet; ein Live-Modelllauf oder eine erfolgreiche automatische Skillauswahl wird nicht behauptet.

## 1.2. Native Dateien und Layout

Zwei vollständige aktuelle Builderläufe erzeugten alle 70 nativen Dateien byteidentisch. [Native Prüfsummen](native-bestand.json), der [aktuelle Erzeugungsnachweis](dnoti-pruefung.json) und die [Anfragenprüfung](dnoti-layoutpruefung.json) dokumentieren diesen Stand. Die 58 ursprünglichen Dateien wurden gegen den [unveränderten Bestandsnachweis 445.35.7](ursprungsbestand-445.35.7.json) abgeglichen und sind vollständig byteidentisch erhalten. Die [ursprüngliche Layoutprüfung](qa-ergebnis.json) bleibt als historischer Nachweis bestehen.

Alle 16 Seiten der beiden Anfragen sowie sämtliche sechs neuen Begleit-PDF-Seiten wurden vollständig visuell geprüft. Der Gesamtstand umfasst damit 71 geprüfte native Dokumentseiten und die zwei unveränderten Bildschirmansichten. Die zwölf unveränderten Worddateien verwenden A4 und Times New Roman 11 pt; die Anfrage-PDFs ebenfalls. Ihre Schriftdateien enthalten die tatsächliche Times-New-Roman-Familie. Briefkopf, Adressfeld, Absatz- und Seitenumbrüche sowie die vollständige Paginierung wurden geprüft. Ein vorläufiger Ziffernverdacht in verkleinerten Vorschaubildern wurde durch 300-dpi-Detailrender widerlegt.

Für den lokalen Office-Export wurde ausschließlich die gebündelte LibreOffice-Laufzeit verwendet. Fontconfig wurde auf die legitim vorhandenen Systemschriften unter `/System/Library/Fonts/Supplemental` eingestellt. Schriftdateien werden nicht mitgeliefert. Der native Builder bricht ab, wenn keine echte Times New Roman verfügbar ist; eine andere Schrift wird nicht umbenannt oder unter ihrem Namen eingebunden.

## 1.3. Lesefassungen und Archive

Die zentralen Werkzeuge erzeugten die Gesamt-PDFs mit 72 Seiten für Mumbai und 69 Seiten für Dubai. Die zusätzlichen Seiten gegenüber den nativen Unterlagen entstehen insbesondere durch die getrennten Dateiabschnitte. Die Originalformat-ZIPs enthalten die nativen Unterlagen und das jeweilige Gesamt-PDF; die Einzel-PDF-ZIPs enthalten genau 36 beziehungsweise 34 Dokument-PDFs. Beide ZIP-Typen bleiben flach und enthalten zuerst die vorgeschriebene README.txt. Warntexte stehen außerhalb der PDFs. Die beiden Anfragen werden zusätzlich unmittelbar als PDF ausgeliefert und sind mit ihren Aktenfassungen bytegleich.

Der Komponentenbuilder prüft die Einzelakten mit den unveränderten zentralen Builder- und Validatorfunktionen. Er baut kein Sammelarchiv aller übrigen Repository-Akten. Der ausgeführte Releasebau für 445.35.8 erzeugte und verifizierte 14 Release-Dateien. `release-bestand.json` und `checksums-sha256.txt` werden aus den tatsächlich gebauten Dateien erzeugt. Der Bestandsbericht bindet auch Textquelle und Renderer der Anfragen an ihre SHA-256-Prüfsummen. Frühere Releases und Tags bleiben erhalten.

## 1.4. Quellen und fachliche Grenzen

Der [Quellenvermerk](../../notariat-alltag/references/auslandsinvestoren-urkundenverkehr.md) unterscheidet den bilateralen Apostille-Status, eingestellte Legalisation, möglichen Amtshilfeweg und echte Legalisationsvariante. Die Organbestellung wird von einer transaktionsbezogenen Ermächtigung zum Signingzeitpunkt getrennt. Für die gerichtliche Listenprüfung wurde BGH, Beschluss vom 18. März 2025 – II ZB 11/24, Randnummern 33 bis 38, am über DNotI zugänglichen Originaltext geprüft; der direkte BGH-PDF-Abruf war gesperrt.

Die vorhandenen anwaltlichen Eingaben und notariellen Anfragen sind Aktenstoff. Sie bestimmen weder den richtigen Rechtsbehelf noch das Ergebnis. Die Beispiele entscheiden nicht abschließend über ausländisches Gesellschaftsrecht, Genehmigung, Rechtsschein oder die Wirksamkeit des konkreten Erwerbs. Absender, Beteiligte und Vorgänge sind erfunden. Das Deutsche Notarinstitut und seine Anschrift Gerberstraße 19, 97070 Würzburg, sind reale Empfängerangaben, am 6. November anhand der [offiziellen Kontaktseite](https://www.dnoti.de/kontakt/) geprüft. Es wurde keine Anfrage versandt. Die neuen Vollmachtsvorschläge sind ausdrücklich nicht ausgeführt; eine fachkollegiale Mitprüfung wird nicht als Amtsvertretung oder Amtsnachfolge dargestellt.

## 1.5. Repository-Prüfungen

Notariatswerkstatt: zwölf Tests bestanden; Anfrageprüfung: fünf Tests bestanden. Die Anfrageprüfung liest die tatsächlich erzeugten PDFs und prüft vollständige Textübernahme, Empfängerbereich, alle Seitenzahlen, Quellenlinks und den Erhalt der ursprünglichen Dateien. Eine bloße Zusammenfassung und die vertauschte Länderakte werden ausdrücklich als fehlerhafte Ausgaben zurückgewiesen. Die Tests benötigen zum Lesen der eingecheckten PDFs keine lokal installierte Times New Roman.

Marketplace-Import, YAML-Frontmatter, Pluginstruktur, Downloadhinweise, Root-Übersicht und Qualitätsaudit bestanden. Der aktuelle globale Gesamt-PDF-Lauf erfasste 606 Akten; der gezielte Bau erfasste beide veränderten Akten ohne Fehler. Vier nicht betroffene Altprofile behalten ihren dokumentierten Status `needs_review`. Eine neue behauptete Ergebnisbewertung dieser Altprofile erfolgte nicht.

Beim Hinzufügen der zwei Akten verschob die dynamische alphabetische Aufteilung zwei schon veröffentlichte Akten über die Grenze des ersten Begleitreleases. Die vier bestehenden ZIP-Downloads für Großbach und Jänschwalde/Peitz wurden deshalb ausdrücklich auf ihre vorhandenen Assets in `akten-v445.35.3` festgelegt. Die Veröffentlichung dieser vier Assets wurde über die GitHub-Release-Metadaten bestätigt. Ihre Dateien und Tags bleiben unverändert.
