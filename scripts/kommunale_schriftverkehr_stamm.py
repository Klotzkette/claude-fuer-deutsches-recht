"""Zusätzlicher Schriftverkehr für vier bestehende Testakten.

Nur neue, erfundene Unterlagen; alte Originaldateien bleiben unverändert.
Die Briefe sind DOCX-Zwischenquellen und werden vom Builder nur als PDF ausgeliefert.
Der Geburtsschadenentwurf ist eine am 05.10.2026 angefertigte historische
Rekonstruktion des Standes 22.09.2026, durch Vergleich und Zahlung überholt.
"""


def D(file, title, date, body, kind, sender='', recipient=''):
    return dict(file=file, title=title, date=date, body=body.strip(), kind=kind,
                sender=sender, recipient=recipient)


def K(label, source, description):
    return dict(label=label, source=source, description=description)


CASES = [
dict(
slug='kommunale-haftpflicht-personenschaden',
claim_file='06_Klageentwurf_Kuemmel.docx',
notes='Neuer Schriftverkehr aus Sicht der Anspruchstellerin. Die Stadt wird von Clara Klee vertreten; Klägervertreterin ist ausschließlich Leona Ehlers. Klageentwurf vom 05.10.2026, nicht eingereicht. Die neue Stadtbestätigung konkretisiert die öffentlich-rechtliche Benutzung des Bürgerhauses. Vorläufiger Streitwert 2.842,50 EUR; Schmerzensgeld unbeziffert mit 2.500 EUR Orientierung, materielle Positionen 342,50 EUR. Das Anlagenverzeichnis wird aus exhibits angefügt.',
attachments={'03_Anwaltliche_Uebermittlung.eml':['04_Anspruchsschreiben_Kuemmel.pdf'], '02_Mandantin_Ergaenzung.eml':[]},
exhibits=[
K('K1','02_Ereignismeldung.docx','Ereignismeldung mit Ort, Zeit und nasser Stelle'),
K('K2','04_Reinigungskontrolle.docx','Nachträglich erstelltes Kontrollblatt'),
K('K3','11_Teamchat.txt','Warnung um 18:03 Uhr und Reaktion bis 18:12 Uhr'),
K('K4','schriftverkehr-und-klage/01_Zeuge_Mansour.eml','Ergänzende Wahrnehmungen des Kassenmitarbeiters'),
K('K5','08_Zeugin_Lina.eml','Beobachtungen der Zeugin Okafor'),
K('K6','03_Behandlungsbericht.docx','Distale Radiusfraktur links'),
K('K7','05_Haushaltshilfe_Rechnung.docx','Zehn Hilfestunden, Rechnung und Zahlung'),
K('K8','12_Alltag_Kuemmel.docx','Konkrete Einschränkungen und Angehörigenhilfe'),
K('K9','06_Jacke_Kaufbeleg.docx','Anschaffung der Jacke im April 2025'),
K('K10','09_Reinigung_Rueckfrage.eml','Grenzen der erinnerten Kontrollzeit'),
K('K11','schriftverkehr-und-klage/04_Anspruchsschreiben_Kuemmel.pdf','Präzisierte Forderung und Gegenstand der Sachschäden'),
K('K12','schriftverkehr-und-klage/05_Antwort_Stadt.pdf','Benutzungsverhältnis und offene Haftungsprüfung'),
],
documents=[
D('01_Zeuge_Mansour.eml','Bücherabend: meine Beobachtung vor der Meldung','2026-10-02T16:22:00+02:00', '''Sehr geehrte Frau Morgenrot,

ich ergänze den von mir exportierten Gruppenchat. Ich stand am 12. September an der Einlasskasse neben dem Büchertisch. Dort wurden keine Eintrittsgelder erhoben; ich zählte die Besucher und gab Programmblätter aus. Gegen 18:02 Uhr sah ich vor der Matte einen glänzenden Fleck. Ich konnte aus etwa drei Metern Entfernung nicht erkennen, woher die Flüssigkeit kam. Ich schrieb um 18:03 Uhr die gespeicherte Nachricht und las kurz darauf Ludgers Antwort „gleich“.

Bis zum Ruf nach dem Sturz sah ich niemanden dort wischen oder ein Schild aufstellen. Ich hatte keine eigene Sperrkette an der Kasse. Ein Mitarbeiter hätte sich aber zwischen die Außentür und die nasse Stelle stellen und Besucher über die rechte trockene Seite leiten können. Es gab nach meiner Wahrnehmung weder Gedränge noch einen anderen Notfall. Dass ich das nicht selbst veranlasste, erklärt sich aus meiner Annahme, Ludger kümmere sich nach seiner Antwort sofort darum. Den eigentlichen Sturz habe ich nur aus dem Augenwinkel bemerkt.

Meine ladungsfähige Dienstanschrift ist Stadt Hainbogen, Kulturamt, Buchsbaumplatz 4, 97299 Hainbogen. Ich bin bereit, meine Wahrnehmungen als Zeuge zu schildern. Der Chat zeigt keine Lesebestätigungen; ich kann deshalb nichts darüber sagen, wann Celine die Nachricht tatsächlich gelesen hat.

Mit freundlichen Grüßen
Farid Mansour''','email','Farid Mansour <farid.mansour@hainbogen.example>','Mira Morgenrot <recht@hainbogen.example>'),
D('02_Mandantin_Ergaenzung.eml','Unterlagen zum Sturz und Umfang meiner Forderung','2026-10-03T09:18:00+02:00', '''Sehr geehrte Frau Ehlers,

Sie vertreten nur mich. Frau Klee ist nach meiner Kenntnis auf der anderen Seite für die Stadt tätig. Ich möchte, dass Sie zunächst meinen Anspruch erklären und einen Klageentwurf vorbereiten. Eine Klage soll ohne meine Entscheidung noch nicht eingereicht werden.

Den Gips trage ich weiterhin. Bei der Kontrolle wurde mir kein dauerhafter Schaden bestätigt; einen neuen schriftlichen Befund habe ich noch nicht. Die Beschwerden in der ersten Woche und meine Schwierigkeiten mit Wäsche und schweren Einkäufen habe ich in meinen Notizen beschrieben. Die zehn bezahlten Stunden der Haushaltshilfe betreffen die dort genannten Verrichtungen. Die unbezahlte Hilfe meiner Tochter will ich nicht noch einmal in Geld abrechnen.

Meine dunkelgrüne Jacke war vor dem Sturz gebraucht, aber unbeschädigt. Der linke Ärmel ist jetzt eingerissen. Meine Tochter Senta Kümmel, Lerchenbogen 10, 97299 Hainbogen, sah den Riss, als sie zum Bürgerhaus kam. Die Jacke liegt ungewaschen in einem Beutel bei mir und kann vorgelegt werden. Für sie beschränke ich die jetzige Forderung auf 45 EUR. Die alten 89,90 EUR waren der Kaufpreis, nicht ein ermittelter Zeitwert. Die noch gesuchten Taxibelege und eine zusätzliche Kostenpauschale sollen nicht in die Klage aufgenommen werden.

Freundliche Grüße
Ottilie Kümmel''','email','Ottilie Kümmel <ottilie.kuemmel@briefpost.example>','Rechtsanwältin Leona Ehlers <leona@ehlers-recht.example>'),
D('03_Anwaltliche_Uebermittlung.eml','Kümmel gegen Stadt Hainbogen – Anspruchsschreiben','2026-10-03T11:05:00+02:00', '''Sehr geehrte Frau Morgenrot,

ich vertrete Frau Ottilie Kümmel und übersende Ihnen das beigefügte Anspruchsschreiben. Der ursprünglich genannte Jackenkaufpreis wird für die jetzige Bezifferung auf einen gebrauchten Wert von 45 EUR begrenzt. Taxikosten, Angehörigenhilfe und eine Pauschale werden in diesem Schritt nicht verlangt. Die bezahlte Haushaltshilfe und das Schmerzensgeld bleiben getrennte Positionen.

Bitte sichern Sie den vollständigen Chatexport, die vorhandenen Fassungen des Kontrollblatts und die Angaben zur Benutzung des Bürgerhauses. Ich bitte insbesondere um Klarstellung, in welcher Rechtsform die Stadt die allgemeine Besucherbenutzung organisiert. Aus dem Umstand, dass kein Eintritt verlangt wurde, leite ich allein noch keine abschließende Haftungszuordnung ab.

Ein gerichtliches Verfahren habe ich nicht eingeleitet. Die Antwortbitte meiner Mandantin zum 9. Oktober besteht fort. Für die Zahlung ist im Schreiben eine gesonderte Frist bezeichnet. Meine Mandantin ist an einer zügigen außergerichtlichen Lösung interessiert.

Mit freundlichen Grüßen
Leona Ehlers, Rechtsanwältin''','email','Rechtsanwältin Leona Ehlers <leona@ehlers-recht.example>','Mira Morgenrot <recht@hainbogen.example>'),
D('04_Anspruchsschreiben_Kuemmel.docx','Kümmel gegen Stadt Hainbogen – präzisierte Forderung','03.10.2026', '''Rechtsanwältin Leona Ehlers
Buchfinkenstraße 9, 97299 Hainbogen

An die Stadt Hainbogen
Rechtsamt, Frau Mira Morgenrot
Buchsbaumplatz 1, 97299 Hainbogen

Sturz im Bürgerhaus am 12. September 2026

Sehr geehrte Frau Morgenrot,

ich vertrete Frau Ottilie Kümmel, Lerchenbogen 8, 97299 Hainbogen. Meine Mandantin stürzte um etwa 18:08 Uhr unmittelbar vor der Schmutzfangmatte des Bürgerhauses. Die nasse Stelle ist im Ereignisbericht dokumentiert. Die Chatwarnung von 18:03 Uhr und die Antwort des Hausmeisters von 18:04 Uhr sind bei der Prüfung der rechtzeitig möglichen Sicherung zu berücksichtigen. Die spätere Niederschrift einer nur ungefähr erinnerten Kontrolle widerlegt diese konkrete Gefahrenmeldung nicht.

Meine Mandantin erlitt die im Ambulanzbericht beschriebene Radiusfraktur links. Sie verlangt ein angemessenes Schmerzensgeld, für das sie derzeit 2.500 EUR zugrunde legt. Hinzu kommen die tatsächlich bezahlten 297,50 EUR für zehn Stunden erforderlicher Haushaltshilfe und 45 EUR für die beim Sturz beschädigte gebrauchte Jacke. Damit ergibt sich für die außergerichtliche Verständigung ein Betrag von 2.842,50 EUR. Die Hilfe ihrer Tochter, Taxikosten und eine allgemeine Pauschale werden mit diesem Schreiben nicht zusätzlich berechnet. Das Schmerzensgeld ist anhand des vollständigen Verlaufs zu beurteilen; eine endgültige Prognose dauerhafter Folgen liegt noch nicht vor.

Bitte teilen Sie bis zum 9. Oktober Ihre Haftungsposition und die Rechtsform der Besucherbenutzung mit. Zur Zahlung des begründeten Betrags setzen wir eine Frist bis zum 16. Oktober 2026. Mit dieser Frist wird kein bereits eingetretener Verzug rückdatiert. Falls einzelne Positionen aus Ihrer Sicht nicht ausreichend belegt sind, bezeichnen Sie bitte den konkreten Einwand und die dafür maßgeblichen Tatsachen.

Die Forderung enthält keine Abfindung unbekannter Spätfolgen und keine Erklärung zum Versicherungsschutz der Stadt. Ein Klageentwurf wird vorbereitet; er wurde nicht eingereicht. Eine nachvollziehbare außergerichtliche Lösung bleibt möglich.

Mit freundlichen Grüßen
Leona Ehlers
Rechtsanwältin''','letter'),
D('05_Antwort_Stadt.docx','Stadt Hainbogen – Antwort zum Bürgerhaus','05.10.2026', '''Stadt Hainbogen
Rechtsamt, Buchsbaumplatz 1, 97299 Hainbogen

An Rechtsanwältin Leona Ehlers
Buchfinkenstraße 9, 97299 Hainbogen

Frau Kümmel – Bücherabend vom 12. September 2026

Sehr geehrte Frau Ehlers,

wir bestätigen den Eingang Ihres Schreibens. Die Stadt Hainbogen besitzt und betreibt das Bürgerhaus. Es ist als gemeindliche öffentliche Einrichtung gewidmet. Der Bücherabend war eine eigene Veranstaltung unseres Kulturamts im Rahmen dieses Benutzungszwecks. Die Zulassung der Besucher erfolgte im öffentlich-rechtlichen Benutzungsverhältnis; individuelle private Veranstaltungs- oder Mietverträge wurden mit ihnen nicht geschlossen. Die Stadt hat ihren Sitz im Landgerichtsbezirk Würzburg. Bürgermeisterin ist Jette Linden.

Die Gruppe erhielt um 18:03 Uhr die von Herrn Mansour beschriebene Nachricht. Der Inhalt der weiteren Wahrnehmungen und die damals praktisch mögliche Reaktion werden geprüft. Eine genaue Kontrolle der Fliesen um 17:55 Uhr können wir nach der Klarstellung von Frau Kaya nicht bestätigen. Daraus folgt für uns allerdings noch nicht ohne Weiteres, dass jedes zwischenzeitliche Auftreten von Nässe pflichtwidrig unbeachtet blieb.

Die Forderung über 2.842,50 EUR ist vorgemerkt. Wir erklären heute weder ein Anerkenntnis noch eine Zahlung. Bei Schmerzensgeld und Haushaltshilfe benötigen wir einen nachvollziehbaren Verlauf; die ursprüngliche Rechnung über Hilfeleistungen bestreiten wir als Urkunde nicht. Die beschädigte Jacke sollte bis zur Abstimmung erhalten bleiben. Wir werden die Antwortbitte zum 9. Oktober berücksichtigen und Ihren Zahlungszeitpunkt gesondert behandeln.

Unsere versicherungsrechtlichen Unterlagen sind noch nicht vollständig. Das ist kein sachlicher Einwand gegen einen begründeten Anspruch Ihrer Mandantin. Eine Aussage über Mitgliedschaft in einem Schadenausgleich oder Rückdeckung wird nicht abgegeben.

Mit freundlichen Grüßen
Mira Morgenrot
Für die Stadt Hainbogen''','letter'),
D('06_Klageentwurf_Kuemmel.docx','Klageentwurf Kümmel gegen Stadt Hainbogen','05.10.2026', '''ENTWURF VOM 5. OKTOBER 2026 – NICHT EINGEREICHT

An das Landgericht Würzburg
Ottostraße 5, 97070 Würzburg

Klage der Frau Ottilie Kümmel, Lerchenbogen 8, 97299 Hainbogen,
– Klägerin –
Prozessbevollmächtigte: Rechtsanwältin Leona Ehlers, Buchfinkenstraße 9, 97299 Hainbogen,

gegen die Stadt Hainbogen, vertreten durch die Erste Bürgermeisterin Jette Linden, Buchsbaumplatz 1, 97299 Hainbogen,
– Beklagte –

wegen Schadensersatzes und Schmerzensgeldes aus dem Sturz vom 12. September 2026.
Vorläufiger Streitwert: 2.842,50 EUR.

## 1. Anträge und Umfang

Für den Fall der späteren Freigabe und Einreichung wird beantragt,

1. die Beklagte zu verurteilen, an die Klägerin ein angemessenes Schmerzensgeld zu zahlen, dessen Höhe in das Ermessen des Gerichts gestellt wird, wobei nach gegenwärtigem Vortrag mindestens 2.500 EUR als angemessen angesehen werden, nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage;
2. die Beklagte zu verurteilen, an die Klägerin 342,50 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage zu zahlen;
3. der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Es wird um Anordnung des schriftlichen Vorverfahrens gebeten. Ein Versäumnisurteil wird nur für den Fall beantragt, dass die gesetzlichen Voraussetzungen nach wirksamer Zustellung und Ablauf der Verteidigungsanzeigefrist vorliegen. Der Entwurf behauptet weder eine Zustellung noch eine bereits abgelaufene Gerichtsfrist.

Der materielle Antrag betrifft ausschließlich 297,50 EUR bezahlte Haushaltshilfe und 45 EUR Wert der beschädigten gebrauchten Jacke. Die früher erwähnten Taxikosten, weitere Angehörigenhilfe und eine allgemeine Pauschale sind nicht Gegenstand dieser Klage. Das Schmerzensgeld wird nach dem gesamten bei der maßgeblichen Entscheidung erkennbaren Verletzungsverlauf bemessen; eine künstliche Aufteilung nach einzelnen Wochen wird nicht verlangt. Noch unbekannte, objektiv nicht vorhersehbare Spätfolgen sind mit dem vorliegenden Zahlungsbegehren nicht als pauschal abgefunden erklärt.

## 2. Zuständigkeit und Benutzungsverhältnis

Die Klage betrifft die Verletzung einer drittgerichteten Amtspflicht bei der Sicherung einer gemeindlichen öffentlichen Einrichtung. Die Beklagte hat ihre Eigentümer- und Betreiberstellung, die öffentliche Widmung und die öffentlich-rechtliche Zulassung der Besucher ausdrücklich bestätigt. Es handelt sich um eine eigene Veranstaltung des Kulturamts innerhalb des Widmungszwecks. Damit wird die Amtshaftungszuordnung nicht lediglich aus dem öffentlichen Eigentum oder dem fehlenden Eintrittspreis abgeleitet. Beweis: Stadtantwort vom 5. Oktober 2026, Anlage K12.

Für den Anspruch aus § 839 BGB in Verbindung mit Art. 34 GG ist das Landgericht gemäß § 71 Abs. 2 Nr. 2 GVG ohne Rücksicht auf den Streitwert zuständig. Die seit 2026 in § 23 Nr. 1 GVG genannte allgemeine Amtsgerichtsgrenze von 10.000 EUR ändert diese besondere Zuweisung nicht. Die Beklagte hat ihren Sitz im Bezirk des angerufenen Gerichts; dort liegt auch der Ereignisort. Die örtliche Zuständigkeit folgt aus §§ 12, 17 und 32 ZPO. Klägerin ist die unmittelbar verletzte Besucherin. Ansprüche ihrer Tochter oder eines Sozialleistungsträgers werden nicht geltend gemacht.

Sollte das Gericht die bestätigte Benutzungsorganisation abweichend einordnen, wird um Hinweis gebeten. Die vorgetragenen Sicherungs- und Organisationspflichten sind dann auch unter § 823 Abs. 1 BGB sowie den hierfür einschlägigen Zurechnungsnormen zu prüfen. Eine bestimmte sachliche Zuständigkeit wird für diesen alternativen rechtlichen Ansatz nicht allein aus der Bezeichnung „Stadt“ beansprucht.

## 3. Ereignis und erkennbare Gefahr

Am 12. September 2026 veranstaltete das Kulturamt im Bürgerhaus am Buchsbaumplatz 4 einen öffentlichen Bücherabend. Der Eingang war ab 17:30 Uhr geöffnet. Vor der inneren Saaltür lag eine Schmutzfangmatte. Der Bereich zwischen Außentür und Matte war gefliest. Nach Regen am Nachmittag musste mit Feuchtigkeit gerechnet werden; entscheidend ist hier jedoch die anschließend konkret gemeldete nasse Stelle.

Um 18:03 Uhr schrieb der Einlassmitarbeiter Farid Mansour in die dienstliche Gruppe, vor der Matte glänze eine kleine Pfütze, und bat um einen Wischer. Hausmeister Ludger Lauch antwortete um 18:04 Uhr, er sei im Saal am Mikrofon und komme gleich. Um 18:08 Uhr folgte die Meldung des Sturzes. Erst um 18:12 Uhr wurde gewischt und ein Schild aufgestellt. Der Chat enthält diese Zeitstempel, aber keine Lesebestätigungen. Die Klägerin behauptet deshalb nicht, dass auch die Reinigungskraft jede Nachricht zeitgleich gelesen habe. Beweis: Chatexport, Anlage K3; ergänzende Nachricht des Herrn Mansour, Anlage K4; Zeugnis Mansour, zu laden über die Beklagte, Kulturamt, Buchsbaumplatz 4.

Die Klägerin ging normal durch den Eingang. Kurz vor der Matte rutschte ihr ein Fuß weg. Sie stürzte auf die linke Hand. Die Zeugin Lina Okafor stand etwa drei Meter entfernt am Büchertisch. Sie beobachtete das Wegrutschen, sah kein Mobiltelefon in der Hand der Klägerin und nahm vor dem Sturz kein Warnschild wahr. Nach dem Ereignis sah sie klare Flüssigkeit an der Sturzstelle. Ihre frühere Wendung „alles nass“ bezog sie später ausdrücklich auf diese Stelle, nicht auf sämtliche Eingangsflächen. Beweis: Anlage K5; Zeugnis Lina Okafor, zu laden über Lesekreis Hainbogen, Buchsbaumplatz 4, 97299 Hainbogen.

Der hinzugekommene Hausmeister sah selbst einen etwa handtellergroßen nassen Bereich vor der Matte. Er hat den Sturz nicht gesehen und kann Herkunft und Dauer der Nässe nicht bestimmen. Diese Begrenzung seiner Kenntnis steht der zuvor dokumentierten Warnung nicht entgegen. Beweis: Ereignismeldung, Anlage K1; Zeugnis Ludger Lauch, zu laden über die Beklagte.

## 4. Pflichtverletzung und Kausalität

Die Beklagte musste den benutzbaren Zugang im Rahmen des Zumutbaren gegen konkrete, für Besucher nicht zuverlässig erkennbare Rutschgefahren sichern. Verlangt wird keine lückenlose Gefahrlosigkeit und auch keine ständige Trockenheitsgarantie bei jeder Witterung. Beanstandet wird, dass eine tatsächlich gemeldete Pfütze vor dem erwartbar benutzten Zugang mehrere Minuten ohne kurzfristige Absicherung blieb, obwohl ein einfaches Warnen oder Umlenken möglich war.

Nach Herrn Mansours Beobachtung gab es weder Gedränge noch einen konkurrierenden Notfall. Eine Person hätte Besucher auf der trockenen rechten Seite vorbeiführen können. Der Hausmeister hatte die Meldung nach seiner Antwort wahrgenommen. Die Reinigungskraft las sie erst nach dem Sturz; ihr Telefon lag im Nebenraum, eine Vertretung für eingehende Gefahrenmeldungen war nicht vereinbart. Die Klägerin rügt damit sowohl die konkrete Reaktion als auch die unklare Organisation der kurzfristigen Sicherung. Beweis: Anlagen K3, K4 und K10; Zeugnis Celine Kaya, zu laden über den Reinigungsdienst der Beklagten.

Das Kontrollblatt wurde erst am Folgetag erstellt. Frau Kaya beschrieb einen nur ungefähr auf 17:55 Uhr geschätzten Gang mit einem vollen Müllsack; eine gezielte Prüfung der Fliesen fand nicht statt. Die Klägerin erklärt diesen nachträglichen Vermerk nicht allein wegen seines Erstellungsdatums für wertlos. Er beweist aber weder eine genaue Kontrollminute noch eine damals sicher trockene Fläche und beseitigt die spätere konkrete Warnung nicht. Beweis: Anlagen K2 und K10.

Eine rechtzeitige Warnung oder Sperrung hätte verhindert, dass die Klägerin gerade über die nasse Stelle ging. Die zeitliche und örtliche Verbindung ergibt sich aus der Chatmeldung, dem beobachteten Wegrutschen und dem unmittelbar danach festgestellten Wasser. Eine andere Sturzursache ist nicht belegt. Die Klägerin bietet für den Ablauf ihre persönliche Anhörung und, soweit zulässig, Parteivernehmung an; dies wird nicht als Ersatz für die verfügbaren unabhängigen Zeugen behandelt.

Zum allgemeinen Umfang zumutbarer Sicherung vgl. BGH, Urteil vom 9. September 2008 – VI ZR 279/06, Rn. 9–10. Der dortige Sachverhalt ist kein Bürgerhausfall; herangezogen wird nur der allgemeine Maßstab. Der konkrete Organisationsvorwurf folgt hier aus den eigenen Unterlagen der Beklagten.

## 5. Verletzung und immaterieller Schaden

Die Ambulanz stellte am selben Abend eine nicht verschobene distale Radiusfraktur links fest und legte einen Unterarmgips an. Durchblutung, Motorik und Sensibilität waren erhalten. Weitere akute Verletzungen sind nicht dokumentiert. Beweis: Behandlungsbericht, Anlage K6; Zeugnis der behandelnden Ärztin Dr. Indira Klee, Ambulanz Kleeweg, Kleeweg 3, 97299 Hainbogen; erforderlichenfalls medizinisches Sachverständigengutachten.

Die rechtshändige Klägerin konnte sich zwar teilweise selbst versorgen, jedoch keine schweren Einkäufe, gefüllten Töpfe oder Wäschekörbe sicher tragen. In der ersten Woche bestanden besonders nachts Schmerzen. Sie lebt allein; ihre Tochter half im Wesentlichen an Wochenenden. Eine Operation oder bleibende Funktionsbeeinträchtigung wird nicht behauptet. Ein aktueller schriftlicher Verlaufsbericht muss vor einer tatsächlichen Einreichung ergänzt beziehungsweise im Verfahren beigezogen werden. Beweis: Alltagsnotizen, Anlage K8; Zeugnis Senta Kümmel, Lerchenbogen 10.

Die Klägerin hält derzeit ein Schmerzensgeld von insgesamt mindestens 2.500 EUR gemäß § 253 Abs. 2 BGB für angemessen. Maßgeblich sind Bruch, Ruhigstellung, Schmerzen und Alltagsbeschränkungen, nicht ein starres Tagessystem. Vorleistungen auf das Schmerzensgeld gab es nicht. Die Einschätzung ist kein medizinisch abgesicherter Dauerschadenzuschlag und soll die richterliche Gesamtwürdigung nicht vorwegnehmen.

## 6. Materieller Schaden und Einwendungen

Die Klägerin bezahlte 297,50 EUR für zehn Stunden Haushaltshilfe an vier Tagen. Die Rechnung nennt Einkauf, Küche, Wäsche, Bad, Böden und Bettwäsche. Diese Tätigkeiten konnte die Klägerin mit der ruhiggestellten linken Hand nicht im erforderlichen Umfang selbst ausführen. Der Aufwand passt zu einem 64-Quadratmeter-Einpersonenhaushalt und liegt unter dem vorher geschätzten üblichen Wochenaufwand, wobei einzelne leichte Tätigkeiten weiterhin möglich waren. Es wird nicht jeder frühere Haushaltszeitanteil als vollständiger Ausfall angesetzt. Beweis: Rechnung und Zahlungsbestätigung, Anlage K7; Anlage K8; Zeugnis Hedwig Hummel, Gartenbogen 6, 97299 Hainbogen. Die unentgeltliche Wochenendhilfe der Tochter wird nicht nochmals abgerechnet.

Die gebrauchte Jacke war im April 2025 für 89,90 EUR gekauft worden und riss beim Sturz am linken Ärmel ein. Die Klägerin verlangt hierfür nur 45 EUR und stellt das Kleidungsstück zur Besichtigung zur Verfügung. Der Kaufbeleg beweist allein die damalige Anschaffung, nicht den Sturzschaden oder den heutigen Wert; hierfür werden die Wahrnehmung der Tochter und der Augenschein angeboten. Beweis: Anlage K9, Zeugnis Senta Kümmel und Vorlage der Jacke. Eine neue Jacke wurde nicht gekauft; ein Neupreis wird nicht zusätzlich verlangt.

Ein Mitverschulden nach § 254 BGB ist nicht aus bloß allgemein möglicher Feuchtigkeit herzuleiten. Die Klägerin ging normal, trug flache Schuhe und benutzte kein Telefon. Sollte die Beklagte abweichende konkrete Wahrnehmungen vortragen, sind diese aufzuklären. Die Klägerin stützt ihre Darstellung nicht auf eine unzulässige generelle Beweislastumkehr. Eine anderweitige Ersatzleistung ist nicht erfolgt; die hier verlangten Positionen stehen nach ihrem Vortrag ihr selbst zu. Medizinische Behandlungskosten werden nicht geltend gemacht.

## 7. Zinsen und Verfahrensstand

Die Zahlungsfrist des außergerichtlichen Anspruchsschreibens K11 läuft bei Erstellung dieses Entwurfs noch. Vorgerichtliche Verzugszinsen oder bereits entstandene Prozesskosten werden daher nicht erfunden. Beantragt sind ausschließlich Prozesszinsen nach §§ 291, 288 Abs. 1 Satz 2 BGB ab dem Tag nach einer erst künftig möglichen Zustellung. Die Versicherungsprüfung der Beklagten beeinflusst den gesetzlichen Anspruch nicht. Eine Vergleichsbereitschaft ist weder Haftungsanerkenntnis noch Verzicht der Klägerin.

Die genannten Anlagen werden vor Einreichung mit ihren Originalen abgeglichen. Der Entwurf benötigt insbesondere die abschließende Entscheidung der Klägerin über das Vorgehen und den aktuellen Behandlungsstand. Eine entsprechende Beauftragung wird durch das Vorhandensein dieses Dokuments nicht behauptet.

Leona Ehlers
Rechtsanwältin – Entwurf ohne Einreichung''','claim'),
]),
]

