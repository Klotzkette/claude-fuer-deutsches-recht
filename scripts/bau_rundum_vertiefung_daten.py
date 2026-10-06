"""Eigenständige Eingangsunterlagen zu den fünf Abläufen aus Seminar-Insert 2."""

CASES = {}


def case(slug, title, project, description, checks):
    value = dict(slug=slug, title=title, project=project, description=description,
                 checks=checks, pieces=[])
    CASES[slug] = value
    return value


def doc(c, file, title, date, sender, recipient, ref, signer, sections, table=None):
    c['pieces'].append(dict(file=file, title=title, date=date, sender=sender,
                            recipient=recipient, ref=ref, signer=signer,
                            sections=sections, table=table))


def csv(c, file, title, date, owner, headers, rows):
    c['pieces'].append(dict(file=file, title=title, date=date, owner=owner,
                            headers=headers, rows=rows))


def mail(c, file, title, date, sender, recipient, body, attachments=()):
    c['pieces'].append(dict(file=file, title=title, date=date, sender=sender,
                            recipient=recipient, body=body, attachments=attachments))


def book(c, file, title, date, owner, sheets):
    c['pieces'].append(dict(file=file, title=title, date=date, owner=owner, sheets=sheets))


def txt(c, file, title, date, text):
    c['pieces'].append(dict(file=file, title=title, date=date, text=text))


def eur(value):
    return f'{value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


L = case('bau-rundum-abschlagsrechnung-lemgo',
         'Dritte Abschlagsrechnung für das Quartiershaus Brake in Lemgo',
         'Quartiershaus Brake, Umbau Werkflügel, Lemgo',
         'Kumulative Rohbaurechnung mit fortgeschriebenen Mengen, zwei unterschiedlich behandelten Nachträgen, Teilzahlungen und einer noch nicht erledigten Beanstandung.',
         ['Kumulative Leistungen, frühere Rechnungen und tatsächlich geleistete Zahlungen getrennt abgleichen.',
          'Aufmaß, Liefernachweis, Preisvereinbarung und Anordnung für jede Abweichung anhand ihrer Herkunft unterscheiden.',
          'Einbehalte und Sicherungsklausel prüfen, ohne aus einer Buchung ein Anerkenntnis abzuleiten.'])
LS = 'Weserbogen Bau GmbH\nKlinkerweg 14, 32657 Lemgo\nrechnung@weserbogen-bau.example'
LA = 'Quartiershaus Brake gGmbH\nLindenkai 8, 32657 Lemgo\nprojekt@quartiershaus-brake.example'
LP = 'Raumfuge Architektur PartG\nSiebenhöfer Weg 22, 32657 Lemgo\npost@raumfuge.example'

doc(L, '01_Bauauftrag.docx', 'Bauauftrag Rohbau Werkflügel', '2026-04-17', LA, LS, 'QB-26 / R01',
    'gez. Dr. Anne Rößler, Geschäftsführerin\ngez. Jörg Hagemann, Geschäftsführer', [
    ('1 Leistungsumfang', 'Wir beauftragen die Rohbauarbeiten am Werkflügel des Quartiershauses Brake gemäß dem Leistungsverzeichnis R01 vom 10.04.2026. Die acht Positionen ergeben 146.700,00 EUR netto. Umsatzsteuer wird mit 19 Prozent gesondert berechnet. Die Ausführung erfolgt vom 04.05. bis 31.08.2026. Die Bestandsfundamente bleiben erhalten; zusätzliche Unterfangungen sind nicht im Preis enthalten.'),
    ('2 Abrechnung', 'Abschlagsrechnungen sind zum Monatsende kumulativ nach nachgewiesener Leistung einzureichen. Frühere Rechnungen und eingegangene Zahlungen sind gesondert auszuweisen. Für die Mengenprüfung ist Raumfuge Architektur zuständig. Dessen Aufmaßunterschrift bestätigt die gemeinsam festgestellten Maße, nicht die Beauftragung zusätzlicher Leistungen. Zahlung erfolgt binnen 21 Kalendertagen nach Zugang einer prüfbaren Rechnung.'),
    ('3 Sicherung und Änderungen', 'Als Vertragserfüllungssicherheit werden fünf Prozent des jeweiligen kumulativen Bruttowerts einbehalten, höchstens fünf Prozent der Bruttoauftragssumme einschließlich vereinbarter Änderungen. Eine Ablösung durch die im Vertrag bezeichnete unbefristete Bürgschaft ist möglich. Mängelbezogene Zurückbehaltungen werden getrennt mitgeteilt. Änderungen mit Preiswirkung beauftragt ausschließlich die Geschäftsführerin in Textform. VOB/B in der bei Vertragsschluss ausgehändigten Fassung ist vereinbart; die individuelle Sicherungsabrede ist davon getrennt dokumentiert.')])

LV_L = [
    ['01.010', 'Baustelleneinrichtung', 'psch', 1, 12500],
    ['02.010', 'Bodenplatte Beton', 'm³', 120, 185],
    ['02.020', 'Bewehrung', 't', 18, 1450],
    ['03.010', 'Mauerwerk', 'm²', 420, 92],
    ['03.020', 'Wandschalung', 'm²', 260, 42],
    ['04.010', 'Deckenbeton', 'm³', 85, 198],
    ['04.020', 'Abdichtung Sockel', 'm²', 150, 37],
    ['05.010', 'Stahlstützen montiert', 'St', 8, 1745],
]
doc(L, '02_Leistungsverzeichnis.pdf', 'Leistungsverzeichnis R01', '2026-04-10', LP, LA, 'QB-26 / LV R01',
    'gez. Dipl.-Ing. Kirsten Seidel, Projektleitung', [
    ('1 Abrechnungsgrenzen', 'Das Preisblatt gilt für den Werkflügel zwischen Achsen 1 bis 6. Bewehrung wird nach freigegebener Stahlliste und nachgewiesenem Einbau abgerechnet. Anlieferungen allein bilden keine Einbaumenge. Mauerwerksöffnungen werden entsprechend der vertraglich vereinbarten Aufmaßregel abgezogen. Die hier aufgeführten Mengen dienen der Beauftragung; abgerechnet werden die ausgeführten Mengen.'),
    ('2 Leistungsinhalt', 'Der Einheitspreis der Stahlstützen umfasst Lieferung, Montage, Verguss und die Anschlussplatten. Nur angelieferte, im Lager verbliebene Stützen werden nicht als montierte Stützen angesetzt. Die Baustelleneinrichtung wird bei vollständiger Einrichtung mit der ersten Abschlagsrechnung angesetzt; sie wird in späteren kumulativen Aufstellungen unverändert fortgeführt. Sockelabdichtung enthält Untergrundvorbereitung und Schutzlage.')],
    (['Pos.', 'Leistung', 'Einheit', 'Menge', 'EP netto EUR'], LV_L))

csv(L, '03_Aufmass_Vormonate.csv', 'Aufmaßstände Mai und Juni', '2026-06-30', 'Kirsten Seidel / Leon Brandt',
    ['Pos', 'Einheit', 'Mai_kumulativ', 'Juni_kumulativ', 'Aufmaßblatt', 'Unterzeichner'],
    [[r[0], r[2], a, b, 'AM-05/AM-06', 'Seidel; Brandt'] for r, a, b in zip(LV_L,
     [1, 40, 6, 90, 60, 0, 0, 0], [1, 90, 13, 240, 160, 35, 50, 4])])

doc(L, '04_Abschlagsrechnung_1.pdf', 'Erste Abschlagsrechnung', '2026-05-31', LS, LA, 'Rechnung WB-26051 / QB-26',
    'gez. Maren Beck, Rechnungswesen', [
    ('1 Leistungszeitraum', 'Wir berechnen die bis 29.05.2026 ausgeführten Leistungen. Die Einrichtung wurde am 06.05. vollständig übernommen. Die Mengen entsprechen Aufmaß AM-05. Die Rechnung ist kumulativ; vorausgegangene Abschläge bestehen nicht.'),
    ('2 Zahlungsanforderung', 'Die Leistungssumme beträgt 39.400,00 EUR netto und 7.486,00 EUR Umsatzsteuer, zusammen 46.886,00 EUR. Nach fünf Prozent Sicherungseinbehalt von 2.344,30 EUR fordern wir 44.541,70 EUR an. Bitte verwenden Sie das in Ihrem Lieferantenstamm freigegebene Zahlkonto und den Verwendungszweck WB-26051.')],
    (['Pos.', 'Menge', 'EP netto EUR', 'Betrag netto EUR'], [[r[0], q, r[4], round(q*r[4], 2)] for r,q in zip(LV_L,[1,40,6,90,60,0,0,0])]))

doc(L, '05_Abschlagsrechnung_2.pdf', 'Zweite Abschlagsrechnung', '2026-06-30', LS, LA, 'Rechnung WB-26079 / QB-26',
    'gez. Maren Beck, Rechnungswesen', [
    ('1 Fortschreibung', 'Abgerechnet werden die Leistungen bis 30.06.2026 auf Grundlage des Aufmaßes AM-06. Die Werte der ersten Rechnung sind in den folgenden Mengen enthalten. Nachtrag N01 ist ausgeführt, wird aber erst im Juli gemeinsam mit der abschließenden Aufmaßergänzung fakturiert.'),
    ('2 Zahlungsanforderung', 'Die kumulative Nettosumme beträgt 92.560,00 EUR, die Umsatzsteuer 17.586,40 EUR und der Bruttowert 110.146,40 EUR. Der kumulative Sicherungseinbehalt beträgt 5.507,32 EUR. Von 104.639,08 EUR verbleiben nach dem am 22.06. verbuchten ersten Zahlungseingang von 44.541,70 EUR noch 60.097,38 EUR. Weitere Zahlungseingänge sind bis zum Ausstellungsdatum nicht verbucht.')],
    (['Pos.', 'Menge', 'EP netto EUR', 'Betrag netto EUR'], [[r[0], q, r[4], round(q*r[4], 2)] for r,q in zip(LV_L,[1,90,13,240,160,35,50,4])]))

csv(L, '06_Kreditorenbewegungen.csv', 'Kreditorenkonto Weserbogen', '2026-08-04', 'Quartiershaus Brake / Denise Jung',
    ['Buchung', 'Datum', 'Beleg', 'Art', 'Betrag_EUR', 'Zahlungsreferenz'], [
    ['K1001','2026-06-02','WB-26051','Rechnung_brutto',46886,''],
    ['K1034','2026-06-22','WB-26051','Auszahlung',44541.70,'Z260622-11'],
    ['K1077','2026-07-02','WB-26079','Zuwachs_brutto',63260.40,''],
    ['K1091','2026-07-21','WB-26079','Auszahlung',48097.38,'Z260721-08'],
    ['K1103','2026-07-29','WB-26079','Auszahlung',8000,'Z260729-03'],
    ['K1104','2026-07-29','WB-26079','Noch_nicht_ausgezahlt',4000,'Beanstandung Sockel'],
    ])

doc(L, '07_Nachtrag_N01.docx', 'Vereinbarung Nachtrag N01', '2026-06-12', LA, LS, 'QB-26 / N01',
    'gez. Dr. Anne Rößler\ngez. Jörg Hagemann', [
    ('1 Unterfangung Achse 2', 'Aufgrund der am 08.06. geöffneten Fundamenttasche wird eine zusätzliche Unterfangung aus Beton auf 18,00 m Länge beauftragt. Vereinbart werden 210,00 EUR netto je laufendem Meter einschließlich abschnittsweisen Aushubs, Schalung und Rückverfüllung. Die Gesamtsumme bei dieser Menge beträgt 3.780,00 EUR netto. Mehrmengen bedürfen eines ergänzenden gemeinsamen Aufmaßes.'),
    ('2 Ausführung und Nachweise', 'Die Arbeit erfolgt zwischen 15. und 18.06.2026 nach Skizze U-02. Das gemeinsame Aufmaß U-02 vom 18.06. weist 18,00 m aus. Brandt und Seidel haben es mit diesem Ergebnis unterzeichnet; ein Vorbehalt zur Länge besteht nicht. Ein gesonderter Stillstand wird mit dieser Preisvereinbarung weder beauftragt noch abgegolten. Die übrigen Vertragsbedingungen bleiben bestehen.'),
    ('3 Abrechnung', 'Die Leistung ist als eigene Position N01.010 in der kumulativen Rechnung zu führen. Die ursprüngliche Bodenplattenmenge wird hierdurch nicht verändert. Die Geschäftsführerin bestätigt diese Vereinbarung für die Auftraggeberin; die technische Projektleitung erhält eine Ausfertigung.')])

doc(L, '08_Nachtragsangebot_N02.pdf', 'Angebot N02 für Pumpenhaltung', '2026-07-08', LS, LA, 'Angebot WB-N02',
    'gez. Leon Brandt, Bauleiter', [
    ('1 Anlass', 'Am 06.07. trat im südlichen Arbeitsraum Wasser aus der geöffneten Bestandsleitung ein. Herr Brandt verständigte Frau Seidel um 09:20 Uhr. Nach seiner Erinnerung verlangte sie, den Arbeitsraum bis zur Freilegung trocken zu halten. Wir haben am selben Tag eine Tauchpumpe eingesetzt. Eine unterschriebene Preisvereinbarung liegt unserem Bauleiter bislang nicht vor.'),
    ('2 Preisangebot', 'Wir bieten zwölf Pumpentage vom 06. bis einschließlich 17.07. zu 340,00 EUR netto je Kalendertag an, zusammen 4.080,00 EUR netto. Der Tagespreis enthält Gerät, Strom, Kontrolle und die zweimalige Umsetzung. Wir behandeln die Leistung als zusätzliche Wasserhaltung und bitten um Bestätigung bis 10.07.2026. Die Pumpen wurden am 18.07. abgeholt.'),
    ('3 Abgrenzung', 'Die Auftraggeberin hatte am 07.07. gefragt, ob die Baustelleneinrichtung bereits eine einfache Wasserhaltung umfasst. Wir halten den Einsatz wegen der geöffneten Bestandsleitung für darüber hinausgehend. Mit diesem Angebot wird unsere Preisforderung mitgeteilt; die von uns erbetene Beauftragung ist nicht beigefügt.')])

doc(L, '09_Aufmass_Juli.docx', 'Gemeinsames Aufmaß AM07', '2026-07-31', LP, LS, 'QB-26 / AM-07',
    'gez. Kirsten Seidel, Objektüberwachung\ngez. Leon Brandt, Bauleitung mit Vorbehalt zu 03.010', [
    ('1 Aufnahmetermin', 'Am 31.07.2026 wurden zwischen 07:30 und 10:10 Uhr die ausgeführten Bauteile im Werkflügel aufgenommen. Die Werte sind kumulativ einschließlich Juni. Für die Bewehrung lag Stahlliste S-06 mit 17,40 t eingebauter Masse vor. 0,80 t verblieben nach Wiegen im verschlossenen Lager. Der Lieferschein allein wurde nicht als Einbaunachweis unterzeichnet.'),
    ('2 Mauerwerk und Stützen', 'Die Bruttofläche des Mauerwerks beträgt 402,00 m². Für die drei Öffnungen an Achse 5 wurden 9,60 m² abgezogen, so dass Frau Seidel 392,40 m² festhält. Herr Brandt unterschreibt nur die Maße und hält an 402,00 m² für seine Abrechnung fest. Sechs Stahlstützen sind einschließlich Verguss eingebaut. Zwei liegen auf Paletten; deren Anschlussplatten fehlen noch.'),
    ('3 Pumpen und Nebenarbeiten', 'N01 ist mit 18,00 m erledigt. Zur Pumpe wurde kein gemeinsames Tagesprotokoll geführt. Im Bautagebuch sind Betriebskontrollen an den neun Arbeitstagen zwischen 06. und 16.07. vermerkt; am 17.07. fehlt ein Eintrag. Hier wird weder ein Pumpenpreis noch eine Anordnungsbefugnis bestätigt.')],
    (['Pos.', 'Einheit', 'Festgehaltene Menge'], [[r[0],r[2],q] for r,q in zip(LV_L,[1,118.5,17.4,392.4,248,82,142,6])]))

csv(L, '10_Wareneingang_Juli.csv', 'Wareneingang Werkflügel', '2026-07-30', 'Weserbogen / Lagerführer Niklas Arndt',
    ['Datum','Lieferschein','Material','Menge','Einheit','Verbleib'], [
    ['2026-07-02','S-719','Bewehrung',4.4,'t','eingebaut; S-06'],
    ['2026-07-14','S-754','Bewehrung',0.8,'t','Lager Werkflügel'],
    ['2026-07-20','ST-280','Stahlstütze',2,'St','montiert'],
    ['2026-07-28','ST-291','Stahlstütze',2,'St','Paletten ohne Anschlussplatten'],
    ['2026-07-30','AB-162','Abdichtungsbahn',150,'m²','142 m² verarbeitet; 8 m² Rest'],
    ])

