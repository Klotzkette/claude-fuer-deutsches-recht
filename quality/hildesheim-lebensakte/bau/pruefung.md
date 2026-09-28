# Prüfung der Bauunterlagen zur Hildesheimer Lebensakte

Stand: 28. September 2026. Alle Projektdaten, Namen, Messungen und Ausführungsmeldungen sind fiktive Übungsdaten. Die bestehenden 198 Ausgangsdateien wurden durch diesen Generator nicht verändert.

## Umfang

98 zusätzliche Originale: 95 Worddateien mit 459 Seiten und drei CSV-Register. Darin enthalten sind zehn monatliche Bautagebücher mit genau 304 Tagesseiten vom 1. Dezember 2027 bis 29. September 2028, sieben Detailleistungsverzeichnisse mit 134 Positionen auf 74 Seiten, 16 Begehungsprotokolle, zwölf Befund- und zwölf Nachkontrollprotokolle, 28 Materialempfangsbelege, acht bearbeitbare Bauvorlagen, ein Berichtigungsblatt zum überlieferten Kurzauszug sowie ein vierseitiger Personalabgleich. Der separate Bautagebuchband umfasst genau 304 Seiten und zählt nicht als zusätzliches Original.

Die Detailpositionen erklären die unveränderten 26 Ausgangsgruppen und sieben Lospauschalen von zusammen 2.080.000 EUR netto. Sie verwandeln die bestehenden Pauschalverträge nicht in Einheitspreisverträge. Nachtrag 01 über 18.000 EUR netto wird getrennt geführt. Materialempfangsbelege erzeugen weder zusätzliche Rechnungen noch neue Kosten neben dem bestehenden Vertragsumfang.

## Technische und rechnerische Kontrollen

`bauwirtschaft_hildesheim_lebensakte_bau.py --check` prüft die lückenlose Tagesfolge, sämtliche Los- und Gruppensummen, 28 eindeutige Lieferbelege, 23 überlieferte Anker, zwölf Befundfolgen sowie die Feiertage anhand einer unabhängigen gregorianischen Osterberechnung. Auf Feiertagen stehen keine produktiven Arbeitsgänge oder Kolonnen. Die ruhige Vorbegehung am Sonntag, 10. September 2028, bleibt von gewerblicher Ausführung getrennt.

Zusätzliche Flussprüfungen sichern 90 m³ Bodenplattenbeton, 246 m³ Deckenbeton, 150 m³ Gründungspolster und 48 Fenster. Beton wird nur an den jeweiligen belegten Liefertagen eingebaut. Fenstereinbau überschreitet zu keinem Datum den angelieferten Bestand. Alle ausgewiesenen Ruhetagsstände stimmen exakt mit dem zuletzt dokumentierten produktiven Stand überein; stückweise Einheiten bleiben ganzzahlig. Montageanteile einer Anlage werden als geschätzte Prozentfortschritte und ausdrücklich nicht als abnahmefähiger Mengenbeleg beschrieben.

Nachtrag 01 ist vom 7. bis 11. Februar 2028 mit täglich drei Mitarbeitern und je 11,4 zusätzlichen Stunden belegt. Seine Tagesmengen summieren sich zu 60 m³ Aushub, 45 m³ Filtermaterial, 30 m Leitung und 57 Stunden. Jeder Tag mit tatsächlichem Arbeitsgang oder Nachtragsausführung hat einen produktiven Personalstand größer null.

Alle 23 überlieferten Kurzvermerke wurden einzeln mit den parallelen Arbeitsgängen abgeglichen. Der ausdrücklich auf den 29. September 2028 datierte Personalabgleich von Nora Feld und Hans Müller unterscheidet gewerbliche Tagesbesetzung, einzelne Montagegruppen und Besprechungsteilnehmer. Am 25. August gehören die ursprünglichen fünf Personen zur Aufzugsmontage; mit den vier anderen Gewerken sind insgesamt 19 gewerblich eingesetzte Personen belegt. Die Originaldatei 050 bleibt unverändert. Für die technischen Prüfungen wurden die Originale 163 bis 165 vollständig abgeglichen: HLS- und Lüftungsmessungen am 6. September, Elektroprüfungen aller neun Verteilungen am 7. September; am 8. September folgen Dokumentenübergabe und Einweisung, keine erst später abgeschlossene Messung.

