# 1. Alltagskorrespondenz für v445.8.1

Prüfstand: 28. September 2026. Die Ergänzung betrifft die bestehende Hildesheimer Lebensakte. Sie enthält 44 neue Originale in elf zusammenhängenden Vorgängen: 35 E-Mails und neun Wordvermerke. Die Quellen für die Generierung liegen in `scripts/data/hildesheim-alltag-{bau,menschen,kaufmaennisch}.json`; der reproduzierbare Einstieg ist `scripts/build-bauwirtschaft-hildesheim-alltag.py`.

## 1.1. Inhalt und damaliger Kenntnisstand

Sämtliche 44 Texte wurden von den jeweiligen Bearbeitern und anschließend vollständig im Hauptstrang gelesen. Die Prüfung bezog Namen, Zuständigkeiten, Mengen, Termine, Wohnungszuordnung, Ablesewerte und Belegnummern ein. Die drei gesonderten Prüfvermerke nennen die verwendeten Originalquellen und die jeweilige Fortsetzung. Neue Uhrzeiten, Gespräche und Alltagsszenen sind fiktive Ergänzungen innerhalb des bereits simulierten Projektverlaufs.

Bei der Schlussredaktion wurden unter anderem eine reflexive Formulierung über die Urheberschaft eines Aufmaßes sowie ein nicht belegter Zwischenschritt bei der Eingabe eines Ablesedatums beseitigt. Eine Rückzahlungsankündigung wird vom Bankeingang getrennt; der Jahresauszug vom 31. Dezember 2028 wird erst in Nachrichten vom Januar 2029 ausgewertet. Prüfungen und Lieferungen werden erst nach ihrem dokumentierten Termin bestätigt. Die Kenntnis späterer Befunde wird nicht in frühere Nachrichten verlegt.

Die Ergänzung enthält keine neuen juristischen Gutachten oder Rechtsprechungsbehauptungen. Sie verändert keine Baukosten, Rechnungen, Zahlungen, Mietverträge, Vertragsfristen oder abgeschlossenen Prüfprotokolle. Die Verkaufsvariante bleibt eine unbeschlossene Option. Die 29 Skills und das 100-seitige Werkstatthandbuch bleiben inhaltlich unverändert. Eine neue Modellbewertung des Plugins wird durch diese Aktenprüfung nicht behauptet.

## 1.2. Bestand und Ausgabe

Der Aktenbestand zählt 410 Originaldateien: 184 DOCX, 101 PDF, 84 EML, 28 XML, sieben CSV, drei XLSX, zwei PNG und eine TXT-Datei. `alltag-bestand-v445.8.0.json` hält die 366 vorherigen Originale mit Quellhashes fest. Der Regressionstest bestätigt für sämtliche Dateien dieses Ausgangsstands Bytegleichheit. Der frühere Basisabgleich mit den 198 Ausgangsdateien bleibt zusätzlich bestehen.

Das Gesamt-PDF umfasst 1.217 Seiten: 13 Seiten Dokumentenregister und 1.204 Seiten Akteninhalt. Die bisherigen 366 PDF-Lesefassungen mit zusammen 1.160 Seiten wurden bytegleich aus dem bereits geprüften Stand übernommen. Die 44 neuen Unterlagen tragen jeweils eine zusätzliche Inhaltsseite bei. Jeder Originaldatei ist ein Lesezeichen sowie eine gedruckte Anfangsseite und ein Umfang zugeordnet.

Die neun Worddateien wurden mit dem kanonischen `render_docx.py` in PDF und Seitenbilder umgewandelt. Alle 44 neuen Dokumentseiten wurden vollständig in Originalgröße visuell geprüft; die einzelnen PDF-Hashes stehen in den drei Teilprüfvermerken. Der Hauptstrang prüfte zusätzlich sämtliche 13 neu aufgebauten Registerseiten. Die Registerzeilen und Zahlen bleiben vollständig lesbar; es gibt keine abgeschnittenen Zellen oder überlagerten Fußzeilen. Die letzte Seite enthält die reguläre Fortsetzung der drei verbleibenden Registerzeilen.

Das Originalformat-ZIP enthält 412 Einträge: Herkunfts-README, 410 Originale und Gesamt-PDF. Das Einzel-PDF-ZIP enthält 411 Einträge: Herkunfts-README und 410 einzelne PDF-Lesefassungen. Die Unterordner bleiben in beiden Varianten erhalten. Der zusätzliche 304-seitige Bautagebuchband ist unverändert als gesonderter Download erreichbar.

## 1.3. Automatische Prüfungen

Die folgenden lokalen Prüfungen wurden erfolgreich ausgeführt:

- `scripts/test-bauwirtschaft-hildesheim-lebensakte.py --assets /tmp/hildesheim-lebensakte-alltag/dist`: zehn Tests ohne Auslassung. Enthalten sind der tatsächliche ZIP-/Originalvergleich, der vollständige Textabgleich aller Einzel-PDFs und aller Dokumentteile des Gesamt-PDFs, sämtliche gedruckten Registerverweise sowie MIME-Antwortketten und deren Chronologie.
- `scripts/test-testakte-projektordner.py`: sechs Tests einschließlich Pfadsicherheit und Erhalt der bestehenden flachen Aktenexporte.
- `scripts/test-bauwirtschaft.py`: zehn Tests.
- `scripts/validate-testakten-dokumentqualitaet.py`: 79 Akten, 2.175 formale Dokumente und 9.479 Exportdateien bestanden.
- Pluginstruktur, Versionsübersichten, Laufzeitbudgets, Qualitätsprofile, Markdownstruktur und Downloadhinweise bestanden.

Diese Abnahme dokumentiert den lokalen Stand vor Veröffentlichung. Release-Lauf und tatsächlich öffentlich heruntergeladene Dateien sind gesondert zu prüfen; ihre Fertigstellung wird hier nicht vorweggenommen. Die aktuellen lokalen Artefakthashes stehen in `export-manifest.json`.