book(L, '11_Abschlagsrechnung_3.xlsx', 'Dritte Abschlagsrechnung WB26098', '2026-08-03',
     'Weserbogen Bau GmbH / Maren Beck', [dict(name='WB26098',
       headers=['Position','Leistung','Einheit','Menge kum.','EP netto EUR','Betrag netto EUR'],
       rows=[[r[0],r[1],r[2],q,r[4],f'=ROUND(D{i}*E{i},2)'] for i,(r,q) in enumerate(zip(LV_L,[1,118.5,18.2,402,248,82,142,8]),6)] +
            [['N01.010','Unterfangung','m',18,210,'=ROUND(D14*E14,2)'],['N02.010','Pumpenhaltung','Tag',12,340,'=ROUND(D15*E15,2)']],
       tail=[['Kumulativ netto','','','','','=SUM(F6:F15)'],['Umsatzsteuer',0.19,'','','','=ROUND(F16*B17,2)'],
             ['Kumulativ brutto','','','','','=F16+F17'],['Sicherung',0.05,'','','','=ROUND(F18*B19,2)'],
             ['Zahlung 22.06.',44541.70],['Zahlungen Juli',56097.38],
             ['Anforderung brutto','','','','','=F18-F19-B20-B21']],
       notes=['Leistungsstand 31.07.2026. Forderungsaufstellung des Auftragnehmers.',
              'Fünf Prozent Sicherung. Mängelbedingte Rückbehalte sind hier nicht nochmals abgezogen.',
              'gez. Maren Beck, Rechnungswesen; 03.08.2026. Vertrag QB-26/R01.'],
       controls={'F16':151522.5,'F18':180311.78,'F22':70657.11},
       mutation={'cell':'D13','value':6,'result':'F16','expected':148032.5})])

mail(L, '12_Rechnungseingang.eml', 'QB-26: dritte Abschlagsrechnung WB-26098', '2026-08-03T09:14:00+02:00',
     'Maren Beck <rechnung@weserbogen-bau.example>', 'Kirsten Seidel <post@raumfuge.example>',
     'Sehr geehrte Frau Seidel,\n\nanbei erhalten Sie unsere dritte kumulative Abschlagsrechnung sowie das gemeinsame Aufmaß AM-07. Bitte leiten Sie den freigegebenen Stand an Frau Rößler weiter. Die offenen 4.000,00 EUR aus der zweiten Rechnung sind im Abzug der tatsächlich erhaltenen Zahlungen berücksichtigt; wir stellen hierfür keine vierte Leistung in Rechnung.\n\nDie zusätzlich gelieferten Stützen haben wir vollständig aufgenommen, weil sie nach unserer Auffassung bereits dem Projekt zugeordnet sind. Beim Mauerwerk bleiben wir bei der Bruttofläche. Für die Pumpenhaltung liegt Ihnen unser Angebot vom 08.07. vor. Bitte teilen Sie uns etwaige Kürzungen positionsbezogen mit. Wir bitten um Auszahlung des angeforderten Betrags bis 24.08.2026.\n\nMit freundlichen Grüßen\nMaren Beck\nWeserbogen Bau GmbH',
     ['11_Abschlagsrechnung_3.xlsx','09_Aufmass_Juli.docx'])

doc(L, '13_Sockelkontrolle.pdf', 'Kontrolle der Sockelabdichtung', '2026-07-17', LP, LA, 'QB-26 / Begehung 17.07.',
    'gez. Kirsten Seidel, Objektüberwachung', [
    ('1 Feststellungen', 'An der westlichen Türschwelle wurden auf rund 2,40 m Länge offene Überlappungen festgestellt. Bei der Sichtkontrolle um 13:15 Uhr ließen sich zwei Bahnenränder von Hand anheben. Herr Brandt war anwesend und sagte eine Nacharbeit bis 24.07. zu. Eine Prüfung verdeckter Bereiche fand nicht statt. Von den sonstigen 142,00 m² wurde keine flächenhafte Ablösung festgestellt.'),
    ('2 Nächster Baustellentermin', 'Vor Verfüllung ist der betreffende Bereich erneut zu zeigen. Frau Seidel schätzt den unmittelbar sichtbaren Nacharbeitsumfang nach Gespräch mit dem Polier vorläufig auf rund 2.000,00 EUR brutto. Ein bepreistes Angebot eines Dritten liegt nicht vor. Der Betrag ist eine Baustelleneinschätzung und keine Rechnung. Die Maßnahme soll nicht durch eine pauschale Veränderung sämtlicher Abdichtungsmengen ersetzt werden.'),
    ('3 Rückmeldung', 'Bis zur Abfassung dieses Berichts ist eine Erledigungsanzeige nicht eingegangen. Frau Jung erhält eine Kopie für den Zahlungslauf. Die Behauptung des Auftragnehmers, die Bahnen seien mittlerweile nachgeklebt, wurde bei diesem Termin nicht überprüft.')])

doc(L, '14_Zahlungsmitteilung.docx', 'Mitteilung zum zweiten Abschlag', '2026-07-20', LA, LS, 'QB-26 / WB-26079',
    'gez. Dr. Anne Rößler, Geschäftsführerin', [
    ('1 Zahlungslauf', 'Von Ihrer Anforderung aus WB-26079 über 60.097,38 EUR werden zunächst 48.097,38 EUR angewiesen. Weitere 8.000,00 EUR folgen voraussichtlich am 29.07.; dies beruht auf unserem internen Zahlungslimit und nicht auf einer weiteren Beanstandung. Der Sicherungseinbehalt aus der Rechnung ist hiervon unabhängig.'),
    ('2 Sockelabdichtung', 'Wegen der offenen Bahnenränder behalten wir darüber hinaus vorerst 4.000,00 EUR ein. Wir stützen uns auf den Baustellenbericht vom 17.07. und die dort genannte Kostenschätzung. Bitte zeigen Sie die Nacharbeit vor dem Verfüllen an. Sobald der Bereich kontrolliert ist, entscheiden wir über die Auszahlung; eine Reduzierung der Vertragssicherheit ist damit nicht erklärt.'),
    ('3 Bürgschaft', 'Ihre Nachfrage nach Ablösung der Sicherheit haben wir erhalten. Eine Bürgschaft ist bislang nicht übergeben worden. Die Aufmaßbestätigung der Objektüberwachung ersetzt weder unsere Prüfung einer Bürgschaft noch eine Bestätigung des Nachtrags N02.')])

mail(L, '15_Buchhaltung_Rueckfrage.eml', 'WB-26098: Abzug der Zahlungen und Sockelbereich', '2026-08-04T11:26:00+02:00',
     'Denise Jung <buchhaltung@quartiershaus-brake.example>', 'Kirsten Seidel <post@raumfuge.example>',
     'Sehr geehrte Frau Seidel,\n\nauf dem Kreditorenkonto stehen tatsächlich drei Auszahlungen über zusammen 100.639,08 EUR. Die Überweisung vom 29.07. wurde nicht zurückgebucht. Aus der zweiten Anforderung sind 4.000,00 EUR weiterhin nicht bezahlt. Bitte bestätigen Sie uns nicht nochmals 60.097,38 EUR als Zahlung, nur weil dieser Betrag auf der Rechnung steht.\n\nHerr Brandt rief heute an und sagte, die Sockelecke sei fertig. Eine Kontrolle oder Freigabe habe ich nicht gesehen. Frau Rößler ist am 06.08. wieder im Haus. Bis dahin soll der dritte Abschlag nicht ungeprüft in den Zahlungslauf gehen. Eine Bürgschaft befindet sich auch heute nicht im Originalposteingang. Anbei der unveränderte Kontenauszug aus unserem Nebenbuch.\n\nMit freundlichen Grüßen\nDenise Jung\nBuchhaltung', ['06_Kreditorenbewegungen.csv'])

H = case('bau-rundum-vgv-bewerbung-hameln',
         'Planungsbewerbung für das Lernhaus Am Werder in Hameln',
         'Lernhaus Am Werder, Umbau einer Berufsschule, Hameln',
         'VgV-Teilnahmeantrag eines Planungsbüros mit veröffentlichten Auswahlkriterien, belastbaren Referenzbelegen, Kapazitätskonflikten und einem vorläufigen Konzept für die spätere Angebotsphase.',
         ['Mindestanforderungen, Bewerberauswahl und spätere Zuschlagskriterien auseinanderhalten.',
          'Referenzen nach Zeitraum, eigenem Leistungsanteil und tatsächlich dokumentierter Leistung auswählen.',
          'Teamkapazität und Fremdleistungen belegen; fehlende Zusagen nicht durch Konzeptbehauptungen ersetzen.'])
HS = 'Schulbauverband Weserraum\nWerderbogen 31, 31785 Hameln\nvergabe@schulbau-weserraum.example'
HP = 'Faltwerk Architektur PartG\nHafenwinkel 12, 31785 Hameln\nbewerbung@faltwerk.example'

doc(H, '01_Bekanntmachungsdaten.pdf', 'Teilnahmewettbewerb Lernhaus Am Werder', '2026-09-07', HS,
    'Interessierte Planungsbüros', 'Vergabe SW-2026-18 / Datenstand 1', 'gez. Eva Brüning, Vergabestelle', [
    ('1 Gegenstand und Verfahren', 'Der Schulbauverband Weserraum beabsichtigt die stufenweise Beauftragung der Objektplanung Gebäude für den Umbau der Berufsschule zum Lernhaus Am Werder. Vorgesehen sind die Leistungsphasen 2 bis 8; zunächst werden die Phasen 2 bis 4 beauftragt. Die erwartete Gesamtvergütung einschließlich Optionen beträgt 620.000 EUR netto. Das Verfahren wird als Verhandlungsverfahren mit Teilnahmewettbewerb nach VgV geführt. Eine Garantie für den Abruf weiterer Stufen besteht nicht.'),
    ('2 Teilnahme und Auswahl', 'Teilnahmeanträge sind bis 09.10.2026, 12:00 Uhr, ausschließlich über das Verfahrenspostfach der Plattform einzureichen. Eine Übersendung an unsere allgemeine E-Mail-Adresse genügt nicht. Bei ausreichender Zahl geeigneter Bewerber werden drei Büros zur Angebotsabgabe eingeladen. Die Auswahl richtet sich nach der beigefügten Kriterienfassung vom selben Tag. Bei Punktgleichheit am dritten Platz entscheidet das Los unter den gleich platzierten geeigneten Bewerbern.'),
    ('3 Nachweise', 'Benötigt werden die Berufszulassung der verantwortlichen Person, die Erklärung über Ausschlussgründe, die Versicherungserklärung, zwei Referenzblätter und Angaben zum vorgesehenen Team. Konzepte und Honorarangebote werden im Teilnahmeantrag nicht verlangt. Rückfragen sind bis 30.09.2026 über das Verfahrenspostfach zu stellen. Der Informationsstand und die Antworten werden allen registrierten Interessenten identisch zugänglich gemacht.')])

doc(H, '02_Auswahl_und_Zuschlagskriterien.pdf', 'Kriterien für Teilnahme und spätere Angebote', '2026-09-07', HS,
    'Interessierte Planungsbüros', 'SW-2026-18 / Anlage K1', 'gez. Eva Brüning, Vergabestelle', [
    ('1 Mindestanforderungen', 'Die verantwortliche Person muss zur Führung der Berufsbezeichnung Architektin oder Architekt berechtigt sein. Verlangt wird eine Berufshaftpflicht mit 3 Mio. EUR für Personenschäden und 2 Mio. EUR für sonstige Schäden, mindestens zweifach maximiert, oder eine verbindliche Erklärung des Versicherers über die entsprechende Erhöhung im Auftragsfall. Mindestens eine Büroreferenz muss die Phasen 3 bis 8 enthalten, deren Phase 8 zwischen 01.01.2021 und dem Bewerbungsschluss abgeschlossen wurde, bei Baukosten der Kostengruppen 300 und 400 von mindestens 3 Mio. EUR netto. Ältere Referenzen werden für diese Mindestanforderung nicht zugelassen.'),
    ('2 Begrenzung auf drei Büros', 'Gewertet werden genau zwei benannte Büroreferenzen aus dem genannten Zeitraum. Je Referenz werden 10 Punkte für vollständig selbst erbrachte Phasen 3 bis 8, 8 Punkte für Umbau unter fortgesetzter Nutzung, 6 Punkte für Bildungsnutzung und 6 Punkte für mindestens 5 Mio. EUR netto Baukosten vergeben. Teilpunkte sind nicht vorgesehen. Zusätzlich werden 20 Punkte für mindestens acht Jahre Berufserfahrung der benannten Projektleitung und 20 Punkte für mindestens fünf Jahre Berufserfahrung der Stellvertretung vergeben. Maximal sind 100 Punkte erreichbar. Selbst erbrachte Anteile sind bei Arbeitsgemeinschaften getrennt auszuweisen.'),
    ('3 Angebotsphase', 'Erst nach Einladung werden folgende Zuschlagskriterien angewandt: Projektorganisation 30 Prozent, Umbaukonzept im laufenden Schulbetrieb 25 Prozent, Kosten- und Terminsteuerung 20 Prozent, Honorar 25 Prozent. Die ersten drei Kriterien werden jeweils auf einer Skala von 0 bis 5 anhand der auftragsbezogenen Schlüssigkeit bewertet. Die eingeladenen Büros erhalten die vollständige Bewertungsbeschreibung und Preisformel mit der Angebotsaufforderung. Diese späteren Kriterien werden nicht zur Rangfolge im Teilnahmewettbewerb verwendet.')])

doc(H, '03_Projektbeschreibung.docx', 'Aufgabenstellung Lernhaus Am Werder', '2026-09-07', HS, 'Bewerberkreis SW-2026-18',
    'SW-2026-18 / Anlage P1', 'gez. Daniel Wöhler, Projektverantwortlicher', [
    ('1 Bestand und Nutzung', 'Der zweigeschossige Schulbau von 1978 soll ein Lernhaus mit Metallwerkstatt, Bibliothek und offenen Lernbereichen aufnehmen. Die Bruttogrundfläche beträgt 3.850 m². Der westliche Unterrichtsflügel bleibt mit rund 180 Lernenden in Betrieb. Im Sommer 2027 stehen sechs zusammenhängende Wochen ohne regulären Unterricht zur Verfügung. Die Werkstatt muss nach den Ferien wieder erreichbar sein.'),
    ('2 Planungsaufgabe', 'Die Kostenvorgabe für die Kostengruppen 300 und 400 beträgt 5,8 Mio. EUR netto zum Stand August 2026. Rückbau, Brandschutz und gebäudetechnische Erneuerung sind mit der Tragwerks- und Fachplanung abzustimmen. Eine Schadstofferkundung wurde separat bestellt; deren Ergebnis liegt noch nicht vor. Der Auftrag umfasst keine Garantie, dass vorhandene Leitungswege unverändert nutzbar sind.'),
    ('3 Organisation', 'Für Januar bis März 2027 erwartet der Verband regelmäßige Planungsabstimmungen mit Nutzern. Die Projektleitung soll persönlich erreichbar sein und eine belastbare Vertretung benennen. Eine täglich anwesende Projektleitung wird nicht verlangt. Der Verband möchte Bauabschnitte mit getrennten Fluchtwegen und eine nachvollziehbare Freigabeorganisation. Konkrete Abschnittspläne sind erst nach Beauftragung zu entwickeln.')])

REFS_H = [
 ['FW-19','Campus Hofgarten','Bildung','2024-08-30',6.2,'3-8','vollständig','ja','05_Referenz_Hofgarten.pdf'],
 ['FW-22','Stadtteilhaus Südbogen','Bildung und Beratung','2025-11-14',4.4,'5-8','ARGE Anteil 40 Prozent','ja','06_Referenz_Suedbogen.pdf'],
 ['FW-11','Lernzentrum Nordtor','Bildung','2020-12-18',5.9,'3-8','vollständig','ja','Archivkarte N11'],
 ['FW-28','Schule Riedhof','Bildung','2027-06-30',7.1,'3-8 geplant','Phase 5 läuft','nein','Auftragsstand 30.09.'],
 ['FW-16','Verwaltungsbau Lindenhof','Verwaltung','2023-03-03',5.2,'3-8','vollständig','nein','Archivkarte V16'],
 ['FW-07','Sporthalle Wiesenrain','Sport','2022-07-22',3.6,'3-8','Lena Kruse beim Vorbüro','nein','07_Kruse_Referenzzuordnung.eml'],
]
csv(H, '04_Referenzarchiv.csv', 'Referenzarchiv Stand September', '2026-09-30', 'Faltwerk / Archiv Anna Finke',
    ['Kennung','Projekt','Nutzung','Abschluss_Phase8','KG300400_Mio_EUR_netto','Phasen','Leistungsanteil','Betrieb_fortgesetzt','Beleg'], REFS_H)

