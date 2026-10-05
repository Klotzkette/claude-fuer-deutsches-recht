"""Feuerwehreinsatz und beleggebundene Fortsetzungen vier bestehender Akten."""

FOLDER = 'kommunikation-und-deckung/'
LAWYER = 'Rechtsanwältin Leonie von Tann\nMohnanger 8, 97082 Lindenquell bei Würzburg'
CITY = 'Stadt Lindenquell – Rechtsstelle\nRathausplatz 1, 97082 Lindenquell bei Würzburg'
INSURER = 'Mainbogen Kommunalversicherung VVaG – Schadenabteilung\nKornblumenstraße 18, 97084 Würzburg'
COUNTY = 'Landkreis Würzburg – Sachgebiet Feuerwehrwesen\nZeppelinstraße 15, 97074 Würzburg'


def document(file, title, body, kind='document', sender='', recipient='', date='05.10.2026'):
    return dict(file=file, title=title, body=body.strip(), kind=kind,
                sender=sender, recipient=recipient, date=date)


def letter(file, title, body, sender, recipient, date='05.10.2026'):
    return document(file, title, f'{sender}\n\n{recipient}\n\n{body.strip()}',
                    'letter', sender, recipient, date)


def email(file, title, body, sender, recipient, date):
    return document(file, title, body, 'email', sender, recipient, date)


def k(label, file, description):
    return dict(label=label, source=FOLDER + file, description=description)


FIRE_EXHIBITS = [
    k('K1', '02_Einsatzbericht.docx', 'Einsatzbericht vom 15.09.2026 mit ergänztem Rückbauablauf.'),
    k('K2', '03_Zeugin_Schlauchende.eml', 'Zeitnahe Beobachtung der Nachbarin zur Wasserführung.'),
    k('K3', '04_Befund_und_Inventar.docx', 'Gemeinsamer Ortsbefund und positionsbezogenes Schadeninventar.'),
    k('K4', '05_Rechnungen_und_Zahlungen.docx', 'Rechnungsabschriften, Zahlungen, Vorsteuer und Restwerte.'),
    k('K5', '06_Landkreis_Auskunft.pdf', 'Auskunft zu Einsatzleitung und tatsächlicher Rolle des Landkreises.'),
    k('K6', '07_Anspruchsschreiben.pdf', 'Außergerichtliche Bezifferung vom 02.10.2026.'),
    k('K7', '08_Stadt_Zwischenantwort.pdf', 'Städtische Zwischenantwort vom 05.10.2026.'),
    k('K8', '09_Mandantenfreigabe.eml', 'Begrenzter Klagevorbereitungsauftrag, Eigentum und fehlende Drittleistung.'),
    k('K9', '13_Technik_Nachtrag.docx', 'Technische Abgrenzung des Wasserschadens von Brandfolgen.'),
]


FIRE_CLAIM = '''ENTWURF – nicht eingereicht
Stand: 05.10.2026

Rechtsanwältin Leonie von Tann
Mohnanger 8, 97082 Lindenquell bei Würzburg

An das Landgericht Würzburg
Ottostraße 5, 97070 Würzburg

Klage

des Wendelin Knopf, handelnd unter Buchbinderei Wendelin Knopf e.K., Kelterbogen 14, 97082 Lindenquell bei Würzburg,
– Kläger –

Prozessbevollmächtigte: Rechtsanwältin Leonie von Tann, Mohnanger 8, 97082 Lindenquell bei Würzburg,

gegen

die Stadt Lindenquell, vertreten durch den Ersten Bürgermeister Anselm Buchner, Rathausplatz 1, 97082 Lindenquell bei Würzburg,
– Beklagte –

wegen Schadensersatz nach einem Feuerwehreinsatz
Vorläufiger Streitwert: 47.820,00 EUR
Unser Zeichen: VT 26/118

## 1 Anträge

Namens und in Vollmacht des Klägers wird beantragt, die Beklagte zu verurteilen, an den Kläger 47.820,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem auf die Zustellung der Klage folgenden Tag zu zahlen. Ferner wird beantragt, der Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Gegenstand ist der abgeschlossene Sachschaden an Betriebsmitteln und Vorräten sowie die konkret bezahlte Ersatzmaschinenmiete. Weitere Betriebsunterbrechungsschäden, entgangener Gewinn, außergerichtliche Rechtsanwaltskosten und Gebäudeschäden werden nicht geltend gemacht. Ein Feststellungsantrag wird nicht gestellt. Der Kläger verlangt die nach Vorsteuerabzug verbleibenden Nettobeträge; die Beträge sind weder Bruttorechnungen noch pauschale Reserven eines Versicherers.

## 2 Parteien, Anspruch und Zuständigkeit

Der Kläger betreibt die Buchbinderei als Einzelkaufmann. Er ist Eigentümer der hier betroffenen Falzmaschine, der Druckbogen und der Lagerhilfen. Die Bezeichnung e.K. bezeichnet keinen vom Kläger verschiedenen Rechtsträger. Die Geschäftsräume sind gemietet; Ansprüche des Gebäudeeigentümers sind nicht Bestandteil dieser Klage. Eigentum, Geschäftsnutzung und Zahlung bestätigt der Kläger in Anlage K8; die Inventarnummern und Rechnungsadressaten ergeben sich aus Anlagen K3 und K4.

Die Beklagte unterhält die Freiwillige Feuerwehr Lindenquell. Ihr Kommandant leitete den Einsatz am 14.09.2026 und den anschließenden Rückbau. Der geltend gemachte Anspruch folgt aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 Satz 1 GG. Das Landgericht ist nach § 71 Abs. 2 Nr. 2 GVG für Amtshaftung unabhängig von der Wertgrenze zuständig; der Streitwert übersteigt zudem 10.000,00 EUR. Die örtliche Zuständigkeit folgt jedenfalls aus § 32 ZPO, weil die Beschädigung in Lindenquell im Gerichtsbezirk Würzburg eintrat.

## 3 Brandbekämpfung und gesonderter Wassereintritt

Am 14.09.2026 brannte gegen 09:08 Uhr ein abgestellter handgezogener Holztransportwagen in der vom Betrieb des Klägers baulich getrennten städtischen Garagenzeile Kelterbogen 16. Die Feuerwehr löschte den Brand. An den Räumen des Klägers brannte es nicht. Ihr Zugang befindet sich seitlich am Hof; ein Lichtschacht führt zum tieferliegenden Maschinenraum. Die zum Löschen verwendete Leitung verlief über den Hof an diesem Lichtschacht vorbei. Der Kläger verlangt keinen Ersatz unvermeidbarer Löschschäden während der Brandbekämpfung.

Um 09:31 Uhr meldete Kommandant Kaspar Kresse „Feuer aus“. Eine Kontrolle der Garagenzeile ergab um 09:42 Uhr keine fortdauernde Brandgefahr. Um 09:46 Uhr ordnete er den Rückbau an. Der für die Leitung zuständige Trupp legte das drucklose, offene Ende einer C-Leitung auf dem Rand des Lichtschachts ab. Die sonst vorhandene Gitterabdeckung war für die Schlauchführung teilweise beiseitegeschoben. Beim anschließenden Zusammenlegen glitt das Ende in den Schacht. Niemand hielt oder sicherte es. Die Klägerseite stützt diesen Ablauf auf den Einsatzbericht und die eigenen Wahrnehmungen des Schlauchführers, Anlage K1.

Maschinist Hanno Halm öffnete um 09:49 Uhr nach einem Zuruf die Wasserzufuhr zur Spülung. Er nahm irrtümlich an, das freie Ende liege auf dem Hof beim Ablauf. Eine Rückmeldung über seine tatsächliche Lage holte er nicht ein. Wasser floss durch den Lichtschacht und das dort angekippte Kellerfenster in den Maschinenraum. Die Nachbarin Jovana Wacholder bemerkte um 09:55 Uhr das Laufgeräusch und rief dem Trupp zu. Um 09:57 Uhr wurde die Zufuhr geschlossen. Die genannten Zeiten beruhen teils auf dem Funkprotokoll, teils auf zeitnahen persönlichen Notizen; eine sekundengenaue Messung wird nicht behauptet.

Beweis: Einsatzbericht, Anlage K1; Zeugnis des Kaspar Kresse und des Hanno Halm, beide zu laden über Feuerwehr Lindenquell, Gerätehaus, Amselspange 4, 97082 Lindenquell; Zeugnis der Jovana Wacholder, Kelterbogen 12, 97082 Lindenquell, Anlage K2. Frau Wacholder hat den früheren Löschvorgang nicht vollständig beobachtet. Sie kann aber das frei liegende Schlauchende, den Wassereintritt und ihre Warnung schildern. Ihre Aussage wird auf diese Wahrnehmungen begrenzt.

## 4 Amtspflichtverletzung und Verantwortlichkeit

Abwehrender Brandschutz gehört nach Art. 1 Abs. 1 BayFwG zu den Aufgaben der Gemeinde. Der Rückbau der dafür eingesetzten Leitungen stand noch unmittelbar mit diesem öffentlichen Einsatz in Zusammenhang. Es handelte sich weder um eine private Gefälligkeit des Feuerwehrvereins noch um einen vom Kläger bestellten Werkvertrag. Die Pflicht, beim Umgang mit der eigenen Wasserleitung vermeidbare Schäden am Eigentum des unmittelbar benachbarten Betriebs zu verhindern, bestand gerade gegenüber dem Kläger.

Vor erneuter Wasserfreigabe waren das freie Ende festzustellen und zu sichern. Dies erforderte weder eine aufwendige Begutachtung noch einen Eingriff in die laufende Rettung. Die Löschphase war beendet; für die behauptete kurze Kontrolle standen Schlauchtrupp und Maschinist zur Verfügung. Der Trupp durfte eine drucklose Leitung zum geordneten Rückbau ablegen, jedoch nicht ohne gesicherte Verständigung wieder beaufschlagen lassen. Der Maschinist durfte aus einem unbestimmten Zuruf nicht folgern, dass der Auslauf frei zum Hofablauf führe. Gerade die fehlende Rückmeldung verband die beiden Fehler zu der hier eingetretenen Eigentumsbeschädigung.

Die Einsatzlage ist aus damaliger Sicht zu beurteilen. Aus dem späteren Wasserschaden allein wird kein Verschulden abgeleitet. Ausschlaggebend sind die dokumentierte Entspannung der Lage, die bekannte offene Verbindung zum tieferliegenden Raum und die einfach mögliche Kontrolle vor Wiederöffnung. Art. 25 BayFwG unterstreicht für Eingriffsmaßnahmen die Begrenzung auf das Erforderliche; eine Befugnis, ohne Einsatznutzen unkontrolliert Wasser in Nachbarräume zu leiten, ergibt sich daraus nicht.

Der Haftungsmaßstab ist nicht auf grobe Fahrlässigkeit beschränkt. Der Bundesgerichtshof verneint für die amtliche Gefahrenabwehr durch die Feuerwehr eine entsprechende Anwendung des § 680 BGB; es bleibt beim allgemeinen Fahrlässigkeitsmaßstab (BGH, Urteil vom 14.06.2018 – III ZR 54/17, BGHZ 219, 77, Rn. 47, 53). Der dortige Fall betraf umweltschädlichen Löschschaum. Hier wird allein die Aussage zum Haftungsmaßstab herangezogen; ein gleicher technischer Sachverhalt oder eine automatische Haftung für jedes Löschmittel wird nicht behauptet.

Die Beklagte ist der richtige Rechtsträger. Das Landratsamt bestätigte, dass kein Kreisbrandrat die Einsatzleitung übernommen hatte. Weder eine Katastrophenfeststellung noch eine besondere Weisung des Landkreises lag vor. Ein vom Landkreis bezuschusstes Gerät verändert den Träger dieser konkreten Tätigkeit nicht. Art. 2 BayFwG über überörtliche Ausstattung und Art. 18 BayFwG über die Einsatzleitung sind voneinander zu unterscheiden. Beweis: Auskunft vom 25.09.2026, Anlage K5. Ein Behördenkontakt begründet keine gesamtschuldnerische Haftung des Landkreises.

## 5 Ursächlichkeit und Abgrenzung

Der Wassereintritt beschränkte sich auf die tieferliegende Fläche hinter dem Lichtschacht. Dort standen die Falzmaschine und fünf Wagen mit Papierbogen. Die gemeinsame Besichtigung vom 15.09.2026 dokumentiert eine Wasserlinie bis acht Zentimeter über dem Boden. In der Garagenzeile entstandener Ruß gelangte nicht in diesen Raum. Der angrenzende trockene Materialraum und die oberhalb der Wasserlinie gelagerten Bogen blieben unbeschädigt. Der Kläger macht sie folgerichtig nicht geltend. Der technische Nachtrag bestätigt durchgefeuchtete Baugruppen im unteren Maschinenteil und schließt einen vorbestehenden elektrisch verursachten Ausfall nach der dokumentierten Wartung nicht bloß abstrakt, sondern anhand der betroffenen Bauteile aus.

Beweis: gemeinsamer Ortsbefund mit Inventar, Anlage K3; technischer Nachtrag, Anlage K9; Zeugnis der Diplom-Ingenieurin Marisol Mohn, Technikbüro Mohn, Spindelgasse 21, 97082 Lindenquell. Erforderlichenfalls wird ein gerichtliches maschinen- und wassertechnisches Sachverständigengutachten angeboten. Anknüpfungstatsachen sind Wasserlinie, Schlauchlage, Zeitablauf, Wartungsbefund und ausgetauschte Baugruppen. Der Privatbefund ersetzt das gerichtliche Gutachten nicht.

Bei gesicherter Leitung wäre das Spülwasser in den Hofablauf gelangt. Die beschädigten Gegenstände befanden sich außerhalb des Brandbereichs. Weder notwendiges Löschwasser noch Rauch noch eine eigene undichte Leitung des Klägers erklären den örtlich begrenzten Befund. Der Kläger hat die Trocknung noch am selben Tag veranlasst und elektrische Geräte bis zur Freigabe stillgelegt. Er fordert keine hypothetischen Mehrschäden, die erst bei unterbliebener Trocknung eingetreten wären.

## 6 Einzelne Schadenpositionen

Die Instandsetzung der Falzmaschine kostete 22.800,00 EUR netto. Davon entfallen 10.400,00 EUR auf den Antrieb, 6.900,00 EUR auf zwei Steuermodule und 5.500,00 EUR auf Aus- und Einbau sowie Prüfung. Der Maschinenlieferant prüfte zunächst eine Reinigung; sie gewährleistete bei den wasserbelasteten Modulen keine sichere Funktion. Er ersetzte nur die benannten Bauteile. Weder eine größere Maschine noch zusätzliche Funktionen wurden beschafft. Die Vergleichsbetrachtung und die Weiterverwendung der Altmaschine sind in Anlagen K4 und K9 dokumentiert.

Für Absaugung und technische Trocknung wurden 6.480,00 EUR netto bezahlt. Die Leistung betraf ausschließlich den Maschinenraum und die betroffenen beweglichen Betriebsmittel. Reparaturen am Mietgebäude sind nicht eingeschlossen. Für die gesonderte Entsorgung unbrauchbarer Papierbogen und nasser Lagerhilfen fielen 1.200,00 EUR netto an. Der Bogenbestand wird mit seinem belegten Einstandswert von 8.640,00 EUR angesetzt; Verkaufserlöse oder eine Handelsspanne werden nicht hinzugerechnet. Verwertbare obere Lagen blieben im Bestand und sind bereits ausgeschieden. Ein weiterer Schrott- oder Verkaufserlös ist nicht angefallen.

Während der Reparatur vom 16.09. bis 29.09.2026 mietete der Kläger eine funktional vergleichbare Ersatzfalzmaschine einschließlich Anlieferung und Rückholung für 8.700,00 EUR netto. Sie wurde für vorhandene Aufträge eingesetzt. Die Werkstatt bestätigte den Bedarf und die Reparaturdauer. Der Kläger verlangt für dieselben Tage keinen entgangenen Gewinn. Der Mietaufwand war im Verhältnis zu den dokumentierten laufenden Aufträgen und der möglichen Fremdvergabe wirtschaftlich; die Vergleichsrechnung ist Anlage K4 beigefügt. Er behauptet keinen abstrakten Nutzungswert.

Diese Positionen ergeben 22.800,00 EUR + 6.480,00 EUR + 1.200,00 EUR + 8.640,00 EUR + 8.700,00 EUR = 47.820,00 EUR. Beweis für Rechnung, Zahlung und Zusammensetzung: Anlage K4; Zeugnis der Buchhalterin Nuria Klee, zu laden über den Betrieb des Klägers. Alle Rechnungsbeträge mit Umsatzsteuer wurden bezahlt; eingeklagt wird wegen der Vorsteuerabzugsberechtigung allein der Nettoaufwand. Der Eigentümer hat die beschädigten Gegenstände aus eigenen Mitteln erworben und keine Entschädigung einer Sachversicherung erhalten.

## 7 Einwendungen und anderweitiger Ersatz

Der Hinweis der Beklagten auf allgemeine Einsatzhektik trägt keine pauschale Haftungsfreistellung. Die Beklagte kann die tatsächlichen Abläufe bestreiten; deshalb werden die benannten Zeugen und gegebenenfalls ein Sachverständiger angeboten. Ein automatisches Beweisanzeichen allein aus dem Wassereintritt wird nicht verlangt. Die noch strittige Frage, wer den Spülzuruf gab, beseitigt nicht die dokumentierte Pflicht beider städtischen Funktionsbereiche zur sicheren Wasserfreigabe.

Ein Mitverschulden nach § 254 BGB liegt nicht vor. Der Kläger hielt das Kellerfenster im üblichen Kippzustand; dort war weder mit frei auslaufendem Schlauchwasser noch mit einem Brandangriff zu rechnen. Der Kläger blieb auf Aufforderung außerhalb des abgesperrten Hofs. Er durfte die Leitung nicht eigenmächtig bewegen. Frau Wacholder warnte sofort nach ihrer Wahrnehmung. Die Lagerung auf niedrigen Transportwagen genügte im normalen trockenen Maschinenraum; sie begründet keine Pflicht, ohne konkreten Anlass alle Betriebsmittel gegen einen fremdverursachten Wasserstrahl zu erhöhen.

Auch § 839 Abs. 1 Satz 2 BGB steht dem Anspruch nicht entgegen. Es gibt keinen festgestellten privaten Schädiger, keine Abtretung und keine Drittleistung. Nach dem Einsatzbericht deutet der Brandbefund auf einen technischen Defekt eines auf dem handgezogenen Transportwagen gelagerten Akkugeräts. Garagenzeile, Wagen und Gerät gehören ebenfalls der Beklagten. Ein etwaiger weiterer Anspruch gegen denselben Rechtsträger wäre keine anderweitige Ersatzmöglichkeit gegenüber einem Dritten. Vor allem betrifft die Klage einen gesonderten Rückbaufehler nach Brandende. Die fehlende eigene Sachversicherung und die unveränderte Anspruchsinhaberschaft bestätigt Anlage K8.

Art. 27 BayFwG enthält einen eigenständig zu prüfenden Entschädigungsanspruch und keinen Haftungsausschluss für schuldhafte Amtspflichtverletzungen. Der Kläger verlangt hier den konkret entstandenen Schaden aus dem bezeichneten fehlerhaften Rückbau. Die Prüfung dieses Anspruchs darf nicht mit der Frage verwechselt werden, ob er einen zumutbaren, notwendigen Eingriff zur Rettung seines eigenen Vermögens hätte hinnehmen müssen. Ein eigener Entschädigungsverwaltungsakt ist nicht Gegenstand dieser Klage.

## 8 Außergerichtlicher Stand und Zinsen

Die Klägervertreterin bezifferte den Schaden am 02.10.2026 und bat um Antwort bis zum 12.10.2026, Anlage K6. Die Beklagte antwortete am 05.10.2026 mit Sachfragen, ohne die Forderung endgültig zurückzuweisen oder eine Zahlung zuzusagen, Anlage K7. Der Kläger hat einen ausformulierten Entwurf beauftragt, jedoch noch keine Einreichung freigegeben, Anlage K8. Die außergerichtliche Aufklärung dauert an. Eine künftige Zahlung wäre vor Einreichung von der Forderung abzuziehen. Ein versäumtes Rechtsmittel im Sinne des § 839 Abs. 3 BGB ist nicht ersichtlich: Gegen die plötzlich erfolgende Wasserfreigabe stand dem abgesperrten Kläger keine rechtzeitig wirksame gerichtliche Abwehr zur Verfügung.

Der Zinsantrag stützt sich auf §§ 291, 288 Abs. 1 Satz 2 BGB. Er setzt weder einen erfundenen Zustellungstag noch einen bereits abgelaufenen außergerichtlichen Zahlungstermin voraus. Der Geschäftsbetrieb des Klägers macht den Schadensersatzanspruch nicht zu einer Entgeltforderung mit einem Zinssatz von neun Prozentpunkten. Gegen eine Entscheidung durch den Einzelrichter bestehen keine Bedenken. Ein Vergleich auf Grundlage der gesicherten Einzelpositionen bleibt möglich.

Leonie von Tann
Rechtsanwältin
'''


