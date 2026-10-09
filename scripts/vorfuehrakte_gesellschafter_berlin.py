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
Kläger,
Prozessbevollmächtigte: Rechtsanwältin Walburga Fürst, Kanzlei Fürst, Berliner Straße 91, 13189 Berlin,
gegen die Spreebogen Lichtwerk GmbH, Mühlenstraße 64, 13187 Berlin, eingetragen beim Amtsgericht Charlottenburg unter HRB 241806 B, vertreten durch die einzelvertretungsberechtigte Geschäftsführerin Kunigunde Rabenstein,
Beklagte,
wegen Anfechtung eines Abberufungsbeschlusses,
vorläufiger Streitwert: 25000 EUR,
erheben wir namens und in Vollmacht des Klägers Klage.

## 1. Anträge

1.1. Der in der Gesellschafterversammlung der Spreebogen Lichtwerk GmbH vom 9. September 2026 unter dem zweiten Tagesordnungspunkt, bezeichnet in Ziffer 1.2 der Einladung vom 26. August 2026, als angenommen festgestellte Beschluss mit dem Wortlaut „Herr Gottfried Seidel wird aus wichtigem Grund mit sofortiger Wirkung als Geschäftsführer der Spreebogen Lichtwerk GmbH abberufen“ wird für nichtig erklärt.

1.2. Hilfsweise, für den Fall, dass das Gericht eine durch Anfechtungsurteil zu beseitigende Beschlusswirkung verneint, wird festgestellt, dass durch die unter Ziffer 1.1 bezeichnete Beschlussfassung eine wirksame Abberufung des Klägers als Geschäftsführer der Beklagten nicht zustande gekommen ist.

1.3. Die Beklagte trägt die Kosten des Rechtsstreits.

Es wird die Anordnung des schriftlichen Vorverfahrens angeregt. Für den Fall, dass die Beklagte ihre Verteidigungsbereitschaft nicht rechtzeitig anzeigt, wird der Erlass eines Versäumnisurteils nach Paragraf 331 Absatz 3 ZPO beantragt, soweit dessen Voraussetzungen vorliegen. Der Kläger begehrt ausschließlich die Klärung seiner Organstellung aufgrund des bezeichneten Beschlusses. Vergütung, Beendigung seines Anstellungsvertrags, Zahlungsansprüche aus dem Einkauf und Veränderungen seiner Beteiligung sind nicht Gegenstand dieser Klage.

## 2. Gesellschaftsverhältnisse und Maßstab der Geschäftsführung

## 2.1. Beteiligungen und Organstellung

Die Beklagte plant, montiert und wartet Beleuchtungs- und Steuerungstechnik für Bühnen und Veranstaltungsräume. Der Kläger hat den Betrieb 2019 gemeinsam mit Frau Rabenstein aufgebaut. Das Stammkapital beträgt 25000 EUR. Frau Rabenstein hält den Geschäftsanteil Nr. 1 über 10000 EUR, der Kläger den Geschäftsanteil Nr. 2 über 8750 EUR und Frau Heller den Geschäftsanteil Nr. 3 über 6250 EUR. Das entspricht 40, 35 und 25 Prozent. Eine Veränderung dieser Beteiligungen ist nicht erfolgt.

Der Kläger und Frau Rabenstein wurden in Ziffer 3.2 des Gesellschaftsvertrags zu Geschäftsführern bestellt und jeweils zur Einzelvertretung ermächtigt. Eine Befreiung von Paragraf 181 BGB wurde ihnen nicht erteilt. Der Registerausdruck vom 21. September 2026 führt beide weiterhin als Geschäftsführer. Der Kläger stützt seine Klage allerdings nicht allein auf diesen Registerstand, sondern auf die Unwirksamkeit der gegen ihn beschlossenen Maßnahme.

Beweis: Gesellschaftsvertrag vom 18. Juni 2019, Anlage K1; Gesellschafterliste, Anlage K2; aktueller Registerausdruck vom 21. September 2026, Anlage K3.

## 2.2. Zustimmungsvorbehalte und Abberufungsschutz