doc(H, '05_Referenz_Hofgarten.pdf', 'Bestätigung Campus Hofgarten', '2024-09-12',
    'Bildungswerk Hofgarten gGmbH\nAhornhof 6, 32756 Detmold\nbau@hofgarten-bildung.example', HP,
    'HG-19 / Schlussdokumentation', 'gez. Petra Kroll, Bauherrenvertretung', [
    ('1 Auftrag', 'Faltwerk Architektur hat den Campus Hofgarten mit 4.100 m² Bruttogrundfläche umgebaut. Das Büro erbrachte die Objektplanung der Phasen 3 bis 8 eigenständig. Die Phasen 1 und 2 waren zuvor durch ein anderes Büro bearbeitet worden. Projektleiterin bei Faltwerk war Lena Kruse; die örtliche Überwachung lag bei Mehmet Aydin.'),
    ('2 Durchführung', 'Die Unterrichtsnutzung in zwei Bauabschnitten lief während der Arbeiten weiter. Im laufenden Schulbetrieb mussten Lieferwege täglich mit der Schulleitung abgestimmt werden. Die von uns festgestellten Kosten der Kostengruppen 300 und 400 betragen 6.200.000 EUR netto. Die wesentlichen Leistungen der Phase 8 einschließlich Kostenfeststellung wurden am 30.08.2024 abgeschlossen.'),
    ('3 Bestätigung', 'Wir bestätigen die genannten Leistungsanteile und den Zeitraum. Gewährleistungsbegehungen waren gesondert vereinbart und sind mit diesem Datum nicht beendet. Für Rückfragen steht unsere Projektverwaltung unter der im Briefkopf angegebenen Anschrift zur Verfügung. Diese Bestätigung trifft keine Aussage über verfügbare Kapazitäten des Büros für künftige Projekte.')])

doc(H, '06_Referenz_Suedbogen.pdf', 'Bestätigung Stadtteilhaus Südbogen', '2025-12-03',
    'Südbogen Bildungsstiftung\nSchulring 17, 31832 Springe\nverwaltung@suedbogen.example', HP,
    'SB-22 / ARGE Faltwerk und Baukontur', 'gez. Helga Neumann, Vorstand', [
    ('1 Vertrag und Anteil', 'Die Arbeitsgemeinschaft Faltwerk und Baukontur betreute den Umbau des Stadtteilhauses Südbogen. Faltwerk übernahm die Ausführungsplanung, die Vorbereitung der Vergabe und die Objektüberwachung für den Innenausbau. Die Entwurfs- und Genehmigungsplanung der Phasen 3 und 4 wurde von Baukontur verantwortet. Der honorarbezogene Anteil von Faltwerk an der Arbeitsgemeinschaft betrug 40 Prozent.'),
    ('2 Projektwerte', 'Im Haus wurden Volkshochschulräume und eine Beratungsstelle betrieben. Die Nutzung wurde abschnittsweise aufrechterhalten. Die Baukosten der Kostengruppen 300 und 400 betrugen insgesamt 4.400.000 EUR netto. Der von Faltwerk betreute Innenausbau ist darin enthalten, aber nicht gesondert als eigenständiges Gesamtobjekt abgerechnet. Die Phase 8 der Arbeitsgemeinschaft endete am 14.11.2025.'),
    ('3 Ansprechpartner', 'Für die planerische Koordination stand uns beim Büro Faltwerk Mehmet Aydin zur Verfügung. Die Bestätigung bezieht sich auf die tatsächlich ausgeführten Leistungen und macht aus dem ARGE-Anteil keinen alleinigen Gesamtauftrag. Wir bitten, diese Abgrenzung bei weiteren Referenzabfragen beizubehalten.')])

mail(H, '07_Kruse_Referenzzuordnung.eml', 'Sporthalle Wiesenrain: Bitte Büro und Person trennen', '2026-09-29T15:41:00+02:00',
    'Lena Kruse <kruse@faltwerk.example>', 'Anna Finke <archiv@faltwerk.example>',
    'Liebe Frau Finke,\n\ndie Halle Wiesenrain habe ich von 2019 bis 2022 beim damaligen Büro Feldmaß geleitet. Faltwerk war weder Vertragspartner noch Mitglied einer Arbeitsgemeinschaft. Bitte führen Sie die Halle in meinem Lebenslauf als persönliche Erfahrung, nicht als abgeschlossene Büroreferenz von Faltwerk. Das archivierte Abschlussdatum 22.07.2022 stimmt.\n\nZum Campus Hofgarten war ich ab Januar 2021 bei Faltwerk verantwortlich. Herr Aydin hat dort die Überwachung übernommen. Für die Hamelner Bewerbung können wir die vorliegende Auftraggeberbestätigung verwenden. Ich kann jedoch für Januar 2027 keine Verfügbarkeit von 24 Wochenstunden zusagen: Riedhof bindet mich nach der aktuellen Personalplanung mit 26 Stunden, hinzu kommen sechs Stunden Büroleitung.\n\nFreundliche Grüße\nLena Kruse\nArchitektin, Partnerin')

doc(H, '08_Versicherungsbestaetigung.pdf', 'Berufshaftpflicht für Faltwerk Architektur', '2026-09-23',
    'Hansewinkel Versicherungsverein a. G.\nKontorhof 20, 30159 Hannover\nvertrag@hansewinkel.example', HP,
    'Vertrag HW-FA-2086', 'gez. Sina Vogt, Vertragsservice', [
    ('1 Versicherungsschutz', 'Für Faltwerk Architektur PartG besteht bis 31.12.2026 eine Berufshaftpflichtversicherung mit einer Deckung von 3.000.000 EUR je Personenschaden und 1.000.000 EUR je sonstigem Schaden. Die Versicherungssummen stehen je Versicherungsjahr zweifach zur Verfügung. Dies entspricht dem derzeit vereinbarten Vertrag, nicht automatisch einer projektspezifisch erhöhten Deckung.'),
    ('2 Anfrage Lernhaus', 'Für das Projekt Lernhaus Am Werder haben Sie eine Erhöhung der Deckung für sonstige Schäden auf 2.000.000 EUR angefragt. Die Risikoprüfung läuft. Wir benötigen hierzu die abschließende Leistungsbeschreibung und die Erklärung, ob Leistungen für die Schadstoffplanung übernommen werden sollen. Eine verbindliche Deckungszusage für die Erhöhung erteilen wir mit diesem Schreiben noch nicht.'),
    ('3 Weiteres Vorgehen', 'Bitte übermitteln Sie die Angaben bis 02.10.2026, damit wir vor Ihrem Bewerbungsschluss antworten können. Die vorliegende Bestätigung kann zum Nachweis des bestehenden Versicherungsschutzes verwendet werden. Eine besondere Versicherungsbescheinigung für den Auftragsfall stellen wir erst nach Abschluss der Risikoprüfung aus.')])

doc(H, '09_Teamprofile.docx', 'Vorgesehenes Team Lernhaus', '2026-09-28', HP, 'Büroleitung Faltwerk Architektur',
    'SW-2026-18 / Personalstand 28.09.', 'gez. Anna Finke, Personalorganisation', [
    ('1 Projektleitung Lena Kruse', 'Lena Kruse schloss ihr Architekturstudium 2012 ab und ist seit Juli 2015 als Architektin eingetragen. Seit 2021 ist sie Partnerin bei Faltwerk. Sie leitete den Campus Hofgarten und verantwortet derzeit die Ausführungsplanung Riedhof. Ihre Wochenarbeitszeit beträgt 40 Stunden. Urlaub vom 04. bis 15.01.2027 ist bestätigt; die Kapazitätsdatei enthält bereits die durchschnittliche Reduzierung im Januar.'),
    ('2 Stellvertretung Mehmet Aydin', 'Mehmet Aydin arbeitet seit Oktober 2018 als angestellter Architekt. Er betreute Hofgarten in der Objektüberwachung und den Innenausbau Südbogen. Seine vertragliche Wochenarbeitszeit beträgt 32 Stunden. Er ist im ersten Quartal 2027 mit 18 Wochenstunden am Projekt Südkai gebunden. Eine Erhöhung auf Vollzeit ist besprochen, aber nicht vereinbart.'),
    ('3 Ergänzendes Personal', 'Clara Weiß steht mit 40 Wochenstunden für Ausführungsplanung und Dokumentation zur Verfügung. Ihre vorhandenen Projektbindungen nehmen im Januar 24 Stunden ein. Für Moderation und Nutzerworkshops ist die externe Planerin Frauke Bendel angefragt. Eine Verpflichtungserklärung liegt nicht vor. Die beiden im Teamprofil benannten Führungsrollen dürfen ohne Zustimmung der Büroleitung nicht gegen andere Personen ausgetauscht werden.')])

book(H, '10_Personaleinsatz.xlsx', 'Personaleinsatz erstes Quartal 2027', '2026-09-30', 'Faltwerk / Anna Finke', [dict(
    name='Kapazität', headers=['Person und Monat','Verfügbar h/W','Bestand h/W','Büro h/W','Lernhaus h/W','Rest h/W'],
    rows=[[label,a,b,c,d,f'=B{i}-C{i}-D{i}-E{i}'] for i,(label,a,b,c,d) in enumerate([
      ['Kruse Januar',32,26,6,16],['Kruse Februar',40,24,6,16],['Kruse März',40,20,6,16],
      ['Aydin Januar',32,18,2,12],['Aydin Februar',32,18,2,12],['Aydin März',32,14,2,12],
      ['Weiß Januar',40,24,2,16],['Weiß Februar',40,20,2,16],['Weiß März',40,16,2,16]],6)],
    tail=[], notes=['Durchschnittliche Wochenstunden je Monat, keine Vollzeitäquivalente.',
    'Lernhaus ist eine Disposition, noch keine Freigabe. Urlaub ist in Verfügbar enthalten.',
    'gez. Anna Finke; 30.09.2026. Externe Zusagen sind nicht eingerechnet.'],
    controls={'F6':-16,'F7':-6,'F8':-2,'F9':0,'F12':-2},
    mutation={'cell':'E6','value':0,'result':'F6','expected':0})])

mail(H, '11_Bendel_Kapazitaet.eml', 'Lernhaus Hameln: Nutzerworkshops im Februar', '2026-10-01T08:53:00+02:00',
    'Frauke Bendel <post@bendel-planung.example>', 'Lena Kruse <kruse@faltwerk.example>',
    'Sehr geehrte Frau Kruse,\n\nfür die angefragte Moderation kann ich im Februar und März 2027 jeweils acht Wochenstunden reservieren, sofern wir bis 16.10. eine Beauftragung vereinbaren. Im Januar bin ich vollständig in Langenhagen gebunden. Eine Projektleitung oder Objektüberwachung biete ich für das Lernhaus nicht an.\n\nSie können mich derzeit als angefragte externe Moderatorin erwähnen. Als verbindlich verfügbares Mitglied Ihres Teams möchte ich ohne Leistungsvereinbarung noch nicht benannt werden. Eine Verpflichtungserklärung werde ich erst nach Prüfung des endgültigen Umfangs unterzeichnen. Bitte schicken Sie mir insbesondere die geplante Zahl der Abendtermine und die Anforderungen an die Dokumentation. Mein Tagessatz beträgt 920 EUR netto für acht Stunden, Reisekosten nach Vereinbarung.\n\nMit freundlichen Grüßen\nFrauke Bendel\nArchitektin')

doc(H, '12_Konzeptstand_Buero.docx', 'Konzeptstand Lernhaus Am Werder', '2026-09-30', HP, 'Lena Kruse und Mehmet Aydin',
    'SW-2026-18 / Entwurf 0.3', 'Bearbeitet von Clara Weiß, noch nicht durch die Büroleitung freigegeben', [
    ('1 Projektorganisation', 'Wir schlagen Lena Kruse als Projektleiterin und Mehmet Aydin als Stellvertreter vor. Unser bisheriger Text geht von einer wöchentlichen Vor-Ort-Runde der Projektleiterin ab Januar aus. Für Krankheitsvertretungen soll ein gemeinsames Entscheidungsbuch geführt werden. Die Personaldisposition vom 30.09. ist noch nicht mit diesem Text abgeglichen. Frauke Bendel ist für Workshops angefragt; ihre Zusage wurde bei der Abfassung noch erwartet.'),
    ('2 Unterricht während des Umbaus', 'Wir möchten den westlichen Unterrichtsflügel zunächst vom Baustellenzugang trennen. Materialtransporte sollen außerhalb der Ankunftszeiten stattfinden. Vor dem ersten Abschnitt soll eine gemeinsame Wegebegehung mit Schulleitung und Brandschutzplanung stattfinden. Ob die Werkstatt während der Sommerferien vollständig umgebaut werden kann, hängt von der noch ausstehenden Erkundung und den Lieferzeiten ab. Einen geprüften Abschnittsplan haben wir noch nicht erstellt.'),
    ('3 Kosten und Termine', 'Für die Kostengruppen 300 und 400 wird die Vorgabe von 5,8 Mio. EUR netto übernommen. Änderungen sollen vor Freigabe mit Kosten und Terminauswirkung vorgelegt werden. Als Beispiel wurde bisher Südbogen genannt; die dortige ARGE-Leistung ist in der Bewerbung präzise abzugrenzen. Dieser Text wurde für eine mögliche spätere Einladung vorbereitet und ist noch kein Bestandteil des Teilnahmeantrags.')])

mail(H, '13_Antwort_Vergabestelle.eml', 'SW-2026-18: Antwort 03 an alle Interessenten', '2026-09-25T10:06:00+02:00',
    'Eva Brüning <vergabe@schulbau-weserraum.example>', 'Interessentenverteiler <verfahren-sw18@schulbau-weserraum.example>',
    'Sehr geehrte Damen und Herren,\n\nauf die Frage nach dem Referenzzeitraum bestätigen wir: Maßgeblich ist der Abschluss der Phase 8 zwischen 01.01.2021 und Bewerbungsschluss. Eine noch laufende Phase 8 genügt hierfür nicht. Persönliche Erfahrungen können im Lebenslauf genannt werden. Sie ersetzen nicht die geforderte Büroreferenz mit ausgewiesenen eigenen Leistungsanteilen.\n\nIm Teilnahmeantrag sind genau zwei Referenzen zu bezeichnen. Mehrfachnennungen desselben Projekts werden nicht als verschiedene Referenzen behandelt. Die bereits veröffentlichte Kriterienanlage bleibt ansonsten unverändert. Ein Konzept wird erst von den eingeladenen Büros verlangt und ist nicht als zusätzliches Auswahlkriterium vorgesehen.\n\nDiese Antwort wird allen registrierten Interessenten gleichzeitig über das Verfahrenspostfach zugänglich gemacht. Der Bewerbungsschluss bleibt am 09.10.2026 um 12:00 Uhr.\n\nMit freundlichen Grüßen\nEva Brüning\nVergabestelle')

doc(H, '14_Buerostandard_Bewerbungen.docx', 'Bürostandard für Teilnahmeanträge', '2026-05-18', HP,
    'Projektleitungen und Bewerbungsassistenz', 'Organisation / Standard BS-04', 'gez. Lena Kruse, Partnerin', [
    ('1 Referenzangaben', 'Die Bewerbungsassistenz übernimmt aus dem Archiv nur Angaben, die durch Vertrag oder Auftraggeberbestätigung belegt sind. Erfahrungen von Mitarbeitenden aus früheren Büros werden mit damaligem Büro und persönlicher Rolle bezeichnet. Eine öffentliche Projektseite ersetzt keine Bestätigung des eigenen Leistungsanteils. Die verantwortliche Projektleitung zeichnet die endgültige Referenzauswahl ab.'),
    ('2 Textbausteine und Personal', 'Konzepttexte werden anhand der konkret veröffentlichten Kriterien und Projektaufgabe erstellt. Frühere Zusagen zu Anwesenheit oder Reaktionszeiten dürfen nicht ungeprüft übernommen werden. Die Personalorganisation bestätigt vor Freigabe die verfügbaren Stunden. Externe Leistungen dürfen nur als gesichert dargestellt werden, wenn Umfang, Zeitraum und verbindliche Zusage vorliegen.'),
    ('3 Einreichung', 'Die Büroleitung gibt den Teilnahmeantrag einschließlich Anlagenverzeichnis frei. Nur die benannte Person lädt die Unterlagen im Verfahrenspostfach hoch und archiviert die Eingangsbestätigung. Der Versand einer internen Entwurfsdatei per E-Mail ersetzt weder Freigabe noch Einreichung. Jede Änderung nach Freigabe erhält einen neuen Dateistand.')])

mail(H, '15_Auftrag_Bueroleitung.eml', 'Hameln: Unterlagen bis Montag zusammenführen', '2026-10-02T16:10:00+02:00',
    'Lena Kruse <kruse@faltwerk.example>', 'Anna Finke <bewerbung@faltwerk.example>',
    'Sehr geehrte Frau Finke,\n\nbitte stellen Sie bis Montag den Teilnahmeantrag für SW-2026-18 zusammen. Wir haben sechs Projekte im Archiv, aber noch keine verbindliche Auswahl der zwei einzureichenden Referenzen. Prüfen Sie die Angaben gegen die Bestätigungen und legen Sie mir die Auswahl zur Unterschrift vor. Die noch ausstehende Deckungszusage habe ich beim Versicherer erneut angefragt.\n\nDen Konzeptstand von Frau Weiß möchte ich als Vorbereitung für eine spätere Einladung behalten. Er soll nicht als zusätzliche Referenz oder als bereits abgegebenes Angebot in den Antrag geraten. Die Stundenfrage lösen wir in der Partnerbesprechung; bis dahin bitte keine uneingeschränkte Verfügbarkeit erklären. Frau Bendels heutige Nachricht ist bei der Teamdarstellung zu berücksichtigen. Einen Upload am Portal habe ich noch nicht freigegeben.\n\nMit freundlichen Grüßen\nLena Kruse\nPartnerin', ['12_Konzeptstand_Buero.docx'])

