"""Individuelle Quellenunterlagen zur Berliner Beschlussklage."""


def D(file, title, date, body, sender='', recipient='', **extra):
    return dict(file=file, title=title, date=date, body=body.strip(), sender=sender, recipient=recipient, **extra)


def E(file, title, date, sender, recipient, body):
    return dict(file=file, title=title, date=date, body=body.strip(), **{'from': sender, 'to': recipient})


SLUG = 'gesellschafterstreit-klageerwiderung-berlin'
DOCS = [
E('01_Mandat_Rabenstein.eml', 'Spreebogen Lichtwerk / Klage Seidel – bitte heute zurückrufen', '2026-10-02T08:17:00+02:00',
  'Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>', '"Dr. Adelbert Feuchtwanger" <af@feuchtwanger-recht.example>', '''
Sehr geehrter Herr Dr. Feuchtwanger,

wir brauchen Ihre Hilfe für die Gesellschaft, nicht für mich persönlich. Gottfried Seidel hat wegen seiner Abberufung geklagt. Das Gerichtspaket kam am letzten Freitag, 25. September. Wir haben bisher nichts an das Gericht geschrieben. Ottilie hat es erst gestern vollständig eingescannt. Bitte übernehmen Sie die Vertretung der Spreebogen Lichtwerk GmbH und bereiten Sie die Klageerwiderung vor. Sagen Sie mir vorher, welche Tatsachen wir noch belegen müssen und ob Sie einen gesonderten Beschluss oder eine Vollmacht benötigen.

Wir bauen und warten Lichtsteuerungen für kleine Bühnen. Zwölf Beschäftigte warten gerade darauf, wer Bestellungen freigeben darf. Ich möchte keinen Rundumschlag gegen Gottfried. Die Zahlung an seine eigene Firma und die Freigaben dürfen aber nicht einfach weiterlaufen. Wir haben ihm seinen Anstellungsvertrag nicht gekündigt; sein Septembergehalt ist bezahlt. Kunden gegenüber hat niemand von einer Entlassung gesprochen.

Im Anhang stehen die Klage und die Verfügung. Die weiteren Unterlagen liegen in der Ablage. Bitte keine Ansprüche gegen Gottfried ohne Rücksprache erheben. Ein Gespräch über eine künftige technische Rolle ist für uns denkbar, nicht aber eine Erklärung, alles sei schon bereinigt. Ich bin heute bis 11 Uhr im Betrieb, danach telefonisch erreichbar.

Mit freundlichen Grüßen
Kunigunde Rabenstein
Geschäftsführerin | Spreebogen Lichtwerk GmbH
Mühlenstraße 64, 13187 Berlin
kr@spreebogen-lichtwerk.example
Handelsregister: Amtsgericht Charlottenburg, HRB 241806 B
Anlagen: 02_Klage_Seidel.docx; 03_Gerichtliche_Verfuegung.pdf
'''),
D('02_Klage_Seidel.docx', 'Klage', '22.09.2026', '''
In dem Rechtsstreit des Herrn Gottfried Seidel, Florastraße 78, 13187 Berlin,
Kläger, Prozessbevollmächtigte: Rechtsanwältin Walburga Fürst, Kanzlei Fürst, Berliner Straße 91, 13189 Berlin,
gegen die Spreebogen Lichtwerk GmbH, Mühlenstraße 64, 13187 Berlin, vertreten durch die Geschäftsführerin Kunigunde Rabenstein,
Beklagte, wegen Beschlussanfechtung, vorläufiger Streitwert: 25000 EUR,
erheben wir namens und in Vollmacht des Klägers Klage.

## 1. Anträge

1.1. Der unter Tagesordnungspunkt 2 in der Gesellschafterversammlung der Beklagten vom 9. September 2026 festgestellte Beschluss, Herrn Gottfried Seidel aus wichtigem Grund mit sofortiger Wirkung als Geschäftsführer abzuberufen, wird für nichtig erklärt.

1.2. Hilfsweise wird festgestellt, dass der vorgenannte Beschluss nichtig ist.

1.3. Die Beklagte trägt die Kosten des Rechtsstreits.

Wir beantragen die Anordnung des schriftlichen Vorverfahrens. Für den Fall der Säumnis werden die gesetzlichen Anträge angekündigt. Die Klage wird elektronisch eingereicht. Der Kläger wendet sich ausschließlich gegen die Organabberufung; Vergütungsansprüche sind nicht Gegenstand dieser Klage.

## 2. Gesellschaft und Bestellung

Der Kläger hat 2019 gemeinsam mit Frau Rabenstein den Betrieb aufgebaut. Er hält den Geschäftsanteil Nr. 2 mit einem Nennbetrag von 8750 EUR, entsprechend 35 Prozent. Frau Rabenstein hält 40 Prozent und Frau Ottilie Heller 25 Prozent des Stammkapitals von 25000 EUR. Der Kläger ist seit Gründung Geschäftsführer für Technik und Einkauf. Frau Rabenstein betreut Vertrieb und Personal. Beide sind einzeln vertretungsberechtigt. Der Gesellschaftsvertrag beschränkt die Abberufung auf einen wichtigen Grund. Der Kläger hat der Gesellschaft weder den Rücken gekehrt noch Betriebsmittel entzogen.

Beweis: Gesellschaftsvertrag vom 18. Juni 2019, Anlage K1; Gesellschafterliste vom selben Tag, Anlage K2; Registerauszug vom 21. September 2026, Anlage K3.

## 3. Einladung und Versammlung

Die Einladung vom 26. August 2026 ging dem Kläger am 28. August per Einschreiben zu. Sie nennt als Grund einer Abberufung eine Zahlung an die Seidel Bühnenservice e.K. und fehlende Einkaufsfreigaben. Der Kläger nahm teil. Frau Heller leitete die Versammlung. Bei Tagesordnungspunkt 2 erklärte der Kläger sein Nein; Frau Rabenstein stimmte dafür. Frau Heller enthielt sich. Anschließend erklärte Frau Heller, die Stimme des Klägers zähle wegen eines wichtigen Grundes nicht, und stellte die Annahme des Antrags fest. Der Kläger widersprach der Zählung und dem Ergebnis noch im Raum. Seine Stellungnahme wurde nicht wörtlich aufgenommen.

Beweis: Einladung nebst Anlage, Anlage K4; Niederschrift vom 9. September 2026, Anlage K5. Frau Ottilie Heller ist unter der Anschrift der Beklagten zu laden.

Der Kläger bekam die vollständige Niederschrift am 11. September 2026 per E-Mail. Er hat weder einer Behandlung außerhalb der angekündigten Gegenstände noch einem Verzicht auf seine Stimme zugestimmt. Die beigefügte Niederschrift wird insoweit als Urkunde vorgelegt, nicht als inhaltlich richtig anerkannt.

## 4. Der Auftrag Lindenhof

Die Seidel Bühnenservice e.K. gehört dem Kläger. Sie hat für den Auftrag des Kulturhauses Lindenhof kurzfristig Material beschafft und sechs gebrauchte Steuergeräte überholt. Die Beklagte konnte die Wiedereröffnung sonst nicht termingerecht bedienen. Frau Rabenstein wusste von der Beauftragung. Am 19. August schrieb sie im betrieblichen Nachrichtenaustausch: „Dann mach das, aber ich brauche die endgültige Zahl.“ Der Kläger verstand dies als Freigabe. Er bestreitet, die Gesellschaft hintergangen zu haben.

Die Rechnung SBS-2026-084 vom 20. August lautet über 18400 EUR brutto. Sie wurde am 21. August bezahlt. Teile des Materials waren am 24. August im Betrieb; der Rest wurde auf der Baustelle eingebaut. Der Kläger nahm an, die vereinbarte Gegenzeichnung könne wegen der Eile nachgereicht werden. Die vorhandene Preisübersicht nannte zunächst 14900 EUR brutto. Der Aufpreis ergab sich aus vier zusätzlichen Arbeitsstunden und einem kurzfristigen Zukauf. Die Rechnung enthält die endgültigen Positionen.

Beweis: Rechnung, Anlage K6; Nachrichtenaustausch, Anlage K7; Zeugnis des Herrn Tassilo Brandt, Werkstattleiter der Beklagten, zu laden über diese. Eine schriftliche Auftragserteilung an die Einzelfirma ist dem Kläger derzeit nicht zugänglich. Die Geschäftsführung hat seinen Zugang zur Einkaufsablage gesperrt. Der Kläger bittet um Vorlage der vollständigen Nachrichtendatei und der Wareneingangsbuchung.

## 5. Ablauf und Einwände

Der Kläger hat Frau Rabenstein am 24. August mündlich auf die Zahlung hingewiesen. Am 27. August erhielt er eine schriftliche Beanstandung. Seine schriftliche Antwort vom 31. August erläutert den Zeitdruck und bietet eine gemeinsame Durchsicht der Belege an. Ein Gespräch fand vor der Versammlung nicht statt. Die Beklagte hatte nach seiner Wahrnehmung sämtliche Geräte, Kabel und Leistungen erhalten. Ein finanzieller Schaden ist nicht dargelegt. Die Beklagte verkürzt die Angelegenheit auf eine fehlende Gegenzeichnung, obwohl sie den Auftrag wirtschaftlich wollte.

Beweis: Beanstandung vom 27. August und Antwort vom 31. August, Anlagen K8 und K9. Für die Mitteilung am 24. August wird Parteivernehmung angeboten; ein unabhängiger Zeuge war nicht anwesend.

Die behaupteten älteren Freigabeverstöße wurden bei der Versammlung nicht konkret benannt. Eine Zahlungsaufforderung auf Rückerstattung liegt nicht vor. Der Kläger ist bereit, den unklaren Mehrbetrag anhand von Stundenaufzeichnungen aufzuklären. Er erkennt eine Pflichtverletzung dadurch nicht an.

## 6. Rechtliche Begründung

Die Beklagte muss die in ihrer Satzung vorausgesetzten Tatsachen eines wichtigen Grundes darlegen. Ein bloßer Vertrauensverlust aus dem Streit der Gesellschafter genügt nach Auffassung des Klägers nicht. Maßgeblich ist der tatsächliche Sachverhalt bei Beschlussfassung; dazu wird auf BGH, Urteil vom 4. April 2017, II ZR 77/16, Randnummern 9 bis 17, verwiesen. Der Kläger beruft sich auf Paragraf 38 Absatz 2 GmbHG und Ziffer 5.3 des Gesellschaftsvertrags.

Die Berufung auf ein Stimmverbot ersetzt keinen Nachweis. Außerdem bestreitet der Kläger, dass die Verfahrensleitung einen abschließenden Feststellungsauftrag besaß. Die Satzungsfrist wird durch die vorliegende Klage gewahrt. Der Gerichtskostenvorschuss wird nach Zugang der Kostenrechnung unverzüglich geleistet.

## 7. Anlagen und Abschluss

K1 Gesellschaftsvertrag; K2 Gesellschafterliste; K3 Registerauszug; K4 Einladung; K5 Niederschrift; K6 Rechnung SBS-2026-084; K7 Nachrichtenverlauf; K8 Beanstandung; K9 Antwort Seidel. Diese Unterlagen sind der Klage als gesonderte Dateien beigefügt.

Walburga Fürst
Rechtsanwältin
Übermittlung aus dem eigenen besonderen elektronischen Anwaltspostfach
''', 'Kanzlei Walburga Fürst | Berliner Straße 91 | 13189 Berlin\npost@fuerst-recht.example | Zeichen: WF 216/26', 'An das Landgericht Berlin II\nLittenstraße 12–17, 10179 Berlin\nPer besonderem elektronischen Anwaltspostfach'),
D('03_Gerichtliche_Verfuegung.pdf', 'Verfügung im schriftlichen Vorverfahren', '24.09.2026', '''
Geschäftszeichen: 32 O 187/26
Seidel gegen Spreebogen Lichtwerk GmbH

Sehr geehrte Damen und Herren,

im oben genannten Rechtsstreit wird das schriftliche Vorverfahren angeordnet. Die Beklagte wird aufgefordert, binnen einer Notfrist von zwei Wochen nach Zustellung der Klageschrift durch einen Rechtsanwalt anzuzeigen, ob sie sich gegen die Klage verteidigen will. Die Notfrist ist nicht verlängerbar.

Die Beklagte erhält eine weitere Frist von zwei Wochen nach Ablauf der Notfrist zur schriftlichen Klageerwiderung. Darin sind die Einwendungen gegen die Klage sowie Beweismittel mitzuteilen. Verspätetes Vorbringen kann unter den gesetzlichen Voraussetzungen unberücksichtigt bleiben. Vor dem Landgericht besteht Anwaltszwang; eine eigene Erklärung der Partei ersetzt den erforderlichen anwaltlichen Schriftsatz nicht.

Geht keine rechtzeitige Verteidigungsanzeige ein, kann auf Antrag ohne mündliche Verhandlung ein Versäumnisurteil ergehen. Soweit die Beklagte unterliegt, trägt sie die Kosten des Rechtsstreits einschließlich der notwendigen Kosten der Gegenseite nach Paragraf 91 ZPO. Das Versäumnisurteil wird nach Paragraf 708 Nummer 2 ZPO ohne Sicherheitsleistung für vorläufig vollstreckbar erklärt; bei der hier erhobenen Beschlussklage betrifft die Vollstreckung insbesondere die Kosten. Anträge auf Fristverlängerung für die Erwiderung sind vor Fristablauf unter Darlegung der Gründe einzureichen; über sie entscheidet das Gericht.

Anlage: Klageschrift vom 22.09.2026 mit Anlagen K1 bis K9.

Dr. Irmgard Wallroth, Richterin am Landgericht
Für die Geschäftsstelle: Mechthild Baur, Justizbeschäftigte
Elektronisch erstellte Ausfertigung zur Zustellung.
''', 'Landgericht Berlin II | Zivilkammer 32\nLittenstraße 12–17 | 10179 Berlin', 'Spreebogen Lichtwerk GmbH\nMühlenstraße 64\n13187 Berlin'),
D('04_Zustellung_Posteingang.txt', 'Posteingang / gelber Umschlag', '25.09.2026', '''
09:42 Uhr, Empfang Werkstatt, Mühlenstraße 64, 13187 Berlin.
Übergeben durch Zusteller an Ottilie Heller, Buchhaltung. Frau Rabenstein war beim Kundentermin. Herr Seidel war nicht im Haus.
Absender: Landgericht Berlin II. Aktenzeichen auf Umschlag: 32 O 187/26.
Auf dem Umschlag notiert: Zugestellt am 25.09.2026.
Inhalt: Verfügung 24.09.2026, Klageschrift 22.09.2026 und neun Anlagen.
Umschlag in Papierablage „Gericht September“ gelegt, nicht entsorgt.
25.09., 10:08 Uhr: Mappe auf Tisch KR gelegt. Klebezettel „Gericht / Seidel“.
01.10., 16:35 Uhr: KR fragt nach elektronischen Kopien. Versand an Kanzlei wird für Freitag vorbereitet.
Ottilie Heller, 01.10.2026, 17:12 Uhr
'''),
D('05_Gesellschaftsvertrag_K1.docx', 'Gesellschaftsvertrag der Spreebogen Lichtwerk GmbH', '18.06.2019', '''
Arbeitsabschrift der Urkunde UR-Nr. 218/2019 des Notars Dr. Ruprecht Greiner in Berlin. Die Gesellschafter bestätigten am 21.09.2026 gegenüber der Buchhaltung, dass keine spätere Satzungsänderung vorliegt.

## 1. Firma, Sitz und Geschäftsjahr

1.1. Die Firma lautet Spreebogen Lichtwerk GmbH. Sitz ist Berlin. Geschäftsjahr ist das Kalenderjahr. Die Gesellschaft wird auf unbestimmte Zeit errichtet.

1.2. Gegenstand ist die Planung, Montage und Wartung von Beleuchtungs- und Steuerungstechnik für Bühnen und Veranstaltungsräume sowie der Handel mit zugehörigem Material. Genehmigungspflichtige Tätigkeiten werden erst nach Erteilung der erforderlichen Erlaubnisse ausgeübt.

## 2. Stammkapital und Einlagen

Das Stammkapital beträgt 25000 EUR. Kunigunde Rabenstein übernimmt Anteil Nr. 1 zu 10000 EUR, Gottfried Seidel Anteil Nr. 2 zu 8750 EUR und Ottilie Heller Anteil Nr. 3 zu 6250 EUR. Alle Einlagen sind in Geld zu erbringen. Eine Nachschusspflicht besteht nicht. Die Gesellschaft trägt Gründungskosten bis zu 1800 EUR.

## 3. Geschäftsführung und Vertretung

3.1. Die Gesellschaft hat einen oder mehrere Geschäftsführer. Ist nur ein Geschäftsführer bestellt, vertritt er allein. Sind mehrere bestellt, vertreten zwei gemeinsam oder einer mit einem Prokuristen. Die Gesellschafterversammlung kann Einzelvertretungsbefugnis erteilen und von den Beschränkungen des Paragrafen 181 BGB befreien.

3.2. Kunigunde Rabenstein und Gottfried Seidel werden zu Geschäftsführern bestellt. Ihnen wird jeweils Einzelvertretungsbefugnis erteilt. Eine Befreiung von Paragraf 181 BGB wird bei Gründung nicht erteilt.

3.3. Die Gesellschafterversammlung kann eine Geschäftsordnung beschließen. Intern bedürfen Erwerb und Veräußerung von Grundstücken, Aufnahme von Krediten über 50000 EUR sowie Geschäfte mit Gesellschaftern oder von ihnen beherrschten Unternehmen der vorherigen Zustimmung der Gesellschafterversammlung. Die gesetzliche Außenvertretung bleibt unberührt.

## 4. Einberufung und Beschlussfassung

4.1. Jeder Geschäftsführer darf eine Gesellschafterversammlung einberufen. Die Einladung erfolgt durch eingeschriebenen Brief an die zuletzt mitgeteilte Anschrift mit einer Frist von mindestens zehn Kalendertagen; Versand- und Versammlungstag werden nicht mitgerechnet. Die Tagesordnung ist beizufügen. Bei einer Abberufung aus wichtigem Grund sind die wesentlichen tatsächlichen Vorwürfe anzugeben.

4.2. Die Versammlung ist beschlussfähig, wenn mehr als die Hälfte des Stammkapitals vertreten ist. Jeder volle Euro eines Geschäftsanteils gewährt eine Stimme. Einfache Beschlüsse bedürfen der Mehrheit der gültig abgegebenen Stimmen, soweit zwingendes Recht oder dieser Vertrag keine größere Mehrheit verlangen. Enthaltungen gelten nicht als abgegebene Stimmen.

4.3. Zum Versammlungsleiter wählen die anwesenden Gesellschafter mit einfacher Mehrheit eine Person. Der Leiter darf das Abstimmungsergebnis und die Annahme oder Ablehnung eines Antrags feststellen. Die Niederschrift muss Anträge, abgegebene Stimmen, nicht berücksichtigte Stimmen, Widersprüche und Ergebnis enthalten. Sie ist vom Leiter zu unterzeichnen und sämtlichen Gesellschaftern unverzüglich zu übermitteln.

4.4. Die Vertretung durch einen anderen Gesellschafter, Rechtsanwalt oder Steuerberater ist mit Vollmacht in Textform zulässig. Beschlüsse außerhalb einer Versammlung setzen das gesetzlich erforderliche Einverständnis voraus. Gesetzliche Informationsrechte bleiben unberührt.

## 5. Bestellung und Abberufung

5.1. Bestellung, Vergütung und Anstellungsvertrag der Geschäftsführer werden durch Gesellschafterbeschluss geregelt. Organstellung und Anstellungsvertrag sind selbständig.

5.2. Über Maßnahmen gegenüber einem Geschäftsführer wird für jeden Beschlussgegenstand gesondert abgestimmt. Die Beurteilung eines gesetzlichen Stimmverbots wird in der Niederschrift festgehalten.

5.3. Die Abberufung eines Geschäftsführers ist nur bei Vorliegen eines wichtigen Grundes zulässig. Über seinen Anstellungsvertrag ist gesondert zu entscheiden. Die Abberufung allein beendet diesen Vertrag nicht.

## 6. Jahresabschluss und Ergebnis

Die Geschäftsführung legt den Jahresabschluss mit einem Vorschlag zur Ergebnisverwendung innerhalb der gesetzlichen Fristen vor. Ausschüttungen erfolgen nach Verhältnis der Nennbeträge und nur auf Grundlage eines Gesellschafterbeschlusses unter Wahrung der Kapitalerhaltung. Abschlagszahlungen bedürfen eines gesonderten Beschlusses.

## 7. Geschäftsanteile und Ausscheiden

Abtretung und Verpfändung von Geschäftsanteilen bedürfen der Zustimmung der Gesellschafterversammlung mit 75 Prozent der abgegebenen Stimmen. Gesetzliche Formvorschriften bleiben unberührt. Im Todesfall gehen Anteile auf Erben über; mehrere Erben benennen einen gemeinsamen Vertreter. Ein allgemeines Recht zur Einziehung gegen den Willen des Inhabers wird nicht vereinbart.

## 8. Beschlussstreitigkeiten und Schlussbestimmungen

8.1. Klagen gegen festgestellte Gesellschafterbeschlüsse sind binnen eines Monats ab Zugang der Niederschrift gegen die Gesellschaft zu erheben. Bei Teilnahme und ausdrücklicher Ergebnisfeststellung beginnt die Frist mit der Versammlung. Zwingende gesetzliche Regeln bleiben unberührt. Eine Schiedsvereinbarung wird nicht getroffen.

8.2. Bekanntmachungen erfolgen in den gesetzlich vorgesehenen Medien. Vertragsänderungen bedürfen der gesetzlichen Form. Für den Fall der Unwirksamkeit einer Bestimmung vereinbaren die Gesellschafter, über eine wirksame, ihrem wirtschaftlichen Zweck möglichst nahekommende Regelung zu verhandeln; eine automatische ersetzende Regelung wird nicht fingiert.

Kunigunde Rabenstein / Gottfried Seidel / Ottilie Heller
Namenswiedergabe aus der bei der Buchhaltung abgelegten Abschrift.
'''),
D('06a_Gesellschafterliste_K2.docx', 'Gesellschafterliste', '18.06.2019', '''
Spreebogen Lichtwerk GmbH, Berlin, Amtsgericht Charlottenburg, HRB 241806 B.
Geschäftsanschrift: Mühlenstraße 64, 13187 Berlin.

Nr. 1: Kunigunde Rabenstein, geboren am 14.02.1979, wohnhaft Berlin, 10000 EUR, 40 Prozent.
Nr. 2: Gottfried Seidel, geboren am 09.11.1975, wohnhaft Berlin, 8750 EUR, 35 Prozent.
Nr. 3: Ottilie Heller, geboren am 23.04.1982, wohnhaft Berlin, 6250 EUR, 25 Prozent.
Stammkapital gesamt 25000 EUR. Einlagen laut Buchhaltung vollständig bezahlt.

Kunigunde Rabenstein / Gottfried Seidel, Geschäftsführer
Namenswiedergabe der eingereichten Liste. Keine Veränderungen der Geschäftsanteile seit Gründung in der Buchhaltung erfasst. Ablageabgleich durch Ottilie Heller am 21.09.2026.
'''),
D('06b_Registerabruf_K3.pdf', 'Handelsregister – aktueller Ausdruck', '21.09.2026', '''
Amtsgericht Charlottenburg, HRB 241806 B. Abruf 21.09.2026, 10:16 Uhr.
Firma: Spreebogen Lichtwerk GmbH. Sitz: Berlin.
Geschäftsanschrift: Mühlenstraße 64, 13187 Berlin.
Stammkapital: 25000 EUR. Rechtsform: Gesellschaft mit beschränkter Haftung.
Gesellschaftsvertrag vom 18.06.2019.

Gegenstand: Planung, Montage und Wartung von Beleuchtungs- und Steuerungstechnik für Bühnen und Veranstaltungsräume sowie Handel mit zugehörigem Material.

Allgemeine Vertretung: bei mehreren Geschäftsführern gemeinschaftlich durch zwei Geschäftsführer oder durch einen Geschäftsführer mit einem Prokuristen. Eingetragen sind Kunigunde Rabenstein und Gottfried Seidel, jeweils einzelvertretungsberechtigt. Eine Befreiung von Paragraf 181 BGB ist für keinen von beiden eingetragen. Prokura ist nicht eingetragen. Die bisherige Satzung ist vom 18.06.2019.

Geschäftsführer: Kunigunde Rabenstein, Berlin, geboren am 14.02.1979; Gottfried Seidel, Berlin, geboren am 09.11.1975. Eine weitere Änderung der Geschäftsführer ist in diesem Ausdruck nicht enthalten. Letzte Eintragung: 04.07.2019, laufende Nummer 1. Ende des aktuellen Ausdrucks.
'''),
D('07_Einladung_K4.docx', 'Einladung zur Gesellschafterversammlung am 09.09.2026', '26.08.2026', '''
Sehr geehrter Herr Seidel, sehr geehrte Frau Heller,

ich lade Sie zur Gesellschafterversammlung der Spreebogen Lichtwerk GmbH am Mittwoch, 9. September 2026, 10:00 Uhr, Besprechungsraum der Werkstatt, Mühlenstraße 64, 13187 Berlin, ein.

## 1. Tagesordnung

1.1. Wahl der Versammlungsleitung und Feststellung der Beschlussfähigkeit.

1.2. Abberufung von Herrn Gottfried Seidel als Geschäftsführer aus wichtigem Grund mit sofortiger Wirkung. Zur Entscheidung gestellt werden seine alleinige Beauftragung der ihm gehörenden Seidel Bühnenservice e.K. im Projekt Lindenhof und die durch ihn am 21.08.2026 veranlasste Zahlung von 18400 EUR ohne den vorherigen Gesellschafterbeschluss. Weiterer Gegenstand ist die Missachtung der Geschäftsordnung vom 10.01.2025 trotz der dort vereinbarten schriftlichen Freigaben. Rechnung, Geschäftsordnung und der derzeit vorhandene Lieferbeleg können nach Terminvereinbarung im Büro eingesehen werden. Eine Kopie der Rechnung ist beigefügt.

1.3. Bericht zum laufenden Auftrag Lindenhof. Keine Abstimmung über Schadensersatz, Anteilsentzug oder Kündigung des Anstellungsvertrags.

## 2. Antrag und Vorbereitung

Zu Ziffer 1.2 beantrage ich: „Herr Gottfried Seidel wird aus wichtigem Grund mit sofortiger Wirkung als Geschäftsführer der Spreebogen Lichtwerk GmbH abberufen.“ Bitte nehmen Sie zu den Vorwürfen vor oder während der Versammlung Stellung. Sie können einen bevollmächtigten Vertreter nach Ziffer 4.4 des Gesellschaftsvertrags entsenden. Weitere Unterlagen sende ich auf konkrete Anfrage zu.

Mit freundlichen Grüßen
Kunigunde Rabenstein, Geschäftsführerin
Anlage: Rechnung SBS-2026-084
Postausgang: beide Einschreiben am 26.08.2026 um 16:08 Uhr eingeliefert. Auslieferung an Seidel am 28.08.2026, an Heller am 27.08.2026.
''', 'Spreebogen Lichtwerk GmbH\nMühlenstraße 64 | 13187 Berlin\nkr@spreebogen-lichtwerk.example', 'Gottfried Seidel, Florastraße 78, 13187 Berlin\nOttilie Heller, Mühlenstraße 64, 13187 Berlin'),
D('08_Niederschrift_K5.docx', 'Niederschrift der Gesellschafterversammlung', '09.09.2026', '''
Ort: Mühlenstraße 64, Berlin. Beginn 10:02 Uhr, Ende 11:18 Uhr. Anwesend: Kunigunde Rabenstein mit 10000 Stimmen, Gottfried Seidel mit 8750 Stimmen und Ottilie Heller mit 6250 Stimmen. Das gesamte Stammkapital ist vertreten. Kein anwaltlicher Begleiter. Die Einladungsbelege liegen vor.

## 1. Leitung

Frau Heller wird mit allen 25000 Stimmen zur Versammlungsleiterin gewählt. Sie nimmt die Wahl an und führt die Niederschrift. Herr Seidel bittet, seinen Widerspruch zu jedem gegen ihn gerichteten Beschluss aufzunehmen. Frau Heller erklärt, sie werde die Wortmeldungen zusammenfassen, nicht stenografisch aufnehmen.

## 2. Aussprache zur Abberufung

Frau Rabenstein verweist auf die Rechnung von 18400 EUR und die Geschäftsordnung. Sie erklärt, dass keine Zustimmung aller Gesellschafter eingeholt worden sei. Sie habe ein weiteres Angebot und den endgültigen Betrag sehen wollen. Die Überweisung sei dennoch erfolgt. Sie halte es nicht mehr für vertretbar, Herrn Seidel weiterhin allein Einkaufsverpflichtungen eingehen zu lassen.

Herr Seidel erklärt, der Lieferant habe auf sofortiger Zahlung bestanden. Er habe die Ware zum Teil über seine Einzelfirma beschafft und den Auftrag retten müssen. Die Nachricht „Dann mach das“ habe er als Freigabe verstanden. Er könne die fehlenden Nachweise bis Ende September vervollständigen. Auf Nachfrage, wer für die GmbH den Auftrag an seine Einzelfirma erteilt habe, antwortet er: „Das habe ich erledigt. Sonst wäre es liegen geblieben.“ Er bestreitet eine persönliche Bereicherung.

Frau Heller berichtet, am 24.08. seien vier Geräte eingegangen. Über zwei weitere Geräte und die Montagezeiten habe sie bis heute nur die Angaben von Herrn Seidel. Sie enthält sich einer Bewertung, weil sie auf der Baustelle nicht anwesend war. Sie hält fest, dass Herr Seidel der Vorlage einer Rückzahlungserklärung nicht zustimmt; eine solche Erklärung war kein Tagesordnungspunkt.

## 3. Abstimmung und Feststellung

Zur Abstimmung steht genau der Antrag aus der Einladung: Abberufung von Herrn Gottfried Seidel aus wichtigem Grund mit sofortiger Wirkung. Frau Rabenstein stimmt mit 10000 Stimmen Ja. Herr Seidel erklärt mit 8750 Stimmen Nein. Frau Heller enthält sich mit 6250 Stimmen.

Frau Heller berücksichtigt die Nein-Stimmen von Herrn Seidel nicht; sie nennt als Grund seine Betroffenheit von der Abberufung aus wichtigem Grund. Sie stellt den Antrag mit 10000 Ja-Stimmen und ohne berücksichtigte Nein-Stimme als angenommen fest. Herr Seidel widerspricht ausdrücklich seinem Stimmrechtsausschluss, der Feststellung und der Abberufung. Er erklärt, es fehle der wichtige Grund. Auf seinen Wunsch wird dieser Widerspruch aufgenommen.

## 4. Weitere Erklärungen

Über den Anstellungsvertrag wird nicht abgestimmt. Es wird kein Schadensersatzbeschluss gefasst. Frau Rabenstein kündigt an, den Notar mit der Registeranmeldung zu befassen. Herr Seidel verlangt, den laufenden Lindenhof-Auftrag weiter technisch begleiten zu dürfen. Eine Vereinbarung darüber kommt nicht zustande. Die Unterlagen sollen gesichert bleiben; Frau Heller soll Kopien herausgeben, wenn Herr Seidel konkrete Belege benennt.

Ottilie Heller, Versammlungsleiterin
Niederschrift erstellt am 10.09.2026. Versand an alle drei Gesellschafter am 11.09.2026, 08:25 Uhr. Namenswiedergabe der unterschriebenen Papierfassung.
'''),
D('09_Geschaeftsordnung.docx', 'Geschäftsordnung und Einkaufsfreigaben', '10.01.2025', '''
Beschlossen von sämtlichen Gesellschaftern der Spreebogen Lichtwerk GmbH am 10.01.2025; Zustimmung jeweils persönlich erklärt. Diese Geschäftsordnung regelt das Innenverhältnis und ändert nicht den Gesellschaftsvertrag.

## 1. Ressorts

Kunigunde Rabenstein führt Vertrieb, Personal und die laufende Liquiditätsübersicht. Gottfried Seidel führt Technik, Materialeinkauf und Baustellenkoordination. Beide berichten einander wöchentlich über Bestellungen, Beanstandungen und Zahlungspflichten. Die Geschäftsführung bleibt gemeinsam für den Überblick über die Gesellschaft verantwortlich.

## 2. Bestellungen und Zahlungen

Einzelbestellungen über 10000 EUR brutto sind vor Beauftragung dem jeweils anderen Geschäftsführer mit Leistungsumfang, Preis, Liefertermin und Vergleichsangebot vorzulegen. Die Zustimmung ist in Textform in der Projektablage zu sichern. Zahlungen über dieser Grenze dürfen erst nach entsprechender Freigabe ausgelöst werden. Die technisch eingerichtete Einzelberechtigung im Bankportal bleibt bestehen, begründet aber keine interne Freigabe.

Bei einer unmittelbaren Gefahr für Personen oder drohendem erheblichen Sachschaden darf ein Geschäftsführer erforderliche Sofortmaßnahmen veranlassen. Er muss den anderen noch am selben Tag unterrichten. Ein nur drohender Terminverlust gegenüber Kunden ersetzt die Freigabe nicht. Die Satzungsregel für Geschäfte mit Gesellschaftern oder deren Unternehmen bleibt uneingeschränkt bestehen.

## 3. Nachweise

Wareneingänge werden durch den Werkstattleiter anhand von Stückzahl und sichtbarem Zustand dokumentiert. Die Buchhaltung gleicht Rechnung, Auftrag und Wareneingang ab. Fehlende Unterlagen sind binnen fünf Arbeitstagen nachzureichen. Ein Lieferbeleg ersetzt keine Preisfreigabe; eine Preisfreigabe ersetzt keinen Lieferbeleg.

## 4. Laufende Kontrolle

Bei Zweifeln hält die Buchhaltung Rücksprache mit beiden Geschäftsführern, bevor sie selbst eine Zahlung freigibt. Vom Geschäftsführer eigenständig ausgeführte Zahlungen werden im Bankprotokoll mit Nutzerkennung dokumentiert. Die Monatsliste wird allen Gesellschaftern bereitgestellt.

Kunigunde Rabenstein / Gottfried Seidel / Ottilie Heller
Von allen unterschriebene Ausfertigung in Ordner „Gesellschaft / 2025“.
'''),
D('10_Rechnung_SBS_K6.pdf', 'Rechnung SBS-2026-084', '20.08.2026', '''
Projekt: Kulturhaus Lindenhof, Bühnensteuerung. Leistungszeitraum 19.–20.08.2026.
Sehr geehrte Damen und Herren, wir berechnen die kurzfristige Beschaffung und Aufarbeitung gemäß Abstimmung mit Herrn Seidel. Lieferung ab Werkstatt, Geräte einschließlich Funktionsprüfung. Eigentumsvorbehalt bis zur vollständigen Zahlung.

Bitte zahlen Sie 18400,00 EUR ohne Abzug bis zum 21.08.2026 auf die bereits hinterlegte Geschäftsverbindung. Unsere Bankverbindung hat sich nicht geändert. Bei Rückfragen zur Zuordnung nennen Sie bitte die Rechnungsnummer.

Mit freundlichen Grüßen
Gottfried Seidel, Inhaber
Steuernummer 35/512/60821 | Rechnungsausgang 20.08.2026, 18:41 Uhr
''', 'Seidel Bühnenservice e.K. | Gottfried Seidel\nSchönhauser Straße 163, 13158 Berlin\nrechnung@seidel-buehnenservice.example', 'Spreebogen Lichtwerk GmbH\nMühlenstraße 64, 13187 Berlin', tables=[{'headers':['Position','Leistung','Netto EUR'], 'rows':[['1','Sechs überholte Steuergeräte, je 1950 EUR','11700,00'],['2','Kabelsatz und Sonderstecker','1900,00'],['3','Transport und Einbauunterstützung','1000,00'],['4','Expressbeschaffung und Zusatzarbeit','862,18'],['','Nettosumme','15462,18'],['','Umsatzsteuer 19 Prozent','2937,82'],['','Rechnungsbetrag','18400,00']]}]),
D('11_Nachrichten_K7.txt', 'Nachrichtenexport – Lindenhof Einkauf', '19.08.2026', '''
Export durch Kunigunde Rabenstein am 28.09.2026 aus dem betrieblichen Kanal. Zeitzone Berlin. Teilnehmer: Kunigunde Rabenstein und Gottfried Seidel.

19.08.2026 07:46 Seidel: Der ursprüngliche Lieferant schafft es nicht. Ich kann die sechs Geräte über meine Firma zusammenbekommen, mit Einbauhilfe. Nach erster Rechnung 14900 brutto, vielleicht noch Expresszuschlag.
19.08.2026 08:04 Rabenstein: Dann mach das, aber ich brauche die endgültige Zahl. Nichts ohne den Preisabgleich. Schick mir das andere Angebot und frag Ottilie wegen der Gesellschafterfreigabe.
19.08.2026 08:07 Seidel: Ich bin schon unterwegs, liefere nach.
19.08.2026 08:10 Rabenstein: Morgen 9 Uhr telefonieren? Heute bin ich im Außentermin.
20.08.2026 09:03 Seidel: Bin auf der Bühne. Rückruf später.
20.08.2026 18:44 Seidel: Rechnung jetzt 18400. Zwei Geräte musste ich woanders holen. Geht gleich per Mail an die Buchhaltung.
21.08.2026 07:31 Rabenstein: Gerade erst gesehen. Wo sind Vergleich und Zustimmung? Bitte noch nicht zahlen, bis wir das gemeinsam angesehen haben.
21.08.2026 07:49 Seidel: Musste raus, sonst liefern die nicht. Erkläre ich am Montag.
21.08.2026 08:02 Rabenstein: Das war nicht abgesprochen. Montag 8 Uhr im Büro.

Keine weiteren Nachrichten im exportierten Zeitraum 19.–21.08.2026. Telefonate sind in diesem Export nicht enthalten.
'''),
D('12_Beanstandung_K8.docx', 'Vorgang Lindenhof / fehlende Freigabe', '27.08.2026', '''
Lieber Gottfried,

am 21. August hast Du 18400 EUR an Deine Einzelfirma überwiesen. Ich hatte Dir um 07:31 Uhr geschrieben, dass bis zur gemeinsamen Durchsicht nicht gezahlt werden soll. Das Bankprotokoll nennt 07:43 Uhr als Ausführung. Es liegt weder der Gesellschafterbeschluss zu diesem Geschäft noch das von mir erbetene Vergleichsangebot vor.

Bitte gib uns bis Montag, 31. August, den vollständigen Bestellvorgang, die Fremdrechnungen zum Expresszuschlag und eine Aufstellung, wo die sechs Steuergeräte eingebaut oder gelagert sind. Im Wareneingang stehen bisher nur vier. Tassilo kann nicht bestätigen, dass die zwei übrigen Geräte unmittelbar zur Baustelle gingen. Ich will das nicht aus Gerüchten beurteilen.

Deine Aussage am Montag, die Buchhaltung solle sich nicht in die Technik einmischen, hat die Situation verschärft. Ottilie soll die Zahlung prüfen können. Gib ihr deshalb bitte auch die Zahlungsfreigabe, auf die Du Dich berufst. Ich erinnere an unsere von allen unterschriebene Geschäftsordnung. Wir müssen vor der Versammlung eine nachvollziehbare Antwort haben.

Dies ist keine Kündigung Deines Anstellungsvertrags. Die angekündigte Versammlung findet statt. Bitte bewahre sämtliche Nachrichten und Belege unverändert auf.

Kunigunde Rabenstein
Geschäftsführerin
Übergabe im Büro am 27.08.2026, 15:20 Uhr, Empfang durch Gottfried Seidel auf Bürokopie vermerkt.
''', 'Spreebogen Lichtwerk GmbH\nMühlenstraße 64, 13187 Berlin', 'Herrn Gottfried Seidel\nIm Hause'),
D('13_Antwort_Seidel_K9.docx', 'Meine Antwort zum Auftrag Lindenhof', '31.08.2026', '''
Liebe Kunigunde,

ich habe Deine Nachricht vom 21. August erst gelesen, nachdem ich bezahlt hatte. Dass ich den Auftrag an meine Firma selbst erteilt habe, war aus Zeitdruck. Ich habe mit Deinem „Dann mach das“ gerechnet. Ottilie war wegen der Monatsabrechnung beschäftigt. Einen förmlichen Beschluss habe ich nicht eingeholt. Wir haben früher Kleinaufträge telefonisch geregelt, allerdings nicht in dieser Höhe.

Vier Geräte stehen auf dem Lieferbeleg. Zwei habe ich am 22. August direkt zur Bühne gefahren. Es waren Austauschgeräte aus meinem Bestand. Ich habe dort keinen unterschriebenen Beleg bekommen, weil die Bauleitung nicht da war. Die Monteure müssten sie gesehen haben. Bitte fragt Tassilo nach dem schwarzen Transportkoffer. Meine Fotos zeigen nur die Verpackung, nicht die Seriennummern.

Der Zuschlag ist nicht reine Marge. Ich habe Material zugekauft und am Wochenende gearbeitet. Einen gesonderten Stundenzettel habe ich bislang nicht geschrieben. Bis zum 4. September kann ich die Fremdrechnung und meine Kalendernotizen bringen. Das Vergleichsangebot des ursprünglichen Lieferanten ist nie endgültig geworden. Es gab nur dessen telefonische Zahl.

Ich bin bereit, die Kalkulation mit Dir durchzugehen und eine nicht belegbare Position notfalls gutzuschreiben. Eine Rückzahlung von 18400 EUR oder ein Schuldeingeständnis werde ich nicht unterschreiben. Der Auftrag wurde fertig und der Kunde hat uns bezahlt. Bitte lass mich weiter die Technik betreuen; niemand sonst kennt alle Installationen.

Gottfried Seidel
Persönlich abgegeben am 31.08.2026, 17:05 Uhr. Empfang Ottilie Heller.
''', 'Gottfried Seidel\nFlorastraße 78, 13187 Berlin', 'Spreebogen Lichtwerk GmbH\nKunigunde Rabenstein'),
D('14_Wareneingang_Lindenhof.docx', 'Wareneingang WE-0824 / Lindenhof', '24.08.2026', '''
Anlieferung 24.08.2026, 08:35 Uhr am Werkstatttor Mühlenstraße. Überbracht durch Gottfried Seidel im Firmenkombi. Annahme: Tassilo Brandt. Im Fahrzeug vier Steuergeräte in blauen Kisten und zwei Kartons Kabel. Keine sechs Geräte gezählt.

Erfasst: Serien L-402, L-407, L-411 und L-419, jeweils gebraucht, äußerlich gereinigt. Kabelkartons ungeöffnet an Montagewagen 2. Einschaltprüfung der vier Geräte um 09:20 Uhr ohne Fehlermeldung. Eine Prüfung am tatsächlichen Lastkreis erfolgt erst auf der Baustelle. Alte Typenschilder wurden nicht ersetzt.

Herr Seidel sagte, die übrigen zwei Geräte seien bereits am Samstag direkt zum Lindenhof gefahren. Dazu liegt mir kein Lieferschein vor. Ich war am Samstag nicht im Dienst. Herr Albrecht Riedel vom Lindenhof sagte telefonisch, er habe auf der Bühne „mehrere Kisten“ gesehen, könne aber weder Zahl noch Eigentümer zuordnen. Ein Abgleich der Seriennummern ist noch nicht erfolgt.

Die beigefügte Rechnung lag bei Anlieferung nicht vor. Ein Preis wurde von mir nicht bestätigt. Die Unterschrift unter dem Wareneingang betrifft nur die oben gezählten Gegenstände.

Tassilo Brandt, Werkstattleiter
Notiz vom 04.09.2026: Rechnung erhalten; dort sechs Geräte. Rückfrage an GS per Mail weitergegeben.
''', 'Spreebogen Lichtwerk GmbH\nWerkstatt / Wareneingang'),
E('15_Zeuge_Brandt.eml', 'Re: Unterlagen zum Lindenhof / was ich selbst gesehen habe', '2026-10-01T14:38:00+02:00', 'Tassilo Brandt <tb@spreebogen-lichtwerk.example>', 'Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>', '''
Hallo Kunigunde,

ich habe die vier Geräte am Montag selbst gezählt. Ob Gottfried zwei weitere am Samstag direkt geliefert hat, weiß ich nicht. Ich habe ihm am Freitag geholfen, einen schwarzen Koffer aus der Werkstatt zu laden. Den habe ich nicht geöffnet. Dass darin zwei Geräte waren, hat er mir erst später gesagt.

Beim Montagsgespräch im Büro war ich ungefähr die letzten fünf Minuten dabei. Ich habe gehört, dass Du nach der Freigabe gefragt hast und Gottfried sagte, es sei jetzt erledigt. Ob Ihr vorher telefonisch eine Freigabe besprochen habt, kann ich nicht sagen. Bitte schreibt mir nicht als Aussage zu, es sei sicher nichts geliefert worden.

Der Lindenhof funktioniert inzwischen. Dort wurden auch zwei Geräte aus einem früheren Auftrag weiterbenutzt. Deshalb kann ich aus der Anzahl eingebauter Geräte allein nichts über die streitige Lieferung ableiten. Ich kann am Dienstag ab 15 Uhr persönlich sprechen. Den Wareneingang habe ich angehängt.

Viele Grüße
Tassilo Brandt
Werkstattleitung | Spreebogen Lichtwerk GmbH
Mühlenstraße 64, 13187 Berlin
Anlage: 14_Wareneingang_Lindenhof.docx

Am 01.10.2026 um 10:12 schrieb Kunigunde Rabenstein:
Bitte schreib auf, was Du selbst gesehen hast. Die Kanzlei braucht keine Vermutungen.
'''),
E('16_Rechnungseingang.eml', 'SBS-2026-084 / Lindenhof / Zahlung morgen', '2026-08-20T18:42:00+02:00', 'Gottfried Seidel <rechnung@seidel-buehnenservice.example>', 'Ottilie Heller <oh@spreebogen-lichtwerk.example>', '''
Hallo Ottilie,

anbei die endgültige Rechnung. Bitte auf Lindenhof buchen. Es sind jetzt 18400 EUR einschließlich Steuer. Ich habe die kurzfristige Materialbeschaffung und die zusätzlichen Stunden zusammengefasst. Die erste Zahl war vor dem Zukauf. Die Kalkulation reiche ich nach, ich fahre gleich noch auf die Baustelle.

Das muss morgen raus. Wenn Du nicht dazu kommst, mache ich die Überweisung selbst. Kunigunde weiß, dass der ursprüngliche Lieferant ausgefallen ist. Den Lieferbeleg bekommst Du mit der Ware.

Grüße
Gottfried
Seidel Bühnenservice e.K.
Schönhauser Straße 163, 13158 Berlin
rechnung@seidel-buehnenservice.example
Anlage: 10_Rechnung_SBS_K6.pdf
'''),
D('17_Bankprotokoll.csv', 'Kontobewegungen Projektkonto August', '31.08.2026', '', headers=['Buchungstag','Uhrzeit','Referenz','Zweck','Eingang_EUR','Ausgang_EUR','Benutzer'], rows=[['18.08.2026','09:10','B-0818','Lindenhof Abschlag',25000,0,'Bankeingang'],['19.08.2026','11:04','B-0819','Werkstattmiete',0,2400,'OH'],['21.08.2026','07:43','B-0821','SBS-2026-084',0,18400,'GS'],['24.08.2026','12:06','B-0824','Kabelkontor',0,1250,'OH'],['28.08.2026','10:22','B-0828','Lindenhof Restzahlung',12000,0,'Bankeingang'],['31.08.2026','13:17','B-0831','Löhne Sammelauftrag',0,18750,'KR']]),
D('18_Telefonvermerk_Heller.docx', 'Telefonvermerk – Ottilie Heller', '02.10.2026', '''
Kanzlei Feuchtwanger, Sachbearbeitung Adelbert Feuchtwanger. Gespräch 09:36–09:48 Uhr mit Ottilie Heller, Buchhaltung und Gesellschafterin. Aktenzeichen AF 326/26.

Frau Heller sagt, sie habe die Einladung und die Niederschrift mitverfasst. Sie habe sich bei der Abstimmung enthalten, weil sie die zusätzliche Lieferung nicht beurteilen könne. Sie erinnert sich daran, dass Herr Seidel Nein sagte. Auf Nachfrage: Die Entscheidung, seine Stimme nicht zu zählen, habe sie selbst getroffen. Es habe kein vorheriges anwaltliches Gutachten gegeben. Sie habe Ziffer 4.3 der Satzung vor der Versammlung gelesen.

Die Bankliste enthält nur das Projektkonto. Eine förmliche Freigabe für die SBS-Rechnung hat sie in der digitalen Ablage bis heute nicht gefunden. Sie hat aber den Papierordner „Einkauf August“ noch nicht vollständig durchgesehen. Herr Seidel hatte am 4. September nur zwei Handyfotos eines Kassenbons geschickt; sie konnte Betrag und Aussteller nicht lesen. Sie will die Originale erneut anfordern.

Die Septembervergütung von Herrn Seidel wurde am 30. September über das Lohnkonto gezahlt, nicht über das Projektkonto. Ein Antrag auf einstweiligen Rechtsschutz ist bei der Gesellschaft bis heute nicht eingegangen. Der Briefumschlag zur Klage liegt noch im Büro. Sie bringt ihn zusammen mit dem Originalprotokoll am Montag mit.

Aufgenommen: Dr. Adelbert Feuchtwanger
Frau Heller bat um Zusendung dieses Vermerks vor einer Verwendung ihres Namens als Zeugin. Eine Bestätigung des Wortlauts liegt noch nicht vor.
'''),
]

