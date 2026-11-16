# Verständliche Werkstätten und interaktive Fallansichten

Die Werkstatt-Prompts und zentralen Einstiegsskills führen vorhandene Unterlagen zu einem verwendbaren Ergebnis. Sie erklären den Vorgang, zeigen bei komplexen Zusammenhängen eine passende Ansicht und arbeiten neue Angaben in dasselbe Dokument ein. Eine Visualisierung ist besonders hilfreich, wenn sich Zeitpunkte, Beteiligte, Beträge, Varianten oder Belegketten sonst nur schwer überblicken lassen.

## 1. So lässt sich damit arbeiten

Den passenden Werkstatt-Prompt mit den Fallunterlagen verwenden oder im installierten Plugin den Auftrag beschreiben. Die Werkstatt wählt eine zur Frage passende Darstellung selbst. Der Nutzer muss kein Darstellungswerkzeug auswählen und keine besondere Startformel kennen.

Beispiele:

| Auftrag | Was die Ansicht verständlich macht | Anschließendes Ergebnis |
| --- | --- | --- |
| „Vergleiche diese vier Türenangebote und bereite die Verhandlung vor.“ | Welche LV-Position welches Angebot erfüllt, welche Nebenleistung fehlt und welcher Preis nur unter einer Bedingung gilt. | Aufklärungsfragen und Verhandlungsnotiz mit Belegen. |
| „Was ist in dieser Compliance-Akte eigentlich passiert?“ | Unternehmen, Produkt, Rezeptur, Charge, Kennzeichnung, Lieferung und entdeckter Hinweis; Tatsachen und Verdacht bleiben unterscheidbar. | Untersuchungsauftrag oder Zwischenbericht zur konkret erreichten Bearbeitungsstufe. |
| „Ab wann war die Gesellschaft zahlungsunfähig?“ | Getrennte Stichtage und die zugehörigen Mittel und fälligen Verbindlichkeiten; eine unsichere Finanzierungsannahme erscheint als Variante. | Nachrechenbarer Stichtagsvermerk; Überschuldung bleibt ein eigener Befund. |
| „Ordne diese Rechnungen und Zahlungseingänge für den Monat.“ | Verbindung von Rechnung, Zahlung, Nettobetrag, Steuer und Erklärungsfeld; fehlende Belege werden nicht zu Nullbeträgen. | Abstimmtabelle und die beauftragte Erklärungsvorbereitung. |
| „Überarbeite den Vertrag nach dieser Änderung.“ | Ausgangsklausel, vorgeschlagene Fassung und die davon betroffenen weiteren Regelungen. | Ausformulierter Vertragsentwurf, der die ausgewählte Variante tatsächlich enthält. |

Bei einer einfachen Frage bleibt die Antwort kurz. Bei einem ausdrücklich bestellten Brief oder Vertrag entsteht das Dokument; eine zusätzliche Übersicht darf dessen Fertigstellung nicht verdrängen.

## 2. Lange Werkstatt-Prompts verwenden

Ein Werkstatt-Prompt kann bei Bedarf auch rund 100 Seiten umfassen. Er beginnt trotzdem mit der konkreten Aufgabe. Die ausführliche Fassung dient der Arbeit an Entscheidungsvarianten, Beweislast, Quellen und Gegenpositionen. Für den laufenden Auftrag werden die einschlägigen Abschnitte verwendet.

Bei langen Fassungen empfiehlt es sich, den Prompt als Markdown- oder Textdatei zusammen mit den für den ersten Schritt erforderlichen Unterlagen bereitzustellen. Ein möglicher Startauftrag lautet: „Verwende die beigefügte Werkstatt als Arbeitsanweisung. Wir vertreten die Klägerin. Lies zuerst Urteil und Zustellungsnachweis, prüfe die Fristen und arbeite die tragenden Urteilsgründe bis zu einem Entwurf für die Berufungsbegründung durch.“ Steht der Dateizugriff nicht zur Verfügung, kann man Einstieg und benötigte Kapitel nacheinander in dasselbe Gespräch einfügen. Die Werkstatt hält dabei die benutzten Belege, offenen Entscheidungen und den nächsten Abschnitt fest. Vor der Übergabe prüft sie das gesamte Dokument auf Widersprüche.

Die Werkstatt prüft das Recht zum maßgeblichen Zeitpunkt und sucht für entscheidende Fragen nach neuerer Rechtsprechung. Sie bestätigt den Quellenstand erst, wenn sie die einschlägige amtliche Quelle geprüft hat. Der [Quellenbericht zur Prompt-Sammlung](../quality/source-audits/2026-11-16-workflows/README.md) erläutert, welche Urteile im Volltext geprüft wurden und wo der Abgleich nur Metadaten erfasste.

## 3. Darstellung in ChatGPT und Claude

Die Prompts richten sich nach den tatsächlich angebotenen Funktionen. Ein Produktname allein beweist weder Dateizugriff noch eine interaktive Oberfläche. In einer geeigneten Umgebung können sie eine eingebettete Grafik, ein Artefakt oder ein kleines Applet direkt erzeugen. Ohne diese Funktion liefern sie eine verständliche Tabelle oder beschriftete statische Darstellung und setzen den Auftrag fort.