doc(H, '16_Bewerberangaben.docx', 'Bewerberangaben Faltwerk Architektur', '2026-10-02', HP, HS,
    'SW-2026-18 / Erfassungsstand vor Freigabe', 'Erfasst: Anna Finke\nFreigabe durch die Partnerin steht aus', [
    ('1 Büro und Kontakt', 'Bewerberin ist Faltwerk Architektur PartG mit Sitz in Hameln. Als bevollmächtigte Ansprechpartnerin ist Lena Kruse vorgesehen. Das Büro beschäftigt einschließlich Partnerinnen und Partnern elf fachlich Mitarbeitende. Die Zahlen aus der Personalstatistik betragen neun für 2023, zehn für 2024 und elf für 2025. Die Bewerbung soll als Einzelbüro erfolgen, nicht als Bewerbergemeinschaft.'),
    ('2 Leistungsorganisation', 'Die Objektplanung soll durch das eigene Team erbracht werden. Für die Nutzerworkshops wird eine externe Moderation erwogen. Die konkreten Verpflichtungsunterlagen sind noch nicht zurückgekommen. Die Nachweise zur Berufszulassung liegen in der Personalakte; für die Einreichung muss die zuständige Partnerin deren aktuelle Fassung bereitstellen.'),
    ('3 Stand der Erklärung', 'Die Assistenz hat noch keine unterschriebene Erklärung zu Ausschlussgründen erhalten. Auch die Auswahl der zwei Referenzen ist nicht freigegeben. Dieses Erfassungsblatt wurde aus dem Bürostamm erstellt und ist nicht als unterschriebener Teilnahmeantrag versandt worden. Die verbindliche Erklärung wird erst nach Kontrolle der zusammengeführten Anlagen abgegeben.')])

G = case('bau-rundum-angebotspruefung-goslar',
         'Angebotseingang für die Fassade am Bildungsforum Oker in Goslar',
         'Bildungsforum Oker, Fassadenlos F03, Goslar',
         'Öffentliches Bauvergabeverfahren mit verschlossenem elektronischem Eingang, drei positionsbezogenen Angeboten, technischen Abweichungen, fehlenden Nachweisen und begrenztem Zugriff auf Bieterdaten.',
         ['Eingang, Öffnung und Integrität von Vollständigkeit und Wertung getrennt behandeln.',
          'Bieterforderungen, Verfahrensvorgaben und rechtliche Zulässigkeit einer Nachforderung unterscheiden.',
          'Drei Angebotssummen positionsbezogen nachvollziehen; Produktgleichwertigkeit nicht aus einem Werbetext ableiten.',
          'Vertraulichkeit wahren und weder Nachforderung noch Zuschlag eigenständig versenden.'])
GA = 'Zweckverband Bildungsforum Harz\nOkerterrasse 9, 38640 Goslar\nvergabe@bildungsforum-harz.example'
GP = 'Kantenraum Ingenieure GmbH\nHüttenwinkel 18, 38642 Goslar\nvergabe@kantenraum.example'
doc(G, '01_Verfahrensbedingungen.docx', 'Vergabebedingungen Fassadenlos F03', '2026-09-04', GA,
    'Interessierte Bauunternehmen', 'ZBH-26-31 / Ausgabe 1', 'gez. Miriam Ehlers, Leitung Vergabe', [
    ('1 Vergabegegenstand', 'Der Zweckverband vergibt das Fassadenlos F03 des Bildungsforums Oker im offenen Verfahren. Die öffentliche Bekanntmachung und die Bereitstellung der Unterlagen erfolgen am 07.09.2026. Der geschätzte Gesamtwert des Bauvorhabens beträgt 8,4 Mio. EUR netto. Als Verfahrensgrundlage ist die VOB/A-EU 2026, Bekanntmachung vom 22.07.2026, benannt. Diese Bedingungen beschreiben die konkrete Angebotsanforderung; sie ersetzen nicht die Prüfung der anwendbaren Vergaberegeln.'),
    ('2 Abgabe und Unterlagen', 'Angebote müssen bis 05.10.2026, 10:00 Uhr, verschlüsselt über das Vergabepostfach eingehen. Eine E-Mail-Abgabe ist nicht vorgesehen. Bindefrist ist der 04.12.2026. Mit dem Angebot sind das ausgefüllte Preisblatt, die Produktangaben je Fenstertyp und die Eigenerklärung E1 einzureichen. Bei benannten Nachunternehmen sind Tätigkeitsumfang und Name anzugeben. Die Verpflichtungserklärung N2 wird auf gesondertes Verlangen angefordert. Die Vergabestelle legt sich mit diesen Bedingungen nicht vorab auf eine Nachforderung sämtlicher denkbarer Mängel fest.'),
    ('3 Leistung und Wertung', 'Nebenangebote sind nicht zugelassen. Gleichwertige Produkte sind innerhalb der beschriebenen technischen Mindestanforderungen zulässig und im Produktblatt konkret zu benennen. Der Preis ist alleiniges Zuschlagskriterium unter den wertbaren Angeboten. Preisnachlässe ohne Bedingungen sind im Anschreiben anzugeben. Skonto wird nicht in den Vergleichspreis einbezogen. Eine Produktänderung nach Ablauf der Angebotsfrist ist mit der Aufforderung zur bloßen Erläuterung nicht automatisch gestattet.'),
    ('4 Kommunikation', 'Bieterfragen und Antworten werden über das Vergabepostfach geführt. Die Angebotsöffnung findet ohne Bieteranwesenheit statt. Inhalte konkurrierender Angebote werden nicht ungeprüft herausgegeben. Die Angebotsprüfung erfolgt durch die Vergabestelle mit technischer Unterstützung von Kantenraum. Ein Zuschlag bedarf der gesonderten Entscheidung des Zweckverbands.')])

ITEM_G = [
 ['01.010','Aluminiumfenster F1','m²',240],['01.020','Türanlage T1','St',18],
 ['02.010','Pfosten Riegel F2','m²',120],['02.020','Sonnenschutz','St',60],
 ['03.010','Rauchabzug R1','St',24],['04.010','Baustelleneinrichtung','psch',1],
 ['04.020','Anschlussdetail D4','St',16],['04.030','Laibungsbekleidung','m',80],
]
PRICES_G = {'Rautenbau':[315,1900,680,820,1450,9800,2150,165],
            'Okerfenster':[302,1840,645,805,1430,11500,2200,160],
            'Bergglas':[328,1810,670,790,1510,8700,2090,155]}
doc(G, '02_Leistungsverzeichnis.pdf', 'Leistungsverzeichnis Fassade F03', '2026-09-04', GP, GA,
    'BFO / F03 / Revision 2', 'gez. Jonas Blume, Fachplanung Fassade', [
    ('1 Fenster und Verglasung', 'Die Menge 240 m² der Position 01.010 umfasst die Außenmaße aller Elemente vom Typ F1. Für das vollständig angebotene Element ist ein Wärmedurchgangskoeffizient Uw von höchstens 1,0 W/(m²K) nachzuweisen. Ein Wert allein für die Verglasung ist dafür nicht ausreichend. Das Produkt ist mit Systembezeichnung und vorgesehener Verglasung zu benennen. Die technische Anforderung gilt unabhängig vom Hersteller.'),
    ('2 Leistungsschnittstellen', 'Türantriebe, Anschlussbleche und Montage sind in den jeweiligen Einheitspreisen enthalten. Position 03.010 umfasst den kompletten Rauchabzug einschließlich Antrieb und Funktionsprüfung im Verbund mit der Steuerung. Die Anschlussdetails D4 werden nicht zusätzlich nach laufendem Meter vergütet. Für Sonnenschutz ist die im Antwortschreiben vom 22.09. beschriebene Steuerung mitzuerfassen.'),
    ('3 Termine', 'Aufmaß vor Ort ist ab 07.12.2026 möglich. Die Montage ist für 01.03. bis 30.04.2027 vorgesehen. Die Gerüststellung übernimmt ein anderes Los. Der Auftragnehmer hat seine Transportmittel und die Abstimmung der Hebetermine einzukalkulieren. Die folgenden Mengen sind für alle Bieter unverändert zu bepreisen.')],
    (['Position','Leistung','Einheit','Menge'],ITEM_G))

mail(G, '03_Bieterantwort_Steuerung.eml', 'ZBH-26-31: Antwort 04 zur Sonnenschutzsteuerung', '2026-09-22T13:00:00+02:00',
    'Miriam Ehlers <vergabe@bildungsforum-harz.example>', 'Bieterverteiler <bieter-f03@bildungsforum-harz.example>',
    'Sehr geehrte Damen und Herren,\n\ndie Position 02.020 enthält die lokalen Motorsteuergeräte und die Inbetriebnahme der Sonnenschutzantriebe. Die zentrale Wetterstation gehört zum Elektrolos. Die Schnittstelle wird als potentialfreier Kontakt ausgeführt. Bitte kalkulieren Sie die erforderlichen Anschlussklemmen und die Abstimmung mit dem Elektrolos ein.\n\nDie Preise sind weiterhin in das unveränderte Mengenblatt F03 einzutragen. Es werden keine weiteren Positionen eingefügt. Anfragen nach dem Einsatz eines anderen Fenstersystems sind mit genauer System- und Glasangabe zu stellen. Die Mindestanforderung Uw höchstens 1,0 W/(m²K) für das vollständige Element bleibt bestehen.\n\nDiese Nachricht wurde gleichzeitig im Verfahrenspostfach für alle registrierten Unternehmen veröffentlicht. Angebots- und Bindefrist ändern sich nicht.\n\nMit freundlichen Grüßen\nMiriam Ehlers\nLeitung Vergabe')

doc(G, '04_Oeffnungsniederschrift.pdf', 'Niederschrift elektronische Angebotsöffnung', '2026-10-05', GA,
    'Vergabeakte ZBH-26-31, zugriffsberechtigter Personenkreis', 'ZBH-26-31 / Öffnung 10:03 Uhr',
    'gez. Miriam Ehlers, Öffnende\ngez. David Schütz, zweite anwesende Person', [
    ('1 Verschlossener Eingang', 'Die Angebotsfrist endete am 05.10.2026 um 10:00 Uhr. Bis dahin wurden die drei eingegangenen Container im System als verschlüsselt und nicht lesbar geführt. Um 10:03 Uhr gaben Ehlers und Schütz gemeinsam die Öffnung frei. Die Sitzung endete um 10:21 Uhr. Bieter waren nicht anwesend. Vorfristige Lesezugriffe sind im exportierten Zugriffsprotokoll nicht verzeichnet.'),
    ('2 Festgehaltene Erklärungen', 'Die in der folgenden Tabelle genannten Summen wurden aus den Angebotsanschreiben abgelesen. Bei Bergglas wurde ein unbedingter Nachlass von zwei Prozent vorgelesen. Rautenbau nennt zwei Prozent Skonto bei Zahlung binnen zehn Tagen. Diese Niederschrift enthält keine Entscheidung über Vollständigkeit, Rechenrichtigkeit, Gleichwertigkeit oder Zuschlagsfähigkeit.'),
    ('3 Ablage', 'Die aus den Containern exportierten Angebots-PDFs liegen unverändert im geschützten Ordner. Für die drei Hauptangebote wurden beim Export SHA-256-Prüfsummen in 15_Exportprotokoll.txt geschrieben. Das Dokumentenregister bezeichnet vorhandene und nicht vorgefundene Dateien. Ein nicht vorgefundener Nachweis wurde nicht durch eine leere Ersatzdatei ergänzt.')],
    (['Bieter','Eingang','Abgelesen netto EUR','Erklärung'],
     [[name,date,eur(sum(r[3]*p for r,p in zip(ITEM_G,prices))-(440 if name=='Bergglas' else 0)),extra] for (name,prices),date,extra in zip(PRICES_G.items(),
       ['02.10.2026 14:12','05.10.2026 09:41','05.10.2026 09:58'],['2 % Skonto','kein Nachlass','2 % Nachlass'])]))

for number, name, address, signer, paragraphs in [
    (5,'Rautenbau','Rautenbau Fassaden GmbH\nGewerbebogen 7, 38644 Goslar\nangebot@rautenbau.example','gez. Nora Baumeister, Geschäftsführerin',[
       ('1 Angebotserklärung','Wir bieten das Fassadenlos F03 nach den überlassenen Unterlagen einschließlich Antwort 04 zu den im Preisblatt genannten Einheitspreisen an. Das Angebot bindet uns bis 04.12.2026. Die Montage zwischen 01.03. und 30.04.2027 ist berücksichtigt. Bei Zahlung binnen zehn Tagen gewähren wir zwei Prozent Skonto. Einen unbedingten Nachlass bieten wir nicht an.'),
       ('2 Produkte und Nachweise','Für F1 bieten wir das System RB 90 mit Dreifachverglasung an. Für das angebotene Referenzelement mit 1,23 × 1,48 m erklären wir Uw 0,96 W/(m²K). Die übrigen Größen werden nach Aufmaß gerechnet. Fremdleistungen sind nicht vorgesehen. Die Eigenerklärung E1 ist Bestandteil dieses Angebots: Über unser Vermögen ist kein Insolvenzverfahren eröffnet oder beantragt. Wir haben fällige Steuern und Sozialabgaben entrichtet und erklären, dass die abgefragten Ausschlussgründe nicht vorliegen. Die Angaben bestätigen wir mit der Unterschrift unter diesem Angebot.')]),
    (6,'Okerfenster','Okerfenster Montage GmbH\nWerkbogen 25, 38259 Salzgitter\nangebote@okerfenster.example','gez. Enno Voss, Geschäftsführer',[
       ('1 Angebotserklärung','Unser Angebot gilt für die unveränderten Mengen des Leistungsverzeichnisses. Wir gewähren weder Skonto noch einen pauschalen Nachlass. Die Bindefrist und die Montagezeit erkennen wir an. Den Rauchabzug soll Nordlicht Antriebstechnik montieren; dessen Tätigkeit ist im Nachunternehmerverzeichnis bezeichnet.'),
       ('2 Produktangabe','Für die Aluminiumfenster bieten wir das System OV 78 mit Glas G3 an. Das beigefügte Datenblatt nennt Ug 0,6 W/(m²K), jedoch keinen für alle angebotenen Größen gerechneten Uw-Wert. Nach unserer Einschätzung ist das System wirtschaftlich gleichwertig. Die unterschriebene Eigenerklärung E1 wurde von unserer Assistenz zum Upload vorbereitet. Wir bitten, uns zu benachrichtigen, falls sie im Container nicht lesbar ist.')]),
    (7,'Bergglas','Bergglas Bauelemente GmbH\nBergwiesenweg 16, 38678 Clausthal-Zellerfeld\nvergabe@bergglas.example','gez. Judith Rehberg, Prokuristin',[
       ('1 Angebotserklärung','Wir bieten das Los F03 mit einem unbedingten Nachlass von zwei Prozent auf die gesamte Nettosumme an. Der Nachlass gilt auch für die auf den Einheitspreisen beruhende Abrechnung. Ein zusätzliches Skonto wird nicht eingeräumt. Wir halten uns bis 04.12.2026 gebunden und haben den vorgesehenen Montagezeitraum kalkuliert.'),
       ('2 Technische Angaben','Wir bieten für F1 das System BG 92 mit Dreifachverglasung an. Für das angebotene Referenzelement mit 1,23 × 1,48 m erklären wir Uw 0,98 W/(m²K). Die Rauchabzugssteuerung stammt aus unserer eigenen Fertigung. Eigenerklärung E1: Über unser Vermögen ist kein Insolvenzverfahren eröffnet oder beantragt. Fällige Steuern und Sozialabgaben sind entrichtet. Die abgefragten Ausschlussgründe liegen nach unserer Kenntnis nicht vor. Die Erklärung und die technischen Angaben sind Bestandteil dieses unterschriebenen Angebots.')])]:
    values = PRICES_G[name]
    rows = [[r[0],r[3],p,eur(33000 if name=='Bergglas' and r[0]=='04.020' else r[3]*p)] for r,p in zip(ITEM_G,values)]
    correct = sum(r[3]*p for r,p in zip(ITEM_G,values))
    stated = correct-440 if name=='Bergglas' else correct
    paragraphs.append(('3 Angebotssumme',f'Die im Anschreiben ausgewiesene Nettosumme vor Nachlass beträgt {eur(stated)} EUR. '+
      (f'Nach zwei Prozent Nachlass werden {eur(round(stated*0.98,2))} EUR netto und {eur(round(stated*0.98*1.19,2))} EUR brutto genannt.' if name=='Bergglas'
       else f'Bei 19 Prozent Umsatzsteuer nennen wir {eur(round(stated*1.19,2))} EUR brutto.')))
    doc(G, f'{number:02}_Angebot_{name}.pdf', f'Angebot {name} Fassadenlos F03', '2026-10-02', address, GA,
        f'ZBH-26-31 / {name} Angebot', signer, paragraphs,
        (['Pos.','Menge','EP netto EUR','GP laut Angebot EUR'],rows))

