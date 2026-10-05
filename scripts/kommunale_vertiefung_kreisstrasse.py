"""Fallbezogene Vertiefung: Kreisstraßenbaum und vier Bestandsakten.

Alle Personen, Körperschaften, Vertragsprogramme und Geschäftsvorfälle sind
synthetisch. Bestehende Originale werden durch dieses Datenmodul nicht verändert.
"""

FOLDER = 'kommunikation-und-deckung'


def D(file, title, date, kind, body, sender='', recipient=''):
    return dict(file=file, title=title, date=date, kind=kind, body=body.strip(),
                sender=sender, recipient=recipient)


def K(label, file, description):
    return dict(label=label, source=f'{FOLDER}/{file}', description=description)


CASES = [dict(
    slug='akha-wuerzburg-kreisstrassenbaum',
    title='Wunibaldine Seifert und der Kreisstraßenbaum',
    summary='Ein erkennbar vorgeschädigter Straßenbaum stürzt auf einen Pkw. Gemeinde und Landkreis streiten über den Kontrollauftrag; Personenschaden, Haushaltsführung und Rückversicherungsreserve sind getrennt zu prüfen.',
    is_new=True,
    notes='Synthetischer Landkreis Mainleiten und synthetische Gemeinde Apfelried im für die Übung gesetzten Landgerichtsbezirk Würzburg. Die Kreisstraße ML 17 und sämtliche Anschriften sind erfunden. Der Landkreis wird wegen eigener Organisations- und Kontrollversäumnisse verklagt; ein privatrechtlicher Dienstleistungsvertrag verschiebt die Straßenbaulast nicht. Die Verletzte hat keinen Anspruch gegen AKHA oder den Rückversicherer aus deren interner Abrechnung. Unbezifferter Schmerzensgeldantrag mit 90.000 EUR Orientierung; bezifferter materieller Schaden 22.730 EUR; Feststellung weiterer eigener materieller Schäden, soweit noch nicht vom Zahlungsantrag erfasst. Kein Verfahren eingeleitet. Reserven sind keine anerkannten Forderungen.',
    core=['01_Pruefauftrag.eml','02_Unfall_und_Zeugen.docx','03_Strasse_und_Kontrollvertrag.docx','04_Baumkontrolle.docx','06_Eigenaufwand.docx','16_Klageentwurf_Seifert.docx'],
    exhibits=[
        K('K1','02_Unfall_und_Zeugen.docx','Unfallhergang und begrenzte Zeugenaussagen'),
        K('K2','03_Strasse_und_Kontrollvertrag.docx','Straßenklassifizierung, Baulast und Dienstleistungsvertrag'),
        K('K3','04_Baumkontrolle.docx','Kontrollnotiz vor dem Unfall und späterer Sachverständigenbefund'),
        K('K4','05_Behandlung_und_Prognose.docx','Behandlungsverlauf und begrenzte Prognose'),
        K('K5','06_Eigenaufwand.docx','Bezahlte Haushaltshilfe, Fahrten, Pkw-Wert und Drittleistungsabgleich'),
        K('K6','08_Gemeinde_Warnmeldung.eml','Übermittlung der konkreten Warnung an den Landkreis'),
        K('K7','09_Landkreis_Antwort.pdf','Zuständigkeit, Empfang und streitige Kontrolle'),
        K('K8','13_Anspruchsschreiben.pdf','Außergerichtliche Forderung und Anlagenübermittlung'),
        K('K9','14_Landkreis_Fristantwort.eml','Offene Regulierung und keine Anerkennung'),
    ],
    attachments={
        '01_Pruefauftrag.eml':[f'{FOLDER}/03_Strasse_und_Kontrollvertrag.docx',f'{FOLDER}/07_Versicherungsmodell.docx'],
        '08_Gemeinde_Warnmeldung.eml':[f'{FOLDER}/04_Baumkontrolle.docx'],
        '11_Rueckversicherungsanfrage.eml':[f'{FOLDER}/07_Versicherungsmodell.docx',f'{FOLDER}/10_Versicherer_Reservebrief.pdf'],
        '14_Landkreis_Fristantwort.eml':[f'{FOLDER}/09_Landkreis_Antwort.pdf'],
        '15_Abstimmung_Erstversicherer.eml':[f'{FOLDER}/12_Rueckversicherer_Antwort.pdf'],
    },
    documents=[
D('01_Pruefauftrag.eml','ML 17: Baumunfall, Haftungsabwehr und getrennte Deckungsprüfung','2026-10-05T13:40:00+02:00','email', '''Sehr geehrte Frau Klee,

der Landkreis Mainleiten beauftragt Sie mit der Prüfung des Unfalls von Frau Wunibaldine Seifert am 17. August auf der Kreisstraße ML 17. Bitte prüfen Sie die Verantwortung unseres Straßenbauamts anhand der beigefügten Vereinbarung mit Apfelried. Unser Auftrag umfasst weder ein Mandat der Gemeinde noch ein Mandat unseres Versicherers Frankenbogen. Die im Ordner enthaltene Klageschrift aus Sicht der Verletzten ist eine Übungsfassung der Gegenseite; Sie sollen sie auf tragfähige Einwendungen prüfen.

Inzwischen liegt die auf den Vorgang bezogene Deckungsbestätigung vor. Wir benötigen getrennte Antworten zur Außenhaftung, zu unserem Verhältnis zur Gemeinde, zur Versicherungsdeckung und zur späteren Rückversicherung. Eine Reserveschätzung darf nicht als Angebot an Frau Seifert verwendet werden. Besonders wichtig ist mir, dass die Nachricht vom 20. Juli und der letzte Bearbeitungsstand des Baumauftrags erhalten bleiben. Bitte keine nachträgliche Vervollständigung des damaligen Kontrollblatts.

Frau Ehlers hat eine Antwort bis 12. Oktober erbeten. Wir haben keine Zahlung geleistet und keine Haftung anerkannt. Bitte erstellen Sie zunächst einen Antwortentwurf sowie eine konkrete Beweisliste. Ein Vergleich bedarf unserer gesonderten Entscheidung; Ihre Prüfung soll nicht von der internen Schichtenrechnung abhängig gemacht werden.

Mit freundlichen Grüßen
Ernestine Rübenacker, Rechtsamt''','Ernestine Rübenacker <recht@mainleiten.example>','Rechtsanwältin Clara Klee <clara@klee-kolben.example>'),
D('02_Unfall_und_Zeugen.docx','Unfallaufnahme und getrennte Zeugenaussagen','18.08.2026','document', '''1. Gesicherter Aufnahmebefund

Am 17. August 2026 um 16:42 Uhr lag eine etwa 19 Meter hohe Esche quer über der Kreisstraße ML 17, Abschnitt 120, Kilometer 2,340, außerhalb der Ortsdurchfahrt Apfelried. Ihr Stamm traf das Dach des Pkw von Wunibaldine Seifert, Rosenquergasse 7, 97074 Würzburg. Der Pkw war zuvor auf der rechten Fahrspur in Richtung Apfelried unterwegs. Die Fahrerin wurde eingeklemmt, um 17:06 Uhr befreit und in die Unfallklinik gebracht. Der Baum stand im Straßenbegleitstreifen. Ein weiteres Fahrzeug war nicht beteiligt. Auf der Fahrbahn lag vor dem Stamm kein anderes Hindernis.

2. Aussage des nachfolgenden Fahrers

Gottlob Özdemir, Weidenbogen 14, 97076 Würzburg, fuhr mit etwa 60 Metern Abstand hinter Frau Seifert. Nach seiner Schätzung bewegten sich beide Fahrzeuge mit ungefähr 55 km/h bei zulässigen 70 km/h. Er sah die Baumkrone plötzlich nach rechts über die Straße kippen. Der Stamm traf den vorausfahrenden Wagen, bevor dieser daran vorbeifuhr. Er sah keine Ausweichbewegung auf den Randstreifen. Er kann die Geschwindigkeit nicht technisch messen und weiß nicht, ob die Klägerin den Baum vor dem Kippen wahrgenommen hatte. Starken Wind oder einen Sturm nahm er nicht wahr; es war trocken.

3. Beobachtung des Rettungsdiensts

Rettungsassistentin Amalia Benz, zu laden über Rettungswache Mainbogen, Hilfegasse 6, 97080 Würzburg, fand die Fahrerin angeschnallt und ansprechbar im Wagen. Frau Seifert gab an, nur ein Knacken gehört zu haben. Diese Mitteilung ist keine eigene Beobachtung des Unfallbeginns durch Frau Benz. Der Wagen stand etwa sechs Meter hinter der ursprünglichen Stammachse. Ein Mobiltelefon lag in der verschlossenen Mittelkonsole.

4. Sicherung

Der Wurzelstock und drei markierte Stammstücke wurden durch den Kreisbauhof auf das umzäunte Betriebsgelände Straßenbogen 2 verbracht. Die Kennzeichnung lautet ML17-226. Es gibt weder eine heimliche Videoaufnahme noch eine Geschwindigkeitsmessung. Eine Fahrbahnfreigabe erfolgte erst nach Abschluss der Sicherung um 21:15 Uhr. Aufnahmevermerk des Kreisbauhofs: Hanno Brösel. Die Zeugen haben ihre jeweiligen Absätze am 18. August als zutreffend bestätigt.'''),
D('03_Strasse_und_Kontrollvertrag.docx','Straßenbestandsauszug und Vereinbarung zur Baumkontrolle','01.07.2026','document', '''1. Straßenbestand

Der vom Straßenbauamt am 1. Juli 2026 bestätigte Bestandsauszug ordnet den gesamten Abschnitt 120 der ML 17 dem Landkreis Mainleiten als Straßenbaulastträger zu. Kilometer 2,340 liegt außerhalb der festgesetzten Ortsdurchfahrt. Baum 226 steht auf dem zum Straßengrund gehörenden Seitenstreifen, nicht im angrenzenden Privatwald. Eigentümer des Straßengrundstücks und des Baums ist der Landkreis. Der Auszug enthält keine Übertragung der Baulast auf die Gemeinde Apfelried.

2. Vereinbarung vom 18. Dezember 2025

Der Landkreis Mainleiten, vertreten durch Landrätin Selma Hasenbein, und die Gemeinde Apfelried, vertreten durch Bürgermeister Ignaz Schnabel, vereinbaren für 2026 privatrechtliche Kontrollleistungen. Der Gemeindebauhof führt die beauftragten Sichtkontrollen nach fachlicher Unterweisung aus und dokumentiert konkrete Auffälligkeiten baumbezogen. Besondere Hinweise sind unverzüglich an das zentrale Postfach des Kreisstraßenbauamts zu melden. Die Vergütung beträgt 12.000 EUR jährlich. Eine hoheitliche Aufgabenübertragung oder eine Änderung der Straßenbaulast ist nicht vereinbart.

Der Landkreis behält die Entscheidung über vertiefte Untersuchungen, Verkehrsabsicherung und Fällungen. Er kontrolliert jeden Werktag den Eingang der Warnmeldungen, legt für auffällige Bäume eine dokumentierte Bearbeitungsfrist fest und prüft die Erledigung. Die Gemeinde darf bei unmittelbar erkennbarer Gefahr den Straßenbauhof telefonisch alarmieren und den Gefahrenbereich vorläufig sichern, soweit ihre Mittel dafür ausreichen. Sie entscheidet nicht über eine dauerhafte Verkehrsbeschränkung.

3. Haftung im Innenverhältnis

Jede Körperschaft trägt die Folgen eigener schuldhafter Vertragsverletzungen nach den gesetzlichen Regeln. Eine verschuldensunabhängige Freistellung des Landkreises oder ein Verzicht auf Ansprüche verletzter Dritter wird nicht vereinbart. Bei mehreren Ursachen bleiben Kausalität und Verantwortungsanteile gesondert aufzuklären. Beide Seiten erhalten die Unterlagen der jeweils anderen Seite, soweit dies für die konkrete Schadenbearbeitung erforderlich und rechtlich zulässig ist.

Der Auszug wurde von Ernestine Rübenacker und Ignaz Schnabel am 1. Juli 2026 als vollständig für diese Zuständigkeits- und Kontrollregelungen bestätigt. Er enthält keine Versicherungsbedingungen.'''),
D('04_Baumkontrolle.docx','Baum 226: Vorbefund, Auftrag und Untersuchung nach dem Ereignis','02.09.2026','document', '''1. Kontrollnotiz vom 20. Juli 2026

Gemeindemitarbeiterin Roswitha Yilmaz untersuchte Baum 226 am 20. Juli vom Boden aus. Am Stammfuß sah sie einen breiten alten Rindenschaden, dunkle weiche Stellen und zwei seitlich austretende Pilzfruchtkörper. In der Krone befand sich ein auffällig dünn belaubter Bereich. Sie schrieb: „Standfestigkeit nicht aus bloßer Sichtkontrolle zuverlässig beurteilbar; zeitnahe fachkundige Wurzelstockprüfung veranlassen.“ Eine konkrete Pilzart bestimmte sie nicht. Die Beobachtung wurde am selben Tag mit der Baumkennung an das zentrale Postfach des Kreisstraßenbauamts versandt. Zeugin: Roswitha Yilmaz, Gemeindebauhof, Mühlbogen 3, Apfelried.

2. Bearbeitungsstand des Landkreises

Das Eingangsjournal bestätigt den Eingang am 20. Juli um 14:08 Uhr. Am 21. Juli legte Sachbearbeiter Hanno Brösel den Auftrag U-226 an. Im Feld „Erledigung“ steht seit 30. Juli „an Unternehmer gegeben“. Ein Untersuchungsbericht, ein Termin oder eine Empfangsbestätigung des Unternehmers ist nicht verknüpft. Das Straßenbauamt teilte am 27. August mit, dass kein Untersuchungsauftrag das Haus verlassen hatte. Der Status war durch Übernahme eines Entwurfstextes gesetzt worden. Eine Straßenabsicherung bis zur Prüfung wurde nicht veranlasst.

3. Untersuchung vom 24. August

Baumsachverständige Dr. Selin Heller untersuchte den gesicherten Wurzelstock und die Stammteile. Die tragenden Wurzelansätze wiesen ausgedehnte ältere Fäulnis auf; an mehreren Stellen ließ sich Holz mit einem stumpfen Prüfgerät ohne erheblichen Druck ablösen. Das Bruchbild passt zu einem Verlust der Standfestigkeit aus diesem Bereich. Die bei der Kontrolle beschriebenen äußeren Schäden waren fachlich geeignet, eine vertiefte Untersuchung auszulösen. Eine solche Untersuchung hätte nach ihrer Einschätzung den erheblichen Standfestigkeitsmangel mit hoher Wahrscheinlichkeit erkannt. Sie hält bei diesem Befund eine kurzfristige Sperrung des Fallbereichs bis zur fachgerechten Entfernung für erforderlich.

4. Aussagegrenzen

Die Sachverständige hat den stehenden Baum nicht selbst gesehen und stützt ihre zeitliche Einordnung zusätzlich auf die Kontrollnotiz. Die genaue Entwicklung einzelner Fäulniszonen zwischen 20. Juli und 17. August lässt sich nach dem Bruch nicht millimetergenau rekonstruieren. Ihr Befund ist ein von der Klägerin beauftragtes Privatgutachten, kein gerichtliches Sachverständigengutachten. Ladungsanschrift: Baumlabor Heller, Werkbogen 9, 97080 Würzburg. Unterschrieben am 2. September 2026, Dr. Selin Heller.'''),
D('05_Behandlung_und_Prognose.docx','Behandlung, gegenwärtige Einschränkungen und Prognose','28.09.2026','document', '''1. Behandlung

Wunibaldine Seifert, geboren am 11. Mai 1981, erlitt am 17. August 2026 eine instabile Fraktur des ersten Lendenwirbelkörpers mit inkompletter neurologischer Schädigung sowie eine Fraktur des rechten Unterarms. Noch am Unfalltag erfolgten Dekompression und Stabilisierung der Wirbelsäule, am 19. August die operative Versorgung des Unterarms. Die stationäre Akutbehandlung dauerte bis 4. September, anschließend erfolgte stationäre Rehabilitation bis 25. September. Diese Daten ergeben sich aus dem für diese Akte zusammengefassten Entlassungsbericht der fiktiven Unfallklinik Mainbogen.

2. Zustand am 28. September

Die Patientin kann kurze Strecken mit zwei Unterarmgehstützen und Begleitung zurücklegen. Auf längeren Wegen benötigt sie einen Rollstuhl. Sie berichtet tägliche Schmerzen im Rücken und eine rasche Erschöpfbarkeit. Treppensteigen und das Tragen von Lasten sind derzeit nicht möglich. Der rechte Arm darf noch nicht voll belastet werden. Eine dauerhafte vollständige Querschnittlähmung wird nicht diagnostiziert. Die weitere neurologische Erholung lässt sich zu diesem frühen Zeitpunkt nicht zuverlässig vorhersagen.

3. Haushalt und weitere Behandlung

Die Patientin lebt mit ihrem Ehemann Friedrich Seifert und der neunjährigen Tochter in einer 95-Quadratmeter-Wohnung. Sie benötigt vorerst Unterstützung bei Körperpflege, Transfers, Einkäufen und Haushaltsarbeiten. Ein barrierearmer Umbau und weitere Hilfsmittel werden geprüft, sind aber noch nicht bestellt. Kontrollen der Wirbelsäulenstabilisierung sind erforderlich. Eine spätere Materialentfernung und weitere Rehabilitation sind möglich; ihre konkrete Notwendigkeit und ihr Zeitpunkt stehen noch nicht fest. Die Ärztin befürwortet eine erneute Bedarfsbewertung nach drei Monaten.

4. Abrechnung und Aussageumfang

Krankenhaus- und Rehabilitationsleistungen wurden mit der gesetzlichen Krankenversicherung abgerechnet. Die Bescheinigung bewertet keinen rechtlichen Anspruch und keinen Kapitalwert. Sie enthält keine Aussage, dass jede angegebene Haushaltshilfestunde medizinisch erforderlich gewesen sei. Hierzu müssen Tätigkeiten und verbleibende Eigenleistungen zugeordnet werden. Verantwortliche Ärztin: Dr. Marlene Vogel, Unfallklinik Mainbogen, Klinikring 12, 97080 Würzburg. Für ein gerichtliches Verfahren ist sie nach Schweigepflichtentbindung als sachverständige Zeugin benannt; ein unabhängiges medizinisches Gutachten bleibt möglich.'''),
D('06_Eigenaufwand.docx','Bezahlte Aufwendungen, Fahrzeugschaden und Leistungen Dritter','02.10.2026','document', '''1. Haushaltshilfe

Die Klägerin bezahlte am 29. September die Rechnung HH-260926 der Haushaltsdienste Hermine & Helfer, Leiterin Hermine Daubner, Rosenquergasse 20, Würzburg. Die Rechnung umfasst 140 Stunden zu 25 EUR einschließlich aller Entgeltbestandteile, insgesamt 3.500 EUR. Davon entfallen im Zeitraum 18. August bis 25. September 98 Stunden auf Küche, Wäsche und Reinigung im bisherigen eigenen Aufgabenbereich der Klägerin sowie 42 Stunden auf Einkauf und schulbezogene Alltagsversorgung der Tochter, die ebenfalls zuvor von der Klägerin übernommen wurden. Der Ehemann erbrachte daneben seine unveränderten eigenen Haushaltsanteile. Seine zusätzliche unentgeltliche Hilfe wird nicht in dieser Rechnung angesetzt. Arbeitslisten und Zahlungsbestätigung sind Bestandteile dieser zusammengefassten Belegurkunde.

2. Erforderliche Fahrten

Bezahlte Beförderungskosten von 480 EUR betreffen vier Fahrten der Klägerin zu ärztlich angeordneten ambulanten Untersuchungen am 8., 15., 22. und 28. September zu je 120 EUR. Die erste Fahrt erfolgte aus der Rehabilitation, die letzte aus der Wohnung. Das Angebot umfasste die notwendige Begleitunterstützung beim Ein- und Aussteigen. Familienbesuche und Fahrten des Ehemanns sind nicht enthalten. Rechnungsstellerin: Mainbogen Mobilität GmbH, Fahrtberichte MM-0908 bis MM-0928. Die Klägerin bezahlte gesammelt am 30. September.

3. Fahrzeug

Der eigene Pkw der Klägerin erlitt Totalschaden. Der im Gutachten vom 25. August ermittelte Wiederbeschaffungswert beträgt 19.800 EUR. Nach dem dort dokumentierten regionalen Privatmarkt fällt bei der Ersatzbeschaffung keine gesondert ausweisbare Umsatzsteuer an. Ein verbindliches Restwertangebot über 1.600 EUR wurde am 3. September angenommen; die Zahlung ist eingegangen. Verlangt werden deshalb 18.200 EUR Fahrzeugschaden. Die bezahlte Rechnung für die Bergung am Unfalltag beträgt 550 EUR. Nutzungsausfall, Mietwagen, eine Pauschale und Gutachterkosten werden in der vorbereiteten Klage nicht verlangt. Fahrzeug-Sachverständiger: Leopold Nowak, Prüfbogen 4, Würzburg. Eine Kaskoversicherung bestand nicht.

4. Abgleich

Die Summe der bezifferten eigenen Positionen lautet 3.500 EUR + 480 EUR + 18.200 EUR + 550 EUR = 22.730 EUR. Die Krankenkasse Mainbogen hat am 1. Oktober nach Prüfung der vier Fahrten und des Hilfezeitraums bestätigt, hierfür weder Leistungen erbracht zu haben noch nach ihren Leistungsentscheidungen erbringen zu müssen. Die Krankenhaus- und Rehabilitationskosten bleiben dagegen vollständig außerhalb der Klage. Die für dieses Übungsszenario beigefügte Bescheidzusammenfassung wurde von der Klägerin am 2. Oktober bestätigt; eine darüber hinausgehende Aussage über zukünftige Ansprüche nach § 116 SGB X ist damit nicht verbunden. Weitere Erstattungen, Abtretungen oder Zahlungen auf die 22.730 EUR liegen nach ihrer Erklärung nicht vor.'''),
D('07_Versicherungsmodell.docx','Vorgangsspezifischer Vertrags- und Rückversicherungsstand','30.09.2026','document', '''1. Erstversicherung

Für die synthetische Vertragsübung bestätigt Frankenbogen Kommunalversicherung VVaG dem Landkreis Mainleiten den Vertrag KH-ML-2026 für den Zeitraum 1. Januar bis 31. Dezember 2026. Versichert sind gesetzliche Haftpflichtansprüche aus der Kreisstraßenverwaltung einschließlich der Baumkontrolle. Die Versicherungssumme beträgt 10.000.000 EUR je Ereignis; sie ist für den Vorgang frei verfügbar. Der Landkreis trägt 5.000 EUR Selbstbehalt je Ereignis, nicht je einzelne Anspruchsposition. Frankenbogen organisiert Anspruchsabwehr und Regulierung; der Landkreis darf ohne Abstimmung keine Vergleichszusage auf Kosten des Versicherers abgeben. Gegenüber der Verletzten bleiben die gesetzlichen Ansprüche ungekürzt.

2. Gesonderte Rückversicherung des Erstversicherers

Frankenbogen hält bei Auenfels Rückversicherung AG für diese Übung einen direkten, ereignisbezogenen Exzedentenvertrag. Nach dieser gesetzten Einzelvereinbarung beträgt die Priorität 1.000.000 EUR des von Frankenbogen tatsächlich getragenen entschädigungsfähigen Nettoschadens nach Abzug des kommunalen Selbstbehalts. Darüber folgt ein Limit von 4.000.000 EUR. Gesonderte Rechtsverfolgungs- und Regulierungskosten sind in diesem Modell nicht Teil der Bezugsgröße. Die Deckung für diesen Ereignisjahrgang wird von Auenfels bestätigt; eine Haftungsanerkennung gegenüber der Verletzten folgt daraus nicht.

3. Meldung und Abrechnung

Sobald Frankenbogen einen entschädigungsfähigen Nettoschaden oberhalb von 750.000 EUR erwarten muss, übersendet es eine Vorabmeldung mit Sachverhalt, Reservebegründung und Belegen. Oberhalb der Priorität liegende Zahlungen werden nach Nachweis abgerechnet. Vergleichsvorschläge oberhalb einer erwarteten Nettobelastung von 1.000.000 EUR sind vorher zur Abstimmung vorzulegen. Die Anmeldung einer Reserve erzeugt keine bereits fällige Rückversicherungsforderung. Auenfels zahlt ausschließlich an Frankenbogen. Es besteht in diesem Vorgang kein Vertrag der Verletzten und kein Zahlungsweg über den Landkreis zu Auenfels.

4. Eigenständigkeit des Szenarios

Diese frei gesetzten Modellbedingungen bilden keine realen AKHA-Verträge oder Marktbedingungen ab. Anders als im gesonderten Fall Nora Winter wird hier kein Mitgliederselbstbehalt einer Ausgleichsebene eingeschoben. Eine dort verwendete Priorität von 10.000.000 EUR darf nicht in diese Akte übernommen werden. Bestätigung des Modellstands: Hannes Fink für Frankenbogen, Adelheid Sturm für Auenfels, 30. September 2026.'''),
D('08_Gemeinde_Warnmeldung.eml','Baum 226: Warnung vom Juli und unsere Handlungsgrenzen','2026-09-03T10:22:00+02:00','email', '''Sehr geehrte Frau Rübenacker,

ich übersende die zusammengeführte Kontrollakte mit unverändertem Julivermerk. Roswitha Yilmaz meldete die Auffälligkeiten am 20. Juli an Ihr zentrales Straßenpostfach. Ich habe ihren Versand im gemeindlichen System geprüft. In Ihrem Antwortauszug steht als Eingang 14:08 Uhr. Der Baum war damit kein Fall, den unser Bauhof als unauffällig freigegeben hätte. Wir haben damals allerdings auch nicht noch einmal telefonisch nachgefasst; ob dies nach Lage des Befunds erforderlich war, lassen wir prüfen.

Die vereinbarte fachkundige Wurzelstockuntersuchung und die Entscheidung über eine Sperrung lagen nach unserem Vertrag beim Landkreis. Unser Mitarbeiter hatte weder einen Untersuchungsauftrag an einen Unternehmer erteilt noch eine Bestätigung über einen erledigten Auftrag gesehen. Bitte erklären Sie, woher der Status „an Unternehmer gegeben“ stammt. Wir wollen weder Ihren Ablauf vorwegnehmen noch unsere eigenen Versäumnisse ausschließen.

Die Gemeinde wird ihre Bediensteten als Zeugen benennen und den ursprünglichen Datenstand erhalten. Eine pauschale Übernahme sämtlicher Ansprüche von Frau Seifert können wir derzeit nicht erklären. Bitte führen Sie mögliche Ansprüche aus unserem Vertrag getrennt von der Entschädigung der Fahrerin. Ein gemeinsames Gespräch mit unseren jeweiligen Versicherungsbearbeitern ist sinnvoll, sofern die Rollen vorher klar sind.

Mit freundlichen Grüßen
Ignaz Schnabel, Bürgermeister''','Ignaz Schnabel <buergermeister@apfelried.example>','Ernestine Rübenacker <recht@mainleiten.example>'),
D('09_Landkreis_Antwort.docx','Baum 226 – Stellungnahme zum Kontrollauftrag','04.09.2026','letter', '''Landkreis Mainleiten · Rechtsamt
Ernestine Rübenacker · Kreisplatz 3 · 97070 Würzburg

Gemeinde Apfelried
Herrn Bürgermeister Ignaz Schnabel · Rathausbogen 1 · 97299 Apfelried

Sehr geehrter Herr Schnabel,

wir bestätigen den Eingang der Warnmeldung Ihrer Mitarbeiterin am 20. Juli um 14:08 Uhr. Die Kreisstraße ML 17 einschließlich des Seitenstreifens steht im betroffenen Abschnitt in unserer Baulast. Der privatrechtliche Kontrollvertrag ändert diese Zuordnung nicht. Der Schadensfall wird deshalb nicht mit dem bloßen Hinweis auf die von Ihnen ausgeführten Sichtkontrollen an die Gemeinde abgegeben.

Unsere technische Abteilung hat festgestellt, dass der Eintrag „an Unternehmer gegeben“ keinen ausgeführten Versand belegt. Nach dem derzeitigen Stand wurde ein Entwurf vorbereitet, der Auftrag jedoch nicht abgesandt. Es ist auch keine vertiefte Untersuchung dokumentiert. Wir prüfen, weshalb die Erledigungskontrolle diesen Widerspruch nicht aufgriff. Herr Brösel wird zu seinen Arbeitsschritten getrennt befragt. Seine Erinnerung soll nicht in das alte Kontrollblatt eingetragen werden.

Offen bleibt, ob Ihre Mitarbeiterin angesichts der von ihr beschriebenen Auffälligkeiten zusätzlich unmittelbar hätte alarmieren müssen. Wir machen damit keinen bereits bezifferten Erstattungsanspruch geltend. Bitte übermitteln Sie die damalige fachliche Unterweisung und die gemeindliche Vertretungsregel für dringende Baumhinweise bis zum 11. September. Unsere eigenen Unterlagen zur Postfachvertretung stellen wir Ihnen im Gegenzug zur Verfügung.

Frau Seifert erhält eine eigene Antwort, sobald ihre Bevollmächtigte die Forderungen und den Behandlungsstand übermittelt hat. Wir werden sie nicht auf interne Abstimmungen zwischen den Körperschaften verweisen. Eine Anerkennung der Haftung oder einer Quote wird durch diesen organisatorischen Zwischenstand nicht erklärt. Unser Versicherer wurde mit dem tatsächlichen Eingang der Warnung und dem unvollständigen Auftrag befasst; es wird keine bereinigte Chronologie verwendet.

Mit freundlichen Grüßen
Ernestine Rübenacker
Für den Landkreis Mainleiten'''),
D('10_Versicherer_Reservebrief.docx','Seifert – begründete Großschadenreserve und Unterlagenbedarf','30.09.2026','letter', '''Frankenbogen Kommunalversicherung VVaG
Gundula Pfennig · Versicherungsbogen 8 · 97080 Würzburg

Landkreis Mainleiten · Rechtsamt
Frau Ernestine Rübenacker · Kreisplatz 3 · 97070 Würzburg

Sehr geehrte Frau Rübenacker,

auf Grundlage des Vertragsstands vom heutigen Tag führen wir den Vorgang als gedeckten Haftpflichtfall, dessen Haftungsgrund und Höhe weiter zu prüfen sind. Der Selbstbehalt des Landkreises beträgt einmalig 5.000 EUR je Ereignis. Er wird nicht von jeder Forderung der Verletzten abgezogen. Eine Einigung über eine Zahlung an Frau Seifert ist bislang nicht erfolgt.

Unsere Bruttoreserve beträgt zunächst 1.350.000 EUR. Darin sehen wir 120.000 EUR als internen Bewertungsansatz für den immateriellen Schaden, 30.000 EUR für bisherige eigene materielle Ansprüche, 900.000 EUR für mögliche spätere Pflege-, Haushaltsführungs- und Erwerbsfolgen sowie 300.000 EUR für denkbare Trägerregresse vor. Diese Ansätze sind vorsichtig gesetzte Reserven und weder behauptete Schadensbeträge der Verletzten noch ein Vergleichsangebot. Die laufende medizinische Entwicklung kann sie erheblich verändern. Der bezifferte Eigenaufwand von 22.730 EUR darf nicht zusätzlich zu den hierfür bereits reservierten 30.000 EUR aufgeschlagen werden.

Für die spätere Bedarfsbewertung benötigen wir eine konkrete Tätigkeitsaufstellung, die Belastbarkeit der rechten Hand und eine abgestimmte Übersicht zu Drittleistungen. Bitte fordern Sie keine pauschale lebenslange Haushaltsrente aus einer allgemeinen Diagnose ab. Die gegenwärtige Rechnung der Haushaltshilfe betrifft einen geschlossenen Zeitraum; künftige Bedarfe sind ein eigener Prüfungsschritt.

Rechnerisch ergibt die Reserve nach dem kommunalen Selbstbehalt eine vorläufige eigene Nettobelastung von 1.345.000 EUR. Bei unverändertem Modell würde die obere Schicht daraus 345.000 EUR erreichen. Wir melden deshalb vorsorglich an Auenfels. Dies ist keine aktuelle Erstattungsforderung: Es fehlt schon an einer entschädigungsfähigen Zahlung. Die anwaltlichen Bearbeitungskosten führen wir gesondert. Wir bitten um Ihre ausdrückliche Bestätigung, dass die bisherigen Unterlagen weder ein Anerkenntnis noch eine Zusage gegenüber der Gemeinde enthalten.

Mit freundlichen Grüßen
Gundula Pfennig
Schadenbearbeitung'''),
D('11_Rueckversicherungsanfrage.eml','Vorabmeldung Seifert – Ereignis ML17-226 und 345.000 EUR Szenario','2026-10-01T09:15:00+02:00','email', '''Sehr geehrte Frau Sturm,

wir melden das Baumereignis ML17-226 unter dem bestätigten Programm vorab. Beigefügt sind der Vertragsstand und unser Reservebrief. Die 1.350.000 EUR sind eine Gesamtschätzung einschließlich noch ungeprüfter Trägerregresse. Nach 5.000 EUR kommunalem Selbstbehalt liegt die Modellbezugsgröße bei 1.345.000 EUR. Oberhalb Ihrer Priorität von 1.000.000 EUR ergäben sich bei einer späteren Zahlung in dieser Höhe 345.000 EUR. Wir verlangen diesen Betrag heute nicht.

Die Verletzte macht gegenwärtig eigene bezifferte Positionen und einen noch nicht abschließend bezifferten immateriellen Anspruch geltend. Der Verlauf der neurologischen Verletzung ist offen. Unsere hohe Reserve soll diese Unsicherheit abbilden; sie ist keine medizinische Prognose und insbesondere kein rechnerisch gesicherter lebenslanger Kapitalwert.

Bitte bestätigen Sie den Eingang und benennen Sie die für eine spätere Abrechnung erforderlichen Belege. Die direkte Regulierung bleibt bei uns. Frau Seifert und die Gemeinde Apfelried sind weder Adressatinnen dieser Anmeldung noch Zahlungsempfängerinnen aus Ihrem Vertrag. Die Frage eines vertraglichen Innenausgleichs zwischen Gemeinde und Landkreis wird gesondert bearbeitet und reduziert die Bezugsgröße erst, soweit nach dem Programm tatsächlich anrechenbare Rückflüsse feststehen.

Mit freundlichen Grüßen
Hannes Fink''','Hannes Fink <rueckdeckung@frankenbogen.example>','Adelheid Sturm <schaden@auenfels-rueck.example>'),
D('12_Rueckversicherer_Antwort.docx','Eingangsbestätigung und Abrechnungsanforderungen ML17-226','02.10.2026','letter', '''Auenfels Rückversicherung AG
Adelheid Sturm · Kontorbogen 11 · 60313 Frankfurt am Main

Frankenbogen Kommunalversicherung VVaG
Herrn Hannes Fink · Versicherungsbogen 8 · 97080 Würzburg

Sehr geehrter Herr Fink,

wir bestätigen die Vorabmeldung vom 1. Oktober für das im Vertragsstand vom 30. September beschriebene Ereignis. Die darin vereinbarte Anmeldeschwelle von 750.000 EUR erwarteter Nettobelastung ist nach Ihrem Reserveansatz erreicht. Die Rechnung 1.350.000 EUR abzüglich 5.000 EUR kommunalem Selbstbehalt abzüglich 1.000.000 EUR Priorität ergibt 345.000 EUR. Sie ist als Szenariorechnung nachvollziehbar. Eine Abrechnung oder Zahlungsfreigabe über diese Summe liegt damit nicht vor.

Für eine spätere Erstattung benötigen wir die haftungsrechtliche Bewertung einschließlich der Meldung vom 20. Juli, eine getrennte Liste eigener Ansprüche der Verletzten und übergegangener Ansprüche sowie die tatsächlich ausgeführten Entschädigungszahlungen. Der nachgewiesene Betrag ist um den vereinbarten Selbstbehalt und anrechenbare Rückflüsse zu bereinigen; gesonderte Regulierungskosten gehören nach diesem Modell nicht zur Schicht. Bitte führen Sie den gleichen Aufwand nicht zugleich als Haushaltsführungsschaden, Pflegebedarf und Trägerregress.

Vor einem Vergleich, durch den Ihre erwartete Nettobelastung 1.000.000 EUR übersteigt, bitten wir um die vertraglich vereinbarte Abstimmung. Das lässt Ihre Aufgabe, berechtigte Ansprüche gegenüber der Verletzten ordnungsgemäß zu bearbeiten, unberührt. Eine Ablehnung wegen noch fehlender Rückversicherungsunterlagen wäre keine Antwort auf deren Haftungsanspruch. Der Landkreis erhält aus unserem Vertrag keinen unmittelbaren Zahlungsanspruch; mit Frau Seifert nehmen wir nicht Kontakt auf.

Bitte aktualisieren Sie die Reserve nach der nächsten neurologischen Verlaufskontrolle. Eine bloße Multiplikation heutiger Hilfestunden mit der statistischen Restlebensdauer reicht für einen Vergleichsvorschlag nicht. Wir erwarten vielmehr benannte Prognoseannahmen und eine Abgrenzung zwischen sicherem bisherigem Aufwand, möglichen weiteren Schäden und bewusst offenbleibenden Positionen. Bis dahin bleibt die Meldung in unserem System vorgemerkt; eine Forderung ist nicht zur Auszahlung gebucht.

Mit freundlichen Grüßen
Adelheid Sturm
Schaden Rückversicherung'''),
D('13_Anspruchsschreiben.docx','Seifert gegen Landkreis Mainleiten – Personenschaden ML 17','02.10.2026','letter', '''Rechtsanwältin Leona Ehlers
Kanzlei Ehlers · Rechtsbogen 4 · 97070 Würzburg

Landkreis Mainleiten · Rechtsamt
Frau Ernestine Rübenacker · Kreisplatz 3 · 97070 Würzburg

Sehr geehrte Frau Rübenacker,

ich vertrete ausschließlich Frau Wunibaldine Seifert. Wir machen Ansprüche aus dem Baumunfall vom 17. August geltend. Ihre eigene Auskunft bestätigt, dass die konkrete Warnung des Gemeindebauhofs am 20. Juli einging und bis zum Unfall keine vertiefte Untersuchung beauftragt wurde. Meine Mandantin verlangt keine Garantie gegen jeden natürlichen Astbruch. Maßgeblich sind die bei diesem Baum dokumentierten Auffälligkeiten und die unterbliebene Reaktion hierauf.

Die bereits bezahlten beziehungsweise abschließend abgrenzbaren eigenen materiellen Schäden betragen 22.730 EUR. Darin enthalten sind 3.500 EUR Haushaltshilfe, 480 EUR erforderliche Beförderungskosten, 18.200 EUR Fahrzeugschaden nach Restwertabzug und 550 EUR Bergung. Die zusammengefasste Belegurkunde erläutert Zeiträume, Drittleistungen und die tatsächlich ausgeführten Zahlungen. Krankenhaus- und Rehabilitationskosten werden nicht für meine Mandantin verlangt. Eine Kaskoleistung ist nicht erfolgt.

Daneben fordern wir ein angemessenes Schmerzensgeld, das wir nach dem derzeitigen Verlauf mit wenigstens 90.000 EUR bewerten. Die Höhe bleibt einer Gesamtschau einschließlich der im maßgeblichen Entscheidungszeitpunkt vorhersehbaren Folgen vorbehalten. Es handelt sich nicht um einen gesonderten Betrag für die ersten sechs Wochen. Für weitere eigene materielle Schäden bitten wir um Anerkennung der Ersatzpflicht unter ausdrücklichem Ausschluss übergegangener Ansprüche Dritter.

Bitte teilen Sie uns bis 12. Oktober mit, ob eine außergerichtliche Regulierung möglich ist, und leisten Sie auf die bezifferten materiellen Ansprüche bis 16. Oktober. Ihre internen Vertrags- oder Rückversicherungsfragen sind nicht Voraussetzung dafür, sich zu den gesetzlichen Ansprüchen zu erklären. Die medizinische Entwicklung wird weiter dokumentiert. Eine Klage ist noch nicht eingereicht; der vorbereitete Entwurf soll erst nach einer Entscheidung meiner Mandantin verwendet werden. Mit diesem Schreiben werden weder unbekannte Schäden abgefunden noch Versicherer als zusätzliche Anspruchsgegner benannt.

Mit freundlichen Grüßen
Leona Ehlers
Rechtsanwältin'''),
D('14_Landkreis_Fristantwort.eml','Seifert – Eingang Ihrer Forderung und weiterer Prüfstand','2026-10-05T14:30:00+02:00','email', '''Sehr geehrte Frau Ehlers,

wir haben Ihr Schreiben vom 2. Oktober erhalten und bestätigen die Antwortfrist zum 12. Oktober. Unser Schreiben an die Gemeinde vom 4. September ist zu Ihrer vollständigen Information beigefügt. Es bestätigt die Kreisstraßenbaulast und den dokumentierten Eingang der Warnung. Es enthält weder ein Schuldanerkenntnis noch eine abschließende medizinische oder baumfachliche Bewertung.

Wir haben Frankenbogen den unveränderten Aktenstand zur Haftungsprüfung übergeben. Diese Beteiligung berührt die Anspruchsstellung Ihrer Mandantin gegenüber dem Landkreis nicht. Sie muss sich weder an einen Rückversicherer noch an einen kommunalen Ausgleich wenden. Wir stellen die Bearbeitung auch nicht bis zum Abschluss unserer Abstimmung mit der Gemeinde zurück.

Für die bezahlte Haushaltshilfe bitten wir um Übermittlung der bei Ihnen vorhandenen Tageslisten. Wir möchten die in der Zusammenfassung genannten 140 Stunden dem früheren Aufgabenanteil Ihrer Mandantin zuordnen. Eine Kürzung allein wegen Hilfe durch Angehörige haben wir damit nicht erklärt. Die Kosten der Krankenhausbehandlung sind aus Ihrer jetzigen Forderung ausgenommen; bitte halten Sie diese Trennung bei weiteren Nachweisen aufrecht. Zu Ihrer Zahlungsbitte nehmen wir nach Eingang der fachlichen Stellungnahme gesondert Stellung. Bis heute ist keine Zahlung angewiesen worden.

Mit freundlichen Grüßen
Ernestine Rübenacker''','Ernestine Rübenacker <recht@mainleiten.example>','Rechtsanwältin Leona Ehlers <leona@ehlers-recht.example>'),
D('15_Abstimmung_Erstversicherer.eml','ML17-226: Rückversicherung bestätigt Eingang, Reserve unverändert','2026-10-05T15:10:00+02:00','email', '''Sehr geehrte Frau Rübenacker,

die Antwort von Auenfels ist beigefügt. Der Rückversicherer hat den Eingang unserer Vorabmeldung bestätigt und die Modellrechnung nachvollzogen. Er hat keine 345.000 EUR freigegeben. Wir buchen daher weiterhin eine Reserve und keine vereinnahmte Rückdeckung. Eine spätere Zahlung aus dem oberen Vertrag würde an Frankenbogen gehen, nicht an den Landkreis oder an Frau Seifert.

Für die Haftungsbearbeitung benötigen wir jetzt die originale Postfachvertretungsregel und die Tätigkeitslisten der Haushaltshilfe. Bitte nehmen Sie keine pauschale Mithaftungsquote aus einer angeblichen allgemeinen Betriebsgefahr des Pkw an. Es gibt nach den bisherigen Zeugenangaben weder eine festgestellte Geschwindigkeitsüberschreitung noch eine Beteiligung eines zweiten Fahrzeugs. Jede Kürzung braucht ihre eigene tatsächliche und rechtliche Grundlage.

Die Gemeinde will ihre Unterweisung und ihre Möglichkeit einer kurzfristigen Absicherung darlegen. Ob daraus ein interner Anspruch folgt, ist offen. Wir reduzieren deshalb heute weder die Schadenreserve noch eine Entschädigung um einen erhofften Rückgriff. Den Klageentwurf von Frau Ehlers beurteilen wir anhand der dort gestellten Anträge; die Reserveschätzung von 1.350.000 EUR ist keine zusätzliche Forderung und gehört nicht als anerkannter Betrag in Ihre Antwort.

Mit freundlichen Grüßen
Gundula Pfennig''','Gundula Pfennig <schaden@frankenbogen.example>','Ernestine Rübenacker <recht@mainleiten.example>'),
D('16_Klageentwurf_Seifert.docx','Klageentwurf Seifert gegen Landkreis Mainleiten','05.10.2026','claim', '''ENTWURF – nicht eingereicht

An das Landgericht Würzburg, Zivilabteilung, Ottostraße 5, 97070 Würzburg

Wunibaldine Seifert, Rosenquergasse 7, 97074 Würzburg, Klägerin,
Prozessbevollmächtigte: Rechtsanwältin Leona Ehlers, Rechtsbogen 4, 97070 Würzburg,
gegen Landkreis Mainleiten, vertreten durch Landrätin Selma Hasenbein, Kreisplatz 3, 97070 Würzburg, Beklagter.

## 1. Anträge

Namens der Klägerin wird beantragt:

1.1. Den Beklagten zu verurteilen, an die Klägerin ein angemessenes Schmerzensgeld aus dem Unfall vom 17. August 2026 auf der Kreisstraße ML 17, Abschnitt 120, Kilometer 2,340, zu zahlen, dessen Höhe in das Ermessen des Gerichts gestellt wird, wobei die Klägerin nach dem gegenwärtigen Sachstand mindestens 90.000 EUR für angemessen hält, nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage.

1.2. Den Beklagten zu verurteilen, an die Klägerin 22.730 EUR nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem Tag nach Zustellung der Klage zu zahlen.

1.3. Festzustellen, dass der Beklagte verpflichtet ist, der Klägerin sämtliche weiteren bereits entstandenen und künftig entstehenden materiellen Schäden aus dem in Antrag 1.1 bezeichneten Unfall zu ersetzen, soweit sie nicht bereits Gegenstand des bezifferten Zahlungsantrags 1.2 sind und die Ansprüche nicht auf Sozialversicherungsträger oder andere Dritte übergegangen sind oder übergehen.

1.4. Dem Beklagten die Kosten des Rechtsstreits aufzuerlegen.

Der vorläufige Streitwert wird mit 192.730 EUR angegeben: 90.000 EUR als Schmerzensgeldorientierung, 22.730 EUR Zahlungsantrag und vorläufig 80.000 EUR für das Feststellungsinteresse. Die Bewertung des Feststellungsantrags ist eine prozessuale Schätzung und kein beantragtes Pflegekapital. Das Gericht wird um Bestimmung nach § 3 ZPO gebeten. Die Klägerin beantragt das schriftliche Vorverfahren. Ein Versäumnisurteil wird für den Fall der gesetzlichen Voraussetzungen nach wirksamer Zustellung und Fristablauf beantragt.

## 2. Zuständigkeit und Gegenstand

Gegenstand ist ein Amtshaftungsanspruch aus § 839 Abs. 1 BGB in Verbindung mit Art. 34 GG. § 71 Abs. 2 Nr. 2 GVG weist ihn dem Landgericht unabhängig von der Höhe der geltend gemachten Beträge zu. Die örtliche Zuständigkeit folgt aus §§ 12, 17 und 32 ZPO. Sitz des Beklagten und Ereignisort liegen nach dem für diesen fiktiven Fall gesetzten Zuständigkeitszuschnitt im Landgerichtsbezirk Würzburg. Die öffentlichen Straßen der Übungskörperschaft liegen in Bayern.

Die Klägerin ist die verletzte Fahrerin und Eigentümerin des beschädigten Pkw. Sie macht ausschließlich eigene Ansprüche geltend. Ein Versicherer wird nicht mitverklagt. Es besteht kein Vertrag der Klägerin mit dem Beklagten, der Gemeinde oder deren Versicherern. Der privatrechtliche Kontrollvertrag regelt das Innenverhältnis der Körperschaften und wird als Beleg der Aufgabenverteilung vorgelegt, nicht als eigener Zahlungsanspruch der Klägerin.

## 3. Straßenbaulast und konkrete Warnung

Der Baum stand im Seitenstreifen der gewidmeten Kreisstraße außerhalb der Ortsdurchfahrt. Der Bestandsauszug benennt den Beklagten als Baulastträger und Eigentümer. Nach Art. 41 Satz 1 Nr. 2 BayStrWG liegt die Baulast für Kreisstraßen grundsätzlich bei den Landkreisen und kreisfreien Gemeinden. Eine abweichende Übertragung ist hier nicht erfolgt. Die Beauftragung der Gemeinde mit Sichtkontrollen lässt die Baulast gemäß Art. 44 Abs. 2 Satz 1 BayStrWG unberührt. Beweis: Bestands- und Vertragsauszug, Anlage K2.

Der Beklagte hatte sich die Entscheidung über vertiefte Untersuchungen, die Verarbeitung der Warnmeldungen und die Erledigungskontrolle ausdrücklich vorbehalten. Am 20. Juli stellte die Gemeindemitarbeiterin Roswitha Yilmaz am Baum 226 Rindenschäden, weiche dunkle Stellen und Pilzfruchtkörper fest. Sie verlangte eine zeitnahe fachkundige Prüfung der Standfestigkeit. Ihre Nachricht ging nach dem eigenen Journal des Beklagten um 14:08 Uhr ein. Beweis: Anlage K3, ergänzende Nachricht Anlage K6; Zeugnis Roswitha Yilmaz, Gemeindebauhof, Mühlbogen 3, 97299 Apfelried.

Die Fachprüfung wurde nicht beauftragt. Der Vermerk „an Unternehmer gegeben“ beruhte nach Auskunft des Straßenbauamts auf einem übernommenen Entwurfstext. Eine Empfangsbestätigung, ein Untersuchungsergebnis und eine Absicherung gab es nicht. Der Beklagte hat den Eingang der Warnung und diesen Ablauf im Schreiben vom 4. September bestätigt. Beweis: Anlage K7; Zeugnis Hanno Brösel, zu laden über den Beklagten, Straßenbauamt, Kreisplatz 3.

## 4. Unfall und Ursächlichkeit

Am 17. August um 16:42 Uhr kippte der Baum über die Fahrbahn und traf das Dach des dort fahrenden Pkw. Der nachfolgende Zeuge Gottlob Özdemir sah das Kippen und den Einschlag. Seine ungefähre Geschwindigkeitsschätzung von 55 km/h ist keine Messung; sie bietet jedoch keinen Anhalt für eine Überschreitung der zulässigen 70 km/h. Die Klägerin war angeschnallt. Der Rettungsdienst fand das Telefon in der verschlossenen Mittelkonsole. Beweis: Anlage K1; Zeugnis Gottlob Özdemir, Weidenbogen 14, Würzburg, sowie Amalia Benz, zu laden über Rettungswache Mainbogen, Hilfegasse 6, Würzburg.

Die Privatgutachterin Dr. Selin Heller stellte ältere ausgedehnte Fäulnis der tragenden Wurzelansätze fest. Die zuvor dokumentierten äußeren Anzeichen hätten eine vertiefte Untersuchung erfordert. Nach ihrer Beurteilung wäre der erhebliche Standfestigkeitsmangel dabei mit hoher Wahrscheinlichkeit entdeckt worden; bis zur Entfernung hätte der Fallbereich gesperrt werden müssen. Beweis: Anlage K3; gerichtliches baumfachliches Sachverständigengutachten unter Untersuchung der gesicherten Teile ML17-226. Der Privatbericht ist qualifizierter Parteivortrag und ersetzt den gerichtlichen Beweis nicht.

Bei rechtzeitiger Untersuchung und Absicherung hätte die Klägerin den Fallbereich nicht befahren. Zwischen Warnung und Unfall lagen nahezu vier Wochen. Selbst wenn keine sofortige Fällung geboten gewesen sein sollte, hätte der Beklagte den konkreten Verdacht nicht ohne Termin und ohne Nachverfolgung liegen lassen dürfen. Der Baumsturz wird nicht allein aus dem nachträglichen Schadensbild als vorhersehbar behauptet; die Klägerin stützt sich auf die ausdrücklich vor dem Ereignis festgehaltenen Hinweise.

## 5. Amtspflichtverletzung und Gegenargumente

Art. 9 Abs. 1 und Abs. 5 BayStrWG ordnet die Straßenunterhaltung und Überwachung der Verkehrssicherheit dem öffentlichen Amt zu. Die Sicherung schützt gerade die ordnungsgemäßen Benutzer der Straße. Die Klägerin gehört dazu. Art. 10 Abs. 1 BayStrWG ergänzt die Verantwortung der Straßenbaubehörde für die Einhaltung der öffentlich-rechtlichen Vorschriften und anerkannten technischen Regeln; daraus wird keine eigenständige Übertragung auf die Gemeinde abgeleitet.

Es besteht keine Pflicht zur Beseitigung jedes natürlichen Baumrisikos. Der BGH begrenzt die Sicherung auf zumutbare Maßnahmen und unterscheidet konkrete Verdachtszeichen von unvermeidbaren Gefahren gesunder Bäume: BGH, Urteil vom 06.03.2014 – Az. III ZR 352/13, amtlicher Entscheidungstext, Rn. 7–8 und 12. Die Entscheidung betrifft Thüringer Landesrecht und einen natürlichen Astbruch; ihre bundesrechtlichen Sicherungsmaßstäbe werden herangezogen, die bayerische Amtszuordnung folgt gesondert aus Art. 9 Abs. 5 BayStrWG. Hier bestehen mit den vorgefundenen Schäden und der Warnmeldung konkrete Anknüpfungstatsachen. Die bloße Baumart oder das spätere Schadensausmaß sind nicht der Haftungsgrund.

Der Beklagte handelte jedenfalls fahrlässig, weil eine eingegangene konkrete Warnung ohne ausgeführten Prüfauftrag und ohne Nachkontrolle blieb. Die eigene vertragliche Zuständigkeitsverteilung verstärkt die tatsächliche Zuordnung dieses Versäumnisses. Eine möglicherweise zusätzlich fehlerhafte Reaktion der Gemeinde beseitigt die selbständige Pflicht des Beklagten nicht. Ob ihm aus dem Kontrollvertrag ein Rückgriff zusteht, wird im Innenverhältnis geklärt. Ein feststehender und realisierbarer anderweitiger Ersatzanspruch der Klägerin ist nicht aufgezeigt; insbesondere ist die bloße Vertragsforderung des Beklagten gegen die Gemeinde kein eigener Ersatzanspruch der Klägerin. Eine private Kaskoversicherung besteht nicht. Die Klägerin hat keine rechtzeitig verfügbare Schutzmöglichkeit ungenutzt gelassen; § 839 Abs. 3 BGB steht nicht entgegen.

Ein Mitverschulden nach § 254 BGB ergibt sich aus dem dokumentierten Verlauf nicht. Der Beklagte muss konkrete hierfür erhebliche Umstände vortragen. Die Klägerin verlangt keine automatische Beweislastumkehr. Ebenso wenig rechtfertigt das abstrakte Schlagwort Betriebsgefahr ohne Prüfung der einschlägigen Zurechnungsvoraussetzungen einen pauschalen Abzug von 20 oder 25 Prozent. Ein zweites beteiligtes Kraftfahrzeug liegt nicht vor; die Baumgefahr war für die Klägerin vor ihrem plötzlichen Eintritt nicht erkennbar.

## 6. Verletzungen und Schmerzensgeld

Die Klägerin erlitt eine instabile Lendenwirbelfraktur mit inkompletter neurologischer Schädigung und eine Fraktur des rechten Unterarms. Zwei Operationen, die stationäre Akutbehandlung und anschließende Rehabilitation sind dokumentiert. Am 28. September benötigte sie Gehhilfen und auf längeren Wegen einen Rollstuhl. Sie leidet unter täglichen Schmerzen und kann Lasten und Treppen derzeit nicht selbständig bewältigen. Beweis: Anlage K4; sachverständiges Zeugnis Dr. Marlene Vogel, Unfallklinik Mainbogen, Klinikring 12, Würzburg, nach Entbindung von der Schweigepflicht; medizinisches Sachverständigengutachten.

Nach § 253 Abs. 2 BGB ist ein angemessenes Schmerzensgeld geschuldet. Die Orientierung von 90.000 EUR knüpft an Verletzungsschwere, Eingriffe, bisherige Dauer und die erhebliche Ungewissheit der funktionellen Erholung an. Sie ist keine behauptete Vergleichstabelle und kein aus einer fremden Entscheidung übernommener Tarif. Eine dauerhafte vollständige Lähmung wird nicht behauptet. Der Antrag erfasst in einheitlicher Bewertung alle im maßgeblichen Entscheidungszeitpunkt bekannten oder objektiv vorhersehbaren immateriellen Folgen. Eine künstliche Teilklage nur über die ersten Wochen wird nicht erhoben. Der Feststellungsantrag betrifft ausschließlich materielle Schäden.

## 7. Bezifferte materielle Positionen

Die Haushaltshilfe kostet 3.500 EUR für 140 tatsächlich abgerechnete Stunden zu 25 EUR. Die Tätigkeiten ersetzen den vorher von der Klägerin übernommenen Anteil im Dreipersonenhaushalt. Der unveränderte Eigenanteil ihres Ehemanns wird nicht bezahlt; seine zusätzliche unentgeltliche Unterstützung wird hier nicht nochmals bewertet. Die Rechnung betrifft einen abgeschlossenen Zeitraum bis 25. September. Genau diese abgerechneten Leistungen sind vom Feststellungsantrag ausgenommen; zusätzlicher ungedeckter Bedarf nach diesem Zeitraum wird dadurch nicht abgeschnitten. Beweis: Anlage K5, Zeugnis Hermine Daubner, Rosenquergasse 20, Würzburg; Zeugnis Friedrich Seifert, Anschrift der Klägerin. Die medizinische Erforderlichkeit ist erforderlichenfalls sachverständig zu klären.

Hinzu kommen 480 EUR für vier notwendige Fahrten zu angeordneten Untersuchungen, 18.200 EUR Fahrzeugschaden und 550 EUR Bergung. Der Fahrzeugbetrag beruht auf 19.800 EUR Wiederbeschaffungswert abzüglich tatsächlich erzieltem Restwert von 1.600 EUR. Der ausgewertete Privatmarkt enthält keinen gesondert abziehbaren Umsatzsteueranteil. Ein Neupreis wird nicht verlangt. Beweis: Anlage K5; Zeugnis und erforderlichenfalls Sachverständigengutachten zum Fahrzeugwert, Leopold Nowak, Prüfbogen 4, Würzburg. Die Summe beträgt genau 22.730 EUR.

Die Krankenkasse hat für die konkret genannten Haushaltshilfe- und Beförderungspositionen keine sachlich und zeitlich entsprechenden Leistungen erbracht oder nach den dokumentierten Entscheidungen zu erbringen. Übergegangene Krankenhaus- und Rehabilitationskosten sind ausgenommen. Maßgeblich ist bei § 116 Abs. 1 SGB X nicht allein, ob schon Geld floss, sondern auch, ob entsprechende Sozialleistungen zu erbringen sind. Die Klägerin beansprucht deshalb weder einen ihr nicht mehr zustehenden Trägerregress noch einen doppelten Ersatz. Die Angaben sind vor einer tatsächlichen Einreichung anhand aktueller Trägerauskünfte fortzuschreiben.

## 8. Feststellung, Zinsen und Verfahrensstand

Weitere materielle Schäden sind wegen möglicher zusätzlicher Rehabilitation, Hilfsmittel, Wohnanpassung, Haushaltsunterstützung und Erwerbseinschränkungen konkret möglich. Nach dem Befund vom 28. September besteht der Hilfebedarf fort; die bisher abgerechnete Haushaltshilfe endet dagegen schon am 25. September. Die Schadensentwicklung ist insgesamt noch nicht abgeschlossen. Die weiteren Bedarfe und die dazugehörigen Drittleistungen sind auch für den anschließenden Zeitraum bis zu diesem Entwurf noch nicht abschließend abgegrenzt und beziffert. Daraus folgt das Feststellungsinteresse nach § 256 Abs. 1 ZPO. Der Antrag erfasst diese weiteren materiellen Schäden ohne künstlichen späteren Beginn, nimmt aber die mit Antrag 1.2 verlangten Positionen und Ansprüche Dritter ausdrücklich aus. Die Klägerin verlangt kein heute ungeprüftes lebenslanges Kapital und übernimmt insbesondere keine interne Reserve als Schaden.

Die außergerichtliche Forderung und die Antwort des Beklagten ergeben sich aus Anlagen K8 und K9. Bei Erstellung dieses Entwurfs laufen die dort genannten Fristen noch. Deshalb werden ausschließlich Prozesszinsen aus §§ 291, 288 Abs. 1 Satz 2 BGB seit dem Tag nach einer erst künftig möglichen Zustellung beantragt. Weder Rechtshängigkeit noch Verzug werden rückwirkend fingiert. Eine Einreichung setzt die abschließende Mandantenentscheidung und den Abgleich des aktuellen Behandlungs- und Zahlungsstands voraus.

Leona Ehlers
Rechtsanwältin – Entwurf ohne Einreichung'''),
])]