Vier gezielte Mutationstests bestätigen die Fehlererkennung bei einem falschen Fenster-Ruhetagsstand, fehlendem Personal am Nachtragstag, Fenstereinbau vor der Lieferung und verdoppelten Nachtragsstunden. Ergebnis: vier von vier fehlerhafte Varianten zurückgewiesen; Einzelheiten in `mutationstests.json`.

## Berichtigung des überlieferten Datums

Der ursprüngliche Kurzauszug vom 5. Juni 2028 bleibt erhalten. Das ausdrücklich datierte Berichtigungsblatt vom 6. Juni 2028 ordnet die irrtümlich auf Pfingstmontag eingetragenen Trockenbau- und Leitungsarbeiten mit zwölf Personen dem tatsächlichen Ausführungstag 6. Juni zu. Als erklärende Personen sind Jan Merz und Elif Sand benannt. Es handelt sich nicht um eine rückwirkende Umdeutung einer Ist-Ausführung zur Planung.

## Rendering und Sichtprüfung

Alle 95 Worddateien wurden mit dem gebündelten LibreOffice über den Renderer des Dokumenten-Skills in PDF und Seiten-PNG umgewandelt. Die 95 Quellhashes, PDF-Pfade, Seitenzahlen und PNG-Verzeichnisse stehen in `renderindex.json`; die 98 Originalhashes stehen in `manifest.json`. Sämtliche Quellhashes und Seitenzahlen wurden abschließend erneut gegen die tatsächlichen Dateien geprüft. Es gibt keine überzähligen Tagesseiten. Alle Monatsseiten enthalten genau ein Tagesblatt mit dem passenden Datum.

Die 155 Seiten außerhalb der monatlichen Bautagebücher wurden vollständig visuell gelesen und geprüft: alle LV-Seiten, Begehungen, Mängelakten, Lieferbelege, Bauvorlagen, das Berichtigungsblatt und der Personalabgleich. Geänderte Einzelblätter wurden erneut gerendert und erneut vollständig geprüft. Die Sichtprüfung fand keine abgeschnittenen Texte, Tabellenkollisionen, fehlenden Zeichen, leeren Folgeseiten oder blauen Titelbalken. Die Dateien verwenden Times New Roman und lesbare, ausdrücklich dimensionierte Tabellen.

Zusätzlich wurden alle 134 Seiten der abgeleiteten PDF-Lesefassung des LV-Kalkulationsregisters und alle zwölf Seiten des Mängelregisters visuell geprüft. Der Datensatzmodus ist einfach gestaltet, aber sämtliche Felder und Texte sind lesbar; es gibt keine abgeschnittenen Einträge oder Kollisionen. Die Prüfung erfasste jede Seite, keine Stichprobe. Die zugehörigen Renderquellen und Hashes liegen im zentralen Paketindex unter `/tmp/hildesheim-lebensakte/pakete-qa/index.json`.

Die vollständige unabhängige Sichtprüfung der 304 monatlichen Bautagebuchseiten erfolgt durch die beiden parallelen Prüfstränge Finanz und Planung; deren Abschluss wird im übergreifenden Prüfprotokoll dokumentiert. Alle 304 Seiten wurden bereits einmal unabhängig gelesen. Die gezielt geänderten Monatsseiten wurden den beiden Prüfsträngen zur abschließenden erneuten Sichtung übergeben; `finale-monatsaenderungen.json` bezeichnet jede betroffene Seite und den finalen Quellhash. Die monatlichen Quellstände sind nach Berichtigung der Ruhetagsberechnung, Nachtragsbesetzung, Personalzuordnung, technischen Prüftermine und rückblickenden Formulierungen eingefroren. Keine Vorabfassung darf den finalen Quellhash ersetzen.

Der veröffentlichte Bautagebuch-Gesamtband wird mit `--render` aus genau den zehn Monats-PDFs zusammengesetzt. Für jede seiner 304 Seiten wurden Text und unkomprimierter PDF-Inhaltsstream mit der zugehörigen Monatsseite verglichen: identisch. So gibt es keinen zweiten, abweichend umbrechenden Satz derselben Tagesberichte.

## Quellen und Grenzen

Die rechtlichen und technischen Grundlagen mit konkreten Abruf- und Aussagegrenzen stehen in `quellen.md`. Es werden keine unzugänglichen DIN- oder VDE-Einzelanforderungen frei erfunden. Projektmengen sind transparente Fiktion und ersetzen keine Ausführungsplanung, Tragwerksberechnung oder Fachmessung. Datierte Originale beschreiben den am jeweiligen Tag bekannten Zustand; spätere Erkenntnisse werden nicht vorweggenommen.
