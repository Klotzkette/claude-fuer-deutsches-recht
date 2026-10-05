"""Zusätzlicher Schriftverkehr und Klägerentwürfe; die Stammakten bleiben unverändert."""

LAWYER = 'Rechtsanwältin Leonie von Tann, Mohnanger 8, 97082 Lindenquell bei Würzburg'
CITY = 'Stadt Lindenquell, vertreten durch den Ersten Bürgermeister Anselm Buchner, Rathausplatz 1, 97082 Lindenquell bei Würzburg'
COURT_ADDRESS = 'Ottostraße 5, 97070 Würzburg'


def doc(file, title, body, kind, sender, recipient, date='05.10.2026'):
    return dict(file=file, title=title, date=date, body=body.strip(), kind=kind,
                sender=sender, recipient=recipient, **{'from': sender, 'to': recipient})


def mail(file, title, body, sender, recipient, hour):
    return doc(file, title, body, 'email', sender, recipient,
               f'2026-10-05T{hour}:00+02:00')


def exhibit(label, source, description):
    return dict(label=label, source=source, description=description)


def claim(plaintiff, defendant, court, value, ref, content, exhibits):
    appendix = '\n\n'.join(f"{x['label']}: {x['description']}\nDatei: {x['source']}" for x in exhibits)
    return f'''ENTWURF – nicht eingereicht\nStand: 05.10.2026\n\n{LAWYER}\nAn das {court}\n{COURT_ADDRESS}\n\nKlage\n\n{plaintiff}\n– klagende Partei –\n\nProzessbevollmächtigte: {LAWYER}\n\ngegen\n\n{defendant}\n– beklagte Partei –\n\nwegen Schadensersatz\nVorläufiger Streitwert: {value} EUR\nAktenzeichen der Prozessbevollmächtigten: {ref}\n\n{content.strip()}\n\n## 9 Anlagenverzeichnis\n\n{appendix}\n\nLeonie von Tann\nRechtsanwältin'''


CAR_EXHIBITS = [
    exhibit('K1', '07_Forderung.eml', 'Forderung Dinkel vom 24.09.2026 mit ursprünglicher Berechnung.'),
    exhibit('K2', '02_Fahrerbericht.docx', 'Fahrerbericht Quast vom 08.09.2026 zum Streifkontakt.'),
    exhibit('K3', '03_Fahrzeug_und_Einsatz.docx', 'Fuhrparkauskunft und Einsatzauftrag vom 09.09.2026.'),
    exhibit('K4', '04_Zeugin.eml', 'Unabhängige Schilderung Amani vom 11.09.2026.'),
    exhibit('K5', '05_Reparaturrechnung.docx', 'Rechnung KD-260916 einschließlich Zahlungsbestätigung und Vorschadenabgrenzung.'),
    exhibit('K6', '06_Taxibelege.docx', 'Beide Werkstattfahrten und Erläuterung des Ersatzbedarfs.'),
    exhibit('K7', '09_Werkstatt_Rueckfrage.eml', 'Werkstattauskunft Dorn vom 01.10.2026.'),
    exhibit('K8', 'schriftverkehr-und-klage/01_Mandantenmail.eml', 'Ergänzung und Begrenzung der geltend gemachten Summe vom 05.10.2026.'),
    exhibit('K9', 'schriftverkehr-und-klage/02_Ergaenzende_Auskunft.eml', 'Ergänzende Erreichbarkeit und Beobachtungsgrenzen der Zeugin Amani.'),
    exhibit('K10', 'schriftverkehr-und-klage/04_Anspruchsschreiben.pdf', 'Anwaltliches Anspruchsschreiben vom 05.10.2026.'),
    exhibit('K11', 'schriftverkehr-und-klage/05_Antwort.pdf', 'Vorläufige Antwort der Stadt vom 05.10.2026.'),
]

CAR_CLAIM = claim('Tassilo Dinkel, Quittenbogen 12, 97082 Lindenquell bei Würzburg', CITY,
    'Landgericht Würzburg', '2.188,80', 'VT 26/104', '''## 1 Anträge

Namens und in Vollmacht des Klägers wird beantragt, die Beklagte zu verurteilen, an den Kläger 2.188,80 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem auf die Zustellung der Klage folgenden Tag zu zahlen. Ferner wird beantragt, der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

## 2 Gegenstand und Zuständigkeit

Der Kläger verlangt die Kosten der tatsächlich ausgeführten Reparatur seines privaten Kompaktwagens sowie zweier Werkstattfahrten. Der bei der Beklagten beschäftigte Fahrer Veit Quast streifte das abgestellte Fahrzeug am 08.09.2026 mit einem Transporter der Beklagten. Die frühere, nicht einzeln belegte Abwicklungspauschale von 25,00 EUR ist nicht Gegenstand dieser Klage. Die Reduzierung gegenüber dem Schreiben vom 24.09.2026 beruht auf der Erklärung des Klägers vom 05.10.2026, nicht auf einer Zahlung der Beklagten. Beweis: ursprüngliche Forderung, Anlage K1, und ergänzende Erklärung des Klägers, Anlage K8.

Das Landgericht ist nach § 71 Abs. 2 Nr. 2 GVG zuständig, weil der Kläger neben der Halterhaftung eine Verletzung drittbezogener Amtspflichten geltend macht. Der Streitwert unterhalb der allgemeinen amtsgerichtlichen Wertgrenze ändert diese besondere Zuständigkeit nicht. Die Fahrt diente unmittelbar der Sicherung einer gewidmeten Ortsstraße. Der Unfallort im Quittenbogen liegt im Gerichtsbezirk Würzburg; die örtliche Zuständigkeit folgt jedenfalls aus § 32 ZPO. Derselbe Lebenssachverhalt trägt den ergänzend geltend gemachten Anspruch aus § 7 Abs. 1 StVG.

## 3 Unfallhergang und Einsatz

Der Kläger hatte seinen blauen Kompaktwagen vollständig in der markierten Parkbucht vor Quittenbogen 12 abgestellt. Er ist Eigentümer, nutzt ihn ausschließlich privat und saß während des Unfalls nicht im Fahrzeug. Am 08.09.2026 gegen 09:12 Uhr hielt der städtische Transporter mit der Fuhrparknummer 17 wegen eines entgegenkommenden Lieferwagens an. Beim anschließenden langsamen Vorwärtsfahren geriet seine rechte hintere Ecke an die linke hintere Tür des klägerischen Fahrzeugs. Es entstand eine frische längliche Schramme mit Eindellung. Der Fahrer bemerkte das Schaben, hielt sofort an und verständigte den Kläger durch Klingeln.

Beweis: Fahrerbericht, Anlage K2; Zeugnis des Veit Quast, zu laden über Stadt Lindenquell, Bauhof, Amselspange 2, 97082 Lindenquell; Zeugnis der Yasmin Amani, Quittenbogen 10, erster Stock, 97082 Lindenquell, Anlagen K4 und K9. Die Zeugin beobachtete vom Küchenfenster aus den stehenden Wagen, das Vorwärtsfahren und den Kontakt. Sie kann weder einen genauen Zentimeterabstand noch den Blick des Fahrers in den Spiegel bekunden. Darauf wird der Beweisantritt ausdrücklich nicht erstreckt.

Die Beklagte trägt Betriebskosten und Wartung des Transporters, entscheidet über seinen Einsatz und besitzt ihn seit 2022. Quast stand während seiner Dienstzeit unter der Disposition des Bauhofs. Um 08:55 Uhr war ihm aufgetragen worden, sechs Baken und zwei Warnleuchten direkt zu einer kurz zuvor gemeldeten Fahrbahnabsenkung vor Quittenbogen 26 zu bringen und die Stelle gegen Befahren zu sichern. Der Unfallort vor Haus 12 lag auf diesem direkten Weg. Nach dem Zusammenstoß übernahm ein Ersatzteam den Auftrag. Ein privater Transport oder eine bloße Fahrt zum regelmäßigen Arbeitsplatz lag nicht vor.

Beweis: Fuhrparkauskunft und Einsatzauftrag 26-391, Anlage K3; Zeugnis der Hildegard Knorz, Disposition, zu laden über den genannten Bauhof. Die Kennzeichnung als „Amtsfahrt“ im Fahrtenbuch ist ein ergänzendes Indiz. Entscheidend sind die konkret belegten Sicherungsmittel, der unmittelbare Auftrag und sein örtlicher Zusammenhang mit der öffentlichen Gefahrenstelle.

## 4 Verantwortung der Beklagten

Die Beklagte haftet als Halterin nach § 7 Abs. 1 StVG. Das Fahrzeug wurde mit ihrem wirtschaftlichen Aufwand und in ihrem Verfügungsbereich betrieben. Der Schaden entstand durch seine Fahrbewegung. Es geht daher nicht um eine bloß gelegentliche Anwesenheit einer Arbeitsmaschine an einem anderen Schadensort. Ein außergewöhnliches äußeres Ereignis oder ein technischer Defekt wird auch vom Fahrer nicht beschrieben. Der entgegenkommende Lieferwagen erklärt das vorherige Anhalten, beseitigt aber nicht den Zusammenhang zwischen Wiederanfahren und Streifkontakt.

Daneben besteht ein Anspruch aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG. Der Fahrer erfüllte unmittelbar eine kommunale Straßenverkehrssicherungsaufgabe. Art. 9 Abs. 5 BayStrWG ordnet diese Aufgabe dem öffentlichen Amt zu. Zur sicheren Erfüllung gehörte, bei gewöhnlicher Verkehrsteilnahme ausreichenden seitlichen Abstand zum ruhenden Eigentum Dritter zu halten und gegebenenfalls weiter abzuwarten. Die Sicherungsfahrt erforderte weder eine Berührung des geparkten Wagens noch eine riskante Fortsetzung. Quast hat keine Sonderrechte in Anspruch genommen. Sein eigener Bericht nennt keine unvermeidbare Ausweichbewegung.

Für den funktionellen Zusammenhang einer Einsatzfahrt mit öffentlicher Aufgabe und die Auswirkungen auf die persönliche Fahrerhaftung wird auf BGH, Urteil vom 18.12.2007 – VI ZR 235/06, Rn. 22–25, verwiesen. Die dortigen Feuerwehr- und Sozialversicherungsfragen werden hier nicht übertragen. Die bei hoheitlicher Einordnung eingreifende Haftungsüberleitung schützt nicht die Beklagte vor ihrer Außenverantwortung. Der Fahrer wird deshalb nicht zusätzlich persönlich nach § 18 StVG verklagt. Die eigenständige Halterhaftung der Beklagten bleibt bestehen.

Auch der Hinweis auf eine denkbare andere Ersatzquelle greift nicht durch: Der Streit betrifft gewöhnliche Teilnahme am Straßenverkehr; hierzu behandelt die genannte Entscheidung die Grenze des § 839 Abs. 1 Satz 2 BGB. Eine Versicherungsleistung an den Kläger liegt überdies nicht vor. Ob die Beklagte intern Versicherungsschutz oder einen kommunalen Ausgleich besitzt, ist für die eingeklagte Außenforderung unerheblich. Ein bestimmter Versicherer oder Ausgleichsverband wird nicht als weiterer Schuldner behauptet.

## 5 Reparaturschaden

Die Werkstatt Korbinian Dorn richtete die linke hintere Tür und lackierte sie nach Vorbereitung neu. Die Rechnung KD-260916 weist zweimal sechs Arbeitsstunden zu jeweils 95,00 EUR, mithin 570,00 EUR für das Richten und 570,00 EUR für die Lackierarbeit, aus. Hinzu kommen 360,00 EUR Lackmaterial, 200,00 EUR für Demontage und Montage sowie 100,00 EUR für die beschädigte Zierleiste. Der Nettobetrag beträgt 1.800,00 EUR, die tatsächlich berechnete Umsatzsteuer 342,00 EUR und der bezahlte Gesamtbetrag 2.142,00 EUR.

Beweis: Rechnung mit Zahlungsbestätigung, Anlage K5; ergänzende Auskunft, Anlage K7; Zeugnis des Korbinian Dorn, Karosseriewerkstatt Korbinian Dorn, Spindelgasse 4, 97082 Lindenquell. Der Zeuge kann die vorgefundene Eindellung, den Arbeitsumfang und die Zahlung am 16.09.2026 bestätigen. Zum technischen Zusammenhang zwischen dem beschriebenen seitlichen Kontakt und den abgerechneten Arbeiten wird erforderlichenfalls die Einholung eines kraftfahrzeugtechnischen Sachverständigengutachtens angeboten. Als Anknüpfungstatsachen dienen der konkrete Berührungsbereich, der Fahrerbericht und die werkstattseitig erhaltenen Aufnahmebilder, deren Herausgabe der Kläger bereits erbeten hat. Diese Bilder sind mangels bisheriger Dateiübermittlung noch keine Anlage dieser Klage.

Ein älterer Kratzer an der rechten vorderen Stoßstange wurde von der Werkstatt bei Annahme getrennt vermerkt und weder beseitigt noch abgerechnet. Der Kläger verlangt keine Aufwertung des gesamten Fahrzeugs. Die bezahlte Rechnung ersetzt zwar nicht die Prüfung der Unfallursächlichkeit jeder Position; zusammen mit der örtlich begrenzten Beschädigung und dem werkstattseitigen Befund belegt sie hier die erforderliche Wiederherstellung nach § 249 Abs. 2 BGB. Eine unwirtschaftliche Ersatzbeschaffung oder ein Totalschaden wird nicht behauptet.

Der Bruttoansatz folgt aus der tatsächlich durchgeführten, vollständig bezahlten Reparatur. Der Kläger ist Rentner und betreibt kein Unternehmen. Ein Vorsteuerabzug steht ihm für dieses Fahrzeug nicht zu. Die Umsatzsteuer wird daher nicht lediglich aus einem unverbindlichen Kostenvoranschlag übernommen. Die Parteianhörung des Klägers wird zur privaten Nutzung und zur Zahlung ergänzend angeregt; die objektive Rechnungs- und Zahlungsbestätigung bleibt das vorrangige Beweismittel.

## 6 Werkstattfahrten und Gesamtbetrag

Der Wagen war zunächst fahrbereit und wurde am 15.09.2026 um 08:00 Uhr zur Reparatur gebracht. Die Abholung erfolgte am 16.09.2026 um 16:20 Uhr. Der Kläger fuhr nach Abgabe und zur Abholung jeweils mit Taxi Nadir Nuss zwischen Werkstatt und Wohnung. Die Quittungen 5118 und 5146 weisen jeweils 23,40 EUR einschließlich Umsatzsteuer aus. Zusammen sind dies 46,80 EUR. Trinkgelder oder weitere Besorgungsfahrten sind nicht enthalten.

Beweis: Taxibelege und Erläuterung, Anlage K6; Zeugnis des Nadir Nuss, Taxi Nadir Nuss, Holundersteig 5, 97082 Lindenquell. Die beiden Wege dienten unmittelbar der Durchführung der Reparatur. Der zweite Familienwagen stand zu den benötigten Zeiten nicht zur Verfügung, weil die Ehefrau ihn für ihre Frühschicht außerhalb des Orts benötigte. Dazu wird das Zeugnis der Irmgard Dinkel, Quittenbogen 12, 97082 Lindenquell, angeboten. Ein Mietwagen oder zusätzlicher Nutzungsausfall wird nicht verlangt.

Die Gesamtsumme errechnet sich aus 2.142,00 EUR Reparaturkosten zuzüglich 46,80 EUR Beförderungskosten und beträgt 2.188,80 EUR. Die am 24.09.2026 zusätzlich verlangten 25,00 EUR werden nicht eingeklagt, weil der Kläger keine Einzelbelege gesammelt hat und diesen Nebenstreit vermeiden möchte. Dies verändert weder die Rechnungssumme noch die ursprüngliche Unfallschilderung. Außergerichtliche Anwaltskosten sind ebenfalls nicht Teil des Zahlungsantrags.

## 7 Einwendungen und Beweiswürdigung

Die Beklagte fordert in ihrem vorläufigen Schreiben vom 05.10.2026 Aufnahmebilder und nähere Angaben zur Nutzung des zweiten Familienwagens. Die Klägerseite legt die schon vorhandene Werkstattauskunft und die ergänzende Erklärung vor. Ein verbindliches Anerkenntnis wird aus dem Fahrerbericht nicht hergeleitet. Sein Gewicht liegt vielmehr in der zeitnahen konkreten Beschreibung eines eigenen Wahrnehmungsvorgangs, die mit der unabhängigen Zeugin und dem Schadenbild übereinstimmt.

Für ein Mitverschulden nach § 254 BGB besteht nach den verfügbaren Tatsachen keine Grundlage. Der Kläger fuhr nicht, öffnete keine Tür und hatte den Wagen innerhalb der Parkbucht abgestellt. Die Zeugin bestätigt gerade diesen Standort. Es wird keine beliebige Quote allein wegen der Eigenschaft als Fahrzeughalter gebildet. Sollte die Beklagte eine konkrete Parkbehinderung geltend machen, müsste sie sich mit der beobachteten Lage und dem Streifbereich auseinandersetzen. Der Kläger bietet hierzu die bereits benannten Zeugen an.

Eine vollständige Klärung durch die noch ausstehenden Fotos ist wünschenswert, aber nicht Voraussetzung dafür, den bewiesenen äußeren Ablauf zu schildern. Ebenso wenig wird aus dem Fehlen eines Fotos auf eine Beweisvereitelung geschlossen. Der Werkstattinhaber hat lediglich zwei Bilder aus der Annahme angekündigt; eine vollständige Unfallrekonstruktion hat er ausdrücklich nicht zugesagt.

## 8 Zinsen und Verfahrensstand

Der Zinsantrag beruht auf §§ 291, 288 Abs. 1 Satz 2 BGB und knüpft allein an eine künftige Zustellung an. Ein Zustellungstag wird nicht vorweggenommen. Auf einen bereits eingetretenen Verzug, eine abgelaufene Zahlungsfrist oder eine ernsthafte endgültige Erfüllungsverweigerung stützt sich der Kläger nicht. Seine ursprüngliche Bitte um Antwort bis 12.10.2026 ist am Entwurfsstand noch offen. Die vorläufige Antwort vom 05.10.2026 enthält noch keine abschließende Sachentscheidung.

Eine Einigung wurde bislang nicht erreicht; der laufende Schriftwechsel eröffnet weiterhin eine außergerichtliche Lösung. Dieser Entwurf dient der Vorbereitung und liegt nicht beim Gericht. Zur Entscheidung durch den Einzelrichter bestehen keine Bedenken. Ein besonderer Antrag auf Videoverhandlung wird derzeit nicht gestellt. Die Anlagen K10 und K11 bilden den bislang erreichten außergerichtlichen Stand ab und sind bei einer späteren Einreichung um zwischenzeitliche Zahlungen oder weitere Erklärungen zu ergänzen.''', CAR_EXHIBITS)

