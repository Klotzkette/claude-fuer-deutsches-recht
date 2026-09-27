"""Originalunterlagen der Planung für das Wohnhaus mit acht Wohnungen."""
from pathlib import Path
import math

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white

from bauwirtschaft_hildesheim_common import CASE, ASSETS, build_records, setup_fonts


def H(text): return ("h", text)
def T(text): return text
def P(): return ("page",)


def record(n, filename, date, issuer, recipient, title, sections, **extra):
    return dict(number=n, filename=f"{n:03d}_{filename}", date=date, issuer=issuer,
                recipient=recipient, title=title, sections=sections, **extra)


def documents():
    return [
        record(1, "Projektauftrag_Wohnhof.pdf", "2026-10-05", "bauherr", "architekt", "Projektauftrag Wohnhof Am Steinbogen", [
            T("Wir beauftragen Sie mit der Vorbereitung unseres Neubaus mit acht dauerhaft zu vermietenden Wohnungen am Wohnhof Am Steinbogen 18 in Hildesheim. Die Steinbogen Wohnen GmbH hält das 1.300 m² große Grundstück für dieses Vorhaben bereit. Eine Aufteilung und ein Verkauf von Eigentumswohnungen sind nicht vorgesehen. Die Planung beginnt am 5. Oktober 2026; die Übergabe zur Vermietung streben wir für September 2028 an."),
            H("1 Wirtschaftlicher Rahmen"),
            T("Die Investitionsobergrenze beträgt 3.650.000,00 EUR brutto einschließlich Grundstück, Planung, Errichtung, Erwerbsnebenkosten und Finanzierung. Wir rechnen bei der langfristigen Wohnraumvermietung nicht mit einem Vorsteuerabzug. Die Kostendarstellung muss deshalb Bruttobeträge und Umsatzsteuer getrennt zeigen. Fördermittel und eine Bindung an öffentliche Vergabeverfahren sind bislang nicht Bestandteil der Finanzierung. Angebote werden gleichwohl vergleichbar und nachvollziehbar ausgewertet."),
            H("2 Nutzungsziel und Entscheidungsweg"),
            T("Vorgesehen sind insgesamt 600 m² Wohnfläche: sechs Wohnungen in den unteren beiden Geschossen und zwei Wohnungen im obersten Geschoss. Wir wünschen einen Aufzug mit drei Halten, stufenlose Zugänge, einen gemeinschaftlichen Fahrradraum und einen kleinen Spielbereich. Die Wohnungen sollen alltagstauglich für unterschiedliche Altersgruppen nutzbar sein. Nachträgliche Mieterausbauten sollen auf ein Minimum beschränkt bleiben."),
            T("Die Geschäftsführung entscheidet über Varianten, Kostenrahmen, wesentliche Materialänderungen und Vergaben. Das Architekturbüro erhält keine Vollmacht, Bauverträge in unserem Namen abzuschließen, Forderungen anzuerkennen oder Abnahmen für uns zu erklären. Freigaben sind mit Planstand, Datum und Kostenfolge zu dokumentieren. Bis zur Unterzeichnung des Architektenvertrags dürfen nur die bereits besprochene Ortsaufnahme und die Klärung des Planungsbedarfs vorbereitet werden."),
            H("3 Erste Unterlagen"),
            T("Bitte legen Sie bis Ende Oktober ein Bedarfsprogramm, einen Terminrahmen und eine Liste der benötigten Fachbeiträge vor. Die Grenzlage, Erschließung und Grundstücksentwässerung sind ausdrücklich zu klären. Eine verbindliche Aussage zur planungsrechtlichen Zulässigkeit liegt uns noch nicht vor. Den bisherigen Nachbarschaftseindruck verstehen wir nicht als Genehmigungszusage."),
        ]),
        record(2, "Bedarfsprogramm_und_Planungsziele.docx", "2026-10-12", "architekt", "bauherr", "Bedarfsprogramm für acht Mietwohnungen", [
            T("Das am 12. Oktober 2026 mit der Bauherrin abgestimmte Programm beschreibt die Anforderungen für den Variantenvergleich. Es ersetzt weder die Bauvorlagen noch die Fachnachweise. Maßgeblich sind ein wirtschaftlicher Betrieb, robuste Materialien und dauerhaft vermietbare Grundrisse."),
            H("1 Wohnungen und gemeinschaftliche Flächen"),
            T("Im Erdgeschoss werden WE 01 mit 68 m², WE 02 mit 75 m² und WE 03 mit 82 m² vorgesehen. Im ersten Obergeschoss wiederholt sich die Größenfolge als WE 04 bis WE 06. Im zweiten Obergeschoss erhalten WE 07 und WE 08 jeweils 75 m². Die Sollsumme beträgt 600 m². Jede Wohnung benötigt einen eigenen Abstellbereich, einen Waschmaschinenplatz und eine nutzbare Küchenzone. Kellerflächen sind ausgeschlossen. Müll, Haustechnik und Fahrräder werden deshalb ebenerdig organisiert."),
            H("2 Erreichbarkeit und Barrierefreiheit"),
            T("Alle acht Wohnungen sind barrierefrei zu planen. WE 01 erhält zusätzlich die für eine rollstuhlgerechte Nutzung notwendigen Bewegungsflächen und Ausstattungsvorbereitungen. Die Bauherrin bestellt den Aufzug unabhängig von einer höhenabhängigen gesetzlichen Aufzugpflicht. Vom gekennzeichneten Stellplatz bis WE 01 und zu den übrigen Wohnungen wird eine stufenlose Wegekette vorgesehen. Türdurchgänge, Bewegungsflächen und lichte Aufzugsmaße sind in der Ausführungsplanung nachzuweisen; die Angabe einer Wohnfläche allein belegt diese Anforderungen nicht."),
            H("3 Grundstück und Außenanlagen"),
            T("Acht Pkw-Stellplätze einschließlich eines barrierefrei nutzbaren Platzes werden freiwillig eingeplant. Für Fahrräder sind 16 gesicherte Bewohnerplätze und vier Besucherplätze vorzusehen. Der Spielbereich erhält 30 m² zusammenhängende Fläche im südöstlichen Garten, abgegrenzt von der Zufahrt. Die Entwässerung darf weder zum Nachbargrundstück noch auf den öffentlichen Gehweg führen. Eine Versickerung ist erst nach Baugrundbewertung festzulegen."),
            H("4 Qualität und Betrieb"),
            T("Wärmepumpe und Photovoltaik werden vorgesehen. Schallschutzstandort und Stromanschluss sind vor Ausschreibung zu prüfen. Zur Übergabe werden Wohnungszähler, Betreiberhandbuch und Wartungsübersicht verlangt."),
            H("5 Festgehaltene Zielkonflikte"),
            T("Eine Vergrößerung der Wohnfläche über 600 m² setzt die erneute Abstimmung von Genehmigung, Kosten und Barrierefreiheit voraus. Größere Balkone werden zurückgestellt. Grundstück und Finanzierung bleiben Teil jeder Investitionsentscheidung."),
        ]),
        record(3, "Architektenvertrag_mit_Stufenabruf.docx", "2026-10-19", "bauherr", "architekt", "Architektenvertrag Wohnhof Am Steinbogen", [
            T("Die Steinbogen Wohnen GmbH als Auftraggeberin und das in dieser Urkunde bezeichnete Architekturbüro als Auftragnehmer schließen für den Neubau des Achtfamilienhauses am Wohnhof Am Steinbogen 18 in Hildesheim folgenden Vertrag. Beide Parteien handeln unternehmerisch. Der Vertrag wird durch Austausch dieser inhaltlich übereinstimmenden Erklärungen in Textform geschlossen."),
            H("1 Gegenstand und Planungsgrundlagen"),
            T("Der Auftragnehmer übernimmt die Objektplanung Gebäude und Innenräume für acht Mietwohnungen mit insgesamt 600 m² geplanter Wohnfläche, ohne Keller, mit drei oberirdischen Geschossen und einem Aufzug. Der Vertragsumfang orientiert sich an den Grundleistungen der Leistungsphasen 1 bis 9 gemäß Anlage 10 Nummer 10.1 HOAI, soweit diese für das bezeichnete Objekt tatsächlich erforderlich und nach Nummer 2 abgerufen sind. Das Bedarfsprogramm vom 12. Oktober 2026 sowie die nachfolgend schriftlich bestätigten Planungsentscheidungen bestimmen die vereinbarten Planungsziele."),
            T("Die anfängliche Investitionsobergrenze von 3.650.000,00 EUR brutto umfasst Grundstück, Planung, Errichtung, Erwerbsnebenkosten und Finanzierung. Der Auftragnehmer erfasst die ihm mitgeteilten Kostenanteile, kennzeichnet nicht von ihm fachlich ermittelte Ansätze und meldet absehbare Überschreitungen mit Handlungsoptionen unverzüglich. Er schuldet keine Finanzierungszusage, keinen Vermietungserfolg und keine Garantie für das Preisverhalten der Bauunternehmen."),
            H("2 Stufenweise Beauftragung"),
            T("Mit Abschluss dieses Vertrags werden die Leistungsphasen 1 und 2 verbindlich abgerufen. Die Leistungsphasen 3 und 4 bilden die zweite Stufe; die Leistungsphasen 5 bis 7 bilden die dritte Stufe; die Leistungsphase 8 bildet die vierte und die Leistungsphase 9 die fünfte Stufe. Jeder weitere Abruf erfolgt durch eine Erklärung der Auftraggeberin in Textform. Ein Anspruch auf Abruf weiterer Stufen besteht nicht. Die Auftragnehmerin beginnt eine nicht abgerufene Stufe erst nach dem entsprechenden Abruf. Die Anrede Auftragnehmer in dieser Urkunde bezeichnet das Architekturbüro unabhängig von der jeweils handelnden Person."),
            T("Die Bearbeitungsfristen werden bei jedem Abruf anhand des dann bekannten Genehmigungs- und Vergabestands festgelegt. Bereits begonnene beauftragte Leistungen sind sachgerecht abzuschließen oder nach Weisung geordnet zu übergeben. Gesetzliche Kündigungsrechte und die hierfür geltenden Vergütungsfolgen bleiben unberührt."),
            H("3 Honorar und Abrechnung"),
            T("Für sämtliche vollständig erbrachten und abgerufenen Vertragsleistungen der Leistungsphasen 1 bis 9 wird ein Pauschalhonorar von 145.000,00 EUR netto zuzüglich gesetzlicher Umsatzsteuer vereinbart. Bei 19 Prozent Umsatzsteuer ergibt dies 172.550,00 EUR brutto. Das Pauschalhonorar umfasst übliche Nebenkosten, örtliche Besprechungen und die vereinbarte digitale Planübergabe. Eine gesonderte Nebenkostenpauschale fällt nicht an."),
            T("Zur Zuordnung auf die Abrufstufen und für nachvollziehbare Abschlagsrechnungen entfallen 2.900,00 EUR netto auf Leistungsphase 1, 10.150,00 EUR auf Leistungsphase 2, 21.750,00 EUR auf Leistungsphase 3, 4.350,00 EUR auf Leistungsphase 4, 36.250,00 EUR auf Leistungsphase 5, 14.500,00 EUR auf Leistungsphase 6, 5.800,00 EUR auf Leistungsphase 7, 46.400,00 EUR auf Leistungsphase 8 und 2.900,00 EUR auf Leistungsphase 9. Die Verteilung begründet keinen Zahlungsanspruch für nicht erbrachte oder nicht abgerufene Leistungen."),
            T("Abschläge dürfen entsprechend dem nachgewiesenen Wert vertragsgemäß erbrachter Leistungen verlangt werden. Jede Rechnung weist Leistungsstand, bereits berechnete Beträge, Umsatzsteuer und eingegangene Zahlungen aus. Eine Zahlung innerhalb von 21 Kalendertagen nach Eingang einer prüffähigen und berechtigten Rechnung wird vereinbart; gesetzlich zwingende Fälligkeitsvoraussetzungen bleiben zu beachten. Die Schlussrechnung setzt die gesetzlich erforderliche Abnahme und eine prüffähige Schlussrechnung voraus. Pauschalhonorar und Stufenteilbeträge ändern sich nicht allein durch eine Veränderung der anrechenbaren Kosten."),
            H("4 Fachplanung und zusätzliche Leistungen"),
            T("Tragwerksplanung, technische Ausrüstung, Baugrunduntersuchung, Vermessung, gesonderte bauphysikalische Nachweise und fachrechtliche Anträge außerhalb der Objektplanung beauftragt die Auftraggeberin unmittelbar. Der Auftragnehmer benennt rechtzeitig den fachlichen Bedarf, koordiniert die vereinbarten Schnittstellen und berücksichtigt freigegebene Fachbeiträge. Die Fachplaner bleiben für ihre eigenen Leistungen verantwortlich."),
            T("Besondere Leistungen, zusätzliche Varianten nach abgeschlossener Entscheidung, Änderungen bereits freigegebener Planungsziele und wiederholte Leistungen sind vor ihrer Ausführung nach Gegenstand, zeitlicher Folge und Vergütung in Textform abzustimmen. Eine bloße Teilnahme an einer Besprechung oder der Eingang eines Änderungswunsches gilt nicht als gesonderte Beauftragung. Soweit gesetzliche Änderungs- und Vergütungsregelungen unmittelbar eingreifen, bleiben sie unberührt; die Beteiligten dokumentieren den Anlass und den Leistungsumfang unverzüglich."),
            H("5 Mitwirkung und Planfreigaben"),
            T("Die Auftraggeberin stellt die verfügbaren Grundstücks- und Finanzierungsangaben vollständig zur Verfügung und trifft angeforderte Entscheidungen innerhalb einer im Einzelfall angemessenen Frist. Der Auftragnehmer benennt die benötigte Entscheidung, den zugehörigen Planstand und die absehbaren Termin- und Kostenfolgen einer Verzögerung. Freigaben der Auftraggeberin ersetzen weder die geschuldete fachliche Prüfung noch behördliche Entscheidungen."),
            T("Pläne werden mit eindeutiger Nummer, Revisionsstand und Ausgabedatum übergeben. Überholte Planstände werden in einer Änderungsliste gekennzeichnet. Baustellenfreigaben beziehen sich ausschließlich auf die bezeichneten Bauteile und den freigegebenen Umfang; eine noch offene Fachplanung ist ausdrücklich auszuweisen."),
            H("6 Vergabe und rechtliche Beratung"),
            T("Der Auftragnehmer bereitet technische Leistungsbeschreibungen vor, prüft Angebote fachlich und wirtschaftlich und wirkt am Zusammenstellen der Vertragsunterlagen mit. Er verwendet dabei die von der Auftraggeberin rechtlich freigegebenen Vertragsgrundlagen. Er erhält keine Vollmacht zum Abschluss oder zur Änderung von Bauverträgen und keine Vollmacht zur Erklärung der Abnahme, zum Vergleich oder zum Forderungsverzicht."),
            T("Eine eigenständige, auf die Interessen der Auftraggeberin zugeschnittene rechtliche Gestaltung streitiger oder risikoverteilender Vertragsklauseln ist nicht als Leistung des Architekturbüros vereinbart. Hierzu beauftragt die Auftraggeberin bei Bedarf unmittelbar eine hierfür befugte Rechtsberatung. Das Architekturbüro liefert die technischen und wirtschaftlichen Tatsachen und stimmt die Unterlagen mit dieser Beratung ab. Eine technische Freigabe darf nicht als rechtliche Prüfung bezeichnet werden."),
            H("7 Abnahme und Dokumentation"),
            T("Die Abnahme von Bauleistungen erklärt ausschließlich die Auftraggeberin oder eine hierzu im Einzelfall ausdrücklich bevollmächtigte Person. Der Auftragnehmer bereitet im beauftragten Umfang Abnahmen vor, stellt festgestellte Mängel zusammen und dokumentiert die Erledigung. Die Abnahme seiner eigenen Planungs- und Überwachungsleistungen wird von der Bauabnahme getrennt behandelt. Gesetzliche Ansprüche auf Teilabnahme bleiben unberührt."),
            T("Die Leistungsphase 9 umfasst die im beauftragten Leistungsbild geschuldete fachliche Bewertung innerhalb der dafür maßgeblichen Zeiträume, die erforderliche Objektbegehung vor Ablauf der einschlägigen Mängelanspruchsfristen und die Mitwirkung bei der Freigabe von Sicherheiten. Eine fortlaufende Überwachung späterer Mängelbeseitigungsarbeiten wird dadurch nicht stillschweigend zusätzlich beauftragt. Die Übergabe erfolgt mit Planverzeichnis, Revisionsunterlagen, Prüfprotokollen, Kontaktdaten der Firmen und einer Fristenübersicht."),
            H("8 Schlussbestimmungen"),
            T("Für Haftung, Mängelrechte, Verjährung und Kündigung gelten die gesetzlichen Bestimmungen, soweit dieser Vertrag keine wirksame speziellere Vereinbarung enthält. Eine pauschale Haftungsfreizeichnung wird nicht vereinbart. Die Auftraggeberin erhält nach Zahlung der geschuldeten Vergütung die zur vertragsgemäßen Errichtung, Nutzung, Unterhaltung und Änderung dieses konkreten Gebäudes erforderlichen Nutzungsrechte an den übergebenen Planungsunterlagen. Weitergehende urheberrechtliche Befugnisse verbleiben beim Berechtigten."),
            T("Die Parteien geben ihre Annahmeerklärungen am 19. Oktober 2026 in dieser gemeinsamen Vertragsfassung ab. Für die Steinbogen Wohnen GmbH: Maren Birk, Geschäftsführerin, erklärt die Annahme sämtlicher vorstehender Vereinbarungen. Für Konturfeld Architektur PartG mbB: Nora Feld, Architektin, erklärt die Annahme sämtlicher vorstehender Vereinbarungen. Die Namen schließen die jeweiligen Erklärungen in Textform ab."),
        ]),
        record(4, "Ortsbesichtigung_Grundlagen.pdf", "2026-10-23", "architekt", "bauherr", "Protokoll der ersten Ortsbesichtigung", [
            T("Am 23. Oktober 2026 wurden Grundstück, Zufahrt und angrenzende Bebauung gemeinsam mit der Bauherrin besichtigt. Es handelte sich um eine Sichtaufnahme bei trockener Witterung. Verdeckte Leitungen, rechtliche Grenzverhältnisse und der Untergrund konnten dabei nicht festgestellt werden."),
            H("1 Grundstück und Umgebung"),
            T("Die Arbeitsvermessung zeigt ein annähernd rechteckiges Grundstück von 32,50 m Breite und 40,00 m Tiefe. Die Straße liegt nördlich. Das Gelände fällt von Nordwest nach Südost um etwa 0,35 m ab. Im Garten stehen zwei kleinere Obstbäume. Im nördlichen Drittel befinden sich Reste einer befestigten Zufahrt; für deren Rückbau wurde noch keine Schadstoffuntersuchung durchgeführt."),
            T("Die benachbarten Gebäude wurden ohne Betreten fremder Grundstücke aufgenommen: westlich ein dreigeschossiges Wohnhaus mit etwa 10,20 m oberem Abschluss, östlich ein zweigeschossiges Wohnhaus mit ausgebautem Dach und etwa 9,60 m Firsthöhe, südlich zwei Wohngebäude mit zwei beziehungsweise drei sichtbaren Geschossen. Die Werte dienen zunächst dem Variantenvergleich und sind vor der Einreichung anhand vermessener Ansichten zu präzisieren. Eine abschließende Bestimmung der näheren Umgebung ist damit nicht verbunden."),
            H("2 Befunde und Klärungsbedarf"),
            T("Am südlichen Zaun ist nach Auskunft der Bauherrin nach Starkregen Wasser stehen geblieben. Eine Mulde ist sichtbar, die Ursache jedoch offen. Ein Schachtdeckel im nördlichen Zufahrtsbereich trägt keine eindeutige Kennzeichnung. Die Bauherrin konnte kein aktuelles Leitungskataster vorlegen. Vor Erdarbeiten sind Leitungsauskünfte und eine örtliche Einweisung einzuholen."),
            H("3 Nächste Bearbeitung"),
            T("Das Büro veranlasst nach Einzelauftrag die Arbeitsvermessung und empfiehlt zwei Baugrundaufschlüsse sowie einen Versickerungsversuch. Die Bauherrin stellt Erwerbsunterlagen und verfügbare Grundbuch- beziehungsweise Baulastenauskünfte gesondert bereit. Ein Beginn von Bauarbeiten wird aus diesem Protokoll nicht abgeleitet. Im Variantenvergleich werden der tiefe südöstliche Gartenbereich und die Lage der Entwässerung gesondert behandelt."),
        ]),
        record(5, "Lageplan_LP01.pdf", "2027-06-24", "vermessung", "architekt", "Lageplan LP01", [], plan=True),
        record(6, "Baugrund_und_Versickerungsbefund.pdf", "2026-11-16", "geo", "bauherr", "Baugrundbefund und Hinweise zur Gründung", [
            T("Für den geplanten nicht unterkellerten Wohnungsneubau wurden am 9. November 2026 zwei Kleinbohrungen bis 6,00 m unter Gelände und ein Versickerungsversuch im südöstlichen Grundstücksbereich durchgeführt. Die Aufschlusspunkte sind auf das örtliche Koordinatensystem des Lageplans LP01 bezogen: B 1 bei x 10,00 m und y 17,00 m, B 2 bei x 23,00 m und y 28,00 m. Die Beschreibung gilt nur für die erfassten Punkte."),
            H("1 Schichten und Wasser"),
            T("B 1 zeigt bis 0,40 m humosen Oberboden, bis 1,10 m sandig-schluffige Auffüllung und darunter bis zur Endteufe steifen, lokal kiesigen Geschiebelehm. B 2 zeigt bis 0,35 m Oberboden, bis 0,90 m Auffüllung und darunter ebenfalls steifen Geschiebelehm. In B 2 trat nach zwei Stunden bei 2,40 m unter Gelände Wasser ein. Eine Grundwassermessstelle wurde nicht eingerichtet. Ein einzelner Bohrtag erlaubt keine Aussage zum höchsten zu erwartenden Wasserstand."),
            H("2 Gründung und Erdarbeiten"),
            T("Eine flach gegründete Bodenplatte erscheint bei vollständigem Austausch ungeeigneter Auffüllungen grundsätzlich möglich. Die Tragwerksplanung hat Setzungsunterschiede, Randverdickungen und die tatsächlichen Lasten zu prüfen. Für die Vorbemessung kann bei einer ausreichend verdichteten Tragschicht ein Bettungsmodul von 15 MN/m³ als Arbeitsansatz verwendet werden; die endgültige Festlegung erfolgt anhand der abgestimmten Gründungsgeometrie. Die Gründungssohle ist vor Einbau der Sauberkeitsschicht geotechnisch abzunehmen."),
            H("3 Niederschlagswasser"),
            T("Der Versuch im südöstlichen Bereich ergab eine geringe Wasserdurchlässigkeit mit einem orientierenden Durchlässigkeitsbeiwert von 0,0000002 m/s. Eine ausschließlich auf Versickerung gestützte Grundstücksentwässerung wird auf dieser Grundlage nicht empfohlen. Die Fachplanung soll Rückhaltung und gedrosselte Ableitung mit dem Entwässerungsträger abstimmen. Ein unkontrollierter Überlauf auf Nachbargrundstücke ist zu vermeiden."),
            H("4 Abgrenzung und weiteres Vorgehen"),
            T("Eine chemische Boden- oder Asphaltanalyse ist nicht Gegenstand dieser Untersuchung. Vor Entsorgung sind repräsentative Deklarationsproben nach dem tatsächlichen Aushubkonzept zu bilden. Die Bauherrin soll für die Ausschreibung eine Mengenreserve für örtlich tiefer reichende Auffüllung vorsehen. Abweichungen bei der Freilegung, Wasserzutritte oder weiche Stellen sind vor Fortsetzung der Gründung anzuzeigen."),
        ]),
        record(7, "Variantenvergleich_Vorplanung.docx", "2026-12-04", "architekt", "bauherr", "Variantenentscheidung für das Achtfamilienhaus", [
            T("Für den nächsten Planungsschritt empfehlen wir Variante 2 mit einem zentralen Erschließungskern und einem im Süden zurückgesetzten obersten Geschoss. Die Empfehlung berücksichtigt das Bedarfsprogramm, den Baugrundbefund vom 16. November 2026 und die Investitionsobergrenze. Eine behördliche Zulässigkeitsentscheidung ist damit noch nicht verbunden."),
            H("1 Vergleichsgrundlage"),
            T("Alle Varianten enthalten acht Wohnungen, den Aufzug mit drei Halten und die vorgesehenen Außenanlagen. Die Grundstückskosten und Finanzierungskosten werden im Vergleich unverändert behandelt. Die technische Ausrüstung wird einheitlich mit Wärmepumpe und Photovoltaik angesetzt. Ein Vergleich, der bei einer Variante den Aufzug oder die erforderlichen Bewegungsflächen wegließe, würde die Entscheidungsgrundlage verzerren."),
            H("2 Varianten"),
            T("Variante 1 bildet drei Geschosse über der vollständigen Grundfläche von 20,00 m × 15,00 m ab. Die Brutto-Grundfläche beträgt 900 m². Die zusätzliche Fläche verbessert Abstellmöglichkeiten, führt aber zu einem größeren Baukörper als für das Wohnflächenprogramm erforderlich. Gegenüber der bevorzugten Variante entstehen 80 m² zusätzliche Brutto-Grundfläche. Die Einfügung der südlichen Fassadenflucht wäre vertieft abzustimmen."),
            T("Variante 2 ordnet Erdgeschoss und erstes Obergeschoss auf jeweils 20,00 m × 15,00 m an. Das zweite Obergeschoss misst 20,00 m × 11,00 m und ist an der Südseite um 4,00 m zurückgesetzt. Die Brutto-Grundfläche beträgt 820 m². Die Wohnungen des obersten Geschosses erhalten keine begehbare Dachterrasse auf der Rücksprungfläche. Das vereinfacht Abdichtung, Nutzung und Flächenberechnung. Drei Vollgeschosse werden der weiteren Planung zugrunde gelegt."),
            T("Variante 3 verteilt die Wohnungen auf zwei Häuser mit vier Wohnungen. Sie erfordert zwei Treppenräume und eine zweite vertikale Erschließung oder verändert das Erreichbarkeitsprogramm. Zugleich werden Leitungswege und Fassadenanteile größer. Der Vorteil einer kleineren Einzelkubatur rechtfertigt für die Bauherrin derzeit nicht die zusätzlichen Erschließungsflächen."),
            H("3 Entscheidungsvoraussetzungen"),
            T("Vor der Entwurfsfreigabe sind die äußere Höhe, die Abstandsflächen, die stufenlose Erreichbarkeit aller Wohnungen und die Entwässerung abzustimmen. Die Kosten werden in der zentralen Kostenfortschreibung geführt. Ein pauschaler Quadratmeterpreis aus einer anderen Gebäudeklasse wird nicht als Kostenberechnung übernommen. Die Entscheidung zugunsten von Variante 2 bleibt bis zur Rückmeldung der Bauaufsicht und der Finanzierung unter dem Vorbehalt, dass keine wesentlichen Hindernisse auftreten."),
        ]),
        record(8, "Variantenfreigabe_und_Abruf.eml", "2026-12-09", "bauherr", "architekt", "Freigabe Variante 2 und Abruf der nächsten Stufe", [
            T("Wir geben die Variante 2 aus Ihrem Vergleich vom 4. Dezember für die weitere Entwurfsbearbeitung frei. Acht Wohnungen und insgesamt 600 m² Wohnfläche bleiben die Grundlage. Die zurückgesetzte Dachfläche soll keine Mieterdachterrasse werden. Bitte verfolgen Sie den Aufzug und die rollstuhlgerechte WE 01 weiter; eine Einsparung dieser Eigenschaften ist nicht freigegeben."),
            T("Hiermit rufen wir die Leistungsphasen 3 und 4 nach Nummer 2 unseres Vertrags vom 19. Oktober 2026 ab. Bitte legen Sie uns vor der Einreichung den vollständigen Entwurfsstand und die fortgeschriebene Kostenberechnung vor. Die Investitionsobergrenze bleibt bei 3.650.000,00 EUR brutto. Auf eine möglicherweise günstige Ausschreibung dürfen Mehrkosten in der Planung nicht vorab gestützt werden."),
            T("Die Nachbarhöhen sind noch nicht abschließend geprüft. Bitte klären Sie auch, ob die Feuerwehr die nördliche Anleiterzone akzeptiert und ob die Fahrräder besser im Nebengebäude oder im Hauptgebäude untergebracht werden. Wir benötigen Ihre Rückmeldung hierzu bis zum Entwurfsgespräch im Februar."),
        ], attachments=["007_Variantenvergleich_Vorplanung.docx"]),
        record(9, "Besprechung_Bauaufsicht_Entwurfsstand.pdf", "2027-02-12", "architekt", "bauherr", "Vermerk zur Abstimmung mit der Bauaufsicht", [
            T("Am 12. Februar 2027 wurde der Entwurfsstand in einer telefonischen Vorbesprechung mit der Bauaufsicht erläutert. Dieser Vermerk gibt das Gespräch aus Sicht des Architekturbüros wieder. Eine Bauvoranfrage und ein Bauvorbescheid sind nicht Gegenstand des Gesprächs; eine Bindungswirkung wird nicht festgehalten."),
            H("1 Baukörper und Umgebung"),
            T("Vorgestellt wurden acht Wohnungen, eine Gebäudegrundfläche von 20,00 m × 15,00 m, ein oberstes Geschoss von 20,00 m × 11,00 m und eine Attikahöhe von 9,90 m über dem Bezugsgelände. Das oberste Geschoss wird als drittes Vollgeschoss bezeichnet. Die Höhe des Fußbodens des höchstgelegenen Aufenthaltsraums beträgt 6,20 m. Für die Einfügungsbeurteilung werden Ansichten der näheren Umgebung und eine nachvollziehbare Erschließungsdarstellung erwartet."),
            H("2 Unterlagenbedarf"),
            T("Die Mitarbeiterin bat darum, den Lageplan mit den Abstandsdarstellungen, die Wohnungsliste und das Barrierefreiheitskonzept zusammen einzureichen. Die Einordnung des Verfahrens und der erforderlichen Bauvorlagen erfolgt durch die Bauaufsicht anhand des vollständigen Antrags. Die bloße Aufnahme eines Vorhabens in eine Vorbesprechung ist keine Bestätigung der Vollständigkeit oder Zulässigkeit."),
            H("3 Festgehaltene offene Punkte"),
            T("Die Lage der Anleiterstellen und die nutzbare Breite der nördlichen Zugangszone sind noch mit der Brandschutzplanung abzugleichen. Die Entwässerung ist gesondert mit dem zuständigen Träger zu klären. Die Bauherrin hat noch keine Erschließungsbestätigung übergeben. Das Büro erstellt eine Nachweisliste und legt die endgültigen Einreichungsunterlagen der Bauherrin zur Freigabe vor."),
        ]),
        record(10, "Entwurfsbeschreibung_Stand_Maerz.docx", "2027-03-19", "architekt", "bauherr", "Entwurfsbeschreibung und abgestimmter Planungsstand", [
            T("Der Entwurf vom 19. März 2027 setzt Variante 2 um. Er enthält acht Wohnungen mit 600 m² Wohnfläche und einen gemeinsamen Erschließungskern mit Treppe und Aufzug. Die Freigabe dieses Entwurfs ist Grundlage für den Bauantrag; die Ausführung wird erst mit den späteren Detailplänen freigegeben."),
            H("1 Kubatur und Konstruktion"),
            T("Erdgeschoss und erstes Obergeschoss haben eine äußere Grundfläche von jeweils 300 m². Das zweite Obergeschoss hat eine Grundfläche von 220 m² und ist an der Südseite zurückgesetzt. Die Summe der Brutto-Grundflächen beträgt damit 820 m². Die Geschossfußböden liegen bei ±0,00 m, +3,10 m und +6,20 m; die Attika endet bei +9,90 m. Ein Keller ist nicht vorgesehen. Die Bodenplatte wird auf einer ausgetauschten und verdichteten Tragschicht gegründet."),
            T("Vorgesehen sind tragende Mauerwerkswände und Stahlbetondecken. Der Treppenraum bildet den zentralen Erschließungsbereich. Die Fassaden erhalten einen robusten mineralischen Oberputz; Sockel und Türanschlüsse werden gegen Spritzwasser ausgebildet. Die zurückgesetzte Dachfläche über dem ersten Obergeschoss ist ausschließlich Wartungsfläche und wird nicht als Wohnfläche angesetzt."),
            H("2 Wohnungen und Erschließung"),
            T("Die Wohnungen WE 01 bis WE 03 liegen im Erdgeschoss, WE 04 bis WE 06 im ersten Obergeschoss, WE 07 und WE 08 im zweiten Obergeschoss. Die Wohnflächenfolge lautet 68, 75, 82, 68, 75, 82, 75 und 75 m². Die Flächenaufstellung unterscheidet Wohnflächen von gemeinschaftlichen Flächen und Konstruktionsflächen. Der Aufzug bedient alle drei Ebenen. Alle acht Wohnungen werden barrierefrei vorgesehen; WE 01 wird zusätzlich rollstuhlgerecht ausgelegt."),
            H("3 Außenanlagen und Technik"),
            T("Acht Pkw-Plätze einschließlich des gekennzeichneten barrierefreien Stellplatzes liegen an der Nordseite und entlang der westlichen Zufahrt. Der Fahrradbereich bietet 16 gesicherte Plätze; vier Besucherplätze liegen beim Hauseingang. Ein 30 m² großer Spielbereich liegt im südöstlichen Garten. Eine Wärmepumpe versorgt Heizung und Warmwasser; die Dachfläche nimmt eine Photovoltaikanlage auf. Die Standort- und Leistungsdetails werden mit der Fachplanung abgestimmt."),
            H("4 Freigabestand"),
            T("Die Bauherrin bestätigt die Kubatur, Wohnungszahl, Wohnflächenziele und das Erschließungsprinzip. Offen bleiben die abschließende Tragwerksbemessung, der objektspezifische Energiebedarfsnachweis, die Dimensionierung der Rückhaltung und die detaillierte Schalldämmung der technischen Anlagen. Die endgültigen Genehmigungsunterlagen müssen diese Beiträge in der jeweils erforderlichen Form enthalten. Der freigegebene Entwurf berechtigt nicht zur Bestellung abweichender Bauteile."),
        ]),
        record(11, "Grundrisse_EG_1OG_GP01.pdf", "2027-03-19", "architekt", "bauherr", "Grundrisse GP01", [], plan=True),
        record(12, "Grundriss_2OG_GP02.pdf", "2027-03-19", "architekt", "bauherr", "Grundriss GP02", [], plan=True),
        record(13, "Schnitt_Ansichten_SP01.pdf", "2027-03-19", "architekt", "bauherr", "Schnitt und Ansichten SP01", [], plan=True),
        record(14, "Wohnflaechenberechnung_acht_Wohnungen.docx", "2027-03-22", "architekt", "bauherr", "Wohnflächenberechnung für acht Wohnungen", [
            T("Die nachfolgende Aufstellung erfasst die geplanten lichten Raumgrundflächen des Entwurfs. Balkon- und Terrassenflächen werden nicht angesetzt. Gemeinschaftliche Treppen-, Aufzugs-, Technik- und Fahrradflächen sind nicht Teil der Wohnflächen. Die Gesamtfläche von 600,00 m² ist ein Planungsstand und nach Ausführung anhand des tatsächlichen Bestands zu kontrollieren."),
            H("1 Erdgeschoss und erstes Obergeschoss"),
            T("WE 01 und WE 04 haben jeweils 68,00 m²: Wohnen und Küche 26,00 m², Schlafen 14,00 m², Zimmer 10,00 m², Bad 7,00 m², Flur 8,00 m² und Abstellraum 3,00 m². Die Grundflächen werden vollständig angesetzt. Bei WE 01 werden Bewegungsflächen und Türanfahrbereiche zusätzlich im Barrierefreiheitsdetail geprüft; ihre Lage darf bei der Möblierung nicht verstellt werden."),
            T("WE 02 und WE 05 haben jeweils 75,00 m²: Wohnen und Küche 29,00 m², Schlafen 14,00 m², Zimmer 12,00 m², Bad 7,00 m², Flur 10,00 m² und Abstellraum 3,00 m². WE 03 und WE 06 haben jeweils 82,00 m²: Wohnen und Küche 29,00 m², Schlafen 14,00 m², Zimmer 1 mit 11,00 m², Zimmer 2 mit 10,00 m², Bad 7,00 m², Flur 8,00 m² und Abstellraum 3,00 m²."),
            H("2 Zweites Obergeschoss"),
            T("WE 07 und WE 08 haben jeweils 75,00 m²: Wohnen und Küche 28,00 m², Schlafen 14,00 m², Zimmer 12,00 m², Bad 7,00 m², Flur 11,00 m² und Abstellraum 3,00 m². Die zurückgesetzte Dachfläche vor der Südfassade ist nicht zur Wohnnutzung bestimmt. Sie wird auch nicht anteilig als Terrasse in diese Berechnung aufgenommen."),
            H("3 Summen und Abgrenzung"),
            T("Erdgeschoss 225,00 m², erstes Obergeschoss 225,00 m² und zweites Obergeschoss 150,00 m² ergeben zusammen 600,00 m². Die Brutto-Grundfläche von 820,00 m² ist eine andere Flächengröße und enthält unter anderem gemeinschaftliche Flächen und Bauteilquerschnitte. Ein Quotient aus Brutto-Grundfläche und Wohnfläche ersetzt keine Ermittlung der einzelnen Raumflächen."),
            T("Die Raumwerte werden als Planungsansätze mit zwei Dezimalstellen geführt und vor der Vermietung am ausgeführten Bestand überprüft. Die übersichtlichen A3-Grundrisse stellen das Erschließungs- und Raumordnungsprinzip dar; für Möbel-, Tür- und Installationsbestellungen sind die bemaßten Ausführungsdetails und späteren Aufmaße maßgeblich. Eine zugesicherte mietvertragliche Fläche wird mit dieser internen Berechnung noch nicht vereinbart."),
        ]),
        record(15, "Fachplanerkoordination_Entwurf.docx", "2027-04-07", "architekt", "bauherr", "Abstimmung von Tragwerk und technischer Ausrüstung", [
            T("In der Besprechung vom 7. April 2027 wurden die Fachbeiträge mit dem Entwurf GP01 und GP02 abgeglichen. Teilgenommen haben Objektplanung, Tragwerksplanung und technische Ausrüstung. Die Bauherrin erhielt das Protokoll zur Entscheidung über die noch offenen Ausstattungsfragen."),
            H("1 Tragwerk"),
            T("Die Tragwerksplanung bestätigt das Grundprinzip aus Mauerwerk und Stahlbetondecken. Für die vorläufigen Spannweiten werden 22 cm starke Decken berücksichtigt; endgültige Bewehrung und Durchstanznachweise folgen in der Ausführungsplanung. Die Randzone am südlichen Rücksprung des obersten Geschosses benötigt ein abgestimmtes Wärmebrückendetail. Der Aufzugsschacht erhält keine nachträglich ungeprüften Aussparungen."),
            H("2 Leitungsführung"),
            T("Die TGA plant zwei durchgehende Installationszonen bei den innenliegenden Bädern. Die Fallleitungen werden nicht durch die tragende Treppenraumwand geführt. Im ersten Entwurf lag ein Lüftungsdurchbruch zu dicht am Deckenauflager; die TGA verschiebt ihn um 25 cm nach Osten und legt bis zum 21. April eine abgestimmte Aussparungsliste vor. Die Objektplanung übernimmt erst den von der Tragwerksplanung bestätigten Stand."),
            H("3 Energie und Schall"),
            T("Für die Wärmepumpe wird der nordöstliche Technikbereich geprüft. Die Bauherrin wünscht keine Außeneinheit unmittelbar neben den Schlafraumfenstern der WE 02. Die Fachplanung bewertet deshalb die südöstliche Aufstellfläche einschließlich Leitungsweg und Schallausbreitung. Die Photovoltaikbelegung muss Wartungswege, Dachabläufe und die Befestigung an der Dachkonstruktion berücksichtigen."),
            H("4 Barrierefreiheit und Freigaben"),
            T("Bei WE 01 bleibt im Bad eine freie Bewegungsfläche von 1,50 m × 1,50 m vorgesehen. Der Waschmaschinenanschluss wandert in den Abstellbereich, damit die Fläche nicht durch ein Gerät eingeschränkt wird. Die Bauherrin bestätigt diese Anordnung. Türlisten mit lichten Durchgangsmaßen sind vor Ausschreibung zu erstellen. Das Protokoll enthält noch keine Freigabe der Ausführungsstatik oder der haustechnischen Anlagen."),
        ]),
        record(16, "Energie_und_Entwaesserungskonzept.pdf", "2027-04-23", "tga", "architekt", "Konzept für Energieversorgung und Grundstücksentwässerung", [
            T("Das Konzept koordiniert die Versorgung von acht Wohnungen mit 600 m² Wohnfläche. Energiebedarfsnachweis und Ausführungsberechnungen werden gesondert fortgeschrieben."),
            H("1 Wärmeerzeugung und Verteilung"),
            T("Vorgesehen ist eine elektrisch betriebene Luft-Wasser-Wärmepumpe mit witterungsgeführter Niedertemperaturverteilung und wohnungsweiser Verbrauchserfassung. Die vorläufige Anlagenkonfiguration umfasst zwei Wärmepumpen mit jeweils 18 kW Nennleistung. Die raumweise Heizlast, die tatsächliche Leistung am Auslegungspunkt und der Warmwasserbedarf sind gesondert zu berechnen; die Summe der Nennleistungen ist kein Ersatz für diese Bemessung. Die Warmwasserbereitung wird gesondert bemessen. Die Außeneinheit wird südöstlich neben dem Technikzugang angeordnet; die Schallbewertung muss vor Gerätebestellung den konkreten Typ und den Nachtbetrieb erfassen."),
            H("2 Gebäudehülle und Dach"),
            T("Für die weitere Berechnung werden Außenwand 0,18 W/(m²K), Dach 0,14 W/(m²K), Bodenplatte 0,20 W/(m²K) und Fenster 0,90 W/(m²K) als Planungsziele angesetzt. Diese Einzelwerte ersetzen keinen vollständigen energetischen Nachweis. Auf dem oberen Dach werden 80 Photovoltaikmodule mit je 450 Wp und jeweils 2,00 m² Modulfläche vorgesehen. Daraus ergeben sich 36 kWp und 160 m² Modulfläche bei insgesamt 300 m² Dachfläche über beide Dachniveaus. Die Anforderung an den solaren Dachflächenanteil und mögliche bautechnische Einschränkungen sind anhand der konkreten Dachgeometrie nachzuweisen. Wartungswege, Dachabläufe, Aufkantungen und die konstruktive Lastaufnahme sind in der Belegung berücksichtigt und vor Montage mit der Werkplanung abzugleichen. Alle acht Pkw-Plätze erhalten Leitungsinfrastruktur und Vorverkabelung; zunächst werden zwei Ladepunkte hergestellt. Lastmanagement und Netzanschluss sind mit der Netzbetreiberin abzustimmen."),
            H("3 Niederschlagswasser"),
            T("Wegen des schwach durchlässigen Bodens wird das Dachwasser über eine unterirdische Rückhaltung mit zunächst 12 m³ Nutzvolumen gesammelt. Als Arbeitsansatz für die Drosselung werden 1,0 l/s verwendet. Nutzvolumen und Abgabemenge sind vom Entwässerungsträger anhand des endgültigen Flächennachweises zu bestätigen. Ein Notüberlauf wird in den eigenen tiefer liegenden Gartenbereich geführt und darf weder Gebäudezugänge noch Nachbargrundstücke belasten."),
            H("4 Offene Nachweise"),
            T("Vor Ausschreibung sind Heizlast, Warmwasser, Netzanschluss, Schall, Dachbelegung und Entwässerung abschließend zu berechnen. Die Ansätze sind keine zugesicherte Geräteleistung. Die Grundstücksentwässerung setzt die erforderliche Zustimmung des zuständigen Trägers voraus."),
        ]),
        record(17, "Brandschutz_Barrierefreiheit_Konzept.docx", "2027-05-03", "architekt", "bauamt", "Konzept für Rettungswege und barrierefreie Nutzung", [
            T("Das Konzept gehört zum Bauantrag für acht Wohnungen. Die Ausführungsplanung konkretisiert Bauteilqualitäten, Anschlüsse und lichte Maße. Widersprüche zwischen Fachbeiträgen sind vor Bauteilfreigabe zu bereinigen."),
            H("1 Gebäude und Rettungswege"),
            T("Das Gebäude hat drei oberirdische Vollgeschosse. Der Fußboden des höchstgelegenen Aufenthaltsraums liegt 6,20 m über dem festgelegten Bezugsgelände. Acht eigenständige Wohnungen mit jeweils weniger als 400 m² werden vorgesehen. Der Bauantrag ordnet das Vorhaben der Gebäudeklasse 3 zu. Der erste Rettungsweg führt aus jeder Wohnung über den notwendigen Treppenraum ins Freie."),
            T("Der zweite Rettungsweg wird für die oberen Wohnungen über anleiterbare Fensterflächen an der nördlichen beziehungsweise seitlichen Fassade vorgesehen. Die zugehörigen Anleiterstellen und der Zugang sind im Lageplan markiert und dauerhaft freizuhalten. Die konkrete Erreichbarkeit und die Anleiterbarkeit der Fenster sind im Zuge der Genehmigungsbearbeitung abzustimmen. Die Fensterabmessungen und Brüstungshöhen werden im Ausführungsplan dokumentiert. Ein Aufzug ersetzt keinen Rettungsweg."),
            H("2 Bauliche Maßnahmen"),
            T("Tragende und aussteifende Bauteile sowie Decken werden in der für die Gebäudeklasse nachgewiesenen Qualität geplant. Trennbauteile zwischen Wohnungen, Treppenraumabschlüsse und Leitungsdurchführungen sind mit den jeweiligen Nachweisen abzustimmen. Ein allgemeiner Produktprospekt gilt nicht als Nachweis für einen bestimmten Einbau. Das Leitungs- und Abschottungskonzept wird vor Beginn der Rohinstallation in einer gemeinsamen Planrunde geprüft."),
            H("3 Barrierefreie Wohnungen"),
            T("Alle acht Wohnungen werden barrierefrei gestaltet und über stufenlose Wege und den Aufzug erreicht. WE 01 wird zusätzlich rollstuhlgerecht ausgeführt. Dort werden insbesondere 1,50 m × 1,50 m Bewegungsflächen, nutzbare Türanfahrbereiche und die Vorbereitung von Haltegriffen berücksichtigt. Die maßgeblichen lichten Maße sind vor Bestellung der Türen und Sanitärobjekte zu prüfen. Möblierung darf die freien Bewegungsflächen nicht unterschreiten."),
            H("4 Außenraum und Betrieb"),
            T("Der gekennzeichnete barrierefreie Pkw-Stellplatz wird nahe dem Hauseingang angeordnet und mit einem stufenlosen Zugang verbunden. 16 gesicherte Fahrradplätze und vier Besucherplätze werden ausgewiesen. Der Spielbereich liegt abseits der Zufahrt. Im späteren Betrieb müssen Rettungswege, Anleiterstellen und Bewegungsflächen frei bleiben; Abstellnutzungen des Treppenraums sind nicht in das Raumprogramm eingerechnet."),
        ]),
        record(18, "Bauantrag_Begleitschreiben.docx", "2027-05-10", "bauherr", "bauamt", "Bauantrag für den Neubau eines Achtfamilienhauses", [
            T("Sehr geehrte Damen und Herren, wir beantragen die Genehmigung für den Neubau eines Wohnhauses mit acht dauerhaft zu vermietenden Wohnungen am Wohnhof Am Steinbogen 18 in Hildesheim. Die digitale Einreichung umfasst die Antragsdaten, die von den verantwortlichen Beteiligten bestätigten Bauvorlagen und dieses Begleitschreiben. Das Schreiben ersetzt nicht die erforderlichen digitalen Antragsfelder und Nachweise."),
            H("1 Vorhaben"),
            T("Das nicht unterkellerte Gebäude erhält drei Vollgeschosse, eine Brutto-Grundfläche von 820 m² und eine Wohnfläche von 600 m². Erdgeschoss und erstes Obergeschoss messen außen jeweils 20,00 m × 15,00 m; das oberste Geschoss misst 20,00 m × 11,00 m. Die Höhe des Fußbodens des höchstgelegenen Aufenthaltsraums beträgt 6,20 m, die Attikahöhe 9,90 m. Ein Aufzug erschließt alle Geschosse. Sämtliche Wohnungen sind barrierefrei vorgesehen; WE 01 wird rollstuhlgerecht geplant."),
            H("2 Planungsrecht und Erschließung"),
            T("Wir legen der Einreichung eine Beurteilung der im Zusammenhang bebauten näheren Umgebung zugrunde und bitten um Prüfung der Einfügung nach § 34 BauGB. Die beigefügten Ansichten und die Grundstücksdarstellung erläutern Art und Maß der benachbarten Nutzung, Bauweise und überbaute Grundstücksflächen. Ein für das Vorhaben maßgeblicher qualifizierter Bebauungsplan wird in dieser Einreichung nicht geltend gemacht. Die Erschließungsunterlagen und die Grundstücksentwässerung sind Bestandteil der ergänzenden Nachweisführung."),
            H("3 Bauvorlagen"),
            T("Beigefügt sind die Baubeschreibung, der Lageplan LP01, die Grundrisse GP01 und GP02, Schnitt und Ansichten SP01, die Wohnflächenberechnung und das Konzept für Rettungswege und Barrierefreiheit. Die Fachbeiträge zum Tragwerk und zur Energieversorgung werden nach Maßgabe der Verfahrensanforderungen vervollständigt. Bitte teilen Sie uns mit, falls Sie weitere Unterlagen oder eine Präzisierung der eingereichten Darstellungen benötigen."),
            T("Ansprechpartnerin für die Bauherrin ist die Geschäftsführung; technische Rückfragen richten Sie bitte zugleich an das beauftragte Architekturbüro. Rechtsgeschäftliche Erklärungen, eine Änderung des Antrags oder ein Rechtsbehelfsverzicht bedürfen einer Erklärung der Bauherrin. Wir bitten um Bestätigung des Eingangs unter Angabe des Aktenzeichens."),
        ], attachments=["005_Lageplan_LP01.pdf", "011_Grundrisse_EG_1OG_GP01.pdf", "012_Grundriss_2OG_GP02.pdf", "013_Schnitt_Ansichten_SP01.pdf", "014_Wohnflaechenberechnung_acht_Wohnungen.docx", "017_Brandschutz_Barrierefreiheit_Konzept.docx", "019_Baubeschreibung.docx"]),
        record(19, "Baubeschreibung.docx", "2027-05-10", "architekt", "bauamt", "Baubeschreibung zum Wohnhausneubau", [
            T("Zum Antrag vom 10. Mai 2027: Die Steinbogen Wohnen GmbH errichtet acht Wohnungen zur langfristigen Vermietung. Beherbergung und gewerbliche Nutzung sind nicht beantragt."),
            H("1 Grundstück und Gebäude"),
            T("Das Grundstück hat eine Fläche von 1.300 m². Der Hauptbaukörper beansprucht 300 m² Grundfläche; das oberste Geschoss ist an der Südseite zurückgesetzt. Drei Vollgeschosse werden angegeben. Bei 6,20 m Höhe des obersten Aufenthaltsraumfußbodens und acht Nutzungseinheiten wird das Gebäude in Gebäudeklasse 3 eingeordnet. Die äußere Attika liegt bei 9,90 m. Die obere Dachoberfläche liegt bei 9,60 m, die Dachoberfläche der südlichen Rücksprungfläche bei 6,20 m. Unterkante der konstruktiven Bodenplatte ist −0,34 m. Der hieraus geometrisch ermittelte Rauminhalt beträgt 220 m² × 9,94 m + 80 m² × 6,54 m = 2.710,00 m³. Die Attika wird nicht pauschal als gesamte Dachhöhe angesetzt. Ein Keller wird nicht hergestellt."),
            H("2 Baukonstruktion"),
            T("Die Gründung erfolgt nach Tragwerks- und Baugrundplanung als Stahlbetonbodenplatte auf geeigneter Tragschicht. Tragende Wände werden aus Mauerwerk, Decken und Treppe aus Stahlbeton hergestellt. Die Außenwand erhält eine gedämmte, verputzte Konstruktion. Das obere Dach und die südliche Rücksprungfläche werden als abgedichtete Flachdächer ausgebildet. Die Rücksprungfläche ist Wartungsfläche und keine Gemeinschafts- oder Mieterdachterrasse."),
            H("3 Nutzung und Erreichbarkeit"),
            T("Die Wohnflächen betragen 225 m² im Erdgeschoss, 225 m² im ersten und 150 m² im zweiten Obergeschoss. Treppenraum und Aufzug mit drei Halten erschließen die acht barrierefreien Wohnungen; WE 01 wird zusätzlich rollstuhlgerecht. Trennbauteile und Anschlüsse folgen dem abgestimmten Schall- und Brandschutzkonzept."),
            H("4 Außenanlagen"),
            T("Es werden acht Pkw-Stellplätze freiwillig hergestellt, davon einer gekennzeichnet und barrierefrei nutzbar. Die Planung enthält 16 gesicherte Fahrradplätze und vier Besucherplätze. Der 30 m² große Spielbereich im südöstlichen Garten wird von den Verkehrsflächen getrennt. Niederschlagswasser wird zurückgehalten und nach gesonderter Abstimmung gedrosselt abgeleitet. Die erforderlichen Zustimmungen zur Grundstücksentwässerung bleiben gesondert nachzuweisen."),
            H("5 Technische Anlagen"),
            T("Wärmepumpe und Photovoltaik sind vorgesehen. Anlagenumfang, Schall- und Energienachweis erstellt die Fachplanung. Ein bestimmter Effizienzhausstandard und eine Förderung werden nicht zugesagt."),
        ]),
        record(20, "Nachforderung_Bauaufsicht.pdf", "2027-06-02", "bauamt", "bauherr", "Nachforderung zum Bauantrag", [
            T("Zum Bauantrag vom 10. Mai 2027 für das Wohnhaus mit acht Wohnungen wird das Aktenzeichen BA 2027 0618 geführt. Für die weitere Bearbeitung benötigen wir die nachstehend bezeichneten Ergänzungen. Dieses Schreiben enthält weder eine Baugenehmigung noch eine Freigabe vorzeitiger Arbeiten."),
            H("1 Lage und Rettungswege"),
            T("Bitte ergänzen Sie im Lageplan die freizuhaltenden Anleiterstellen und den zugehörigen Zugang. Die bisherige Stellplatzanordnung lässt nicht erkennen, ob die Anleiterstelle an der Nordostecke bei belegten Pkw-Plätzen erreichbar bleibt. Legen Sie außerdem eine bemaßte Darstellung der Abstandsflächen und eine nachvollziehbare Gegenüberstellung der Gebäudehöhen der näheren Umgebung vor."),
            H("2 Barrierefreie Nutzung"),
            T("Das Konzept bezeichnet sämtliche acht Wohnungen als barrierefrei und WE 01 als rollstuhlgerecht. In den bisher vorgelegten Plänen fehlen jedoch die lichten Türmaße, die Bewegungsflächen im Bad der WE 01 und die nutzbaren Abmessungen des Aufzugs. Bitte reichen Sie diese Angaben einschließlich des stufenlosen Wegs vom gekennzeichneten Stellplatz zum Hauseingang nach. Die pauschale Bezeichnung einer Wohnung ersetzt die erforderliche Darstellung nicht."),
            H("3 Entwässerung und Dach"),
            T("Bitte legen Sie die ergänzte Grundstücksentwässerungsplanung mit Rückhaltung, Drosselung und Notentwässerungsweg vor. Die Ableitung zum Nachbargrundstück ist auszuschließen. Ergänzen Sie ferner die Darstellung der Photovoltaikbelegung mit den für Wartung und Dachabläufe erforderlichen freien Bereichen."),
            H("4 Weiteres Verfahren"),
            T("Wir bitten um gebündelte Einreichung bis zum 30. Juni 2027 unter Angabe des Aktenzeichens und eindeutiger Kennzeichnung geänderter Planstände. Die bisher eingereichten Unterlagen verbleiben in der Akte; ersetzen Sie diese durch vollständige revidierte Pläne. Sollte die Frist nicht eingehalten werden können, bitten wir um frühzeitige Mitteilung mit Begründung und einem belastbaren Nachreichungstermin."),
        ]),
        record(21, "Antwort_Nachforderung.docx", "2027-06-24", "architekt", "bauamt", "Ergänzungen zum Bauantrag BA 2027 0618", [
            T("Sehr geehrte Damen und Herren, namens der Bauherrin reichen wir zu Ihrem Schreiben vom 2. Juni 2027 die ergänzten Darstellungen ein. Der Gebäudekörper, die Anzahl der Wohnungen und die beantragte Nutzung bleiben unverändert. Die nachstehenden Änderungen sind im Planverzeichnis als Revision 1 gekennzeichnet."),
            H("1 Anleiterstellen und Abstandsdarstellung"),
            T("Die nördliche Stellplatzreihe wurde um 0,80 m nach Westen versetzt. An der Nordostecke bleibt die markierte Anleiterzone frei; Poller oder Fahrradständer sind dort nicht vorgesehen. Der Zugang wird in einer durchgehend nutzbaren Breite von mindestens 1,25 m dargestellt. Die Gebäudeaußenkanten halten im gewählten Lageplan mindestens 6,25 m zu den seitlichen Grundstücksgrenzen und 11,00 m beziehungsweise 14,00 m zu Nord- und Südgrenze ein. Der südliche Rücksprung des obersten Geschosses vergrößert den Abstand dort zusätzlich."),
            H("2 Barrierefreiheit"),
            T("Die Ergänzung zeigt bei WE 01 freie Bewegungsflächen von 1,50 m × 1,50 m im Bad sowie die erforderlichen Anfahrbereiche an den Türen. Für die Wohnungseingänge werden 0,90 m lichte Durchgangsbreite vorgesehen. Der Aufzug erhält eine nutzbare Kabine von 1,10 m × 1,40 m und eine lichte Türbreite von 0,90 m. Die Fläche vor dem Aufzug bleibt von Türschwenkbereichen und Abstellnutzung frei. Die übrigen Wohnungen werden anhand der ausgewiesenen lichten Maße barrierefrei geplant."),
            H("3 Entwässerung und Photovoltaik"),
            T("Das Niederschlagswasser wird über eine Rückhaltung geführt. Im ergänzten Fachplan ist der Notentwässerungsweg auf dem eigenen Grundstück eingetragen. Die endgültige Drosselmenge wird mit dem Entwässerungsträger gesondert festgelegt. Die Photovoltaikbelegung wahrt Wartungsstreifen und die Zugänglichkeit der Dachabläufe; technische Einbauten wurden aus diesen Bereichen herausgenommen."),
            H("4 Verzeichnis und Verbindlichkeit"),
            T("Die Revision betrifft Lageplan LP01, Barrierefreiheitsdetail BF01 und Dach- und Entwässerungsschema TE01. In den Grundrissen wird allein die Lage einzelner Türen und Einbauten präzisiert; Wohnflächen und Kubatur werden nicht geändert. Bitte führen Sie die bezeichneten Revisionen anstelle der entsprechenden Vorstände. Die Bauherrin bestätigt die Ergänzungen. Eine Freigabe zur Ausführung beantragen wir mit dieser Nachreichung nicht gesondert."),
        ], attachments=["005_Lageplan_LP01.pdf", "024_Ausfuehrungsdetails_AP01.pdf", "027_Koordinierter_Planstand_R01.pdf"]),
        record(22, "Baugenehmigung_BA20270618.pdf", "2027-07-16", "bauamt", "bauherr", "Baugenehmigung für das Achtfamilienhaus", [
            T("Aktenzeichen BA 2027 0618. Auf Ihren Antrag vom 10. Mai 2027 in der ergänzten Fassung vom 24. Juni 2027 wird der Neubau eines Wohnhauses mit acht Wohnungen am Wohnhof Am Steinbogen 18 in Hildesheim nach Maßgabe der zugehörigen genehmigten Bauvorlagen und der nachstehenden Nebenbestimmungen genehmigt. Die Entscheidung ergeht im vereinfachten Baugenehmigungsverfahren. Die Genehmigung erfasst den dafür gesetzlich bestimmten Prüfungsumfang; außerhalb dieses Umfangs bleiben die Bauherrin und die verantwortlichen Beteiligten zur Einhaltung der öffentlich-rechtlichen Anforderungen verpflichtet."),
            H("1 Gegenstand"),
            T("Genehmigt wird die Wohnnutzung in drei Vollgeschossen ohne Keller. Die Gebäudegrundfläche beträgt 300 m², die Grundfläche des obersten Geschosses 220 m². Der Fußboden des höchstgelegenen Aufenthaltsraums liegt bei 6,20 m, die Attika bei 9,90 m über dem festgelegten Bezugsgelände. Der Antrag bezeichnet das Gebäude als Gebäudeklasse 3. Die Entscheidung bezieht sich auf acht Wohnungen mit insgesamt 600 m² geplanter Wohnfläche; Änderungen an Nutzung, Kubatur oder wesentlichen Rettungswegen bedürfen vor ihrer Ausführung einer erneuten verfahrensrechtlichen Klärung."),
            H("2 Maßgebliche Unterlagen"),
            T("Maßgeblich sind die Antragsbeschreibung vom 10. Mai 2027, die Baubeschreibung, Lageplan LP01 in Revision 1, Grundrisse GP01 und GP02, Schnitt und Ansichten SP01 sowie die Nachreichung vom 24. Juni 2027 mit Barrierefreiheitsdetail BF01 und Entwässerungsschema TE01. Spätere Ausführungspläne werden durch ihre Erstellung nicht automatisch Bestandteil dieser Genehmigung. Bei Abweichungen ist vor Ausführung mit der Bauaufsicht abzustimmen, ob geänderte Bauvorlagen oder ein gesonderter Antrag erforderlich sind."),
            H("3 Nebenbestimmungen"),
            T("Die in den genehmigten Unterlagen bezeichneten Anleiterstellen und Zugänge sind frei von dauerhaften Einbauten und abgestellten Fahrzeugen zu halten. Die Ausführung der Grundstücksentwässerung setzt die erforderliche gesonderte Zustimmung des zuständigen Entwässerungsträgers voraus. Die Ableitung von Niederschlagswasser auf Nachbargrundstücke ist nicht zulässig. Vor Beginn der betroffenen Arbeiten sind die gesetzlich erforderlichen bautechnischen Nachweise und die für sie notwendigen Bestätigungen in der vorgeschriebenen Form vorzuhalten beziehungsweise einzureichen."),
            T("Sämtliche acht Wohnungen und die zugehörigen Wege sind entsprechend den eingereichten Darstellungen barrierefrei auszuführen; WE 01 ist zusätzlich rollstuhlgerecht herzustellen. Der gekennzeichnete Stellplatz und die im Antrag dargestellten Fahrradabstellanlagen sind spätestens zur Aufnahme der Nutzung nutzbar herzustellen. Der Spielbereich ist bis zur Nutzungsaufnahme entsprechend dem genehmigten Lageplan anzulegen."),
            H("4 Hinweise und Rechtsbehelf"),
            T("Erforderliche Anzeigen zum Baubeginn und zur Nutzung sind fristgerecht in der vorgeschriebenen Form abzugeben. Diese Genehmigung ersetzt keine privatrechtlichen Zustimmungen und keine außerhalb ihres Regelungsumfangs erforderlichen öffentlich-rechtlichen Erlaubnisse. Über Gebühren wird gesondert entschieden. Mit Arbeiten darf erst begonnen werden, wenn die gesetzlichen Voraussetzungen und die vor Baubeginn zu erfüllenden Anforderungen vorliegen."),
            T("Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Widerspruch bei der Stadt Hildesheim erhoben werden. Der Widerspruch ist schriftlich, zur Niederschrift oder in der gesetzlich zugelassenen elektronischen Form einzulegen. Eine einfache E-Mail genügt den Anforderungen an die elektronische Form nicht. Die Frist richtet sich nach der tatsächlichen Bekanntgabe; das Ausfertigungsdatum allein belegt diese nicht."),
        ]),
        record(23, "Abruf_LPH5_bis7.eml", "2027-07-21", "bauherr", "architekt", "Abruf der Ausführungsplanung und Vergabevorbereitung", [
            T("Uns liegt die Baugenehmigung vom 16. Juli 2027 seit dem 20. Juli vor. Wir rufen hiermit die Leistungsphasen 5 bis 7 nach unserem Architektenvertrag ab. Bitte bereiten Sie die Ausführungsplanung sowie die vergleichbaren Vergabeunterlagen für die sieben besprochenen Lose vor. Der Abruf umfasst keine eigenständige rechtliche Gestaltung der Bauvertragsklauseln; hierzu stimmen wir einen direkten Auftrag mit unserer Rechtsberatung ab."),
            T("Wir benötigen insbesondere die endgültige Türliste, die Details zu den schwellenlosen Anschlüssen und die koordinierte Durchbruchsplanung. Bei der Rücksprungfläche möchten wir am Wartungsdach festhalten. Eine spätere Dachterrasse wurde von uns nicht bestellt. Bitte nehmen Sie die Nebenbestimmungen der Baugenehmigung in die Termin- und Freigabeliste auf."),
            T("Die vorgesehenen Vergaben sollen bis November 2027 entscheidungsreif sein. Ziel bleibt der Baubeginn im Dezember 2027 und die Übergabe im September 2028. Informieren Sie uns unmittelbar, falls notwendige Fachnachweise oder Lieferzeiten diese Folge gefährden. Eine Vorbestellung von Aufzug oder Fenstern ohne unsere ausdrückliche Vergabeentscheidung ist nicht freigegeben."),
        ], attachments=["022_Baugenehmigung_BA20270618.pdf"]),
        record(24, "Ausfuehrungsdetails_AP01.pdf", "2027-06-24", "architekt", "bauherr", "Barrierefreiheitsdetails BF01", [], plan=True),
        record(25, "Koordinierung_Ausfuehrungsplanung.docx", "2027-08-20", "architekt", "bauherr", "Koordinierung der Ausführungsplanung", [
            T("In der Planrunde vom 20. August 2027 wurden die Ausführungsdetails für Rohbau, Hülle und technische Ausrüstung zusammengeführt. Grundlage sind die Genehmigung vom 16. Juli 2027 und die abgerufene dritte Vertragsstufe. Die Ergebnisse dienen der Bereinigung der Leistungsverzeichnisse; eine Unternehmervariante ist damit noch nicht genehmigt."),
            H("1 Schwellenloser Zugang und Sockel"),
            T("Die Außentür zum Hauseingang erhält eine schwellenlose Ausbildung mit unmittelbar vorgelagerter Entwässerungsrinne. Die Außenfläche fällt vom Gebäude weg; eine Aufkantung quer über den Zugang ist nicht zulässig. Abdichtung, Anschlussflansch und Entwässerung sind im Detail AP02 gemeinsam zu beschreiben. Die bisherige Standardposition der Fassadenfirma mit einer 4 cm hohen Türschwelle wird nicht in das Leistungsverzeichnis übernommen."),
            H("2 Sanitärschacht und Rohbau"),
            T("Die TGA legt den revidierten Schacht im Bereich der Wohnungen WE 02 und WE 05 vor. Die Durchbrüche bleiben innerhalb der durch die Tragwerksplanung bestätigten Öffnungszone. Ein zusätzlicher Kernbohrungswunsch im Treppenraum ist zurückgestellt. Durchführungen in raumabschließenden Bauteilen sind nach dem abgestimmten Abschottungskonzept auszuführen und vor Verschluss zu dokumentieren."),
            H("3 Aufzug und Türen"),
            T("Für den Aufzug werden drei Halte, 1,10 m × 1,40 m nutzbare Kabine und 0,90 m lichte Türbreite ausgeschrieben. Schachtmaße, Unterfahrt, Überfahrt und Befestigungskräfte sind aus den Herstellerangaben vor Rohbauabschluss abzugleichen. Das geforderte lichte Maß darf nicht mit dem Rohbaumaß verwechselt werden. Die Wohnungseingangstüren erhalten ebenfalls 0,90 m lichte Durchgangsbreite; Beschläge und Türschließer sind auf die vorgesehenen Nutzungsmöglichkeiten abzustimmen."),
            H("4 Noch offene Punkte"),
            T("Der endgültige Wärmepumpentyp und die Schallberechnung liegen noch nicht vor. Die TGA liefert die Unterlagen bis zum 3. September. Für die Dachabdichtung fehlen die freigegebenen Anschlüsse der Photovoltaikunterkonstruktion. Die Objektplanung lässt die entsprechenden Positionen bis zum Eingang dieser Beiträge als nicht zur Bestellung freigegeben kennzeichnen. Die Bauherrin hat keiner Ausführung auf Grundlage eines bloßen Katalogdetails zugestimmt."),
        ]),
        record(26, "Freigabe_Details_mit_Rueckfrage.eml", "2027-09-08", "bauherr", "architekt", "Freigabe der Details und Rückfrage zum Wartungsdach", [
            T("Wir geben die in Ihrer Planrunde vom 20. August erläuterten schwellenlosen Zugänge und die lichte Wohnungseingangsbreite von 0,90 m für die Ausschreibung frei. Die WE 01 bleibt rollstuhlgerecht. Bitte berücksichtigen Sie bei der Bemusterung, dass sich die Türen ohne übermäßige Bedienkräfte nutzen lassen. Den Eingang wollen wir nicht nachträglich durch eine kleine Stufe vereinfachen."),
            T("In einer älteren Visualisierung ist auf der Rücksprungfläche noch eine Sitzgruppe zu sehen. Diese Abbildung stammt aus der Variantenphase. Wir möchten ausdrücklich keine zur Wohnung gehörende Dachterrasse und keine entsprechende Angabe in einem Mietexposé. Bitte teilen Sie allen Planern und späteren Unternehmen den Stand Wartungsdach mit und entfernen Sie die Sitzgruppe aus den aktuellen Vertriebsbildern."),
            T("Bei der Wärmepumpe möchten wir die Gerätauswahl erst nach Eingang der Schallbewertung freigeben. Die am Telefon genannte Lieferalternative ist noch nicht bestellt. Bitte stellen Sie Kosten- und Terminfolge einer Änderung nachvollziehbar dar, bevor Sie sie in die Vergabeempfehlung aufnehmen."),
        ], attachments=["025_Koordinierung_Ausfuehrungsplanung.docx"]),
        record(27, "Koordinierter_Planstand_R01.pdf", "2027-06-24", "tga", "architekt", "Dach und Entwässerung TE01", [], plan=True),
        record(28, "Flaechen_Abstaende_Aussenanlagen.pdf", "2027-09-15", "architekt", "bauherr", "Flächennachweis und Außenanlagenstand", [
            T("Der Nachweis vom 15. September 2027 fasst die Flächenansätze für Ausschreibung und Bauablauf zusammen. Er bezieht sich auf ein 1.300 m² großes Grundstück mit 32,50 m × 40,00 m. Die Maße stammen aus der projektbezogenen Arbeitsvermessung und sind vor Absteckung mit der verantwortlichen Vermessung abzugleichen."),
            H("1 Baukörper und Abstände"),
            T("Der Hauptbaukörper liegt von x 6,25 m bis x 26,25 m und von y 14,00 m bis y 29,00 m im örtlichen System. Norden liegt bei wachsendem y. Damit betragen die seitlichen Grenzabstände jeweils 6,25 m, der Abstand zur nördlichen Grenze 11,00 m und zur südlichen Grenze 14,00 m. Das zweite Obergeschoss nimmt den Bereich y 18,00 m bis y 29,00 m ein. Die Gebäudegrundfläche beträgt 300 m². Der rechnerische Mindestansatz von 0,5 × 9,90 m ergibt 4,95 m; in den gezeichneten Hauptfassadenbereichen liegen die tatsächlichen Abstände darüber. Sonderkonstellationen und Bauteile sind nach dem genehmigten Lageplan gesondert zu beurteilen."),
            H("2 Nutzungsflächen im Freien"),
            T("Die acht Pkw-Stellplätze enthalten einen 3,50 m × 5,00 m großen gekennzeichneten Platz nahe dem Hauseingang. Die übrigen Plätze werden mit jeweils 2,50 m × 5,00 m geplant. Die gemeinsame Fahrgasse ist 6,00 m breit. Die erforderlichen Bewegungs- und Einfahrtsflächen dürfen nicht als zusätzliche Stellplätze vermietet werden. Die freizuhaltende Anleiterzone bleibt außerhalb der Stellplatzflächen."),
            T("Für 16 gesicherte Fahrräder wird eine eingehauste Abstellfläche mit geeigneten Anschließmöglichkeiten vorgesehen; vier weitere Plätze liegen am Eingang. Der 30 m² große Spielbereich liegt im südöstlichen Garten. Der übrige Garten bleibt begrünt. Die Rückhaltung wird unter einer zugänglichen Außenfläche angeordnet, so dass Kontrollöffnungen erreichbar bleiben."),
            H("3 Abstimmungsstand"),
            T("Die Ausschreibung muss zwischen befestigten Flächen, Spielbereich, Vegetationsflächen und Entwässerungsanlagen unterscheiden. Die endgültigen Aufmaße werden für die Abrechnung vor Ort festgestellt. Eine Nachverdichtung der Stellplätze, ein Carport oder eine spätere Terrassennutzung ist nicht Bestandteil dieses Stands und darf nicht ohne Prüfung der Genehmigungslage umgesetzt werden."),
        ]),
        record(29, "Abschluss_Ausfuehrungsplanung.docx", "2027-09-24", "architekt", "bauherr", "Übergabe des koordinierten Ausführungsstands", [
            T("Wir übergeben den koordinierten Stand für die Vorbereitung der Vergabe. Er umfasst das unveränderte Wohnungsprogramm, die abgestimmten Barrierefreiheitsmaßnahmen und die genehmigte Kubatur. Die weiter unten bezeichneten unternehmerbezogenen Unterlagen werden nach Vergabe geprüft; sie sind kein Anlass, fachlich noch offene Entscheidungen als bereits erledigt zu behandeln."),
            H("1 Abgestimmte Grundlagen"),
            T("Die Planung bleibt bei drei Vollgeschossen, 820 m² Brutto-Grundfläche und 600 m² Wohnfläche. Der Rücksprung über dem ersten Obergeschoss wird als Wartungsdach ausgeführt. Alle acht Wohnungen sind barrierefrei vorgesehen; WE 01 ist rollstuhlgerecht. Der Aufzug erschließt drei Halte. Die Nachforderung der Bauaufsicht wurde am 24. Juni beantwortet, die Genehmigung am 16. Juli erteilt. Die Nebenbestimmungen werden im Bauablauf fortgeführt."),
            H("2 Schnittstellen der Vergabe"),
            T("Die sieben Lose umfassen Rohbau, Dach und Fassade und Fenster, Heizung und Lüftung und Sanitär, Elektro und Photovoltaik, Innenausbau, Aufzug sowie Außenanlagen. An den Losgrenzen sind insbesondere Abdichtungsanschlüsse, Durchbrüche, Brandschutzabschottungen, Stromversorgung des Aufzugs und der Wärmepumpe sowie die Erdarbeiten für die Rückhaltung ausdrücklich zuzuordnen. Eine Leistung darf nicht allein wegen einer Schnittstelle in beiden Leistungsverzeichnissen unbemerkt abgerechnet werden."),
            H("3 Werkplanung und Freigaben"),
            T("Die Aufzugsfirma liefert nach Vergabe die produktspezifische Werkplanung; die Tragwerksplanung prüft die übergebenen Lasten und Befestigungspunkte. Die Fensterfirma legt die Detailanschlüsse und die lichten Durchgänge vor Fertigung vor. Die Photovoltaikmontage wird mit Dachabdichtung und Tragwerk abgestimmt. Diese Prüfungen sind vor den jeweils betroffenen Arbeiten einzuplanen. Eine Vergabeentscheidung ersetzt die technische Freigabe der Werkplanung nicht."),
            H("4 Offene Entscheidung der Bauherrin"),
            T("Für die Wärmepumpe liegen zwei technisch mögliche Geräte vor. Der Vergleich wird mit den endgültigen Angeboten und dem Schallnachweis abgeschlossen. Die Bauherrin entscheidet hierüber im Rahmen der Vergabe. Die zuvor zurückgestellte Dachterrasse wird nicht als Wahlposition aufgenommen. Änderungen gegenüber dem vorliegenden Stand sind in der Vergabeempfehlung mit Kosten, Terminfolge und gegebenenfalls Genehmigungsbedarf darzustellen."),
            T("Die Unterlagen sind zur Ausschreibung freigegeben. Bestellungen setzen Auftrag, freigegebene Werkplanung und erforderliche Nachweise voraus. Spätere Revisionen werden mit Empfängern und Ausgabedatum protokolliert."),
        ], attachments=["150_Detailplanung_Schwelle_und_Deckendurchbruch.pdf"]),
        record(150, "Detailplanung_Schwelle_und_Deckendurchbruch.pdf", "2027-08-21", "architekt", "bauherr", "Ausführungsdetails zum Eingang und Sanitärschacht", [], plan=True),
    ]


