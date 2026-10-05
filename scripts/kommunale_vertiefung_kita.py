"""Fallbezogene Quellen für neue Kita-Akte und vier ergänzte Altakten.

Nur Inhalte. Der gemeinsame Builder erzeugt Briefe als DOCX und PDF und fügt
der Klage das aus ``exhibits`` gebildete Anlagenverzeichnis hinzu.
"""

FOLDER = 'kommunikation-und-deckung'


def doc(file, title, date, kind, body, sender='', recipient=''):
    return dict(file=file, title=title, date=date, kind=kind,
                body=body.strip(), sender=sender, recipient=recipient)


def ex(n, filename, description):
    return dict(label=f'K{n}', source=f'{FOLDER}/{filename}', description=description)


CASES = [dict(
    slug='akha-wuerzburg-kitaplatz',
    title='Leni Sauermilch – vier Monate ohne Betreuungsplatz',
    summary='Eine angestellte Mutter verlangt 10.360 EUR Verdienstausfall vom Jugendhilfeträger. Gemeinde, Landkreis und Kommunalversicherer streiten über rechtzeitige Anmeldung, verfügbare Tagespflege, Personalplanung und Schadensminderung.',
    is_new=True,
    notes='Alle Personen, Unternehmen, Gemeinden, Landkreis und Versicherungsbedingungen sind erfunden. Der Landkreis Mainlaub ist eine Fallkonstruktion im Landgerichtsbezirk Würzburg; die kreisangehörige Gemeinde Quendelbrunn ist nicht die kreisfreie Stadt Würzburg. Vertragsbeträge und Meldeschwellen sind ausschließlich Szenarioannahmen, keine Angaben zu AKHA-Regeln. Die Klägerin verlangt eigenen Verdienstausfall, nicht den Förderanspruch des Kindes. Die nicht eingereichte Klage berücksichtigt den bis 05.10.2026 bekannten Sachstand. Der private Einzelvertrag des Versicherers hat eine eigene Rückdeckung; es wird kein direkter Familienanspruch gegen AKHA oder Rückversicherer behauptet. Der bereits durchgeführte verwaltungsgerichtliche Eilrechtsschutz ist in einem anwaltlichen Dokumentationsblatt beschrieben; es wird keine amtlich wirkende Gerichtsentscheidung nachgebaut.',
    core=[f'{FOLDER}/01_Bedarfsanmeldung.docx', f'{FOLDER}/02_Arbeitgeberbestaetigung.docx', f'{FOLDER}/03_Schadensrechnung.docx', f'{FOLDER}/16_Klageentwurf_Sauermilch.docx'],
    exhibits=[
        ex(1,'01_Bedarfsanmeldung.docx','Bedarf ab 01.05.2026, Familienangaben und dokumentierter Zugang beim Jugendamt'),
        ex(2,'02_Arbeitgeberbestaetigung.docx','Vereinbarter Wiedereinstieg, Entgelt und unbezahlte Freistellung'),
        ex(3,'03_Schadensrechnung.docx','Monatliche Nettoberechnung einschließlich ersparter Betreuung und Fahrten'),
        ex(4,'04_Kapazitaetsvermerk.docx','Planungsstand, zwei Personalabgänge und nicht beschiedene Reserve'),
        ex(5,'05_Betreuungssuche.docx','Konkrete Alternativen und nicht bedarfsdeckendes Augustangebot'),
        ex(6,'06_Eilrechtsschutz_Dokumentation.docx','Anwaltliche Dokumentation des Eilantrags und weiterer Maßnahmen'),
        ex(7,'08_Gemeinde_an_Jugendamt.eml','Gemeinde bestätigt Anmeldung und offene Stellen'),
        ex(8,'09_Augustangebot.eml','Inhalt und zeitliche Grenzen des Tagespflegeangebots'),
        ex(9,'10_Arbeitgeber_Ergaenzung.eml','Tatsächlicher Arbeitsbeginn und fehlende Ausweichmöglichkeit'),
        ex(10,'13_Anspruchsschreiben.pdf','Zahlungsaufforderung mit Zugang und Fristsetzung'),
        ex(11,'14_Landkreis_Stellungnahme.pdf','Einwendungen des Landkreises und noch offene Prüfung'),
    ],
    attachments={
        '08_Gemeinde_an_Jugendamt.eml':[f'{FOLDER}/01_Bedarfsanmeldung.docx'],
        '10_Arbeitgeber_Ergaenzung.eml':[f'{FOLDER}/02_Arbeitgeberbestaetigung.docx'],
        '11_Landkreis_an_Versicherer.eml':[f'{FOLDER}/03_Schadensrechnung.docx',f'{FOLDER}/14_Landkreis_Stellungnahme.pdf'],
        '12_Versicherer_Rueckfragen.eml':[f'{FOLDER}/07_Deckungsblatt.docx'],
    },
    documents=[
        doc('01_Bedarfsanmeldung.docx','Bedarfsanmeldung und Eingang beim Jugendamt','12.01.2026','document','''## 1 Antrag der Eltern

Wir, Naila Sauermilch und Anselm Sauermilch, Quendelgasse 7, 97299 Quendelbrunn, beantragen für unsere Tochter Leni Sauermilch, geboren am 24. April 2025, ab dem 1. Mai 2026 einen Betreuungsplatz von Montag bis Freitag zwischen 07:45 und 15:30 Uhr. Wir leben mit Leni durchgehend in Quendelbrunn und üben die elterliche Sorge gemeinsam aus. Zuständiger Jugendhilfeträger unseres Wohnorts ist der Landkreis Mainlaub.

Naila nimmt zum 1. Mai ihre unbefristete Beschäftigung bei der Mainfaden Medizintechnik GmbH in Würzburg wieder auf. Die Arbeit findet von 08:30 bis 15:00 Uhr vor Ort statt. Anselm arbeitet montags bis freitags von 06:30 bis 15:30 Uhr als Instandhalter; ein dauerhafter Schichttausch ist nicht vereinbart. Wir können eine Krippe oder eine geeignete Kindertagespflege in Anspruch nehmen. Es geht nicht nur um unsere bevorzugte Einrichtung Quendelzwerge. Bitte prüfen Sie alle zumutbaren Möglichkeiten, auch außerhalb des Gemeindegebiets.

Wir melden den Bedarf unmittelbar beim Jugendamt an. Die Gemeinde erhält eine Kopie. Wegen der Wege und Übergaben benötigen wir den genannten Umfang. Wir bitten um rechtzeitige Mitteilung, damit eine Eingewöhnung noch im April vereinbart werden kann. Das Ende der Elternzeit steht fest. Ohne Betreuung droht ein monatlicher Verdienstausfall.

Naila Sauermilch und Anselm Sauermilch

## 2 Registrierter Eingang

Jugendamt Mainlaub, Posteingang JH-24-116: Vollständiger Antrag einschließlich Arbeitszeitbestätigung am 12. Januar 2026 um 10:14 Uhr im Funktionspostfach eingegangen. Eingang am 13. Januar um 09:22 Uhr durch Sachbearbeiterin Roswitha Knödel bestätigt. Geburtsdatum, Wohnort und Betreuungsbeginn wurden richtig erfasst. Die Akte ist nicht als reine Wartelistenanmeldung bei einer einzelnen Einrichtung geführt. Eine besondere gesetzliche Anmeldefrist wird mit diesem Registerauszug nicht behauptet.'''),
        doc('02_Arbeitgeberbestaetigung.docx','Wiedereinstieg und Entgelt von Naila Sauermilch','21.09.2026','document','''Mainfaden Medizintechnik GmbH, Fadenlaubweg 14, 97076 Würzburg

## 1 Vertragsgrundlage

Frau Naila Sauermilch ist seit 2020 unbefristet als technische Dokumentationsassistentin beschäftigt. Die schriftliche Rückkehrvereinbarung vom 8. Dezember 2025 sieht ab 1. Mai 2026 eine Tätigkeit von montags bis freitags jeweils 08:30 bis 15:00 Uhr einschließlich einer halbstündigen unbezahlten Pause vor. Das sind 30 Arbeitsstunden wöchentlich. Die Vergütung beträgt monatlich 4.150,00 EUR brutto. Ein monatlicher Nettoauszahlungsbetrag von 2.860,00 EUR ergibt sich unter den im gesamten Zeitraum unveränderten persönlichen Abzugsmerkmalen aus unserer Vergleichsabrechnung. Die Septemberabrechnung weist denselben Betrag aus.

## 2 Tatsächlicher Verlauf

Wegen fehlender Kinderbetreuung bewilligten wir auf Antrag unbezahlte Freistellung vom 1. Mai bis 31. August, jeweils mit Rückkehrmöglichkeit zum Beginn der folgenden Arbeitswoche nach einer Vorankündigung von fünf Arbeitstagen. Wir zahlten in diesen vier Monaten weder Lohn noch freiwilligen Ausgleich. Die Rückkehrvereinbarung wurde nicht aufgehoben. Eine bereits gebundene Vertretung hätte den Wiedereinstieg nicht verhindert. Die Aufgaben wurden zwischenzeitlich durch Mehrarbeit im Team und einen kündbaren Dienstleistungsabruf abgedeckt.

Am 1. September nahm Frau Sauermilch die Arbeit tatsächlich auf. Die Betreuung war nach Eingewöhnung Ende August gewährleistet. Sie erschien seither zu den vereinbarten Zeiten. Die Tätigkeit erfordert den Zugriff auf im Betrieb verwahrte technische Originalunterlagen und die Abstimmung mit der Qualitätsprüfung. Wir konnten im fraglichen Zeitraum weder reine Heimarbeit noch einen täglichen Zweistundenblock zwischen 10:00 und 12:00 Uhr anbieten. Eine Verschiebung auf Abende oder Wochenenden war organisatorisch nicht möglich.

## 3 Abrechnung und Auskunft

Eine durchgängige Beschäftigung von Mai bis August hätte nach unserem Abrechnungslauf 11.440,00 EUR netto erbracht. Sonderzahlungen, Boni, Überstunden und Arbeitgeberbeiträge sind in diesem Betrag nicht enthalten. Die Aussage zur hypothetischen Nettoabrechnung steht unter dem Vorbehalt einer späteren Einkommensteuerveranlagung; eine zusätzliche Steuer auf Schadensersatz wird hier nicht hochgerechnet. Als Auskunftsperson steht Personalleiterin Ottilie Wacker, zu laden unter der Geschäftsanschrift, zur Verfügung.

Ottilie Wacker, Personalleitung'''),
        doc('03_Schadensrechnung.docx','Vier Monatsbudgets und Abzüge','22.09.2026','document','''## 1 Anspruchszeitraum

Naila Sauermilch verlangt ausschließlich den eigenen Nettoverdienstausfall vom 1. Mai bis 31. August 2026. Grundlage sind die Arbeitgeberbestätigung und die folgenden privaten Budgetangaben. Die Arbeitgeberin beziffert den entgangenen Nettoauszahlungsbetrag für jeden der vier Monate mit 2.860,00 EUR, zusammen 11.440,00 EUR. Für April und September wird kein Ausfall verlangt.

## 2 Ersparnisse

Das vorab angefragte kommunale Betreuungsmodell hätte monatlich 230,00 EUR Elternbeitrag gekostet; dieselbe Belastung gilt für den seit September genutzten Platz. Im Mai, Juni, Juli und August wurde kein Beitrag erhoben. Deshalb werden viermal 230,00 EUR, insgesamt 920,00 EUR, abgezogen. Verpflegungsbeiträge werden nicht angesetzt: Leni hätte sowohl zuhause als auch bei Betreuung essen müssen; ein darüber hinausgehender konkret ersparter Mehrbetrag ist nicht belegt.

Die geplanten Arbeitsfahrten hätten gegenüber den tatsächlich zurückgelegten Privatfahrten nach der gemeinsamen Aufstellung 40,00 EUR monatliche zusätzliche Kraftstoff- und Parkkosten verursacht. Abgezogen werden viermal 40,00 EUR, insgesamt 160,00 EUR. Fixe Fahrzeugkosten bleiben in beiden Verläufen bestehen. Eine zusätzliche steuerliche Kilometerpauschale wird nicht noch einmal abgezogen.

## 3 Monatliche Differenzen

Für Mai ergibt sich 2.860,00 EUR abzüglich 230,00 EUR und 40,00 EUR, mithin 2.590,00 EUR. Für Juni, Juli und August gilt dieselbe Rechnung. Viermal 2.590,00 EUR ergibt 10.360,00 EUR. Die Addition enthält keine pauschale Entschädigung für familiären Stress und keine Bewertung der eigenen Kinderbetreuungsstunden.

## 4 Weitere Geldbewegungen

Das Elterngeld endete vor Mai. Die Familienkasse zahlte unverändert Kindergeld; es wäre auch bei rechtzeitiger Arbeitsaufnahme angefallen. Es gab für Mai bis August weder Arbeitslosengeld noch Ersatzlohn, Krankengeld oder Versicherungsleistungen. Eine am 4. Juni erteilte private Betreuungsanfrage führte mangels Kapazität zu keinem Vertrag und keiner Rechnung. Schadensersatz oder Vorschüsse sind bis 5. Oktober nicht eingegangen. Ein Darlehen von Anselms Vater finanzierte den Alltag; seine Rückzahlungspflicht wird nicht als zusätzliche Schadensposition geltend gemacht.

Naila Sauermilch, mit Anselm Sauermilch abgeglichen'''),
        doc('04_Kapazitaetsvermerk.docx','Jugendamt – Kapazitäten und ungeklärte Reserve','25.09.2026','document','''Landkreis Mainlaub, Jugendamt, Sachgebiet Kindertagesbetreuung

## 1 Stand vor dem Betreuungsbeginn

Die Bedarfsplanung vom November 2025 führte für Quendelbrunn und zwei Nachbarorte elf zusätzliche Bedarfe zum Frühjahr 2026. Eine am 9. Dezember eingegangene Personalmitteilung kündigte zwei Abgänge bei Quendelzwerge zum 31. März an. Die Gemeinde meldete dies am 12. Dezember an uns. Für den Beginn 1. Mai waren zwölf neue Plätze mit einer zusätzlichen Fachkraft vorgesehen. Die Ausschreibung erfolgte erst am 15. Februar; der Grund für den Abstand zur Dezembermeldung ist in der Personalakte nicht erklärt. Keine Einstellung war bis Ende April abgeschlossen.

## 2 Reserveangebot

Die anerkannte Tagespflegeperson Walburga Schätzlein bot dem Jugendamt am 2. Februar zwei zusätzliche Plätze in genehmigten Räumen an. Voraussetzung war nach ihrer Erklärung die bis 15. Februar erbetene Entscheidung über einen befristeten Zuschuss von 3.200,00 EUR zur Ersatzkraft. Eine Fachprüfung bestätigte am 10. Februar, dass die räumlichen und fachlichen Voraussetzungen bestanden. Die Vorlage blieb bis 27. März im Haushaltsumlauf. Am 30. März teilte Frau Schätzlein mit, dass die Ersatzkraft inzwischen anderweitig gebunden sei. Ob sie bei fristgerechter Zuschussentscheidung tatsächlich beide Plätze zum 1. Mai hätte eröffnen können, muss anhand ihrer Unterlagen und der damaligen Personalzusage geklärt werden. Eine sichere hypothetische Zuweisung an Leni wird hier nicht bescheinigt.

## 3 Weiterer Verlauf

Der am 5. Juni dokumentierte Krankenstand von zwei bereits eingesetzten Betreuungspersonen verschärfte die Lage, erklärt aber nicht den fehlenden Platz am 1. Mai. Eine Liste der umliegenden Einrichtungen wurde den Eltern mehrfach überlassen. Der erste konkrete Platznachweis betraf ab 17. August nur Montag bis Donnerstag 09:00 bis 12:00 Uhr bei der 42 Kilometer vom Wohnort entfernten Tagespflegestelle Rosenhut. Die Eltern lehnten nach Rücksprache mit dem Arbeitgeber ab. Ein Platz in Quendelbrunn ab 1. September wurde am 14. August zugesagt; die Eingewöhnung fand vom 17. bis 28. August statt.

Roswitha Knödel, Sachbearbeitung. Dieser Vermerk dokumentiert Aktenfunde; er ersetzt keine Aussage der Gemeinde, der Reservekraft oder der Eltern.'''),
        doc('05_Betreuungssuche.docx','Betreuungssuche und Tagesablauf der Familie','23.09.2026','document','''## 1 Suche von Januar bis April

Naila Sauermilch fragte am 19. Januar bei Quendelzwerge, am 22. Januar bei Mainkäfer und am 4. Februar bei der Kindertagespflege Hiltrud Kleinlaut nach. Keine dieser Stellen bot einen bedarfsdeckenden Platz ab Mai an. Hiltrud Kleinlaut hatte nur einen bereits belegten Nachmittagsplatz. Die Familie beschränkte sich nicht auf eine bestimmte Konzeption. Am 12. März fragte Naila beim Jugendamt nach Kindertagespflege und nach einer Übergangslösung. Am 8. April wiederholte die Anwältin dies mit dem konkreten Hinweis auf den bevorstehenden Nettoausfall.

## 2 Familie und Arbeit

Anselm Sauermilch arbeitete werktags von 06:30 bis 15:30 Uhr einschließlich Pause; seine Anfahrt dauerte 25 Minuten. Der Arbeitgeber bestätigte auf Anfrage am 16. April, dass ein täglicher Schichtwechsel für vier Monate nicht angeboten werden könne. Die Großmutter lebte in Hannover und unterstützte an einem Wochenende, nicht an Werktagen. Der Großvater in Würzburg war selbst pflegebedürftig. Eine pauschale Behauptung, alle Angehörigen seien arbeitsunfähig, wird nicht erhoben. Entscheidend ist, dass keine Person die tägliche Betreuung tatsächlich übernehmen konnte. Eine private Agentur teilte am 4. Juni mit, dass sie keine geeignete Betreuungsperson für fünf Tage pro Woche vermitteln könne; es wurde nichts gebucht oder gezahlt.

## 3 Augustangebot und Ende des Ausfalls

Das Angebot Rosenhut umfasste zwölf Stunden pro Woche, ohne Freitag, und sah keine Randzeiten vor. Zwischen Wohnort und Tagespflege lagen 42 Kilometer. Eine Fahrt von der Tagespflege zur Arbeitsstätte hätte zusätzlich rund 35 Minuten gedauert. Selbst bei pünktlicher Abgabe um 09:00 Uhr wären nur etwa zwei Arbeitsstunden bis zur erforderlichen Abfahrt zur Abholung geblieben. Die Arbeitgeberin bestätigte, dass daraus kein nutzbarer Arbeitsplatz entstehe. Die Eltern boten an, Rosenhut mit einer zweiten Betreuung zu kombinieren. Das Jugendamt konnte keine Ergänzung benennen.

Der ab September verfügbare Platz Quendelzwerge umfasst 07:45 bis 15:30 Uhr an fünf Tagen. Die Eingewöhnung lief Ende August. Es gab seitdem keine betreuungsbedingte Abwesenheit der Mutter. Die Familie verlangt keine Zahlung für die Eingewöhnung im April, keinen entgangenen Urlaub und keinen unbestimmten Folgeschaden.

Naila Sauermilch'''),
        doc('06_Eilrechtsschutz_Dokumentation.docx','Anwaltliche Dokumentation des Primärrechtsschutzes','24.09.2026','document','''Rechtsanwältin Jolanda Knospenlaub, Zedernfächerweg 9, 97074 Würzburg

## 1 Antrag und dokumentierter Versand

Ich beantragte am 14. April 2026 im Namen der minderjährigen Leni Sauermilch, vertreten durch Naila und Anselm Sauermilch, beim Bayerischen Verwaltungsgericht Würzburg eine einstweilige Anordnung gegen den Landkreis Mainlaub. Der Antrag verlangte, ab 1. Mai bis zur Entscheidung über den Förderanspruch einen geeigneten Betreuungsplatz von Montag bis Freitag 07:45 bis 15:30 Uhr nachzuweisen. Der in der Kanzlei gespeicherte elektronische Versandbericht weist den erfolgreichen Eingang am 14. April um 15:06 Uhr aus. Der Bericht und das Antragsexemplar befinden sich in der Mandatsakte; dieses Blatt gibt den Ablauf wieder und ist kein gerichtlicher Eingangsstempel.

## 2 Eilverfahren und Durchsetzung

Nach dem Eingang der Stellungnahme des Landkreises am 21. April beantragte ich ausdrücklich, die Angelegenheit noch vor Ende April zu entscheiden. Am 28. April wurde dem Antrag nach der in der Kanzlei vorliegenden Entscheidung stattgegeben. Der Landkreis bestritt nicht den Förderanspruch, erklärte jedoch, einen verfügbaren Platz erst finden zu müssen. Ich forderte ihn am 29. April unter Hinweis auf die vollziehbare Anordnung zur Umsetzung auf. Am 5. Mai beantragte ich gerichtliche Vollstreckungsmaßnahmen, nachdem keine konkrete Einrichtung benannt worden war. Nach weiterer gerichtlicher Androhung teilte der Landkreis am 18. Mai weiterhin das Fehlen eines geeigneten Platzes mit. Weitere Umsetzungsaufforderungen erfolgten am 4. Juni und 2. Juli. Das Verfahren wurde nicht gegen eine Abfindung erledigt.

## 3 Grenzen der Dokumentation

Dieses Blatt ist eine anwaltliche Verlaufsbestätigung. Für eine gerichtliche Zivilklage sollen die konkret bezeichneten elektronischen Schriftsätze, Eingangsbestätigungen und Entscheidungen aus der Verwaltungsgerichtsakte beigezogen werden. Ein amtlich wirkender Beschluss wird nicht durch eine selbst gestaltete Abschrift ersetzt. Am 2. September erklärten die Beteiligten das Förderverfahren nach tatsächlicher Platzbereitstellung für erledigt. Die hier geltend gemachten Verdienstausfallschäden waren weder Gegenstand einer Zahlung noch einer abschließenden materiellen Einigung.

Jolanda Knospenlaub, Rechtsanwältin'''),
        doc('07_Deckungsblatt.docx','Deckungsblatt ML-JH-2026-116','05.10.2026','document','''Kommunalversicherung Mainbogen VVaG – Sachbearbeiter Vitus Hasenwinkel

## 1 Erfasster Vertrag

Versicherungsnehmer ist der Landkreis Mainlaub. Der für 2026 erfasste Vertrag KM-ML-2026 umfasst gesetzliche Haftpflichtansprüche aus der Tätigkeit seines Jugendamts einschließlich reiner Vermögensschäden aus fahrlässiger Amtspflichtverletzung. Die Versicherungssumme hierfür beträgt 1.000.000,00 EUR je Schadenereignis. Der Selbstbehalt beträgt 1.000,00 EUR je Schadenereignis. Abwehrkosten fallen nach diesem Vertragsauszug außerhalb des Selbstbehalts an. Vorsätzliche Herbeiführung ist ausgeschlossen; die vorliegenden Unterlagen belegen bislang keine vorsätzliche Schadenszufügung. Die Deckungsprüfung ersetzt die Prüfung der gesetzlichen Haftung nicht.

## 2 Meldung und Reserve

Schadenmeldung des Landkreises am 30. September, ergänzt am 2. Oktober. Gefordert werden 10.360,00 EUR. Die Arbeitsreserve beträgt vorläufig 13.000,00 EUR, davon 10.360,00 EUR möglicher Hauptanspruch und 2.640,00 EUR geschätzte Abwehr- und Nebenkosten. Eine Arbeitsreserve stellt weder ein Anerkenntnis noch eine Zahlungsfreigabe dar. Sollte die Hauptforderung vollständig begründet sein, wären nach dem vereinbarten Selbstbehalt 1.000,00 EUR beim Landkreis und 9.360,00 EUR beim Versicherer abzurechnen. Der gesetzliche Anspruch der Mutter würde dadurch nicht auf zwei Gegner verteilt.

## 3 Rückdeckung

Der interne Rückdeckungsvermerk ordnet das Jugendamtsrisiko dem Jahresvertrag RB-2026 zu. Für diesen Vertrag ist eine Einzelmeldung ab einer erwarteten Gesamtbelastung von 250.000,00 EUR vorgesehen. Darunter erfolgt nur eine periodische Bestandsmeldung ohne personenbezogene Einzelfallunterlagen. Der Rückdeckungsanteil beginnt nach dem erfassten Vertragsauszug oberhalb einer Priorität von 500.000,00 EUR. Die bisherige Reserve erreicht weder Meldeschwelle noch Priorität. Deshalb wird zu Sauermilch kein personenbezogenes Schreiben an einen Rückversicherer erzeugt. Weitere ähnliche Ansprüche dürfen nicht ohne Prüfung einer einschlägigen Serienschadenklausel zusammengerechnet werden; eine solche Zusammenrechnung ist hier nicht festgestellt.

## 4 Nächster Entscheidungspunkt

Vor einer Zahlung müssen Reserveangebot, Eingangs- und Personalchronologie sowie die Gegenrechnung der Arbeitskosten geklärt werden. Die Familie erhält ihre Sachantwort vom Landkreis. Ein direkter Zahlungsanspruch gegen einen internen Ausgleichsverband oder Rückversicherer ergibt sich aus diesem Blatt nicht. Vitus Hasenwinkel führt die Deckungsakte; die rechtliche Entscheidung über das Anspruchsschreiben liegt weiterhin beim Landkreis.'''),
        doc('08_Gemeinde_an_Jugendamt.eml','Sauermilch: Anmeldung lag vor – unser Personalstand','2026-05-04T10:20:00+02:00','email','''Sehr geehrte Frau Knödel,

anbei erhalten Sie die bei uns gespeicherte Bedarfsanmeldung mit Ihrem Januar-Eingangsvermerk. Frau Sauermilch hatte von Anfang an ausdrücklich nach jeder geeigneten Krippe oder Tagespflege gefragt. Bitte führen Sie den Vorgang nicht als bloßen Wunsch nach Quendelzwerge. Am vergangenen Donnerstag stand die Familie erneut im Rathaus; wir konnten keinen freien Platz vermitteln.

Die Gemeinde ist Betreiberin von Quendelzwerge, aber nicht selbst Jugendhilfeträger. Wir hatten Ihnen die zwei Personalabgänge am 12. Dezember mitgeteilt. Die Ausschreibung wurde tatsächlich erst am 15. Februar veröffentlicht. Nach der Rücksprache mit unserer Personalstelle lässt sich die dazwischenliegende Liegezeit nicht mit einem noch fehlenden Stellenbeschluss erklären: Der Beschluss war am 8. Dezember bereits vorhanden. Ob sich bei früherer Ausschreibung jemand beworben hätte, können wir nicht versprechen.

Bitte prüfen Sie das im Februar besprochene Reserveangebot von Frau Schätzlein und andere erreichbare Tagespflegen. Die Mutter hat uns die gerichtliche Anordnung gezeigt. Dass wir vor Ort keinen Platz haben, beantwortet Ihre Nachweispflicht gegenüber dem Kind nicht. Wir benötigen eine gemeinsame, sachlich richtige Antwort und keine weitere Rundmail mit einer Liste bereits erfolglos angerufener Einrichtungen.

Freundliche Grüße
Kunibert Quassel
Geschäftsleitung Gemeinde Quendelbrunn''','Kunibert Quassel <geschaeftsleitung@quendelbrunn.example>','Roswitha Knödel <jugendamt@mainlaub-kreis.example>'),
        doc('09_Augustangebot.eml','Verbindliches Angebot Rosenhut: Zeiten und Ergänzungsbedarf','2026-08-12T09:15:00+02:00','email','''Sehr geehrte Frau Sauermilch,

wir können Ihnen bei der Tagespflegestelle Rosenhut ab Montag, 17. August, verbindlich einen Platz für Leni anbieten. Die Betreuung ist montags bis donnerstags von 09:00 bis 12:00 Uhr möglich. Freitag und zusätzliche Randstunden kann die Stelle nicht übernehmen. Sie liegt nach unserer Wegberechnung 42 Kilometer von Ihrer Anschrift entfernt. Der Beitrag würde entsprechend der kurzen Buchungszeit gesondert berechnet; einen Ganztagsbeitrag verlangen wir für dieses Angebot nicht.

Uns ist bewusst, dass Sie 07:45 bis 15:30 Uhr an fünf Tagen angemeldet haben. Wir bezeichnen die drei Stunden daher nicht als vollständige Erfüllung Ihres Bedarfs. Bitte besprechen Sie trotzdem mit Ihrer Arbeitgeberin, ob eine befristete teilweise Rückkehr möglich wäre. Ihre Mitteilung, dass Ihr Mann zu diesen Zeiten ebenfalls arbeitet, haben wir vermerkt. Eine zweite ergänzende Tagespflege können wir heute nicht konkret benennen.

Unabhängig davon soll die Einstellung bei Quendelzwerge zum 1. September erfolgen. Die dortige Leitung möchte morgen über die Eingewöhnung sprechen. Das ist heute noch keine verbindliche Zusage für September. Wir werden Ihnen bis Freitag eine belastbare schriftliche Nachricht geben und den Versicherungsbereich über den bis dahin entstandenen Erwerbsausfall gesondert informieren. Sie müssen zur Prüfung dieses Angebots keine Erklärung abgeben, auf Schadensersatz zu verzichten.

Mit freundlichen Grüßen
Roswitha Knödel''','Roswitha Knödel <jugendamt@mainlaub-kreis.example>','Naila Sauermilch <naila.sauermilch@briefpost.example>'),
        doc('10_Arbeitgeber_Ergaenzung.eml','Sauermilch: Septemberabrechnung und Rückkehrmöglichkeiten','2026-09-23T13:40:00+02:00','email','''Sehr geehrte Frau Knospenlaub,

ich bestätige die beigefügte Arbeitgeberbescheinigung nach Abgleich mit der heute vorbereiteten Septemberabrechnung. Frau Sauermilch hat am 1. September tatsächlich begonnen. Der Nettoauszahlungsbetrag beträgt 2.860,00 EUR. Eine Sonderprämie oder nachträgliche Erstattung der vier unbezahlten Monate ist darin nicht enthalten.

Zum Einwand einer früheren Teilzeitrückkehr: Wir haben am 13. August nicht aus Bequemlichkeit abgelehnt. Bei Ankunft nach 09:35 Uhr und notwendiger Abfahrt vor 11:25 Uhr blieben weniger als zwei zusammenhängende Stunden. In dieser Zeit konnte Frau Sauermilch die Dokumentationsläufe mit der Qualitätsprüfung nicht übernehmen. Eine Aufgabe ausschließlich zuhause bestand nicht. Unsere Vertretung hätte dagegen eine reguläre Rückkehr nach fünf Arbeitstagen Vorlauf auch im Juni oder Juli nicht verhindert. Wir hätten dann den externen Abruf entsprechend reduziert.

Frau Sauermilch hat uns seit April regelmäßig über die Suche informiert. Sie hat die unbezahlte Freistellung jeweils wegen fehlender Betreuung und mit ausdrücklichem Rückkehrvorbehalt beantragt. Wir haben keinen Wunsch nach einer unabhängig davon geplanten längeren Familienpause dokumentiert. Wenn für die Schadensprüfung die Brutto-Netto-Vergleichsabrechnung benötigt wird, stellen wir sie ihrer Bevollmächtigten mit Einverständnis der Arbeitnehmerin zur Verfügung; eine allgemeine Personalaktenübersendung an mehrere Versicherungsstellen ist dafür nicht erforderlich.

Freundliche Grüße
Ottilie Wacker''','Ottilie Wacker <personal@mainfaden-med.example>','Rechtsanwältin Jolanda Knospenlaub <kanzlei@knospenlaub.example>'),
        doc('11_Landkreis_an_Versicherer.eml','ML-JH-116: 10.360 EUR, Reserveangebot und Aktenabgleich','2026-10-02T11:05:00+02:00','email','''Sehr geehrter Herr Hasenwinkel,

anbei übersende ich die Schadensrechnung der Familie sowie unsere Stellungnahme vom 30. September. Die Forderung beträgt jetzt nachvollziehbar 10.360,00 EUR. Sie enthält weder vier volle Bruttogehälter noch zusätzlich eine fiktive Vergütung der Eigenbetreuung. Die abgezogenen Beiträge von 920,00 EUR und Fahrtkosten von 160,00 EUR sind noch mit den Belegen zu prüfen.

Die Antragstellung im Januar und die fehlende bedarfsgerechte Betreuung bis Ende August bestreiten wir nicht. Unser Hauptpunkt ist das Verschulden. Zwei Personalabgänge, das verspätet bearbeitete Zuschussangebot und die spätere Krankheitswelle sind unterschiedliche Vorgänge. Ich möchte deshalb nicht die Formulierung „unvorhersehbarer Personalausfall“ für den gesamten Zeitraum freigeben. Das Mai-Defizit bestand vor den Erkrankungen. Frau Schätzlein will nächste Woche ihre damalige Zusage der Ersatzkraft heraussuchen; eine schriftliche Verfügbarkeitserklärung liegt uns heute noch nicht vor.

Bitte bestätigen Sie Deckungsumfang, Selbstbehalt und die Frage, ob der Betrag eine Rückdeckungsmeldung auslöst. Wir benötigen keine Zustimmung zu einem Anerkenntnis, sondern zunächst eine belastbare Prüfung und eine Person, die die Arbeitgeberrechnung mit unserer Kasse abgleicht. Die Antwortfrist der Anwältin läuft bis 16. Oktober. Ohne weitere Abstimmung werde ich keinen Vergleich abschließen und keine familienbezogenen Daten an zusätzliche Stellen senden.

Mit freundlichen Grüßen
Irmtraud Hopfenstiel
Kreisrechtsrätin''','Irmtraud Hopfenstiel <recht@mainlaub-kreis.example>','Vitus Hasenwinkel <schaden@mainbogen-vers.example>'),
        doc('12_Versicherer_Rueckfragen.eml','ML-JH-116: Deckung erfasst, Haftung noch offen','2026-10-05T09:35:00+02:00','email','''Sehr geehrte Frau Hopfenstiel,

das beigefügte Deckungsblatt gibt die für diesen Vorgang erfassten Vertragsdaten wieder. Reine Vermögensschäden des Jugendamts sind grundsätzlich eingeschlossen. Ein Selbstbehalt von 1.000,00 EUR würde im Innenverhältnis gelten. Die Klägerin könnte bei begründetem Anspruch trotzdem den gesamten Betrag vom Landkreis verlangen; bitte verweisen Sie sie nicht für einen Teilbetrag an uns.

Für die Haftungsprüfung benötige ich die Entscheidungskette zum Zuschuss von 3.200,00 EUR. Wer durfte die Ausgabe bewilligen, wann lag die fachlich vollständige Vorlage vor und weshalb blieb sie liegen? Das kleine Reserveangebot ist für die Verschuldensfrage möglicherweise wichtiger als die allgemeine Personalstatistik. Bitte prüfen Sie auch die tatsächliche Reichweite des Eilbeschlusses und der nachfolgenden Durchsetzungsanträge. Ein pauschaler Einwand, die Eltern hätten überhaupt keinen Rechtsschutz gesucht, passt nicht zur Akte.

Der Fall bleibt mit einer Arbeitsreserve von 13.000,00 EUR deutlich unter unserer vertraglichen Einzelmeldeschwelle. Ein personenbezogener Rückversichererbericht ist deshalb nicht vorgesehen. Das ist eine Deckungs- und Datenminimierungsentscheidung, keine Aussage über die politische Bedeutung fehlender Kitaplätze. Wir planen bis 12. Oktober eine interne Entscheidungsvorlage. Bis dahin darf die Versicherung gegenüber der Familie weder als zahlungsbereit noch als endgültig ablehnend dargestellt werden.

Mit freundlichen Grüßen
Vitus Hasenwinkel''','Vitus Hasenwinkel <schaden@mainbogen-vers.example>','Irmtraud Hopfenstiel <recht@mainlaub-kreis.example>'),
        doc('13_Anspruchsschreiben.docx','Sauermilch gegen Landkreis Mainlaub – Verdienstausfall','24.09.2026','letter','''Rechtsanwältin Jolanda Knospenlaub, Zedernfächerweg 9, 97074 Würzburg

Landkreis Mainlaub, Kreisrechtsstelle, Lindenquendelplatz 2, 97076 Würzburg

Sehr geehrte Frau Hopfenstiel,

ich vertrete Frau Naila Sauermilch. Für den Zeitraum vom 1. Mai bis 31. August verlangt sie 10.360,00 EUR Ersatz ihres durch den fehlenden Betreuungsplatz verursachten Verdienstausfalls. Ich bitte um Zahlung bis 16. Oktober 2026. Die Forderung wird für die Mutter persönlich erhoben; das abgeschlossene Förderverfahren ihrer Tochter und dessen Kosten sind davon zu unterscheiden.

Der Betreuungsbedarf war Ihrem Jugendamt seit 12. Januar bekannt. Trotz konkret benannter Arbeitszeiten wurde bis Ende August kein Platz nachgewiesen, der die Rückkehr an den Arbeitsplatz ermöglicht hätte. Meine Mandantin hatte sich weder auf Quendelzwerge festgelegt noch Kindertagespflege abgelehnt. Das Augustangebot umfasste nur drei Stunden an vier Tagen, dazu erhebliche Wege. Eine Ergänzung war nicht verfügbar. Die Arbeitgeberin hat nachvollziehbar erklärt, weshalb daraus keine sinnvolle Teilrückkehr entstehen konnte.

Die Rechnung setzt bei viermal 2.860,00 EUR netto an und zieht 920,00 EUR ersparte Beiträge sowie 160,00 EUR ersparte Arbeitsfahrten ab. Eigenbetreuungszeit, Belastungsentschädigung und fiktive Kosten privater Betreuung werden nicht zusätzlich verlangt. Seit September arbeitet meine Mandantin wieder. Die Familienkasse hat keine ausfallbezogene Ersatzleistung erbracht; das unveränderte Kindergeld wird nicht als solcher Ersatz behandelt.

Die Behauptung eines allgemeinen Fachkräftemangels genügt nicht zur Erklärung der konkreten Dezember- und Februarvorgänge. Bitte sichern Sie die Unterlagen zum Reserveangebot von Frau Schätzlein und den vollständigen Haushaltsumlauf. Die Gemeinde hat die rechtzeitige Anmeldung bereits bestätigt. Primärrechtsschutz wurde rechtzeitig beantragt und nach Erlass der Anordnung weiter betrieben. Eine Einwendung nach § 839 Abs. 3 BGB muss sich deshalb auf eine konkret unterlassene, erfolgversprechende Maßnahme beziehen.

Wir sind zur Besprechung begründeter Einwendungen bereit. Ein Verzicht auf noch zu prüfende zusätzliche Steuerfolgen wird durch die gegenwärtige Bezifferung nicht erklärt. Die Forderung enthält solche Folgen aber auch nicht vorsorglich als pauschalen Aufschlag. Bitte antworten Sie direkt an meine Kanzlei und teilen Sie einen etwaigen Informationsbedarf zusammenhängend mit.

Mit freundlichen Grüßen
Jolanda Knospenlaub
Rechtsanwältin'''),
        doc('14_Landkreis_Stellungnahme.docx','Ihre Forderung vom 24. September – laufende Prüfung','30.09.2026','letter','''Landkreis Mainlaub, Kreisrechtsstelle, Lindenquendelplatz 2, 97076 Würzburg

Rechtsanwältin Jolanda Knospenlaub, Zedernfächerweg 9, 97074 Würzburg

Sehr geehrte Frau Knospenlaub,

Ihr Schreiben ist am 25. September eingegangen. Wir prüfen die Forderung Ihrer Mandantin über 10.360,00 EUR. Eine Zahlung oder ein Anerkenntnis ist damit nicht verbunden. Die von Ihnen bis 16. Oktober gesetzte Frist ist vermerkt. Der Landkreis ist für das Jugendamt zuständig; wir verweisen die Familie nicht zur Anspruchsprüfung an die Gemeinde Quendelbrunn.

Den rechtzeitigen Eingang der Anmeldung, die gerichtliche Inanspruchnahme und die Arbeitsaufnahme zum 1. September stellen wir nach dem bisherigen Aktenabgleich nicht in Abrede. Unterschiedlich beurteilen wir die Ursachen des fehlenden Platzes und die zumutbaren Überbrückungsmöglichkeiten. Zum Angebot Rosenhut erkennen wir, dass der angemeldete Bedarf nicht vollständig abgedeckt war. Wir möchten dennoch die schriftliche Arbeitgeberauskunft sehen, auf die Sie sich zur unmöglichen Teilrückkehr berufen. Eine zusätzliche Betreuung für Freitag oder die Randstunden haben wir nicht benannt; eine solche Möglichkeit behaupten wir heute auch nicht nachträglich.

Das Reserveangebot von Frau Schätzlein wird derzeit mit der Jugendamts- und Haushaltsakte abgeglichen. Es darf nicht ohne ihre damaligen Personalunterlagen als sicher verfügbar behandelt werden. Umgekehrt werden wir die bekannte Verzögerung im Haushaltsumlauf nicht allein mit den erst im Juni eingetretenen Erkrankungen erklären. Die zeitlichen Zusammenhänge sind getrennt zu betrachten. Die Gemeinde haben wir um Erhaltung ihrer Personal- und Ausschreibungsunterlagen gebeten.

Für die Berechnung bitten wir um eine Erläuterung, ob in den 2.860,00 EUR regelmäßige Sonderbestandteile enthalten sind und auf welcher Grundlage die Fahrtkostenersparnis angesetzt wurde. Die Übermittlung einer vollständigen privaten Kontoakte benötigen wir nicht. Ein geeigneter Arbeitgebernachweis und die auf diesen Anspruch beschränkte Budgetaufstellung reichen zunächst aus. Bitte informieren Sie uns, falls andere Stellen auf denselben Ausfall bereits Leistungen erbracht haben.

Unser Kommunalversicherer erhält die zur Prüfung notwendigen Unterlagen. Über die gesetzliche Forderung Ihrer Mandantin antwortet weiterhin der Landkreis. Ob und in welcher Höhe ein Versicherer uns intern entlastet, ist keine Voraussetzung für die Bearbeitung Ihres Anspruchs.

Mit freundlichen Grüßen
Irmtraud Hopfenstiel
Kreisrechtsrätin'''),
        doc('15_Versicherer_an_Landkreis.docx','ML-JH-116 – Entscheidungsvorbereitung und Abgrenzung','05.10.2026','letter','''Kommunalversicherung Mainbogen VVaG, Schadenabteilung, Kornfalterweg 6, 97076 Würzburg

Landkreis Mainlaub, Kreisrechtsstelle, Lindenquendelplatz 2, 97076 Würzburg

Sehr geehrte Frau Hopfenstiel,

nach dem bisherigen Aktenstand besteht ein erhebliches Haftungsrisiko. Der Landkreis kann sich nicht darauf beschränken, keinen eigenen freien Krippenplatz gehabt zu haben. Die konkrete Planung, das Reserveangebot und der Verlauf der Durchsetzung müssen gemeinsam bewertet werden. Eine abschließende Empfehlung über die vollständige Forderung von 10.360,00 EUR geben wir erst nach den ergänzenden Auskünften. Bitte legen Sie dieses Schreiben der Familie nicht als Zahlungszusage vor.

Für die Personalchronologie ist die Dezembermeldung wesentlich. Wir bitten um eine kurze, von der Gemeinde freigegebene Darstellung, weshalb eine erst im Februar veröffentlichte Ausschreibung ausreichend gewesen sein soll. Daneben benötigen wir die Erklärung von Frau Schätzlein zur tatsächlich gesicherten Ersatzkraft und zum letztmöglichen Entscheidungstag. Eine später bekannt gewordene Erkrankung kann den früheren Bearbeitungsstillstand nicht rückwirkend erklären. Sollte es hierfür einen anderen dokumentierten Grund geben, gehört er in die Prüfung.

Der Nettoansatz ist durch die Arbeitgeberbestätigung grundsätzlich prüfbar. Bitte gleichen Sie die Septemberabrechnung mit der hypothetischen Berechnung ab und klären Sie nur die für den Unterschied relevanten Merkmale. Die vollständige Krankheits- oder Personalgeschichte der Mutter ist nicht erforderlich. Die angeführten Ersparnisse sind sachgerecht als Abzüge zu untersuchen. Familienunterstützung ersetzt dagegen nicht ohne Weiteres das Gehalt; eine Darlehensaufnahme ist keine endgültige Ersatzleistung.

Deckungsseitig haben wir eine Arbeitsreserve von 13.000,00 EUR eingerichtet. Die Rückdeckungspriorität von 500.000,00 EUR und die Einzelmeldeschwelle von 250.000,00 EUR werden deutlich unterschritten. Wir werden den Rückversicherer deshalb nicht mit einem personenbezogenen Einzelfallbericht beteiligen. Ihre Selbstbeteiligung von 1.000,00 EUR ändert den gesetzlichen Ersatzanspruch der Mutter nicht. Bei vollständiger Begründetheit bliebe der Mutter ein Anspruch gegen den Landkreis über den gesamten Betrag.

Bitte geben Sie uns bis 12. Oktober die ergänzenden Informationen oder eine genaue Mitteilung, welche Unterlage noch fehlt. Danach können wir eine Vergleichsspanne mit den jeweiligen Beweisrisiken vorlegen. Ein Vergleich ohne belastbare Kenntnis der Reservekapazität würde gerade die entscheidende Frage offenlassen.

Mit freundlichen Grüßen
Vitus Hasenwinkel
Schadenreferent'''),
        doc('16_Klageentwurf_Sauermilch.docx','Klageentwurf Sauermilch gegen Landkreis Mainlaub','05.10.2026','claim','''ENTWURF – NICHT EINGEREICHT

An das Landgericht Würzburg
Ottostraße 5, 97070 Würzburg

## 1 Parteien und Anträge

In dem Rechtsstreit der Naila Sauermilch, Quendelgasse 7, 97299 Quendelbrunn, Klägerin, Prozessbevollmächtigte Rechtsanwältin Jolanda Knospenlaub, Zedernfächerweg 9, 97074 Würzburg,

gegen den Landkreis Mainlaub, vertreten durch Landrat Eberwin Rappel, Lindenquendelplatz 2, 97076 Würzburg, Beklagter,

wird beantragt, den Beklagten zu verurteilen, an die Klägerin 10.360,00 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz ab dem auf die Zustellung der Klage folgenden Tag zu zahlen und die Kosten des Rechtsstreits zu tragen.

Der Streitwert beträgt 10.360,00 EUR. Für den Fall nicht rechtzeitiger Anzeige der Verteidigungsbereitschaft wird bei Vorliegen der gesetzlichen Voraussetzungen ein Versäumnisurteil im schriftlichen Vorverfahren beantragt. Die außergerichtliche Zahlungsfrist endet erst am 16. Oktober. Dieser Entwurf unterstellt weder ihren Ablauf noch eine Einreichung oder Zustellung. Vorgerichtliche Anwaltskosten, Kosten des Förderverfahrens, Zinsaufwendungen für Familiendarlehen und künftige Steuerfolgen sind nicht Gegenstand des Zahlungsantrags.

## 2 Rechtsweg, Zuständigkeit und Anspruchsinhaberin

Die Klägerin verlangt eigenen Verdienstausfall wegen der unterbliebenen Erfüllung des Förderanspruchs ihrer Tochter. Sie klagt nicht als Vertreterin des Kindes auf einen Betreuungsplatz. Für den Amtshaftungsanspruch ist nach Art. 34 Satz 3 GG der ordentliche Rechtsweg eröffnet. Das Landgericht ist gemäß § 71 Abs. 2 Nr. 2 GVG unabhängig vom Streitwert ausschließlich sachlich zuständig. Der Sitz des Beklagten und das für die Bearbeitung verantwortliche Jugendamt liegen in Würzburg; die örtliche Zuständigkeit folgt aus §§ 17, 32 ZPO.

Der Beklagte ist nach Art. 15 AGSG örtlicher Träger der öffentlichen Jugendhilfe. Er handelt insoweit im eigenen Wirkungskreis. Die kreisangehörige Gemeinde Quendelbrunn betreibt eine Einrichtung und wirkt bei der Platzsuche mit; dies ersetzt die gesetzliche Verantwortung des Landkreises nicht. Anstellungskörperschaft der mit der Anspruchserfüllung befassten Jugendamtsbeschäftigten ist der Beklagte. Eine gesamtschuldnerische Haftung der Gemeinde wird mangels eines hierfür hinreichend aufgeklärten eigenständigen Anspruchs nicht mit eingeklagt.

## 3 Bedarf und rechtzeitige Kenntnis

Leni Sauermilch wurde am 24. April 2025 geboren. Sie lebt seit ihrer Geburt mit beiden sorgeberechtigten Eltern in Quendelbrunn im Zuständigkeitsbereich des Beklagten. Der unmittelbar an das Jugendamt gerichtete Antrag vom 12. Januar 2026 bezeichnete den Beginn 1. Mai und die Zeiten Montag bis Freitag 07:45 bis 15:30 Uhr. Die Klägerin erklärte darin ihren vertraglich vereinbarten Wiedereinstieg; der ebenfalls berufstätige Vater konnte die Betreuung zu diesen Zeiten nicht übernehmen. Die Eltern akzeptierten eine geeignete Kindertagespflege und beschränkten sich nicht auf eine Wunscheinrichtung.

Beweis: Bedarfsanmeldung und Eingangsdokumentation, Anlage K1; Bestätigung der Gemeinde, Anlage K7; Zeugnis der Roswitha Knödel, zu laden über den Beklagten, und des Kunibert Quassel, zu laden über Gemeinde Quendelbrunn, Quendelplatz 1, 97299 Quendelbrunn. Zum gemeinsamen Wohnort und zur praktischen Betreuungssituation wird ergänzend das Zeugnis des Anselm Sauermilch unter der Klägeranschrift angeboten.

Die Rückkehrvereinbarung vom 8. Dezember 2025 sah ab 1. Mai eine 30-Stunden-Woche vor Ort in Würzburg vor. Arbeitsbeginn war 08:30 Uhr, Arbeitsende 15:00 Uhr einschließlich einer halbstündigen unbezahlten Pause. Der beantragte Betreuungsumfang berücksichtigte Anfahrt und Übergaben. Ein bereits vereinbarter späterer Wiedereinstieg lag nicht vor. Das tatsächliche Ende der Betreuungslücke am 1. September führte sofort zur Arbeitsaufnahme.

Beweis: Arbeitgeberbestätigung, Anlage K2; ergänzende Nachricht, Anlage K9; Zeugnis der Ottilie Wacker, Mainfaden Medizintechnik GmbH, Fadenlaubweg 14, 97076 Würzburg.

## 4 Pflichtverletzung und konkrete Planung

Leni hatte ab Vollendung ihres ersten Lebensjahres nach § 24 Abs. 2 SGB VIII Anspruch auf Förderung in einer Tageseinrichtung oder Kindertagespflege. Der zeitliche Umfang richtet sich über § 24 Abs. 2 Satz 2 nach dem individuellen Bedarf. Trotz der rechtzeitigen Anmeldung wurde für Mai bis August kein bedarfsdeckender Platz nachgewiesen. Eine bloße Liste bereits erfolglos kontaktierter Einrichtungen erfüllte den Anspruch nicht. Der Beklagte schuldete keinen Erfolg einer bestimmten pädagogischen Wunschgestaltung, wohl aber einen tatsächlich nutzbaren geeigneten Betreuungsplatz.

Die Pflicht besteht nicht lediglich im Umfang vorhandener Kapazität. Die Eltern gehören zum geschützten Personenkreis; ihr betreuungsbedingter Erwerbsausfall kann ersatzfähig sein. Hierzu BGH, Urt. v. 20.10.2016 – Az. III ZR 278/15, BGHZ 212, 303, Rn. 17–19, 24–27 und 34–39; amtlicher Volltext: https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/III_ZS/2015/III_ZR_278-15.pdf?__blob=publicationFile&v=1. Die Aussage ersetzt nicht den Nachweis der einzelnen Haftungsvoraussetzungen im vorliegenden Fall.

Die Akte zeigt konkrete Versäumnisse. Zwei Personalabgänge waren seit Dezember bekannt. Die Ausschreibung erfolgte erst am 15. Februar. Ein am 2. Februar angebotenes Reservekontingent von zwei Plätzen scheiterte nach der bisherigen Dokumentation daran, dass die fachlich am 10. Februar geprüfte Zuschussvorlage bis 27. März im Haushaltsumlauf blieb. Die dafür vorgesehene Ersatzkraft war dann anderweitig gebunden. Die erst im Juni aufgetretenen Erkrankungen erklären weder diese Verzögerung noch das bereits am 1. Mai bestehende Defizit.

Beweis: Kapazitätsvermerk, Anlage K4; Gemeindeauskunft, Anlage K7; Zeugnis der Roswitha Knödel sowie der Walburga Schätzlein, Tagespflege Schätzlein, Lindenkapselweg 8, 97299 Quendelbrunn. Die konkret bezeichnete Zuschussvorlage und ihre Laufvermerke befinden sich beim Beklagten; ihre Vorlage gemäß § 142 ZPO wird angeregt. Ein unbestimmter Zugriff auf sämtliche Haushaltsakten wird nicht beantragt.

Die Klägerin behauptet nicht, dass ihr gerade einer der beiden Reserveplätze zwingend zugewiesen worden wäre. Die Vorgänge belegen zunächst ein erhebliches Organisationsversäumnis und sind für die Entlastung erheblich. Für das Verschulden kommt der Beweis des ersten Anscheins in Betracht; der Beklagte kann ihn durch konkrete Tatsachen erschüttern. Eine verschuldensunabhängige Erfolgshaftung wird nicht geltend gemacht. Vgl. BGH, Urt. v. 20.10.2016 – Az. III ZR 278/15, a.a.O., Rn. 40–42.

## 5 Augustangebot und Schadensminderung

Am 12. August bot der Beklagte ab 17. August Betreuung nur montags bis donnerstags 09:00 bis 12:00 Uhr in der 42 Kilometer entfernten Stelle Rosenhut an. Freitag und Randzeiten blieben offen. Die Klägerin besprach eine Teilrückkehr sofort mit der Arbeitgeberin und fragte nach ergänzender Betreuung. Die Arbeitgeberin konnte für das nach Hin- und Rückfahrt verbleibende Zeitfenster von weniger als zwei Stunden keine sinnvolle Tätigkeit anbieten. Eine zweite Betreuung konnte der Beklagte nicht benennen. Das Angebot war somit kein Ersatz für den angemeldeten Tagesbedarf.

Beweis: Betreuungsprotokoll, Anlage K5; konkretes Angebot, Anlage K8; Arbeitgeberergänzung, Anlage K9; Zeugnis der Ottilie Wacker und der Roswitha Knödel. Die Klägerin lehnt Kindertagespflege nicht grundsätzlich ab. Maßgeblich sind die nachgewiesenen Zeiten und Wege, nicht eine abstrakte Entfernungspauschale. Nach § 254 BGB ist eine wirtschaftlich sinnvolle Teilnutzung zu prüfen; sie bestand hier nach dem aktuellen Belegstand nicht.

Die Familie fragte mehrere Einrichtungen und eine private Vermittlung an. Es gab keinen tatsächlich verfügbaren privaten Ganztagsplatz, den sie allein wegen seines Preises abgelehnt hätte. Anselm arbeitete zu den benötigten Zeiten; eine dauerhafte Schichtänderung wurde nicht angeboten. Die Großeltern konnten keine verlässliche tägliche Betreuung übernehmen. Die Klägerin beantragte ihre unbezahlte Freistellung mit einer kurzfristigen Rückkehrmöglichkeit. Sie schuf daher keine selbständige Bindung an eine unnötig lange Erwerbspause.

## 6 Primärrechtsschutz und weitere Ersatzmöglichkeiten

Der Förderanspruch wurde am 14. April im Namen des Kindes im Eilverfahren geltend gemacht. Nach der stattgebenden Entscheidung vom 28. April folgten die Umsetzungsaufforderung vom 29. April, der Vollstreckungsantrag vom 5. Mai und weitere Durchsetzungsaufforderungen. Der Landkreis stellte trotzdem erst ab September eine geeignete Betreuung bereit. Die Klägerin hat den Eintritt des Ausfalls nicht lediglich abgewartet.

Beweis: Anwaltliche Verlaufsdokumentation, Anlage K6; Beiziehung der dort konkret bezeichneten Verwaltungsgerichtsakte und der elektronischen Eingangsberichte. Der Beklagte kann das von ihm selbst geführte Eilverfahren anhand von Beteiligten, Antragstag und Entscheidungstag eindeutig zuordnen. Das Dokument K6 ist keine amtliche Urkunde über den Inhalt einer Entscheidung. Die Klägerin bietet die Originalverfahrensunterlagen zum Beweis des tatsächlichen Ablaufs an.

Ein Einwand nach § 839 Abs. 3 BGB erfordert eine konkret schuldhaft unterlassene geeignete Maßnahme und deren Schadensvermeidungswirkung. Zur erforderlichen Einzelfallprüfung vgl. OLG Brandenburg, Beschl. v. 20.02.2024 – Az. 2 W 3/24, amtlicher Volltext, Gründe unter 2 c: https://gerichtsentscheidungen.brandenburg.de/gerichtsentscheidung/24287. Die dortige Entscheidung im Prozesskostenhilfeverfahren ersetzt keine Sachentscheidung hier; insbesondere wird das dort zusätzlich angewandte Staatshaftungsgesetz nicht auf Bayern übertragen.

Ein anderweitiger durchsetzbarer Ersatzanspruch im Sinne von § 839 Abs. 1 Satz 2 BGB besteht nach dem gegenwärtigen Sachstand nicht. Die Arbeitgeberin schuldete während der vereinbarten unbezahlten Freistellung kein Entgelt. Ein privater Betreuungsvertrag mit einem schadensersatzpflichtigen Anbieter wurde nicht geschlossen. Familiendarlehen sind rückzahlbar und ersetzen keinen Schaden endgültig. Erhielte die Klägerin später eine auf denselben Ausfall bezogene Ersatzleistung, wäre diese offenzulegen und anzurechnen, soweit rechtlich geboten.

## 7 Ursächlichkeit und bezifferter Schaden

Bei rechtzeitiger Betreuung hätte die Klägerin die konkret vereinbarte Arbeit ab 1. Mai aufgenommen. Die Arbeitgeberin hatte Arbeit und Vergütung bereitgehalten. Eine Vertretung verhinderte die Rückkehr nicht. Der tatsächliche Beginn am 1. September stützt diese Prognose. Dass die Klägerin nicht arbeitete, beruhte auf der Betreuungslücke; eine Krankheit, Kündigung oder davon unabhängige private Erwerbspause ist nicht ersichtlich. Dies ist nach §§ 249, 252 BGB und § 287 ZPO anhand der konkreten Beschäftigungstatsachen zu bewerten.

Vier Monatsauszahlungen von jeweils 2.860,00 EUR ergeben 11.440,00 EUR. Davon werden vier ersparte Betreuungsbeiträge von je 230,00 EUR, zusammen 920,00 EUR, sowie viermal 40,00 EUR zusätzliche Arbeitsfahrtkosten, zusammen 160,00 EUR, abgezogen. Es verbleiben 10.360,00 EUR, entsprechend 2.590,00 EUR für jeden der vier Monate. Die Anspruchssumme verteilt sich damit eindeutig auf Mai, Juni, Juli und August; sie ist kein unbestimmter Teilbetrag aus verschiedenen Forderungen.

Beweis: Berechnung und Budgetangaben, Anlage K3; Arbeitgeberunterlagen, Anlagen K2 und K9; Zeugnis der Ottilie Wacker zum Lohnlauf und des Anselm Sauermilch zu den tatsächlichen Haushaltsausgaben. Die Septemberabrechnung dient der Kontrolle des unveränderten Nettoansatzes. Zusätzliche Steuerfolgen einer späteren Ersatzleistung werden derzeit nicht hochgerechnet. Ersparte variable Kosten werden abgezogen; ohnehin weiterlaufende fixe Haushaltskosten werden nicht noch einmal als Schaden verlangt.

Elterngeld endete vor dem Anspruchszeitraum. Ausfallbezogene Sozialleistungen und Versicherungszahlungen gab es nicht. Unverändertes Kindergeld wäre in beiden Verläufen angefallen. Der Betrag enthält weder Bruttosozialbeiträge noch fiktive Ersatzbetreuungskosten neben dem Nettoverdienstausfall. Kosten des Kindes oder hypothetische Genugtuung für die Familie sind nicht Gegenstand der Klage.

## 8 Vorverfahren, Zinsen und Schluss

Mit Schreiben vom 24. September, eingegangen am 25. September, wurde die Zahlung bis 16. Oktober verlangt, Anlage K10. Der Beklagte kündigte am 30. September weitere Prüfungen an und erhob Einwendungen zu Organisation und Schadensminderung, Anlage K11. Diese werden mit der vorliegenden konkreten Chronologie beantwortet. Eine Zahlung ist nicht erfolgt. Prozesszinsen werden gemäß §§ 291, 288 Abs. 1 BGB erst ab dem Tag nach tatsächlicher Zustellung beantragt.

Die interne Deckung des Beklagten begrenzt den gesetzlichen Anspruch der Klägerin nicht. Weder Selbstbehalt noch Rückdeckungspriorität sind gegen sie einzuwenden. Ein Versicherer, ein Ausgleichsverband oder ein Rückversicherer wird nicht ohne eigenständige Anspruchsgrundlage verklagt. Die Klägerin bleibt zu einer Einigung auf der Grundlage der belegten Monatsdifferenzen und konkret benannter Beweisrisiken bereit.

Jolanda Knospenlaub
Rechtsanwältin
Entwurfsfassung ohne Unterschrift und ohne Einreichung'''),
    ],
)]


