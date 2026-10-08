# Enterprise-SaaS-Rahmenvertrag

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

1. Zuerst wird die in Abschnitt 1.3 getroffene mietrechtliche Einordnung durchgerechnet, weil sie den ganzen Vertrag trägt. Findet auf die entgeltliche Bereitstellung Mietrecht Anwendung, mindert sich die Vergütung nach § 536 Abs. 1 Satz 2 BGB kraft Gesetzes für die Zeit, in der die Tauglichkeit gemindert ist, ohne dass es einer Erklärung der Kundin bedarf. Damit steht die Minderung neben den Gutschriften des Abschnitts 5.3, und Abschnitt 5.4 muss ausdrücklich sagen, ob angerechnet oder ersetzt wird. Der in Abschnitt 10.1 vorgesehene Ausschluss der verschuldensunabhängigen Haftung für anfängliche Mängel nach § 536a Abs. 1 Fall 1 BGB ist individuell verhandelbar, in vorformulierten Bedingungen dagegen an § 307 Abs. 1 Satz 1 und Abs. 2 Nr. 1 BGB zu messen.

2. Danach wird die Zweistufigkeit aus Rahmenvertrag und Bestellschein widerspruchsfrei gemacht. Abschnitt 2.5 gibt dem Bestellschein Vorrang, Abschnitt 3.3 lässt Abweichungen nur bei ausdrücklicher Kennzeichnung zu. Beides zusammen bedeutet, dass ein Bestellschein die Haftungsgrenze des Abschnitts 10.3 oder die Verfügbarkeit des Abschnitts 5.1 nur dann verschiebt, wenn er die Abweichung benennt; wer im Vertrieb Bestellscheine ohne diesen Hinweis unterzeichnet, verändert den Rahmenvertrag nicht, sondern erzeugt einen Auslegungsstreit.

3. Erst dann werden die Zahlenwerke der Verfügbarkeit geschlossen. Abschnitt 5.1 führt die geschuldete Quote als Platzhalter, während die Staffel in Abschnitt 5.3 mit festen Schwellen von 99,5, 98,0 und 95,0 Prozent arbeitet und Abschnitt 9.3 die außerordentliche Kündigung an die dauerhafte Unterschreitung knüpft. Wird der Platzhalter verhandelt, müssen alle drei Stellen mitgeführt werden. Zu entscheiden ist außerdem, ob die Ausschlussfrist von vierzehn Tagen in Abschnitt 5.3 überhaupt laufen kann, solange der Verfügbarkeitsbericht nach Abschnitt 5.5 nur auf Verlangen erstellt wird.

4. Anschließend wird die Rechtsnatur der Gutschrift bestimmt. Werden die Service Credits als pauschalierter Schadensersatz verstanden und von der Kundin gestellt, verlangt § 309 Nr. 5 Buchst. a BGB, dass die Pauschale den gewöhnlich zu erwartenden Schaden nicht übersteigt, und § 309 Nr. 5 Buchst. b BGB, dass der Anbieterin der Nachweis eines geringeren Schadens ausdrücklich offensteht; wird die Gutschrift als Vertragsstrafe ausgestaltet, tritt § 309 Nr. 6 BGB hinzu. Im unternehmerischen Verkehr gelten diese Verbote nach § 310 Abs. 1 Satz 1 BGB nicht unmittelbar, wirken aber nach § 310 Abs. 1 Satz 2 BGB in die Inhaltskontrolle nach § 307 BGB hinein. Stammt die Klausel von der Anbieterin und soll sie abschließend sein, ist sie eine Haftungsbegrenzung und an § 307 Abs. 2 Nr. 2 BGB zu messen.

