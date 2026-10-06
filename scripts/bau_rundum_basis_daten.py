"""Individuell verfasste Originalunterlagen für fünf Bauwirtschaft-Einstiegsakten."""


def dokument(datei, titel, absender, empfaenger, datum, zeichen, *seiten):
    return dict(datei=datei, titel=titel, absender=absender, empfaenger=empfaenger,
                datum=datum, zeichen=zeichen, seiten=seiten)


def mail(datei, absender, empfaenger, datum, betreff, text, antwort=None):
    return dict(datei=datei, absender=absender, empfaenger=empfaenger, datum=datum,
                betreff=betreff, text=text, antwort=antwort)


def tabelle(kopf, zeilen, breiten):
    return dict(kopf=kopf, zeilen=zeilen, breiten=breiten)


AKTEN = {
    "bau-rundum-begehung-einbeck": {
        "titel": "Begehung des Nachbarschaftshauses Kieselgarten in Einbeck",
        "stand": "2026-09-23",
        "beschreibung": "Begehungsmemo, Randnotizen, Messwerte und zwei illustrierte Befundskizzen zu Ausbauarbeiten; getrennte Vertrags- und Abnahmestände der beteiligten Gewerke.",
        "dokumente": [
            dokument("02_Begehungsmemo.docx", "Begehungsmemo Kieselgarten", "Maren Döring | Bauüberwachung Döring und Stettner", "Projektablage KG 26 | Heike Lenz", "22.09.2026, 12:10 Uhr", "KG-26 / BM-09 / Fassung 1",
                """1 Rundgang am 22 September

Ich war von 09:05 bis 10:35 Uhr im Nachbarschaftshaus Kieselgarten, Kieselgartenweg 14, 37574 Einbeck. Heike Lenz vom Verein war durchgehend dabei. Jonas Falk von Leineputz kam um 09:25 Uhr hinzu und ging um 10:05 Uhr. Nils Bödeker von Elektro Faden war von 09:50 bis 10:20 Uhr anwesend. Weder Glaserei Fenstertreu noch Sanitärbetrieb Quellwerk waren vertreten. Das Haus war für Besucher geschlossen; im Erdgeschoss arbeiteten zwei Maler.

Wir begannen im Mehrzweckraum 0.03. Links neben Tür T03 verläuft ein schräger Riss von der oberen linken Zargenecke in Richtung Fenster. Ich habe drei Stellen mit der Risskarte verglichen. Die größte abgelesene Breite lag bei etwa 0,4 mm, nicht bei 4 mm, wie es mein erster Zuruf gewesen sein könnte. Die Linie war rund 62 cm lang. Ob nur der Anstrich oder auch der Putz betroffen ist, haben wir nicht geöffnet. Herr Falk vermutet Bewegung im Anschluss; Frau Lenz sagte, die Linie sei am Freitag noch nicht aufgefallen.

2 Fenster und Tür im Erdgeschoss

Am Ostfenster F07 in Raum 0.03 ist das untere innere Anschlussband auf ungefähr 18 cm nicht mit dem Putz verbunden. Der sichtbare Spalt liegt zwischen Band und Laibung, nicht zwischen Flügel und Rahmen. Bei geschlossenem Fenster habe ich mit dem Handrücken einen Luftzug zu spüren geglaubt; eine Messung fand nicht statt. Ich habe hierfür die Skizze SK-01 angefertigt. Die Zuständigkeit am Anschluss haben Falk und Lenz unterschiedlich beschrieben. Die Glaserei hat laut Lenz das Band eingebaut, Leineputz den Anschluss überspachtelt.

Tür T05 zum Abstellraum streifte bei vier von fünf Öffnungen am Boden. Der Boden war trocken und frei von Verpackung. Auf der Bandseite beträgt der sichtbare Luftspalt unten ungefähr 3 mm, gegenüber weniger als 1 mm. Ich habe weder an Bändern noch am Türschließer gedreht. Die Tür ist kein ausgewiesener Rettungswegausgang. Der Planstand in meiner Mappe war KG-A-12/03 vom 08.09.2026.

Aufgezeichnet von Maren Döring am 22.09.2026 nach dem Rundgang. Die Reihenfolge folgt meinem Weg, nicht den Firmenverträgen.""",
                """3 Waschraum und Beleuchtung

Im Waschraum 0.06 blieb am Bodenablauf eine kleine Wasserfläche stehen. Frau Lenz hatte um 09:30 Uhr etwa zwei Liter Leitungswasser aus einem Messbecher ausgegossen. Um 09:38 Uhr stand neben dem Rost noch Wasser, maximal etwa 4 mm tief nach unserem Zollstock. Wir haben kein Raster nivelliert. Die Fuge an der Nordwand war trocken. Die Fläche wurde danach aufgenommen, damit niemand ausrutscht. Meine Skizze SK-02 zeigt die Lage, aber keine vermessenen Höhenlinien.

Am Waschtisch WT2 tropfte es nach dem Öffnen der Armatur unterhalb des Eckventils. Wir stellten die Armatur nach etwa 20 Sekunden wieder ab und stellten einen Eimer darunter. Es blieb offen, ob Wasser vom Anschluss oder aus dem vorher nassen Lappen kam. Frau Lenz sperrte den Platz mit einem Zettel; der Waschraum wird noch nicht öffentlich genutzt. Quellwerk wurde um 10:42 Uhr telefonisch erreicht. Die E-Mail von Frau Voß soll folgen.

Im Flur 0.01 zündete Leuchte L14 bei Betätigung des Schalters zweimal nicht; beim dritten Versuch leuchtete sie. Die benachbarte L13 funktionierte jedes Mal. Herr Bödeker öffnete nichts und sagte, er wolle zuerst den Bewegungsmelder prüfen. Auf dem alten Zettel im Container steht L12. Ich habe den Aufkleber an der betroffenen Leuchte heute selbst als L14 gelesen. Im Technikraum war keine Störung angezeigt. Über die Ursache kann ich nichts sagen.

4 Letzte Beobachtungen und Unterlagen

Im Flur fehlen bei zwei Steckdosen die Beschriftungen, die im Abnahmeblatt Elektro unter Punkt 3 genannt sind. Herr Bödeker zeigte einen Ausdruck mit zwei nachgelieferten Etiketten, brachte sie während des Rundgangs aber nicht an. Die im selben Blatt genannte Abdeckung an Dose D09 sitzt inzwischen fest. Wir haben die Dose nicht geöffnet. Der Netzwerkmessbericht lag heute nicht vor.

Frau Lenz nannte den 30.09.2026 als geplanten Möbelliefertermin. Sie bat ausdrücklich darum, Reparaturen am Waschraum nicht auf den Vormittag dieser Lieferung zu legen. Eine Frist habe ich keiner Firma gesetzt. Herr Falk bot mündlich einen Besuch am 25.09. an, wollte aber zuvor wissen, ob die Glaserei kommt. Für die Ausbaugewerke ist am 29.09. ein Termin vorgesehen; ob dabei eine Abnahme erfolgen kann, soll Frau Lenz nach Rücksprache entscheiden.

Maren Döring | Abschluss der Niederschrift um 12:10 Uhr"""),
            dokument("04_Vertrag_Ausbau.docx", "Vereinbarung über die Ausbauarbeiten", "Nachbarschaft Kieselgarten e. V. | Heike Lenz, Vorstand", "Leineputz Ausbau GmbH | Jonas Falk", "06.07.2026", "KG-26 / AU-04 / beiderseits bestätigte Vertragsausfertigung",
                """1 Vertragsgegenstand

Der Verein Nachbarschaft Kieselgarten e. V., Kieselgartenweg 14, 37574 Einbeck, beauftragt die Leineputz Ausbau GmbH, Flechtgasse 8, 37574 Einbeck, mit den Putz-, Maler- und Bodenfliesenarbeiten im Erdgeschoss des Nachbarschaftshauses. Vertragsunterlagen sind diese Vereinbarung, das Angebot LP-26061 vom 30.06.2026, die Raumausbauliste KG-R-04 vom 27.06.2026 und die VOB/B in der Ausgabe 2016. Die Unterlagen wurden beiden Parteien vor Unterzeichnung vollständig übergeben. Bei inhaltlichen Widersprüchen werden die Parteien die betroffene Leistung vor ihrer Ausführung gemeinsam klären.

Der Auftrag umfasst 286 m² Wandoberflächen, 114 m² Deckenanstrich und 18 m² Bodenfliesen im Waschraum 0.06. Zum Fensteranschluss gehören das Einbetten des bauseits montierten Anschlussbands und das Überarbeiten der Laibungen. Lieferung und Befestigung des Bands sowie das Einstellen von Fenstern und Türen gehören nicht zum Auftrag. Die Zuordnung beschreibt die vereinbarte Leistung; die Parteien treffen damit keine Feststellung über Ursachen späterer Schäden.

2 Vergütung und Ablauf

Die Angebotssumme beträgt 31.800,00 EUR netto zuzüglich 6.042,00 EUR Umsatzsteuer, insgesamt 37.842,00 EUR brutto. Abgerechnet werden die tatsächlich ausgeführten Mengen zu den vereinbarten Einheitspreisen. Die Arbeiten beginnen am 13.07.2026. Die Fertigstellung ist für den 25.09.2026 vereinbart. Die Überprüfung am 22.09. ist ein Baustellenrundgang vor dem vorgesehenen Abnahmetermin am 29.09.2026. Durch den Rundgang wird keine förmliche Abnahme erklärt.

Die Parteien vereinbaren eine förmliche Abnahme. Eine Abnahmeerklärung des Vereins darf Heike Lenz abgeben. Bauüberwacherin Maren Döring darf Beobachtungen aufnehmen und technische Rückfragen stellen; sie erhält durch diesen Vertrag keine Vollmacht zur Abnahme, zum Anerkennen von Nachträgen oder zum Verzicht auf Rechte. Die Nutzung einzelner Räume zur Zwischenlagerung der Vereinsmöbel wird gesondert abgestimmt.

3 Ansprechpartner und Zugang

Jonas Falk koordiniert die Ausführung; seine geschäftliche Kontaktadresse lautet j.falk@leineputz.example. Der Verein ist über heike.lenz@kieselgarten.example erreichbar. Reparaturtermine werden mit Frau Lenz abgestimmt, weil der Zugang außerhalb der Arbeitszeit verschlossen ist. Ausführung und technische Prüfung bleiben Aufgabe der jeweils zuständigen Fachfirma.

Für den Verein: Heike Lenz. Für Leineputz Ausbau GmbH: Jonas Falk. Beide Bestätigungen wurden am 06.07.2026 in der Projektablage erfasst."""),
            dokument("05_Gewerkekarte.pdf", "Vertragskontakte Kieselgarten", "Heike Lenz | Nachbarschaft Kieselgarten e. V.", "Maren Döring | Bauüberwachung", "21.09.2026, 16:25 Uhr", "KG-26 / Kontakte / Stand 3",
                ["""1 Beauftragte Firmen

Die folgende Karte ersetzt meine Liste vom 04.09.2026. Frau Döring, bitte verwenden Sie für die Terminabstimmung die Firmenadressen und nicht die privaten Telefonnummern der Monteure. Der Westanbau gehört nicht zum gegenwärtigen Bauabschnitt. Im Erdgeschoss gibt es vier getrennte Verträge; eine Abnahme bei einer Firma sagt nichts über die übrigen Leistungen aus.""",
                 tabelle(["Gewerk / Vertrag", "Firma und Kontakt", "Umfang"], [
                     ["Ausbau / AU-04", "Leineputz Ausbau GmbH\nJonas Falk\nj.falk@leineputz.example", "Putz, Anstrich, Bodenfliesen; Anschlussband einbetten"],
                     ["Bauelemente / BE-02", "Glaserei Fenstertreu GmbH\nTessa Ahrens\nt.ahrens@fenstertreu.example", "Fenster, Innentüren, Bandmontage, Einstellen der Beschläge"],
                     ["Sanitär / SA-03", "Quellwerk Sanitär GmbH\nAlina Voß\na.voss@quellwerk.example", "Waschtische, Eckventile, Leitungen, Ablaufkörper"],
                     ["Elektro / EL-01", "Elektro Faden GmbH\nNils Bödeker\nn.boedeker@elektro-faden.example", "Leuchten, Schalter, Beschriftung, Datendosen"],
                 ], [0.23, 0.40, 0.37]),
                 """2 Stand meiner Ablage

Elektro wurde am 10.09.2026 gesondert abgenommen. Das Blatt liegt unter EL-01/AB-01. Für Ausbau, Bauelemente und Sanitär gibt es bisher kein Abnahmeprotokoll. Die Firmen sollen am 29.09. um 09:00 Uhr erscheinen; Einladungen sind am 18.09. versandt worden. Ich habe niemandem zugesagt, dass unabhängig vom Befund abgenommen wird. Der Verein hat das Haus noch nicht für den Betrieb geöffnet.

Bei Sanitär ist seit 18.09. Frau Voß zuständig; der bisher aufgeschriebene Herr Riemann arbeitet nicht mehr für Quellwerk. Tür T05 und Fenster F07 wurden am 17.08. durch Fenstertreu montiert. Wer den Anschluss an F07 zuletzt bearbeitet hat, kann ich nicht aus der Rechnung erkennen. Die Karte enthält hierzu keinen Befund.

Heike Lenz | Verteiler: Bauüberwachung und Vereinsablage"""]),
            dokument("06_Abnahme_Elektro.pdf", "Abnahme der Elektroinstallation", "Nachbarschaft Kieselgarten e. V. | Heike Lenz", "Elektro Faden GmbH | Nils Bödeker", "10.09.2026, 14:00 bis 15:05 Uhr", "KG-26 / EL-01 / AB-01",
                """1 Gegenstand und Erklärung

Im Nachbarschaftshaus Kieselgarten, Kieselgartenweg 14, 37574 Einbeck, haben Heike Lenz und Nils Bödeker die Leistungen des Elektrovertrags EL-01 vom 02.07.2026 gemeinsam besichtigt. Maren Döring nahm als Bauüberwacherin teil. Erfasst sind ausschließlich die Elektroarbeiten im Erdgeschoss nach Angebot EF-2628 vom 29.06.2026. Die Beleuchtung des Westanbaus ist nicht Gegenstand dieses Vertrags.

Heike Lenz erklärt für den Verein die Abnahme der Leistungen des Elektrovertrags. Die nachstehend festgehaltenen Punkte bleiben vorbehalten. Diese Erklärung betrifft keine Ausbau-, Fenster-, Türen- oder Sanitärleistungen anderer Firmen. Eine gemeinsame Abnahme des Gesamtgebäudes ist nicht erklärt worden.

2 Beobachtungen beim Termin

Die Raumbeleuchtung ließ sich im Rahmen der Bedienprobe in sämtlichen zugänglichen Räumen einschalten. An Leuchte L14 wurde bei dieser Probe kein Aussetzer festgestellt. Eine vollständige elektrische Prüfung wurde durch die Anwesenden nicht wiederholt; Herr Bödeker übergab den Prüfbericht EF-P26-28 vom 09.09.2026 an Frau Lenz. Die dort aufgeführten Messungen sind von der Fachfirma vorgenommen worden.

3 Vorbehaltene Punkte

Im Flur 0.01 fehlen an den Steckdosen S07 und S08 die vereinbarten Stromkreiskennzeichnungen. An der Datendose D09 im Mehrzweckraum sitzt die Abdeckung locker. Der vereinbarte Messbericht für die Datenverkabelung wurde nicht übergeben. Herr Bödeker sagt zu, die Kennzeichnungen und die Befestigung bis 18.09.2026 zu erledigen und den Bericht bis zu diesem Datum zu senden. Eine technische Neubewertung anderer Gewerke ist damit nicht verbunden.

Frau Lenz behält wegen dieser drei Punkte die Rechte des Vereins vor. Die Abnahmeerklärung wird hierdurch nicht zurückgenommen. Im heutigen Termin werden weder ein Vergleich über Ansprüche noch ein Verzicht auf noch unbekannte Mängel vereinbart. Über den Umfang einer Schlusszahlung wird in diesem Protokoll keine Entscheidung getroffen.

4 Bestätigung

Das Protokoll wurde den Beteiligten am Ende des Termins vorgelesen und am 10.09.2026 um 15:05 Uhr von Heike Lenz und Nils Bödeker bestätigt. Maren Döring hat eine Ausfertigung zur Bauakte genommen. Ablagevermerk von Heike Lenz, 10.09.2026, 16:20 Uhr."""),
            dokument("07_Montagebericht_Tueren.docx", "Montagebericht Bauelemente Erdgeschoss", "Tessa Ahrens | Glaserei Fenstertreu GmbH", "Heike Lenz | Nachbarschaft Kieselgarten e. V.", "17.08.2026, 16:40 Uhr", "BE-02 / Montagezettel 217",
                """1 Ausführung am 17 August

Unser Montageteam, Tessa Ahrens und Leon Witte, war heute von 07:15 bis 16:00 Uhr am Kieselgartenweg 14. Wir haben die Innentüren T03, T04 und T05 eingehängt sowie die Fenster F06 und F07 abschließend eingestellt. Der Boden im Abstellraum 0.05 war mit Schutzvlies abgedeckt. Bei T05 fehlte vor der Tür noch der endgültige Übergang zur Flurfläche. Wir konnten deshalb die endgültige untere Luft an dieser Stelle nicht beurteilen.

T05 ließ sich nach dem Einhängen ohne erkennbaren Kontakt mit dem damals sichtbaren Boden bewegen. Das ist keine Aussage über den späteren Fliesenaufbau im Flur. Wir haben die Bänder in mittlerer Stellung belassen. Ein Kürzen des Türblatts wurde weder vereinbart noch ausgeführt. Der Bauüberwachung war bei unserem Telefonat um 15:20 Uhr bekannt, dass nach den Bodenarbeiten ein Einstelltermin erforderlich sein kann.

2 Anschluss am Ostfenster

Das innere Anschlussband an F07 wurde unten über die gesamte Rahmenbreite von 1,36 m am Rahmen befestigt und auf den vorbereiteten Untergrund geführt. Die Laibung war an der unteren rechten Ecke staubig; dort haben wir vor der Verklebung nachgereinigt. Das Band wurde nicht überputzt. Die Putzarbeiten übernimmt laut Leistungsverteilung Leineputz. Eine Öffnung oder Haftzugprüfung des späteren Anschlusses ist nicht Bestandteil unseres heutigen Montageberichts.

Beim Verlassen der Baustelle war das Band sichtbar und nicht mit einer Schutzleiste verdeckt. Die Breite der auf dem Untergrund liegenden Klebefläche haben wir nicht nachgemessen. Wir haben keine Fotos in die Projektablage übertragen. Die Eintragung im Tageszettel bezeichnet das Fenster als F07, Ostseite Raum 0.03; ein älterer Aufkleber F7 ist dieselbe Stelle.

3 Weitere Abstimmung

Bitte teilen Sie uns nach Abschluss der Boden- und Putzarbeiten einen gemeinsamen Termin mit. Dabei wollen wir die Bedienung der Türen und Fenster erneut prüfen und die Anschlussflächen mit der Bauüberwachung ansehen. Eine Abnahme ist heute nicht durchgeführt worden. Die Montageleistung wurde von Leon Witte auf diesem Bericht als ausgeführt erfasst; die Bestätigung der Leistungserbringung durch den Verein steht noch aus.

Tessa Ahrens | t.ahrens@fenstertreu.example"""),
            dokument("13_Tagesbericht_Ausbau.pdf", "Tagesbericht Ausbau vom 18 September", "Jonas Falk | Leineputz Ausbau GmbH", "Projektablage KG-26", "18.09.2026, 16:15 Uhr", "LP-26061 / TB-31",
                """1 Arbeiten und Besetzung

Von 07:00 bis 15:45 Uhr waren Milan Otte und Sarah Köster im Erdgeschoss tätig. Sie haben die Wandflächen in Raum 0.03 fertig gestrichen und die Sockelfugen im Waschraum 0.06 geschlossen. Jonas Falk war von 11:10 bis 11:40 Uhr zur Abstimmung vor Ort. Die Räume 0.03 und 0.06 wurden anschließend für weitere Arbeiten der Folgegewerke offen gelassen. Das Gebäude war nicht öffentlich zugänglich.

Am Fenster F07 wurde ein etwa handbreiter Bereich unten rechts nachgespachtelt. Milan Otte berichtet, dass an der Übergangsstelle zum inneren Band kein neuer Bandstreifen eingesetzt wurde. Die Oberfläche wurde nach dem Trocknen gestrichen. Der Tagesbericht sagt nichts darüber aus, ob die verdeckte Verklebung auf der ganzen Länge tragfähig war. Eine gesonderte Prüfung der Luftdichtheit wurde nicht beauftragt und nicht vorgenommen.

2 Waschraum

Der Ablaufrost wurde zum Reinigen herausgenommen und wieder eingelegt. An der gegenüberliegenden Wand standen währenddessen zwei geschlossene Farbeimer. Die Bodenfläche wurde mit einem feuchten Schwamm gereinigt, nicht geflutet. Wir haben dabei keine Wasserprobe am Ablauf gemacht. Die Fugen waren um 15:00 Uhr äußerlich trocken; zur Restfeuchte unter den Fliesen enthält dieser Bericht keine Messung.

Die sichtbare Oberfläche liegt am Rand des Ablaufrahmens nach unserem Richtscheit nicht überall auf gleicher Höhe. Wir haben das heute nicht protokolliert vermessen. Alina Voß von Quellwerk war nicht anwesend. Den Ablaufkörper haben wir nicht verändert. Eine Festlegung, ob der Rahmen oder die angrenzende Fliese nachzuarbeiten ist, wurde nicht getroffen.

3 Termine

Der letzte Restanstrich im Abstellraum ist für den 24.09.2026 vorgesehen. Beim Rundgang am 22.09. kann ich ab etwa 09:25 Uhr teilnehmen. Bitte geben Sie mir Bescheid, ob die Glaserei ebenfalls erscheint; ohne sie möchte ich den Fensteranschluss nicht nochmals öffnen. Der Fertigstellungstermin 25.09. bleibt in unserer Wochenplanung stehen. Eine Fertigmeldung haben wir mit diesem Tagesbericht nicht erklärt.

Jonas Falk | erfasst am 18.09.2026 um 16:15 Uhr"""),
        ],
        "mails": [
            mail("01_Lenz_an_Doering.eml", "Heike Lenz <heike.lenz@kieselgarten.example>", "Maren Döring <m.doering@doering-stettner.example>", "2026-09-22T16:20:00+02:00", "Kieselgarten: Unterlagen vom Rundgang",
                 """Sehr geehrte Frau Döring,

anbei gehen meine Randnotizen und die aktuelle Gewerkkarte in die gemeinsame Ablage. Könnten Sie aus Ihrem Sprachmemo, den Notizen und Ihren beiden Bildskizzen ein ordentliches Begehungsprotokoll machen? Ich benötige die einzelnen Beobachtungen je Gewerk und Firma, damit ich die Termine nicht durcheinanderbringe. Bitte belassen Sie unklare Ursachen als unklar. Besonders beim Fenster haben zwei Firmen gearbeitet.

Mir ist wichtig, dass Elektro bereits am 10.09. abgenommen wurde, während Ausbau, Bauelemente und Sanitär noch vor ihrer vorgesehenen Abnahme stehen. Die passende rechtliche Grundlage und etwaige Fristen möchte ich mit Ihnen prüfen, bevor etwas an die Firmen versandt wird. Bitte nehmen Sie den von Herrn Falk genannten Freitag nicht als von uns gesetzte Frist auf.

Das Möbelunternehmen kommt am 30.09. um 08:00 Uhr. Ich habe heute nur den nassen Platz unter WT2 gesperrt und keine andere Nutzung freigegeben. Für die Bildeinträge liegen uns Ihre Skizzen vor, keine Baustellenfotografien. Die Beschriftungen sollen das auch im Protokoll deutlich sagen.

Mit freundlichen Grüßen
Heike Lenz
Vorstand Nachbarschaft Kieselgarten e. V."""),
            mail("08_Quellwerk_Rueckmeldung.eml", "Alina Voß <a.voss@quellwerk.example>", "Maren Döring <m.doering@doering-stettner.example>", "2026-09-22T14:18:00+02:00", "WT2 und Bodenablauf im Kieselgarten",
                 """Sehr geehrte Frau Döring,

ich bestätige unser Telefonat um 10:42 Uhr. Am Waschtisch WT2 haben wir am 16.09. das Eckventil ersetzt. Unser Monteur hat die Verbindung anschließend bei geöffneter Armatur angesehen; ein förmliches Dichtheitsprotokoll für diese einzelne Verbindung wurde nicht erstellt. Ich kann aus der Ferne nicht entscheiden, woher das von Ihnen geschilderte Wasser stammt. Lassen Sie den Platz bitte bis zu unserer Prüfung unbenutzt.

Ich kann am 24.09. zwischen 08:00 und 09:00 Uhr kommen. Den Termin habe ich mit Frau Lenz noch nicht bestätigt. Wir prüfen Ventil, Anschluss und Siphon. Beim Bodenablauf wollen wir gleichzeitig die Einbaulage des Rostrahmens ansehen. Den Fliesenanschluss hat nicht unsere Firma hergestellt. Daraus leite ich aber noch keine Ursache für das stehende Wasser ab; dafür fehlen mir Höhenmessungen.

In unserer Ablage steht bislang nur ein Inbetriebnahmetermin, keine Abnahme. Bitte schicken Sie mir das genaue Raumkürzel und Ihre Beobachtung mit Zeitpunkt. Ersatzteile für das Ventil bringen wir mit. Eine Zusage zu einer vollständigen Beseitigung noch am selben Tag kann ich ohne Befund nicht machen.

Mit freundlichen Grüßen
Alina Voß
Quellwerk Sanitär GmbH"""),
            mail("14_Elektro_Termin.eml", "Nils Bödeker <n.boedeker@elektro-faden.example>", "Heike Lenz <heike.lenz@kieselgarten.example>", "2026-09-23T08:15:00+02:00", "Flurleuchte L14 und Beschriftungen",
                 """Sehr geehrte Frau Lenz,

nach dem gestrigen Rundgang habe ich unseren Prüfbericht vom 09.09. nochmals gelesen. Darin ist L14 im Flur verzeichnet; der Zettel mit L12 war eine handschriftliche Vormerkung aus der Montagephase. Für die jetzige Meldung verwenden wir L14. Ob das Schaltverhalten vom Melder, Anschluss oder Leuchtenbauteil kommt, müssen wir am Gerät prüfen. Ich werde das nicht vorab als bloßen Bedienfehler abtun.

Wir schlagen Donnerstag, 24.09., 13:00 Uhr vor. Dabei bringe ich die noch fehlenden Stromkreiskennzeichnungen für S07 und S08 mit. Die Abdeckung D09 haben wir am 17.09. befestigt. Den Datenmessbericht habe ich im Büro angefordert; der Bericht liegt dieser E-Mail noch nicht bei. Bitte tragen Sie ihn daher nicht als übergeben ein.

Die Arbeiten im Waschraum sind nicht Teil unseres Auftrags. Falls dort Wasser in die Nähe einer elektrischen Anschlussstelle gelangt, geben Sie uns bitte sofort Bescheid und lassen Sie den Bereich nicht benutzen. Eine solche Beobachtung wurde mir gestern nicht geschildert.

Mit freundlichen Grüßen
Nils Bödeker
Elektro Faden GmbH"""),
        ],
        "texte": {
            "03_Randnotizen_Lenz.txt": """Heike Lenz | Kieselgarten | Notizbuch Seite 38
22.09.2026, 09:05 bis 10:35 Uhr. Übertragen um 15:55 Uhr.

09:05 Maren hat Schlüssel. Niemand von Quellwerk da. Im Kalender steht noch Riemann, bitte Firmenkarte ansehen, jetzt Voß.
09:14 Riss links T03. Ich meine, Freitag war nichts zu sehen. Am Freitag war ich aber nur an der Tür, nicht bei gutem Seitenlicht. Maren hält Karte hin. Nicht selbst gemessen.
09:22 F07 unten offen, ungefähr eine Handbreit. Mein Handy blieb im Büro. Maren zeichnet die Stelle später. Ich habe keine Fotos aufgenommen.
09:25 Falk kommt. Er sagt, Band sei von Fenstertreu. Ich erinnere mich an Milan mit Spachtel am Freitag. Nicht sicher, ob genau diese Ecke.
09:30 Wasser aus 2-Liter-Becher am Ablauf. Um 09:38 noch Pfütze links neben Rost. Nicht nachgegossen. Danach mit Lappen aufgenommen.
09:41 WT2: Wasser an Hand beim Ventil. Lappen lag schon im Schrank; war eventuell noch feucht. Eimer hingestellt, Schild geschrieben. Kein Tropfen gezählt.
09:50 Bödeker im Flur. L14 geht nicht zweimal, dann doch. Auf Containerzettel steht L12. Maren liest das Schild L14 ab.
10:10 Etiketten fehlen noch, zwei Stück. D09 sieht ordentlich aus. Bericht Datenleitung immer noch nicht bei mir angekommen.
10:30 Möbel am 30.09. morgens. Falk sagt Freitag denkbar; keine feste Zusage, keine Frist von mir. 29.09. bleibt Besichtigungstermin mit Firmen, Ausgang offen.

Nachtrag 22.09., 15:50 Uhr: Frau Voß hat gemailt, muss ihren Termin noch bestätigen. Ich kann am 24.09. erst ab 08:30 Uhr vor Ort sein. Frau Döring hat keine Vollmacht für meine Abnahmeerklärung. Elektroblatt vom 10.09. in Ordner EL-01 gefunden.
""",
        },
        "csv": {
            "09_Ablesungen.csv": (["Befund_ID", "Zeitpunkt", "Raum", "Bauteil", "Größe", "Wert", "Einheit", "Methode", "Ableserin", "Grenze"], [
                ["B01", "2026-09-22T09:14:00+02:00", "0.03", "T03 links oben", "Rissbreite", "0,4", "mm", "Risskarte", "Maren Döring", "größte von drei Ablesungen; keine Öffnung"],
                ["B01", "2026-09-22T09:16:00+02:00", "0.03", "T03 links oben", "Risslänge", "62", "cm", "Zollstock", "Maren Döring", "ungefähr"],
                ["B02", "2026-09-22T09:22:00+02:00", "0.03", "F07 unten", "sichtbarer offener Anschluss", "18", "cm", "Zollstock", "Maren Döring", "keine verdeckte Prüfung"],
                ["B03", "2026-09-22T09:28:00+02:00", "0.05", "T05 Bandseite", "Luft zum Boden", "3", "mm", "Zollstock", "Maren Döring", "Schätzung"],
                ["B04", "2026-09-22T09:30:00+02:00", "0.06", "Ablauf", "ausgegossenes Wasser", "2", "l", "Messbecher", "Heike Lenz", "einmalig"],
                ["B04", "2026-09-22T09:38:00+02:00", "0.06", "neben Ablauf", "Wassertiefe", "4", "mm", "Zollstock", "Maren Döring", "maximal ungefähr; kein Nivellement"],
            ])
        },
        "bilder": [
            dict(datei="10_Skizze_F07.png", art="fenster", titel="SK-01 | Ostfenster F07 | Raum 0.03", datum="22.09.2026, 11:35 Uhr | Maren Döring", beschriftung="Offener Anschluss unten rechts: etwa 18 cm", untertitel="Befund B02 aus dem Rundgang 09:22 Uhr. Band und Putz nicht geöffnet."),
            dict(datei="11_Skizze_Waschraum.png", art="ablauf", titel="SK-02 | Bodenablauf | Waschraum 0.06", datum="22.09.2026, 11:50 Uhr | Maren Döring", beschriftung="Wasserrest westlich des Rosts, etwa 4 mm tief", untertitel="Befund B04 um 09:38 Uhr. Kein Nivellement; Flächenform nur schematisch."),
        ],
        "zusatztexte": {
            "12_Zugangskalender.txt": """Nachbarschaft Kieselgarten e. V. | Heike Lenz
Zugangskalender, Stand 23.09.2026, 08:45 Uhr | KG-26/ZK-06

24.09.2026: Schlüsselübergabe frühestens 08:30 Uhr durch Lenz. Quellwerk hat 08:00 bis 09:00 vorgeschlagen; Überschneidung noch abzusprechen. Elektro Faden schlägt 13:00 Uhr vor. Kein durchgehend offenes Haus.
25.09.2026: Leineputz möchte eventuell am Fensteranschluss arbeiten. Gemeinsamer Termin mit Fenstertreu bisher nicht bestätigt. Fertigstellung Ausbau laut AU-04 vorgesehen; kein neuer Termin vereinbart.
28.09.2026: Reinigung von 10:00 bis 14:00 Uhr, Schlüssel bei Lenz. Waschraum 0.06 nur nach Rücksprache betreten. WT2 bleibt bis zur fachlichen Prüfung abgesperrt.
29.09.2026: Firmenbesichtigung um 09:00 Uhr, Einladungen vom 18.09. Frau Lenz entscheidet über etwaige Abnahmeerklärungen. Ausbau, Sanitär und Bauelemente getrennt dokumentieren. Elektrotermin ist nicht neu angesetzt; bestehendes Blatt bleibt in EL-01.
30.09.2026: Möbelanlieferung von 08:00 bis 11:00 Uhr über Seiteneingang. Bodenflächen nicht mit Werkzeug zustellen. Das ist eine Lieferung, keine Eröffnung des Hauses.
03.10.2026: Ursprünglich angefragter Vereinsnachmittag wurde am 21.09. abgesagt. Es gibt keine freigegebene öffentliche Nutzung.

Dieser Kalender hält Zugangsmöglichkeiten fest. Er enthält keine an Firmen gerichteten Beseitigungsfristen. Änderungen bestätigt Heike Lenz über heike.lenz@kieselgarten.example.
"""
        },
        "pruefung": [
            "Einzelbeobachtungen mit Raum, Bauteil, Zeit, Quelle und Messgrenze erfassen; B01 0,4 mm nicht zu 4 mm machen und L14 nicht als L12 führen.",
            "Gewerke und Firmen zuordnen, aber bei Fensteranschluss und Bodenablauf keine alleinige Verursachung aus der Vertragskarte ableiten.",
            "Abnahme Elektro vom 10.09. getrennt von den noch nicht abgenommenen Gewerken behandeln; passende Rechtsgrundlage und Fristen fachlich prüfen lassen, nicht blind vereinheitlichen.",
            "Skizzen nicht als Fotos oder Messpläne bezeichnen; angebotene Termine nicht zu gesetzten Fristen und Beobachtungen nicht zu bewiesenen Ursachen umdeuten.",
        ],
    },
}