def plan_canvas(filename, title, date, ident, scale):
    setup_fonts()
    path = Path(CASE) / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(path), pagesize=landscape(A3), invariant=1)
    c.setTitle(title)
    c.setSubject("Technische Bauzeichnung")
    c.setAuthor("Klotzkette")
    c._plan_info = (title, date, ident, scale)
    frame(c)
    return c


def font(c, size=9, bold=False):
    # Standard PDF fonts keep the technical drawings independently reproducible.
    c.setFont("HildesheimBold" if bold else "Hildesheim", size)


def frame(c):
    w, h = landscape(A3)
    title, date, ident, scale = c._plan_info
    c.setStrokeColor(HexColor("#263540")); c.setLineWidth(.5)
    c.rect(12*mm, 12*mm, w-24*mm, h-24*mm)
    font(c, 17, True); c.drawString(20*mm, h-27*mm, title)
    font(c, 10); c.drawString(20*mm, h-35*mm, "Wohnhof Am Steinbogen 18 | Hildesheim | Acht Wohnungen zur Vermietung")
    c.line(12*mm, 34*mm, w-12*mm, 34*mm)
    font(c, 9, True); c.drawString(20*mm, 25*mm, f"{ident}  |  {scale} bei Ausdruck auf A3 ohne Anpassung")
    font(c, 8); c.drawString(20*mm, 18*mm, f"Stand {date}  |  Steinbogen Wohnen GmbH  |  Maße in m, Detailmaße in cm")
    c.drawRightString(w-20*mm, 18*mm, f"Blatt {c.getPageNumber()}")


