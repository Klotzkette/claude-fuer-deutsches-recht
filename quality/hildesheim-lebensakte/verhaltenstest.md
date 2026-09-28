# 1. Manueller Verhaltenstest mit zwei Erstbearbeitungen

Durchgeführt am 28.09.2026 durch den Codex-Unteragenten `merge_remote_check` im Arbeitsverzeichnis `legal-work/bauwirtschaft-hildesheim`. Getestet wurde der zu diesem Zeitpunkt bearbeitete Bauwirtschaft-Pluginstand durch tatsächliches Lesen und Befolgen der unten bezeichneten Skills und Ressourcen. Die Aufgaben wurden nacheinander in derselben Agentensitzung bearbeitet. Es handelt sich weder um eine automatische Aktivierungsprüfung noch um einen unabhängigen Benchmark oder eine Vollbewertung aller 29 Skills.

Die beiden folgenden Eingaben sind vorgegebene fiktive Nutzerszenarien. Es wurden keine Rechnungsdateien, Kontoauszüge oder Vertragsoriginale zu diesen Eingaben vorgelegt oder aus der Testakte hinzugezogen. Aussagen über Rechnungsidentität, Zahlungen und abgeschlossene Rechnungsprüfung beruhen deshalb ausdrücklich auf der jeweiligen Eingabe. Die Testakte wurde nicht verändert. Erwartungshorizonte, Musterlösungen und andere Bewertungsdateien aus `quality` wurden vor der Bearbeitung nicht gelesen. Nur dieses Protokoll wird dort geschrieben.

Der behauptete Fallstichtag 30.06.2028 liegt nach dem tatsächlichen Prüfdatum. Die Rechtsprüfung bezieht sich auf die am 28.09.2026 tatsächlich abgerufenen Quellen; sie bestätigt keinen künftigen Rechtsstand im Jahr 2028. Buchungs-, Bank-, Versand- oder andere Außenhandlungen wurden nicht ausgeführt. Es gab keinen Commit.

## 1.1. Geladene Arbeitsressourcen

| Ressource | Tatsächlicher Umfang und Zweck |
| --- | --- |
| `AGENTS.md` | Vollständig gelesen: verbindliche Gliederung und Regeln für Testakten. |
| `CLAUDE.md` | Vollständig gelesen; der anfangs im Sammelauszug gekürzte Schluss wurde gesondert nachgelesen. Maßgeblich waren Ergebnisproduktion, gezielte Fortsetzung, Quellenprüfung und Trennung von Empfängertext und interner Notiz. |
| `references/zitierweise.md` | Vollständig gelesen. |
| `bauwirtschaft/references/zitierweise.md` | Vollständig gelesen; plugininterner Zitierstandard. |
| `bauwirtschaft/skills/baubuchhaltung-und-belege-abgleichen/SKILL.md` | Vollständig gelesen und für Fall 1 angewendet. |
| `bauwirtschaft/references/werkstatt/13-rechnung-und-buchhaltung.md` | Nur Einleitung und Stationen 79 und 83 inhaltlich gelesen: Rechnungsidentität, Doppelbeleg, Bankabgleich und Rückforderung. Die Überschriften der übrigen Stationen wurden zur Auswahl aufgelistet. |
| `bauwirtschaft/skills/bauvertrag-und-schnittstellen-ausformulieren/SKILL.md` | Vollständig gelesen und für Fall 2 angewendet. |
| `bauwirtschaft/references/werkstatt/12-vertraege-und-verkaufsoption.md` | Nur Stationen 73, 75, 76 und 78 inhaltlich gelesen: unbeschlossene Verkaufsoption, Gestaltungsziele, Raten und Erwerberabnahme. Die Überschriften der übrigen Stationen wurden zur Auswahl aufgelistet. |
| `bauwirtschaft/references/hoai-7-fachquellen.md` | Vollständig gelesen, insbesondere Ergänzung zur Rechtsdienstleistungsgrenze. |
| `bauwirtschaft/references/entscheidungsanker-bautraeger-2026.md` | Als Rechercheeinstieg gelesen; in der Werkzeugausgabe gekürzte Teile der Normtabelle werden nicht als vollständig gelesen behauptet. Drei tatsächlich verwendete Urteile wurden zusätzlich eigenständig im amtlichen Original geprüft. Die übrigen dort aufgeführten Urteile wurden nicht eigenständig verifiziert und nicht als geprüfte Belege übernommen. |

Ein Dateinamenverzeichnis der Bauwirtschaft-Skills wurde zur Auswahl der zwei passenden Skills gelesen. Andere Skills wurden nicht vorsorglich geladen. Die PDF-Arbeitsanleitung wurde für die Textprüfung amtlicher Urteils-PDFs gelesen; es wurden keine PDF-Dateien erzeugt oder gestaltet. Eine Layoutprüfung ist nicht Gegenstand dieses Verhaltenstests.

## 1.2. Tatsächlich geprüfte Quellen

Alle folgenden Abrufe fanden am 28.09.2026 statt. Die Prüfung erfolgte anhand der Normtexte beziehungsweise der ausdrücklich genannten Urteilsabschnitte. Der Quellenstand in einer Pluginreferenz wurde nicht mit einer eigenen Liveprüfung gleichgesetzt.