CASES.append(dict(
    slug='kommunale-haftpflicht-personenschaden',
    title='Ottilie Kümmel: Stadt und Versicherer im Nachgang',
    summary='Die nachträglich aufgefundene Vertragsbestätigung ergänzt den früheren offenen Deckungsstand. Stadt und Versicherer grenzen Haftungsprüfung, einmaligen Selbstbehalt und fehlenden Rückversicherungsbedarf ab.',
    is_new=False,
    notes='Der Grundbestand und der vorhandene Klageentwurf bleiben unverändert. Neu eingegangene Vertragsinformationen stammen erst vom Nachmittag des 05.10.2026; sie werden nicht rückwirkend in die frühere Recherchelage hineingelesen. Die Gemeinde hat weiterhin weder gezahlt noch die Haftung anerkannt. Kein sachlicher Anlass für eine Beteiligung eines Landkreises.',
    core=['01_Archivnachtrag.eml','02_Stadt_Schadenmeldung.docx','03_Versicherer_Deckungsantwort.docx','04_Versicherer_Abstimmung.eml'],
    exhibits=[],
    attachments={
        '01_Archivnachtrag.eml':[f'{FOLDER}/03_Versicherer_Deckungsantwort.pdf'],
        '04_Versicherer_Abstimmung.eml':['schriftverkehr-und-klage/04_Anspruchsschreiben_Kuemmel.pdf',f'{FOLDER}/03_Versicherer_Deckungsantwort.pdf'],
    },
    documents=[
D('01_Archivnachtrag.eml','Bürgerhaus: Vertragsantwort jetzt eingegangen','2026-10-05T16:15:00+02:00','email', '''Liebe Mira,

die Vertragsverwaltung von Frankenbogen hat heute um 15:35 Uhr auf unsere konkrete Anfrage geantwortet. Die Bestätigung ist beigefügt. Meine Nachricht vom 2. Oktober war damals richtig: Wir hatten nur eine Prämienbuchung und keinen belastbaren Vertragsstand. Erst die heutige Antwort bestätigt Laufzeit, Einbeziehung des Bürgerhauses, den einmaligen Selbstbehalt und die Bearbeitungsstelle. Bitte ordne sie als neuen Eingang ein und ersetze nicht die alte Nachricht.

Unsere Stadt bleibt Auftraggeberin von Frau Klee. Der Versicherer hat erklärt, dass er die Schadenbearbeitung übernimmt, aber keine Haftungsanerkennung abgegeben. Die derzeit 342,50 EUR materieller Eigenaufwand und die Schmerzensgeldforderung sind deshalb weiter sachlich zu prüfen. Insbesondere kann ein erst am Folgetag ausgefülltes Kontrollblatt nicht nachträglich zu einem zeitgenauen Nachweis umgeschrieben werden.

Bitte leite die Unterlagen an Frau Klee weiter und stimme den Antwortentwurf mit dem benannten Bearbeiter ab. Eine zusätzliche Meldung an irgendeinen Ausgleich oder Rückversicherer sollen wir nach dessen ausdrücklicher Erklärung nicht versenden. Der kleine Fall bleibt bei der Stadt und ihrem Erstversicherer. Die Antwortbitte von Frau Kümmel zum 9. Oktober wird durch die Deckungsklärung nicht verlängert.

Viele Grüße
Gundula Pfennig, Risikostelle Stadt Hainbogen''','Gundula Pfennig <risiken@hainbogen.example>','Mira Morgenrot <recht@hainbogen.example>'),
D('02_Stadt_Schadenmeldung.docx','Kümmel – ergänzende Schadenmeldung mit tatsächlichem Kontrollstand','05.10.2026','letter', '''Stadt Hainbogen · Rechtsamt
Mira Morgenrot · Buchsbaumplatz 1 · 97299 Hainbogen

Frankenbogen Kommunalversicherung VVaG
Herrn Götz Linde · Versicherungsbogen 8 · 97080 Würzburg

Sehr geehrter Herr Linde,

wir übersenden Ihnen den ergänzten Schadenstand zum Sturz von Frau Ottilie Kümmel im Bürgerhaus am 12. September. Eigentümerin und Betreiberin ist unsere Stadt. Der Bücherabend wurde durch das Kulturamt innerhalb der öffentlich-rechtlich organisierten Benutzung veranstaltet. Ein privater Veranstalter oder ein externer Reinigungsunternehmer war nicht beteiligt. Die Sicherung des Eingangs lag bei unseren Beschäftigten.

Bitte legen Sie Ihrer Prüfung den unveränderten Chat zugrunde. Die Meldung der Pfütze ging um 18:03 Uhr ein; der Hausmeister antwortete um 18:04 Uhr. Der Sturz wurde um 18:08 Uhr gemeldet, gewischt wurde erst danach. Das Kontrollblatt wurde am Folgetag erstellt und beruht hinsichtlich 17:55 Uhr auf einer ungefähren Erinnerung. Wir wollen diese Unschärfe weder verschweigen noch als Beleg einer bestimmten früheren Kontrollminute verwenden. Die Zeugin am Büchertisch hat den Sturz beobachtet, die Reinigungskraft dagegen nicht.

Die ergänzte Forderung umfasst 297,50 EUR bezahlte Haushaltshilfe, 45 EUR für die gebrauchte Jacke und ein unbeziffertes Schmerzensgeld mit einer Orientierung von 2.500 EUR. Frühere Taxipositionen und eine Pauschale werden im jetzigen Klageentwurf nicht verlangt. Die Angehörigenhilfe wird nicht neben der Rechnung nochmals abgerechnet. Ein schriftlicher aktueller Heilungsverlauf steht noch aus.

Wir bitten um Bestätigung des konkreten Versicherungsschutzes und um Abstimmung der weiteren Bearbeitung. Der Stadt steht nach wie vor kein Beleg für eine besondere Ausgleichszugehörigkeit dieses Vorgangs zur Verfügung. Bitte benennen Sie ausdrücklich, ob Sie selbst eine weitere Meldung für erforderlich halten. Frau Klee prüft ausschließlich für unsere Stadt; eine Beauftragung für Sie wird daraus nicht hergeleitet. Eine Zahlung oder ein Haftungsanerkenntnis wurde nicht erklärt.

Mit freundlichen Grüßen
Mira Morgenrot
Rechtsamt'''),
D('03_Versicherer_Deckungsantwort.docx','Bürgerhaus Hainbogen – Vorgangsbestätigung nach Archivabgleich','05.10.2026','letter', '''Frankenbogen Kommunalversicherung VVaG
Götz Linde · Versicherungsbogen 8 · 97080 Würzburg

Stadt Hainbogen · Risikostelle
Frau Gundula Pfennig · Buchsbaumplatz 1 · 97299 Hainbogen

Sehr geehrte Frau Pfennig,

nach dem heute abgeschlossenen Archivabgleich bestätigen wir für diesen synthetischen Vorgang den Vertrag KH-HB-2026 mit Laufzeit vom 1. Januar bis 31. Dezember 2026. Versichert ist die gesetzliche Haftpflicht der Stadt aus dem eigenen Betrieb des Bürgerhauses einschließlich der eigenen Kulturveranstaltungen und des eigenen Reinigungsdiensts. Die Versicherungssumme beträgt 5.000.000 EUR je Ereignis. Der städtische Selbstbehalt beträgt 500 EUR je Ereignis und wird nach Prüfung der berechtigten Entschädigung einmalig im Verhältnis zwischen uns und der Stadt berücksichtigt.

Diese Bestätigung ergänzt den erst heute belegten Vertragsstand. Aus ihr folgt weder, dass die angemeldeten 2.842,50 EUR in voller Höhe geschuldet sind, noch dass die Klägerin wegen des Selbstbehalts weniger verlangen könnte. Nach derzeitigem Bearbeitungsstand liegt kein Anlass für einen Deckungsausschluss vor. Wir übernehmen die vereinbarte Prüfung und Anspruchsabwehr. Die medizinische Entwicklung und die begrenzte Aussagekraft des Kontrollblatts bleiben dabei offene Bewertungsfragen.

Für diesen Fall ist keine gesonderte Meldung der Stadt an eine Rückversicherung vorgesehen. Unser internes Modellprogramm setzt für eine Einzelfallmeldung eine erwartete eigene Nettobelastung von 750.000 EUR voraus. Diese Grenze wird nach dem dokumentierten Sachstand ersichtlich nicht erreicht. Wir bestätigen hiermit weder eine AKHA-Mitgliedschaft noch einen Zahlungsanspruch aus einem kommunalen Ausgleich. Bitte legen Sie in Ihrer Akte keine künstliche Forderung gegen eine weitere Ebene an.

Stimmen Sie einen etwaigen Regulierungsvorschlag vorher mit uns ab. Unsere Beteiligung verschiebt weder die gegenüber Frau Kümmel bezeichnete Antwortfrist noch das Mandat von Frau Klee. Wir möchten zunächst den aktualisierten Befund und die konkrete Zuordnung der Hilfeleistungen erhalten; ein kleiner, zeitnaher Vergleich kann danach geprüft werden. Die Stadt muss dafür kein fiktives Schuldanerkenntnis abgeben. Eine Zahlung wurde heute noch nicht veranlasst.

Mit freundlichen Grüßen
Götz Linde
Kommunale Haftpflicht'''),
D('04_Versicherer_Abstimmung.eml','Kümmel: nächste Schritte zur kleinen Regulierung','2026-10-05T16:40:00+02:00','email', '''Sehr geehrte Frau Morgenrot,

unsere Bestätigung und das Anspruchsschreiben sind nochmals beigefügt, damit wir über denselben Stand sprechen. Bitte lassen Sie Frau Klee zunächst den Zusammenhang zwischen der konkreten Warnmeldung und der nicht sofort abgesicherten Stelle bewerten. Eine pauschale Ablehnung mit dem Satz „bei Regen muss man aufpassen“ wäre nach den derzeitigen Unterlagen keine ausreichende Antwort auf den Vorwurf Ihrer Besucherinnen.

Der aktuelle Kontrollbefund zum Handgelenk soll zeigen, ob sich die bislang beschriebene unkomplizierte Heilung bestätigt. Wir brauchen für den Schmerzensgeldvergleich keine aus einem anderen Großschaden entlehnte Tabelle. Die beiden materiellen Positionen sind konkret und überschaubar; bei der Jacke geht es um den gebrauchten Wert von 45 EUR, nicht um den alten Kaufpreis.

Der Selbstbehalt wird nur einmal auf eine später feststehende Gesamtentschädigung bezogen. Solange keine Einigung getroffen und kein Betrag gezahlt wurde, führen wir keinen Erstattungseingang. Ihre Risikostelle erhält nach einer Regulierung eine nachvollziehbare Abrechnung. Ein Landkreis ist weder Betreiber des Bürgerhauses noch Vertragspartei; wir nehmen ihn deshalb nicht in den Verteiler auf. Bitte senden Sie uns Ihren abgestimmten Antwortentwurf bis zum 7. Oktober.

Mit freundlichen Grüßen
Götz Linde''','Götz Linde <goetz.linde@frankenbogen.example>','Mira Morgenrot <recht@hainbogen.example>'),
]))

