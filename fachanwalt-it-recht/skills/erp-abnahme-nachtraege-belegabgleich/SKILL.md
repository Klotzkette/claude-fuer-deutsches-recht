---
name: erp-abnahme-nachtraege-belegabgleich
description: Prüft bei einem streitigen ERP-Einführungsprojekt Abnahme, ursprünglichen Leistungsumfang und Nachtragsvergütung anhand von Pflichtenheft, Tickets und Freigaben. Liefert eine Leistungs- und Zahlungsbrücke mit konkretem Entwurf; nicht für reine SaaS-Ausfälle, Datenschutzmeldungen oder Lizenzinventare.
---

# 1. Zweck und Anwendungsfall

Ordne ein B2B-Einführungsprojekt, bei dem Schlussrechnung, Fehlerbehebung und vergütungspflichtige Änderungen vermischt werden. Der Schwerpunkt ergänzt allgemeine Software-Mängelprüfung um die versionsgenaue Verknüpfung von Sollfunktion, Test, Abnahme und Nachtrag. Nicht allein aus der Bezeichnung ERP oder aus einem agilen Vorgehen auf einen Vertragstyp schließen.

## 2. Eingaben

Lies Vertrag, Leistungsbeschreibung und priorisierte Fassungen, Zahlungsplan, Änderungsvereinbarungen, Vollmachten, Testprotokolle, Tickets, Abnahmeaufforderungen und Korrespondenz. Erfasse ursprüngliche Erfolgspflicht, Teilabnahmen, Produktivbeginn, Fristen, Mitwirkungsbeiträge, Lizenz- und Betriebsanteile. Bei widersprechenden Versionen Datum, Autor und Freigabestatus nennen. Nur einmal gebündelt nach entscheidenden Lücken fragen; sofort einen bedingten Projektvermerk liefern.

## 3. Ablauf und Checkliste

### 3.1. Vertrags- und Sollmatrix

Ordne Implementierung, Anpassung, Datenmigration, Beratung und laufenden Betrieb nach der konkreten Leistungspflicht ein. Werkvertragsrecht nur für entsprechend eingeordnete Leistungsteile anwenden. Jede Funktion erhält Sollquelle, Version, vereinbarte Testbedingungen, Ist-Ergebnis und Verantwortlichkeit. Eine im Lastenheft beschriebene Anforderung und ein erst später gewünschtes Zusatzmodul dürfen nicht dieselbe Nachtragsbehandlung erhalten.

### 3.2. Tickets und Nachträge

Klassifiziere jedes Ticket begründet als ursprüngliche Leistung, Fehlerbehebung, zusätzliche Änderung oder offenes Mitwirkungsproblem. Prüfe Nachtragsangebot, beauftragte Menge, Preis, Vertretungsmacht, Freigabe und Vertragsmechanik. Eine technische Ticketbestätigung ist nicht automatisch eine kaufmännische Vergütungsfreigabe; das Fehlen einer Unterschrift entscheidet aber ohne Prüfung von Vertretung, Verhalten und Formabrede ebenfalls nicht abschließend. Arbeitsstunden belegen Aufwand, nicht allein einen zusätzlichen Vergütungsanspruch. Bauvertragsrechtliche Nachtragsregeln nicht ungeprüft auf Software übertragen.

### 3.3. Prüfung der Abnahme

Untersuche ausdrückliche, konkludente und fingierte Abnahme getrennt nach Paragraf 640 BGB und Vertragslage. Produktivnutzung allein nicht mechanisch als Abnahme werten; Pilotbetrieb, Kenntnis von Fehlern, Vorbehalte und Erklärungen würdigen. Für die Fiktion Fertigstellung, angemessene Aufforderungsfrist und Reaktion prüfen. Rechtzeitige Verweigerung unter Benennung mindestens eines Mangels ist von der Frage zu trennen, ob die Abnahme wegen nur unwesentlicher Mängel verlangt werden kann. Eine Teilabnahme nicht auf sämtliche Module ausdehnen.

