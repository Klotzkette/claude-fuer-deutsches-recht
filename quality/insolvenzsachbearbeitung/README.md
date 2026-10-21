# 1. Qualitätsnachweis Insolvenzsachbearbeitung

Diese Prüfung betrifft `insolvenzsachbearbeitung` 1.0.0, die ergänzten Inhalte des `insolvenzforderungen-checker` 445.35.4 und die vier zugehörigen Testakten. Prüfdatum ist der 21.10.2026. Redaktionelle Prüfung, ausgeführte technische Tests und Modellanwendungsprobe werden getrennt bezeichnet.

## 1.1. Rechtsquellen und fachliche Abgrenzungen

Der [Quellenbericht](quellenpruefung-2026-10-21.md) und die [strukturierte Quellenliste](quellenpruefung-2026-10-21.json) dokumentieren 16 amtlich gelesene Entscheidungsanker und die konkret geöffneten Normtexte. Bei Entscheidungen werden gelesene Randnummern oder Seiten, tragende Aussage und Aussagegrenze angegeben. Eine Suchtrefferanzeige wurde nicht als Volltextlektüre gewertet.

Die redaktionelle Prüfung trennt insbesondere Beschluss und Befugnis, vorläufiges und eröffnetes Verfahren, Kauf und Kommission, vorhandene Ware und Erlös, Aus- und Absonderung, Individualisierung und Belegvollständigkeit sowie Schuldner- und Verwalterwiderspruch. Die KI erstellt interne Prüfungsvorschläge; sie ersetzt keine gerichtliche Feststellung.

## 1.2. Aktenprüfung

Die Prüfmanifeste im [Aktenordner](akten/) weisen jede Originaldatei, ihren Hash und ihre Seitenzuordnung aus. Die vier Akten verwenden eigene fiktive Personen, Verfahren und Geschäftsvorgänge. E-Mails enthalten ihre tatsächlich bezeichneten Anlagen. Die Original-ZIPs bewahren die versionierten Dateien; der Paketmodus erzeugt keine neuen Sachverhaltsangaben.

Bei Familie Haberlein wurden die Personaldaten, Antrags- und Eröffnungsdaten, die gerichtliche Ergänzungsfrist und die interne Beratungsfrist gegengeprüft. Das zunächst unzutreffend genannte Alter Jonnas und zwei Datumswidersprüche wurden berichtigt. Die Excel-Abstimmung zählt interne Kontoüberträge nicht als Einkommen oder Aufwand. Aus 5.018 EUR externen Eingängen und 3.097,40 EUR erfassten Abflüssen ergeben sich 1.920,60 EUR rechnerischer Rest. Dieser Rest wird ausdrücklich weder als vollständiger Haushaltsüberschuss noch als pfändbarer Betrag behandelt. Weitere Ausgabenbelege fehlen bewusst.

Der Gläubigerabgleich zeigt 277.480 EUR einmalig erfasste wirtschaftliche Kreditkonten einschließlich der bekannten Kosten. Persönliche Haftung Fridolins und Lales wird getrennt ausgewiesen. Die jeweiligen Belegstichtage, fehlende Aktualisierungen und ungeklärte Zinsen bleiben sichtbar; Grundschuldnominalbetrag und Hausrückstände werden nicht ungeprüft hinzugerechnet.

## 1.3. Dokumentgestaltung und Tabellen

Die Originaldokumente verwenden Times New Roman, 11 pt. Die Office-Dokumente wurden mit dem gebündelten LibreOffice-Renderer in PDF umgesetzt. Die XLSX-Dateien wurden mit dem Artifact Tool erstellt. Änderungen an ausgewählten Eingaben wurden tatsächlich gerechnet, ihre Folgewirkung kontrolliert und danach zurückgesetzt. Originale, Gesamt-PDF und Einzel-PDF-Pakete werden auf Vollständigkeit und korrekte Anlagenbytes geprüft. Der Linux-Workflow darf bei fehlender Times New Roman Liberation Serif verwenden und weist diese Ersatzschrift im Buildbericht aus.

## 1.4. Prüfbefehle und Grenzen

