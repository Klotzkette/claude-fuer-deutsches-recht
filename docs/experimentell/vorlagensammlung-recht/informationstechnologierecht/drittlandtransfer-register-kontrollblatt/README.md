# Drittlandtransfer-Register und Kontrollblatt
Internes Registerblatt zur laufenden Kontrolle von internationalen Datentransfers, Transferinstrumenten und Nachprüfungsfristen.

## Download
- [⬇ Drittlandtransfer-Register und Kontrollblatt – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/drittlandtransfer-register-kontrollblatt/drittlandtransfer-register-kontrollblatt.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Drittlandtransfer-Register und Kontrollblatt – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/drittlandtransfer-register-kontrollblatt/drittlandtransfer-register-kontrollblatt.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`drittlandtransfer-register-kontrollblatt.odt`](drittlandtransfer-register-kontrollblatt.odt) · [`drittlandtransfer-register-kontrollblatt.md`](drittlandtransfer-register-kontrollblatt.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage gehört zum Drittlandtransfer-Paket und dient der Dokumentation oder Freigabe eines konkreten internationalen Datentransfers. Sie passt nur, wenn Datenkategorien, Empfänger, Drittland, Transfermechanismus und technische Schutzmaßnahmen bereits fallbezogen erhoben werden können.

## Einschlägige Normen

- Art. 44 DSGVO als Grundnorm für Übermittlungen personenbezogener Daten in Drittländer und an internationale Organisationen.
- Art. 45 DSGVO für Angemessenheitsbeschlüsse, insbesondere die jeweils aktuelle EU-Liste und den EU-US Data Privacy Framework-Beschluss.
- Art. 46 Abs. 1 und Abs. 2 Buchst. c DSGVO für Standarddatenschutzklauseln; Durchführungsbeschluss (EU) 2021/914 als SCC-Modulanker.
- Art. 47 DSGVO für Binding Corporate Rules und Art. 49 Abs. 1 DSGVO für eng auszulegende Ausnahmen.
- Art. 28, Art. 30, Art. 32, Art. 35 DSGVO, wenn Auftragsverarbeitung, Verzeichnis, Sicherheitsmaßnahmen oder Datenschutz-Folgenabschätzung berührt sind.

## Pflichtangaben

Erforderlich sind Transfer-ID, Geschäftsprozess, System, Empfänger, Land, Rolle, Transferinstrument, DPF- oder SCC-Nachweis, TIA-Status, Betroffeneninformation, Auflagen, Nachprüfungsdatum und technischer Verantwortlicher.

## Mustertext mit Platzhaltern

Die Vorlage enthält eine registerfähige Tabelle mit Freigabevermerk und Eskalationslogik bei Statusänderungen.

## Hinweise zur Verwendung

Der Transfer wird erst freigegeben, wenn Datenkategorien, Empfängerrolle, Land, Unterauftragnehmer, Zugriffsszenarien und Übermittlungsmechanismus getrennt dokumentiert sind. SCC, Angemessenheitsbeschluss, Data Privacy Framework, Binding Corporate Rules und Art. 49 DSGVO sind keine austauschbaren Etiketten, sondern unterschiedliche Rechtfertigungswege mit eigener Begründung.

Fristen- und Nachweisarchitektur: Rezertifizierung, Lieferantenbestätigung, Review des Transfer Impact Assessment, Unterauftragnehmerfreigabe, Betroffeneninformation und Abhilfemaßnahmen werden mit Datum, Verantwortlichem und Wiedervorlage geführt. Behördenzugriffe und Exportbeschränkungen werden nicht pauschal bewertet, sondern nach Datenart, Zugriffswahrscheinlichkeit, Verschlüsselung und organisatorischer Kontrolle.

Abgrenzung: Für SCC-Begleitvereinbarung `informationstechnologierecht/standardvertragsklauseln-scc-begleitvereinbarung/`; für TIA `informationstechnologierecht/transfer-impact-assessment-scc-dsgvo/`; für DPF-Prüfung `informationstechnologierecht/eu-us-data-privacy-framework-pruefung/`.

## Taktische Hinweise

### Vorgehensreihenfolge

1. Zuerst wird der Registerschnitt festgelegt, damit das Kontrollblatt nicht an der falschen Einheit hängt. Eine Register-ID nach dem Kopf des Blattes wird je Kombination aus Dienst, Empfänger und Zielland vergeben, nicht je Anbieter; ein Anbieter mit Produktivsystem in einem Land, Supportzugriff aus einem zweiten und Backup in einem dritten erzeugt drei Zeilen. Erst dieser Schnitt macht die Statusfelder in Abschnitt 3.3 aussagekräftig, weil sonst eine gesperrte Teilübermittlung im Sammeleintrag verschwindet.

2. Danach wird Abschnitt 1.4 mit dem tatsächlichen Datenfluss abgeglichen und nicht mit der Produktbeschreibung des Anbieters. Speicherung, Fernzugriff, Support, Backup, Analyse und Weiterübermittlung sind eigenständige Übermittlungen im Sinne des Art. 44 DSGVO und jede von ihnen braucht ein tragendes Instrument. Belegt wird das über die Liste der administrativen Rollen mit Standort und über die Angabe, aus welchen Ländern der zweite und dritte Supportlevel arbeitet.

3. Erst dann wird das Instrument in Abschnitt 3.1 eingetragen, und zwar in der Stufenfolge des Kapitels V. Trägt ein Angemessenheitsbeschluss nach Art. 45 Abs. 1 DSGVO, ist damit nichts über die Auftragsverarbeitung gesagt, sodass Abschnitt 4.2 den Vertrag nach Art. 28 Abs. 3 DSGVO gesondert ausweisen muss. Fehlt ein Angemessenheitsbeschluss, kommen die geeigneten Garantien nach Art. 46 Abs. 1 und Abs. 2 DSGVO in Betracht; die Ausnahmen des Art. 49 Abs. 1 DSGVO taugen nach Art. 49 Abs. 1 Unterabs. 2 DSGVO nur für gelegentliche, nicht wiederholte Übermittlungen und sind für ein Produktivsystem regelmäßig kein Registereintrag, sondern ein Sperrgrund.

4. Anschließend werden die Nachweise in Abschnitt 3.2 mit Datum und Ablageort versehen, weil das Register die Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO bedient. Ein Eintrag „SCC vorhanden“ ohne Modulangabe, Unterzeichnungsdatum und befüllte Annexe ist kein Nachweis. Parallel wird Abschnitt 5.2 mit dem Verzeichnis der Verarbeitungstätigkeiten abgeglichen, das nach Art. 30 Abs. 1 Buchst. e DSGVO ohnehin die Drittlandempfänger und nach Art. 30 Abs. 1 Buchst. f DSGVO die vorgesehenen Löschfristen führen muss; zwei getrennt gepflegte Listen laufen sonst auseinander.

5. Zuletzt wird die Eskalation nach Abschnitt 6.3 an Fristen gebunden, die von außen vorgegeben sind. Ein ungeklärter Behördenzugriff kann zugleich eine Verletzung des Schutzes personenbezogener Daten sein, für die Art. 33 Abs. 1 DSGVO die Meldung binnen 72 Stunden nach Bekanntwerden verlangt und Art. 33 Abs. 5 DSGVO die interne Dokumentation vorschreibt. Wer Eskalationsempfänger benennt, ohne eine Reaktionszeit zu setzen, verliert diese Frist im Postlauf zwischen Fachbereich, Einkauf und Datenschutz.

### Typische Gegnereinwände mit Antwortlinie

- Der Fachbereich hält das Kontrollblatt für eine Dopplung des Verarbeitungsverzeichnisses und will es einsparen. Antwortlinie: Das Verzeichnis nach Art. 30 Abs. 1 DSGVO beschreibt die Verarbeitung, das Kontrollblatt trägt die Entscheidung über die Übermittlung mit Auflage, Frist und Freigabehistorie nach Abschnitt 7. Ohne diese Entscheidungsebene lässt sich die Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO nicht erfüllen, weil das Verzeichnis nicht ausweist, wer wann unter welchen Bedingungen freigegeben hat.

- Der Anbieter erklärt, seine Unterauftragnehmerliste stehe im Internet und werde laufend aktualisiert, weshalb eine Freigabe je Fall entbehrlich sei. Antwortlinie: Art. 28 Abs. 2 Satz 2 DSGVO lässt eine allgemeine schriftliche Genehmigung nur zu, wenn der Auftragsverarbeiter beabsichtigte Änderungen vorab mitteilt und dem Verantwortlichen die Möglichkeit zum Einspruch bleibt. Ein bloßer Verweis auf eine Webseite genügt dafür nicht; Abschnitt 4.2 verlangt die konkrete Unterauftragsgenehmigung, Abschnitt 6.2 die anlassbezogene Nachprüfung bei jedem neuen Unterauftragsverarbeiter.

- Die Informationssicherheit meldet, die Daten seien verschlüsselt, weshalb die Kritikalität in Abschnitt 2.3 herabgestuft werden könne. Antwortlinie: Verschlüsselung ist eine Maßnahme nach Art. 32 Abs. 1 Buchst. a DSGVO und ändert die Datenart nicht. Entscheidend ist, wer den Schlüssel hält und ob der Empfänger die Daten für seine Leistung im Klartext benötigt; Abschnitt 4.1 führt die Schlüsselverwaltung deshalb als eigenes Feld, und erst deren Beantwortung rechtfertigt eine niedrigere Einstufung.

- Der Einkauf will einen laufenden Transfer trotz abgelaufener Auflage nicht sperren, weil der Betrieb sonst stillsteht. Antwortlinie: Abschnitt 3.3 kennt neben Freigabe und Sperre ausdrücklich die Zwischenstufe der Freigabe unter Auflagen und den Status der Nachprüfung. Die Fortführung wird deshalb befristet, mit einer benannten verantwortlichen Person nach Abschnitt 3.4 und mit einem Abhilfeplan verbunden; eine unbefristete Duldung dagegen ist die Entscheidung, das Restrisiko dauerhaft zu tragen, und muss dann auch so protokolliert werden.

### Häufige Fehler

- Abschnitt 3.1 wird gepflegt, Abschnitt 6.1 dagegen mit einem pauschalen Jahresdatum gefüllt. Die für die Praxis entscheidenden Auslöser stehen in Abschnitt 6.2, weil sich Listungsstatus, Zielland und Unterauftragnehmerkette zwischen zwei Jahresterminen ändern; ohne Anlassbindung dokumentiert das Register einen Zustand, den es seit Monaten nicht mehr gibt.

- Die Freigabehistorie in Abschnitt 7 wird überschrieben statt fortgeschrieben. Dadurch geht verloren, unter welchen Annahmen die frühere Entscheidung getroffen wurde, und im Gespräch mit der Aufsichtsbehörde lässt sich nicht mehr zeigen, dass auf eine Statusänderung überhaupt reagiert wurde.

- Abschnitt 5.1 verweist auf eine Betroffeneninformation, ohne deren Inhalt am konkreten Transfer zu prüfen. Art. 13 Abs. 1 Buchst. f DSGVO verlangt die Angabe der Absicht der Übermittlung an ein Drittland samt Hinweis auf das Vorliegen oder Fehlen eines Angemessenheitsbeschlusses und auf die geeigneten Garantien; ein allgemeiner Satz über internationale Dienstleister erfüllt das nicht.

- Das Kontrollblatt wird als Anlage in externe Fragebögen oder Datenräume gegeben, obwohl der Warnhinweis der Vorlage es als internes Dokument ausweist. Es enthält Restrisikobewertungen und offene Auflagen; deren Weitergabe schafft eine Beweislage gegen die eigene Organisation und ist bei Mandatsbezug zusätzlich an § 43a Abs. 2 BRAO (Bundesrechtsanwaltsordnung) und § 203 Abs. 1 Nr. 3 StGB zu messen.

## Verwandte Vorlagen

- [SCC-Begleitvereinbarung für Drittlandtransfer](../standardvertragsklauseln-scc-begleitvereinbarung/) — wenn der in Abschnitt 3.1 eingetragene Rechtfertigungsweg über Standardvertragsklauseln tatsächlich vertraglich umgesetzt werden muss.
- [Transfer Impact Assessment für SCC-Drittlandtransfer](../transfer-impact-assessment-scc-dsgvo/) — wenn der in Abschnitt 3.2 verlangte Nachweis zur Rechtslage im Empfängerland erst noch erarbeitet wird.
- [Unterauftragsverarbeiter-Freigabe für Drittlandtransfer](../unterauftragsverarbeiter-drittlandtransfer-freigabe/) — wenn die nach Abschnitt 6.2 auslösende Meldung eines neuen Unterauftragnehmers eine eigene Freigabeentscheidung erfordert.
- [Betroffeneninformation zum Drittlandtransfer](../betroffeneninformation-drittlandtransfer-dsgvo/) — wenn das Datum in Abschnitt 5.1 nicht nur nachgetragen, sondern die Information selbst neu gefasst werden muss.
- [Drittlandtransfer Aussetzung und Abhilfeplan](../drittlandtransfer-aussetzung-abhilfeplan/) — wenn der Status nach Abschnitt 3.3 auf Sperre wechselt und die Rückabwicklung, Datenrückgabe und Ersatzlösung geplant werden.
