"""Zwei native Vertragsakten zur Anwendung freigegebener Unternehmensplaybooks.

Alle Textfassungen sind eigenständige Aktenoriginale. Bewertungsdaten und
Musterlösungen gehören nicht in die exportierten Arbeitsbestände.
"""


def D(file, title, day, sender, recipient, body, **extra):
    return dict(file=file, title=title, date=day, sender=sender, recipient=recipient, body=body.strip(), **extra)


def E(file, title, day, sender, recipient, body):
    return dict(file=file, title=title, date=day, **{'from': sender, 'to': recipient}, body=body.strip())


def T(code, title, starting, fallback, forbidden):
    return dict(id=code, title=title, starting=starting, fallback=fallback, forbidden=forbidden)


NDA_TOPICS = [
    T('NDA-01', 'Vertrauliche Informationen und Ausnahmen',
      ['Der Vertrag schützt als vertraulich gekennzeichnete Informationen sowie solche, deren Vertraulichkeit nach den Umständen erkennbar ist.', 'Öffentlich bekannte, bereits rechtmäßig bekannte, rechtmäßig von Dritten erhaltene und unabhängig entwickelte Informationen sind ausgenommen.'],
      ['Auch ohne Kennzeichnung mitgeteilte technische Projektinformationen dürfen geschützt sein, wenn der Projektbezug erkennbar ist.', 'Die vier Ausnahmen für Öffentlichkeit, Vorwissen, rechtmäßigen Dritterhalt und unabhängige Entwicklung bleiben erhalten.'],
      ['Der Empfänger muss unabhängig entwickelte Informationen ohne Ausnahme wie Informationen der anderen Partei behandeln.']),
    T('NDA-02', 'Projektzweck und zugelassene Personen',
      ['Die Nutzung ist auf die Prüfung der gemeinsamen Entwicklung des Tischsensors Federlicht beschränkt.', 'Zugang erhalten nur eigene Beschäftigte und beruflich verschwiegene Berater, soweit sie ihn für das Projekt benötigen.'],
      ['Die Nutzung bleibt auf das Projekt Federlicht beschränkt.', 'Benannte externe Fachkräfte dürfen Zugang erhalten, wenn sie vorher gleichwertig zur Vertraulichkeit verpflichtet werden und nur den erforderlichen Teil erhalten.'],
      ['Eine Partei darf Projektinformationen ohne projektbezogene Beschränkung für beliebige eigene Produkte nutzen.']),
    T('NDA-03', 'Dauer der Bindung',
      ['Für gewöhnliche vertrauliche Informationen endet die Pflicht drei Jahre nach Beendigung der Gespräche.', 'Für Geschäftsgeheimnisse dauert der Schutz nur so lange an, wie die gesetzlichen Voraussetzungen ihres Schutzes bestehen.'],
      ['Für gewöhnliche vertrauliche Informationen endet die Pflicht spätestens fünf Jahre nach Beendigung der Gespräche.', 'Für Geschäftsgeheimnisse bleibt der Schutz an die gesetzlichen Schutzvoraussetzungen gebunden.'],
      ['Sämtliche Informationen bleiben ohne zeitliche Begrenzung und ohne Rücksicht auf ihren fortbestehenden Schutzbedarf geheim zu halten.']),
    T('NDA-04', 'Rückgabe und Sicherungskopien',
      ['Produktive Kopien müssen innerhalb von zehn Werktagen nach Aufforderung zurückgegeben oder gelöscht werden.', 'Die tatsächlich eingerichtete technische Konfiguration löscht Sicherungskopien spätestens nach 30 Tagen.'],
      ['Produktive Kopien müssen innerhalb von 20 Werktagen zurückgegeben oder gelöscht werden; gesetzliche Aufbewahrungspflichten und eine gesperrte Belegkopie für die Rechtsverteidigung bleiben zulässig.', 'Sicherungskopien bleiben gesperrt und werden nach der tatsächlich eingerichteten Konfiguration spätestens nach 90 Tagen überschrieben.'],
      ['Die empfangende Partei darf produktive Kopien nach Rückgabeaufforderung zeitlich unbegrenzt frei weiterverwenden.']),
    T('NDA-05', 'Gesetzlich erzwungene Offenlegung',
      ['Der Vertrag gestattet eine gesetzlich oder behördlich zwingende Offenlegung im erforderlichen Umfang.', 'Soweit rechtlich zulässig, ist die offenlegende Partei vorab zu informieren.'],
      ['Zwingende Offenlegungen bleiben erlaubt; eine vorherige Information ist nur geschuldet, soweit sie rechtlich zulässig und praktisch möglich ist.'],
      ['Die empfangende Partei muss auch bei einer vollziehbaren gesetzlichen Offenlegungspflicht schweigen.']),
    T('NDA-06', 'Untersuchung des Prototyps',
      ['Der Vertrag verbietet die Zerlegung und Rückentwicklung überlassener Prototypen.'],
      ['Die Parteien dürfen im Projektplan konkret bezeichnete Tests durchführen; Nachbau, Herauslösen von Firmware und Nutzung außerhalb des Projekts bleiben untersagt.'],
      ['Die empfangende Partei darf den Prototyp ohne Zweckbegrenzung nachbauen und gewonnene Konstruktionsdaten frei verwerten.']),
    T('NDA-07', 'Haftung und Vertragsstrafe',
      ['Der Vertrag enthält keine Vertragsstrafe und lässt die gesetzliche verschuldensabhängige Haftung bestehen.'],
      ['Eine Vertragsstrafe setzt einen schuldhaften wesentlichen Verstoß voraus und ist je Verstoß auf 5.000 EUR begrenzt.', 'Die Vertragsstrafe wird auf einen Schadensersatzanspruch wegen desselben Verstoßes angerechnet.'],
      ['Eine Vertragsstrafe fällt unabhängig von einem Verschulden an.', 'Eine Vertragsstrafe übersteigt für einen einzelnen Verstoß 10.000 EUR.']),
    T('NDA-08', 'Recht und Gerichtsstand',
      ['Es gilt deutsches Recht und für die beiden deutschen Gesellschaften ist Berlin als ausschließlicher Gerichtsstand vereinbart.'],
      ['Es gilt deutsches Recht; anstelle Berlins ist Leipzig als ausschließlicher Gerichtsstand zulässig.'],
      ['Der Vertrag unterliegt ausschließlich dem Recht eines anderen Staates als Deutschland.']),
]

ARB_TOPICS = [
    T('ARB-01', 'Arbeitszeit und Mehrarbeit',
      ['Die regelmäßige Wochenarbeitszeit beträgt 40 Stunden ohne Pausen.', 'Mit dem Monatsgehalt sind höchstens zehn angeordnete oder genehmigte Überstunden pro Monat abgegolten; darüber hinaus ist ein klarer Ausgleich vereinbart.'],
      ['Die regelmäßige Wochenarbeitszeit liegt zwischen 38 und 40 Stunden ohne Pausen.', 'Mit dem Monatsgehalt sind höchstens zehn angeordnete oder genehmigte Überstunden pro Monat abgegolten; darüber hinaus ist ein klarer Ausgleich vereinbart.'],
      ['Jede Mehrarbeit ist ohne zahlenmäßige Grenze mit dem Monatsgehalt abgegolten.']),
    T('ARB-02', 'Arbeitsort und mobiles Arbeiten',
      ['Der regelmäßige Arbeitsort ist das Berliner Büro; mobile Arbeit ist auf einen Tag pro Woche an einem genehmigten Ort innerhalb Deutschlands begrenzt.', 'Der konkret vorgesehene mobile Arbeitsplatz ist tatsächlich gegen die Einsicht Dritter geschützt.'],
      ['Der regelmäßige Arbeitsort bleibt Berlin; bis zu zwei mobile Arbeitstage pro Woche innerhalb Deutschlands sind zulässig und an die geltenden Schutzvorgaben gebunden.', 'Der konkret vorgesehene mobile Arbeitsplatz ist tatsächlich gegen die Einsicht Dritter geschützt.'],
      ['Die Arbeitnehmerin darf ihren dauerhaften Arbeitsort ohne Zustimmung in einen beliebigen Staat verlegen.']),
    T('ARB-03', 'Vergütung und Fälligkeit',
      ['Das feste Bruttomonatsgehalt beträgt höchstens 4.800 EUR und ist zum Monatsende fällig.'],
      ['Das feste Bruttomonatsgehalt beträgt höchstens 5.000 EUR und ist zum Monatsende fällig.'],
      ['Das feste Bruttomonatsgehalt übersteigt ohne neue Budgetfreigabe 5.000 EUR.']),
    T('ARB-04', 'Dauer Probezeit und Kündigung',
      ['Das Arbeitsverhältnis ist unbefristet und eine Probezeit von sechs Monaten mit zweiwöchiger Kündigungsfrist ist vereinbart.', 'Nach der Probezeit gelten die gesetzlichen Kündigungsfristen; die Arbeitgeberin erhält kein pauschales Freistellungsrecht für jede Kündigung.'],
      ['Das Arbeitsverhältnis ist unbefristet und die Probezeit dauert höchstens sechs Monate.', 'Eine Freistellung nach einer Kündigung setzt eine konkrete Interessenabwägung im Einzelfall voraus.'],
      ['Die Arbeitgeberin darf nach jeder Kündigung ohne weitere Voraussetzungen einseitig von der Arbeitspflicht freistellen.']),
    T('ARB-05', 'Vertraulichkeit nach dem Ausscheiden',
      ['Die nachvertragliche Verschwiegenheit ist auf konkret schutzbedürftige Geheimnisse beschränkt; allgemeine berufliche Kenntnisse bleiben nutzbar.', 'Gesetzlich erlaubte Meldungen und Offenlegungen werden nicht untersagt.'],
      ['Die Geheimhaltung nennt hinreichend bestimmte Geheimnisbereiche, endet mit dem Wegfall ihres Schutzbedarfs und lässt berufliche Erfahrung sowie erlaubte Meldungen unberührt.'],
      ['Nach dem Ausscheiden müssen alle jemals bekannt gewordenen internen Vorgänge zeitlich unbegrenzt geheim gehalten werden.']),
    T('ARB-06', 'Ausschlussfristen',
      ['Für die Geltendmachung von Ansprüchen ist mindestens eine dreimonatige Frist in Textform vorgesehen.', 'Die Regelung nimmt gesetzlich unverzichtbare Ansprüche, insbesondere den gesetzlichen Mindestlohn, ausdrücklich aus.'],
      ['Der Vertrag enthält keine vertragliche Ausschlussfrist.'],
      ['Die Ausschlussfrist erfasst ausdrücklich auch Ansprüche auf den gesetzlichen Mindestlohn.']),
    T('ARB-07', 'Nebentätigkeit und Wettbewerb',
      ['Entgeltliche Nebentätigkeiten sind anzuzeigen und dürfen nur bei konkreter Beeinträchtigung berechtigter betrieblicher Interessen untersagt werden.', 'Der Vertrag enthält kein nachvertragliches Wettbewerbsverbot.'],
      ['Für entgeltliche Nebentätigkeiten ist eine Zustimmung vorgesehen, die ohne konkrete entgegenstehende berechtigte Interessen zu erteilen ist.', 'Der Vertrag enthält kein nachvertragliches Wettbewerbsverbot.'],
      ['Jede Nebentätigkeit einschließlich unentgeltlicher privater Tätigkeiten ist ausnahmslos verboten.']),
    T('ARB-08', 'Fortbildung',
      ['Die Arbeitgeberin stellt pro Kalenderjahr zwei bezahlte Fortbildungstage für arbeitsbezogene und vorab abgestimmte Veranstaltungen zur Verfügung.'],
      ['Die Arbeitgeberin stellt pro Kalenderjahr einen bezahlten Fortbildungstag für eine arbeitsbezogene und vorab abgestimmte Veranstaltung zur Verfügung.'],
      ['Die Arbeitnehmerin muss jede betrieblich angeordnete Fortbildung unbezahlt außerhalb der Arbeitszeit absolvieren.']),
]