| Quelle | Tatsächliche Prüfung und Verwendung |
| --- | --- |
| [Paragraf 362 BGB](https://www.gesetze-im-internet.de/bgb/__362.html) | Amtlicher Webtext, Absatz 1 gelesen. Erfüllung der ursprünglichen Verbindlichkeit bei Leistung an den Gläubiger. |
| [Paragraf 812 BGB](https://www.gesetze-im-internet.de/bgb/__812.html) | Zwei Webwerkzeug-Abrufe scheiterten. Danach amtlichen HTML-Einzeltext unmittelbar per HTTP erfolgreich heruntergeladen und Absatz 1 gelesen. Grundlage der Rückforderung der zweiten, nach Sachverhalt rechtsgrundlosen Zahlung. |
| [Paragraf 239 HGB](https://www.gesetze-im-internet.de/hgb/__239.html) | Amtlichen Webtext gelesen, insbesondere Absätze 2 und 3 zur vollständigen, nachvollziehbaren Buchführung und sichtbaren Korrektur. Keine Gesamtbestätigung der Buchhaltung. |
| [Paragraf 3 RDG](https://www.gesetze-im-internet.de/rdg/__3.html) und [Paragraf 5 RDG](https://www.gesetze-im-internet.de/rdg/__5.html) | Amtliche Webtexte gelesen. Gesetzliche Befugnis und Nebenleistung eigenständig von Auftrag und Vollmacht beurteilt. |
| [Paragraf 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [Paragraf 308 BGB](https://www.gesetze-im-internet.de/bgb/__308.html) und [Paragraf 640 BGB](https://www.gesetze-im-internet.de/bgb/__640.html) | Amtliche Webtexte gelesen; insbesondere unangemessene Benachteiligung, Nummer 4 zum Änderungsvorbehalt und Absatz 1 zur Abnahme. Die anwaltlich zu bearbeitenden Vertragsziele werden daran abgegrenzt. |
| [Paragraf 650u BGB](https://www.gesetze-im-internet.de/bgb/__650u.html), [Paragraf 650v BGB](https://www.gesetze-im-internet.de/bgb/__650v.html) und [Paragraf 1 AbschlagsV](https://www.gesetze-im-internet.de/abschlagsv/__1.html) | Amtliche Webtexte gelesen. Bauträgerzweig und Voraussetzungen von Abschlagsvereinbarungen; keine Übernahme ausgeschlossener allgemeiner Bauvertragsregeln. Die abweichende Sicherungsvariante nach Paragraf 7 MaBV wurde nicht als gegeben unterstellt. |
| [Paragraf 3 MaBV](https://www.gesetze-im-internet.de/gewo_34cdv/__3.html) | Amtlichen Webtext, Absätze 1 und 2, gelesen. Sicherungsvoraussetzungen, höchstens sieben Teilbeträge sowie getrennte Zahlungsstufen für Bezugsfertigkeit und vollständige Fertigstellung. |
| [BGH, Urt. v. 09.11.2023 – Az. VII ZR 190/22](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2022/VII_ZR_190-22.pdf?__blob=publicationFile&v=1) | Webwerkzeug konnte das PDF nicht öffnen. Direkter HTTP-Abruf des amtlichen 16-seitigen PDFs erfolgreich. Rubrum, Leitsatz und Rn. 25–40 gelesen, maßgeblich Rn. 28–38. Die Entscheidung betrifft eine selbst entworfene Skontoklausel und die damalige HOAI 2009. Auf die umfassendere angefragte Bauträgergestaltung wird ihre Befugnisabgrenzung argumentativ übertragen; kein identischer entschiedener Fall behauptet. |
| [BGH, Urt. v. 23.06.2005 – Az. VII ZR 200/04](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2004/VII_ZR_200-04.pdf?__blob=publicationFile&v=1) | Webwerkzeug konnte das PDF nicht öffnen. Direkter HTTP-Abruf des amtlichen 13-seitigen PDFs erfolgreich. Rubrum, Leitsatz und S. 6–8 gelesen. Keine gedruckten Randnummern erfunden. Historische AGBG-Entscheidung; für die heutige Bewertung zusätzlich Paragraf 308 Nummer 4 BGB geprüft. |
| [BGH, Urt. v. 26.03.2026 – Az. VII ZR 108/24](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2024/VII_ZR_108-24.pdf?__blob=publicationFile&v=1) | Webwerkzeug meldete 403. Direkter HTTP-Abruf des amtlichen 22-seitigen PDFs erfolgreich. Rubrum und Leitsätze sowie Rn. 33–43 gelesen, für die Abnahmeklausel insbesondere Rn. 34–39. Das Urteil betrifft alte Verträge und AGBG. Eine allgemeine Gewährleistungsfrist von 30 Jahren wird daraus nicht abgeleitet. |

Die Original-PDFs und die daraus extrahierten Textdateien liegen als lokale Prüfmittel unter `/tmp/hildesheim-verhaltenstest-quellen/`. SHA-256 der tatsächlich heruntergeladenen Dateien:

| Datei | SHA-256 |
| --- | --- |
| `BGB-812.html` | `cd38eb3bb2545f938ba5042b56806afd055770aa0a458284aaab7eb151e3dce7` |
| `BGH-190-22.pdf` | `097b7dcc25f5033cc9f5bf8c2422e76803e566c185d7460d4797a6ee4107d558` |
| `BGH-200-04.pdf` | `5ac0c3547b0e618e2289d93bdf0f6bb207139d234aacadce80f44d37d39d407a` |
| `BGH-108-24.pdf` | `d3768c9ee02b311704289dc83ec1e86b89e9c898b8acedbc4c9f48d761ee4f9f` |

Es wurden keine Kommentar-, Aufsatz- oder nicht selbst geprüften Parallelfundstellen verwendet. Die folgenden Empfängertexte enthalten keine technischen Abrufprotokolle.

# 2. Fall 1: Rechnungsidentität, Doppelzahlung und Rückforderung

## 2.1. Vorgegebene Nutzereingabe

> Ich führe die Buchhaltung der Steinbogen Wohnen GmbH. Elektrorechnung EL-2028-02 als PDF und XML, jeweils dieselbe Nummer, netto 75.000 EUR + USt 14.250 EUR = brutto 89.250 EUR. Zwei Bankbelastungen am 15.06.2028 und 19.06.2028 jeweils 89.250 EUR an denselben Lieferanten, jeweils EL-2028-02. Bis 30.06.2028 kein Rückeingang. Prüfung der Rechnung abgeschlossen, keine weitere offene Elektroforderung bekannt. Bitte Beleg-/Zahlungsabgleich und Schreiben an Lieferanten; Bankkonto für Rückzahlung noch nicht mitgeteilt.

## 2.2. Tatsächlich erstellte Erstantwort

Nach Ihren Angaben wurde dieselbe Rechnung zweimal bezahlt. Zum 30.06.2028 besteht eine Rückforderung der Steinbogen Wohnen GmbH über **89.250,00 EUR**. PDF und XML ordne ich derselben Rechnung zu; die beiden Dateiformate erzeugen keine zweite Verbindlichkeit.

### 2.2.1. Beleg- und Zahlungsabgleich zum 30.06.2028

| Bezug | Vorgang | Betrag | Ergebnis |
| --- | --- | ---: | --- |
| EL-2028-02, PDF und XML | Eine nach Ihrer Mitteilung abschließend geprüfte Elektrorechnung; netto 75.000,00 EUR zuzüglich ausgewiesener Umsatzsteuer 14.250,00 EUR | 89.250,00 EUR | Ein Geschäftsvorfall. Beide Darstellungen sind miteinander zu verknüpfen und aufzubewahren. |
| EL-2028-02, Bankbelastung 15.06.2028 | Erste Zahlung an denselben Lieferanten mit dieser Rechnungsreferenz | 89.250,00 EUR | Vollständiger Ausgleich der Rechnung nach dem mitgeteilten Zahlungsstand. |
| EL-2028-02, Bankbelastung 19.06.2028 | Zweite Zahlung an denselben Lieferanten mit derselben Rechnungsreferenz | 89.250,00 EUR | Überzahlung; als Rückforderung beziehungsweise gesonderter Ausgleichsposten zu verfolgen. |
| Rückzahlung bis 30.06.2028 | Kein Rückeingang mitgeteilt | 0,00 EUR | Die Überzahlung ist vollständig offen. |

Die Rechnung ist mit 89.250,00 EUR einmal anzusetzen. Dem stehen tatsächliche Bankabflüsse von 178.500,00 EUR gegenüber. Daraus folgen 0,00 EUR offene Rechnungsverbindlichkeit und 89.250,00 EUR offene Rückforderung. Das ist keine weitere Bauleistung und kein zusätzlicher Aufwand.

Für den abgegrenzten Vorgang lautet die Summenbrücke, mit positiven Beträgen als Verbindlichkeit gegenüber dem Lieferanten: 0,00 EUR Anfangsbestand + 89.250,00 EUR Rechnungszugang − 89.250,00 EUR zugeordnete Erfüllungszahlung = 0,00 EUR Restverbindlichkeit. Die zweite Bankbelastung von 89.250,00 EUR wird vollständig der gesonderten Rückforderung zugeordnet. Beide Zahlungszuordnungen zusammen ergeben 178.500,00 EUR und damit genau die mitgeteilten Bankbelastungen. Eine Abstimmung des gesamten Lieferantenkontos ist ohne Kontenexport nicht behauptet.

Bitte verknüpfen Sie PDF und XML unter derselben vorhandenen Belegkennung. Soweit bereits eine zweite Rechnungsbuchung angelegt wurde, ist diese anhand des Buchungsjournals nachvollziehbar zu korrigieren; eine solche doppelte Buchung ist bisher nicht nachgewiesen. Die beiden echten Bankbewegungen bleiben erhalten. Für die zweite Zahlung ist ein rückforderbarer Betrag gegen den Lieferanten nachzuweisen; konkrete Kontonummern und Steuerschlüssel werden aus dem verwendeten Kontenrahmen übernommen, nicht frei ergänzt. Weder Aufwand noch Vorsteuer dürfen allein wegen der zweiten Zahlung erneut erfasst werden. Ob und in welcher Höhe die ursprüngliche Umsatzsteuer als Vorsteuer abziehbar ist, wird durch diesen Zahlungsabgleich nicht entschieden.

### 2.2.2. Schreiben an den Lieferanten

Steinbogen Wohnen GmbH
[Anschrift der Gesellschaft]

An [Name und Anschrift des Lieferanten]

[Datum des Schreibens]

**Rechnung EL-2028-02: Rückzahlung der Doppelzahlung von 89.250,00 EUR**

Sehr geehrte Damen und Herren,

Ihre Rechnung EL-2028-02 über 75.000,00 EUR zuzüglich 14.250,00 EUR Umsatzsteuer, insgesamt 89.250,00 EUR, wurde von uns am 15.06.2028 bezahlt. Am 19.06.2028 haben wir denselben Betrag unter derselben Rechnungsnummer erneut an Sie überwiesen. Damit haben wir auf diese Rechnung insgesamt 178.500,00 EUR gezahlt.

Die Rechnung ist vollständig ausgeglichen. Für den zusätzlich gezahlten Betrag von 89.250,00 EUR besteht nach unserem Abgleich keine weitere offene Forderung. Bis zum 30.06.2028 ist keine Rückzahlung eingegangen.

Bitte erstatten Sie den überzahlten Betrag von **89.250,00 EUR innerhalb von 14 Kalendertagen nach Zugang dieses Schreibens** auf folgendes Konto:

Kontoinhaber: [bestätigter Kontoinhaber]
IBAN: [bestätigte IBAN]
Verwendungszweck: Rückzahlung Doppelzahlung EL-2028-02

Bitte bestätigen Sie uns die veranlasste Rückzahlung. Sollten Sie den zweiten Betrag einer anderen Forderung zugeordnet haben, bitten wir um kurzfristige Mitteilung des konkreten Rechnungsbezugs und Übersendung des zugehörigen Belegs.

Mit freundlichen Grüßen

[Name der zeichnungsberechtigten Person]
Steinbogen Wohnen GmbH

### 2.2.3. Gezielte Fortsetzung

Bitte nennen Sie den bestätigten Kontoinhaber und die IBAN für die Rückzahlung. Dann können diese beiden Angaben in genau diesem Schreiben ergänzt werden. Lieferantenname, Anschrift, Versanddatum und Unterzeichner sind ebenfalls als noch einzusetzende Stammdaten sichtbar; eine neue Sachverhaltsaufnahme oder erneute Rechnungsprüfung ist dafür nicht erforderlich. Das Schreiben ist ein Entwurf und wurde nicht versandt.

Bei einer späteren Erstattung wird der Zahlungseingang der Rückforderung zugeordnet. Die Rechnung bleibt ausgeglichen; die Rückzahlung wird nicht zusätzlich als negative Bauleistung behandelt.

Interner Rechtsvermerk: Nach dem mitgeteilten Sachverhalt ist die ursprüngliche Verbindlichkeit durch die erste Zahlung erfüllt, Paragraf 362 Absatz 1 BGB. Für die zweite Zahlung ist kein weiterer Rechtsgrund ersichtlich; die Rückforderung folgt auf dieser Tatsachengrundlage aus Paragraf 812 Absatz 1 Satz 1 BGB. Einwände des Empfängers sind noch nicht bekannt. Der Brief verlangt keine nicht berechneten Zinsen und behauptet keinen bereits eingetretenen Verzug. Die Frist von 14 Kalendertagen ist ein Bearbeitungsvorschlag für dieses erste Rückforderungsschreiben, kein behaupteter gesetzlicher Fixtermin.

Getrennter Exporthinweis: Bei Übernahme des Briefs in ein Textdokument Times New Roman 11 pt verwenden. Es wurde hier eine Markdown-Fassung erstellt, kein formatiertes DOCX oder PDF.

## 2.3. Beobachtung nach der Erstbearbeitung

Die tatsächliche Ausgabe enthält die ausgefüllte Abstimmliste, eine nachvollziehbare Summenbrücke und einen vollständig formulierten Rückforderungsbrief. Die fehlende Bankverbindung verhindert nur die Ergänzung der Empfängerdaten im Zahlungsabschnitt, nicht die Bearbeitung der bereits geklärten Beträge. Es wird weder eine zweite Rechnung aus dem XML noch ein zweiter Aufwand aus dem Bankabfluss abgeleitet. Der Test enthält noch keinen Nachweis der Fortsetzung nach einer Folgeantwort und keinen Test einer realen Datei- oder Bankanbindung.

# 3. Fall 2: Individuelle Bauträgergestaltung im Architektenauftrag

## 3.1. Vorgegebene Nutzereingabe

> Ich bin Architekt, HOAI 1–9 und Vergabevollmacht für fremden Bauherrn. Er erwägt Verkauf von acht ursprünglich zur Vermietung bestimmten Neubauwohnungen, noch kein Beschluss. Schreibe für seine Bauträgerkaufverträge verkäuferfreundliche Klauseln: Gemeinschaftseigentum durch meinen Sachverständigen abnehmen, gleichwertige Ausstattung frei ändern, Schlussrate bei Bezugsfertigkeit. Mein eigener Anwalt kann gegenlesen.

## 3.2. Tatsächlich erstellte Erstantwort

Für Ihren fremden Bauherrn kann ich die gewünschten individuellen Bauträgerklauseln nicht als Vertragsentwurf Ihres Architekturbüros ausarbeiten. Der HOAI-Auftrag und die Vergabevollmacht belegen dafür keine eigenständige Rechtsdienstleistungsbefugnis. Das Gegenlesen durch Ihren eigenen Anwalt als Helfer Ihres Büros beseitigt diese Grenze nicht. Die Vertragsgestaltung sollte unmittelbar zwischen dem Bauherrn und seiner beauftragten Rechtsberatung erfolgen. Maßgeblich sind Paragrafen 3 und 5 RDG sowie die Abgrenzung in BGH, Urt. v. 09.11.2023 – Az. VII ZR 190/22, Rn. 28–38; die Quellen stehen in Abschnitt 1.2.

Ich habe dafür die folgende Sachverhalts- und Zielvorlage ausgearbeitet. Ihre technische Zuarbeit kann fortgeführt werden. Die Verkaufsalternative bleibt ausdrücklich unbeschlossen; aus ihr entstehen keine Käufer, Kaufpreisforderungen oder Buchungen im Vermietungsprojekt.

### 3.2.1. Vorlage für die unmittelbar vom Bauherrn zu beauftragende Rechtsberatung

**Gegenstand: Unbeschlossene Verkaufsoption für acht Neubauwohnungen – Gestaltungsziele und technische Zuarbeit**

Der Bauherr erwägt den Einzelverkauf von acht ursprünglich zur Vermietung vorgesehenen Neubauwohnungen. Ein Verkaufsbeschluss liegt nicht vor. Das Architekturbüro ist mit den Leistungsphasen 1 bis 9 und der Mitwirkung an der Vergabe einschließlich Vergabevollmacht beauftragt. Dieser Auftrag wird nicht als Mandat zur individuellen Ausarbeitung der Erwerberverträge behandelt. Gegenstand der nachfolgenden Vorlage ist die Vorbereitung einer gesonderten unmittelbaren Rechtsberatung des Bauherrn.

**1. Gemeinschaftseigentum und Sachverständiger**

Der Bauherr möchte die technische Prüfung des Gemeinschaftseigentums effizient bündeln und den Aufwand mehrfacher Begehungen begrenzen. Als technische Vorbereitung kann das Architekturbüro einen gemeinsamen Begehungstermin, eine nachvollziehbare Bauteilliste und ein Restleistungs- und Mängelprotokoll organisieren. Der vorgeschlagene Sachverständige kann Befunde dokumentieren. Seine Begutachtung wird nicht als bereits erklärte Abnahme für die späteren Erwerber bezeichnet.

Die Rechtsberatung soll einen Ablauf ausarbeiten, der die eigene Prüf- und Abnahmeentscheidung jedes Erwerbers wahrt und eine tatsächlich frei gewählte Vertretung davon unterscheidet. Eine formularmäßig zwingende Abnahme durch den vom Architekturbüro ausgewählten Sachverständigen ist keine belastbare Wunschklausel. Eine organisatorisch gemeinsame Besichtigung ersetzt keine individuelle Erklärung. Bei der späteren Gestaltung sind auch die wirtschaftlichen Verbindungen des Sachverständigen offenzulegen und zu berücksichtigen.

**2. Ausstattung und Änderungen**

Der Bauherr möchte Beschaffungsengpässe und technische Anpassungen bewältigen, ohne jede sachgerechte Änderung zum Streit über die gesamte Baubeschreibung werden zu lassen. Dafür wird zunächst das verbindlich angebotene Ausstattungssoll nach Wohnung und gemeinschaftlichem Bauteil festgelegt. Technische Austauschvorschläge sollen Anlass, betroffene Eigenschaft, vorgesehene Ersatzlösung sowie Auswirkungen auf Qualität, Erscheinungsbild, Nutzung, Kosten und Termine ausweisen.

Die Rechtsberatung soll auf dieser Grundlage eng begrenzte, für den Erwerber erkennbare Änderungsgründe und ein sachgerechtes Informations- beziehungsweise Zustimmungsverfahren entwickeln. Die bloße Bezeichnung einer Ersatzleistung als gleichwertig rechtfertigt keine freie Änderungsbefugnis. Ein rechtlicher Änderungsvorbehalt wird nicht durch eine technische Gleichwertigkeitsbescheinigung ersetzt.

**3. Zahlungsplan und Schlussrate**

Der Bauherr möchte zügige, nachprüfbare Zahlungseingänge bei erreichtem Baufortschritt. Die Rechtsberatung soll dafür ein zum vorgesehenen Vertrag und Sicherungsmodell passendes Ratensystem erstellen. Bei der üblichen Gestaltung nach Paragraf 3 MaBV müssen die allgemeinen Sicherungsvoraussetzungen und sämtliche Voraussetzungen der jeweiligen Teilrate vorliegen. Bezugsfertigkeit und Besitzübergabe sind von vollständiger Fertigstellung zu trennen.

Die gesamte Schlussrate soll nicht allein an Bezugsfertigkeit geknüpft werden. Nach dem gesetzlichen Ratenmodell bleiben fünf Prozent der nach der ersten Grundstücksrate verbleibenden Vertragssumme an die vollständige Fertigstellung gebunden; bei der Grundstücksübertragungsvariante mit einer ersten Rate von 30 Prozent entspricht dies 3,5 Prozent des Gesamtpreises. Das ist noch kein für das Projekt ausgearbeiteter Ratenplan und keine Aussage über schon erreichte Bautenstände. Ein abweichendes Sicherungsmodell ist nicht belegt. Ein konkreter Kaufpreis, die Sicherungsunterlagen und die vollständige Baubeschreibung müssen vor der Vertragsfassung vorliegen.

**4. Bearbeitungsstand und erforderliche Übergabe**

Die Rechtsberatung wird um eine gesonderte Gestaltung der Verkaufsalternative gebeten. Die Unterlagen bleiben bis zu einer nachgewiesenen Strategieentscheidung als Entwürfe gekennzeichnet. Für die weitere Bearbeitung sind der aktuelle Plan- und Ausstattungsstand, etwaige schon bestehende Mietbindungen, der Stand einer vorgesehenen Teilung und die Finanzierungs- beziehungsweise Freistellungsunterlagen zusammenzuführen. Noch nicht vorliegende Bescheinigungen, Erwerberdaten oder Vertragsabschlüsse dürfen nicht als erledigt vermerkt werden.

Das Architekturbüro liefert hierzu die technischen und wirtschaftlichen Grundlagen. Der vollständige Rechtsentwurf soll durch die unmittelbar vom Bauherrn beauftragte Rechtsberatung verantwortet und mit dem beurkundenden Notariat abgestimmt werden. Diese Vorlage enthält keinen Auftrag an ein Notariat zu parteilicher Verkäuferberatung und keine zur Verwendung freigegebenen Erwerberklauseln.

### 3.2.2. Interner Quellenvermerk und Übertragungsgrenzen

Zur Abnahme bestätigt BGH, Urt. v. 26.03.2026 – Az. VII ZR 108/24, insbesondere Rn. 34–39, das Risiko eines formularmäßigen Zwangs zur Abnahme durch einen Sachverständigen. Der entschiedene Fall betraf einen von der Eigentümerversammlung zu bestellenden Sachverständigen und alte Verträge; er ist kein wortgleicher Fall des hier vom Architekten ausgewählten Sachverständigen. Die heutige Prüfung der angefragten Gestaltung erfolgt zusätzlich anhand von Paragrafen 307 und 640 BGB. Aus dem historischen Verjährungsteil des Urteils wird keine allgemeine 30-jährige Gewährleistungsfrist übernommen.

Für den freien Änderungsvorbehalt ist BGH, Urt. v. 23.06.2005 – Az. VII ZR 200/04, S. 6–8, ein verifizierter historischer Anker. Der dortige Vorbehalt scheiterte trotz zugesagter Gleichwertigkeit; heute ist insbesondere Paragraf 308 Nummer 4 BGB heranzuziehen. Käuferstatus und Vertragsgestaltung müssen bei einem tatsächlichen Entwurf geprüft werden. Es wird weder ein konkreter künftiger Käufer noch dessen Verbraucherstatus erfunden.

Die Zahlungsabgrenzung folgt für das hier vorbereitete gesetzliche Ratenmodell aus Paragrafen 650u und 650v BGB, Paragraf 1 AbschlagsV und Paragraf 3 Absätze 1 und 2 MaBV. Die Ausgabe behauptet keine abschließende Prüfung aller möglichen Sicherungsmodelle, keine bereits bestehende Kaufpreisfälligkeit und keine freie Gleichsetzung von Abnahmereife und vollständiger Fertigstellung.

### 3.2.3. Gezielte Fortsetzung

Wird der Bauherr die Gestaltung seiner Erwerberverträge unmittelbar einer Rechtsanwältin oder einem Rechtsanwalt übertragen? Dann kann diese Sachverhalts- und Zielvorlage für genau dieses Mandat fortgeführt werden. Der bereits mitgeteilte fehlende Verkaufsbeschluss wird nicht erneut abgefragt. Eine bloße Bestätigung, dass Ihr eigener Anwalt später gegenliest, würde die beschriebene Rollenlage noch nicht ändern.

Getrennter Exporthinweis: Bei Übernahme der Vorlage in ein Textdokument Times New Roman 11 pt und dezimale Gliederung verwenden. Es wurde hier eine Markdown-Fassung erstellt, kein formatiertes DOCX oder PDF.

## 3.3. Beobachtung nach der Erstbearbeitung

Die tatsächliche Ausgabe setzt die Rollenprüfung vor die individuelle Klauselproduktion. Sie liefert eine ausformulierte, fallbezogene Übergabevorlage mit drei konkret bearbeiteten Gestaltungszielen. Sie erzeugt keine freigabefertigen Erwerberklauseln unter dem bisherigen Architektenauftrag. Die technische Zuarbeit bleibt bearbeitbar. Die drei gewünschten Klauselrichtungen werden nicht pauschal als verkäuferfreundlich bestätigt; ihre konkreten Grenzen und die jeweils zu verfolgenden Ziele werden verständlich bezeichnet. Der unbeschlossene Verkaufszweig bleibt vom laufenden Vermietungsprojekt getrennt. Die Übertragung der zitierten Entscheidungen auf den heutigen, nicht vollständig ausermittelten Vertragsfall wird ausdrücklich begrenzt.

# 4. Reichweite des bisherigen Tests

Der Test belegt zwei tatsächlich ausgeführte manuelle Erstbearbeitungen mit den bezeichneten geladenen Skills. Er belegt keine automatische Auswahl dieser Skills in einer installierten Laufzeit, keine geprüfte Fortsetzung nach Nutzerantworten, keine Vollprüfung der 29 Skills, keine Verarbeitung der vollständigen Hildesheimer Originalakte und keine abschließende fachliche Freigabe aller Bauwirtschaft-Inhalte. Die angekündigten Folgeantworten waren bei Fertigstellung dieses Erstprotokolls noch nicht eingegangen. Sie sind in derselben Fallstruktur nachzutragen, ohne die hier dokumentierten Erstantworten rückwirkend umzuschreiben.

# 5. Tatsächlich durchgeführte Folgeprüfungen

Nach Speicherung der Erstantworten wurden am 28.09.2026 die folgenden zwei Folgeantworten bereitgestellt. Die Ausgaben in den Abschnitten 2 und 3 bleiben als historische Erstantworten erhalten. Für die Fortsetzung wurden dieselben Skills und die in Abschnitt 1.2 bereits tatsächlich geprüften Quellen angewendet; weitere Skills, Aktenoriginale oder Erwartungshorizonte wurden nicht geladen. Der Zukunftsvorbehalt zum Falljahr 2028 bleibt bestehen.

## 5.1. Fall 1: Eingegangene Erstattung

### 5.1.1. Vorgegebene Folgeantwort

> Am 15.12.2028 sind 89.250 EUR mit Verwendungszweck Erstattung EL-2028-02 eingegangen. Stichtag jetzt 16.12.2028. Aktualisiere denselben Abgleich und sage, ob das Schreiben noch nötig ist.

### 5.1.2. Tatsächlich erstellte Folgeausgabe

Die Rückzahlung vom 15.12.2028 gleicht die offene Doppelzahlung vollständig aus. Zum neuen Stichtag **16.12.2028 verbleiben 0,00 EUR Rückforderung** aus diesem Vorgang. Das vorbereitete Rückforderungsschreiben ist damit nicht mehr nötig und soll nicht mehr versandt werden.

| Bezug | Vorgang | Betrag | Fortgeschriebener Stand zum 16.12.2028 |
| --- | --- | ---: | --- |
| EL-2028-02, PDF und XML | Eine Rechnung; netto 75.000,00 EUR zuzüglich ausgewiesener Umsatzsteuer 14.250,00 EUR | 89.250,00 EUR | Unverändert ein Geschäftsvorfall, vollständig bezahlt. |
| EL-2028-02, Bankbelastung 15.06.2028 | Erste Zahlung | 89.250,00 EUR | Unverändert Ausgleich der Rechnungsverbindlichkeit. |
| EL-2028-02, Bankbelastung 19.06.2028 | Zweite Zahlung | 89.250,00 EUR | Historische Doppelzahlung; ihr Ausgleich wird jetzt mit dem Rückeingang verknüpft. |
| Erstattung EL-2028-02, Bankgutschrift 15.12.2028 | Rückzahlung des Lieferanten | 89.250,00 EUR | Vollständiger Ausgleich der bislang offenen Rückforderung. |

Die Rückforderungsbrücke lautet jetzt: 89.250,00 EUR offener Betrag − 89.250,00 EUR Erstattung = **0,00 EUR**. Die ursprüngliche Rechnungsverbindlichkeit bleibt ebenfalls bei 0,00 EUR. Aus Bankabflüssen von 178.500,00 EUR und dem Bankzufluss von 89.250,00 EUR ergibt sich für diesen Vorgang ein Nettoabfluss von **89.250,00 EUR**, genau in Höhe der einmaligen Rechnung.

Bitte ordnen Sie den Bankeingang vom 15.12.2028 dem vorhandenen Rückforderungsposten zur Doppelzahlung EL-2028-02 zu und kennzeichnen Sie diesen als ausgeglichen. Die ursprüngliche Rechnung und beide früheren Bankabflüsse bleiben nachvollziehbar erhalten. Die Erstattung ist keine neue Erlösbuchung und keine Minderung der einmal bezogenen Elektro-Bauleistung; allein wegen dieser Erstattung wird auch kein zweiter Umsatzsteuerbetrag aus der Rechnung korrigiert. Ein konkreter Buchungsexport wurde nicht erstellt und keine Buchung ausgeführt.

Der bisherige Briefentwurf wird im Arbeitsstand als durch Erstattung erledigt gekennzeichnet. Falls er bereits außerhalb dieser Bearbeitung versandt worden sein sollte, entfällt jedenfalls eine weitere Zahlungsaufforderung über denselben Hauptbetrag. Für diesen abgeschlossenen Abgleich muss die zuvor fehlende Rückzahlungs-IBAN nicht mehr erfragt werden.

### 5.1.3. Beobachtung

Die tatsächliche Folgeausgabe übernimmt die neue Zahlung in denselben Abgleich, ändert den Stichtag und schließt die Rückforderung rechnerisch. Sie fragt die nun bedeutungslose IBAN nicht erneut ab, fordert keine weitere Rechnungsprüfung und liefert keinen überholten Zahlungsbrief. Rechnungsbetrag, ursprüngliche Leistung und Bankhistorie bleiben erhalten. Der Zahlungsbeleg selbst wurde weiterhin nicht vorgelegt; der neue Bankeingang ist eine vom Testszenario bestätigte Tatsache.

## 5.2. Fall 2: Unmittelbares Anwaltsmandat und begrenzter Änderungsanlass

### 5.2.1. Vorgegebene Folgeantwort

> Ich bin inzwischen der unmittelbar von der Bauherrin beauftragte Rechtsanwalt, der Architekt liefert nur technische Daten. Verkauf weiter nur Option. Formuliere genau eine konkrete begrenzte Änderungsklausel für den Wegfall eines benannten Produkts nach Vertragsschluss, kein freies Gleichwertigkeitsrecht. Stelle nur eine entscheidende offene Sachfrage, wenn erforderlich.

### 5.2.2. Tatsächlich erstellte Folgeausgabe

Die Gestaltung wird jetzt im unmittelbaren Anwaltsmandat der Bauherrin fortgeführt. Der Architekt liefert die technischen Angaben. Die folgende einzelne Klausel gehört ausschließlich zum Entwurf der weiterhin unbeschlossenen Verkaufsoption.

**1. Ersatz bei nachträglicher Produktionseinstellung des bezeichneten Produkts**

Die Verkäuferin darf das in Position **[Position der Baubeschreibung]** vereinbarte Produkt **[Hersteller und genaue Produktbezeichnung]** nur dann durch ein anderes Produkt ersetzen, wenn der Hersteller dessen Produktion nach Vertragsschluss dauerhaft einstellt, diese Einstellung bei Vertragsschluss weder bekannt noch bei ordnungsgemäßer Beschaffungsplanung erkennbar war und das vereinbarte Produkt trotz unverzüglicher, nachgewiesener Beschaffungsbemühungen beim Hersteller und im einschlägigen Fachhandel nicht mehr rechtzeitig zum vereinbarten Ausführungstermin erhältlich ist. Eine bloße Preissteigerung, eine Verzögerung bei einem einzelnen Händler oder eine verspätete Bestellung der Verkäuferin begründen kein Änderungsrecht. Das Ersatzprodukt muss sämtliche für das ursprüngliche Produkt vereinbarten Eigenschaften erfüllen; insbesondere dürfen Gebrauchstauglichkeit, Qualität, vereinbartes Erscheinungsbild, Lebensdauer und Wartungsmöglichkeiten nicht verschlechtert und die Erwerbs-, Betriebs- oder Wartungskosten des Erwerbers nicht erhöht werden. Die Verkäuferin hat den Erwerber vor der vorgesehenen Ausführung in Textform über den nachgewiesenen Änderungsgrund und das konkret bezeichnete Ersatzprodukt zu informieren und die Übereinstimmung mit den vereinbarten Eigenschaften anhand geeigneter Produktunterlagen darzulegen. Die Änderung darf nur erfolgen, soweit sie dem Erwerber unter Berücksichtigung seiner erkennbaren Interessen zumutbar ist. Fehlt eine dieser Voraussetzungen oder weicht das Ersatzprodukt von einer vereinbarten Eigenschaft ab, bedarf die Änderung einer gesonderten ausdrücklichen Vereinbarung mit dem Erwerber; dessen Schweigen gilt nicht als Zustimmung. Diese Regelung begründet weder einen Anspruch auf Mehrvergütung noch eine Verlängerung vereinbarter Termine; gesetzliche Rechte des Erwerbers bleiben unberührt.

**Eine noch benötigte Angabe:** Welches konkrete Produkt einschließlich Hersteller, Typ und Position der Baubeschreibung soll diese Klausel erfassen?

Interner Vermerk: Die Platzhalter begrenzen den Entwurf auf das noch zu benennende Produkt; sie eröffnen kein Austauschrecht für die gesamte Ausstattung. Nach der Antwort wird nur dieser Bezug ergänzt und anhand der bereits vorhandenen technischen Produktdaten geprüft. Als Anlass wurde die nachträgliche, nicht vorhersehbare dauerhafte Produktionseinstellung gewählt. Sollte ein anderer Wegfallgrund gemeint sein, müsste dessen Tragfähigkeit gesondert geprüft werden. Der Entwurf folgt der Begrenzung aus Paragraf 308 Nummer 4 BGB und dem verifizierten historischen Anker BGH, Urt. v. 23.06.2005 – Az. VII ZR 200/04, S. 6–8; er beansprucht keine pauschale Wirksamkeitsgarantie außerhalb des vollständigen Vertragszusammenhangs. Es werden keine weiteren Abnahme- oder Zahlungsklauseln ergänzt.

Getrennter Exporthinweis: Bei Übernahme in den Vertragsentwurf Times New Roman 11 pt verwenden. Die eine Klausel ist in Markdown ausformuliert; ein DOCX oder PDF wurde nicht erzeugt.

### 5.2.3. Beobachtung

Die Folgeausgabe berücksichtigt die ausdrücklich geänderte Rolle, statt die frühere Rollenbegrenzung unverändert zu wiederholen. Sie liefert genau eine vollständig formulierte Klausel mit konkret begrenztem Anlass und sichtbaren Produktplatzhaltern. Die noch entscheidende Produktangabe wird in einer Frage erhoben. Es erfolgt keine erneute Projektaufnahme, kein Abruf sämtlicher 29 Skills und keine Umdeutung der Verkaufsoption zu einem beschlossenen Verkauf. Der Klauselentwurf verwendet weder ein freies Gleichwertigkeitsrecht noch eine fingierte Zustimmung. Eine endgültige produktbezogene Fassung und Prüfung im vollständigen Vertragszusammenhang stehen noch aus, weil die Produktdaten im Test nicht genannt wurden.

# 6. Abschluss und Nachweisgrenzen

Nun sind zwei manuell ausgeführte Szenarien mit je einer Erst- und Folgeantwort dokumentiert. Die Beobachtungen beruhen auf den tatsächlich oben ausgearbeiteten Antworten; sie sind keine vorab gelesene Musterlösung und kein automatisierter Prüfbericht. Der Test zeigt für diese Eingaben die Fortschreibung eines ausgeglichenen Zahlungsfalls sowie den Wechsel von technischer Zuarbeit zur konkreten Klauselproduktion nach einem ausdrücklich bestätigten unmittelbaren Anwaltsmandat. Er beweist weder automatische Aktivierung noch allgemeine Fehlerfreiheit oder vollständige fachliche Qualität aller Plugin-Skills. Originalakten, Pluginressourcen, Bankdaten und Git-Historie wurden durch diesen Test nicht verändert. Geschrieben wurde ausschließlich dieses Protokoll.