Der Kläger verantwortete Technik, Materialeinkauf und Baustellenkoordination; Frau Rabenstein betreute Vertrieb und Personal. Ziffer 3.3 des Gesellschaftsvertrags verlangt vor Geschäften mit Gesellschaftern oder ihren beherrschten Unternehmen die Zustimmung der Gesellschafterversammlung. Hinzu kommt die von sämtlichen Gesellschaftern am 10. Januar 2025 beschlossene Geschäftsordnung. Danach sind Einzelbestellungen über 10000 EUR brutto vor Beauftragung dem jeweils anderen Geschäftsführer mit Leistungsumfang, Preis, Liefertermin und Vergleichsangebot vorzulegen. Die Zustimmung ist in Textform zu sichern. Auch die Zahlung setzt eine entsprechende Freigabe voraus.

Der Kläger stellt diese Regelungen nicht in Abrede. Die technische Einzelberechtigung im Bankportal ersetzte keine interne Zustimmung. Auch war ein drohender Kundenterminverlust nach der Geschäftsordnung keine allgemeine Ausnahme. Streit besteht darüber, ob die konkrete Handhabung und die anschließend unvollständige Dokumentation unter Berücksichtigung der gesamten Umstände eine sofortige Abberufung rechtfertigten.

Ziffer 5.3 des Gesellschaftsvertrags lässt die Abberufung ausschließlich bei einem wichtigen Grund zu. Organstellung und Anstellungsvertrag sind ausdrücklich getrennt. Eine Kündigung des Anstellungsvertrags wurde am 9. September nicht beschlossen. Die Gesellschaft hat sich damit bewusst gegen die jederzeitige freie Abberufbarkeit entschieden.

Beweis: Anlage K1, Ziffern 3.2, 3.3, 5.1 und 5.3; Geschäftsordnung vom 10. Januar 2025, bei der Beklagten in der Datei 09_Geschaeftsordnung.docx und als unterschriebene Ausfertigung im Ordner „Gesellschaft / 2025“ vorhanden. Deren Vorlage wird nach Paragraf 142 Absatz 1 ZPO angeregt.

## 3. Der Einkauf für das Kulturhaus Lindenhof

## 3.1. Ausfall des Lieferanten und Nachrichten vom 19. August

Im August 2026 musste die Beklagte die Bühnensteuerung des Kulturhauses Lindenhof für dessen Wiedereröffnung fertigstellen. Der ursprünglich vorgesehene Lieferant konnte den Termin nicht einhalten. Der Kläger schlug deshalb vor, über seine Einzelfirma Seidel Bühnenservice e.K. sechs gebrauchte Steuergeräte zu beschaffen beziehungsweise aufzuarbeiten und Einbauhilfe zu leisten. Er teilte Frau Rabenstein am 19. August um 07:46 Uhr mit, dass die erste Kalkulation 14900 EUR brutto betrage und möglicherweise ein Expresszuschlag hinzukomme. Die Einschaltung seines eigenen Unternehmens wurde damit vor Durchführung offengelegt.

Frau Rabenstein antwortete um 08:04 Uhr: „Dann mach das, aber ich brauche die endgültige Zahl. Nichts ohne den Preisabgleich. Schick mir das andere Angebot und frag Ottilie wegen der Gesellschafterfreigabe.“ Der Kläger antwortete um 08:07 Uhr, er sei schon unterwegs und liefere nach. Diese vollständige Nachricht ist zugrunde zu legen. Der Kläger beruft sich nicht auf eine verkürzte, vorbehaltlose schriftliche Genehmigung des endgültigen Preises. Er verstand die Antwort jedoch als Einverständnis mit der Ersatzbeschaffung als solcher und nahm irrig an, die erforderliche Dokumentation und Gegenzeichnung nachreichen zu können.

Beweis: Nachrichtenverlauf vom 19. bis 21. August 2026, Anlage K7; ergänzend persönliche Anhörung des Klägers. Eine weitere, endgültige telefonische Preisfreigabe wird mit dieser Klage nicht behauptet.

## 3.2. Rechnung und Zahlung

Die Rechnung SBS-2026-084 vom 20. August 2026 weist sechs überholte Steuergeräte zu jeweils 1950 EUR netto, zusammen 11700 EUR, Kabelsatz und Sonderstecker für 1900 EUR, Transport und Einbauunterstützung für 1000 EUR sowie Expressbeschaffung und Zusatzarbeit für 862,18 EUR aus. Die Nettosumme beträgt 15462,18 EUR, die Umsatzsteuer 2937,82 EUR und der Endbetrag 18400 EUR. Der Kläger übersandte die Rechnung an die Buchhaltung und teilte Frau Rabenstein am 20. August um 18:44 Uhr den Endbetrag mit. Dabei erklärte er, zwei Geräte habe er andernorts beschaffen müssen.