def text(c, x, y, s, size=8, bold=False):
    font(c,size,bold); c.drawString(x*mm,y*mm,s)


def dim(c, x1, y1, x2, y2, label):
    c.setLineWidth(.35); c.setStrokeColor(HexColor("#65727b"))
    c.line(x1*mm,y1*mm,x2*mm,y2*mm)
    if abs(y1-y2)<.01:
        for x in (x1,x2): c.line((x-1.2)*mm,(y1-1.2)*mm,(x+1.2)*mm,(y1+1.2)*mm)
        text(c,(x1+x2)/2-4,y1+2,label)
    else:
        for y in (y1,y2): c.line((x1-1.2)*mm,(y-1.2)*mm,(x1+1.2)*mm,(y+1.2)*mm)
        c.saveState(); c.translate((x1-2)*mm,(y1+y2)/2*mm); c.rotate(90); font(c,8); c.drawCentredString(0,0,label); c.restoreState()
    c.setStrokeColor(black)


def rect(c,x,y,w,h,fill=None,lw=.8):
    c.setLineWidth(lw); c.setStrokeColor(black)
    c.setFillColor(HexColor(fill) if fill else white)
    c.rect(x*mm,y*mm,w*mm,h*mm,stroke=1,fill=bool(fill))
    c.setFillColor(black)


