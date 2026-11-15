# Vier gemeinsame Fachplugins und ihre erhaltenen Akten

Die gemeinsamen Plugins verbinden die bisherigen Arbeitswege und Fachbibliotheken. Wählen Sie das benötigte Ergebnis im jeweiligen Plugin. Alle bisherigen Testakten, Originaldateien, Vorlagen und veröffentlichten Akten-Downloads bleiben erhalten.

## 1. Gemeinsame Einstiege

| Bisherige Zugänge | Gemeinsames Plugin | Aktive Skills | Aktenbestand |
| --- | --- | --- | --- |
| Bauträgervertrag-Prüfer und Bauträgervertragsprüfer | [Bauträgerverträge](../../../bautraegervertrag-pruefer/README.md) | 10 | Birkenpfuhl sowie die beiden lokalen Vertragsakten Hohenwartshofen und Marewald |
| Arbeitszeugnis-Analyse und Arbeitszeugnisprüfer | [Arbeitszeugnisprüfer](../../../arbeitszeugnispruefer/README.md) | 8 | Zentrale Analyseakte und vollständige lokale Dokumentensammlung |
| Sozialversicherungsstatus-Prüfer und Sozialversicherungspflicht-Prüfer | [Sozialversicherungspflicht und Status](../../../sozialversicherungspflicht-pruefer/README.md) | 14 | Alle zwölf bisherigen Fälle |
| Projekteinkauf Baubranche und Bauunternehmer Einkauf | [Bauunternehmer Einkauf](../../../bauunternehmer-einkauf/README.md) | 14 | Sieben Einstiegsakten und drei Krimpfort-Akten |

Die bisherigen Ordner bleiben als Wegweiser und Quellarchive erreichbar. Im aktuellen Marketplace wird je Paar das gemeinsame Paket ausgewählt. Die historischen Manifeste, Fachtexte und eigenständigen Prompt-Dateien sind weiterhin nachvollziehbar; für die laufende Arbeit dienen die gemeinsamen Anleitungen.

## 2. Fachliche Zusammenführung

Die Menüs bilden konkrete Aufgaben ab. Die Bauträgerprüfung unterscheidet Erwerber, Bauträger, GdWE und Verwaltung. Die Zeugnisprüfung verbindet Gesamtprüfung, begrenzte Analyse und Fassungsvergleich. Die Statusprüfung trennt Beschäftigung, Versicherungszweige, Beiträge und das bei Auslandsbezug vorrangig zu bestimmende Sozialversicherungsrecht. Der Einkauf führt Einsteiger ebenso wie den Projekteinkauf durch LV-Erstellung, Recherche, GAEB, Vergleich, Verhandlung und Abwicklung.

Zusätzliche Fachtexte sind innerhalb des gemeinsamen Pakets erreichbar. Widersprüchliche Anleitungen wurden an der aktiven Zielfassung bereinigt; insbesondere darf eine bloße Mängelanzeige nicht als allgemeine Verjährungshemmung behandelt und eine Zeugnisnote nicht durch pauschale Wortwerte und mechanische Notenabzüge berechnet werden. Die Originalfassungen bleiben im bisherigen Quellordner dokumentiert. Die gezielten Fachprüfungen und ihre Grenzen stehen in den jeweiligen Prüfprofilen; die Zusammenführung ist keine pauschale Neuprüfung sämtlicher historischen Rechtsquellen.

## 3. Schutz der Testakten

Ausgangsstand ist Commit `29b4fb0684eb15d0e4cf2f68c5d9653ff43c8637`. Der [Erhaltungsbestand](erhaltungsbestand.json) erfasst alle versionierten Dateien in Testakten- und Fixture-Verzeichnissen sowie sämtliche versionierten PDF-, Office-, ZIP-, E-Mail-, Bild- und GAEB-Artefakte. Die Markdown-Arbeitsanweisungen im Hilfsordner `testakten/megaprompts` sind keine Fallakten und dürfen fachlich fortgeschrieben werden.