Am 21. August veranlasste der Kläger die Überweisung an seine Einzelfirma. Das Beanstandungsschreiben nennt hierfür 07:43 Uhr. Frau Rabenstein hatte im Nachrichtenkanal um 07:31 Uhr verlangt, vor der gemeinsamen Durchsicht noch nicht zu zahlen. Der Kläger hat diese Nachricht nach seiner Erinnerung erst nach Ausführung der Überweisung gelesen. Er bestreitet deshalb, eine bereits gelesene konkrete Zahlungsuntersagung bewusst übergangen zu haben. Die zeitliche Reihenfolge von Nachricht und Bankauftrag beweist für sich noch nicht den Zeitpunkt seiner Kenntnisnahme.

Der Kläger hatte keinen förmlichen Gesellschafterbeschluss eingeholt. Er erteilte den Auftrag an seine Einzelfirma selbst. Die ursprüngliche Zahl von 14900 EUR war vorläufig; gegenüber dem Rechnungsbetrag besteht eine Differenz von 3500 EUR brutto. Der Kläger führte diese auf zusätzliche Arbeit und kurzfristigen Zukauf zurück. Er benennt vier zusätzliche Arbeitsstunden, verfügt aber derzeit über keine geschlossene, zeitgleich erstellte Überleitung des gesamten Mehrbetrags. Die Klage behauptet deshalb weder einen durchgängigen Rechnungsnachweis noch einen von allen Gesellschaftern genehmigten Endpreis.

Beweis: Rechnung, Anlage K6; vollständiger Nachrichtenverlauf, Anlage K7; Beanstandung, Anlage K8; Antwort des Klägers, Anlage K9. Zur ausgeführten Zahlung wird ergänzend die Vorlage der bezeichneten Buchung SBS-2026-084 vom 21. August 2026 im Bankprotokoll der Beklagten nach Paragraf 142 Absatz 1 ZPO angeregt.

## 3.3. Lieferumfang und verbleibende Nachweise

Der Kläger trägt vor, dass die abgerechneten Geräte und Materialien dem Lindenhof-Auftrag zugutekamen. Vier Geräte lieferte er am 24. August zur Werkstatt der Beklagten. Zwei weitere Geräte brachte er nach seiner Darstellung bereits am Samstag, dem 22. August, unmittelbar zur Bühne. Hierfür erhielt er keinen unterschriebenen Lieferschein. Seine Fotos zeigen Verpackungen, keine lesbaren Seriennummern. Der Werkstattbeleg über vier Geräte wird deshalb nicht als Beleg für die zusätzliche Direktlieferung ausgegeben.

Beweis für die Annahme der vier Geräte in der Werkstatt: Zeugnis des Werkstattleiters Tassilo Brandt, zu laden über die Beklagte, Mühlenstraße 64, 13187 Berlin; Wareneingang WE-0824 vom 24. August 2026, dessen Vorlage aus dem Besitz der Beklagten angeregt wird. Hinsichtlich der unmittelbaren Lieferung am 22. August wird die Vernehmung des Klägers als Partei mit Zustimmung der Beklagten nach Paragraf 447 ZPO angeboten; andernfalls wird seine persönliche Anhörung angeregt. Herr Brandt wird nicht als Augenzeuge einer Lieferung auf der Baustelle benannt, bei der er nicht anwesend war.

Der Auftrag wurde fertiggestellt und vom Kunden bezahlt. Das begründet nach Auffassung des Klägers ein erhebliches Indiz für einen wirtschaftlich nutzbaren Leistungseinsatz. Es ersetzt aber weder die Zuordnung jedes abgerechneten Geräts noch eine Prüfung des Preises. Der Kläger beantragt, die Beklagte zur Erklärung über die Fertigstellung und den Zahlungseingang aufzufordern. Die Behauptung einer vollständigen Lieferung bleibt insoweit beweisbedürftig, als sie über den Werkstattbeleg hinausgeht.

## 4. Beanstandung und Gesellschafterversammlung

## 4.1. Aufklärungsbemühungen vor dem Beschluss

