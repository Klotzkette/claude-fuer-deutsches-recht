"""Redaktionelle Quelldaten; erzeugt keine ausgelieferten Artefakte."""
from pathlib import Path
import json, csv, io
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'scripts/data/bav-konzern-faelle'
LAW='Monkī · Treuenfels Rechtsanwälte Partnerschaft mbB'
ADDRESS='Am Rheinbogen 18, 51373 Leverkusen'
CONTACT=f'{LAW}\n{ADDRESS}\nDr. Monkī D. Rufi / Dr. Nora Treuenfels\nmail@monki-treuenfels.example'

def paras(t): return [s.strip() for s in t.strip().split('\n\n') if s.strip()]
def case(slug,title,client,city,story,assignment):
 return dict(slug=slug,title=title,client=client,city=city,story=story,assignment=assignment,law_firm={'name':LAW,'address':ADDRESS,'partners':['Dr. Monkī D. Rufi','Dr. Nora Treuenfels'],'email':'mail@monki-treuenfels.example'},documents=[],workbooks=[],slides=[],controls={})
def doc(c,id,file,title,date,sender,recipient,text,phase='Grundakte',attachments=None,**extra):
 path=f'{phase}/{id}_{file}'
 d=dict(id=id,path=path,kind=Path(file).suffix[1:],title=title,date=date,sender=sender,recipient=recipient,subject=title,body=paras(text),attachments=attachments or [])
 d.update(extra); c['documents'].append(d);return path

def workbook(c,id,file,title,sheets,phase='Grundakte'):
 path=f'{phase}/{id}_{file}'; c['workbooks'].append(dict(id=id,path=path,title=title,sheets=sheets));return path

def csvdoc(c,id,file,title,columns,rows,phase='Grundakte'):
 s=io.StringIO(); w=csv.writer(s,delimiter=';');w.writerow(columns);w.writerows(rows)
 return doc(c,id,file,title,'2026-10-20',c['client'],'Projektteam',s.getvalue(),phase,csv={'columns':columns,'rows':rows},raw=s.getvalue())

def presentation(c,id,title,slides):
 c['slides'].append(dict(id=id,path=f'Grundakte/{id}_Lenkungskreis.pptx',title=title,slides=[{'title':a,'bullets':b} for a,b in slides]))

def mandate(c,ref,date,deadline):
 return doc(c,'01','Mandatsanfrage.eml','Betriebliche Altersversorgung – Auftrag und Entscheidungstermin',date,f'Vorstand <vorstand@{ref}.example>','Dr. Nora Treuenfels <mail@monki-treuenfels.example>',f'''Sehr geehrte Frau Dr. Treuenfels,

{c['story']}

{c['assignment']} Bitte bereiten Sie die Unterlagen so auf, dass die Geschäftsleitung bis {deadline} entscheiden kann, welche Variante tatsächlich weiterverfolgt wird. Der Termin ist ein interner Planungstermin; wir erwarten keine Erklärung, dass die arbeitsrechtliche Umsetzung bis dahin sicher abgeschlossen sein werde.

Wir benötigen eine nachvollziehbare Trennung der Arbeitgeber, Versorgungswege, betroffenen Personen und Finanzierungsquellen. Die Pensionsrückstellung in der Konzernrechnung ist nicht unser verfügbares Bankguthaben. Bitte fragen Sie bei Widersprüchen zunächst die in den Unterlagen genannten Sachbearbeiter und halten Sie fest, aus welcher Datei eine Zahl stammt. Ein ungeprüftes Gesamturteil über alle Bestände hilft uns im Vorstand nicht.

Die Personalabteilung hat ihre Exporte auf den unten bezeichneten Stand eingefroren. Nachlieferungen werden mit Eingangsdatum in einem eigenen Ordner gesammelt. Es wurden noch keine Beschäftigten angeschrieben, keine Einigungsstelle angerufen und keine individuellen Zustimmungserklärungen eingesammelt. Bitte entwerfen Sie solche Schritte nur als gesondert zu genehmigende nächste Maßnahmen.

Mit freundlichen Grüßen
Die Geschäftsleitung
{c['client']}''')

def engagement(c,ref,date,budget):
 return doc(c,'02','Mandatsvereinbarung.pdf','Mandatsvereinbarung – betriebliche Altersversorgung',date,CONTACT,c['client'],f'''1 Vertragsparteien und Gegenstand

{c['client']} beauftragt {LAW}, {ADDRESS}, mit der rechtlichen Begleitung des in der Mandatsanfrage beschriebenen Projekts. Federführend bearbeiten Dr. Monkī D. Rufi und Dr. Nora Treuenfels das Mandat unter dem Aktenzeichen MT-{ref.upper()}-2026. Ansprechpartnerin für fachliche Freigaben ist die Geschäftsleitung; Projektmitarbeiter dürfen tatsächliche Angaben übermitteln, aber den Beratungsauftrag nicht eigenmächtig erweitern.

1.1 Geschuldete Leistungen

Die Kanzlei sichtet die zur Verfügung gestellten Versorgungsregelungen, Verträge und Korrespondenzen, erhebt entscheidungserhebliche Lücken und erstellt nach Abstimmung des Sachverhalts eine rechtliche Entscheidungsvorlage. Auf gesonderte Anforderung werden vollständige Entwürfe für Verhandlungen, Beschäftigteninformationen und erforderliche Vertragsänderungen erstellt. Eine automatische Versendung oder Einreichung ist nicht beauftragt. Die Mandantin entscheidet über tatsächliche Umsetzung und Budget.

1.2 Abgrenzung der Beratung

Nicht beauftragt sind die Erstellung eines versicherungsmathematischen Gutachtens, eine Abschlussprüfung, individuelle Steuerberatung der Versorgungsberechtigten oder eine Anlageempfehlung. Die Kanzlei überprüft die rechtliche Bedeutung wirtschaftlicher Annahmen, bestätigt aber nicht die Richtigkeit einer vom Unternehmen gelieferten Barwertberechnung. Für ausländische Unternehmen wird bei Bedarf ein gesonderter Auftrag vereinbart. Das Mandat enthält keine Zusage eines bestimmten bilanziellen Ergebnisses oder einer Zustimmung Dritter.

2 Zusammenarbeit und Dokumente

Die Mandantin stellt maßgebliche Originalfassungen und sämtliche Nachträge bereit. Eine aktuelle Verwaltungstabelle ersetzt die zugrunde liegende Zusage nicht. Wenn eine Datei nur ein Auszug oder eine nicht unterzeichnete Fassung ist, wird dies im Begleitschreiben vermerkt. Die Kanzlei führt ein Eingangsverzeichnis und bewahrt widersprechende Fassungen nebeneinander auf, bis die Mandantin die Herkunft geklärt hat. Sie darf keine nachträgliche Glättung der Personalhistorie als gesicherte Tatsache behandeln.

2.1 Termine und Zwischenstände

Der vereinbarte Entscheidungstermin ist abhängig von der rechtzeitigen Lieferung der entscheidungserheblichen Dokumente. Kann eine Frage mangels Belegen noch nicht abschließend beurteilt werden, legt die Kanzlei die vorhandenen Varianten mit den konkreten Folgen und der fehlenden Information vor. Ein Zwischenstand wird nicht als unterschriftsreife Umsetzungsvorlage gekennzeichnet. Die Parteien stimmen wöchentlich mittwochs einen schriftlichen Sachstand ab.

3 Vergütung und Kostensteuerung

Die Vergütung richtet sich nach der gesondert unterzeichneten Vergütungsvereinbarung. Für die erste Sichtungs- und Strukturierungsphase gilt ein internes Planungsbudget von {budget} EUR netto. Dieses Planungsbudget ist keine pauschale Vergütung und keine Zustimmung zu Mehrleistungen. Bei absehbarer Überschreitung um mehr als zehn Prozent unterrichtet die Kanzlei die Mandantin vor weiterer nicht eilbedürftiger Tätigkeit. Reise- und externe Sachverständigenkosten bedürfen gesonderter Freigabe.

4 Kommunikation und Datenzugriff

Der Datenaustausch erfolgt über den vereinbarten geschützten Datenraum. Beschäftigtendaten werden nur den für das Mandat erforderlichen Personen zugänglich gemacht. Die Parteien verwenden in Arbeitslisten möglichst Personalnummern. Über den Einsatz zusätzlicher Dienstleister und den erforderlichen Zugriff wird gesondert entschieden. Eine allgemeine Zustimmung zur Weitergabe vollständiger Personalakten an frei zugängliche Systeme wird durch diese Vereinbarung nicht erteilt.

5 Freigabe, Beendigung und Aktenherausgabe

Erklärungen gegenüber Beschäftigten, Gremien, Versorgungsträgern oder Behörden bedürfen der inhaltlichen Freigabe der Mandantin. Gesetzliche berufliche Pflichten der Kanzlei bleiben unberührt. Bei Beendigung werden die vom Unternehmen überlassenen Dokumente und die zur Fortführung erforderlichen Arbeitsstände geordnet bereitgestellt; Aufbewahrungspflichten bleiben bestehen. Änderungen des Beratungsgegenstands und zusätzlicher Vertretungsaufträge werden dokumentiert.

Für {c['client']}: Geschäftsleitung, elektronisch freigegeben am {date}.
Für {LAW}: Dr. Nora Treuenfels, Rechtsanwältin, am {date}.''')

def source_policy(c,id,file,date,name,employer,scope,benefit,funding,extras=''):
 return doc(c,id,file,name,date,employer,'Personalabteilung und versorgungsberechtigte Beschäftigte',f'''1 Zweck und persönlicher Geltungsbereich

{employer} gewährt den nachfolgend bezeichneten Beschäftigten eine zusätzliche Versorgung für Alter, Invalidität und Hinterbliebene. {scope} Maßgeblich für die Aufnahme ist die schriftliche Bestätigung der Personalabteilung. Ein späterer Wechsel des Arbeitsbereichs allein hebt eine bereits erteilte Zusage nicht auf. Wer eine besondere schriftliche Einzelzusage erhalten hat, wird im Aufnahmeverzeichnis gesondert geführt; das Verhältnis beider Zusagen ist im Einzelvertrag festzuhalten.

1.1 Beginn und Dienstzeit

Die anrechenbare Dienstzeit beginnt mit dem in der Aufnahmebestätigung bezeichneten Beschäftigungsbeginn. Unbezahlte Freistellungen werden nur angerechnet, wenn dies vor Beginn schriftlich vereinbart worden ist. Krankheit, bezahlter Urlaub und gesetzliche Schutzfristen unterbrechen die Dienstzeit nicht. Bei Teilzeit werden Dienstzeit und Entgelt nach den nachfolgenden Regeln getrennt erfasst; eine doppelte Minderung derselben Teilzeitphase ist nicht vorgesehen.

2 Versorgungsleistung

{benefit}

2.1 Leistungsbeginn

Die Altersrente beginnt grundsätzlich mit dem Monat nach Vollendung des 65. Lebensjahres und Beendigung des Arbeitsverhältnisses. Bei gesetzlich zulässiger vorzeitiger Inanspruchnahme vermindert sich die errechnete Rente um 0,3 Prozent für jeden Monat vor diesem Zeitpunkt, höchstens um 10,8 Prozent. Eine Weiterarbeit über das Versorgungsalter hinaus bedarf einer gesonderten Berechnung; bereits ausgezahlte Renten werden nicht zusätzlich als Dienstzeit vergütet. Die Personalabteilung teilt den errechneten Beginn und die zugrunde gelegten Zeiten schriftlich mit.

2.2 Invalidität und Hinterbliebene

Bei nachgewiesener dauernder voller Erwerbsminderung vor dem regulären Rentenbeginn wird die bis zum Eintritt des Versorgungsfalls erworbene Leistung gezahlt. Die Berechtigten legen den Bescheid des gesetzlichen Rentenversicherungsträgers oder gleichwertige Nachweise vor. Nach dem Tod einer versorgungsberechtigten Person erhält deren bei Eintritt des Versorgungsfalls bestehender Ehepartner 60 Prozent der maßgeblichen Alters- oder Invaliditätsrente. Minderjährige Kinder erhalten je 10 Prozent; die Summe sämtlicher Hinterbliebenenleistungen beträgt höchstens 100 Prozent. Die Prüfung besonderer familiärer Verhältnisse erfolgt anhand der tatsächlichen Nachweise und nicht allein durch einen automatisierten Familienstands-Code.

3 Finanzierung und Durchführung

{funding} Leistungen werden monatlich zum letzten Bankarbeitstag auf das bezeichnete Konto überwiesen. Eine Finanzierung über einen Dritten verändert die vom Arbeitgeber schriftlich erteilte Zusage nur, wenn dies wirksam vereinbart wird. Der Berechtigte erhält bei Aufnahme eine Kopie dieser Ordnung und seiner individuellen Bestätigung. Der Arbeitgeber hält Dienstzeiten, Entgeltgrößen und Beitragsbuchungen nachvollziehbar vor.

3.1 Auskünfte und Änderungen persönlicher Verhältnisse

Die Berechtigten melden Änderungen ihrer Anschrift, Bankverbindung und den Eintritt eines Versorgungsfalls. Eine verspätete Anschriftenmitteilung beseitigt nicht den bestehenden Anspruch. Bei widersprechenden Angaben prüft die Personalabteilung die Belege und gewährt Gelegenheit zur Stellungnahme. Eine automatisch erzeugte Jahresinformation beschreibt den Verwaltungsstand; sie ersetzt keine Vereinbarung über eine Änderung der Zusage.

4 Ausscheiden und Übertragung

Beim Ausscheiden stellt der Arbeitgeber die bis zum Austritt maßgeblichen Dienstzeiten und Berechnungsgrundlagen schriftlich fest. Gesetzlich unverfallbare Ansprüche bleiben erhalten. Eine Übertragung auf einen anderen Arbeitgeber oder Versorgungsträger wird nur auf der Grundlage der im Übertragungszeitpunkt geltenden Voraussetzungen und erforderlichen Erklärungen durchgeführt. Die Personalabteilung veranlasst keine Auszahlung des Rückkaufswerts allein deshalb, weil der Beschäftigte den Arbeitsplatz wechselt.

5 Anpassung und Änderungen dieser Ordnung

Die laufenden Leistungen werden zu den nach Gesetz und individueller Zusage maßgeblichen Zeitpunkten überprüft. Über jede Überprüfung wird eine nachvollziehbare Mitteilung erstellt. Änderungen dieser Ordnung bedürfen einer ausdrücklichen schriftlichen Regelung der zuständigen Parteien; aus einer technischen Umstellung der Personalsoftware folgt keine Änderung. Bereits erteilte Einzelzusagen sind bei der Änderung gesondert zu erfassen. Zwingende gesetzliche Rechte werden durch diese Ordnung nicht eingeschränkt.

6 Schlussbestimmungen

Diese Ordnung tritt mit dem auf dem Titel angegebenen Datum in Kraft. Frühere Regelungen werden nur insoweit ersetzt, wie der persönliche Geltungsbereich dieser Ordnung reicht und eine wirksame Ablösung möglich ist. Sollten einzelne Bestimmungen unwirksam sein, prüfen die Parteien eine wirksame Regelung des betroffenen Gegenstands; eine pauschale einseitige Neufestsetzung der gesamten Versorgung ist damit nicht verbunden.

{extras}

Für den Arbeitgeber: Geschäftsleitung. Für den Betriebsrat: Vorsitz. Unterzeichnete Archivfassung; Übertragung in das elektronische Archiv durch Personalverwaltung.''')

