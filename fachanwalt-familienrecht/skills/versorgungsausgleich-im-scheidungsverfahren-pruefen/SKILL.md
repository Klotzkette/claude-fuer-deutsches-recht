---
name: versorgungsausgleich-im-scheidungsverfahren-pruefen
description: "Prüft den Versorgungsausgleich im laufenden Scheidungsverfahren von Ehezeit und Anrechten bis zur Stellungnahme. Trennt Auskunft, Teilung und Ausnahmen und verweist bei Beschwerde oder späterer Anpassung in eigenständige Verfahren."
---

# Versorgungsausgleich im Scheidungsverfahren prüfen

## 1. Zweck und Anwendungsfall

Für die erstmalige Entscheidung über Versorgungsanrechte bei Scheidung. Ein konkreter Auskunftsfehler geht direkt zu `versorgungsauskuenfte-und-anrechtswerte-pruefen`, ein Streit um interne oder externe Teilung zu `versorgungsteilung-und-zielversorgung-pruefen`. Die beiden Detailaufgaben nicht nochmals als allgemeine Erstprüfung ausführen.

## 2. Eingaben

Heiratsurkunde, Zustellung des Scheidungsantrags, Gericht und Aktenzeichen, Trägerauskünfte, Versicherungs- und Versorgungsverläufe, Teilungsordnungen, Vereinbarungen, Rentenbeginn sowie Auslandsbezug. Den Trennungszeitpunkt nicht als Ehezeitende verwenden.

## 3. Ablauf

### 3.1. Ehezeit und Anrechtsbestand

Lade [Ehezeit, Halbteilung und Fallweichen](references/ehezeit-anrechte-und-fallweichen.md). Dort stehen Monatsgrenzen, Antrag bei kurzer Ehe, Versorgungsarten, Abgrenzung zum Zugewinn und die anrechtsbezogene Ergebnisstruktur. Die Ehezeit endet am letzten Tag des Monats vor Zustellung. Bei bis zu drei Jahren ist der Antrag eines Ehegatten zu prüfen, nicht automatisch grobe Unbilligkeit anzunehmen.

Erfasse jedes Anrecht mit Inhaber, Träger, Kennung, Ehezeitanteil, Ausgleichswert, Einheit, Kapitalwert und Auskunftsstatus. Fehlende Auskünfte nachfordern; nicht Gesamtvermögen oder Rentenprognosen halbieren.

### 3.2. Sachentscheidung

Prüfe die Teilungsform je Anrecht. Geringfügigkeit, fehlende Ausgleichsreife, Vereinbarung und grobe Unbilligkeit sind unterschiedliche Weichen. Lade nur den einschlägigen eigenständigen Skill: `geringfuegigkeit-18-versausglg`, `nicht-ausgleichsreife-anrechte-19-versausglg`, `vereinbarung-ueber-versorgungsausgleich-6-ff-versausglg` oder `ausschluss-grobe-unbilligkeit-27-versausglg`.

Bei Verzögerung des Scheidungsverfahrens `scheidungsverbund-va-fristenplan` und gegebenenfalls `verbundabtrennung-versorgungsausgleich` nutzen. Eine Abtrennung ersetzt keine Prüfung der einzelnen Anrechte.

### 3.3. Eigenständige Verfahren erhalten

| Lage | Eigenständiger Arbeitsweg |
| --- | --- |
| Angriff auf noch anfechtbaren Beschluss | `beschwerde-gegen-va-beschluss-famfg` |
| Änderung einer Altentscheidung | `abaenderung-versorgungsausgleich-51-versausglg` |
| Totalrevision mit Todesfall | `versorgungsausgleich-totalrevision-und-tod` |
| Tod vor Abschluss des Verfahrens | `versorgungsausgleich-verstorbener-paragraf-31-versausglg` |
| Ausgleich erst nach der Scheidung | `ausgleich-nach-der-scheidung-20-ff-versausglg` |
| Kürzung trotz Unterhaltspflicht | `anpassung-wegen-unterhalt-33-ff-versausglg` |
| Invalidität oder besondere Altersgrenze | `anpassung-wegen-invaliditaet-oder-besonderer-haerte` |
| Tod der ausgleichsberechtigten Person nach Rechtskraft | `tod-eines-ehegatten-anpassung-37-ff-versausglg` |
| Auskunft oder Vollstreckung nach der Entscheidung | `nachtraegliche-auskunft-und-vollstreckung` |

Entscheidungsdatum, Rechtskraft und anwendbares altes oder neues Recht bestimmen die Route. Eine nachträgliche Änderung ist keine beliebige Reparatur eines ursprünglichen Fehlers.

## 4. Quellenpflicht

Nutze [references/zitierweise.md](../../../references/zitierweise.md) und die [geprüften Rechtsanker](../../references/rechtsanker-2026-09-05.md). Verifiziere Teilungsordnung und Versorgungsträgerauskunft zusätzlich am konkreten Fall. Für noch nicht vollständig verifizierte Rechtsprechung keine Randnummern ergänzen.

## 5. Ausgabeformat

Ehezeitblatt und Anrechtsmatrix als Anlagen; ausformulierte Stellungnahme mit getrenntem Ergebnis je Anrecht, offenen Auskünften und nächster Frist. Ausformulierungspflicht und Formatstandard: vollständige Sätze statt Skelett, Times New Roman 11 pt, dezimale Gliederung mit Leerzeilen; bei Markdown Exporthinweis. Beschlussvorschläge brauchen eindeutige Träger, Kennungen, Beträge und Einheiten.

## 6. Beispiele

Bei einer kurzen Ehe zunächst Monatsgrenzen und Antrag prüfen. Liegen nach Rechtskraft neue Rentenauskünfte vor, zuerst Rechtsbehelfsweg und Änderungsgrund bestimmen; nicht die ursprüngliche Scheidungsprüfung wiederholen.