AKTEN["bau-rundum-lv-abgleich-detmold"] = {
    "titel": "Baubeschreibung und Ausbau LV für das Lernatelier Bachwinkel in Detmold",
    "stand": "2026-09-18",
    "beschreibung": "Zwei Fassungen der Baubeschreibung, ein noch nicht freigegebenes Ausbau-LV und eigenständige Planungsbeiträge für den Umbau eines privaten Lernateliers.",
    "dokumente": [
        dokument("02_Baubeschreibung_01.pdf", "Baubeschreibung Lernatelier Bachwinkel", "Nora Küster | Planungsbüro Raumkante", "Bachwinkel Lernen GmbH | Ole Reinhold", "02.09.2026", "BW-26 / BB-01 / Fassung zur Nutzerbesprechung",
            """1 Gebäude und Nutzung

Das Erdgeschoss des Hauses Bachwinkel 22 in 32756 Detmold wird zu einem Lernatelier mit zwei Gruppenräumen umgebaut. Auftraggeberin ist die Bachwinkel Lernen GmbH. Raum 0.11 erhält zwölf Arbeitsplätze, Raum 0.12 acht Plätze. Der dazwischenliegende Flur 0.10 verbindet Eingang und Hofausgang. Der Teeraum 0.13 dient ausschließlich der Zubereitung von Getränken; eine Kochküche ist nicht vorgesehen. Das Obergeschoss bleibt unberührt.

Diese Fassung beschreibt den Besprechungsstand vom 01.09.2026. Die Ausbaumaße richten sich nach Plan BW-A-21/02. Die Trennwand zwischen den Gruppenräumen wird als Metallständerwand ausgeführt. Für die Kalkulation ist eine Fertigdicke von 100 mm angesetzt. Die Art und Stärke der Beplankung wird mit der Fachplanung noch abgestimmt. Die zum Flur gerichteten Oberflächen werden vollflächig gestrichen. Am Bestandsmauerwerk bleiben die vorhandenen Putzflächen erhalten, soweit sie tragfähig sind.

2 Oberflächen

In den Gruppenräumen und im Flur ist ein elastischer Belag vorgesehen. Der Auftraggeber bevorzugt zunächst PVC in Bahnen. Die endgültige Materialentscheidung soll am 09.09. getroffen werden. Für die Kostenschätzung werden 96 m² Belagsfläche verwendet. Sockel sollen aus demselben Material hochgezogen werden. Im Teeraum bleiben die vorhandenen Bodenfliesen bestehen, sofern die Prüfung nach Demontage der Küchenzeile keine losen Fliesen ergibt.

An der neuen Trennwand sollen die Stoßstellen der Platten verspachtelt werden. Die Oberflächenqualität ist mit dem späteren Anstrich abzustimmen. In Raum 0.11 wird das Licht überwiegend entlang der Wand geführt. Das Lichtkonzept liegt noch nicht vor. Ein Musterfeld soll vor dem vollflächigen Anstrich von Frau Küster und Herrn Reinhold angesehen werden.

3 Türen und Decken

Tür T12 zwischen Flur und Gruppenraum 0.12 wird erneuert. Für den vorläufigen Kostenansatz wird eine Tür ohne besondere Feuerwiderstandsanforderung mit einer lichten Durchgangsbreite von 0,90 m angesetzt. Die Tür zum Hof bleibt bestehen. Ob T12 besondere Eigenschaften benötigt, ist im Brandschutzbeitrag zu klären. Die Unterdecke im Flur wird auf einer Fläche von 24 m² erneuert. Revisionsöffnungen sind in dieser frühen Fassung noch nicht gezählt.

Nora Küster | Versandstand vom 02.09.2026. Diese Fassung ist nicht als Ausführungsfreigabe bezeichnet."""),
        dokument("03_Baubeschreibung_02.docx", "Baubeschreibung Lernatelier Bachwinkel", "Nora Küster | Planungsbüro Raumkante", "Bachwinkel Lernen GmbH | Ole Reinhold", "11.09.2026", "BW-26 / BB-02 / abgestimmter Nutzerstand",
            """1 Geltungsbereich und Wandaufbau

Diese Fassung ersetzt BB-01 vom 02.09.2026 für die weitere Vorbereitung der Ausschreibung. Grundriss und Nutzungsgrenzen bleiben unverändert: Gruppenräume 0.11 und 0.12, Flur 0.10 sowie Teeraum 0.13 im Erdgeschoss Bachwinkel 22, Detmold. Die Bauherrin hat am 09.09. die Materialauswahl bestätigt. Die Vergabe ist privat; ein Auftrag an ein Ausbauunternehmen besteht noch nicht. Die Freigabe der LV-Fassung erfolgt gesondert.

Die Trennwand zwischen den Gruppenräumen erhält eine Fertigdicke von 125 mm, mit beidseitig zweilagiger Beplankung und Mineralwolleeinlage. Die freie Wandlänge beträgt 4,80 m, die Höhe 3,10 m. In der Wand liegt keine Türöffnung. Für die Wandfläche wird nur eine Ansichtsfläche zur Mengenangabe angesetzt; beide Wandseiten gehören zur beschriebenen Leistung. Die Montage endet an der tragenden Decke und nicht an der späteren Unterdecke.

Die sichtbaren Oberflächen der neuen Wand sind für den geplanten matten Anstrich und das seitlich einfallende Licht vollflächig zu spachteln. Vereinbart ist für die Ausschreibungsbeschreibung die Qualitätsstufe Q3. Ein Musterfeld von 2 m² wird vor Ausführung der Gesamtfläche im Raum 0.11 angelegt. Das Musterfeld ersetzt nicht die Beschreibung der geschuldeten Oberfläche. Auf Bestandsputz ist nach Reinigung und örtlichen Ausbesserungen ein Anstrich vorgesehen; ein vollflächiger Neuputz ist dort nicht enthalten.

2 Bodenbeläge

In 0.11, 0.12 und 0.10 wird Linoleum in Bahnen ausgeschrieben. PVC ist nach der Nutzerbesprechung nicht mehr vorgesehen. Die geometrische Bodenfläche beträgt nach BW-M-02 insgesamt 96,00 m². Die Mengen im Leistungsverzeichnis sollen als Einbaumengen ohne Verschnittzuschlag stehen; der Verschnitt ist bei der Preisbildung zu berücksichtigen. Die Sockel werden als gesonderte Leistung mit 10 cm Höhe beschrieben. Die Bemusterung erfolgt anhand dreier gedeckter Farbtöne; ein bestimmtes Fabrikat wurde nicht festgelegt.

Der Teeraum 0.13 gehört nicht zu diesen 96,00 m². Seine 12,00 m² Fliesen bleiben erhalten. Nur zwei lose Fliesen im Bereich der früheren Küchenzeile werden ausgetauscht, soweit gleichformatiges Material beschafft werden kann. Der Untergrund für Linoleum ist vor Einbau zu prüfen; erforderliche weitergehende Maßnahmen sind vor Ausführung mit der Planung abzustimmen.

Nora Küster | BB-02, Seite 1""",
            """3 Türen

Für Tür T12 gilt der Fachbeitrag BS-09 vom 10.09.2026. Die Tür erhält die dort projektspezifisch benannten Eigenschaften für die Abtrennung des Gruppenraums zum Flur. Die lichte Durchgangsbreite beträgt 1,00 m; das Rohbaumaß und die Bandseite ergeben sich aus Türblatt BW-T-12/02. Eine automatische Offenhaltung ist nicht vorgesehen. Der Hersteller muss die Eignung des gelieferten Gesamtsystems einschließlich Zarge und Schließmittel nachweisen. Diese Baubeschreibung trifft keine eigenständige brandschutztechnische Bemessung.

Der Flur bleibt während der Bauzeit gesperrt. Staubschutz und eine abschließbare Trennung zum weiterhin genutzten Treppenhaus sind Bestandteil des Ausbauauftrags. Schlüssel werden ausschließlich von Ole Reinhold ausgegeben. Der Bestandsausgang zum Hof wird weder versetzt noch im Querschnitt verkleinert. Sein Zustand ist vor Beginn gemeinsam zu dokumentieren.

4 Unterdecken und Wartungszugang

Im Flur 0.10 wird die Unterdecke auf 24,00 m² erneuert. Die Abhanghöhe beträgt 35 cm unter Bestandsdecke. Über der Decke liegen Absperreinrichtungen und zwei Anschlusskästen. Nach dem Fachbeitrag TW-06 vom 10.09.2026 sind zwei demontierbare Revisionsöffnungen mit freier Öffnung von jeweils 600 × 600 mm vorzusehen. Die genaue Lage wird vor Montage anhand der tatsächlich eingebauten Anlagen festgelegt. Ein bloßer Zugang durch Ausbau von Leuchten genügt für diese beiden Stellen nicht.

In den Gruppenräumen bleiben die vorhandenen Decken bestehen und werden gestrichen. Die Gesamtfläche dieser beiden Decken beträgt 72,00 m². Akustikelemente an den Wänden gehören zu einem späteren Möblierungsauftrag und sind nicht im Ausbau-LV enthalten. Die angebotene Ausführung darf deshalb keine Wandabsorber stillschweigend einpreisen.

5 Stand und Beteiligte

Die Auftraggeberin hat Material und Raumnutzung bestätigt, nicht sämtliche technischen Einzelheiten der Fachbeiträge. Brandschutzplanerin Elke Mertens prüft die Türkonfiguration; TGA-Planer Cem Arslan prüft die Zugänglichkeit oberhalb der Flurdecke. Herr Reinhold entscheidet über Farben erst nach Bemusterung. Der Ausbau soll vom 02.11. bis 27.11.2026 erfolgen. Ein Vertragstermin ist daraus noch nicht entstanden.

Nora Küster | Planungsbüro Raumkante | n.kuester@raumkante.example"""),
        dokument("04_LV_Ausbau_03.docx", "Leistungsverzeichnis Ausbau Bachwinkel", "Ralf Seeger | Planungsbüro Raumkante", "Interne Vergabeablage BW-26", "14.09.2026", "BW-LV-AU / Revision 03 / noch nicht versandt",
            ["""1 Vorbemerkungen

Die Leistungen betreffen den Innenausbau des Erdgeschosses Bachwinkel 22, Detmold. Abgerechnet werden die tatsächlich ausgeführten Mengen zu den angebotenen Einheitspreisen. Die nachstehenden Mengen dienen der Angebotskalkulation. Preise sind vom Bieter einzutragen; dieses Dokument enthält keine Planerpreise. Die Baustelle kann nach Terminabstimmung besichtigt werden. Ausbauleistungen im Obergeschoss sind nicht enthalten.

Grundlage des Mengengerüsts ist BW-A-21/02. Beim Fortschreiben der Texte wurden die Raumbezeichnungen aus BB-01 übernommen. Die Einarbeitung der am 11.09. eingegangenen Fach- und Nutzerunterlagen ist im internen Laufzettel noch nicht als abgeschlossen vermerkt. Ralf Seeger hat die Revision 03 am 14.09. um 16:30 Uhr in die Ablage gestellt.

1.1 Baustelleneinrichtung

Position 01.010 umfasst das Einrichten und Räumen der Ausbauarbeitsplätze einschließlich einer staubdichten und abschließbaren Trennung zum Treppenhaus. Vorhandene Flächen außerhalb des Arbeitsbereichs sind vor Beschädigung zu schützen. Die Schutzmaßnahmen sind bis zum Abschluss der stauberzeugenden Arbeiten vorzuhalten und anschließend rückstandsfrei zurückzubauen. Menge: 1 pauschal.

1.2 Metallständerwand

Position 02.010 umfasst die Trennwand zwischen 0.11 und 0.12 als nichttragende Metallständerwand mit 100 mm Fertigdicke, beidseitig einlagiger Beplankung und Mineralwolleeinlage. Die Wand ist an angrenzende Bauteile anzuschließen und bis zur tragenden Decke zu führen. Öffnungen sind nicht vorgesehen. Menge: 14,88 m².

Position 02.020 umfasst das Verspachteln der sichtbaren Plattenflächen der Position 02.010 in Qualitätsstufe Q2 einschließlich der Befestigungspunkte. Ein vollflächiger Feinspachtelauftrag ist nicht Bestandteil dieser Position. Das anschließende Anstrichsystem ist in Position 04.010 erfasst. Menge: 29,76 m².""",
             tabelle(["Position", "Menge", "Einheit"], [["01.010", "1", "pauschal"], ["02.010", "14,88", "m²"], ["02.020", "29,76", "m²"]], [0.5, 0.25, 0.25])],
            """2 Bodenarbeiten

Position 03.010 umfasst Lieferung und Verlegung eines PVC-Belags in Bahnen in den Gruppenräumen 0.11 und 0.12 sowie im Flur 0.10. Der Belag wird vollflächig verklebt; Fugen sind entsprechend dem gewählten System zu schließen. Der Farbton wird aus der Standardkollektion des angebotenen Herstellers gewählt. Die Position umfasst einen Verschnittansatz von 10 Prozent in der ausgeschriebenen Menge. Menge: 105,60 m².

Position 03.020 umfasst Sockelstreifen aus dem Material der Position 03.010, 8 cm hoch, einschließlich Innen- und Außenecken. Abgerechnet wird die ausgeführte Länge. Öffnungen werden abgezogen. Menge: 67,20 m. Die Erneuerung der Fliesen in Raum 0.13 ist nicht enthalten. Zum Austausch einzelner loser Fliesen ist in dieser Revision keine Position angelegt.

3 Malerarbeiten

Position 04.010 umfasst den zweifachen matten Anstrich der neuen Wandflächen mit einer für den Untergrund geeigneten Beschichtung. Kleinere Schleifarbeiten an den verspachtelten Fugen und die erforderliche Grundierung sind eingeschlossen. Die Beschichtung ist gleichmäßig ohne erkennbare Ansätze auszuführen. Menge: 29,76 m². Eine besondere Musterfläche ist in dieser Position nicht genannt.

Position 04.020 umfasst Reinigen, örtliches Ausbessern und zweimaliges Streichen der Bestandswandflächen. Die Mengenzusammenstellung führt hierfür 141,50 m². Das Entfernen größerer loser Putzbereiche wird vor Ausführung mit der Bauleitung abgestimmt und ist nicht Bestandteil dieser Position. Position 04.030 umfasst den Anstrich der bestehenden Decken in 0.11 und 0.12 mit insgesamt 72,00 m².

Ralf Seeger | Mengenstand aus BW-M-01; Übernahme in Revision 03 am 14.09.2026""",
            """4 Türen und Unterdecken

Position 05.010 umfasst Tür T12 als glattes Holztürelement ohne besondere Feuerwiderstands- oder Rauchschutzanforderung. Die lichte Durchgangsbreite beträgt 0,90 m, die Höhe 2,10 m. Beschläge, Zarge, Drückergarnitur und Montage sind enthalten. Ein Türschließer ist nicht vorgesehen. Die Oberfläche wird werkseitig weiß beschichtet. Menge: 1 Stück. Die endgültige Bandseite wird vor Bestellung aus dem Ausführungsplan übernommen.

Position 06.010 umfasst die abgehängte geschlossene Gipsplattendecke im Flur 0.10, Abhängung 35 cm unter Bestandsdecke, einschließlich Unterkonstruktion, Randanschlüssen und Verspachtelung. Menge: 24,00 m². Öffnungen für die in der Elektroplanung benannten Leuchten sind einzuschneiden; gesonderte Revisionsklappen sind nicht vorgesehen. Bei Bedarf erfolgt der Zugang oberhalb der Decke nach Ausbau der Leuchten.

5 Abschlussarbeiten und Abgrenzung

Position 07.010 umfasst die Reinigung der eigenen Arbeitsbereiche und das Entfernen der von den Ausbauarbeiten verursachten Verschmutzungen an angrenzenden geschützten Flächen. Der vorhandene Hofausgang bleibt erhalten und ist bei Transporten zu schützen. Menge: 1 pauschal. Die laufende Gebäudereinigung und das Reinigen der unberührten Räume im Obergeschoss gehören nicht zum Leistungsumfang.

Lose Möblierung, Wandabsorber und die Teeküchenmöbel werden durch die Auftraggeberin gesondert beschafft. Elektroanschlüsse und Trinkwasserleitungen werden nicht mit diesem LV vergeben. Der Ausbauunternehmer muss den Zugang zu den betroffenen Anschlussstellen mit der Bauleitung koordinieren. Die Montageplanung für Revisionsstellen ist vor Schließen der Decke vorzulegen, soweit solche Stellen mit den Fachplanern vereinbart werden.

Zusammengestellt von Ralf Seeger. Revision 03 umfasst drei Seiten. Angebotsversand und technische Freigabe sind im Verteiler noch nicht bestätigt."""),
        dokument("05_Aufmassraeume.pdf", "Raummaße Erdgeschoss Bachwinkel", "Nora Küster | Planungsbüro Raumkante", "Ralf Seeger | Ausschreibung", "11.09.2026, 09:15 Uhr", "BW-M-02 / zu BW-A-21/02",
            ["""1 Flächen und Abzüge

Die Maße wurden am 08.09. von Nora Küster und Ole Reinhold im geräumten Erdgeschoss aufgenommen. Es handelt sich um lichte Innenmaße. Der Flur ist rechteckig; Nischen über 10 cm Tiefe gibt es in den erfassten Räumen nicht. Bodenflächen werden ohne Verschnitt angegeben. Die Summe der Räume mit neuem elastischem Belag beträgt 96,00 m². Der 12,00 m² große Teeraum bleibt davon getrennt.""",
             tabelle(["Raum", "Länge × Breite", "Bodenfläche"], [["0.11 Gruppenraum", "9,00 × 4,80 m", "43,20 m²"], ["0.12 Gruppenraum", "6,00 × 4,80 m", "28,80 m²"], ["0.10 Flur", "12,00 × 2,00 m", "24,00 m²"], ["0.13 Teeraum", "4,00 × 3,00 m", "12,00 m²"]], [0.45, 0.3, 0.25]),
             """2 Wand und Sockel

Die neue Trennwand ist 4,80 m lang und 3,10 m hoch. Daraus ergeben sich 14,88 m² für eine Wandansicht und 29,76 m² für beide zu beschichtenden Seiten. Die Wand enthält keine Öffnung. Diese geometrischen Werte entscheiden nicht über Wanddicke oder Beplankung.

Der Umfang der drei Belagsräume beträgt zusammen 77,20 m. Öffnungen und nicht zu belegende feste Anschlussbereiche ergeben zusammen 10,00 m Abzug. Für den Sockel verbleiben deshalb 67,20 m. Die Höhe ist eine Material- und Leistungsfestlegung, keine Größe aus diesem Aufmaß. Das Raumblatt BW-M-01 vom 02.09. führte bereits dieselben Innenmaße, enthielt aber in seiner Übertragungszeile 105,60 m² einschließlich zehn Prozent Verschnitt.

3 Sichtbare Grenzen

Die Raumhöhe wurde an drei zugänglichen Punkten geprüft. Unter abgehängten Teilen im Flur wurde die Bestandsdecke nicht geöffnet. Aus der Skizze BW-A-21/02 dürfen keine exakten Lagen verdeckter Leitungen abgenommen werden. Revisionsstellen werden vor Montage mit der Fachplanung örtlich festgelegt.

Nora Küster | geprüft gegen die örtlichen Maßnotizen am 11.09.2026"""]),
        dokument("06_Fachbeitrag_Brandschutz.pdf", "Tür T12 im Lernatelier", "Elke Mertens | Ingenieurbüro Brandlinie", "Nora Küster | Planungsbüro Raumkante", "10.09.2026", "BS-09 / BW-26 / Türabstimmung",
            """1 Gegenstand der Abstimmung

Sehr geehrte Frau Küster, für die Trennung des Gruppenraums 0.12 vom Flur 0.10 haben wir die Türkonfiguration im Projekt Bachwinkel heute mit Herrn Reinhold besprochen. Die folgende Festlegung bezieht sich ausschließlich auf Tür T12 in der vorliegenden Umbauplanung. Sie ist keine allgemeine Aussage über Türen in Lernräumen. Die Bestandswand neben der Öffnung bleibt in unserer weiteren Detailprüfung zu berücksichtigen.

2 Vorgabe für die weitere Planung

Für die Ausschreibung ist T12 als feuerhemmendes, rauchdichtes und selbstschließendes Element einschließlich abgestimmter Zarge und Schließmittel zu beschreiben. Die lichte Durchgangsbreite soll nach der Nutzerabstimmung 1,00 m betragen. Eine bloße Türblattbezeichnung reicht für die Bestellung nicht aus; das angebotene System und seine Eignung für die vorhandene Einbausituation sind vor Bestellung zu prüfen. Die konkrete Nachweisführung und Einbaudetails müssen wir anhand des ausgewählten Systems freigeben.

Im vorläufigen Kostenblatt wurde noch ein Element ohne besondere Anforderungen und mit 0,90 m Breite geführt. Dieser Ansatz entspricht nicht dem heutigen Fachbeitrag. Ich habe keine automatische Offenhaltung vorgesehen. Der Nutzer wünscht eine im Alltag leicht zu bedienende Tür; die hierfür geeigneten Beschläge stimmen wir anhand des angebotenen Systems ab. Ein dauerhaftes Offenstellen durch einen Keil ist keine von uns geplante Betriebsweise.

3 Weitere Bearbeitung

Bitte legen Sie mir vor dem Versand das Türblatt und den zugehörigen LV-Text gemeinsam vor. Ich muss dann insbesondere Einbauwand, Anschlüsse und die Zusammenstellung des Systems nachvollziehen können. Der beigefügte Plan BW-A-21/02 zeigt die Lage, ersetzt aber keinen Systemnachweis. Die Abmessung der Rohbauöffnung ist noch anhand des gewählten Elements festzulegen.

Diese Nachricht erweitert nicht den Auftrag auf das Obergeschoss. Für andere Bestandstüren enthält sie keine Aussage. Die in BB-01 angekündigte spätere Abstimmung ist mit diesem Fachbeitrag für T12 konkretisiert; die weitere technische Prüfung bleibt erforderlich.

Mit freundlichen Grüßen
Elke Mertens | e.mertens@brandlinie.example"""),
        dokument("07_TGA_Revisionsstellen.docx", "Wartungszugang oberhalb der Flurdecke", "Cem Arslan | TGA Büro Leitwerk", "Nora Küster | Planungsbüro Raumkante", "10.09.2026, 15:30 Uhr", "TW-06 / BW-26",
            """1 Einbauten im Flur

Sehr geehrte Frau Küster, oberhalb der Flurdecke 0.10 liegen zwei Absperreinrichtungen der Heizungsleitungen und zwei Anschlusskästen. Die Absperreinrichtungen befinden sich im westlichen Drittel, die Kästen am Übergang zu Raum 0.12. Die Angaben beruhen auf unserer Öffnung vom 08.09.2026. Ein durchgehender Zugang vom Nachbarraum ist wegen der vorhandenen Unterzüge nicht möglich. Die Konstruktion der neuen Decke muss den späteren Wartungszugang berücksichtigen.

Wir benötigen zwei demontierbare Revisionsöffnungen mit freiem Durchgang von jeweils 600 × 600 mm. Die Angabe meint das freie Öffnungsmaß, nicht das Außenmaß des Klappenrahmens. Die Öffnungen dürfen durch die Unterkonstruktion oder hinter der Klappe liegende Leitungen nicht wieder verengt werden. Die Lage ist vor Montage vor Ort zu markieren. Eine Verschiebung um wenige Zentimeter kann nötig sein; eine Verringerung des freien Maßes ist damit nicht freigegeben.

2 Abgrenzung zur Elektroplanung

Die vorgesehenen Einbauleuchten haben wesentlich kleinere Ausschnitte. Über diese Ausschnitte sind die Absperreinrichtungen nicht sicher zu bedienen. Der Zugang darf deshalb nicht allein vom Ausbau einer Leuchte abhängig gemacht werden. Die zwei Revisionsöffnungen sind im Ausbau-LV eigenständig zu erfassen oder vollständig in einer klar bezeichneten Deckenposition zu beschreiben. Die Elektroplanung enthält dafür keine Lieferung.

Die Revision TW-05 vom 03.09. ging noch von zugänglichen Bestandsdeckenfeldern aus. Nach der Entscheidung für eine geschlossene Gipsplattendecke ist diese Annahme entfallen. Die Leitungsführung selbst wird dadurch nicht verändert. Der Vorschlag betrifft die Wartbarkeit; technische Anforderungen an ein gegebenenfalls klassifiziertes Deckensystem sind mit der zuständigen Fachplanung abzugleichen.

3 Termin

Vor dem Schließen der Decke möchte ich die erreichbaren Bauteile mit dem Trockenbauer ansehen. Für die Planfreigabe benötige ich einen Deckenspiegel mit den beiden Öffnungen und den Leuchten. Einen solchen Plan habe ich bislang nicht erhalten. Bitte rechnen Sie die Öffnungen nicht als zusätzliche neue Boden- oder Deckenfläche; die 24,00 m² Flurgrundfläche ändern sich durch sie nicht.

Mit freundlichen Grüßen
Cem Arslan | c.arslan@leitwerk.example"""),
        dokument("08_Nutzerbesprechung.docx", "Materialbesprechung vom 9 September", "Ole Reinhold | Bachwinkel Lernen GmbH", "Nora Küster und Ralf Seeger | Planungsbüro Raumkante", "09.09.2026, 17:10 Uhr", "BW-26 / NB-04",
            """1 Teilnehmer und Raumprogramm

Die Besprechung fand von 15:00 bis 16:20 Uhr im Büro der Bachwinkel Lernen GmbH statt. Teilgenommen haben Ole Reinhold, Nora Küster und Ralf Seeger. Die zwölf Arbeitsplätze in 0.11 und acht Plätze in 0.12 bleiben unverändert. Das Lager im Obergeschoss ist nicht Bestandteil des Umbauauftrags. Herr Reinhold bestätigt, dass im Teeraum keine Kochgeräte mit eigener Abluft geplant sind.

2 Materialentscheidungen

Nach Ansicht der drei vorgelegten Belagsmuster entscheidet sich Herr Reinhold für Linoleum in Bahnen in den beiden Gruppenräumen und im Flur. Die Entscheidung ersetzt den bisherigen Kostenansatz PVC. Ein bestimmtes Fabrikat wird nicht vorgeschrieben. Der Sockel soll 10 cm hoch sein, weil die Reinigung mit größeren Geräten erfolgen soll. Der genaue Farbton wird nach den Angeboten anhand der verfügbaren Kollektion gewählt. Die Planung darf hierfür drei Farbtöne vorschlagen.

Die neue Wand zwischen den Gruppenräumen soll wegen der mitgebrachten Fachplanung mit 125 mm Fertigdicke und beidseitig zweilagiger Beplankung weiterbearbeitet werden. Für die sichtbare Oberfläche wird Q3 vorgesehen. Herr Seeger weist darauf hin, dass im LV-Arbeitsstand noch die frühere Wandbeschreibung steht. Frau Küster nimmt die Änderungen in BB-02 auf. Der heutige Vermerk enthält keine Freigabe des Leistungsverzeichnisses.

3 Erhalt und Bemusterung

Die Fliesen im Teeraum bleiben erhalten. Zwei lose Fliesen unmittelbar vor der alten Küchenzeile sollen nach Möglichkeit ersetzt werden. Wenn kein passendes Format zu beschaffen ist, entscheidet Herr Reinhold nach Vorlage einer Alternative; ein vollständiger neuer Fliesenboden wird heute nicht bestellt. Die bestehenden Gruppendecken werden nur gestrichen. Die Wandabsorber werden später zusammen mit den Möbeln beschafft.

Für den Anstrich der neuen Wand vereinbaren die Teilnehmer ein Musterfeld von 2 m² in Raum 0.11. Dabei sollen Farbe und sichtbare Oberflächenwirkung unter dem tatsächlichen Licht beurteilt werden. Der Mustertermin wird mit der ausführenden Firma festgelegt. Die technischen Anforderungen bleiben in der Beschreibung zu benennen; der Vermerk ersetzt diese nicht.

Ole Reinhold | Bestätigt per E-Mail am 09.09.2026 um 17:10 Uhr"""),
    ],
    "mails": [
        mail("01_Kuester_LV_Abgleich.eml", "Nora Küster <n.kuester@raumkante.example>", "Ralf Seeger <r.seeger@raumkante.example>", "2026-09-17T09:05:00+02:00", "Bachwinkel: Vor dem Versand noch BB gegen LV lesen",
             """Guten Morgen Herr Seeger,

bitte gleichen Sie die Baubeschreibung mit dem Ausbau-LV ab, bevor wir die Unterlagen an die drei angefragten Firmen senden. Im Ordner liegen BB-01 und BB-02; die ältere Datei soll für die Entstehungsgeschichte erhalten bleiben. Ich brauche eine Liste der Widersprüche und fehlenden Leistungen mit genauen Fundstellen in den jeweiligen Fassungen. Eine bloße Zusammenfassung hilft mir bei der Freigabe nicht.

Bitte ändern Sie die LV-Datei zunächst nicht. Ich möchte die betroffenen Textstellen nebeneinander sehen und mit Ole Reinhold sowie den Fachplanern besprechen. Eine jüngere E-Mail ist nicht automatisch eine neue vollständige Leistungsbeschreibung. Bei Maßen und Mengen bitte angeben, ob eine andere Mengendefinition oder wirklich eine abweichende Geometrie vorliegt.

Die Anfrage soll ursprünglich am 21.09. hinausgehen. Ich habe noch keine Versandfreigabe erteilt. Herr Arslan hat insbesondere um den Deckenspiegel gebeten; seine Nachricht befindet sich ebenfalls in der Ablage. Bitte nehmen Sie offene Nachweise als offen auf, ohne eine technische Freigabe zu formulieren.

Freundliche Grüße
Nora Küster"""),
        mail("10_Seeger_Dateiversand.eml", "Ralf Seeger <r.seeger@raumkante.example>", "Nora Küster <n.kuester@raumkante.example>", "2026-09-14T16:42:00+02:00", "BW-LV-AU Revision 03 in der Ablage",
             """Hallo Frau Küster,

die Revision 03 des Ausbau-LV liegt jetzt im Projektordner. Ich habe die Trennung zum Treppenhaus und den Deckenanstrich ergänzt. Die neuen Nutzerwünsche vom Mittwoch habe ich beim heutigen Durchlauf noch nicht vollständig in jede Position übernommen. Der Dateiname soll daher nicht als Bestätigung einer abschließenden Prüfung verstanden werden.

Die 14,88 m² in der Wandposition sind eine Ansicht. Für Spachtel und Anstrich habe ich 29,76 m², also beide Seiten, eingesetzt. Bei den Bodenflächen steht noch meine Übertragungszeile aus BW-M-01 mit zehn Prozent Verschnitt. Das Raumblatt von Freitag habe ich erhalten, die Mengenspalte aber noch nicht umgestellt.

Den alten Türtext habe ich stehen gelassen, bis wir den neuen Fachbeitrag gemeinsam durchsehen. Der Deckenspiegel ist noch nicht in meinem Posteingang. Es gibt keinen Versand an Firmen und keine ausgedruckte Angebotsfassung. Bitte verwenden Sie für die Besprechung diese Revision und nicht meinen lokalen Zwischenstand vom 12.09.

Viele Grüße
Ralf Seeger
Planungsbüro Raumkante"""),
    ],
    "texte": {
        "11_Planlauf_Notizen.txt": """Planungsbüro Raumkante | BW-26 | Posteingang Nora Küster
Stand 18.09.2026, 08:20 Uhr

02.09., 10:00: BB-01 an Reinhold, Seeger. Zu diesem Zeitpunkt PVC und T12 ohne festgelegte Spezialanforderung im Kostenansatz. Datei nicht löschen, Sitzungsbezug.
09.09., 17:10: Nutzervermerk NB-04 bestätigt. Linoleum, Sockel 10 cm, Wand 125 mm, Q3, Musterfeld. Herr Seeger war bei Besprechung dabei.
10.09., 11:25: BS-09 von Elke Mertens eingegangen. Türblatt BW-T-12/02 wurde angekündigt, ist im Ordner noch nicht als eigene Zeichnung abgelegt. In BB-02 darauf verwiesen.
10.09., 15:30: TW-06 von Cem Arslan eingegangen. Freies Revisionsmaß und örtliche Markierung. Deckenspiegel noch offen.
11.09., 09:15: BW-M-02 erstellt. Gleiche Raumgeometrie, anderer Umgang mit Verschnitt gegenüber Übertragungszeile M-01.
11.09., 14:20: BB-02 abgelegt und an Reinhold geschickt. Nutzerstand bestätigt; kein technisches Freigabeblatt für LV.
14.09., 16:42: Seeger meldet LV Revision 03. Nicht versandt. Drei Seiten.
17.09., 09:05: Nora bittet um Abgleich mit Fundstellen. Termin am 18.09. um 14:00 vorgesehen.
18.09., 08:20: Bis jetzt keine zusätzliche Türzeichnung und kein Deckenspiegel erhalten. Keine telefonische Freigabe von Mertens oder Arslan dokumentiert.
"""
    },
    "csv": {
        "09_Mengenuebertragung.csv": (["Stand", "Quelle", "Bauteil", "Ansatz", "Menge", "Einheit", "Ersteller"], [
            ["02.09.2026", "BW-M-01 Übertragungszeile", "Boden elastisch", "96,00 * 1,10", "105,60", "m²", "Ralf Seeger"],
            ["11.09.2026", "BW-M-02 Abschnitt 1", "Boden elastisch", "43,20 + 28,80 + 24,00", "96,00", "m²", "Nora Küster"],
            ["11.09.2026", "BW-M-02 Abschnitt 2", "Trennwand eine Ansicht", "4,80 * 3,10", "14,88", "m²", "Nora Küster"],
            ["11.09.2026", "BW-M-02 Abschnitt 2", "Trennwand zwei Seiten", "14,88 * 2", "29,76", "m²", "Nora Küster"],
            ["11.09.2026", "BW-M-02 Abschnitt 2", "Sockel", "77,20 - 10,00", "67,20", "m", "Nora Küster"],
            ["14.09.2026", "BW-LV-AU 03 Pos. 06.010", "Flurdecke", "12,00 * 2,00", "24,00", "m²", "Ralf Seeger"],
        ])
    },
    "bilder": [dict(datei="12_Raumschema.png", art="raeume", titel="BW-A-21/02 | Raumschema Erdgeschoss", datum="08.09.2026 | Nora Küster", beschriftung="0.11: 43,20 m² | 0.12: 28,80 m² | 0.10: 24,00 m²", untertitel="Schematische Zuordnung, nicht maßstäblich. Verbindliche Innenmaße im Raumblatt BW-M-02.")],
    "pruefung": [
        "Fundstellen bis zu Fassung, Seite, Abschnitt und LV-Position nachvollziehbar belegen; BB-02 ersetzt BB-01 nur in seinem erklärten Geltungsbereich.",
        "Wandaufbau, Q3/Q2, Linoleum/PVC, Sockelhöhe, T12 und Revisionsöffnungen getrennt erfassen; fehlendes Türblatt und fehlenden Deckenspiegel nicht erfinden.",
        "96,00 m² Einbaufläche und 105,60 m² einschließlich Verschnitt unterscheiden; 14,88 und 29,76 m² sind verschiedene Ansichtsdefinitionen, kein Rechenfehler.",
        "Keine Versand- oder technische Freigabe behaupten und den gewünschten Belegabgleich nicht durch eigenmächtige LV-Neufassung ersetzen.",
    ],
}