CASES = [dict(
    slug='akha-wuerzburg-feuerwehreinsatz',
    title='Würzburg: Das Schlauchende im Lichtschacht',
    summary='Nach einem gelöschten Garagenbrand wird beim Rückbau eine Leitung unkontrolliert gespült. Die benachbarte Buchbinderei verlangt 47.820 EUR; Stadt, Landkreis und Versicherer klären unterschiedliche Rollen.',
    is_new=True,
    core=[FOLDER+'02_Einsatzbericht.docx', FOLDER+'04_Befund_und_Inventar.docx', FOLDER+'05_Rechnungen_und_Zahlungen.docx', FOLDER+'06_Landkreis_Auskunft.pdf', FOLDER+'10_Vertragsauszug.docx', FOLDER+'15_Klageentwurf.docx'],
    notes='Alle Personen, Unternehmen, Lindenquell und Versicherungsbedingungen sind erfunden; der Landkreis Würzburg und das Gericht sind reale Einrichtungen, deren hier geschilderte Vorgänge vollständig fiktiv sind. Der Erstversicherer ist Mainbogen Kommunalversicherung VVaG. Die modellhafte Schadenexzedentenschwelle von 250.000 EUR stammt ausschließlich aus dem beigefügten Szenarioauszug und bildet keine tatsächlichen AKHA-Verhältnisse ab. Keine unmittelbare Forderung gegen AKHA oder Rückversicherer. Der Klageentwurf ist noch nicht eingereicht, die Antwortfrist 12.10.2026 noch offen. Word- und PDF-Fassungen der Briefe sind inhaltsgleich. Leistungsdaten und Bestätigungen sind Bestandteil des fiktiven Aktenbestands, keine realen Urkunden.',
    exhibits=FIRE_EXHIBITS,
    attachments={
        '01_Mandatsanfrage.eml': [FOLDER+'02_Einsatzbericht.docx'],
        '09_Mandantenfreigabe.eml': [FOLDER+'04_Befund_und_Inventar.docx', FOLDER+'05_Rechnungen_und_Zahlungen.docx'],
        '11_Stadt_an_Versicherer.eml': [FOLDER+'02_Einsatzbericht.docx', FOLDER+'06_Landkreis_Auskunft.pdf', FOLDER+'10_Vertragsauszug.docx'],
        '12_Versicherer_Rueckfragen.eml': [FOLDER+'08_Stadt_Zwischenantwort.pdf'],
    },
    documents=[
        email('01_Mandatsanfrage.eml', 'Knopf: Maschinenraum nass, bitte Anspruch prüfen', '''Sehr geehrte Frau von Tann,

ich betreibe die Buchbinderei im Kelterbogen 14. Die Feuerwehr hat gestern den Brand in der benachbarten Garage gelöscht. Danach lief durch unseren Lichtschacht Wasser aus einer Feuerwehrleitung in den Maschinenraum. Ich war hinter der Absperrung und durfte nicht hinein. Erst Frau Wacholder sah, wo das Wasser hinging. Der Kommandant hat mir heute den beigefügten Einsatzbericht gegeben; eine Kostenübernahme hat er nicht versprochen.

Die Maschine steht still. Eine Fachfirma hat Strom und Wasserreste gesichert; morgen soll die Diagnose erfolgen. Bitte melden Sie noch keinen runden Umsatzverlust an. Ich kann unsere Aufträge zum Teil durch eine Mietmaschine abarbeiten und möchte das zuerst vergleichen. Die nassen Papierbogen gehören mir. Der Hauseigentümer kümmert sich selbst um das Gebäude; ich möchte seinen Schaden nicht mit meinem zusammenwerfen.

Ich bitte um Anspruchsprüfung und einen Brief an die Stadt, sobald wir eine belastbare Aufstellung haben. Eine Klage soll zunächst nur vorbereitet werden. Nach meinem Versicherungskalender besteht seit Januar keine Inhaltsversicherung mehr. Ich suche den Kündigungsbeleg und lasse dies von der Buchhaltung bestätigen. Ich verspreche mir keine unmittelbare Zahlung von einem Rückversicherer; ich brauche einen Ansprechpartner für meinen Schaden.

Mit freundlichen Grüßen
Wendelin Knopf''', 'Wendelin Knopf <wendelin.knopf@buchbinderei.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '2026-09-15T16:10:00+02:00'),
        document('02_Einsatzbericht.docx', 'Einsatz 26-F144 und Rückbauvermerk', '''## 1 Einsatz und Beteiligte

Am 14.09.2026 wurde um 09:08 Uhr ein Brand an einem abgestellten handgezogenen Holztransportwagen in der städtischen Garagenzeile Kelterbogen 16 gemeldet. Garagenzeile, Wagen und das darauf gelagerte Akkugerät gehören der Stadt. Die Freiwillige Feuerwehr Lindenquell traf um 09:17 Uhr ein. Kommandant Kaspar Kresse übernahm und behielt die Einsatzleitung. Zwei Fahrzeuge und zwölf Kräfte der Stadt waren eingesetzt. Der Kreisbrandrat war telefonisch informiert, aber nicht vor Ort. Eine Übernahme oder Übertragung der Einsatzleitung erfolgte nicht. Eine Katastrophe wurde nicht festgestellt.

## 2 Zeitfolge

Um 09:31 Uhr wurde „Feuer aus“ gemeldet. Bei der Nachkontrolle um 09:42 Uhr bestanden keine offenen Glutstellen mehr. Um 09:46 Uhr begann auf Anweisung des Kommandanten der Rückbau. Eine drucklose C-Leitung lag neben dem Lichtschacht der Buchbinderei. Schlauchführer Tassilo Zorn berichtet, dass das offene Ende zunächst auf dem Schachtrand gelegen und beim Zusammenlegen hineingerutscht sei. Er hatte das Ende nicht festgehalten. Die Gitterabdeckung war teilweise beiseitegeschoben.

Maschinist Hanno Halm öffnete nach einem Zuruf um 09:49 Uhr die Wasserzufuhr zur Leitungsspülung. Den Rufenden kann er nicht sicher benennen. Er nahm ohne Sichtkontrolle oder Rückbestätigung an, das Ende liege beim Hofablauf. Gegen 09:55 Uhr warnte eine Nachbarin vor Wasser im Lichtschacht; um 09:57 Uhr war die Zufuhr geschlossen. Die Funkzeiten 09:31 und 09:46 stammen aus dem Protokoll, die übrigen Uhrzeiten aus den noch am Einsatztag abgeglichenen Notizen. Eine exakte Durchflussmessung existiert nicht.

## 3 Maßnahmen und Grenzen

Die Buchbinderei wurde stromlos geschaltet, stehendes Wasser abgesaugt und der Eigentümer verständigt. Es war kein Löschangriff in ihre Räume erfolgt. Während des Rückbaus bestand keine erneute Brandbekämpfungsnotwendigkeit. Die Mitglieder fertigten keine Innenaufnahmen an. Dieser Bericht ist keine Zahlungszusage.

Die erste technische Sichtung des ausgebrannten Transportwagens ergab einen möglichen Defekt des darauf gelagerten Akkugeräts; ein schuldhafter Umgang eines unabhängigen Dritten ist bislang nicht festgestellt. Der Wagen besitzt weder eigenen Antrieb noch eine Anhängervorrichtung für Kraftfahrzeuge. Die Brandursache ist nicht mit der Ursache des Wassereintritts gleichzusetzen. Die Wasserleitung und der Verteiler wurden technisch geprüft; ein Riss oder Ventildefekt wurde nicht festgestellt.

Kaspar Kresse, Kommandant, 15.09.2026''', date='15.09.2026'),
        email('03_Zeugin_Schlauchende.eml', 'Meine Wahrnehmung am Lichtschacht', '''Sehr geehrte Frau von Tann,

Herr Knopf hat mich gebeten, Ihnen meine Beobachtung aufzuschreiben. Ich heiße Jovana Wacholder und wohne im Kelterbogen 12, 97082 Lindenquell. Ich sah am 14. September vom Hofzugang aus einen Schlauch mit offenem Ende im Lichtschacht des Nachbarhauses. Aus dem Ende strömte Wasser. Das kleine Kellerfenster war gekippt; das Wasser lief gegen die Scheibe und in die Öffnung. Ich habe laut gerufen und auf den Schacht gezeigt. Nach meiner Handyuhr war es ungefähr 09:55 Uhr.

Ein Feuerwehrmann kam herüber, rief etwas zum Fahrzeug und kurz danach hörte der Wasserstrom auf. Ob es eine oder zwei Minuten dauerte, kann ich nicht sekundengenau sagen. Den ersten Löschangriff habe ich nicht gesehen, und ich kenne weder den Namen des Mannes noch den technischen Druck. Ich sah zu diesem Zeitpunkt keine Flammen mehr. Herr Knopf stand neben mir auf der anderen Seite der Absperrung und ging erst mit der Feuerwehr in den Keller.

Ich habe keine Fotos gemacht. Bitte nennen Sie meine Nachricht deshalb nicht Fotobeweis. Ich kann vor Gericht schildern, was ich gesehen habe. Über den Wert der Maschine weiß ich nichts. Die Frage, wer vorher den Befehl zur Spülung gab, kann ich ebenfalls nicht beantworten.

Mit freundlichen Grüßen
Jovana Wacholder''', 'Jovana Wacholder <jovana.wacholder@postfach.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '2026-09-17T11:20:00+02:00'),
        document('04_Befund_und_Inventar.docx', 'Ortsbefund und Schadeninventar Knopf', '''## 1 Besichtigung

Am 15.09.2026 besichtigten Wendelin Knopf, Buchhalterin Nuria Klee und Diplom-Ingenieurin Marisol Mohn den Maschinenraum. Die Nasslinie lag bis acht Zentimeter über dem Boden und nahm vom Lichtschacht aus ab. Der trockene Nebenraum und oberhalb der Linie gelagerte Ware zeigten keine Durchfeuchtung. Ein Rußeintrag oder eine thermische Beschädigung war im Maschinenraum nicht festzustellen. Es wurden schriftliche Maß- und Bestandsaufnahmen gefertigt; Fotografien gehören nicht zu diesem Vorgang.

## 2 Maschine

Betroffen ist die Falzmaschine FK-8, Inventarnummer WK-041, im Eigentum des Einzelkaufmanns Wendelin Knopf, erworben und bezahlt 2022. Der Antrieb und zwei untere Steuermodule lagen im Nassbereich. Die Maschine wurde seit 14.09.2026 nicht mehr betrieben. Die letzte dokumentierte Wartung am 04.08.2026 ergab ordnungsgemäße Funktion. Am 16.09. bestätigte der Herstellerkundendienst die Reparaturmöglichkeit. Der Rahmen, die obere Steuerung und die Falztaschen bleiben erhalten. Die technische Stellungnahme vom 02.10. ist gesondert abgeheftet.

## 3 Papier und weitere Kosten

Auf fünf niedrigen Wagen mit vier Zentimeter hoher Ladefläche standen 18 bereits bezahlte Lose hochwertiger Buchbogen. Zwölf vollständig durchnässte Lose mit zusammen 48.000 Bogen zu je 0,18 EUR Einstandswert waren nicht weiterverwendbar; der Wert beträgt 8.640,00 EUR netto. Die sechs oberen, trockenen Lose wurden nicht ausgebucht. Kein Ansatz enthält einen Verkaufspreis oder Gewinn. Lieferanteneigentum oder Eigentum eines Kunden besteht an diesen Bogen nicht.

Die Trocknung betraf ausschließlich den Maschinenraum und die darin stehenden beweglichen Sachen. Der Vermieter ließ eventuelle Gebäudefolgen gesondert prüfen. Dessen Rechnung wird nicht auf Knopf übertragen. Nasse Bogen wurden nach Freigabe am 18.09. entsorgt; zwei Musterlose bleiben als Beleg in verschlossenen Wannen verwahrt. Die ausgewechselten Module liegen beim Kundendienst zur Besichtigung. Einen allein durch Lagerung verursachten Vorschaden fand die gemeinsame Sichtung nicht.

Marisol Mohn, Nuria Klee, Wendelin Knopf; aufgenommen am 15.09., Inventar abgeglichen am 29.09., technischer Nachtrag vermerkt am 02.10.2026''', date='02.10.2026'),
        document('05_Rechnungen_und_Zahlungen.docx', 'Rechnungsabschriften und Zahlungsabgleich', '''## 1 Kundendienstrechnung MM-260929

Maschinenservice Marisol Mohn, Spindelgasse 21, 97082 Lindenquell, berechnet Wendelin Knopf für die am 29.09.2026 abgeschlossene Reparatur des Antriebs 10.400,00 EUR, zweier Steuermodule zusammen 6.900,00 EUR und Aus- und Einbau mit Funktionsprüfung 5.500,00 EUR. Nettosumme: 22.800,00 EUR; Umsatzsteuer 4.332,00 EUR; brutto 27.132,00 EUR. Zahlung am 30.09.2026 vollständig gutgeschrieben. Neue Zusatzfunktionen wurden nicht eingebaut. Die alte Maschine bleibt im Einsatz.

## 2 Trocknungsrechnung TS-260922

Trocknung Selma Sauer, Holunderbogen 9, 97082 Lindenquell, berechnet für Absaugung und Reinigung am 14./15.09. 1.680,00 EUR, acht Trocknungstage einschließlich Geräte und Kontrolle 3.840,00 EUR sowie Abbau und Schlussmessung 960,00 EUR. Netto 6.480,00 EUR; Umsatzsteuer 1.231,20 EUR; brutto 7.711,20 EUR. Gezahlt am 24.09.2026. Enthalten sind keine Putz-, Estrich- oder sonstigen Gebäudearbeiten.

## 3 Entsorgungsrechnung EE-260919

Entsorgung Erdmute Eichel, Weidenhügel 7, 97082 Lindenquell, berechnet für Abholung, Verwiegung und stoffgerechte Entsorgung der durchnässten Bogen und wertlosen Lagerhilfen 1.200,00 EUR netto, 228,00 EUR Umsatzsteuer und 1.428,00 EUR brutto. Der Auftrag wurde am 18.09. ausgeführt; Zahlung am 23.09. Ein Verwertungserlös wurde nicht erzielt. Zwei Musterlose wurden auf Wunsch des Eigentümers nicht entsorgt.

## 4 Warenwert

Der Wareneingang PB-260731 von Papierkontor Balthasar Bohne weist für die zwölf betroffenen Lose 48.000 Bogen zu 0,18 EUR aus. Netto 8.640,00 EUR, Umsatzsteuer 1.641,60 EUR, brutto 10.281,60 EUR. Die Lieferung wurde am 04.08. vollständig bezahlt; am 14.09. lag kein Eigentumsvorbehalt mehr vor. Die Inventurliste in der Befundakte scheidet die trockenen Lose ausdrücklich aus. Ein zweiter Ersatz derselben Bogen aus einer Nachbestellung wird nicht verlangt.

## 5 Ersatzmaschine

Die Rechnung LF-260930 von Leihtechnik Fridolin Fink, Mispelring 19, 97082 Lindenquell, betrifft 14 Kalendertage vom 16.09. bis einschließlich 29.09. zu je 550,00 EUR = 7.700,00 EUR sowie Anlieferung, Einrichtung und Rückholung zusammen 1.000,00 EUR. Netto 8.700,00 EUR; Umsatzsteuer 1.653,00 EUR; brutto 10.353,00 EUR. Bezahlt am 02.10. Die Maschine war hinsichtlich Format und Leistung mit der reparierten Maschine vergleichbar.

Nuria Klee verglich am 16.09. die verbindlichen Falzaufträge: Fremdvergabe hätte 12.400,00 EUR netto Bearbeitungs- und Transportkosten verursacht und 1.700,00 EUR eigene variable Kosten erspart. Der Mehraufwand von 10.700,00 EUR übersteigt die Miete von 8.700,00 EUR. Die Belegschaft erledigte die Aufträge mit der Mietmaschine; kein zusätzlicher Verdienstausfall.

## 6 Abgleich

Kontoabgleich Nuria Klee, 02.10.2026: Gesamtaufwand brutto 56.905,80 EUR, abzugsfähige Vorsteuer 9.085,80 EUR, geltend gemachter Nettoschaden 47.820,00 EUR. Keine Versicherungs- oder Vermieterzahlung, Abtretung oder Forderungsveräußerung. Die Abschriften erfassen Leistung, Betrag und Zahlung der Belege vollständig.''', date='02.10.2026'),
        letter('06_Landkreis_Auskunft.docx', 'Einsatz Lindenquell: Leitung und Zuständigkeit', '''Sehr geehrte Frau Färber,

zu Ihrer Anfrage vom 22. September haben wir die Meldung der örtlichen Feuerwehr und die Aufzeichnungen des Kreisbrandrats abgeglichen. Der Kreisbrandrat wurde über den Einsatz telefonisch unterrichtet. Er kam weder an die Einsatzstelle noch übernahm er die Leitung. Eine Übertragung auf eine andere Person nach Art. 18 Abs. 5 BayFwG ist nicht dokumentiert. Nach dem Bericht führte Kommandant Kaspar Kresse die örtlichen Kräfte bis zum Einsatzende. Eine Katastrophenfeststellung oder Leitung nach dem Bayerischen Katastrophenschutzgesetz erfolgte nicht.

Die von Ihrer Verwaltung angesprochene Förderung eines Geräteanhängers durch den Landkreis betrifft die Ausstattung, nicht die Übernahme dieses Einsatzes. Art. 2 BayFwG ordnet dem Landkreis überörtliche Aufgaben zu. Daraus folgt nicht, dass jeder Einsatz einer kreisangehörigen Feuerwehr im Namen des Landkreises geführt wird. Der hier betroffene Schlauch und der Verteiler gehören nach Ihrer Geräteliste zudem zum eigenen Bestand der Stadt. Wir geben damit keine abschließende rechtliche Beurteilung sämtlicher denkbarer Haftungsfragen ab, sondern bestätigen die in unseren Unterlagen feststellbaren Zuständigkeits- und Ablaufdaten.

Für den Schaden des Nachbarbetriebs ist zwischen der Brandbekämpfung und dem späteren Umgang mit der offenen Leitung zu unterscheiden. Unser Sachgebiet war an der Wasserfreigabe nicht beteiligt. Einen technischen Befund zum Druck oder zur konkreten Schlauchlage können wir daher nicht beisteuern. Bitte sichern Sie die eigenen Einsatzunterlagen und die voneinander getrennten Erinnerungen der unmittelbar beteiligten Kräfte. Nachträgliche Ergänzungen sollten mit ihrem Erstellungsdatum erkennbar bleiben.

Wir behandeln Ihre Anfrage als Sachaufklärung zwischen Behörden. Eine Regulierungsvollmacht für Ihren Versicherer, eine Deckungszusage des Landkreises oder ein Schuldanerkenntnis wird hiermit nicht erklärt. Eine Weitergabe an Ihre Rechtsvertretung und den mit dem Fall befassten Haftpflichtversicherer ist im erforderlichen Umfang möglich. Bitte legen Sie diesem Schreiben keine unbeteiligten medizinischen oder sonstigen besonders persönlichen Daten bei.

Mit freundlichen Grüßen
Dr. Erdmute Eberlein
Sachgebiet Feuerwehrwesen''', COUNTY, CITY, '25.09.2026'),
        letter('07_Anspruchsschreiben.docx', 'Knopf: Bezifferter Anspruch aus dem Rückbau', '''Sehr geehrte Frau Färber,

ich vertrete Herrn Wendelin Knopf, Inhaber der Buchbinderei im Kelterbogen 14. Wir machen wegen des Wassereintritts vom 14. September 47.820,00 EUR geltend. Die beigefügten Belegabschriften weisen 22.800,00 EUR Maschinenreparatur, 6.480,00 EUR Trocknung, 1.200,00 EUR Entsorgung, 8.640,00 EUR verlorenen Bogenbestand und 8.700,00 EUR Ersatzmaschinenmiete aus. Alle Beträge sind wegen der Vorsteuerabzugsberechtigung netto. Ein Gebäudeschaden des Vermieters, ein pauschaler Gewinnverlust und die zugleich vermiedene Fremdvergabe sind nicht in dieser Summe enthalten.

Nach dem Einsatzbericht war die Brandbekämpfung bereits beendet, als die Leitung zur Spülung erneut mit Wasser beaufschlagt wurde. Ihr offenes Ende lag ungesichert im Lichtschacht. Mein Mandant verlangt deshalb keinen Ausgleich dafür, dass die Feuerwehr den Nachbarbrand überhaupt bekämpfte. Er beanstandet eine gesonderte, vermeidbare Beschädigung beim Rückbau. Die Wasserfreigabe hätte nach Sichtkontrolle oder bestätigter Übergabe unterbleiben beziehungsweise am gesicherten Hofablauf erfolgen können.

Die Auskunft des Landkreises grenzt dessen Rolle ab. Eine Übernahme der Einsatzleitung ist nicht erfolgt. Wir richten den Anspruch aus § 839 BGB in Verbindung mit Art. 34 GG daher gegen Ihre Stadt. Der Hinweis auf Nothilfe lässt einfache Fahrlässigkeit nicht generell entfallen; hierzu verweisen wir auf BGH, Urteil vom 14.06.2018 – III ZR 54/17, BGHZ 219, 77, Rn. 47, 53. Der dortige Löschschaumfall wird ausschließlich wegen des Haftungsmaßstabs angeführt.

Bitte teilen Sie uns bis zum 12. Oktober mit, welche konkrete Position oder Tatsachenangabe aus Ihrer Sicht weiterer Klärung bedarf und ob Sie eine Regulierung veranlassen. Ausgetauschte Module und Papiermuster werden zur Besichtigung aufbewahrt. Mein Mandant ist zu einer abgestimmten Besichtigung bereit. Eine Zahlung eines Dritten oder eine Abtretung liegt nicht vor. Eine gerichtliche Einreichung ist bisher nicht erfolgt; der angefragte Antworttermin ist am heutigen Tag noch offen.

Mit freundlichen Grüßen
Leonie von Tann
Rechtsanwältin''', LAWYER, CITY, '02.10.2026'),
        letter('08_Stadt_Zwischenantwort.docx', 'Knopf: Zwischenantwort und weitere Aufklärung', '''Sehr geehrte Frau von Tann,

Ihr Schreiben vom 2. Oktober mit der Bezifferung auf 47.820,00 EUR liegt uns vor. Wir haben die Unterlagen zur Haftungs- und Deckungsprüfung weitergeleitet. Die Stadt trifft mit diesem Zwischenbescheid keine abschließende Entscheidung über Grund oder Höhe. Insbesondere ist die Beteiligung unseres Versicherers weder ein Schuldanerkenntnis gegenüber Ihrem Mandanten noch eine Übertragung unserer Stellung als möglicher Anspruchsgegner.

Der Kommandant bestätigt die Beendigung der eigentlichen Brandbekämpfung vor Beginn des Rückbaus. Offen bleibt, von wem der Zuruf zur Spülung stammte und welche Verständigung zwischen Schlauchtrupp und Maschinist vorausging. Wir lassen hierzu getrennte Ergänzungen erstellen. Die bloße Behauptung eines Notfalleinsatzes wird unsere Stellungnahme nicht ersetzen. Zugleich bitten wir um Verständnis, dass ein nachträglich erkennbarer Wassereintritt allein noch keine vollständige Rekonstruktion des Verschuldens erlaubt.

Zur Maschine benötigen wir die Abgrenzung zwischen Reparatur und Verbesserung sowie die Bestätigung, welche ausgebauten Teile weiterhin besichtigt werden können. Bitte erläutern Sie außerdem die Zahl der tatsächlich durchnässten Papierlose und die zeitliche Überschneidung der Ersatzmiete mit der Reparatur. Der Ansatz von Nettobeträgen ist bei dem beschriebenen Vorsteuerabzug grundsätzlich nachvollziehbar. Die vorgelegten Zahlungsangaben werden wir mit den Einzelrechnungen und dem Inventar abgleichen; ein pauschaler Prozentabschlag ist derzeit nicht vorgesehen.

Die Anfrage an den Landkreis diente der Klärung von Einsatzleitung und Ausstattung. Aus der dortigen Auskunft ergibt sich keine eigene Beteiligung an der Wasserfreigabe. Wir möchten den Vorgang deshalb nicht durch eine unbegründete Verweisung Ihres Mandanten zwischen Behörden verzögern. Ein denkbarer interner Erstattungsweg wäre gesondert zu prüfen und könnte eine begründete Außenhaftung nicht von sich aus beseitigen.

Wir halten Ihren Antworttermin 12. Oktober im Blick und bitten um den angekündigten technischen Nachtrag. Eine endgültige Ablehnung oder ein Vergleichsangebot ist mit diesem Schreiben nicht verbunden. Bei neuen Belegen zur Schadenminderung würden wir eine Besichtigung kurzfristig abstimmen.

Mit freundlichen Grüßen
Kunigunde Färber
Rechtsstelle''', CITY, LAWYER, '05.10.2026'),
        email('09_Mandantenfreigabe.eml', 'Klageentwurf bitte vorbereiten, noch nicht einreichen', '''Sehr geehrte Frau von Tann,

bitte erstellen Sie jetzt den vollständigen Klageentwurf mit Anträgen, Rechtsgründen und Anlagen. Er soll noch nicht eingereicht werden. Die Stadt soll ihre angekündigte Antwort bis zum 12. Oktober geben können. Ich schicke die ergänzte Befund- und Rechnungsübersicht als Anlagen. Frau Klee hat den Zahlungslauf bis Freitag abgeglichen: Es ist alles bezahlt; von Stadt, Versicherer oder Vermieter kam nichts zurück.

Die Maschine und die aufgeführten Papierbogen gehören mir allein. Aufträge meiner Kunden begründen kein Eigentum an diesen unbedruckten Bogen. Unsere Inhaltsversicherung endete am 31.12.2025; im laufenden Jahr wurde kein Anschlussvertrag geschlossen. Eine Leistung daraus habe ich nicht beantragt und kann ich für September nicht erhalten. Ansprüche habe ich weder abgetreten noch verkauft. Auch der Vermieter hat mir nichts erstattet und verfolgt eventuelle Schäden an seinem Gebäude selbst.

Mir ist wichtig, dass die 8.700 Euro Miete nicht neben einem zusätzlich erfundenen Gewinnverlust stehen. Wir konnten die Aufträge mit der gemieteten Maschine abarbeiten. Die Fremdvergabe wäre nach unserem Vergleich teurer geworden. Bitte lassen Sie im Entwurf stehen, dass Frau Wacholder keine Fotos hat. Der technische Nachtrag von Frau Mohn kommt ebenfalls heute. Wenn Sie noch einen konkreten Beleg brauchen, fragen Sie bitte Frau Klee und mich gemeinsam.

Mit freundlichen Grüßen
Wendelin Knopf''', 'Wendelin Knopf <wendelin.knopf@buchbinderei.example>', 'Leonie von Tann <kanzlei@von-tann.example>', '2026-10-05T09:20:00+02:00'),
        document('10_Vertragsauszug.docx', 'Deckungsunterlagen: Vereinbarter Prüffall LQ-AH-2026', '''## 1 Vertragsinhalt der Fallakte

Versicherungsnehmerin ist die Stadt Lindenquell; Versicherer ist Mainbogen Kommunalversicherung VVaG. Im Vertrag LQ-AH-2026 für den Zeitraum 01.01. bis 31.12.2026 ist die gesetzliche Haftpflicht aus der gemeindlichen Feuerwehr einschließlich Rückbau und Wiederherstellung der Einsatzbereitschaft erfasst. Die Prüfung der Haftung sowie die Abwehr unbegründeter und Befriedigung begründeter Ansprüche gehören zum vereinbarten Leistungsumfang. Die Sachschadendeckung beträgt 5.000.000 EUR je Ereignis. Für Sachschäden ist ein Selbstbehalt von 1.000 EUR vereinbart. Er verändert den Außenanspruch eines Geschädigten nicht.

## 2 Meldung und Regulierung

Die Stadt meldet mögliche Versicherungsfälle unverzüglich nach Kenntnis an die Schadenabteilung und reicht wesentliche Berichte sowie Bezifferungen nach. Die Meldebestätigung ersetzt keine Anerkennung der Außenforderung. Vergleiche werden zwischen Stadt und Versicherer abgestimmt; eine Freigabe im Innenverhältnis ist kein Vertrag mit dem Geschädigten. Daten werden nur im erforderlichen Umfang über den geschützten Schadenkanal übermittelt. Ein Landkreis wird nicht allein wegen seiner Aufsichtstätigkeit mitversichert.

## 3 Rückversicherung im Szenario

Der Versicherer hält für diesen Vertragsbestand eine eigene Schadenexzedentenvereinbarung mit Kranich Rückversicherung AG. Sie setzt bei 250.000 EUR versicherter Entschädigung je Ereignis oberhalb der Selbstbeteiligung des Erstversicherers an; Kostenregelungen und Kumule wären gesondert abzustimmen. Eine Einzelanzeige ist ab einer voraussichtlichen Belastung von 200.000 EUR sowie bei erkennbar zusammengehörigen Serienschäden vorgesehen. Der vorliegende, isolierte Sachschaden von 47.820 EUR erreicht diese Schwelle nicht. Es wird daher keine fallbezogene Rückversichererkorrespondenz erzeugt.

## 4 Herkunft und Reichweite

Die vorstehenden Vertragsbestimmungen sind eine vollständige didaktische Vereinbarung ausschließlich für diesen fiktiven Prüffall. Sie sind keine Wiedergabe tatsächlicher Bedingungen von AKHA, BADK, eines bestehenden Kommunalversicherers oder eines realen Rückversicherers. Eine AKHA-Mitgliedschaft oder Beteiligung wird für diesen Vorgang nicht unterstellt. Die Ausfertigung wurde im Fallarchiv am 18.09.2026 zur Schadenakte genommen. Unterzeichnet im Szenario durch Roswitha Kren für die Stadt und Severin Salbei für den Versicherer.''', date='18.09.2026'),
        email('11_Stadt_an_Versicherer.eml', 'Schaden MK-F-260914: Einsatzbericht und Kreisantwort', '''Sehr geehrter Herr Salbei,

wir ergänzen unsere Erstmeldung vom 16. September um den Einsatzbericht, die Auskunft des Landkreises und den zur Akte genommenen Vertragsauszug. Der Anspruch wird inzwischen mit 47.820 Euro netto beziffert. Die Originalforderungen und die weitere Belegübersicht liegen im geschützten Schadenkanal. Die Gemeindezugehörigkeit unseres Kommandanten und seiner Kräfte ist unstreitig; eine Leitung durch den Kreisbrandrat hat nicht stattgefunden.

Bitte prüfen Sie die Haftung aus dem Rückbau gesondert von der Notwendigkeit des Löschangriffs. Wir möchten dem Kläger nicht pauschal entgegenhalten, Feuerwehrarbeit sei nur bei grober Fahrlässigkeit haftungsrelevant. Offen sind die konkrete Verständigung vor Öffnung des Ventils und der technisch erforderliche Reparaturumfang. Frau von Tann bietet die Besichtigung ausgebauter Teile und zweier Papiermuster an. Wir werden die Frist bis 12. Oktober für eine sachbezogene Antwort nutzen.

Nach dem bisherigen Einzelbetrag sehen wir keinen Anlass für eine besondere Rückversicherermeldung. Bitte bestätigen Sie dies anhand der für unseren Bestand geltenden Vereinbarung; aus einer allgemeinen Rubrik „Rückdeckung“ sollen keine fremden Bedingungen in den Vorgang geraten. Der Selbstbehalt ist intern zu verbuchen. Er wird nicht als Abzug gegenüber Herrn Knopf dargestellt. Eine Zahlung haben wir bislang nicht angewiesen und einen Vergleich nicht angeboten.

Mit freundlichen Grüßen
Kunigunde Färber''', 'Kunigunde Färber <recht@lindenquell.example>', 'Severin Salbei <schaden@mainbogen-kommunal.example>', '2026-10-02T16:40:00+02:00'),
        email('12_Versicherer_Rueckfragen.eml', 'MK-F-260914: Sachprüfung, Reserve und Meldeweg', '''Sehr geehrte Frau Färber,

wir führen den Fall unter MK-F-260914 im Vertrag LQ-AH-2026. Die gemeldete Tätigkeit fällt nach dem vorgelegten Sachverhalt in den beschriebenen versicherten Bereich. Die Haftungshöhe ist damit noch nicht anerkannt. Wir haben vorläufig 47.820 Euro Entschädigungsaufwand eingestellt und den Selbstbehalt von 1.000 Euro gesondert vermerkt. Eine Reserve ist keine Zahlungszusage und wird nicht als bereits erbrachte Leistung an die Klägerseite gemeldet.

Die beigefügte Zwischenantwort Ihrer Rechtsstelle enthält die richtigen konkreten Nachfragen. Bitte reichen Sie die technische Abgrenzung, die Belege zur Miete und die Bestätigung fehlender Drittzahlungen nach. Für eine Regulierungsentscheidung möchten wir insbesondere wissen, ob neue Maschinenteile einen messbaren Vorteil über die Wiederherstellung hinaus schaffen. Ein ungeprüfter Abzug „neu für alt“ kommt ebenso wenig in Betracht wie eine ungesehene Übernahme sämtlicher Kosten.

Die in Ihrem Auszug dokumentierte Einzelmeldeschwelle der Rückversicherung ist nicht erreicht. Es gibt bisher auch keinen Hinweis auf weitere zum selben Ereignis zusammenzufassende Großforderungen. Deshalb eröffnen wir dort keinen Einzelfall. Sollten Gebäudeschäden oder weitere Betroffene bekannt werden, prüfen wir das Kumul erneut. Der Landkreis, AKHA und der Rückversicherer werden nicht vorsorglich als unmittelbare Gegner des Buchbinders bezeichnet. Für den Außenkontakt bleibt Ihre Stadt zuständig.

Mit freundlichen Grüßen
Severin Salbei''', 'Severin Salbei <schaden@mainbogen-kommunal.example>', 'Kunigunde Färber <recht@lindenquell.example>', '2026-10-05T14:10:00+02:00'),
        document('13_Technik_Nachtrag.docx', 'Technischer Nachtrag: Falzmaschine, Trocknung und Ersatzmiete', '''## 1 Auftrag und Material

Wendelin Knopf beauftragte die technische Abgrenzung des Wasserschadens an FK-8. Ausgewertet wurden der gemeinsam aufgenommene Nassbereich, die Wartung vom 04.08., die Diagnose vom 16.09. und die bis 29.09. abgeschlossene Reparatur. Die Aussage zur Einwirkungsrichtung stützt sich auf den örtlichen Befund, nicht auf eine persönliche Beobachtung des Schlauchbetriebs. Ein gerichtliches Gutachten wird hierdurch nicht ersetzt.

## 2 Schaden und Reparatur

Der Wasserstand erreichte Antrieb und zwei untere Steuermodule. Dort fanden sich Feuchterückstände; die oberen Komponenten blieben trocken. Die während der Wartung festgehaltenen Funktionswerte waren unauffällig. Der Kundendienst führte an den feuchten Modulen zunächst eine Reinigung und Isolationsprüfung durch; die Freigabewerte wurden nicht erreicht. Ersatz war erforderlich. Antrieb und Module wurden durch baugleiche aktuelle Ersatzteile ersetzt, ohne Leistungssteigerung, Kapazitätserweiterung oder Verlängerung eines vereinbarten Wartungsintervalls. Ein eigenständiger wirtschaftlicher Mehrwert gegenüber einer funktionsfähigen reparierten Maschine ist technisch nicht erkennbar; eine rechtliche Vorteilsausgleichung entscheidet dies nicht vorweg.

## 3 Zeit und Vermeidung von Mehrkosten

Die Reparatur dauerte wegen Diagnostik und Teilelieferung vom 16.09. bis 29.09.2026. Die Schlussprüfung erfolgte am 29.09. um 15:40 Uhr. Die Leihmaschine war nur während dieser Zeit vorhanden. Ihre Rückholung war Bestandteil des Pauschaltransports. Eine technisch zumutbare frühere Wiederaufnahme mit der beschädigten Maschine bestand nicht. Durch die sofortige Abschaltung und die Trocknung wurde eine weitere Beschädigung der oberen Baugruppen vermieden.

## 4 Vorbehalte und Sicherung

Die Ersatzteile beweisen nicht für sich, wer den Schlauch öffnete. Zum Brandort lag keine räumliche Verbindung durch Rauch oder Löschwasserablauf in der Garage vor. Die Wasserlinie konzentrierte sich unmittelbar hinter dem Lichtschacht. Ein eigener Rohrbruch wurde bei der Sichtung nicht gefunden. Die ausgebauten Module werden bis 30.11.2026 aufbewahrt; eine Besichtigung kann nach Terminabsprache erfolgen. Zwei Musterlose Papier bleiben beim Betrieb. Der Umfang der nicht mehr verwendbaren Bogen wurde mit der Buchhaltung und dem Inventar abgeglichen.

Diplom-Ingenieurin Marisol Mohn, 02.10.2026''', date='02.10.2026'),
        document('14_Rechts_und_Rollenvermerk.docx', 'Rechtsvermerk: Feuerwehr, Stadt und Landkreis', '''## 1 Prüfauftrag und Ergebnis

Der Rückbau nach dem Einsatz ist funktional Teil der gemeindlichen Tätigkeit. Bei bewiesenem ungesichertem Spülen haftet grundsätzlich die Stadt aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG. Die Lehreinheit trennt den erforderlichen Löschangriff von einem vermeidbaren späteren Ausführungsfehler. Ein Sachschaden allein beweist weder Fahrlässigkeit noch die Schadenshöhe.

## 2 Rollen

Art. 1 BayFwG betrifft die gemeindliche Pflichtaufgabe, Art. 2 die überörtliche Ausstattung durch den Landkreis und Art. 18 die konkrete Einsatzleitung. Hier blieb diese beim örtlichen Kommandanten. Das ist belegt und wird nicht aus der bloßen Kreisangehörigkeit abgeleitet. Art. 9 BayFwG regelt Freistellungs-, Entgeltfortzahlungs- und Erstattungsansprüche der Feuerwehrdienstleistenden; er ist keine Anspruchsgrundlage für den außenstehenden Buchbinder.

Art. 27 BayFwG ist gesondert zu lesen: unzumutbarer Schaden, Subsidiarität, Ausschluss bei unmittelbarem Schutz des Betroffenenvermögens und Begrenzung auf Vermögensschaden sind eigene Voraussetzungen. Die Norm verdrängt eine schuldhafte Amtspflichtverletzung nicht durch eine pauschale „Einsatzimmunität“. Ob notwendige Maßnahmen einen Entschädigungsanspruch ausgelöst hätten, entscheidet den hier geltend gemachten Rückbaufehler nicht.

## 3 Rechtsprechungsanker und Beweis

BGH, Urteil vom 14.06.2018 – III ZR 54/17, BGHZ 219, 77, Rn. 47 und 53: Für Amtshaftung bei amtlicher Gefahrenabwehr besteht kein allgemeines Nothelferprivileg nach § 680 BGB. Dieser Anker ersetzt die konkrete ex-ante-Sorgfaltsprüfung nicht. Die dort behandelten PFOS-Folgen dürfen nicht auf gewöhnliches Wasser übertragen werden. Für diesen Fall müssen die Leitungslage, Kommunikation vor Freigabe, zeitliche Entspannung und technische Ursächlichkeit bewiesen werden.

## 4 Deckung und nächste Schritte

Die dokumentierten Bedingungen ergeben einen möglichen Erstversicherungsschutz mit 1.000 EUR Selbstbehalt. Weder Selbstbehalt noch Reserve kürzen den Außenanspruch. Die fiktive Einzelmeldeschwelle der Rückversicherung ist derzeit nicht erreicht. Eine tatsächliche AKHA-Beteiligung ist nicht vereinbart. Vor einer Klageeinreichung sind Antwortstand, Zahlungen, Eigentum, Abtretungen und konkrete Beweisanschriften erneut abzugleichen. Der vorliegende Auftrag betrifft zunächst nur die Vorbereitung; kein Schriftsatz wurde versandt.'''),
        document('15_Klageentwurf.docx', 'Klageentwurf Knopf gegen Stadt Lindenquell', FIRE_CLAIM, 'claim', LAWYER, 'Landgericht Würzburg'),
    ],
)]

CASES.append(dict(
    slug='akha-wuerzburg-fahrzeugschaden', title='Dinkel: Versicherungsweg und Belegabgleich',
    summary='Die am Nachmittag aufgefundenen Fuhrparkunterlagen ermöglichen erstmals eine belegte Schadenmeldung; Fahrerhaftung, Stadt, Kfz-Deckung und Rückdeckung bleiben getrennt.',
    is_new=False, core='Konkrete Halterhaftung, hoheitliche Sicherungsfahrt, Schadenhöhe und erstmalig dokumentierter Deckungsweg.',
    notes='Die neuen Archiv- und Versicherertatsachen treten erst am 05.10.2026 nach 16:30 Uhr hinzu. Frühere Nachrichten über fehlende Unterlagen und die bisherigen Ansprüche bleiben unverändert. Mainbogen Kommunalversicherung VVaG und die hier wiedergegebenen Bedingungen sind reine Fallfiktion; kein Nachweis tatsächlicher AKHA-Beteiligung. Der bestehende Klageentwurf bleibt bei 2.188,80 EUR und ist nicht eingereicht.',
    exhibits=[],
    attachments={
        '03_Stadt_Belegversand.eml': [FOLDER+'01_Stadt_Schadenanzeige.pdf', '02_Fahrerbericht.docx', '03_Fahrzeug_und_Einsatz.docx', '05_Reparaturrechnung.docx', '06_Taxibelege.docx'],
        '04_Versicherer_Bearbeitungsstand.eml': [FOLDER+'02_Versicherer_Bestaetigung.pdf'],
    },
    documents=[
        letter('01_Stadt_Schadenanzeige.docx', 'Fuhrpark 17: Erstmeldung nach Eingang der Vertragsausfertigung', '''Sehr geehrter Herr Salbei,

wir melden den Streifkontakt unseres Transporters mit dem Fahrzeug des Herrn Tassilo Dinkel am 8. September. Die heute um 16:35 Uhr aus dem Vertragsarchiv eingegangene Ausfertigung ordnet Fuhrparknummer 17 dem Kfz-Haftpflichtvertrag MK-KFZ-2026 zu. Sie gilt vom 1. Januar bis 31. Dezember 2026 und nennt unsere Stadt als Versicherungsnehmerin. Diese Ergänzung erklärt, warum Frau Kren in ihrer Nachricht vom 30. September noch keinen vollständigen Vertragsstand nennen konnte. Eine rückdatierte Schadenmeldung wird daraus nicht gemacht.

Herr Dinkel verfolgt nach seiner heutigen Erklärung 2.188,80 EUR. Darin stecken 2.142,00 EUR bezahlte Reparaturkosten und 46,80 EUR für zwei Werkstattfahrten. Die ursprünglich verlangten 25,00 EUR Abwicklungspauschale sind ausdrücklich ausgeklammert. Unser Fahrer beschreibt den Kontakt beim Vorwärtsfahren; die Zeugin sah den Wagen innerhalb der Parkbucht. Streitfragen bestehen vor allem zur Belegvervollständigung und nicht zu einem behaupteten Verkehrsmanöver des Geschädigten.

Der Auftrag unserer Disposition betraf die unmittelbare Sicherung einer Fahrbahnabsenkung. Wir bitten deshalb neben der Halterhaftung um Beachtung der hoheitlichen Einordnung. Eine persönliche Inanspruchnahme des Fahrers wird gegenüber der Klägervertreterin nicht als alternative Regulierung angeboten. Der Landkreis hatte weder Fahrzeugherrschaft noch Einsatzauftrag. Wir leiten die Sache nicht allein wegen unserer Kreisangehörigkeit an ihn weiter.

Bitte bestätigen Sie Vertrag, Bearbeitungszeichen und erforderliche Nachforderungen. Wir stellen mit gesonderter E-Mail die vorhandenen Belege bereit. Die Werkstattbilder fehlen weiterhin; ihre Existenz wird nicht mit ihrem Eingang verwechselt. Die Klägervertreterin hat den Antworttermin 12. Oktober beibehalten. Wir haben heute noch keine Zahlung oder verbindliche Deckung gegenüber ihr erklärt. Ein möglicher interner Selbstbehalt darf in einer späteren Außenabrechnung nicht einfach von den belegten Kosten abgezogen werden. Zu einer Ausgleichseinrichtung oder Rückversicherung liegen der Stadt keine eigenen Anspruchsunterlagen vor.

Mit freundlichen Grüßen
Kunigunde Färber''', CITY, INSURER),
        letter('02_Versicherer_Bestaetigung.docx', 'Dinkel: Vertragsbestätigung und begrenzter Prüfauftrag', '''Sehr geehrte Frau Färber,

wir bestätigen um 18:10 Uhr den Eingang Ihrer heutigen Meldung unter MK-KFZ-26391. Nach unserer Vertragsverwaltung war Fuhrparknummer 17 am 8. September im Vertrag MK-KFZ-2026 erfasst. Der Versicherungsschutz erstreckt sich auf gesetzliche Haftpflichtansprüche aus dem Gebrauch des bezeichneten Fahrzeugs einschließlich der beschriebenen dienstlichen Sicherungsfahrt. Als Leistung sind Prüfung und Abwehr unbegründeter sowie Befriedigung begründeter Ansprüche vereinbart. Ein Selbstbehalt für diesen Haftpflichtschaden ist nicht vereinbart. Die Vertragsbestätigung ist noch keine Anerkennung jeder einzelnen Forderungsposition.

Bitte halten Sie die reduzierte Anspruchssumme von 2.188,80 EUR fest. Die Rechnung betrifft nach den Unterlagen allein die linke hintere Tür. Der rechte vordere Stoßstangenkratzer darf weder als unfallbedingter Schaden vergütet noch als Grund für eine pauschale Ablehnung der gesamten Reparatur verwendet werden. Die zwei Taxifahrten sind anhand der konkreten Werkstattzeiten und der Nichtverfügbarkeit des zweiten Familienwagens zu beurteilen. Eine zusätzliche Nutzungsausfallentschädigung wird nicht gefordert.

Wir bitten um Nachreichung der angekündigten Annahmebilder, sobald diese tatsächlich verfügbar sind. Bis dahin erlauben Fahrerbericht und Zeugin eine Sachprüfung, aber keine fotografische Beweissicherung. Der Sicherungsauftrag wird bei der Prüfung von Art. 34 GG und § 18 StVG berücksichtigt. Der eigenständige Anspruch gegen die Halterin wird hierdurch nicht übergangen. Ob daneben ein Direktanspruch aus einem Versicherungsverhältnis eröffnet ist, ändert nichts daran, dass der vorliegende Klageentwurf allein gegen Ihre Stadt gerichtet ist.

Eine einzelne Rückversichereranzeige ist für diese isolierte Forderung in unserer Bearbeitung nicht veranlasst. Mit diesem Schreiben wird keine Zugehörigkeit Ihrer Stadt zu AKHA oder einer anderen Ausgleichseinrichtung bestätigt. Sollte später ein davon abweichender Vertrag vorgelegt werden, wäre er gesondert zu prüfen. Bitte richten Sie Ihre Sachantwort bis zum 12. Oktober an die Klägervertreterin; eine Zahlung ist bislang weder von uns noch von Ihrer Stadt gebucht.

Mit freundlichen Grüßen
Severin Salbei
Schadenabteilung''', INSURER, CITY),
        email('03_Stadt_Belegversand.eml', 'MK-KFZ-26391: Erstmeldung mit Fahrer-, Einsatz- und Kostenbelegen', '''Sehr geehrter Herr Salbei,

anbei finden Sie die heutige Schadenanzeige als PDF, den unveränderten Fahrerbericht, die Fuhrparkauskunft, die Reparaturrechnung und die Taxibelege. Die Vertragsausfertigung kam erst um 16:35 Uhr aus dem Archiv; der frühere Schriftwechsel wird dadurch nicht rückwirkend berichtigt. Die Mitteilung an Frau von Tann von 16:10 Uhr enthielt folgerichtig noch keine Versicherungszusage.

Bitte verwenden Sie die tatsächlich bezifferten 2.188,80 Euro. In der Forderung vom 24. September standen noch 25 Euro mehr. Herr Dinkel hat diese Pauschale heute aus seinem Klageauftrag herausgenommen, ohne eine Zahlung zu erhalten. Die Rechnung über die Tür ist vollständig bezahlt. Der ältere Kratzer vorne rechts wurde nicht bearbeitet. Die Belege zu den Taxifahrten betreffen ausschließlich Abgabe und Abholung; der andere Familienwagen war nach der ergänzenden Erklärung im Schichteinsatz der Ehefrau.

Wir wollen keinen automatischen Prozentsatz für fehlende Fotos ansetzen. Bitte nennen Sie gegebenenfalls eine einzelne Rechnungsposition, deren Erforderlichkeit Sie nicht nachvollziehen können. Der Werkstattinhaber wird um die bereits angekündigten Bilder gebeten. Der Landkreis ist an diesem örtlichen Sicherungsauftrag nicht beteiligt. Eine Nachricht an eine Rückversicherung oder Ausgleichseinrichtung habe ich nicht veranlasst.

Mit freundlichen Grüßen
Kunigunde Färber''', 'Kunigunde Färber <recht@lindenquell.example>', 'Severin Salbei <schaden@mainbogen-kommunal.example>', '2026-10-05T17:10:00+02:00'),
        email('04_Versicherer_Bearbeitungsstand.eml', 'MK-KFZ-26391: Bestätigung beigefügt, noch keine Zahlung', '''Sehr geehrte Frau Färber,

anbei übersenden wir die unterzeichnete Vertrags- und Bearbeitungsbestätigung als PDF. Unsere heutige Prüfung knüpft an die tatsächlich übermittelten Unterlagen an. Ein Werkstattfoto befindet sich nicht in den Anlagen Ihrer E-Mail; wir werden es deshalb weder in einem internen Bericht noch in einem Schreiben an den Anspruchsteller als bereits vorliegend aufführen.

Die bloße Bezeichnung „Amtsfahrt“ reicht für die rechtliche Einordnung nicht aus. Die konkrete Dispositionsanweisung mit Baken, Warnleuchten und unmittelbarer Fahrt zur Absenkung liefert hier die zusätzlich benötigten Tatsachen. Für die Anspruchshöhe bleiben Vorschadenabgrenzung und Ersatzbedarf relevant. Bitte fragen Sie zur Ehefrau nur nach den betroffenen Zeitfenstern; eine umfassende Beschäftigten- oder Gesundheitsakte wird dafür nicht benötigt.

Wir haben 2.188,80 Euro als vorläufige Entschädigungsreserve erfasst. Das ist ein Bearbeitungswert und keine an Herrn Dinkel gezahlte Summe. Vor einem abschließenden Anerkenntnis stimmen wir die Ergebnisbewertung mit Ihnen ab. Bei einer Einigung kann die Zahlung an den Geschädigten im Rahmen des übernommenen Haftpflichtschutzes erfolgen; der heutige Brief ist noch kein Vergleich. Die Antwortfrist 12. Oktober bleibt im Kalender. Eine bloße interne Weiterleitung hemmt sie nicht und verlängert sie auch nicht von selbst.

Mit freundlichen Grüßen
Severin Salbei''', 'Severin Salbei <schaden@mainbogen-kommunal.example>', 'Kunigunde Färber <recht@lindenquell.example>', '2026-10-05T18:20:00+02:00'),
    ],
))

BATH = 'Lindenqueller Bäderbetrieb GmbH – Geschäftsführung\nSeerosenbogen 3, 97082 Lindenquell bei Würzburg'

CASES.append(dict(
    slug='akha-wuerzburg-schwimmbad', title='Rebhuhn: Betriebshaftpflicht und Betreiberrolle',
    summary='Die GmbH meldet den Leitermangel nach Eingang ihres Vertragsordners; Gesundheitsdaten, Sachprüfung und städtische Beteiligung werden sauber getrennt.',
    is_new=False, core='Privatrechtlicher Badvertrag, konkrete Wartungspflicht, begrenzter Personenschaden und Versicherung der Betreiber-GmbH.',
    notes='Fortsetzung am 05.10.2026 nach 16:30 Uhr. Fiktive Betriebshaftpflichtbedingungen werden erst jetzt im Briefwechsel dokumentiert. Die Stadt ist Gesellschafterin und nicht automatisch weitere Schuldnerin. Kein Kreis- oder Rückversichererfall bei diesem begrenzten Schaden. Die vorhandene Klage über 892,70 EUR bleibt unverändert und nicht eingereicht.',
    exhibits=[],
    attachments={
        '03_Betreiberin_Belegversand.eml': [FOLDER+'01_Betreiberin_Schadenanzeige.pdf', '02_Benutzungsordnung_und_Eintritt.docx', '03_Unfallmeldung.docx', '04_Kontrollbuch.docx'],
        '04_Versicherer_Datenabgrenzung.eml': [FOLDER+'02_Versicherer_Bestaetigung.pdf'],
    },
    documents=[
        letter('01_Betreiberin_Schadenanzeige.docx', 'Leiterunfall Rebhuhn: Schadenanzeige der Betreiberin', '''Sehr geehrter Herr Salbei,

wir melden den Vorfall vom 22. August, bei dem Frau Walburga Rebhuhn an der westlichen Beckenleiter verletzt wurde. Der vollständige Ordner unserer Betriebshaftpflicht wurde heute um 16:40 Uhr aus der Altregistratur geliefert. Die dortige Ausfertigung nennt unsere GmbH als Versicherungsnehmerin des Vertrags MK-BAD-2026. Frau Krens Mitteilung vom 2. Oktober über den damals noch fehlenden Vertrag war zutreffend und wird als historischer Aktenstand beibehalten.

Frau Rebhuhn verlangt inzwischen bestimmt 850,00 EUR Schmerzensgeld und 42,70 EUR Auslagen. Eine Klage liegt uns nicht vor. Der frühere Kurzvermerk „am Beckenrand ausgerutscht“ stammt vom Ersthelfer, der den Unfall nicht beobachtete. Die Klägerin beschreibt eine bewegliche Leiterstufe. Kontrollbuch und spätere technische Prüfung bestätigen eine lockere Befestigung; die Leiter war trotz des Eintrags um 07:35 Uhr zunächst nicht gesperrt worden. Wir möchten diese Tatsachen offenlegen, ohne aus jeder abweichenden Formulierung automatisch ein Anerkenntnis oder einen Täuschungsvorwurf abzuleiten.

Das Bad wird von unserer GmbH auf Grundlage privatrechtlicher Eintrittsverträge betrieben. Die Stadt ist alleinige Gesellschafterin, führt aber weder den Eintrittsvertrag noch die tägliche Wasseraufsicht im eigenen Namen. Bitte behandeln Sie die GmbH deshalb als mögliche Schuldnerin. Eine allgemeine Aufsichtsfunktion des Landkreises begründet für die mechanische Leiterbefestigung keinen eigenen Anspruch der Besucherin gegen ihn.

Wir übermitteln zunächst die Betriebs- und Unfallunterlagen. Den eingeschränkt zugänglichen Behandlungsbericht geben wir nur in dem Umfang weiter, der für die konkrete Prüfung erforderlich ist, über den geschützten Schadenkanal. Bitte benennen Sie die benötigten Informationen und den vorgesehenen Empfängerkreis. Einen Personenschaden mit lebenslangem Pflegebedarf haben wir nicht gemeldet. Eine Weitergabe an Rückversicherer oder andere Ausgleichsstellen ist daher nicht vorsorglich vorgesehen. Bis zum Abschluss Ihrer Prüfung sind weder eine Zahlung noch ein Vergleich zugesagt.

Mit freundlichen Grüßen
Fatima Fink
Geschäftsführerin''', BATH, INSURER),
        letter('02_Versicherer_Bestaetigung.docx', 'Rebhuhn: Deckungsbereich und sachliche Nachfragen', '''Sehr geehrte Frau Fink,

wir bestätigen den Eingang Ihrer Meldung unter MK-BAD-26222 und die vertragliche Zuordnung des Lindenbads zur Lindenqueller Bäderbetrieb GmbH. Nach der für diesen Vorgang maßgeblichen Fallvereinbarung MK-BAD-2026 besteht im Kalenderjahr 2026 Betriebshaftpflichtschutz für die gesetzliche Haftpflicht aus dem entgeltlichen Badbetrieb einschließlich der Verkehrssicherung und der notwendigen Instandhaltung von Einstiegen. Die vereinbarte Versicherungssumme für Personenschäden beträgt 5.000.000 EUR je Ereignis. Für diesen Personenschaden ist kein Selbstbehalt vorgesehen. Diese Angaben betreffen den Innenvertrag, nicht bereits die Haftungsentscheidung gegenüber Frau Rebhuhn.

Die medizinischen Unterlagen sollen sich zunächst auf die behauptete Schienbeinverletzung und deren Verlauf beschränken. Wir benötigen keine vollständige lebenslange Krankenakte. Eine pauschale Schweigepflichtentbindung ist nicht aus dem bloßen Besuch des Bads abzuleiten. Bitte dokumentieren Sie den erforderlichen Übermittlungszweck und nutzen Sie den vereinbarten geschützten Kanal. Die Zugangskontrolle in Ihrer Schadenakte bleibt bestehen.

Zur Haftungsprüfung sind der frühe Hinweis auf die wackelnde Stufe, die fehlende Sperrung und der tatsächliche Unfallablauf entscheidend. Bitte bewahren Sie das ausgetauschte Befestigungsteil weiter auf. Die widersprüchliche erste Kurzbeschreibung lässt sich durch die Aussage des Ersthelfers und der Zeugin aufklären. Für ein Rennen oder einen Sprung liegt nach den bisherigen Unterlagen keine eigene Wahrnehmung vor; darauf soll eine Ablehnung nicht ohne weitere Tatsachen gestützt werden.

Die Höhe des bestimmten Schmerzensgelds bleibt zu bewerten. Eine Reserve von 892,70 EUR ist lediglich unser aktueller Bearbeitungsansatz. Die Stadt als Gesellschafterin und der Landkreis werden dadurch nicht zu Mitschuldnern. Ein individueller Rückversicherungsvorgang ist bei diesem begrenzten, bisher folgenlos abgeheilten Ereignis nicht eröffnet. Die Vereinbarung und unser Brief sind Bestandteile dieses fiktiven Falls und belegen keine tatsächliche AKHA-Beteiligung. Bitte stimmen Sie eine abschließende Antwort mit uns ab, sobald die eng umgrenzte medizinische Klärung vorliegt.

Mit freundlichen Grüßen
Severin Salbei
Schadenabteilung''', INSURER, BATH),
        email('03_Betreiberin_Belegversand.eml', 'MK-BAD-26222: Betriebsunterlagen, Unfallmeldung und Kontrollbuch', '''Sehr geehrter Herr Salbei,

die beigefügte Schadenanzeige und die drei Betriebsunterlagen dokumentieren die Rollen und den Leiterbefund. Der Kontrollbucheintrag von 07:35 Uhr bleibt in seiner ursprünglichen Form erhalten. Wir ergänzen keine nachträgliche Sperrung, die damals nicht stattgefunden hat. Die Leiter wurde erst nach dem Unfall um 10:48 Uhr gesperrt und nach Reparatur um 11:35 Uhr wieder freigegeben.

Die Klägervertreterin verlangt bestimmt 850 Euro Schmerzensgeld und 42,70 Euro für Verbandmaterial und Taxi. Es geht nicht um eine Pflegekostenreserve. Der Ersthelfer Anselm Klee sah den Unfall nicht selbst; sein kurzer Text ist deshalb keine zuverlässige Grundlage für die Behauptung, die Besucherin sei gerannt. Die Bekannte Nwosu hat eine eigene Beobachtung geschildert. Herr Lerch kann die fehlende Sicherungsscheibe und die spätere Reparatur erklären.

Ich habe den Behandlungsbericht dieser normalen E-Mail bewusst nicht als Anlage beigefügt. Unsere separate Prüfung des erforderlichen Umfangs und Übermittlungswegs läuft. Bitte bestätigen Sie uns den vorgesehenen geschützten Schadenkanal und die zuständige Sachbearbeitung. Die Stadt erhält den allgemeinen Beteiligungsbericht ohne medizinische Einzelheiten. Sie ist nicht unsere Vertragspartnerin der Besucherin und soll auch nicht ohne konkrete Grundlage einen eigenen Anspruch des Landkreises anmelden.

Mit freundlichen Grüßen
Fatima Fink''', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', 'Severin Salbei <schaden@mainbogen-kommunal.example>', '2026-10-05T17:15:00+02:00'),
        email('04_Versicherer_Datenabgrenzung.eml', 'MK-BAD-26222: Enger Prüfbedarf statt vollständiger Krankenakte', '''Sehr geehrte Frau Fink,

anbei erhalten Sie unsere Bestätigung als PDF. Für die weitere Prüfung brauchen wir den Befund zur rechten Schienbeinverletzung, den dokumentierten Verlauf bis zur Kontrolle und die heute mitgeteilten verbliebenen Beschwerden. Andere Erkrankungen oder Behandlungen sind zunächst nicht erforderlich. Bitte klären Sie die rechtliche Grundlage der konkreten Übermittlung und übermitteln Sie die erforderlichen Ausschnitte im geschützten Kanal an die zuständige Personenschadensachbearbeitung.

Die Organisation Ihrer GmbH und die unterbliebene Sperrung werden unabhängig von der Versicherungsfrage geprüft. Ein Betriebsvertrag kann eine eigene Pflichtverletzung nicht in eine Verantwortung der Stadt umetikettieren. Umgekehrt führt unsere Deckungsbestätigung nicht automatisch dazu, dass jeder geforderte Betrag angemessen ist. Die Auslagen von 42,70 Euro sind einzeln belegt; beim Schmerzensgeld ist insbesondere die begrenzte Verletzung und der geschilderte Verlauf zu würdigen.

Bitte teilen Sie der Klägervertreterin mit, welche sachliche Rückfrage verbleibt, statt lediglich auf eine noch laufende Versicherungsprüfung zu verweisen. Wir haben weder eine Zahlung ausgeführt noch einen Vergleich genehmigt. Bei neuen konkreten Dauerfolgen wäre die Reserve neu zu prüfen. Bislang besteht kein Anlass für eine besondere Meldung an einen Rückversicherer oder für die Übermittlung der medizinischen Unterlagen an den Landkreis. Die vorhandenen Dokumente bleiben in Ihrer Akte unverändert erhalten.

Mit freundlichen Grüßen
Severin Salbei''', 'Severin Salbei <schaden@mainbogen-kommunal.example>', 'Fatima Fink <geschaeftsfuehrung@lindenbad.example>', '2026-10-05T18:25:00+02:00'),
    ],
))

CASES.append(dict(
    slug='akha-wuerzburg-baumpflege', title='Sesam: Stadtpflichten und Unternehmerregress',
    summary='Die Stadt meldet den Astkontakt; der Versicherer trennt eigene Absperrpflicht, technische Unternehmerleistung und den noch fehlenden Aufstellnachweis.',
    is_new=False, core='Begrenzte Freigabe, funktionelle Helferstellung, mögliche Dritthaftung und Regress ohne erfundene Gesamtschuld.',
    notes='Neue Vertragsangaben und Nachrichten vom späten 05.10.2026 ergänzen den zuvor offenen Archivstand. Alle neuen Versicherungsbedingungen sind reine Fallfiktion; keine automatische AKHA-Beteiligung. Der Aufstellnachweis bleibt weiterhin fehlend. Die ursprüngliche Klage über 3.011,40 EUR und die Frist 13.10.2026 bleiben unverändert.',
    exhibits=[],
    attachments={
        '03_Stadt_Versicherer_Belege.eml': [FOLDER+'01_Stadt_Schadenanzeige.pdf', '02_Arbeitsauftrag.docx', '03_Absperrvermerk.docx', '04_Ereignisbericht.docx'],
        '04_Versicherer_Regressfragen.eml': [FOLDER+'02_Versicherer_Pruefauftrag.pdf', '09_Unternehmen_Stellungnahme.eml'],
    },
    documents=[
        letter('01_Stadt_Schadenanzeige.docx', 'Kerbelring: Eigene Sicherungspflicht und Unternehmerleistung', '''Sehr geehrter Herr Salbei,

wir melden den Astkontakt vom 3. September am Kerbelring 18. Herr Leander Sesam verlangt 3.011,40 EUR für die bezahlte Reparatur und zwei Tage Ersatzwagen. Der Klägervertreterin wurde heute eine Zwischenantwort erteilt. Die erbetene Antwortfrist bis zum 13. Oktober bleibt offen. Eine Zahlung oder abschließende Anerkennung ist nicht erfolgt.

Um 16:45 Uhr ging die aktuelle Vertragsausfertigung aus unserem Archiv ein. Sie bestätigt für das Kalenderjahr 2026 unter MK-AH-LQ-2026 die gesetzliche Haftpflicht unserer Stadt aus Straßenunterhalt und zugehöriger Verkehrssicherung. Der Vorgang war zuvor nur über Beitragsunterlagen zugeordnet; deshalb enthielt Frau Krens Nachricht vom 2. Oktober noch keine belastbare Deckungsaussage. Bitte prüfen Sie jetzt die gemeldete Tätigkeit anhand der vollständigen Angaben und bestätigen Sie Ihre Schadenbearbeitung.

Unser Arbeitsauftrag teilte die Aufgaben auf: Die Stadt sollte Parkraum und Absperrung sichern und einzelne Arbeitsbereiche freigeben; Astwerk Amal Berg GmbH bestimmte Schnitt- und Seiltechnik. Herr Zwirn will nur den südlichen Bereich freigegeben haben. Der Vorarbeiter verstand den Zuruf weiter und begann trotz des sichtbaren Wagens mit der Entlastung. Wir möchten diese Spannung aufklären und nicht durch die pauschale Behauptung erledigen, sämtliche Verantwortung liege beim beauftragten Unternehmen.

Der tatsächliche Aufstellnachweis für das mobile Halteverbot fehlt weiterhin. Die Bestellung für den 31. August ist kein Nachweis des vollzogenen Aufbaus. Auch aus der Sichtbarkeit der Schilder am Unfallmorgen folgt noch nicht, wann der Wagenhalter sie erkennen konnte. Bitte setzen Sie deshalb keine feste Mitverschuldensquote ohne die fehlenden Tatsachen an.

Eine eigene Haftpflichtdeckung des Unternehmens ist noch nicht belegt. Dessen mögliche Haftung, eine funktionelle Helferstellung und eine denkbare interne Erstattung sind getrennt zu prüfen. Der Landkreis war weder Auftraggeber noch Bauleiter dieser örtlichen Straßenmaßnahme. Eine nur vorsorgliche Rückversichereranzeige bei der kleinen Einzelforderung ist aus unserer Sicht nicht veranlasst. Für die Außenkommunikation bleibt die Stadt zuständig.

Mit freundlichen Grüßen
Kunigunde Färber''', CITY, INSURER),
        letter('02_Versicherer_Pruefauftrag.docx', 'Sesam: Haftungsprüfung ohne voreilige Regresszuweisung', '''Sehr geehrte Frau Färber,

wir führen Ihre Meldung unter MK-AH-26-B47. Der von Ihnen vorgelegte Vertrag MK-AH-LQ-2026 erfasst die gesetzliche Haftpflicht der Stadt aus den genannten Straßenunterhaltungsaufgaben. Die im Fall vereinbarte Sachschadensumme beträgt 5.000.000 EUR je Ereignis; der Selbstbehalt beträgt 500 EUR. Eigene Ansprüche gegen beauftragte Unternehmen werden damit weder aufgehoben noch automatisch begründet. Eine eigenständige Versicherung der Astwerk Amal Berg GmbH wird durch den Vertrag der Stadt nicht nachgewiesen.

Für die Außenhaftung ist zunächst Ihre eigene Absperr- und Koordinationsleistung zu beurteilen. Die Frage, ob das Unternehmen bei dieser Aufgabe als Verwaltungshelfer tätig wurde, verlangt daneben eine funktionelle Betrachtung des konkreten Auftrags. Die technische Eigenverantwortung des Unternehmens und Ihre Vorgaben müssen hierzu zusammen gelesen werden. Es wäre voreilig, entweder jede Unternehmerhaftung auszuschließen oder den Geschädigten allein auf die Firma zu verweisen.

Bitte sichern Sie die getrennten Aussagen zu dem Zuruf um 08:10 Uhr. Das Tagesblatt „Beginn“ ersetzt keine eindeutige Bereichsfreigabe. Ebenso bleibt offen, ob die Schilder rechtzeitig aufgestellt wurden. Wir benötigen das noch fehlende Blatt oder, falls es nicht existiert, die konkrete Auskunft der damals eingesetzten Person. Eine nachträgliche Bestätigung des gewünschten Aufstelltags ohne eigene Wahrnehmung ist keine verlässliche Ergänzung.

Bei dem bezifferten Betrag von 3.011,40 EUR geht es um einen begrenzten Sachschaden. Wir haben diesen Betrag als vorläufige Außenreserve und den vertraglichen Selbstbehalt separat erfasst. Beides ist noch keine Regulierung oder Kürzung der Forderung des Herrn Sesam. Eine Rückversichererakte wird auf diesem Stand nicht eröffnet. Eine Zugehörigkeit zu AKHA oder einer anderen Ausgleichseinrichtung ist nicht aus dem Ordnernamen Ihrer Altregistratur abzuleiten.

Bitte veranlassen Sie vorerst keinen Forderungsverzicht gegenüber dem Unternehmen. Zugleich soll der Geschädigte nicht auf einen nur theoretischen Ersatzanspruch verwiesen werden. Falls ein Regress oder eine Beteiligung des Unternehmens später tragfähig wird, benötigen wir die tatsächlichen Befugnisse, die Vertragsgrundlagen und eine nachvollziehbare Kausalitätsbewertung. Die Antwortfrist 13. Oktober bleibt davon unberührt.

Mit freundlichen Grüßen
Severin Salbei''', INSURER, CITY),
        email('03_Stadt_Versicherer_Belege.eml', 'MK-AH-26-B47: Auftrag, Absperrvermerk und Unternehmensbericht', '''Sehr geehrter Herr Salbei,

beigefügt sind unsere heutige Schadenanzeige sowie die drei unveränderten Kernunterlagen. Die Abweichung zwischen Zwirns enger Freigabe und Königs Verständnis bleibt darin sichtbar. Wir haben den Unternehmensbericht nicht auf eine für uns günstigere Fassung umgeschrieben. Das Seil lief nach dessen Darstellung über eine Astgabel; die städtische Absperrung sollte den gefährdeten Bereich zuvor freihalten.

Der Aufstellnachweis ist auch nach der heutigen Nachfrage nicht eingegangen. Die Bestellung der Halteverbotsschilder bleibt lediglich eine Bestellung. Herr Sesam gibt an, den Wagen schon vorher abgestellt zu haben. Ob er bei pflichtgemäßer Aufmerksamkeit später hätte reagieren müssen, können wir ohne tatsächlichen Aufstellzeitpunkt und Zugangsmöglichkeit nicht abschließend beurteilen. Die Stadt hat nicht dokumentiert, dass der Wagen vor Schnittbeginn entfernt war; gerade er stand sichtbar noch in der mittleren Bucht.

Die neuen Versicherungsunterlagen wurden erst um 16:45 Uhr verfügbar. Unsere vorherige Antwort an die Klägervertreterin enthielt deshalb keine verbindliche Deckungsaussage. Bitte teilen Sie konkrete Nachforderungen bis zur sachlichen Antwort am 13. Oktober mit. Ich werde das Unternehmen gesondert um Angaben zu seiner eigenen Haftpflicht und den Zuständigkeiten bitten. Eine Zusage, dass wir es endgültig aus jeder Haftung entlassen, ist damit nicht verbunden.

Mit freundlichen Grüßen
Kunigunde Färber''', 'Kunigunde Färber <recht@lindenquell.example>', 'Severin Salbei <schaden@mainbogen-kommunal.example>', '2026-10-05T17:20:00+02:00'),
        email('04_Versicherer_Regressfragen.eml', 'MK-AH-26-B47: Offene Fragen zur Firma bleiben offen', '''Sehr geehrte Frau Färber,

Sie erhalten unsere heutige Prüfbestätigung und die uns übermittelte Stellungnahme des Unternehmens vom 29. September als Anlagen zurück, damit der Bezug eindeutig bleibt. Diese Stellungnahme benennt eine eigenverantwortliche Schnitttechnik, bestätigt aber keine vorhandene Haftpflichtversicherung. Bitte fordern Sie gegebenenfalls die konkrete Deckungsurkunde an; ein allgemeiner Satz „wir sind versichert“ würde die Frage nicht vollständig klären.

Für den Amtshaftungseinwand anderweitiger Ersatzmöglichkeit brauchen wir einen tatsächlich tragfähigen Anspruch und keinen bloßen Hinweis auf eine Firma am Einsatzort. Ebenso darf eine Verwaltungshelferwertung nicht allein aus dem Wort „Auftrag“ abgeleitet werden. Der vorliegende Arbeitsauftrag verbindet städtische Bereichsvorgaben mit eigener technischer Durchführung. Die tatsächliche Weisungsdichte und der konkrete Fehler sind deshalb fallbezogen zu bewerten.

Der Selbstbehalt von 500 Euro bleibt Ihre interne Angelegenheit und wird nicht als Kürzung vom Reparatur- oder Mietwagenbeleg kommuniziert. Wir haben keine Zahlung freigegeben und keinen Vergleich geschlossen. Ein möglicher Unternehmerregress wird gesondert vorbereitet, ohne dass Herr Sesam eine unbestimmte dritte Stelle suchen muss. Die sichere Aufbewahrung des Tagesblatts und der Originalberichte bleibt vorrangig. Bitte lassen Sie neue Erinnerungsvermerke mit Erstellungsdatum versehen, statt eine fehlende Freigabeskizze nachträglich als damaliges Original erscheinen zu lassen.

Mit freundlichen Grüßen
Severin Salbei''', 'Severin Salbei <schaden@mainbogen-kommunal.example>', 'Kunigunde Färber <recht@lindenquell.example>', '2026-10-05T18:30:00+02:00'),
    ],
))

CASES.append(dict(
    slug='akha-wuerzburg-schlagloch', title='Oliveira: Meldungsorganisation und abgegrenzter Altschaden',
    summary='Stadt und Versicherer klären den Bearbeitungsweg der Bürgermeldung, ohne aus dem Folgetagsmaß einen Unfallbefund zu machen oder den alten Reifen erneut zu verlangen.',
    is_new=False, core='Straßenverkehrssicherung, konkrete Reaktionsmöglichkeit, Vorschäden und begrenzte Beweisbasis.',
    notes='Zusatzschriften erst am späten 05.10.2026; offene Tatsachen werden nicht nachträglich geschlossen. Die modellhaften Vertragsangaben sind reine Fallfiktion und keine tatsächlichen AKHA-Bedingungen. Der bestehende Entwurf bleibt bei 741,50 EUR; ein Kreis- oder Rückversichereranspruch wird nicht künstlich erzeugt.',
    exhibits=[],
    attachments={
        '03_Stadt_Versicherer_Service.eml': [FOLDER+'01_Stadt_Schadenanzeige.pdf', '03_Strasse_und_Kontrollen.docx', '04_Meldung_und_Reparatur.docx', '05_Werkstattbefund.docx'],
        '04_Versicherer_Beweisstand.eml': [FOLDER+'02_Versicherer_Pruefantwort.pdf', 'schriftverkehr-und-klage/02_Ergaenzende_Auskunft.eml'],
    },
    documents=[
        letter('01_Stadt_Schadenanzeige.docx', 'Hagebuttenweg: Schadenanzeige und Grenzen des Meldebefunds', '''Sehr geehrter Herr Salbei,

wir melden die Forderung des Herrn Celestino Oliveira wegen des Fahrbahnausbruchs am Hagebuttenweg. Die heute um 16:45 Uhr aus dem Archiv übermittelte Ausfertigung MK-AH-LQ-2026 ordnet den örtlichen Straßenunterhalt dem kommunalen Haftpflichtvertrag zu. Der bisherige Schriftwechsel über fehlende Vertragsbedingungen bleibt als damaliger Stand richtig. Erst mit den heutigen Unterlagen können wir den Vorgang vollständig zur Deckungsprüfung vorlegen.

Die Forderung wurde auf 741,50 EUR begrenzt. Eingeklagt werden sollen 499,80 EUR für die Felge, 59,50 EUR für die Achsprüfung und 182,20 EUR für das Abschleppen. Der schon im Juli beanstandete Reifen und dessen Montage bleiben mit zusammen 178,50 EUR ausdrücklich außerhalb dieses Entwurfs. Wir wollen den Vorschaden gleichwohl für die technische Ursache des Druckverlusts und des Abschleppbedarfs getrennt prüfen lassen. Eine rein rechnerische Kürzung ersetzt diese Kausalitätsfrage nicht.

Die Bürgermeldung ging am 8. September um 16:42 Uhr ein und wurde erst am 9. September um 07:18 Uhr geöffnet. Der behauptete Unfall lag dazwischen, um 06:50 Uhr. Die Mitteilung enthielt weder Maße noch Foto. Die acht Zentimeter Tiefe wurden am 10. September festgestellt; sie sind kein eigener Messwert vom Unfallmorgen. Ob vor dem Unfall ein zeitgerechtes Tätigwerden möglich und geboten war, hängt deshalb sowohl von der damaligen Gefahr als auch von der konkreten Organisation unseres Meldesystems ab.

Die Straße steht in städtischer Baulast. Der Landkreis unterhält den Hagebuttenweg nicht und erhält keine operative Weiterleitung sämtlicher Serviceformulare. Eine zusätzliche Haftung aus unserer bloßen Kreisangehörigkeit wird nicht behauptet. Bitte beurteilen Sie Kontroll- und Reaktionspflicht anhand dieses Straßenabschnitts, nicht mit einem abstrakten täglich geltenden Kontrollrhythmus.

Wir haben um Beweissicherung bei der Werkstatt gebeten. Die Frist der Klägerseite bis zum 14. Oktober bleibt offen. Weder einen Vergleich noch eine pauschale Anerkennung haben wir abgegeben. Die Meldung dient der geordneten Sachprüfung und darf nicht mit einer Zusage über Versicherung oder Rückdeckung gegenüber Herrn Oliveira verwechselt werden.

Mit freundlichen Grüßen
Kunigunde Färber''', CITY, INSURER),
        letter('02_Versicherer_Pruefantwort.docx', 'Oliveira: Konkrete Reaktionspflicht statt rückwirkender Gewissheit', '''Sehr geehrte Frau Färber,

wir bestätigen die Bearbeitung unter MK-AH-26-H24. Nach dem Vertrag MK-AH-LQ-2026 ist die gesetzliche Haftpflicht der Stadt aus Straßenunterhalt und Verkehrssicherung für das Kalenderjahr 2026 erfasst. Für Sachschäden sind im Szenario 5.000.000 EUR je Ereignis und ein Selbstbehalt von 500 EUR vereinbart. Prüfung, Abwehr und Befriedigung richten sich nach der tatsächlich begründeten Außenforderung. Der Selbstbehalt liefert weder einen Einwand des Geschädigten gegen den Vertrag noch einen pauschalen Kürzungsgrund gegen dessen Haftungsanspruch.

Bitte klären Sie, wer am 8. September nach Ende der Außendienstschicht für dringende Hinweise erreichbar war und wie das Serviceformular gegenüber Bürgern beschrieben wurde. Eine regelmäßig erst morgens gelesene allgemeine Eingangsbox und eine als ständig überwacht beworbene Gefahrenmeldestelle wären unterschiedlich zu bewerten. Bisher liegt zu dieser konkreten Ausgestaltung kein hinreichender Beleg vor. Wir werden deshalb aus dem elektronischen Eingangszeitpunkt nicht automatisch gesicherte tatsächliche Kenntnis aller diensthabenden Kräfte ableiten.

Der Wortlaut der Meldung spricht von einer aufbrechenden Flickstelle und einem Ausweichmanöver beim Radfahren. Er begründet konkreten Prüfbedarf, beantwortet aber nicht von selbst Dringlichkeit, Größe und Erkennbarkeit am Unfallmorgen. Die spätere Vermessung und Frau Pflaums Ergänzung sind mit ihren jeweiligen Wahrnehmungszeiten zu verwenden. Den ungesicherten Zustand am 9. September dürfen wir weder verharmlosen noch mit einer Messung vom Folgetag gleichsetzen.

Zur Kausalität ist der alte Seitenwandschnitt getrennt von der frischen Felgenverformung zu behandeln. Die Selbstangabe von 30 bis 35 km/h bleibt sichtbar; eine feste Mitverschuldensquote ohne technische und örtliche Einordnung setzen wir nicht an. Die Werkstatt soll Reifen und Felge bis zur abgeschlossenen Abstimmung aufbewahren.

Wir haben vorläufig 741,50 EUR als Außenreserve erfasst. Eine Zahlung oder Vergleichsvollmacht gegenüber dem Bürger ist damit nicht verbunden. Eine besondere Rückversicherungsmeldung und eine Beteiligung des Landkreises sind nach dem jetzigen Einzelfallstand nicht veranlasst. Bitte halten Sie den Antworttermin 14. Oktober ein und teilen Sie konkrete noch offene Fragen mit.

Mit freundlichen Grüßen
Severin Salbei''', INSURER, CITY),
        email('03_Stadt_Versicherer_Service.eml', 'MK-AH-26-H24: Serviceablauf und unveränderte technische Unterlagen', '''Sehr geehrter Herr Salbei,

ich übersende die heutige Anzeige, das Straßenblatt, die Servicemeldung mit Reparaturbericht und den Werkstattbefund. Die Unterlagen bleiben unverändert. Unsere Servicezentrale sucht die im September gültige Beschreibung des Meldeformulars und die zugehörige Dienstanweisung. Diese Unterlagen liegen heute noch nicht vor. Es wäre deshalb falsch, bereits eine lückenlose abendliche Überwachung oder deren zulässigen vollständigen Ausschluss zu behaupten.

Der Ausbruch wurde erst am 10. September vermessen. Frau Pflaums frühere Wahrnehmung und ihre heutige Ergänzung können für den zeitlichen Verlauf wichtig sein, geben aber keine eigene Tiefenmessung für den Unfallmorgen her. Die Klägerseite kennt diese Einschränkung. Die ursprünglichen 920 Euro sind außerdem nicht mehr der Streitbetrag des vorbereiteten Entwurfs. Der alte Reifen und dessen Montage wurden herausgenommen; zu Felge, Achsprüfung und Abschleppen bleiben 741,50 Euro.

Bitte prüfen Sie insbesondere, ob trotz dieser Abgrenzung ein Teil des Abschleppbedarfs auf den früheren Reifenbefund zurückgehen könnte. Die Werkstatt kann eine technische Einschätzung abgeben, hat aber den Fahrbahnkontakt nicht gesehen. Wir haben das Unternehmen um weitere Aufbewahrung gebeten. Der Landkreis betreibt weder unser Serviceportal noch diesen Straßenabschnitt. Eine Weiterleitung dorthin würde die Sachfragen nicht lösen und ersetzt unsere eigene Antwort bis zum 14. Oktober nicht.

Mit freundlichen Grüßen
Kunigunde Färber''', 'Kunigunde Färber <recht@lindenquell.example>', 'Severin Salbei <schaden@mainbogen-kommunal.example>', '2026-10-05T17:25:00+02:00'),
        email('04_Versicherer_Beweisstand.eml', 'MK-AH-26-H24: Bitte Wahrnehmungszeiten und Schadenposten trennen', '''Sehr geehrte Frau Färber,

beigefügt sind unsere schriftliche Prüfantwort und die ergänzende Auskunft der Anwohnerin aus der bisherigen Akte. Die letztere bleibt eine Zeugenschilderung mit begrenztem zeitlichem Blick. Sie ersetzt keine Messung am 9. September um 06:50 Uhr. Bitte kennzeichnen Sie in Ihrer Antwort genau, welche Aussage vor dem Unfall beobachtet wurde und welche erst danach hinzukam.

Der fehlende Dienstplan muss nachgefordert werden, ohne ihn nachträglich passend zu schreiben. Für die Amtshaftung interessieren die konkrete Gefahr und die damals zumutbare Organisation. Ein interner Zweiwochenplan ist weder automatisch ausreichend noch für sich schon ein Pflichtverstoß. Ebenso kann der elektronische Zugang einer unspezifischen Meldung unterschiedliche Reaktionsfragen auslösen, je nachdem, wie die Annahme organisiert und nach außen dargestellt war.

Die Anspruchsbegrenzung auf 741,50 Euro ist nachvollziehbar gerechnet. Damit steht die rechtliche Erforderlichkeit jeder Position noch nicht fest. Beim Abschleppen brauchen wir die konkrete Nichtfahrbereitschaft nach dem Stoß und die Abgrenzung zum alten Reifenriss; eine doppelte Kürzung derselben Position wäre zu vermeiden. Ein neu hinzugekommener Zahlungsbeleg liegt uns nicht vor. Die eingestellte Reserve ist nicht als Zahlung zu verbuchen. Wir eröffnen auf diesem Stand keine Rückversichererakte und keine Forderung gegen den Landkreis.

Mit freundlichen Grüßen
Severin Salbei''', 'Severin Salbei <schaden@mainbogen-kommunal.example>', 'Kunigunde Färber <recht@lindenquell.example>', '2026-10-05T18:35:00+02:00'),
    ],
))
