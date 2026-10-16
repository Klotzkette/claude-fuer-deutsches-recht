# 1. Lesender Release-Review Phishing C-70/25

Datum: 16.10.2026. Repository: Klotzkette/claude-fuer-deutsches-recht. Geprüfte Komponentenfassung: 445.35.4. Der Review hat keine Repository-Datei geändert und keinen Commit erzeugt. Temporäre Prüfergebnisse liegen außerhalb des Repositorys.

## 1.1 Ergebnis

Im abschließend geprüften Stand wurden keine verbleibenden konkreten Veröffentlichungs- oder Logikfehler gefunden. Ein während des Reviews belegter Fehler wurde dem Hauptagenten gemeldet und anschließend durch ihn korrigiert: Der vorhandene Hauptproblem-Prompt des Fachanwalts für Bank- und Kapitalmarktrecht fehlte zunächst im Asset-Satz. Die korrigierte Funktion `prompts()` nimmt vorhandene Hauptproblem-Dateien zusätzlich auf; das fertige Paket enthält nun 39 Assets. Der nachfolgende vollständige Pakettest besteht.

Die Aussage bezieht sich auf die unten genannten Programme und den lokalen Paketbestand. Sie bestätigt keine bereits erfolgte GitHub-Veröffentlichung und ersetzt keine Kontrolle öffentlicher Downloads.

## 1.2 Gelesene Programme

- `scripts/build-phishing-release.py`
- `scripts/build-phishing-testakte-pakete.py`
- `phishing-vorfall-pruefer/scripts/phishing_case_gate.py`
- `scripts/test-phishing-tukowiecka.py`
- zusätzlich `scripts/test-phishing-release.py`, `scripts/prompt_profiles.py`, die relevanten zentralen ZIP-Validatoren und die gemeinsame Dokumentauswahl.

Dokumentation, Workflow und Integrationsänderungen des Hauptagenten waren ausdrücklich nicht Gegenstand des Reviews.

## 1.3 Releasequellen und Ausschlüsse

Der Komponentenbuilder sammelt sieben Plugin-Verzeichnisse. Er prüft vorhandene Manifestversionen, verbietet symbolische Links, entfernt Caches, Testaktenordner, CLAUDE.md und separate Begleitprompts aus den installierbaren ZIPs. Jeder ZIP-Eintrag wird gegen die Quelldatei verglichen. Für den portablen ZIP wird derselbe Dateisatz mit genau einem Plugin-Präfix verwendet. Die zentralen Prüfungen kontrollieren zusätzlich Skill-Dateien und den installierten Schwerpunkt-Skill.

Begleitprompts werden als eigene Dateien ausgeliefert. Die korrigierte Auswahl umfasst den vorhandenen Fachanwalts-Hauptproblem-Prompt, den profilierten AGB-Hauptproblem-Prompt sowie die zusätzliche Betreuungs-Unterlagenwerkstatt als byteidentisches MD/TXT-Paar. Die aktuelle vollständige Assetprüfung wurde gegen `/tmp/phishing-release/final` ausgeführt und bestand für alle 39 Dateien einschließlich Prüfsummen, Quellenidentität und kompakten Promptgrenzen.

## 1.4 Testakte und unveränderte Altakte

Die neue Akte enthält 28 Originaldateien. Deren aktuelle SHA-256-Werte wurden unabhängig mit dem Prüfprotokoll verglichen. Alle 10 E-Mails wurden geparst; sämtliche 13 MIME-Anhänge stimmen bytegenau mit den zugehörigen Originaldateien überein.

Der Aktenbuilder prüft Quellenhashes vor der Konvertierung. Er arbeitet bei Excel mit einer temporären Druckkopie, ändert dabei Druckausrichtung und Zeilenhöhen, nicht die Zellenwerte oder Formeln der Originaldatei. Die Originalpakete enthalten die Originalbytes. Einzel-PDF-ZIP und Original-ZIP besitzen den vorgesehenen zweisprachigen Wurzelhinweis. Das Gesamt-PDF wird aus den 28 Einzel-PDFs in derselben Reihenfolge zusammengesetzt. Die fertige Paketprüfung bestätigt 33 Seiten und seitenweise identischen extrahierbaren Text zwischen Einzel- und Gesamtfassung.