AKTEN["bau-rundum-bieterfragen-celle"] = {
    "titel": "Leistungsbeschreibung und Bieterpost zum Lesesaal Finkenstieg in Celle",
    "stand": "2026-09-25",
    "beschreibung": "Öffentliche Bauvergabe einer Lesesaalmodernisierung mit vorläufiger Leistungsbeschreibung, Bestandsdaten, Produktnotiz und später eingegangenen Bieterfragen. Antworten und Berichtigung sind noch nicht erstellt.",
    "dokumente": [
        dokument("02_Vergabedaten.pdf", "Vergabedaten Lesesaal Finkenstieg", "Kommunaler Gebäudeverbund Finkenstieg | Zentrale Beschaffung", "Jana Wendel | Vergabesachbearbeitung", "17.09.2026", "KGF-26-41 / Verfahrensblatt 02",
            """1 Vorhaben

Der Kommunale Gebäudeverbund Finkenstieg beschafft Bauleistungen für die Modernisierung des Lesesaals Finkenstieg 8, 29221 Celle. Gegenstand sind die Erneuerung der Beleuchtung und der zugehörigen Leitungsabschnitte, eine örtliche Deckenergänzung sowie die Inbetriebnahme der Steuerung. Der Gebäudeverbund ist im vorliegenden Verfahren öffentlicher Auftraggeber. Es handelt sich nicht um eine private Angebotseinholung. Verfahrensverantwortlich ist Jana Wendel, technische Projektleiterin ist Daria Schenk.

Die zentrale Beschaffungsstelle hat das Verfahren als öffentliche Ausschreibung nach dem ersten Abschnitt der VOB/A angelegt. Die Prüfung der Verfahrenswahl und der einschlägigen Landesvorgaben liegt in der zentralen Vergabeakte; dieses Blatt ist keine vergaberechtliche Stellungnahme. Eine EU-Bekanntmachung ist in diesem Vorgang nicht angelegt. Es gibt ein Los für die zusammenhängenden Arbeiten im Lesesaal. Nebenangebote sind nach dem vorbereiteten Datenblatt nicht zugelassen.

2 Unterlagen und Kommunikation

Für den vorgesehenen Versand sind LB-02 vom 16.09.2026, Raumbuch RB-03, Bestandsaufnahme EL-B-07, der Ablaufkalender sowie das Formblatt zur Angebotsabgabe vorgesehen. Die Produktnotiz PN-04 ist bisher eine interne Beschaffungsnotiz und nicht als verbindlicher Planerentscheid freigegeben. Daria Schenk prüft die technische Vollständigkeit. Jana Wendel verantwortet die Einstellung in den Projektraum der Vergabeplattform.

Bieterkommunikation erfolgt ausschließlich über den Projektraum KGF-26-41. Technische Mitarbeiter dürfen vor Ort Bestandsmerkmale erläutern, sollen aber keine abweichenden Ausführungszusagen an einzelne Unternehmen geben. Inhaltliche Antworten und Unterlagenänderungen werden von der Beschaffungsstelle geprüft und einheitlich bereitgestellt. Ein mündliches Gespräch ersetzt keine dokumentierte Änderung der Leistungsbeschreibung.

3 Termine

Der interne Vorabcheck ist am 18.09. vorgesehen. Die Freischaltung ist für den 21.09. um 09:00 Uhr geplant. Angebote sollen bis 09.10.2026 um 10:00 Uhr eingehen. Der Termin am 01.10. um 12:00 Uhr ist als organisatorischer Zieltermin für Rückfragen vermerkt, nicht als Zusage, spätere Hinweise auf Unterlagenfehler unbeachtet zu lassen. Ob eine Änderung die Angebotsfrist berührt, entscheidet die Vergabestelle nach Prüfung des konkreten Inhalts.

Jana Wendel | j.wendel@kgf-celle.example"""),
        dokument("03_Leistungsbeschreibung_02.docx", "Leistungsbeschreibung Lesesaal Finkenstieg", "Daria Schenk | Technische Projektleitung KGF", "Zentrale Beschaffung | Jana Wendel", "16.09.2026", "KGF-26-41 / LB-02 / technischer Arbeitsstand",
            """1 Baustelle und Vorhaltung

Die Arbeiten finden im Lesesaal im Erdgeschoss Finkenstieg 8 in Celle statt. Der Saal hat eine Grundfläche von 144,00 m². Die benachbarte Ausleihe bleibt werktags geöffnet. Der Zugang für Personal und Material erfolgt über den Hof. Der Auftragnehmer schützt die bestehenden Regale und die angrenzende Ausleihe gegen Staub und Beschädigung. Mobile Regale im Saal werden vor Beginn durch den Nutzer verschoben; an die Wand geschraubte Regale verbleiben im Raum.

Position 01.010 umfasst das Einrichten, Vorhalten und Räumen der erforderlichen Arbeitsbereiche und Abdeckungen für die gesamte Ausführungszeit. Die Baustelle kann tagsüber betrieben werden. Geräuschintensive Arbeiten sind mit dem Nutzer abzustimmen. Menge: 1 pauschal. Einen festen Zeitkorridor für Bohrungen nennt diese Position nicht. Der Ablaufkalender ist bei der Einsatzplanung zu berücksichtigen.

Position 01.020 umfasst den Ausbau und die fachgerechte Entsorgung der vorhandenen Rasterleuchten einschließlich Leuchtmittel. Im Raumbuch sind 36 Leuchten aufgeführt. Menge in dieser Position: 32 Stück. Die betroffenen Stromkreise sind vor Beginn der Arbeiten durch die ausführende Elektrofachkraft zu sichern. Der Bestand in der Ausleihe bleibt in Betrieb und wird nicht mit ausgebaut.

2 Neue Beleuchtung

Position 02.010 umfasst die Lieferung und betriebsfertige Montage von LED-Einbauleuchten, Fabrikat Lichtkontur, Typ Lesa 420, oder gleichwertig. Die Leuchten werden in die vorhandene Rasterdecke eingesetzt. Gehäuse weiß, Lichtfarbe 4.000 K, Anschlussleistung höchstens 30 W. Eine Gleichwertigkeit ist mit Produktunterlagen darzustellen. Abmessungen, Lichtstrom und Blendungsbegrenzung werden in dieser Position nicht beziffert. Menge: 36 Stück.

Die Lichtverteilung muss für die vorhandenen Leseplätze geeignet sein. Eine projektspezifische lichttechnische Berechnung ist vor Bestellung vorzulegen. Der Auftraggeber hat noch keine Produktbemusterung freigegeben. Eine gelieferte Produktserie darf nicht allein aufgrund ihrer Typbezeichnung als technisch geeignet betrachtet werden.

Daria Schenk | LB-02, Seite 1""",
            """3 Steuerung und Leitungen

Position 02.020 umfasst die Steuerung der Leuchten über eine zentrale Bedienstelle am Eingang und die Anbindung an die vorhandene Steuerung. Das System ist passend zum Bestand auszuführen. Die Leuchten müssen dimmbar sein. An der Bedienstelle sind drei Szenen abzurufen: Reinigung, Lesebetrieb und Veranstaltung. Die genauen Helligkeitswerte werden bei der Inbetriebnahme mit dem Nutzer festgelegt. Menge: 1 Anlage.

Position 02.030 umfasst neue Leitungsabschnitte von den vorhandenen Abzweigstellen zu den neuen Leuchten, einschließlich Befestigung und Anschluss. Angesetzt sind 180,00 m. Die Leitungsart und die Zahl zusätzlich benötigter Steueradern werden nach Aufnahme des Bestands festgelegt. Leitungen, die nach Prüfung weiterverwendet werden können, sollen erhalten bleiben. Der Bestandsbericht EL-B-07 ist zu beachten; ein vollständig geöffnetes Leitungsnetz liegt nicht vor.

Position 02.040 umfasst die erforderlichen Anpassungen im vorhandenen Unterverteiler UV-L. Freie Platzreserven sind vorhanden. Der Auftragnehmer prüft die Eignung vor Ausführung und dokumentiert die vorgenommenen Änderungen. Menge: 1 pauschal. Ein neuer Verteiler ist nicht ausgeschrieben. Die Anlage in der Ausleihe darf außerhalb der abgestimmten Abschaltzeiten nicht außer Betrieb gesetzt werden.

4 Decke

Position 03.010 umfasst das Schließen von vier nicht mehr benötigten Deckenausschnitten mit zum Bestand passenden Platten. Die sichtbare Oberfläche soll sich in Farbe und Raster an den Bestand anpassen. Menge: 4 Stück. Für mögliche zusätzliche Anpassungen infolge abweichender Leuchtenabmessungen enthält das LV keine weitere Position. Neue Leuchten sind in vorhandene Rasterfelder einzubauen; ein vollständiger Deckentausch ist nicht Teil des Auftrags.

Die Deckenplatten dürfen nur in den Arbeitsfeldern aufgenommen werden. Beschädigte Bestandsplatten sind vor Beginn fotografisch zu dokumentieren und dem Auftraggeber anzuzeigen. Der Nutzer weist auf einen alten Wasserfleck im nordöstlichen Randfeld hin. Der Bericht enthält keine Aussage über die Ursache oder den Zustand verdeckter Tragteile.

Daria Schenk | LB-02, Seite 2""",
            """5 Inbetriebnahme und Unterlagen

Position 04.010 umfasst die Inbetriebnahme der neuen Beleuchtung, die elektrische Prüfung durch die Fachfirma und die Einweisung zweier Mitarbeiter des Nutzers. Die Einweisung soll 90 Minuten dauern. Der Auftragnehmer übergibt Stromlaufunterlagen, Produktdaten, eine Beschreibung der programmierten Szenen und das Prüfprotokoll in elektronischer Form. Menge: 1 pauschal. Die elektrische Prüfung ist von einer bloßen Bedienprobe zu unterscheiden.

Für die Abnahme ist ein gemeinsamer Termin vorgesehen. Der Betrieb einer einzelnen Leuchte während der Montage ist keine in dieser Beschreibung vereinbarte Abnahmehandlung. Die Zugänglichkeit der Anschlussstellen ist vor dem Schließen der Rasterdecke zu prüfen. Der Auftragnehmer meldet verdeckte Abweichungen der Projektleitung, bevor darauf aufbauende Arbeiten ausgeführt werden.

6 Ausführung und Nutzerbetrieb

Die Ausführung ist vom 09.11. bis 20.11.2026 vorgesehen. Die Ausleihe bleibt Montag bis Freitag von 09:00 bis 18:00 Uhr geöffnet. Der Lesesaal selbst ist gesperrt; die Verbindungstür zur Ausleihe dient während dieser Zeit nicht als Materialzugang. Der Hofzugang steht von 07:00 bis 17:00 Uhr zur Verfügung. Anlieferungen nach 17:00 Uhr sind nur nach gesonderter Abstimmung möglich.

In der bisherigen Kostenschätzung wurden Montagearbeiten an zehn Werktagen angesetzt. Das ist keine zugesagte tägliche Vollverfügbarkeit jedes Raums. Die Nutzertermine im Ablaufkalender wurden nach Erstellung der Kostenschätzung ergänzt. Die Belegung des Nebenraums am 12.11. und 17.11. ist bei der konkreten Abstimmung zu berücksichtigen. Die dortigen Veranstaltungen werden durch diese Beschreibung nicht abgesagt.

7 Unterlagenstand

Die Leistungsbeschreibung umfasst drei Seiten und trägt den Index 02. Ihr gehen die Raumbuchfassung RB-03 und die Bestandsaufnahme EL-B-07 als eigenständige Unterlagen bei. Die Produktnotiz PN-04 ist eine gesonderte interne Notiz. In dieser Fassung werden keine Bieterfragen beantwortet. Die technische Projektleitung hat den Text am 16.09.2026 an die Beschaffung übergeben.

Daria Schenk | d.schenk@kgf-celle.example"""),
        dokument("04_Raumbuch.pdf", "Raumbuch Lesesaal", "Finja Paulsen | Gebäudedokumentation KGF", "Daria Schenk | Technische Projektleitung", "15.09.2026", "RB-03 / Finkenstieg 8",
            ["""1 Raumaufnahme

Der Lesesaal wurde am 14.09.2026 von Finja Paulsen und Daria Schenk begangen. Die lichte Länge beträgt 12,00 m, die Breite 12,00 m, die Höhe bis Rasterdecke 3,20 m. Die Ausleihe wurde nicht vermessen. An drei Wänden stehen feste Regale; in der Saalmitte gibt es sechs bewegliche Tische mit insgesamt 24 Leseplätzen. Die Rasterfelder sind als 600-mm-Raster angelegt. Das tatsächlich nutzbare Einbaumaß einer Leuchte muss am System geprüft werden.

2 Leuchtenbestand

Bei der Zählung wurden sechs Reihen mit jeweils sechs Leuchten erfasst. Die Reihen sind von West nach Ost als 1 bis 6 bezeichnet. Alle 36 Leuchten waren sichtbar. Vier Leuchten am Nordrand gehören weiterhin zum Lesesaal, obwohl sie in einem älteren Belegungsplan über dem Regalband liegen. Sie wurden nicht als Ausleihe ausgesondert.""",
             tabelle(["Merkmal", "Feststellung", "Quelle"], [["Raumfläche", "144,00 m²", "lichte Maße 12,00 × 12,00 m"], ["Leuchten", "36 Stück", "6 Reihen mit je 6 Stück"], ["Deckenausschnitte ohne Leuchte", "4 Stück", "ehemalige Lautsprecherstellen"], ["Bedienstelle", "1 am Südeingang", "vorhandener Taster; Funktion vor Ort nicht geöffnet"]], [0.28, 0.30, 0.42]),
             """3 Offene Bestandsmerkmale

Die Rasterdecke wurde nur an zwei Stellen angehoben. Typenschild und Schaltgeräte der Leuchten wurden dort nicht vollständig erfasst. Ob sämtliche Bestandsleitungen für die neue Steuerung genutzt werden können, ist aus dieser Aufnahme nicht abzuleiten. Die vier ungenutzten Deckenausschnitte sind keine ausgebauten Leuchten; sie stammen nach Auskunft des Nutzers von früheren Lautsprechern. Ein Austausch von nur 32 Leuchten würde vier Bestandsleuchten im Saal belassen.

Finja Paulsen | erfasst am 15.09.2026, 10:10 Uhr"""]),
        dokument("05_Produktnotiz.docx", "Produktnotiz zur Kostenermittlung", "Daria Schenk | Technische Projektleitung KGF", "Jana Wendel | Zentrale Beschaffung", "08.09.2026", "PN-04 / intern",
            """1 Herkunft der Bezeichnung

Für die vorläufige Kostenermittlung habe ich die Bezeichnung Lichtkontur Lesa 420 aus dem Altprojekt unseres Büros übernommen. Es liegt für den Lesesaal Finkenstieg kein aktuelles Angebot dieses Lieferanten und keine projektspezifische Freigabe vor. Die Typbezeichnung in meiner Notiz ist deshalb keine geprüfte Festlegung der hier erforderlichen Eigenschaften. Ein Herstellerdatenblatt habe ich der Vergabeakte bislang nicht beigefügt.

Die Hausmeister haben von guten Erfahrungen mit der Bedienung der Beleuchtung im Nachbargebäude berichtet. Ich habe daraus zunächst die Produktbezeichnung übernommen, nicht aber einen technischen Nachweis der Anschlussfähigkeit an UV-L. Die Anlagen der beiden Gebäude wurden zu unterschiedlichen Zeiten errichtet. Eine Gleichheit der Steuerung ist nicht nachgewiesen. Insbesondere ist offen, ob die vorhandene Bedienstelle nur einen Schaltkontakt oder einen Steuerbus bedient.

2 Anforderungen aus der Nutzung

Der Lesesaal benötigt eine Beleuchtung für längeres Lesen an den Tischen und für die Reinigung. Der Nutzer möchte zusätzlich eine gedimmte Veranstaltungsszene. In meiner Skizze stehen 4.000 K und maximal 30 W je Leuchte. Ein erforderlicher Lichtstrom je Leuchte, eine Blendungsbegrenzung und die Nachweise für die konkrete Raumgeometrie sind noch nicht in Zahlen beschrieben. Die fehlenden Angaben lassen sich nicht zuverlässig durch einen Produktnamen ersetzen.

Die Einbauleuchten müssen zur vorhandenen Rasterdecke passen. Ein vollständiger Deckenaustausch war im Budgetansatz nicht enthalten. Für Alternativprodukte müssen wir daher noch festhalten, welche geometrischen und funktionalen Eigenschaften zu erfüllen sind und welche Unterlagen die Prüfung ermöglichen. Ich habe hierfür noch keine abschließende Merkmalsliste unterschrieben.

3 Weitergabe

Bitte behandeln Sie diese Notiz als Herkunftsnachweis meines Kostenansatzes. Sie ist nicht zur Übersendung als Bieterantwort formuliert. Vor einer verbindlichen technischen Festlegung möchte ich die Bestandsergebnisse und die Nutzervorgaben nebeneinanderlegen. Eine vergaberechtliche Begründung für eine Beschränkung auf ein Fabrikat enthält diese Notiz nicht.

Daria Schenk | 08.09.2026, 16:00 Uhr"""),
        dokument("06_Bestandsaufnahme.pdf", "Bestandsaufnahme Unterverteiler und Bedienstelle", "Erik Tamm | Fachplanung Strompfad", "Daria Schenk | Technische Projektleitung KGF", "15.09.2026", "EL-B-07 / Ortstermin 14.09.2026",
            """1 Besichtigung

Am 14.09.2026 von 07:30 bis 08:40 Uhr habe ich mit Hausmeisterin Anke Freese den Unterverteiler UV-L und zwei geöffnete Rasterfelder im Lesesaal angesehen. Die Ausleihe wurde währenddessen nicht abgeschaltet. Die Aufnahme war eine begrenzte Bestandsbesichtigung, keine wiederkehrende elektrische Prüfung. Wir haben keine Leiter unter Spannung umgeklemmt und keine Leitungswege vollständig verfolgt.

Im Verteiler sind sechs unbestückte Teilungseinheiten sichtbar. Daraus folgt allein noch nicht, dass jede denkbare Steuerung ohne weitere Anpassung eingebaut werden kann. Die Wärmebelastung, Absicherung und Anschlussbedingungen wurden bei diesem Termin nicht für eine neue Anlage berechnet. Ein vollständiger aktueller Stromlaufplan konnte im Hausmeisterraum nicht gefunden werden.

2 Bedienstelle

Am Südeingang sitzt ein Taster mit zwei Wippen. Nach Angabe von Frau Freese lässt sich damit bislang nur ein- und ausschalten. Hinter der Abdeckung sind an der zugänglichen Stelle zwei angeschlossene Leiter erkennbar. Eine eindeutige Typkennzeichnung des dortigen Geräts wurde nicht aufgenommen. In einem alten Plan ist daneben handschriftlich „Dimmen später“ notiert. Das belegt keine tatsächlich vorhandene Busleitung.

Oberhalb der zwei geöffneten Deckenfelder liegen Leitungen in unterschiedlichen Trassen. Eine Aderzahl wurde nicht für alle Abgänge festgestellt. Die pauschale Annahme, die neue dimmbare Anlage könne ohne zusätzliche Steuerleitung angeschlossen werden, kann ich aus diesem Termin nicht bestätigen. Ebenso wenig kann ich schon sagen, dass sämtliche vorhandenen Leitungen ersetzt werden müssen.

3 Nächster Fachtermin

Vor der abschließenden Ausführungsplanung ist eine gezielte Aufnahme bei abgestimmter Abschaltung erforderlich. Dafür schlage ich den 28.09. von 07:00 bis 08:30 Uhr vor. Der Nutzer hat den Termin noch nicht bestätigt. Änderungen der Leistungsbeschreibung müssen danach anhand der tatsächlichen Erkenntnisse geprüft werden; dieser Bericht legt kein bestimmtes Steuerungsprotokoll fest.

Erik Tamm | e.tamm@strompfad.example"""),
        dokument("13_Ablaufkalender.pdf", "Betriebszeiten während der Lesesaalarbeiten", "Anke Freese | Hausdienst Finkenstieg", "Daria Schenk | Technische Projektleitung", "17.09.2026", "KGF-26-41 / NK-02",
            """1 Regelbetrieb

Die Ausleihe bleibt während der vorgesehenen Arbeiten vom 09.11. bis 20.11.2026 werktags von 09:00 bis 18:00 Uhr geöffnet. Der Lesesaal wird in dieser Zeit für Besucher geschlossen. Der Hof kann für Anlieferungen von 07:00 bis 17:00 Uhr genutzt werden. Die Zufahrt ist 3,20 m breit. Eine dauerhafte Lagerung auf dem markierten Rettungsweg im Hof ist nicht vorgesehen. Einen abschließbaren Lagerraum können wir nur mit 8 m² im Erdgeschoss anbieten.

2 Veranstaltungen

Am 12.11. und 17.11. finden im Nebenraum jeweils von 10:00 bis 13:00 Uhr bereits gebuchte Lesungen statt. Dabei stören Bohr- und Stemmarbeiten im Lesesaal erheblich. Aus Nutzersicht sollen solche Arbeiten an diesen beiden Tagen vor 09:30 Uhr oder nach 13:30 Uhr liegen. Ob die Ausschreibung diese Zeitfenster verbindlich vorgibt, muss die Projektleitung mit der Vergabestelle abstimmen. Der Hausdienst kann die Veranstaltungen nicht eigenständig absagen.

Für gewöhnliche Montage ohne erhebliche Geräuschentwicklung bestehen diese besonderen Veranstaltungsfenster nicht. Die erforderlichen Stromabschaltungen müssen wir jedoch gesondert abstimmen, weil Ausleihterminals und Eingangsbeleuchtung nicht unbemerkt ausfallen dürfen. Im Kalender ist bisher kein Abschalttermin während der Ausführungszeit bestätigt.

3 Zugang und Einrichtung

Die beweglichen Tische und Regale im Lesesaal werden bis 06.11. nachmittags durch den Nutzer zur Seite gestellt. Die fest verschraubten Wandregale bleiben stehen. Der Hausdienst kann keine Hubarbeitsbühne stellen. Die Höhe bis Decke beträgt im Saal 3,20 m. Vor Arbeitsbeginn erfolgt die Schlüsselübergabe an eine benannte verantwortliche Person des Auftragnehmers. Eine tägliche Öffnung vor 07:00 Uhr ist bislang nicht zugesagt.

Dieser Kalender wurde am 17.09. um 11:45 Uhr an Frau Schenk übermittelt. Er ist gegenüber NK-01 um die beiden Lesungstermine ergänzt. Der Ausführungszeitraum selbst wurde nicht verändert.

Anke Freese | a.freese@kgf-celle.example"""),
        dokument("14_Nutzernotiz.docx", "Bedienung des Lesesaals", "Livia Berg | Leitung Lesesaal Finkenstieg", "Daria Schenk | Technische Projektleitung", "18.09.2026", "KGF-26-41 / Nutzervermerk 05",
            """1 Alltag

Sehr geehrte Frau Schenk, die Beschäftigten möchten die neue Beleuchtung ohne Tablet und ohne Anmeldung an einem Benutzerkonto bedienen können. Die vorhandene Stelle am Südeingang ist für uns richtig gelegen. Wir benötigen gut erkennbare Tasten für normalen Lesebetrieb, Reinigung und eine reduzierte Beleuchtung bei Vorträgen. Die Helligkeit im Vortragsbetrieb möchten wir bei einer gemeinsamen Einweisung ausprobieren, weil die Projektionsfläche an der Nordwand steht.

Die Wünsche beschreiben die Bedienung aus Nutzersicht. Ob die vorhandene Verkabelung dafür ausreicht, können wir nicht beurteilen. Herr Tamm hat die Wandstelle angesehen und wollte für die weitere Aufnahme nochmals kommen. Ein bestimmtes Steuerungssystem oder Fabrikat haben wir nicht ausgewählt. Die Bezeichnung Lesa 420 war mir bis zu Ihrer Kostennotiz nicht bekannt.

2 Bestand und Reinigung

In den letzten Monaten wurden einzelne Leuchtmittel ersetzt. Die vier Leuchten über dem nördlichen Regalband gehören weiterhin zum Saal. Sie sollen aus unserer Sicht nicht als Altbestand stehen bleiben. Über dem Regalband ist das Reinigen schwierig; der Abstand zum oberen Regalboden beträgt nur ungefähr 80 cm. Die Montagefirma muss hierfür geeignete Arbeitsmittel mitbringen. Wir können die fest verschraubten Regale nicht vor Beginn abnehmen.

3 Einweisung

Für die Einweisung stehen Livia Berg und Hausmeisterin Anke Freese zur Verfügung. Ein Termin am 20.11. ist grundsätzlich möglich, aber noch nicht fest bestätigt. Wir benötigen die Bedienbeschreibung auch als ausdruckbare Datei für den Hausmeisterordner. Die Dokumentation soll die tatsächlich programmierten Szenen benennen; eine allgemeine Herstellerbroschüre ohne Bezug auf unsere Bedienstelle reicht uns im Betrieb nicht.

Die beiden Lesungen im Nebenraum bleiben gebucht. Bitte stimmen Sie eine Änderung der Bauzeiten mit uns ab, bevor wir Einladungen zurücknehmen. Von einer verlängerten Schließung des Lesesaals wissen wir bislang nichts.

Mit freundlichen Grüßen
Livia Berg | l.berg@kgf-celle.example"""),
    ],
    "mails": [
        mail("01_Vorabpruefung.eml", "Jana Wendel <j.wendel@kgf-celle.example>", "Daria Schenk <d.schenk@kgf-celle.example>", "2026-09-18T08:10:00+02:00", "KGF-26-41: Leistungsbeschreibung vorab durchsehen",
             """Sehr geehrte Frau Schenk,

bitte sehen Sie die Leistungsbeschreibung vor der vorgesehenen Veröffentlichung auf unklare Angaben und Produktvorgaben durch. Ich brauche für die Abstimmung die konkrete Stelle und die fehlende Information, nicht bereits eine stillschweigend geänderte Angebotsgrundlage. Die Produktnotiz liegt intern bei; sie gehört bislang nicht zum veröffentlichten Paket.

Die Mengen im Raumbuch und die Anforderungen an die Steuerung verdienen einen Blick. Ich möchte keine nur scheinbar genaue Antwort weitergeben, solange Herr Tamm den Bestand nicht abschließend kennt. Bitte kennzeichnen Sie Fragen, die wir technisch klären müssen. Eine Rechtsprüfung oder eine Freigabe durch Sie allein ist nicht beauftragt.

Unsere interne Runde ist heute um 14:00 Uhr. Danach entscheide ich mit der zuständigen Leitung über das weitere Vorgehen. Bitte versenden Sie keine Unterlagen an mögliche Bieter. Den Schriftverkehr führe ich über den Projektraum, damit alle Unternehmen denselben Stand erhalten.

Mit freundlichen Grüßen
Jana Wendel
Zentrale Beschaffung"""),
        mail("07_Bieterfrage_Mengen.eml", "Pia Kröger <p.kroeger@stromfeld.example>", "Vergabestelle KGF <vergabe@kgf-celle.example>", "2026-09-22T10:12:00+02:00", "KGF-26-41 / Frage 1 / Anzahl Leuchten",
             """Sehr geehrte Damen und Herren,

wir bearbeiten das veröffentlichte Paket V01 vom 21.09.2026. In Position 01.020 sollen 32 Leuchten ausgebaut werden, während Position 02.010 36 neue Leuchten enthält. Das Raumbuch nennt sechs Reihen mit jeweils sechs Bestandsleuchten. Sollen vier alte Leuchten weiterverwendet werden oder sind alle 36 auszubauen? Die vier Deckenergänzungen in Position 03.010 können wir anhand der Raumbuchbeschreibung nicht als Leuchtenausbau zuordnen.

Bitte teilen Sie außerdem mit, ob das nördliche Regalband zu dem vollständig zu erneuernden Bereich gehört. Für ein Angebot müssen wir wissen, ob Demontage, Entsorgung und Montage dort enthalten sind. Die Arbeit über den feststehenden Regalen benötigt bei uns einen anderen Aufwand als die frei zugänglichen Felder.

Wir bitten um eine im Projektraum bereitgestellte Klarstellung der betroffenen Mengen. Wir haben bisher kein Angebot abgegeben und kalkulieren keine zusätzliche Menge ohne eindeutige Vorgabe. Eine Besichtigung allein würde den Widerspruch zwischen den Textstellen für uns nicht auflösen.

Mit freundlichen Grüßen
Pia Kröger
Stromfeld Ausbau GmbH"""),
        mail("08_Bieterfrage_Fabrikat.eml", "Moritz Runge <m.runge@hellpfad.example>", "Vergabestelle KGF <vergabe@kgf-celle.example>", "2026-09-23T08:47:00+02:00", "KGF-26-41 / Frage 2 / Leuchte und Gleichwertigkeit",
             """Sehr geehrte Damen und Herren,

in Position 02.010 ist Lichtkontur Lesa 420 oder gleichwertig genannt. Uns fehlt eine Liste der maßgeblichen Eigenschaften, anhand derer Sie die Gleichwertigkeit beurteilen wollen. Sind neben 4.000 K und höchstens 30 W ein bestimmter Lichtstrom, eine Blendungsbegrenzung oder bestimmte Abmessungen verbindlich? Welcher Nachweis soll bereits mit dem Angebot vorliegen, welcher erst vor Bestellung?

Unser vorgesehenes Alternativprodukt hat andere Gehäuseaußenmaße als die uns bekannte Leuchte mit ähnlicher Bezeichnung. Im Raumbuch steht ein 600-mm-Raster, jedoch kein freies Einbaumaß. Müssen wir etwaige Anpassungen der Rasterdecke mit anbieten oder ist eine ohne Anpassung passende Leuchte erforderlich? Ein aktuelles Datenblatt des benannten Produkts finden wir in V01 nicht.

Die Frage betrifft aus unserer Sicht die gemeinsame Kalkulationsgrundlage. Wir bitten nicht um eine individuelle Vorabzulassung unseres Fabrikats, sondern um die für alle geltenden Merkmale. Technische Unterlagen können wir nach Festlegung der Anforderungen beifügen.

Mit freundlichen Grüßen
Moritz Runge
Hellpfad Elektrotechnik GmbH"""),
        mail("09_Bieterfrage_Steuerung.eml", "Sibel Hartung <s.hartung@schaltgarten.example>", "Vergabestelle KGF <vergabe@kgf-celle.example>", "2026-09-24T13:26:00+02:00", "KGF-26-41 / Frage 3 / Steuerung und Bohrzeiten",
             """Sehr geehrte Damen und Herren,

die Position 02.020 verlangt eine zum Bestand passende Steuerung mit drei Szenen. Im Bestandsbericht EL-B-07 ist das vorhandene System jedoch nicht identifiziert. Dürfen wir eine neue eigenständige Steuerung kalkulieren, oder müssen wir ein bestimmtes vorhandenes Protokoll anbinden? Bitte nennen Sie die für die Leitungsposition maßgebliche Aderzahl beziehungsweise die funktionale Abgrenzung der neu zu liefernden Leitungen.

Eine zweite Frage betrifft Position 01.010. Dort sind Arbeiten tagsüber vorgesehen, im Ablaufkalender sind für zwei Tage lärmintensive Arbeiten nur außerhalb der Veranstaltungen erwünscht. Gelten die genannten Zeitfenster verbindlich für die Angebotskalkulation? Bitte stellen Sie klar, ob Abschaltungen während der Öffnungszeit der Ausleihe zulässig sind und wer die dafür notwendigen Termine abstimmt.

Wir haben keine eigene Bestandsöffnung vorgenommen. Unsere Kalkulation kann daher weder eine vorhandene Busleitung noch eine vollständige Neuverkabelung voraussetzen. Sofern sich die Angaben nach dem Fachtermin ändern, benötigen wir die aktualisierten Unterlagen mit einheitlichem Versionsstand.

Mit freundlichen Grüßen
Sibel Hartung
Schaltgarten Anlagenbau GmbH"""),
        mail("15_Bieterpost_buendeln.eml", "Jana Wendel <j.wendel@kgf-celle.example>", "Daria Schenk <d.schenk@kgf-celle.example>", "2026-09-25T09:00:00+02:00", "KGF-26-41: Eingegangene Fragen für die gemeinsame Antwort",
             """Sehr geehrte Frau Schenk,

inzwischen liegen drei Bieternachrichten vor. Bitte bündeln Sie die angesprochenen Themen und bereiten Sie einen Antwortentwurf für die Veröffentlichung an alle Bieter vor. Ich brauche neben dem Entwurf die Zuordnung, welche Punkte lediglich erläutert werden können und wo wir erst die Beschreibung oder Mengen ändern müssten. Offene technische Angaben dürfen im Entwurf nicht durch Annahmen ersetzt werden.

Die Vorabprüfung vom 18.09. ist noch nicht als abgeschlossener Prüfvermerk in unserer Ablage. Das Paket V01 ging am 21.09. mit LB-02 unverändert online. Eine Mitteilung V02 oder eine beantwortete Bieterfrage gibt es bisher nicht. Bitte behandeln Sie die drei Absender gleich und nehmen Sie keine individuelle Produktfreigabe in eine Antwort auf.

Herr Tamms ergänzender Ortstermin ist weiterhin nicht bestätigt. Sobald uns das Ergebnis vorliegt, prüfen wir auch, ob die Angebotsfrist angepasst werden muss. Ein Versand oder eine Veröffentlichung durch Sie ist mit dieser E-Mail nicht beauftragt. Ich werde die abgestimmte Fassung über den Projektraum bereitstellen.

Mit freundlichen Grüßen
Jana Wendel"""),
    ],
    "texte": {"10_Projektpostfach.txt": """Kommunaler Gebäudeverbund Finkenstieg | Projektraum KGF-26-41
Export von Jana Wendel, 25.09.2026, 08:45 Uhr. Zeitzone Europe/Berlin.

21.09.2026 09:00: Paket V01 freigeschaltet. Enthalten: LB-02 vom 16.09., RB-03 vom 15.09., EL-B-07 vom 15.09., NK-02 vom 17.09., Angebotsformblatt. Keine PN-04. Dateiinhalte gegenüber internem Stand unverändert.
22.09.2026 10:12: Nachricht Q-001, Stromfeld Ausbau, Menge Ausbau und Nordregal. Eingang im Projektraum. Export als 07_Bieterfrage_Mengen.eml.
23.09.2026 08:47: Nachricht Q-002, Hellpfad Elektrotechnik, Gleichwertigkeit und Deckenraster. Export als 08_Bieterfrage_Fabrikat.eml.
24.09.2026 13:26: Nachricht Q-003, Schaltgarten Anlagenbau, Steuerung und Arbeitsfenster. Export als 09_Bieterfrage_Steuerung.eml.
24.09.2026 16:10: Hausdienst telefonisch wegen Ortstermin am 28.09. angefragt. Keine Bestätigung im Projektraum.
25.09.2026 08:45: Keine Antwort veröffentlicht. Keine Unterlagenrevision V02 hochgeladen. Angebotsfrist in der Plattform weiterhin 09.10.2026, 10:00 Uhr.

Der Export bildet den Posteingang ab. Namen der fragenden Unternehmen sind in diesem internen Export sichtbar; über die Fassung einer Veröffentlichung entscheidet die Vergabestelle. Es besteht keine private Zusage an einen der Absender.
"""},
    "csv": {"11_Leuchtenzaehlung.csv": (["Reihe", "Lage", "Bestand_Stück", "Zähldatum", "Erfasserin", "Bemerkung"], [
        ["1", "West", "6", "2026-09-14", "Finja Paulsen", "vollständig sichtbar"], ["2", "westliche Mitte", "6", "2026-09-14", "Finja Paulsen", "vollständig sichtbar"], ["3", "Mitte", "6", "2026-09-14", "Finja Paulsen", "vollständig sichtbar"], ["4", "Mitte", "6", "2026-09-14", "Finja Paulsen", "vollständig sichtbar"], ["5", "östliche Mitte", "6", "2026-09-14", "Finja Paulsen", "Nordfeld über festem Regal"], ["6", "Ost", "6", "2026-09-14", "Finja Paulsen", "Nordfeld über festem Regal"],
    ])},
    "bilder": [dict(datei="12_Leuchtenschema.png", art="leuchten", titel="LS-03 | Lesesaal Finkenstieg | 36 Bestandsleuchten", datum="14.09.2026 | Finja Paulsen", beschriftung="6 Reihen mit jeweils 6 Leuchten | Raum 12,00 × 12,00 m", untertitel="Schematische Bestandsskizze. Keine lichttechnische Berechnung und kein Einbaumaßblatt.")],
    "pruefung": [
        "Vorabprüfung der LB und spätere Bündelung der drei Bieterfragen als zwei zeitlich getrennte Bearbeitungsschritte abbilden.",
        "32/36 Leuchten, Gleichwertigkeitsmerkmale, Rastermaße, Steuerung, Leitungsumfang und Arbeitsfenster mit konkreten Quellen erfassen.",
        "Aus dem Zusatz oder gleichwertig keine automatische Zulässigkeit der Produktvorgabe ableiten; technische Kriterien und vergaberechtliche Prüfung offenlegen.",
        "Entwurf gemeinsamer Antworten von ungeklärten technischen Fakten und nötigen Unterlagenänderungen trennen; weder Veröffentlichung noch Friständerung erfinden.",
    ],
}