Der Validator vergleicht alle 20.079 geschützten Dateipfade und ihren vollständigen Inhalt mit der ursprünglichen Git-Blob-ID. Nur für im Ausgangscommit ausdrücklich als Text mit Zeilenenden-Regel markierte Dateien berücksichtigt er die Git-konforme LF/CRLF-Darstellung. Binärdateien und nicht entsprechend markierte Texte bleiben bytegenau geschützt; nachträglich geänderte Attribute lockern die Prüfung nicht. Auch die früheren Plugin-Quellen bleiben bytegleich erhalten; bei einer Wegweiser-README wird die danebenliegende vollständige `README-bestand.md` geprüft. Die Prüfung benötigt keine heruntergeladenen oder manuell nachgetragenen Prüfsummen. Sie erkennt fehlende Dateien und veränderte Inhalte.

Die bisherigen Qualitätsprofile der vier bisherigen Zugänge liegen unverändert unter [legacy-evals](legacy-evals/). Die aktuellen Profile gehören den vier gemeinsamen Plugins. Historische Prüfstände werden durch eine neue Pfadzuordnung nicht als frisch geprüft ausgegeben.

Die neun Regressionstests des Erhaltungsprüfers testen unter anderem gelöschte und verfälschte Akten, verlorene Aktenverweise, fehlende Quellarchive und eine versehentlich doppelte Marketplace-Auswahl. Der Erhaltungsnachweis wird vor Veröffentlichung dieser Zusammenführungsrunde erneut geprüft. Er ist der Nachweis für diesen Änderungssatz, kein Verbot späterer ausdrücklich beauftragter Aktenüberarbeitungen.

## 4. Veröffentlichung und Installationen

Die vier gemeinsamen Pakete werden als `qualitaetsrunde-v445.36.5` über den bestehenden geschützten Komponentenworkflow veröffentlicht. Die Paketprüfung vergleicht alle enthaltenen Dateien mit dem geprüften Checkout und kontrolliert erreichbare Fachtexte sowie höchstens 20 aktive Skills. Der Publisher lädt die erzeugten Assets erneut herunter und prüft sie vor der öffentlichen Freigabe.

Die Akten werden in dieser Runde weder neu erzeugt noch ersetzt. Ihre bestehenden versionierten Downloadadressen bleiben maßgeblich. Bereits veröffentlichte Releases und Tags bleiben erhalten.

## 5. Prüfwege

- [Maschinenlesbare Zuordnung](../../../scripts/plugin-consolidations.json)
- [Erhaltungsprüfung](../../../scripts/validate-plugin-consolidation.py)
- [Regressionen des Erhaltungsprüfers](../../../scripts/test-plugin-consolidation.py)
- [Struktureller Ausgangsbericht](../../pluginstruktur-2026-11-15/README.md)

Die Prüfung umfasst Dateiintegrität, Verweise, auswählbare Arbeitswege und Paketinhalte. Ein tatsächlicher Import oder eine Ausführung aller Arbeitsabläufe in jeder unterstützten KI-Oberfläche wird damit nicht behauptet.

## 6. Nachgewiesener Umfang

Der aktuelle Marketplace enthält 311 Plugins und 3.153 auswählbare Skills. Die Aktenübersicht bleibt bei 631 zentralen und 643 insgesamt erfassten Testakten. Alle 20.079 geschützten Originaldateien sind unverändert; darunter befinden sich sämtliche 18.712 Fall- und Fixture-Dateien des Ausgangsstands. Die vier gemeinsamen Plugins verweisen auf alle bisherigen Fallbestände.

Der Paket-Vorabbau erzeugt 14 Dateien: vier native Plugin-ZIPs, acht eigenständige Promptdateien, Inventar und Prüfsummen. Die abschließende Veröffentlichung baut erneut aus dem sauberen Merge-Commit und prüft die wieder heruntergeladenen Dateien. Die alten Quellarchive sind bewusst von der aktiven Auswahl getrennt; unbekannte zusätzliche Manifeste und Skillordner bleiben Prüfungsfehler.

Bei den Gesamtprüfungen fiel außerdem eine bereits bestehende Unstimmigkeit zwischen dem BAV-Ersatzregister und zwei Prüfwerkzeugen auf. Beide Werkzeuge prüfen nun das ausdrücklich registrierte Originalarchiv, dessen Bytes sowie die tatsächlich erreichbaren aktuellen Fachkapitel. Die BAV-Fachtexte wurden dabei nicht geändert. Historische Vollreviews von Gesellschafterstreit und Wirtschaftsanwalt bleiben erhalten; ihre Navigationsrevision belegt ausschließlich die Ersetzung der Marketplace-Zahl 315 durch 311.
