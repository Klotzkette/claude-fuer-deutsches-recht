---
name: anlagen-zu-schriftsaetzen
description: "Hauptworkflow für gerichtliche Anlagenproduktion: liest Schriftsatz und Aktenordner zuerst, verbindet jede Behauptung mit ihrem Beleg, hält K-, B-, AST- oder AG-Nummern fort, erkennt Lücken und Dubletten und routet bei bevorstehendem Versand unmittelbar in die beA-Endfertigung mit PDF-, Stempel-, Dateinamen-, Signatur- und Eingangskontrolle."
---

# Anlagen zu Schriftsätzen bauen

## 1. Direktstart

Wenn Schriftsatz und Dateien vorliegen, lies zuerst den maßgeblichen Schriftsatz und erfasse die Dateinamen. Öffne anschließend die darin zitierten Belege; bei großen Ordnern arbeite abschnittsweise und kennzeichne noch nicht gelesene Unterlagen. Frage nicht erneut nach bereits belegten Angaben. Erzeuge eine Belegmatrix und kennzeichne:

1. Anlagenzitate ohne Datei,
2. Dateien ohne Anlagenzitat,
3. widersprüchliche Nummern oder Bezeichnungen,
4. entscheidungserheblichen Vortrag, der nur in einer Anlage steht,
5. Frist-, Lesbarkeits-, Schwärzungs- oder Formatrisiken.

Frage höchstens nach der Rolle oder dem bisher verwendeten Nummernkreis, wenn diese Weiche nicht aus Schriftsatz und Akte folgt.

## 2. Belegmatrix

| Schriftsatzstelle | Tatsachenbehauptung | Beweisangebot | Anlage | Quelldatei | Status |
| --- | --- | --- | --- | --- | --- |
| Seite und Absatz | ausformulierter Tatsachenkern | Urkunde, Zeuge oder anderes Beweismittel | K 1 oder B 1 | eindeutiger Dateiname | vorhanden, fehlt oder widersprüchlich |

Die Reihenfolge folgt dem Beweisgang des Schriftsatzes, nicht dem zufälligen Ordnernamen. Eine Anlage belegt eine im Schriftsatz vorgetragene Tatsache; sie ersetzt den Vortrag nicht.

## 3. Nummernkreis

Klägeranlagen laufen als `K`, Beklagtenanlagen als `B`, Antragsteller- und Antragsgegneranlagen nach dem erkennbaren Gerichts- oder Kanzleistandard. Replik und Duplik setzen den bisherigen Nummernkreis fort. Beginne nie stillschweigend wieder bei 1.

## 4. Produktionsweiche

Wenn nur die inhaltliche Zuordnung offen ist, arbeite die Belegmatrix und Lückenliste ab. Sobald der Schriftsatz versandt werden soll, wechsle ohne erneutes Vollinterview in `bea-versandmappe-endfertigung`.

Das Werkzeug `werkzeuge/build_anlagenkonvolut.py` erzeugt aus vorbereiteten Dateien einen Versandordner und interne Prüfunterlagen. Es stempelt standardmäßig jede Seite und versendet nichts. Die juristische Zuordnung und die anwaltliche Freigabe bleiben vorgelagert.

Der Office-Lauf verwendet ein eigenes temporäres Profil und akzeptiert nur eine neu erzeugte, lesbare PDF. Nach 120 Sekunden endet die Konvertierung der betroffenen Anlage; unter Linux und macOS werden auch ihre Kindprozesse beendet. Sichere den Fehler in der Stop-Liste, bearbeite die übrigen Belege weiter und verlange gezielt einen Ersatzexport. Keine unveränderte Wiederholungsschleife, kein stilles Weglassen der Anlage und keine Versandfreigabe trotz fehlgeschlagener Konvertierung.

## 5. Ergebnis

Liefere je nach Arbeitsstand:

1. Belegmatrix und Lückenliste,
2. fortgeschriebenes Anlagenverzeichnis,
3. konkrete Umbenennungs- und Konvertierungsanweisung,
4. versandfertige Einzel-PDFs und interne Prüffassung,
5. Freigabevermerk und Eingangskontrollplan.

Die Rechts- und Technikanker stehen in `references/BEA-ENDPRODUKTION-RECHT-TECHNIK.md`.
