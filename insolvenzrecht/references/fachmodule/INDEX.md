# Insolvenzrecht: integrierte Fachmodule

Das Hauptplugin bearbeitet anwaltliche Insolvenzmandate, Insolvenzverwaltung, laufende Sachbearbeitung und Berichte mit lokal enthaltenen Fachtexten und Vorlagen. Für diese Aufgaben ist keine Installation der früheren Einzelpakete erforderlich.

## 1. Rolle und bestelltes Arbeitsprodukt entscheiden

Die Akte zuerst lesen und den bereits geklärten Stand fortschreiben. Genau ein führendes Modul öffnen. Ein zweites Modul nur für einen konkreten Übergabepunkt hinzunehmen; keine neue Aktenaufnahme beginnen.

| Ausgangslage | Modul |
| --- | --- |
| Mandat, Antrag, Anspruch, Haftung oder Verhandlung aus anwaltlicher Sicht bearbeiten. | [Anwaltliche Insolvenz- und Sanierungsarbeit](fachanwalt/INDEX.md) |
| Bestellung, Eröffnungsauftrag, Masse, Fortführung oder Verteilung aus Verwalter- oder Sachwaltersicht bearbeiten. | [Insolvenzverwaltung](verwaltung/INDEX.md) |
| Eingänge, Forderungen, Eigentum, Sicherheiten, Kasse, Beschlüsse und Gläubigerbriefe in der konkreten Akte bearbeiten. | [Insolvenzsachbearbeitung](sachbearbeitung/INDEX.md) |
| Zwischenbericht, Schlussbericht, Schlussrechnung, Schlussverzeichnis oder Nachtragsverteilung aus belegten Fachständen erstellen. | [Berichte und Rechnungslegung](berichte/INDEX.md) |

## 2. Eigenständige Spezialwerkzeuge

Eine eigene Gläubigerforderung anmelden, den Eintritt der Zahlungsunfähigkeit oder Überschuldung vollständig rekonstruieren oder einen Insolvenzplan beziehungsweise StaRUG-Plan erstellen: Diese drei Aufträge bleiben bei den dafür separat angebotenen Spezialwerkzeugen. Den geklärten Aktenstand, Zahlen, Belege und offenen Fragen dorthin übergeben. Eine gewünschte externe Anwendung muss tatsächlich verfügbar sein; andernfalls das Übergabepaket und den erreichbaren Download bereitstellen.

## 3. Herkunft und Aktualität

Die Fachmodule werden aus ausdrücklich zugeordneten Bestandsquellen reproduzierbar gebaut. Die Auswahl befindet sich in `scripts/data/insolvenzrecht-fachmodule.json`; [SOURCE_MAP.json](SOURCE_MAP.json) weist jede Quelldatei mit Hash, Ziel, Auswahlgrund und Übernahmeart aus. Die Kopie ist keine erneute materielle Rechtsprüfung. Tragende Normen und Rechtsprechung vor Anwendung anhand aktueller amtlicher Quellen prüfen. Die redaktionelle Änderung erfolgt an der ausgewiesenen Quelle, anschließend wird das Hauptpaket neu erzeugt.
