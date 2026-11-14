---
name: anlagen-stempel-und-deckblattlogik
description: "Entwickelt eine widerspruchsfreie Stempel- und Konvolutlogik für gerichtliche Anlagen: setzt K-, B-, AST- oder AG-Bezeichnungen auf jede Seite oben rechts, wahrt den bestehenden Nummernkreis, verhindert Überdeckung, gliedert echte Konvolute nachvollziehbar und gleicht Stempel, Dateiname, Deckblatt, Verzeichnis und Schriftsatzbezug ab."
---

# Stempel- und Deckblattlogik

## 1. Grundregel

Die Anlagenbezeichnung steht auf jeder Seite der Anlage oben rechts. Der Berliner Gerichtshinweis empfiehlt dies ausdrücklich für sämtliche Seiten. Der Stempel muss nach der PDF-Erzeugung sichtbar bleiben und darf keinen Urkundentext, keine Unterschrift, keinen vorhandenen Stempel, keinen Barcode und keine Seitenzahl überdecken.

## 2. Nummernkreis

1. Prozessrolle aus Schriftsatz und Vorakten bestimmen.
2. Letzte bereits eingereichte Nummer feststellen.
3. Neue Anlage fortlaufend anschließen.
4. Replik oder Duplik nicht als Anlass für einen Neustart behandeln.
5. Nachreichung mit dem bereits verwendeten Anlagenzitat abstimmen.

## 3. Einzelanlage oder Konvolut

Eine Sammelanlage ist nur sinnvoll, wenn die Dokumente eine erkennbare Einheit bilden. Das Deckblatt nennt:

1. Hauptbezeichnung,
2. Dokumente und Reihenfolge,
3. Datum oder Zeitraum,
4. Seitenbereich,
5. gemeinsames Beweisthema.

Unteranlagen wie `K 12.1` und `K 12.2` nur verwenden, wenn Schriftsatz, Stempel, Deckblatt und Verzeichnis diese Untergliederung überall identisch abbilden. Sonst eigenständige Anlagenziffern vergeben.

## 4. Sichtkontrolle

| Prüfung | Stop-Befund |
| --- | --- |
| Position | Stempel abgeschnitten, gedreht oder überdeckt Inhalt |
| Bezeichnung | Seite trägt andere Nummer als Dateiname |
| Vollständigkeit | nur erste Seite eines mehrseitigen Belegs bezeichnet |
| Konvolut | Unterlagenfolge weicht vom Deckblatt ab |
| Schriftsatz | Anlagenzitat passt nicht zum sichtbaren Stempel |

## 5. Werkzeug

`../anlagen-zu-schriftsaetzen/werkzeuge/build_anlagenkonvolut.py` stempelt standardmäßig jede Seite und erzeugt zusätzlich ein internes Prüfkonvolut. Das Prüfkonvolut ist nicht automatisch die an das Gericht zu sendende Datei; die getrennten Versanddateien bleiben maßgeblich.

## 6. Output

Liefere Stempelspezifikation, Nummernfortschreibung, Konvolutdeckblatt, Abweichungsliste und Sichtkontrollvermerk. Bei fertigem Paket in `bea-versandmappe-endfertigung` weiterarbeiten.