# 1 MEISSNER
m=case('bav-strategie-konzern-meissner-rheinwerk-ag','RHEINGOLD 2030 – vierzehn Ordnungen und drei unterschiedliche Besitzstände','MEISSNER RHEINWERK AG','Düsseldorf','Die MEISSNER RHEINWERK AG baut Industriekomponenten. Acht deutsche Gesellschaften mit Werken in Düsseldorf, Stuttgart und Bremen verwalten vierzehn historisch gewachsene Versorgungsordnungen. Der Vorstand möchte ab 2027 ein einheitliches System für Neueintritte und die noch aktive Belegschaft. CFO Henrick Otterbach-Veltheim nennt zugleich ein Einsparziel von 18 Mio. EUR jährlich. Unterschiedliche Zusagetexte, alte Standortwechsel und nicht abgestimmte Gremien machen aus dem scheinbaren IT-Projekt eine grundlegende Personal- und Finanzentscheidung.','Ermitteln Sie aus den Originalregelungen und Bestandsdaten, welche Gruppen durch die Entwurfsvarianten betroffen sind. Entwickeln Sie einen belastbaren Projektweg mit wirtschaftlicher Gegenrechnung, Zuständigkeitsklärung und vollständigen Entwürfen für die erforderlichen Abstimmungen; entscheiden Sie nicht allein anhand der Bezeichnung „Future Service“.')
mandate(m,'meissner-rheinwerk','2026-10-19','30. November 2026');engagement(m,'rheingold','2026-10-20','85.000')
vo1=source_policy(m,'03','Versorgungsordnung_Duesseldorf_1987.pdf','1987-11-22','Versorgungsordnung Düsseldorf 1987 – unterzeichnete Archivfassung','MEISSNER RHEINWERK AG','Diese Ordnung gilt für die Arbeitnehmer des Düsseldorfer Werks nach einer Aufnahmebestätigung und einer fünfjährigen Wartezeit.','Die jährliche Altersrente beträgt für jedes volle anrechenbare Dienstjahr 0,45 Prozent des letzten vollen jährlichen pensionsfähigen Festgehalts. Es werden höchstens 35 Dienstjahre berücksichtigt. Pensionsfähig sind zwölf feste Monatsgehälter ohne variable Vergütung, Überstundenvergütung und Reisekostenerstattungen. Für Teilzeitabschnitte wird das pensionsfähige Vollzeitgehalt mit dem Verhältnis der vereinbarten zur regelmäßigen Vollzeit multipliziert; die gesamte Leistung ist nach den Zeitabschnitten zu gewichten.','Der Arbeitgeber erfüllt die Direktzusage aus eigenen Mitteln. Die Bildung einer bilanziellen Rückstellung ist keine separate Einzahlung zugunsten einzelner Personen.')
vo2=source_policy(m,'04','Versorgungsordnung_Stuttgart_2002.pdf','2002-10-14','Versorgungsordnung Stuttgart 2002 – Leistungsplan','MEISSNER RHEINWERK Schwabenwerk Produktions GmbH','Diese Ordnung erfasst die im Werk Stuttgart beschäftigten Arbeitnehmer nach fünf Jahren Betriebszugehörigkeit. Aufnahme, Austritt und besondere Zusagen werden in einem eigenen Verzeichnis geführt.','Für jedes volle anrechenbare Dienstjahr beträgt die jährliche Altersrente 0,50 Prozent des letzten jährlichen Festgehalts, höchstens für 35 Dienstjahre. Die Summe aus dieser Betriebsrente und der anrechenbaren gesetzlichen Jahresrente soll 70 Prozent des pensionsfähigen Entgelts nicht überschreiten. Übersteigt sie diese Grenze, wird allein die Betriebsrente auf den Differenzbetrag begrenzt. Die anrechenbare gesetzliche Rente wird aus dem im Versorgungsfall vorgelegten Rentenbescheid ermittelt; für Hochrechnungen ist sie gesondert als Schätzung auszuweisen.','Die Durchführung erfolgt über die Schwabenwerk-Unterstützungskasse e.V. Arbeitgeber und Kasse führen getrennte Unterlagen über die Zusage und die Finanzierung. Der Abschluss einer Rückdeckungsversicherung wird nicht als Änderung des Leistungsversprechens behandelt.')
vo3=source_policy(m,'05','Versorgungsordnung_Bremen_2014.pdf','2014-05-17','Versorgungsordnung Bremen 2014 – Beitragsbausteine','MEISSNER RHEINWERK Bremen GmbH','Diese Ordnung erfasst Neueintritte am Standort Bremen seit dem 1. Januar 2008 und Personen, deren Aufnahme in diese Fassung schriftlich bestätigt worden ist.','Der Arbeitgeber verwendet jährlich 4 Prozent des pensionsfähigen Jahresfestentgelts für einen Versorgungsbaustein. Der für das jeweilige Beitragsjahr maßgebliche Verrentungsfaktor wird mit der Jahresinformation dokumentiert. Für den Beitragsjahrgang 2014 beträgt die jährliche garantierte Altersrente ab 65 je 1.000 EUR Beitrag 45 EUR. Spätere Beitragstabellen gelten ausschließlich für die jeweils bezeichneten neuen Beitragsjahre. Die bereits gebildeten garantierten Bausteine werden durch eine neue Tabelle nicht herabgesetzt. Überschüsse werden gesondert ausgewiesen und nicht ohne entsprechende Zusage als garantiert bezeichnet.','Die Beiträge werden an die Hansebund Pensionsfonds AG überwiesen. Diese fiktive Vertragsbezeichnung bezeichnet den im Gruppenvertrag genannten Durchführungsträger; die Arbeitgeberzusage und die Versicherungsunterlagen werden gesondert archiviert.')
# remove case-breaking word fictitious from archive narrative
m['documents'][-1]['body']=[p.replace('Diese fiktive Vertragsbezeichnung bezeichnet den im Gruppenvertrag genannten Durchführungsträger; ','') for p in m['documents'][-1]['body']]
doc(m,'06','Nachtrag_Schliessung_1999.pdf','Nachtrag zur Düsseldorfer Versorgungsordnung – Schließung für Neueintritte','1999-12-15','MEISSNER RHEINWERK AG / Betriebsrat Düsseldorf','Personalverwaltung', '''1 Schließungsstichtag

Die Aufnahme in die Versorgungsordnung Düsseldorf 1987 endet für Personen, deren Arbeitsverhältnis erstmals nach dem 31. Dezember 1999 beginnt. Bereits bis zu diesem Datum aufgenommene Beschäftigte werden nach der bisherigen Ordnung weitergeführt. Der Stichtag begrenzt weder die künftig anrechenbare Dienstzeit dieser Personen noch die Berücksichtigung späterer Gehaltsentwicklungen.

2 Standortwechsel

Bei einem konzerninternen Wechsel ist vor Unterzeichnung des neuen Arbeitsvertrags schriftlich festzuhalten, ob und in welchem Umfang der neue Arbeitgeber die bisherige Zusage übernimmt. Eine Änderung der organisatorischen Kostenstelle genügt nicht. Die Personalabteilungen sollen eine Kopie der Übernahmebestätigung bei beiden Arbeitgebern ablegen.

3 Durchführung

Bis zum 31. März 2000 erstellt die Personalabteilung eine Liste der zum Stichtag aufgenommenen Beschäftigten. Nachträgliche Korrekturen wegen verspätet erfasster Eintritte sind unter Beifügung des Arbeitsvertrags zu dokumentieren. Alle übrigen Regelungen bleiben unberührt.

Düsseldorf, 15. Dezember 1999. Für die Geschäftsleitung: Gerd Meissner. Für den Betriebsrat: Elke Dornberg.''')
doc(m,'07','Uebernahmebestaetigung_Standortwechsel_2003.pdf','Persönliche Versorgungsbestätigung – Wechsel von Düsseldorf nach Stuttgart','2003-08-25','MEISSNER RHEINWERK Schwabenwerk Produktions GmbH','Frau Maren Scholz, Personalnummer M-0017', '''Sehr geehrte Frau Scholz,

Sie wechseln zum 1. September 2003 aus dem Arbeitsverhältnis mit der MEISSNER RHEINWERK AG in unser Unternehmen. Wir bestätigen Ihnen, dass Ihre betriebliche Altersversorgung nach der Versorgungsordnung Düsseldorf 1987 einschließlich des Nachtrags vom 15. Dezember 1999 fortgeführt wird. Als Beginn der anrechenbaren Dienstzeit gilt der 1. April 1992. Die Beschäftigungszeiten werden ohne Unterbrechung behandelt.

Die für die Versorgung maßgeblichen Gehaltsentwicklungen in Ihrem neuen Arbeitsverhältnis werden nach der bisherigen Ordnung berücksichtigt. Ihre organisatorische Zuordnung zum Stuttgarter Werk führt nicht zur Aufnahme in den Leistungsplan Stuttgart 2002. Eine doppelte Versorgung aus beiden Ordnungen wird nicht zugesagt. Andere Bestandteile Ihres neuen Arbeitsvertrags werden durch diese Bestätigung nicht verändert.

Bitte bewahren Sie diese Bestätigung zusammen mit der Versorgungsordnung auf. Eine Kopie geht an die Personalabteilungen beider Gesellschaften.

Für die Schwabenwerk Produktions GmbH: Personalgeschäftsführer Jens Rademacher. Empfang bestätigt: Maren Scholz, 26. August 2003.''')
doc(m,'08','Projektauftrag_Rheingold.pdf','Projektauftrag RHEINGOLD 2030 – Arbeitsstand Vorstand','2026-10-12','Vorstand MEISSNER RHEINWERK AG','Projektleitung HR und Treasury', '''1 Ausgangslage

Die Pensionsverwaltung betreut vierzehn Ordnungen mit unterschiedlichen Aufnahme- und Berechnungsregeln. Manuelle Nachbearbeitung von 200 bis 300 Fällen pro Monat bindet Personal. Ziel ist, Neueintritte ab 2027 in ein einheitliches Angebot aufzunehmen und bestehende Zusagen so weit wie rechtlich und wirtschaftlich vertretbar zu ordnen. Eine bloße Umbenennung der Altsysteme erfüllt den Auftrag nicht.

2 Wirtschaftliches Ziel

Treasury soll drei Varianten rechnen: Fortführung der bisherigen Systeme, Umstellung künftiger Beiträge bei Erhalt aller bisherigen Berechnungsbezüge und Festschreibung sowohl der Dienstzeit als auch des Entgelts zum 31. Dezember 2026. Die zuletzt genannte Variante wurde noch nicht rechtlich freigegeben. Das jährliche Einsparziel von 18 Mio. EUR betrifft den Personalaufwand der Planung ab 2028; es darf nicht als sofortiger freier Mittelzufluss dargestellt werden.

3 Zuständigkeiten

Die jeweiligen Arbeitgeber bleiben für die Erfüllung ihrer Zusagen zuständig. Der Konzernprojektleiter koordiniert die Daten, kann aber keine Betriebsvereinbarung für sämtliche Gesellschaften allein abschließen. Die Frage der zuständigen Arbeitnehmervertretung soll vor Eröffnung inhaltlicher Verhandlungen dokumentiert werden. Vorhandene Beauftragungsbeschlüsse sind mit ihrem Umfang einzuholen.

4 Entscheidungsvorlage

Die Vorlage soll je Gruppe die derzeitige Zusage, wirtschaftliche Wirkung, betroffene Anspruchselemente, erforderliche Zustimmung und Umsetzungsdauer zeigen. Arbeitnehmerkommunikation darf erst nach Abgleich mit den Originalzusagen freigegeben werden. Eine Versicherungslösung für Rentner wird in diesem Teilprojekt nur als gesonderte Option geführt.

5 Projektbudget

Für externe rechtliche Sichtung sind 85.000 EUR netto, für Datenbereinigung 60.000 EUR und für die gesonderte versicherungsmathematische Bewertung 95.000 EUR reserviert. Die 240.000 EUR Gesamtbudget werden nicht mit den angestrebten laufenden Einsparungen verrechnet. Freigabe: Vorstand Personal und Finanzen, 12. Oktober 2026.''')
doc(m,'09','Konzernstruktur_Arbeitgeber.pdf','Gesellschaften, Arbeitnehmervertretungen und Datenverantwortliche','2026-10-20','Konzernsekretariat MEISSNER RHEINWERK AG','Projektteam RHEINGOLD', '''1 Unternehmen und Betriebe

Die MEISSNER RHEINWERK AG ist Muttergesellschaft und Arbeitgeberin des Düsseldorfer Werks sowie der Konzernzentrale. Die Schwabenwerk Produktions GmbH ist Arbeitgeberin des Stuttgarter Werks. Bremen GmbH, München Komponenten GmbH, Hamburg Logistik GmbH, Eisenach Systeme GmbH, Saarbrücken Service GmbH und Vertrieb Deutschland GmbH sind rechtlich selbstständige Arbeitgeber. Die Holding-Anteilseignerschaft ist kein einheitliches Arbeitsverhältnis.

2 Vertretungsstruktur

In Düsseldorf, Stuttgart, Bremen, München und Hamburg bestehen örtliche Betriebsräte. Die AG besitzt einen Gesamtbetriebsrat für Werk und Zentrale. Ein Konzernbetriebsrat mit Delegierten aus den vertretenen Gesellschaften besteht seit 2011. Das Konzernsekretariat hat bisher nur die Errichtungsunterlagen und den aktuellen Vorsitz übermittelt; konkrete Beauftragungen zur Ablösung der einzelnen Versorgungsordnungen sind damit nicht belegt.

3 Datenwege

Stephan Adloff-Werthmann verantwortet die HR-Sammelliste. Sven-Olaf Bramwasser führt die Versorgungsadministration. Treasury liefert Vermögenswerte, die Abschlussabteilung liefert getrennte HGB- und IFRS-Zahlen. Die Standortpersonalleiter bestätigen individuelle Übernahmen. Das lokale Archiv Stuttgart wird erst am 29. Oktober durchsucht. Zwei Zahlen aus einer gleichnamigen Übersicht dürfen nicht ohne Stichtags- und Konsolidierungskreisprüfung zusammengeführt werden.''')
doc(m,'10','Entwurf_Konzernordnung_2027.docx','Konzernversorgung 2027 – Verhandlungsentwurf der Personalabteilung','2026-10-16','Konzernpersonal MEISSNER RHEINWERK AG','Konzernbetriebsrat', '''1 Beteiligte und Entwurfsstand

Dieser Text ist ein Verhandlungsentwurf der Personalabteilung. Er ist nicht unterzeichnet. Als beteiligte Arbeitgeber sind die AG, die Schwabenwerk Produktions GmbH und Bremen GmbH vorgesehen. Der Konzernbetriebsrat wird um Mitteilung gebeten, für welche Regelungsgegenstände er die Verhandlung übernimmt. Ein Firmenlogo auf diesem Entwurf begründet keine Beauftragung durch örtliche Gremien.

2 Neueintritte

Für erstmals ab dem 1. Januar 2027 eingestellte Beschäftigte der drei Unternehmen soll der Arbeitgeber jährlich 4 Prozent des festen pensionsfähigen Jahresgehalts für eine betriebliche Altersversorgung aufwenden. Variable Vergütung und Aufwendungsersatz bleiben außer Betracht. Die aus den Beiträgen resultierenden zugesagten Leistungen sollen in einer ergänzenden Leistungstabelle bestimmt werden. Ein Durchführungsträger ist noch nicht ausgewählt. Vor seiner Auswahl werden keine individuellen Leistungsbeträge genannt.

3 Bereits Beschäftigte

Für Beschäftigte mit Direkt- oder Unterstützungskassenzusagen soll die nach der bisherigen Ordnung auf den 31. Dezember 2026 hochgerechnete Anwartschaft als Eurobetrag festgehalten werden. Künftige Dienstzeiten und Gehaltssteigerungen sollen diesen Betrag nach Vorstellung der Projektleitung nicht mehr erhöhen. Für Beschäftigungszeiten ab dem 1. Januar 2027 sollen zusätzlich Beiträge gemäß Nummer 2 gezahlt werden. Der festgehaltene Eurobetrag wird in einer individuellen Mitteilung ausgewiesen; Berechnungsfehler können unter Vorlage der Entgelt- und Dienstzeitbelege korrigiert werden.

3.1 Übergangsgutschrift

Beschäftigte, die am 31. Dezember 2026 mindestens 55 Jahre alt sind und mindestens 20 anrechenbare Dienstjahre besitzen, sollen für die Jahre 2027 bis 2030 eine zusätzliche jährliche Gutschrift von 1 Prozent des pensionsfähigen Entgelts erhalten. Für Beschäftigte ab 60 Jahren beträgt sie 2 Prozent. Teilzeit wird anhand des tatsächlich pensionsfähigen Entgelts berücksichtigt. Die Gutschriften sollen zusammen mit dem neuen Beitrag einen getrennten zusätzlichen Baustein bilden. Eine rechtliche oder wirtschaftliche Gleichwertigkeit gegenüber der bisherigen Ordnung ist mit dieser Entwurfsregelung nicht festgestellt.

4 Bereits ausgeschiedene Beschäftigte und Rentner

Unverfallbar ausgeschiedene Beschäftigte und laufende Rentner sollen von den Änderungen nach Nummer 3 nicht erfasst werden. Ihre vorhandenen Zusagetexte, Berechnungsgrundlagen und Anpassungsprüfungen bleiben Gegenstand der bisherigen Verwaltung. Ein späterer Wechsel des Durchführungsträgers soll einer eigenen Entscheidung vorbehalten bleiben.

5 Information und Datenkorrektur

Vor Unterzeichnung soll jeder erfassten Person eine nachvollziehbare Vergleichsberechnung vorgelegt werden. Hierfür benötigt die Personalverwaltung die zugesagte Dienstzeit, den letzten relevanten Gehaltsstand und sämtliche Sonderzusagen. Ein automatischer Systemwert wird nicht allein deshalb verbindlich, weil eine Person auf eine E-Mail nicht antwortet. Betriebsräte erhalten die zur Vorbereitung erforderlichen Informationen in abgestimmter Form.

6 Inkrafttreten und Vorbehalte

Der vorgesehene Starttermin ist der 1. Januar 2027. Ob dieser Termin für alle Gruppen erreichbar ist, bleibt nach Prüfung der Originalzusagen, Zuständigkeiten und Vergleichsrechnungen zu entscheiden. Bis zu einer wirksamen Vereinbarung wird die bisherige Verwaltung fortgeführt. Die Unterzeichnungszeilen sind in dieser internen Verhandlungsfassung noch nicht Bestandteil des Textes.''')
doc(m,'11','KBR_Antwort.pdf','RHEINGOLD – Unterlagen und Vertretungsumfang','2026-10-21','Konzernbetriebsrat MEISSNER RHEINWERK','Vorstand Personal', '''Sehr geehrte Frau Brindeau-Lorbach,

wir sind zur Erörterung eines gemeinsamen Rahmens bereit. Wir erklären damit weder die Zustimmung zu einer Festschreibung noch, dass der Konzernbetriebsrat für jede Versorgungsordnung originär zuständig ist. Bitte legen Sie zunächst den organisatorischen Grund dar, weshalb die einzelnen Leistungen nicht auf Gesellschaftsebene geregelt werden können. Das einheitliche Personalprogramm war auch bisher mit unterschiedlichen Ordnungen betreibbar.

Der Düsseldorfer Gesamtbetriebsrat hat uns am 15. Oktober mit der Sammlung von Informationen beauftragt. Die Beauftragung enthält ausdrücklich keine Abschlussvollmacht für eine Kürzung. Stuttgart hat noch keinen Beschluss gefasst. Bremen verlangt eine eigene Gegenrechnung zum bestehenden Pensionsfondsmodell. Bitte bezeichnen Sie in der Einladung nicht sämtliche örtlichen Gremien als bereits vertreten.

Wir benötigen außerdem die Personalgruppen nach Zusagegrundlage, eine Gegenüberstellung der Gehaltsdynamik und die wirtschaftliche Herleitung des Einsparziels. Ein Gesamtbetrag aus dem Konzernabschluss lässt nicht erkennen, welcher Arbeitgeber welche Last trägt. Für die Sitzung am 4. November reservieren wir drei Stunden.

Reinhardt Sülzbach, Vorsitzender des Konzernbetriebsrats.''')
doc(m,'12','GBR_Beauftragung_Information.pdf','Beschluss des Gesamtbetriebsrats Düsseldorf','2026-10-15','Gesamtbetriebsrat Düsseldorf','Konzernbetriebsrat', '''1 Beschlussgegenstand

Der Gesamtbetriebsrat beauftragt den Konzernbetriebsrat, im Projekt RHEINGOLD Informationen zur Datenstruktur, zu vorgesehenen Verwaltungsabläufen und zu den Arbeitgebervorschlägen einzuholen und in gemeinsamen Gesprächen vorzustellen. Der Auftrag umfasst die Entgegennahme und Ordnung von Unterlagen. Eine Befugnis zum Abschluss einer ablösenden Versorgungsregelung wird nicht übertragen.

2 Informationsrücklauf

Vor einer etwaigen Erweiterung des Auftrags sind die betroffenen Zusagegruppen und die vorgeschlagenen Eingriffe schriftlich zu erläutern. Beschlussunterlagen sollen spätestens sieben Kalendertage vor der nächsten Sitzung vorliegen. Der Gesamtbetriebsrat behält sich die Beteiligung eines eigenen Sachverständigen vor.

3 Abstimmung

Anwesend waren 15 von 17 Mitgliedern. Der Beschluss wurde mit 13 Ja-Stimmen, einer Nein-Stimme und einer Enthaltung gefasst. Die Beschlussfähigkeit wurde festgestellt. Diese Ausfertigung wird am 16. Oktober an den Konzernbetriebsrat und die Personalabteilung übermittelt.

Martina Feldbusch, Vorsitzende. Protokollführung: Jochen Berg.''')
doc(m,'13','Stuttgart_Personalarchiv.eml','Standortwechsler sind im Export anders codiert','2026-10-22','Petra Holm <archiv@schwabenwerk.example>','Stephan Adloff-Werthmann <hr@meissner-rheinwerk.example>', '''Stephan,

die 23 Personen im Reiter „Wechsel“ haben als technischen Schlüssel K-VO-2, weil die alte Abrechnung keine standortfremden Codes zuließ. Daraus kann man nicht schließen, dass alle die Stuttgarter Zusage haben. Für Maren Scholz liegt eine ausdrückliche Übernahme der Düsseldorfer Ordnung vor. Bei den übrigen 22 Personen habe ich bisher nur Arbeitsvertragskopien und nicht alle Beiblätter gefunden.

Bitte lasst die IT die Daten bis zur Klärung nicht auf „bestätigt“ setzen. Ich kann die Archivkisten am 29. Oktober durchsehen; am 28. ist im Werk Inventur. Der Export berücksichtigt auch vier unbezahlte Freistellungen, deren Dienstzeitanrechnung nicht geprüft ist. Die aktuelle Gehaltsspalte stimmt mit der Septemberabrechnung überein, ist aber keine Aussage zum maßgeblichen pensionsfähigen Entgelt.

Petra''',attachments=[f'Grundakte/07_Uebernahmebestaetigung_Standortwechsel_2003.pdf'])
doc(m,'14','CFO_Zielbild.eml','RHEINGOLD – was die 18 Mio. EUR bedeuten sollen','2026-10-22','Henrick Otterbach-Veltheim <cfo@meissner-rheinwerk.example>','Dr. Nora Treuenfels <mail@monki-treuenfels.example>', '''Sehr geehrte Frau Dr. Treuenfels,

der Aufsichtsrat erwartet keine Streichung bereits laufender Renten. Er erwartet, dass wir die Kosten künftiger Beschäftigungszeiten besser planen können. Die 18 Mio. EUR stehen in der Strategieplanung als Einsparziel im jährlichen Aufwand ab 2028. Unser Controlling hat daraus im ersten Foliensatz versehentlich eine „Liquiditätsentlastung 2027“ gemacht. Bitte verwenden Sie diese Folie nicht ohne Erläuterung.

Für das laufende Jahr haben wir positive operative Ergebnisse, gleichzeitig stehen 140 Mio. EUR Investitionen in neue Anlagen und 38 Mio. EUR höhere Finanzierungskosten an. Ich möchte wissen, welche wirtschaftlichen Gründe wir tatsächlich belegen müssen. Ein pauschaler Hinweis auf den Konzernumbau genügt mir nicht. Bitte fordern Sie gezielt die Zahlen des jeweiligen Arbeitgebers an, wenn die Konzernzahlen nicht ausreichen.

Die Fachabteilung hat noch keine Freigabe, das Entgelt bei allen Personen einzufrieren. Ich möchte die Kosten dieser Variante trotzdem sehen, damit wir die Diskussion verstehen.

Mit freundlichen Grüßen
Henrick Otterbach-Veltheim''')
doc(m,'15','Controlling_Planungsgrundlagen.pdf','Planungsgrundlagen 2027 bis 2030 – Stand ohne Rechtsfreigabe','2026-10-23','Konzerncontrolling','Projekt RHEINGOLD', '''1 Abgrenzung

Die beiliegende Tabelle ist ein internes Planungsmodell. Sie enthält keine Bewertung individueller Rentenansprüche und kein versicherungsmathematisches Gutachten. Die Eingaben stammen aus HR, der betrieblichen Budgetplanung und groben Sensitivitätsannahmen. DBO, handelsrechtliche Rückstellung, Steuerwert und verfügbare Liquidität werden getrennt ausgewiesen.

2 Bezugsgrößen

Das Bestandsregister umfasst 14 Ordnungen. Die aktuelle deutsche IFRS-Summe beträgt nach der Tabelle 1.682 Mio. EUR; die frühere Zahl 2.400 Mio. EUR war eine andere internationale Konzernabgrenzung und enthält zudem einen älteren Bewertungsstichtag. Die Zahlen dürfen nicht als zwei Messungen desselben Bestands verglichen werden. Das CTA-Vermögen von 780 Mio. EUR ist zweckgebunden und kein frei verfügbares Giroguthaben.

3 Kalkulation der Zukunftskosten

Für die Beitragsvariante werden nur die aktiven Personen des ausgewählten Bestands mit dem Jahresfestgehalt multipliziert. Aufwands- und Zahlungsannahmen werden nicht als identisch gesetzt. Die Entgeltsteigerung von jährlich 2,8 Prozent ist eine Planannahme; eine feste Zusage wird dadurch nicht ersetzt. Die Finanzierung des Übergangsbeitrags ist im Reiter „Budget“ separat aufgeführt.

4 Grenzen

Die Tabelle enthält keine Sterbewahrscheinlichkeiten und keine vollständigen Rentenbarwerte. Eine Entscheidung über individuelle Vor- oder Nachteile verlangt die nachgelagerte Berechnung anhand der jeweiligen Zusage. Freigabe für den Lenkungskreis nur mit diesem Begleitblatt.''')
doc(m,'16','Berechnungsauftrag_Anbieter.pdf','Angebot Datenbereinigung und versicherungsmathematische Einzelberechnung','2026-10-23','Rheinblick Aktuarservice GmbH, Hafenring 14, 51371 Leverkusen','MEISSNER RHEINWERK AG', '''Sehr geehrte Damen und Herren,

wir bieten die Bereinigung der im ersten Los übergebenen 48 repräsentativen Personalfälle und eine anschließende Einzelberechnung an. Die Auswahl ist keine statistisch repräsentative Stichprobe des Gesamtbestands. Für Personen mit ungeklärter Zusagegrundlage werden getrennte Berechnungsvarianten erstellt; wir entscheiden nicht selbst, welche Versorgungsordnung rechtlich gilt.

1 Leistungen

Wir gleichen Eintritts- und Austrittszeiten, Teilzeitfaktoren, pensionsfähige Gehälter und Zusatzbestätigungen ab. Danach rechnen wir die vom Auftraggeber rechtlich festgelegten Szenarien: unveränderte Fortführung, Dienstzeitbegrenzung bei fortgeführtem Entgeltbezug und Dienstzeit-/Entgeltbegrenzung. Den neuen Beitragsbaustein stellen wir separat dar. Eine bloße Differenz zweier Rückstellungen wird nicht als Verlust einer einzelnen Person ausgewiesen.

2 Preis und Termine

Das Festhonorar für dieses Los beträgt 18.000 EUR netto. Es umfasst zwei Korrekturrunden und einen zweistündigen Ergebnistermin. Die Bearbeitungszeit beträgt zehn Arbeitstage ab vollständigem Eingang der Unterlagen und schriftlicher Szenariofreigabe. Zusätzliche Fälle werden mit 280 EUR netto je Fall berechnet, jedoch erst nach ausdrücklichem Abruf. Die ausgewiesenen Konditionen sind unser individuelles Angebot bis zum 20. November 2026.

3 Voraussetzungen und Grenzen

Benötigt werden Originalzusagen, alle Nachträge, zeitbezogene Entgelt- und Teilzeitdaten sowie die Abgrenzung der berücksichtigten Gehaltsbestandteile. Der Auftrag ersetzt weder die arbeitsrechtliche Entscheidung noch die gesonderte Bewertung nach HGB oder IFRS. Ergebnisse dürfen nur mit den angegebenen Annahmen weiterverwendet werden.

Rheinblick Aktuarservice GmbH, Geschäftsführerin Dr. Alina Hesse.''')
doc(m,'17','Personalgespraech_Scholz.docx','Gesprächsvermerk Maren Scholz – Versorgungsbestätigung','2026-10-24','Petra Holm, Personalverwaltung Stuttgart','Personalakte M-0017', '''1 Anlass und Gesprächsteilnehmer

Maren Scholz meldet sich nach einer internen Information zum Projekt RHEINGOLD bei der Personalverwaltung. Sie ist 58 Jahre alt, arbeitet seit 1992 im Konzern und seit September 2003 in Stuttgart. Petra Holm führt das Gespräch; Stephan Adloff-Werthmann nimmt die letzten zehn Minuten telefonisch teil. Der Vermerk gibt die Aussagen wieder und ist keine Leistungsfestsetzung.

2 Angaben von Frau Scholz

Frau Scholz erklärt, beim Standortwechsel sei ihr zugesichert worden, sie verliere „keinen Tag und keinen Gehaltsbezug“. Sie bringt die schriftliche Bestätigung von 2003 mit. Ihr derzeitiges Jahresfestgehalt beträgt 82.000 EUR, nach der angekündigten tariflichen Anpassung könnte es 2027 höher sein. Sie plant derzeit bis zum 65. Lebensjahr zu arbeiten. Eine Entgeltumwandlung besteht zusätzlich bei einem anderen Träger und gehört nach ihrer Erinnerung nicht zu dieser Zusage.

3 Offene Daten

Der HR-Export weist K-VO-2 aus; die Bestätigung nennt die Düsseldorfer Ordnung. Im Jahr 2016 bestand eine sechsmonatige unbezahlte Pflegefreistellung. Frau Scholz erinnert sich an eine ergänzende E-Mail zur Dienstzeitanrechnung, hat diese aber nicht dabei. Die Personalabteilung sagt eine Archivrecherche zu. Eine verbindliche Rentenhöhe wird in diesem Gespräch nicht genannt.

4 Weiteres Vorgehen

Frau Scholz möchte vor jeder Umstellung die Berechnung mit und ohne künftige Gehaltsentwicklung sehen. Sie stimmt der Weitergabe ihrer Unterlagen an die beauftragte Kanzlei zu. Ein Verzicht oder eine Zustimmung zu einer Änderung wird nicht erklärt.''')
doc(m,'18','Bremen_Rueckfrage.eml','Neue Beitragsordnung versus bereits garantierte Bausteine','2026-10-25','Mila Evers <pensionen@bremen-rheinwerk.example>','Projekt RHEINGOLD <projekt@meissner-rheinwerk.example>', '''Guten Morgen,

bitte behandelt die 917 aktiven Bremer Personen nicht so, als hätten sie alle eine Endgehaltszusage. Bei uns werden bereits Beitragsbausteine aufgebaut. Für 2014 gilt der damals vereinbarte Faktor, für später gezahlte Beiträge gelten andere Tabellen. Die Garantien der bisherigen Bausteine und unverbindliche Überschussangaben stehen in den Jahresinformationen in verschiedenen Spalten.

Der derzeitige Entwurf nennt für alle 4 Prozent Beitrag. Das ist bei uns kein neuer Vorteil, sondern bereits die Grundregel. Wenn die neue Verwaltung geringere Verrentungsfaktoren oder andere Kosten verwendet, kann die gleiche Beitragsquote trotzdem ein anderes Ergebnis ergeben. Wir brauchen deshalb die vollständigen Leistungs- und Kostentabellen des vorgesehenen Anbieters. Der bisherige Gruppenvertrag ist in der Akte; eine neue Angebotstabelle haben wir noch nicht erhalten.

Viele Grüße
Mila Evers''')
doc(m,'19','Gruppenvertrag_Bremen.pdf','Gruppenvertrag Hansebund – Verwaltung und Beitragstabellen','2014-05-17','Hansebund Pensionsfonds AG, Am Wall 116, 28195 Bremen','MEISSNER RHEINWERK Bremen GmbH', '''1 Vertragspartner und Bestand

Die Hansebund Pensionsfonds AG führt die für die Beschäftigten der MEISSNER RHEINWERK Bremen GmbH nach der Versorgungsordnung vom 17. Mai 2014 angemeldeten Beitragsbausteine. Vertragspartner für die Beitragszahlung ist der Arbeitgeber. Die individuellen Leistungsausweise werden den erfassten Beschäftigten jährlich zur Verfügung gestellt. Die Aufnahme einer Person wird erst nach Übereinstimmung von Anmeldung, Beitrag und Identitätsdaten bestätigt.

2 Beiträge und Fälligkeit

Die Arbeitgeberbeiträge werden monatlich am letzten Bankarbeitstag fällig. Der Arbeitgeber übermittelt bis zum 20. des Monats die Personaldaten und die zugehörigen Beiträge. Eine Korrektur bereits gemeldeter Beiträge ist mit Personennummer, Beitragsmonat und Grund zu dokumentieren. Nicht zuordenbare Zahlungen werden auf einem Klärungskonto geführt und nicht ohne Identifizierung einem anderen Beschäftigten zugeschlagen.

3 Garantierte Bausteine

Die garantierte jährliche Altersrente für den Beitragsjahrgang 2014 beträgt je 1.000 EUR Beitrag 45 EUR ab Alter 65. Dieser Faktor gilt ausschließlich für diesen Beitragsjahrgang. Spätere Beitragstabellen werden rechtzeitig vor Beginn des jeweiligen Beitragsjahres schriftlich vereinbart. Bereits gebildete garantierte Bausteine werden durch eine neue Tabelle nicht verändert. Eine unverbindliche Überschussprojektion wird ausdrücklich getrennt ausgewiesen.

4 Daten und Leistungsfall

Bei Eintritt eines Leistungsfalls übermittelt der Arbeitgeber die erforderlichen Beschäftigungs- und Beitragsdaten. Die berechtigte Person legt die für den Leistungsbeginn erforderlichen Nachweise vor. Unstimmigkeiten werden dokumentiert; eine fehlende historische Personalnummer allein berechtigt nicht zur endgültigen Ablehnung einer ansonsten belegten Zuordnung. Der Träger stellt die Berechnung und die verwendeten Bausteine nachvollziehbar dar.

5 Kosten

Für Verwaltung und Leistungsauszahlung werden die in der Beitrags- und Kostentabelle vereinbarten Kosten berücksichtigt. Eine nachträgliche Kostenänderung für bestehende garantierte Bausteine ist hiermit nicht vereinbart. Für zusätzliche Arbeitgeberauswertungen außerhalb der jährlichen Standardinformation ist vorab ein gesondertes Angebot zu erstellen.

6 Beendigung und Bestandsübertragung

Die Kündigung des Gruppenvertrags beendet nicht automatisch die bereits bestehenden Versorgungsrechte. Vor jeder Übertragung sind der betroffene Bestand, sämtliche vorhandenen Bausteine, die erforderlichen Erklärungen und die technische Anschlussverwaltung festzulegen. Der Träger stellt hierzu ein Bestandsverzeichnis zum vereinbarten Stichtag bereit. Die kündigende Partei darf dieses Verzeichnis nicht mit einer Bestätigung der arbeitsrechtlichen Wirksamkeit gleichsetzen.

7 Schlussregelung

Abweichende individuelle Zusagen des Arbeitgebers werden durch diesen Gruppenvertrag nicht aufgehoben. Änderungen dieses Vertrags werden schriftlich dokumentiert. Für den Träger: Vorstand Uwe Reimers. Für den Arbeitgeber: Geschäftsführerin Anke Bremkamp. Unterzeichnung am 17. Mai 2014.''')
doc(m,'20','Treasury_CTA_Bestand.pdf','Rheinland Pension Trust – Vermögensmitteilung','2026-09-30','Rheinland Pension Trust e.V., Rheinbogen 29, 51373 Leverkusen','MEISSNER RHEINWERK AG / Treasury', '''Sehr geehrte Damen und Herren,

zum 30. September 2026 beträgt der im Verwaltungsauszug erfasste Marktwert des Sicherungsvermögens 780.000.000 EUR. Davon entfallen 62.000.000 EUR auf Liquidität, 468.000.000 EUR auf Anleihen, 194.000.000 EUR auf Aktien und 56.000.000 EUR auf Immobilienfonds. Die Werte sind zum genannten Stichtag ermittelte Marktwerte und keine Zusage künftiger Verwertungserlöse.

Das Vermögen ist nach dem Treuhandvertrag zur Sicherung der bezeichneten Versorgungsverpflichtungen gebunden. Es wird nicht automatisch an einen neuen Durchführungsträger ausgekehrt, wenn der Arbeitgeber ein Harmonisierungsprojekt beschließt. Für eine gewünschte Entnahme oder Übertragung benötigen wir den konkreten vertraglichen Tatbestand, die Zuordnung zu den gesicherten Ansprüchen und die erforderlichen Zustimmungen.

In der Projektpräsentation wurde das gesamte Vermögen dem deutschen aktiven Bestand zugerechnet. Unser Auszug enthält auch Sicherungspositionen für ausgeschiedene Berechtigte und Rentner. Bitte verwenden Sie für Einzelgruppen nicht einen pauschalen proportionalen Abzug ohne Prüfung des Treuhandvertrags.

Sabine Korte, Geschäftsführung.''')
doc(m,'21','Protokoll_Lenkungskreis.docx','Lenkungskreis – Datenstand und Entscheidungsvorbereitung','2026-10-26','Projektsekretariat RHEINGOLD','Vorstand, HR, Treasury, Kanzlei', '''1 Teilnehmer und Ziel

Anwesend sind Henrick Otterbach-Veltheim, Constanze Brindeau-Lorbach, Stephan Adloff-Werthmann, Sven-Olaf Bramwasser und Dr. Nora Treuenfels. Die Sitzung dient der Festlegung des zu prüfenden Sachverhalts. Eine Umstellung wird nicht beschlossen.

2 Diskussion der Zahlen

Treasury bestätigt die 780 Mio. EUR als Marktwert des Treuhandvermögens zum 30. September. Der CFO bestätigt, dass die 18 Mio. EUR ein Aufwandseinsparziel ab 2028 sind. Der Personalleiter kann noch nicht bestätigen, dass alle 23 Standortwechsler die im System hinterlegte Zusage besitzen. Die Kanzlei erhält den Auftrag, bei jeder Variante zwischen technischer Verwaltung, Anspruchsinhalt und Finanzierung zu unterscheiden.

3 Gremien und Kommunikation

Der Konzernbetriebsrat hat nur eingeschränkte Beauftragungen vorgelegt. Die AG soll bis zum 2. November die wirtschaftlichen Gründe je betroffenem Arbeitgeber liefern. Eine bereits vorbereitete Beschäftigten-E-Mail mit der Formulierung „Ihre Rechte bleiben vollständig unverändert“ wird zurückgestellt, weil noch keine individuellen Vergleichsberechnungen vorliegen.

4 Termine

Am 4. November findet ein Informationsgespräch mit dem Konzernbetriebsrat statt. Am 10. November sollen die ersten Berechnungsvarianten vorliegen. Der Vorstand entscheidet am 30. November über die weitere Verhandlungsrichtung. Die Personalverwaltung erhält keine Freigabe zur Änderung der Abrechnungsschlüssel.''')
doc(m,'22','Teams_Projektchat.png','Teams – Projektkanal RHEINGOLD am 26. Oktober','2026-10-26','Projektkanal RHEINGOLD','Projektmitglieder', '''09:08 | Controlling – Im Chart steht noch „18 Mio. Cash“. Ich ändere das vor der Sitzung auf „Aufwandsziel ab 2028“.

09:11 | HR – Bitte auch die 23 Stuttgarter Wechsler markieren. Die Übersicht heißt bereinigt, weil Dubletten entfernt sind, nicht weil alle Zusagen geprüft sind.

09:13 | Treasury – Die 780 Mio. dürfen wir nicht für neue Maschinen einplanen. Das ist Treuhandvermögen.

09:17 | Projektleitung – Beschlussfolie heute nur zum Prüfauftrag. Keine Umsetzung zum 1. Januar als schon sicher darstellen.

09:20 | Controlling – Verstanden. Die Version von gestern liegt noch im Vorstandsordner; ich schicke eine Berichtigung mit Datum.''',screen_title='Teams | RHEINGOLD · Projektsteuerung')
doc(m,'23','Budgetfreigabe.pdf','Freigabe der Datenbereinigung – erste Tranche','2026-10-27','Vorstand MEISSNER RHEINWERK AG','Konzerncontrolling', '''Die erste Tranche der externen Einzelberechnung wird mit 18.000 EUR netto freigegeben. Der Betrag wird aus dem Projektbudget für versicherungsmathematische Arbeiten von 95.000 EUR bestritten. Das rechtliche Sichtungsbudget von 85.000 EUR und das interne Datenbereinigungsbudget von 60.000 EUR bleiben hiervon getrennt.

Der Freigabebetrag deckt ausschließlich das Angebot vom 23. Oktober für 48 Personen und die dort beschriebenen zwei Korrekturrunden. Eine Erweiterung auf den Gesamtbestand ist gesondert vorzulegen. Vor Auftragserteilung muss HR die Auswahl nach Ordnungen, Alter, Teilzeit, Standortwechsel und besonderen Zusagen erläutern.

Die Freigabe enthält keine Entscheidung zugunsten einer Ablösungsvariante. Sie berechtigt auch nicht zur Übermittlung vollständiger Personalakten an andere Bieter. Berechnungsdaten werden über den vereinbarten geschützten Datenraum bereitgestellt. Freigegeben: Henrick Otterbach-Veltheim und Constanze Brindeau-Lorbach.''')
doc(m,'24','Archivfund_Stuttgart.eml','Nachlieferung: 22 weitere Wechselbestätigungen und abweichender Vermerk','2026-10-29','Petra Holm <archiv@schwabenwerk.example>','Dr. Nora Treuenfels <mail@monki-treuenfels.example>', '''Sehr geehrte Frau Dr. Treuenfels,

bei der Archivsichtung sind für weitere 18 der 22 gesuchten Personen schriftliche Fortführungsbestätigungen gefunden worden. Zwei Verträge enthalten dagegen ausdrücklich eine neue Stuttgarter Zusage mit gesondertem Besitzstandsbetrag. Für zwei Personen fehlen die unterschriebenen Zusatzseiten weiterhin. Die Namenszuordnung steht in der beigefügten Nachlieferungsliste.

Außerdem enthält die Akte von Frau Scholz einen von beiden Seiten unterzeichneten Freistellungsnachtrag. Danach wird die sechsmonatige Pflegefreistellung von 2016 für die Versorgungsdienstzeit voll angerechnet. Im derzeitigen System fehlen diese sechs Monate. Ich habe den Systemwert nicht überschrieben, damit Sie die Abweichung nachvollziehen können.

Die frühere Auskunft „alle Wechsel einheitlich“ war zu weitgehend. Bitte arbeiten Sie mit den beigefügten Einzelzuordnungen und fragen Sie bei den zwei offenen Fällen vor einer Berechnung nochmals nach.

Mit freundlichen Grüßen
Petra Holm''',phase='Fortsetzung',attachments=['Fortsetzung/25_Freistellungsnachtrag_Scholz.pdf','Fortsetzung/36_Archivabgleich.csv'])
doc(m,'25','Freistellungsnachtrag_Scholz.pdf','Zusatzvereinbarung zur Pflegefreistellung','2016-05-20','MEISSNER RHEINWERK Schwabenwerk Produktions GmbH','Maren Scholz', '''1 Freistellungszeitraum

Frau Maren Scholz wird auf eigenen Wunsch vom 1. Juni bis 30. November 2016 ohne laufende Arbeitsvergütung von der Arbeitsleistung freigestellt. Grund ist die Pflege eines nahen Angehörigen. Das Arbeitsverhältnis besteht fort. Der vereinbarte Wiedereintritt in die bisherige Vollzeitbeschäftigung ist der 1. Dezember 2016.

2 Betriebliche Altersversorgung

Abweichend von der allgemeinen Regel für unbezahlte Freistellungen wird dieser Zeitraum für die anrechenbare Dienstzeit nach der für Frau Scholz fortgeltenden Versorgungsordnung Düsseldorf 1987 vollständig berücksichtigt. Der Arbeitgeber bestätigt die entsprechende Fortführung in der Versorgungsverwaltung. Für die Bestimmung des pensionsfähigen Entgelts gelten die ursprüngliche Ordnung und die Übernahmebestätigung von 2003 fort; die fehlende Vergütung während der Freistellung wird nicht als dauerhaftes Jahresfestgehalt von null behandelt.

3 Sonstige Rechte

Eine zusätzliche Entgeltzahlung für den Freistellungszeitraum wird nicht vereinbart. Die sonstigen Vertragsbestimmungen bleiben unberührt. Die Personalabteilung übersendet Frau Scholz eine Kopie dieser Vereinbarung und dokumentiert die Dienstzeitanrechnung.

Stuttgart, 20. Mai 2016. Unterzeichnet: Maren Scholz und Jens Rademacher, Personalgeschäftsführer.''',phase='Fortsetzung')
doc(m,'26','Bremen_Faktorhinweis.eml','Die neue Anbietertabelle enthält keine Garantie wie 2014','2026-11-03','Mila Evers <pensionen@bremen-rheinwerk.example>','Projekt RHEINGOLD <projekt@meissner-rheinwerk.example>', '''Guten Tag,

die inzwischen eingegangene Kostenskizze des neuen Anbieters arbeitet mit einem prognostizierten Faktor und einem daneben stehenden Mindestwert. In der Controlling-Datei wurde nur die Prognosespalte übernommen. Bitte lassen Sie deshalb keine Aussage versenden, die neue 4-Prozent-Zusage sei bei gleichem Beitrag automatisch gleichwertig.

Die Skizze ist noch kein verbindliches Angebot und enthält auch keine zugesagte Behandlung der bisherigen Bausteine. Ich habe den Anbieter um eine vollständige Leistungsbeschreibung gebeten. Die laufenden Beiträge an Hansebund sollen bis zu einer freigegebenen Umstellung unverändert gezahlt werden. Ein Lastschrifteinzug darf nicht vorsorglich widerrufen werden.

Mila Evers''',phase='Fortsetzung')
doc(m,'27','Vorstand_Zusatzauftrag.eml','Bitte Vergleich für Vorstandssitzung verständlich aufbereiten','2026-11-05','Constanze Brindeau-Lorbach <personalvorstand@meissner-rheinwerk.example>','Dr. Monkī D. Rufi <mail@monki-treuenfels.example>', '''Sehr geehrter Herr Dr. Rufi,

wir benötigen zusätzlich eine Darstellung, die ein Vorstandsmitglied ohne Pensionsspezialwissen versteht. Zeigen Sie bitte an Frau Scholz und zwei weiteren klar bezeichneten Personen, welcher Teil aus bisheriger Dienstzeit stammt, welcher Teil von künftigem Entgelt abhängt und welcher aus weiteren Beschäftigungsjahren entsteht. Wir wollen nicht drei verschiedene Eingriffe unter demselben Wort „Einfrieren“ beschließen.

Die Gegenüberstellung soll Originalregel, Arbeitgeberentwurf, wirtschaftliche Eingaben und noch fehlende Daten getrennt ausweisen. Eine belastbare rechtliche Empfehlung darf erst aus dieser Zuordnung folgen. Bitte schlagen Sie außerdem vor, welche Unterlagen den jeweiligen Betriebsräten vor der nächsten Gesprächsrunde vorgelegt werden müssen.

Es gibt weiterhin keine Einigungsstelle und keinen Rechtsstreit. Der Auftrag bleibt ein Gestaltungs- und Verhandlungsmandat. Den vorgesehenen Start 1. Januar sollen Sie ausdrücklich auf Realisierbarkeit prüfen.

Mit freundlichen Grüßen
Constanze Brindeau-Lorbach''',phase='Fortsetzung')
doc(m,'28','Auswahl_48_Personen.txt','Auswahlvermerk der Personalverwaltung – Berechnungslos 1','2026-10-27','Sven-Olaf Bramwasser','Datenraum RHEINGOLD', '''Die 48 Datensätze sind bewusst ausgewählte Einzelfälle und keine Hochrechnungspopulation. Je 16 Personen stammen aus Düsseldorf, Stuttgart und Bremen. Innerhalb jeder Gruppe wurden verschiedene Eintrittsjahre, Vollzeit- und Teilzeitverläufe sowie rentennahe Personen aufgenommen. Die Person M-0017 ist Maren Scholz; ihre Vertragsabweichung ist gesondert gekennzeichnet.

Im Export bezeichnet „Jahresfestgehalt“ die aktuelle Payroll-Größe. Ob jede Zulage pensionsfähig ist, muss anhand des Originaltexts geprüft werden. „Dienstmonate_System“ ist ein Verwaltungswert; bei Frau Scholz fehlen sechs Monate. „DBO_Gesamt“ ist nicht Bestandteil der Personendatei und darf nicht auf diese 48 Personen proportional verteilt werden.

Der Rechnungsparameter für die künftige Gehaltssteigerung dient nur dem Szenariovergleich. Der Export enthält keine persönlichen Lebenserwartungen. Rentenbarwerte sollen erst nach rechtlicher Festlegung der Szenarien separat beauftragt werden.''')
doc(m,'29','HR_Arbeitspaket_Datenfreigabe.docx','Datenfreigabe – Verantwortliche und noch nicht bestätigte Angaben','2026-10-28','Konzernpersonal','Projektleitung', '''1 Umfang der Freigabe

Die Personalverwaltung bestätigt für den Export vom 27. Oktober die Zahl der ausgewählten Personen, die derzeitige organisatorische Gesellschaftszuordnung und das in September abgerechnete Festgehalt. Sie bestätigt noch nicht die materielle Zuordnung sämtlicher Versorgungsordnungen. Der Status „aktiv“ bezeichnet ein laufendes Arbeitsverhältnis, nicht die Erfüllung aller Aufnahmebedingungen einer bestimmten Zusage.

2 Klärungsschritte

Stuttgart prüft die Standortwechsel und die vier Freistellungsfälle. Düsseldorf gleicht die Einzelzusagen mit der zentralen Liste ab. Bremen stellt die historischen Beitragstabellen und Garantiebestände bereit. Treasury bestätigt nur die Vermögenswerte, nicht die Übertragbarkeit auf einzelne Personen. Controlling dokumentiert die unterschiedlichen Bewertungsstichtage.

3 Verwendung

Die Daten dürfen für die vereinbarte Szenarioplanung verwendet werden, wenn offene Felder sichtbar bleiben. Eine Löschung widersprechender Altwerte oder automatisierte Korrektur ohne Herkunftsbeleg ist nicht freigegeben. Nach Eingang neuer Dokumente wird eine neue Version mit Änderungsprotokoll erstellt. Der unveränderte Export bleibt im Datenraum erhalten.''')
orders=[['K-VO-1','Düsseldorf','Direktzusage',1412,0,1435,487300000,0],['K-VO-2','Stuttgart','Unterstützungskasse',924,178,1054,314200000,112400000],['K-VO-3','Wuppertal','abgewickelt',0,0,0,0,0],['K-VO-4','Vertrieb','Direktversicherung',0,342,87,31400000,31100000],['K-VO-5','Bremen','Pensionsfonds',917,68,324,198700000,187200000],['K-VO-6','München','Direktversicherung',0,97,203,28900000,28700000],['K-VO-7','Vorstand','Einzelzusagen',0,4,11,18700000,0],['K-VO-8','München','Beitragsbausteine',642,0,0,43100000,43100000],['K-VO-9','AT','Einzelzusagen',210,48,126,110000000,0],['K-VO-10','Organbestand','Einzelzusagen',0,2,9,9000000,0],['K-VO-11','Hamburg','Pensionskasse',0,186,342,114000000,86500000],['K-VO-12','Eisenach','Beitragsbausteine',388,12,18,24600000,20300000],['K-VO-13','Standortwechsel','Sondervereinbarungen',23,17,41,62400000,0],['K-VO-14','Saarbrücken','Direktzusage',198,106,262,239700000,0]]
cols=['Ordnung','Bereich','Durchführung','Aktive','Ausgeschiedene','Rentner','IFRS_Wert_EUR','Externes_Vermoegen_EUR']
wb1=workbook(m,'30','Bestandsregister.xlsx','Bestandsregister Deutschland – Verwaltungsstand 30.09.2026',[{'name':'Ordnungen','columns':cols,'rows':orders,'formats':{'IFRS_Wert_EUR':'currency','Externes_Vermoegen_EUR':'currency'}},{'name':'Budget','columns':['Arbeitspaket','Freigabe_EUR','Gebunden_EUR','Verfuegbar_EUR'],'rows':[['Rechtliche Sichtung',85000,0,'=B6-C6'],['Datenbereinigung',60000,0,'=B7-C7'],['Einzelberechnung',95000,18000,'=B8-C8'],['Gesamt','=SUM(B6:B8)','=SUM(C6:C8)','=SUM(D6:D8)']],'formats':{'Freigabe_EUR':'currency','Gebunden_EUR':'currency','Verfuegbar_EUR':'currency'}}])
persons=[]
for i in range(1,49):
 group='K-VO-1' if i<=16 else 'K-VO-2' if i<=32 else 'K-VO-5'
 persons.append([f'M-{i:04}',group,'AG' if i<=16 else 'Schwabenwerk' if i<=32 else 'Bremen',1962+i%22,1988+i%20,round(48000+(i%14)*3200,2),1 if i%4 else .7,(2026-(1988+i%20))*12,'offen' if i in [17,22,29] else 'Verwaltungsstand'])
