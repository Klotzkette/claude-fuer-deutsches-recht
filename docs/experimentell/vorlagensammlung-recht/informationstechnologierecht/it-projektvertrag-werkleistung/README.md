# IT-Projektvertrag (Werkvertrag, agil/V-Modell XT, Mitwirkungspflichten)
Werkvertrag für IT-Projekte mit Regelungen zu Leistungsumfang, Abnahme, Mitwirkungspflichten und Gewährleistung.

## Download
- [⬇ IT Projektvertrag (Werkvertrag, agil/V Modell XT, Mitwirkungspflichten) – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/it-projektvertrag-werkleistung/it-projektvertrag-werkleistung.odt) — Offene Bürofassung (OpenDocument)
- [⬇ IT Projektvertrag (Werkvertrag, agil/V Modell XT, Mitwirkungspflichten) – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/it-projektvertrag-werkleistung/it-projektvertrag-werkleistung.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`it-projektvertrag-werkleistung.odt`](it-projektvertrag-werkleistung.odt) · [`it-projektvertrag-werkleistung.md`](it-projektvertrag-werkleistung.md)

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

1. Zuerst wird das Leistungssoll geschlossen. Abschnitt 1.2 erklärt Anlage 1 zum verbindlichen Vertragsbestandteil, lässt aber Lastenheft, Pflichtenheft und Product Backlog nebeneinander stehen; das Lastenheft beschreibt nur den Bedarf des Auftraggebers, das Pflichtenheft die Umsetzungszusage des Auftragnehmers. Solange offenbleibt, welches Dokument in welchem Freigabestand gilt, ist die vereinbarte Beschaffenheit nach § 633 Abs. 2 Satz 1 BGB unbestimmt und die Auslegung fällt auf die gewöhnliche Verwendung nach § 633 Abs. 2 Satz 2 Nr. 2 BGB zurück. Festzulegen sind daher der Freigabestand mit Datum, eine Rangfolge zwischen Vertragstext, Pflichtenheft und Backlog und die ausdrückliche Aussage, ob nicht genannte Funktionen geschuldet sind. Dabei wird auch das Anlagenverzeichnis geradegezogen, denn Abschnitt 14.4 führt Anlage 5 als Open-Source-Liste, während die Anlagentabelle am Dokumentende dieselbe Anlage anders bezeichnet und die Anlagen 1 bis 3 dort denselben Namen tragen.

2. Danach wird die Variantenwahl in Abschnitt 2 wirklich vollzogen. Variante A für die Phasenplanung und Variante B für Scrum tragen beide die Nummern 2.1 und 2.2; wer nicht eine der beiden streicht, hat Meilenstein-Abnahmen und Sprint-Reviews gleichzeitig vereinbart und im Streit zwei widersprüchliche Vorgehenspflichten. Bleibt Variante B stehen, muss die Zuordnung der Priorisierungshoheit zum Auftraggeber als Product Owner mit der werkvertraglichen Erfolgshaftung aus Abschnitt 1.4 abgestimmt werden, weil sonst der Auftragnehmer den Erfolg für ein Backlog schuldet, dessen Inhalt er nicht bestimmt.

3. Erst dann wird die Abnahmearchitektur gebaut. Zusammenzuführen sind die Gesamtabnahme nach den Abschnitten 9.1 und 9.2, die Abnahmefiktion nach Abschnitt 9.3, die Teilabnahmen nach Abschnitt 9.4, der Zahlungsplan nach Abschnitt 5.2 und die Gewährleistungsfrist nach Abschnitt 10.1. Zu entscheiden ist ausdrücklich, ob die Teilabnahmen echte Abnahmen mit Gefahrübergang nach § 644 Abs. 1 Satz 1 BGB, Fälligkeit nach § 641 Abs. 1 Satz 2 BGB und Verjährungsbeginn nach § 634a Abs. 2 BGB sein sollen oder nur dokumentierte Fortschrittsbestätigungen ohne diese Wirkungen.