CASES.append(dict(
    slug='akha-wuerzburg-glatteis',
    title='Glatteis – nachgefundene Deckung und Streit um den Sturzpunkt',
    summary='Vier zusätzliche Korrespondenzen zwischen Rechtsstelle, Bauhof und Kommunalversicherer klären 1.748,75 EUR Forderung, Selbstbehalt, Beweissicherung und fehlenden Rückdeckungsbedarf.',
    is_new=False,
    notes='Die vier neuen Korrespondenzen spielen am Nachmittag des 05.10.2026 nach Erstellung des bestehenden Klageentwurfs. Erst jetzt aufgefundene Versicherungsdaten widersprechen nicht dem früheren Hinweis, dass keine Deckungsunterlagen vorliegen. Alle neu ergänzten Vertragsangaben sind ausschließlich fiktive Szenarioannahmen und keine tatsächlichen AKHA-Regeln. Das städtische Prüfmandat und sämtliche bisherigen Originale bleiben erhalten.',
    core=['schriftverkehr-und-klage/16_Klageentwurf.docx',f'{FOLDER}/01_Stadt_an_Kommunalversicherer.docx'],
    exhibits=[],
    attachments={
        '03_Bauhof_Beweissicherung.eml':['04_Einsatzprotokoll.docx','schriftverkehr-und-klage/12_Disposition_Ergaenzung.eml'],
        '04_Versicherer_an_Rechtsstelle.eml':[f'{FOLDER}/02_Versicherer_Deckungsantwort.pdf'],
    },
    documents=[
        doc('01_Stadt_an_Kommunalversicherer.docx','Zeisig – neue Deckungsunterlagen und konkrete Prüffragen','05.10.2026','letter','''Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Kommunalversicherung Mainbogen VVaG, Kornfalterweg 6, 97076 Würzburg

Sehr geehrter Herr Hasenwinkel,

unsere Vertragsverwaltung hat heute gegen 14:00 Uhr den Vertrag KM-W-2026 zugeordnet. Bis dahin lagen der Rechtsstelle und der beauftragten Kanzlei keine Versicherungsunterlagen für den Sturzfall Zeisig vor. Wir melden den Vorgang jetzt zur Deckungsprüfung nach und bitten um ausdrückliche Mitteilung, welche Bedeutung Sie dem Meldezeitpunkt beimessen. Wir stellen den bisherigen Kenntnisstand nicht nachträglich anders dar.

Die Forderung beträgt nach dem ergänzten Anwaltsschreiben 148,75 EUR Haushaltshilfe und ein mit 1.600,00 EUR bewertetes Schmerzensgeld. Die Anspruchstellerin behauptet keinen Dauerschaden. Die Frist für unsere Antwort endet am 12. Oktober. Eine Zahlung oder ein Anerkenntnis ist nicht erfolgt. Die Kanzlei soll zunächst das Haftungsrisiko prüfen; ein gerichtliches Verfahren ist nicht eingeleitet.

Der Bauhof kann die Erststreuung um 05:54 Uhr und die Nachstreuung um 07:52 Uhr zeitlich belegen. Die entscheidende neue Meldung ging um 07:20 Uhr ein. Ein verfügbarer Handtrupp hätte nach der ergänzten Aussage möglicherweise vor dem Sturz um 07:42 Uhr tätig werden können. Die frühere pauschale Annahme, sämtliche Kräfte seien am Seniorenhaus gebunden gewesen, trägt deshalb nicht ohne weitere Prüfung. Andererseits kann die Zeugin den letzten Fußkontakt wegen eines Lieferwagens nicht sicher sehen. Dieser Unterschied zwischen Fahrbahn und Gehweg bleibt wesentlich.

Bitte prüfen Sie Abwehrdeckung und Selbstbehalt getrennt von der Frage, ob der behauptete Sturzpunkt bewiesen werden kann. Wir bitten weder um eine vollständige Ablehnung wegen einer früheren Streufahrt noch um eine Zahlung allein wegen der Einsatzlücke. Bei einer möglichen Vergleichsspanne müssen Aussagegrenzen, Verletzungsverlauf und nachgewiesene Hilfe berücksichtigt werden. Für eine Beteiligung des Landkreises besteht kein tatsächlicher Anknüpfungspunkt; der Abschnitt ist eine Gemeindestraße der kreisfreien Stadt.

Wir sichern Telefonblatt, Fahrzeugdaten und Schichtbuch. Bitte benennen Sie die noch benötigten Informationen gebündelt. Medizinische Unterlagen werden nur soweit für diesen Anspruch erforderlich weitergegeben. Einen personenbezogenen Rückversichererbericht bitten wir bei dieser begrenzten Forderung nicht vorsorglich anzulegen.

Mit freundlichen Grüßen
Gertraud Holler
Rechtsstelle'''),
        doc('02_Versicherer_Deckungsantwort.docx','Zeisig – vorläufige Deckung und Abwehrführung','05.10.2026','letter','''Kommunalversicherung Mainbogen VVaG, Kornfalterweg 6, 97076 Würzburg

Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

wir bestätigen Ihre heutige Nachmeldung unter der Schadennummer MB-W-26113. Der erfasste Vertrag umfasst gesetzliche Haftpflichtansprüche aus dem kommunalen Winterdienst mit einer Versicherungssumme von 5.000.000,00 EUR für Personen- und Sachschäden je Schadenereignis. Der vereinbarte Selbstbehalt beträgt 500,00 EUR; erforderliche Abwehrkosten werden nach dem uns vorliegenden Vertragsauszug außerhalb dieses Selbstbehalts behandelt. Das ist keine Entscheidung über die Berechtigung der Forderung von Frau Zeisig.

Die späte Zuordnung der Vertragsunterlagen prüfen wir gesondert. Eine Leistungsfreiheit wird aus dem Datum Ihrer Meldung allein nicht abgeleitet. Bitte teilen Sie mit, wann die Vertragsverwaltung erstmals einen Versicherungsbezug erkannte, weshalb die Meldung unterblieb und ob dadurch eine konkrete Aufklärungsmöglichkeit verloren ging. Der Unfall vom Januar ist lange her; gerade deshalb sollten unveränderte ursprüngliche Unterlagen und erst jetzt entstandene Ergänzungen sauber unterschieden werden.

Haftungsseitig sehen wir zwei getrennte Beweisfragen: War der Sturz noch auf der Fahrbahnquerung, und hätte eine zumutbare Reaktion auf die neue Meldung ihn verhindert? Die Zeugin kann zur eigenen Rutschbeobachtung etwas beitragen, aber die verdeckten Füße der Geschädigten nicht nachträglich sichtbar machen. Der verfügbaren Mannschaft kommt Bedeutung zu, ohne dass eine berechnete Ankunftszeit bereits den tatsächlichen Streuerfolg beweist. Bitte lassen Sie die Erinnerungen einzeln dokumentieren und nicht in einer gemeinsamen Formulierung angleichen.

Wir setzen vorläufig eine Reserve von 3.200,00 EUR einschließlich Abwehrkosten. Unsere Vertragsakte sieht eine personenbezogene Rückdeckungsmeldung erst ab 250.000,00 EUR erwarteter Gesamtbelastung vor; der vorliegende Vorgang erreicht diese Schwelle nicht. Es gibt deshalb keinen Einzelfallbrief an einen Rückversicherer. Die Reserve und diese interne Einordnung sind gegenüber Frau Zeisig weder ein Anerkenntnis noch ein Kürzungsgrund.

Bitte stimmen Sie den Antwortentwurf bis 8. Oktober mit uns ab. Ein Vergleich bedarf einer konkreten Beschlussvorlage mit Betrag und Abgeltungsumfang. Bei inzwischen ausgeheilten Beschwerden soll keine pauschale Abgeltung unbekannter Dauerschäden beiläufig in einen kurzen Zahlungsbrief geraten. Eine externe Erklärung ist mit diesem Schreiben noch nicht freigegeben.

Mit freundlichen Grüßen
Vitus Hasenwinkel
Schadenreferent'''),
        doc('03_Bauhof_Beweissicherung.eml','W-12: Originalprotokoll und spätere Ergänzung bleiben getrennt','2026-10-05T15:30:00+02:00','email','''Sehr geehrte Frau Holler,

ich habe das Einsatzprotokoll vom Januar und meine Ergänzung zur Disposition beigefügt. Die Dateien bleiben in ihren bisherigen Fassungen erhalten. Das Telefonblatt liegt im Winterdienstordner; Frau Seufert hat bestätigt, dass sie dort nach dem Unfall nichts ergänzt hat. Der spätere Besprechungsvermerk vom 14. Januar ist ein anderes Dokument und soll nicht als Eintrag von 07:20 Uhr ausgegeben werden.

Huriye Demir und Hilmar Engelbrecht können die Rückkehr um 07:18 Uhr sowie den fahrbereiten Kleintransporter erklären. Beide haben heute ausdrücklich gesagt, dass die zwölf Minuten Anfahrtszeit eine Erfahrungsangabe sind. Niemand hat die Januarbedingungen nachgestellt. Ob ein um 07:35 Uhr beginnender Streueinsatz die konkrete Stelle bis 07:42 Uhr sicher gemacht hätte, können wir nicht aus einer Sommerprobefahrt ableiten.

Die Frau aus der Bäckerei war nach unserer Rechnungsliste Ottilie Hasel. Ich habe sie noch nicht für eine gemeinsame Besprechung mit den Beschäftigten eingeladen. Falls ihre Aussage benötigt wird, soll sie ihre Erinnerung selbst wiedergeben, bevor wir ihr unsere Zeitrekonstruktion vorlegen. Ein Unfallfoto ist weiterhin nicht gefunden worden. Bitte teilen Sie dem Versicherer diese Grenzen mit; wir möchten weder eine technische Messung vortäuschen noch eine vorhandene Personalreserve verschweigen.

Freundliche Grüße
Ottmar Dörflein''','Ottmar Dörflein <bauhof@wuerzburg-fallakten.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        doc('04_Versicherer_an_Rechtsstelle.eml','MB-W-26113: Antwortfrist und mögliche Gesprächslinie','2026-10-05T16:40:00+02:00','email','''Sehr geehrte Frau Holler,

anbei unser heutiges Deckungsschreiben. Für die Antwort an Frau Eichenlaub schlagen wir vor, die bestätigten Einsatzzeiten ausdrücklich zu nennen und den Sturzpunkt als offen zu behandeln. Eine Formulierung, wonach die Klägerin sicher erst auf dem Gehweg gestürzt sei, wäre mit der vorhandenen Zeugin nicht belegt. Ebenso wenig sollte die berechnete Handtruppzeit als sicher verhinderter Unfall dargestellt werden.

Die Haushaltshilfe von 148,75 EUR ist nach Rechnung und Zahlung nachvollziehbar, muss aber zum konkreten Verletzungsbedarf passen. Beim mit 1.600,00 EUR bewerteten Schmerzensgeld sind Dauer, Beschwerden und Ausheilung maßgeblich. Einen pauschalen Prozentsatz wegen Winterwetters wenden wir nicht an. Die Fotos der Schuhsohlen, nach denen gelegentlich gefragt wird, liegen nicht vor; das darf nicht als bewiesenes ungeeignetes Schuhwerk behandelt werden.

Bitte senden Sie den Kanzleientwurf vor der angekündigten Rückmeldung am 12. Oktober. Wenn die Stadt ein Vergleichsgespräch führen möchte, genügt zunächst eine interne Spanne mit kurzer Begründung. Die 500,00 EUR Selbstbehalt beeinflussen Ihre interne Belastung, nicht den Anspruch der Geschädigten. Wir beteiligen bei dieser Reserve keinen Rückversicherer mit personenbezogenen Unterlagen. Die konkrete Zuständigkeit verbleibt bei Ihnen und unserem Schadenreferat; eine zusätzliche Anfrage an einen Landkreis würde hier keinen offenen Sachpunkt klären.

Mit freundlichen Grüßen
Vitus Hasenwinkel''','Vitus Hasenwinkel <schaden@mainbogen-vers.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
    ],
))


CASES.append(dict(
    slug='akha-wuerzburg-antragsbearbeitung',
    title='Kaffee Nouri – kleiner Geldbetrag, sauber getrennte Verantwortlichkeit',
    summary='Der Versicherungsabgleich trennt 119 EUR zusätzliche Stornokosten, ursprüngliche Wagenmiete, amtliche Auskunft, Selbstbehalt und Kosten einer möglichen Amtshaftungsklage.',
    is_new=False,
    notes='Zusatzkorrespondenz am Nachmittag des 05.10.2026 nach dem bestehenden Anspruchs- und Klageentwurf. Versicherungsdaten werden erst jetzt zugeordnet; ihre Zahlen sind fiktive Szenarioannahmen, keine AKHA-Bedingungen. Die Forderung bleibt auf 119 EUR begrenzt. Keine rückwirkende Änderung der ursprünglichen Stornobedingungen oder neue Vertretung der Anspruchstellerseite.',
    core=['schriftverkehr-und-klage/16_Klageentwurf.docx',f'{FOLDER}/01_Stadt_Meldung_Nouri.docx'],
    exhibits=[],
    attachments={
        '03_Sachgebiet_an_Rechtsstelle.eml':['04_Registerauszug.docx','07_Sachgebietsleitung.docx'],
        '04_Versicherer_Selbstbehalt.eml':[f'{FOLDER}/02_Versicherer_Nouri.pdf'],
    },
    documents=[
        doc('01_Stadt_Meldung_Nouri.docx','Nouri – Nachmeldung eines Auskunfts- und Bearbeitungsfehlers','05.10.2026','letter','''Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Kommunalversicherung Mainbogen VVaG, Kornfalterweg 6, 97076 Würzburg

Sehr geehrter Herr Hasenwinkel,

die Vertragsverwaltung hat uns heute Nachmittag erstmals den Einschluss reiner Vermögensschäden im Vertrag KM-W-2026 zugänglich gemacht. Wir melden hiermit den Vorgang Nouri nach. Die ursprüngliche Forderung betrug 238,00 EUR Wagenmiete. Nach der ergänzten Prüfung verlangt der anwaltliche Entwurf nur noch 119,00 EUR, die durch die nicht genutzte Sonderkulanz am 18. Juni zusätzlich verloren gegangen sein sollen. Eine Erstattung wurde nicht zugesagt und nicht gezahlt.

Der Antrag auf Sondernutzung betraf den 20. und 21. Juni, im Register standen versehentlich Julidaten. Neben diesem Bearbeitungsfehler geht es um eine telefonische Auskunft am Morgen des 18. Juni. Die reguläre Stornofrist war am Vorabend bereits abgelaufen. Eine erst an diesem Morgen erteilte Auskunft kann diese frühere Entscheidung nicht verursacht haben. Neu belegt ist aber ein gesondertes Kulanzangebot der Vermieterin bis 12:00 Uhr. Ob die Auskunft dazu führte, dieses konkrete Angebot ungenutzt verstreichen zu lassen, ist gesondert zu prüfen.

Bitte behandeln Sie die Kulanz nicht als nachträglich umgeschriebene Mietbedingung. Die Vermieterin hat den damaligen Nachrichtenverlauf erst jetzt in einer E-Mail wiedergegeben. Eine technische Originalausleitung des Geschäftstelefons liegt nicht in der Akte. Die Sachbearbeiterin erinnert sich an eine rechtzeitige Vorlage, Herr Nouri an eine zugesagte Entscheidung am Folgetag. Eine gleichzeitige Telefonnotiz gibt es nicht.

Wir bitten um Mitteilung zu Abwehrdeckung und Selbstbehalt. Der geringe Forderungsbetrag macht die Amtshaftungsprüfung nicht entbehrlich, rechtfertigt aber auch keinen aufwendigen Rundlauf durch weitere Versicherungsstellen. Ein Vergleich wäre wirtschaftlich denkbar, darf jedoch nicht als Eingeständnis eines von vornherein gebundenen Genehmigungsanspruchs formuliert werden. Für die Sondernutzung war die Stadt selbst zuständig; ein Landkreis hatte keine Entscheidung zu treffen.

Die Antwortfrist endet am 12. Oktober. Bitte teilen Sie uns bis 8. Oktober mit, ob Sie zusätzliche Belege benötigen. Den rechtlichen Entwurf erarbeitet die für die Stadt beauftragte Kanzlei. Das ursprüngliche Mandat wird nicht auf einen Prozess oder ein Schuldanerkenntnis erweitert.

Mit freundlichen Grüßen
Gertraud Holler'''),
        doc('02_Versicherer_Nouri.docx','Nouri – Deckung, Kleinschaden und zweifache Kausalitätsprüfung','05.10.2026','letter','''Kommunalversicherung Mainbogen VVaG, Kornfalterweg 6, 97076 Würzburg

Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

wir erfassen den Vorgang unter MB-W-26238. Der uns heute zugeordnete Vertragsauszug sieht für reine Vermögensschäden aus fahrlässiger Amtspflichtverletzung eine Versicherungssumme von 1.000.000,00 EUR und einen Selbstbehalt von 1.000,00 EUR je Schadenereignis vor. Die Hauptforderung von 119,00 EUR liegt vollständig innerhalb dieses Selbstbehalts. Erforderliche Abwehrkosten werden gesondert behandelt. Ob diese entstehen sollen, ist im Verhältnis zu einer begründeten Einigung wirtschaftlich abzuwägen.

Wir bestätigen keine gesetzliche Haftung allein aufgrund des falschen Registereintrags. Für den zusätzlichen Verlust aus der Kulanz ist die tatsächliche Entscheidungssituation am 18. Juni maßgeblich. Bitte klären Sie, ob Herr Nouri das bis 12:00 Uhr geltende Angebot kannte, wann er mit Ihrer Mitarbeiterin sprach und weshalb er nach dem Gespräch nicht absagte. Die positive interne Einschätzung des Vorhabens belegt noch keine erteilte Erlaubnis. Umgekehrt darf der Vorgang nicht allein mit dem Satz abgelehnt werden, es habe keinen unterschriebenen Bescheid gegeben: Auch eine konkrete unrichtige Auskunft kann für eine Vermögensentscheidung erheblich sein.

Der Anspruchsteller hatte Eilrechtsschutz erwähnt. Für § 839 Abs. 3 BGB reicht dieser Hinweis als Abwehrargument noch nicht. Es muss eine zumutbare Maßnahme ermittelt werden, die den gerade streitigen Verlust hätte verhindern können. Ein fiktiver Eilbeschluss binnen weniger Stunden darf dabei nicht selbstverständlich unterstellt werden. Diese Frage soll die Kanzlei ausdrücklich im Verhältnis zur eigenständigen Kulanzentscheidung behandeln.

Eine Meldung des Einzelfalls an einen Rückversicherer ist nicht vorgesehen. Der erfasste Rückdeckungsvertrag verlangt personenbezogene Einzelberichte erst ab einer erwarteten Belastung von 250.000,00 EUR; ein möglicher Anspruch von 119,00 EUR fällt nicht darunter. Auch eine behauptete Serienzugehörigkeit wird ohne passende Klausel und tatsächliche Prüfung nicht gebildet.

Bitte legen Sie uns eine knappe Entscheidungsvorlage mit Beweisrisiko, möglichem Einigungsbetrag und Kostenvergleich vor. Eine Zahlung soll, falls beschlossen, ihren konkreten Anlass bezeichnen und keine pauschale Rechtsbehauptung zur gesamten behördlichen Bearbeitung enthalten. Die Frist der Gegenseite bleibt durch unseren internen Schriftwechsel unberührt.

Mit freundlichen Grüßen
Vitus Hasenwinkel'''),
        doc('03_Sachgebiet_an_Rechtsstelle.eml','Nouri: Register und Erinnerungsgrenzen zum Telefonat','2026-10-05T15:25:00+02:00','email','''Sehr geehrte Frau Holler,

ich habe den Registerauszug und meine Notiz vom 24. Juni beigefügt. Die beiden Dokumente zeigen die falschen Julidaten und unsere positive örtliche Vorprüfung. Sie enthalten keinen unterschriebenen Bescheid. Frau Merk konnte die Erlaubnis nicht selbst erteilen; meine Unterschrift wäre erforderlich gewesen.

Zum Telefonat am 18. Juni bleibt Frau Merk bei ihrer Erinnerung, sie habe eine rechtzeitige Vorlage angekündigt. Sie kann heute weder die genaue Minute noch eine wörtliche Aussage „morgen bekommen Sie den Bescheid“ bestätigen. Sie hat auch nicht notiert, dass ihr die um 12:00 Uhr ablaufende neue Kulanz bekannt gewesen wäre. Bitte schreiben Sie deshalb nicht, sie habe diese Frist sicher gewusst. Herr Nouris abweichende Erinnerung muss gesondert geprüft werden.

Der am 19. Juni dokumentierte Zeitdruck und die zu diesem Zeitpunkt verstrichene reguläre Stornofrist werden durch das erst jetzt bestätigte Sonderangebot nicht falsch. Es sind zwei verschiedene Fristen. Ich hätte bei richtiger Wiedervorlage unterschreiben können; die damals dokumentierte Sachlage enthält kein entgegenstehendes Nutzungshindernis. Daraus kann ich aber keine sichere Aussage ableiten, wann ein Gericht auf einen Antrag am 18. Juni entschieden hätte. Bitte erhalten Sie diese Trennung auch in der Versichererkorrespondenz.

Freundliche Grüße
Eberhard Abelein''','Eberhard Abelein <strassenrecht@wuerzburg-fallakten.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        doc('04_Versicherer_Selbstbehalt.eml','MB-W-26238: 119 EUR Anspruch sind nicht 119 EUR Prozesskosten','2026-10-05T16:20:00+02:00','email','''Sehr geehrte Frau Holler,

anbei unser Deckungsschreiben. Der Selbstbehalt ist eine interne Vertragsfrage. Bitte verwenden Sie ihn nicht in einem Ablehnungsschreiben an Herrn Nouri: Er beantwortet nicht, ob eine falsche Auskunft zum Verlust der Kulanz führte. Ebenso wenig sollten Sie die Landgerichtszuständigkeit als Argument gegen die kleine Forderung verwenden. Gerade bei Amtshaftung kann ein sehr geringer Streitwert mit erheblichen Vertretungskosten zusammentreffen.

Wir empfehlen, vor einem Prozess über die 119,00 EUR die Erklärung der Vermieterin konkret abzugleichen. Entscheidend ist, ob sie die Zahlung bei einer Absage bis 12:00 Uhr wirklich erstattet hätte und ob Herr Nouri bei zutreffender Auskunft rechtzeitig abgesagt hätte. Dass er ursprünglich hoffte, den Wagen nutzen zu können, schließt einen späteren anderen Entschluss nicht automatisch aus. Seine eigene Anhörung ersetzt allerdings nicht ohne Weiteres den Nachweis sämtlicher Gesprächsinhalte.

Bitte schicken Sie uns keine vollständige Telefonanlage oder Daten anderer Antragsteller. Die auf diesen Vorgang bezogenen Einträge und die vorhandenen E-Mails reichen für den nächsten Schritt. Eine Zahlung bleibt bis zur städtischen Entscheidung offen. Sollten Sie aus wirtschaftlichen Gründen vergleichen wollen, benennen Sie die bereinigte Forderung und den konkreten Abgeltungsumfang. Wir halten keine personenbezogene Rückdeckungsmeldung vor und haben keine andere Körperschaft um Kostenbeteiligung gebeten.

Mit freundlichen Grüßen
Vitus Hasenwinkel''','Vitus Hasenwinkel <schaden@mainbogen-vers.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
    ],
))


CASES.append(dict(
    slug='akha-wuerzburg-baugenehmigung',
    title='Baugenehmigung Adebayo – Gewinnrechnung statt doppelter Mietansätze',
    summary='Die spätere Versicherungsakte stellt die neue Forderung von 860 EUR, die früheren Mietansätze, Genehmigungsverlauf und verwaltungsgerichtlichen Rechtsschutz gegenüber.',
    is_new=False,
    notes='Nachgefundene Versicherungsunterlagen und ergänzende Korrespondenz am Nachmittag des 05.10.2026. Alle Deckungsangaben sind fiktive Szenarioannahmen. Die kreisfreie Stadt bleibt zuständige Bauaufsichtsbehörde; ein Landkreis wird nicht als angeblich zuständige Genehmigungsstelle eingeschoben. Die alte Forderungsfassung bleibt sichtbar, die neue Forderung beträgt unverändert 860 EUR.',
    core=['schriftverkehr-und-klage/16_Klageentwurf.docx',f'{FOLDER}/01_Stadt_Meldung_Adebayo.docx'],
    exhibits=[],
    attachments={
        '03_Bauaufsicht_Chronologie.eml':['05_Bearbeitungsvermerk.docx'],
        '04_Versicherer_Rechnung.eml':['schriftverkehr-und-klage/13_Finanzierungsvergleich.eml',f'{FOLDER}/02_Versicherer_Adebayo.pdf'],
    },
    documents=[
        doc('01_Stadt_Meldung_Adebayo.docx','Adebayo – neue Anspruchsberechnung und Deckungszuordnung','05.10.2026','letter','''Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Kommunalversicherung Mainbogen VVaG, Kornfalterweg 6, 97076 Würzburg

Sehr geehrter Herr Hasenwinkel,

nach der heutigen erstmaligen Zuordnung unserer Versicherungsunterlagen melden wir den Vorgang Adebayo zum Vertrag KM-W-2026. Die bislang ohne Deckungsunterlagen arbeitende Rechtsstelle hat die ursprüngliche Mietkostenforderung inzwischen mit der nachgereichten Kundenbestätigung abgeglichen. Der aktuelle gegnerische Entwurf verlangt 860,00 EUR. Die früheren Unterlagen werden nicht ersetzt; die Berechnungsänderung soll für die Prüfung nachvollziehbar bleiben.

Die Klägerseite setzt jetzt 1.080,00 EUR entgangenes Beratungshonorar an, zieht 180,00 EUR ersparte variable Kosten und 80,00 EUR hypothetische reguläre Kreditzinsen ab und addiert 40,00 EUR tatsächlich belastete Bereitstellungszinsen. Die Miete wird nicht zusätzlich verlangt, weil sie auch bei rechtzeitiger Genehmigung angefallen wäre. Bitte beurteilen Sie den neuen Anspruch auf dieser Grundlage und nicht auf der früheren Summe bloßer Raumkosten.

Unsere Bauaufsicht hatte aus einem anderen Vorgang Maschinen- und Lieferverkehr übernommen, obwohl ein Büro mit zwei Arbeitsplätzen beantragt war. Der Fehler wurde nach der Verpflichtungsklage erkannt. Die anschließende erneute Ortsprüfung ergab keine neue Anforderung. Gleichwohl ist noch zu klären, wann eine fehlerfreie Bearbeitung einschließlich Zeichnung abgeschlossen gewesen wäre, wann Handwerker und Ausstattung bereitgestanden hätten und ob der betreffende Kundenauftrag dann tatsächlich durchgeführt worden wäre. Die spätere Genehmigung allein beantwortet diese Kausalitätsfragen nicht.

Die Stadt ist als kreisfreie Stadt selbst untere Bauaufsichtsbehörde. Das Landratsamt war an dieser Entscheidung nicht beteiligt. Wir möchten deshalb weder dort eine fingierte Genehmigungszuständigkeit abfragen noch eine weitere Körperschaft allein wegen der allgemeinen Bezeichnung „Bauamt“ in die Schadenakte aufnehmen. Die Kanzlei prüft für uns Haftung und den rechtzeitig ergriffenen verwaltungsgerichtlichen Rechtsschutz.

Bitte bestätigen Sie den Umgang mit reinen Vermögensschäden, Selbstbehalt und Abwehrkosten. Bis zum 12. Oktober müssen wir der gegnerischen Anwältin antworten. Keine Zahlung wurde veranlasst. Eine spätere Einigung müsste ausdrücklich den geltend gemachten Zeitraum und die hier bereinigte Gewinnrechnung erfassen, ohne die Kosten des anderen Gerichtsverfahrens stillschweigend mitzuentscheiden.

Mit freundlichen Grüßen
Gertraud Holler'''),
        doc('02_Versicherer_Adebayo.docx','Adebayo – Haftungsprüfung und fehlende Großschadenmeldung','05.10.2026','letter','''Kommunalversicherung Mainbogen VVaG, Kornfalterweg 6, 97076 Würzburg

Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Sehr geehrte Frau Holler,

wir führen Ihre Nachmeldung unter MB-W-26086. Der Vertragsauszug erfasst fahrlässig verursachte reine Vermögensschäden aus der Tätigkeit der städtischen Bauaufsicht bis 1.000.000,00 EUR je Schadenereignis. Die vereinbarte Selbstbeteiligung beträgt 1.000,00 EUR. Bei einer vollständig berechtigten Hauptforderung von 860,00 EUR läge diese damit vollständig bei der Stadt. Erforderliche Abwehrkosten sind gesondert zu behandeln. Der Selbstbehalt trifft keine Aussage über die Berechtigung der Forderung.

Nach dem Bearbeitungsvermerk ist der übernommene Sachverhalt zum Maschinenbetrieb ein konkreter Fehler, keine bloß vertretbare unterschiedliche Auslegung des wirklichen Bürovorhabens. Für die Frage des verursachten Geldschadens sind jedoch weitere Schritte erforderlich. Der Zeitpunkt der Entscheidungsreife ist nicht automatisch der Zeitpunkt einer zugestellten Genehmigung. Die Klägerseite muss erläutern, ab wann sie den Raum nach genehmigter Wandöffnung tatsächlich hätte nutzen können und weshalb der geltend gemachte Auftrag gerade in dem verlorenen Zeitraum ausgefallen ist.

Die neue Rechnung ist gegenüber einer Addition von Miete und vollem Honorar methodisch besser abgegrenzt. Sie darf trotzdem nicht ungeprüft als bewiesen übernommen werden. Bitte kontrollieren Sie die 180,00 EUR variablen Kosten, die tatsächliche Bindung des Kunden und den angesetzten hypothetischen Kreditzins. Die 40,00 EUR Bereitstellungszinsen sind belegt; daneben auch noch dieselben regulären Zinsen als Schaden zu verlangen, würde tatsächlichen und hypothetischen Verlauf vermischen. Die Miete läuft in beiden Verläufen und bildet keinen zusätzlichen Differenzposten.

Eine personenbezogene Meldung an einen Rückversicherer ist bei dieser Belastung nicht vorgesehen. Die vertragliche Einzelmeldeschwelle liegt bei 250.000,00 EUR. Ein Rückdeckungsbedarf darf weder aus der Behördenbezeichnung noch aus einem grundsätzlich bedeutsamen Bearbeitungsfehler hergeleitet werden. Es gibt zudem keinen Anlass, Gesundheitsdaten oder Unterlagen anderer Bauherren in diesen Vorgang einzubeziehen.

Bitte legen Sie eine kurze Entscheidungsvorlage mit zwei konkret datierten Bearbeitungsverläufen und dem daraus folgenden Betrag vor. Die verwaltungsgerichtliche Kostenfrage bleibt getrennt. Vor einer vergleichsweisen Zahlung ist zu bestimmen, ob ausschließlich die vorliegende Hauptforderung erledigt werden soll. Eine pauschale Abgeltung aller Ansprüche aus sämtlichen Bauverfahren wäre dafür zu weit.

Mit freundlichen Grüßen
Vitus Hasenwinkel'''),
        doc('03_Bauaufsicht_Chronologie.eml','Adebayo: Zeichnungstermine und fehlender Gegenbeleg','2026-10-05T15:45:00+02:00','email','''Sehr geehrte Frau Holler,

anbei nochmals mein Bearbeitungsvermerk vom 28. Juli. Ich kann bestätigen, dass die Ortsprüfung vom 21. Juli gegenüber dem ursprünglichen Antrag keine neue tatsächliche Anforderung ergab. Der Genehmigungsentwurf lag am 28. Juli fertig vor und wurde am 3. August gezeichnet. Den ursprünglichen falschen Textbaustein habe ich nicht durch eine bereinigte Fassung ersetzt; beide Fassungen bleiben in der elektronischen Akte.

Für Mai lässt sich die Unterschrift nicht auf einen sicheren Tag zurückrechnen. Am 12. Mai war die fachliche Prüfung beendet, am 19. Mai lag der falsche Entwurf vor. Ob die zutreffende Fassung an diesem oder erst am folgenden Zeichnungstag unterzeichnet worden wäre, weiß ich nicht mehr. Die Kanzlei sollte dafür keinen angeblich verbindlichen Drei-Tage-Standard annehmen. Einen solchen Standard haben wir nicht.

Die Angaben zur Ausbaukapazität stammen von den beteiligten Handwerkern, nicht von unserer Behörde. Ich kann beurteilen, ob zusätzliche Auflagen erforderlich waren, aber nicht garantieren, wann der Handwerker ohne den Fehler tatsächlich begonnen hätte. Ebenso wenig kann ich das Beratungshonorar des Kunden bestätigen. Bitte trennen Sie diese Punkte in der Meldung an den Versicherer. Für die technische und bauordnungsrechtliche Prüfung stehe ich als Auskunftsperson zur Verfügung; über eine Zahlung kann ich nicht entscheiden.

Mit freundlichen Grüßen
Yasemin Kraus''','Yasemin Kraus <bauaufsicht@wuerzburg-fallakten.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
        doc('04_Versicherer_Rechnung.eml','MB-W-26086: Rechenweg 1.080 minus 180 minus 80 plus 40','2026-10-05T16:35:00+02:00','email','''Sehr geehrte Frau Holler,

ich habe die vorhandene Nachricht zum Finanzierungsvergleich und unser heutiges Deckungsschreiben beigefügt. Der derzeitige Rechenweg lautet 1.080,00 EUR Honorar abzüglich 180,00 EUR variable Kosten abzüglich 80,00 EUR reguläre Kreditzinsen im gedachten rechtzeitigen Verlauf zuzüglich 40,00 EUR tatsächliche Bereitstellungskosten. Das ergibt 860,00 EUR. Die Addition selbst ist richtig; die tatsächlichen Voraussetzungen bleiben zu prüfen.

Bitte vermeiden Sie, dass die Kasse daneben noch die ursprünglich geltend gemachte Miete als offenen Zusatzposten führt. Sie soll in der Chronologie sichtbar bleiben, wird aber in der neuen Forderung nicht doppelt verlangt. Der gleiche Raum wäre auch bei rechtzeitiger Durchführung bezahlt worden. Ob ein später nachgeholter Auftrag den Ausfall mindert, ist dagegen eine konkrete Frage an die Klägerseite. Eine ohne Grundlage unterstellte Nachholung reicht für eine Kürzung nicht aus.

Unsere Rolle ist derzeit die Prüfung des gemeldeten Haftpflichtfalls. Wir führen das Verwaltungsgerichtsverfahren nicht für die Klägerin und ersetzen keine gerichtliche Entscheidung zur Genehmigung. Bei einer Einigung über 860,00 EUR würde der Hauptbetrag innerhalb des Selbstbehalts liegen. Eine wirtschaftlich vernünftige Lösung kann dennoch sinnvoll sein, wenn die Belege den Anspruch tragen. Die interne Kostentragung darf nicht die Beweiswürdigung steuern. Bitte senden Sie die datierte Alternativchronologie mit dem Kanzleientwurf vor dem 12. Oktober.

Mit freundlichen Grüßen
Vitus Hasenwinkel''','Vitus Hasenwinkel <schaden@mainbogen-vers.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
    ],
))


CASES.append(dict(
    slug='akha-wuerzburg-abwasseranlage',
    title='Abwasseranlage – Eigentumsschaden der Stadt und Haftpflicht des Tiefbauers',
    summary='Stadt, Tiefbauunternehmen und dessen Betriebshaftpflichtversicherer korrespondieren über 4.236,40 EUR Fremdkosten, die unbewiesene 30-Prozent-Kürzung und den Entlastungsnachweis nach § 831 BGB.',
    is_new=False,
    notes='Neue Korrespondenz am Nachmittag des 05.10.2026 nach dem bestehenden Klageentwurf. Die Deckung des Tiefbauers wird erstmals durch dessen Versicherer benannt. Die Stadt bleibt geschädigte Eigentümerin, nicht haftpflichtige Versicherungsnehmerin dieses Vorgangs. Vertragszahlen sind ausschließlich erfundene Szenarioannahmen. Kein Eigenschadenersatz aus städtischer Haftpflicht oder AKHA; kein ungeprüfter Direktanspruch gegen den Betriebshaftpflichtversicherer.',
    core=['schriftverkehr-und-klage/16_Klageentwurf.docx',f'{FOLDER}/01_Stadt_an_Tiefbauer.docx'],
    exhibits=[],
    attachments={
        '03_Versicherer_an_Tiefbauer.eml':['03_Leitungsauskunft.docx','schriftverkehr-und-klage/11_Polier_Suchschlitz.eml'],
        '04_Tiefbauer_an_Stadt.eml':[f'{FOLDER}/02_Tiefbauer_an_Versicherer.pdf'],
    },
    documents=[
        doc('01_Stadt_an_Tiefbauer.docx','Schlehenfächerweg – Forderung, Deckungsnachweis und Kürzungseinwand','05.10.2026','letter','''Stadt Würzburg, Rechtsstelle, Mainlaubplatz 1, 97070 Würzburg

Grab & Grund Tiefbau GmbH, Geschäftsführerin Ida Sauer, Kieswindenweg 12, 97076 Würzburg

Sehr geehrte Frau Sauer,

ergänzend zu unserem Schreiben vom 2. Oktober bleiben wir bei der Forderung über 4.236,40 EUR. Die Zahlungsfrist bis 16. Oktober besteht unverändert. Der Betrag setzt sich aus 3.284,40 EUR bezahlter Reparatur und 952,00 EUR notwendiger Überleitung zusammen. Die zuvor diskutierten 336,00 EUR eigener Stunden sind nicht Gegenstand dieser Forderung. Bitte führen Sie diese Abgrenzung auch in Ihrer Schadenmeldung an einen Versicherer fort.

Ihre vorgeschlagene Kürzung um 30 Prozent entspricht 1.270,92 EUR. Es verblieben 2.965,48 EUR. Das ist bislang ein Verhandlungsvorschlag, kein nachgewiesener Mitverantwortungsanteil und kein von uns angenommener Vergleich. Unsere Leitungsauskunft wies auf den alten Planstand, die ungefähre Tiefe und einen Suchkorridor von einem Meter zu beiden Seiten hin. Der nach der Schilderung Ihres Poliers um etwa 60 Zentimeter versetzte Aushub lag innerhalb dieses Bereichs. Die tatsächliche Lage war vor dem maschinellen Fortsetzen nicht positiv festgestellt.

Wir bitten um konkrete Erläuterung, welche unserer Angaben trotz des ausdrücklichen Unsicherheitshinweises eine sichere Freigabe zum Baggereinsatz vermittelt haben soll. Ein fehlendes neues Aufmaß ist kein Ersatz für diese Darlegung. Ebenso benötigen wir für den von Ihnen angekündigten Entlastungsnachweis die auf diesen Arbeitsgang bezogenen Anweisungen, Kontrollen und Zuständigkeiten. Eine allgemeine Erklärung, Ihre Beschäftigten seien erfahren, beantwortet die tatsächliche Durchführung noch nicht.

Sollte Ihre Betriebshaftpflicht die Bearbeitung übernehmen, teilen Sie uns bitte Versicherer und Schadennummer mit. Wir werden daraus nicht ohne zusätzliche rechtliche Grundlage einen unmittelbaren Anspruch gegen den Versicherer ableiten. Unsere Schuldnerin bleibt nach dem bisherigen Sachstand Ihr Unternehmen. Die Beschädigung einer städtischen Anlage wird auch nicht dadurch zu einem Haftpflichtschaden der Stadt, dass diese Mitglied einer kommunalen Versicherung ist.

Wir sind bereit, konkrete technische Einwendungen zu besprechen. Eine Zahlung oder ein rechtsverbindliches Teilanerkenntnis liegt bislang nicht vor. Bitte übersenden Sie keine Unterlagen zu anderen Baustellen, soweit sie die behauptete Aufsicht und Arbeitsorganisation im vorliegenden Vorgang nicht betreffen. Wir sichern den Reparatur- und Zahlungsnachweis und erwarten Ihre Antwort innerhalb der bestehenden Frist.

Mit freundlichen Grüßen
Gertraud Holler'''),
        doc('02_Tiefbauer_an_Versicherer.docx','Bagger-Schaden Stadt Würzburg – Bitte um Prüfung des Kürzungsvorschlags','05.10.2026','letter','''Grab & Grund Tiefbau GmbH, Kieswindenweg 12, 97076 Würzburg

Felsenranke Versicherung AG, Haftpflichtschäden, Buchenquastweg 4, 97076 Würzburg

Sehr geehrte Frau Bitterlich,

wir bitten um Bearbeitung des am 7. September entstandenen Schadens am öffentlichen Abwasserkanal am Schlehenfächerweg. Unsere heutige Meldung erfolgt nach interner Zuordnung der Police BT-2026-441. Bislang hatte die Stadt von uns weder einen Versicherungsschein noch eine Deckungszusage erhalten. Eine eigene Haftpflichtdeckung der Stadt ist für unsere Verantwortung nicht maßgeblich. Bitte bestätigen Sie die Schadennummer und den Umfang Ihrer Abwehrprüfung.

Die Stadt verlangt 4.236,40 EUR aus zwei bezahlten Fremdrechnungen. Unsere frühere Annahme, zusätzlich seien noch 336,00 EUR städtische Verwaltungsstunden eingeklagt, trifft nach dem neuen Schreiben nicht zu. Wir haben eine Kürzung um 30 Prozent angeregt, weil der Plan von 1988 den Kanal nur ungefähr abbildete. Einen Vergleich haben wir nicht geschlossen. Auch ein vorbehaltloses Anerkenntnis des verbleibenden Betrags von 2.965,48 EUR war damit nicht verbunden. Es wurde nichts gezahlt.

Nach der inzwischen eingeholten Auskunft des Poliers stand die Suchanweisung auf derselben Seite wie der Planhinweis. Seine frühere Erinnerung an eine nicht gelesene Rückseite soll deshalb nicht aufrechterhalten werden. Der Suchschlitz war erst 70 bis 80 Zentimeter tief. Der Polier ließ danach ungefähr 60 Zentimeter seitlich mit dem Bagger weiterarbeiten; der Kanal wurde getroffen. Wir können nicht erklären, er habe außerhalb des bezeichneten Suchkorridors gearbeitet. Ob eine Handsuche unter den damaligen Bodenverhältnissen ohne zusätzliche Sicherung möglich gewesen wäre, ist noch zu klären.

Beide eingesetzten Personen sind unsere Arbeitnehmer. Wir stellen gerade Unterweisungen und Kontrollunterlagen zusammen. Eine konkrete persönliche Anweisung von mir zum maschinellen Fortsetzen gab es nicht. Den gesetzlichen Entlastungsnachweis möchten wir nicht allein mit meiner Abwesenheit führen. Bitte sagen Sie uns, welche organisatorischen Unterlagen für die Prüfung erforderlich sind, und unterscheiden Sie dabei zwischen allgemeiner Schulung und tatsächlicher Kontrolle dieses Arbeitsgangs.

Unsere Auftraggeberin war Faserfink Netz GmbH, nicht die Stadt. Einen Werklohnanspruch oder eine Aufrechnung gegen die Stadt gibt es daher nicht. Vor einer weiteren Antwort möchten wir Ihre Einschätzung zu Haftung, Mitverantwortung und Selbstbehalt erhalten. Die Zahlungsfrist der Stadt läuft bis 16. Oktober.

Mit freundlichen Grüßen
Ida Sauer
Geschäftsführerin'''),
        doc('03_Versicherer_an_Tiefbauer.eml','FR-260907: konkrete Arbeitsanweisung statt pauschaler Planquote','2026-10-05T16:05:00+02:00','email','''Sehr geehrte Frau Sauer,

wir führen den Vorgang unter FR-260907. Ihre Betriebshaftpflicht umfasst nach dem erfassten Vertragsauszug gesetzliche Sachschadenhaftung aus Tiefbauarbeiten bis 3.000.000,00 EUR je Schadenereignis bei 1.000,00 EUR Selbstbehalt. Eine abschließende Deckungszusage erteilen wir heute nicht; insbesondere ist der Zeitpunkt der Nachmeldung noch zu erläutern. Die gesetzliche Haftung und die versicherungsvertragliche Prüfung bleiben getrennt.

Anbei die uns vorgelegte Leitungsauskunft und die Polierergänzung. Beide sprechen gegen eine ohne Weiteres feststehende 30-Prozent-Kürzung. Die alte Planlage wurde als unsicher bezeichnet, der Korridor war ausdrücklich freizulegen. Bitte reichen Sie die tatsächliche Unterweisung und Aufsicht nach. Erfahrung und Seminarbesuche können relevant sein, ersetzen aber nicht sämtliche Voraussetzungen eines Entlastungsbeweises nach § 831 BGB. Wir nehmen auch nicht allein aus der Bezeichnung „Polier“ eine Organstellung an.

Die Forderung umfasst nur die zwei Fremdrechnungen. Die Stadt hat die Umsatzsteuer nach ihrer konkreten Buchungszuordnung nicht abgezogen. Ein pauschaler Hinweis auf kommunale Vorsteuerberechtigung wäre daher unzureichend. Bei 4.236,40 EUR Hauptforderung besteht nach unserer Einzelmeldeschwelle von 250.000,00 EUR kein Anlass für einen personenbezogenen Rückversichererbericht. Bitte erklären Sie gegenüber der Stadt weder ein Anerkenntnis noch eine endgültige Ablehnung, bevor wir die Arbeitsorganisation und die Reparaturunterlagen abgeglichen haben.

Mit freundlichen Grüßen
Amelie Bitterlich''','Amelie Bitterlich <haftpflicht@felsenranke-vers.example>','Ida Sauer <geschaeftsfuehrung@grab-grund.example>'),
        doc('04_Tiefbauer_an_Stadt.eml','Schlehenfächerweg – Versicherungsbearbeitung ohne Anerkenntnis','2026-10-05T16:50:00+02:00','email','''Sehr geehrte Frau Holler,

unsere Betriebshaftpflicht wird unter der Nummer FR-260907 von der Felsenranke Versicherung AG, Frau Amelie Bitterlich, bearbeitet. Mein heutiges Meldeschreiben füge ich zur Klarstellung des übermittelten Sachverhalts bei. Es ist kein Schuldanerkenntnis und keine Zusage des Versicherers. Die Forderung bleibt gegen unser Unternehmen gerichtet; wir bitten Sie nicht, ausschließlich gegen den Versicherer vorzugehen.

Wir haben die geforderten 4.236,40 EUR und die Nichtgeltendmachung der 336,00 EUR Eigenstunden richtiggestellt. Der Versicherer prüft unseren bisherigen Vorschlag einer 30-Prozent-Kürzung und hat dazu konkrete Unterlagen verlangt. Es besteht bislang keine Einigung über 2.965,48 EUR. Wir haben weder diesen Betrag noch den vollen Betrag überwiesen.

Die Aussage unseres Poliers, die Suchanweisung habe auf derselben Seite gestanden, wird unverändert weitergegeben. Wir stellen derzeit die auf diesen Einsatz bezogenen Unterweisungen und Kontrollvermerke zusammen. Nicht vorhandene Kontrollen werden nicht durch nachträglich ausgefüllte Formulare ersetzt. Sollten einzelne Unterlagen fehlen, werden wir dies ausdrücklich mitteilen. Die Stadt muss für unseren Schadenfall keine eigene Haftpflichtmeldung abgeben. Eine mögliche Sachversicherung der Anlage ist uns nicht bekannt und wird von uns auch nicht unterstellt.

Wir halten Ihre Frist bis 16. Oktober fest und werden uns vorher wieder melden. Für einen sachlichen Austausch über Planlage und Arbeitsausführung stehen wir zur Verfügung; eine abschließende Quote lässt sich aus dem Alter des Plans allein nicht begründen.

Mit freundlichen Grüßen
Ida Sauer''','Ida Sauer <geschaeftsfuehrung@grab-grund.example>','Gertraud Holler <recht@wuerzburg-fallakten.example>'),
    ],
))
