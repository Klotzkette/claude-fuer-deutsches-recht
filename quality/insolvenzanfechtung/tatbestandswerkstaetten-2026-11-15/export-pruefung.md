# Unabhängige Prüfung der erzeugten Werkstattexporte

## 1. Ergebnis

Die tatsächlich erzeugten Exporte wurden am 15.11.2026 mit `scripts/test-anfechtung-werkstattprompts.py` geprüft: **14 Tests bestanden**. Das Paket enthält zehn vollständige Module mit insgesamt 63.479 Wörtern und 179 gesetzten PDF-Seiten. Die Einzelmodule umfassen 17 bis 19 Seiten. Exakte Dateigrößen, SHA-256-Werte, Zeitpunkt, Aufruf und Prüfgrenzen stehen in [export-pruefung.json](export-pruefung.json); der erfolgreiche vollständige Lauf ist in [export-tests.log](export-tests.log) dokumentiert.

ZIP-SHA-256: `5c36c5b81e80040a62a1f2844bbe3d2c8acba4f009e1947e1f153357d6d199b7`.

## 2. Technischer Prüfgegenstand

Die Positivprobe verwendet die echten Dateien aus `docs/werkstattprompts/insolvenzanfechtung/`. Die Negativproben verändern ausschließlich temporäre Kopien dieser Dateien. Geprüft werden unter anderem fehlende, doppelte und zusätzliche ZIP-Mitglieder, falsche Wort- und Seitenangaben, gekürzte PDFs, geänderte Quelltexte, PDF-Inhalte, Linkziele und Quellenstandszeilen. Bei den Inhaltsmanipulationen werden die betreffenden Prüfsummen gezielt neu berechnet, damit die Prüfung nicht bloß einen veralteten Hash erkennt.

Der Prüfvertrag vergleicht den vollständigen sichtbaren Text in Quellreihenfolge. Er entfernt dabei ausschließlich Whitespace und die tatsächlich verwendete Markdown-Darstellungssyntax. Dezimal- und Tausenderzeichen, Minuszeichen, Prozent und Promille sowie Vergleichszeichen bleiben erhalten. Zusätzlich werden die Linkziele der PDF-Annotationen mit den Markdown-Zielen und die Kopf-/Fußzeilen in Einzel- und Sammelfassung überprüft.

## 3. Nachgewiesene Erkennung des früheren Fehlers

Eine gezielte Mutation verändert einen echten Betrag im PDF von „18.000 Euro“ zu „180,00 Euro“ und aktualisiert dessen Prüfsumme. Der aktuelle Vertrag weist die Datei wegen der abweichenden sichtbaren Aussage zurück. Die frühere Normalisierung hätte beide Werte auf dieselbe Ziffernfolge reduziert.

Zur Negativkontrolle wurde ausschließlich im Speicher eines eigenen Prüfprozesses nochmals die frühere Normalisierung eingesetzt. Derselbe Regressionstest scheiterte erwartungsgemäß, weil dann kein Fehler mehr ausgelöst wurde. Dieses beabsichtigte Gegenexperiment steht in [export-alte-normalisierung-negativkontrolle.log](export-alte-normalisierung-negativkontrolle.log). Dessen dokumentierter Testfehlschlag ist der Nachweis, dass die Regression die frühere Schwäche erkennt; die Produktionsdateien wurden dabei nicht zurückgesetzt oder abgeschwächt.

## 4. Grenzen

Die Tests ersetzen keine visuelle Vollkontrolle aller Seiten, keine materielle Gesamtprüfung der Rechtsaussagen und keinen Live-Modellbenchmark. Die amtlichen Quellenprüfungen stehen in den gesonderten Fachberichten. Veröffentlichung und heruntergeladene Releaseassets werden durch diesen lokalen Exporttest nicht als geprüft behauptet. Kompilierung der beiden Prüfscripts und `git diff --check` bestanden zusätzlich.
