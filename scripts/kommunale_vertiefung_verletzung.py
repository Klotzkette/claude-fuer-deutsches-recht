"""Zusätzlicher Austausch und begründeter Klageentwurf zum Rangierunfall."""
def d(file, title, date, kind, body, sender='', recipient=''):
    return dict(file=file, title=title, date=date, kind=kind, body=body.strip(), sender=sender, recipient=recipient)

CASES = [dict(
    slug='akha-fiktives-verletzungsrisiko',
    title='Fiktives Verletzungsrisiko',
    summary='Zwei Insassen, getrennte medizinische Angaben und eine streitige Eigenforderung nach einem Rangierunfall.',
    is_new=False,
    core=[],
    notes='Der neue Klageentwurf betrifft allein Ottokar Wolkenbein gegen die Stadt Lindenquell und 636,20 EUR als vorläufige Wertvorstellung. Die Forderungen Pimpinellas und der Krankenkasse werden nicht eingeklagt. Die 79 EUR für die Wellnessmassage bleiben außerhalb des Zahlungsantrags. Die Klägervertretung Rhabarber ist von der bereits beauftragten Versicherervertretung Knister getrennt. Die vorhandenen Quellen werden nicht um eine gesicherte Verletzungsdiagnose oder ein ärztlich angeordnetes Taxi ergänzt. Für diesen kleinen Vorgang wird keine erfundene Einzelkorrespondenz mit einem Rückversicherer angelegt.',
    attachments={
        '01_Wolkenbein_an_Anwaeltin.eml':['08_Hausarzt.docx','12a_Apotheke.docx','12b_Massage.docx','12c_Taxi.docx'],
        '02_Bestand_an_Schadenstelle.eml':['14_Vertragsbestaetigung.eml'],
    },
    exhibits=[
        dict(label='K1',source='02_Unfallmeldung.docx',description='Unfallmeldung des Fahrers vom 14. September 2026'),
        dict(label='K2',source='03_Fuhrpark.docx',description='Halterstellung und privatrechtlicher Fahrtzweck'),
        dict(label='K3',source='04_Zeugin.eml',description='Wahrnehmungen der Zeugin Konfetti'),
        dict(label='K4',source='06_Ambulanz_Wolkenbein.docx',description='Zeitnahe klinische Beschwerdedokumentation'),
        dict(label='K5',source='07_Radiologie.docx',description='Röntgenbefund ohne frische knöcherne Verletzung'),
        dict(label='K6',source='08_Hausarzt.docx',description='Vorbefund, Verlauf und Rezeptierung'),
        dict(label='K7',source='12a_Apotheke.docx',description='Bezahlte eigene Zuzahlung von 5 EUR'),
        dict(label='K8',source='12c_Taxi.docx',description='Bezahlte Fahrten zur Verlaufskontrolle über 31,20 EUR'),
        dict(label='K9',source='13_Chat_Insassen.txt',description='Zeitnahe eigene Nachrichten über den Verlauf'),
        dict(label='K10',source='kommunikation-und-deckung/01_Wolkenbein_an_Anwaeltin.eml',description='Ergänzende Angaben zu Beschwerden, Taxi und Klageumfang'),
        dict(label='K11',source='kommunikation-und-deckung/03_Anspruch_Rhabarber.pdf',description='Konkretisierung der beschränkten Eigenforderung'),
        dict(label='K12',source='16_Zahlung_Fahrzeug.txt',description='Bereits regulierter, getrennt zu behandelnder Fahrzeugschaden'),
    ],
    documents=[
        d('01_Wolkenbein_an_Anwaeltin.eml','Mein Auftrag und die Fahrt zu Frau Dr Kicher','2026-10-05T14:00:00+02:00','email','''Sehr geehrte Frau Rhabarber,

ich bitte Sie um einen Klageentwurf gegen die Stadt. Abschicken sollen Sie noch nichts. Die 79 Euro für die Massage möchte ich zunächst herauslassen, weil Frau Wumm mir nur eine Wellnessleistung berechnet hat. Bei 600 Euro Schmerzensgeld, meinen fünf Euro aus der Apotheke und 31,20 Euro Taxi bleibe ich. Die Berichte und die drei getrennten Belege schicke ich mit. Frau Pimpinella erteile ich dadurch keinen Auftrag in ihrem Namen; die Kasse macht ihre eigenen Beträge geltend.

Am 22. September konnte ich wieder geradeaus fahren. Beim weiteren Drehen nach links zum rückwärtigen Verkehr zog es aber noch. Deshalb habe ich das Taxi zum Kontrolltermin genommen. Frau Dr. Kicher hatte mir diese Fahrt nicht vorher angeordnet; ich habe sie selbst bestellt. Meine Schwester sagte am Vorabend ab. Einen Bus hätte ich theoretisch nehmen können, die Haltestelle liegt rund 650 Meter von meiner Wohnung und die andere etwa 500 Meter von der Praxis entfernt. Ich kann nicht behaupten, dass Gehen unmöglich gewesen wäre. Mir ging es um die sichere und pünktliche Fahrt zur Kontrolle. Bitte stellen Sie das im Entwurf nicht als verordneten Krankentransport dar.

Die frühere Verspannung war rechts. Am Morgen des 14. September hatte ich nach meiner Erinnerung keine Schmerzen, nach dem Stoß zog es links. Heute bin ich wieder beschwerdefrei. Die Berichte dürfen Sie für diesen Anspruch verwenden; zusätzliche fremde Krankenunterlagen brauche ich dafür nicht. Die Autoreparatur ist bereits bezahlt.

Freundliche Grüße
Ottokar Wolkenbein
Quittenbogen 19, Lindenquell''','Ottokar Wolkenbein <ottokar@postfach.example>','Rechtsanwältin Rosa Rhabarber <rosa@rhabarber-recht.example>'),
        d('02_Bestand_an_Schadenstelle.eml','KH 26 914 – Bestätigung und Abgrenzung des Meldewegs','2026-10-05T14:15:00+02:00','email','''Hallo Gundula,

anbei nochmals meine Bestandsbestätigung vom 29. September. Der Transporter 17 gehört in unseren Kfz-Haftpflichtvertrag FB-KH-4417. Die allgemeine Haftpflichtakte der Stadt ist dafür nicht zuständig. Bitte vermeidet eine zweite Schadenanlage unter der Sammelpolice; sonst erscheint die bereits gezahlte Reparatur zweimal im Reservensystem. Die Zahlungsjournalnummer KH-26-914 bleibt führend.

Die offenen angemeldeten Beträge ergeben derzeit 1.268,40 Euro: 403,20 Euro Kassenregress, 715,20 Euro Eigenforderung Wolkenbein und 150 Euro Eigenforderung Pimpinella. Das ist nur die Summe der Eingänge, keine Haftungsbewertung. Wenn Herr Wolkenbein seine Forderung durch eine Bevollmächtigte einschränkt, legt bitte das neue Schreiben daneben und dokumentiert, welche Position tatsächlich weiterverfolgt wird. Ändert den historischen Eingangsbetrag nicht rückwirkend.

Eine Einzelschadenmeldung an einen Rückversicherer ist in diesem Vorgang nicht veranlasst. Der mir vorliegende Vertragsauszug belegt keine konkrete Rückdeckungsvereinbarung; ich kann deshalb keine Priorität oder Erstattungsquote nennen. Bitte sendet insbesondere keine ungekürzten medizinischen Unterlagen routinemäßig in eine weitere Verteilerliste. Sollte ein konkreter vertraglicher Meldeanlass auftreten, fordere ich zuerst den maßgeblichen Vertragstext und die dafür benötigten Angaben an.

Viele Grüße
Eulalia Pixel
Vertragsservice''','Eulalia Pixel <bestand@frankenbogen.example>','Gundula Funk <schaden@frankenbogen.example>'),
        d('03_Anspruch_Rhabarber.docx','Wolkenbein gegen Stadt Lindenquell – Eigenforderung','05.10.2026','letter','''Rechtsanwältin Rosa Rhabarber
Wacholdersteg 12, 97074 Würzburg

Frankenbogen Kommunalversicherung VVaG
Frau Gundula Funk, Kastanienbogen 7, 97070 Würzburg

Sehr geehrte Frau Funk,

ich vertrete ausschließlich Herrn Ottokar Wolkenbein. Unter Bezug auf Ihren Vorgang KH-26-914 konkretisiere ich seine Eigenforderung auf ein angemessenes Schmerzensgeld mit einer derzeitigen Wertvorstellung von 600 EUR sowie 36,20 EUR eigene Aufwendungen. Davon entfallen 5 EUR auf die Rezeptzuzahlung und 31,20 EUR auf die Fahrt zur hausärztlichen Kontrolle. Die Massagekosten von 79 EUR werden mit diesem Schreiben nicht weiterverfolgt. Eine Erklärung für Frau Pimpinella oder die Krankenkasse ist damit nicht verbunden.

Die vorhandenen Berichte sind differenziert zu lesen. Herr Wolkenbein gab unmittelbar nach dem Zusammenstoß linksseitige Beschwerden an; die Ambulanz dokumentierte Druckschmerz und Ziehen bei Linksdrehung. Das Röntgen zeigte keine frische knöcherne Verletzung. Daraus folgt weder ein bewiesener bestimmter Distorsionsgrad noch die Widerlegung jeder Gesundheitsbeeinträchtigung. Die frühere rechtsbetonte Verspannung ist bekannt und muss mit dem zeitlichen Verlauf abgeglichen werden. Eine zusätzliche objektive Messung oder eine unfallanalytische Begutachtung behaupten wir nicht.

Für die Taxifahrt liegt keine ärztliche Verordnung vor. Mein Mandant beschreibt noch Beschwerden beim Schulterblick; die Erforderlichkeit der Fahrt bleibt deshalb anhand der konkreten Situation und der erreichbaren Alternativen zu beurteilen. Ich bitte um Benennung Ihrer tatsächlichen Einwände zu dieser Position. Die Rechnung der allgemeinen Wellnessmassage reicht uns nach heutigem Stand nicht, um einen Heilbehandlungsbedarf substantiiert geltend zu machen.

Bitte antworten Sie bis zum 12. Oktober 2026. Die bezahlten 1.785 EUR für die Fahrzeugreparatur werden nicht erneut verlangt. Die Kassenleistungen gehören ebenfalls nicht in den Zahlungsantrag meines Mandanten. Eine Erklärung zum Deckungsverhältnis der Stadt oder zu einer Rückversicherung ist nicht Gegenstand dieses Schreibens. Bis zur Abstimmung mit meinem Mandanten wird eine Klage lediglich vorbereitet.

Mit freundlichen Grüßen
Rosa Rhabarber
Rechtsanwältin'''),
        d('04_Versicherer_an_Stadt.docx','Rangierunfall am Bürgerhaus – Stand der getrennten Forderungen','05.10.2026','letter','''Frankenbogen Kommunalversicherung VVaG
Gundula Funk, Kastanienbogen 7, 97070 Würzburg

Stadt Lindenquell, Fuhrparkleitung
Frau Hildegard Knorz, Sonnenwinkel 8, 97299 Lindenquell

Sehr geehrte Frau Knorz,

wir bearbeiten den Vorgang KH-26-914 weiter unter dem Kfz-Haftpflichtvertrag des Transporters 17. Die 1.785 EUR für die Fahrzeugreparatur sind ausgezahlt. Die übrigen Forderungen werden getrennt geprüft. Herr Wolkenbein hat nun Rechtsanwältin Rhabarber eingeschaltet; sie beziffert seine weiterverfolgten eigenen Aufwendungen auf 36,20 EUR und nennt für das Schmerzensgeld 600 EUR. Die ursprünglich zusätzlich verlangten 79 EUR für die Massage verfolgt sie in ihrem heutigen Schreiben nicht weiter. Die Kassenforderung von 403,20 EUR und die 150 EUR von Frau Pimpinella bleiben gesonderte Eingänge.

Bitte geben Sie uns bis zum 8. Oktober nur die noch fehlende tatsächliche Auskunft: Wie lange stand der Privatwagen bereits an der Lieferbucht, und gab es vor dem Zurücksetzen eine erkennbare Bewegung dieses Fahrzeugs? Falls Ihr Mitarbeiter dazu keine sichere Erinnerung besitzt, soll er gerade dies festhalten. Eine nachträglich geschätzte Anstoßgeschwindigkeit wäre ohne Grundlage nicht hilfreich. Von den Insassen erwähnte Fotos liegen der Schadenstelle bislang nicht vor; wir fordern sie unmittelbar dort an.

Die medizinischen Berichte verbleiben in unserer Leistungsprüfung. Ihrer Fuhrparkstelle werden daraus keine Diagnosen oder Angaben über andere Behandlungen übermittelt. Für Ihre Stellungnahme zu Fahrtzweck und Ablauf werden diese Daten nicht benötigt. Bitte bewahren Sie die Unfallmeldung und die damalige Dienstanweisung auf, ohne den Originaltext durch eine nachträgliche Zusammenfassung zu ersetzen.

Das Rechtsmandat von Frau Knister gilt allein für unseren Versicherer. Weder sie noch wir haben dadurch eine zusätzliche anwaltliche Vertretung der Stadt in einem späteren Prozess zugesagt. Sobald eine Klage zugestellt wird, benötigen wir die vollständige Zustellung einschließlich Datum und Umschlag, damit Zuständigkeit, Verteidigung und etwaige Fristen konkret abgestimmt werden können. Eine Klagezustellung ist uns gegenwärtig nicht bekannt. Aus diesem Zwischenstand folgt kein Anerkenntnis und keine weitere Zahlungsanweisung.

Mit freundlichen Grüßen
Gundula Funk
Kommunalschäden'''),
        d('05_Klageentwurf_Wolkenbein.docx','Klageentwurf Wolkenbein gegen Stadt Lindenquell','05.10.2026','claim','''ENTWURF VOM 5. OKTOBER 2026 – NICHT EINGEREICHT

An das Amtsgericht Würzburg

Klage des Herrn Ottokar Wolkenbein, Quittenbogen 19, 97299 Lindenquell,
– Kläger –
Prozessbevollmächtigte: Rechtsanwältin Rosa Rhabarber, Wacholdersteg 12, 97074 Würzburg,

gegen die Stadt Lindenquell, vertreten durch die Erste Bürgermeisterin oder den Ersten Bürgermeister [Name vor Einreichung ergänzen], Sonnenwinkel 8, 97299 Lindenquell,
– Beklagte –

wegen Schadensersatzes und Schmerzensgeldes nach dem Verkehrsunfall vom 14. September 2026.
Vorläufige Wertvorstellung: 636,20 EUR.

## 1. Anträge

Der Kläger beantragt,

1. die Beklagte zu verurteilen, an ihn ein angemessenes Schmerzensgeld zu zahlen, dessen Höhe in das Ermessen des Gerichts gestellt wird, wobei nach dem vorgetragenen Verlauf ein Betrag von mindestens 600 EUR für angemessen gehalten wird, nebst Zinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz seit dem Tag nach Zustellung der Klage;
2. die Beklagte zu verurteilen, an ihn 36,20 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem Basiszinssatz seit dem Tag nach Zustellung der Klage zu zahlen;
3. der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Die Klage erfasst allein die eigene Körper- und Gesundheitsbeeinträchtigung des Klägers und die zwei bezeichneten Aufwendungen. Der bezahlte Fahrzeugschaden, Leistungen der Krankenkasse, eine Eigenforderung der Beifahrerin und die privat gebuchte Massage sind nicht Gegenstand des Zahlungsbegehrens. Ein Feststellungsantrag wegen nicht konkret erkennbarer Dauerfolgen wird nicht gestellt. Über die tatsächliche Einreichung ist noch nicht entschieden.

## 2. Zuständigkeit und Anspruchsgegnerin

Der Kläger nimmt die Beklagte als Halterin des Transporters 17 aus §§ 7 Abs. 1, 11 StVG in Anspruch. Sie trägt Betriebskosten und Wartung und entscheidet über den Einsatz. Die Fahrt diente der Rückholung von Klapptischen nach einer privatrechtlichen Saalvermietung; ein Gefahrenabwehreinsatz lag nicht vor. Es wird keine Amtshaftungszuständigkeit allein aus der Eigenschaft der Beklagten als Stadt abgeleitet. Beweis: Fuhrparkauskunft vom 30. September, Anlage K2.

Das Amtsgericht ist bei der beantragten Größenordnung nach § 23 Nr. 1 GVG sachlich zuständig. Der Anspruch wird aus dem Fahrzeugbetrieb, nicht aus einem Behandlungsvertrag oder Behandlungsfehler erhoben. Die besondere Zuweisung von Heilbehandlungsstreitigkeiten an das Landgericht ist daher nicht einschlägig. Unfallort und Sitz der Beklagten liegen im Bezirk Würzburg; die örtliche Zuständigkeit folgt aus §§ 12, 17, 32 ZPO und § 20 StVG. Der Entwurf richtet sich allein gegen die Stadt. Er behauptet keine unmittelbare Verpflichtung einer Ausgleichseinrichtung oder eines Rückversicherers gegenüber dem Kläger.

## 3. Zusammenstoß und unmittelbare Beschwerden

Am 14. September um 08:17 Uhr stand der Kläger angeschnallt am Steuer seines Kleinwagens auf dem öffentlich zugänglichen Vorplatz des Bürgerhauses. Der Fahrer der Beklagten, Balthasar Brumm, setzte den Transporter rückwärts aus der Lieferbucht und stieß mit der hinteren Ecke gegen die linke Vorderseite des stehenden Wagens. Beide Fahrzeuge kamen unmittelbar zum Stillstand. Eine bestimmte Anstoßgeschwindigkeit wird mangels Messung nicht behauptet. Beweis: Fahrerbericht, Anlage K1; Zeugnis Brumm, zu laden über den Bauhof der Beklagten, Sonnenwinkel 8.

Die Zeugin Cosima Konfetti sah den bereits stehenden Privatwagen und das Rückwärtsfahren. Nach dem Kontakt legte der Kläger die Hand links an seinen Hals. Die Zeugin verstand eine Äußerung über ein Ziehen, konnte deren Zeitpunkt vor oder nach dem Bauhofanruf aber nicht sicher festlegen. Der Kläger hatte am Morgen nach eigener Erinnerung keine Beschwerden und bemerkte das linksseitige Ziehen erstmals nach dem Stoß. Beweis: Anlage K3; Zeugnis Cosima Konfetti, Holunderbogen 6, Lindenquell; persönliche Anhörung des Klägers und, soweit die gesetzlichen Voraussetzungen vorliegen, Parteivernehmung.

Die Schilderung verlangt keine technische Rekonstruktion aus einer bloßen Größenangabe zum Fahrzeugschaden. Ebenso wird aus dem selbstständigen Aussteigen nicht auf Beschwerdefreiheit geschlossen. Die Beklagte kann den Betriebszusammenhang anhand des eigenen Fahrerberichts und der Fuhrparkunterlagen nachvollziehen.

## 4. Verletzung und ursächlicher Zusammenhang

In der Notaufnahme um 09:44 Uhr berichtete der Kläger von linksseitigem Nackenziehen mit drei Punkten auf einer Zehnerskala. Bei der klinischen Untersuchung gab er Druckschmerz an der linken paravertebralen Muskulatur und Ziehen bei Linksdrehung an. Neurologische Ausfälle oder eine knöcherne Mittelliniendruckdolenz wurden nicht festgestellt. Die Ambulanz dokumentierte eine Verdachtsdiagnose, keine gutachterlich gesicherte bestimmte Strukturverletzung. Beweis: Anlage K4; Zeugnis Dr. Walburga Zündel, Klinik am Lindenbogen, Lindenquell, nach Schweigepflichtentbindung des Klägers; medizinisches Sachverständigengutachten.

Das Röntgen zeigte keine frische knöcherne Verletzung und geringe degenerative Veränderungen. Es beantwortet nicht abschließend die Frage nach einer vorübergehenden schmerzhaften muskulären Beeinträchtigung. Beweis: Radiologiebericht, Anlage K5; erforderlichenfalls Beiziehung der unter der Fallnummer A-260914-119 geführten Aufnahmen und sachverständige Bewertung.

Die hausärztliche Kartei enthält eine rechtsbetonte Verspannung nach Gartenarbeit im August. Der Kläger verschweigt diesen Vorbefund nicht. Bei der Kontrolle am 22. September schilderte er linksseitiges Ziehen nach dem Septemberereignis, damals bereits weitgehend gebessert. Die Ärztin dokumentierte links noch einen angegebenen muskulären Druckschmerz. Der zeitnahe Chat hält die Entwicklung vom ersten Ziehen über Besserung bis zur Kontrolle fest. Er gibt eigene Angaben wieder und ist kein unabhängiges medizinisches Gutachten. Beweis: Anlagen K6 und K9; Zeugnis Dr. Adelgund Kicher, Schwalbenwinkel 3, Lindenquell, nach entsprechender Entbindung; medizinisches Sachverständigengutachten.

Der Kläger behauptet eine unfallbedingte vorübergehende schmerzhafte Beeinträchtigung, nicht lediglich die Gefahr einer möglicherweise späteren Verletzung. Die haftungsbegründende Verletzung und ihre Ursächlichkeit sind nach § 286 ZPO zu beweisen. § 287 ZPO wird nicht benutzt, um eine fehlende Primärverletzung zu ersetzen. BGH, Urteil vom 17. September 2013 – VI ZR 95/13, Rn. 8 und 10–14, verlangt eine vollständige Würdigung der Beschwerden und ihrer Unfallbedingtheit: Der bloße Verdacht genügt nicht; sichtbare äußere Unfallspuren sind aber keine zwingende Voraussetzung. Der dortige Kassenregress wird nicht als Entscheidung über die hier beanspruchte konkrete Geldhöhe dargestellt.

## 5. Schmerzensgeld und eigene Aufwendungen

Der Kläger hält für das zeitnah dokumentierte Ziehen, die ärztliche Abklärung und die mehrtägige Beeinträchtigung ein einheitliches Schmerzensgeld von mindestens 600 EUR für angemessen. Er war nicht stationär aufgenommen, ist Rentner und macht weder Arbeitsunfähigkeit noch Verdienstausfall geltend. Eine bleibende Einschränkung wird nicht behauptet. Die Behandlung selbst ersetzt nicht den erforderlichen Nachweis einer Verletzung; entscheidend bleibt der geschilderte und unter Beweis gestellte Verlauf. Die Größenordnung ist keine aus einer anderen Entscheidung übernommene feste Schmerzensgeldtaxe.

Die 5 EUR eigene Zuzahlung wurden für das am Unfalltag ärztlich rezeptierte Schmerzmittel entrichtet. Die Rezeptierung und die nach Patientenauskunft dreimalige Einnahme sind im Hausarztbericht festgehalten. Beweis: Anlagen K6 und K7. Der Kläger verlangt nur seinen eigenen Zahlbetrag, nicht den vom Kostenträger getragenen Arzneimittelpreis. Erhält die Krankenkasse weitere Ansprüche aus § 116 SGB X, entstehen dadurch keine zusätzlichen Eigenkosten des Klägers.

Die 31,20 EUR betreffen zwei tatsächlich bezahlte Taxifahrten zur Verlaufskontrolle und zurück. Die Strecke, Uhrzeiten und Zahlung sind quittiert. Beweis: Anlage K8; Zeugnis Jette Wirbel, Wiesenbogen 5, Lindenquell. Der Kläger nahm das Taxi wegen des noch unangenehmen Schulterblicks. Der Wagen war wieder verfügbar, die Schwester stand nicht zur Verfügung. Der Weg mit öffentlichen Verkehrsmitteln hätte zusätzliche Fußwege verlangt; Gehunfähigkeit wird nicht behauptet. Beweis: ergänzende eigene Nachricht, Anlage K10; persönliche Anhörung; zur medizinischen Bedeutung des fortbestehenden Ziehens sachverständige Begutachtung.

Die Taxifahrt war nicht ärztlich angeordnet. Der Kläger meint gleichwohl, dass eine kurze direkte Fahrt zur gebotenen Verlaufskontrolle in seiner damaligen Situation erforderlich und angemessen war. Sollte das Gericht eine günstigere zumutbare Alternative als ausreichend ansehen, ist diese Position gesondert zu würdigen. Die Ungewissheit über 31,20 EUR macht weder die Medikamentenzuzahlung noch den behaupteten Verletzungsverlauf gegenstandslos. Allgemeine Fahrtpauschalen oder weitere unbelegte Fahrten werden nicht verlangt.

## 6. Abgrenzung und Einwendungen

Die Reparatur von 1.785 EUR ist bereits bezahlt. Die Zahlung ist ausdrücklich auf den Sachschaden begrenzt und wird deshalb weder nochmals verlangt noch als Anerkenntnis der Körperverletzung behandelt. Beweis: Anlage K12. Die Beschwerde- und Untersuchungslage der Beifahrerin ist ein anderer Lebenssachverhalt. Aus ihrem unauffälligen Befund wird weder auf die Gesundheit des Klägers noch auf einen Anspruch in seinem Namen geschlossen.

Soweit bei der Halterabwägung § 17 StVG einschlägig ist, sind nur feststehende unfallursächliche Umstände zu gewichten. Nach dem Fahrerbericht und der Zeugin stand der Wagen des Klägers bereits vor dem Rückwärtsfahren. Ein eigener Fahrfehler ist nicht ersichtlich. Der Kläger beansprucht volle Haftung der Beklagten wegen des nachgewiesenen Rückwärtsanstoßes; er setzt aber weder eine schematische Betriebsgefahrquote noch ohne Tatsachenvortrag ein unabwendbares Ereignis fest.

Die Anspruchskonkretisierung an die Schadenstelle ist als Anlage K11 beigefügt. Der dortige Antworttermin ist bei Erstellung des Entwurfs nicht abgelaufen. Vorgerichtlicher Verzug und bereits angefallene Prozesskosten werden nicht behauptet. Die Zinsen werden nach §§ 291, 288 Abs. 1 Satz 2 BGB erst ab dem Tag nach der künftigen Klagezustellung beantragt.

Rosa Rhabarber
Rechtsanwältin – nicht eingereichter Entwurf'''),
    ]
)]
