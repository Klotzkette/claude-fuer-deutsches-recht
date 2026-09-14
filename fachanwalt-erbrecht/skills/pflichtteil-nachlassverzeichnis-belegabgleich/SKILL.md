---
name: pflichtteil-nachlassverzeichnis-belegabgleich
description: "Gleicht ein vorliegendes Nachlassverzeichnis mit Stichtagsauskünften, Kontobewegungen, Immobilienwerten und behaupteten Nachlassschulden ab. Quantifiziert die Pflichtteilswirkung konkreter Abweichungen und trennt Ergänzung, Wertermittlung und Versicherung an Eides statt."
---

# 1. Zweck und Anwendungsfall

Prüfe eine bereits vorliegende Pflichtteilsauskunft auf entscheidende Bestands-, Ermittlungs- und Wertabweichungen. Die Verbindung von hohen Nachlasswerten, vielen Bankbelegen und streitigen Passiva rechtfertigt den Schwerpunkt. Anders als Erstinventar, allgemeine Auskunftsdurchsetzung oder reine Pflichtteilsrechnung beginnt dieser Skill mit dem Widerspruch zwischen Verzeichnis und Gegenbeleg. Nicht für Testamentserrichtung oder eine vollständige Erbauseinandersetzung.

## 1.1. Eingaben

Lies Todesdatum, Erbstatut, Personenstand, Verfügung und Nichterbenstellung, sämtliche Fassungen des privaten oder notariellen Verzeichnisses, Anlagen, notarielle Ermittlungsangaben, Bank- und Depotbestätigungen, Bewertungen, Schuldnachweise und bisherige Aufforderungen oder Titel. Fehlende Familienangaben verhindern nur die endgültige Quote, nicht den Bestandsabgleich. Keine persönlichen Daten in öffentliche Suchanfragen senden.

## 1.2. Ablauf und Checkliste

1. Bestimme Berechtigten, Erben als Auskunftsschuldner und Verzeichnisart. Ein Steuerinventar oder ausländisches Verfahrensdokument ist nicht ohne Prüfung ein notarielles Verzeichnis nach Paragraf 2314 BGB. Bei Titel dessen exakten Umfang lesen.
2. Weise jeder Position einen stabilen Identifikator zu. Vergleiche Ausgangsverzeichnis, Ergänzung und Gegenbeleg mit Dokumentdatum, maßgeblichem Wertstichtag, Betrag, Rechtsinhaber und Streitstatus. Abweichungen nicht durch Wahl des jeweils jüngsten Belegs verdecken.
3. Rekonstruiere Bankbestände zum Todestag. Späterer Saldo plus Auszahlungen minus Einzahlungen kann nur bei vollständiger Bewegungsliste einen Stichtagswert ergeben. Depotverkauf und Verkaufserlös nicht zugleich als Aktivvermögen erfassen. Gemeinschaftskonto, Vollmacht und Eigentum auseinanderhalten; Anteil nicht allein aus Kontobezeichnung bestimmen.
4. Trenne Bestand von Bewertung. Ein verzeichnetes, aber nicht bewertetes Haus löst eine Wertermittlungsfrage aus, nicht automatisch eine Ergänzung des Bestands. Steuerwert und späterer Verkaufspreis sind keine ungeprüften Todestagswerte. Preis, Zustand, Zeitpunkt und Belastungen als Bewertungsbelege prüfen.
5. Prüfe jede behauptete Nachlassschuld nach Entstehung, Rechtsgrund, Gläubiger, Zahlung und Abzugsfähigkeit für den Pflichtteil. Pauschale Pflegevergütung ohne Vereinbarung ist nicht automatisch eine Schuld. Vermächtnisse oder der zu berechnende Pflichtteil dürfen die eigene Basis nicht ungeprüft mindern. Steuerliche Abzugsregeln nicht übernehmen.
6. Klassifiziere den Fehler und leite nur den passenden Weg ab: fehlende Ermittlungen oder ausgelassene Gruppen können Ergänzung tragen; begründete Sorgfaltszweifel führen zur Prüfung nach Paragraf 260 Absatz 2 BGB; reine Wertlücken zur Wertermittlung. Notarielle Eigenrecherche anhand konkreter Spuren prüfen. Paragraf 2314 vermittelt keinen pauschalen Anspruch auf sämtliche Belege wie Paragraf 1379 BGB. Beschaffungsweg und Umfang jeder Unterlagenanforderung begründen.
7. Rechne unstreitige reale Masse und Abweichungsvarianten: Aktiva minus zulässige Passiva, darauf Pflichtteilsquote. Für jede Korrektur finanzielle Wirkung zeigen. Schenkungen als separate mögliche Ergänzungsmasse mit Vollzugsdatum, Gegenleistung, Nutzungsrecht und eigener Prüfung führen, nicht als noch vorhandenes Guthaben addieren. Anrechnung und Ausgleichung bei Hinweisen gesondert prüfen.
8. Liefere nach höchstens einer gebündelten Rückfrage die Teilrechnung und eine bestimmte Nachforderung. Verjährung und titulierte Erfüllung gesondert behandeln; eine bloße Aufforderung nicht als sichere Hemmung ausgeben. Keine Erklärungen, Vergleiche, Bankanfragen oder Vollstreckung eigenmächtig veranlassen.

## 1.3. Quellenpflicht

Optional ergänzt die [Zitierweise](../../references/zitierweise.md) die Quellenarbeit. Entscheidungen mit Gericht, Datum, Aktenzeichen und überprüfter Fundstelle zitieren; Dokumentbefund und Schlussfolgerung trennen. Prüfstand 14.09.2026; vor Verwendung aktualisieren.

- BGB [Paragraf 2314](https://www.gesetze-im-internet.de/bgb/__2314.html), [Paragraf 2311](https://www.gesetze-im-internet.de/bgb/__2311.html), [Paragraf 260](https://www.gesetze-im-internet.de/bgb/__260.html) und [Paragraf 2303](https://www.gesetze-im-internet.de/bgb/__2303.html): Auskunft, Todestagsbewertung, Sorgfaltsprüfung und Quote.
- BGH, Urteil vom 20.05.2020, Az. IV ZR 193/19, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IV_ZS/2019/IV_ZR_193-19.pdf?__blob=publicationFile&v=1), Randnummern 8 bis 11: eigenständige notarielle Ermittlungen, Mitwirkung des Erben und Ergänzung bei verweigerter Mitwirkung. Nicht jede inhaltliche Beanstandung rechtfertigt ein neues Verzeichnis.

## 1.4. Ausgabeformat

`ergebnis.md` enthält Sachverhalt, Abweichungstabelle mit Euro-Auswirkung, belegte Ausgangs- und Variantenrechnung, nach Fehlerart getrennte Nachforderung und einen ausformulierten Briefentwurf an den Erben. Bei Titel zusätzlich begründete Verfahrensempfehlung, kein automatischer Vollstreckungsantrag.

Ausformulierungspflicht: vollständige Sätze, keine Skelette. Formatstandard: Times New Roman 11 pt und dezimale Gliederung mit Leerzeilen; bei Markdown Exporthinweis. Nur tatsächlich erzeugte Dateien verlinken.

## 1.5. Beispiele

Das Verzeichnis verwendet den Kontosaldo einen Monat nach dem Tod und zieht eine unbelegte Pflegeforderung ab. Rekonstruiere den Todestag anhand vollständiger Buchungen und zeige die Pflichtteilswirkung des bestrittenen Abzugs. Eine separate unbekannte Bankverbindung verlangt Ermittlungen, keinen erfundenen Guthabenansatz.