Am 24. August erläuterte der Kläger Frau Rabenstein im Büro die Zahlung und den aus seiner Sicht erforderlichen kurzfristigen Einkauf. Für den Gesprächsinhalt aus eigener Wahrnehmung wird seine Parteivernehmung nach Paragraf 447 ZPO mit Zustimmung der Beklagten, hilfsweise seine persönliche Anhörung, angeboten. Der Kläger verfügt über keine vollständige Gesprächsaufzeichnung.

Am 27. August übergab Frau Rabenstein ihm die schriftliche Beanstandung. Verlangt wurden bis zum 31. August der Bestellvorgang, Fremdrechnungen und Angaben zum Verbleib der sechs Geräte. Sie verwies auf die fehlende Gesellschafterzustimmung und den Preisvergleich. Die angebliche Äußerung, die Buchhaltung solle sich nicht in die Technik einmischen, wird bestritten, soweit daraus eine dauerhafte Verweigerung jeder Rechnungskontrolle abgeleitet wird.

Der Kläger antwortete am 31. August schriftlich. Er räumte ein, keinen förmlichen Beschluss eingeholt zu haben, erläuterte die behauptete Direktlieferung und bot eine gemeinsame Kalkulationsdurchsicht sowie gegebenenfalls eine Gutschrift für eine nicht belegbare Position an. Eine Rückzahlung des Gesamtbetrags oder ein Schuldeingeständnis lehnte er ab. Die in Aussicht gestellte vollständige Belegaufbereitung war bis zur Versammlung nicht abgeschlossen. Sein Angebot zur sachlichen Prüfung blieb bestehen; eine gemeinsame vollständige Belegdurchsicht fand zuvor nicht statt.

Beweis: Beanstandung vom 27. August, Anlage K8; Antwort vom 31. August, Anlage K9; zur noch offenen Dokumentation und den Erklärungen in der Versammlung Anlage K5.

## 4.2. Einladung, Aussprache und Abstimmung

Die Einladung vom 26. August ging dem Kläger am 28. August per Einschreiben zu. Sie benannte die Eigenbeauftragung, die Zahlung von 18400 EUR ohne vorherigen Gesellschafterbeschluss und die Missachtung der Geschäftsordnung. Der Kläger macht keinen allein aus diesen Daten hergeleiteten Einladungsfristverstoß geltend. Sämtliche Gesellschafter erschienen am 9. September; das gesamte Stammkapital war vertreten. Frau Heller wurde mit allen 25000 Stimmen zur Versammlungsleiterin gewählt.

Frau Rabenstein hielt dem Kläger die fehlenden Freigaben und Nachweise vor. Er verwies auf den Zeitdruck, seine Auslegung der Nachricht und die noch zu vervollständigenden Unterlagen. Frau Heller erklärte, sie könne über die vier im Werkstattbeleg erfassten Geräte hinaus den Lieferumfang und die Montagezeiten nicht beurteilen. Der Kläger widersprach der Forderung nach einer Rückzahlungserklärung. Über eine solche Erklärung wurde nicht abgestimmt.

Für die Abberufung stimmte Frau Rabenstein mit 10000 Stimmen. Der Kläger stimmte mit 8750 Stimmen dagegen. Frau Heller enthielt sich mit 6250 Stimmen. Sie zählte die Nein-Stimmen des Klägers wegen seiner Betroffenheit nicht und stellte die Annahme des Abberufungsantrags fest. Der Kläger widersprach ausdrücklich dem Stimmrechtsausschluss, der Feststellung und der Abberufung. Die Niederschrift ging ihm am 11. September zu. Über eine Kündigung des Anstellungsvertrags oder Schadensersatz wurde nicht beschlossen.

Beweis: Einladung, Anlage K4; Niederschrift, Anlage K5; Zeugnis der Ottilie Heller, zu laden über die Beklagte. Ihre Vernehmung wird für Wahl, Abstimmung, Ergebnisfeststellung und Widerspruch sowie die von ihr selbst abgegebenen Erklärungen angeboten, nicht für ihr unbekannte Lieferhandlungen. Die Urkundenvorlage bedeutet keine Anerkennung sämtlicher zusammengefasster Wertungen im Protokoll.

## 5. Zulässigkeit und Umfang des Rechtsschutzes

## 5.1. Zuständigkeit, Parteien und Klagefrist

