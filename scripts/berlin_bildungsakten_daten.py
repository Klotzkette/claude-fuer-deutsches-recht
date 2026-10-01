"""Vollständige, fiktive Belege für sechs Berliner Bildungsakten."""

def D(file, title, date, sender, recipient, body, **extra):
    return dict(file=file, title=title, date=date, sender=sender, recipient=recipient, body=body.strip(), **extra)

def E(file, title, date, sender, recipient, body):
    return dict(file=file, title=title, date=date, **{'from': sender, 'to': recipient}, body=body.strip())

def T(file, title, date, body):
    return dict(file=file, title=title, date=date, body=body.strip())

def X(file, title, sheets):
    return dict(file=file, title=title, sheets=sheets)

SCHULE = 'berliner-schulrecht-eltern-schueler'
HOCHSCHULE = 'berliner-hochschulrecht-professoren'
CASES = []

CASES.append(dict(slug='berlin-kita-sonnenkringel', title='Kita Sonnenkringel und der frühe Arbeitsbeginn', plugin=SCHULE, date='19.08.2026', client='Mara und Felix Aydin für ihre Tochter Leni',
 summary='Leni ist zwei Jahre alt und soll ab September eine Kita besuchen. Ein Gutschein liegt vor. Der angebotene Platz, die Eingewöhnung und die neuen Arbeitszeiten ihrer Eltern passen noch nicht zusammen.',
 assignment='Die Eltern bitten um Unterstützung bei einer verlässlich nutzbaren Betreuung ab September und der Klärung des Gutscheinumfangs. Die kleine Kita Sonnenkringel soll nach Möglichkeit erhalten bleiben.',
 documents=[
D('01_Auftrag_Familie_Aydin.docx','Betreuung für Leni ab September','19.08.2026','Mara und Felix Aydin\nWeichselstraße 42, 12045 Berlin','Rechtsanwältin Jule Morgen\nKanzlei am Kanal, Berlin', '''Sehr geehrte Frau Morgen,

wir bitten Sie, uns bei einem Kitaplatz für unsere Tochter Leni, geboren am 14.03.2024, zu unterstützen. Mara beginnt am 01.09.2026 wieder mit der Arbeit. Der Gutschein nennt sieben bis neun Stunden. Die angebotene Kita öffnet erst um 8 Uhr, Maras Frühdienst beginnt um 7 Uhr.

Am liebsten möchten wir Leni in der Sonnenkringel lassen. Sie war beim Kennenlernen sofort bei der Holzeisenbahn zu Hause. Die Leitung bemüht sich, kann aber vor Oktober keinen sicheren Platz zusagen. Felix kann Leni an manchen Tagen bringen, seine Baustellentermine beginnen jedoch zweimal in der Woche ebenfalls früh.

Bitte klären Sie, was wir jetzt von wem verlangen können und welches Schreiben zuerst nötig ist. Wir möchten die Zusammenarbeit mit den Einrichtungen freundlich halten. Einer kostenpflichtigen Übergangslösung haben wir noch nicht zugestimmt. Maras Mutter hilft in der Eingewöhnung, übernimmt aber keine dauerhafte Betreuung.

Mit freundlichen Grüßen
Mara und Felix Aydin'''),
D('02_Antrag_Betreuung.docx','Antrag auf einen Betreuungsgutschein','08.06.2026','Mara Aydin\nWeichselstraße 42, 12045 Berlin','Bezirksamt Neukölln von Berlin\nJugendamt, Kindertagesbetreuung', '''Sehr geehrte Damen und Herren,

für meine Tochter Leni Aydin, geboren am 14.03.2024, beantrage ich ab dem 01.09.2026 einen Betreuungsgutschein für neun bis elf Stunden täglich. Leni wohnt mit beiden Eltern in der Weichselstraße 42. Wir suchen seit April einen Platz im nördlichen Neukölln.

Ich werde ab September als Medizinische Fachangestellte in einer Praxis in Charlottenburg mit wechselnden Früh- und Spätdiensten arbeiten. Mein Mann Felix ist Bauzeichner und muss zweimal wöchentlich zu frühen Baustellenterminen nach Spandau. Die genauen Dienstpläne erhalten wir erst im Juli. Eine vorläufige Arbeitgeberbestätigung liegt bei.

Bitte berücksichtigen Sie neben den Arbeitszeiten auch die Fahrzeiten und die wechselnde Verteilung der Wochentage. Für eine Rückfrage erreichen Sie mich unter mara.aydin@familie-aydin.example. Ich bitte zugleich um Unterstützung bei der Suche nach einem tatsächlich verfügbaren Platz.

Mit freundlichen Grüßen
Mara Aydin'''),
E('03_Eingang_Jugendamt.eml','Ihr Antrag für Leni Aydin','2026-06-09T10:14:00+02:00','Kitaservice Neukölln <kita@jugend-neukoelln.example>','Mara Aydin <mara.aydin@familie-aydin.example>', '''Sehr geehrte Frau Aydin,

Ihr Antrag vom 08.06.2026 ist eingegangen und wird unter KTB-26-1847 geführt. Die Arbeitgeberunterlagen nennen noch keine festen Zeiten. Bitte senden Sie den Dienstplan nach, sobald er vorliegt. Die Platzsuche haben wir gesondert aufgenommen. Mit der Bearbeitung des Gutscheins ist keine Reservierung in einer Einrichtung verbunden.

Freundliche Grüße
Nora Winter, Kitaservice'''),
D('04_Gutscheinbescheid.docx','Bewilligung des Betreuungsumfangs für Leni Aydin','07.07.2026','Bezirksamt Neukölln von Berlin\nJugendamt, Kindertagesbetreuung','Mara und Felix Aydin\nWeichselstraße 42, 12045 Berlin', '''Sehr geehrte Frau Aydin, sehr geehrter Herr Aydin,

für Leni Aydin, geboren am 14.03.2024, wird für den Zeitraum 01.09.2026 bis 31.08.2027 ein Betreuungsumfang von über sieben bis höchstens neun Stunden täglich bewilligt. Ihr weitergehender Antrag auf einen Umfang von über neun bis höchstens elf Stunden wird abgelehnt.

Die bisher vorliegenden Arbeitsbescheinigungen weisen eine regelmäßige tägliche Abwesenheit von höchstens neun Stunden aus. Die angekündigten konkreten Schichtpläne liegen uns noch nicht vor. Wir haben die Angaben des anderen Elternteils zur variablen Arbeitszeit berücksichtigt. Ein konkreter Platz wird mit diesem Schreiben nicht zugewiesen.

Änderungen der Arbeitszeiten und ergänzende Nachweise können Sie unter Angabe des Geschäftszeichens KTB-26-1847 einreichen.

Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Widerspruch beim Bezirksamt Neukölln von Berlin, Jugendamt, eingelegt werden.

Im Auftrag
Nora Winter''', reference='KTB-26-1847'),
D('05_Arbeitgeber_Mara.docx','Arbeitszeiten ab September','22.07.2026','Praxisgemeinschaft Spreebogen\nOrganisationsbüro, Berlin Charlottenburg','Mara Aydin', '''Sehr geehrte Frau Aydin,

wir bestätigen Ihren Wiedereinstieg ab 01.09.2026 mit 32 Wochenstunden an vier Tagen. Im September arbeiten Sie montags und donnerstags von 7.00 bis 15.30 Uhr, dienstags und freitags von 9.30 bis 18.00 Uhr. Darin liegt jeweils eine unbezahlte Pause von 30 Minuten. Mittwochs arbeiten Sie nicht.

Für die ersten beiden Septemberwochen haben wir auf Ihren Wunsch Urlaub vorgemerkt. Die Freigabe betrifft den Zeitraum bis einschließlich 11.09.2026. Die Kollegin, die Ihre Frühdienste derzeit abdeckt, reduziert ab dem 14.09.2026 ihre Arbeitszeit. Ein weiterer regelmäßiger Tausch ist deshalb nicht zugesagt.

Wir freuen uns auf Ihren Wiedereinstieg und können einzelne kurzfristige Lösungen besprechen. Eine dauerhafte Arbeit im Homeoffice ist an der Anmeldung und bei den Untersuchungen nicht möglich.

Mit freundlichen Grüßen
Dr. Selma Vogt
Für die Praxisgemeinschaft'''),
X('06_Wochenplan_September.xlsx','Betreuungszeiten im September',[dict(name='Wochenplan',headers=['Tag','Mara Beginn','Mara Ende','Felix Beginn','Felix Ende','Bringen','Abholen','Stunden'], widths=[16,16,16,16,16,16,16,16], formats={'B':'hh:mm','C':'hh:mm','D':'hh:mm','E':'hh:mm','F':'hh:mm','G':'hh:mm','H':'0.00'}, rows=[['Montag',7/24,15.5/24,7/24,16/24,6.25/24,16.5/24,'=(G2-F2)*24'],['Dienstag',9.5/24,18/24,9/24,16.5/24,8.25/24,17/24,'=(G3-F3)*24'],['Mittwoch',None,None,9/24,16.5/24,9/24,14/24,'=(G4-F4)*24'],['Donnerstag',7/24,15.5/24,7/24,16/24,6.25/24,16.5/24,'=(G5-F5)*24'],['Freitag',9.5/24,18/24,9/24,15/24,8.25/24,15.5/24,'=(G6-F6)*24'],['Wochensumme',None,None,None,None,None,None,'=SUM(H2:H6)']],expected={'H2':10.25,'H7':41.5},perturbations=[{'input':'G2','value':17/24,'output':'H2','expected':10.75}]),dict(name='Wege', headers=['Strecke','Minuten','Notiert am','Bemerkung'],widths=[38,14,18,56], formats={'B':'0'},rows=[['Wohnung zur Sonnenkringel',12,'16.07.2026','Zu Fuß mit Leni; Abgabe zusätzlich etwa zehn Minuten.'],['Sonnenkringel zur Praxis',43,'16.07.2026','Fahrt mit Umstieg bei normalem Betrieb.'],['Wohnung zur Kita Am Gartenband',24,'05.08.2026','Bus und Fußweg; Wartezeit bereits enthalten.'],['Am Gartenband zur Praxis',51,'05.08.2026','Morgens selbst abgefahren.'],['Felix Baustelle zur Sonnenkringel',47,'10.08.2026','Ohne Stau; Rückfahrt von wechselnden Baustellen.']])]),
T('07_Suche_Notizbuch.txt','Maras Notizen zur Platzsuche','06.08.2026', '''14.04.2026 Sonnenkringel: Frau Albers nimmt uns auf die Liste. Noch kein freier Platz ab September.
22.04.2026 Kita Kleine Brücke: nur Warteliste, Rückruf Ende Juni vereinbart.
30.06.2026 Kleine Brücke: leider kein Platz, auch nicht für einen kürzeren Tag.
16.07.2026 Sonnenkringel besucht. Leni wollte nicht von der Holzeisenbahn weg. Ein Kind zieht möglicherweise um; die Eltern haben noch nicht gekündigt.
04.08.2026 Kitaservice nennt Am Gartenband in Britz. Besichtigung am nächsten Tag möglich.
05.08.2026 Am Gartenband besichtigt. Schöner Garten, ruhige Gruppe. Öffnung erst 8 Uhr. Frau Seidel sagt, vor September sei keine Eingewöhnung möglich.'''),
E('08_Sonnenkringel_Warteliste.eml','Leni auf unserer Warteliste','2026-07-17T15:48:00+02:00','Kita Sonnenkringel <leitung@sonnenkringel.example>','Mara Aydin <mara.aydin@familie-aydin.example>', '''Liebe Frau Aydin,

es war schön, Sie drei kennenzulernen. Wir können momentan einen Platz ab 01.10.2026 in Aussicht stellen. Der Vertrag der wegziehenden Familie ist noch nicht beendet. Bitte kündigen Sie deshalb keine andere Möglichkeit.

Unsere regulären Zeiten sind 6.30 bis 17.00 Uhr. Über eine Ankunft um 6.15 Uhr an zwei Tagen müssten wir im Team sprechen. Das ist nicht unser derzeitiges Angebot. Ich melde mich nach dem Urlaub am 17. August.

Herzliche Grüße
Paula Albers'''),
D('09_Platzangebot_Gartenband.docx','Betreuungsangebot für Leni Aydin','04.08.2026','Bezirksamt Neukölln von Berlin\nJugendamt, Kitaservice','Mara und Felix Aydin\nWeichselstraße 42, 12045 Berlin', '''Sehr geehrte Frau Aydin, sehr geehrter Herr Aydin,

die Kita Am Gartenband, Träger Kinderwege Berlin gGmbH, kann Ihrer Tochter ab 01.09.2026 einen Platz anbieten. Die Einrichtung befindet sich im Ortsteil Britz. Der Träger hat uns eine tägliche Öffnungszeit von 8.00 bis 17.00 Uhr gemeldet. Die Kontaktaufnahme erfolgt über leitung@gartenband.example.

Bitte teilen Sie uns bis zum 12.08.2026 mit, ob Sie das Angebot annehmen. Der Betreuungsvertrag ist unmittelbar mit dem Träger abzuschließen. Die Eingewöhnung und die im Rahmen des Gutscheins buchbaren Zeiten vereinbaren Sie dort.

Wir haben im Suchprofil eine variable Tätigkeit des Vaters vermerkt. Sollten die angegebenen Öffnungszeiten Ihren Bedarf nicht abdecken, erläutern Sie bitte konkret, an welchen Tagen eine andere Betreuung benötigt wird. Die Einrichtung hält den Platz bis zum genannten Rückmeldetermin frei.

Im Auftrag
Nora Winter'''),
E('10_Rueckmeldung_Platzangebot.eml','Angebot Am Gartenband und Frühdienste','2026-08-06T21:03:00+02:00','Mara Aydin <mara.aydin@familie-aydin.example>','Kitaservice Neukölln <kita@jugend-neukoelln.example>', '''Sehr geehrte Frau Winter,

vielen Dank für die Vermittlung. Wir haben Am Gartenband besucht und möchten den Platz nicht vorschnell absagen. Die Öffnung um 8 Uhr deckt unsere Montage und Donnerstage nicht ab. Felix hat an diesen Tagen feste Termine ab 7 Uhr in Spandau. Seine frühere Bescheinigung war noch für die Tätigkeit im Büro formuliert.

Können Sie uns ein Angebot mit früherer Öffnung machen? Bitte schließen Sie unsere Suche noch nicht. Den aktuellen Wochenplan und die Bestätigung von Maras Arbeitgeber fügen wir unserer Nachricht bei; die Dateien heißen 06_Wochenplan_September.xlsx und 05_Arbeitgeber_Mara.docx.

Freundliche Grüße
Mara und Felix Aydin'''),
E('11_Felix_Arbeitgeber.eml','Baustellentermine ab September','2026-08-07T11:32:00+02:00','Planwerk Ufer <buero@planwerk-ufer.example>','Felix Aydin <felix.aydin@familie-aydin.example>', '''Lieber Felix,

hier die gewünschte Bestätigung: Ab 01.09.2026 sind montags und donnerstags die Aufmaßtermine auf unserer Baustelle in Spandau jeweils um 7.00 Uhr angesetzt. Du führst dort die Planabgleiche durch. Die übrigen Bürozeiten kannst du zwischen 9 und 17 Uhr verteilen. Freitags ist ein Ende um 15 Uhr möglich.

Unsere Bescheinigung aus Juni betraf die damals vorgesehene reine Bürotätigkeit. Das Projekt wurde im Juli umgeplant. Für die erste Septemberwoche kann ich dich bei den beiden Baustellenterminen vertreten, danach nicht regelmäßig.

Viele Grüße
Jakob Weiss'''),
D('12_Eingewoehnung_Gartenband.docx','Eingewöhnung von Leni','10.08.2026','Kita Am Gartenband\nKinderwege Berlin gGmbH','Mara und Felix Aydin', '''Liebe Familie Aydin,

wir haben für Leni den ersten Besuch am 01.09.2026 um 9 Uhr vorgesehen. In den ersten drei Tagen bleibt eine vertraute Bezugsperson mit ihr etwa eine Stunde bei uns. Wir entscheiden danach gemeinsam über die erste kurze Trennung. Bitte halten Sie in den ersten beiden Wochen den Vormittag frei.

Die Dauer der Eingewöhnung richtet sich nach Leni. Wir können heute nicht verbindlich zusagen, dass ab 14.09.2026 ein voller Betreuungstag möglich ist. Ihre Mutter darf Sie nach vorheriger Absprache begleiten und ablösen. Frau Seidel ist Lenis feste Bezugserzieherin.

Die Öffnungszeit von 8.00 bis 17.00 Uhr gilt auch nach Abschluss der Eingewöhnung. Eine frühere Betreuung können wir personell nicht anbieten. Bitte geben Sie uns bis 12.08.2026 Bescheid, ob wir den Vertragsentwurf für Sie vorbereiten sollen.

Herzliche Grüße
Greta Seidel'''),
T('13_Familienchat.txt','Familienchat Betreuung im September','11.08.2026', '''11.08.2026 18:21 Mara: Mama, wären die ersten Vormittage ab dem 1. September noch möglich?
11.08.2026 18:26 Birgit: Ja, die erste Woche. In der zweiten muss ich Dienstag und Donnerstag zur eigenen Arbeit. Ich helfe gern, jeden Morgen schaffe ich das aber nicht.
11.08.2026 18:30 Felix: Ich kann am 8. September morgens mitkommen. Die Baustelle ist immer Montag und Donnerstag.
11.08.2026 18:34 Mara: Danke euch. Ich hatte im Telefonat gesagt, Oma hilft zwei Wochen. Das klang wahrscheinlich zu großzügig.
11.08.2026 18:40 Birgit: Wir kriegen die Eingewöhnung hin. Nur bitte keinen festen Frühdienstplan auf mich bauen.'''),
D('14_Ergaenzung_Gutschein.docx','Ergänzende Arbeitsnachweise und Betreuungszeiten','11.08.2026','Mara und Felix Aydin\nWeichselstraße 42, 12045 Berlin','Bezirksamt Neukölln von Berlin\nJugendamt, Kitaservice', '''Sehr geehrte Frau Winter,

wir beantragen unter Bezug auf Ihren Bescheid vom 07.07.2026 erneut einen Betreuungsumfang von über neun bis höchstens elf Stunden für Leni ab September. Der Brief wurde uns nach unserer Erinnerung am 10.07.2026 zugestellt. Damals waren die neuen Baustellentermine noch nicht bekannt.

Die Bestätigung von Planwerk Ufer vom 07.08.2026 und der Wochenplan zeigen den Bedarf am Montag und Donnerstag. Zwischen notwendiger Abgabe und möglicher Abholung liegen jeweils zehn Stunden und fünfzehn Minuten. Die anderen Tage sind kürzer. Am Mittwoch möchte Mara Leni weiterhin selbst nachmittags betreuen.

Bitte prüfen Sie die ergänzten Unterlagen und unsere Platzsuche zusammen. Wir haben dem Träger Am Gartenband noch nicht abgesagt, aber auch keinen Vertrag geschlossen. Frau Seidel kennt unser Problem. Eine dauerhaft zugesagte familiäre Ersatzbetreuung steht nicht zur Verfügung.

Mit freundlichen Grüßen
Mara und Felix Aydin'''),
E('15_Kitaservice_Antwort.eml','KTB-26-1847 Rückmeldung zu Ihren Unterlagen','2026-08-13T09:15:00+02:00','Kitaservice Neukölln <kita@jugend-neukoelln.example>','Mara Aydin <mara.aydin@familie-aydin.example>', '''Sehr geehrte Frau Aydin,

Ihre Ergänzung wurde an die Gutscheinstelle weitergeleitet. Dort läuft sie als Änderungsantrag. In der Platzsuche ist Am Gartenband derzeit als angeboten vermerkt, nicht als angenommen. Die Leitung hat die Rückmeldung ausnahmsweise bis 21.08.2026 verlängert.

Bei der Sonnenkringel ist uns ein möglicher Beginn im Oktober gemeldet worden. Eine vorzeitige Aufnahme im September hat der Träger nicht bestätigt. Bitte teilen Sie uns auch mit, ob die Großmutter an den beiden frühen Tagen einspringen kann. In unserer Gesprächsnotiz steht bislang „Oma unterstützt im September“.

Freundliche Grüße
Nora Winter'''),
D('16_Sonnenkringel_Besuchsnotiz.docx','Besuch bei der Sonnenkringel','17.08.2026','Mara Aydin','Persönliche Ablage', '''Heute habe ich um 15.45 Uhr mit Frau Albers in der Kita gesprochen. Felix war per Telefon dabei. Die wegziehende Familie hat inzwischen schriftlich zum 30.09.2026 gekündigt. Frau Albers möchte uns den Oktoberplatz anbieten, sobald der Träger die Belegung bestätigt.

Über den September haben wir länger gesprochen. Eine kurze Kennenlernzeit nachmittags wäre an zwei Tagen möglich, solange ich bei Leni bleibe. Das sei keine reguläre Betreuung und ersetze die spätere Eingewöhnung nicht. Frau Albers hat ausdrücklich gesagt, dass sie dafür keinen Septembervertrag anbieten kann.

Ich fragte nach 6.15 Uhr. Sie will noch mit der Frühdienstkollegin reden. Regulär beginnt die Öffnung um 6.30 Uhr. Felix meinte, dass er mit einer Viertelstunde Verschiebung einzelner Baustellentermine vielleicht helfen könnte. Er hat das noch nicht mit Jakob abgesprochen.

Leni hat beim Gehen allen gewunken. Wir würden den Platz wirklich gern nehmen, benötigen aber vorher eine tragfähige Lösung für den September und die beiden frühen Tage.'''),
E('17_Leitung_bestaetigt.eml','Oktoberplatz und Öffnungszeiten','2026-08-18T12:08:00+02:00','Kita Sonnenkringel <leitung@sonnenkringel.example>','Mara Aydin <mara.aydin@familie-aydin.example>', '''Liebe Frau Aydin,

der Träger hat den Platz ab 01.10.2026 heute bestätigt. Wenn Sie sich dafür entscheiden, senden wir den Betreuungsvertrag. Bis 25.08.2026 können wir Ihnen Zeit geben.

Unsere Öffnungszeit bleibt 6.30 bis 17.00 Uhr. Die Kollegin kann wegen ihrer eigenen Anfahrt keinen festen Beginn um 6.15 Uhr zusagen. Ich schreibe das ausdrücklich, damit wir keine falsche Erwartung wecken. Für den Nachmittag am 27. August können Sie gern mit Leni zum Kennenlernen kommen.

Herzliche Grüße
Paula Albers'''),
E('18_Nachtrag_an_Kanzlei.eml','Noch zwei Details zu Leni','2026-08-19T19:26:00+02:00','Mara Aydin <mara.aydin@familie-aydin.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

im Wochenplan stehen die Bringezeiten für die nahe Sonnenkringel. Für Am Gartenband müssten wir früher losfahren, die Einrichtung öffnet aber erst später. Das wollte ich kenntlich machen. Die Praxis hat bisher nur den Urlaub bis 11. September bestätigt.

Felix hat heute gefragt, ob seine Montagstermine um 7.15 Uhr beginnen könnten. Jakob prüft es für September, verspricht aber noch nichts. Wir haben weiterhin keinen Vertrag unterschrieben. Bitte sprechen Sie vor einem verbindlichen Betreuungsvertrag mit uns.

Freundliche Grüße
Mara Aydin''')]))

CASES.append(dict(slug='berlin-schulplatz-siebte-klasse',title='Ein Schulplatz für Mila in Klasse 7',plugin=SCHULE,date='24.06.2026',client='Nora und David Berger für Mila Berger',summary='Mila möchte 2026/27 die fiktive Berliner Uferblick Schule besuchen, eine öffentliche Integrierte Sekundarschule. Ihre Schwester bleibt dort in Klasse 10. Ein früh eingereichter Haushaltsbeleg erscheint später im System.',assignment='Die Eltern möchten die Ablehnung der Wunschschule überprüfen lassen und den bereits eingelegten Widerspruch ergänzen. Der angebotene Platz an der zweiten Wunschschule soll dabei gesichert bleiben.',documents=[
D('01_Auftrag_Berger.docx','Aufnahme von Mila in die siebte Klasse','22.06.2026','Nora und David Berger\nPichelsdorfer Straße 87, 13595 Berlin','Rechtsanwältin Jule Morgen\nKanzlei am Kanal, Berlin', '''Sehr geehrte Frau Morgen,

wir bitten um Hilfe bei der Ablehnung unserer Tochter Mila, geboren am 21.11.2013, an der Uferblick Schule. Es geht um Klasse 7 im Schuljahr 2026/27. Mila besucht bisher die Grundschule am Lindensteg. Ihre Schwester Jona geht bereits zur Uferblick Schule und bleibt dort im kommenden Schuljahr in Klasse 10.

Die Schule schreibt, der Geschwisterstatus sei erst nach dem Auswahlverfahren belegt worden. Wir haben ihn bei der Anmeldung angekreuzt und am selben Tag Jonas Schulbescheinigung abgegeben. Die gemeinsame Haushaltsbescheinigung kam vier Tage später per E-Mail. Im Portal sehen wir dafür jetzt den 21. Mai, obwohl die Mail am 14. März herausging.

Wir haben am 22. Juni vorsorglich Widerspruch eingelegt. Bitte prüfen Sie die Unterlagen und übernehmen Sie die weitere Korrespondenz. Mila hat einen Platz an unserer Zweitwunschschule erhalten. Den möchten wir nicht durch ein Missverständnis verlieren.

Mit freundlichen Grüßen
Nora und David Berger'''),
D('02_Anmeldung_Erstwunsch.docx','Anmeldung zur Uferblick Schule','10.03.2026','Nora und David Berger','Uferblick Schule\nÖffentliche Integrierte Sekundarschule, Berlin Spandau', '''Wir melden unsere Tochter Mila Berger, geboren am 21.11.2013, für die Jahrgangsstufe 7 im Schuljahr 2026/27 an. Die Uferblick Schule ist unser erster Wunsch. Als zweiten Wunsch geben wir die Schule am Grünbogen und als dritten Wunsch die Westpark Schule an.

Mila wohnt mit uns in der Pichelsdorfer Straße 87 in Berlin. Ihre Schwester Jona Berger, geboren am 12.02.2011, lebt ebenfalls in diesem Haushalt. Jona besucht derzeit die Klasse 9b der Uferblick Schule und wird diese Schule im kommenden Schuljahr weiter besuchen. Das Feld „Geschwisterkind an dieser Schule“ haben wir mit Ja beantwortet.

Wir geben den Anmeldebogen der Grundschule und die Förderprognose im Original ab. Jonas Schulbescheinigung vom 05.03.2026 liegt bei. Die aktuelle Meldebescheinigung haben wir beantragt und werden sie nachreichen, sobald sie vorliegt.

Nora Berger und David Berger
Am 10.03.2026 im Sekretariat abgegeben.'''),
E('03_Eingang_Anmeldung.eml','Anmeldung Mila Berger eingegangen','2026-03-10T14:38:00+01:00','Uferblick Schule <sekretariat@uferblick-schule.example>','Nora Berger <nora@berger-familie.example>', '''Sehr geehrte Frau Berger,

wir bestätigen die Anmeldung Ihrer Tochter Mila für Klasse 7 im Schuljahr 2026/27 unter UB-7-26-118. In Ihrer Mappe lagen Anmeldebogen, Förderprognose und Jonas Schulbescheinigung. Den ergänzenden Nachweis über den gemeinsamen Haushalt senden Sie bitte unter Angabe dieser Nummer an diese Adresse.

Die Anmeldungen werden im Zeitraum vom 5. bis 12. März entgegengenommen. Nach Abschluss des Verfahrens erhalten Sie eine schriftliche Entscheidung, voraussichtlich Mitte Juni. Eine Aufnahmezusage ist mit dieser Eingangsbestätigung nicht verbunden.

Freundliche Grüße
Tessa Krüger, Schulsekretariat'''),
D('04_Schulbescheinigung_Jona.docx','Schulbesuch von Jona Berger','05.03.2026','Uferblick Schule\nÖffentliche Integrierte Sekundarschule, Berlin Spandau','Nora und David Berger', '''Hiermit bestätigen wir, dass Jona Berger, geboren am 12.02.2011, im Schuljahr 2025/26 die Klasse 9b unserer Schule besucht. Nach dem derzeitigen Stand setzt sie ihren Schulbesuch im Schuljahr 2026/27 in Jahrgangsstufe 10 fort. Eine Abmeldung liegt nicht vor.

In unseren Stammdaten ist als Anschrift Pichelsdorfer Straße 87, 13595 Berlin, gespeichert. Diese Bescheinigung wird auf Wunsch der Eltern für die Anmeldung der jüngeren Schwester Mila ausgestellt.

Tessa Krüger
Schulsekretariat'''),
D('05_Meldebescheinigung_Haushalt.docx','Bescheinigung der gemeldeten Wohnung','13.03.2026','Bezirksamt Spandau von Berlin\nBürgeramt','Nora Berger\nPichelsdorfer Straße 87, 13595 Berlin', '''Für die nachstehend bezeichneten Personen ist im Melderegister als alleinige Wohnung die Pichelsdorfer Straße 87, 13595 Berlin, verzeichnet: Nora Berger, geboren am 08.05.1980, David Berger, geboren am 16.10.1979, Jona Berger, geboren am 12.02.2011, und Mila Berger, geboren am 21.11.2013.

Die Wohnung ist für alle genannten Personen seit 01.08.2019 eingetragen. Weitere Wohnungen sind in diesem Auszug nicht verzeichnet. Die Bescheinigung gibt den Registerstand vom 13.03.2026 wieder und wird auf Antrag von Nora Berger ausgestellt.

Im Auftrag
Leonie Horn''',reference='Melderegisterauskunft MB-26-0313-74'),
E('06_Nachreichung_am_14_Maerz.eml','UB-7-26-118 Nachweis gemeinsamer Haushalt','2026-03-14T09:07:00+01:00','Nora Berger <nora@berger-familie.example>','Uferblick Schule <sekretariat@uferblick-schule.example>', '''Sehr geehrte Frau Krüger,

anbei wie besprochen die Meldebescheinigung für uns und unsere beiden Töchter. Mila und Jona leben weiterhin zusammen bei uns. Die Bescheinigung wurde gestern ausgestellt. Jonas Schulbescheinigung haben Sie bereits seit der Anmeldung am Dienstag.

Bitte ordnen Sie den Haushaltsnachweis Milas Anmeldung UB-7-26-118 zu. Die beigefügte Datei haben wir in unserer Ablage als 05_Meldebescheinigung_Haushalt.docx gespeichert. Vielen Dank für Ihre freundliche Hilfe beim Anmelden.

Mit freundlichen Grüßen
Nora Berger'''),
T('07_Mailausgang_Notiz.txt','Mailablage auf Noras Laptop','21.06.2026', '''Nachgesehen am 21.06.2026 um 19.40 Uhr durch Nora Berger.
Ordner „Gesendet“, Nachricht vom 14.03.2026, 09:07 Uhr.
Betreff: UB-7-26-118 Nachweis gemeinsamer Haushalt.
Empfänger: sekretariat@uferblick-schule.example.
Anhang in der lokal gespeicherten Nachricht: 05_Meldebescheinigung_Haushalt.docx, 37 KB.
Es liegt keine automatische Fehlermeldung im Posteingang. Eine persönliche Eingangsbestätigung für diesen Anhang finde ich nicht. Die EML in unserer Akte wurde aus diesem Ordner exportiert; der Anhang liegt daneben als eigene Datei.
Im Elternportal steht bei „Haushaltsnachweis“ das Datum 21.05.2026. Ob damit Upload oder Bearbeitung gemeint ist, steht dort nicht.'''),
D('08_Information_Aufnahme.docx','Aufnahme in Jahrgangsstufe 7','26.01.2026','Uferblick Schule\nSchulleitung','Eltern der künftigen siebten Klassen', '''Liebe Eltern,

unsere Schule nimmt zum Schuljahr 2026/27 vier siebte Klassen auf. Bei mehr Anmeldungen als verfügbaren Plätzen erfolgt die Aufnahme nach dem vorgesehenen Auswahlverfahren. Die Anmeldung ist keine Platzreservierung.

Bitte kennzeichnen Sie im Anmeldebogen, ob ein Geschwisterkind die Schule im kommenden Schuljahr weiterhin besuchen wird und im selben Haushalt lebt. Wir benötigen dazu eine aktuelle Schulbescheinigung und einen Nachweis zum gemeinsamen Haushalt. Sprechen Sie das Sekretariat an, wenn eine Unterlage noch ausgestellt wird.

Für die Auswahl nach schulischen Kriterien verwenden wir die in der Förderprognose ausgewiesene Durchschnittsnote. Bei gleichem Rang entscheidet das Los. Die Auswahl nach diesen Kriterien und die gesonderte Losvergabe werden protokolliert. Besondere Härtegründe erläutern Sie bitte schriftlich und mit den dazugehörigen Belegen.

Wir freuen uns darauf, Ihre Kinder beim Kennenlernnachmittag begrüßen zu dürfen.

Freundliche Grüße
Ruben West, Schulleiter'''),
X('09_Unterlagen_und_Termine.xlsx','Familienablage zur Schulaufnahme',[dict(name='Ablage', headers=['Vorgang','Datum Familie','Datum Schule','Beleg','Notiz'],widths=[32,18,18,34,55],rows=[['Anmeldung','10.03.2026','10.03.2026','Eingangsbestätigung','Geschwisterkind im abgegebenen Bogen benannt.'],['Schulbescheinigung Jona','05.03.2026','10.03.2026','Bestätigung des Sekretariats','Jona bleibt im kommenden Schuljahr.'],['Haushaltsbescheinigung','13.03.2026','21.05.2026','Mail vom 14.03.; Portalanzeige','Familie kennt die Bedeutung des Portaldatums nicht.'],['Auswahlabschluss',None,'19.05.2026','Auskunft vom 23.06.','Datum erstmals in dieser E-Mail genannt.'],['Ablehnung erstellt',None,'17.06.2026','Ablehnungsschreiben','Aktenzeichen UB-7-26-118.'],['Brief im Kasten','20.06.2026',None,'Notiz zum Umschlag','Nora hat Samstag geleert.'],['Widerspruch','22.06.2026','22.06.2026','Eingangsbestätigung','Ergänzung angekündigt.']]),dict(name='Schulwege',headers=['Schule','Fußweg Minuten','Bus Minuten','Gesamt Minuten','Erprobt'],widths=[38,20,20,22,35],formats={'B':'0','C':'0','D':'0'},rows=[['Uferblick Schule',12,0,'=B2+C2','Gemeinsam mit Jona gegangen.'],['Schule am Grünbogen',10,21,'=B3+C3','Eine Busfahrt, ohne Umstieg.'],['Westpark Schule',14,24,'=B4+C4','Weg am offenen Nachmittag.']],expected={'D2':12,'D3':31},perturbations=[{'input':'C3','value':25,'output':'D3','expected':35}])]),
D('10_Ablehnung_Uferblick.docx','Entscheidung über die Aufnahme von Mila Berger','17.06.2026','Bezirksamt Spandau von Berlin\nSchul- und Sportamt','Nora und David Berger\nPichelsdorfer Straße 87, 13595 Berlin', '''Sehr geehrte Frau Berger, sehr geehrter Herr Berger,

Ihr Antrag auf Aufnahme Ihrer Tochter Mila Berger in die Jahrgangsstufe 7 der Uferblick Schule zum Schuljahr 2026/27 wird abgelehnt. Die Zahl der Anmeldungen überstieg die verfügbaren Plätze. Mila konnte weder über die schulischen Auswahlkriterien noch im anschließenden Losverfahren berücksichtigt werden.

Ein besonderer Härtefall wurde nicht beantragt. Die Voraussetzungen einer Berücksichtigung als im selben Haushalt lebendes Geschwisterkind waren bei Abschluss der Auswahl nicht vollständig nachgewiesen. Der ergänzende Haushaltsnachweis wurde in der Bewerbungsakte erst am 21.05.2026 erfasst. Die Schulbescheinigung der Schwester lag zuvor vor.

Für Mila wird ein Platz an der Schule am Grünbogen bereitgestellt. Sie erhalten hierzu gesonderte Nachricht. Der Wechsel in Jahrgangsstufe 7 ist damit sichergestellt.

Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Widerspruch beim Bezirksamt Spandau von Berlin, Schul- und Sportamt, eingelegt werden.

Im Auftrag
Elisa Stern''', reference='UB-7-26-118'),
T('11_Umschlag_und_Briefkasten.txt','Notiz zum Eingang des Briefes','20.06.2026', '''Nora hat am Samstag, 20.06.2026, gegen 11 Uhr den Briefkasten geleert. Der Brief des Schulamtes lag zwischen Werbung und der Wochenzeitung. Am Freitag hatte David den Kasten nicht geleert; am Donnerstagabend war er nach seiner Erinnerung leer.
Auf dem Umschlag steht ein maschineller Aufdruck vom 18.06.2026. Es war ein gewöhnlicher Brief ohne gelben Zustellumschlag. Den Umschlag haben wir nach dem Öffnen in die Papierablage gelegt. Mila hat den Bescheid am Samstag nach dem Frühstück gelesen.
Notiert von Nora am selben Tag um 15 Uhr.'''),
D('12_Widerspruch_Eltern.docx','Widerspruch zur Aufnahmeentscheidung','22.06.2026','Nora und David Berger\nPichelsdorfer Straße 87, 13595 Berlin','Bezirksamt Spandau von Berlin\nSchul- und Sportamt', '''Sehr geehrte Damen und Herren,

gegen Ihren Bescheid vom 17.06.2026 zu UB-7-26-118 legen wir Widerspruch ein. Mila sollte bei der Aufnahme an der Uferblick Schule mit ihrem Geschwisterstatus berücksichtigt werden. Wir haben Jona bereits im Anmeldebogen angegeben, ihre Schulbescheinigung am 10. März abgegeben und die Meldebescheinigung am 14. März per E-Mail nachgereicht.

Uns ist nicht verständlich, weshalb das Datum 21. Mai als erstmaliger Nachweis behandelt wird. Bitte senden Sie uns die Unterlagen zu Milas Auswahl, insbesondere die Eingangs- und Bearbeitungsvermerke zu unserer Nachreichung und den sie betreffenden Auszug aus dem Auswahlprotokoll. Daten anderer Kinder benötigen wir nicht in identifizierbarer Form.

Wir lassen uns beraten und ergänzen die Begründung nach Einsicht in die Unterlagen. Mit diesem Schreiben verzichten wir nicht auf den angebotenen Schulplatz an der Schule am Grünbogen.

Mit freundlichen Grüßen
Nora und David Berger'''),
E('13_Eingang_Widerspruch.eml','Widerspruch UB-7-26-118','2026-06-22T15:52:00+02:00','Schulamt Spandau <aufnahme@schulamt-spandau.example>','Nora Berger <nora@berger-familie.example>', '''Sehr geehrte Frau Berger,

Ihr heute in der Poststelle abgegebener und von beiden Eltern unterzeichneter Widerspruch ist eingegangen. Die zuständige Stelle fordert die Bewerbungsunterlagen bei der Schule an. Über eine Einsicht erhalten Sie gesondert Nachricht.

Bitte beachten Sie die Rückmeldefrist in der gesonderten Aufnahmeinformation der Schule am Grünbogen. Ihr Widerspruch gegen den Erstwunsch ersetzt diese Rückmeldung nicht.

Freundliche Grüße
Elisa Stern'''),
E('14_Sekretariat_zum_Scan.eml','Ihre Nachfrage zum Haushaltsnachweis','2026-06-23T10:23:00+02:00','Uferblick Schule <sekretariat@uferblick-schule.example>','Nora Berger <nora@berger-familie.example>', '''Sehr geehrte Frau Berger,

ich erinnere mich an Ihre Mappe mit Jonas Bescheinigung. Im System ist der Haushaltsnachweis am 21.05.2026 abgelegt. An diesem Tag haben wir mehrere Papiermappen nachgescannt. Daraus allein kann ich nicht sagen, wann die Datei erstmals im gemeinsamen Postfach einging.

Nach unserem Ablaufvermerk wurde die Auswahl am 19.05.2026 abgeschlossen. Ich bin gebeten worden, den Nachrichtenverlauf aus März herauszusuchen. Bitte geben Sie uns dafür noch etwas Zeit. Den digitalen Eingangsstempel kann ich selbst nicht verändern.

Freundliche Grüße
Tessa Krüger'''),
E('15_Eltern_Nachricht_weitergeleitet.eml','Weiterleitung der März-Nachricht','2026-06-23T12:02:00+02:00','Nora Berger <nora@berger-familie.example>','Schulamt Spandau <aufnahme@schulamt-spandau.example>', '''Sehr geehrte Frau Stern,

ich sende Ihnen die am 14. März versandte Nachricht erneut. Das ist keine neue Änderung unserer Wohnverhältnisse. Mila und Jona leben seit Jahren gemeinsam mit uns in derselben Wohnung. Die Meldebescheinigung selbst trägt das Datum 13. März.

Die Schule prüft ihren Posteingang. Ich kann aus meiner Ablage nur den Versand zeigen. Für März habe ich keine gesonderte Lesebestätigung. Bitte berücksichtigen Sie diese Unterscheidung bei der Zuordnung der Unterlagen.

Freundliche Grüße
Nora Berger'''),
D('16_Aufnahme_Zweitwunsch.docx','Aufnahme von Mila an der Schule am Grünbogen','18.06.2026','Bezirksamt Spandau von Berlin\nSchul- und Sportamt','Nora und David Berger', '''Sehr geehrte Frau Berger, sehr geehrter Herr Berger,

Ihre Tochter Mila Berger wird zum Schuljahr 2026/27 in Jahrgangsstufe 7 der Schule am Grünbogen aufgenommen. Diese Schule haben Sie als Zweitwunsch benannt. Die Aufnahmeinformation zur Klassenzuweisung und zum ersten Schultag erhalten Sie unmittelbar von der Schule.

Bitte bestätigen Sie der Schule bis 01.07.2026, dass Ihnen die Aufnahmeentscheidung vorliegt, und vereinbaren Sie die Übergabe der noch benötigten Unterlagen. Ein Rechtsbehelf gegen die Entscheidung über Ihre Erstwunschschule wird durch die Rückmeldung nicht zurückgenommen.

Wir wünschen Mila einen guten Start in der neuen Schule.

Im Auftrag
Elisa Stern'''),
E('17_Jona_Bestaetigung_Schule.eml','Schulbesuch Jona im kommenden Jahr','2026-06-24T08:36:00+02:00','Uferblick Schule <sekretariat@uferblick-schule.example>','Nora Berger <nora@berger-familie.example>', '''Sehr geehrte Frau Berger,

auf Ihre Nachfrage bestätige ich, dass Jona für das Schuljahr 2026/27 in unserer künftigen Klasse 10b geführt wird. Eine Abmeldung liegt nicht vor. Die Schulbescheinigung vom 05.03.2026 war insoweit zutreffend.

Ich habe Ihre März-Mail inzwischen im Archiv gefunden, aber die technische Zuordnung des Anhangs ist noch nicht abgeschlossen. Eine Aussage dazu, welche Unterlagen dem Auswahlgremium am 19. Mai vorlagen, kann ich heute noch nicht treffen.

Freundliche Grüße
Tessa Krüger'''),
E('18_Mila_Wunsch_an_Eltern.eml','Wegen der neuen Schule','2026-06-24T16:18:00+02:00','Mila Berger <mila@berger-familie.example>','Nora Berger <nora@berger-familie.example>', '''Mama,

ich wäre am liebsten mit Jona an der Uferblick. Die Werkstatt am offenen Tag fand ich schön. Falls es nicht klappt, will ich aber auch zur Kennenlernrunde am Grünbogen gehen. Samira ist dort angenommen worden und wir könnten zusammen fahren.

Bitte sagt der Kanzlei, dass ich nicht ein ganzes Schuljahr warten möchte. Ich möchte nur verstehen, warum Jona in dem Brief nicht richtig mitgezählt wurde. Den Bogen hatten wir doch zusammen ausgefüllt.

Mila''')]))

CASES.append(dict(slug='berlin-schule-klassenchat',title='Der vertauschte Termin im Klassenchat',plugin=SCHULE,date='30.09.2026',client='Anja und Timur Sommer für Emil Sommer',summary='Emil besucht Klasse 8 einer fiktiven öffentlichen Berliner ISS. Eine harmlose Chataktion sorgt für einen verspäteten Unterrichtsbeginn. Zwischen Gespräch, schriftlicher Mitteilung und Verweis bleiben Ablauf und Anhörung unklar.',assignment='Die Eltern möchten die schulische Maßnahme einordnen und gegebenenfalls eine Überprüfung erreichen. Emil soll Verantwortung für seinen eigenen Beitrag übernehmen; die Familie wünscht ein gutes weiteres Miteinander.',documents=[
D('01_Auftrag_Sommer.docx','Maßnahme nach dem Klassenchat','30.09.2026','Anja und Timur Sommer\nSchivelbeiner Straße 31, 10439 Berlin','Rechtsanwältin Jule Morgen\nKanzlei am Kanal, Berlin', '''Sehr geehrte Frau Morgen,

unser Sohn Emil, geboren am 18.01.2013, besucht die Klasse 8c der Parkbogen Schule. Nach einer Chataktion am 14. September erhielt er zunächst einen mündlichen Tadel und nun einen schriftlichen Verweis. Bitte sehen Sie sich an, wie diese Entscheidung zustande gekommen ist und welche Reaktion sinnvoll ist.

Emil hat eine alte Stundenplanabbildung mit einer lustig gemeinten Änderung verschickt. Er hat eingesehen, dass andere Kinder das ernst nehmen konnten, und sich bei Frau Feld entschuldigt. Es gab keine Beschimpfungen, Drohungen oder Gewalt. Uns geht es auch nicht um ein Vorgehen gegen die Lehrerin. Wir möchten wissen, was tatsächlich in Emils Schülerakte steht.

Zur Klassenkonferenz konnten wir an dem vorgeschlagenen Tag nicht. Wir hatten schriftlich um einen anderen Termin gebeten. Emil wurde vorher kurz aus dem Unterricht geholt. Er weiß nicht, ob dieses Gespräch seine Anhörung sein sollte.

Mit freundlichen Grüßen
Anja und Timur Sommer'''),
T('02_Klassenchat_Export.txt','Chat 8c Lernpause','14.09.2026', '''14.09.2026 18:42 Emil: Hab den alten Plan nochmal gefunden. Morgen Mathe erst zur zweiten? Das wär mal schön :)
14.09.2026 18:43 Emil: [Anlage: alter Stundenplan mit von Emil ergänzter Zeile „Dienstag erste Stunde FREI?“]
14.09.2026 18:44 Nika: Bitte nicht, ich steh sonst wieder vor der falschen Tür.
14.09.2026 18:44 Ben: Ich leite das mal an die andere Gruppe weiter.
14.09.2026 18:45 Emil: War ein Scherz, der echte Plan steht im Schulportal. Morgen normal 8 Uhr.
14.09.2026 18:47 Zoe: Bei mir auch normal Mathe. Nehmt den Portalplan.
14.09.2026 19:03 Ben: Zu spät, weitergeleitet. Schreib es denen noch.
14.09.2026 19:04 Emil: Hab dort keinen Zugang. Kannst du bitte?
Exportiert am 18.09.2026 vom Telefon Emil Sommer. Der Anhang liegt hier nicht als Bild vor; der angezeigte Anlagenname ist im Export erhalten.'''),
T('03_Stundenplan_Abschrift.txt','Text der versandten Stundenplanabbildung','18.09.2026', '''Von Emil am 18.09.2026 vom eigenen Telefon abgeschrieben:
Oben stand „8c Stundenplan, Stand August“. Darunter waren Montag bis Freitag und die Fächer eingetragen. Über dem Dienstag hatte ich mit dem Bildstift „erste Stunde FREI?“ geschrieben. Das Fragezeichen war klein am rechten Rand.
Ich hatte keinen Schulbriefkopf neu eingefügt. Auf der alten Vorlage stand unten weiterhin der Name der Schule. Ich weiß nicht, welchen Ausschnitt Ben weitergeschickt hat. Im eigenen Chat habe ich die vollständige Abbildung versandt. Mein gespeichertes Bild ist beim Aufräumen der Downloads nicht mehr da; im Chat wird noch eine kleine Vorschau gezeigt.
Emil Sommer'''),
E('04_Lehrerin_an_Eltern.eml','Verspätungen nach Nachricht im Klassenchat','2026-09-15T13:16:00+02:00','Parkbogen Schule <klasse8c@parkbogen-schule.example>','Anja Sommer <anja@sommer-familie.example>', '''Liebe Frau Sommer,

heute kamen fünf Kinder erst zur zweiten Stunde. Zwei beriefen sich auf eine weitergeleitete Stundenplanabbildung von Emil. Wir haben zunächst etwa zwölf Minuten benötigt, um zu klären, ob weitere Kinder fehlten. Emil war selbst pünktlich da.

Ich habe mit ihm gesprochen und ihn mündlich getadelt. Er hat sich entschuldigt und erklärt, dass er seine Nachricht im ursprünglichen Chat sofort richtiggestellt habe. Bitte sprechen Sie zu Hause mit ihm darüber, wie leicht sich solche Bilder verselbstständigen. Ich werde die Schulleitung über den Vorgang informieren.

Freundliche Grüße
Lea Feld'''),
D('05_Mitteilung_Tadel.docx','Mitteilung zum Gespräch vom 15 September','16.09.2026','Parkbogen Schule\nKlassenleitung 8c, Berlin Pankow','Anja und Timur Sommer', '''Liebe Frau Sommer, lieber Herr Sommer,

im gestrigen Gespräch wurde Emil wegen des Versendens einer veränderten Stundenplanabbildung mündlich getadelt. Auf dem verwendeten Formular wird diese Mitteilung als „schriftlicher Tadel“ geführt. Das Gespräch fand am Ende der ersten Stunde statt.

Emil hat erklärt, dass seine Nachricht ein Scherz gewesen sei und er sie wenige Minuten später richtiggestellt habe. Fünf Kinder kamen gleichwohl verspätet. Ob alle dieselbe weitergeleitete Nachricht gesehen hatten, war im Gespräch nicht geklärt. Emil hat angeboten, bei der nächsten Klassenstunde den tatsächlichen Ablauf zu erzählen.

Bitte bestätigen Sie den Erhalt dieser Mitteilung. Die Schulleitung wird noch entscheiden, ob weitere Schritte erforderlich sind. Ein Ausschluss vom Unterricht ist mit diesem Schreiben nicht verbunden.

Freundliche Grüße
Lea Feld'''),
D('06_Einladung_Klassenkonferenz.docx','Einladung zum Gespräch vor der Klassenkonferenz','18.09.2026','Parkbogen Schule\nSchulleitung','Anja und Timur Sommer', '''Sehr geehrte Frau Sommer, sehr geehrter Herr Sommer,

die Klassenkonferenz befasst sich am Donnerstag, 24.09.2026, um 14.30 Uhr mit dem Vorfall im Klassenchat. Erwogen wird ein schriftlicher Verweis. Emil soll durch die Weitergabe einer veränderten Stundenplanabbildung am 14. September zur Verspätung mehrerer Mitschüler und einer Unterrichtsstörung am Folgetag beigetragen haben.

Sie und Emil erhalten vor der Beratung Gelegenheit, sich dazu zu äußern. Bitte kommen Sie um 14.15 Uhr in Raum 012. Sie können uns vorab auch eine schriftliche Erklärung senden. Falls Sie verhindert sind, melden Sie sich bitte beim Sekretariat. Frau Feld hat uns bereits die Richtigstellung im ursprünglichen Chat mitgeteilt.

Die Einladung wurde heute im Schulportal an beide dort gespeicherten Sorgeberechtigtenkonten eingestellt. Einen Ausdruck erhält Emil in seiner Postmappe.

Mit freundlichen Grüßen
Maren Beck, Schulleiterin'''),
E('07_Eltern_bitten_Terminwechsel.eml','Termin am 24. September','2026-09-21T07:41:00+02:00','Anja Sommer <anja@sommer-familie.example>','Parkbogen Schule <sekretariat@parkbogen-schule.example>', '''Sehr geehrte Frau Beck,

wir haben Emils Einladung am Wochenende in der Mappe gefunden. Am Donnerstag können wir wegen festgelegter Arbeitstermine beide nicht um 14.15 Uhr kommen. Am Freitag ab 13 Uhr oder am Montag ab 15 Uhr wäre es uns möglich. Bitte bestätigen Sie einen Ersatztermin.

Emil möchte schildern, dass er den Plan sofort berichtigt hat. Wir schicken den Chatverlauf heute mit. Mein Portalzugang funktioniert seit dem Handywechsel nicht, Timur erhält Benachrichtigungen noch an seine alte Adresse. Bitte antworten Sie vorläufig an diese E-Mail-Adresse.

Freundliche Grüße
Anja Sommer'''),
D('08_Gespraechsnotiz_Emil.docx','Gespräch am Donnerstag vor der Konferenz','24.09.2026','Emil Sommer','Für meine Eltern', '''Herr Lenz hat mich in der fünften Stunde aus dem Unterricht geholt. Wir saßen ungefähr acht Minuten im kleinen Besprechungsraum. Er fragte, ob ich das Bild geschickt habe. Ich habe Ja gesagt und erklärt, dass ich zwei Minuten später „Morgen normal 8 Uhr“ geschrieben habe.

Er fragte auch, ob ich verstanden habe, dass andere wegen meines Bildes zu spät kamen. Ich sagte, ich verstehe das und es tut mir leid. Ich wusste aber nicht, ob wirklich alle fünf mein Bild hatten. Bei einem Kind war nach dessen eigener Nachricht der Bus ausgefallen.

Herr Lenz sagte, die Erwachsenen besprechen das heute. Ich dachte, das Gespräch mit meinen Eltern wird noch verschoben. Ich habe nicht gefragt, ob ich jemanden mitbringen darf. Am Ende sollte ich wieder zu Englisch gehen. Einen Text habe ich dort nicht unterschrieben.

Emil'''),
X('09_Zeiten_und_Rueckmeldungen.xlsx','Notizen zu Dienstag und den Gesprächen',[dict(name='Dienstag',headers=['Rückmeldung','Ankunft','Unterrichtsbeginn','Minuten später','Quelle'],widths=[35,18,21,22,49],formats={'B':'hh:mm','C':'hh:mm','D':'0'},rows=[['Emil',7.9/24,8/24,'=MAX(0,(B2-C2)*1440)','Frau Felds E-Mail; Emil selbst pünktlich.'],['Zwei Kinder mit Bild',8.75/24,8/24,'=(B3-C3)*1440','Erste Nachricht der Klassenleitung.'],['Kind mit Busproblem',8.25/24,8/24,'=(B4-C4)*1440','Nachricht im Klassenchat laut Emil.'],['Zwei weitere Kinder',None,8/24,None,'Kein eigener Zeitnachweis in unserer Ablage.']],expected={'D2':0,'D3':45},perturbations=[{'input':'B3','value':8.5/24,'output':'D3','expected':30}]),dict(name='Kontakte',headers=['Datum','Person','Vorgang','Antwort'],widths=[18,25,50,50],rows=[['15.09.2026','Frau Feld','Gespräch mit Emil und Mail an Eltern.','Eltern sprechen am Abend mit Emil.'],['18.09.2026','Schulleitung','Einladung im Portal und in Postmappe.','Mappe am Wochenende gelesen.'],['21.09.2026','Anja','Bitte um anderen Termin.','Keine persönliche Antwort bis Donnerstag.'],['24.09.2026','Herr Lenz','Kurzes Gespräch mit Emil.','Notiz von Emil am Abend.'],['29.09.2026','Anja','Brief mit Verweis im Briefkasten.','Am 30. September Kanzlei angeschrieben.']])]),
D('10_Emils_Erklaerung.docx','Meine Erklärung zum Stundenplanbild','21.09.2026','Emil Sommer, Klasse 8c','Frau Beck und die Klassenkonferenz', '''Ich habe das alte Stundenplanbild am Montag in unsere private Gruppe geschickt und einen Scherz darauf geschrieben. Ich wollte, dass wir zusammen darüber lachen, wie schön eine freie erste Stunde wäre. Als Nika nachfragte und Ben weiterleiten wollte, habe ich geschrieben, dass am Dienstag normal um 8 Uhr Mathe ist.

Das Bild war trotzdem keine gute Idee. Ich habe nicht daran gedacht, dass jemand nur das Bild ohne meine Nachricht bekommt. Es tut mir leid, dass Frau Feld erst suchen musste, wer fehlt, und der Unterricht später richtig anfangen konnte. Ich möchte in der Klassenstunde erklären, warum man Termine im Schulportal nachsehen sollte.

Ich habe niemanden gebeten, zu Hause zu bleiben. In der anderen Gruppe bin ich nicht. Deshalb habe ich Ben gebeten, auch meine Berichtigung weiterzuschicken. Ob er das getan hat, weiß ich nicht. Ich habe Frau Feld am Dienstag schon gesagt, dass das Bild von mir war.

Emil Sommer'''),
E('11_Bens_Mutter.eml','Bens Weiterleitung','2026-09-22T20:17:00+02:00','Daria Kurz <daria@kurz-familie.example>','Anja Sommer <anja@sommer-familie.example>', '''Liebe Anja,

Ben hat mir den Verlauf gezeigt. Er hat nur das Bild in die andere Gruppe geschickt. Die Erklärung darunter hat er zunächst nicht mitgenommen. Er sagt, dass er erst am nächsten Morgen bemerkte, dass manche es ernst nahmen. Er hat sich heute ebenfalls bei Frau Feld gemeldet.

Ich bin einverstanden, dass du diese Mail der Schule gibst. Die einzelnen Namen aus der anderen Gruppe möchte ich hier nicht weiterverteilen. Ben soll seinen eigenen Anteil selbst erklären. Wir finden gut, dass die Kinder in der Klassenstunde darüber sprechen wollen.

Viele Grüße
Daria'''),
D('12_Schriftlicher_Verweis.docx','Schriftlicher Verweis für Emil Sommer','28.09.2026','Parkbogen Schule\nSchulleitung','Anja und Timur Sommer\nSchivelbeiner Straße 31, 10439 Berlin', '''Sehr geehrte Frau Sommer, sehr geehrter Herr Sommer,

Emil Sommer wird ein schriftlicher Verweis erteilt. Die Klassenkonferenz hat am 24.09.2026 hierüber beraten und beschlossen. Grundlage ist die von Emil versandte veränderte Stundenplanabbildung, infolge derer mehrere Kinder am 15. September verspätet zum Unterricht erschienen und die erste Stunde beeinträchtigt wurde.

Emils Entschuldigung und die Richtigstellung im ursprünglichen Chat wurden berücksichtigt. Die Konferenz hält eine förmliche Reaktion für erforderlich, weil eine schulisch verwendete Vorlage verändert und über eine private Gruppe verbreitet wurde. Der mündliche Tadel allein wurde als nicht ausreichend angesehen.

Emil wurde am 24. September persönlich angehört. Sie erhielten eine Einladung; eine Teilnahme erfolgte nicht. Ihre schriftliche Erklärung vom 21. September lag der Konferenz vor. Der Verweis wird in der Schülerakte dokumentiert.

Gegen diese Entscheidung kann innerhalb eines Monats nach Bekanntgabe Widerspruch bei der Parkbogen Schule eingelegt werden.

Mit freundlichen Grüßen
Maren Beck, Schulleiterin'''),
E('13_Sekretariat_Termin.eml','Ihre Nachricht vom 21. September','2026-09-29T10:35:00+02:00','Parkbogen Schule <sekretariat@parkbogen-schule.example>','Anja Sommer <anja@sommer-familie.example>', '''Sehr geehrte Frau Sommer,

ich habe nachgesehen: Ihre Nachricht vom 21. September wurde zusammen mit Emils Erklärung ausgedruckt. Der Wunsch nach einem anderen Termin war im E-Mail-Text enthalten. Ob er beim Ansetzen der Konferenz noch berücksichtigt werden konnte, kläre ich mit Frau Beck.

Die Portalkonten sind inzwischen aktualisiert. Die alte E-Mail-Adresse von Herrn Sommer war bis gestern als Benachrichtigungsadresse eingetragen. Die Einladung befand sich zusätzlich in Emils Postmappe.

Freundliche Grüße
Mina Lorenz'''),
D('14_Bitte_um_Unterlagen.docx','Unterlagen zur Klassenkonferenz vom 24 September','29.09.2026','Anja und Timur Sommer','Parkbogen Schule\nSchulleitung', '''Sehr geehrte Frau Beck,

heute haben wir den schriftlichen Verweis erhalten. Bitte erläutern Sie uns, weshalb die Konferenz stattfand, obwohl wir um einen anderen Gesprächstermin gebeten hatten. Wir haben die Einladung nicht ignoriert. Unsere Nachricht und Emils Erklärung gingen am 21. September an das Sekretariat.

Wir bitten um den Emil betreffenden Teil des Protokolls und die Unterlagen, auf die sich die Feststellung der Verspätungen stützt. Namen anderer Kinder können dabei unkenntlich gemacht werden. Bitte teilen Sie uns außerdem mit, ob die Mitteilung vom 16. September als eigener Vorgang oder als Dokumentation des mündlichen Tadels in der Schülerakte liegt.

Emil möchte weiterhin an der vorbereiteten Klassenstunde mitwirken. Wir möchten die Sache in Ruhe klären und melden uns nach der Beratung erneut.

Mit freundlichen Grüßen
Anja und Timur Sommer'''),
E('15_Schulsozialarbeit.eml','Klassenstunde zum Umgang mit Terminen','2026-09-25T14:16:00+02:00','Schulsozialarbeit Parkbogen <sozial@parkbogen-schule.example>','Anja Sommer <anja@sommer-familie.example>', '''Liebe Frau Sommer,

Emil und Ben haben heute vorgeschlagen, gemeinsam eine kurze Erklärung für die Klassenstunde vorzubereiten. Wir möchten dabei den Verlauf ohne Vorführen einzelner Kinder besprechen. Beide können zeigen, wie man Originalnachrichten und Weiterleitungen auseinanderhält.

Ich habe mit Emil über seine Sorge gesprochen, jetzt als jemand zu gelten, dem man nichts glauben könne. Im Alltag erlebe ich ihn sonst als hilfsbereit. Die Klassenstunde kann unabhängig von der noch offenen Rückfrage zum Verfahren stattfinden.

Freundliche Grüße
Sina Lenz, Schulsozialarbeiterin'''),
D('16_Abrede_Klassenstunde.docx','Gemeinsamer Beitrag zur Klassenstunde','28.09.2026','Emil Sommer und Ben Kurz','Lea Feld und Sina Lenz', '''Wir möchten in der Klassenstunde am 02.10.2026 erklären, wie sich die Nachricht zum Stundenplan verbreitet hat. Emil beschreibt das ursprüngliche Bild und seine Berichtigung. Ben beschreibt die Weiterleitung ohne den zugehörigen Text.

Wir zeigen keine Namen oder privaten Nachrichten anderer Kinder. Stattdessen schreiben wir auf zwei Zettel, welche Informationen im ersten Chat und in der Weiterleitung standen. Danach möchten wir gemeinsam sammeln, wo sichere Informationen zu Unterrichtszeiten zu finden sind.

Wir wissen, dass dadurch die verlorene Unterrichtszeit nicht zurückkommt. Wir möchten aber dazu beitragen, dass so etwas nicht noch einmal passiert. Frau Lenz begleitet das Gespräch. Wir haben jeweils ungefähr zwei Minuten für unseren eigenen Beitrag vorgesehen.

Emil Sommer und Ben Kurz'''),
E('17_Lehrerin_Kontext.eml','Zur ersten Stunde am 15. September','2026-09-30T08:44:00+02:00','Parkbogen Schule <klasse8c@parkbogen-schule.example>','Anja Sommer <anja@sommer-familie.example>', '''Liebe Frau Sommer,

zur zeitlichen Einordnung: Emil war pünktlich. Die zwölf Minuten in meiner ersten Mail betrafen die Klärung der fehlenden Kinder, nicht eine zwölfminütige Verspätung Emils. Bei einem der fünf Kinder wurde später ein Busproblem genannt. Dies habe ich der Schulleitung am 23. September nachgetragen.

Emils schriftliche Erklärung lag mir vor. Ich möchte, dass wir nach der Klärung wieder gut miteinander weiterarbeiten. Den Beitrag zur Klassenstunde habe ich mit ihm und Ben besprochen.

Freundliche Grüße
Lea Feld'''),
E('18_Eltern_Nachtrag.eml','Emil möchte weiter zur Schule gehen','2026-09-30T18:20:00+02:00','Anja Sommer <anja@sommer-familie.example>','Jule Morgen <post@kanzlei-kanal.example>', '''Sehr geehrte Frau Morgen,

Emil geht weiter ganz normal zum Unterricht. Es gibt keinen Ausschluss und keine angedrohte Versetzung in eine andere Klasse. Bitte berücksichtigen Sie das bei Ihrer Rückmeldung. Die neue Mail von Frau Feld haben wir beigefügt.

Uns ist wichtig, dass seine Entschuldigung bestehen bleibt. Wir möchten sie nicht zurücknehmen, nur weil wir den Verweis überprüfen lassen. Wegen des Protokolls hat die Schule noch nicht geantwortet. Den Brief vom 28. September fanden wir am 29. September im Kasten.

Freundliche Grüße
Anja Sommer''')]))

CASES.append(dict(slug='berlin-professur-berufungszusage',title='Nelas Labor und die Berufungszusage',plugin=HOCHSCHULE,date='30.09.2026',client='Prof. Dr. Nela Ahrens',summary='Nela Ahrens hat im April eine W2-Professur an der fiktiven staatlichen Universität an der Spree Berlin angetreten. Die sachliche Ausstattung ist schriftlich zugesagt, doch das vorgesehene Labor wird später frei und ein Teil der Mittel ist intern gesperrt.',assignment='Die Professorin möchte die Reichweite ihrer Zusage und einen tragfähigen Weg zur Ausstattung klären lassen. Sie will ein arbeitsfähiges Labor und eine verlässliche Mittelplanung für die vereinbarte Laufzeit.',documents=[
D('01_Auftrag_Ahrens.docx','Ausstattung meiner Professur','30.09.2026','Prof. Dr. Nela Ahrens\nUniversität an der Spree Berlin, Fachbereich Bildungswissenschaften','Rechtsanwalt Moritz Seidel\nKanzlei Campus und Stadt, Berlin', '''Sehr geehrter Herr Seidel,

ich bitte Sie, die beigefügte Berufungszusage und ihre bisherige Umsetzung zu prüfen. Ich habe die W2-Professur für digitale Lernumgebungen zum 01.04.2026 angetreten. Die Kolleginnen und Kollegen haben mich sehr freundlich aufgenommen. Für das Wintersemester fehlt uns aber weiterhin ein Labor, in dem sechs Personen parallel und teilweise akustisch getrennt arbeiten können.

Vor meiner Rufannahme wurden 120.000 Euro Erstausstattung, laufende Sachmittel und eine halbe wissenschaftliche Stelle für drei Jahre schriftlich zugesagt. Die Stelle ist besetzt. Von den Sachmitteln sind nach der aktuellen Liste noch 65.600 Euro nicht durch Bestellungen gebunden. Das Präsidium hat weitere Bestellungen nun zurückgestellt und verweist auf die Haushaltslage.

Bitte klären Sie, welche Bestandteile ich wie einfordern kann und ob die angebotene Raumlösung genügt. Ich möchte nicht um jeden Quadratmeter streiten. Die zugesagten Funktionen müssen aber rechtzeitig nutzbar sein. Einen gerichtlichen Schritt möchte ich erst nach Ihrer Erläuterung abstimmen.

Mit freundlichen Grüßen
Nela Ahrens'''),
D('02_Ruf_W2.docx','Ruf auf die Professur für digitale Lernumgebungen','03.12.2025','Senatsverwaltung für Wissenschaft, Gesundheit und Pflege\nAbteilung Wissenschaft, Berlin','Dr. Nela Ahrens\nLeipzig', '''Sehr geehrte Frau Dr. Ahrens,

wir erteilen Ihnen den Ruf auf die W2-Professur für digitale Lernumgebungen im Fachbereich Bildungswissenschaften der Universität an der Spree Berlin. Der Dienstantritt ist vorbehaltlich des Abschlusses der persönlichen und dienstrechtlichen Voraussetzungen zum 01.04.2026 vorgesehen.

Über die sachliche und personelle Ausstattung führen Sie mit der Universität gesonderte Verhandlungen. Nach deren Mitteilung stehen Frau Vizepräsidentin Faber und der Dekan, Professor Klein, dafür am 16. Dezember zur Verfügung. Bitte übersenden Sie der Universität vorab eine kurze Beschreibung der für Ihre Forschung und Lehre erforderlichen Ausstattung.

Wir freuen uns, wenn Sie den Ruf annehmen und den Aufbau des neuen Lehr- und Forschungsbereichs mitgestalten. Dieses Schreiben enthält noch keine verbindliche Zusage einzelner Räume oder zusätzlicher Ausstattungsmittel.

Mit freundlichen Grüßen
Im Auftrag
Dr. Friederike Weber'''),
E('03_Verhandlungsnotiz_Dekan.eml','Unser Gespräch zu Räumen und Geräten','2025-12-17T16:11:00+01:00','Prof. Dr. Anton Klein <dekan@uas-berlin.example>','Dr. Nela Ahrens <nela.ahrens@lehrraum.example>', '''Liebe Frau Ahrens,

ich habe aus unserem Gespräch sechs Bildschirmarbeitsplätze, zwei Messsysteme für Blickbewegungen und eine akustisch abgeschirmte Gesprächsmöglichkeit mitgenommen. Wir planen dafür rund 80 Quadratmeter. Raum B-214 wäre gut geeignet, wird aber erst nach dem Umzug der Medienwerkstatt frei.

Ich habe dem Präsidium einen Beginn mit einem kleineren Übergangsraum vorgeschlagen. Die endgültige Zusage kommt von dort. Für die 120.000 Euro Erstausstattung liegt unsere fachliche Befürwortung vor. Bitte sagen Sie mir, wenn ich eine wesentliche Funktion vergessen habe.

Herzliche Grüße
Anton Klein'''),
D('04_Schriftliche_Berufungszusage.docx','Sachliche und personelle Ausstattung der Professur','12.01.2026','Universität an der Spree Berlin\nPräsidium','Dr. Nela Ahrens', '''Sehr geehrte Frau Dr. Ahrens,

für die Übernahme der W2-Professur für digitale Lernumgebungen sagen wir Ihnen für die Zeit vom 01.04.2026 bis 31.03.2029 eine wissenschaftliche Beschäftigtenstelle im Umfang von 50 Prozent einer Vollzeitstelle sowie jährlich 24.000 Euro laufende Sachmittel zu. Für die Erstausstattung werden einmalig 120.000 Euro bereitgestellt. Beschaffungen erfolgen nach den für die Universität geltenden Beschaffungsregeln.

Für Forschung und forschungsbezogene Lehre wird eine funktionsgerechte Laborfläche von etwa 80 Quadratmetern mit sechs Bildschirmarbeitsplätzen und einer akustisch abgeschirmten Gesprächsmöglichkeit bereitgestellt. Vorgesehen ist Raum B-214, sobald die Medienwerkstatt ausgezogen ist. Bis dahin erhalten Sie Raum A-108. Die funktionsgerechte Gesamtlösung soll spätestens zum Beginn der Vorlesungen im Wintersemester 2026/27 zur Verfügung stehen. Ein bestimmter Einzelraum wird nicht dauerhaft festgeschrieben.

Die Mittel sind für den genannten Zeitraum in der internen Finanzplanung berücksichtigt. Änderungen des Verwendungszwecks bedürfen der Abstimmung mit dem Präsidium. Nach Ablauf der drei Jahre wird die weitere Ausstattung nach den dann geltenden Zuweisungsregeln beraten.

Mit freundlichen Grüßen
Prof. Dr. Eva Faber
Für das Präsidium''', reference='BA-26-04'),
D('05_Rufannahme.docx','Annahme des Rufes','20.01.2026','Dr. Nela Ahrens','Senatsverwaltung für Wissenschaft, Gesundheit und Pflege\nAbteilung Wissenschaft\nGleichlautend an das Präsidium der Universität an der Spree Berlin', '''Sehr geehrte Frau Dr. Weber, sehr geehrte Frau Professorin Faber,

ich nehme den Ruf auf die W2-Professur für digitale Lernumgebungen zum 01.04.2026 an. Grundlage meiner Entscheidung ist neben den besprochenen Aufgaben die schriftliche Ausstattungszusage des Präsidiums vom 12.01.2026. Ich freue mich auf die Zusammenarbeit mit dem Fachbereich und den Aufbau des Labors.

Die Übergangsnutzung von Raum A-108 ist für mich bis zum Vorlesungsbeginn im Wintersemester tragbar. Ich beginne im Sommer mit der Entwicklung der Lehrformate und den Beschaffungen. Für die ab Oktober geplanten Erhebungen benötige ich die im Schreiben beschriebenen sechs Arbeitsplätze und die akustische Trennung.

Die Personalstelle wird die noch benötigten Unterlagen bis Ende dieser Woche erhalten. Für eine gemeinsame Beschaffungsbesprechung schlage ich den 10. Februar vor.

Mit freundlichen Grüßen
Nela Ahrens'''),
E('06_Budgetanlage.eml','Kostenstelle und Anfangsbudget','2026-03-20T11:47:00+01:00','Finanzservice UAS <finanzen@uas-berlin.example>','Prof. Dr. Nela Ahrens <nela.ahrens@uas-berlin.example>', '''Sehr geehrte Frau Ahrens,

die Kostenstelle 4817 ist eingerichtet. Für die Erstausstattung sind 120.000 Euro als Berufungsmittel hinterlegt. Für laufende Sachmittel stehen ab April 2026 anteilig 18.000 Euro für das Kalenderjahr zur Verfügung; die Jahreszusage beträgt 24.000 Euro.

Bitte reichen Sie Gerätebestellungen über den Einkauf ein. Die Mittelanzeige ist noch keine Ausgabefreigabe für jeden einzelnen Auftrag. Bei Beschaffungen oberhalb der internen Wertgrenzen unterstützen wir Sie bei der Verfahrenswahl. Frau Ivers ist Ihre Ansprechpartnerin.

Freundliche Grüße
Carla Ivers'''),
D('07_Antritt_und_Uebergabe.docx','Übergabe des Raumes A 108','01.04.2026','Universität an der Spree Berlin\nGebäudeservice und Prof. Dr. Nela Ahrens','Raumverwaltung', '''Am 01.04.2026 wurde Professorin Ahrens der Raum A-108 mit zwei Schlüsseln übergeben. Die Nutzfläche beträgt 42 Quadratmeter. Nach Abzug des fest eingebauten Schranks und der Verkehrsflächen können dort vier der vorgesehenen sechs Bildschirmarbeitsplätze aufgestellt werden.

Der Raum ist als Übergangslösung für den Aufbau der Professur vorgesehen. Es gibt keine separate akustisch abgeschirmte Fläche. Die vorhandenen Netzwerkanschlüsse wurden bei Übergabe gemeinsam geprüft und funktionieren. Der zusätzliche Stromkreis für die mobile Gesprächskabine ist hier nicht vorhanden.

Die Schlüssel für B-214 wurden nicht übergeben. Nach Auskunft des Gebäudeservice ist der Auszug der Medienwerkstatt für Ende August geplant. Der Stand wird beim nächsten Raumgespräch am 02.07.2026 aktualisiert.

Aufgenommen von Mira Hart, Gebäudeservice.
Nela Ahrens war bei der Begehung anwesend.'''),
X('08_Ausstattung_Stand_September.xlsx','Ausstattungsplanung Nela Ahrens',[dict(name='Erstausstattung',headers=['Posten','Stück','Euro je Stück','Gebunden Euro','Stand'],widths=[38,14,22,24,52],formats={'B':'0','C':'#,##0.00','D':'#,##0.00'},rows=[['Blickbewegungsmessgerät',2,12500,'=B2*C2','Bestellt 08.06.2026; Lieferung erfolgt.'],['Arbeitsrechner',6,1800,'=B3*C3','Bestellt 15.06.2026; vier aufgebaut.'],['Mobile Gesprächskabine',1,18600,'=B4*C4','Bestellt 22.07.2026; Liefertermin noch offen.'],['Summe gebunden',None,None,'=SUM(D2:D4)','Keine Aussage über bereits bezahlte Rechnungen.'],['Berufungsbudget',None,None,120000,'Zusage vom 12.01.2026.'],['Noch nicht gebunden',None,None,'=D6-D5','Bestellfreigabe seit 15.09. zurückgestellt.']],expected={'D5':54400,'D7':65600},perturbations=[{'input':'C4','value':19600,'output':'D7','expected':64600}]),dict(name='Räume',headers=['Raum','Nutzfläche qm','Arbeitsplätze','Akustische Trennung','Stand'],widths=[20,20,20,33,55],formats={'B':'0','C':'0'},rows=[['A-108',42,4,'Nein','Seit 01.04. nutzbar; Übergang.'],['B-214',82,6,'Geplant','Medienwerkstatt noch darin.'],['C-032',76,6,'Nebenraum nur nach Buchung','Am 24.09. besichtigt; geteilt mit Sprachlabor.']])]),
E('09_Raumverzug.eml','B-214 wird später frei','2026-08-27T09:19:00+02:00','Gebäudeservice UAS <raeume@uas-berlin.example>','Prof. Dr. Nela Ahrens <nela.ahrens@uas-berlin.example>', '''Liebe Frau Ahrens,

leider zieht die Medienwerkstatt nicht Ende August aus. Die Elektroarbeiten in ihren neuen Räumen dauern länger als geplant. Der derzeitige Umzugstermin ist der 16. November. Ich weiß, dass das Ihren Kursbeginn trifft.

Wir prüfen deshalb C-032 mit einem angrenzenden Besprechungsraum. Die Gesamtfläche wäre ähnlich. Allerdings nutzt das Sprachlabor den Nebenraum dienstags und donnerstags. Bitte senden Sie mir Ihre festen Erhebungstermine, damit wir prüfen können, ob sich die Zeiten ergänzen.

Viele Grüße
Mira Hart'''),
T('10_Telefonnotiz_Dekan.txt','Telefonat mit Anton Klein','02.09.2026', '''Nela, Notiz direkt nach dem Gespräch um 16.15 Uhr.
Anton möchte, dass ich C-032 anschaue. Er sagt, die Raumzusage sei für die Funktionen gedacht gewesen, nicht für die Türnummer. Darin sind wir uns einig. Ich habe erklärt, dass die getrennten Gespräche gleichzeitig mit den Bildschirmaufgaben laufen.
Er dachte bisher, die Gesprächskabine sei schon geliefert. Ich sagte: bestellt ja, Liefertermin noch offen; in A-108 fehlt außerdem der Stromkreis. Er fragt beim Gebäudeservice nach.
Zu den freien 65.600 Euro wusste er noch nichts von einer Sperre. Er vermutet eine vorübergehende Bestellpause, wollte das aber nicht zusagen.'''),
D('11_Mitteilung_Budget.docx','Weitere Beschaffungen aus Berufungsmitteln','15.09.2026','Universität an der Spree Berlin\nPräsidium und Finanzdezernat','Prof. Dr. Nela Ahrens', '''Sehr geehrte Frau Ahrens,

bis zur abgeschlossenen Überprüfung der verfügbaren Haushaltsmittel werden weitere Beschaffungen aus dem noch nicht gebundenen Anteil Ihrer Berufungsmittel zurückgestellt. Bereits wirksam beauftragte Lieferungen werden weiter abgewickelt. Ihre wissenschaftliche Beschäftigtenstelle und die laufenden Sachmittel sind von dieser vorläufigen Maßnahme nicht erfasst.

Die Universität muss kurzfristig gestiegene Bewirtschaftungskosten auffangen. Wir bitten Sie, uns bis zum 25.09.2026 mitzuteilen, welche noch nicht ausgelösten Bestellungen für den Beginn des Wintersemesters unverzichtbar sind. Über diese Bedarfe wird einzeln entschieden.

Mit der vorläufigen Zurückstellung wird die Berufungszusage vom 12.01.2026 nicht insgesamt aufgehoben. Über Umfang und Dauer der Einschränkung können wir heute noch keine abschließende Mitteilung machen. Das Präsidium wird die Lage in seiner Sitzung Anfang Oktober erneut beraten.

Mit freundlichen Grüßen
Prof. Dr. Eva Faber'''),
E('12_Bedarfsmeldung.eml','Unverzichtbare Beschaffungen zum Kursbeginn','2026-09-21T10:06:00+02:00','Prof. Dr. Nela Ahrens <nela.ahrens@uas-berlin.example>','Finanzservice UAS <finanzen@uas-berlin.example>', '''Liebe Frau Ivers,

für den Oktober benötige ich zusätzlich sechs höhenverstellbare Tische für zusammen 5.400 Euro und zwei mobile Sichtschutzmodule für zusammen 2.800 Euro. Die Angebote liegen dem Einkauf seit dem 7. September vor. Diese 8.200 Euro sind in meiner Bestellliste noch nicht als gebunden enthalten.

Die Tische kann ich sowohl in B-214 als auch in C-032 verwenden. Beim Sichtschutz müssen wir den endgültigen Raum noch abgleichen. Die akustische Trennung ersetzen die Module nicht. Bitte teilen Sie mir mit, ob die Beschaffung bis zum 5. Oktober ausgelöst werden kann.

Viele Grüße
Nela Ahrens'''),
D('13_Begehung_C032.docx','Begehung des Raumes C 032','24.09.2026','Gebäudeservice UAS\nMira Hart und Prof. Dr. Nela Ahrens','Raumverwaltung', '''Bei der heutigen Begehung waren Mira Hart, Nela Ahrens und die Laborleiterin des Sprachlabors, Dr. Judith Brandt, anwesend. C-032 hat 76 Quadratmeter und bietet genügend Platz für sechs Bildschirmarbeitsplätze. Der angrenzende Raum C-033 ist 12 Quadratmeter groß und lässt sich akustisch gut abtrennen.

C-033 wird dienstags von 10 bis 14 Uhr und donnerstags von 9 bis 13 Uhr für Sprachtests benötigt. Professorin Ahrens hat gerade diese Zeiten für parallele Gespräche in ihrem Lehrforschungsprojekt vorgesehen. Eine Nutzung am Montag und Mittwoch wäre möglich, erfordert aber eine Änderung des angekündigten Kursplans.

Die Netzwerkanschlüsse in C-032 sind vorhanden. Der Gebäudeservice hält die erforderliche Stromversorgung für die mobile Kabine bis 19. Oktober für herstellbar. Einen verbindlichen Auftrag gibt es noch nicht. C-032 könnte zunächst bis Ende März genutzt werden. Über eine anschließende Nutzung ist noch nicht entschieden.

Mira Hart hat diese Notiz am selben Nachmittag an alle Teilnehmenden gesandt.'''),
E('14_Liefertermin_Kabine.eml','Ihre Bestellung Gesprächskabine','2026-09-25T08:54:00+02:00','Lernraum Technik <service@lernraum-technik.example>','Prof. Dr. Nela Ahrens <nela.ahrens@uas-berlin.example>', '''Sehr geehrte Frau Professorin Ahrens,

für Ihre Bestellung LT-260722 bestätigen wir die mögliche Anlieferung am 19.10.2026. Voraussetzung ist, dass Sie uns bis zum 05.10. den endgültigen Aufstellraum und die Freigabe der Stromversorgung nennen. Die Kabine benötigt eine lichte Aufstellfläche von 2,40 mal 2,20 Metern zuzüglich Zugang.

Eine Zwischenlagerung in unserem Lager ist bis Ende November ohne zusätzliche Kosten möglich. Danach müssten wir den Liefertermin neu abstimmen. Bitte geben Sie uns Bescheid, sobald die Universität den Raum festgelegt hat.

Freundliche Grüße
Lukas Dorn'''),
D('15_Bitte_um_Umsetzung.docx','Umsetzung der Ausstattungszusage','28.09.2026','Prof. Dr. Nela Ahrens','Universität an der Spree Berlin\nPräsidium', '''Sehr geehrte Frau Professorin Faber,

ich bitte um eine verbindliche Mitteilung, wie die funktionsgerechte Laborausstattung und die erforderlichen Beschaffungen zum Beginn des Wintersemesters umgesetzt werden. Die Nutzung eines anderen Raumes als B-214 ist für mich vorstellbar. Dafür müssen sechs Bildschirmplätze und die gleichzeitige akustisch getrennte Gesprächsführung verfügbar sein.

Die Begehung von C-032 hat eine Überschneidung mit den Sprachtests gezeigt. Ich kann meinen Kurs einmalig auf Montag und Mittwoch legen, wenn die Stundenplanstelle und die teilnehmenden Studierenden zustimmen. Eine dauerhafte jährliche Neuplanung wäre jedoch schwierig. Bitte klären Sie auch den Stromanschluss und die rechtzeitige Freigabe der bereits benannten Tische und Sichtschutzmodule.

Meine Rufannahme beruhte auf Ihrer Zusage vom 12.01.2026. Ich möchte die zugesagten Mittel weiterhin ausschließlich für den Aufbau verwenden. Eine Umwidmung oder ein Verzicht auf den verbleibenden Betrag ist mit diesem Schreiben nicht verbunden.

Mit freundlichen Grüßen
Nela Ahrens'''),
T('16_Notiz_Kursplanung.txt','Notiz für meine Kursvorbereitung','29.09.2026', '''Der Kurs „Lernen beobachten“ hat 18 Anmeldungen. Ich plane drei Gruppen mit jeweils sechs Personen. Die Gespräche laufen parallel zu den Bildschirmaufgaben. Es geht um Lernwege, nicht um medizinische Untersuchungen.
Die Studierenden haben bislang Dienstagvormittag und Donnerstagvormittag im Plan. Ein Wechsel auf Montag oder Mittwoch wäre für sechs von ihnen laut erster Rückmeldung schwierig. Die Stundenplanstelle hat noch keine abschließende Antwort.
Falls wir bis Ende Oktober nur vier Rechner nutzen, brauche ich zusätzliche Durchgänge. Die wissenschaftliche Mitarbeiterin kann diese nicht allein leiten; sie beginnt im Oktober zunächst mit 50 Prozent und ihrem eigenen Projekt.
Nela, 29.09.2026'''),
E('17_Praesidium_Zwischenstand.eml','Ihre Ausstattung und unser Termin','2026-09-29T16:09:00+02:00','Präsidialbüro UAS <praesidium@uas-berlin.example>','Prof. Dr. Nela Ahrens <nela.ahrens@uas-berlin.example>', '''Sehr geehrte Frau Ahrens,

Frau Faber möchte die Raumfrage und die Beschaffung am 06.10.2026 gemeinsam mit Ihnen, Herrn Klein und dem Gebäudeservice besprechen. Die beiden Bedarfspositionen über insgesamt 8.200 Euro wurden in die Entscheidungsunterlage aufgenommen.

Bitte verstehen Sie diese Nachricht noch nicht als Bestellfreigabe. Für C-032 wird geprüft, ob die Nebenraumnutzung in den ersten sechs Wochen angepasst werden kann. Wir hoffen, Ihnen beim Termin eine konkrete Lösung vorlegen zu können.

Freundliche Grüße
Mette Paul'''),
E('18_Nachtrag_Mandantin.eml','Termin am 6. Oktober und Unterlagen','2026-09-30T17:03:00+02:00','Prof. Dr. Nela Ahrens <nela.ahrens@uas-berlin.example>','Moritz Seidel <post@campus-stadt.example>', '''Sehr geehrter Herr Seidel,

den Termin am 6. Oktober habe ich angenommen. Mir wäre eine kurze Einschätzung davor sehr hilfreich. Die Stellenausstattung funktioniert bislang, und die laufenden Sachmittel wurden nicht gekürzt. Der Konflikt betrifft den Laborbetrieb und die weitere Erstausstattung.

Ich möchte im Gespräch verbindliche Daten und Zuständigkeiten festhalten. Bitte schreiben Sie zunächst nur mir. Mit einer rechtlichen Vertretung nach außen möchte ich nach Ihrer Einschätzung entscheiden, wie deutlich wir auftreten.

Mit freundlichen Grüßen
Nela Ahrens''')]))

CASES.append(dict(slug='berlin-professur-lehrdeputat',title='Simons Lehrplan und das Stadtprojekt',plugin=HOCHSCHULE,date='30.09.2026',client='Prof. Dr. Simon Bergmann',summary='Ein W2-Universitätsprofessor plant neun Lehrveranstaltungsstunden und beantragt zwei Stunden Ermäßigung für eine zusätzliche Forschungskoordination. Eine Vorjahresmail, ein befristeter Bescheid und ein Entwurf der Lehrplanung werden unterschiedlich verstanden.',assignment='Der Professor bittet um Einordnung der Lehrverpflichtung und des offenen Ermäßigungsantrags sowie um ein Schreiben, das seine Forschung und eine verlässliche Lehre zusammenführt.',documents=[
D('01_Auftrag_Bergmann.docx','Lehrverpflichtung und Projektkoordination','30.09.2026','Prof. Dr. Simon Bergmann\nUniversität an der Spree Berlin, Institut für Stadtforschung','Rechtsanwalt Moritz Seidel\nKanzlei Campus und Stadt, Berlin', '''Sehr geehrter Herr Seidel,

bitte beraten Sie mich zur Lehrplanung für das Wintersemester 2026/27. Ich bin vollbeschäftigter W2-Universitätsprofessor. Meine regelmäßige Lehrverpflichtung beträgt neun Lehrveranstaltungsstunden. Für die Koordination des neuen Forschungsverbunds Offene Stadtkarte habe ich am 2. September eine Ermäßigung um zwei Stunden beantragt. Eine Entscheidung steht aus.

Das Dekanat meint, mein vorläufiger Plan umfasse nur sieben Stunden. In meiner eigenen Tabelle komme ich einschließlich des Blockseminars auf neun. Gleichzeitig wurde eine Kollegin bereits gefragt, ob sie eine Seminargruppe übernimmt. Ich möchte vermeiden, dass am Ende eine Gruppe doppelt oder gar nicht geplant ist.

Im vergangenen Winter gab es eine Ermäßigung um eine Stunde. Die damalige E-Mail klingt allgemein, der zugehörige Bescheid war jedoch befristet. Ich habe bisher keine Lehrveranstaltung abgesagt und warte auf eine schriftliche Entscheidung. Bitte klären Sie auch, welche Unterlagen die Universität noch benötigt.

Mit freundlichen Grüßen
Simon Bergmann'''),
D('02_Personalstelle_Lehrverpflichtung.docx','Lehrverpflichtung der Professur','08.07.2024','Universität an der Spree Berlin\nPersonaldezernat','Prof. Dr. Simon Bergmann', '''Sehr geehrter Herr Professor Bergmann,

Sie nehmen Ihre W2-Universitätsprofessur für Stadtbezogene Datenmethoden in Vollbeschäftigung wahr. Für die Lehrplanung wird eine regelmäßige Lehrverpflichtung von neun Lehrveranstaltungsstunden zugrunde gelegt. Dies entspricht der für Ihre Tätigkeit geltenden Regelung der Berliner Lehrverpflichtungsverordnung.

Die semesterbezogene Planung erfolgt mit dem Fachbereich. Entscheidungen über eine Ermäßigung werden gesondert mit Umfang und Zeitraum mitgeteilt. Zusätzliche Aufgaben oder eine im Gespräch angekündigte Prüfung verändern die Lehrverpflichtung nicht ohne eine entsprechende Entscheidung.

Bitte reichen Sie die Lehrnachweise jeweils nach dem vom Fachbereich bekanntgegebenen Verfahren ein. Fragen zur Anrechnung einzelner Lehrformen klären Sie rechtzeitig vor Beginn der Veranstaltung mit der zuständigen Stelle.

Mit freundlichen Grüßen
Frida Sommer
Personaldezernat'''),
E('03_Vorjahr_Email.eml','Entlastung im kommenden Winter','2025-08-19T14:27:00+02:00','Prof. Dr. Anton Klein <dekan@uas-berlin.example>','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>', '''Lieber Simon,

wir unterstützen deine Entlastung wegen der Einführung des gemeinsamen Datenarchivs. Du sollst dafür im kommenden Winter eine Stunde weniger lehren. Frau Sommer bereitet die formale Entscheidung vor. Bitte plane die Archivaufgabe deshalb zusammen mit den verbleibenden acht Stunden.

Dass wir Forschung und Lehre vernünftig zusammenbringen müssen, gilt natürlich auch in den nächsten Runden. Über weitere Zeiträume sprechen wir, sobald die Aufgaben feststehen. Ich danke dir, dass du das Archiv für alle mit aufbaust.

Viele Grüße
Anton'''),
D('04_Vorjahr_Bescheid.docx','Ermäßigung für das Wintersemester 2025 26','02.09.2025','Universität an der Spree Berlin\nPräsidium','Prof. Dr. Simon Bergmann', '''Sehr geehrter Herr Professor Bergmann,

Ihre Lehrverpflichtung wird für das Wintersemester 2025/26 um eine Lehrveranstaltungsstunde ermäßigt. Die für diesen Zeitraum zu erbringende Lehrverpflichtung beträgt damit acht Lehrveranstaltungsstunden. Die Ermäßigung dient dem zeitlich begrenzten Aufbau des institutsübergreifenden Datenarchivs.

Diese Entscheidung gilt vom 01.10.2025 bis zum 31.03.2026. Eine Fortsetzung in späteren Semestern ist damit nicht zugesagt. Sollten weitere besondere Aufgaben übertragen werden, ist deren Umfang in einem neuen Antrag darzulegen. Die tatsächliche Lehrleistung ist im üblichen Lehrnachweis zu dokumentieren.

Die Entscheidung wurde mit dem Dekanat und der Personalstelle abgestimmt. Bitte teilen Sie wesentliche Änderungen der benannten Aufgabe unverzüglich mit.

Mit freundlichen Grüßen
Prof. Dr. Eva Faber''',reference='LV-25-088'),
D('05_Projektauftrag_Offene_Stadtkarte.docx','Koordination des Forschungsverbunds Offene Stadtkarte','24.08.2026','Universität an der Spree Berlin\nVizepräsidium Forschung','Prof. Dr. Simon Bergmann', '''Sehr geehrter Herr Professor Bergmann,

Sie übernehmen ab 01.10.2026 die wissenschaftliche Koordination des Verbunds Offene Stadtkarte. Der Verbund verbindet stadtbezogene Messdaten mit gemeinsam entwickelten Auswertungsmethoden. In der ersten Phase bis 31.03.2027 sind Datenvereinbarungen zwischen den beteiligten Einrichtungen, ein gemeinsamer Methodenworkshop und die Abstimmung des Erhebungsplans zu organisieren.

Die Projektplanung setzt dafür durchschnittlich einen Arbeitstag pro Woche an. Die Aufgaben werden neben Ihrer eigenen Teilprojektleitung wahrgenommen. Aus dem bewilligten Projektbudget steht keine Stelle für eine zentrale wissenschaftliche Koordination zur Verfügung. Eine studentische Hilfskraft unterstützt die Terminorganisation.

Das Vizepräsidium befürwortet, dass Sie für diese zusätzliche Aufgabe eine angemessene Entlastung in der Lehre beantragen. Mit diesem Auftrag wird noch keine konkrete Ermäßigung der Lehrverpflichtung bewilligt. Den Antrag richten Sie bitte über das Dekanat an die zuständige Stelle.

Mit freundlichen Grüßen
Dr. Oda Neumann'''),
X('06_Lehrplanung_WS2026_27.xlsx','Lehrplanung von Simon Bergmann',[dict(name='Planung',headers=['Veranstaltung','Einheiten à45 Minuten','Bezugswochen','LVS rechnerisch','Stand'],widths=[43,24,21,23,54],formats={'B':'0','C':'0','D':'0.00'},rows=[['Vorlesung Daten in der Stadt',30,15,'=B2/C2','Selbst geleitet; zwei Einheiten je Lehrwoche.'],['Seminargruppe 1',30,15,'=B3/C3','Selbst geleitet; eigenständige Gruppe.'],['Seminargruppe 2',30,15,'=B4/C4','Selbst geleitet; Vertretung nur angefragt.'],['Blockseminar Messdaten',45,15,'=B5/C5','45 Lehreinheiten ohne Pausen; Anrechnung angefragt.'],['Summe Plan',None,None,'=SUM(D2:D5)','Stand 28.09.2026; keine Veranstaltung abgesagt.'],['Regelverpflichtung',None,None,9,'Vollbeschäftigte W2-Universitätsprofessur.'],['Beantragte Ermäßigung',None,None,2,'Noch nicht bewilligt.'],['Bei Bewilligung verbleibend',None,None,'=D7-D8','Nur Rechenwert; keine Entscheidung.']],expected={'D6':9,'D9':7},perturbations=[{'input':'B5','value':30,'output':'D6','expected':8}]),dict(name='Blocktermine',headers=['Datum','Einheiten à45 Minuten','Gruppe','Inhalt'],widths=[19,27,26,65],formats={'B':'0'},rows=[['06.11.2026',9,'Ein gemeinsamer Kurs','Messreihen vorbereiten und erste gemeinsame Auswertung.'],['13.11.2026',9,'Ein gemeinsamer Kurs','Datenqualität und Dokumentation.'],['27.11.2026',9,'Ein gemeinsamer Kurs','Auswertungswerkstatt.'],['08.01.2027',9,'Ein gemeinsamer Kurs','Vergleich der Datensätze.'],['22.01.2027',9,'Ein gemeinsamer Kurs','Ergebniswerkstatt und Rückmeldung.'],['Summe', '=SUM(B2:B6)',None,'Pausen kommen hinzu und zählen nicht als Lehreinheiten.']],expected={'B7':45})]),
E('07_Lehrkalender.eml','Planungswochen im Wintersemester','2026-08-27T10:42:00+02:00','Studienbüro UAS <studium@uas-berlin.example>','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>', '''Lieber Herr Bergmann,

für unsere Lehrplanung des Wintersemesters 2026/27 rechnen wir mit 15 Lehrwochen zwischen 12.10.2026 und 05.02.2027. Die beiden Wochen vom 21.12.2026 bis 01.01.2027 bleiben vorlesungsfrei. Diese Planungszahl verwenden Sie bitte in der Übersicht zum Blockseminar.

Die Umrechnung der tatsächlich selbst gehaltenen Lehreinheiten ist mit der Deputatsstelle abzustimmen. Ein Termin umfasst bei Ihnen neun Einheiten zu je 45 Minuten zuzüglich Pausen. Bitte geben Sie nicht neun Zeitstunden ein; sonst entsteht eine andere Summe.

Freundliche Grüße
Lotte Winter'''),
D('08_Antrag_Ermaessigung.docx','Antrag auf Ermäßigung der Lehrverpflichtung','02.09.2026','Prof. Dr. Simon Bergmann','Universität an der Spree Berlin\nÜber das Dekanat an das Präsidium', '''Sehr geehrte Damen und Herren,

ich beantrage für das Wintersemester 2026/27 eine Ermäßigung meiner Lehrverpflichtung um zwei Lehrveranstaltungsstunden. Anlass ist die mir am 24.08.2026 übertragene wissenschaftliche Koordination des Verbunds Offene Stadtkarte. Die erste Projektphase erfordert durchschnittlich einen zusätzlichen Arbeitstag pro Woche und mehrere gemeinsame Workshops.

Der beigefügte Lehrplan umfasst zunächst neun Stunden einschließlich des Blockseminars. Im Fall einer Bewilligung könnte die zweite Seminargruppe mit zwei Stunden durch eine Lehrbeauftragte übernommen werden. Frau Dr. Eva Hellwig ist fachlich geeignet und grundsätzlich interessiert. Eine Beauftragung und ihre Finanzierung sind noch nicht erfolgt.

Die Vorlesung, die erste Seminargruppe und das Blockseminar würde ich selbst durchführen. Bitte entscheiden Sie möglichst bis Ende September, damit die Studierenden verlässlich planen können. Bis zu einer Entscheidung bleibt mein vollständiger Plan bestehen. Der frühere Bescheid für 2025/26 wird von mir nicht als fortgeltende Entlastung zugrunde gelegt.

Mit freundlichen Grüßen
Simon Bergmann'''),
E('09_Lehrbeauftragte_Interesse.eml','Seminargruppe im Winter','2026-09-04T17:33:00+02:00','Dr. Eva Hellwig <eva@hellwig-forschung.example>','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>', '''Lieber Simon,

die zweite Seminargruppe könnte ich fachlich gut übernehmen. Donnerstags von 14 bis 16 Uhr passt für mich. Ich brauche aber spätestens am 5. Oktober eine verbindliche Zusage und die Konditionen. Bis dahin halte ich den Termin vorläufig frei.

Die Betreuung einer Gruppe ist für mich etwas anderes als nur bei deinen Sitzungen dabei zu sein. Bitte klärt, ob ich die Gruppe eigenständig übernehmen soll. Solange der Lehrauftrag nicht erteilt ist, möchte ich im Vorlesungsverzeichnis noch nicht als Lehrende erscheinen.

Viele Grüße
Eva'''),
T('10_Telefonat_Dekanat.txt','Telefonnotiz zum Antrag','09.09.2026', '''Simon, 9. September, 11.20 Uhr, Gespräch mit Dekan Klein.
Anton meint, mein „alter Entlastungsfall“ sei doch schon bekannt. Ich sagte, der alte Bescheid endete im März und betraf das Archiv. Jetzt geht es um die Koordination des Verbunds.
Er hat die Tabelle auf dem Bildschirm. Er liest bei den beiden Seminargruppen zunächst zusammen zwei Stunden. Ich erläutere: zwei eigenständige Gruppen, beide von mir geplant, jede zwei Stunden. Wir sind am Telefon bei neun Stunden gelandet, sofern das Blockseminar mit drei zählt.
Er möchte die Deputatsstelle fragen und den Antrag in die nächste Sitzung geben. Ich habe keine mündliche Bewilligung verstanden.'''),
D('11_Fachbereichsrat_Auszug.docx','Auszug aus der Beratung zur Lehrplanung','16.09.2026','Universität an der Spree Berlin\nFachbereich Bildungswissenschaften, Geschäftsstelle','Prof. Dr. Simon Bergmann', '''Der Fachbereichsrat hat in seiner Sitzung vom 16.09.2026 den Antrag von Professor Bergmann auf Entlastung wegen der Verbundkoordination beraten. Der zusätzliche Koordinationsbedarf wird fachlich befürwortet. Der Dekan wird gebeten, die Finanzierung der vorgeschlagenen Lehrbeauftragung mit dem Präsidium zu klären.

In der Beratung wurde eine Ermäßigung um zwei Lehrveranstaltungsstunden für das Wintersemester 2026/27 unterstützt. Zugleich wurde darauf hingewiesen, dass die zuständige Stelle noch über den Antrag entscheidet. Die Lehrplanung darf bis dahin keine unbesetzte Seminargruppe ausweisen.

Die Studienbüroleitung berichtete, dass die Anrechnung des Blockseminars noch geprüft werde. Sie bittet um die genaue Zahl der Lehreinheiten ohne Pausen und um die Bestätigung, dass Professor Bergmann die Veranstaltung selbst durchführt.

Dieser Auszug wurde am 18.09.2026 durch die Geschäftsstelle versandt.
Mette Paul'''),
E('12_Nachfrage_Deputatsstelle.eml','Blockseminar und Gruppen im Lehrplan','2026-09-18T09:11:00+02:00','Deputatsstelle UAS <deputat@uas-berlin.example>','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>', '''Sehr geehrter Herr Bergmann,

in der ersten Meldung des Studienbüros waren die Seminargruppen zusammen mit zwei LVS erfasst. Bitte bestätigen Sie, dass Sie zwei getrennte Gruppen jeweils zwei Stunden selbst leiten. Zum Blockseminar benötigen wir die Termine und die Zahl der Lehreinheiten ohne Pausen.

Die bloße Mitarbeit an studentischen Projekten ist nicht automatisch eine zusätzliche Lehrveranstaltung. Bitte beschreiben Sie deshalb kurz den Ablauf Ihres Blockseminars. Über den Ermäßigungsantrag kann ich Ihnen noch keinen Entscheidungsstand mitteilen.

Freundliche Grüße
Frida Sommer'''),
D('13_Lehrplan_Erlaeuterung.docx','Erläuterung der selbst durchgeführten Lehre','21.09.2026','Prof. Dr. Simon Bergmann','Universität an der Spree Berlin\nDeputatsstelle', '''Sehr geehrte Frau Sommer,

die beiden Seminargruppen bestehen aus getrennten Teilnehmendenkreisen und werden im bisherigen Plan jeweils von mir persönlich unterrichtet. Jede Gruppe trifft sich einmal wöchentlich für zwei Lehreinheiten von je 45 Minuten. Die Veranstaltungen finden nicht gleichzeitig statt.

Das Blockseminar Messdaten ist eine eigenständige Lehrveranstaltung mit fünf Terminen und jeweils neun Lehreinheiten. Ich leite die gesamte Veranstaltung selbst. Es wechseln kurze Einführungen, angeleitete Auswertung und gemeinsame Besprechung. Die Pausen sind zusätzlich eingeplant und in den 45 Einheiten nicht enthalten. Der Arbeitsplan sieht keine Anrechnung privater Vorbereitungszeit der Studierenden vor.

In meiner Übersicht ergeben sich bei 15 Lehrwochen drei Stunden für das Blockseminar und zusammen neun Stunden für den vollständigen Plan. Bitte bestätigen Sie die anzusetzende Anrechnung. Falls der Ermäßigungsantrag bewilligt wird, soll nur die zweite Seminargruppe durch Frau Dr. Hellwig übernommen werden.

Mit freundlichen Grüßen
Simon Bergmann'''),
T('14_Teamchat_Lehrplan.txt','Teamchat Studienorganisation','23.09.2026', '''23.09.2026 09:06 Lotte: Im Entwurf steht Eva schon bei Gruppe 2. Ist der Auftrag durch?
23.09.2026 09:09 Simon: Nein, noch nicht. Bitte bis zur Entscheidung meinen Namen drinlassen.
23.09.2026 09:12 Lotte: Danke. Ich hatte das aus der Sitzung als fest übernommen.
23.09.2026 09:16 Simon: Wir brauchen auch noch die Bestätigung zum Blockseminar. Die Termine stehen, ich halte sie frei.
23.09.2026 09:22 Lotte: Habe die Veröffentlichung angehalten. Die Raumreservierungen bleiben bestehen.
23.09.2026 09:28 Simon: Gut, die Studierenden sollen eine klare Fassung bekommen.'''),
E('15_Praesidium_Zwischenstand.eml','Antrag LV-26-113','2026-09-25T12:38:00+02:00','Präsidialbüro UAS <praesidium@uas-berlin.example>','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>', '''Sehr geehrter Herr Professor Bergmann,

Ihr Antrag liegt mit der Stellungnahme des Fachbereichs vor. Es fehlt noch die haushaltsseitige Bestätigung für den vorgeschlagenen Lehrauftrag. Die Entscheidung wird in der Sitzung am 06.10.2026 vorbereitet.

Bis zu einer gesonderten Entscheidung gilt Ihre bisherige Lehrverpflichtung. Die Unterstützungsbekundung im Fachbereichsrat ist uns bekannt. Sie stellt noch keine Bewilligung dar. Wir bemühen uns wegen des nahen Vorlesungsbeginns um eine rechtzeitige Rückmeldung.

Freundliche Grüße
Mette Paul'''),
D('16_Arbeitsaufwand_September.docx','Aufgaben in der Startphase des Verbunds','28.09.2026','Prof. Dr. Simon Bergmann','Eigene Projektablage', '''In der Woche vom 21. bis 25. September habe ich zusätzlich zur üblichen Teilprojektarbeit zwei Abstimmungen mit Partnerhochschulen vorbereitet, die gemeinsame Datenstruktur überarbeitet und den Auftaktworkshop organisiert. Dafür habe ich rund acht Stunden aufgewendet. Die Hilfskraft konnte Einladungen und Raumbuchungen übernehmen, nicht jedoch die fachlichen Vereinbarungen.

Für Oktober sind drei gemeinsame Arbeitsrunden vorgesehen. Die Partner benötigen vor den eigenen Erhebungen ein einheitliches Vorgehen. Wenn die Koordination unverändert bei mir bleibt und der volle Lehrplan bestehen bleibt, muss ich eigene Datenauswertungen nach hinten verschieben. Ich habe hierfür bislang keinen neuen Zeitplan mit dem Projektträger vereinbart.

Ich möchte die zusätzliche Aufgabe weiter wahrnehmen. Der Verbund arbeitet gut zusammen. Für eine Entlastung an anderer Stelle wäre auch eine Aufteilung der Koordination denkbar, sofern die Partner und das Vizepräsidium zustimmen. Bisher ist dazu nichts verabredet.

Simon Bergmann'''),
E('17_Deputatsstelle_Rueckfrage.eml','Ihre Erläuterung vom 21. September','2026-09-29T10:07:00+02:00','Deputatsstelle UAS <deputat@uas-berlin.example>','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>', '''Sehr geehrter Herr Bergmann,

die zwei getrennten Seminargruppen sind nun entsprechend erfasst. Die Übersicht weist deshalb insgesamt neun rechnerische Stunden aus. Beim Blockseminar wird die Bestätigung der Lehrform noch mit dem Studienbüro abgeschlossen. Ihre fünf Termine mit 45 Lehreinheiten sind dabei zugrunde gelegt.

Bitte bewahren Sie nach Durchführung die tatsächlich gehaltenen Termine auf. Eine spätere Übernahme der zweiten Gruppe durch Frau Hellwig muss in beiden Lehrnachweisen eindeutig abgebildet werden. Für dieselbe Gruppe können nicht gleichzeitig Ihnen und ihr die vollen Stunden zugerechnet werden.

Freundliche Grüße
Frida Sommer'''),
E('18_Nachtrag_Bergmann.eml','Vollständiger Plan bleibt vorerst bestehen','2026-09-30T16:42:00+02:00','Prof. Dr. Simon Bergmann <simon.bergmann@uas-berlin.example>','Moritz Seidel <post@campus-stadt.example>', '''Sehr geehrter Herr Seidel,

Frau Hellwig hält ihren Termin noch bis 5. Oktober frei. Die Sitzung des Präsidiums ist erst am 6. Oktober. Das sollten wir in einer möglichen Rückfrage ansprechen. Ich werde die Gruppe bis zu einer klaren Übernahme selbst vorbereiten.

Mein Wunsch ist eine Entscheidung über die beantragten zwei Stunden und eine klare Aufgabenverteilung. Ich will weder eine frühere Ermäßigung einfach fortschreiben noch Lehrstunden doppelt anrechnen. Bitte erläutern Sie mir auch eine sinnvolle Vorgehensweise, falls die Universität den Antrag ablehnt.

Mit freundlichen Grüßen
Simon Bergmann''')]))

CASES.append(dict(slug='berlin-professur-forschungslabor',title='Tareks Messlabor und die gemeinsame Raumnutzung',plugin=HOCHSCHULE,date='30.09.2026',client='Prof. Dr. Tarek Linden',summary='Ein Berliner Universitätslabor soll zugunsten gemeinsamer Nutzung umziehen. Professor Linden unterstützt die Idee, benötigt für seine Klimasensoren jedoch ununterbrochene Messfenster, ausreichende Arbeitsflächen und Klarheit über zweckgebundene Mittel.',assignment='Der Professor bittet um Prüfung der Raum- und Mittelentscheidung und um einen Vorschlag für eine sachliche Intervention vor dem geplanten Umzug. Eine funktionsfähige gemeinsame Nutzung bleibt sein Ziel.',documents=[
D('01_Auftrag_Linden.docx','Räume und Mittel für das Messlabor','30.09.2026','Prof. Dr. Tarek Linden\nUniversität an der Spree Berlin, Institut für Stadtforschung','Rechtsanwalt Moritz Seidel\nKanzlei Campus und Stadt, Berlin', '''Sehr geehrter Herr Seidel,

bitte prüfen Sie die Entscheidung, unser Labor im November von W-118 nach W-043 zu verlegen und die frei werdende Fläche gemeinsam zu nutzen. Ich unterstütze die Zusammenarbeit mit der Nachbargruppe. Die bislang angebotenen Zeitfenster passen aber nicht zu den mehrtägigen Vergleichsmessungen unserer Sensoren.

Nach dem Protokoll der Raumkommission wurde angenommen, dass wir nur werktags einzelne Stunden benötigen. Meine im August übersandte Projektbeschreibung nennt dagegen drei ununterbrochene Messläufe von jeweils 48 Stunden. Offenbar war der letzte Teil der Beschreibung in der Sitzungsmappe nicht dabei. Der kleinere Ersatzraum hat außerdem noch keine ausreichenden Anschlüsse.

Parallel wurden 18.000 Euro aus unserem laufenden Sachmittelansatz in einen gemeinsamen Gerätepool verschoben. Ein Teil unserer Bestellungen hängt an einer gesonderten Projektförderung. Bitte klären Sie, welche Unterlagen wir benötigen und wie wir vor dem Umzug verbindlich zu einer funktionsfähigen Lösung kommen.

Mit freundlichen Grüßen
Tarek Linden'''),
D('02_Raumzuweisung_2023.docx','Nutzung des Labors W 118','15.09.2023','Universität an der Spree Berlin\nDekan und Gebäudeservice','Prof. Dr. Tarek Linden', '''Sehr geehrter Herr Professor Linden,

dem Arbeitsbereich Stadtklima und Sensorsysteme wird ab 01.10.2023 Raum W-118 mit einer Nutzfläche von 78 Quadratmetern zur Verfügung gestellt. Die Zuweisung dient dem Aufbau und der Durchführung von Messreihen sowie der Aufbewahrung der zugehörigen Geräte. Die regulären Lehrveranstaltungen bleiben in den zentral geplanten Lehrräumen.

Die Nutzung wird im Rahmen der weiteren Raumplanung überprüft. Änderungen werden mit dem Arbeitsbereich und dem Gebäudeservice abgestimmt. Eine dauerhafte ausschließliche Nutzung gerade dieses Raumes wird nicht zugesagt. Bei der Planung sind die dokumentierten Funktionen des Labors zu berücksichtigen.

Bitte benennen Sie eine verantwortliche Kontaktperson für Schlüssel, Geräte und Zugang. Der Raum darf nur für die vorgesehenen Hochschulaufgaben genutzt werden. Der Gebäudeservice führt die vorhandenen Strom- und Netzwerkanschlüsse in seinem Bestandsplan.

Mit freundlichen Grüßen
Prof. Dr. Anton Klein'''),
E('03_Projektbewilligung.eml','Projekt Stadtklimasensoren beginnt im Oktober','2026-07-02T13:24:00+02:00','Forschungsfonds UAS <foerderung@uas-berlin.example>','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>', '''Sehr geehrter Herr Linden,

Ihr Teilprojekt Stadtklimasensoren wird für die Zeit vom 01.10.2026 bis 30.09.2027 mit 48.000 Euro aus dem universitären Forschungsfonds unterstützt. Davon entfallen 30.000 Euro auf Sensorik und Kalibrierung sowie 18.000 Euro auf studentische Unterstützung und Messfahrten.

Die Mittel sind entsprechend dem genehmigten Arbeitsplan zu verwenden. Änderungen zwischen diesen beiden Ansätzen stimmen Sie bitte vorab mit uns ab. Die erste Vergleichsreihe ist für November vorgesehen. Der Zwischenbericht wird zum 31.03.2027 erwartet.

Freundliche Grüße
Oda Neumann'''),
D('04_Projektbeschreibung_Raum.docx','Raumbedarf für die Vergleichsmessungen','12.08.2026','Prof. Dr. Tarek Linden','Universität an der Spree Berlin\nRaumkommission', '''Unser Labor prüft kleine Temperatursensoren für Messungen im Stadtraum. Im kommenden Winter vergleichen wir die Geräte unter denselben Umgebungsbedingungen. Die Arbeit erfordert keine medizinischen oder biologischen Versuche. Benötigt werden sechs zusammenhängende Arbeitstische, ein abschließbarer Schrank und eine stabile Strom- und Netzwerkversorgung.

Für die Auswertung reichen an vielen Tagen zwei Bildschirmplätze. Die Messaufbauten selbst dürfen während laufender Vergleichsreihen nicht umgesetzt werden. Die bisherige Raumfläche von 78 Quadratmetern enthält auch Flächen für Material, das wir gemeinsam mit der Nachbargruppe aufbewahren könnten.

Im November sind drei Messläufe von jeweils 48 Stunden ohne Unterbrechung vorgesehen. Dafür benötigen wir Zugang auch am Abend und zwischen den üblichen Buchungsfenstern. Die Sensoren laufen überwiegend selbstständig, eine Person kontrolliert den Aufbau zweimal täglich. Ein Umsetzen zwischen zwei Buchungen würde den jeweiligen Vergleichslauf unbrauchbar machen.

Eine gemeinsame Nutzung ist gut möglich, wenn diese Messfenster frühzeitig festgelegt werden. Wir können die drei Läufe innerhalb des Novembers verschieben, benötigen aber mindestens zwei Wochen Vorlauf zur Abstimmung mit den Partnern.

Prof. Dr. Tarek Linden'''),
E('05_Uebersendung_Raumbedarf.eml','Raumkommission Bedarf unseres Labors','2026-08-12T15:39:00+02:00','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>','Raumkommission UAS <raumkommission@uas-berlin.example>', '''Liebe Frau Paul,

anbei die Beschreibung unseres Raumbedarfs. Besonders wichtig ist der Abschnitt über die drei ununterbrochenen Messläufe im November. Die reine Zahl von Bildschirmarbeitsplätzen bildet den Bedarf deshalb nicht ab.

Ich bin vom 17. bis 28. August im Urlaub. Meine Kollegin Dr. Elif Rahn kann in dieser Zeit an einer Begehung teilnehmen und die Aufbauten erläutern. Wir sind für eine gemeinsame Nutzung offen, wenn die Messläufe möglich bleiben.

Die Datei heißt 04_Projektbeschreibung_Raum.docx.

Viele Grüße
Tarek Linden'''),
T('06_Teamchat_Begehung.txt','Arbeitsgruppenchat zur Raumbegehung','24.08.2026', '''24.08.2026 11:12 Elif: War gerade mit Mira in W-043. Zwei lange Tische passen, sechs einzelne eher nicht. Es gibt nur zwei freie Netzwerkdosen.
24.08.2026 11:15 Tarek: Danke. Habt ihr die 48-Stunden-Läufe besprochen?
24.08.2026 11:19 Elif: Ja. Mira dachte, das wäre im Besprechungsraum daneben möglich. Der ist aber abends abgeschlossen.
24.08.2026 11:22 Tarek: Bitte halte das in der Notiz fest. Ich bin Montag wieder da.
24.08.2026 11:28 Elif: Mach ich. Die Nachbargruppe ist freundlich, wir wollen nur vorher wissen, wann welcher Aufbau stehenbleiben darf.'''),
D('07_Begehung_W043.docx','Begehung des Ersatzraumes W 043','24.08.2026','Dr. Elif Rahn\nArbeitsbereich Stadtklima und Sensorsysteme','Prof. Dr. Tarek Linden und Gebäudeservice', '''Bei der Begehung waren Mira Hart vom Gebäudeservice und ich anwesend. W-043 hat 46 Quadratmeter. Zwei große Tische sind vorhanden. Zusätzliche Tische würden die Durchgänge stark einschränken. Für die vorgesehenen sechs Messplätze wäre eine andere Möblierung nötig.

Es gibt zwei nutzbare Netzwerkanschlüsse. Weitere Anschlüsse können nach Aussage von Frau Hart installiert werden; ein Termin steht noch nicht fest. Der Raum hat einen normalen Transponderzugang. Der benachbarte Raum W-045 wird nach 18 Uhr zentral verschlossen und kann nicht ohne zusätzliche Freigabe für laufende Messungen genutzt werden.

Ich habe erläutert, dass die Messaufbauten 48 Stunden stehenbleiben müssen. Frau Hart möchte prüfen, ob W-045 während der drei Messläufe zusammenhängend bereitgestellt werden kann. Wir haben noch keine konkrete Belegung vereinbart. Einen Umzugstermin konnte ich für die Arbeitsgruppe nicht bestätigen.

Elif Rahn'''),
X('08_Laborplanung_und_Mittel.xlsx','Messfenster und Projektmittel',[dict(name='Messfenster',headers=['Lauf','Geplanter Beginn','Dauer Stunden','Messplätze','Platzstunden','Status'],widths=[18,26,23,20,22,56],formats={'C':'0','D':'0','E':'0'},rows=[['Vergleich 1','03.11.2026',48,6,'=C2*D2','Beginn 09 Uhr; bis 05.11. 09 Uhr ohne Umsetzen.'],['Vergleich 2','10.11.2026',48,6,'=C3*D3','Beginn 09 Uhr; Termin mit Partner abstimmbar.'],['Vergleich 3','24.11.2026',48,6,'=C4*D4','Beginn 09 Uhr; Termin mit Partner abstimmbar.'],['Summe',None,'=SUM(C2:C4)',None,'=SUM(E2:E4)','Drei getrennte Messläufe.']],expected={'C5':144,'E5':864},perturbations=[{'input':'D2','value':4,'output':'E5','expected':768}]),dict(name='Projektmittel',headers=['Ansatz','Bewilligt Euro','Bereits gebunden Euro','Verfügbar Euro','Zweck'],widths=[33,24,27,25,56],formats={'B':'#,##0.00','C':'#,##0.00','D':'#,##0.00'},rows=[['Sensorik und Kalibrierung',30000,24600,'=B2-C2','Forschungsfonds Stadtklimasensoren.'],['Hilfskräfte und Messfahrten',18000,6200,'=B3-C3','Forschungsfonds Stadtklimasensoren.'],['Summe Projekt', '=SUM(B2:B3)','=SUM(C2:C3)','=SUM(D2:D3)','Getrennt vom allgemeinen Sachmittelansatz.'],['Allgemeine Sachmittel',36000,11000,'=B5-C5','Vor der Poolzuweisung laut Dekanat.'],['In Gerätepool übertragen',18000,None,None,'Mitteilung vom 14.09.; interne Buchung noch offen.']],expected={'D4':17200,'D5':25000})]),
E('09_Einladung_Raumkommission.eml','Sitzung der Raumkommission am 9. September','2026-09-01T09:31:00+02:00','Raumkommission UAS <raumkommission@uas-berlin.example>','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>', '''Lieber Herr Linden,

die Raumkommission berät am 09.09.2026 um 10 Uhr über die gemeinsame Nutzung der Laborflächen. Ihre schriftliche Bedarfsmeldung liegt vor. Sie können Ihren Bedarf zu Beginn der Sitzung für etwa zehn Minuten erläutern. Bitte geben Sie uns bis Freitag Bescheid, ob Sie teilnehmen können.

Auf der Tagesordnung stehen die Verlagerung Ihres Arbeitsbereichs nach W-043 und die gemeinsame Nutzung von W-118 durch zwei Gruppen. Eine endgültige Umzugsanordnung erlässt die Kommission nicht selbst; sie legt ihre Empfehlung dem Dekanat vor.

Freundliche Grüße
Mette Paul'''),
E('10_Bitte_um_Zuschaltung.eml','Teilnahme an der Raumkommission','2026-09-03T12:07:00+02:00','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>','Raumkommission UAS <raumkommission@uas-berlin.example>', '''Liebe Frau Paul,

am 9. September leite ich bis 10.30 Uhr einen bereits lange vereinbarten Workshop. Könnten Sie meinen Punkt danach aufrufen oder mich für zehn Minuten digital zuschalten? Elif ist an diesem Tag bei einer Messfahrt. Die schriftliche Beschreibung sollte den Bedarf vollständig enthalten.

Bitte achten Sie besonders auf die ununterbrochenen Messfenster im November. Wenn ich vorher nichts höre, gehe ich davon aus, dass Sie die Unterlagen beraten und wir anschließend die Einzelheiten besprechen. Einen Umzug zum 1. November habe ich bislang nicht zugesagt.

Viele Grüße
Tarek Linden'''),
D('11_Protokoll_Raumkommission.docx','Auszug aus der Sitzung der Raumkommission','09.09.2026','Universität an der Spree Berlin\nGeschäftsstelle der Raumkommission','Dekanat und beteiligte Arbeitsbereiche', '''Die Raumkommission empfiehlt, den Arbeitsbereich Stadtklima und Sensorsysteme zum 01.11.2026 nach W-043 zu verlagern. W-118 soll künftig als gemeinsam buchbares Labor genutzt werden. Die bisherige exklusive Nutzung erscheint nach der vorliegenden Bedarfsmeldung nicht erforderlich.

In der Sitzung lag eine Kurzfassung der Beschreibung vom 12.08.2026 vor. Sie endete nach dem Absatz über den Bedarf an Bildschirmplätzen. Darin werden sechs Arbeitstische und an vielen Tagen zwei Bildschirmplätze genannt. Der Gebäudeservice hält eine Nutzung von W-043 zusammen mit zeitweisen Buchungen von W-045 für möglich. Einzelne Tagesfenster sollen im gemeinsamen Kalender abgestimmt werden.

Professor Linden war nicht anwesend. Seine Bitte um eine spätere Behandlung oder digitale Zuschaltung konnte wegen des engen Zeitplans nicht umgesetzt werden. Die Kommission empfiehlt dem Dekanat, die technischen Voraussetzungen vor dem Umzug durch den Gebäudeservice bestätigen zu lassen.

Die Empfehlung wurde mit vier Ja-Stimmen und einer Enthaltung angenommen. Eine Entscheidung über gesondert bewilligte Projektmittel war nicht Gegenstand der Sitzung.

Mette Paul'''),
D('12_Dekan_Raum_und_Pool.docx','Raumplanung und gemeinsamer Gerätepool','14.09.2026','Universität an der Spree Berlin\nDekanat des Fachbereichs','Prof. Dr. Tarek Linden', '''Sehr geehrter Herr Professor Linden,

auf Grundlage der Empfehlung der Raumkommission wird Ihr Arbeitsbereich ab 01.11.2026 in W-043 untergebracht. W-118 wird ab diesem Zeitpunkt gemeinsam genutzt. Bitte stimmen Sie den Umzug mit dem Gebäudeservice ab. Die erforderlichen Anschlüsse sollen vor Beginn der Nutzung hergestellt sein.

Für die gemeinsame Geräteausstattung werden 18.000 Euro aus dem allgemeinen Sachmittelansatz Ihres Arbeitsbereichs dem Gerätepool des Fachbereichs zugeordnet. Die Einzelbeschaffungen werden mit den beteiligten Arbeitsbereichen abgestimmt. Gesondert zweckgebundene Projektmittel sind damit nicht zur freien Verwendung freigegeben.

Wir erwarten von der gemeinsamen Nutzung eine bessere Auslastung und möchten zugleich Ihre laufenden Projekte ermöglichen. Bitte übermitteln Sie dem Gebäudeservice Ihre konkreten Buchungswünsche. Sollten bei der technischen Vorbereitung Schwierigkeiten auftreten, ist das Dekanat unverzüglich zu informieren.

Mit freundlichen Grüßen
Prof. Dr. Anton Klein'''),
T('13_Telefonnotiz_Finanzservice.txt','Gespräch zur Umbuchung','16.09.2026', '''Tarek, 16.09., 15.10 Uhr, Telefonat mit Carla Ivers.
Carla sagt, die 18.000 Euro sollen aus den allgemeinen Sachmitteln kommen. Das Projektkonto mit 48.000 Euro bleibt getrennt. Die Umbuchung ist im System noch nicht vollzogen.
Ich habe gefragt, was mit den bereits gebundenen 11.000 Euro der allgemeinen Sachmittel passiert. Sie sagte, diese Bestellungen würden erfüllt; wie viel danach für eigene neue Bestellungen verbleibt, müsse sie mit dem Dekanat abstimmen.
Wir haben vereinbart, dass ich die Liste der gebundenen Beträge sende. Carla hat keine Zusage gemacht, den Poolbeschluss zurückzunehmen.'''),
D('14_Bitte_erneute_Befassung.docx','Messfenster und technische Voraussetzungen','18.09.2026','Prof. Dr. Tarek Linden','Universität an der Spree Berlin\nDekanat und Raumkommission', '''Sehr geehrter Herr Professor Klein, sehr geehrte Mitglieder der Raumkommission,

ich bitte um erneute Befassung mit der vorgesehenen Verlagerung. Im Protokoll steht, dass nur eine Kurzfassung meiner Bedarfsmeldung vorlag. Der darin fehlende Teil erläutert die drei 48-stündigen Messläufe im November. Eine Nutzung in einzelnen Tagesfenstern genügt dafür nicht.

Ich bin bereit, die Termine innerhalb des Novembers abzustimmen und Materialien gemeinsam zu lagern. Bitte bestätigen Sie vor einer verbindlichen Umzugsplanung, wo sechs Messplätze zusammenhängend aufgebaut bleiben können, wann die Strom- und Netzwerkanschlüsse nutzbar sind und wie der Zugang außerhalb üblicher Öffnungszeiten geregelt wird.

Die Projektmittel und die allgemeinen Sachmittel sind in meiner Übersicht getrennt. Bitte teilen Sie mir mit, wie die bereits gebundenen 11.000 Euro des allgemeinen Ansatzes bei der Poolzuweisung berücksichtigt werden. Ich möchte vermeiden, dass dieselben Mittel in zwei Planungen erscheinen.

Mit freundlichen Grüßen
Tarek Linden'''),
E('15_Partnergruppe_Zeitfenster.eml','Gemeinsame Nutzung im November','2026-09-22T17:06:00+02:00','Prof. Dr. Judith Brandt <judith.brandt@uas-berlin.example>','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>', '''Lieber Tarek,

wir können W-118 für eure drei Messläufe zusammenhängend freihalten, wenn die Termine bis Mitte Oktober feststehen. Unsere eigenen Übungen liegen im November meist montags und freitags. Dienstagnachmittag bis Donnerstagnachmittag wäre daher am einfachsten.

Dein erster Vorschlag beginnt dienstags schon um 9 Uhr; da haben wir noch einen Aufbau stehen. Lass uns die sechs Stunden besprechen. Mir ist wichtig, dass wir nicht während einer laufenden Messung räumen müssen. Auch unsere Gruppe braucht ein paar feste Schränke.

Viele Grüße
Judith'''),
D('16_Technikstand_Gebaeudeservice.docx','Technischer Stand vor der Laborverlagerung','25.09.2026','Universität an der Spree Berlin\nGebäudeservice, Mira Hart','Dekanat und Prof. Dr. Tarek Linden', '''Für W-043 ist die Erweiterung um vier Netzwerkanschlüsse und einen zusätzlichen Stromkreis geplant. Das ausführende Unternehmen hat bislang den 16.11.2026 als frühesten Termin genannt. Eine frühere Ausführung wird angefragt. Bis zur Erweiterung können zwei Messplätze an den vorhandenen Anschlüssen betrieben werden.

Für W-045 ist eine zeitlich befristete zusätzliche Zugangsfreigabe technisch möglich. Sie muss durch die Raumverwaltung eingerichtet werden. Eine konkrete Freigabe für die drei Messläufe liegt noch nicht vor. W-118 bleibt bis zu einer abgestimmten Übergabe technisch unverändert nutzbar.

Ein Transport der empfindlichen Messgeräte soll durch den bestehenden Rahmenvertrag erfolgen. Der Auftrag ist noch nicht erteilt. Wir bitten um eine gemeinsame Festlegung des Umzugstermins, sobald die Entscheidung zu Messfenstern und Ersatzflächen vorliegt.

Mira Hart
Gebäudeservice'''),
E('17_Dekanat_Terminangebot.eml','Besprechung der Laborplanung','2026-09-28T11:52:00+02:00','Prof. Dr. Anton Klein <dekan@uas-berlin.example>','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>', '''Lieber Tarek,

deine vollständige Bedarfsmeldung einschließlich der Messfenster ist jetzt in der Sitzungsablage. Wir sollten die Messläufe und den technischen Termin gemeinsam mit Judith und Mira besprechen. Ich schlage den 7. Oktober um 14 Uhr vor.

Der allgemeine Umzugstermin steht bislang noch im Plan. Ich habe den Gebäudeservice aber gebeten, vor unserem Gespräch keinen Transportauftrag auszulösen. Die 18.000 Euro für den Gerätepool werden getrennt auf die Tagesordnung genommen. Bitte bring die Übersicht über die gebundenen allgemeinen Sachmittel mit.

Viele Grüße
Anton'''),
E('18_Nachtrag_Linden.eml','Gemeinsame Nutzung bleibt mein Ziel','2026-09-30T18:04:00+02:00','Prof. Dr. Tarek Linden <tarek.linden@uas-berlin.example>','Moritz Seidel <post@campus-stadt.example>', '''Sehr geehrter Herr Seidel,

Judiths Vorschlag könnte eine Lösung sein. Wir müssten die drei Messläufe jeweils auf Dienstagnachmittag verschieben und in W-118 stehenlassen. Das wäre fachlich vertretbar, wenn Zugang und feste Arbeitsplätze gesichert sind. Für die Zwischenzeiten könnten zwei Rechner in W-043 genügen.

Bitte prüfen Sie die Unterlagen mit diesem Ziel. Ich beanspruche keinen Raum für immer, benötige aber eine belastbare Arbeitsmöglichkeit für das bewilligte Projekt. Vor dem Gespräch am 7. Oktober hätte ich gern eine Einschätzung zur Raumentscheidung und zur Mittelzuweisung.

Mit freundlichen Grüßen
Tarek Linden''')]))