5. Zuletzt werden Datenschutz und Exit zusammengeführt. Abschnitt 8.2 erlaubt eine Verarbeitung im Drittland nur unter den Voraussetzungen der Art. 44 bis 49 DSGVO und mit Zustimmung der Kundin, was ohne dokumentiertes Transfer Impact Assessment (TIA, Prüfung der Rechtslage im Empfängerland) nicht beurteilbar ist; die Kette der Unterauftragsverarbeiter richtet sich nach Art. 28 Abs. 2 und Abs. 4 DSGVO. Der Datenexport nach Abschnitt 9.4 wird mit der Rückgabe- und Löschpflicht nach Art. 28 Abs. 3 Buchst. g DSGVO abgeglichen und zusätzlich für den Insolvenzfall durchdacht, weil § 103 InsO (Insolvenzordnung) dem Verwalter bei beiderseits nicht vollständig erfüllten Verträgen ein Wahlrecht gibt und die Überleitungsunterstützung dann nicht mehr durchsetzbar ist. Live-Rechercheanker: „BGH Anwendung Mietrecht Softwareüberlassung auf Zeit“ und „§ 103 InsO Erfüllungswahl Dauerschuldverhältnis Cloud“.

### Typische Gegnereinwände mit Antwortlinie

- Die Anbieterin erklärt, die Service Credits nach Abschnitt 5.3 seien die abschließende Rechtsfolge einer Unterschreitung. Antwortlinie: Abschnitt 5.4 ordnet nur die Anrechnung an und lässt weitergehende Ansprüche bei Vorsatz und grober Fahrlässigkeit unberührt; die mietrechtliche Minderung nach § 536 Abs. 1 Satz 2 BGB tritt daneben unabhängig vom Verschulden ein. Soll sie ausgeschlossen werden, muss das ausdrücklich geschehen und hält in vorformulierten Bedingungen der Kontrolle nach § 307 Abs. 1 Satz 1 BGB nur stand, wenn ein gleichwertiger Ausgleich bleibt.

- Die Anbieterin verweist auf ihr Recht zur Weiterentwicklung nach Abschnitt 6.2 und ändert eine von der Kundin genutzte Kernfunktion mit vier Wochen Vorlauf ab. Antwortlinie: Ein einseitiger Änderungsvorbehalt in vorformulierten Bedingungen ist an § 308 Nr. 4 BGB zu messen und nur wirksam, wenn die Änderung für die andere Seite zumutbar ist; im unternehmerischen Verkehr wirkt diese Wertung über § 310 Abs. 1 Satz 2 BGB in § 307 BGB hinein. Verlangt wird deshalb, dass nachteilige Funktionsänderungen an der Leistungsbeschreibung in Anlage 1 gemessen werden und der Kundin bei wesentlicher Verschlechterung ein Sonderkündigungsrecht für den betroffenen Bestellschein zusteht.

- Die Anbieterin beruft sich bei einer Rechnungskürzung auf das Aufrechnungs- und Zurückbehaltungsverbot in Abschnitt 7.4. Antwortlinie: § 309 Nr. 3 BGB erklärt ein Aufrechnungsverbot für unbestrittene oder rechtskräftig festgestellte Forderungen für unwirksam; die Klausel nimmt diese beiden Fälle richtigerweise aus. Sie darf aber nicht so gelesen werden, dass sie das Zurückbehaltungsrecht aus demselben Vertragsverhältnis wegen eines laufenden Mangels ausschließt, weil das im Dauerschuldverhältnis den Druckmechanismus der Kundin vollständig beseitigt und an § 307 Abs. 2 Nr. 1 BGB scheitert.

- Die Anbieterin rechnet nach einer Nutzerzählung eine Nachvergütung für zurückliegende Monate ab. Antwortlinie: Abschnitt 4.2 begründet eine Mitteilungspflicht der Kundin, aber kein Recht zur rückwirkenden Abrechnung ohne Feststellung des Zeitpunkts der Überschreitung. Verlangt werden der konkrete Nachweis je Monat, die vertraglich definierte Zählweise für benannte Nutzer einschließlich ausgeschiedener und gesperrter Konten sowie die Klarstellung, ab wann die Nachvergütung nach Abschnitt 3.2 gilt.