Das Landgericht Berlin II ist bei dem vorläufig mit 25000 EUR bewerteten Interesse nach Paragraf 71 Absatz 1 GVG sachlich und wegen des Sitzes der Beklagten nach Paragraf 17 Absatz 1 ZPO örtlich zuständig. Der Streitwert berücksichtigt die Bedeutung der bestrittenen Organstellung; er ist nicht mit dem Rechnungsbetrag gleichzusetzen. Der Kläger ist als unverändert beteiligter Gesellschafter zur Anfechtung des ihn betreffenden Beschlusses befugt. Beklagte ist nach Ziffer 8.1 der Satzung die Gesellschaft. Im Rubrum ist ihre weitere einzelvertretungsberechtigte Geschäftsführerin bezeichnet. Die Zuständigkeit der Gesellschafter für die Prozessvertretung nach Paragraf 46 Nummer 8 GmbHG bleibt hiervon unberührt.

Ziffer 8.1 der Satzung bestimmt eine Monatsfrist. Weil der Kläger an der Versammlung teilnahm und das Ergebnis ausdrücklich festgestellt wurde, ist für ihn bereits der 9. September maßgeblich; der Zugang der Niederschrift am 11. September verschiebt den Beginn nicht. Die Klage wird am 22. September und damit vor Ablauf am 9. Oktober 2026 eingereicht. Es wird um unverzügliche Zustellung gebeten. Der Gerichtskostenvorschuss wird nach Eingang der Kostenanforderung unverzüglich gezahlt; für eine demnächst erfolgende Zustellung wird auf Paragraf 167 ZPO verwiesen.

## 5.2. Beschlussfeststellung und Hilfsantrag

Die Klage richtet sich vorrangig auf die Beseitigung des ausdrücklich festgestellten Beschlusses. Ziffer 4.3 der Satzung ermächtigt die gewählte Versammlungsleiterin zur Feststellung von Ergebnis und Annahme. Der Kläger bestreitet deshalb nicht allein wegen der fehlenden anwaltlichen Begleitung ihre Feststellungskompetenz. Die gerichtliche Kontrolle der materiellen Voraussetzungen wird durch diese Kompetenz jedoch nicht ausgeschlossen.

Der Hilfsantrag erfasst ausschließlich den Fall, dass das Gericht eine durch Anfechtung zu beseitigende Wirkung der bezeichneten Feststellung verneint. Das Feststellungsinteresse nach Paragraf 256 Absatz 1 ZPO ergibt sich daraus, dass die Beklagte die Organstellung als beendet behandelt und die Registeranmeldung angekündigt hat. Die konkrete Rechtsunsicherheit besteht bereits jetzt. Beantragt wird weder eine neue Bestellung noch eine Feststellung über unbekannte künftige Beschlüsse. Ein gesonderter Zahlungs- oder Beschäftigungsantrag wird nicht erhoben.

## 6. Begründetheit

## 6.1. Maßgeblich ist ein tatsächlich bestehender wichtiger Grund

Der Beschluss verletzt Ziffer 5.3 der Satzung in Verbindung mit Paragraf 38 Absatz 2 GmbHG. Die Satzung bindet die Abberufung an einen wichtigen Grund. Die Gesellschaftermehrheit durfte diese Voraussetzung weder durch die Bezeichnung des Antrags noch durch die Nichtberücksichtigung der Klägerstimmen ersetzen.

Nach BGH, Urteil vom 04.04.2017 – Az. II ZR 77/16, amtlicher Volltext, ECLI:DE:BGH:2017:040417UIIZR77.16.0, Randnummern 9 und 14, ist im Beschlussprozess entscheidend, ob bei Beschlussfassung objektiv ein wichtiger Grund bestand. Wer sich darauf beruft, trägt die Darlegungs- und Beweislast. Hier betrifft dies die Beklagte. Randnummer 17 verlangt für die Unzumutbarkeit weiterer Geschäftsführung eine Abwägung sämtlicher Umstände. Die Entscheidung rechtfertigt damit weder eine automatische Abberufung bei jeder internen Pflichtverletzung noch deren generelle Unwirksamkeit bei fehlendem Vermögensschaden.

## 6.2. Eigenbeauftragung und fehlende Freigaben