CASES = [dict(
    slug='akha-wuerzburg-fahrzeugschaden', claim_file='06_Klageentwurf.docx',
    exhibits=CAR_EXHIBITS,
    notes='Klage nur 2.188,80 EUR; ursprüngliche 25-EUR-Pauschale ausdrücklich ausgeklammert. Antwortfrist 12.10.2026 am Stichtag offen. Eigene Klägervertreterin, keine Mandatsvermischung. Zusätzliche Anschriften und Namen sind Fortsetzungstatsachen.',
    attachments={'03_Begleitmail.eml': ['05_Antwort.pdf', '../02_Fahrerbericht.docx', '../03_Fahrzeug_und_Einsatz.docx']},
    documents=[
mail('01_Mandantenmail.eml', 'Dinkel: Betrag und Werkstattwege', '''Sehr geehrte Frau von Tann,

bitte bereiten Sie, wie heute besprochen, zunächst das Schreiben und einen Klageentwurf vor. Eine Einreichung beauftrage ich heute nicht; meine Bitte um Antwort bis 12. Oktober soll bestehen bleiben. Die 25 Euro für Telefonate und Kopien möchte ich nicht mit einklagen. Ich finde dafür keine einzelnen Belege mehr. Es bleiben die bezahlte Reparatur von 2.142,00 Euro und zwei Taxifahrten zu je 23,40 Euro, also 2.188,80 Euro.

Meine Frau Irmgard kann bestätigen, dass sie unseren zweiten Wagen an beiden Werkstatttagen für ihre Frühschicht benötigte. Sie wohnt wie ich am Quittenbogen 12, 97082 Lindenquell. Die Taxifahrten führten nur zur Werkstatt beziehungsweise nach Hause. Ich bin weiter Eigentümer des reparierten Autos, habe keine Ansprüche abgetreten und bislang keinen Cent von einer Versicherung oder der Stadt erhalten.

Die Bilder auf meinem alten Telefon lassen sich noch nicht zuverlässig öffnen. Bitte behaupten Sie deshalb nicht, dass sie schon als Anlage verfügbar wären. Herr Dorn sagte, seine Werkstattbilder seien noch gespeichert. Ich habe ihn gebeten, sie aufzubewahren. Mir ist wichtig, dass der alte Kratzer vorne rechts nicht mit der beschädigten hinteren Tür vermischt wird.

Mit freundlichen Grüßen
Tassilo Dinkel''', 'Tassilo Dinkel <tassilo.dinkel@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '10:10'),
mail('02_Ergaenzende_Auskunft.eml', 'Amani: Anschrift und Grenzen meiner Beobachtung', '''Sehr geehrte Frau von Tann,

Sie dürfen meine Nachricht vom 11. September verwenden. Meine vollständige Anschrift lautet Yasmin Amani, Quittenbogen 10, erster Stock, 97082 Lindenquell bei Würzburg. Ich bin bereit, als Zeugin auszusagen. Ich kenne Herrn Dinkel nur vom Grüßen und habe kein eigenes Interesse an seiner Erstattung.

Ich habe das Auto vor dem Kontakt vollständig in der Parkbucht stehen sehen. Der Transporter fuhr nach einer kurzen Pause weiter, dann kam das Schaben. Von oben sah ich die rechte hintere Ecke des Transporters dicht an der linken Tür des blauen Autos. Welcher Millimeter zuerst berührte, kann ich selbstverständlich nicht sagen. Auch die Spiegel des Fahrers habe ich nicht beobachtet. Ich möchte nicht, dass meine Schilderung genauer gemacht wird, als sie ist.

Fotos oder ein Video besitze ich nicht. Ob die Tür schon vorher einen ganz kleinen Kratzer hatte, weiß ich nicht. Die längliche beschädigte Stelle nach dem Zusammenstoß und das sofortige Anhalten habe ich dagegen selbst gesehen. Bitte geben Sie diese Unterscheidung so weiter.

Mit freundlichen Grüßen
Yasmin Amani''', 'Yasmin Amani <yasmin.amani@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '10:45'),
mail('03_Begleitmail.eml', 'Dinkel: Vorläufige Antwort und zwei Sachunterlagen', '''Sehr geehrte Frau von Tann,

anbei erhalten Sie unsere heutige vorläufige Antwort als PDF sowie den Fahrerbericht und die Fuhrparkauskunft als unveränderte Dokumentkopien. Die Unterlagen werden zur Sachaufklärung übermittelt. Ein Anerkenntnis zu Grund oder Höhe ist damit nicht verbunden. Wir haben Ihre Mitteilung zur Verringerung der geltend gemachten Summe auf 2.188,80 Euro vermerkt.

Unsere Rechtsstelle hat Frau Rechtsanwältin Samira Seidel mit der Prüfung für die Stadt beauftragt. Sie vertritt nicht Ihren Mandanten und auch nicht den Fahrer persönlich. Bitte richten Sie weitere Tatsachenmitteilungen zunächst an mich, damit Werkstattbilder und Fuhrparkakte gemeinsam ausgewertet werden können. Die Fahreranschrift für dienstliche Rückfragen ist der Bauhof, Amselspange 2, 97082 Lindenquell.

Wir behandeln den 12. Oktober weiterhin als den von Herrn Dinkel erbetenen Antworttermin. Die heutige Zwischenantwort setzt keine neue Zahlungsfrist und enthält keine Zusage eines Versicherers. Eine Zahlung ist bisher nicht angewiesen worden.

Mit freundlichen Grüßen
Kunigunde Färber
Stadt Lindenquell, Rechtsstelle''', 'Kunigunde Färber <recht@lindenquell.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '16:10'),
doc('04_Anspruchsschreiben.docx', 'Dinkel gegen Stadt Lindenquell – Reparatur und Werkstattfahrten', '''Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

Stadt Lindenquell – Rechtsstelle
Rathausplatz 1, 97082 Lindenquell bei Würzburg

05.10.2026 · Unser Zeichen VT 26/104

Sehr geehrte Frau Färber,

ich vertrete Herrn Tassilo Dinkel, Quittenbogen 12, in der Angelegenheit vom 8. September 2026. Mein Mandant verfolgt nunmehr 2.188,80 EUR: 2.142,00 EUR aus der bezahlten Reparaturrechnung und 46,80 EUR für die beiden notwendigen Werkstattfahrten. Die zuvor genannte Pauschale von 25,00 EUR wird in diesem Schreiben nicht weiterverfolgt. Eine Zahlung oder anderweitige Erstattung ist nicht erfolgt.

Nach Fahrerbericht und Zeugenschilderung berührte der städtische Transporter den vollständig in seiner Parkbucht stehenden Wagen beim Vorwärtsfahren. Die linke hintere Tür wurde instand gesetzt; der alte Kratzer an der rechten vorderen Stoßstange blieb unberührt. Die Werkstatt kann die Abgrenzung erläutern. Mein Mandant ist Privatnutzer ohne Vorsteuerabzug. Seine Ehefrau benötigte den zweiten Familienwagen an den beiden Reparaturtagen selbst; ein Mietwagen wurde nicht genommen.

Die Einordnung der konkreten Sicherungsfahrt ist neben der eigenständigen Halterhaftung zu prüfen. Bitte teilen Sie nicht lediglich mit, dass es eine Amtsfahrt gewesen sei. Maßgeblich sind tatsächlicher Auftrag und Betrieb des Fahrzeugs. Ich bitte um die vorhandene Fahrer- und Fuhrparkauskunft sowie um eine Aussage, welche einzelne Rechnungsposition aus Ihrer Sicht ungeklärt bleibt.

Die bereits erbetene Antwort bis zum 12. Oktober 2026 bleibt bestehen. Ich erwarte Ihre begründete Stellungnahme und eine Mitteilung, ob die belegte Summe ausgeglichen wird. Aufnahmebilder werden nachgereicht, sobald sie tatsächlich vorliegen. Bis dahin behaupte ich keine fotografische Unfallrekonstruktion. Dieses Schreiben enthält keine Erklärung, eine bereits laufende Frist sei abgelaufen.

Mit freundlichen Grüßen
Leonie von Tann
Rechtsanwältin''', 'letter', LAWYER, CITY),
doc('05_Antwort.docx', 'Stadt Lindenquell – Zwischenantwort an die Klägervertreterin', '''Stadt Lindenquell – Rechtsstelle
Rathausplatz 1, 97082 Lindenquell bei Würzburg

Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

05.10.2026 · Zeichen LQ-R 26/391

Sehr geehrte Frau von Tann,

wir bestätigen den Eingang Ihres heutigen Schreibens. Die Reduzierung der Forderung auf 2.188,80 EUR ist vermerkt. Den Kontakt zwischen unserem Transporter und dem geparkten Wagen stellen wir auf Grundlage des Fahrerberichts derzeit nicht in Abrede. Ein abschließendes Anerkenntnis, insbesondere zum Umfang des erforderlichen Reparaturaufwands, geben wir damit nicht ab.

Wir übermitteln Ihnen Fahrerbericht und Fuhrparkauskunft. Daraus ergibt sich der unmittelbare Sicherungsauftrag für die Fahrbahnabsenkung. Die Rechtsprüfung betrifft sowohl die tatsächliche Halterstellung als auch die Bedeutung dieses Einsatzes. Die bloße Fahrtenbuchüberschrift ist nicht unsere alleinige Entscheidungsgrundlage. Eine persönliche Zahlungszusage des Fahrers ist nicht dokumentiert.

Bitte lassen Sie die zwei bei der Werkstatt gespeicherten Bilder der beschädigten Tür sichern und nach Möglichkeit übersenden. Die Trennung vom alten Stoßstangenkratzer ist nachvollziehbar beschrieben, muss aber mit der Werkstattaufnahme abgeglichen werden. Zu den Taxifahrten bitten wir um Bestätigung, dass der zweite Familienwagen zu den konkreten Abgabe- und Abholzeiten nicht verfügbar war. Ihre heutige Erläuterung wird in die Prüfung einbezogen; die bloße Existenz eines zweiten Wagens ist für uns noch kein Ablehnungsgrund.

Wir wollen Ihnen bis zum 12. Oktober eine weitere Nachricht geben. Eine verbindliche Regulierung oder Deckung durch einen bestimmten Versicherer können wir heute nicht erklären. Bitte verstehen Sie diese sachbezogenen Rückfragen nicht als abschließende Zurückweisung des Anspruchs.

Mit freundlichen Grüßen
Kunigunde Färber
Rechtsstelle der Stadt Lindenquell''', 'letter', CITY, LAWYER),
doc('06_Klageentwurf.docx', 'Klageentwurf Dinkel gegen Stadt Lindenquell', CAR_CLAIM, 'claim', LAWYER, 'Landgericht Würzburg')
])]

BATH_EXHIBITS = [
    exhibit('K1', '02_Benutzungsordnung_und_Eintritt.docx', 'Eintrittsbeleg und privatrechtliche Benutzungsordnung, zusammengestellt am 28.09.2026.'),
    exhibit('K2', '03_Unfallmeldung.docx', 'Erstvermerk Klee vom 22.08.2026 ohne eigene Unfallbeobachtung.'),
    exhibit('K3', '04_Kontrollbuch.docx', 'Morgenmeldung, unterbliebene Sperrung und spätere Reparatur der Leiter.'),
    exhibit('K4', '05_Behandlungsbericht.docx', 'Befunde der Dr. Sporn vom 22.08. und 01.09.2026.'),
    exhibit('K5', '06_Auslagenbelege.docx', 'Verbandmaterial 18,90 EUR und Taxi 23,80 EUR.'),
    exhibit('K6', '07_Forderung.eml', 'Forderung und Berichtigung der Erstschilderung vom 25.09.2026.'),
    exhibit('K7', '08_Zeugin_Nwosu.eml', 'Beobachtung der Zeugin Nwosu vom 28.09.2026.'),
    exhibit('K8', '09_Technik_Rueckmeldung.eml', 'Technische Erläuterung Lerch vom 29.09.2026.'),
    exhibit('K9', 'schriftverkehr-und-klage/01_Mandantenmail.eml', 'Beschwerdeverlauf und begrenzter Klageauftrag vom 05.10.2026.'),
    exhibit('K10', 'schriftverkehr-und-klage/02_Ergaenzende_Auskunft.eml', 'Lerch zu Beweisstück, Erreichbarkeit und fehlender Freigabeprüfung.'),
    exhibit('K11', 'schriftverkehr-und-klage/04_Anspruchsschreiben.pdf', 'Anwaltliche Bezifferung vom 05.10.2026.'),
    exhibit('K12', 'schriftverkehr-und-klage/05_Antwort.pdf', 'Betreiberantwort mit Einwendungen zu Unfallablauf und Schmerzensgeld.'),
]

BATH_CLAIM = claim('Walburga Rebhuhn, Pflaumenstieg 6, 97082 Lindenquell bei Würzburg',
    'Lindenqueller Bäderbetrieb GmbH, vertreten durch die Geschäftsführerin Fatima Fink, Seerosenbogen 3, 97082 Lindenquell bei Würzburg',
    'Amtsgericht Würzburg', '892,70', 'VT 26/105', '''## 1 Anträge

Namens und in Vollmacht der Klägerin wird beantragt, die Beklagte zu verurteilen, an die Klägerin 850,00 EUR Schmerzensgeld sowie weitere 42,70 EUR materiellen Schadensersatz, zusammen 892,70 EUR, nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem auf die Zustellung der Klage folgenden Tag zu zahlen. Ferner wird beantragt, der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Der Schmerzensgeldantrag ist bewusst auf einen bestimmten Betrag gerichtet. Er enthält keinen verdeckten Antrag auf einen beliebigen Mehrbetrag. Ein Feststellungsantrag wegen künftiger Schäden wird auf dem derzeitigen Befundstand nicht gestellt.

## 2 Vertrag, Parteien und Gericht

Die Klägerin kaufte am 22.08.2026 um 10:06 Uhr für 6,50 EUR eine Eintrittskarte für das Lindenbad. Vertragspartnerin war die beklagte GmbH, die das Bad betreibt, Eintrittsentgelte im eigenen Namen vereinnahmt und eigenes Betriebs- und Aufsichtspersonal beschäftigt. Die Eintrittsbedingungen sehen ausdrücklich ein privatrechtliches Benutzungsverhältnis vor. Die Klägerin verlangt Ersatz wegen einer nicht gesicherten mechanisch lockeren Einstiegsstufe. Die Stadt ist zwar alleinige Gesellschafterin, wird aber nicht als Vertragspartnerin oder zusätzliche Schuldnerin verklagt.

Beweis: Eintrittsbeleg und Benutzungsordnung, Anlage K1. Das Amtsgericht ist nach § 23 Nr. 1 GVG sachlich zuständig; der bestimmte Zahlungsanspruch liegt unter der seit 2026 maßgeblichen Grenze von 10.000 EUR. Eine Amtshaftung wird gegen die GmbH nicht geltend gemacht. Das Bad liegt im Gerichtsbezirk Würzburg; der behauptete Verletzungsort begründet jedenfalls die örtliche Zuständigkeit nach § 32 ZPO. Vertragliche und deliktische Ansprüche betreffen denselben Lebenssachverhalt.

## 3 Ablauf im Bad

Die Klägerin benutzte die westliche Edelstahlleiter, um in das Becken zu steigen. Sie ging rückwärts hinunter und hielt sich mit beiden Händen an den Holmen fest. Als sie den rechten Fuß auf die zweite Stufe setzte, gab diese nach. Ihr rechtes Schienbein stieß an das Metall unterhalb der Stufe. Es entstand eine blutende, ungefähr drei Zentimeter lange oberflächliche Riss- und Schürfwunde mit Prellung. Die Klägerin war weder auf dem Beckenumgang gerannt noch dort vor Erreichen der Leiter ausgerutscht.

Zum beobachtbaren Bewegungsablauf wird das Zeugnis der Chinwe Nwosu, Pflaumenstieg 8, 97082 Lindenquell, angeboten. Die Zeugin stand etwa einen Meter hinter der Klägerin und sah deren Absacken an der Leiter sowie den anschließenden Kontakt. Sie hatte keine lückenlose Sicht auf beide Füße. Diese Grenze ihrer Wahrnehmung ist in Anlage K7 offengelegt. Ergänzend wird die persönliche Anhörung der Klägerin angeregt. Die Zeugin soll die eigene Schilderung der Klägerin nicht in Punkten ersetzen, die sie selbst nicht sehen konnte.

Anselm Klee versorgte die Klägerin gegen 10:42 Uhr und notierte sinngemäß ein Ausrutschen am Beckenrand mit Anschlagen am Metall. Er beobachtete den Unfall nicht und ließ die Klägerin den Text nicht unterschreiben. Seine knappe Zusammenfassung ist daher keine eigene Augenzeugenbeschreibung und kein von der Klägerin gebilligtes Protokoll. Sie zeigte ihm die Leiter. Bei seiner Kontrolle gegen 10:48 Uhr stellte er die lose Stufe fest und sperrte den Einstieg. Beweis: Anlage K2; Zeugnis des Anselm Klee, zu laden über die Beklagte, Seerosenbogen 3, 97082 Lindenquell.

## 4 Kenntnis und unterbliebene Sicherung

Bereits um 07:35 Uhr hatte die Mitarbeiterin Marisol Sturm die lockere rechte Befestigung der zweiten Stufe bemerkt. Sie meldete sie um 07:41 Uhr dem Techniker Severin Lerch. Dieser war wegen eines Filteralarms anderweitig gebunden. Eine Sperrkette wurde bis zum Unfall nicht angebracht. Der rote Hinweis im Personalraum erreichte die Besucher nicht. Auch die Übergabe um 09:50 Uhr führte weder zu einer wirksamen Sperrung noch zu einer Belastungsprüfung vor weiterer Benutzung.

Beweis: Kontrollbuch, Anlage K3; Zeugnis der Marisol Sturm und des Severin Lerch, beide zu laden über die Beklagte unter der genannten Betriebsanschrift. Lerch bestätigte am 29.09.2026 und erneut am 05.10.2026, dass die Meldung eingegangen war, aber keine Person eine erfolgreiche Abhilfe zurückgemeldet hatte. Seine technische Rückmeldung und die ergänzende Auskunft werden als Anlagen K8 und K10 vorgelegt. Gegen 11:20 Uhr fand er eine fehlende Sicherungsscheibe, ersetzte Mutter und Scheibe und prüfte die Leiter unter Belastung. Die Freigabe erfolgte erst gegen 11:35 Uhr. Die ausgebaute Mutter ist bezeichnet aufbewahrt; ein unverändertes vollständiges Befestigungssystem steht dagegen nicht mehr zur Besichtigung bereit.

Die Beklagte schuldete aus dem Eintrittsvertrag Rücksicht auf die körperliche Unversehrtheit ihrer Besucherinnen, §§ 280 Abs. 1, 241 Abs. 2 BGB. Die sichere Benutzbarkeit einer angebotenen Einstiegsleiter gehört dazu. Zwischen einer normalen nassen Oberfläche und einer nachgebenden tragenden Stufe besteht ein entscheidender Unterschied. Nach der konkreten Morgenmeldung musste die Beklagte den Einstieg entweder fachgerecht instand setzen und prüfen oder für die Besucher erkennbar sperren. Beides war ohne Stilllegung des ganzen Bades möglich. Der Filteralarm erklärt die verzögerte Reparatur, rechtfertigt aber keine über Stunden offen gebliebene gefährliche Leiter.

Das Verhalten des für Wartung und Besuchersicherheit eingesetzten Personals wird der Beklagten nach § 278 BGB zugerechnet. Für ein fehlendes Vertretenmüssen ist nach § 280 Abs. 1 Satz 2 BGB die Beklagte darlegungspflichtig. Daraus folgt keine Umkehr der Beweislast für das Nachgeben der Stufe oder den Verletzungszusammenhang; diese Tatsachen werden mit den bezeichneten Beweismitteln unterlegt. Daneben kommt die Verletzung der betrieblichen Verkehrssicherungspflicht aus § 823 Abs. 1 BGB in Betracht. Schon die vertragliche Zurechnung trägt den gegen die Betreiberin gerichteten Anspruch, ohne dass eine Entlastung nach § 831 BGB diesen beseitigen könnte.

BGH, Urteil vom 05.10.2004 – VI ZR 294/03, gedruckte Seiten 6–8 des amtlichen Volltexts, beschreibt den Schutz vor besonderen, nicht ohne Weiteres erkennbaren Gefahren eines Schwimmbadbetriebs. Die dortige Wasserrutsche ist technisch nicht mit dieser Leiter gleichzusetzen. Entscheidend ist hier die tatsächlich bekannte mechanische Gefahr. Weder eine technische Rutschennorm noch eine Beweislastregel aus Ertrinkungsfällen wird übernommen.

## 5 Verletzung und Schmerzensgeld

Dr. Mirela Sporn untersuchte die Klägerin am Unfalltag um 12:05 Uhr. Sie stellte die oberflächliche drei Zentimeter lange Verletzung und eine Prellung am rechten Schienbein fest. Eine tiefe klaffende Wunde, eine Nahtversorgung, ein klinischer Frakturhinweis oder ein neurovaskulärer Ausfall lagen nicht vor. Die Wunde wurde gereinigt und verbunden; der Tetanusschutz war ausreichend. Am 01.09.2026 war sie trocken und weitgehend geschlossen. Es bestanden noch eine leichte Verfärbung und Druckschmerz. In der ersten Woche waren längeres Gehen und Knien schmerzhaft eingeschränkt.

Beweis: Behandlungsbericht, Anlage K4; Zeugnis der behandelnden Ärztin Dr. Mirela Sporn, Ringelgasse 8, 97082 Lindenquell. Die Klägerin entbindet die Ärztin für die Befunde und die Behandlung dieser konkreten Verletzung von der Schweigepflicht. Zu einem darüber hinausgehenden allgemeinen Gesundheitszustand wird kein Beweisantritt erhoben. Falls die Beklagte den Zusammenhang zwischen dem dokumentierten Anstoß und den Befunden substantiiert bestreitet, wird ein medizinisches Sachverständigengutachten zu diesem Zusammenhang angeboten.

Nach der ergänzenden Erklärung vom 05.10.2026, Anlage K9, kann die Klägerin wieder ohne Beschwerden gewöhnlich gehen. Beim längeren Knien verspürt sie noch Druckempfindlichkeit; die Stelle ist rötlich sichtbar. Diese letzten Angaben sind ihre eigene Wahrnehmung und kein neuer ärztlicher Befund. Seit dem 01.09.2026 hat keine weitere Untersuchung stattgefunden. Eine bleibende Narbe oder dauerhafte Funktionseinbuße wird deshalb nicht behauptet. Die Klägerin war nicht stationär behandelt worden und verlangt keinen Verdienstausfall.

Der bestimmte Betrag von 850,00 EUR nach § 253 Abs. 2 BGB berücksichtigt die akute blutende Verletzung, die erste schmerzhafte Woche und die nachfolgende Druckempfindlichkeit. Zugleich begrenzen der oberflächliche Befund, die fehlende Naht und die weitgehend abgeschlossene Heilung das Gewicht der Verletzung. Der Betrag wird nicht aus einem vermeintlich festen Tarif abgeleitet. Die bekannte und leicht sperrbare Fehlerstelle prägt den Anlass der Genugtuung, ersetzt aber nicht die maßvolle Bewertung der tatsächlichen Folgen. Sollte das Gericht einen geringeren Betrag für angemessen halten, ist nur der bezifferte Antrag in diesem Umfang zu beurteilen.

## 6 Materielle Aufwendungen

Die Klägerin kaufte am 22.08.2026 Verbandmaterial für 18,90 EUR. Der Apothekenbeleg gliedert diesen Betrag in 10,90 EUR für Wundauflagen und 8,00 EUR für Binden. Die Materialien dienten dem Verbandwechsel nach der Erstversorgung. Hinzu kommt die Taxifahrt von der Praxis zur Wohnung am selben Tag um 12:42 Uhr für 23,80 EUR. Die Freundin hatte die Klägerin kostenfrei zur Praxis gebracht, konnte sie aber nach dem Termin nicht zurückfahren. Eine doppelte Fahrtkostenabrechnung erfolgt nicht.

Beweis: Auslagenbelege, Anlage K5; für Beförderung und Barzahlung Zeugnis des Nadir Nuss, Taxi Nadir Nuss, Holundersteig 5, 97082 Lindenquell. Das verletzte und frisch versorgte Bein rechtfertigte die kurze Heimfahrt im Taxi. Die Klägerin verlangt weder die Erstattung des Eintritts noch Kosten für eine nicht belegte Haushaltshilfe. Der materielle Antrag beträgt daher genau 18,90 EUR zuzüglich 23,80 EUR, insgesamt 42,70 EUR. Zahlungen Dritter oder Abtretungen liegen nach ihrer Erklärung nicht vor.

## 7 Einwendungen und Kausalität

Die Beklagte verweist in ihrer Antwort, Anlage K12, auf die abweichende Erstnotiz und die eingeschränkte Sicht der Zeugin. Beides wird nicht übergangen. Entscheidend ist die Gesamtbetrachtung: Die lose zweite Stufe war lange vor dem Unfall gemeldet, unmittelbar nach der von der Klägerin bezeichneten Benutzung erneut festgestellt und danach repariert worden. Der dokumentierte Anstoß am Schienbein ist mit einem Absacken an dieser Stelle vereinbar. Klee kann erläutern, aus welchem Gespräch seine verkürzte Notiz entstand. Die Klägerin hat bereits im Forderungsschreiben vom 25.09.2026 und damit vor diesem Entwurf eine Berichtigung verlangt; dieses Schreiben ist Anlage K6.

Zum technischen Nachgeben der Stufe unter gewöhnlichem Körpergewicht wird erforderlichenfalls ein Sachverständigengutachten unter Auswertung des Kontrollbuchs, der Zeugenaussagen und des erhaltenen Befestigungsteils angeboten. Der reparierte Zustand beweist nicht für sich allein den früheren Unfallmechanismus. Die Klägerin verlangt deshalb keine schematische Beweislastumkehr. Die bekannte Lockerung, die zeitnahe Sperrung und die eigene Wahrnehmung bilden vielmehr überprüfbare Anknüpfungstatsachen.

Ein Mitverschulden nach § 254 BGB folgt nicht schon aus der allgemeinen Nässe eines Bades. Die Klägerin hielt sich an beiden Holmen fest. Eine für Besucher erkennbare Sperrung oder Warnung fehlte; der Hinweis hing nur im Personalraum. Ein falsches Auftreten auf einer sichtbar gefährlichen Stufe müsste konkret festgestellt werden. Die Beklagte behauptet bisher keinen eigenen Augenzeugen hierfür. Die Klägerin räumt die Wahrnehmungsgrenzen der Zeugin ein, ohne damit einen anderen Unfallablauf zuzugestehen.

## 8 Zinsen und außergerichtlicher Stand

Die beanspruchten Prozesszinsen folgen aus §§ 291, 288 Abs. 1 Satz 2 BGB. Sie beginnen nach dem Antrag erst am Tag nach einer künftigen Zustellung. Ein früherer Verzugsbeginn wird nicht behauptet. Die mit Schreiben vom 25.09.2026 erbetene Antwort bis zum 12.10.2026 ist am Entwurfsstand noch nicht fällig. Die Betreiberin hat am 05.10.2026 lediglich eine vorläufige Gegenposition mitgeteilt. Eine abschließende Ablehnung oder ein bereits geführtes Gerichtsverfahren wird daraus nicht gemacht.

Das anwaltliche Anspruchsschreiben vom 05.10.2026, Anlage K11, und die Antwort der Betreiberin, Anlage K12, führten noch nicht zu einer Einigung. Die Klägerin ist für einen sachbezogenen Vergleich offen. Der Entwurf ist nicht eingereicht; vor einer späteren Einreichung ist der weitere Beschwerde- und Verhandlungsstand abzugleichen. Es wird derzeit keine besondere Form der Videoverhandlung beantragt. Die vorhandenen Rechnungen, die bestimmten Beträge und das nachfolgende Anlagenverzeichnis ermöglichen der Beklagten eine konkrete Stellungnahme zu jedem geltend gemachten Posten.''', BATH_EXHIBITS)

CASES.append(dict(
    slug='akha-wuerzburg-schwimmbad', claim_file='06_Klageentwurf.docx', exhibits=BATH_EXHIBITS,
    notes='Privatrechtlicher Vertrag mit GmbH; AG-Zuständigkeit und 850 EUR bestimmtes Schmerzensgeld plus42,70. Kein Dauerschaden behauptet, kein Feststellungsantrag. Neue Anschriften und Heilungsverlauf als Fortsetzung kenntlich.',
    attachments={'03_Begleitmail.eml': ['05_Antwort.pdf', '../03_Unfallmeldung.docx', '../04_Kontrollbuch.docx', '../09_Technik_Rueckmeldung.eml']},
    documents=[
mail('01_Mandantenmail.eml', 'Rebhuhn: Heilungsverlauf und Auftrag', '''Sehr geehrte Frau von Tann,

ich bitte um ein anwaltliches Schreiben an die Bädergesellschaft und einen Klageentwurf für den Fall, dass wir keine Einigung erzielen. Bitte reichen Sie noch nichts ein. Ich hatte eine Antwort bis 12. Oktober erbeten und will diese Zeit abwarten. Es bleibt bei 850 Euro Schmerzensgeld und 42,70 Euro belegten Auslagen. Meine Nachbarin Chinwe Nwosu wohnt am Pflaumenstieg 8, 97082 Lindenquell, und ist mit ihrer Benennung als Zeugin einverstanden.

Zum heutigen Zustand: Normales Gehen geht wieder ohne Beschwerden. Wenn ich länger knie, drückt die Stelle noch. Sie ist rötlich, aber ich kann nicht sagen, ob das eine bleibende Narbe wird. Nach dem Termin am 1. September war ich nicht mehr bei Dr. Sporn. Bitte machen Sie daraus keinen zusätzlichen ärztlichen Befund. In der ersten Woche war die Wunde besonders beim Treppensteigen und Knien störend. Eine Haushaltshilfe habe ich nicht bezahlt.

Dr. Sporn darf Ihnen und gegebenenfalls dem Gericht über genau diese Verletzung berichten. Ich entbinde sie insoweit von der Schweigepflicht. Niemand hat mir bisher Geld erstattet, auch das Eintrittsgeld nicht. Der kurze Erstvermerk des Bademeisters gibt meine Schilderung weiterhin nicht richtig wieder: Ich war bereits auf der Leiter, als die Stufe nachgab.

Mit freundlichen Grüßen
Walburga Rebhuhn''', 'Walburga Rebhuhn <walburga.rebhuhn@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '09:55'),
mail('02_Ergaenzende_Auskunft.eml', 'Lindenbad: Aufbewahrung der Mutter und Dienstanschriften', '''Sehr geehrte Frau von Tann,

Frau Fink hat mich gebeten, Ihre konkrete Nachfrage zur Befestigung zu beantworten. Die am 22. August ausgebaute Mutter liegt weiterhin in einem beschrifteten Beutel im verschlossenen Technikschrank. Auf dem Beutel stehen Datum und „Westleiter, zweite Stufe rechts“. Die damals fehlende Sicherungsscheibe kann ich naturgemäß nicht vorlegen. An der Leiter sind seit der Reparatur eine neue Mutter und eine neue Scheibe montiert. Der alte Zustand lässt sich daher am laufenden Badbetrieb nicht unverändert besichtigen.

Meine Darstellung vom 29. September bleibt richtig. Nach der Morgenmeldung habe ich wegen des Filteralarms nicht selbst gesperrt. Ich bekam vor dem Unfall auch keine Nachricht, jemand anderes habe die Stufe repariert oder unter Last geprüft. Das rote Blatt im Personalraum war keine für Gäste sichtbare Warnung. Ob Frau Rebhuhn mit dem rechten oder linken Fuß zuerst abstieg, habe ich nicht gesehen.

Marisol Sturm, Anselm Klee und ich sind über Lindenqueller Bäderbetrieb GmbH, Seerosenbogen 3, 97082 Lindenquell erreichbar. Bitte vereinbaren Sie eine Besichtigung des Beutels über die Geschäftsführung, damit die Entnahme nachvollziehbar bleibt.

Mit freundlichen Grüßen
Severin Lerch, Badtechnik''', 'Severin Lerch <technik@lindenbad.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '11:05'),
mail('03_Begleitmail.eml', 'Rebhuhn: Zwischenantwort und Betriebsunterlagen', '''Sehr geehrte Frau von Tann,

anbei übersende ich die heutige Antwort unserer Geschäftsführerin Fatima Fink als PDF. Ebenfalls beigefügt sind die unveränderten Kopien des Unfallvermerks, des Kontrollbuchauszugs und der technischen Rückmeldung vom 29. September. Damit sollen die verschiedenen Zeitpunkte und Wahrnehmungen überprüfbar sein. Aus der Überlassung folgt keine Zustimmung zu Ihrer Schmerzensgeldbemessung.

Unsere Gesellschaft bearbeitet den Anspruch selbst als Betreiberin und Vertragspartnerin. Die Stadt erhält nicht anstelle der GmbH die an sie gerichteten Zahlungsforderungen. Frau Rechtsanwältin Samira Seidel prüft die Angelegenheit ausschließlich für unsere Gesellschaft. Einen gemeinsamen Auftrag mit Frau Rebhuhn gibt es nicht.

Bitte berücksichtigen Sie, dass das Technikteam den Unfall nicht beobachtet hat. Der technische Zustand und die konkrete Fußbewegung sind verschiedene Fragen. Über eine ergänzende Untersuchung der behaupteten fortbestehenden Beschwerden können wir sprechen, sobald ein entsprechender ärztlicher Befund vorliegt. Der 12. Oktober bleibt der gewünschte Antworttermin; ein Vergleich ist noch nicht geschlossen.

Mit freundlichen Grüßen
Fatima Fink
Geschäftsführerin''', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '16:20'),
doc('04_Anspruchsschreiben.docx', 'Rebhuhn gegen Bäderbetrieb – Ersatz wegen loser Einstiegsstufe', '''Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

Lindenqueller Bäderbetrieb GmbH
Geschäftsführerin Fatima Fink
Seerosenbogen 3, 97082 Lindenquell bei Würzburg

05.10.2026 · Unser Zeichen VT 26/105

Sehr geehrte Frau Fink,

ich vertrete Frau Walburga Rebhuhn wegen der Verletzung am 22. August in Ihrem Bad. Meine Mandantin verlangt weiterhin 850,00 EUR Schmerzensgeld und 42,70 EUR Auslagen, insgesamt 892,70 EUR. Sie stützt sich auf ihren Eintrittsvertrag mit Ihrer Gesellschaft. Die kommunale Gesellschafterstellung macht die Stadt nicht zur Ersatzschuldnerin des Vertrags.

Entscheidend ist die seit dem Morgen gemeldete lose zweite Stufe der Westleiter. Meine Mandantin stieg rückwärts und mit beiden Händen an den Holmen in das Becken. Die Stufe gab nach; sie schlug mit dem rechten Schienbein an. Der knappe Erstvermerk stammt von einem Mitarbeiter, der das Ereignis nicht beobachtete, und wurde von ihr nicht unterschrieben. Frau Nwosu kann das Absacken an der Leiter bestätigen, beansprucht aber keine vollständige Sicht auf beide Füße.

Der ärztliche Bericht beschreibt eine oberflächliche Wunde und Prellung, ohne Naht, Fraktur oder stationäre Behandlung. Auf dieser Grundlage wird kein Dauerschaden behauptet. Der Betrag berücksichtigt die schmerzhafte erste Woche und die noch bestehende Druckempfindlichkeit. Die Wundversorgungskosten von 18,90 EUR und die Heimfahrt aus der Praxis von 23,80 EUR sind gesondert belegt. Verdienstausfall, Haushaltshilfe und Eintrittsgeld sind nicht Gegenstand unserer Forderung.

Bitte erläutern Sie bis zum bereits genannten 12. Oktober, weshalb die gemeldete Leiter vor dem Unfall nicht gesperrt wurde und welche konkrete Unfallalternative Sie annehmen. Ich bitte zugleich darum, das ausgebaute Befestigungsteil und die ursprünglichen Betriebsaufzeichnungen weiter zu erhalten. Meine Mandantin ist zu einer sachbezogenen außergerichtlichen Lösung bereit.

Mit freundlichen Grüßen
Leonie von Tann
Rechtsanwältin''', 'letter', LAWYER, 'Lindenqueller Bäderbetrieb GmbH, Seerosenbogen 3, 97082 Lindenquell'),
doc('05_Antwort.docx', 'Bäderbetrieb – Vorläufige Stellungnahme zu Ablauf und Forderung', '''Lindenqueller Bäderbetrieb GmbH
Seerosenbogen 3, 97082 Lindenquell bei Würzburg

Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

05.10.2026 · Zeichen LB 26/0822

Sehr geehrte Frau von Tann,

wir bedauern die Verletzung Ihrer Mandantin. Die morgendliche Meldung einer lockeren Stufe und die erst nach dem Ereignis angebrachte Sperrung nehmen wir ernst. Derzeit können wir dennoch weder den von Ihnen dargestellten Bewegungsablauf noch die gesamte Forderung abschließend anerkennen. Unsere Mitarbeiterin hatte einen technischen Fehler gemeldet; sie war beim späteren Abstieg nicht anwesend.

Der Erstvermerk spricht von einem Ausrutschen am Beckenrand. Wir sehen, dass Herr Klee kein Augenzeuge war und Frau Rebhuhn den Vermerk nicht unterschrieben hat. Gerade deshalb möchten wir beide Wahrnehmungen auseinanderhalten. Die Zeugin Nwosu konnte nach ihrer eigenen Nachricht die Fußstellung nicht vollständig sehen. Bitte teilen Sie mit, ob eine weitere Person den eigentlichen Tritt auf die zweite Stufe beobachtet hat. Wir behaupten nicht, eine normale nasse Fläche erkläre bereits jeden Unfall.

Die vorliegenden Auslagen sind beziffert. Beim Schmerzensgeld sind die oberflächliche Verletzung, die fehlende Nahtversorgung und der weitgehend verheilte Befund vom 1. September zu berücksichtigen. Einen neueren medizinischen Bericht haben wir nicht. Den verlangten Betrag von 850,00 EUR halten wir deshalb bisher für nicht ausreichend erläutert, schließen eine angemessene Entschädigung aber nicht grundsätzlich aus.

Die alte Mutter bleibt erhalten; Herr Lerch hat Ihnen die Aufbewahrung erläutert. Wir übermitteln die vorhandenen Betriebsunterlagen und wollen bis zum 12. Oktober nach rechtlicher Prüfung erneut Stellung nehmen. Eine Deckungszusage oder ein verbindliches Vergleichsangebot ist mit diesem Schreiben nicht verbunden.

Mit freundlichen Grüßen
Fatima Fink
Geschäftsführerin''', 'letter', 'Lindenqueller Bäderbetrieb GmbH', LAWYER),
doc('06_Klageentwurf.docx', 'Klageentwurf Rebhuhn gegen Bäderbetrieb', BATH_CLAIM, 'claim', LAWYER, 'Amtsgericht Würzburg')
]))

TREE_EXHIBITS = [
    exhibit('K1', '02_Arbeitsauftrag.docx', 'Arbeitsauftrag 26-B47 mit Schnittvorgaben und städtischer Absperrzuständigkeit.'),
    exhibit('K2', '03_Absperrvermerk.docx', 'Vermerk Zwirn vom 04.09.2026 zur begrenzten Freigabe.'),
    exhibit('K3', '04_Ereignisbericht.docx', 'Bericht König über Seilführung, Freigabeverständnis und Astkontakt.'),
    exhibit('K4', '05_Zeugin.eml', 'Beobachtungen der Kioskbetreiberin Lenz vom 10.09.2026.'),
    exhibit('K5', '06_Reparaturrechnung.docx', 'Reparaturrechnung Halm über 2.927,40 EUR mit Zahlungshinweis.'),
    exhibit('K6', '07_Mietwagenrechnung.docx', 'Zwei Tage Ersatzwagen für 84,00 EUR und Nutzungsangaben.'),
    exhibit('K7', '08_Forderung.eml', 'Forderung Sesam vom 22.09.2026 und Abstellzeit des Wagens.'),
    exhibit('K8', '09_Unternehmen_Stellungnahme.eml', 'Stellungnahme Astwerk Amal Berg vom 29.09.2026.'),
    exhibit('K9', 'schriftverkehr-und-klage/01_Mandantenmail.eml', 'Ergänzungen zu Erstattungen, Parken und Ersatzbedarf vom 05.10.2026.'),
    exhibit('K10', 'schriftverkehr-und-klage/02_Ergaenzende_Auskunft.eml', 'Unternehmerische Ergänzung zu Technik, Weisungsinhalt und Anschriften.'),
    exhibit('K11', 'schriftverkehr-und-klage/04_Anspruchsschreiben.pdf', 'Konkretisiertes Anspruchsschreiben an die Stadt.'),
    exhibit('K12', 'schriftverkehr-und-klage/05_Antwort.pdf', 'Städtische Gegenposition zu Freigabe, Unternehmer und Halteverbot.'),
]

TREE_CLAIM = claim('Leander Sesam, Kerbelring 18, 97082 Lindenquell bei Würzburg', CITY,
    'Landgericht Würzburg', '3.011,40', 'VT 26/106', '''## 1 Anträge

Namens und in Vollmacht des Klägers wird beantragt, die Beklagte zu verurteilen, an den Kläger 3.011,40 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem auf die Zustellung der Klage folgenden Tag zu zahlen. Ferner wird beantragt, der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

## 2 Anspruchsgegenstand und Zuständigkeit

Der Kläger verlangt Ersatz der Reparatur seines privaten Kombis und eines Ersatzwagens für zwei Werkstatttage. Am 03.09.2026 gegen 08:23 Uhr traf ein bei angeordneten Pflegearbeiten abgetrennter Ast des kommunalen Straßenahorns KR18 das vor Kerbelring 18 abgestellte Fahrzeug. Die Beklagte hatte die Arbeiten veranlasst und die Räumung des Arbeitsbereichs sowie seine abschnittsweise Freigabe selbst übernommen. Der Kläger stützt seine Forderung insbesondere auf die bei der Stadt verbliebene Sicherungs- und Koordinationspflicht.

Der Kerbelring ist eine gewidmete Ortsstraße in der Baulast der Beklagten; der Ahorn gehört als Straßenbaum zur öffentlichen Anlage. Die konkrete Arbeit diente der Beseitigung eines frisch gespaltenen, auskragenden Astes. Nach Art. 9 Abs. 5 BayStrWG ist die Straßenverkehrssicherung öffentliche Aufgabe. Der Anspruch wird deshalb aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG hergeleitet. Das Landgericht ist unabhängig vom Streitwert nach § 71 Abs. 2 Nr. 2 GVG sachlich und wegen des im Bezirk gelegenen Schadensorts nach § 32 ZPO örtlich zuständig.

## 3 Auftrag, Absperrung und Schadensablauf

Am 31.08.2026 stellte die städtische Baumkontrolle den frischen Spalt fest. Mit Auftrag 26-B47 vom 01.09.2026 bestimmte die Beklagte den Baum, den markierten Schnittbereich und den Arbeitstag. Das Unternehmen Astwerk Amal Berg GmbH sollte die Schnitttechnik, Geräte, Seilführung und Besetzung fachlich selbst festlegen. Die Beklagte übernahm dagegen die Parkraumfreimachung, Absperrung und abschnittsweise Arbeitsfreigabe. Solange Fahrzeuge im Fallbereich standen, sollte der betroffene Abschnitt nicht bearbeitet werden.

Beweis: Arbeitsauftrag, Anlage K1; Zeugnis des Ottokar Zwirn, zu laden über Stadt Lindenquell, Bauhof, Amselspange 2, 97082 Lindenquell; Zeugnis des Ravi König, Astwerk Amal Berg GmbH, Scherenbogen 4, 97082 Lindenquell. Diese Aufteilung ist für die Haftung entscheidend: Der Kläger behauptet nicht, dass die Stadt jeden einzelnen technischen Handgriff vorgegeben hätte. Er beruft sich darauf, dass die Stadt gerade die grundlegende räumliche Sicherung selbst in der Hand behielt.

Um 07:40 Uhr stand der schwarze Kombi des Klägers weiterhin in der mittleren Parkbucht. Um 07:55 Uhr wurden Baken gestellt. Zwirn bat einen Kollegen, bei Anwohnern zu klingeln. Gegen 08:10 Uhr erteilte er nach seinem Vermerk nur eine Freigabe für den bereits freien südlichen Bereich. Der Vorarbeiter König verstand die Äußerung weitergehend. Eine gemeinsame Skizze, eindeutige Markierung der Freigabegrenze oder gegengezeichnete Freigabe existiert in den vorliegenden Unterlagen nicht. Das Tagesblatt vermerkt nur den Beginn um 08:10 Uhr.

Um 08:20 Uhr telefonierte Zwirn wegen einer möglichen Entfernung des weiterhin geparkten Fahrzeugs mit der Disposition. Drei Minuten später blieb bei der Schnittarbeit ein Seil an einer Astgabel hängen. Das Holz schwenkte aus und traf Dach und Heckscheibe des Kombis. Ein unmittelbarer Kontakt des Fahrzeugs mit Werkzeug oder Arbeitskorb ist nicht behauptet. Beweis: Absperrvermerk, Anlage K2; Ereignisbericht, Anlage K3; ergänzende Stellungnahmen, Anlagen K8 und K10; Zeugnisse Zwirn und König. Die Mitarbeiterin Inés Waldner ist für die beobachtete Ausführung ebenfalls über das Unternehmen zu laden.

Fadime Lenz sah vom gegenüberliegenden Kiosk aus Baken, den noch dort stehenden Wagen und den telefonierenden städtischen Mitarbeiter. Sie hörte die Freigabe nicht. Ihr Zeugnis wird für diese äußeren Umstände angeboten, nicht für den Wortlaut eines ungehörten Gesprächs. Ladungsanschrift: Kiosk Fadime Lenz, Kerbelring 17, 97082 Lindenquell. Ihre E-Mail ist Anlage K4. Das Schadensereignis wird dadurch mit zeitnahen Wahrnehmungen aus verschiedenen Blickrichtungen verknüpft, ohne eine vollständige Augenzeugenschaft aller Beteiligten zu unterstellen.

## 4 Eigene Amtspflichtverletzung der Stadt

Die Beklagte musste die aktiven Arbeiten so organisieren, dass vorhersehbar gefährdetes fremdes Eigentum im betroffenen Bereich geschützt wurde. Der Kläger stand mit seinem Wagen gerade in der Zone, deren Räumung die Stadt übernommen hatte. Selbst wenn eine Teilfreigabe zulässig war, musste für das ausführende Team unmissverständlich erkennbar sein, welcher Abschnitt gesperrt blieb. Angesichts des für alle sichtbaren Fahrzeugs reichte ein undifferenzierter Arbeitsbeginn ohne verlässlich vermittelte Grenze nicht aus.

Der Anspruch setzt keine Pflicht voraus, jedes denkbare Restrisiko auszuschließen. Der konkrete Schutz war hier zumutbar: Arbeit am betroffenen Ast erst nach tatsächlicher Räumung oder nach einer fachlich gesicherten, eindeutig abgestimmten Abgrenzung. Die Stadt musste nicht selbst die optimale Seiltechnik erfinden. Sie durfte aber das von ihr verantwortete Freigabesystem nicht so führen, dass ein bekanntes Hindernis im Gefahrenbereich bei bereits laufender Arbeit verblieb. Die zeitgleiche Rückfrage wegen Abschleppens belegt, dass die Beseitigung dieses Hindernisses noch ungelöst war.

BGH, Urteil vom 04.07.2013 – III ZR 250/12, Rn. 13–18, behandelt zumutbare Sicherungsmaßnahmen bei aktiven Straßenunterhaltungsarbeiten. Die dort erörterten Schutzmaßnahmen bei Mäharbeiten sind keine technische Anleitung für Baumpflege. Übertragbar ist die Pflicht, konkret vorhersehbare Eigentumsschäden bei der gewählten Arbeitsweise mit zumutbaren Mitteln zu verhindern. Hier werden Räumung, klare Freigabegrenzen und Unterbrechung beansprucht, keine bestimmte Schutzwand aus einem anderen Sachverhalt.

Bei klar vermitteltem und beachtetem Stopp des betroffenen Abschnitts wäre der Schnitt mit dem Wagen im Schwenkbereich nicht ausgeführt worden. Darin liegt der Zusammenhang zwischen dem vorgeworfenen Koordinationsfehler und dem Schaden. Sollte die Beklagte behaupten, das Unternehmen habe eine unmissverständliche ausdrückliche Sperre eigenmächtig übergangen, sind der tatsächliche Wortlaut, seine Wahrnehmbarkeit und die räumliche Zuordnung durch die genannten Zeugen zu klären. Der Kläger leitet nicht schon aus dem bloßen Schadenseintritt einen städtischen Fehler ab.

## 5 Stellung des Fachunternehmens und anderweitiger Ersatz

Zusätzlich kommt eine Zurechnung der konkreten Ausführung als hoheitliche Helfertätigkeit in Betracht. Maßgeblich sind Auftrag und tatsächliche Einbindung insgesamt. Baum, Schnittziel, Zeitpunkt und abschnittsweise Freigabe stammten von der Stadt. Das Unternehmen war zugleich fachlich frei in Seilführung, Geräten und Personaleinsatz. Diese technische Selbstständigkeit ist ein gewichtiges Gegenargument, schließt einen funktionellen Helferzusammenhang aber nicht allein durch die Rechtsform des Unternehmens aus.

BGH, Urteil vom 11.01.2024 – III ZR 15/23, Rn. 9 und 11–17, stellt auf den funktionellen Aufgabenbezug und den Einfluss der öffentlichen Hand ab. Die Entscheidung betraf die Umsetzung einer konkreten Beschilderungsanordnung. Der Kläger setzt daher nicht jeden kommunalen Auftrag mit einem Verwaltungshelferverhältnis gleich. Die vorliegenden Weisungs- und Freigabeelemente sind vielmehr an diesen Kriterien zu würdigen. Wird die Tätigkeit als hoheitliche Hilfe eingeordnet, ist die haftungsrechtliche Überleitung nach Art. 34 GG auch für den Ausführungsfehler zu beachten.

Wird das Unternehmen dagegen als selbstständiger privater Leistungserbringer eingeordnet, bleibt die eigene städtische Sicherungspflicht als gesonderter Haftungsgrund bestehen. Ein denkbarer deliktischer Anspruch gegen das Unternehmen wird nicht verschwiegen. Der Einwand aus § 839 Abs. 1 Satz 2 BGB trägt hier dennoch nicht: Die beanstandete Pflicht zur Sicherung des Arbeits- und Verkehrsbereichs entspricht inhaltlich der allgemeinen Verkehrssicherungspflicht. Für diesen Bereich greift das Verweisungsprivileg nicht ein; vgl. OLG Hamm, Urteil vom 06.04.2022 – 11 U 143/21, Rn. 25, amtlicher Volltext. Dort war ebenfalls eine mögliche Haftung des ausführenden Unternehmens zu berücksichtigen. Nordrhein-westfälisches Straßenrecht wird nicht auf die bayerische Aufgabe übertragen.

Es geht nicht um einen allein hoheitlich geprägten Entscheidungsfehler bei einer straßenverkehrsrechtlichen Anordnung, sondern um die konkrete Sicherung einer betriebenen Arbeitsstelle. Der Kläger muss daher keine unbelegte Insolvenz des Unternehmens behaupten. Die Stadt kann ihre Außenverantwortung nicht allein mit dem Hinweis auf dessen Betriebshaftpflicht verneinen. Ein möglicher Innenausgleich zwischen Stadt und Unternehmen ist nicht Gegenstand dieser Klage; der Kläger verlangt die Summe nur einmal.

## 6 Reparatur und Ersatzmobilität

Die Karosserie Hedwig Halm GmbH reparierte das Fahrzeug am 10. und 11.09.2026. Die Rechnung umfasst netto 800,00 EUR Dachinstandsetzung, 720,00 EUR Lackierung, 460,00 EUR Heckscheibe, 380,00 EUR Einbau und 100,00 EUR Reinigung. Die Nettosumme beträgt 2.460,00 EUR, die Umsatzsteuer 467,40 EUR, die bezahlte Gesamtsumme 2.927,40 EUR. Die Zahlung erfolgte am 16.09.2026. Beweis: Anlage K5; Zeugnis der Hedwig Halm, Karosserie Hedwig Halm GmbH, Mispelgasse 7, 97082 Lindenquell.

Dach- und Glasschaden passen zum herabgeschwenkten Holz. Bei substantiiertem technischem Bestreiten wird ein Sachverständigengutachten zum Zusammenhang zwischen Astkontakt, Schadenbereichen und erforderlichen Reparaturmaßnahmen angeboten. Der Kläger verlangt keinen Ersatz eines bloßen Kostenvoranschlags und keine allgemeine Wertverbesserung. Das Fahrzeug wurde bis zur Reparatur in einer geschützten Garage abgestellt und nicht weitergefahren. Der Kläger ist angestellter Buchhändler, nutzt den Kombi privat und kann die tatsächlich angefallene Umsatzsteuer nicht als Vorsteuer abziehen.

Für den 10. und 11.09.2026 mietete er bei Mobilität Noura Nessel einen Ersatzwagen für zwei Tage zu je 42,00 EUR brutto, insgesamt 84,00 EUR. Die Rechnung enthält 70,59 EUR netto und 13,41 EUR Umsatzsteuer. Der Wagen wurde von 07:30 Uhr am ersten bis 18:10 Uhr am zweiten Tag genutzt und 84 Kilometer gefahren. Beweis: Anlage K6; Zeugnis der Noura Nessel, Mobilität Noura Nessel, Gewerberingel 2, 97082 Lindenquell. Der Kläger benötigte die Fahrten für seinen Arbeitsweg und verfügte über keinen zweiten eigenen Wagen.

Zwischen dem 03. und 09.09.2026 half eine unentgeltliche Fahrgemeinschaft. Hierfür wird nichts verlangt. Diese vorübergehende Hilfe stand an den beiden Reparaturtagen nicht mehr zur Verfügung, wie der Kläger in Anlage K9 konkretisiert. Die kurze Mietdauer und der einfache Ersatzwagen beschränken den Aufwand. Zusätzlicher Nutzungsausfall oder pauschale Mobilitätskosten werden nicht geltend gemacht. Die Summe beträgt folglich 2.927,40 EUR zuzüglich 84,00 EUR, mithin 3.011,40 EUR. Eine Erstattung durch einen Versicherer oder das Unternehmen ist nicht erfolgt.

## 7 Halteverbot und Mitverantwortung

Die Beklagte verweist auf ein für den 31.08.2026 bestelltes mobiles Halteverbot. Der Bestellvermerk vom 28.08.2026 beweist jedoch nicht die tatsächliche Aufstellung und Sichtbarkeit. Der Kläger stellte sein Auto am 02.09.2026 gegen 21:30 Uhr ab und nahm keine entsprechenden Schilder wahr. Seine ursprüngliche Forderung mit dieser zeitlichen Angabe wird als Anlage K7 vorgelegt. Dies ist seine Wahrnehmung, keine Behauptung, dass eine frühere Aufstellung technisch unmöglich sei. Ein Aufstellprotokoll oder zeitbezogenes Foto ist bislang nicht vorgelegt.

Für den Abstellzeitpunkt wird die persönliche Anhörung des Klägers angeregt. Die Beklagte kann den Aufsteller und vorhandene Aufzeichnungen benennen. Eine pauschale Beweisvereitelung wird nicht unterstellt. Sollte ein erkennbares Halteverbot bewiesen werden, wäre dessen Bedeutung für das Belassen des Wagens nach § 254 BGB konkret abzuwägen. Auch ein verbotswidrig abgestellter Wagen darf aber nicht bei bekanntem Standort ohne geeignete Schutzorganisation beschädigt werden. Der erkennbare Konflikt war vor dem Schnitt bereits Gegenstand der städtischen Räumungsbemühungen.

Ein Rechtsmittel, mit dem der Kläger den plötzlich ausgelösten Astkontakt noch rechtzeitig hätte abwenden können, ist nicht ersichtlich. Er hatte keinen vorher bekanntgegebenen Bescheid über eine konkret bevorstehende gefährliche Schnittausführung erhalten. Der Tatbestand des § 839 Abs. 3 BGB wird nicht schon durch die allgemeine Möglichkeit ersetzt, sich irgendwann nach Straßenarbeiten zu erkundigen.

## 8 Zinsen und Verfahrensstand

Es werden allein Prozesszinsen nach §§ 291, 288 Abs. 1 Satz 2 BGB ab dem Tag nach künftiger Zustellung verlangt. Eine bereits erfolgte Zustellung oder ein abgelaufener Antworttermin wird nicht behauptet. Der Kläger hatte um Antwort bis 13.10.2026 gebeten. Das anwaltliche Anspruchsschreiben vom 05.10.2026 ist Anlage K11. Hierauf liegt lediglich die vorläufige Gegenposition der Stadt vom selben Tag, Anlage K12, vor. Dieser Entwurf bleibt deshalb vorbereitend und ist nicht eingereicht.

Die Klägerseite ist weiterhin zu einer außergerichtlichen Klärung anhand von Freigabeverständnis und Aufstellnachweis bereit. Eine Einigung oder Zahlung hat es nicht gegeben. Gegen eine Entscheidung durch den Einzelrichter bestehen keine Bedenken; ein besonderer Videoantrag wird derzeit nicht gestellt. Bei einer späteren Einreichung müssen neue Belege oder Zahlungen berücksichtigt werden, ohne den hier geschilderten Stand rückwirkend als endgültige Ablehnung auszugeben.''', TREE_EXHIBITS)

CASES.append(dict(
    slug='akha-wuerzburg-baumpflege', claim_file='06_Klageentwurf.docx', exhibits=TREE_EXHIBITS,
    notes='Baum: eigene städtische Sicherung plus offene funktionelle Helferwertung. Zusatzanker OLG Hamm06.04.2022–11U143/21Rn25 amtlicher Suchvolltext für §839I2. Keine private Unternehmerhaftung automatisch verdrängt. Frist13.10 offen.',
    attachments={'03_Begleitmail.eml': ['05_Antwort.pdf', '../02_Arbeitsauftrag.docx', '../03_Absperrvermerk.docx']},
    documents=[
mail('01_Mandantenmail.eml', 'Sesam: Parkzeit, Ersatzwagen und Vorbereitung', '''Sehr geehrte Frau von Tann,

bitte erstellen Sie ein weiteres Schreiben und vorsorglich einen Klageentwurf gegen die Stadt, aber reichen Sie noch nichts ein. Die von mir erbetene Antwort bis 13. Oktober steht noch aus. Ich habe 2.927,40 Euro an die Werkstatt und 84 Euro für den Ersatzwagen bezahlt. Eine Erstattung, auch von Astwerk, habe ich nicht erhalten. Die Forderung beträgt weiter 3.011,40 Euro.

Ich stellte den Wagen am 2. September ungefähr um 21:30 Uhr vor Kerbelring 18 ab. Mir fielen keine mobilen Halteverbotsschilder auf. Ich kann aber nicht bezeugen, was dort zwei Tage früher aufgestellt wurde. Ein Klingeln am Unfallmorgen habe ich nicht gehört. Bitte schreiben Sie nicht, niemand habe geklingelt; das kann ich aus meiner Wohnung nicht sicher ausschließen.

Die kostenlose Fahrgemeinschaft vom 3. bis 9. September organisierte mein Kollege Dietmar Wacholder, Sandbirkenweg 7, 97082 Lindenquell. Am 10. und 11. September hatte er frei und fuhr nicht zur Arbeit. Deshalb brauchte ich für diese beiden Tage den Mietwagen. Ich habe kein zweites eigenes Auto. Der Kombi gehört mir privat; als angestellter Buchhändler kann ich keine Vorsteuer abziehen. Eine zusätzliche Entschädigung für die übrigen Tage verlange ich nicht.

Mit freundlichen Grüßen
Leander Sesam''', 'Leander Sesam <leander.sesam@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '10:20'),
mail('02_Ergaenzende_Auskunft.eml', 'Astwerk: Technische Verantwortung und Freigabe', '''Sehr geehrte Frau von Tann,

wir beantworten Ihre Nachfrage ohne Anerkennung einer Ersatzpflicht. Der Bericht unseres Vorarbeiters Ravi König bleibt unverändert. Die Seilführung wurde von unserem Team gewählt. Die Stadt schrieb uns weder eine bestimmte Astgabel noch einen konkreten Anschlagpunkt vor. Herr König verstand die Erklärung um 08:10 Uhr als weitergehende Arbeitsfreigabe, während Herr Zwirn später von einer Begrenzung auf den südlichen Abschnitt sprach. Einen unterschriebenen gemeinsamen Freigabeplan gibt es bei uns nicht.

Unsere Mitarbeiterin am Arbeitskorb hieß Inés Waldner. Sie und Herr König sind über Astwerk Amal Berg GmbH, Scherenbogen 4, 97082 Lindenquell, erreichbar. Frau Waldner kann die Ausführung beschreiben; das vorausgegangene Gespräch hat sie aus ihrer Position nicht vollständig gehört. Dass das Fahrzeug noch in der Bucht stand, war für unser Team sichtbar. Über ein Abschleppen entschied das Team nicht.

Wir erkennen an, dass ein Seil an der Gabel hängen blieb und der Ast ausschwenkte. Welche rechtliche Verantwortung hieraus neben dem städtischen Sicherungsauftrag folgt, muss getrennt bewertet werden. Unsere betriebliche Haftpflichtversicherung ist noch mit der Prüfung befasst. Es gibt bisher weder eine Zahlung noch ein gemeinsames Anerkenntnis mit der Stadt.

Mit freundlichen Grüßen
Amal Berg, Geschäftsführerin''', 'Amal Berg <buero@astwerk-berg.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '11:15'),
mail('03_Begleitmail.eml', 'Sesam: Antwort mit Auftrag und Absperrvermerk', '''Sehr geehrte Frau von Tann,

beigefügt sind unsere heutige Antwort als PDF sowie die unveränderten Kopien des Arbeitsauftrags 26-B47 und des Absperrvermerks vom 4. September. Diese Unterlagen sollen die von Ihnen angesprochene Aufgabenverteilung nachvollziehbar machen. Die fachliche Schnitttechnik war dem Unternehmen überlassen; die Stadt übernahm Freimachung und abschnittsweise Freigabe. Über die Reichweite der tatsächlich gesprochenen Freigabe liegen unterschiedliche Erinnerungen vor.

Wir suchen weiterhin nach dem tatsächlichen Aufstellnachweis für das mobile Halteverbot. Die vorhandene Bestellung vom 28. August allein wird Ihnen nicht als Foto einer Aufstellung ausgegeben. Ein solcher Nachweis liegt dieser Nachricht nicht bei. Für einen gemeinsamen Ortstermin zur Erläuterung der Bereiche würden wir Herrn Zwirn hinzuziehen, ohne damit den damaligen Zustand vollständig rekonstruieren zu können.

Die rechtliche Prüfung durch Frau Seidel betrifft ausschließlich die Stadt. Sie vertritt weder Astwerk noch Ihren Mandanten. Unser heutiges Schreiben ist eine Zwischenstellungnahme; der von Herrn Sesam genannte 13. Oktober ist noch nicht erreicht.

Mit freundlichen Grüßen
Kunigunde Färber, Rechtsstelle''', 'Kunigunde Färber <recht@lindenquell.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '16:30'),
doc('04_Anspruchsschreiben.docx', 'Sesam gegen Stadt – Schaden bei Baumpflege am Kerbelring', '''Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

Stadt Lindenquell – Rechtsstelle
Rathausplatz 1, 97082 Lindenquell bei Würzburg

05.10.2026 · Unser Zeichen VT 26/106

Sehr geehrte Frau Färber,

mein Mandant Leander Sesam hält seine Forderung von 3.011,40 EUR aufrecht. Sie setzt sich aus 2.927,40 EUR bezahlter Reparatur und 84,00 EUR für zwei Mietwagentage zusammen. Bitte nehmen Sie bis zum bereits erbetenen 13. Oktober dazu Stellung. Eine Regulierung ist bislang weder durch Sie noch durch das ausführende Unternehmen erfolgt.

Der Anspruch richtet sich nicht allein darauf, jeden Fehler eines von der Stadt beauftragten Unternehmens der Stadt zuzurechnen. Nach dem Auftrag verblieben Freimachung, Absperrung und abschnittsweise Freigabe bei Ihnen. Der Wagen stand sichtbar im betroffenen Bereich. Die unterschiedliche Erinnerung von Herrn Zwirn und Herrn König zur Freigabe verlangt daher eine konkrete Erklärung, wie die Grenze des erlaubten Arbeitsbereichs vor Beginn vermittelt und abgesichert wurde.

Bitte übermitteln Sie Auftrag und Absperrvermerk sowie den tatsächlichen Aufstellnachweis des behaupteten Halteverbots. Mein Mandant sah beim Abstellen am 2. September gegen 21:30 Uhr keine mobilen Schilder. Er behauptet nicht, aus eigener Wahrnehmung die Situation am 31. August zu kennen. Eine Bestellung der Schilder beantwortet die Frage ihrer späteren Sichtbarkeit nicht.

Der Kombi wurde am 10. und 11. September repariert. Die vorherige kostenlose Fahrgemeinschaft war an diesen beiden Tagen nicht verfügbar. Mein Mandant verlangt deshalb nur die beiden nachgewiesenen Miettage, keinen zusätzlichen Nutzungsausfall. Auf eine bestimmte Deckung Ihrer Stadt oder des Unternehmens stützt er seinen Anspruch nicht. Eine sachbezogene Klärung der Außenschuld bleibt unabhängig von internen Versicherungsfragen möglich.

Mit freundlichen Grüßen
Leonie von Tann
Rechtsanwältin''', 'letter', LAWYER, CITY),
doc('05_Antwort.docx', 'Stadt Lindenquell – Freigabe und Unternehmerverantwortung', '''Stadt Lindenquell – Rechtsstelle
Rathausplatz 1, 97082 Lindenquell bei Würzburg

Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

05.10.2026 · Zeichen LQ-R 26/B47

Sehr geehrte Frau von Tann,

die von Ihnen beschriebene Aufgabenteilung trifft im Ausgangspunkt zu. Wir haben die Freimachung des Parkraums übernommen. Nach Erinnerung unseres Mitarbeiters Herrn Zwirn war um 08:10 Uhr jedoch ausschließlich der bereits freie südliche Abschnitt freigegeben. Wir haben das Unternehmen nicht angewiesen, über dem noch abgestellten Wagen weiterzuarbeiten. Die Seilführung wurde vom Fachunternehmen eigenständig gewählt.

Wir müssen deshalb klären, ob ein Missverständnis über die Freigabe, ein Ausführungsfehler oder beides für den Schaden ursächlich war. Ein kommunaler Auftrag macht ein selbstständig arbeitendes Unternehmen nicht ohne Weiteres zum haftungsrechtlichen Verwaltungshelfer. Ebenso wenig erklären wir damit jede eigene Sicherungspflicht der Stadt für erledigt. Den Arbeitsauftrag und den Vermerk stellen wir Ihnen zur Verfügung.

Das mobile Halteverbot war für den 31. August bestellt. Der tatsächliche Aufstellnachweis wird noch gesucht. Bis zu dessen Auffinden können wir aus der Bestellung allein keine sichere Aussage ableiten, was Ihr Mandant am 2. September sehen musste. Sollte eine rechtzeitige erkennbare Aufstellung nachweisbar sein, behalten wir uns vor, den Abstellvorgang bei der Verantwortungsverteilung zu berücksichtigen.

Zu den beiden Mietwagentagen benötigen wir keine pauschale Forderung über den gesamten Ausfallzeitraum. Ihre Begrenzung und die Angaben zur Fahrgemeinschaft sind in die Prüfung aufgenommen. Eine endgültige Zahlungsentscheidung oder Deckungszusage liegt heute nicht vor. Wir wollen Ihnen bis zum 13. Oktober erneut schreiben und bitten das Unternehmen parallel um eine präzise Darstellung des Freigabegesprächs.

Mit freundlichen Grüßen
Kunigunde Färber
Rechtsstelle der Stadt Lindenquell''', 'letter', CITY, LAWYER),
doc('06_Klageentwurf.docx', 'Klageentwurf Sesam gegen Stadt Lindenquell', TREE_CLAIM, 'claim', LAWYER, 'Landgericht Würzburg')
]))

HOLE_EXHIBITS = [
    exhibit('K1', '02_Schadenmeldung.docx', 'Schadenmeldung Oliveira vom 10.09.2026 mit Geschwindigkeit und Fahrspur.'),
    exhibit('K2', '03_Strasse_und_Kontrollen.docx', 'Straßenmerkmale, Kontrollplan und Befahrung vom 27.08.2026.'),
    exhibit('K3', '04_Meldung_und_Reparatur.docx', 'Bürgerhinweis vom 08.09., Bearbeitungszeiten und Messung am 10.09.2026.'),
    exhibit('K4', '05_Werkstattbefund.docx', 'Frischer Felgenschaden und älterer Reifenriss als getrennte Befunde.'),
    exhibit('K5', '06_Reparaturrechnung.docx', 'Bezahlte Werkstattrechnung mit getrennten Positionen.'),
    exhibit('K6', '07_Abschlepprechnung.docx', 'Abschleppbeleg und dokumentierte Nichtfahrbereitschaft.'),
    exhibit('K7', '08_Forderung.eml', 'Ursprüngliche Forderung über 920,00 EUR und Hinweis auf den alten Reifenriss.'),
    exhibit('K8', 'schriftverkehr-und-klage/01_Mandantenmail.eml', 'Begrenzung auf 741,50 EUR und Bestätigung der bisherigen Angaben.'),
    exhibit('K9', 'schriftverkehr-und-klage/02_Ergaenzende_Auskunft.eml', 'Ergänzende zeitliche Wahrnehmung der Anwohnerin Pflaum.'),
    exhibit('K10', 'schriftverkehr-und-klage/04_Anspruchsschreiben.pdf', 'Reduzierte Forderung und Nachfrage zum Meldesystem.'),
    exhibit('K11', 'schriftverkehr-und-klage/05_Antwort.pdf', 'Städtische Einwendungen zu Kontrollpflicht, Erkennbarkeit und Altschaden.'),
]

HOLE_CLAIM = claim('Celestino Oliveira, Kornellenpfad 9, 97082 Lindenquell bei Würzburg', CITY,
    'Landgericht Würzburg', '741,50', 'VT 26/107', '''## 1 Anträge

Namens und in Vollmacht des Klägers wird beantragt, die Beklagte zu verurteilen, an den Kläger 741,50 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem auf die Zustellung der Klage folgenden Tag zu zahlen. Ferner wird beantragt, der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Der Antrag umfasst die neue Felge mit 499,80 EUR brutto, die Achsprüfung mit 59,50 EUR brutto und das Abschleppen mit 182,20 EUR brutto. Der neue Reifen und die gesonderte Montageposition sind bewusst nicht Gegenstand der Klage. Die ursprüngliche außergerichtliche Summe von 920,00 EUR wird damit um 178,50 EUR vermindert. Die ursprüngliche Forderung ist Anlage K7; die ausdrückliche Begrenzung durch den Kläger vom 05.10.2026 ist Anlage K8.

## 2 Anspruch und Zuständigkeit

Der Kläger verlangt Ersatz wegen der Beschädigung seines Privatwagens am 09.09.2026 gegen 06:50 Uhr auf dem Hagebuttenweg vor Haus 24. Die Beklagte ist für diese gewidmete Ortsstraße einschließlich ihrer Verkehrssicherung zuständig. Der Hagebuttenweg ist etwa 340 Meter lang und 5,4 Meter breit; er erschließt Wohnhäuser und kleinere Gewerbebetriebe. Es gilt eine Geschwindigkeitsbegrenzung von 30 km/h. Die Straßenunterlagen der Beklagten weisen diese Merkmale aus, Anlage K2.

Der geltend gemachte Amtshaftungsanspruch folgt aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG und Art. 9 Abs. 5 BayStrWG. Für ihn ist gemäß § 71 Abs. 2 Nr. 2 GVG unabhängig von der geringen Forderungshöhe das Landgericht zuständig. Der Schadensort liegt im Bezirk Würzburg und begründet die örtliche Zuständigkeit nach § 32 ZPO. Eine vertragliche Beschaffenheitsgarantie für eine vollkommen ebene Fahrbahn wird nicht behauptet.

## 3 Fahrt und Schadensereignis

Der Kläger befuhr den Hagebuttenweg am 09.09.2026 gegen 06:50 Uhr. Es war bedeckt, die Fahrbahn feucht und das Tageslicht noch schwach. Ein Lieferwagen kam entgegen. Der Kläger hielt sich deshalb weiter rechts, ohne nach seiner Wahrnehmung den Bordstein zu berühren. Das rechte Vorderrad geriet in die beschädigte Fläche vor Haus 24. Er hörte einen harten Schlag. Etwa zwanzig Meter weiter hielt er an; der Reifen verlor Luft und an der Felge war eine Verformung erkennbar. Ein Ersatzrad führte er nicht mit. Um 07:02 Uhr rief er den Abschleppdienst.

Die Geschwindigkeit hat der Kläger von Beginn an nur auf ungefähr 30 bis 35 km/h geschätzt. Er korrigiert diese Schätzung nicht nachträglich auf einen scheinbar sicheren Wert unterhalb der zulässigen Grenze. Eine Kameraaufzeichnung oder das Kennzeichen des entgegenkommenden Fahrzeugs liegt nicht vor. Beweis für den unmittelbaren Zustand nach dem Ereignis: Abschlepprechnung mit Einsatzangaben, Anlage K6; Zeugnis des Mehmet Seitz, Abschleppdienst Selma Sauer, Schlehentor 2, 97082 Lindenquell. Dieser Zeuge sah nicht die Durchfahrt durch das Loch, sondern erst das liegengebliebene Fahrzeug.

Zum eigenen Fahrablauf wird die persönliche Anhörung des Klägers angeregt. Seine zeitnahe Schadenmeldung vom 10.09.2026 ist Anlage K1. Die konkrete frische Felgenverformung und der Werkstattbefund sind weitere Anknüpfungstatsachen. Eine neutrale Augenzeugin des Radkontakts wird nicht erfunden. Für den Zusammenhang zwischen einem harten Fahrbahnkantenkontakt und dem dokumentierten frischen Felgenschaden wird ein kraftfahrzeugtechnisches Sachverständigengutachten angeboten.

## 4 Zustand der Stelle und zeitliche Erkenntnisse

Bei der planmäßigen langsamen Kontrollbefahrung am 27.08.2026 um 09:20 Uhr vermerkte der Mitarbeiter Alfons Degen eine flache ältere Flickstelle ohne offenes Loch. Er hielt dort nicht an und nahm keine Maße. Die nächste Regelkontrolle war für den 10.09.2026 vorgesehen. Der interne Plan sieht etwa zweiwöchentliche Kontrollen und zusätzliche Reaktionen auf Meldungen vor. Beweis: Anlage K2; Zeugnis des Alfons Degen und der Brunhild Späth, beide zu laden über Stadt Lindenquell, Straßenunterhalt, Amselspange 2, 97082 Lindenquell.

Am 08.09.2026 um 16:42 Uhr ging über das städtische Serviceformular die Nachricht der Anwohnerin Adelgunde Pflaum ein. Sie wies auf das Aufbrechen der alten Flickstelle vor Haus 24 und darauf hin, dass sie der Stelle bereits am Vortag mit dem Fahrrad ausgewichen war. Die Nachricht enthielt kein Foto und keine gemessene Tiefe. Sie wurde am 09.09.2026 um 07:18 Uhr geöffnet und um 07:24 Uhr zugeordnet. Der Unfall lag davor. Der Bearbeitungsvermerk nennt zunächst die nächste Runde. Erst um 11:06 Uhr wurde der Fahrzeugschaden telefonisch gemeldet.

Beweis: Eingang und Bearbeitungsverlauf, Anlage K3; Zeugnis der Sibel Auer, zu laden über die Beklagte, Rathausplatz 1, 97082 Lindenquell. Die Klägerseite setzt den Öffnungszeitpunkt nicht ohne Weiteres mit dem frühestmöglichen organisatorischen Zugriff gleich. Umgekehrt wird auch nicht behauptet, eine Meldung müsse unabhängig von Inhalt und Tageszeit innerhalb weniger Minuten zu einer Reparatur führen. Entscheidend ist, wie solche konkreten Gefahrenhinweise gewichtet und erforderlichenfalls einer erreichbaren Stelle zugeleitet werden.

Frau Pflaum hat am 05.10.2026 ergänzt, sie habe am 07.09.2026 am Nachmittag offene, unregelmäßige Ränder gesehen und mit dem Fahrrad Abstand gehalten. Am folgenden Nachmittag habe Wasser in der Vertiefung gestanden. Sie habe weder einen Zollstock benutzt noch ein Foto aufgenommen. Beweis: Anlage K9; Zeugnis der Adelgunde Pflaum, Hagebuttenweg 22, 97082 Lindenquell. Ihr Beweisantritt betrifft das Bestehen einer bereits offenen Vertiefung vor dem Unfall, nicht die exakten Maße am Unfallmorgen.

Am 10.09.2026 gegen 08:10 Uhr maß der Reparaturtrupp ungefähr 55 Zentimeter Länge, 38 Zentimeter Breite und acht Zentimeter Tiefe, etwa 25 Zentimeter vom Fahrbahnrand entfernt. Die Stelle war inzwischen trocken. Nach Sicherung wurde sie bis 09:05 Uhr ausgebessert. Lose Teile wurden entsorgt. Diese Messung ist ein späterer Befund. Sie beweist nicht automatisch dieselbe Tiefe am 09.09.2026 um 06:50 Uhr und erst recht nicht einen gleichartigen Zustand seit der Kontrolle vom 27.08.2026.

## 5 Pflichtverletzung und Vermeidbarkeit

Die Beklagte musste die Straße im Rahmen des nach ihrer Art, Bedeutung und tatsächlichen Gefahrenlage Zumutbaren überwachen und auf hinreichend konkrete Hinweise reagieren. Ein allgemeiner Anspruch auf eine schlaglochfreie Ortsstraße besteht nicht. Hier ging es jedoch um eine aufgebrochene Flickstelle im gewöhnlich befahrenen rechten Bereich, die bereits am Vortag konkret gemeldet und zuvor von einer Radfahrerin umfahren worden war. Eine solche Meldung erforderte eine inhaltliche Dringlichkeitsprüfung; bloße Einreihung in die nächste Regelrunde genügte nach Auffassung des Klägers nicht.

Der Vorwurf betrifft vor allem die Organisation der Meldungsbearbeitung vor dem morgendlichen Verkehr. Die Klägerseite macht sich die erkennbare Angabe zu eigen, dass eine bereits offene Kante bestand, und hält eine zeitnahe Besichtigung oder vorläufige Warnung für erforderlich. Ob eine zumutbar eingerichtete Bearbeitung nach Eingang um 16:42 Uhr noch am Abend oder jedenfalls vor 06:50 Uhr des Folgetags zu wirksamer Sicherung geführt hätte, muss anhand der tatsächlichen Dienst- und Weiterleitungsabläufe festgestellt werden. Die Beklagte hat dazu bislang nur die späteren Öffnungs- und Zuordnungszeiten mitgeteilt.

Das ist eine wesentliche Beweisfrage und wird nicht durch das bloße spätere Reparaturdatum übersprungen. Der Kläger bietet das Zeugnis der zuständigen Mitarbeiterinnen Auer und Späth zum vorhandenen Meldeweg, seinen Eingangszeiten und einer vorgesehenen Weiterleitung dringender Hinweise an. Er behauptet keinen bereits gesicherten persönlichen Kenntnisstand eines bestimmten Mitarbeiters am Vorabend. Ein gerichtlicher Hinweis wird erbeten, falls der vorhandene Vortrag zur organisatorisch möglichen Reaktion nicht ausreicht. Eine allgemeine Pflicht zur Offenlegung sämtlicher städtischer Unterlagen wird nicht beantragt.

Auch der zweiwöchentliche Kontrollplan ist kein gesetzlicher Mindeststandard und kein automatischer Entlastungsbeweis. Aus dem Bericht über eine flache Flickstelle am 27.08.2026 allein wird keine damals schon erkennbare akute Gefahr hergeleitet. Sollte die Zeugin Pflaum nur eine sehr kurzfristige Veränderung bestätigen können und eine frühere Reaktion auf ihre Meldung nicht zumutbar gewesen sein, betrifft dies gerade den geltend gemachten Pflicht- und Kausalitätsnachweis. Der Anspruch wird nicht hilfsweise auf einen unbekannten baulichen Herstellungsfehler gestützt.

OLG Hamm, Urteil vom 15.11.2013 – 11 U 52/12, Rn. 18–28, insbesondere Rn. 20–25, zeigt die notwendige Trennung von Kontrollfehler, zeitlicher Entstehung und Schadensvermeidbarkeit. Die dortige Autobahn- und Schachtkonstellation liefert weder einen festen Kontrollabstand noch einen Zentimetergrenzwert für diese Ortsstraße. Der Kläger beruft sich ausschließlich auf den methodischen Zusammenhang zwischen erkennbarer konkreter Gefahr, zumutbarer Reaktion und dem hier geltend gemachten Radschaden.

## 6 Schaden und Abgrenzung des alten Reifens

Die Werkstatt Radwerk Raban Rost stellte eine frische Verformung an der Innenseite der rechten Vorderfelge fest. Dieser Befund ist mit einem kräftigen Kantenkontakt vereinbar. Zugleich dokumentierte die Werkstatt einen schon bei einer Untersuchung am 21.07.2026 vorhandenen, ungefähr 18 Millimeter langen Seitenwandriss am Reifen. Damals war bereits zum Austausch geraten worden. Der Kläger verschweigt diesen Vorschaden nicht. Die bloße neue Rechnung über Radarbeiten beweist daher keinen vollständig neuen Reifenschaden.

Beweis: Werkstattbefund, Anlage K4; Zeugnis des Raban Rost, Radwerk Raban Rost, Kelterbogen 5, 97082 Lindenquell. Felge und Reifen sind bis in den Oktober hinein aufbewahrt. Zum frischen Charakter der Felgenverformung, ihrem Zusammenhang mit dem geschilderten Kontakt und der hierdurch verursachten fehlenden Weiterfahrmöglichkeit wird ein technisches Sachverständigengutachten angeboten. Der alte Reifenriss darf nicht ohne Untersuchung als neue Lochfolge zugerechnet werden; ebenso wenig erklärt er ohne Weiteres die neue Verformung der Felge.

Die Werkstattrechnung beträgt 737,80 EUR brutto. Darin enthalten sind netto 420,00 EUR für die Felge, 120,00 EUR für den Reifen, 30,00 EUR Montage und 50,00 EUR Achsprüfung. Der Kläger bezahlt diese Rechnung, beschränkt den Antrag aber auf die Felge einschließlich 79,80 EUR Umsatzsteuer, also 499,80 EUR, und die durch den harten Stoß veranlasste Achsprüfung einschließlich 9,50 EUR Umsatzsteuer, also 59,50 EUR. Der Reifen zu 142,80 EUR brutto bleibt wegen des Austauschbedarfs aus dem Vorschaden außen vor.

Auch die Montageposition von 35,70 EUR brutto wird zur Vermeidung eines Streits über ohnehin erforderliche Reifenwechselarbeiten nicht eingeklagt. Dies ist eine Begrenzung der verlangten Positionen, keine Behauptung, die Werkstatt habe nicht montiert. Die Rechnung mit Zahlungshinweis ist Anlage K5. Die Reparatur wurde am 10.09.2026 freigegeben und der Wagen am 11.09.2026 um 16:15 Uhr abgeholt. Der Kläger nutzt ihn privat und hat keinen Vorsteuerabzug. Es werden deshalb tatsächlich entstandene Bruttobeträge und keine nur geschätzte Umsatzsteuer verlangt.

Hinzu kommen 182,20 EUR für den Abschleppdienst Selma Sauer. Der Wagen wurde nach dem Luftverlust und der erkennbar beschädigten Felge über vier Kilometer zur Werkstatt gebracht. Die Rechnung weist 153,11 EUR netto und 29,09 EUR Umsatzsteuer aus; bezahlt wurde sie am 12.09.2026. Beweis: Anlage K6 und Zeugnis Seitz. Entscheidend ist die nach dem Kontakt eingetretene Nichtfahrbereitschaft. Falls die Beklagte behauptet, allein der alte Reifenriss habe diese verursacht, ist dies anhand des technischen Befunds und des unmittelbar beobachteten Zustands zu klären.

Die verlangte Summe beträgt 499,80 EUR zuzüglich 59,50 EUR zuzüglich 182,20 EUR, insgesamt 741,50 EUR. Es werden keine Mietwagenkosten, kein Nutzungsausfall, keine Pauschale und keine vorgerichtlichen Anwaltskosten verlangt. Eine Ersatzleistung Dritter liegt nach der Erklärung des Klägers nicht vor.

## 7 Geschwindigkeit, Sichtbarkeit und Eigenanteil

Die Beklagte beruft sich in ihrer Antwort vom 05.10.2026, Anlage K11, auf die geschätzten 30 bis 35 km/h, die rechte Fahrspur und den bekannten Reifenriss. Der Kläger hält dem entgegen, dass er eine Begegnung auf einer schmalen Ortsstraße bewältigte und eine wassergefüllte Vertiefung in schwachem Morgenlicht nicht in ihrer Tiefe erkennen konnte. Daraus folgt aber kein Freibrief für eine beliebige Geschwindigkeit. Ob ein langsameres Fahren den konkreten Felgenstoß vermieden oder vermindert hätte, ist im Rahmen von § 254 BGB gegebenenfalls sachverständig zu beurteilen.

Der Kläger verlangt zunächst den vollen Betrag der eng begrenzten Positionen. Er verschweigt nicht, dass ein festgestellter vermeidbarer Fahrfehler oder ein ursächlicher Zustand des Reifens zu einer Kürzung führen kann. Unabhängig von einem persönlichen Fahrfehler ist eine konkret mitwirkende Betriebsgefahr des eigenen Fahrzeugs nach § 254 BGB in Verbindung mit § 7 StVG zu prüfen; auch hierfür bedarf es feststellbarer unfallursächlicher Umstände. Vgl. OLG Hamm, Urteil vom 06.04.2022 – 11 U 143/21, Rn. 27–30. Die dortige Quote wird nicht auf diesen Sachverhalt übertragen. Eine Quote wird nicht allein aus der Überschreitungsspanne oder dem Vorhandensein eines Kfz gebildet. Erforderlich bleiben tatsächlicher Fahrablauf, Erkennbarkeit der Vertiefung und konkrete Auswirkung auf die geltend gemachten Schäden. Der spätere trockene Reparaturbefund beantwortet die Sichtverhältnisse des feuchten Unfallmorgens nicht vollständig.

## 8 Prozesszinsen und Stand der Vorbereitung

Der Zinsantrag beruht auf §§ 291, 288 Abs. 1 Satz 2 BGB und beginnt erst am Tag nach künftiger Zustellung. Ein schon eingetretener Verzug wird nicht geltend gemacht. Die erbetene städtische Antwort bis 14.10.2026 steht am 05.10.2026 noch aus. Die Zwischenantwort enthält Einwendungen, aber keine Zahlung und keine abschließend erklärte Regulierung. Dieser Entwurf ist nicht eingereicht.

Das anwaltliche Schreiben vom 05.10.2026, Anlage K10, konkretisiert sowohl den reduzierten Betrag als auch die Nachfrage zur Meldungsbearbeitung. Die weitere außergerichtliche Aufklärung konzentriert sich auf den zeitlichen Zustand der Stelle und die zumutbare Bearbeitung des konkreten Hinweises. Eine Einigung wurde bislang nicht erzielt; ein sachbezogenes Gespräch bleibt möglich. Gegen die Entscheidung durch den Einzelrichter bestehen keine Bedenken. Ein besonderer Antrag zur Videoverhandlung wird derzeit nicht gestellt. Vor einer späteren Einreichung sind insbesondere neue Angaben zur Meldungsorganisation und eine fachliche Einschätzung der Schadensursache zu berücksichtigen.''', HOLE_EXHIBITS)

CASES.append(dict(
    slug='akha-wuerzburg-schlagloch', claim_file='06_Klageentwurf.docx', exhibits=HOLE_EXHIBITS,
    notes='Bewusst beweisriskante Amtshaftung: Reaktionsmöglichkeit zwischen08.09.16:42und09.09.06:50 nicht erfunden. Kein allgemeiner Kontrollstandard. Anspruch741,50; Altreifen142,80 und Montage35,70 ausdrücklich ausgeschlossen. Frist14.10 offen.',
    attachments={'03_Begleitmail.eml': ['05_Antwort.pdf', '../03_Strasse_und_Kontrollen.docx', '../04_Meldung_und_Reparatur.docx']},
    documents=[
mail('01_Mandantenmail.eml', 'Oliveira: Begrenzung der Forderung und Geschwindigkeit', '''Sehr geehrte Frau von Tann,

bitte bereiten Sie das anwaltliche Schreiben und einen Klageentwurf vor, ohne schon Klage einzureichen. Ich möchte die angekündigte Prüfung und die Antwort bis 14. Oktober abwarten. Wir sollten den neuen Reifen nicht von der Stadt verlangen: Auf den Seitenwandriss war ich im Juli schon hingewiesen worden. Auch die 35,70 Euro für Montage möchte ich in der Klage nicht zum eigenen Nebenstreit machen.

Damit bleiben die Felge mit 499,80 Euro, die Achsprüfung mit 59,50 Euro und das Abschleppen mit 182,20 Euro, zusammen 741,50 Euro. Ich habe sämtliche Rechnungen bezahlt, nichts abgetreten und keine Erstattung bekommen. Das Auto ist mein privates Fahrzeug. Ich kann keine Vorsteuer abziehen.

An meiner Schätzung von 30 bis 35 km/h halte ich fest. Ich habe nicht genau auf den Tacho geschaut und kann jetzt keine bessere Zahl liefern. Der Lieferwagen kam entgegen; ein Kennzeichen habe ich nicht. Ich bin nach rechts gegangen, aber nach meiner Erinnerung nicht gegen den Bordstein. Ob ich das Loch früher hätte erkennen können, lässt sich für mich im Nachhinein schwer beurteilen. Bitte stellen Sie die Messung des Trupps am nächsten Tag nicht als meine eigene Messung am Unfallmorgen dar.

Mit freundlichen Grüßen
Celestino Oliveira''', 'Celestino Oliveira <celestino.oliveira@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '10:25'),
mail('02_Ergaenzende_Auskunft.eml', 'Pflaum: Was ich vor der Meldung gesehen habe', '''Sehr geehrte Frau von Tann,

Frau Auer hat mich nach meiner Meldung zum Hagebuttenweg gefragt. Sie können diese Antwort auch für Herrn Oliveira verwenden. Meine Anschrift lautet Adelgunde Pflaum, Hagebuttenweg 22, 97082 Lindenquell. Am Montag, dem 7. September, am Nachmittag fuhr ich mit dem Rad an Haus 24 vorbei. An der alten Flickstelle waren offene, unregelmäßige Ränder zu sehen. Ich hielt mit dem Vorderrad Abstand. Es war mehr als nur eine andersfarbige Asphaltfläche.

Am Dienstagnachmittag sah ich Wasser in der Vertiefung und meldete die Stelle um 16:42 Uhr im Serviceformular. Ich habe weder Tiefe noch Länge gemessen. Eine genaue Handspanne möchte ich nachträglich nicht schätzen. Fotos habe ich nicht gemacht. Ich kann auch nicht sagen, ob über Nacht weitere Stücke herausbrachen. Den Unfall am Mittwochmorgen habe ich nicht gesehen; ich erfuhr erst später davon.

Mir ist wichtig, dass meine Nachricht richtig zeitlich eingeordnet wird. Dass ich am Montag auswich, bedeutet nicht, dass die Stelle schon bei der städtischen Augustkontrolle so aussah. Wer das Formular am Dienstag hätte lesen können und wie dringende Meldungen intern weitergeleitet werden, weiß ich ebenfalls nicht.

Mit freundlichen Grüßen
Adelgunde Pflaum''', 'Adelgunde Pflaum <adelgunde.pflaum@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '11:35'),
mail('03_Begleitmail.eml', 'Oliveira: Zwischenantwort und Kontrollunterlagen', '''Sehr geehrte Frau von Tann,

anbei finden Sie unsere heutige Antwort als PDF sowie die unveränderten Unterlagen zu Straße und Kontrollen und zu Meldung und Reparatur. Wir haben die neue Forderung über 741,50 Euro vermerkt. Dass Sie Reifen und Montage ausklammern, erleichtert die Betragszuordnung, ersetzt aber nicht die Prüfung des Zusammenhangs zwischen Fahrbahnzustand, Felgenschaden und Abschleppen.

Die genauen Maße wurden erst am 10. September aufgenommen. Eine Messung oder ein Foto vom Unfallmorgen liegt der Stadt nicht vor. Die Nachricht von Frau Pflaum ging am Vorabend um 16:42 Uhr ein, wurde um 07:18 Uhr geöffnet und um 07:24 Uhr zugeordnet. Zur allgemeinen Weiterleitung außerhalb der Außendienstzeit soll die zuständige Stelle gesondert berichten; eine fertige Organisationsbeschreibung übersenden wir heute nicht.

Herr Mehmet Seitz, der den Wagen abholte, ist nach Auskunft des Abschleppbetriebs über Abschleppdienst Selma Sauer, Schlehentor 2, 97082 Lindenquell erreichbar. Er hat keinen Unfallhergang aus eigener Anschauung gemeldet. Frau Rechtsanwältin Seidel prüft unsere Position; eine abschließende Antwort ist bis zum genannten 14. Oktober noch möglich.

Mit freundlichen Grüßen
Kunigunde Färber, Rechtsstelle''', 'Kunigunde Färber <recht@lindenquell.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '16:40'),
doc('04_Anspruchsschreiben.docx', 'Oliveira gegen Stadt – Konkretisierte Forderung und Meldungsbearbeitung', '''Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

Stadt Lindenquell – Rechtsstelle
Rathausplatz 1, 97082 Lindenquell bei Würzburg

05.10.2026 · Unser Zeichen VT 26/107

Sehr geehrte Frau Färber,

ich vertrete Herrn Celestino Oliveira wegen des Radschadens vom 9. September im Hagebuttenweg. Die geltend gemachte Summe wird auf 741,50 EUR begrenzt. Verlangt werden 499,80 EUR für die Felge, 59,50 EUR für die Achsprüfung und 182,20 EUR für das Abschleppen. Der im Juli bereits beanstandete Reifen und die Montageposition werden nicht in den vorbereiteten Zahlungsantrag aufgenommen.

Der Werkstattbefund unterscheidet den alten Seitenwandriss von der frischen Felgenverformung. Diese Trennung sollte auch Ihre Prüfung tragen. Mein Mandant behauptet weder einen von Anfang an neuwertigen Reifen noch eine bereits belegte Unfallursächlichkeit jeder Rechnungszeile. Felge und Reifen werden bei der Werkstatt zur möglichen Untersuchung aufbewahrt.

Für die Haftung kommt es auf den Zustand vor dem Unfall und die zumutbare Bearbeitung der Meldung vom Vorabend an. Frau Pflaum hat nun erläutert, dass sie bereits am 7. September offene Ränder sah. Exakte Maße nennt sie nicht. Bitte teilen Sie mit, wie konkrete Gefahrenhinweise nach Ende des Außendiensts gesichtet und nötigenfalls weitergeleitet werden. Allein aus dem späteren Öffnen um 07:18 Uhr ergibt sich noch nicht, ob zuvor eine zumutbare Sicherung möglich gewesen wäre.

Mein Mandant hält an seiner ungefähren Geschwindigkeit von 30 bis 35 km/h fest. Er verschweigt dieses Gegenargument nicht. Die Messung vom 10. September ist ein späterer Befund und darf die fehlende Messung am Unfallmorgen nicht ersetzen. Ich bitte um eine sachbezogene Antwort bis zum bereits erbetenen 14. Oktober und bin für eine außergerichtliche Klärung der noch offenen Kausalitätsfragen offen.

Mit freundlichen Grüßen
Leonie von Tann
Rechtsanwältin''', 'letter', LAWYER, CITY),
doc('05_Antwort.docx', 'Stadt Lindenquell – Kontrollrhythmus, Reaktionszeit und Vorschaden', '''Stadt Lindenquell – Rechtsstelle
Rathausplatz 1, 97082 Lindenquell bei Würzburg

Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

05.10.2026 · Zeichen LQ-R 26/H24

Sehr geehrte Frau von Tann,

Ihre Beschränkung auf 741,50 EUR ist vermerkt. Eine Ersatzpflicht können wir derzeit nicht anerkennen. Der Hagebuttenweg wurde am 27. August kontrolliert; dokumentiert ist eine flache ältere Flickstelle ohne offenes Loch. Die Regelkontrolle war für den 10. September vorgesehen. Ob vor dem Unfall eine besondere Kontroll- oder Sicherungsmaßnahme geboten war, hängt von der zwischenzeitlichen Entwicklung und vom Inhalt der Meldung ab.

Frau Pflaums Hinweis enthielt keine Maße und kein Foto. Er ging um 16:42 Uhr nach Ende des regulären Außendiensts ein und wurde am nächsten Morgen bearbeitet. Wir prüfen Ihre Nachfrage zur Weiterleitung dringender Meldungen. Dass der Unfall schon um 06:50 Uhr geschah, macht eine angemessene Reaktionszeit zu einer wesentlichen Frage. Eine Meldung am Vorabend belegt für sich allein noch nicht, dass die Stadt die Stelle vor diesem Zeitpunkt hätte sichern müssen.

Ebenso müssen Sichtbarkeit, Fahrgeschwindigkeit und technische Ursache geklärt werden. Ihr Mandant schätzt bis zu 35 km/h bei erlaubten 30 km/h und kannte den früheren Reifenriss. Auch wenn der Reifenpreis nicht mehr verlangt wird, kann sein Zustand für Luftverlust und Abschleppbedarf relevant bleiben. Wir behaupten damit nicht, der alte Riss erkläre automatisch die frische Felgenverformung.

Die später gemessenen acht Zentimeter Tiefe sind kein rückwirkend gesicherter Unfallbefund. Wir übersenden die vorhandenen Aufzeichnungen und wollen bis zum 14. Oktober weiter Stellung nehmen. Ein fertiges Ergebnis der Organisationsprüfung oder eine Deckungszusage gibt es heute nicht. Eine gemeinsame technische Besichtigung der erhaltenen Teile erscheint sinnvoll, wenn sie auf die konkreten offenen Fragen beschränkt wird.

Mit freundlichen Grüßen
Kunigunde Färber
Rechtsstelle der Stadt Lindenquell''', 'letter', CITY, LAWYER),
doc('06_Klageentwurf.docx', 'Klageentwurf Oliveira gegen Stadt Lindenquell', HOLE_CLAIM, 'claim', LAWYER, 'Landgericht Würzburg')
]))

# Nur Quellenmetadaten für die Prüfung; keine zusätzliche Akten- oder Briefdatei.
LEGAL_SOURCES = [
    {'source': 'kommunale-haftpflicht/references/alltagsfaelle-bayern.md', 'checked': '05.10.2026', 'scope': 'Amtliche Primäranker AA01, AA04, AA05, AA06, AA10 und materielle Normen.'},
    {'source': 'https://www.gesetze-im-internet.de/gvg/__23.html', 'checked': '05.10.2026', 'scope': 'Amtsgericht bis10.000EUR; GmbH-Fall.'},
    {'source': 'https://www.gesetze-im-internet.de/gvg/BJNR005130950.html', 'checked': '05.10.2026', 'scope': 'GVG; besondere LG-Zuständigkeit zusätzlich durch bestehende Referenz verifiziert.'},
    {'source': 'https://www.gesetze-im-internet.de/zpo/__253.html', 'checked': '05.10.2026', 'scope': 'Rubrum, bestimmte Anträge, Klagegegenstand und Verfahrensangaben.'},
    {'source': 'https://www.gesetze-im-internet.de/zpo/__32.html', 'checked': '05.10.2026', 'scope': 'Gerichtsstand der unerlaubten Handlung; amtlicher Suchtext.'},
    {'source': 'https://www.gesetze-im-internet.de/bgb/__291.html', 'checked': '05.10.2026', 'scope': 'Prozesszinsen; amtlicher Suchtext.'},
    {'source': 'https://nrwe.justiz.nrw.de/pdfdownload/downloadEntscheidung.php?entscheidung=%2Fnrwe%2Folgs%2Fhamm%2Fj2022%2F11_U_143_21_Urteil_20220406.html', 'checked': '05.10.2026', 'scope': 'OLG Hamm06.04.2022–11U143/21Rn25; amtlicher Suchvolltext: allgemeine Verkehrssicherung und §839I2, kein Übertrag NRW-Straßenrecht. Rn27–30 zur konkreten Betriebsgefahr zusätzlich durch unabhängige amtliche HTML-Prüfung des Rechtsagenten bestätigt.'},
]
