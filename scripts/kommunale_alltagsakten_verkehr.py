"""Vier kommunale Alltagsakten aus dem Raum Würzburg, ohne Lösungstexte."""


def D(file, title, day, sender, body):
    return dict(file=file, title=title, date=day, sender=sender, body=body.strip())


def E(file, title, day, sender, recipient, body):
    return dict(file=file, title=title, date=day, **{'from': sender, 'to': recipient}, body=body.strip())


CASES = [
dict(
slug='akha-wuerzburg-fahrzeugschaden',
title='Würzburg: Der Transporter am Quittenbogen',
summary='Eine Fahrt zur Sicherung einer Fahrbahnabsenkung endet am geparkten Privatwagen. Reparaturrechnung, Fahrerbericht und eine unabhängige Zeugin liegen vor.',
core=['01_Pruefauftrag.eml', '02_Fahrerbericht.docx', '03_Fahrzeug_und_Einsatz.docx', '04_Zeugin.eml', '05_Reparaturrechnung.docx', '07_Forderung.eml'],
xlsx=[],
attachments={'07_Forderung.eml': ['05_Reparaturrechnung.docx', '06_Taxibelege.docx']},
documents=[
E('01_Pruefauftrag.eml', 'Quittenbogen: Prüfvermerk und Antwort an Herrn Dinkel', '2026-10-05T08:15:00+02:00', 'Kunigunde Färber <recht@lindenquell.example>', 'Rechtsanwältin Samira Seidel <samira@seidel-kanzlei.example>', '''Sehr geehrte Frau Seidel,

wir beauftragen Sie für die Stadt Lindenquell bei Würzburg mit einem internen Prüfvermerk und einem vollständig ausformulierten Antwortentwurf an Herrn Tassilo Dinkel. Unser Transporter berührte am 8. September dessen abgestellten Wagen. Herr Dinkel verlangt 2.213,80 EUR und bittet um Antwort bis zum 12. Oktober. Wir benötigen Ihre Unterlagen bis zum 8. Oktober.

Der Wagen der Stadt war mit Absperrmaterial auf dem Weg zu einer gemeldeten Fahrbahnabsenkung. Im Fahrtenbuch steht „Amtsfahrt“. Bitte prüfen Sie die Bedeutung des tatsächlichen Einsatzes für die Ansprüche gegen die Stadt und unseren Fahrer; die Bezeichnung im Fahrtenbuch soll keine rechtliche Einordnung vorwegnehmen. Die Stadt ist Halterin und Eigentümerin des Transporters. Sie vertreten ausschließlich uns, nicht Herrn Dinkel oder Herrn Quast persönlich.

Bitte trennen Sie belegte Reparaturkosten, Mobilitätskosten und die zusätzlich verlangte Pauschale. Benennen Sie höchstens die entscheidenden noch benötigten Angaben. Versicherung und eine mögliche kommunale Ausgleichslösung sind gesondert zu klären; die Akte enthält keine Deckungszusage. Anerkenntnis und Zahlung wurden nicht erklärt. Der Antwortentwurf bleibt intern, ein Versand ist nicht beauftragt.

Mit freundlichen Grüßen
Kunigunde Färber, Rechtsstelle'''),
D('02_Fahrerbericht.docx', 'Fahrerbericht vom Quittenbogen', '08.09.2026', 'Stadt Lindenquell · Straßenunterhalt · Veit Quast', '''## 1 Fahrt und Kontakt

Am 8. September 2026 fuhr ich gegen 09:12 Uhr mit dem städtischen Transporter, Fuhrparknummer 17, in den Quittenbogen. Im Laderaum lagen sechs Absperrbaken und zwei Warnleuchten. Am Ende der Straße sollte ich die gemeldete Fahrbahnabsenkung sichern. Neben Haus 12 stand rechts ein blauer Privatwagen in einer markierten Parkbucht.

Ein Lieferwagen kam mir entgegen. Ich hielt zunächst an und rollte dann langsam vorwärts, als der Lieferwagen an mir vorbeigefahren war. Dabei hörte ich rechts ein Schaben. Meine rechte hintere Fahrzeugecke hatte die linke hintere Tür des blauen Wagens berührt. Einen Defekt an Lenkung oder Bremse bemerkte ich nicht. Auf dem Beifahrersitz saß niemand; es gab keinen Einweiser.

## 2 Maßnahmen

Ich hielt sofort an und klingelte bei den Häusern 10 und 12. Herr Dinkel kam aus Haus 12. Wir sahen eine frische längliche Schramme und eine Eindellung an seiner linken hinteren Tür. An unserem Transporter befanden sich blaue Lackspuren. Ich gab Herrn Dinkel Namen, Dienststelle und Fuhrparknummer. Eine Aussage zur Bezahlung habe ich nicht gemacht. Frau Amani, die am Küchenfenster von Haus 10 stand, sagte, sie habe den Kontakt gesehen.

Die Sicherung der Absenkung übernahm anschließend ein zweites Team. Ich meldete den Unfall um 09:21 Uhr telefonisch an die Disposition. Fotos nahm Herr Dinkel mit seinem Telefon auf; eine Kopie habe ich nicht erhalten.

Veit Quast'''),
D('03_Fahrzeug_und_Einsatz.docx', 'Fuhrparkauskunft und Einsatzauftrag 26-391', '09.09.2026', 'Stadt Lindenquell · Bauhof · Hildegard Knorz', '''## 1 Fahrzeug und Fahrer

Der Transporter mit der Fuhrparknummer 17 steht seit 2022 im Eigentum der Stadt Lindenquell. Die Stadt trägt Betriebskosten, Wartung und Einsatzplanung und ist in der Zulassungsbescheinigung als Halterin eingetragen. Zulässige Gesamtmasse: 3,5 Tonnen. Das Fahrzeug wird für den Straßenunterhalt eingesetzt. Veit Quast ist bei der Stadt als Bauhofmitarbeiter beschäftigt und war am 8. September von 07:00 bis 15:30 Uhr im Dienst.

## 2 Auftrag am 8. September

Um 08:47 Uhr meldete die Streckenkontrolle eine frische Absenkung neben einem Schacht im Quittenbogen vor Haus 26. Der Quittenbogen ist nach unserem Straßenverzeichnis eine gewidmete Ortsstraße in der Baulast der Stadt. Die Disposition wies Herrn Quast um 08:55 Uhr an, Baken und Warnleuchten aus dem Bauhof zu holen, direkt zur Stelle zu fahren und sie bis zum Eintreffen des Reparaturtrupps gegen Befahren zu sichern.

Die Fahrt diente keinem privaten Transport und keiner Vermietung. Der Unfallort vor Haus 12 liegt auf dem direkten Weg. Das Fahrtenbuch enthält für 09:00 Uhr den Eintrag „Amtsfahrt / Absperrung Quittenbogen“. Ein Auftrag, dort zu rangieren oder in der Parkbucht zu halten, bestand nicht. Die Absperrung wurde nach dem Unfall durch das Ersatzteam um 09:44 Uhr aufgebaut.

Hildegard Knorz, Disposition'''),
E('04_Zeugin.eml', 'Beobachtung am 8. September', '2026-09-11T18:24:00+02:00', 'Yasmin Amani <yasmin.amani@postfach.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

ich wohne im ersten Stock von Quittenbogen 10 und sah am Dienstagmorgen aus meinem Küchenfenster auf die Straße. Der blaue Wagen stand vollständig in seiner Parkbucht. Niemand saß darin. Ich kenne Herrn Dinkel nur vom Grüßen im Haus; verwandt oder geschäftlich verbunden sind wir nicht.

Der graue Transporter hielt wegen eines entgegenkommenden Lieferwagens kurz an. Als er weiterfuhr, bewegte sich seine hintere rechte Ecke sehr dicht am blauen Wagen entlang. Ich hörte ein Schaben und sah, dass der Fahrer sofort anhielt. Den genauen Abstand kann ich aus der oberen Etage nicht schätzen. Ob der Fahrer in den Spiegel sah, war für mich nicht erkennbar.

Ich blieb am Fenster, bis Herr Dinkel herauskam. Vor dem Kontakt war niemand am blauen Wagen beschäftigt. Ob dieser schon kleinere Kratzer hatte, weiß ich nicht; die frische längliche Stelle an der Tür war danach aus meinem Fenster zu sehen. Eine Videoaufnahme habe ich nicht. Für Rückfragen bin ich abends erreichbar.

Mit freundlichen Grüßen
Yasmin Amani'''),
D('05_Reparaturrechnung.docx', 'Rechnung KD-260916 mit Zahlungsbestätigung', '16.09.2026', 'Karosseriewerkstatt Korbinian Dorn · Spindelgasse 4, Lindenquell', '''Rechnung an Tassilo Dinkel, Quittenbogen 12, Lindenquell. Privatfahrzeug: blauer Kompaktwagen, Werkstattauftrag 26-184. Annahme am 15. September um 08:00 Uhr, Abholung am 16. September um 16:20 Uhr.

## 1 Ausgeführte Arbeiten

Die linke hintere Tür wurde nach dem seitlichen Streifkontakt instand gesetzt. Ausbeulen und Richten: 6 Stunden zu 95,00 EUR, zusammen 570,00 EUR netto. Vorbereitung und Lackierung der Tür: 6 Stunden zu 95,00 EUR, zusammen 570,00 EUR netto. Lackmaterial: 360,00 EUR netto. Ausbau und Einbau von Türgriff, Dichtung und Zierleiste: 200,00 EUR netto. Neue beschädigte Zierleiste: 100,00 EUR netto.

Nettosumme: 1.800,00 EUR. Umsatzsteuer 19 Prozent: 342,00 EUR. Rechnungsbetrag: 2.142,00 EUR. Der Betrag wurde am 16. September bei Abholung vollständig per Karte bezahlt.

## 2 Abgrenzung

Abgerechnet sind nur die Arbeiten an der linken hinteren Tür. Ein älterer kleiner Kratzer an der rechten vorderen Stoßstangenecke wurde bei Annahme vermerkt und nicht bearbeitet. Das Fahrzeug war vor Beginn der Reparatur fahrbereit. Eine Achsvermessung, eine Wertminderungsbewertung und eine Mietwagengestellung gehörten nicht zum Auftrag. Die Rechnung enthält keine Arbeiten auf Vorrat und keinen Kostenvoranschlag.

Korbinian Dorn'''),
D('06_Taxibelege.docx', 'Taxibelege und Erläuterung der Werkstattfahrten', '17.09.2026', 'Taxi Nadir Nuss · Lindenquell · Quittungen 5118 und 5146', '''## 1 Quittung 5118

Am 15. September 2026 wurde Herr Tassilo Dinkel um 08:12 Uhr an der Karosseriewerkstatt, Spindelgasse 4, abgeholt und zum Quittenbogen 12 gefahren. Fahrtentgelt einschließlich Umsatzsteuer: 23,40 EUR. Der Betrag wurde bar bezahlt; ein Trinkgeld ist darin nicht enthalten. Nadir Nuss hat die Beförderung und Zahlung auf dem ausgehändigten Beleg bestätigt.

## 2 Quittung 5146

Am 16. September 2026 wurde Herr Tassilo Dinkel um 15:48 Uhr am Quittenbogen 12 abgeholt und zur Werkstatt in der Spindelgasse 4 gefahren. Fahrtentgelt einschließlich Umsatzsteuer: 23,40 EUR. Der Betrag wurde bar bezahlt. Auch dieser Beleg umfasst ausschließlich das Beförderungsentgelt.

## 3 Ergänzung des Fahrgasts

Ich habe den Wagen selbst zur Reparatur gebracht und am Folgetag abgeholt. Für diese beiden Wege nutzte ich das Taxi. Einen Mietwagen hatte ich nicht; Nutzungsausfall fordere ich nicht zusätzlich. Meine Frau benötigte unseren zweiten Wagen an beiden Tagen für ihre Frühschicht außerhalb des Orts. Die Rechnungen betreffen keine Wege zur Arbeit und keine privaten Besorgungsfahrten. Die beiden Taxibeträge ergeben zusammen 46,80 EUR.

Tassilo Dinkel, ergänzt am 17. September 2026'''),
E('07_Forderung.eml', 'Reparatur bezahlt – meine Forderung', '2026-09-24T17:42:00+02:00', 'Tassilo Dinkel <tassilo.dinkel@postfach.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

mein Wagen ist wieder repariert. Anbei schicke ich die Reparaturrechnung über 2.142,00 EUR und die beiden Taxibelege mit meiner Erläuterung über zusammen 46,80 EUR. Zusätzlich verlange ich 25,00 EUR für Telefonate, Kopien und die Abwicklung. Damit ergibt sich ein Gesamtbetrag von 2.213,80 EUR. Einzelne Telefon- und Kopierkosten habe ich bisher nicht zusammengestellt.

Das Auto gehört mir privat. Ich bin Rentner und betreibe kein Unternehmen; die auf der Werkstattrechnung ausgewiesene Umsatzsteuer kann ich nicht als Vorsteuer abziehen. Meine Kaskoversicherung habe ich nicht in Anspruch genommen. Von anderer Seite habe ich für diesen Schaden nichts erhalten. Einen zusätzlichen Mietwagen oder Nutzungsausfall verlange ich nicht.

Ihr Fahrer hat mir den Ablauf vor Ort geschildert. Von einer Zusage der Stadt gehe ich trotzdem erst aus, wenn ich etwas Schriftliches bekomme. Bitte geben Sie mir bis zum 12. Oktober Nachricht. Die Fotos auf meinem alten Telefon muss mein Enkel noch übertragen; er kommt am nächsten Wochenende. Wenn Sie eine bestimmte Ansicht brauchen, schreiben Sie mir das bitte.

Mit freundlichen Grüßen
Tassilo Dinkel'''),
E('08_Fuhrpark_Deckungsunterlagen.eml', 'Fuhrpark 17: Vertragsunterlagen noch nicht vollständig', '2026-09-30T10:12:00+02:00', 'Roswitha Kren <risiken@lindenquell.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Liebe Frau Färber,

für den Transporter 17 enthält die Fuhrparkablage eine Beitragsbuchung für 2026 mit dem Text „Kfz-Haftpflicht Sammelbestand“. Die Buchung ist kein vollständiger Versicherungsschein. Die aktuelle Fahrzeugliste, die Bedingungen und der vereinbarte Meldeweg fehlen mir noch. Ich habe sie heute beim Vertragsarchiv angefordert. Eine Schaden- oder Deckungsentscheidung liegt hier nicht vor.

Daneben findet sich in einer alten Ordnerstruktur die Rubrik „kommunaler Ausgleich / Rückdeckung“. Dort liegt für diesen Schaden kein Vertrag und keine Mitgliedsbestätigung. Ich kann daraus weder eine Zugehörigkeit zu einer Ausgleichseinrichtung noch eine Zuständigkeit für den Fahrzeugschaden bestätigen. Eine Weiterleitung an eine solche Stelle habe ich deshalb noch nicht vorgenommen.

Bitte geben Sie mir nach Ihrer Prüfung den sachlichen Unfallhergang und die aufgeschlüsselten Beträge. Den Fahrerbericht und die konkrete Einsatzzuordnung habe ich bereits gesichert. Haftungsbewertung und Vertragsprüfung sollen in unserer Antwort an Herrn Dinkel nicht ineinanderlaufen. Bisher wurde weder eine Regulierung zugesagt noch eine Zahlung ausgelöst.

Viele Grüße
Roswitha Kren'''),
E('09_Werkstatt_Rueckfrage.eml', 'Zur Türreparatur und den Bildern', '2026-10-01T13:06:00+02:00', 'Korbinian Dorn <werkstatt@dorn-karosserie.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

Herr Dinkel hat mich ermächtigt, die Angaben auf unserer Rechnung zu erläutern. Bei Annahme sahen wir eine frische Eindellung mit horizontalem Lackabrieb an der linken hinteren Tür. Das Schadensbild passte zu dem von ihm beschriebenen seitlichen Kontakt. Eine technische Unfallrekonstruktion haben wir nicht vorgenommen.

Die Tür ließ sich fachgerecht richten; ein Austausch war nicht erforderlich. Die Lackierung war auf die Tür begrenzt. Den älteren Kratzer vorne rechts haben wir im Annahmeblatt ausdrücklich ausgenommen. Unser Rechnungsbetrag ist vollständig bezahlt. Weitere Rechnungen oder Nachträge zu diesem Auftrag gibt es nicht.

Ich habe vor Arbeitsbeginn zwei Werkstattfotos aufgenommen. Unser Servicebüro kann diese auf Ihre konkrete Anfrage herausgeben. Zu der Position von 25,00 EUR in Herrn Dinkels Schreiben kann ich nichts sagen; sie stammt nicht von uns. Das Fahrzeug blieb über Nacht wegen der Trocknungszeit in der Halle. Es stand nach Abschluss der Arbeiten ab 15:30 Uhr am 16. September zur Abholung bereit.

Mit freundlichen Grüßen
Korbinian Dorn'''),
]),
dict(
slug='akha-wuerzburg-schwimmbad',
title='Würzburg: Die lose Stufe im Lindenbad',
summary='Eine Besucherin verletzt sich an einer bekannten lockeren Beckenstufe. Eintrittsvertrag, Kontrollbuch und eine ungenaue erste Meldung führen zur Betreiber-GmbH.',
core=['01_Pruefauftrag.eml', '02_Benutzungsordnung_und_Eintritt.docx', '03_Unfallmeldung.docx', '04_Kontrollbuch.docx', '05_Behandlungsbericht.docx', '07_Forderung.eml'],
xlsx=[],
attachments={'07_Forderung.eml': ['05_Behandlungsbericht.docx', '06_Auslagenbelege.docx']},
documents=[
E('01_Pruefauftrag.eml', 'Lindenbad: Unfall Frau Rebhuhn – interner Vermerk und Antwort', '2026-10-05T08:35:00+02:00', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', 'Rechtsanwältin Samira Seidel <samira@seidel-kanzlei.example>', '''Sehr geehrte Frau Seidel,

für die Lindenqueller Bäderbetrieb GmbH beauftrage ich Sie mit der Prüfung des Vorfalls vom 22. August im Lindenbad. Bitte erstellen Sie bis 8. Oktober einen internen Prüfvermerk und einen ausformulierten Antwortentwurf an Frau Walburga Rebhuhn. Sie verlangt 892,70 EUR und hat um Antwort bis zum 12. Oktober gebeten. Der Auftrag umfasst keinen Versand und kein Zahlungsanerkenntnis.

Die GmbH betreibt das Bad auf eigene Rechnung, beschäftigt das Aufsichtspersonal und hat Frau Rebhuhn die Tageskarte verkauft. Alle Geschäftsanteile hält die Stadt Lindenquell bei Würzburg. Unsere Benutzungsordnung und die Tageskartenabrechnung liegen bei; bitte behandeln Sie die Stadt und die Betreiberin nicht als austauschbare Anspruchsgegner. Sie vertreten in dieser Sache nur die GmbH.

Mich beschäftigt besonders der Unterschied zwischen der ersten Unfallmeldung und der späteren Schilderung zur Einstiegsstufe. Prüfen Sie bitte auch, was aus der bereits vor dem Unfall festgehaltenen Lockerung folgt. Ein aktueller Verlaufsbefund wurde noch nicht eingereicht. Halten Sie Haftung, Anspruchshöhe und die noch offene Versicherungsprüfung auseinander. Weder unsere Gesellschafterin noch wir haben eine Kostenübernahme zugesagt.

Mit freundlichen Grüßen
Fatima Fink, Geschäftsführerin'''),
D('02_Benutzungsordnung_und_Eintritt.docx', 'Betriebsunterlagen: Benutzungsordnung und Tageskarte', '28.09.2026', 'Lindenqueller Bäderbetrieb GmbH · Lindenbad · Seerosenbogen 3, Lindenquell', '''## 1 Betreiberin und Vertrag

Das Lindenbad wird von der Lindenqueller Bäderbetrieb GmbH betrieben. Die Stadt Lindenquell ist alleinige Gesellschafterin. Die GmbH übernimmt Kasse, Wasseraufsicht, laufende Wartung und Reparaturaufträge mit eigenem Personal und auf eigene Rechnung. Diese Angaben entsprechen der Betriebsregelung vom 2. Januar 2026, die von der Geschäftsführung und der Gesellschafterin unterzeichnet wurde.

Nach der seit 1. Mai 2026 an der Kasse ausgehängten Benutzungsordnung schließen Gäste mit dem Kauf einer Eintrittskarte einen privatrechtlichen Vertrag mit der GmbH. Der Tagespreis wird von der GmbH erhoben und vereinnahmt. Ein städtischer Gebührenbescheid wird nicht erstellt. Erwachsene zahlen für den Tagesbesuch 6,50 EUR einschließlich Umsatzsteuer.

## 2 Verhalten und Meldungen

Die Beckenumgänge sind langsam zu begehen. Gäste sollen sichtbare Schäden und lockere Einbauten unmittelbar der Aufsicht melden. Gesperrte Zugänge dürfen nicht benutzt werden. Für das Sportbecken stehen eine breite Treppe und zwei seitliche Edelstahlleitern zur Verfügung. Eine bestimmte Zugangsart wird erwachsenen Gästen nicht vorgeschrieben.

## 3 Eintritt am Unfalltag

Kassenbon LB-260822-074 bestätigt den Verkauf einer Erwachsenen-Tageskarte am 22. August 2026 um 10:06 Uhr für 6,50 EUR, bezahlt per Karte. Frau Rebhuhn legte diesen Bon bei ihrer späteren Vorsprache vor. An der Kasse wurde kein Sondertarif vereinbart. Die vorstehende Abschrift wurde am 28. September durch Kassiererin Edda Eichel mit dem Kassenjournal und der ausgehängten Ordnung abgeglichen.'''),
D('03_Unfallmeldung.docx', 'Unfallmeldung Lindenbad, Sportbecken', '22.08.2026', 'Lindenqueller Bäderbetrieb GmbH · Wasseraufsicht · Anselm Klee', '''## 1 Aufnahme um 10:42 Uhr

Frau Walburga Rebhuhn meldete sich um 10:42 Uhr mit einer blutenden Schürfwunde am rechten Schienbein bei der Aufsicht. Ich schrieb in das Kurzformular: „Am Beckenrand ausgerutscht; Bein an Metall angeschlagen.“ Das waren meine zusammenfassenden Worte nach einem kurzen Gespräch. Ich habe den Vorfall selbst nicht gesehen und ließ Frau Rebhuhn diesen Wortlaut nicht unterschreiben.

Sie zeigte auf die westliche Edelstahlleiter des Sportbeckens. Ich versorgte die Wunde zunächst mit einem sterilen Verband. Frau Rebhuhn sagte, sie sei mit dem rechten Fuß auf einer Stufe weggerutscht und habe sich dabei gestoßen. Sie war ansprechbar und konnte auftreten, wollte wegen der Schmerzen aber ärztlich abgeklärt werden. Ihre Bekannte organisierte die Heimfahrt.

## 2 Kontrolle des Zugangs

Um 10:48 Uhr drückte ich die zweite Stufe unterhalb des Beckenumgangs von Hand nach unten. Sie ließ sich auf einer Seite bewegen; eine Befestigungsmutter saß sichtbar locker. Ich sperrte die Leiter mit einer festen Kette und einem Hinweisschild. Der Zugang über die breite Treppe blieb möglich. Erst beim Nachlesen des Kontrollbuchs sah ich den Eintrag des Frühdienstes zur selben Stufe.

Ich habe kein Rennen und keinen Sprung der Besucherin beobachtet. Über Nässe am Beckenumgang lässt sich aus meinem Kurztext keine besondere Feststellung ableiten. Die Wundversorgung und die Sperrung sind meine eigenen Beobachtungen.

Anselm Klee'''),
D('04_Kontrollbuch.docx', 'Kontrollbuchauszug vom 22. August 2026', '22.08.2026', 'Lindenqueller Bäderbetrieb GmbH · Frühdienst · Marisol Sturm', '''## 1 Kontrolle vor Öffnung

07:35 Uhr: Wasserwerte und Sichtprüfung ohne Besonderheit. An der westlichen Leiter des Sportbeckens wackelt die zweite Stufe unter Belastung leicht. Die Mutter an der rechten Befestigung lässt sich mit dem Finger drehen. Ich melde dies um 07:41 Uhr an den diensthabenden technischen Mitarbeiter Severin Lerch. Er kündigt an, nach Abschluss der Arbeiten an der Filteranlage vorbeizukommen.

07:50 Uhr: Die Leiter ist noch nicht repariert. Ich habe einen roten Reparaturzettel an das Kontrollbrett im Personalraum gehängt. Am Becken selbst habe ich keine Kette und kein Schild angebracht. Bei der Dienstübergabe um 09:50 Uhr spreche ich die Filterstörung und die erwartete Technikrunde an. Ob ich die lose Stufe ausdrücklich erwähnt habe, kann ich später nicht mehr sicher sagen.

## 2 Eintrag nach dem Vorfall

10:48 Uhr, Anselm Klee: Nach Verletzung einer Besucherin Leiter geprüft; zweite Stufe rechts locker. Zugang mit Kette gesperrt. Technik erneut angerufen. Andere Zugänge frei.

11:20 Uhr, Severin Lerch: Befestigung ausgebaut. Sicherungsscheibe fehlt. Mutter und Sicherung erneuert, beide Seiten festgezogen und belastet. Stufe bewegt sich nicht mehr. Leiter um 11:35 Uhr nach gemeinsamer Kontrolle mit Anselm Klee freigegeben.

Die Uhrzeiten der ersten Meldung und des erneuten Anrufs wurden am selben Tag aus dem internen Telefondisplay übernommen. Die letzte vollständige schriftliche Leiterkontrolle vor diesem Tag ist am 20. August mit „fest“ eingetragen.'''),
D('05_Behandlungsbericht.docx', 'Ambulanter Bericht und Kontrolle', '01.09.2026', 'Praxis Dr. Mirela Sporn · Ringelgasse 8, Lindenquell', '''Patientin: Walburga Rebhuhn, geboren am 4. November 1964. Erstvorstellung am 22. August 2026 um 12:05 Uhr. Die Patientin berichtet, beim Einstieg in ein Schwimmbecken an einer beweglichen Stufe abgerutscht und mit dem rechten Schienbein an eine Metallkante gestoßen zu sein.

## 1 Erstbefund

Es zeigt sich eine etwa drei Zentimeter lange oberflächliche Riss- und Schürfwunde am rechten vorderen Unterschenkel mit örtlicher Prellung. Keine klaffende tiefe Wunde, keine Durchblutungs- oder Sensibilitätsstörung. Die Patientin kann unter leichten Schmerzen auftreten. Klinisch besteht kein Hinweis auf eine knöcherne Verletzung. Die Wunde wird gereinigt und mit einem Verband versorgt. Eine Naht ist nicht erforderlich. Der Tetanusschutz wurde überprüft und ist nach dem vorgelegten Impfpass ausreichend.

## 2 Kontrolle am 1. September

Die Wunde ist trocken und weitgehend geschlossen. Es bestehen noch Druckempfindlichkeit und eine leichte Verfärbung. Kein Anhalt für eine Infektion. Die Patientin schildert Schmerzen vor allem beim Knien und bei längeren Spaziergängen in der ersten Woche. Eine Arbeitsunfähigkeitsbescheinigung wurde nicht verlangt; die Patientin ist im Ruhestand.

Bei anhaltenden Beschwerden wird eine erneute Kontrolle empfohlen. Ob eine sichtbare Narbe verbleibt, lässt sich heute nicht abschließend beurteilen. Spätere Untersuchungen sind in diesem Bericht nicht enthalten.

Dr. Mirela Sporn'''),
D('06_Auslagenbelege.docx', 'Auslagen: Verbandmaterial und Taxifahrt', '24.08.2026', 'Walburga Rebhuhn · Sammlung der quittierten Auslagen', '''## 1 Verbandmaterial

Der Kassenbeleg der Ringel-Apotheke vom 22. August 2026, Beleg 822-119, nennt sterile Wundauflagen für 10,90 EUR und eine Packung Fixierbinden für 8,00 EUR. Gesamtpreis einschließlich Umsatzsteuer: 18,90 EUR. Zahlung per Karte. Die Ware wurde abgegeben; der Beleg ist kein Kostenvoranschlag. Frau Rebhuhn kaufte das Material nach der ärztlichen Versorgung für die empfohlenen Verbandwechsel zu Hause.

## 2 Heimfahrt

Die Quittung von Taxi Nadir Nuss, Nummer 4932, bestätigt die Fahrt am 22. August 2026 um 12:42 Uhr von der Praxis in der Ringelgasse 8 zur Wohnung von Frau Rebhuhn, Pflaumenstieg 6. Entgelt einschließlich Umsatzsteuer: 23,80 EUR, bar bezahlt. Die Fahrt vom Bad zur Praxis übernahm ihre Bekannte ohne Entgelt; dafür wird nichts berechnet.

## 3 Erklärung zu den Belegen

Die beiden ausgegebenen Beträge ergeben zusammen 42,70 EUR. Ich habe hierfür keine Erstattung erhalten und die Belege nicht bei einer privaten Zusatzversicherung eingereicht. Weitere Fahrtkosten, Behandlungskosten oder Hilfe im Haushalt rechne ich in meiner Forderung nicht ab. Die Eintrittskarte verlange ich ebenfalls nicht zurück. Die beiden Zahlungsbelege habe ich am 24. August zusammen mit dieser Erläuterung abgeheftet.

Walburga Rebhuhn'''),
E('07_Forderung.eml', 'Verletzung an Ihrer Einstiegsleiter – Belege', '2026-09-25T11:28:00+02:00', 'Walburga Rebhuhn <walburga.rebhuhn@postfach.example>', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', '''Sehr geehrte Frau Fink,

ich fordere von Ihrer Bäderbetrieb GmbH 850,00 EUR Schmerzensgeld und meine Auslagen von 42,70 EUR, insgesamt 892,70 EUR. Als Anlagen übersende ich den Bericht meiner Ärztin und meine Sammlung der quittierten Auslagen. Vor allem in der ersten Woche konnte ich nicht bequem knien und bin kaum spazieren gegangen. Jetzt sieht man noch eine gerötete Stelle. Ob das eine bleibende Narbe wird, weiß ich nicht.

In der ersten Meldung steht wohl „am Beckenrand ausgerutscht“. Das trifft den Ablauf nicht genau. Ich hielt beide Holme der westlichen Leiter fest, setzte den rechten Fuß auf die zweite Stufe und spürte, wie diese nachgab. Mein Bein stieß beim Abrutschen an die darunterliegende Metallkante. Ich bin weder gerannt noch vom Rand ins Wasser gesprungen.

Frau Nwosu war hinter mir und hat mich anschließend zur Praxis gefahren. Ich bitte Sie, ihr und dem Kontrollbuch nachzugehen. Einen neuen Arztbericht habe ich nicht; seit dem 1. September war ich nicht mehr dort. Bitte antworten Sie bis zum 12. Oktober. Eine Zahlung oder eine Einigung gab es bisher nicht.

Mit freundlichen Grüßen
Walburga Rebhuhn'''),
E('08_Zeugin_Nwosu.eml', 'Mein Standort an der Leiter', '2026-09-28T19:08:00+02:00', 'Chinwe Nwosu <chinwe.nwosu@postfach.example>', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', '''Sehr geehrte Frau Fink,

ich war am 22. August mit Frau Rebhuhn im Bad. Wir kennen uns aus der Nachbarschaft und gehen gelegentlich zusammen schwimmen. Ich stand etwa einen Meter hinter ihr auf dem Beckenumgang. Sie stieg rückwärts über die Leiter hinunter und hielt die beiden Holme. Plötzlich sackte sie etwas ab und rief auf. Ich sah ihre Füße in diesem Augenblick wegen ihres Körpers und des Wassers nicht vollständig.

Sie sagte direkt danach, dass die Stufe weggerutscht sei. Ich kann bestätigen, dass sie die Leiter benutzte und nicht einfach auf dem Beckenrand ausrutschte. Ob eine Mutter locker war oder wie stark sich die Stufe bewegte, habe ich selbst nicht geprüft. Vor dem Vorfall war an der Leiter keine Kette zu sehen. Ein Schild nahm ich dort ebenfalls nicht wahr.

Ich habe Frau Rebhuhn vom Bad zur Praxis gebracht und bin danach zur Arbeit gefahren. Beim Gespräch mit der Aufsicht stand ich daneben, habe aber nicht auf jedes Wort geachtet. Sie war aufgeregt und sprach zunächst nur von „abgerutscht“. Wenn die erste Meldung anders verstanden wurde, kann ich das nachvollziehen; einen Sprung vom Rand habe ich jedenfalls nicht gesehen.

Mit freundlichen Grüßen
Chinwe Nwosu'''),
E('09_Technik_Rueckmeldung.eml', 'Westliche Leiter: Reparatur und vorherige Meldung', '2026-09-29T09:14:00+02:00', 'Severin Lerch <technik@lindenbad.example>', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', '''Guten Morgen Frau Fink,

Marisol hat mich am Unfalltag vor Öffnung tatsächlich wegen der lockeren Stufe angerufen. Ich sagte, ich käme nach dem Filteralarm. Ich habe nicht gefragt, ob sie die Leiter solange sperrt, und ihr auch keine ausdrückliche Sperranweisung gegeben. Im Rückblick hatte jeder von uns wohl angenommen, der andere werde das Nötige veranlassen. Schriftlich festgehalten hatten wir das damals nicht.

Bei der Reparatur fand ich rechts eine lockere Mutter ohne Sicherungsscheibe. Die Stufe konnte sich dort unter Belastung absenken. Ich ersetzte die Befestigungsteile und prüfte beide Seiten. Einen Bruch der Stufe gab es nicht. Das ausgebaute Teil liegt noch im Technikschrank, beschriftet mit dem Datum und dem Leiterstandort.

Die letzte Wartung mit Demontage war im Juni durch unser eigenes Team erfolgt. Wer damals die rechte Befestigung montiert hat, ergibt sich aus dem Arbeitszettel nicht. Der Zettel bestätigt nur den Abschluss der Wartung. Eine externe Firma war an dieser Leiter im Sommer nicht tätig. Weitere Schäden oder Unfälle an derselben Stufe sind mir nicht bekannt.

Viele Grüße
Severin Lerch'''),
E('10_Vertragsstand.eml', 'Versicherung der Bäderbetrieb GmbH', '2026-10-02T10:37:00+02:00', 'Roswitha Kren <verwaltung@lindenbad.example>', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', '''Liebe Frau Fink,

unsere Buchhaltung führt eine eigene Betriebshaftpflichtposition für die GmbH. Der letzte vollständige Vertragsordner ist bei der ausgelagerten Altregistratur. Hier liegen lediglich Zahlungsnachweise und eine Korrespondenz zu einem anderen Schaden aus 2024. Damit kann ich den aktuellen Umfang, mögliche Selbstbehalte und Meldepflichten für den Vorfall vom 22. August noch nicht belastbar feststellen.

Die städtische Beteiligungsverwaltung hat mir heute bestätigt, dass sie keine Erklärung zur Mitversicherung der GmbH abgeben kann. Die hundertprozentige Beteiligung allein ist in unseren vorhandenen Unterlagen kein Nachweis eines bestimmten Versicherungsschutzes. Auch zu einer kommunalen Ausgleichseinrichtung liegt uns kein Aufnahme- oder Deckungsbeleg vor.

Die aktuellen Unterlagen sind angefordert. Frau Rebhuhns Behandlungsbericht befindet sich bis dahin nur in der beschränkten Schadenakte; ich habe ihn nicht an einen externen Empfänger übermittelt. Bitte lassen Sie mich wissen, welche Unterlagen für eine vorbereitete Schadenmeldung benötigt werden. Eine solche Meldung und eine Deckungsentscheidung sind im vorliegenden Vorgang bisher nicht dokumentiert.

Viele Grüße
Roswitha Kren'''),
]),
dict(
slug='akha-wuerzburg-baumpflege',
title='Würzburg: Ein Ast über dem Kerbelring',
summary='Beim angeordneten Rückschnitt eines Straßenbaums trifft ein Ast ein geparktes Auto. Arbeitsauftrag und Aussagen zeigen verteilte Zuständigkeiten für Schnitt und Sperrung.',
core=['01_Pruefauftrag.eml', '02_Arbeitsauftrag.docx', '03_Absperrvermerk.docx', '04_Ereignisbericht.docx', '05_Zeugin.eml', '08_Forderung.eml'],
xlsx=[],
attachments={'08_Forderung.eml': ['06_Reparaturrechnung.docx', '07_Mietwagenrechnung.docx']},
documents=[
E('01_Pruefauftrag.eml', 'Kerbelring: Astschaden – Zuständigkeiten und Antwortentwurf', '2026-10-05T09:00:00+02:00', 'Kunigunde Färber <recht@lindenquell.example>', 'Rechtsanwältin Samira Seidel <samira@seidel-kanzlei.example>', '''Sehr geehrte Frau Seidel,

bitte prüfen Sie für die Stadt Lindenquell bei Würzburg den Fahrzeugschaden vom 3. September am Kerbelring. Herr Leander Sesam verlangt von der Stadt 3.011,40 EUR. Beauftragt sind ein interner Prüfvermerk und ein vollständig ausformulierter Antwortentwurf bis zum 8. Oktober. Herr Sesam bittet um Rückmeldung bis 13. Oktober. Es ist kein Versand beauftragt.

Der Baum gehört zum Straßenbestand der Stadt. Den konkreten Rückschnitt ordnete unsere Baumkontrolle zur Sicherung des Straßenraums an. Die praktische Ausführung übernahm das Fachunternehmen Astwerk Amal Berg GmbH. Unser Einsatzleiter war vor Ort; seine Aufgaben und die des Unternehmens stehen im Arbeitsauftrag. Bitte klären Sie anhand dieser tatsächlichen Einbindung, welche Ansprüche und Verantwortlichkeiten in Betracht kommen. Die bloße Bezeichnung als Auftragnehmer soll die Prüfung nicht ersetzen.

Sie vertreten ausschließlich die Stadt. Das Unternehmen ist nicht mitmandatiert. Wir benötigen getrennte Aussagen zur Forderung des Bürgers und zu möglichen internen Rückgriffsfragen. Beim Absperrablauf weichen die Angaben voneinander ab. Vollständige Haftpflichtunterlagen der Stadt und des Unternehmens liegen nicht vor. Bisher gibt es weder ein Anerkenntnis noch eine Zahlung oder eine Deckungsentscheidung.

Mit freundlichen Grüßen
Kunigunde Färber'''),
D('02_Arbeitsauftrag.docx', 'Arbeitsauftrag 26-B47: Straßenbaum Kerbelring', '01.09.2026', 'Stadt Lindenquell · Straßenunterhalt · Baumkontrolle Ottokar Zwirn', '''## 1 Anlass und Leistungsbereich

Der Ahorn mit der Bestandsnummer KR-18 steht auf städtischem Straßengrund vor Kerbelring 18. Der Kerbelring ist eine gewidmete Ortsstraße in städtischer Baulast. Bei der Kontrolle am 31. August wurde an einem über Fahrbahn und Parkbucht ragenden Starkast eine frische Längsspaltung festgestellt. Der Ast ist am 3. September vor Freigabe des Arbeitsbereichs abschnittsweise zu entlasten und bis zum markierten Ansatz zurückzunehmen.

## 2 Aufgabenverteilung

Die Astwerk Amal Berg GmbH stellt zwei qualifizierte Beschäftigte, Hubarbeitsbühne, Schnittwerkzeug und Sicherungsseile. Sie bestimmt die geeignete Schnitt- und Seiltechnik sowie die sichere Bedienung ihrer Geräte. Ein freies Pflegeprogramm oder die Auswahl weiterer Bäume ist nicht beauftragt. Die markierten Schnitte werden gemeinsam mit dem städtischen Einsatzleiter Ottokar Zwirn vor Beginn durchgesprochen; Abweichungen bedürfen seiner Rücksprache.

Die Stadt stellt die mobile Straßensperrung, veranlasst die Freihaltung der betroffenen Parkbuchten und kontrolliert den geräumten Bereich. Der Einsatzleiter gibt die einzelnen Arbeitsabschnitte vor Ort frei. Das Unternehmen beginnt den Schnitt erst nach dieser Freigabe und unterbricht die Arbeit, wenn Personen oder Fahrzeuge im möglichen Fallbereich verbleiben.

## 3 Abwicklung

Arbeitsbeginn ist für 3. September um 08:00 Uhr vereinbart. Das Unternehmen rechnet den vereinbarten Einsatz nach Aufwand ab. Der städtische Einsatzleiter dokumentiert Freigaben und besondere Vorkommnisse auf dem Tagesblatt. Auftrag angenommen am 1. September durch Amal Berg; Ausfertigung freigegeben durch Ottokar Zwirn.'''),
D('03_Absperrvermerk.docx', 'Vermerk zum Arbeitsbereich vor Kerbelring 18', '04.09.2026', 'Stadt Lindenquell · Einsatzleitung · Ottokar Zwirn', '''## 1 Einrichtung am Morgen

Ich war am 3. September ab 07:40 Uhr vor Ort. Die mobile Halteverbotsbeschilderung sollte nach meiner Bestellung seit dem 31. August vor den drei betroffenen Parkbuchten stehen. Den Aufstellnachweis mit Uhrzeit und Fotos habe ich in meiner Mappe bislang nicht gefunden. Bei meiner Ankunft standen die Schilder am Anfang und Ende des Abschnitts. Ein schwarzer Privatwagen befand sich noch in der mittleren Parkbucht vor Haus 18.

Um 07:55 Uhr stellte unser Bauhof die Fahrbahnbaken. Ich bat einen Kollegen, in Haus 18 nach dem Fahrzeughalter zu fragen. Für den südlichen Kronenteil gab ich um 08:10 Uhr den Beginn frei, weil dessen Fallbereich nach unserer Besprechung neben der freien Fahrbahn liegen sollte. Den über der mittleren Parkbucht liegenden Ast wollte ich erst nach Entfernung des Wagens freigeben.

## 2 Offener Ablauf

Gegen 08:20 Uhr telefonierte ich einige Meter entfernt mit der Disposition wegen eines Abschleppfahrzeugs. Als ich zurücksah, fiel ein Aststück auf das abgestellte Auto. Ich habe den auslösenden Schnitt nicht gesehen. Einen ausdrücklichen Zuruf zur Freigabe des Asts über dem Wagen habe ich nach meiner Erinnerung nicht gegeben.

Das Tagesblatt enthält nur „08:10 Beginn“. Eine eindeutige Zeichnung des zuerst freigegebenen Teilbereichs und eine Gegenzeichnung des Unternehmens fehlen. Das Blatt habe ich nach dem Vorfall unverändert zur Schadenakte gegeben. Der Halter kam wenig später aus Haus 18. Eine Abschleppmaßnahme wurde nicht mehr durchgeführt.

Ottokar Zwirn'''),
D('04_Ereignisbericht.docx', 'Bericht des Unternehmens zum Astkontakt', '04.09.2026', 'Astwerk Amal Berg GmbH · Vorarbeiter Ravi König', '''## 1 Besprechung und Schnitt

Am 3. September trafen wir um 07:45 Uhr am Kerbelring ein. Herr Zwirn zeigte mir die Markierungen und besprach die Reihenfolge. Für mich bedeutete sein Zuruf „Sie können anfangen“ um etwa 08:10 Uhr, dass wir die Entlastung des markierten Astbereichs beginnen konnten. Dass der schwarze Wagen noch stand, war mir bekannt. Ich ging davon aus, dass die kleinen Teilstücke mit dem Seil sicher in die freie Fahrbahn geführt würden.

Den ersten größeren Abschnitt schnitt meine Kollegin von der Bühne aus. Ich führte das Sicherungsseil vom Boden. Nach dem Schnitt drehte sich das Stück stärker als erwartet zur Parkbucht. Das Seil lief unter Spannung über eine Astgabel und ließ sich nicht rechtzeitig nachführen. Die Spitze traf das Dach des schwarzen Wagens und rutschte über die hintere Scheibe. Es war nach meiner Uhr ungefähr 08:23 Uhr.

## 2 Reaktion und Unterlagen

Wir stoppten sofort und legten das restliche Holz kontrolliert ab. Am Dach war eine Delle sichtbar, die hintere Scheibe war gerissen. Herr Zwirn kam zurück. Der Wagen wurde abgedeckt. Niemand wurde verletzt. Werkzeug und Bühne hatten keinen Kontakt mit dem Auto; getroffen hat es das abgesägte Aststück.

Ich habe keine eigene schriftliche Freigabe erhalten. Unser Team war für Seilführung und Schnitttechnik zuständig. Eine Räumung oder Abschleppung des Privatwagens hatten wir nicht beauftragt. Die konkrete Verständigung über den Bereich vor dem ersten Schnitt sollte bitte mit Herrn Zwirn besprochen werden; eine Audio- oder Videoaufzeichnung gibt es nicht.

Ravi König'''),
E('05_Zeugin.eml', 'Was ich vom Kiosk aus gesehen habe', '2026-09-10T14:32:00+02:00', 'Fadime Lenz <fadime.lenz@postfach.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

ich öffnete am 3. September meinen Kiosk auf der gegenüberliegenden Seite des Kerbelrings kurz vor acht Uhr. Das schwarze Auto stand da bereits. Zwei Mitarbeiter stellten Baken auf. Zwischen dem Auto und dem Baum lag kein durchgehendes Absperrband; die Fahrbahn war in diesem Abschnitt für den normalen Verkehr gesperrt. Wann die Halteverbotsschilder aufgestellt wurden, weiß ich nicht.

Ich sah später einen Mann mit orangefarbener Stadtjacke am Telefon etwas abseits stehen. Von der Bühne wurde am Baum gearbeitet. Ein Aststück schwang zur Seite und traf den Wagen. Das Seil war für mich erkennbar, aber ich kann nicht beurteilen, ob es richtig geführt wurde. Vom Inhalt der Besprechung zwischen dem Mann und der Baumfirma habe ich nichts gehört.

Herr Sesam kam nach dem Geräusch aus dem Haus und fragte, warum man ihn nicht früher geholt habe. Ich weiß nicht, ob vorher schon jemand bei ihm geklingelt hatte. Der Mann mit der Stadtjacke und die Baumleute sahen sich anschließend zusammen den Schaden an. Ich habe kein Schuldeingeständnis gehört. Meine Sicht auf das Auto war frei, die genaue Schnittstelle in der Krone konnte ich dagegen nicht sehen.

Mit freundlichen Grüßen
Fadime Lenz'''),
D('06_Reparaturrechnung.docx', 'Rechnung RH-260914 mit Zahlungseingang', '14.09.2026', 'Karosserie Hedwig Halm GmbH · Mispelgasse 7, Lindenquell', '''Rechnung an Leander Sesam, Kerbelring 18, Lindenquell. Reparatur des privaten Kombis nach Astkontakt vom 3. September. Annahme zur Instandsetzung am 10. September, Fertigstellung am 11. September 2026.

## 1 Leistungen

Dachhaut im hinteren Bereich ausgebeult und gerichtet: 800,00 EUR netto. Vorbereitungs- und Lackierarbeiten am beschädigten Dachbereich einschließlich Lackmaterial: 720,00 EUR netto. Hintere Scheibe geliefert: 460,00 EUR netto. Aus- und Einbau der Scheibe mit Klebesatz und Dichtmaterial: 380,00 EUR netto. Innenraum von Splittern gereinigt und Abschlusskontrolle durchgeführt: 100,00 EUR netto.

Nettobetrag: 2.460,00 EUR. Umsatzsteuer 19 Prozent: 467,40 EUR. Gesamtbetrag: 2.927,40 EUR. Zahlungseingang am 16. September: 2.927,40 EUR, ohne Abzug.

## 2 Umfang und Standzeiten

Die Positionen betreffen die beim Astkontakt eingedrückte Dachstelle und die dadurch gerissene hintere Scheibe. Einen gesonderten Vorschaden in diesen Bereichen vermerkte die Annahme nicht. Eine Bewertung des allgemeinen Fahrzeugzustands oder einer merkantilen Wertminderung wurde nicht beauftragt. Vor dem Werkstatttermin stand das Fahrzeug mit abgedeckter Hecköffnung in der privaten Garage. Es wurde ab dem Schaden bis zur Reparatur nicht im Straßenverkehr benutzt. Die Werkstatt konnte erst nach Eingang der Scheibe mit der Instandsetzung beginnen.

Hedwig Halm'''),
D('07_Mietwagenrechnung.docx', 'Rechnung MW-260911 mit Erläuterung des Mieters', '17.09.2026', 'Mobilität Noura Nessel · Gewerberingel 2, Lindenquell', '''Rechnung vom 11. September 2026 an Leander Sesam, Kerbelring 18, Lindenquell. Mietvertrag 26-299 über einen Kleinwagen für den 10. und 11. September 2026. Übernahme am 10. September um 07:30 Uhr, Rückgabe am 11. September um 18:10 Uhr.

## 1 Entgelt und Nutzung

Vereinbarter Endpreis: 42,00 EUR je Miettag einschließlich Umsatzsteuer und vereinbarter Haftungsbegrenzung. Zwei Tage ergeben 84,00 EUR. Enthaltene Umsatzsteuer 19 Prozent: 13,41 EUR; Nettobetrag: 70,59 EUR. Der Rechnungsbetrag wurde bei Rückgabe vollständig per Karte bezahlt. Es fielen keine Zustell-, Reinigungs- oder Mehrkilometerkosten an.

Der Kilometerzähler stand bei Übergabe auf 18.220 und bei Rückgabe auf 18.304 Kilometern. Die gefahrene Strecke beträgt 84 Kilometer. Das Fahrzeug wurde vollgetankt zurückgegeben. Eigene Kraftstoffkosten sind nicht Bestandteil dieser Rechnung.

## 2 Ergänzung des Mieters

Ich benötigte den Ersatzwagen an beiden Tagen für meine Arbeit im Nachbarort. Vom 3. bis 9. September konnte ich Fahrgemeinschaften nutzen und verlange dafür nichts. Einen zweiten eigenen Wagen habe ich nicht. Nutzungsausfall wird neben dieser Rechnung nicht geltend gemacht. Der Mietwagen war kleiner als mein beschädigter Kombi. Die Gesamtsumme von 84,00 EUR entspricht dem abgebuchten Betrag.

Leander Sesam, ergänzt am 17. September 2026'''),
E('08_Forderung.eml', 'Astschaden am Kerbelring: Rechnungen', '2026-09-22T18:51:00+02:00', 'Leander Sesam <leander.sesam@postfach.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

ich fordere von der Stadt 2.927,40 EUR Reparaturkosten und 84,00 EUR Mietwagenkosten, zusammen 3.011,40 EUR. Die beiden bezahlten Rechnungen sind dieser Nachricht beigefügt. Das Fahrzeug gehört mir privat, ich bin angestellter Buchhändler und kann keine Vorsteuer abziehen. Eine Zahlung meiner Kaskoversicherung oder der Baumfirma habe ich nicht erhalten.

Ich parkte am Abend des 2. September gegen 21:30 Uhr vor unserem Haus. Ein Halteverbotsschild fiel mir dabei nicht auf. Am Morgen arbeitete ich zunächst zu Hause. Geklingelt hat bei mir nach meiner Erinnerung niemand, bevor der Ast auf das Dach fiel. Ob jemand an einer anderen Wohnung klingelte, kann ich nicht sagen. Ich habe deshalb Zweifel an der Behauptung, ich hätte das Auto trotz einer erkennbaren Sperrung dort stehen lassen.

Die Baumfirma sagte mir lediglich, sie arbeite im Auftrag der Stadt. Ich möchte nicht selbst zwischen verschiedenen Stellen vermitteln müssen. Bitte antworten Sie mir bis zum 13. Oktober. Das beschädigte Fahrzeug ist repariert; die Werkstatt hat die Annahmefotos gespeichert. Ich verlange weder einen zusätzlichen Nutzungsausfall noch einen pauschalen Wertverlust.

Mit freundlichen Grüßen
Leander Sesam'''),
E('09_Unternehmen_Stellungnahme.eml', 'Kerbelring: Auftrag und weiterer Schriftwechsel', '2026-09-29T08:46:00+02:00', 'Amal Berg <geschaeftsfuehrung@astwerk.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

wir bestätigen, dass unser Team den Auftrag 26-B47 ausführte. Die Stadt hatte Baum, zu entfernenden Ast und Arbeitstag bestimmt. Ihr Einsatzleiter war für die Räumung und die Freigabe der Teilbereiche vor Ort. Unser Unternehmen wählte die technischen Schnitt- und Seilverfahren selbst und setzte eigene Beschäftigte sowie eigene Geräte ein. Es handelte sich nicht um einen allgemeinen Pflegevertrag, bei dem wir selbstständig eine Baumreihe kontrollieren und Arbeiten auswählen.

Wir haben Herrn Sesam keine Übernahme seiner Forderung zugesagt. Unser Vorarbeiter hat den tatsächlichen Ablauf bereits schriftlich festgehalten. Die unterschiedliche Erinnerung an die Freigabe muss geklärt werden. Wir bitten um das städtische Tagesblatt und insbesondere um die Dokumentation, wann welche Parkbuchten geräumt oder freigegeben waren.

Den Vorgang haben wir intern an die für unsere Betriebshaftpflicht zuständige Verwaltung gegeben. Eine Deckungszusage liegt uns nicht vor. Eine Versicherungsbestätigung mit Bedingungen oder einer Entscheidung zu diesem Schaden kann ich heute deshalb nicht übersenden. Bitte stimmen Sie weitere Korrespondenz direkt mit mir ab; das Unternehmen wird in dieser Sache nicht durch Ihre anwaltliche Vertretung vertreten.

Mit freundlichen Grüßen
Amal Berg'''),
E('10_Risiko_und_Unterlagen.eml', 'Kerbelring: fehlender Aufstellnachweis und Vertragsstand', '2026-10-02T12:16:00+02:00', 'Roswitha Kren <risiken@lindenquell.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Liebe Frau Färber,

zum Halteverbot habe ich die Bestellung der Schilder im Bauhofsystem gefunden. Sie wurde am 28. August ausgelöst und nennt den 31. August als Aufstelltag. Eine Bestellung belegt aber noch nicht den tatsächlichen Aufbau. Das unterschriebene Aufstellblatt und die dort vorgesehenen Fotos habe ich beim Außendienst angefordert. Die Schilder selbst und ihre Position am Unfallmorgen werden von Herrn Zwirn beschrieben.

Die Stadtakte enthält bislang keine aktuelle Haftpflichturkunde und keine Bedingungen zur Einbeziehung beauftragter Unternehmen. Auch die in der Altregistratur geführte Rubrik „Schadenausgleich“ belegt für sich weder eine Mitgliedschaft noch die Zuständigkeit einer bestimmten Einrichtung. Für eine Rückdeckung liegt überhaupt kein Vertragsdokument in diesem Vorgang. Das ist noch aufzuklären, bevor wir hierzu eine Aussage treffen.

Die Rechnungen des Bürgers und die Berichte sind gesichert. Unsere Fragen zur Absperrung und zur gegenseitigen Verständigung betreffen den tatsächlichen Ablauf. Davon getrennt werde ich die Vertragsunterlagen zusammentragen. Eine Schadenmeldung nach außen oder eine Anerkennung gegenüber Herrn Sesam ist durch mich bisher nicht erfolgt.

Viele Grüße
Roswitha Kren'''),
]),
dict(
slug='akha-wuerzburg-schlagloch',
title='Würzburg: Die Felge am Hagebuttenweg',
summary='Ein Autofahrer verlangt Rad- und Abschleppkosten nach einem Schlagloch. Kontrolle, Bürgermeldung und Werkstattbefund lassen Zeitpunkt und Reifenschaden getrennt prüfen.',
core=['01_Pruefauftrag.eml', '02_Schadenmeldung.docx', '03_Strasse_und_Kontrollen.docx', '04_Meldung_und_Reparatur.docx', '05_Werkstattbefund.docx', '06_Reparaturrechnung.docx'],
xlsx=[],
attachments={'08_Forderung.eml': ['06_Reparaturrechnung.docx', '07_Abschlepprechnung.docx']},
documents=[
E('01_Pruefauftrag.eml', 'Hagebuttenweg: erste Prüfung und Antwort an Herrn Oliveira', '2026-10-05T09:25:00+02:00', 'Kunigunde Färber <recht@lindenquell.example>', 'Rechtsanwältin Samira Seidel <samira@seidel-kanzlei.example>', '''Sehr geehrte Frau Seidel,

für die Stadt Lindenquell bei Würzburg beauftragen wir Sie mit einem internen Prüfvermerk und einem ausformulierten Antwortentwurf zu Herrn Celestino Oliveiras Forderung von 920,00 EUR. Es geht um den Hagebuttenweg, eine Ortsstraße in unserer Straßenbaulast. Bitte legen Sie uns beides bis 8. Oktober vor; Herr Oliveira bittet um Antwort bis 14. Oktober. Versenden Sie den Entwurf nicht.

Die Beschädigung ereignete sich am 9. September gegen 06:50 Uhr. Eine ältere Bürgermeldung wurde am Tag davor im System erfasst, die genaue Lochmessung erfolgte erst am Folgetag des Unfalls. Bitte setzen Sie die nachträglichen Maße nicht ungeprüft mit dem Zustand zur Unfallzeit gleich. Wir benötigen eine nachvollziehbare Einordnung von Kontrolle, Kenntnis, möglicher Warnung und Erkennbarkeit für den Fahrer.

Der Werkstattbefund unterscheidet zwischen der eingedrückten Felge und einem bereits zuvor dokumentierten Reifenriss. Bitte behandeln Sie diesen Unterschied auch bei der Höhe. Sie vertreten die Stadt; ein Mandat des Fahrers besteht nicht. Die Akte enthält keine Aussage einer Versicherung zur Deckung. Es gab bislang keine Zahlung, keinen Vergleich und kein Anerkenntnis. Die verbleibenden Rückfragen sollen sich auf die tatsächlich entscheidenden Lücken beschränken.

Mit freundlichen Grüßen
Kunigunde Färber'''),
D('02_Schadenmeldung.docx', 'Schadenmeldung Hagebuttenweg', '10.09.2026', 'Celestino Oliveira · Kornellenpfad 9, Lindenquell', '''## 1 Meine Fahrt

Am 9. September 2026 fuhr ich gegen 06:50 Uhr mit meinem privaten Kleinwagen auf dem Hagebuttenweg in Richtung Ringelplatz. Vor Haus 24 geriet das rechte Vorderrad in ein Loch am rechten Fahrbahnrand. Es gab einen kräftigen Schlag, danach zog das Fahrzeug nach rechts. Ich hielt ungefähr zwanzig Meter weiter an. Der rechte Vorderreifen verlor Luft, und am Felgenhorn sah ich eine deutliche Verformung.

Es war hell genug zum Fahren ohne Fernlicht, aber bedeckt und die Fahrbahn war noch feucht. Ich schätze meine Geschwindigkeit auf 30 bis 35 km/h; die zulässige Höchstgeschwindigkeit dort beträgt 30 km/h. Entgegen kam ein Lieferwagen. Ich fuhr deshalb rechts, allerdings nicht auf dem Gehweg. Ich erkannte die Vertiefung erst unmittelbar vor dem Kontakt. Ob Wasser darin stand, kann ich nicht sicher sagen. Ein Warnschild habe ich nicht gesehen.

## 2 Danach

Ich rief einen Abschleppdienst, weil ich kein Ersatzrad mitführte. Der Wagen kam zur Werkstatt. Das Schlagloch habe ich später zu Fuß angesehen, aber nicht selbst vermessen. Die Maße in der städtischen Antwort stammen daher nicht von mir. Eine Dashcam habe ich nicht; das Kennzeichen des Lieferwagens habe ich mir nicht gemerkt.

Der Wagen gehört mir und wird nur privat genutzt. Die Werkstatt hatte bei einem früheren Besuch bereits etwas zum rechten Vorderreifen gesagt; ihren Auftrag vom Juli habe ich dort angefordert. Für die jetzige Rechnung möchte ich die alten und neuen Feststellungen sauber auseinanderhalten.

Celestino Oliveira'''),
D('03_Strasse_und_Kontrollen.docx', 'Straßenblatt und Kontrollauszug Hagebuttenweg', '16.09.2026', 'Stadt Lindenquell · Straßenunterhalt · Brunhild Späth', '''## 1 Straßenabschnitt

Der Hagebuttenweg ist im städtischen Bestandsverzeichnis als gewidmete Ortsstraße erfasst. Straßenbaulast und laufende Unterhaltung liegen bei der Stadt Lindenquell. Der Abschnitt zwischen Kornellenpfad und Ringelplatz ist etwa 340 Meter lang und 5,4 Meter breit. Er erschließt Wohnhäuser und eine kleine Gewerbezufahrt. Es besteht eine Geschwindigkeitsbegrenzung auf 30 km/h. Vor Haus 24 gibt es weder eine Baustelle noch eine Aufgrabung eines Versorgers.

## 2 Plan und tatsächliche Kontrollen

Der interne Streckenplan sieht für diesen Abschnitt eine Kontrolle alle zwei Wochen sowie zusätzliche Kontrollen nach konkreten Meldungen vor. Die Sichtung erfolgt bei langsamer Fahrt, bei Auffälligkeiten wird angehalten. Die Strecke wird regelmäßig von demselben Mitarbeiter gefahren; Vertretungen werden auf dem Kontrollblatt vermerkt.

Am 27. August um 09:20 Uhr trug Kontrolleur Alfons Degen ein: „Rechter Fahrbahnrand vor 24: ältere flache Flickstelle, kein offener Ausbruch erkennbar.“ Er hielt dort nicht an und nahm keine Messung vor. Die nächste planmäßige Fahrt war für 10. September eingetragen. Für den Zeitraum dazwischen liegt kein weiteres Kontrollblatt zu diesem Abschnitt vor.

## 3 Bearbeitungsstand

Eine Bürgermeldung vom 8. September wurde am 9. September morgens zur Prüfung zugeteilt. Wann aus der früheren Flickstelle ein tieferer Ausbruch entstand, ist im Straßenblatt nicht dokumentiert. Der Reparaturtrupp hat seine Feststellungen vom 10. September gesondert niedergelegt. Ein Warnschild wurde nach dem Kontrollbuch erst an diesem Tag aufgestellt.

Brunhild Späth'''),
D('04_Meldung_und_Reparatur.docx', 'Servicemeldung und Reparaturbericht', '10.09.2026', 'Stadt Lindenquell · Straßenservice · Sibel Auer', '''## 1 Eingang der Meldung

Am 8. September 2026 um 16:42 Uhr schrieb Anwohnerin Adelgunde Pflaum über das Serviceformular: „Vor Hagebuttenweg 24 bricht die alte geflickte Stelle auf. Beim Fahrradfahren bin ich gestern ausgewichen. Bitte sehen Sie danach.“ Ein Foto und Maße waren nicht beigefügt. Die Nachricht ging nach Ende der regulären Außendienstschicht ein. Sie wurde am 9. September um 07:18 Uhr von der Servicezentrale geöffnet und um 07:24 Uhr dem Straßenunterhalt zugeteilt. Als Rückmeldung war „Besichtigung nächste Runde“ eingetragen.

Die Schadenmeldung von Herrn Oliveira ging am 9. September um 11:06 Uhr telefonisch ein. Danach wurde ein gesonderter Auftrag an den Reparaturtrupp ausgelöst. Ein Einsatz am selben Tag ist im System nicht vermerkt.

## 2 Befund am Folgetag

Am 10. September um 08:10 Uhr fand unser Trupp vor Haus 24 einen Fahrbahnausbruch mit unregelmäßigem Rand. Die größte Länge betrug 55 Zentimeter, die größte Breite 38 Zentimeter und die tiefste Stelle 8 Zentimeter. Die rechte Kante lag etwa 25 Zentimeter vom Bordstein entfernt. Wasser stand zu diesem Zeitpunkt nicht im Loch. Wir stellten Warnbaken auf und füllten die Stelle bis 09:05 Uhr mit Reparaturasphalt.

Die Maße beschreiben unseren Befund vom 10. September. Niemand aus dem Trupp hatte die Stelle zur Unfallzeit am Vortag gesehen. Ob sich der Ausbruch zwischenzeitlich vergrößert hatte, wurde nicht untersucht. Die ausgebauten losen Stücke wurden als Straßenkehricht entsorgt.

Sibel Auer, Truppleitung'''),
D('05_Werkstattbefund.docx', 'Werkstattbefund und früherer Annahmevermerk', '11.09.2026', 'Radwerk Raban Rost · Kelterbogen 5, Lindenquell', '''## 1 Untersuchung nach dem Ereignis

Das Fahrzeug von Celestino Oliveira wurde am 9. September durch den Abschleppdienst angeliefert. Am rechten Vorderrad ist das innere Felgenhorn frisch eingedrückt. Das Rad verliert am Sitz des Reifens Luft. Die Verformung ist mit einer starken Kantenbelastung vereinbar. Eine Zuordnung zu einem bestimmten Schlagloch oder einer bestimmten Geschwindigkeit ist aus diesem Werkstattbefund allein nicht möglich.

Am rechten Vorderreifen befindet sich zusätzlich ein etwa 18 Millimeter langer Seitenwandschnitt mit gealtertem Rand. Dessen Lage stimmt mit der Beschreibung in unserem Annahmevermerk vom 21. Juli überein. Damals hatte Herr Oliveira einen langsamen Druckverlust prüfen lassen. Wir vermerkten: „Kleiner äußerer Seitenwandschnitt vorne rechts; Reifen zeitnah ersetzen, nicht reparieren.“ Herr Oliveira ließ die Erneuerung damals noch nicht ausführen. Eine Verformung der Felge wurde im Juli nicht vermerkt.

## 2 Reparatur und Aufbewahrung

Wir ersetzten die verformte Felge und den rechten Vorderreifen. Die Achsprüfung ergab keine zusätzliche Abweichung. Der linke Vorderreifen hatte noch 6 Millimeter Profil und blieb nach unserem Abgleich von Größe und Ausführung montiert. Der ausgetauschte rechte Reifen hatte 4 Millimeter Restprofil. Er und die Felge werden bis Ende Oktober im Werkstattlager aufbewahrt.

Ob der vorhandene Seitenwandschnitt durch den jetzigen Stoß weiter aufging, lässt sich nach unseren Beobachtungen nicht zuverlässig trennen. Eine zerstörende Materialuntersuchung wurde nicht vorgenommen. Der frühere Annahmevermerk ist in unserem Auftragsarchiv gespeichert.

Raban Rost'''),
D('06_Reparaturrechnung.docx', 'Rechnung RR-260911 mit Zahlungsbestätigung', '11.09.2026', 'Radwerk Raban Rost · Kelterbogen 5, Lindenquell', '''Rechnung an Celestino Oliveira, Kornellenpfad 9, Lindenquell. Werkstattauftrag 26-418. Fahrzeug angeliefert am 9. September, nach Reparatur abgeholt am 11. September 2026 um 16:15 Uhr.

## 1 Abgerechnete Leistungen

Eine Ersatzfelge gleicher Ausführung: 420,00 EUR netto. Ein Sommerreifen gleicher Größe und geeigneter Ausführung: 120,00 EUR netto. Montage, Auswuchten und Prüfung der Vorderachse: 80,00 EUR netto. Nettobetrag: 620,00 EUR. Umsatzsteuer 19 Prozent: 117,80 EUR. Rechnungsbetrag: 737,80 EUR.

Der Rechnungsbetrag wurde am 11. September bei Abholung per Karte vollständig bezahlt. Die ausgetauschte Felge und der Reifen verbleiben vorübergehend zur möglichen Besichtigung im Lager. Für diese Aufbewahrung wurde kein Entgelt berechnet. Mietwagen, Abschleppen und spätere Begutachtungen sind in dieser Rechnung nicht enthalten.

## 2 Bezug zum Befund

Die Rechnung beschreibt die tatsächlich ausgeführten Arbeiten. Der getrennte Werkstattbefund hält den bereits im Juli beschriebenen Seitenwandschnitt und die nun eingedrückte Felge fest. In der Pauschale von 80,00 EUR entfallen nach dem Arbeitszettel 30,00 EUR netto auf die Reifenmontage mit Auswuchten und 50,00 EUR netto auf die Achsprüfung. Weitere Schäden wurden bei unserem Auftrag nicht instand gesetzt. Herr Oliveira erteilte den Reparaturauftrag nach telefonischer Besprechung des Befunds am 10. September.

Raban Rost'''),
D('07_Abschlepprechnung.docx', 'Rechnung AS-260910: Transport zur Werkstatt', '10.09.2026', 'Abschleppdienst Selma Sauer · Schlehentor 2, Lindenquell', '''Rechnung an Celestino Oliveira, Kornellenpfad 9, Lindenquell. Einsatz am 9. September 2026, Rufannahme um 07:02 Uhr. Aufnahmeort: Hagebuttenweg, etwa zwanzig Meter hinter Haus 24 in Richtung Ringelplatz. Ziel: Radwerk Raban Rost, Kelterbogen 5.

## 1 Leistung und Entgelt

Das Fahrzeug stand am rechten Fahrbahnrand. Das rechte Vorderrad war deutlich drucklos. Wegen der sichtbaren Verformung und des fehlenden Ersatzrads wurde das Fahrzeug aufgeladen und zur Werkstatt transportiert. Die Leistung umfasst Anfahrt, Verladung, vier Kilometer Transport und Abladen. Vereinbarter Gesamtpreis einschließlich Umsatzsteuer: 182,20 EUR. Darin enthaltene Umsatzsteuer 19 Prozent: 29,09 EUR; Nettobetrag: 153,11 EUR.

Der Gesamtbetrag wurde am 12. September 2026 überwiesen und vollständig gutgeschrieben. Standgeld, Nachtzuschlag und eine weitergehende Pannenreparatur wurden nicht berechnet. Einen Schutzbrief oder eine Abrechnung über einen Automobilclub hat der Kunde nicht angegeben.

## 2 Wahrnehmung des Fahrers

Unser Mitarbeiter sah die Verformung des rechten Vorderrads, hat aber weder das behauptete Schlagloch vermessen noch den Ablauf des Fahrbahnkontakts beobachtet. Der Kunde berichtete den Hergang bei unserer Ankunft. Das Fahrzeug wurde aus Sicherheitsgründen nicht zur Werkstatt gefahren; eine Diagnose zur Ursache des Reifenschadens war nicht Gegenstand des Transportauftrags.

Selma Sauer'''),
E('08_Forderung.eml', 'Hagebuttenweg: bezahlte Rechnungen über 920 Euro', '2026-09-28T16:18:00+02:00', 'Celestino Oliveira <celestino.oliveira@postfach.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Sehr geehrte Frau Färber,

anbei übersende ich die Werkstattrechnung über 737,80 EUR und die Abschlepprechnung über 182,20 EUR. Zusammen verlange ich 920,00 EUR von der Stadt. Ich habe beide Beträge bezahlt. Das Auto ist mein Privatwagen; ich bin Arbeitnehmer und zum Vorsteuerabzug nicht berechtigt. Eine Kasko- oder Schutzbriefleistung habe ich weder erhalten noch beantragt.

Die Werkstatt hatte im Juli tatsächlich einen kleinen Schnitt am rechten Reifen festgestellt. Ich ließ ihn damals nicht austauschen, weil der Druck danach mehrere Wochen hielt. Mir ist klar, dass Sie dazu fragen werden. Nach dem Schlag am 9. September war das Rad sofort platt und die Felge sichtbar verbogen. Ob der Reifen ohnehin hätte ersetzt werden müssen, kann ich technisch nicht beurteilen; ich bitte um eine konkrete Erklärung, falls Sie eine Position kürzen wollen.

Frau Pflaum aus Haus 22 sagte mir später, sie habe den Fahrbahnschaden bereits gemeldet. Wie tief er bei ihrer Meldung war, weiß ich nicht. Ich habe keine eigenen Fotos vor dem Unfall. Bitte geben Sie mir bis zum 14. Oktober eine nachvollziehbare Antwort. Zusätzlichen Nutzungsausfall, Telefonkosten oder einen Wertverlust rechne ich nicht ab.

Mit freundlichen Grüßen
Celestino Oliveira'''),
E('09_Service_und_Deckung.eml', 'Hagebuttenweg: Nachfragen an Service und Vertragsarchiv', '2026-10-02T09:44:00+02:00', 'Roswitha Kren <risiken@lindenquell.example>', 'Kunigunde Färber <recht@lindenquell.example>', '''Liebe Frau Färber,

Frau Pflaums ursprüngliche Meldung enthielt kein Foto. Der Service hat sie heute um eine genauere Beschreibung gebeten: Seit wann war die Vertiefung offen, wie sah sie aus und gab es vor dem 9. September Wasser darin? Eine Antwort liegt noch nicht vor. Der Eintrag „Besichtigung nächste Runde“ stammt von der Servicebearbeitung, nicht von einem Mitarbeiter, der die Stelle am 9. September selbst gesehen hätte.

Zu unserer Haftpflicht habe ich im aktuellen Ordner nur eine Beitragszuordnung für den Straßenunterhalt gefunden. Versicherungsschein, Bedingungen und ein etwaiger Selbstbehalt sind im Vertragsarchiv angefordert. Eine Zusage zur Regulierung dieses Falls liegt nicht vor. Die im Ablageplan genannte Rubrik „AKHA / Ausgleich“ enthält keine Aufnahmeurkunde und keinen sonstigen Beleg einer Mitgliedschaft; daraus werde ich keine Aussage gegenüber dem Bürger ableiten.

Herr Oliveira hat noch kein Vergleichsangebot erhalten. Der technische Reifenbefund wird getrennt von der Frage geführt, wann wir von der Fahrbahngefahr wussten. Die vorhandenen Originalrechnungen und Kontrollunterlagen bleiben gesichert. Eine Anfrage an einen Versicherer oder eine Ausgleichseinrichtung wurde in diesem Vorgang durch mich noch nicht versandt.

Viele Grüße
Roswitha Kren'''),
]),
]
