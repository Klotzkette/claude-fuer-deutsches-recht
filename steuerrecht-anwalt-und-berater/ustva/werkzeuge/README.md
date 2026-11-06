# UStVA Erfassungsdateien aus einem geprüften Arbeitsstand

Der Helfer erzeugt eine Tabelle für die manuelle Erfassung in Mein ELSTER und eine maschinenlesbare Kopie des geprüften Arbeitsstands. Er prüft Kennzahlzuordnung, Einheiten, Vorzeichen, Rechenkontrollen und einen Belegabgleich. Die fachliche Auswahl der Kennzahlen und die steuerliche Einordnung bleiben Aufgabe des bearbeitenden Skills.

## 1 Aufruf

```sh
python3 ustva_ausgabe.py arbeitsstand.json --out ausgabe-neu
```

Das Ausgabeziel muss neu sein. Der Standardweg benötigt nur Python 3.10 oder neuer. Der Status lautet nach dem Export `prepared_not_transmitted`. Die erzeugte CSV ist eine Erfassungshilfe und wird zeilenweise mit dem Jahresformular abgeglichen.

## 2 Eingabevertrag

Die JSON enthält genau `schema_version`, `year`, `period`, `taxpayer`, `approval_status`, `mapping`, `fields`, `arithmetic` und `reconciliation`. Unterstützt sind die Arbeitsjahre 2025 und 2026, die Zeiträume `Q1` bis `Q4` sowie `M01` bis `M12`. `taxpayer` enthält `name` und die betriebliche `steuernummer`, optional `ust_id`, `w_id`, `finanzamt` und `address`. `approval_status` ist `reviewed` oder `approved`. Dieser Prüfstatus ist keine Versandhandlung.

`mapping` enthält `year`, `source`, `reviewed_on` im ISO-Datumsformat und ein Objekt `fields`. Dessen Schlüssel sind die geprüften Kennzahlen. Jede Definition enthält genau `label`, `unit`, eine eindeutige `semantic` und die boolesche Vorzeichenregel `allow_negative`. Die fachliche Quelle und ihre Jahresfassung müssen vor dem Aufruf geprüft werden.

`fields` ist eine Liste mit `kennzahl`, `label`, `amount`, `unit` und `source`. Betrag und Kennzahl sind Zeichenfolgen. Beträge verwenden einen Punkt als Dezimaltrennzeichen und keine Tausenderzeichen. `EUR` bedeutet ganze Euro, `EUR_CENT` bedeutet Euro mit höchstens zwei Nachkommastellen, `FLAG` bedeutet 0 oder 1. Die Einheiten und Bezeichnungen müssen mit der geprüften Zuordnung übereinstimmen. Zahlen werden nicht stillschweigend auf die Feldeinheit abgerundet.

Ein erforderliches Berichtigungsmerkmal wird als geprüfte Kennzahl mit der Einheit `FLAG` übergeben. Die Erfassungstabelle wiederholt Unternehmer, Steuernummer, Jahr und Zeitraum bei jeder Kennzahl.

`arithmetic` enthält mindestens eine Rechenkontrolle und insbesondere eine Kontrolle des Ergebnisses in Kennzahl 83. Jede Kontrolle hat `id`, `result_field`, `terms` und `rounding`. Jeder Term enthält `field` und einen Dezimalfaktor als Zeichenfolge. Die Rundungsregel ist `HALF_UP` oder `DOWN`. Beispiel für einen fachlich passenden einfachen Fall ist Kz 81 mal 0.19 zuzüglich Kz 86 mal 0.07 abzüglich Kz 66 gleich Kz 83. Die tatsächlich benötigten Kontrollterme ergeben sich aus den Umsätzen und der Jahresfassung. Der Helfer ergänzt keine Steuerfälle.

`reconciliation` enthält mindestens einen unabhängig ermittelten Abgleich mit `id`, `actual`, `expected` und `source`. Beide Beträge sind Dezimalzeichenfolgen. Die Fundstelle soll auf die Rechnungsmatrix oder einen anderen nachvollziehbaren Kontrollnachweis verweisen.