csv(G, '08_Preisdaten_Export.csv', 'Positionswerte der Angebotscontainer', '2026-10-05', 'Vergabestelle / David Schütz',
    ['Bieter','Pos','Menge','Einheit','EP_EUR_netto','GP_eingetragen_EUR','Unbedingter_Nachlass_Prozent'],
    [[name,r[0],r[3],r[2],p,33000 if name=='Bergglas' and r[0]=='04.020' else r[3]*p,2 if name=='Bergglas' else 0]
     for name,prices in PRICES_G.items() for r,p in zip(ITEM_G,prices)])

doc(G, '09_Produktblatt_OV78.pdf', 'Produktblatt OV78 mit Verglasung G3', '2026-09-18',
    'Okerfenster Montage GmbH\nWerkbogen 25, 38259 Salzgitter\ntechnik@okerfenster.example', GA,
    'OV78 / G3 / Datenblatt 09-2026', 'gez. Enno Voss, technische Geschäftsführung', [
    ('1 Aufbau', 'Das angebotene Profilsystem OV78 hat eine Bautiefe von 78 mm und thermisch getrennte Rahmen. Die Verglasung G3 wird mit einem Ug-Wert von 0,6 W/(m²K) geliefert. Der Rahmenwert Uf beträgt nach unserer Systemberechnung 1,7 W/(m²K). Die Angabe zum Glas ist kein Gesamtwert für ein eingebautes Fensterelement.'),
    ('2 Berechnungsbeispiel', 'Für ein Element mit Außenmaßen 1,23 m × 1,48 m und der vorgesehenen Randverbundausführung ergibt unsere Berechnung Uw 1,12 W/(m²K). Für größere Elemente mit höherem Glasanteil können andere Werte entstehen. Eine Größenliste für die 240 m² des Loses F03 haben wir diesem Blatt nicht beigefügt. Das Datenblatt enthält keine Zusicherung eines Uw-Werts von 1,0 für jede angebotene Größe.'),
    ('3 Lieferumfang', 'Die Verbindung mit dem Sonnenschutz erfolgt nach der Schnittstellenbeschreibung vom 22.09.2026; diese Angabe wurde dem Angebotstext beigefügt, nicht dem Ausgabestand dieses Datenblatts. Für ein anderes Profilsystem wäre eine gesonderte Kalkulation erforderlich. Dieses Blatt beschreibt ausschließlich OV78 mit G3 und bietet keinen automatischen Systemwechsel an.')])

csv(G, '10_Dokumentenregister.csv', 'Containerinhalt bei Erstöffnung', '2026-10-05', 'David Schütz / Vergabestelle',
    ['Bieter','Unterlage','Eingangsfeststellung','Fundort','Aufgenommen_durch'],[
    ['Rautenbau','Preisblatt und Erklärung','vorhanden','05_Angebot_Rautenbau.pdf','Schütz'],
    ['Rautenbau','E1','im unterschriebenen Hauptangebot','05_Angebot_Rautenbau.pdf / Abschnitt 2','Schütz'],
    ['Okerfenster','Preisblatt','vorhanden','06_Angebot_Okerfenster.pdf','Schütz'],
    ['Okerfenster','E1','nicht vorgefunden','kein Exportobjekt','Schütz'],
    ['Okerfenster','Produktblatt','vorhanden','09_Produktblatt_OV78.pdf','Schütz'],
    ['Okerfenster','N2 Verpflichtung','nicht vorgefunden','noch nicht gesondert verlangt','Schütz'],
    ['Bergglas','Preisblatt und E1','im unterschriebenen Hauptangebot','07_Angebot_Bergglas.pdf / Abschnitt 2','Schütz'],
    ['Bergglas','F1 Elementangabe','im unterschriebenen Hauptangebot','07_Angebot_Bergglas.pdf / Abschnitt 2','Schütz'],
    ])

mail(G, '11_Okerfenster_Erlaeuterung.eml', 'F03: Eigenerklärung und Profil OV78', '2026-10-05T12:44:00+02:00',
    'Enno Voss <angebote@okerfenster.example>', 'Miriam Ehlers <vergabe@bildungsforum-harz.example>',
    'Sehr geehrte Frau Ehlers,\n\nunsere Assistenz hat bemerkt, dass E1 möglicherweise nicht im Angebotscontainer lag. Wir verlangen eine Gelegenheit zur Nachreichung und halten einen Ausschluss ohne diese Gelegenheit für unzulässig. Das ist unsere Auffassung zum Verfahren. Eine unterschriebene E1 senden wir mit dieser Nachricht noch nicht nach, weil wir den vorgesehenen Übermittlungsweg abwarten möchten.\n\nZum Profil OV78 möchten wir ergänzen, dass der Glaswert von 0,6 sehr gut ist. Sollte Ihnen das System nicht genügen, könnten wir OV90 gegen Mehrpreis liefern. Die Höhe des Mehrpreises ist noch nicht kalkuliert. Unser ursprüngliches Angebot bleibt OV78 mit G3. Wir bitten, das beigefügte Datenblatt zunächst technisch zu prüfen und unsere Preise nicht anderen Bietern mitzuteilen.\n\nMit freundlichen Grüßen\nEnno Voss\nGeschäftsführer', ['09_Produktblatt_OV78.pdf'])

mail(G, '12_Rautenbau_Auskunftsverlangen.eml', 'ZBH-26-31: Bitte um Öffnungsdaten und Einsicht', '2026-10-05T15:32:00+02:00',
    'Nora Baumeister <angebot@rautenbau.example>', 'Miriam Ehlers <vergabe@bildungsforum-harz.example>',
    'Sehr geehrte Frau Ehlers,\n\nwir bitten um Mitteilung der bei Öffnung verlesenen Endbeträge. Darüber hinaus verlangen wir die ungeschwärzten Preisblätter und Produktnachweise der Wettbewerber. Nach unserer Auffassung müssen wir daraus die Vergleichbarkeit der Angebote selbst prüfen können. Wir erwarten Ihre Antwort bis 07.10.2026.\n\nUns wurde auf einer anderen Baustelle gesagt, ein Wettbewerber biete ein schmaleres Profilsystem an. Den Wahrheitsgehalt können wir nicht beurteilen. Bitte verstehen Sie dies nicht als eigene technische Feststellung. Wir haben keine Erlaubnis gegeben, unsere Kalkulation oder unsere Lieferantenpreise an andere Bieter zu übersenden. Unser Interesse an Auskünften zu den Konkurrenten ändert daran nichts.\n\nMit freundlichen Grüßen\nNora Baumeister\nRautenbau Fassaden GmbH')

doc(G, '13_Vertraulichkeit_Projektgruppe.docx', 'Zugriff auf die Angebotsunterlagen', '2026-10-05', GA, GP,
    'ZBH-26-31 / Zugriff F03', 'gez. Miriam Ehlers, Leitung Vergabe\nBestätigt: Jonas Blume', [
    ('1 Berechtigter Kreis', 'Kantenraum erhält Zugriff ausschließlich für Jonas Blume und Sabine Kern zur technischen und rechnerischen Prüfung des Fassadenloses. Die Dateien dürfen nicht in allgemein zugängliche Projekträume übernommen werden. Die zugelassenen Personen behandeln Preise, Produktkonfigurationen und Nachunternehmerangaben vertraulich. Ein Beratungsauftrag für einen der drei Bieter ist unverzüglich zu melden.'),
    ('2 Kommunikation', 'Rückfragen an Bieter werden zunächst als Entwurf an die Vergabestelle gegeben. Kantenraum versendet keine Nachforderungen oder Produktfreigaben im eigenen Namen. Ebenso werden auf direkte Nachfrage eines Bieters keine fremden Unterlagen ausgehändigt. Über Auskunft und etwaige Schwärzungen entscheidet die Vergabestelle nach gesonderter Prüfung.'),
    ('3 Stand', 'Bis 05.10.2026, 16:00 Uhr, wurde keine Nachforderung freigegeben und kein Zuschlag beschlossen. Die technische Prüfung soll bis 08.10. erste konkrete Fundstellen liefern. Das Preisblatt ist als Arbeitskopie zu bearbeiten; die ursprünglichen Exportdateien bleiben unverändert.')])

doc(G, '14_Mittelbereitstellung.docx', 'Mittelstand Fassadenlos', '2026-09-03',
    'Zweckverband Bildungsforum Harz\nKämmerei, Okerterrasse 9, 38640 Goslar\nfinanzen@bildungsforum-harz.example',
    'Miriam Ehlers, Vergabestelle', 'Haushalt BFO-26 / F03', 'gez. Carsten Möller, Kämmerer', [
    ('1 Budget', 'Für das Fassadenlos sind im Projektbudget 405.000 EUR brutto einschließlich der erwarteten Baupreisreserve eingestellt. Die Kostenberechnung der Fachplanung vom 28.08. ist als interne Kalkulation beigefügt. Sie ist nicht zur Weitergabe an die Bieter bestimmt. Das Gesamtprojektbudget wird getrennt geführt und beträgt derzeit 10,4 Mio. EUR brutto.'),
    ('2 Finanzierung', 'Die Maßnahme wird aus Eigenmitteln des Zweckverbands und einem bewilligten Investitionszuschuss finanziert. Der Zuschuss ersetzt die vergaberechtliche Prüfung nicht. Eine Auftragserteilung oberhalb der losbezogenen Mittel bedarf eines zusätzlichen Beschlusses. Der Eingang eines preislich passenden Angebots führt nicht von selbst zu einer Verpflichtungsermächtigung.'),
    ('3 Vorlage', 'Bitte legen Sie vor Zuschlag die nachvollziehbare Gesamtverpflichtung einschließlich Umsatzsteuer und gegebenenfalls weiterer unvermeidbarer Kosten vor. Die interne Kostenberechnung darf nicht nachträglich als bereits veröffentlichte Bewertungsregel behandelt werden. Der nächste Verbandsausschuss tagt am 22.10.2026.')])

txt(G, '15_Exportprotokoll.txt', 'Protokoll des geschützten Angebotsexports', '2026-10-05',
    'Zweckverband Bildungsforum Harz\nOkerterrasse 9, 38640 Goslar\nVerfahren ZBH-26-31 / Sitzung 05.10.2026\n\n'
    '1 Ablauf\n\n09:59:59: Drei verschlüsselte Container gespeichert. Inhaltszugriff gesperrt.\n'
    '10:00:00: Angebotsfrist abgelaufen. Keine weitere Abgabe in dieser Sitzung.\n'
    '10:03:12: Öffnungsfreigabe durch Miriam Ehlers und David Schütz.\n'
    '10:21:09: Export der lesbaren Hauptangebote in den geschützten Arbeitsordner abgeschlossen.\n\n'
    '2 Prüfsummen der exportierten Hauptangebote\n\n{hashes}\n\n'
    'Die Prüfsummen beziehen sich auf die hier abgelegten PDF-Dateien nach Entschlüsselung, nicht auf die verschlüsselten Transportcontainer. '
    'Eine externe qualifizierte Zeitstempelprüfung wird mit diesem Protokoll nicht bescheinigt. '
    'Die Summen gestatten den Abgleich der Arbeitskopie mit dem Export.\n\n'
    '3 Abschluss\n\nGez. David Schütz, Exportverantwortlicher. Gegenkontrolle: Miriam Ehlers.\n')

book(G, '16_Kostenberechnung_Fassade.xlsx', 'Kostenberechnung F03 vor Ausschreibung', '2026-08-28', 'Kantenraum / Jonas Blume', [dict(
    name='Kostenberechnung',headers=['Position','Leistung','Einheit','Menge','EP netto EUR','Betrag netto EUR'],
    rows=[[r[0],r[1],r[2],r[3],p,f'=ROUND(D{i}*E{i},2)'] for i,(r,p) in enumerate(zip(ITEM_G,[320,1900,680,810,1490,10000,2100,160]),6)],
    tail=[['Netto','','','','','=SUM(F6:F13)'],['Umsatzsteuer',0.19,'','','','=ROUND(F14*B15,2)'],['Brutto','','','','','=F14+F15']],
    notes=['Interne Kostenberechnung vor Angebotsabgabe, keine Angebotswertung.',
           'Gez. Jonas Blume; 28.08.2026. Bezugsmenge: LV F03 Revision 2.'],
    controls={'F14':333360,'F16':396698.4},
    mutation={'cell':'D6','value':241,'result':'F14','expected':333680})])

M = case('bau-rundum-bauzeit-claim-minden',
         'Bauzeitforderung beim Hochwasserlager Wesertor in Minden',
         'Hochwasserlager Wesertor, Neubau Gerätehalle, Minden',
         'Bauzeitforderung mit vereinbartem Ablauf, tatsächlichen Vorgängen, zwei überlappenden Störungen, Wetter- und Personalaufzeichnungen sowie belegten Kostenansätzen und bestrittenen Zeitanteilen.',
         ['Störungszeitraum, konkrete Tätigkeit, kausale Verschiebung und Kostenzeitraum jeweils belegen.',
          'Überlappende Störungen und anderweitige Einsatzmöglichkeiten berücksichtigen, ohne Tage pauschal zu addieren.',
          'Wetter, Unterbesetzung und abweichende Zeitaufzeichnungen als Gegenmaterial würdigen.',
          'Forderung und Anspruchsgrundlage getrennt prüfen; aus der Rechnungsaufstellung keine rechtliche Anerkennung ableiten.'])
MA = 'Logistikverband Wesertor\nDeichbogen 28, 32423 Minden\nbau@wesertor-logistik.example'
MS = 'Porta Hallenbau GmbH\nGewerbeanger 5, 32457 Porta Westfalica\nprojekt@porta-hallenbau.example'
MP = 'Tragwerk Hunte Partnerschaft\nBrückenhof 13, 32423 Minden\nplanung@tragwerk-hunte.example'

doc(M, '01_Bauvertrag_Termine.docx', 'Bauvertrag Gerätehalle Wesertor', '2026-02-09', MA, MS,
    'HW-26 / Los Rohbau', 'gez. Ines Reuter, Verbandsleitung\ngez. Stefan Köster, Geschäftsführer', [
    ('1 Bauleistung', 'Porta Hallenbau übernimmt den Rohbau und die Dachunterkonstruktion der Gerätehalle am Standort Wesertor zum Einheitspreisvolumen von 684.000 EUR netto. Leistungsbeginn ist der 02.03.2026, die Übergabe der geschlossenen Rohbauhülle ist für 15.05.2026 vereinbart. Der Ablaufplan vom 13.02. wird nach gemeinsamer Abstimmung als Vertragsanlage geführt. Arbeitswoche ist Montag bis Freitag; Sonn- und Feiertagsarbeiten sind nicht vorausgesetzt.'),
    ('2 Mitwirkungen', 'Die freigegebene Fundamentplanung soll bis 06.03. und die Leitungsfreigabe für die Südtrasse bis 13.03. vorliegen. Die Freigabe von Nordtrasse und westlichen Fundamenten ist davon getrennt möglich. Der Auftragnehmer organisiert seine Kolonnen und zeigt konkret behinderte Leistungen mit Beginn, Ort und möglicher Ausweicharbeit an. Im Vertrag wird VOB/B vereinbart; ein pauschaler Tagesentschädigungssatz wurde nicht festgelegt.'),
    ('3 Dokumentation', 'Baubesprechungen finden montags statt. Tagesberichte nennen Personal, Geräte und tatsächlich bearbeitete Achsen. Geänderte Termine werden nicht allein durch Eintrag im Bericht Vertragsfristen. Die Bauherrin erteilt technische Freigaben über die Projektleitung; eine Anerkennung zusätzlicher Vergütung bedarf der gesonderten Erklärung der Verbandsleitung.')])

BASE_M = [
 ['V01','Einrichtung','2026-03-02','2026-03-02',''],
 ['V02','Aushub','2026-03-03','2026-03-06','V01'],
 ['V03','Fundamente','2026-03-09','2026-03-13','V02'],
 ['V04','Bodenplatte','2026-03-16','2026-03-20','V03'],
 ['V05','Wände','2026-03-23','2026-03-31','V04'],
 ['V06','Decke','2026-04-01','2026-04-10','V05'],
 ['V07','Erhärtung','2026-04-11','2026-04-17','V06'],
 ['V08','Dachunterkonstruktion','2026-04-20','2026-04-24','V07'],
 ['V09','Abdichtung','2026-04-27','2026-04-30','V08'],
 ['V10','Fassadenanker','2026-05-04','2026-05-08','V09'],
 ['V11','Räumen und Kontrolle','2026-05-11','2026-05-13','V10'],
 ['V12','Übergabe','2026-05-15','2026-05-15','V11'],
]
ACTUAL_M = [
 ['2026-03-02','2026-03-02'],['2026-03-03','2026-03-10'],['2026-03-11','2026-03-30'],
 ['2026-03-19','2026-03-31'],['2026-03-26','2026-04-14'],['2026-04-15','2026-04-28'],
 ['2026-04-29','2026-05-05'],['2026-05-06','2026-05-13'],['2026-05-15','2026-05-22'],
 ['2026-05-26','2026-06-02'],['2026-06-03','2026-06-05'],['2026-06-08','2026-06-08'],
]
book(M, '02_Vertragsablauf.xlsx', 'Vertragsablauf Gerätehalle', '2026-02-13', 'Porta Hallenbau / Stefan Köster', [dict(
    name='Ablauf',headers=['Vorgang','Leistung','Beginn','Ende','Kalendertage','Vorgänger'],
    rows=[[r[0],r[1],{'date':r[2]},{'date':r[3]},f'=D{i}-C{i}+1',r[4]] for i,r in enumerate(BASE_M,6)],
    tail=[],notes=['Datumsbänder zeigen Kalenderbelegung einschließlich Wochenenden und Erhärtung.',
    'Montage an Arbeitstagen; Feiertage 03.04., 06.04., 01.05. und 14.05. sind arbeitsfrei.',
    'V03/V04 abschnittsweise Nord vor Süd. Kolonne Rohbau: sechs Fachkräfte.',
    'gez. Stefan Köster und Ines Reuter; abgestimmt am 13.02.2026.'],
    controls={'E8':5,'E11':10,'E17':1}, mutation={'cell':'D8','date':'2026-03-16','result':'E8','expected':8})])