Für `testakten/phishing-vorfall-mayer-sparkasse-berlin` zeigte `git diff --name-only` keine Änderung. Dessen vorhandene JSON-Eingabe wurde mit dem aktualisierten Helfer neu ausgewertet: behaupteter Schaden und Transaktionssumme betragen jeweils 12.295,00 Euro; der Abgleich ist wahr, eine menschliche Freigabe wird nicht erzeugt. Die historische Ausgabedatei wurde nicht verändert.

## 1.5 Summen und Befugnisgrenzen

Die zwei neuen Excel-Arbeitsmappen wurden mit Formeln und gespeicherten Ergebnissen geöffnet. Drei dokumentierte Formelprüfungen stimmen mit dem aktuellen Dateistand überein. Der Kontoverlauf ist rechnerisch konsistent: 2.146,38 Euro Anfangssaldo, abzüglich 700 Euro, 62 Euro und 27,45 Euro, zuzüglich einer sachfremden Apothekenerstattung von 12,80 Euro, ergeben 1.369,73 Euro. Die 12,80 Euro sind ausdrücklich kein Phishing-Erstattungsbetrag; der streitige Betrag bleibt 700 Euro.

Der Helfer akzeptiert nur endliche nichtnegative Geldbeträge und echte boolesche Faktoren. Fehlende Beträge und unvollständige Transaktionslisten ergeben unbekannte Summen und keinen bestätigten Abgleich. Ein Minutenabstand entscheidet keine rechtliche Unverzüglichkeit. Belastende Fahrlässigkeitsindikatoren setzen die Erstattungsprüfung nicht automatisch auf Rot.

Zusätzlich wurden alle vier Autorisierungszustände mit leeren und behaupteten Verdachtsdaten durchgespielt. Selbst eine vollständig ausgefüllte behauptete Behördenmitteilung mit unverifiziertem Inhalt erzeugt nur einen Prüfstatus, keine bestätigte Betrugsausnahme. `human_release_granted` blieb in sämtlichen Proben falsch. Die Hinweise nennen ausdrücklich, dass Begründung und Behördenzuständigkeit rechtlich geprüft werden müssen.

## 1.6 Lesefassungen und ausgeführte Prüfungen

Die Werkstatt-Lesefassung enthält 7 Seiten mit 27.538 extrahierten Textzeichen; die Schnellstart-Lesefassung 3 Seiten mit 7.424 Textzeichen. Eine unabhängige Koordinatenkontrolle fand in beiden PDFs keine Zeichen außerhalb der Seitengrenzen. Die Seitenzahl der Werkstatt ist angesichts des tatsächlich enthaltenen Textes plausibel. Diese Kontrolle ist keine Behauptung einer eigenständigen visuellen Prüfung jeder Seite; die gesonderte Sichtprüfung aller zehn Seiten ist in `prompt-pdf-pruefung.json` dokumentiert.

Ausgeführt und bestanden:

- `scripts/test-phishing-tukowiecka.py`: 11 Regressionstests.
- `scripts/test-phishing-release.py`: Quellen, sieben Komponenten, Promptgrenzen und Regressionen.
- `scripts/test-phishing-release.py --dist /tmp/phishing-release/final`: 39 Assets, Prüfsummen, Plugin- und Promptquellen, Originalakten und PDF-Zusammenführung.
- Eigene lesende Prüfroutine `/tmp/phishing-c70-25/review_readonly.py`: 28 Quellenhashes, 10 E-Mails, 13 Anhänge, 2 Arbeitsmappen, 3 Formelergebnisse, Kontosaldo, PDF-Seitengrenzen, Neuauswertung der Altakte und Befugnisgrenzen des Helfers.
