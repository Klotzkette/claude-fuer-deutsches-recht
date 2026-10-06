"""Ausformulierte Aktenstücke der zwei fortgesetzten Bauvergaben, keine Lösungen."""
from datetime import date, timedelta
from decimal import Decimal
from bauvergabe_falldaten import CASES, LV, money, total

def de(value):
    return date.fromisoformat(value).strftime('%d.%m.%Y')

def documents(c):
    clinic=c['short']=='Klinik'; result=[]
    owner=c['owner']; winner=c['winner']; rival=c['rival']; ref=c['reference']
    offer_date=(date.fromisoformat(c['deadline'])-timedelta(days=1)).isoformat()
    clarification_date='2026-11-25' if clinic else '2026-12-02'
    clarification_reply='2026-11-27' if clinic else '2026-12-04'
    clarification_deadline='30. November 2026' if clinic else '7. Dezember 2026'
    def doc(stage,name,title,body,stamp='06.10.2026',pdf=False):
        result.append(dict(file=f'{stage}/{name}.docx',title=title,date=stamp,body=body.strip(),pdf=pdf))
    def mail(stage,name,title,body,stamp,sender,recipient,attachments=()):
        result.append(dict(file=f'{stage}/{name}.eml',title=title,date=stamp,
                           body=body.strip(),sender=sender,recipient=recipient,attachments=list(attachments)))
    p='01-vergabeunterlagen'
    doc(p,'01_Projektauftrag','Projektauftrag und Finanzierung',f'''
{owner} · {c['address']}

## 1. Beschluss vom 28. September 2026

Die Geschäftsführung beauftragt die Vergabestelle mit der Vorbereitung des Vorhabens „{c['title']}“. Der Neubau umfasst {c['area']} Quadratmeter Bruttogrundfläche. {('Das Gebäude enthält eine interdisziplinäre Ambulanz, Diagnostikbereiche und bauliche Räume für die Krankenhausapotheke. Der Altbau bleibt während der Rohbauarbeiten in Betrieb. Apothekenbetrieb, Arzneimittelbeschaffung und medizinische Großgeräte werden nicht mit dem Rohbaulos vergeben.' if clinic else 'Vorgesehen sind 16 dauerhaft preisgebundene Mietwohnungen mit gemeinsamem Treppenhaus, Aufzug und Fahrradabstellraum. Die Vermietung erfolgt nach einem kommunalen Belegungskonzept. Ein Verkauf von Eigentumswohnungen ist nicht beschlossen.')}

Der vollständige Bauauftrag wird mit {money(c['project_net'])} EUR ohne Umsatzsteuer geschätzt. Die Kostenermittlung schließt sämtliche funktional zusammengehörenden Baugewerke, die bereits festgelegten Bauabschnitte und vorhersehbare Optionen ein. Planungsleistungen und Grundstückserwerb sind gesondert ausgewiesen. Die Schätzung für {c['lot']} beträgt {money(c['lot_budget'])} EUR netto. Sie ist eine interne Budgetgröße und wird nicht als Bieterpreis ausgegeben. Die Losbildung bleibt vor Veröffentlichung freizugeben.

## 2. Gesellschaft und öffentlicher Zweck

Die Stadt {c['city']} hält alle Geschäftsanteile, bestellt die Mehrheit des Aufsichtsrats und übt die gesellschaftsrechtliche Kontrolle aus. Der Gesellschaftsvertrag verpflichtet die Gesellschaft zur {('dauerhaften bedarfsgerechten stationären und ambulanten Versorgung unabhängig von der individuellen Rentabilität einzelner Fachabteilungen' if clinic else 'Bereitstellung bezahlbaren Wohnraums für Haushalte, die sich am örtlichen Wohnungsmarkt nicht angemessen versorgen können')}. Ausschüttungen an Gesellschafter sind ausgeschlossen. Ein kommunaler Betrauungsbeschluss und ein jährlicher Ausgleich nachgewiesener ungedeckter Gemeinwohlkosten liegen der Geschäftsführung vor. Der Ausgleich ersetzt keine freie Gewinnerzielungsgarantie für beliebige Projekte. Die Vergabestelle soll die Unterlagen zur Einordnung nach Paragraf 99 Nummer 2 GWB in die Vergabeakte nehmen; die Beteiligungsquote allein ist nicht als Begründung ausreichend.

## 3. Auftrag und Zuständigkeit

{c['purchaser']} führt das Verfahren. {c['engineer']} koordiniert Planung, Mengen und technische Freigaben. Änderungen an Kosten oder Vertragsumfang werden nur durch {c['lead']} oder eine dokumentiert bevollmächtigte Vertretung erklärt. Das Planungsbüro hat keine Vollmacht, vergütungspflichtige Zusatzleistungen zu beauftragen. Die Veröffentlichung ist nach der Vergabereifeprüfung für den {de(c['published'])} vorgesehen. Es gibt bisher weder eine Bekanntmachung noch einen Vertrag. Ein vorab versandter Arbeitsstand wird nicht rückwirkend zur veröffentlichten Fassung erklärt.

{c['lead']}, Geschäftsführung
''','28.09.2026')
    doc(p,'02_Planungsstand_Risikovermerk','Planungsstand, Schnittstellen und offene Baugrundfrage',f'''
{c['architect']} · Projekt {ref}

## 1. Technischer Arbeitsstand

Die Vorbemessung des Tragwerks liegt in Revision P03 vor. Die Positions- und Mengenliste vom 5. Oktober nennt die Mengen für den Rohbau. Ausführungsreife Details der Gründung werden erst nach ergänzender Baugrunderkundung freigegeben. Ein Bodenaustausch ist in der aktuellen Mengenliste nicht enthalten. Für den östlichen Baugrubenrand fehlt ein ergänzender Aufschluss. Dort wurde bei der Besichtigung dunkle Auffüllung angetroffen; eine abfallrechtliche Einstufung liegt noch nicht vor. Niemand hat eine belastbare pauschale Entsorgungsklasse für das gesamte Grundstück festgestellt.

{('Die Zufahrt kreuzt werktags zwischen 06:30 und 08:00 Uhr den Lieferverkehr der Bestandsapotheke. Rettungswege müssen ohne Voranmeldung jederzeit frei bleiben. Staubschutz, Erschütterungsmessung und die Abschottung zum laufenden Klinikbetrieb sind mit der Krankenhaushygiene abzustimmen. Die Klinik hat eine lärmempfindliche Diagnostik von 09:00 bis 12:00 Uhr gemeldet. Noch fehlt die Bestätigung, welche Geräte tatsächlich vibrationskritisch sind.' if clinic else 'Der westliche Nachbar nutzt seine Grundstückszufahrt werktags ab 07:00 Uhr. Eine vertragliche Überfahrtsgenehmigung liegt nicht vor. Die Baustelleneinrichtung soll vollständig auf dem Baugrundstück liegen. Die Feuerwehrzufahrt und der spätere Aufzugsschacht sind mit den getrennt vergebenen Außenanlagen- und Aufzugsgewerken abzustimmen. Eine pauschale Mitbenutzung des Nachbargrundstücks darf nicht vorausgesetzt werden.')}

## 2. Dokumentenregister

Plan P03 beschreibt die Bauteilgeometrie; die vorliegende Textfassung enthält keine prüffähige Statik. Das Brandschutzkonzept BS02 ist mit dem Tragwerksentwurf abzugleichen. Der Baugrundbericht BG01 enthält nur die vorhandenen Aufschlüsse. Die Vergabestelle hat am 6. Oktober um eine Ergänzung der fehlenden Erkundung vor Veröffentlichung gebeten. Eine Mengenliste ohne zugehörige Bauteil- und Messregeln ist nicht freigabefähig. Ich werde die offenen Punkte bis 9. Oktober schriftlich zurückmelden.

## 3. Schnittstellen im Leistungsverzeichnis

Die Position Leitungsdurchführungen umfasst ausschließlich die Rohbauöffnungen der abgestimmten Durchbruchsliste. Leitungsinstallation, Abschottung nach Installation und technische Inbetriebnahme werden anderen Losen zugeordnet. Vorhaltekosten und Gerüstleistungen müssen hinsichtlich Umfang und Zeitraum eindeutig beschrieben werden. Eine Klausel „sämtliche sonstigen Leistungen sind enthalten“ ist in dieser Fassung nicht vorgesehen. Die Bauteilqualitäten sind in einem eigenen Material- und Bauteilblatt festzulegen; Kurztexte der Mengentabelle ersetzen dieses Blatt nicht.

{c['engineer']}
''')
    paragraphs=[]
    for i,(pos,title,unit) in enumerate(LV,1):
        paragraphs.append(f'## {i+1}. Position {pos}\n\n{title}. Vorgesehene Menge: {c["quantities"][i-1]} {unit}. Die Menge ist anhand der Bauteilliste P03 nachzurechnen. Abgerechnet wird die tatsächlich ausgeführte, nachgewiesene Leistung in der angegebenen Einheit; für Pauschalpositionen gilt der vollständig beschriebene Umfang. Schnittstellen und erforderliche Freigaben ergeben sich aus den nachfolgenden besonderen Regeln.')
    doc(p,'03_Leistungsbeschreibung_Arbeitsstand','Leistungsbeschreibung Rohbau – Arbeitsstand vor Freigabe',f'''
{owner} · {ref} · Revision U03

## 1. Vorbemerkungen und Leistungsgrenzen

Gegenstand ist {c['lot']}. Der Auftragnehmer koordiniert seine Arbeiten mit den benannten Nachbargewerken; eine Übernahme ihrer Leistungen ist damit nicht verbunden. Der Bauleiter dokumentiert Aufmaße vor dem Verdecken. Transport- und Entsorgungsleistungen setzen die konkret benannte Einstufung und Annahmestelle voraus. Der derzeit fehlende Aufschluss am östlichen Baugrubenrand ist vor Freigabe dieser Fassung zu ergänzen. Der Auftraggeber stellt die geprüften Ausführungspläne rechtzeitig zur Verfügung. Geänderte Pläne erhalten eine eindeutige Revision und ein Freigabedatum.

{(chr(10)*2).join(paragraphs)}

## 18. Material- und Bauteilblatt

Der Betonansatz unterscheidet im endgültigen LV die Gründungsbauteile, Wände und Decken nach den aus Statik und Expositionsbedingungen abgeleiteten Eigenschaften. Die zusammengefasste Mengentabelle enthält derzeit noch keine endgültige Aufteilung. Für Abdichtung, Dämmung und Mauerwerk fehlen die endgültigen freigegebenen Bauteiltypen. Diese Fassung bleibt deshalb ein prüfbarer Arbeitsstand und ist noch keine vollständige ausschreibungsreife technische Planung. Konkrete Typen, Nachweise und Messregeln sind durch die zuständigen Planer zu ergänzen. Eine Marke wird nicht verbindlich vorgeschrieben.

## 19. Betrieb und Nachweise

{('Tagesbezogene Sperrzeiten und Hygienemaßnahmen werden mit der Klinikbetriebsleitung schriftlich abgestimmt. Der Auftragnehmer dokumentiert seine Staubschutzkontrollen und meldet eine Beeinträchtigung von Rettungswegen unverzüglich. Die Rohbauabnahme ist keine arzneimittelrechtliche Betriebsfreigabe der Krankenhausapotheke.' if clinic else 'Lieferungen erfolgen über das Baugrundstück; private Nachbarflächen werden ohne Zustimmung nicht benutzt. Die technische Abnahme des Rohbaus ist weder die Wohnungsübergabe an Mieter noch die Inbetriebnahme des Aufzugs.')}
Die Arbeitsunterlagen enthalten kein elektronisch validiertes GAEB-Austauschdokument. Eine CSV oder Excel-Datei darf nicht durch bloßes Umbenennen als GAEB-Datei ausgegeben werden.
''')
    doc(p,'04_Teilnahme_und_Wertung','Teilnahmebedingungen und vorgesehene Wertungsmethode',f'''
{owner} · Vergabeverfahren {ref} · Entwurf vom 6. Oktober 2026

## 1. Verfahren, Leistung und Kommunikation

Vorgesehen ist ein offenes Verfahren für {c['lot']}. Angebote werden ausschließlich über den in der Bekanntmachung zu benennenden elektronischen Zugang abgegeben. Die folgenden Daten sind Vorbereitungsdaten: Versand der Bekanntmachung {de(c['published'])}; ursprünglicher Angebotsschluss {de(c['original_deadline'])}, 10:00 Uhr; Bindefrist zunächst bis 31. Januar 2027. Eine gewöhnliche E-Mail ersetzt die elektronische Angebotsabgabe nicht. Rückfragen sind über den Kommunikationsbereich einzureichen und werden bei allgemeiner Bedeutung allen Interessenten gleichzeitig zugänglich gemacht.

## 2. Eignung und Kapazitäten

Der Bieter erklärt seine berufliche Befähigung, das Nichtvorliegen einschlägiger Ausschlussgründe und die Verfügbarkeit der für das Los benötigten personellen und technischen Mittel. Als Erfahrung werden zwei vergleichbare Rohbauleistungen der letzten fünf Jahre mit Auftraggeberkontakt, Leistungszeit, eigenem Anteil und Art des Bauwerks verlangt. Identische Gebäude oder Referenzen ausschließlich aus {c['city']} werden nicht verlangt. Der Auftraggeber berücksichtigt eine nachvollziehbare Vergleichbarkeit auch bei anders bezeichneten Gebäuden. Weitergehende Nachweise werden von aussichtsreichen Bietern nach Maßgabe der geltenden Regeln angefordert. Nachunternehmerleistung, Eignungsleihe und Bietergemeinschaft sind getrennt offenzulegen.

{('Für die Klinik wird keine zusätzliche örtliche oder krankenhausspezifische Unternehmensreferenz als Mindestanforderung festgelegt. Die Qualität des angebotenen Betriebsschutzes wird ausschließlich nach den angekündigten Zuschlagskriterien bewertet.' if clinic else 'Mindestens eines der beiden Referenzprojekte muss die vom Bieter selbst oder von einem hierfür benannten Eignungsleiher ausgeführte Herstellung vergleichbarer bewehrter Brandwände umfassen. Diese Erfahrung ist wegen der im Rohbaulos enthaltenen tragenden Brandwand mit ihren Bewehrungs- und Anschlussdetails erforderlich. Vergleichbarkeit richtet sich nach der ausgeführten Konstruktion und den maßgeblichen Anschlussarbeiten, nicht nach einem identischen Gebäudetyp, Auftraggeber oder Standort. Wird hierfür fremde Erfahrung genutzt, muss das benannte Unternehmen die betreffenden Brandwandarbeiten tatsächlich ausführen.')}

Bei Eignungsleihe sind Unternehmen, konkrete Kapazität und tatsächliche Leistungserbringung zu benennen. Die verbindliche Verfügbarkeit muss nachgewiesen werden. Eine erst nach Angebotsschluss neu gewonnene Kapazität ist nicht schon deshalb zulässig, weil der Auftraggeber eine Unterlage nachfordert. Eine bereits erklärte Kapazität und der nachgereichte Beleg ihres Bestands werden getrennt beurteilt.

## 3. Zuschlagskriterien

{('Der Angebotspreis erhält höchstens 80 Punkte. Die Formel lautet niedrigster wertbarer Angebotspreis geteilt durch den jeweiligen Angebotspreis, multipliziert mit 80. Das konkrete Baustellen- und Betriebsschutzkonzept erhält höchstens 20 Punkte. Bewertet werden die auf den vorgegebenen Klinikbetrieb bezogene Trennung der Wege, Staubschutzorganisation und Störfallkommunikation. Jede Dimension erhält null bis fünf Punkte; die vierte Dimension ist der konkrete Ablauf zur rechtzeitigen Freigabe lärmintensiver Arbeiten. Allgemeine Werbeaussagen ersetzen kein Konzept. Die Detailmaßstäbe sind vor Veröffentlichung zu vervollständigen; regionale Unternehmenssitze und allgemeine Erfahrung am Ort sind keine Zuschlagskriterien.' if clinic else 'Der Zuschlag wird auf das wirtschaftlichste wertbare Angebot mit dem niedrigsten Gesamtpreis erteilt. Ein Preisvergleich findet erst auf unveränderter Leistungsbasis statt. Eignungsnachweise werden nicht zusätzlich bepunktet. Ein geringer Preis allein ersetzt weder die Eignung noch die erforderliche Aufklärung auffälliger Preisansätze.')}

## 4. Angebotsinhalt

Das Angebot besteht aus dem ausgefüllten Preisblatt, dem Angebotsschreiben, den geforderten Erklärungen und {('dem Betriebsschutzkonzept' if clinic else 'der Übersicht der eingesetzten Unternehmen')}. Nebenangebote sind in dieser Ausschreibung nicht zugelassen. Änderungen der vorgegebenen Vertragsbedingungen sind offenzulegen und können zum Ausschluss führen. Allgemeine Geschäftsbedingungen des Bieters werden nicht als stillschweigende Änderung akzeptiert. Eine Nachforderung fehlender Unterlagen bleibt nach der geltenden VOB/A-EU zu prüfen; die Vergabestelle entscheidet hier nicht vorab, jede denkbare Lücke nachfordern zu dürfen.
''')
    doc(p,'05_Bauvertrag_Entwurf','Bauvertrag – Rohbaulos, Entwurf ohne Zuschlag',f'''
{owner} · Vertragsentwurf {ref}

## 1. Gegenstand und Vertragsgrundlagen

Der Auftraggeber beauftragt den im späteren Zuschlagsschreiben bezeichneten Auftragnehmer mit {c['lot']}. Dieser Entwurf enthält noch keine Annahme eines Angebots. Bestandteil des späteren Vertrags werden das ausdrücklich angenommene Angebot, das abschließende Leistungsverzeichnis einschließlich der bekannt gegebenen Berichtigungen, die freigegebenen Vertragspläne und die vollständig zur Verfügung gestellte VOB/B in der vertraglich bezeichneten Fassung. Die konkrete Rangfolge wird bei widersprechenden Leistungsangaben überprüft; eine technisch unklare Leistung wird nicht durch eine pauschale Vollständigkeitsklausel nachträglich erweitert.

## 2. Vergütung und Ausführung

Die Vergütung beruht auf den angebotenen Einheitspreisen und den nachgewiesenen tatsächlich ausgeführten Mengen. Vereinbarte Pauschalpositionen bleiben nach ihrem ausdrücklich beschriebenen Umfang abzurechnen. Der voraussichtliche Beginn ist der {de(c['start'])}, der vorgesehene Fertigstellungstermin der {de(c['finish'])}. Voraussetzung ist die rechtzeitige Übergabe des Baufelds und der freigegebenen Ausführungsunterlagen. Der Auftragnehmer legt binnen zehn Werktagen nach Zuschlag einen abgestimmten Bauzeitenplan vor. Widersprüche zwischen Terminplan und Vertragsbedingungen werden vor Ausführungsbeginn schriftlich geklärt.

## 3. Anordnungen und zusätzliche Vergütung

Anordnungen zur Änderung des vertraglichen Leistungsumfangs darf für den Auftraggeber nur die Geschäftsführung oder eine ausdrücklich benannte bevollmächtigte Person treffen. Das Planungsbüro darf technische Erläuterungen geben, besitzt aber keine allgemeine Abschlussvollmacht für vergütungspflichtige Nachträge. Der Auftragnehmer zeigt Leistungsänderungen und ihre absehbaren Preis- und Terminfolgen unverzüglich nachvollziehbar an. Die vergütungsrechtliche Beurteilung folgt der tatsächlich anwendbaren Vertragsgrundlage. Ein technischer Prüfvermerk ersetzt keine Preisvereinbarung. Gesetzliche Rechte werden durch das Fehlen einer vorab abgeschlossenen Preisvereinbarung nicht pauschal ausgeschlossen.

## 4. Dokumentation, Abrechnung und Abnahme

Aufmaße werden bauteilbezogen mit Planrevision, Datum und Beteiligten festgehalten. Die Unterschrift unter einem Aufmaß bestätigt den dokumentierten Messvorgang und enthält ohne zusätzliche Erklärung kein Anerkenntnis der Anspruchsgrundlage oder des Preises. Abschläge beziehen sich auf nachgewiesene vertragsgemäße Leistungen. Die Schlussrechnung weist den ursprünglichen Vertragsumfang, vereinbarte Änderungen und streitige Positionen getrennt aus. Der Auftraggeber prüft die Rechnung innerhalb der maßgeblichen Frist und bezeichnet Einwendungen konkret. Eine Zahlung ohne nähere Erklärung soll nicht als pauschales Anerkenntnis aller weiteren Forderungen verstanden werden.

Die Abnahme erfolgt nach gemeinsamer Begehung mit Protokoll. Bekannte Mängel und erforderliche Vorbehalte werden bezeichnet; Schlusszahlung und förmliche Abnahme werden nicht gleichgesetzt. Eine Vertragsstrafe ist in dieser Entwurfsfassung nicht vereinbart. Sicherheiten und Einbehalte dürfen nicht ohne abschließend geprüfte Vereinbarung aus einer anderen Vorlage ergänzt werden.

## 5. Öffentliche Auftragsänderung

Der Auftraggeber prüft unabhängig von der zivilrechtlichen Vergütung, ob eine geplante Änderung nach Paragraf 132 GWB ohne neues Vergabeverfahren zulässig ist und ob eine Bekanntmachung erforderlich wird. Eine Preisvereinbarung bestätigt nicht automatisch die vergaberechtliche Zulässigkeit. Die Parteien dokumentieren den geänderten Gegenstand, seinen Wert und die konkret tragende Änderungsgrundlage.
''')
    mail(p,'06_Freigabe_offene_Punkte','Bitte vor Veröffentlichung: Baugrund und LV-Version',f'''
Guten Morgen {c['engineer']},

die Geschäftsführung möchte am {de(c['published'])} veröffentlichen. Bitte bestätigen Sie bis 9. Oktober nicht nur „LV fertig“, sondern die zugehörige Bauteilliste, den Stand der Tragwerksfreigabe und die Ergebnisse des östlichen Bodenaufschlusses. In U03 stehen Beton und Schalung noch zusammengefasst. Das muss vor dem Versand der endgültigen Fassung nachprüfbar aufgeteilt sein. Die Kalkulation darf nicht auf einem stillschweigend unterstellten unbelasteten Boden beruhen.

{('Die Klinikbetriebsleitung hat außerdem die morgendlichen Anlieferungen zur Apotheke angesprochen. Ohne bestätigtes Logistikkonzept kann ich die Ausführungsfristen nicht freigeben.' if clinic else 'Bitte lassen Sie die Nachbarzufahrt aus dem Baustelleneinrichtungsplan heraus, solange uns keine Zustimmung vorliegt. Der Hausmeister kann diese Zustimmung nicht für die Nachbarin erteilen.')}

Ich habe den Arbeitsstand beigefügt. Die interne Kostenschätzung wird nicht an Bieter verteilt. Bitte senden Sie mir die fehlenden Angaben mit Revisionsnummer; keine stillen Änderungen an der alten Datei.

Viele Grüße
{c['purchaser']}
''','2026-10-06T09:15:00+02:00',f'{c["purchaser"]} <vergabe@{c["slug"]}.example>',f'{c["engineer"]} <planung@{c["slug"]}.example>',[f'{p}/02_Planungsstand_Risikovermerk.docx'])
    p='02-vergabeverfahren'
    doc(p,'01_Bekanntmachungsprotokoll','Veröffentlichungs- und Änderungsprotokoll',f'''
{owner} · {ref} · Bearbeitung {c['purchaser']}

## 1. Veröffentlichung

Der Bekanntmachungsdatensatz wurde am {de(c['published'])} um 09:12 Uhr zur Veröffentlichung abgesandt. Die Verfahrensakte verwendet die interne Kennung {ref}; eine echte TED-Veröffentlichungsnummer ist in diesem Ablageauszug nicht enthalten. Der Versandnachweis und der öffentlich bereitgestellte Wortlaut sind vor einer rechtlichen Fristenbewertung gesondert beizuziehen. Der Arbeitsstand U03 ist als überholt markiert. Die Vergabestelle erhielt am 9. Oktober die ergänzte Planerliste U04; ihr genauer Inhalt und die Übereinstimmung mit dem tatsächlich veröffentlichten Paket sind anhand des Portalexports zu prüfen.

## 2. Fristen und Unterlagen

Der ursprüngliche Angebotsschluss war {de(c['original_deadline'])}, 10:00 Uhr. Nach Rückfragen zu Transportwegen und Bodenansätzen wurde die Frist auf {de(c['deadline'])}, 10:00 Uhr verlängert. Die Berichtigung betrifft die Darstellung der Transportleistung, nicht die Menge der Betonposition. Eine bereits eingereichte Fassung kann bis zum neuen Angebotsschluss zurückgenommen und vollständig ersetzt werden. Das Portal soll die zurückgezogene Datei nicht als zweites wertbares Angebot behandeln.

## 3. Ablage und Konflikt

In der Planungsablage liegt weiterhin die alte Datei U03. Ein Mitarbeiter hatte diese Datei am 2. November intern weitergeleitet. Im Vergabeportal soll nach Aussage der Sachbearbeitung seit Veröffentlichung U04 gelegen haben. Die Aussage ist anhand der Versions- und Abrufprotokolle zu kontrollieren. Eine nachträglich gefertigte Übersicht darf fehlende damalige Freigaben nicht ersetzen. Das interne Revisionsregister weist beide Fassungen aus und nennt, wer welche Berichtigung freigegeben hat.
''',de(c['deadline']))
    mail(p,'02_Bieterfrage_Boden','Rückfrage Position 02.02 und Annahmestelle',f'''
Sehr geehrte Vergabestelle,

wir bearbeiten {ref}. Im Preisblatt steht bei Position 02.02 lediglich „Transport unbelasteten Aushubs“. Der Baugrundvermerk spricht dagegen von einer dunklen Auffüllung am östlichen Rand. Welche Untersuchung und welche Annahmestelle sind für die Kalkulation verbindlich? Bitte benennen Sie zudem die zu kalkulierende einfache Transportentfernung. Eine pauschale Bestätigung, sämtliche Entsorgungskosten seien einzurechnen, erlaubt uns keinen vergleichbaren Preis.

Wir bitten um eine für alle Bieter zugängliche Antwort. Falls die Antwort den Leistungsumfang ändert, benötigen wir die geänderte Positionsfassung und ausreichend Zeit für Rückfragen bei den Annahmestellen. Die übrigen Preise sind noch nicht abschließend freigegeben. Bitte bestätigen Sie den Eingang dieser Nachricht über das Portal.

Mit freundlichen Grüßen
{c['rival_lead']} · {rival}
''','2026-11-04T10:08:00+01:00',f'{c["rival_lead"]} <angebot@stein-ziegel.example>',f'Vergabestelle <vergabe@{c["slug"]}.example>')
    doc(p,'03_Berichtigung_01','Berichtigung 01 – Transportansatz und neue Angebotsfrist',f'''
{owner} · An alle registrierten Interessenten · {ref}

Sehr geehrte Damen und Herren,

für die Kalkulation der Position 02.02 ist eine einfache Entfernung von 18 Kilometern zur Annahmestelle Kieshof Nord anzusetzen. Die Vergütung dieser Position umfasst Transport und die im ergänzten Annahmeblatt ausdrücklich bezeichnete Annahme unbelasteten Materials. Die ergänzende Untersuchung vom 9. Oktober unterscheidet den unbelasteten Regelbereich vom östlichen Auffüllungsbereich. Der östliche Bereich wird vor Beginn dieser Rohbauleistung durch einen gesonderten Auftrag behandelt. Seine Entsorgung ist nicht in Position 02.02 einzurechnen. Der Auftragnehmer darf Material nicht ohne Zuordnung und Freigabe abfahren.

Die angebotenen Mengen bleiben unverändert. Für die Kalkulation ist der veröffentlichte Planstand U04 einschließlich dieser Berichtigung maßgeblich. Die intern zirkulierende Arbeitsfassung U03 enthält unvollständige technische Angaben und ist nicht als zusätzliche Leistungsanforderung heranzuziehen. Sollten Ihre heruntergeladenen Dateien hiervon abweichen, benennen Sie bitte die Dateinamen und Abrufzeiten umgehend.

Die Angebotsfrist endet nun am {de(c['deadline'])} um 10:00 Uhr. Die ursprüngliche Frist {de(c['original_deadline'])} wird ersetzt. Bereits abgegebene Angebote können bis zum neuen Fristende vollständig zurückgenommen und erneut abgegeben werden. Die Bindefrist bleibt zunächst der 31. Januar 2027. Bitte berücksichtigen Sie diese Berichtigung im Angebotsschreiben.

Mit freundlichen Grüßen
{c['purchaser']} · Vergabestelle
''','06.11.2026',pdf=True)
    doc(p,'05_Wertungsvermerk_erster_Stand','Wertungsvermerk – erster Bearbeitungsstand',f'''
{owner} · {ref} · Interne Vergabeakte

## 1. Eingang und Prüfstand

Zum neuen Angebotsschluss sind drei Angebote eingegangen. Das Angebot von {winner} lautet über {money(total(c))} EUR netto. Das Angebot von {rival} lautet über {money(total(c,c['rival_multiplier']))} EUR netto; das dritte Angebot liegt bei {money(total(c,c['third_multiplier']))} EUR netto. Die Beträge wurden rechnerisch mit den Preisblättern abgeglichen. Rückgezogene Uploads werden nicht als weitere Angebote gezählt. Dokumente zur Herkunft eines Preisbestandteils sind noch keine Zustimmung zur Änderung des eingereichten Preises.

## 2. Vermerk der Bearbeitung

{('Das Team hat in der ersten Arbeitsrunde zehn Qualitätspunkte für das Betriebsschutzkonzept und weitere zehn Punkte für bereits ausgeführte Baustellen im Stadtgebiet vergeben. Für Klinker sind acht Konzeptpunkte und acht Regionalpunkte notiert. Für Stein sind neun Konzeptpunkte und vier Regionalpunkte notiert. In den Teilnahmebedingungen steht dagegen ein einheitliches Betriebsschutzkonzept mit vier Dimensionen und insgesamt 20 Punkten. Die Sitznähe des Unternehmens wird dort nicht genannt. Der vorliegende Vermerk erläutert noch nicht, wie die Regionalpunkte aus den veröffentlichten Kriterien folgen sollen.' if clinic else 'Mörtelbau benannte im Angebot Maurermeister Rado Knuff GmbH als Eignungsleiher für die Erfahrung mit bewehrten Brandwänden. Das Anschreiben verwies auf eine Verpflichtung vom 20. November; die zugehörige Anlage fehlte im ersten Download der Vergabestelle. Nach Anforderung vom 2. Dezember ging am 4. Dezember die unterschriebene Erklärung ein. Ziegelwerk behauptet, hier sei nachträglich ein neues Unternehmen eingeführt worden. Die ursprüngliche Bieterliste nennt Knuff bereits; die Portaldatei und der genaue Verpflichtungsumfang sind vor abschließender Einordnung abzugleichen.')}

## 3. Weiteres Vorgehen

Die Sachbearbeitung empfiehlt vorläufig den Zuschlag an {winner}. Die Empfehlung ist kein Vertragsschluss. Die Geschäftsführung verlangt vor Versand der endgültigen Entscheidung eine nachvollziehbare Prüfung der offenen Frage. Die Wertungstabelle und die vertraulichen Bieterunterlagen werden ausschließlich der Vergabestelle und ihrer beauftragten Rechtsberatung zugänglich gemacht. Einem Bieter wird nicht ohne gesonderte Prüfung die vollständige Kalkulation des Konkurrenten überlassen.

{c['purchaser']}
''',de(c['notice']))
    doc(p,'06_Vorabinformation','Information über die beabsichtigte Zuschlagserteilung',f'''
{owner} · {c['address']}

An {rival} · Geschäftsführung {c['rival_lead']}

{de(c['notice'])} · {ref}

Sehr geehrte Damen und Herren,

wir beabsichtigen, den Zuschlag für {c['lot']} an {winner} zu erteilen. Ihr Angebot wird nicht berücksichtigt. {('Nach der bisher dokumentierten Wertung erzielt Ihr Angebot weniger Gesamtpunkte. Der Preis wurde nach der angekündigten Verhältnisformel berücksichtigt. In der Qualitätsbewertung wurden das Betriebsschutzkonzept und die regionale Baustellenerfahrung herangezogen. Eine Einzelaufschlüsselung ist diesem Schreiben nicht beigefügt.' if clinic else 'Ihr wertbarer Angebotspreis beträgt '+money(total(c,c['rival_multiplier']))+' EUR netto und liegt über dem wertbaren Preis des vorgesehenen Zuschlagsempfängers von '+money(total(c))+' EUR netto. Die Vergabestelle hält dessen Eignung nach Prüfung der vorgelegten Unterlagen für nachgewiesen.')}

Die elektronische Absendung dieses Schreibens ist für heute vorgesehen. Der früheste nach der Wartefrist vorgesehene Vertragsschluss ist der {de(c['first_award'])}. Ein Zuschlag erfolgt nicht, solange ein anderweitiges gesetzliches Zuschlagsverbot oder eine entgegenstehende gerichtliche Anordnung besteht. Fragen und Einwendungen sind unter Angabe der Verfahrenskennung über den Kommunikationsbereich an uns zu richten.

Mit freundlichen Grüßen
{c['purchaser']}
''',de(c['notice']),pdf=True)
    p='03-bieterarbeit'
    doc(p,'01_Angebotsentscheidung','Geschäftsführungsnotiz zur Angebotsfreigabe',f'''
{winner} · Geschäftsführung {c['director']}

## 1. Kapazität und Kostenbasis

Wir wollen {c['lot']} anbieten. Das Team kann ab {de(c['start'])} eingesetzt werden, sofern das noch laufende Hallenprojekt planmäßig abschließt. Der Polier hat bislang nur einen Wochenüberblick geschickt; eine schriftliche Personaldisposition für die ersten acht Wochen fehlt noch. Die Preisansätze beruhen auf den angefragten Lieferpreisen und den kalkulierten Stunden. Das interne Kalkulationsblatt wird nicht als Bestandteil unseres Angebots eingereicht. Die Verhandlungsuntergrenze bleibt ebenfalls intern.

## 2. Freigabefragen

Ich gebe ein Angebot nur auf Grundlage der veröffentlichten Berichtigung 01 frei. Die Mehrkosten eines vom Auftraggeber später geänderten Bauwerks werden nicht vorsorglich als unbestimmter Risikozuschlag in jede Position aufgenommen. Wir müssen aber die eindeutig beschriebenen Schutz-, Koordinations- und Vorhalteleistungen vollständig kalkulieren. {('Die Erfahrung unserer Mannschaft mit laufendem Klinikbetrieb ist im Konzept konkret zu beschreiben; ein Firmenprospekt genügt dafür nicht. Der Apothekerbetrieb ist keine von uns zu übernehmende Genehmigungsleistung.' if clinic else 'Die Brandwandreferenz wird durch Knuff bereitgestellt. Vor Abgabe ist zu prüfen, ob dessen Verpflichtung die konkrete Leistung und das tatsächlich eingesetzte Personal umfasst. Eine bloße Liste befreundeter Firmen reicht nicht.')}

## 3. Abgabe und Vertretung

Das Angebot darf erst nach meinem Abgleich von Preisblatt, Nachunternehmerangaben und Terminbindung hochgeladen werden. Es ist mit der vorgesehenen Vertretungsangabe abzugeben. Eine abweichende Vertragsfassung mit unseren allgemeinen Einkaufsbedingungen wird nicht beigefügt. Der Sachbearbeiter speichert die Eingangsbestätigung und prüft, ob die vollständige letzte Fassung tatsächlich vor {de(c['deadline'])} um 10:00 Uhr eingegangen ist. Ein erfolgreicher Dateiupload allein beweist noch nicht die fristgerechte endgültige Abgabe.
''','18.11.2026')
    doc(p,'03_Eignung_Kapazitaeten','Erklärung zur Eignung und zu eingesetzten Unternehmen',f'''
{winner} · {ref}

## 1. Eigene Leistung

Wir übernehmen die Rohbaukoordination, Betonarbeiten und die Baustellenleitung. Die Kalkulation beruht auf eigenen Fachkräften für Schalung und Betonage sowie den im Angebot bezeichneten Nachunternehmerleistungen. Unsere Referenzliste umfasst den Rohbau eines Verwaltungsgebäudes 2023 und eines Pflegezentrums 2025. Für beide Vorhaben benennen wir den jeweiligen Bauherrnkontakt und den tatsächlich selbst erbrachten Leistungsanteil. Die Namen der eingesetzten Bauleiter werden nur soweit verlangt und datenschutzrechtlich erforderlich übermittelt.

{('Die Eignung unseres Unternehmens wird unabhängig von der gesonderten Bewertung des angebotenen Betriebsschutzkonzepts dargestellt.' if clinic else 'Die von uns selbst ausgeführten Anteile dieser beiden Vorhaben enthalten keine mit der ausgeschriebenen Konstruktion vergleichbaren bewehrten Brandwände. Für diese ausdrücklich verlangte Erfahrung berufen wir uns daher auf die nachfolgend benannte Knuff-Kapazität. Unsere eigenen Referenzen allein sollen die ergänzende Brandwandanforderung nicht als erfüllt darstellen.')}

## 2. Unternehmen und Verfügbarkeit

{('Die Spezialfirma Hiltrud Gerüstbau GmbH führt die in Position 06.01 beschriebenen Gerüstarbeiten aus. Wir stützen unsere eigene Rohbaueignung nicht auf deren Unternehmensreferenzen. Ihr Angebot vom 17. November umfasst die vereinbarte Vorhaltung und den Rückbau. Ein separater Kapazitätsnachweis ist vorzulegen, falls die Vergabestelle eine entsprechende Verfügbarkeitserklärung verlangt.' if clinic else 'Für die Erfahrung mit den bewehrten Brandwänden nehmen wir die Kapazität der Maurermeister Rado Knuff GmbH in Anspruch. Knuff soll die betreffenden Brandwandarbeiten tatsächlich ausführen. In der für unser Angebot vorgesehenen Unternehmensliste ist diese Gesellschaft namentlich genannt. Die Geschäftsführung von Knuff erklärte heute, am 20. November, schriftlich, Personal und Erfahrung für die bezeichnete Leistung im Ausführungszeitraum zur Verfügung zu stellen. Die unterschriebene Verpflichtung liegt unserer Angebotsbearbeitung vor und ist als gesonderte Anlage für die Abgabe vorgesehen. Diese Erklärung bestätigt keine bereits erfolgte Portalabgabe.')}

## 3. Erklärung der Geschäftsführung

Wir erklären nach Prüfung der derzeit verfügbaren Unternehmensunterlagen, dass uns keine nicht offengelegten einschlägigen zwingenden Ausschlussgründe bekannt sind. Behördliche Auskünfte oder Registerauszüge werden dadurch nicht vorweggenommen. Änderungen der benannten Unternehmen oder ihrer Kapazitäten werden wir unverzüglich offenlegen und nicht stillschweigend durch andere Unternehmen ersetzen. Die Erklärung erstreckt sich nur auf die bezeichnete Vergabe; sie ist keine pauschale Erklärung für fremde Unternehmen.

{c['director']}, Geschäftsführung
''','20.11.2026')
    if not clinic:
        doc(p,'03a_Verpflichtung_Knuff','Verpflichtung zur Bereitstellung von Kapazitäten und zur eigenen Leistungserbringung',f'''
Maurermeister Rado Knuff GmbH · Geschäftsführung

An {winner} · Für das Vergabeverfahren {ref} des Auftraggebers {owner}

## 1. Bereitgestellte Kapazität

Wir verpflichten uns gegenüber {winner}, unsere Erfahrung mit bewehrten Brandwänden und die für die bezeichneten Brandwandarbeiten erforderlichen fachkundigen Beschäftigten für {c['lot']} bereitzustellen. Die Verpflichtung bezieht sich auf die im Angebot bezeichneten Brandwandarbeiten und den ausgeschriebenen Ausführungszeitraum vom {de(c['start'])} bis zum {de(c['finish'])}. Sie ist für den Fall der Zuschlagserteilung an {winner} verbindlich und steht nicht unter dem Vorbehalt einer späteren unverbindlichen Kapazitätsentscheidung.

## 2. Eigene Leistungserbringung

Wir werden die Brandwandarbeiten, für die unsere berufliche Erfahrung in Anspruch genommen wird, mit unserem hierfür vorgesehenen Personal tatsächlich selbst ausführen. Die Überlassung einer bloßen Unternehmensreferenz ohne entsprechende Leistungserbringung ist nicht Gegenstand dieser Erklärung. Die Rohbaukoordination und die weiteren im Angebot als eigene Leistung bezeichneten Arbeiten verbleiben bei {winner}. Eine Änderung dieser Abgrenzung oder ein Ersatzunternehmen werden nicht durch diese Erklärung zugelassen.

## 3. Nachweise und Vertretung

Die konkreten Referenzangaben, deren Vergleichbarkeit und die zum Einsatz vorgesehenen Kapazitäten sind anhand der gesonderten Referenz- und Personaldokumentation zu prüfen. Diese Verpflichtung ersetzt weder deren sachliche Prüfung noch die Prüfung etwaiger Ausschlussgründe unseres Unternehmens. Rückfragen zur Bindung und Verfügbarkeit können unmittelbar an unsere Geschäftsführung gerichtet werden. Die vorliegende Erklärung ist am 20. November 2026 durch unsere Geschäftsführung abgegeben; die Angebotsbearbeitung hat den Nachweis der Vertretungsbefugnis und die unterschriebene Ursprungsfassung aufzubewahren.

Geschäftsführung Maurermeister Rado Knuff GmbH
''','20.11.2026')
    doc(p,'04_Angebotsschreiben','Angebot für das Rohbaulos',f'''
{winner}

An {owner} · Vergabestelle · {c['address']}

{de(offer_date)} · {ref}

Sehr geehrte Damen und Herren,

wir bieten {c['lot']} zu den Einheitspreisen des beigefügten Preisblatts an. Die rechnerische Angebotssumme beträgt {money(total(c))} EUR netto, zuzüglich der gesetzlich geschuldeten Umsatzsteuer. Das Angebot berücksichtigt die Berichtigung 01 vom 6. November und den darin bezeichneten Leistungsstand. Nebenangebote geben wir nicht ab. Die in den Vergabeunterlagen vorgegebenen Ausführungsfristen werden angeboten; die dort geregelten Voraussetzungen für Plan- und Baufeldübergabe bleiben maßgeblich.

Wir halten uns bis zum 31. Januar 2027 an dieses Angebot gebunden. Eine Verlängerung der Bindefrist bedarf unserer ausdrücklichen Erklärung; sie wird nicht aus bloßem Schweigen abgeleitet. Die Erklärung zu eigenen und fremden Kapazitäten ist Bestandteil des Angebots. {('Das geforderte Betriebsschutzkonzept erläutert die vorgesehenen getrennten Lieferwege, Staubschutzkontrollen und Meldeketten.' if clinic else 'Die Unternehmensliste benennt die Maurermeister Rado Knuff GmbH für die tatsächlich von ihr auszuführenden Brandwandarbeiten.')}

Unsere interne Urkalkulation ist nicht Bestandteil der allgemeinen Angebotsunterlagen. Soweit eine gesonderte Hinterlegung wirksam vereinbart wird, erfolgt sie nach den dort beschriebenen Regeln. Wir fügen keine abweichenden Allgemeinen Geschäftsbedingungen bei. Fragen zu diesem Angebot richten Sie bitte über den vorgegebenen Kommunikationsweg an unsere Vergabebearbeitung.

Mit freundlichen Grüßen
{c['director']}
''',de(offer_date))
    mail(p,'05_Nachforderung','Anforderung ergänzender Unterlagen',f'''
Sehr geehrte Damen und Herren,

bei der Prüfung Ihres Angebots {ref} ist folgende Frage offen geblieben: {('Bitte erläutern Sie anhand bereits vorhandener Kalkulationsgrundlagen, welche Vorhaltezeit in Position 06.01 enthalten ist und weshalb diese Position deutlich unter der Kostenschätzung liegt. Der Gesamtpreis und die angebotene Leistung dürfen durch die Erläuterung nicht geändert werden.' if clinic else 'Bitte legen Sie die in Ihrer ursprünglichen Unternehmensliste bezeichnete Verpflichtung der Maurermeister Rado Knuff GmbH vom 20. November vor. Die Anforderung bezieht sich ausschließlich auf die schon benannte Kapazität. Eine erstmalige Benennung eines anderen Unternehmens ist damit nicht angefordert.')}

Wir setzen hierfür eine Frist bis {clarification_deadline}, 12:00 Uhr. Falls sich aus Ihrer Antwort eine Änderung des ursprünglichen Angebots ergibt, kennzeichnen Sie diese ausdrücklich. Die Vergabestelle wird selbst prüfen, ob und in welchem Umfang die Ergänzung berücksichtigt werden darf. Eine Aufforderung ist keine Zusicherung der Zuschlagsfähigkeit.

Mit freundlichen Grüßen
{c['purchaser']}
''',clarification_date+'T10:10:00+01:00',f'Vergabestelle <vergabe@{c["slug"]}.example>',f'{winner} <angebot@{c["slug"]}-bau.example>')
    mail(p,'06_Antwort_Aufklaerung','Antwort auf Ihre Anforderung – unveränderter Angebotspreis',f'''
{('Sehr geehrte Frau Klapper,' if clinic else 'Sehr geehrter Herr Knödler,')}

{('in Position 06.01 haben wir die im Terminplan vorgesehene Vorhaltung einschließlich eines innerbetrieblich bereits verfügbaren Gerüstbestands kalkuliert. Wir nutzen eigene Lagerflächen; eine zusätzliche externe Anmietung ist im angebotenen Zeitraum nicht erforderlich. Der Preis enthält den beschriebenen Auf- und Abbau. Verlängert sich die Vorhaltung aus anderen Ursachen, folgt daraus nicht automatisch ein zusätzlicher Vergütungsanspruch. Hierzu wären Ursache, Vertragsgrundlage und Zeitraum gesondert zu beurteilen.' if clinic else 'die beigefügte Verpflichtung bestätigt die vor Angebotsschluss erklärte Verfügbarkeit der Knuff-Kapazität. Das Unternehmen, seine Aufgabe und die Verantwortlichkeit für die Brandwandarbeiten bleiben unverändert. Wir reichen keinen neuen Eignungsleiher und keine neue Referenz ein. Die Vergabestelle kann die Angaben unmittelbar bei der Geschäftsführung von Knuff überprüfen. Dass die Anlage beim ersten Upload fehlte, räumen wir ein.')}

Unser Angebotspreis bleibt bei {money(total(c))} EUR netto. Die Erläuterung enthält weder einen Nachlass noch eine Änderung der angebotenen Leistung. Bitte bestätigen Sie den Eingang über das Portal. Für eine Rückfrage zur konkret bezeichneten Unterlage stehen wir heute bis 16:00 Uhr zur Verfügung.

Mit freundlichen Grüßen
{c['director']}
''',clarification_reply+'T11:20:00+01:00',f'{winner} <angebot@{c["slug"]}-bau.example>',f'Vergabestelle <vergabe@{c["slug"]}.example>',[] if clinic else [f'{p}/03a_Verpflichtung_Knuff.docx'])
    p='04-rechtsschutz'
    mail(p,'01_Mandatsauftrag','Bitte Zuschlag verhindern und Aktenlage prüfen',f'''
Sehr geehrte Kanzlei,

wir beauftragen Sie für {rival} mit der Prüfung und erforderlichen Wahrung unserer Rechte im Verfahren {ref}. Die Vorabinformation ist bei uns am {de(c['notice'])} elektronisch eingegangen. {('Von den Regionalpunkten haben wir erstmals durch dieses Schreiben erfahren. Unser Betriebsschutzkonzept berücksichtigt den Klinikbetrieb ausführlich. Ob und weshalb die Vergabestelle es anders bewertet hat, wissen wir nicht.' if clinic else 'Wir haben gehört, dass Mörtelbau nachträglich eine fremde Brandwandreferenz nachgereicht haben soll. Uns fehlt der ursprüngliche Angebotsinhalt; wir können bisher nicht unterscheiden, ob nur ein Beleg fehlte oder eine neue Kapazität eingeführt wurde.')}

Bitte formulieren Sie zunächst die konkrete Beanstandung und klären Sie, bis wann welche Schritte erforderlich sind. Wir möchten den Auftrag weiterhin ausführen und können unser Angebot bis zum 31. Januar halten. Eine Nachprüfung soll vorbereitet werden, falls keine rechtzeitige Abhilfe erfolgt. Bitte stimmen Sie eine tatsächliche Einreichung und die damit verbundenen Kosten vorher mit uns ab. Wir erlauben keine Weitergabe unserer vollständigen Kalkulation an Wettbewerber.

Mit freundlichen Grüßen
{c['rival_lead']}
''',c['objection']+'T08:30:00+01:00',f'{c["rival_lead"]} <geschaeftsfuehrung@stein-ziegel.example>',f'{c["counsel"]} <post@baukanzlei.example>')
    doc(p,'02_Ruege_Entwurf','Rüge des angekündigten Zuschlags – Entwurf',f'''
{c['counsel']} · Baukanzlei · Im Auftrag von {rival}

An {owner} · Vergabestelle · {ref}

Sehr geehrte Damen und Herren,

namens unserer Mandantin rügen wir die beabsichtigte Zuschlagserteilung. {('Ihre Vorabinformation benennt regionale Baustellenerfahrung als Qualitätskriterium. Ein solches Kriterium ist den unserer Mandantin zugänglichen Teilnahmebedingungen nicht zu entnehmen. Angekündigt waren ausschließlich der Preis und das konkret beschriebene Betriebsschutzkonzept. Eine nachträgliche Ergänzung verändert die Wettbewerbsbedingungen und kann unsere Zuschlagschance beeinträchtigen. Unsere Mandantin hat ihr Konzept auf die veröffentlichten Maßstäbe ausgerichtet.' if clinic else 'Es bestehen konkrete Zweifel an der ordnungsgemäßen Eignungsprüfung des vorgesehenen Zuschlagsempfängers. Nach der uns vorliegenden Information soll die Brandwandkapazität erst im Zuge einer Nachforderung belegt worden sein. Wir behaupten nicht ohne Aktenkenntnis, jedes nachgereichte Dokument sei unzulässig. Entscheidend ist, ob die konkrete fremde Kapazität bereits rechtzeitig benannt und tatsächlich verfügbar war oder nach Angebotsschluss erstmals in das Angebot eingeführt wurde.')}

Wir bitten um Überprüfung anhand der ursprünglichen Angebote und der veröffentlichten Bedingungen sowie um eine nachvollziehbare Antwort. Die Prüfung darf nicht durch nachträglich angepasste Vergabevermerke ersetzt werden. Unsere Mandantin verlangt die Wahrung ihrer Rechte aus Paragraf 97 Absatz 6 GWB und eine transparente, gleiche Behandlung. Im Falle erforderlicher Korrektur ist das Verfahren in den rechtmäßigen Stand zurückzuversetzen; ein Anspruch auf unmittelbare Auftragserteilung wird mit dieser Rüge nicht behauptet.

Bitte teilen Sie uns vor dem angekündigten frühesten Zuschlagstermin mit, ob Sie abhelfen. Die Rüge selbst begründet kein allgemeines automatisches Zuschlagsverbot. Gerade deshalb benötigen wir eine rechtzeitige Erklärung und werden bei ausbleibender Abhilfe den erforderlichen Rechtsschutz prüfen. Die Rüge wird nach dokumentierter Kenntnis am {de(c['objection'])} erhoben. Den Zugang sichern wir gesondert über den Kommunikationsbereich.

Mit freundlichen Grüßen
{c['counsel']}
''',de(c['objection']),pdf=True)
    mail(p,'03_Nichtabhilfe','Ihre Beanstandung im Verfahren '+ref,f'''
Sehr geehrte Damen und Herren,

wir helfen Ihrer Rüge vom {de(c['objection'])} derzeit nicht ab. {('Die Fachabteilung sieht die bisher verwendeten Erfahrungsangaben als Konkretisierung des Betriebsschutzkonzepts an. Die Rechtsstelle hat hierzu noch keinen abschließenden Vermerk erstellt. Wir nehmen Ihre Auffassung, es handele sich um ein eigenständiges Kriterium, zur Kenntnis und werden die Bewertungsunterlagen sichern.' if clinic else 'Nach Auffassung unserer Bearbeitung war Knuff bereits im Angebot benannt. Die Ergänzung betrifft deshalb einen fehlenden Beleg. Wir werden die Uploadhistorie und den genauen Inhalt der Verpflichtung noch einmal abgleichen. Ihre pauschale Annahme, jedes Nachreichen sei ein neues Angebot, teilen wir nicht.')}

Der angekündigte Zuschlag bleibt vorgesehen. Dies ist die ausdrückliche Mitteilung unserer derzeitigen Nichtabhilfe. Ob weitere gesetzliche Hindernisse bestehen, wird vor einer Zuschlagserteilung gesondert geprüft. Bitte richten Sie weitere Nachrichten über den Verfahrenszugang an uns. Die Bereitstellung dieser Nachricht ist am heutigen Tag protokolliert; die Kenntnisnahme wurde um 14:12 Uhr bestätigt.

Mit freundlichen Grüßen
{c['purchaser']}
''',c['refusal']+'T14:05:00+01:00',f'Vergabestelle <vergabe@{c["slug"]}.example>',f'{c["counsel"]} <post@baukanzlei.example>')
    doc(p,'04_Nachpruefungsantrag_Entwurf','Nachprüfungsantrag – Arbeitsentwurf der Bevollmächtigten',f'''
An die Vergabekammer Westfalen bei der Bezirksregierung Münster

{rival}, vertreten durch die Geschäftsführung {c['rival_lead']}, Antragstellerin,
gegen {owner}, {c['address']}, vertreten durch {c['lead']}, Antragsgegnerin.

Verfahren {ref} · {c['lot']} · Bearbeitungsstand {de(c['petition'])}

## 1. Anträge

Die Antragstellerin beantragt, der Antragsgegnerin die Zuschlagserteilung auf der Grundlage der beanstandeten Wertung zu untersagen und sie zu verpflichten, die Prüfung und Wertung unter Beachtung der Rechtsauffassung der Vergabekammer zu wiederholen. Sie beantragt ferner die Einsicht in die zur Wahrnehmung ihrer Rechte erforderlichen Teile der Vergabeakte unter Schutz berechtigter Geschäftsgeheimnisse sowie die Auferlegung der Verfahrenskosten auf die Antragsgegnerin. Die notwendige Hinzuziehung der Bevollmächtigten soll festgestellt werden. Eine unmittelbare Erteilung des Auftrags wird nicht beantragt.

## 2. Interesse am Auftrag und Verfahrensstand

Die Antragstellerin hat ein fristgerechtes Angebot zu {money(total(c,c['rival_multiplier']))} EUR netto abgegeben und hält an ihrem Interesse am Auftrag fest. Die Antragsgegnerin beabsichtigt laut Vorabinformation vom {de(c['notice'])} den Zuschlag an {winner}. Der Gesamtbauwert beträgt nach den Projektunterlagen {money(c['project_net'])} EUR netto. Dass der betrachtete Vertrag ein einzelnes Los betrifft, lässt die erforderliche Gesamtbetrachtung des Bauvorhabens nicht entfallen. Die Einordnung der kommunal beherrschten Gesellschaft nach Paragraf 99 Nummer 2 GWB ist anhand ihrer öffentlichen Aufgabe und der Organisationsunterlagen zu belegen.

Die Antragstellerin erfuhr von dem gerügten Umstand am {de(c['notice'])}. Ihre Rüge vom {de(c['objection'])} und die ausdrückliche Nichtabhilfe vom {de(c['refusal'])} sind beigefügt. Der Entwurf wird vor dem angekündigten Vertragsschluss und innerhalb von 15 Kalendertagen nach Zugang der Nichtabhilfe erstellt. Vor tatsächlicher Einreichung sind Zugangsnachweise und ein zwischenzeitlicher Zuschlag erneut zu prüfen. Eine reine Absendung der Rüge wird nicht mit ihrem Eingang gleichgesetzt.

## 3. Beanstandeter Vergabeverstoß

{('Die Antragsgegnerin hat neben Preis und Betriebsschutzkonzept regionale Baustellenerfahrung berücksichtigt. Das verändert die angekündigte Wertung. Der vollständige bekannt gegebene Kriterienkatalog und der ursprüngliche Wertungsvermerk sind deshalb beizuziehen. Eine interne Bewertungsmethode darf die Zuschlagskriterien oder deren Gewichtung nicht verändern. Dies ist der einschlägige begrenzte Aussagegehalt von EuGH, Urteil vom 14. Juli 2016 – C-6/15, TNS Dimarso, Rn. 27–32 (ECLI:EU:C:2016:555; amtlicher Volltext https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62015CJ0006). Die Entscheidung bedeutet nicht, dass jede interne Unterüberlegung stets vorab veröffentlicht werden muss. Hier wird gerade die Einführung eines eigenständigen, vorher nicht angekündigten Gesichtspunkts beanstandet. Maßgeblich bleiben Paragraf 127 GWB und die für dieses Bauverfahren geltenden Wertungsregeln.' if clinic else 'Zu klären ist, ob die Antragsgegnerin lediglich einen fehlenden Nachweis einer schon benannten und verfügbaren Kapazität ergänzt oder ein nachträglich verändertes Angebot zugelassen hat. Eine Aufklärung darf nicht tatsächlich zur Einreichung eines neuen Angebots führen. Dazu EuGH, Urteil vom 11. Mai 2017 – C-131/16, Archus und Gama, Rn. 27–37 (ECLI:EU:C:2017:358; amtlicher Volltext https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62016CJ0131). Der Ausgangsfall betrifft eine Sektorenvergabe und entscheidet nicht pauschal die Nachforderungsfrage dieses Rohbauauftrags. Hier sind die Voraussetzungen der geltenden VOB/A-EU, insbesondere die Unterscheidung von bereits vorhandenem Nachweis und neu geschaffenem Angebotsinhalt, konkret anzuwenden. Die Antragstellerin muss die Behauptung eines erstmaligen Kapazitätswechsels anhand der einzusehenden Akte erhärten oder korrigieren.')}

## 4. Drohender Schaden und Akteneinsicht

Der beanstandete Vorgang kann die Zuschlagschance unserer Mandantin beeinträchtigen. {('Die Qualitätsbewertung ist wertungsoffen; die Antragstellerin hält ihr Betriebsschutzkonzept für konkurrenzfähig. Sie kann ohne die bekannt gegebene Maßstabsfassung und die Begründung der Einzelpunkte nicht beurteilen, ob die Rangfolge auch bei rechtmäßiger Wertung bestehen bleibt.' if clinic else 'Die Antragstellerin liegt preislich hinter dem vorgesehenen Zuschlagsempfänger. Fehlt diesem eine rechtzeitig vorhandene und erforderliche Kapazität, kann dies ihre eigene Chance verbessern. Ist dagegen nur ein zulässig nachforderbarer Beleg ergänzt worden, trägt diese Beanstandung nicht. Der Antrag stellt die ungeklärte Alternative ausdrücklich dar.')}

Die begehrte Akteneinsicht beschränkt sich auf die entscheidungserheblichen Verfahrens- und Wertungsunterlagen. Die Urkalkulation anderer Bieter wird nicht pauschal verlangt. Geheimnisschutz und wirksamer Rechtsschutz sind für die jeweilige Information abzuwägen; eine vollständige Schwärzung aller tragenden Gründe bedarf einer konkreten Rechtfertigung. EuGH, Urteil vom 17. November 2022 – C-54/21, Antea Polska (ECLI:EU:C:2022:888; amtlicher Volltext https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0054), betrifft diese Abwägung, ersetzt aber nicht die Anwendung von Paragraf 165 GWB.

## 5. Zuschlagssicherung und Anlagen

Wir bitten um unverzügliche Information der Antragsgegnerin über den Antrag nach Paragraf 169 Absatz 1 GWB. Erst die gesetzlich vorgesehene Information durch die Vergabekammer löst das dort geregelte Zuschlagsverbot aus. Der nach dem 1. Juli 2026 begonnene Vorgang ist unter Beachtung des Übergangsrechts zu behandeln. Bei einem Obsiegen der Antragsgegnerin vor der Vergabekammer endet das Verbot in der aktuellen Fassung bereits mit Bekanntgabe der Entscheidung; eine anschließende Beschwerde gegen die Ablehnung hat nicht automatisch aufschiebende Wirkung. Erforderliche weitere Eilmaßnahmen wären deshalb unverzüglich gesondert zu prüfen.

Anlage A1: Teilnahmebedingungen, 01-vergabeunterlagen/04_Teilnahme_und_Wertung.docx.
Anlage A2: Vorabinformation, 02-vergabeverfahren/06_Vorabinformation.pdf.
Anlage A3: Rüge, 04-rechtsschutz/02_Ruege_Entwurf.pdf.
Anlage A4: Nichtabhilfe, 04-rechtsschutz/03_Nichtabhilfe.eml.
Die bisherige Anlage A1 ist nur die interne Ausgangsfassung. Vor Einreichung muss die tatsächlich veröffentlichte Endfassung beigefügt und ihr Inhalt abgeglichen werden. Die Entwurfsanlagen dürfen nicht als vollständiger Zustellungsnachweis bezeichnet werden.

{c['counsel']}
''',de(c['petition']))
    doc(p,'05_Fortgang_Aktennotiz','Kanzleiaktennotiz – Abhilfe, Offenlegung und Rücknahme',f'''
{c['counsel']} · Mandat {rival} · {ref}

## 1. Verfahrensmitteilungen

Nach unserem Kanzleiverlauf wurde der Antrag am {de(c['petition'])} übermittelt. Die Information der Antragsgegnerin durch die Vergabekammer wurde am {de(c['service'])} bestätigt. Dieser Vermerk dokumentiert den Arbeitsablauf der Kanzlei; er ist weder ein gerichtlicher Beschluss noch ein amtlicher Eingangsbeleg. Die Originalübermittlungsnachweise sind in der elektronischen Ausgangsakte zu prüfen. Ein Zuschlag wurde uns bis zu diesem Zeitpunkt nicht gemeldet.

## 2. Erklärung der Vergabestelle

{('Die Vergabestelle sagte die Wiederholung der Qualitätswertung anhand der ursprünglich veröffentlichten Maßstäbe ohne Regionalpunkte zu. Die neue Bewertungsrunde soll durch andere fachkundige Mitarbeiter dokumentiert werden. Eine gesonderte Aufschlüsselung der Betriebsschutzbewertung wurde in nicht vertraulicher Form angekündigt. Die Mandantin erkannte an, dass eine Korrektur nicht automatisch zu ihrem Zuschlag führt.' if clinic else 'Die Vergabestelle legte die ursprüngliche Unternehmensliste in geschwärzter Form vor. Sie enthält Knuff bereits vor Ablauf der Angebotsfrist. Die am 4. Dezember nachgereichte Verpflichtung verweist auf den am 20. November erklärten Leistungsumfang. Die Mandantin verlangte noch die Prüfung, ob die benannte Erfahrung tatsächlich der zu erbringenden Brandwandleistung zugeordnet ist. Die Vergabestelle sagte eine dokumentierte Ergänzung der Eignungsprüfung zu, ohne neue Kapazitäten zuzulassen.')}

## 3. Auftrag der Mandantin

Die Mandantin stimmte am {de(c['withdrawal'])} nach Besprechung der dokumentierten Abhilfe einer Rücknahme des laufenden Nachprüfungsantrags zu. Damit wird keine bestimmte Kostenentscheidung der Vergabekammer behauptet. Gebühren, notwendige Aufwendungen und die Erledigungs- oder Rücknahmefolgen sind anhand der tatsächlichen Verfahrensentscheidung abzurechnen. Es bleibt bei der Forderung, vor einem späteren Zuschlag eine neue, zutreffend begründete Vorabinformation zu erhalten. Etwaige neue selbstständige Verstöße sind gesondert nach Kenntnis und Fristauslöser zu prüfen.

Die Akte enthält keine fingierte gerichtliche Entscheidung. Für eine erneute Bearbeitung im früheren Stadium darf der spätere Ausgang nicht als damals bereits bekannte Tatsache verwendet werden.
''',de(c['withdrawal']))
    p='05-nachtragsmanagement'
    doc(p,'01_Zuschlag_Vertragsbaseline','Zuschlag und verbindlicher Vertragsstand',f'''
{owner} · {c['address']}

An {winner} · {ref}

Sehr geehrte Damen und Herren,

wir nehmen Ihr weiterhin bindendes Angebot für {c['lot']} zu {money(total(c))} EUR netto an. Vertragsgrundlage ist die abschließende veröffentlichte Leistungsfassung U04 mit Berichtigung 01, Ihr unverändertes Preisblatt und die im Angebot bezeichneten Vertragsbedingungen. Der ursprüngliche vorbereitende Stand U03 ist keine zusätzliche Leistungsvorgabe. Die VOB/B wurde mit dem vollständigen Vergabepaket bereitgestellt und nach der im Vertrag bezeichneten Fassung vereinbart. Die Einbeziehung und etwaige Abweichungen sind bei einer konkreten Rechtsfrage am vollständigen Vertrag nachzuvollziehen.

Die neue Vorabinformation wurde nach dokumentierter Korrektur der Prüfung am {de(c['new_notice'])} elektronisch abgesandt. Die Vergabestelle hat vor diesem Zuschlag den Ablauf der Wartefrist und das Fehlen einer fortbestehenden Zuschlagssperre geprüft. Der frühere vorgesehene Zuschlagstermin wurde nicht genutzt. {('Die Geschäftsführung hat die gegenüber dem ursprünglichen Losbudget erforderlichen zusätzlichen 23.200,00 EUR am 4. Januar freigegeben.' if clinic else 'Die aktualisierte Budgetfreigabe bestätigt das unveränderte Rohbaulos und lässt die Mittel für die getrennten Ausbaugewerke unberührt.')}

Der Ausführungsbeginn ist {de(c['start'])}; die Fertigstellung des Loses ist für {de(c['finish'])} vereinbart. Bitte legen Sie den Bauzeitenplan und die benannte Baustellenleitung fristgerecht vor. {c['engineer']} koordiniert fachlich, besitzt aber keine allgemeine Vollmacht zur Beauftragung vergütungspflichtiger Änderungen. Solche Erklärungen sind an die Geschäftsführung zu richten. Die Unterzeichnung eines Aufmaßes bestätigt ohne weitere Erklärung weder Preis noch Anspruchsgrund.

Mit freundlichen Grüßen
{c['lead']}, Geschäftsführung
''',de(c['award']),pdf=True)
    mail(p,'02_Anordnung_Planrevision','Anordnung Planrevision P07 – gesonderte Kostenaufstellung',f'''
{('Sehr geehrter Herr Klinker,' if clinic else 'Sehr geehrte Frau Mörtel,')}

{('wir ordnen die Vertiefung der Fundamente in Achse D bis F gemäß geprüfter Revision P07 an. Die neue Gründungsgeometrie führt nach dem Planeraufmaß zu zusätzlichen 220 Kubikmetern Beton, 34.000 Kilogramm Betonstahl und 920 Quadratmetern Schalung. Die Freigabe betrifft die bezeichnete Änderung. Der Baugrund im betroffenen Bereich wurde neu beurteilt; der konkrete Zusammenhang mit den ursprünglichen Erkundungsangaben wird gesondert dokumentiert.' if clinic else 'wir ordnen die geänderte Ausführung der Brandwand zwischen Treppenhaus und Gebäudeflügel gemäß geprüfter Revision P07 an. Gegenüber dem Vertragsstand sind 140 Quadratmeter Mauerwerk, 44 Kubikmeter Beton und 8.000 Kilogramm Betonstahl zusätzlich vorgesehen. Der Brandschutzplaner hat die Änderung am 2. März freigegeben. Die Entscheidung ist keine bloße Bitte des Bauleiters, sondern wird hier namens der Geschäftsführung erklärt.')}

Bitte legen Sie uns eine nachvollziehbare Darstellung der Mehr- und Minderkosten sowie etwaiger Terminfolgen vor. Eine zusätzliche Bauzeitvergütung oder ein bestimmter Zuschlagssatz wird mit dieser Nachricht nicht anerkannt. Erläutern Sie auch, welche Leistungen aus dem bisherigen Vertrag entfallen. Bereits enthaltene Leistungen dürfen nicht nochmals berechnet werden. Die Vergabestelle prüft parallel die öffentliche Auftragsänderung; die technische Notwendigkeit allein ersetzt diese Prüfung nicht.

Mit freundlichen Grüßen
{c['lead']}
''','2027-03-05T09:40:00+01:00',f'Geschäftsführung <leitung@{c["slug"]}.example>',f'{winner} <bauleitung@{c["slug"]}-bau.example>')
    doc(p,'03_Nachtragsangebot','Nachtragsangebot N01 – geänderte Ausführung',f'''
{winner} · An {owner} · Nachtrag N01 zu {ref}

## 1. Änderungsgegenstand und Abgrenzung

Wir nehmen Bezug auf die Anordnung der Geschäftsführung vom 5. März 2027 und die geprüfte Revision P07. Gegenstand dieses Angebots ist {('die zusätzliche Fundamentvertiefung in Achse D bis F' if clinic else 'die geänderte Brandwand im Bereich des Treppenhauses')}. Die im ursprünglichen Vertrag bereits enthaltenen Mengen bleiben in der Vertragsabrechnung. N01 erfasst ausschließlich die dokumentierte Mehrleistung. Die Aufmaßliste und die Einzelkostenrechnung sind beigefügt. Eine bloße Mengenabweichung bei unverändertem Bauentwurf wird nicht ohne Prüfung mit einer angeordneten Leistungsänderung gleichgesetzt.

## 2. Vergütungsansatz

{('Für Beton setzen wir 220 Kubikmeter zu 268,00 EUR, für Betonstahl 34.000 Kilogramm zu 2,52 EUR und für zusätzliche Schalung 920 Quadratmeter zu 78,00 EUR an. Daraus folgen 58.960,00 EUR, 85.680,00 EUR und 71.760,00 EUR, insgesamt 216.400,00 EUR direkte Mehrkosten.' if clinic else 'Für zusätzliches Mauerwerk setzen wir 140 Quadratmeter zu 186,00 EUR, für Beton 44 Kubikmeter zu 257,00 EUR und für Betonstahl 8.000 Kilogramm zu 2,48 EUR an. Daraus folgen 26.040,00 EUR, 11.308,00 EUR und 19.840,00 EUR, insgesamt 57.188,00 EUR direkte Mehrkosten.')}

Auf diese direkten Kosten beanspruchen wir 8 Prozent allgemeine Geschäftskosten und 5 Prozent Wagnis und Gewinn. Die Prozentsätze sind unsere Angebotsforderung; sie werden nicht als bereits vereinbarte oder gesetzlich feststehende Werte bezeichnet. Baustellengemeinkosten sind in den direkten Ansätzen nur enthalten, soweit sie konkret zugeordnet sind. Zusätzlich angesetzte Vorhaltekosten bedürfen deshalb eines Abgleichs gegen Doppelberechnung. Die maßgebliche rechtliche Berechnungsmethode hängt von Vertrag, Anordnung und Vereinbarung ab; unser Angebot setzt diese Prüfung nicht außer Kraft.

## 3. Terminbehauptung und Unterlagen

Wir machen zunächst zwölf zusätzliche Kalendertage geltend. Im Wochenbericht der heutigen Baubesprechung, der diesem abschließenden Angebot beigefügt ist, sind allerdings nur fünf Tage ausdrücklich der fehlenden Planfreigabe zugeordnet; an zwei Tagen war unsere eigene Schalungskolonne nicht vollständig besetzt. Den Einfluss auf den kritischen Weg und mögliche Überlagerungen werden wir anhand des fortgeschriebenen Terminplans erläutern. Der hier genannte Zeitraum wird nicht zugleich als abschließend bewiesener Entschädigungs- oder Schadensersatzanspruch dargestellt.

Wir bitten um Prüfung und einen Besprechungstermin. Die Freigabe des Aufmaßes soll ausdrücklich von einer Preisvereinbarung getrennt werden. Eine Gesamterledigung weiterer Forderungen bieten wir mit N01 nicht an. Die laufende Vertragsleistung wird im Rahmen der bestehenden Pflichten fortgeführt; gesetzliche oder vertragliche Rechte bei offenen Anordnungs- und Vergütungsfragen bleiben einer gesonderten Prüfung vorbehalten.

{c['director']}
''','12.03.2027')
    doc(p,'05_Bauablauf_Protokoll','Baubesprechung und Wochenbericht 10',f'''
{ref} · Besprechung vom 12. März 2027 · {c['engineer']}, {c['director']}, {c['purchaser']}

## 1. Festgehaltene Ereignisse

Am 1. März fragte die Bauleitung nach der endgültigen Revision der betroffenen Bauteile. Die ursprüngliche vertragliche Planung erlaubte die Ausführung der jetzt geänderten Bauteile so nicht. Am 3. März war der aktualisierte Plan intern abgestimmt, aber noch nicht zur Ausführung freigegeben. Die Geschäftsführung ordnete die Änderung am 5. März an. Der Auftragnehmer meldete am selben Tag eine Behinderung des betroffenen Arbeitsabschnitts. Die Nachricht ging der Projektleitung um 11:26 Uhr zu. Die Arbeiten in zwei anderen Abschnitten liefen weiter.

## 2. Uneinigkeit über die Folgen

Der Auftragnehmer ordnet fünf Tage der fehlenden Planfreigabe zu und verlangt insgesamt zwölf zusätzliche Kalendertage. Die Projektleitung hält den zusätzlichen Zeitraum nicht für ausreichend erklärt. Der Wochenbericht weist außerdem für den 8. und 9. März einen Ausfall eigener Schalungsfachkräfte aus. Die Parteien sind sich nicht einig, ob dieser Ausfall gleichzeitig wirkte oder die durch die Änderung ausgelöste Verschiebung weiter verlängerte. Ein vollständiger Soll-Ist-Abgleich mit Abhängigkeiten und eingesetzten Ressourcen ist noch nicht übergeben.

## 3. Aufmaß und nächste Schritte

Das gemeinsame Aufmaß bestätigt die in N01 benannten zusätzlichen Mengen vorbehaltlich der Kontrolle am tatsächlich ausgeführten Bauteil. Die Unterschriften unter dem Messblatt bestätigen keinen Preis und keinen pauschalen Bauzeitanspruch. Die Projektleitung fordert Lieferbelege, Stundenaufzeichnungen und die Darstellung ersparter Vertragsleistungen. Der Auftragnehmer soll die behaupteten Warte- und Wiederanlaufzeiten getrennt ausweisen. Die Vergabestelle führt die Änderungsliste fort und prüft die einschlägige Ausnahme nach Paragraf 132 GWB einschließlich möglicher Bekanntmachung.

## 4. Abweichende Erinnerung

{c['director']} erinnert eine mündliche Zusage des Planers, „die Mehrkosten seien in Ordnung“. {c['engineer']} bestätigt nur die technische Erforderlichkeit der neuen Geometrie. Beide halten fest, dass die Vergütung in der Besprechung nicht abschließend vereinbart wurde. Das Protokoll geht am 12. März an die Beteiligten. Die fehlende Antwort eines Empfängers wird nicht automatisch als Anerkennung aller streitigen Rechtsfolgen behandelt.
''','12.03.2027')
    mail(p,'07_Pruefantwort','N01: Mengen bestätigt, Preis und Bauzeit noch offen',f'''
Sehr geehrte Damen und Herren,

wir haben Ihre Unterlagen zu N01 geprüft. Die zusätzlich angeordneten Mengen sind nachvollziehbar beschrieben. Bitte reichen Sie die direkten Kostenbelege und die Aufteilung der enthaltenen Baustellengemeinkosten nach. Die geforderten 8 Prozent und 5 Prozent bestätigen wir bisher nicht. Insbesondere benötigen wir die Abgrenzung zu bereits vergüteten Vorhaltepositionen.

Die behaupteten zwölf zusätzlichen Tage erkennen wir auf Grundlage des Wochenberichts nicht an. Bitte legen Sie den fortgeschriebenen Bauzeitenplan mit kritischem Weg und den tatsächlichen Mannschaftsstärken vor. Fünf dokumentierte Wartearbeitstage werden nicht ungeprüft in zwölf anspruchsbegründende Kalendertage umgerechnet. Wir treffen damit noch keine abschließende Entscheidung über einen ausreichend belegten Teilanspruch.

Unsere Bauleitung ist zu einer gemeinsamen Kostenbesprechung am 19. März bereit. Ein vergaberechtlicher Änderungsvermerk und eine etwaige Veröffentlichung werden von der Vergabestelle gesondert bearbeitet. Diese interne Prüfung ersetzt keine Preisvereinbarung mit Ihnen.

Mit freundlichen Grüßen
{c['purchaser']}
''','2027-03-15T14:20:00+01:00',f'Vergabestelle <vergabe@{c["slug"]}.example>',f'{winner} <nachtrag@{c["slug"]}-bau.example>',[f'{p}/05_Bauablauf_Protokoll.docx'])
    doc(p,'08_Abschlagsrechnung','Abschlagsrechnung 03 – Vertragsleistung und offener Nachtrag',f'''
{winner} · Rechnung AR-2027-03 · An {owner}

## 1. Abgerechneter Stand zum 31. März 2027

Die bisher aufgemessene Vertragsleistung beträgt 480.000,00 EUR netto. Bereits vereinnahmte Abschlagszahlungen betragen 300.000,00 EUR netto. Aus der unveränderten Vertragsleistung verbleiben damit 180.000,00 EUR netto. Hinzu kommen 34.200,00 EUR Umsatzsteuer bei dem für diese Rechnung angesetzten Steuersatz von 19 Prozent, mithin 214.200,00 EUR brutto. Die steuerliche Behandlung der konkreten Leistung ist anhand der Unternehmer- und Empfängereigenschaft vor der tatsächlichen Abrechnung zu prüfen; ein Übergang der Steuerschuld wird hier nicht unterstellt.

## 2. Noch nicht abgerechnete Position

N01 wird mit dieser Rechnung nicht zusätzlich gefordert, weil die gemeinsame Leistungsfeststellung noch nicht abgeschlossen ist. Der Nachtrag bleibt in der gesonderten Forderungsliste als streitig vermerkt. Die dort beanspruchten Zuschläge und Bauzeitfolgen werden deshalb weder in die 480.000,00 EUR eingerechnet noch ein zweites Mal als Abschlag angefordert. Die Rechnung enthält keine Erklärung über die endgültige Erledigung des Nachtrags.

## 3. Beleg und Prüfung

Die Vertragsleistung ist durch die positionsbezogenen Aufmaßblätter der Abschlagsprüfung nachzuweisen. Die vorliegende Kurzrechnung ersetzt diese Blätter nicht. Wir bitten um zeitnahe Benennung konkreter Einwendungen und um Zahlung innerhalb der vertraglich und gesetzlich maßgeblichen Frist nach Zugang der prüfbaren Unterlagen. Eine Zahlungserinnerung ohne festgestellten Zugang und Fälligkeit wird noch nicht versandt.

{c['director']}
''','31.03.2027',pdf=True)
    doc(p,'09_Abnahmeprotokoll','Rohbauabnahme – Feststellungen und Vorbehalte',f'''
{owner} und {winner} · {ref}

## 1. Begehung und Erklärung

Die Beteiligten begehen das Rohbaulos am {de(c['finish'])}. Für den Auftraggeber nimmt {c['lead']} teil; die technische Begleitung übernimmt {c['engineer']}. Für den Auftragnehmer nimmt {c['director']} teil. Der Auftraggeber erklärt die Abnahme der besichtigten Rohbauleistung mit den nachfolgenden ausdrücklich festgehaltenen Mängeln. Eine Abnahme der getrennten Ausbau- und Technikgewerke ist damit nicht verbunden.

## 2. Feststellungen

An der Türöffnung im Treppenhaus ist die Sollbreite anhand des freigegebenen Detailplans erneut zu kontrollieren. Zwei dokumentierte Durchführungen fehlen noch in der Revisionsliste. Der Auftragnehmer wird die Unterlagen bis zum 12. November vervollständigen und die geometrische Abweichung bis dahin mit einem prüffähigen Vorschlag bewerten. Die Parteien halten fest, dass die Unvollständigkeit der Revisionsliste keinen Verzicht auf die vereinbarte Dokumentation bewirkt. Die Rechte wegen der bekannten Mängel werden ausdrücklich vorbehalten.

## 3. Offene Vergütung

Der Nachtrag N01 und die behaupteten Bauzeitfolgen bleiben hinsichtlich der noch nicht vereinbarten Positionen streitig. Die Abnahme enthält kein Anerkenntnis der geltend gemachten Zuschlagssätze und keinen Verzicht des Auftragnehmers auf offene Ansprüche. Eine Vertragsstrafe ist im zugrunde gelegten Vertrag nicht vereinbart. Der Schlussrechnungsstand, das Ergebnis der Änderungsprüfung und die Verjährungsfristen sind jeweils gesondert festzustellen; aus diesem Protokoll wird kein pauschaler Schlussstrich unter sämtliche Ansprüche abgeleitet.

{c['lead']} · {c['director']} · {c['engineer']}
''',de(c['finish']))
    return result
