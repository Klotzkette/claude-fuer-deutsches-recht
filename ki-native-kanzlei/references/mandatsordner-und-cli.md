# 1. Ein Mandatsordner, ein führender Stand

Die Hilfsprogramme arbeiten ausschließlich mit dem gewählten lokalen Ordner. Sie senden keine Nachricht und greifen auf keinen Kanzleiserver zu. Claude Code oder Codex können sie bei verfügbarem Python ausführen. In ChatGPT funktionieren die Prompts mit bereitgestellten Dateien; ein lokaler Mandatsordner ist dort nur fortschreibbar, wenn die verwendete Oberfläche den Zugriff tatsächlich bereitstellt. Ohne Dateizugriff werden die aktualisierten Dateien zum Herunterladen geliefert. Eine automatische Synchronisierung darf nicht behauptet werden.

`00_Mandat/mandatsjournal.sqlite` ist der führende strukturierte Stand. `01_Bearbeitung` enthält Arbeitsprodukte, `02_Honorar` die aus dem Journal abgeleiteten Honoraransichten und `03_beA_Vorbereitung` die Versandvorbereitung. Originale können in einem danebenliegenden, unveränderten Originalordner liegen. Das Journal ist ein lokales Hilfsmittel, kein manipulationssicheres GoBD-Archiv und kein Ersatz für eine ordnungsgemäße Finanzbuchführung.

## 1.1. Vor jedem fachlichen Arbeitsschritt

Die gespeicherte Honorargrundlage kurz vorhalten: „Für diesen Auftrag sind 240 EUR netto je Stunde mit einem Nettohonorardeckel von 1.200 EUR dokumentiert. Gilt das weiterhin für diesen Schritt?“ Bei einem Festpreis nach Umfang und Zusatzauftrag fragen, bei einem Fee Quote nach seiner Verbindlichkeit und bei einer Schätzung nach einem zusätzlich vereinbarten Deckel. Änderungen nicht aus einer Überschrift ableiten.

Nach der Tätigkeit tatsächliche Minuten, Person, Datum, Abrechenbarkeit und den gewünschten Abrechnungstext erfragen. Einen Text vorschlagen, der die konkrete Tätigkeit beschreibt und keine unnötigen Geheimnisse offenbart. Erst nach Bestätigung als abrechenbar übernehmen. Auch echte Nullminuten und nicht abrechenbare Tätigkeiten bleiben als solche erkennbar. Während einer offenen Rückfrage darf an anderen beauftragten Teilen weitergearbeitet werden.

## 1.2. Voraussetzungen und Aufruf

Für das Journal und den XML-Exporter genügt Python 3.10 oder neuer ohne zusätzliche Pakete. Die separaten PDF-Werkzeuge benötigen die in Abschnitt 4 genannten Abhängigkeiten. Pfade mit Leerzeichen immer in Anführungszeichen setzen. Eingaben werden in einer UTF-8-JSON-Datei gespeichert; es werden keine personenbezogenen Angaben in Shell-Befehle interpoliert.

```bash
python3 "<Pluginordner>/scripts/kanzlei.py" init --akte "/Mandate/SI-2026-001" --data "/Arbeitsordner/mandat.json"
python3 "<Pluginordner>/scripts/kanzlei.py" terms --akte "/Mandate/SI-2026-001" --data "/Arbeitsordner/honorar.json"
python3 "<Pluginordner>/scripts/kanzlei.py" time --akte "/Mandate/SI-2026-001" --data "/Arbeitsordner/zeit.json"
python3 "<Pluginordner>/scripts/kanzlei.py" status --akte "/Mandate/SI-2026-001"
python3 "<Pluginordner>/scripts/kanzlei.py" draft --akte "/Mandate/SI-2026-001"
```

`status` liest den Journalstand. Die übrigen erfolgreichen Befehle schreiben die Honoraransichten synchron fort. Es läuft kein Hintergrunddienst. Nach einem unterbrochenen Export erzeugt `draft` die Ansichten aus dem Journal erneut. Der Journalstand ist in jeder Ansicht bezeichnet.

# 2. Eingabefelder und Rechenumfang

## 2.1. Mandat und Honorar

`init` benötigt `matter_id`, `client` und `subject`. Die Akten-ID muss eindeutig sein. Derselbe Ordner darf nicht mit anderen Mandatsdaten überschrieben werden.

`terms` benötigt `id`, `model`, `scope`, `agreement_ref`, `confirmed` und `vat_rate`. Ein Honorarabschnitt erhält beispielsweise die ID `HV-1`. Die Modelle sind `hourly` für Zeithonorar, `capped` für gedeckeltes Zeithonorar, `estimate` für Zeithonorar mit unverbindlicher Schätzung, `flat` für Festpreis und `rvg` für eine separat geprüfte gesetzliche Gebührenberechnung. Ein verbindliches Festpreisangebot wird als `flat` erfasst; ein verbindlicher Höchstbetrag als `capped`. Ein ungeklärter Fee Quote wird noch keinem dieser Modelle als bestätigte Vereinbarung gleichgesetzt.

