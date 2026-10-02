"""Native Konfliktakte Zink und Zunder ohne vorgegebene rechtliche Lösung."""

def D(file,title,day,sender,recipient,body,**extra):
    return dict(file=file,title=title,date=day,sender=sender,recipient=recipient,body=body.strip(),**extra)

def E(file,title,day,sender,recipient,body):
    return dict(file=file,title=title,date=day,**{'from':sender,'to':recipient},body=body.strip())

FIRMA='Zink & Zunder Metallbau GmbH\nWerkhof Weißensee 14, 13088 Berlin\nbuero@zink-zunder.example'
ROMY='Romy Yilmaz\nParkbogen 7, 13086 Berlin\nromy@zink-zunder.example'
KUNI='Kunibert Knopf\nEisenwinkel 4, 13088 Berlin\nkunibert@zink-zunder.example'
THEKLA='Thekla Spätzle\nLerchenzeile 11, 13129 Berlin\nthekla@zink-zunder.example'
KANZLEI='Rechtsanwältin Clara Klee\nKanzlei Klee und Kolben\nKanalbüro 9, 10999 Berlin\nclara@klee-kolben.example'
SATZUNG='''## 1 Firma Sitz und Gegenstand

Die Gesellschaft führt die Firma Zink & Zunder Metallbau GmbH. Ihr Sitz ist Berlin. Gegenstand des Unternehmens sind die Planung, Herstellung, Montage und Reparatur von Metallkonstruktionen, Fenstern, Geländern und Treppen sowie damit verbundene technische Dienstleistungen. Die Gesellschaft darf Zweigniederlassungen errichten und sich an anderen Unternehmen beteiligen, soweit dies ihrem Unternehmensgegenstand dient.

## 2 Dauer und Geschäftsjahr

Die Gesellschaft besteht auf unbestimmte Zeit. Das Geschäftsjahr ist das Kalenderjahr. Bekanntmachungen der Gesellschaft erfolgen, soweit gesetzlich erforderlich, in den gesetzlich vorgesehenen Medien.

## 3 Stammkapital und Geschäftsanteile

Das Stammkapital beträgt 50.000 EUR. Kunibert Knopf hält den Geschäftsanteil mit der laufenden Nummer 1 im Nennbetrag von 20.000 EUR. Romy Yilmaz hält den Geschäftsanteil mit der laufenden Nummer 2 im Nennbetrag von 17.500 EUR. Thekla Spätzle hält den Geschäftsanteil mit der laufenden Nummer 3 im Nennbetrag von 12.500 EUR. Die Einlagen sind in Geld zu erbringen. Nach den zum 1. März 2023 vorliegenden Zahlungsbestätigungen sind die Einlagen vollständig geleistet.

## 4 Geschäftsführung und Vertretung

Die Gesellschaft hat einen oder mehrere Geschäftsführer. Sind mehrere Geschäftsführer bestellt, wird die Gesellschaft durch zwei Geschäftsführer gemeinschaftlich oder durch einen Geschäftsführer gemeinsam mit einem Prokuristen vertreten. Ist nur ein Geschäftsführer bestellt, vertritt er die Gesellschaft allein. Eine Befreiung von den Beschränkungen des § 181 BGB wird mit dieser Satzung nicht erteilt. Eine besondere Befreiung bedarf eines gesonderten zulässigen Gesellschafterbeschlusses und der erforderlichen weiteren Umsetzung.

Die Geschäftsführer führen die Geschäfte gemeinsam. Die interne Aufgabenverteilung lässt ihre gesetzlichen Pflichten unberührt. Maßnahmen außerhalb des gewöhnlichen Geschäftsbetriebs sind vor ihrer Durchführung miteinander abzustimmen. Die Gesellschafterversammlung kann eine Geschäftsordnung beschließen.

## 5 Fakultativ eingerichteter Beirat

Die Gesellschaft kann einen Beirat aus zwei externen, nicht an der Gesellschaft beteiligten Personen einrichten. Die Gesellschafterversammlung bestellt und entlässt die Mitglieder mit einfacher Mehrheit der abgegebenen Stimmen. Die Amtszeit beträgt drei Jahre; Wiederbestellung ist zulässig. Der Beirat berät die Geschäftsführung und übt ausschließlich die in dieser Satzung und einer darauf beruhenden Beiratsordnung ausdrücklich übertragenen internen Zustimmungsbefugnisse aus. Er ist kein Aufsichtsrat und vertritt die Gesellschaft nicht gegenüber Dritten.

Der Beirat entscheidet einstimmig. Seine Zustimmung ist vor Aufnahme, wesentlicher Änderung, Besicherung oder vorzeitiger Rückzahlung eines Darlehens mit einem Betrag von mehr als 25.000 EUR einzuholen. Sachlich zusammenhängende Teilgeschäfte werden zusammengerechnet. Dies gilt auch für Gesellschafterdarlehen und für wirtschaftlich vergleichbare Finanzierungsgeschäfte. Die ordnungsgemäße Erfüllung bereits wirksam vereinbarter, fälliger laufender Zinszahlungen bedarf keiner erneuten Zustimmung. Die Zustimmung ist mindestens in Textform zu dokumentieren. Eine bloße Kenntnisnahme oder die Teilnahme eines Beiratsmitglieds an einem Gespräch ersetzt sie nicht.

Der Zustimmungsvorbehalt gilt im Innenverhältnis. Die Vertretungsregelung nach Abschnitt 4 bleibt unberührt. Ist der Beirat nicht besetzt oder verweigert er die Zustimmung, kann die Geschäftsführung die Gesellschafterversammlung vor Durchführung des Geschäfts um eine Entscheidung ersuchen. Daraus folgt keine automatische Erteilung einer fehlenden Erklärung gegenüber dem Vertragspartner.

## 6 Einberufung der Gesellschafterversammlung

Jeder Geschäftsführer ist berechtigt, eine Gesellschafterversammlung einzuberufen. Die Einladung erfolgt mindestens 14 volle Kalendertage vor dem Versammlungstag in Textform an die zuletzt schriftlich mitgeteilte Post- oder E-Mail-Adresse jedes Gesellschafters. Der Tag des Zugangs und der Versammlungstag werden nicht mitgerechnet. Die Einladung nennt Ort, Zeit und die Tagesordnung so konkret, dass die Gesellschafter sich auf die Beschlussgegenstände vorbereiten können.

Ergänzungen der Tagesordnung sind allen Gesellschaftern mindestens sieben volle Kalendertage vor der Versammlung in Textform mitzuteilen. Der Zugangstag und der Versammlungstag werden nicht mitgerechnet. Über nicht rechtzeitig angekündigte Gegenstände wird nur beschlossen, wenn sämtliche Gesellschafter anwesend oder vertreten sind und mit der Beschlussfassung einverstanden sind. Jeder Gesellschafter darf sich durch einen anderen Gesellschafter oder einen zur beruflichen Verschwiegenheit verpflichteten Rechtsanwalt aufgrund einer Vollmacht in Textform vertreten lassen.

## 7 Leitung Stimmrechte und Mehrheiten

Die anwesenden oder vertretenen Gesellschafter wählen einen Versammlungsleiter mit einfacher Mehrheit der abgegebenen Stimmen. Der Versammlungsleiter stellt die Anwesenheit fest, leitet die Aussprache, lässt über jeden Beschlussantrag getrennt abstimmen und gibt die von ihm festgestellten Ergebnisse bekannt. Beanstandungen sind auf Verlangen in das Protokoll aufzunehmen.

Je ein EUR des Nennbetrags eines Geschäftsanteils gewährt eine Stimme. Beschlüsse werden grundsätzlich mit mehr als der Hälfte der gültig abgegebenen Stimmen gefasst. Stimmenthaltungen und ungültige Stimmen bleiben für die Berechnung dieser Mehrheit außer Betracht. Gesetzliche Stimmverbote bleiben unberührt. Die Zahlungsfähigkeit oder die Bereitschaft eines Gesellschafters zur Beteiligung an einer Kapitalmaßnahme begründet für sich allein kein zusätzliches satzungsmäßiges Stimmverbot.

Beschlüsse über Satzungsänderungen einschließlich einer Kapitalerhöhung und über die Zustimmung zur Übertragung von Geschäftsanteilen bedürfen mindestens 75 Prozent der gültig abgegebenen Stimmen. Die gesetzlich erforderlichen Formen, Zustimmungen und Registerhandlungen bleiben unberührt. Die Bestellung und Abberufung von Geschäftsführern unterliegt der einfachen Mehrheit, soweit zwingendes Recht nichts anderes verlangt. Die Wirksamkeit eines Beschlusses wird durch seine Aufnahme in das Protokoll nicht zusätzlich zugesichert.

## 8 Übertragung und Belastung von Geschäftsanteilen

Jede Übertragung oder Belastung eines Geschäftsanteils bedarf der vorherigen Zustimmung der Gesellschafterversammlung nach Abschnitt 7. Die Zustimmung kann sich auf einen konkret bezeichneten Erwerber und bestimmte Vertragsbedingungen beziehen. Sie ersetzt weder eine erforderliche notarielle Beurkundung noch die persönliche Vertragserklärung des veräußernden Gesellschafters. Eine Pflicht aller Gesellschafter, einem Verkauf ihrer Anteile zuzustimmen oder ihre Anteile mitzuverkaufen, wird mit dieser Satzung nicht begründet.

Ein Gesellschafter, der verkaufen möchte, legt den anderen Gesellschaftern Erwerber, Preis, wesentliche Bedingungen und den vorgesehenen Vollzugstermin in Textform offen. Unverbindliche Gespräche dürfen geführt werden; eine Bindung der übrigen Gesellschafter entsteht hierdurch nicht.

## 9 Einziehung aus wichtigem Grund

Ein Geschäftsanteil kann mit Zustimmung des betroffenen Gesellschafters eingezogen werden. Ohne dessen Zustimmung ist die Einziehung zulässig, wenn in seiner Person ein wichtiger Grund vorliegt, der den übrigen Gesellschaftern unter Abwägung aller Umstände die Fortsetzung der Gesellschaft mit ihm unzumutbar macht. Hierzu können insbesondere eine schwere schuldhafte Verletzung wesentlicher gesellschaftlicher Pflichten oder eine fortgesetzte erhebliche Schädigung der Gesellschaft gehören. Ein bloßer Meinungsunterschied über eine Geschäftsentscheidung genügt nicht allein.

Vor der Beschlussfassung ist dem betroffenen Gesellschafter Gelegenheit zu geben, zu den konkret bezeichneten Vorwürfen Stellung zu nehmen. Über die Einziehung wird für jeden betroffenen Anteil einzeln beschlossen. Der betroffene Gesellschafter ist bei der Abstimmung über die Einziehung seines eigenen Anteils nicht stimmberechtigt; sein Nennbetrag bleibt bei dieser Abstimmung für die Mehrheitsberechnung außer Betracht. Der Beschluss bedarf mindestens 75 Prozent der verbleibenden gültig abgegebenen Stimmen.

Die Einziehung wird mit Zugang der Beschlussmitteilung an den betroffenen Gesellschafter wirksam, soweit die gesetzlichen Voraussetzungen vorliegen. Sie darf nicht durchgeführt werden, wenn gesetzliche Voraussetzungen fehlen. Die Geschäftsführung hat insbesondere die für die Einziehung und die Finanzierung der Abfindung erforderlichen Angaben zu erheben und der Gesellschafterversammlung vorzulegen. Eine anderweitige Ausschließung eines Gesellschafters wird durch diesen Abschnitt nicht automatisch fingiert.

## 10 Abfindung

Bei einer Einziehung erhält der betroffene Gesellschafter eine Abfindung in Höhe des auf seinen Anteil entfallenden Verkehrswerts. Bewertungsstichtag ist der Tag des Einziehungsbeschlusses. Können sich die Beteiligten nicht binnen vier Wochen auf den Wert einigen, wird ein unabhängiger Wirtschaftsprüfer gemeinsam ausgewählt. Kommt auch darüber keine Einigung zustande, soll die Industrie- und Handelskammer Berlin um Benennung eines geeigneten Sachverständigen ersucht werden.

Die Abfindung ist in drei gleichen Jahresraten zu zahlen; die erste Rate ist sechs Monate nach verbindlicher Feststellung des Werts fällig. Der noch offene Betrag wird ab dem Bewertungsstichtag mit zwei Prozentpunkten über dem jeweiligen Basiszinssatz jährlich verzinst. Gesetzliche Zahlungsverbote bleiben unberührt. Die Stundung und die Ratenregelung heben zwingende Grenzen der Kapitalerhaltung nicht auf. Weitere Ansprüche und die gerichtliche Überprüfung bleiben unberührt.

## 11 Protokoll und gerichtliche Überprüfung

Über jede Versammlung wird ein Protokoll mit Teilnehmern, Anträgen, Abstimmungsergebnissen, Ergebnisfeststellungen und verlangten Widersprüchen gefertigt. Der Versammlungsleiter unterzeichnet das Protokoll und übersendet es unverzüglich an alle Gesellschafter. Eine Empfangsbestätigung bedeutet keine Zustimmung zum Inhalt.

Klagen zur Anfechtung von Gesellschafterbeschlüssen sind innerhalb eines Monats nach Zugang des Protokolls zu erheben. Zwingende gesetzliche Regelungen, insbesondere über nichtige Beschlüsse, bleiben unberührt. Der Ablauf dieser Frist wird nicht durch ein bloßes außergerichtliches Korrekturverlangen aufgehalten. Diese Regelung enthält keine Vereinbarung darüber, welche Beschlüsse im konkreten Fall anfechtbar oder nichtig sind.

## 12 Jahresabschluss und Ergebnisverwendung

Die Geschäftsführung stellt den Jahresabschluss innerhalb der gesetzlichen Fristen auf und legt ihn den Gesellschaftern vor. Über Feststellung des Jahresabschlusses und Verwendung des Ergebnisses entscheidet die Gesellschafterversammlung unter Beachtung zwingender Vorschriften. Ausschüttungen erfolgen entsprechend den Beteiligungsverhältnissen, soweit keine zulässige abweichende Vereinbarung getroffen wird.

## 13 Kosten und Schlussbestimmungen

Die Gesellschaft trägt Gründungskosten bis zu einem Gesamtbetrag von 2.500 EUR. Weitere Kostenregelungen ergeben sich aus dem jeweiligen Auftrag. Änderungen dieser Satzung bedürfen der gesetzlich vorgeschriebenen Form. Soweit einzelne Bestimmungen unwirksam sind, beurteilen sich ihre Folgen nach den gesetzlichen Vorschriften. Die übrigen Vertragsbestimmungen bleiben bestehen, soweit dies rechtlich zulässig ist.

Die vorliegende Arbeitsabschrift gibt den in der Gesellschaft abgelegten Satzungstext vom 1. März 2023 wieder. Sie ist keine beglaubigte Abschrift und ersetzt keinen aktuellen Register- oder Urkundennachweis.'''
DOCS=[
E('01_Mandatsauftrag_Romy.eml','Persönlicher Auftrag wegen der Versammlung und der nächsten Schritte','2026-10-02T08:15:00+02:00','Romy Yilmaz <romy@zink-zunder.example>','Clara Klee <clara@klee-kolben.example>','''Guten Morgen Frau Klee,

ich beauftrage Sie persönlich als Gesellschafterin. Bitte behandeln Sie das nicht als Auftrag der GmbH. Nach der Versammlung am 25. September weiß ich nicht, ob ich noch Geschäftsführerin sein soll und ob Kunibert und ich nach dem Protokoll überhaupt noch Anteile haben sollen. Ich bestreite die gegen mich gerichteten Feststellungen. Mein Protokollzugang war am Montag, 28. September, um 09.12 Uhr per E-Mail.

Bitte beraten Sie mich heute bis 16 Uhr zu den erforderlichen Schutzmaßnahmen, Fristen und den nächsten Schreiben. Ich brauche einen klaren persönlichen Handlungsplan, einen Entwurf zur Sicherung meiner Rechte und die nötigen vorbereiteten Dokumente, sofern gerichtliche Schritte notwendig sind. Bitte prüfen Sie jede Abstimmung gesondert und auch die Kapitalerhöhung. Der Notartermin ist erst für den 9. Oktober vorgesehen. Eine sofortige Versendung, Klage oder Registereingabe ist mit diesem Auftrag noch nicht freigegeben; bitte legen Sie mir die konkreten Entwürfe vor.

Ich will die Werkstatt erhalten. Ich kann im Moment nicht weitere 28.000 EUR einzahlen und möchte deshalb nicht meine Stimme oder meinen Anteil verlieren. Meine 60.000 EUR stehen weiterhin im Unternehmen. Das Darlehen von Kunibert habe ich allein auf der Seite der GmbH unterschrieben; Gundula war damals nicht dabei. Über meine eigene Verantwortung dürfen Sie mir bitte auch unangenehme Dinge deutlich sagen.

Freundliche Grüße
Romy Yilmaz'''),
D('02_Gesellschaft_und_Personen.docx','Gesellschaft und Personen bei Zink und Zunder','23.09.2026',FIRMA,'Interne Gesellschaftsablage','''## 1 Beteiligungen

Das Stammkapital beträgt 50.000 EUR. Nach der zuletzt im Gesellschaftsordner abgelegten Gesellschafterliste hält Kunibert Knopf 20.000 EUR und damit 40 Prozent, Romy Yilmaz 17.500 EUR und damit 35 Prozent sowie Thekla Spätzle 12.500 EUR und damit 25 Prozent. Diese Übersicht ist eine interne Abschrift. Eine aktualisierte amtliche Registerauskunft ist nicht beigefügt. Eine Abtretung oder Kapitaländerung nach 2023 ist in der Ablage nicht dokumentiert.

## 2 Geschäftsführung und Prokura

Kunibert Knopf betreut Werkstatt und Vertrieb. Romy Yilmaz verantwortet Projekte, Einkauf und die laufende kaufmännische Abstimmung. Beide sind seit der Gründung Geschäftsführer. Die abgelegte Vertretungsregel lautet: zwei Geschäftsführer gemeinsam oder ein Geschäftsführer gemeinsam mit einem Prokuristen. Eine Befreiung von § 181 BGB ist in den vorliegenden Bestellungsunterlagen nicht erteilt.

Gundula Pfennig ist als externe kaufmännische Fachkraft tätig und hat Gesamtprokura gemeinsam mit einem Geschäftsführer. Sie hält keine Anteile. Die tatsächlichen aktuellen Registereintragungen müssen anhand eines aktuellen Auszugs abgeglichen werden; diese Übersicht ist selbst kein Registerauszug.

## 3 Beirat und weitere Beteiligte

Der Beirat besteht aus der externen Wirtschaftsingenieurin Mechthild Mohn und dem externen Betriebswirt Samir Senf. Beide sind weder Gesellschafter noch Geschäftsführer und halten nach ihren Erklärungen auch keine Beteiligung an Fensterfuchs. Hanna Blech führt Gespräche über einen Kauf aller Geschäftsanteile für ihre eigene unternehmerische Tätigkeit. Ein Kaufvertrag ist nicht unterschrieben.

## 4 Ablage und Erreichbarkeit

Alle drei Gesellschafter haben den Versand von Einladungen und Protokollen an ihre hier verwendeten E-Mail-Adressen ausdrücklich angegeben. Die Postanschrift der GmbH lautet Werkhof Weißensee 14, 13088 Berlin. Kennungen wie BANK-ZZ oder IT-ZZ sind interne Ablagezeichen und keine echten Bank- oder Registeridentifikatoren.'''),
D('03_Satzung_Arbeitsabschrift_2023.docx','Satzung der Zink und Zunder Metallbau GmbH','01.03.2023',FIRMA,'Gesellschaftsablage',SATZUNG),
D('04_Bestellung_und_Vertretung.docx','Abschrift der Bestellung und Vertretungsregelung','01.03.2023',FIRMA,'Gesellschaftsablage','''## 1 Geschäftsführerbestellung

Die drei Gründungsgesellschafter bestellen Kunibert Knopf und Romy Yilmaz zu Geschäftsführern. Die Geschäftsführer sind jeweils nur gemeinsam mit einem weiteren Geschäftsführer oder einem Prokuristen zur Vertretung befugt. Eine Einzelvertretungsbefugnis wird keinem von ihnen erteilt. Von den Beschränkungen des § 181 BGB werden sie nicht befreit.

## 2 Prokura

Gundula Pfennig wird Gesamtprokura gemeinsam mit einem Geschäftsführer erteilt. Sie darf die Gesellschaft nicht allein vertreten. Eine Befreiung von § 181 BGB wird auch ihr nicht erteilt. Die Anmeldung der Bestellung und der Vertretungsregelung wird gesondert vorbereitet.

## 3 Interne Aufgaben

Kunibert Knopf übernimmt die technische Werkstattorganisation und den Vertrieb. Romy Yilmaz übernimmt Projektsteuerung, Einkauf und die kaufmännische Planung. Finanzierungen werden gemeinsam abgestimmt. Die Aufgabenverteilung ändert die gemeinschaftliche Vertretung und die Beiratsvorbehalte nicht.

## 4 Ablagevermerk

Diese am 23. September 2026 aus dem Gesellschaftsordner übertragene Abschrift gibt die damals abgelegten Beschlüsse wieder. Sie enthält keine beglaubigte Unterschrift, keine Urkundenrolle und keine amtliche Registerbescheinigung. Nachträgliche Sondervollmachten oder Befreiungsbeschlüsse befinden sich in dem übergebenen Ordner nicht.'''),
D('05_Beiratsordnung.docx','Beiratsordnung Zink und Zunder','15.03.2023',FIRMA,'Geschäftsführung und Beirat','''## 1 Bestellung und Aufgabe

Mechthild Mohn und Samir Senf werden für drei Jahre als externe Mitglieder des fakultativen Beirats bestellt. Der Beirat berät die Geschäftsführung. Er besitzt keine Vertretungsmacht nach außen. Seine Zuständigkeiten ergeben sich aus Abschnitt 5 der Satzung.

## 2 Anträge und Beschlüsse

Zustimmungsanträge werden gleichzeitig an beide Mitglieder übermittelt. Der Antrag nennt Vertragspartner, Betrag, Laufzeit, Zinsen, Sicherheiten, Zweck und erwartete Folgen für die Liquidität. Bei Gesellschaftergeschäften wird die Beteiligung des Vertragspartners ausdrücklich bezeichnet. Wesentliche Vertragsänderungen und vorzeitige Rückzahlungen oberhalb der satzungsmäßigen Grenze benötigen einen eigenen Antrag.

Eine Zustimmung kommt nur durch übereinstimmende ausdrückliche Erklärungen beider Mitglieder zustande. Der zuständige Geschäftsführer legt die Erklärungen zusammen mit der freigegebenen Vertragsfassung ab. Schweigen, eine informelle Gesprächsteilnahme oder die Bestätigung des Nachrichteneingangs gelten nicht als Zustimmung. Ohne ausreichende Angaben darf der Beirat Nachfragen stellen.

## 3 Informationsaustausch

Der Beirat kann die Geschäftsführung um die zur Beratung erforderlichen Unterlagen bitten. Er übernimmt dadurch weder die Geschäftsführung noch eine Abschlussprüfung. Erkennt er ungeklärte Zuständigkeits- oder Finanzierungsfragen, weist er die Geschäftsführung darauf hin. Er trifft keine verbindliche Entscheidung über streitige Gesellschafterbeschlüsse oder individuelle Ansprüche eines Gesellschafters.

## 4 Nachgetragener Ablagevermerk vom 23. September 2026

Gundula Pfennig hat bei Zusammenstellung dieser Arbeitsabschrift ergänzt: Die Gesellschafter haben die Bestellung beider Mitglieder am 10. März 2026 unverändert für weitere drei Jahre erneuert. Die entsprechende einfache Niederschrift liegt dem Personalbüro vor. Dieser Vermerk gehört nicht zum ursprünglichen Text vom 15. März 2023.'''),
D('06_Darlehen_Romy_60000.docx','Darlehensvertrag mit Romy Yilmaz','10.01.2025',ROMY,FIRMA,'''## 1 Parteien und Auszahlung

Romy Yilmaz gewährt der Zink & Zunder Metallbau GmbH ein Darlehen von 60.000 EUR. Die GmbH wird beim Abschluss dieses Vertrags durch Geschäftsführer Kunibert Knopf gemeinsam mit Prokuristin Gundula Pfennig vertreten. Romy Yilmaz handelt ausschließlich als Darlehensgeberin. Der Betrag ist am 10. Januar 2025 auf das Geschäftskonto der GmbH auszuzahlen und für den laufenden Geschäftsbetrieb bestimmt.

## 2 Zinsen

Das Darlehen wird mit 3 Prozent jährlich verzinst. Für das erste Kalenderjahr 2025 vereinbaren die Parteien unabhängig vom Auszahlungstag einen festen Zinsbetrag von 1.800 EUR, zahlbar am 30. Dezember 2025. Ab 2026 werden Zinsen zeitanteilig auf den tatsächlich noch offenen Darlehensbetrag berechnet; sie sind am 30. Dezember des jeweiligen Jahres fällig. Eine automatische Zinskapitalisierung ist nicht vereinbart.

## 3 Laufzeit und Rückzahlung

Das Darlehen ist am 31. Dezember 2027 zur Rückzahlung fällig. Vorzeitige Teilzahlungen können die Parteien vereinbaren. Das Recht zur außerordentlichen Kündigung aus wichtigem Grund bleibt unberührt. Ein Nachrang, ein Rangrücktritt, eine Sicherheit oder ein Verzicht auf Rückzahlung wird mit diesem Vertrag nicht vereinbart.

## 4 Unterlagen und Erklärungen

Änderungen sollen zu Beweiszwecken in Textform festgehalten werden; gesetzliche Formerfordernisse und individuelle Vereinbarungen bleiben unberührt. Die internen Zustimmungsunterlagen der Gesellschaft werden gesondert verwahrt. In dieser Vertragsabschrift wird nicht bestätigt, dass der Beirat eine Zustimmung erteilt hat.

## 5 Unterschriftsvermerk der Ablage

Die im Ordner vorhandene unterzeichnete Fassung trägt nach dem Ablagevermerk die Unterschriften Romy Yilmaz als Darlehensgeberin sowie Kunibert Knopf und Gundula Pfennig für die GmbH. Diese lesbare Arbeitsabschrift bildet keine Unterschriftsgrafik nach. Der Zahlungseingang von 60.000 EUR am 10. Januar 2025 und die Zahlung von 1.800 EUR am 30. Dezember 2025 sind in der Buchungsübersicht vermerkt. Eine Tilgung dieses Darlehens ist bis zum 30. September 2026 nicht gebucht.'''),
D('07_Darlehen_Kunibert_40000.docx','Darlehensvertrag mit Kunibert Knopf','01.06.2026',KUNI,FIRMA,'''## 1 Parteien und Zahlung

Kunibert Knopf stellt der Zink & Zunder Metallbau GmbH 40.000 EUR zur Verfügung. Der Betrag wird am 1. Juni 2026 auf das Geschäftskonto überwiesen. Er soll eine Materialbestellung für den Sommer überbrücken. Auf Seiten der GmbH ist in der vorliegenden Fassung ausschließlich Romy Yilmaz als Unterzeichnerin genannt.

## 2 Zinsen und Laufzeit

Das Darlehen wird mit 4 Prozent jährlich auf den jeweils offenen Betrag verzinst. Zinsen sind erstmals am 30. Dezember 2026 fällig. Der Darlehensbetrag soll spätestens am 31. Mai 2028 zurückgezahlt werden. Vorzeitige Teilrückzahlungen sind mit Zustimmung beider Vertragsparteien möglich. Sicherheiten, ein qualifizierter Rangrücktritt und ein allgemeiner Forderungsverzicht sind nicht vereinbart.

## 3 Änderungen

Änderungen sollen schriftlich dokumentiert werden. Die Darlehensgeberseite darf eine Auszahlung oder Rückzahlung nicht allein durch eine interne Buchungsanweisung ersetzen. Die gesetzlichen Rechte beider Parteien bleiben unberührt. Eine Beiratszustimmung wird in diesem Text nicht erklärt oder bescheinigt.

## 4 Übernommener Unterschriftsstand

Die ausgedruckte Fassung im Ordner trägt nach der Dokumentation des Personalbüros nur die Unterschriften Kunibert Knopf als Darlehensgeber und Romy Yilmaz für die GmbH. Gundula Pfennig hat diese Fassung nicht unterschrieben. Eine auf diesen Vertrag bezogene Sondervollmacht liegt nicht in der Akte. Es gibt keinen dokumentierten Gesellschafterbeschluss, der den Unterschriftsstand abschließend behandelt. Die Abschrift enthält keine nachgebildeten Unterschriften.

## 5 Buchungsvermerke

Am 1. Juni 2026 wurden 40.000 EUR als Eingang von Kunibert Knopf gebucht. Am 15. September 2026 wurden 30.000 EUR mit dem Text Teilrückzahlung Darlehen Knopf ausgezahlt. Im Darlehenskonto verbleiben rechnerisch 10.000 EUR Hauptforderung. Eine Zinszahlung für 2026 ist nicht gebucht. Diese Buchungsvermerke enthalten keine rechtliche Bestätigung des Vertragsschlusses oder der Rückzahlung.'''),
E('08_Beirat_Anfrage_Darlehen.eml','Unterlagen zu den Darlehen und zur Septemberzahlung','2026-09-21T10:20:00+02:00','Romy Yilmaz <romy@zink-zunder.example>','Mechthild Mohn <mechthild@beirat-mohn.example>','''Guten Tag Frau Mohn,

ich suche die Beiratszustimmungen zu meinem Darlehen von 60.000 EUR aus Januar 2025 und zum Darlehen von Kunibert über 40.000 EUR aus Juni 2026. In unserer gemeinsamen Ablage finde ich die Verträge, aber keine eindeutige Zustimmung beider Mitglieder. Kunibert meint, das sei jeweils im Gespräch erledigt worden.

Hinzu kommt die Teilrückzahlung von 30.000 EUR an Kunibert am 15. September. Bitte sehen Sie auch nach, ob Ihnen dafür ein Antrag vorlag. Ich habe die Zahlung im Bankverfahren freigegeben, weil Kunibert sagte, sein Geld sei nur für den Sommer gedacht gewesen. Das ist keine Erklärung von mir, dass alle erforderlichen Beschlüsse vorhanden waren.

Bitte sprechen Sie sich mit Herrn Senf ab und schicken Sie uns vorhandene Nachrichten. Ich möchte fehlende Unterlagen nicht durch Erinnerungen ersetzen.

Freundliche Grüße
Romy Yilmaz'''),
E('09_Beirat_Zwischenantwort.eml','Re Unterlagen zu den Darlehen','2026-09-23T14:40:00+02:00','Mechthild Mohn <mechthild@beirat-mohn.example>','Romy Yilmaz <romy@zink-zunder.example>','''Guten Tag Frau Yilmaz,

ich erinnere mich an ein Gespräch über Ihr Darlehen Anfang 2025. Ich habe bisher nur eine Nachricht gefunden, dass wir die Zahlen besprechen wollten. Eine ausdrückliche gemeinsame Zustimmung kann ich daraus nicht bestätigen. Herr Senf durchsucht seine Ablage noch.

Vom Darlehen über 40.000 EUR wusste ich dem Grunde nach, hatte aber vor dem Sommer keine abschließende Vertragsfassung mit Unterschriften gesehen. Die Teilrückzahlung von 30.000 EUR war mir vor Ihrer jetzigen Anfrage nicht konkret bekannt. Bitte verstehen Sie diese Mail weder als nachträgliche Zustimmung noch als Feststellung, dass es nirgendwo eine Zustimmung gibt.

Für eine belastbare Prüfung brauchen wir beide Verträge, die Zahlungsunterlagen und die damaligen Anfragen. Ich bitte darum, vorerst keine fehlenden Freigaben zu behaupten, sondern den Dokumentenstand offenzulegen.

Mit freundlichen Grüßen
Mechthild Mohn'''),
D('10_Zahlungsnachweis_15_September.docx','Interner Zahlungsnachweis zur Rückzahlung an Kunibert','16.09.2026','Gundula Pfennig\nKaufmännische Verwaltung\ngundula@zink-zunder.example',FIRMA,'''## 1 Buchung

Das Geschäftskonto BANK-ZZ weist zum 15. September 2026 eine Auszahlung von 30.000 EUR an Kunibert Knopf aus. Als Verwendungszweck wurde Teilrückzahlung Darlehen Knopf Juni 2026 eingetragen. Es handelt sich um eine Tilgung; eine zusätzliche Zinszahlung wurde nicht angewiesen. BANK-ZZ ist unsere interne Kontobezeichnung und keine IBAN.

## 2 Technischer Ablauf

Kunibert sandte den Zahlungswunsch am 14. September intern an Romy. Romy erfasste die Zahlung und gab sie am 15. September um 09.18 Uhr im Bankverfahren frei. Gundula bestätigte um 09.31 Uhr als zweite technische Freigeberin. Der Kontoauszug zeigt die Ausführung am selben Tag. Die zweite Freigabe dokumentiert den Zahlungsablauf; ein unterzeichneter Vertragsnachtrag oder eine Beiratsentscheidung war dem Vorgang nicht beigefügt.

## 3 Gespräch bei Freigabe

Kunibert erklärte, er benötige einen Teil seines Geldes für eine andere Anschaffung. Romy fragte, ob ausreichend Geld für Löhne und Material bleibe. Kunibert verwies auf erwartete Kundenzahlungen. Gundula prüfte den zum Freigabezeitpunkt sichtbaren Kontostand, nicht die rechtliche Wirksamkeit des Darlehens und nicht sämtliche Fälligkeiten.

## 4 Ablage

Der Banklauf ist in der Finanzarbeitsmappe zusammen mit den übrigen Septemberbewegungen erfasst. Dieser interne Nachweis ist keine amtliche Bankbescheinigung. Die ursprünglichen Bankunterlagen und die Nachrichten vom 14. September sollen bei Bedarf zusätzlich aus der Buchhaltung gesichert werden.'''),
E('11_Steuerbuero_Rueckfragen.eml','Darlehen Zinsen und Unterlagen für die Durchsicht','2026-09-29T13:05:00+02:00','Edda Erbs <edda@steuerbuero-erbs.example>','Gundula Pfennig <gundula@zink-zunder.example>','''Guten Tag Frau Pfennig,

für unsere laufende steuerliche Durchsicht benötige ich zu beiden Gesellschafterdarlehen die unterschriebenen Fassungen, die Zustimmungsunterlagen, den betrieblichen Finanzierungszweck und die damaligen Überlegungen zu Zinssatz und Laufzeit. Beim Darlehen von Frau Yilmaz fällt mir die feste erste Jahresverzinsung von 1.800 EUR trotz Auszahlung am 10. Januar auf; bitte reichen Sie die Vereinbarung dazu ein. Für Herrn Knopf stehen 4 Prozent im Vertrag. Für 2026 sehe ich noch keine Zinszahlung.

Bitte erläutern Sie die Tilgung von 30.000 EUR vom 15. September und legen Sie die Zahlungsfreigaben bei. Vertretung, wirtschaftliche Einordnung, Zinsberechnung und ein möglicher Fremdvergleich sind noch nicht abschließend geprüft. Ich habe weder eine verdeckte Gewinnausschüttung festgestellt noch liegt mir hierzu ein bestandskräftiger Steuerbescheid oder ein Gerichtsurteil vor.

Die Augustübersicht ist ein interner Buchungsstand und kein von uns geprüfter Abschluss. Bitte lassen Sie außerdem Fälligkeiten, offene Stundungsabreden und verfügbare weitere Mittel klären.

Mit freundlichen Grüßen
Edda Erbs'''),
D('12_Finanzgespraech_Kapitalbedarf.docx','Besprechung zum Finanzierungsbedarf der Werkstatt','08.09.2026',FIRMA,'Geschäftsführung und Beirat','''## 1 Gespräch und Anlass

Am 8. September besprachen Kunibert Knopf, Romy Yilmaz und Gundula Pfennig die Finanzierung der nächsten Monate. Für die vorgeschlagene Material- und Maschinenplanung wird ein zusätzlicher Mittelzufluss von 80.000 EUR angesetzt. Die Zahl ist ein Planungsvorschlag; sie ist nicht identisch mit sämtlichen bereits fälligen Verbindlichkeiten. Konkrete Aufträge, Liefertermine und verfügbare Kreditlinien müssen noch zusammengeführt werden.

## 2 Kapitalvorschlag

Kunibert schlägt vor, das Stammkapital von 50.000 auf 100.000 EUR zu erhöhen. Auf die neuen Geschäftsanteile von insgesamt 50.000 EUR sollen zusätzlich 30.000 EUR Aufgeld gezahlt werden. Kunibert möchte alle neuen Anteile übernehmen und insgesamt 80.000 EUR einzahlen. Er verlangt, dass Romy keine neuen Anteile erhält, weil sie derzeit kein zusätzliches Geld bereitstellen könne. Auch Thekla soll nach seinem Vorschlag nichts zeichnen.

Romy weist darauf hin, dass ihr Darlehen von 60.000 EUR weiterhin in der Gesellschaft steht. Sie möchte vor einer Entscheidung Alternativen, Beteiligungsfolgen und die neue Liquiditätsplanung sehen. Thekla erklärt, aktuell ebenfalls keine weitere Einlage zusagen zu wollen. Eine schriftliche Verzichtserklärung auf eigene Beteiligungsmöglichkeiten hat keine von beiden abgegeben.

## 3 Zahlenstand und Grenzen

Die interne Übersicht zum 31. August zeigt rechnerisch ein Eigenkapital von 7.000 EUR bei einer Bilanzsumme von 257.000 EUR. Forderungen und Vorräte sind noch nicht abschließend bewertet. Eine Unternehmensbewertung und eine Prognose liegen nicht vor. Der Bankbestand vom 31. August beträgt 42.000 EUR. Über eine Zahlungsunfähigkeit oder Überschuldung wurde in diesem Gespräch keine belastbare Feststellung getroffen.

## 4 Weiteres Vorgehen

Die Buchhaltung soll bis Anfang Oktober den Septemberbanklauf, die offenen Posten und die beiden Darlehenskonten zusammenstellen. Stundungen und zusätzliche Finanzierungsmöglichkeiten sind noch nicht bestätigt. Der Beirat soll eine vollständige Unterlage erhalten. Kunibert möchte die Kapitalfrage auf die nächste Gesellschafterversammlung setzen.'''),
D('13_Unverbindliches_Angebot_Hanna.docx','Unverbindlicher Erwerbsvorschlag für Zink und Zunder','03.09.2026','Hanna Blech\nBlechwerk Beteiligungen\nAtelierhof 6, 13353 Berlin\nhanna@blechwerk.example','Kunibert Knopf Romy Yilmaz und Thekla Spätzle','''## 1 Interesse

Ich interessiere mich für den Erwerb sämtlicher Geschäftsanteile an der Zink & Zunder Metallbau GmbH. Die Werkstatt und die Arbeitsplätze sollen nach meiner derzeitigen Planung am Standort verbleiben. Ich möchte die drei Gesellschafter in die Gespräche einbeziehen. Dieses Schreiben ist weder ein bindendes Kaufangebot noch eine Verpflichtung der Gesellschafter zum Verkauf.

## 2 Preisvorstellung

Für alle Geschäftsanteile zusammen stelle ich mir zunächst einen Kaufpreis von 150.000 EUR vor. Grundlage wäre ein noch zu vereinbarender schulden- und liquiditätsbezogener Kaufpreismechanismus nach Prüfung der Zahlen. Gesellschafterdarlehen sind in dieser Preiszahl nicht als abgegolten behandelt; ihre Ablösung, Übernahme oder Fortführung müsste ausdrücklich geregelt werden. Eine Abfindungsbewertung für einen internen Gesellschafterstreit ist mit dieser Preisvorstellung nicht verbunden.

## 3 Bedingungen

Ich benötige eine wirtschaftliche, steuerliche und rechtliche Prüfung der Gesellschaft. Bei einem Vertrag erwarte ich übliche, noch zu verhandelnde Garantien und Haftungsgrenzen. Offene Verbindlichkeiten, Eigentum an technischen Unterlagen und die Zusammenarbeit der bisherigen Geschäftsführung sind für mich wesentliche Punkte. Weder ein uneingeschränkter Garantieumfang noch ein Ausschluss jeglicher Verkäuferhaftung ist damit vorgegeben.

## 4 Ablauf

Wenn grundsätzlich Interesse besteht, möchte ich am 6. Oktober einen gemeinsamen Gesprächstermin wahrnehmen. Ein notarieller Kaufvertrag müsste gesondert ausgehandelt und von sämtlichen Verkäufern abgeschlossen werden. Es besteht keine Exklusivität und keine Verpflichtung, einzelne Gesellschafter gegen ihren Willen aus dem Vorgang herauszunehmen. Ich behalte mir vor, die Gespräche ohne Vertragsabschluss zu beenden.'''),
E('14_Hanna_Angebotsversand.eml','Mein erster unverbindlicher Vorschlag','2026-09-03T15:10:00+02:00','Hanna Blech <hanna@blechwerk.example>','Romy Yilmaz <romy@zink-zunder.example>','''Guten Tag Frau Yilmaz,

anbei mein erster unverbindlicher Erwerbsvorschlag, den ich heute inhaltsgleich auch Herrn Knopf und Frau Spätzle übersende. Mir ist ein gemeinsames Gespräch mit allen drei Gesellschaftern wichtig. Die 150.000 EUR sind ein Ausgangspunkt für die Prüfung und keine verbindliche Zusage.

Die Gesellschafterdarlehen sollten wir gesondert erfassen. Ich möchte keine ungeklärte private Auseinandersetzung übernehmen. Bitte nennen Sie mir früh, welche Garantien oder Preisbedingungen für Sie wesentlich sind. Am 6. Oktober habe ich noch Zeit für eine Besprechung.

Mit freundlichen Grüßen
Hanna Blech'''),
E('15_Romy_Garantien_und_Preis.eml','Vor einem Verkauf brauche ich Klarheit','2026-09-04T11:05:00+02:00','Romy Yilmaz <romy@zink-zunder.example>','Hanna Blech <hanna@blechwerk.example>','''Guten Tag Frau Blech,

vielen Dank. Ich bin zu Gesprächen bereit, möchte aber vor einer Zustimmung wissen, wie mein Darlehen von 60.000 EUR behandelt wird. Für meinen Anteil stelle ich mir derzeit mindestens 60.000 EUR vor, zusätzlich zur gesonderten Darlehensregelung. Das ist meine Verhandlungsposition, keine mit den anderen Gesellschaftern abgestimmte Unternehmensbewertung.

Ich kann keine unbegrenzte persönliche Garantie für alle früheren Geschäftsvorfälle abgeben. Bitte lassen Sie uns Haftungsobergrenzen, Wissensqualifikationen und die konkrete Verteilung möglicher Risiken besprechen. Ich will den Verkauf nicht grundsätzlich verhindern; ich möchte einen Vertrag, den ich verantworten kann.

Bitte beziehen Sie mich in die nächste Fassung ein. Eine Vollmacht an Kunibert, meinen Anteil zu veräußern, habe ich nicht erteilt.

Freundliche Grüße
Romy Yilmaz'''),
dict(file='16_Chat_Verkaeufergruppe.txt',title='Chatverlauf Verkaufsgespräch',date='07.09.2026',body='''Export der Gruppe Zukunft Werkstatt durch Thekla Spätzle am 7. September 2026.

04.09.2026 16:12 | Kunibert Knopf: Hanna kauft nur das ganze Paket. Wenn jeder extra Bedingungen stellt, ist sie weg.
04.09.2026 16:19 | Romy Yilmaz: Ich verkaufe nicht blind mit unbeschränkten Garantien. Mein Darlehen ist auch noch da.
04.09.2026 16:23 | Thekla Spätzle: Wir haben doch noch gar keinen Vertrag. Lasst uns die Punkte erst sammeln.
07.09.2026 09:03 | Kunibert Knopf: Für mich ist das Blockade. Gleichzeitig braucht die Werkstatt frisches Geld.
07.09.2026 09:17 | Romy Yilmaz: Bedingungen aushandeln ist nicht dasselbe wie nie verkaufen. Bitte sag Hanna nicht, ich hätte alles abgelehnt.
07.09.2026 09:28 | Thekla Spätzle: Ich möchte die Zahlen sehen. Mit 150.000 als Gesprächseinstieg kann ich leben, unterschrieben habe ich nichts.'''),
D('17_Fensterfuchs_Projektprofil.docx','Projektprofil Fensterfuchs Metallwerk','16.09.2026','Fensterfuchs Metallwerk UG in Vorbereitung\nKontakt Kunibert Knopf\nkunibert@fensterfuchs.example','Interessenten','''## 1 Vorhaben

Unter dem Namen Fensterfuchs Metallwerk soll eine kleine Werkstatt für individuelle Metallfenster und Montagehilfen aufgebaut werden. Kunibert Knopf betreut die Vorbereitung. Derzeit werden Angebote für Räume und Maschinen eingeholt. Als künftige Rechtsform ist eine Unternehmergesellschaft vorgesehen. Dieses Projektblatt behauptet keine bereits abgeschlossene Handelsregistereintragung.

## 2 Angebotene Leistungen

Vorgesehen sind die Planung kleiner Metallkonstruktionen, die Fertigung von Sonderfenstern und die Begleitung von Montagen. Erste Anfragen sollen zunächst geprüft werden. Verbindliche Lieferzusagen, ein bestehender Maschinenpark oder eine schon besetzte Belegschaft werden mit diesem Blatt nicht bestätigt.

## 3 Unterlagen

Für die Vorbereitung werden eigene Erfahrungen, öffentlich zugängliche Produktinformationen und rechtmäßig nutzbare Entwürfe benötigt. Die Rechte an fremden Modellen und Kundendaten müssen vor einer Nutzung geklärt werden. Dieses Blatt enthält keine Freigabe der Zink & Zunder Metallbau GmbH zur Übernahme ihrer Unterlagen.

## 4 Kontakt

Anfragen können an Kunibert Knopf unter kunibert@fensterfuchs.example gerichtet werden. Eine separate Geschäftskontonummer oder eine Registerkennung wird noch nicht mitgeteilt. Das Profil wurde am 16. September als Word-Anlage an einen interessierten Kontakt versandt.'''),
E('18_Kundenanfrage_Altbogen.eml','Wer bearbeitet unsere Fensteranfrage künftig','2026-09-18T09:25:00+02:00','Marta Alt <marta@altbogen.example>','Romy Yilmaz <romy@zink-zunder.example>','''Guten Tag Frau Yilmaz,

Herr Knopf hat mir das Profil Fensterfuchs geschickt. Ich bin nun unsicher, ob unsere neue Anfrage für die Metallfenster in der Hofdurchfahrt von Zink & Zunder oder von seinem neuen Projekt bearbeitet werden soll. Der laufende Treppenauftrag bleibt aus unserer Sicht bei Ihrer GmbH. Die Zahlung vom 4. September betraf diesen alten Auftrag.

Für die Fenster gibt es noch keinen Auftrag und keinen vereinbarten Preis. Die Zeichnung, die ich Herrn Knopf am 11. September geschickt habe, stammt aus unserem Planungsbüro; die Nutzungsrechte müssten wir bei einer Beauftragung regeln. Ich habe ihm keine pauschale Erlaubnis gegeben, unsere vollständigen Projektunterlagen an ein neues Unternehmen weiterzureichen.

Bitte melden Sie sich mit einer klaren Zuständigkeit. Wir möchten den guten Kontakt zur Werkstatt behalten und keinen internen Streit auslösen.

Freundliche Grüße
Marta Alt'''),
dict(file='19_CAD_Zugriffsprotokoll.txt',title='Export technischer Dateizugriffe',date='22.09.2026',body='''Interne Kennung IT-ZZ. Export durch Milena Roth, externer IT-Service. Zeitzone Europe/Berlin. Auszug aus dem Dateiserverprotokoll für die genannten Vorgänge, kein vollständiges Geräteabbild.

11.09.2026 14:08 | Benutzer k.knopf | Lesen | Projekte/Altbogen/Kundenplan_Hofdurchfahrt_v1.dwg | Dateigröße 4.820.144 Byte.
16.09.2026 18:42 | Benutzer k.knopf | Lesen | Entwicklung/Fensterrahmen_ZZ_2025_v7.step | Dateigröße 8.145.200 Byte.
16.09.2026 18:43 | Benutzer k.knopf | Kopieren auf verbundenes USB-Laufwerk | Entwicklung/Fensterrahmen_ZZ_2025_v7.step | Dateigröße 8.145.200 Byte.
16.09.2026 18:44 | Benutzer k.knopf | Kopieren auf verbundenes USB-Laufwerk | Projekte/Altbogen/Kundenplan_Hofdurchfahrt_v1.dwg | Dateigröße 4.820.144 Byte.
17.09.2026 07:50 | Benutzer r.yilmaz | Lesen | Entwicklung/Fensterrahmen_ZZ_2025_v7.step | Dateigröße 8.145.200 Byte.

Die Benutzerkennung bezeichnet das angemeldete Konto. Die Protokolldatei weist keine spätere Nutzung bei einem anderen Unternehmen nach. Die Zuordnung der Urheber- und Nutzungsrechte ist nicht Gegenstand des technischen Exports. Der ursprüngliche Serverbestand wurde nicht gelöscht.'''),
D('20_IT_Vermerk_und_Rechte.docx','Vermerk zum CAD Export und zur Ablage','22.09.2026','Milena Roth\nExterner IT-Service\nit@roth-service.example',FIRMA,'''## 1 Technischer Befund

Ich habe die in der beigefügten Textdatei bezeichneten Serverereignisse ausgelesen. Das Konto k.knopf hat am 16. September zwei Dateien auf ein verbundenes USB-Laufwerk kopiert. Der Serverbestand blieb bestehen. Ob Kunibert persönlich am Gerät saß, ergibt sich aus dem Ereignisprotokoll allein nicht. Eine Weiterleitung per E-Mail und ein Import in ein fremdes System wurden mit diesem Auftrag nicht untersucht.

## 2 Dateiherkunft

Der Dateiname Fensterrahmen_ZZ_2025_v7 gehört zu einem gemeinsamen Entwicklungsordner. Laut Projektnotiz haben Romy, Kunibert und ein früherer externer Zeichner daran gearbeitet. Die Rechtevereinbarung mit dem Zeichner habe ich nicht. Der Kundenplan Hofdurchfahrt wurde von Marta Alt übermittelt und ist im Kundenordner abgelegt. Aus einem Dateinamen folgt für mich kein Alleineigentum an sämtlichen technischen oder urheberrechtlichen Positionen.

## 3 Zugriffsorganisation

Beide Geschäftsführer besitzen persönliche Kennungen. Der Entwicklungsordner ist nicht öffentlich freigegeben. Der Zugriff ist auf die beiden Geschäftsführer und zwei benannte Beschäftigte beschränkt; Änderungen werden protokolliert. Ein vom System erzwungenes Verbot, USB-Datenträger zu verwenden, bestand nicht. Ob eine arbeits- oder gesellschaftsrechtliche Vorgabe verletzt wurde, habe ich nicht geprüft.

## 4 Sicherung

Eine unveränderte Kopie des Logauszugs liegt bei der kaufmännischen Verwaltung. Ich habe keine privaten Geräte untersucht und keine Postfächer geöffnet. Vor einer weitergehenden Sicherung sollten Auftrag, Berechtigung, Umfang und die betroffenen Daten geklärt werden. Bis dahin wurden die Logdaten gegen routinemäßiges Überschreiben gesichert.'''),
E('21_Kunibert_Stellungnahme.eml','Fensterfuchs und die Dateien','2026-09-23T18:05:00+02:00','Kunibert Knopf <kunibert@zink-zunder.example>','Romy Yilmaz <romy@zink-zunder.example>','''Romy,

ich habe die Dateien für ein Gespräch mit einem möglichen Maschinenanbieter auf den Stick kopiert. Ich bestreite nicht, den Stick benutzt zu haben. Ich habe aber nach meiner Erinnerung keine Kundendatei bei Fensterfuchs eingespielt und keinen Zink-&-Zunder-Auftrag dorthin umgebucht. Die Anfrage von Altbogen war ein neues Fensterprojekt, noch kein Auftrag.

Fensterfuchs ist bislang ein Vorhaben. Ich will mir eine Perspektive offenhalten, falls unser Verkauf oder die Finanzierung scheitert. An dem Rahmenmodell habe ich selbst mitgearbeitet. Mir ist klar, dass das nicht automatisch alle Rechte an den anderen Beiträgen klärt. Den Stick kann ich zu einer gemeinsam vereinbarten Sicherung mitbringen; meine privaten Dateien darauf möchte ich nicht pauschal herausgeben.

Ich finde deinen Ton überzogen. Gleichzeitig halte ich die alleinige Unterschrift unter mein Darlehen und deine Haltung zum Verkauf für klärungsbedürftig. Lass uns die Vorgänge in der Versammlung getrennt besprechen.

Kunibert'''),
D('22_Einladung_09_September.docx','Einladung zur Gesellschafterversammlung am 25 September 2026','09.09.2026','Kunibert Knopf\nGeschäftsführer\nkunibert@zink-zunder.example','Romy Yilmaz und Thekla Spätzle','''Sehr geehrte Mitgesellschafterinnen,

ich lade Sie zur Gesellschafterversammlung am Freitag, 25. September 2026, um 10 Uhr in den Besprechungsraum der Werkstatt, Werkhof Weißensee 14, 13088 Berlin, ein. Die folgenden Gegenstände sollen getrennt beraten und beschlossen werden.

## 1 Eröffnung und Leitung

Feststellung der Teilnehmer und Wahl der Versammlungsleitung.

## 2 Finanzierung und Kapitalerhöhung

Beschlussvorschlag: Das Stammkapital soll von 50.000 EUR auf 100.000 EUR erhöht werden. Der neue Geschäftsanteil von 50.000 EUR soll ausschließlich Kunibert Knopf zur Übernahme angeboten werden. Auf den neuen Anteil soll ein Aufgeld von 30.000 EUR gezahlt werden. Romy Yilmaz und Thekla Spätzle sollen von der Beteiligung an dieser Ausgabe ausgeschlossen sein. Kunibert soll insgesamt 80.000 EUR einzahlen. Die entsprechende Änderung der Satzung und ein Notartermin sollen vorbereitet werden. Es wird für diesen Versammlungstermin keine notarielle Beurkundung organisiert.

## 3 Platz für angekündigte Ergänzung

Romy hat Einwände gegen Kuniberts Nebenprojekt angekündigt. Ein konkret formulierter Ergänzungsantrag wird allen Gesellschaftern gesondert übersandt, sobald er vorliegt. Mit dieser Ankündigung wird noch kein unbestimmter Ausschlussbeschluss zur Abstimmung gestellt.

## 4 Geschäftsführung und Beteiligung von Romy Yilmaz

Ich beantrage, Romy Yilmaz wegen der aus meiner Sicht pflichtwidrigen Abwicklung meines Darlehens und der von mir beanstandeten Behinderung der Verkaufsgespräche aus wichtigem Grund als Geschäftsführerin abzuberufen. Getrennt hiervon beantrage ich die Einziehung ihres Geschäftsanteils Nr. 2 aus wichtigem Grund. Die einzelnen Vorgänge und Romys Stellungnahme sollen vor den Abstimmungen erörtert werden.

## 5 Erwerbsgespräch mit Hanna Blech

Beschlussvorschlag: Zustimmung zur Veräußerung sämtlicher Anteile an Hanna Blech auf Grundlage eines noch zu verhandelnden Kaufvertrags mit einem Gesamtkaufpreis von zunächst 150.000 EUR. Eine Verpflichtung zur Unterzeichnung soll im Wortlaut des Beschlusses nicht erklärt werden. Die Gesellschafterdarlehen sind gesondert zu behandeln.

## 6 Unterlagen zu Darlehen und Liquidität

Aussprache über Darlehensverträge, Zustimmungen, Zinsen und Liquiditätsplanung sowie Beauftragung der Zusammenstellung fehlender Unterlagen. Eine abschließende Genehmigung ungeklärter Verträge ist unter diesem Tagesordnungspunkt nicht beantragt.

Bitte bestätigen Sie den Zugang der Einladung. Die vorhandenen Verträge, die Satzung und Hannas Vorschlag liegen im Gesellschaftsordner. Sie können die Unterlagen vor dem Termin einsehen und eigene Kopien für die Vorbereitung erhalten.

Mit freundlichen Grüßen
Kunibert Knopf'''),
E('23_Einladung_Zugang.eml','Einladung 25 September und Zugangsbestätigungen','2026-09-09T17:35:00+02:00','Gundula Pfennig <gundula@zink-zunder.example>','Kunibert Knopf <kunibert@zink-zunder.example>','''Guten Tag Herr Knopf,

ich habe Ihre Einladung heute um 09.10 Uhr unverändert an Romy und Thekla versandt; die identische Word-Datei hängt zur Dokumentation an dieser Nachricht. Romy bestätigte den Erhalt heute um 10.02 Uhr mit dem Text Einladung erhalten, ich komme. Thekla antwortete um 11.26 Uhr mit dem Text Bei mir angekommen, Termin ist eingetragen.

Alle drei Adressen entsprechen den im Gesellschaftsordner benannten Adressen. Die beiden Antworten sind im Büro abrufbar. Es wurde keine Weiterleitung an unbeteiligte Beschäftigte vorgenommen. Der Termin findet in Präsenz statt, nicht per Videokonferenz.

Bitte reichen Sie mir einen konkret formulierten Ergänzungsantrag rechtzeitig, falls Romy ihn übersendet. Ich kann nur den Versand dokumentieren, nicht die Beschlussvorschläge rechtlich freigeben.

Freundliche Grüße
Gundula Pfennig'''),
E('24_Romy_Ergaenzungsantrag.eml','Ergänzung zu TOP 3 bitte vollständig an alle','2026-09-11T15:40:00+02:00','Romy Yilmaz <romy@zink-zunder.example>','Kunibert Knopf <kunibert@zink-zunder.example>','''Kunibert,

ich verlange die konkrete Aufnahme folgender zwei getrennten Anträge unter TOP 3: deine Abberufung als Geschäftsführer aus wichtigem Grund und die Einziehung deines Geschäftsanteils Nr. 1 aus wichtigem Grund. Ich stütze die Anträge auf die Vorbereitung eines unmittelbaren Konkurrenzbetriebs, die Ansprache unseres Kunden Altbogen und den Verdacht der Nutzung unserer Entwicklungsunterlagen. Die Tatsachen und deine Erklärung sollen vor einer Entscheidung erörtert werden.

Zum jetzigen Zeitpunkt habe ich das Fensterfuchs-Vorhaben und die Kundenansprache angesprochen; den genauen technischen Zugriff lassen wir noch klären. Ich behaupte nicht, dass damit bereits alle Rechtefragen entschieden sind. Bitte übersende den Nachtrag morgen an alle, damit niemand von den Anträgen erst im Raum erfährt.

Ich bin mit der Aufnahme deiner Anträge gegen mich nicht einverstanden, werde dazu aber Stellung nehmen. Ein Verzicht auf Einwände oder auf meine Stimmrechte ist diese Mail nicht.

Romy'''),
D('25_Tagesordnung_Nachtrag.docx','Ergänzung der Tagesordnung für den 25 September 2026','12.09.2026','Kunibert Knopf\nGeschäftsführer', 'Kunibert Knopf Romy Yilmaz und Thekla Spätzle','''Die Einladung vom 9. September 2026 wird ausschließlich hinsichtlich TOP 3 wie folgt konkretisiert. Ort und Zeit bleiben unverändert. Die beiden Anträge sind getrennt zu behandeln.

## 3.1 Abberufung von Kunibert Knopf

Romy Yilmaz beantragt, Kunibert Knopf aus wichtigem Grund als Geschäftsführer abzuberufen. Sie begründet dies mit der Vorbereitung eines aus ihrer Sicht konkurrierenden Unternehmens Fensterfuchs, der Ansprache des Kunden Altbogen und dem Verdacht der Nutzung von Entwicklungsunterlagen der GmbH. Kunibert soll vor der Abstimmung Gelegenheit zur Stellungnahme erhalten. Die tatsächlichen Zugriffe und die Rechte an den Unterlagen sind bislang nicht abschließend geklärt.

## 3.2 Einziehung des Geschäftsanteils von Kunibert Knopf

Romy Yilmaz beantragt getrennt hiervon die Einziehung des Geschäftsanteils Nr. 1 von Kunibert Knopf im Nennbetrag von 20.000 EUR aus wichtigem Grund. Sie beruft sich auf dieselben Vorgänge. Über Abfindung, Bewertung und die vorgelegten Finanzangaben ist vor einer Entscheidung zu sprechen. Eine bestimmte Abfindungssumme wird mit dem Antrag nicht festgelegt.

## 3.3 Weitere Unterlagen zur Ergänzung

Kunibert und Romy sollen vor der Versammlung die Unterlagen zu den von ihnen erhobenen Vorwürfen verfügbar machen. Die Vorlage weiterer Belege ersetzt nicht die Aussprache. Die übrigen Gegenstände der Einladung bleiben bestehen. Über neue, nicht angekündigte Beschlussgegenstände soll ohne Zustimmung aller Gesellschafter nicht abgestimmt werden.

Kunibert Knopf'''),
E('26_Nachtrag_Zugang.eml','Tagesordnungsnachtrag heute an alle zugestellt','2026-09-12T13:15:00+02:00','Gundula Pfennig <gundula@zink-zunder.example>','Romy Yilmaz <romy@zink-zunder.example>','''Guten Tag Frau Yilmaz,

anbei der konkretisierte Nachtrag, den Herr Knopf heute freigegeben hat. Ich habe dieselbe Datei um 09.05 Uhr an Sie, Herrn Knopf und Frau Spätzle geschickt. Herr Knopf bestätigte um 09.12 Uhr den Erhalt, Sie antworteten um 09.38 Uhr mit Erhalten und Thekla um 12.47 Uhr mit Gelesen, die beiden Punkte sind klar.

Die Rückmeldungen bestätigen aus meiner Sicht nur den technischen Zugang und keine Zustimmung zum Inhalt. Ihre Unterlagen zum Nebenprojekt können vor dem Termin ergänzt werden. Ich lege die Einladung und den Nachtrag zusammen ab. Das Personalbüro wird keine Abstimmungen vorwegnehmen und keine Teilnehmerrechte aus der E-Mail-Antwort ableiten.

Freundliche Grüße
Gundula Pfennig'''),
D('27_Protokoll_25_September.docx','Protokoll der Gesellschafterversammlung vom 25 September 2026','28.09.2026',FIRMA,'Kunibert Knopf Romy Yilmaz und Thekla Spätzle','''## 1 Teilnehmer und Leitung

Die Versammlung findet am 25. September 2026 von 10.00 bis 12.15 Uhr im Besprechungsraum der Werkstatt statt. Kunibert Knopf, Romy Yilmaz und Thekla Spätzle sind während sämtlicher Abstimmungen persönlich anwesend. Gundula Pfennig fertigt Notizen; sie hat keine Stimme. Ein Notar ist nicht anwesend. Thekla wird mit den Stimmen aller drei Gesellschafter zur Leiterin gewählt. Einladung und Nachtrag werden als zugegangen bezeichnet. Romy und Kunibert behalten ihre Einwände zu den konkreten Anträgen ausdrücklich vor.

Thekla verwendet für die Dokumentation jedes einzelnen Votums die zu Beginn vorliegende Beteiligungsliste mit 20.000 Stimmen für Kunibert, 17.500 für Romy und 12.500 für sich. Sie kündigt an, wegen der wechselseitigen Streitigkeiten keine geänderte Gesellschafterliste als bereits gesichert zugrunde zu legen. Ob frühere Feststellungen Folgen für spätere Abstimmungen haben, wird in der Versammlung nicht rechtlich geklärt.

## 2 Kapitalerhöhung und Beteiligung

Kunibert hält seinen angekündigten Antrag aufrecht: Erhöhung des Stammkapitals auf 100.000 EUR, alleinige Übernahme des neuen Anteils von 50.000 EUR durch ihn und zusätzlich 30.000 EUR Aufgeld. Romy und Thekla sollen keine neuen Anteile erhalten. Romy verlangt Alternativen und widerspricht einem Ausschluss ihrer Stimme. Sie erklärt, sie könne derzeit nicht weiteres Geld zusagen; sie gibt keine Verzichtserklärung ab.

Um 10.32 Uhr stimmt Kunibert mit 20.000 Stimmen dafür, Romy mit 17.500 dagegen und Thekla mit 12.500 dafür. Thekla erklärt auf Kuniberts Anregung, Romys Stimme werde wegen ihrer fehlenden Finanzierungsfähigkeit nicht mitgezählt. Sie stellt den Antrag mit 32.500 von 32.500 gewerteten Stimmen als angenommen fest. Romy widerspricht sofort sowohl ihrer Nichtberücksichtigung als auch der Ergebnisfeststellung und verlangt die Aufnahme ihres Nein-Votums. Ihre Erklärung wird aufgenommen.

Eine notarielle Beurkundung findet nicht statt. Der Notartermin zur weiteren Befassung ist für den 9. Oktober angefragt. Es liegen weder eine Übernahmeerklärung in der erforderlichen Form noch eine Registeranmeldung oder Eintragung zu dieser Kapitalmaßnahme vor. Kunibert hat die 80.000 EUR noch nicht eingezahlt.

## 3 Anträge gegen Kunibert Knopf

Romy erläutert das Fensterfuchs-Projekt, die Anfrage von Altbogen und den inzwischen vorliegenden CAD-Zugriff. Kunibert räumt das Kopieren auf einen USB-Stick ein, bestreitet aber eine Weiterverwendung in einem Konkurrenzbetrieb. Er verlangt die Prüfung der Rechte des externen Zeichners und der Kundin. Eine Einigung über diese Tatsachen wird nicht erreicht.

## 3.1 Abberufung

Um 10.58 Uhr stimmt Romy mit 17.500 Stimmen für Kuniberts Abberufung aus wichtigem Grund. Kunibert stimmt mit 20.000 dagegen. Thekla enthält sich mit 12.500 Stimmen. Thekla zählt Kuniberts Nein mit, lässt ihre Enthaltung im Nenner außer Betracht und stellt den Antrag bei 17.500 Ja und 20.000 Nein als abgelehnt fest. Romy widerspricht der Mitberücksichtigung Kuniberts und der Ergebnisfeststellung. Kunibert widerspricht einer Behandlung als bereits abberufener Geschäftsführer.

## 3.2 Einziehung

Um 11.12 Uhr stimmen Romy mit 17.500 und Thekla mit 12.500 Stimmen für die Einziehung von Kuniberts Anteil Nr. 1. Kunibert gibt mit 20.000 Stimmen ein Nein ab und widerspricht dem Antrag sowie seiner Nichtberücksichtigung. Thekla zählt seine Stimme unter Hinweis auf die Satzung nicht mit und stellt den Antrag mit 30.000 von 30.000 gewerteten Stimmen vorläufig als angenommen fest. Kunibert verlangt ausdrücklich die Aufnahme seines Widerspruchs.

Ein Abfindungswert wird nicht ermittelt. Die Augustzahlen liegen vor, sind aber nicht geprüft. Eine Finanzierung der Abfindung wird weder zugesagt noch durch einen Beleg nachgewiesen. Thekla erklärt, ihre Feststellung solle vor jeder Umsetzung rechtlich geprüft werden. Über einen endgültigen bereinigten Gesellschafterbestand herrscht keine Einigkeit.

## 4 Anträge gegen Romy Yilmaz

Kunibert beanstandet Romys alleinige Unterschrift unter seinem Darlehen, ihre Freigabe der Teilrückzahlung und ihre Bedingungen zum Verkauf. Romy weist darauf hin, dass er Darlehensgeber und Empfänger der Rückzahlung war, dass sie sich auf seine Angaben verlassen habe und dass sie einen Verkauf nicht grundsätzlich ablehne. Sie will ihre eigene Verantwortung prüfen lassen, bestreitet aber die behaupteten Ausschlussgründe.

## 4.1 Abberufung

Um 11.34 Uhr stimmt Kunibert mit 20.000 Stimmen für Romys Abberufung aus wichtigem Grund. Thekla stimmt mit 12.500 dagegen; Romy stimmt mit 17.500 dagegen. Thekla lässt Romys Stimme nicht in die Wertung eingehen und stellt den Antrag mit 20.000 Ja und 12.500 Nein vorläufig als angenommen fest. Romy widerspricht dem Stimmrechtsausschluss, der Tatsachengrundlage und dem festgestellten Ergebnis. Sie erklärt, die gegen Kunibert gerichtete frühere Feststellung dürfe nicht ohne Prüfung übergangen werden.

## 4.2 Einziehung

Um 11.47 Uhr stimmen Kunibert mit 20.000 und Thekla mit 12.500 Stimmen für die Einziehung von Romys Anteil Nr. 2. Romy gibt mit 17.500 Stimmen ein Nein ab. Thekla zählt dieses Nein nicht und stellt den Antrag mit 32.500 von 32.500 gewerteten Stimmen vorläufig als angenommen fest. Romy widerspricht sofort dem Antrag, ihrer Nichtberücksichtigung und der Ergebnisfeststellung. Kunibert erklärt, er akzeptiere die Einziehung seines eigenen Anteils weiterhin nicht.

Auch für Romys Anteil werden weder ein Abfindungswert noch eine gesicherte Finanzierung festgestellt. Thekla bittet, aus den widersprüchlichen Feststellungen keine bereits abgestimmte neue Eigentümer- oder Vertretungslage abzuleiten. Eine Vollzugsentscheidung oder eine gesonderte Klärung der Reihenfolge erfolgt nicht.

## 5 Verkauf an Hanna Blech

Um 12.02 Uhr stimmen Kunibert mit 20.000 und Thekla mit 12.500 Stimmen für die Zustimmung zum Verkauf aller Anteile an Hanna Blech auf der beschriebenen Verhandlungsgrundlage. Romy stimmt mit 17.500 dagegen und verweist auf Preis, Darlehen und Garantien. Thekla berücksichtigt alle drei abgegebenen Stimmen. Sie stellt 32.500 Ja von insgesamt 50.000 Stimmen und damit 65 Prozent fest und erklärt den Antrag bei der vorgesehenen 75-Prozent-Mehrheit für abgelehnt. Es wird kein Kaufvertrag unterschrieben und keine Vertretungsvollmacht für Romys Anteil erteilt.

## 6 Unterlagen und Schluss

Alle drei wollen die Darlehens- und Zustimmungsunterlagen zusammenstellen lassen. Diese Verständigung enthält keine Genehmigung eines streitigen Darlehens oder einer Rückzahlung, keinen Anspruchsverzicht und keine Entlastung. Gundula soll die Septemberbuchungen und die offenen Posten zusammenführen. Eine abschließende Feststellung zu Steuern oder Insolvenzgründen findet nicht statt.

Thekla schließt die Sitzung um 12.15 Uhr. Sie erklärt, dass vor Änderungen der Registeranmeldungen, Gesellschafterliste oder Bankberechtigungen eine rechtliche Prüfung erfolgen solle. Sie hält dennoch an der hier wiedergegebenen Bekanntgabe der einzelnen Ergebnisse fest. Romy und Kunibert stimmen keiner Gesamtbereinigung der Rechtslage zu.

## 7 Protokollvermerk

Thekla Spätzle hat diese Fassung am 28. September 2026 zur Übersendung freigegeben. Der Name steht als Wiedergabe ihres Freigabevermerks unter der Arbeitsabschrift; es wird keine Unterschriftsgrafik nachgebildet. Romys und Kuniberts in der Sitzung erklärte Einwände sind im Text aufgenommen. Eine Zustimmung der beiden zum gesamten Protokoll wird nicht behauptet.

Thekla Spätzle'''),
D('28_Theklas_Mitschrift.docx','Persönliche Mitschrift von Thekla Spätzle','25.09.2026',THEKLA,'Eigene Ablage','''Ich habe die Leitung übernommen, weil Romy und Kunibert sich schon vor Beginn gegenseitig unterbrochen haben. Bei der Kapitalfrage sagte Kunibert, wer nicht mitfinanzieren könne, habe dazu nichts zu entscheiden. Ich habe Romys Nein deshalb nicht mitgezählt. Romy hat sofort protestiert. Ich bin keine Juristin und weiß nicht, ob meine Berechnung richtig war.

Bei Kuniberts Abberufung habe ich mich enthalten. Ich wollte zunächst die Dateien und die Kundenanfrage klären. Bei seiner Einziehung habe ich dann ja gestimmt, weil ich einen Ausweg aus dem Streit wollte. Mir war nicht klar, wie sich diese Feststellung auf die folgenden Stimmen auswirken könnte. Ich habe daher überall weiter die ursprünglichen Beträge notiert und gesagt, dass die Umsetzung geprüft werden muss.

Bei Romys Abberufung habe ich nein gestimmt, weil die kaufmännische Arbeit sonst liegen bleibt. Bei der Einziehung ihres Anteils habe ich trotzdem ja gestimmt, weil ich dachte, ein späterer Anteilsverkauf an Hanna könne dann einfacher werden. Romy sagte, das sei keine vernünftige Grundlage. Sie hat bei beiden Punkten nein gestimmt und widersprochen.

Wir haben keine Abfindung gerechnet. Kunibert sagte, die GmbH werde das schon über Raten schaffen. Gundula hatte nur die Augustübersicht und keine bestätigte Planung vorliegen. Ich habe keine Zusage von Hanna erhalten, Abfindungen zu finanzieren. Mir wäre am liebsten, wir würden die Dinge rechtlich sortieren und dann miteinander verhandeln, bevor im Betrieb Fakten geschaffen werden.'''),
E('29_Protokollversand_28_September.eml','Protokoll vom 25 September zur Kenntnisnahme','2026-09-28T09:12:00+02:00','Thekla Spätzle <thekla@zink-zunder.example>','Romy Yilmaz <romy@zink-zunder.example>','''Guten Morgen Romy,

anbei die von mir freigegebene Fassung des Protokolls. Kunibert bekommt dieselbe Datei zeitgleich. Ich habe die Abstimmungen getrennt mit den jeweils tatsächlich abgegebenen Stimmen und deinen Widersprüchen aufgenommen. Die unterschiedlichen Feststellungen bleiben so stehen, wie ich sie bekannt gegeben habe; damit behaupte ich nicht, dass die Gesellschaft nun abschließend neu geordnet ist.

Bitte bestätige nur den Erhalt. Wir sollten vor dem Notartermin rechtlichen Rat einholen. Nach meinem Kenntnisstand wurden bisher keine neue Gesellschafterliste eingereicht, keine Geschäftsführeränderung angemeldet und keine Bankrechte geändert. Ich habe niemandem eine Vollmacht erteilt, das für alle Beteiligten zu erledigen.

Viele Grüße
Thekla'''),
E('30_Romy_Zugang_und_Widerspruch.eml','Erhalten aber keine Zustimmung zu den Ergebnissen','2026-09-28T09:37:00+02:00','Romy Yilmaz <romy@zink-zunder.example>','Thekla Spätzle <thekla@zink-zunder.example>','''Hallo Thekla,

ich bestätige den Zugang deiner Mail mit dem Protokoll heute um 09.12 Uhr. Ich habe den Anhang geöffnet. Diese Bestätigung ist keine Zustimmung zu den gegen mich gerichteten Ergebnissen oder zum Ausschluss meiner Stimme bei der Kapitalmaßnahme. Meine bereits in der Sitzung erklärten Einwände bleiben vollständig bestehen.

Bitte veranlasse keine Änderung meiner Zugänge, meiner Geschäftsführerstellung oder der Gesellschafterliste auf dieser Grundlage. Ich werde den Vorgang persönlich prüfen lassen. Ich verlange auch die Beibehaltung der vollständigen Mitschriften und der zugrunde liegenden Dateien, damit die tatsächlich abgegebenen Stimmen nachvollziehbar bleiben.

Ich will eine sachliche Lösung für den Betrieb. Aus diesem Korrekturverlangen soll aber niemand einen Verzicht auf gerichtliche Schritte oder Fristen ableiten. Ich melde mich mit einer geordneten Stellungnahme.

Romy'''),
D('31_Beirat_Stand_30_September.docx','Stand der Unterlagen beim Beirat','30.09.2026','Mechthild Mohn und Samir Senf\nFakultativer Beirat\nbeirat@zink-zunder.example',FIRMA,'''## 1 Erhaltene Unterlagen

Uns liegen inzwischen die beiden Darlehensabschriften, die Augustübersicht und die Mitteilung über die Zahlung von 30.000 EUR vor. Die Prüfung früherer Zustimmungsnachrichten ist noch nicht abgeschlossen. Herr Senf hat eine Gesprächseinladung aus Januar 2025 gefunden; Frau Mohn eine kurze Nachricht zum Sommerbedarf 2026. Diese Unterlagen belegen für sich keine ausdrückliche gemeinsame Freigabe der konkreten Vertragsfassungen.

## 2 Noch benötigte Angaben

Bitte stellen Sie die damaligen Vertragsfassungen, Anträge, Antworten und Zahlungsfreigaben vollständig zusammen. Wir benötigen außerdem die Fälligkeiten der aktuellen offenen Posten, mögliche Stundungen und konkrete Finanzierungszusagen. Der Bankbestand allein beantwortet die anstehenden Fragen nicht. Die Augustübersicht ist nicht geprüft und enthält noch offene Bewertungsfragen.

## 3 Rollen

Wir entscheiden nicht über die Wirksamkeit der streitigen Gesellschafterbeschlüsse. Wir können weder die Vertretungsregel im Außenverhältnis ändern noch einen persönlichen Auftrag Romys in einen Auftrag der GmbH umwandeln. Diese Stellungnahme enthält keine nachträgliche Genehmigung der Darlehen oder Rückzahlung.

## 4 Vorschlag

Wir regen an, die Dokumente unverändert zu sichern und bis zur rechtlichen Klärung keine auf den streitigen Einziehungsfeststellungen beruhende Neuordnung als einvernehmlich zu behandeln. Die laufenden gesetzlichen Pflichten der zuständigen Personen bleiben zu beachten. Eine abschließende Freigabe weiterer Zahlungen geben wir mit diesem Schreiben nicht.'''),
D('32_Romys_Mandantennotiz.docx','Persönliche Notiz für die Beratung','01.10.2026',ROMY,KANZLEI,'''## 1 Was ich erreichen möchte

Ich möchte meinen Anteil und meine Rechte sichern, ohne die Werkstatt zu zerstören. Ich bin zu einem fairen Verkauf bereit, wenn Preis, mein Darlehen und Garantien geregelt sind. Ich möchte weder automatisch Kuniberts Anteil übernehmen noch meine Zustimmung durch einen Streitvorwurf ersetzt sehen.

## 2 Eigene Handlungen

Ich habe Kuniberts Darlehen allein für die GmbH unterschrieben. Ich ging damals davon aus, dass die andere Unterschrift später ergänzt wird. Dafür habe ich keinen unterschriebenen Nachtrag. Bei der Rückzahlung habe ich mich auf seine Darstellung verlassen, dass das Geld nur kurzfristig gebraucht worden sei. Gundula hat die Bankzahlung technisch bestätigt. Ich weiß nicht, ob das rechtlich etwas an der Darlehensfrage ändert.

## 3 Konkurrenz und Unterlagen

Kunibert erzählte mir am 8. September nach dem Finanzierungsgespräch erstmals von Fensterfuchs und sagte, er habe schon mit Marta Alt über ein eigenes Angebot gesprochen. So habe ich das Gespräch verstanden; Kunibert bezeichnet es inzwischen als bloße Vorüberlegung. Einen schriftlichen Nachweis dieser frühen Ansprache hatte ich bei meinem Ergänzungsantrag noch nicht. Das Projektprofil und die Kundenmail kamen erst später hinzu. Der Logauszug zeigt Kopien, aber ich kann nicht aus eigener Kenntnis sagen, wo die Dateien danach verwendet wurden. Beim Rahmenmodell haben mehrere Personen mitgearbeitet. Den Vertrag mit dem früheren Zeichner suche ich noch. Ich möchte keine Behauptung unterschreiben, die ich nicht belegen kann.

## 4 Stand nach der Versammlung

Bis heute habe ich unverändert Zugriff auf die betriebliche Ablage. Eine Registeränderung wurde mir nicht gezeigt. Das Protokoll ging mir am 28. September zu. Den Notartermin am 9. Oktober habe ich nicht abgesagt, aber auch keine Erklärung genehmigt. Bitte prüfen Sie, welche Schritte vorher notwendig sind und gegen wen ich jeweils vorgehen muss. Meine E-Mail-Adressen und Postanschrift stehen in den Unterlagen.'''),
D('33_Genehmigung_Entwurf_ungezeichnet.docx','Ungezeichneter Entwurf zur Behandlung des Darlehens Knopf','29.09.2026','Kunibert Knopf',FIRMA,'''## 1 Entwurf

Die Zink & Zunder Metallbau GmbH erklärt, dass sie den am 1. Juni 2026 mit Kunibert Knopf dokumentierten Darlehensvertrag und die am 15. September 2026 erfolgte Teilrückzahlung von 30.000 EUR genehmigt. Kunibert Knopf nimmt diese Erklärung als Darlehensgeber entgegen. Weitere Ansprüche sollen mit dieser Erklärung nicht erlassen werden.

## 2 Vorgesehene Zeichnung

Für die Gesellschaft sind im Text Kunibert Knopf und Romy Yilmaz als gemeinsame Unterzeichner vorgesehen. Kunibert Knopf soll zusätzlich auf der Darlehensgeberseite unterzeichnen. Gundula Pfennig ist in diesem Entwurf nicht als Unterzeichnerin genannt. Eine gesonderte Befreiung von § 181 BGB oder ein auf diese Erklärung bezogener Gesellschafterbeschluss ist nicht beigefügt.

## 3 Dokumentenstand

Dieses Blatt ist ein Vorschlag Kuniberts aus der E-Mail-Abstimmung. Es wurde von niemandem unterzeichnet. Romy hat keine Zustimmung erteilt. Die Protokollstreitigkeiten und der tatsächliche Vertretungsstand wurden bei Erstellung nicht abschließend geprüft. Der Entwurf wird nur zur Beratung vorgelegt und enthält keine bereits abgegebene Genehmigungserklärung.'''),
D('34_Bueronotiz_Vollzugsstand.docx','Büronotiz zu Zugängen und nächsten Terminen','01.10.2026','Gundula Pfennig\ngundula@zink-zunder.example','Gesellschaftsablage','''## 1 Zugänge und Unterlagen

Die bisherigen betrieblichen Kennungen der beiden Geschäftsführer sind unverändert aktiv. Ich habe keine private oder betriebliche E-Mail gelöscht und die Versammlungsunterlagen zusammengehalten. Der CAD-Logauszug ist gesichert. Private Geräte werden durch das Büro nicht ohne geklärten Auftrag untersucht.

## 2 Register und Bank

Mir ist keine auf die Versammlung vom 25. September gestützte Registeranmeldung oder neue Gesellschafterliste bekannt. Ich habe keine solche Erklärung unterschrieben oder versandt. Die Bank hat von uns noch keinen Änderungsauftrag für die Vertretungs- oder Zugriffsrechte erhalten. Ob außerhalb unseres Büros jemand Unterlagen vorbereitet hat, kann ich nicht abschließend ausschließen.

## 3 Termine

Bei dem angefragten Notar ist der 9. Oktober um 11 Uhr vorgemerkt. Eine beurkundungsreife Fassung ist dem Büro nicht übermittelt worden. Hanna Blech hat für den 6. Oktober ein unverbindliches Gespräch angeboten. Die Steuerberatung wartet auf die Darlehensunterlagen. Keiner dieser Termine ersetzt aus Sicht des Büros die gesonderte Bearbeitung gesetzlicher oder vereinbarter Fristen.

## 4 Anweisungen

Romy und Kunibert erteilen teilweise gegensätzliche interne Weisungen. Ich habe beide um eine schriftliche Klärung gebeten, wer welche Maßnahmen beauftragt. Diese Notiz trifft keine rechtliche Entscheidung über ihre Organstellung. Notwendige laufende Fristsachen und Zahlungen werden nicht allein aufgrund einer privaten Einschätzung zurückgestellt, sondern den verantwortlichen Personen zur konkreten Entscheidung vorgelegt.'''),
E('35_Rueckfrage_Abfindung.eml','Was bedeuten die Einziehungen für das Geld','2026-09-30T16:25:00+02:00','Thekla Spätzle <thekla@zink-zunder.example>','Mechthild Mohn <mechthild@beirat-mohn.example>','''Guten Tag Frau Mohn,

ich habe nach der Sitzung versucht zu verstehen, wie die Abfindung überhaupt bezahlt werden könnte. Im Protokoll steht dazu kein Betrag. Kunibert meinte, drei Raten würden reichen. Romy bestreitet schon den Grund. Ich habe keine Bewertung und auch keine Finanzierungszusage gesehen.

Hannas Zahl von 150.000 EUR war nur ein unverbindlicher Gesprächseinstieg für alle Anteile und bezog die Darlehen nicht ein. Ich möchte diese Zahl nicht stillschweigend als feststehenden Abfindungswert einsetzen. Bitte sagen Sie mir, welche Unterlagen für eine belastbare Bewertung gebraucht werden. Mir ist bewusst, dass Sie als Beirat die streitigen Beschlüsse nicht verbindlich beurteilen können.

Freundliche Grüße
Thekla Spätzle'''),
E('36_Samir_Hinweis_Ablage.eml','Bitte die Ausgangsunterlagen getrennt lassen','2026-10-01T10:10:00+02:00','Samir Senf <samir@senf-beratung.example>','Gundula Pfennig <gundula@zink-zunder.example>','''Guten Tag Frau Pfennig,

bitte lassen Sie die ursprüngliche Satzung, das Protokoll und die persönlichen Notizen als getrennte Dateien bestehen. Ein nachträglich geglättetes Gesamtprotokoll würde die tatsächlich unterschiedlichen Aussagen verdecken. Die Tabellen dürfen die abgegebenen Stimmen zeigen, sollen aber keine ungeklärte Wirksamkeit der Einziehungen vorwegnehmen.

Für die Finanzunterlagen benötigen wir unterschiedliche Stichtage: die interne Augustbilanz, den tatsächlichen Septemberbanklauf und die Fälligkeiten zum 30. September. Die Rückzahlung eines Darlehens ist nicht einfach als Aufwand zu behandeln. Bitte weisen Sie offene Unterlagen und eventuelle Stundungen ausdrücklich aus, anstatt sie mit Null zu füllen.

Die rechtliche und steuerliche Beratung muss außerdem klären, wer für welche Erklärung zuständig ist. Ich kann keine persönliche Vertretungsmacht für Romy oder Kunibert erteilen.

Mit freundlichen Grüßen
Samir Senf'''),
]
CASE=dict(slug='gesellschafterstreit-zink-und-zunder',title='Zink und Zunder Gesellschafter im Streit',date='02.10.2026',client='Romy Yilmaz persönlich als Gesellschafterin',plugin='gesellschafterstreit',summary='Eine Berliner Metallbau-GmbH mit drei Gesellschaftern streitet über Kapitalbedarf, die Leitung der Gesellschaft, Darlehen, einen möglichen Verkauf und ein Nebenprojekt. Die Feststellungen der Versammlung stehen neben widersprechenden persönlichen Erklärungen und noch offenen Unterlagen.',assignment='Bearbeiten Sie Romy Yilmaz’ persönlichen Auftrag anhand der vorhandenen Dokumente. Ordnen Sie Rolle, Fristen, Beteiligungen, jede einzelne Abstimmung und die noch offenen Belege. Entwickeln Sie die notwendigen Schutzmaßnahmen und vollständig ausformulierten Dokumente, ohne streitige Rechtsfolgen als bereits gesicherte Tatsachen zu behandeln. Halten Sie persönliche und gesellschaftliche Ansprüche sowie Aufträge getrennt.',documents=DOCS,attachments={'14_Hanna_Angebotsversand.eml':['13_Unverbindliches_Angebot_Hanna.docx'],'18_Kundenanfrage_Altbogen.eml':['17_Fensterfuchs_Projektprofil.docx'],'23_Einladung_Zugang.eml':['22_Einladung_09_September.docx'],'26_Nachtrag_Zugang.eml':['25_Tagesordnung_Nachtrag.docx'],'29_Protokollversand_28_September.eml':['27_Protokoll_25_September.docx']})
CASES=[CASE]