csv(M, '03_Isttermine.csv', 'Isttermine aus Bauleitungsmeldungen', '2026-06-08', 'Porta Hallenbau / Timo Fricke',
    ['Vorgang','Leistung','Istbeginn','Istende','Erfassungsbeleg','Bearbeiter'],
    [[r[0],r[1],a[0],a[1],f'Tagesabschluss {a[1]} / Fricke','Timo Fricke'] for r,a in zip(BASE_M,ACTUAL_M)])

doc(M, '04_Behinderungsanzeige_Plan.docx', 'Behinderungsanzeige Fundamentplanung', '2026-03-09', MS, MA,
    'HW-26 / Anzeige B01', 'gez. Timo Fricke, Bauleiter', [
    ('1 Fehlende Freigabe', 'Heute um 07:00 Uhr lag die für 06.03. angekündigte Fundamentplanung noch nicht vollständig vor. Das Detail F-17 der südlichen Stützenfüße ist offen. Ohne Bewehrungsführung und Ankermaße können wir dort die Fundamentbewehrung nicht verlegen. Die Aushubarbeiten im Norden werden zunächst fortgesetzt.'),
    ('2 Betroffene Ressourcen', 'Für diese Woche waren sechs Fachkräfte und der Mobilkran vorgesehen. Tatsächlich sind heute vier Fachkräfte anwesend. Wir ordnen drei Personen dem nördlichen Aushub und eine Person der Materialvorbereitung zu. Das südliche Fundamentband war im Vertragsablauf ab heute vorgesehen. Eine belastbare Dauer der Beeinträchtigung können wir ohne Freigabetermin noch nicht nennen.'),
    ('3 Aufforderung', 'Bitte teilen Sie bis morgen 12:00 Uhr mit, wann F-17 freigegeben wird und ob ein abschnittsweises Vorgehen zugelassen ist. Wir behalten uns Kosten- und Terminfolgen vor. Diese Anzeige nennt den gegenwärtigen Zustand; eine konkrete Verlängerungsberechnung wird damit noch nicht vorgelegt. Den Umfang möglicher Ausweicharbeiten halten wir in den Tagesberichten fest.')])

mail(M, '05_Planfreigaben.eml', 'HW-26: F17 Revision C freigegeben', '2026-03-20T11:18:00+01:00',
    'Dr. Rolf Stein <planung@tragwerk-hunte.example>', 'Timo Fricke <projekt@porta-hallenbau.example>',
    'Sehr geehrter Herr Fricke,\n\nF17 Revision C ist seit 11:05 Uhr im Projektraum freigegeben. Die Freigabe betrifft die südlichen Stützenfüße. Die mit Revision B am 10.03. um 16:20 Uhr freigegebenen westlichen und nördlichen Fundamente bleiben unverändert. Nach unserem Planversandbuch wurde Revision B von Ihnen am 11.03. um 06:48 Uhr abgerufen.\n\nDie zusätzliche Ankerlage war nach der Kollisionsprüfung mit der Bestandsleitung erforderlich. Wir bestätigen nicht, dass seit 09.03. sämtliche Fundamentarbeiten stillstanden. Bitte setzen Sie die offenen Abschnitte nach den freigegebenen Maßen fort und melden Sie abweichende Bestandslagen vor dem Betonieren. Eine Kostenübernahme erklären wir als Tragwerksplanung nicht. Diese Nachricht bestätigt die Freigabezeiten; der zeichnerische Plan verbleibt im Projektraum. Es wird kein Plan als E-Mail-Anlage übersandt.\n\nMit freundlichen Grüßen\nDr. Rolf Stein\nTragwerksplaner')

doc(M, '06_Behinderungsanzeige_Leitung.docx', 'Behinderungsanzeige Südtrasse', '2026-03-16', MS, MA,
    'HW-26 / Anzeige B02', 'gez. Timo Fricke, Bauleiter', [
    ('1 Leitungsbereich', 'Die vom Netzbetreiber angekündigte Freischaltung der Leitung im südlichen Arbeitsstreifen ist heute um 07:30 Uhr nicht erfolgt. Der Leitungsbereich ist durch eine rot markierte Absperrung gesichert. Unsere Kolonne darf in diesem Streifen weder ausheben noch Anker setzen. Betroffen sind die südöstlichen Fundamenttaschen S3 und S4 sowie der anschließende Plattenrand.'),
    ('2 Arbeitsablauf', 'Für dieselben südlichen Stützenfüße steht außerdem F17 Revision C noch aus. Im Norden wird die Schalung geschlossen; hier kann weitergearbeitet werden. Wir haben den Kran für diese Umsetzungen genutzt. Die Bodenplatte kann in der geplanten zusammenhängenden Taktfolge nicht hergestellt werden. Welcher Zeitanteil auf die fehlende Zeichnung und welcher auf die Leitung entfällt, wurde vor Ort nicht festgelegt.'),
    ('3 Erforderliche Mitteilung', 'Bitte nennen Sie einen verbindlichen Freischalttermin. Wir melden den Wegfall der Behinderung, sobald Netzbetreiber und Projektleitung die Arbeitsfläche freigeben. Eine veränderte Ausführung der Fundamente in Leitungsnähe erfolgt nicht ohne technische Freigabe. Wir verlangen Ersatz der hieraus entstehenden zusätzlichen Kosten und behalten die Bezifferung vor.')])

doc(M, '07_Netzbetreiber_Freigabe.pdf', 'Freigabe des südlichen Arbeitsstreifens', '2026-03-27',
    'Wesertrasse Netzdienste GmbH\nLeitungsring 11, 32423 Minden\nbetrieb@wesertrasse.example', MA,
    'WT-2617 / Südtrasse Gerätehalle', 'gez. Janne Ahlers, Betriebsverantwortliche', [
    ('1 Umschaltung', 'Die Leitung im südlichen Baufeld wurde am 26.03.2026 um 15:40 Uhr außer Betrieb genommen. Die Endkontrolle erfolgte am 27.03. zwischen 08:00 und 09:00 Uhr. Ab 27.03., 09:15 Uhr, kann der markierte Arbeitsstreifen nach Rücksprache mit der örtlichen Bauleitung wieder bearbeitet werden. Die seit 16.03. geltende Zutrittsbeschränkung wird aufgehoben.'),
    ('2 Verzögerungsgrund', 'Der ursprünglich für 13.03. geplante Termin konnte nicht gehalten werden, weil ein zugesagter Abschaltpunkt im Nachbarbetrieb nicht verfügbar war. Die technische Klärung wurde am 24.03. abgeschlossen. Die Absperrung betraf ausschließlich die Südtrasse, nicht die nördliche Zufahrt oder das westliche Fundamentband.'),
    ('3 Übergabe', 'Herr Fricke wurde telefonisch um 09:20 Uhr informiert. Er erklärte, die Geräte würden zunächst für die laufenden Wandarbeiten benötigt; der südliche Bereich solle am folgenden Arbeitstag wieder besetzt werden. Mit diesem Schreiben wird keine Bewertung der Bauzeitforderung oder der vertraglichen Verantwortlichkeit vorgenommen.')])

txt(M, '08_Bautagebuch.txt', 'Bautagebuch Rohbau Wesertor', '2026-06-08',
    'Porta Hallenbau GmbH | Gewerbeanger 5, 32457 Porta Westfalica\n'
    'Bautagebuch HW-26, Bauleiter Timo Fricke. Auszug der Tagesblätter 09.03. bis 08.06.2026.\n\n'
    '1 März\n\n09.03., 07:00: F17 Süd fehlt; vier Fachkräfte, Norden Aushub. 10.03.: Aushub Nord beendet, Süd offen. '
    '11.03.: drei Fachkräfte, Beginn Fundamente West nach Abruf F17B; Regen ab 13:00, Abdeckung. '
    '12.03.: drei Fachkräfte, sechs Personenstunden Räumen, sonst kein Betonieren; Wasser auf Planum. '
    '13.03.: drei Fachkräfte, Schalung Nord; Abschalttermin entfällt. '
    '16.03.: sechs Fachkräfte; Südtrasse gesperrt, Schalung West. Kran 4,0 Betriebsstunden. '
    '17.03.: Nordbewehrung, Materialumlagerung; Kran 3,5 Stunden. '
    '18.03.: Fundamente West fertig. 19.03.: Bodenplatte Nord begonnen. '
    '20.03.: F17C ab 11:05 freigegeben, Südtrasse weiter gesperrt. '
    '23.03.: sechs Fachkräfte, Bodenplatte Nord, Kran 5,0 Stunden. '
    '24.03.: Bodenplatte Mitte, Kran 4,5 Stunden. 25.03.: Bodenplatte letzter Teil Nord fertig. '
    '26.03.: Wandbeginn Nord. 27.03.: Telefon Freischaltung Süd 09:20; Kolonne an Wänden. '
    '30.03.: südliche Fundamentergänzung ausgeführt, Kran hierfür 2,0 Stunden. '
    '31.03.: südlicher Plattenrand geschlossen, Bodenplatte damit vollständig.\n\n'
    '2 April\n\n14.04.: Wände einschließlich Süd geschlossen. '
    '15.04.: Deckenschalung begonnen. 22.04.: Team auf acht Fachkräfte erhöht. '
    '23.04.: acht Fachkräfte, zusätzliche Schicht dokumentiert. 24.04.: acht Fachkräfte. '
    '27.04.: acht Fachkräfte. 28.04.: Deckenbetonage abgeschlossen. '
    '29.04. bis 05.05.: Erhärtung, tägliche Kontrolle durch zwei Personen.\n\n'
    '3 Mai und Juni\n\n06.05.: Dachunterkonstruktion begonnen. 13.05.: Dachunterkonstruktion fertig. '
    '15.05.: Abdichtung begonnen. 22.05.: Abdichtung geschlossen. 26.05.: Fassadenanker begonnen. '
    '02.06.: Fassadenanker beendet. 03.06.: Räumen und Mängeldurchgang. '
    '05.06.: Reststellen geschlossen. 08.06.: Übergabe um 10:00 Uhr, Nutzer erhält Schlüssel.\n\n'
    'Die Einträge wurden tagesbezogen geführt und hier am 08.06. für den Auftraggeber ausgegeben. '
    'Die Wetterwerte stehen gesondert im Messprotokoll. Zusätzliche Schichtstunden werden im Personalexport geführt. '
    'Gez. Timo Fricke, Bauleiter. Gegenzeichnung des Auftraggebers für diesen Auszug liegt nicht vor.\n')

csv(M, '09_Wettermessungen.csv', 'Baustellenmessung am Container', '2026-03-30', 'Polier Dirk Wendt; Gerät Regenmesser RM2',
    ['Datum','Temperatur_07Uhr_C','Niederschlag_mm_24h','Windmaximum_kmh','Beobachtung','Messort'],[
    ['2026-03-09',4,0,18,'trocken','Container Nord'],['2026-03-10',5,2,21,'feucht','Container Nord'],
    ['2026-03-11',3,18,32,'Regen ab 13 Uhr','Container Nord'],['2026-03-12',2,26,39,'Wasser auf Planum','Container Nord'],
    ['2026-03-13',4,12,28,'Schalung nass','Container Nord'],['2026-03-16',5,1,17,'kein Wasserstau Nord','Container Nord'],
    ['2026-03-20',6,0,20,'trocken','Container Nord'],['2026-03-23',7,0,16,'trocken','Container Nord'],
    ['2026-03-27',8,2,19,'leichter Regen','Container Nord'],['2026-03-30',9,0,14,'trocken','Container Nord'],
    ])

csv(M, '10_Personalstunden.csv', 'Personaldisposition und Stundenexport', '2026-04-30', 'Porta Hallenbau / Personal Jana Brüggemann',
    ['Datum','Soll_Fachkraefte','Ist_Fachkraefte','Regelstunden_gesamt','Zusatzstunden_gesamt','Disposition'],[
    ['2026-03-09',6,4,32,0,'zwei Personen auf Auftrag PW-18'],['2026-03-10',6,4,32,0,'PW-18 nicht beendet'],
    ['2026-03-11',6,3,24,0,'eine Person krank; zwei PW-18'],['2026-03-12',6,3,24,0,'eine Person krank; zwei PW-18'],
    ['2026-03-13',6,3,24,0,'eine Person krank; zwei PW-18'],['2026-03-16',6,6,48,0,'Stammkolonne vollständig'],
    ['2026-04-22',6,8,64,24,'Beschleunigung'],['2026-04-23',6,8,64,32,'Beschleunigung'],
    ['2026-04-24',6,8,64,32,'Beschleunigung'],['2026-04-27',6,8,64,32,'Beschleunigung'],
    ['2026-04-28',6,8,64,24,'Beschleunigung'],
    ])

doc(M, '11_Geraete_und_Gemeinkosten.pdf', 'Kostenbelege Gerätehalle März bis April', '2026-05-05', MS,
    'Geschäftsführung Porta Hallenbau', 'HW-26 / Kostenblatt K05', 'gez. Jana Brüggemann, kaufmännische Projektbetreuung', [
    ('1 Geräte', 'Für den Mobilkran liegt Mietrechnung KM-260331 über 22 berechnete Arbeitstage im März zu 420,00 EUR netto vor. Wochenenden sind nicht berechnet. Die Rechnungssumme beträgt 9.240,00 EUR netto. Die Rechnung unterscheidet nicht zwischen produktivem Einsatz und Stillstand. Nach den Gerätestundenkarten gab es am 16., 17., 23. und 24.03. produktive Hubarbeiten.'),
    ('2 Tagesansätze', 'Die Containerkosten werden aus dem Projektmietvertrag mit 90,00 EUR netto pro berechnetem Arbeitstag angesetzt. Baustelleneinrichtung und Zaun sind mit 45,00 EUR je Arbeitstag intern verteilt. Für Bauleitung und Polier setzt die Kostenstelle gemeinsam 560,00 EUR je Tag an. Diese Personen betreuten während der fraglichen Wochen auch die fortgesetzten Arbeiten im Norden; getrennte Stunden nach Störungsursache sind nicht erfasst.'),
    ('3 Zusatzschichten', 'Die Lohnbuchhaltung weist für 22. bis 28.04. insgesamt 144 zusätzliche Personenstunden aus. Der interne Vollkostensatz beträgt 60,00 EUR je Stunde einschließlich Zuschlägen. Herr Fricke hatte zunächst 160 Stunden angekündigt. Eine Rechnung eines externen Beschleunigungsunternehmens besteht nicht. Die Geschäftsführung möchte außerdem acht Prozent allgemeine Geschäftskosten auf die verlangten verlängerten Tageskosten ansetzen; eine projektbezogene Mehrkostenaufstellung hierzu liegt nicht vor.')])

doc(M, '12_Bauzeitforderung.docx', 'Forderung wegen verlängerter Bauzeit', '2026-06-10', MS, MA,
    'HW-26 / Forderung BZ01', 'gez. Stefan Köster, Geschäftsführer', [
    ('1 Unsere Zeitberechnung', 'Wir fordern wegen der verspäteten Fundamentplanung und der verspäteten Leitungsfreigabe zusätzliche Vergütung. Für den fehlenden Plan setzen wir die zehn Arbeitstage vom 09. bis 20.03. an. Für die gesperrte Südtrasse setzen wir weitere zehn Arbeitstage vom 16. bis 27.03. an. Wir gelangen damit zu zwanzig vergütungspflichtigen Tagen. Die Übergabe erfolgte tatsächlich erst am 08.06. statt am 15.05.2026.'),
    ('2 Kostenforderung', 'Unsere beigefügte Berechnung ergibt 33.684,00 EUR netto, zuzüglich 6.399,96 EUR Umsatzsteuer, insgesamt 40.083,96 EUR. Darin enthalten sind verlängerte Tageskosten, zusätzliche Personalstunden und acht Prozent allgemeine Geschäftskosten auf die Tageskosten. Wir verlangen Zahlung binnen 21 Tagen. Die April-Schichten betrachten wir als notwendige Beschleunigung zur Begrenzung weiteren Verzugs.'),
    ('3 Begründung unserer Forderung', 'Wir halten die Bauherrin für die fehlende Planung und die nicht freigegebene Leitung verantwortlich. Unsere Anzeigen vom 09. und 16.03. liegen vor. Aus unserer Sicht gehen die späteren Verschiebungen auf diese Ereignisse zurück. Dass im Norden gearbeitet wurde, beseitigt nach unserer Auffassung die Belastung durch vorgehaltene Ressourcen nicht. Eine rechtliche Anerkennung der Forderung durch den Verband behaupten wir nicht; über Grundlage und Umfang besteht noch keine Einigung.')])