4. Anschließend werden die Mitwirkungspflichten des Abschnitts 4 rechtlich eingeordnet. Sind sie echte Vertragspflichten, folgen aus ihrer Verletzung Verzug nach § 286 Abs. 1 BGB und Schadensersatz nach § 280 Abs. 1 BGB; sind sie bloße Obliegenheiten des Auftraggebers, bleiben nur die Entschädigung nach § 642 Abs. 1 BGB, das Kündigungsrecht nach § 643 BGB und im Prozess die Anrechnung nach § 254 Abs. 1 BGB. Die Formulierung in Abschnitt 4.2, Kosten würden „nach § 642 BGB vergütet", ist zu schärfen, weil § 642 Abs. 2 BGB eine nach Verzugsdauer und vereinbarter Vergütung bemessene Entschädigung unter Abzug ersparter Aufwendungen und anderweitigen Erwerbs gewährt und keinen Kostenerstattungsanspruch.

5. Zuletzt werden Verzugsfolgen und Kündigungsfolgen nachgerechnet. Die Vertragsstrafe des Abschnitts 3.4 setzt Verzug voraus, der beim festen Go-Live-Termin des Abschnitts 3.2 nach § 286 Abs. 2 Nr. 1 BGB ohne Mahnung eintritt; ihre Höhe ist bei vorformulierter Verwendung an § 307 Abs. 1 Satz 1 BGB zu messen, weil § 310 Abs. 1 Satz 2 BGB die Inhaltskontrolle im Unternehmerverkehr nicht beseitigt. Parallel wird die Vergütungsfolge der freien Kündigung in Abschnitt 13.2 an § 648 Satz 2 und Satz 3 BGB angepasst und die Exit-Unterstützung nach Abschnitt 13.4 mit Format, Frist und Stundensatz so gefasst, dass der Arbeitsstand auch bei Streit über die Vergütung herausgegeben wird.

### Typische Gegnereinwände mit Antwortlinie

- Der Auftragnehmer hält das Werk nach Abschnitt 9.3 für abgenommen, weil der Auftraggeber die Abnahmefrist verstreichen ließ. Antwortlinie: § 640 Abs. 2 Satz 1 BGB verlangt die Fertigstellung des Werks, eine vom Unternehmer gesetzte angemessene Abnahmefrist und das Ausbleiben einer Verweigerung unter Angabe mindestens eines Mangels; ein einziger im Mängelrügebericht nach Abschnitt 9.2 benannter Mangel sperrt die Fiktion, und ohne Fertigstellung beginnt die Frist nicht zu laufen. Vorgelegt werden Lieferprotokoll, Abnahmetestbericht und der Zugangsnachweis der Mängelrüge.

- Der Auftragnehmer beruft sich auf fehlende Mitwirkung, verlangt neue Termine und zusätzliche Vergütung. Antwortlinie: § 642 Abs. 1 BGB setzt Annahmeverzug voraus, also eine unterlassene Mitwirkungshandlung des Auftraggebers bei gleichzeitiger Leistungsbereitschaft des Auftragnehmers; verlangt werden deshalb die Behinderungsanzeige nach Abschnitt 3.3 mit Datum, die Bezeichnung der konkret ausgebliebenen Freigabe innerhalb der Frist des Abschnitts 4.1 und der Nachweis, welcher Arbeitsschritt dadurch stillstand. Die Höhe folgt § 642 Abs. 2 BGB und nicht der internen Kostenrechnung des Auftragnehmers.

- Der Auftragnehmer bezeichnet eine geforderte Funktion als Change Request und rechnet sie nach Abschnitt 5.4 zusätzlich ab. Antwortlinie: Zuerst wird geprüft, ob die Funktion vom Leistungssoll der Anlage 1 bereits gedeckt ist, denn dann liegt keine Änderung vor. Im umgekehrten Fall gilt: Ein gesetzliches Anordnungsrecht besteht hier nicht, weil § 650b BGB nur für den Bauvertrag nach § 650a BGB gilt; ohne den unterzeichneten Nachtrag nach Abschnitt 8.1 Nummer 4 entsteht weder eine Leistungspflicht noch ein Vergütungsanspruch, und Stundennachweise ohne die in Abschnitt 5.4 verlangte Gegenzeichnung tragen die Forderung nicht.

