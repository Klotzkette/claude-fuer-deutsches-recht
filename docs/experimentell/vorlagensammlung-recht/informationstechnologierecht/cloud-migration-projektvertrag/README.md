# Cloud-Migration-Projektvertrag

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

## Besondere Warnhinweise

Cloud-Migration ist Ausfall-, Datenschutz- und Vendor-Lock-in-riskant. Cutover, Rollback, Backups, Zugriffe und Exit müssen testbar geregelt werden.

## Download

- [⬇ Cloud Migration Projektvertrag – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/cloud-migration-projektvertrag/cloud-migration-projektvertrag.md.zip)
- [⬇ Cloud Migration Projektvertrag – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/cloud-migration-projektvertrag/cloud-migration-projektvertrag.odt)

Vorschau im Repository: [`cloud-migration-projektvertrag.odt`](cloud-migration-projektvertrag.odt) · [`cloud-migration-projektvertrag.md`](cloud-migration-projektvertrag.md)

## Hinweise zur Verwendung

IT-Verträge müssen Leistungsgegenstand, Servicegrenze, Mitwirkung, Change Request, Abnahme, Betrieb, Mängel, Datenexport, Exit und Sicherheit voneinander trennen. Pauschale Verfügbarkeits- oder Projektformulierungen tragen nicht, wenn Provider, Kunde, Unterauftragnehmer und Cloudplattform unterschiedliche Pflichten haben.

Fristen- und Beweisarchitektur: Meilenstein, Sprint, Abnahme, Incident-Reaktionszeit, Wiederherstellungszeit, Wartungsfenster, Exit-Start, Datenrückgabe und Löschung werden mit Messpunkt, Eskalation und Rechtsfolge geführt. Bei personenbezogenen Daten wird parallel ein AVV nach `informationstechnologierecht/auftragsverarbeitungsvertrag-dsgvo/` oder eine eigene Verantwortlichkeitsregel genutzt.

Abgrenzung: Für SaaS `informationstechnologierecht/software-as-a-service-vertrag/`; für agile Entwicklung `informationstechnologierecht/software-entwicklungsvertrag-agil/`; für Outsourcing und Exit `informationstechnologierecht/it-outsourcing-transition-vertrag/`.

## Taktische Hinweise

### Vorgehensreihenfolge beim Entwurf

1. Zuerst wird der Erfolg beschrieben, den die Migration schuldet, weil davon Abnahme, Verjährung und Vergütung abhängen. Die Überführung eines bestehenden Bestands in eine Zielarchitektur nach Abschnitt 2.1 ist ein werkvertraglich geschuldeter Erfolg nach § 631 Abs. 1 BGB; Beratung außerhalb der Migrationsschnittstellen und der Dauerbetrieb nach Abschnitt 2.2 sind es nicht. In Anlage 1 werden deshalb je Quellsystem die Zielwerte für Datenvollständigkeit, Schnittstellenfunktion, Berechtigungsgleichheit und Antwortzeit so festgeschrieben, dass ein bestandener Funktionstest nach Anlage 4 Ziffer 1.1 die Erfolgserreichung tatsächlich belegt.

2. Danach werden die Mitwirkungspflichten der Kundin aus Abschnitt 3 rechtlich einsortiert. Wird die Bereitstellung von Systeminformationen, Testnutzern und Fachfreigaben nur als Obliegenheit ausgestaltet, führt ihre Verletzung nach § 642 Abs. 1 BGB zu einer Entschädigung für die Wartezeit und nach § 643 BGB zur Kündigungsmöglichkeit der Dienstleisterin, aber nicht zu Schadensersatz; sollen daneben Schadensersatzansprüche entstehen, muss Abschnitt 3.1 die Bereitstellung ausdrücklich als vertragliche Pflicht bezeichnen. Für Schäden aus fehlerhaften Vorgaben der Kundin ist zusätzlich § 645 Abs. 1 BGB als Anker zu prüfen, weil er den Vergütungsanspruch bei Untergang oder Verschlechterung infolge einer Anweisung des Bestellers erhält.

3. Erst dann wird die Abnahmemechanik gebaut, denn Abschnitt 2.4.4 und Anlage 4 nennen den Funktionstest, ohne die Rechtsfolgen zu ordnen. Zu regeln sind Teilabnahmen für die in Anlage 5 Ziffer 1.2 vorgesehenen Meilensteine, die Fristsetzung mit der Wirkung des § 640 Abs. 2 Satz 1 BGB, wonach das Werk als abgenommen gilt, wenn die Kundin die Abnahme nicht innerhalb einer angemessenen Frist unter Angabe mindestens eines Mangels verweigert, und der Vorbehalt bekannter Mängel nach § 640 Abs. 3 BGB. Weil die Verjährung der Mängelrechte nach § 634a Abs. 1 Nr. 3 und Abs. 2 BGB mit der Abnahme beginnt, ist außerdem festzuhalten, welches Dokument die Abnahme trägt: das Testprotokoll, die Cutover-Freigabe oder das Betriebshandover.