def line(c,x1,y1,x2,y2,lw=.7):
    c.setLineWidth(lw); c.line(x1*mm,y1*mm,x2*mm,y2*mm)


def door(c,x,y,w=9,direction=1):
    # Door opening and swing in the horizontal wall, in drawing millimetres.
    c.setStrokeColor(white); c.setLineWidth(2.8); c.line(x*mm,y*mm,(x+w)*mm,y*mm)
    c.setStrokeColor(black); c.setLineWidth(.4)
    c.line(x*mm,y*mm,x*mm,(y+direction*w)*mm)
    if direction>0: c.arc((x-w)*mm,(y-w)*mm,(x+w)*mm,(y+w)*mm,0,90)
    else: c.arc((x-w)*mm,(y-w)*mm,(x+w)*mm,(y+w)*mm,270,90)


def north(c,x,y):
    line(c,x,y,x,y+14,1); line(c,x,y+14,x-2,y+10,1); line(c,x,y+14,x+2,y+10,1);text(c,x-1,y+17,"N",10,True)


def note_lines(c,x,y,lines,size=8,step=5):
    for i,s in enumerate(lines): text(c,x,y-i*step,s,size)


def draw_lage(c):
    # 1:200: one real metre is five drawing millimetres.
    x,y,k=35,45,5
    px=lambda v:x+v*k
    py=lambda v:y+v*k
    rect(c,x,y,32.5*k,40*k,None,.8)
    c.setDash(3,2);line(c,x-8,y+41*k,x+32.5*k+8,y+41*k);c.setDash()
    text(c,x+20,y+41*k+2,"Wohnhof Am Steinbogen",10,True)
    rect(c,px(6.25),py(14),100,75,"#e8eef2",1.5)
    c.setDash(3,2); line(c,px(6.25),py(18),px(26.25),py(18)); c.setDash()
    note_lines(c,px(8),py(24),["Neubau 20,00 x 15,00", "3 Vollgeschosse", "Attika +9,90", "EG ±0,00 = Bezugsgelände"],8)
    text(c,px(8),py(17),"Rücksprung 2. OG 4,00",7)
    # Four spaces north, four west of the drive.
    for i in range(4):
        xx=6.25+(3.5 if i else 0)+(i-1)*2.5 if i else 6.25
        ww=3.5 if i==0 else 2.5
        rect(c,px(xx),py(35),ww*k,5*k,"#f3f3f3",.4);text(c,px(xx)+2,py(36),f"P{i+1}",7)
    for i in range(4):
        rect(c,px(.5),py(13+i*5.0),2.5*k,5*k,"#f3f3f3",.4);text(c,px(.6)+2,py(15+i*5),f"P{i+5}",7)
    text(c,px(6.25),py(33),"P1 barrierefrei 3,50 x 5,00",6.5)
    c.setDash(2,2); rect(c,px(23.0),py(31),3.25*k,7*k,None,.5); c.setDash()
    text(c,px(23.1),py(35),"Anleiter-",6);text(c,px(23.1),py(33.7),"zone frei",6)
    rect(c,px(22),py(3),5*k,6*k,"#e6efe2"); text(c,px(22.4),py(6),"Spiel 30 m²",7)
    rect(c,px(4),py(3),8*k,3*k,"#eceded");text(c,px(4.4),py(4),"16 Fahrradplätze",7)
    rect(c,px(27),py(31),4*k,2*k,"#eceded");text(c,px(27.1),py(31.7),"4 Fahrräder",6.5)
    c.setDash(2,2);rect(c,px(14),py(6),4*k,3*k,None,.5);c.setDash();text(c,px(13),py(5),"Rückhaltung unter Gelände",6.5)
    for yy in (11,25): c.circle(px(30)*mm,py(yy)*mm,7,stroke=1,fill=0)
    dim(c,x,y-5,x+32.5*k,y-5,"32,50")
    dim(c,x-7,y,x-7,y+40*k,"40,00")
    dim(c,px(6.25),py(14)-6,px(26.25),py(14)-6,"20,00")
    north(c,222,235)
    note_lines(c,235,245,["1 Grundstück und Bezug", "1.300 m² | örtliches Koordinatensystem", "Südwestecke x 0,00 / y 0,00", "Norden in positiver y-Richtung", "", "2 Abstände Hauptbaukörper", "West 6,25 | Ost 6,25", "Nord 11,00 | Süd 14,00", "Gebäude x 6,25 bis 26,25", "Gebäude y 14,00 bis 29,00", "2. OG y 18,00 bis 29,00", "", "3 Revision 1 vom 24.06.2027", "Anleiterzone von Stellplätzen getrennt.", "Stufenloser Zugang über Nordseite.", "Pkw-Fahrgasse 6,00 m freihalten.", "", "4 Planungsgrundlage", "Projektbezogene Arbeitsvermessung.", "Kein Auszug aus dem Liegenschaftskataster.", "Grenzfeststellung und amtliche Bauvorlagen", "werden durch diese Übersicht nicht ersetzt."],8,6)