AKTEN["bau-rundum-behinderung-soest"] = {
    "titel": "Bauablauf am Werkstattgebäude Schilfrain in Soest",
    "stand": "2026-09-16",
    "beschreibung": "Ein Bauleiterdiktat und zeitnahe Ausführungsbelege zu einer nicht freigegebenen Arbeitsfläche, einem geänderten Öffnungsplan und verfügbaren Ausweicharbeiten. Eine förmliche Anzeige liegt noch nicht vor.",
    "dokumente": [
        dokument("03_Vertrag_Rohbau.docx", "Rohbauauftrag Werkstatt Schilfrain", "Werkraum Schilfrain GmbH | Geschäftsführerin Amelie Reuter", "Massivbau Dammert GmbH | Geschäftsführer Stefan Lück", "24.08.2026", "SR-26 / RB-01 / Vertragsausfertigung",
            """1 Leistung und Vertragsunterlagen

Die Werkraum Schilfrain GmbH, Schilfrain 19, 59494 Soest, beauftragt die Massivbau Dammert GmbH, Feldbogen 6, 59494 Soest, mit dem Rohbau des eingeschossigen Werkstattgebäudes. Vertragsgrundlagen sind dieser Auftrag, das Angebot MD-26108 vom 18.08.2026, das LV RB-07 und die VOB/B Ausgabe 2016. Diese Unterlagen sind beiden Parteien bei Unterzeichnung ausgehändigt worden. Der Auftrag umfasst Fundamente, Bodenplatte, Stahlbetonwände und die im LV beschriebenen Öffnungen; die technische Fachplanung wird durch die Auftraggeberin gestellt.

Die Auftragssumme auf Grundlage der ausgeschriebenen Mengen beträgt 286.400,00 EUR netto zuzüglich 54.416,00 EUR Umsatzsteuer, insgesamt 340.816,00 EUR brutto. Die Abrechnung erfolgt nach ausgeführten Mengen und vereinbarten Einheitspreisen. Über Nachträge wird nur aufgrund einer gesonderten nachvollziehbaren Beschreibung entschieden. Dieser Vertrag vereinbart keine pauschale Vergütung für ungeklärte spätere Störungen.

2 Mitwirkung und Freigaben

Die Auftraggeberin stellt die abgestimmten Schal- und Bewehrungspläne rechtzeitig vor den betreffenden Arbeiten bereit. Im Bereich der Technikrinne unter der Bodenplatte verlegt ihr gesonderter Auftragnehmer Rohrsteg Haustechnik die Leitungen. Die Rohrlage und der Abschluss seiner Arbeiten sind vor dem darüberliegenden Bewehrungseinbau gemeinsam zu prüfen. Eine Überdeckung ohne die erforderliche technische Kontrolle ist nicht vorgesehen.

Für den Schriftverkehr über Ausführung und Termine ist die Auftraggeberin unter bau@werkraum-schilfrain.example erreichbar. Eine Kopie geht an die Objektüberwachung. Fachplanerin oder Objektüberwachung dürfen technische Abläufe koordinieren; rechtsgeschäftliche Vereinbarungen über Vergütungsänderungen oder geänderte Vertragstermine trifft Amelie Reuter. Die Vertragsparteien benennen damit Ansprechpartner, ohne die Wirksamkeit einzelner künftiger Erklärungen vorwegzunehmen.

3 Termine

Arbeitsbeginn ist der 31.08.2026. Der Rohbau soll bis 30.10.2026 fertiggestellt werden. Der von den Parteien bestätigte Detailablauf RB-T-01 vom 25.08. liegt der Koordination zugrunde; seine einzelnen Zwischenansätze sind keine gesondert vereinbarten Vertragsfristen. Die Auftraggeberin und der Auftragnehmer werden erkennbare Abweichungen zeitnah besprechen und die betroffenen Vorgänge dokumentieren.

Amelie Reuter und Stefan Lück | Vertragsbestätigung am 24.08.2026"""),
        dokument("04_Ablauf_01.docx", "Arbeitsfolge Bodenplatte und Wände", "David Kroll | Bauleitung Massivbau Dammert", "Amelie Reuter und Objektüberwachung Petra Simmen", "25.08.2026", "RB-T-01 / bestätigt zur Koordination am 27.08.2026",
            ["""1 Geplanter Ablauf

Die Bodenplatte wird in zwei Feldern hergestellt. Feld West liegt zwischen den Achsen 1 bis 3, Feld Ost zwischen 3 bis 5. Beide Felder sind durch eine geplante Arbeitsfuge getrennt. Das Westfeld ist unabhängig zugänglich. Die Technikrinne quert ausschließlich das Ostfeld zwischen Achsen 4 und 5. Der Kolonnenansatz beträgt fünf Beschäftigte mit acht Anwesenheitsstunden je regulärem Arbeitstag, einschließlich einer halben Stunde Pause.

Die nachstehende Folge geht von fertig verlegten Leitungen in der Technikrinne bis zum 11.09. um 12:00 Uhr und einer anschließenden Kontrolle aus. Die Bewehrung kann im Bereich der Rinne erst danach geschlossen werden. Im übrigen Ostfeld kann sie abschnittsweise vorbereitet werden; eine vollständige Betonage setzt den Abschluss sämtlicher Vorarbeiten im Feld voraus.""",
             tabelle(["Vorgang", "Geplanter Zeitraum", "Abhängigkeit"], [["Westfeld Bewehrung", "07.09. bis 09.09.", "Sauberkeitsschicht vorhanden"], ["Westfeld Betonage", "10.09., 07:00 Uhr", "Kontrolle am 09.09."], ["Ostfeld Bewehrung", "14.09. bis 15.09.", "Technikrinne fertig und kontrolliert"], ["Ostfeld Betonage", "16.09., 07:00 Uhr", "Bewehrung und Öffnungsdetails freigegeben"], ["Wandschalung West", "17.09. bis 18.09.", "technische Freigabe des Westfelds"], ["Wandschalung Ost", "21.09. bis 23.09.", "Ostplatte ausreichend für Folgearbeiten"]], [0.32, 0.27, 0.41]),
             """2 Arbeitsmittel und Ausweichfläche

Die Wandschalung für das Westfeld kommt am 15.09. mittags. Zuvor können an der Westseite Randabschlüsse nachbearbeitet und Schalungsträger sortiert werden. Diese Tätigkeiten bieten nicht für die gesamte Kolonne zwei volle Tage Arbeit. Für das Ostfeld sind Bewehrungsstahl und Abstandhalter ab 11.09. auf der Baustelle verfügbar. Die Betonbestellung wird durch David Kroll abgestimmt.

3 Fortschreibung

Die Vorgänge werden bei Änderungen einzeln fortgeschrieben. Ein verschobener Betontermin wird nicht ohne Prüfung als gleich lange Verschiebung des Rohbauendes übernommen. Die Westarbeiten und Liefermöglichkeiten sind dafür gesondert anzusehen. Die Terminansätze dienen der Ausführungskoordination, nicht einer bereits erklärten Bewertung möglicher Ansprüche.

David Kroll | d.kroll@massivbau-dammert.example"""]),
        dokument("05_Bautagebuch.pdf", "Bautagebuch Bodenplatte", "David Kroll | Massivbau Dammert GmbH", "Baustellenablage SR-26", "15.09.2026, 17:20 Uhr", "BT-12 / Einträge 14. und 15.09.2026",
            """1 Montag 14 September

Arbeitsbeginn 07:00 Uhr. Anwesend: David Kroll, Mehmet Aydin, Ronja Seifert, Benno Schulz und Janis Weber. Gegen 07:10 Uhr war die Technikrinne zwischen Achsen 4 und 5 auf etwa 9 m Länge noch offen. Es lagen zwei Leitungsbündel ohne abschließende Befestigung in der Rinne. Herr Malz von Rohrsteg war vor Ort und sagte, zwei Formstücke fehlten. Einen schriftlichen Fertigtermin nannte er nicht. Petra Simmen kam um 08:05 Uhr.

Bis 08:30 Uhr wurden Lage und freier Arbeitsraum angesehen. Es gab keine Freigabe zum Schließen der Bewehrung über der Rinne. Ab 08:30 Uhr stellten Aydin und Seifert im freien Ostabschnitt Abstandhalter und erste Matten. Schulz und Weber arbeiteten an Randabschalungen im Westen. Kroll koordinierte Lieferung und Planrückfrage. Ab 13:00 Uhr half Schulz im freien Ostabschnitt; Weber räumte weiter im Westen auf. Die Kolonne war bis 16:00 Uhr anwesend, Pause 12:00 bis 12:30 Uhr.

Um 11:18 Uhr erhielt ich von Petra Simmen die Ankündigung eines geänderten Öffnungsplans. Das betraf zwei Durchführungen nahe Achse 5. Der Plan war um 16:00 Uhr noch nicht in unserem Projektraum. Im freien Abschnitt war Bewehrung möglich, im Bereich der Durchführungen nicht abschließend. Das Tagebuch ordnet die heute eingesetzten Stunden Tätigkeiten zu; daraus ergibt sich nicht automatisch eine vergütungsfähige Stillstandszeit.

2 Dienstag 15 September

Beginn 07:00 Uhr mit derselben Kolonne. Die Formstücke wurden laut Rohrsteg um 09:40 Uhr angeliefert. Der Einbau dauerte bis etwa 12:20 Uhr. Frau Simmen führte um 14:30 Uhr eine Sichtkontrolle durch und bat um eine Ergänzung der Halterung. Eine vollständige Freigabe zur Überdeckung lag um 16:00 Uhr nicht vor. Die Wandschalung West kam um 12:45 Uhr; Schulz und Weber entluden und sortierten sie.

Um 10:05 Uhr erreichte uns der Öffnungsplan S-17/04. Ein öffnungsnahes Bewehrungsdetail wurde darin gegenüber S-17/03 verändert. Kroll bat die Tragwerksplanung um Bestätigung, wie mit den bereits vorbereiteten Stäben zu verfahren sei. Um 15:10 Uhr sagte die Disposition des Betonwerks, der alte Termin 16.09., 07:00 Uhr könne nicht beliebig bis zum Vorabend offen gehalten werden. Kroll stornierte ihn um 15:25 Uhr telefonisch. Eine Stornorechnung lag zum Ende des Tages nicht vor.

David Kroll | fortgeschrieben 15.09.2026, 17:20 Uhr"""),
        dokument("06_Lieferbeleg.pdf", "Lieferbeleg Wandschalung West", "Schalgerät Linden GmbH | Disposition Frauke Dorn", "Massivbau Dammert GmbH | Baustelle Schilfrain 19", "15.09.2026, 12:45 Uhr", "Lieferschein SG-26194",
            ["""1 Lieferung

Die nachstehenden Teile wurden am 15.09.2026 mit Fahrzeug SG-18 an die Baustelle Schilfrain 19 in Soest geliefert. Fahrer war Uwe Strack. Ankunft 12:35 Uhr, Beginn Entladung 12:45 Uhr, Ende 13:25 Uhr. Benno Schulz und Janis Weber nahmen die Teile an. Einsetzen und Ausrichten der Schalung sind nicht Leistungen dieser Lieferung.""",
             tabelle(["Teil", "Menge", "Zuordnung"], [["Rahmenelement 2,70 × 0,90 m", "18 Stück", "Wände Westfeld"], ["Rahmenelement 2,70 × 0,60 m", "8 Stück", "Wände Westfeld"], ["Richtstütze", "12 Stück", "Wände Westfeld"], ["Verbindungskiste", "2 Stück", "Zubehör; verschlossen übergeben"]], [0.49, 0.19, 0.32]),
             """2 Zustand und Übernahme

Schulz vermerkte bei der Übernahme zwei verschmutzte Elementrückseiten. Ein Schaden an der Schalhaut wurde beim Entladen nicht festgestellt. Eine vollständige Prüfung sämtlicher Zubehörteile fand während der Entladung nicht statt. Die Teile wurden auf Lagerfläche West abgelegt; der Zugang zur Technikrinne blieb frei. Die Lieferung war für den 15.09. zwischen 12:00 und 14:00 Uhr angekündigt und lag innerhalb dieses Fensters.

3 Mietbeginn

Die vereinbarte Mietzeit beginnt am 15.09.2026. Ein anderer Mietbeginn oder eine kostenfreie Verlängerung ist auf diesem Lieferschein nicht vereinbart. Die Disposition erhielt keine Mitteilung über eine Stilllegung der gesamten Baustelle. Eine Rückholung wurde nicht angefragt. Frau Dorn kann über eine spätere Verlängerung erst nach Mitteilung des tatsächlich benötigten Enddatums entscheiden.

Frauke Dorn | f.dorn@schalgeraet-linden.example. Übernahme durch Benno Schulz am 15.09.2026, 13:25 Uhr in der Lieferablage bestätigt."""]),
        dokument("07_Beton_Disposition.pdf", "Disposition Bodenplatte Ost", "Henning Wilke | Betonwerk Körnig GmbH", "David Kroll | Massivbau Dammert GmbH", "16.09.2026, 08:05 Uhr", "BK-26-883 / Telefonbestätigung",
            """1 Bestellung und Absage

Sehr geehrter Herr Kroll, wir bestätigen den Verlauf unserer Disposition für die Bodenplatte Ost in Soest. Sie hatten am 10.09.2026 eine Lieferung von 42,00 m³ Beton für den 16.09. ab 07:00 Uhr angemeldet. Pumpe und Lieferfolge sollten wir gemeinsam mit Ihnen am Vortag endgültig abstimmen. Am 15.09. um 15:25 Uhr haben Sie den Termin telefonisch abgesagt, weil die Fläche nach Ihrer Mitteilung nicht betonierbereit sei.

Die Absage ist bei uns vor Beladung eingegangen. Es wurde für diese Baustelle kein Beton produziert oder abgefahren. Die von einem anderen Unternehmen gestellte Pumpe haben wir nicht in Ihrem Namen storniert. Etwaige Kosten dieses Unternehmens können wir deshalb weder bestätigen noch beziffern. Über eigene Dispositionskosten haben wir noch keine Rechnung gestellt.

2 Neue Liefermöglichkeit

Unser nächstes derzeit frei planbares Zeitfenster ist Freitag, 18.09.2026, ab 10:00 Uhr. Wir halten es bis heute 12:00 Uhr unverbindlich vor. Für eine feste Bestellung benötigen wir bis dahin Ihre Bestätigung der Betonierbereitschaft, der Menge und des Pumpentermins. Die Menge von 42,00 m³ ist aus der alten Anmeldung übernommen; eine aktualisierte Mengenprüfung haben wir nicht vorgenommen.

Eine Lieferung am Donnerstagmorgen können wir zurzeit nicht zusagen. Falls ein anderer Auftrag ausfällt, melden wir uns, möchten Ihre Bauablaufplanung aber nicht auf diese ungewisse Möglichkeit stützen. Die vorgesehene Lieferdauer am Freitag beträgt bei ungestörter Abnahme etwa vier Stunden. Zufahrt und Standfläche der Pumpe müssen frei sein.

3 Reichweite dieser Bestätigung

Wir kennen weder die Ursache der fehlenden Betonierbereitschaft noch die vertraglichen Termine zwischen Ihnen und Ihrem Auftraggeber. Dieses Schreiben hält ausschließlich Bestell- und Lieferinformationen fest. Eine Übernahme von Kosten oder eine Anerkennung einer Bauzeitverlängerung ist damit nicht verbunden.

Mit freundlichen Grüßen
Henning Wilke | h.wilke@beton-koernig.example"""),
        dokument("11_Ablauf_02.docx", "Wochenplanung ab 16 September", "David Kroll | Massivbau Dammert GmbH", "Polier Mehmet Aydin und Disposition", "16.09.2026, 08:20 Uhr", "RB-T-02 / vorläufiger Kolonnenplan",
            """1 Stand am Mittwochmorgen

Die Technikrinne im Ostfeld ist noch nicht zur Überdeckung freigegeben. Frau Simmen hat für heute 09:30 Uhr einen weiteren Termin angekündigt. Auch die Rückfrage zum Bewehrungsdetail an den geänderten Durchführungen ist noch offen. Der Betontermin von heute 07:00 Uhr ist abgesagt. Eine neue Lieferung für Freitag ab 10:00 Uhr kann bis heute 12:00 Uhr angemeldet werden; Pumpe und Freigaben sind noch nicht bestätigt.

2 Kolonneneinsatz

Aydin und Seifert halten zunächst die vorbereiteten Bewehrungsbereiche im Ostfeld frei und prüfen die für das Änderungsdetail bereits gelieferten Stäbe gegen die neue Liste, ohne Stäbe eigenständig umzubiegen. Schulz und Weber beginnen nach der bereits vorliegenden technischen Freigabe des Westfelds mit dem Sortieren und Vorbereiten der Wandschalung. Kroll nimmt am Termin zur Technikrinne teil und stimmt die Liefermöglichkeiten ab. Die Baustelle ist deshalb nicht insgesamt ohne Arbeit.

Für Donnerstag ist das Stellen der ersten Westwände vorgesehen. Ob gleichzeitig die Ostbewehrung abgeschlossen werden kann, hängt von den noch offenen Rückmeldungen ab. Eine vollständige Verlagerung aller fünf Beschäftigten in die Westwände ist wegen des begrenzten Arbeitsraums heute nicht sinnvoll. Der konkrete Einsatz wird im Tagebuch und in der Stundenliste fortgeschrieben, nicht pauschal als Stillstand eingetragen.

3 Annahmen und Termine

Wenn Rinne und Detail heute freigegeben werden, könnte die Ostbewehrung nach derzeitiger Einschätzung am Donnerstag fertig werden. Das ist eine Arbeitsannahme und keine zugesagte Fertigmeldung. Der mögliche Betontermin am Freitag würde weitere Abstimmung über die anschließenden Wände erfordern. Auswirkungen auf den vertraglichen Rohbautermin 30.10. werden damit noch nicht beziffert. Die vorausgehende Planung RB-T-01 bleibt als Vergleichsstand erhalten.

Diese Wochenplanung geht nur an die Kolonne und die Disposition. Sie ist keine an die Auftraggeberin gerichtete förmliche Erklärung. Bitte tatsächliche Beginn- und Endzeiten weiterhin erfassen und bei einer Freigabe deren Zeitpunkt und Gegenstand notieren.

David Kroll | Stand 16.09.2026, 08:20 Uhr"""),
    ],
    "mails": [
        mail("01_Kroll_Buero.eml", "David Kroll <d.kroll@massivbau-dammert.example>", "Lea Friese <l.friese@massivbau-dammert.example>", "2026-09-16T08:32:00+02:00", "Schilfrain: Diktat und Unterlagen für das Schreiben",
             """Guten Morgen Frau Friese,

ich habe auf dem Weg zum Container die Fakten ins Telefon gesprochen. Die Textübertragung liegt als Datei 02 bei; bitte machen Sie daraus einen Entwurf der förmlichen Behinderungsanzeige an unsere Auftraggeberin. Ich kontrolliere Daten, Ursachen und den tatsächlichen Arbeitsablauf vor dem Versand. Bitte setzen Sie nicht einfach alle Anwesenheitsstunden als Stillstand an. Im Westen arbeiten wir weiter.

Der Vertrag und beide Ablaufstände liegen ebenfalls im Ordner. Das Gespräch mit Frau Simmen ist noch kein von mir versandtes Schreiben. Insbesondere weiß ich nicht, ob Frau Reuter die einzelnen Auswirkungen bereits kennt. Ich möchte einen nachvollziehbaren Text darüber, welche Arbeiten seit wann betroffen sind, was wir trotzdem tun und welche Rückmeldungen wir brauchen. Eine abschließende Forderung über Tage oder Geld kann ich heute nicht freigeben.

Für die Kontaktadresse verwenden Sie bitte die im Vertrag benannte Auftraggeberadresse und nehmen Frau Simmen in Kopie. Senden Sie selbst noch nichts ab. Nach dem Termin um 09:30 Uhr könnte eine Ergänzung erforderlich sein. Der Betonlieferant hält Freitag nur bis heute Mittag vor.

Freundliche Grüße
David Kroll"""),
        mail("08_Simmen_Plan.eml", "Petra Simmen <p.simmen@kontur-bauleitung.example>", "David Kroll <d.kroll@massivbau-dammert.example>", "2026-09-15T10:05:00+02:00", "SR-26: Öffnungsplan S-17 Index 04",
             """Sehr geehrter Herr Kroll,

der Öffnungsplan S-17/04 steht seit 09:55 Uhr im Projektraum. Gegenüber Index 03 sind die beiden Durchführungen bei Achse 5 um jeweils 120 mm nach Norden versetzt. Der Abstand zwischen den Durchführungen bleibt 800 mm. Die ergänzende Bewehrung ist im Detail 6 geändert. Bitte prüfen Sie mit der Tragwerksplanung, ob die bereits zugeschnittenen Stäbe unverändert genutzt werden können; ich erteile hierzu keine statische Freigabe.

Rohrsteg meldet für heute Vormittag die fehlenden Formstücke. Ich komme um 14:30 Uhr zur Technikrinne. Eine Freigabe zur Überdeckung kann ich vor Prüfung des ausgeführten Zustands nicht bestätigen. Ihr Hinweis gestern um 08:05 Uhr ist in meinem Tagesvermerk aufgenommen. Eine von Ihnen an die Auftraggeberin gerichtete förmliche Anzeige ist damit nicht dokumentiert.

Bitte geben Sie den freien Westbereich nicht ungenutzt auf. Die Freigabe des Westfelds für die vorgesehenen Schalungsarbeiten ist Ihnen bereits am 14.09. um 16:10 Uhr mitgeteilt worden. Welche Mannschaftsstärke dort sinnvoll eingesetzt werden kann, stimmen Sie mit Ihrem Polier ab. Zusätzliche Vergütung oder eine Änderung des Vertragstermins sage ich nicht zu.

Mit freundlichen Grüßen
Petra Simmen"""),
    ],
    "texte": {
        "02_Diktat_Kroll.txt": """David Kroll | Massivbau Dammert | Baustelle Schilfrain, Soest
Sprachnotiz am 16.09.2026, 07:48 bis 07:52 Uhr. Textübertragung 08:02 Uhr.

Ich komme gerade von der Ostplatte. Heute ist Mittwoch. Es ist nicht die ganze Baustelle zu, aber über der Technikrinne geht es noch nicht. Das war Montag schon so. Wir waren um sieben da, um zehn nach sieben stand ich an der Rinne. Rohrsteg hatte zwei Bündel drin, aber die Formstücke fehlten und die Befestigungen waren nicht fertig. Ich habe mit Malz gesprochen, Simmen kam kurz nach acht. Sie hat nicht gesagt, wir dürften zudecken.

Ich hatte am Montag fünf Leute einschließlich mir. Aydin und Seifert konnten die Matten daneben anfangen. Schulz und Weber haben im Westen weitergemacht. Nach Mittag ging Schulz nach Osten. Also bitte nicht schreiben, fünf Leute standen zwei Tage herum. Was in welcher Stunde war, steht in der Liste, ich habe sie gestern noch korrigiert. Die Pausen sind extra.

Dann noch der Plan. Montag sagte Simmen, die Öffnungen müssten anders liegen. Den neuen Plan habe ich Dienstag um zehn nach fünf bekommen, nein, zehn Uhr fünf morgens. Index vier. Zwei Öffnungen 120 Millimeter weiter nach Norden, Detail sechs anders. Dafür brauche ich noch die Bestätigung von der Statik, ob unser geschnittener Stahl passt. Das ist nicht dasselbe wie die offene Rinne. Beides hält jetzt die Fertigstellung des Ostfelds auf.

Gestern Nachmittag war Rohrsteg fertig mit Einsetzen, aber Simmen wollte noch eine Halterung mehr. Sie kommt heute halb zehn. Ich weiß also nicht, wann wir wirklich freikommen. Beton heute um sieben habe ich gestern um 15:25 abgesagt. Wilke hat Freitag zehn Uhr angeboten, aber nur vorläufig. Eine Rechnung für die Absage habe ich nicht. Die Pumpe muss ich noch separat anrufen.

Die Westschalung kam gestern 12:45. Damit können zwei Leute arbeiten, vielleicht nachher drei, das muss Aydin sehen. Es fehlt nicht an allem Material. Den Rohbautermin Ende Oktober kann ich jetzt nicht seriös neu berechnen. Erst muss ich wissen, wann der Osten betoniert wird. Bitte im Brief klar sagen, was konkret betroffen ist, und nichts von vier Wochen Verzögerung erfinden. Den Brief muss ich noch ansehen. Frau Reuter hat von mir dazu bislang nur den üblichen Jour-fixe-Kalender, kein Schreiben mit diesen Einzelheiten.
""",
        "12_Telefonnotizen.txt": """Baustelle SR-26 | Notizbuch David Kroll | Stand 16.09.2026, 08:25 Uhr

14.09. 07:18, Gespräch mit Eike Malz/Rohrsteg an der Rinne: zwei Formstücke fehlen. Malz erwartet Nachricht aus Lager, nennt keine Uhrzeit.
14.09. 08:05, Petra Simmen vor Ort: Rinne offen, keine Überdeckung. Hinweis auf Ausweichflächen West. Kein Gespräch mit Amelie Reuter.
14.09. 11:18, Simmen telefonisch: neuer Öffnungsplan in Arbeit, Durchführungen Achse 5. Kein Plananhang zum Telefonat.
14.09. 16:10, Simmen telefonisch: Westfeld für die vorgesehenen Schalungsarbeiten technisch freigegeben. Ostfeld ausdrücklich ausgenommen.
15.09. 14:30, Simmen vor Ort: zusätzliche Halterung in der Rinne erforderlich. Malz hört mit. Keine schriftliche Abschlussbestätigung.
15.09. 15:10, Wilke/Betonwerk: heutige Disposition braucht Entscheidung. Kroll will Rückmeldung zur Rinne abwarten.
15.09. 15:25, Kroll an Wilke: Termin 16.09., 07:00 abgesagt. Noch keine Kosten genannt.
16.09. 07:35, Wilke: 18.09., 10:00 möglich, Rückmeldung bis 12:00. Bestätigung als 07_Beton_Disposition.pdf angekündigt.
16.09. 08:25: Keine E-Mail oder förmliche Anzeige von Kroll an bau@werkraum-schilfrain.example im Ausgang. Entwurf wird angefordert. Dieses Notizbuch bleibt intern.
""",
    },
    "csv": {"09_Stundenliste.csv": (["Datum", "Person", "Anwesenheit_h", "Pause_h", "Ost_freier_Abschnitt_h", "West_Arbeiten_h", "Koordination_Warten_h", "Erfasst_von"], [
        ["2026-09-14", "David Kroll", "9,0", "0,5", "0,0", "0,0", "8,5", "David Kroll"], ["2026-09-14", "Mehmet Aydin", "9,0", "0,5", "7,0", "0,0", "1,5", "David Kroll"], ["2026-09-14", "Ronja Seifert", "9,0", "0,5", "7,0", "0,0", "1,5", "David Kroll"], ["2026-09-14", "Benno Schulz", "9,0", "0,5", "3,0", "4,0", "1,5", "David Kroll"], ["2026-09-14", "Janis Weber", "9,0", "0,5", "0,0", "7,0", "1,5", "David Kroll"],
        ["2026-09-15", "David Kroll", "9,0", "0,5", "0,0", "0,0", "8,5", "David Kroll"], ["2026-09-15", "Mehmet Aydin", "9,0", "0,5", "5,0", "0,0", "3,5", "David Kroll"], ["2026-09-15", "Ronja Seifert", "9,0", "0,5", "5,0", "0,0", "3,5", "David Kroll"], ["2026-09-15", "Benno Schulz", "9,0", "0,5", "0,0", "6,0", "2,5", "David Kroll"], ["2026-09-15", "Janis Weber", "9,0", "0,5", "0,0", "6,0", "2,5", "David Kroll"],
    ])},
    "bilder": [dict(datei="10_Arbeitsfelder.png", art="felder", titel="SR-26 | Arbeitsfelder Bodenplatte | Index 04", datum="15.09.2026 | David Kroll", beschriftung="Westfeld Achsen 1 bis 3 | Ostfeld Achsen 3 bis 5", untertitel="Schematische Lageübersicht. Rinne im Ostfeld; kein Schal- oder Bewehrungsplan.")],
    "pruefung": [
        "Aus Diktat und Belegen erst einen förmlichen Entwurf erstellen; die Akte enthält noch keine bereits versandte Behinderungsanzeige.",
        "Offene Rinne und geändertes Bewehrungsdetail mit jeweils eigenem Beginn, Ursache, Betroffenheit und Nachweis darstellen; Adressat und Zugang vor Versand prüfen.",
        "Ausweicharbeiten West und freie Ostabschnitte berücksichtigen; Koordination und Warten nicht ohne Aufschlüsselung als Stillstand abrechnen.",
        "Keine sichere Verlängerung bis zum Rohbauende, keine ungeprüfte Geldforderung und keine erfundene Freigabe erklären; technische und rechtliche Kontrolle vor Versand vorsehen.",
    ],
}