4. Anschließend wird die Verantwortung für die Daten selbst getrennt. Abschnitt 6.4 verlangt zu Recht mehr als einen technischen Import, doch die Beweisführung entsteht erst durch die Sicherung vor dem Cutover, den dokumentierten Stichprobenabgleich und den Wiederherstellungstest aus Anlage 4 Ziffer 1.1. Soweit personenbezogene Daten migriert werden, ist die Dienstleisterin Auftragsverarbeiterin, sodass die Pflichtinhalte des Art. 28 Abs. 3 der Datenschutz-Grundverordnung (DSGVO) einzeln in Anlage 3 abzubilden sind, die Migrationswerkzeuge und Betriebsstandorte der Zustimmungsmechanik des Art. 28 Abs. 2 DSGVO unterliegen, die Weitergabe derselben Pflichten an Unterauftragnehmer nach Art. 28 Abs. 4 DSGVO erfolgt und die Meldung eines Vorfalls nach Art. 33 Abs. 2 DSGVO unverzüglich an die Kundin geht, damit diese die Frist von 72 Stunden aus Art. 33 Abs. 1 DSGVO halten kann. Für Zielregionen außerhalb der Union greift die Prüfreihenfolge aus Art. 45 Abs. 1, Art. 46 Abs. 2 Buchst. c und Art. 49 Abs. 1 DSGVO, die Anlage 3 Ziffer 2.2 mit dem Transfer Impact Assessment (TIA), also der Bewertung der Rechtslage im Zielland, verknüpft.

5. Danach wird geprüft, ob die Migration Personal berührt. Übernimmt die Dienstleisterin mit dem Betriebshandover auch die Betriebsmannschaft, das Rechenzentrum oder eine abgrenzbare Betriebsfunktion, kann ein Betriebsteilübergang nach § 613a Abs. 1 Satz 1 BGB eintreten mit der Folge, dass Arbeitsverhältnisse übergehen, die Unterrichtung nach § 613a Abs. 5 BGB geschuldet ist und das Widerspruchsrecht nach § 613a Abs. 6 BGB die Personalplanung verändert. Diese Frage ist vor der Zeichnung zu klären, weil sie die Vergütung nach Anlage 5 und die Hypercare-Phase nach Abschnitt 8.1 verschiebt.

6. Zuletzt wird der Rückweg geregelt. Abschnitt 8.3 nennt den exportfähigen Datenstand, doch die Rückabwicklung trägt erst, wenn der Rollback-Punkt aus Anlage 2 mit einer Zeitgrenze versehen ist, der Leistungsstand bei Kündigung aus wichtigem Grund gemeinsam festgestellt wird, wie es § 648a Abs. 4 BGB vorsieht, und die freie Kündigung der Kundin nach § 648 BGB mit ihrer Vergütungsfolge ausdrücklich vom Fall der berechtigten Kündigung getrennt wird. Der Exit-Test aus Anlage 4 Ziffer 3.2 wird terminiert, sonst bleibt der Ausstieg eine Absichtserklärung. Live-Rechercheanker: „BGH IT-Projekt Abnahme Werkvertrag Kündigung Teilleistung Abrechnung“.

### Typische Einwände der Gegenseite und Antwortlinien