Für Zeithonorar wird `rate_eur` benötigt. Weitere Felder sind `cap_eur`, `estimate_eur` beziehungsweise `flat_eur`. Beträge sind netto, in EUR und höchstens centgenau. Bei `capped` ist mit `cap_scope=fees_only` oder `fees_and_expenses` ausdrücklich festzulegen, ob Auslagen in den Netto-Deckel fallen. Eine Schätzung begrenzt den Rechenbetrag nicht. Eine Überschreitung erzeugt eine offene Kostenkommunikation.

Die lokale Rechenhilfe unterstützt nur ausdrücklich angegebene inländische Standardumsätze mit `vat_rate=19`. Kleinunternehmer, Auslandsleistungen, Reverse Charge, nicht steuerbare durchlaufende Posten und besondere Steuersätze werden im Fachworkflow gesondert berechnet. Ein nicht unterstützter Steuerfall führt zu einem Fehler und niemals stillschweigend zu 19 Prozent. Die Prüfung der Vergütungsvereinbarung, gesetzlicher Untergrenzen, Fälligkeit und Auslagenerstattung bleibt gesondert erforderlich.

Solange `confirmed=false` ist, werden unbekannte Parameter und später eingehende Vereinbarungsangaben ergänzt; der Betrag wird nicht in den bekannten Gesamtbetrag übernommen. Bereits bestätigte und verwendete Grundlagen werden nicht nachträglich umgeschrieben. Eine zusätzliche Honorarphase darf nur einen tatsächlich getrennten Leistungsumfang erfassen. Einen laufenden Gesamtdeckel darf man nicht durch eine neue Phasen-ID umgehen. Änderungen desselben bereits bestätigten Auftrags bedürfen einer gesonderten nachvollziehbaren Neubewertung außerhalb der einfachen Hilfsrechnung.

## 2.2. Zeiten und Korrekturen

`time` erhält `id`, `terms_id`, `work_date`, `person`, `minutes`, `narrative`, `billable`, `confirmed` und `source`. Datum im Format `YYYY-MM-DD`; tatsächliche ganze Minuten, ohne automatische Viertelstundenrundung. `minutes=null`, `billable=null` oder `confirmed=false` halten einen ungeklärten Eintrag offen. Eine bestätigte Zeit braucht Dauer und Abrechenbarkeit. Ohne bekannte Honorargrundlage kann `terms_id=null` bleiben; der Zeitbeleg bleibt erhalten, aber eine Honorarzuordnung offen.

Eine unveränderte Eingabe mit derselben ID ist wirkungslos und erzeugt keine zweite Buchung. Dieselbe ID mit anderem Inhalt wird abgewiesen. Eine Korrektur erfolgt durch begründetes Storno und eine neue ID. Im neuen Quellenvermerk auf die ersetzte Buchung verweisen. Auch die Zuordnung einer zunächst unzugeordneten Zeit erfolgt auf diesem nachvollziehbaren Weg.

```bash
python3 "<Pluginordner>/scripts/kanzlei.py" void --akte "/Mandate/SI-2026-001" --id "Z-3" --reason "Dauer nach Rücksprache berichtigt"
```

Der Entwurf enthält nur bestätigte, zugeordnete und abrechenbare Beträge. Ungeklärte Positionen bleiben daneben sichtbar. Die bekannten Teilbeträge sind keine vollständige Rechnung. Bei Festpreis werden Minuten dokumentiert, jedoch nicht zusätzlich auf den Festpreis aufgeschlagen. RVG-Gebühren werden niemals aus einem Stundensatz abgeleitet.

## 2.3. Auslagen, gesetzliche Gebühren und Zahlungen

`expense` benötigt `id`, `terms_id`, `date`, `net_eur`, `description`, `source`, `confirmed` und `tax_classification=own_taxable`. Das letzte Feld bestätigt die bereits geprüfte Einordnung als eigene steuerpflichtige Leistung. Echte durchlaufende Posten dürfen nicht darüber erfasst werden.

`manual-fee` benötigt die gleichen Identifikations-, Datums-, Betrags-, Beschreibungs- und Quellenfelder sowie `legal_reviewed=true`. Es ist ausschließlich für einen RVG-Honorarabschnitt bestimmt. Die gesonderte Berechnung muss insbesondere Gegenstand, Gebührentatbestand, Gebührensatz, Wert oder Rahmen, Anrechnung, Auslagen und Übergangsrecht belegen. Das Eingabefeld ersetzt diesen Beleg nicht.

