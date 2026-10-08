# Managed Cybersecurity Service Vertrag

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

## Download

- [⬇ Managed Cybersecurity Service Vertrag – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/cybersecurity-managed-service-vertrag/cybersecurity-managed-service-vertrag.md.zip)
- [⬇ Managed Cybersecurity Service Vertrag – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/cybersecurity-managed-service-vertrag/cybersecurity-managed-service-vertrag.odt)

Vorschau im Repository: [`cybersecurity-managed-service-vertrag.odt`](cybersecurity-managed-service-vertrag.odt) · [`cybersecurity-managed-service-vertrag.md`](cybersecurity-managed-service-vertrag.md)

## Taktische Hinweise

### Vorgehensreihenfolge beim Entwurf

1. Zuerst wird die Leistungszusage des Abschnitts 1.3 gegen die Anlage 1 gehalten. Der Vertrag ordnet die Überwachung als Dienstvertrag nach § 611 Abs. 1 BGB ein, was Abnahme und Mängelrechte nach den §§ 634 ff. BGB ausschließt und Leistungsstörungen in die §§ 280, 281 BGB verweist. Einzelne Bausteine tragen dagegen Werkcharakter, etwa der Abschlussbericht nach Abschnitt 5.3 und der Schwachstellenscan nach Abschnitt 6.1; für diese ist in Anlage 1 Ziffer 2.3 festzulegen, ob ein Ergebnis oder nur eine sorgfältige Tätigkeit geschuldet ist, weil sonst offen bleibt, welche Rechtsfolge ein unbrauchbarer Bericht auslöst.

2. Danach werden die Reaktionszeiten aus Abschnitt 4.2 anknüpfungsfest gemacht. Der dortige Fristbeginn mit der Erkennung im Security Operations Center liegt allein in der Sphäre des Security-Providers; hinzuzusetzen ist ein objektiver Anknüpfungspunkt, nämlich der Zeitstempel, mit dem das auslösende Ereignis in der Auswertungsplattform eingeht. Ebenso zu definieren sind die „erste qualifizierte Befassung“ als Fristende, der Kommunikationsweg für die Benachrichtigung und die Behandlung von Ereignissen, die erst durch nachgelieferte Protokolldaten auswertbar werden. Die Beweisgrundlage bilden die Messrohdaten, die Abschnitt 6.3 für zwölf Monate vorhält und in die die Kundin Einsicht nehmen darf.

3. Erst dann wird die Malus-Architektur geprüft. Die Gutschriften nach Abschnitt 4.3 sind auf 30 Prozent der Monatsvergütung begrenzt und nach Abschnitt 4.4 innerhalb von 14 Tagen geltend zu machen. Eine so kurze Geltendmachungsfrist wirkt als Ausschlussfrist und ist an § 307 Abs. 1 BGB zu messen, zumal die Kundin die Unterschreitung erst aus dem Monatsbericht nach Abschnitt 6.3 erkennt; die Frist ist deshalb an den Zugang des Berichts zu knüpfen. Werden die Gutschriften als Pauschalierung verstanden, muss der Kundin nach dem in § 309 Nr. 5 Buchst. b BGB ausgedrückten Gedanken der Nachweis eines höheren Schadens offenstehen, der über § 310 Abs. 1 Satz 2 BGB auch im Unternehmerverkehr Indizwirkung hat.

4. Anschließend wird das Eingriffsmandat geordnet. Abschnitt 5.1 erlaubt Eilmaßnahmen nur im Rahmen einer Vorabmandatierung nach Anlage 1 Ziffer 2.4; dort sind die zulässigen Eingriffe, die betroffenen Systeme, die Grenze bei produktionskritischen Anwendungen, das Vier-Augen-Prinzip und die Nachdokumentation zu bezeichnen. Zugleich ist zu regeln, wer den Betriebsausfall trägt, wenn eine Isolierung auf einem Fehlalarm beruht, und wie sich die Freigabefristen aus Abschnitt 3.2 auf die Reaktionszeiten auswirken, wenn die Kundin nicht erreichbar ist.

