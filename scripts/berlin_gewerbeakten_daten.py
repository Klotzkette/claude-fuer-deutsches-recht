"""Drei ausgearbeitete Berliner Betriebsakten; nur Quelldaten für den zentralen Builder."""

def D(file, title, date, sender, recipient, body, **extra):
    return dict(file=file, title=title, date=date, sender=sender, recipient=recipient, body=body.strip(), **extra)

def E(file, title, date, sender, recipient, body):
    return dict(file=file, title=title, date=date, **{'from': sender, 'to': recipient}, body=body.strip())

def T(file, title, date, body):
    return dict(file=file, title=title, date=date, body=body.strip())

def X(file, title, sheets):
    return dict(file=file, title=title, sheets=sheets)

PLUGIN = 'berliner-gewerbeaufsicht-betrieb'
CASES = []

CASES.append(dict(slug='berlin-gewerbe-restaurant-kichererbse', title='Die Kichererbse übernimmt das Café', plugin=PLUGIN, date='02.10.2026', client='Mina Yilmaz und Ottokar Kühn für die Kichererbse Berlin GmbH', summary='Zwei Freunde übernehmen ein kleines Café in Berlin und wollen vegetarische Abendgerichte anbieten. Alte Erlaubnis, neue Räume, ein Kühlschrank und sechs Gehwegtische passen noch nicht ganz zusammen.', assignment='Die Betreiber bitten um ein konkretes Schreiben an das Ordnungsamt und einen verständlichen Ablauf bis zur Eröffnung. Der angekündigte Weinabend soll nur stattfinden, wenn die Voraussetzungen vorliegen.', attachments={'12_Nachweise_an_Amt.eml':['05_Betriebskonzept.docx','06_Startbudget.xlsx'],'16_Reparatur_belegt.eml':['14_Servicebericht_Kuehlung.docx']}, documents=[
D('01_Auftrag_Kichererbse.docx','Unsere Eröffnung am 16. Oktober','02.10.2026','Mina Yilmaz und Ottokar Kühn\nKichererbse Berlin GmbH, Pflügerstraße 81, 12047 Berlin','Rechtsanwältin Jule Morgen\nKanzlei am Kanal, Berlin', '''Sehr geehrte Frau Morgen,

wir übernehmen das bisherige Café von Herrn Fritz Fröhlich und möchten am 16. Oktober als Kichererbse eröffnen. Mina kümmert sich um Küche und Einkauf, Ottokar um Service und die Unterlagen. Wir sind beide Geschäftsführer der Kichererbse Berlin GmbH und vertreten die Gesellschaft einzeln. Unsere Registerunterlagen haben wir dem Ordnungsamt bereits geschickt.

Herr Fröhlich meint, mit seiner alten Konzession und unserer Gewerbeanmeldung könnten wir sofort loslegen. Die Sachbearbeiterin hat dagegen noch Unterlagen für eine vorläufige Erlaubnis verlangt. Wir haben den Weinabend schon in unserem Freundeskreis angekündigt, jedoch noch keine Eintrittskarten verkauft. Auf der Internetseite steht bisher nur „Eröffnung im Oktober“.

Zusätzlich möchten wir sechs kleine Tische vor das Haus stellen. Herr Fröhlich hatte zwei; seine Erlaubnis dafür haben wir nicht gefunden. Der Keller soll nur Vorratslager bleiben. Die Kühlvitrine war bei einer Besichtigung zu warm. Der Techniker hat sie inzwischen repariert, und die Lebensmittel aus der betroffenen Lieferung wurden zurückgegeben. Die Nachweise liegen bei.

Bitte erstellen Sie die jetzt nötige Antwort an das Ordnungsamt und sagen Sie uns verständlich, welche Schritte vor welchem Teil der Eröffnung fehlen. Wir können zunächst ohne Wein und ohne Gehwegtische öffnen, wenn das rechtlich und praktisch trägt. Bitte reichen Sie noch nichts ein; wir möchten den Entwurf kurz gemeinsam lesen. Wir möchten mit dem Amt und den Nachbarn freundlich zusammenarbeiten.

Mit freundlichen Grüßen
Mina Yilmaz und Ottokar Kühn'''),
D('02_Uebernahmevereinbarung.docx','Vereinbarung über Inventar und Betriebsübergang','10.09.2026','Fritz Fröhlich, bisheriger Betreiber des Café Feierabend','Kichererbse Berlin GmbH, vertreten durch Mina Yilmaz', '''1. Gegenstand der Übergabe

Fritz Fröhlich übergibt der Kichererbse Berlin GmbH zum 01.10.2026 das im Übergabeprotokoll bezeichnete Inventar des Café Feierabend in der Pflügerstraße 81. Der Kaufpreis beträgt 18.000 EUR und ist am Übergabetag fällig. Er umfasst Theke, Kaffeemaschine, Kühlvitrine, Tische und Stühle. Nicht umfasst sind private Gegenstände des Verkäufers und dessen laufende Lieferverträge.

2. Betrieb und Räume

Der Verkäufer hat den Cafébetrieb bis zum 20.09.2026 geführt. Danach bleibt das Lokal wegen Reinigung und Malerarbeiten geschlossen. Der Mietvertrag der Käuferin beginnt am 01.10.2026. Der Gastraum und die Küche werden in ihrer Lage nicht verändert. Der Keller bleibt Lager. Der Verkäufer übergibt die bei ihm vorhandenen Behördenunterlagen in einem Ordner.

3. Genehmigungen und Unterlagen

Der Verkäufer erklärt, dass für seinen bisherigen Betrieb eine Gaststättenerlaubnis vorliegt. Die Käuferin wird die für ihren eigenen Betrieb erforderlichen Anzeigen und Anträge selbst veranlassen. Eine Zusage, dass eine Behörde der Käuferin eine bestimmte Erlaubnis erteilt oder die geplante Erweiterung des Außenbereichs zulässt, wird nicht abgegeben. Der Verkäufer unterstützt sie durch Auskunft über die bisherige Nutzung.

4. Kühlvitrine und Übergabe

Die Vitrine zeigt zeitweise schwankende Temperaturen. Die Käuferin veranlasst vor Nutzung eine technische Prüfung; der Verkäufer übernimmt nach Vorlage der Rechnung bis zu 450 EUR der Reparaturkosten. Die Zahlung des Inventarkaufpreises gilt nicht als technische Abnahme der Vitrine. Beide Seiten erhalten eine unterschriebene Ausfertigung dieser Vereinbarung.

Fritz Fröhlich / Mina Yilmaz'''),
E('03_Froehlich_zur_Konzession.eml','Der rote Ordner und die Tische','2026-09-11T16:42:00+02:00','Fritz Fröhlich <fritz@cafe-feierabend.example>','Ottokar Kühn <ottokar@kichererbse.example>', '''Lieber Ottokar,

im roten Ordner ist meine Konzession von 2017. Ich habe damit Kaffee, Kuchen, Bier und Wein angeboten. Ihr macht doch fast dasselbe, deshalb dachte ich, das liefe einfach weiter. Die zwei Tische draußen hatte ich im Sommer meistens stehen. Den Straßenbescheid finde ich gerade nicht. Bitte verlasst euch bei sechs Tischen lieber nicht auf meine Erinnerung.

Der letzte reguläre Tag ist der 20. September. Danach räume ich nur noch auf.

Viele Grüße
Fritz'''),
D('04_Alte_Gaststaettenerlaubnis.docx','Erlaubnis für das Café Feierabend','12.04.2017','Bezirksamt Neukölln von Berlin\nOrdnungsamt, Gewerbeangelegenheiten','Fritz Fröhlich\nCafé Feierabend, Pflügerstraße 81, 12047 Berlin', '''Sehr geehrter Herr Fröhlich,

Ihnen wird die Erlaubnis erteilt, am Standort Pflügerstraße 81 in Berlin ein Café mit Ausschank alkoholischer und alkoholfreier Getränke sowie Abgabe zubereiteter Speisen zum Verzehr an Ort und Stelle zu betreiben. Die Erlaubnis bezieht sich auf die im beigefügten und zum Bestandteil dieser Entscheidung erklärten Grundriss bezeichneten Räume im Erdgeschoss. Im Gastraum sind 24 Sitzplätze dargestellt. Der Keller ist als Lagerraum bezeichnet und darf nicht als Gastraum verwendet werden.

Der Betrieb ist so zu führen, dass vermeidbare Belästigungen der Nachbarschaft unterbleiben. Türen und Fenster sind bei verstärkter Musikwiedergabe geschlossen zu halten, soweit hierdurch die erforderliche Lüftung und die sichere Benutzung der Rettungswege nicht beeinträchtigt werden. Eine Nutzung öffentlicher Straßenflächen ist nicht Gegenstand dieser Erlaubnis. Die dafür erforderliche gesonderte Entscheidung ist bei der zuständigen Stelle einzuholen.

Änderungen der Betriebsart, der zugelassenen Räume oder der verantwortlichen Betriebsführung sind vor ihrer Umsetzung mit der zuständigen Stelle abzuklären. Andere öffentlich-rechtliche Anforderungen, insbesondere des Bau-, Lebensmittel- und Arbeitsschutzrechts, bleiben unberührt. Der Bescheid wird mit dem Raumplan in Ihrer Betriebsakte geführt. Das Gebührenblatt ist gesondert beigefügt.

Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Widerspruch beim Bezirksamt Neukölln von Berlin eingelegt werden.

Im Auftrag
Hanna Reuter''', reference='Gew-2017-214-F'),
D('05_Betriebskonzept.docx','Betriebskonzept Kichererbse, Fassung 24. September','24.09.2026','Mina Yilmaz\nKichererbse Berlin GmbH','Für die Antragsunterlagen', '''1. Angebot und Zeiten

Die Kichererbse soll ein vegetarisches Café mit kleiner Abendkarte werden. Vorgesehen sind Frühstück, Kuchen, zwei warme Tagesgerichte und Salate. Der Innenbetrieb ist zunächst Dienstag bis Samstag von 9 bis 22 Uhr sowie Sonntag von 10 bis 18 Uhr geplant. Montag bleibt geschlossen. Wein und Bier sollen nur nach Vorliegen der notwendigen Erlaubnis ausgeschenkt werden. Eine Tanzveranstaltung oder regelmäßige verstärkte Livemusik ist nicht vorgesehen.

2. Räume und Plätze

Der Gastraum soll 24 Sitzplätze behalten. Die Internetvorlage unseres Reservierungsprogramms nennt noch 30 Plätze; diese Zahl wurde aus einer Standardmaske übernommen. Im Keller werden haltbare Vorräte und Reinigungsmittel in getrennten Bereichen gelagert. Gäste werden dort nicht bewirtet. Die Küche bleibt an derselben Stelle, die vorhandene Abluftanlage soll vor Eröffnung gewartet werden.

3. Außenbereich

Wir wünschen sechs Zweiertische auf dem Gehweg unmittelbar vor dem Lokal. Eine maßstäbliche Skizze mit den tatsächlichen Abständen fehlt noch. Vor einer Entscheidung über die Fläche werden wir dort keine Tische aufstellen. Zwei vorhandene Tische aus dem Inventar bleiben solange im Lager. Die Hausverwaltung hat dem Vorhaben grundsätzlich zugestimmt, aber keine straßenrechtliche Aussage gemacht.

4. Hygiene und Personal

Mina führt die Küchenorganisation. Die Warenannahme dokumentiert sie mit Datum und Temperaturprüfung nach Produktanforderung. Die defekte Kühlvitrine wird bis zur Reparatur nicht genutzt. Drei Beschäftigte beginnen im Oktober. Ihre Nachweise werden vor dem ersten tatsächlichen Kücheneinsatz geprüft. Die Schulung zur neuen Speisekarte und zu den Allergenen ist für den 12. Oktober vorgesehen.'''),
X('06_Startbudget.xlsx','Startkosten und Platzplanung',[dict(name='Startkosten',headers=['Position','Angebot EUR','Beauftragt EUR','Bezahlt EUR','Offen EUR'],widths=[35,18,18,18,18],formats={'B':'#,##0.00','C':'#,##0.00','D':'#,##0.00','E':'#,##0.00'},rows=[['Inventar',18000,18000,18000,'=C2-D2'],['Kuehlreparatur',420,420,420,'=C3-D3'],['Abluftwartung',680,680,0,'=C4-D4'],['Gehwegmoebel',950,0,0,'=C5-D5'],['Summe','=SUM(B2:B5)','=SUM(C2:C5)','=SUM(D2:D5)','=SUM(E2:E5)']],expected={'B6':20050,'C6':19100,'D6':18420,'E6':680},perturbations=[{'input':'D4','value':680,'output':'E6','expected':0}]),dict(name='Plaetze',headers=['Bereich','Plan','Alter Bescheid','Differenz','Notiz'],widths=[23,12,20,14,54],formats={'B':'0','C':'0','D':'0'},rows=[['Gastraum',24,24,'=B2-C2','Betriebskonzept vom 24. September.'],['Gehweg',12,0,'=B3-C3','Antragsskizze noch offen; alte Unterlage fehlt.'],['Keller',0,0,'=B4-C4','Lager, keine Gaeste.']],expected={'D2':0,'D3':12},perturbations=[{'input':'B3','value':4,'output':'D3','expected':4}])]),
T('07_Teamchat_Eroeffnung.txt','Chat zwischen Mina, Ottokar und Fritzi','25.09.2026', '''25.09.2026 18:04 Ottokar: Im Reservierungstool stehen noch 30. Ich ändere das heute auf 24.
25.09.2026 18:06 Mina: Bitte auch keine Tische draußen versprechen. Wir haben die Skizze noch nicht.
25.09.2026 18:10 Fritzi: Ich kann beim Weinabend bedienen. Meine Belehrung ist aus 2022, bei meiner bisherigen Stelle arbeite ich seitdem durchgehend in der Küche.
25.09.2026 18:12 Mina: Bring bitte die Unterlagen mit. Wir schauen auch nach der letzten Folgebelehrung.
25.09.2026 18:20 Ottokar: Ohne Wein wäre die Eröffnung auch schön. Dann machen wir Birnenschorle und Suppe. Nur bitte rechtzeitig entscheiden.'''),
E('08_Eingang_Gewerbeanzeige.eml','Eingang Ihrer Gewerbeanzeige','2026-09-25T09:11:00+02:00','Gewerbeservice Neukölln <gewerbe@amt-neukoelln.example>','Kichererbse Berlin GmbH <buero@kichererbse.example>', '''Sehr geehrte Damen und Herren,

Ihre Anzeige für die Kichererbse Berlin GmbH mit beabsichtigtem Beginn 01.10.2026 ist eingegangen. Als Tätigkeit ist „Café und vegetarische Speisewirtschaft, Ausschank von Getränken“ angegeben. Die Empfangsbescheinigung wird gesondert bereitgestellt. Diese Nachricht enthält keine Entscheidung über Ihren Antrag auf Gaststättenerlaubnis oder die Nutzung des Gehwegs.

Mit freundlichen Grüßen
Lene Sommer'''),
D('09_Besichtigungsnotiz_Lebensmittel.docx','Besichtigung vor Betreiberwechsel','28.09.2026','Bezirksamt Neukölln von Berlin\nVeterinär- und Lebensmittelaufsicht','Kichererbse Berlin GmbH\nMina Yilmaz', '''Sehr geehrte Frau Yilmaz,

bei der gemeinsamen Besichtigung am 28.09.2026 um 10.15 Uhr wurden die Küche und die Kühlvitrine im Gastraum in Augenschein genommen. Sie erklärten, dass noch kein öffentlicher Betrieb stattfindet und die vorhandenen Lebensmittel zu einem internen Probelauf gehören. In der Vitrine befanden sich sechs verschlossene Becher Joghurtdip und vier Salatschalen aus der Lieferung desselben Morgens. Die Anzeige des Geräts lag bei 10,8 Grad Celsius. Eine unabhängige Produktmessung wurde bei diesem Termin nicht vorgenommen.

Sie haben zugesagt, die Ware bis zur Klärung nicht abzugeben und mit dem Lieferanten die Rücknahme abzustimmen. Das Gerät soll vor weiterer Nutzung technisch überprüft werden. Bitte übermitteln Sie bis zum 07.10.2026 den Servicebericht und eine nachvollziehbare Dokumentation zur Behandlung der betroffenen Ware. Bei erneuter Nutzung ist die Funktionskontrolle in die betriebliche Eigenkontrolle aufzunehmen.

Die Reinigung unter dem Arbeitstisch und die fehlende Kennzeichnung zweier Reinigungsmittelbehälter wurden ebenfalls angesprochen. Sie erklärten, beide Punkte vor Übergabe zu erledigen. Die vollständige betriebliche Hygieneorganisation war nicht Gegenstand einer abschließenden Prüfung. Bitte halten Sie die Personalbelehrungen und die für Ihre tatsächlichen Abläufe vorgesehenen Eigenkontrollunterlagen bereit.

Dieses Schreiben dokumentiert die besprochenen Punkte und die erbetenen Nachweise. Eine Entscheidung über gaststättenrechtliche oder baurechtliche Erlaubnisse ist damit nicht verbunden. Für Rückfragen steht die unterzeichnende Sachbearbeitung zur Verfügung.

Im Auftrag
Elvira Brandt''', reference='LM-26-1189'),
E('10_Lieferant_Ruecknahme.eml','Rücknahme Dip und Salat vom 28. September','2026-09-28T14:20:00+02:00','Frischefreunde Berlin <service@frischefreunde.example>','Mina Yilmaz <mina@kichererbse.example>', '''Liebe Mina,

wir haben heute um 12.40 Uhr sechs ungeöffnete Dipbecher und vier Salatschalen aus Lieferschein FF-260928-14 zurückgenommen. Die Ware wird nicht erneut verkauft. Eine Gutschrift über 54,60 EUR folgt. Unsere Fahrerin hat notiert, dass ihr die Produkte aus der betroffenen Vitrine entfernt hattet. Über die Temperatur während der Zeit bei euch können wir keine abschließende Aussage treffen.

Viele Grüße
Rosa Malik'''),
D('11_Ordnungsamt_Nachforderung.docx','Unterlagen zur Übernahme des Gaststättenbetriebs','29.09.2026','Bezirksamt Neukölln von Berlin\nOrdnungsamt, Gewerbeangelegenheiten','Kichererbse Berlin GmbH\nPflügerstraße 81, 12047 Berlin', '''Sehr geehrte Frau Yilmaz, sehr geehrter Herr Kühn,

zu Ihrem Antrag auf Erteilung einer Gaststättenerlaubnis und Ihrer Bitte um eine vorläufige Erlaubnis benötigen wir eine eindeutige Darstellung des beabsichtigten Betriebs. Bitte reichen Sie bis zum 08.10.2026 das aktuelle Betriebskonzept und einen dem tatsächlichen Zustand entsprechenden Grundriss ein. Teilen Sie insbesondere mit, ob gegenüber dem bisherigen Café eine Änderung der Betriebsart oder zusätzliche Gasträume vorgesehen sind.

Die vorhandene Erlaubnis vom 12.04.2017 ist an Herrn Fröhlich gerichtet. Eine Entscheidung über Ihre eigenen Anträge ist bisher nicht ergangen. Die Gewerbeanzeige wird in einem gesonderten Vorgang bearbeitet. Bitte erläutern Sie den geplanten Alkoholausschank und den gewünschten Betriebsbeginn. Ihre Nachricht nennt den 01.10.2026, die beigefügte Veranstaltungsankündigung den 16.10.2026. Für die tatsächliche Übernahme bitten wir um Angabe des letzten Betriebstags des bisherigen Inhabers.

Die Nutzung des Gehwegs ist nicht Gegenstand dieses Antrags. Für die geplanten Außenplätze wenden Sie sich mit einem maßstäblichen Lageplan an die zuständige Stelle für Sondernutzung. Bitte verwenden Sie bis zu einer Klärung keine Formulierung, nach der die alten Außenplätze bereits auf Ihre Gesellschaft übergegangen seien.

Diese Nachforderung enthält keine abschließende Entscheidung über die Erlaubnisfähigkeit. Sollten Sie einen zunächst begrenzten Betriebsumfang beabsichtigen, beschreiben Sie diesen bitte konkret. Eine Eröffnung mit erlaubnispflichtigem Ausschank darf nicht allein auf die vorliegende Eingangsbestätigung gestützt werden.

Im Auftrag
Lene Sommer''', reference='Gast-26-774'),
E('12_Nachweise_an_Amt.eml','Gast-26-774: Konzept und Kostenübersicht','2026-09-30T10:06:00+02:00','Ottokar Kühn <ottokar@kichererbse.example>','Lene Sommer <gewerbe@amt-neukoelln.example>', '''Sehr geehrte Frau Sommer,

anbei übersende ich unser Betriebskonzept vom 24. September und die interne Startkostenübersicht. Den aktuellen Grundriss lässt Mina gerade zeichnen. Wir meinen mit dem 1. Oktober die vertragliche Übernahme; für Gäste soll erst am 16. Oktober geöffnet werden. Die sechs Gehwegtische werden bis zur Klärung nicht aufgestellt.

Wir lassen uns bei der Antwort auf Ihre weiteren Fragen unterstützen. Eine Erlaubnisentscheidung haben wir noch nicht erhalten.

Mit freundlichen Grüßen
Ottokar Kühn'''),
T('13_Temperaturnotizen.txt','Temperaturen und Arbeiten an der Vitrine','30.09.2026', '''28.09.2026 09:10 Mina: Anzeige 9,6 Grad. Ware eben geliefert, nicht ausgegeben.
28.09.2026 10:15 Besichtigung: Anzeige 10,8 Grad.
28.09.2026 10:30 Ware gesperrt, Lieferant angerufen.
28.09.2026 12:40 Rücknahme durch Lieferantin.
29.09.2026 Vitrine leer und außer Nutzung.
30.09.2026 12:00 Techniker fertig. Anzeige nach Probelauf 4,2 Grad, keine Lebensmittel im Gerät.
30.09.2026 16:00 Anzeige 4,1 Grad. Neues Einstechthermometer bestellt. Die Werte hier sind Geräteanzeigen, keine Produktkerntemperaturen.'''),
D('14_Servicebericht_Kuehlung.docx','Servicebericht Kühlvitrine KF-24','30.09.2026','Kühle Kiste Technik GmbH\nServicetechniker Balduin Wolf','Kichererbse Berlin GmbH', '''Sehr geehrte Frau Yilmaz,

am 30.09.2026 wurde die Kühlvitrine KF-24, interne Gerätenummer KIC-02, am Standort Pflügerstraße 81 geprüft. Der Einsatz begann um 9.20 Uhr und endete um 12.00 Uhr. Bei der Prüfung war das Gerät leer. Festgestellt wurden eine verschmutzte Kondensatoreinheit und eine nicht vollständig schließende Türdichtung. Die Kondensatoreinheit wurde gereinigt und die Türdichtung ersetzt. Weitere Reparaturen wurden bei diesem Einsatz nicht beauftragt.

Nach Wiederinbetriebnahme und einem Probelauf zeigte das Gerät eine Temperatur von 4,2 Grad Celsius. Der Wert wurde an der internen Anzeige abgelesen und mit einem separaten Luftfühler im Innenraum plausibilisiert. Eine Untersuchung von Lebensmitteln oder eine rückwirkende Bewertung der Lagerbedingungen fand nicht statt. Über die Eignung zuvor gelagerter Produkte kann dieser Bericht daher keine Aussage treffen.

Wir empfehlen, die Reinigung des Kondensators in den Wartungsplan aufzunehmen und den Schließzustand der Tür regelmäßig zu kontrollieren. Die Betreiberin wurde darauf hingewiesen, dass dichte Beladung die Luftzirkulation beeinträchtigen kann. Für die produktspezifischen Lagertemperaturen ist die betriebliche Organisation verantwortlich.

Die Reparaturkosten betragen einschließlich Anfahrt und Material 420 EUR brutto. Die Zahlung wurde bei Abschluss des Einsatzes per Karte vorgenommen. Der Bericht bezieht sich ausschließlich auf die genannte Vitrine. Die übrigen Kühlgeräte, die Abluftanlage und die vollständige Küche waren nicht Gegenstand des Auftrags.

Mit freundlichen Grüßen
Balduin Wolf, Servicetechniker'''),
E('15_Hausverwaltung_Gehweg.eml','Ihre geplanten Tische vor dem Haus','2026-09-30T14:17:00+02:00','Hausverwaltung Hofbogen <verwaltung@hofbogen.example>','Mina Yilmaz <mina@kichererbse.example>', '''Sehr geehrte Frau Yilmaz,

wir haben grundsätzlich keine Einwände gegen kleine Tische vor Ihrer Einheit. Der Gehweg gehört jedoch nicht zu Ihrer Mietfläche. Bitte holen Sie die behördliche Entscheidung ein und halten Sie den Hauseingang frei. Die Anwohnerin Frau Knöpfle hat wegen ihres Rollators um ausreichend Platz gebeten. Wir vermitteln gern ein kurzes Kennenlernen.

Freundliche Grüße
Alma Vogt'''),
E('16_Reparatur_belegt.eml','LM-26-1189: Servicebericht','2026-10-01T08:35:00+02:00','Mina Yilmaz <mina@kichererbse.example>','Elvira Brandt <lebensmittel@amt-neukoelln.example>', '''Sehr geehrte Frau Brandt,

anbei erhalten Sie den Servicebericht. Die betroffenen Produkte wurden zurückgegeben und nicht an Gäste abgegeben. Die Rücknahmebestätigung liegt vor; ich kann sie bei Bedarf weiterleiten. Unter dem Arbeitstisch wurde gereinigt, und die Reinigungsmittelbehälter sind jetzt bezeichnet. Die Vitrine bleibt bis zu unserer ersten Warenanlieferung leer.

Mit freundlichen Grüßen
Mina Yilmaz'''),
D('17_Personalnotiz.docx','Personal und Nachweise für den ersten Monat','01.10.2026','Mina Yilmaz\nInterne Betriebsorganisation','Ottokar Kühn', '''1. Küchenorganisation

Ich leite die Küche und bin während der ersten zwei Betriebswochen bei jeder Speisenausgabe anwesend. Meine Bescheinigung nach der Erstbelehrung stammt aus März 2019. Ich habe damals unmittelbar danach in der Küche des Restaurants meiner Tante begonnen und bis August 2026 dort gearbeitet. Die letzte dokumentierte Arbeitgeberbelehrung ist vom 15.02.2025; die Kopie habe ich angefordert. Für unsere eigene Organisation bereite ich eine Einweisung anhand der tatsächlichen Abläufe vor.

2. Beschäftigte

Fritzi Behnke soll ab dem 12. Oktober 20 Stunden wöchentlich in Küche und Service arbeiten. Sie bringt ihre vorhandenen Belehrungsunterlagen am Montag mit. Cem Winter übernimmt zunächst ausschließlich Service und Kasse, hilft aber möglicherweise beim Anrichten der Salate. Diese Aufgabenverteilung ist noch nicht abschließend besprochen. Traudel Pohl unterstützt uns beim Spülen an zwei Abenden. Ihre Unterlagen haben wir noch nicht gesehen.

3. Schulung und Arbeitszeiten

Für den 12. Oktober ist eine gemeinsame Einweisung in Reinigung, Warenannahme, Allergenauskunft und Meldung gesundheitlicher Beschwerden geplant. Die Teilnahme wird dokumentiert. Wir möchten tatsächlichen Beginn, Ende und Pausen täglich erfassen; der bisherige Dienstplan enthält nur Sollzeiten. Ottokar richtet dafür eine einfache Erfassung ein und kontrolliert die erste Woche selbst.

4. Offene organisatorische Punkte

Die Telefonnummer des Wartungsdienstes und der Ablageort für Nachweise werden an der Innenseite der Bürotür notiert. Patientendaten oder vergleichbare sensible Unterlagen gibt es in unserem Betrieb nicht. Angaben zu Erkrankungen sollen nicht in die allgemeine Teamgruppe, sondern unmittelbar an mich gehen. Wir benötigen noch eine Vertretung für meine freien Tage.'''),
E('18_Nachtrag_ohne_Wein.eml','Eröffnung notfalls mit Birnenschorle','2026-10-02T11:15:00+02:00','Ottokar Kühn <ottokar@kichererbse.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

Mina und ich sind einverstanden, den Weinabend gegebenenfalls zu verschieben. Bitte prüfen Sie aber, ob eine vorläufige Erlaubnis für die tatsächliche Übernahme in Betracht kommt. Den Keller wollen wir wirklich nicht für Gäste nutzen. Die Reservierungsmaske ist inzwischen auf 24 Plätze gestellt; der Ausdruck vom 23. September in der Akte ist veraltet.

Wir freuen uns über einen konkreten Entwurf. Bitte keine Zusage im Namen von Fritz abgeben.

Viele Grüße
Ottokar Kühn''')]))

CASES.append(dict(slug='berlin-gewerbe-spaeti-abendfuchs',title='Der Abendfuchs und der Sonntag',plugin=PLUGIN,date='02.10.2026',client='Samira Özdemir, Betreiberin des Späti Abendfuchs',summary='Ein freundlicher Kiezladen in Friedrichshain bekommt nach einer Sonntagskontrolle Post. Stadtpläne, Kaffee, Waschmittel, Nachbarschaftsfest und eine alte Sortimentsliste führen zu unterschiedlichen Vorstellungen.',assignment='Die Betreiberin möchte auf die Anhörung sachlich antworten und eine rechtmäßige Wochenplanung erhalten. Eine echte Umgestaltung zum Café ist nur eine spätere Option.',attachments={'11_Antwort_mit_Sortiment.eml':['04_Sortiment_September.docx','06_Umsaetze_und_Zeiten.xlsx']},documents=[
D('01_Auftrag_Abendfuchs.docx','Hilfe wegen unserer Sonntagsöffnung','02.10.2026','Samira Özdemir\nSpäti Abendfuchs, Krossener Straße 47, 10245 Berlin','Rechtsanwältin Jule Morgen\nKanzlei am Kanal, Berlin', '''Sehr geehrte Frau Morgen,

ich betreibe den Abendfuchs seit 2023 als Einzelunternehmen. Am Sonntag, dem 20. September, war eine Kontrolle im Laden. Nun soll ich erklären, weshalb ich geöffnet hatte. Ich dachte, die Stadtpläne und das Hotel um die Ecke machten uns zu einem Laden für Touristen. Bei uns kaufen aber natürlich auch sehr viele Nachbarn ein, und unter der Woche führen wir Waschmittel, Nudeln und Katzenfutter.

Am Sonntag hatte mein Mitarbeiter Willibald einige Regale mit einem Vorhang abgedeckt. Ob trotzdem eine Packung Kaffee aus dem hinteren Regal verkauft wurde, weiß ich erst seit seiner Nachricht. Das möchte ich nicht verschweigen. Auf dem Kassenbon stehen außerdem zwei Flaschen Wasser und eine Zeitung. Ich habe die Belege und meine Warenübersicht beigefügt.

Bitte verfassen Sie eine sachliche Antwort auf die Anhörung und erklären Sie mir, wie ich den Laden in den kommenden Wochen rechtmäßig öffnen kann. Ich möchte nicht sofort klagen und auch keine Geschichte über einen Touristenladen erfinden. Wenn meine bisherige Vorstellung falsch war, muss ich die Planung ändern. Der Laden ist klein, und ich arbeite selbst viele Schichten.

Die Idee eines richtigen Cafés mit weniger Handel können wir später prüfen. Für jetzt brauche ich keine Umbauplanung. Das Straßenfest Ende Oktober ist ebenfalls noch nicht sicher. Bitte senden Sie ohne meine Rückmeldung nichts an das Amt. Die Frist im Brief endet am 9. Oktober.

Mit freundlichen Grüßen
Samira Özdemir'''),
D('02_Gewerbeempfang.docx','Empfang der Gewerbeanzeige','03.04.2023','Bezirksamt Friedrichshain-Kreuzberg von Berlin\nOrdnungsamt, Gewerbeangelegenheiten','Samira Özdemir\nKrossener Straße 47, 10245 Berlin', '''Sehr geehrte Frau Özdemir,

der Eingang Ihrer Gewerbeanzeige vom 01.04.2023 wird bestätigt. Angezeigt wurde der Beginn eines Einzelhandels mit Lebensmitteln, Getränken, Zeitungen, Tabakwaren und Waren des täglichen Bedarfs unter der Geschäftsbezeichnung Abendfuchs am Standort Krossener Straße 47. Als Beginn der Tätigkeit haben Sie den 01.04.2023 angegeben. Die Anzeige wird unter dem nachstehend genannten Geschäftszeichen geführt.

Diese Bescheinigung bestätigt den Eingang der von Ihnen abgegebenen Anzeige. Sie enthält keine besondere Erlaubnis zur Öffnung an Sonn- und Feiertagen und keine Entscheidung über eine gaststättenrechtliche, baurechtliche oder straßenrechtliche Zulassung. Soweit für einzelne Tätigkeiten zusätzliche Anforderungen gelten, sind diese gesondert zu beachten. Bitte bewahren Sie die Bescheinigung bei Ihren Betriebsunterlagen auf.

Die von Ihnen angegebenen Daten werden nach Maßgabe der gesetzlichen Regelungen an die zuständigen Stellen weitergeleitet. Änderungen der angezeigten Tätigkeit, eine Verlegung innerhalb Berlins und die Aufgabe des Betriebs sind mit dem jeweils vorgesehenen Verfahren mitzuteilen. Bitte nennen Sie bei Rückfragen stets die Geschäftsbezeichnung und den Standort, damit eine eindeutige Zuordnung möglich ist.

In Ihrer Anzeige ist kein Ausschank alkoholischer Getränke zum Verzehr an Ort und Stelle bezeichnet. Sollte sich das tatsächliche Betriebskonzept ändern, beschreiben Sie die vorgesehenen Tätigkeiten rechtzeitig gegenüber der zuständigen Stelle. Diese allgemeine Information ersetzt keine Prüfung eines späteren konkreten Vorhabens. Eine Kopie Ihrer Anzeige befindet sich in der Betriebsakte.

Im Auftrag
Marlene Hoff''',reference='Gew-FK-23-903'),
E('03_Hotelkooperation.eml','Stadtpläne für unsere Gäste','2026-08-18T10:00:00+02:00','Hotel Kiezkissen <empfang@kiezkissen.example>','Samira Özdemir <samira@abendfuchs.example>', '''Liebe Samira,

wir schicken unsere Gäste gern zu dir, wenn sie Wasser oder einen Stadtplan brauchen. Einen Exklusivvertrag brauchen wir dafür nicht. Unser Hotel hat 28 Zimmer, die Belegung schwankt. Wie viele Gäste wirklich zu dir kommen, erfassen wir nicht. Bitte schreib also nicht, dass wir täglich eine bestimmte Kundenzahl garantieren.

Viele Grüße
Luise Chen, Empfang'''),
D('04_Sortiment_September.docx','Warenübersicht und Überlegungen zum Sortiment','15.09.2026','Samira Özdemir\nSpäti Abendfuchs','Interne Ablage', '''1. Aktuelles Angebot

Wir führen gekühlte Getränke, Bier, Wein, verpackte Snacks, Zeitungen, Tabakwaren, Kaffee, Tee, Nudeln, Konserven, Waschmittel, Toilettenpapier und Katzenfutter. Im vorderen Regal liegen außerdem Postkarten und Stadtpläne. Die Stadtpläne sind seit August im Angebot. Zwei Kartons mit älteren Reiseführern wurden noch nicht ausgepackt. Die Lebensmittel werden überwiegend originalverpackt abgegeben; frische belegte Brötchen bieten wir derzeit nicht an.

2. Kunden und Zeiten

Unter der Woche kommen vor allem Menschen aus den umliegenden Häusern. Am Wochenende besuchen uns zusätzlich Hotelgäste und Spaziergänger. Wir erfassen weder Wohnort noch Reisezweck der Kunden. Die bisherige Ladenöffnung ist Montag bis Samstag von 8 bis 24 Uhr. Sonntags haben wir zuletzt von 13 bis 20 Uhr geöffnet, weil ich von einer passenden Ausnahme ausging. Eine schriftliche Entscheidung speziell für unsere Sonntagsöffnung liegt nicht vor.

3. Kaffee und Sitzgelegenheit

Neben der Kasse steht eine kleine Kaffeemaschine. Kaffee wird im Becher abgegeben. Zwei Hocker am Fenster werden gelegentlich genutzt, meist wartet dort jemand auf die Begleitung. Eine gesonderte Speisekarte oder Bedienung an Tischen gibt es nicht. Alkohol wird in verschlossenen Flaschen verkauft. Eine spätere Umgestaltung zu einem kleinen Café wurde mit dem Vermieter nur unverbindlich angesprochen.

4. Noch nicht umgesetzte Änderungen

Ich überlege, Haushaltswaren ganz aus dem Sortiment zu nehmen. Das ist noch keine Entscheidung. Die vorhandene Ware bleibt bis auf Weiteres unter der Woche im Verkauf. Sonntags wurde ein Teil des hinteren Regals zuletzt mit einem Vorhang verdeckt. Willibald soll mir sagen, ob das im Alltag überhaupt eindeutig gehandhabt wurde.'''),
D('05_Kontrollvermerk.docx','Kontrolle am Sonntag, 20. September','21.09.2026','Bezirksamt Friedrichshain-Kreuzberg von Berlin\nOrdnungsamt, Außendienst','Betriebsakte Abendfuchs', '''Am 20.09.2026 wurde die Verkaufsstelle Abendfuchs in der Krossener Straße 47 um 15.12 Uhr geöffnet angetroffen. Im Laden befanden sich der Beschäftigte Willibald Kraft sowie drei Kunden. Die Inhaberin war nicht anwesend. Angeboten wurden im vorderen Bereich Getränke, Tabakwaren, Zeitungen, Süßwaren, Postkarten und Stadtpläne. Ein Teil des hinteren Regals war durch einen Stoffvorhang verdeckt. Seitlich waren Packungen mit Nudeln und Tierfutter erkennbar.

Während der Anwesenheit wurde an einen Kunden eine Packung gemahlener Kaffee, zwei Flaschen Wasser und eine Zeitung abgegeben. Der Beschäftigte nahm die Kaffeepackung aus einem Regal hinter dem Vorhang. Er erklärte, dass er den Kunden kenne und dieser regelmäßig sonntags komme. Der Kunde verließ den Laden, ohne dass seine Personalien festgestellt wurden. Ein Kassenbon wurde ausgedruckt; eine Kopie wurde mit Zustimmung des Beschäftigten zur Akte genommen.

An der Eingangstür hing ein Schild „Sonntag 13 bis 20 Uhr“. Eine besondere behördliche Öffnungsentscheidung konnte vor Ort nicht vorgelegt werden. Der Beschäftigte verwies auf die Stadtpläne und das nahe Hotel. Eine abschließende rechtliche Bewertung wurde mit ihm nicht erörtert. Er erhielt den Hinweis, dass die Inhaberin schriftlich angehört werde.

Die beiden Hocker am Fenster waren während der Kontrolle unbesetzt. Ein Ausschank alkoholischer Getränke wurde nicht beobachtet. Die Maschine für Kaffee im Becher stand eingeschaltet neben der Kasse. Über das gesamte Wochensortiment und die wirtschaftliche Verteilung der Umsätze konnten vor Ort keine verlässlichen Angaben gemacht werden.

Notiert von Karlotta Weiss''',reference='Lad-FK-26-441'),
X('06_Umsaetze_und_Zeiten.xlsx','Umsatzgruppen und Wochenzeiten',[dict(name='Umsatzgruppen',headers=['Warengruppe','Mo bis Sa EUR','Sonntag EUR','Gesamt EUR'],widths=[38,24,22,22],formats={'B':'#,##0.00','C':'#,##0.00','D':'#,##0.00'},rows=[['Getraenke',2450,430,'=B2+C2'],['Tabak und Zeitungen',1340,210,'=B3+C3'],['Snacks und Kaffee',720,95,'=B4+C4'],['Haushalt und Vorrat',860,18,'=B5+C5'],['Postkarten und Plaene',65,22,'=B6+C6'],['Gesamt','=SUM(B2:B6)','=SUM(C2:C6)','=SUM(D2:D6)']],expected={'B7':5435,'C7':775,'D7':6210},perturbations=[{'input':'C5','value':0,'output':'C7','expected':757}]),dict(name='Wochenplan',headers=['Tag','Beginn h','Ende h','Stunden','Besetzung'],widths=[30,16,16,16,45],formats={'B':'0.00','C':'0.00','D':'0.00'},rows=[['Montag',8,24,'=C2-B2','Samira und Willibald, getrennte Schichten'],['Dienstag',8,24,'=C3-B3','Samira und Willibald, getrennte Schichten'],['Mittwoch',8,24,'=C4-B4','Samira und Hedi, getrennte Schichten'],['Donnerstag',8,24,'=C5-B5','Samira und Hedi, getrennte Schichten'],['Freitag',8,24,'=C6-B6','Samira und Willibald, getrennte Schichten'],['Samstag',8,24,'=C7-B7','Samira und Hedi, getrennte Schichten'],['Sonntag bisher',13,20,'=C8-B8','Willibald; Plan wird ueberprueft']],expected={'D8':7},perturbations=[{'input':'C8','value':18,'output':'D8','expected':5}])]),
T('07_Kassenbon_Abschrift.txt','Abschrift des Bons vom Kontrolltag','20.09.2026', '''Abendfuchs, Krossener Straße 47, Berlin
Bon 20260920-0048, 20.09.2026 15:14
Gemahlener Kaffee 500 g             6,49 EUR
Mineralwasser 0,5 l, zwei Flaschen   3,00 EUR
Pfand zwei Flaschen                 0,50 EUR
Sonntagszeitung                     3,20 EUR
Summe                             13,19 EUR
Bar erhalten                      15,00 EUR
Rückgeld                           1,81 EUR

Samiras Notiz: Abschrift vom Originalbon. Kaffee ist die Packung aus dem hinteren Regal, kein zubereiteter Kaffee im Becher.'''),
E('08_Willibald_erklaert.eml','Was am Sonntag passiert ist','2026-09-22T19:30:00+02:00','Willibald Kraft <willibald@abendfuchs.example>','Samira Özdemir <samira@abendfuchs.example>', '''Liebe Samira,

ja, ich habe die Kaffeepackung verkauft. Herr Wendt kauft sie fast jede Woche und fragte ausdrücklich danach. Ich dachte, der Vorhang sei vor allem gegen die freie Auswahl gedacht. Das war offenbar nicht klar. Die zwei Hocker waren leer, niemand hat dort Bier getrunken. Bitte schreib dem Amt nicht, dass es nur Kaffee aus der Maschine war.

Willibald'''),
D('09_Anhoerung_Ladenoeffnung.docx','Anhörung zur Sonntagsöffnung des Abendfuchs','25.09.2026','Bezirksamt Friedrichshain-Kreuzberg von Berlin\nOrdnungsamt, Gewerbeangelegenheiten','Samira Özdemir\nKrossener Straße 47, 10245 Berlin', '''Sehr geehrte Frau Özdemir,

nach dem beigefügten Kontrollvermerk war Ihre Verkaufsstelle am Sonntag, dem 20.09.2026, um 15.12 Uhr geöffnet. Es wurden unter anderem gemahlener Kaffee in einer Verkaufspackung, Wasser und eine Zeitung abgegeben. Nach den bislang vorliegenden Informationen handelt es sich um einen Einzelhandel mit gemischtem Sortiment für den täglichen Bedarf. Eine besondere Öffnungsentscheidung für diesen Sonntag ist uns nicht bekannt.

Wir geben Ihnen Gelegenheit, bis zum 09.10.2026 zu den Feststellungen Stellung zu nehmen. Bitte teilen Sie mit, auf welchen Ausnahmetatbestand Sie die Sonntagsöffnung stützen, und beschreiben Sie das tatsächlich während der gesamten Woche angebotene Sortiment. Wenn Sie von einer besonderen touristischen Ausrichtung ausgehen, erläutern Sie die dafür maßgeblichen Umstände. Die bloße Nähe zu einem Beherbergungsbetrieb genügt als tatsächliche Beschreibung noch nicht.

Es wird geprüft, ob Ihnen das Offenhalten der Verkaufsstelle an Sonn- und Feiertagen außerhalb zulässiger Ausnahmen durch eine gesonderte Verfügung zu untersagen ist. Eine solche Verfügung ist mit diesem Schreiben noch nicht erlassen. Über einen etwaigen Ordnungswidrigkeitenvorgang wird gesondert entschieden. Diese Anhörung ist nicht als Erlaubnis zur weiteren Sonntagsöffnung zu verstehen.

Bitte reichen Sie vorhandene Belege geordnet unter Angabe des Geschäftszeichens ein. Soweit Sie den Betrieb seit der Kontrolle tatsächlich geändert haben, nennen Sie Datum und Umfang der Änderung. Für eine Einsicht in die vorhandenen Unterlagen können Sie einen Termin vereinbaren oder die Übersendung elektronischer Kopien beantragen.

Im Auftrag
Marlene Hoff''',reference='Lad-FK-26-441'),
E('10_Samira_fragt_Amt.eml','Lad-FK-26-441: Unterlagen und Frist','2026-09-28T11:06:00+02:00','Samira Özdemir <samira@abendfuchs.example>','Marlene Hoff <gewerbe@amt-fk.example>', '''Sehr geehrte Frau Hoff,

ich habe Ihr Schreiben am Samstag aus dem Briefkasten genommen. Ich werde bis zum 9. Oktober antworten und lasse mich beraten. Bitte senden Sie mir eine lesbare Kopie des Kontrollvermerks; die letzte Seite meines Ausdrucks ist sehr blass. Eine Verlängerung beantrage ich derzeit nicht. Am vergangenen Sonntag blieb der Laden geschlossen.

Mit freundlichen Grüßen
Samira Özdemir'''),
E('11_Antwort_mit_Sortiment.eml','Unterlagen für Ihre Prüfung','2026-09-29T20:17:00+02:00','Samira Özdemir <samira@abendfuchs.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

anbei die Warenübersicht und meine Tabelle für die Woche vom 14. bis 20. September. Die Umsatzgruppen kommen aus meiner Kasse; sie sagen nichts darüber, ob ein Kunde Tourist ist. Die 18 EUR sonntags bei Haushalt und Vorrat enthalten den Kaffee und weitere Kleinigkeiten, die ich noch mit Willibald zuordnen muss. Bitte verwenden Sie die Zeile nicht als Zahl der verkauften Packungen.

Freundliche Grüße
Samira Özdemir'''),
D('12_Veranstalter_Absicht.docx','Vorläufige Planung eines Nachbarschaftstags','30.09.2026','Kiezrunde Abendsonne e. V.\nVorsitzender Balthasar Nguyen','Samira Özdemir\nSpäti Abendfuchs', '''Liebe Frau Özdemir,

wir planen für Sonntag, den 25. Oktober 2026, einen kleinen Nachbarschaftstag im Hof unseres Vereinsraums. Vorgesehen sind eine Pflanzentauschbörse, ein Reparaturtisch für kleine Haushaltsgegenstände und ein Kinderbüchertausch. Die Veranstaltung soll von 14 bis 18 Uhr stattfinden. Wir rechnen derzeit mit etwa 80 bis 120 Besuchern über den Nachmittag verteilt. Diese Schätzung beruht auf unserem Sommertermin und ist keine zugesagte Besucherzahl.

Wir hatten besprochen, dass Ihr Laden Wasser und verpackte Snacks für die Helfer liefern könnte. Ein eigener Verkaufsstand im Hof wurde noch nicht vereinbart. Ebenso haben wir keine Aussage dazu getroffen, ob Ihr Geschäft an diesem Tag geöffnet sein darf. Die öffentlich-rechtlichen Fragen unseres Festes klären wir getrennt. Der Hof liegt rund 350 Meter von Ihrem Laden entfernt und ist von dort nicht unmittelbar sichtbar.

Die endgültige Zusage der Hausgemeinschaft steht noch aus. Falls sie ausbleibt, verschieben wir den Termin auf einen Samstag im November. Bitte lassen Sie deshalb noch keine kostenpflichtigen Plakate drucken. Wir möchten erst am 7. Oktober verbindlich über Termin und Ort entscheiden. Eine Anzeige zur besonderen Sonntagsöffnung Ihres Ladens haben wir für Sie nicht erstattet.

Gern informieren wir Sie über den weiteren Stand. Uns ist wichtig, dass die Veranstaltung überschaubar bleibt und die Nachbarn eingebunden werden. Eine Bühne, verstärkte Musik oder ein großer Straßenverkauf sind nicht vorgesehen. Wir freuen uns über Ihre Unterstützung als Lieferantin, auch wenn Ihr Laden an diesem Sonntag geschlossen bleibt.

Herzliche Grüße
Balthasar Nguyen'''),
T('13_Chat_Kaffeeidee.txt','Kleiner Teamchat zur Kaffeeidee','30.09.2026', '''30.09.2026 17:10 Hedi: Könnten wir nicht einfach Café auf das Schild schreiben?
30.09.2026 17:13 Samira: So einfach wohl nicht. Ich möchte wirklich wissen, was wir dürfen.
30.09.2026 17:15 Willibald: Zwei Hocker und die Maschine machen noch keinen schönen Cafébetrieb. Küche haben wir auch keine.
30.09.2026 17:20 Hedi: Dann planen wir erstmal die Woche ordentlich. Ich kann samstags früher anfangen.
30.09.2026 17:23 Samira: Danke. Den Sonntag am 4. Oktober lassen wir vorerst geschlossen. Das Fest ist noch nicht bestätigt.'''),
D('14_Mietvertragsnachtrag_Entwurf.docx','Entwurf: mögliche Erweiterung der Nutzung','01.10.2026','Hausverwaltung Fuchsbogen\nEntwurfsstand ohne Unterschriften','Samira Özdemir', '''1. Gegenstand der Besprechung

Die Parteien erwägen, die bisher als Einzelhandelsfläche vermieteten Räume künftig teilweise für einen kleinen Cafébetrieb zu nutzen. Gegenstand dieses Entwurfs ist allein die zivilrechtliche Zustimmung der Vermieterseite zu einer später näher beschriebenen Nutzung. Eine verbindliche Änderung des Mietvertrags ist bisher nicht vereinbart. Der bestehende Mietvertrag bleibt bis zu einer Unterzeichnung unverändert.

2. Noch festzulegender Umfang

Die Zahl der Sitzplätze, die tatsächliche Zubereitung von Speisen und Getränken, die Lüftung sowie die Betriebszeiten sind noch offen. Die Mieterin wird ein konkretes Konzept vorlegen. Ein Ausschank alkoholischer Getränke und eine Nutzung des Gehwegs sind von diesem Entwurf nicht umfasst. Bauliche Veränderungen bedürfen einer vorherigen Abstimmung mit der Vermieterseite und dürfen erst nach Klärung erforderlicher öffentlich-rechtlicher Voraussetzungen begonnen werden.

3. Behörden und Kosten

Die Vermieterseite erteilt mit diesem Entwurf keine Aussage zur Genehmigungsfähigkeit. Die Parteien werden nach Vorliegen des Konzepts festlegen, wer welche Planungs- und Antragskosten trägt. Eine Verpflichtung der Mieterin zur Umsetzung eines Cafébetriebs besteht nicht. Die bloße Erwähnung dieses Entwurfs gegenüber Dritten darf nicht als bereits erteilte behördliche Erlaubnis oder endgültige mietvertragliche Zustimmung dargestellt werden.

4. Weiteres Vorgehen

Für den 20. Oktober ist ein unverbindliches Gespräch vorgesehen. Bis dahin sollen keine Einbauten bestellt werden. Samira Özdemir kann sich nach rechtlicher und wirtschaftlicher Prüfung entscheiden, den bisherigen Einzelhandel unverändert fortzuführen. Beide Seiten möchten vermeiden, dass eine vorschnelle Bezeichnung als Café Erwartungen auslöst, die der tatsächliche Betrieb nicht erfüllt.

Unterschriften sind nicht geleistet.'''),
E('15_Amt_Kopie.eml','Lad-FK-26-441: Kontrollvermerk','2026-10-01T09:12:00+02:00','Marlene Hoff <gewerbe@amt-fk.example>','Samira Özdemir <samira@abendfuchs.example>', '''Sehr geehrte Frau Özdemir,

Sie können den Kontrollvermerk in unserem Portal erneut herunterladen. Die vorhandene Fassung umfasst drei beschriebene Seiten einschließlich der Bonkopie. Derzeit liegen keine weiteren Kontrollfeststellungen zu einem Alkoholausschank vor. Die Anhörungsfrist 9. Oktober bleibt bestehen. Über eine Untersagungsverfügung ist noch nicht entschieden.

Mit freundlichen Grüßen
Marlene Hoff'''),
D('16_Betriebsnotiz_Wochenplanung.docx','Arbeitsstand für die nächsten beiden Wochen','01.10.2026','Samira Özdemir','Willibald Kraft und Hedi Santos', '''1. Öffnung und Kundeninformation

Für den 4. und 11. Oktober plane ich zunächst keine Sonntagsöffnung. An die Tür kommt ein sachlicher Hinweis, dass wir die Öffnungszeiten prüfen und an diesen beiden Tagen geschlossen bleiben. Bitte diskutiert mit Kunden keine angebliche Ausnahme, solange wir hierzu keinen belastbaren Stand haben. Die Werktagsöffnung bleibt vorerst wie bisher. Änderungen teilen wir gemeinsam mit.

2. Sortiment und Kasse

Die Warenliste vom 15. September beschreibt das aktuelle Angebot. Haushaltswaren und Vorratslebensmittel werden nicht heimlich aus der Liste gestrichen, solange wir sie weiter verkaufen. Bitte ordnet Verkäufe in der Kasse der zutreffenden Gruppe zu. Die vorhandene Gruppe „Snacks und Kaffee“ soll künftig zwischen zubereitetem Kaffee und Verkaufspackungen unterscheiden. Alte Buchungen werden dabei nicht überschrieben; Erläuterungen werden als Notiz ergänzt.

3. Schichten und Aufgaben

Die Tabelle enthält die Ladenzeiten, nicht die Arbeitszeit einer einzelnen Person. Wir erstellen weiterhin getrennte Schichten und erfassen tatsächlichen Beginn, Ende und Pausen. Hedi übernimmt am Samstagvormittag die Warenannahme. Willibald prüft mit mir den Bestand an Zeitungen und Stadtplänen. Ich bleibe für die Behördenkorrespondenz verantwortlich und leite die Antwort zur gemeinsamen Information weiter.

4. Spätere Entscheidungen

Über eine echte Umgestaltung des Betriebs sprechen wir erst nach der Beratung und dem Termin mit der Vermietung. Es werden keine neuen Hocker oder Küchengeräte bestellt. Die Unterstützung des Nachbarschaftstags als Lieferantin kann unabhängig davon vorbereitet werden, sobald der Verein den Termin bestätigt. Bis dahin geben wir keine öffentliche Zusage für eine Ladenöffnung am Veranstaltungstag ab.'''),
E('17_Nachbar_freundlich.eml','Danke für die frühen Flaschenkisten','2026-10-01T18:43:00+02:00','Traugott Wendt <traugott@nachbarschaft.example>','Samira Özdemir <samira@abendfuchs.example>', '''Liebe Frau Özdemir,

danke, dass die Flaschenkisten jetzt morgens statt kurz vor Mitternacht abgeholt werden. Das hilft uns im Vorderhaus. Ich war der Kunde mit der Kaffeepackung am Sonntag. Wenn Sie den Vorgang erklären müssen, bestätige ich gern, was ich gekauft habe. Ich möchte Ihnen keine Schwierigkeiten machen, aber auch nichts Falsches erzählen.

Herzliche Grüße
Traugott Wendt'''),
E('18_Nachtrag_Fest_offen.eml','Zum Fest bitte noch nichts behaupten','2026-10-02T10:02:00+02:00','Samira Özdemir <samira@abendfuchs.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

der Verein hat den Hof noch nicht sicher. Bitte begründen Sie die Kontrolle vom 20. September nicht mit dem erst geplanten Oktoberfest. Das sind zwei verschiedene Termine. Mir ist am wichtigsten, die Antwort korrekt zu machen und künftig einen verlässlichen Plan zu haben.

Viele Grüße
Samira Özdemir''')]))

CASES.append(dict(slug='berlin-gewerbe-radiologie-spreebogen',title='Radiologie Spreebogen bekommt ein CT',plugin=PLUGIN,date='02.10.2026',client='Dr. Nela Ahrens und Dr. Farid Benali, Berufsausübungsgemeinschaft Radiologie Spreebogen',summary='Eine ärztliche Berufsausübungsgemeinschaft erweitert ihren bestehenden MRT-Betrieb um ein CT. Lieferant, Fachkundenachweise, Raumbezeichnung und geplanter Abendbetrieb sind noch nicht vollständig abgestimmt.',assignment='Die Ärzte möchten ein präzises Abstimmungsschreiben an LAGetSi und einen belastbaren Startplan. Der bisherige MRT-Betrieb soll sachgerecht getrennt betrachtet werden.',attachments={'08_Anzeige_Nachreichung.eml':['04_Geraete_und_Raeume.docx','06_Startplan_und_Kosten.xlsx'],'15_Sachverstaendige_Nachtrag.eml':['13_Pruefbericht_Auszug.docx']},documents=[
D('01_Auftrag_Radiologie.docx','CT-Erweiterung unserer Praxis','02.10.2026','Dr. Nela Ahrens und Dr. Farid Benali\nRadiologie Spreebogen, Alt-Moabit 149, 10557 Berlin','Rechtsanwältin Jule Morgen\nKanzlei am Kanal, Berlin', '''Sehr geehrte Frau Morgen,

wir betreiben seit 2021 gemeinsam eine ärztliche Berufsausübungsgemeinschaft mit MRT-Diagnostik. Nun kommt ein CT hinzu. Der Lieferant möchte am 5. Oktober technisch übergeben, und unser Praxismanagement hat erste Patiententermine ab dem 19. Oktober vorgemerkt. Wir möchten die Inbetriebnahme rechtlich und organisatorisch sauber vorbereiten. Eine Gewerbeanmeldung liegt für unsere Heilbehandlung bisher nicht vor; der Geräteverkäufer hat uns dazu widersprüchliche Hinweise gegeben.

Die Anzeige an LAGetSi haben wir am 21. September versandt. Die Behörde hat danach noch Unterlagen verlangt. Insbesondere stimmen die Raumbezeichnungen in zwei Dokumenten nicht überein. Tatsächlich geht es um denselben Raum, der nach dem Umbau intern eine andere Nummer bekam. Ob der Sachverständigenbericht schon vollständig genügt, möchten wir prüfen lassen. Wir haben Ihnen den aktuellen Auszug und die E-Mails beigefügt.

Zunächst soll das CT werktags nur betrieben werden, wenn Farid vor Ort ist. Für einen späteren Abendbetrieb wurde unverbindlich eine teleradiologische Zusammenarbeit angefragt. Dazu gibt es noch keinen Vertrag und keinen Genehmigungsbescheid. Bitte behandeln Sie das nicht als bereits bestehende Organisation.

Wir benötigen ein genaues Schreiben an LAGetSi und einen verständlichen Plan für das Praxismanagement. Der seit Jahren laufende MRT-Betrieb soll nicht ohne Anlass mit dem CT gleichgesetzt werden. Bitte reichen Sie ohne Rücksprache nichts ein. Wir möchten insbesondere vermeiden, Patientinnen und Patienten einen Termin zu bestätigen, den wir anschließend absagen müssen.

Mit freundlichen Grüßen
Nela Ahrens und Farid Benali'''),
D('02_Betreiberdarstellung.docx','Organisation der Berufsausübungsgemeinschaft','10.09.2026','Dr. Nela Ahrens und Dr. Farid Benali','Für die Betriebsunterlagen', '''1. Rechtlicher und wirtschaftlicher Betrieb

Dr. Nela Ahrens und Dr. Farid Benali führen die Radiologie Spreebogen als rechtsfähige Gesellschaft bürgerlichen Rechts. Beide sind approbierte Ärzte und Gesellschafter zu gleichen Teilen. Der Gesellschaftsvertrag sieht gemeinsame Vertretung bei Anschaffung wesentlicher Geräte und Abschluss langfristiger Verträge vor. Die Behandlungsverträge werden durch die Berufsausübungsgemeinschaft geschlossen. Die Praxisräume und Geräte werden nicht an eine gesonderte Betreibergesellschaft vermietet.

2. Bisherige Tätigkeit

Seit 2021 bietet die Praxis MRT-Untersuchungen an. Es werden keine offenen radioaktiven Stoffe verwendet. Eine nuklearmedizinische Tätigkeit und Strahlentherapie sind nicht vorgesehen. Ein kleiner Bestand an Ohrstöpseln und Patientenbekleidung wird ausschließlich für die Untersuchungen vorgehalten; ein eigenständiger Warenhandel besteht nicht. Das CT wird als zusätzliches diagnostisches Gerät angeschafft.

3. Verantwortungszuordnung

Farid soll die strahlenschutzbezogenen Aufgaben für den CT-Betrieb koordinieren. Der Entwurf der internen Zuordnung wurde noch nicht von beiden Gesellschaftern unterschrieben. Die genaue Mitteilung an die Behörde und die erforderlichen Bestellungen sollen nach Beratung abschließend erstellt werden. Nela übernimmt weiterhin das allgemeine Praxismanagement und den Schwerpunkt MRT. Beide bleiben in die wesentlichen Entscheidungen eingebunden.

4. Personal und Zeiten

Die Praxis beschäftigt drei medizinisch-technische Mitarbeiterinnen sowie zwei Kräfte an der Anmeldung. Der erste CT-Dienstplan ist noch vorläufig. Urlaub und Vertretung für Farid im November sind nicht geklärt. Der beabsichtigte Start am 19. Oktober ist eine Planungsannahme und keine gegenüber Patienten verbindlich abgegebene Zusage. Eine spätere Ausweitung der Betriebszeiten wird gesondert vorbereitet.'''),
E('03_Lieferant_Startsignal.eml','Ihr CT ist bald startklar','2026-09-14T13:08:00+02:00','Bildwerk Medizintechnik <vertrieb@bildwerk.example>','Radiologie Spreebogen <organisation@radiologie-spreebogen.example>', '''Sehr geehrte Frau Dr. Ahrens,

die technische Übergabe ist für den 5. Oktober vorgesehen. Unser Vertrieb sagt gelegentlich „betriebsbereit“, meint damit aber unsere Installation und Einweisung. Die behördlichen und medizinischen Voraussetzungen prüfen wir für Sie nicht. Bitte stimmen Sie Patiententermine mit Ihren Fachleuten ab. Für einen Gewerbeschein kann ich Ihnen leider keine belastbare Auskunft geben; meine vorige Nachricht war insoweit zu pauschal.

Freundliche Grüße
Benno Krull'''),
D('04_Geraete_und_Raeume.docx','Gerätebestand und Raumbezeichnungen','16.09.2026','Praxismanagerin Malika Roth\nRadiologie Spreebogen','Dr. Nela Ahrens und Dr. Farid Benali', '''1. Vorhandenes MRT

Das MRT-Gerät MR-SB-01 steht seit 2021 im Untersuchungsraum am Ende des Flurs. An diesem Raum und am Gerät sind im Zusammenhang mit der CT-Erweiterung keine Umbauten vorgesehen. Der Zugang erfolgt weiterhin durch den kontrollierten Bereich. Die vorhandene Geräteakte, Einweisungsunterlagen und Wartungsnachweise liegen im Technikschrank. Die Patientenanmeldung wird von beiden Bereichen gemeinsam genutzt.

2. Neues CT

Das CT-Gerät CT-SB-02 soll im ehemaligen Archivraum aufgestellt werden. In den Planunterlagen des Vermieters heißt dieser Raum „Raum 2“. Nach unserer internen Umnummerierung im Sommer verwenden wir die Bezeichnung „Raum 3“. Es ist derselbe Raum gegenüber dem Personalzimmer. Die Seriennummer des endgültig gelieferten Geräts lautet BW-CT-260914. Das Angebot aus Mai nannte noch eine vorläufige Projektnummer.

3. Bauliche Arbeiten und Unterlagen

Die Abschirmung wurde nach dem Plan der Fachfirma eingebaut. Der abschließende Nachweis für die Tür war bei Erstellung dieser Übersicht noch offen. Eine bloße Rechnung der Baufirma soll nicht als vollständiger technischer Nachweis abgelegt werden. Die vorhandene bauaufsichtliche Korrespondenz und die Zustimmung des Vermieters befinden sich im Projektordner. Ob der gesamte Vorgang abgeschlossen ist, wird noch mit der Planerin geklärt.

4. Nicht geplante Anwendungen

Offene radioaktive Stoffe, nuklearmedizinische Diagnostik und therapeutische Bestrahlung sind nicht Teil dieses Projekts. Der CT-Betrieb soll zunächst ausschließlich während persönlicher Anwesenheit von Farid stattfinden. Eine Anfrage wegen späterer Teleradiologie liegt lediglich als E-Mail vor. Bitte verwenden Sie diese Übersicht nur gemeinsam mit den aktuellen technischen Nachweisen.'''),
D('05_Personal_Fachkunde.docx','Nachweise und Einsatz für den CT-Start','18.09.2026','Dr. Farid Benali','Interne Projektakte CT', '''1. Ärztliche Nachweise

Meine Fachkundebescheinigung für die vorgesehenen diagnostischen CT-Anwendungen liegt in der Personalakte. Die letzte Aktualisierung habe ich im Mai 2025 abgeschlossen. Die Kopien wurden für die Anzeige eingescannt, allerdings ist auf einer Seite der Rand abgeschnitten. Eine vollständige Fassung wird erneut bereitgestellt. Nelas Fachkundenachweis betrifft nicht ohne Weiteres jede von mir geplante CT-Anwendung. Sie wird den CT-Betrieb daher zunächst nicht allein vertreten.

2. Medizinisch-technisches Personal

Malika hat für zwei Mitarbeiterinnen die vorhandenen Berufs- und Kenntnisnachweise zusammengestellt. Bei der dritten Kollegin ist die Aktualisierungsbescheinigung noch beim früheren Arbeitgeber angefordert. Bis zur Klärung wird sie nicht allein am CT eingesetzt. Der genaue Einsatzplan soll nach Vorliegen der Einweisung und der technischen Übergabe festgelegt werden. Ein im Kalender eingetragener Dienst ist noch keine Bestätigung, dass sämtliche fachlichen Voraussetzungen bereits geprüft sind.

3. Verantwortung und Vertretung

Ich soll die strahlenschutzbezogene Organisation führen. Der Umfang meiner Befugnisse, die Vertretung und die erforderliche Anzeige unserer Zuordnung werden mit Nela abgestimmt. Die Dokumente sollen die tatsächliche Gesellschaftsorganisation wiedergeben. Eine für November geplante Fortbildungsreise ist bei der Betriebsplanung zu berücksichtigen. Für diesen Zeitraum ist noch kein CT-Vertreter verbindlich zugesagt.

4. Geplante Anwendungszeiten

Wir starten, wenn die Voraussetzungen vorliegen, montags bis freitags von 9 bis 16 Uhr. Ein Abendbetrieb wird nicht allein aufgrund meiner telefonischen Erreichbarkeit aufgenommen. Die Anfrage an einen teleradiologischen Dienst betrifft eine spätere Erweiterung. Patiententermine werden zunächst nur vorgemerkt und erst nach der internen Freigabe bestätigt. Ich bitte das Praxisteam, diese Unterscheidung bei der Terminvergabe ausdrücklich zu verwenden.'''),
X('06_Startplan_und_Kosten.xlsx','Projektkosten und Nachweisstand',[dict(name='Kosten',headers=['Position','Beauftragt EUR','Bezahlt EUR','Offen EUR','Stand'],widths=[30,22,22,20,35],formats={'B':'#,##0.00','C':'#,##0.00','D':'#,##0.00'},rows=[['CT-Anschaffung',245000,196000,'=B2-C2','Rest bei technischer Uebergabe'],['Abschirmung',18500,15000,'=B3-C3','Tuernachweis ausstehend'],['Sachverstaendige',2100,0,'=B4-C4','Nachtermin vorgesehen'],['Einweisung',1800,0,'=B5-C5','Termin 5. Oktober'],['Gesamt','=SUM(B2:B5)','=SUM(C2:C5)','=SUM(D2:D5)','Keine Betriebsfreigabe aus Zahlung']],expected={'B6':267400,'C6':211000,'D6':56400},perturbations=[{'input':'C4','value':2100,'output':'D6','expected':54300}]),dict(name='Nachweise',headers=['Unterlage','Erforderlich intern','Vorhanden','Differenz','Hinweis'],widths=[35,20,18,18,48],formats={'B':'0','C':'0','D':'0'},rows=[['Vollstaendige Fachkundekopie',1,0,'=B2-C2','Seite abgeschnitten; neu scannen'],['Abschluss Tuernachweis',1,0,'=B3-C3','Nachmessung angefragt'],['Betreiberzuordnung unterschrieben',1,0,'=B4-C4','Entwurf liegt vor'],['Geraeteidentifikation',1,1,'=B5-C5','Seriennummer steht fest'],['Offene Unterlagen','=SUM(B2:B5)','=SUM(C2:C5)','=SUM(D2:D5)','Interne Liste, keine Vollstaendigkeitsgarantie']],expected={'D6':3},perturbations=[{'input':'C2','value':1,'output':'D6','expected':2}])]),
T('07_Terminnotizen.txt','Projekttermine, Stand 21. September','21.09.2026', '''21.09.2026 Anzeige versandt; Unterlagen noch nicht alle abschließend geprüft.
24.09.2026 Geplante Erstprüfung der Sachverständigen.
28.09.2026 Rückfrage wegen Abschirmung der Tür.
02.10.2026 Beratungstermin.
05.10.2026 Technische Übergabe und Geräteeinweisung.
06.10.2026 Frühester angebotener Nachtermin der Sachverständigen.
19.10.2026 Erste Patiententermine nur vorgemerkt, nicht bestätigt.
02.–06.11.2026 Farid auf Fortbildung; CT-Vertretung noch offen.

Malika: Die Datumsreihe ist unsere Planung. Sie enthält keine behördliche Bestätigung eines Starttags.'''),
E('08_Anzeige_Nachreichung.eml','CT-SB-02: ergänzende Gerätedaten','2026-09-22T10:44:00+02:00','Dr. Farid Benali <farid@radiologie-spreebogen.example>','LAGetSi Strahlenschutz <strahlenschutz@lagetsi-kontakt.example>', '''Sehr geehrte Damen und Herren,

zu unserer gestern übersandten Anzeige reichen wir die aktuelle Geräte- und Raumübersicht nach. Die Projektkostentabelle füge ich für die zeitliche Abstimmung bei. Der Raum trägt intern jetzt die Nummer 3 und im alten Plan die Nummer 2. Wir klären die eindeutige Bezeichnung im technischen Nachweis. Der abschließende Bericht der Sachverständigen liegt noch nicht vor.

Mit freundlichen Grüßen
Farid Benali'''),
D('09_LAGetSi_Nachforderung.docx','Nachweise zum angezeigten CT-Betrieb','25.09.2026','Landesamt für Arbeitsschutz, Gesundheitsschutz und technische Sicherheit Berlin\nFachbereich Strahlenschutz','Radiologie Spreebogen\nDr. Nela Ahrens und Dr. Farid Benali', '''Sehr geehrte Frau Dr. Ahrens, sehr geehrter Herr Dr. Benali,

Ihre Anzeige vom 21.09.2026 und die ergänzende Nachricht vom 22.09.2026 sind eingegangen. Für die weitere Bearbeitung benötigen wir eine eindeutige Zuordnung von Betreiber, Röntgeneinrichtung und geprüftem Raum. Bitte stimmen Sie die Bezeichnungen in Anzeige, Raumplan und Sachverständigenunterlagen ab. In den bislang vorliegenden Unterlagen wird sowohl Raum 2 als auch Raum 3 genannt.

Die Bescheinigung einschließlich des vollständigen Prüfberichts eines behördlich bestimmten Sachverständigen ist nachzureichen. Aus dem derzeitigen Projektvermerk ergibt sich, dass die abschließende Prüfung der Türabschirmung noch offen ist. Außerdem bitten wir um vollständige lesbare Kopien der einschlägigen Fachkunde- und Aktualisierungsnachweise und um die abschließenden Unterlagen zur Wahrnehmung der strahlenschutzrechtlichen Aufgaben bei Ihrer Gesellschaft.

Bitte erläutern Sie, ob ein teleradiologischer Betrieb beabsichtigt ist. Ihre Anzeige beschreibt ärztliche Anwesenheit vor Ort; eine beigefügte Terminnachricht erwähnt dagegen eine mögliche Abendversorgung durch einen externen Dienst. Soll diese lediglich später geprüft werden, teilen Sie dies ausdrücklich mit. Der beabsichtigte Umfang ist für die Einordnung des Verfahrens wesentlich.

Dieses Schreiben bestätigt den Eingang, nicht das Vorliegen sämtlicher Nachweise. Eine vorzeitige positive Mitteilung zur Inbetriebnahme wird hiermit nicht erteilt. Bitte reichen Sie die genannten Unterlagen gebündelt ein und nennen Sie bei weiteren Schreiben das Geschäftszeichen. Ein bereits vereinbarter Patiententermin ersetzt die erforderlichen Voraussetzungen nicht.

Im Auftrag
Alma Seifert''',reference='Str-26-CT-218'),
E('10_Teleradiologie_Anfrage.eml','Abendbefundung ab November?','2026-09-26T15:16:00+02:00','Fernblick Radiologie <koordination@fernblick.example>','Dr. Farid Benali <farid@radiologie-spreebogen.example>', '''Lieber Farid,

wir können über eine spätere Zusammenarbeit sprechen. Bislang gibt es weder eine vertragliche Zusage noch ein fertiges Versorgungskonzept für euren Standort. Bitte stellt unsere Erreichbarkeit nicht als bereits genehmigte Teleradiologie dar. Wir müssten Geräte, Personal vor Ort, Zeiten und die einschlägigen Anforderungen gemeinsam klären. Für den Oktoberstart planen wir keine Dienste ein.

Viele Grüße
Dr. Jolanda Winter'''),
E('11_Planerin_Raum.eml','Raum 2 ist jetzt intern Raum 3','2026-09-28T09:50:00+02:00','Planungsbüro Raumfaden <planung@raumfaden.example>','Malika Roth <organisation@radiologie-spreebogen.example>', '''Liebe Frau Roth,

ich bestätige: Der frühere Archivraum gegenüber dem Personalzimmer ist im Vermieterplan Raum 2. Eure interne Nummer 3 bezeichnet denselben Raum. Ich ergänze den Plan um beide Bezeichnungen und die Gerätenummer. Das ersetzt nicht die offene technische Nachprüfung der Tür. Die bauaufsichtliche Rückfrage zur geänderten Nutzung bearbeite ich ebenfalls noch; eine abschließende Rückmeldung habe ich heute nicht erhalten.

Beste Grüße
Hedi Krause'''),
D('12_Interne_MRT_Organisation.docx','MRT-Betrieb während der CT-Erweiterung','29.09.2026','Dr. Nela Ahrens','Praxisteam Radiologie Spreebogen', '''1. Bestehender Untersuchungsbereich

Der MRT-Bereich wird während der CT-Erweiterung in seiner bisherigen räumlichen und organisatorischen Form weitergeführt. Das MRT-Gerät wird nicht versetzt. Die dafür vorgesehenen Kontrollen und Wartungstermine bleiben bestehen. Der CT-Montagebereich ist vom Patientenweg durch eine geschlossene Baustellentür getrennt. Die Anmeldung informiert Patienten über mögliche kurze Wartezeiten, ohne technische Arbeiten als abgeschlossen darzustellen.

2. Zugang und Sicherheit

Die bestehenden Regeln zum kontrollierten Zugang in den MRT-Bereich gelten unverändert. Monteure dürfen diesen Bereich nicht ohne Begleitung betreten. Werkzeuge, Transportwagen und andere Gegenstände werden nicht aus dem CT-Bereich in den MRT-Raum gebracht. Vor einer Untersuchung werden die hierfür vorgesehenen Patientenabklärungen durchgeführt. Das Team verwendet die aktuellen internen Unterlagen und Herstellerhinweise; diese Notiz ersetzt keine fachliche Unterweisung.

3. Gemeinsame Bereiche

Anmeldung, Personalraum und ein Teil des Flurs werden gemeinsam genutzt. Falls die Baustelle einen Rettungsweg oder den sicheren Zugang beeinträchtigt, wird die Arbeit unterbrochen und mit der zuständigen Leitung abgestimmt. Die bloße Trennung der Geräte bedeutet nicht, dass gemeinsame organisatorische Probleme unbeachtlich wären. Hinweise auf Stolperstellen oder offene Türen sind unmittelbar an Malika zu melden.

4. Kommunikation mit Patienten

MRT-Termine werden wie bisher bestätigt, soweit die sichere Durchführung gewährleistet ist. CT-Termine bleiben zunächst Vormerkungen. Bitte sagt nicht, beide Geräte seien bereits gemeinsam freigegeben. Fragen zur späteren CT-Anwendung beantwortet Farid. Bei Unsicherheit über die tatsächliche Sicherheit eines Ablaufs wird die Untersuchung nicht aus Zeitdruck begonnen. Diese Notiz wird nach Abschluss der Montage erneut mit dem Team besprochen.'''),
D('13_Pruefbericht_Auszug.docx','Zwischenstand der Sachverständigenprüfung CT-SB-02','30.09.2026','Sachverständigenbüro Strahlklar\nDiplom-Physikerin Gesine Pohl','Radiologie Spreebogen', '''Sehr geehrte Frau Dr. Ahrens, sehr geehrter Herr Dr. Benali,

dieser Zwischenbericht fasst den Termin vom 24.09.2026 und die nachfolgende Unterlagensichtung zusammen. Geprüft wurde die für das CT-Gerät mit Seriennummer BW-CT-260914 vorgesehene Installation im ehemaligen Archivraum. Der Raum war im Ausgangsplan als Raum 2 und in der Praxisbeschriftung als Raum 3 bezeichnet. Eine eindeutige gemeinsame Bezeichnung wird in den abschließenden Bericht aufgenommen.

Die vorgelegten Planunterlagen zur Abschirmung wurden eingesehen. Für den Türbereich fehlt noch die abschließende Bestätigung der Ausführung. Eine ergänzende Messung ist vorgesehen. Solange dieser Punkt offen ist, stellen wir keine uneingeschränkte abschließende Bescheinigung über den vorgesehenen Betrieb aus. Das vorliegende Dokument ist ein Zwischenstand und darf nicht als vollständiger Abschlussbericht bezeichnet werden.

Die vom Hersteller durchzuführende technische Übergabe und Geräteeinweisung erfolgen nach dessen Mitteilung am 05.10.2026. Diese Leistungen sind von unserem Auftrag zu unterscheiden. Ebenfalls nicht Gegenstand dieses Zwischenberichts sind die gewerberechtliche Einordnung der Praxis, eine vollständige Prüfung der bauaufsichtlichen Nutzung oder eine Bewertung eines späteren teleradiologischen Betriebs. Der bislang beschriebene Zweck ist diagnostisches CT bei ärztlicher Anwesenheit vor Ort.

Wir können am 06.10.2026 einen Nachtermin anbieten, sofern die erforderlichen Unterlagen bis zum Vortag vorliegen. Bitte bestätigen Sie den Termin und nennen Sie eine anwesende verantwortliche Person. Nach Abschluss erhalten Sie eine gesonderte abschließende Dokumentation. Eine Aussage über die behördliche Verfahrensentscheidung ist damit nicht verbunden.

Mit freundlichen Grüßen
Gesine Pohl'''),
T('14_Praxischat.txt','Chat zur Terminvergabe','30.09.2026', '''30.09.2026 12:05 Malika: Darf ich den 19. Oktober schon fest bestätigen?
30.09.2026 12:08 Farid: Bitte noch nicht. Technische Übergabe ist nicht das ganze Verfahren.
30.09.2026 12:11 Nela: MRT bleibt separat geplant, solange die Wege sicher sind. Bitte nicht alle Termine absagen.
30.09.2026 12:14 Malika: Auf einer Berliner Seite stehen vier Wochen. Im Gesetz finde ich jetzt zwei. Ich lege beide Ausdrucke zur Beratung.
30.09.2026 12:18 Farid: Genau deshalb lassen wir den Ablauf prüfen. Der Türnachweis und die vollständigen Kopien fehlen ohnehin noch.
30.09.2026 12:21 Nela: Die Abendkooperation ist nur eine Idee für später. Das muss im Schreiben klar werden.'''),
E('15_Sachverstaendige_Nachtrag.eml','Zwischenbericht und Nachtermin','2026-10-01T08:54:00+02:00','Gesine Pohl <post@strahlklar.example>','Radiologie Spreebogen <organisation@radiologie-spreebogen.example>', '''Sehr geehrte Damen und Herren,

anbei erhalten Sie den Zwischenbericht vom 30. September. Der angebotene Nachtermin am 6. Oktober bleibt bis morgen reserviert. Bitte übersenden Sie zuvor die Unterlage zur Türabschirmung und den Plan mit eindeutiger Raumbezeichnung. Wir stellen die abschließende Bescheinigung erst nach Prüfung der offenen Punkte aus.

Mit freundlichen Grüßen
Gesine Pohl'''),
D('16_Verantwortungszuordnung_Entwurf.docx','Entwurf zur strahlenschutzbezogenen Organisation','01.10.2026','Dr. Nela Ahrens und Dr. Farid Benali','Interne Abstimmung, noch nicht unterzeichnet', '''1. Gegenstand des Entwurfs

Dieser Entwurf betrifft ausschließlich den geplanten diagnostischen CT-Betrieb der Berufsausübungsgemeinschaft Radiologie Spreebogen. Betreiber soll die rechtsfähige Gesellschaft bürgerlichen Rechts der beiden unterzeichnenden Gesellschafter sein. Die genaue öffentlich-rechtliche Mitteilung und die erforderlichen Bestellungen werden nach Prüfung der gesetzlichen Anforderungen gesondert fertiggestellt. Der Entwurf wird nicht als bereits wirksame Bestellung an die Behörde übermittelt.

2. Geplante Aufgabenwahrnehmung

Farid soll die strahlenschutzbezogenen Aufgaben im täglichen Betrieb koordinieren und die erforderlichen Unterlagen aktuell halten. Er soll die Befugnis erhalten, den CT-Betrieb bei fehlenden Voraussetzungen zu unterbrechen. Nela unterstützt die Personal- und Terminorganisation. Die gesellschaftsrechtlichen Entscheidungs- und Vertretungsregeln werden durch diesen Entwurf noch nicht geändert. Die verbleibende Verantwortung beider Gesellschafter ist bei der endgültigen Fassung ausdrücklich zu berücksichtigen.

3. Noch offene Punkte

Zu klären sind die genaue Abgrenzung zwischen Aufgaben des Strahlenschutzverantwortlichen und einer erforderlichen Bestellung von Strahlenschutzbeauftragten, die Vertretung im Urlaub, der räumliche und sachliche Aufgabenbereich sowie die Mitteilung an LAGetSi. Es wird keine fachliche Qualifikation einer Person angenommen, die durch die vorhandenen Bescheinigungen nicht gedeckt ist. Die vollständigen Fachkundenachweise werden der endgültigen Fassung zugrunde gelegt.

4. Weiteres Vorgehen

Nach der Beratung ergänzen die Gesellschafter die offenen Regelungen und zeichnen die erforderlichen Dokumente gemeinsam. Erst danach erhält das Praxismanagement die verbindliche Organisationsfassung. Ein teleradiologischer Abendbetrieb ist nicht Gegenstand dieses Entwurfs. Dieser wird gegebenenfalls später mit eigener Verfahrens- und Personalplanung vorbereitet.

Keine Unterschriften geleistet.'''),
E('17_Fachkundekopie_folgt.eml','Vollständige Kopie morgen','2026-10-01T19:11:00+02:00','Dr. Farid Benali <farid@radiologie-spreebogen.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

die vollständige Fachkundekopie liegt im Original in der Praxis. Ich scanne sie morgen neu. Bitte schreiben Sie nicht, dass sie Ihrer heutigen Nachricht bereits beigefügt wäre. Der Zwischenbericht der Sachverständigen ist tatsächlich noch kein Abschluss. Für die Teleradiologie haben wir keinerlei feste Zusage abgegeben.

Mit freundlichen Grüßen
Farid Benali'''),
E('18_Planung_bleibt_vorlaeufig.eml','Terminplan und Patienteninformation','2026-10-02T09:03:00+02:00','Malika Roth <organisation@radiologie-spreebogen.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

wir haben zwölf CT-Termine für die Woche ab 19. Oktober nur vorgemerkt. Die Patienten wissen, dass eine Bestätigung folgt. Die Kostenübersicht enthält bereits bezahlte Abschläge, aber keine behördliche Freigabe. Bitte geben Sie uns nach Ihrer Prüfung einen Plan, welche Unterlage welchen Schritt auslöst. Das wäre für die Organisation hilfreicher als ein pauschales Ja oder Nein zur ganzen Praxis.

Freundliche Grüße
Malika Roth''')]))