persons[16]=['M-0017','K-VO-2','Schwabenwerk',1968,1992,82000,1,408,'Übernahmebestätigung K-VO-1 / sechs Monate prüfen']
workbook(m,'31','Personenlos_48.xlsx','Einzelberechnung – 48 ausgewählte Personen',[{'name':'Personen','columns':['Person','Systemordnung','Arbeitgeber','Geburtsjahr','Eintrittsjahr','Jahresfestgehalt_EUR','Teilzeitfaktor','Dienstmonate_System','Pruefstatus'],'rows':persons,'formats':{'Jahresfestgehalt_EUR':'currency'}},{'name':'Szenario_Scholz','columns':['Groesse','Wert','Einheit'],'rows':[['Jahresfestgehalt 2026',82000,'EUR'],['Jährlicher Dienstzeitfaktor',.0045,'Anteil'],['Dienstjahre ohne Korrektur',34,'Jahre'],['Dienstjahre mit sechs Monaten',34.5,'Jahre'],['Plan-Gehaltssteigerung',.028,'Anteil pro Jahr'],['Plan-Jahre bis 65',7,'Jahre'],['Neue Beitragsquote',.04,'Anteil'],['Hinweis','Planungsdaten; keine Barwertbewertung','']]}])
csvdoc(m,'32','Pensionen_Zahlungslauf.csv','Auszug laufender Zahlungen September',['Beleg','Monat','Ordnung','Person','Brutto_EUR','Banklauf'],[[f'PL-09-{i:03}','2026-09','K-VO-1' if i<=12 else 'K-VO-2',f'R-{i:04}',round(420+i*34.75,2),'2026-09-30'] for i in range(1,25)])
csvdoc(m,'33','Projekt_Dokumenteneingang.csv','Eingangsregister Originalfassungen',['Dokument','Datum','Herkunft','Status'],[['Düsseldorf 1987','2026-10-20','Werksarchiv','unterzeichnet'],['Schließung 1999','2026-10-20','Werksarchiv','unterzeichnet'],['Stuttgart 2002','2026-10-20','Kassenverwaltung','unterzeichnet'],['Bremen 2014','2026-10-20','Pensionsverwaltung','unterzeichnet'],['Scholz 2003','2026-10-22','Personalakte','unterzeichnet'],['Konzernordnung 2027','2026-10-20','Projektleitung','Entwurf ohne Unterschrift']])
presentation(m,'34','RHEINGOLD – Entscheidungsvorbereitung',[('Worum es geht',['14 Ordnungen, unterschiedliche Arbeitgeber und Zusagen','Aufwandsziel: 18 Mio. EUR jährlich ab 2028','Start 2027 ist ein Wunsch, noch keine Umsetzung']),('Drei Varianten',['Unveränderte Fortführung','Dienstzeitbegrenzung mit weiterem Entgeltbezug','Dienstzeit und Entgelt festschreiben; Beitragssystem ergänzen']),('Vor Entscheidung klären',['Standortwechsel und Einzelbestätigungen','Beteiligung örtlicher Gremien und KBR','Anspruch, Bilanzwert und Liquidität getrennt vergleichen']),('Nächster Lenkungskreis',['48 Personen gezielt berechnen','Anbieterinformationen vollständig anfordern','Keine Mitarbeiterinformation vor Datenabgleich'])])
doc(m,'35','Datenraum_Ansicht.png','Datenraum – Versionsstände der Personalunterlagen','2026-10-28','Datenraum RHEINGOLD','Projektteam', '''RHEINGOLD / Personal / Stand 28.10.2026

Bestandsregister – freigegeben für Planung – 14 Ordnungen

Personenlos 48 – Status teilweise ungeklärt – verantwortlich HR

Konzernordnung 2027 – Verhandlungsentwurf – NICHT UNTERZEICHNET

Scholz / Fortführung 2003 – Originalscan liegt vor

Archiv Stuttgart / Nachlieferung – angekündigt für 29.10.

Hinweis Projektleitung: Die Markierung „bereinigt“ betrifft Dubletten, nicht die rechtliche Prüfung.''',screen_title='RHEINGOLD | Datenraum · Dokumentenstatus')
csvdoc(m,'36','Archivabgleich.csv','Nachlieferung Standortwechsler',['Fallgruppe','Anzahl','Nachweis','Systemkorrektur'],[['Fortführung Düsseldorf bestätigt',19,'Scholz + 18 Archivbestätigungen','noch nicht vorgenommen'],['Stuttgarter Zusage mit Besitzstand',2,'Neue Aufnahmebestätigung','Einzelberechnung nötig'],['Zusatzseite nicht gefunden',2,'Arbeitsvertrag ohne Beiblatt','offen']],'Fortsetzung')
m['controls']={'order_count':14,'ifrs_total_eur':sum(r[6] for r in orders),'population_total':sum(sum(r[3:6]) for r in orders),'selected_persons':48,'selected_salary_total_eur':sum(r[5] for r in persons),'cta_eur':780000000,'budget_eur':240000,'budget_committed_eur':18000,'archive_switches':23,'chronology':'Grundakte bis 28.10.2026; Fortsetzung beginnt 29.10.2026.'}

def save(c):
 import re
 for d in c['documents']:
  if d['kind']=='eml':
   for f,t in [('sender','from_email'),('recipient','to_email')]:
    match=re.search(r'<([^>]+)>',d[f]); d[t]=match.group(1) if match else ('projekt@'+c['slug'].removeprefix('bav-')+'.example')
  else:
   for f in ['sender','recipient']:
    if '\n' not in d[f] and not re.search(r'\b\d{5}\b',d[f]):
     if 'Treuenfels' in d[f] or 'Rufi' in d[f]: d[f]+='\n'+ADDRESS
     elif c['city']=='Düsseldorf': d[f]+='\nCarlsplatz 12\n40213 Düsseldorf'
     elif c['city']=='Leverkusen': d[f]+='\nAm Werkbogen 14\n51373 Leverkusen'
     elif c['city']=='Duisburg': d[f]+='\nHafenallee 62\n47119 Duisburg'
     else: d[f]+='\nWerkstraße 27\n47829 Krefeld'
 paths={d['path'] for d in c['documents']}|{d['path'] for d in c['workbooks']}|{d['path'] for d in c['slides']}
 for d in c['documents']:
  assert all(p in paths for p in d['attachments']),(c['slug'],d['id'],d['attachments'])
 assert len(paths)==len(c['documents'])+len(c['workbooks'])+len(c['slides'])
 (OUT/(c['slug']+'.json')).write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 print(c['slug'],len(paths),'Originale',sum(len(' '.join(d['body']).split()) for d in c['documents']),'Textwoerter',c['controls'])
