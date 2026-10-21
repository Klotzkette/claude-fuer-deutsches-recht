# 1. Prüfung der neuen Anfechtungsakten

Prüfstand: 21.10.2026. Die Akten Blechliebe Bamberg und Faltenwurf Fürth enthalten jeweils 24 Originaldateien und 24 PDF-Seiten. Die JSON-Dateien in diesem Ordner dokumentieren Originaldateien, SHA-256, Einzel- und Startseiten. Diese Prüfdateien gehören nicht in die Akten-ZIPs.

## 1.1. Inhalt und Formate

Blechliebe enthält sechs Word-Dateien, sieben PDF-Belege, sieben E-Mails, zwei Excel-Arbeitsmappen und zwei Textdateien. Faltenwurf enthält sechs Word-Dateien, acht PDF-Belege, sechs E-Mails, zwei Excel-Arbeitsmappen und zwei Textdateien. Die E-Mails besitzen MIME-Köpfe, reservierte Kontaktadressen und bei bezeichneten Anlagen die tatsächlichen Originalbytes. Die eingebetteten Dateien wurden gegen die selbständigen Originale verglichen.

Der Versandvermerk vom 12.05.2026 in der Sicherungsabtretung vom 08.05.2026 ist ausdrücklich als nachträglicher Vermerk ausgewiesen. Minna Eberlein arbeitet in der Insolvenzkanzlei; Alina Kessel bleibt die Buchhalterin der Faltenwurf GmbH. Beide Rollen werden nicht vermischt.

## 1.2. Excel und Lesefassungen

Vier Arbeitsmappen wurden mit artifact-tool erstellt. Alle Formelzellen sind vorhanden und berechnet; die Fehlersuche fand keine Excel-Fehlerwerte. Je Arbeitsmappe wurde eine Eingabe um 100 Euro verändert, die entsprechende Änderung des Ergebnisses geprüft und die Eingabe anschließend wiederhergestellt. Die Ergebnisse betragen 8.700,00 Euro offene Lieferantenforderungen, 34.140,00 Euro Zahlungseingänge, 200.000,00 Euro verbleibende Darlehens- und Auslagenkonten und 17.000,00 Euro Bankrestkapital. Kategorien und Grenzen der jeweiligen Berechnung stehen in der Arbeitsmappe.

Datumszellen enthalten echte Excel-Datumswerte; Beträge bleiben numerisch. Das explizite deutsche Zahlenformat wurde im nativen Office-PDF kontrolliert. Der Vorschau-Renderer von artifact-tool stellt Datumsserien und Gebietsschema teilweise abweichend dar; maßgeblich für die Sichtkontrolle waren deshalb zusätzlich die tatsächlichen Office-Lesefassungen. Die vier Arbeitsmappen drucken auf jeweils eine vollständige Seite, einschließlich ihrer Erläuterungen.

Alle zwölf Word-Dateien wurden mit render_docx.py gerendert und die Seitenbilder angesehen. Die Gesamtakten wurden seitenweise als Bilder gerendert und im Überblick kontrolliert; die Excel-Seiten zusätzlich einzeln. Eine Prüfung aller 48 PDF-Seiten ergab keine Schrift außerhalb der Seitengrenzen. Times New Roman ist in dieser Buildumgebung vorhanden. Kein Original-PDF und keine PDF-Lesefassung enthalten den Testakten-Warnhinweis; dieser steht vor den Downloads und in der README.txt jedes ZIPs.

## 1.3. Wiederholbarer Paketbau

`python3 scripts/build-insolvenzanfechtung-akten.py --package-only --dist <Zielordner>` benötigt LibreOffice und die Python-Bibliotheken des Repositorys, jedoch weder artifact-tool noch einen Node-Lauf. Word und Excel werden aus den vorhandenen Originalen nativ konvertiert; E-Mail- und Text-Lesefassungen entstehen aus den gespeicherten Originalbytes. Die JSON-Vorlage bestimmt lediglich Dateiauswahl und Katalogbeschreibung. E-Mail-Anlagen werden nicht doppelt in das Gesamt-PDF übernommen.

Zwei aufeinanderfolgende Paketläufe lieferten identische SHA-256-Werte der Release-Dateien und ließen alle 48 Originale unverändert. Jedes der vier ZIPs enthält genau 24 Unterlagen sowie README.txt. Die Originaldateien in den ZIPs stimmen mit den SHA-256-Werten der Prüfmanifeste überein. Gesamt-PDF und Einzel-PDF-ZIP enthalten jeweils 24 Dokumente mit insgesamt 24 Seiten.
