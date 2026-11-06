# Quellen und Übermittlungswege für die Umsatzsteuer-Voranmeldung

## 1 Steuerliche Primärquellen

Die am 6. November 2026 geprüften Einstiege sind anhand des konkreten Besteuerungszeitraums zu verwenden. Bei einer historischen Anmeldung sind die damals geltenden Fassungen maßgeblich.

| Quelle | Aussage und Prüfgrenze |
| --- | --- |
| [§ 18 UStG](https://www.gesetze-im-internet.de/ustg_1980/__18.html) | Voranmeldung, Turnus, Abgabe und Zahlung. Die Jahresregel und Sonderfälle nachprüfen. |
| [§ 13 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13.html) und [§ 20 UStG](https://www.gesetze-im-internet.de/ustg_1980/__20.html) | Entstehungszeitpunkt und gestattete Istbesteuerung. EÜR und Vorsteuerzeitpunkt separat prüfen. |
| [§ 15 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html) | Abzug, Ausschluss und Aufteilung. Rechnung, Leistung und Vorauszahlung unterscheiden. |
| [§ 17 UStG](https://www.gesetze-im-internet.de/ustg_1980/__17.html) | Änderung der Bemessungsgrundlage und Zeitraum der Berichtigung. |
| [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) | Kleinunternehmerbefreiung, Verzicht und besondere Erklärungspflichten. |
| [§ 168 AO](https://www.gesetze-im-internet.de/ao_1977/__168.html) | Wirkung der Steueranmeldung und Zustimmung bei Herabsetzung oder Vergütung. |
| [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html) | Gesetzliche Anzeige- und Berichtigungspflichten. Ein Rechtsbehelf gegen eine abweichende Festsetzung ist gesondert einzuordnen. |
| [BFH, Urteil vom 25. Juni 2025, XI R 17/22](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202520301/) | Leitsatz 2 und Rn. 24 begrenzen die Rückwirkung beim erstmaligen Steuerausweis. Der Fall betrifft keine allgemeine Freigabe beliebiger Rechnungsberichtigungen. |

## 2 Formulardatenimport

Die [amtliche Hilfe zum UStVA-Upload](https://www.elster.de/eportal/helpGlobal?themaGlobal=ustva_upload) dokumentiert den Portalimport. Verwenden Sie den jahrespassenden Nutzdatenblock `Anmeldungssteuern`, ISO-8859-15 und die aktuellen Importregeln. `Kz09` sowie bestimmte Namens- und Beraterfelder werden dabei ausgelassen. Prüfen Sie den tatsächlichen Import im Formular.

Die erforderlichen Schemata und Jahresplausibilitäten liegen laut ELSTER in der ERiC-Dokumentation. Ein öffentliches Beispiel mit der Version 2023 ist kein verifiziertes Schema für andere Jahre. Ein Rechnungs-XML und ein eigener Datenexport sind andere Datenarten. Eine Schemafreigabe, ein erfolgreicher Formularimport und die Annahme einer Anmeldung sind jeweils eigene Nachweise.

## 3 Authentifizierte Übermittlung

Die [amtliche Entwicklerseite](https://www.elster.de/elsterweb/infoseite/entwickler) beschreibt ERiC als Bibliothek für Steueranwendungen. Die lokale Anwendung benötigt das passende Jahresmodul und eine tatsächlich unterstützte Übermittlungsfunktion. Entwicklerzugang, Jahresdokumentation und Herstellerintegration sind keine automatisch im Plugin enthaltenen Fähigkeiten.

Für den Portalweg oder eine vorhandene lokale Integration verwendet der Nutzer seine geschützte Anmeldung. Zertifikatsdatei und PIN beziehungsweise Passwort werden weder im Chat angefordert noch in Datenexporte oder Protokolle geschrieben. Der konkrete Abgabeauftrag wird mit dem endgültigen Datensatz abgeglichen.

## 4 Lokale Vorbereitungshilfe

Die Vorbereitungshilfe unter `werkzeuge/ustva_ausgabe.py` erzeugt aus strukturierten, geprüften Felddaten die dokumentierten lokalen Ausgaben. Ihr Aufruf und ihre Eingabeanforderungen stehen bei dem Werkzeug. Sie ersetzt keine steuerliche Belegprüfung und keine amtliche ERiC-Plausibilisierung. Prüfen Sie ihren gemeldeten Status und den späteren Formular- oder Annahmenachweis gesondert.

## 5 Redaktioneller Prüfstand

Skill, Werkstatt und Mini wurden anhand von gesetzlichen Grundlagen, amtlichen ELSTER-Hinweisen und synthetischen Aufgaben redaktionell geprüft. Ein echter Login, eine Übermittlung für einen Steuerpflichtigen und ein bestätigter Import in Mein ELSTER gehören nicht zu diesem Prüfstand.