save(m)
# 2 CARVE-OUT
c=case('bav-carve-out-rheinbogen-automation','Projekt KANTE – Betriebsübergang, CTA und verschwundene zwölf Personen','Rheinbogen Automation Holding SE','Leverkusen','Die Rheinbogen-Gruppe verkauft ihre Automationssparte mit 842 Beschäftigten an die Nordfeld Industries GmbH. Zur Diskussion stehen der Verkauf der Anteile an der operativen GmbH und eine Übertragung einzelner Betriebsmittel und Arbeitsverhältnisse. Die Transaktionsplanung enthält 46,8 Mio. EUR Pensionsverpflichtungen und 28 Mio. EUR zugeordnetes Treuhandvermögen. Im Kaufpreismodell wird die Vermögensposition bereits abgezogen, obwohl die Treuhänderin eine Übertragung noch nicht bestätigt hat.','Prüfen Sie die beiden tatsächlichen Transaktionswege getrennt. Erstellen Sie eine belegte Zuordnung von Arbeitgebern, Beschäftigten, Zusagen, Verpflichtungen und Sicherungsvermögen sowie eine Entscheidungsvorlage und benötigte Vertragsentwürfe für Signing und Closing.')
mandate(c,'rheinbogen-automation','2026-10-12','27. November 2026');engagement(c,'kante','2026-10-13','110.000')
doc(c,'03','Transaktionsauftrag.pdf','Projekt KANTE – Entscheidung zwischen Anteilsverkauf und Betriebsübertragung','2026-10-09','Rheinbogen Automation Holding SE','Projektteam Verkauf', '''1 Geschäft und Verkaufsziel

Die operative Rheinbogen Automation GmbH entwickelt Anlagensteuerungen und beschäftigt 842 Personen in Leverkusen und Dormagen. Die Holding hält sämtliche Anteile. Der Interessent Nordfeld Industries GmbH will den Geschäftsbereich übernehmen. Der indikative Unternehmenswert beträgt 92 Mio. EUR vor den im Angebot bezeichneten Finanzierungs- und Pensionsanpassungen.

2 Zwei Strukturvarianten

Variante Anteilskauf: Die Nordfeld Industries GmbH erwirbt sämtliche Anteile an der operativen GmbH. Der bestehende Arbeitgeber soll unverändert bleiben. Die Holding verlangt in diesem Fall eine Prüfung ihrer bestehenden Garantien und Treasury-Verflechtungen.

Variante Betriebsübertragung: Nordfeld übernimmt Maschinen, Kundenverträge, IP und die dem Geschäft zugeordneten Arbeitsverhältnisse auf eine neue Erwerbergesellschaft. Für nicht übergehende Personen und alte Rentner muss die Planung ausdrücklich ausweisen, wer weiterhin Schuldner bleibt. Beide Varianten stehen noch zur Verhandlung; eine Entscheidung oder Arbeitnehmerinformation liegt nicht vor.

3 Zeitplan und Freigaben

Am 27. November soll die Verhandlungsrichtung beschlossen werden. Signing ist für Dezember vorgesehen, Closing für den 1. April 2027. Eine Unternehmensbewertung ist kein Gutachten über die Wirksamkeit einer Übertragung von Pensionsverpflichtungen. Treasury, HR und Recht sollen vor dem Beschluss einen gemeinsamen Abgleich vorlegen.''')
doc(c,'04','Term_Sheet_Nordfeld.pdf','Indikatives Term Sheet – Erwerb Automationsgeschäft','2026-10-07','Nordfeld Industries GmbH, Werftstraße 9, 28195 Bremen','Rheinbogen Automation Holding SE', '''1 Gegenstand

Nordfeld beabsichtigt den Erwerb des Automationsgeschäfts. Die Parteien prüfen vorrangig einen Anteilskauf. Sollte die Due Diligence wesentliche nicht abgrenzbare Altlasten zeigen, bleibt als Alternative eine Übertragung des operativen Betriebs auf eine Erwerbergesellschaft offen. Dieses Term Sheet verpflichtet noch nicht zum Abschluss eines Erwerbsvertrags.

2 Preisannahme

Der indikative Unternehmenswert beträgt 92.000.000 EUR. Für das Pensionsmodell legt Nordfeld zunächst einen Verpflichtungswert von 46.800.000 EUR und ein tatsächlich mitübertragenes Sicherungsvermögen von 28.000.000 EUR zugrunde. Die Differenz von 18.800.000 EUR soll als pensionsbezogene Preisanpassung behandelt werden. Weitere Kaufpreisanpassungen für Finanzschulden, Barmittel und Working Capital sind gesondert zu verhandeln. Die 92 Mio. EUR sind daher nicht bereits der zu zahlende Anteilskaufpreis.

3 Voraussetzungen

Die Annahme zum Sicherungsvermögen gilt nur, soweit das Vermögen dem übernommenen Verpflichtungsbestand tatsächlich erhalten bleibt und vertraglich zulässig zugeordnet werden kann. Wir verlangen eine Bestätigung des Treuhänders und eine Liste der Begünstigten. Eine nachträgliche Unterdeckung aus unvollständiger Personenübermittlung soll nicht vom Käufer getragen werden.

4 Personal und Zusagen

Die beigefügte HR-Liste ist ein Arbeitsstand. Zusagen, die nicht in der Liste erscheinen, sind nicht allein deshalb ausgeschlossen. Vor Vertragsunterzeichnung benötigen wir sämtliche Ordnungen, Einzelzusagen, Übernahmebestätigungen und das Verhältnis zwischen dem operativen Unternehmen und der Holding. Der Begriff „economic pension transfer“ soll keine Aussage über eine automatische rechtliche Enthaftung enthalten.

5 Verbindlichkeit

Vertraulichkeit und Zugang zum Datenraum werden gesondert vereinbart. Die wirtschaftlichen Punkte sind bis zum Abschluss der Due Diligence unverbindlich. Dieses Angebot gilt bis 27. November 2026. Dr. Jannik Voss, Geschäftsführer Nordfeld Industries GmbH.''')
source_policy(c,'05','Versorgungsordnung_2009.pdf','2009-01-01','Rheinbogen Versorgung 2009','Rheinbogen Automation GmbH','Diese Ordnung gilt für Beschäftigte der Gesellschaft, die vor dem 1. Januar 2017 aufgenommen wurden. Eine Aufnahme nach diesem Datum bedarf einer gesonderten schriftlichen Bestätigung.','Die jährliche Altersrente beträgt 0,40 Prozent des bei Rentenbeginn maßgeblichen jährlichen Festgehalts für jedes volle Dienstjahr, höchstens für 35 Jahre. Für Teilzeitphasen wird das Verhältnis der vereinbarten Arbeitszeit zur Vollzeit berücksichtigt. Nachgewiesene konzerninterne Vorbeschäftigungszeiten werden nur angerechnet, soweit die Aufnahmebestätigung dies vorsieht.','Die Gesellschaft erteilt eine Direktzusage. Sie kann Vermögen zur Sicherung in eine Treuhand einbringen; das ändert den Schuldner der Zusage nicht allein durch die Einzahlung.')
source_policy(c,'06','Versorgungsordnung_2017.pdf','2017-01-01','Rheinbogen Versorgung 2017 – Beitragsorientierte Zusage','Rheinbogen Automation GmbH','Diese Ordnung gilt für Neueintritte ab dem 1. Januar 2017 ohne entgegenstehende Einzelbestätigung.','Der Arbeitgeber stellt jährlich 3,5 Prozent des pensionsfähigen Jahresfestentgelts als Beitrag bereit. Hieraus entstehen die in der jeweiligen Jahresbestätigung bezeichneten garantierten Leistungsbausteine. Die Versicherung weist garantierte und nicht garantierte Leistungen getrennt aus. Bereits garantierte Bausteine werden nicht aufgrund einer später geänderten Beitragstabelle neu berechnet.','Der Arbeitgeber führt die Beiträge einer Direktversicherung bei der Morgenrhein Lebensversicherung AG zu. Die arbeitsrechtliche Zusage und der Gruppenvertrag werden getrennt verwaltet.')
doc(c,'07','CTA_Treuhandvertrag.pdf','Rheinbogen Pension Trust – Verwaltungstreuhand und Sicherungsabrede','2018-03-15','Rheinbogen Pension Trust e.V., Am Werkbogen 20, 51373 Leverkusen','Rheinbogen Automation Holding SE und Rheinbogen Automation GmbH', '''1 Parteien und Zweck

Die Rheinbogen Automation Holding SE und die Rheinbogen Automation GmbH, nachfolgend gemeinsam Treugeber, übertragen die im Vermögensverzeichnis bezeichneten Werte auf den Rheinbogen Pension Trust e.V. als Treuhänder. Die Verwaltung dient der Finanzierung und Sicherung der im Begünstigtenverzeichnis erfassten Versorgungsverpflichtungen. Das Vermögen ist getrennt vom eigenen Vermögen des Treuhänders zu führen. Die bloße Zuordnung im Konzernabschluss ersetzt keine Eintragung in die vertragsgemäßen Verzeichnisse.

1.1 Zuordnung der Verpflichtungen

Für jede Teilzusage werden Arbeitgeber, begünstigte Person und Sicherungsumfang im Verzeichnis bezeichnet. Bei einer Person mit mehreren Zusageteilen sind getrennte Zuordnungen zulässig. Die Treugeber melden Änderungen schriftlich mit dem zugrunde liegenden Dokument. Nicht nachgewiesene Änderungen werden als Klärungsposten geführt. Ein Kostenstellenwechsel berechtigt nicht zur Umbuchung des gesicherten Arbeitgebers.

2 Vermögensverwaltung

Der Treuhänder legt die Werte nach der vereinbarten Anlagerichtlinie an. Er darf keine Mittel zur allgemeinen Betriebsmittelfinanzierung der Treugeber verwenden. Bis zu 10 Prozent dürfen als Liquiditätsreserve gehalten werden. Verfügungen erfolgen nach dem Vier-Augen-Prinzip und werden dokumentiert. Monatliche Berichte unterscheiden Einzahlungen, Entnahmen, Erträge, Kosten und Bewertungsänderungen.

2.1 Auszahlung zur Erstattung von Renten

Die Erstattung tatsächlich gezahlter gesicherter Renten setzt einen belegten Zahlungsnachweis und die Zuordnung zu einer erfassten Verpflichtung voraus. Eine bloße Aufwandsbuchung reicht nicht aus. Der Treuhänder prüft nicht die vollständige arbeitsrechtliche Richtigkeit des Rentenbescheids, darf bei erkennbaren Widersprüchen jedoch ergänzende Nachweise verlangen.

3 Sicherungsfall

Bei Eintritt des vertraglich bezeichneten Sicherungsfalls werden Auszahlungen an die Treugeber ausgesetzt. Der Treuhänder verwaltet das Vermögen zugunsten der gesicherten Berechtigten nach der Sicherungsabrede. Eine Übertragung auf einen anderen Treuhänder setzt die Wahrung des Sicherungszwecks und die erforderliche vertragliche Prüfung voraus. Gesetzliche Rechte und die Abstimmung mit einem gegebenenfalls zuständigen Sicherungsträger bleiben unberührt.

4 Unternehmensveränderung

Ein Anteilseignerwechsel bei einem Treugeber führt nicht allein zur Freigabe des Sicherungsvermögens. Bei Betriebsübertragungen oder einem Wechsel des Schuldners von Versorgungsverpflichtungen legen die Parteien vorab den betroffenen Bestand und die gewünschte Fortführung der Sicherung fest. Der Treuhänder stimmt einer Auskehrung oder Weiterübertragung erst zu, wenn die rechtliche Zuordnung der Verpflichtungen, der Sicherungszweck und die erforderlichen Erklärungen nachgewiesen sind.

4.1 Teilbestände

Eine Aufteilung erfolgt anhand einer dokumentierten Bewertungs- und Zuordnungsmethode. Ein Anteil des Gesamtvermögens darf nicht allein im Verhältnis der Kopfzahlen entnommen werden. Für bislang nicht zugeordnete Zusageteile ist ein Klärungsbetrag zurückzubehalten. Die Parteien protokollieren den Stichtag, Marktwerte, Transaktionskosten und die Behandlung späterer Korrekturen.

5 Berichte und Prüfung

Der Treuhänder stellt jährlich einen Vermögensnachweis und ein Verzeichnis der erfassten Verpflichtungen zur Verfügung. Die Treugeber bestätigen die Personal- und Leistungsdaten. Fehler werden mit Datum und Ursprungsbeleg korrigiert; die frühere Fassung bleibt nachvollziehbar. Ein Bericht über die Rechnungslegung ist keine Zustimmung zu einer geplanten Transaktion.

6 Laufzeit und Beendigung

Die ordentliche Kündigung ist mit zwölf Monaten Frist zum Jahresende möglich. Sie hebt den Sicherungszweck für bestehende Verpflichtungen nicht auf. Vor Beendigung ist eine gleichwertige Fortführung der vereinbarten Sicherung oder eine andere nach diesem Vertrag zulässige Verwendung festzulegen. Der Treuhänder zahlt das Vermögen nicht allein aufgrund einer Kündigung an die Holding aus.

Unterzeichnet am 15. März 2018: Für die Holding Eva Sandner, für die Automation GmbH Karim Berg, für den Trust Sabine Renne.''')
doc(c,'08','Holding_Garantie_2018.pdf','Zahlungszusage der Holding für die Automation GmbH','2018-03-15','Rheinbogen Automation Holding SE','Rheinbogen Automation GmbH', '''1 Inhalt der Zusage

Die Rheinbogen Automation Holding SE verpflichtet sich gegenüber der Rheinbogen Automation GmbH, ihr auf schriftliche Anforderung die Mittel bereitzustellen, die diese zur fristgerechten Erfüllung der in Anlage „Pensionsbestand 2018“ bezeichneten Versorgungszahlungen benötigt, soweit die Gesellschaft die Mittel nicht aus laufenden Einnahmen oder zulässigen Treuhanderstattungen aufbringen kann. Die jährliche Anforderung ist mit einer Liquiditätsübersicht und den fälligen Zahlungen zu belegen.

2 Begünstigte und Anspruchsinhaber

Vertragliche Gläubigerin dieser Mittelbereitstellungszusage ist die Automation GmbH. Diese Vereinbarung enthält keine ausdrückliche Erklärung gegenüber einzelnen Versorgungsberechtigten. Ob weitere Ansprüche aus anderen Dokumenten bestehen, wird damit nicht geregelt. Die Gesellschaft hat die empfangenen Mittel ausschließlich zur Erfüllung der bezeichneten Versorgungspflichten einzusetzen.

3 Umfang und Dauer

Die Zusage gilt für die erfassten Verpflichtungen bis zu ihrer vollständigen Erfüllung. Eine Änderung der Beteiligungsverhältnisse ist in dieser Vereinbarung nicht als Beendigungsgrund genannt. Die Parteien können eine andere Finanzierung vereinbaren, dürfen damit aber nicht ohne gesonderte Prüfung in Rechte Dritter eingreifen. Eine einseitige Aufhebung durch Übermittlung eines geänderten Konzernorganigramms ist ausgeschlossen.

4 Abrechnung

Über Anforderung und Verwendung wird jährlich abgerechnet. Nicht benötigte Beträge werden nach Abstimmung zurückgeführt, sofern sämtliche fälligen Versorgungszahlungen gedeckt sind. Für Streitigkeiten über die Abrechnung sind zunächst die Finanzleiter beider Unternehmen einzuschalten.

Unterzeichnet am 15. März 2018: Eva Sandner für die Holding; Karim Berg für die Automation GmbH.''')
doc(c,'09','Asset_Deal_Entwurf.docx','Betriebsübertragungsvertrag – Verhandlungsfassung Pensionsregelung','2026-10-14','Nordfeld Industries GmbH','Rheinbogen Automation Holding SE', '''1 Entwurfsstand und Transaktionsumfang

Dieser Vertragstext ist ein nicht unterzeichneter Verhandlungsstand für die Alternative einer Betriebsübertragung. Verkäuferin ist die Rheinbogen Automation GmbH; Käuferin soll die Nordfeld Automation Erwerbsgesellschaft mbH sein. Die zu übertragenden Betriebsmittel, Kundenverträge und Rechte werden in gesonderten Verzeichnissen abschließend bezeichnet. Der Entwurf ist kein Nachweis einer bereits erfolgten Übertragung.

2 Arbeitsverhältnisse

Die Parteien erfassen die dem Betrieb zugeordneten Beschäftigten in einem gemeinsamen Personalverzeichnis. Die tatsächliche Zuordnung wird anhand von Tätigkeit, Organisation und Beschäftigungshistorie geprüft. Die Parteien wollen gesetzlich übergehende Rechte nicht durch eine unvollständige Anlage ausschließen. Für Personen, die einem Übergang widersprechen oder dem übertragenen Betrieb nicht angehören, wird ein gesonderter organisatorischer und wirtschaftlicher Umgang vereinbart.

3 Pensionspflichten im Innenverhältnis

Die Käuferin soll im Verhältnis zur Verkäuferin die nach dem Stichtag wirtschaftlich zu tragenden Verpflichtungen für die tatsächlich übergehenden Arbeitsverhältnisse übernehmen. Der Verkäuferentwurf verwendet hierfür einen Barwert von 46.800.000 EUR. Dieser Wert ist vor Signing mit dem endgültigen Personal- und Zusagebestand abzugleichen. Verpflichtungen gegenüber ausgeschiedenen Berechtigten und Rentnern verbleiben nach dieser Entwurfsfassung zunächst bei der Verkäuferin, soweit nicht ein gesonderter wirksamer Übertragungsweg vereinbart wird.

3.1 Rechte der Berechtigten

Die Regelung des Innenverhältnisses wird gegenüber Beschäftigten nicht als pauschale Befreiung eines bisherigen Schuldners bezeichnet. Gesetzliche Haftung, notwendige Erklärungen und die Wirksamkeit eines Schuldnerwechsels sind gesondert zu beurteilen. Die Verkäuferin darf Beschäftigte nicht allein unter Verweis auf diesen Vertrag an einen anderen Anspruchsgegner verweisen.

4 Treuhandvermögen

Der Kaufpreis berücksichtigt 28.000.000 EUR Sicherungsvermögen nur, soweit die zugehörigen Verpflichtungen und Sicherungsrechte beim Closing tatsächlich entsprechend der freigegebenen Struktur fortgeführt werden. Die Zustimmung des Treuhänders ist Closing-Voraussetzung. Falls der Treuhänder die Übertragung eines Teilbetrags verweigert, werden die Parteien den Kaufpreis und eine alternative Sicherung vor Closing erneut schriftlich festlegen. Eine einseitige Auskehrungsanweisung der Holding reicht nicht aus.

5 Garantien und Daten

Die Verkäuferin soll die Vollständigkeit der übergebenen Versorgungsordnungen, Nachträge, Einzelzusagen und Übernahmebestätigungen erklären. Eine Garantie allein anhand der aktuellen Payroll-Codes ist nicht vorgesehen. Bekannte Datenlücken werden mit betroffenen Personen und wirtschaftlicher Spannweite aufgeführt. Beide Parteien führen einen gemeinsamen Korrekturprozess für später auftauchende Zusageteile.

6 Durchführung und Übergangsleistungen

Für sechs Monate nach Closing soll die bisherige Pensionsadministration technische Dienstleistungen erbringen. Sie entscheidet nicht über streitige Ansprüche und gibt keine rechtsverbindlichen Ablehnungen im Namen der Käuferin ohne Auftrag ab. Die Vertragsparteien legen Verantwortliche, Zugriffsrechte, Datenformate und Eskalation schriftlich fest. Die Vergütung wird im Servicevertrag geregelt.

7 Freigaben und Beendigung

Bis zur Unterzeichnung und Erfüllung der vereinbarten Closing-Voraussetzungen besteht keine Pflicht zum Vollzug dieser Entwurfsfassung. Die Parteien dokumentieren die endgültige Strukturentscheidung. Kommt die Transaktion nicht zustande, bleiben die bisherigen Zusagen und Verwaltungsprozesse unberührt.''')
doc(c,'10','Share_Deal_Entwurf.docx','Anteilsübertragungsvertrag – Pensionsklauseln in Verhandlung','2026-10-14','Rheinbogen Automation Holding SE','Nordfeld Industries GmbH', '''1 Kaufgegenstand und Arbeitgeber

Die Holding soll sämtliche Geschäftsanteile an der Rheinbogen Automation GmbH an Nordfeld verkaufen. Die operative Gesellschaft bleibt nach diesem Vertragsmodell dieselbe juristische Person und Arbeitgeberin. Dieser Entwurf enthält keine Übertragung einzelner Arbeitsverhältnisse auf Nordfeld. Die Beteiligten dürfen gegenüber Beschäftigten aus dem Anteilseignerwechsel allein keinen Wechsel des Versorgungsschuldners ableiten.

2 Kaufpreisrechnung

Der indikative Unternehmenswert von 92.000.000 EUR wird um die vereinbarten Finanzierungs- und Pensionspositionen angepasst. Die vorläufige Pensionsanpassung beträgt 18.800.000 EUR, berechnet aus 46.800.000 EUR Verpflichtungswert abzüglich 28.000.000 EUR zugeordnetem Sicherungsvermögen. Beide Größen beziehen sich auf den vereinbarten wirtschaftlichen Stichtag. Nicht gesicherte oder falsch zugeordnete Zusageteile sind bei der Festlegung der endgültigen Anpassung zu berücksichtigen.

3 Bestehende Sicherheit

Die bestehende Treuhand soll zugunsten der erfassten Verpflichtungen fortgeführt werden. Ein Anteilseignerwechsel wird nicht als Entnahmegrund vereinbart. Die Parteien legen die Fortführung nach Maßgabe des Treuhandvertrags mit dem Treuhänder fest. Die Mittelbereitstellungszusage der Holding vom 15. März 2018 wird nicht bereits durch Unterzeichnung dieses Anteilskaufvertrags als erledigt behandelt. Eine Ablösung bedarf einer gesonderten wirksamen Vereinbarung und Prüfung der betroffenen Rechte.

4 Offenlegung

Die Verkäuferin legt die vorhandenen Zusagetexte und bekannten Sonderbestätigungen offen. Der Käufer erhält einen vollständigen Stand der Personalzuordnung mit Herkunftsbelegen. Eine Zahl aus dem Konzernabschluss gilt nicht als individualisierter Nachweis eines Anspruchs. Für nach Signing entdeckte Dokumente gilt ein Meldeprozess mit Zuordnung zu betroffenen Personen, wirtschaftlicher Bewertung und Entscheidung vor Closing.

5 Freistellung im Innenverhältnis

Die Parteien verhandeln eine Freistellung für vor dem Stichtag verursachte, nicht offengelegte zusätzliche Versorgungslasten. Umfang, Selbstbehalt und Laufzeit sind noch nicht abschließend vereinbart. Dieser Text erteilt weder Arbeitnehmern eine neue Zusage noch beseitigt er vorhandene Ansprüche. Ein Vergleich über konkrete Fälle bedarf gesonderter Zustimmung der dazu berechtigten Personen.

6 Vollzug

Voraussetzung des Vollzugs sind die vereinbarten gesellschaftsrechtlichen und vertraglichen Freigaben, die Bestätigung der Datenübergabe und ein abgestimmter Verwaltungsprozess. Die vorläufige Kaufpreisrechnung wird unmittelbar vor Closing aktualisiert. Bis dahin wird kein Vermögen allein zur Erreichung eines in einer Präsentation genannten Zielwerts aus der Treuhand entnommen.''')
doc(c,'11','HR_Mapping_Methodik.pdf','Personenmapping – Auszug und Gesamtbestand sauber trennen','2026-10-15','Personalabteilung Rheinbogen Automation','Transaktionsteam', '''1 Gesamtbestand

Die verkaufsrelevante Arbeitgeberliste enthält 842 aktive Beschäftigte. Zusätzlich führt die Gesellschaft 216 unverfallbar Ausgeschiedene und 318 laufende Rentner. Diese drei Statusgruppen werden getrennt ausgewiesen. Rentner werden nicht als Beschäftigte behandelt, nur weil sie eine aktive Zahlungsnummer im Abrechnungssystem besitzen.

2 Detailauszug

Der übergebene Detailauszug enthält 60 ausgewählte Personen, darunter 48 reguläre Beschäftigte und zwölf mit historischen Holding-Zusageteilen. Er ist nicht die vollständige Liste aller 842 Beschäftigten. Die 46,8 Mio. EUR Verpflichtungswert stammen aus dem Gesamtbestandsmodell und dürfen nicht aus den 60 Zeilen hochgerechnet werden.

3 Zuordnungsproblem

Zwölf Personen wechselten 2019 aus der Holding in die operative Gesellschaft. Ihr laufendes Arbeitsverhältnis wird dort abgerechnet. Der technische Export zeigt nur den neuen Beitragsplan. Nach einem Vermerk im Altarchiv wurde jedoch ein Zusageteil aus der Holding separat fortgeführt. Ob der neue Arbeitgeber auch diesen Teil übernommen hat, ist anhand der Verträge zu klären. Das Feld „Pension=yes“ beantwortet diese Frage nicht.

4 Datenstatus

Der Auszug ist am 15. Oktober eingefroren. Änderungen werden mit Originalbeleg und Datum nachgeliefert. Das Transaktionsteam darf fehlende Zusagebeträge nicht mit null auffüllen und anschließend als Garantieanlage ausgeben.''')
doc(c,'12','Wechselvertrag_2019.pdf','Dreiseitige Vereinbarung – Wechsel von Jonas Heller','2019-09-20','Rheinbogen Automation Holding SE und Rheinbogen Automation GmbH','Jonas Heller, Personalnummer K-0049', '''1 Wechsel des Arbeitsverhältnisses

Das Arbeitsverhältnis von Jonas Heller mit der Holding endet im gegenseitigen Einvernehmen am 30. September 2019. Mit Wirkung zum 1. Oktober 2019 wird es bei der Automation GmbH zu den im beigefügten Arbeitsvertrag genannten Bedingungen fortgesetzt. Die bisherige Betriebszugehörigkeit seit dem 1. Februar 2001 wird für Kündigungsfrist und Jubiläum berücksichtigt.

2 Betriebliche Altersversorgung

Die bis zum Wechsel bei der Holding erteilte Direktzusage wird hinsichtlich der bis zum 30. September 2019 erdienten Dienstzeit bei der Holding fortgeführt. Der dafür ausgewiesene Jahresrentenbetrag beträgt 4.860 EUR nach dem seinerzeitigen Berechnungsstand. Eine abschließende Festschreibung der nach der Altordnung vorgesehenen Entgeltbezüge ist hiermit nicht vereinbart. Für Beschäftigungszeiten bei der Automation GmbH erfolgt eine neue Aufnahme in den Beitragsplan 2017.

3 Abgrenzung

Die Automation GmbH übernimmt durch diese Vereinbarung nicht ausdrücklich die Schuldnerstellung der Holding für den Altteil. Sie stellt der Holding die zur Berechnung benötigten Entgeltdaten zur Verfügung. Eine Abgeltung oder Auszahlung des Altteils wird nicht vereinbart. Beide Zusageteile werden in der jährlichen Auskunft getrennt ausgewiesen.

4 Dokumentation

Jonas Heller erhält eine Ausfertigung dieser Vereinbarung. Beide Personalabteilungen nehmen sie zu ihrer Akte. Die Umstellung der Personalnummer darf nicht zur Löschung der alten Versorgungszuordnung führen.

Unterzeichnet: Jonas Heller, Eva Sandner für die Holding und Karim Berg für die Automation GmbH, 20. September 2019.''')
# compact but specific correspondence
corr=[
('13','Kaeufer_Datenfrage.eml','Fehlende Altzusagen der zwölf Wechselpersonen','2026-10-16','Nordfeld Due Diligence <dd@nordfeld.example>','HR Rheinbogen <hr@rheinbogen-automation.example>', 'In der Datenraumliste steht für zwölf Personen nur der Beitragsplan 2017. In den Personalkostenunterlagen finden wir aber Zahlungen an die Holding mit dem Text „Altversorgung“. Bitte liefern Sie die zugrunde liegenden Wechselvereinbarungen und bestätigen Sie, ob der Wert von 46,8 Mio. EUR diese Teile enthält. Wir behandeln das Fehlen einer PDF nicht als Beleg, dass keine Verpflichtung besteht.\n\nUnser Preisblatt zieht 28 Mio. EUR Sicherungsvermögen ab. Bitte bestätigen Sie außerdem, ob darin Vermögen für die Holding-Altteile steckt. Eine Zahl, die beide Bestände umfasst, kann nicht unbesehen dem Kaufobjekt zugerechnet werden. Bis zur Klärung bleibt die Pensionsgarantie in unserem Vertragsentwurf offen.'),
('14','Trust_Antwort.pdf','Übertragung des Sicherungsvermögens – Angaben fehlen','2026-10-17','Rheinbogen Pension Trust e.V.','Rheinbogen Automation Holding SE', 'Sehr geehrte Frau Sandner,\n\nwir haben den geplanten Carve-out zur Kenntnis genommen. Eine Zustimmung zur Entnahme oder Übertragung von 28 Mio. EUR liegt nicht vor. Unser Vermögensbericht ist keine Transaktionsfreigabe. Bitte benennen Sie zunächst die gewählte Struktur und den jeweils betroffenen Schuldner der Versorgungsansprüche.\n\nDas aktuelle Teilvermögensverzeichnis enthält 25,6 Mio. EUR für Zusagen der operativen Gesellschaft und 2,4 Mio. EUR für erfasste Holding-Altteile der zwölf Wechselpersonen. Bei einem Anteilskauf kann ein Teilvermögen weiter bestehen; bei einer Übertragung von Betriebsmitteln sind die Zuordnung und die Fortführung der Sicherung gesondert zu dokumentieren. Wir benötigen die beabsichtigten vertraglichen Erklärungen und einen Abgleich der Begünstigtenlisten. Eine prozentuale Aufteilung nur nach Kopfzahl akzeptieren wir nicht.\n\nSabine Renne, Geschäftsführerin.'),
('15','Treasury_Kaufpreis.eml','Preisblatt v3 – 28 Mio. nicht als bereits verfügbar behandeln','2026-10-18','Treasury <treasury@rheinbogen-automation.example>','Transaktionsteam <deal@rheinbogen-automation.example>', 'Im Preisblatt v3 werden 28 Mio. EUR vom Verpflichtungswert abgezogen. Das war eine wirtschaftliche Annahme und keine Zusage des Trusts. Nach dessen Mitteilung hängen 2,4 Mio. EUR mit Holding-Altteilen zusammen. Bitte rechnen Sie eine zusätzliche Variante mit nur 25,6 Mio. EUR zugeordnetem Vermögen.\n\nDie 18,8 Mio. EUR Differenz im Term Sheet und die 21,2 Mio. EUR bei geringerem Vermögensansatz sind keine zwei verschiedenen versicherungsmathematischen Verpflichtungen, sondern zwei Preisannahmen. Ob 46,8 Mio. EUR überhaupt der richtige Verpflichtungskreis ist, bleibt ebenfalls offen. Bitte die beiden Fragen nicht in einer einzigen Korrekturzeile verstecken.'),
('16','BR_Anfrage.pdf','Information zur geplanten Veräußerung','2026-10-19','Betriebsrat Rheinbogen Automation GmbH','Geschäftsführung', 'Sehr geehrter Herr Berg,\n\nBeschäftigte haben in der Kantine von einem „Verkauf der Pensionen“ gehört. Bitte stellen Sie klar, welche Struktur überhaupt geplant ist. Uns liegt lediglich ein Foliensatz mit den Begriffen Share Deal und Asset Deal vor. Eine Erklärung, dass alle Versorgungen unverändert „mitgehen“, lässt sich daraus nicht ableiten.\n\nWir verlangen eine verständliche Darstellung der betroffenen Arbeitgeber und Personengruppen, der bisherigen Zusagen und der geplanten Verwaltung. Besonders die zwölf aus der Holding gewechselten Personen erhalten widersprüchliche Jahresinformationen. Bitte führen Sie uns nicht nur eine aggregierte Barwertzahl vor. Wir schlagen ein Informationsgespräch am 28. Oktober vor. Eine Zustimmung zu Vertragsänderungen ist damit nicht erklärt.\n\nLea Küppers, Betriebsratsvorsitzende.'),
('17','Personalgespraech_Heller.docx','Gesprächsnotiz Jonas Heller','2026-10-20','HR Rheinbogen Automation','Personalakte K-0049', 'Jonas Heller berichtet, dass ihm beim Wechsel 2019 ausdrücklich zwei Versorgungsbestandteile erklärt worden seien. Die letzte Jahresinformation des operativen Arbeitgebers zeige nur die Beiträge seit 2019. Eine gesonderte Information der Holding habe er 2024 erhalten, 2025 aber nicht gefunden. Er habe nie einer Auszahlung oder einem Verzicht zugestimmt.\n\nHeller legt den dreiseitigen Wechselvertrag vor. Sein heutiges Jahresfestgehalt beträgt 88.000 EUR. Die Angabe 4.860 EUR im Vertrag versteht er als damaligen Berechnungsstand, nicht als unveränderlichen Endbetrag. Die Personalverwaltung nimmt diese Auffassung auf, trifft jedoch keine rechtliche Festlegung. Die Entgeltübermittlung an die Holding wurde nach einem Personalsoftwarewechsel im Januar 2025 unterbrochen.\n\nHR sagt die Nachlieferung des Schnittstellenprotokolls zu. Der neue Käufer wurde bisher nicht bevollmächtigt, gegenüber Heller eine verbindliche Rentenauskunft zu erteilen.'),
('18','Schnittstellenprotokoll.txt','Payroll-Schnittstelle Holding – Ereignisprotokoll','2026-10-20','IT-Payroll Rheinbogen','Projekt KANTE', '02.01.2025, 07:12: Import neuer Personalnummern erfolgreich.\n\n02.01.2025, 07:18: Zwölf Datensätze ohne gültiges Zielkennzeichen ALT-HOLDING. Export in Fehlerwarteschlange. Beitragsplan 2017 weiterhin verarbeitet.\n\n03.02.2025: Ticket an HR erstellt. Betroffene IDs K-0049 bis K-0060.\n\n18.02.2025: Ticket auf „erledigt“ gesetzt, weil monatlicher Versicherungsbeitrag erfolgreich lief. Kein Nachweis eines erneuten Altversorgungs-Exports im Ticket.\n\n20.10.2026: Rekonstruktion aus Protokollarchiv durch IT. Der Status „erledigt“ bezieht sich nach dem Kommentar auf den Beitragslauf, nicht auf die fehlende Entgeltmeldung an die Holding.'),
('19','Kaeufer_Versicherungsangebot.pdf','Anfrage zur Fortführung der Direktversicherungen','2026-10-21','Morgenrhein Lebensversicherung AG, Rheinstraße 51, 53113 Bonn','Nordfeld Industries GmbH', 'Sehr geehrte Damen und Herren,\n\nwir können die bestehende Vertragsverwaltung grundsätzlich weiterführen, benötigen aber die endgültige Transaktionsstruktur. Ein Wechsel des Anteilseigners ist in unserer Verwaltung anders zu erfassen als ein Wechsel des Versicherungsnehmers. Vor einer Änderung sind Vertragsnummern, versicherte Personen, Bezugsrechte und Erklärungsbefugnisse abzugleichen.\n\nUnsere Verwaltungsgebühr für den hier angefragten einmaligen Migrationslauf beträgt nach aktuellem Angebot 24.000 EUR netto. Das Angebot umfasst einen Probelauf, eine Fehlerliste und einen produktiven Lauf nach Freigabe. Eine arbeitsrechtliche Enthaftung oder steuerliche Unbedenklichkeitsbestätigung ist nicht Bestandteil unseres Angebots. Garantierte Leistungen bereits bestehender Verträge werden durch die bloße Migration nicht neu kalkuliert.\n\nDas Angebot gilt bis zum 30. November 2026. Für weitere Vertragsänderungen erstellen wir nach Vorlage der konkreten Erklärungen ein gesondertes Angebot.'),
('20','TSA_Administration.docx','Übergangsservicevertrag Pensionsadministration – Entwurf','2026-10-22','Rheinbogen Automation Holding SE','Nordfeld Industries GmbH', '1 Leistungsumfang\n\nDie Holding soll für sechs Monate nach Closing die technische Erfassung, Datenübermittlung und Vorbereitung der monatlichen Zahlungen für die im Übergabeverzeichnis bezeichneten Zusagen übernehmen. Die Verarbeitung erfolgt nach den vom jeweiligen Arbeitgeber freigegebenen Regeln. Die Dienstleisterin entscheidet nicht eigenständig über streitige Leistungsansprüche oder eine Änderung der Zusage.\n\n2 Daten und Zuständigkeit\n\nDer Auftraggeber benennt eine fachlich verantwortliche Person und stellt die verbindlichen Zusagetexte zur Verfügung. Die Dienstleisterin meldet Abweichungen, fehlende Angaben und nicht zuordenbare Personen innerhalb von zwei Arbeitstagen. Die vorhandenen Rohdaten bleiben mit Versionsstand erhalten. Eine Korrektur ist mit Quelle, Datum und Freigabe zu protokollieren.\n\n3 Vergütung\n\nDie monatliche Vergütung beträgt 9.500 EUR netto. Hinzu kommt einmalig 15.000 EUR netto für Einrichtung, Berechtigungsprüfung und Testlauf. Das Gesamtentgelt für sechs Monate beträgt 72.000 EUR netto. Zusätzliche Rechtsberatung, versicherungsmathematische Bewertung und die Migration in ein neues System sind nicht eingeschlossen.\n\n4 Kontrolle und Übergabe\n\nJeder Zahlungsentwurf wird mit den Stammdaten und dem freigegebenen Rentenbescheid abgeglichen. Der Auftraggeber gibt die Zahlung frei. Bei Ende der Laufzeit werden Daten, Änderungsprotokolle und offene Klärungsposten in einem vereinbarten maschinenlesbaren Format übergeben. Bis zur bestätigten Übernahme bleibt ein gemeinsamer Notfallkontakt erreichbar.\n\n5 Vertraulichkeit und Beendigung\n\nZugriffe werden auf die erforderlichen Beschäftigten beschränkt. Die datenschutzrechtlichen Rollen und erforderlichen Vereinbarungen werden vor Beginn verbindlich festgelegt. Ein technisch möglicher Zugriff ist keine allgemeine Freigabe für andere Konzernzwecke. Bei ausbleibendem Closing beginnt dieser Vertrag nicht. Es handelt sich um eine noch nicht unterzeichnete Verhandlungsfassung.'),
('21','Lenkungskreis.docx','Lenkungskreis Projekt KANTE – Stand vor Strukturentscheidung','2026-10-23','Projektsekretariat','Vorstand und Projektteam', 'Die Finanzleitung will den Anteilskauf bevorzugen, weil die operative Gesellschaft als Arbeitgeberin bestehen bleiben könnte. Der Käufer hält die Alternative Betriebsübertragung offen. HR bestätigt, dass die zwölf Holding-Altteile im Personalauszug fehlen. Der Trust hat keinen Mittelabfluss genehmigt.\n\nBeschlossen wird ausschließlich, beide Varianten getrennt zu rechnen und die Zuordnung der zwölf Personen vor der nächsten Preisrunde zu klären. Es wird kein Kaufvertrag freigegeben. Die Holding-Garantie soll im Vertragsvergleich ausdrücklich auftauchen; der Verkäufer hatte sie in der bisherigen Liste „Konzernverflechtungen“ als erledigt markiert, weil keine Mittel angefordert wurden.\n\nNächste Schritte: Archivverträge bis 29. Oktober, aktualisierte Verpflichtungsabgrenzung bis 4. November, Gespräch mit dem Trust am 6. November. Das Personalteam darf noch keine Information versenden, nach der Nordfeld sämtliche Altansprüche schulde.'),
('22','Teams_Closing.png','Projektkanal – der Screenshot mit den grünen Haken','2026-10-23','Projekt KANTE','Transaktionsteam', '14:02 | M&A – Können wir „CTA transfer confirmed“ grün setzen?\n\n14:04 | Treasury – Nein. Wir haben einen Vermögensnachweis, keine Transferzustimmung.\n\n14:06 | HR – Auch „all pensions mapped“ stimmt nicht. Zwölf Holding-Altteile fehlen.\n\n14:09 | M&A – Ich ändere den Status auf offen und nehme beide Punkte in den nächsten Lenkungskreis.\n\n14:12 | Recht – Bitte alte Präsentation archivieren, nicht still überschreiben.'),
('23','Datenzugriff.pdf','Vereinbarung zum kontrollierten Datenraumzugang','2026-10-13','Rheinbogen Automation Holding SE','Nordfeld Industries GmbH', '1 Zulässiger Zweck\n\nDie bereitgestellten Unterlagen dürfen ausschließlich zur Prüfung der geplanten Transaktion verwendet werden. Zugriff erhalten die namentlich benannten Mitglieder des Erwerberteams und dessen beauftragte Berater. Eine Weitergabe an operative Wettbewerbsabteilungen ist nicht gestattet. Personenbezogene Angaben werden soweit möglich durch Projektnummern ersetzt.\n\n2 Zugriff und Rückfragen\n\nDownloads werden protokolliert. Rückfragen zu Einzelpersonen werden über das Projektsekretariat gebündelt; Beschäftigte werden nicht unmittelbar kontaktiert. Bei einem erkennbar nicht erforderlichen personenbezogenen Dokument unterrichtet der Empfänger das Projektteam und verwendet es bis zur Klärung nicht weiter.\n\n3 Ende des Verfahrens\n\nBei Abbruch der Transaktion werden Arbeitskopien nach abgestimmter Rückgabe- oder Löschungsregel behandelt; gesetzliche Aufbewahrungspflichten werden gesondert berücksichtigt. Das Recht zur Einsicht begründet weder eine Zustimmung zur Änderung von Versorgungen noch einen Anspruch auf Übertragung von Sicherungsvermögen.'),
]
for id,file,title,date,sender,recipient,body in corr: doc(c,id,file,title,date,sender,recipient,body)
doc(c,'24','Archivnachlieferung.eml','Zwölf Altteile: fünf Verträge abweichend','2026-10-29','Archiv Holding <archiv@rheinbogen-automation.example>','Dr. Nora Treuenfels <mail@monki-treuenfels.example>', '''Sehr geehrte Frau Dr. Treuenfels,

wir haben alle zwölf Wechselvereinbarungen gefunden. Sieben entsprechen dem Vertrag Heller: Altteil verbleibt bei der Holding. Fünf enthalten eine zusätzliche Vereinbarung vom 30. September 2019, nach der die operative Gesellschaft im Innenverhältnis die Kosten trägt. Die Zusatzvereinbarung ist von den beiden Unternehmen unterschrieben, nicht von den Beschäftigten. Sie bezeichnet sich als „Kostenübernahme“.

Der vorliegende Gesamtwert von 46,8 Mio. EUR enthält nach Rückmeldung der Abschlussabteilung nur die unmittelbaren Zusagen der operativen Gesellschaft. Für die zwölf Holding-Altteile nennt deren interne Modellrechnung weitere 3,6 Mio. EUR. Diese Zahl ist ein gesonderter Planungswert, kein bestätigter Transferpreis. Die Zuordnung muss jetzt mit dem Treuhandvermögen von 2,4 Mio. EUR abgeglichen werden.

Bitte prüfen Sie die Originale und rechnen Sie nicht einfach alle Positionen auf den Kaufpreis auf, bevor die Transaktionsstruktur entschieden ist.''',phase='Fortsetzung',attachments=['Fortsetzung/25_Kostenuebernahme_2019.pdf','Fortsetzung/34_Holding_Altteile.csv'])
doc(c,'25','Kostenuebernahme_2019.pdf','Vereinbarung zwischen Holding und operativer Gesellschaft – fünf Altteile','2019-09-30','Rheinbogen Automation Holding SE','Rheinbogen Automation GmbH', '''1 Gegenstand

Für die fünf in der Anlage mit den Personalnummern K-0056 bis K-0060 bezeichneten Personen erstattet die Automation GmbH der Holding die aus den bis zum Wechsel bestehenden Zusagen tatsächlich zu zahlenden Versorgungsleistungen. Die Erstattung wird jährlich auf Basis der nachgewiesenen Zahlungen abgerechnet. Der in einer Konzernbewertung ausgewiesene Barwert ist keine sofort fällige Zahlung.

2 Verhältnis zu den Beschäftigten

Diese Vereinbarung wird allein zwischen den beiden Gesellschaften geschlossen. Sie enthält keine Erklärung der Beschäftigten und keine an diese gerichtete Mitteilung eines Schuldnerwechsels. Die Holding erteilt weiterhin die Auskünfte zum Altteil. Ob eine spätere Änderung der arbeitsrechtlichen Schuldnerstellung vorgenommen werden soll, bedarf einer gesonderten Prüfung und Vereinbarung.

3 Daten

Die operative Gesellschaft übermittelt die für die Altteilberechnung benötigten Entgeltdaten bis zum 31. Januar des Folgejahres. Fehler und fehlende Datensätze werden innerhalb von zehn Arbeitstagen geklärt. Das Jahresabrechnungsblatt weist die zugrunde liegenden Versorgungszahlungen einzeln aus.

Unterzeichnet am 30. September 2019: Eva Sandner und Karim Berg.''',phase='Fortsetzung')
doc(c,'26','Kaeufer_Neue_Forderung.eml','Preisrunde – Sicherung und Haftung ausdrücklich verhandeln','2026-11-04','Nordfeld Industries <deal@nordfeld.example>','Rheinbogen Holding <deal@rheinbogen-automation.example>', '''Sehr geehrte Frau Sandner,

wir halten unser Interesse am Anteilskauf aufrecht. Nach den Archivfunden erwarten wir jedoch einen vollständigen Überblick der zusätzlichen Kostenübernahmen und der Holding-Altteile. Die bisherige Zusage „46,8 Mio. vollständig“ können wir nicht akzeptieren, solange der Begriff vollständig nicht an einen klaren Verpflichtungskreis gebunden ist.

Bitte stellen Sie die Varianten einschließlich Fortführung der Holding-Garantie, Ersatzsicherung und Verwaltungsservice dar. Wir verlangen nicht die ungeprüfte Zusicherung, jede Form einer wirtschaftlichen Kostenübernahme befreie einen Arbeitgeber. Wir benötigen eine praktisch vollziehbare Struktur mit klarer Zuständigkeit gegenüber den Berechtigten.

Unser Kaufpreismodell bleibt vorläufig. Die ursprünglich abgezogenen 28 Mio. EUR Sicherungsvermögen dürfen nur mit dem Bestand verrechnet werden, für den sie tatsächlich gebunden bleiben. Die nächste Preisrunde findet am 12. November statt.''',phase='Fortsetzung')
doc(c,'27','Trust_Gespraechsnotiz.docx','Telefonat mit der Treuhänderin – Fortführung statt Entnahme','2026-11-06','Rheinbogen Treasury','Projekt KANTE', '''Sabine Renne erläutert, dass der Trust keine Transaktion verbieten wolle, aber eine belegte Zuordnung brauche. Bei unverändertem Arbeitgeber könne das vorhandene Teilvermögen grundsätzlich weiterverwaltet werden; Änderungen der Kontrolle und der Informationswege müssten dennoch vertraglich umgesetzt werden. Eine Auskehrung auf ein gewöhnliches Verkäuferkonto sei etwas anderes als die Fortführung einer Sicherung.

Die 2,4 Mio. EUR für Holding-Altteile würden nicht automatisch der operativen Gesellschaft zugeordnet, nur weil die zwölf Personen dort arbeiten. Die fünf internen Kostenübernahmen müssten im Zusammenhang mit den tatsächlichen Zusagen gelesen werden. Renne fordert einen gemeinsamen Vorschlag von Recht, HR und Treasury mit Bestand, Struktur und vorgesehenen Erklärungen.

Es wird keine Zustimmung protokolliert. Der Trust wird nach Erhalt eines vollständigen Vorschlags innerhalb von zehn Arbeitstagen Stellung nehmen. Der im Projektkalender eingetragene Closing-Termin wird von ihr nicht bestätigt.''',phase='Fortsetzung')
people=[[f'K-{i:04}','Automation GmbH','Aktiv','Plan 2009' if i<=26 else 'Plan 2017',round(43000+i*650,2),'2019 Holding-Wechsel' if i>=49 else 'Regulär','Altteil unklar' if i>=49 else 'Verwaltungsstand'] for i in range(1,61)]
workbook(c,'28','Personal_Detailauszug.xlsx','60 ausgewählte Personalzuordnungen',[{'name':'Auszug_60','columns':['Person','Arbeitgeber','Status','Systemplan','Jahresfestgehalt_EUR','Historie','Pruefstatus'],'rows':people,'formats':{'Jahresfestgehalt_EUR':'currency'}},{'name':'Gesamtbestand','columns':['Status','Personen','Verpflichtungswert_EUR','Herkunft'],'rows':[['Aktiv',842,28600000,'Gesamtbestandsmodell'],['Unverfallbar ausgeschieden',216,6100000,'Gesamtbestandsmodell'],['Rentner',318,12100000,'Gesamtbestandsmodell'],['Gesamt','=SUM(B6:B8)','=SUM(C6:C8)','keine Hochrechnung aus Detailauszug']],'formats':{'Verpflichtungswert_EUR':'currency'}}])
workbook(c,'29','Preisbruecke.xlsx','Vorläufige pensionsbezogene Preisbrücke',[{'name':'Szenarien','columns':['Variante','Unternehmenswert_EUR','Verpflichtung_EUR','Sicherungsvermoegen_EUR','Nettoanpassung_EUR','Wert_vor_sonstigen_Anpassungen_EUR'],'rows':[['Term Sheet',92000000,46800000,28000000,'=C6-D6','=B6-E6'],['Vermögen operative Zusagen',92000000,46800000,25600000,'=C7-D7','=B7-E7']],'formats':{k:'currency' for k in ['Unternehmenswert_EUR','Verpflichtung_EUR','Sicherungsvermoegen_EUR','Nettoanpassung_EUR','Wert_vor_sonstigen_Anpassungen_EUR']}},{'name':'Service','columns':['Leistung','Monate','Monatsbetrag_EUR','Einmalbetrag_EUR','Gesamt_EUR'],'rows':[['Übergangsadministration',6,9500,15000,'=B6*C6+D6']],'formats':{'Monatsbetrag_EUR':'currency','Einmalbetrag_EUR':'currency','Gesamt_EUR':'currency'}}])
csvdoc(c,'30','CTA_Zuordnung.csv','Treuhandvermögen nach Sicherungskreis',['Sicherungskreis','Liquiditaet_EUR','Anleihen_EUR','Fonds_EUR','Gesamt_EUR'],[['Operative Zusagen',1600000,18000000,6000000,25600000],['Holding-Altteile',400000,1500000,500000,2400000]])
csvdoc(c,'31','Versicherungsbeitraege.csv','Monatsbeiträge ausgewählter Personen',['Person','Monat','Jahresfestgehalt_EUR','Beitragssatz','Monatsbeitrag_EUR'],[[r[0],'2026-09',r[4],.035,round(r[4]*.035/12,2)] for r in people[26:]])
presentation(c,'32','Projekt KANTE – zwei Transaktionswege',[('Geschäft und Bestand',['842 aktive Beschäftigte,216 Ausgeschiedene,318 Rentner','Anteilskauf oder Betriebsübertragung noch offen','92 Mio. EUR indikativer Unternehmenswert']),('Pensionen nicht nur als Kaufpreiszeile',['46,8 Mio. EUR operativer Verpflichtungswert','28 Mio. EUR Trustvermögen mit zwei Sicherungskreisen','Zwölf Holding-Altteile nicht im Payroll-System']),('Vor Signing klären',['Persönliche Zusagen und historische Wechsel','Fortführung der Garantie und Treuhand','Separate Haftungs- und Datenregelung']),('Vor Closing bereitstellen',['Endgültige Personen- und Verpflichtungszuordnung','Zustimmungen und arbeitsrechtliche Informationen','Übergangsservice mit klaren Freigaben'])])
doc(c,'33','Datenraum_Status.png','Datenraumstatus KANTE','2026-10-23','Projektsekretariat','Transaktionsteam','''Personalbestand 842 – Gesamtzählung bestätigt

Detailauszug 60 – keine vollständige Garantieanlage

CTA 28 Mio. – Vermögensnachweis vorhanden, Übertragung offen

Holding-Garantie – Vertrag gefunden, Ablösung nicht vereinbart

Zwölf Altteile – Archivsuche bis 29.10.

Vertragsstruktur – zwei Entwürfe, keine Unterschrift''')
csvdoc(c,'34','Holding_Altteile.csv','Nachlieferung zwölf Altteile',['Person','Planungswert_EUR','CTA_Zuordnung_EUR','Interne_Kostenuebernahme','Vertrag'],[[f'K-{i:04}',300000,200000,'ja' if i>=56 else 'nein','Kostenübernahme zusätzlich' if i>=56 else 'Wechselvertrag Altteil Holding'] for i in range(49,61)],'Fortsetzung')
c['controls']={'active_total':842,'deferred_total':216,'retired_total':318,'selected_persons':60,'holding_special_persons':12,'operating_obligation_eur':46800000,'cta_total_eur':28000000,'cta_operating_eur':25600000,'cta_holding_eur':2400000,'holding_extra_obligation_eur':3600000,'tsa_total_eur':72000,'chronology':'Grundakte bis 23.10.2026; Fortsetzung ab 29.10.2026.'}
save(c)
# Fachliche Gegenlese: Zeitachsen und tatsächlich vorhandene Unterlagen.
for d in m['documents']:
 if d['id']=='03':
  d['body']=[p.replace('Bei nachgewiesener dauernder voller Erwerbsminderung vor dem regulären Rentenbeginn wird die bis zum Eintritt des Versorgungsfalls erworbene Leistung gezahlt. Die Berechtigten legen den Bescheid des gesetzlichen Rentenversicherungsträgers oder gleichwertige Nachweise vor.','Bei nachgewiesener dauernder Erwerbsunfähigkeit vor dem regulären Rentenbeginn wird die bis zum Eintritt des Versorgungsfalls erworbene Leistung gezahlt. Maßgeblich ist der Bescheid des gesetzlichen Rentenversicherungsträgers über eine Rente wegen Erwerbsunfähigkeit nach den bei Eintritt des Versorgungsfalls geltenden Voraussetzungen; ein gleichwertiger ärztlicher Nachweis wird gesondert geprüft.') for p in d['body']]
 if d['id']=='05': d['body']=[p.replace('AG. die Arbeitgeberzusage','AG. Die Arbeitgeberzusage') for p in d['body']]
 if d['id']=='16':d['body']=[p.replace('48 repräsentativen Personalfälle','48 gezielt ausgewählten Personalfälle') for p in d['body']]
 if d['id']=='24':
  d['title']=d['subject']='Nachlieferung: Abgleich der 22 weiteren Wechselpersonen'
  d['body'].insert(-1,'Die Scans der 18 weiteren Fortführungsbestätigungen und der beiden neuen Zusagen sind noch nicht in den Datenraum übertragen. Die Nachlieferungsliste ist zunächst ein Fundverzeichnis der Archivverwaltung; sie ersetzt die Prüfung der einzelnen unterschriebenen Texte nicht. Die Originale wurden zur Digitalisierung angefordert.')
 if d['id']=='36':d['date']='2026-10-29'
 if d['id']=='15':d['body'].append('Das Register benennt vierzehn Ordnungen. Im ersten Arbeitspaket liegen nur die vollständigen Texte Düsseldorf 1987 mit Nachtrag 1999, Stuttgart 2002 und Bremen 2014 vor. Für die übrigen elf Ordnungen sind die Registerwerte kein Ersatz für Originaltexte. Sie werden in dieser Phase nicht zur Umsetzung freigegeben; die Projektleitung muss die Unterlagen separat beschaffen.')
