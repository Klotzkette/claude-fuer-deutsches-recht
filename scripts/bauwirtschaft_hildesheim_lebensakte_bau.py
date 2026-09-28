"""Tagesgenaue Bauausführung und Detail-LV der fiktiven Hildesheimer Lebensakte.

Ergänzt den unveränderten Ausgangsfall. Alle Werte sind Simulationsdaten.
Fachliche Grundlagen und Grenzen: quality/hildesheim-lebensakte/bau/quellen.md.
"""
from __future__ import annotations

import argparse
import calendar
import csv
import io
import json
import hashlib
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

from bauwirtschaft_hildesheim_bau import LOTS
from bauwirtschaft_hildesheim_common import ACTORS, euro, written_norms
from bauwirtschaft_hildesheim_lebensakte_common import save_docx

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten' / 'bauwirtschaft-hildesheim-lebensakte'
SOURCE = ROOT / 'testakten' / 'bauwirtschaft-neubau-achtfamilienhaus-hildesheim'
QA = ROOT / 'quality' / 'hildesheim-lebensakte' / 'bau'
ASSETS = Path(os.environ.get('HILDESHEIM_LEBENSAKTE_ASSETS', '/tmp/hildesheim-lebensakte'))
REF = 'SW-HI-26-08'
AUTHOR = 'Klotzkette'
START, END = date(2027, 12, 1), date(2028, 9, 29)
WEEKDAYS = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
MONTHS = ['', 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
FOREMEN = {'rohbau': 'Georg Schmidt', 'huelle': 'Heinrich Bauer', 'hls': 'Alfred Müller', 'elektro': 'Wilhelm Fischer', 'ausbau': 'Walter Schneider', 'aufzug': 'Ludwig Weber', 'aussen': 'Ernst Hoffmann'}

# Untergliederungen der unverändert vereinbarten Pauschalpositionen. Kein Wechsel
# zu einem Einheitspreisvertrag; Mengen dienen Kalkulation und Fortschrittsprüfung.
# Je Zeile: Kurztext | Menge | Einheit | Einzelansatz EUR | projektbezogener Langtext.
DETAILS = {
'rohbau': [
'''Bauzaun mit Tor|145|m|40|Die Baustellengrenze erhält standsichere Zaunelemente und ein abschließbares Tor; der öffentliche Gehweg und die Nachbarzugänge bleiben frei.
Container und Sanitärbetrieb|10|Monat|900|Aufenthalts- und Sanitärcontainer werden auf dem freigegebenen Stellplatz eingerichtet, versorgt und regelmäßig gereinigt.
Kranaufstellung und Vorhaltung|1|Anlage|17000|Der Baustellenkran wird entsprechend Aufstellplanung und Tragfähigkeitsnachweis montiert, geprüft, betrieben und nach Rohbauabschluss demontiert.
Baustrom und Beleuchtung|1|Anlage|4200|Eine geprüfte Baustrom-Unterverteilung mit geschützten Leitungswegen und Baustellenbeleuchtung wird für den eigenen Rohbaubetrieb bereitgestellt.
Räumung der Einrichtung|1|Leistung|4000|Temporäre Flächen, Fundamente und Schutzmaßnahmen des Rohbaubetriebs werden geordnet zurückgebaut und die Flächen dem Folgegewerk übergeben.''',
'''Regulärer Bodenaushub|600|m³|45|Aushub und innerbetrieblicher Transport erfolgen abschnittsweise im planmäßigen Baufeld; Oberboden und Unterboden bleiben getrennt.
Abfuhr regulärer Überschussboden|420|m³|65|Überschüssiger Boden wird nur nach dokumentierter Deklaration an die dafür geeignete Annahmestelle abgegeben; Annahmescheine sind vorzulegen.
Gründungspolster|150|m³|85|Geeignetes mineralisches Material wird im freigegebenen Gründungsbereich lagenweise eingebaut; Schichtdicken und Verdichtungsverfahren sind mit der Baugrundplanung abzustimmen.
Gräben im Gründungsbaufeld|150|m|85|Die Gräben im Rohbaubaufeld werden einschließlich erforderlicher Sicherung hergestellt und nach Freigabe lagenweise verfüllt; Außenleitungen des Loses Außenanlagen sind nicht enthalten.
Verdichtungskontrollen|12|Prüfort|850|An zwölf vorab mit der Baugrundplanung abgestimmten Orten werden Tragfähigkeit und Verdichtung mit dem für Boden und Einbauzustand geeigneten Verfahren dokumentiert.''',
'''Bodenplatte Beton|90|m³|340|Die Bodenplatte wird nach Schalplan und freigegebener Betonfestlegung einschließlich Einbau, Verdichtung und Nachbehandlung hergestellt; Bewehrung und Schalung sind gesondert kalkuliert.
Decken und tragende Betonbauteile|246|m³|320|Die Geschossdecken und übrigen tragenden Betonbauteile werden in freigegebenen Takten hergestellt; Aussparungen, Durchführungen und Einbauteile sind vor jedem Takt abzugleichen.
Bewehrungsstahl|45|t|1700|Bewehrung wird nach freigegebenen Stahllisten geliefert, mit den geforderten Abstandhaltern eingebaut und vor dem Betonieren zur Kontrolle zugänglich gehalten.
Tragendes Mauerwerk|900|m²|145|Tragende Wände werden mit den in der Tragwerks- und Bauphysikplanung festgelegten Stein- und Mörtelsystemen einschließlich Anschlüssen und Überbindemaßen errichtet.
Schalflächen|800|m²|40|Schalung und temporäre Unterstützung werden entsprechend Belastung, Betonierfolge und vorgesehener Oberfläche ausgeführt; Ausschalfristen folgen der konkreten Festigkeitsentwicklung.
Treppenläufe|4|Stück|2920|Die vier Treppenläufe werden mit abgestimmten Auflager- und Schallschutzdetails eingebaut; Transport, Montage und Schutz bis zur Übergabe sind enthalten.''',
'''Nichttragende Rohbauwände|400|m²|115|Nichttragende massive Innenwände werden mit den planmäßigen Anschlüssen erstellt; Installationsschachtbekleidungen des Ausbaugewerks sind ausgeschlossen.
Aufzugschacht Rohbau|90|m²|320|Schachtwände und Auflager werden mit der Werkplanung des Aufzugs abgeglichen; Rohbaumaße dürfen nicht aus den lichten Kabinenmaßen abgeleitet werden.
Treppenpodeste|4|Stück|4200|Die Podeste werden mit den freigegebenen Lagerungen und Anschlussbewehrungen hergestellt; die angesetzten vier Bauteile sind im Schalplan eindeutig zu kennzeichnen.
Geplante Durchbruchschließungen|80|Stück|480|Die planmäßig vorgesehenen Öffnungen werden nach Einbau der Leitungen mit dem zugehörigen Rohbaumaterial geschlossen; zugelassene Leitungsabschottungen bleiben bei den Fachgewerken.
Sockelrohbau|100|m|180|Sockelabschnitte und Aufkantungen werden höhengerecht vorbereitet; der schwellenlose Haupteingang erhält die ausgesparte Anschlussgeometrie des Details AP02.
Rohbauanschlüsse|40|Stück|300|Die im Anschlussregister erfassten Wand- und Deckenanschlüsse werden vor dem Verdecken kontrolliert und für die nachfolgenden Gewerke dokumentiert.'''
],
'huelle': [
'''Dachabdichtung|300|m²|115|Beide Flachdachebenen werden mit dem abgestimmten Abdichtungssystem ausgeführt; die 80 m² große Rücksprungfläche bleibt Wartungsdach und wird nicht zur Terrasse ausgebaut.
Gefälledämmung|300|m²|110|Die Gefälledämmung wird gemäß Gefälleplan verlegt; Dämmwirkung, Druckbeanspruchung und Entwässerungswege werden gemeinsam mit Dachlasten und PV-Aufstellung geprüft.
Attika und Randanschlüsse|140|m|175|Rand- und Attikaanschlüsse werden einschließlich Ecken und Abdeckungen hergestellt; Anschlusslängen sind an den abgewickelten Detailmaßen zu prüfen.
Haupt und Notentwässerung|8|Stück|1750|Abläufe und Notentwässerung werden in der im Entwässerungsplan zugeordneten Funktion eingebaut; die acht kalkulierten Ablaufstellen sind keine frei austauschbaren Standardteile.
Dachdurchdringungen|8|Stück|1800|Durchdringungen werden mit systemverträglichen Anschlüssen und zugänglicher Kontrolle ausgeführt; zusätzliche Bohrungen für die PV-Anlage bedürfen vorheriger Abstimmung.
Temporärer Dachschutz|300|m²|32|Die fertige Abdichtung wird während nachfolgender Arbeiten gegen mechanische Beschädigung geschützt; Schutzlagen werden vor der Endkontrolle aufgenommen.''',
'''Fassadendämmsystem|620|m²|145|Die Fassadenflächen erhalten das freigegebene Gesamtsystem aus Dämmung, Befestigung und Putz; Systembestandteile verschiedener Hersteller dürfen nicht ungeprüft kombiniert werden.
Sockelabdichtung und Oberfläche|75|m²|160|Sockelzonen werden mit Spritzwasserschutz und abgestimmtem Übergang zur erdberührten Abdichtung hergestellt; Außenanlagen dürfen diese Anschlüsse nicht überbauen.
Laibungen und Fensteranschlüsse|220|m|65|Laibungen erhalten durchgehende Dämm- und Anschlussdetails; Anschlussprofile und Bewegungsmöglichkeiten der Fenster sind vor dem Putzauftrag abzustimmen.
Fassadengerüst|690|m²|20|Für den eigenen Fassadenumfang wird ein geeignetes Gerüst einschließlich Zugang, Prüfung und Anpassung gestellt; die Rohbaugerüste sind hiervon vertraglich getrennt.''',
'''Regelfenster|40|Stück|2000|Die vierzig Regelfenster werden nach freigegebener Fensterliste mit den festgelegten Öffnungsarten, Verglasungen und bauphysikalischen Eigenschaften geliefert und montiert.
Große Fensterelemente|8|Stück|3750|Die acht großen Elemente der Wohnbereiche folgen der Fensterliste; erforderliche Sicherheitsverglasung und Rettungsöffnungen sind elementbezogen auszuweisen.
Hauseingangselement|1|Stück|6000|Das Hauseingangselement wird mit der schwellenlosen Anschlussausbildung AP02 und den lichten Durchgangsmaßen eingebaut; eine vier Zentimeter hohe Standardschwelle ist nicht geschuldet.
Montagefugen|200|m|95|Die Anschlussfugen werden innen luftdicht, in der Fuge gedämmt und außen schlagregensicher nach dem freigegebenen Systemdetail hergestellt; der Untergrund ist vorab zu prüfen.
Außenfensterbänke|50|m|100|Fensterbänke und seitliche Anschlüsse erhalten die geplante Neigung und eine freie Wasserführung; verdeckte Dichtstoffraupen dürfen den Ablauf nicht behindern.''',
'''Außenliegender Sonnenschutz|24|Stück|1000|Die vierundzwanzig in der Fassadenliste bezeichneten Elemente erhalten motorisierten Sonnenschutz mit zugänglicher Wartungsmöglichkeit; Befestigungen berücksichtigen die Fassadenlasten.
Bedienung und Anschluss Sonnenschutz|24|Stück|250|Antriebe werden am bauseits bereitgestellten Übergabepunkt angeschlossen und funktionsbezogen gekennzeichnet; die feste Elektro-Zuleitung verbleibt im Elektrolos.
Fenster und Beschlageinstellung|48|Stück|100|Alle achtundvierzig Fenster werden auf Bedienbarkeit, Schließdruck und Funktionsfähigkeit geprüft; die Einstellung wird je Element dokumentiert.
Luftdichtheitskontrollen|2|Termin|1800|Ein baubegleitender und ein abschließender Kontrolltermin werden mit Energieplanung und Messdienst abgestimmt; abweichende Messbedingungen und Leckagen sind konkret aufzunehmen.
Pflege und Bestandsunterlagen|1|Satz|1600|Die Bauherrin erhält elementbezogene Pflegehinweise, Produktunterlagen und eine Liste zugänglicher Wartungspunkte; pauschale Haftungsausschlüsse sind nicht Bestandteil der Leistung.'''
],
'hls': [
'''Wärmepumpenkaskade|2|Stück|16500|Zwei Luft-Wasser-Wärmepumpen mit je 18 kW nominaler Leistung werden nach freigegebener Geräteauswahl aufgestellt; Heizlast, Leistungskennlinie und Schallbewertung bestimmen die Auslegung.
Speicher und Hydraulik|2|Stück|8000|Die abgestimmten Speicher werden mit Armaturen, Dämmung und hydraulischer Einbindung geliefert; ihre Aufgaben und Inhalte sind im Anlagenschema zu bezeichnen.
Wohnungsverteiler|8|Stück|2200|Jede Wohnung erhält einen zugänglichen, beschrifteten Heizkreisverteiler mit einzeln einstellbaren Kreisen; die Zugänglichkeit ist mit dem Ausbau zu sichern.
Flächenheizung|600|m²|65|Die beheizten Wohnflächen erhalten das geplante Rohrsystem mit raumbezogenen Verlegeabständen; die Rohrlage wird vor dem Estrich dokumentiert und geschützt.
Heizungsleitungen|220|m|80|Haupt- und Steigleitungen werden einschließlich Halterungen und Dämmung verlegt; Brandschutzdurchführungen werden mit den dafür vorgesehenen Systemen abgestimmt.
Regelung und Abgleich|1|Anlage|16800|Die Kaskadenregelung wird einschließlich hydraulischem Abgleich und wohnungsbezogenen Sollwerten eingerichtet; eine sommerliche Funktionsprobe ersetzt keine spätere Winterbeobachtung.''',
'''Trinkwasserleitungen|680|m|55|Kaltwasser, Warmwasser und Zirkulation werden in den geplanten Leitungswegen hygienegerecht installiert; nicht benötigte Totleitungen werden nicht eingebaut.
Schmutzwasserleitungen innen|300|m|65|Die inneren Abwasserleitungen werden mit planmäßigen Gefällen, Reinigungsmöglichkeiten und schallentkoppelten Befestigungen verlegt; Außenleitungen sind gesondert vergeben.
Sanitärausstattung Regelwohnungen|7|Bad|6500|Die sieben Bäder der Wohnungen 02 bis 08 werden nach freigegebener Ausstattungsliste einschließlich Armaturen und barrierefrei geplanten Bewegungsflächen eingerichtet.
Sanitärausstattung Wohnung 01|1|Bad|12500|Das rollstuhlgerechte Bad der Wohnung 01 erhält unterfahrbaren Waschtisch, freigehaltene Anfahrflächen und belastbare Haltegriffbefestigungen nach Detail BF01.
Technikanschlüsse Sanitär|1|Anlage|10100|Hausanschlussraum und Technikbereich erhalten die im Schema vorgesehenen Armaturen, Sicherungen und Entleerungen; Übergabepunkte zum Versorger sind eindeutig zu kennzeichnen.''',
'''Wohnungslüftungsgeräte|8|Stück|5500|Jede Wohnung erhält die dem Lüftungskonzept entsprechende Anlage mit zugänglichen Filtern und bedienbaren Betriebsstufen; Schallanforderungen sind gerätebezogen abzugleichen.
Lüftungsleitungen|180|m|70|Luftleitungen, Schalldämpfung und Kondensatführung werden mit Ausbauhöhen und Wartungszugängen koordiniert; nicht zugängliche Filterplätze sind unzulässig.
Durchführungen Lüftung|20|Stück|220|Die zwanzig kalkulierten Durchführungen werden nach dem jeweiligen Bauteil- und Brandschutzdetail ausgeführt und vor dem Verschließen nachvollziehbar bezeichnet.
Einregulierung der Luftmengen|8|Wohnung|500|Die vereinbarten Volumenströme werden wohnungsweise eingestellt und in einem Messblatt mit Gerät, Betriebsstufe und Messbedingungen dokumentiert.''',
'''Wohnungswärmezähler|8|Stück|700|Acht der Abrechnung dienende Wärmezähler werden mit Einbauort und Kennzeichen dokumentiert; die Zuordnung zu Wohnungen ist vor Übergabe zu kontrollieren.
Wasserzähler|16|Stück|250|Jede Wohnung erhält die vorgesehenen Kalt- und Warmwasserzähler einschließlich zugänglicher Absperrung; Kennzeichen und Anfangsstände werden wohnungsweise erfasst.
Druck und Spülprüfungen|3|Prüfgruppe|2800|Heizungs-, Kaltwasser- und Warmwasserleitungssystem werden nach geeignetem anlagenspezifischem Verfahren geprüft; Prüfmedium, Zeiten, Drücke und abgegrenzte Bauteile sind zu protokollieren.
Revisionsunterlagen Haustechnik|1|Satz|7000|Die ausgeführten Leitungswege, Armaturen, Geräteeinstellungen und Wartungspunkte werden in einem prüfbaren Unterlagensatz zusammengeführt.
Gemeinsame Inbetriebnahme|1|Terminfolge|5000|Die Fachfirma wirkt bei Einweisung und gemeinsamer Funktionsprüfung mit und übergibt den dokumentierten Anlagenzustand; laufende Wartungsentgelte sind nicht enthalten.'''
],
'elektro': [
'''Zählerschrank und Hauptverteilung|1|Anlage|10500|Zählerschrank und Hauptverteilung werden mit Netzbetreiber und Messkonzept abgestimmt; Anschlussleistung und erforderliche Schutzorgane werden projektspezifisch bemessen.
Wohnungsverteilungen|8|Stück|1300|Acht Verteilungen werden mit den vorgesehenen Schutzorganen, Reserveplätzen und dauerhaften Stromkreisbezeichnungen eingebaut.
Wohnungsstromkreise|72|Stück|350|Je Wohnung werden neun Stromkreise nach Stromkreisverzeichnis installiert; Leitungslängen, Verlegeart und Abschaltbedingungen sind durch die Elektrofachplanung zu bestimmen.
Steckdosen und Auslässe|220|Stück|65|Die planmäßig bezeichneten Anschlusspunkte werden mit abgestimmten Bedienhöhen und Abständen eingebaut; besondere Bereiche erhalten die projektbezogenen Schutzmaßnahmen.
Erdung und Potentialausgleich|1|Anlage|4600|Erdung und Potentialausgleich werden mit den Rohbau-Einbauteilen koordiniert, vor dem Verdecken dokumentiert und messtechnisch überprüft.''',
'''Türkommunikation|8|Teilnehmer|600|Die Türkommunikation wird für acht Wohnungen mit eindeutig zugeordneten Teilnehmern eingerichtet; Außenstation und Bedienbarkeit sind mit dem Eingangselement abzustimmen.
Glasfaserleerrohre|8|Wohnung|450|Leerrohre werden vom festgelegten Übergabepunkt zu jeder Wohnung mit dokumentierten Zugwegen verlegt; ein Telekommunikationsvertrag ist nicht enthalten.
Allgemeinbeleuchtung|40|Stück|150|Treppenraum, Technik- und Außenbereiche erhalten die festgelegten Leuchten und Schaltungen; Bewegungsmelder werden auf die tatsächlichen Laufwege eingestellt.
Technische Anlagenzuleitungen|3|Stück|1600|Die beiden Wärmepumpen und der Aufzug erhalten die geplanten Zuleitungen bis zu den bezeichneten Anschlussklemmen; interne Herstellerschaltungen bleiben den Anlagenlieferanten zugeordnet.
Kommunikationsdokumentation|1|Satz|800|Die Bauherrin erhält Teilnehmerlisten, Leitungswege und eine verständliche Bedienungsanleitung der allgemeinen Anlagen.''',
'''Vorverkabelung Stellplätze|8|Stück|1100|Alle acht Stellplätze werden vollständig für die spätere Erweiterung vorverkabelt; Leitungswege und Ausbaureserve werden im Bestandsplan bezeichnet.
Ladepunkte|2|Stück|3000|Zwei Ladepunkte mit jeweils bis zu 11 kW werden montiert; einer liegt am barrierefreien Stellplatz 01 mit nutzbar angeordnetem Bedienbereich.
Lastmanagement|1|Anlage|2800|Das Lastmanagement verteilt die verfügbare Anschlussleistung zwischen Ladepunkten und weiterer Hauslast; die Einstellgrenzen werden dokumentiert.
Netzabstimmung und Prüfung|1|Leistung|2400|Netzabstimmung, Prüfung und Funktionstest beider Ladepunkte werden mit Einzel- und Gleichzeitbetrieb dokumentiert; spätere Betreiberentgelte sind ausgeschlossen.''',
'''PV Module|80|Stück|180|Achtzig Module mit je 450 Wp ergeben 36 kWp installierte Nennleistung und 160 m² Modulfläche; die Ausrichtung folgt dem abgestimmten Belegungsplan.
PV Unterkonstruktion|80|Modulplatz|90|Die Unterkonstruktion wird mit Tragwerk und Dachabdichtung abgestimmt; Ballastierung oder Befestigung darf nicht ohne projektbezogenen Nachweis geändert werden.
Wechselrichter|2|Stück|4500|Die Wechselrichter werden passend zu den vier Strings und dem Netzanschlusskonzept ausgewählt, zugänglich montiert und dauerhaft gekennzeichnet.
PV Gleichstromleitungen|400|m|18|Gleichstromleitungen werden geschützt und nach den erforderlichen Trenn- und Kennzeichnungsgrundsätzen geführt; Dachübergänge werden mit dem Hüllenlos abgestimmt.
Messkonzept und Netzanschluss PV|1|Leistung|4200|Die Anlage wird für Allgemeinstromnutzung und Überschusseinspeisung angemeldet; eine Belieferung einzelner Mietparteien wird nicht eingerichtet.
PV Prüfung und Anlagenbuch|1|Satz|3000|Stringzuordnung, Messwerte und Schutzeinrichtungen werden dokumentiert; die Bauherrin erhält Anlagenbuch und Einweisung ohne Zusage eines bestimmten Jahresertrags.'''
],
'ausbau': [
'''Trockenbauwände|400|m²|90|Die nichttragenden Ausbauwände werden mit dem freigegebenen Aufbau errichtet; Befestigungen, Schallentkopplung und Verstärkungen für Einbauten sind vor Beplankung zu koordinieren.
Innenputz|1600|m²|22|Die vorgesehenen Wandflächen erhalten einen zum Untergrund und zur anschließenden Beschichtung passenden Putz; Feuchte und Saugverhalten werden vor Auftrag geprüft.
Schachtbekleidungen|80|m²|140|Installationsschächte werden erst nach dokumentierter Leitungs- und Abschottungskontrolle geschlossen; Revisionsöffnungen bleiben zugänglich.
Spachtelung von Ausbauflächen|800|m²|18|Die Ausbauflächen werden auf die vereinbarte nachfolgende Beschichtung vorbereitet; streiflichtkritische Bereiche und Musterflächen sind vor Serienausführung abzustimmen.
Dokumentation verdeckter Bauteile|1|Satz|3200|Schachtzuordnung, Verstärkungen und verdeckte Anschlüsse werden vor dem Schließen erfasst; die Dokumentation ordnet jeden Befund einem Raum zu.''',
'''Estrich|700|m²|40|Estrich wird mit den abgestimmten Randanschlüssen und Fugen auf Wohnungs- und Allgemeinflächen eingebaut; Heizkreise und Schalltrennungen dürfen nicht beschädigt werden.
Holzboden in Wohnbereichen|460|m²|85|Die bezeichneten Wohnbereiche erhalten den freigegebenen Holzbelag; für Wohnung 07 ist die vereinbarte Eichenqualität verbindlich und ein Austauschprodukt bedarf vorheriger Zustimmung.
Fliesenflächen Wohnungen|140|m²|85|Bäder und die weiteren in der Raumliste bezeichneten Flächen erhalten die bemusterte Fliese mit geeignetem Aufbau und geplanten Anschlüssen.
Belag Allgemeinflächen|100|m²|70|Treppen- und allgemeine Verkehrsflächen erhalten den vereinbarten robusten Belag einschließlich planmäßiger Randanschlüsse; die nutzbaren Durchgangsbreiten bleiben erhalten.
Belegreifemessungen|8|Wohnung|500|Vor dem Verlegen werden Feuchte und Eignung des Untergrunds an dokumentierten Messstellen geprüft; Freigabeentscheidungen beziehen sich auf Estrichsystem und vorgesehenen Belag.''',
'''Wohnungseingangstüren|8|Stück|2400|Acht Wohnungseingangstüren werden mit den festgelegten Schall- und Schutzanforderungen eingebaut; die geplante lichte Durchgangsbreite von 0,90 m ist nach Einbau nachzuweisen.
Innentüren|40|Stück|620|Innentüren werden gemäß Türliste mit den richtigen Anschlägen und barrierefrei geplanten Durchgängen geliefert; Zargen dürfen Bewegungsflächen nicht unbemerkt verkleinern.
Besondere Treppenraumtüren|3|Stück|2200|Die drei in der Brandschutz- und Türliste bezeichneten Abschlüsse werden mit dem freigegebenen System einschließlich Beschlägen montiert; Eigenmächtige Kürzungen sind ausgeschlossen.
Schließanlage|1|Anlage|3000|Schließzylinder und Schlüssel werden nach dem abgestimmten Schließplan zugeordnet; Übergabe und Reserveschlüssel werden quittiert.
Türeinstellung und Nachkontrolle|7|Kontrollabschnitt|200|Die Türen werden in sieben räumlichen Kontrollabschnitten wiederholt auf Freigängigkeit und Schließen geprüft; festgestellte Funktionsabweichungen werden bauteilbezogen abgearbeitet.''',
'''Wand und Deckenanstriche|2700|m²|12|Die vorgesehenen Flächen werden nach abgestimmter Bemusterung beschichtet; Untergrundmängel sind vor Beginn anzuzeigen und nicht durch Beschichtung zu verdecken.
Elastische Ausbauanschlüsse|320|m|20|Die zum Ausbau gehörenden Bewegungsfugen werden mit geeigneten Materialien hergestellt und im Wartungsplan verortet; Abdichtungsfugen anderer Gewerke bleiben getrennt.
Lackierung Ausbauflächen|40|Stück|120|Die bezeichneten Bauteile erhalten die abgestimmte Lackoberfläche; Beschläge und funktionsrelevante Dichtungen werden dabei geschützt.
Endreinigung|820|m²|10|Alle beauftragten Innenflächen werden materialgerecht gereinigt und kontrollierbar übergeben; die Bezugsgröße ist die Brutto-Grundfläche und nicht die Wohnfläche.
Schutz fertiger Oberflächen|1600|m²|2|Fertige Oberflächen werden während eigener Folgearbeiten geschützt und die Schutzabdeckungen rechtzeitig vor der gemeinsamen Sichtprüfung entfernt.'''
],
'aufzug': [
'''Antrieb und Tragmittel|1|Anlage|12000|Antrieb und Tragmittel werden für die vereinbarte Nennlast von 630 kg und drei Halte gemäß freigegebener Werkplanung ausgeführt.
Kabine|1|Stück|14000|Die nutzbare Kabine misst 1,10 m mal 1,40 m; Einbauten und Bekleidungen dürfen diese nutzbaren Abmessungen nicht unterschreiten.
Schachttüren|3|Stück|2500|Die drei Haltestellen erhalten die abgestimmten automatischen Türen mit 0,90 m lichter Durchgangsbreite und den erforderlichen Verriegelungen.
Führungsschienen und Befestigungen|1|Satz|5500|Schienen und Befestigungen werden auf die freigegebenen Schachtlasten abgestimmt; Abweichungen vom Rohbaumaß sind vor Montage zu klären.
Montage und Einbringung|1|Leistung|6000|Die Anlage wird mit gesichertem Schachtzugang montiert; Montagearbeitsplätze und Materialtransport werden mit der Baustellenkoordination abgestimmt.''',
'''Steuerung|1|Anlage|3500|Die Steuerung bedient die drei Halte und wird mit dem vorgesehenen Betriebs- und Notbetriebskonzept abgestimmt.
Bedientableaus|3|Stück|450|Die Haltestellentableaus werden in den freigegebenen Bedienhöhen montiert; ihre Erreichbarkeit wird bei der Schlusskontrolle geprüft.
Notrufgerät|1|Anlage|1850|Die Zweirichtungsverbindung wird eingerichtet und mit der Empfangsstelle erprobt; laufende Notrufentgelte sind Gegenstand des Betriebsvertrags.
Interne Verdrahtung|1|Satz|1300|Die interne Anlagenverdrahtung wird vollständig gekennzeichnet; die bauseitige Zuleitung endet an dem mit dem Elektrolos abgestimmten Anschluss.''',
'''Prüfung vor Inbetriebnahme|1|Termin|2200|Die erforderliche Prüfung durch die zuständige zugelassene Überwachungsstelle wird organisiert; das Unternehmen legt die notwendigen Unterlagen vor, entscheidet aber nicht selbst über das Prüfergebnis.
Funktions und Befreiungsversuche|1|Terminfolge|1500|Funktion, Notbetrieb und Befreiung werden mit qualifizierten Beteiligten erprobt und protokolliert; die spätere Betreiberorganisation wird einbezogen.
Anlagenunterlagen|1|Satz|1300|Die Bauherrin erhält Anlagenbuch, Schaltunterlagen, Prüfunterlagen und erreichbare Störungskontakte.
Einweisung Betreiber|2|Stunde|500|Die benannten Vertreter der Verwaltung werden in das sichere Betriebs- und Störungsverfahren eingewiesen; Teilnahme und Themen werden festgehalten.
Prüfschnittstellen fertigstellen|1|Leistung|1000|Zugänge, Kennzeichnungen und die vereinbarten Prüfschnittstellen werden vor dem Termin hergestellt; eine erfolgsunabhängige Bescheinigung wird nicht geschuldet.'''
],
'aussen': [
'''Wegeflächen|140|m²|120|Die stufenlosen Wege werden mit tragfähigem Unterbau und geplantem Gefälle hergestellt; Wasser wird vom Gebäude weggeführt.
Pkw Stellplatzflächen|145|m²|90|Die acht Stellplätze einschließlich Stellplatz 01 werden entsprechend Lageplan befestigt; Rangier- und Bewegungsflächen sind vor Einbau mit dem Aufmaß abzugleichen.
Fahrradabstellplätze|20|Platz|350|Sechzehn Bewohner- und vier Besucherplätze werden standsicher auf der vorgesehenen Fläche angeordnet; sie dürfen Rettungs- und Zugangswege nicht verengen.
Abfallstandfläche|20|m²|140|Die Abfallstandfläche wird befestigt und über einen nutzbaren Weg erschlossen; Randanschlüsse und Entwässerung werden mit der Verwaltung abgestimmt.
Borde und Einfassungen|150|m|65|Einfassungen werden höhengerecht gesetzt; die stufenlosen Übergänge erhalten keine nachträglichen Stolperkanten.
Eingangsrinne|12|m|400|Die Rinne vor dem Eingang wird mit dem Abdichtungsanschluss AP02 und der Ableitung koordiniert; Einbauhöhe und Reinigungszugang werden gemeinsam geprüft.
Anschluss barrierefreier Zugangsweg|1|Leistung|5800|Der Weg von Stellplatz 01 bis zum Eingang wird mit durchgängigen Bewegungsflächen, nutzbaren Querneigungen und den freigegebenen Detailhöhen fertiggestellt.''',
'''Regenwasserleitung außen|80|m|100|Regenwasserleitungen werden bis zu den bezeichneten Übergabepunkten mit dokumentierten Höhen und Gefällen verlegt; ungenehmigte Versickerung ist nicht enthalten.
Schmutzwasserleitung außen|50|m|120|Schmutzwasserleitungen werden mit den abgestimmten Übergängen und Reinigungsmöglichkeiten ausgeführt; Leitungsgräben werden nach Kontrolle lagenweise verfüllt.
Regenrückhaltung|1|Anlage|9000|Die freigegebene Rückhaltung wird einschließlich gedrosselter Ableitung eingebaut; Volumen und Drosselwert richten sich nach der Entwässerungsplanung.
Kontrollschächte|2|Stück|2000|Zwei zugängliche Kontrollschächte werden mit den planmäßigen Anschlusssohlen hergestellt; Deckelhöhen werden an die endgültige Oberfläche angepasst.
Entwässerungsprüfung und Bestandsaufmaß|1|Satz|3000|Leitungszustand, Dichtheit nach geeignetem Verfahren und die Bestandslage werden dokumentiert; Prüfmedium, Prüfabschnitt und Ergebnis sind zu benennen.''',
'''Rasenflächen|300|m²|24|Die Rasenflächen erhalten geeigneten Oberboden, Feinplanum und Ansaat einschließlich Fertigstellungspflege bis zur Abnahme.
Pflanzflächen|100|m²|40|Pflanzbeete werden gemäß Pflanzplan mit standortgerechten Arten hergestellt; Pflanzabstände und spätere Pflegezugänge sind einzuhalten.
Kleinkinderspielbereich|30|m²|250|Der 30 m² große Spielbereich wird mit den freigegebenen Geräten, geeigneten Oberflächen und erforderlichen Sicherheitsräumen errichtet; Geräteunterlagen sind vor Einbau abzugleichen.
Trennung zum Fahrbereich|40|m|95|Die Einfriedung trennt den Spielbereich vom Fahrverkehr; Zugänge dürfen weder eine Fangstelle noch einen unkontrollierten direkten Laufweg auf die Fahrfläche schaffen.
Sitzgelegenheiten|2|Stück|1000|Zwei Sitzgelegenheiten werden dauerhaft befestigt und mit nutzbaren seitlichen Bewegungsflächen angeordnet.
Fertigstellung und Nachpflege|1|Leistung|5500|Die vereinbarte Fertigstellungspflege und Nachpflege werden mit Maßnahmen, Intervallen und Zuständigkeit dokumentiert; Abnahme und Pflegezeitraum bleiben unterscheidbar.'''
]}

def detail_rows():
    rows = []
    for li, (actor, title, total, groups) in enumerate(LOTS, 1):
        assert len(groups) == len(DETAILS[actor])
        for gi, ((gtitle, gtotal, scope), raw) in enumerate(zip(groups, DETAILS[actor]), 1):
            group = []
            for pi, line in enumerate(raw.splitlines(), 1):
                label, qty, unit, price, text = line.split('|')
                q, p = Decimal(qty), Decimal(price)
                group.append(dict(los=li, actor=actor, los_title=title, group=gi, group_title=gtitle,
                                  id=f'{li}.{gi}.{pi}', title=label, qty=str(q), unit=unit,
                                  unit_price=str(p), net=str(q*p), text=text,
                                  parent_id=f'{li+1}.{gi}', group_total=str(gtotal)))
            assert sum(Decimal(r['net']) for r in group) == Decimal(gtotal), (actor,gtitle)
            rows.extend(group)
        assert sum(Decimal(r['net']) for r in rows if r['actor']==actor)==Decimal(total)
    return rows

def document(title, subtitle=''):
    doc = Document(); section = doc.sections[0]
    section.page_width=Cm(21); section.page_height=Cm(29.7)
    section.top_margin=Cm(1.5); section.bottom_margin=Cm(1.55)
    section.left_margin=Cm(1.9); section.right_margin=Cm(1.9)
    section.header_distance=Cm(.65); section.footer_distance=Cm(.7)
    for style in doc.styles:
        if style.type==1:
            style.font.name='Times New Roman'; style.font.size=Pt(11); style.font.color.rgb=RGBColor(0,0,0)
            style.paragraph_format.space_after=Pt(6); style.paragraph_format.line_spacing=1.02
            fonts=style.element.get_or_add_rPr().get_or_add_rFonts()
            for k in list(fonts.attrib):
                if k.endswith('Theme'): del fonts.attrib[k]
            for k in ('ascii','hAnsi','eastAsia','cs'): fonts.set(qn('w:'+k),'Times New Roman')
            for border in style.element.xpath('./w:pPr/w:pBdr'):border.getparent().remove(border)
    for name, size in [('Title',16),('Heading 1',12),('Heading 2',11)]:
        style=doc.styles[name]; style.font.bold=True; style.font.size=Pt(size)
        style.paragraph_format.space_before=Pt(9);style.paragraph_format.space_after=Pt(7)
        style.paragraph_format.keep_with_next=True
    doc.core_properties.author=AUTHOR;doc.core_properties.last_modified_by=AUTHOR
    doc.core_properties.title=title;doc.core_properties.language='de-DE'
    doc.core_properties.created=datetime(2026,9,28);doc.core_properties.modified=datetime(2026,9,28)
    h=section.header.paragraphs[0];h.text='Wohnhof Am Steinbogen 18 · Hildesheim · '+REF
    for run in h.runs:run.font.size=Pt(9)
    foot=section.footer.paragraphs[0];foot.text='Konturfeld Architektur · Projektakte · Seite '
    field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');foot._p.append(field)
    for run in foot.runs:run.font.size=Pt(9)
    if title:doc.add_paragraph(title,'Title')
    if subtitle:doc.add_paragraph(subtitle)
    return doc

def paragraph(doc, text, style=None):
    return doc.add_paragraph(written_norms(text),style)

def table(doc, rows, widths):
    tab=doc.add_table(rows=0,cols=len(widths));tab.autofit=False
    for col,w in zip(tab.columns,widths):col.width=Cm(w)
    borders=OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        el=OxmlElement('w:'+edge);el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
    tab._tbl.tblPr.append(borders)
    for i,row in enumerate(rows):
        tr=tab.add_row();pr=tr._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
        if i==0:pr.append(OxmlElement('w:tblHeader'))
        for c,v,w in zip(tr.cells,row,widths):
            c.width=Cm(w);c.text=str(v);cp=c._tc.get_or_add_tcPr()
            margins=OxmlElement('w:tcMar')
            for edge in ('top','left','bottom','right'):
                e=OxmlElement('w:'+edge);e.set(qn('w:w'),'75');e.set(qn('w:type'),'dxa');margins.append(e)
            cp.append(margins)
            if i==0:
                shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'E8EDF0');cp.append(shade)
            for p in c.paragraphs:
                p.paragraph_format.space_after=Pt(2);p.paragraph_format.space_before=Pt(2)
                for r in p.runs:r.font.size=Pt(10);r.bold=i==0
    doc.add_paragraph()

