# 1. Unabhängiger Review der Alltagskorrespondenz

Prüfdatum: 28.09.2026. Geprüft wurde der Arbeitsstand von `feat/hildesheim-alltag` für v445.8.1 gegen `origin/main` mit Commit `aede75149b8ab96906ce173b566c6e69c99da3e0`. Reviewer: Codex-Unteragent `merge_remote_check`.

**Befund: keine konkreten Fehler oder Regressionen im geprüften Umfang.**

## 1.1. Geprüfter Umfang

Gelesen wurden der neue Builder `scripts/build-bauwirtschaft-hildesheim-alltag.py`, die Erweiterung der Lebensakten-Tests, die Datensatzstruktur und Metadaten aller drei `scripts/data/hildesheim-alltag-*.json`, die Änderungen der Akten-, Plugin- und zentralen README sowie die aufgerufene DOCX-Normalisierung. Geprüft wurden außerdem die erzeugten E-Mail-Header und die tatsächliche Zuordnung zu Original- und Einzel-PDF-Archiven. Eine erneute vollständige redaktionelle oder visuelle Sichtprüfung der separat bereits gegengelesenen 44 Seiten war nicht Gegenstand dieses Auftrags.

## 1.2. Tatsächliche Gegenprüfungen

1. Ein direkter Vergleich der aktuellen Dateiinhalte mit den Git-Blob-IDs aus `origin/main` bestätigt: **alle 366 bisherigen Originale sind bytegleich**. Der Nachweis beruht nicht ausschließlich auf dem neu hinzugefügten Bestandsmanifest.
2. Alle **44 neuen Dateien** wurden mit dem Builder im Speicher erneut erzeugt; Datei-Schreibzugriffe wurden dafür abgefangen und die DOCX-ZIP-Normalisierung auf einen Speicherpuffer angewendet. Mit der verwendeten gebündelten Runtime **Python 3.12.14** sind sämtliche erzeugten Bytes identisch mit den vorhandenen Originalen. Keine Aktenoriginale wurden dabei überschrieben.
3. Die Ergänzung enthält **35 EML und neun DOCX in elf Vorgängen mit jeweils vier Unterlagen**. Antwortbezüge führen zu früheren Unterlagen desselben Vorgangs. Der Builder überspringt Wordvermerke bei technischen E-Mail-Referenzen und verknüpft stattdessen die vorhandenen vorherigen Nachrichten. Die tatsächlich erzeugten `In-Reply-To`- und `References`-Header wurden durch die ausgeführte Fallsuite geprüft.
4. Über den gesamten Bestand von **84 E-Mails** wurde keine doppelte `Message-ID` gefunden. Die neuen Datumsheader entsprechen zusätzlich unabhängig vom Testmanifest den JSON-Zeitpunkten in `Europe/Berlin`, einschließlich Winter- und Sommerzeit. Die geprüften Header haben keine Parserdefekte; Absender, Empfänger und gegebenenfalls CC-Adressen verwenden reservierte `.example`-Adressen. Es wurden keine behaupteten Dateianhänge ohne vorhandene Anlagen festgestellt.
5. Alle Datensatzbezüge lassen sich auf vorhandene Aktenstücke zurückführen. Die neue Zuordnung wahrt die vier ausdrücklich vorgesehenen Unterordner; die übrige Exportarchitektur wird durch diese Änderung nicht umgestellt. Die README-Angaben zu Anzahl, Formaten, Vorgangszeiträumen und Gesamtumfang stimmen mit den geprüften Daten und Ausgaben überein.
6. Der tatsächlich vorhandene Exportindex enthält **410 Quellen**, darunter exakt die 44 neuen Unterlagen mit insgesamt **44 PDF-Seiten**. Das Gesamt-PDF hat **1.217 Seiten**. Das Original-ZIP enthält 412 Einträge einschließlich Gesamt-PDF und Hinweisdatei, das Einzel-PDF-ZIP 411 Einträge einschließlich Hinweisdatei. In beiden Archiven steht `README.txt` zuerst.
7. Die vollständige neue Fallsuite wurde unabhängig mit `--assets /tmp/hildesheim-lebensakte-alltag/dist` ausgeführt: **zehn Tests bestanden, kein Test übersprungen, 13,125 Sekunden**. Dabei wurden auch die tatsächlichen Originalbytes, Einzel-PDF-Inhalte, Gesamt-PDF-Lesezeichen und gedruckten Registerverweise kontrolliert. `git diff --check` für die geänderten Tests und gelesenen README-Dateien ergab keinen Befund.

## 1.3. Grenzen und Abschluss

Die Byte-Reproduzierbarkeit ist für Python 3.12.14 geprüft. Eine zusätzliche Speicherprobe unter Python 3.14.6 erzeugte bei drei E-Mails andere Faltungen der Betreffheader bei unverändertem Nachrichtenkörper; das ist eine Abhängigkeit der Standardbibliothek und kein hier behaupteter Inhalts- oder Exportfehler. Eine versionsübergreifende Bytegarantie wird daher nicht ausgesprochen.

Die Prüfung umfasst keinen vollständigen GitHub-Release-Lauf und keine erneute Sichtprüfung sämtlicher 1.217 PDF-Seiten. Sie erweitert weder den Aktenumfang noch die fachlichen Aussagen der Autorentexte. Außer diesem Bericht wurde keine Repository-Datei geschrieben. Kein Commit, Push oder sonstiger externer Vorgang wurde ausgeführt.