`payment` benötigt `id`, `date`, `gross_eur`, `kind`, `reference`, `source` und `confirmed`. Arten: `payment`, `advance` oder `third_party`. Die Zahlung wird separat dokumentiert. Sie wird nicht automatisch als Umsatz gebucht oder von einem Honorar abgezogen. Zuerst Rechnung und Leistungszeitraum zuordnen, Vorschussbesteuerung und Verrechnung prüfen, Fremdgeld getrennt halten und erst dann den passenden Buchhaltungsexport erstellen.

## 2.4. Dateien und Wiederherstellung

Der Entwurf besteht aus `rechnungsentwurf.md`, `rechnungsentwurf.json` und `zeiten.csv`. JSON enthält offene Positionen, Phasen, Zahlungen und Journalrevision. CSV wird gegen Tabellen-Formeleinschleusung abgesichert. Diese Ansichten werden regeneriert; manuelle Änderungen gehören als neue belegte Eingabe ins Journal. Backups der Datenbank und fachübliche Zugriffsrechte bleiben Teil des Kanzleibetriebs. Eine Datenbankkopie nur bei geschlossenem Werkzeug oder mit dem SQLite-Backup-Verfahren erzeugen.

# 3. E-Rechnung als echte XML-Datei

`scripts/xrechnung.py` erzeugt eine UBL-XRechnung 3.0.2 für den ausdrücklich begrenzten Standardfall: EUR, inländische Parteien, positive Positionen, 19 Prozent Umsatzsteuer, keine Rabatte, Verrechnung von Vorschüssen, Gutschriften oder Sonderbesteuerung. Für andere Konstellationen den Fachskill und ein geeignetes geprüftes Rechnungswerkzeug verwenden. XRechnung 4.0 ist am dokumentierten Quellenstand noch keine finale Produktionsversion.

Die vollständige Eingabestruktur steht in `assets/xrechnung-beispiel.json`. Stammdaten, tatsächlicher Leistungsempfänger, Leistungszeitraum, Rechnungsnummer, Käuferreferenz, elektronische Adressen, Steuerdaten und Zahlungsdaten müssen belegt sein. Eine Rechtschutzversicherung ist nicht allein aufgrund ihrer Zahlung der Leistungsempfänger. Bei B2G keine Leitweg-ID erfinden.

```bash
python3 "<Pluginordner>/scripts/xrechnung.py" --input "/Arbeitsordner/rechnung.json" --output "/Mandate/SI-2026-001/02_Honorar/Rechnung_Entwurf_v1.xml"
```

`document_state=draft` kennzeichnet die XML als Entwurf. `approved` setzt zusätzlich `legal_reviewed=true` voraus; das ersetzt weder eine echte Prüfung noch die Freigabe zum Versand. Der Export vergibt keine Nummer und prüft kein kanzleiweites Rechnungsnummernregister. Eine bestehende Ausgabedatei wird nicht überschrieben. Die XML wird nicht automatisch aus einer unvollständigen Honoraransicht als endgültige Rechnung übernommen.

Das Beispiel verwendet ausschließlich fiktive Parteien und Steuerdaten. Die IBAN `DE79000000001234567890` stammt als ausdrücklich nicht existierender, formal gültiger Testwert aus der amtlichen KoSIT-Testsuite. Die Musterdatei ist keine Rechnung über eine wirkliche Leistung und darf nicht versendet werden. Der Beispielbetrag ist ein Rechenbeispiel zum bekannten Zeitstand, keine abschließende Forderung aus der Übungsakte.

Nach jedem konkreten XML-Export den aktuellen offiziellen KoSIT-Validator mit der zugehörigen XRechnung-Konfiguration einsetzen. Der Beispieltest allein validiert keine spätere Rechnung. Die Versionen und Prüfergebnisse stehen im separaten Qualitätsbericht. Ein erfolgreicher Schematron-/XSD-Test belegt keine Echtheit der Steuernummer, Rechtswirksamkeit der Honorarforderung oder erfolgreiche Zustellung. Ein PDF-Ausdruck ist zusätzlich möglich; er ersetzt den strukturierten Originaldatensatz nicht.

# 4. beA-Vorbereitung aus belegter Anlagenzuordnung

`scripts/build_anlagenkonvolut.py` und `office_process.py` stammen aus dem vorhandenen Anlagen-Werkzeug dieses Repositorys. Im neuen Plugin wird standardmäßig nur die erste Anlagenseite gestempelt. Die Dateigröße wird konservativ gegen 200.000.000 Bytes geprüft. Quelle und aktuelle technische Grenzen stehen in `rechtsquellen.md`.

