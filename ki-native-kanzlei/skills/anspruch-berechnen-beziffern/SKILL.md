---
name: anspruch-berechnen-beziffern
description: Beziffert Geldansprüche aus Rechnungen, Gutschriften und Zahlungen. Trennt Hauptforderung, Verzugsbeginn, Zinsabschnitte, Tilgungsbestimmung und Nebenforderungen; liefert eine nachrechenbare Forderungsaufstellung und betragsgleiche Anträge statt einer bloßen Rechnungssumme.
---
# Geldansprüche nachvollziehbar berechnen und beantragen

## 1. Zweck und Anwendungsfall

Erstellen Sie die belastbare Bezifferung für Zahlungsaufforderung, Klage, Erledigung nach Teilzahlung oder Vollstreckungsauftrag. Beginnen Sie mit dem gewünschten Stichtag und Anspruch. Dieser Skill bucht kein Geld und ersetzt weder den Buchhaltungsbestand noch die rechtliche Prüfung des Anspruchsgrundes. Ein tituliertes Zinsmaß wird nicht durch ein vermeintlich günstigeres gesetzliches Maß ersetzt.

## 2. Eingaben

Lesen Sie Vertrag oder Titel, Rechnungen, Gutschriften, Mahnungen samt Zugang und Buchungsbelege. Erfassen Sie die Parteienrolle, den Leistungszeitraum, Umsatzsteuerbehandlung, Zahlungszweck und tatsächlichen Geldeingang. Fragen Sie gezielt nach fehlendem Zahlungstag oder Zugangsnachweis. Fehlt nur ein Zinssatz, berechnen Sie die belegte Hauptforderung weiter und weisen die Zinsen als noch offen aus, nicht als null.

Übernehmen Sie Zahlen mit Dokumentfundstelle. OCR-Verwechslungen bei Dezimalzeichen, Währung und Rechnungsnummer sind am Bild zu kontrollieren. Rechnung und dieselbe Rechnung als E-Mail-Anhang sind eine Forderung, nicht zwei.

## 3. Ablauf

### 3.1. Forderungen voneinander trennen

Erfassen Sie pro Forderung Rechtsgrund, Brutto-/Nettobetrag, Fälligkeit und Einwendungen. Verwechseln Sie die Umsatzsteuer einer Vergütungsforderung nicht mit einem nur unter bestimmten Voraussetzungen ersatzfähigen Steueranteil eines Schadens. Eine bestrittene Gutschrift und eine behauptete Gegenforderung sind getrennte Sachverhalte. Aufrechnung, Zurückbehaltung und Erfüllung erhalten jeweils eine eigene Prüfung.

### 3.2. Zahlungen richtig zuordnen

Ordnen Sie Zahlungen zuerst anhand einer wirksamen Tilgungsbestimmung zu. Prüfen Sie bei mehreren Schulden Paragraf 366 BGB und innerhalb einer Schuld Paragraf 367 BGB. Eine eindeutige Vereinbarung kann den gesetzlichen Auffangweg verdrängen; dokumentieren Sie auch einen Widerspruch des Empfängers. Ziehen Sie Teilzahlungen nicht einfach immer vollständig von der Hauptforderung ab. Ungeklärte Zuordnungen bekommen zwei ausdrücklich bezeichnete Rechenvarianten, keine stillschweigende Entscheidung.

### 3.3. Zinslauf belegen

Trennen Sie Fälligkeit, Verzug und Rechtshängigkeit. Bei einer Entgeltforderung ohne Verbraucherbeteiligung prüfen Sie den besonderen Zinssatz; nicht jede Forderung zwischen Unternehmen ist eine Entgeltforderung. Bestimmen Sie den Basiszinssatz nach der amtlichen Veröffentlichung für jeden betroffenen Zeitraum. Teilen Sie den Lauf bei Satzwechsel, Teilzahlung oder Kapitaländerung auf. Legen Sie Tageszählung und Rechenstichtag offen, vermeiden Sie doppelt gezählte Zahlungstage. Verwenden Sie Dezimalrechnung und runden Sie erst nach der erklärten Methode auf Cent.