def playbook_body(identifier, version, company, scope, topics, specifics):
    lines = [f'## 1 Auftrag und Geltung',
             f'{company} verwendet dieses Playbook {identifier}, Version {version}, für {scope}. Die Geschäftsführung hat diese Fassung am 14. September 2026 freigegeben. Zuständig für Abweichungsentscheidungen ist die Geschäftsführerin; die Fachabteilung darf Rückfragen beantworten und Vorschläge machen, aber keine roten Linien aufheben.',
             'Der Ausgangspunkt ist die Startposition (S). Eine Rückfallposition (F1) ist ein zulässiger Verhandlungskompromiss und bedarf der in der Freigabe genannten Zustimmung. Die Position N bezeichnet nicht akzeptable Bedingungen. Bei S und F1 müssen alle zugehörigen Regeln erfüllt sein. Jede einzelne erkannte Bedingung einer N-Position ist eine rote Linie; mehrere dort genannte Bedingungen müssen nicht zusammen vorliegen.',
             'Die Regelkennungen bleiben bei einer bloßen Textpflege unverändert. Geprüft wird jede Regel anhand der maßgeblichen Vertragsfassung und ihrer einbezogenen Anlagen. Tatsächliche Voraussetzungen werden nur anhand der dazugehörigen Belege festgestellt. Fehlt ein Beleg, ist die Regel nicht verifizierbar. Ein im gesamten maßgeblichen Vertrag fehlendes Thema ist als nicht gefunden auszuweisen und darf nicht aus einer älteren Fassung ergänzt werden.',
             'Die Auswertung nennt je Regel die Fundstelle mit Dateiname, Abschnitt und kurzem wörtlichem Ausschnitt. Bei zulässigen Positionen lautet das Ergebnis erfüllt oder nicht erfüllt; bei N lautet es erkannt oder nicht erkannt. Nicht verifizierbare Regeln stehen gesondert neben der Erfüllt-Zahl und zählen nicht zu deren Nenner. Die wörtliche Trefferzahl einer N-Position wird nicht umgekehrt. Eine erkannte rote Linie führt für das Thema zu hohem Risiko. Eine vollständig erfüllte Startposition ohne rote Linie hat kein Playbook-Risiko; eine vollständig erfüllte Rückfallposition hat mittleres Risiko. Andere Abweichungen und verbleibende Tatsachenlücken sind mit ihrem konkreten Grund auszuweisen; ungeklärte Tatsachen sind kein positiver Nachweis.',
             specifics,
             'Diese Regeln sind Unternehmenspositionen und keine Aussage darüber, dass eine Klausel gesetzlich erlaubt oder unwirksam ist. Die rechtliche Prüfung, insbesondere zwingendes Recht und die Kontrolle vorformulierter Vertragsbedingungen, erfolgt getrennt. Eine interne Freigabe ersetzt diese Prüfung nicht. Der Bericht und ein Änderungsvorschlag bleiben intern; ein Versand oder Vertragsschluss benötigt einen gesonderten Auftrag.']
    for i, t in enumerate(topics, 2):
        lines.append(f'## {i} {t["title"]}')
        lines.append(f'Thema {t["id"]}. Die nachstehenden Bedingungen gelten ausschließlich für dieses Thema.')
        for suffix, label, key in [('S', 'Startposition', 'starting'), ('F1', 'Rückfallposition', 'fallback'), ('N', 'Nicht akzeptable Position', 'forbidden')]:
            lines.append(f'{label} {t["id"]}-{suffix}.')
            for r, text in enumerate(t[key], 1):
                lines.append(f'{t["id"]}-{suffix}-R{r}: {text}')
    return '\n\n'.join(lines)


