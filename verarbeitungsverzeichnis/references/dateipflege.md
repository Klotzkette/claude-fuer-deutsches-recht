# 1. Lokale Pflege mit einer führenden Datei

Der Helfer `scripts/vvt.py` führt das Verarbeitungsverzeichnis in einer JSON-Datei. Excel dient der strukturierten Bearbeitung, Word der lesbaren Darstellung und XML dem verlustfreien Austausch innerhalb dieses Plugins. Die HTML-Übersicht lässt sich lokal öffnen, nach Tätigkeiten filtern und als JSON herunterladen. Sie benötigt weder Server noch Anmeldung. Sie ist eine Momentaufnahme und aktualisiert sich nach einem erneuten Export; eine Cloud-Synchronisation, Benutzerverwaltung oder laufende Überwachung ist damit nicht verbunden.

Bearbeiten Sie das Unternehmen zuerst anhand seiner tatsächlichen Verarbeitungstätigkeiten. Die technische Grenze von 5.000 Tätigkeiten beziehungsweise 25 MiB Eingabedatei beschreibt den Umfang des Helfers. Sie ist keine gesetzliche Befreiung, Unternehmensgrößenschwelle oder Zusicherung der Eignung für jede Organisation. Ein Nachweis über Beschäftigtendaten oder Patientendaten gehört in einen geschützten Belegordner; in das Verzeichnis gehören die erforderlichen Kategorien und Belegverweise, regelmäßig keine Personal-, Patienten- oder Kundeneinzellisten.

## 1.1. Voraussetzungen

Für Status, JSON, XML und HTML genügt Python 3.10 oder neuer. Excel benötigt `openpyxl`, Word `python-docx`. Die Pakete werden durch den Helfer weder selbst installiert noch über das Netz geladen. Fehlt eine Bibliothek, ist der betreffende Export offen; der Helfer behauptet keine erzeugte Datei. In einer bereits eingerichteten Umgebung lautet der Einstieg `python3 scripts/vvt.py --help`, ausgeführt im Pluginordner. Ansonsten ist der vollständige Pfad zum Skript einzusetzen.

Dateien und Sicherungsverzeichnis sind innerhalb der freigegebenen Unternehmensumgebung abzulegen. Betriebssystemzugriffe, Laufwerksverschlüsselung, Datensicherung und gegebenenfalls Rollenrechte werden dort eingerichtet. Der Helfer setzt neue Register-, Word- und Exceldateien auf einen restriktiven Dateimodus, stellt aber keine plattformübergreifende Zugriffsverwaltung bereit. Die Dateihashes weisen einen konkreten Bearbeitungsstand aus. Sie sind keine Signatur, Identitätsprüfung oder manipulationssichere Archivierung.

## 1.2. Register anlegen und lesen

Die Befehle setzen ein bereits vorhandenes Arbeitsverzeichnis voraus. In den Beispielen ist Alma Gundelfinger eine fiktive verantwortliche Person.

```bash
python3 scripts/vvt.py init arbeit/vvt.json --organization "Federkiel GmbH" --contact "Geschäftsführung, Musterweg 7, Beispielstadt" --dpo "Bestellung und Kontaktdaten noch zu prüfen" --actor "Alma Gundelfinger" --reason "Erstaufnahme der Verarbeitungstätigkeiten"
python3 scripts/vvt.py status arbeit/vvt.json
python3 scripts/vvt.py validate arbeit/vvt.json
```

`status` nennt Register-ID, Revision, SHA-256, Tätigkeitszahl, Lücken, offene Screeningfragen, dokumentierte Pflichttrigger und den Stand der DSFA-Prüfung. `validate` kontrolliert das Datenmodell, zulässige Werte und wesentliche interne Widersprüche. Ein erfolgreicher Lauf bedeutet keine materielle DSGVO-Konformität. Die Lückenprüfung erfasst für Verantwortliche andere Rollenfelder als für Auftragsverarbeiter. Sie enthält zusätzlich die intern erforderliche zuständige Person; das Feld `owner` ist dadurch keine gesonderte gesetzliche Mindestangabe nach Artikel 30 DSGVO. Der Helfer erkennt beispielsweise keine unzutreffende Löschfrist, bloß vorgeschobene Einwilligung oder fehlende tatsächliche Schutzmaßnahme.

# 2. Tätigkeiten und Änderungen erfassen

