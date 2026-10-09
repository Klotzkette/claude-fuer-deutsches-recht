"""Offene Vergleichsunterlagen zum Berliner Bestandsfall, Stand 09.10.2026.

Die Daten sind Rohmaterial für die weitere anwaltliche Bearbeitung. Weder ein
Vergleichsschluss noch ein Gerichtsausgang oder ein neuer Beschluss wird fingiert.
"""
from textwrap import dedent


def doc(name, title, day, sender, recipient, body):
    return dict(file=name + '.docx', title=title, date=day, sender=sender,
                recipient=recipient, body=dedent(body).strip())


def mail(name, title, day, sender, recipient, body, attachments=()):
    return dict(file=name + '.eml', title=title, date=day, sender=sender,
                recipient=recipient, body=dedent(body).strip(), attachments=list(attachments))


CASE = dict(
    slug='gesellschafterstreit-klageerwiderung-berlin',
    title='Offener Vergleich und Gesellschaftervereinbarung – Berlin',
    entry='Beginnen Sie mit dem erweiterten Gesellschaftsauftrag V06. V01 ist ein ungezeichneter Verhandlungsentwurf vom 9. Oktober 2026. Lesen Sie dazu die gegensätzlichen Positionen V02 bis V04 und das Gesprächsprotokoll V05. V07 bis V11 dokumentieren Übermittlung und Rückmeldungen. Zuerst bleibt die Prozessverteidigung zu bearbeiten; Vergleichsgespräche verändern die Fristen am 9. und 23. Oktober nicht.',
    docs=[
doc('V01_Gesellschaftervereinbarung_Entwurf', 'Gesellschaftervereinbarung und Vergleichsrahmen – Entwurf', '09.10.2026',
    'Kanzlei Walburga Fürst | Berliner Straße 91, 13189 Berlin\nArbeitsfassung der Klägervertreterin, 13:15 Uhr',
    'Spreebogen Lichtwerk GmbH; Kunigunde Rabenstein; Gottfried Seidel; Ottilie Heller', '''
ENTWURF – Stand 9. Oktober 2026, 13:15 Uhr. Nicht unterschrieben und nicht abschließend abgestimmt. Die nachfolgend als Alternative bezeichneten Regelungen sind konkurrierende vollständige Regelungsvorschläge. Ihre Aufnahme bedeutet weder Zustimmung noch Wahl einer Alternative. Insbesondere sind Organstellung, Rechnungsbereinigung, Finanzierungsgrenze und Vollzug offen. Eine Gegenzeichnung dieser Arbeitsfassung ist nicht erbeten.

## 1 Parteien, Ausgangslage und Gegenstand

1.1 Vertragsparteien sollen die Spreebogen Lichtwerk GmbH, Mühlenstraße 64, 13187 Berlin, sowie Kunigunde Rabenstein, Gottfried Seidel und Ottilie Heller jeweils persönlich sein. Die Gesellschaft ist in der Endfassung durch die nach Abschnitt 14 nachgewiesene vertretungsberechtigte Person zu bezeichnen. Rabensteins persönliche Erklärung und eine Erklärung für die Gesellschaft werden getrennt abgegeben.

1.2 Das Stammkapital bleibt bei 25.000 EUR. Rabenstein hält Anteil Nr. 1 über 10.000 EUR, Seidel Anteil Nr. 2 über 8.750 EUR und Heller Anteil Nr. 3 über 6.250 EUR; die Beteiligungen betragen unverändert 40, 35 und 25 Prozent. Diese Vereinbarung enthält weder eine Kapitalerhöhung noch eine Anteilsabtretung.

1.3 Die Parteien wollen ihre Zusammenarbeit im Lichtbetrieb und eine mögliche Beilegung des Verfahrens 32 O 187/26 vor dem Landgericht Berlin II regeln. Sie geben damit keine gemeinsame Bewertung des Beschlusses vom 9. September oder der Zahlung über 18.400 EUR ab. Die Vereinbarung soll schuldrechtliche Pflichten begründen; erforderliche gesellschaftsrechtliche Beschlüsse und Satzungsänderungen werden gesondert vollzogen.

## 2 Beratung, Verhandlungsbefugnis und Kosten des Entwurfs

2.1 Dr. Adelbert Feuchtwanger berät und vertritt ausschließlich die Gesellschaft. Walburga Fürst vertritt ausschließlich Seidel. Rabenstein und Heller handeln hinsichtlich ihrer persönlichen Beteiligungen auf eigene Rechnung und entscheiden selbst über zusätzliche Beratung. Die Zuleitung eines Entwurfs begründet kein gemeinsames Mandat und keine Befugnis eines Anwalts, für weitere Parteien Erklärungen abzugeben.

2.2 Jede Partei trägt ihre eigenen Beratungskosten. Kosten eines gemeinsam beauftragten Notars oder Rechnungsprüfers dürfen erst nach gemeinsamer Festlegung von Auftrag, Kostenrahmen und Kostenträger ausgelöst werden. Die Gesellschaft übernimmt keine persönlichen Beratungskosten eines Gesellschafters ohne gesonderte wirksame Entscheidung. Prozesskosten werden ausschließlich nach Abschnitt 13 behandelt.

2.3 Änderungen werden durch die jeweiligen Bevollmächtigten oder durch die persönlich betroffene Partei bestätigt. Schweigen auf einen Entwurf, die Teilnahme an einer Besprechung und die Übermittlung von Unterlagen gelten nicht als Zustimmung. Eine Verhandlungsbefugnis umfasst weder Abschlussvollmacht noch Prozessverzicht.

## 3 Künftige Geschäftsführung und technische Verantwortung

3.1 Alternative Seidel: Die Parteien veranlassen eine gesonderte, auf die Zukunft gerichtete Entscheidung über Seidels Bestellung zum technischen Geschäftsführer. Für sechs Monate ab vollständigem Vollzug wird eine gemeinsame Vertretung durch Rabenstein und Seidel vorgesehen. Erforderliche Satzungs-, Beschluss- und Registermaßnahmen werden zuvor festgelegt. Die Parteien überprüfen nach sechs Monaten anhand der Einkaufsberichte die dauerhafte Organisationsform. Eine rückwirkende Anerkennung des Septemberbeschlusses ist damit nicht verbunden.

3.2 Alternative Gesellschaft: Rabenstein führt die Gesellschaft weiter; Seidel übernimmt zunächst bis zum 31. Januar 2027 die technische Projektbegleitung im Rahmen einer gesondert vereinbarten Aufgabenbeschreibung. Er erhält dadurch keine rechtsgeschäftliche Vertretungs- oder Bankbefugnis. Nach Prüfung der Rechnungsunterlagen und der Zusammenarbeit wird erneut über eine Organbestellung beraten; eine Bestellung wird nicht zugesagt.

3.3 Keine Alternative gilt bereits durch diesen Entwurf als gewählt. Bis zum gesonderten wirksamen Vollzug werden aus der Vergleichsverhandlung weder eine neue Bestellung noch ein Rücktritt abgeleitet. Die Parteien lassen den streitigen bisherigen Organstatus rechtlich gesondert beurteilen.

## 4 Anstellungsverhältnis und technische Mitarbeit

4.1 Die Parteien behandeln Organstellung und Anstellungsverhältnis getrennt. Die Septembervergütung ist gezahlt. Die Oktoberabrechnung und alle weiteren Ansprüche werden anhand des bestehenden Anstellungsvertrags gesondert geprüft; die Abberufung wird in dieser Vereinbarung nicht als Kündigung erklärt. Weder Vergütungsverzicht noch Abgeltung bisheriger Ansprüche werden durch eine Aufgabenänderung stillschweigend vereinbart.

4.2 Für eine technische Übergangsrolle sind Arbeitsumfang, Weisungsweg, Baustellenzugang, Haftpflichtdeckung und Vergütung vor Beginn schriftlich festzulegen. Seidel bietet drei Projekttage wöchentlich bis Ende Januar an; die Gesellschaft verlangt zusätzlich eine erreichbare Vertretung bei Störungen. Ohne diese Einigung entsteht keine Verpflichtung zu einer unentgeltlichen Beratung oder zu einer zusätzlichen Bereitschaft.

4.3 Seidel erhält die für vereinbarte Aufgaben notwendigen Unterlagen und abgestimmten Kundentermine. Er darf gegenüber Kunden keine Organbefugnis aus der Übergangsrolle ableiten. Rabenstein benennt für jede Bestellung eine verantwortliche Person. Persönliche Bankzugänge werden nicht allein wegen einer technischen Mitarbeit reaktiviert. Die Fortgeltung bestehender Ansprüche bleibt unberührt.

## 5 Einkaufsfreigaben und Zahlungsablauf

5.1 Die Geschäftsordnung vom 10. Januar 2025 wird durch gesonderten Beschluss präzisiert. Zusammengehörige Bestellungen eines Projekts dürfen nicht zur Umgehung einer Freigabe aufgeteilt werden. Vor Freigabe sind Leistungsumfang, Bruttopreis, Liefertermin und Vergleichsangebot oder die belegte Unerreichbarkeit eines Vergleichsangebots vorzulegen. Eine Eingangsbestätigung der Buchhaltung ersetzt keine Entscheidung.

5.2 Alternative Gesellschaft: Für Verpflichtungen und Zahlungen über 7.500 EUR brutto ist eine dokumentierte zweite Freigabe erforderlich. Alternative Seidel: Die bestehende Grenze von 10.000 EUR brutto bleibt erhalten. In beiden Alternativen benennt ein gesonderter Organisationsbeschluss die entscheidungsbefugten Personen; Heller übernimmt durch ihre Buchhaltungstätigkeit keine Geschäftsführungsverantwortung.

5.3 Sofortmaßnahmen bei unmittelbarer Gefahr für Personen oder erheblichen Sachschaden werden noch am selben Tag mit Anlass, Betrag und Empfänger dokumentiert. Ein Kundentermin allein begründet keine Ausnahme. Bankberechtigungen und interner Freigabeablauf werden gemeinsam überprüft. Diese Innenregelung behauptet keine automatische Unwirksamkeit eines dennoch gegenüber einem Lieferanten abgeschlossenen Geschäfts; die Folgen eines Verstoßes werden gesondert beurteilt.

## 6 Geschäfte mit Gesellschaftern und nahestehenden Unternehmen

6.1 Vor jeder Beauftragung eines Gesellschafters oder seines Unternehmens werden Beteiligung, Leistungsumfang und Preis offengelegt. Dies erfasst die Seidel Bühnenservice e.K. ohne Betragsuntergrenze. Die nach Satzung erforderliche Gesellschafterentscheidung wird vor Auftrag und Zahlung gesondert herbeigeführt; anwendbare Stimmverbote werden geprüft und protokolliert. Der betroffene Gesellschafter erteilt sich keine interne Genehmigung selbst.

6.2 Alternative Gesellschaft: Neue Geschäfte mit Seidels Einzelfirma werden bis zum Abschluss der Rechnungsprüfung ausgesetzt. Alternative Seidel: Ein Auftrag bleibt währenddessen zulässig, wenn Vergleichspreis, Leistungsnachweis und die erforderliche konfliktfreie Entscheidung vorliegen. Eine pauschale Befreiung von Beschränkungen des Selbstkontrahierens wird in keiner Alternative vereinbart.

6.3 Die Parteien legen vor Umsetzung fest, wer die Gesellschaft beim konkreten Vertrag vertritt. Eine bloße Freigabe durch Heller genügt hierfür nicht. Diese Regeln genehmigen die Rechnung SBS-2026-084 und ihre Zahlung nicht nachträglich. Die Beteiligten behalten hierzu ihre unterschiedlichen Auffassungen; eine abschließende Bereinigung ist ausschließlich nach Abschnitt 7 möglich.

## 7 Prüfung und mögliche Bereinigung der Rechnung

7.1 Die Prüfung betrifft ausschließlich die Rechnung SBS-2026-084 vom 20. August 2026 und die Zahlung von 18.400 EUR am 21. August. Bis zum 16. Oktober werden verfügbare Fremdbelege, Stundenaufzeichnungen und Seriennummern in einer gemeinsamen Belegliste zusammengeführt. Originale bleiben erhalten. Vier dokumentierte Wareneingänge, der nachgetragene Eintrag zu L-433 und die unklare Bearbeitung von L-427 werden getrennt bewertet.

7.2 Ein gemeinsam beauftragter unabhängiger Rechnungsprüfer soll offene Positionen bis zum 22. Oktober erläutern; sein Bericht ist ohne weitere Vereinbarung kein verbindliches Schiedsgutachten. Die Parteien können tatsächliche Einwendungen binnen drei Arbeitstagen nach Zugang ergänzen. Terminüberschreitungen verändern gerichtliche Fristen nicht.

7.3 Alternative Seidel: Eine abschließende Gutschrift wird erst nach Prüfung vereinbart und auf höchstens 2.380 EUR brutto begrenzt. Alternative Gesellschaft: Vor einem Anspruchsverzicht erfolgt zunächst eine Zahlung von 3.500 EUR; ihre endgültige Anrechnung wird nach Prüfung geregelt. Heller schlägt stattdessen eine gemeinsam geregelte Verwahrung bis zur Einigung vor. Keine Variante ist angenommen; weder Prüfdifferenzen noch Angebotssummen gelten als bewiesener Schaden.

## 8 Information, Ablage und Berichtswesen

8.1 Jeder Gesellschafter erhält monatlich bis zum zehnten Arbeitstag des Folgemonats eine Übersicht der Liquidität, offenen Forderungen, Verbindlichkeiten und freigabepflichtigen Bestellungen. Heller stellt vorhandene Buchhaltungsdaten zusammen; die Verantwortung für deren Freigabe und Erläuterung liegt bei der Geschäftsführung. Eine zusätzliche persönliche Gewährleistung Hellers wird nicht vereinbart.

8.2 Für Seidels Einsicht in die Lindenhof-Unterlagen wird nach gemeinsamer Terminabstimmung ein geschützter Lesezugang oder eine geordnete Kopienbereitstellung eingerichtet. Veränderungen und Löschungen der Originalablage sind ausgeschlossen. Die Gesellschaft dokumentiert, welche Unterlagen wann bereitgestellt wurden, und begründet konkret, wenn sie einzelne Unterlagen zurückhält.

8.3 Das zusätzliche Berichtswesen beschränkt gesetzliche Auskunfts- und Einsichtsrechte nicht. Ein pauschaler Ausschluss wegen des laufenden Streits wird nicht vereinbart. Vertrauliche Daten dürfen von den Empfängern nur für gesellschaftsbezogene Prüfung und zulässige Rechtsverfolgung verwendet werden. Der Zugang zu Abrechnungsunterlagen vermittelt weder Zahlungsberechtigung noch Vertretungsmacht.

## 9 Zustimmungsvorbehalte und Beschlussverfahren

9.1 Die Parteien wollen für neue Kredite, Sicherheiten für fremde Verbindlichkeiten und Investitionen außerhalb eines beschlossenen Jahresbudgets einen besonderen Zustimmungskatalog vereinbaren. Rabenstein und Seidel schlagen eine Schwelle von 75 Prozent des gesamten Stammkapitals vor. Heller verlangt bei neuen persönlichen Finanzierungsbeiträgen außerdem die ausdrückliche Zustimmung jedes belasteten Gesellschafters. Die konkrete Abgrenzung zu laufenden Bestellungen wird vor der Endfassung festgelegt.

9.2 Bis zu einer wirksamen Satzungsänderung bleiben die vorhandenen gesellschaftsrechtlichen Mehrheits- und Verfahrensregeln maßgeblich. Eine schuldrechtliche Verpflichtung, eine bestimmte Zustimmung einzuholen, wird nicht als bereits geänderte Beschlussmehrheit ausgegeben. Zwingende Stimmverbote bleiben bei jeder Entscheidung gesondert zu prüfen.

9.3 Einladungen, Anträge, Stimmen, Enthaltungen, nicht berücksichtigte Stimmen und Widersprüche werden nachvollziehbar dokumentiert. Die Parteien streben eine neutrale Versammlungsleitung bei persönlichen Konflikten an; die Bestellung erfolgt im Einzelfall nach der Satzung. Heller wird nicht dauerhaft zur Konfliktentscheiderin verpflichtet. Die Septemberniederschrift wird nicht nachträglich umgeschrieben.

## 10 Künftiger Finanzierungsbedarf

10.1 Die Geschäftsführung legt bis zum 30. Oktober eine Liquiditätsvorschau bis März 2027 vor. Der bislang nur vorsorglich erörterte Betrag von 40.000 EUR ist weder festgestellter Fehlbetrag noch beschlossene Kapitalzuführung. Vorrangig werden betriebliche Zahlungstermine, verfügbare Bankmittel und realistische Kundeneingänge betrachtet.

10.2 Alternative Rabenstein: Ein belegter Bedarf soll zunächst durch freiwillige Gesellschafterdarlehen entsprechend den Beteiligungen angeboten werden. Alternative Seidel: Vor einem solchen Angebot wird eine Bankfinanzierung geprüft; er sagt kein Darlehen zu. Heller lehnt jede automatische Nachschuss-, Bürgschafts- oder Sicherheitenpflicht ab. Ohne gesonderten Vertrag entsteht keine Finanzierungsverpflichtung.

10.3 Zins, Laufzeit, Rückzahlung, Sicherheiten und Risiken eines Darlehens werden erst anhand eines konkreten Finanzierungsvorschlags vereinbart. Die Nichtteilnahme führt aufgrund dieses Entwurfs weder zu einer Verwässerung noch zu einem Stimmrechtsverlust oder einer Verkaufspflicht. Eine spätere Kapitalerhöhung bleibt einem eigenständigen, formgerechten Verfahren vorbehalten und ist kein Bestandteil dieses Vergleichsrahmens.

## 11 Dauerhafte Meinungsverschiedenheiten und Beteiligungen

11.1 Scheitert derselbe zustimmungsbedürftige Antrag in zwei ordnungsgemäßen Beratungen, sollen die Parteien binnen zehn Arbeitstagen eine weitere Besprechung unter neutraler Moderation durchführen. Die Auswahl und ein Kostenrahmen werden gemeinsam bestätigt. Scheitert die Auswahl, darf jede Partei eine geeignete Person vorschlagen; daraus folgt keine einseitige Ernennung.

11.2 Die Moderation endet spätestens zwanzig Arbeitstage nach ihrer Beauftragung, sofern alle Beteiligten keine Verlängerung vereinbaren. Sie hemmt keine gerichtliche, gesetzliche oder satzungsmäßige Frist und sperrt keinen erforderlichen Eilrechtsschutz. Eine Schiedsvereinbarung oder verbindliche Mehrheitsentscheidung des Moderators wird nicht getroffen.

11.3 Es wird kein Kaufangebot erzwungen und keine Buchwertabfindung vereinbart. Eine spätere freiwillige Trennung setzt gesonderte Verhandlungen über Bewertung, Finanzierung, Haftung und Form voraus. Die bestehenden Satzungsregeln über Anteilsübertragungen bleiben bestehen. Dieser Entwurf enthält auch keine bedingte Verpflichtung zur Abtretung. Die Parteien bleiben bis zu einem gesonderten wirksamen Geschäft Inhaber ihrer bisherigen Anteile.

## 12 Vertraulichkeit und gemeinsame Außenkommunikation

12.1 Vergleichsvorschläge werden nur an Berater, erforderliche Entscheidungsträger und gesetzlich berechtigte Empfänger weitergegeben. Offenlegung gegenüber Gericht, Behörden oder Versicherern sowie zur zulässigen Rechtsverfolgung bleibt möglich. Keine Partei verpflichtet sich, Tatsachen falsch darzustellen oder vorhandene Beweismittel zurückzuhalten, zu verändern oder zu vernichten.

12.2 Eine Mitteilung an Beschäftigte oder Kunden wird vor Veröffentlichung gemeinsam abgestimmt. Sie beschreibt ausschließlich die tatsächlich wirksam geregelten Zuständigkeiten. Weder eine feststehende Unterschlagung noch eine vollständige Entlastung Seidels wird behauptet. Ein Vergleichsangebot stellt kein Anerkenntnis seiner zugrunde gelegten Tatsachen dar.

12.3 Rabenstein wünscht eine sachliche Betriebsmitteilung nach Vollzug; Seidel verlangt vorherige Zustimmung zum Wortlaut. Heller möchte, dass ihr Name nur bei ihrer tatsächlichen Zuständigkeit genannt wird. Bis zur Einigung beantwortet die Gesellschaft betriebliche Rückfragen anhand der jeweils gesondert geprüften aktuellen Befugnisse. Eine behauptete Vertraulichkeit ersetzt keinen wirksamen Schutz vor jeder prozessualen Verwendung; hierüber treffen die Parteien keine Zusicherung.

## 13 Prozess, Anspruchsumfang und Vergleichskosten

13.1 Die Fristen für die Verteidigungsanzeige am 9. Oktober und die Klageerwiderung am 23. Oktober 2026 werden unabhängig von den Gesprächen bearbeitet. Dieser Entwurf dokumentiert weder einen Gerichtseingang noch eine Verlängerung. Er verpflichtet keine Partei, vor Erfüllung der Vollzugsbedingungen eine Klage zurückzunehmen, einen Anspruch anzuerkennen oder einen Prozessverzicht zu erklären.

13.2 Nach vollständigem Vollzug soll ein gesonderter Prozessvergleich ausgearbeitet werden. Sein Umfang muss den Beschlussstreit und die konkret abschließend bereinigten Rechnungspositionen bezeichnen. Anstellungs- und Vergütungsansprüche werden nur einbezogen, wenn sie einzeln geprüft und ausdrücklich aufgeführt sind. Eine pauschale Erledigung sämtlicher bekannter und unbekannter Ansprüche wird nicht vereinbart.

13.3 Seidel bietet an, dass jede Prozesspartei ihre eigenen Anwaltskosten und die Hälfte der Gerichtskosten trägt. Die Gesellschaft hält ihre Zustimmung hierzu bis zur Rechnungsbereinigung offen. Persönliche Beratungskosten Rabensteins und Hellers werden nicht zu Prozesskosten der Gesellschaft. Über bereits verauslagte Beträge, Vergleichsmehrwert und zusätzliche Gebühren ist vor Abschluss gesondert abzurechnen.

## 14 Form, Unterschriften, Beginn und Vollzug

14.1 Die endgültige Vereinbarung wird von allen drei Gesellschaftern persönlich und gesondert für die Gesellschaft durch ihren wirksam legitimierten Vertreter unterschrieben. Die Vertretung im Prozess, beim Vergleich, beim Anstellungsvertrag und bei etwaigen Ansprüchen gegen Seidel ist gegenstandsbezogen zu klären. Noch fehlende Beschlüsse und Vollmachten werden beigefügt. Rabensteins Geschäftsführereigenschaft oder die Unterschrift ihres Anwalts wird nicht pauschal als ausreichender Nachweis behandelt.

14.2 Satzungsänderungen werden gesondert notariell beschlossen und registerrechtlich vollzogen. Eine etwaige spätere Anteilsübertragung oder entsprechende Verpflichtung wird dem Notar vorgelegt. Notwendige Formvorschriften werden nicht durch Textformklauseln ersetzt. Die Beteiligten lassen prüfen, ob die Verbindung einzelner Regelungen eine weitergehende Beurkundung erfordert.

14.3 Zieltermin ist der 1. November 2026; bei späterem Vollzug beginnt die vereinbarte Zusammenarbeit erst nach dessen Bestätigung. Voraussetzungen sind die gewählte Organ- und Anstellungsregelung, erforderliche Beschlüsse und Registerwirkungen, ein abgestimmter Bankablauf, bereitgestellte Informationen sowie die vereinbarte Rechnungszahlung oder Verwahrung. Beide Parteivertretungen bestätigen den belegten Vollzug vor jeder prozessbeendenden Erklärung. Wird bis zum 30. Oktober keine unterschriftsfähige Fassung erreicht, wird weiterverhandelt oder abgebrochen; ein Vergleich entsteht dadurch nicht. Bei Unwirksamkeit einer Bestimmung verhandeln die Parteien eine Ersatzregelung, ohne deren Inhalt automatisch zu fingieren.

Unterschriften sind nicht geleistet. Die endgültigen Unterzeichnungsfelder werden erst nach Klärung der Vertretung und Auswahl sämtlicher Alternativen erstellt.
'''),
doc('V02_Fuerst_Verhandlungsposition', 'Vergleichsvorschlag aus Sicht des Klägers', '08.10.2026',
    'Rechtsanwältin Walburga Fürst\nBerliner Straße 91, 13189 Berlin\nZeichen WF 216/26',
    'Dr. Adelbert Feuchtwanger\nFür die Spreebogen Lichtwerk GmbH', '''
Sehr geehrter Herr Kollege Dr. Feuchtwanger,

mein Mandant möchte nicht dauerhaft über jeden Werkstattschlüssel streiten. Er ist zu einer Gesamtregelung bereit, die ihm eine reale technische Aufgabe lässt. Das bedeutet weder, dass er die Abberufung für wirksam hält, noch dass er einen Schadensersatzanspruch anerkennt. Ich vertrete ausschließlich Herrn Seidel. Für Frau Rabenstein und Frau Heller gebe ich keine Erklärung ab. Bitte behandeln Sie die folgenden Vorschläge als zusammenhängendes Verhandlungsangebot, dessen Einzelteile nicht isoliert angenommen werden können.

## 1 Organstellung und Anstellung

Herr Seidel strebt eine ausdrücklich auf die Zukunft gerichtete Bestellung zum technischen Geschäftsführer an. Um Ihre Mandantin von einem erneuten Alleingang zu entlasten, bietet er für sechs Monate gemeinsame Vertretung mit Frau Rabenstein an. Anschließend sollen beide anhand der tatsächlichen Zusammenarbeit über die Organisationsform sprechen. Welche Beschlüsse und gegebenenfalls Satzungsänderungen dafür erforderlich sind, müssen wir vor Abschluss festhalten. Einen automatischen Rückfall in unbeschränkte Einzelvertretung verlangt er nicht.

Als zweite Möglichkeit kann er sich eine technische Übergangsrolle bis zum 31. Januar vorstellen. Er könnte drei Tage wöchentlich die laufenden Bühnenprojekte betreuen. Eine pauschale Bereitschaft an sämtlichen übrigen Tagen und die sofortige Kündigung seines bisherigen Vertrags lehnt er ab. Die Vergütung für Oktober ist gesondert zu behandeln. Dass die Septembervergütung gezahlt wurde, ist bekannt; über einen Verzicht auf weitere Ansprüche habe ich keinen Auftrag. Eine technische Aufgabe braucht einen definierten Umfang, Zugang zu den erforderlichen Unterlagen und Klarheit über Haftpflichtdeckung und Ansprechpartner.

## 2 Rechnung und künftige Freigaben

Mein Mandant hat die Zuordnung des sechsten Geräts noch nicht aufgeklärt. Die neuen Unterlagen rechtfertigen weder die Behauptung vollständiger Nichtleistung noch die unbesehene Bestätigung aller Rechnungspositionen. Er würde nach gemeinsamer Prüfung eine Gutschrift bis höchstens 2.380 EUR brutto erwägen. Das ist seine wirtschaftliche Vergleichsgrenze, keine Berechnung eines anerkannten Schadens. Eine Zahlung vor Sichtung der Belege bietet er nicht an. Ein gemeinsam ausgewählter sachkundiger Rechnungsprüfer kann helfen; ein verbindliches Schiedsgutachten möchte mein Mandant zunächst nicht vereinbaren. Nach Zugang seines Berichts sollen beide Seiten drei Arbeitstage für ergänzende tatsächliche Einwendungen haben.

Die Freigabegrenze von 10.000 EUR brutto soll bleiben. Zusammengehörige Bestellungen dürfen nicht aufgeteilt werden. Nachweise über Preis und Leistungsumfang sowie eine dokumentierte zweite Freigabe akzeptiert er, sofern Zuständigkeit und Vertretung bei Abwesenheit feststehen. Ein Liefertermin soll keine Ausnahme begründen; echte Gefahrenfälle müssen weiter handhabbar bleiben. Für Geschäfte mit seiner Einzelfirma akzeptiert er gesonderte konfliktfreie Entscheidungen auch unterhalb der Betragsgrenze. Eine generelle Sperre sämtlicher Lieferungen bis zum Abschluss des Streits lehnt er ab. Die Frage des Selbstkontrahierens soll bei jedem konkreten Geschäft ordentlich geklärt werden.

## 3 Beteiligung, Finanzierung und Information

Die Beteiligungen bleiben bei 40, 35 und 25 Prozent. Mein Mandant verhandelt weder eine Kapitalerhöhung noch einen Verkauf seines Anteils. Eine Satzungsregel über 75 Prozent des gesamten Stammkapitals für neue Kredite, fremde Sicherheiten und Investitionen außerhalb des Budgets erscheint ihm besprechbar. Er verlangt keine Einbeziehung gewöhnlicher Materialbestellungen in ein allgemeines Vetorecht.

Vor einem Gesellschafterdarlehen muss die Möglichkeit einer Bankfinanzierung geprüft werden. Aus einem derzeit genannten möglichen Bedarf von 40.000 EUR kann niemand eine persönliche Zahlungspflicht ableiten. Wir brauchen zunächst eine Vorschau bis März 2027. Monatliche Zahlen bis zum zehnten Arbeitstag und ein dokumentierter Lesezugang zur Einkaufsablage wären hilfreich. Gesetzliche Informationsrechte sollen davon unabhängig bleiben.

## 4 Konflikte, Kosten und Vollzug

Nach zwei gescheiterten Beratungen desselben Gegenstands kann eine neutrale Moderation binnen zehn Arbeitstagen beginnen. Sie soll nach zwanzig Arbeitstagen enden, sofern alle keine Verlängerung wünschen. Eine Zwangsverkaufsregel, Buchwertabfindung oder Schiedsvereinbarung kommt nicht in Betracht. Gesetzliche und gerichtliche Fristen müssen unberührt bleiben.

Die Vergleichskommunikation soll vertraulich bleiben, ohne Offenlegung an Berater, Gerichte, Versicherer oder Behörden und zulässige Rechtsverfolgung zu verhindern. Beweismittel müssen erhalten bleiben. Eine Betriebsmitteilung bedarf eines gemeinsam gebilligten Wortlauts. Mein Mandant wird weder öffentlich ein Fehlverhalten eingestehen noch eine unzutreffende Entlastung verlangen.

Für das Verfahren bietet er eigene Anwaltskosten je Partei und hälftige Gerichtskosten an. Persönliche Berater bezahlen die Gesellschafter selbst. Gemeinsame Prüfer- oder Notarkosten werden nur nach vorherigem Auftrag ausgelöst. Erledigt werden sollen nur ausdrücklich bezeichnete Streitgegenstände; unbekannte Ansprüche und ungeprüfte Vergütung werden nicht pauschal abgegolten.

Ein Zielbeginn am 1. November ist vorstellbar. Bis zum 30. Oktober müsste eine vollständige Fassung vorliegen. Erforderliche Beschlüsse, registerrechtliche Wirkungen, Rechnungszahlung, Bankablauf und Informationszugang müssen zuvor nachgewiesen sein. Alle drei Gesellschafter unterschreiben persönlich; für die Gesellschaft ist eine getrennte, wirksam legitimierte Erklärung erforderlich. Bitte klären Sie die Vertretung für Prozess, Vergleich und Anstellung gegenstandsbezogen. Die gesetzlichen Formanforderungen einschließlich einer möglichen Gesamtbeurkundung sind vor Unterzeichnung zu prüfen. Die Parteien sollen bei einer unwirksamen Regelung erneut verhandeln; eine fiktive Ersatzregelung lehne ich ab.

Eine Klagerücknahme vor Vollzug biete ich nicht an. Die Verteidigungsfristen laufen unabhängig von diesem Schreiben. Sollten wir nicht rechtzeitig einig werden, wird weiterverhandelt oder das Gespräch beendet, ohne dass darin bereits ein Vergleich liegt. Auch Schweigen, Unterlagenversand und Teilnahme am Gespräch sollen keine Zustimmung zum Vertragsentwurf ersetzen.

Mit kollegialen Grüßen
Walburga Fürst
Rechtsanwältin
'''),
doc('V03_Rabenstein_Gegenposition', 'Gesellschaftsposition und persönliche Vorbehalte zum Vergleich', '09.10.2026',
    'Kunigunde Rabenstein\nSpreebogen Lichtwerk GmbH | Mühlenstraße 64, 13187 Berlin',
    'Dr. Adelbert Feuchtwanger\nZur Verwendung im Gespräch mit Rechtsanwältin Fürst', '''
Sehr geehrter Herr Dr. Feuchtwanger,

die folgenden Punkte sollen Ihnen für das heutige Gespräch dienen. Soweit es den Betrieb betrifft, erläutere ich den Wunsch der Gesellschaft. Wo ich über meinen Geschäftsanteil, meine private Finanzierung oder meine persönliche Unterschrift spreche, ist das meine eigene Position und kein zusätzlicher Beratungsauftrag an Sie. Sie sollen die Gesellschaft verteidigen und für sie verhandeln. Bitte lassen Sie bei jedem späteren Beschluss prüfen, wer entscheiden und wer unterschreiben darf. Ich möchte nicht erneut ein Papier vorlegen, dessen Bedeutung nachher jede Person anders versteht.

## 1 Was für den Betrieb vorstellbar ist

Eine technische Mitarbeit Gottfrieds kann sinnvoll sein. Ich bevorzuge zunächst eine Übergangsaufgabe bis zum 31. Januar 2027. Drei feste Projekttage sind besprechbar, aber wir brauchen auch für Störungen an anderen Tagen eine verlässliche Zuständigkeit. Gottfried muss nicht allein rund um die Uhr erreichbar sein; wir müssten eine Vertretung im Team organisieren und deren Aufwand kennen. Bankzugang oder rechtsgeschäftliche Vertretung darf aus dieser Mitarbeit nicht automatisch folgen.

Eine erneute Organbestellung verspreche ich jetzt nicht. Dafür möchte ich erst die Rechnung und einige Wochen Zusammenarbeit sehen. Eine gemeinsame Vertretung könnte zusätzlich unser Tagesgeschäft verlangsamen. Sollte sie trotzdem die einzige tragfähige Lösung sein, müssen wir ihre gesellschaftsrechtliche Umsetzung vorher klären. Die Septemberentscheidung wird nicht rückdatiert oder aus dem Protokoll entfernt. Gottfrieds Anstellungsvertrag ist dadurch nicht nebenbei beendet. Bitte prüfen Sie die Oktobervergütung gesondert anhand des Vertrags; über deren Höhe und Fälligkeit will ich in diesem Brief nichts erfinden.

## 2 Rechnung und Einkaufsablauf

Für eine Einigung über die Rechnung hätte ich zunächst 3.500 EUR zurück auf dem Gesellschaftskonto erwartet. Das entspricht der Differenz zwischen erster Preisangabe und Endrechnung, beweist aber keinen Schaden in dieser Höhe. Ich bin bereit, über die endgültige Anrechnung nach Prüfung zu sprechen. Die Obergrenze von 2.380 EUR aus Frau Fürsts Schreiben erscheint mir vorschnell, solange die Expresskosten und das letzte Gerät unklar sind. Ottilies Idee einer neutralen Verwahrung möchte ich hören; die GmbH braucht aber Klarheit, wann sie tatsächlich über Geld verfügen könnte.

Bis zum 16. Oktober sollten alle verfügbaren Unterlagen in einer Liste stehen. Ein unabhängiger sachkundiger Prüfer könnte bis zum 22. Oktober Rückfragen beantworten. Wir müssen dessen Auftrag und Kosten gemeinsam festlegen. Seine Einschätzung soll zunächst eine Verständigung ermöglichen, nicht ohne weitere Abrede unsere Ansprüche verbindlich entscheiden. Fehlende Belege dürfen nicht nachträglich als zeitgleich unterschriebene Liefernachweise erscheinen.

Die Einkaufsgrenze möchte ich künftig auf 7.500 EUR brutto senken. Zusammengehörige Beschaffungen müssen zusammengerechnet werden. Wer auf der Baustelle eine unmittelbare Gefahr beseitigen muss, soll handeln können und noch am selben Tag berichten. Die drohende Verspätung eines Kundenauftrags allein reicht mir nicht. Ich möchte außerdem die technisch möglichen Zahlungen im Bankportal mit den internen Befugnissen abgleichen. Mir ist bewusst, dass ein interner Verstoß nicht ohne Weiteres einen Liefervertrag beseitigt.

Geschäfte mit einer Gesellschafterfirma benötigen für mich vorab eine nachvollziehbare, rechtlich wirksame Entscheidung und eine geeignete Vertretung beim Vertragsabschluss. Ich bevorzuge bis zur Rechnungsprüfung keine neuen Aufträge an SBS. Eine bestehende satzungsmäßige Zustimmungspflicht soll keinesfalls durch die Einkaufsgrenze oder eine Buchhaltungsfreigabe ersetzt werden. Auch eine nachträgliche Genehmigung der Augustzahlung wird in diesem Papier nicht erklärt.

## 3 Information und Mehrheiten

Eine monatliche Übersicht bis zum zehnten Arbeitstag unterstütze ich. Ottilie kann die Daten zusammenstellen, muss aber nicht persönlich für jeden offenen Kundenposten einstehen. Den Lesezugang zu den Lindenhof-Unterlagen können wir so einrichten, dass nichts gelöscht wird. Konkrete berechtigte Einwendungen gegen einzelne Dokumente müssen benannt werden; einen vollständigen Ausschluss Gottfrieds wegen des Prozesses wünsche ich nicht.

Über 75 Prozent des gesamten Stammkapitals bei neuen Krediten, fremden Sicherheiten und Investitionen außerhalb des Jahresbudgets können wir sprechen. Die vorhandene Satzung gilt bis zu einer wirksamen Änderung weiter. Ich möchte keine Formulierung, nach der unser Gespräch schon eine neue Satzung wäre. Bei persönlich belastenden Finanzierungen braucht es ohnehin die betroffenen Personen am Tisch. Bei konfliktbelasteten Versammlungen ist eine neutrale Leitung sinnvoll. Ottilie soll nicht auf Dauer Richterin zwischen uns sein.

## 4 Meine persönliche Finanzierungshaltung

Ich halte weiterhin 40 Prozent; Gottfried hält 35 und Ottilie 25 Prozent. Kein Anteil wird durch dieses Gespräch verkauft. Für einen belegten saisonalen Bedarf bis möglicherweise 40.000 EUR möchte ich zunächst freiwillige Darlehen nach Beteiligungsverhältnis anbieten. Vorher brauchen wir bis zum 30. Oktober die Liquiditätsvorschau bis März. Ich erkenne an, dass weder Gottfried noch Ottilie heute einen Beitrag zusagen. Auch ich unterschreibe noch keine Bürgschaft. Eine Kapitalerhöhung wurde nicht beschlossen und soll nicht als bereits laufender Vorgang erscheinen.

## 5 Grenzen des Abschlusses

Eine kurze Moderation bei wiederholt blockierten Entscheidungen ist vernünftig. Sie darf keine Fristen verschieben und niemanden zum Anteilsverkauf zwingen. Eine allgemeine Abfindung zum Buchwert lehne auch ich ab. Ein späterer Verkauf wäre eine eigene Verhandlung mit eigener Formprüfung.

Die Betriebsmitteilung soll sachlich bleiben und erst nach geklärten Zuständigkeiten erfolgen. Beratung und erforderliche Offenlegung müssen trotz Vertraulichkeit möglich sein; vorhandene Unterlagen werden erhalten. Eigene persönliche Berater bezahlt jeder selbst. Die Gesellschaft kann gemeinsame Vollzugskosten nur nach klarem Auftrag übernehmen. Über hälftige Gerichtskosten entscheide ich für die Gesellschaft noch nicht; zunächst muss die Rechnungsbereinigung tragfähig sein. Einen pauschalen Verzicht auf unbekannte Ansprüche wünsche ich nicht.

Vor Unterzeichnung brauche ich eine Vollzugsliste mit Beschlüssen, Vertretung, Bankablauf, Information und Rechnungsregelung. Meine persönliche Unterschrift ersetzt die Erklärung für die Gesellschaft nicht. Notar und Register sind dort einzubeziehen, wo es erforderlich ist. Zielbeginn 1. November und Redaktionsziel 30. Oktober sind für mich Termine zur Planung, keine automatische Bindung. Die Anwälte sollen den Vollzug belegen, bevor irgendjemand den Prozess beendet. Bis dahin erwarten wir die ordentliche Verteidigung einschließlich der heutigen Frist und der Erwiderung am 23. Oktober.

Mit freundlichen Grüßen
Kunigunde Rabenstein
'''),
doc('V04_Heller_Persoenliche_Position', 'Persönliche Stellungnahme zur künftigen Zusammenarbeit', '09.10.2026',
    'Ottilie Heller\nGesellschafterin mit 25 Prozent | Mühlenstraße 64, 13187 Berlin',
    'Kunigunde Rabenstein; Gottfried Seidel\nZur Weitergabe an deren jeweilige anwaltliche Vertretung', '''
Liebe Kunigunde, lieber Gottfried,

ich möchte, dass wir den Betrieb wieder ordentlich führen können. Das hier schreibe ich als Gesellschafterin. Es ist keine Zahlungsfreigabe aus der Buchhaltung und keine Vollmacht, mich anwaltlich zu vertreten. Herr Dr. Feuchtwanger vertritt die Gesellschaft, Frau Fürst Gottfried. Für mich habe ich bislang niemanden beauftragt. Bevor ich persönlich unterschreibe, will ich die fertige Fassung prüfen lassen können. Dafür möchte ich mindestens fünf Arbeitstage ab Zugang der vollständigen Unterlagen haben. Ich zahle meine Beratung selbst.

## 1 Arbeitsteilung und Informationen

Gottfrieds technisches Wissen wird weiter gebraucht. Ob er wieder Geschäftsführer wird oder zunächst drei Tage die Projekte begleitet, müssen wir ausdrücklich entscheiden. Ich möchte keine Formulierung, die ihn durch die Überschrift Technischer Leiter heimlich zum Geschäftsführer macht. Falls er bis Januar mitarbeitet, brauchen die Monteure einen verlässlichen Ansprechpartner für die anderen Tage. Sein Anstellungsvertrag, die Oktoberabrechnung und mögliche spätere Änderungen gehören auf einen eigenen Zettel mit überprüften Zahlen.

Eine monatliche Zahlenübersicht bis zum zehnten Arbeitstag kann ich aus der Buchhaltung vorbereiten. Die Geschäftsführung muss sie prüfen und erläutern. Ich übernehme keine persönliche Garantie für Kundenzahlungen und entscheide auch nicht allein, ob Ausgaben unternehmerisch sinnvoll sind. Lesezugang und Kopien für Gottfried sind möglich, wenn die Originalablage geschützt bleibt. Seine gesetzlichen Informationsrechte sollen dabei nicht von meiner Verfügbarkeit abhängen.

## 2 Rechnung und Kontrolle

Vier Geräte habe ich über den Wareneingang, L-433 über den späteren Eintrag und L-427 bislang nur als altes Gerät beziehungsweise möglichen Umbau. Bitte schreibt weder sechs belegte Neulieferungen noch zwei nachweislich fehlende Geräte in einen Vergleich. Der Prüfer soll Rechnung, Zahlung und Leistungsbelege getrennt behandeln. Ein Bericht bis zum 22. Oktober erscheint mir nur erreichbar, wenn bis zum 16. Oktober alles Verfügbare gesammelt ist. Über fehlende Unterlagen muss dann offen gesprochen werden.

Zwischen 2.380 und 3.500 EUR möchte ich nicht durch Bauchgefühl entscheiden. Man könnte einen vereinbarten Betrag bei einer gemeinsam ausgewählten geeigneten Stelle verwahren, bis die Endabrechnung feststeht. Es gibt aber noch keine Stelle, keine Verwahrungszusage und keine Kostenvereinbarung. Ein Gericht oder ein Notar soll nicht ohne Anfrage als bereit bezeichnet werden. Ich will auch nicht als Buchhalterin fremdes Geld privat entgegennehmen.

Die Entscheidung zwischen 7.500 und 10.000 EUR muss der Betrieb tragen können. Wichtiger ist mir, dass derselbe Auftrag nicht in drei kleine Rechnungen zerlegt wird und dass eine zweite befugte Person entscheidet. Die Freigabe für eine Gesellschafterfirma muss davon getrennt bleiben. Wenn jemand persönlich betroffen ist, soll rechtlich geprüft werden, wer abstimmen und den Vertrag unterschreiben darf. Meine Unterschrift unter einer Buchung ersetzt beides nicht.

## 3 Meine Beteiligung und mein Geld

Meine 25 Prozent bleiben bestehen. Eine allgemeine 75-Prozent-Regel schützt mich nicht gegen alles, denn Kunigunde und Gottfried kommen zusammen genau auf diesen Anteil. Persönliche Darlehen, Bürgschaften oder sonstige Belastungen dürfen deshalb nur mit meiner ausdrücklichen Zustimmung entstehen. Ich kann gegenwärtig keinen Betrag zusagen. Der erwähnte mögliche Bedarf von 40.000 EUR ist noch keine belastbare Planung. Eine Vorschau bis März muss her, bevor wir über Bank oder freiwillige Gesellschafterdarlehen reden.

Ich möchte keine automatische Verwässerung, keine Sanktion durch Entzug meines Stimmrechts und keinen Verkaufszwang, wenn ich kein Geld nachschieße. Einen späteren freiwilligen Verkauf kann man getrennt besprechen. Eine Buchwertabfindung akzeptiere ich nicht. Ich möchte außerdem nicht dauerhaft alle streitigen Versammlungen leiten. Bei persönlichen Konflikten soll eine neutrale Leitung ordnungsgemäß gewählt werden; das vorhandene Septemberprotokoll bleibt unverändert.

## 4 Abschluss und Gesprächskultur

Eine begrenzte Moderation nach zwei gescheiterten Beratungen ist gut. Wenn wir uns nicht einmal über die Person einigen, gibt es eben noch keinen Moderator. Einseitige Ernennung und bindende Entscheidung über meinen Kopf hinweg lehne ich ab. Laufende Fristen dürfen deswegen nicht versäumt werden.

Eine gemeinsame Mitteilung an Mitarbeiter soll nur die tatsächlich geklärten Zuständigkeiten benennen. Mein Name gehört nicht in einen Satz, der mich für alte Lieferungen verantwortlich macht. Ich unterstütze Vertraulichkeit, aber keine falschen Aussagen und kein Verschwindenlassen von Nachrichten. Jeder muss mit seinen Beratern und nötigenfalls mit Gericht oder Behörden sprechen können.

Alle persönlichen Unterschriften und die gesonderte Vertretung der Gesellschaft müssen erkennbar sein. Ein Notar muss prüfen können, welche Punkte eine Beurkundung oder Registerumsetzung brauchen. Am 1. November kann nur beginnen, was wir zuvor wirksam vereinbart und umgesetzt haben. Falls bis zum 30. Oktober keine klare Fassung vorliegt, gilt nicht plötzlich die letzte Rundmail. Über unwirksame Teile müssten wir neu sprechen. Vor belegtem Vollzug soll keine Klage zurückgenommen werden. Auch eine allgemeine Erledigung unbekannter Ansprüche oder meiner persönlichen Rechte möchte ich nicht unterschreiben.

Herzliche Grüße
Ottilie Heller
'''),
doc('V05_Gespraechsprotokoll_09_Oktober', 'Gesprächsnotiz zum offenen Vergleichsrahmen', '09.10.2026',
    'Ottilie Heller\nNotizen aus dem Gespräch, ergänzt um die zugeordneten Entwurfsnummern um 14:45 Uhr',
    'Kunigunde Rabenstein; Gottfried Seidel; Walburga Fürst; Dr. Adelbert Feuchtwanger', '''
Das Gespräch fand am 9. Oktober 2026 von 10:00 bis 11:25 Uhr telefonisch statt. Teilgenommen haben Kunigunde Rabenstein, Gottfried Seidel, Ottilie Heller, Rechtsanwältin Walburga Fürst für Seidel und Rechtsanwalt Dr. Adelbert Feuchtwanger für die Gesellschaft. Ich habe mit Zustimmung der Anwesenden mitgeschrieben. Es gibt keine Tonaufnahme. Die Zuordnung zu den Abschnitten der um 13:15 Uhr datierten Arbeitsfassung habe ich nach deren Eingang ergänzt; sie war noch nicht Grundlage des Gesprächs. Niemand hat diese Notiz gemeinsam unterschrieben oder als verbindlich bestätigt.

## 1 Rollen und Verfahrensstand

Dr. Feuchtwanger erklärte zu Beginn, dass er nur für die Gesellschaft spreche. Rabenstein und ich nehmen unsere persönlichen Rechte selbst wahr. Frau Fürst bestätigte ihr Mandat für Seidel. Die Beratung zu einer Einigung wurde gewünscht, eine Abschlussvollmacht aus dem Telefonat aber ausdrücklich nicht abgeleitet. Ob für die Gesellschaft neben der Geschäftsführervollmacht weitere gegenstandsbezogene Beschlüsse oder Vertretungsnachweise erforderlich sind, soll geprüft werden. Das Telefonat enthält keinen solchen Beschluss.

Die Wiedervorlagen für Verteidigungsanzeige am heutigen 9. Oktober und Erwiderung am 23. Oktober wurden angesprochen. Eine beA-Eingangsbestätigung lag in den hier gemeinsam besprochenen Unterlagen nicht vor. Dr. Feuchtwanger verwies auf die getrennte Bearbeitung des Gerichtsausgangs durch die Kanzlei. Ich kann hier nur das Gespräch dokumentieren und bestätige keinen erfolgten Versand. Die Teilnehmer waren sich einig, aus Vergleichsgesprächen keine Fristverschiebung abzuleiten.

## 2 Parteien und Beratungsfragen – Entwurfsabschnitte 1 und 2

Alle nannten unverändert 25.000 EUR Stammkapital und die Beteiligungen 40, 35 und 25 Prozent. Gegenstand ist die bestehende GmbH mit Lichtbetrieb, kein neuer Beteiligungseinstieg. Grundlage waren Frau Fürsts Schreiben V02, Rabensteins Gegenposition V03 und mein Schreiben V04. Die beabsichtigte Vereinbarung soll persönliche Verpflichtungen der Gesellschafter und Pflichten der Gesellschaft klar unterscheiden. Gesellschaftsrechtliche Wirkungen sollen gesondert umgesetzt werden.

V02 Abschnitt 4 und V03 Abschnitt 5 enthalten den Wunsch nach eigenen Beratungskosten je Partei und gesonderten Aufträgen für gemeinsame Vollzugskosten. Ich habe auf fünf Arbeitstagen Prüfungszeit für eine vollständige Endfassung bestanden. Rabenstein hielt dies für vernünftig, wollte aber die Prozessbearbeitung davon unabhängig halten. Die Prüfungsfrist fehlt noch im übersandten Entwurf; sie ist nachzutragen oder ausdrücklich abzulehnen. Es wurde kein gemeinsames Anwaltsmandat erteilt.

## 3 Tätigkeit und Anstellung – Entwurfsabschnitte 3 und 4

Seidel wiederholte V02 Abschnitt 1: künftige Bestellung, zunächst sechs Monate gemeinsame Vertretung. Rabenstein bevorzugt entsprechend V03 Abschnitt 1 eine technische Übergangsrolle bis zum 31. Januar 2027. Seidel hält drei Projekttage für machbar; eine zusätzliche Störungsbereitschaft bleibt ungeklärt. Ich habe eine Vertretung für die übrigen Tage verlangt. Eine organisatorische Entscheidung wurde nicht getroffen.

Die Oktobervergütung bleibt gesondert anhand des Anstellungsvertrags zu prüfen. Niemand behauptete, der Septemberbeschluss habe diesen Vertrag automatisch beendet. Zugang, Aufgabenbeschreibung, Haftpflichtdeckung und Weisungsweg stehen noch aus. Der Vertragsentwurf darf die offene Organfrage deshalb nicht mit einer Funktionsbezeichnung entscheiden.

## 4 Freigaben und Eigengeschäfte – Entwurfsabschnitte 5 und 6

Aus V02 Abschnitt 2 und V03 Abschnitt 2 ergeben sich die konkurrierenden Grenzen von 10.000 und 7.500 EUR brutto. Zusammenrechnung verbundener Bestellungen, Nachweis des Preises und eine dokumentierte zweite Entscheidung wurden als Arbeitsgrundlage akzeptiert. Wer im späteren Organmodell tatsächlich befugt wäre, ist noch zu bestimmen. Die Buchhaltung soll nicht die fehlende zweite Geschäftsführungsentscheidung ersetzen.

Bei Geschäften mit Seidels Einzelfirma verlangt Rabenstein eine vorläufige Sperre, Seidel dagegen die Möglichkeit ordnungsgemäß freigegebener Einzelaufträge. V04 Abschnitt 2 verlangt getrennte Prüfung von Stimmrecht und Vertragsvertretung. Niemand erklärte eine allgemeine Befreiung vom Selbstkontrahierungsverbot oder die nachträgliche Genehmigung der Augustzahlung. Der Unterschied zwischen interner Pflicht und Wirkung gegenüber Lieferanten wurde angesprochen, ohne einzelne bestehende Verträge abschließend zu bewerten.

## 5 Rechnung – Entwurfsabschnitt 7

Seidels Grenze von 2.380 EUR stammt aus V02 Abschnitt 2; Rabensteins gewünschte vorläufige Zahlung von 3.500 EUR aus V03 Abschnitt 2. Mein Vorschlag einer Verwahrung aus V04 Abschnitt 2 ist eine dritte Möglichkeit, keine angenommene Zwischenlösung. Eine geeignete Stelle wurde nicht benannt. Die beiden Beträge sind Verhandlungspositionen und keine gemeinsam festgestellte Forderung.

Die Teilnehmer wollen verfügbare Belege möglichst bis zum 16. Oktober sammeln und einen gemeinsam beauftragten Prüfer bis zum 22. Oktober befragen. Auftrag, Person und Preis stehen aus. Einwendungen sollen drei Arbeitstage möglich bleiben. Frau Fürst widersprach einer automatischen Verbindlichkeit des Prüferberichts. Die unterschiedliche Herkunft der Gerätedaten bleibt sichtbar. Die erste Klagebehauptung wird durch dieses Gespräch weder stillschweigend berichtigt noch als gemeinsam richtig bestätigt; ihre prozessuale Behandlung obliegt der jeweiligen Vertretung.

## 6 Information und Mehrheiten – Entwurfsabschnitte 8 und 9

V02 Abschnitt 3, V03 Abschnitt 3 und V04 Abschnitt 1 begründen den monatlichen Bericht und geschützten Lesezugang. Ich kann vorhandene Zahlen liefern, übernehme aber keine persönliche Garantie. Eine konkrete Bereitstellung ist noch zu organisieren. Gesetzliche Informationsrechte sollen davon unabhängig bleiben.

Die vorgeschlagenen 75 Prozent beziehen sich nach den Äußerungen auf das gesamte Stammkapital und auf einen begrenzten Katalog. Dies darf nicht mit der jetzigen Satzungsregel über abgegebene Stimmen verwechselt werden. Ich habe darauf hingewiesen, dass die 75-Prozent-Schwelle mir kein eigenes Vetorecht gibt und keine persönlichen Finanzierungspflichten ohne meine Zustimmung begründen soll. Satzungsänderung, schuldrechtliche Zustimmungspflicht und gesetzliches Stimmverbot müssen im späteren Text getrennt erkennbar sein. Eine neutrale Versammlungsleitung wird gewünscht, aber im Einzelfall ordnungsgemäß gewählt. Die alte Niederschrift wird nicht ersetzt.

## 7 Finanzierung und Konfliktlösung – Entwurfsabschnitte 10 und 11

V03 Abschnitt 4 schlägt freiwillige anteilige Darlehen vor, V02 Abschnitt 3 vorherige Bankprüfung. V04 Abschnitt 3 schließt meine automatische Finanzierung und Verwässerung aus. Die 40.000 EUR sind ein vorsorglicher Gesprächsbetrag. Rabenstein will bis zum 30. Oktober eine Vorschau bis März 2027 erstellen lassen. Niemand hat Geld zugesagt, Kapital übernommen oder eine Kapitalerhöhung beschlossen.

V02 Abschnitt 4 und V04 Abschnitt 4 begründen die begrenzte Moderation ohne einseitige Ernennung, Schiedsentscheidung oder Fristhemmung. Rabenstein erklärte hierzu entsprechend V03 Abschnitt 5 Gesprächsbereitschaft. Niemand möchte eine Buchwertklausel oder einen automatischen Verkauf. Ein späterer freiwilliger Verkauf bleibt ein eigener Vorgang einschließlich Formprüfung.

## 8 Kommunikation und Prozess – Entwurfsabschnitte 12 und 13

Die Positionen zur Vertraulichkeit und Beweissicherung stehen jeweils im letzten Abschnitt der drei Briefe. Seidel verlangt Zustimmung zur Betriebsmitteilung; Rabenstein wünscht eine Mitteilung über wirksame Zuständigkeiten; ich möchte keine unzutreffende Zuschreibung eigener Verantwortung. Es wurde kein gemeinsamer Text beschlossen und keine absolute Unverwertbarkeit von Verhandlungsmaterial zugesichert.

V02 Abschnitt 4 enthält das Angebot, eigene Anwaltskosten zu tragen und Gerichtskosten zu halbieren. V03 Abschnitt 5 hält die Gesellschaftszustimmung offen. V04 Abschnitt 4 verlangt, persönliche Rechte nicht pauschal abzugelten. Der genaue Umfang eines späteren Prozessvergleichs muss gesondert ausgearbeitet werden. Anstellungsansprüche und unbekannte Ansprüche sind bislang nicht abschließend erfasst. Vor erfüllten Bedingungen wird keine Prozessbeendigung versprochen.

## 9 Unterschriften und Vollzug – Entwurfsabschnitt 14

Alle drei Briefe verlangen persönliche Unterschriften und eine gesonderte legitimierte Vertretung der Gesellschaft. Erforderliche Organentscheidungen, Satzungsform, registerrechtliche Wirkungen und eine mögliche Beurkundung der Gesamtvereinbarung sind vorab zu klären. Die vorhandene Unterschriftenmappe aus dem Nachtrag ist kein Nachweis einer schon ausreichenden Prozess- oder Abschlussvollmacht.

1. November ist gewünschter Beginn, 30. Oktober ein Redaktionsziel. Ohne vollständige Regelung und belegten Vollzug wird daraus kein automatischer Vertrag. Die Parteien sollen bei unwirksamen Bestimmungen neu verhandeln, wie V02 Abschnitt 4 und V04 Abschnitt 4 verlangen. Frau Fürst hat angekündigt, zunächst die konkurrierenden Regelungen lesbar zusammenzuführen. Dr. Feuchtwanger soll sodann aus Gesellschaftssicht überarbeiten. Dieser nächste Arbeitsschritt ist keine Billigung des um 13:15 Uhr entstandenen Entwurfs.

Ottilie Heller
Gesprächsnotiz, versandt zur Korrektur am 09.10.2026 um 15:10 Uhr
'''),
    ],
    emails=[
mail('V06_Mandatserweiterung_Gesellschaft', 'Spreebogen: Verteidigung bleibt vorrangig – zusätzlich Vergleich prüfen', '2026-10-09T08:10:00+02:00',
    'Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>', 'Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>', '''
Sehr geehrter Herr Dr. Feuchtwanger,

ich erweitere den Auftrag für die Spreebogen Lichtwerk GmbH um die Prüfung eines Vergleichs und einer Vereinbarung über die weitere Zusammenarbeit. Bitte bearbeiten Sie zunächst die Verteidigung gegen die Klage einschließlich der ausführlichen Klageerwiderung. Anschließend soll ein tragfähiger Entwurf für die Gesellschaft entstehen. Frau Fürst wird wohl eine erste Vertragsfassung schicken. Meine beigefügte Stellungnahme enthält unsere betrieblichen Grenzen und ausdrücklich getrennt meine persönlichen Wünsche.

Sie vertreten weiterhin ausschließlich die Gesellschaft. Ich beauftrage Sie nicht für mich persönlich, nicht für Ottilie und selbstverständlich nicht für Gottfried. Bitte klären Sie, welche Vertretung und welche Beschlüsse für den Prozess, einen Vergleich, den Anstellungsvertrag und eine mögliche Rechnungsbereinigung jeweils benötigt werden. Die angekündigte Vollmacht ist kein Ersatz für eine fehlende Entscheidung. Ob alle erforderlichen Unterschriften bereits in Ihrer Akte sind, kann ich heute aus dem Betrieb nicht bestätigen.

Bitte geben Sie Vergleichserklärungen erst nach einer gesonderten Freigabe der dann zuständigen Personen ab. Heute geht es um Prüfung, Entwurf und das Gespräch. Eine Widerklage oder ein pauschaler Anspruchsverzicht ist damit nicht beauftragt. Auch Kosten für einen Prüfer oder Notar sollen erst nach einem konkreten Vorschlag ausgelöst werden.

Die Fristen am heutigen 9. Oktober und am 23. Oktober bleiben für mich dringend. Bitte bestätigen Sie den tatsächlichen Gerichtseingang gesondert, sobald Sie ihn belegen können. Eine Gesprächszusage von Frau Fürst beruhigt mich insoweit nicht.

Mit freundlichen Grüßen
Kunigunde Rabenstein
Geschäftsführerin, Spreebogen Lichtwerk GmbH

Anlage: V03_Rabenstein_Gegenposition.docx
''', ('V03_Rabenstein_Gegenposition.docx',)),
mail('V07_Fuerst_Vergleichsvorstoss', '32 O 187/26 – Gespräch um 10 Uhr und Position meines Mandanten', '2026-10-09T08:36:00+02:00',
    'Walburga Fürst <post@fuerst-recht.example>', 'Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>', '''
Sehr geehrter Herr Kollege Dr. Feuchtwanger,

anbei erhalten Sie mein gestern mit Herrn Seidel besprochenes Schreiben. Er möchte das Telefonat um 10 Uhr nutzen, um zwischen einer künftigen Organstellung und einer technischen Übergangslösung zu unterscheiden. Beides gleichzeitig als bereits vereinbart festzuhalten, wäre falsch. Er kann drei feste Projekttage anbieten. Ob Ihre Mandantin damit ihre Kunden verlässlich betreuen kann, sollten wir konkret besprechen.

Die Zahl von 2.380 EUR ist seine derzeitige Vergleichsgrenze nach Rechnungsprüfung. Sie ist kein Anerkenntnis, dass genau dieser Betrag überzahlt wurde. Er will die Belege bis zum 16. Oktober möglichst vollständig zusammentragen. Bei der Seriennummer des letzten Geräts besteht weiter Unsicherheit. Bitte lassen Sie die Septemberniederschrift und die bisherigen Unterlagen unverändert; spätere Erläuterungen sollen als solche erkennbar bleiben.

Ich vertrete nur Herrn Seidel. Frau Heller kann ihre Vorstellungen selbst erklären und eigene Beratung hinzuziehen. Für die Gesellschaft gehe ich von Ihrer gesondert zu prüfenden Bevollmächtigung aus. Aus der Teilnahme von Frau Rabenstein werde ich keine Abschlussvollmacht für sämtliche Gegenstände ableiten.

Mein Mandant möchte eine spätere Betriebsmitteilung vorher lesen. Persönliche Beratungskosten trägt jeder selbst; gemeinsamer Prüfer und Notar benötigen einen abgestimmten Auftrag. Eine Einigung über die Prozesskosten ist noch nicht erreicht. Die Klage wird heute weder zurückgenommen noch für erledigt erklärt. Die laufenden gerichtlichen Fristen werden durch unser Gespräch nicht verändert; bitte organisieren Sie Ihre Verteidigung unabhängig davon.

Mit kollegialen Grüßen
Walburga Fürst
Rechtsanwältin

Anlage: V02_Fuerst_Verhandlungsposition.pdf
''', ('V02_Fuerst_Verhandlungsposition.pdf',)),
mail('V08_Heller_Rollen_und_Grenzen', 'Vor dem Telefonat: meine 25 Prozent und die Buchhaltung bitte trennen', '2026-10-09T09:02:00+02:00',
    'Ottilie Heller <oh@spreebogen-lichtwerk.example>',
    'Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>, Gottfried Seidel <gs@seidel-buehnenservice.example>', '''
Liebe Kunigunde, lieber Gottfried,

ich schicke Euch meinen Brief vor dem Telefonat, damit meine Punkte nicht zwischen Euren beiden Vorschlägen verschwinden. Bitte gebt ihn vollständig an Eure jeweiligen anwaltlichen Ansprechpartner weiter. Herr Dr. Feuchtwanger soll erkennen können, dass ich persönlich spreche und kein gemeinsames Mandat erteile. Eine fertige Vertragsfassung möchte ich vor meiner Unterschrift mindestens fünf Arbeitstage prüfen lassen können.

Die Monatsübersicht kann ich vorbereiten, wenn die Geschäftsführung die Verantwortung für Prüfung und Erläuterung übernimmt. Ein Lesezugang zur Lindenhof-Ablage ist ebenfalls machbar. Ich möchte aber nicht mit meiner Buchhaltungsunterschrift automatisch Preisfreigaben, einen Lieferumfang oder fremde Vertretungsmacht bestätigen. Bei der Rechnung fehlt mir weiterhin eine saubere Zuordnung des letzten Geräts. Aus einem funktionierenden Kundenauftrag folgt für mich keine lückenlose Lieferdokumentation.

Bei der Finanzierung ist mir besonders wichtig, dass 75 Prozent Kunigunde und Gottfried gemeinsam erreichen können. Meine persönlichen Darlehen oder Bürgschaften dürfen deshalb nicht über eine solche Mehrheit entstehen. Ich habe heute kein Geld zugesagt. Eine Verwahrung zur Überbrückung des Rechnungsstreits wäre eine Überlegung, aber bislang gibt es weder einen Verwahrer noch einen vereinbarten Betrag.

Ich schreibe im Gespräch gern mit. Das wird kein Gesellschaftsbeschluss und kein von allen bestätigtes Ergebnisprotokoll. Bitte berichtet der Werkstatt erst von einer Einigung, wenn die Zuständigkeiten wirklich geregelt sind. Die Gerichtsfristen bleiben Aufgabe der Kanzlei; einen Versandnachweis habe ich selbst nicht.

Herzliche Grüße
Ottilie

Anlage: V04_Heller_Persoenliche_Position.docx
''', ('V04_Heller_Persoenliche_Position.docx',)),
mail('V09_Fuerst_Entwurfsversand', 'Arbeitsfassung 13:15 Uhr – Alternativen bitte ausdrücklich offen lassen', '2026-10-09T13:40:00+02:00',
    'Walburga Fürst <post@fuerst-recht.example>', 'Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>', '''
Sehr geehrter Herr Kollege Dr. Feuchtwanger,

ich übersende die angekündigte bearbeitbare Arbeitsfassung. Sie führt die besprochenen Wünsche in vierzehn Abschnitten zusammen. Ich habe die konkurrierenden Organmodelle, die Freigabegrenzen und die Rechnungsvarianten nebeneinander ausformuliert. Mein Mandant hat damit keiner Variante Ihrer Mandantin zugestimmt. Bitte kennzeichnen Sie Änderungen so, dass wir tatsächliche Verständigung und bloße Redaktionsarbeit auseinanderhalten können.

Die Vereinbarung soll die bestehende Gesellschaft betreffen. Weder wird Kapital erhöht noch ein Anteil übertragen. Bei den Zustimmungsvorbehalten muss eine etwaige schuldrechtliche Bindung von der noch gesondert umzusetzenden Satzungsänderung getrennt bleiben. Für die technische Übergangsrolle fehlen noch Aufgabenbeschreibung, Bereitschaftsregelung und die geprüften Angaben aus dem Anstellungsvertrag. Ohne diese Ergänzungen ist die Fassung nicht unterschriftsreif.

Auch die Vertretung der Gesellschaft darf nicht pauschal in der Unterschriftenzeile verschwinden. Bitte prüfen Sie Prozess, Vergleich, Organentscheidung und Anstellung jeweils am konkreten Gegenstand. Erforderliche Beschlüsse, notarielle Schritte und Registerwirkungen sollten in einer Vollzugsliste stehen. Das gewünschte Datum 1. November ist kein Beginn ohne erfüllte Bedingungen.

Eine allgemeine Erledigung aller Ansprüche habe ich bewusst nicht aufgenommen. Die Kostenaufteilung ist weiterhin nur Seidels Angebot. Frau Hellers Bitte um eigene Prüfungszeit muss noch in den Ablauf eingearbeitet werden; ich habe den Entwurf vor diesem Abgleich herausgegeben. Bitte geben Sie ihn deshalb weder als abgestimmt weiter noch zum Unterschreiben aus. Bis zum belegten Vollzug wird keine prozessbeendende Erklärung zugesagt.

Mit kollegialen Grüßen
Walburga Fürst
Rechtsanwältin

Anlage: V01_Gesellschaftervereinbarung_Entwurf.docx
''', ('V01_Gesellschaftervereinbarung_Entwurf.docx',)),
mail('V10_Rabenstein_Entwurfsrueckmeldung', 'Zum Entwurf: Übergangsrolle, Zahlung und Gesellschaftsvertretung bleiben offen', '2026-10-09T14:25:00+02:00',
    'Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>', 'Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>', '''
Sehr geehrter Herr Dr. Feuchtwanger,

ich habe Frau Fürsts Entwurf gelesen und lege meine heutige Stellungnahme nochmals daneben. Die Alternativen sind für mich tatsächlich offen. Ich möchte zunächst die technische Übergangsrolle prüfen lassen. Einer sofortigen neuen Geschäftsführerbestellung stimme ich mit dieser Mail nicht zu. Für die Störungseinsätze brauchen wir einen praktikablen Plan; drei feste Tage allein beantworten die Frage der übrigen Woche noch nicht.

Bei Abschnitt 7 reicht mir eine spätere Gutschrift bis höchstens 2.380 EUR derzeit nicht. Die vorläufige Zahlung von 3.500 EUR und Ottilies Verwahrungsidee sollen anhand der Liquidität und der noch offenen Belege verglichen werden. Bitte stellen Sie keine dieser Zahlen als festgestellten Schaden oder bereits angenommenes Angebot dar. Auch neue SBS-Aufträge während der Prüfung bleiben für mich problematisch.

Die Trennung von persönlicher Vereinbarung, Gesellschaftsbeschlüssen und Satzungsänderung erscheint mir richtig. Ich möchte aber vor Unterzeichnung sehen, welche Personen jeweils handeln dürfen und welche Nachweise tatsächlich vorliegen. Mein Geschäftsführertitel allein soll im Entwurf keine ungeprüfte Antwort auf jede Vertretungsfrage sein. Die Kanzlei soll nur die Gesellschaft beraten; meine persönliche Darlehensbereitschaft wäre gesondert zu erklären.

Bitte arbeiten Sie erst die notwendige Verteidigung und dann die Vertragsfassung für unsere Seite aus. Ottilies fünf Arbeitstage für die persönliche Prüfung können wir berücksichtigen, ohne dafür Gerichtsfristen verstreichen zu lassen. Zur heutigen Verteidigungsanzeige benötige ich weiterhin die gesonderte Bestätigung des tatsächlichen Eingangs. Diese Mail enthält keine Freigabe zur Prozessbeendigung.

Mit freundlichen Grüßen
Kunigunde Rabenstein

Anlagen: V03_Rabenstein_Gegenposition.pdf; V01_Gesellschaftervereinbarung_Entwurf.docx
''', ('V03_Rabenstein_Gegenposition.pdf', 'V01_Gesellschaftervereinbarung_Entwurf.docx')),
mail('V11_Heller_Protokoll_und_Korrekturen', 'Gesprächsnotiz: bitte korrigieren, eine Einigung steht dort nicht', '2026-10-09T15:10:00+02:00',
    'Ottilie Heller <oh@spreebogen-lichtwerk.example>',
    'Kunigunde Rabenstein <kr@spreebogen-lichtwerk.example>, Gottfried Seidel <gs@seidel-buehnenservice.example>, Walburga Fürst <post@fuerst-recht.example>, Dr. Adelbert Feuchtwanger <af@feuchtwanger-recht.example>', '''
Sehr geehrte Frau Fürst, sehr geehrter Herr Dr. Feuchtwanger,
liebe Kunigunde, lieber Gottfried,

anbei sende ich meine Gesprächsnotiz und zur eindeutigen Zuordnung nochmals meinen persönlichen Brief. Die Nummern der Vertragsabschnitte habe ich erst nach Eingang der Arbeitsfassung ergänzt. Wir hatten diesen Text morgens noch nicht vor uns. Bitte gebt mir konkrete Korrekturen, wenn ich eine Äußerung falsch zugeordnet habe. Schweigen soll keine Genehmigung des Protokolls bedeuten.

Mir ist aufgefallen, dass meine gewünschte Prüfungszeit von fünf Arbeitstagen noch nicht als Regelung im Entwurf steht. Ich möchte sie vor einer persönlichen Unterschrift haben. Das darf selbstverständlich nicht bedeuten, dass die Gesellschaft ihre Verteidigungsfristen liegen lässt. Einen Gerichtseingang kann ich als Buchhaltung weiterhin nicht bestätigen; dafür brauche ich die Nachricht der Kanzlei.

Meine Verwahrungsidee ist ebenfalls nur ein Vorschlag. Es gibt keine ausgewählte Stelle und keinen angenommenen Verwahrungsauftrag. Bitte schreibt in einer nächsten Fassung nicht, Geld liege bereits sicher bereit. Auch die Liquiditätsvorschau muss erst erstellt werden. Der Betrag von 40.000 EUR ist noch kein festgestellter Finanzierungsbedarf und keine Zusage der Gesellschafter.

Ich habe die offenen Klauseln jeweils den Briefstellen und Gesprächsbeiträgen zugeordnet. Dadurch sollte sichtbar bleiben, warum die Varianten im Entwurf stehen. Für die Werkstatt möchte ich bis zur tatsächlichen Regelung nur belastbare Zuständigkeiten nennen. Über unbekannte Ansprüche, meine privaten Rechte oder einen automatischen Verkauf haben wir uns nicht geeinigt. Dieses Protokoll ersetzt weder Beschluss noch Unterschrift noch Vollzug.

Mit freundlichen Grüßen
Ottilie Heller

Anlagen: V05_Gespraechsprotokoll_09_Oktober.docx; V04_Heller_Persoenliche_Position.pdf
''', ('V05_Gespraechsprotokoll_09_Oktober.docx', 'V04_Heller_Persoenliche_Position.pdf')),
    ],
)

# Amtliche Normen am 09.10.2026 abgerufen; Recherchemetadaten gehören nicht in
# die Briefe oder den Verhandlungsentwurf. Keine behauptete Rechtsprechung.
VERIFIED_LEGAL_SOURCES = (
    'https://www.gesetze-im-internet.de/gmbhg/__15.html',
    'https://www.gesetze-im-internet.de/gmbhg/__37.html',
    'https://www.gesetze-im-internet.de/gmbhg/__46.html',
    'https://www.gesetze-im-internet.de/gmbhg/__51a.html',
    'https://www.gesetze-im-internet.de/gmbhg/__53.html',
    'https://www.gesetze-im-internet.de/gmbhg/__54.html',
    'https://www.gesetze-im-internet.de/zpo/__276.html',
)