def draw_neighbours(c):
    x,y,k=101,107,2.5
    p=lambda a:x+a*k
    q=lambda a:y+a*k
    rect(c,p(0),q(0),32.5*k,40*k,None,.7)
    rect(c,p(6.25),q(14),20*k,15*k,"#d8e6ef",1.2)
    text(c,p(7),q(22),"Neubau",9,True)
    text(c,p(7),q(19),"3 Geschosse",7)
    for xx,yy,ww,dd,label,desc in [
        (-20,17,15,15,"Westhaus","Wohnen | 3 Geschosse | 10,20 m"),
        (36,18,16,13,"Osthaus","Wohnen | 2 Geschosse + Dach | 9,60 m"),
        (0,-17,15,12,"Südwesthaus","Wohnen | 2 Geschosse | 8,20 m"),
        (18,-17,14,14,"Südosthaus","Wohnen | 3 Geschosse | 10,10 m"),
    ]:
        rect(c,p(xx),q(yy),ww*k,dd*k,"#edf0ef",.7)
        text(c,p(xx)+3,q(yy+dd/2),label,7)
    c.setDash(3,2);line(c,p(-24),q(40),p(56),q(40));line(c,p(-24),q(46),p(56),q(46));c.setDash()
    text(c,p(-2),q(42),"Wohnhof Am Steinbogen",9)
    dim(c,p(0),q(-2),p(32.5),q(-2),"32,50")
    north(c,272,239)
    note_lines(c,282,233,["1 Umgebungsaufnahme", "Westhaus: 3 Geschosse, oberer", "Abschluss 10,20 m.", "Osthaus: 2 Geschosse und Dach,", "Firsthöhe 9,60 m.", "Südwesthaus: 2 Geschosse,", "Firsthöhe 8,20 m.", "Südosthaus: 3 Geschosse,", "oberer Abschluss 10,10 m.", "", "2 Nutzungsbefund", "Die aufgenommenen Häuser dienen", "der Wohnnutzung. Keine gewerbliche", "Nutzung war bei der Ortsaufnahme", "an diesen Gebäuden erkennbar.", "", "3 Abgrenzung", "Darstellung der unmittelbaren Umgebung", "nach Ortsaufnahme und Arbeitsmaßen.", "Beurteilung der näheren Umgebung bleibt", "Teil der Genehmigungsprüfung.", "Kein amtlicher Katasterauszug."],8,6)
    text(c,35,50,"Maßstab 1 zu 400; Maße und Höhenangaben sind gegenüber der Grafik maßgeblich.",8)