Zuerst das Hauptdokument vollständig auf Anlagenbezüge prüfen und die tatsächlichen Belege nach Inhalt, Datum, Aussteller und Fassung zuordnen. Erst danach Kopien in einen Arbeitsordner mit Namen wie `Anlage_K1_Pachtvertrag.pdf` legen. Das Werkzeug kann diese vorgeprüfte Zuordnung verarbeiten; es erkennt nicht selbst zuverlässig aus einem Schriftsatz, welches Beweisstück gemeint ist. K3a, Konvolute, bereits eingereichte Anlagen, Widersprüche und fehlende Belege müssen im Fachskill einzeln geklärt werden.

```bash
python3 "<Pluginordner>/scripts/build_anlagenkonvolut.py" --eingang "/Mandate/SI-2026-001/Anlagenkopien" --ausgang "/Mandate/SI-2026-001/03_beA_Vorbereitung/Version1" --hauptdokument "/Mandate/SI-2026-001/01_Bearbeitung/Schriftsatz.pdf" --praefix K --stempel-seiten erste --strict
```

Benötigt werden `pypdf`, `reportlab` und für Office-Konvertierung LibreOffice. Vorhandene Laufzeit verwenden; keine systemweiten Änderungen oder Installation behaupten. Ein existierender Ausgabeordner bleibt geschützt; `--ueberschreiben` im normalen Mandatsworkflow nicht verwenden. Originale niemals als Arbeitskopien stempeln. Signierte Dateien bleiben unverändert; eine Ansichtskopie muss ausdrücklich getrennt beauftragt und bezeichnet werden. Aktive PDF-Inhalte, fehlende Schriftressourcen oder nicht kontrollierbare Konvertierungen erzeugen offene Befunde.

Alle Stempelkopien visuell kontrollieren, insbesondere erste Seite, Querformat, Textüberlagerungen, Seitenzahl und Lesbarkeit. Prüfbericht und interne Metadaten gehören nicht zu den einzureichenden Anlagen. Die erzeugte Mappe ist eine Vorbereitung. Zuständigkeit, Empfänger, Frist, erforderliche Signatur und sicherer Übermittlungsweg werden vor einem ausdrücklich beauftragten Versand geprüft. Eine Versandbestätigung gilt erst nach tatsächlich eingegangener technischer Bestätigung und ihrer Kontrolle.


### 4.1 Vollständiger Nachrichtenumfang

Das beA-Handbuch v4.6.1 begrenzt normale Dateinamen beim Hochladen auf 84 Zeichen einschließlich Erweiterung, Signaturdateien auf 90. Die Erzeugung hält für Bundesprofile 84 und für die übrigen Profile konservativ 60 Zeichen ein. Die ERVB-Grenze beträgt 1.000 Dateien und 200 Megabyte; die lokale Prüfung rechnet konservativ mit 200.000.000 Bytes. Mit wiederholtem `--zusatzdatei /pfad/xjustiz_nachricht.xml` lassen sich tatsächlich vorhandene weitere Nachrichtendateien in die Mengenprüfung aufnehmen. Dazu zählen auch Signaturdateien und gegebenenfalls Nachrichtentext.pdf. Das Skript verändert diese Zusatzdateien nicht. Seine Mengenprüfung bestätigt nur den übergebenen Bestand: vor Versand die vollständige tatsächliche Nachricht erneut prüfen.

# 5. Mandatslauf als Zustandsdatei

`scripts/mandatslauf.py` führt `00_Mandat/mandatslauf.json`: Phase, Nebenläufe, Produktregister mit SHA-256 je führender Fassung, Gates G1 bis G8, offene Fragen, Revision und Historie. Befehle: `init` (mit `--matter-id` und `--stufe` 0 bis 3), `phase` (mit `--grund`, optional `--nebenlauf`), `product` (mit `--id`, `--pfad` relativ zum Mandatsordner, `--skill`, `--zustand` entwurf, geprueft oder freigegeben), `gate` (mit `--gate` und `--aktion` oeffnen, freigeben, ablehnen, nicht-erforderlich oder zuruecksetzen; `freigeben` und `ablehnen` verlangen `--person` und `--bezug`), `question` (mit `--text`, optional `--erledigt`), `status` und `next`. Die Datei wird atomar geschrieben; `init` überschreibt keinen vorhandenen Lauf; `freigegeben` setzt eine zuvor geprüfte Fassung voraus; der Wechsel in die Phase `abschluss` ist erst nach Entscheidung über G4, G5 und G8 möglich. Der Helfer schreibt keinen Kalender, versendet nichts und bucht nichts. Die Regeln zu Stufen und Gates stehen in [Mandatslauf und Freigabestufen](mandatslauf-und-freigaben.md).