def save(doc, relative):
    return save_docx(doc,relative)

def build_lvs(rows):
    for li,(actor,title,total,groups) in enumerate(LOTS,1):
        own=[r for r in rows if r['actor']==actor]
        doc=document(f'Detailleistungsverzeichnis Los {li}',title+' · Erläuterungsstand 12.11.2027 · HOAI Leistungsphasen 6 und 7')
        paragraph(doc,'1 Vertragsbezug und Kalkulationszweck','Heading 1')
        paragraph(doc,f'Dieses Blatt konkretisiert die Mengen- und Preisansätze des Angebots vom 29.10.2027 und des Bauvertrags vom 12.11.2027 mit {ACTORS[actor][0]}. Die Pauschale von {euro(total)} EUR netto sowie die Leistungsgrenzen des Ausgangs-LV vom 04.10.2027 bleiben maßgeblich. Die Unterpositionen begründen keinen Einheitspreisvertrag und keinen automatischen Mehrvergütungsanspruch bei einer Mengenabweichung.')
        paragraph(doc,'Die Mengen sind nachvollziehbare Kalkulationsansätze des freigegebenen Planstands vom 24.09.2027. Sie sind weder ein bereits gemessenes Bestandsaufmaß noch ein Ersatz für die Werk- und Montageplanung. Die Ausführung wird nach Bauteil, Aufmaßblatt und Planrevision dokumentiert. Bei Änderungen werden Anlass, tatsächlich betroffene Leistung und Vertragsgrundlage gesondert geprüft; eine technische Freigabe ist kein Zusatzauftrag.')
        paragraph(doc,'2 Summen und ursprüngliche Positionen','Heading 1')
        table(doc,[['Ausgangs-LV','Leistungsgruppe','Netto EUR']]+[[f'{li+1}.{j}',g[0],euro(g[1])] for j,g in enumerate(groups,1)]+[['','Los gesamt',euro(total)]],[3.0,10.3,3.8])
        paragraph(doc,'3 Anforderungen an Angebot und Ausführung','Heading 1')
        paragraph(doc,'Angeboten ist die vollständige beschriebene Leistung einschließlich eigener Nebenarbeiten, Schutz und geordneter Dokumentation. Produktvorschläge und Abweichungen sind vor Beschaffung schriftlich mit ihrem Einfluss auf Funktion, Nachweise und Schnittstellen vorzulegen. Gesetzlich erforderliche Nachweise und die anerkannten Regeln der Technik werden projektbezogen geprüft. Produkt- und Verwendungsnachweise müssen das konkret vorgesehene System und den maßgeblichen Ausgabestand erkennen lassen.')
        paragraph(doc,'Die im Projekt geschlossenen Verträge folgen dem BGB. Aus einer fachüblichen LV-Bezeichnung folgt keine Einbeziehung der VOB/B. Die hier verwendeten Einzelansätze unterstützen Kalkulation und Rechnungsprüfung; sie bewerten weder einen unbestellten Nachtrag noch ersetzen sie die Prüfung einer konkreten Änderungsvereinbarung.')
        if actor=='elektro':paragraph(doc,'Die PV-Unterpositionen 4.4.1 bis 4.4.6 summieren sich auf 45.000,00 EUR netto. Die übrigen Elektropositionen summieren sich auf 105.000,00 EUR netto. Die steuerliche Trennung des Ausgangsvertrags bleibt erhalten; Ladepunkte sind nicht allein wegen einer gemeinsamen Rechnung Bestandteil der PV-Begünstigung.')
        for pair in range(0,len(own),2):
            doc.add_page_break()
            for r in own[pair:pair+2]:
                paragraph(doc,r['id']+' '+r['title'],'Heading 1')
                paragraph(doc,f"Bezug: Ursprungsposition {r['parent_id']} {r['group_title']}. Kalkulation: {r['qty']} {r['unit']} × {euro(Decimal(r['unit_price']))} EUR = {euro(Decimal(r['net']))} EUR netto.")
                paragraph(doc,r['text'])
                paragraph(doc,'Der Unternehmer prüft den freigegebenen Untergrund und die ihm übergebenen Anschlussbedingungen vor Beginn dieser Position. Er benennt erkennbare Widersprüche mit Ort und Planbezug und stimmt deren Klärung mit der Objektüberwachung ab, bevor eine später nicht mehr zugängliche Ausführung entsteht.')
                paragraph(doc,f"Der Leistungsnachweis bezeichnet Menge, Ort und Ausführungstag sowie die zugehörige Unterposition {r['id']}. Lieferbelege und Prüfblätter werden dem betreffenden Bauteil zugeordnet; eine Unterschrift über Anlieferung oder Mengenaufnahme enthält keine rechtsgeschäftliche Abnahme der gesamten Vertragsleistung.")
        paragraph(doc,'Geprüft für die technische Koordination: Nora Feld. Kalkulation erläutert durch die Bauleitung des Auftragnehmers. Die Bauherrin hält an der vereinbarten Lospauschale fest.')
        save(doc,f'06_Leistungsverzeichnisse/Detail-LV/LV_{li:02d}_{actor}_Detail.docx')
    out=CASE/'06_Leistungsverzeichnisse/Detail-LV/LV_Kalkulationsregister.csv'
    with out.open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    QA.mkdir(parents=True,exist_ok=True);(QA/'lv-kalkulation.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def day(s): return date.fromisoformat(s)

HOLIDAYS = {
    day('2027-12-25'):'Erster Weihnachtstag', day('2027-12-26'):'Zweiter Weihnachtstag',
    day('2028-01-01'):'Neujahr', day('2028-04-14'):'Karfreitag',
    day('2028-04-17'):'Ostermontag', day('2028-05-01'):'Tag der Arbeit',
    day('2028-05-25'):'Christi Himmelfahrt', day('2028-06-05'):'Pfingstmontag',
}
# Der Bestandsauszug nennt den 05.06.2028 als Trockenbautermin. Dieser Tag ist
# Pfingstmontag. Die Erweiterung erklärt ihn als ruhige Bestandskontrolle,
# nicht als nachträglich erfundene Genehmigung für gewerbliche Feiertagsarbeit.
WINTER = {START+timedelta(days=i) for i in range((END-START).days+1)
          if day('2027-12-24') <= START+timedelta(days=i) <= day('2028-01-02')}
WEATHER_STOPS = {day('2028-01-04'), day('2028-01-05')}

def workdays(start,end):
    return [start+timedelta(days=i) for i in range((end-start).days+1)
            if (start+timedelta(days=i)).weekday()<5 and start+timedelta(days=i) not in HOLIDAYS
            and start+timedelta(days=i) not in WINTER and start+timedelta(days=i) not in WEATHER_STOPS]

# Eigenständige Arbeitsgänge mit mengenbezogener Fortschreibung. Die Ortsfolge
# gehört zum Arbeitsgang, nicht zu einem beliebigen austauschbaren Tagestext.
TASK_RAW = '''2027-12-01|2027-12-03|rohbau|145|m|Bauzaun aufstellen|Westgrenze;Nordgrenze;Ostgrenze|1.1.1|Zaunfüße und Torflügel werden gegen Verschieben gesichert.|Der Gehweg bleibt außerhalb des Baustellenzugangs nutzbar.
2027-12-06|2027-12-15|rohbau|600|m³|regulären Boden lösen und verladen|Achsen A bis B;Achsen B bis C;Nordseite|1.2.1|Boden wird nach erkennbarem Material getrennt gelagert.|Der Baggerführer hält Abstand zur gesicherten Baugrubenkante.
2027-12-16|2027-12-23|rohbau|420|m³|regulären Überschussboden abfahren|Bodenlager West;Bodenlager Nord;Baustraße|1.2.2|Die Annahmestelle wird mit Materialbezeichnung im Abfuhrbeleg geführt.|Die Reifenreinigung verhindert Bodeneintrag auf den Gehweg.
2028-01-03|2028-01-11|rohbau|150|m³|Gründungspolster einbauen|Westzone;Mittelzone;Nordzone|1.2.3|Der Polier kontrolliert Schichtdicke und Verdichtungsfolge.|Der südöstliche Anschlussbereich bleibt für den späteren Baugrundabgleich offen.
2028-01-12|2028-01-21|rohbau|270|m²|Sauberkeitsschicht vorbereiten|Achsen A bis B;Achsen B bis C;Technikzone|1.3.1|Aussparungen und Höhen werden vor dem nächsten Arbeitsschritt mit der Tragwerksplanung abgeglichen.|Einbetonierte Leitungsdurchführungen werden nicht aus unmaßstäblichen Kopien abgeleitet.
2028-01-24|2028-02-01|rohbau|12|t|Bodenplattenbewehrung im freien Baufeld verlegen|Westplatte;Mittelplatte;Nordplatte|1.3.3|Abstandhalter und Stöße werden vor der Überdeckung geprüft.|Die südöstliche Zone wird erst nach Klärung des örtlichen Baugrunds geschlossen.
2028-02-14|2028-02-18|rohbau|90|m³|Bodenplatte abschnittsweise betonieren|Westplatte;Mittelplatte;Südostanschluss|1.3.1|Vor jedem Abschnitt wird die Freigabe von Bewehrung und Durchführungen dokumentiert.|Frischbeton wird nach dem abgestimmten Winterkonzept geschützt und nachbehandelt.
2028-02-21|2028-03-03|rohbau|300|m²|tragende Wände im Erdgeschoss errichten|WE 01;WE 02;WE 03|1.3.4|Öffnungen und Wandanschlüsse werden mit Grundriss und TGA-Führung abgeglichen.|Das für WE 01 erforderliche lichte Maß wird nicht mit dem Rohbaumaß gleichgesetzt.
2028-03-06|2028-03-08|rohbau|300|m²|Decke über Erdgeschoss schalen und bewehren|Deckenfeld West;Deckenfeld Mitte;Deckenfeld Ost|1.3.5|Durchbrüche und Auflager werden vor der Betonage gemeinsam kontrolliert.|Temporäre Unterstützungen bleiben gemäß Ausschal- und Belastungskonzept stehen.
2028-03-09|2028-03-09|rohbau|90|m³|Decke über Erdgeschoss betonieren|Decke über Erdgeschoss|1.3.2|Lieferscheine werden der Betonierfolge und dem Einbauort zugeordnet.|Die Nachbehandlung beginnt unmittelbar nach Herstellung der Oberfläche.
2028-03-10|2028-03-17|rohbau|300|m²|Decke nachbehandeln und Folgeflächen sichern|Westfeld;Mittelfeld;Ostfeld|1.3.2|Die Freigabe für Folgelasten erfolgt nach dem konkreten Beton- und Temperaturverlauf.|Zusatzlasten aus Materialstapeln werden nicht ohne Abstimmung zugelassen.
2028-03-20|2028-03-28|rohbau|300|m²|tragende Wände im ersten Obergeschoss errichten|WE 04;WE 05;WE 06|1.3.4|Fensteröffnungen und Schachtachsen werden eingemessen.|Die Aufzugfirma erhält das Schachtmaßblatt und prüft ihre Befestigungspunkte.
2028-03-29|2028-03-31|rohbau|90|m³|Decke über erstem Obergeschoss herstellen|Decke WE 04;Decke WE 05;Decke WE 06|1.3.2|Der Rücksprung des obersten Geschosses bleibt in der Schalung erkennbar.|Die 80 m² große Rücksprungfläche ist als Wartungsdach vorgesehen.
2028-04-03|2028-04-13|rohbau|300|m²|Wände des zweiten Obergeschosses errichten|WE 07;WE 08;Treppenraum oben|1.3.4|Attikahöhen und obere Schachtmaße werden mit dem Schnitt abgeglichen.|Der Zugang zu den tieferliegenden Dachflächen bleibt gesichert.
2028-04-18|2028-04-21|rohbau|66|m³|obere Dachdecke betonieren|Decke WE 07;Decke WE 08;Treppenraumdecke|1.3.2|Die Betonierabschnitte folgen der freigegebenen Tragwerksplanung.|Der Dachdecker übernimmt nur nachgewiesen tragfähige und geeignete Flächen.
2028-04-24|2028-04-28|rohbau|80|Stück|Rohbauöffnungen und Anschlüsse fertigstellen|Erdgeschoss;Erstes Obergeschoss;Zweites Obergeschoss|1.4.4|Noch erforderliche Leitungsöffnungen bleiben mit Kennzeichnung zugänglich.|Leitungsabschottungen der Fachgewerke werden nicht durch beliebige Mörtelfüllungen ersetzt.
2028-04-03|2028-04-07|huelle|80|m²|Wartungsdach vorläufig witterungssicher herstellen|Rücksprung West;Rücksprung Ost|2.1.1|Anschlüsse an den noch laufenden Rohbau werden als temporärer Zustand dokumentiert.|Die endgültige Abdichtung bleibt bis zum Abschluss der Anschlüsse offen zu kontrollieren.
2028-04-24|2028-05-05|huelle|220|m²|oberes Flachdach abdichten|Dach WE 07;Dach WE 08;Attikazone|2.1.1|Gefälle und Ablaufhöhen werden vor dem Schließen des Dachaufbaus kontrolliert.|PV-Auflager werden mit den vorgesehenen Schutzlagen abgestimmt.
2028-04-10|2028-05-12|huelle|48|Stück|Fensterelemente montieren|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|2.3.1|Jedes Element wird mit Fensterliste und Anschlussdetail abgeglichen.|Die Anschlussfuge bleibt bis zur Stichprobe der Objektüberwachung zugänglich.
2028-05-15|2028-06-09|huelle|620|m²|Fassadendämmung und Putz aufbauen|Westfassade;Nordfassade;Ostfassade;Südfassade|2.2.1|Untergrund, Systembefestigung und Öffnungsanschlüsse werden abschnittsweise geprüft.|Der Auftrag erfolgt nur bei den für das konkrete System geeigneten Bedingungen.
2028-06-12|2028-06-16|huelle|24|Stück|Sonnenschutz und Hüllenanschlüsse prüfen|Westfassade;Südfassade;Ostfassade|2.4.1|Antriebe, Fensterbänke und Entwässerungsöffnungen werden sichtbar kontrolliert.|Die PV-Montage greift nicht ungeprüft in die fertige Dachabdichtung ein.
2028-04-10|2028-04-28|hls|220|m|Heizungssteigleitungen montieren|Technikraum;Schacht EG;Schacht erstes Obergeschoss|3.1.5|Halterungen und Dehnmöglichkeiten werden mit dem vorgesehenen Aufbau abgeglichen.|Durchführungen werden bis zur fachgerechten Abschottung gekennzeichnet.
2028-05-02|2028-05-26|hls|680|m|Trinkwasserleitungen verlegen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|3.2.1|Offene Rohrenden werden gegen Verschmutzung geschützt.|Wasserwechsel und spätere Inbetriebnahme werden bereits vor der Endmontage abgestimmt.
2028-05-29|2028-06-16|hls|300|m|Abwasserstränge und Anschlüsse verlegen|Schacht West;Schacht Mitte;Schacht Ost|3.2.2|Gefälle und schallentkoppelte Befestigung werden vor dem Verdecken geprüft.|Die Abstimmung mit den Außenleitungen erfolgt am bezeichneten Übergabepunkt.
2028-06-19|2028-06-30|hls|600|m²|Flächenheizung und Verteiler vorbereiten|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|3.1.4|Rohrlagen und Heizkreiskennzeichen werden vor Estrichbeginn aufgenommen.|Die anschließende Rohrnetzprüfung wird als eigener Prüfstand dokumentiert.
2028-04-10|2028-05-12|elektro|72|Stück|Leitungswege der Wohnungsstromkreise vorbereiten|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|4.1.3|Schlitze und Durchbrüche werden mit Tragwerk und Ausbau abgestimmt.|Tragende Bauteile werden nicht ohne Freigabe nachgestemmt.
2028-05-15|2028-06-16|elektro|220|Stück|Dosen und Leitungsauslässe setzen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|4.1.4|Bedienhöhen und Einbauorte werden vor dem Putzen kontrolliert.|Die besondere Erreichbarkeit in WE 01 bleibt im Ausbauplan sichtbar.
2028-06-19|2028-06-30|elektro|8|Stück|Wohnungsverteilungen bestücken|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|4.1.2|Stromkreisbezeichnungen folgen dem abgestimmten Verzeichnis.|Die spätere vollständige Messung wird durch die bloße Montage nicht vorweggenommen.
2028-06-06|2028-06-16|ausbau|400|m²|Trockenbauunterkonstruktionen errichten|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|5.1.1|Bekleidungen bleiben an den noch zu prüfenden Leitungsstellen offen.|Der Kurzvermerk war irrtümlich auf den 05.06. datiert; die dort bezeichnete tatsächliche Arbeit gehört zum 06.06.
2028-06-19|2028-06-30|ausbau|1600|m²|Innenputz und Ausbauflächen herstellen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|5.1.2|Untergrundfeuchte und Anschlussfugen werden vor dem Auftrag geprüft.|Der Raum wird für die anschließenden Trocknungsschritte freigehalten.
2028-07-03|2028-07-07|ausbau|700|m²|Estrich einbauen|Erdgeschoss;Erstes Obergeschoss;Zweites Obergeschoss|5.2.1|Randdämmstreifen und Heizrohrschutz werden vor Beginn kontrolliert.|Die frischen Flächen werden gegen zu frühe Begehung abgesperrt.
2028-07-10|2028-07-28|ausbau|8|Wohnung|Estrichtrocknung verfolgen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|5.2.5|Lüftungs- und Aufheizschritte werden mit Estrich- und Heizungssystem abgestimmt.|Die Zahl der Beobachtungen allein beweist noch keine Belegreife.
2028-07-31|2028-08-11|ausbau|600|m²|Wohnungsbodenbeläge verlegen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|5.2.2|Die Freigabe des Untergrunds wird raumweise vor Verlegung geprüft.|Die Materialkontrolle des sichtbaren Verlegezustands ersetzt noch keinen Abgleich jeder Chargenbezeichnung.
2028-08-14|2028-08-25|ausbau|51|Stück|Türen und Schließanlage einstellen|Wohnungseingänge;Innentüren;Treppenraumabschlüsse|5.3.1|Anschläge und lichte Durchgänge werden mit Türliste und Bewegungsflächen verglichen.|Selbstschließende Türen werden ohne Festkeilen erprobt.
2028-08-21|2028-08-31|ausbau|2700|m²|Malerarbeiten und Reinigungsabschnitte abschließen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08;Allgemeinflächen|5.4.1|Oberflächen werden bei normaler Nutzungssituation auf auffällige Fehlstellen kontrolliert.|Schutzfolien werden erst nach Abschluss der angrenzenden Arbeiten entfernt.
2028-07-03|2028-07-14|aufzug|3|Haltestelle|Führung und Schachttüren montieren|Erdgeschoss;Erstes Obergeschoss;Zweites Obergeschoss|6.1.3|Schachtzugänge werden während der Montage gegen unbefugtes Betreten gesichert.|Die Anlage bleibt gesperrt und wird nicht als Baustellenlastenaufzug genutzt.
2028-07-17|2028-08-04|aufzug|1|Anlage|Kabine und Antrieb montieren|Schacht;Kabine;Antriebsbereich|6.1.2|Befestigungen und Kabinenmaße werden gegen die Werkplanung geprüft.|Montageprobeläufe finden nur unter Verantwortung der Aufzugfirma statt.
2028-08-07|2028-08-25|aufzug|1|Anlage|Steuerung und Notruf fertigstellen|Steuerung;Haltestellen;Notrufanschluss|6.2.1|Die elektrische Schnittstelle und die Erreichbarkeit der Empfangsstelle werden abgeglichen.|Die förmliche Prüfung vor Inbetriebnahme bleibt für den 07.09.2028 terminiert.
2028-07-17|2028-07-28|aussen|130|m|äußere Entwässerungsleitungen verlegen|Westliche Trasse;Nördliche Trasse;Übergabepunkte|7.2.1|Leitungshöhen und Gefälle werden vor Verfüllung aufgenommen.|Die festgelegte gedrosselte Ableitung wird nicht durch Versickerung ersetzt.
2028-07-31|2028-08-11|aussen|285|m²|Wege und Stellplatzflächen herstellen|Zugangsweg;Stellplätze 01 bis 04;Stellplätze 05 bis 08|7.1.1|Höhen werden mit der schwellenlosen Eingangsausbildung abgeglichen.|Der Weg vom barrierefreien Stellplatz bleibt stufenlos und frei von Materiallagern.
2028-08-14|2028-08-25|aussen|400|m²|Rasen und Pflanzflächen herstellen|Westlicher Garten;Nördlicher Garten;Östlicher Garten|7.3.1|Oberboden und Pflanzflächen werden vor Verdichtung durch andere Gewerke geschützt.|Bewässerung und Fertigstellungspflege werden im Pflegeblatt dokumentiert.
2028-08-28|2028-09-08|aussen|30|m²|Spielbereich und Einfriedung fertigstellen|Spielbereich;Zaun zum Fahrweg;Sitzplätze|7.3.3|Gerätezonen und nutzbare Sicherheitsräume werden mit den Herstellerunterlagen abgeglichen.|Fahrrad- und Besucherabstellplätze werden nicht als Gerätefreifläche angerechnet.
2028-08-14|2028-08-25|hls|8|Wohnung|Sanitär und Lüftung endmontieren|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|3.2.3|Armaturen, Filterzugänge und Kennzeichnungen werden wohnungsweise geprüft.|Die gesonderten Messprotokolle der Inbetriebnahme bleiben erforderlich.
2028-08-14|2028-08-25|elektro|80|Modul|PV Anlage montieren|String 1;String 2;String 3;String 4|4.4.1|Dachschutz, Montagekräfte und Gleichstromwege werden gemeinsam kontrolliert.|Die Anlage bleibt bis zu den erforderlichen Prüfungen und der Netzabstimmung im Montagezustand.
2028-08-28|2028-09-01|elektro|8|Stellplatz|Ladevorbereitung und Ladepunkte fertigstellen|Stellplatz 01 bis 04;Stellplatz 05 bis 08|4.3.1|Alle acht Stellplätze erhalten die vorgesehene Vorbereitung; nur zwei Ladepunkte werden installiert.|Die Funktionsprüfung des Lastmanagements wird im Inbetriebnahmebericht festgehalten.
2028-09-06|2028-09-06|hls|8|Wohnung|Inbetriebnahme und Messblätter abschließen|WE 01 bis 03;WE 04 bis 06;WE 07 bis 08|3.4.5|Hydraulische Einstellungen, Luftmengen und Zählerzuordnung werden mit den Fachprotokollen abgeglichen.|Der gemeinsame Termin ersetzt keine rechtsgeschäftliche Bauabnahme.
2028-09-07|2028-09-07|elektro|9|Verteilung|elektrische Anlagen abschließend prüfen|Wohnungsverteilungen;Allgemeinverteilung;Technische Abgänge|4.1.2|Die Elektrofachkraft ordnet die Messwerte dem tatsächlichen Stromkreis zu.|Eine spätere Änderung des Anlagenstands erfordert eine erneute fachliche Bewertung.
2028-09-11|2028-09-14|ausbau|1|Tür|Treppenraumtür im ersten Obergeschoss nachstellen|Treppenraum erstes Obergeschoss|5.3.5|Der am 10.09. aufgefallene unvollständige Schließvorgang wird reproduziert und bearbeitet.|Für den 14.09. ist die Nachkontrolle mit drei aufeinanderfolgenden Schließversuchen geplant.
2028-09-11|2028-09-14|huelle|1|Anschluss|sichtbaren Fensterbankablauf prüfen und bearbeiten|WE 05 Wohnzimmer Nord|2.3.5|Der sichtbare Anschluss wird geöffnet und der Wasserablauf kontrolliert.|Die Sichtkontrolle schließt einen weiter innen verdeckten Befund nicht aus.
2028-09-18|2028-09-22|ausbau|820|m²|Übergabereinigung und Schutzrückbau durchführen|Wohnungen;Treppenraum;Technikräume|5.4.4|Die bereits abgenommenen Flächen werden ohne neue Beschädigungen für die Verwaltung vorbereitet.|Der bekannte Belagsvorbehalt in WE 07 wird dadurch nicht erledigt.
2028-09-04|2028-09-05|hls|8|Wohnung|Messzugänge und Einregulierung vorbereiten|WE 01 bis 04;WE 05 bis 08|3.4.5|Messstellen, Sollwerte und Gerätezuordnung werden vor dem vorgesehenen Prüftag abgeglichen.|Es werden heute keine Ergebnisse der erst für den 06.09. vorgesehenen Abschlussprüfung bestätigt.
2028-09-04|2028-09-06|elektro|9|Verteilung|Stromkreiszuordnung und Prüfzugänge vorbereiten|Wohnungsverteilungen;Allgemeinverteilung|4.1.2|Zugänglichkeit, Verbrauchertrennung und Stromkreiskennzeichen werden für die Messung vorbereitet.|Der Abschlussprüfbericht ist erst nach der vorgesehenen Prüfung am 07.09. auszustellen.
2028-09-07|2028-09-07|hls|1|Termin|Betriebsbuch und Wasserwechsel übergeben|Technikraum|3.4.5|Die vorhandenen Ergebnisse vom 06.09. werden der Verwaltung erläutert; Einstellungen werden dabei nicht verändert.|Dieser Termin ist keine zusätzliche Messung sämtlicher Wohnungen.
2028-09-08|2028-09-08|hls|1|Termin|HLS Unterlagen übergeben und Verwaltung einweisen|Technikraum und Verwaltungsübergabe|3.4.5|Arne Thiel erläutert die am 06.09. erstellten Messblätter und die Betriebsorganisation.|Der abgeschlossene Prüfstand wird nicht durch eine neue pauschale Tagesmenge erweitert.
2028-09-08|2028-09-08|elektro|1|Termin|Elektro Prüfunterlagen übergeben und Verwaltung einweisen|Allgemeinverteilung und Verwaltungsübergabe|4.1.2|Selin Voß erläutert die Ergebnisse vom 07.09. und die zugeordneten Abschaltorgane.|Am Übergabetag finden keine zusätzlichen Abschlussmessungen an zuvor ungeprüften Verteilungen statt.'''

def tasks():
    result=[]
    for i,line in enumerate(TASK_RAW.splitlines(),1):
        a,b,actor,quantity,unit,label,places,lv,check,restriction=line.split('|')
        lv={
            'Fensterelemente montieren':'2.3.1 und 2.3.2',
            'Wohnungsbodenbeläge verlegen':'5.2.2 und 5.2.3',
            'äußere Entwässerungsleitungen verlegen':'7.2.1 und 7.2.2',
            'Wege und Stellplatzflächen herstellen':'7.1.1 und 7.1.2',
            'Rasen und Pflanzflächen herstellen':'7.3.1 und 7.3.2',
            'Sanitär und Lüftung endmontieren':'3.2.3, 3.2.4 und 3.3.1',
            'Türen und Schließanlage einstellen':'5.3.1, 5.3.2, 5.3.3 und 5.3.4',
        }.get(label,lv)
        dates=workdays(day(a),day(b));assert dates
        if label=='Bodenplatte abschnittsweise betonieren':dates=[day('2028-02-14'),day('2028-02-18')]
        if label=='Decke über erstem Obergeschoss herstellen':dates=[day('2028-03-29')]
        if label=='obere Dachdecke betonieren':dates=[day('2028-04-18')]
        result.append(dict(id=f'T{i:03d}',start=a,end=b,actor=actor,quantity=quantity,unit=unit,label=label,
                           places=places.split(';'),lv=lv,check=check,restriction=restriction,dates=dates))
    return result

DELIVERY_RAW = '''2027-12-01|rohbau|145|m|Bauzaunelemente und Tor|Nordwestlicher Baustellenzugang|1.1.1|Elemente auf Vollständigkeit und sichtbare Schäden geprüft; Tor gesondert gekennzeichnet.
2027-12-01|rohbau|2|Stück|Aufenthalts und Sanitärcontainer|Freigegebene Containerfläche|1.1.2|Aufstellpunkte mit Lageplan abgeglichen; Anschlüsse bleiben bis Fachprüfung gesperrt.
2028-01-03|rohbau|75|m³|Mineralisches Gründungspolster erste Lieferung|Lager West|1.2.3|Körnung und Herkunft mit Materialfreigabe abgeglichen; Material getrennt von Aushub gelagert.
2028-01-06|rohbau|75|m³|Mineralisches Gründungspolster zweite Lieferung|Lager West|1.2.3|Die zweite Lieferung vervollständigt den Ansatz von 150 m³; Einbau nur auf geeignetem Untergrund.
2028-01-24|rohbau|12|t|Bewehrungsstahl Bodenplatte|Bewehrungslager|1.3.3|Stahllisten und Bündelkennzeichen stimmen im geprüften Umfang überein; Stahl gegen Verschmutzung gelagert.
2028-02-08|rohbau|45|m³|Filtermaterial Nachtrag 01|Achsen C bis D und 3 bis 4|NT01|Die Lieferung gehört ausschließlich zum beauftragten Nachtrag von 18.000 EUR netto; Filterabstufung vor Einbau mit Dr. Venn geprüft.
2028-02-09|rohbau|30|m|Dränleitung Nachtrag 01|Südostanschluss|NT01|Längen 12 m, 10 m und 8 m für den abgestimmten Verlauf bereitgestellt; keine dauerhafte Grundwasserabsenkung beauftragt.
2028-02-14|rohbau|45|m³|Transportbeton Bodenplatte erster Takt|West und Mittelzone|1.3.1|Fünf Teillieferungen zu je 9 m³ sind im Sammelbeleg erfasst; Einbaubeginn erst nach Bewehrungskontrolle.
2028-02-18|rohbau|45|m³|Transportbeton Bodenplatte zweiter Takt|Mittelzone und Südostanschluss|1.3.1|Fünf Teillieferungen zu je 9 m³ schließen die 90 m³ Bodenplattenansatzmenge; Nachbehandlung ist im Tagesbericht geführt.
2028-03-09|rohbau|90|m³|Transportbeton Decke Erdgeschoss|Decke über Erdgeschoss|1.3.2|Zehn Teillieferungen zu je 9 m³ wurden der Betonierfolge zugeordnet; die Oberfläche wurde laufend nachbehandelt.
2028-03-29|rohbau|90|m³|Transportbeton Decke erstes Obergeschoss|Decke über erstem Obergeschoss|1.3.2|Die Mengenlieferung gehört zur Decke und nicht zum Wartungsdachaufbau; Nachbehandlung folgt dem Betonierkonzept.
2028-04-18|rohbau|66|m³|Transportbeton obere Dachdecke|Oberste Deckenebene|1.3.2|Die Lieferung schließt die Deckenansatzmenge von 246 m³; frühe Dachlasten sind ohne Tragwerksfreigabe nicht zulässig.
2028-04-03|huelle|80|m²|Temporärer Dachschutz Rücksprung|Wartungsdach|2.1.1|Der vorläufige Schutz ist kein zusätzliches Terrassenpaket; die endgültigen Anschlüsse folgen später.
2028-04-24|huelle|300|m²|Dämm und Abdichtungspaket beide Dachniveaus|Abgegrenzte Dachlagerflächen|2.1.1|Das Paket betrifft insgesamt 300 m² Dachfläche; zulässige Lagerlasten und Schutz der Unterlagen wurden abgestimmt.
2028-04-10|huelle|18|Stück|Fensterelemente Erdgeschoss|Wohnungen 01 bis 03|2.3.1|Elementnummern wurden mit der Fensterliste abgeglichen; Montagefugen bleiben für Stichproben zugänglich.
2028-04-24|huelle|18|Stück|Fensterelemente erstes Obergeschoss|Wohnungen 04 bis 06|2.3.1|Elemente weisen keine sichtbaren Transportschäden auf; Glaskanten bleiben geschützt.
2028-05-08|huelle|12|Stück|Fensterelemente zweites Obergeschoss|Wohnungen 07 bis 08|2.3.1|Mit dieser Lieferung liegen 48 Fensterelemente auf der Baustelle; das Hauseingangselement gehört nicht zu dieser Stückzahl.
2028-05-02|hls|680|m|Trinkwasserrohrsystem|Geschütztes Installationslager|3.2.1|Rohrenden sind verschlossen; Lagerung und spätere Spülfolge wurden dem Vorarbeiter erläutert.
2028-06-19|hls|8|Stück|Heizkreisverteiler|Wohnungen 01 bis 08|3.1.3|Je Wohnung ist ein Verteiler bezeichnet; Montageplätze bleiben für Bedienung und Wartung zugänglich.
2028-06-19|elektro|8|Stück|Wohnungsverteilungen|Wohnungen 01 bis 08|4.1.2|Verteilungskennzeichen wurden vergeben; Schutzorgane und Stromkreise werden im Endprüfbericht separat erfasst.
2028-07-03|ausbau|700|m²|Estrichmaterial und Einbauansatz|Wohnungen und Allgemeinflächen|5.2.1|Die Flächenansatzmenge setzt sich aus 600 m² Wohnungen und 100 m² Allgemeinbereichen zusammen; Liefereinheiten des Materials werden nicht als bereits belegreife Fläche verstanden.
2028-07-03|aufzug|3|Stück|Aufzug Schachttüren|Haltestellen EG bis zweites Obergeschoss|6.1.3|Türkennzeichnungen und lichte Durchgänge wurden mit der freigegebenen Werkplanung verglichen.
2028-07-17|aufzug|1|Stück|Aufzugkabine und Antrieb|Gesicherter Montagebereich|6.1.2|Kabinenansatz 1,10 m mal 1,40 m und Nennlast 630 kg wurden anhand der Lieferung abgeglichen; Nutzung bleibt gesperrt.
2028-07-17|aussen|130|m|Entwässerungsleitungen außen|Trassenlager Nord|7.2.1|80 m Regenwasser- und 50 m Schmutzwasserleitungen sind getrennt bezeichnet; Übergabepunkte folgen dem Entwässerungsplan.
2028-07-31|ausbau|460|m²|Holzbeläge Wohnbereiche|Trockener Innenlagerbereich|5.2.2|Empfangen wurden 460 m² laut Begleitpapier; die Chargenprüfung von WE 07 wird im Wareneingang nicht als erledigt bestätigt.
2028-08-14|hls|2|Stück|Wärmepumpen|Vorgesehene Aufstellfläche|3.1.1|Beide Geräte haben je 18 kW nominale Leistung; Typenbezeichnung und freigegebene Schallplanung wurden abgeglichen.
2028-08-14|elektro|80|Stück|PV Module|Gesicherte Dachanlieferung|4.4.1|80 Module zu je 450 Wp ergeben 36 kWp; Montage erfolgt auf insgesamt 160 m² Modulfläche.
2028-08-28|elektro|2|Stück|Ladepunkte|Stellplätze 01 und 05|4.3.2|Zwei Ladepunkte mit jeweils bis zu 11 kW sind geliefert; die Vorbereitung aller acht Stellplätze ist eine getrennte Leistung.'''

def deliveries():
    result=[]
    for i,line in enumerate(DELIVERY_RAW.splitlines(),1):
        dt,actor,qty,unit,title,place,lv,finding=line.split('|')
        if title.startswith('Fensterelemente'):lv='2.3.1 und 2.3.2'
        if title=='Entwässerungsleitungen außen':lv='7.2.1 und 7.2.2'
        result.append(dict(id=f'LB-{i:03d}',date=dt,actor=actor,quantity=qty,unit=unit,title=title,place=place,lv=lv,finding=finding))
    return result

EVENTS = {
'2027-12-01':'Bauzaun und Container wurden im abgestimmten Bereich aufgestellt. Nora Feld und Timo Wendt kontrollierten die Trennung zum öffentlichen Gehweg. Die Einrichtung ist dem Beginn des Rohbaus am 06.12. vorgeschaltet.',
'2027-12-16':'Wegen Regens wurden Bodenlager abgedeckt und offene Gräben gesichert. Es fand keine Betonage statt. Der Abtransport blieb auf bereits freigegebene und sicher erreichbare Lagerbereiche beschränkt.',
'2028-01-04':'Der gefrorene Untergrund war für weiteren Einbau des Gründungspolsters nicht geeignet. Die Einbaukolonne blieb abgemeldet; es wurden nur die Baustellensicherung und die Terminabstimmung fortgeführt.',
'2028-01-05':'Die Freigabe des gefrorenen Untergrunds lag weiterhin nicht vor. Der Rohbauleiter stellte den Einbau für einen zweiten Tag zurück. Material wurde weder auf gefrorenem Grund eingebaut noch als fertige Gründungsleistung gemeldet.',
'2028-01-12':'Die Vorbereitung der Sauberkeitsschicht wurde mit den geplanten Aussparungen abgeglichen. Dr. Jens Rabe prüfte die offenen Schnittstellen; vor der späteren Betonage bleibt eine gesonderte Bewehrungs- und Einbauteilkontrolle erforderlich.',
'2028-02-02':'Im südöstlichen Gründungsbereich, Achsen C bis D und 3 bis 4, wurde eine örtliche wasserführende Feinsandschicht sichtbar. Dr. Ute Venn und die Bauherrin wurden informiert. Nur der betroffene Bereich blieb offen; zwei Beschäftigte und der Bagger wurden soweit möglich in die Westzone umgesetzt.',
'2028-02-03':'Die Südostzone blieb für den Baugrundtermin gesperrt. Dr. Ute Venn erläuterte die örtliche Filter- und Dränpackung; Timo Wendt bereitete Mengen und Arbeitsansätze vor. Die Westzone konnte weiter bearbeitet werden, ohne die ungeklärte Stelle zu überdecken.',
'2028-02-04':'Steinwerk legte das Nachtragsangebot 01 über 18.000,00 EUR netto vor. Nora Feld und die Fachplanung prüften die technische Einbindung. Noch heute erfolgte keine rechtsgeschäftliche Beauftragung durch die Objektüberwachung.',
'2028-02-05':'Die Baustelle ruhte. Maren Birk beauftragte im Büro den örtlich begrenzten Nachtrag 01 zum vereinbarten Pauschalpreis von 18.000,00 EUR netto. Die Freigabe ist für den vorgesehenen Beginn am 07.02. im Vorgang 054 abgelegt.',
'2028-02-07':'Die Kolonne begann den beauftragten Nachtrag 01. Für den ersten Abschnitt wurden 18 m³ zusätzlicher Aushub getrennt erfasst. Drei Mitarbeiter leisteten jeweils 3,8 Stunden zusätzliche Arbeit; übrige Tätigkeiten sind nicht dem Nachtrag zugeschlagen.',
'2028-02-08':'Im Nachtrag wurden weitere 18 m³ Aushub und 10 m³ Filtereinbau erfasst. Die Materiallieferung LB-006 wurde der Südostzone zugeordnet. Drei Mitarbeiter leisteten jeweils 3,8 zusätzliche Stunden; die freigegebenen übrigen Rohbauflächen blieben zugänglich.',
'2028-02-09':'Im Nachtrag wurden 12 m³ Aushub, 15 m³ Filtereinbau und 12 m Dränleitung aufgenommen. Der Anschluss blieb sichtbar. Drei Mitarbeiter leisteten jeweils 3,8 zusätzliche Stunden; ein Anschluss außerhalb des abgestimmten Systems wurde nicht hergestellt.',
'2028-02-10':'Der Nachtrag umfasste heute 12 m³ Aushub, 20 m³ Filtereinbau und 10 m Dränleitung. Drei Mitarbeiter leisteten jeweils 3,8 zusätzliche Stunden. Die Fachplanung kontrollierte die Einbindung vor der vorgesehenen gemeinsamen Aufnahme.',
'2028-02-11':'Nora Feld, Timo Wendt und Dr. Ute Venn nahmen den Nachtrag vor dem Verdecken gemeinsam auf. Heute wurden die restlichen 8 m Dränleitung sowie 3 × 3,8 zusätzliche Stunden erfasst. Die Summe beträgt 60 m³ Aushub, 45 m³ Filter, 30 m Leitung und 57 Arbeitsstunden.',
'2028-03-23':'Beim Rundgang wurden die Schachtmaße im ersten Obergeschoss kontrolliert. Hubpunkt erhielt das Maßblatt. Kabinenmaß und lichte Türöffnung werden dabei von den erforderlichen Rohbaumaßen unterschieden; die Werkplanung bleibt maßgeblich.',
'2028-04-03':'Dachraum begann am freigegebenen Rücksprung mit dem ersten Dachabschnitt. Es handelt sich um das Wartungsdach über dem ersten Obergeschoss. Die obere Dachdecke entsteht später; ihr Abschluss wird heute nicht vorweggenommen.',
'2028-04-28':'Timo Wendt und Nora Feld hielten die Rohbauübergabe an die Folgegewerke fest. Sichtbare Öffnungen und Anschlüsse wurden zugeordnet. Eine Abnahme des gesamten Rohbauvertrags oder eine Freigabe ungeprüfter verdeckter Bauteile wurde damit nicht erklärt.',
'2028-05-12':'Die letzten Fensteranschlüsse befanden sich in Arbeit. Wegen Regens lag der Schwerpunkt auf geschützten Montagebereichen; Anschlussfugen wurden nicht ohne geeignete Bedingungen geschlossen. Die sichtbare Kontrolle blieb elementbezogen.',
'2028-06-05':'Pfingstmontag: Es gab keine reguläre gewerbliche Bauausführung. Der ursprüngliche Kurzvermerk ordnet zwölf Personen und den Arbeitsstand irrtümlich diesem Datum zu. Jan Merz und Elif Sand berichtigen den Erfassungsfehler am 06.06. ausdrücklich: Die bezeichnete Ausführung und der Personaleinsatz fanden am 06.06.2028 statt. Das Berichtigungsblatt bleibt neben dem unveränderten Kurzauszug erhalten.',
'2028-06-06':'Jan Merz und Elif Sand berichtigen den falsch datierten Kurzbericht: Die dort für den 05.06. genannten zwölf Personen und die Arbeit an Trockenbau und Leitungsführung gehören zum heutigen 06.06.2028. Der heutige produktive Personalstand wird mit zwölf geführt; am gestrigen Feiertag fand keine reguläre Bauausführung statt.',
'2028-06-16':'Dachraum meldete die Gebäudehülle geschlossen. Die PV-Unterkonstruktion wurde mit Lichtkreis abgestimmt. Die Kontrolle erfasste die zugänglichen Anschlüsse; aus dieser Meldung wird keine Erklärung über die mangelfreie Beschaffenheit sämtlicher verdeckter Einzelheiten abgeleitet.',
'2028-06-30':'Die TGA-Rohinstallation wurde als fertig gemeldet. Die Rohrnetzprüfung vor dem Estrich wurde für den nächsten zulässigen Arbeitstermin vorbereitet; die für den 06.09. geplante Schlussprüfung soll den dann erreichten Anlagenstand gesondert dokumentieren.',
'2028-07-17':'Grünkante begann mit den Außenanlagen und steckte Stellplatz 01 ab. Der Weg vom barrierefreien Stellplatz zum Eingang wurde freigehalten. Schwerer Baustellenverkehr wurde auf die verbliebene Lieferzone beschränkt.',
'2028-08-10':'Die Bodenbeläge waren im Einbau. Die Chargenbezeichnungen und die vollständige Übereinstimmung mit der Bemusterung wurden heute noch nicht abschließend abgeglichen. Der Tagesvermerk bestätigt lediglich den sichtbaren Arbeitsstand und erklärt keine bemusterungsbezogene Materialfreigabe.',
'2028-08-25':'Hubpunkt meldete die Montage des Aufzugs beendet. Die Prüfung vor Inbetriebnahme bleibt auf den 07.09. terminiert; der Aufzug wurde noch nicht für den allgemeinen Betrieb freigegeben. Die Verwaltung erhielt den Ansprechpartner für die spätere Einweisung.',
'2028-09-06':'Arne Thiel dokumentierte die abschließenden Druck- und Spülprüfungen sowie den hydraulischen Abgleich; die Messwerte stehen in den Originalen 163 und 164. Die Verwaltung übernahm den organisierten Wasserwechsel bis zum Einzug.',
'2028-09-07':'Lichtkreis schloss die Stromkreisprüfung und die PV- sowie Ladepunktprüfung ab. Die Aufzugprüfung fand durch die bezeichnete Überwachungsstelle statt. Die Ergebnisse sind in den Originalen 165 bis 167 festgehalten und werden nicht durch dieses Tagebuch ersetzt.',
'2028-09-08':'Die gemeinsame Inbetriebnahme mit Planwerk und den Fachfirmen fand statt. Anlagenprotokolle und Bedienunterlagen wurden geordnet. Die Einweisung der Verwaltung ersetzte weder die spätere förmliche Bauabnahme noch die Wohnungsübergaben.',
'2028-09-10':'Die vier Beteiligten der vereinbarten ruhigen Sonntagsvorbegehung fanden drei Punkte: eine nicht vollständig schließende Tür im ersten Obergeschoss, einen auffälligen Fensterbankablauf in WE 05 und einen abweichenden Holzbelag in WE 07. Gewerbliche Bauarbeiten fanden nicht statt.',
'2028-09-11':'Die Bauherrin zeigte die drei Befunde aus der Vorbegehung schriftlich an. Für den Belag wurde noch keine Vertragsänderung oder Minderung vereinbart. Hans Müller koordinierte die getrennte technische Nachprüfung; rechtsgeschäftliche Erklärungen blieben bei Maren Birk.',
'2028-09-14':'Die nachgestellte Tür schloss in drei Funktionsprüfungen vollständig. Am geöffneten sichtbaren Fensterbankanschluss in WE 05 war der Wasserlauf frei. Der Belag in WE 07 blieb abweichend und für die Abnahme ausdrücklich offen.',
'2028-09-15':'Maren Birk erklärte für die sieben bezeichneten Bauverträge die förmlichen Abnahmen. Beim Ausbau blieb der bekannte Belagsmangel in WE 07 vorbehalten. Die Originalniederschrift 059 enthält die einzelnen Erklärungen; Architektenleistungen wurden heute nicht abgenommen.',
'2028-09-22':'Die Gebäude- und Betreiberunterlagen wurden an Bauherrin und Mietverwaltung übergeben. Der Vorgang umfasst die Fertigstellungsmitteilung und die Wartungsorganisation. Der Belagsvorbehalt in WE 07 sowie der kaufmännische Elektro-Zahlungsabgleich blieben gesonderte offene Vorgänge.',
'2028-09-29':'Die acht Wohnungen wurden mit Schlüssel- und Zählerzuordnung an die Mietparteien übergeben. Die Anfangsstände stehen im Register 169; Mietbeginn bleibt der 01.10.2028. Der abweichende Belag in WE 07 bleibt als offener Vorgang bestehen; eine vertragliche Erledigung oder Rechnungskorrektur ist bisher nicht vereinbart.',
}

def legacy_anchors():
    raw=(SOURCE/'050_Bautagebuch.csv').read_text(encoding='utf-8-sig').replace('\\r\\n','\n')
    return {row['Datum']:row for row in csv.DictReader(io.StringIO(raw))}

def weather(d, anchors):
    if d.isoformat() in anchors:return anchors[d.isoformat()]['Witterung']
    if d in WEATHER_STOPS:return 'Frost, morgens −4 °C, mittags −1 °C; gefrorener Untergrund'
    base={12:4,1:3,2:6,3:10,4:13,5:17,6:20,7:23,8:22,9:18}[d.month]
    temp=base+((d.day*3+d.month)%7)-3
    condition=['trocken','bedeckt','trocken','leichter Regen','wechselnd bewölkt','trocken','bedeckt'][d.toordinal()%7]
    return f'{condition}, {temp} °C bei der Tageskontrolle'

def task_progress(t,d):
    ix=t['dates'].index(d);n=len(t['dates']);q=Decimal(t['quantity'])
    discrete=t['unit'] in ('Stück','Wohnung','Modul','Haltestelle','Stellplatz','Verteilung','Tür')
    if discrete:
        before=Decimal(int(q*ix/n));after=Decimal(int(q*(ix+1)/n))
    else:
        before=(q*ix/n).quantize(Decimal('.01'));after=(q*(ix+1)/n).quantize(Decimal('.01'))
    if t['label']=='Fensterelemente montieren':
        segments=[('2028-04-10','2028-04-21',0,18,'WE 01 bis 03'),('2028-04-24','2028-05-05',18,18,'WE 04 bis 06'),('2028-05-08','2028-05-12',36,12,'WE 07 bis 08')]
        seg=next(s for s in segments if day(s[0])<=d<=day(s[1]))
        seq=workdays(day(seg[0]),day(seg[1]));ix=seq.index(d);n=len(seq)
        before=Decimal(seg[2]+int(Decimal(seg[3])*ix/n));after=Decimal(seg[2]+int(Decimal(seg[3])*(ix+1)/n))
    location=t['places'][min(len(t['places'])-1,ix*len(t['places'])//n)]
    if t['label']=='Fensterelemente montieren':location=seg[4]
    return dict(task=t['id'],actor=t['actor'],lv=t['lv'],location=location,done=str(after-before),cumulative=str(after),unit=t['unit'],measurement_kind='estimated_mounting_share_not_accepted_quantity' if t['unit']=='Anlage' else 'daily_work_quantity',label=t['label'],check=t['check'],restriction=t['restriction'])

def crew_counts(dt, actors, anchors, nt_work):
    counts={a:{'rohbau':6,'huelle':4,'hls':3,'elektro':3,'ausbau':5,'aufzug':2,'aussen':3}[a] for a in actors}
    if len(actors)==1 and dt in anchors:counts[actors[0]]=int(anchors[dt]['Personal'])
    fixes={
      '2028-04-28':{'rohbau':8}, '2028-05-12':{'huelle':5},
      '2028-06-06':{'huelle':3,'hls':3,'elektro':3,'ausbau':3},
      '2028-06-16':{'huelle':6}, '2028-06-30':{'hls':7},
      '2028-07-17':{'aussen':7,'ausbau':1}, '2028-08-10':{'ausbau':7},
      '2028-08-25':{'aufzug':5}, '2028-09-14':{'ausbau':2,'huelle':2},
    }
    counts.update(fixes.get(dt,{}))
    if nt_work:counts={'rohbau':3}
    return counts

PERSONNEL_SCOPE={
 '2028-04-28':'Acht Personen des Rohbauabschnitts; gleichzeitig vier Hülle, drei HLS und drei Elektro. Gesamt 18.',
 '2028-06-05':'Datumsfehler: zwölf Personen gehören zum 06.06.; Berichtigung Jan Merz und Elif Sand vom 06.06. Maßgeblicher Feiertagsstand null.',
 '2028-06-16':'Neun Personen der Hüllen- und Elektrogruppe, davon sechs Hülle und drei Elektro; zusätzlich drei HLS und fünf Ausbau. Gesamt 17.',
 '2028-06-30':'Zehn Personen der TGA-Gruppe, davon sieben HLS und drei Elektro; zusätzlich fünf Ausbau. Gesamt 15.',
 '2028-07-17':'Sieben Personen Außenanlagen; zusätzlich zwei Aufzugmonteure und eine Person zur Estrichtrocknungskontrolle. Gesamt zehn.',
 '2028-08-25':'Fünf Personen der Aufzug-Montagegruppe; zusätzlich fünf Ausbau, drei Außenanlagen, drei HLS und drei Elektro. Gesamt 19.',
 '2028-09-08':'Acht Teilnehmer der gemeinsamen Inbetriebnahme: drei HLS, drei Elektro sowie zwei Planungs-/Überwachungsvertreter. Zusätzlich drei Personen Außenanlagen. Neun gewerblich Mitwirkende plus zwei Terminvertreter.',
 '2028-09-10':'Vier Teilnehmer der ruhigen Vorbegehung; keine gewerbliche Kolonne.',
 '2028-09-15':'Neun Teilnehmer der förmlichen Abnahmen; keine produktive Baukolonne.',
}

def calendar_records():
    ts=tasks(); lbs=deliveries();anchors=legacy_anchors();records=[]
    for i in range((END-START).days+1):
        d=START+timedelta(days=i);dt=d.isoformat();active=[task_progress(t,d) for t in ts if d in t['dates']]
        lbs_today=[lb for lb in lbs if lb['date']==dt]
        nt_values={'2028-02-07':(18,0,0),'2028-02-08':(18,10,0),'2028-02-09':(12,15,12),'2028-02-10':(12,20,10),'2028-02-11':(0,0,8)}
        nt_work=({'contract':'NT01','workers':3,'hours_per_worker':'3.8','total_hours':'11.4','excavation_m3':nt_values[dt][0],'filter_m3':nt_values[dt][1],'drain_m':nt_values[dt][2]} if dt in nt_values else None)
        holiday=HOLIDAYS.get(d);closed=d.weekday()>4 or holiday or d in WINTER or d in WEATHER_STOPS
        reason=holiday or ('vereinbarte Winterruhe' if d in WINTER else 'witterungsbedingter Einbaustopp' if d in WEATHER_STOPS else 'Samstagsruhe' if d.weekday()==5 else 'Sonntagsruhe' if d.weekday()==6 else '')
        actors=sorted(set(a['actor'] for a in active)|({'rohbau'} if nt_work or dt=='2028-02-02' else set()))
        crew=crew_counts(dt,actors,anchors,nt_work);headcount=sum(crew.values())
        participants={'2028-09-08':2,'2028-09-10':4,'2028-09-15':9}.get(dt,0)
        if closed:headcount=0
        if dt=='2028-09-10':headcount=0
        if d in WEATHER_STOPS:headcount=0
        if not active and not closed and d>day('2028-09-15'):headcount=2
        event=EVENTS.get(dt,'')
        changes=[f"{m['id']} {m['title']}: {'Befund aufgenommen' if m['opened']==dt else 'Nachkontrolle dokumentiert'}; Einzelprotokoll im Mängelordner." for m in defects() if dt in (m['opened'],m['closed'])]
        if changes:event=(event+' '+' '.join(changes)).strip()
        team='; '.join(ACTORS[a][0]+(f' ({crew[a]} Personen)' if dt in anchors or dt=='2028-06-06' else '')+' unter '+FOREMEN[a] for a in actors) or ('Mietverwaltung und Objektüberwachung' if d>day('2028-09-15') and not closed else 'keine reguläre Baukolonne')
        sections=[];rest_stand=None
        if closed:
            first=f'Für den {WEEKDAYS[d.weekday()]}, {d.strftime("%d.%m.%Y")}, ist {reason} dokumentiert. Es wurden keine regulären gewerblichen Bauleistungen und keine produktiven Kolonnenstunden angesetzt. '+('Die vierköpfige ruhige Vorbegehung ist unten gesondert festgehalten.' if dt=='2028-09-10' else 'Die Bauleitung erhielt den Sicherungsstand aus dem Kontrollgang und der letzten Übergabe.')
        elif dt=='2028-09-15':
            first='Neun Vertreter der Vertragsparteien und Objektüberwachung nahmen an den förmlichen Abnahmen teil. Eine produktive Baukolonne oder achtstündige gewerbliche Tagesleistung wurde nicht erfasst. Die Teilnahmezahl des ursprünglichen Kurzvermerks wird nicht als Kolonnenstundennachweis übernommen.'
        elif nt_work:
            first='Die Nachtragskolonne von Steinwerk war mit drei produktiven Mitarbeitern unter Georg Schmidt eingesetzt. Für NT01 sind je Mitarbeiter 3,8 Stunden, zusammen 11,4 Stunden, dokumentiert. Diese Stunden werden nicht zusätzlich als drei volle Achtstundentage angesetzt. Eingesetzt wurden Kleinbagger, Verdichtungsgerät und Handwerkzeug in der Südostzone.'
        else:
            first=f'Der Arbeitstag lief mit {headcount} im Tagesstand erfassten Personen. Eingesetzt waren {team}. Die Regelarbeitszeit lag bei 07:30 bis 16:00 Uhr einschließlich 30 Minuten Pause; gesonderte Prüf- und Besprechungstermine sind keine zusätzlichen achtstündigen Kolonnenansätze.'
            devices={'rohbau':('Bagger und Verdichtungsgerät' if d<day('2028-02-14') else 'Kran und Betoniergerät' if any('beton' in a['label'] for a in active) else 'Kran und Montagewerkzeug'), 'huelle':'Fassadengerüst und Montagewerkzeug', 'hls':'Rohrpresswerkzeug', 'elektro':'Kabeleinziehgerät und Fachmessmittel', 'ausbau':'Ausbauwerkzeug mit Staubabsaugung', 'aufzug':'gesicherte Montagezuggeräte', 'aussen':'Kleinbagger und Verdichtungsgerät'}
            if participants:first+=f' Zusätzlich waren {participants} Vertreter von Planung und Objektüberwachung zum gemeinsamen Termin anwesend; sie sind nicht in den Kolonnenansätzen enthalten.'
            if actors:first+=' Geräte: '+', '.join(devices[a] for a in actors)+'.'
        sections.append(('1 Witterung und Besetzung',f'{weather(d,anchors)}. '+first))
        if active:
            texts=[]
            for a in active:
                if a['unit']=='Anlage':
                    progress=f"Geschätzter Montagefortschritt heute {euro(Decimal(a['done'])*100)} Prozentpunkte, kumuliert {euro(Decimal(a['cumulative'])*100)} Prozent des Montagegangs; kein abnahmefähiger Mengenbeleg"
                elif Decimal(a['done'])==0:
                    progress=f"Vorbereitung und Kontrolle ohne zusätzlich fertiggestellte Einheit; Stand {a['cumulative']} {a['unit']}"
                else:progress=f"Tagesansatz {a['done'].replace('.',',')} {a['unit']}; kumulierter Arbeitsansatz {a['cumulative'].replace('.',',')} {a['unit']}"
                texts.append(f"{ACTORS[a['actor']][0]}: Im Bereich {a['location']} wurde „{a['label']}“ fortgeführt. {progress} (Vorgang {a['task']}, LV {a['lv']}).")
            # Arbeitsansätze sind nachvollziehbarer täglicher Fortschritt, keine
            # rechtsgeschäftliche Mengenanerkennung oder zusätzliche Rechnung.
            sections.append(('2 Ausführung und Arbeitsstand',' '.join(texts)))
        elif nt_work:
            quantities=[f"{nt_work[k]} {u} {label}" for k,u,label in [('excavation_m3','m³','zusätzlicher Aushub'),('filter_m3','m³','Filtermaterial'),('drain_m','m','Dränleitung')] if nt_work[k]]
            sections.append(('2 Ausführung und Arbeitsstand','Im Bereich C bis D und 3 bis 4 wurden heute '+', '.join(quantities)+' ausgeführt. Die Tagesmengen gehören ausschließlich zum beauftragten Nachtrag 01. Der Anschluss bleibt bis zur gemeinsamen Kontrolle zugänglich; die bestehende Lospauschale und der Nachtrag werden getrennt nachgewiesen.'))
        elif closed:
            nearby=[t for t in ts if day(t['start'])<=d<=day(t['end'])]
            if nearby:
                current=nearby[0];prior=[x for x in current['dates'] if x<d]
                cum=Decimal(task_progress(current,prior[-1])['cumulative']) if prior else Decimal('0')
                rest_stand={'task':current['id'],'last_work_date':prior[-1].isoformat() if prior else None,'cumulative':str(cum),'unit':current['unit'],'measurement_kind':'estimated_mounting_share_not_accepted_quantity' if current['unit']=='Anlage' else 'daily_work_quantity'}
                stand=(f"geschätzt {euro(cum*100)} Prozent des Montagegangs; kein abnahmefähiger Mengenbeleg" if current['unit']=='Anlage' else f"{str(cum).replace('.',',')} {current['unit']}")
                second=f"Der zuletzt erreichte Arbeitsansatz für „{current['label']}“ beträgt {stand}. Er wurde heute nicht erhöht. Die Bereiche {', '.join(current['places'])} bleiben dem laufenden Arbeitsgang zugeordnet; ein ruhender Kalendertag ist kein Nachweis einer zusätzlichen Ausführung."
            else:second='Die zuletzt dokumentierten Bauleistungen bleiben unverändert. Es wurden weder zusätzliche Mengen aufgemessen noch neue Bauteile verdeckt. Die Tagesfolge bleibt auch ohne produktive Arbeit vollständig, damit Ruhezeiten nicht mit fehlenden Aufzeichnungen verwechselt werden.'
            sections.append(('2 Arbeitsruhe und Sicherungsstand',second))
        else:
            second=('Hans Müller und die Mietverwaltung ordneten die wohnungsbezogenen Unterlagen, Schlüssel und Übergabetermine. Die Unterlagen wurden gegen die acht Wohnungsnummern und das Zählerregister geprüft. Der bekannte Belagsvorbehalt der WE 07 blieb in der offenen Liste sichtbar.' if d>day('2028-09-15') else 'Die Objektüberwachung führte die anstehenden Prüf- und Freigabevorgänge mit der Bauleitung zusammen. Die Mengenstände wurden heute nicht aus bloßen Liefer- oder Besprechungsbelegen erhöht. Der nächste ausführbare Abschnitt bleibt an die dokumentierten Vorleistungen gebunden.')
            sections.append(('2 Koordination und Arbeitsstand',second))
        if event:coord=event
        elif active:
            selected=active[i%len(active)];coord=selected['check']+' '+selected['restriction']
            coord+=' Hans Müller hielt die örtliche Zuordnung fest und gab die Rückfrage an die zuständige Fachplanung weiter, soweit sie deren Leistungsbereich betraf.'
        else:
            places=['den verschlossenen Baustellenzugang','die gesicherten Materiallager','die gekennzeichneten Verkehrswege','die zugänglichen Entwässerungsstellen','die gesperrten technischen Anlagen']
            coord=f'Der Kontrollvermerk betrifft {places[i%len(places)]}. Im kontrollierten sichtbaren Bereich wurde keine neue akute Störung gemeldet. Nicht begangene oder verdeckte Bereiche sind damit nicht als mängelfrei bestätigt. Der nächste reguläre Arbeitsbeginn bleibt von geeigneten Bedingungen und der jeweiligen Freigabe abhängig.'
        sections.append(('3 Kontrolle und Entscheidungen',coord))
        if lbs_today:
            proof=' '.join(f"{lb['id']}: {lb['quantity']} {lb['unit']} {lb['title']} für {lb['place']}; Empfang und Umfang stehen im gesonderten Beleg." for lb in lbs_today)
        else:
            proof=('Es ging keine gesondert archivierte Materialanlieferung ein. Vorhandenes Material bleibt dem zuletzt erfassten Bestand zugeordnet; eine fehlende neue Lieferung wird nicht als Fehlmenge gewertet.' if closed else 'Die Materialentnahmen wurden dem vorhandenen Bestand des ausführenden Gewerks zugeordnet. Die Bauleitung behält die beschriebenen Bereiche bis zur Kontrolle für das Folgegewerk zugänglich. Abweichungen bei Menge oder Qualität werden im betreffenden Liefer- beziehungsweise Prüfbeleg festgehalten.')
        if dt in anchors:proof+=' Bezug zum ursprünglichen Kurzvermerk: 050_Bautagebuch.csv, Zeile '+dt+'.'
        if dt in PERSONNEL_SCOPE:proof+=' Der Kurzvermerk enthält einen engeren Personalbezug; die gewerblichen Kolonnen und Terminbeteiligten werden hier getrennt geführt.'
        sections.append(('4 Belege und Fortsetzung',proof))
        signature='Erfasst: Hans Müller, Unterstützung der Objektüberwachung. Tagesmeldungen: '+(', '.join(FOREMEN[a] for a in actors) or 'Bauleitung beziehungsweise Mietverwaltung')+'.'
        records.append(dict(number=i+1,date=dt,weekday=WEEKDAYS[d.weekday()],holiday=holiday or '',reason=reason,workers=headcount,weather=weather(d,anchors),tasks=active,crew=crew,meeting_participants=participants,extra_work=nt_work,rest_stand=rest_stand,deliveries=[x['id'] for x in lbs_today],sections=sections,signature=signature,legacy=anchors.get(dt)))
    assert len(records)==304
    return records

def build_diaries(records):
    months=defaultdict(list)
    for r in records:months[r['date'][:7]].append(r)
    for ym,entries in months.items():
        doc=document('');doc.core_properties.title='Bautagebuch '+ym
        for i,r in enumerate(entries):
            if i:doc.add_page_break()
            paragraph(doc,f"Bautagebuch {r['date'][8:10]} {MONTHS[int(r['date'][5:7])]} {r['date'][:4]}",'Title')
            paragraph(doc,f"Tagesblatt {r['number']:03d} von 304 · {r['weekday']} · Leistungsphase 8"+(' · Übergabephase' if r['date']>'2028-09-15' else ''))
            for heading,text in r['sections']:
                paragraph(doc,heading,'Heading 1');paragraph(doc,text)
            paragraph(doc,r['signature'])
        save(doc,f'08_Bauausfuehrung/01_Bautagebuch/{ym[:4]}/BTB_{ym}.docx')
    out=CASE/'08_Bauausfuehrung/01_Bautagebuch/Bautagebuch_Kalenderregister.csv'
    with out.open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f);writer.writerow(['Tagesblatt','Datum','Wochentag','Feiertag','Ruhegrund','Produktivpersonal','Witterung','Arbeitsgänge','Lieferbelege','Monatsdatei'])
        for r in records:writer.writerow([r['number'],r['date'],r['weekday'],r['holiday'],r['reason'],r['workers'],r['weather'],'; '.join([t['task'] for t in r['tasks']]+(['NT01'] if r['extra_work'] else [])),'; '.join(r['deliveries']),f"{r['date'][:4]}/BTB_{r['date'][:7]}.docx"])
    (QA/'baukalender.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (QA/'lieferungen.json').write_text(json.dumps(deliveries(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Die Lesefassung wird erst mit --render aus den finalen Monats-PDFs
    # zusammengefügt. Die Erzeugung der DOCX ersetzt sie nicht durch einen
    # abweichend umbrechenden Zweitsatz.

DEFECT_RAW='''2028-01-11|2028-01-12|rohbau|Gründung Westkante|Die Abdeckung der Polsterkante war auf etwa 4 m zurückgeschlagen; Oberflächenwasser konnte den Rand erreichen.|Georg Schmidt soll die Abdeckung vor der nächsten Niederschlagsphase befestigen und den betroffenen Rand auf Aufweichung kontrollieren.|Die Abdeckung war wieder durchgängig befestigt. Der zugängliche Rand zeigte keine sichtbare Aufweichung; die Baugrundprüfung für die spätere Gründung bleibt davon getrennt.|Sicherung Gründungskante
2028-02-14|2028-02-14|rohbau|Bodenplatte West vor Betonage|An zwei kontrollierten Bewehrungsstellen waren Abstandhalter verschoben; der geplante Abstand zur Schalung war dort nicht gesichert.|Die Betonage des örtlich betroffenen Feldes bleibt bis zur erneuten Bewehrungskontrolle zurückgestellt. Die Bauleitung ordnet die Stellen im Schalplan zu.|Die beiden Abstandhalter wurden vor Betonierbeginn ersetzt und die Lage gemeinsam kontrolliert. Die Freigabe betrifft nur die bezeichneten sichtbaren Stellen.|Abstandhalter vor Betonage
2028-05-10|2028-05-12|huelle|WE 03 Fenster im Schlafzimmer|Das innere Anschlussband lag an der rechten unteren Ecke auf rund 12 cm noch lose; die Bekleidung war nicht geschlossen.|Heinrich Bauer soll den Untergrund und das Band vor dem Verdecken systemgerecht herstellen und die Ecke zur Nachkontrolle offenlassen.|Die Ecke war im zugänglichen Zustand vollständig angearbeitet. Die Stichprobe ergab keinen sichtbaren offenen Spalt; sie ersetzt keine Gesamtmessung der Gebäudehülle.|Anschlussband Fenster WE 03
2028-06-21|2028-06-23|elektro|WE 02 Wohnungsverteilung|Zwei vorbereitete Stromkreisbezeichnungen waren vertauscht; die Anlage war noch nicht für die Nutzung freigegeben.|Wilhelm Fischer soll den Kennzeichnungsplan mit der Leitungszuordnung abgleichen und die betroffenen Beschriftungen berichtigen.|Die Montagebeschriftung wurde korrigiert. Die noch durchzuführende abschließende elektrische Prüfung bleibt maßgeblich für den Endzustand; die heutige Beschriftungskorrektur nimmt sie nicht vorweg.|Beschriftung Verteilung WE 02
2028-06-28|2028-06-30|ausbau|WE 04 Installationsschacht|Die vorgesehene Revisionsöffnung war durch ein Unterkonstruktionsprofil eingeengt; der Armaturenzugang war noch nicht nutzbar.|Walter Schneider soll die Öffnung mit der TGA-Planung abstimmen und das Profil vor der Beplankung entsprechend versetzen.|Die Öffnung war frei und die Armatur für die vorgesehene Bedienung zugänglich. Der abgeglichene Ausbauzustand wurde vor dem Schließen des Schachts aufgenommen.|Revisionsöffnung WE 04
2028-07-03|2028-07-04|ausbau|WE 01 Flur vor Estrich|Am Anschluss zur aufgehenden Wand fehlte ein kurzer Abschnitt des Randdämmstreifens; Estrich war dort noch nicht eingebaut.|Der bezeichnete Bereich bleibt bis zum geschlossenen Randanschluss ausgespart. Der Polier soll die durchgängige Trennung vor dem Einbringen kontrollieren.|Der Randdämmstreifen war lückenlos ergänzt. Die Stelle wurde vor Estricheinbau begangen und nicht als bereits fertige Estrichfläche abgerechnet.|Randanschluss Estrich WE 01
2028-08-03|2028-08-04|aussen|Zugangsweg vor Hauseingang|Die lose gesetzte Pflasterlehre zeigte an einem Kontrollpunkt eine zum Eingang gerichtete Neigung; die Fläche war noch nicht endgültig verdichtet.|Ernst Hoffmann soll die Lehre anhand des Höhenplans berichtigen und die Ableitung zur vorgesehenen Rinne vor Fertigstellung kontrollieren.|Die Lehre wurde korrigiert. Die Höhenkontrolle ergab im bezeichneten Abschnitt eine vom Gebäude wegführende Ausbildung; die Endprüfung des gesamten Wegs bleibt gesondert.|Höhenkontrolle Eingangsweg
2028-08-17|2028-08-18|aufzug|Aufzug Haltestelle erstes Obergeschoss|Die vorläufige Kennzeichnung einer Haltestellenleitung stimmte nicht mit dem Montageplan überein; die Anlage war gesperrt.|Ludwig Weber soll die interne Zuordnung prüfen und die Kennzeichnung vor den Funktionsversuchen berichtigen.|Die Leitung war dem Montageplan entsprechend gekennzeichnet. Diese Sichtkontrolle ist weder die Prüfung vor Inbetriebnahme noch eine Freigabe für den Nutzerbetrieb.|Kennzeichnung Aufzug
2028-09-11|2028-09-14|ausbau|Treppenraumtür erstes Obergeschoss|In der Vorbegehung vom 10.09. schloss die Tür aus der üblichen Öffnungsstellung nicht vollständig; ein Hindernis im Schwenkbereich war nicht erkennbar.|Innenraum Ausbau soll Beschlag und Schließer prüfen und die Funktion vor dem Abnahmetermin wiederholt vorführen.|Die eingestellte Tür schloss am 14.09. in drei unmittelbar aufeinanderfolgenden Versuchen vollständig. Der sichtbare Befund wurde im Original 058 mitgeteilt.|Türfunktion vor Abnahme
2028-09-11|2028-09-14|huelle|WE 05 Wohnzimmerfenster Nord|Der sichtbare Fensterbankablauf fiel in der Vorbegehung auf. Der örtliche Anschluss war für eine weitere Prüfung zu öffnen; eine abschließende Aussage über verdeckte Ursachen lag nicht vor.|Dachraum soll den sichtbaren Anschluss öffnen, die Wasserführung prüfen und die Maßnahme bauteilbezogen dokumentieren.|Am 14.09. war der sichtbare Ablauf nach der Bearbeitung frei. Im geöffneten sichtbaren Bereich war kein Feuchteschaden erkennbar. Über nicht geöffnete Anschlussbereiche enthält diese Nachkontrolle keine abschließende Aussage.|Fensterbank WE 05 vor Abnahme
2028-09-11|2028-10-15|ausbau|WE 07 Wohnbereich Holzbelag|Die eingebaute Eichenqualität wich von der vereinbarten Bemusterung ab. Eine technische Untauglichkeit wurde aus dem Materialvergleich allein nicht hergeleitet.|Die Bauherrin verlangt die genaue Produktbezeichnung und ein Angebot zur Wiederherstellung oder ausdrücklichen Vereinbarung. Bis dahin bleibt der bekannte Mangel bei der Abnahme vorbehalten.|Am 15.10. vereinbarten die Parteien den Verbleib des Belags und eine Vergütungsherabsetzung um 2.500 EUR netto zuzüglich 475 EUR Umsatzsteuer. Nur diese Materialabweichung ist vertraglich erledigt; der Erstattungsnachweis folgt gesondert.|Abweichender Holzbelag WE 07
2030-11-08|2030-12-16|huelle|WE 05 Wohnzimmerfenster Nord im Betrieb|Nach der Mietermeldung vom 04.11. war ein örtlicher Feuchtestreifen sichtbar. Laub am äußeren Profil erklärte den verzögerten Wasserlauf nicht abschließend.|Dachraum soll den Anschluss gezielt öffnen und die Ursache dokumentieren. Die Verwaltung sichert den bisherigen Reinigungsstand; eine pauschale Verantwortungszuweisung an die Mietpartei unterbleibt.|Nach Öffnung am 18.11. wurde eine verdeckte zu hohe Dichtstoffraupe entfernt. Am 16.12. zeigte die zugängliche Innenfläche keine neue sichtbare Feuchte. Der technische Abschluss ersetzt keine anwaltliche Prüfung von Anerkenntnis und Fristwirkung.|Feuchtevorgang WE 05 im Betrieb'''

def defects():
    result=[]
    for i,line in enumerate(DEFECT_RAW.splitlines(),1):
        opened,closed,actor,location,finding,request,resulttext,title=line.split('|')
        result.append(dict(id=f'M-{i:03d}',opened=opened,closed=closed,actor=actor,location=location,finding=finding,request=request,result=resulttext,title=title))
    return result

INSPECTIONS=[
('2027-12-03','Einrichtung und Zugang','Der Bauzaun mit abschließbarem Zugang ist aufgebaut. Der öffentliche Gehweg liegt außerhalb des Baustellenlagers. Container und Kranstellfläche sind dem Einrichtungsplan zugeordnet.','Die Bauleitung erhält den Auftrag, Flucht- und Zufahrtswege täglich freizuhalten. Ein Kontrollgang ersetzt weder die Gefährdungsbeurteilung der Unternehmen noch die Aufgaben des gesondert bestellten Koordinators.'),
('2028-01-12','Gründungsvorbereitung und Aussparungen','Die westliche und mittlere Vorbereitungsfläche ist zugänglich. Die Aussparungen im Technikbereich wurden mit den Fachplänen abgeglichen; die südöstliche Anschlusszone ist noch nicht geschlossen.','Die Betonage bleibt an die gesonderte Kontrolle von Bewehrung und Einbauteilen gebunden. Aus der heutigen Besichtigung folgt keine umfassende Baugrundfreigabe.'),
('2028-02-11','Filter und Dränpackung vor Verdecken','Der Nachtrag ist im Bereich C bis D und 3 bis 4 sichtbar. Das gemeinsame Aufmaß nennt 60 m³ zusätzlichen Aushub, 45 m³ Filtermaterial, 30 m Leitung und 57 Zusatzstunden.','Die Mengen erklären die vereinbarte Pauschale von 18.000 EUR netto. Eine zusätzliche Wasserhaltung außerhalb des freigegebenen Konzepts ist nicht beauftragt.'),
('2028-03-08','Bewehrung und Durchführungen Decke Erdgeschoss','Die Decke über dem Erdgeschoss ist zur Kontrolle vorbereitet. Öffnungen, Auflager und die TGA-Durchführungen wurden anhand der Schal- und Fachpläne verglichen.','Offene Durchführungen werden vor Betonierbeginn eindeutig gekennzeichnet. Die Objektüberwachung ersetzt mit dieser Kontrolle keine statische Neuberechnung.'),
('2028-03-23','Aufzugschacht und Rohbaumaße','Die zugänglichen Schachtwände des ersten Obergeschosses wurden aufgenommen und mit der Hersteller-Werkplanung abgeglichen. Die Kabine bleibt mit 1,10 m mal 1,40 m nutzbar und die Tür mit 0,90 m licht geplant.','Hubpunkt erhält die Maßaufnahme vor Fertigung der Schachtkomponenten. Änderungen an Befestigungskräften sind an die Tragwerksplanung zurückzugeben.'),
('2028-04-28','Übergabe Rohbau an Folgegewerke','Die sichtbaren Wand- und Deckenabschnitte, die Fensteröffnungen und die freigehaltenen Leitungsdurchführungen wurden mit den beteiligten Bauleitungen begangen.','Die Übergabe ermöglicht die weitere Ausführung. Sie ist keine rechtsgeschäftliche Abnahme des Rohbauvertrags und keine pauschale Bestätigung verdeckter Bauteile.'),
('2028-05-12','Fenstermontage und Anschlussfugen','Die 48 Fenster sind nach den drei Lieferabschnitten zugeordnet. Stichproben erfassen die erreichbaren inneren Anschlussbänder und die äußeren Fensterbankbereiche. Der Befund M-003 ist nachkontrolliert.','Bekleidungen dürfen nur die tatsächlich geprüften Bereiche schließen. Weitere Anschlüsse werden in der laufenden Hüllenkontrolle verfolgt.'),
('2028-06-16','Hülle und Schnittstelle Photovoltaik','Dach- und Fassadenarbeiten sind im zugänglichen Abschlussstand besichtigt. Die PV-Auflager und Leitungsübergänge wurden zwischen Dachraum und Lichtkreis abgestimmt.','Schutzlagen bleiben bei der PV-Montage erhalten. Die Meldung einer geschlossenen Hülle beseitigt keine möglicherweise verdeckten Mängel.'),
('2028-06-30','Technik vor Estrich und Schachtschluss','Die Rohinstallation ist den Wohnungen und Schächten zugeordnet. Die Revisionsöffnung der WE 04 ist zugänglich; Rohrlagen, Verteiler und Durchführungen wurden vor dem Verdecken dokumentiert.','Die anlagenspezifische Rohrnetzprüfung und die Belegreifefreigabe sind jeweils getrennt zu dokumentieren. Eine baubegleitende Sichtprüfung ist keine elektrische oder hygienische Endprüfung.'),
('2028-07-07','Estrich und Trocknungsorganisation','Die eingebauten Estrichbereiche sind gesichert. Randanschlüsse und Bewegungsfugen bleiben nachvollziehbar; die Wohnung 01 ist nach Ergänzung des Randdämmstreifens ausgeführt.','Lüftung und Aufheizfolge werden mit den beteiligten Fachfirmen abgestimmt. Beläge werden nicht allein nach Ablauf einer pauschalen Zahl von Tagen freigegeben.'),
('2028-08-04','Höhen und Entwässerung Außenanlagen','Die korrigierte Pflasterlehre vor dem Hauseingang wurde kontrolliert. Die Wegeausbildung führt Wasser vom Gebäude zur vorgesehenen Entwässerung, ohne den stufenlosen Zugang aufzugeben.','Die endgültigen Höhen sind vor dem letzten Verdichtungsgang aufzunehmen. Der Stellplatz 01 und der Weg zum Eingang bleiben frei von Behinderungen.'),
('2028-08-25','Aufzug und Vorbereitung Anlagenprüfungen','Die Montage des Aufzugs ist beendet; die Anlage ist bis zur erforderlichen Prüfung gesperrt. Die Prüftermine für Elektro, Haustechnik und Aufzug sind mit den Fachfirmen abgestimmt.','Die Verwaltung wird in die Betriebsorganisation eingewiesen. Eine Hersteller-Montagemeldung wird nicht als Prüfbescheinigung der Überwachungsstelle behandelt.'),
('2028-09-10','Vorbegehung vor den Bauabnahmen','Die ruhige Besichtigung mit vier Beteiligten erfasst Türfunktion im ersten Obergeschoss, Fensterbankablauf der WE 05 und die abweichende Belagsqualität der WE 07. Gewerbliche Bauarbeiten wurden am Sonntag nicht ausgeführt.','Die Bauherrin erhält drei getrennte Befunde zur schriftlichen Mitteilung. Keine Teilabnahme oder Vergütungsvereinbarung wird in dieser Vorbegehung erklärt.'),
('2028-09-14','Nachkontrolle vor Abnahme','Türfunktion und sichtbarer Fensterbankablauf sind nachbearbeitet. Die drei Schließversuche waren erfolgreich; der sichtbare Wasserablauf war frei. Die Materialabweichung WE 07 besteht fort.','Der bekannte Belagsmangel wird für die Abnahme ausdrücklich vorbehalten. Die nachträgliche technische Begehung nimmt die Entscheidung der Bauherrin nicht vorweg.'),
('2028-09-22','Gebäudeunterlagen und Betreiberübergabe','Pläne, Anlagenprüfungen, Bedienhinweise und Zählerzuordnung wurden mit der Verwaltung durchgesehen. Der Belagsvorgang WE 07 sowie der Elektro-Zahlungsabgleich bleiben als getrennte offene Vorgänge vermerkt.','Die Verwaltung erhält die Wartungszuständigkeiten und bereitet die acht Wohnungsübergaben vor. Die Übergabe des Unterlagensatzes ist keine zusätzliche Bau- oder Architektenabnahme.'),
('2030-11-08','Feuchteprüfung im laufenden Mietbetrieb','Im Wohnbereich der WE 05 ist nach der Mietermeldung ein örtlicher Feuchtestreifen sichtbar. Die Sichtprüfung und der Laubfund am Außenprofil erlauben noch keine abschließende Ursachenzuweisung.','Die gezielte Öffnung erfolgt durch Dachraum im direkten Auftrag der Bauherrin. Die Wirkung späterer Erklärungen auf Anspruchsfristen wird getrennt rechtlich geprüft.'),
]

def build_protocols():
    for i,(dt,title,finding,nextstep) in enumerate(INSPECTIONS,1):
        doc=document('Begehungsprotokoll '+str(i),title+' · '+day(dt).strftime('%d.%m.%Y'))
        paragraph(doc,'1 Anlass und Umfang','Heading 1')
        paragraph(doc,f'Die Begehung betrifft den bezeichneten Zustand des Achtfamilienhauses Wohnhof Am Steinbogen 18 in Hildesheim. Nora Feld führt die fachliche Abstimmung; Hans Müller dokumentiert Ort, sichtbaren Befund und den nächsten Arbeitsschritt. Die jeweils betroffene Bauleitung ist einbezogen. Grundlage sind die genehmigten Bauvorlagen und die für den Abschnitt freigegebenen Ausführungsunterlagen.')
        paragraph(doc,'2 Feststellungen','Heading 1');paragraph(doc,finding)
        related=[m for m in defects() if m['opened']<=dt<=m['closed']]
        if related:paragraph(doc,'Im zugehörigen Befundregister werden geführt: '+', '.join(m['id']+' '+m['title'] for m in related)+'. Die einzelne Mängelzuordnung und die gesonderten Nachkontrollen bleiben maßgeblich.')
        paragraph(doc,'3 Weitere Ausführung','Heading 1');paragraph(doc,nextstep)
        paragraph(doc,'Die heute besichtigten Flächen waren ohne zerstörende Eingriffe zugänglich. Nicht sichtbare Bauteile und andere Ausführungsstände werden mit diesem Protokoll nicht bestätigt. Wird der Bereich später geändert oder verdeckt, sind Datum, verantwortliches Gewerk und die zugehörigen Freigaben im Tagesbericht festzuhalten.')
        paragraph(doc,'4 Verteilung und Zeichnung','Heading 1')
        paragraph(doc,'Das Protokoll wird der Bauherrin und den betroffenen Bauleitungen zur Kenntnis gegeben. Eine sachliche Berichtigung soll den konkreten Absatz und den abweichenden Befund bezeichnen; Schweigen wird nicht als Abnahme, Nachtragsauftrag oder Verzicht auf Einwendungen vereinbart. Protokollführung: gez. Hans Müller. Fachliche Durchsicht: gez. Nora Feld.')
        save(doc,f'08_Bauausfuehrung/02_Begehungen/BG_{i:02d}_{dt}.docx')
    for m in defects():
        for phase,dt in [('Befund',m['opened']),('Nachkontrolle',m['closed'])]:
            doc=document(f"{phase} {m['id']}",m['title']+' · '+day(dt).strftime('%d.%m.%Y'))
            paragraph(doc,'1 Bauteil und Beteiligte','Heading 1')
            paragraph(doc,f"Der Vorgang betrifft {m['location']} im Projekt {REF}. Zuständiges Gewerk ist {ACTORS[m['actor']][0]}; für die laufende Ausführung ist {FOREMEN[m['actor']]} benannt. Nora Feld führt die technische Abstimmung, Hans Müller hält den sichtbaren Zustand fest. Rechtsgeschäftliche Entscheidungen trifft die Bauherrin.")
            paragraph(doc,'2 Festgestellter Zustand','Heading 1');paragraph(doc,m['finding'] if phase=='Befund' else m['result'])
            paragraph(doc,'3 Maßnahme und Zuordnung','Heading 1')
            paragraph(doc,m['request'] if phase=='Befund' else f"Die Nachkontrolle ist dem ersten Befund vom {day(m['opened']).strftime('%d.%m.%Y')} zugeordnet. Die Dokumentation wird zusammen mit dem ursprünglichen Bericht aufbewahrt; der frühere Befund wird nicht überschrieben.")
            if m['id']=='M-011':paragraph(doc,('Für die bevorstehende Abnahme ist der bekannte Belagsmangel ausdrücklich offenzuhalten. Eine Vergütungsherabsetzung oder ein Verzicht auf Beseitigung ist bisher nicht vereinbart; die Bauherrin entscheidet erst nach Vorlage der erforderlichen Unterlagen.' if phase=='Befund' else 'Die Abnahme vom 15.09.2028 enthält den Vorbehalt zur bekannten Materialabweichung. Der heutige Vergleich beschränkt sich auf diesen Punkt; andere mögliche Verlege- oder Folgeschäden werden nicht pauschal ausgeschlossen. Die Rückzahlung der Rechnungskorrektur ist ein eigener Buchhaltungsvorgang.'))
            elif m['id']=='M-012':paragraph(doc,'Die unternehmerische Erklärung zur unentgeltlichen Bearbeitung und der tatsächliche Öffnungsbefund werden im Originalwortlaut archiviert. Das Fristenregister wird nicht allein durch das Datum dieses Protokolls überschrieben. Die Rechtsfolgen von Verhandlungen oder Anerkenntnissen sind gesondert zu prüfen.')
            else:paragraph(doc,'Die Dokumentation ist auf den bezeichneten Ort und den heute zugänglichen Zustand begrenzt. Eine technische Freigabe zum nächsten Arbeitsschritt enthält keine Abnahme des gesamten Gewerks. Bei einem erneuten Befund wird der Vorgang wieder geöffnet und mit einer neuen Datumszeile ergänzt.')
            paragraph(doc,'4 Abschluss des Vermerks','Heading 1')
            paragraph(doc,('Der Befund bleibt bis zur dokumentierten Nachkontrolle beziehungsweise einer ausdrücklichen vertraglichen Regelung offen. Die gesetzten Arbeitsschritte werden mit dem Bauablauf koordiniert; eine bestrittene Ursache wird nicht als abschließend bewiesen behandelt.' if phase=='Befund' else 'Der bezeichnete Nachkontrollstand wird dem Befundregister zugeordnet. Soweit die Ausführung fachlich weitergeführt werden kann, gilt dies nur für den konkret kontrollierten Abschnitt und den dokumentierten Zustand. Andere bekannte oder verdeckte Mängel werden dadurch nicht erledigt.')+' Protokoll: gez. Hans Müller; technische Durchsicht: gez. Nora Feld.')
            save(doc,f"08_Bauausfuehrung/03_Maengel/{m['id']}_{phase}_{dt}.docx")
    with (CASE/'08_Bauausfuehrung/03_Maengel/Maengelregister.csv').open('w',encoding='utf-8-sig',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(defects()[0]));wr.writeheader();wr.writerows(defects())
    (QA/'maengel.json').write_text(json.dumps(defects(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def build_deliveries():
    for lb in deliveries():
        doc=document('Liefer und Empfangsbeleg '+lb['id'],lb['title']+' · '+day(lb['date']).strftime('%d.%m.%Y'))
        paragraph(doc,'1 Lieferung und Leistungsbezug','Heading 1')
        paragraph(doc,f"{ACTORS[lb['actor']][0]} dokumentiert die Anlieferung für das Projekt {REF}. Empfangen wurden {lb['quantity']} {lb['unit']} {lb['title']} für den Bereich {lb['place']}. Der Vorgang ist der Detailposition {lb['lv']} zugeordnet.")
        table(doc,[['Merkmal','Feststellung'],['Anlieferung',day(lb['date']).strftime('%d.%m.%Y')],['Bauvorhaben','Achtfamilienhaus Hildesheim'],['Menge und Einheit',lb['quantity']+' '+lb['unit']],['Empfang',FOREMEN[lb['actor']]],['Belegbezug',lb['id']+' / Tagesbericht '+lb['date']]],[4.0,13.1])
        paragraph(doc,'2 Empfangskontrolle','Heading 1');paragraph(doc,lb['finding'])
        paragraph(doc,'Der Empfang bestätigt die bezeichnete Menge und den bei Anlieferung sichtbaren Zustand. Verdeckte Produkteigenschaften und die spätere Eignung des eingebauten Systems werden damit nicht abschließend bestätigt. Beanstandete oder noch nicht freigegebene Teile sind getrennt zu halten und vor Einbau mit der Bauleitung zu klären.')
        paragraph(doc,'3 Kaufmännische Abgrenzung','Heading 1')
        paragraph(doc,'Dieser Beleg ist keine zusätzliche Rechnung an die Bauherrin und löst keine weitere Vergütung neben dem bestehenden Bauvertrag aus. Materiallieferungen des beauftragten Unternehmens sind bereits in dessen Leistungsumfang enthalten. Die Mengen dienen dem Abgleich von Lieferung, Einbau und den vereinbarten Abschlagsständen; Doppelbuchungen sind ausgeschlossen.')
        paragraph(doc,f"Empfang dokumentiert: gez. {FOREMEN[lb['actor']]}. In das Projektarchiv übernommen: gez. Hans Müller.")
        save(doc,f"08_Bauausfuehrung/04_Lieferungen_und_Pruefungen/{lb['id']}_{lb['date']}.docx")

TEMPLATES=[
('Tagesbericht','1 Auftrag und Tagesgrenze','Der Bericht erfasst den [Datum TT.MM.JJJJ] im Projekt [Projektbezeichnung] von [Beginn] bis [Ende]. Verantwortlich für die Erfassung ist [Name und Funktion]. Er bezeichnet tatsächliche Beobachtungen und die Herkunft fremder Tagesmeldungen getrennt.','2 Personen Wetter und Geräte','Die am Tag eingesetzten Unternehmen sind [Unternehmen]. Für jedes Unternehmen werden [Zahl der Beschäftigten], [Arbeitszeit] und [eingesetzte Geräte] erfasst. Die Witterung wurde um [Uhrzeit] am [Messort] mit [Beobachtung oder Messwert] dokumentiert; daraus folgende Einschränkungen werden an der konkret betroffenen Arbeit erklärt.','3 Ausführung und Kontrolle','Am Bauteil [Ort und Bauteil] wurde die Leistung [Leistung] auf Grundlage des Plans [Nummer und Revision] ausgeführt. Der Tagesfortschritt beträgt [Menge und Einheit]; der bis heute nachvollziehbare Stand beträgt [Menge und Einheit]. Vor dem Verdecken wurde [Prüfgegenstand] durch [Person] mit dem Ergebnis [Befund] kontrolliert.','4 Entscheidung und Fortsetzung','Die offene Frage [konkrete Frage] muss vor [betroffener Folgearbeit] von [zuständiger Person] bis [Datum] entschieden werden. Die technische Abstimmung enthält keine rechtsgeschäftliche Beauftragung zusätzlicher Leistungen. Zugeordnet sind die Belege [Belegnummern]. Bei Arbeitsruhe werden Anlass, unveränderter Stand und Sicherungsmaßnahmen dokumentiert.'),
('Baubegehung','1 Anlass und Grenzen','Am [Datum] begehen [Beteiligte] den Bereich [Ort und Bauteil]. Der Termin dient [konkreter Anlass]. Zugänglich waren [Bereiche]; nicht begangen oder verdeckt waren [Bereiche]. Eine weitergehende Untersuchung ist nur dokumentiert, soweit sie tatsächlich durchgeführt wurde.','2 Beobachtung und Beleg','Festgestellt wurde [konkreter sichtbarer Zustand mit Maß, Lage und Zeitpunkt]. Die Beobachtung stützt sich auf [Messung, Plan oder sonstiger Beleg]. Die vermutete Ursache [Arbeitshypothese] ist von der gesicherten Feststellung zu unterscheiden.','3 Maßnahmen und Zuständigkeit','[Unternehmen] übernimmt die Maßnahme [ausformulierte Leistung] bis [Datum]. Vor einer kosten- oder terminwirksamen Vertragsänderung ist die Entscheidung der hierzu befugten Person [Name] einzuholen. Das nächste Gewerk darf [betroffener Bereich] erst nach [konkreter Voraussetzung] verdecken.','4 Nachkontrolle und Verteilung','Die Nachkontrolle findet am [Datum] mit [Beteiligten] statt. Das Protokoll wird an [Empfänger] verteilt. Schweigen wird nicht als Abnahme oder Nachtragsauftrag vereinbart; tatsächliche Berichtigungen sollen den konkreten Absatz und den abweichenden Befund bezeichnen.'),
('Maengelanzeige','1 Vertragsbezug und Feststellung','Aus dem Vertrag vom [Datum] schulden Sie [bezeichnete Leistung] am Projekt [Projekt]. Am [Datum] wurde an [Bauteil und Ort] folgender Zustand festgestellt: [vollständige Beschreibung]. Die Abweichung von [vertragliche Beschaffenheit oder geschuldeter Erfolg] ergibt sich aus [Unterlage].','2 Verlangen und Frist','Wir fordern Sie auf, den bezeichneten vertragswidrigen Zustand fachgerecht zu beseitigen und die Fertigstellung bis zum [Datum] mitzuteilen. Die Frist berücksichtigt [Zugang, Umfang und Dringlichkeit]. Bitte stimmen Sie den Zugang mit [Person] ab und benennen Sie vor Beginn Ihre vorgesehene Vorgehensweise.','3 Sicherung des Befunds','Vor Veränderungen ist der Zustand durch [geeignete gemeinsame Dokumentation] festzuhalten. Bei unmittelbar drohendem Schaden sind erforderliche Sicherungsmaßnahmen mit Ursache, Umfang und Kostenbelegen zu dokumentieren. Eine Ursachenvermutung wird nicht als abschließender Nachweis dargestellt.','4 Rechte und Nachprüfung','Die Nachprüfung soll am [Datum oder abgestimmter Termin] stattfinden. Über eine rechtsgeschäftliche Abnahme oder eine Einigung zur Vergütung entscheidet [befugte Person]. Gesetzliche Rechte bleiben im jeweils bestehenden Umfang gewahrt; eine bloße Mängelanzeige wird nicht als automatische Hemmung der Verjährung behandelt.'),
('Nachkontrolle','1 Bezug zum Befund','Diese Nachkontrolle betrifft ausschließlich den Befund [Kennzeichen] vom [Datum] am Bauteil [Ort]. Die bisher dokumentierte Abweichung lautet [vollständige Beschreibung]. Beteiligte sind [Namen und Funktionen].','2 Ausgeführte Maßnahme','[Unternehmen] hat nach eigener Mitteilung am [Datum] folgende Arbeit ausgeführt: [konkrete Maßnahme]. Bei der heutigen Kontrolle waren [Bereiche] zugänglich; [Bereiche] blieben verdeckt. Die Beobachtung der Objektüberwachung wird von der Unternehmermitteilung getrennt bezeichnet.','3 Prüfung und Ergebnis','Geprüft wurde [konkretes Verfahren] unter [Bedingungen]. Das Ergebnis lautet [Befund mit Messwert oder beobachteter Funktion]. Der Vorgang ist [weiter offen oder technisch erledigt] für den bezeichneten Prüfbereich; eine nicht geprüfte Eigenschaft wird nicht miterledigt.','4 Folgeschritt','Erforderlich bleibt [konkrete Handlung] durch [Person] bis [Datum]. Die technische Kontrolle erklärt keine Abnahme des gesamten Gewerks und keine pauschale Vereinbarung über die Fristwirkung einer Nachbesserung. Rechtserhebliche Unternehmererklärungen werden im Original archiviert.'),
('Bedenkenhinweis','1 Betroffene Ausführung','Im Projekt [Projekt] betrifft der Hinweis die vorgesehene Ausführung [Leistung und Ort] nach Plan [Nummer und Revision]. Wir haben am [Datum] folgenden erkennbaren Umstand festgestellt: [Befund].','2 Technische Auswirkung','Die unveränderte Ausführung kann nach unserer fachlichen Einschätzung zu [konkrete Auswirkung] führen, weil [nachvollziehbare technische Begründung]. Diese Einschätzung betrifft [abgegrenzter Umfang]; nicht überprüfte Annahmen sind [Annahmen].','3 Entscheidung und Zwischenzustand','Wir bitten [zuständige Person], die Frage [präzise Entscheidung] bis [Datum] zu klären und die erforderlichen Planunterlagen bereitzustellen. Bis dahin führen wir [unbetroffene Arbeiten] fort und sichern [betroffener Bereich] mit [Maßnahme]. Eine vollständige Baustellenstilllegung wird nur behauptet, wenn sie tatsächlich vorliegt.','4 Vertragsfolgen','Die Auswirkungen auf den Ablauf werden in [Terminbezug] dokumentiert. Dieser Hinweis ist weder ein vereinbarter neuer Endtermin noch eine abschließende Mehrkostenforderung. Bei einer geänderten Leistung werden Umfang, Preis und Entscheidungsbefugnis gesondert geklärt.'),
('Nachtragspruefung','1 Änderungsanlass und Vertrag','Das Angebot [Nummer] vom [Datum] betrifft den Bauvertrag vom [Datum] und die beabsichtigte Änderung [konkreter Inhalt]. Zu prüfen ist zunächst, ob die Leistung bereits vom vereinbarten Erfolg und den Vertragsunterlagen umfasst ist.','2 Menge Preis und Abgrenzung','Die nachgewiesene Menge beträgt [Menge und Einheit]. Der Preisansatz setzt sich aus [Lohn, Material, Gerät und weiteren nachgewiesenen Bestandteilen] zusammen. Bereits enthaltene oder anderweitig abgerechnete Bestandteile [Bezeichnung] werden abgezogen; die nachvollziehbare Mehr- oder Mindervergütung beträgt [Betrag] EUR netto.','3 Termin und Entscheidung','Der Unternehmer benennt als konkret betroffene Folge [Arbeit und Zeitraum] und erläutert [Ursache und mögliche Gegenmaßnahme]. Die technische Bewertung durch [Planer] ersetzt keine rechtsgeschäftliche Annahme. Die Entscheidung liegt bei [bevollmächtigte Person]; gesetzliche Änderungs- und Anordnungsrechte sind getrennt zu prüfen.','4 Dokumentierter Abschluss','Die Entscheidung lautet [vollständig ausformulierte Annahme, Ablehnung oder Klärungsanforderung]. Ihre Reichweite ist auf [Leistungsumfang] begrenzt. Leistungsnachweise und Kostenfortschreibung werden erst entsprechend der feststehenden Vertragsgrundlage fortgeschrieben.'),
('Bauteilfreigabe','1 Bauteil und nächster Arbeitsschritt','Die Kontrolle betrifft [Bauteil und Ort] vor [nächster Arbeitsschritt] auf Grundlage der Unterlagen [Planstände]. Beteiligte sind [Namen und Funktionen].','2 Geprüfter Zustand','Geprüft wurden [sichtbare Merkmale und gegebenenfalls Messwerte] mit dem Ergebnis [konkreter Befund]. Nicht zugänglich waren [Bereiche]. Noch fehlende Nachweise sind [Nachweise oder ausdrückliche Fehlanzeige].','3 Technische Entscheidung','Für den bezeichneten Arbeitsabschnitt kann [konkrete Folgearbeit] unter der Voraussetzung [Bedingung] fortgesetzt werden. [Abweichender Bereich] bleibt bis [erforderliche Klärung] offen. Der Unternehmer bleibt für die vertragsgerechte eigene Ausführung verantwortlich.','4 Reichweite','Diese technische Freigabe ist keine rechtsgeschäftliche Abnahme, keine Erweiterung des Auftrags und kein Verzicht auf bekannte oder verdeckte Mängelrechte. Die tatsächliche Ausführung und ein späteres Verdecken werden mit Datum und Verantwortlichem im Tagesbericht dokumentiert.'),
('Abnahmeprotokoll','1 Gegenstand und Beteiligte','Die Parteien [Besteller] und [Unternehmer] besichtigen am [Datum] die Leistungen aus dem Vertrag vom [Datum] im Projekt [Projekt]. Vertretungsbefugnis und Umfang der Besichtigung sind [Angaben].','2 Feststellungen','Die Leistung ist in folgendem Stand vorhanden: [vollständige Beschreibung]. Bekannte Mängel sind [konkrete Bauteile und Befunde]. Fehlende Restleistungen sind [Leistungen]; über ihre Bedeutung für die Abnahmereife wird unter Berücksichtigung des Vertrags und des gesetzlichen Maßstabs entschieden.','3 Erklärung der Bestellerseite','Die befugte Bestellerseite erklärt [ausdrückliche Abnahme oder begründete Verweigerung]. Bei Abnahme werden die Rechte wegen folgender bekannter Mängel ausdrücklich vorbehalten: [Befunde]. Ein Vertragsstrafenvorbehalt wird nur aufgenommen, wenn eine entsprechende Vereinbarung besteht und der konkrete Sachverhalt dies erfordert.','4 Unterlagen und weitere Schritte','Die Übergabeunterlagen sind [Unterlagen und Fehlstand]. Maßnahmen und Fristen lauten [Zuständigkeiten und Termine]. Die Parteien unterzeichnen mit [Namen und Funktionen]. Eine Zustandsfeststellung bei verweigerter Abnahme ist als eigener Vorgang nach seinen Voraussetzungen zu prüfen und nicht durch Umbenennen dieses Protokolls herzustellen.'),
]

def build_templates():
    for i,t in enumerate(TEMPLATES,1):
        name,*parts=t;visible_name=name.replace('Maengel','Mängel').replace('pruefung','prüfung');doc=document('Vorlage '+visible_name,'Bearbeitbares Arbeitsdokument für ein Bauprojekt')
        paragraph(doc,'Die nachfolgenden Felder werden für den konkreten Vorgang ausgefüllt. Nicht anwendbare Alternativen werden vor Unterzeichnung entfernt; ein ungeklärter Sachverhalt wird als offen bezeichnet und nicht durch eine pauschale Bestätigung ersetzt.')
        for j in range(0,len(parts),2):paragraph(doc,parts[j],'Heading 1');paragraph(doc,parts[j+1])
        paragraph(doc,'Dokument erstellt durch [Name und Funktion] am [Datum]. Unterzeichnung beziehungsweise dokumentierte Weitergabe: [Name und Rolle].')
        save(doc,f'12_Wordvorlagen/Bau/VB_{i:02d}_{name}.docx')
    doc=document('Berichtigung des Bautagebuchauszugs','Berichtigung durch Jan Merz und Elif Sand vom 06.06.2028')
    paragraph(doc,'1 Anlass','Heading 1');paragraph(doc,'Der ursprüngliche Kurzauszug 050_Bautagebuch.csv enthält für den 05.06.2028 den Stand „Trockenbau und Leitungsführung; Abschottungen noch offen“ sowie zwölf Personen. Der 05.06.2028 ist Pfingstmontag und in Niedersachsen ein gesetzlicher Feiertag. Der Eintrag wird deshalb nicht als Nachweis regulärer gewerblicher Bauarbeit oder zwölf geleisteter Personentage übernommen.')
    paragraph(doc,'2 Berichtigung des Erfassungsfehlers','Heading 1');paragraph(doc,'Wir, Jan Merz für Innenraum Ausbau und Elif Sand für Planwerk, berichtigen den Datumsfehler unseres Tagesvermerks ausdrücklich. Die dort bezeichnete tatsächliche Arbeit an Trockenbau und Leitungsführung mit zwölf Personen fand am 06.06.2028 statt. Beim Übertragen wurde irrtümlich das Datum 05.06.2028 eingetragen. Am Pfingstmontag wurden diese Arbeiten nicht ausgeführt; der produktive Personalstand für den 05.06. beträgt null. Für den 06.06. werden zwölf tatsächlich eingesetzte Personen geführt. Es handelt sich um die Berichtigung eines Erfassungsfehlers, nicht um eine nachträgliche Genehmigung für Feiertagsarbeit.')
    paragraph(doc,'3 Aufbewahrung und Reichweite','Heading 1');paragraph(doc,'Der überlieferte Kurzauszug bleibt unverändert erhalten. Dieser Ergänzungsvermerk macht die zeitliche und personelle Zuordnung nachvollziehbar; er wird zusammen mit dem Monatsband Juni aufbewahrt. Andere datierte Anker des Kurzauszugs bleiben bestehen.')
    paragraph(doc,'Berichtigt am 06.06.2028: gez. Jan Merz; gez. Elif Sand. In das Tagesregister übernommen: gez. Hans Müller. Fachlich zur Kenntnis genommen: Nora Feld.')
    save(doc,'08_Bauausfuehrung/01_Bautagebuch/Ergaenzung_Kurzauszug_Pfingstmontag.docx')

def build_personnel_addendum():
    entries=[r for r in calendar_records() if r['legacy']]
    doc=document('Personalabgleich der Baukurzvermerke','Ausdrückliche Ergänzung vom 29.09.2028 durch Nora Feld und Hans Müller')
    paragraph(doc,'Wir ergänzen die Personenangaben der 23 überlieferten Kurzvermerke 050_Bautagebuch.csv um ihre genaue Reichweite und die gewerkeweise Tagesbesetzung. Die ursprüngliche Datei bleibt unverändert. Mehrere Kurzvermerke nannten nur die am bezeichneten Gewerk oder Termin beteiligte Gruppe; diese Zahl durfte nicht ungeprüft als gesamtes Baustellenpersonal fortgeschrieben werden. Der nachfolgende Abgleich bezeichnet die innerhalb dieser Projektakte bestätigte Zuordnung ausdrücklich.')
    for start in range(0,len(entries),6):
        if start:
            doc.add_page_break();paragraph(doc,'Personalabgleich Fortsetzung','Title')
        rows=[['Datum','Kurzvermerk','Gesamtstand und Zuordnung']]
        for r in entries[start:start+6]:
            scope=PERSONNEL_SCOPE.get(r['date'])
            if not scope:
                names=', '.join(f"{ACTORS[a][0]} {n}" for a,n in r['crew'].items())
                scope=f"{r['workers']} gewerblich eingesetzte Personen; {names}. Die ursprüngliche Zahl bleibt für diesen Tagesstand zutreffend."
                if r['extra_work']:scope+=' Darin die drei Mitarbeiter mit je 3,8 Stunden ausschließlich für NT01; keine zusätzlichen vollen Personentage.'
            rows.append([day(r['date']).strftime('%d.%m.%Y'),r['legacy']['Personal']+' Personen',scope])
        table(doc,rows,[2.2,2.5,12.4])
        paragraph(doc,'Die angegebenen Personen sind Präsenzzahlen des bezeichneten Vorgangs. Besprechungsteilnahme ist kein zusätzlicher Achtstundentag und keine Vergütungsanerkennung. Maßgeblich für NT01 bleiben die getrennt dokumentierten 57 Stunden. Andere Leistungen oder frühere Mengen werden mit diesem Personalabgleich nicht zusätzlich abgerechnet.')
    paragraph(doc,'Bestätigt am 29.09.2028: gez. Nora Feld, verantwortliche Objektüberwachung; gez. Hans Müller, Dokumentation der gewerkebezogenen Tagesmeldungen. Die Zuordnungen wurden mit den bezeichneten Bauleitungen abgeglichen.')
    save(doc,'08_Bauausfuehrung/01_Bautagebuch/Ergaenzung_Personalabgleich_2028-09-29.docx')
    (QA/'personalabgleich.json').write_text(json.dumps([{'date':r['date'],'legacy_count':int(r['legacy']['Personal']),'workers':r['workers'],'crew':r['crew'],'meeting_participants':r['meeting_participants'],'explanation':PERSONNEL_SCOPE.get(r['date'],'Gewerbliche Gesamtzahl des Tagesstands unverändert.')} for r in entries],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def validate():
    rows=detail_rows();records=calendar_records();lbs=deliveries()
    assert sum(Decimal(r['net']) for r in rows)==Decimal('2080000')
    assert {r['date'] for r in records}=={(START+timedelta(days=i)).isoformat() for i in range(304)}
    assert all(not r['tasks'] and r['workers']==0 for r in records if r['holiday'])
    assert len({r['id'] for r in lbs})==len(lbs)==28
    assert sum(Decimal(r['quantity']) for r in lbs if r['title'].startswith('Transportbeton Decke') or r['title']=='Transportbeton obere Dachdecke')==246
    assert sum(Decimal(r['quantity']) for r in lbs if r['title'].startswith('Transportbeton Bodenplatte'))==90
    assert sum(Decimal(r['quantity']) for r in lbs if r['title'].startswith('Fensterelemente'))==48
    assert sum(Decimal(r['quantity']) for r in lbs if r['title'].startswith('Mineralisches Gründungspolster'))==150
    assert len(legacy_anchors())==23
    assert len(defects())==12 and len(INSPECTIONS)==16
    year=2028
    a=year%19; b=year//100; c=year%100; d=b//4; ee=b%4; f=(b+8)//25; g=(b-f+1)//3
    h=(19*a+b-d-g+15)%30; ii=c//4; k=c%4; ll=(32+2*ee+2*ii-h-k)%7; mm=(a+11*h+22*ll)//451
    e=date(year,(h+ll-7*mm+114)//31,(h+ll-7*mm+114)%31+1)
    assert {e-timedelta(days=2),e+timedelta(days=1),e+timedelta(days=39),e+timedelta(days=50)}<=set(HOLIDAYS)
    # Materialverbrauch darf in den konkret belegten Abläufen der Anlieferung
    # nicht vorausgehen. Tagesbeton wird nicht als Lagerbestand vorgetragen.
    for r in records:
        window=sum(Decimal(t['done']) for t in r['tasks'] if t['label']=='Fensterelemente montieren')
        if window:
            before=sum(Decimal(t['done']) for rr in records if rr['date']<=r['date'] for t in rr['tasks'] if t['label']=='Fensterelemente montieren')
            supplied=sum(Decimal(x['quantity']) for x in lbs if x['date']<=r['date'] and x['title'].startswith('Fensterelemente'))
            assert before<=supplied,(r['date'],before,supplied)
        concretes=[t for t in r['tasks'] if t['label'] in ('Bodenplatte abschnittsweise betonieren','Decke über Erdgeschoss betonieren','Decke über erstem Obergeschoss herstellen','obere Dachdecke betonieren')]
        if concretes:
            assert sum(Decimal(t['done']) for t in concretes)==sum(Decimal(x['quantity']) for x in lbs if x['date']==r['date'] and x['title'].startswith('Transportbeton'))
    assert next(r for r in records if r['date']=='2028-06-05')['workers']==0
    assert next(r for r in records if r['date']=='2028-06-06')['workers']==12
    extras=[r['extra_work'] for r in records if r['extra_work']]
    assert len(extras)==5 and sum(Decimal(r['total_hours']) for r in extras)==57
    assert [sum(r[k] for r in extras) for k in ('excavation_m3','filter_m3','drain_m')]==[60,45,30]
    assert all(r['workers']>0 for r in records if r['tasks'] or r['extra_work'])
    assert all(r['workers']==sum(r['crew'].values()) for r in records if r['tasks'] or r['extra_work'])
    assert next(r for r in records if r['date']=='2028-08-25')['workers']==19
    assert all(r['date']=='2028-09-07' for r in records for t in r['tasks'] if t['label']=='elektrische Anlagen abschließend prüfen')
    assert all(r['date']=='2028-09-06' for r in records for t in r['tasks'] if t['label']=='Inbetriebnahme und Messblätter abschließen')
    last={}
    for r in records:
        for t in r['tasks']:last[t['task']]=(r['date'],t['cumulative'])
        if r['rest_stand']:
            s=r['rest_stand'];expected=last.get(s['task'],(None,'0'))
            assert (s['last_work_date'],s['cumulative'])==expected,(r['date'],s,expected)
    assert next(r for r in records if r['date']=='2028-05-06')['rest_stand']['cumulative']=='36'
    assert next(r for r in records if r['date']=='2028-05-07')['rest_stand']['cumulative']=='36'
    return {'days':len(records),'lv_positions':len(rows),'lv_net':'2080000.00','deliveries':len(lbs),'defects':12,'inspection_protocols':16,'templates':8,'legacy_anchors':23}

def owned_files():
    paths=[]
    for rel in ['06_Leistungsverzeichnisse/Detail-LV','08_Bauausfuehrung/01_Bautagebuch','08_Bauausfuehrung/02_Begehungen','08_Bauausfuehrung/03_Maengel','08_Bauausfuehrung/04_Lieferungen_und_Pruefungen','12_Wordvorlagen/Bau']:
        paths.extend(p for p in (CASE/rel).rglob('*') if p.is_file() and 'Bestandsnachweise' not in p.parts)
    return sorted(paths)

def manifest():
    data=[]
    for p in owned_files():
        data.append({'source':str(p.relative_to(CASE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'kind':p.suffix.lstrip('.')})
    (QA/'manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return data

def render():
    from pypdf import PdfReader, PdfWriter
    runtime=Path(os.environ.get('CODEX_WORKSPACE_RUNTIME',str(Path.home()/'.cache/codex-runtimes/codex-primary-runtime'))).expanduser()
    renderer_setting=os.environ.get('DOCX_RENDERER')
    candidates=sorted((Path.home()/'.codex/plugins/cache/openai-primary-runtime/documents').glob('*/skills/documents/render_docx.py'))
    renderer=Path(renderer_setting).expanduser() if renderer_setting else (candidates[-1] if candidates else None)
    if renderer is None or not renderer.is_file():
        raise FileNotFoundError('Gebündelter Dokumenten-Renderer fehlt. DOCX_RENDERER auf die Datei render_docx.py des installierten Dokumenten-Skills setzen.')
    if not (runtime/'dependencies/bin/override').is_dir():
        raise FileNotFoundError('Gebündelte Laufzeit fehlt. CODEX_WORKSPACE_RUNTIME auf das Codex-Verzeichnis mit dependencies/bin/override setzen.')
    index=[]
    for p in owned_files():
        if p.suffix!='.docx':continue
        sha=hashlib.sha256(p.read_bytes()).hexdigest();out=ASSETS/'bau-qa'/p.stem
        out.mkdir(parents=True,exist_ok=True);pdf=out/(p.stem+'.pdf');stamp=out/'source.sha256'
        if not (pdf.exists() and stamp.exists() and stamp.read_text()==sha):
            env=os.environ.copy();env['PATH']=str(runtime/'dependencies/bin/override')+':'+str(runtime/'dependencies/bin/fallback')+':'+env.get('PATH','')
            args=[sys.executable,str(renderer),str(p),'--output_dir',str(out),'--emit_pdf']
            with (out/'render.log').open('w') as log:subprocess.run(args,stdout=log,stderr=subprocess.STDOUT,check=True,env=env)
            stamp.write_text(sha)
        pages=len(PdfReader(pdf).pages)
        index.append({'source':str(p.relative_to(CASE)),'sha256':sha,'pdf':str(pdf),'pages':pages,'qa_png_dir':str(out)})
        print(p.name,pages,flush=True)
        (QA/'renderindex.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Die veröffentlichte Lesefassung besteht exakt aus den geprüften Wordseiten.
    # Keine zweite, anders umbrechende Satzfassung derselben Tagesberichte.
    writer=PdfWriter()
    for row in sorted((r for r in index if Path(r['source']).name.startswith('BTB_')),key=lambda r:r['source']):
        writer.append(row['pdf'],outline_item=Path(row['source']).stem.replace('BTB_','Bautagebuch '))
    assert len(writer.pages)==304
    writer.add_metadata({'/Title':'Bautagebuch vom 01.12.2027 bis 29.09.2028','/Author':AUTHOR})
    writer.write(CASE/'gesamt-pdf/bauwirtschaft-hildesheim-lebensakte_bautagebuch.pdf')
    return index

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--render',action='store_true');parser.add_argument('--check',action='store_true');args=parser.parse_args()
    if args.render:render();return
    info=validate()
    if not args.check:
        build_lvs(detail_rows());build_diaries(calendar_records());build_protocols();build_deliveries();build_templates();build_personnel_addendum();info['original_files']=len(manifest())
    print(json.dumps(info,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
