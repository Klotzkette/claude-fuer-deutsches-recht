# 1. Vom ersten Gespräch zum gepflegten Register

Die Arbeit beginnt mit vorhandenen Unterlagen und einem konkreten Produkt. Fragen Sie bei offenem Ziel, ob der Nutzer den Bestand sehen, ein neues Verzeichnis anlegen oder Änderungen einpflegen möchte. Ein beantworteter Auftrag deckt die erforderliche interne Dateiarbeit ab. Externe Erklärungen, produktive Systemänderungen und Behördenvorlagen sind davon zu unterscheiden.

## 1.1. Arbeitsphasen

| Phase | Ergebnis | Übergang |
|---|---|---|
| Einstieg | Unternehmen, Rolle, Umfang, führender Bestand sind geklärt. | Bestand erheben oder konkrete Änderung abgleichen. |
| Erhebung | Tätigkeiten, Quellen, Personen- und Datenkategorien liegen vor. | Rechtsgrundlagen, Löschung und Dienstleister prüfen. |
| Fachprüfung | Nachweisbare Angaben und offene Entscheidungen sind getrennt. | Register zusammenführen und DSFA-Vorprüfung durchführen. |
| Entscheidung | Menschliche Bewertung mit Begründung und geprüftem Sachstand. | Maßnahmen abarbeiten, erforderliche DSFA vertiefen. |
| Ausgabe | Rollengetrennte Dateien mit identischem Stand. | Interne Nutzung oder konkret freigegebene Vorlage. |
| Pflege | Änderungen, Konflikte und Wiedervorlagen sind nachvollziehbar. | Betroffene Fachprüfung erneut aufnehmen. |

## 1.2. Produktkennungen und Übergaben

Die folgenden Produktkennungen bezeichnen Arbeitsprodukte, nicht zwingend gleichnamige Dateien. Jede Übergabe nennt Tätigkeitskennung, führende Registerrevision, Belege, offenen Punkt und benötigte Rückgabe. Ein formaler Importerfolg ersetzt keine fachliche Beantwortung.

| Abgebender Skill | Produkt | Empfangender Skill | Rückgabe |
|---|---|---|---|
| Verarbeitungen erheben | `erhebung` | Verzeichnis erstellen | Zugeordnete Tätigkeitskennungen, Trennungs- oder Lückenfragen. |
| Verarbeitungen erheben | `erhebung` | Rechtsgrundlagen und Löschung | `rechts-und-loeschpruefung` mit Registerformulierungen und Nachweisen. |
| Verarbeitungen erheben | `erhebung` | Dienstleister, Transfers und TOM | `dienstleisterpruefung` mit Rollen- und Transferbefunden. |
| Verzeichnis erstellen | `register` | Risiken und DSFA | `dsfa-vorpruefung` mit gebundener Entscheidung oder konkretem Vertiefungsauftrag. |
| Risiken und DSFA | `dsfa-vorpruefung` | Dienstleister, Transfers und TOM | Nachgewiesene Maßnahmen, Grenzen und verbleibender Prüfbedarf. |
| Fachprüfung | `register` und Fachbefund | Änderungen nachhalten | `aenderungsprotokoll`, neue Revision und veraltete Prüfstände. |
| Änderungen nachhalten | `register` | Verzeichnis ausgeben | `exportpaket` mit Ausgabeformaten, Stand und Prüfbericht. |
| Verzeichnis ausgeben | `exportpaket` | Verzeichnis steuern | Tatsächlicher Ausgabeort, Umfang und nächster Pflegeanlass. |

## 1.3. Drei unabhängige rechtliche Prüfungen

Die Ausnahme von der Verzeichnisführung nach Artikel 30 Absatz 5 DSGVO, die DSFA-Pflicht nach Artikel 35 und die Benennungspflicht nach Artikel 37 sowie § 38 BDSG haben unterschiedliche Voraussetzungen. Eine kleine Belegschaft beantwortet keine dieser Fragen allein. Interne Bearbeitungsprioritäten ordnen Aufgaben und sind keine gesetzlichen Risikoklassen.

Bei einer DSFA-pflichtigen Verarbeitung ist die vollständige Folgenabschätzung ein weiteres Produkt. Die gespeicherte Auswahl „erforderlich“ bedeutet weder, dass diese schon erstellt wurde, noch dass eine Konsultation erledigt oder die Verarbeitung genehmigt wurde. Eine negative Entscheidung benötigt einen dokumentierten Sachstand und tragfähige Begründung. Geänderte Tatsachen verlangen erneute Betrachtung.

# 2. Arbeitsmodi

## 2.1. Mit Dateizugriff