KF = 'Kupferfink Sensorik GmbH\nMina Kupfer, Geschäftsführerin\nWerkhof 12, 13357 Berlin\nmina@kupferfink.example'
LB = 'Lindenbogen Design GmbH\nSeverin Bock, Geschäftsführer\nAteliergasse 7, 04107 Leipzig\nseverin@lindenbogen.example'
KANZLEI = 'Rechtsanwältin Clara Klee\nKanzlei Klee und Kolben\nBüro am Kanal 9, 10999 Berlin\nclara@klee-kolben.example'
NDA_CURRENT = '''## 1 Parteien und Projekt

Die Kupferfink Sensorik GmbH, Werkhof 12, 13357 Berlin, vertreten durch ihre Geschäftsführerin Mina Kupfer, und die Lindenbogen Design GmbH, Ateliergasse 7, 04107 Leipzig, vertreten durch ihren Geschäftsführer Severin Bock, wollen die gemeinsame Entwicklung des Tischsensors Federlicht prüfen. Der Sensor soll Berührungen und die Ausrichtung eines Gegenstands auf einer Arbeitsfläche erkennen. Jede Partei kann im Verlauf der Gespräche sowohl Informationen offenlegen als auch empfangen. Diese Vereinbarung verpflichtet beide Parteien in gleicher Weise.

## 2 Vertrauliche Informationen

Vertraulich sind mitgeteilte technische und kaufmännische Informationen, die als vertraulich gekennzeichnet sind oder deren Vertraulichkeit nach den Umständen erkennbar ist. Dazu gehören insbesondere die überlassenen Schaltungsunterlagen, Messdaten, Gehäuseentwürfe und nicht veröffentlichten Kalkulationen zum Projekt Federlicht. Die empfangende Partei behandelt solche Informationen mit derselben Sorgfalt wie eigene vergleichbare Geheimnisse, mindestens jedoch mit angemessener Sorgfalt.

Nicht vertraulich sind Informationen, die bereits öffentlich bekannt sind oder ohne Vertragsverletzung öffentlich werden, der empfangenden Partei nachweislich schon rechtmäßig bekannt waren, ihr ohne Geheimhaltungsbruch rechtmäßig von Dritten zugehen oder von ihr unabhängig ohne Verwendung der vertraulichen Informationen entwickelt werden. Die empfangende Partei legt auf begründete Nachfrage die Umstände der jeweils beanspruchten Ausnahme dar.

## 3 Zweck und Personen

Die Informationen dürfen ausschließlich zur Prüfung der gemeinsamen Entwicklung des Tischsensors Federlicht verwendet werden. Zugang erhalten eigene Beschäftigte sowie beruflich zur Verschwiegenheit verpflichtete rechtliche und steuerliche Berater, soweit sie die Informationen für diesen Zweck benötigen. Die Parteien informieren ihre Beschäftigten über diese Pflicht und beschränken den Zugriff auf den erforderlichen Umfang. Besondere Zugangsrechte nach Anlage 1 bleiben unberührt.

## 4 Prototypen und Rechte

Mit der Offenlegung werden weder Patente noch Urheberrechte oder sonstige Nutzungsrechte übertragen. Eine Partei darf die überlassenen Prototypen ohne Zustimmung der anderen Partei weder zerlegen noch rückentwickeln. Die ausdrücklich in Anlage 1 vereinbarten Untersuchungen sind davon ausgenommen. Ein Anspruch auf Abschluss eines Entwicklungs- oder Liefervertrags entsteht nicht. Keine Partei schuldet aufgrund dieser Vereinbarung eine Vergütung oder die Überlassung weiterer Informationen.

## 5 Dauer

Diese Vereinbarung gilt ab Unterzeichnung. Jede Partei kann die Gespräche in Textform beenden. Die Pflicht zur Geheimhaltung gewöhnlicher vertraulicher Informationen endet fünf Jahre nach dem Zugang dieser Erklärung. Für Informationen, die Geschäftsgeheimnisse sind, dauert der Schutz darüber hinaus nur so lange an, wie die gesetzlichen Voraussetzungen des Geschäftsgeheimnisschutzes bestehen. Die vorstehend geregelten Ausnahmen bleiben während der gesamten Dauer anwendbar.

## 6 Rückgabe und Löschung

Nach einer Aufforderung in Textform gibt die empfangende Partei überlassene Unterlagen und Prototypen innerhalb von 20 Werktagen zurück und löscht produktive elektronische Kopien. Gesetzlich aufzubewahrende Unterlagen und eine gesperrte Belegkopie für die Rechtsverteidigung dürfen für den jeweils erforderlichen Zeitraum aufbewahrt werden. Aufbewahrte Informationen dürfen nur für diesen Zweck verwendet werden und bleiben geschützt.

Automatisch erzeugte Sicherungskopien sind vom produktiven Zugriff zu sperren und im gewöhnlichen Sicherungszyklus spätestens nach 90 Tagen zu überschreiben. Bis dahin dürfen sie ausschließlich zur Wiederherstellung nach einem technischen Ausfall verwendet werden. Wiederhergestellte vertrauliche Informationen sind anschließend erneut nach dieser Vereinbarung zu behandeln. Die empfangende Partei bestätigt die Erledigung auf Nachfrage in Textform.

## 7 Vertragsstrafe und Haftung

Für jeden Verstoß gegen die Geheimhaltungs- oder Nutzungsbeschränkung zahlt die verletzende Partei der anderen Partei eine Vertragsstrafe von 25.000 EUR. Die Vertragsstrafe fällt unabhängig von einem Verschulden an. Ein weitergehender Schadensersatzanspruch bleibt bestehen; die Vertragsstrafe wird auf einen solchen Anspruch wegen desselben Verstoßes angerechnet. Im Übrigen gelten die gesetzlichen Haftungsregelungen.

## 8 Schlussbestimmungen

Es gilt deutsches Recht. Ausschließlicher Gerichtsstand für Streitigkeiten zwischen den beiden Gesellschaften ist Berlin. Anlage 1 mit der Kennung FED-AN1 und dem Stand 25. September 2026 ist Bestandteil dieser Vereinbarung. Soweit sie zu den Abschnitten 3 und 4 abweichende konkrete Regelungen trifft, geht sie vor; im Übrigen bleibt diese Vereinbarung unverändert. Änderungen bedürfen einer Vereinbarung beider Parteien. Gesetzliche Formvorschriften bleiben unberührt.

## 9 Unterzeichnung

Diese Fassung ist ein noch nicht unterzeichneter Entwurf vom 25. September 2026. Als Unterschriftsberechtigte sind für Kupferfink Sensorik GmbH Mina Kupfer und für Lindenbogen Design GmbH Severin Bock vorgesehen. Die Unterzeichnung soll nach Abschluss der Vertragsprüfung in zwei gleichlautenden Exemplaren erfolgen.'''

NDA_OLD = NDA_CURRENT.replace('25. September 2026', '18. September 2026').replace('Anlage 1 mit der Kennung FED-AN1 und dem Stand 18. September 2026 ist Bestandteil dieser Vereinbarung. Soweit sie zu den Abschnitten 3 und 4 abweichende konkrete Regelungen trifft, geht sie vor; im Übrigen bleibt diese Vereinbarung unverändert.', 'Anlagen sind mit dieser ersten Fassung noch nicht vereinbart.').replace('Besondere Zugangsrechte nach Anlage 1 bleiben unberührt.', '').replace('Die ausdrücklich in Anlage 1 vereinbarten Untersuchungen sind davon ausgenommen.', '').replace('fünf Jahre', 'drei Jahre').replace('Für jeden Verstoß gegen die Geheimhaltungs- oder Nutzungsbeschränkung zahlt die verletzende Partei der anderen Partei eine Vertragsstrafe von 25.000 EUR. Die Vertragsstrafe fällt unabhängig von einem Verschulden an. Ein weitergehender Schadensersatzanspruch bleibt bestehen; die Vertragsstrafe wird auf einen solchen Anspruch wegen desselben Verstoßes angerechnet. Im Übrigen gelten die gesetzlichen Haftungsregelungen.', 'Für eine schuldhafte Verletzung dieser Vereinbarung gelten die gesetzlichen Haftungsregeln. Eine Vertragsstrafe ist nicht vereinbart.').replace('## 8 Schlussbestimmungen', '## 8 Gesetzlich erforderliche Offenlegung\n\nGesetzlich oder behördlich zwingend erforderliche Offenlegungen sind im erforderlichen Umfang erlaubt. Soweit rechtlich zulässig, informiert die empfangende Partei die andere Partei vorab und unterstützt angemessene Schutzmaßnahmen.\n\n## 9 Schlussbestimmungen').replace('## 9 Unterzeichnung', '## 10 Unterzeichnung')