def draw_floor(c,level):
    x,y,k=32,(100 if level==2 else 68),10
    # Geometric planning diagram with building envelope and room boundaries.
    upper=level==2
    depth=11 if upper else 15
    rect(c,x,y,200,depth*k,"#fafafa",1.5)
    rect(c,x+3,y+3,194,depth*k-6,None,.6)
    if not upper:
        # Three dwellings around a north-facing circulation core.
        line(c,x,y+50,x+200,y+50,1.2)
        line(c,x+78,y+50,x+78,y+150,1.2);line(c,x+117,y+50,x+117,y+150,1.2)
        line(c,x+38,y+50,x+38,y+103); line(c,x,y+103,x+78,y+103)
        line(c,x+117,y+103,x+200,y+103);line(c,x+157,y+50,x+157,y+103)
        for xx in (40,80,120,160): line(c,x+xx,y,x+xx,y+28)
        line(c,x,y+28,x+80,y+28);line(c,x+120,y+28,x+200,y+28)
        line(c,x+78,y+82,x+117,y+82)
        rect(c,x+81,y+115,14,24);rect(c,x+99,y+114,15,20)
        for yy in range(117,139,3): line(c,x+81,y+yy,x+95,y+yy,.4)
        text(c,x+81,y+144,"Treppe",7);text(c,x+99,y+125,"Lift",7)
        if level==0:door(c,x+91,y+150,9,-1)
        door(c,x+87,y+50,9,1)
        for xx,side in ((78,1),(117,-1)):
            c.saveState();c.translate((x+xx)*mm,(y+91)*mm);c.rotate(90);door(c,0,0,9,side);c.restoreState()
        label=(1,2,3) if level==0 else (4,5,6)
        text(c,x+9,y+133,f"WE {label[0]:02d} | 68 m²",11,True)
        text(c,x+124,y+133,f"WE {label[1]:02d} | 75 m²",11,True)
        text(c,x+84,y+35,f"WE {label[2]:02d}",10,True);text(c,x+84,y+21,"82 m²",9)
        for xx in (10,125):
            text(c,x+xx,y+117,"Wohnen und Küche",8)
            text(c,x+xx,y+87,"Schlafen",8);text(c,x+xx+37,y+87,"Zimmer",8)
            text(c,x+xx,y+59,"Bad / Flur / Abstellen",7)
        for xx,lab in ((7,"Wohnen"),(45,"Schlafen"),(124,"Zimmer 1"),(166,"Zimmer 2")):
            text(c,x+xx,y+13,lab,7)
        text(c,x+9,y+40,"Küche",7);text(c,x+129,y+40,"Bad / Flur / Abstellen",7)
    else:
        line(c,x+80,y+40,x+80,y+110,1.2);line(c,x+120,y+40,x+120,y+110,1.2)
        line(c,x+80,y+40,x+120,y+40,1.2);line(c,x+100,y,x+100,y+40,1.2)
        for xx in (0,120):
            line(c,x+xx,y+45,x+xx+80,y+45);line(c,x+xx+40,y,x+xx+40,y+45)
        rect(c,x+83,y+75,14,24);rect(c,x+102,y+75,15,20)
        for yy in range(77,99,3):line(c,x+83,y+yy,x+97,y+yy,.4)
        text(c,x+6,y+92,"WE 07 | 75 m²",11,True);text(c,x+125,y+92,"WE 08 | 75 m²",11,True)
        text(c,x+8,y+69,"Wohnen und Küche",8);text(c,x+125,y+69,"Wohnen und Küche",8)
        for xx in (8,128):text(c,x+xx,y+22,"Schlafen",8);text(c,x+xx+41,y+22,"Zimmer",8)
        text(c,x+82,y+57,"Flur",7);text(c,x+104,y+83,"Lift",7)
        for xx,side in ((80,1),(120,-1)):
            c.saveState();c.translate((x+xx)*mm,(y+58)*mm);c.rotate(90);door(c,0,0,9,side);c.restoreState()
        c.setDash(3,2);rect(c,x,y-40,200,40,None,.5);c.setDash()
        text(c,x+15,y-24,"Rücksprungfläche 4,00 m | Wartungsdach | keine Dachterrasse",9)
    for wx in (12,48,130,168):
        for wy in (0,depth*k):
            c.setStrokeColor(white);c.setLineWidth(3);c.line((x+wx)*mm,(y+wy)*mm,(x+wx+14)*mm,(y+wy)*mm)
            c.setStrokeColor(black);line(c,x+wx,y+wy-1,x+wx+14,y+wy-1,.45);line(c,x+wx,y+wy+1,x+wx+14,y+wy+1,.45)
    dim(c,x,y-9,x+200,y-9,"20,00"); dim(c,x-8,y,x-8,y+depth*k,f"{depth},00")
    north(c,246,229)
    note_lines(c,260,231,[f"1 {'Erdgeschoss' if level==0 else ('Erstes Obergeschoss' if level==1 else 'Zweites Obergeschoss')}", f"Fußboden {'±0,00' if level==0 else ('+3,10' if level==1 else '+6,20')} m", "Außenwände und Wohnungsgrenzen", "durch Linien dargestellt.", "Raumordnungs- und Erschließungsplan.", "", "2 Flächen", f"Wohnfläche {'225,00' if level<2 else '150,00'} m²", f"Brutto-Grundfläche {'300,00' if level<2 else '220,00'} m²", "Maßgeblich ist die Raumflächenliste.", "Möblierung nach Detailplanung.", "", "3 Erreichbarkeit", "Alle Wohnungen barrierefrei geplant.", "WE 01 zusätzlich rollstuhlgerecht.", "Lift mit drei Halten, Kabine 1,10 x 1,40.", "Türdetails und Bewegungsflächen BF01.", "", "4 Nutzung", "Keine Keller- oder Dachterrassenfläche.", "Technik und Fahrradabstellen ebenerdig.", "Plan dient der Entwurfskoordination.", "Fertigungsmaße vor Bestellung prüfen."],8,6)


