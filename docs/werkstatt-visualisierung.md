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

## 2. Darstellung in ChatGPT und Claude Cowork

Die Prompts richten sich nach den tatsächlich angebotenen Funktionen. Ein Produktname allein beweist weder Dateizugriff noch eine interaktive Oberfläche. In einer geeigneten Umgebung können sie eine eingebettete Grafik, ein Artefakt oder ein kleines Applet direkt erzeugen. Ohne diese Funktion liefern sie eine verständliche Tabelle oder beschriftete statische Darstellung und setzen den Auftrag fort.

ChatGPT beschreibt interaktive Visualisierungen als von Oberfläche und Verfügbarkeit abhängige Funktion. Für Plugin-Oberflächen dokumentiert OpenAI eine isolierte UI-Ressource mit definierten Kommunikationswegen. Deshalb prüfen die Anweisungen Fähigkeiten und setzen weder beliebige eingebettete Webseiten noch eine automatisch vorhandene Modellrückmeldung voraus. [Visualizations](https://learn.chatgpt.com/docs/visualizations), [Add UI to your MCP server](https://developers.openai.com/plugins/build/chatgpt-ui).

Claude dokumentiert eigene Visualisierungen für Chat und Cowork auf Web und Desktop. In Cowork ist die Anschlussfrage durch einen Klick in der Visualisierung laut Hilfe nicht verfügbar. Deshalb muss eine Auswahl auch als lesbarer Text übernommen werden können. Erst wenn die Auswahl beim Modell angekommen ist, kann es den Entwurf daraufhin fortschreiben. [Custom visuals in chat and Cowork](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork).

Der vorhandene Anwendungs- oder Dateiworkflow promptloser Plugins bleibt erhalten. Eine statische Plugin-Vorschauseite wird nicht als Fallanwendung ausgegeben. Aktive Funktionen, Export und erfolgreiche Sichtprüfung werden nur bestätigt, wenn sie tatsächlich stattgefunden haben.

Produktdokumentation geprüft am 13. November 2026. Verfügbarkeit und Kontoeinstellungen können sich ändern; die Prüfung im konkreten Arbeitslauf bleibt erforderlich.

## 3. Die Auswahl bleibt nachvollziehbar

Die Ansicht verbindet jeden tragenden Wert mit seiner Fundstelle. Belegte Daten, streitige Angaben, fehlende Nachweise und angenommene Varianten bleiben unterscheidbar. Ein Schieberegler erzeugt keine verbindliche Rechtsfolge und keine erfundene Erfolgswahrscheinlichkeit.

Wenn der Nutzer eine Alternative wählt oder weitere Unterlagen liefert, werden betroffene Rechenschritte und Textabschnitte im laufenden Arbeitsprodukt angepasst. Die Werkstatt fragt bereits beantwortete Punkte nicht erneut ab. Sie endet mit dem beauftragten Dokument und erklärt verbleibende, tatsächlich entscheidende Lücken.

## 4. Pflege und Prüfgrenzen

Die explizite Zuordnung in `scripts/data/werkstatt-visualisierung-profile.json` erfasst alle Marketplace-Plugins und ihre tatsächlich vorhandenen Haupt- oder Einstiegsskills. Eine feste elfte Position wird nicht unterstellt. Bestehende Fachtexte werden durch einen markierten Zusatz ergänzt; dessen Entfernung stellt den vorherigen Text bytegenau wieder her. Eigenständige Werkstatt-Prompts enthalten die benötigten Anweisungen selbst. Installierbare Skills nutzen ergänzend eine paketlokale Referenz.

`python3 scripts/sync-werkstatt-visualisierung.py --check` prüft den veröffentlichten Quellbestand gegen diese Zuordnung. `--write` synchronisiert die Ergänzungen; `--record-review` bindet ausschließlich bereits passende redaktionelle Dateiprüfungen an den ergänzten Stand. Eine vorher schon abweichende Datei erhält dadurch keine nachträgliche fachliche Freigabe. Die Generatoren erzeugen dieselben Ergänzungen; bestehende TXT-Kopien bleiben byteidentisch.

Die Regressionen prüfen vollständige Abdeckung, Fachzuordnung, Quellen- und Dateierhaltung, wiederholbare Synchronisierung, die beiden promptlosen Angebote, funktionsabhängige Rückfallwege und die Übergabe von UI-Auswahlen. Diese Prüfungen belegen keine Live-Ausführung aller Plugins in allen Oberflächen. Für eine konkrete erzeugte Anwendung sind Sichtprüfung, Bedienung und Rechenergebnis im jeweiligen Arbeitslauf gesondert zu kontrollieren.
