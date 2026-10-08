# IT-Outsourcing-Transition-Vertrag

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

1. Vor Vertragsabschluss werden Ausgangsbetrieb, Assets, Lizenzen, Personalabhängigkeiten, Datenbestände, Drittverträge und technische Schulden in einem abgestimmten Übergabeinventar erfasst. Für jedes Objekt werden Eigentümer, Übertragbarkeit, erforderliche Zustimmung und Übergabekriterium festgelegt.
2. Danach werden Transition-Wellen, Parallelbetrieb, Meilensteine, Abnahmekriterien und Vergütungsfolgen miteinander verzahnt. Kritische Dienste erhalten einen Rückfallplan und einen benannten Entscheider für Go-live, Abbruch oder Wiederholung.
3. Vor jeder Übergabewelle werden Zugänge, Datenschutzrollen, Sicherheitsfreigaben und Betriebsnachweise geprüft. Am Ende sichern Exit-Test, Datenexport und Löschprotokoll die spätere Rückübertragbarkeit unabhängig vom Provider.

### Typische Gegnereinwände mit Antwortlinie

- Der Provider macht Verzögerungen von unzureichender Mitwirkung des Kunden abhängig. Die Antwortlinie verlangt eine konkrete Mitwirkungsanforderung, rechtzeitige Eskalation und den nachgewiesenen Einfluss auf den kritischen Pfad.
- Der Kunde beanstandet, der Meilenstein sei trotz technischer Inbetriebnahme nicht abnahmefähig. Die Antwortlinie trennt Betriebsaufnahme, vereinbarte Abnahmekriterien und verbleibende Mängel nach ihrer tatsächlichen Auswirkung.
- Ein Drittanbieter verweigert Lizenz- oder Vertragsübertragung. Die Antwortlinie ordnet Zustimmung, Ersatzbeschaffung, Übergangslizenz und Kostenfolge bereits dem betroffenen Asset zu.

### Häufige Fehler

- Transition und späterer Regelbetrieb verwenden unterschiedliche Service-, Sicherheits- oder Eskalationsbegriffe.
- Ein Parallelbetrieb wird vereinbart, ohne Datenführerschaft, Synchronisation und Abschaltentscheidung festzulegen.
- Der Exit nennt weder Exportformat noch Übergabezeit, Unterstützungspflicht und Löschbestätigung.

## Verwandte Vorlagen

- [Quellcode-Herausgabe- und Datenexport-Notfallplan](../quellcode-herausgabe-und-datenexport-notfallplan/) — operationalisiert die Herausgabe, wenn Transition oder Exit unter Zeitdruck scheitern.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — regelt messbare Betriebsqualität nach erfolgreicher Transition.
- [Software-as-a-Service-Vertrag (B2B; SLA)](../software-as-a-service-vertrag/) — eignet sich für den anschließenden standardisierten Cloudbetrieb ohne umfassende Übernahmephase.
- [Leitvorlage IT-Outsourcing Risikopaket](../leitvorlage-it-outsourcing-risikopaket-zweisprachig/) — bündelt Risiko-, Kontroll- und Governance-Dokumentation für komplexe Outsourcingvorhaben.

## Download

- [⬇ IT Outsourcing Transition Vertrag – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/it-outsourcing-transition-vertrag/it-outsourcing-transition-vertrag.md.zip)
- [⬇ IT Outsourcing Transition Vertrag – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/it-outsourcing-transition-vertrag/it-outsourcing-transition-vertrag.odt)

Vorschau im Repository: [`it-outsourcing-transition-vertrag.odt`](it-outsourcing-transition-vertrag.odt) · [`it-outsourcing-transition-vertrag.md`](it-outsourcing-transition-vertrag.md)