Der Helfer [vvt.py](../scripts/vvt.py) führt den lokalen JSON-Bestand und erzeugt Ansichten. Vor der Verwendung Hilfe und [Dateipflege](dateipflege.md) lesen. Änderungen werden mit Registerrevision, Prüfsumme, Name und Anlass durchgeführt. Excel-Rückimporte beziehen sich auf einen bestimmten Ausgangsstand; der Helfer verweigert widersprüchliche Übernahmen. Fehlende Zeilen sind keine Löschanweisung.

Der lokale Helfer bietet keine echte Mehrbenutzer-Datenbank, keine automatische Anmeldung bei einer Datenschutzplattform und keinen ständigen Hintergrunddienst. Er ersetzt keine unabhängige Sicherung oder Berechtigungsverwaltung des Speicherorts. Bei vielen gleichzeitigen Bearbeitern oder komplizierten Unternehmensgruppen ist ein hierfür geeignetes System zu wählen; die Daten können als Migrationsgrundlage dienen.

## 2.2. Ohne Dateizugriff

Arbeiten Sie mit einem klar gekennzeichneten Registerentwurf und einem abschließenden Statusblock. Dieser nennt Unternehmen, Rolle, Tätigkeitskennungen, zugrunde gelegten Stand, offene Fragen und nächstes Produkt. Keine nicht erfolgte Speicherung, Synchronisation oder Erinnerungsfunktion behaupten. Nach erneutem Hochladen prüfen Sie, ob tatsächlich die letzte führende Fassung vorliegt.

Die Nutzerin kann JSON oder Excel in einer geeigneten Umgebung weiterführen. Ein im Chat dargestellter Datenblock ist noch keine tatsächlich angelegte Datei. Erzeugen Sie nur unterstützte Formate oder nennen Sie die Grenze konkret. Eine solche technische Grenze rechtfertigt nicht das Erfinden fehlender Betriebsangaben.

# 3. Freigaben und Entscheidungen

Sachliche Entscheidungen stammen von der benannten zuständigen Person. Der Datenschutzbeauftragte berät und überwacht; die Rolle macht ihn nicht automatisch zum betrieblichen Entscheider sämtlicher Vorgänge. Eine Maschinenbezeichnung oder bloß eingetragener Name beweist keine abgegebene Entscheidung. Quellen, Zeitpunkt, Begründung und Zuständigkeit müssen nachvollziehbar sein.

Vor einer externen Vorlage werden Adressat, Inhalt, Anlagen und Versandweg bestimmt. Ein interner Auftrag zur Registerpflege ist keine Einwilligung in öffentliche Veröffentlichung. Die konkrete Nutzerautorisierung kann den externen Schritt bereits umfassen; dann wird sie dokumentiert und nicht unnötig erneut abgefragt. Unklare Außenwirkung wird bis zur notwendigen Klärung vorbereitet, während unabhängige interne Arbeit fortgesetzt wird.

# 4. Pflegeanlässe

Neue Software, geänderte Funktionen, zusätzliche Zwecke, sensible Daten, neue Empfänger, Unterauftragnehmer, Fernzugriffe, Löschregeln und Vorfälle sind typische Anlässe. Weder die Bezeichnung einer Software noch ihre unveränderte Versionsnummer belegt unveränderte Verarbeitung. Die Prüfung muss die tatsächliche Nutzung erfassen.

Eine frei gewählte jährliche Wiedervorlage ist ein Organisationsstandard und keine pauschale gesetzliche Jahresfrist. Risiko- oder sachverhaltsbedingte Änderungen können eine frühere Prüfung erfordern. Ohne eingerichtete und bestätigte Erinnerung wird nur ein Datum gespeichert. Offene Maßnahmen nennen zuständige Person, benötigten Nachweis und Termin; bei Fristablauf verschwinden sie nicht aus dem Cockpit.

# 5. Qualitätskontrolle

Prüfen Sie an realistischen Sachverhalten: regelmäßig verarbeitender Kleinstbetrieb; Dienstleister in zwei Rollen; nicht geklärter Drittlandsupport; KI-Pilot mit besonders schutzbedürftigen Personen; konkurrierende Excel-Bearbeitung; veraltete DSFA-Entscheidung. Eine Datei kann technisch gültig und inhaltlich unvollständig sein. Bezeichnen Sie den Umfang jedes Selbsttests präzise.

Enddokumente und Empfängerschreiben werden vollständig ausformuliert. Tabellen dienen der Übersicht und ersetzen keine erforderliche Begründung. Formatstandard ist Times New Roman, 11 pt, mit dezimaler Gliederung. Bei einer tatsächlichen Ersatzschrift oder reinem Chattext wird dies in einer gesonderten Exportnotiz erläutert.