### 3.4. Zahlung und Abhilfe

Bilde je Leistungsteil: vereinbarte Vergütung plus rechtlich belegte Nachträge minus Zahlungen und Gutschriften gleich offener Saldo. Zeige daneben den fälligen und den streitigen Anteil. Noch nicht fällige Vergütung ist kein endgültig erlassener Betrag. Einbehalt nach Paragraf 641 Absatz 3 BGB erst bei seinen Voraussetzungen; Regelansatz des Doppelten erforderlicher Mangelbeseitigungskosten vom vollständigen Mängeleinwand und von Schadensersatz unterscheiden.

Vor Abnahme grundsätzlich Erfüllung und allgemeines Leistungsstörungsrecht prüfen. Mängelrechte nach Paragraf 634 BGB nicht automatisch vorziehen: Ein Abrechnungsverhältnis kann Ausnahmen tragen, aber das bloße Vorschussverlangen genügt nicht. Beabsichtigte endgültige Abkehr vom Projekt als rechtlich erhebliche Entscheidung kennzeichnen. Keine automatische Zweiversuchsregel aus dem Kaufrecht auf das Werk übertragen. Verjährung nach konkreter Anspruchsart und Beginn ermitteln, nicht pauschal fünf Jahre für Softwarewerke behaupten.

### 3.5. Beweis und Abschluss

Sichere eine reproduzierbare Fehlerbeschreibung mit Version, Datenbasis, Schritten, erwarteter und tatsächlicher Ausgabe; personenbezogene Testdaten minimieren. Benenne konkret erforderliche technische Gutachterfragen ohne einen technischen Befund zu erfinden. Prüfe einmal Belegketten, Summen und Alternativen. Keine produktiven Systeme verändern, keine Abnahme oder Kündigung erklären und keine Zahlung zurückhalten oder anweisen; nur Entwürfe und Entscheidungsvorlagen erstellen.

## 4. Quellenpflicht

Nutze [Zitierweise](../../references/zitierweise.md), sofern verfügbar, und prüfe die Normfassung zum Vertrags- und Leistungszeitpunkt.

- [Paragraf 640 BGB](https://www.gesetze-im-internet.de/bgb/__640.html): Abnahme, Fiktion und Vorbehalt.
- [Paragraf 641 BGB](https://www.gesetze-im-internet.de/bgb/__641.html): Fälligkeit und angemessener Einbehalt.
- [BGH, Urteil vom 19.01.2017, Az. VII ZR 301/13](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&nr=77407), amtliche Leitsätze: Mängelrechte grundsätzlich nach Abnahme und Ausnahme des Abrechnungsverhältnisses. Allgemeines Werkvertragsrecht, keine spezifische ERP-Entscheidung. Am 14.09.2026 amtlichen Suchauszug geprüft; Volltextabruf gesperrt. Weitergehende Aussagen und Randnummern nur nach Volltextprüfung.

## 5. Ausgabeformat

Erstelle `ergebnis.md` mit Sachverhalt, einer Tabelle zum Abgleich von vereinbarter Leistung, Tickets und Nachträgen, Abnahmezeitachse, nachvollziehbarer Vergütungsrechnung, Beweisbedarf und ausformuliertem Schreiben zur Abnahme- oder Rechnungsfrage. Vollständige Sätze statt Skeletten, keine unbelegten Erledigungsbestätigungen. Dezimale Überschriften, Times New Roman 11 pt beim Export, bei Markdown entsprechender Exporthinweis. Freigabe und Zugang bleiben bei der Mandatsverantwortung.

## 6. Beispiele

Passend: Nach ERP-Produktivstart verlangt der Anbieter die Schlussrate und berechnet Fehlerbehebung als Zusatzauftrag. Passend ist auch die Prüfung aus Anbietersicht, ob eine benannte Änderungsfreigabe die Rechnung trägt. Nicht passend sind eine reine Datenpannenmeldung oder ein monatlicher SaaS-Verfügbarkeitsstreit ohne Einführungsprojekt.