nda_docs = [
 E('01_Auftrag_Vertragspruefung.eml', 'Federlicht bitte anhand unseres freigegebenen Playbooks prüfen', '2026-09-28T09:10:00+02:00', 'Mina Kupfer <mina@kupferfink.example>', 'Clara Klee <clara@klee-kolben.example>', '''Guten Morgen Frau Klee,

bitte prüfen Sie den NDA-Entwurf vom 25. September einschließlich der Anlage FED-AN1 gegen unser Playbook PB-KF-NDA in der freigegebenen Version 1.2. Die Fassung vom 18. September liegt nur zur Einordnung im Vorgang und ist nicht mehr unsere Verhandlungsgrundlage. Bisher ist nichts unterschrieben und es wurden noch keine vertraulichen Schaltungen übertragen.

Ich brauche eine übersichtliche Auswertung nach den acht Themen, mit jeder einzelnen Regel, dem tatsächlich gefundenen Text und einer kurzen Begründung. Bitte unterscheiden Sie unsere Wunschpositionen von rechtlichen Bedenken. Wenn Unterlagen fehlen, stellen Sie die konkrete Rückfrage. Legen Sie außerdem einen vollständig formulierten Änderungsvorschlag und eine kurze Begleitmail vor, beides zunächst nur für mich.

Unser gemeinsamer Termin ist am 2. Oktober um 14 Uhr. Bis dahin genügt mir die interne Fassung. Die Technik darf Fragen beantworten, aber keine Vertragsabweichungen freigeben. Bitte senden Sie nichts direkt an Lindenbogen.

Freundliche Grüße
Mina Kupfer'''),
 D('02_Playbook_NDA_V1_2.docx', 'Verhandlungspositionen für die Geheimhaltungsvereinbarung Federlicht', '14.09.2026', KF, 'Rechtsabteilung und Projektleitung', playbook_body('PB-KF-NDA', '1.2', 'Kupferfink Sensorik GmbH', 'gegenseitige Geheimhaltungsvereinbarungen für die Designkooperation Federlicht', NDA_TOPICS, 'Sicherungskopien sind der einzige zusätzliche technische Tatsachenpunkt dieser Fassung. Die vertraglich zugesagte Frist und die tatsächlich eingerichtete Frist sind getrennt zu prüfen. Eine unverbindliche Erinnerung aus einem Gespräch ersetzt keine Bestätigung der IT.')),
 E('03_Freigabe_Playbook.eml', 'Freigabe PB-KF-NDA Version 1.2', '2026-09-14T16:20:00+02:00', 'Mina Kupfer <mina@kupferfink.example>', 'Clara Klee <clara@klee-kolben.example>', '''Guten Tag Frau Klee,

anbei gebe ich unser Playbook PB-KF-NDA in der Version 1.2 für Federlicht frei. Es ersetzt die intern diskutierte Version 1.1. Die Nummern der Regeln sind verbindlich; bitte führen Sie sie im Bericht mit.

Vollständig erfüllte Startpositionen können Sie als innerhalb unseres Standards einordnen. Rückfallpositionen möchte ich im kurzen Abschlussvermerk ausdrücklich sehen; deren Annahme entscheide ich selbst. Jede einzelne erkannte Bedingung unter einer nicht akzeptablen Position muss zu mir zurück. Auch ein Kompromiss bleibt gesondert rechtlich zu prüfen. Bitte verändern Sie das Playbook während der Vertragsprüfung nicht stillschweigend.

Viele Grüße
Mina Kupfer'''),
 D('04_NDA_Entwurf_25_September.docx', 'Gegenseitige Geheimhaltungsvereinbarung Federlicht', '25.09.2026', LB, KF, NDA_CURRENT, reference='LB-FED-NDA-02 | nicht unterzeichnet'),
 D('05_NDA_Altstand_18_September.docx', 'Frühere Fassung der Geheimhaltungsvereinbarung Federlicht', '18.09.2026', LB, KF, 'Diese frühere Fassung wurde am 25. September 2026 ersetzt und wird nur im Verlauf aufbewahrt.\n\n' + NDA_OLD, reference='LB-FED-NDA-01 | überholt'),
 D('06_Anlage_FED_AN1.docx', 'Anlage 1 zum Projekt Federlicht', '25.09.2026', LB, KF, '''## 1 Bezug und Rang

Diese Anlage FED-AN1 gehört zum NDA-Entwurf LB-FED-NDA-02 vom 25. September 2026. Sie wird gemeinsam mit ihm unterzeichnet. Für die nachstehenden konkreten Fragen geht sie den Abschnitten 3 und 4 des NDA vor. Alle anderen Regelungen des NDA bleiben unberührt. Die Anlage ist bisher nicht unterzeichnet.

## 2 Externe Fachkraft

Lindenbogen darf die selbstständige Messingenieurin Olga Kern in das Projekt einbeziehen. Vor dem ersten Zugang muss Lindenbogen sie schriftlich mindestens in gleichem Umfang zur Geheimhaltung und Zweckbindung verpflichten. Olga Kern erhält nur die für ihre Messaufgabe erforderlichen Ansichten und Messdaten. Sie darf keine weiteren Personen hinzuziehen. Lindenbogen bleibt für die ordnungsgemäße Einbeziehung verantwortlich.

## 3 Gestattete Untersuchungen

Lindenbogen und Olga Kern dürfen das abnehmbare, ausdrücklich als Wartungsdeckel gekennzeichnete Gehäuseteil öffnen, die Abmessungen der sichtbaren Halterungen messen und einen Temperaturtest des geschlossenen Geräts von 10 bis 35 Grad Celsius durchführen. Das Auslesen oder Herauslösen von Firmware, das Ablösen von Vergussmaterial und die Rekonstruktion der Schaltung sind nicht gestattet. Ein Nachbau und jede Verwertung der Erkenntnisse außerhalb der Prüfung der gemeinsamen Entwicklung Federlicht bleiben untersagt.

## 4 Organisation

Die Untersuchungen finden im Leipziger Messraum von Lindenbogen statt. Es werden keine Personenaufnahmen angefertigt. Das Gerät bleibt während der Untersuchungen ausgeschaltet, soweit die Temperaturmessung keine Versorgung erfordert. Vor dem Versand stimmen die Projektleitungen den Termin ab.''', reference='FED-AN1'),
 E('07_Versand_Gegnerentwurf.eml', 'Federlicht aktuelle Entwürfe vom 25. September', '2026-09-25T17:25:00+02:00', 'Severin Bock <severin@lindenbogen.example>', 'Mina Kupfer <mina@kupferfink.example>', '''Hallo Frau Kupfer,

anbei die neue vollständige Fassung des NDA und die Anlage FED-AN1. Bitte betrachten Sie nur diese beiden Dateien als unser aktuelles Angebot. Die Anlage regelt die Messaufgabe von Frau Kern genauer. Der alte Text vom 18. September ist überholt.

Unsere Geschäftsführung möchte den neuen Abschnitt zur Vertragsstrafe beibehalten. Über die Höhe können wir sprechen. Für normale Projektinformationen haben wir nun fünf Jahre vorgesehen. Ein Vertragsabschluss ist mit dieser Mail nicht erklärt; wir wollen die abgestimmten Fassungen gemeinsam unterschreiben.

Freundliche Grüße
Severin Bock'''),
 D('08_Projektblatt_Federlicht.docx', 'Projekt Federlicht und der erste Datenaustausch', '21.09.2026', KF, 'Projektablage Federlicht', '''## 1 Vorhaben

Kupferfink entwickelt eine kleine Sensorplatine für die Arbeitsfläche einer Montagehilfe. Lindenbogen soll prüfen, ob ein robustes, gut zu reinigendes Gehäuse hergestellt werden kann. Die erste gemeinsame Phase betrifft ausschließlich die Machbarkeit. Eine Serienlieferung und eine exklusive Zusammenarbeit sind noch nicht vereinbart.

## 2 Geplante Unterlagen

Nach Unterzeichnung des NDA sollen das CAD-Modell des Gehäuses, ein vereinfachter Montageplan und drei Messreihen über einen geschützten Projektraum ausgetauscht werden. Die vollständige Schaltung und der Quellcode verbleiben vorerst bei Kupferfink. Die Dateien werden mit Projektkennung und einem Vertraulichkeitsvermerk versehen. Leserechte werden einzeln erteilt und protokolliert.

## 3 Zuständigkeiten

Mina Kupfer entscheidet über Vertragspositionen. Hartmut Fink betreut die Hardware bei Kupferfink. Bei Lindenbogen koordiniert Severin Bock das Projekt; Olga Kern soll die benannten Messungen übernehmen. Ein Auftrag an Olga Kern und ihre Verpflichtungserklärung liegen Kupferfink noch nicht vor. Die Projektleitung wird vor dem ersten Zugang danach fragen.

## 4 Termin

Ein erster Prototyp kann frühestens am 12. Oktober 2026 versandt werden. Es gibt keinen sachlichen Grund, das Gerät vor Abschluss der Prüfung zu verschicken. Eine Entscheidung über den weitergehenden Entwicklungsvertrag soll erst nach Auswertung der Messungen fallen.'''),
 D('09_Zugriffsplan.docx', 'Geplante Zugriffe im Projektraum Federlicht', '24.09.2026', 'Hartmut Fink\nHardwareentwicklung Kupferfink\nhartmut@kupferfink.example', 'Mina Kupfer', '''## 1 Einrichtung

Für den Projektraum FED ist eine getrennte Gruppe geplant. Mina Kupfer und Hartmut Fink erhalten Verwaltungsrechte; Severin Bock soll Leserechte auf Gehäusemodell und Messreihen erhalten. Ein Download des Quellcodes ist nicht vorgesehen. Der Projektraum ist noch nicht geöffnet und enthält derzeit nur öffentliche Produktfotos.

## 2 Externer Zugang

Olga Kern soll nach Vorlage ihrer Verpflichtungserklärung eine persönliche zeitlich begrenzte Kennung erhalten. Eine Sammelkennung für das gesamte Atelier ist nicht vorgesehen. Jede Vergabe und Sperrung wird im Zugriffsprotokoll erfasst. Die Messingenieurin erhält nur die in der Anlage FED-AN1 genannten Daten.

## 3 Offener technischer Punkt

Für Sicherungskopien gilt der Zyklus des jeweiligen Unternehmensservers. Kupferfink kann die Einstellung bei Lindenbogen nicht selbst einsehen. Hartmut Fink hat bislang weder einen Administrationsauszug noch eine schriftliche Bestätigung erhalten. Die Projektleitung darf deshalb keine bestimmte tatsächliche Löschfrist zusichern.'''),
 D('10_Notiz_Sicherungskopien.docx', 'Telefonnotiz zu den Sicherungskopien bei Lindenbogen', '24.09.2026', 'Hartmut Fink\nhartmut@kupferfink.example', 'Mina Kupfer', '''Ich habe heute um 11.20 Uhr mit Herrn Bock über die technische Ablage gesprochen. Er erinnerte sich an einen älteren Sicherungsplan mit einer Frist von 30 Tagen. Er sagte ausdrücklich, dass er seit dem Serverwechsel im August keinen Zugang zu den Einstellungen hat. Die Administratorin Petra Ebert ist bis zum 29. September abwesend.

Ich habe um eine schriftliche Bestätigung nach ihrer Rückkehr gebeten. Eine solche Bestätigung liegt noch nicht vor. Ich konnte auch nicht klären, ob die alten Monatsstände auf einem gesonderten Datenträger weitergeführt werden. Über die vertragliche Obergrenze von 90 Tagen haben wir keine neue Vereinbarung getroffen.

Die Erinnerung an 30 Tage soll nicht als verbindliche technische Auskunft in die Vertragsfassung übernommen werden. Herr Bock will den administrativen Stand gesondert nachreichen.'''),
 E('11_Rueckfrage_Technik.eml', 'Sicherungskopien bitte noch offen lassen', '2026-09-28T10:05:00+02:00', 'Severin Bock <severin@lindenbogen.example>', 'Hartmut Fink <hartmut@kupferfink.example>', '''Hallo Herr Fink,

bitte korrigieren Sie unsere Gesprächsnotiz nicht auf 30 Tage. Ich habe dazu nur eine alte Erinnerung. Auf einem Zettel steht zudem etwas von 60 Tagen nach dem Serverwechsel; ich kann weder die Herkunft noch die derzeitige Einstellung bestätigen. Petra muss das prüfen.

Die im NDA zugesagten höchstens 90 Tage bleiben unser Vertragsvorschlag. Wie wir das technisch belegen, reiche ich nach. Derzeit habe ich weder einen Export der Einstellungen noch eine belastbare Bestätigung. Bitte führen Sie die tatsächliche Sicherungsfrist noch als offen.

Viele Grüße
Severin Bock'''),
 D('12_Besprechungsnotiz_Verhandlung.docx', 'Vorbereitung des Gesprächs über Federlicht', '28.09.2026', KF, 'Clara Klee', '''## 1 Gewünschtes Ergebnis

Mina Kupfer möchte eine kurze, beidseitige Geheimhaltungsvereinbarung ohne wirtschaftliche Bindung an einen späteren Auftrag. Der Termin am 2. Oktober dient der Klärung des Texts; unterschrieben wird nur eine abgestimmte Endfassung.

## 2 Persönliche Verhandlungspräferenzen

Fünf Jahre für normale Projektunterlagen wären für Mina akzeptabel, wenn im Bericht erkennbar bleibt, dass dies von ihrer Startposition abweicht. Die besondere Messaufgabe von Olga Kern ist sachlich nötig. Die Projektleitung soll aber keine Erlaubnis zum Nachbau erteilen. Ein vollständiger Wechsel zum Vertragsmuster von Kupferfink ist nicht gewünscht; die vorhandene Struktur kann bleiben.

## 3 Noch zu klären

Zur Vertragsstrafe möchte Mina einen konkreten Änderungsvorschlag. Sie hat dazu noch keine Ausnahme freigegeben. Für die Sicherungskopien soll Petra Ebert eine schriftliche Auskunft geben. Das weitere Vorgehen mit Behördenanfragen wurde im Gespräch nicht angesprochen. Frau Klee soll den gesamten Vertrag dennoch anhand aller Playbookregeln prüfen, auch wenn ein Thema beim Verhandlungsgespräch nicht vorkam.'''),
 E('13_Interne_Nachverhandlung.eml', 'Bitte die Anlage nicht versehentlich entfernen', '2026-09-29T08:30:00+02:00', 'Mina Kupfer <mina@kupferfink.example>', 'Clara Klee <clara@klee-kolben.example>', '''Guten Morgen Frau Klee,

mir ist wichtig, dass der Zugriff von Frau Kern und die begrenzten Messungen in der Anlage erhalten bleiben. Das ist keine allgemeine Freigabe unserer Technik, sondern der Grund für die Kooperation. Bitte zeigen Sie eine Fassung, mit der wir weiterverhandeln können.

Eine neue Freigabe der Vertragsstrafe gibt es nicht. Ich habe auch nicht zugestimmt, aus dem technischen Vermerk eine garantierte Löschfrist von 30 Tagen zu machen. Wenn bis zu Ihrer Prüfung keine Bestätigung da ist, lassen Sie die Tatsachenfrage offen und formulieren Sie mir eine kurze Rückfrage.

Danke und freundliche Grüße
Mina Kupfer'''),
 E('14_Terminbestaetigung.eml', 'Gespräch am 2. Oktober um 14 Uhr', '2026-09-29T12:15:00+02:00', 'Severin Bock <severin@lindenbogen.example>', 'Mina Kupfer <mina@kupferfink.example>', '''Guten Tag Frau Kupfer,

der Termin am 2. Oktober um 14 Uhr passt. Wir sprechen über Ihre Anmerkungen zur Fassung vom 25. September und zur Anlage desselben Tages. Weitere Anlagen oder Einkaufsbedingungen gehören nicht zum NDA.

Petra kann die Sicherungseinstellungen diese Woche voraussichtlich noch prüfen; eine belastbare Antwort habe ich bisher nicht. Falls diese erst nach dem Termin vorliegt, können wir den technischen Nachweis gesondert nachhalten. Bitte schicken Sie vor dem Gespräch nur eine von Ihnen freigegebene Fassung.

Freundliche Grüße
Severin Bock'''),
 dict(file='15_Projektchat.txt', title='Chatverlauf Projekt Federlicht', date='29.09.2026', body='''Kanal: Federlicht intern. Export durch Mina Kupfer am 29. September 2026 um 16.40 Uhr.

28.09.2026 10:18 | Hartmut Fink: Ich habe die 30 Tage aus meiner Gesprächsnotiz nicht als Zusage eingetragen. Die neue Mail sagt ja ausdrücklich, dass es noch offen ist.
28.09.2026 10:24 | Mina Kupfer: Gut. Bitte bis zur Unterschrift keine Schaltungsdaten hochladen.
28.09.2026 10:27 | Hartmut Fink: Ist so eingerichtet. Im Raum liegen nur die öffentlichen Fotos vom alten Gehäuse.
29.09.2026 09:04 | Mina Kupfer: Für Frau Kern brauchen wir den begrenzten Zugang. Die Rechtsprüfung soll nicht aus Versehen die Messaufgabe streichen.
29.09.2026 09:11 | Hartmut Fink: Verstanden. Firmware und Verguss bleiben tabu; den Wartungsdeckel muss sie öffnen dürfen.
29.09.2026 16:33 | Mina Kupfer: Den neuen NDA hat noch niemand unterschrieben. Die Änderungsvorschläge gehen erst zu mir.'''),
]