CASES.append(dict(
    slug='akha-wuerzburg-rohrbruch',
    title='Zimt & Zange: Trocknung und Deckungsklärung',
    summary='Der Versorger meldet die begrenzte Teilforderung und erhält erstmals einen konkreten Versicherungsstand; vorläufige Schadenpositionen werden nicht zu einer Rückversicherungsforderung hochgerechnet.',
    is_new=False,
    notes='Erst am Nachmittag des 05.10.2026 ergänzte Vertragsauskunft. Die leere alte Ablagerubrik bleibt als damaliger Kenntnisstand erhalten. Keine pauschale AKHA-Zuordnung, kein Landkreis als künstlicher Beteiligter. Vorhandene 2.400-EUR-Teilklage und alle Altbelege unverändert.',
    core=['01_Versorger_Anmeldung.docx','02_Versicherer_Vertragsstand.docx','03_Archiv_Weiterleitung.eml','04_Rueckversicherung_Einordnung.eml'],
    exhibits=[],
    attachments={
        '03_Archiv_Weiterleitung.eml':[f'{FOLDER}/02_Versicherer_Vertragsstand.pdf','schriftverkehr-und-klage/04_Teilforderung_Zimt.pdf'],
        '04_Rueckversicherung_Einordnung.eml':[f'{FOLDER}/02_Versicherer_Vertragsstand.pdf'],
    },
    documents=[
D('01_Versorger_Anmeldung.docx','Straßenleitung Kaffeebogen – Ergänzung zur Schadenanmeldung','05.10.2026','letter', '''Kommunalversorgung Mainbogen GmbH
Mira Morgenrot · Netzlaubenweg 4 · 97076 Würzburg

Frankenbogen Kommunalversicherung VVaG
Frau Gerlinde Hahn · Versicherungsbogen 8 · 97080 Würzburg

Sehr geehrte Frau Hahn,

wir melden Ihnen den Rohrbruch vom 14. September anhand des heute ergänzten Aktenstands. Betreiberin der außerhalb des Gebäudes liegenden Straßenverteilungsleitung ist unsere Gesellschaft. Frau Waffel ist Eigentümerin des betroffenen Gebäudes und nicht Betreiberin des Straßennetzes. Das Leck und das Nachlassen des Wassereintritts nach der Absperrung sind im Einsatzbericht und Störungslog dokumentiert. Bitte legen Sie diese konkreten Daten zugrunde und behandeln Sie den Vorgang nicht ohne Ortsprüfung als hausinternen Leitungsschaden.

Herr Zimt verfolgt nun zunächst eine offene Teilforderung von 2.400 EUR netto für bezahlte Trocknungsleistungen. Die ergänzenden Nachrichten grenzen die betroffenen Leistungen und eine begrenzte Abtretung der Eigentümerin ab. Weder der gesamte vorläufige Ansatz von 15.100 EUR noch ausgefallener Umsatz wird als bereits feststehender Schaden in diese Forderung übernommen. Die Mühlen sind gebraucht und noch nicht abschließend auf Reparierbarkeit geprüft. Die Elektroarbeiten benötigen ebenfalls eine saubere Trennung zwischen Eigentümer- und Mieterpositionen.

Wir haben bislang keine Haftung anerkannt oder eine Zahlung geleistet. Frau Klee ist ausschließlich durch unsere Gesellschaft mit der rechtlichen Erstprüfung beauftragt. Bitte bestätigen Sie Ihre Deckungsposition und die dafür tatsächlich zugrunde gelegten Vertragsunterlagen. Unsere alte Ordnerbezeichnung „AKHA/Rückdeckung“ enthält keinen Beitrittsnachweis und soll auch von Ihnen nicht als solcher verwendet werden.

Wir möchten den Schaden sachgerecht regulieren und zugleich Doppelanmeldungen vermeiden. Teilen Sie bitte mit, ob Sie mit Frau Waffel eine eigene Forderungsaufstellung abstimmen oder ob wir diese zunächst über die Bevollmächtigten anfordern sollen. Die Antwortbitte des Herrn Zimt zum 12. Oktober bleibt bestehen. Eine Meldung durch uns an einen Rückversicherer ist ohne belegten Meldeweg weder vorgenommen noch beauftragt.

Mit freundlichen Grüßen
Mira Morgenrot
Kommunalversorgung Mainbogen GmbH'''),
D('02_Versicherer_Vertragsstand.docx','Rohrbruch Mainbogen – Deckungsstand und Meldeweg','05.10.2026','letter', '''Frankenbogen Kommunalversicherung VVaG
Gerlinde Hahn · Versicherungsbogen 8 · 97080 Würzburg

Kommunalversorgung Mainbogen GmbH
Frau Mira Morgenrot · Netzlaubenweg 4 · 97076 Würzburg

Sehr geehrte Frau Morgenrot,

wir bestätigen nach Eingang des Archivsatzes um 14:20 Uhr den für diese synthetische Akte gesetzten Vertrag WV-MB-2026 vom 1. Januar bis 31. Dezember 2026. Der versicherte Betrieb umfasst die öffentliche Wasserversorgung Ihrer Gesellschaft einschließlich der im Einsatzbericht bezeichneten Straßenverteilungsleitung. Die Deckungssumme beträgt 5.000.000 EUR je Ereignis. Für die Entschädigung ist ein Selbstbehalt Ihrer Gesellschaft von 1.000 EUR je Ereignis vereinbart. Abwehrkosten werden nach der gesonderten Kostenzusage geführt.

Für den gemeldeten Wasseraustritt übernehmen wir die Prüfung der gesetzlichen Haftpflicht und die vereinbarte Anspruchsabwehr. Die Einbeziehung des Betriebs bedeutet noch keine Anerkennung aller angemeldeten Positionen. Bei der Trocknung müssen insbesondere Zahlung, Leistungsgegenstand und die Reichweite der Abtretung zusammenpassen. Bei den Mühlen ist der bloße Ersatzbeschaffungspreis kein bereits festgestellter Schaden. Ein vier Tage entfallener Umsatz darf nicht ohne Abzug ersparter Aufwendungen als entgangener Gewinn behandelt werden.

Die neue Bestätigung ersetzt nicht rückwirkend Ihre Nachricht vom 2. Oktober. Damals fehlten diese Vertragsdaten. Sie begründet auch keine Mitgliedschaft in einem bestimmten Schadenausgleich. Für dieses Szenario ist nur unsere Direktversicherung belegt. Unsere eigene Rückversicherung wird von uns verwaltet; Ihre Gesellschaft meldet dort keinen Anspruch an. Die vorsorgliche Rückfrage zu dem alten Ordnernamen wird getrennt dokumentiert, damit daraus keine Phantomforderung entsteht.

Für die jetzige Teilforderung könnte eine später vollständig berechtigte Zahlung von 2.400 EUR im Innenverhältnis zu 1.000 EUR Selbstbehalt und 1.400 EUR Versicherungsleistung führen. Das ist ein bedingtes Rechenbeispiel, keine Abrechnung oder Zahlungszusage. Weitere berechtigte Ansprüche desselben Ereignisses lösen nicht nochmals denselben Selbstbehalt aus. Bitte führen Sie bis zur gemeinsamen Freigabe weder diese beiden Beträge als Zahlung noch eine weitere Ausgleichserstattung als Forderung.

Mit freundlichen Grüßen
Gerlinde Hahn
Haftpflicht Versorgung'''),
D('03_Archiv_Weiterleitung.eml','Rohrbruch: neue Vertragsantwort und begrenzte Teilforderung','2026-10-05T15:35:00+02:00','email', '''Sehr geehrte Frau Klee,

die heute eingegangene Antwort des Versicherers ist beigefügt, ebenso das bereits vorliegende Teilforderungsschreiben. Bitte ergänzen Sie Ihre Bewertung um diesen neuen Kenntnisstand. Unsere vorherige Anfrage bleibt in der Akte, weil bis heute Nachmittag tatsächlich keine Vertragsdaten belegt waren. Die Bezeichnung des alten leeren Unterordners wird weiterhin nicht als Nachweis einer AKHA-Mitgliedschaft verwendet.

Mir ist wichtig, dass die mögliche Rechnung 1.000 EUR Selbstbehalt und 1.400 EUR Versicherungsanteil nicht mit der noch offenen Haftungsprüfung verwechselt wird. Herr Zimt verlangt die 2.400 EUR von uns. Ein Selbstbehalt kann ihm nicht als genereller Kürzungsgrund entgegengehalten werden. Die neue Versichererantwort behandelt nur die interne Kostenzuordnung für den Fall einer berechtigten Regulierung.

Bitte prüfen Sie die Abtretungsnachrichten im Zusammenhang mit der tatsächlich bezahlten Trocknungsrechnung. Die technischen Fragen an die Mühlen und die Elektroinstallation sollen getrennt offenbleiben. Wir möchten jetzt einen präzisen Antwortentwurf zur Teilforderung und eine kurze Nachforderung zu den übrigen Positionen. Eine Gesamtfreigabe der ursprünglichen 15.100 EUR erteilen wir nicht. Auch eine Klage oder ein Vergleich ist nicht durch die Weiterleitung der Anlagen beauftragt.

Mit freundlichen Grüßen
Mira Morgenrot''','Mira Morgenrot <recht@mainbogen-versorgung.example>','Rechtsanwältin Clara Klee <clara@klee-kolben.example>'),
D('04_Rueckversicherung_Einordnung.eml','Mainbogen Wasseraustritt – interne Vertragsauskunft ohne Einzelmeldung','2026-10-05T16:05:00+02:00','email', '''Sehr geehrte Frau Hahn,

unsere Rückdeckungsabteilung hat Ihre interne Anfrage anhand des für die Übung gesetzten Vertragsspiegels geprüft. Der Wasserversorgungsvertrag fällt in das von Frankenbogen geführte allgemeine Haftpflichtportfolio mit 1.000.000 EUR Priorität auf unseren entschädigungsfähigen Nettoschaden und 4.000.000 EUR Limit darüber. Die Einzelfallmeldeschwelle beträgt 750.000 EUR erwarteter Nettobelastung. Diese interne Auskunft ist weder eine Zusage an den Versorger noch eine echte AKHA-Bedingung. Einen externen Rückversicherer haben wir wegen des alten Ordnernamens nicht angeschrieben.

Die mitgeteilte Teilforderung von 2.400 EUR und die sonstigen ungeprüften Positionen geben nach dem vorhandenen Stand keinen Anlass für eine Einzelanmeldung in dieser Schicht. Wir eröffnen deshalb keine Rückversicherungsabrechnung. Sollte sich später ein wesentlich anderer Großschadenumfang ergeben, wäre er mit tatsächlichen Belegen erneut zu bewerten; der alte Ordnername genügt dafür nicht.

Bitte stimmen Sie die sachliche Regulierung weiterhin unmittelbar mit unserer Versicherungsnehmerin ab. Die Beleganforderungen zu Trocknung, fremdem Eigentum und entgangenem Gewinn bleiben bei Ihrem Schadenreferat. Für diesen internen Vertragsabgleich werden keine Unterlagen des Anspruchstellers an zusätzliche externe Stellen übermittelt. Eine Rückversicherungsforderung von Frankenbogen ist aus unserem Austausch nicht entstanden; ein Zahlungseingang wird nicht gebucht.

Mit freundlichen Grüßen
Hannes Fink
Interne Rückdeckungsabteilung''','Hannes Fink <rueckdeckung@frankenbogen.example>','Gerlinde Hahn <gerlinde.hahn@frankenbogen.example>'),
]))

