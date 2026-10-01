# 1. Rechtsprechungsanker: dritter Prüfdurchgang am 01.10.2026

## 1.1. Ergebnis und Umfang

Ausgangspunkt ist main `3fcd595306f5fcb686db7c68cde57542204fed2d` (v445.20.2). Der Durchgang ergänzt die beiden Prüfungen vom 30.09.2026. Alle 258 Plugins wurden im Bestands- und Profilabgleich erfasst; fachlich vertieft wurden elf Plugins. In weiteren 36 Plugins wurden nach Abgleich von Gericht, Datum und Aktenzeichen veraltete Quellenadressen ersetzt. Es wurden keine zusätzlichen Skills angelegt und keine Testakten geändert.

**Sieben neu geprüfte Entscheidungen aus 2026** sind fachbezogen in die jeweils einschlägigen Skills und Promptfassungen eingeflossen. Werkstatt, Mini und Hauptproblem wurden dort angeglichen, wo die Entscheidung den konkreten Arbeitsweg betrifft. Ein fachfremder Hauptproblem-Prompt erhält keinen bloßen Aktualitätsabsatz. Bestehende Rückfragen und Abläufe bleiben erhalten.

Dies ist ein repositoryweiter Bestandsabgleich mit gezielten materiellen Vertiefungen, keine vollständige Neuzertifizierung aller 24.730 erfassten Markdown-Dateien. Unveränderte Anker behalten den früher dokumentierten Prüfstatus. Technische Tests ersetzen keine rechtliche Quellenprüfung.

## 1.2. Neue Entscheidungen und konkrete Anwendung

| Fachgebiet | Entscheidung | Eingebaute Prüfung |
| --- | --- | --- |
| Bau- und Architektenrecht | BGH, 15.01.2026 – VII ZR 119/24 | Prüfung übernommener Fremdplanung, konkrete Planungs-/Überwachungsaufgabe und Mitwirkung; keine automatische Haftungsquote oder HOAI-Phasenzuordnung. |
| Mietrecht | BGH, 01.07.2026 – VIII ZR 50/23 | Erstmalige Nutzung nach wesentlicher Wiederherstellung zuvor unbewohnbaren Wohnraums; kein pauschaler Ausschluss der Mietpreisbremse allein wegen hoher Kosten. |
| Sozialrecht | BSG, 18.06.2026 – B 3 KR 2/25 R | Hilfsmittelbedarf anhand konkreter Wege, Fähigkeiten, Sicherheit und Alternativen; keine automatische Bewilligung des Wunschmodells. |
| Einziehung | BGH, 08.01.2026 – 3 StR 203/25 | Tatsächlicher Zugriff auf eingelagerte Beute statt bloßer Wohnungsinhaberschaft oder Mittäterschaft. |
| Strafzumessung | BGH, 24.02.2026 – 5 StR 623/25 | Bloße Mittäterschaft nicht nochmals strafschärfend werten; konkrete zusätzliche Ausführungsmerkmale gesondert prüfen. |
| Strafbefehl | LG Nürnberg-Fürth, 24.07.2026 – 12 Qs 43/26 | Grenzen einer inhaltlichen Ergänzung nach Rechtskraft; keine Gleichsetzung mit allgemeiner Nichtigkeit. |
| Steuerrecht | BFH, 15.04.2026 – X R 14/24 | Geeigneten inneren Betriebsvergleich vor externer Richtsatzschätzung erwägen; Fehler der Methodenwahl beseitigen die Schätzungsbefugnis nicht automatisch. |

Amtliche Links, gelesene Randnummern, Übertragungsgrenzen und geänderte Fachdateien stehen in den drei Berichten:

- [Bau- und Mietrecht](bau-und-miete.md), einschließlich Korrektur falscher WEG-Fundstellen, Anfechtungsfristen und Abnahmefiktion.
- [Sozialrecht und neue Sprachplugins](sozial-und-neue-plugins.md), einschließlich E-Mail-Widerspruch, Kommunikationshilfen und konkreter Hilfsmittelnormen.
- [Straf- und Steuerrecht](straf-und-steuer.md), einschließlich Berichtigung des Strafbefehls-Sanktionskatalogs und der Normzuordnung zur Strafzumessung.