Jede Tätigkeit erhält eine dauerhaft eindeutige Kennung wie `VT-0001`. Neue Kennungen dürfen nicht aus gelöschten Zeilen wiederverwendet werden. Eine neue Tätigkeit beginnt ohne abweichende Angabe mit `status: "geplant"`. Eine Prüfung aktiviert sie nicht automatisch. Weitere zulässige Werte sind `aktiv`, `pausiert` und `beendet`. Eine beendete Tätigkeit wird mit `status: "beendet"` fortgeführt; der Helfer bietet keine automatische Löschoperation. Registerrevision und Tätigkeitsrevision sind unterschiedliche Angaben. Eine Sachänderung erhöht beide, eine dokumentierte Prüfung erhöht die Registerrevision. Unverändert zurückgespielte Daten erzeugen keine Scheinänderung.

## 2.1. JSON-Änderung

Eine Änderungsdatei enthält ein Objekt oder eine Liste solcher Objekte. Nicht genannte Felder bleiben erhalten. Ein leerer Text leert das benannte Feld und bedeutet „noch nicht erhoben“. Der Text `unbekannt` bedeutet eine ausdrücklich festgehaltene Erkenntnislücke. `nein` darf nicht als Ersatz für einen fehlenden Befund verwendet werden.

```json
{
  "id": "VT-0001",
  "title": "Lohnabrechnung",
  "role": "controller",
  "owner": "Alma Gundelfinger",
  "purpose": "Die Vergütung wird berechnet und die gesetzlichen Abgaben werden abgeführt.",
  "data_subjects": "Beschäftigte und ausgeschiedene Beschäftigte.",
  "sources": "Datenflussplan Lohn, Fassung 3; Interview Personalabteilung.",
  "next_review": "2027-03-15"
}
```

Nach `status` sind die tatsächlich ausgegebene Revision und der dort genannte Hash einzusetzen. `AKTUELLER_HASH` im folgenden Beispiel ist ein sichtbar auszuwechselnder Platzhalter, kein gültiger Prüfwert.

```bash
python3 scripts/vvt.py upsert arbeit/vvt.json --input arbeit/aenderung.json --expected-revision 0 --expected-sha256 AKTUELLER_HASH --actor "Alma Gundelfinger" --reason "Personalabteilung hat Zwecke und Datenkategorien bestätigt"
```

Die Sachfelder und ihre Rollenbedeutung erläutert das [Datenmodell](datenmodell.md). Die Schlüssel `review` und unbekannte Felder lassen sich nicht durch eine gewöhnliche Sachänderung einschleusen. Enthält eine Änderungsliste einen Fehler, wird keine ihrer Tätigkeiten übernommen. Ein eigener Prüfungsbefehl hält die DSFA-Entscheidung fest.

## 2.2. Organisation ändern

Organisationsdaten werden durch `update-org` mit denselben Versionsangaben gepflegt. Die Eingabedatei darf `name`, `contact`, `representative` und `dpo` enthalten. Nicht genannte Felder bleiben erhalten.

```bash
python3 scripts/vvt.py update-org arbeit/vvt.json --input arbeit/organisation-aenderung.json --expected-revision 3 --expected-sha256 AKTUELLER_HASH --actor "Alma Gundelfinger" --reason "Datenschutzbeauftragte und Kontaktweg haben gewechselt"
```

Ein geänderter Organisationskontext öffnet die gespeicherten DSFA-Prüfungen erneut und erhöht die Tätigkeitsrevisionen. Die vorherigen Entscheidungen bleiben in der gesicherten Registervorfassung nachvollziehbar. Dies ist eine bewusst konservative technische Behandlung; die zuständige Person beurteilt, welcher fachliche Prüfumfang wegen der konkreten Änderung erforderlich ist.

# 3. Excel ausgeben und gezielt zurückspielen

```bash
python3 scripts/vvt.py export arbeit/vvt.json --out arbeit/export-r3 --formats json,xlsx,docx,xml,html
python3 scripts/vvt.py import-xlsx arbeit/vvt.json --input arbeit/export-r3/verarbeitungsverzeichnis.xlsx --actor "Alma Gundelfinger" --reason "Geprüfter Rücklauf der Fachabteilungen"
```

Der Export überschreibt keine vorhandene Ausgabedatei. Benutzen Sie für jeden Stand einen neuen Ordner. JSON bleibt die führende Fassung; Word-Änderungen werden nicht automatisch importiert.

## 3.1. Blätter und Bearbeitung