CASES.append(dict(
    slug='akha-wuerzburg-betriebsfahrzeug',
    title='Kehrmaschine 7: Großschadenbesprechung ohne vorschnelle Bezifferung',
    summary='Stadtbetriebe, Erstversicherer und Rückversicherer besprechen Gebäude, gebrauchte Technik und bloßen Nachbarumsatz; erst die neue Vertragsauskunft ermöglicht eine ausdrücklich bedingte Schichtenrechnung.',
    is_new=False,
    notes='Keine Änderung der alten 1.840.000-EUR-Anmeldesumme oder des bestehenden Gebäudeklageentwurfs. Vertragsdaten werden erstmals am 05.10.2026 nachmittags mitgeteilt. Die Spanne von 1,2 bis 2,1 Mio. EUR betrifft nur Geräte; sie ist weder Gutachten noch zusätzliche Forderung.',
    core=['01_Stadtbetriebe_Sachstand.docx','02_Versicherer_Grossschaden.docx','03_Anmeldung_Rueckversicherer.eml','04_Rueckversicherer_Rueckfrage.eml'],
    exhibits=[],
    attachments={
        '03_Anmeldung_Rueckversicherer.eml':[f'{FOLDER}/02_Versicherer_Grossschaden.pdf','12_Forderungsuebersicht.xlsx'],
        '04_Rueckversicherer_Rueckfrage.eml':[f'{FOLDER}/02_Versicherer_Grossschaden.pdf'],
    },
    documents=[
D('01_Stadtbetriebe_Sachstand.docx','Fahrzeug 7 – unveränderte Beweismittel und getrennte Anspruchsteller','05.10.2026','letter', '''Stadtbetriebe Steinbogen GmbH
Mira Morgenrot · Betriebshof Laubenring 9 · 97076 Würzburg

Frankenbogen Kommunalversicherung VVaG
Frau Gundula Pfennig · Versicherungsbogen 8 · 97080 Würzburg

Sehr geehrte Frau Pfennig,

wir bestätigen für die Großschadenbesprechung, dass Fahrzeug 7 nach dem Unfall vom 25. September unverändert in der Werkstatt steht. Herr Blech hat nach dem Ereignis keine Einstellung an der Feststellbremse vorgenommen. Die technische Untersuchung ist noch nicht abgeschlossen. Seine Angabe, den Hebel vermutlich angezogen zu haben, darf deshalb weder in eine sichere Funktionsbestätigung noch in ein bereits bewiesenes Versagen der Bremse umformuliert werden.

Eigentümerin und Halterin der 40 km/h schnellen Maschine ist unsere Gesellschaft. Der Gewerbehof war während der Geschäftszeiten für Lieferverkehr zugänglich. Nach dem derzeitigen Stand war der Unfall keine hoheitliche Einsatzfahrt des Landkreises. Wir sehen daher keinen Anlass, einen Landkreis als haftenden Rechtsträger einzusetzen. Die Gemeinde ist über ihre Beteiligung an unserer GmbH informiert; eine eigene Schuldübernahme hat sie nicht erklärt.

Die Gebäudeunterlagen der Hofbogen Immobilien GmbH, die Geräteliste der Prisma Bühnenbildtechnik GmbH und die Nachricht der Nuri Nudelwerk GmbH bleiben getrennte Eingänge. Die 1.650.000 EUR für Prisma beruhen auf Neupreisansätzen für gebrauchte Geräte. Die Spanne von 1.200.000 bis 2.100.000 EUR betrifft dieselben Geräte und wird nicht zusätzlich addiert. Niemand hat die Geräte entsorgt. Ein bloßer Produktionsumsatz des Nachbarbetriebs wird ebenfalls nicht als feststehender Eigentumsschaden bestätigt.

Bitte klären Sie anhand des heute nachgereichten Vertragssatzes Deckung und Rückversicherungsweg. Ihre Beauftragung von Frau Klee ist allein Ihr Mandat; wir nehmen hiermit keinen zusätzlichen Anwaltsauftrag vor. Für die fachliche Abstimmung stehen unsere Fuhrparkleiterin und der Werkstattleiter zur Verfügung. Bitte geben Sie uns vorab konkrete Fragen, damit das Gespräch die offenen Tatsachen aufklärt und nicht nur die bisherige Anmeldesumme wiederholt. Eine Zahlung, Haftungsanerkennung oder Gesamtfreigabe ist bisher nicht erfolgt.

Mit freundlichen Grüßen
Mira Morgenrot
Stadtbetriebe Steinbogen GmbH'''),
D('02_Versicherer_Grossschaden.docx','Kehrmaschine – ergänzter Vertragsstand und getrennte Schadenbewertung','05.10.2026','letter', '''Frankenbogen Kommunalversicherung VVaG
Gundula Pfennig · Versicherungsbogen 8 · 97080 Würzburg

Stadtbetriebe Steinbogen GmbH
Frau Mira Morgenrot · Betriebshof Laubenring 9 · 97076 Würzburg

Sehr geehrte Frau Morgenrot,

der vollständige Archivsatz ist heute um 14:45 Uhr eingegangen. Für diese synthetische Akte bestätigen wir den Kfz-Haftpflichtvertrag KFZ-SB-2026 für Fahrzeug 7 mit Laufzeit vom 1. Januar bis 31. Dezember 2026 und einer für dieses Ereignis verfügbaren Sachschadendeckung von 5.000.000 EUR. Ein Selbstbehalt Ihrer Gesellschaft ist in diesem Vertrag nicht vereinbart. Die zeitweise ausgeschaltete Kehrfunktion beendet die Kfz-Deckung nicht. Den genauen Unfallablauf und die behaupteten Schäden prüfen wir weiterhin.

Unsere direkte Modellrückversicherung bei Auenfels setzt eine Priorität von 1.000.000 EUR auf den von uns tatsächlich getragenen entschädigungsfähigen Schaden aus einem Ereignis und ein anschließendes Limit von 4.000.000 EUR voraus. Bearbeitungs- und Abwehrkosten bleiben außerhalb dieser Bezugsgröße. Die Meldeschwelle beträgt 750.000 EUR erwartete Nettobelastung. Das ist keine allgemeine AKHA-Regel, sondern der für diesen Übungsfall neu belegte Vertragsstand; die frühere Nachricht über fehlende Unterlagen bleibt als damaliger Kenntnisstand erhalten.

Für die Arbeitsbesprechung verwenden wir ein ausdrücklich bedingtes Beispiel: Würden 145.000 EUR Gebäudeschaden und 1.200.000 EUR ersatzfähiger Geräteschaden anerkannt und ausgezahlt, ergäbe sich eine Bezugsgröße von 1.345.000 EUR und ein möglicher Schichtbetrag von 345.000 EUR. Die 1.200.000 EUR sind nur die Untergrenze der ungeprüften Gerätespanne, kein Gutachten. Der Nachbarumsatz von 45.000 EUR wird nicht ohne eigene Anspruchsprüfung hinzugefügt. Das Rechenbeispiel ersetzt weder die dokumentierte Anmeldung von 1.840.000 EUR noch eine tatsächliche Zahlung.

Wir melden wegen des möglichen Umfangs vorsorglich an Auenfels. Die Anspruchsteller erhalten dadurch keinen neuen Ansprechpartner für ihre Forderungen. Bitte sichern Sie Geräte, Bremsbefund und Gebäudedokumentation. Über Vergleichszahlungen entscheiden wir erst nach getrennter Prüfung der Anspruchsberechtigung, Reparaturmöglichkeiten, Restwerte und Doppelpositionen. Bisher ist aus dieser Schadenbearbeitung keine Zahlung ausgeführt worden.

Mit freundlichen Grüßen
Gundula Pfennig
Kfz-Großschaden'''),
D('03_Anmeldung_Rueckversicherer.eml','Fahrzeug 7: vorsorgliche Meldung, Gerätewerte weiterhin offen','2026-10-05T15:20:00+02:00','email', '''Sehr geehrte Frau Sturm,

wir melden den Kehrmaschinenunfall vom 25. September vorsorglich unter dem heute bestätigten Programm. Der Vertragsbrief und die bisherige Forderungsübersicht sind beigefügt. Die Übersicht bleibt bewusst auf der Ebene angemeldeter Beträge: 145.000 EUR Gebäude, 1.650.000 EUR Geräte und 45.000 EUR Umsatz des Nachbarbetriebs, insgesamt 1.840.000 EUR. Aus dieser Summe wird heute keine Erstattungsforderung an Sie errechnet.

Prisma muss Seriennummern, Anschaffungsbelege und Reparaturmöglichkeiten beibringen. Die Neuwerte gebrauchter Technik sind kein gesicherter Verlust. Auch die alternative Schätzung von 1.200.000 bis 2.100.000 EUR ist ausschließlich eine Spanne derselben Geräteposition. Wir werden weder deren Mittelwert noch die obere Grenze ungeprüft als anerkannten Schaden behandeln.

Der beigefügte Brief erläutert lediglich ein mögliches Szenario mit 1.345.000 EUR Gesamtschaden und 345.000 EUR oberhalb Ihrer Priorität. Bitte bestätigen Sie die Vorabmeldung und nennen Sie Ihren Unterlagenbedarf vor einer Vergleichsabstimmung. Frau Klee prüft ausschließlich für uns. Wir übersenden keine vermeintliche Zustimmung der Stadtbetriebe zu einer Zahlung; eine solche liegt nicht vor. Ebenso gibt es noch keinen Bankabfluss, den wir abrechnen könnten.

Mit freundlichen Grüßen
Hannes Fink''','Hannes Fink <rueckdeckung@frankenbogen.example>','Adelheid Sturm <schaden@auenfels-rueck.example>'),
D('04_Rueckversicherer_Rueckfrage.eml','Kehrmaschine: Eingang bestätigt, keine Freigabe aus Neupreisliste','2026-10-05T16:10:00+02:00','email', '''Sehr geehrter Herr Fink,

wir bestätigen den Eingang als Vorabmeldung unter dem in Ihrem beigefügten Brief bezeichneten Modellprogramm. Das mögliche Überschreiten der Meldeschwelle ist nachvollziehbar. Eine Rückversicherungsforderung oder ein Zahlungseingang ist hierdurch nicht entstanden. Die 345.000 EUR bleiben eine bedingte Szenariogröße, bis der entschädigungsfähige Nettoschaden und Ihre Zahlungen nachgewiesen sind.

Bitte übermitteln Sie für eine spätere Abstimmung die technische Bewertung der beschädigten Geräte mit Reparaturkosten, verbleibendem Nutzwert und gegebenenfalls Restwert. Dabei muss deutlich bleiben, wer Eigentümer jedes Geräts ist. Für das Gebäude benötigen wir eine Zuordnung von Wiederherstellung und etwaiger Verbesserung. Die Nudelwerk-Position ist getrennt nach Anspruchsgrundlage und tatsächlichem Ertragsausfall zu prüfen; 45.000 EUR Umsatz sind keine selbstverständliche Entschädigung.

Wir bitten außerdem um eine Ereigniszuordnung für alle drei Anspruchsteller. Ein gemeinsamer Unfall kann nach dem Vertrag ein Ereignis bilden, ohne dass jede Forderung deshalb berechtigt wird. Eine zusätzliche Priorität je Gerät oder je Anspruchsteller wird nach dem bestätigten Programm nicht abgezogen. Bitte informieren Sie uns vor einer Einigung, die Ihre erwartete Nettobelastung über 1.000.000 EUR erhöht. Unsere interne Abstimmung darf nicht als angebliches Recht der Geschädigten auf eine direkte Regulierung durch Auenfels dargestellt werden.

Mit freundlichen Grüßen
Adelheid Sturm''','Adelheid Sturm <schaden@auenfels-rueck.example>','Hannes Fink <rueckdeckung@frankenbogen.example>'),
]))

