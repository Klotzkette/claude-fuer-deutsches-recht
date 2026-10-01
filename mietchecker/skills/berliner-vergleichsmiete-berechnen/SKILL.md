---
name: berliner-vergleichsmiete-berechnen
description: Berechnet eine Berliner Wohnraummiete anhand des passenden Mietspiegelfelds, des amtlichen Straßenverzeichnisses und der örtlichen Orientierungshilfe. Dokumentiert Ausstattung und Spanneneinordnung statt Stadtmittelwert oder pauschalem Höchstwert.
---
# 1. Berliner Vergleichsmiete berechnen

## 1. Zweck und Anwendungsfall

Ermittle die Einzelvergleichsmiete in Berlin. Das Ergebnis ist zunächst ein Mietspiegelvergleich, noch keine zulässige Anfangsmiete oder wirksame Erhöhung.

## 2. Eingaben

Stichtag, Adresse, tatsächliche Wohnfläche, Bezugsfertigkeit und Wohnungsmerkmale mit Belegen. Aktueller Mietspiegel und Straßenverzeichnis. Bei Baujahren 1973 bis 1990 ist der historische Gebietsstand relevant.

## 3. Ablauf

1. Geltungsbereich prüfen; die Berliner Tabelle ist nicht für jede Wohnform geeignet. Hausnummernabschnitt und einfache, mittlere oder gute Wohnlage aus dem amtlichen Verzeichnis bestimmen.
2. Genau eine Tabellenzeile nach Lage, Bezugsfertigkeit und Fläche auswählen. Unterwert, Mittelwert und Oberwert mit Ausgabe und Zeilennummer festhalten. Ein saniertes Bad ändert nicht automatisch das Baualter.
3. Die fünf Merkmalsgruppen getrennt anhand der konkreten Orientierungshilfe bewerten. Unbekannt bleibt unbekannt; Merkmale innerhalb einer Gruppe gegeneinander abwägen und erst danach den Gruppensaldo bilden.
4. Gruppensalden gegeneinander aufrechnen. Positives Gesamtergebnis auf die Differenz Oberwert minus Mittelwert beziehen; negatives auf Mittelwert minus Unterwert. Nicht 20 Prozent des gesamten Mietpreises je Gruppe aufschlagen.
5. Doppelzählungen etwa bei energetischer Ausstattung nach den örtlichen Ausschlussregeln vermeiden. Nachgewiesene Mieterausstattung nicht dem Vermieter zurechnen.
6. Rechenblatt liefern, ungeklärte Merkmale als Variante zeigen und anschließend an Anfangsmieten- oder Erhöhungsprüfung anschließen. Das Rechenhilfsskript `scripts/mietrechnung.py` im Plugin ist optional; ohne Ausführung offen rechnen.

## 4. Quellenpflicht

Paragrafen 558c und 558d BGB, Berliner Mietspiegel 2026; BGH, Urteil vom 18.11.2020, VIII ZR 123/20. Die Orientierungshilfe ist eine Schätzgrundlage und nicht selbst der qualifizierte Tabellenteil.

[Zitierweise](../../references/zitierweise.md) und [örtliche Quellen](../../references/ortsrecht-und-rechtsprechung.md) beachten. Quellenstand offenlegen; keine ungelesenen Randnummern ergänzen.

## 5. Ausgabeformat

Liefere das beauftragte Endprodukt in vollständigen, ausformulierten Sätzen, nicht als Skelett oder bloße Aufzählung. Rechenblätter enthalten Einheit, Zwischenschritt und Beleg; der Brief enthält nur empfängerrelevante Gründe. Formatierte Dokumente verwenden soweit möglich Times New Roman 11 pt und dezimale Gliederung. Bei reiner Textausgabe den Exporthinweis getrennt halten. Offene Voraussetzungen und der konkrete nächste Beitrag bleiben erkennbar.

## 6. Beispiel

Bei einer Wohnung mit 62 Quadratmetern aus 1932 in mittlerer Lage zunächst Zeile 81 der Ausgabe 2026 prüfen. Die Rechnung darf eine Ausnahme der Mietpreisbremse weder unterstellen noch ausschließen.