for i,r in enumerate(persons,1):
 if i==17:continue
 birth=1960+(i%15)
 entry=(1985+i%14) if i<=16 else (1998+i%12) if i<=32 else (2008+i%9)
 entry=max(entry,birth+18)
 assert entry<=1999 if i<=16 else True
 r[3]=birth;r[4]=entry;r[7]=(2026-entry)*12+8
m['workbooks'][1]['sheets'][1]['rows']=[['Stichtag des Datenexports','2026-09-30','Datum'],['Jahresfestgehalt am Stichtag',82000,'EUR'],['Jährlicher Dienstzeitfaktor',.0045,'Anteil'],['Dienstmonate System',408,'Monate'],['Dienstmonate nach Nachtrag',414,'Monate'],['Volle Dienstjahre am Stichtag',34,'Jahre; beide Varianten'],['Dienstmonate am 31.12.2026 mit Nachtrag',417,'Monate'],['Gehaltssteigerung Planung',.028,'Anteil pro Jahr'],['Plan-Jahre bis 65 ab Jahresende',7,'Jahre; Geburt1968'],['Neue Beitragsquote',.04,'Anteil'],['Hinweis','Sechs Monate ändern am Stichtag noch nicht die Zahl voller Jahre; spätere Jahressprünge prüfen.',''],['Abgrenzung','Planungsmodell; keine Barwertbewertung','']]
for ca,budget in [(m,85000),(c,110000)]:
 doc(ca,'37','Verguetungsvereinbarung.pdf','Vergütungsvereinbarung – Sichtungs- und Strukturierungsphase','2026-10-20' if ca is m else '2026-10-13',CONTACT,ca['client'],f'''1 Vereinbarte Vergütung

Die Parteien vereinbaren für anwaltliche Leistungen in dem mit der Mandatsvereinbarung bezeichneten Projekt eine Vergütung nach Zeitaufwand. Der Stundensatz beträgt für Partner 420 EUR netto und für angestellte Rechtsanwälte 290 EUR netto. Abgerechnet wird in Einheiten von sechs Minuten entsprechend der tatsächlich aufgewendeten Zeit. Reisezeit wird nur bei vorheriger Vereinbarung mit der Hälfte des jeweiligen Satzes berechnet. Umsatzsteuer wird in gesetzlicher Höhe zusätzlich ausgewiesen.

2 Budget und Nachweis

Für die erste Sichtungs- und Strukturierungsphase ist ein Planungsbudget von {budget:,.0f} EUR netto vereinbart. Es ist weder eine Pauschale noch eine Erlaubnis zur unbegrenzten Fortführung. Tätigkeiten werden mit Datum, Bearbeiter, Gegenstand und Dauer nachvollziehbar dokumentiert. Bei absehbarer Überschreitung um mehr als zehn Prozent informiert die Kanzlei vor weiteren nicht eilbedürftigen Arbeiten und holt eine Budgetentscheidung ein. Die Mandantin erhält monatlich einen Tätigkeitsnachweis und eine Rechnung.

3 Abgrenzung und Auslagen

Nicht enthalten sind externe Gutachter, notarielle oder gerichtliche Kosten und individuell beauftragte ausländische Beratung. Solche Kosten werden vor Beauftragung abgestimmt. Allgemeine Büro- und Kommunikationskosten sind in den Stundensätzen enthalten. Für gerichtliche Verfahren ist eine gesonderte Beauftragung erforderlich. Diese Vereinbarung betrifft ein außergerichtliches Beratungsmandat.

4 Hinweis und Fälligkeit

Die vereinbarte Vergütung kann von der gesetzlichen Vergütung abweichen. Ein etwaiger Kostenerstattungsanspruch gegen Dritte umfasst regelmäßig höchstens die nach den gesetzlichen Regeln erstattungsfähige Vergütung; die Mandantin kann daher einen Teil der vereinbarten Kosten selbst tragen. Rechnungen sind binnen 21 Kalendertagen nach Zugang zur Zahlung fällig. Bei Einwendungen teilen die Parteien die beanstandeten Positionen konkret mit.

Unterzeichnet für {ca['client']}: Geschäftsleitung. Unterzeichnet für {LAW}: Dr. Nora Treuenfels. Die Parteien erhalten jeweils eine Ausfertigung.''')
# Kontrollen beziehen sich auf echte Tabellenformeln, Header in Zeile5.
m['workbooks'][0]['controls']=[{'sheet':'Budget','cell':'B9','expected':240000},{'sheet':'Budget','cell':'C9','expected':18000},{'sheet':'Budget','cell':'D9','expected':222000}]
c['workbooks'][0]['controls']=[{'sheet':'Gesamtbestand','cell':'B9','expected':1376},{'sheet':'Gesamtbestand','cell':'C9','expected':46800000}]
c['workbooks'][1]['controls']=[{'sheet':'Szenarien','cell':'E6','expected':18800000},{'sheet':'Szenarien','cell':'F6','expected':73200000},{'sheet':'Szenarien','cell':'E7','expected':21200000},{'sheet':'Service','cell':'E6','expected':72000}]
save(m);save(c)
for d in c['documents']:
 if d['id']=='05': d['body']=[p.replace('Diese Ordnung gilt für Beschäftigte der Gesellschaft, die vor dem 1. Januar 2017 aufgenommen wurden. Eine Aufnahme nach diesem Datum bedarf einer gesonderten schriftlichen Bestätigung.','Diese Ordnung gilt für Beschäftigte der Gesellschaft nach schriftlicher Aufnahmebestätigung. Die Personalabteilung führt das Aufnahmeverzeichnis und händigt bei Aufnahme eine Ausfertigung aus.') for p in d['body']]
 if d['id']=='07':
  pos=d['body'].index('3 Sicherungsfall')
  d['body'][pos+1]='Der Sicherungsfall tritt ein, wenn über das Vermögen eines Treugebers das Insolvenzverfahren eröffnet oder ein entsprechender Eröffnungsantrag mangels Masse rechtskräftig abgewiesen wird. Der Treuhänder wird hierüber unverzüglich unterrichtet. Bis zur Klärung darf er bei einem nachgewiesenen Eröffnungsantrag vorsorglich Erstattungen an den betroffenen Treugeber aussetzen. Die Aussetzung ist keine Feststellung einer Insolvenz durch den Treuhänder. Die getrennten Sicherungskreise anderer Treugeber bleiben gesondert zu beurteilen.'
  d['body'].insert(pos+2,'3.1 Sicherungsabrede und Begünstigte')
  d['body'].insert(pos+3,'Die im Begünstigtenverzeichnis bezeichneten Personen erwerben im Sicherungsfall nach Maßgabe dieser Vereinbarung einen eigenen Anspruch gegen den Treuhänder auf Verwendung des ihnen zugeordneten Sicherungsvermögens zur Erfüllung der erfassten Versorgung. Der Anspruch ist auf das hierfür verfügbare Vermögen und die tatsächlich bestehende Versorgungsforderung begrenzt. Er ist kein zusätzliches zweites Rentenversprechen. Der Treuhänder prüft die Forderungszuordnung, legt einen Zahlungsplan offen und verhindert eine doppelte Befriedigung derselben Forderung. Leistungen eines gesetzlichen Sicherungsträgers und gesetzliche Forderungsübergänge werden abgestimmt und dokumentiert. Die Vertragsparteien erklären durch diesen Vertrag nicht verbindlich, ob und in welchem Umfang im konkreten Sicherungsfall gesetzlicher Insolvenzschutz besteht.')
 if d['id'] in ['09','10']:
  d['title']=d['subject']=('Versorgungsanlage zum Betriebsübertragungsvertrag – Verhandlungsentwurf' if d['id']=='09' else 'Versorgungsanlage zum Anteilskaufvertrag – Verhandlungsentwurf')
  d['body'].insert(0,'Diese Anlage regelt ausschließlich die pensionsbezogenen Punkte einer möglichen Transaktion. Sie ist kein vollständiger Kaufvertrag. Die übrigen Kaufgegenstände, allgemeinen Garantien, kartellrechtlichen Voraussetzungen und allgemeinen Kaufpreisregeln sind nicht Gegenstand dieser Anlage; ein unterzeichneter Hauptvertrag liegt noch nicht vor.')
doc(c,'38','Nachtrag_Schliessung_2016.pdf','Nachtrag zur Versorgungsordnung 2009 – Neueintritte ab 2017','2016-11-22','Rheinbogen Automation GmbH / Betriebsrat','Personalabteilung', '''1 Schließung für Neueintritte

Personen, deren Arbeitsverhältnis erstmals ab dem 1. Januar 2017 beginnt, werden nicht mehr in die Versorgungsordnung 2009 aufgenommen. Für sie soll die gesonderte Versorgungsordnung 2017 gelten. Bereits aufgenommene Beschäftigte bleiben in der bisherigen Ordnung; ihre künftig anrechenbare Dienstzeit und die darin geregelten Entgeltbezüge werden durch diesen Nachtrag nicht begrenzt.

2 Besondere Übernahmen

Bei späteren konzerninternen Wechseln ist schriftlich zu bestimmen, welche Zusage fortgeführt oder neu erteilt wird. Eine technische Zuordnung im Abrechnungssystem ersetzt diese Vereinbarung nicht. Vorhandene individuelle Bestätigungen werden zusammen mit diesem Nachtrag aufbewahrt.

3 Inkrafttreten

Dieser Nachtrag tritt am 1. Januar 2017 in Kraft. Im Übrigen bleibt die Versorgungsordnung vom 1. Januar 2009 unverändert. Unterzeichnet am 22. November 2016: Karim Berg für die Geschäftsführung; Lea Küppers für den Betriebsrat.''')
save(c)
for ca in [m,c]:
 for d in ca['documents']:
  d['body']=[p.replace('85,000 EUR','85.000 EUR').replace('110,000 EUR','110.000 EUR').replace('den dreiseitigen Wechselvertrag','den von drei Parteien unterzeichneten Wechselvertrag') for p in d['body']]
  if ca is c and d['id']=='34':d['date']='2026-10-29'
people[48][4]=88000
# Beitragszeilen aus korrigierten Gehaltsdaten ableiten.
for d in c['documents']:
 if d['id']=='31':
  d['csv']['rows']=[[r[0],'2026-09',r[4],.035,round(r[4]*.035/12,2)] for r in people[26:]]
  ss=io.StringIO();ww=csv.writer(ss,delimiter=';');ww.writerow(d['csv']['columns']);ww.writerows(d['csv']['rows']);d['raw']=ss.getvalue();d['body']=[d['raw']]