## 1.3. Quellenadressen und Entscheidungsidentität

Aus allen 258 Profilen wurden zunächst 412 Quellenzuordnungen mit 343 unterschiedlichen URLs abgerufen. 39 alte BGH-Adressen waren unbrauchbar oder nicht erreichbar. Für jede davon wurde ein amtliches PDF geladen und dessen Entscheidungskopf abgeglichen. Die neuen Adressen stehen in 68 Fachdateien von 32 Plugins sowie in insgesamt 36 Pluginprofilen. Dieser Linkersatz ist ausdrücklich keine erneute Prüfung sämtlicher Entscheidungsgründe.

- [Quellenbericht mit allen 39 Entscheidungsidentitäten](quellenlinks.md)
- [Abrufregister und Zugriffsgrenzen](quellen-erreichbarkeit.json)
- [Bestätigte BGH-Ersatzadressen mit Prüfsummen](bgh-linkersatz.json)
- [Geänderte Dateien des Linkersatzes](linkaenderungen.json)

49 EUR-Lex-Adressen lieferten beim technischen Abruf keinen Inhalt; ein zusätzlicher Browserabruf zeigte eine JavaScript-/Robot-Prüfung. Weitere Portalfehler bleiben als Abrufgrenzen dokumentiert. Sie wurden weder als Bestätigung noch als Beweis falscher Rechtsprechung behandelt.

## 1.4. Bestand und technische Prüfung

[bestand.json](bestand.json) vergleicht Profile und Promptdateien mit dem [zweiten Prüfdurchgang vom 30.09.2026](../2026-09-30-zweiter-durchgang/README.md). Das Inventarskript unterstützt hierfür jetzt `--baseline-inventory`; der bisherige Standardvergleich bleibt erhalten. Die Prüfsumme des gesamten Dateiinventars enthält auch Vergleichsstatus und ist daher kein vom Ausgangsregister unabhängiger Inhaltsfingerabdruck. Einzelne Profil- und Dateiprüfsummen sind unverändert direkt vergleichbar.

[pruefungen.json](pruefungen.json) dokumentiert Generatoren, Konsistenzprüfungen, bestehende Regressionstests und die lokal erzeugten Plugin-/Markdown-Pakete mit tatsächlichen Ergebnissen. Es wurden keine neuen Live-Modelltests durchgeführt.

Abschluss: sieben Generatoren erfolgreich, 19 Prüfkommandos und beide Paketvalidatoren bestanden. Nach der letzten fachlichen Korrektur wurden Profilhashes, Frontmatter, Markdown-Struktur und Diff erneut geprüft. Die zunächst zu langen Strafrecht-/Steuerrecht-Hauptproblem-Prompts wurden gekürzt; auch der Schwerpunkt-Generator bestand danach. Alle 258 lokalen Plugin-ZIPs entsprechen den Paketregeln. Der [Inventar-Gegenlauf](inventar-pruefung.json) bestätigt 258 unveränderte Profile und 804 unveränderte Promptdateien beim Vergleich des Endregisters mit sich selbst.

[aenderungen.json](aenderungen.json) enthält die Prüfsummen der 167 geänderten Bestandsdateien. Unter den eigenständigen Prompts wurden 43 Werkstatt-, 38 Mini- und sechs Hauptproblem-Dateien aktualisiert. Vier der 47 betroffenen Pluginprofile brauchten ausschließlich eine Quellenadresskorrektur im Profil; Fachdateien wurden insgesamt in 43 Pluginverzeichnissen geändert.

Die bestehenden 100-seitigen Bauwirtschaft-Hauptwerkstattfassungen in Markdown, DOCX und PDF wurden in diesem Durchgang nicht neu bearbeitet oder gerendert. Der neue Bauanker ist in der Quellenreferenz, im Mini sowie in den einschlägigen LPH-5-/8-Skills und deren eigenen Werkstatt-Prompts eingearbeitet. Die frühere Prüfung der Hauptwerkstatt wird dadurch nicht neu datiert.

Diese Änderung aktualisiert den Repositorybestand. Ein neuer öffentlicher Release mit neuem Tag und neu hochgeladenen ZIP-Dateien gehört nicht zu diesem Prüfdurchgang.
