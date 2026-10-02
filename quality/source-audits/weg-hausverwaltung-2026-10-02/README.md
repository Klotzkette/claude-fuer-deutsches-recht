# 1. WEG-Hausverwaltung: Prüfung vom 2. Oktober 2026

## 1.1. Fachlicher Umfang

Das bestehende Plugin behält seine 93 Skills. 46 Fachtexte sind gezielt überarbeitet. Die Oktoberreferenz enthält 30 anhand amtlicher Volltexte geprüfte BGH-Entscheidungen, darunter zehn aus 2026. Die ergänzende Quellenprüfung behandelt Mietumlage, Bettwanzen und Datenschutz. Aussage, Fundstelle und Übertragungsgrenze stehen in den Quellenberichten; daraus folgt keine Vollprüfung jeder Aussage aller 93 Skills.

- [WEG-Quellenprüfung](weg-pruefbericht.md)
- [WEG-Quellenbelege](weg-quellen.json)
- [Inventar der Skills mit Endfassungs-Prüfsummen](weg-skill-inventar.json)
- [Miet-, Befalls- und Datenschutzquellen](miet-datenschutz-quellen.md)

## 1.2. Tatsächliche Anwendungsproben

Ein Agent hat Mini-, Hauptproblem- und Werkstatt-Prompt nacheinander auf Spreebogen, Lindenhof und Sonnenwinkel angewendet. Dies sind drei tatsächliche Arbeitsprodukte im selben fortbestehenden Kontext, kein Benchmark dreier unabhängiger Modelle. Ein weiterer Agent hat anschließend die Ausgaben gegen alle 100 Rohunterlagen geprüft. Diese zweite Prüfung ist unabhängig durchgeführt, aber nicht verblindet.

Die zentralen Berechnungen und Fallabgrenzungen sind im geprüften Umfang bestätigt. Kein kritischer Fehler wurde festgestellt. Der getrennte Exporthinweis für reine Textausgaben fehlt jedoch in den drei Ergebnissen. Die tatsächlichen Ausgaben bleiben unverändert dokumentiert; der formale Nachtrag steht getrennt. Aktenbedingt offene Tatsachen, rechtliche Teilfragen und Versandfreigaben sind keine bestandenen Abschlussprüfungen.

- [Durchführung und Grenzen](anwendungsproben/methodik.txt)
- [Unabhängige Bewertung](probe-independent-review.json)
- [Erneuter Quellen- und Rechenabgleich](probe-review-source-checks.json)
- [Formaler Nachtrag](anwendungsproben/exporthinweis.txt)

## 1.3. Dokumente und Technik

Vier neue Akten enthalten 132 Originaldateien: 80 Word-Dokumente, 41 E-Mails, sechs Excel-Arbeitsmappen und fünf Textnotizen. Die Prüfung unterscheidet gespeicherte Formelwerte, tatsächliche Office-Neuberechnung mit geänderten Eingaben und unabhängige Rechenketten. E-Mail-Anhänge sind bytegenau mit den Originalen abgeglichen.

Sämtliche 80 Word-Seiten, 13 Tabellenblätter und 30 Werkstattseiten sind visuell geprüft. Die PDF-Prüfung umfasst 364 Seiten aus 132 Einzel-PDFs und vier Gesamt-PDFs: 271 unterschiedliche gerenderte Seiten wurden einzeln angesehen; 93 pixelidentische Wiederholungen sind über einen vollständigen Bildvergleich zugeordnet. Vier zunächst fehlende CO₂-Ziffern wurden im PDF-Renderer korrigiert und die betroffenen Endseiten erneut angesehen. Originalunterlagen blieben dabei unverändert.

- [Native Rechnungen, Formeländerungen und Mailanlagen](native-financial-mime-checks.json)
- [Excel-Sichtprüfung](spreadsheet-visual-review.json)
- [Word-Sichtprüfung](word-visual-review.json)
- [Endgültige PDF-Sichtprüfung](pdf-final-visual-review.json)
- [Werkstatt-Sichtprüfung](workshop-visual-review.json)
- [Technische Prüfkommandos](technical-checks.json)

Die technischen Rubrikkriterien und die qualitativen Anwendungsproben sind getrennte Nachweise. Nicht durchgeführte menschliche Rubrikkriterien bleiben offen. Release-Verpackung und öffentlicher Download-Abgleich erfolgen anschließend am endgültigen Merge-Commit; dieser Bericht behauptet sie nicht vorab.