AKTEN["bau-rundum-baugrund-verden"] = {
    "titel": "Baugrundunterlagen für die Gerätehalle Weidenmaß in Verden",
    "stand": "2026-09-21",
    "beschreibung": "Dreiseitiger geotechnischer Kurzbericht mit zweitseitiger Ergänzung, Feldbelegen, Laborwerten und geändertem Laststand. Kennwerte, Einheiten und räumliche Geltungsgrenzen erfordern projektbezogene Ingenieurprüfung.",
    "dokumente": [
        dokument("02_Baugrundbericht.pdf", "Baugrundbericht Gerätehalle Weidenmaß", "Dr. Jule Hagedorn | Ingenieurgeologie Erdspur", "Weidenmaß Gerätedienst GmbH | Bernd Kessler", "04.09.2026", "EG-26-118 / Bericht 01 / Umfang 3 Seiten",
            """1 Auftrag und untersuchter Entwurf

Die Weidenmaß Gerätedienst GmbH plant eine eingeschossige Gerätehalle am Weidenmaß 7 in 27283 Verden. Grundlage unseres Auftrags vom 14.08.2026 ist der Grundriss WM-A-02 vom 12.08.2026 mit einer Hallenfläche von 18,00 × 24,00 m. Angenommen wurde eine leichte Stahlhalle ohne Kranbahn, ohne Unterkellerung und mit üblichen bodenstehenden Lagerregalen. Einzelne schwere Maschinenfundamente waren nicht Gegenstand der übergebenen Planung. Der Bericht enthält drei Seiten; Feldaufzeichnungen und Laborwerte sind eigenständige Anlagen in der Projektablage.

2 Aufschlüsse und Höhen

Am 26.08.2026 wurden drei Kleinbohrungen KB1 bis KB3 bis 5,00 m unter jeweiligem Gelände und zwei leichte Rammsondierungen ausgeführt. Die Aufschlüsse liegen im westlichen und mittleren Hallenbereich. Ein östlicher Streifen war wegen abgestellter Geräte nicht zugänglich. Die Lageübersicht WM-G-01 zeigt diese Lücke. Die Höhen wurden auf den örtlichen Projektfestpunkt mit 20,00 m bezogen. Dieser Festpunkt ist kein amtlich überprüfter Höhenanschluss. Zahlen dürfen deshalb nicht ohne weiteren Nachweis als Höhen über NHN verwendet werden.

Die Ansatzhöhen betragen bei KB1 20,16 m, bei KB2 20,08 m und bei KB3 19,98 m im örtlichen System. Die geplante Oberkante Fertigfußboden beträgt nach WM-A-02 20,30 m. Die Aufschlusstiefen werden in den Feldblättern ab Ansatzpunkt angegeben. Eine Tiefe von 1,20 m unter Gelände ist daher nicht dasselbe wie eine feste Höhenkote von 19,10 m.

3 Schichten

Unter einer 0,20 bis 0,30 m starken Oberbodenschicht wurde sandige Auffüllung mit einzelnen Ziegelstücken angetroffen. Die Unterkante der Auffüllung lag bei KB1 0,80 m, bei KB2 1,00 m und bei KB3 1,20 m unter Gelände. Darunter folgen überwiegend mitteldichte Sande. Bei KB3 ist zwischen 1,20 und 1,60 m eine weiche schluffige Zwischenlage eingeschaltet. Ihre seitliche Ausdehnung ist mit den drei Aufschlüssen nicht belegt. Im unzugänglichen Oststreifen können andere Verhältnisse vorliegen.

Die Ansprache beschreibt die punktuell angetroffenen Schichten. Aus einer Verbindung der Bohrpunkte im Lagebild entsteht kein flächiger Nachweis gleichmäßiger Tragfähigkeit. Für den späteren Aushub sind die tatsächlichen Schichten mit dem beschriebenen Bild abzugleichen.

Dr. Jule Hagedorn | EG-26-118, Seite 1 von 3""",
            ["""4 Vorläufige Kennwerte

Die folgenden Werte sind vorläufige charakteristische Ansätze für die jeweils benannten natürlichen Schichten im untersuchten Bereich. Sie sind keine zulässigen Bodenpressungen und keine bereits abgeleiteten Bemessungswiderstände. Die Auffüllung erhält aufgrund ihrer wechselnden Zusammensetzung keinen einheitlichen Bemessungsansatz. Die Tragwerksplanung muss Lasten, Geometrie, Wasserzustand und Nachweise für die tatsächliche Gründung zusammenführen.""",
             tabelle(["Schicht", "Wichte / unter Auftrieb", "Reibung / Kohäsion", "Steifemodul"], [["Mitteldichter Sand", "19 / 10 kN/m³", "32° / 0 kN/m²", "25 bis 40 MN/m²"], ["Weicher Schluff KB3", "18 / 8 kN/m³", "22° / 3 kN/m²", "3 bis 6 MN/m²"]], [0.24, 0.27, 0.27, 0.22]),
             """5 Wasserbeobachtung

In den Bohrlöchern wurde am 26.08.2026 nach rund 30 Minuten Wasser zwischen 1,65 und 1,80 m unter Gelände beobachtet. Die Beobachtungsdauer war kurz; jahreszeitliche Höchststände sind daraus nicht abzulesen. Für die Vorplanung wird zunächst eine Wasserhöhe von 19,30 m im örtlichen System angesetzt. Das ist eine vorsichtige Arbeitsannahme für den bisherigen Entwurf, kein amtlich oder langjährig abgesicherter Bemessungswasserstand.

Für anstehende Sande wurde aus zwei Laborproben ein Wasserdurchlässigkeitsbereich von 2 × 10^-5 bis 6 × 10^-5 m/s abgeleitet. Der Bereich betrifft die untersuchten Sandproben, nicht die schluffige Lage, die Auffüllung oder das Gesamtgrundstück. Er ist kein Freibrief für eine Versickerungsanlage. Grundwasserhaltung und Einleitung sind eigenständig mit Planung und zuständigen Stellen abzustimmen.

6 Gründung des bisherigen Entwurfs

Für die leichte Halle erscheint nach dem bisherigen Aufschlussbild eine flache Gründung nach Entfernung von Oberboden und nicht tragfähiger Auffüllung grundsätzlich weiter untersuchbar. Ein pauschaler Austausch bis zu einer überall gleichen Tiefe lässt sich aus drei Bohrpunkten nicht ableiten. Die Schlufflage bei KB3 ist unter den betroffenen Gründungsteilen gesondert zu behandeln. Abmessungen und konkrete Nachweise der Fundamente enthält dieser Bericht nicht.

Dr. Jule Hagedorn | EG-26-118, Seite 2 von 3"""],
            """7 Erdarbeiten und Kontrolle

Der Aushub ist so zu führen, dass die Gründungssohle nicht aufgeweicht oder durch Befahren aufgelockert wird. Niederschlagswasser darf sich nicht dauerhaft in offenen Fundamentgruben sammeln. Das konkrete Bauverfahren, die Sicherung von Baugruben und ein erforderliches Wasserhaltungskonzept sind vor Ausführung projektbezogen zu planen. Dieser Kurzbericht enthält keine prüffähige Baugrubenstatik und keine Festlegung einer allgemein sicheren Böschungsneigung.

Vor Einbau eines Ersatzmaterials soll die freigelegte Sohle durch eine geotechnisch fachkundige Person abgenommen und der tatsächliche Schichtverlauf dokumentiert werden. Ersatzmaterial, Einbaudicken und Verdichtungsnachweise müssen zur jeweiligen Gründung und zum Bauverfahren passen. Ein pauschaler Wert aus einer fremden Baustelle ist nicht Bestandteil unserer Empfehlung. Für den derzeit vorgesehenen Hallenboden ist eine abgestimmte Prüffläche zweckmäßig; die endgültigen Abnahmekriterien sind nach Last- und Bodenplattenplanung festzulegen.

8 Auffälligkeiten und Entsorgung

In der Auffüllung wurden Ziegelstücke und örtlich dunkle Schlieren gesehen. Eine chemische Untersuchung ist nicht beauftragt worden. Die vorliegenden Laborwerte betreffen Korngrößen, Wassergehalt und Durchlässigkeit, nicht Schadstoffe. Weder eine abfallrechtliche Einstufung noch die Annahme uneingeschränkter Wiederverwendbarkeit wird mit diesem Bericht erklärt. Für den geplanten Abtransport sind erforderliche Untersuchungen und Annahmebedingungen gesondert zu klären.

9 Grenzen und weitere Abstimmung

Eine Laständerung, tiefere Gründung oder Erweiterung in den nicht aufgeschlossenen Oststreifen erfordert eine erneute fachliche Beurteilung. Bitte legen Sie uns den abgestimmten Lastplan und die Fundamentgeometrie vor, bevor Kennwerte in eine abschließende Bemessung eingehen. Besonders die weiche Zwischenlage kann Setzungsunterschiede verursachen; ihre räumliche Ausdehnung bleibt ohne ergänzende Aufschlüsse offen.

Dieser Bericht umfasst tatsächlich drei Seiten. Die Angaben beziehen sich auf den am 14.08. übergebenen Hallenentwurf und die genannten Untersuchungen. Er enthält weder eine Freigabe zur Ausführung der Fundamente noch eine behördliche Erlaubnis zur Wasserhaltung. Die eigenständigen Feldblätter, Labortabellen und die Lageübersicht bleiben für das Verständnis der einzelnen Werte heranzuziehen.

Dr. Jule Hagedorn | Ingenieurgeologie Erdspur | j.hagedorn@erdspur.example"""),
        dokument("03_Ergaenzung_01.pdf", "Ergänzung zum Baugrundbericht Weidenmaß", "Dr. Jule Hagedorn | Ingenieurgeologie Erdspur", "Mika Ehlers | Tragwerksplanung Pfeilermaß", "18.09.2026", "EG-26-118 / Ergänzung 01 / Umfang 2 Seiten",
            ["""1 Anlass und zusätzlicher Aufschluss

Herr Ehlers hat uns am 11.09. den Laststand WM-L-03 mitgeteilt. Neu vorgesehen sind zwei höher belastete Stützen am Ostrand und ein bodenstehender Maschinensockel. Die geänderten Lasten waren nicht Grundlage unseres Berichts vom 04.09.2026. Am 14.09. konnten wir nach Räumung des Oststreifens KB4 bis 6,00 m unter Gelände ausführen. Die Ansatzhöhe beträgt 20,02 m im unveränderten örtlichen Höhensystem.

An KB4 reicht die Auffüllung bis 1,40 m unter Gelände. Darunter folgt weicher bis örtlich breiiger Schluff bis 2,10 m. Erst darunter wurde mitteldichter Sand erbohrt. Das ergänzt den Bericht insbesondere für den östlichen Hallenteil; die Schichtgrenzen der westlichen Aufschlüsse werden dadurch nicht nachträglich verändert. Eine linienförmige Verbindung von KB3 und KB4 ist weiterhin eine Interpretation und kein flächiger Aufschluss.""",
             tabelle(["KB4", "Tiefe unter Gelände", "Örtliche Unterkante"], [["Oberboden", "0,00 bis 0,25 m", "19,77 m"], ["Auffüllung", "0,25 bis 1,40 m", "18,62 m"], ["Schluff", "1,40 bis 2,10 m", "17,92 m"], ["Sand", "2,10 bis 6,00 m", "14,02 m"]], [0.3, 0.35, 0.35]),
             """2 Geänderte Wasserannahme

Am 14.09. wurde Wasser bei KB4 nach 45 Minuten in 1,10 m Tiefe, entsprechend 18,92 m örtlicher Höhe, beobachtet. In dem provisorischen Beobachtungsrohr stieg es am 16.09. auf 19,08 m. Nach Einbeziehung dieser Beobachtungen erhöhen wir den vorläufigen Wasseransatz für die weitere Projektplanung von 19,30 auf 19,60 m im örtlichen System. Das ist eine geänderte Planungsannahme mit Sicherheitszuschlag, kein gemessener Höchststand. Der bisherige Ansatz aus Bericht 01, Abschnitt 5, soll für die weitere Planung nicht unverändert fortgeschrieben werden.

Dr. Jule Hagedorn | Ergänzung 01, Seite 1 von 2"""],
            """3 Östliche Gründung und Kennwerte

Die Kennwerte für mitteldichten Sand aus Bericht 01 bleiben als vorläufige Ansätze für tatsächlich anstehenden und entsprechend bestätigten Sand verwendbar. Sie dürfen nicht auf den gesamten östlichen Gründungsbereich einschließlich der Auffüllung und des Schluffs übertragen werden. Für die neu erkannte Schluffschicht ist für weitere vergleichende Setzungsbetrachtungen zunächst ein Steifemodul von 2 bis 4 MN/m² anzusetzen. Der frühere Bereich von 3 bis 6 MN/m² bezog sich auf die dünnere Lage bei KB3 und wird dadurch nicht zu einem einheitlichen Grundstückswert.

Für die beiden neuen Stützen und den Maschinensockel reicht die allgemeine Vorbewertung einer flachen Gründung im Bericht nicht aus. Erforderlich sind projektspezifische Nachweise unter Berücksichtigung der tatsächlichen Lastkombinationen, Fundamentabmessungen und gegenseitigen Einflüsse. Als zu untersuchende Varianten kommen ein örtlich angepasster Bodenaustausch oder eine Lastabtragung in tiefere geeignete Schichten in Betracht. Wir haben keine Variante abschließend ausgewählt und keine Austauschtiefe freigegeben.

4 Bodenplatte und Erdarbeiten

Die Bodenplatte ist nicht mit den Stützenfundamenten gleichzusetzen. Die vom Nutzer genannte Flächenlast von 20 kN/m² ersetzt weder Stützenlasten noch die konzentrierte Last des Maschinensockels. Für die Bodenplatte sind unterschiedliche Untergrundsteifigkeiten im Übergang West zu Ost zu berücksichtigen. Falls ein Bettungsmodul benötigt wird, ist er aus dem konkreten System herzuleiten; der Steifemodul aus der Tabelle ist nicht zahlenidentisch als Bettungsmodul in MN/m³ einzusetzen.

Bei dem erhöhten Wasseransatz können tiefere Austauschmaßnahmen unter Wasser liegen. Das muss in Bauverfahren, Wasserhaltung und Nachweisen berücksichtigt werden. Eine wasserrechtliche Entscheidung ist nicht Bestandteil dieser Ergänzung. Die chemische Beschaffenheit der Auffüllung bleibt ununtersucht. Die Nachforderung einer chemischen Deklaration wird durch unsere geotechnische Ergänzung nicht erledigt.

5 Fortgeltung und Übergabe

Die Abschnitte 7 und 8 des ursprünglichen Berichts zu Sohlkontrolle, Ausführung und fehlender chemischer Untersuchung bleiben bestehen. Die frühere Annahme einer leichten Halle ohne zusätzliche Sonderlasten beschreibt den neuen Laststand nicht vollständig. Vor einer Ausführung benötigen wir die abgestimmte Fundamentplanung und die prüffähigen Lastangaben. Die heutige Ergänzung umfasst zwei Seiten und ist mit Bericht 01 sowie den Rohdaten zu lesen.

Dr. Jule Hagedorn | 18.09.2026"""),
        dokument("04_Lastmitteilung.docx", "Laststand Gerätehalle Weidenmaß", "Mika Ehlers | Tragwerksplanung Pfeilermaß", "Dr. Jule Hagedorn | Ingenieurgeologie Erdspur", "11.09.2026", "WM-L-03 / Vorbemessung",
            ["""1 Änderungen gegenüber WM-L-02

Sehr geehrte Frau Dr. Hagedorn, der Nutzer hat den geplanten Betrieb am 09.09. ergänzt. Am östlichen Rand sollen zwei Stützen höhere Vertikallasten erhalten. Außerdem ist ein separat auf dem Boden gegründeter Maschinensockel vorgesehen. Die Gebäudeaußenmaße bleiben 18,00 × 24,00 m, die Fußbodenhöhe bleibt 20,30 m im örtlichen System. Eine Kranbahn ist weiterhin nicht vorgesehen.

Die folgenden Werte sind charakteristische Vertikallasten aus der Vorbemessung. Lastkombinationen und Teilsicherheitsbeiwerte sind darin nicht eingerechnet. Horizontallasten und Momente müssen wir Ihnen mit dem abschließenden Fundamentplan nachreichen. Bitte verwenden Sie die Tabelle daher nicht als vollständige prüffähige Lastübergabe.""",
             tabelle(["Bauteil", "Ständige Last Gk", "Veränderliche Last Qk"], [["Stütze Ost 1", "420 kN", "180 kN"], ["Stütze Ost 2", "460 kN", "190 kN"], ["Maschinensockel", "260 kN", "80 kN"], ["Reguläre Stütze West", "210 kN", "90 kN"]], [0.42, 0.29, 0.29]),
             """2 Bodenplatte und Höhen

Für die Bodenplatte liegt als vorläufige Nutzervorgabe eine gleichmäßig verteilte Verkehrslast von 20 kN/m² vor. Das ist keine Bodenpressung eines Stützenfundaments. Der Maschinensockel hat im Vorentwurf 2,40 × 1,80 m Grundfläche. Die Unterkante ist noch nicht festgelegt. Für Einzelfundamente wurde bislang vorläufig 19,10 m örtliche Höhe skizziert. Die Eignung dieser Höhenlage ist anhand Ihrer Ergänzung und unserer Bemessung zu prüfen.

3 Rückfrage

Bitte beurteilen Sie den bislang unzugänglichen Oststreifen gesondert. Wir benötigen eine Aussage darüber, welche Schichten dort für die weiteren Nachweise angesetzt werden dürfen und welche ergänzenden Untersuchungen nötig sind. Eine bloße Wiederholung der Sandwerte aus Bericht 01 würde den geänderten Laststand nicht klären. Eine Ausführungsfreigabe der Fundamente haben wir nicht erteilt.

Mit freundlichen Grüßen
Mika Ehlers | m.ehlers@pfeilermass.example"""]),
        dokument("05_Feldblatt.pdf", "Feldaufzeichnungen KB3 und KB4", "Lars Söllner | Feldteam Ingenieurgeologie Erdspur", "Dr. Jule Hagedorn | Projektleitung", "14.09.2026, 16:15 Uhr", "EG-26-118 / Feldblatt F-04",
            ["""1 KB3 vom 26 August

Ansatzhöhe 19,98 m im örtlichen System. Bohrbeginn 11:05 Uhr, Ende 12:00 Uhr. Die obere Probe war sandig mit vereinzelten Ziegelbruchstücken. Zwischen 1,20 und 1,60 m wurde weicher graubrauner Schluff angesprochen, darunter Sand. Das Bohrloch wurde nach Abschluss und Wasserbeobachtung verfüllt; ein dauerhaftes Messrohr wurde an KB3 nicht eingebaut.""",
             tabelle(["Tiefe", "Ansprache", "Probe"], [["0,00 bis 0,20 m", "Oberboden", "keine Laborprobe"], ["0,20 bis 1,20 m", "sandige Auffüllung", "KB3-P1 bei 0,80 m"], ["1,20 bis 1,60 m", "weicher Schluff", "KB3-P2 bei 1,40 m"], ["1,60 bis 5,00 m", "mitteldichter Sand", "KB3-P3 bei 2,40 m"]], [0.27, 0.47, 0.26]),
             """2 KB4 vom 14 September

Ansatzhöhe 20,02 m. Bohrbeginn 08:30 Uhr, Ende 10:10 Uhr. Der Gerätestreifen im Osten war geräumt. Unter 0,25 m Oberboden lag Auffüllung bis 1,40 m. Zwischen 1,40 und 2,10 m wurde weicher, stellenweise breiiger Schluff angetroffen. Von 2,10 bis 6,00 m folgte Sand. Probe KB4-P2 stammt aus 1,75 m Tiefe, Probe KB4-P3 aus 2,80 m. Im Auffüllungsbereich wurden Ziegelstücke bemerkt; eine chemische Probe war nicht Teil des heutigen Auftrags.

Wasser stand nach 45 Minuten bei 1,10 m unter Ansatzhöhe. Ein provisorisches Rohr wurde zur erneuten Ablesung belassen. Der Rohrkopf liegt 0,30 m über Gelände und damit bei 20,32 m im örtlichen System. Messwerte ab Rohrkopf müssen um diesen Versatz berücksichtigt werden. Die spätere Wasserliste enthält bereits auf die örtliche Höhe umgerechnete Werte und die jeweiligen Rohablesungen.

Lars Söllner | Feldbuch abgeschlossen 14.09.2026, 16:15 Uhr"""]),
        dokument("09_Labormitteilung.pdf", "Geotechnische Laborwerte Weidenmaß", "Dr. Eva Rabe | Bodenlabor Kornzahl", "Dr. Jule Hagedorn | Ingenieurgeologie Erdspur", "17.09.2026", "KZ-26-772 / Ergebnisbegleitschreiben",
            """1 Proben und Auftrag

Sehr geehrte Frau Dr. Hagedorn, wir übersenden die Ergebnisse der für Weidenmaß eingelieferten Bodenproben. Die Sandproben KB1-P3 und KB2-P3 gingen am 27.08. ein, die Proben KB4-P2 und KB4-P3 am 15.09. Die Kennzeichnung und Entnahmetiefe haben wir aus Ihren Feldangaben übernommen. Eine eigene Zuordnung der Proben zu Grundstücksflächen haben wir nicht vorgenommen.

Die Tabelle 06_Laborwerte.csv enthält je Zeile Probe, Entnahmetiefe, Parameter, Zahlenwert und Einheit. Die Durchlässigkeitswerte stehen in m/s. Der Wert 0,000018 m/s für KB4-P3 entspricht 1,8 × 10^-5 m/s. Er darf nicht als 0,000018 mm/s gelesen werden. Die Wasserdurchlässigkeit wurde an der eingelieferten Probe ermittelt; eine Feldversickerung ist nicht untersucht worden.

2 Wassergehalt und Feinanteil

Für KB4-P2 aus dem Schluff liegt der gravimetrische Wassergehalt bei 31,0 Prozent. Das ist nicht der Anteil des Grundwassers am Porenvolumen. Der Feinanteil der Sandprobe KB4-P3 beträgt 7,2 Massenprozent. Diese Größen beschreiben unterschiedliche Merkmale und dürfen trotz gleicher Prozentdarstellung nicht zu einer Summe zusammengeführt werden.

Ein Steifemodul wurde in unserem Laborauftrag nicht unmittelbar bestimmt. Die im Bericht und in der Ergänzung genannten Modulbereiche stammen aus der ingenieurgeologischen Bewertung. Ebenso enthält unsere Tabelle keinen Bettungsmodul. Für eine statische Berechnung sind die Kennwerte durch die zuständigen Planer unter Berücksichtigung des konkreten Systems auszuwählen.

3 Abgrenzung

Chemische Parameter wurden nicht untersucht. Es gibt aus unserem Auftrag weder eine abfallrechtliche Deklaration noch eine Aussage zur uneingeschränkten Wiederverwendung der Auffüllung. Die Unterlagen umfassen das vorliegende Begleitschreiben und die CSV-Ergebnistabelle. Eine frühere Tabelle wurde nicht durch geänderte Zahlen überschrieben; die neu hinzugekommenen Proben tragen eigene Kennungen.

Mit freundlichen Grüßen
Dr. Eva Rabe | e.rabe@kornzahl.example"""),
        dokument("11_Bauherrnvermerk.docx", "Nutzungsergänzung Gerätehalle", "Bernd Kessler | Weidenmaß Gerätedienst GmbH", "Mika Ehlers und Architektin Tabea Sommer", "09.09.2026", "WM-26 / Besprechung 06",
            """1 Betriebseinrichtung

Die Besprechung fand heute von 13:00 bis 14:15 Uhr am Betriebsstandort Weidenmaß 7 statt. Teilgenommen haben Bernd Kessler, Mika Ehlers und Tabea Sommer. Der Betrieb möchte im Ostteil eine stationäre Reinigungsmaschine aufstellen. Ihr Sockel ist im Vorentwurf 2,40 × 1,80 m groß. Die endgültigen dynamischen Daten des Lieferanten fehlen noch. Herr Ehlers soll zunächst die angegebenen statischen Lasten für die Vorbemessung aufnehmen und die fehlenden Angaben gesondert anfordern.

Die beiden östlichen Stützen tragen künftig einen zusätzlichen Wartungssteg. Es handelt sich nicht um eine Kranbahn. Die Westseite der Halle bleibt bei der ursprünglich geplanten Nutzung. Eine vollflächig gleichmäßige Erhöhung sämtlicher Stützenlasten wurde nicht beschlossen. Die lichte Hallengeometrie bleibt 18,00 × 24,00 m.

2 Zugang zur Untersuchung

Die im Oststreifen abgestellten Geräte werden bis 11.09. nachmittags umgesetzt, damit das geotechnische Büro den bisher fehlenden Aufschluss herstellen kann. Am 14.09. steht Lars Söllner ab 08:00 Uhr ein Ansprechpartner zur Verfügung. Bernd Kessler weist darauf hin, dass der Streifen früher als befestigte Abstellfläche genutzt wurde. Eine Dokumentation über den Aufbau oder frühere Bodenverfüllungen liegt im Betrieb nicht vor.

3 Termin und Freigaben

Der ursprünglich gewünschte Beginn der Erdarbeiten am 05.10. bleibt ein Ziel des Betriebs. Herr Ehlers sagt hierfür keine technische Freigabe zu. Erst müssen die ergänzende Baugrundbeurteilung, die fehlenden Maschinenangaben und die Fundamentnachweise vorliegen. Tabea Sommer führt die Planstände zusammen. Es wird keine bestimmte Gründungsart in dieser Besprechung bestellt.

Für Aushubmaterial ist ein Angebot zur chemischen Untersuchung einzuholen. Die Laborwerte aus der geotechnischen Erstuntersuchung sollen nicht als Ersatz verwendet werden. Herr Kessler möchte Mengen und Kosten erst nach Vorliegen einer belastbaren Entsorgungsgrundlage festlegen.

Bernd Kessler | b.kessler@weidenmass.example"""),
    ],
    "mails": [
        mail("01_Ehlers_Unterlagen.eml", "Mika Ehlers <m.ehlers@pfeilermass.example>", "Tabea Sommer <t.sommer@sommer-planraum.example>", "2026-09-21T08:40:00+02:00", "Weidenmaß: Bericht und Ergänzung zusammenführen",
             """Sehr geehrte Frau Sommer,

bitte stellen Sie aus dem Baugrundbericht, seiner Ergänzung und den beigefügten Tabellen eine Anforderungsliste für unsere weitere Fundamentplanung zusammen. Ich brauche zu jedem Punkt die genaue Fundstelle und den räumlichen Geltungsbereich. Vor allem soll erkennbar bleiben, welche Annahmen durch die Ergänzung geändert wurden und welche Angaben nur für die Sandproben gelten.

Zahlenwerte, Einheiten, Lastarten und Höhenbezüge prüfe ich anschließend selbst gegen die Originale und unsere Berechnung. Bitte leiten Sie keine Fundamentabmessungen oder verbindlichen Bemessungswerte aus der Liste ab. Der Bericht umfasst drei Seiten, die Ergänzung zwei; die übrigen Dateien sind eigenständige Anlagen. Eine umfangreichere Gutachtenfassung liegt uns nicht vor.

Die Lastmitteilung ist noch nicht vollständig prüffähig. Vom Maschinenlieferanten fehlen weiterhin dynamische Angaben, und unser örtlicher Höhenbezug ist kein nachgewiesener NHN-Anschluss. Diese Lücken möchte ich in der Besprechung am 23.09. offen ansprechen. Für die Erdarbeiten besteht keine Ausführungsfreigabe.

Mit freundlichen Grüßen
Mika Ehlers
Tragwerksplanung Pfeilermaß"""),
        mail("10_Hagedorn_Uebergabe.eml", "Dr. Jule Hagedorn <j.hagedorn@erdspur.example>", "Mika Ehlers <m.ehlers@pfeilermass.example>", "2026-09-18T15:12:00+02:00", "EG-26-118: Ergänzung 01 und neue Rohdaten",
             """Sehr geehrter Herr Ehlers,

die Ergänzung 01 ist heute abgeschlossen. Bitte lesen Sie sie zusammen mit Bericht 01. Die zusätzliche Bohrung KB4 trifft eine mächtigere weiche Lage als KB3. Der neue Wasseransatz von 19,60 m ist eine vorläufige Planungsannahme im örtlichen System und darf nicht als am 16.09. gemessener Wasserstand bezeichnet werden. Die tatsächlich beobachtete Höhe steht in der Wasserliste.

Die Laborwerte zu KB4 wurden als neue Proben ergänzt. Wir haben die früheren Sandwerte nicht rückwirkend verändert. Für den östlichen Bereich ist eine gesonderte Beurteilung der Stützen und des Sockels erforderlich. Bitte schicken Sie vor einer abschließenden Nachweisführung Ihre Fundamentgeometrie sowie die Lastkombinationen und fehlenden Maschinenangaben.

Unsere Aufzeichnungen enthalten keine chemische Deklaration des Auffüllmaterials. Auch ein Wasserhaltungskonzept oder eine behördliche Einleiterlaubnis ist nicht beigefügt. Die nächste fachliche Abstimmung kann am 23.09. um 11:00 Uhr stattfinden. Damit ist weder eine bestimmte Gründungsvariante gewählt noch die Ausführung freigegeben.

Mit freundlichen Grüßen
Dr. Jule Hagedorn"""),
    ],
    "texte": {"12_Hoehen_Notiz.txt": """Tabea Sommer | WM-26 | Höhen- und Unterlagenlauf
21.09.2026, 09:10 Uhr

Projektfestpunkt an Hofmarke: örtliche Höhe 20,00 m, übernommen aus Bestandsaufmaß WM-V-01 vom 12.08.2026. Kein bescheinigter Anschluss an das amtliche Höhensystem in unserer Ablage.
OK Fertigfußboden laut WM-A-02: 20,30 m örtlich. Die Außenmaße 18,00 × 24,00 m bleiben in WM-A-03 vom 09.09. unverändert. Neu ist nur die Darstellung des Maschinensockels und des Wartungsstegs im Osten.
KB4 Gelände 20,02 m örtlich. Rohrkopf 0,30 m höher, also 20,32 m. Rohablesung ab Rohrkopf am 16.09. 1,24 m; daraus ergibt sich 19,08 m Wasserhöhe. Nicht mit 1,24 m unter Gelände verwechseln.
Vorläufige Fundamentunterkante 19,10 m aus Lastmitteilung ist nur eine Skizzenannahme. Unter KB4 entspräche sie 0,92 m unter Gelände und läge damit noch im Auffüllungsbereich. Nicht als freigegebene Gründungssohle in Ausführungspläne übernehmen.
Bericht 01 vom 04.09. liegt mit drei Seiten vor. Ergänzung 01 vom 18.09. liegt mit zwei Seiten vor. Keine Fassung mit 80 Seiten eingegangen.
Eingang neue Laborwerte 17.09.; Wasserliste fortgeführt bis 16.09. Es fehlen dynamische Maschinenangaben, vollständiger Fundamentplan, chemische Deklaration und Nachweis des amtlichen Höhenanschlusses. Termine sind in der Besprechung vom 23.09. abzustimmen.
"""},
    "csv": {
        "06_Laborwerte.csv": (["Probe", "Entnahmedatum", "Tiefe_m_u_Gelände", "Material", "Parameter", "Wert", "Einheit", "Bericht"], [
            ["KB1-P3", "2026-08-26", "2,00", "Sand", "Wasserdurchlässigkeit", "0,000020", "m/s", "KZ-26-772"],
            ["KB2-P3", "2026-08-26", "2,50", "Sand", "Wasserdurchlässigkeit", "0,000060", "m/s", "KZ-26-772"],
            ["KB3-P2", "2026-08-26", "1,40", "Schluff", "Wassergehalt gravimetrisch", "28,0", "%", "KZ-26-772"],
            ["KB4-P2", "2026-09-14", "1,75", "Schluff", "Wassergehalt gravimetrisch", "31,0", "%", "KZ-26-772"],
            ["KB4-P3", "2026-09-14", "2,80", "Sand", "Wasserdurchlässigkeit", "0,000018", "m/s", "KZ-26-772"],
            ["KB4-P3", "2026-09-14", "2,80", "Sand", "Feinanteil", "7,2", "Massen-%", "KZ-26-772"],
        ]),
        "07_Wasserbeobachtungen.csv": (["Punkt", "Zeitpunkt", "Bezug", "Bezugshöhe_m_örtlich", "Ablesung_m_unter_Bezug", "Wasserhöhe_m_örtlich", "Beobachtungsdauer", "Erfasser"], [
            ["KB1", "2026-08-26T10:00:00+02:00", "Gelände", "20,16", "1,80", "18,36", "30 min", "Lars Söllner"],
            ["KB2", "2026-08-26T11:10:00+02:00", "Gelände", "20,08", "1,70", "18,38", "30 min", "Lars Söllner"],
            ["KB3", "2026-08-26T12:30:00+02:00", "Gelände", "19,98", "1,65", "18,33", "30 min", "Lars Söllner"],
            ["KB4", "2026-09-14T10:55:00+02:00", "Gelände", "20,02", "1,10", "18,92", "45 min", "Lars Söllner"],
            ["KB4", "2026-09-16T09:00:00+02:00", "Rohrkopf", "20,32", "1,24", "19,08", "Folgeablesung", "Lars Söllner"],
        ]),
    },
    "bilder": [dict(datei="08_Aufschlusslage.png", art="bohrungen", titel="WM-G-01 | Aufschlusslage Gerätehalle Weidenmaß", datum="14.09.2026 | Lars Söllner", beschriftung="Halle 18,00 × 24,00 m | KB4 ergänzt im Oststreifen", untertitel="Schematische Lageübersicht, nicht maßstäblich. Bohrpunkte belegen keine flächigen Schichtgrenzen.")],
    "pruefung": [
        "Anforderungsliste mit Bericht/Ergänzung, Seite, Abschnitt und Tabellenbezug erstellen; tatsächlicher Umfang drei plus zwei Seiten statt erfundener 80 Seiten.",
        "Wasserannahme 19,30/19,60 m von Beobachtung 19,08 m trennen, örtliche Höhen nicht als NHN deklarieren und Rohrkopfversatz 0,30 m beachten.",
        "Charakteristische Lasten und Kennwerte nicht als fertige Bemessungswiderstände ausgeben; MN/m², MN/m³, kN/m², kN und m/s sauber unterscheiden.",
        "Östlichen Schluff, neue Sonderlasten, fehlende chemische Untersuchung und dynamische Angaben projektspezifisch berücksichtigen; Ingenieurprüfung und keine Ausführungsfreigabe.",
    ],
}
