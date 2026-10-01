# 1. Forderungsdaten elektronisch übergeben

## 1.1. Anmeldung, Prüftabelle und Gerichtseinreichung unterscheiden

Der Eingang beim Verwalter, dessen Prüfungsentscheidung und die gerichtliche Tabellenführung sind verschiedene Vorgänge. Nach Paragraf 174 Absatz 4 InsO ist eine elektronische Anmeldung möglich. Ein vorgegebener üblicher Übermittlungsweg ersetzt nicht den zusätzlich anzubietenden sicheren Weg nach Paragraf 130a ZPO. Die gerichtliche Niederlegung der Tabelle samt Unterlagen nach Paragraf 175 InsO ist gesondert zu organisieren. Ein vollständig importierter Datensatz beweist weder den Zugang einer Anmeldung noch die Feststellung der Forderung. [Amtlicher Text zu Paragraf 174](https://www.gesetze-im-internet.de/inso/__174.html), [Paragraf 175](https://www.gesetze-im-internet.de/inso/__175.html).

Vor der Einreichung Gerichtsprofil, Zuständigkeit, Empfängerpostfach, zulässige Anlagenformate und Signatur- beziehungsweise Übermittlungsweg bestätigen. Die persönliche Rolle des Einreichers ist erheblich; die elektronische Nutzungspflicht und die Voraussetzungen einer Ersatzeinreichung sind insbesondere nach [Paragraf 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html) zu prüfen. Ein technischer Export ersetzt diese Prüfung nicht.

## 1.2. Schneller, lokaler Prüfdatenexport

Das mitgelieferte Hilfsprogramm verarbeitet bereits erfasste und belegte Werte. Es liest keine Akte selbständig aus, entscheidet keine Rechtsfrage und verschickt nichts. Aus dem Plugin-Verzeichnis:

```sh
python3 scripts/forderungsexport.py Forderungen.json Ausgabe_2026_09_10
```

Das Programm erzeugt `Prueftabelle.csv`, `Pruefdaten.json`, ausdrücklich internes `Pruefdaten_INTERN.xml`, ein Prüfprotokoll mit Dateiprüfsummen und einen Lesehinweis. Für diesen Weg genügt Python 3.10 oder neuer. Kann der Client keine Programme ausführen, die Prüftabelle und die vollständigen Gläubigerbriefe direkt ausgeben; einen nicht ausgeführten Dateiexport niemals behaupten.

`Pruefdaten_INTERN.xml` ist kein XJustiz-Dokument und darf nicht als gerichtliche Tabellenübergabe ausgegeben werden.

Der Zielordner muss neu sein. Beträge werden ohne Gleitkommarundung addiert; gemeldeter Betrag, nicht bestrittener Vorschlag und bestrittener Vorschlag müssen rechnerisch zusammenpassen. Auch bei vollständigem Bestreiten bleibt die ursprüngliche Anmeldung sichtbar. Ein verspäteter Eingang wird lediglich markiert. Weder Rang noch Sicherheitenwert führen zu automatischem Ausschluss oder Abzug. Die CSV verwendet Semikolon, UTF-8 mit BOM und deutsches Dezimalkomma für Excel; JSON und XML verwenden den Dezimalpunkt. Formelausführende CSV-Textzellen werden entschärft; die Originaltexte bleiben im JSON erhalten.

## 1.3. Verbindliche Eingabefelder

Ein vollständiges, bewusst noch ungeprüftes [technisches Eingabebeispiel](export-eingabe-beispiel.json) zeigt die Struktur. Die Bezeichnungen und das Aktenzeichen darin dienen nur der Programmerprobung und dürfen nicht in ein echtes Verfahren übernommen werden.

Die JSON-Eingabe enthält `schema_version: 1`, `verfahren` und die Liste `forderungen`. Unbekannte oder doppelte Felder führen zum Abbruch, damit keine Informationen unbemerkt verloren gehen.

| Bereich | Inhalt |
| --- | --- |
| `verfahren` | `aktenzeichen`, `schuldner`, `gericht`, `eroeffnung`, `anmeldefrist`, `stichtag` |
| Identität | Stabile `id`, positive eindeutige `tabellenblatt`, `glaeubiger`, `eingang`, `rang_angemeldet` |
| Beträge | `hauptforderung`, `zinsen`, `kosten`, `unerlaubte_handlung`; jeweils Zeichenkette wie `14280.00`, ohne Tausenderzeichen |
| Nachweise | `grund`, nicht leere Liste `belege`, `sicherheit`; bei Zinsen zusätzlich `zinsgrund`, bei Kosten `kostengrund` |
| Kennzeichen | `tituliert`, `titel_bei_den_akten`, `fuer_den_ausfall`; jeweils ausdrücklich `true` oder `false` |
| `pruefung` | `status` und ausformulierter `begruendung`; Status `offen` ohne Teilbeträge oder `vorschlag` mit `nicht_bestritten` und `bestritten` |

Datumswerte haben das Format `2026-09-10`. Der Deliktsbetrag ist Teil des angemeldeten Gesamtbetrags, kein zusätzlicher Summand. `0.00` ist ausdrücklich anzugeben, wenn keine solche Kennzeichnung angemeldet ist. Der Helfer bildet ausschließlich Hauptforderung, Zinsen und Kosten ab; besondere weitere Nebenforderungsarten, Fremdwährungen, bedingte Teilbeträge und unklare Betragszuordnungen werden im Fachverfahren bearbeitet. Keine Werte in ein unpassendes Feld pressen.

`grund`, `zinsgrund` und `kostengrund` müssen jeweils die Forderung beziehungsweise Berechnung eindeutig bezeichnen und dürfen für den XJustiz-Export höchstens 255 Zeichen enthalten. Ausführliche Begründungen gehören in den Vermerk und die beigefügten Dokumente. Bei einer offenen Prüfung bleiben die vorgeschlagenen Teilbeträge leer, nicht null.

## 1.4. XJustiz nur mit passenden Stammdaten und Schema

Stand der technischen Verifikation: 1. Oktober 2026. XJustiz 3.6.2 ist derzeit gültig; die veröffentlichte Version 4.0.0 gilt erst ab 30. April 2027. Nicht automatisch die höchste Versionsnummer auswählen. Das INSO-Modul trägt innerhalb des Pakets 3.6.2 weiterhin den Dateinamen `xjustiz_0300_insolvenz_3_5.xsd`. Maßgeblich sind das vollständige Paket und der Nachrichtenkopf, nicht die Moduldateinummer. [Amtliche Versionsübersicht und Downloads](https://xjustiz.justiz.de/XJustiz-Versionen/index.php).

Der optionale Export unterstützt nur die erstmalige Tabellenübergabe `0300005`, Ereignis `044` ohne Erklärungen. Er erzeugt keine Erklärungen über festgestellte Beträge aus internen Vorschlägen. Übergaben mit Erklärungen, Änderungsnachrichten `0300006` und gerichtliche Rückmeldungen gehören in die dafür eingerichtete Fachsoftware.

Benötigt werden:

1. Ein von der Verwaltung kontrolliertes XJustiz-Stammdatengerüst desselben Verfahrens: Nachrichtenkopf, Gerichtsaktenzeichen, Empfängergerichtscode, Grunddaten mit Beteiligten und Rollen, Fachdatenteil mit `beteiligte.inso`. Es darf noch keine Forderungen enthalten. Bereits übermittelte Daten nicht für einen erneuten Erstversand verwenden.
2. Das vollständig entpackte amtliche XSD-Paket, nicht nur eine einzelne Datei. Es wird nicht nachgeladen und nicht mit dem Plugin gebündelt. Für die lokale Schema-Prüfung muss `lxml` vorhanden sein.
3. Auf oberster JSON-Ebene `xjustiz` mit `empfaenger_code` und `waehrungsliste_version` aus dem aktuellen Fachverfahrensprofil. Bei jeder Forderung zusätzlich `xjustiz` mit `rollennummer`, `beteiligtennummer`, `beteiligtenkennung` und geprüftem `rang_code` der aktuellen Codeliste. Keine frei erfundenen Rollen, Kennungen oder Codelistenversionen verwenden. Namen und Anschriften müssen zusätzlich persönlich gegen die Beteiligtenzuordnung geprüft werden.

```sh
python3 scripts/forderungsexport.py Forderungen.json Ausgabe_Gericht \
  --xjustiz-vorlage Stammdaten.xml \
  --xsd /lokales/schema/xjustiz_0300_insolvenz_3_5.xsd
```

Der Helfer gleicht Aktenzeichen, Gerichtscode und Verknüpfungen ab, erhält die stabilen Forderungs- und Beteiligtenkennungen, erzeugt eine neue Nachrichten-ID und prüft das Ergebnis gegen das bereitgestellte Schema. Fehler brechen den Export ab. Ab dem Versionswechsel am 30. April 2027 sperrt er diesen Weg bis zur Anpassung. Die neutrale Prüftabelle bleibt nutzbar.

## 1.5. Freigabe vor Versand

Auch ein erfolgreich XSD-geprüfter Entwurf ist noch nicht versandfreigegeben. Externe Codelisten, Schematron-Regeln, Gerichtsvorgaben, Gläubigeridentität, Rangzuordnung, vollständige Anlagen, bereits erfolgte Einreichungen und die Vollständigkeit der Tabelle müssen gesondert geprüft werden. Die amtlichen [XJustiz-Werkzeuge](https://xjustiz.justiz.de/XJustiz-Werkzeuge/index.php) und das eingesetzte Fachverfahren sind hierfür geeignete Anknüpfungspunkte. Ein grünes XSD-Ergebnis belegt nur die geprüfte technische Struktur.

Die Verwaltung vergleicht vor dem Versand Anzahl und Summe der Forderungen mit dem Eingangsbuch, kontrolliert Gläubiger und Verfahrensdaten und lässt offene Punkte sichtbar. Freigabe, Versandprotokoll und gerichtliche Eingangsbestätigung getrennt ablegen. Scheitert der Export, das lesbare Ergebnis sichern und den konkreten Fehler an die zuständige Fachverfahrensbetreuung geben; nicht durch Umbenennen einer beliebigen XML-Datei eine gerichtliche Importfähigkeit vortäuschen.