## 3 Vorhandene Import-XML prüfen

Mein ELSTER unterstützt für die UStVA einen XML-Upload der Nutzdaten. Der amtliche Aufbau und die jährlichen Plausibilitätsregeln stehen in der ERiC-Dokumentation. Der Upload verwendet den Nutzdatenwurzelknoten `Anmeldungssteuern` und ISO-8859-15. Das authentifizierte Übermitteln über ERiC ist ein eigener Vorgang. [Amtliche Uploadhilfe](https://www.elster.de/eportal/helpGlobal?themaGlobal=ustva_upload) · [Entwicklerzugang](https://www.elster.de/elsterweb/infoseite/entwickler)

```sh
python3 ustva_ausgabe.py arbeitsstand.json --out ausgabe-neu \
  --import-xml vorhandene-jahresdatei.xml --xsd lokales-jahresschema.xsd
```

Dieser optionale Weg benötigt `lxml`. Das Jahres-XSD und seine lokalen Abhängigkeiten müssen vollständig im selben Verzeichnis oder in dessen Unterverzeichnissen vorliegen. Für ein freigegebenes Schema-Paket mit gemeinsamem Oberverzeichnis kann dieses mit `--schema-root VERZEICHNIS` angegeben werden. Netzwerkzugriffe, externe Entitäten und Pfade außerhalb dieses Verzeichnisses sind gesperrt.

Zusätzlich benötigt `mapping.xml` genau `namespace`, `version`, `year_path`, `period_path`, `period`, `period_value`, `fields`, `taxpayer` und `metadata`. `period` bezeichnet den Arbeitszeitraum, `period_value` seinen anhand der Jahresdokumentation geprüften XML-Wert. Die Pfade folgen dem geprüften Jahresschema und sind einfache Elementpfade, etwa `./u:Steuerfall/u:Umsatzsteuervoranmeldung/u:Jahr`. `u` bezeichnet den angegebenen Namensraum. `fields` ordnet jeder tatsächlich ausgegebenen Kennzahl genau einen solchen Pfad zu.

`taxpayer` ordnet mindestens `steuernummer` dem entsprechenden XML-Element zu. Für diesen Prüfweg muss auch `taxpayer.steuernummer` in den Stammdaten die anhand der amtlichen Zuordnung geprüfte 13-stellige ELSTER-Steuernummer enthalten. Der Vergleich entfernt Leerzeichen und Trennzeichen. Eine Landes-Steuernummer wird nicht heuristisch umgerechnet. Weitere zu prüfende Unternehmerangaben können ebenfalls ihren Elementpfaden zugeordnet werden.

`metadata` ist eine Zuordnung zusätzlicher Elementpfade zu deren ausdrücklich geprüften Textwerten, beispielsweise für das Erstellungsdatum oder die Angaben des Datenlieferanten. Bei fehlenden weiteren Metadaten ist sie leer. Alle befüllten XML-Blattwerte müssen durch die Zuordnungen erfasst sein. Weitere Steuerkennzahlen dürfen auch nicht als Metadaten versteckt werden. Der Helfer prüft Wurzel, XML-Version, Unternehmer, Jahr, Zeitraum und sämtliche Kennzahlen gegen den Arbeitsstand. Erst danach kopiert er die geprüfte XML in das Ausgabepaket.

Der XML-Prüfbericht belegt XSD-Prüfung und Werteabgleich anhand der angegebenen Quellen. Er führt Jahresplausibilitätsprüfung, Portalannahme und Übermittlung als weiterhin ungeprüft beziehungsweise nicht erfolgt. Ein Zertifikat oder Passwort wird vom Helfer nicht verarbeitet. Für die tatsächliche Übermittlung werden die freigegebene lokale Steueranwendung oder das angemeldete Mein-ELSTER-Konto verwendet.