Prüfen Sie gesondert vorgerichtliche Kosten, Verzugspauschale und Anrechnung. Aus einer einmal verzinsten Forderung wird ohne Rechtsgrund keine Zinseszinsforderung. Bei Titeln lesen Sie Wortlaut und Beginn exakt ab. Bleibt ein aktueller Basiszinssatz unverifiziert, liefern Sie die Rechenformel und benennen genau die fehlende Quelle.

### 3.4. Gegenkontrolle und Antrag

Kontrollieren Sie unabhängig: Ausgangsforderungen minus belegte Gutschriften minus wirksam zugeordnete Tilgung müssen den ausgewiesenen Rest ergeben. Prüfen Sie erste und letzte Zinsperiode sowie den Tag jeder Teilzahlung. In einer Tabelle bleiben Eingaben, Formeln und Quellen unterscheidbar. Eine reine CSV enthält keine vorgeblich geprüften Tabellenformeln.

Formulieren Sie den Zahlungsantrag mit dem richtigen verbliebenen Kapital und abgestuften Zinsanträgen. Bei Zahlung während des Prozesses geben Sie den Vorgang an `schriftsatz-ueberarbeiten-erwidern`; erklären Sie weder Erledigung noch Rücknahme automatisch. Bei einem Titel folgt `titel-pruefen-vollstreckung-planen`. Speichern Sie Fassung und Stichtag, nicht bei jedem Aufruf eine zusätzliche Forderung.

## 4. Quellenpflicht

Maßgeblich sind Paragrafen 247, 286, [288](https://www.gesetze-im-internet.de/bgb/__288.html), 289, 291, 362, 366 und [367 BGB](https://www.gesetze-im-internet.de/bgb/__367.html), bei titulierten Ansprüchen zunächst der Titel. Belegen Sie den historischen Basiszinssatz über die Deutsche Bundesbank. Eine allgemeine Verzugspassage aus einer Entscheidung ersetzt weder den eigenen Zugangsnachweis noch die Anspruchsprüfung. Prüfen Sie spezialgesetzliche Fälligkeit und Zinsregeln im betroffenen Mandat, insbesondere im Arbeits- und öffentlichen Recht.

## 5. Ausgabeformat

Liefern Sie eine prüfbare Aufstellung mit Belegbezug, Zinsperioden und Zahlungszuordnung sowie den ausformulierten Antrag und einen kurzen Mandantenhinweis zu offenen Beträgen. Bei Dateizugriff erstellen Sie eine bearbeitbare Tabelle und eine lesbare PDF-Fassung; andernfalls eine kopierbare Tabelle. Begleittext in Times New Roman 11 pt, dezimale Gliederung. Ungeprüfte Annahmen stehen nur im internen Rechenvermerk. Versand oder Einreichung bleiben gesondert freizugeben.

## 6. Beispiele

### 6.1. Zahlung auf eine einzelne Rechnung

Die Rechnung beträgt 14280 Euro, eine bestätigte Gutschrift 1190 Euro. Für die Zahlung von 5000 Euro ist ausdrücklich die Hauptforderung dieser Rechnung vereinbart. Der Kapitalrest beträgt 8090 Euro. Zinsen werden dennoch nach den tatsächlichen Zeitabschnitten berechnet; aus dem heutigen Rest darf nicht rückwirkend der gesamte Zinslauf entstehen.

### 6.2. Titel mit neun statt fünf Prozentpunkten

Der Titel weist fünf Prozentpunkte über dem Basiszinssatz aus. Der Mandant verlangt nun neun, weil beide Parteien Unternehmer sind. Bereiten Sie nur den titulierten Umfang für die Vollstreckung vor. Eine zusätzliche materiell-rechtliche Forderung bedarf eines eigenen Auftrags und eines eigenen Prüfwegs.