CASES.append(dict(
slug='akha-wuerzburg-rohrbruch',
claim_file='06_Teilklageentwurf_Zimt.docx',
notes='Entwurf vom 05.10.2026, nicht eingereicht. Offene Teilklage ausschließlich wegen der bezahlten Trocknungskosten von 2.400 EUR netto; weder die vorläufigen 15.100 EUR noch Umsatz werden als fertiger Schaden übernommen. Eigene Anspruchsposition und eng begrenzte Abtretung werden getrennt vorgetragen. Das Anlagenverzeichnis wird aus exhibits angefügt.',
attachments={'03_Annahme_und_Mandat.eml':[], '01_Trocknungsumfang.eml':[]},
exhibits=[
K('K1','02_Schadenmeldung.docx','Wassereintritt, eigener Betrieb und betroffene Sachen'),
K('K2','03_Einsatzbericht.docx','Außerhalb des Hauses gerissene Straßenleitung und tatsächlicher Betreiber'),
K('K3','11_Stoerungslog.txt','Zeitlicher Zusammenhang von Absperrung und nachlassendem Eintritt'),
K('K4','04_Trocknung_Rechnung.docx','Leistungen, Nettobetrag und bezahlte Rechnung'),
K('K5','schriftverkehr-und-klage/01_Trocknungsumfang.eml','Zweck und Abgrenzung der Trocknungsleistungen'),
K('K6','08_Vermieterin.eml','Eigentümerin, Vermietung und unbekannter Zustand der Durchführung'),
K('K7','schriftverkehr-und-klage/02_Begrenzte_Abtretung.eml','Angebot der eng bezeichneten Anspruchsabtretung'),
K('K8','schriftverkehr-und-klage/03_Annahme_und_Mandat.eml','Annahme der Abtretung und Ausgabenbestätigung'),
K('K9','schriftverkehr-und-klage/04_Teilforderung_Zimt.pdf','Außergerichtliche Begrenzung und Zahlungsaufforderung'),
K('K10','schriftverkehr-und-klage/05_Antwort_Versorgung.pdf','Betreiberbestätigung und konkrete Einwendungen'),
],
documents=[
D('01_Trocknungsumfang.eml','TR-260918: Umfang unserer Arbeiten','2026-10-02T14:10:00+02:00', '''Sehr geehrter Herr Zimt,

ich bestätige für die Trockenwerk Tilda Tuch GmbH unsere Rechnung vom 18. September. Wir pumpten am 14. September das noch stehende Wasser aus Ihrem Lagerkeller ab und nahmen den verunreinigten Boden auf. Die Geräte liefen anschließend bis zur Abholung am 18. September. Reinigung und Feuchtemessungen betrafen denselben Raum, einschließlich der Stellflächen Ihrer Mühlen. Ohne diese Maßnahmen hätten Sie weder die dortigen eigenen Betriebssachen sicher bergen noch den gemieteten Raum wieder nutzen können. Die Arbeiten dienten zugleich dazu, die weitere Durchfeuchtung des Gebäudes zu begrenzen.

Die 600 EUR für Abpumpen und Erstaufnahme, 1.200 EUR für Gerätebereitstellung und Betrieb sowie 600 EUR für Reinigung und Feuchtemessungen sind die drei Positionen derselben Rechnung. Elektrische Reparaturen, Mühlenreparaturen, eine neue Wandabdichtung oder Ausbauarbeiten sind darin nicht enthalten. Eine zweite Rechnung für denselben Einsatz haben wir weder an Frau Waffel noch an eine Versicherung gestellt. Ihre Zahlung von 2.856 EUR ging am 19. September vollständig ein. Wie schon in der Rechnung vermerkt, blieb die Prüfung der Wand offen; wir bescheinigen keine vollständige bauliche Sanierung.

Ich kann Ort, Arbeitsablauf und Rechnung persönlich erläutern. Die Entscheidung über die Ursache des Rohrbruchs liegt außerhalb unseres Auftrags.

Freundliche Grüße
Tilda Tuch
Geschäftsführerin · Trockenwerk Tilda Tuch GmbH
Werkbogen 3, 97076 Würzburg''','email','Tilda Tuch <rechnung@trockenwerk.example>','Eberhard Zimt <eberhard@zimt-zange.example>'),
D('02_Begrenzte_Abtretung.eml','Kaffeebogen: Abtretung nur für die bezahlte Trocknung','2026-10-03T09:10:00+02:00', '''Lieber Herr Zimt,

Sie haben die Rechnung TR-260918 allein bezahlt. Ich habe dafür weder Ihnen noch dem Trocknungsunternehmen Geld erstattet und werde dieselben Kosten nicht noch einmal für mich verlangen.

Zur eindeutigen Zuordnung biete ich Ihnen hiermit die Abtretung aller mir gegen die Kommunalversorgung Mainbogen GmbH aus dem Wassereintritt vom 14. September 2026 am Kaffeebogen 6 zustehenden Ersatzansprüche an, soweit sie gerade die in Rechnung TR-260918 enthaltenen Abpump-, Trocknungs-, Reinigungs- und Messleistungen bis zu 2.400 EUR netto betreffen. Erfasst wird nur diese Kostenposition, unabhängig davon, ob sie rechtlich meinem Gebäudeeigentum oder Ihrer Nutzung zuzuordnen ist. Ich garantiere damit nicht, dass tatsächlich ein eigener Anspruch in dieser Höhe besteht. Ansprüche auf weitere Wand- oder Elektroreparaturen, Mietforderungen und sonstige Gebäudeschäden verbleiben bei mir. Die Abtretung verändert unseren Mietvertrag nicht und begründet keine zusätzliche Zahlungspflicht Ihrerseits.

Bitte bestätigen Sie die Annahme. Gegenüber dem Versorgungsunternehmen darf diese Nachricht vorgelegt werden. Ich habe diese begrenzten Ansprüche nicht anderweitig abgetreten. Eine Erstattung durch einen Gebäudeversicherer ist für diese Rechnung nicht erfolgt.

Mit freundlichen Grüßen
Walburga Waffel
Eibenhof 8, 97074 Würzburg''','email','Walburga Waffel <walburga@waffel-immobilien.example>','Eberhard Zimt <eberhard@zimt-zange.example>'),
D('03_Annahme_und_Mandat.eml','Annahme Ihrer begrenzten Abtretung','2026-10-03T11:42:00+02:00', '''Sehr geehrte Frau Waffel,

ich nehme Ihr heutiges Abtretungsangebot für die bezeichnete Trocknungsrechnung bis 2.400 EUR netto an. Auch ich verlange diese Position nur einmal. Ich habe die Bruttorechnung vom Geschäftskonto bezahlt und bin für diese Leistung zum Vorsteuerabzug berechtigt. Weder Sie noch ein Versicherer haben mir diese Kosten ersetzt.

Für meine Forderung ist nun Rechtsanwältin Alina Ahrens, Gerstenbogen 11, 97070 Würzburg, beauftragt. Ihre Tätigkeit gilt ausschließlich mir. Frau Klee ist nach meiner Kenntnis für die Gegenseite tätig. Frau Ahrens darf die außergerichtliche Forderung zunächst auf die belegten Trocknungskosten beschränken und einen Klageentwurf vorbereiten; eine Klage ist damit nicht eingereicht. Meine frühere Summe von 15.100 EUR war ausdrücklich vorläufig. Über Mühlen, Elektrik oder einen nach Kosten und nachgeholten Aufträgen bereinigten Ausfall liegen noch nicht alle Informationen vor.

Ich werde weder Ihren übrigen Gebäudeschaden noch meine unaufgeklärten Positionen in diese Teilforderung hineinrechnen. Die durchfeuchteten Mühlen und das ausgebaute Rohrstück sollen weiter für eine gemeinsame Untersuchung zur Verfügung bleiben.

Freundliche Grüße
Eberhard Zimt''','email','Eberhard Zimt <eberhard@zimt-zange.example>','Walburga Waffel <walburga@waffel-immobilien.example>'),
D('04_Teilforderung_Zimt.docx','Bezahlte Trocknungskosten: begrenzte Zahlungsaufforderung','04.10.2026', '''Rechtsanwältin Alina Ahrens
Gerstenbogen 11, 97070 Würzburg

An die Kommunalversorgung Mainbogen GmbH
Geschäftsführung und Rechtsabteilung
Netzlaubenweg 4, 97076 Würzburg

Sehr geehrte Damen und Herren,

ich vertrete ausschließlich Eberhard Zimt, Inhaber von Zimt & Zange am Kaffeebogen 6 in Würzburg. Im Anschluss an seine vorläufige Forderungsanmeldung verlange ich zunächst 2.400,00 EUR netto für die tatsächlich ausgeführten und am 19. September bezahlten Trocknungsarbeiten. Bitte zahlen Sie diesen Betrag bis zum 16. Oktober 2026 an meinen Mandanten. Die erbetene Rückmeldung bis zum 12. Oktober bleibt sinnvoll; eine bereits abgelaufene Zahlungsfrist wird daraus nicht hergeleitet.

Ihr eigener Einsatzbericht lokalisiert den Längsriss etwa 1,5 Meter vor der Hauswand in der Straßenverteilungsleitung. Der Zusammenhang mit dem Wassereintritt wird durch dessen Rückgang nach der Absperrung gestützt. Eine ursprünglich von der Mitarbeiterin vermutete Heizungsleckage wurde bei der Sichtkontrolle nicht festgestellt. Wir stützen die Forderung insbesondere auf § 2 Abs. 1 HPflG. Der Gebäudestandort der beschädigten Sachen allein erfüllt den Ausschluss des § 2 Abs. 3 Nr. 1 HPflG nicht, wenn das Wasser aus der außerhalb gelegenen Anlage austrat.

Die Rechnung betrifft ausschließlich Abpumpen, Trocknung, Reinigung und Feuchtemessungen. Frau Waffel hat ergänzend ihre etwaigen Ansprüche gegen Sie aus genau dieser Position bis zur Nettosumme abgetreten; mein Mandant hat angenommen. Damit wird kein zweiter Kostenersatz beansprucht. Umsatzsteuer ist wegen des Vorsteuerabzugs nicht Bestandteil der Forderung. Die drei gebrauchten Mühlen, Elektroarbeiten und ein etwaiger Erwerbsschaden sind ausdrücklich nicht Gegenstand dieses bezifferten Teilbegehrens. Über diese Positionen wird auch kein Verzicht erklärt.

Bitte erhalten Sie das ausgebaute Rohrstück und ermöglichen Sie eine abgestimmte Besichtigung. Benennen Sie konkrete Tatsachen, auf die Sie einen Ausschluss oder ein Mitverschulden stützen. Der bislang ungeklärte Zustand einer älteren Wanddurchführung ist noch kein Nachweis einer dem Mandanten zurechenbaren Pflichtverletzung.

Mit freundlichen Grüßen
Alina Ahrens
Rechtsanwältin''','letter'),
D('05_Antwort_Versorgung.docx','Rohrbruch Kaffeebogen: Antwort auf die Teilforderung','05.10.2026', '''Kommunalversorgung Mainbogen GmbH
Netzlaubenweg 4, 97076 Würzburg
Geschäftsführer Konrad Fenn

An Rechtsanwältin Alina Ahrens
Gerstenbogen 11, 97070 Würzburg

Sehr geehrte Frau Ahrens,

wir bestätigen den Eingang Ihres Schreibens vom 4. Oktober. Unsere Gesellschaft betreibt die im Einsatzbericht bezeichnete Straßenverteilungsleitung auf eigene Rechnung und entscheidet über Kontrolle, Absperrung und Wiederinbetriebnahme. Sitz und Geschäftsleitung befinden sich an der oben genannten Anschrift. Den festgestellten Riss außerhalb des Hauses stellen wir nach dem bisherigen Einsatzbefund nicht in Frage.

Eine Haftungsanerkennung erklären wir nicht. Der Materialbefund liegt noch nicht vor. Auch der genaue Wasserweg durch die Wanddurchführung ist nicht abschließend untersucht. Wir halten es für prüfbedürftig, ob die Gebäudeschäden dem gesetzlichen Gebäudeausschluss unterfallen und ob die Eigentümerin für eine unzureichende Abdichtung verantwortlich ist. Bitte erläutern Sie außerdem, weshalb sämtliche Trocknungsarbeiten Ihrem Mandanten und nicht der Eigentümerin zuzuordnen sein sollen. Ihre Mitteilung der begrenzten Abtretung werden wir berücksichtigen; deren Wirksamkeit und Reichweite sind damit nicht anerkannt.

Wir vermerken, dass aktuell nur 2.400 EUR netto verlangt werden. Die übrige Anmeldung behandeln wir weiterhin als unvollständig belegt. Das Rohrstück bleibt erhalten. Einen Besichtigungstermin können die Beteiligten gesondert abstimmen. Mit diesem Schreiben werden keine Versicherungsbedingungen bestätigt und keine Zahlung zugesagt. Wir bemühen uns um eine inhaltliche Rückmeldung innerhalb Ihrer Frist.

Mit freundlichen Grüßen
Mira Morgenrot
Rechtsabteilung''','letter'),
D('06_Teilklageentwurf_Zimt.docx','Entwurf einer offenen Teilklage – Trocknungskosten','05.10.2026', '''ENTWURF VOM 5. OKTOBER 2026 – NICHT EINGEREICHT
Nur bezahlte Trocknungskosten; andere Positionen bleiben außerhalb dieses Verfahrensentwurfs.

An das Amtsgericht Würzburg
Ottostraße 5
97070 Würzburg

Eberhard Zimt, Einzelunternehmer unter der Bezeichnung Zimt & Zange, Kaffeebogen 6, 97076 Würzburg,
– Kläger –
Prozessbevollmächtigte: Rechtsanwältin Alina Ahrens, Gerstenbogen 11, 97070 Würzburg,

gegen

Kommunalversorgung Mainbogen GmbH, Netzlaubenweg 4, 97076 Würzburg, vertreten durch den Geschäftsführer Konrad Fenn,
– Beklagte –

wegen Ersatzes von Trocknungskosten nach Wasseraustritt aus einer Straßenleitung.
Vorläufiger Streitwert: 2.400,00 EUR.

## 1. Anträge und genauer Gegenstand

Für den Fall einer späteren Einreichung wird beantragt,

1. die Beklagte zu verurteilen, an den Kläger 2.400,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage zu zahlen;
2. der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Die Klage betrifft ausschließlich den Nettobetrag der Rechnung TR-260918 der Trockenwerk Tilda Tuch GmbH vom 18. September 2026. Sie wird als offene Teilklage aus dem Schadensereignis erhoben. Innerhalb dieser Rechnung werden die drei Positionen Abpumpen und Erstaufnahme, Gerätebetrieb sowie Reinigung und Feuchtemessung vollständig verlangt. Es handelt sich nicht um einen beliebig herausgelösten Teil eines ungegliederten Gesamtschadens.

Nicht Gegenstand sind Mühlenreparatur oder Mühlenersatz, elektrische Instandsetzung, weitere Gebäudearbeiten und ein Erwerbsschaden. Der Kläger übernimmt insbesondere seine frühere überschlägige Anmeldung von 15.100 EUR nicht als fertige Schadenberechnung. Die dort enthaltenen 3.400 EUR waren Nettoumsatz und kein nachgewiesener Gewinn. Ein Verzicht auf außerhalb dieser Teilklage liegende Ansprüche wird nicht erklärt. Die gegenwärtige Teilforderung ist gegenüber jeder späteren Berechnung als bereits verlangte Position zu kennzeichnen, um Überschneidungen zu vermeiden.

## 2. Zuständigkeit und Beteiligte

Das Amtsgericht ist nach § 23 Nr. 1 GVG sachlich zuständig. Der 2026 maßgebliche allgemeine Zuständigkeitswert beträgt 10.000 EUR; die hier isoliert eingeklagte Forderung bleibt darunter. Es geht nicht um einen Amtshaftungsanspruch. Die Beklagte wird als Betreiberin einer Wasserleitungsanlage nach dem Haftpflichtgesetz in Anspruch genommen. Ein kommunaler Gesellschafter allein verändert diesen Anspruch nicht in Amtshaftung. Ihr Sitz befindet sich in Würzburg; auch Anlage, Schadensort und betroffener Betrieb liegen hier. Die örtliche Zuständigkeit folgt aus §§ 12, 17 ZPO und ergänzend dem örtlichen Bezug des Schadensereignisses nach § 32 ZPO.

Der Kläger ist natürliche Person und führt das Geschäft als Einzelunternehmen. Die Geschäftsbezeichnung ist keine eigene juristische Person. Die Beklagte bestätigt ihre tatsächliche Betriebsverantwortung für den betroffenen Straßenabschnitt in K10. Damit hängt ihre Inhabereigenschaft nicht allein davon ab, ob ein Grundstücksregister die Leitung als Eigentum ausweist. Sie entscheidet über Einsatz, Unterhaltung und Absperrung und betreibt die Anlage auf eigene Rechnung.

## 3. Schadensereignis und Herkunft des Wassers

Am 14. September 2026 gegen 06:50 Uhr bemerkte die Mitarbeiterin Mira Ben Ami Wasser im Lagerkeller des Geschäfts Kaffeebogen 6. Um etwa 07:20 Uhr stand es an der tiefsten Stelle ungefähr zwölf Zentimeter hoch. Dort befanden sich eigene gebrauchte Vorführmühlen des Klägers. Wasser gelangte in deren Gehäuse; außerdem waren Boden, untere Wände und Steckdosen betroffen. Die erste telefonische Vermutung eines Heizungsrohrbruchs beruhte auf dem sichtbaren Wasser und war keine technische Feststellung.

Beweis: Schadenmeldung K1; Zeugnis der Mira Ben Ami, zu laden über den Betrieb des Klägers, Kaffeebogen 6, 97076 Würzburg.

Die Störungsmeldung ging um 07:04 Uhr bei der Beklagten ein. Ihr Netzteam sperrte den Straßenleitungsabschnitt um 07:42 Uhr ab. Danach ließ der Wassereintritt durch die Leitungsdurchführung in der Kelleraußenwand deutlich nach. Bei der Freilegung um 09:15 Uhr fand Einsatzleiter Severin Sprosse einen Längsriss in der Straßenverteilungsleitung. Die Schadstelle befand sich im öffentlichen Gehweg rund 1,5 Meter vor der Außenwand, nicht in der Hausleitung hinter dem Zähler. Ein gebrochenes Heizungsrohr wurde bei der Sichtkontrolle nicht gefunden; der angezeigte Heizungsdruck blieb unverändert. Nach Ersatz des gerissenen Stücks wurde die Leitung um 13:30 Uhr wieder in Betrieb genommen.

Beweis: Einsatzbericht K2; Störungslog K3; Zeugnis des Severin Sprosse, zu laden über die Beklagte. Ergänzend wird bei substantiiertem Bestreiten ein wassertechnisches Sachverständigengutachten zum Zusammenhang zwischen äußerer Leckage, Eintrittsweg und Kellerüberflutung angeboten.

Diese räumliche und zeitliche Folge trägt die Behauptung, dass Wasser aus der von der Beklagten betriebenen Leitung die Überflutung verursachte. Eine vollständige Materialuntersuchung liegt noch nicht vor. Der Kläger behauptet daher weder einen bestimmten Korrosionsmechanismus noch eine nachgewiesene schuldhafte Wartungslücke. Für die vorrangige Gefährdungshaftung ist die technische Ursache des Risses von seiner bereits belegten Funktion als Austrittsstelle zu unterscheiden.

## 4. Erforderliche Maßnahmen und Anspruchszuordnung

Der Kläger beauftragte am Schadenstag Trockenwerk Tilda Tuch. Das Unternehmen pumpte ab, nahm die Verunreinigungen auf, betrieb bis zum 18. September Trocknungsgeräte und führte Reinigung und Feuchtemessungen aus. Die Maßnahmen dienten dem Bergen und weiteren Schutz der eigenen Betriebssachen, der Wiederherstellung der Nutzbarkeit des gemieteten Raums und der Begrenzung fortschreitender Gebäudedurchfeuchtung. Sie umfassten weder eine neue Wandabdichtung noch Mühlen- oder Elektroreparaturen.

Beweis: Rechnung und Zahlungsbestätigung K4; Erläuterung K5; Zeugnis der Tilda Tuch, Werkbogen 3, 97076 Würzburg.

Die Rechnung lautet auf den Kläger. Er bezahlte am 19. September 2.856 EUR brutto. Da er für diese betrieblichen Eingangsleistungen zum Vorsteuerabzug berechtigt ist, verlangt er nur 2.400 EUR netto. Er hat keine Erstattung der Eigentümerin oder eines Versicherers erhalten. Rechnung und Zahlung allein ersetzen den Nachweis der Erforderlichkeit nicht. Diesen erbringt der Kläger durch den beschriebenen Wasserstand, die konkreten Arbeitspositionen und die Aussage der Auftragnehmerin. Für die Angemessenheit der angesetzten Kosten wird, falls diese konkret bestritten wird, Sachverständigenbeweis angeboten.

Die Eigentümerin Walburga Waffel hatte den Keller an den Kläger vermietet. Soweit die einheitlichen Sofortmaßnahmen rechtlich ihrem Gebäudeschaden zuzuordnen sein sollten, hat sie am 3. Oktober ihre gegen die Beklagte bestehenden Ansprüche aus genau den Leistungen der Rechnung TR-260918 bis 2.400 EUR netto an den Kläger abgetreten. Dieser nahm am selben Tag an. Gegenstand und Schuldner sind bestimmt; weitergehende Wand-, Elektro- oder Mietpositionen bleiben ausgenommen. Die Abtretung dient nicht dazu, nicht bestehende Ansprüche zu erzeugen, sondern ordnet einen etwaigen Anspruch aus dieser einzigen Kostenposition zu.

Beweis: Vermieterinnennachricht K6, Abtretungsangebot K7 und Annahme K8; Zeugnis der Walburga Waffel, Eibenhof 8, 97074 Würzburg.

Der Kläger stützt die Forderung vorrangig auf eigene notwendige Aufwendungen zur Beseitigung der Folgen der Sachbeschädigung und hilfsweise, soweit das Gericht die Maßnahmen dem Gebäudeeigentum zuordnet, auf die abgetretenen Ansprüche nach § 398 BGB. Beide Begründungen verfolgen dieselbe einmalige Zahlung, keine kumulierten Beträge. Eine Leistung würde deshalb in beiden Zuordnungen berücksichtigt; die Eigentümerin erhebt diese Rechnungsposition nicht daneben.

## 5. Haftung und Einwendungen

§ 2 Abs. 1 HPflG erfasst Schäden durch die Wirkungen von Flüssigkeiten, die von einer Rohrleitungsanlage ausgehen. Hier trat Wasser aus der Straßenverteilungsleitung aus und beschädigte Sachen im Keller. Die Beklagte ist Inhaberin der Anlage. Für diesen gesetzlichen Haftungsgrund ist eine zuvor konkret erkannte Leckgefahr nicht Voraussetzung. Der Kläger muss dennoch Anlage, Inhaber, Austritt, Sachbeschädigung und Zusammenhang mit der verlangten Kostenposition darlegen und beweisen.

Die Beklagte verweist in K10 auf den Gebäudeausschluss. Nach § 2 Abs. 3 Nr. 1 HPflG genügt jedoch nicht, dass der Schaden innerhalb eines Gebäudes eintrat. Auch die dort bezeichnete Anlage muss innerhalb des Gebäudes gelegen sein. Der festgestellte Riss liegt außerhalb; gerade diese Abgrenzung ist durch K2 belegt. Die bloße Weiterleitung des ausgetretenen Wassers durch eine Wandöffnung macht die äußere Straßenanlage nicht zur inneren Hausinstallation. Sollte sich bei weiterer Untersuchung eine andere ursächliche Schadstelle ergeben, wäre die Zuordnung neu zu bewerten. Ein solcher Befund liegt derzeit nicht vor.

Höhere Gewalt ist nicht mit einer unbekannten Materialursache gleichzusetzen. Es ist kein von außen kommendes außergewöhnliches Ereignis vorgetragen. Eine Entlastung wegen sorgfältiger Wartung beseitigt die gesetzliche Gefährdungshaftung ebenfalls nicht. Umgekehrt wird eine Verschuldenshaftung nach § 823 BGB nicht allein daraus hergeleitet, dass überhaupt ein Rohr riss. Eine solche zusätzliche Begründung würde gesonderte Feststellungen zu Organisations-, Kontroll- oder Reparaturpflichten erfordern.

Zur Wanddurchführung liegt bisher nur vor, dass sie älter ist. Frau Waffel kennt keinen Wassereintritt in den vergangenen zwei Jahren; eine fachlich festgestellte Vorschädigung fehlt. Selbst eine objektive Undichtigkeit beantwortete noch nicht, wer hiervon wusste, welche Sicherungspflicht bestand und welche Maßnahme den Schaden verhindert hätte. Für ein dem Kläger zuzurechnendes Mitverschulden nach § 254 BGB fehlen damit bislang konkrete Tatsachen. Auch die Aufstellung von Vorführmühlen auf niedrigen Rollbrettern in einem zuvor nutzbaren Lagerkeller begründet ohne bekannte Überflutungsgefahr keine bestimmte Kürzungsquote. Der Kläger verschweigt die offenen baulichen Fragen nicht und ermöglicht die Untersuchung.

## 6. Höhe, Zinsen und Verfahrensstand

Die Forderung setzt sich aus 600 EUR Abpumpen und Erstaufnahme, 1.200 EUR Gerätebereitstellung und Betrieb sowie 600 EUR Reinigung und Feuchtemessungen zusammen. Sämtliche Ansätze sind netto. Ein zusätzlicher Ersatz der gezahlten Umsatzsteuer würde wegen des Vorsteuerabzugs über den verbleibenden Schaden hinausgehen. Ersatz für neue Mühlen lässt sich aus einer telefonischen Preisangabe für Neugeräte nicht ableiten und wird hier nicht beansprucht. Ebenso ist das noch nicht beauftragte Elektroangebot kein Bestandteil der Zahlungsklage.

Mit K9 wurde Zahlung bis zum 16. Oktober verlangt. Diese Frist läuft bei Erstellung des Entwurfs noch. Ein früherer Verzug oder eine erfolgte Klagezustellung werden nicht behauptet. Die beantragten Prozesszinsen richten sich nach §§ 291, 288 Abs. 1 Satz 2 BGB und beginnen erst am Tag nach einer tatsächlichen Zustellung. Es werden fünf Prozentpunkte verlangt; der Schadenersatz ist keine Entgeltforderung aus einem Geschäft zwischen Unternehmern.

Die Unterlagen zu Versicherung, Schadenausgleich und Rückdeckung bleiben außerhalb dieses Klagegegenstands. Aus einem leeren Aktenordner entsteht weder eine Anspruchsgegnerin noch eine Deckungszusage. Die Beklagte bleibt aus dem eigenen Anlagenbetrieb in Anspruch genommen. Vor einer Einreichung sind die Anlagen vollständig beizufügen, Zustellanschriften nochmals zu bestätigen und die Entscheidung des Klägers über das weitere Vorgehen einzuholen. Dieser Entwurf dokumentiert keine bereits erhobene Klage.

Alina Ahrens
Rechtsanwältin – Entwurf ohne Einreichung''','claim'),
]))