CASES.append(dict(
    slug='akha-wuerzburg-geburtsschaden',
    title='Nora Winter: abgeschlossene Familienzahlung und offener interner Ausgleich',
    summary='Klinik, kommunaler Gesellschafter, Erstversicherer und Rückversicherer gleichen den bereits bezahlten Vergleich ab. Zwei offene Beträge von jeweils 3,2 Mio. EUR liegen auf verschiedenen Ebenen und dürfen nicht addiert werden.',
    is_new=False,
    notes='Der Teilvergleich vom 23.09.2026 und die am 29.09.2026 ausgeführte Schlusszahlung bleiben unangetastet. Keine neue Klage oder Zahlungsforderung gegen die Familie. Historischer Klageentwurf vor Vergleich bleibt erhalten. Modellwerte exakt wie bestehende Arbeitsmappe: 13,2 Mio. EUR Familienzahlung, 1,5 Mio. EUR Mitgliedsselbstbehalt, 11,7 Mio. EUR Bruttoausgleich, 8,5 Mio. EUR Eingang, 3,2 Mio. EUR offen, 10 Mio. EUR ursprüngliche Priorität, 650.000 EUR separate Drittregressreserve.',
    core=['01_Klinik_Abschlussbrief.docx','02_Erstversicherer_Schichtenbrief.docx','03_Rueckversicherer_Pruefstand.eml','04_Klinik_Gesellschafterbericht.eml'],
    exhibits=[],
    attachments={
        '03_Rueckversicherer_Pruefstand.eml':['14_Interne_Modellvereinbarung.docx',f'{FOLDER}/02_Erstversicherer_Schichtenbrief.pdf'],
        '04_Klinik_Gesellschafterbericht.eml':[f'{FOLDER}/01_Klinik_Abschlussbrief.pdf',f'{FOLDER}/02_Erstversicherer_Schichtenbrief.pdf','12_Zahlung_und_Schichten.xlsx'],
    },
    documents=[
D('01_Klinik_Abschlussbrief.docx','Winter – Familienzahlung abgeschlossen, Unterlagen für interne Abrechnung','05.10.2026','letter', '''Klinik Mainblick GmbH
Mareike Seidel · Mainauenweg 18 · 97074 Würzburg

Frankenbogen Kommunalversicherung VVaG
Frau Gundula Pfennig · Versicherungsbogen 8 · 97080 Würzburg

Sehr geehrte Frau Pfennig,

wir bestätigen nach Abgleich mit dem Elternschreiben und Ihrem Zahlungsjournal, dass die Schlusszahlung von 12.000.000 EUR am 29. September ausgeführt wurde. Zusammen mit den vier früheren Vorschüssen von 300.000 EUR, 250.000 EUR, 350.000 EUR und 300.000 EUR sind die im Teilvergleich vereinbarten 13.200.000 EUR vollständig an Nora geleistet. Die Familie hat seitdem keine neue Forderung erhoben. Der historische Klagevorentwurf betrifft den Stand vor dem Vergleich und ist kein offener Gerichtsauftrag.

Für den Bericht an unsere kommunale Gesellschafterin benötigen wir eine verständliche Darstellung der noch offenen internen Abrechnung. Nach Ihrem Stand vom 2. Oktober hat Frankenbogen 8.500.000 EUR aus der Ausgleichsebene erhalten; weitere 3.200.000 EUR stehen dort offen. Diese Differenz ist kein noch unbezahlter Betrag des Vergleichs. Bitte vermeiden Sie in den Auswertungen die missverständliche Überschrift „Restforderung Winter“, wenn damit Ihre eigene Ausgleichsforderung gemeint ist.

Die gesonderte Reserve von 650.000 EUR betrifft mögliche übergegangene Ansprüche der Kranken- und Pflegekasse. Sie ist weder eine sechste Familienzahlung noch eine freie Reserve für eine erneute Abfindung. Uns liegt noch keine prüffähige abschließende Trägerabrechnung vor. Bitte senden Sie hierfür nur die konkret erforderlichen Nachfragen; die Eltern sollen nicht erneut bereits erledigte Zahlungsvoraussetzungen nachweisen müssen.

Unsere Stellungnahme enthält kein Anerkenntnis eines Trägerregresses und keine Änderung des Vorbehalts für bei Vergleichsschluss nicht vorhersehbare weitere Schäden. Die in der Deckungsbestätigung genannte Versicherungssumme von 30.000.000 EUR und der fehlende Selbstbehalt der Klinik bleiben vom internen Mitgliedsselbstbehalt unberührt. Bitte bestätigen Sie, dass eine ausstehende Rückversicherungszahlung weder die bereits erfüllte Familienzahlung noch eine zusätzliche Zahlungspflicht unserer Klinik auslöst.

Mit freundlichen Grüßen
Mareike Seidel
Geschäftsführerin'''),
D('02_Erstversicherer_Schichtenbrief.docx','Winter – Abgleich von Erfüllung, Ausgleich und Rückversicherung','05.10.2026','letter', '''Frankenbogen Kommunalversicherung VVaG
Hannes Fink · Versicherungsbogen 8 · 97080 Würzburg

Klinik Mainblick GmbH
Frau Mareike Seidel · Mainauenweg 18 · 97074 Würzburg

Sehr geehrte Frau Seidel,

die Leistung an Nora ist vollständig erfüllt. Der in unseren Unterlagen enthaltene Mitgliedsselbstbehalt von 1.500.000 EUR wird ausschließlich von Frankenbogen im internen Modell getragen. Er ist kein Selbstbehalt Ihrer Klinik und wird weder von Ihnen noch von der Familie nachgefordert. Ihr Krankenhaushaftpflichtvertrag enthält nach der bereits vorliegenden Bestätigung keinen Selbstbehalt.

Die interne Anmeldung beruht auf insgesamt 13.200.000 EUR tatsächlicher Entschädigung einschließlich der alten Vorschüsse. Nach Abzug von 1.500.000 EUR verbleiben 11.700.000 EUR Bruttoforderung an die Ausgleichsebene. Davon gingen am 2. Oktober 8.500.000 EUR bei Frankenbogen ein; offen bleiben 3.200.000 EUR. Unsere momentane Liquiditätsbelastung beträgt deshalb 4.700.000 EUR. Sie ist von der nach vollständigem Modellvollzug vorgesehenen endgültigen Eigenbelastung von 1.500.000 EUR zu unterscheiden.

Die Ausgleichsebene hat ihrerseits eine Anmeldung von 3.200.000 EUR an Auenfels. Nach der Modellvereinbarung bezieht sich die dortige Priorität von 10.000.000 EUR auf den ursprünglichen Gesamtschaden von 13.200.000 EUR und nicht auf den zuvor um unseren Mitgliedsselbstbehalt gekürzten Betrag. Deshalb ergibt sich 3.200.000 EUR, nicht der früher fehlerhaft genannte Betrag von 1.700.000 EUR. Der offene Betrag bei Frankenbogen und der offene Betrag bei der Ausgleichsebene sind zwei Abrechnungsbeziehungen derselben oberen Schicht und werden nicht zu 6.400.000 EUR addiert.

Bis heute liegt weiterhin kein Zahlungseingang von Auenfels vor. Die Anmeldung ersetzt weder Fälligkeitsprüfung noch Bankabgleich. Die gesonderte Drittregressreserve von 650.000 EUR ist in keiner dieser Zahlungs- und Schichtenrechnungen enthalten. Für sie ist keine Rückdeckungsforderung gebucht. Tatsächliche AKHA-Vertragsbedingungen werden durch diese frei gesetzte Modellvereinbarung nicht behauptet. Die Eltern haben mit diesen internen Vorgängen nichts zu veranlassen; wir verlangen keine neue Bestätigung ihrer bereits belegten Schlusszahlung.

Mit freundlichen Grüßen
Hannes Fink
Rückdeckung und Controlling'''),
D('03_Rueckversicherer_Pruefstand.eml','Winter: Kassenabgleich vollständig, obere Schicht weiter ungeprüft','2026-10-05T15:50:00+02:00','email', '''Sehr geehrte Frau Zobel,

der Kassenabgleich zu den fünf ausgeführten Entschädigungszahlungen liegt jetzt vollständig vor. Unter dem beigefügten Modellstand ist Ihre Anmeldung von 3.200.000 EUR rechnerisch nachvollziehbar: 13.200.000 EUR ursprünglicher anrechenbarer Schaden abzüglich 10.000.000 EUR Priorität. Der Mitgliedsselbstbehalt von Frankenbogen wird bei dieser Bezugsgröße nicht nochmals vorab abgezogen. Wir korrigieren damit keinen Vergleich, sondern ordnen die interne Rechnung den vereinbarten Ebenen zu.

Unsere Leistungsprüfung ist heute noch nicht abgeschlossen. Es gibt keine Abrechnungsbestätigung und keinen Zahlungseingang bei Ihnen. Bitte behandeln Sie den Eingang der Belege nicht als Auszahlung. Die Kosten der Regulierung und die separate Reserve von 650.000 EUR für offene Drittregresse gehören nicht zur angemeldeten Vergleichssumme. Eine spätere Trägerforderung wäre nach Anspruch und Vertragszuordnung gesondert vorzulegen.

Wir benötigen noch Ihre Bestätigung, dass frühere Vorschüsse nicht bereits separat durch uns erstattet wurden. Nach den übermittelten Konten besteht dafür kein Anhaltspunkt. Die Familie ist keine Vertragspartnerin dieser Rückversicherung und soll nicht um eine weitere Auszahlungsfreigabe gebeten werden. Ihre Bruttoabrechnung gegenüber Frankenbogen bleibt ein eigenes Verhältnis; wir treffen mit dieser Nachricht keine Aussage über deren Fälligkeit oder Vorfinanzierung. Bitte halten Sie beide offenen 3.200.000-EUR-Posten getrennt.

Mit freundlichen Grüßen
Adelheid Sturm''','Adelheid Sturm <schaden@auenfels-rueck.example>','Ottilie Zobel <ausgleich@modell-ausgleich.example>'),
D('04_Klinik_Gesellschafterbericht.eml','Winter: Bericht an die kommunale Gesellschafterin ohne neue Familienforderung','2026-10-05T16:25:00+02:00','email', '''Sehr geehrte Frau Morgenrot,

für die Beteiligungsverwaltung der Stadt Hainbogen, die nach unserem Beteiligungsspiegel 60 Prozent der Geschäftsanteile hält, übersende ich unsere Abschlusskorrespondenz und die unveränderte Arbeitsmappe. Die dort abgebildete Familienleistung von 13.200.000 EUR ist vollständig bezahlt. Der historische Klageentwurf ist mit Vergleich und Zahlung überholt; er wird nur als früherer Arbeitsstand aufbewahrt. Bitte nehmen Sie ihn nicht als neues Prozessrisiko in den Bericht für die Gesellschafterin auf.

Die noch offenen 3.200.000 EUR betreffen eine Forderung unseres Erstversicherers an seine Ausgleichsebene. Daneben meldet diese Ebene denselben oberen Anteil an ihren Rückversicherer. Die Beträge werden nicht zusammengerechnet. Aus den internen offenen Erstattungen folgt keine neue Einlageforderung an eine kommunale Gesellschafterin und keine Kürzung der bereits erfüllten Zahlung an Nora. Wir berichten Ihnen als Beteiligungsverwaltung; Sie übernehmen dadurch weder die Behandlungsverantwortung noch eine eigene Versicherungsrolle.

Die 650.000 EUR Drittregressreserve bleibt eine separate, noch nicht durch Einzelabrechnungen belegte Schätzung. Die Familie hat nach dem Vergleich keine neue Forderung gestellt. Bitte verwenden Sie im Sitzungsvermerk den Zusatz „interne Erstattung offen“, damit nicht erneut der Eindruck eines ungedeckten Restbetrags für Nora entsteht. Vor einem Bericht nach außen sind personenbezogene Behandlungsdetails gesondert zu reduzieren. Die vollständige Akte bleibt bei den mit der Regulierung befassten Stellen.

Mit freundlichen Grüßen
Mareike Seidel''','Mareike Seidel <geschaeftsfuehrung@klinik-mainblick.example>','Mira Morgenrot <recht@hainbogen.example>'),
]))

for _case in CASES:
    _case['core'] = [f'{FOLDER}/{file}' for file in _case['core']]