book(M, '13_Forderungsberechnung.xlsx', 'Berechnung BZ01 des Auftragnehmers', '2026-06-10', 'Porta Hallenbau / Stefan Köster', [dict(
    name='BZ01', headers=['Kostenart','Bezug','Einheit','Anzahl','Satz netto EUR','Betrag netto EUR'],
    rows=[['Mobilkran','B01 und B02','Tag',20,420,'=ROUND(D6*E6,2)'],
          ['Container','B01 und B02','Tag',20,90,'=ROUND(D7*E7,2)'],
          ['Bauleitung und Polier','B01 und B02','Tag',20,560,'=ROUND(D8*E8,2)'],
          ['Zaun und Einrichtung','B01 und B02','Tag',20,45,'=ROUND(D9*E9,2)'],
          ['Zusatzschichten','April','h',160,60,'=ROUND(D10*E10,2)']],
    tail=[['Tageskosten','','','','','=SUM(F6:F9)'],['Geschäftskosten',0.08,'','','','=ROUND(F11*B12,2)'],
          ['Forderung netto','','','','','=F11+F10+F12'],['Umsatzsteuer',0.19,'','','','=ROUND(F13*B14,2)'],
          ['Forderung brutto','','','','','=F13+F14']],
    notes=['Ansätze der Forderung, keine Anerkennung durch die Auftraggeberin.',
           'Tage: zehn wegen Planung zuzüglich zehn wegen Leitung laut Schreiben vom 10.06.',
           'gez. Stefan Köster; Stundenansatz April gemäß erster Bauleitermeldung.'],
    controls={'F11':22300,'F13':33684,'F15':40083.96},
    mutation={'cell':'D10','value':144,'result':'F13','expected':32724})])

mail(M, '14_Erwiderung_Verband.eml', 'HW-26: Forderung BZ01 wird derzeit nicht freigegeben', '2026-06-12T14:35:00+02:00',
    'Ines Reuter <bau@wesertor-logistik.example>', 'Stefan Köster <projekt@porta-hallenbau.example>',
    'Sehr geehrter Herr Köster,\n\nwir können Ihre Forderung BZ01 auf Grundlage der bisherigen Unterlagen nicht zur Zahlung freigeben. Sie rechnen Plan- und Leitungstage nebeneinander ab, obwohl sich beide Anzeigen auf denselben Südabschnitt beziehen. Bitte erläutern Sie anhand des Vertragsablaufs, welche konkrete Tätigkeit wann nicht ausgeführt werden konnte und wie sie den Übergabetermin beeinflusst hat.\n\nDie Personalübersicht zeigt vom 09. bis 13.03. eine kleinere Kolonne als vorgesehen. Zudem wurde bei Regen am 12.03. nicht betoniert. Die Gerätestunden im Norden widersprechen einem vollständigen Kranstillstand. Ihre 160 Zusatzstunden stimmen nicht mit den 144 Stunden aus der Lohnbuchhaltung überein. Das bedeutet nicht, dass wir sämtliche Mehrkosten ausschließen; eine Zuordnung fehlt uns jedoch. Bitte senden Sie eine nachvollziehbare Ergänzung bis 19.06.2026.\n\nMit freundlichen Grüßen\nInes Reuter\nVerbandsleitung')

doc(M, '15_Besprechung_Beschleunigung.docx', 'Besprechung zu den Deckenschichten', '2026-04-20', MA, MS,
    'HW-26 / Besprechung 12', 'gez. Ines Reuter, Protokoll\nZur Kenntnis: Timo Fricke', [
    ('1 Stand', 'Die Besprechung fand um 09:00 Uhr am Container statt. Die Deckenarbeiten hatten am 15.04. begonnen. Herr Fricke erklärte, dass mit der bisherigen Besetzung eine Fertigstellung der Decke vor Ende April unsicher sei. Frau Reuter bat um Vorschläge zur Begrenzung der weiteren Verschiebung, ohne einen neuen Übergabetermin verbindlich zu vereinbaren.'),
    ('2 Zusätzliche Schichten', 'Herr Fricke schlug zwei zusätzliche Fachkräfte und verlängerte Schichten vom 22. bis 28.04. vor. Er rechnete zunächst mit 160 zusätzlichen Personenstunden. Frau Reuter erklärte, sie werde die Auswirkungen mit der Verbandsleitung besprechen. Eine Vergütungszusage gab sie nicht ab. Herr Fricke sagte, die Firma werde die Einteilung wegen der Betonbestellung bereits am selben Tag veranlassen.'),
    ('3 Nachweise', 'Die tatsächlich geleisteten Zusatzstunden sollen aus der Zeiterfassung kommen. Der Auftragnehmer wird angeben, welche Regelstunden ohnehin zur Vertragserfüllung angefallen wären. Ein gesonderter Beschleunigungspreis wurde in der Besprechung nicht verhandelt. Die Ursache einzelner Verschiebungen blieb zwischen den Beteiligten streitig.')])

M['pieces'].append(dict(file='16_Baufeldskizze.png', title='Baufeldskizze Gerätehalle mit Nordtakt und Südtrasse',
    date='2026-03-16', drawing='minden', owner='Tragwerk Hunte / Dr. Rolf Stein'))

N = case('bau-rundum-nachtrag-northeim',
         'Entwässerungsänderung am Rettungszentrum Leinetor in Northeim',
         'Rettungszentrum Leinetor, Entwässerung des Übungshofs, Northeim',
         'Angebot für eine geänderte Rohrdimension mit unklarer Reichweite einer Baustellenanweisung, abschnittsweisen Mengen, ursprünglicher Preisermittlung, aktuellem Lieferangebot und noch ausstehender Bauherrenentscheidung.',
         ['Änderungswunsch, technische Anweisung, Vertretungsmacht und Preisvereinbarung anhand getrennter Belege beurteilen.',
          'Geänderte, entfallende und unveränderte Mengen sowie Preisbestandteile nachvollziehbar abgrenzen.',
          'Fristen und offene Entscheidungen aus dem Schriftverkehr führen, ohne bereits eine Beauftragung oder einen Anspruch zu unterstellen.'])
NA = 'Rettungsdienst Leinetor gGmbH\nLeineanger 40, 37154 Northeim\nbau@leinetor-rettung.example'
NS = 'Rhume Tiefbau GmbH\nKiesbogen 18, 37154 Northeim\nangebot@rhume-tiefbau.example'
NP = 'Wasserlinie Ingenieure PartG\nMühlenwinkel 6, 37154 Northeim\nplanung@wasserlinie.example'

doc(N, '01_Bauauftrag_Entwaesserung.docx', 'Bauauftrag Entwässerung Übungshof', '2026-07-20', NA, NS,
    'RL-26 / Auftrag T02', 'gez. Dr. Gesa Lindner, Geschäftsführerin\ngez. Uwe Brinkmann, Geschäftsführer', [
    ('1 Leistung und Termine', 'Rhume Tiefbau übernimmt die Entwässerungsarbeiten am Übungshof des Rettungszentrums Leinetor. Vertragsgrundlage sind das Leistungsverzeichnis T02 vom 15.07.2026 und die bestätigte Kalkulation des Auftragnehmers. Die Ausführung ist für 14.09. bis 16.10.2026 vorgesehen. Die Zufahrt zum Rettungsbetrieb muss währenddessen auf mindestens 3,50 m Breite freigehalten werden.'),
    ('2 Abrechnung', 'Abgerechnet wird nach den vereinbarten Einheitspreisen und gemeinsam festgestellten Mengen. Die Bodenmengen sind im gewachsenen Zustand zu bestimmen. Rohrlängen werden entlang der Leitungsachse zwischen den Außenkanten der Schächte gemessen. Bögen und Muffen sind in den Rohrpreisen enthalten. Umsatzsteuer wird mit 19 Prozent berechnet. VOB/B ist nach der ausgehändigten Vertragsfassung vereinbart.'),
    ('3 Weisungen', 'Wasserlinie betreut Planung und örtliche Bauüberwachung. Die Bauüberwachung darf technische Einzelheiten innerhalb der beauftragten Leistung koordinieren. Preisänderungen und zusätzliche Leistungen werden durch die Geschäftsführerin der Auftraggeberin bestätigt. Maßnahmen zur unmittelbaren Gefahrenabwehr sind unverzüglich zu melden. Eine Vollmacht zum Abschluss beliebiger Nachtragsvereinbarungen erhält die Bauüberwachung mit diesem Vertrag nicht.')])

LV_N=[['01.010','Rohr DN150 einschließlich Bettung','m',300,84.71],
      ['01.020','Kontrollschacht','St',6,1250],['02.010','Aushub Leitungsgraben','m³',210,24.5],
      ['02.020','Bodenabfuhr','t',180,19],['03.010','Pflaster wiederherstellen','m²',190,48],
      ['04.010','Einrichtung und Verkehrssicherung','psch',1,6200]]
doc(N, '02_Leistungsverzeichnis.pdf', 'Leistungsverzeichnis T02', '2026-07-15', NP, NA,
    'RL-26 / T02 / Preisstand Angebot 17.07.', 'gez. Dipl.-Ing. Hannah Küster, Projektleitung', [
    ('1 Entwässerungssystem', 'Vorgesehen ist eine Freigefälleleitung DN150 mit sechs Kontrollschächten. Die Planung vom 15.07. enthält 300 m vorläufige Leitungsachse. Nach Bestandsaufnahme können sich die Längen verändern. Eine Vergrößerung des Durchmessers ist nicht Bestandteil der Position 01.010. Bestehende Anschlussstutzen sind vor Bestellung der Rohrteile aufzunehmen.'),
    ('2 Preisumfang', 'Der Einheitspreis der Rohrposition umfasst Lieferung, Bettung, Verlegung, Muffen, Bögen und Verdichtung im Rohrbereich. Aushub, Abfuhr und Pflaster werden in den gesonderten Positionen geführt. Eine erneute Baustelleneinrichtung ist bei abschnittsweiser Herstellung innerhalb des vereinbarten Zeitraums nicht zusätzlich vorgesehen.'),
    ('3 Ausführung', 'Der nördliche Rettungszugang wird zuerst bearbeitet. Erst nach Wiederherstellung der befahrbaren Fläche darf der südliche Hof geöffnet werden. Die Rohre werden vor Verfüllung gemeinsam aufgenommen. Eine Anpassung des LV durch handschriftlichen Eintrag auf dem Aufmaß ersetzt keine Preisvereinbarung.')],
    (['Pos.','Leistung','Einheit','Menge','EP netto EUR'],LV_N))

book(N, '03_Urkalkulation_Rohr.xlsx', 'Preisermittlung Rohr DN150', '2026-07-17', 'Rhume Tiefbau / Uwe Brinkmann', [dict(
    name='DN150',headers=['Bestandteil','Bezug','Einheit','Ansatz je m','Satz netto EUR','Kosten je m EUR'],
    rows=[['Lohn','Kolonne','h',.6,38,'=ROUND(D6*E6,2)'],['Rohrmaterial','DN150','m',1,34,'=ROUND(D7*E7,2)'],
          ['Gerät','Kleingerät','h',.2,48,'=ROUND(D8*E8,2)'],['Transport','Zuordnung','psch/m',1,6,'=ROUND(D9*E9,2)']],
    tail=[['Einzelkosten','','','','','=SUM(F6:F9)'],['Zuschlag',.17,'','','','=ROUND(F10*B11,2)'],
          ['Einheitspreis','','','','','=F10+F11']],
    notes=['Zuschlag auf Einzelkosten einschließlich Baustellen- und Geschäftskosten sowie Wagnis/Gewinn.',
           'Preisermittlung zum Angebot 17.07.2026; gez. Uwe Brinkmann.'],
    controls={'F10':72.4,'F11':12.31,'F12':84.71},
    mutation={'cell':'E7','value':35,'result':'F12','expected':85.88})])

mail(N, '04_Aenderungswunsch.eml', 'Leinetor: stärkere Entwässerung im südlichen Hof', '2026-09-17T16:25:00+02:00',
    'Dr. Gesa Lindner <bau@leinetor-rettung.example>', 'Hannah Küster <planung@wasserlinie.example>',
    'Sehr geehrte Frau Küster,\n\nnach der Vorführung mit zwei Waschfahrzeugen möchten wir prüfen lassen, ob die Entwässerung im südlichen Übungshof größer dimensioniert werden muss. Gemeint ist zunächst der südliche Zulauf zwischen N2 und S4. Der nördliche Rettungszugang soll nach Möglichkeit unverändert bleiben. Bitte lassen Sie technische Notwendigkeit, Kosten und Auswirkungen auf den 16.10. feststellen.\n\nEin Nachtragsbudget habe ich noch nicht freigegeben. Ich bin vom 21. bis 28.09. nicht im Haus. Frau Arens bereitet die Entscheidung vor; eine Bestellung soll erst nach der Aufstellung der Varianten erfolgen. Bitte halten Sie den Rettungsweg befahrbar und melden Sie ein Sicherheitsproblem sofort. Unser Wunsch nach Prüfung ist noch keine Zustimmung zu einem bestimmten Gesamtpreis oder zu einer Umstellung sämtlicher Leitungen.\n\nMit freundlichen Grüßen\nDr. Gesa Lindner\nGeschäftsführerin')

doc(N, '05_Zustaendigkeit_Bauprojekt.docx', 'Zuständigkeit während der Abwesenheit', '2026-09-18', NA,
    'Miriam Arens und Wasserlinie Ingenieure', 'RL-26 / Organisationsmitteilung 09', 'gez. Dr. Gesa Lindner, Geschäftsführerin', [
    ('1 Interne Aufgaben', 'Miriam Arens koordiniert während meiner Abwesenheit vom 21. bis 28.09. das Bauprojekt und führt die Gespräche mit Planung und Auftragnehmern. Sie darf Unterlagen anfordern und Termine abstimmen. Ihr intern zugeteilter Ausgabenrahmen für laufende Beschaffungen beträgt 10.000 EUR netto je Vorgang. Eine Aufteilung zusammengehöriger Beschaffungen zur Einhaltung dieses Rahmens ist nicht zulässig.'),
    ('2 Nachträge', 'Bauliche Nachträge mit Eingriffen in die genehmigte Entwässerung werden der Geschäftsführung vorgelegt. Frau Arens erhält hierfür keine eigenständige Freigabe. Die technische Überwachung darf auf Gefahren für den Rettungsbetrieb reagieren und hat die Geschäftsführung umgehend zu informieren. Eine Mengen- oder Preisbestätigung ist gesondert zu dokumentieren.'),
    ('3 Weitergabe', 'Diese Mitteilung geht intern an Frau Arens und an Wasserlinie. Ob und wann Rhume Tiefbau eine Kopie erhält, ist in der Projektakte zu vermerken. Eine Empfangsbestätigung des Auftragnehmers liegt bei Unterzeichnung nicht vor. Die allgemeine Vertragsregel zu Preisänderungen bleibt unverändert.')])

csv(N, '06_Aufmass_Leitungsachsen.csv', 'Achslängen nach Bestandsaufnahme', '2026-09-21', 'Wasserlinie / Vermesser Falk Ernst',
    ['Abschnitt','Von','Bis','Länge_m','DN_LV','Messverfahren','Freigabestand'],[
    ['N1','Schacht N1','Schacht N2',86,150,'Achse außen zu außen','bestehende Planung'],
    ['S1','Schacht N2','Schacht S2',64,150,'Achse außen zu außen','Änderungswunsch Süd'],
    ['S2','Schacht S2','Schacht S4',72,150,'Achse außen zu außen','Änderungswunsch Süd'],
    ['N2','Schacht S4','Einleitung E1',58,150,'Achse außen zu außen','Bestandsanschluss prüfen'],
    ])

doc(N, '07_Lieferangebot_DN200.pdf', 'Lieferangebot Rohrsystem DN200', '2026-09-22',
    'Rohrkontor Südniedersachsen GmbH\nLagerwinkel 19, 37574 Einbeck\nverkauf@rohrkontor.example', NS,
    'RK-26221 / Lieferung Leinetor', 'gez. Silke Damm, Verkauf', [
    ('1 Materialangebot', 'Wir bieten das angefragte Rohrsystem DN200 einschließlich der von Ihnen genannten Standardmuffen zum Nettopreis von 49,50 EUR je Meter an. Zugrunde liegt eine Gesamtbestellung von 280 m. Bei einer Bestellung von nur 136 m beträgt der Nettopreis 52,00 EUR je Meter. Sonderübergänge auf vorhandene DN150-Stutzen sind nicht in diesen Preisen enthalten und werden nach Maß angeboten.'),
    ('2 Lieferung und Bindung', 'Das Angebot ist bis 28.09.2026, 12:00 Uhr, verbindlich. Bei Bestellung bis zu diesem Zeitpunkt können wir am 01.10. ausliefern. Nach Fristablauf sind Preis und Liefertermin erneut abzufragen. Eine bevorratete Menge wurde noch nicht für Sie reserviert. Die Lieferung erfolgt frei Baustelle bei vollständiger Abnahme in einem Abruf.'),
    ('3 Bestandsware', 'Von den bereits gelieferten 300 m DN150 können ungeöffnete Bundware und unbeschädigte Formteile nach Prüfung zurückgenommen werden. Vorläufig kalkulieren wir eine Bearbeitungspauschale von zehn Prozent des ursprünglichen Materialwerts. Wir haben noch keine Mengenliste zur Rücknahme und erteilen daher keine Gutschrift. Dieser Punkt ist nicht im neuen Meterpreis verrechnet.')])