CASES.append(dict(
slug='akha-wuerzburg-geburtsschaden',
claim_file='06_Historischer_Klagevorentwurf_Winter.docx',
notes='ARCHIVSTATUS: Am 05.10.2026 rekonstruierter historischer Vorentwurf mit ausschließlich dem Erkenntnisstand vom 22.09.2026. Durch Teilvergleich vom 23.09.2026 und vollständige Familienzahlung von insgesamt 13,2 Mio. EUR überholt; NICHT EINREICHBAR. Keine neue Familienforderung, keine Klage gegen AKHA oder Rückdeckung. Historischer Gegenstand: 80.000 EUR verbleibende konkrete Wohnanpassungskosten sowie weiteres angemessenes Schmerzensgeld mit 600.000 EUR Orientierung nach 300.000 EUR Vorschuss, vorläufiger Streitwert 680.000 EUR. Nur der materielle Anspruch ist eine sachlich abgegrenzte Teilklage; Schmerzensgeld umfasst alle damals erkennbaren und vorhersehbaren Folgen. Keine freie Kapitalisierung künftiger Renten. Das Anlagenverzeichnis wird aus exhibits angefügt; es enthält keine erst nach dem 22.09.2026 entstandenen Belege.',
attachments={'03_Archivstatus_05Oktober.eml':[], '01_Eltern_Umbaukosten.eml':[]},
exhibits=[
K('K1','03_Geburtsdokumentation.docx','Geburtsverlauf und frühe Befunde; nur Auszug, vollständige Ausgangsakte gesondert vorzulegen'),
K('K2','04_Gutachten_Geburtshilfe.docx','Beurteilung vom 23.04.2018 zu Verzögerung und Kausalität'),
K('K3','05_Haftungsanerkenntnis.docx','Anerkenntnis mit Feststellungswirkung, Verjährungsverzicht und Schmerzensgeldvorschuss'),
K('K4','07_Pflegebericht.docx','Aktueller Funktions- und Unterstützungsbedarf im Juni 2026'),
K('K5','06_Eltern_Pflegealltag.eml','Elternangaben zum Alltag und zur Vertretung allein des Kindes'),
K('K6','17_Wohnanpassung.docx','180.000 EUR Rechnung, zweckgebundener Abschlag 100.000 EUR und Restzahlung 80.000 EUR'),
K('K7','schriftverkehr-und-klage/01_Eltern_Umbaukosten.eml','Historische Bestätigung zur Finanzierung und Zweckabgrenzung'),
K('K8','schriftverkehr-und-klage/02_Klinik_Zwischenstand.eml','Historischer Zahlungs- und Prüfstand vor einem Vergleich'),
K('K9','schriftverkehr-und-klage/04_Forderung_vor_Vergleich.pdf','Historisches begrenztes Zahlungsbegehren'),
K('K10','schriftverkehr-und-klage/05_Antwort_vor_Vergleich.pdf','Historische Antwort ohne Anerkennung der verlangten Höhe'),
],
documents=[
D('01_Eltern_Umbaukosten.eml','Noras Umbau: Rechnung, Zahlungen und Umfang','2026-09-20T18:40:00+02:00', '''Sehr geehrter Herr Berg,

für die Vorbereitung eines begrenzten Zahlungsbegehrens bestätigen wir den Stand vom heutigen 20. September. Die Rechnung der Raumweg Bau GmbH vom 28. August beträgt 180.000 EUR brutto. Am 5. Februar wurden daraus 100.000 EUR als Abschlag bezahlt; dieses Geld stammte aus dem für die Wohnanpassung bestimmten Teil des bisherigen Vorschusses. Die restlichen 80.000 EUR wurden am 4. September von Noras Konto bezahlt. Wir verlangen den Abschlag nicht noch einmal. Die Rechnung ist vollständig beglichen und richtet sich an Nora, vertreten durch uns.

Der Auftrag betraf den stufenlosen Zugang, die erforderlichen Türanpassungen, das Pflegebad und die Vorbereitung des Deckenlifts. Es ging um die alltägliche Versorgung Noras in unserem Haus. Wir haben keine allgemeine Küchenmodernisierung, neue Terrasse oder eigene Wohnraumvergrößerung in diese Rechnung aufnehmen lassen. Das Eigentum am Haus liegt bei uns Eltern; Nora erhielt deshalb kein Grundstück. Die Aufwendungen dienen trotzdem ihrer notwendigen Nutzung und Versorgung. Andere Rechnungen oder künftige Umbauwünsche sollen nicht in die verbleibenden 80.000 EUR hineingerechnet werden.

Uns geht es nur um Ansprüche Noras. Eigene Verdienstausfälle von uns Eltern sollen Sie nicht einklagen. Das 2018 gezahlte Schmerzensgeld von 300.000 EUR ist bei jeder weiteren Forderung abzuziehen. Wir wünschen eine Prüfung eines weiteren Schmerzensgeldes; eine verbindliche Vereinbarung über einen Endbetrag besteht heute noch nicht. Eine Berechnung lebenslanger Pflege oder eines gesamten Erwerbsschadens auf dieser schmalen Grundlage wollen wir nicht als feststehend darstellen.

Bitte behandeln Sie Ihre Ausarbeitung zunächst als Vorbereitung und besprechen Sie einen möglichen gerichtlichen Schritt erneut mit uns. Die Vergleichsgespräche laufen weiter.

Hannah und Tobias Winter
Auenpfad 7, 97072 Würzburg''','email','Hannah und Tobias Winter <familie.winter@briefpost.example>','Rechtsanwalt Selim Berg <selim.berg@berg-auen.example>'),
D('02_Klinik_Zwischenstand.eml','Winter: Zahlungszuordnung vor weiterer Besprechung','2026-09-21T10:25:00+02:00', '''Sehr geehrter Herr Berg,

zur Vorbereitung der weiteren Besprechung bestätige ich den Stand vom 21. September: Die im Anerkenntnis vom 15. Juni 2018 zugesagten 300.000 EUR wurden als Schmerzensgeldvorschuss gezahlt. Von den weiteren bereits geleisteten 900.000 EUR waren 800.000 EUR für bisherige materielle Mehrbedarfspositionen und 100.000 EUR für die Wohnanpassung bestimmt. Eine weitere Zahlung allein auf die Schlussrechnung Raumweg vom 28. August ist bis heute nicht erfolgt. Diese Zuordnung ändert nicht die noch offene Prüfung der Schlussrechnung und möglicher Drittleistungen.

Ein Endbetrag für das Schmerzensgeld ist noch nicht vereinbart. Ebenso gibt es heute keine verbindliche Gesamtabfindung künftiger Pflege-, Wohn- oder Erwerbsschäden. Das Anerkenntnis von 2018 besteht mit seinem dort beschriebenen Umfang fort. Wir erklären weder, dass jeder künftig geforderte Betrag berechtigt ist, noch, dass eine für Vergleichsgespräche verwendete Rechengröße bereits einer gesetzlichen Forderung entspricht.

Bitte grenzen Sie gegebenenfalls bezifferte Forderungen von noch offenen Zukunftspositionen ab. Ihre Antwort kann uns über die bekannte Schadenbearbeitung erreichen; die Klinik bleibt Anspruchsgegnerin. Aussagen zu einem internen Ausgleich oder einer Rückdeckung sind mit dieser Nachricht nicht verbunden.

Mit freundlichen Grüßen
Mareike Seidel
Geschäftsführerin · Klinik Mainblick GmbH
Mainauenweg 18, 97074 Würzburg''','email','Mareike Seidel <geschaeftsfuehrung@klinik-mainblick.example>','Rechtsanwalt Selim Berg <selim.berg@berg-auen.example>'),
D('03_Archivstatus_05Oktober.eml','Nur Archiv: Vorentwurf 22. September durch Vergleich überholt','2026-10-05T12:10:00+02:00', '''Liebe Frau Winter, lieber Herr Winter,

für die Dokumentation des Ablaufs ist der historische Vorentwurf mit Erkenntnisstand 22. September nun in lesbarer Form zur Akte genommen. Seine heutige Ausfertigung bedeutet ausdrücklich keinen neuen Einreichungsauftrag. Das Dokument ist überholt und darf nicht als aktuelle Klage eingereicht werden.

Am 23. September wurde der Teilvergleich über insgesamt 13,2 Millionen EUR geschlossen. Nach den bereits früher gezahlten 1,2 Millionen EUR gingen am 29. September weitere 12 Millionen EUR ein. Damit sind die im Vergleich bezifferten Familienpositionen bezahlt. Auch die im historischen Entwurf behandelten Schmerzensgeld- und Wohnkostenpositionen dürfen nicht nochmals verlangt werden. Die Archivkopie zeigt nur, welche engere Forderung vor dem Vergleich anhand damaliger Unterlagen hätte vorbereitet werden können. Die damals nicht bekannten späteren Vergleichs- und Zahlungsunterlagen sind deshalb nicht als Anlagen des historischen gerichtlichen Vortrags aufgeführt.

Die im Vergleich ausdrücklich vorbehaltenen Fälle wären nur nach dessen Voraussetzungen und anhand eines neuen konkreten Sachverhalts gesondert zu prüfen. Ein solcher neuer Anspruch wird mit dieser Nachricht nicht behauptet. Interne Abrechnungen zwischen Versicherer, Schadenausgleich und Rückdeckung begründen ebenfalls keine erneute Familienforderung. Für eine Klage Noras gegen einen fiktiven Modellausgleich gibt es hier keine belegte Grundlage.

Bitte verwahren Sie die Ausarbeitung mit der Kennzeichnung „historisch – überholt – nicht einreichbar“. Ich bestätige nochmals: Es wurde auf Grundlage dieses Vorentwurfs keine Klage erhoben.

Mit freundlichen Grüßen
Selim Berg
Rechtsanwalt''','email','Rechtsanwalt Selim Berg <selim.berg@berg-auen.example>','Hannah und Tobias Winter <familie.winter@briefpost.example>'),
D('04_Forderung_vor_Vergleich.docx','Historisches Forderungsschreiben vor dem Vergleich','21.09.2026', '''ARCHIVKOPIE – historischer Stand 21. September 2026.
Am 5. Oktober 2026 für die Akte ausgefertigt. Durch den späteren Teilvergleich und dessen Bezahlung überholt; keine aktuelle Zahlungsaufforderung.

Rechtsanwalt Selim Berg · Kanzlei Berg & Auen
Auenring 11, 97072 Würzburg

An die Klinik Mainblick GmbH
z. H. Geschäftsführerin Mareike Seidel
Mainauenweg 18, 97074 Würzburg

Sehr geehrte Frau Seidel,

ich vertrete Nora Winter, geboren am 14. Februar 2016, gemeinsam gesetzlich vertreten durch Hannah und Tobias Winter. Unter Berücksichtigung des Anerkenntnisses von 2018 und der bereits geleisteten Vorschüsse präzisiere ich zwei gegenwärtig prüfbare Positionen. Dieses Schreiben gibt ausschließlich den Stand vom 21. September wieder; die parallel geführten Vergleichsgespräche haben heute noch keinen verbindlichen Gesamtabfindungsbetrag hervorgebracht.

Aus der vollständig bezahlten Rechnung Raumweg Bau GmbH über 180.000 EUR brutto verbleiben nach Anrechnung des zweckbezogenen Abschlags von 100.000 EUR noch 80.000 EUR. Die Rechnung betrifft Zugang, Türanpassung, Pflegebad und Liftvorbereitung für Nora. Eine über diese Rechnung hinausgehende Wohnkapitalisierung wird nicht verlangt. Bitte teilen Sie bis zum 30. September mit, welche konkrete Position Sie beanstanden, und ersetzen Sie den berechtigten Restbetrag.

Daneben halten wir ein weiteres angemessenes Schmerzensgeld für erforderlich. Unsere derzeitige Orientierung beträgt insgesamt 900.000 EUR, wovon die bereits gezahlten 300.000 EUR abzuziehen sind; die offene Orientierung beträgt daher 600.000 EUR. Dies ist eine zu begründende Bewertung der schweren, dauerhaften Folgen und kein bereits anerkannter oder tariflich festgelegter Betrag. Maßgeblich sollen sämtliche jetzt erkennbaren und vorhersehbaren Folgen sein. Eine beliebige Aufteilung in Schmerzensgeldjahre beabsichtigen wir nicht.

Künftige Pflege- und Erwerbsschäden sollen in diesem begrenzten Zahlungsbegehren nicht frei kapitalisiert werden. Die Rechte aus dem Anerkenntnis, einschließlich seiner Feststellungswirkung und seines Verjährungsverzichts, bleiben im dort geregelten Umfang bestehen. Eigene Ansprüche der Eltern, übergegangene Ansprüche von Leistungsträgern und interne Versicherungsabrechnungen sind nicht Gegenstand dieses Schreibens. Eine Gesamterledigung wird nicht angeboten.

Mit freundlichen Grüßen
Selim Berg
Rechtsanwalt''','letter'),
D('05_Antwort_vor_Vergleich.docx','Historische Antwort auf das begrenzte Forderungsschreiben','22.09.2026', '''ARCHIVKOPIE – historischer Stand 22. September 2026.
Am 5. Oktober 2026 für die Akte ausgefertigt. Durch spätere Vereinbarung und Zahlung überholt; kein aktueller Regulierungsstand.

Klinik Mainblick GmbH
Mainauenweg 18, 97074 Würzburg

An Rechtsanwalt Selim Berg
Auenring 11, 97072 Würzburg

Sehr geehrter Herr Berg,

wir haben Ihr Schreiben vom 21. September erhalten. An der durch das Anerkenntnis von 2018 beschriebenen Haftung dem Grunde nach halten wir fest. Die von Ihnen nun verlangten Beträge sind dadurch nicht automatisch anerkannt. Ihre Anrechnung des Schmerzensgeldvorschusses von 300.000 EUR und des für die Wohnanpassung verwendeten Abschlags von 100.000 EUR entspricht der mitgeteilten Zweckzuordnung; eine weitere auf diese Rechnung geleistete Zahlung ist uns heute nicht bekannt.

Wir möchten zur Schlussrechnung insbesondere die medizinisch bedingte Erforderlichkeit sämtlicher Arbeiten und etwaige Leistungen anderer Träger überprüfen. Dass die Rechnung bezahlt ist, beantwortet diese Fragen nicht allein. Die Restforderung von 80.000 EUR nehmen wir zur Prüfung auf. Einen pauschalen Vorteil allein aus dem Eigentum der Eltern am Wohnhaus behaupten wir damit nicht; eine mögliche darüber hinausgehende Verbesserung wäre konkret zu bewerten.

Auch die Schmerzensgeldhöhe bleibt Gegenstand der Besprechung. Der aktuelle Bericht beschreibt einen sehr hohen Hilfebedarf. Er enthält aber keine individuelle statistische Lebenszeitprognose, aus der eine taggenaue Berechnung abgeleitet werden könnte. Einen bestimmten Gesamtbetrag haben wir bisher nicht verbindlich vereinbart. Bitte verstehen Sie diese Antwort weder als endgültige Ablehnung jeder weiteren Zahlung noch als Einigung auf 900.000 EUR.

Die Gespräche werden fortgesetzt. Eine Vereinbarung zur abschließenden Regulierung anderer Positionen ist mit diesem Antwortschreiben nicht geschlossen. Interne Rückdeckungsmodelle werden nicht Bestandteil der Haftungsbeziehung zu Nora Winter.

Mit freundlichen Grüßen
Mareike Seidel
Geschäftsführerin''','letter'),
D('06_Historischer_Klagevorentwurf_Winter.docx','Historischer Klagevorentwurf: Erkenntnisstand 22. September','05.10.2026', '''HISTORISCHER VORENTWURF – ÜBERHOLT – NICHT EINREICHBAR
Redaktionell ausgefertigt am 5. Oktober 2026. Der nachfolgende gerichtliche Entwurf rekonstruiert ausschließlich den Erkenntnisstand vom 22. September 2026.
Späterer Archivhinweis: Der Teilvergleich vom 23. September 2026 und die vollständige Zahlung von insgesamt 13,2 Millionen EUR haben die hier vorbereiteten Forderungen erledigt. Dieser Text ist keine aktuelle Klage und darf keine erneute Forderung auslösen. Die späteren Unterlagen sind nicht Beweismittel des nachfolgenden historischen Vortrags.

Historischer Entwurfsstand: Würzburg, 22. September 2026

An das Landgericht Würzburg
Ottostraße 5
97070 Würzburg

Nora Winter, geboren am 14. Februar 2016, Auenpfad 7, 97072 Würzburg, gemeinsam gesetzlich vertreten durch ihre sorgeberechtigten Eltern Hannah Winter und Tobias Winter, beide ebenda,
– Klägerin –
Prozessbevollmächtigter: Rechtsanwalt Selim Berg, Kanzlei Berg & Auen, Auenring 11, 97072 Würzburg,

gegen

Klinik Mainblick GmbH, Mainauenweg 18, 97074 Würzburg, vertreten durch ihre Geschäftsführerin Mareike Seidel,
– Beklagte –

wegen weiterer Entschädigung für einen Geburtsschaden.
Vorläufiger Streitwert des historischen Entwurfs: 680.000,00 EUR.

## 1. Historisch vorbereitete Anträge und deren Reichweite

Auf dem Stand vom 22. September 2026 wären folgende Anträge zur Entscheidung der gesetzlichen Vertreterinnen und Vertreter vorbereitet worden:

1. Die Beklagte wird verurteilt, an die Klägerin über den bereits geleisteten Schmerzensgeldvorschuss von 300.000 EUR hinaus ein weiteres angemessenes, in das Ermessen des Gerichts gestelltes Schmerzensgeld zu zahlen, dessen zusätzliche Höhe nach Vorstellung der Klägerin 600.000 EUR nicht unterschreiten sollte, nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage.
2. Die Beklagte wird verurteilt, an die Klägerin 80.000 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage zu zahlen.
3. Der Beklagten werden die Kosten des Rechtsstreits auferlegt.

Der materielle Antrag zu 2 ist eine offen erklärte, sachlich abgegrenzte Teilklage: Er erfasst ausschließlich den nach Anrechnung des zweckgebundenen Abschlags verbleibenden Betrag der bereits bezahlten Rechnung RW-260828 der Raumweg Bau GmbH. Frühere Pflege- und Betreuungskosten, künftiger Mehrbedarf, Erwerbsschäden und andere Wohnkosten sind nicht Gegenstand dieses Zahlungsbegehrens. Eine beliebige Quote aus einem unaufgeschlüsselten Millionenbetrag wird nicht verlangt.

Der Schmerzensgeldantrag wird dagegen nicht künstlich auf einzelne Jahre oder einzelne bereits bekannte Folgen begrenzt. Er verlangt eine einheitliche Entschädigung unter Einbeziehung sämtlicher im historischen Beurteilungszeitpunkt erkennbarer und vorhersehbarer Verletzungsfolgen. Die Klägerin rechnet den Vorschuss vollständig an. Unvorhersehbare spätere Entwicklungen wären nach den dafür geltenden Voraussetzungen gesondert zu beurteilen; ein pauschaler Vorbehalt macht bereits vorhersehbare Folgen nicht zu einem neuen Schmerzensgeldanspruch.

Eine weitere Feststellungsklage wird nicht vorbereitet. Das Anerkenntnis vom 15. Juni 2018 enthält bereits die dort näher bestimmte Wirkung einer rechtskräftigen Feststellung und einen Verjährungsverzicht. Ein zusätzliches Feststellungsinteresse müsste über diesen bestehenden Schutz hinaus konkret dargelegt werden. Der vorliegende Entwurf konzentriert sich deshalb auf zwei bezifferbare beziehungsweise gerichtlich zu bemessende Zahlungspositionen.

## 2. Parteien, Zuständigkeit und bestehendes Anerkenntnis

Die Klägerin ist das behandelte und geschädigte Kind. Ihre Eltern handeln gemeinsam für sie; eigene persönliche Ansprüche der Eltern werden nicht geltend gemacht. Die Beklagte ist die Trägerin der Klinik. Der Versicherer und ein interner Schadenausgleich sind keine weiteren Beklagten dieses Entwurfs. Eine interne Rückdeckungsrechnung schafft keinen unmittelbaren Zahlungsanspruch des Kindes.

Das Landgericht ist sowohl wegen des über 10.000 EUR liegenden Streitwerts nach § 71 Abs. 1 GVG als auch nach § 71 Abs. 2 Nr. 9 GVG für Streitigkeiten aus Heilbehandlungen unabhängig vom Streitwert zuständig. Die 2026 geltende besondere Zuständigkeit wird neben der Wertzuständigkeit benannt. Sitz der Beklagten und Behandlungsort liegen in Würzburg; die örtliche Zuständigkeit folgt aus §§ 12, 17 und 32 ZPO. Eine tatsächliche Einreichung, Zustellung oder Geschäftsverteilung zu einer bestimmten Kammer wird nicht behauptet.

Die Frankenbogen Kommunalversicherung VVaG erklärte am 15. Juni 2018 namens und mit Vollmacht der Beklagten die volle Haftung für die durch den Geburtsfehler verursachten materiellen und immateriellen Schäden einschließlich künftiger Folgen, soweit Ansprüche nicht auf Dritte übergegangen sind. Ein Mitverschulden von Mutter oder Kind wurde nicht eingewandt. Das Anerkenntnis soll im festgehaltenen Umfang wie ein am 15. Juni 2018 rechtskräftig gewordenes Feststellungsurteil wirken; die Verjährungseinrede wurde bis zum 15. Juni 2048 ausgeschlossen. Es ist dennoch kein unmittelbar vollstreckbarer Zahlungstitel über jede künftig benannte Summe.

Beweis: Anerkenntnis K3; historische Bestätigung K8 und Antwort K10. Einwendungen zur konkreten Schadenshöhe, zur Kausalität einzelner Ausgaben und zu übergegangenen Ansprüchen sind von der bereits anerkannten Haftung dem Grunde nach zu unterscheiden.

## 3. Geburtsverlauf und Folgen

Die Klägerin wurde am 14. Februar 2016 um 03:04 Uhr in der Klinik der Beklagten geboren. Der Dokumentationsauszug verzeichnet späte Dezelerationen ab 01:58 Uhr, die Kontaktaufnahme der Hebamme um 02:08 Uhr und eine ärztliche Untersuchung um 02:14 Uhr. Erst um 02:38 Uhr wurde die Sectio entschieden; um 02:42 Uhr erfolgte die OP-Alarmierung. Nach der Geburt bestand eine schwere Hypoxie mit dokumentiertem Nabelarterien-pH von 6,93 und Basendefizit von 18. Es folgten Reanimation, neonatologische Behandlung und Befunde einer hypoxisch-ischämischen Schädigung.

Beweis: Dokumentationsauszug K1. Für einen gerichtlichen Sachverständigen wären zusätzlich die vollständigen CTG-Aufzeichnungen, Kreißsaal-, OP- und Neonatologieunterlagen aus dem Klinikarchiv beizuziehen; der Auszug wird nicht als vollständige Ausgangsakte ausgegeben.

Die geburtshilfliche Beurteilung von Dr. Elin Rosenthal vom 23. April 2018 beruht nach ihrem Bericht auf den vollständigen damaligen Unterlagen. Danach hätte spätestens um 02:14 Uhr eine dringliche Entbindung veranlasst werden müssen; das Abwarten bis 02:38 Uhr war nicht gerechtfertigt. Sie bewertet den Zusammenhang zwischen Verzögerung und schwerer Schädigung als hoch wahrscheinlich und nennt keine andere wesentliche Ursache. Die abweichende Erinnerung an den Zeitpunkt einer Oberarztbenachrichtigung ändert ihre Bewertung des maßgeblichen Entscheidungszeitpunkts nicht.

Beweis: Gutachten K2; erforderlichenfalls geburtshilfliches Sachverständigengutachten unter Einbeziehung der vollständigen Dokumentation. Der Entwurf erklärt den Fehler nicht eigenständig zu einem bereits gerichtlich festgestellten groben Behandlungsfehler. Eine Beweislastumkehr wird nicht ohne Prüfung ihrer Voraussetzungen behauptet. Der medizinische Maßstab ist derjenige des Behandlungszeitpunkts 2016; spätere Leitlinien werden nicht rückwirkend zu damaligen Pflichten gemacht.

Der aktuelle sozialpädiatrische Bericht vom 11. Juni 2026 beschreibt eine schwere zerebrale Bewegungsstörung mit umfassendem Hilfebedarf bei Transfers, Selbstversorgung und Nahrungsaufnahme, Entwicklungsbeeinträchtigungen und Epilepsie. Die Klägerin benötigt Begleitung und kann zentrale Verrichtungen nicht selbständig ausführen. Wahrnehmungs- und Kontaktmöglichkeiten bestehen; die Schwere der Einschränkungen wird nicht dadurch aufgehoben. Die Eltern schildern einen durch Versorgung und Unterstützung bestimmten Tagesablauf. Zu einzelnen nächtlichen Verrichtungen beruhen die Angaben auf ihren Aufzeichnungen, nicht auf einer durchgehenden ärztlichen Beobachtung.

Beweis: Bericht K4; Elternnachricht K5. Für die individuelle Schmerzensgeldbemessung wird ergänzend neuropädiatrischer Sachverständigenbeweis zu Funktionsniveau, dauerhaften Beeinträchtigungen und vorhersehbaren Folgen angeboten. Eine genaue Lebenszeitprognose ist in den vorhandenen Unterlagen nicht enthalten und wird nicht erfunden.

## 4. Weiteres Schmerzensgeld

Der Anspruch ergibt sich aus der anerkannten Haftung sowie den vertraglichen und deliktischen Grundlagen, insbesondere §§ 630a, 280 Abs. 1, 278, 823 Abs. 1 und 253 Abs. 2 BGB. Soweit der Behandlungsvertrag mit der Mutter geschlossen wurde, ist die Einbeziehung des Kindes in dessen Schutzbereich zu berücksichtigen; daneben besteht der eigene deliktische Schutz seiner körperlichen Integrität. Die verbindliche Erklärung der Beklagten beseitigt hier die Notwendigkeit, einen allein aus der Rechtsform der Klinik abgeleiteten öffentlich-rechtlichen Haftungsweg zu konstruieren.

Die Klägerin hält angesichts der seit der Geburt bestehenden gravierenden und dauerhaften Beeinträchtigungen ein Gesamt-Schmerzensgeld von 900.000 EUR für angemessen und macht nach Abzug der gezahlten 300.000 EUR eine weitere Orientierung von 600.000 EUR geltend. Der Betrag wird nicht aus einem Vergleich mit einer anderen Person oder aus einer festen Tagessumme abgeleitet. Er ist ein begründungsbedürftiger Antrag an das Gericht, dessen Bemessungsermessen durch die Zahl nicht ersetzt wird.

Gewicht haben insbesondere der frühe Schadenseintritt, die alltagsprägende Abhängigkeit von Hilfe, der Verlust erheblicher Möglichkeiten selbstbestimmter Lebensgestaltung, körperliche Belastungen durch Behandlung und Versorgung sowie die Dauerhaftigkeit der wesentlichen Einschränkungen. Die Klägerin stützt sich dabei auf die konkreten Befunde. Sie behauptet keine lückenlos dokumentierten Schmerzen gleicher Intensität an jedem Tag und keine medizinisch gesicherte Restlebensdauer. Eine schematische Multiplikation eines Tagesbetrags mit angenommenen Lebensjahren wäre hierfür keine tragfähige Bemessung.

Die Gegenseite kann die Höhe trotz Anerkenntnisses überprüfen lassen. Zu berücksichtigen ist deshalb, dass die medizinischen Unterlagen noch sachverständig vertieft werden können und der genannte Gesamtbetrag nicht als unstreitig gelten darf. Die bereits lange geleistete Zahlung von 300.000 EUR wird in voller Höhe auf den immateriellen Gesamtanspruch angerechnet; sie wird weder als zusätzlicher Schaden noch als unberührte Pauschale neben einer neuen Vollentschädigung behandelt. Materielle Pflege- oder Bauzahlungen mindern das Schmerzensgeld nicht ohne entsprechende Zweckbestimmung.

## 5. Verbleibende Wohnanpassungskosten

Die Raumweg Bau GmbH stellte am 28. August 2026 für den am 12. Januar beauftragten und am 20. August abgenommenen Umbau 180.000 EUR brutto in Rechnung. Gegenstand waren der stufenlose Zugang, erforderliche Türanpassungen, das Pflegebad und die Vorbereitung eines Deckenlifts. Am 5. Februar wurden 100.000 EUR aus dem hierfür bestimmten Vorschuss bezahlt. Die restlichen 80.000 EUR wurden am 4. September von Noras Konto überwiesen. Die Rechnung ist damit vollständig bezahlt, der Schaden durch die Rechnungshöhe aber noch nicht in jeder rechtlichen Hinsicht abschließend bewertet.

Beweis: Rechnung einschließlich Zahlungsvermerken K6; Elternbestätigung K7; Zuordnungsbestätigung der Beklagten K8. Die Originalzahlungsbelege sind vor einer gerichtlichen Einreichung den Vermerken zuzuordnen und bei Bestreiten vorzulegen. Eine erst nach dem historischen Stichtag erstellte Gesamtabrechnung wird hierfür nicht verwendet.

Die Aufwendungen dienen der notwendigen Versorgung des verletzten Kindes und sind nach §§ 249, 843 Abs. 1 BGB als verletzungsbedingter Mehrbedarf zu prüfen. Das Haus gehört den Eltern. Das schließt einen auf die notwendige Nutzung für Nora gerichteten Aufwand nicht allein deshalb aus, erfordert aber die klare Trennung von kindbedingten Mehrkosten und allgemeiner Verbesserung des Elternvermögens. Nach K7 sind keine allgemeine Küchenmodernisierung, Terrasse oder Wohnraumerweiterung eingerechnet. Die einzelnen Arbeiten passen zu den in K4 belegten Transfer- und Versorgungsbedürfnissen.

Zur medizinischen und bautechnischen Erforderlichkeit der konkreten Anpassungen wird Sachverständigenbeweis angeboten. Ein etwaiger eigenständiger Vermögensvorteil, eine über das Notwendige hinausgehende Ausführung oder Leistungen eines anderen Kostenträgers sind konkret abzugrenzen. Der Entwurf leitet aus der Zahlung der Rechnung keine unwiderlegbare Erforderlichkeit ab. Die Klägerin und ihre Vertreter werden vorhandene Drittleistungsbescheide offenlegen. Ein Übergang nach den sozialrechtlichen Regeln darf nicht durch eine doppelte private Inanspruchnahme umgangen werden.

Die Klägerin ist insoweit private Endverbraucherin ohne Vorsteuerabzug. Die tatsächlich angefallene und bezahlte Umsatzsteuer ist Bestandteil des Aufwandes. Nach zweckbezogener Anrechnung der bereits hierfür verwendeten 100.000 EUR verbleiben die verlangten 80.000 EUR. Die zusätzlich gezahlten 800.000 EUR betrafen nach K8 andere bisherige materielle Mehrbedarfspositionen; sie werden nicht erneut als offener Schaden verlangt und nicht ohne Anlass ein zweites Mal auf dieselbe Wohnrechnung angerechnet.

## 6. Nicht erhobene Zukunftspositionen und Verfahrensstand

Aus dem Assistenzangebot und familiären Bildungsangaben wird in diesem Entwurf keine pauschale Millionenforderung kapitalisiert. Für laufend entstehenden künftigen Mehrbedarf sieht § 843 BGB grundsätzlich die wiederkehrende Leistung vor. Eine Kapitalabfindung nach § 843 Abs. 3 BGB verlangt einen wichtigen Grund; weder ein bloßer Rechenwunsch noch die Verwendung einer runden Verhandlungssumme ersetzt diese Voraussetzung. Ebenso fehlt eine belastbare individuelle Berechnung eines gesamten künftigen Erwerbsschadens. Diese Fragen sind hier nicht entscheidungsreif und bleiben außerhalb der beiden Zahlungsanträge.

Mit K9 wurde eine Reaktion bis zum 30. September erbeten. Am historischen Entwurfstag 22. September war diese Frist noch offen; die Antwort K10 enthielt keine verbindliche Einigung auf die geforderte Höhe. Vorgerichtlicher Verzug wird deshalb nicht fingiert. Die Anträge sehen ausschließlich Prozesszinsen nach §§ 291, 288 Abs. 1 Satz 2 BGB ab dem Tag nach einer erst noch möglichen Zustellung vor. Auch ein bereits entstandener Prozesskostenschaden wird nicht behauptet.

Dieser historische Entwurf hätte vor einer Einreichung die abschließende Entscheidung der gesetzlichen Vertreter, die vollständige Anlagenprüfung und die Abstimmung mit dem Stand der laufenden Vergleichsgespräche erfordert. Er erklärt weder die allgemeinen materiellen Rechte insgesamt für erledigt noch verlangt er bereits abgegoltene Positionen ein zweites Mal. Nach dem später eingetretenen, im Archivkopf erläuterten Vergleich und dessen Zahlung darf er tatsächlich nicht eingereicht werden.

Selim Berg
Rechtsanwalt – historischer, überholter Vorentwurf''','claim'),
]))