save(m);save(c)
# 3 RENTNERGESELLSCHAFT
r=case('bav-rentnergesellschaft-rheinhafen-logistik','Projekt ANKER – Rentnergesellschaft mit drei Angeboten und einer zweifelhaften Immobilie','Rheinhafen Logistik Holding GmbH','Duisburg','Die Rheinhafen-Gruppe will ihr operatives Hafengeschäft neu ordnen. 1.240 laufende Renten und 186 unverfallbare Anwartschaften stehen einem internen Verpflichtungsmodell von 86,4 Mio. EUR gegenüber. Drei Anbieter schlagen Verwaltung, Versicherung beziehungsweise Übernahme einer Rentnergesellschaft vor. Im Vorstand werden zwei unterschiedliche Wege vermischt: Ausgliederung der Versorgung in eine neue Gesellschaft oder Verbleib der Verpflichtungen in der bisherigen Gesellschaft nach Verkauf des operativen Betriebs. Als Finanzierung ist neben Wertpapieren eine Hafenimmobilie vorgesehen.','Vergleichen Sie Struktur, Haftung, Finanzierung und Leistungsumfang der drei Angebote. Entwickeln Sie einen belastbaren Entscheidungsvorschlag mit Stressrechnung, Unterlagenliste und ausformulierten Verhandlungsunterlagen. Prüfen Sie die tatsächlich gewählte Übertragungsstruktur; nehmen Sie keine automatische Befreiung bisheriger Schuldner an.')
mandate(r,'rheinhafen-logistik','2026-10-14','3. Dezember 2026');engagement(r,'anker','2026-10-15','95.000')
source_policy(r,'03','Versorgungsordnung_1994.pdf','1994-04-01','Rheinhafen Versorgung 1994','Rheinhafen Logistik GmbH','Diese Ordnung gilt für Arbeitnehmer der Gesellschaft nach schriftlicher Aufnahme und einer Wartezeit von fünf Jahren. Besondere Einzelzusagen werden im Aufnahmeverzeichnis gesondert dokumentiert.','Die jährliche Altersrente beträgt 0,40 Prozent des letzten jährlichen pensionsfähigen Festgehalts je vollem anrechenbaren Dienstjahr, höchstens für 35 Dienstjahre. Als Festgehalt gelten zwölf Monatsgehälter ohne Überstunden, variable Prämien und Aufwendungsersatz. Bei Teilzeit werden die einzelnen Zeitabschnitte nach ihrem Arbeitszeitanteil gewichtet.','Die Gesellschaft erfüllt die zugesagte Versorgung unmittelbar. Rückstellungen und zugeordnete Kapitalanlagen dienen der Finanzierung, verändern aber nicht allein den Anspruch gegen die Gesellschaft.')
r['documents'][-1]['body']=[p.replace('dauernder voller Erwerbsminderung','dauernder Erwerbsunfähigkeit') for p in r['documents'][-1]['body']]
doc(r,'04','Vorstandsauftrag_Strukturen.pdf','Projekt ANKER – zwei Unternehmensstrukturen getrennt prüfen','2026-10-12','Rheinhafen Logistik Holding GmbH','Recht, Personal, Treasury', '''1 Ausgangssituation

Die operative Rheinhafen Logistik GmbH betreibt Lager und Umschlaganlagen. Sie schuldet die in der Bestandsdatei erfassten Renten und Anwartschaften. Das laufende Hafengeschäft soll teilweise verkauft werden. Der Vorstand will das Pensionsrisiko besser finanzieren und die Verwaltung professionalisieren. Der Verkauf eines Geschäfts und die Übertragung von Versorgungsverpflichtungen sind dabei zwei getrennte Vorgänge.

2 Variante Ausgliederung

In der ersten Variante sollen bezeichnete Versorgungsverpflichtungen und das dazu vorgesehene Vermögen auf eine neu zu gründende Rheinhafen Versorgung GmbH ausgegliedert werden. Das operative Geschäft verbliebe zunächst in der bisherigen Gesellschaft. Vor einer Entscheidung sind der vollständige Übertragungsweg, die ausreichende Ausstattung und fortbestehende Haftungspositionen zu prüfen.

3 Variante Verbleib

In der zweiten Variante wird das operative Geschäft verkauft, während die Pensionsverpflichtungen bei der bisherigen Logistik GmbH verbleiben. Diese würde anschließend im Wesentlichen Versorgung und Vermögen verwalten. Der Projektname „Rentnergesellschaft“ allein beschreibt somit nicht den rechtlichen Entstehungsweg. Aus dem Namen darf keine einheitliche Aussage über Ausstattung, Haftung oder Enthaftung abgeleitet werden.

4 Angebote und Finanzierung

Drei Anbieter wurden gebeten, ihren tatsächlichen Leistungsumfang darzustellen. Das niedrigste Verwaltungsentgelt ist nicht automatisch die wirtschaftlich günstigste Gesamtstruktur. Die Hafenimmobilie wird bisher mit 14 Mio. EUR angesetzt; ein aktueller Nachweis über Belastungen, Sanierungsbedarf und kurzfristige Verwertbarkeit fehlt noch. Der Vorstand verlangt einen Abgleich mit laufenden Zahlungen und Stressszenarien.''')
doc(r,'05','Ausstattungsvereinbarung_Entwurf.docx','Ausstattungsvereinbarung für die geplante Versorgungsgesellschaft – Entwurf','2026-10-16','Rheinhafen Logistik Holding GmbH','Projektteam ANKER', '''1 Gegenstand und Entwurfsstatus

Die Parteien verhandeln eine gesonderte Ausstattungsvereinbarung für die Variante einer Ausgliederung von Versorgungsverpflichtungen. Dieser Text ist kein vollständiger Ausgliederungsvertrag und kein Nachweis einer bereits vollzogenen Umwandlung. Er soll die wirtschaftliche Ausstattung und ihre Kontrolle regeln. Die vollständige gesellschaftsrechtliche Struktur und die erforderlichen Erklärungen sind gesondert vorzubereiten.

2 Übernommener Bestand

Der vorgesehene Bestand umfasst 1.240 laufende Renten und 186 unverfallbare Anwartschaften. Maßgeblich sind die im endgültigen Bestandsverzeichnis bezeichneten Einzelzusagen, Nachträge, Hinterbliebenenleistungen und Anpassungsregelungen. Nicht aufgefundene Unterlagen werden als offene Positionen geführt; eine fehlende Dokumentzeile bedeutet keinen Verzicht der Berechtigten. Die Summe des internen Planungsmodells beträgt 86.400.000 EUR zum 30. September 2026. Sie ist vor Vollzug durch eine gesonderte fachliche Bewertung zu überprüfen.

3 Anfangsausstattung

Vorgesehen sind 8.000.000 EUR liquide Mittel, 50.000.000 EUR Anleihen, 12.000.000 EUR Aktienfonds und eine Hafenimmobilie mit bisher angenommenem Wert von 14.000.000 EUR. Der Gesamtansatz beträgt damit 84.000.000 EUR. Die Immobilie wird nur mit dem nach Prüfung tatsächlich übertragbaren Nettovermögenswert berücksichtigt. Bestehende Sicherheiten, Rechte Dritter, Verwertungskosten und notwendige Sanierungskosten sind offenzulegen. Eine Buchwertfortführung ersetzt diese Prüfung nicht.

3.1 Übertragung und Nachweis

Die liquide Ausstattung muss spätestens zum Vollzugstag auf dem Konto der Versorgungsgesellschaft verfügbar sein. Wertpapiere werden über Depotübertrag mit Wertstellungsnachweis eingebracht. Für die Immobilie sind die erforderlichen schuldrechtlichen und dinglichen Erklärungen sowie die Behandlung bestehender Belastungen vorzubereiten. Der Geschäftsführer bestätigt nur tatsächlich erfolgte und belegte Übertragungen, nicht eine bloße Absichtserklärung.

4 Ergänzende Finanzierung

Nach Vorstellung der Holding soll ein zusätzlicher Finanzierungsrahmen von bis zu 15.000.000 EUR bereitstehen. Rechtsnatur, Gläubiger, Abrufvoraussetzungen und Laufzeit werden in einer gesonderten Vereinbarung festgelegt. Eine mündliche Aussage der Holding ersetzt diese Verpflichtung nicht. Der Rahmen wird nicht als vorhandenes Bankguthaben in den Anfangsbestand aufgenommen.

5 Liquiditätssteuerung

Die Versorgungsgesellschaft erstellt monatlich einen Zahlungsplan für mindestens zwölf Monate und jährlich eine längerfristige Bestandsplanung. Fällige Renten, Verwaltungskosten, Steuern und absehbare Sonderzahlungen werden getrennt erfasst. Die Planung verwendet nachvollziehbare Annahmen; Marktwerte und langfristige Renditeerwartungen werden nicht als sofort verfügbare Zahlungsmittel behandelt. Bei Unterschreitung einer Liquiditätsreserve von sechs Monatsausgaben ist die Geschäftsführung unverzüglich zu unterrichten.

6 Kontrolle und Bericht

Der Bericht enthält Rentenzahlungen, Bestandsveränderungen, Anpassungsprüfungen, Verwaltungsentgelte, Vermögenswerte und Abweichungen vom Plan. Fehlende historische Zusagetexte werden in einem offenen Register geführt. Der Verwaltungsdienstleister darf keine Leistungen allein zur Einhaltung eines Budgets kürzen. Eine Änderung des Leistungsversprechens bedarf eigener rechtlicher Prüfung und der erforderlichen Erklärungen.

7 Haftung und Rechte Dritter

Die Parteien werden den jeweiligen gesetzlichen Übertragungsweg und fortbestehende Haftungspositionen gesondert dokumentieren. Diese Vereinbarung behauptet keine automatische Befreiung der bisherigen Versorgungsschuldner oder der Holding. Eine interne Kosten- oder Risikoübernahme ist von Ansprüchen der Berechtigten zu unterscheiden. Gegenüber Rentnern dürfen nur abgestimmte und rechtlich geprüfte Informationen verwendet werden.

8 Voraussetzungen der Freigabe

Vor einer Unterzeichnung müssen die Bestandsabgrenzung, Bewertung, Immobilientitel, ergänzende Finanzierung, Verwaltung und Verantwortlichkeit vollständig geklärt sein. Der interne Zieltermin ersetzt diese Freigaben nicht. Bis zum Vollzug zahlt die bisherige Schuldnerin die Renten unverändert weiter. Ein Ende der bisherigen Zahlungsfreigaben allein aufgrund einer Projektentscheidung ist ausgeschlossen.''')
doc(r,'06','Betriebsverkauf_Absicht.pdf','Verkauf des Umschlagbetriebs – Eckpunkte des Interessenten','2026-10-13','Westkai Operations GmbH, Speicherstraße 41, 47119 Duisburg','Rheinhafen Logistik GmbH', '''Sehr geehrte Damen und Herren,

unser Interesse richtet sich auf die Umschlaganlagen, Kundenverträge und den hierfür eingesetzten Betrieb. Eine Übernahme des gesamten Gesellschaftsmantels ist derzeit nicht vorgesehen. Wir gehen davon aus, dass bestehende Rentner- und ausgeschiedene Anwärterbestände nicht allein durch den Verkauf der Betriebsmittel auf uns übergehen. Die Behandlung der dem übertragenen Betrieb zugeordneten aktiven Beschäftigten einschließlich ihrer Zusagen muss dagegen gesondert geregelt werden.

Der indikative Kaufpreis von 63 Mio. EUR bezieht sich auf die im technischen Verzeichnis bezeichneten Betriebsmittel und Vertragspositionen. Die Hafenimmobilie Flurstück 428 ist nicht enthalten. Deren Eigentum, Belastungen und Vermietung bleiben im weiteren Verfahren zu prüfen. Eine Annahme, dass der Kaufpreis vollständig zur freien Ausschüttung an die Holding zur Verfügung steht, ist nicht Bestandteil unseres Angebots.

Bis zum 25. November benötigen wir eine verbindliche Beschreibung der Verkaufsgegenstände und der verbleibenden Verpflichtungen. Dieses Schreiben ist unverbindlich und ersetzt weder einen Kaufvertrag noch eine Erklärung gegenüber Beschäftigten oder Versorgungsberechtigten.

Westkai Operations GmbH, Geschäftsführerin Paula van Heek.''')
doc(r,'07','Holding_Unterstuetzung_Entwurf.pdf','Finanzierungsrahmen der Holding – noch nicht unterzeichneter Entwurf','2026-10-18','Rheinhafen Logistik Holding GmbH','Rheinhafen Versorgung GmbH in Planung', '''1 Vorgesehene Verpflichtung

Die Holding soll der Versorgungsgesellschaft bis zu 15.000.000 EUR zur Verfügung stellen, wenn deren laufende Liquidität zur Erfüllung der im freigegebenen Bestandsverzeichnis erfassten Versorgungspflichten nicht ausreicht. Der Entwurf bezeichnet die Gesellschaft als Gläubigerin. Eigene unmittelbare Ansprüche der Rentner werden in dieser Fassung nicht ausdrücklich eingeräumt.

2 Abruf und Nachweis

Ein Abruf soll einen vom Geschäftsführer unterzeichneten Zwölfmonats-Liquiditätsplan, die fälligen Zahlungen und einen Abgleich der verfügbaren Mittel enthalten. Nach Vorstellung der Holding soll die Auszahlung binnen zehn Bankarbeitstagen erfolgen. Noch offen ist, ob eine vorherige Verwertung sämtlicher Wertpapiere oder der Immobilie verlangt werden darf. Diese Frage ist vor Unterzeichnung zu entscheiden.

3 Laufzeit und Rang

Die Holding schlägt eine Laufzeit von zehn Jahren vor. Verlängerung, Verzinsung, Rückzahlbarkeit und ein möglicher Rangrücktritt sind noch nicht verbindlich vereinbart. Der Entwurf darf deshalb nicht als bereits vorhandene dauerhafte Eigenkapitalausstattung behandelt werden. Rückzahlungen dürfen nur nach einem gesondert freigegebenen Finanzierungsplan erfolgen.

4 Strukturentscheidung

Der Finanzierungsrahmen soll nur für die Variante einer neu gegründeten Versorgungsgesellschaft gelten. Für den Verbleib der Verpflichtungen in der bisherigen Logistik GmbH enthält dieser Text noch keine entsprechende Zusage. Eine Anpassung wäre ausdrücklich vorzunehmen. Geschäftsführung und Gesellschafter haben den Entwurf noch nicht freigegeben.''')
providers=[('08','Nordanker','Nordanker Pension Services GmbH','Kaistraße 8, 40221 Düsseldorf',84000000,180000,98000,'Verwaltung im bestehenden Schuldnerunternehmen','Wir übernehmen die technische Administration und bereiten Zahlungsdateien vor. Die vorhandene Gesellschaft bleibt Schuldnerin. Wir erwerben keine Gesellschaftsanteile und versprechen keine befreiende Übernahme der Renten. Die Anlageentscheidung bleibt bei der Gesellschaft; ein Vermögensverwaltungsmandat ist nicht Bestandteil dieses Angebots.','Die Gesellschaft stellt das zu verwaltende Vermögen selbst. Der Betrag von 84 Mio. EUR ist eine vom Auftraggeber gelieferte Modellgröße und keine von uns bestätigte ausreichende Ausstattung.'),('09','Rentenfels','Rentenfels Leben AG','Bonner Ufer 23, 50968 Köln',102600000,240000,0,'Rückdeckungsversicherung des bezeichneten Bestands','Wir bieten den Abschluss einer Rückdeckungsversicherung für den im Datenstand bezeichneten Bestand an. Versicherungsnehmerin und Arbeitgeberin bleiben zunächst dieselbe Gesellschaft. Ob im Anschluss ein anderer Rechtsweg zur Übertragung von Verpflichtungen gewählt werden kann, ist nicht Gegenstand dieses Angebots. Der Versicherungsvertrag allein wird von uns nicht als Befreiung des arbeitsrechtlichen Schuldners bezeichnet.','Der vorläufige Einmalbeitrag beträgt 102,6 Mio. EUR. Er setzt den unveränderten Bestand, die bezeichneten Leistungsregeln und die vollständigen historischen Daten voraus. Verwaltungskosten sind im angebotenen Beitrag enthalten; zusätzliche rechtliche Transaktionskosten sind nicht eingeschlossen.'),('10','Hafenruh','Hafenruh Versorgungsmanagement GmbH','Werftallee 11, 20457 Hamburg',94500000,350000,120000,'Erwerb einer zuvor ausgestatteten Versorgungsgesellschaft','Wir bieten nach vorgelagerter Strukturierung den Erwerb der Anteile an einer Versorgungsgesellschaft an. Die Gesellschaft selbst bleibt Trägerin der in ihr vorhandenen Verpflichtungen. Wir verlangen eine vollständige rechtliche und wirtschaftliche Prüfung der vorgelagerten Übertragung. Unser Anteilserwerb ist keine Erklärung, dass alle bisherigen Haftungspositionen anderer Gesellschaften erlöschen.','Wir verlangen vor Anteilserwerb eine liquide beziehungsweise frei übertragbare Ausstattung von 94,5 Mio. EUR. Die Hafenimmobilie wird nur nach gesonderter Bewertung und Zustimmung angerechnet. Eine offene Finanzierungszusage der Holding rechnen wir nicht zum geforderten Anfangsvermögen. Zusätzlich fallen 350.000 EUR Einrichtung und 120.000 EUR jährliche Administration an.')]
for id,short,name,address,capital,setup,annual,kind,scope,funding in providers:
 doc(r,id,f'Angebot_{short}.pdf',f'Angebot {short} – {kind}','2026-10-20',f'{name}, {address}','Rheinhafen Logistik Holding GmbH',f'''Sehr geehrte Frau Lindkamp,

wir danken für die Unterlagen zum Projekt ANKER. Unser Angebot bezieht sich auf 1.240 laufende Renten und 186 unverfallbare Anwartschaften nach dem übergebenen Bestandsstand. Die folgenden Konditionen sind ein individuelles Angebot unseres Hauses; sie enthalten keine Feststellung eines allgemeinen Marktpreises.

1 Gegenstand

{scope}

1.1 Abgrenzung der Leistungen

Ein gerichtliches Verfahren, eine individuelle steuerliche Beratung der Berechtigten oder eine pauschale Prüfung sämtlicher Altzusagen ist nicht eingeschlossen. Wir benötigen vor Vertragsabschluss die vollständigen Leistungsregeln, sämtliche bekannten Sonderzusagen, den Status der Anpassungsprüfungen und Informationen über laufende Streitigkeiten. Der uns bisher übergebene Detailauszug mit 48 Personen ersetzt den vollständigen Bestand nicht.

2 Finanzierung und Preis

{funding} Die in der Vergleichsdatei ausgewiesenen Einrichtungs- und Verwaltungsentgelte betragen {setup:,.0f} EUR einmalig und {annual:,.0f} EUR jährlich. Diese Zahlen sind Nettoplanungsbeträge; die umsatzsteuerliche Behandlung der jeweiligen Leistung ist vor endgültiger Rechnung festzulegen. Kapitalbereitstellung, Einmalentgelt und laufende Kosten sind im Angebotsvergleich getrennt auszuweisen.

2.1 Angebotsvoraussetzungen

Vorausgesetzt werden zutreffende Geburts- und Rentenbeginndaten, vollständige Hinterbliebeneninformationen und die unveränderten beschriebenen Leistungsregeln. Ungeklärte Personen oder fehlende Nachträge werden vor Bindung des Angebots gesondert bewertet. Eine bloße Änderung der Dateibezeichnung von „offen“ auf „bestätigt“ beseitigt keinen Datenvorbehalt.

3 Leistungsverwaltung

Die Zahlungsdatei wird monatlich mit dem freigegebenen Leistungsbestand abgeglichen. Neue Versorgungsfälle und Todesmeldungen werden mit Eingangsdatum und Belegen dokumentiert. Wir führen ein Änderungsprotokoll und stellen Berichte für Geschäftsführung und zuständige Kontrollstellen bereit. Ein abweichender Kontostand ist kein Grund, eine rechtlich geschuldete Rente ohne Freigabe neu festzusetzen.

3.1 Kommunikation

Ein Informationsschreiben an Berechtigte ist vor Versand mit dem Auftraggeber abzustimmen. Es benennt den tatsächlichen Ansprechpartner und den weiterhin maßgeblichen Schuldner. Wir verwenden nicht die Aussage „garantiert haftungsfrei“, solange die konkrete Struktur nicht fachlich geprüft und vollzogen ist. Rückfragen werden nach Datenberichtigung, Leistungsprüfung und rechtlicher Streitfrage unterschieden.

4 Vermögen und Stress

Die von Ihnen genannte Hafenimmobilie ist illiquide. Wir verlangen vor jeder Anrechnung einen aktuellen Titel- und Belastungsnachweis, eine nachvollziehbare Bewertung und Angaben zum Sanierungsbedarf. Eine jährliche Bruttomiete darf nicht ohne Kosten und Leerstandsrisiko als frei verfügbarer Nettozufluss geplant werden. In der Szenarioplanung sind Marktwertänderungen, zusätzliche Rentenzahlungen, Kosten und Liquiditätsreserven getrennt zu zeigen.

5 Umsetzung

Nach vollständigem Dateneingang planen wir zwölf Wochen für Prüfung, Testmigration und Freigabe. Der Beginn der Frist setzt einen geklärten Strukturweg voraus. Eine bereits im Projektkalender vorgesehene Übertragung am 1. April 2027 ist keine Zusage unsererseits. Vor dem produktiven Lauf werden zwei Zahlungsmonate parallel geprüft und sämtliche Differenzen schriftlich freigegeben.

6 Bindung

Dieses Angebot gilt bis zum 30. November 2026 unter den ausdrücklich genannten Daten- und Strukturvorbehalten. Eine Bindung an einen später geänderten Bestand ist damit nicht verbunden. Der vollständige Vertrag wird erst nach Abschluss der Prüfung unterzeichnet. Bitte bestätigen Sie zunächst, welche unserer angebotenen Leistungen Sie weiterverfolgen möchten.

Mit freundlichen Grüßen
Geschäftsleitung {name}''')
doc(r,'11','Immobilie_Wertnotiz.pdf','Hafenhalle 4 – interne Wertannahme','2026-09-30','Immobilienverwaltung Rheinhafen','Treasury', '''1 Objekt

Die Hafenhalle 4 liegt am Kaiweg 18 in Duisburg, Flurstück 428 der projektinternen Objektliste. Sie wird an die Westkai Service GmbH vermietet. Die jährliche Nettokaltmiete beträgt 840.000 EUR. Der Mietvertrag läuft nach dem derzeitigen Verwaltungsstand bis Ende 2031. Betriebskosten, Instandhaltung und Finanzierung sind in dieser Miete nicht enthalten.

2 Wertansatz

Für die interne Projektplanung wurde ein Wert von 14 Mio. EUR angesetzt. Die Zahl beruht auf einer älteren Ertragsbetrachtung und wurde für den Septemberbericht unverändert übernommen. Sie ist weder ein aktuelles Verkehrswertgutachten noch eine Bestätigung eines kurzfristig realisierbaren Verkaufserlöses. Ein Angebot zum Kauf der Halle liegt nicht vor.

3 Noch ausstehende Unterlagen

Die aktuelle Belastungsauskunft, die Dachprüfung und ein Nachtrag zum Mietvertrag wurden angefordert. Die Finanzierungsabteilung soll bestätigen, ob aus einem Verkauf zunächst ein Darlehen abzulösen wäre. Bis dahin sollte der Wertansatz im Finanzierungsmodell als offen bezeichnet werden. Die Sachbearbeitung hat keine Freigabe zur Übertragung des Objekts erteilt.''')
doc(r,'12','Mietvertrag_Hafenhalle.pdf','Gewerbemietvertrag Hafenhalle 4','2021-12-15','Rheinhafen Logistik GmbH','Westkai Service GmbH, Kaiweg 18, 47119 Duisburg', '''1 Mietgegenstand

Die Vermieterin überlässt der Mieterin die Lagerhalle 4 mit 8.400 Quadratmetern Lagerfläche, den zugehörigen Büroflächen und der im Lageplan bezeichneten Rangierfläche am Kaiweg 18 in Duisburg. Die Nutzung ist auf Lagerung, Kommissionierung und zugehörige Verwaltung beschränkt. Gefährliche Stoffe dürfen nur nach vorheriger Zustimmung und Einhaltung der erforderlichen Voraussetzungen eingelagert werden.

2 Laufzeit

Das Mietverhältnis beginnt am 1. Januar 2022 und läuft bis zum 31. Dezember 2031. Eine Verlängerung bedarf schriftlicher Vereinbarung. Die vorzeitige Beendigung aus wichtigem Grund bleibt unberührt. Eine Veräußerung der Halle berechtigt die Mieterin nicht allein zur Einstellung der Mietzahlung.

3 Miete und Betriebskosten

Die monatliche Nettokaltmiete beträgt 70.000 EUR. Die Mieterin zahlt zusätzlich eine Betriebskostenvorauszahlung von 12.000 EUR monatlich; über die tatsächlich umlagefähigen Kosten wird jährlich abgerechnet. Die Nettokaltmiete ist bis zum dritten Bankarbeitstag des Monats zu überweisen. Umsatzsteuer wird nur nach den im konkreten Mietverhältnis geltenden Voraussetzungen zusätzlich berechnet. Eine Verrechnung mit streitigen Gegenforderungen erfolgt nur nach gesonderter Abstimmung oder auf tragfähiger rechtlicher Grundlage.

4 Instandhaltung

Die Vermieterin trägt die Instandhaltung der tragenden Konstruktion und des Dachs. Die Mieterin übernimmt die laufende Wartung ihrer eigenen technischen Einrichtungen und meldet erkennbare Gebäudemängel unverzüglich. Der Mieterin bekannte Feuchtigkeitsschäden werden fotografiert und dem Vermieter mit Ort und Datum übermittelt. Die bloße Entgegennahme einer Meldung ist keine Anerkennung einer bestimmten Schadenshöhe.

5 Baumaßnahmen

Notwendige Arbeiten werden so geplant, dass der Lagerbetrieb möglichst wenig beeinträchtigt wird. Bei erheblichen Einschränkungen stimmen die Parteien einen Ablaufplan ab. Rechte wegen tatsächlicher Gebrauchseinschränkungen bleiben gesondert zu prüfen. Die Vermieterin darf eine notwendige Dachreparatur nicht allein auf den Mieter abwälzen, weil das Objekt später übertragen werden soll.

6 Übergabe und Rückgabe

Der Zustand bei Übergabe wird im gemeinsamen Protokoll festgehalten. Bei Vertragsende gibt die Mieterin die Flächen geräumt zurück. Eigene Einbauten werden nach Vereinbarung entfernt oder übernommen. Offene Betriebskostenabrechnungen bleiben bestehen.

Unterzeichnet am 15. Dezember 2021: Judith Lindkamp für die Rheinhafen Logistik GmbH; Paula van Heek für die Westkai Service GmbH.''')
rcorr=[('13','Rentnerbrief.pdf','Nachfrage zur Meldung „Rentnergesellschaft“','2026-10-21','Hans-Martin Rabe, Hafenblick 14, 47119 Duisburg','Rheinhafen Personalservice','Sehr geehrte Damen und Herren,\n\nich habe 38 Jahre im Hafen gearbeitet und erhalte seit 2015 eine Betriebsrente. Aus der Zeitung habe ich erfahren, dass der Betrieb verkauft werden soll. In einer Betriebsratsinformation steht nun das Wort Rentnergesellschaft. Bitte teilen Sie mir verständlich mit, wer künftig meine Rente schulden soll und ob sich die Anpassung oder die Zahlungstermine ändern.\n\nMeine letzte Mitteilung nennt monatlich 1.460 EUR vor Abzügen. Eine Zustimmung zu einem Wechsel des Schuldners oder einen Verzicht habe ich nicht erklärt. Ich bitte auch um Erklärung, ob die Hafenhalle tatsächlich meine Rente sichern soll. Einen Grundstücksanteil habe ich nie erhalten und könnte damit auch keine laufenden Rechnungen bezahlen.\n\nMit freundlichen Grüßen\nHans-Martin Rabe'),('14','HR_Antwortentwurf.docx','Antwortentwurf Personalservice – noch nicht freigegeben','2026-10-22','Personalservice Rheinhafen','Geschäftsleitung zur Freigabe','Sehr geehrter Herr Rabe,\n\ndie Gesellschaft prüft gegenwärtig verschiedene Wege zur künftigen Organisation und Finanzierung der betrieblichen Altersversorgung. Eine endgültige Strukturentscheidung ist noch nicht getroffen. Ihre bisherigen Rentenzahlungen werden derzeit durch die Rheinhafen Logistik GmbH unverändert fortgeführt.\n\nWir haben Ihre Fragen zum Schuldner, zu Anpassungen und zur Finanzierung aufgenommen. Sobald eine konkrete, fachlich geprüfte Entscheidung vorliegt, werden wir Sie über die für Sie maßgeblichen tatsächlichen Änderungen informieren. Eine Zustimmung oder einen Verzicht erbitten wir mit diesem Schreiben nicht. Die Finanzierung über Vermögenswerte bedeutet nicht, dass Sie statt Ihrer Rente einen Grundstücksanteil erhalten sollen.\n\nBitte wenden Sie sich bis dahin mit Änderungen Ihrer Kontoverbindung oder Anschrift weiterhin an den Personalservice. Dieser Text ist intern zur Freigabe vorgelegt; Versand noch nicht erfolgt.'),('15','CFO_Finanzierung.eml','84 Mio. Vermögen sind nicht 84 Mio. Liquidität','2026-10-22','Judith Lindkamp <cfo@rheinhafen-logistik.example>','Projekt ANKER <projekt@rheinhafen-logistik.example>','Bitte zeigt im Lenkungskreis die 8 Mio. EUR Bankliquidität getrennt von Wertpapieren und Immobilie. Die Halle wird nicht in zwölf gleichen Monatsraten verkauft. Aus der Jahresmiete sind Instandhaltung, Verwaltung und gegebenenfalls Finanzierung zu bedienen.\n\nDer Rahmen von 15 Mio. EUR ist bisher nur ein Entwurf. Er darf nicht zur vorhandenen Ausstattung addiert werden, als läge das Geld schon auf dem Konto. Außerdem muss die Frage geklärt werden, welche Gesellschaft den Rahmen überhaupt abrufen könnte. Für die Variante „operativen Betrieb verkaufen und Pensionen in alter Gesellschaft lassen“ ist der Entwurf noch nicht angepasst.\n\nIch möchte eine einfache Zwölfmonatsrechnung mit Anfangsmitteln, tatsächlich fälligen Renten, Kosten, sicheren Zuflüssen und getrennten Stressannahmen. Ein positiver Barwert allein beantwortet meine Liquiditätsfrage nicht.'),('16','Anbieterfrage.eml','Bitte Angebote auf gleichen Bestand beziehen','2026-10-23','Projekt ANKER <projekt@rheinhafen-logistik.example>','Anbieterkoordination <angebote@anker-projekt.example>','Die drei Angebote unterscheiden sich erheblich im Gegenstand. Bitte bestätigt jeweils, ob lediglich Verwaltung, ein Versicherungsvertrag oder der Anteilserwerb an einer Versorgungsgesellschaft gemeint ist. Kapitalbedarf, Einrichtungskosten und laufende Entgelte sollen getrennt ausgewiesen werden.\n\nAlle Vergleiche müssen denselben Bestand von 1.240 Rentnern und 186 ausgeschiedenen Anwärtern verwenden. Die Datei mit 48 Detailpersonen ist nur ein Ausschnitt zur Prüfung der Datenqualität. Bitte nennt, welche weiteren Unterlagen ihr für ein bindendes Angebot benötigt und welche Anpassungen oder Hinterbliebenenleistungen eure Annahmen enthalten.\n\nWir haben keine allgemeine rechtliche Enthaftung angefragt. Wenn ein Angebot einen bestimmten Übertragungsweg voraussetzt, ist dieser genau zu benennen.'),('17','Board_Protokoll.docx','Lenkungskreis ANKER – keine Freigabe zum Vollzug','2026-10-24','Projektsekretariat','Geschäftsführung und Holding','Der Vorstand diskutiert die drei Angebote. Das Verwaltungsmodell Nordanker erscheint im jährlichen Entgelt günstiger, übernimmt jedoch keine Finanzierung. Rentenfels verlangt einen höheren Einmalbeitrag für den bezeichneten Versicherungsumfang. Hafenruh erwartet eine vorgelagerte Gesellschaftsstruktur und eine bestimmte Anfangsausstattung. Die Preise werden deshalb nicht als unmittelbar vergleichbare Gesamtkosten behandelt.\n\nDie Geschäftsführung stellt fest, dass die 14 Mio. EUR Immobilienansatz noch keine aktuelle Bewertungsgrundlage besitzen. Der Finanzierungsrahmen der Holding ist nicht unterzeichnet. Der Bestandsauszug enthält nicht alle individuellen Zusagetexte. Eine Umsetzung wird deshalb noch nicht freigegeben.\n\nBeschlossen wird die Einholung der Belastungsunterlagen, des Dachberichts und einer vollständigen Erläuterung der Anbieterbedingungen. Die Rentenzahlung bei der bestehenden Gesellschaft läuft unverändert weiter. Das Projektteam legt für den 3. Dezember eine Entscheidungsvorlage vor.'),('18','Verwaltung_Bestand.pdf','Rentenverwaltung – Umfang und Datenqualität','2026-10-23','Rheinhafen Personalservice','Projekt ANKER','Der Gesamtbestand umfasst 1.240 laufende Renten, darunter 180 Hinterbliebenenrenten, sowie 186 unverfallbare Anwartschaften. Die monatliche Bruttorentensumme beträgt 620.000 EUR. Der Detailauszug enthält 48 ausgewählte Fälle und darf nicht mit dem Gesamtbestand gleichgesetzt werden.\n\nBei 17 ausgeschiedenen Anwärtern fehlt die originale Aufnahmebestätigung; die Verwaltung verfügt über Jahresinformationen und Zahlungsverläufe. Bei neun laufenden Renten ist eine besondere Anpassungsklausel aus einer Einzelzusage vermerkt. Diese Fälle sind noch nicht in die allgemeine Anbietertabelle eingeordnet. Die Verwaltung bittet um gesonderte Prüfung vor einer Garantieerklärung zur Vollständigkeit.\n\nEs bestehen derzeit keine gerichtlichen Verfahren in dem übergebenen Projektbestand. Drei Auskunftsanfragen sind offen. Eine technische Null im Feld „Sonderklausel“ bedeutet im alten System „nicht erfasst“, nicht zwingend „nicht vorhanden“.'),('19','Anlagepolitik.pdf','Vorläufige Anlagerichtlinie – Arbeitsstand Treasury','2026-10-24','Rheinhafen Treasury','Geschäftsführung','1 Liquidität\n\nEs soll jederzeit eine Reserve für mindestens sechs Monate der planbaren Renten- und Verwaltungsausgaben verfügbar bleiben. Bei einer Unterschreitung berichtet Treasury am selben Arbeitstag an die Geschäftsführung. Die Reserveschwelle ist ein internes Steuerungsziel und keine rechtliche Aussage zur ausreichenden Gesamtausstattung.\n\n2 Anlagegrenzen\n\nNeue Anlagen sollen sich an erwarteten Zahlungsterminen orientieren. Aktienfonds, langfristige Anleihen und Immobilien sind mit ihren jeweiligen Markt- und Verwertungsrisiken zu erfassen. Die erwartete Rendite darf nicht als garantierter Zufluss verwendet werden.\n\n3 Kontrolle\n\nMarktwerte werden monatlich aktualisiert. Fälligkeiten, laufende Erträge und Veräußerungen werden getrennt ausgewiesen. Bei wesentlichen Abweichungen vom Finanzplan ist ein aktualisierter Zahlungsplan vorzulegen. Eine Änderung der Anlagerichtlinie darf keine eigenständige Kürzung von Versorgungsleistungen auslösen.'),('20','Dachtermin.eml','Hafenhalle – Besichtigung erst nächste Woche','2026-10-25','Immobilienverwaltung <immobilien@rheinhafen-logistik.example>','Treasury <treasury@rheinhafen-logistik.example>','Die Dachbesichtigung ist für den 29. Oktober bestätigt. Der Mieter hat seit August Feuchtigkeit in zwei Lagergassen gemeldet. Bisher wurde provisorisch abgedichtet. Die Rechnungen hierfür sind bezahlt, beantworten aber nicht, ob eine größere Sanierung notwendig ist.\n\nBitte verwendet die frühere Aussage „kein Instandhaltungsbedarf“ nicht weiter. Sie stammt aus dem Zustandsbericht 2021. Der Gutachter soll zunächst den Umfang beschreiben; ein verbindliches Sanierungsangebot ist nicht beauftragt. Eine mögliche Beeinträchtigung des Mietbetriebs muss anschließend mit dem Mieter besprochen werden.'),('21','Projektchat.png','Teams – Angebotspreise im Vergleich','2026-10-25','Projekt ANKER','Projektteam','10:04 | Einkauf – Nordanker kostet nur 98.000 pro Jahr, also viel günstiger?\n\n10:06 | Treasury – Das ist nur Verwaltung. Die 84 Mio. Ausstattung bleiben unsere Aufgabe.\n\n10:08 | HR – Bitte gleiche Leistungen vergleichen, auch Anpassungen und Hinterbliebene.\n\n10:12 | M&A – Und Hafenruh kauft Anteile nach der Strukturierung, nicht automatisch jede Rentenschuld.\n\n10:15 | Projektleitung – Vergleich wird in Umfang, Kapital, Kosten und Voraussetzungen getrennt.')]
for id,file,title,date,sender,recipient,body in rcorr:doc(r,id,file,title,date,sender,recipient,body)
doc(r,'22','Dachbericht.pdf','Hafenhalle 4 – Befund nach Ortsbesichtigung','2026-10-30','Baukontor Ufer GmbH, Werftplatz 3, 47059 Duisburg','Rheinhafen Immobilienverwaltung', '''1 Besichtigung

Die Dachflächen wurden am 29. Oktober 2026 gemeinsam mit der Hausverwaltung und dem Mieter begangen. In zwei Bereichen bestehen Durchfeuchtungen der Dämmung. Die vorläufigen Abdichtungen verhindern nicht sämtliche Wassereintritte. Eine unmittelbare Räumung der gesamten Halle wurde bei der Besichtigung nicht angeordnet; die betroffenen Lagergassen sind jedoch besonders zu überwachen.

2 Maßnahmen

Empfohlen wird eine abschnittsweise Erneuerung der Abdichtung und beschädigter Dämmung. Nach grober Mengenermittlung beträgt der Kostenrahmen 2,2 bis 2,9 Mio. EUR netto. Für die Projektplanung soll vorläufig mit 2,5 Mio. EUR gerechnet werden. Dies ist eine Kostenschätzung und kein verbindliches Angebot eines ausführenden Unternehmens. Eine Ausschreibung und die Koordination mit dem Lagerbetrieb stehen aus.

3 Zeit und Nutzung

Die Arbeiten würden voraussichtlich vier bis sechs Monate dauern. Ob und in welchem Umfang die Nutzung eingeschränkt wird, hängt vom Bauablauf ab. Die vertraglichen Folgen im Mietverhältnis sind nicht Gegenstand dieses technischen Berichts. Vor einer Vermögensübertragung sollte der bekannte Instandhaltungsbedarf in die Bewertung aufgenommen werden.

Dipl.-Ing. Carsten Ufer, Baukontor Ufer GmbH.''',phase='Fortsetzung')
doc(r,'23','Bank_Belastung.pdf','Hafenhalle – Ablösebetrag und Sicherheitenfreigabe','2026-11-02','Niederrhein Handelsbank AG, Uferstraße 32, 47051 Duisburg','Rheinhafen Logistik GmbH', '''Sehr geehrte Frau Lindkamp,

zu Ihrer Anfrage bestätigen wir für das Objekt Hafenhalle 4 eine Darlehensrestschuld von 3.000.000 EUR zum 31. Oktober 2026. Die Forderung wird durch die im Sicherheitenvertrag bezeichnete Grundschuld gesichert. Ein Verkauf oder eine Übertragung des Grundstücks führt nicht ohne weitere Erklärung zur Freigabe unserer Sicherheit.

Für eine Freigabe benötigen wir den vorgesehenen Transaktionsweg und eine abgestimmte Ablösung oder Ersatzsicherung. Der hier genannte Betrag enthält keine Berechnung einer möglicherweise zusätzlich anfallenden Vorfälligkeitsentschädigung und keine Notar- oder Löschungskosten. Eine verbindliche Ablöseabrechnung erstellen wir zum konkreten Vollzugstermin.

Die frühere interne Vermögensliste mit 14 Mio. EUR Objektwert weist die Darlehensposition nicht aus. Diese Liste kann daher nicht als Bestätigung eines lastenfreien Nettovermögenswerts verwendet werden.

Niederrhein Handelsbank AG, Firmenkundenbetreuung.''',phase='Fortsetzung')
doc(r,'24','Mieter_Schreiben.pdf','Feuchtigkeitsschäden – Vorbehalt weiterer Mietrechte','2026-11-03','Westkai Service GmbH','Rheinhafen Logistik GmbH', '''Sehr geehrte Damen und Herren,

in Lagergasse 7 und 8 kommt es weiterhin zu Wassereintritten. Wir haben Waren verlagert und zusätzliche Abdeckungen verwendet. Bitte teilen Sie uns bis zum 13. November mit, wann eine nachhaltige Sanierung beginnt und welche Flächen währenddessen nicht nutzbar sein werden.

Wir behalten uns die Prüfung mietvertraglicher Rechte wegen der Einschränkungen vor. Eine konkrete Minderungsquote haben wir bislang nicht erklärt. Die bisher gezahlte Monatsmiete ist daher kein Beleg dafür, dass alle künftigen Mieten unverändert und ohne Gegenansprüche eingehen werden. Für einen abgestimmten Bauablauf stehen wir zur Verfügung.

Eine Übertragung des Objekts auf eine andere Gesellschaft ändert nichts daran, dass wir einen klaren Ansprechpartner für die Mängelbeseitigung benötigen. Bitte nehmen Sie uns in die Terminplanung auf.

Paula van Heek, Geschäftsführerin.''',phase='Fortsetzung')
doc(r,'25','Hafenruh_Nachtrag.eml','Immobilie wird vorerst nicht als Anfangsausstattung anerkannt','2026-11-05','Hafenruh <angebote@hafenruh.example>','Projekt ANKER <projekt@rheinhafen-logistik.example>', '''Sehr geehrte Damen und Herren,

nach Durchsicht des Dachberichts und der Bankmitteilung rechnen wir die Hafenhalle derzeit nicht mit 14 Mio. EUR in die geforderte Anfangsausstattung ein. Bitte liefern Sie einen aktualisierten Nettoansatz einschließlich Finanzierung, Sanierung und Verwertungskosten. Bis dahin erwarten wir liquide Ersatzmittel oder eine neu zu verhandelnde Struktur.

Unser Angebot über 94,5 Mio. EUR Mindestanfangsausstattung ist keine Zusage, einen nicht werthaltig geprüften Sachwert zum früheren Buch- oder Planwert zu übernehmen. Auch die angekündigte Holding-Unterstützung ist bislang nicht unterzeichnet und ersetzt nach unserem Angebot keine Anfangsausstattung.

Bitte berücksichtigen Sie diese Punkte in der Entscheidungsvorlage. Eine Bindung an den bisher angesetzten 14-Mio.-Wert besteht nicht. Das übrige Angebot bleibt unter seinen Daten- und Strukturvorbehalten bestehen.''',phase='Fortsetzung',attachments=['Fortsetzung/22_Dachbericht.pdf','Fortsetzung/23_Bank_Belastung.pdf'])
workbook(r,'26','Finanzierung_und_Stress.xlsx','Finanzierung und zwölfmonatige Zahlungsplanung',[{'name':'Ausstattung','columns':['Vermoegen','Ursprungsansatz_EUR','Korrektur_EUR','Rechenansatz_EUR'],'rows':[['Bank',8000000,0,'=B6-C6'],['Anleihen',50000000,0,'=B7-C7'],['Aktienfonds',12000000,0,'=B8-C8'],['Hafenhalle',14000000,0,'=B9-C9'],['Gesamt','=SUM(B6:B9)','=SUM(C6:C9)','=SUM(D6:D9)']],'formats':{x:'currency' for x in ['Ursprungsansatz_EUR','Korrektur_EUR','Rechenansatz_EUR']}},{'name':'Liquiditaet','columns':['Monat','Anfang_EUR','Miete_brutto_EUR','Renten_EUR','Verwaltung_EUR','Objektkosten_EUR','Ende_EUR'],'rows':[[f'2027-{i:02}',8000000 if i==1 else f'=G{i+4}',70000,620000,round(98000/12,2),20000,f'=B{i+5}+C{i+5}-D{i+5}-E{i+5}-F{i+5}'] for i in range(1,13)],'formats':{x:'currency' for x in ['Anfang_EUR','Miete_brutto_EUR','Renten_EUR','Verwaltung_EUR','Objektkosten_EUR','Ende_EUR']}},{'name':'Stressparameter','columns':['Parameter','Annahme','Abgrenzung'],'rows':[['Aktienmarkt',-.25,'Wertänderung; keine automatische Zahlung'],['Anleihenmarkt',-.08,'Wertänderung; keine automatische Zahlung'],['Rentenanstieg',.03,'Planstress; keine Rechtsentscheidung'],['Mietausfall',3,'Monate; Szenario keine bereits erklärte Minderung'],['Holdingrahmen',15000000,'Entwurf; kein sicherer Zufluss']]}])
r['workbooks'][-1]['controls']=[{'sheet':'Ausstattung','cell':'D10','expected':84000000},{'sheet':'Liquiditaet','cell':'G17','expected':1062000.04}]
workbook(r,'27','Angebotsvergleich.xlsx','Drei individuelle Angebote – unterschiedliche Leistungsumfänge',[{'name':'Angebote','columns':['Anbieter','Gegenstand','Kapitalansatz_EUR','Einrichtung_EUR','Jaehrlich_EUR','Bisheriger_Schuldner'],'rows':[[p[1],p[7],p[4],p[5],p[6],'keine automatische Freistellung'] for p in providers],'formats':{'Kapitalansatz_EUR':'currency','Einrichtung_EUR':'currency','Jaehrlich_EUR':'currency'}},{'name':'Bestand','columns':['Status','Personen','Monatsrente_EUR','Planungswert_EUR'],'rows':[['Alters- und Invaliditätsrenten',1060,560000,71600000],['Hinterbliebene',180,60000,6800000],['Unverfallbar ausgeschieden',186,0,8000000],['Gesamt','=SUM(B6:B8)','=SUM(C6:C8)','=SUM(D6:D8)']],'formats':{'Monatsrente_EUR':'currency','Planungswert_EUR':'currency'}}])
r['workbooks'][-1]['controls']=[{'sheet':'Bestand','cell':'B9','expected':1426},{'sheet':'Bestand','cell':'C9','expected':620000},{'sheet':'Bestand','cell':'D9','expected':86400000}]
csvdoc(r,'28','Detailbestand_48.csv','Ausgewählter Detailbestand – keine vollständige Rentnerliste',['Person','Status','Geburtsjahr','Rentenbeginn','Monatsrente_EUR','Zusagestand'],[[f'A-{i:04}','Altersrente' if i<=36 else 'Hinterbliebenenrente' if i<=42 else 'Anwartschaft',1945+i%15,'2015-07-01' if i<=42 else '',round(340+i*17.5,2) if i<=42 else 0,'1994; individuelle Belege prüfen'] for i in range(1,49)])
csvdoc(r,'29','Zahlungslauf_September.csv','Bankfreigabe Rentenzahlung September',['Lauf','Datum','Empfaengeranzahl','Brutto_EUR','Status'],[['RH-2026-09','2026-09-30',1240,620000,'ausgeführt'],['RH-2026-10','2026-10-30',1240,620000,'Vorbereitung; noch nicht ausgeführt']])
workbook(r,'30','Immobilie_Nachlieferung.xlsx','Immobilienansatz nach neuen Unterlagen',[{'name':'Nettoansatz','columns':['Position','EUR','Beleg'],'rows':[['Alter Ansatz',14000000,'interne Wertnotiz'],['Darlehensablösung',-3000000,'Bankmitteilung02.11.'],['Sanierung Planung',-2500000,'Dachbericht30.10.'],['Zwischensumme','=SUM(B6:B8)','ohne Verkaufskosten; kein Verkehrswert'],['Liquiditaet',0,'Kein Verkauf und kein freier Geldzufluss erfolgt']],'formats':{'EUR':'currency'}}],phase='Fortsetzung')
r['workbooks'][-1]['controls']=[{'sheet':'Nettoansatz','cell':'B9','expected':8500000}]
presentation(r,'31','ANKER – Rentnergesellschaft verstehen',[('Zwei Strukturwege',['Verpflichtungen ausgliedern','Operatives Geschäft verkaufen, Pensionen verbleiben','Gleicher Projektname bedeutet unterschiedliche Rechtsfragen']),('Drei Angebote',['Nordanker: Verwaltung','Rentenfels: Versicherung','Hafenruh: Erwerb ausgestatteter Gesellschaft']),('Finanzierung getrennt zeigen',['84 Mio. EUR bisheriger Vermögensansatz','8 Mio. EUR davon unmittelbar liquide','15 Mio. EUR Holdingrahmen noch Entwurf']),('Entscheidung vorbereiten',['Immobilie prüfen, Bestand vervollständigen','Stress und Fälligkeiten rechnen','Keine automatische Enthaftung versprechen'])])
doc(r,'32','Datenraum_Ansicht.png','Datenraum ANKER – offene Bestandteile','2026-10-25','Projektsekretariat','Projektteam','''Bestand 1.426 Personen – Gesamtzählung vorhanden

48 Detailfälle – ausgewählte Stichprobe

17 Aufnahmebestätigungen – Suche offen

Hafenhalle – Dachprüfung am 29.10.

Holdingrahmen – nicht unterschrieben

Drei Angebote – verschiedene Leistungsmodelle''')
doc(r,'33','Verguetung.pdf','Vergütungsvereinbarung Projekt ANKER','2026-10-15',CONTACT,r['client'],'''Die Parteien vereinbaren für die außergerichtliche Sichtungs- und Strukturierungsphase eine Vergütung nach Zeitaufwand. Partnerstunden werden mit 420 EUR netto, anwaltliche Mitarbeit mit 290 EUR netto berechnet. Zeiteinheiten betragen sechs Minuten entsprechend tatsächlichem Aufwand. Umsatzsteuer wird zusätzlich in gesetzlicher Höhe ausgewiesen.

Das Planungsbudget beträgt 95.000 EUR netto. Vor absehbarer Überschreitung um mehr als zehn Prozent informiert die Kanzlei die Mandantin und stimmt weitere nicht eilbedürftige Arbeiten ab. Monatliche Rechnungen enthalten Bearbeiter, Datum, Tätigkeit und Dauer. Allgemeine Bürokosten sind enthalten. Externe Bewertungen und Transaktionskosten werden nur nach eigener Freigabe beauftragt.

Ein Kostenerstattungsanspruch gegen Dritte deckt regelmäßig höchstens die gesetzlich erstattungsfähige Vergütung. Die vereinbarte Vergütung kann darüber hinausgehen und insoweit von der Mandantin selbst zu tragen sein. Rechnungen sind binnen21 Kalendertagen nach Zugang fällig. Ein gerichtlicher Vertretungsauftrag ist nicht eingeschlossen.

Unterzeichnet am15.Oktober2026: Judith Lindkamp für die Holding und Dr.Nora Treuenfels für die Kanzlei.''')
doc(r,'34','Bankkonto_Bestaetigung.pdf','Treuhandfreie Bankliquidität – Saldenmitteilung','2026-09-30','Niederrhein Handelsbank AG, Uferstraße 32, 47051 Duisburg','Rheinhafen Logistik GmbH', '''Sehr geehrte Damen und Herren,

für das in Ihrer Projektplanung bezeichnete Geschäftskonto bestätigen wir zum 30. September einen Habensaldo von 8.000.000 EUR. Die Bestätigung bezieht sich ausschließlich auf diesen Kontostand. Sie bestätigt weder den Wert der Depotanlagen noch die ausreichende Ausstattung einer künftigen Versorgungsgesellschaft.

Über eine Übertragung des Kontos auf eine andere juristische Person wurde noch keine Vereinbarung geschlossen. Hierfür benötigen wir die konkrete Struktur, Vertretungsnachweise und erforderliche Kontoeröffnungsunterlagen. Die Verfügbarkeit des Guthabens ist von den sonstigen Vertrags- und Sicherheitenverhältnissen zu unterscheiden.

Die mit der Hafenhalle verbundene Darlehensverbindlichkeit wird gesondert geführt. Bitte rechnen Sie einen Immobilienwert nicht ohne Prüfung der dazugehörigen Finanzierung als lastenfreies Vermögen hinzu. Eine konkrete Ablöseabrechnung wird auf Anforderung zum gewünschten Stichtag erstellt.''')
doc(r,'35','Weitere_Aufklaerung.eml','Vor Entscheidung: neun Sonderklauseln und Anpassungskosten','2026-11-06','Personalservice <pensionen@rheinhafen-logistik.example>','Dr. Nora Treuenfels <mail@monki-treuenfels.example>', '''Sehr geehrte Frau Dr. Treuenfels,

wir haben bei den neun im Register vermerkten Sonderfällen weitere Jahresinformationen gefunden. Die zugrunde liegenden individuellen Vertragsseiten sind noch nicht vollständig digitalisiert. Bitte behandeln Sie deshalb die allgemeine Rentensteigerung von3 Prozent im Stressblatt nicht als abschließende Abbildung aller rechtlichen Anpassungspflichten.

Die Anbieter haben bislang den Standardbestand bewertet. Wir bitten darum, die offenen Sonderzusagen als konkrete Bedingung für die nächste Angebotsrunde aufzunehmen. Für die Vorstandssitzung benötigen wir eine verständliche Erläuterung, welche Entscheidung auf Grundlage der vorhandenen Unterlagen schon möglich ist und welche erst nach Nachlieferung getroffen werden kann.

Die reguläre Rentenzahlung ist sichergestellt. Eine neue Leistungsfestsetzung oder Kündigung des Verwaltungsbestands wurde nicht veranlasst.''',phase='Fortsetzung')
for d in r['documents']:
 d['body']=[p.replace('180,000 EUR','180.000 EUR').replace('98,000 EUR','98.000 EUR').replace('240,000 EUR','240.000 EUR').replace('350,000 EUR','350.000 EUR').replace('120,000 EUR','120.000 EUR').replace('binnen21','binnen 21').replace('am15.Oktober2026','am 15. Oktober 2026').replace('Dr.Nora','Dr. Nora').replace('von3 Prozent','von 3 Prozent') for p in d['body']]
