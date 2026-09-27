"""Fiktive Erwerbsurkunden und Freistellungsbelege. Autor: Klotzkette."""
from __future__ import annotations
import json
from datetime import date
from bauwirtschaft_hildesheim_common import ROOT, CASE, ACTORS, REF, euro, build_records

RECORDS = []
PROPERTY = 'Grundbuch von Hildesheim Blatt 88018, Bestandsverzeichnis Nummer 1, Gemarkung Hildesheim, Flur 88, Flurstück 18/6, Gebäude- und Freifläche Wohnhof Am Steinbogen 18, Größe 1.300 m²'
CONTRACTORS = ['rohbau', 'huelle', 'hls', 'elektro', 'ausbau', 'aufzug', 'aussen', 'versorger']


def add(n, name, dt, issuer, title, sections, recipient='bauherr', **extra):
    d = dict(number=n, filename=f'{n:03d}_{name}.pdf', date=dt, issuer=issuer,
             recipient=recipient, title=title, sections=sections, **extra)
    RECORDS.append(d)
    return d


def taxid(actor):
    return '30/145/' + str(12000 + list(ACTORS).index(actor) * 113)


def documents():
    RECORDS.clear()
    add(149, 'Grundstueckskaufvertrag_UVZ_118_2026', '2026-11-03', 'notar',
        'Grundstückskaufvertrag UVZ 118 2026', [
        'Verhandelt zu Hildesheim am 3. November 2026 vor mir, Dr. Carla Fink, Notarin mit dem Amtssitz Hildesheim. Die nachfolgende Niederschrift wird in Urschrift aufgenommen. Die Beteiligten sind der Notarin aus den vorgelegten gültigen Lichtbildausweisen bekannt; die Vertretungsbefugnisse wurden anhand der vorgelegten Registerunterlagen festgestellt.',
        ('h', '1 Erschienene und Vertretung'),
        'Es erscheinen Herr Nils Kamm, handelnd als einzelvertretungsberechtigter Geschäftsführer der Leinequartier Grundstücksverwaltung GmbH mit Sitz in Hildesheim, geschäftsansässig Grundstückshof 31, 31134 Hildesheim, als Verkäuferin, und Frau Maren Birk, handelnd als einzelvertretungsberechtigte Geschäftsführerin der Steinbogen Wohnen GmbH mit Sitz in Hildesheim, geschäftsansässig Wohnhof Am Steinbogen 18, 31134 Hildesheim, als Käuferin. Beide Gesellschaften handeln im eigenen Namen und für eigene Rechnung. Die Erschienenen erklären, dass die für diesen Erwerb erforderlichen gesellschaftsinternen Zustimmungen vorliegen.',
        ('h', '2 Grundstück und Kaufgegenstand'),
        'Die Verkäuferin ist im nachstehend bezeichneten Grundbuch als alleinige Eigentümerin eingetragen: ' + PROPERTY + '. Die Notarin hat das Grundbuch am 3. November 2026 elektronisch eingesehen. Abteilung II und Abteilung III enthalten keine Eintragungen. Offene Eintragungsanträge wurden bei der Einsicht nicht mitgeteilt. Die Verkäuferin erklärt, seitdem keine Verfügungen über das Grundstück getroffen zu haben.',
        'Die Verkäuferin verkauft dieses Grundstück mit allen wesentlichen Bestandteilen und dem ihr gehörenden Zubehör an die Käuferin zu Alleineigentum. Das Grundstück ist unbebaut und unvermietet. Bewegliche Gegenstände werden nicht gesondert verkauft. Die Käuferin plant den Neubau eines Wohngebäudes mit acht Mietwohnungen. Die Verkäuferin übernimmt weder Planungs- noch Bauleistungen und hat keinen Einfluss auf deren spätere Beauftragung.',
        ('page',),
        ('h', '3 Kaufpreis und Fälligkeitsvoraussetzungen'),
        'Der Kaufpreis beträgt 450.000,00 EUR, in Worten vierhundertfünfzigtausend Euro. Die Parteien vereinbaren keine Option zur Umsatzsteuer. Der Kaufpreis ist ohne Abzug binnen vierzehn Kalendertagen nach Zugang der schriftlichen Fälligkeitsmitteilung der Notarin zu zahlen, frühestens am 30. November 2026; eine frühere Zahlung nach Zugang der Mitteilung ist gestattet. Die Käuferin zahlt unmittelbar auf das auf die Verkäuferin lautende Erwerbskonto bei der Leinebogen Projektbank AG, bankinterne Kontokennung LQ-ERWERB-01. Die dem Käufer bereits übergebene Zahlungsanweisung der Verkäuferin ist vor Zahlungsfreigabe anhand der bekannten Ansprechpartnerin der Bank abzugleichen. Ein Notaranderkonto wird nicht eingerichtet.',
        'Die Notarin soll die Fälligkeit erst mitteilen, wenn die Vormerkung zugunsten der Käuferin im vereinbarten lastenfreien Rang eingetragen ist und das Zeugnis der zuständigen Gemeinde über das Nichtbestehen oder die Nichtausübung eines gesetzlichen Vorkaufsrechts vorliegt. Die Käuferin benötigt keine Finanzierungsgrundschuld vor Eigentumsumschreibung. Weitere Genehmigungen oder die Ablösung von Verkäufergrundpfandrechten sind nach den Erklärungen und Unterlagen der Beteiligten nicht erforderlich. Ergibt sich bei der Abwicklung ein entgegenstehendes Hindernis, wird die Fälligkeit bis zu dessen Beseitigung nicht mitgeteilt.',
        'Die Käuferin weist die unbare Zahlung durch Kontoauszug nach; die Verkäuferin bestätigt den vollständigen Eingang. Die Notarin hat über die gesetzlichen Beschränkungen der Gegenleistung beim Immobilienerwerb und die erforderlichen Nachweise belehrt. Bargeld, Kryptowerte, Gold, Platin und Edelsteine werden nicht zur Erfüllung verwendet. Die Käuferin darf Zahlungen nur auf eine auf die Verkäuferin lautende, verifizierte Bankverbindung leisten.',
        ('h', '4 Besitz Nutzen Lasten und Erschließung'),
        'Besitz, Nutzungen, Gefahr und Verkehrssicherungspflichten gehen am Tag nach vollständigem Kaufpreiseingang auf die Käuferin über. Die Verkäuferin übergibt das Grundstück geräumt und frei von schuldrechtlichen Nutzungsrechten Dritter. Bis zum Übergang trägt sie die laufenden öffentlichen und privaten Lasten. Die Parteien erstellen ein Übergabeprotokoll; ein vorgreiflicher Zutritt zu Vermessungs- und Untersuchungszwecken bedarf ihrer gesonderten Abstimmung.',
        'Die Verkäuferin trägt Erschließungs- und sonstige Anliegerbeiträge für Anlagen, deren beitragspflichtige Herstellung oder Verbesserung bei Vertragsschluss abgeschlossen ist, unabhängig vom Zeitpunkt der Bescheiderteilung. Für später begonnene oder abgeschlossene Maßnahmen trägt die Käuferin die auf das Grundstück entfallenden Beiträge. Hausanschlüsse für das Neubauvorhaben und von der Käuferin beauftragte Grundstücksarbeiten gehen zu ihren Lasten. Eine Zusage bestimmter Anschlusskosten oder der sofortigen Bebaubarkeit wird nicht erteilt.',
        ('page',),
        ('h', '5 Beschaffenheit Rechtsmängel und Verantwortung'),
        'Die Käuferin kennt das Grundstück aus Besichtigung und den ihr übergebenen Unterlagen. Die Verkäuferin erklärt, dass ihr keine Altlasten, schädlichen Bodenveränderungen, Kampfmittelbelastungen, unterirdischen Anlagen oder außerhalb des Grundbuchs begründeten Rechte Dritter bekannt sind. Sie hat das Grundstück nicht selbst gewerblich genutzt. Diese Wissenserklärung ersetzt keine Bodenuntersuchung und ist keine Garantie für eine bestimmte Gründungsart oder Tragfähigkeit.',
        'Die Verkäuferin schuldet die Übertragung frei von eingetragenen und von ihr begründeten nicht übernommenen Rechten Dritter. Sachmängelrechte der Käuferin werden im Übrigen ausgeschlossen; dies gilt nicht bei arglistigem Verschweigen, ausdrücklich übernommener Garantie, vorsätzlicher oder grob fahrlässiger Pflichtverletzung sowie bei Verletzung von Leben, Körper oder Gesundheit. Für Rechtsmängel gelten die gesetzlichen Bestimmungen. Die Käuferin trägt das Risiko der baurechtlichen Zulässigkeit ihres Vorhabens, soweit die Verkäuferin keine unrichtigen Angaben vorsätzlich oder arglistig macht.',
        'Die Notarin hat darauf hingewiesen, dass sie keine technische Baugrund- oder Wirtschaftlichkeitsprüfung vornimmt und der beabsichtigte Neubau einer eigenen öffentlich-rechtlichen Prüfung bedarf. Die Flächenangabe wird dem Bestandsverzeichnis entnommen; Kaufgegenstand ist das Grundstück innerhalb seiner rechtlichen Grenzen. Eine Teilflächenveräußerung oder Grundstücksteilung ist nicht vereinbart.',
        ('h', '6 Auflassung Vormerkung und Grundbuchvollzug'),
        'Die Beteiligten sind darüber einig, dass das Eigentum an dem in Ziffer 2 bezeichneten Grundstück auf die Steinbogen Wohnen GmbH übergeht. Sie erklären die Auflassung unbedingt. Die Verkäuferin bewilligt und die Käuferin beantragt zur Sicherung des Anspruchs auf Eigentumsübertragung die Eintragung einer Auflassungsvormerkung zugunsten der Käuferin an rangbereiter Stelle. Die Käuferin bewilligt deren Löschung bei ihrer Eigentumseintragung, sofern keine zwischenzeitlichen Eintragungen ohne ihre Zustimmung bestehen bleiben.',
        'Die Notarin soll den Antrag auf Eigentumsumschreibung erst einreichen, wenn der vollständige Kaufpreiseingang unbar nachgewiesen ist und die steuerliche Unbedenklichkeitsbescheinigung vorliegt. Bis dahin darf sie keine Ausfertigung oder beglaubigte Abschrift herausgeben, die ohne diese Vollzugssperre die Eigentumsumschreibung ermöglicht. Die Erschienenen bevollmächtigen die Notarin und ihre amtliche Vertretung, die zur vereinbarten Abwicklung erforderlichen Anträge getrennt oder beschränkt zu stellen und zu berichtigen, soweit dadurch der wirtschaftliche Vertragsinhalt nicht verändert wird.',
        ('page',),
        ('h', '7 Vollzugsauftrag Kosten und Ausfertigungen'),
        'Die Notarin wird mit der Anforderung und Prüfung des kommunalen Negativzeugnisses, der Überwachung der Fälligkeitsvoraussetzungen, der Fälligkeitsmitteilung und dem vertragsgemäßen Grundbuchvollzug einschließlich elektronisch strukturierter Antragsdaten beauftragt. Die Erwerberin trägt die Kosten dieser Urkunde, ihres Vollzugs, der Vormerkung und Eigentumsumschreibung sowie die Grunderwerbsteuer. Jede Partei trägt die Kosten einer von ihr gesondert beauftragten Beratung selbst. Kosten für die Löschung von Verkäuferbelastungen fallen nach dem festgestellten Grundbuchstand nicht an.',
        'Die Beteiligten bestätigen, dass keine Nebenabreden über zusätzliche Kaufpreisbestandteile oder eine Bindung an bestimmte Bauunternehmen bestehen. Der Maklervertrag der Käuferin mit Wohnfeld Grundstücke GmbH ist nicht Gegenstand einer eigenen Vergütungszusage in dieser Urkunde. Die Notarin hat über die gesamtschuldnerische Außenhaftung für Steuern und Kosten sowie darüber belehrt, dass der Eigentumserwerb erst durch Eintragung eintritt.',
        'Die Notarin belehrt über die rechtliche Tragweite der Vormerkung, des Lastenübergangs und der Auflassung. Änderungen und Ergänzungen dieses Kaufvertrags bedürfen der gesetzlich vorgesehenen Form. Eine unwirksame Einzelregelung lässt den Vertrag nur soweit bestehen, wie dies dem Gesetz und dem übereinstimmenden Parteiwillen entspricht; eine automatische Ersetzung durch eine beliebige wirtschaftlich ähnliche Regelung wird nicht vereinbart.',
        ('h', '8 Abschluss der Niederschrift'),
        'Diese Niederschrift wurde den Erschienenen von der Notarin vollständig vorgelesen, von ihnen genehmigt und sodann eigenhändig unterschrieben. Gez. Nils Kamm für die Leinequartier Grundstücksverwaltung GmbH. Gez. Maren Birk für die Steinbogen Wohnen GmbH. Gez. Dr. Carla Fink, Notarin.',
        'Ausfertigungs- und Versandvermerk der Geschäftsstelle: Die für die Beteiligten, Behörden und den Vollzug angeforderten S/W-Ausfertigungen und Abschriften einschließlich der maßgeblichen Vollzugsmitteilungen ergeben insgesamt 60 abgegebene Seiten. Die Urschrift verbleibt in der notariellen Verwahrung; die elektronische Fassung wird in der elektronischen Urkundensammlung verwahrt. Der Urkundsinhalt wird mit diesem Versandvermerk nicht geändert.',
        ], signer='Dr. Carla Fink, Notarin · Übereinstimmung der Abschrift mit der Urschrift bestätigt')

    add(170, 'Grundschuldbestellung_UVZ_139_2026', '2026-12-19', 'notar',
        'Grundschuldbestellung UVZ 139 2026', [
        'Verhandelt zu Hildesheim am 19. Dezember 2026 vor Dr. Carla Fink, Notarin mit Amtssitz Hildesheim. Erschienen ist Maren Birk, handelnd als einzelvertretungsberechtigte Geschäftsführerin der Steinbogen Wohnen GmbH, Wohnhof Am Steinbogen 18, 31134 Hildesheim. Identität und Vertretungsbefugnis wurden anhand der vorgelegten Ausweis- und Registerunterlagen festgestellt. Die Gesellschaft handelt als Grundstückseigentümerin und als Darlehensnehmerin. Eine persönliche Verpflichtung von Frau Birk im eigenen Namen ist nicht Gegenstand dieser Urkunde.',
        ('h', '1 Grundbuch und Gläubigerin'),
        'Belastet wird: ' + PROPERTY + '. Die Notarin hat das Grundbuch am 19. Dezember 2026 elektronisch eingesehen. Die Steinbogen Wohnen GmbH ist seit 18. Dezember 2026 als Eigentümerin eingetragen. Die beim Erwerb eingetragene Auflassungsvormerkung ist gelöscht; Abteilungen II und III sind unbelastet. Begünstigte Gläubigerin ist die Leinebogen Projektbank AG mit Sitz Hildesheim, Bankhof 4, 31134 Hildesheim.',
        ('h', '2 Bestellung und Rang'),
        'Die Eigentümerin bestellt zugunsten der Gläubigerin eine Buchgrundschuld in Höhe von 1.600.000,00 EUR, in Worten eine Million sechshunderttausend Euro, nebst 15 Prozent jährlichen Grundschuldzinsen seit dem 19. Dezember 2026 und einer einmaligen Nebenleistung von 5 Prozent des Grundschuldkapitals. Ein Grundschuldbrief wird ausgeschlossen. Das Recht soll die erste Rangstelle in Abteilung III erhalten; ihm sollen keine Rechte in Abteilung II vorgehen. Die Eigentümerin bewilligt und beantragt die entsprechende Eintragung.',
        'Die dinglichen Zinsen und die Nebenleistung erweitern den Sicherungsrahmen. Sie sind nicht mit dem vertraglich vereinbarten Darlehenszins von 3,60 Prozent gleichzusetzen und begründen im Innenverhältnis keinen Anspruch auf eine zusätzliche laufende Darlehensvergütung. Das Grundschuldkapital wird erst nach Kündigung mit einer Frist von sechs Monaten fällig. Die zwingenden Grenzen des § 1193 BGB für eine Sicherungsgrundschuld bleiben bestehen.',
        ('page',),
        ('h', '3 Dingliche Vollstreckungsunterwerfung'),
        'Die Eigentümerin unterwirft sich wegen des Grundschuldkapitals, der bezeichneten Grundschuldzinsen und der einmaligen Nebenleistung der sofortigen Zwangsvollstreckung aus dieser Urkunde in das belastete Grundstück in der Weise, dass die Vollstreckung gegen den jeweiligen Eigentümer zulässig sein soll. Die Eigentümerin bewilligt und beantragt die Eintragung dieser Unterwerfung gemäß § 800 ZPO. Die Bezeichnung als sofortige Unterwerfung hebt die gesetzlichen Voraussetzungen der Fälligkeit, Kündigung, Klauselerteilung und Zustellung nicht auf.',
        ('h', '4 Persönliches Schuldversprechen der Gesellschaft'),
        'Die Steinbogen Wohnen GmbH übernimmt gegenüber der Gläubigerin zusätzlich die persönliche Haftung für einen Betrag von 1.600.000,00 EUR nebst den in Ziffer 2 bezeichneten Zinsen und der Nebenleistung. Sie unterwirft sich insoweit der sofortigen Zwangsvollstreckung aus dieser Urkunde in ihr gesamtes Vermögen gemäß § 794 Absatz 1 Nummer 5 ZPO. Die Gläubigerin darf aus persönlicher Haftung und Grundschuld zusammen nur einmal Befriedigung verlangen. Die Sicherungszweckbeschränkung und die darin geregelten Voraussetzungen einer Verwertung gelten auch für dieses Schuldversprechen.',
        'Die Notarin hat erläutert, dass die vollstreckbare Urkunde eine gerichtliche Klage über die titulierten Ansprüche ersetzen kann und Einwendungen gegebenenfalls mit den vorgesehenen Rechtsbehelfen geltend zu machen sind. Vollstreckbare Ausfertigungen sind nur unter Beachtung der gesetzlichen Voraussetzungen zu erteilen. Die Eigentümerin erhält eine beglaubigte Abschrift; eine weitere vollstreckbare Ausfertigung unterliegt den gesetzlichen Beschränkungen.',
        ('h', '5 Sicherungszweck und Freigabe'),
        'Die Eigentümerin bestätigt die mit der Bank gesondert vereinbarte enge Sicherungsabrede: Grundschuld und persönliches Schuldversprechen sichern ausschließlich die Ansprüche der Leinebogen Projektbank AG aus dem am 19. Dezember 2026 geschlossenen Projektdarlehen SW-HI-26-08 über 1.600.000,00 EUR einschließlich seiner wirksam vereinbarten Nebenforderungen. Forderungen gegen Dritte oder aus anderen Bankverbindungen werden nicht erfasst. Eine Verwertung setzt voraus, dass eine gesicherte Forderung fällig und unbeglichen ist und die gesetzlichen sowie vertraglichen Voraussetzungen vorliegen.',
        'Nach vollständiger Erfüllung der gesicherten Ansprüche und Wegfall des Sicherungszwecks hat die Bank die Sicherheit nach Wahl der Eigentümerin durch Löschungsbewilligung oder Rückabtretung freizugeben. Bei dauerhaftem Missverhältnis zwischen Sicherungswert und gesicherten Forderungen bestehen die vertraglich und gesetzlich vorgesehenen Freigabeansprüche. Die enge Sicherungsabrede liegt der Bank und der Eigentümerin in gleichlautender, unterzeichneter Fassung vor.',
        ('page',),
        ('h', '6 Grundbuchanträge und Empfangsvollmacht'),
        'Die Notarin wird beauftragt, die Eintragung der Grundschuld und der Vollstreckungsunterwerfung unter Erstellung der erforderlichen strukturierten Daten zu beantragen. Die Gläubigerin hat die Notarin mit gesonderter schriftlicher Vollmacht bevollmächtigt, die dingliche Einigungserklärung der Eigentümerin für sie entgegenzunehmen. Die Entgegennahme wird außerhalb dieser Beurkundungsverhandlung gesondert erklärt und dokumentiert. Die Vollmacht berechtigt nicht dazu, den Sicherungszweck zu erweitern oder zusätzliche Forderungen anzuerkennen.',
        'Die Gesellschaft trägt die Kosten dieser Urkunde, der gesetzlich vergütungspflichtigen Betreuung, der Eintragung und der vereinbarten Ausfertigungen. Es bestehen keine zusätzlichen Treuhandauflagen, keine Rangbeschaffung durch Ablösung fremder Rechte und kein Verwahrungsauftrag für Geld. Die Notarin soll der Bank den Eintragungsstand mitteilen; eine gesonderte Rangbescheinigung wird nicht beauftragt.',
        ('h', '7 Abschluss der Niederschrift'),
        'Der Inhalt wurde der Erschienenen vollständig vorgelesen, von ihr genehmigt und eigenhändig unterschrieben. Gez. Maren Birk für die Steinbogen Wohnen GmbH. Gez. Dr. Carla Fink, Notarin. Die vorstehende Grundschuldbestellung ist Bestandteil der getrennt geführten Finanzierungsakte zum Darlehen vom 19. Dezember 2026.',
        ('h', '8 Gesonderter Empfangsvermerk vom 22 Dezember 2026'),
        'Aufgrund der schriftlich erteilten Empfangsvollmacht nehme ich, Dr. Carla Fink, am 22. Dezember 2026 um 10:15 Uhr die in der Urkunde vom 19. Dezember 2026, UVZ 139/2026, enthaltene dingliche Einigungserklärung gesondert für die Leinebogen Projektbank AG entgegen. Die Empfangsvollmacht ist in der Nebenakte verwahrt. Die Eigentümerin hat die Erklärung nicht widerrufen. Mit der Entgegennahme wird die Bindung der Eigentümerin gegenüber der Gläubigerin nach Maßgabe von § 873 Absatz 2 BGB herbeigeführt. Gez. Dr. Carla Fink, Notarin.',
        'Geschäftsstellenvermerk: Die angeforderten S/W-Ausfertigungen, beglaubigten Abschriften und Vollzugsmitteilungen zur Grundschuldbestellung umfassen insgesamt 40 abgegebene Seiten. Die Aufnahme des Empfangsvermerks verändert den Text der ursprünglichen Erklärung nicht. Der Eintragungsantrag wird mit den elektronisch strukturierten Daten an das Grundbuchamt übermittelt. Die Urschrift verbleibt in notarieller Verwahrung.',
        ], signer='Dr. Carla Fink, Notarin · Abschrift einschließlich des gesonderten Empfangsvermerks')

    for number, actor in enumerate(CONTRACTORS, 171):
        name, address, _, _ = ACTORS[actor]
        security = f'2600000{number:03d}01'
        add(number, 'Freistellung_48b_'+actor, '2026-12-20', 'steuer',
            'Freistellungsbescheinigung zum Steuerabzug bei Bauleistungen', [
            'Bescheinigung gemäß § 48b Absatz 1 Satz 1 des Einkommensteuergesetzes. Empfänger von Bauleistungen des nachstehend bezeichneten Unternehmens sind für Gegenleistungen innerhalb des angegebenen Gültigkeitszeitraums von der Pflicht zum Steuerabzug befreit.',
            ('t', [['Merkmal', 'Angabe'], ['Leistendes Unternehmen', name], ['Anschrift', address], ['Steuernummer', taxid(actor)], ['Sicherheitsnummer', security], ['Ausstellendes Finanzamt', 'Finanzamt Hildesheim'], ['Ausstellungsdatum', '20.12.2026'], ['Gültigkeitszeitraum', '01.01.2027 bis einschließlich 31.12.2028'], ['Umfang', 'Allgemeine Freistellung für Bauleistungen; keine Beschränkung auf einzelne Aufträge oder Leistungsempfänger']], [142,353]),
            'Die Freistellung gilt für Gegenleistungen, die innerhalb des bezeichneten Gültigkeitszeitraums erbracht werden. Eine Aufrechnung mit Gegenansprüchen steht einer Zahlung gleich. Die Bescheinigung ist dem Leistungsempfänger vor Erbringung der Gegenleistung vorzulegen. Da keine Beschränkung auf eine einzelne Bauleistung besteht, kann dem Leistungsempfänger eine Kopie überlassen werden.',
            'Die Erteilung erfolgt unter dem Vorbehalt des Widerrufs. Für die Prüfung der Gültigkeit sind Steuernummer und Sicherheitsnummer anzugeben. Der Leistungsempfänger kann eine elektronische Bestätigung beim Bundeszentralamt für Steuern einholen oder sich bei dem ausstellenden Finanzamt vergewissern. Die Bescheinigung trifft keine Aussage über die Steuerschuldnerschaft nach § 13b UStG.',
            ], recipient=actor, signer='Dienstsiegel Finanzamt Hildesheim · Anja Dorn, Veranlagung')

    data = json.loads((ROOT/'quality/hildesheim-achtfamilienhaus/finanzdaten.json').read_text())
    selected = []
    for tx in data['transactions']:
        matches = [a for a in CONTRACTORS if ACTORS[a][0] == tx['counterparty']]
        if matches and tx['direction'] == 'Abfluss':
            actor = matches[0]
            assert '2027-01-01' <= tx['date'] <= '2028-12-31', tx
            selected.append((actor, tx))
    sections = [
        'Interner Abschlussvermerk der kaufmännischen Projektakte zum 31. Dezember 2028. Bearbeitet von Lea Fricke und freigegeben von Maren Birk. Das Register dokumentiert die vor den Bauzahlungen vorliegenden Freistellungsbescheinigungen und die zugeordneten Gültigkeitsabfragen. Maßgeblich sind die einzelnen Zahlungsdaten des Projektkontos; der Rechnungszeitraum allein reicht für die Zuordnung nicht aus.',
        ('h', '1 Eingang und Zuordnung der Bescheinigungen'),
        'Die allgemeinen Freistellungsbescheinigungen der acht unten benannten Auftragnehmer gingen am 21. Dezember 2026 als lesbare Kopien im Projektpostfach ein. Name, Anschrift, Steuernummer, Sicherheitsnummer, Gültigkeitszeitraum und Siegelvermerk wurden mit dem jeweiligen Kreditorenstamm abgeglichen. Die Erstabfrage nach Beginn der Gültigkeit erfolgte am 2. Januar 2027; Ergebnis bei allen acht Datensätzen: Bescheinigung gültig für den Zeitraum 1. Januar 2027 bis 31. Dezember 2028. Originaldateien und Abfragevermerke sind der jeweiligen Kreditorenakte zugeordnet.',
        ('t', [['Beleg', 'Auftragnehmer', 'Steuernummer', 'Sicherheitsnummer']]+[[str(n), ACTORS[a][0], taxid(a), f'2600000{n:03d}01'] for n,a in enumerate(CONTRACTORS,171)], [40,220,100,135]),
        ('page',), ('h', '2 Prüfung vor den ersten Zahlungen'),
        'Zu jeder nachstehenden Überweisung wurde am selben Tag vor Freigabe die Gültigkeit unter der angegebenen Sicherheitsnummer erneut abgefragt. Die jeweilige Bestätigung lautete gültig; es lag kein Widerrufshinweis vor. In den Abfragevermerken sind die ursprüngliche Gültigkeitsdauer und die Identität des Leistenden unverändert gespeichert. Die unten angegebenen Beträge sind die tatsächlich gebuchten Auszahlungen. Das Register entscheidet nicht über die materielle Berechtigung oder die Einmaligkeit der Rechnung.',
    ]
    for part, offset in enumerate(range(0,len(selected),7)):
        if part:
            sections += [('page',), ('h', f'{part+2} Fortgeführte Gültigkeitsprüfungen')]
        rows = [['Zahlung und Abfrage', 'Kreditor und Rechnungsnummer', 'Auszahlung EUR', 'FSB Beleg']]
        for actor, tx in selected[offset:offset+7]:
            n = 171+CONTRACTORS.index(actor)
            rows.append([date.fromisoformat(tx['date']).strftime('%d.%m.%Y'), ACTORS[actor][0]+'\n'+tx['invoice'], euro(tx['amount']), str(n)+'\ngültig'])
        sections.append(('t', rows, [86,243,100,66]))
    sections += [('h', '5 Ablage und Abschluss'),
        'Auftragnehmeridentität und Gültigkeit wurden jeweils vor Zahlung bestätigt. Ein Steuerabzug wurde für die erfassten Zahlungen nicht vorgenommen. Erstattungen von Auftragnehmern werden im Bank- und Rechnungsregister geführt; sie sind keine ausgehenden Gegenleistungen dieses Registers. Für Zahlungen nach Ablauf des 31. Dezember 2028 darf auf diese Bescheinigungen nicht mehr zurückgegriffen werden; gegebenenfalls ist vor einer weiteren Bauzahlung eine neue gültige Bescheinigung anzufordern und zu prüfen.',
        'Planungsleistungen der Architektin und der Fachplaner, Notarkosten, Grundstückskaufpreis, Steuern, behördliche Gebühren und Bankentgelte werden hier nicht als Bauleistungen erfasst. Die Freistellungsunterlagen und Gültigkeitsvermerke bleiben mit den Zahlungsbelegen gemäß den jeweils geltenden Aufbewahrungspflichten in der Projektakte. Die steuerliche Behandlung der Rechnungen einschließlich Umsatzsteuer wird gesondert beurteilt.']
    add(179, 'Freistellung_Abfrage_und_Gueltigkeitsprotokoll', '2028-12-31', 'verwaltung',
        'Register der Freistellungsbescheinigungen und Zahlungsprüfungen', sections,
        signer='Gez. Lea Fricke · Freigabe Maren Birk am 31.12.2028')
    return RECORDS


if __name__ == '__main__':
    build_records(documents())
    print(f'{len(RECORDS)} Erwerbs- und Freistellungsoriginale geschrieben.')