| Blatt | Zweck | Bearbeitung |
| --- | --- | --- |
| Uebersicht | Erläuterungen, Lücken und Prüfstände des Exportzeitpunkts | Lesefassung; keine Neuberechnung in Excel |
| Taetigkeiten | VT-ID, Tätigkeitsrevision, Rolle, Verantwortung, Zwecke, Systeme, Rechtsgrundlagen, Belege und Prüftermin | Sachfelder bearbeiten; vorhandene ID und Revision erhalten |
| Art30 | Rollenabhängige Angaben zu Auftraggebern, Kategorien, Empfängern, Transfers, Löschung und TOM | Sachfelder anhand von Belegen ergänzen |
| Screening | Pflichttrigger, fachliche Prüfkriterien, Begründung, Quellen und interne Priorität | Sachverhalt und Prüfgrundlage aktualisieren |
| Organisation | Kontaktdaten der Organisation | Nur lesen; Änderungen mit `update-org` |
| Entscheidungen | Gespeicherte DSFA-Prüfung und Gültigkeitsstatus | Nur lesen; Entscheidungen mit `review` |
| _meta | Register-ID, Revision und Vergleichshashes | Technisches verborgenes Blatt erhalten |

In den drei Eingabeblättern enthält die verborgene erste Zeile die stabilen Feldschlüssel. Die zweite Zeile erläutert die Spalten auf Deutsch; Daten beginnen in Zeile 3. Spaltennamen, Reihenfolge und Zusatzblätter sind Teil des Importformats. Ein abweichender Export eines anderen Produkts ist zunächst in einem gesonderten Arbeitsgang zuzuordnen und zu prüfen; er kann nicht ungeprüft eingespielt werden.

Der Prüftermin wird als echtes Excel-Datum mit Format `yyyy-mm-dd` ausgegeben und bleibt dadurch sortierbar. Beim Import werden native Datumswerte oder eindeutiger ISO-Text angenommen. Eine bloße Zahlenserie ohne Datumformat, eine Uhrzeit oder ein unmögliches Datum wird abgewiesen. Leere Datumszellen bleiben leer. Eine neue Tätigkeit beginnt im Blatt Taetigkeiten mit neuer VT-ID und Tätigkeitsrevision `0`. Fehlende Zusatzangaben bleiben offen; sie erhalten keine günstigen Standardannahmen.

## 3.2. Importregeln und Konflikte

Ein Import benötigt dieselbe Register-ID, Revision und denselben Hash wie der Ausgangsexport. Sobald zwischenzeitlich eine andere Bearbeitung gespeichert wurde, ist der Rücklauf abzugleichen und neu zu exportieren. Der Helfer führt keine automatische Zusammenführung konkurrierender Änderungen aus.

Fehlende Zeilen oder entfernte Einträge in einem Zusatzblatt löschen keine Tätigkeit und keine anderen Blattangaben. Die Bearbeitung einer vorhandenen leeren Zelle kann dagegen eine explizite Leerung des zugehörigen Sachfelds bedeuten. Doppelte IDs, neue Tätigkeiten ohne Stammzeile, veränderte Prüfentscheidungen, geänderte Organisationsdaten, Formeln, aktive Links, Makros und externe Arbeitsmappenverknüpfungen werden zurückgewiesen. Als Text gespeicherte Inhalte wie `=HYPERLINK(...)` werden nicht ausgeführt. Eine nachträglich von Excel tatsächlich als Formel gespeicherte Eingabe wird beim Import blockiert.

Zeilenhöhe und Textumbruch werden nach dem Inhalt gesetzt. Bei sehr langen Texten erreicht Excel seine Darstellungsgrenze; der Zellinhalt bleibt vollständig erhalten und ist in der Bearbeitungszeile oder in der Word-Lesefassung zu lesen. Ein gedrucktes Blatt darf nicht durch eine zwanghafte Ein-Seiten-Skalierung unlesbar gemacht werden. Die Word-Blätter verwenden Times New Roman, 11 pt und ausformulierte Erläuterungen der dokumentierten Angaben.

# 4. DSFA-Prüfung und Wiederaufnahme

Die interne Priorität `1`, `2` oder `3` ist eine Arbeitsreihenfolge. Sie ist keine gesetzliche Risikoklasse. Weder eine niedrige Priorität noch die interne Kombination aus Schwere und Wahrscheinlichkeit erzeugt eine Freigabe. Der Helfer setzt keine fachliche Bewertung allein aufgrund einer Punktzahl.

Die Screeningfelder `high_risk`, `art35_3` und `positive_list` nehmen jeweils `offen`, `ja` oder `nein` auf. Eine begründete Nichtdurchführung der DSFA lässt sich nur dokumentieren, wenn diese drei Prüffragen zuvor verneint wurden. Die tatsächliche Einschlägigkeit der Liste, der gesetzlichen Tatbestände und der übrigen Risikoumstände muss die zuständige Person belegen; der Helfer verifiziert diese Rechtsfragen nicht. Mehrere gewichtige Kriterien sind fachlich im Zusammenspiel zu würdigen, auch wenn kein bereits bejahter Pflichttrigger eingetragen wurde.