- Der Auftragnehmer wendet ein, die Vertragsstrafe sei nicht mehr durchsetzbar, weil der Auftraggeber das Werk vorbehaltlos abgenommen habe. Antwortlinie: Der Einwand greift, soweit § 341 Abs. 3 BGB reicht; deshalb wird der Vorbehalt der verwirkten Strafe bereits im Abnahmeprotokoll nach Abschnitt 9.2 erklärt und nicht erst in einer späteren Rechnungskorrektur. Wo Teilabnahmen nach Abschnitt 9.4 erteilt werden, gehört der Vorbehalt in jede einzelne Teilabnahme.

### Häufige Fehler

- Abschnitt 13.2 kehrt die Vergütungsfolge der freien Kündigung um. Nach § 648 Satz 2 BGB behält der Auftragnehmer den Anspruch auf die vereinbarte Vergütung und muss sich ersparte Aufwendungen sowie anderweitigen Erwerb anrechnen lassen; Ersparnisse werden also abgezogen und nicht hinzugerechnet, und für den nicht erbrachten Teil greift die Vermutung des § 648 Satz 3 BGB. Wer die Klausel unverändert übernimmt, verhandelt später über eine Rechenformel, die das Gesetz nicht kennt.

- Abschnitt 9.3 verkürzt die Abnahmefiktion auf einen Hinweis des Auftragnehmers. Der Hinweis in Textform ist nach § 640 Abs. 2 Satz 2 BGB nur beim Verbraucherbesteller Voraussetzung; im Unternehmensprojekt entscheidet die angemessene Fristsetzung nach Fertigstellung. Wer sich auf den Hinweis verlässt und die Fristsetzung unterlässt, hat die Fiktion nicht ausgelöst.

- Teilabnahmen nach Abschnitt 9.4 werden im Projektalltag erteilt, ohne ihre Rechtsfolgen zu regeln. Gefahrübergang nach § 644 Abs. 1 Satz 1 BGB, Fälligkeit nach § 641 Abs. 1 Satz 2 BGB, Verjährungsbeginn nach § 634a Abs. 2 BGB und die Umkehr der Beweislast für die Mangelfreiheit treten dann für jeden Sprint gesondert ein, obwohl Abschnitt 10.1 die Gewährleistungsfrist einheitlich an die Gesamtabnahme knüpft.

- Die Gewährleistungsfrist des Abschnitts 10.1 wird als Platzhalter gefüllt, ohne sie § 634a BGB zuzuordnen. Ob die zweijährige Frist des § 634a Abs. 1 Nr. 1 BGB oder die regelmäßige Frist des § 634a Abs. 1 Nr. 3 BGB in Verbindung mit § 195 BGB gilt, ist bei Softwareerstellung nicht einheitlich beantwortet, und eine Verkürzung in vorformulierten Bedingungen ist an § 307 Abs. 1 Satz 1 und Abs. 2 Nr. 1 BGB zu messen. Live-Rechercheanker: „BGH Verjährung Werkvertrag Softwareerstellung § 634a Abs. 1 Nr. 1 BGB" und „BGH Abnahmefiktion § 640 Abs. 2 BGB angemessene Frist Mangel benannt".

## Verwandte Vorlagen

- [Agiler Softwareentwicklungsvertrag](../software-entwicklungsvertrag-agil/) — wenn das Sprintverfahren die Vertragsstruktur selbst tragen soll und nicht nur als Variante B in Abschnitt 2 eingehängt wird.
- [Software-Escrow-Vereinbarung](../software-escrow-vereinbarung/) — für die Hinterlegung, die Abschnitt 6.2 nur als Option und die Alternativklausel nur im Grundsatz benennt.
- [Softwarepflege- und Supportvertrag (Maintenance; SLA)](../softwarepflege-und-supportvertrag/) — für Fehlerbeseitigung und Versionspflege nach Ablauf der Gewährleistungsfrist des Abschnitts 10.1.
- [IT-Service-Level-Agreement](../it-service-level-agreement/) — für Verfügbarkeit, Reaktions- und Wiederherstellungszeiten im Betrieb nach dem Go-Live, den dieser Projektvertrag nicht regelt.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — für den in Abschnitt 7 nur angekündigten gesonderten Vertrag über die Verarbeitung personenbezogener Daten.
