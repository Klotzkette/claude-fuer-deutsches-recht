# API-Nutzungsvertrag B2B

API-Nutzungsvertrag mit Zugriffsschlüsseln, Nutzungsgrenzen, Verfügbarkeit, Datenverantwortung, Sicherheit und Sperrrechten.

## Download
- [⬇ API Nutzungsvertrag B2B – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/api-nutzungsvertrag-b2b/api-nutzungsvertrag-b2b.odt) — Offene Bürofassung (OpenDocument)
- [⬇ API Nutzungsvertrag B2B – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/api-nutzungsvertrag-b2b/api-nutzungsvertrag-b2b.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`api-nutzungsvertrag-b2b.odt`](api-nutzungsvertrag-b2b.odt) · [`api-nutzungsvertrag-b2b.md`](api-nutzungsvertrag-b2b.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

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

## Typische Fallstricke

- Unklare Rollen, fehlende Vollmachten oder widersprüchliche Anlagen machen die spätere Durchsetzung unnötig schwer.
- Pauschale Haftungs-, Kosten- oder Leistungsformulierungen müssen durch prüfbare Schwellen, Fristen und Nachweise ersetzt werden.
- Bei grenzüberschreitenden oder regulierten Sachverhalten sind zwingende Rechtswahl-, Sanktions-, Datenschutz-, Steuer- und Meldepflichten gesondert zu prüfen.

## Taktische Hinweise

### Vorgehensreihenfolge beim Entwurf

1. Zuerst wird die Rechtsnatur des Schnittstellenzugangs festgelegt, weil davon die Mängelrechte der Nutzerin abhängen. Wird die Programmierschnittstelle nach Abschnitt 2.1 dauerhaft zum Gebrauch bereitgestellt und nach Abschnitt 7.1 laufend vergütet, liegt eine Gebrauchsüberlassung nach §§ 535 ff. BGB nahe; steht dagegen die fachliche Auswertung jeder einzelnen Anfrage im Vordergrund, spricht das für einen Dienstvertrag nach § 611 BGB. Die Folge ist erheblich, denn bei mietrechtlicher Einordnung mindert sich das Entgelt nach § 536 Abs. 1 BGB kraft Gesetzes und ohne Rüge, und § 536a Abs. 1 BGB begründet für Anfangsmängel eine verschuldensunabhängige Haftung, die Abschnitt 8 in der vorliegenden Fassung nicht auffängt. Live-Rechercheanker: „BGH Rechtsnatur Softwareüberlassung über Internet Mietvertrag § 535 BGB“.

2. Danach wird die Verfügbarkeit messbar gemacht, denn der Entwurf enthält mit Abschnitt 4 nur Regeln zur Versionierung und zur Abkündigung veralteter Endpunkte sowie mit Anlage 2 die Rate Limits, aber keine Verfügbarkeitszusage. In Anlage 1 sind je Endpunkt der Messpunkt am Gateway, das Messintervall, die zulässige Antwortzeit, die Behandlung angekündigter Wartungsfenster und die Zurechnung von Ausfällen des Identity-Providers festzulegen; der Malus wird als Gutschrift auf das Grundentgelt nach Abschnitt 7.1 ausgestaltet und im Verhältnis zur gesetzlichen Minderung ausdrücklich als abschließend oder als zusätzlich bezeichnet.

3. Erst dann werden die Nutzungsgrenzen des Abschnitts 3.3 an das zwingende Softwarerecht angepasst. Werden der Nutzerin Client-Bibliotheken, ein Software-Development-Kit oder Schemadateien zur Installation überlassen, bleiben das Beobachten, Untersuchen und Testen zur Ermittlung der Ideen und Grundsätze nach § 69d Abs. 3 des Urheberrechtsgesetzes (UrhG) sowie die Dekompilierung zur Herstellung der Interoperabilität nach § 69e Abs. 1 UrhG erlaubt; nach § 69g Abs. 2 UrhG ist eine entgegenstehende Vertragsbestimmung nichtig. Das Verbot ist deshalb auf das Umgehen technischer Schutzmaßnahmen, das Weitergeben von Zugangsschlüsseln und das systematische Auslesen ganzer Datenbestände zuzuspitzen.

4. Anschließend wird die datenschutzrechtliche Rolle bestimmt, die Abschnitt 5.1 bewusst offenlässt. Ruft die Nutzerin über die Schnittstelle personenbezogene Daten für eigene Zwecke ab, sind beide Parteien getrennt Verantwortliche im Sinne des Art. 4 Nr. 7 der Datenschutz-Grundverordnung (DSGVO); verarbeitet die Anbieterin die von der Nutzerin eingespeisten Daten allein nach deren Weisung, gilt Art. 28 DSGVO mit den Pflichtinhalten des Art. 28 Abs. 3 DSGVO, der Genehmigung weiterer Auftragsverarbeiter nach Art. 28 Abs. 2 DSGVO, der Weitergabe derselben Pflichten nach Art. 28 Abs. 4 DSGVO und der Meldung an die Nutzerin unverzüglich nach Art. 33 Abs. 2 DSGVO, damit diese die Frist von 72 Stunden aus Art. 33 Abs. 1 DSGVO halten kann. Die Schlüsselverwaltung nach Abschnitt 2.2 und die Protokollierung nach Abschnitt 2.3 sind als Maßnahmen nach Art. 32 Abs. 1 DSGVO zu beschreiben, nicht als bloße Ordnungspflicht.

5. Zuletzt werden Abrechnung, Sperre und Exit zusammen gelesen. Die Messdatenregel des Abschnitts 7.2 darf nur eine widerlegliche Vermutung begründen und die Rügefrist nicht als Ausschlussfrist wirken, weil sonst § 309 Nr. 12 BGB und § 307 Abs. 1 BGB eingreifen; Entgeltänderungen brauchen einen benannten Anpassungsmaßstab und ein Kündigungsrecht, sonst scheitern sie an § 307 Abs. 1 Satz 2 BGB und § 308 Nr. 4 BGB. Der Entwurf regelt außerdem keinen Datenexport: Zu ergänzen sind Format, Frist und Kostentragung für die Herausgabe der über die Schnittstelle übermittelten Bestände, ein Weiterbetrieb während der Migrationsfrist des Abschnitts 4.2 und ein Löschnachweis nach Vertragsende. Live-Rechercheanker: „BGH Preisanpassungsklausel Dauerschuldverhältnis Transparenz § 307 BGB“.

### Typische Einwände der Gegenseite und Antwortlinien

- Die Nutzerin wendet ein, die Schnittstelle sei über Tage unbrauchbar gewesen, weshalb sie das Entgelt kürze. Antwortlinie: Zunächst wird die Rechtsnatur geklärt, weil die Minderung nach § 536 Abs. 1 BGB nur bei Gebrauchsüberlassung kraft Gesetzes eintritt; sodann wird anhand der Messreihe aus Anlage 1 und der Protokolle nach Abschnitt 2.3 geprüft, ob der Ausfall am vereinbarten Messpunkt lag, ob er auf ein angekündigtes Wartungsfenster nach Abschnitt 4.1 zurückgeht und ob nicht die Nutzerin durch Überschreiten der Rate Limits aus Anlage 2 die Drosselung selbst ausgelöst hat.
- Die Nutzerin wendet ein, die Abschaltung eines Endpunkts sei zu kurzfristig erfolgt, und verlangt den Anpassungsaufwand ersetzt. Antwortlinie: Abschnitt 4.2 verlangt Ankündigung mit Migrationsfrist, Testumgebung und technischer Dokumentation und nimmt nur die sicherheitsbedingte Sofortmaßnahme aus; belegt werden der Zugang der Ankündigung bei dem technischen Ansprechpartner nach Abschnitt 2.1, die Bereitstellung der Sandbox und die Verletzung der eigenen Anpassungs- und Meldepflicht der Nutzerin aus Abschnitt 4.3.
- Die Nutzerin wendet ein, die Sperre nach Abschnitt 6.2 sei unberechtigt gewesen. Antwortlinie: Die Sperre ist nach Abschnitt 6.3 zu begründen und zu dokumentieren und mit dem Wegfall des Grundes aufzuheben; getragen wird sie durch den Nachweis eines Verstoßes gegen Abschnitt 3.1 oder Abschnitt 3.3 aus dem Monitoring nach Abschnitt 6.1, wobei die mildeste wirksame Maßnahme zu wählen ist, also die Sperre eines einzelnen Schlüssels oder Endpunkts statt des Gesamtzugangs.
- Die Nutzerin wendet ein, sie hafte nicht für die Auswertung der abgerufenen Daten, weil die Anbieterin die Datenquelle betreibe. Antwortlinie: Abschnitt 5.1 belässt jeder Partei die Verantwortung für die von ihr bereitgestellten Daten, und Abschnitt 5.3 verbietet die Verwendung der Antworten als alleinige Entscheidungsgrundlage; bei automatisierten Einzelfallentscheidungen mit erheblicher Wirkung für Betroffene trifft die Nutzerin zusätzlich die Pflicht aus Art. 22 Abs. 3 DSGVO, eine menschliche Prüfung sicherzustellen.

### Häufige Fehler

- Abschnitt 8 wird für eine Haftungsbegrenzung gehalten. Er enthält nur Zurechnungs- und Freistellungsregeln, aber keine Grenze nach Betrag, Vorhersehbarkeit oder Schadensart; ohne eine Regelung zu Datenverlust, Wiederherstellungsaufwand und mittelbaren Schäden, die die Grenzen des § 307 Abs. 2 Nr. 2 BGB beachtet, bleibt die Haftung offen, obwohl die Vergütung nach Abschnitt 7 sie nicht abdeckt.
- Das Verbot des Reverse Engineering in Abschnitt 3.3 wird pauschal übernommen. Soweit überlassene Client-Bibliotheken betroffen sind, ist die Klausel wegen § 69g Abs. 2 UrhG in Bezug auf die nach §§ 69d Abs. 3, 69e Abs. 1 UrhG erlaubten Handlungen nichtig, und die Nichtigkeit einer zu weit gefassten Kernklausel schwächt die gesamte Nutzungsordnung.
- Anlage 3 wird als Auftragsverarbeitungsvertrag beigefügt, obwohl die Nutzerin die abgerufenen Daten für eigene Zwecke verwendet. Damit werden die Rollen falsch abgebildet, und die Weisungsfiktion des Art. 28 Abs. 10 DSGVO kann die Nutzerin zur Verantwortlichen machen, ohne dass die Informations- und Rechtsgrundlagenpflichten in ihrem eigenen Verhältnis zu den Betroffenen abgesichert sind.
- Der Exit bleibt ungeregelt. Da die Anbieterin nach Abschnitt 6.2 sperren und nach Abschnitt 4.1 abschalten darf, steht die Nutzerin ohne Herausgabe-, Format- und Fristenregelung nach Vertragsende ohne ihre Bestände da, während die Anbieterin ohne Löschnachweis ihre eigene Löschpflicht nicht belegen kann.

## Verwandte Vorlagen

- [Software-as-a-Service-Vertrag (B2B; SLA)](../software-as-a-service-vertrag/) — für die vollständige Anwendungsnutzung durch Endnutzer statt des reinen Maschinenzugriffs über die Schnittstelle.
- [Platform-as-a-Service-Vertrag B2B](../platform-as-a-service-b2b-vertrag/) — wenn die Nutzerin nicht nur Endpunkte abruft, sondern eigene Anwendungen auf der Plattform der Anbieterin betreibt.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — für die Verfügbarkeits-, Reaktions- und Wiederherstellungswerte, die Anlage 1 dieses Vertrags nur benennt.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — wenn die Anbieterin die eingespeisten Daten weisungsgebunden verarbeitet und Anlage 3 die Pflichtinhalte tragen muss.
- [B2B-Datenverarbeitungs- und Datenlizenzvertrag](../datenverarbeitungs-und-datenlizenzvertrag-b2b/) — wenn nicht der technische Zugang, sondern die Rechteeinräumung an den abgerufenen Datenbeständen der Kern des Geschäfts ist.