```bash
python3 scripts/vvt.py review arbeit/vvt.json --id VT-0001 --decision erforderlich --rationale "Die dokumentierte Bewertung ergibt ein voraussichtlich hohes Risiko; die neue Nutzung wird bis zur erforderlichen Klärung nicht freigegeben." --sources "Fallbezogener Prüfvermerk und geprüfte Primärquellen" --expected-revision 4 --expected-sha256 AKTUELLER_HASH --actor "Alma Gundelfinger" --reason "DSFA-Screening nach Einführung des neuen Systems"
```

Für die begründete Gegenentscheidung lautet der Wert `begruendet_nicht_erforderlich`. Die gespeicherte Prüfung enthält Person, Zeitpunkt, konkrete Begründung, Quellen und Hash des geprüften Sachstands. Der Helfer verlangt einen menschlichen Namen und weist Maschinenbezeichnungen ab; er authentifiziert die Person damit nicht. Die Organisation muss Verantwortlichkeit und Berechtigung gesondert sicherstellen.

Jede Sachänderung entwertet den bisherigen Prüfhash. `status` zeigt die erhaltene Entscheidung dann als `veraltet`; sie darf nicht als aktuelle Freigabe verwendet werden. Das neue Screening, eine nötige DSFA und gegebenenfalls weitere Maßnahmen bleiben eigenständige Aufgaben. Auch eine als erforderlich gespeicherte DSFA-Entscheidung bedeutet nicht, dass die DSFA bereits durchgeführt wurde.

# 5. XML, Sicherung und Fehlerbehandlung

XML wird als UTF-8-Container mit einem JSON-Nutzdatenfeld ausgegeben. Das ist ein offenes, dokumentiertes Pluginformat, kein behaupteter amtlicher Standard und keine zugesicherte Kompatibilität mit fremden Datenschutzprodukten. Es erhält leere Texte, Datentypen, Revisionen und Belegangaben ohne Umdeutung. Die XML-Wurzel enthält die Referenz auf den Ausgangsstand; sie bleibt beim Bearbeiten unverändert.

```bash
python3 scripts/vvt.py import-xml arbeit/vvt.json --input arbeit/export-r3/verarbeitungsverzeichnis.xml --actor "Alma Gundelfinger" --reason "Geprüfter XML-Rücklauf"
```

DSFA-Prüfentscheidungen und Organisation dürfen auch über XML nicht verändert werden. Neue XML-Tätigkeiten tragen Tätigkeitsrevision `1` und eine offene Prüfung. Fehlende Tätigkeiten löschen den Bestand nicht. Dokumenttypdefinitionen, externe Entitäten, UTF-16-Tricks, fremde Kodierungsdeklarationen und unbekannte Strukturen werden zurückgewiesen. Der Import öffnet keine im Inhalt genannten Internetadressen oder Belegpfade.

Vor einer Änderung erhält die bisherige Fassung unter `vvt.json.history/` eine Datei aus Revision und Hash. Der Schreibvorgang ersetzt die führende Datei atomar; eine Sperrdatei verhindert zwei gleichzeitig schreibende Helfer. Der Verlauf nennt Zeitpunkt, verantwortliche Person, Anlass, geänderte IDs und vorherigen Hash. Die Vorfassungen werden nicht automatisch bereinigt. Organisatorische Aufbewahrung, Wiederherstellung und spätere Löschung einschließlich Sicherungen sind deshalb eigens festzulegen.

Eine vorhandene `.lock`-Datei darf nur nach Prüfung eines noch laufenden Vorgangs entfernt werden. Bei Fehlern bleibt die führende Fassung unverändert; die konkrete Meldung bezeichnet den Konflikt. Ein Dateisystemausfall kann bereits angelegte Sicherungskopien hinterlassen, ohne dass die neue Fassung übernommen wurde. Die Sicherung ist deshalb über den Registerstand und den protokollierten Hash einzuordnen. Die Protokolle und Vorfassungen sind ebenfalls vertraulich.

# 6. Reproduzierbare Prüfung

Der Repositorytest `python3 scripts/test-verarbeitungsverzeichnis-runtime.py` prüft die tatsächlichen Änderungen und Exporte, unter anderem unveränderte Excel- und XML-Rundläufe, Leerwerte, Unicode, Datumsbearbeitung, Versionskonflikte, doppelte IDs, nicht gelöschte fehlende Zeilen, atomaren Abbruch, Formeltext und Formelinjektion, Pflichttrigger, veraltete Prüfungen, Rollenunterschiede, Vorfassungen, gesperrte Dateien, XML-Entitäten, sichere HTML-Einbettung und das Word-Grundformat. Ein technischer Test ersetzt die fachliche Prüfung der [Rechtsquellen](rechtsquellen.md) und der konkreten Verarbeitung nicht.
