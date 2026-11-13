# 1 Eingabe und Start

Der Stichtagsrechner verwendet geordnete Belegpositionen mit Fundstellen. Im Plugin-Ordner startet `node app/server.mjs` den lokalen Dienst. Öffnen Sie [das Applet](http://127.0.0.1:8765/) im Browser. Fügen Sie eine Fall-JSON ein oder wählen Sie die Datei aus. Die Falldaten bleiben bei diesem Weg im Browser. Derselbe Rechner verarbeitet Dateien oder Standardeingabe auf der Kommandozeile.

```sh
node app/cli.mjs app/beispiel.json
node app/cli.mjs - < fall.json
node --test app/engine.test.mjs
```

Die [Beispieldatei](beispiel.json) zeigt zwei Stichtage. Für die Arbeit im Chat kann das Modell dieselbe Struktur aus den Belegen aufbauen. Bei verfügbarer lokaler Node-Laufzeit übergeben Sie die Struktur an den Rechner. In einer Oberfläche ohne Programmausführung werden die Positionen mit denselben Rechenschritten tabellarisch addiert und geprüft.

## 1.1 Kopf und Stichtage

`caseName` enthält die Fallbezeichnung. Die Liste `dates` enthält Objekte mit je einem Kalendertag in `date`, zum Beispiel `2026-06-18`. Je Datum können `liquidity` und `overindebtedness` unabhängig erfasst werden. Jeder Abschnitt besitzt `complete`, `assets` und `liabilities`. `complete` ist eine bestätigte Aussage zum belegten Erfassungsumfang des Abschnitts. Setzen Sie sie bei Datenlücken auf `false` und nennen Sie die Lücken als Textliste in `notes`.

Jede Position besitzt eine je Liste eindeutige `id`, eine `description`, einen Betrag `amountCents` in ganzen, nicht negativen Cent und eine `decision` mit `include`, `exclude` oder `open`. Beispiel: 123,45 Euro werden zu `12345`. Geben Sie die genaue Fundstelle in `source` und den Grund für die Einordnung in `reason` an. Bei einer offenen Position dürfen Fundstelle, Betrag und gegebenenfalls Datum fehlen. Offene Positionen mit ungeklärter Zeitlage bleiben ergebnisrelevant.

## 1.2 Liquidität nach § 17 InsO

- Auf der Aktivseite bezeichnet `availableOn` den belegten Tag, ab dem der Betrag für die Zahlung zur Verfügung steht. Verwenden Sie `kind: "cash"` für verfügbare Bestände oder Kreditmittel und `kind: "inflow"` für Zuflüsse nach dem Stichtag. Haben Sie Zuflüsse bereits im Stichtagsbestand erfasst, rechnen Sie diese nur im Bestand.
- Auf der Passivseite bezeichnet `dueOn` den Tag der tatsächlich zu berücksichtigenden Fälligkeit. Stundung, Teilzahlung, Durchsetzungssperre und strittiger Ansatz sind anhand der Belege zu prüfen und zu dokumentieren. Offene Teilbeträge mit verschiedenen Fälligkeiten erhalten getrennte Positionen.
- Der Rechner summiert A1 und P1 bis einschließlich Stichtag sowie A2 und P2 vom Folgetag bis einschließlich Tag 21. Der Tagesverlauf zeigt, wann Mittel und Pflichten hinzukommen. Die Restlücke ist `max(0, P1 + P2 − A1 − A2)`. Der Nenner ist `P1 + P2`. Die Einordnung nutzt ganze Cent und die exakte Zehnprozentgrenze. Gerundete Prozentwerte dienen der Darstellung.
- Für eine positive Restlücke unter zehn Prozent kann `gapTrend` mit `result: "worsening_to_threshold"`, `"not_expected"` oder `"open"` ergänzt werden. Ab zehn Prozent dokumentiert `nearClosure` mit `"established"`, `"not_established"` oder `"open"` die Würdigung des Ausnahmefalls. Ein entschiedener Eintrag verlangt `source` und `reason`. Für `established` muss die Begründung die sehr wahrscheinliche baldige vollständige oder fast vollständige Schließung und das zumutbare Zuwarten der betroffenen Gläubiger abdecken.
- Verifizieren Sie bei der Sachverhaltsaufbereitung den Belegstand am Stichtag. Spätere Zahlungseingänge und Ausfälle können die Rekonstruktion stützen oder widerlegen. Ein Vorschuss, ein später genehmigter Kredit oder eine nicht frei verfügbare Position verlangt eine eigene Prüfung. Würdigen Sie die gesetzliche Vermutung bei Zahlungseinstellung separat.

Der Bundesgerichtshof bezieht bei der Liquiditätsbilanz auch die im Dreiwochenzeitraum fällig werdenden und eingeforderten Pflichten ein. Eine belegte tagesgenaue Liquiditätsentwicklung kann als eigener Darlegungsweg dienen. Für die Anfechtung kommt es darauf an, einzelne Positionen und ihre Fälligkeit mit konkreten Unterlagen darzulegen. [§ 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html) · [BGH, Urteil vom 19. Dezember 2017 – II ZR 88/16, Rn. 33–35, 41](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2016/II_ZR__88-16.pdf?__blob=publicationFile&v=1) · [BGH, Urteil vom 28. Juni 2022 – II ZR 112/21, Rn. 12–15](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/II_ZS/2021/II_ZR_112-21.pdf?__blob=publicationFile&v=1) · [BGH, Urteil vom 18. April 2024 – IX ZR 129/22, Rn. 20–25](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_129-22.pdf?__blob=publicationFile&v=1)

## 1.3 Überschuldung nach § 19 InsO

Der Rechner bildet den Zwölfmonatshorizont der aktuellen Fassung des § 19 Abs. 2 InsO ab. Prüfen Sie für historische Fälle den am Stichtag geltenden Rechtsstand. Geben Sie den belegten Prognosebefund unter `forecast.result` als `"positive"`, `"negative"` oder `"open"` ein. `forecast.through` bezeichnet das belegte Prognoseende oder bei negativem Befund den konkret belegten früheren Finanzierungsabbruch. Bei einer weiter reichenden negativen Planung können Sie mit `forecast.failureOn` den früheren belegten Abbruch angeben. Der Rechner verlangt den Abbruch innerhalb des Zwölfmonatshorizonts. Ein entschiedener Eintrag verlangt `source` und `reason`. Für eine positive Prognose fordert der Rechner die vollen zwölf Monate nach dem Stichtag. Eine belastbare positive Fortbestehensprognose trägt die Prüfung selbst dann, wenn der Vermögensstatus noch nicht vollständig vorliegt. Bei offener Prognose und belegter Unterdeckung gibt der Rechner einen offenen Befund aus.

Auf der Aktivseite stehen die belegten, zum Szenario passenden Verwertungswerte. Dokumentieren Sie Verwertungsdauer, Kosten und stille Reserven. Auf der Passivseite stehen bestehende Verbindlichkeiten einschließlich der zum Stichtag noch nicht fälligen. Ordnen Sie jede Finanzierungsabrede einzeln ein. Bewerten Sie Rechtswirkung, Datum, Bedingungen und Durchsetzbarkeit einer Nachrang- oder Patronatserklärung für § 17 und § 19 jeweils eigenständig. [§ 19 InsO](https://www.gesetze-im-internet.de/inso/__19.html) · [§ 39 InsO](https://www.gesetze-im-internet.de/inso/__39.html) · [BGH, Urteil vom 5. März 2015 – IX ZR 133/14, amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2014/IX_ZR_133-14.pdf?__blob=publicationFile&v=1)

## 1.4 Ergebnis weiterverwenden

`results` enthält je Stichtag die Summen, die Befunde und die Belegpositionen. `firstCandidate` gibt für beide Tatbestände den jeweils frühesten stützenden geprüften Tag und, sofern vorhanden, den davor geprüften Tag sowie den letzten gegenläufigen Befund an. Bei einer Akte mit mehreren möglichen Tagen arbeiten Sie die erste relevante Veränderung anhand der Belege heraus. Fügen Sie für strittige Einordnungen getrennte Rechenvarianten mit abweichenden Positionen hinzu und begründen Sie die Wahl der tragfähigen Variante. Für eine spätere Anfechtungsprüfung ist der Befund mit dem Zeitpunkt der einzelnen Rechtshandlung zu verknüpfen.
