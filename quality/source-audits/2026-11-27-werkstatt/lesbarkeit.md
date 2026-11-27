# Werkstattprompts lesen und mit einer Akte benutzen

Geprüft wurden die Einstiege und Arbeitsabläufe von 335 Werkstatttexten aus dem Marketplace. Hinzu kommen zehn separat erreichbare Fachtexte. Der Stand der Durchsicht ist der 27. November 2026. Wer eine Akte bearbeiten möchte, findet am Anfang des jeweiligen Prompts die Fachfrage und das bestellbare Dokument. Der ausführliche Ablauf folgt darunter.

## 1. Welche Texte wurden geprüft?

Der Marketplace umfasst 314 Plugins. Ein Plugin kann mehrere Werkstätten oder einen anderen Einstieg haben. Die 335 Markdown-Quellen schließen beispielsweise die neun HOAI-Leistungsphasen, zehn Werkstätten zu §§ 130–139 InsO sowie die verschachtelten Fachwerkstätten zur Verbraucherinsolvenz ein. Gezählt wird jede Werkstatt einmal. Textkopien, ZIP-Dateien, Schnellstarts, Skills und Megaprompts sind eigene Vertriebs- oder Arbeitsformen.

Die zehn weiteren Quellen umfassen sechs weiterhin erreichbare Werkstätten für Arbeitszeugnisanalyse, Bauträgervertrag, Forderungsanmeldung, Insolvenzrecht, Projekteinkauf und Sozialversicherungsstatus. Hinzu kommen die Anspruchswerkstatt des Patentanmelders und die drei eigenständigen Vollworkflows für Vergabestelle, Bieter und unterlegene Unternehmen. [Inventar und Einzelbefunde erzeugen](../../../scripts/werkstatt_lesbarkeit.py)

## 2. Was ergibt die Durchsicht?

| Merkmal | Befund |
| --- | --- |
| Einstieg | Redaktionelle oder fachliche Änderungen betreffen 71 von 335 Marketplace-Werkstätten sowie drei der zehn weiteren Fachtexte. Zusammen sind das 74 Markdown-Quellen. Zehn vorhandene TXT-Fassungen geben den jeweiligen Markdown-Text bytegleich wieder. Die Zahl der Erstabsätze mit mehr als 500 Zeichen sank von 62 auf acht. Der Median liegt bei 346 Zeichen. Besonders dichte Fachpassagen, etwa Einzelprüfungen der Insolvenzanfechtung, bleiben zusammen lesbar. |
| Umfang | Die kanonischen Quellen umfassen 2.214 bis 35.778 durch Leerraum getrennte Wörter, im Median 3.345. Der kürzeste Text führt vom betrieblichen Regelungsbedarf bis zum Vollzug einer Vereinbarung. Die längste Werkstatt bündelt Bauprojektrollen und Leistungsphasen. Eine einheitliche Mindestlänge würde diesen Unterschieden nicht gerecht. |
| Vom Eingang zum Dokument | Für jede Quelle wurden Fachabschnitte, Einstieg, Anhaltspunkte für Ausgangsunterlagen, Fallvarianten, Weiterarbeit und Arbeitsergebnis erfasst. Die kanonischen Texte haben sechs bis 101 Hauptabschnitte. Der erste Absatz steht vor technischen Bedienhinweisen. Bei den drei eigenständigen Vergabe-Vollworkflows folgt die Skill-Tabelle auf die fachliche Anleitung. |
| Weiterarbeit | Sieben Werkstätten erhielten zusätzliche fachliche Abzweigungen. So bekommt eine zweite Kündigung eine eigene Zugangs-, Fristen- und Anhörungsprüfung. Ein nachgereichter Entgeltnachweis wird dem betroffenen Versicherungsmonat zugeordnet. Bei einem neuen Auswertungsbericht im Betrieb werden Zugriffsrechte und die Klausel für den Pilotbetrieb erneut geprüft. |
| Rechtsprechung | Ausgewählte Entscheidungen wurden in die jeweils betroffenen Arbeitsschritte eingearbeitet. Quellenart, konkrete Anwendung und Reichweite stehen zusammen. Der fachliche Nachweis beschreibt auch ältere Fundstellen und offene Quellenprüfungen. [Quellenprüfung und Entscheidungsnachweise](README.md) |

## 3. Drei Beispiele zum Ausprobieren

- **Kündigung.** Erstes Kündigungsschreiben und Zugangsnachweis vorlegen, danach eine weitere Kündigung und die Anhörung des Betriebsrats. Am Entwurf ist prüfbar, welche Frist und welcher Antrag sich auf welche Kündigung beziehen. [Kündigungsschutzwerkstatt](../../../arbeitsrecht-kuendigungsschutzklagewerkstatt/arbeitsrecht-kuendigungsschutzklagewerkstatt-werkstatt.md)
- **Vergabestelle.** E-Mail der Fachabteilung und Leistungsverzeichnis vorlegen, danach eine Bieterrüge. Der Vermerk soll die in Betracht kommenden Teil- und Fachlose sowie die belegten Gründe für die vorgeschlagene Zusammenfassung erkennen lassen. Die Antwort muss den konkreten Einwand behandeln. [Werkstatt der Vergabestelle](../../../vergaberecht-werkstatt/vergabestelle-behoerden/vergabestelle-behoerden-werkstatt.md)
- **Patentanmeldung.** Einen Anspruch mit Schritten auf Gerät und Server vorlegen. Im Erfindergespräch klären, wer die Schritte tatsächlich ausführt und welche Ausführung sich anhand welcher Merkmale nachweisen lässt. Eine neue Anspruchsfassung braucht für jede Änderung eine Offenbarungsstelle. [Patentrechtswerkstatt](../../../patentrecht/patentrecht-werkstatt.md)

## 4. Wie lassen sich die Befunde nachprüfen?

`python scripts/werkstatt_lesbarkeit.py --details` gibt für jeden Text die Länge, den Umfang des ersten Absatzes, die Zahl der Hauptabschnitte und auffindbare Textstellen zu den vier Arbeitsmerkmalen aus. Der gemeinsame Visualisierungsbaustein zählt bei der Suche nach diesen Stellen nicht mit. `python scripts/test-prompt-openings.py` prüft unter anderem den Fließtext vor der ersten Tabelle und erfasst auch die drei eigenständigen Vergabe-Vollworkflows.

Die Fundstellen machen die Durchsicht nachvollziehbar. Ob ein Modell aus einer bestimmten Akte die richtige Klage, Vergabeentscheidung oder Anmeldung erstellt, lässt sich nur an der konkreten Antwort prüfen. Für diese Bestandsaufnahme wurden keine vergleichenden Modellläufe in Claude, ChatGPT oder Pandektes durchgeführt.