r['controls']={'pensioners':1240,'deferred':186,'population_total':1426,'selected_persons':48,'monthly_pensions_eur':620000,'annual_pensions_eur':7440000,'plan_obligation_eur':86400000,'initial_assets_eur':84000000,'cash_eur':8000000,'property_old_eur':14000000,'property_debt_eur':3000000,'property_repair_eur':2500000,'property_arithmetic_net_eur':8500000,'holding_frame_uncommitted_eur':15000000,'chronology':'Grundakte bis25.10.2026; Fortsetzung ab30.10.2026.'}
save(r)
r['workbooks'][0]['controls'][1]['expected']=1061999.96
save(r)
# 4 PENSIONSKASSE
p=case('bav-pensionskasse-niederrhein-verbund','Kürzung bei der Kasse – wer zahlt die Differenz im Niederrhein-Verbund?','Niederrhein Industrieverbund AG','Krefeld','Der Niederrhein-Verbund finanziert betriebliche Altersversorgung über die Rheinwiese Pensionskasse. Seit September 2026 zahlt die Kasse niedrigere garantierte Renten und geringere nicht garantierte Überschüsse. 680 Rentner aus drei Zusagekohorten sind betroffen; daneben bestehen 1.460 aktive und 320 ausgeschiedene Anwartschaften. HR hat die Kürzungen zunächst als reine Kassenangelegenheit behandelt. Nun verlangt eine frühere Mitarbeiterin die Differenz, während Treasury sowohl laufende Ausgleichszahlungen als auch zusätzliche Finanzierung der Kasse planen soll.','Ordnen Sie Kassenleistung, Arbeitgeberzusage, garantierte Leistung, Überschuss und Anpassung je Kohorte zu. Bereiten Sie die sachliche Aufklärung, eine verständliche Entscheidungsvorlage, Liquiditätsrechnung und die notwendigen Antwort- und Vertragsentwürfe vor. Eine Klage oder fertige rechtliche Musterlösung ist nicht enthalten.')
mandate(p,'niederrhein-verbund','2026-10-19','4. Dezember 2026');engagement(p,'rheinwiese','2026-10-20','90.000')
source_policy(p,'03','Gesamtzusage_1992.pdf','1992-06-01','Versorgungszusage Niederrhein 1992','Niederrhein Industrieverbund AG','Diese Zusage gilt für die im Aufnahmeverzeichnis erfassten Beschäftigten der AG nach schriftlicher Bestätigung.','Die jährliche Altersrente beträgt 0,35 Prozent des letzten jährlichen Festgehalts für jedes volle anrechenbare Dienstjahr, höchstens für 35 Jahre. Der Arbeitgeber sagt diese Leistung zu und verwendet die Leistungen der Rheinwiese Pensionskasse zu ihrer Erfüllung. Nicht garantierte Überschüsse der Kasse werden zusätzlich ausgezahlt, soweit sie tatsächlich zugeteilt werden; eine feste Überschusshöhe wird hierdurch nicht versprochen.','Die Durchführung erfolgt über Beiträge an die Rheinwiese Pensionskasse. Der Arbeitgeber und die Kasse führen getrennte Unterlagen über Zusage und Versicherungsleistung.')
p['documents'][-1]['body']=[b.replace('dauernder voller Erwerbsminderung','dauernder Erwerbsunfähigkeit') for b in p['documents'][-1]['body']]
source_policy(p,'04','Gesamtzusage_2001.pdf','2001-01-01','Niederrhein Versorgung 2001 – Beitragsbausteine','Niederrhein Komponenten GmbH','Diese Ordnung erfasst die von der Komponenten GmbH ab dem 1. Januar 2001 aufgenommenen Beschäftigten.','Der Arbeitgeber stellt jährlich 3 Prozent des pensionsfähigen Festgehalts als Beitrag bereit. Die aus jedem Beitragsjahr entstehende garantierte Leistung wird nach der vereinbarten Leistungstabelle in einer Jahresmitteilung dokumentiert. Bereits garantierte Bausteine werden als eigener Bestand ausgewiesen. Nicht garantierte Überschussprojektionen sind von der zugesagten Leistung getrennt darzustellen.','Die Beiträge werden an die Rheinwiese Pensionskasse gezahlt. Eine technische Änderung der Kassenverwaltung ersetzt keine Änderung der arbeitsrechtlichen Zusage.')
doc(p,'05','Einzelzusage_Seidel_1998.pdf','Versorgungsbestätigung für Claudia Seidel','1998-09-01','Niederrhein Service GmbH','Claudia Seidel, Personalnummer N-0001', '''Sehr geehrte Frau Seidel,

wir bestätigen Ihre Aufnahme in die betriebliche Altersversorgung unseres Hauses zum1.September1998. Für Ihre Versorgung werden Beiträge an die Rheinwiese Pensionskasse abgeführt. Die daraus nach den bei Aufnahme vereinbarten Tarifen garantierte Leistung wird Ihnen als betriebliche Versorgungsleistung zugesagt. Die jeweilige Jahresinformation weist die garantierte Rente und nicht garantierte Überschussanteile getrennt aus.

Bei Eintritt des Versorgungsfalls erteilen wir Ihnen eine Bestätigung der zugesagten Leistung auf der Grundlage der erfassten Beiträge und Vertragsunterlagen. Zusätzlich von der Kasse tatsächlich zugeteilte Überschüsse werden an Sie weitergegeben. Eine feste Höhe künftiger Überschüsse garantieren wir nicht. Abweichende individuelle Abreden bedürfen einer schriftlichen Bestätigung.

Bereits erteilte Zusagen werden nicht allein dadurch geändert, dass die Kasse ihre Satzung oder Verwaltungssoftware ändert. Bei einem Wechsel des Arbeitgebers sind die vorhandenen Rechte und die hierfür erforderlichen Erklärungen gesondert festzuhalten. Sie erhalten diese Bestätigung zusammen mit den bei Aufnahme geltenden Versicherungsbedingungen.

Unterzeichnet: Dr. Leonhard Mertens, Geschäftsführer der Niederrhein Service GmbH. Empfang bestätigt: Claudia Seidel.''')
doc(p,'06','Satzung_Rheinwiese.pdf','Satzung Rheinwiese Pensionskasse – für den Bestand maßgebliche Fassung','2020-07-01','Rheinwiese Pensionskasse VVaG, Kassenweg 6, 47829 Krefeld','Mitgliedsunternehmen und Versicherte', '''1 Zweck und Mitgliedschaft

Die Kasse führt die in ihren Tarifen bezeichnete betriebliche Altersversorgung für Beschäftigte ihrer Mitgliedsunternehmen durch. Aufnahme, Beiträge und Leistungsumfang richten sich nach Satzung, Tarif und individueller Versicherungsbestätigung. Die Mitgliedschaft eines Arbeitgebers allein beantwortet nicht, welche arbeitsrechtliche Zusage er seinen Beschäftigten erteilt hat.

2 Organe

Organe sind die Mitgliederversammlung, der Vorstand und der Aufsichtsrat. Der Vorstand führt die laufenden Geschäfte und erstellt die erforderlichen Berichte. Der Aufsichtsrat überwacht die Geschäftsführung. Satzungsänderungen und grundlegende Maßnahmen werden nach den in der Einladung bezeichneten Gegenständen beschlossen und dokumentiert. Eine Pressemitteilung ersetzt keine Beschlussausfertigung.

3 Beiträge und Bestandsführung

Die Beiträge sind zu den im Tarif bestimmten Terminen zu zahlen. Der Arbeitgeber meldet die versicherten Personen und die erforderlichen Entgeltdaten. Fehlerhafte oder unvollständige Meldungen werden mit Herkunft, Datum und Korrekturgrund festgehalten. Beiträge, die keiner Person zugeordnet werden können, werden nicht ohne Prüfung zur Finanzierung anderer individueller Verträge verwendet.

4 Versicherungsleistungen

Die Kasse erbringt die im jeweiligen Vertrag garantierten Leistungen und die nach den hierfür geltenden Voraussetzungen zugeteilten Überschüsse. Garantierte und nicht garantierte Bestandteile werden in der Mitteilung erkennbar getrennt. Eine Vorausberechnung künftiger Überschüsse ist keine selbstständige Garantie. Der Eintritt des Leistungsfalls ist durch die vereinbarten Nachweise zu belegen.

5 Rechnungslegung und Sicherung

Der Vorstand stellt die erforderlichen versicherungstechnischen Berechnungen und Vermögensnachweise auf. Die Kapitalanlage ist am dauerhaften Leistungszweck auszurichten. Die Verwendung von Sicherungsmitteln, der Umgang mit Fehlbeträgen und etwaige aufsichtsrechtliche Maßnahmen richten sich nach den jeweils geltenden Anforderungen. Eine betriebswirtschaftliche Planung wird nicht als behördliche Genehmigung bezeichnet.

6 Behandlung eines Fehlbetrags

Stellt die fachliche Bewertung einen Fehlbetrag fest, legt der Vorstand der Mitgliederversammlung einen Maßnahmenplan vor. Er enthält Ursache, betroffenen Tarifbestand, mögliche zusätzliche Finanzierung, Auswirkungen auf garantierte Leistungen und Überschüsse sowie die erforderlichen aufsichtsrechtlichen Schritte. Eine Kürzung darf nicht allein durch Buchung im Auszahlungssystem eingeführt werden. Vor Umsetzung müssen die einschlägigen satzungsmäßigen und gesetzlichen Voraussetzungen geprüft und die erforderlichen Entscheidungen und Genehmigungen dokumentiert sein.

6.1 Mitteilung an Berechtigte

Die Kasse bezeichnet die konkrete Maßnahme, den betroffenen Vertragsbestand, den Zeitpunkt, die bisherige und künftige Leistung sowie die Grundlage der Entscheidung. Eine Änderung der Leistung der Kasse wird nicht zugleich als abschließende Feststellung sämtlicher Ansprüche gegen den Arbeitgeber ausgegeben. Anfragen zu einer darüber hinausgehenden arbeitsrechtlichen Zusage werden mit den betroffenen Arbeitgebern abgegrenzt.

7 Überschüsse

Die Überschussverwendung erfolgt nach dem jeweiligen Tarif und den beschlossenen Zuteilungsregeln. Für laufende Renten ist auszuweisen, welche Überschüsse dem jeweiligen Rentnerbestand zugeordnet werden und wie sie verwendet werden. Ein Gesamtbetrag über alle Tarife genügt nicht als Nachweis der Verwendung im einzelnen Tarif. Eine Senkung nicht garantierter künftiger Zuteilungen wird getrennt von einer Änderung garantierter Leistungen erläutert.

8 Unternehmensveränderungen

Ein Ausscheiden eines Mitgliedsunternehmens oder eine Unternehmensübertragung führt nicht ohne weitere Prüfung zum Erlöschen vorhandener Versicherungsrechte. Vor einer Bestandsübertragung werden die betroffenen Verträge, notwendigen Erklärungen und Aufsichtsvoraussetzungen ermittelt. Die Kasse stellt die hierfür erforderlichen Bestandsunterlagen bereit.

9 Schlussbestimmungen

Diese Fassung gilt ab dem1.Juli2020. Spätere Änderungen werden mit Beschlussdatum und Wirksamkeitsvoraussetzungen gesondert dokumentiert. Individuelle Vertragsbestätigungen und Tarifbedingungen bleiben Teil der vollständigen Versicherungsunterlagen. Ausfertigung: Vorstand und Aufsichtsratsvorsitz der Rheinwiese Pensionskasse.''')
doc(p,'07','Kasse_Kuerzungsmitteilung.pdf','Leistungsmitteilung September2026 – Kürzung und Überschussänderung','2026-08-12','Rheinwiese Pensionskasse VVaG, Kassenweg 6, 47829 Krefeld','Mitgliedsunternehmen Niederrhein-Verbund', '''Sehr geehrte Damen und Herren,

wir teilen mit, dass wir die garantierten laufenden Renten im bezeichneten Altbestand ab1.September2026 um6 Prozent vermindern. Daneben werden die laufenden nicht garantierten Überschusszahlungen nach den beigefügten Tarifgruppen reduziert. Der Vorstand stützt die Maßnahme auf den Maßnahmenbeschluss der Mitgliederversammlung vom30.Juni2026 und die Satzungsbestimmung zur Behandlung eines Fehlbetrags.

Für den von Ihnen gemeldeten Gesamtbestand von680 laufenden Renten beträgt die bisherige garantierte Monatsleistung300.000EUR. Nach der Kürzung werden282.000EUR gezahlt. Die nicht garantierten monatlichen Überschüsse sinken nach der aktuellen Bestandsberechnung von60.000EUR auf55.000EUR. Die Gesamtzahlung beträgt damit337.000EUR statt360.000EUR.

Die betroffenen Personen erhalten individuelle Mitteilungen mit den bisherigen und neuen Bestandteilen. Eine Aussage zu einem zusätzlichen Anspruch aus einer Arbeitgeberzusage treffen wir hiermit nicht. Die Mitgliedsunternehmen sollen die arbeitsrechtlichen Auswirkungen in eigener Zuständigkeit prüfen.

Die vollständige Beschlussausfertigung, die Berechnungsgrundlagen und die aufsichtsrechtlichen Unterlagen werden über unser Mitgliederportal bereitgestellt. In Ihrem derzeitigen Downloadpaket sind noch nicht alle Dokumente enthalten. Bitte richten Sie Rückfragen an das Bestandsmanagement; wir stellen fehlende Ausfertigungen auf konkrete Anforderung bereit.

Dr. Vera Hain, Vorstand.''')
doc(p,'08','Seidel_Leistungsmitteilung.pdf','Claudia Seidel – individuelle Rentenmitteilung','2026-08-17','Rheinwiese Pensionskasse VVaG','Claudia Seidel, Kastanienweg 11, 47803 Krefeld', '''Sehr geehrte Frau Seidel,

Ihre monatliche garantierte Rente beträgt bisher1.200,00EUR. AbSeptember2026 zahlen wir hierauf1.128,00EUR. Die Verringerung beträgt72,00EUR beziehungsweise6 Prozent. Zusätzlich erhalten Sie künftig40,00EUR nicht garantierten Überschuss statt bisher60,00EUR. Die Gesamtzahlung sinkt somit von1.260,00EUR auf1.168,00EUR monatlich.

Die garantierte Leistung und der Überschuss sind getrennte Bestandteile. Die Überschusszahlung ist nach unseren Vertragsunterlagen nicht in unveränderlicher Höhe garantiert. Die Änderung beruht auf der vom Vorstand umgesetzten Maßnahme im bezeichneten Bestand. Die zugrunde liegenden Unterlagen können über das Bestandsmanagement angefordert werden.

Diese Mitteilung betrifft unsere Zahlung als Pensionskasse. Ob Ihr früherer Arbeitgeber aufgrund seiner Zusage zusätzliche Leistungen schuldet, entscheiden wir hiermit nicht. Bitte wenden Sie sich wegen der Arbeitgeberzusage auch an die Niederrhein Service GmbH. Für eine Erklärung unserer Berechnung stehen wir Ihnen zur Verfügung.

Rheinwiese Pensionskasse, Leistungsservice.''')
doc(p,'09','Rentenbescheid_Arbeitgeber_2021.pdf','Versorgungsbestätigung bei Rentenbeginn – Claudia Seidel','2021-06-18','Niederrhein Service GmbH','Claudia Seidel', '''Sehr geehrte Frau Seidel,

zum Beginn Ihrer Altersversorgung am1.Juli2021 bestätigen wir auf Grundlage Ihrer Zusage vom1.September1998 die monatliche garantierte Betriebsrente von1.200,00EUR. Die Auszahlung erfolgt derzeit durch die Rheinwiese Pensionskasse. Der nach heutigem Stand zusätzlich zugeteilte Überschuss beträgt60,00EUR monatlich. Dieser zusätzliche Anteil wird gesondert als nicht garantiert ausgewiesen.

Die laufende Gesamtzahlung beträgt bei Rentenbeginn1.260,00EUR vor etwaigen gesetzlich vorzunehmenden Abzügen. Über die Entwicklung der Leistung und erforderliche Anpassungsfragen informieren wir Sie gesondert. Mit der Auszahlung durch die Kasse ist keine besondere Verzichtserklärung Ihrerseits verbunden. Bitte teilen Sie Änderungen Ihrer Anschrift und Kontoverbindung dem Leistungsservice mit.

Diese Bestätigung beruht auf den erfassten Beiträgen und dem bei Rentenbeginn geltenden Vertragsstand. Falls Sie abweichende individuelle Vereinbarungen besitzen, senden Sie uns bitte eine Kopie zur Prüfung.

Dr. Leonhard Mertens, Geschäftsführer.''')
doc(p,'10','HR_Erste_Rundmail.eml','Kassenmitteilung – zunächst keine manuelle Ausgleichsbuchung','2026-08-19','HR Shared Service <hr@niederrhein-verbund.example>','Payroll <payroll@niederrhein-verbund.example>', '''Guten Morgen,

die Kasse hat eine allgemeine Kürzung mitgeteilt. Bitte bucht zunächst keinen automatischen Arbeitgeberausgleich für den gesamten Bestand, weil wir die einzelnen Zusagen und Bestandteile noch nicht abgeglichen haben. Die Zahlungen der Kasse werden abSeptember nach deren Datei übernommen. Ich hatte im Gespräch gestern gesagt, dies sei „nur ein Problem der Kasse“. Diese Einschätzung ist nicht rechtlich geprüft.

Wir benötigen von den drei Gesellschaften die ursprünglichen Arbeitgeberzusagen und die letzten Leistungsbestätigungen. Besonders die garantierte Leistung und die Überschüsse müssen auseinandergehalten werden. Bitte schließt individuelle Beschwerden nicht mit einem Standardtext ab. Leitet sie an die Projektgruppe weiter und haltet Eingang und Antwortfrist fest.

Viele Grüße
Anne Brück, HR Shared Service''')
doc(p,'11','Seidel_Anforderung.pdf','Bitte um Ausgleich und Erläuterung der Rentenkürzung','2026-10-16','Claudia Seidel, Kastanienweg 11, 47803 Krefeld','Niederrhein Service GmbH', '''Sehr geehrte Damen und Herren,

seitSeptember erhalte ich92EUR weniger im Monat. Im Jahr2021 hat mir Ihr Unternehmen die garantierte Rente von1.200EUR bestätigt. Die Kasse zahlt hiervon nun nur1.128EUR. Bitte teilen Sie mir mit, ob Sie die fehlenden72EUR übernehmen und wie die weiteren20EUR beim Überschuss zu behandeln sind. Ich möchte keine allgemeine Antwort, dass ich mich nur an die Kasse wenden soll.

Außerdem habe ich seitRenteneintritt keine verständliche Mitteilung darüber erhalten, ob und wann eine Anpassung geprüft wurde. In den Jahresbriefen stehen lediglich neue Überschusswerte. Bitte senden Sie mir die für mich maßgeblichen Unterlagen und erklären Sie, ob damit die Anpassungsfrage erledigt sein soll.

Ich bitte bis6.November2026 um eine konkrete Antwort. Eine Klage habe ich nicht erhoben. Ich füge die ursprüngliche Zusage, Ihre Rentenbestätigung und die aktuelle Kassenmitteilung bei.

Mit freundlichen Grüßen
Claudia Seidel''')
doc(p,'12','Seidel_Email.eml','Unterlagen zu meinem Schreiben vom16.Oktober','2026-10-19','Claudia Seidel <claudia.seidel@example.example>','Personalservice <pensionen@niederrhein-verbund.example>', '''Sehr geehrte Frau Brück,

hier kommen die drei Unterlagen aus meinem Schreiben nochmals elektronisch. Mir geht es zunächst darum, wer die fehlenden Beträge zahlen muss und ob meine damalige Zusage weiterhin gilt. Ich habe von einer Kollegin gehört, dass die AG andere Briefe verschickt hat als die Service GmbH. Bitte verwenden Sie deshalb nicht einfach deren Standardantwort für meinen Fall.

Die Kasse hat auf meinem Konto imSeptember undOktober jeweils1.168EUR vor den in der Abrechnung genannten Abzügen ausgewiesen. Ich habe keine Zustimmung zur Kürzung unterschrieben. Bitte bestätigen Sie den Eingang. Für ein Gespräch bin ich amDienstagvormittag erreichbar; die Bearbeitung darf aber nicht daran scheitern, dass ich nicht sofort ansTelefon gehe.

Mit freundlichen Grüßen
Claudia Seidel''',attachments=['Grundakte/05_Einzelzusage_Seidel_1998.pdf','Grundakte/08_Seidel_Leistungsmitteilung.pdf','Grundakte/09_Rentenbescheid_Arbeitgeber_2021.pdf'])
doc(p,'13','Anpassungsprotokoll_2024.pdf','Sitzungsvermerk Personal und Treasury – Anpassungsrunde2024','2024-07-03','Niederrhein Service GmbH','Geschäftsführung', '''1 Beratungsgegenstand

Die Personalabteilung stellt die im Jahr2021 begonnenen Renten vor. Für Claudia Seidel ist der Rentenbeginn1.Juli2021 erfasst. Ein aktueller Tarifnachweis zur Überschussverwendung liegt in der Sitzung nicht vor. Die vorgelegte Kassenübersicht weist nur eine Gesamtsumme über verschiedene Tarife aus.

2 Bisherige Behandlung

Treasury schlägt vor, keine zusätzliche Arbeitgeberzahlung einzuplanen, weil die Kasse Überschüsse ausschütte. HR fragt, ob dies für alle Zusagen und Verträge genüge. Eine abschließende rechtliche Prüfung erfolgt in der Sitzung nicht. Es wird vereinbart, die Tarifbedingungen und die tatsächliche Verwendung der Überschüsse nachzufordern.

3 Offene Erledigung

Die Nachforderung soll durch Anne Brück erfolgen. Ein endgültiger Beschluss über den einzelnen Anspruch von Frau Seidel wird nicht gefasst. Im Protokoll ist keine an die Betroffenen versandte individuelle Anpassungsentscheidung dokumentiert. Der nächste Termin wird aufOktober2024 verschoben. Der Vermerk bleibt als offener Vorgang in der Personalakte.''')
doc(p,'14','Kassentarif_2010.pdf','Tarifbedingungen Rheinwiese – Überschusszuordnung','2010-01-01','Rheinwiese Pensionskasse VVaG','Mitgliedsunternehmen', '''1 Garantierte Leistung

Die garantierte Leistung richtet sich nach den für die Beiträge vereinbarten Tarifgrundlagen und der individuellen Versicherungsbestätigung. Sie wird im Jahresausweis getrennt von nicht garantierten Zusatzleistungen dargestellt. Eine Projektion des Gesamtertrags begründet keine Garantie eines bestimmten zukünftigen Überschussbetrags.

2 Überschusszuweisung

Die Kasse bildet nach den geltenden Rechnungsgrundlagen Überschussgruppen für die bezeichneten Tarife. Der Vorstand beschließt die Zuteilung nach Maßgabe der Satzung und der hierfür geltenden Voraussetzungen. Die Zuteilungsmitteilung bezeichnet das Jahr, den Tarif und die begünstigte Gruppe. Eine Summe über alle Gruppen wird nicht ohne Zuordnung auf jeden einzelnen Vertrag übertragen.

3 Verwendung im Rentenbezug

Soweit nach dem konkreten Tarif Überschussanteile im Rentenbezug zugeteilt werden, werden sie zur Erhöhung der laufenden Leistung des betreffenden Bestands verwendet. Für Sondertarife oder abweichende individuelle Vereinbarungen ist die jeweilige Vertragsfassung zu prüfen. Ob die tatsächliche Verwendung in einem bestimmten Jahr alle Voraussetzungen einer arbeitsrechtlichen Anpassungsausnahme erfüllt, wird durch diese allgemeine Tarifbeschreibung nicht abschließend bestätigt.

4 Nachweis

Die Kasse stellt dem Mitgliedsunternehmen auf Anforderung die für seinen Bestand erforderliche Aufteilung bereit. Das Unternehmen muss dabei Vertragsnummer, Zusagegruppe und Prüfjahr benennen. Fehlende historische Zuordnungen werden als Klärungsposten geführt. Eine nicht ausgefüllte Spalte darf nicht als positiver Verwendungsnachweis verwendet werden.

5 Änderungen

Änderungen der Tarifbedingungen werden mit Geltungsbeginn und betroffenen Vertragsgruppen mitgeteilt. Die Kasse entscheidet damit nicht über außerhalb des Versicherungsvertrags erteilte Arbeitgeberzusagen.''')
doc(p,'15','Treasury_Auftrag.pdf','Treasury – zwei unterschiedliche Finanzierungsfragen','2026-10-20','Finanzvorstand Niederrhein Industrieverbund AG','Treasury und Recht', '''1 Laufende Arbeitgeberleistungen

Für die Planung ist zu ermitteln, welche Gesellschaft aufgrund ihrer tatsächlichen Zusagen zusätzliche monatliche Zahlungen leisten muss. Die garantierte Kürzung von18.000EUR proMonat und die Überschussverringerung von5.000EUR dürfen nicht ungeprüft als einheitlicher Anspruch aller Rentner behandelt werden. Die Zahlungen sind den drei Arbeitgebern zuzuordnen.

2 Zusätzliche Finanzierung der Kasse

Daneben hat die Kasse um Gespräche über zusätzliche Mittel der Mitgliedsunternehmen gebeten. Ein zusätzlicher Kassenbeitrag ist nicht automatisch identisch mit der Erfüllung einer konkreten Rentenforderung gegen den Arbeitgeber. Für beide Wege sind Kosten, Zweckbindung, Auswirkung auf zukünftige Leistungen und vertragliche Voraussetzungen getrennt darzustellen.

3 Liquidität

Die AG verfügt zum30.September über18Mio.EUR freie Bankliquidität. Die Komponenten GmbH und Service GmbH führen eigene Konten. Eine vorhandene Konzernliquidität ist kein Nachweis, dass jede Tochtergesellschaft ohne Vereinbarung hierüber verfügen darf. Für eine interne Finanzierung ist ein ausdrücklicher Abruf- und Rückzahlungsmechanismus vorzulegen.

4 Auftrag

Bitte rechnen Sie eine Variante mit ausschließlich garantierten Differenzbeträgen und eine vorsichtige obere Planungsvariante mit der gesamten tatsächlichen Zahlungslücke. Diese Planvarianten sind keine rechtliche Vorentscheidung. Eine pauschale Ablehnung von Rentneranfragen wird nicht freigegeben.''')
doc(p,'16','Kasse_Finanzierungsvorschlag.pdf','Mitgliederfinanzierung2027 – Gesprächsvorschlag','2026-10-21','Rheinwiese Pensionskasse VVaG','Niederrhein-Verbund', '''Sehr geehrte Damen und Herren,

wir schlagen Gespräche über eine zusätzliche Finanzierung von6Mio.EUR durch die Mitgliedsunternehmen des Niederrhein-Verbunds vor. Dieser Betrag ist eine Verhandlungsgröße unseres Planungsmodells. Eine bindende Verpflichtung Ihrer Unternehmen besteht aus diesem Schreiben noch nicht. Vorgesehen wären drei Raten von je2Mio.EUR in2027,2028 und2029.

Bitte teilen Sie mit, welche Gesellschaften an einer konkreten Vereinbarung mitwirken könnten. Zu klären sind Zweckbindung, verbindliche Leistungsziele, die Behandlung der bereits umgesetzten Kürzung und die erforderlichen Beschlüsse und aufsichtsrechtlichen Voraussetzungen. Wir haben Ihnen noch keine genehmigte Vereinbarung übermittelt.

Die im Jahr2026 geänderten gesetzlichen Möglichkeiten einer vorübergehenden Unterdeckung werden gesondert geprüft. Wir erklären hiermit nicht, dass deren Voraussetzungen in unserem Fall bereits erfüllt seien oder dass sie ohne weitere Grundlage eine Kürzung rechtfertigen. Ein belastbarer Vorschlag erfordert Satzungsabgleich, Finanzierungszusagen und die erforderlichen Genehmigungen.

Dr.Vera Hain, Vorstand.''')
pcorr=[('17','Payroll_Abgleich.eml','Kürzungsliste: Brutto, Netto und Arbeitgeber trennen','2026-10-21','Payroll <payroll@niederrhein-verbund.example>','Projektgruppe <projekt@niederrhein-verbund.example>','Die Kassenliste enthält Bruttobeträge. Bitte vergleicht sie nicht unmittelbar mit den auf Privatkonten eingegangenen Nettobeträgen. Für den Arbeitgeberausgleich benötigen wir zunächst die sachlich zugeordneten garantierten und zusätzlichen Bestandteile.\n\nDie Liste umfasst680 Rentner. Der Detailauszug mit42 Personen dient der Belegprüfung und ist keine Vollauswertung. Claudia Seidel trägt die NummerN-0001 und gehört zur Service GmbH. Ihr garantierter Fehlbetrag beträgt72EUR, die Überschussdifferenz20EUR. Ein automatischer Sammellauf ist noch nicht freigegeben.\n\nWir haben die historischen Beträge nicht überschrieben. FürSeptember undOktober stehen jeweils alte und neue Komponenten im Export. Bitte gebt bei einer Freigabe den Monat, Rechtsgrund und die steuerliche Abwicklung gesondert an.'),('18','Betriebsrat.pdf','Anfrage zur Zukunft der Kassenversorgung','2026-10-22','Gesamtbetriebsrat Niederrhein-Verbund','Vorstand Personal','Sehr geehrte Damen und Herren,\n\naktive Beschäftigte fragen, ob die Kürzung der Rentner auch ihre künftigen Ansprüche betrifft. Die bisherigen Informationen vermischen laufende Renten, garantierte Anwartschaften und nicht garantierte Hochrechnungen. Bitte stellen Sie die Auswirkungen für diese Gruppen getrennt dar.\n\nWir benötigen eine Beschreibung der Arbeitgeberzusagen, der Kassenmaßnahme und der beabsichtigten Finanzierung. Die bloße Aussage „die Kasse hat entschieden“ beantwortet die Frage nach den Zusagen der Unternehmen nicht. Eine Änderung der Versorgung aktiver Beschäftigter ist bislang weder erläutert noch vereinbart.\n\nBitte laden Sie zu einem Informationsgespräch ein und übermitteln Sie die vorgesehenen Erläuterungen vorab. Diese Anfrage enthält keine Zustimmung zu einer Leistungskürzung oder zu einer bestimmten Finanzierungsstruktur.'),('19','Lenkungskreis.docx','Projektgruppe Rheinwiese – offene Fragen vor Rentnerantworten','2026-10-23','Projektsekretariat','HR, Treasury, Recht','Die Projektgruppe bestätigt, dass die Kasse seitSeptember niedrigere Zahlungen leistet. Die garantierte Differenz und die Überschussänderung werden getrennt behandelt. Für die drei Arbeitgeber liegen unterschiedliche Zusagetexte vor. Der Ausdruck „Kassenrisiko“ ersetzt keine Prüfung dieser Texte.\n\nDas Anpassungsprotokoll2024 zeigt eine unerledigte Nachforderung. Die allgemeine Tarifbeschreibung allein belegt nicht die tatsächliche Überschussverwendung im maßgeblichen Bestand. HR soll die offenen Unterlagen konkret anfordern.\n\nTreasury berechnet laufende Ausgleichsvarianten und den getrennten Mitgliederfinanzierungsvorschlag. Eine Zahlung von6Mio.EUR an die Kasse wird nicht freigegeben. Bis zur Entscheidung werden Rentneranfragen individuell erfasst; es wird kein Standardablehnungsschreiben versandt.'),('20','Gesellschaftsfinanzierung.docx','Darlehensrahmen für laufende Versorgungsausgaben – Verhandlungsentwurf','2026-10-24','Niederrhein Industrieverbund AG','Niederrhein Komponenten GmbH und Niederrhein Service GmbH','1 Zweck\n\nDie AG soll den beiden Tochtergesellschaften einen gemeinsamen Darlehensrahmen von500.000EUR zur Finanzierung tatsächlich fälliger betrieblicher Versorgungsleistungen bereitstellen. Die interne Finanzierung verändert den jeweiligen Schuldner der Versorgungsleistung nicht. Jede Gesellschaft weist ihre eigenen Abrufe und Zahlungen gesondert nach.\n\n2 Abruf\n\nEin Abruf erfordert einen freigegebenen Monatsplan mit den betroffenen Leistungsbestandteilen und eine Bestätigung der Geschäftsführung. Die AG zahlt innerhalb von fünf Bankarbeitstagen auf das Konto der abrufenden Gesellschaft. Nicht benötigte Mittel werden mit der nächsten Abrechnung verrechnet. Ein Abruf für einen zusätzlichen Kassenbeitrag ist von diesem Zweck nicht umfasst.\n\n3 Verzinsung und Rückzahlung\n\nDer Entwurf sieht eine Verzinsung von3,5Prozent jährlich und eine Rückzahlung bis31.Dezember2028 vor. Die Zinsen werden monatlich auf den tatsächlich ausgereichten Betrag berechnet. Steuerliche und gesellschaftsrechtliche Angemessenheit sind vor Unterzeichnung zu prüfen. Es ist kein Rangrücktritt vereinbart.\n\n4 Kontrolle\n\nDie Tochtergesellschaften berichten monatlich über Verwendung und Liquidität. Die AG kann keine Kürzung rechtlich geschuldeter Renten verlangen, nur um eine Darlehensgrenze einzuhalten. Bei absehbarer Überschreitung wird unverzüglich eine Finanzierungsentscheidung eingeholt. Dieser Entwurf ist nicht unterzeichnet.'),('21','Teams_Renten.png','Teams – Wer ist für die Differenz zuständig?','2026-10-24','Projektgruppe Rheinwiese','HR und Treasury','09:31 | HR – Seidel verlangt92EUR, sind das alles garantierte Beträge?\n\n09:33 | Payroll – Nein:72EUR Garantie,20EUR Überschuss.\n\n09:35 | Recht – Zusage1998 und Bescheid2021 getrennt vom Kassentarif lesen.\n\n09:37 | Treasury – Bitte laufenden Ausgleich nicht mit6MioKassenfinanzierung verwechseln.\n\n09:40 | HR – Ich stoppe den Standardtext und fordere die Unterlagen2024 an.'),('22','Unterlagenanforderung.eml','Bitte konkrete Unterlagen zur Maßnahme und Überschussverwendung','2026-10-26','Projekt Rheinwiese <projekt@niederrhein-verbund.example>','Bestandsmanagement <bestand@rheinwiese.example>','Sehr geehrte Damen und Herren,\n\nbitte stellen Sie uns die vollständige Beschlussausfertigung vom30.Juni, den betroffenen Tarifkreis, die einschlägige Satzungsfassung und die aufsichtsrechtlichen Unterlagen zur umgesetzten Maßnahme zur Verfügung. Unsere aktuelle Akte enthält nur die Ankündigung und die geänderten Leistungsmitteilungen.\n\nFür die Anpassungsprüfung benötigen wir außerdem die tatsächlich zugeteilten Überschüsse und deren Verwendung je Tarifgruppe für2021 bis2024. Eine Gesamtsumme über sämtliche Mitglieder genügt uns nicht. Bitte kennzeichnen Sie historische Lücken ausdrücklich und ersetzen Sie sie nicht mit einer aktuellen Tarifbeschreibung.\n\nFür Claudia Seidel bitten wir um Zuordnung der Vertragsnummer zur Zusage1998 und zur Leistungsbestätigung2021. Die Anfrage soll weder eine Zustimmung zur Kürzung noch eine abschließende rechtliche Anerkennung der Maßnahme darstellen.'),('23','Service_Gespraech.docx','Gespräch mit ehemaliger Personalreferentin','2026-10-27','Anne Brück, HR','Projekt Rheinwiese','Die ehemalige Personalreferentin Eva Neuhaus erinnert sich, dass bei der Service GmbH die garantierte Kassenleistung ausdrücklich als Arbeitgeberleistung zugesagt wurde. Sie verweist auf die Bestätigung1998 und die Rentenmitteilung2021. Sie kann nicht bestätigen, dass alle Beschäftigten dieselben Texte erhalten haben.\n\nDie Überschussinformationen seien früher jährlich abgelegt worden. Nach einem Archivwechsel2022 seien einige Anlagen nur in einem alten Laufwerk verblieben. Neuhaus nennt den Ordner „Kasse-Renten-Abgleich“, hat derzeit aber keinen Zugriff. Sie erklärt, dass ein Tabellenfeld „Anpassung erledigt“ häufig nach Versand einer Kasseninformation gesetzt worden sei, ohne den Inhalt der Information rechtlich zu prüfen.\n\nDer Vermerk hält die Erinnerung fest und ersetzt die angekündigte Archivrecherche nicht. Neuhaus hat keine Vollmacht, für die Gesellschaft Ansprüche anzuerkennen oder abzulehnen.')]
for id,file,title,date,sender,recipient,body in pcorr:doc(p,id,file,title,date,sender,recipient,body)
doc(p,'24','Kasse_Nachlieferung.eml','Tarifgruppen nicht vollständig zugeordnet','2026-11-02','Bestandsmanagement <bestand@rheinwiese.example>','Projekt Rheinwiese <projekt@niederrhein-verbund.example>', '''Sehr geehrte Damen und Herren,

für2024 haben wir die Überschussverwendung der Standardtarife rekonstruiert. Bei den zwölf Verträgen der SondergruppeRW-S98 fehlt noch die eindeutige Zuordnung zu den damaligen Zuteilungstabellen. Claudia Seidel ist nach der Vertragsnummer dieser Gruppe zugeordnet. Die pauschale Portalmarkierung „Überschüsse verwendet“ bezog sich nur auf den Gesamtbestand und kann diese Einzelfrage nicht beantworten.

Die vollständige aufsichtsrechtliche Korrespondenz zur Kürzungsmaßnahme wird derzeit für die Übermittlung aufbereitet. Wir bitten Sie, aus dem bisher fehlenden Download weder eine bereits bewiesene Genehmigung noch deren Nichtvorliegen abzuleiten. Für Ihre Akte ist der Nachweis weiterhin offen.

Wir stellen die vorhandene Tarifgruppenliste bei. Die Arbeitsgruppe soll die noch fehlenden Unterlagen konkret benennen. Eine rechtliche Bewertung der Arbeitgeberzusage übernehmen wir nicht.''',phase='Fortsetzung',attachments=['Fortsetzung/32_Tarifgruppen_Nachlieferung.csv'])
doc(p,'25','Alte_Mail_2024.eml','Wiedergefunden: offene Frage zur Service-Sondergruppe','2024-10-08','Personalverwaltung <altarchiv@niederrhein-verbund.example>','Treasury <treasury@niederrhein-verbund.example>', '''Guten Tag,

für die zwölf VerträgeRW-S98 fehlen uns weiterhin die tarifbezogenen Überschussnachweise. Die allgemeine Kasseninformation beantwortet die Frage nicht. Bitte lasst den Status im Anpassungsregister offen, bis die konkrete Zuordnung geprüft wurde.

Frau Seidel hatte bereits telefonisch nachgefragt, wann sie eine verständliche Mitteilung erhält. Wir haben noch keinen endgültigen Antworttext. Eine abschließende Prüfung der wirtschaftlichen Lage der Service GmbH liegt ebenfalls nicht in dieser Akte. Bitte gebt das Thema an die neue Sachbearbeitung weiter, wenn unser Laufwerk zumJahresende umgestellt wird.

Eva Neuhaus''',phase='Fortsetzung',archive_received='2026-11-03')
doc(p,'26','Seidel_Nachfrage.eml','Frist6.November – bitte konkreter Zwischenstand','2026-11-05','Claudia Seidel <claudia.seidel@example.example>','Personalservice <pensionen@niederrhein-verbund.example>', '''Sehr geehrte Frau Brück,

Sie haben meinen Eingang bestätigt, aber noch nicht erklärt, ob die garantierte Differenz bezahlt wird. FürSeptember undOktober fehlen zusammen144EUR der garantierten Leistung; die zusätzlichen Überschussdifferenzen betragen zusammen40EUR. Die Novemberzahlung wird nach der Kassenmitteilung ebenfalls geringer ausfallen.

Bitte teilen Sie mir mit, welche Frage bereits geklärt ist und welche Unterlage noch fehlt. Ich möchte nicht nur den Hinweis erhalten, die Kasse müsse antworten. Auch meine Frage zur Anpassung seit2021 ist offen. Ich bin bereit, noch vorhandene Unterlagen zu übersenden, wenn Sie konkret sagen, was Sie benötigen.

Eine Klage ist weiterhin nicht eingereicht. Ich bitte um einen nachvollziehbaren schriftlichen Sachstand und einen konkreten Termin für die weitere Antwort.''',phase='Fortsetzung')
cohorts=[['AG – Zusage1992',260,140000,25000,131600,23000],['Komponenten – Zusage2001',180,90000,18000,84600,16500],['Service – Zusage1998',240,70000,17000,65800,15500]]
workbook(p,'27','Kuerzungen_Kohorten.xlsx','Monatliche Kassenleistung nach Zusagegruppen',[{'name':'Kohorten','columns':['Gruppe','Rentner','Garantie_alt_EUR','Ueberschuss_alt_EUR','Garantie_neu_EUR','Ueberschuss_neu_EUR','Garantiedifferenz_EUR','Gesamtdifferenz_EUR'],'rows':[a+[f'=C{i+6}-E{i+6}',f'=C{i+6}+D{i+6}-E{i+6}-F{i+6}'] for i,a in enumerate(cohorts)]+[['Gesamt','=SUM(B6:B8)','=SUM(C6:C8)','=SUM(D6:D8)','=SUM(E6:E8)','=SUM(F6:F8)','=SUM(G6:G8)','=SUM(H6:H8)']],'formats':{x:'currency' for x in ['Garantie_alt_EUR','Ueberschuss_alt_EUR','Garantie_neu_EUR','Ueberschuss_neu_EUR','Garantiedifferenz_EUR','Gesamtdifferenz_EUR']}},{'name':'Seidel','columns':['Monat','Garantie_alt_EUR','Garantie_neu_EUR','Ueberschuss_alt_EUR','Ueberschuss_neu_EUR','Garantiedifferenz_EUR','Gesamtdifferenz_EUR'],'rows':[[mon,1200,1128,60,40,f'=B{i+6}-C{i+6}',f'=B{i+6}+D{i+6}-C{i+6}-E{i+6}'] for i,mon in enumerate(['2026-09','2026-10','2026-11'])],'formats':{x:'currency' for x in ['Garantie_alt_EUR','Garantie_neu_EUR','Ueberschuss_alt_EUR','Ueberschuss_neu_EUR','Garantiedifferenz_EUR','Gesamtdifferenz_EUR']}}])
p['workbooks'][-1]['controls']=[{'sheet':'Kohorten','cell':'B9','expected':680},{'sheet':'Kohorten','cell':'G9','expected':18000},{'sheet':'Kohorten','cell':'H9','expected':23000},{'sheet':'Seidel','cell':'F6','expected':72},{'sheet':'Seidel','cell':'G6','expected':92}]
workbook(p,'28','Treasury_Planung.xlsx','Planungsvarianten – keine Entscheidung über einzelne Ansprüche',[{'name':'Laufender_Ausgleich','columns':['Variante','Monatsbetrag_EUR','Monate_2026','Plan_2026_EUR','Plan_2027_EUR'],'rows':[['Nur garantierte Differenz',18000,4,'=B6*C6','=B6*12'],['Gesamte Zahlungslücke',23000,4,'=B7*C7','=B7*12']],'formats':{'Monatsbetrag_EUR':'currency','Plan_2026_EUR':'currency','Plan_2027_EUR':'currency'}},{'name':'Kassenfinanzierung','columns':['Jahr','Rate_EUR','Status'],'rows':[[2027,2000000,'Verhandlungsvorschlag'],[2028,2000000,'Verhandlungsvorschlag'],[2029,2000000,'Verhandlungsvorschlag'],['Gesamt','=SUM(B6:B8)','Keine Unterschrift']],'formats':{'Rate_EUR':'currency'}},{'name':'Bestandsumfang','columns':['Gruppe','Aktiv','Ausgeschieden','Rentner'],'rows':[['AG',610,140,260],['Komponenten',470,90,180],['Service',380,90,240],['Gesamt','=SUM(B6:B8)','=SUM(C6:C8)','=SUM(D6:D8)']]}])
p['workbooks'][-1]['controls']=[{'sheet':'Laufender_Ausgleich','cell':'D6','expected':72000},{'sheet':'Laufender_Ausgleich','cell':'E6','expected':216000},{'sheet':'Laufender_Ausgleich','cell':'E7','expected':276000},{'sheet':'Kassenfinanzierung','cell':'B9','expected':6000000},{'sheet':'Bestandsumfang','cell':'B9','expected':1460},{'sheet':'Bestandsumfang','cell':'C9','expected':320}]
pr=[]
for i in range(1,43):
 g=1200 if i==1 else 300+i*9
 old=60 if i==1 else 20+i
 new=40 if i==1 else round(old*.9,2)
 pr.append([f'N-{i:04}','Service' if i<=14 else 'AG' if i<=28 else 'Komponenten','RW-S98' if i<=12 else 'Standard',g,old,round(g*.94,2),new,'Ausgewählter Detailfall'])