| Aufgabe | ChatGPT bei tatsächlich verfügbarer Funktion | Claude bei tatsächlich verfügbarer Funktion |
| --- | --- | --- |
| Längerer Schriftsatz, Vertrag oder Gutachten | Den Entwurf in einer bearbeitbaren Dokumentansicht wie Canvas fortführen. | Ein bearbeitbares Dokumentartefakt verwenden und die laufende Fassung dort fortführen. |
| Filter, Belegauswahl oder Rechenvariante | Eine eingebettete Visualisierung oder eine ausführbare HTML-Vorschau nutzen. Erst ein funktionierender Filter macht daraus eine interaktive Ansicht. | Eine interaktive Visualisierung im Chat oder in Cowork nutzen, bei einer eigenständigen Fallansicht ein privates Artefakt erstellen. |
| Dateierzeugung ohne Vorschau | Eine tatsächlich bereitgestellte, eigenständige HTML-Datei kann lokal geöffnet werden. | Derselbe Dateiweg, wenn Dateierzeugung und Abruf möglich sind. Der bloße Aufruf eines Hosting- oder Publikationsbefehls ist kein Ersatz. |
| Nur Text verfügbar | Mit Belegkennungen, Tabelle und klar benannten Varianten im selben Gespräch weiterarbeiten. | Mit Belegkennungen, Tabelle und klar benannten Varianten im selben Gespräch weiterarbeiten. |

Die dokumentierten Vorschauen und Artefakte hängen von Oberfläche, Berechtigungen und Konto ab. Ein Markdown-Prompt registriert keine neue App und baut keinen Rückkanal. Eine Auswahl muss deshalb auch als lesbarer Text übernommen werden können. Erst wenn sie im Gespräch angekommen ist, kann die Werkstatt den Entwurf damit fortschreiben.

Ein privates [Artefakt aus Claude Code](https://code.claude.com/docs/en/artifacts#availability) kann auf der Infrastruktur des Anbieters liegen. Wenn der Arbeitsbereich diesen Weg nicht für die betreffenden Daten erlaubt, bleibt die Werkstatt bei einer lokalen Datei oder beim zugelassenen Textweg.

Produktdokumentation, geprüft am 16. November 2026: [ChatGPT Canvas](https://openai.com/index/introducing-canvas/), [Dateivorschau in ChatGPT](https://learn.chatgpt.com/docs/artifacts-viewer), [Oberflächen für verbundene ChatGPT-Apps](https://developers.openai.com/plugins/build/chatgpt-ui), [Claude-Artefakte](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them), [Claude Cowork](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile).

Der vorhandene Anwendungs- oder Dateiworkflow promptloser Plugins bleibt erhalten. Eine statische Plugin-Vorschauseite wird nicht als Fallanwendung ausgegeben. Aktive Funktionen, Export und erfolgreiche Sichtprüfung werden nur bestätigt, wenn sie tatsächlich stattgefunden haben.

## 4. Die Auswahl bleibt nachvollziehbar

Die Ansicht verbindet jeden tragenden Wert mit seiner Fundstelle. Belegte Daten, streitige Angaben, fehlende Nachweise und angenommene Varianten bleiben unterscheidbar. Ein Schieberegler erzeugt keine verbindliche Rechtsfolge und keine erfundene Erfolgswahrscheinlichkeit.

Wenn der Nutzer eine Alternative wählt oder weitere Unterlagen liefert, werden betroffene Rechenschritte und Textabschnitte im laufenden Arbeitsprodukt angepasst. Die Werkstatt fragt bereits beantwortete Punkte nicht erneut ab. Sie endet mit dem beauftragten Dokument und erklärt verbleibende, tatsächlich entscheidende Lücken.

In der [interaktiven Demo zur Kündigungsakte](https://klotzkette.github.io/claude-fuer-deutsches-recht/werkstatt/fallansicht.html) lässt sich das an einem fiktiven Fall ausprobieren: Belege auswählen, einen streitigen Zugang als Variante setzen und den daraus entstehenden Arbeitsauftrag in einen Chat übernehmen. Das Beispiel läuft im Browser und ist keine Verbindung zu einem Modell.

## 5. Pflege und Prüfgrenzen

Die explizite Zuordnung in `scripts/data/werkstatt-visualisierung-profile.json` erfasst alle Marketplace-Plugins und ihre tatsächlich vorhandenen Haupt- oder Einstiegsskills. Eine feste elfte Position wird nicht unterstellt. Bestehende Fachtexte werden durch einen markierten Zusatz ergänzt; dessen Entfernung stellt den vorherigen Text bytegenau wieder her. Eigenständige Werkstatt-Prompts enthalten die benötigten Anweisungen selbst. Installierbare Skills nutzen ergänzend eine paketlokale Referenz.

Besondere Größen- und Klartextvorgaben bleiben wirksam. Die Bauwirtschaft nutzt deshalb eine kompakte Einbindung mit der vollständigen lokalen Referenz. Klartextprofile erhalten unformatierte Beschriftungen. Bereits vorhandene TXT-Kopien, einschließlich besonderer Werkstätten, bleiben mit ihrem Markdown-Inhalt identisch; zusätzliche Nebenformate entstehen nur nach dem Publikationsprofil.

`python3 scripts/sync-werkstatt-visualisierung.py --check` prüft den veröffentlichten Quellbestand gegen diese Zuordnung. `--write` synchronisiert die Ergänzungen; `--record-review` bindet ausschließlich bereits passende redaktionelle Dateiprüfungen an den ergänzten Stand. Eine vorher schon abweichende Datei erhält dadurch keine nachträgliche fachliche Freigabe. Die Generatoren erzeugen dieselben Ergänzungen; bestehende TXT-Kopien bleiben byteidentisch.

Die Regressionen prüfen vollständige Abdeckung, Fachzuordnung, Quellen- und Dateierhaltung, wiederholbare Synchronisierung, die beiden promptlosen Angebote, funktionsabhängige Rückfallwege und die Übergabe von UI-Auswahlen. Diese Prüfungen belegen keine Live-Ausführung aller Plugins in allen Oberflächen. Für eine konkrete erzeugte Anwendung sind Sichtprüfung, Bedienung und Rechenergebnis im jeweiligen Arbeitslauf gesondert zu kontrollieren.
