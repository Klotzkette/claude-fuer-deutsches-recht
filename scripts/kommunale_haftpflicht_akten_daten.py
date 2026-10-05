"""Drei kleine kommunale Haftpflichtakten mit nativen Quellen, ohne Musterlösung."""

def D(file, title, day, sender, body):
    return dict(file=file, title=title, date=day, sender=sender, body=body.strip())

def E(file, title, day, sender, recipient, body):
    return dict(file=file, title=title, date=day, **{'from': sender, 'to': recipient}, body=body.strip())

CASES = [
dict(slug='kommunale-haftpflicht-personenschaden', title='Ottilie Kümmel im Bürgerhaus',
summary='Ein Sturz auf nassen Fliesen, eine nachgetragene Reinigungskontrolle und überschaubare Forderungen aus einer Handgelenksverletzung.',
core=['01_Pruefauftrag.eml','02_Ereignismeldung.docx','03_Behandlungsbericht.docx','04_Reinigungskontrolle.docx','07_Forderung_Kuemmel.eml','11_Teamchat.txt'],
xlsx=[], attachments={'07_Forderung_Kuemmel.eml':['03_Behandlungsbericht.docx','05_Haushaltshilfe_Rechnung.docx','06_Jacke_Kaufbeleg.docx']},
documents=[
E('01_Pruefauftrag.eml','Bürgerhaus: Bitte um erste Einschätzung und Antwortentwurf','2026-10-05T08:10:00+02:00','Mira Morgenrot <recht@hainbogen.example>','Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Guten Morgen Frau Klee,

ich beauftrage Sie für die Stadt Hainbogen mit der Prüfung des Vorfalls vom 12. September im städtischen Bürgerhaus. Eigentümerin und Betreiberin des Hauses ist die Stadt; den Bücherabend veranstaltete unser Kulturamt selbst. Eintritt wurde nicht erhoben. Der Reinigungsdienst wurde von eigenen Beschäftigten geleistet.

Bitte geben Sie uns bis 7. Oktober eine kurze Einschätzung zu Grund und Umfang möglicher Ansprüche und einen Antwortentwurf an Frau Kümmel. Ihre Forderung enthält eine Antwortbitte bis 9. Oktober. Unterscheiden Sie bitte das, was wir bereits belegen können, von dem, was wir noch erfragen müssen. Besonders ärgert mich die erst am Folgetag eingetragene Kontrolle; ich möchte wissen, was der Eintrag tatsächlich trägt.

Eine Zahlung oder ein Anerkenntnis ist noch nicht erfolgt. Bitte versenden Sie vor unserer Freigabe nichts. Unsere Vertragsunterlagen zur Versicherung habe ich angefordert; die Korrespondenz dazu liegt bei.

Freundliche Grüße
Mira Morgenrot, Rechtsamt'''),
D('02_Ereignismeldung.docx','Ereignismeldung Bürgerhaus','13.09.2026','Stadt Hainbogen · Bürgerhaus · Hausmeister Ludger Lauch', '''## 1 Ort und Veranstaltung

Am Samstag, 12. September 2026, fand im Bürgerhaus am Buchsbaumplatz 4, Hainbogen, ein öffentlicher Bücherabend statt. Der Eingang war ab 17:30 Uhr geöffnet. Vor der inneren Saaltür liegt eine Schmutzfangmatte; zwischen Außentür und Matte befinden sich helle Fliesen. Am Nachmittag hatte es geregnet. Gegen 18 Uhr war es draußen nach meiner Erinnerung trocken.

## 2 Sturz und Hilfe

Um 18:08 Uhr wurde ich aus dem Saal zum Eingang gerufen. Frau Ottilie Kümmel saß links neben der Matte auf dem Boden und hielt ihr linkes Handgelenk. Sie sagte: „Auf der glatten Stelle bin ich weggerutscht.“ Ich sah einen etwa handtellergroßen nassen Bereich auf den Fliesen vor der Matte. Ich habe den Sturz selbst nicht gesehen und kann weder die Ursache der Nässe noch deren Dauer angeben.

Wir holten einen Stuhl, betreuten Frau Kümmel und verständigten ihre Tochter. Ein Rettungswagen brachte sie zur Behandlung. Der Eingangsbereich wurde um 18:12 Uhr gesperrt und trocken gewischt. Vor meinem Eintreffen habe ich dort kein Warnschild gesehen. Ob zuvor eines aufgestellt war, weiß ich nicht.

## 3 Unterlagen und Rückfrage

Die Kontrolle am Eingang war dem Reinigungsdienst übertragen. Ich bat Celine Kaya am Sonntag um ihren Eintrag im Kontrollblatt. Der Teamchat ist gespeichert. Eine Kamera gibt es im Eingangsbereich nicht. Frau Kümmel trug flache Schuhe; eine Prüfung der Sohlen fand nicht statt.

Ludger Lauch, niedergeschrieben am 13. September um 10:20 Uhr.'''),
D('03_Behandlungsbericht.docx','Ambulanter Behandlungsbericht','12.09.2026','Ambulanz Kleeweg · Dr. Indira Klee · Hainbogen', '''Patientin: Ottilie Kümmel, geboren am 16. Februar 1959. Vorstellung am 12. September 2026 um 19:05 Uhr in Begleitung ihrer Tochter. Die Patientin berichtet über einen Sturz auf die linke Hand im Bürgerhaus. Rechtshändigkeit wird angegeben.

## 1 Befund

Schwellung und Druckschmerz am linken Handgelenk; Durchblutung, Motorik und Sensibilität der Finger bei Untersuchung erhalten. In der Röntgenuntersuchung zeigt sich eine nicht verschobene distale Radiusfraktur links. Es erfolgt eine Ruhigstellung im Unterarmgips. Es bestehen keine dokumentierten Hinweise auf eine weitere akute Verletzung.

## 2 Weiteres Vorgehen

Die Patientin erhält Hinweise zur Gipskontrolle und zur sofortigen Wiedervorstellung bei zunehmenden Beschwerden. Eine ambulante Verlaufskontrolle in der folgenden Woche wird empfohlen. Belastendes Tragen und Arbeiten mit der linken Hand sollen zunächst unterbleiben. Eine konkrete Stundenzahl für Hilfe im Haushalt wurde heute nicht erhoben.

Eine abschließende Aussage zur Heilungsdauer oder zu bleibenden Folgen ist am heutigen Behandlungstag nicht möglich. Die Patientin nimmt den Bericht für ihre Unterlagen mit.

Dr. Indira Klee'''),
D('04_Reinigungskontrolle.docx','Kontrollblatt Eingang Bürgerhaus','13.09.2026','Stadt Hainbogen · Reinigungsdienst · Celine Kaya', '''Veranstaltung: Bücherabend am 12. September 2026. Bereich: Außentür, Fliesen und Schmutzfangmatte vor dem Saal. Dienstzeit Celine Kaya: 16:30 bis 19:00 Uhr.

## 1 Eintrag zur Kontrolle

17:30 Uhr: Matte lag flach. Sichtkontrolle des Eingangs ohne Besonderheit.

17:55 Uhr: Nach meiner Erinnerung bin ich am Eingang vorbeigegangen. Ich habe damals keinen deutlich nassen Fleck gesehen. Ich habe nicht mit der Hand geprüft, ob die Fliesen trocken waren. Ich trug einen vollen Abfallsack und war auf dem Weg zum Hof.

18:12 Uhr: Nach Meldung eines Sturzes wurde der Eingangsbereich abgesperrt. Ich wischte die Stelle vor der Matte trocken und stellte ein Warnschild auf. Um 18:20 Uhr gab Herr Lauch den Weg wieder frei.

## 2 Erstellungszeit

Dieses Blatt habe ich auf Bitte von Herrn Lauch am 13. September um 09:40 Uhr ausgefüllt. Während des Bücherabends hatte ich die Kontrollen nicht schriftlich festgehalten. Die Uhrzeit 17:55 Uhr ist aus meiner Erinnerung an den Schichtablauf übernommen; ich habe dazu keinen Zeitstempel.

Celine Kaya'''),
D('05_Haushaltshilfe_Rechnung.docx','Rechnung HK-260922','22.09.2026','Haushaltsservice Hedwig Hummel · Gartenbogen 6, Hainbogen · rechnung@hummel-hilfe.example', '''Rechnungsempfängerin: Ottilie Kümmel, Lerchenbogen 8, Hainbogen.

Leistungszeitraum: 14. bis 21. September 2026. Vereinbarter Stundensatz: 25,00 EUR netto.

Am 14. September: Einkauf und Küche, 2 Stunden. Am 16. September: Wäsche und Bad, 3 Stunden. Am 18. September: Einkauf und Böden, 3 Stunden. Am 21. September: Wäsche und Bettwäsche, 2 Stunden. Insgesamt wurden 10 Stunden geleistet.

Nettobetrag: 250,00 EUR. Umsatzsteuer 19 Prozent: 47,50 EUR. Rechnungsbetrag: 297,50 EUR.

Zahlbar innerhalb von sieben Tagen auf die bereits mitgeteilte Bankverbindung. Zahlungsbestätigung vom 23. September 2026: Der Rechnungsbetrag von 297,50 EUR ist vollständig eingegangen.

Hedwig Hummel'''),
D('06_Jacke_Kaufbeleg.docx','Kassenbeleg JK-250408','08.04.2025','Jackenkontor Liesel Lenz · Marktlaube 3, Hainbogen', '''Verkauf am 8. April 2025 um 11:36 Uhr.

Damenjacke „Gartenabend“, Größe 40, dunkelgrün, Artikel G40: 89,90 EUR einschließlich Umsatzsteuer. Enthaltene Umsatzsteuer bei 19 Prozent: 14,35 EUR. Zahlung per Karte: 89,90 EUR.

Ein Artikel. Keine weiteren Käufe auf diesem Beleg.

Vielen Dank für Ihren Einkauf.

Jackenkontor Liesel Lenz'''),
E('07_Forderung_Kuemmel.eml','Mein Sturz beim Bücherabend – Belege','2026-09-28T10:42:00+02:00','Ottilie Kümmel <ottilie.kuemmel@briefpost.example>','Mira Morgenrot <recht@hainbogen.example>', '''Sehr geehrte Frau Morgenrot,

ich bitte die Stadt um 2.500 EUR Schmerzensgeld. Seit dem Sturz bin ich im Alltag erheblich eingeschränkt. Dazu kommen 297,50 EUR Haushaltshilfe und 89,90 EUR für meine Jacke, die beim Sturz am linken Ärmel aufgerissen ist. Der Kaufbeleg ist von April letzten Jahres; neu gekauft habe ich noch keine. Für zwei Taxifahrten zur Kontrolle habe ich insgesamt 36 EUR bezahlt, die Quittungen suche ich noch.

Anbei erhalten Sie den Bericht der Ambulanz, die Rechnung mit Zahlungsbestätigung und den Jackenbeleg als drei Dateien. Ich lebe allein. Meine Tochter kann nur am Wochenende helfen. Ich habe zusätzlich aufgeschrieben, was mir im Haushalt schwerfiel.

Ich war nicht in Eile und habe kein Warnschild gesehen. Mit dem Handy habe ich mich im Eingang nicht beschäftigt. Bitte antworten Sie bis zum 9. Oktober. Mir wäre eine vernünftige Einigung lieber als monatelanger Schriftverkehr.

Freundliche Grüße
Ottilie Kümmel'''),
E('08_Zeugin_Lina.eml','Was ich im Eingang gesehen habe','2026-09-29T16:35:00+02:00','Lina Okafor <lina@lesekreis.example>','Mira Morgenrot <recht@hainbogen.example>', '''Guten Tag,

ich stand am 12. September links neben dem Büchertisch, etwa drei Meter vom Eingang entfernt. Frau Kümmel ging normal herein. Kurz vor der Matte rutschte ihr ein Fuß weg; welchen Fuß, kann ich nicht mehr sicher sagen. Sie hielt kein Handy in der Hand.

Nach dem Sturz sah ich Wasser oder eine andere klare Flüssigkeit auf den Fliesen. Die Matte selbst fühlte sich an der Stelle, an der ich mit der Hand aufstützte, trocken an. Ich kann nicht sagen, ob jemand etwas verschüttet hatte oder ob die Nässe von draußen kam. Ich war erst wenige Minuten vorher angekommen. Ein Warnschild habe ich vor dem Sturz nicht wahrgenommen.

In der Gruppe schrieb ich damals „alles nass“. Damit meinte ich die unmittelbare Sturzstelle, nicht den ganzen Eingangsbereich.

Beste Grüße
Lina Okafor'''),
E('09_Reinigung_Rueckfrage.eml','Kontrollblatt: Uhrzeit ist Erinnerung','2026-09-30T09:18:00+02:00','Celine Kaya <celine.kaya@hainbogen.example>','Mira Morgenrot <recht@hainbogen.example>', '''Hallo Frau Morgenrot,

ja, das Kontrollblatt habe ich erst sonntags ausgefüllt. 17:55 war ungefähr die Zeit, zu der ich mit dem Müll durch den Eingang ging. Ich habe nicht auf eine Uhr geschaut. Vielleicht war es auch ein paar Minuten früher.

Die Chatnachricht von 18:03 habe ich erst nach dem Sturz gelesen. Mein Telefon lag im Nebenraum am Ladegerät. Ich hatte keine gesonderte Vertretung dafür vereinbart. Den gelben Aufsteller holte ich nach dem Zuruf aus dem Putzraum; vorher hatte ich ihn nicht im Eingang aufgestellt.

Ich möchte bitte, dass aus meinem Eintrag nicht „um 17:55 sicher trocken“ gemacht wird. So genau habe ich nicht hingesehen.

Celine'''),
E('10_Vertragsunterlagen.eml','Bürgerhaus – Versicherungspapiere noch im Altarchiv','2026-10-02T11:06:00+02:00','Gundula Pfennig <risiken@hainbogen.example>','Mira Morgenrot <recht@hainbogen.example>', '''Liebe Mira,

im aktuellen Ordner liegt nur eine Prämienbuchung mit dem Stichwort Haftpflicht. Daraus kann ich weder den versicherten Zeitraum noch Bedingungen, Selbstbehalt oder Meldeweg ablesen. Den vollständigen Vertrag habe ich beim Altarchiv angefordert. Eine Deckungsentscheidung liegt nicht vor.

Ob für diesen Bereich ein kommunaler Schadenausgleich oder eine Rückdeckung besteht, kann ich heute nicht belegen. Bitte keine entsprechende Zugehörigkeit oder Zusage nach außen behaupten. Ich brauche von Euch die genaue Ereignisbeschreibung und eine Liste der angemeldeten Positionen; danach kann ich die Vertragsunterlagen gezielt abgleichen und die Meldung vorbereiten.

Viele Grüße
Gundula'''),
D('11_Teamchat.txt','Bücherabend – Chatexport Eingang','12.09.2026','', '''18:03 Farid: Vor der Matte glänzt eine kleine Pfütze. Kann jemand mit dem Wischer kommen? Ich stehe an der Kasse und kann hier gerade nicht weg.
18:04 Ludger: Bin im Saal am Mikro, gleich.
18:08 Farid: Frau gestürzt, bitte jetzt zum Eingang!
18:09 Ludger: Bin da, bitte Eingang links freihalten.
18:10 Lina: Alles nass da. Ich bleibe bei der Dame.
18:12 Celine: Wische jetzt. Schild steht.
18:20 Ludger: Stelle trocken, Eingang wieder offen.

Exportiert von Farid Mansour am 13.09.2026. Diese Gruppe zeigt keine Lesebestätigungen an.'''),
D('12_Alltag_Kuemmel.docx','Meine Notizen nach dem Sturz','27.09.2026','Ottilie Kümmel · Lerchenbogen 8, Hainbogen', '''Ich bin Rentnerin und wohne allein in einer Wohnung mit 64 Quadratmetern. Vor dem Sturz habe ich nach meiner Schätzung etwa zwölf Stunden pro Woche eingekauft, gekocht, geputzt und Wäsche versorgt. Gartenarbeit fällt bei mir nicht an.

In der ersten Woche konnte ich mit der rechten Hand kleine Brote zubereiten und mich weitgehend selbst anziehen. Töpfe, einen vollen Wäschekorb und die Einkaufstasche konnte ich nicht sicher tragen. Beim Haarewaschen half mir am Sonntag meine Tochter. Sie war an den beiden Wochenenden jeweils ungefähr zwei Stunden für Einkäufe und Wäsche da. Geld hat sie dafür nicht verlangt.

Frau Hummel war an vier Tagen insgesamt zehn Stunden hier. Ihre Zeiten stehen auf der Rechnung. Das war teils dieselbe Arbeit, die sonst ich erledigt hätte; zusätzliche Hilfe meiner Tochter war hauptsächlich am Wochenende nötig. Eine getrennte Stundenliste meiner Tochter haben wir nicht geführt.

Die linke Hand schmerzte nachts besonders in der ersten Woche. Die Kontrollpraxis hat den Gips bisher belassen. Einen aktuellen schriftlichen Befund habe ich noch nicht angefordert. Ob etwas zurückbleibt, hat mir niemand gesagt.

Ottilie Kümmel'''),
]),
dict(slug='akha-wuerzburg-rohrbruch', title='Würzburg: Wasser bei Zimt & Zange',
summary='Ein Leck in einer Straßenleitung, drei gebrauchte Kaffeemühlen und vier geschlossene Verkaufstage. Die Vertragsunterlagen zur Deckung und Rückdeckung fehlen.',
core=['01_Pruefauftrag.eml','02_Schadenmeldung.docx','03_Einsatzbericht.docx','07_Kostenuebersendung.eml','09_Vertragsanfrage.eml','12_Kostenliste.xlsx'],
xlsx=['12_Kostenliste.xlsx'], attachments={'07_Kostenuebersendung.eml':['04_Trocknung_Rechnung.docx','06_Elektro_Angebot.docx']},
documents=[
E('01_Pruefauftrag.eml','Rohrbruch Würzburg – erste Prüfung bis Mittwoch','2026-10-05T08:35:00+02:00','Mira Morgenrot <recht@mainbogen-versorgung.example>','Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Sehr geehrte Frau Klee,

die Kommunalversorgung Mainbogen GmbH beauftragt Sie mit der ersten Prüfung des Rohrbruchs vom 14. September in Würzburg. Wir betreiben die Straßenverteilungsleitung am Gewerbehof Kaffeebogen 6. Der Laden Zimt & Zange im Erdgeschoss meldet Schäden aus dem darunterliegenden Lagerkeller.

Bitte ordnen Sie Haftungsgrund und Forderungspositionen anhand der beigefügten Unterlagen und entwerfen Sie eine kurze Nachforderungsliste. Den Ort des Lecks bitte genau aus dem Einsatzbericht übernehmen. Frau Waffel ist Gebäudeeigentümerin, nicht Betreiberin unseres Straßennetzes.

Unsere Risikostelle hat im Ablagesystem eine alte Rubrik „AKHA/Rückdeckung“ gefunden, aber keine Vertragsurkunde. Daraus soll ausdrücklich keine Mitgliedschaft oder Deckungsaussage abgeleitet werden. Wir brauchen getrennt eine Liste der Unterlagen, die wir für die Prüfung von Versicherung oder Schadenausgleich und einer etwaigen Rückdeckung anfordern müssen. Bitte keine Kontaktaufnahme oder Meldung ohne unsere Freigabe.

Rückmeldung an uns bitte bis 7. Oktober. Herr Zimt hat um eine Nachricht bis 12. Oktober gebeten.

Mit freundlichen Grüßen
Mira Morgenrot'''),
D('02_Schadenmeldung.docx','Schadenmeldung Lagerkeller','19.09.2026','Eberhard Zimt · Zimt & Zange Kaffeemaschinenwerkstatt · Kaffeebogen 6, Würzburg', '''Am Montag, 14. September 2026, öffnete Mira Ben Ami gegen 06:50 Uhr die Kellertür und sah Wasser auf dem Boden. Gegen 07:20 Uhr stand das Wasser an der tiefsten Stelle etwa zwölf Zentimeter hoch. Wir riefen die Kommunalversorgung an. Erst dachten wir, ein Rohr unserer Heizung sei geplatzt.

Im Keller lagerten drei eigene, gebrauchte Vorführmühlen. Sie standen auf niedrigen Rollbrettern. Wasser gelangte in die Gehäuse; wir haben sie seitdem nicht eingeschaltet. Außerdem waren Steckdosen und der untere Teil der Wand feucht. Den Raum konnten wir nicht nutzen.

Der Laden blieb vom 14. bis einschließlich 17. September geschlossen. Wir beliefern auch Kunden vor Ort, konnten aber ohne unsere Werkstatt und sichere Elektrik nicht normal arbeiten. Ab 18. September verkauften wir wieder; Reparaturarbeiten im Keller blieben ausgesetzt.

Das Geschäft führe ich als Einzelunternehmer. Die drei Mühlen gehören meinem Betrieb. Den Laden mit Keller habe ich von Walburga Waffel gemietet. Die Lieferbelege und eine Aufstellung zum Alter der Mühlen lege ich nach. Ich bitte um Ersatz unserer Kosten und der ausgefallenen Geschäftseinnahmen.

Eberhard Zimt'''),
D('03_Einsatzbericht.docx','Einsatzbericht Wasserleitung Kaffeebogen','14.09.2026','Kommunalversorgung Mainbogen GmbH · Netzbetrieb · Severin Sprosse', '''## 1 Einsatz und Befund

Störmeldung eingegangen um 07:04 Uhr. Absperrung des Leitungsabschnitts um 07:42 Uhr. Bei der Freilegung um 09:15 Uhr wurde ein Längsriss in der Straßenverteilungsleitung gefunden. Die freigelegte Stelle liegt im öffentlichen Gehwegbereich etwa 1,5 Meter vor der Außenwand von Kaffeebogen 6 und damit außerhalb des Gebäudes. Es handelt sich nicht um die Leitung hinter dem Wasserzähler im Keller.

Nach dem internen Netzplan und unserer Anlagenkartei steht diese Verteilungsleitung im Eigentum der Kommunalversorgung Mainbogen GmbH; Betrieb, Kontrolle und Absperrung übernimmt unser Netzteam. Einen Grundbuch- oder Vertragsnachweis habe ich dieser Meldung nicht beigefügt. Das ausgebaute Rohrstück wird im Betriebshof aufbewahrt. Eine Materialuntersuchung steht noch aus.

## 2 Wasserweg und Wiederinbetriebnahme

An der Durchführung der Versorgungsleitungen in der Kelleraußenwand trat bei unserer Ankunft Wasser ein. Nach Absperrung der Straßenleitung ließ dieser Eintritt deutlich nach. Im Keller fanden wir bei unserer Sichtkontrolle kein erkennbar gebrochenes Heizungsrohr; der Heizungsdruck blieb laut Anzeige unverändert. Eine vollständige Gebäudeprüfung war nicht Gegenstand unseres Einsatzes.

Wir ersetzten das gerissene Stück und nahmen die Leitung um 13:30 Uhr nach Druckprüfung wieder in Betrieb. Die Ursache des Risses und die Dichtigkeit der Kellerwanddurchführung sind noch nicht abschließend untersucht.

Severin Sprosse, Einsatzleiter'''),
D('04_Trocknung_Rechnung.docx','Rechnung TR-260918','18.09.2026','Trockenwerk Tilda Tuch GmbH · Werkbogen 3, Würzburg · rechnung@trockenwerk.example', '''An Eberhard Zimt, Zimt & Zange, Kaffeebogen 6, Würzburg.

Auftrag vom 14. September 2026. Einsatzort: Lagerkeller Kaffeebogen 6. Leistungen vom 14. bis 18. September: Abpumpen und Erstaufnahme 600,00 EUR netto; Bereitstellung und Betrieb der Trocknungsgeräte 1.200,00 EUR netto; Reinigung und Feuchtemessungen 600,00 EUR netto.

Nettosumme: 2.400,00 EUR. Umsatzsteuer 19 Prozent: 456,00 EUR. Rechnungsbetrag: 2.856,00 EUR.

Die Abrechnung umfasst keine Instandsetzung der Elektroanlage und keinen Ersatz der gelagerten Mühlen. Geräte wurden am 18. September abgeholt. An der Wand bleibt weiterer Prüfbedarf bestehen.

Zahlungseingang am 19. September 2026: 2.856,00 EUR vollständig erhalten.

Tilda Tuch, Geschäftsführerin'''),
D('05_Muehlen_Bestandsliste.docx','Bestandsliste der drei Vorführmühlen','21.09.2026','Zimt & Zange · Eberhard Zimt', '''Standort vor dem Wassereintritt: Lagerkeller Kaffeebogen 6, links neben der Werkbank. Alle drei Mühlen gehörten dem Betrieb und waren regelmäßig als Vorführgeräte im Einsatz. Es handelt sich um denselben Modelltyp „Mahlfink M2“.

Mühle ZZ-01: gekauft im Februar 2023 für 2.000,00 EUR netto. Mühle ZZ-02: gekauft im Juni 2023 für 2.000,00 EUR netto. Mühle ZZ-03: gekauft im Januar 2024 für 2.000,00 EUR netto. Der Gesamtbetrag der damaligen Anschaffungen war 6.000,00 EUR netto.

Der Lieferant hat mir am Telefon für drei neue gleichartige Geräte einen Preis von jeweils 2.500,00 EUR netto genannt. Auf dieser Grundlage verlange ich 7.500,00 EUR netto. Eine schriftliche Offerte liegt mir noch nicht vor. Die historischen Kaufrechnungen habe ich im Archiv angefordert.

Ob die Mühlen repariert werden können, ist bisher nicht untersucht. Ein Händler meinte unverbindlich, vielleicht seien noch rund 200 EUR pro Stück als Teileträger erzielbar. Dafür gibt es weder ein Kaufangebot noch einen tatsächlichen Erlös. Ich habe nichts entsorgt.

Eberhard Zimt'''),
D('06_Elektro_Angebot.docx','Angebot EL-260920','20.09.2026','Elektro Elmar Eule · Werkstattkranz 2, Würzburg · elmar@elektro-eule.example', '''An Eberhard Zimt, Zimt & Zange, Kaffeebogen 6, Würzburg.

Nach der Besichtigung am 19. September bieten wir die Prüfung der betroffenen Kellerstromkreise, den Austausch von vier Steckdosen und zugehörigen Leitungsabschnitten sowie die abschließende Messung an.

Arbeitszeit: 16 Stunden zu 75,00 EUR netto = 1.200,00 EUR. Material und Messpauschale: 600,00 EUR netto. Nettobetrag: 1.800,00 EUR. Umsatzsteuer 19 Prozent: 342,00 EUR. Gesamtbetrag: 2.142,00 EUR.

Das Angebot setzt voraus, dass sich kein weiterer Schaden an der Hauptverteilung zeigt. Es gilt bis 15. Oktober 2026. Ein Auftrag wurde noch nicht erteilt. Die betroffenen Kellerstromkreise bleiben bis zur Freigabe abgeschaltet; der Verkaufsraum verfügt über einen getrennten Stromkreis.

Elmar Eule'''),
E('07_Kostenuebersendung.eml','Belege und mein vorläufiger Betrag','2026-09-25T13:16:00+02:00','Eberhard Zimt <eberhard@zimt-zange.example>','Mira Morgenrot <recht@mainbogen-versorgung.example>', '''Sehr geehrte Frau Morgenrot,

anbei die bezahlte Trocknungsrechnung und das Elektroangebot als zwei Word-Dateien. Dazu rechne ich 7.500 EUR netto für neue Mühlen und 3.400 EUR für die vier Tage, an denen wir geschlossen hatten. Zusammen mit 2.400 EUR netto Trocknung und 1.800 EUR netto Elektrik ergibt das vorläufig 15.100 EUR.

Ich bin für diese betrieblichen Eingangsleistungen zum Vorsteuerabzug berechtigt und fordere die dort ausgewiesene Umsatzsteuer nicht zusätzlich. Die Elektroarbeiten sind noch nicht bestellt. Vielleicht kann Frau Waffel einen Teil übernehmen; verbindlich zugesagt hat sie nichts. Eine doppelte Erstattung will ich selbstverständlich nicht.

Bitte geben Sie mir bis zum 12. Oktober eine Rückmeldung, welche Unterlagen Ihnen noch fehlen. Die Mühlen stehen weiterhin im Keller und können besichtigt werden.

Freundliche Grüße
Eberhard Zimt'''),
E('08_Vermieterin.eml','Kaffeebogen 6 – Wanddurchführung und Mietvertrag','2026-09-28T09:22:00+02:00','Walburga Waffel <walburga@waffel-immobilien.example>','Mira Morgenrot <recht@mainbogen-versorgung.example>', '''Guten Morgen,

ich bin Eigentümerin des Hauses Kaffeebogen 6. Den Verkaufsraum und den Keller habe ich an Herrn Zimt vermietet. Unsere Hausleitung beginnt hinter dem Kellerwasserzähler. Für die Straßenleitung habe ich keine Betriebsbefugnis. Herr Sprosse zeigte mir das ausgetauschte Rohrstück draußen im Gehweg.

Die Wanddurchführung ist älter. Ob sie schon vor dem Vorfall undicht war, weiß ich nicht. In den letzten zwei Jahren hat mir Herr Zimt keinen Wassereintritt gemeldet. Mietvertrag und Wasserliefervertrag liegen noch im Papierordner meines Verwalters; ich lasse sie heraussuchen. Ich kann daher heute auch keine vertragliche Kostenteilung für die Elektroarbeiten nennen.

Die Reparatur der Kellerwand habe ich noch nicht beauftragt. Eine eigene bezifferte Forderung erhebe ich mit dieser Nachricht nicht.

Mit freundlichen Grüßen
Walburga Waffel'''),
E('09_Vertragsanfrage.eml','Versicherung, Schadenausgleich, Rückdeckung: Unterlagen fehlen','2026-10-02T14:40:00+02:00','Gundula Pfennig <risiken@mainbogen-versorgung.example>','Mira Morgenrot <recht@mainbogen-versorgung.example>', '''Liebe Mira,

die Ablagerubrik „AKHA/Rückdeckung“ ist vorhanden, enthält aber nur einen leeren Unterordner aus einer früheren Bestandsaufnahme. Ich habe keinen Beitrittsnachweis, keine Satzung oder Bedingungen für unseren Betrieb und keinen aktuellen Deckungs- oder Rückdeckungsvertrag gefunden. Auch ein für den Schaden bestätigter Selbstbehalt oder eine Leistungsgrenze ist nicht dokumentiert.

Ich habe deshalb heute bei unserer kaufmännischen Leitung die vollständigen Unterlagen einschließlich Nachträgen, Laufzeiten und zuständiger Meldestelle angefordert. Bis dahin kann ich nicht sagen, ob und wie diese Angelegenheit dort überhaupt angeschlossen ist. Bitte für die Anfrage Haftungsprüfung, etwaige Deckung und etwaige Rückdeckung getrennt aufführen.

Nach außen wurde noch keine Deckungszusage erteilt. Eine Haftungsanerkennung unserer Gesellschaft gibt es ebenfalls nicht.

Gundula'''),
E('10_Umsatz_Rueckfrage.eml','Die 3.400 EUR sind Umsatz, noch keine Gewinnrechnung','2026-10-01T17:05:00+02:00','Eberhard Zimt <eberhard@zimt-zange.example>','Mira Morgenrot <recht@mainbogen-versorgung.example>', '''Hallo Frau Morgenrot,

die 850 EUR pro Tag habe ich aus vier vergleichbaren Septembertagen des Vorjahres übernommen, also viermal 850 EUR = 3.400 EUR. Das sind die Nettoumsätze laut meiner Kasse. Eine Berechnung des entgangenen Gewinns ist das noch nicht. Wareneinsatz und ersparte Kosten habe ich nicht herausgerechnet.

Einige Kunden haben ihre Reparaturaufträge nur verschoben. Wie viel davon später nachgeholt wurde, kann meine Buchhalterin erst nächste Woche sagen. Personalkosten und Miete liefen weiter. Ich lasse Kassenberichte, Auftragsliste und die betreffenden Einkaufsrechnungen zusammenstellen.

Freundliche Grüße
Eberhard Zimt'''),
D('11_Stoerungslog.txt','Störungsannahme Kaffeebogen','14.09.2026','', '''07:04 Mira Ben Ami meldet Wasser im Keller. Vermutung Anruferin: „Vielleicht unsere Heizung.“
07:10 Netzteam alarmiert, Severin Sprosse übernimmt.
07:42 Straßenabschnitt abgesperrt. Rückmeldung Team: Wassereintritt im Keller nimmt ab.
09:15 Team meldet Riss an freigelegter Straßenverteilungsleitung vor Haus 6.
10:05 Eberhard Zimt fragt nach Ersatz seiner Mühlen. Disposition verweist zur Schadenbearbeitung; keine Kostenübernahme zugesagt.
13:30 Leitung nach Reparatur und Druckprüfung wieder freigegeben.
15:20 Trocknungsfirma arbeitet im Keller. Elektrische Prüfung separat erforderlich.

Auszug erstellt am 15.09.2026 durch Disponentin Yasmin Zobel.'''),
]),
dict(slug='akha-wuerzburg-betriebsfahrzeug', title='Würzburg: Die Kehrmaschine am Hallentor',
summary='Eine rollende Kehrmaschine, Gebäudeschaden, eine vorläufig hohe Geräteforderung und ein Nachbar mit reiner Umsatzausfallmeldung.',
core=['01_Pruefauftrag.eml','02_Unfallmeldung.docx','05_Geraete_Aufstellung.docx','09_Nachbarbetrieb.eml','10_Vertragsunterlagen.eml','12_Forderungsuebersicht.xlsx'],
xlsx=['12_Forderungsuebersicht.xlsx'], attachments={'07_Gebaeudeeigentuemerin.eml':['04_Bau_Angebot.docx'],'08_Geraeteeigentuemerin.eml':['05_Geraete_Aufstellung.docx']},
documents=[
E('01_Pruefauftrag.eml','Kehrmaschine Würzburg – Ansprüche und nächste Schritte','2026-10-05T09:02:00+02:00','Gundula Pfennig <schaden@frankenbogen-versicherung.example>','Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Sehr geehrte Frau Klee,

ich beauftrage Sie ausschließlich für die Frankenbogen Kommunalversicherung VVaG mit einer ersten Einschätzung zum Unfall der Kehrmaschine unserer Versicherungsnehmerin Stadtbetriebe Steinbogen GmbH am 25. September im Gewerbehof Hallenbogen 12 in Würzburg. Ein Vertretungsauftrag der Stadtbetriebe wird damit nicht erteilt. Frau Morgenrot hat uns die beigefügten Betriebsunterlagen und Anspruchstellernachrichten zur Schadenprüfung übermittelt.

Laut Betriebsbericht ist die Stadtbetriebe Steinbogen GmbH Halterin und Eigentümerin der Maschine; Herr Blech fuhr im Rahmen seines Dienstes. Das Gelände ist während der Geschäftszeiten ohne Zugangskontrolle für Lieferverkehr geöffnet.

Es liegen drei Forderungen vor. Die Geräteforderung ist hoch, aber noch nicht durch einen Sachverständigen geprüft. Bitte stellen Sie Haftungsgrundlagen, Schäden und benötigte Belege für jede geschädigte Person getrennt dar. Wir benötigen daneben eine vorläufige Großschadeneinschätzung und eine Liste der Fragen zur Deckung und etwaigen Rückdeckung. Vertragsbestand und fehlende Unterlagen erläutert meine Nachricht vom 2. Oktober; konkrete Grenzen dürfen nicht aus der Höhe der Anmeldung abgeleitet werden.

Unsere Schadenleitung benötigt bis 7. Oktober eine Übersicht und einen Entwurf an Frau Morgenrot zur weiteren Sachaufklärung. Keine Zahlung, kein Anerkenntnis und keine externe Meldung ohne unsere Freigabe. Gebäudesicherung und Beweissicherung laufen laut Stadtbetrieben bereits. Das Fahrzeug wird mit der internen Betriebsnummer 7 bezeichnet.

Mit freundlichen Grüßen
Gundula Pfennig, Schadenbearbeitung'''),
D('02_Unfallmeldung.docx','Unfallmeldung Fahrzeug 7','25.09.2026','Stadtbetriebe Steinbogen GmbH · Fuhrpark · Burkhard Blech', '''## 1 Ablauf

Am 25. September 2026 um etwa 09:14 Uhr hielt ich die Kehrmaschine Nummer 7 im Gewerbehof Hallenbogen 12 an, um eine umgefallene Absperrbake zu entfernen. Die bauartbedingte Höchstgeschwindigkeit beträgt laut unserer Fahrzeugkarte 40 km/h. Der Motor lief, das Kehraggregat war ausgeschaltet. Ich stieg aus. Nach wenigen Sekunden rollte die Maschine vorwärts gegen das Hallentor. Das Tor wurde nach innen gedrückt und stieß gegen dahinter abgestellte Transportgestelle.

Ich glaube, den Hebel der Feststellbremse angezogen zu haben. Ob er vollständig eingerastet war, kann ich nach dem Schreck nicht sicher sagen. Das leichte Gefälle hatte ich unterschätzt. Andere Personen wurden nach meiner Wahrnehmung nicht getroffen.

## 2 Unmittelbare Folgen

Das Hallentor und angrenzendes Mauerwerk waren beschädigt. Die Halle wurde geräumt und abgesperrt. Auf Anweisung des hinzugezogenen Elektrikers wurde die gemeinsame Stromversorgung dieses Hofabschnitts vorsorglich bis zum Abend abgeschaltet. Der Nachbarbetrieb Nuri Nudelwerk konnte in dieser Zeit nicht produzieren.

Die Kehrmaschine wurde gesichert und in die Werkstatt gebracht. Ich habe seitdem nichts an der Bremse verstellt. Die Werkstatt soll den technischen Zustand dokumentieren. Ich habe keinem Betroffenen eine Entschädigung zugesagt.

Burkhard Blech

Nachtrag der Fuhrparkleitung vom 28. September: Bis heute liegt uns keine Personenschadenmeldung vor.'''),
D('03_Zeugin_Samira.docx','Beobachtung am Hallenbogen','28.09.2026','Samira Schwan · Kurierdienst Schwan · samira@schwan-kurier.example', '''Ich wartete am 25. September kurz nach neun mit meinem Lastenrad im Gewerbehof Hallenbogen 12. Ein orangefarbenes Fahrzeug stand einige Meter vor dem Hallentor. Ein Mann stieg aus und ging zu einer Bake. Dann bewegte sich das Fahrzeug langsam vorwärts. Ich hörte einen lauten Schlag und sah, dass das Tor nach innen stand.

Am Telefon habe ich später von einem „Lieferwagen“ gesprochen. Das war ungenau. Als ich näher kam, sah ich seitliche Bürsten und den Schriftzug Stadtbetriebe Steinbogen. Es war die Kehrmaschine. Wie der Fahrer die Bremse bedient hatte, konnte ich aus meinem Winkel nicht sehen.

Hinter dem Tor lagen Metallgestelle und schwarze Kisten übereinander. Wie viele Geräte darin beschädigt waren, weiß ich nicht. Ich sah keine verletzte Person. Mein eigenes Rad blieb unbeschädigt.

Samira Schwan, niedergeschrieben am 28. September 2026.'''),
D('04_Bau_Angebot.docx','Vorläufiges Angebot HB-260929','29.09.2026','Baukontor Balduin Balken GmbH · Werkplatz 8, Würzburg · angebot@balken-bau.example', '''An Hofbogen Immobilien GmbH, Hallenbogen 12, Würzburg.

Nach Besichtigung des beschädigten Hallentors am 28. September bieten wir vorbehaltlich der Öffnung der Wandanschlüsse folgende Arbeiten an:

Ausbau, Entsorgung und Ersatz des Hallentors: 68.000,00 EUR netto. Instandsetzung von Sturz, Mauerwerk und Anschlüssen: 52.000,00 EUR netto. Baustelleneinrichtung, Hebetechnik und vorübergehender Verschluss: 25.000,00 EUR netto.

Vorläufiger Nettobetrag: 145.000,00 EUR. Umsatzsteuer 19 Prozent: 27.550,00 EUR. Vorläufiger Bruttobetrag: 172.550,00 EUR.

Das Angebot enthält keinen Ersatz von Mieterausstattung, keine Mietausfälle und keine Schäden an gelagerten Geräten. Verdeckte Schäden sind nicht bewertet. Eine statische Freigabe ist vor Ausführung erforderlich. Der Auftrag wurde noch nicht erteilt. Bisherige Sicherungsarbeiten sind in diesem Angebot nicht nochmals als gesonderte Rechnung abgerechnet.

Balduin Balken'''),
D('05_Geraete_Aufstellung.docx','Vorläufige Aufstellung beschädigter Veranstaltungstechnik','30.09.2026','Prisma Bühnenbildtechnik GmbH · Hallenbogen 12, Würzburg · Juno Kühn', '''Die nachstehenden Geräte gehören nach unserer Anlagenliste der Prisma Bühnenbildtechnik GmbH. Sie standen hinter dem Hallentor auf zwei Transportgestellen. Das eingedrückte Tor verschob die Gestelle; Gehäuse und sichtbare Anschlüsse wurden beschädigt. Eine vollständige technische Funktionsprüfung steht aus.

20 LED-Wandmodule der Serie P, angeschafft 2023/2024: vorläufiger Ersatzansatz je 45.000 EUR netto, zusammen 900.000 EUR. 6 Medienserver, angeschafft 2022/2023: je 75.000 EUR netto, zusammen 450.000 EUR. 10 Projektionsmodule, angeschafft 2024: je 30.000 EUR netto, zusammen 300.000 EUR. Summe der vorläufigen Neupreisansätze: 1.650.000 EUR netto.

Die Geräte sind gebraucht. Die Ansätze stammen aus unserer aktuellen Beschaffungsliste und sind weder Zeitwerte noch geprüfte Reparaturkosten. Seriennummern, Kaufrechnungen und Wartungsprotokolle werden noch zugeordnet. Die Zahl der tatsächlich irreparablen Geräte steht nicht fest. Verwertungsangebote liegen nicht vor; nichts wurde entsorgt.

Unser technischer Leiter nennt als grobe Spanne 1.200.000 bis 2.100.000 EUR netto, abhängig vom Reparaturumfang und der Verfügbarkeit gleichwertiger Geräte. Diese Spanne betrifft allein die Geräte, nicht Gebäude oder Nachbarbetrieb. Die Mitte dieser Spanne wurde nicht als Sachverständigenwert bestätigt.

Juno Kühn, kaufmännische Leitung'''),
D('06_Werkstattauftrag.docx','Prüfauftrag Kehrmaschine 7','28.09.2026','Stadtbetriebe Steinbogen GmbH · Fuhrparkleitung · Hedwig Hummel', '''An die Werkstatt, zu Händen Farid Fink.

Bitte dokumentieren Sie den Zustand der Kehrmaschine Nummer 7 nach dem Ereignis vom 25. September. Bis zur Befundaufnahme darf sie nicht wieder eingesetzt werden. Der Schlüssel liegt versiegelt in der Fuhrparkverwaltung; der Fahrer meldet keine nachträgliche Betätigung der Feststellbremse.

Zu prüfen und zu dokumentieren sind insbesondere Stellung und Funktion der Feststellbremse, Betätigungskräfte, sichtbare Defekte und der Stand der letzten Wartung. Eine Probefahrt soll erst nach Freigabe und gesicherter Befundaufnahme stattfinden. Bitte erhalten Sie ausgebaute Teile.

Die letzte turnusmäßige Wartung ist im Kalender für August vermerkt. Das unterschriebene Wartungsblatt ist noch nicht im Fahrzeugordner. Bitte suchen Sie es heraus. Ein technischer Defekt wird mit diesem Auftrag weder bestätigt noch ausgeschlossen.

Eingangsvermerk Werkstatt, 2. Oktober: Fahrzeug gesichert. Vollständiger Prüfbericht voraussichtlich am 8. Oktober. Noch keine Freigabe zur Wiederinbetriebnahme.

Hedwig Hummel'''),
E('07_Gebaeudeeigentuemerin.eml','Hallentor: Angebot und Forderung','2026-09-30T08:17:00+02:00','Kunigunde Knopf <kunigunde@hofbogen-immobilien.example>','Mira Morgenrot <recht@steinbogen-betriebe.example>', '''Sehr geehrte Frau Morgenrot,

für die Hofbogen Immobilien GmbH mache ich zunächst 145.000 EUR netto für die Beschädigung unseres Hallentors und des angrenzenden Mauerwerks geltend. Das vorläufige Bauangebot ist beigefügt. Unsere Gesellschaft ist Eigentümerin der Halle. Wir sind hinsichtlich dieser Aufwendungen zum Vorsteuerabzug berechtigt.

Die Veranstaltungstechnik in der Halle gehört der Mieterin Prisma Bühnenbildtechnik und ist in unserer Forderung nicht enthalten. Über Mietausfälle sprechen wir gegebenenfalls später; dazu beziffere ich heute nichts. Den Auftrag zur vollständigen Reparatur haben wir noch nicht erteilt, weil die statische Freigabe aussteht.

Bitte bestätigen Sie bis zum 9. Oktober, dass die Angelegenheit bei Ihnen bearbeitet wird.

Mit freundlichen Grüßen
Kunigunde Knopf, Geschäftsführerin'''),
E('08_Geraeteeigentuemerin.eml','Prisma: vorläufige Geräteforderung und Besichtigung','2026-10-01T11:28:00+02:00','Juno Kühn <juno@prisma-buehnentechnik.example>','Mira Morgenrot <recht@steinbogen-betriebe.example>', '''Guten Tag Frau Morgenrot,

für unsere eigenen Geräte melden wir vorläufig 1.650.000 EUR netto an. Die Aufstellung finden Sie als Anlage. Eine abschließende Bewertung ist das noch nicht. Wir sind zum Vorsteuerabzug berechtigt und setzen hier keine Umsatzsteuer an.

Bitte schlagen Sie kurzfristig eine gemeinsame Besichtigung vor. Die Aufstellung enthält nur Geräte, die hinter dem beschädigten Tor standen. Nicht jedes davon ist bereits einzeln technisch geprüft. Die Buchhaltung sucht Kaufrechnungen und Seriennummernlisten zusammen. An anderer Stelle eingelagerte Geräte sind in diesem Betrag nicht enthalten.

Ob wir einzelne Veranstaltungen mit Leihtechnik bedienen müssen, ist noch offen. Solche Zusatzkosten sind in der heutigen Forderung nicht enthalten. Bis zur Besichtigung bleiben die Geräte unverändert und gekennzeichnet stehen.

Beste Grüße
Juno Kühn'''),
E('09_Nachbarbetrieb.eml','Produktionsausfall Nuri Nudelwerk','2026-10-01T15:53:00+02:00','Nuri Şahin <nuri@nuri-nudelwerk.example>','Mira Morgenrot <recht@steinbogen-betriebe.example>', '''Sehr geehrte Frau Morgenrot,

unsere Nuri Nudelwerk GmbH nutzt den Nachbarraum im gleichen Hof. Wegen der vorsorglichen Stromabschaltung am 25. September konnten wir drei Großaufträge nicht rechtzeitig produzieren. Zusammen waren das 45.000 EUR Nettoumsatz. Wir bitten um Ersatz.

An unseren Maschinen, Vorräten und Räumen ist nach unserem bisherigen Stand nichts beschädigt. Die Kühlschränke blieben im zulässigen Temperaturbereich, es musste keine Ware entsorgt werden. Unsere Räume waren weiterhin zugänglich. Strom hatten wir ungefähr von 09:25 bis 18:40 Uhr nicht.

Zwei Kunden haben storniert, mit dem dritten reden wir über einen Ersatztermin. Die 45.000 EUR sind die Auftragssumme vor Abzug von Material und anderen ersparten Kosten. Belege und Stornierungsnachrichten kann ich nachreichen. Ich weiß, dass unser Fall anders aussieht als das eingedrückte Tor, aber der Ausfall trifft uns trotzdem hart.

Mit freundlichen Grüßen
Nuri Şahin, Geschäftsführer'''),
E('10_Vertragsunterlagen.eml','Fahrzeug 7: Vertragsbestand und Großschadenunterlagen','2026-10-02T10:33:00+02:00','Gundula Pfennig <schaden@frankenbogen-versicherung.example>','Leitung Schaden <schadenleitung@frankenbogen-versicherung.example>', '''Guten Morgen Frau Zobel,

unser Bestandssystem führt die Stadtbetriebe Steinbogen GmbH für Fahrzeug 7 als Versicherungsnehmerin einer Kfz-Haftpflichtversicherung mit Laufzeit 1. Januar bis 31. Dezember 2026. Der Schaden ist zur Bearbeitung angelegt. Die vollständige Police mit Bedingungen und Nachträgen ist jedoch noch aus dem Vertragsarchiv beizuziehen; den Vertragssatz habe ich heute angefordert. Ein Datenbankeintrag ersetzt für unsere Deckungsprüfung nicht den genauen Vertragsinhalt.

Wegen der angemeldeten Geräteforderung habe ich den Vorgang an unsere Großschadenstelle gegeben. Welches Rückdeckungsprogramm für diesen Vertrag und diesen Schaden gelten könnte, ist in den vorliegenden Unterlagen nicht belegt. Die Vertragsverwaltung soll den tatsächlich einschlägigen Vertrag, Nachträge, Meldevoraussetzungen und Ansprechpartner benennen. Eine Beteiligung am AKHA oder eine Leistung daraus ist hiermit nicht bestätigt.

Deckungssummen, Selbstbehalte, Zusammenrechnung von Ansprüchen und Rückdeckungsgrenzen lassen sich aus dieser Akte noch nicht ablesen. Haftungsbewertung, eigene Deckungsprüfung und eine etwaige Rückdeckungsanfrage sind daher getrennt vorzubereiten. Bitte keine Quote oder Zuständigkeit allein aus der Anmeldungshöhe ableiten.

Eine Deckungszusage oder Haftungsanerkennung ist bisher nicht erteilt. Die Höhe der Geräteforderung habe ich allein als vorläufige Anmeldung in die Übersicht übernommen.

Gundula'''),
D('11_Fuhrparkchat.txt','Fahrzeug 7 – Dispositionschat','25.09.2026','', '''09:15 Burkhard: Maschine ist gegen das Tor gerollt. Bin ausgestiegen wegen der Bake. Bitte Unterstützung.
09:16 Hedwig: Verletzte? Motor aus, Fahrzeug sichern, Abstand halten.
09:18 Burkhard: Soweit ich sehe niemand verletzt. Motor ist aus. Tor und Kisten beschädigt.
09:24 Hedwig: Elektriker kommt, bitte nichts an Geräten bewegen.
09:31 Burkhard: Ich dachte Bremse war drin. Bin gerade nicht sicher, ob der Hebel ganz eingerastet war.
10:12 Farid: Abschleppen nach Befundfotos. Werkstattplatz ist frei.
18:44 Hedwig: Strom im Hof wieder da. Maschine bleibt gesperrt. Technikbericht folgt erst nach Untersuchung.

Exportiert am 28.09.2026 durch Hedwig Hummel. Befundfotos befinden sich noch auf dem Werkstattgerät und sind diesem Export nicht beigefügt.'''),
]),
]