csvdoc(p,'29','Detailauszug_42.csv','42 ausgewählte Renten – Einzelfallabgleich',['Person','Arbeitgeber','Tarifgruppe','Garantie_alt_EUR','Ueberschuss_alt_EUR','Garantie_neu_EUR','Ueberschuss_neu_EUR','Umfang'],pr)
csvdoc(p,'30','Dokumenteneingang.csv','Unterlagenstand der Projektgruppe',['Unterlage','Stand','Status'],[['Zusage1992','2026-10-19','Original vorliegend'],['Zusage2001','2026-10-19','Original vorliegend'],['Seidel1998/2021','2026-10-19','Original vorliegend'],['Beschlussausfertigung30.06.2026','2026-10-26','angefordert'],['Aufsichtsunterlagen','2026-10-26','angefordert'],['TarifnachweisRW-S98','2026-10-26','offen']])
presentation(p,'31','Rheinwiese – Kasse und Arbeitgeberzusage unterscheiden',[('Was passiert ist',['680 laufende Renten seitSeptember geringer','Garantie300.000→282.000EUR proMonat','Überschuss60.000→55.000EUR proMonat']),('Drei Ebenen',['Kassenvertrag und konkrete Maßnahme','Arbeitgeberzusage je Gesellschaft','Anpassung und tatsächliche Überschussverwendung']),('Finanzierung',['Laufende Differenzzahlung prüfen','6MioEUR Mitgliederfinanzierung nur Vorschlag','Interner Darlehensrahmen getrennt gestalten']),('Nächste Entscheidung',['Seidel konkret antworten','Fehlende Originalnachweise beschaffen','Keine pauschale Lösung für alle Kohorten'])])
csvdoc(p,'32','Tarifgruppen_Nachlieferung.csv','Nachlieferung zur Überschusszuordnung',['Tarifgruppe','Vertraege_im_Detailauszug','Nachweis2024','Status'],[['RW-S98',12,'nicht vollständig zugeordnet','offen'],['Standard',30,'Gruppenaufteilung vorhanden','Einzelzuordnung abgleichen']],'Fortsetzung')
p['documents'][-1]['date']='2026-11-02'
doc(p,'33','Portal_Status.png','Mitgliederportal – unterschiedliche Dokumentstände','2026-10-26','Rheinwiese Mitgliederportal','Mitgliedsunternehmen','''Leistungsmitteilungen September – verfügbar

Beschlussausfertigung Juni – Bereitstellung angefragt

Aufsichtsunterlagen – individueller Zugang in Klärung

Überschussverwendung gesamt – verfügbar

TarifgruppeRW-S98 – historische Zuordnung offen

Hinweis der Projektgruppe: Statusanzeige ersetzt keinen Vertragsnachweis.''')
doc(p,'34','Verguetungsvereinbarung.pdf','Vergütungsvereinbarung Projekt Rheinwiese','2026-10-20',CONTACT,p['client'],'''Die außergerichtliche Bearbeitung wird nach tatsächlichem Zeitaufwand vergütet. Für Partner gilt ein Satz von420EUR netto proStunde, für anwaltliche Mitarbeit290EUR netto. Die kleinste Abrechnungseinheit beträgt sechsMinuten entsprechend tatsächlicher Tätigkeit. Umsatzsteuer wird zusätzlich in gesetzlicher Höhe ausgewiesen. Monatliche Nachweise enthalten Datum, Bearbeiter, Tätigkeit und Dauer.

Für Sichtung, Strukturierung und die erste Entscheidungsvorlage gilt ein Planungsbudget von90.000EUR netto. Es handelt sich nicht um eine Pauschale. Vor absehbarer Überschreitung um mehr als10Prozent stimmt die Kanzlei weitere nicht eilbedürftige Arbeiten ab. Allgemeine Bürokosten sind enthalten. Externe Bewertungen und Gerichtsvertretung bedürfen eines gesonderten Auftrags.

Ein Erstattungsanspruch gegen Dritte umfasst regelmäßig höchstens gesetzlich erstattungsfähige Kosten. Die Mandantin kann deshalb einen Teil der vereinbarten Vergütung selbst tragen müssen. Rechnungen sind binnen21Kalendertagen nachZugang fällig. Einwendungen werden unter Benennung der jeweiligen Position mitgeteilt.

Unterzeichnet am20.Oktober2026: Vorstand der Niederrhein IndustrieverbundAG und Dr.Nora Treuenfels.''')
doc(p,'35','Liquiditaet_Service.pdf','Service GmbH – Mittelbedarf und Verantwortlichkeit','2026-10-28','Geschäftsführung Niederrhein Service GmbH','Konzern-Treasury', '''Sehr geehrte Damen und Herren,

unsere Gesellschaft verfügt zum30.September über420.000EUR freie Bankmittel. Daneben bestehen laufende Lohn- und Lieferantenzahlungen. Die Konzernzahl von18Mio.EUR ist nicht unser Kontostand. Bitte planen Sie einen zusätzlichen Mittelabruf nur auf Grundlage einer tatsächlich vereinbarten Finanzierung.

Für die Service-Kohorte beträgt die monatliche garantierte Kassenkürzung4.200EUR; hinzu kommen1.500EUR weniger Überschüsse. Ob und in welchem Umfang zusätzliche Arbeitgeberzahlungen zu leisten sind, soll anhand der konkreten Zusagen entschieden werden. Wir sind bereit, freigegebene Zahlungen umzusetzen, benötigen dafür aber eine klare Fallzuordnung und einen nachvollziehbaren Buchungsgrund.

Eine zusätzliche Finanzierung der Kasse über mehrere Jahre soll nicht ohne gesonderte Geschäftsführungsentscheidung aus unserem Konto geleistet werden. Der Entwurf des Darlehensrahmens wird derzeit geprüft. Bitte lassen Sie Rentneranfragen nicht allein wegen der internen Finanzierungsabstimmung unbeantwortet.

Dr.Leonhard Mertens, Geschäftsführer.''')
# Typografie aus Diktat-/Schnelltexten zuverlässig normalisieren, ohne Zahlen zu ändern.
import re
for d in p['documents']:
 d['body']=[re.sub(r'(?<=[A-Za-zÄÖÜäöüß])(?=\d)|(?<=\d)(?=[A-Za-zÄÖÜäöüß])',' ',t).replace('Dr.Vera','Dr. Vera').replace('Dr.Leonhard','Dr. Leonhard').replace('Dr.Nora','Dr. Nora').replace('IndustrieverbundAG','Industrieverbund AG').replace('proStunde','pro Stunde').replace('nachZugang','nach Zugang').replace('sechsMinuten','sechs Minuten').replace('amDienstagvormittag','am Dienstagvormittag').replace('ansTelefon','ans Telefon').replace('seitRenteneintritt','seit Renteneintritt').replace('zumJahresende','zum Jahresende') for t in d['body']]
p['controls']={'pensioners':680,'active':1460,'deferred':320,'selected_persons':42,'guarantee_before_monthly_eur':300000,'guarantee_after_monthly_eur':282000,'surplus_before_monthly_eur':60000,'surplus_after_monthly_eur':55000,'guarantee_gap_monthly_eur':18000,'total_gap_monthly_eur':23000,'seidel_guarantee_gap_eur':72,'seidel_surplus_gap_eur':20,'kasse_uncommitted_financing_eur':6000000,'chronology':'Grundakte bis28.10.2026; Fortsetzung ab02.11.2026; Archivmail2024 wurde am03.11.2026 nachgeliefert.'}
save(p)
# Abschließender Datenabgleich nach unabhängiger Gegenlese.
for d in r['documents']:
 d['body']=[x.replace('Der Vorstand','Die Geschäftsführung').replace('der Vorstand','die Geschäftsführung').replace('Vorstandssitzung','Geschäftsführungssitzung').replace('Vorstandsentscheidung','Geschäftsführungsentscheidung') for x in d['body']]
 if d['id']=='28':
  rows=d['csv']['rows']
  for i,a in enumerate(rows,1):
   if i<=36:
    a[2]=1938+i%13;a[3]=f'{a[2]+65}-07-01'
   elif i<=42:a[2]=1950+i%11;a[3]='2015-07-01'
   else:a[2]=1962+(i-43);a[3]=''
  ss=io.StringIO();ww=csv.writer(ss,delimiter=';');ww.writerow(d['csv']['columns']);ww.writerows(rows);d['raw']=ss.getvalue();d['body']=[d['raw']]
 if d['id']=='15':d['body'].append('Die Zahlungsplanung enthält die Nettokaltmiete von70.000EUR monatlich als Zufluss vor Objektkosten und Finanzierung. Etwaige Umsatzsteuer wird in diesem Planungsblatt nicht als verfügbarer Ertrag angesetzt; Betriebskostenvorauszahlungen und zugehörige Ausgaben werden ebenfalls nicht als Nettomietüberschuss behandelt.')
r['workbooks'][0]['sheets'][1]['columns'][2]='Nettokaltmiete_vor_Objektkosten_EUR'
r['workbooks'][0]['sheets'][1]['formats'].pop('Miete_brutto_EUR')
r['workbooks'][0]['sheets'][1]['formats']['Nettokaltmiete_vor_Objektkosten_EUR']='currency'
for ca in [m,c,r,p]:
 for d in ca['documents']:
  if d['kind'] in ['csv']:continue
  def pretty(t):
   t=re.sub(r'(?<=[A-Za-zÄÖÜäöüß])(?=\d)|(?<=\d)(?=[A-Za-zÄÖÜäöüß])',' ',t)
   t=re.sub(r'(\d)\.(?=[A-ZÄÖÜ])',r'\1. ',t)
   for a,b in {'seitSeptember':'seit September','abSeptember':'ab September','imSeptember':'im September','undOktober':'und Oktober','fürSeptember':'für September','aufOktober':'auf Oktober','fürSeptember':'für September','für2024':'für 2024','proMonat':'pro Monat','proStunde':'pro Stunde','seitRenteneintritt':'seit Renteneintritt','zumJahresende':'zum Jahresende','nachZugang':'nach Zugang','binnen21':'binnen 21','sechsMinuten':'sechs Minuten','undOktober':'und Oktober','Gesellschaftsfinanzierung2027':'Gesellschaftsfinanzierung 2027'}.items():t=t.replace(a,b)
   return t
  d['body']=[pretty(x) for x in d['body']]
  for field in ['title','subject']:d[field]=pretty(d[field])
 save(ca)
for d in p['documents']:
 if d['id']=='01':d['body']=[t.replace('Eine Klage oder fertige rechtliche Musterlösung ist nicht enthalten.','Wir haben noch kein gerichtliches Verfahren eingeleitet. Zunächst sollen die konkreten Ansprüche und die tragfähige außergerichtliche Vorgehensweise geprüft werden.') for t in d['body']]
 if d['id']=='12':d['body']=[t.replace('Die Kasse hat auf meinem Konto im September und Oktober jeweils 1.168 EUR vor den in der Abrechnung genannten Abzügen ausgewiesen.','Die September-Leistungsabrechnung der Kasse weist 1.168 EUR brutto aus. Für Oktober ist derselbe Bruttobetrag angekündigt. Der auf meinem Konto eingegangene Nettobetrag enthält die in der Abrechnung ausgewiesenen Abzüge; er ist nicht mit dem Bruttobetrag gleichzusetzen.') for t in d['body']]
 if d['id']=='30':d['date']='2026-10-26'
p['workbooks'][0]['sheets'][1]['columns'].append('Status')
for row,status in zip(p['workbooks'][0]['sheets'][1]['rows'],['Septemberabrechnung Brutto','Oktoberleistung angekündigt; keine Bankbestätigung','Novemberleistung angekündigt; Planstand']):row.append(status)
# Sachlich passende Absender- und Empfängeranschriften statt pauschaler Konzernanschrift.
address_map={'Schwabenwerk':'Werkstraße 42\n70469 Stuttgart','Personalverwaltung Stuttgart':'Werkstraße 42\n70469 Stuttgart','Bremen GmbH':'Hafenallee 19\n28217 Bremen','Nordfeld Industries':'Werftstraße 9\n28195 Bremen','Nordfeld Automation Erwerbsgesellschaft':'Werftstraße 9\n28195 Bremen'}
for ca in [m,c,r,p]:
 for d in ca['documents']:
  if d['kind']=='eml':
   if 'claudia.seidel@' in d.get('from_email',''):d['from_email']='claudia.seidel@privatpost.example';d['sender']=d['sender'].replace('claudia.seidel@example.example','claudia.seidel@privatpost.example')
   continue
  for field in ['sender','recipient']:
   raw=d[field]
   for key,adr in address_map.items():
    if key in raw and '\n' in raw: d[field]=raw.split('\n')[0]+'\n'+adr;break
 save(ca)
for ca in [m,c,r,p]:
 for deck in ca['slides']:
  for slide in deck['slides']:
   slide['bullets']=[pretty(t).replace('Beschäftigte,216','Beschäftigte, 216').replace('Ausgeschiedene,318','Ausgeschiedene, 318').replace('Garantie 300.000→282.000 EUR pro Monat','Garantierte Leistung: 300.000 → 282.000 EUR pro Monat').replace('Überschuss 60.000→55.000 EUR pro Monat','Überschuss: 60.000 → 55.000 EUR pro Monat').replace('6 Mio EUR','6 Mio. EUR') for t in slide['bullets']]
 for d in ca['documents']:
  if d['kind']!='csv':d['body']=[t.replace('Mio.EUR','Mio. EUR').replace('Mio. EUR','Mio. EUR') for t in d['body']]
 save(ca)