Die fehlende Gesellschafterzustimmung ist ein ernstzunehmender Vorwurf. Nach Paragraf 37 Absatz 1 GmbHG hatte der Kläger interne Beschränkungen zu beachten. Sein Aufgabenbereich Technik und die Einzelvertretung entbanden ihn davon nicht. Ebenso wenig ersetzte Frau Rabensteins Nachricht einen Gesellschafterbeschluss. Der Kläger stützt seine Verteidigung gegen die Abberufung deshalb auf die konkrete Schwere des Vorgangs und dessen beherrschbare Folgen, nicht auf eine Aufhebung der Satzungsregel durch Zeitdruck.

Auch Paragraf 181 BGB ist zu berücksichtigen: Der Kläger handelte nach eigener Darstellung auf beiden Seiten des Geschäfts und besaß keine allgemeine Befreiung. Eine wirksame besondere Gestattung oder spätere Genehmigung wird nicht als bereits bewiesen vorgetragen. Aus der möglichen Unwirksamkeit des Liefergeschäfts folgt jedoch nicht ohne weitere Würdigung die Unzumutbarkeit seiner weiteren Organstellung. Rechtsgeschäftliche Wirksamkeit, interne Pflichtverletzung und Abberufungsgrund sind jeweils gesondert zu beurteilen.

Gegen eine gezielte Schädigung sprechen die Offenlegung der eigenen Firma bereits vor der Beschaffung, die Mitteilung des Endbetrags vor Zahlung und das nachfolgende Angebot einer überprüfbaren Abrechnung. Ein bewusstes Zuwiderhandeln gegen eine gelesene Zahlungsuntersagung wird bestritten. Die Beklagte muss insbesondere zwischen dem sicheren Fehlen formeller Freigaben und dem weitergehenden Vorwurf absichtlicher Missachtung einer konkreten Nachricht unterscheiden.

## 6.3. Lieferstreit und Interessenabwägung

Aus dem Werkstattbeleg über vier Geräte folgt nicht zwingend, dass zwei weitere Geräte niemals auf die Baustelle gelangten. Umgekehrt beweist die Fertigstellung des Kundenauftrags nicht die vollständige Erfüllung der Rechnung der Einzelfirma. Die noch offene Gerätezuordnung und Kalkulation verlangen Aufklärung. Ein vorsätzliches Abrechnen nicht erbrachter Leistungen ist mit den vorgelegten Unterlagen nicht belegt. Der Kläger hält an seiner Darstellung fest und stellt sich der Beweisaufnahme.

Die Abwägung muss zugleich den Betrag von 18400 EUR, die Nähe zum eigenen wirtschaftlichen Interesse und die verspäteten Belege berücksichtigen. Auf Klägerseite stehen seine seit Gründung ausgeübte technische Leitung, seine Kenntnisse der Installationen, der tatsächlich fertiggestellte Auftrag und das Angebot, unbelegte Positionen zu korrigieren. Ein bezifferter Schaden ist bislang nicht dargelegt. Das allein entscheidet den Prozess nicht, mindert aber das Gewicht eines Vorwurfs, der die Zahlung ohne Bewertung der Gegenleistung als vollständigen Vermögensverlust behandelt.

Am 9. September waren nach Auffassung des Klägers weniger einschneidende Kontrollen ausreichend: Belegprüfung mit verbindlicher Nachfrist, Ausschluss eigenständiger Freigabe von Zahlungen an die Einzelfirma und gemeinsame Zahlungsfreigaben. Dies sind keine bereits beschlossenen Maßnahmen, sondern naheliegende Alternativen, deren Eignung bei der Abwägung zu prüfen war. Der Kläger hatte Aufklärung und gegebenenfalls Gutschrift angeboten. Seine Weigerung, den gesamten Rechnungsbetrag ohne Prüfung zurückzuzahlen, durfte nicht für sich als Verweigerung jeder Zusammenarbeit gewertet werden.

Der Kläger behauptet nicht, vor jeder Abberufung müsse zwingend eine Abmahnung erfolgen. Hier hätte aber erläutert werden müssen, weshalb kontrollierte Fortführung trotz des Aufklärungsangebots unzumutbar war. Konkret belegte frühere gleichartige Verstöße sind in Einladung und Niederschrift nicht aufgeführt. Ein pauschaler Hinweis auf verlorenes Vertrauen ersetzt diese Begründung nicht. Die Gesamtabwägung rechtfertigt deshalb nach Auffassung des Klägers die sofortige Organabberufung nicht.

