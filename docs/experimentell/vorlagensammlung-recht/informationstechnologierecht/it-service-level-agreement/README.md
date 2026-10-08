# IT-Service-Level-Agreement

SLA für IT-Betrieb mit Verfügbarkeiten, Reaktionszeiten, Wartungsfenstern, Credits und Eskalation.

## Download
- [⬇ IT Service Level Agreement – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/it-service-level-agreement/it-service-level-agreement.odt) — OpenDocument-Arbeitsfassung
- [⬇ IT Service Level Agreement – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/it-service-level-agreement/it-service-level-agreement.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`it-service-level-agreement.odt`](it-service-level-agreement.odt) · [`it-service-level-agreement.md`](it-service-level-agreement.md)

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

1. Zuerst wird der Hauptvertrag typisiert, dem dieses Service Level Agreement (SLA, Dienstgütevereinbarung) nach Abschnitt 1.2 als Bestandteil beigefügt ist. Wird die Software als Software as a Service (SaaS) gebrauchsweise überlassen, greift Mietrecht, und die Minderung tritt nach § 536 Abs. 1 Satz 2 BGB kraft Gesetzes ein, sobald die Tauglichkeit gemindert ist. Liegt ein Dienstvertrag nach § 611 Abs. 1 BGB vor, gibt es keine Minderung, sondern nur Schadensersatz nach § 280 Abs. 1 BGB und die Kündigung. Bei werkvertraglicher Einordnung entscheidet § 633 Abs. 2 BGB über die Mangelhaftigkeit. Von dieser Zuordnung hängt ab, ob die Service Credits nach Abschnitt 7 neben die gesetzlichen Rechte treten oder an ihre Stelle treten sollen.

2. Danach wird die Verfügbarkeitsdefinition rechnerisch geschlossen. Zusammenzulesen sind der Messpunkt je Dienst in der Tabelle des Abschnitts 2.1, die Formel des Abschnitts 3.2, die Mindestdauer einer Störung nach Abschnitt 3.3, die Wartungsfenster nach Abschnitt 5.1 und die Überschreitungsregel des Abschnitts 5.2. Weil die Formel die Gesamtminuten des Kalendermonats als Bezugsgröße nimmt und Wartungszeiten nach Abschnitt 3.3 nicht als Ausfall gelten, gehen angekündigte Wartungsminuten als verfügbare Zeit in die Quote ein; wer das nicht will, rechnet sie aus der Bezugsgröße heraus. Ebenso ist ausdrücklich zu entscheiden, ob mehrere kurze Unterbrechungen unterhalb der Mindestdauer für den Monat summiert werden.

3. Erst dann werden die Zahlenwerke widerspruchsfrei gemacht. Abschnitt 3.1 führt die geschuldete Verfügbarkeit als Platzhalter, während die Staffel des Abschnitts 3.4, die Eskalationsstufe 2 in Abschnitt 9.1 und das Sonderkündigungsrecht des Abschnitts 10.2 feste Werte nennen. Wird der Platzhalter verhandelt, müssen alle drei Stellen mitgeführt werden, sonst löst die Eskalation bei einer Quote aus, die mit der geschuldeten nicht mehr übereinstimmt, und das Kündigungsrecht hängt an einem Wert, den der Vertrag nicht schuldet.

4. Anschließend wird die Rechtsnatur des Malus geklärt, und zwar getrennt danach, wer die Bedingungen stellt. Steht die Staffel in den vorformulierten Bedingungen des Kunden, ist sie ein pauschalierter Anspruch des Verwenders: § 309 Nr. 5 Buchst. a BGB verlangt, dass die Pauschale den nach dem gewöhnlichen Lauf der Dinge zu erwartenden Schaden nicht übersteigt, und § 309 Nr. 5 Buchst. b BGB, dass dem Dienstleister der Nachweis eines geringeren oder ausgebliebenen Schadens ausdrücklich offensteht; wird der Malus als Vertragsstrafe bezeichnet, tritt § 309 Nr. 6 BGB hinzu. Im Unternehmensverkehr gelten diese Verbote nach § 310 Abs. 1 Satz 1 BGB nicht unmittelbar, wirken aber nach § 310 Abs. 1 Satz 2 BGB in die Prüfung nach § 307 Abs. 1 und Abs. 2 BGB hinein. Stammen die Bedingungen dagegen vom Dienstleister und sollen die Credits abschließend sein, ist die Staffel eine Haftungsbegrenzung und an § 307 Abs. 2 Nr. 2 BGB sowie § 309 Nr. 7 Buchst. a und b BGB zu messen.

5. Zuletzt werden Kündigung und Datenrückgabe geordnet. Das Sonderkündigungsrecht des Abschnitts 10.2 wird an § 314 Abs. 1 BGB gespiegelt, weil § 314 Abs. 2 BGB bei einer Pflichtverletzung grundsätzlich eine Abmahnung oder Abhilfefrist verlangt und § 314 Abs. 3 BGB die Erklärung nur innerhalb angemessener Frist zulässt; bei mietvertraglichem Hauptvertrag tritt § 543 Abs. 3 BGB daneben. Die Herausgabe- und Löschpflicht des Abschnitts 10.3 wird mit Art. 28 Abs. 3 Buchst. g DSGVO abgestimmt, die Datensicherung nach Abschnitt 8 mit Art. 32 Abs. 1 Buchst. b und Buchst. c DSGVO und der Wiederherstellungstest nach Abschnitt 8.3 mit Art. 32 Abs. 1 Buchst. d DSGVO.

### Typische Gegnereinwände mit Antwortlinie

