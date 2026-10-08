# 1 AGB-Werkstatt: Abnahme 1.0.0

Stand: 9. Oktober 2026. Umfang: ausschließlich das neue Plugin, drei eigenständige Prompts, drei Mandatsakten und ihre Einbindung. Der vorhandene AGB-Recht-Prüfer bleibt unverändert.

## 1.1 Fachlicher Zuschnitt

Zehn Fachskills und ein Hauptskill führen von den vorhandenen Unterlagen zur vollständigen AGB-Fassung und zu gesonderten Kunden- und Umsetzungstexten. Vertragsart, Verbrauchereigenschaft, Vertriebsweg und gewünschte Interessenlage bestimmen die Auswahl. Bank- und Kreditbedingungen werden nicht ungeprüft in Händlerbedingungen übernommen.

Die Quellenkarte trennt gelesene Volltexte, amtliche Leitsätze, amtliche Zusammenfassungen und technisch eingeschränkte Abrufe. Entscheidungen werden mit Aussage und Übertragungsgrenze eingesetzt. Kein Anspruch auf vollständige Rechtsprechungskenntnis; kein Nachweis garantierter Rechtssicherheit. Die elektronische Widerrufsfunktion des Rechtsstands 2026 wird vom Bestell- und Kündigungsbutton abgegrenzt.

## 1.2 Nachweise

| Prüfung | Ergebnis |
| --- | --- |
| Pluginstruktur | Bestanden |
| Marketplace-Importstruktur | Bestanden: 293 Plugins und 23193 Skills |
| YAML-Frontmatter | Bestanden: keine Fehler oder Warnungen |
| Hauptverzeichnis und Bestandszahlen | Bestanden |
| `scripts/test-agb-werkstatt.py` | Zehn Regressionstests bestanden |
| Kompaktprompts | Schnellstart und Hauptproblem jeweils höchstens 7500 Zeichen und Bytes |
| Installationspakete | Elf Skills, konsistente Manifeste, keine automatisch installierten Standalone-Prompts oder Akten |
| Paketwiederholung | Pluginarchive bei Wiederholung bytegleich |
| Originalunterlagen | 36 Dateien; neun DOCX, neun PDF, neun EML und neun CSV-/Textdateien |
| E-Mail-Anhänge | Dateiinhalte bytegleich mit den zugeordneten Originaldokumenten |
| Rechnungen | Zeilensummen gegen Gesamtbetrag und den tatsächlich enthaltenen Rechnungstext geprüft |
| Aktenpakete | Je zwölf Einzel-PDFs; flache ZIPs ohne Markdown und mit verbindlicher README.txt |
| Downloadhinweise | Alle neuen Akten- und Plugin-Downloadgruppen geprüft |
| Dokumentqualität | Bestehende Sprach-, Kontakt-, E-Mail- und Metadatenprüfungen auf sämtliche 36 Originalstücke angewandt |
| Sichtprüfung | Alle neun gerenderten Word-Seiten und alle 36 Seiten der Einzel-PDF-Pakete kontrolliert |

Jedes Gesamt-PDF hat 18 Seiten einschließlich der vom bestehenden Builder eingefügten Trennblätter. Die Akten enthalten Geschäftsunterlagen und Mandatsaufträge, keine beigefügte Lösung. Vorhandene Draft-Klauseln sind Aussagen der jeweiligen Verfasser, keine rechtlichen Empfehlungen.

## 1.3 Abgegrenzte Altbefunde

Die repositoryweite Navigationsprüfung meldet neun bereits außerhalb dieser Ergänzung bestehende Befunde: einen nicht aufgelösten Bruchteil-Link in der experimentellen Vorlagensammlung, einen lokalen Pfad in einer vorhandenen Qualitätsprobe sowie sieben direkte Markdown-Vorschauziele in anderen Komponenten. Diese Prüfung ist insgesamt nicht grün.

Die repositoryweite Akten-Downloadprüfung meldet noch fünf Befunde zu den beiden Archivpfaden der bestehenden Schweriner IT-Vergabeakte und deren Verweis im Fachanwalt-Vergaberecht-README. Für die drei neuen AGB-Akten und das neue Plugin bestehen keine Befunde. Diese Altpfade werden im vorliegenden Komponentenrelease nicht umgeschrieben.

## 1.4 Reichweite

Es wurde kein Live-Benchmark in sämtlichen fremden Arbeitsoberflächen durchgeführt. Eine strukturell passende Installation ist nicht dasselbe wie ein nachgewiesen fehlerfreier juristischer Lauf. Externe Recherchezugänge, Dateiexport und Veröffentlichung hängen von der verwendeten Oberfläche und deren Freigaben ab.

Die 15 Release-Dateien bestehen aus zwei Pluginarchiven, drei Markdown-Prompts, drei Gesamt-PDFs, sechs Aktenarchiven und einer Prüfsummenliste. Ältere Sammelarchive bleiben unverändert; die Downloadverzeichnisse verweisen für diese Ergänzung auf das Komponentenrelease.