5. Danach wird die Meldekette rückwärts gerechnet, weil die Fristen der Kundin die Zulieferfristen des Providers bestimmen. Bei einer Verletzung des Schutzes personenbezogener Daten muss die Kundin die Aufsichtsbehörde nach Art. 33 Abs. 1 der Datenschutz-Grundverordnung (DSGVO) binnen 72 Stunden unterrichten, während der Provider als Auftragsverarbeiter nach Art. 33 Abs. 2 DSGVO unverzüglich zu melden hat; die Benachrichtigung betroffener Personen richtet sich nach Art. 34 Abs. 1 DSGVO. Unterfällt die Kundin dem Anwendungsbereich der Richtlinie (EU) 2022/2555 (NIS-2, zweite Richtlinie zur Netz- und Informationssicherheit), tritt die Staffel aus Art. 23 Abs. 4 der Richtlinie hinzu: Frühwarnung innerhalb von 24 Stunden, Meldung innerhalb von 72 Stunden und Abschlussbericht binnen eines Monats, umgesetzt über das BSI-Gesetz in seiner jeweils geltenden Fassung. Abschnitt 5.4 überlässt die rechtliche Bewertung zu Recht der Kundin, braucht aber eine eigene Zulieferfrist in Stunden für die technische Erstinformation, weil der Abschlussbericht nach Abschnitt 5.3 erst nach fünf Werktagen vorliegt. Live-Rechercheanker: „BSI-Gesetz NIS-2-Umsetzung Anwendungsbereich Registrierung Meldefristen besonders wichtige Einrichtungen“.

6. Zuletzt werden Datenschutz, Mitbestimmung und Ausstieg geschlossen. Anlage 3 verweist bisher nur auf den Auftragsverarbeitungsvertrag; dessen Pflichtinhalte nach Art. 28 Abs. 3 DSGVO, die Genehmigung von Unterauftragsverarbeitern nach Art. 28 Abs. 2 DSGVO mit Widerspruchsrecht bei Wechseln, die Weitergabe derselben Pflichten nach Art. 28 Abs. 4 DSGVO und die Maßnahmen nach Art. 32 Abs. 1 DSGVO müssen tatsächlich vorliegen. Weil das Monitoring nach Abschnitt 2.2 auch Verhalten und Leistung von Beschäftigten erfassbar macht, ist die Mitbestimmung nach § 87 Abs. 1 Nr. 6 des Betriebsverfassungsgesetzes (BetrVG) einzuplanen, die Abschnitt 3.4 der Kundin überlässt; die Auswertungsregeln, die Zweckbindung und ein Auswertungsverbot für Leistungskontrollen gehören dazu in Anlage 1. Für den Ausstieg wird die Überleitungsunterstützung nach Abschnitt 11.3 preislich in Anlage 2 hinterlegt, und die Herausgabe nach Abschnitt 11.4 wird um die Messrohdaten und die kundenspezifischen Auswertungsregeln erweitert, soweit Abschnitt 9.2 dem nicht entgegensteht.

### Typische Einwände der Gegenseite und Antwortlinien

- Der Security-Provider wendet ein, die Reaktionszeit sei gewahrt, weil der Vorfall erst später im Security Operations Center erkannt worden sei. Antwortlinie: Abschnitt 4.2 knüpft den Fristbeginn an die Erkennung, doch die Erkennung ist keine Ermessensentscheidung, sondern Gegenstand der geschuldeten Korrelationsleistung nach Abschnitt 2.2. Vorgelegt werden die Messrohdaten aus Abschnitt 6.3 mit dem Eingangszeitstempel des auslösenden Ereignisses, und geprüft wird, ob das Regelwerk das Ereignis überhaupt erfassen konnte; eine verspätete Erkennung aufgrund eines unzureichenden Regelwerks ist Pflichtverletzung und nicht Fristverschiebung.
- Der Security-Provider wendet ein, er schulde nach Abschnitt 1.3 keine Vorfallfreiheit und hafte deshalb für den erfolgreichen Angriff nicht. Antwortlinie: Abschnitt 1.3 schließt nur die Erfolgshaftung aus, nicht die Haftung für die Verletzung der Überwachungs-, Klassifizierungs- und Reaktionspflichten; nach § 280 Abs. 1 Satz 2 BGB wird das Verschulden vermutet, wenn die Pflichtverletzung feststeht. Angesetzt wird an der Einhaltung des anerkannten Stands der Technik, an der Vollständigkeit der angebundenen Protokollquellen nach Anlage 1 Ziffer 2.1 und an der Frage, ob eine kritische Schwachstelle innerhalb der Frist des Abschnitts 6.2 gemeldet wurde.
- Der Security-Provider wendet ein, die Gutschriften nach Abschnitt 4.3 seien die abschließende Rechtsfolge einer Unterschreitung. Antwortlinie: Abschnitt 4.4 lässt weitergehende gesetzliche Ansprüche ausdrücklich unberührt und ordnet lediglich eine Anrechnung an; eine Beschränkung auf die Gutschrift wäre bei Verletzung der sicherheitskritischen Hauptleistungspflicht an § 307 Abs. 2 Nr. 2 BGB zu messen, weil sie die Erreichung des Vertragszwecks gefährdet. Verlangt wird deshalb eine Klarstellung, dass Gutschrift und Schadensersatz nebeneinander bestehen und nur wirtschaftlich verrechnet werden.
- Die Kundin wendet ein, der Provider hätte die gemeldete kritische Schwachstelle selbst schließen müssen. Antwortlinie: Abschnitt 2.3 und Abschnitt 6.2 weisen die Behebung ausdrücklich der Kundin zu, solange Anlage 1 nichts anderes vorsieht; geschuldet sind Meldung binnen 24 Stunden und Priorisierungsvorschlag. Bleibt die Kundin untätig, ist ihr Beitrag nach § 254 Abs. 1 BGB anzurechnen, und die Mitwirkungsregel des Abschnitts 3.5 verlängert die abhängigen Fristen.