### Häufige Fehler

- Die Verfügbarkeitsformel des Abschnitts 5.1 zieht die angekündigten Wartungsfenster aus der Bezugsgröße heraus, während Abschnitt 6.2 bis zu acht Wartungsstunden je Kalendermonat zulässt. Ohne eine Obergrenze für ungeplante Notfallwartung lässt sich die Betriebszeit rechnerisch schönen; die Ankündigungsfrist von 48 Stunden ist deshalb mit einer Zugangsregelung und einer Rechtsfolge für ihre Überschreitung zu verbinden.

- Abschnitt 8.2 verlangt für Drittlandverarbeitung die Zustimmung der Kundin, während der Auftragsverarbeitungsvertrag als Anlage 2 typischerweise eine allgemeine Genehmigung von Unterauftragsverarbeitern nach Art. 28 Abs. 2 Satz 2 DSGVO enthält. Werden beide Regelungen nicht aufeinander abgestimmt, ist unklar, ob der Wechsel eines Unterauftragnehmers in ein Drittland bereits genehmigt ist; die Widerspruchsfrist und ihre Rechtsfolge gehören deshalb in denselben Text.

- Die Haftungsgrenze des Abschnitts 10.3 knüpft an die im betroffenen Bestellschein gezahlte Jahresvergütung an, während der Schaden regelmäßig aus dem Ausfall des Gesamtsystems entsteht. Bei einer Aufteilung in viele kleine Bestellscheine sinkt die Haftungssumme, ohne dass sich das Risiko ändert; sinnvoll ist eine Bezugsgröße über alle Bestellscheine desselben Vertragsjahres.

- Der Datenexport nach Abschnitt 9.4 wird ohne Format, Datenmodell und Testlauf vereinbart. Ein Export in einem „gängigen, maschinenlesbaren Format“ ist ohne Angabe von Struktur, Metadaten und Anhängen nicht überprüfbar; die Löschbestätigung nach Anlage 3 Nummer 2.2 kommt dann, bevor die Kundin die Vollständigkeit überhaupt prüfen konnte.

## Verwandte Vorlagen

- [Software-as-a-Service-Vertrag (B2B; SLA)](../software-as-a-service-vertrag/) — wenn kein Rahmenwerk mit Bestellscheinen, sondern ein einzelner SaaS-Vertrag mit festem Leistungsumfang geschlossen wird.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — wenn die in den Abschnitten 5 und 6 nur grob gesetzten Messpunkte, Störungsklassen und Eskalationsstufen als eigene Anlage ausgearbeitet werden.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — für die in Abschnitt 8.1 als Anlage 2 vorausgesetzte Vereinbarung mit Weisungs-, Unterauftrags- und Löschregelung.
- [IT-Outsourcing-Transition-Vertrag](../it-outsourcing-transition-vertrag/) — wenn der Wechsel zu einem Nachfolgeanbieter mehr verlangt als den Datenexport nach Abschnitt 9.4.
- [Quellcode-Herausgabe- und Datenexport-Notfallplan](../quellcode-herausgabe-und-datenexport-notfallplan/) — wenn für Insolvenz oder Betriebseinstellung der Anbieterin ein Notfallzugriff auf Daten und Betriebsmittel abgesichert werden soll.

## Download

- [⬇ Enterprise SaaS Rahmenvertrag – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/enterprise-saas-rahmenvertrag/enterprise-saas-rahmenvertrag.md.zip)
- [⬇ Enterprise SaaS Rahmenvertrag – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/enterprise-saas-rahmenvertrag/enterprise-saas-rahmenvertrag.odt)

Vorschau im Repository: [`enterprise-saas-rahmenvertrag.odt`](enterprise-saas-rahmenvertrag.odt) · [`enterprise-saas-rahmenvertrag.md`](enterprise-saas-rahmenvertrag.md)
