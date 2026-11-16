# Prüfung der zehn großen Anfechtungswerkstätten

## 1. Fachliche Quellenprüfung

Die zehn eigenständigen Prompts zu §§ 130–139 InsO wurden am 15. November 2026 erstellt und anhand der in den Einzelberichten bezeichneten amtlichen Originale geprüft. Die Berichte benennen gelesene Abschnitte, konkrete Aussage und Grenze. Ein Abruf ohne Lektüre wird nicht als fachliche Prüfung ausgegeben. Literaturfundstellen werden nicht aus Gedächtnis ergänzt.

- [§§ 130–133: Quellen und gelesene Randnummern](130-133-quellen.json).
- [Gegenlese §§ 134–136 und nachgeprüfte Korrektur](gegenlese-134-136-durch-130-133.md).
- [§§ 134–136: Quellenbericht](134-136-quellen.md) und [Originalnachweise](134-136-quellen.json).
- [§§ 137/139: Quellen und Originalhashes](137-139-quellen.json) und [unabhängige Gegenlese](gegenlese-137-139.md).
- [§ 138: Fachprüfung](audit-138.md) und [Originalnachweise](audit-138.json).
- [Technische Gegenlese der Releaseintegration](technische-gegenlese-release.md).
- [Gesonderter Abgleich der Liquiditäts- und Insolvenzreifeprüfung](../../insolvenz-liquiditaet-2026-11-15/README.md).

Die komprimierten Originale sind unverändert archiviert; im jeweiligen Bericht beziehen sich Originalhashes auf die entpackten Bytes. Frühere Quellenprüfungen und Modellprofile bleiben als historische Prüfstände erhalten. Die Fortschreibung eines Fingerabdrucks nach einem dokumentierten fachlichen Zusatz behauptet keine neue Durchführung älterer Modelltests.

Am 16.11.2026 kam nach Quellenlektüre [BGH, Urteil vom 24.09.2026, IX ZR 65/25, Rn. 8–23](https://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/jb-KORE313232026.zip) zur Einzelwerkstatt nach § 130 InsO hinzu. Der Umfangsbericht und die Repo-Exporte binden diese Fassung. Der frühere [Exportprüfbericht](export-pruefung.json) dokumentiert das veröffentlichte Ausgangspaket vom 15.11.2026.

## 2. Export und Umfang

Der [vom Builder erzeugte Umfangsbericht](umfang.json) bindet jede Markdown-Datei an Hash, Wortzahl und tatsächliche PDF-Seitenzahl. Der Export besteht aus zehn einzelnen PDF-Lesefassungen, zehn Markdown-Dateien, zehn bytegleichen TXT-Dateien, Leserhinweis und demselben Umfangsbericht. Ein Gesamtband enthält die vollständige Folge der zehn PDFs samt Modul-Lesezeichen. Es werden keine künstlichen Seitenumbrüche eingefügt; Satzschrift ist die auf dem Buildrechner legitim verfügbare Times New Roman, 11 pt.

Der Prüfvertrag kontrolliert vollständigen sichtbaren Text einschließlich rechtlich bedeutsamer Zahlen- und Satzzeichen, Quellenlinkziele, Seitenfolge, Schrift und Versions-/Quellenstand. Gezielte Manipulationstests ändern wirkliche PDF-Inhalte und erneuern dabei die bloßen Prüfsummen; auch solche Abweichungen müssen erkannt werden. Die Releaseprüfung vergleicht zusätzlich sämtliche Paketmitglieder bytegenau mit den Quellen.

Je Modul wurden erste, mittlere und letzte Seite tatsächlich als Bild gerendert und visuell geprüft, insgesamt 30 Seiten. Die Stichprobe zeigt klare Überschriften, vollständige Tabellen und freistehende Kopf-/Fußzeilen ohne sichtbaren Textbeschnitt. Die automatisierte Volltextprüfung erfasst alle Seiten; eine visuelle Einzelprüfung jeder Seite wird nicht behauptet.

## 3. Prüfgrenzen

Diese Dokumentation betrifft Quellenlektüre, Gegenlese, Rechen- und Exportkontrollen. Sie ist kein erfolgreicher Live-Modelllauf in ChatGPT oder Claude und keine Garantie eines bestimmten späteren Prozessergebnisses. Die fiktiven Fallvarianten bleiben von echten gerichtlichen Feststellungen getrennt. Bei späterer Verwendung sind neue Normfassungen und einschlägige Entscheidungen erneut zu prüfen.