- Der Dienstleister rechnet die Ausfallzeit heraus und beruft sich auf Wartung, fehlerhafte Kundenkonfiguration nach Abschnitt 2.2 oder versäumte Mitwirkung nach Abschnitt 11.3. Antwortlinie: Abschnitt 5.2 macht jede Überschreitung des angekündigten Fensters zum Ausfall, und die Ankündigungsfristen der Tabelle in Abschnitt 5.1 sind mit Zugangsnachweis zu belegen. Für fremde Infrastruktur gilt, dass sich der Dienstleister das Verschulden seiner Erfüllungsgehilfen nach § 278 Satz 1 BGB zurechnen lassen muss, soweit er sie zur Erfüllung einsetzt; die Ausnahme in Abschnitt 2.2 erfasst nur Störungen außerhalb seines Einflussbereichs. Nachgeprüft wird über die Einsicht in die Monitoring-Daten nach Abschnitt 6.3.

- Der Dienstleister wendet ein, die Lösungszeit sei nach der Tabelle in Abschnitt 4.1 nur angestrebt und daher nicht geschuldet. Antwortlinie: Das trifft für diese Spalte zu; verbindlich sind dort allein die Reaktionszeiten, deren Lauf Abschnitt 4.3 an den Eingang der Meldung im Kanal der Anlage 1 knüpft. Wer Lösungszeiten durchsetzen will, macht sie zur Leistungspflicht mit eigener Rechtsfolge und verankert die Wiederanlaufzeit aus Abschnitt 8.2 in der Staffel des Abschnitts 3.4; andernfalls bleibt nur der Eskalationspfad des Abschnitts 9.1.

- Der Dienstleister behandelt die Service Credits als abschließende Regelung und verweigert weitere Ansprüche. Antwortlinie: Abschnitt 7.2 bestimmt das Gegenteil und lässt weitergehende gesetzliche Ansprüche unberührt, soweit der Schaden die Credits übersteigt. Ist der Hauptvertrag ein Mietvertrag, tritt die Minderung nach § 536 Abs. 1 Satz 2 BGB ohnehin kraft Gesetzes ein; ihre Abbedingung in vorformulierten Bedingungen ist an § 307 Abs. 1 Satz 1 BGB zu messen. Gerechnet wird auf Grundlage des Berichts nach Abschnitt 6.2.

- Der Dienstleister hält den Credit-Antrag nach Abschnitt 7.3 für verfallen. Antwortlinie: Geltend gemacht wird zunächst, dass die Antragsfrist die Berichtspflicht des Abschnitts 6.2 voraussetzt und ohne vollständigen Bericht die Berechnungsgrundlage fehlt; ergänzend ist eine so kurze Ausschlussfrist in vorformulierten Bedingungen an § 307 Abs. 1 Satz 1 und Abs. 2 Nr. 1 BGB zu messen, weil sie der gesetzlichen Verjährung vorgreift.

### Häufige Fehler

- Abschnitt 4.1 sagt im Passiv, dass Incidents klassifiziert werden, benennt aber nicht, wer die Klasse festlegt und was bei Streit über sie gilt. Weil Reaktionszeit, Eskalation und Credit an der Klasse hängen, gehören die Zuständigkeit, eine Frist für die Rückstufung und ein Verfahren für den Dissens in den Vertrag.

- Die Wiederanlaufzeit (Recovery Time Objective, RTO) und der maximal tolerierte Datenverlust (Recovery Point Objective, RPO) aus Abschnitt 8.2 bleiben ohne Rechtsfolge, weil sie weder in der Staffel des Abschnitts 3.4 noch im Kündigungsrecht des Abschnitts 10.2 auftauchen. Ihre Verfehlung bleibt dann sanktionslos, obwohl gerade sie den Schaden bestimmt.

- Der Messpunkt in Abschnitt 2.1 wird nur mit dem Beispieltext gefüllt. Ohne konkreten Endpunkt, Prüfintervall, Standort des Messsystems und Behandlung von Teilstörungen ist die Quote des Abschnitts 3.1 im Streit nicht beweisbar, und das Monitoring des Dienstleisters bleibt die einzige Datenquelle.

- Die als Best-Effort geführten Dienste der letzten Tabellenzeile in Abschnitt 2.1 und der Anlage 2 werden im Betriebsalltag wie SLA-pflichtige Dienste behandelt, ohne dass Staffel, Reaktionszeit oder Eskalation für sie gelten. Live-Rechercheanker: „BGH Verfügbarkeit Service Level Beschaffenheitsvereinbarung Minderung § 536 BGB" und „BGH pauschalierter Schadensersatz AGB Unternehmerverkehr Nachweis geringerer Schaden".

## Verwandte Vorlagen

- [Software-as-a-Service-Vertrag (B2B; SLA)](../software-as-a-service-vertrag/) — als Hauptvertrag, auf den Abschnitt 1.2 verweist, wenn die Leistung gebrauchsweise überlassen wird.
- [Softwarepflege- und Supportvertrag (Maintenance; SLA)](../softwarepflege-und-supportvertrag/) — wenn nicht die Betriebsverfügbarkeit, sondern Fehlerklassen, Versionspflege und Support den Gegenstand bilden.
- [Managed Cybersecurity Service Vertrag](../cybersecurity-managed-service-vertrag/) — wenn Erkennung, Meldung und Abwehr von Sicherheitsvorfällen eigene Reaktionspflichten tragen sollen.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — für Datensicherung, Rückgabe und Löschung, die die Abschnitte 8 und 10.3 nur betriebstechnisch beschreiben.
- [IT-Outsourcing-Transition-Vertrag](../it-outsourcing-transition-vertrag/) — wenn der Betrieb übernommen oder an einen Nachfolger übergeben wird und der Datenexport nach Abschnitt 10.3 nicht genügt.