SP = 'Spreebogen Produktstudio GmbH\nFrieda Fröhlich, Geschäftsführerin\nUferwerk 18, 12435 Berlin\nfrieda@spreebogen.example'
NA = 'Nora Aydin\nKiefernweg 23, 12055 Berlin\nnora@postfach.example'
ARB_CURRENT = '''## 1 Vertragsparteien und Beginn

Die Spreebogen Produktstudio GmbH, Uferwerk 18, 12435 Berlin, vertreten durch ihre Geschäftsführerin Frieda Fröhlich, und Frau Nora Aydin, Kiefernweg 23, 12055 Berlin, schließen folgenden Arbeitsvertrag. Das Arbeitsverhältnis beginnt am 1. November 2026 und wird auf unbestimmte Zeit geschlossen. Es ist kein kalendermäßiges oder zweckgebundenes Ende vereinbart.

## 2 Tätigkeit und Arbeitsort

Frau Aydin wird als Produktdesignerin beschäftigt. Ihre Tätigkeit umfasst die Entwicklung von Bedienoberflächen, die Erstellung von Prototypen sowie die Abstimmung mit Entwicklung und Kundenbetreuung. Die Arbeitgeberin darf ihr unter Berücksichtigung ihrer Interessen andere gleichwertige und zumutbare Aufgaben übertragen. Der regelmäßige Arbeitsort ist das Büro Uferwerk 18 in Berlin. Ergänzend gilt die Anlage Mobiles Arbeiten und Arbeitszeit vom 28. September 2026.

## 3 Arbeitszeit und Mehrarbeit

Die regelmäßige Arbeitszeit beträgt 40 Stunden pro Woche ohne Ruhepausen und verteilt sich grundsätzlich auf Montag bis Freitag. Die Lage der täglichen Arbeitszeit wird unter Beachtung der gesetzlichen Ruhepausen und Ruhezeiten betrieblich abgestimmt. Beginn, Ende und Dauer der täglichen Arbeit sowie Pausen werden im betrieblichen Zeiterfassungssystem dokumentiert; dies gilt auch bei mobiler Arbeit.

Überstunden bedürfen einer vorherigen Anordnung oder Genehmigung durch die Teamleitung. Mit dem Monatsgehalt sind bis zu zehn solcher Überstunden je Kalendermonat abgegolten. Weitere angeordnete oder genehmigte Überstunden werden innerhalb der folgenden drei Monate durch entsprechende bezahlte Freizeit ausgeglichen. Ist dies aus betrieblichen Gründen nicht möglich, werden sie mit dem auf eine Arbeitsstunde entfallenden Anteil des festen Monatsgehalts vergütet. Eine Verpflichtung zur Mehrarbeit besteht nur im gesetzlich zulässigen und im Einzelfall zumutbaren Umfang. Die Aufzeichnung von Arbeitszeit begründet für sich allein keine Genehmigung von Mehrarbeit.

## 4 Vergütung

Die Arbeitnehmerin erhält ein festes Bruttomonatsgehalt von 4.900 EUR. Es wird am letzten Bankarbeitstag des jeweiligen Monats auf ihr von ihr benanntes Konto überwiesen. Für einen nur anteilig bestehenden Monat wird das Gehalt zeitanteilig berechnet. Ein Bonus, eine Provision oder eine jährliche Sonderzahlung ist nicht vereinbart. Gesetzliche Ansprüche auf Entgeltfortzahlung bleiben unberührt.

## 5 Urlaub und Verhinderung

Die Arbeitnehmerin hat bei einer Fünftagewoche Anspruch auf 28 Arbeitstage bezahlten Erholungsurlaub je Kalenderjahr. Der Urlaub ist mit der Teamleitung unter Berücksichtigung der gesetzlichen Vorgaben abzustimmen. Für Ein- und Austrittsjahre gelten die gesetzlichen Mindestansprüche; darüber hinausgehender Urlaub wird zeitanteilig gewährt, soweit dadurch der gesetzliche Anspruch nicht unterschritten wird.

Eine Arbeitsverhinderung ist unverzüglich unter Angabe ihrer voraussichtlichen Dauer mitzuteilen. Bei Krankheit gelten die gesetzlichen Nachweis- und Mitwirkungspflichten, einschließlich des Verfahrens zum elektronischen Abruf der Arbeitsunfähigkeitsdaten, soweit dieses anwendbar ist. Die Arbeitgeberin kann im gesetzlich zulässigen Umfang einen früheren Nachweis verlangen.

## 6 Probezeit und Beendigung

Die ersten sechs Monate gelten als Probezeit. In dieser Zeit können beide Parteien das Arbeitsverhältnis mit einer Frist von zwei Wochen kündigen. Nach der Probezeit gelten die gesetzlichen Kündigungsfristen. Jede Kündigung bedarf der gesetzlich vorgeschriebenen Schriftform; die elektronische Form ist ausgeschlossen. Wer die Unwirksamkeit einer Kündigung geltend machen will, muss die gesetzlich vorgesehene Klagefrist beachten, regelmäßig drei Wochen ab Zugang der schriftlichen Kündigung.

Nach Ausspruch einer Kündigung durch eine der Parteien darf die Arbeitgeberin die Arbeitnehmerin ohne weitere Voraussetzungen bis zum Ablauf der Kündigungsfrist unter Fortzahlung der Vergütung einseitig von der Arbeitspflicht freistellen. Eine Anrechnung von Urlaub wird nur durch eine gesonderte unwiderrufliche Erklärung für einen konkret bestimmten Zeitraum vorgenommen.

## 7 Verschwiegenheit

Während und nach dem Arbeitsverhältnis hat die Arbeitnehmerin über sämtliche ihr bekannt gewordenen internen Vorgänge, Informationen und Geschäftsabläufe der Arbeitgeberin zeitlich unbegrenzt Stillschweigen zu bewahren. Dies gilt unabhängig davon, ob die betreffende Information im Einzelfall noch geheim oder schutzbedürftig ist. Gesetzlich erlaubte Meldungen nach dem Hinweisgeberschutzrecht und gesetzlich vorgeschriebene Offenlegungen bleiben unberührt.

## 8 Nebentätigkeit und Wettbewerb

Entgeltliche Nebentätigkeiten sind der Arbeitgeberin vor Aufnahme in Textform anzuzeigen. Die Arbeitgeberin darf sie nur untersagen, soweit konkrete berechtigte betriebliche Interessen, insbesondere gesetzliche Arbeitszeitgrenzen oder eine unmittelbare Konkurrenztätigkeit, entgegenstehen. Eine ehrenamtliche private Tätigkeit ist nicht anzeigepflichtig. Während des Arbeitsverhältnisses gelten die gesetzlichen Wettbewerbspflichten. Ein nachvertragliches Wettbewerbsverbot wird nicht vereinbart.

## 9 Ausschlussfrist

Ansprüche aus dem Arbeitsverhältnis sind innerhalb von drei Monaten nach Fälligkeit in Textform gegenüber der anderen Partei geltend zu machen. Andernfalls verfallen sie. Ausgenommen sind Ansprüche wegen vorsätzlicher Pflichtverletzung, wegen Verletzung von Leben, Körper oder Gesundheit sowie gesetzlich unverzichtbare Ansprüche, insbesondere der Anspruch auf den gesetzlichen Mindestlohn. Die gesetzlichen Verjährungsregeln bleiben für nicht verfallene Ansprüche unberührt.

## 10 Weitere Bedingungen und Anlagen

Eine betriebliche Altersversorgung wird nicht zugesagt. Auf das Arbeitsverhältnis finden nach Angaben der Arbeitgeberin keine Tarifverträge und keine Betriebsvereinbarungen Anwendung. Die Anlage Mobiles Arbeiten und Arbeitszeit vom 28. September 2026 wird Bestandteil des Vertrags und geht bei Widersprüchen den Abschnitten 2 und 3 vor. Andere Anlagen sind nicht einbezogen. Individuelle Vereinbarungen und zwingende gesetzliche Bestimmungen bleiben unberührt.

## 11 Unterzeichnung

Diese Fassung AV-NA-03 vom 28. September 2026 ist noch nicht unterzeichnet. Die Vertragsexemplare sollen nach Abstimmung von Frieda Fröhlich für die Arbeitgeberin und Nora Aydin für sich selbst unterzeichnet werden. Die Arbeitnehmerin erhält ein unterschriebenes Exemplar einschließlich der einbezogenen Anlage.'''
ARB_OLD = ARB_CURRENT.replace('28. September 2026', '18. September 2026').replace('AV-NA-03', 'AV-NA-01').replace('4.900 EUR', '4.800 EUR').replace('Mit dem Monatsgehalt sind bis zu zehn solcher Überstunden je Kalendermonat abgegolten.', 'Mit dem Monatsgehalt ist jede anfallende Mehrarbeit unabhängig von ihrer Dauer abgegolten.').replace('Ergänzend gilt die Anlage Mobiles Arbeiten und Arbeitszeit vom 18. September 2026.', 'Eine Vereinbarung über mobile Arbeit liegt dieser ersten Fassung noch nicht bei.').replace('Die Anlage Mobiles Arbeiten und Arbeitszeit vom 18. September 2026 wird Bestandteil des Vertrags und geht bei Widersprüchen den Abschnitten 2 und 3 vor. Andere Anlagen sind nicht einbezogen.', 'Anlagen sind mit dieser ersten Fassung noch nicht vereinbart.').replace('## 11 Unterzeichnung', '## 11 Fortbildung\n\nDie Arbeitgeberin stellt der Arbeitnehmerin pro Kalenderjahr zwei bezahlte Fortbildungstage für arbeitsbezogene und vorab abgestimmte Veranstaltungen zur Verfügung. Die Auswahl und der Termin werden mit der Teamleitung abgestimmt.\n\n## 12 Unterzeichnung')

