# 1. KI-Workshop Bauwirtschaft

Vier Akten verbinden Planung, Bauausführung, Vergabe und kaufmännische Arbeit. Das Plugin **Bauwirtschaft** enthält 20 ausführende Skills. Die Werkstatt und der kompakte Mini-/Schnellstart-Prompt sind eigenständige Markdown-Dateien. Die Testakten werden separat bereitgestellt.

## 1.1. Vorbereitung

Öffne die [Plugin-Übersicht](../bauwirtschaft/README.md) und lade dort das Plugin oder einen der beiden Prompts. Für die Buchhaltungsübungen verwende den erweiterten Stand ab v445.4.0. Das Originalformat-ZIP der gewählten Akte enthält bearbeitbare Excel- und Word-Dateien sowie Rechnungen, Korrespondenz und weitere Belege. Entpacke es in einen eigenen Arbeitsordner. Gesamt-PDF und Einzel-PDFs eignen sich zum Lesen; für Neuberechnungen brauchst du die Originaltabellen.

Arbeite für jede Übung in einer Kopie des Aktenordners. Lade entweder den passenden Fachskill oder den eigenständigen Prompt und ergänze den jeweiligen Arbeitsauftrag unten. Halte beim Vergleich mehrerer Modelle Aktenstand und Auftrag gleich. Ein ausgefülltes Arbeitsblatt oder ein Prüfvermerk eines Beteiligten ist Teil der Fallunterlagen und muss anhand seiner Belege geprüft werden.

| Übung | Akte | Vorschlag für die Dauer | Ergebnis |
| --- | --- | --- | --- |
| HOAI und Bauausführung | Bürgerhaus Einbeck | 45 Minuten | Belegte Phasenübersicht, Prüfvermerk zur Schlussrechnung und Übergabe-/Restpunkteliste. |
| Bauvergabe | Feuerwehrhaus Northeim | 45 Minuten | Angebotsvergleich, Vergabevermerk und begründeter nächster Verfahrensschritt. |
| Baubuchhaltung | Bauunternehmen Bad Salzuflen | 60–90 Minuten | Belegregister, Buchungsvorschläge, OPOS-/Bankabgleich und Zahlungsvorschlag. |
| Projektsteuerung | Werkhalle Warendorf | 30 Minuten | Kostenprognose, Zahlungsplanung und Entscheidungsvorlage. |

Die Übungen sind einzeln verwendbar. Für einen Workshop mit drei Stunden wähle HOAI, Vergabe und Buchhaltung und plane kurze gemeinsame Besprechungen ein.

## 1.2. Akten auswählen

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Akte | Unterlagen und Downloads |
| --- | --- |
| Bürgerhaus Leinewinkel in Einbeck | [44 Originalunterlagen, Gesamt-PDF und beide ZIP-Varianten](../testakten/bauwirtschaft-hoai-buergerhaus-einbeck/README.md). |
| Lüftungslos Feuerwehrhaus Northeim | [32 Originalunterlagen, Gesamt-PDF und beide ZIP-Varianten](../testakten/bauwirtschaft-vergabeverfahren-feuerwehrhaus-northeim/README.md). |
| Bauunternehmen Bad Salzuflen | [18 unterschiedliche Rechnungen, weitere Belege und Tabellen](../testakten/bauwirtschaft-buchhaltung-bauunternehmen-bad-salzuflen/README.md). |
| Werkhalle Warendorf | [30 Originalunterlagen, Gesamt-PDF und beide ZIP-Varianten](../testakten/bauwirtschaft-baumanagement-werkhalle-warendorf/README.md). |

## 1.3. Bürgerhaus Einbeck: Leistungsphasen 1–9