- Die Kundin verweigert die Abnahme, weil die Restmängelliste noch offen ist. Antwortlinie: Nach § 640 Abs. 1 BGB besteht die Abnahmepflicht bereits, wenn nur unwesentliche Mängel verbleiben, und Anlage 4 Ziffer 1.2 lässt Abnahmehindernisse nur bei wesentlicher Beeinträchtigung von produktiver Nutzung, Datenintegrität, Sicherheit oder vereinbarten Kernprozessen zu. Vorgelegt werden das Testprotokoll mit Fehlerklassen, die Zuordnung der Restmängel nach Anlage 4 Ziffer 2.2 zu Schweregrad und Workaround und die Fristsetzung, die die Wirkung des § 640 Abs. 2 Satz 1 BGB auslöst.
- Die Dienstleisterin verlangt Mehrvergütung, weil Freigaben und Testnutzer verspätet gekommen seien. Antwortlinie: Ohne Freigabe in Textform nach Anlage 5 Ziffer 2.2 ist Zusatzaufwand nicht abrechenbar; als Anspruchsgrundlage bleibt allein die Entschädigung nach § 642 BGB, die eine konkrete, aus dem Cutover-Kalender belegte Wartezeit voraussetzt und keinen entgangenen Gewinn umfasst. Gegengehalten wird zudem die eigene Prüf- und Rügepflicht der Dienstleisterin aus Abschnitt 4.2, deren Verletzung bei erkennbaren Migrationssperren nach § 254 Abs. 1 BGB anzurechnen ist.
- Die Kundin macht einen Datenverlust im Cutover-Fenster geltend. Antwortlinie: Zunächst wird der Maßstab des Abschnitts 6.4 angelegt, also der Abgleich von Datenbestand, Berechtigungen, Metadaten und Stichproben mit der Fachbereichsfreigabe; sodann wird geprüft, ob die Abweichung auf offengelegte Altlasten oder Dateninkonsistenzen zurückgeht, für die Abschnitt 3.3 die Verantwortung der Kundin festhält, und ob während des freigegebenen Fensters produktive Änderungen erfolgt sind, die Abschnitt 6.1 ausdrücklich der Auftraggeberin zuweist.
- Die Dienstleisterin beruft sich auf eine Störung beim Cloud-Provider. Antwortlinie: Abschnitt 2.2 nimmt die Provider-Verfügbarkeit außerhalb des vereinbarten Service Levels aus, entlastet aber nicht von Auswahl, Konfiguration und Steuerung; setzt die Dienstleisterin den Provider zur Erfüllung ihrer eigenen Migrationspflichten ein, ist er Erfüllungsgehilfe im Sinne des § 278 Satz 1 BGB, und im Bereich der Auftragsverarbeitung bleibt sie nach Art. 28 Abs. 4 DSGVO für die Pflichten des Unterauftragnehmers verantwortlich.

### Häufige Fehler

- Meilensteinzahlungen werden vereinbart, ohne die Abnahme zu strukturieren. Ohne ausdrückliche Teilabnahmen bleibt offen, wann die Vergütung nach § 641 Abs. 1 BGB fällig wird, wann die Beweislast für Mängel auf die Kundin übergeht und wann die Verjährungsfrist des § 634a Abs. 2 BGB zu laufen beginnt, sodass am Projektende alle Fristen gleichzeitig streitig sind.
- Anlage 3 beschreibt Rollen und Maßnahmen, ersetzt aber keinen Auftragsverarbeitungsvertrag. Fehlen die Pflichtinhalte des Art. 28 Abs. 3 DSGVO im Einzelnen, insbesondere Weisungsbindung, Vertraulichkeit, Unterstützung bei Betroffenenrechten, Löschung oder Rückgabe nach Abschluss und Nachweis- und Prüfrechte, bleibt die Migration ohne wirksame Rechtsgrundlage für die Verarbeitung durch die Dienstleisterin.
- Testmigrationen laufen mit unveränderten Produktivdaten. Abschnitt 7.2 verlangt Anonymisierung oder Minimierung; ohne sie entsteht eine zusätzliche Verarbeitung ohne eigenen Zweck, die Löschung temporärer Extrakte und Transfer-Buckets ist nicht nachweisbar, und bei besonderen Datenkategorien nach Art. 9 Abs. 1 DSGVO fehlt die gesonderte Rechtfertigung.
- Der Exit wird auf Abschnitt 8.3 und Anlage 4 Ziffer 3.1 verkürzt, ohne den Wechsel technisch zu erproben. Bleibt der Exit-Test aus Anlage 4 Ziffer 3.2 unterminiert und das Exportformat unbenannt, verfestigt sich die Bindung an Provider und Werkzeuge, und die Rückabwicklung nach einem gescheiterten Cutover kostet mehr als die Migration selbst.

## Verwandte Vorlagen

- [IT-Outsourcing-Transition-Vertrag](../it-outsourcing-transition-vertrag/) — wenn nicht nur die Umgebung wechselt, sondern der Betrieb dauerhaft auf einen Dienstleister übergeht.
- [IT-Projektvertrag (Werkvertrag, agil/V-Modell XT, Mitwirkungspflichten)](../it-projektvertrag-werkleistung/) — für Neuentwicklung und Anpassung, die Abschnitt 2.2 hier ausdrücklich ausnimmt.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — für die Vereinbarung, auf die Abschnitt 7.2 verweist und die Anlage 3 nicht ersetzt.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — für den Regelbetrieb nach dem Betriebshandover, den dieser Projektvertrag bewusst nicht regelt.
- [Quellcode-Herausgabe- und Datenexport-Notfallplan](../quellcode-herausgabe-und-datenexport-notfallplan/) — wenn der Exit-Test aus Anlage 4 Ziffer 3.2 in einen belastbaren Notfallablauf überführt werden soll.