CASES.append(dict(
slug='akha-wuerzburg-betriebsfahrzeug',
claim_file='06_Klageentwurf_Hofbogen.docx',
notes='Klageentwurf vom 05.10.2026, nicht eingereicht. Klägerin ist allein die Gebäudeeigentümerin Hofbogen Immobilien GmbH, Beklagte sind Halterin und Fahrer. 145.000 EUR netto aus qualifiziertem, noch vorläufigem Bauangebot; fremde Geräte- und Umsatzansprüche bleiben getrennt. § 12 StVG und die deliktischen Anspruchsgrundlagen werden ausdrücklich getrennt geprüft. Das Anlagenverzeichnis wird aus exhibits angefügt.',
attachments={'03_Zeugin_Bestaetigung.eml':[]},
exhibits=[
K('K1','02_Unfallmeldung.docx','Rollen, Fahrzeugdaten und Unfallablauf'),
K('K2','03_Zeugin_Samira.docx','Unabhängige Beobachtung und Fahrzeugkorrektur'),
K('K3','11_Fuhrparkchat.txt','Zeitnahe Fahrermeldung und Unsicherheit zur Bremse'),
K('K4','06_Werkstattauftrag.docx','Gesicherter Prüfzustand und noch ausstehender Befund'),
K('K5','07_Gebaeudeeigentuemerin.eml','Eigentum, Forderung und Vorsteuerabzug'),
K('K6','04_Bau_Angebot.docx','Drei konkret bezeichnete Baupositionen'),
K('K7','schriftverkehr-und-klage/01_Bauangebot_Erlaeuterung.eml','Grundlagen, Begrenzung und vorläufiger Charakter der Kalkulation'),
K('K8','schriftverkehr-und-klage/02_Auftrag_und_Rollen.eml','Privater Reinigungsauftrag, Halterin und Fahreranschrift'),
K('K9','schriftverkehr-und-klage/03_Zeugin_Bestaetigung.eml','Sichtbarer Fahrzeuglauf und Ladungsanschrift'),
K('K10','schriftverkehr-und-klage/04_Forderung_Hofbogen.pdf','Gebäudeforderung gegen Halterin und Fahrer'),
K('K11','schriftverkehr-und-klage/05_Antwort_Stadtbetriebe.pdf','Offene Technik- und Höhenfragen, mehrere Geschädigte'),
K('K12','05_Geraete_Aufstellung.docx','Nur für Höchstbetragsfrage: ausdrücklich ungeprüfte fremde Anmeldung'),
],
documents=[
D('01_Bauangebot_Erlaeuterung.eml','HB-260929: Grundlagen und offene Punkte','2026-10-02T10:16:00+02:00', '''Sehr geehrte Frau Knopf,

ich erläutere unser Angebot vom 29. September. Das Torblatt war nach dem Anstoß sichtbar verwunden, die seitliche Führung aus ihrer Verankerung gezogen. Unsere Besichtigung am 28. September ergab keine fachgerechte Möglichkeit, das vorhandene Blatt nur zurückzubiegen. Die 68.000 EUR betreffen ein Tor vergleichbarer Abmessungen und Sicherheitsausstattung einschließlich Ausbau und Entsorgung, keine Vergrößerung oder leistungsfähigere Neuanlage. Die 52.000 EUR betreffen die sichtbar gerissenen Anschlüsse, den Sturzbereich und das Mauerwerk unmittelbar am Tor. Die 25.000 EUR erfassen die für diese Arbeiten kalkulierte Baustelleneinrichtung, Hebetechnik und den vorübergehenden Verschluss.

Das bleibt eine vorläufige Baukalkulation. Ob verdeckte Schäden einen anderen Umfang verlangen, lässt sich erst nach statischer Untersuchung und Öffnung beurteilen. Eine statische Freigabe bescheinige ich nicht. Auch eine abschließende Bewertung möglicher Gebrauchsvorteile durch das neue Tor war nicht unser Auftrag. Die bezeichneten Arbeiten sollen den vorherigen Funktionszustand wiederherstellen. Ausstattung der Mieterin und Mietausfälle haben wir nicht eingerechnet; die bisherige Sicherung wird nicht ein zweites Mal als eigener Rechnungsbetrag verlangt.

Sie haben den vollständigen Bauauftrag noch nicht erteilt. Eine kurzfristige gemeinsame Besichtigung mit der Gegenseite ist möglich. Bitte erhalten Sie Tor und ausgebrochene Teile bis zur dokumentierten Begutachtung. Ich kann die sichtbaren Befunde und die Kalkulationsgrundlagen als Zeuge erläutern; eine unabhängige Begutachtung wird dadurch nicht ersetzt.

Mit freundlichen Grüßen
Balduin Balken
Baukontor Balduin Balken GmbH, Werkplatz 8, 97076 Würzburg''','email','Balduin Balken <angebot@balken-bau.example>','Kunigunde Knopf <kunigunde@hofbogen-immobilien.example>'),
D('02_Auftrag_und_Rollen.eml','Hallenbogen: Reinigungsauftrag und Beteiligte','2026-10-02T14:36:00+02:00', '''Sehr geehrte Frau Knopf,

für die weitere Korrespondenz bestätige ich: Die Stadtbetriebe Steinbogen GmbH, Betriebshof Laubenring 9, 97076 Würzburg, ist Halterin und Eigentümerin der Kehrmaschine Nummer 7. Unsere Geschäftsführerin ist Hedwig Sommer. Herr Burkhard Blech, Werkzeugpfad 5, 97076 Würzburg, war am 25. September unser angestellter Fahrer und führte den ihm übertragenen Reinigungsauftrag aus.

Der konkrete Auftrag betraf die Reinigung des privaten Gewerbehofs Hallenbogen 12 auf Grundlage Ihrer privatrechtlichen Bestellung. Es handelte sich nicht um eine öffentlich gewidmete Straße oder eine hoheitliche Straßenreinigungsmaßnahme. Dass Lieferverkehr tagsüber ohne Zugangskontrolle hineinfährt, ändert den Auftragsinhalt nicht. Eine besondere hoheitliche Weisung wurde Herrn Blech nicht erteilt.

Die Fahrzeugkarte weist 40 km/h bauartbedingte Höchstgeschwindigkeit aus. Die Maschine verfügt weder über eine automatisierte Fahrfunktion nach § 1a StVG noch über eine autonome Fahrfunktion nach § 1e StVG. Die technische Untersuchung der Feststellbremse ist noch offen; der angekündigte vollständige Werkstattbericht wird erst für den 8. Oktober erwartet. Aus dem fehlenden Wartungsblatt im Fahrzeugordner schließen wir bislang weder eine ausgefallene Wartung noch einen technischen Defekt. Bitte werten Sie diese Tatsachenbestätigung nicht als Anerkenntnis sämtlicher Schadenspositionen.

Mit freundlichen Grüßen
Hedwig Hummel
Fuhrparkleitung · Stadtbetriebe Steinbogen GmbH''','email','Hedwig Hummel <fuhrpark@steinbogen-betriebe.example>','Kunigunde Knopf <kunigunde@hofbogen-immobilien.example>'),
D('03_Zeugin_Bestaetigung.eml','Beobachtung am 25. September und meine Anschrift','2026-10-03T15:08:00+02:00', '''Sehr geehrte Frau Knopf,

Sie dürfen meine schriftliche Schilderung vom 28. September verwenden. Meine ladungsfähige Anschrift lautet Samira Schwan, Kurierdienst Schwan, Paketsteg 4, 97076 Würzburg. Ich sah die Maschine einige Sekunden stehen, dann den Fahrer aussteigen und zur Bake gehen. Danach rollte sie ohne Fahrer gegen das Tor. Einen weiteren Anstoß durch ein anderes Fahrzeug oder einen Menschen habe ich nicht gesehen. Die Bedienung des Bremshebels konnte ich weiterhin nicht erkennen.

Das Tor war beim Eintreffen geschlossen. Es wurde durch den Aufprall nach innen gedrückt. Vorher habe ich das Mauerwerk nicht gezielt untersucht; ich kann daher keinen fachlichen Vergleich aller alten und neuen Risse anbieten. Meine erste Bezeichnung als Lieferwagen war falsch, wie ich bereits erläutert habe. Ich habe keine Kenntnis über den Wert der Geräte hinter dem Tor und kann aus den sichtbaren Kisten keine vollständigen Totalschäden ableiten.

Eine Erklärung, dass sämtliche angemeldeten Kosten stimmen, möchte ich nicht unterschreiben. Für meine eigenen Beobachtungen stehe ich zur Verfügung.

Mit freundlichen Grüßen
Samira Schwan''','email','Samira Schwan <samira@schwan-kurier.example>','Kunigunde Knopf <kunigunde@hofbogen-immobilien.example>'),
D('04_Forderung_Hofbogen.docx','Hallentor: Forderung der Gebäudeeigentümerin','04.10.2026', '''Rechtsanwalt Nils Feder
Mainblattweg 6, 97070 Würzburg

An die Stadtbetriebe Steinbogen GmbH
z. H. Geschäftsführerin Hedwig Sommer
Betriebshof Laubenring 9, 97076 Würzburg
Zugleich an Herrn Burkhard Blech, Werkzeugpfad 5, 97076 Würzburg

Sehr geehrte Frau Sommer, sehr geehrter Herr Blech,

ich vertrete ausschließlich die Hofbogen Immobilien GmbH, vertreten durch Frau Kunigunde Knopf, Hallenbogen 12, 97076 Würzburg. Sie verlangt 145.000 EUR netto für die Beschädigung ihres Hallentors und angrenzender Bauteile durch die am 25. September abgestellte und anschließend weggerollte Kehrmaschine. Bitte regulieren Sie die berechtigte Forderung bis zum 19. Oktober 2026 oder benennen Sie bis zum 12. Oktober Ihre konkreten Einwendungen und einen Termin für die gemeinsame technische Aufnahme.

Die Halterhaftung nach § 7 StVG und die Fahrerhaftung nach § 18 StVG sind neben den schuldabhängigen Ansprüchen zu prüfen. Der private Reinigungsauftrag und das ausgeschaltete Kehraggregat sprechen hier für den verwirklichten Fortbewegungsvorgang. Herr Blech hat das Fahrzeug bei laufendem Motor auf leichtem Gefälle verlassen und kann nicht bestätigen, dass die Feststellbremse vollständig eingerastet war. Einen technisch abschließend festgestellten Bremsdefekt behauptet meine Mandantin nicht.

Der Gebäudebetrag beruht auf dem vorläufigen Angebot des Baukontors Balken. Die drei Positionen sind separat bezeichnet; die statische Prüfung und die Untersuchung verdeckter Schäden bleiben offen. Umsatzsteuer wird nicht verlangt. Bitte erhalten Sie Ihrerseits die Maschine einschließlich Bremse und Wartungsunterlagen. Die Gebäudeeigentümerin wird die beschädigten Teile bis zur abgestimmten Aufnahme erhalten, soweit die Verkehrssicherheit dies zulässt.

Fremde Veranstaltungstechnik gehört nicht meiner Mandantin. Weder die Anmeldung der Prisma GmbH noch der von Nuri Nudelwerk genannte Umsatz wird in diesen Anspruch eingerechnet. § 12 StVG verlangt bei mehreren berechtigten Sachschadenansprüchen gegebenenfalls eine gesonderte Höchstbetragsprüfung. Daraus darf keine Kürzung allein anhand ungeprüfter Neupreislisten abgeleitet werden. Schuldhaft begründete Ansprüche außerhalb des StVG bleiben nach § 16 StVG gesondert zu prüfen.

Dieses Schreiben ist eine außergerichtliche Forderung, keine Klageeinreichung. Einen Auftrag für die Versicherung oder die Gegenseite habe ich nicht.

Mit freundlichen Grüßen
Nils Feder
Rechtsanwalt''','letter'),
D('05_Antwort_Stadtbetriebe.docx','Hallenbogen: gemeinsame Besichtigung und offene Schadenhöhe','05.10.2026', '''Stadtbetriebe Steinbogen GmbH
Betriebshof Laubenring 9, 97076 Würzburg

An Rechtsanwalt Nils Feder
Mainblattweg 6, 97070 Würzburg

Sehr geehrter Herr Feder,

wir bestätigen den Eingang der Gebäudeforderung und die durch Frau Hummel mitgeteilten Rollen. Der Fahrer Herr Blech ist über Ihre Inanspruchnahme informiert. Die Haftungs- und Deckungsprüfung dauert an. Unsere Gesellschaft und Herr Blech erklären mit dieser Antwort kein Anerkenntnis. Herr Blech hat die im Unfallbericht beschriebene Unsicherheit zur vollständig eingerasteten Bremse nicht zurückgenommen; ein fertiger Werkstattbefund liegt heute nicht vor.

Die Höhe von 145.000 EUR ist aus unserer Sicht noch durch einen unabhängigen Sachverständigen zu prüfen. Insbesondere interessieren uns die Erforderlichkeit des vollständigen Toraustauschs, der Umfang bereits vorhandener Schäden, eine mögliche Verbesserung und die Abgrenzung zwischen vorübergehender Sicherung und endgültiger Wiederherstellung. Wir begrüßen deshalb eine gemeinsame Besichtigung. Die Maschine bleibt gesichert. Das fehlende Wartungsblatt suchen wir weiter; Aussagen über den genauen Wartungsverlauf können wir derzeit nicht abschließend treffen.

Daneben hat Prisma eine vorläufige Geräteforderung über 1.650.000 EUR und der Nachbarbetrieb eine Umsatzposition angemeldet. Diese Beträge sind nicht als festgestellte Entschädigungen anerkannt. Wir behalten uns die Prüfung der gesetzlichen Haftungsgrenzen und sämtlicher Anspruchsvoraussetzungen vor. Eine konkrete anteilige Kürzung Ihrer Forderung haben wir noch nicht berechnet. Der Vertragseintrag bei Frankenbogen ersetzt für die Deckung keine vollständige Police.

Bitte übersenden Sie einen Terminvorschlag. Eine Zahlung bis zur von Ihnen gesetzten Frist können wir heute noch nicht zusagen. Diese Nachricht ist keine Prozessvollmacht für Ihre Kanzlei und bestätigt keine bereits erfolgte gerichtliche Inanspruchnahme.

Mit freundlichen Grüßen
Mira Morgenrot
Rechtsabteilung''','letter'),
D('06_Klageentwurf_Hofbogen.docx','Klageentwurf der Gebäudeeigentümerin','05.10.2026', '''ENTWURF VOM 5. OKTOBER 2026 – NICHT EINGEREICHT
Gegenstand allein: Schäden der Hofbogen Immobilien GmbH an Tor und Gebäude.

An das Landgericht Würzburg
Ottostraße 5
97070 Würzburg

Hofbogen Immobilien GmbH, Hallenbogen 12, 97076 Würzburg, vertreten durch ihre Geschäftsführerin Kunigunde Knopf,
– Klägerin –
Prozessbevollmächtigter: Rechtsanwalt Nils Feder, Mainblattweg 6, 97070 Würzburg,

gegen

1. Stadtbetriebe Steinbogen GmbH, Betriebshof Laubenring 9, 97076 Würzburg, vertreten durch ihre Geschäftsführerin Hedwig Sommer,
2. Burkhard Blech, Werkzeugpfad 5, 97076 Würzburg,
– Beklagte –

wegen Gebäudeschäden durch eine wegrollende Kehrmaschine.
Vorläufiger Streitwert: 145.000,00 EUR.

## 1. Anträge und Abgrenzung

Für eine spätere Einreichung wird beantragt,

1. die Beklagten als Gesamtschuldner zu verurteilen, an die Klägerin 145.000,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach der jeweiligen Klagezustellung zu zahlen;
2. den Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Die Klägerin verlangt ausschließlich den für die Wiederherstellung ihres Hallentors, Sturzbereichs und unmittelbar angrenzenden Mauerwerks einschließlich notwendiger Baustelleneinrichtung, Hebetechnik und vorübergehenden Verschlusses angesetzten Nettobetrag. Das Angebot weist diese Positionen mit 68.000 EUR, 52.000 EUR und 25.000 EUR gesondert aus. Umsatzsteuer ist nicht Gegenstand des Begehrens.

Die hinter dem Tor abgestellte Veranstaltungstechnik gehört der Prisma Bühnenbildtechnik GmbH. Deren Ansprüche werden weder in Prozessstandschaft noch aus abgetretenem Recht erhoben. Auch der gemeldete Umsatzverlust der Nuri Nudelwerk GmbH, etwaige Mietausfälle der Klägerin und gegenwärtig nicht bewertete verdeckte Schäden sind nicht Teil der Zahlungsklage. Eine spätere Berechnung weiterer eigener Schäden müsste Überschneidungen mit den hier erfassten Positionen ausschließen. Aus dem Umfang der gegenwärtigen Forderung folgt kein Verzicht auf solche anderen eigenen Ansprüche.

## 2. Zuständigkeit und Anspruchsgegner

Das Landgericht ist nach § 71 Abs. 1 GVG sachlich zuständig. Die Forderung übersteigt die seit 2026 maßgebliche allgemeine Grenze des § 23 Nr. 1 GVG von 10.000 EUR. Beide Beklagten haben ihren Sitz beziehungsweise Wohnsitz im Gerichtsbezirk; auch der Unfall ereignete sich in Würzburg. Die örtliche Zuständigkeit folgt aus §§ 12, 13 und 17 ZPO, ergänzend aus § 32 ZPO. Die gemeinsame Inanspruchnahme beruht auf demselben Unfall und ist nach §§ 59, 60 ZPO zulässig.

Die Beklagte zu 1 war Halterin und Eigentümerin der Kehrmaschine, der Beklagte zu 2 ihr angestellter Fahrer. Der konkrete Auftrag beruhte auf einer privaten Bestellung zur Reinigung des Gewerbehofs. Eine öffentlich gewidmete Straße, hoheitliche Straßenreinigung oder eine entsprechende besondere Weisung lag nicht vor. Die öffentliche Zugänglichkeit während des Lieferverkehrs ist davon zu unterscheiden. Eine Haftungsüberleitung nach Art. 34 GG wird nicht allein aus dem Namen Stadtbetriebe abgeleitet; der Fahrer wird hier persönlich wegen privaten Handelns in Anspruch genommen.

Beweis: Betriebsbestätigung K8; Unfallmeldung K1. Die Klägerin ist selbst Gebäudeeigentümerin; ihre Geschäftsführerin hat dies bereits in K5 bestätigt. Bei substantiiertem Bestreiten wird der zugehörige Eigentumsnachweis vorzulegen sein. Ein Versicherer wird in diesem Entwurf nicht verklagt, da die vollständigen Vertragsunterlagen noch fehlen und es für die gewählte Anspruchsverfolgung hierauf nicht ankommt.

## 3. Unfallablauf und Beweisangebot

Am 25. September 2026 gegen 09:14 Uhr hielt der Beklagte zu 2 die Kehrmaschine Nummer 7 einige Meter vor dem Hallentor an, um eine umgefallene Absperrbake zu entfernen. Der Motor lief weiter, das Kehraggregat war ausgeschaltet. Er verließ die Maschine. Wenige Sekunden später rollte sie auf dem leichten Gefälle vorwärts, traf das geschlossene Tor und drückte es nach innen. Dabei wurden das Tor und angrenzende Bauteile beschädigt; dahinterstehende Gestelle wurden verschoben.

Beweis: Unfallmeldung K1; Zeugnis der Samira Schwan, Paketsteg 4, 97076 Würzburg, deren schriftliche Beobachtungen K2 und K9 wiedergeben; Fuhrparkchat K3. Die Zeugin sah keinen weiteren äußeren Anstoß. Ihre anfängliche ungenaue Bezeichnung als Lieferwagen ist berichtigt. Sie erkannte die seitlichen Bürsten und den Schriftzug der Stadtbetriebe. Ihre Wahrnehmung wird nicht um eine von ihr gerade nicht beobachtete Bedienung des Bremshebels ergänzt.

Der Beklagte zu 2 erklärte selbst, er glaube den Hebel angezogen zu haben, könne aber ein vollständiges Einrasten nicht sicher bestätigen. Im zeitnahen Chat um 09:31 Uhr wiederholte er diese Unsicherheit. Er hatte das leichte Gefälle unterschätzt. Die Klägerin behauptet, dass das Fahrzeug vor dem Aussteigen nicht wirksam gegen das absehbare Wegrollen gesichert war. Sie stützt dies auf den unbeaufsichtigten Rollvorgang, die Fahrererklärung und den fehlenden äußeren Anstoß. Eine vorsätzliche Handlung wird nicht behauptet.

Die technische Untersuchung ist noch nicht abgeschlossen. Der Werkstattauftrag K4 sieht die Dokumentation von Stellung, Funktion und Betätigungskräften der Feststellbremse sowie des Wartungsstands vor. Das Fahrzeug bleibt gesichert; der vollständige Bericht wird erst für den 8. Oktober erwartet. Das bloße Fehlen eines unterschriebenen Wartungsblatts im Ordner beweist noch nicht, dass keine Wartung stattfand. Umgekehrt wird ein unerkannter technischer Defekt nicht ohne Befund als feststehende Entlastung behandelt.

Zum Zustand der Bremse, der erforderlichen Sicherung auf dem vorhandenen Gefälle und zur technischen Vereinbarkeit der behaupteten Bremsbetätigung mit dem Wegrollen wird Sachverständigenbeweis angeboten. Die Beklagten werden um Vorlage des Berichts und der vorhandenen Wartungsunterlagen gebeten; bei Bedarf kommt eine gerichtliche Vorlageanordnung nach § 142 ZPO in Betracht. Ein bereits angefertigtes Gutachten oder sein Ergebnis wird nicht vorweggenommen.

## 4. Gesetzliche Haftungsgrundlagen

Die Beklagte zu 1 haftet als Halterin nach § 7 Abs. 1 StVG. Das Schadenereignis entstand bei dem Betrieb des Fahrzeugs: Die ungesicherte Bewegung der Maschine verwirklichte deren Fortbewegungsrisiko unmittelbar im Anprall. Dass das Kehraggregat ausgeschaltet war, entfernt diesen Vorgang nicht aus dem Fahrzeugbetrieb. Die Einordnung folgt aus dem konkreten Ablauf und nicht daraus, dass jedes Gerät mit Motor stets dem StVG unterfiele. Die bauartbedingte Höchstgeschwindigkeit beträgt 40 km/h; die Ausnahme des § 8 Nr. 1 StVG für Fahrzeuge bis 20 km/h greift deshalb nicht ein. Hinweise auf höhere Gewalt fehlen.

Der Beklagte zu 2 ist als Fahrzeugführer nach § 18 Abs. 1 StVG verantwortlich, sofern er den gesetzlich vorgesehenen Entlastungsbeweis nicht führt. Darüber hinaus wird er nach § 823 Abs. 1 BGB wegen der schuldhaften Beschädigung des klägerischen Eigentums in Anspruch genommen. Wer ein Fahrzeug bei laufendem Motor auf einem Gefälle verlässt, muss seine wirksame Sicherung gewährleisten. Die Klägerin legt für die Verschuldenshaftung den fehlenden Sicherungserfolg und die konkreten Fahrererklärungen vor; sie verwechselt die Beweislastregel des § 18 StVG nicht mit einer automatisch inhaltsgleichen Regel für jeden deliktischen Anspruch.

Ein allein technisch verursachtes Versagen trotz nachweislich ordnungsgemäßer Sicherung könnte für die persönliche Verschuldensbewertung erheblich werden. Hierzu liegt noch kein Befund vor. Auf eine solche konkrete Einwendung wäre anhand der Untersuchung einzugehen. Die gegenwärtige Unsicherheit rechtfertigt weder die Behauptung eines sicheren Bremsdefekts noch das Weglassen des persönlichen Fehlverhaltens als ernsthaft belegter Anspruchsgrundlage.

Die Beklagte zu 1 haftet daneben nach § 831 Abs. 1 BGB, sofern sie den dort geregelten Entlastungsbeweis nicht führt. Der Fahrer war ihr weisungsabhängiger Beschäftigter und handelte in Ausführung des übertragenen Reinigungsauftrags. Das Anhalten und Beseitigen der Bake standen in diesem Zusammenhang. Eine eigene schuldhafte Organisation der Geschäftsführung wird dagegen nicht aus dem Unternehmensnamen oder dem Unfall allein gefolgert. Für Auswahl, Unterweisung, Überwachung und die maßgeblichen Umstände der Fahrzeugbereitstellung sind konkrete Tatsachen erforderlich. Die Beklagte kann hierzu vortragen und ihre Entlastung beweisen. Die Anspruchsgrundlage wird nicht als verschuldensunabhängige Garantie der Arbeitgeberin dargestellt.

Darüber hinaus besteht zwischen der Klägerin als Bestellerin und der Beklagten zu 1 ein privater Reinigungsvertrag; die Beklagte bestätigt gerade den auf dieser Bestellung beruhenden Hofeinsatz in K8. Bei dessen Ausführung musste sie nach § 241 Abs. 2 BGB das Eigentum ihrer Auftraggeberin vor vermeidbaren Beschädigungen schützen. Der Fahrer war zur Erfüllung dieser Verpflichtungen eingesetzt. Sein Verschulden wird ihr nach § 278 BGB zugerechnet; eine Entlastung allein durch sorgfältige Auswahl nach § 831 BGB beseitigt diesen vertraglichen Anspruch aus § 280 Abs. 1 BGB nicht. Der Anprall erfolgte während der vertraglichen Tätigkeit, nicht bei einer rein privaten Gelegenheit. Auch hier bleiben Pflichtverletzung und Ursächlichkeit konkret nachzuweisen; hinsichtlich des Vertretenmüssens gilt § 280 Abs. 1 Satz 2 BGB. Die Vertragsforderung steht nur der Klägerin als Auftraggeberin zu und wird nicht auf die fremden Geräte- oder Umsatzansprüche ausgedehnt.

Soweit beide Beklagte haften, wird dieselbe Wiederherstellungsleistung nur einmal verlangt. Die gesamtschuldnerische Verknüpfung ergibt sich aus den einschlägigen gesetzlichen Vorschriften, insbesondere § 840 BGB beziehungsweise § 421 BGB. Die Klägerin verlangt keine Addition einer Fahrzeug- und einer Deliktsentschädigung.

## 5. Haftungshöchstbetrag und weitere Geschädigte

Die Haftung nach dem StVG ist für Sachschäden nach § 12 Abs. 1 Satz 1 Nr. 2 StVG grundsätzlich auf insgesamt eine Million EUR je Ereignis begrenzt. Für die vorliegende Maschine bestehen weder eine automatisierte Fahrfunktion nach § 1a StVG noch eine autonome Fahrfunktion nach § 1e StVG; K8 bestätigt dies. Die erhöhte Grenze für diese besondere Betriebsart wird daher nicht verwendet.

Die alleinige Gebäudeforderung liegt zwar unter einer Million EUR. Daneben ist aber die fremde Geräteanmeldung der Prisma GmbH bekannt. Sollten die insgesamt begründeten Entschädigungen die gesetzliche Grenze überschreiten, ist die Verhältnisregel des § 12 Abs. 2 StVG zu berücksichtigen. Eine bloße Anmeldung von 1,65 Millionen EUR zum Neupreis gebrauchter, noch nicht vollständig untersuchter Geräte liefert keine fertige Verteilungsquote. K12 wird deshalb nur zum Nachweis dieser offenen Mehrgeschädigtenfrage vorgelegt, nicht als Beleg eines abschließend berechtigten Geräteanspruchs. Auch ein gemeldeter reiner Umsatzausfall ist nicht ohne Prüfung eine ersatzfähige Sachschadenposition.

Die Klägerin hält an der vollen Forderung fest und stützt sie zusätzlich auf die bezeichneten schuldabhängigen Ansprüche einschließlich der vertraglichen Haftung der Beklagten zu 1. § 16 StVG lässt die weitergehende Haftung nach anderen Vorschriften unberührt. Diese Anspruchsgrundlagen dürfen nicht durch einen pauschalen Verweis auf § 12 StVG abgeschnitten werden; sie müssen aber einschließlich ihres Verschuldensnachweises beziehungsweise ihrer jeweils unterschiedlichen Entlastungsmöglichkeit eigenständig tragfähig sein. Sollte nur die StVG-Haftung durchgreifen und eine Überschreitung durch weitere begründete Forderungen feststehen, wäre eine gesetzliche Kürzung zu berücksichtigen. Der Entwurf verschweigt diese Grenze des vollen Zahlungsbegehrens nicht.

## 6. Wiederherstellungskosten und Gegenargumente

Das Baukontor Balken besichtigte den Schaden am 28. September und kalkulierte am Folgetag 145.000 EUR netto. Das Torblatt war verwunden, eine Führung aus der Verankerung gezogen; Sturzbereich und Maueranschlüsse zeigten Schäden. Die Erläuterung K7 beschreibt den Ersatz durch ein vergleichbares Tor ohne Vergrößerung oder zusätzliche Leistungsmerkmale. Die drei Leistungsgruppen sind einzeln benannt und grenzen Mieterausstattung sowie Mietausfälle aus.

Beweis: Angebot K6; Erläuterung K7; Zeugnis des Balduin Balken, Werkplatz 8, 97076 Würzburg. Zum unfallbedingten Reparaturumfang, zur technischen Erforderlichkeit des Austauschs, zu marktüblichen Kosten und etwaigen anzurechnenden Vorteilen wird ein bautechnisches Sachverständigengutachten angeboten. Die Klägerin wird eine Besichtigung ermöglichen und gefährdete Teile vor Veränderung dokumentieren lassen.

Nach § 249 Abs. 2 Satz 1 BGB kann der zur Wiederherstellung erforderliche Geldbetrag auch vor Durchführung der Reparatur verlangt werden. Dass der Auftrag wegen der ausstehenden Statik noch nicht erteilt wurde, schließt einen solchen Anspruch nicht von vornherein aus. Das Angebot bindet das Gericht jedoch nicht. Es ist eine konkrete Schätz- und Begutachtungsgrundlage; ungeklärte verdeckte Schäden sind darin nicht bewertet. Ergibt die Untersuchung einen geringeren erforderlichen Aufwand oder einen messbaren Vorteil, ist die Forderung entsprechend anzupassen.

Die Klägerin ist zum Vorsteuerabzug berechtigt. Unabhängig davon wird eine noch nicht angefallene Umsatzsteuer bei der derzeitigen Berechnung nicht verlangt. Der Bruttobetrag von 172.550 EUR ist deshalb kein Klagebetrag. Bisherige Sicherungsarbeiten werden nicht nochmals separat addiert. Ebenso wenig werden die hinter dem Tor sichtbaren Kisten als Eigentum der Klägerin behandelt.

Konkrete Anhaltspunkte für ein Mitverschulden der Klägerin nach § 254 BGB fehlen bisher. Die Bereitstellung eines geschlossenen Hallentors und das Lagern von Gegenständen dahinter sind nicht allein pflichtwidrig. Sollten Vorschäden behauptet werden, sind Ort, Art und Einfluss auf die erforderliche Reparatur abzugrenzen; die Zeugin Schwan behauptet ausdrücklich keine fachliche Prüfung des vorherigen Zustands. Eine Betriebsgefahr eines eigenen am Unfall beteiligten Kraftfahrzeugs der Klägerin besteht nicht. Eine pauschale Quote nach § 17 StVG wird daher nicht abgezogen.

## 7. Zinsen, außergerichtlicher Stand und Einreichungsvorbehalt

Die Forderung wurde mit K10 gegenüber beiden Beklagten präzisiert. Die Zahlungsfrist bis zum 19. Oktober ist bei Erstellung dieses Entwurfs noch nicht abgelaufen. K11 bestätigt die noch laufende Prüfung, ohne Zahlung oder Haftung anzuerkennen. Vorgerichtlicher Verzug wird nicht fingiert. Beantragt werden nur Prozesszinsen nach §§ 291, 288 Abs. 1 Satz 2 BGB, jeweils ab dem Tag nach Zustellung an den betreffenden Beklagten. Fünf Prozentpunkte sind maßgeblich; die Schadenersatzforderung ist keine vertragliche Entgeltforderung, für die allein wegen der beteiligten Gesellschaften neun Prozentpunkte verlangt werden könnten.

Vor einer Einreichung sollen der angekündigte technische Befund und die bautechnische Aufnahme ausgewertet, die Eigentums- und Vertretungsnachweise vervollständigt und die Fortentwicklung der Mehrgeschädigtenlage geprüft werden. Die offenen Punkte werden im Entwurf bewusst offengelegt. Eine tatsächlich erteilte Einreichungsvollmacht, ein gerichtliches Aktenzeichen oder ein bereits bestimmter Termin werden nicht behauptet.

Nils Feder
Rechtsanwalt – Entwurf ohne Einreichung''','claim'),
]))
