# 1. Stimmenrechnung mit offengelegten Annahmen

## 1.1. Die Regel steht vor der Rechnung

Der lokale [Stimmenprüfer](../tools/stimmenpruefer.py) benötigt Python 3 und verwendet nur dessen Standardbibliothek. Er entscheidet keine Rechtsfrage. Stimmengewicht, anwendbare Mehrheit, Nenner und etwaige Ausschlüsse ergeben sich aus der geprüften Satzung und dem einschlägigen Recht. Ein Geschäftsanteil, ein Euro Nennbetrag und eine Person dürfen nicht ungeprüft gleichgesetzt werden. Gesetzlicher Ausgangspunkt ist § 47 Abs. 2 GmbHG; Sonderregeln sind gesondert zu erfassen.

`abgegebene-gueltige-stimmen` zählt im Nenner nur Ja und Nein der nicht ausgeschlossenen Personen. `stimmberechtigtes-gesamtkapital` zählt auch deren Enthaltungen, ungültige Stimmen und abwesende Personen. `vertretenes-stimmberechtigtes-kapital` lässt davon nur Abwesende aus. `gesamtkapital` enthält sämtliche eingegebenen Gewichte einschließlich der ausgeschlossenen Personen. Diese vier Varianten sind Rechenmodelle, keine automatisch geltenden Rechtsregeln. Wähle insbesondere bei einer Satzungsschwelle bezogen auf das gesamte Stammkapital nicht stillschweigend den reduzierten Nenner.

Eine einfache Mehrheit kann nach der ermittelten Regel als `>` und `1/2`, eine Mindestmehrheit von drei Vierteln als `>=` und `3/4` eingegeben werden. Eine Mehrheit wird nicht durch Rundung eines Prozentwerts erreicht. Null im Nenner ergibt kein angenommenes oder abgelehntes Ergebnis, sondern einen offenen Rechenbefund. Beschlussfähigkeit, Zustimmungserfordernisse einzelner Gesellschafter und zusätzliche Mehrheiten werden außerhalb dieses Rechners geprüft.

## 1.2. Beispiel für zwei ausdrücklich vorgegebene Varianten

Die folgenden Angaben sind ein Rechenbeispiel und keine rechtliche Einordnung eines konkreten Stimmverbots. Person A stimmt gegen einen Antrag; B und C dafür. Die streitige Alternative nimmt A aus der Zählung. Der Benutzer hat zuvor begründet festzulegen, welche Variante rechtlich trägt.

```json
{
  "basis": "abgegebene-gueltige-stimmen",
  "schwelle": "1/2",
  "vergleich": ">",
  "gesellschafter": [
    {"id": "A", "stimmen": 60, "votum": "nein"},
    {"id": "B", "stimmen": 25, "votum": "ja"},
    {"id": "C", "stimmen": 15, "votum": "ja"}
  ],
  "ausschluesse": [],
  "alternative_ausschluesse": ["A"]
}
```

Speichere die gewählte Eingabe als JSON und führe `python3 tools/stimmenpruefer.py eingabe.json` im Pluginverzeichnis aus. Das Beispiel ergibt exakt 40/100 und 40/40. Halte beide Rechenwege, ihren jeweiligen Ausschluss und die rechtliche Meinungsverschiedenheit fest. Die alternative Zählung ersetzt weder eine tatsächlich abgegebene Stimme noch das tatsächlich verkündete Ergebnis.

## 1.3. Vor jedem Protokolleintrag

Gleiche Gesellschafterkennungen, Stimmengewichte, Anwesenheit, Vollmachten und Voten mit den tatsächlichen Unterlagen ab. Eine fehlende Stimmabgabe wird nicht als Nein erfunden. Gib stattdessen die konkret fehlende Angabe an; berechne erst danach oder liefere ausdrücklich nur ein Szenario. Bei Kopfstimmrecht sind die vereinbarten Kopfgewichte einzutragen, nicht die Kapitalbeträge. Das JSON dokumentiert seine Annahmen und wird nicht ungefragt an die Empfänger des Protokolls angehängt.

Ändert sich eine Klausel oder die Einordnung eines Stimmverbots, passe die Eingabe gezielt an und wiederhole nur die betroffenen TOP-Rechnungen. Bewahre die frühere Variante mit ihrem Stand auf. Ohne ausführbares Werkzeug dieselben Zähler und Nenner nachvollziehbar von Hand rechnen und nicht behaupten, das Skript sei gelaufen.