def draw_section(c):
    x,y,k=35,75,10
    for z in (0,3.1,6.2):
        width=150 if z<6.2 else 110
        start=0 if z<6.2 else 40
        rect(c,x+start,y+z*k,width,2.2,"#d4dce2",.8)
    rect(c,x,y,3.6,62,"#dde5eb");rect(c,x+146.4,y,3.6,99,"#dde5eb")
    rect(c,x+40,y+62,3.6,37,"#dde5eb")
    rect(c,x+40,y+93.5,110,2.5,"#d4dce2")
    rect(c,x+40,y+96,3.6,3,"#dde5eb");rect(c,x+146.4,y+96,3.6,3,"#dde5eb")
    rect(c,x,y-3.4,150,3.4,"#d4dce2",.5)
    line(c,x-12,y,x+158,y,1.3)
    for z,lab in ((0,"±0,00 EG"),(31,"+3,10 1. OG"),(62,"+6,20 2. OG"),(99,"+9,90 Attika")):
        line(c,x+153,y+z,x+161,y+z,.5);text(c,x+163,y+z-1,lab,9)
    text(c,x+47,y+79,"Aufenthaltsräume 2. OG",9)
    text(c,x+20,y+45,"Aufenthaltsräume 1. OG",9)
    text(c,x+20,y+14,"Aufenthaltsräume EG",9)
    text(c,x+2,y+66,"Wartungsdach",7)
    dim(c,x,y-12,x+150,y-12,"15,00");dim(c,x+40,y+108,x+150,y+108,"11,00")
    dim(c,x-8,y,x-8,y+99,"9,90")
    text(c,35,205,"1 Schnitt Süd nach Nord",11,True)
    # North facade with actual window rectangles.
    bx,by=260,63
    rect(c,bx,by,125,61.875,None,1.2)
    for zz in (5,24,43):
        for xx in (8,35,79,105):rect(c,bx+xx,by+zz,10,10,None,.5)
    rect(c,bx+55,by,15,16,None,.6)
    text(c,260,136,"2 Nordansicht 1 zu 160",11,True)
    note_lines(c,260,224,["3 Bezug und Gebäudehöhe", "Bezugsgelände ±0,00 an der Nordfassade.", "Höchster Aufenthaltsraumfußboden +6,20.", "Drei Vollgeschosse, kein Keller.", "Schnittdarstellung 1 zu 100.", "", "4 Planungsstand", "Deckenstärke als Arbeitsansatz 22 cm.", "Endgültige Statik gesondert.", "Dachaufbau nach Wärmeschutzplanung.", "Dachoberfläche oben +9,60 m.", "Unterkante Bodenplatte -0,34 m.", "BRI 220 x 9,94 + 80 x 6,54", "= 2.710,00 m³; ohne Attikaaufschlag."],8,6)


