"""Zusätzlicher Schriftverkehr und nicht eingereichte Klageentwürfe für vier Akten.

Nur Datenquelle. Alte Originalunterlagen bleiben unverändert. Briefe werden vom
Builder ausschließlich als PDF veröffentlicht; die hier genannten DOCX-Dateien
sind Zwischenquellen. Herkunft und unterschiedliche Mandatsrollen stehen im README.
"""


def document(file, title, day, kind, body, sender=None, recipient=None):
    result = dict(file=file, title=title, date=day, kind=kind, body=body.strip())
    if sender:
        result['sender'] = sender
    if recipient:
        result['recipient'] = recipient
    return result


def exhibit(number, source, description):
    return dict(label=f'K{number}', source=source, description=description)


CASES = []

CASES.append(dict(
    slug='akha-wuerzburg-glatteis',
    attachments={},
    claim_file='16_Klageentwurf.docx',
    notes='Gegnerischer, nicht eingereichter Entwurf vom 05.10.2026; das städtische Prüfmandat bleibt unverändert. Anlagenverzeichnis aus exhibits ergänzen. Streitwertvorschlag 1.748,75 EUR. Sturzpunkt und Reaktionszeit bleiben beweisbedürftig.',
    exhibits=[
        exhibit(1, '02_Sturzbericht.docx', 'Zeitnaher eigener Bericht der Klägerin vom 14.01.2026'),
        exhibit(2, '03_Streuplan.docx', 'Örtliche Verhältnisse, Nutzung und Winterdienstplan'),
        exhibit(3, '04_Einsatzprotokoll.docx', 'Erststreuung, Glättemeldung und Nachstreuung'),
        exhibit(4, '05_Wetterbeobachtung.docx', 'Örtliche Beobachtungen am Betriebshof'),
        exhibit(5, '06_Zeugin.eml', 'Erste Auskunft der Zeugin Rahmani'),
        exhibit(6, '07_Befund.docx', 'Ärztlicher Befund und Verlauf bis 03.02.2026'),
        exhibit(7, '08_Haushaltshilfe_Rechnung.docx', 'Rechnung und Zahlung von 148,75 EUR'),
        exhibit(8, 'schriftverkehr-und-klage/11_Zeugin_Ergaenzung.eml', 'Ergänzung der Zeugin zu Standort und Wahrnehmungsgrenzen'),
        exhibit(9, 'schriftverkehr-und-klage/12_Disposition_Ergaenzung.eml', 'Auskunft über verfügbaren Handstreutrupp'),
        exhibit(10, 'schriftverkehr-und-klage/13_Haushalt_und_Verheilung.eml', 'Angaben zu Hilfe, Mitwirkung des Ehemanns und Verlauf'),
        exhibit(11, 'schriftverkehr-und-klage/14_Anspruchsschreiben.pdf', 'Konkretisierung der Forderung vom 02.10.2026'),
        exhibit(12, 'schriftverkehr-und-klage/15_Antwort_Stadt.pdf', 'Stellungnahme der Stadt vom 05.10.2026'),
    ],
    documents=[
        document('11_Zeugin_Ergaenzung.eml', 'Ergänzende Angaben zur Querung am 13. Januar', '2026-09-30T18:15:00+02:00', 'email', '''Sehr geehrte Frau Eichenlaub,

ich bestätige meine Nachricht an die Stadt vom 24. September. Ich stand auf der Haltestellenseite, ungefähr drei Meter hinter dem abgesenkten Bord, und blickte zur Bäckerei. Der Lieferwagen stand rechts in meiner Blickrichtung. Er verdeckte die Füße von Frau Zeisig gerade beim letzten Schritt. Ich kann auch heute nicht zuverlässig sagen, ob ihr rechter Fuß noch auf der Fahrbahn oder schon auf dem abgesenkten Bord stand. Dass ich nach Monaten plötzlich einen genauen Punkt nennen könnte, wäre falsch.

Was ich selbst sicher erlebt habe: Auf meinem Weg zur Haltestelle war ich wenige Minuten zuvor in dem letzten Straßenmeter vor dieser Absenkung weggerutscht. Ich hatte mich am Haltestellenpfosten wieder gefangen. Beim Hinlaufen zu Frau Zeisig setzte ich die Füße deshalb besonders kurz. Frau Zeisig machte vor dem Fallen keine erkennbaren Laufschritte. Sie hatte ihre Tasche in der Hand, kein Telefon. Die Straße glänzte in diesem schmalen Bereich; hinter der Absenkung konnte ich wieder normal stehen.

Meine Wohnanschrift für eine etwaige Ladung ist Blütenrautenweg 18, 97074 Würzburg. Den Namen der Frau mit dem Telefon kenne ich weiterhin nicht. Ich besitze kein Foto und habe keine Messung vorgenommen.

Freundliche Grüße
Leila Rahmani''', 'Leila Rahmani <leila.rahmani@briefpost.example>', 'Rechtsanwältin Frieda Eichenlaub <kanzlei@eichenlaub-recht.example>'),
        document('12_Disposition_Ergaenzung.eml', 'W-12 – ergänzende Rückfrage zur Personalverfügbarkeit', '2026-10-01T10:20:00+02:00', 'email', '''Sehr geehrte Frau Holler,

ich habe wegen der Rückfrage von Frau Eichenlaub das Schichtbuch nochmals mit Huriye Demir und der Disponentin Gerlinde Seufert durchgesehen. Fahrzeug 2 konnte den Einsatz an der steilen Zufahrt zum Seniorenhaus nicht sofort abbrechen. Daneben war aber der Handtrupp Demir/Engelbrecht seit 07:18 Uhr wieder im Hof. Der kleine Handwagen war mit Streugut gefüllt. Die beiden hatten bis zur um 08:00 Uhr vorgesehenen Ablösung keinen weiteren dringlichen Auftrag. Das geht aus dem Rückkehrvermerk im Schichtbuch hervor; eine selbständige Freigabe zum Losgehen durften sie nicht erteilen.

Zum Transport ergänze ich ausdrücklich: Der Handtrupp war mit dem städtischen Kleintransporter 5 zurückgekommen. Dieser stand seit 07:18 Uhr fahrbereit im Hof, war nicht für einen anderen Auftrag eingeplant und hätte den gefüllten Handstreuwagen mitnehmen können. Hilmar Engelbrecht war an diesem Morgen der eingeteilte Fahrer; die nötige Fahrerlaubnis und dienstliche Fahrberechtigung lagen vor. Diese Zuordnung haben wir anhand des Fahrzeugausgabeblatts und mit Herrn Engelbrecht geprüft. Für die rund 1,8 Kilometer bis zur Querung einschließlich Ausladen rechnen die beiden aus ihrer üblichen Tour mit zwölf Minuten. Gemeint ist eine Anfahrt, kein Fußmarsch mit dem Wagen. Eine Nachstellung unter den Januarbedingungen ist das nicht. Wäre der Trupp um 07:23 Uhr beauftragt worden, hätte er nach dieser Erfahrungszeit etwa um 07:35 Uhr vor Ort mit dem Streuen beginnen können. Das Streuen des Querungsstreifens dauert normalerweise zwei bis drei Minuten. Die Zufahrt zum Seniorenhaus hätte weiter von Fahrzeug 2 bearbeitet werden können.

Frau Seufert erklärt, sie habe den ersten Eintrag „Gehweg Bäckerei“ als nachrangige Gehwegmeldung behandelt. Die Wortfolge „Übergang … Leute rutschen“ stehe auf ihrem Telefonblatt; sie habe den Zusammenhang mit der Fahrbahnquerung erst später hergestellt. Das belegt noch nicht, wie glatt es an welchem Punkt um 07:42 Uhr war. Wir verfügen über keine zusätzliche Messung und keinen Salzsensorwert.

Ottmar Dörflein
Bauhof, Kieslaubenweg 2, 97076 Würzburg''', 'Ottmar Dörflein <bauhof@wuerzburg-fallakten.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        document('13_Haushalt_und_Verheilung.eml', 'Haushaltshilfe und heutiger Gesundheitszustand', '2026-10-02T08:35:00+02:00', 'email', '''Sehr geehrte Frau Eichenlaub,

Frau Merklein kannte ich vorher als gelegentliche Helferin, einen laufenden Vertrag hatte ich mit ihr nicht. Im Januar hätte ich ohne den Sturz keine dieser fünf Stunden bestellt. Mein Mann Ottmar Zeisig konnte kochen und kleine Dinge wegräumen. Wegen seiner schon vorher bestehenden Schulterbeschwerden konnte er keinen vollen Wäschekorb und keine schweren Einkaufstaschen tragen. Ich konnte mit der linken Hand zunächst kaum zugreifen. Unsere Kinder wohnen nicht im Haus. Die Rechnung habe ich selbst am 29. Januar bezahlt; keine Kasse und keine andere Person hat sie mir ersetzt.

Die Hilfe beschränkte sich auf die in der Rechnung bezeichneten Tätigkeiten. Wir haben keine zusätzlichen Stunden für Betreuung oder Begleitung bezahlt. Die Behandlung in der Praxis rechnet meine Krankenversicherung ab; solche Behandlungskosten möchte ich nicht selbst fordern. Verdienstausfall habe ich nicht.

Im Februar ließ das Ziehen nach. Etwa Ende Februar konnte ich wieder ohne Beschwerden greifen. Eine weitere Untersuchung habe ich deshalb nicht veranlasst. Ich verlange keinen Ersatz für einen behaupteten Dauerschaden. Für die ersten Tage waren die Schmerzen und die Unsicherheit beim Treppensteigen aber erheblich. Ich trug meine gewöhnlichen flachen Winterstiefel. Eine Begutachtung der Sohlen gibt es nicht; ich kann keine besondere Rutschfestigkeitsklasse nachweisen.

Mit freundlichen Grüßen
Kunigunde Zeisig''', 'Kunigunde Zeisig <kunigunde.zeisig@briefpost.example>', 'Rechtsanwältin Frieda Eichenlaub <kanzlei@eichenlaub-recht.example>'),
        document('14_Anspruchsschreiben.docx', 'Zeisig gegen Stadt Würzburg – ergänzende Begründung', '02.10.2026', 'letter', '''Rechtsanwältin Frieda Eichenlaub
Lindenkornweg 11, 97074 Würzburg

An die Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

ich vertrete Frau Kunigunde Zeisig wegen ihres Sturzes vom 13. Januar. Nach Einsicht in die von Ihnen überlassenen Winterdienstunterlagen konkretisiere ich ihre Forderung auf 148,75 EUR nachgewiesene Haushaltshilfe und ein angemessenes Schmerzensgeld, das wir mit 1.600,00 EUR bewerten. Den am 30. September erbetenen Antworttermin 12. Oktober halten wir aufrecht.

Die Erststreuung um 05:54 Uhr wird nicht pauschal bestritten. Entscheidend ist die neue, konkrete Glättemeldung um 07:20 Uhr. Die Querung gehört nach Ihrem eigenen Tourenblatt zur ersten Priorität, verbindet Haltestelle und Bäckerei und liegt in einer verschatteten Gefällestrecke. Herr Dörflein hat inzwischen bestätigt, dass ein ausgerüsteter Handtrupp im Hof verfügbar war. Nach der angegebenen Wege- und Arbeitszeit hätte dieser den Querungsstreifen vor dem Sturz bearbeiten können, während das Fahrzeug am Seniorenhaus geblieben wäre.

Die Zeugin Rahmani kann den genauen letzten Fußkontakt nicht festlegen. Sie bestätigt jedoch eigenes Rutschen im letzten Fahrbahnabschnitt und normales Gehen meiner Mandantin. Meine Mandantin bleibt bei ihrer zeitnah dokumentierten Erinnerung, noch auf der Fahrbahn ausgerutscht zu sein. Wir behaupten weder ein nicht vorhandenes Unfallfoto noch eine sichere Wahrnehmung der Zeugin über die verdeckte Stelle.

Der Befund weist Distorsion und Prellung aus. Die eingekaufte Hilfe betraf tatsächlich ausgeführte Arbeiten, die wegen der Verletzung anfielen. Einen Dauerschaden, Behandlungskosten der Krankenversicherung und unentgeltliche Familienhilfe machen wir nicht geltend. Die Beschwerden waren nach Angaben meiner Mandantin Ende Februar abgeklungen.

Bitte teilen Sie mit, ob die Stadt den zeitlichen Angaben zum Handtrupp oder dessen Verfügbarkeit widerspricht und auf welche konkreten Aufgaben sie einen solchen Widerspruch stützt. Wir bitten ferner, Telefonblatt, Schichtbuch und Streufahrtdaten im ursprünglichen Zusammenhang aufzubewahren. Eine pauschale Berufung auf die frühere Streufahrt beantwortet die erneute Gefahrenmeldung nicht. Zugleich sind wir bereit, über eine Einigung zu sprechen, die das Beweisrisiko des Sturzpunkts angemessen berücksichtigt.

Mit freundlichen Grüßen
Frieda Eichenlaub
Rechtsanwältin'''),
        document('15_Antwort_Stadt.docx', 'Sturz Krummblattbogen – vorläufige Stellungnahme', '05.10.2026', 'letter', '''Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

An Rechtsanwältin Frieda Eichenlaub
Lindenkornweg 11, 97074 Würzburg

Sehr geehrte Frau Eichenlaub,

wir bestätigen den Eingang Ihres Schreibens vom 2. Oktober. Der Anspruch wird weiterhin geprüft; eine abschließende Entscheidung soll innerhalb der von Ihrer Mandantin gesetzten Frist erfolgen. Mit diesem Schreiben ist weder eine Zahlung zugesagt noch die Haftung anerkannt.

Die Angaben des Bauhofs zum Handtrupp haben wir Ihnen vollständig weitergegeben. Der Trupp befand sich im Hof und hatte keinen neuen dringlichen Auftrag. Ob die telefonische Meldung in der damaligen Situation bereits eine unverzügliche Entsendung dieses Trupps erforderte, halten wir für offen. Das reguläre Streufahrzeug bearbeitete eine steile Zufahrt, bei der ebenfalls Personen gefährdet sein konnten. Die Wegezeit von zwölf Minuten ist ein Erfahrungswert; die tatsächliche Zeit am Unfallmorgen ist nicht nachgestellt. Wir bestreiten deshalb die von Ihnen abgeleitete sichere rechtzeitige Verhinderung des Sturzes.

Weiter bleibt ungeklärt, ob Ihre Mandantin auf der Fahrbahn oder auf dem anschließenden Gehweg ausrutschte. Frau Rahmani hat diesen Punkt ausdrücklich nicht sicher wahrgenommen. Die Unterlagen belegen eine frühe Streufahrt und eine spätere Nachstreuung, aber keinen flächendeckenden Eiszustand um 07:42 Uhr. Die Beobachtungen auf dem Betriebshof dürfen nicht als amtliche Wetterfeststellung für die Unfallstelle behandelt werden.

Die Zahlung von 148,75 EUR ist nachvollziehbar. Die unfallbedingte Erforderlichkeit sämtlicher fünf Stunden und die Bewertung des Schmerzensgelds bleiben Gegenstand der Prüfung. Wir begrüßen die Klarstellung, dass keine bleibende Verletzung behauptet wird. Über etwaige Ansprüche der Krankenversicherung treffen wir mit Ihnen keine Verfügung. Eine quotenmäßige Lösung ist derzeit weder zugesagt noch ausgeschlossen.

Die genannten Betriebsunterlagen werden erhalten. Eine abschließende Entscheidung der Rechtsstelle liegt am heutigen Tag noch nicht vor. Ihr Schreiben hat das vorhandene Prüfmandat der Stadt nicht erweitert; externe Erklärungen eines Bevollmächtigten sind damit nicht verbunden.

Mit freundlichen Grüßen
Gertraud Holler
Rechtsstelle'''),
        document('16_Klageentwurf.docx', 'Klageentwurf Zeisig gegen Stadt Würzburg', '05.10.2026', 'claim', '''ENTWURF – NICHT EINGEREICHT
Stand: 5. Oktober 2026

An das Landgericht Würzburg
Ottostraße 5, 97070 Würzburg

## 1 Parteien und Gegenstand

In dem Rechtsstreit der Kunigunde Zeisig, Flachsblütenweg 7, 97074 Würzburg, Klägerin, Prozessbevollmächtigte: Rechtsanwältin Frieda Eichenlaub, Lindenkornweg 11, 97074 Würzburg,

gegen die Stadt Würzburg, vertreten durch den Oberbürgermeister, Mainlaubplatz 1, 97070 Würzburg, Beklagte,

wegen Amtshaftung aus einem Glätteunfall wird für eine mögliche Einreichung folgender Klageantrag vorbereitet. Der vorgeschlagene Streitwert beträgt 1.748,75 EUR. Ein gerichtliches Aktenzeichen besteht für diesen Entwurf nicht. Die außergerichtlich gesetzte Antwortfrist endet erst am 12. Oktober 2026; der Entwurf enthält keine Behauptung, diese Frist sei bereits abgelaufen.

## 2 Anträge

Die Klägerin beantragt, die Beklagte zu verurteilen, an sie 148,75 EUR sowie ein angemessenes Schmerzensgeld zu zahlen, dessen Höhe in das Ermessen des Gerichts gestellt wird und für das die Klägerin 1.600,00 EUR als angemessen ansieht, jeweils nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz ab dem auf die Zustellung der Klage folgenden Tag.

Die Klägerin beantragt weiter, der Beklagten die Kosten des Rechtsstreits aufzuerlegen. Ein Feststellungsantrag wegen künftiger Schäden wird nicht gestellt. Soweit die Beklagte ihre Verteidigungsbereitschaft nicht rechtzeitig anzeigt, wird bei Vorliegen der gesetzlichen Voraussetzungen ein Versäumnisurteil im schriftlichen Vorverfahren beantragt.

## 3 Zuständigkeit und Streitgegenstand

Die Klage betrifft die Verletzung einer hoheitlich wahrgenommenen kommunalen Winterdienstpflicht. Der Zivilrechtsweg ist nach Art. 34 Satz 3 GG eröffnet. Das Landgericht ist gemäß § 71 Abs. 2 Nr. 2 GVG unabhängig vom geringen Streitwert ausschließlich sachlich zuständig. Die seit 2026 geltende allgemeine Wertgrenze von 10.000 EUR für Amtsgerichte verdrängt diese Sonderzuweisung nicht. Die Beklagte hat ihren Sitz in Würzburg; auch Unfallort und behauptete Pflichtverletzung liegen hier. Die örtliche Zuständigkeit folgt aus §§ 17, 32 ZPO.

Gegenstand sind allein die eigenen Ansprüche der Klägerin wegen der Körperverletzung und ihrer bezahlten Haushaltshilfe. Behandlungskosten der Krankenversicherung werden nicht eingeklagt. Ein Rückdeckungs- oder Versicherungsverhältnis der Beklagten ist keine Voraussetzung der Klage und wird nicht behauptet.

## 4 Unfallstelle und Ablauf

Am 13. Januar 2026 gegen 07:42 Uhr überquerte die Klägerin den Krummblattbogen an der Einmündung Spitalblütenweg, um zur Bushaltestelle zu gelangen. Die innerörtliche Gemeindestraße steht in städtischer Straßenbaulast. Die Beklagte führt den Winterdienst dort durch eigene Beschäftigte aus. Die abgesenkten Borde bilden eine erkennbare Fußgängerverbindung zwischen Bäckerei und Haltestelle. Eine Markierung als Zebrastreifen besteht nicht. Die Straße weist in der verschatteten Kurve etwa vier Prozent Gefälle auf. Sie dient einer Buslinie ab 06:05 Uhr und der Zufahrt zu einem Ärztehaus. Bei einer werktäglichen Novemberzählung benutzten innerhalb der Stunde von 07:00 bis 08:00 Uhr 74 Personen die Querung. Der nächste abgesenkte Übergang liegt etwa 310 Meter entfernt. Die Klägerin beruft sich auf diese konkrete Bedeutung und nicht auf eine allgemeine Pflicht, jede Straße jederzeit eisfrei zu halten.

Beweis: Winterdienstplan vom 2. Dezember 2025, Anlage K2; Zeugnis des Ottmar Dörflein, zu laden über Stadt Würzburg, Bauhof, Kieslaubenweg 2, 97076 Würzburg; erforderlichenfalls gerichtlicher Augenschein der Örtlichkeit zum Verlauf und zu den Entfernungen.

Die Klägerin ging normal und trug flache Winterstiefel. Sie hielt kein Telefon. Kurz vor der gegenüberliegenden Absenkung rutschte ihr rechter Fuß nach ihrer Erinnerung auf der Fahrbahn, ungefähr einen halben Meter vor dem Bord, weg. Sie fiel nach links und stützte sich mit der linken Hand ab. Wo die Hand nach dem Sturz lag, beantwortet nicht, wo der Fuß den Halt verlor. Die Klägerin hatte den Bus um 07:47 Uhr erreichen wollen, rannte aber nicht.

Beweis: Zeitnaher Sturzbericht, Anlage K1; persönliche Anhörung der Klägerin gemäß § 141 ZPO; Zeugnis der Leila Rahmani, Blütenrautenweg 18, 97074 Würzburg, zu Gangart, Sturzbeobachtung und Beschaffenheit ihres eigenen Querungswegs, Anlagen K5 und K8. Eine Parteivernehmung wird nur unter den gesetzlichen Voraussetzungen angeregt. Der eigene Bericht ersetzt keinen unabhängigen Augenzeugen für den letzten Fußkontakt.

Frau Rahmani war selbst kurz zuvor im letzten Fahrbahnabschnitt vor der Absenkung gerutscht. Ein Lieferwagen verdeckte ihr jedoch beim Sturz der Klägerin teilweise die Beine. Ihre frühere Formulierung, der Fuß sei bereits am Gehwegrand gewesen, war eine räumliche Einschätzung und keine sichere Wahrnehmung des letzten Schritts. Die Klägerin legt beide Erklärungen offen. Sollte das Gericht stattdessen einen selbständigen Sturz erst auf dem angrenzenden Gehweg feststellen, wäre die behauptete Pflichtverletzung an der Fahrbahnquerung gesondert auf ihre Ursächlichkeit zu prüfen; die Klage stützt sich nicht auf eine bislang ungeklärte Übertragung der Gehwegreinigung.

## 5 Erneute Glätte und mögliche Reaktion

Das Fahrzeug der Beklagten passierte die Stelle um 05:54 Uhr. Der Fahrer vermerkte eine Streumenge von 15 Gramm je Quadratmeter; der Salzauftrag am einzelnen Übergang ist nicht technisch aufgezeichnet. Die Klägerin muss die Erststreuung nicht widerlegen, um eine spätere Nachstreupflicht darzulegen. Um 07:20 Uhr meldete die Bäckerei telefonisch, der Übergang sei wieder spiegelig und Menschen rutschten. Die Disposition verkürzte diese konkrete Meldung zunächst auf „Gehweg Bäckerei“. Erst um 07:35 Uhr wurde die Nachstreufahrt zugeteilt; das Fahrzeug kam um 07:51 Uhr und streute um 07:52 Uhr. Am Betriebshof waren seit 07:05 Uhr Sprühregen und später ein gefrierender Film beobachtet worden. Diese Beobachtung stammt von Beschäftigten, nicht von einem Wetterdienst, und liegt 1,8 Kilometer entfernt. Sie wird nur als zusätzliche Warninformation, nicht als lokaler Temperaturbeweis verwendet.

Beweis: Einsatzprotokoll und Beobachtungsblatt, Anlagen K3 und K4; Zeugnis der Disponentin Gerlinde Seufert und der Huriye Demir, jeweils zu laden über den genannten Bauhof; Zeugnis des Fahrers Emil Kilian, ebendort, zur zweiten Streufahrt und zum damals sichtbaren Belag.

Nach der ergänzenden Prüfung war der Handtrupp Demir/Engelbrecht bereits um 07:18 Uhr in den Hof zurückgekehrt. Sein Streuwagen war gefüllt; ein dringlicher Folgeauftrag bestand nicht. Die neue Auskunft bestätigt außerdem einen konkret verfügbaren Kleintransporter 5, der den Wagen hätte mitführen können, sowie den eingeteilten und fahrberechtigten Fahrer Hilmar Engelbrecht. Die Klägerin setzt kein zusätzliches Fahrzeug ohne Tatsachengrundlage voraus. Für die rund 1,8 Kilometer entfernte Querung werden zwölf Minuten Anfahrt einschließlich Ausladen als übliche Erfahrungszeit angegeben, kein zwölfminütiger Fußweg mit Handwagen. Bei weiteren zwei bis drei Minuten Arbeitszeit wäre eine um 07:23 Uhr veranlasste Behandlung gegen 07:38 Uhr abgeschlossen gewesen. Der Einsatz am Seniorenhaus hätte dabei fortgesetzt werden können. Die Klägerin verlangt somit keinen Abbruch einer gleichrangigen Gefahrenabwehr. Sie rügt die unterbliebene Nutzung einer vorhandenen zusätzlichen Möglichkeit nach einer konkreten Meldung.

Beweis: Ergänzende Auskunft des Bauhofs, Anlage K9; Zeugnis von Ottmar Dörflein, Huriye Demir und Hilmar Engelbrecht, jeweils zu laden über den Bauhof. Zum Schichtbeginn und zur Rückkehr wird ergänzend die Vorlage des dort bezeichneten Schichtbuchblatts und des in Anlage K9 konkret bezeichneten Fahrzeugausgabeblatts für Kleintransporter 5 vom 13. Januar durch die Beklagte gemäß § 142 ZPO angeregt. Eine allgemeine Durchsuchung nicht näher bestimmter Unterlagen wird nicht beantragt.

Die genannten Minuten sind Erfahrungswerte, keine nachträgliche Messung. Die Klägerin behauptet auf dieser Grundlage die rechtzeitige Durchführbarkeit; sie bietet Zeugen zu Weg, Ausrüstung und tatsächlicher Verfügbarkeit an. Sollte der Wirkungsbeginn des verwendeten Streumittels entscheidungserheblich bestritten werden, wird ergänzend ein sachverständiges Gutachten dazu angeboten, ob unter den durch Zeugen feststellbaren Bedingungen eine Behandlung des schmalen Übergangs vor 07:42 Uhr die Rutschgefahr wesentlich beseitigt hätte. Das Gutachten soll unbekannte Wetterdaten nicht ersetzen.

## 6 Pflichtverletzung und Zurechnung

Die Beklagte haftet aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG. Art. 51 Abs. 1 und 2 BayStrWG bestimmt die kommunale Aufgabe nach Leistungsfähigkeit und örtlichem Bedürfnis. Für die Fahrbahn werden die Gefährlichkeit und die Verkehrsbedeutung durch Kurvenlage, Schatten, Gefälle und Busverkehr konkret belegt. Für die Fußgängerverbindung sprechen zusätzlich die erhebliche Nutzung und die Entfernung der nächsten abgesenkten Querung. Dass kein Zebrastreifen markiert ist, nimmt dem tatsächlich benötigten Übergang nicht seine Bedeutung. Das Tourenblatt allein schafft noch keinen zivilrechtlichen Anspruch; seine tatsächlichen Angaben belegen jedoch die erkannten örtlichen Anforderungen.

Die Amtspflicht schützt auch die Klägerin als Benutzerin dieser Querung vor einem körperlichen Glätteschaden. Nach der konkreten Warnung durfte die Nachricht nicht ohne weitere Klärung einem anderen, nachrangig behandelten Bereich zugeordnet werden. Das Telefonblatt enthielt bereits die entscheidenden Worte zum Übergang und zu rutschenden Personen. Die zusätzliche Wetterbeobachtung erreichte die Disposition um 07:27 Uhr. Bei sachgerechter Aufnahme und Koordination hätte der verfügbare Handtrupp eingesetzt werden können. Darin liegt jedenfalls fahrlässige Verletzung der örtlich begrenzten Sicherungspflicht.

Die Klägerin erkennt an, dass auch nach sachgerechtem Winterdienst neue Glätte auftreten kann und eine angemessene Reaktionszeit verbleibt. Ihr Vorwurf betrifft deshalb weder lückenlose Überwachung noch die Zeit vor Eingang der Meldung. Er betrifft die konkrete Verzögerung zwischen verfügbarer Nachricht und nutzbarem Handtrupp. Ein privat haftender Dritter, gegen den die Klägerin denselben Schaden erfolgreich durchsetzen könnte, ist nicht ersichtlich. Ein vor dem plötzlichen Sturz ergreifbarer Rechtsbehelf im Sinne von § 839 Abs. 3 BGB bestand nicht.

## 7 Verletzung und Höhe

Der Befund vom 13. Januar und die Verlaufskontrolle vom 3. Februar dokumentieren eine Distorsion des linken Handgelenks sowie eine Prellung des rechten Knies. Ein Bruch wurde ausgeschlossen. Ruhigstellung, Kühlung und bedarfsgerechte Schmerzmittel waren erforderlich. Anfang Februar bestanden beim kräftigen Greifen noch Beschwerden. Nach eigener Angabe war die Klägerin Ende Februar beschwerdefrei. Eine länger dauernde ärztlich gesicherte Funktionsstörung wird nicht behauptet.

Beweis: Befundbericht, Anlage K6; Zeugnis der behandelnden Ärztin Dr. Parvin Herbst, Wiesenkornweg 4, 97074 Würzburg, nach Schweigepflichtentbindung; gegebenenfalls medizinisches Sachverständigengutachten zum dokumentierten Verletzungsbild. Zu den im Alltag erlebten Einschränkungen wird Zeugnis des Ottmar Zeisig, Flachsblütenweg 7, 97074 Würzburg, angeboten.

Die Klägerin hält unter Berücksichtigung der Schmerzen, der zwei betroffenen Gliedmaßen und des mehrwöchigen Verlaufs 1.600,00 EUR nach § 253 Abs. 2 BGB für angemessen. Sie macht den Betrag nicht von einer erfundenen Vergleichsentscheidung abhängig. Die gerichtliche Bewertung kann namentlich bei kürzer feststellbarer Beschwerdedauer niedriger ausfallen.

Für fünf tatsächlich geleistete Stunden Haushaltshilfe zahlte sie 125,00 EUR netto zuzüglich 23,75 EUR Umsatzsteuer, zusammen 148,75 EUR. Es ging um Einkauf, Reinigung, Wäsche und Müllentsorgung an drei Tagen. Ihr Ehemann übernahm leichte Arbeiten und Kochen, konnte aber wegen eigener Schulterbeschwerden die schweren Tätigkeiten nicht auffangen. Ohne Unfall wären diese Stunden nicht beauftragt worden. Die Klägerin ist nicht zum Vorsteuerabzug berechtigt. Erstattung durch einen Dritten erfolgte nicht.

Beweis: Rechnung mit Zahlungsbestätigung, Anlage K7; ergänzende Erklärung, Anlage K10; Zeugnis der Agnes Merklein, Malvenkornweg 12, 97074 Würzburg, zu Dauer und ausgeführten Arbeiten; Zeugnis des Ottmar Zeisig zum sonstigen Haushalt und seiner eigenen Mitwirkung. Die Rechnung beweist die Leistung und Bezahlung; die medizinische Erforderlichkeit folgt erst aus dem Zusammenhang mit der Verletzung und den konkret nicht selbst erledigbaren Arbeiten.

## 8 Einwendungen und Beweisgrenzen

Ein Mitverschulden nach § 254 BGB wird bestritten. Die Klägerin war mit Winterstiefeln unterwegs, ging normal und war nicht durch ein Telefon abgelenkt. Der Wunsch, einen Bus zu erreichen, beweist kein Rennen. Dass die Schuhe nicht sachverständig untersucht wurden, wird offen angegeben. Ebenso wird nicht behauptet, die glänzende Fläche sei schlechthin unsichtbar gewesen. Die Klägerin hielt sie für Nässe. Eine erkennbare konkrete Warnung, Absperrung oder gefahrlose nahe Ausweichquerung bestand nach ihrem Kenntnisstand nicht.

Die Beklagte verweist in Anlage K12 auf frühe Streuung, unbekannten genauen Sturzpunkt und unsichere Wegezeit. Diese Einwendungen erfordern Beweisaufnahme. Weder aus dem bloßen Sturz noch aus der späteren Nachstreuung wird allein auf eine Pflichtverletzung geschlossen. Entscheidend ist die Gesamtheit aus Warnmeldung, örtlicher Bedeutung, verfügbarem Personal und feststellbarer Glätte. Die Klägerin beantragt keine pauschale Beweislastumkehr. Das Verfahren muss insbesondere klären, ob ihr Sturz der behaupteten Fahrbahngefahr zuzuordnen ist und eine pflichtgemäße Reaktion rechtzeitig gewirkt hätte.

## 9 Zinsen und abschließende Erklärung

Die Prozesszinsen folgen aus §§ 291, 288 Abs. 1 BGB. Beantragt werden fünf Prozentpunkte, keine neun Prozentpunkte, da es sich um einen Schadensersatzanspruch und nicht um eine entsprechende Entgeltforderung handelt. Der Beginn wird an die tatsächliche künftige Zustellung geknüpft; ein Zustellungsdatum wird nicht vorweggenommen. Vorgerichtliche Anwaltskosten und frühere Verzugszinsen sind nicht Gegenstand dieses Entwurfs.

Mit dem Anspruchsschreiben vom 2. Oktober, Anlage K11, wurden Verfügbarkeit des Handtrupps, tatsächliche Hilfeleistung und begrenzter Verletzungsverlauf gegenüber der Beklagten konkretisiert. Die Klägerin ist zu einer vergleichsweisen Lösung unter Berücksichtigung der tatsächlichen Beweisrisiken bereit. Dies enthält kein Anerkenntnis eines eigenen Verschuldens. Die beigefügten Anlagen enthalten auch die ihr ungünstigen Wahrnehmungsgrenzen und die Stellungnahme der Beklagten.

Frieda Eichenlaub
Rechtsanwältin
Entwurfsfassung ohne Unterschrift und ohne Einreichung'''),
    ]))

CASES.append(dict(
    slug='akha-wuerzburg-antragsbearbeitung',
    attachments={},
    claim_file='16_Klageentwurf.docx',
    notes='Gegnerischer Entwurf. Neu belegte Sonderkulanz bis 18.06.2026 12 Uhr widerspricht nicht der am 19.06. bereits verstrichenen regulären Frist. Nur zusätzliche 119 EUR werden beansprucht. Anlagenverzeichnis aus exhibits ergänzen.',
    exhibits=[
        exhibit(1, '02_Antrag.docx', 'Vollständiger Antrag für den 20. und 21. Juni'),
        exhibit(2, '03_Eingangsbestaetigung.eml', 'Bestätigung der Vollständigkeit und der Junidaten'),
        exhibit(3, '04_Registerauszug.docx', 'Falsche Julierfassung und positive Ortsprüfung'),
        exhibit(4, '05_Falsche_Auskunft.eml', 'Schriftliche Falschauskunft vom 15.06.2026'),
        exhibit(5, '06_Dringende_Nachfrage.eml', 'Richtigstellung, Hinweis auf Kosten und Entscheidungsbedarf'),
        exhibit(6, '07_Sachgebietsleitung.docx', 'Befugnisse, Genehmigungsfähigkeit und damaliger Kenntnisstand'),
        exhibit(7, '08_Wagenmiete_Rechnung.docx', 'Mietvereinbarung, Zahlung und reguläre Stornobedingungen'),
        exhibit(8, '09_Vermieter.eml', 'Tatsächliche Absage und fehlende Weitervermietung'),
        exhibit(9, '10_Forderung.eml', 'Ursprüngliche Forderung und fehlende festen Vorbestellungen'),
        exhibit(10, 'schriftverkehr-und-klage/11_Storno_Kulanz.eml', 'Nachgereichte Dokumentation der einmaligen Kulanzfrist'),
        exhibit(11, 'schriftverkehr-und-klage/12_Telefonat_Praezisierung.eml', 'Präzisierung der unzutreffenden telefonischen Zusage'),
        exhibit(12, 'schriftverkehr-und-klage/13_Entscheidung_Klaeger.eml', 'Zeitliche Entscheidungskette und Beschränkung des Schadens'),
        exhibit(13, 'schriftverkehr-und-klage/14_Reduzierte_Forderung.pdf', 'Korrigierte Forderung von 119,00 EUR'),
        exhibit(14, 'schriftverkehr-und-klage/15_Antwort_Stadt.pdf', 'Einwendungen der Stadt gegen Zurechnung und Rechtsschutzverhalten'),
    ],
    documents=[
        document('11_Storno_Kulanz.eml', 'Nachtrag: mein Angebot am Donnerstagmorgen', '2026-10-01T09:10:00+02:00', 'email', '''Sehr geehrte Frau Dr. Wolfram,

Herr Nouri hat mich nach unserem Kontakt vom Donnerstag, 18. Juni, gefragt. Ich habe den Verlauf auf meinem Geschäftstelefon nachgesehen. Am 18. Juni um 08:46 Uhr schrieb ich ihm: „Eigentlich war die halbe Stornierung gestern 18 Uhr zu Ende. Wenn Sie mir heute bis 12 Uhr verbindlich absagen, mache ich es ausnahmsweise noch für die halbe Miete. Dann bekommen Sie 119 Euro zurück. Danach bleibt es bei 238.“ Um 08:52 Uhr antwortete er: „Danke, ich kläre das sofort mit der Stadt und melde mich, wenn ich absagen muss.“ Dies ist der vollständige Text dieses kurzen Austauschs; ich kann das Telefon mit dem gespeicherten Verlauf vorlegen.

Das war ein einmaliges Angebot von mir, keine schon bei Vertragsschluss vereinbarte Fristverlängerung. Bis 12 Uhr ging keine Absage ein. Ich hätte bei rechtzeitiger Erklärung 119,00 EUR unabhängig von einer Weitervermietung zurückgezahlt. Erst am 19. Juni um 16:22 Uhr sagte Herr Nouri tatsächlich ab. Deshalb stand ihm auch nach meinem Sonderangebot keine Rückzahlung mehr zu.

Meine Nachricht vom 23. Juni ist weiterhin richtig: Nach seiner tatsächlichen Absage war die halbe Stornierung abgelaufen; eine kostenlose Umbuchung oder spätere Gutschrift gab es nicht. Das gesonderte Angebot vom Donnerstag hatte ich damals nicht erwähnt, weil wir über die Absage am Freitag sprachen. Es besteht keine zusätzliche mündliche Kulanzabrede. Der Wagen wurde nicht an andere Kunden vermietet.

Mit freundlichen Grüßen
Karla Storch
Kleiner Wagenverleih, Saatlaubenweg 8, 97076 Würzburg''', 'Karla Storch <storch@kleiner-wagenverleih.example>', 'Rechtsanwältin Dr. Nadia Wolfram <kanzlei@wolfram-recht.example>'),
        document('12_Telefonat_Praezisierung.eml', 'Gespräch mit Herrn Nouri am 18. Juni', '2026-10-01T14:05:00+02:00', 'email', '''Sehr geehrte Frau Holler,

nach der erneuten Rückfrage erinnere ich mich genauer an das Telefonat. Herr Nouri rief am 18. Juni gegen 09:35 Uhr an. Die Uhrzeit ergibt sich aus dem Eintrag in meinem Diensttelefon. Er sagte, der Verleiher habe ihm für diesen Vormittag noch eine letzte Möglichkeit eingeräumt, für die halbe Miete auszusteigen. Ich antwortete sinngemäß: „Der Fehler ist geklärt; Sie bekommen die Erlaubnis morgen.“ Ich hatte ihn damit beruhigen wollen. Meine frühere Angabe, ich habe nur von einer rechtzeitigen Vorlage gesprochen, war zu vorsichtig formuliert. Den Wortlaut kann ich nicht wie aus einer Aufnahme wiedergeben, eine solche gibt es nicht.

Tatsächlich war der Datumsfehler noch nicht im Register korrigiert. Ich hatte den Vorgang nicht mit unterschriftsreifem Bescheid an Herrn Abelein gegeben. Eine Zusage des Sachgebietsleiters über die Unterschrift am Freitag hatte ich nicht. Ich durfte weder die Erlaubnis erteilen noch ihren sicheren Erlass erklären. Aus der positiven Ortsprüfung und dem Hinweis „zustimmungsfähig“ hatte ich geschlossen, dass die Sache schnell erledigt werden könne. Ich habe Herrn Nouri nicht gesagt, dass die Unterschrift noch ungesichert war.

Das ist meine nachträgliche Erinnerung, keine damals angefertigte Gesprächsnotiz. Herr Nouri war ungehalten, aber er hat mir nicht mitgeteilt, dass er trotz einer offenen Entscheidung in jedem Fall an der Wagenmiete festhalten werde.

Mit freundlichen Grüßen
Edeltraud Merk
Sachbearbeitung Sondernutzung''', 'Edeltraud Merk <sondernutzung@wuerzburg-fallakten.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        document('13_Entscheidung_Klaeger.eml', 'Meine Entscheidung zwischen Telefonat und Stornofrist', '2026-10-02T08:50:00+02:00', 'email', '''Sehr geehrte Frau Dr. Wolfram,

das Angebot von Frau Storch und meine Antwort sind richtig wiedergegeben. Meine bisherige Forderung war insoweit unvollständig. Ich hatte den normalen Termin am Mittwoch aus eigener Hoffnung verstreichen lassen. Am Donnerstag bot Frau Storch mir aber noch einmal dieselbe halbe Rückzahlung an. Gerade deshalb rief ich sofort im Amt an. Nach dem Gespräch um 09:35 Uhr schrieb ich Frau Storch nicht mehr. Ich wollte den Wagen nutzen, weil Frau Merk die Erlaubnis für den nächsten Tag angekündigt hatte.

Hätte Frau Merk erklärt, dass noch keine Unterschrift vorbereitet oder abgesprochen war, hätte ich vor zwölf Uhr abgesagt. Ich hatte dafür mein Telefon griffbereit. Die 119 Euro Restkosten hätte ich dann akzeptiert. Einen festen Auftrag oder Kundenumsatz hatte ich nicht in der Hand; ich wollte nicht die ganze Miete aufs Spiel setzen, wenn die Stadt selbst keine sichere Erledigung nennen konnte. Den ersten verpassten Termin am Mittwoch kann ich nicht mit dem späteren Telefonat erklären. Deshalb bin ich mit Ihrer Beschränkung auf die zusätzlichen 119 Euro einverstanden.

Ich habe auch nach dem Telefonat keinen gerichtlichen Eilantrag gestellt. Aus meiner Sicht war die Angelegenheit nun geklärt. Dass der Sachgebietsleiter die Sache noch gar nicht entschieden hatte, erfuhr ich erst am Freitagnachmittag. Die Kleinunternehmerangabe bleibt richtig. Die Wagenrechnung wurde mir nicht erstattet. Eine spätere kostenlose Nutzung oder ein Ersatzgeschäft gab es nicht.

Mit freundlichen Grüßen
Samir Nouri''', 'Samir Nouri <samir@kaffee-nouri.example>', 'Rechtsanwältin Dr. Nadia Wolfram <kanzlei@wolfram-recht.example>'),
        document('14_Reduzierte_Forderung.docx', 'Nouri – Beschränkung und neue Belege', '02.10.2026', 'letter', '''Rechtsanwältin Dr. Nadia Wolfram
Birkenfächerweg 2, 97076 Würzburg

An die Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

ich vertrete Herrn Samir Nouri. Seine bisherige Forderung von 238,00 EUR wird nach ergänzender Sachverhaltsklärung auf 119,00 EUR beschränkt. Die gewöhnliche Stornierungsfrist endete am 17. Juni um 18:00 Uhr. Mein Mandant ließ sie aus Hoffnung auf die behördliche Korrektur verstreichen. Ein erst am nächsten Morgen geführtes Gespräch kann diese frühere Entscheidung nicht verursacht haben.

Frau Storch hat jetzt den gespeicherten Nachrichtenaustausch vom 18. Juni nachgereicht. Sie räumte um 08:46 Uhr ausnahmsweise eine letzte Frist bis 12:00 Uhr für die Rückzahlung von 119,00 EUR ein. Herr Nouri nahm die Nachricht zur Kenntnis und rief um 09:35 Uhr Frau Merk an. Deren zwischenzeitliche Präzisierung bestätigt eine bestimmte Erlaubnisankündigung für Freitag, obwohl weder die Vorlage noch eine verbindliche Unterschriftszusage vorlagen. Mein Mandant konnte deshalb noch nach diesem Telefonat den jetzt verlangten Mehrbetrag vermeiden. Bei wahrheitsgemäßer Information hätte er die Kulanzfrist genutzt.

Wir verlangen nicht die Wagenmiete allein deshalb, weil der Stand ausfiel. Die Vergleichsrechnung lautet: tatsächliche Belastung 238,00 EUR; Belastung bei rechtzeitiger Nutzung des konkreten Kulanzangebots 119,00 EUR; verbleibender Unterschied 119,00 EUR. Einen Gewinn aus ungesicherten Kundenumsätzen behaupten wir nicht. Eine weitere Erlaubnis hätte die Sachgebietsleitung erteilen müssen. Frau Merk konnte keine wirksame Erlaubnis durch ihr Telefonat ersetzen; sie musste jedoch richtig über den Bearbeitungsstand informieren.

Bitte berücksichtigen Sie diese neue Berechnung bei Ihrer Antwort bis 12. Oktober. Ein möglicher Eilantrag und die Frage eines früheren Tätigwerdens dürfen nicht losgelöst davon betrachtet werden, dass mein Mandant ausdrücklich auf die richtige Veranstaltung und die drohenden Kosten hingewiesen und dann eine bestimmte Erledigungsauskunft erhalten hatte. Wir sind für eine wirtschaftliche Erledigung des geringfügigen Anspruchs offen. Weitere Anwaltskosten machen wir mit diesem Schreiben nicht geltend.

Mit freundlichen Grüßen
Dr. Nadia Wolfram
Rechtsanwältin'''),
        document('15_Antwort_Stadt.docx', 'Nouri – Stellungnahme zum nachgereichten Kulanzangebot', '05.10.2026', 'letter', '''Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

An Rechtsanwältin Dr. Nadia Wolfram
Birkenfächerweg 2, 97076 Würzburg

Sehr geehrte Frau Dr. Wolfram,

das Schreiben vom 2. Oktober und die nachgereichten Nachrichten haben wir erhalten. Wir behandeln die Forderung nun in Höhe von 119,00 EUR. Die ursprünglichen Unterlagen werden nicht ausgetauscht; die spätere Konkretisierung ist als Ergänzung zur Akte genommen. Die neuen Angaben der Vermieterin sind mit der tatsächlichen Absage am 19. Juni vereinbar, bedürfen aber gegebenenfalls des Nachweises durch den gespeicherten Verlauf.

Frau Merk hat uns den Inhalt ihrer erneuten Erinnerung bestätigt. Eine Erlaubnis konnte sie nicht selbst erteilen. Die Sachgebietsleitung war zuständig; deren positive interne Vorbewertung ersetzte keinen Bescheid. Eine verbindliche Genehmigungsentscheidung für den nächsten Tag lag im Zeitpunkt des Telefonats nicht vor. Eine derart bestimmte Auskunft hätte deshalb nicht gegeben werden dürfen.

Ob daraus gerade der geltend gemachte Betrag folgt, ist damit noch nicht abschließend entschieden. Herr Nouri wusste seit dem 15. Juni vom Datumsfehler und kannte die Befristung der Veranstaltung. Er hatte selbst gerichtlichen Eilrechtsschutz angesprochen. Aus städtischer Sicht bleibt zu klären, ob früheres Nachfassen bei der Sachgebietsleitung oder ein rechtzeitiger Eilantrag den Ausfall verhindert hätte und ob er tatsächlich am Donnerstagvormittag zur Aufgabe des Vorhabens bereit gewesen wäre. Die bereits zuvor verstrichene reguläre Frist ist für diese innere Entscheidung ein gegenläufiger Gesichtspunkt.

Wir stellen nicht in Abrede, dass bei erfolgreicher Stornierung bis zur nachträglich gewährten Frist 119,00 EUR zurückgezahlt worden wären, sofern Frau Storch das Angebot in der wiedergegebenen Form bestätigt. Die Frage der haftungsrechtlichen Zurechnung bleibt davon zu unterscheiden. Eine Zahlung oder einen Vergleich können wir heute noch nicht zusagen. Die abschließende Antwort soll innerhalb der bis 12. Oktober laufenden Frist erfolgen.

Mit freundlichen Grüßen
Gertraud Holler
Rechtsstelle'''),
        document('16_Klageentwurf.docx', 'Klageentwurf Nouri gegen Stadt Würzburg', '05.10.2026', 'claim', '''ENTWURF – NICHT EINGEREICHT
Stand: 5. Oktober 2026

An das Landgericht Würzburg
Ottostraße 5, 97070 Würzburg

## 1 Parteien und Antrag

In dem Rechtsstreit des Samir Nouri, handelnd unter Kaffee Nouri, Löwensamenweg 3, 97074 Würzburg, Kläger, Prozessbevollmächtigte: Rechtsanwältin Dr. Nadia Wolfram, Birkenfächerweg 2, 97076 Würzburg,

gegen die Stadt Würzburg, vertreten durch den Oberbürgermeister, Mainlaubplatz 1, 97070 Würzburg, Beklagte,

wird beantragt, die Beklagte zu verurteilen, an den Kläger 119,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz ab dem auf die Zustellung der Klage folgenden Tag zu zahlen und die Kosten des Rechtsstreits zu tragen. Der Streitwert beträgt 119,00 EUR. Vorgerichtliche Rechtsanwaltskosten sind nicht Gegenstand des Antrags.

Es handelt sich um einen Entwurf vor Ablauf der außergerichtlichen Antwortfrist am 12. Oktober. Weder eine Einreichung noch eine Zustellung dieser Zivilklage hat stattgefunden. Die wesentlich höhere prozessuale Kostenbelastung im Verhältnis zur Forderung wird durch die sachliche Zuständigkeit nicht beseitigt; der Entwurf nimmt eine Entscheidung über die tatsächliche Einreichung nicht vorweg.

## 2 Rechtsweg und Zuständigkeit

Die geltend gemachte Pflichtverletzung betrifft die hoheitliche Bearbeitung eines Antrags auf Sondernutzungserlaubnis und eine dienstliche Auskunft hierzu. Art. 34 Satz 3 GG eröffnet für den Schadensersatzanspruch den ordentlichen Rechtsweg. Gemäß § 71 Abs. 2 Nr. 2 GVG ist das Landgericht unabhängig vom Streitwert ausschließlich sachlich zuständig. § 23 Nr. 1 GVG mit der seit 2026 geltenden Grenze von 10.000 EUR führt bei Amtshaftungsansprüchen nicht zum Amtsgericht. Die Beklagte hat ihren Sitz in Würzburg; dort wurden die unrichtige Auskunft erteilt und die nachteilige Entscheidung getroffen. Die örtliche Zuständigkeit folgt aus §§ 17, 32 ZPO.

Gegenstand ist ein eigener reiner Vermögensschaden des Klägers. Er begehrt weder nachträglichen Erlass einer für Juni bestimmten Erlaubnis noch verwaltungsgerichtliche Feststellung der Genehmigungsfähigkeit. Eine unzulässige Klage gegen die einzelne Sachbearbeiterin wird nicht erhoben. Die Haftung richtet sich bei Vorliegen der Voraussetzungen gegen die Anstellungskörperschaft.

## 3 Antrag und Fehler im Verwaltungsablauf

Der Kläger beantragte am 28. April 2026, am 20. und 21. Juni jeweils von 09:00 bis 17:00 Uhr auf dem Krummblattplatz einen mobilen Kaffee- und Teestand aufstellen zu dürfen. Beansprucht wurden drei mal zwei Meter, ohne Alkohol, Sitzplätze oder Musik. Die Restgehwegbreite sollte mindestens 2,50 Meter betragen. Es ging um eine eigenständige straßenrechtliche Sondernutzung neben einem Handwerkertag, nicht um eine vom Veranstalter weiterzugebende Standberechtigung. Wasser und Strom sollten selbst mitgeführt werden. Am 29. April bestätigte die Sachbearbeiterin Edeltraud Merk die Vollständigkeit und die zutreffenden Junidaten.

Beweis: Antrag und Eingangsbestätigung, Anlagen K1 und K2. Für die Aktenbearbeitung wird Zeugnis der Edeltraud Merk, zu laden über Stadt Würzburg, Sachgebiet Sondernutzung, Mainlaubplatz 1, 97070 Würzburg, angeboten.

Im Register wurden gleichwohl der 20. und 21. Juli eingetragen. Der Vorgang erhielt deshalb eine Wiedervorlage erst für den 29. Juni. Eine Ortsprüfung am 7. Mai ergab 2,55 Meter Restgehwegbreite und keine entgegenstehenden örtlichen Hindernisse. Sachgebietsleiter Eberhard Abelein bewertete das Vorhaben am 11. Mai intern als zustimmungsfähig. Ein unterschriebener Bescheid existierte nicht. Die Sachbearbeiterin bereitete Entscheidungen vor; zur Erteilung war der Sachgebietsleiter befugt.

Beweis: Registerauszug und Erklärung der Sachgebietsleitung, Anlagen K3 und K6; Zeugnis des Eberhard Abelein, zu laden über die genannte Dienststelle. Die Klage setzt eine positive Vorbewertung nicht mit einer wirksamen Erlaubnis gleich. Sie legt ebenso wenig eine erfundene gebundene Bewilligungspflicht nach einer nicht vorliegenden Satzung zugrunde. Art. 18 BayStrWG bildet den straßenrechtlichen Rahmen. Die konkrete damalige Zulässigkeit und eine rechtzeitige Entscheidungsmöglichkeit werden durch die vorgenannten Tatsachen und die befugte Person belegt.

Am 15. Juni erhielt der Kläger auf seine Nachfrage eine E-Mail, wonach es um einen Stand im Juli gehe. Am 16. Juni um 08:12 Uhr korrigierte er dies, verwies auf den vollständigen Aprilantrag, den bereits gemieteten Wagen und die bis 17. Juni 18:00 Uhr begrenzte halbe Stornierung. Er bat um Entscheidung bis Donnerstag. Dabei erwähnte er, dass er von gerichtlichem Eilrechtsschutz gelesen habe. Eine rechtzeitige schriftliche Korrektur oder Warnung, dass die Entscheidung ungesichert bleibe, erhielt er nicht.

Beweis: E-Mail-Auskunft und dringende Nachfrage, Anlagen K4 und K5. Eine bloße Sachstandsanfrage ohne Termin- oder Schadenshinweis wird dem Gericht damit nicht unterbreitet.

## 4 Mietvertrag und zweite Entscheidungsmöglichkeit

Der Kläger hatte den Wagen „Spatz“ am 2. Juni für das Wochenende gemietet und am 8. Juni 238,00 EUR einschließlich Umsatzsteuer bezahlt. Bei Absage bis zum 17. Juni 18:00 Uhr wäre die Hälfte zurückerstattet worden; danach blieb ohne Weitervermietung der volle Mietpreis geschuldet. Die Beschaffung der behördlichen Erlaubnis war sein Risiko gegenüber der Vermieterin. Er ließ die reguläre Frist aus Hoffnung auf die Korrektur verstreichen. Die erst am 18. Juni erteilte Auskunft wird nicht nachträglich als Ursache dieser bereits abgeschlossenen Entscheidung dargestellt.

Beweis: Mietrechnung mit Bedingungen und ursprüngliche Forderung, Anlagen K7 und K9.

Am 18. Juni um 08:46 Uhr bot die Vermieterin Karla Storch per Nachricht einmalig an, bei verbindlicher Absage bis 12:00 Uhr doch noch 119,00 EUR zurückzuzahlen. Dies war eine nachträgliche Kulanz, keine andere ursprüngliche Vertragsklausel. Der Kläger antwortete um 08:52 Uhr, er werde die Angelegenheit sofort mit der Stadt klären. Das Angebot war von einer Weitervermietung unabhängig. Bei rechtzeitiger Absage hätte Frau Storch die Hälfte tatsächlich erstattet.

Beweis: Ergänzende Nachricht vom 1. Oktober mit vollständiger Wiedergabe des kurzen Verlaufs, Anlage K10; Zeugnis der Karla Storch, Saatlaubenweg 8, 97076 Würzburg; Augenschein des auf ihrem Geschäftstelefon gespeicherten Nachrichtenverlaufs, dessen Vorlage sie zugesagt hat. Die nachträgliche E-Mail wird nicht als technische Sicherung einer damals exportierten Originaldatei bezeichnet. Zur Echtheit und Vollständigkeit steht die Verfasserin zur Verfügung.

Die Nachricht vom 23. Juni widerspricht dem nicht. Sie betrifft die tatsächliche Absage am Freitag, dem 19. Juni, um 16:22 Uhr. Zu diesem Zeitpunkt waren sowohl die reguläre Frist als auch die neue einmalige Kulanz abgelaufen. Die dort verneinte kostenlose Umbuchung ist ebenfalls etwas anderes als die befristete halbe Erstattung. Der Wagen wurde nach der tatsächlichen Absage nicht weitervermietet; es gab keine nachträgliche Einnahme oder Gutschrift.

Beweis: Bestätigung der Vermieterin vom 23. Juni, Anlage K8, sowie ihr Zeugnis.

## 5 Unzutreffende Auskunft am 18. Juni

Um etwa 09:35 Uhr rief der Kläger Frau Merk an und nannte das bis mittags bestehende Kulanzangebot. Sie erklärte sinngemäß, der Fehler sei geklärt und er bekomme die Erlaubnis am nächsten Tag. Das Register war jedoch noch nicht berichtigt; eine unterschriftsreife Vorlage war nicht an den Sachgebietsleiter gegeben worden. Eine verbindliche Zusage über die Zeichnung lag nicht vor. Frau Merk erläuterte diese Unsicherheit nicht. Sie schloss lediglich aus der positiven Ortsprüfung auf eine schnelle Erledigung.

Beweis: Ergänzende dienstliche Erklärung der Frau Merk vom 1. Oktober, Anlage K11; ihr Zeugnis zum Inhalt, zum Kenntnisstand und zur fehlenden Zeichnungsabsprache. Der Kläger bietet ergänzend seine persönliche Anhörung an. Es existiert keine Tonaufnahme und keine zeitgleiche Gesprächsniederschrift. Die gegenüber der ursprünglichen vorsichtigen Erinnerung präzisierte Erklärung wird ausdrücklich als spätere Erinnerung kenntlich gemacht.

Der Kläger unterließ nach dem Gespräch die Absage. Bei wahrheitsgemäßer Information, dass eine Entscheidung für Freitag nicht abgesprochen war, hätte er vor zwölf Uhr storniert. Er hielt sein Telefon bereit und konnte die Vermieterin unmittelbar erreichen. Er verfügte über keine bindenden Vorbestellungen, die das zusätzliche Risiko gerechtfertigt hätten. Die positive bestimmte Auskunft gab für sein weiteres Abwarten den Ausschlag. Am Freitagnachmittag war eine rechtzeitige Unterschrift nicht mehr erreichbar; um 16:22 Uhr sagte er den Wagen ab.

Beweis: Erklärung des Klägers vom 2. Oktober, Anlage K12, und persönliche Anhörung gemäß § 141 ZPO; Zeugnis der Frau Merk zum mitgeteilten Entscheidungsdruck; Zeugnis der Frau Storch zur Erreichbarkeit und ausbleibenden Absage. Eine Parteivernehmung bleibt den gesetzlichen Voraussetzungen vorbehalten. Dass der Kläger die erste Frist aus Hoffnung verstreichen ließ, ist ein gegenläufiger Umstand, beseitigt aber nicht ohne Weiteres seine erst danach eröffnete neue Entscheidungsmöglichkeit.

## 6 Amtspflichtverletzung

Die Anspruchsgrundlage ist § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG. Die mit einer konkreten Antragssache befasste Amtsträgerin musste vollständige, richtige und ihrem tatsächlichen Kenntnisstand entsprechende Auskunft erteilen. Die Pflicht diente gerade dem Kläger, dessen Disposition und bezifferte Zusatzkosten bekannt waren. Sie erfasste auch die Grenze ihrer eigenen Befugnis. Aus einer internen positiven Vorprüfung durfte sie keine sichere Erlaubnis für den nächsten Tag ableiten, ohne die befugte Stelle einbezogen zu haben.

Das Verschulden liegt nicht allein in der später festgestellten Verzögerung. Frau Merk wusste, dass keine Zeichnungsabsprache bestand, und hatte den vom Kläger genannten Stornotermin vor Augen. Bereits die gebotene einfache Prüfung des Bearbeitungsstands hätte eine bestimmte Zusage ausgeschlossen. Die am 5. Oktober erteilte Stellungnahme der Rechtsstelle bestätigt, dass eine solche Auskunft nicht hätte gegeben werden dürfen. Die Beklagte bestreitet jedoch weiterhin Zurechnung und Schadensabwendungsmöglichkeiten.

Beweis: Stellungnahme der Beklagten, Anlage K14. Ein Anerkenntnis des gesamten Zahlungsanspruchs wird daraus nicht hergeleitet.

Die unrichtige Julierfassung und verspätete Weitergabe erklären, weshalb die Situation entstand. Für den beschränkt geltend gemachten Betrag genügt der engere Ursachenzusammenhang zwischen falscher Donnerstagsauskunft und nicht genutzter konkreter Kulanz. Es muss nicht unterstellt werden, eine ordnungsgemäße Bearbeitung hätte zwingend jeden wirtschaftlichen Erfolg des Wochenendverkaufs gesichert. Selbst wenn der befugte Leiter noch rechtmäßig hätte ablehnen können, hätte eine zutreffende Auskunft den Kläger zur kostengünstigeren Absage veranlasst.

## 7 Schaden und rechtmäßiges Alternativverhalten

Der Kläger verlangt keine abstrakte Vergütung ausgefallener Geschäftschancen. Der gezahlte Betrag beträgt 238,00 EUR. Bei zutreffender Information und Absage bis 12:00 Uhr wäre seine endgültige Belastung nach dem konkreten Angebot auf 119,00 EUR gesunken. Die Differenz beträgt genau 119,00 EUR. Bereits vor dem Telefonat unvermeidbar gewordene 119,00 EUR werden von ihm selbst getragen. Damit wird die frühere Forderung von 238,00 EUR ersetzt und nicht um eine weitere Position ergänzt. Die Beschränkung samt neuer Entscheidungskette wurde der Beklagten im Schreiben vom 2. Oktober, Anlage K13, mitgeteilt.

Die Wagenmiete ist nicht schon wegen der fehlenden Nutzung automatisch in voller Höhe ersatzfähig. Die Klage stützt sich auf eine konkret verlorene vertragliche Rückzahlungsmöglichkeit. Eine hypothetische schlechte Umsatzentwicklung berührt diesen abgesonderten Vertrauensschaden nicht. Der Kläger wendet die Kleinunternehmerregelung an und kann aus der Rechnung keine Vorsteuer abziehen. Eine Erstattung, spätere Gutschrift oder anderweitige Wagenverwendung gab es nicht. Eingekaufte Waren konnte er weiterverwenden; dafür und für unbelegte Gewinne verlangt er nichts.

Die Vermieterin haftet nach den vorhandenen Vereinbarungen nicht wegen der Versagung der Sondernutzung. Sie hielt den Wagen bereit und bot sogar zusätzliche Kulanz. Eine anderweitige Ersatzmöglichkeit für denselben Betrag ist nicht ersichtlich. Ob der Kläger bei richtiger Information wirklich abgesagt hätte, ist eine nach den konkreten Umständen zu würdigende Kausalitätsfrage; sie wird nicht allein durch die spätere Selbstauskunft als bewiesen ausgegeben.

## 8 Schadensabwendung und Gegenargumente

§ 839 Abs. 3 BGB setzt ein schuldhaft unterlassenes, zur Abwendung des Schadens geeignetes Rechtsmittel voraus. Hierzu genügt nicht die abstrakte Feststellung, der Kläger habe keinen Antrag nach § 123 VwGO gestellt. Zu prüfen sind Zeitpunkt, Zumutbarkeit und mögliche Wirkung. Am 16. Juni machte er den Fehler schriftlich geltend, verlangte eine kurzfristige Entscheidung und wies auf konkrete Kosten hin. Für eine einfache straßenrechtliche Sondernutzung ist in Bayern nach Art. 12 Abs. 2 AGVwGO grundsätzlich kein Vorverfahren durchzuführen; verwaltungsgerichtlicher Eilrechtsschutz kam jedoch in Betracht.

Die Klägerseite verkennt nicht, dass ein Eilantrag bereits am 16. Juni Anlass zur beschleunigten Prüfung hätte geben können. Die Beklagte müsste für einen Ausschluss darlegen, welches bei zumutbarem Verhalten rechtzeitig erreichbare Ergebnis gerade den eingeklagten Schaden abgewendet hätte. Eine sichere Entscheidung innerhalb weniger Tage, erst recht zwischen 09:35 und 12:00 Uhr am Donnerstag, kann nicht ohne Tatsachengrundlage unterstellt werden. Der Kläger begehrte keinen unklaren zukünftigen Termin, sondern erhielt von der unmittelbar zuständigen Sachbearbeitung eine bestimmte Erledigungsankündigung. Diese neue Auskunft ist für die Zumutbarkeit weiteren Rechtsschutzes zu berücksichtigen.

Nach § 254 BGB ist ferner zu würdigen, dass er zunächst auf Hoffnung vertraute und schon eine Stornofrist verstreichen ließ. Diesem Gesichtspunkt trägt die Beschränkung des Anspruchs Rechnung, ohne damit jede weitere Kürzung auszuschließen. Für die zweite Frist lag eine neue, wesentlich bestimmtere Information vor. Es war nicht erforderlich, dass Frau Merk den Bescheid selbst erteilen konnte; entscheidend ist, dass sie als bearbeitende Amtsträgerin eine angeblich gesicherte Erledigung mitteilte. Der Kläger durfte keine formelle Erlaubnis aus einem Telefonat ableiten, musste die ihm verschwiegene fehlende Zeichnungsabsprache aber auch nicht erraten.

## 9 Zinsen und Verfahrensumfang

Zinsen werden aus §§ 291, 288 Abs. 1 BGB ab dem Tag nach einer tatsächlichen späteren Zustellung beantragt. Ein Anspruch auf neun Prozentpunkte wird nicht erhoben; die Ersatzforderung ist keine Entgeltforderung. Eine bereits eingetretene Rechtshängigkeit oder ein abgelaufener außergerichtlicher Zahlungstermin wird nicht behauptet.

Der geringe Betrag legt eine außergerichtliche Einigung nahe, beseitigt aber weder die Amtspflicht noch die gesetzliche Zuständigkeit. Der Entwurf legt die ursprüngliche höhere Forderung, den später gefundenen Nachrichtenaustausch und die gegenläufigen Umstände offen. Über die Beweiswürdigung wird keine vorweggenommene Sicherheit behauptet.

Dr. Nadia Wolfram
Rechtsanwältin
Entwurfsfassung ohne Unterschrift und ohne Einreichung'''),
    ]))

CASES.append(dict(
    slug='akha-wuerzburg-baugenehmigung',
    attachments={},
    claim_file='16_Klageentwurf.docx',
    notes='Gegnerischer Entwurf. Neue Kundenbestätigung ändert die bislang ausschließlich auf Mietaufwand gestützte Berechnung: 1.080 EUR Honorar minus 180 EUR variable Kosten minus 80 EUR hypothetische Kreditzinsen plus 40 EUR tatsächliche Bereitstellung = 860 EUR. Die Miete fällt beidseits an. Anlagenverzeichnis aus exhibits ergänzen.',
    exhibits=[
        exhibit(1, '02_Antragsbeschreibung.docx', 'Betriebsbeschreibung, Wandöffnung und Vollständigkeitsvermerk'),
        exhibit(2, '03_Versagungsbescheid.docx', 'Versagung aufgrund eines nicht beantragten Maschinenbetriebs'),
        exhibit(3, '04_Klage.eml', 'Bestätigung der rechtzeitig erhobenen Verpflichtungsklage'),
        exhibit(4, '05_Bearbeitungsvermerk.docx', 'Entscheidungsreife, Zuordnungsfehler und Abhilfebearbeitung'),
        exhibit(5, '06_Abhilfe_Genehmigung.docx', 'Genehmigung des unveränderten Vorhabens vom 03.08.2026'),
        exhibit(6, '07_Mietvertrag.docx', 'Feste Raummiete ab Juni'),
        exhibit(7, '08_Bankabrechnung.docx', 'Tatsächlich berechnete Bereitstellungszinsen'),
        exhibit(8, '09_Zahlungsnachweis.docx', 'Mietzahlungen, Zwischennutzung und tatsächlicher Ausbau'),
        exhibit(9, '10_Forderung.eml', 'Ursprüngliche, nun ersetzte Forderungsberechnung'),
        exhibit(10, 'schriftverkehr-und-klage/11_Kundenauftrag.eml', 'Bestätigung eines entfallenen verbindlichen Beratungspakets'),
        exhibit(11, 'schriftverkehr-und-klage/12_Ausbaukapazitaet.eml', 'Konkrete damalige Handwerkerverfügbarkeit'),
        exhibit(12, 'schriftverkehr-und-klage/13_Finanzierungsvergleich.eml', 'Zinsen bei planmäßigem Abruf und tatsächliche Bereitstellung'),
        exhibit(13, 'schriftverkehr-und-klage/14_Neuberechnung.pdf', 'Ersetzende Differenzberechnung über 860,00 EUR'),
        exhibit(14, 'schriftverkehr-und-klage/15_Antwort_Stadt.pdf', 'Einwendungen zu Zeitpunkt, Kundenabsage und Eilrechtsschutz'),
    ],
    documents=[
        document('11_Kundenauftrag.eml', 'Beratungspaket Juni/Juli – Bestätigung des damaligen Auftrags', '2026-10-01T11:25:00+02:00', 'email', '''Sehr geehrte Frau Weller,

ich bestätige für die Formblatt Innenräume GmbH den am 11. Mai mit Frau Adebayo vereinbarten Auftrag. Sie sollte für uns zwei aufeinander aufbauende Material- und Farbberatungen am 12. Juni und 10. Juli 2026 durchführen. Der Gesamtfestpreis betrug 1.080,00 EUR netto zuzüglich gesetzlicher Umsatzsteuer. Es war ein zusammengehörendes Paket, keine unverbindliche Reservierung. Die Treffen sollten in ihrem neuen Büro am Haselkornbogen stattfinden. Wegen der noch nicht veröffentlichten Entwürfe hatten wir ausdrücklich einen abgeschlossenen Beratungsraum vereinbart. Ein offener Arbeitsplatz oder eine Videokonferenz genügte uns nicht. Wir selbst hatten während unseres Ladenumbaus keinen geeigneten Besprechungsraum.

Am 8. Juni erklärte Frau Adebayo, dass die Nutzung versagt worden sei und der Ausbau deshalb noch nicht begonnen habe. Wir hatten für das erste Treffen den 12. Juni als letzten Termin vor einer internen Freigabe festgelegt. Unter diesen Umständen beendeten wir am selben Tag das gesamte Paket entsprechend unserer Terminvereinbarung ohne Vergütung. Die zweite Sitzung setzte die erste voraus. Wir beauftragten am 9. Juni ein anderes Büro; eine Nachholung bei Frau Adebayo gab es nicht. Wäre das vereinbarte Büro verfügbar gewesen, hätten wir beide Leistungen abgerufen und den Preis gezahlt. Wir waren zahlungsfähig und hatten das Budget freigegeben.

Die von Frau Adebayo eingeplanten gedruckten Materialmappen wurden nicht hergestellt. Laut ihrer Auftragskalkulation entfielen darauf 180,00 EUR netto Fremddruckkosten. Ob ihr Druckdienstleister diesen Preis tatsächlich verbindlich angeboten hatte, kann ich nicht aus eigener Kenntnis bestätigen. Wir selbst haben ihr weder Auslagen noch eine Stornopauschale bezahlt. Weitere Vergütung für Vorarbeiten war nicht vereinbart. Bei der Behörde hatte ich zuvor keine Angaben gemacht; Frau Adebayo fragte mich erst jetzt nach einer schriftlichen Bestätigung.

Mit freundlichen Grüßen
Aurelia Gharbi
Geschäftsführerin, Formblatt Innenräume GmbH
Rosmarinlaubenweg 4, 97074 Würzburg''', 'Aurelia Gharbi <a.gharbi@formblatt-innenraeume.example>', 'Rechtsanwältin Anja Weller <anja@weller-recht.example>'),
        document('12_Ausbaukapazitaet.eml', 'Büro Adebayo – unser Terminfenster im Mai', '2026-10-02T09:15:00+02:00', 'email', '''Sehr geehrte Frau Weller,

ich habe unseren internen Kalender geprüft. Am 13. Mai besprach ich mit Frau Adebayo telefonisch folgendes Zeitfenster: Wenn die schriftliche Genehmigung bis 20. Mai vorliegt und sie den Ausbau dann beauftragt, beginnen wir am 22. Mai mit Abstützung und Wandöffnung. Elektro und Heizkörper waren für den 26./27. Mai vorgesehen, Abschluss bis 29. Mai mit Restpuffer bis 31. Mai. Ohne Genehmigung und Auftrag würden wir nicht anfangen. Frau Adebayo erklärte telefonisch, das dann so machen zu wollen. Ich trug diese bedingte Planung in unseren internen Kalender ein. Es gab keine schriftliche Terminreservierung gegenüber Frau Adebayo und noch keinen unbedingt erteilten Bauauftrag. Ihre frühere Angabe einer mündlichen Auskunft ist richtig. Mein heutiges Schreiben macht aus dieser Absprache keine damals ausgetauschte E-Mail. Für den kleinen Auftrag waren mein Mitarbeiter Milan Arendt und ich vorgesehen. Die Elektroarbeiten hatte Jana Rebhuhn für den 26. Mai eingeplant; sie kann ihren damaligen Kalender bestätigen.

Am 14. Mai klärte ich den Zutritt telefonisch unmittelbar mit Herrn Alfons Späth, Haselkornbogen 7, 97074 Würzburg. Er sagte zu, uns nach Vorlage der Genehmigung an den vorgesehenen Bautagen ab 22. Mai morgens aufzuschließen und abends wieder abzuschließen. Eine Schlüsselübergabe an die Mieterin oder eine Büronutzung vor dem 1. Juni war damit nicht verbunden. Der Raum war leer. Herr Späth kann diese gesonderte Zutrittsabsprache bestätigen. Die geprüfte Sturzberechnung, Heizkörper und Leitungsmaterial waren rechtzeitig vorhanden. Unser Angebot umfasste insgesamt 8.000,00 EUR einschließlich der beteiligten Gewerke. Bei Fertigstellung Ende Mai hätten wir am 29. Mai die Schlussrechnung gestellt. Wir hatten Zahlungsziel bis 5. Juni zugesagt; eine Vorfinanzierung durch einen vorzeitigen Kreditabruf war nicht erforderlich. Es fehlte im Mai nach unserer Kenntnis allein die Genehmigung. Über deren gesetzliche Bearbeitungsdauer kann ich nichts sagen.

Als bis 20. Mai keine Freigabe vorlag, mussten wir das Fenster aufgeben. Tatsächlich arbeiteten wir nach Vorlage der Augustgenehmigung vom 6. bis 14. August. Der Umfang blieb gegenüber unserem Maiangebot gleich. Die im Gebäude nötige Wandöffnung war eine tragende Innenwand, kein bloßer Einbau einer Bürotür in eine leichte Trennwand.

Mit freundlichen Grüßen
Fridolin Aumüller
Aumüller Ausbau, Schilfkornweg 16, 97076 Würzburg''', 'Fridolin Aumüller <buero@aumueller-ausbau.example>', 'Rechtsanwältin Anja Weller <anja@weller-recht.example>'),
        document('13_Finanzierungsvergleich.eml', 'Kredit Adebayo – Ergänzung zur Abrechnung vom 5. August', '2026-10-02T12:40:00+02:00', 'email', '''Sehr geehrte Frau Adebayo, sehr geehrte Frau Weller,

mit Einverständnis unserer Kundin erläutere ich den Vergleich für Juni und Juli. Bei Vorlage der Genehmigung und einer vollständigen Schlussrechnung Ende Mai hätte der vereinbarte Betrag von 8.000,00 EUR zum 1. Juni vollständig ausgezahlt werden können. Der Darlehenszins beträgt fest 6,00 Prozent jährlich. Für zwei volle Zinsmonate hätten sich 80,00 EUR reguläre Zinsen ergeben. In diesen ersten beiden Monaten war noch keine Tilgung vorgesehen. Eine zusätzliche Bereitstellungsgebühr wäre auf den vollständig ausgezahlten Betrag nicht mehr angefallen.

Tatsächlich blieb der Kredit in Juni und Juli vollständig unabgerufen. Deshalb wurden nur die bereits belegten 40,00 EUR Bereitstellungszinsen berechnet. Die Differenz für diese beiden Monate beträgt somit zugunsten der Kundin 40,00 EUR. Wer den Schaden mit einem planmäßigen Abruf zum 1. Juni vergleicht, darf die regulären Zinsen von 80,00 EUR nicht weglassen und nur die tatsächlichen 40,00 EUR als Mehrkosten zählen.

Ob der Ausbau bei einer bestimmten behördlichen Bearbeitung wirklich Ende Mai abgeschlossen gewesen wäre, können wir nicht bestätigen. Die Auszahlung setzte die tatsächliche Vorlage beider Unterlagen voraus. Unsere Auskunft betrifft ausschließlich die vertragliche Finanzierung und die Rechenfolge. Andere Kreditkosten, Tilgungsbeträge oder Kosten des Verwaltungsgerichtsverfahrens sind in diesen Zahlen nicht enthalten.

Mit freundlichen Grüßen
Beate Heckenast
Genossenschaftliche Musterbank Mainlaub eG
Buchenfächerweg 10, 97070 Würzburg''', 'Beate Heckenast <beate.heckenast@mainlaub-bank.example>', 'Tola Adebayo <tola@adebayo-planung.example>, Rechtsanwältin Anja Weller <anja@weller-recht.example>'),
        document('14_Neuberechnung.docx', 'Adebayo – ersetzende Schadensberechnung', '02.10.2026', 'letter', '''Rechtsanwältin Anja Weller
Weidenblütenweg 6, 97074 Würzburg

An die Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

die Forderung vom 30. September wird nach ergänzender Prüfung durch eine Forderung von 860,00 EUR ersetzt. Die damalige Aufstellung enthielt 840,00 EUR Miete und 40,00 EUR Bereitstellungszinsen. Die Miete wäre jedoch bei rechtmäßiger Nutzung ebenso angefallen. Meine Mandantin kann sie nicht ohne Weiteres als zusätzlichen Vermögensabfluss ansetzen. Ebenso sind bei dem ursprünglich geplanten Kreditabruf ersparte reguläre Zinsen zu berücksichtigen.

Neu liegt die Bestätigung der Formblatt Innenräume GmbH vor. Sie hatte am 11. Mai zwei zusammengehörende Beratungen am 12. Juni und 10. Juli für insgesamt 1.080,00 EUR netto fest beauftragt. Der Auftrag entfiel am 8. Juni, weil das zugesagte abgeschlossene Büro mangels Genehmigung und Ausbau nicht verfügbar war. Eine Nachholung, Vergütung oder Ersatzbuchung gab es nicht. Die zunächst allein auf Raumkosten gerichtete Forderung beruhte darauf, dass meine Mandantin die geschäftliche Absage noch nicht schriftlich vorlegen konnte. Nun wird ausdrücklich der entgangene Deckungsbeitrag geltend gemacht; eine zusätzliche Erstattung der Mieten wird nicht verlangt.

Vom Honorar sind 180,00 EUR netto nicht angefallene Fremddruckkosten abzuziehen. Meine Mandantin hatte hierfür ein Angebot von Otmar Selim, Druckerei Papierfächer, erhalten. Die Mappen wurden nicht bestellt; der Anbieter kann Preis und fehlende Lieferung bestätigen. Weitere umsatzabhängige Fremdkosten waren bei diesem Paket nicht vorgesehen. Ihre eigene Zeit konnte meine Mandantin für allgemeine Bürovorbereitung nutzen; eine andere vergütete Arbeit ersetzte die ausgefallenen Sitzungen nicht.

Damit ergibt sich zunächst ein ausgefallener Deckungsbeitrag von 900,00 EUR. Bei planmäßigem Abruf wären 80,00 EUR Kreditzinsen angefallen, tatsächlich entstanden 40,00 EUR Bereitstellung. Diese Ersparnis von 40,00 EUR wird abgezogen. Es verbleiben 860,00 EUR. Die Vorsteuer aus nicht hergestellten Druckmappen und Umsatzsteuer auf nicht erbrachte Beratungen werden nicht als Schaden beansprucht.

Herr Aumüller bestätigt das konkrete Ausbauzeitfenster bei einer Genehmigung bis 20. Mai. Ihr eigener Vermerk bezeichnet den Antrag seit 12. Mai als entscheidungsreif; am 19. Mai lag bereits ein Entwurf zur Unterschrift vor, allerdings mit dem fremden Maschinenbetrieb. Bitte erläutern Sie deshalb konkret, welche sachlichen Kontrollschritte bei richtiger Zuordnung noch bis nach dem 20. Mai erforderlich gewesen wären. Wir behaupten keine gesetzliche Genehmigungsfrist bis zu unserem Wunschtermin.

Die gesetzte Antwortfrist bis 12. Oktober bleibt bestehen. Verwaltungsgerichtliche Kosten sind weiterhin nicht Gegenstand dieser Forderung.

Mit freundlichen Grüßen
Anja Weller
Rechtsanwältin'''),
        document('15_Antwort_Stadt.docx', 'Adebayo – neue Forderungsgrundlage und offene Kausalität', '05.10.2026', 'letter', '''Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

An Rechtsanwältin Anja Weller
Weidenblütenweg 6, 97074 Würzburg

Sehr geehrte Frau Weller,

wir nehmen zur Kenntnis, dass Ihre Mandantin nun 860,00 EUR aus einem ausgefallenen konkreten Auftrag verlangt und die frühere Addition von Mietaufwand und Bereitstellungszinsen ersetzt. Die zusätzliche Kundenbestätigung und der Finanzierungsvergleich werden berücksichtigt. Die ursprüngliche Forderung bleibt zur Dokumentation der Entwicklung in der Akte.

Der Zuordnungsfehler im Versagungsbescheid und die unveränderte Genehmigung vom 3. August werden nicht in Abrede gestellt. Auch die Vorbereitung eines Entwurfs am 19. Mai ist dokumentiert. Daraus folgt aus unserer Sicht jedoch nicht schon, dass bei richtiger Bearbeitung bis zum 20. Mai unterschrieben und bekannt gegeben worden wäre. Die abschließende Kontrolle war noch offen. Aus dem Kalender lässt sich deren hypothetischer Ablauf nicht verlässlich rekonstruieren. Wir können derzeit keinen zusätzlichen materiellen Ablehnungsgrund benennen, der bei der Augustprüfung festgestellt worden wäre.

Zur neuen Kundenforderung fragen wir, weshalb keine andere geeignete Besprechungsmöglichkeit verwendet werden konnte und ob der Auftrag trotz der Versagung wenigstens teilweise hätte erhalten werden können. Ebenso bedarf die Höhe der ersparten Druckkosten einer Bestätigung durch den Anbieter; die Kundin hat dazu ausdrücklich keine eigene Kenntnis. Ihre neue Berechnung berücksichtigt zwar die regulären Kreditzinsen. Auch weitere ersparte Ausgaben oder tatsächliche Ersatzaufträge wären jedoch einzubeziehen.

Die Verpflichtungsklage vom 17. Juni und Ihre Erinnerungen sind bekannt. Ob ein früher oder zusätzlich beantragter vorläufiger Rechtsschutz den Schaden hätte vermeiden können, bleibt rechtlich und tatsächlich zu prüfen. Allein aus der späteren Abhilfe ergibt sich keine Entscheidung über den Zahlungsanspruch. Die Erklärung der Erledigung im Verwaltungsprozess wird in diesem Schreiben weder angegriffen noch kostenrechtlich bewertet.

Eine Anerkennung des Betrags ist damit nicht verbunden. Eine abschließende Stellungnahme innerhalb der laufenden Antwortfrist wird vorbereitet. Die vorhandenen Bearbeitungsvermerke werden unverändert aufbewahrt; eine nachträgliche sichere Rekonstruktion des hypothetischen Zeichnungstags liegt nicht vor.

Mit freundlichen Grüßen
Gertraud Holler
Rechtsstelle'''),
        document('16_Klageentwurf.docx', 'Klageentwurf Adebayo gegen Stadt Würzburg', '05.10.2026', 'claim', '''ENTWURF – NICHT EINGEREICHT
Stand: 5. Oktober 2026

An das Landgericht Würzburg
Ottostraße 5, 97070 Würzburg

## 1 Parteien und Anträge

In dem Rechtsstreit der Tola Adebayo, Haselkornbogen 5, 97074 Würzburg, Klägerin, Prozessbevollmächtigte: Rechtsanwältin Anja Weller, Weidenblütenweg 6, 97074 Würzburg,

gegen die Stadt Würzburg, vertreten durch den Oberbürgermeister, Mainlaubplatz 1, 97070 Würzburg, Beklagte,

wird beantragt, die Beklagte zu verurteilen, an die Klägerin 860,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz ab dem auf die Zustellung der Klage folgenden Tag zu zahlen und die Kosten des Rechtsstreits zu tragen. Der Streitwert beträgt 860,00 EUR.

Dieser Entwurf betrifft eine noch nicht erhobene Zivilklage. Das frühere Verfahren vor dem Verwaltungsgericht betraf die Erteilung einer Baugenehmigung. Ein gerichtliches Aktenzeichen wird mangels entsprechender Unterlage nicht erfunden. Die außergerichtliche Antwortfrist vom 12. Oktober ist am Entwurfstag noch nicht abgelaufen. Vorgerichtliche Rechtsanwaltskosten, verwaltungsgerichtliche Verfahrenskosten und ein Feststellungsantrag werden nicht in den Zahlungsantrag aufgenommen.

## 2 Zuständigkeit und Beteiligtenstellung

Die Beklagte ist als kreisfreie Stadt selbst untere Bauaufsichtsbehörde nach Art. 53 BayBO. Die Klage richtet sich gegen sie wegen der Bearbeitung ihres eigenen Bauverfahrens, nicht gegen eine kreisangehörige Gemeinde wegen einer Entscheidung des Landratsamts. Die Verantwortung aus § 839 BGB trifft nach Art. 34 GG die Anstellungskörperschaft. Für den Amtshaftungsanspruch ist der ordentliche Rechtsweg eröffnet und gemäß § 71 Abs. 2 Nr. 2 GVG das Landgericht ohne Rücksicht auf den Streitwert ausschließlich sachlich zuständig. Die allgemeine Amtsgerichtsgrenze von 10.000 EUR ändert daran nichts. Sitz der Beklagten, Baugrundstück und Pflichtverletzung liegen in Würzburg; die örtliche Zuständigkeit folgt aus §§ 17, 32 ZPO.

Die Klägerin ist Mieterin und Antragstellerin des für ihre eigene selbständige Tätigkeit vorgesehenen Büros. Sie macht ihren eigenen Vermögensschaden geltend. Eigentum am Gebäude wird nicht behauptet. Insbesondere wird der entgangene Beratungsgewinn nicht zu einem enteignungsrechtlichen Eingriff in Grundstückseigentum umgedeutet. Die Klage beruht auf der verletzten Amtspflicht zur zutreffenden und sachgerechten Bearbeitung ihres konkreten Antrags.

## 3 Vorhaben und Genehmigungserfordernis

Am 14. April beantragte die Klägerin, 42 Quadratmeter eines bislang unbeheizten Erdgeschosslagers am Haselkornbogen 5 in ein Büro mit zwei Arbeitsplätzen umzubauen und entsprechend zu nutzen. Das Gebäude besitzt drei Geschosse und sechs Einheiten. Beantragt waren eine 90 Zentimeter breite Öffnung in einer tragenden Innenwand mit berechnetem Sturz, technische Ausstattung und Heizung sowie die Nutzung als Aufenthaltsraum. Die zugehörigen Nachweise zu Statik, Belichtung, Lüftung und Brandschutz lagen vor. Am 17. April wurde die Vollständigkeit vermerkt. Es ging weder um einen Maschinenbetrieb noch um eine Produktionswerkstatt oder regelmäßigen Lieferverkehr.

Beweis: Antragsbeschreibung einschließlich behördlichen Vollständigkeitsnachtrags, Anlage K1; Zeugnis der zuständigen Sachbearbeiterin Yasemin Kraus, zu laden über die Stadt Würzburg, Bauaufsicht, Mainlaubplatz 1, 97070 Würzburg. Die Bauakte wird hinsichtlich dieses Antrags und seiner Nachweise als konkret bezeichnete Behördenakte zur Beiziehung angeregt.

Art. 55 Abs. 1 BayBO bildet den Ausgangspunkt der Genehmigungspflicht. Die Klägerin übersieht die seit 2025 erweiterten Erleichterungen für Nutzungsänderungen nach Art. 57 Abs. 4 Nr. 1 BayBO nicht. Ihr Vorhaben erschöpft sich aber nicht in einer bauplanungsrechtlich gebietstypischen Umbenennung von Räumen: Neu entstehen Anforderungen an Aufenthaltsräume; zugleich wird die tragende Wand eines mehrgeschossigen Gebäudes baulich verändert. Die geltend gemachte Genehmigungsbedürftigkeit wird auf dieses konkrete Gesamtvorhaben gestützt. Die Erweiterung der Nutzungsänderungsfreiheit macht zusätzliche bauordnungsrechtliche Anforderungen nicht gegenstandslos. Vgl. Bayerisches Staatsministerium für Wohnen, Bau und Verkehr, Vollzugshinweise vom 4. Februar 2025, Nr. 8 Buchst. g, S. 12 f.

Das Grundstück liegt im unbeplanten bebauten Bereich mit Wohnen, Büros und kleineren Läden. Die Erschließung war gesichert. Die Nutzung blieb innerhalb des vorhandenen Gebäudes. Die spätere Genehmigung stellte für genau dieses unveränderte Vorhaben die Zulässigkeit nach § 34 BauGB und Art. 68 BayBO fest. Die Klägerin leitet die frühere Genehmigungsfähigkeit nicht allein aus einer später geänderten Rechts- oder Planungslage ab. Eine nachträgliche Planänderung oder zusätzliche tatsächliche Voraussetzung ist nicht dokumentiert. Die zwischen Antrag und Entscheidung in Kraft getretene BayBO-Änderung zum 1. Mai 2026 schafft für diese gewöhnliche Bürokonstellation keine hier tragende neue Erlaubnismöglichkeit.

## 4 Fehlerhafte Versagung und Abhilfe

Frau Kraus vermerkte am 12. Mai die interne Entscheidungsreife. Am 19. Mai lag ein Bescheidentwurf zur Unterschrift vor. Dieser übernahm aus einem anderen Vorgang einen Maschinen- und Lieferbetrieb, weil der Dateiname „Werkraum“ missverstanden und die Betriebsbeschreibung nicht erneut gelesen wurde. Der Bescheid vom 2. Juni, zugestellt am 5. Juni, versagte deshalb die Genehmigung wegen eines Vorhabens, das die Klägerin nicht beantragt hatte. Den tatsächlich beantragten Bürobetrieb behandelte er als nicht beantragt.

Beweis: Versagungsbescheid und Bearbeitungsvermerk vom 28. Juli, Anlagen K2 und K4; Zeugnis von Yasemin Kraus sowie Wolfram Reuther, jeweils zu laden über die Bauaufsicht. Der Vermerk ist eine nachträgliche Rekonstruktion der Vorgänge und wird als solche eingeführt.

Am 17. Juni erhob die Prozessbevollmächtigte Verpflichtungsklage beim Bayerischen Verwaltungsgericht Würzburg und machte den Widerspruch zwischen Antrag und Bescheid geltend. Der bestätigte elektronische Eingang erfolgte um 14:08 Uhr. Die Behörde sagte Prüfung bis Ende der folgenden Woche zu. Am 23. Juni erkannte sie die Zuordnungsfrage, gab jedoch die angekündigte Rückmeldung nicht. Die Bevollmächtigte erinnerte am 30. Juni telefonisch und am 7. Juli schriftlich. Die erneute Ortsprüfung erfolgte erst am 21. Juli und brachte keine neue Anforderung. Am 3. August wurde der ablehnende Bescheid aufgehoben und das unveränderte Vorhaben genehmigt; die Zustellung an die Bevollmächtigte erfolgte am 4. August.

Beweis: Bestätigung der Klageeinreichung, Bearbeitungsvermerk und Abhilfebescheid, Anlagen K3 bis K5. Die elektronische Eingangsbestätigung kann bei Bestreiten aus der anwaltlichen Handakte vorgelegt werden. Es wird keine bereits vorliegende gerichtliche Haftungsfeststellung behauptet. Nach der Abhilfe wurde die Hauptsache für erledigt erklärt. Über dortige Kosten wird in jenem Verfahren entschieden; sie werden nicht doppelt beansprucht.

## 5 Rechtmäßiger Ablauf und Ausbaumöglichkeit

Die Klägerin hatte seit 1. Juni eine feste Mietbindung von monatlich 420,00 EUR. Die Umgestaltung durfte nach dem Mietvertrag und dem öffentlich-rechtlichen Verfahrensstand erst nach Freigabe beginnen. Herr Fridolin Aumüller hatte am 13. Mai telefonisch ein konkretes, von Genehmigung und anschließendem Bauauftrag abhängiges Zeitfenster genannt: Genehmigung bis 20. Mai, Beginn am 22. Mai, Elektro und Heizung am 26./27. Mai, Fertigstellung bis 29. Mai mit Puffer bis 31. Mai. Die Klägerin erklärte telefonisch ihre entsprechende Absicht. Eine schriftliche Terminreservierung gegenüber der Klägerin bestand nicht. Der Unternehmer hielt die bedingte Kapazitätsplanung intern im Kalender fest. Die formelle Schlüsselübergabe an die Klägerin war erst für den 1. Juni vereinbart und erfolgte auch erst dann. Daneben hatte Herr Aumüller am 14. Mai unmittelbar mit dem Vermieter vereinbart, dass dieser nach Vorlage der Genehmigung an den Bautagen ab 22. Mai auf- und abschließen würde. Damit war lediglich der Handwerkerzugang, keine vorzeitige Schlüsselüberlassung oder Büronutzung der Klägerin gemeint. Materialien und berechneter Sturz waren verfügbar. Die Schlussrechnung über insgesamt 8.000,00 EUR hätte Ende Mai gestellt werden können. Tatsächlich wurde derselbe Leistungsumfang nach der Genehmigung vom 6. bis 14. August ausgeführt.

Beweis: Mietvertrag und Zahlungs-/Nutzungsnachweis, Anlagen K6 und K8; neue Terminbestätigung, Anlage K11; Zeugnis des Fridolin Aumüller und des Milan Arendt, beide zu laden über Aumüller Ausbau, Schilfkornweg 16, 97076 Würzburg; Zeugnis der Jana Rebhuhn, Rebhuhn Elektrotechnik, Kornmalvenweg 3, 97076 Würzburg, zu ihrem reservierten Termin. Zum gesondert vereinbarten Handwerkerzugang wird außerdem Zeugnis des Alfons Späth, Haselkornbogen 7, 97074 Würzburg, angeboten. Die nachgereichte Bestätigung konkretisiert die schon zuvor erwähnte mündliche Verfügbarkeit durch einen internen Kalendereintrag und benannte Mitarbeiter; eine damals erteilte schriftliche Reservierung wird weiterhin nicht behauptet.

Die Klägerin behauptet, bei inhaltlich richtiger Prüfung des seit 12. Mai entscheidungsreifen Antrags hätte die Beklagte spätestens am 20. Mai genehmigen und die Entscheidung bekannt geben können. Das ist keine gesetzliche starre Bearbeitungsfrist und folgt nicht allein aus dem Wunsch der Klägerin. Maßgeblich sind die bereits erreichte Entscheidungsreife und der tatsächlich am 19. Mai zur Zeichnung vorliegende Entwurf. Die noch ausstehende Schlusskontrolle wird nicht verschwiegen. Deren bei richtiger Zuordnung nötiger Umfang und Dauer sind streitig. Die Beklagte kann derzeit keinen zusätzlichen materiellen Ablehnungsgrund nennen, rekonstruiert aber keinen sicheren hypothetischen Zeichnungstag.

Beweis: Anlagen K4 und K14; Zeugnis der genannten Bearbeiter zu offen gebliebenen Kontrollschritten. Zur konkreten technischen Ausführbarkeit bis Ende Mai wird bei substantiiertem Bestreiten ergänzend ein Bausachverständigengutachten auf Grundlage der eingereichten Planung und der festgestellten Personal-/Materialverfügbarkeit angeboten. Ein Sachverständiger soll keine unbekannten behördlichen Terminentatsachen ersetzen.

## 6 Konkreter entgangener Auftrag

Am 11. Mai hatte die Formblatt Innenräume GmbH ein zusammengehörendes Paket aus zwei Material- und Farbberatungen am 12. Juni und 10. Juli zu 1.080,00 EUR netto fest beauftragt. Es handelte sich um Büro- und Beratungstätigkeit, nicht um die vom Bescheid fälschlich angenommene Werkstatt. Ein abgeschlossener Raum war wegen vertraulicher noch unveröffentlichter Entwürfe vereinbart. Die Kundin verfügte wegen ihres eigenen Ladenumbaus über keinen geeigneten Besprechungsraum. Ein offener Ausweichplatz oder eine Videokonferenz war nicht akzeptiert. Die Klägerin hätte die Arbeit persönlich erbringen können; es fehlte die vereinbarte nutzbare Räumlichkeit.

Als am 8. Juni feststand, dass der Ausbau noch nicht begonnen hatte und der erste Termin nicht stattfinden konnte, beendete die Kundin das Paket aufgrund der vereinbarten Terminregelung ohne Vergütung. Die zweite Beratung setzte die erste voraus. Ein anderes Büro erhielt am 9. Juni den Auftrag. Die Termine wurden bei der Klägerin nicht nachgeholt; weder eine Stornopauschale noch ein Honorar für Vorarbeiten wurde gezahlt. Es gab keinen ersetzenden vergüteten Auftrag. Die eigenen allgemeinen Bürovorbereitungen der Klägerin führten zu keiner zusätzlichen Einnahme.

Beweis: Bestätigung der Kundin, Anlage K10; Zeugnis der Aurelia Gharbi, zu laden über Formblatt Innenräume GmbH, Rosmarinlaubenweg 4, 97074 Würzburg, zu Vertrag, Terminabhängigkeit, Absagegrund, fehlender Nachholung und Zahlung; persönliche Anhörung der Klägerin zur Durchführungsmöglichkeit und zu Ersatzaufträgen. Die Kundin bestätigt freigegebenes Budget und Zahlungsfähigkeit. Damit wird kein bloßer Umsatzplan eines noch nicht eröffneten Betriebs vorgelegt.

Die Beklagte darf nach Ersatzräumen und Teilrettung des Auftrags fragen. Die Klägerin trägt vor, ihre Wohnung habe keinen abgeschlossenen geeigneten Besprechungsraum geboten; eine andere bezahlte Ersatzanmietung ist nicht erfolgt. Der Vertrag verpflichtete die Kundin nicht, auf ein offenes oder fernmündliches Format auszuweichen. Ob eine rechtzeitig verfügbare zumutbare Alternative bestand, bleibt gegebenenfalls anhand eines konkreten Angebots zu prüfen. Eine beliebige theoretische Raumverfügbarkeit irgendwo in der Stadt beweist noch keine zumutbare Rettungsmöglichkeit vor dem festgelegten Freigabetermin.

## 7 Anspruchsgrund und Schadensvergleich

Die Beklagte verletzte schuldhaft die der Klägerin geschuldete Amtspflicht zur zutreffenden Bescheidung, § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG. Der Fehler war bei einfacher Lektüre der richtigen Betriebsbeschreibung vermeidbar. Die Pflicht schützt die Antragstellerin gerade auch vor wirtschaftlichen Nachteilen, die durch ein rechtswidriges Verhindern der beantragten Nutzung entstehen. Der maßgebliche Vergleich ist die rechtzeitige rechtmäßige Bescheidung, nicht eine Garantie des geschäftlichen Erfolgs. Vgl. BGH, Urteil vom 25. Oktober 2007 – III ZR 62/07, Rn. 10–13. Die spätere Genehmigung ist hierfür ein gewichtiges Beweismittel, aber kein Ersatz für die Prüfung des damals möglichen Ablaufs.

Die Klägerin ersetzt ihre frühere Aufstellung von 880,00 EUR vollständig. Die ursprüngliche Forderung vom 30. September ist als Anlage K9 beigefügt; die ausdrücklich ersetzende neue Berechnung vom 2. Oktober wurde der Beklagten mit Anlage K13 übermittelt. Die fixe Miete von 840,00 EUR für Juni und Juli fällt im tatsächlichen und im hypothetischen Verlauf gleichermaßen an. Sie wird nicht nochmals als Schaden addiert. Gewerbliche Mieten bilden nicht schon deshalb eine zusätzliche Vermögenseinbuße, weil die Räume vorübergehend nicht wie geplant nutzbar waren. Entscheidend ist hier der konkret belegte Ausfall eines Auftrags.

Von 1.080,00 EUR Nettohonorar sind 180,00 EUR netto ersparte Fremddruckkosten für die nicht hergestellten Materialmappen abzuziehen. Die Klägerin stützt diesen Betrag auf das damalige Angebot von Otmar Selim, Druckerei Papierfächer, Malvenlaubenweg 8, 97076 Würzburg, dessen Zeugnis zu Preisangebot und Nichtbestellung angeboten wird. Die Kundin kennt nur die Kalkulationsangabe der Klägerin und wird dafür nicht als unmittelbare Zeugin des Druckangebots benannt. Weitere variable Fremdkosten wären nach dieser Kalkulation nicht angefallen. Die eigene Arbeitsleistung begründet keinen fiktiven zu zahlenden Lohnabzug; tatsächlich erzielte Ersatzverdienste wären jedoch zu berücksichtigen und werden verneint.

Damit verbleiben 900,00 EUR entgangener Deckungsbeitrag nach §§ 249, 252 BGB. Umsatzsteuer auf eine nicht erbrachte Leistung wird nicht beansprucht. Bei planmäßiger Fertigstellung wären nach Vorlage der Schlussrechnung 8.000,00 EUR zum 1. Juni abgerufen worden. Hierfür wären bei sechs Prozent jährlich für Juni und Juli 80,00 EUR reguläre Zinsen angefallen. Tatsächlich zahlte die Klägerin nur 40,00 EUR Bereitstellungszinsen. Die ersparten 40,00 EUR werden abgezogen. Der Antrag beläuft sich folglich auf 860,00 EUR.

Beweis: Bankabrechnung und ergänzende Finanzierungsbestätigung, Anlagen K7 und K12; Zeugnis der Beate Heckenast, zu laden über Genossenschaftliche Musterbank Mainlaub eG, Buchenfächerweg 10, 97070 Würzburg. Die Bankauskunft bestätigt die Konditionen, nicht den hypothetischen Fertigstellungstag. Die Rechnung lautet vollständig: rechtmäßiger Verlauf 1.080,00 EUR Einnahme abzüglich 180,00 EUR Druck und 80,00 EUR Kreditzinsen gleich 820,00 EUR; tatsächlicher Verlauf keine Einnahme und 40,00 EUR Bereitstellung gleich minus 40,00 EUR. Der Unterschied beträgt 860,00 EUR. Identische Fixkosten sind aus beiden Seiten herausgekürzt.

## 8 Rechtsschutz und Schadensminderung

Die Klägerin erhob am 17. Juni innerhalb der durch Zustellung am 5. Juni ausgelösten Monatsfrist Verpflichtungsklage. Nach Art. 12 Abs. 2 AGVwGO war in dieser Bausache grundsätzlich unmittelbar zu klagen; ein zusätzliches Widerspruchsverfahren wird nicht behauptet. Sie forderte Abhilfe und ließ nach der angekündigten, dann ausgebliebenen Prüfung mehrfach nachfassen. Es trifft daher nicht zu, sie habe die Versagung widerspruchslos hingenommen.

Ein Antrag nach § 123 VwGO wurde nicht gestellt. Für § 839 Abs. 3 BGB bleibt zu prüfen, ob ein solcher zumutbarer Antrag den konkret eingeklagten Schaden hätte verhindern können. Das Beratungspaket war bereits am 8. Juni insgesamt entfallen und am 9. Juni anderweitig vergeben. Ein erst bei Klageerhebung am 17. Juni beantragter Eilrechtsschutz hätte diesen Verlust nicht ohne Weiteres rückgängig gemacht. Auch ein sofortiger Antrag nach Zustellung am 5. Juni hätte Genehmigung, Ausbau und Rückgewinnung des festen Termins rechtzeitig ermöglichen müssen. Eine sichere Eilentscheidung innerhalb dieses engen Ablaufs wird nicht unterstellt. Für die bereits früher fehlende rechtzeitige Entscheidung sind die im Mai erreichte Entscheidungsreife und die konkreten Kenntnismöglichkeiten der Klägerin gesondert zu würdigen.

Die Klägerin darf nicht allein deshalb mit einem Mitverschulden belastet werden, weil sie vor Erteilung der Genehmigung einen Mietvertrag abschloss. Die individuellen Risiken des festen Mietbeginns und der Kundenbindung sind gleichwohl nach § 254 BGB zu betrachten. Hier verlangt sie keine grenzenlose Übernahme aller Betriebsrisiken. Sie benennt einen konkreten Auftrag, zieht ersparte Kosten ab und legt die unsichere hypothetische Entscheidung bis 20. Mai offen. Sollte das Gericht eine rechtmäßige Bekanntgabe erst zu einem späteren Zeitpunkt feststellen, wären Ausbautermin und Auftragserhalt neu zu beurteilen; der beantragte Betrag folgt nicht automatisch aus dem bloßen Fehler des Ablehnungsbescheids.

Eine realisierbare anderweitige Ersatzmöglichkeit für diesen Schaden ist nicht festgestellt. Weder Vermieter noch Kundin haben eine zugesagte Pflicht zur Beschaffung der Baugenehmigung übernommen. Ein anwaltliches Fehlverhalten wird durch den bewussten Verzicht auf einen angesichts des bereits verlorenen Pakets zweifelhaften Eilantrag nicht ohne konkrete Kausalitätsprüfung behauptet.

## 9 Zinsen und Umfang des Entwurfs

Der Zinsantrag folgt aus §§ 291, 288 Abs. 1 BGB. Er beginnt erst am Tag nach einer tatsächlichen künftigen Zustellung. Neun Prozentpunkte für Entgeltforderungen werden nicht verlangt. Die Genehmigung ist erteilt; dieser Entwurf verfolgt nur den neu berechneten, früher noch nicht verlangten konkreten Vermögensnachteil. Eine Zahlung auf die bisherige oder neue Forderung ist nicht erfolgt.

Anja Weller
Rechtsanwältin
Entwurfsfassung ohne Unterschrift und ohne Einreichung'''),
    ]))

CASES.append(dict(
    slug='akha-wuerzburg-abwasseranlage',
    attachments={},
    claim_file='16_Klageentwurf.docx',
    notes='Stadt als Klägerin; nur 4.236,40 EUR bezahlte Fremdkosten, keine unbereinigte Personalkostenpauschale. § 831 BGB in Verbindung mit Eigentumsverletzung nach § 823 Abs. 1 BGB; kein Stadt-Werkvertrag und kein automatischer Eigenschadenanspruch aus § 2 HPflG. Anlagenverzeichnis aus exhibits ergänzen.',
    exhibits=[
        exhibit(1, '02_Schadenbericht.docx', 'Städtisches Eigentum, Betrieb und Schadenaufnahme'),
        exhibit(2, '03_Leitungsauskunft.docx', 'Planunsicherheit, Suchkorridor und Empfangsbestätigung'),
        exhibit(3, '04_Baggerfuehrer.eml', 'Schilderung des eingesetzten Baggerführers'),
        exhibit(4, '05_Reparaturrechnung.docx', 'Erforderliche Kanalreparatur einschließlich Umsatzsteuer'),
        exhibit(5, '06_Ueberleitung_Rechnung.docx', 'Befristete Überleitung während der Reparatur'),
        exhibit(6, '07_Kassenvermerk.docx', 'Zahlung der Fremdkosten und steuerliche Zuordnung'),
        exhibit(7, '08_Eigene_Stunden.docx', 'Abgrenzung der nicht eingeklagten Eigenstunden'),
        exhibit(8, '09_Unternehmerantwort.eml', 'Bestätigung des Treffers und Einwendungen der Unternehmerin'),
        exhibit(9, 'schriftverkehr-und-klage/11_Polier_Suchschlitz.eml', 'Anweisung, Suchschlitztiefe und Mitarbeiterstellung'),
        exhibit(10, 'schriftverkehr-und-klage/12_Umsatzsteuer.eml', 'Ergänzende Bestätigung fehlender Vorsteuerentlastung'),
        exhibit(11, 'schriftverkehr-und-klage/13_Reparaturumfang.eml', 'Notwendigkeit, Dauer und fehlende technische Verbesserung'),
        exhibit(12, 'schriftverkehr-und-klage/14_Zahlungsaufforderung.pdf', 'Auf Fremdkosten beschränkte Zahlungsaufforderung'),
        exhibit(13, 'schriftverkehr-und-klage/15_Unternehmerbrief.pdf', 'Fortbestehender Kürzungseinwand und fehlende Zahlung'),
    ],
    documents=[
        document('11_Polier_Suchschlitz.eml', 'Schlehenfächerweg – Ablauf vor dem Rohrtreffer', '2026-10-01T16:30:00+02:00', 'email', '''Sehr geehrte Frau Sauer,

ich bestätige auf Ihre Rückfrage, dass ich am 7. September als angestellter Polier der Grab & Grund Tiefbau GmbH den Einsatz am Schlehenfächerweg geleitet habe. Nico Yilmaz war unser angestellter Baggerführer. Wir arbeiteten am Auftrag der Faserfink Netz GmbH, nicht für die Stadt. Sie hatten mir die Leitungsauskunft vom 28. August vollständig weitergeleitet. Ich hatte die eine Seite ausgedruckt. Die Hinweise zum beidseitigen Suchkorridor und zur Tiefe standen auf derselben Seite; einen eigenen Rückseitentext gab es nicht.

Ich ließ an der eingezeichneten Achse zunächst mit der Hand bis ungefähr 70 bis 80 Zentimeter suchen. Dort fanden wir nichts. Die Auskunft nannte etwa 1,20 Meter Überdeckung. Den ganzen Meter links und rechts der Achse hatten wir nicht von Hand freigelegt. Ich wies Nico dann an, mit dem Bagger ungefähr 60 Zentimeter seitlich weiterzugehen. Den Kanalverlauf hatten wir zu diesem Zeitpunkt nicht positiv festgestellt. Ich rechnete damit, dass der alte Plan jedenfalls die Straßenseite richtig zeigte und das Rohr tiefer liegen müsse. Die konkrete Lage wollte ich mit dem nächsten Aushub erkennen. Rückblickend war das keine Freilegung vor dem Maschineneinsatz.

Nach dem Knacken stoppten wir und riefen an. Eine Vermessung des Abstandes zur Planachse habe ich nicht angefertigt. Die später genannten 65 Zentimeter stammen aus der städtischen Aufnahme. Für meine Anweisung ist aber richtig, dass wir uns bewusst noch im seitlichen Warnbereich bewegten. Eine Anweisung der Stadt, dort ohne weitere Ortung zu baggern, gab es nicht. Die betriebliche Jahresunterweisung hatte stattgefunden; über deren genauen Inhalt und die von Ihnen durchgeführten Kontrollen kann ich aus dieser Erinnerung keine vollständige Aussage machen.

Mit freundlichen Grüßen
Raban Kunkel
Polier''', 'Raban Kunkel <r.kunkel@grab-grund.example>', 'Ida Sauer <ida.sauer@grab-grund.example>'),
        document('12_Umsatzsteuer.eml', 'Kanalschaden – Vorsteuer und Zahlung der beiden Rechnungen', '2026-10-02T08:20:00+02:00', 'email', '''Sehr geehrte Frau Holler,

ich ergänze den Kassenvermerk vom 28. September. Die beschädigte DN-200-Hauptleitung gehört der Stadt Würzburg. Der Abwasserbereich wird als unselbständiger Regiebetrieb geführt; es gibt für diese Leitung keine ausgegliederte Eigentümer-GmbH oder einen anderen Rechnungsträger. Die beiden Rechnungen sind an die Stadt adressiert und wurden aus ihrer Kasse bezahlt. Die Reparaturrechnung über 3.284,40 EUR wurde am 22. September, die Überleitungsrechnung über 952,00 EUR am 21. September vollständig beglichen.

Die Leitung dient ausschließlich der öffentlichen Abwasserbeseitigung in diesem Straßenabschnitt. Die betreffenden Eingangsleistungen sind in unserer steuerlichen Zuordnung keiner zum Vorsteuerabzug berechtigenden wirtschaftlichen Tätigkeit zugeordnet. Aus genau diesen Rechnungen wurden weder 524,40 EUR noch 152,00 EUR als Vorsteuer geltend gemacht. Eine Erstattung über einen anderen städtischen Betrieb, eine Förderung oder eine Zahlung des Unternehmers liegt nicht vor. Ich bestätige dies nach Rücksprache mit unserer Steuerstelle; es handelt sich nicht nur um die pauschale Annahme, jede Kommune könne niemals Vorsteuer abziehen.

Die eigenen Mitarbeiterstunden sind in den 4.236,40 EUR nicht enthalten. Die zunächst genannten 336,00 EUR beruhen auf acht angesetzten Stunden einschließlich geschätzter Abwicklung und einem internen Mischsatz. Dieser Betrag ist keine weitere bezahlte Fremdrechnung. Wenn Sie ihn nicht in die Zahlungsaufforderung aufnehmen, vermindert sich der hier bestätigte Fremdkostenbetrag nicht.

Mit freundlichen Grüßen
Mirjam Ben-Ami
Stadtkasse, Mainlaubplatz 1, 97070 Würzburg''', 'Mirjam Ben-Ami <kasse@wuerzburg-fallakten.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        document('13_Reparaturumfang.eml', 'Rechnung vom 10. September – Umfang und Überleitung', '2026-10-02T10:05:00+02:00', 'email', '''Sehr geehrte Frau Holler,

die von uns ausgeführte Arbeit betraf eine einzige frisch gebrochene Länge des Tonrohrs DN 200. Wir haben keine benachbarten Abschnitte vorsorglich erneuert. Das Ersatzstück stellt denselben Querschnitt wieder her. Weder die Kapazität des Netzes noch dessen Nutzungsstandard wurde erhöht. Die Kamera diente dazu, den unmittelbaren Anschlussbereich auf verbliebene Bruchstücke und Schäden zu prüfen. Der vorgefundene übrige Abschnitt war für den bisherigen Betrieb brauchbar; eine ohnehin für dieses Jahr bestellte Sanierung ist uns nicht bekannt.

Der Ablauf ließ sich während der Arbeiten nicht gefahrlos offen in die Grube leiten. Die von Herrn Malik ab 7. September 11:05 Uhr eingerichtete Überleitung hielt den Betrieb bis zum Abschluss am 8. September aufrecht. Wir arbeiteten am 8. September bis kurz vor 14 Uhr am Rohr und prüften anschließend den Ablauf. Die Beendigung der Überleitung um 14:15 Uhr passt zu diesem Ablauf. Die Oberflächenwiederherstellung betrifft nur die für den beschädigten Abschnitt geöffnete Fläche. Arbeitszeit, Material, Kamera und Wiederherstellung sind in unserer Rechnung einzeln ausgewiesen; eine allgemeine Modernisierung ist darin nicht enthalten.

Den Planversatz haben wir nicht vermessungstechnisch überprüft. Die städtische Angabe von etwa 65 Zentimetern ist deshalb nicht mein eigenes Aufmaß. Ich kann jedoch als unmittelbar beteiligte Unternehmerin den frischen Schadenszustand, den Reparaturumfang und die Arbeiten bestätigen. Eine technische Verlängerung der Nutzungsdauer des gesamten Kanals lässt sich aus dem Austausch dieses kurzen beschädigten Stücks nicht ableiten.

Mit freundlichen Grüßen
Irmgard Behrlein
Kanalbau Irmgard Behrlein GmbH
Rosenkieselweg 6, 97076 Würzburg''', 'Irmgard Behrlein <kanalbau@behrlein.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        document('14_Zahlungsaufforderung.docx', 'Stadt Würzburg gegen Grab & Grund Tiefbau GmbH – 4.236,40 EUR', '02.10.2026', 'letter', '''Stadt Würzburg, Rechtsstelle
Mainlaubplatz 1, 97070 Würzburg

An die Grab & Grund Tiefbau GmbH
zu Händen der Geschäftsführerin Ida Sauer
Kieswindenweg 12, 97076 Würzburg

Sehr geehrte Frau Sauer,

namens der Stadt Würzburg fordere ich Sie auf, die durch den Kanalbruch vom 7. September entstandenen Fremdkosten von 4.236,40 EUR bis zum 16. Oktober 2026 zu erstatten. Die vollständigen Rechnungen, Zahlungsbestätigungen und ergänzenden Auskünfte sind dieser Forderung zugeordnet. Die Zahlung wird an die Stadtkasse nach gesonderter Mitteilung des Kassenzeichens erbeten; dieses Schreiben enthält keine Änderung einer bestehenden Bankverbindung.

Ihre Baggerschaufel traf den öffentlichen Hauptkanal. Die Stadt ist Eigentümerin und Betreiberin. Ihr Auftraggeber Faserfink Netz GmbH hat mit der Stadt keinen Reparaturvertrag über diese Beschädigung begründet. Die Forderung beruht auf der Verletzung städtischen Eigentums durch Ihre im Arbeitseinsatz eingesetzten Beschäftigten, insbesondere § 831 BGB in Verbindung mit § 823 Abs. 1 BGB. Ein Vertrag zwischen Stadt und Ihrem Unternehmen wird nicht behauptet.

Der Plan war ausdrücklich als Näherungsangabe aus dem Jahr 1988 bezeichnet. Im Korridor von einem Meter beiderseits der Planachse sollten Sie den Verlauf vor Maschineneinsatz durch Handsuche feststellen. Ihr Polier bestätigt jetzt, dass nur bis etwa 70 bis 80 Zentimeter gesucht wurde, obwohl die Auskunft etwa 1,20 Meter Überdeckung nannte. Die seitliche Verschiebung um rund 60 Zentimeter lag weiterhin im bezeichneten Warnbereich. Der ungesicherte Planverlauf rechtfertigte deshalb keinen Übergang zum Bagger, bevor der Kanal tatsächlich gefunden war.

Wir verlangen 3.284,40 EUR für die Reparatur und 952,00 EUR für die währenddessen notwendige Überleitung. Beide Beträge sind bezahlt. Die Stadt erhält aus diesen konkret zugeordneten öffentlichen Abwasserleistungen keine Vorsteuerentlastung. Es wurde nur der beschädigte Abschnitt gleichwertig wiederhergestellt. Der anfängliche Ansatz eigener Stunden von 336,00 EUR ist nicht Bestandteil dieser Zahlungsaufforderung. Die vorliegende Mischsatzrechnung trägt ohne weitere Aufbereitung keinen unveränderten zusätzlichen Zahlungsantrag; damit ist kein Erlass eines tatsächlich nachweisbaren anderen Anspruchs erklärt.

Bitte benennen Sie konkret, welche Auswahl-, Unterweisungs- und Kontrollmaßnahmen Sie für die verantwortlichen Beschäftigten getroffen hatten, soweit Sie sich auf eine Entlastung nach § 831 BGB berufen. Die bloße Erfahrung des Poliers beantwortet diese Frage nicht vollständig. Wir sind bereit, die Lageunterlagen gemeinsam durchzugehen. Die ungefähre städtische Messung von 65 Zentimetern wird nicht als amtliche Neuvermessung ausgegeben. Sie rechtfertigt nach dem ausdrücklich mitgeteilten Suchkorridor aber keine pauschale Halbierung der Kosten.

Mit freundlichen Grüßen
Gertraud Holler
Rechtsstelle'''),
        document('15_Unternehmerbrief.docx', 'Kanalschaden – Stellungnahme zur Zahlungsaufforderung', '05.10.2026', 'letter', '''Grab & Grund Tiefbau GmbH
Kieswindenweg 12, 97076 Würzburg
Geschäftsführerin Ida Sauer

An die Stadt Würzburg, Rechtsstelle
zu Händen Gertraud Holler
Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

Ihre Zahlungsaufforderung vom 2. Oktober und die Kostenunterlagen liegen vor. Den Treffer unseres Baggers und die in Ihrem Schreiben genannten Rechnungsbeträge bestreiten wir nicht. Dass die Stadt tatsächlich bezahlt und für diese Leistungen keinen Vorsteuerabzug erhalten hat, können wir nicht aus eigenem Wissen bestätigen; die Kassenunterlagen sind dafür nachvollziehbar. Eine Zahlung ist bislang nicht erfolgt.

Wir halten an unserem Einwand fest, dass die Abweichung des alten Lageplans zu dem Unfall beigetragen hat. Auch wenn ein Suchkorridor vermerkt war, erwarten wir von einem Leitungsbetreiber möglichst zuverlässige Bestandsdaten. Uns liegt kein vermessungstechnisch gesichertes neues Aufmaß vor. Wir sehen deshalb weiterhin einen erheblichen Eigenanteil der Stadt und würden einen Abschlag von 30 Prozent verlangen. Das ist unser Verhandlungsstand und keine durch ein Gutachten festgestellte Quote.

Herr Kunkel hat seine ergänzende Darstellung abgegeben. Er war unser angestellter Polier und durfte Herrn Yilmaz Arbeitsanweisungen geben. Wir bestreiten seine Anweisung zur seitlichen Fortsetzung des maschinellen Aushubs nicht. Herr Yilmaz ist seit Februar bei uns angestellt; Herr Kunkel verfügt über langjährige Tiefbauerfahrung. Beide nahmen an betrieblichen Unterweisungen teil. Die Schulungsnachweise und unsere Kontrolldokumentation werden noch zusammengestellt. Mit dem bloßen Hinweis auf die Teilnahme kann ich derzeit keinen lückenlosen Entlastungsnachweis für den konkreten Einsatz vorlegen.

Gegen die Beschränkung auf Fremdkosten haben wir keine Einwendung. Die ursprünglich genannten 336,00 EUR eigener Stadtstunden werden von uns nicht anerkannt. Wir bitten um Nachricht, ob die Stadt unter Berücksichtigung des Planversatzes zu einer abschließenden Einigung über 70 Prozent der Fremdkosten bereit wäre. Dies soll erst nach gesonderter Annahme einen Vergleich begründen. Es ist kein vorbehaltloses Anerkenntnis eines Teilbetrags und keine Zusage einer Versicherungsleistung.

Mit freundlichen Grüßen
Ida Sauer
Geschäftsführerin'''),
        document('16_Klageentwurf.docx', 'Klageentwurf Stadt Würzburg gegen Grab & Grund Tiefbau GmbH', '05.10.2026', 'claim', '''ENTWURF – NICHT EINGEREICHT
Stand: 5. Oktober 2026

An das Amtsgericht Würzburg
Ottostraße 5, 97070 Würzburg

## 1 Parteien und Anträge

In dem Rechtsstreit der Stadt Würzburg, vertreten durch den Oberbürgermeister, Mainlaubplatz 1, 97070 Würzburg, Klägerin, Prozessbevollmächtigte: Klee & Kolben, Rechtsanwältin Clara Klee, Buchslaubenweg 14, 97074 Würzburg,

gegen die Grab & Grund Tiefbau GmbH, vertreten durch die Geschäftsführerin Ida Sauer, Kieswindenweg 12, 97076 Würzburg, Beklagte,

wird beantragt, die Beklagte zu verurteilen, an die Klägerin 4.236,40 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz ab dem auf die Zustellung der Klage folgenden Tag zu zahlen und die Kosten des Rechtsstreits zu tragen. Der Streitwert beträgt 4.236,40 EUR.

Der Entwurf ist noch nicht eingereicht. Die außergerichtliche Zahlungsfrist läuft bis 16. Oktober. Das vorliegende Schriftstück behauptet weder einen Fristablauf noch ein bereits bestehendes gerichtliches Aktenzeichen. Der Antrag umfasst ausschließlich zwei bezahlte Fremdkostenrechnungen. Die zuvor diskutierten 336,00 EUR eigener Personalstunden sind nicht Bestandteil der Klage. Auch vorgerichtliche Anwaltskosten werden nicht beantragt.

## 2 Zuständigkeit und Anspruchsinhaberin

Die Klägerin verfolgt einen privatrechtlichen Ersatzanspruch wegen der Beschädigung ihres Eigentums durch ein gewerbliches Tiefbauunternehmen. Sie ist hier Anspruchstellerin und nicht als angebliche Haftpflichtschuldnerin wegen eines aus ihrem Kanal austretenden Abwassers in Anspruch genommen. Der öffentliche Zweck der beschädigten Anlage verwandelt den Eigentumsschaden nicht in eine Amtshaftungsklage gegen die Stadt.

Das Amtsgericht ist nach § 23 Nr. 1 GVG sachlich zuständig, weil der Wert 10.000 EUR nicht übersteigt und keine wertunabhängige Landgerichtszuständigkeit eingreift. § 71 Abs. 2 Nr. 2 GVG betrifft Ansprüche aus Amtspflichtverletzung, um die es hier nicht geht. Die Beklagte hat ihren Sitz in Würzburg; dort wurde auch die unerlaubte Handlung begangen. Die örtliche Zuständigkeit folgt aus §§ 17, 32 ZPO.

Der beschädigte öffentliche DN-200-Hauptkanal am Schlehenfächerweg 9 gehört der Stadt. Ihr Abwasserbereich wird als unselbständiger Regiebetrieb geführt, der keine eigene Klägerrolle einnimmt. Die Stadt blieb Eigentümerin und Rechnungsträgerin. Eine Übertragung der Leitung auf eine Gesellschaft oder einen Zweckverband hat nicht stattgefunden.

Beweis: Schadenbericht und Kassenvermerk, Anlagen K1 und K6; ergänzende steuerliche Zuordnung, Anlage K10; Zeugnis des Lorenz Dörflein und der Mirjam Ben-Ami, jeweils zu laden über Stadt Würzburg, Mainlaubplatz 1, 97070 Würzburg. Bei substantiiertem Bestreiten kann das konkret betroffene Leitungsstück anhand des städtischen Anlagenbestands zugeordnet werden; eine nicht vorliegende notarielle Eigentumsurkunde wird nicht behauptet.

## 3 Auftrag und Leitungsauskunft

Die Beklagte führte im Auftrag der Faserfink Netz GmbH Glasfaserarbeiten aus. Zwischen ihr und der Klägerin bestand kein Werkvertrag über diese Arbeiten. Die Stadt erteilte auf Anfrage lediglich eine Leitungsauskunft. Am 28. August übermittelte Hanne Pflaum die Lageinformation für den parallel zur Straße verlaufenden Hauptkanal. Die Geschäftsführerin bestätigte den Empfang um 15:20 Uhr und leitete das vollständige Blatt an den Polier Raban Kunkel weiter.

Die Planachse lag nach der alten Eintragung etwa 2,10 Meter von der bezeichneten südlichen Mauerecke entfernt. Eine Überdeckung von ungefähr 1,20 Meter wurde angegeben. Die Auskunft machte deutlich, dass die Eintragung auf dem Stand von 1988 beruhte und die Lage nur angenähert wiedergab. Innerhalb eines Meters beiderseits der Planachse war der Verlauf vor maschinellem Aushub durch Handsuche tatsächlich festzustellen. Bei nicht geklärter Lage sollten die Arbeiten angehalten und die Stadt angesprochen werden. Es lag deshalb keine Freigabe vor, einen ungeklärten Streifen innerhalb dieses Korridors mit dem Bagger abzusuchen.

Beweis: Leitungsauskunft mit Empfangsangabe, Anlage K2; Zeugnis der Hanne Pflaum, zu laden über Stadt Würzburg, Leitungsverwaltung, Mainlaubplatz 1, 97070 Würzburg; Zeugnis des Raban Kunkel, zu laden über die Beklagte. Der Polier bestätigt inzwischen, dass die Hinweise auf derselben einzelnen Seite standen. Die frühere Erinnerung des Baggerführers an eine ungelesene Rückseite wird nicht als Beweis eines tatsächlich vorhandenen Rückseitenblatts übernommen.

## 4 Beschädigung am 7. September

Am 7. September setzte die Beklagte ihren angestellten Baggerführer Nico Yilmaz unter Leitung des ebenfalls angestellten Poliers Raban Kunkel ein. Ein handgegrabener Suchschlitz erreichte an der Planachse nur ungefähr 70 bis 80 Zentimeter Tiefe. Dort wurde kein Rohr gefunden. Der Suchkorridor von einem Meter zu beiden Seiten war nicht vollständig überprüft; insbesondere war der Kanalverlauf nicht positiv festgestellt. Der Polier wies den Fahrer gleichwohl an, etwa 60 Zentimeter seitlich mit dem Bagger fortzufahren. Die Baggerschaufel traf das Tonrohr und brach eine Länge frisch auf. Der Schaden wurde gegen 10:18 Uhr gemeldet; um 10:36 Uhr trafen städtische Beschäftigte ein.

Beweis: Nachricht des Fahrers, Anlage K3; ergänzende Darstellung des Poliers, Anlage K9; Zeugnis des Nico Yilmaz und des Raban Kunkel, jeweils zu laden über Grab & Grund Tiefbau GmbH, Kieswindenweg 12, 97076 Würzburg. Die Beklagte bestätigt den Schaufeltreffer und die Weisungsbeziehung in Anlagen K8 und K13. Zum vorgefundenen frischen Bruch werden Lorenz Dörflein und Milan Petrovic, beide zu laden über den städtischen Abwasserbereich, Mainlaubplatz 1, 97070 Würzburg, als Zeugen benannt.

Milan Petrovic ermittelte mit Maßband eine seitliche Abweichung von ungefähr 65 Zentimetern zur Planachse. Eine amtliche Neuvermessung liegt nicht vor. Die Klägerin kennzeichnet diesen Wert daher als ungefähre Aufnahme. Für den Vorwurf ist entscheidend, dass nach eigener Schilderung des Poliers bewusst ungefähr 60 Zentimeter seitlich und damit innerhalb des bezeichneten Suchbereichs maschinell weitergearbeitet wurde, ohne zuvor den Verlauf und die tatsächliche Tiefe zu klären. Der Sachverhalt beruht nicht allein auf der nachträglichen städtischen Abstandsschätzung.

Der Treffer verursachte eine konkrete Substanzverletzung. Ein vollständiger Rückstau oder die Überflutung privater Räume trat nicht ein. Solche zusätzlichen Schäden werden nicht verlangt. Der Rohrbruch erforderte dennoch eine unverzügliche Überleitung und fachgerechte Wiederherstellung des laufenden öffentlichen Abwasserbetriebs.

## 5 Haftungsgrund und Mitarbeiterverantwortung

Das beschädigte Eigentum ist durch § 823 Abs. 1 BGB geschützt. Der unmittelbare Eingriff war rechtswidrig. Die Befugnis, für einen Netzbetreiber einen Glasfasergraben herzustellen, beinhaltet keine Erlaubnis, fremde Kanäle zu beschädigen. Das Risiko war wegen der ausdrücklich unsicheren Bestandsangabe erkennbar. Aus dem erfolglosen Suchschlitz bis höchstens 80 Zentimeter durfte nicht auf einen freien maschinellen Arbeitsbereich geschlossen werden, obwohl eine ungefähre Überdeckung von 1,20 Meter genannt war.

Für die Beklagte wird der Anspruch insbesondere auf § 831 Abs. 1 BGB gestützt. Fahrer und Polier waren ihre angestellten Verrichtungsgehilfen und handelten in Ausführung des ihnen übertragenen Bauauftrags. Der Schaden entstand während genau dieser weisungsgebundenen Tätigkeit. Der Polier entschied über die Fortsetzung, der Fahrer setzte die Anweisung mit dem betrieblich eingesetzten Bagger um. Es handelt sich nicht um eine nur bei Gelegenheit der Arbeit begangene private Handlung.

Die Auswahl-, Ausstattungs-, Leitungs- und Überwachungsverantwortung ist nach den konkreten Umständen zu prüfen. Die Beklagte beruft sich auf langjährige Erfahrung des Poliers und Teilnahme beider Mitarbeiter an Unterweisungen. Diese Umstände werden nicht ignoriert. Sie ersetzen jedoch noch nicht den vollständigen Entlastungsnachweis nach § 831 Abs. 1 Satz 2 BGB. Welche Einweisung zu unsicheren Leitungsplänen erfolgte, wie die Befolgung kontrolliert wurde und ob der Schaden auch bei pflichtgemäßer Organisation eingetreten wäre, hat die Beklagte bisher nicht mit konkreten Unterlagen belegt. Ihr Schreiben erklärt selbst, dass die Kontrolldokumentation erst zusammengestellt werde.

Beweis: Unternehmensschreiben, Anlage K13, sowie Zeugnis des Raban Kunkel und des Nico Yilmaz zu erhaltenen Arbeitsanweisungen und tatsächlicher Kontrolle. Die Klägerin setzt die bloße Beschäftigung nicht mit unwiderlegbarer Haftung gleich. Gelingt der gesetzliche Entlastungsbeweis, muss dessen Bedeutung für diesen Anspruch berücksichtigt werden. Eine bisher nicht festgestellte persönliche Weisung der Geschäftsführerin zum riskanten Aushub wird nicht erfunden. Auch wird dem Polier nicht allein wegen seiner Berufsbezeichnung eine Organstellung nach § 31 BGB zugeschrieben.

Eine vertragliche Haftung der Beklagten gegenüber der Klägerin ist durch die vorhandenen Unterlagen nicht begründet. Der Auftrag stammt von Faserfink Netz GmbH; aus ihm werden ohne nähere Grundlage keine Schutzwirkung und kein unmittelbarer Zahlungsanspruch der Stadt abgeleitet. § 278 BGB ersetzt die fehlende vertragliche Sonderverbindung nicht. Ebenso schafft § 2 HPflG keinen automatischen Ersatzanspruch des Anlageninhabers für die Reparatur seiner eigenen durch einen fremden Bagger beschädigten Anlage. Die Klage stützt sich auf die konkret bezeichnete deliktische Eigentumsverletzung und die Haftung für die eingesetzten Verrichtungsgehilfen.

## 6 Erforderliche Wiederherstellung und Betrag

Zur Wiederherstellung des beschädigten Abschnitts berechnete die Kanalbau Irmgard Behrlein GmbH 1.400,00 EUR Arbeitsleistung, 460,00 EUR Material, 250,00 EUR Kameraprüfung und 650,00 EUR Oberflächenwiederherstellung, zusammen 2.760,00 EUR netto. Die Umsatzsteuer beträgt 524,40 EUR, der Bruttobetrag 3.284,40 EUR. Es wurde nur eine gebrochene Länge gleichwertig ersetzt. Querschnitt, Kapazität und Nutzungsstandard des Netzes wurden nicht erhöht. Die Kamera prüfte auf Bruchstücke und Anschlussfolgen; die Oberfläche wurde nur im geöffneten Schadensbereich wiederhergestellt.

Beweis: Reparaturrechnung, Anlage K4; ergänzende Auskunft, Anlage K11; Zeugnis der Irmgard Behrlein, zu laden über Kanalbau Irmgard Behrlein GmbH, Rosenkieselweg 6, 97076 Würzburg. Bei technisch substantiiertem Bestreiten werden ein Sachverständigengutachten zur Notwendigkeit und Angemessenheit dieser Maßnahmen und die Besichtigung des dokumentierten Reparaturabschnitts angeboten. Die bloße Rechnung soll eine konkrete technische Einwendung nicht ersetzen.

Während der Reparatur musste der anfallende Abwasserstrom übergeleitet werden. Anwar Malik stellte 280,00 EUR für Einrichtung, 420,00 EUR für den Pumpenbetrieb und 100,00 EUR für zwei Kontrollen in Rechnung, zusammen 800,00 EUR netto zuzüglich 152,00 EUR Umsatzsteuer, insgesamt 952,00 EUR. Die Überleitung begann am 7. September um 11:05 Uhr und endete am 8. September um 14:15 Uhr nach Abschluss und Prüfung der Reparatur. Sie verhinderte zusätzliche Störungen. Eine zeitlich unbegrenzte Vorhaltung oder Reservevermietung wird nicht verlangt.

Beweis: Rechnung, Anlage K5; Zeugnis des Anwar Malik, Weidenkernweg 3, 97076 Würzburg, zu Einrichtung und Laufzeit; Zeugnis der Irmgard Behrlein zum zeitlichen Reparaturbedarf. Die Fremdrechnungen addieren sich zu 4.236,40 EUR. Die Klägerin bezahlte die Überleitung am 21. September und die Reparatur am 22. September vollständig.

Beweis: Kassenvermerk und ergänzende Zahlungsbestätigung, Anlagen K6 und K10; Zeugnis der Mirjam Ben-Ami. Die Klägerin macht tatsächlich entstandene und bezahlte Wiederherstellungskosten nach § 249 Abs. 2 BGB geltend, keine unverbindlichen Kostenvoranschläge. Ein pauschaler Abzug „neu für alt“ ist bei bloßer gleichwertiger Beseitigung eines frischen Bruchs nicht ohne nachgewiesenen wirtschaftlichen Vorteil gerechtfertigt. Eine bereits fest geplante ohnehin erforderliche Erneuerung dieses Abschnitts ist nicht festgestellt.

## 7 Umsatzsteuer, Eigenstunden und Anspruchsumfang

Die Rechnungen betreffen ausschließlich die öffentliche Abwasserbeseitigung dieses Abschnitts. Die Stadt hat für diese Eingangsleistungen keine Vorsteuer geltend gemacht und erhält keine entsprechende steuerliche Entlastung. Der unselbständige Regiebetrieb bildet keine andere Anspruchsinhaberin. Die Klägerin leitet die fehlende Abzugsberechtigung nicht allein aus ihrem kommunalen Status ab; ihre Kasse bestätigt die konkrete steuerliche Zuordnung nach Rücksprache mit der Steuerstelle. Deshalb gehören die tatsächlich angefallenen 676,40 EUR Umsatzsteuer nach § 249 Abs. 2 Satz 2 BGB zur Belastung.

Beweis: Anlage K10 und Zeugnis der Mirjam Ben-Ami. Sollte die Beklagte eine bestimmte steuerliche Erstattungsmöglichkeit darlegen, wird diese gesondert geprüft. Eine Doppelkompensation über Versicherung, Förderung oder einen anderen Rechnungsträger liegt nach der Kassenbestätigung nicht vor.

Die früher genannten 336,00 EUR eigener Stunden werden nicht eingeklagt. Die vorhandene Aufstellung enthält zwar 6,5 Stunden unmittelbar anlassbezogener Tätigkeit, aber daneben geschätzte Abwicklung und einen nicht bereinigten internen Mischsatz. Allein der Umstand, dass Beschäftigte ohnehin Gehalt erhalten, würde unmittelbare erforderliche Schadensbeseitigungsarbeit nicht stets wertlos machen. Der vorliegende pauschale Ansatz bildet jedoch ohne Aufschlüsselung von Tätigkeit und Satz keinen ausreichend abgegrenzten zusätzlichen Antrag. Die Klägerin lässt diese Position daher vollständig außerhalb der vorliegenden Forderung, statt die unzutreffenden acht Stunden ungeprüft zu übernehmen.

Beweis zur Abgrenzung: Eigenstundenaufstellung, Anlage K7. Die Klage ist hinsichtlich der zwei Fremdrechnungen vollständig beziffert; sie verteilt keinen unbestimmten Teilbetrag auf beliebige Schadenspositionen. Ein materieller Erlass anderer etwaiger Ansprüche wird damit nicht erklärt. Die beantragte Summe enthält weder reine Rechtsverfolgungszeit noch pauschale Verwaltungsgemeinkosten.

## 8 Planabweichung und Mitverantwortung

Die Beklagte verlangt im Schreiben vom 5. Oktober eine Kürzung um 30 Prozent. Sie stützt dies auf ungenaue Bestandsdaten und fehlendes neues Aufmaß. Eine solche Quote ist bisher nur ein Verhandlungsvorschlag, kein Ergebnis einer technischen Untersuchung. Die Klägerin verkennt nicht, dass auch eine unzutreffende oder unzureichende Leitungsauskunft bei feststellbarer eigener Pflichtverletzung nach § 254 BGB erheblich sein könnte. Der konkrete Inhalt der Auskunft ist deshalb vollständig als Anlage beigefügt.

Hier wurde die Unsicherheit jedoch ausdrücklich mitgeteilt und durch einen Suchkorridor von einem Meter auf jeder Seite berücksichtigt. Der nach eigener Schilderung bewusst rund 60 Zentimeter versetzte Aushub blieb innerhalb dieses Korridors. Der Polier kannte sowohl die ungefähre Tiefe als auch die Pflicht zur positiven Lagefeststellung. Er rief vor dem maschinellen Fortsetzen nicht bei der Stadt an. Es ist nicht ersichtlich, dass die Stadt eine genau bekannte abweichende Lage verschwiegen oder einen ungefährlichen Korridor verbindlich zugesichert hätte. Das Alter des Plans allein führt unter diesen Umständen nicht zu der verlangten pauschalen Kürzung.

Die Beklagte kann einwenden, eine Handsuche hätte den Kanal gleichwohl nicht rechtzeitig oder gefahrlos auffinden können. Dann sind die konkreten Boden- und Raumverhältnisse sowie zumutbare weitere Ortungsmöglichkeiten zu klären. Das rechtfertigt aber nicht nachträglich den ungeklärten Baggereinsatz ohne Rückfrage. Die Klägerin bietet hierzu bei substantiiertem technischen Streit ein Tiefbausachverständigengutachten an. Der Sachverständige soll die bekannten Warnangaben, Suchschlitztiefe und Arbeitsrichtung zugrunde legen und keine zentimetergenaue Bestandsvermessung fingieren.

## 9 Zinsen, Vergleich und Schluss

Die Prozesszinsen werden aus §§ 291, 288 Abs. 1 BGB ab dem Tag nach tatsächlicher Zustellung beantragt. Es werden fünf Prozentpunkte verlangt. Der deliktische Ersatzanspruch ist keine Entgeltforderung, auch wenn die Beklagte Unternehmerin ist. Die konkrete Zahlungsaufforderung der städtischen Rechtsstelle vom 2. Oktober mit Frist bis 16. Oktober ist als Anlage K12 beigefügt. Der Entwurf setzt weder Verzug vor Ablauf des 16. Oktober noch eine bereits erfolgte Zustellung voraus.

Die Klägerin hat einen Vergleich über 70 Prozent bislang nicht angenommen. Die Unternehmerantwort enthält ausdrücklich kein vorbehaltloses Teilanerkenntnis. Eine Teilzahlung wird nicht angerechnet, weil keine erfolgt ist. Die Klägerin ist zur Erörterung konkreter technischer Einwendungen bereit, hält aber an den vollständig belegten Fremdkosten fest. Die zur Klage beigefügten Unterlagen zeigen sowohl die Eigentümer- und Betreiberrolle der Stadt als auch die tatsächlichen Grenzen von Lageaufnahme und Mitarbeiterkosten.

Clara Klee
Rechtsanwältin
Entwurfsfassung ohne Unterschrift und ohne Einreichung'''),
    ]))

# Die Anlagenverzeichnisse werden einheitlich durch den Builder aus exhibits erzeugt.
# Die Eintragung selbst erzeugt weder native Dateien noch externe Kommunikation.