## 6.4. Stimmverbot und rechnerische Mehrheit

Paragraf 47 Absatz 4 GmbHG und die Grundsätze zum Verbot, über die Missbilligung eigenen Verhaltens selbst zu entscheiden, sind zu beachten. BGH, Urteil vom 04.04.2017 – Az. II ZR 77/16, amtlicher Volltext, ECLI:DE:BGH:2017:040417UIIZR77.16.0, Randnummern 10 bis 15, unterscheidet zwischen der gewöhnlichen Abberufung und der Abberufung aus wichtigem Grund. Den Streit über die Voraussetzungen eines schon vom Versammlungsleiter anzuwendenden Stimmverbots entscheidet das Urteil nicht abschließend; die gerichtliche Sachprüfung bleibt erforderlich.

Der Kläger verkennt zudem nicht die Stimmenverhältnisse: Auch unter Einbeziehung seiner 8750 Nein-Stimmen stehen 10000 Ja-Stimmen gegenüber. Die 6250 Enthaltungsstimmen zählen nach Ziffer 4.2 der Satzung nicht als abgegeben. Der Antrag hätte mithin rechnerisch auch ohne seinen Ausschluss eine einfache Mehrheit erreicht. Die Klage wird nicht auf eine gegenteilige Berechnung gestützt. Ihr tragender Grund bleibt das Fehlen der besonderen materiellen Abberufungsvoraussetzung. Eine Stimmenmehrheit gestattet keine Abweichung von Ziffer 5.3 der Satzung.

## 7. Beweisaufnahme und Anlagen

Die vorgelegten Unterlagen belegen Erklärungen und Abläufe; sie nehmen die Würdigung streitiger Lieferungen oder innerer Vorstellungen nicht vorweg. Angeregt wird die Vorlage der konkret bezeichneten Geschäftsordnung, des Wareneingangs WE-0824 und der Zahlungsbuchung SBS-2026-084 durch die Beklagte. Soweit die Vollständigkeit von K7 bestritten wird, soll außerdem der betriebliche Kanal „Lindenhof Einkauf“ für den 19. bis 21. August 2026 vorgelegt werden. Begehrt wird keine allgemeine Durchsuchung der Geschäftsunterlagen. Der Kläger hat derzeit keinen eigenen Zugang zur Einkaufsablage und benötigt die bezeichneten Belege für den Abgleich.

Der Klage sind folgende neun Anlagen als gesonderte Dateien beigefügt:

7.1. Anlage K1 ist der Gesellschaftsvertrag vom 18. Juni 2019 in der Datei 05_Gesellschaftsvertrag_K1.docx.

7.2. Anlage K2 ist die Gesellschafterliste vom 18. Juni 2019 mit Ablageabgleich vom 21. September 2026 in der Datei 06a_Gesellschafterliste_K2.docx.

7.3. Anlage K3 ist der Registerausdruck vom 21. September 2026 in der Datei 06b_Registerabruf_K3.pdf.

7.4. Anlage K4 ist die Einladung vom 26. August 2026 mit Einlieferungs- und Zustellangaben in der Datei 07_Einladung_K4.docx. Die beigefügte Rechnung wird zugleich gesondert als K6 vorgelegt.

7.5. Anlage K5 ist die Niederschrift der Versammlung vom 9. September 2026, erstellt am 10. September und versandt am 11. September, in der Datei 08_Niederschrift_K5.docx.

7.6. Anlage K6 ist die Rechnung SBS-2026-084 vom 20. August 2026 über 18400 EUR in der Datei 10_Rechnung_SBS_K6.pdf.

7.7. Anlage K7 ist der Nachrichtenverlauf vom 19. bis 21. August 2026 in der Datei 11_Nachrichten_K7.txt.

7.8. Anlage K8 ist die Beanstandung vom 27. August 2026 in der Datei 12_Beanstandung_K8.docx.

7.9. Anlage K9 ist die Antwort des Klägers vom 31. August 2026 in der Datei 13_Antwort_Seidel_K9.docx.

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
Export durch Kunigunde Rabenstein am 21.09.2026 aus dem betrieblichen Kanal. Zeitzone Berlin. Teilnehmer: Kunigunde Rabenstein und Gottfried Seidel.

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