def draw_details(c):
    # Plan of accessible bathroom and lift as measurable vector drawing.
    text(c,30,240,"1 WE 01 Bad und Bewegungsfläche 1 zu 25",11,True)
    x,y,k=35,85,40
    rect(c,x,y,2.8*k,2.5*k,None,1.2)
    rect(c,x,y,60,60,"#e7edf2");text(c,x+6,y+8,"Dusche bodengleich 1,50 x 1,50",7)
    c.setDash(2,2);rect(c,x+.6*k,y+.3*k,1.5*k,1.5*k,None,.5);c.setDash()
    text(c,x+.6*k+4,y+.8*k,"1,50 x 1,50",9)
    c.ellipse((x+48)*mm,(y+72)*mm,(x+64)*mm,(y+100)*mm,stroke=1,fill=0)
    text(c,x+49,y+81,"WC",7)
    rect(c,x+96,y+48,16,25,None,.5);text(c,x+98,y+58,"WT",7)
    door(c,x+70,y,36,-1)
    dim(c,x,y-10,x+112,y-10,"2,80");dim(c,x-8,y,x-8,y+100,"2,50")
    note_lines(c,180,217,["2 Festlegungen", "Freie Bewegungsfläche 1,50 x 1,50 m.", "Tür lichte Breite 0,90 m.", "Tür nach außen öffnend im Ausführungsstand.", "WC seitlich jeweils mindestens 0,90 m frei.", "Waschmaschine im Abstellraum.", "Waschtisch unterfahrbar vorsehen.", "Rutschhemmung und Haltegriffbefestigung", "vor Bestellung produktbezogen abstimmen.", "", "3 Aufzugskabine 1 zu 25"],8,6)
    rect(c,190,80,44,56,None,1.2)
    c.setStrokeColor(white);c.setLineWidth(3);c.line(194*mm,80*mm,230*mm,80*mm);c.setStrokeColor(black)
    line(c,194,78,212,78,.5);line(c,212,79,230,79,.5)
    text(c,191,66,"Schiebetür 0,90 m licht",7)
    text(c,194,107,"1,10 x 1,40",8)
    dim(c,190,72,234,72,"1,10");dim(c,182,80,182,136,"1,40")
    note_lines(c,270,150,["Nutzbare Kabinenmaße dargestellt.", "Schachtmaße nach Herstellerplanung.", "Tür lichte Breite 0,90 m.", "Drei Halte EG, 1. OG, 2. OG.", "Bewegungsfläche vor dem Aufzug", "frei von Türschwenkbereichen halten.", "", "4 Prüfung vor Ausführung", "Bewegungsflächen und Bedienelemente", "im gesamten Zugangsweg abstimmen.", "Diese Detailzeichnung ersetzt keinen", "vollständigen Barrierefreiheitsnachweis."],8,6)


def draw_roof(c):
    x,y,k=32,72,10
    rect(c,x,y,200,110,"#f3f6f7",1.2)
    for r in range(5):
        for col in range(16):rect(c,x+20+col*10,y+5+r*20,10,20,"#d8e6ed",.35)
    text(c,x+8,y+117,"80 Module je 450 Wp | 36 kWp | 160 m² Modulfläche",9)
    c.setDash(3,2);line(c,x+4,y+7,x+196,y+7);line(c,x+194,y+7,x+194,y+103);c.setDash()
    for xx,yy in ((6,6),(193,103)):
        c.circle((x+xx)*mm,(y+yy)*mm,3*mm,stroke=1,fill=0)
        text(c,x+xx-2,y+yy-1,"D",7)
    dim(c,x,y-9,x+200,y-9,"20,00");dim(c,x-8,y,x-8,y+110,"11,00")
    text(c,32,201,"1 Dachaufsicht TE01",11,True)
    # Flow scheme with dimensions and arrows.
    rect(c,263,164,90,17,None,.6);text(c,268,171,"Dachabläufe und Sammelleitung",8)
    rect(c,263,125,90,23,None,.6);text(c,268,137,"Rückhaltung Nutzvolumen 12 m³",8);text(c,268,130,"Arbeitsansatz bis Fachbestätigung",7)
    rect(c,263,87,90,18,None,.6);text(c,268,94,"Drossel 1,0 l/s zum Kanal",8)
    for yy1,yy2 in ((164,148),(125,105)):
        line(c,308,yy1,308,yy2,.8);line(c,308,yy2,306,yy2+3);line(c,308,yy2,310,yy2+3)
    text(c,263,201,"2 Entwässerungsschema",11,True)
    note_lines(c,32,246,["Revision 1 vom 24. Juni 2027", "Wartungswege und Abläufe bleiben zugänglich.", "Rücksprungdach gesondert angeschlossen; keine Dachterrasse.", "Notentwässerung auf eigenes Grundstück, nicht zum Nachbarn."],8,6)
    note_lines(c,263,238,["Endgültige Bemessung und Zustimmung", "des Entwässerungsträgers erforderlich.", "Anlagenkonzept ist keine Einleiterlaubnis."],8,6)


def draw_execution(c):
    text(c,25,243,"1 Eingangsschwelle AP02 1 zu 10",11,True)
    # A measured section: every drawing millimetre corresponds to one centimetre.
    x,y=30,160
    rect(c,x,y-12,118,12,"#e8edf1",.7)
    rect(c,x,y-34,118,22,"#d1dae0",.8)
    rect(c,x,y-46,118,12,"#f1e6c7",.5)
    rect(c,x+118,y,6,48,"#d1dae0",.8)
    # Threshold frame and accessible external drain.
    rect(c,x+116,y-3,11,3,"#c0ced6",.8)
    rect(c,x+127,y-10,15,10,None,.7)
    for xx in range(128,142,2):line(c,x+xx,y,x+xx,y-2,.4)
    line(c,x+142,y,x+202,y-1.2,.9)
    line(c,x+142,y-6,x+202,y-7.2,.5)
    c.setStrokeColor(HexColor("#17608b"));line(c,x+90,y-4,x+126,y-4,1.2);line(c,x+126,y-4,x+126,y-1,1.2);c.setStrokeColor(black)
    text(c,x+4,y+5,"Innen FFB ±0,00",9);text(c,x+144,y+5,"Außen 2 % Gefälle",8)
    text(c,x+5,y-8,"Belag und Estrich 12 cm",8)
    text(c,x+5,y-26,"Stahlbetonplatte 22 cm",8)
    text(c,x+5,y-42,"Dämmung 12 cm",8)
    line(c,x+123,y+28,x+152,y+36,.5);text(c,x+154,y+35,"Rahmen / Anschlussflansch",8)
    line(c,x+135,y-6,x+166,y-20,.5);text(c,x+168,y-21,"Rinne 15 cm breit",8)
    line(c,x+105,y-4,x+165,y-35,.5);text(c,x+167,y-36,"Abdichtung blau",8)
    dim(c,x+127,y-17,x+142,y-17,"0,15")
    note_lines(c,25,86,["Schwelle ohne Höhenversatz; Türöffnung lichte Breite 0,90 m.", "Entwässerungsrinne unmittelbar vor dem Rahmen, an Entwässerung anschließen.", "Abdichtung mit geeignetem Anschlussflansch durchgehend anschließen.", "Die Türfirma und Abdichtungsfirma stimmen das konkrete System vor Fertigung ab.", "Keine nachträgliche Schwellenaufkantung ohne neue Freigabe."],8,6)
    text(c,270,243,"2 Deckenöffnung AP03 1 zu 10",11,True)
    bx,by=272,173
    rect(c,bx,by,105,22,"#d1dae0",.8)
    # Approved opening 16 x 16 cm around an 11 cm pipe.
    c.setFillColor(white);c.rect((bx+44)*mm,by*mm,16*mm,22*mm,stroke=0,fill=1);c.setFillColor(black)
    rect(c,bx+46.5,by-15,11,56,"#eef3f5",.6)
    c.setStrokeColor(HexColor("#aa5544"));line(c,bx+43,by,bx+61,by,2);c.setStrokeColor(black)
    dim(c,bx+44,by+32,bx+60,by+32,"0,16")
    dim(c,bx-5,by,bx-5,by+22,"0,22")
    line(c,bx+59,by-8,bx+90,by-19,.5);text(c,bx+63,by-26,"Rohr außen 110 mm",8)
    note_lines(c,270,116,["Öffnung 160 x 160 mm im Sanitärschacht.", "Lage nach freigegebener Aussparungsliste.", "Keine zusätzliche Bohrung im Auflagerbereich.", "Abschottung passend zu Bauteil und Rohrsystem.", "Eignung und Einbau nach Systemnachweis.", "Ausführung vor Verschluss fotografisch erfassen.", "Keine Vergrößerung ohne Tragwerksfreigabe."],8,6)
    note_lines(c,25,224,["Ausführungsstand 21.08.2027 | Freigabe Objektplanung und Fachplanerkoordination", "Maße vor Ort prüfen. Produktbezogene Werkplanung bleibt vor Bestellung abzugleichen."],8,6)


def build_plans():
    plans = [
        ("005_Lageplan_LP01.pdf", "Lageplan und Außenanlagen", "24.06.2027", "LP01 Revision 1", "1 zu 200", draw_lage),
        ("011_Grundrisse_EG_1OG_GP01.pdf", "Grundrisse Erdgeschoss und erstes Obergeschoss", "19.03.2027", "GP01", "1 zu 100", None),
        ("012_Grundriss_2OG_GP02.pdf", "Grundriss zweites Obergeschoss", "19.03.2027", "GP02", "1 zu 100", lambda c:draw_floor(c,2)),
        ("013_Schnitt_Ansichten_SP01.pdf", "Gebäudeschnitt und Nordansicht", "19.03.2027", "SP01", "wie bezeichnet", draw_section),
        ("024_Ausfuehrungsdetails_AP01.pdf", "Barrierefreiheitsdetails Wohnung und Aufzug", "24.06.2027", "BF01 Revision 1", "1 zu 25", draw_details),
        ("027_Koordinierter_Planstand_R01.pdf", "Dachbelegung und Grundstücksentwässerung", "24.06.2027", "TE01 Revision 1", "Dach 1 zu 100", draw_roof),
        ("150_Detailplanung_Schwelle_und_Deckendurchbruch.pdf", "Ausführungsdetails Eingang und Sanitärschacht", "21.08.2027", "AP02 und AP03 freigegeben", "1 zu 10", draw_execution),
    ]
    for name,title,date,ident,scale,drawer in plans:
        c=plan_canvas(name,title,date,ident,scale)
        if name.startswith("005_"):
            draw_lage(c);c.showPage();c._plan_info=("Umgebungsaufnahme und Baukörper",date,ident,"1 zu 400");frame(c);draw_neighbours(c)
        elif name.startswith("011_"):
            draw_floor(c,0);c.showPage();frame(c);draw_floor(c,1)
        else:drawer(c)
        c.save()


if __name__ == "__main__":
    build_records([r for r in documents() if not r.get("plan")])
    build_plans()