ARB_OLD = ARB_OLD.replace('Weitere angeordnete oder genehmigte Überstunden werden innerhalb der folgenden drei Monate durch entsprechende bezahlte Freizeit ausgeglichen. Ist dies aus betrieblichen Gründen nicht möglich, werden sie mit dem auf eine Arbeitsstunde entfallenden Anteil des festen Monatsgehalts vergütet. ', '').replace('Die Arbeitnehmerin erhält ein unterschriebenes Exemplar einschließlich der einbezogenen Anlage.', 'Die Arbeitnehmerin erhält ein unterschriebenes Exemplar.')

arb_docs = [
 E('01_Auftrag_Arbeitsvertrag.eml', 'Arbeitsvertrag Nora Aydin bitte mit dem Playbook abgleichen', '2026-09-29T08:40:00+02:00', 'Frieda Fröhlich <frieda@spreebogen.example>', 'Clara Klee <clara@klee-kolben.example>', '''Guten Morgen Frau Klee,

bitte prüfen Sie die im Vorgang abgelegte Fassung AV-NA-03 vom 28. September zusammen mit der Anlage vom selben Tag anhand unseres freigegebenen Playbooks PB-SP-ARB Version 2.0. Die Datei vom 18. September ist nur der ältere Verlauf. Nora hat den neuen Entwurf mit ihrem Berater bearbeitet; auch unser Personalbüro hat zwei alte Textbausteine stehen gelassen. Ich brauche daher eine vollständige Prüfung und nicht nur die Änderungen aus der Mail.

Bitte weisen Sie je Thema und je Regel aus, was der Vertrag und die Anlage wirklich sagen. Unsere Budget- und Arbeitszeitpositionen sollen als Unternehmensstandard erkennbar bleiben. Unabhängig davon sollen Sie die rechtlichen Risiken prüfen und einen vollständig formulierten korrigierten Vertragstext sowie einen kurzen Brief an mich vorbereiten. Die Unterlagen gehen vorerst nur an mich.

Der Arbeitsbeginn ist für den 1. November vorgesehen. Wir haben noch nichts unterschrieben. Bitte fragen Sie nur die entscheidenden fehlenden Angaben nach und benutzen Sie keine ältere Klausel als vermeintlichen Teil der aktuellen Fassung.

Freundliche Grüße
Frieda Fröhlich'''),
 D('02_Playbook_Arbeitsvertrag_V2_0.docx', 'Verhandlungspositionen für unbefristete Arbeitsverträge', '14.09.2026', SP, 'Personalbüro und Rechtsberatung', playbook_body('PB-SP-ARB', '2.0', 'Spreebogen Produktstudio GmbH', 'unbefristete Arbeitsverträge mit Beschäftigten im Berliner Produktdesign', ARB_TOPICS, 'Die Zahlen 40 Wochenstunden, zehn abgegoltene Überstunden und die Gehaltsobergrenzen sind interne Verhandlungspositionen, keine gesetzlichen Zulässigkeitsgrenzen. Zulässige Arbeitszeit, Vergütung von Mehrarbeit und deren Anordnung sind gesondert zu beurteilen. Die Zeiterfassung ersetzt diese Prüfung nicht. Ob der konkrete mobile Arbeitsplatz tatsächlich gegen fremde Einsicht geschützt ist, wird anhand der IT-Prüfung oder gleichwertiger Tatsachenbelege beurteilt. Eine vereinbarte Schutzpflicht allein beweist den tatsächlichen Zustand nicht. Die erforderliche IT-Freigabe ist davon getrennt nachzuhalten.')),
 E('03_Freigabe_Playbook.eml', 'PB-SP-ARB 2.0 ist freigegeben', '2026-09-14T15:30:00+02:00', 'Frieda Fröhlich <frieda@spreebogen.example>', 'Clara Klee <clara@klee-kolben.example>', '''Guten Tag Frau Klee,

anbei die freigegebene Version 2.0 unseres Playbooks für das Produktdesign. Es gilt für Nora Aydin ebenso wie für andere unbefristete Einstellungen in diesem Team. Rückfallpositionen müssen im Abschlussvermerk kenntlich sein; ich entscheide über deren Annahme. Eine Fachkraft im Personalbüro darf keine Ausnahme von den roten Linien freigeben.

Die Stunden- und Gehaltswerte sind unsere Unternehmenspositionen. Bitte nennen Sie sie nicht als gesetzliche Grenzen. Rechtliche Bedenken sind auch dann zu prüfen, wenn eine Klausel eine unserer Regeln wörtlich erfüllt. Die schriftliche IT-Freigabe soll vor dem ersten mobilen Arbeitstag vorliegen, muss aber im Vertragsbericht bereits als offen erscheinen, wenn sie fehlt.

Freundliche Grüße
Frieda Fröhlich'''),
 D('04_Arbeitsvertrag_28_September.docx', 'Arbeitsvertrag mit Nora Aydin', '28.09.2026', SP, NA, ARB_CURRENT, reference='AV-NA-03 | Verhandlungsfassung'),
 D('05_Arbeitsvertrag_Altstand_18_September.docx', 'Frühere Fassung des Arbeitsvertrags mit Nora Aydin', '18.09.2026', SP, NA, 'Die folgende frühere Fassung AV-NA-01 ist durch AV-NA-03 ersetzt. Sie bleibt allein zur Nachvollziehbarkeit im Vorgang.\n\n' + ARB_OLD, reference='AV-NA-01 | überholt'),
 D('06_Anlage_Mobiles_Arbeiten.docx', 'Mobiles Arbeiten und Arbeitszeit für Nora Aydin', '28.09.2026', SP, NA, '''## 1 Geltung und Rang

Diese noch nicht unterzeichnete Anlage gehört zum Arbeitsvertragsentwurf AV-NA-03 vom 28. September 2026. Bei Widersprüchen geht sie den Abschnitten 2 und 3 des Hauptvertrags vor. Alle übrigen Regelungen bleiben unverändert. Sie soll gemeinsam mit dem Hauptvertrag unterzeichnet werden.

## 2 Regelmäßige Arbeitszeit

Abweichend von Abschnitt 3 des Hauptvertrags beträgt die regelmäßige Wochenarbeitszeit 38,5 Stunden ohne Ruhepausen. Sie verteilt sich grundsätzlich auf Montag bis Freitag. Die Regeln des Hauptvertrags über Anordnung, Dokumentation, höchstens zehn mit dem Monatsgehalt abgegoltene Überstunden und den Ausgleich darüber hinausgehender Überstunden gelten unverändert. Das feste Monatsgehalt bleibt ebenfalls unverändert.

## 3 Mobile Arbeit

Der regelmäßige Arbeitsort bleibt das Berliner Büro. Nach vorheriger Abstimmung mit der Teamleitung darf Frau Aydin bis zu zwei Tage pro Woche an ihrem genehmigten häuslichen Arbeitsplatz in Deutschland mobil arbeiten. Ein ständiger Wechsel des Arbeitsorts oder eine Tätigkeit aus dem Ausland bedürfen einer gesonderten Vereinbarung. Besprechungen und die berechtigten betrieblichen Anforderungen sind bei der Wahl der Tage zu berücksichtigen.

## 4 Schutz und Ausstattung

Es wird ausschließlich das von der Arbeitgeberin bereitgestellte, verwaltete Notebook verwendet. Der Bildschirm muss gegen Einsicht Dritter geschützt sein; vertrauliche Unterlagen sind verschlossen aufzubewahren. Die Verbindung zum Unternehmensnetz erfolgt über die freigegebene gesicherte Verbindung. Private Personen dürfen das Gerät nicht benutzen. Arbeitszeit- und Gesundheitsschutzvorgaben gelten uneingeschränkt.

Vor dem ersten mobilen Arbeitstag muss die IT den konkret vorgesehenen Arbeitsplatz nach dem vereinbarten internen Verfahren schriftlich freigeben. Bis dahin arbeitet Frau Aydin im Büro. Die Arbeitgeberin stellt die erforderliche betriebliche Ausstattung bereit und trägt die vereinbarten notwendigen Beschaffungskosten. Mit dieser Anlage wird nicht bestätigt, dass die Prüfung bereits stattgefunden hat.

## 5 Abstimmung bei Veränderungen

Ändern sich die räumlichen oder technischen Bedingungen, wird die IT informiert. Bei einem konkret dokumentierten Sicherheitsproblem ist mobile Arbeit bis zur Klärung auszusetzen. Die Parteien suchen dann eine angemessene Lösung. Weitergehende Änderungen dieser Vereinbarung werden gemeinsam abgestimmt.''', reference='AV-NA-AN1'),
 E('07_Versand_Neufassung.eml', 'Nora Aydin neue Fassung und Anlage', '2026-09-28T18:10:00+02:00', 'Nora Aydin <nora@postfach.example>', 'Frieda Fröhlich <frieda@spreebogen.example>', '''Guten Abend Frau Fröhlich,

anbei die heute mit dem Personalbüro zusammengeführte Fassung AV-NA-03 und die Anlage. Bitte nehmen Sie diese beiden Dateien als aktuellen Stand. Die Anlagenregelung zu 38,5 Stunden und zwei mobilen Tagen ist mir wichtig. Die Überstundenregel haben wir im Hauptvertrag zahlenmäßig begrenzt. In Abschnitt 4 stehen jetzt die besprochenen 4.900 EUR.

Mein Berater hat nicht jede Passage des alten Musters geprüft. Ich wünsche mir daher, dass Ihre Rechtsberatung die fertige Fassung noch einmal insgesamt ansieht. Die Vertragsunterzeichnung ist mit dieser Übersendung nicht erfolgt; ich warte auf die abgestimmte Endfassung.

Freundliche Grüße
Nora Aydin'''),
 D('08_Personalblatt.docx', 'Einstellungsdaten Nora Aydin', '23.09.2026', 'Jutta Knopf\nPersonalbüro Spreebogen\njutta@spreebogen.example', 'Frieda Fröhlich', '''## 1 Person und Eintritt

Nora Aydin wohnt am Kiefernweg 23 in 12055 Berlin. Sie soll am 1. November 2026 als Produktdesignerin beginnen. Die Identitäts- und Eintrittsunterlagen werden gesondert im Personalprozess erhoben. Im Vertragsprüfungsordner werden weder eine Ausweiskopie noch Bankdaten benötigt.

## 2 Vertragsrahmen

Vorgesehen ist ein unbefristetes Arbeitsverhältnis in Vollzeit. Eine vorherige Beschäftigung bei Spreebogen bestand nicht. Die Arbeitgeberin ist nach Auskunft der Geschäftsführerin nicht tarifgebunden. Es bestehen im Betrieb kein Betriebsrat und keine Betriebsvereinbarungen. Eine betriebliche Altersversorgung wird derzeit nicht angeboten. Diese Angaben wurden im Gespräch am 22. September erhoben.

## 3 Ansprechpartnerinnen

Frieda Fröhlich ist entscheidungsbefugte Geschäftsführerin. Die fachliche Teamleitung übernimmt Milena Roth. Jutta Knopf bereitet die Personalunterlagen vor und darf keine von der Geschäftsführung nicht freigegebenen Vertragspositionen zusagen.

## 4 Zeitplanung

Die Rechtsprüfung soll bis zum 2. Oktober für das Gespräch mit Nora vorbereitet sein. Die Endfassung wird danach zur Unterschrift vorgelegt. Das Onboarding beginnt am ersten Arbeitstag; der 1. November 2026 ist ein Sonntag, sodass der erste Bürotag Montag, der 2. November, ist.'''),
 D('09_Taetigkeit_Produktdesign.docx', 'Aufgaben im Produktdesign', '22.09.2026', 'Milena Roth\nTeamleitung Produktdesign\nmilena@spreebogen.example', 'Nora Aydin', '''## 1 Arbeitsgegenstand

Sie entwickeln Bedienoberflächen für die internen Planungsprodukte unserer gewerblichen Kunden. Dazu gehören Entwürfe, klickbare Prototypen und die Abstimmung mit den Entwicklern. Kundentermine werden vorab geplant. Eine dauernde Erreichbarkeit außerhalb der vereinbarten Arbeitszeit ist nicht vorgesehen.

## 2 Teamablauf

Das Team arbeitet überwiegend zwischen 9 und 17 Uhr. Die konkrete Lage Ihrer Arbeitszeit stimmen wir innerhalb der gesetzlichen und vertraglichen Grenzen ab. Montags findet im Berliner Büro eine gemeinsame Planung statt. Für andere Tage können wir nach Einrichtung Ihres Arbeitsplatzes mobile Arbeit abstimmen. Bei einem notwendigen Präsenztermin sprechen wir rechtzeitig miteinander.

## 3 Mehrarbeit

Vor einer zeitkritischen Veröffentlichung frage ich, ob zusätzliche Stunden erforderlich sind und wie wir sie ausgleichen. Die Genehmigung dokumentiere ich im Zeitsystem. Das Projektteam soll Mehrarbeit nicht durch private Abendchats voraussetzen. Die laufende Auslastung wird wöchentlich besprochen.

## 4 Zusammenarbeit

Ihre erste Ansprechpartnerin bin ich. Fragen zu Arbeitsvertrag und Vergütung beantwortet das Personalbüro in Abstimmung mit der Geschäftsführerin. Eine Vertragsänderung kann ich selbst nicht zusagen.'''),
 D('10_Vermerk_IT_Arbeitsplatz.docx', 'Vorbereitung des mobilen Arbeitsplatzes', '28.09.2026', 'Otmar Behr\nIT Spreebogen\notmar@spreebogen.example', 'Jutta Knopf', '''Nora Aydin soll ein verwaltetes Notebook mit Festplattenverschlüsselung und gesicherter Verbindung zum Unternehmensnetz erhalten. Die Seriennummer wird bei der Ausgabe erfasst. Das Gerät ist bestellt, aber noch nicht eingerichtet und ausgegeben.

Für den häuslichen Arbeitsplatz benötigen wir eine kurze Beschreibung des abgeschlossenen Arbeitsbereichs und einen gemeinsamen Einrichtungstermin. Die Anmeldung im Ticketsystem IT-2026-184 ist angelegt. Der Status lautet offen. Ein abgeschlossener Arbeitsplatzcheck und eine schriftliche Freigabe liegen nicht vor.

Im Telefonat hat Nora einen separaten Schreibtisch erwähnt. Dies ersetzt den vereinbarten Check nicht. Die technische Einrichtung ist für den 26. Oktober vorgesehen. Bis zur schriftlichen Freigabe ist nach der vorgesehenen Anlage im Büro zu arbeiten. Der Vermerk bestätigt keine bereits erteilte Freigabe.'''),
 E('11_IT_Rueckfrage.eml', 'Ticket 184 ist noch keine Freigabe', '2026-09-29T11:20:00+02:00', 'Otmar Behr <otmar@spreebogen.example>', 'Jutta Knopf <jutta@spreebogen.example>', '''Hallo Jutta,

im Chat steht, der Homeoffice-Platz sei praktisch schon durch. Das ist zu früh. Ich habe den Termin und das Notebook eingeplant, aber weder den konkreten Arbeitsplatz gesehen noch eine Freigabe erteilt. Bitte bleibt beim Status offen.

Nora kann uns vor dem Termin die Beschreibung ihres Arbeitsbereichs schicken. Eine Webcam-Aufnahme der gesamten Wohnung brauchen wir dafür nicht. Nach dem Check sende ich eine kurze schriftliche Bestätigung oder nenne die noch fehlenden Punkte.

Viele Grüße
Otmar'''),
 D('12_Gespraechsnotiz_Frieda.docx', 'Gespräch mit Nora über die Vertragsfassung', '29.09.2026', SP, 'Clara Klee', '''## 1 Stand der Einigung

Nora möchte weiter bei uns anfangen. Für 38,5 Wochenstunden und das feste Gehalt von 4.900 EUR sieht Frieda eine wirtschaftliche Grundlage. Beide Werte sollen in der Prüfung als Abweichung vom Startangebot erkennbar bleiben. Eine pauschale Billigung aller übrigen Abschnitte ist damit nicht verbunden. Das gilt auch für Texte, die aus dem alten Personalformular stammen.

## 2 Arbeitsorganisation

Zwei mobile Arbeitstage sind bei passender Projektplanung möglich. Vor dem Start muss die IT den häuslichen Arbeitsplatz prüfen. Frieda hat im Gespräch keine bereits erteilte IT-Freigabe behauptet. Der Arbeitsort soll Deutschland bleiben.

## 3 Änderungswünsche

Nora wünscht klare Grenzen der Verschwiegenheit, weil sie ihre Berufserfahrung auch später verwenden will. Frieda möchte echte Produktgeheimnisse schützen. Beide wollen keinen Streit über einen pauschalen Geheimhaltungsbegriff. Über eine allgemeine Freistellung nach einer Kündigung haben sie noch nicht gesprochen. Die Rechtsberatung soll dafür einen sachgerechten Text vorschlagen.

## 4 Weitere Unterlagen

Es gibt keine zusätzliche mündliche Vereinbarung über Fortbildung, Boni oder eine betriebliche Altersversorgung. Wenn dazu etwas in den Vertrag soll, muss es ausdrücklich abgestimmt werden. Das ältere Formular soll nicht zur Ergänzung des neuen Vertrags herangezogen werden.'''),
 E('13_Personalbuero_Nachtrag.eml', 'Altbausteine und Nachweis der Bedingungen', '2026-09-30T09:15:00+02:00', 'Jutta Knopf <jutta@spreebogen.example>', 'Clara Klee <clara@klee-kolben.example>', '''Guten Tag Frau Klee,

mir ist aufgefallen, dass die Verschwiegenheit und die Freistellung noch aus unserem alten Formular stammen. Bitte prüfen Sie diese vollständig. Eine Einigung darüber kann ich nicht bestätigen. Der neue Vertrag soll auf jeden Fall unbefristet bleiben.

Frau Aydin erhält nach der Abstimmung beide unterschriebenen Vertragsbestandteile. Bitte prüfen Sie auch, ob damit die erforderlichen Angaben über die Arbeitsbedingungen vollständig und in der erforderlichen Weise nachgewiesen werden. Ich habe hierzu bisher keine gesonderte Empfangsbestätigung erstellt. Eine unterschriebene Vertragsfassung gibt es noch nicht.

Freundliche Grüße
Jutta Knopf'''),
 E('14_Nora_Termin.eml', 'Rückfragen zum Vertragsgespräch', '2026-09-30T17:10:00+02:00', 'Nora Aydin <nora@postfach.example>', 'Frieda Fröhlich <frieda@spreebogen.example>', '''Guten Abend Frau Fröhlich,

der Termin am 2. Oktober passt. Mein Hauptanliegen bleibt, dass die kürzere Wochenarbeitszeit und die zwei mobilen Tage in der Anlage tatsächlich vorgehen. Die Vertraulichkeit soll mich nicht daran hindern, später mein allgemeines Wissen als Designerin zu nutzen.

Die IT-Freigabe ist für mich noch offen. Ich habe den Schreibtisch erwähnt, aber niemand hat den Platz geprüft. Falls dafür etwas fehlt, reiche ich es zum vorgesehenen Termin nach. Zu Fortbildungstagen haben wir noch keine Zusage ausgetauscht. Ich möchte darüber beim Gespräch kurz sprechen.

Freundliche Grüße
Nora Aydin'''),
 dict(file='15_Personalchat.txt', title='Chatverlauf Einstellung Nora Aydin', date='30.09.2026', body='''Kanal: Personal intern. Export durch Jutta Knopf am 30. September 2026 um 17.30 Uhr.

28.09.2026 16:05 | Jutta Knopf: Nora hat die letzte Fassung. Die Anlage geht bei Stunden und mobilem Arbeiten vor.
28.09.2026 16:09 | Milena Roth: Homeoffice ist praktisch schon durch, oder?
28.09.2026 16:12 | Jutta Knopf: Der IT-Termin steht. Ob das schon eine Freigabe ist, frage ich Otmar.
29.09.2026 11:32 | Jutta Knopf: Otmar sagt ausdrücklich nein. Ticket angelegt, Freigabe offen.
29.09.2026 11:35 | Milena Roth: Danke, dann plane ich zunächst Büro ein.
30.09.2026 09:24 | Frieda Fröhlich: Bitte keine Zusage aus dem alten Formular hinzulesen. Frau Klee prüft die neuen beiden Dateien komplett.
30.09.2026 09:28 | Jutta Knopf: Die Altdatei bleibt nur im Verlauf. Unterschrieben ist nichts.'''),
]