Die lokale Abschlussprüfung wurde am 21.10.2026 mit dem gebündelten Python und Node ausgeführt. Die vier Akten umfassen 123 Originaldateien und 124 PDF-Seiten. Der Komponentenbau erzeugte 39 Assets. Alle sieben MD-/TXT-Promptpaare sind byteidentisch; die sieben PDF-Lesefassungen wurden auf vollständigen Prompttext, Glyphen und Seitenränder geprüft. Die Werkstatt hat 21 Seiten, die Verbraucherwerkstatt neun und die Forderungsprüfer-Werkstatt 16 Seiten. Die vier kompakten Lesefassungen haben jeweils zwei Seiten.

| Prüfung | Ergebnis | Umfang |
| --- | --- | --- |
| `test-insolvenzsachbearbeitung.py --dist <Releaseordner>` | Sieben Tests bestanden | Elf Skills, sieben Promptpaare, Versionen, vier Akten, Rechenwerte und 39 Release-Dateien. |
| `test-insolvenzsachbearbeitung-betriebsakten.py --repro <Vergleichsordner>` | Bestanden | Drei Betriebsakten, tatsächliche MIME-Anlagen und identische Wiederholungsprodukte. |
| `test-insolvenzforderungen-checker.py`, Bäckerei- und Asset-Deal-Tests | Bestanden | Bestehende Forderungsprüfer-Funktionen und frühere Akten. |
| `test-insolvenzforderungen-export.py` | Tests bestanden, eine optionale Integration ausgelassen | Die XJustiz-XSD-Prüfung benötigt eine separat bereitgestellte XSD; sie wurde nicht als ausgeführt gewertet. |
| Struktur, Marketplace, YAML, Skillaktivierung und Markdown | Bestanden | 308 Plugins; keine neuen Struktur- oder Aktivierungsfehler. |
| `quality_lab.py audit --require-editorial --require-workflow` | Bestanden | Qualitätsprofile und aktuelle Prompt-Hashes. |
| Schnellstart-, Portable-Start-, Promptöffnungs- und Routingprüfungen | Bestanden | Promptgrenzen, Startlogik und Rollentrennung. |
| Navigationsscan und 51 Navigationstests | Bestanden | 43.963 lokale Links, 2.207 Anker und 113.334 Markdown-Downloadverweise. |
| Akten-README-Downloadprüfung und Root-Übersicht | Bestanden | Neue Akten auffindbar; bestehende Downloadziele erhalten. |

Die [fünf Forderungsanmeldungen](anwendungsprobe-fuenf-anmeldungen.md) wurden als textuelle Anwendungsprobe mit einzelnen Prüfungsvorschlägen, Betragsabgleich und ausformuliertem Nachforderungsbrief bearbeitet. Die [Betriebsaktenprüfung](akten/betriebsakten-qa.md) nennt die tatsächlich geöffneten Dokumente und die Grenze ihrer Sichtprüfung. Die Verbraucherakte wurde zusätzlich auf getrennte Verfahren, Belegstichtage, Fristen und die Nicht-Doppelzählung interner Überträge geprüft.

Die gemeinsamen ZIP- und PDF-Prüffunktionen bestätigen Archivintegrität, Hinweistext, zulässige Dateinamen, PDF-Inhalt und A4 für alle vier Akten. Die Komponentenarchive enthalten gemäß Pflichtstruktur des Testakten-Qualitätsstandards ausschließlich Originale und README; das Gesamt-PDF ist ein eigenes Asset. Der allgemeine Repository-Validator erwartet dagegen zusätzlich ein Gesamt-PDF im Original-ZIP und repo-weite Sammelarchive. Sein vollständiger Hauptlauf wurde deshalb nicht als bestanden behauptet; die Komponentenprüfer kontrollieren den hier ausdrücklich beschriebenen Paketumfang. Bestehende allgemeine Releases werden nicht verändert.

Der ältere Insolvenzanfechtungs-Workflow überspringt einen erneuten Paketvergleich nur bei bloßen Aktualisierungen der Marketplace-Zahl in dessen READMEs. Seine fachlichen und Quellenprüfungen bleiben aktiv; bei manuellem Start oder sonstigen Komponentenänderungen baut er regulär.

Eine textuelle Modellanwendungsprobe ist keine unabhängige juristische Freigabe und kein Oberflächentest in Claude Cowork, Codex oder ChatGPT. Reale Gerichtssoftware, XJustiz-Importe, beA-Versand, Kontozugriffe und Auszahlungen waren nicht Gegenstand dieses Durchlaufs.