Der Fall betrifft das Leistungsbild Gebäude. Die neun Leistungsphasen sind Grundlagenermittlung, Vorplanung, Entwurfsplanung, Genehmigungsplanung, Ausführungsplanung, Vorbereitung der Vergabe, Mitwirkung bei der Vergabe, Objektüberwachung einschließlich Bauüberwachung und Dokumentation sowie Objektbetreuung. Maßgeblich für die Zuordnung ist [Anlage 10 Nummer 10.1 HOAI](https://www.gesetze-im-internet.de/hoai_2013/anlage_10.html). Der konkret geschuldete Umfang folgt aus dem jeweiligen Vertrag.

Die Akte führt vom Bedarf und Architektenvertrag über Planung und Genehmigung bis zu Bautagebuch, Aufmaß, Nachtrag, Schlussrechnung, Abnahme und späterer Mängelmeldung. Einzelne weitere Gewerke sind nur über das Archivverzeichnis nachgewiesen; die Akte bildet damit einen belegten Ausschnitt des Gesamtprojekts ab.

### 1.3.1. Alle Phasen nachvollziehen

Skill: `hoai-phasen-und-planstaende-abgleichen`.

> Erstelle für das Bürgerhaus Leinewinkel eine Tabelle der Gebäude-Leistungsphasen 1 bis 9. Ordne jeder Phase die vorhandenen Unterlagen mit Dateiname, Datum und maßgeblicher Fundstelle zu. Unterscheide beauftragte Leistung, vorhandenes Arbeitsergebnis und noch fehlenden Nachweis. Zeige bei mehreren Planfassungen, welche Fassung wann maßgeblich war. Leite drei konkrete nächste Arbeitsschritte mit Zuständigkeit ab.

### 1.3.2. Schwerpunkt Leistungsphase 8

Skills: `bautagebuch-und-aufmass-fuehren`, `nachtraege-pruefen-und-vereinbaren`, `baurechnungen-pruefen-und-zahlung-vorbereiten`.

> Prüfe die Schlussrechnung anhand des Bauvertrags, der Nachtragsunterlagen und des gemeinsamen Aufmaßes. Stelle positionsbezogen Vertragssoll, belegte Menge, Preis, bisherige Zahlungen und vorgeschlagenen Prüfstatus gegenüber. Begründe Abweichungen anhand der Originalbelege. Erstelle daraus einen vollständigen Rechnungsprüfvermerk und ein kurzes Anschreiben mit den noch erforderlichen Klärungen. Berücksichtige Bautagebuch und Behinderungsanzeige nur, soweit sie für den konkreten Punkt etwas belegen.

### 1.3.3. Abnahme, Übergabe und Leistungsphase 9

Skills: `maengel-und-abnahme-bearbeiten`, `uebergabe-und-gewaehrleistung-organisieren`.

> Führe Abnahmeprotokoll, Übergabe, Archivverzeichnis, spätere Mängelmeldung und Objektbegehung in einer Restpunkte- und Fristenliste zusammen. Unterscheide die bei der Abnahme festgestellten Mängel von den später gemeldeten Mängeln. Ordne die beauftragten Leistungen den Phasen 8 und 9 zu und benenne fehlende Nachweise. Erstelle den nächsten erforderlichen Brief vollständig. Behaupte keine eigene Ortsbesichtigung und keine technische Freigabe.

## 1.4. Feuerwehrhaus Northeim: Vergaberecht mit Zahlen

Skills: `bauangebote-werten-und-vergabevorschlag-erstellen`, `bieterfragen-und-ruegen-bearbeiten`.

> Bearbeite den Vergabestand des Lüftungsloses zum aktenkundigen Stichtag aus Sicht der Vergabestelle. Prüfe die drei Angebote anhand der bekanntgemachten Anforderungen, des Leistungsverzeichnisses und der rechtzeitig vorliegenden Unterlagen. Rechne den Preisspiegel aus den Originalangeboten nach. Trenne Eignung, Angebotsinhalt, Aufklärung und Zuschlagswertung. Beziehe die Bieterfrage, Antwort, Nachforderung, Rüge und Unterlagen zum Nachprüfungsverfahren ein. Erstelle einen begründeten Vergabevermerk mit Fristen, Zuschlagsstatus und dem jetzt erforderlichen Handlungsschritt.

Als zweite Runde kann ein anderes Team aus Sicht des betroffenen Bieters prüfen. Beide Teams sollen dieselben Originaldateien verwenden. Verglichen werden die tragenden Tatsachen, Berechnungen und rechtlichen Schlussfolgerungen, nicht die Länge der Texte.

## 1.5. Bad Salzuflen: Rechnungen, Buchhaltung und Zahlungsverkehr

Skills: `baubuchhaltung-und-belege-abgleichen`, `baurechnungen-pruefen-und-zahlung-vorbereiten`, `projektliquiditaet-und-zahlungsplan-erstellen`.

Die Akte enthält 18 unterschiedliche Rechnungen aus dem Bauumfeld sowie Korrekturbelege und eine erneut übersandte Rechnungskopie. Der Grundbestand und der ergänzende Belegstapel besitzen getrennte Bankbestände. Die Abgrenzung ist in den Übergabeunterlagen dokumentiert. Der fallinterne Konten- und Steuerschlüsselstamm dient der Übung; ein Export darf nicht ungeprüft als Importdatei einer bestimmten Buchhaltungssoftware behandelt werden.

Die Tabellenformeln decken den gelieferten Belegstapel ab. Wenn du in einer weiteren Runde zusätzliche Rechnungen, Korrekturen oder Zahlungen einfügst, lasse die Formelbereiche erweitern und die Bearbeitungsstände aktualisieren. Prüfe anschließend die Summenbrücken erneut.

### 1.5.1. Belege erfassen

> Erfasse sämtliche Rechnungen und Rechnungskorrekturen in einem Belegregister mit Dateiname, Lieferant, Rechnungsnummer, Beleg- und Leistungsdatum, Projekt, Netto-, Steuer- und Gesamtbetrag, Fälligkeit sowie zugehörigem Leistungsnachweis. Erkenne Mehrfachübersendungen anhand des Inhalts. Verknüpfe Korrekturen mit dem ursprünglichen Beleg und zähle eine Rechnungskopie nicht als neue Verbindlichkeit. Kennzeichne fehlende oder widersprüchliche Angaben.

### 1.5.2. Buchungen vorschlagen und abstimmen

> Gleiche das Belegregister mit den vorhandenen Journalen und offenen Posten ab. Erstelle anhand des fallinternen Kontenstamms einen getrennten Buchungsvorschlag mit Buchungsdatum, Soll, Haben, Steuerschlüssel, Projekt, Betrag und Belegbezug. Begründe Korrekturen. Prüfe Umsatzsteuer und gegebenenfalls Bauabzugsteuer gesondert; bei fehlenden Voraussetzungen bleibt die betreffende Zuordnung als Klärpunkt offen. Führe die zwei Bankbestände getrennt vom jeweiligen Anfangs- zum Schlussbestand fort. Löse Sammelzahlungen, Teilzahlungen, Skonto und Sicherheitseinbehalte belegbezogen auf.

### 1.5.3. Zahlung und Rückfragen vorbereiten

> Erstelle aus dem abgestimmten Stand einen Zahlungsvorschlag mit freizugebendem Betrag, Sicherheitseinbehalt, bereits geleisteten Zahlungen, Fälligkeit und noch offenen Freigaben. Formuliere die erforderlichen Rückfragen an Lieferanten oder Projektleitung vollständig. Zeige die Auswirkung des vorgeschlagenen Zahlungslaufs auf die verfügbare Liquidität. Liefere die Tabellen als bearbeitbare Dateien mit nachvollziehbaren Formeln; löse keine Zahlung aus.

## 1.6. Warendorf: Wirtschaftliche Projektsteuerung

Skills: `baubudget-und-kostenprognose-fortschreiben`, `bauablauf-und-terminplan-fortschreiben`, `projektbericht-und-entscheidungsvorlage-erstellen`.

> Aktualisiere für die Werkhalle Warendorf Kostenprognose, Terminstand und Zahlungsplanung anhand der verspäteten Trafostation und der angebotenen Zwischenlösungen. Trenne Auftrag, Rechnung, Zahlung, Restleistung und Risiko. Vermeide die doppelte Erfassung von Nachtrag und Prognose. Stelle dem Auftraggeber die entscheidungsreifen Varianten mit ihren belegten Mehrkosten und Terminfolgen gegenüber und formuliere eine kurze Entscheidungsvorlage.

## 1.7. Gemeinsame Auswertung

Prüfe für jedes Ergebnis, ob die tragenden Aussagen auf konkreten Originalbelegen beruhen, Berechnungen nachgerechnet werden können und der zeitliche Stand gewahrt bleibt. Gute Ergebnisse unterscheiden fehlende Tatsachen von tatsächlichen Fehlern. Ein genanntes Risiko ersetzt keine Rechnung; eine Tabelle ersetzt keinen bestellten Brief.

Bei der Buchhaltung müssen Anfangsbestand, Umsätze und Schlussbestand je Bankkonto aufgehen. Offene Posten müssen sich aus Rechnungen, Korrekturen, Zahlungen und berechtigten weiteren Abzügen erklären lassen. Bei der HOAI-Übung müssen alle neun Phasen nachvollziehbar zugeordnet sein, ohne fehlende Leistungen als erbracht auszugeben. Bei der Vergabe müssen Preise, Anforderungen und Kommunikationszeitpunkte aus dem Aktenstand stammen.

Vergleiche einen ersten Modelllauf mit einer zweiten Runde, in der du nur einen konkreten neuen Beleg oder eine berechtigte Korrektur nachreichst. Das Ergebnis soll im bestehenden Arbeitsstand fortgeführt werden. Die Akten und vorbereiteten Prüffälle sind Übungsmaterial; automatisierte Datei- und Rechentests belegen keine allgemeine fachliche Fehlerfreiheit eines Modells.