book(N, '08_Nachtragsangebot_N03.xlsx', 'Angebotskalkulation N03 DN200', '2026-09-23', 'Rhume Tiefbau / Uwe Brinkmann', [dict(
    name='N03',headers=['Bestandteil','Bezug','Einheit','Ansatz','Satz netto EUR','Betrag netto EUR'],
    rows=[['Lohn neu','je m','h',.85,42,'=ROUND(D6*E6,2)'],['Rohr DN200','je m','m',1,49.5,'=ROUND(D7*E7,2)'],
          ['Gerät neu','je m','h',.3,52,'=ROUND(D8*E8,2)'],['Transport','je m','psch/m',1,8.5,'=ROUND(D9*E9,2)']],
    tail=[['Einzelkosten je m','','','','','=SUM(F6:F9)'],['Zuschlag neu',.18,'','','','=ROUND(F10*B11,2)'],
          ['Neuer EP je m','','','','','=F10+F11'],['Rohr DN200','gesamt','m',280,'=F12','=ROUND(D13*E13,2)'],
          ['Entfall DN150','gesamt','m',280,84.71,'=-ROUND(D14*E14,2)'],
          ['Neue Einrichtung','gesamt','psch',1,1850,'=ROUND(D15*E15,2)'],
          ['Wartezeit','22. bis 25.09.','Tag',4,640,'=ROUND(D16*E16,2)'],
          ['Mehrforderung netto','','','','','=SUM(F13:F16)'],['Umsatzsteuer',.19,'','','','=ROUND(F17*B18,2)'],
          ['Mehrforderung brutto','','','','','=F17+F18']],
    notes=['Angebot betrifft sämtliche 280 m; Gutschrift Altmaterial ist noch nicht vereinbart.',
           'Einrichtungs- und Wartekosten zusätzlich verlangt. Bindung: 28.09.2026, 10:00 Uhr.',
           'gez. Uwe Brinkmann; 23.09.2026.'],
    controls={'F10':109.3,'F12':128.97,'F17':16802.8,'F19':19995.33},
    mutation={'cell':'D13','value':136,'result':'F17','expected':-1768.88})])

doc(N, '09_Begleitschreiben_N03.docx', 'Nachtragsangebot zur Rohrdimension', '2026-09-23', NS, NA,
    'RL-26 / N03', 'gez. Uwe Brinkmann, Geschäftsführer', [
    ('1 Leistungsänderung', 'Wir bieten die Umstellung der nach aktuellem Aufmaß verbleibenden 280 m Leitung auf DN200 an. Die hierfür verlangte Mehrvergütung beträgt 16.802,80 EUR netto zuzüglich Umsatzsteuer. Unsere Kalkulation ist in der Datei 08_Nachtragsangebot_N03.xlsx enthalten. Der neue Rohrpreis wird auf sämtliche Abschnitte angesetzt; der ursprüngliche Preis für 280 m DN150 wird abgezogen.'),
    ('2 Anlass und Kosten', 'Frau Küster sagte am 21.09. auf der Baustelle, wir sollten die größere Dimension vorsehen und die offene Trasse sichern. Wir haben daraufhin den Lieferanten angefragt und die Verlegung zunächst zurückgestellt. Wir verstehen diese Aussage als Anweisung zum geänderten Bauablauf. Ob Frau Küster für die gesamte Umstellung vertretungsberechtigt war, ist zwischen uns noch nicht schriftlich geklärt.'),
    ('3 Entscheidungstermin', 'Bitte bestätigen Sie das Angebot bis 28.09.2026, 10:00 Uhr, damit wir das Lieferangebot rechtzeitig abrufen können. Andernfalls müssen Preis und Termin neu abgefragt werden. Die vier Wartezeittage vom 22. bis 25.09. setzen wir bereits in unserem Angebot an. Eine verbindliche Einigung über diese Wartezeit besteht noch nicht. Eine Ausführung bis 16.10. können wir erst nach Festlegung der Anschlussdetails erneut zusagen.')])

txt(N, '10_Baustellenanweisung_21_September.txt', 'Baustellennotiz zur Südtrasse', '2026-09-21',
    'Wasserlinie Ingenieure PartG\nMühlenwinkel 6, 37154 Northeim\nRL-26 / Baustellennotiz 21.09.2026, 08:15 bis 08:40 Uhr\n\n'
    '1 Gespräch vor Ort\n\nHannah Küster sprach mit Polier Lars Meier und Vermesser Falk Ernst. '
    'Küster sagte: Für den südlichen Übungshof sollen wir die größere Dimension vorsehen. '
    'Die offene Trasse ist zunächst zu sichern; vor Bestellung brauche ich die Mengen und die Anschlussdetails. '
    'Meier erwiderte, dass sich eine Umstellung nur einheitlich lohne und die Kolonne bei fehlender Bestellung nicht weiter verlegen könne. '
    'Küster verwies auf die noch erforderliche Entscheidung von Frau Lindner.\n\n'
    '2 Baustellensicherung\n\nIm Bereich der Rettungszufahrt fehlten um 08:20 Uhr zwei Absperrbaken. '
    'Küster verlangte ihre sofortige Ergänzung. Meier stellte die Baken um 08:30 Uhr auf. '
    'Eine unmittelbare Gefahr durch zu kleine Rohrdurchmesser wurde beim Ortstermin nicht festgestellt. '
    'Der nördliche Abschnitt war noch nicht mit Rohren belegt.\n\n'
    '3 Rückmeldung\n\nMeier bat um eine schriftliche Bestätigung der kompletten Umstellung. '
    'Küster hat auf dieser Notiz nur die Sicherungsmaßnahme und den Gesprächsinhalt abgezeichnet. '
    'Eine Bestellung über 280 m oder ein Preis wurden nicht eingetragen.\n\n'
    'Gez. Hannah Küster, 21.09.2026, 10:05 Uhr.\n'
    'Lars Meier ergänzte am 22.09.: Nach meinem Verständnis sollten wir DN200 ausführen; die Preisfrage blieb offen.\n')

doc(N, '11_Technische_Stellungnahme.docx', 'Rohrdimensionen und Bestandsanschlüsse', '2026-09-24', NP, NA,
    'RL-26 / Technischer Bericht E04', 'gez. Hannah Küster, Projektleitung', [
    ('1 Südlicher Übungshof', 'Die zusätzliche gleichzeitige Nutzung durch zwei Waschfahrzeuge wurde in der bisherigen Betriebsbeschreibung nicht genannt. Für die südlichen Abschnitte zwischen N2 und S4 ist die Bemessung deshalb zu ergänzen. Die dort aufgenommenen Achslängen betragen 64 m und 72 m. Wir schlagen vor, hierfür die größere Dimension DN200 technisch weiterzuverfolgen. Eine abgestimmte Entwässerungsberechnung liegt noch nicht vor.'),
    ('2 Übrige Abschnitte', 'Die nördliche Leitung N1 bis N2 ist 86 m lang. Der Auslauf S4 bis E1 beträgt 58 m und endet an einem vorhandenen DN150-Stutzen. Ein Einbau von DN200 in allen vier Abschnitten löst die Anschlussfrage daher nicht ohne weitere Bauteile. Das Angebot Rhume umfasst 280 m, während der Bauherrenwunsch zunächst den südlichen Hof betraf.'),
    ('3 Einordnung meiner Aussage', 'Meine Baustellenaussage vom 21.09. sollte eine gesicherte Trasse und die Vorbereitung einer Variante bewirken. Ich habe weder einen Preis verhandelt noch die zusätzliche Wartezeit gebilligt. Die sofort angeordnete Sicherung betraf zwei fehlende Baken. Frau Arens erhält die Unterlagen zur Vorlage bei Frau Lindner. Über die Ausführung kann erst nach technischer Abstimmung und Freigabe entschieden werden.')])

mail(N, '12_Beschaffung_Rueckfrage.eml', 'N03: Preisbindung und Rücknahme DN150', '2026-09-25T09:40:00+02:00',
    'Miriam Arens <projekt@leinetor-rettung.example>', 'Uwe Brinkmann <angebot@rhume-tiefbau.example>',
    'Sehr geehrter Herr Brinkmann,\n\nwir haben das Angebot erhalten. Bitte erläutern Sie die Erhöhung des Zuschlags von 17 auf 18 Prozent sowie der Lohn- und Geräteansätze gegenüber der ursprünglichen Preisermittlung. Der Lieferant nennt unterschiedliche Preise für 136 m und 280 m. Wir benötigen die Auswirkungen beider Mengen und den Umgang mit bereits beschafftem DN150-Material. Eine Rücknahmegutschrift ist bisher nicht eingerechnet.\n\nBitte belegen Sie auch, welche Mannschaft und Geräte vom 22. bis 25.09. tatsächlich nicht anderweitig eingesetzt werden konnten. Ich kann den Nachtrag nicht freigeben. Frau Lindner kehrt am 29.09. zurück; damit liegt Ihre Angebotsfrist davor. Können Sie die Bindung bis zur Besprechung am 30.09. verlängern? Diese Anfrage ist keine Bestellung.\n\nMit freundlichen Grüßen\nMiriam Arens\nProjektkoordination')

doc(N, '13_Aufnahmeskizze_Begleitblatt.pdf', 'Aufnahme der Schächte und Anschlüsse', '2026-09-21', NP, NS,
    'RL-26 / Vermessungsblatt V07', 'gez. Falk Ernst, Vermessung\nMengen gesehen: Lars Meier', [
    ('1 Aufnahme', 'Die Aufnahme erfolgte am 21.09. von 07:15 bis 08:10 Uhr. Gemessen wurden Achslängen zwischen den Außenkanten der Schächte. Es ergeben sich 86,00 m, 64,00 m, 72,00 m und 58,00 m, zusammen 280,00 m. Die zuvor ausgeschriebenen 300 m waren aus der frühen Planung abgeleitet. Rohrmaterial war in diesen Abschnitten noch nicht verlegt.'),
    ('2 Bestandsstutzen', 'Am Auslauf E1 wurde ein vorhandener Anschluss DN150 sichtbar. Der Durchmesser wurde am freigelegten Stutzen abgelesen. Die äußere Oberfläche war verschmutzt, ein Herstellerzeichen nicht erkennbar. Die Leitung wurde nicht vollständig freigelegt. Ein weiterer Übergang darf nicht allein aus dem Nennmaß des neu zu bestellenden Rohrs abgeleitet werden.'),
    ('3 Unterzeichnung', 'Herr Meier bestätigt die gemeinsam gemessenen Längen. Zur künftigen Rohrdimension und zur Vergütung wurde keine Vereinbarung unterzeichnet. Der Rohdatenexport 06_Aufmass_Leitungsachsen.csv enthält dieselben vier Abschnitte; im Feld Änderungswunsch wird der Stand der Besprechung bezeichnet, keine technische Genehmigung.')])

csv(N, '14_Terminnotizen.csv', 'Terminnotizen Nachtrag N03', '2026-09-25', 'Rettungsdienst Leinetor / Miriam Arens',
    ['Ereignis','Datum','Uhrzeit','Urheber','Status','Bezug'],[
    ['Änderungsprüfung angefragt','2026-09-17','16:25','Lindner','versandt','04_Aenderungswunsch.eml'],
    ['Angebot Auftragnehmer bindend bis','2026-09-28','10:00','Brinkmann','Frist benannt','09_Begleitschreiben_N03.docx'],
    ['Lieferangebot bindend bis','2026-09-28','12:00','Damm','Frist benannt','07_Lieferangebot_DN200.pdf'],
    ['Geschäftsführung wieder erreichbar','2026-09-29','09:00','Lindner','angekündigt','05_Zustaendigkeit_Bauprojekt.docx'],
    ['Entscheidungsbesprechung','2026-09-30','11:00','Arens','eingeladen','16_Besprechungseinladung.eml'],
    ['Vertraglicher Fertigstellungstermin','2026-10-16','16:00','Bauvertrag','unverändert','01_Bauauftrag_Entwaesserung.docx'],
    ])

doc(N, '15_Nachtragsregister.docx', 'Nachtragsregister Entwässerung', '2026-09-25', NA, 'Geschäftsführung und Projektkoordination',
    'RL-26 / Registerstand 25.09.', 'gez. Miriam Arens, Projektkoordination', [
    ('1 Erfassungsstand', 'Das Register wird von der Projektkoordination geführt. N01 betraf den zusätzlichen Schachtdeckel und wurde am 02.09. mit 860,00 EUR netto bestätigt. N02 betraf eine nicht ausgeführte Asphaltfläche und wurde am 10.09. mit minus 1.240,00 EUR netto vereinbart. Beide Vorgänge bleiben von N03 unberührt. Ihre Unterlagen liegen in den früheren Projektabschnitten und sind nicht Gegenstand der Rohrdimensionierung.'),
    ('2 Eingang N03', 'Das Angebot N03 über 16.802,80 EUR netto wurde am 23.09. um 15:20 Uhr erfasst. Es umfasst nach dem Begleitschreiben die Umstellung aller 280 m, eine neue Einrichtung und vier Tage Wartezeit. Als bisheriger Anlass sind der Bauherrenwunsch vom 17.09. und die Baustellenbesprechung vom 21.09. hinterlegt. Eine Bestellnummer wurde nicht vergeben.'),
    ('3 Offene Entscheidung', 'Technische Berechnung, Anschlussdetails und Rücknahme Altmaterial stehen aus. Die Bindungsfrist soll nach unserer Anfrage verlängert werden; eine Antwort ist noch nicht eingegangen. Frau Lindner entscheidet nach ihrer Rückkehr über den Umfang. Im Register wird für N03 kein bestätigter Betrag ausgewiesen. Das Feld Entscheidung bleibt bis zu einer dokumentierten Erklärung offen.')])

mail(N, '16_Besprechungseinladung.eml', 'Leinetor: N03 am 30.09. um 11 Uhr', '2026-09-25T14:10:00+02:00',
    'Miriam Arens <projekt@leinetor-rettung.example>', 'Hannah Küster <planung@wasserlinie.example>',
    'Sehr geehrte Frau Küster,\n\nFrau Lindner möchte die Rohränderung am 30.09. um 11:00 Uhr im Projektbüro besprechen. Bitte bringen Sie den Stand der technischen Berechnung und eine Darstellung der Anschlussfrage E1 mit. Die von Herrn Brinkmann angebotenen 280 m stimmen zwar mit dem aktuellen Gesamtaufmaß überein, umfassen aber mehr als den zunächst angefragten Südabschnitt.\n\nIch lege das aktuelle Lieferangebot und das Begleitschreiben des Auftragnehmers bei. Die Preisbindung endet vor unserem Termin. Die von mir erbetene Verlängerung ist noch nicht bestätigt. Bitte lösen Sie bis zur Entscheidung keine Materialbestellung in unserem Namen aus. Die vertragliche Sicherung des Rettungswegs ist selbstverständlich fortzuführen; für eine erneute Baustelleneinrichtung liegt noch keine Zustimmung vor.\n\nMit freundlichen Grüßen\nMiriam Arens\nProjektkoordination', ['07_Lieferangebot_DN200.pdf','09_Begleitschreiben_N03.docx'])

doc(L, '16_Baubesprechung_30_Juli.docx', 'Baubesprechung Werkflügel', '2026-07-30', LP, LA, 'QB-26 / Besprechung 18',
    'gez. Kirsten Seidel, Protokollführung', [
    ('1 Teilnehmer und Termin', 'Die Besprechung fand von 08:00 bis 08:45 Uhr im Werkflügel statt. Teilgenommen haben Frau Seidel, Herr Brandt und der Hausmeister Herr Öztürk. Frau Rößler war nicht anwesend. Die nächste Baustellenrunde ist für 06.08., 09:00 Uhr vereinbart.'),
    ('2 Pumpeneinsatz', 'Herr Brandt verlangt die Bestätigung von zwölf Pumpentagen. Frau Seidel erinnert sich an die Bitte, eine akute Wasseransammlung zu beseitigen, nicht an eine Bestellung bis 17.07. Sie will die Ursache der geöffneten Leitung anhand der Tagesberichte klären. Herr Öztürk berichtet, dass am Wochenende 11./12.07. kein Schlüssel für den Pumpenraum ausgegeben wurde; ob die Pumpe ohne Zutritt lief, weiß er nicht.'),
    ('3 Rechnungsunterlagen', 'Das Juli-Aufmaß wird am folgenden Morgen aufgenommen. Herr Brandt kündigt an, angelieferte Stützen mit abzurechnen. Frau Seidel bittet um getrennte Angabe von Lager- und Einbaumengen. Eine Einigung hierzu wurde nicht erzielt. Zur Sockelnacharbeit soll Herr Brandt einen Termin anbieten, bevor der Graben verfüllt wird. In dieser Besprechung wurden keine neuen Preise vereinbart.')])