### Häufige Fehler

- Die Haftungsobergrenze des Abschnitts 10.2 wird ohne Blick auf das Schadensbild vereinbart. Eine Grenze in Höhe der Jahresgrundvergütung steht bei einer Dienstleistung, deren Zweck die Abwehr existenzbedrohender Angriffe ist, in einem Spannungsverhältnis zu § 307 Abs. 2 Nr. 2 BGB; abzustimmen ist sie mit der Deckungssumme aus Abschnitt 10.5, damit die Versicherung nicht unterhalb der vertraglich zugesagten Haftung liegt.
- Die Fristen werden vorwärts statt rückwärts geplant. Solange der Provider erst nach fünf Werktagen berichtet, kann die Kundin weder die 72 Stunden aus Art. 33 Abs. 1 DSGVO noch die Frühwarnung binnen 24 Stunden aus Art. 23 Abs. 4 der Richtlinie (EU) 2022/2555 halten; nötig ist eine gestufte Zulieferpflicht mit Erstinformation in Stunden, Zwischenstand und Abschlussbericht.
- Die arbeitsrechtliche Seite wird mit Abschnitt 3.4 vollständig auf die Kundin verlagert und technisch nicht abgebildet. Ohne Zweckbindung, Rollentrennung, Protokollzugriffsbeschränkung und ein ausdrückliches Verbot der Leistungs- und Verhaltenskontrolle in Anlage 1 lässt sich die Mitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG nicht wirksam ausüben, und die Verarbeitung von Beschäftigtendaten bleibt ohne tragfähige Rechtsgrundlage.
- Die Beweissicherung nach Abschnitt 5.2 wird als rein technische Aufgabe behandelt. Ohne Hashwerte, Verwahrkette, getrennte Ablage und eine Regelung zum Umgang mit Anfragen von Strafverfolgungsbehörden entsteht Streit über die Verwertbarkeit, und die parallele Löschpflicht kollidiert mit der Aufbewahrung, die nur über die Ausnahme des Art. 17 Abs. 3 Buchst. e DSGVO für die Verteidigung von Rechtsansprüchen zu rechtfertigen ist.

## Verwandte Vorlagen

- [IT-Service-Level-Agreement](../it-service-level-agreement/) — für eine eigenständige Service-Level-Anlage, wenn Verfügbarkeit und Reaktionszeiten über den Sicherheitsdienst hinaus geregelt werden.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — für die nach Abschnitt 8.1 vorausgesetzte Anlage 3, die dieser Vertrag nur in Bezug nimmt.
- [Anlage TOM zum Auftragsverarbeitungsvertrag](../avv-tom-anlage-dsgvo/) — für die Beschreibung der Maßnahmen nach Art. 32 DSGVO, auf die Anlage 3 Ziffer 1.2 verweist.
- [Incident-Response-Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO)](../incident-response-meldung-dsk/) — für die Meldung selbst, deren rechtliche Bewertung Abschnitt 5.4 bei der Kundin belässt.
- [IT-Outsourcing-Transition-Vertrag](../it-outsourcing-transition-vertrag/) — wenn nicht nur die Sicherheitsüberwachung, sondern der gesamte Betrieb übergeben und später zurückgeführt wird.