CASES = [
 dict(slug='playbook-nda-kupferfink', title='Kupferfink und das NDA für Federlicht', date='30.09.2026', client='Kupferfink Sensorik GmbH', plugin='playbook-pruefer', summary='Eine Berliner Sensorfirma prüft den NDA-Entwurf ihres Designpartners. Ein freigegebenes Playbook, zwei Vertragsstände, eine ranghöhere Projektanlage und technische Rückfragen gehören zum Vorgang.', assignment='Prüfen Sie den aktuellen NDA samt einbezogener Anlage anhand aller Regeln des freigegebenen Playbooks. Belegen Sie die Einzelurteile am Vertrag, unterscheiden Sie Unternehmensposition und Rechtslage und bearbeiten Sie offene Tatsachenfragen. Erstellen Sie einen internen Bericht, einen vollständig formulierten Änderungsvorschlag und einen Entwurf der Begleitmail.', documents=nda_docs, attachments={'03_Freigabe_Playbook.eml':['02_Playbook_NDA_V1_2.docx'], '07_Versand_Gegnerentwurf.eml':['04_NDA_Entwurf_25_September.docx','06_Anlage_FED_AN1.docx']}),
 dict(slug='playbook-arbeitsvertrag-spreebogen', title='Spreebogen und der Arbeitsvertrag von Nora Aydin', date='30.09.2026', client='Spreebogen Produktstudio GmbH', plugin='playbook-pruefer', summary='Ein Berliner Produktstudio stellt Nora Aydin unbefristet ein. Die gemeinsam bearbeitete Vertragsfassung, eine vorrangige Anlage zum mobilen Arbeiten und das Arbeitgeberplaybook stehen neben dem älteren Personalformular und den Rückfragen der Beteiligten.', assignment='Prüfen Sie Hauptvertrag und Anlage zusammen gegen sämtliche Regeln des Arbeitgeberplaybooks. Zitieren Sie die maßgeblichen Passagen und halten Sie rechtliche Bedenken getrennt von bloßen Abweichungen vom Unternehmensstandard fest. Erstellen Sie einen internen Bericht, eine vollständig ausformulierte überarbeitete Vertragsfassung und einen kurzen Begleitbrief. Bezeichnen Sie entscheidende ungeklärte Tatsachen ausdrücklich.', documents=arb_docs, attachments={'03_Freigabe_Playbook.eml':['02_Playbook_Arbeitsvertrag_V2_0.docx'], '07_Versand_Neufassung.eml':['04_Arbeitsvertrag_28_September.docx','06_Anlage_Mobiles_Arbeiten.docx']}),
]