CASE = dict(slug=SLUG, title='Klageerwiderung im Gesellschafterstreit – Berlin',
    date='02.10.2026', client='Spreebogen Lichtwerk GmbH', plugin='gesellschafterstreit',
    summary='Ein Berliner Betrieb für Bühnenbeleuchtung verteidigt sich gegen die Klage eines abberufenen Gesellschafter-Geschäftsführers. Streit besteht über einen Einkauf bei dessen Einzelfirma, Freigaben, Lieferumfang und die Abstimmung.',
    assignment='Die Gesellschaft wünscht eine Klageerwiderung. Der Auftrag steht in der Mandats-E-Mail; die tatsächlichen Angaben ergeben sich aus Klage, Gesellschaftsunterlagen und Geschäftskorrespondenz. Die Akte enthält keine fertige Verteidigung.',
    core=['01_Mandat_Rabenstein.eml','02_Klage_Seidel.docx','03_Gerichtliche_Verfuegung.pdf','04_Zustellung_Posteingang.txt','05_Gesellschaftsvertrag_K1.docx','08_Niederschrift_K5.docx','11_Nachrichten_K7.txt'],
    documents=DOCS, attachments={'01_Mandat_Rabenstein.eml':['02_Klage_Seidel.docx','03_Gerichtliche_Verfuegung.pdf'], '15_Zeuge_Brandt.eml':['14_Wareneingang_Lindenhof.docx'], '16_Rechnungseingang.eml':['10_Rechnung_SBS_K6.pdf']})
