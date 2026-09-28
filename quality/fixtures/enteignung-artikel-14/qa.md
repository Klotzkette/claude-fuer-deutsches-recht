# 1. Gezielte Abschlussprüfung

Stand: 28.09.2026. Ausschließlich Themenplugin, Themenfixtures, Themenprüfprofil und Göttinger Quellenakte bearbeitet. Keine globalen Generatoren, Root-Registrierungen oder Commits ausgeführt. Die zwischenzeitlich zentral gesetzte Manifestversion 445.11.0 wurde nicht zurückgesetzt.

## 1.1. Umfang

Neun eigenständige Skills, Werkstatt mit 18.282 UTF-8-Bytes, Schnellstart mit 6.916 UTF-8-Bytes, lokales Quellenregister und Zitierregeln. Zehn redaktionelle Evaluationsfälle, gültiges lokales Schema und geprüfte SHA-256-Redaktionshashes. Kein Live-Modellvergleich behauptet.

Die Quellenakte enthält elf individuelle Dateien: fünf PDF mit jeweils zwei Seiten, ein DOCX mit zwei Seiten, zwei EML, zwei TXT und eine CSV mit 15 Datenzeilen. Drei eingebettete PDF-Anhänge sind bytegleich mit den jeweils separat abgelegten Originalen. Keine Bewertungsunterlagen im Quellenexport; der gemeinsame Exportfilter nimmt genau die elf Originale auf.

## 1.2. Builder und Tests

Native Builder: `scripts/build-enteignung-artikel-14-case.py`.

Autoritative Themenquelle: `scripts/fixtures/enteignung-artikel-14/case.json`.

Regressionen: `scripts/test-enteignung-artikel-14.py`, 19 Tests erfolgreich. Geprüft wurden Metadaten, eigenständige Skills, lokale Links, Dezimalgliederung, Promptgrenzen, Quellenanker, Redaktionshashes, Evaluationsabdeckung, Dateiinventar, vollständiger PDF-Text, DOCX-Formatierung, MIME-Inhalt, Anhangsbytes, CSV-Rechnungen, Flächen, Kontaktadressen, Disclaimergrenzen, reproduzierbare Dateibytes und Ablehnung fehlerhafter Fixturepfade. Der bestehende ZIP-Builder wurde ausschließlich im Arbeitsspeicher geprüft: elf Originale plus verbindliche `README.txt`, ohne README.md und rubric.yaml.

Verwendet wurde das gebündelte Python unter `/Users/klotzkette/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`. Dort fehlt PyYAML; für den Prüflauf wurde der vorhandene lokale Paketpfad `/Users/klotzkette/Library/Python/3.14/lib/python/site-packages` am Ende von `sys.path` ergänzt. Keine Abhängigkeiten installiert und keine Runtime-Dateien verändert. Der Builder benötigt python-docx, reportlab und Times New Roman; ein anderer Schriftordner ist über `--font-dir` möglich.

## 1.3. Sichtprüfung

PDF-Seiten: `quality/fixtures/enteignung-artikel-14/render-pdf/`, zehn PNG-Dateien, mit Poppler auf 1.600 Pixel lange Kante gerendert und vollständig visuell geprüft. Plan, Tabellen, Umlaute, Absatzenden und Seitenfüße sind lesbar; keine abgeschnittenen Inhalte oder Überschneidungen.

Word-Seiten: `quality/fixtures/enteignung-artikel-14/render-docx/page-1.png` und `page-2.png`, mit dem bereitgestellten DOCX-Renderer erzeugt und vollständig visuell geprüft. In der ersten Fassung geerbten Titelstrich und Theme-Schrift entfernt, danach erneut gerendert. Endfassung durchgehend Times New Roman, Fließtext 11 pt, schwarze Überschriften. Das PDF in diesem Renderordner ist ausschließlich ein QA-Derivat, kein zusätzliches Quellenoriginal.

## 1.4. Integration

Die bereits vom Parent übernommenen Katalog- und Marketplace-Einträge wurden nicht angefasst. Noch zentral zu bauen beziehungsweise abschließend zu prüfen: Promptderivate, Sammel-PDF, Downloadpakete und Downloadlinks mit zweisprachigem Hinweis. Für ZIPs den vorhandenen zentralen Builder verwenden; er erzeugt die verpflichtende `README.txt`. Themenfixtures, Evaluationsprofil, dieses Prüfprotokoll und Renderbilder gehören nicht in die Quellenpakete. Quellenstand und amtliche URLs stehen vollständig in `quality/evals/enteignung-artikel-14.json` und `enteignung-artikel-14/references/rechtsgrundlagen.md`.
