# Leitvorlage IT-Outsourcing Risikopaket

Große zweisprachige Leitvorlage für IT-Outsourcing, Cloud, Datenschutz, Exit und Service Levels.

Dateien:

- Die bearbeitbare Markdown-Fassung ist über den sprechend beschrifteten Direktdownload abrufbar.
- Die editierbare ODT-Bürofassung ist über den sprechend beschrifteten Direktdownload abrufbar.
- `rubric.yaml` — automatisierte Mindestprüfung

## Download
- [⬇ Leitvorlage IT Outsourcing Risikopaket – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/leitvorlage-it-outsourcing-risikopaket-zweisprachig/leitvorlage-it-outsourcing-risikopaket-zweisprachig.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Leitvorlage IT Outsourcing Risikopaket – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/leitvorlage-it-outsourcing-risikopaket-zweisprachig/leitvorlage-it-outsourcing-risikopaket-zweisprachig.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`leitvorlage-it-outsourcing-risikopaket-zweisprachig.odt`](leitvorlage-it-outsourcing-risikopaket-zweisprachig.odt) · [`leitvorlage-it-outsourcing-risikopaket-zweisprachig.md`](leitvorlage-it-outsourcing-risikopaket-zweisprachig.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage dient einem IT-Vertrag mit Projekt-, Betriebs-, Lizenz-, Support-, Cloud-, API- oder Exit-Bezug. Sie passt, wenn technische Leistung, Service Level, Mitwirkung, Abnahme, Mängel, Sicherheit, Datenschutz und Exit konkret verhandelt werden.

## Einschlägige Normen

- §§ 631, 640 BGB für werkvertragliche Projekt-, Migrations-, Entwicklungs- und Abnahmepflichten.
- §§ 611, 611a, 675 BGB, wenn Beratung, Betrieb, Support oder laufende Dienste im Vordergrund stehen.
- §§ 327 ff. BGB bei digitalen Produkten gegenüber Verbrauchern; bei B2B als Prüfanker für Update-, Bereitstellungs- und Mängelmechanik.
- §§ 280, 281, 286, 307 BGB zu Pflichtverletzung, Nacherfüllung, Verzug und AGB-Kontrolle.
- Art. 28, Art. 32, Art. 33 DSGVO, wenn Betrieb, Hosting, Support oder Migration personenbezogene Daten betrifft.

## Hinweise zur Verwendung

IT-Verträge müssen Leistungsgegenstand, Servicegrenze, Mitwirkung, Change Request, Abnahme, Betrieb, Mängel, Datenexport, Exit und Sicherheit voneinander trennen. Pauschale Verfügbarkeits- oder Projektformulierungen tragen nicht, wenn Provider, Kunde, Unterauftragnehmer und Cloudplattform unterschiedliche Pflichten haben.

Fristen- und Beweisarchitektur: Meilenstein, Sprint, Abnahme, Incident-Reaktionszeit, Wiederherstellungszeit, Wartungsfenster, Exit-Start, Datenrückgabe und Löschung werden mit Messpunkt, Eskalation und Rechtsfolge geführt. Bei personenbezogenen Daten wird parallel ein AVV nach `informationstechnologierecht/auftragsverarbeitungsvertrag-dsgvo/` oder eine eigene Verantwortlichkeitsregel genutzt.

Abgrenzung: Für SaaS `informationstechnologierecht/software-as-a-service-vertrag/`; für agile Entwicklung `informationstechnologierecht/software-entwicklungsvertrag-agil/`; für Outsourcing und Exit `informationstechnologierecht/it-outsourcing-transition-vertrag/`.

## Taktische Hinweise

### Vorgehensreihenfolge

1. Zuerst werden Systemscope und Kritikalität nach Abschnitt 1 festgeschrieben, weil diese Zeile über das anwendbare Regime entscheidet. Ob die Leistung als normal, kritisch oder als Leistung für kritische Infrastrukturen (KRITIS) eingestuft wird und ob der Auftraggeber ein beaufsichtigtes Unternehmen nach Abschnitt 9 ist, bestimmt Nachweis-, Anzeige- und Kündigungspflichten im ganzen Vertragswerk. Unmittelbar danach wird die Rangfolge des Abschnitts 2 korrigiert: Sie stellt den Rahmenvertrag über den Auftragsverarbeitungsvertrag der Anlage 3, sodass allgemeine Vertragsklauseln die Weisungsbindung nach Art. 28 Abs. 3 Buchst. a DSGVO verdrängen könnten. Für datenschutzrechtliche Fragen ist deshalb ein ausdrücklicher Vorrang der Anlage 3 zu vereinbaren.

2. Danach wird die Messbarkeit der Leistung hergestellt. Abschnitt 5 verlangt Leistungsscheine je Servicebaustein mit Übergabepunkt als Messpunkt, Messmethode und Teilausfallregel; erst dann trägt die Verfügbarkeitsformel. Zusammengeführt werden dabei die Malus-Staffel und die Monatskappung aus Abschnitt 5, die Sonderkündigung wegen wiederholter Unterschreitung aus der Risikomatrix in Abschnitt 3 und die Klarstellung in Abschnitt 12, ob die Service Credits auf weitergehenden Schadensersatz angerechnet werden oder ihn unberührt lassen. Bleibt dieses Verhältnis offen, wirkt der Malus im Streit als abschließende Pauschalierung.

3. Erst dann wird die Verarbeitungskette geschlossen. Abschnitt 6 setzt die Pflichtinhalte des Art. 28 Abs. 3 Satz 2 Buchst. a bis h DSGVO um und ergänzt die Hinweispflicht bei rechtswidrigen Weisungen nach Art. 28 Abs. 3 Satz 3 DSGVO; Abschnitt 7 führt die Genehmigung weiterer Auftragsverarbeiter nach Art. 28 Abs. 2 DSGVO und die Pflichtenweitergabe nach Art. 28 Abs. 4 DSGVO. Zu prüfen sind je Verarbeitungsort das Übermittlungsinstrument nach Kapitel V der DSGVO und die Bewertung des Ziellandrechts; die Unterauftragnehmerliste der Anlage 5 wird zum führenden Dokument, weil ohne sie weder Widerspruch noch Audit steuerbar sind.

4. Anschließend wird der Exit gebaut, bevor über Preise gesprochen wird. Abschnitt 4 schuldet Migrationsunterstützung, Herausgabe in dokumentierten Offenformaten und Löschung nach abgeschlossener Migration; die Nachweiszeile der Risikomatrix in Abschnitt 3 verlangt zusätzlich einen Testlauf vor Vertragsende, und genau dieser Testlauf ist die einzige belastbare Kontrolle gegen Vendor-Lock-in. Als Rechercheanker tritt Kapitel VI der Verordnung (EU) 2023/2854 (Datenverordnung, Data Act) über den Wechsel zwischen Datenverarbeitungsdiensten hinzu; ob und mit welchen Höchstfristen und Gebührengrenzen es den konkreten Dienst erfasst, ist vor der Zeichnung live zu prüfen (Suchanker: „Data Act Wechsel Datenverarbeitungsdienste Kündigungsfrist Übergangsfrist Wechselgebühren").

5. Zuletzt werden Haftung, Versicherung und Personalübergang zusammengerechnet. Die Kappungen des Abschnitts 12 werden gegen die Deckungssummen der IT-Haftpflicht- und Cyber-Versicherung gespiegelt, damit keine Lücke zwischen Haftungszusage und Deckung bleibt, und der Katalog der ausgenommenen Pflichtverletzungen wird ausgefüllt. Parallel wird die Prüfung des Betriebsübergangs nach § 613a Abs. 1 Satz 1 BGB nach Abschnitt 13 nicht nur für den Vertragsbeginn, sondern auch für die Rückführung an den Auftraggeber oder einen Folgedienstleister terminiert, weil die Unterrichtung in Textform nach § 613a Abs. 5 BGB und die Monatsfrist des Widerspruchsrechts nach § 613a Abs. 6 BGB Vorlauf brauchen.

### Typische Gegnereinwände mit Antwortlinie

- Der Auftragnehmer verweigert das Vor-Ort-Audit und verweist auf seine Zertifizierung nach ISO/IEC 27001. Antwortlinie: Abschnitt 8 lässt die Ersetzung nur zu, wenn der Geltungsbereich die vertragsgegenständlichen Leistungen und Standorte vollständig abdeckt; verlangt werden daher Zertifikat, Geltungsbereichsdokument und Auditbericht, nicht die Urkunde allein. Unabhängig davon bleibt die Nachweispflicht nach Art. 28 Abs. 3 Satz 2 Buchst. h DSGVO beim Auftragnehmer, und bei Abdeckungslücken oder konkreten Sicherheitsvorfällen lebt das volle Auditrecht nach Abschnitt 8 wieder auf.

- Der Auftragnehmer setzt ein Konzernunternehmen ein und meint, darin liege keine Weitervergabe. Antwortlinie: Abschnitt 7 stellt konzernangehörige Unternehmen ausdrücklich den Unterauftragnehmern gleich. Datenschutzrechtlich ist jede Verarbeitung durch eine andere juristische Person ein weiteres Auftragsverarbeitungsverhältnis, das die Genehmigung nach Art. 28 Abs. 2 DSGVO, die Pflichtenweitergabe nach Art. 28 Abs. 4 DSGVO und den Eintrag in die Liste der Anlage 5 erfordert.

- Der Auftragnehmer bestreitet die Unterschreitung der Verfügbarkeit und legt eigene Zahlen vor. Antwortlinie: Abschnitt 5 gibt dem Auftraggeber den Zugang zu den Rohdaten und das Recht, das Messsystem selbst oder durch Dritte überprüfen zu lassen. Nachgerechnet wird anhand von Messpunkt, Messmethode, angekündigtem Wartungsfenster und Teilausfallregel des jeweiligen Leistungsscheins; fehlen diese Angaben, ist nicht die Messung streitig, sondern die Zusage unbestimmt.

- Der Auftragnehmer verzögert am Vertragsende den Datenexport und beruft sich auf offene Vergütung. Antwortlinie: Abschnitt 4 schuldet die Herausgabe in dokumentierten Offenformaten gegen Vergütung nach dem Preisblatt der Anlage 8; die Pflicht zur Rückgabe oder Löschung nach Art. 28 Abs. 3 Satz 2 Buchst. g DSGVO steht nicht unter dem Vorbehalt eines Vergütungsstreits. Abgesichert wird das durch einen ausdrücklichen Ausschluss von Zurückbehaltungsrechten an Daten, eine hinterlegte Exitvergütung und den Migrationstestlauf aus Abschnitt 3.

### Häufige Fehler

- Die Meldefristen laufen doppelt. Die Risikomatrix in Abschnitt 3 verlangt eine Meldung des Auftragnehmers binnen 24 Stunden, Abschnitt 6 dagegen eine unverzügliche Meldung nach Art. 33 Abs. 2 DSGVO. Da dem Auftraggeber für seine eigene Meldung nach Art. 33 Abs. 1 DSGVO nur 72 Stunden ab Kenntnis bleiben, muss eine der beiden Fristen weichen oder als vertragliche Höchstfrist innerhalb der unverzüglichen Meldung ausgestaltet werden.

- Die Haftungskappung des Abschnitts 12 nimmt Vorsatz und Personenschäden aus, nicht aber die grobe Fahrlässigkeit. In vorformulierten Bedingungen ist eine solche Kappung an § 307 Abs. 1 Satz 1 und Abs. 2 Nummer 2 BGB zu messen, wobei § 309 Nummer 7 Buchst. a und b BGB über § 310 Abs. 1 Satz 2 BGB in die Prüfung hineinwirkt. Zudem begrenzt kein Haftungsdeckel den Anspruch betroffener Personen nach Art. 82 Abs. 1 DSGVO; im Verhältnis der Parteien bleibt nur der Innenausgleich nach Art. 82 Abs. 5 DSGVO.

- Abschnitt 4 lässt alle verbleibenden Daten 30 Tage nach der Migration löschen, ohne gesetzliche Aufbewahrungspflichten auszunehmen. Buchführungs- und Belegunterlagen können nach § 257 Abs. 1 HGB und § 147 Abs. 1 der Abgabenordnung (AO) länger vorzuhalten sein; der Auftragnehmer braucht für die Erfüllung eigener Pflichten eine benannte Ausnahme mit Zweckbindung und Zugriffssperre statt einer pauschalen Löschzusage.

- Beim Ausfüllen wird nur die deutsche Spalte bearbeitet, sodass Platzhalter, Fristen und Beträge in der englischen Spalte abweichen. Die Vorrangregel am Ende des Abschnitts 13 verdeckt diesen Widerspruch nur; zudem steht sie als letzte Zeile im Abschnitt zum Personalübergang und gehört in eine eigene Schlussbestimmung, damit sie nicht als Regel allein für Abschnitt 13 gelesen wird. Live-Rechercheanker: „Betriebsübergang § 613a BGB Outsourcing Unterrichtung fehlerhaft Widerspruchsfrist" und „BaFin Auslagerung Cloud Anbieter Prüfungsrechte aktuelle Fassung".

## Verwandte Vorlagen

- [IT-Outsourcing-Transition-Vertrag](../it-outsourcing-transition-vertrag/) — für den Vollzug des Übergangs, den diese Leitvorlage nur als Exit-Plan der Anlage 6 benennt.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — für die Ausformulierung der Service-Level-Anlage 2 mit Staffel, Reaktionszeiten und Berichtspflicht.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — für die Anlage 3, auf die Abschnitt 6 die gesamte Verarbeitungskette stützt.
- [Anlage TOM zum Auftragsverarbeitungsvertrag](../avv-tom-anlage-dsgvo/) — für die technischen und organisatorischen Maßnahmen der Anlage 4, die Abschnitt 6 nur voraussetzt.
- [Quellcode-Herausgabe- und Datenexport-Notfallplan](../quellcode-herausgabe-und-datenexport-notfallplan/) — wenn der Exit nicht geordnet abläuft, sondern im Störfall gegen einen unwilligen Anbieter durchgesetzt werden muss.
