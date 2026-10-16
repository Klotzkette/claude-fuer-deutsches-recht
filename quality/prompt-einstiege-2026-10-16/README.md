# 1. Prüfung der Prompt-Einstiege

Die Redaktion betrifft die veröffentlichten Werkstatt- und Schnellstart-Prompts. Sie sollen beim Lesen unmittelbar erkennen lassen, welche fachliche Aufgabe bearbeitet wird, welches Dokument daraus entsteht und welche rechtlichen Maßstäbe dabei helfen. Die Prüfung umfasst 302 Katalogeinträge und 609 Markdown-Dateien, einschließlich der neun HOAI-Phasenwerkstätten und der Betreuungs-Unterlagenwerkstatt.

## 1.1. Vorgehen und Abdeckung

Die Einstiege wurden je Fachgebiet gelesen und individuell bearbeitet: 602 Markdown-Dateien geändert, sieben bereits passende Fassungen beibehalten. Passende bestehende Entscheidungen stehen früh mit Anwendungsfall und Aussagegrenze; zugehörige Fach- und Quellenabschnitte sowie Rückfragen und Fortsetzung wurden abgeglichen. Angebote ohne Begleitprompts behalten ihre bisherige Veröffentlichungsform.

Die [Einzelprüfungen](einzelpruefungen.json) enthalten für jeden Katalogeintrag den Befund, Quellenstatus, die tatsächlich veröffentlichten Dateien, Größen und Prüfsummen. Eine Prüfsumme identifiziert die gesamte Datei; sie bescheinigt keine neue juristische Prüfung jedes Absatzes. Historische und rein technische Themen erhalten keine sachfremden Gerichtsentscheidungen. Fehlt ein verifizierter Entscheidungsanker, bleibt diese Grenze erkennbar.

## 1.2. Gegenprüfung und Korrekturen

Eine zusätzliche Lektüre ausgewählter anderer Fachgebiete kontrollierte Zuordnung, Verständlichkeit und Anschluss an den Arbeitsablauf. Dabei wurden insbesondere folgende Befunde bereinigt:

1. Beim einfachen Arbeitszeugnis keine Leistungsbeurteilung verlangen; den Beurteilungsanker ausdrücklich auf das qualifizierte Zeugnis beschränken.
2. Die Signaturregel für gerichtliche Schriftsätze über eine Mitarbeiterkarte nicht auf gewöhnliche Verträge und Beratungsbriefe übertragen.
3. Den Zugangsanker im Wirtschaftsanwalt ausdrücklich dem Kündigungsfall und Paragraf 130 Absatz 1 BGB zuordnen.
4. Widersprüchliche Pflichtübersichten der Vergabestellen-Werkstatt durch interne Prüfung und bedarfsabhängige Entscheidungsvorlagen ersetzen. Ein klar bestelltes Dokument benötigt keine erneute Ausgabewahl.
5. Vorgezogene Entscheidungsabsätze mit ihren Normen verbinden, Rückverweise und verbleibende Überschriften berichtigen sowie mehrfache Dokumenttitel und Doppelnummerierungen beseitigen.
6. Drei bisher fehlende technische Fachzuordnungen für Due Diligence, Untersuchungshaft und Verarbeitungsverzeichnis ergänzen, ohne die individuell bearbeiteten Prompts neu zu erzeugen.

## 1.3. Prüfung und Veröffentlichung

Die [Prüfläufe](prueflaeufe.json) dokumentieren die abschließenden lokalen Validatoren und Regressionstests. Dazu gehören Marketplace, Pluginstruktur, Frontmatter, Veröffentlichungsprofile, Herstellerprüfung, Workflow-Erhaltung, portable Starts, Quellenzuordnung und die neue strukturelle Einstiegsprüfung. Die neue Prüfung kontrolliert lesbare Anfangsabsätze, einen eindeutigen Dokumenttitel und die Stellung von Tabellen; sie kann fachliche Richtigkeit nicht automatisch bestätigen.

Bestehende TXT-Kopien sind mit ihren Markdown-Fassungen synchronisiert. Der Synchronisierer des importierten Vergaberecht-Unterprojekts erhält dessen sechs redigierte Rollenprompts anhand gültiger dateigebundener Qualitätsnachweise; ein abweichender Hash wird zurückgewiesen. Ältere Generatorquellen bleiben als solche bestehen, ersetzen aber keine geprüfte veröffentlichte Fassung. Die kompakten Prompts halten ihre veröffentlichten individuellen Größenprofile ein. Das Komponentenrelease `prompt-einstiege-v1.0.1` enthält eigenständige Markdown-Downloads und Prüfsummen. Es ersetzt weder das allgemeine Marketplace-Release noch bestehende Plugin- oder Aktenpakete. Bereits veröffentlichte PDF-Lesefassungen werden durch diese Markdown-Redaktion nicht rückwirkend geändert.

## 1.4. Grenzen

Dies ist eine redaktionelle Prüfung der Einstiege und ihrer fachlichen Anschlüsse, keine erneute vollständige Verifikation sämtlicher Rechtsquellen. Frühere Quellenstände und Zugriffsgrenzen bleiben bestehen. Statische Prüfungen sind kein Live-Test in einer bestimmten Oberfläche und keine Garantie für juristisch richtige Ergebnisse. Skills, Testakten und Plugin-Manifeste wurden in dieser Runde nicht geändert.
