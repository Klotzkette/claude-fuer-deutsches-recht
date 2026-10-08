---
name: mandatsannahme-interessenkollision
description: "Verwenden, wenn eine neue Anfrage, ein neuer Gegner, ein Zahler neben dem Mandanten, ein Kollisionstreffer oder ein Onlinemandat mit sofortigem Beginn eingeht. Liefert Annahme, begrenzte Beauftragung oder Absage als ausformuliertes Schreiben samt Prüfnotiz zu Identität, Vertretung, Konflikt und Widerruf. Nicht für Fristrechnung oder Honorarhöhe."
---

# Mandat annehmen und Interessenkollision prüfen

## 1. Zweck und Anwendungsfall

Dieser Skill führt eine konkrete Mandatsanfrage zu einer tragfähigen Annahmeentscheidung und einem verwendbaren Schreiben. Er bearbeitet Erstmandate, neue Angelegenheiten bestehender Mandanten, gemeinsame Mandate, Mandatswechsel, Drittfinanzierung und nachträglich erkannte Konflikte. Eine vorbereitete Akte oder erste Zahlung bedeutet keine Annahme jedes gewünschten Auftrags; umgekehrt kann ein Mandat durch tatsächliches Verhalten entstehen, und ein internes Feld „Annahme offen“ verhindert dies nicht, wenn nach außen bereits verbindlich gearbeitet wird.

Ziel ist eine klare Antwort darauf, wer wessen Interessen in welcher Sache ab wann mit welchem Umfang vertritt. Mandatsvertrag, Vollmacht, Vergütungsvereinbarung, Datenverarbeitung und Empfangsvollmacht werden getrennt geprüft, ohne den Mandanten mit fünf Formularrunden zu belasten. Die Kollisionsprüfung untersucht tatsächliche Interessen und dieselbe Rechtssache; sie ist weder auf einen Namensvergleich reduzierbar noch ein allgemeines Verbot, Wettbewerber zu beraten. Der Skill wahrt den erteilten Auftrag: Eine Beratungsanfrage wird nicht eigenmächtig in Prozessvertretung oder eine Mitteilung an die Gegenseite umgewandelt. Ist die Annahme unzulässig oder unmöglich, entsteht eine klare, rechtzeitige Absage mit den notwendigen Informationen zu erkennbaren Fristen.

### 1.1. Auslöser, Abgrenzung und Nachbarskills

Starte diesen Skill, wenn eine Person oder ein Unternehmen erstmals um anwaltliche Hilfe bittet und noch nicht feststeht, ob und mit welchem Umfang die Kanzlei tätig wird. Starte ihn, wenn ein bestehender Mandant eine neue Angelegenheit mit neuen Beteiligten anfragt, wenn Gesellschafter, Erben oder Ehegatten gemeinsam beraten werden wollen, wenn ein Berufsträger mit Altmandaten eintritt oder ausscheidet, und wenn im laufenden Mandat eine neue Partei, eine Widerklage oder ein Organwechsel die Interessenlage verändert.

Die Berechnung einer konkreten Frist übernimmt [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md); dieser Skill sichert nur das fristauslösende Dokument und übergibt das Fristobjekt im Zustand „erfasst“. Die Honorarverhandlung im Einzelnen, insbesondere Deckel, Phasen und Änderungsmechanik, gehört zu [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md). Die Identifizierung nach dem Geldwäschegesetz übernimmt [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md). Allgemeine Berufsrechtsfragen ohne konkrete Anfrage, etwa zu Werbung, Fremdgeld oder KI-Dienstleistern, beantwortet [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md). Die Aktenanlage nach der Annahme übernimmt [Akte und Fristen anlegen](../akte-fristen-anlegen/SKILL.md), die Beendigung [Mandat abschließen](../mandat-abschliessen/SKILL.md).

Dieser Skill versendet nichts, legt keine Vollmacht als erteilt an und leistet keine Sachbearbeitung über die zur Annahmeentscheidung notwendige Sichtung hinaus.

## 2. Eingaben

### 2.1. Anfrage und gewünschtes Ergebnis

Lies die vollständige Anfrage und vorhandene Unterlagen. Erfasse Anlass, gewünschten Erfolg, Rechtsgebiet, Verfahrensstand, bekannte Gegner, Fristen und bisherige Vertretung. Eine Anfrage „Bitte prüfen“ kann eine Erstbewertung oder umfassende Beratung meinen; kläre nur die für Umfang und Fristsicherung entscheidende Unschärfe und frage nicht nach Daten, die aus Dokumenten feststehen.

Bestimme den tatsächlichen Interessenträger. Bei Unternehmen sind genaue Firma, Registeridentität, Sitz und handelndes Organ zu ermitteln; ein Geschäftsführer kann für die Gesellschaft oder persönlich um Rat bitten. Bei Familie, Erbengemeinschaft, Wohnungseigentümergemeinschaft oder Anlegergruppe sind gemeinsame Interessen und individuelle Rechte nicht deckungsgleich. Der Kontakt über dieselbe E-Mail-Adresse ersetzt keine Mandantenbestimmung.

### 2.2. Vertretung, Kostenträger und Datenzugriff

Erfasse die Vertretungsgrundlage und ihre Belege. Bei juristischen Personen kann Registereinsicht, Satzung, Vollmacht oder Organbeschluss nötig sein; bei Minderjährigen, Betreuung, Insolvenz oder Nachlassverwaltung sind besondere Zuständigkeiten zu prüfen. Eine Vollmacht zur Zahlungsabwicklung ist keine Befugnis zur Beauftragung einer Prozessvertretung; eine eingesandte Vollmacht ist auf Inhalt, Umfang und Aussteller zu prüfen.

Kostenträger und Informationsberechtigte werden getrennt erhoben. Rechtsschutzversicherung, Arbeitgeber, Verwandter oder Finanzierer können zahlen, ohne Mandant zu werden; kläre, welche Informationen sie erhalten dürfen. Eine Deckungszusage ist kein Vergütungsvertrag; eine offene Deckungsanfrage bedeutet nicht, dass die Kanzlei kostenlos oder gar nicht beauftragt wurde.

### 2.3. Konfliktbestand und Vorbefassung

Benötigt werden alle für die Prüfung erheblichen Parteien, frühere Namen, verbundene Rechtsträger, wirtschaftlich betroffene Personen und sachliche Beziehungen. Erfasse nicht unterschiedslos den gesamten Konzern, wenn nur eine Tochter betroffen ist; erhebe aber zusätzliche Gesellschaften, wenn deren Interessen konkret relevant werden. Bei häufigen Namen können Geburtsdatum oder Anschrift zur sicheren Zuordnung notwendig sein.

Prüfe frühere persönliche Tätigkeit der vorgesehenen Berufsträger und relevante gemeinschaftliche Berufsausübung, einschließlich früherer Kanzleien, Referendartätigkeit und anderer beruflicher Funktionen. Eine vollständige alte Mandatsakte darf nicht allein für die Kollisionssuche weitergegeben werden; die gesetzlich erlaubte Offenbarung erforderlicher Konfliktdaten ist keine Erlaubnis zum Wissenstransfer.

### 2.4. Entscheidende Angaben

| Angabe | Warum entscheidend | Vorgehen, wenn sie fehlt |
|---|---|---|
| Genauer Rechtsträger des Mandanten | Bestimmt Interessenrichtung, Vertretungsmacht und Konfliktsuche | Rückfrage 1 stellen; Entwurf mit Platzhalter „[Mandantin]“ vorbereiten |
| Gegner und weitere Beteiligte mit Identifikatoren | Ohne sie ist die Konfliktsuche unvollständig | Suche mit bekannten Namen beginnen; Status „Prüfung ausstehend“ |
| Gewünschtes Ergebnis und Auftragsumfang | Trennt Erstbewertung, Beratung und Vertretung | Rückfrage 2 stellen; nur Erstbewertung als gesichert behandeln |
| Fristauslösende Dokumente mit Zugangsdatum | Frist kann die gesamte Reihenfolge bestimmen | Dokument anfordern; Frist als „möglich, ungeprüft“ sofort melden |
| Vertretungsnachweis des Handelnden | Ohne ihn gibt es keinen gesicherten Auftraggeber | Registerauszug oder Vollmacht anfordern; Annahme bedingt formulieren |
| Kostenträger und Informationsrechte Dritter | Verhindert heimliche Steuerung und Geheimnisbruch | Rückfrage 4 stellen; Berichtsregel offenlassen |
| Verbraucherstatus und Vertragsschlussweg | Entscheidet über Fernabsatz, Belehrung und Widerruf | Rückfrage 5 stellen; Belehrung vorsorglich beifügen |
| Frühere Tätigkeit der Berufsträger in der Sache | Persönliches Verbot ist nicht heilbar | Berufsträger einzeln befragen; bis dahin keine Zuteilung |
| Vergütungsgrundlage | Ohne sie keine Leistungszusage mit Kostenfolge | Honorarskill anstoßen; Annahmeschreiben ohne Preisangabe nicht versenden |
| Zugang zum Konfliktregister | Entscheidet, ob ein Negativbefund möglich ist | Ungeprüften Teilbestand benennen; verantwortliche Person festlegen |

### 2.5. Rückfragen in der richtigen Reihenfolge

Stelle nur Fragen, deren Antwort die Annahmeentscheidung verändert, und zwar in dieser Reihenfolge. Erste Frage: „Für wen genau sollen wir tätig werden, für Sie persönlich oder für die Gesellschaft, und in welcher Funktion schreiben Sie uns?“ Zweite Frage: „Was soll am Ende erreicht sein, eine erste Einschätzung, eine Beratung oder die Vertretung gegenüber der Gegenseite oder vor Gericht?“ Dritte Frage: „Gibt es ein Schreiben, einen Bescheid, eine Kündigung oder ein Urteil mit Datum des Zugangs, und wann ist es bei Ihnen eingegangen?“ Vierte Frage: „Wer zahlt die Kosten, und darf diese Person oder Stelle Informationen über das Mandat erhalten?“ Fünfte Frage: „Haben Sie uns ausschließlich per E-Mail, Telefon oder über unser Online-Formular beauftragt, und handeln Sie als Privatperson oder für Ihr Unternehmen?“ Sechste Frage: „Welche weiteren Personen oder Unternehmen sind an der Sache beteiligt, auch auf Ihrer Seite?“

Ohne Antwort auf die erste und zweite Frage wird kein Annahmeschreiben versandfertig gestellt; vorbereitet werden Konfliktsuche mit den bekannten Namen, Chronologie und ein Entwurf mit Platzhaltern. Ohne Antwort auf die dritte Frage wird die mögliche Frist als ungeprüft gekennzeichnet und sofort als Fristobjekt im Zustand „erfasst“ an den Fristenskill übergeben. Ohne Antwort auf die vierte bis sechste Frage werden Vertrag, Belehrung und Prüfnotiz vorbereitet und die betroffenen Stellen als offen markiert.

## 3. Ablauf und Checkliste

### 3.1. Dringlichkeit vor Verwaltungsroutine

Prüfe sofort, ob eine Frist heute, in den nächsten Tagen oder möglicherweise bereits abgelaufen ist. Sichere das fristauslösende Dokument mit Zugangsdatum, lege das Fristobjekt im Zustand „erfasst“ an und übergib die Berechnung an den Fristenskill. Die Aufnahme darf nicht dazu führen, dass niemand eine bekannte Kündigungsschutz- oder Rechtsmittelfrist beachtet; zugleich wird keine Übernahme der Fristverantwortung behauptet, solange Auftrag und Annahme fehlen.

Bei offenem Konflikt und dringender Frist prüfe, welche interne Arbeit ohne verbotene Beratung möglich ist, etwa Chronologie und Hinweis auf anderweitige Vertretung. Zeitdruck beseitigt kein persönliches Tätigkeitsverbot.

[§ 44 BRAO](https://www.gesetze-im-internet.de/brao/__44.html) verlangt, dass der Rechtsanwalt, der einen Auftrag nicht annehmen will, die Ablehnung unverzüglich erklärt, und verpflichtet bei schuldhafter Verzögerung dieser Erklärung zum Ersatz des daraus entstehenden Schadens. Vermeide deshalb „Wir melden uns“, wenn die Kanzlei bereits weiß, dass sie nicht übernimmt. Die Eingangsbestätigung erklärt zutreffend, ob nur die Prüfung einer Übernahme oder bereits die Sachbearbeitung erfolgt.

### 3.2. Mandantenidentität und Interessenrichtung

Beschreibe das Mandatsziel in einem vollständigen Satz und ordne es einem bestimmten Rechtsträger zu. „Die Gesellschaft verlangt Ersatz eines Schadens von ihrem Geschäftsführer“ ist eine andere Interessenrichtung als „Der Geschäftsführer wehrt persönliche Ansprüche ab“. Die Annahme wird nicht auf eine unbestimmte „Unternehmensgruppe“ erstreckt, wenn nur eine Gesellschaft beraten wird.

Prüfe, ob mehrere Personen gemeinsam Mandanten werden sollen. Wenn ja, bestimme gemeinsamen Gegenstand, Kommunikationsregeln, Kostentragung und Umgang mit späteren Interessengegensätzen. Eine Vereinbarung über gemeinsame Information heilt keine von Anfang an bestehende persönliche Kollision. Erfasse mögliche Innenansprüche: Käufer und Verkäufer, Gesellschaft und Organ oder mehrere Erben können dasselbe äußere Ziel verfolgen und intern gegensätzliche Haftungs- oder Verteilungsinteressen haben. Die Prüfung fragt deshalb auch, ob eine sachgerechte Empfehlung an einen Beteiligten einen anderen belasten müsste.

### 3.3. Suchstrategie im Konfliktbestand

Nutze den tatsächlich verfügbaren Kanzleibestand und dokumentiere Suchdatum, Systeme, Suchbegriffe und Einschränkungen. Suche nach genauen Namen, Varianten, früheren Firmenbezeichnungen und sicheren Identifikatoren; bei relevanten Trefferketten werden verbundene Akten geöffnet, soweit Berechtigung und Prüfzweck dies erlauben.

Unterscheide falsch positive Treffer, wirtschaftliche Beziehungen ohne dieselbe Rechtssache und konkrete Vorbefassung. Eine frühere Beratung eines Unternehmens in einer unabhängigen Mietangelegenheit verbietet nicht zwangsläufig ein späteres Mandat gegen dasselbe Unternehmen in einem anderen Lebenssachverhalt; vertrauliches Wissen bleibt dennoch zu prüfen. Fehlt ein Systemzugang, dokumentiere genau, welcher Teilbestand ungeprüft ist. Die Formulierung „keine Treffer im verfügbaren Bestand“ ist zulässig, wenn sie nicht als „keine Kollision möglich“ missverstanden wird.

### 3.4. Dieselbe Rechtssache

Ordne den neuen und den früheren Auftrag ihrem tatsächlichen rechtlichen Zusammenhang zu. Entscheidend sind nicht nur Aktenzeichen, Vertragsdatum oder Gerichtsverfahren; Gestaltung, Durchführung und spätere Streitigkeit über denselben Vertrag können zusammenhängen. Eine frühere gemeinsame Scheidungsfolgenberatung und eine spätere einseitige Durchsetzung einzelner dort geregelter Rechte verlangen genaue Prüfung des damaligen Beratungsgegenstands und der damals offengelegten Interessen. Erstelle bei schwierigen Fällen eine kurze Vergleichsmatrix aus Gegenstand, Ziel, Beteiligten, betroffenen Rechtspositionen und vertraulichem Wissen. „Dieselbe Rechtssache“ wird nicht allein anhand wirtschaftlicher Nähe bejaht; ebenso wenig beseitigt eine neue Anspruchsgrundlage den Zusammenhang.

### 3.5. Widerstreitende Interessen

Prüfe die tatsächliche Interessenlage, nicht nur abstrakte Konfliktmöglichkeiten. Frage: Welche rechtlich sinnvolle Empfehlung müsste der Anwalt jedem Beteiligten geben? Welche Tatsachen dürfte er für den einen nutzen, dem anderen aber nicht offenbaren? Besteht bereits ein Widerspruch zwischen Verteidigung, Aufklärung, Regress und Vergleichsziel?

Das persönliche Tätigkeitsverbot nach [§ 43a Absatz 4 Satz 1 BRAO](https://www.gesetze-im-internet.de/brao/__43a.html) knüpft an dieselbe Rechtssache, eine frühere Beratung oder Vertretung einer anderen Partei und das widerstreitende Interesse an; § 3 Absatz 1 BORA wiederholt dieses Verbot auf Satzungsebene. Es lässt sich nicht durch Zustimmung aufheben. Wenn der Konflikt bereits besteht, ist ein engerer Auftrag nur dann eine Lösung, wenn er den verbotenen Gegenstand tatsächlich ausschließt und die verbleibende Beratung fachlich sinnvoll ist. Eine Umbenennung in „neutrale Moderation“ genügt nicht.

### 3.6. Kanzleizurechnung und Ausnahme

Ermittle, ob ein persönliches Verbot auf andere gemeinschaftlich tätige Anwälte erstreckt wird. § 43a Absatz 4 Sätze 2 und 3 BRAO regeln die Zurechnung und ihr Fortbestehen nach Ausscheiden. Die Ausnahme nach Satz 4 setzt die umfassende Information der betroffenen Mandanten, deren Zustimmung in Textform und geeignete Vorkehrungen zur Wahrung der Verschwiegenheit voraus. Für die Berufsausübungsgesellschaft ist Satz 5 zusätzlich zu prüfen; Satz 6 erlaubt die zur Kollisionsprüfung erforderliche Offenbarung, nicht mehr. § 3 Absatz 4 BORA verlangt daneben, die Einhaltung der Vorkehrungen zum jeweiligen Mandat zu dokumentieren. Beschreibe die Vorkehrungen tatsächlich: getrennte Zugriffsgruppen, Ausschluss aus Besprechungen, keine gegenseitige Vertretung in der Sache, gesonderte Dateiablage, begrenzte Suchindizes und Kontrolle von KI-Wissensbeständen. Eine Sperre nur für den sichtbaren Ordner hilft nicht, wenn eine globale Suche Zusammenfassungen liefert; verantwortliche Person und Überprüfung der Sperre werden festgelegt.

Die umfassende Information darf nicht selbst fremde Geheimnisse offenlegen. Ist eine informierte Zustimmung ohne unzulässige Offenbarung nicht möglich, darf der Mangel nicht durch eine inhaltsleere Verzichtsklausel kaschiert werden. Die Mandantenentscheidung wird ohne Fristdruck dokumentiert.

### 3.7. Sozietätswechsel, frühere Funktionen und § 45 BRAO

Bei Zugang eines Berufsträgers prüfe relevante frühere Mandate vor Bearbeitungsbeginn und erhebe nur die für die Kollision erforderlichen Daten. Das frühere Arbeitgeberverhältnis allein ist weder ein persönlicher Konflikt in jeder dort bearbeiteten Sache noch bedeutungslos.

Referendartätigkeit und frühere Tätigkeiten außerhalb des Anwaltsberufs sind nach den auf Absatz 4 folgenden Absätzen des § 43a BRAO zu prüfen (Absatz 5 für die Referendartätigkeit, Absatz 6 für berufliches Tätigwerden außerhalb des Anwaltsberufs). [§ 45 BRAO](https://www.gesetze-im-internet.de/brao/__45.html) enthält eigenständige Tätigkeitsverbote für denjenigen, der in derselben Rechtssache bereits als Richter, Schiedsrichter, Staatsanwalt, Angehöriger des öffentlichen Dienstes oder Notar tätig war, sowie für bestimmte Verwalter- und Vermögensbetreuungsfunktionen; Absatz 1 Nummer 1 Buchstabe a erfasst Richter, Staatsanwälte und Angehörige des öffentlichen Dienstes, Buchstabe b Schiedsrichter, Schlichter und Mediatoren, Buchstabe c Notare, Notarvertreter, Notariatsverwalter und Notarassessoren, Nummer 2 das Vorgehen gegen den Träger eines zuvor als Insolvenzverwalter, Nachlassverwalter, Testamentsvollstrecker, Betreuer oder ähnlich verwalteten Vermögens und Nummer 3 die außeranwaltliche Tätigkeit für eine andere Partei im widerstreitenden Interesse; Absatz 2 erstreckt Verbote auf gemeinschaftlich Tätige und enthält Ausnahmen für bestimmte Referendar- und wissenschaftliche Mitarbeitertätigkeiten. Absatz 3 lässt die Erstreckung fortbestehen; seine Ausnahme mit umfassender Information, Zustimmung in Textform und Geheimnisschutz gilt nur bei Vorbefassung nach Absatz 1 Nummer 3, nicht für sämtliche Verbote. Der Skill fragt deshalb nicht nur „Haben Sie diese Partei schon beraten?“, sondern erhebt die konkrete frühere Rolle, etwa Schiedsrichter, Mediator, Insolvenzverwalter, Testamentsvollstrecker oder Beamter.

Bei Ausscheiden eines Partners wird der Mandantenwille eingeholt und der rechtliche Übergang bestimmt; eine interne Einigung zwischen Kanzleien ersetzt keine Vertragsübernahme durch den Mandanten. Kündigung und Neuauftrag, Vertragsübernahme und Wechsel des Sachbearbeiters sind verschiedene Wege; der BGH-Anker vom 15.01.2026 wird mit seinen tatsächlichen Voraussetzungen herangezogen. Fristen, Vollmacht und Herausgabe werden unabhängig vom Streit zwischen Berufsträgern gesichert.

### 3.8. Unabhängigkeit und problematische Weisungen

Prüfe § 43a Absatz 1 BRAO, wenn Auftrag, Finanzierung oder Beteiligung die freie Interessenwahrnehmung gefährden. Ein Drittzahler darf nicht heimlich die Strategie bestimmen, während der Mandant nur unterschreibt; ein Vorteil für die Vermittlung von Aufträgen ist nach § 49b Absatz 3 BRAO verboten. Verlangt der Interessent falsche Tatsachen, rückdatierte Dokumente oder eine verdeckte Zahlung, werden rechtliche Grenzen und zulässige Alternativen erläutert. Ein schwieriger oder beschuldigter Mandant ist dadurch nicht von Beratung ausgeschlossen; entscheidend ist die verlangte Tätigkeit. Bei eigener Beteiligung der Kanzlei oder möglicher Haftung der bisherigen Kanzlei in einer übernommenen Sache benennt der Annahmevermerk eine unabhängige Beratung zu diesem Teilgegenstand.

### 3.9. Leistungsfähigkeit und Auftragsbegrenzung

Prüfe Fachkenntnis, Zeit, Sprache, Technik, Vertretungsberechtigung und Versicherung; eine deutsche Zulassung berechtigt nicht zur Vertretung vor jedem ausländischen Gericht, und ein Versicherungsvertrag kann Auslandsbezüge ausschließen. Ein begrenzter Auftrag beschreibt positiv, was geleistet wird, und konkret, was außerhalb liegt: „Wir prüfen den vorgelegten Vertrag nach deutschem Recht hinsichtlich Haftung, Vergütung und Kündigung; eine steuerliche Beurteilung und die Prüfung ausländischer Register erfolgen nicht.“ Hinweise auf naheliegende erhebliche Risiken bleiben trotz Begrenzung erforderlich.

### 3.10. Vollmacht, Vertretung und Prozessvollmacht

Mandatsvertrag und Vollmacht sind getrennte Gegenstände. Der Mandatsvertrag ist das Innenverhältnis; die Vollmacht ist nach [§ 167 BGB](https://www.gesetze-im-internet.de/bgb/__167.html) die durch Erklärung erteilte Vertretungsmacht, deren Wirkung [§ 164 BGB](https://www.gesetze-im-internet.de/bgb/__164.html) bestimmt. Eine weit formulierte Vollmacht erweitert nicht den intern erteilten Auftrag; umgekehrt kann ein Auftrag bestehen, während die Vertretungsbefugnis noch nicht nachgewiesen ist. Schließt jemand ohne tatsächlich bestehende Vertretungsmacht einen Vertrag, hängt die Wirksamkeit nach § 177 BGB von der Genehmigung ab, und der Handelnde kann nach § 179 BGB selbst haften (§ 177 Absatz 1 BGB; nach § 179 Absatz 1 BGB nach Wahl des anderen Teils auf Erfüllung oder Schadensersatz, bei Unkenntnis des Mangels nach Absatz 2 nur auf den Vertrauensschaden, ausgeschlossen nach Absatz 3 bei Kenntnis oder Kennenmüssen des anderen Teils sowie grundsätzlich bei beschränkter Geschäftsfähigkeit des Vertreters ohne Zustimmung seines gesetzlichen Vertreters). Die Akte hält Auftraggeber, Vertreter, Vertretungsgrundlage und Nachweis getrennt fest.

Im Zivilprozess ist die Prozessvollmacht nach [§ 80 ZPO](https://www.gesetze-im-internet.de/zpo/__80.html) schriftlich zu den Gerichtsakten einzureichen und kann nachgereicht werden; ihr gesetzlicher Umfang nach § 81 ZPO umfasst alle Prozesshandlungen einschließlich Vergleich, Verzicht und Anerkenntnis, eine Beschränkung wirkt nach außen nur in den Grenzen des § 83 ZPO, und nach § 88 ZPO wird der Mangel bei einem auftretenden Rechtsanwalt nur auf Rüge geprüft (§ 81, § 83 Absatz 1, § 88 Absatz 2 ZPO). Die interne Auftragsbegrenzung, etwa „kein Vergleichsabschluss ohne Rücksprache“, gehört deshalb in den Mandatsvertrag und die Aktenanweisung.

Ein Auftrag zur erstinstanzlichen Vertretung umfasst nicht selbstverständlich eine Rechtsmittelbegründung; eine Rechtsschutzdeckung für ein Rechtsmittel ist keine Mandantenerklärung zur Einlegung. Bei Mandatswechsel wirkt die Kündigung der Vollmacht gegenüber dem Gegner nach [§ 87 ZPO](https://www.gesetze-im-internet.de/zpo/__87.html) erst mit der Anzeige des Erlöschens, im Anwaltsprozess erst mit der Anzeige der Bestellung eines anderen Anwalts. Gericht, Gegner und bisherige Vertretung werden nur im entsprechenden Auftrag informiert; der neue Auftrag erhält einen klaren Beginn und eine Übergabe der Restfristen.

### 3.11. Verbrauchermandat im Fernabsatz

Prüfe Verbraucherstatus, entgeltliche Dienstleistung und ausschließliche Fernkommunikation bei Verhandlung und Abschluss nach [§ 312c BGB](https://www.gesetze-im-internet.de/bgb/__312c.html). Die Norm nimmt nur den Vertragsschluss aus, der nicht im Rahmen eines für den Fernabsatz organisierten Vertriebs- oder Dienstleistungssystems erfolgt; die Kanzlei trägt dafür die Darlegung. Telefon und E-Mail allein begründen kein solches System, ein standardisierter bundesweiter digitaler Aufnahmeprozess liefert aber gewichtige Indizien; eine Klausel „kein Fernabsatz“ entscheidet nichts.

Liegt ein Fernabsatzvertrag vor, steht dem Verbraucher nach [§ 312g Absatz 1 BGB](https://www.gesetze-im-internet.de/bgb/__312g.html) das Widerrufsrecht nach [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html) zu; die Widerrufsfrist beträgt nach § 355 Absatz 2 BGB vierzehn Tage und beginnt bei Dienstleistungen nicht vor ordnungsgemäßer Belehrung, mit einer absoluten Höchstgrenze von zwölf Monaten und vierzehn Tagen nach [§ 356 Absatz 4 Satz 1 BGB](https://www.gesetze-im-internet.de/bgb/__356.html). Das Erlöschen bei einer entgeltlichen Dienstleistung regelt § 356 Absatz 5 Nummer 2 BGB: Es setzt die vollständige Erbringung, die vorherige ausdrückliche Zustimmung des Verbrauchers zum Beginn vor Fristablauf und seine Bestätigung der Kenntnis voraus, dass er mit vollständiger Vertragserfüllung sein Widerrufsrecht verliert; bei außerhalb von Geschäftsräumen geschlossenen Verträgen ist die Zustimmung zusätzlich auf einem dauerhaften Datenträger zu übermitteln. Der erste Telefontermin oder der Beginn der Aktenprüfung beendet das Widerrufsrecht nicht.

Der Wertersatz für die bis zum Widerruf erbrachte Leistung setzt nach § 357a BGB voraus, dass der Verbraucher ausdrücklich verlangt hat, dass vor Ablauf der Widerrufsfrist begonnen wird (§ 357a Absatz 2 BGB; bei Außergeschäftsraumverträgen muss das Verlangen auf einem dauerhaften Datenträger übermittelt sein, und der Unternehmer muss nach Artikel 246a § 1 Absatz 2 Satz 1 Nummer 1 und 3 EGBGB ordnungsgemäß informiert haben). Wunsch nach sofortiger Tätigkeit, ordnungsgemäße Information und erbrachte Leistung sind zu belegen. Ein Formular, das pauschal jeden Widerruf ausschließt, wird nicht verwendet; der Mandant erhält eine verständliche Erklärung des Verhältnisses zwischen sofortiger Arbeit, Widerruf und Vergütungsfolgen.

Bei Vertragsschluss über eine Online-Benutzeroberfläche wird die elektronische Widerrufsfunktion nach [§ 356a BGB](https://www.gesetze-im-internet.de/bgb/__356a.html) geprüft: während der Widerrufsfrist ständig verfügbar, hervorgehoben und leicht zugänglich; die Funktion heißt „Vertrag widerrufen“ oder gleich eindeutig. Sie erlaubt Angaben zu Name, Vertrag und elektronischem Bestätigungsweg, danach die Bestätigung „Widerruf bestätigen“. Unverzüglich folgt auf dauerhaftem Datenträger die Bestätigung mit Inhalt, Datum und Uhrzeit; Absatz 5 regelt den fristwahrenden Zugang bei rechtzeitiger Absendung. Eine PDF-Belehrung ersetzt die technische Funktion nicht; nicht jede E-Mail-Annahme verpflichtet zum Aufbau eines Mandatsportals. Der Skill erstellt Text und Anforderungen, behauptet aber keine nicht implementierte Funktion.

### 3.12. Informationspflichten und berufsrechtliche Belehrungen

Vor Übernahme eines Auftrags, der nach Gegenstandswert abgerechnet wird, ist nach [§ 49b Absatz 5 BRAO](https://www.gesetze-im-internet.de/brao/__49b.html) darauf hinzuweisen, dass sich die Gebühren nach dem Gegenstandswert richten. Der Hinweis gehört in das Annahmeschreiben und wird mit Datum dokumentiert; ein Hinweis erst in der ersten Rechnung ist kein Hinweis vor Übernahme.

Die [DL-InfoV](https://www.gesetze-im-internet.de/dlinfov/__2.html) verlangt vor Abschluss eines schriftlichen Vertrags, andernfalls vor Erbringung der Dienstleistung die in ihrem § 2 genannten Angaben, darunter Name, Anschrift, Kontaktdaten, Kammer, gesetzliche Berufsbezeichnung und Verleihungsstaat sowie Angaben zur Berufshaftpflichtversicherung mit Name und Anschrift des Versicherers und räumlichem Geltungsbereich; der Verweis auf die berufsrechtlichen Regelungen und ihre Zugänglichkeit ist nach § 3 Absatz 1 Nummer 1 DL-InfoV auf Anfrage zu geben; nach § 4 Absatz 1 Nummer 2 DL-InfoV ist bei nicht im Voraus festgelegtem Preis auf Anfrage der Preis, die Einzelheiten seiner Berechnung oder ein Kostenvoranschlag mitzuteilen, wobei diese Pflicht nach § 4 Absatz 2 DL-InfoV nicht gegenüber Verbrauchern gilt. Diese Angaben werden standardisiert mitgeliefert. Bei Verbraucherverträgen im Fernabsatz kommen die Informationspflichten nach § 312d BGB in Verbindung mit Artikel 246a EGBGB und die gesetzliche Musterbelehrung hinzu.

Berufsrechtlich belehrt wird außerdem über externe Dienstleister und KI-Werkzeuge nach § 43e BRAO und § 203 StGB, soweit ein Geheimniszugang Dritter erforderlich wird; eine Einwilligung in E-Mail-Kommunikation deckt keinen Upload der gesamten Akte in einen fremden KI-Dienst.

### 3.13. Honoraraufnahme und Kostentransparenz

Kläre die Vergütungsgrundlage vor einer missverständlichen Leistungszusage. Möglich sind RVG, Stundenhonorar, Festpreis, verbindliche Preiszusage oder Schätzung mit oder ohne Deckel. Nach [§ 49b Absatz 1 BRAO](https://www.gesetze-im-internet.de/brao/__49b.html) dürfen geringere Gebühren und Auslagen als nach dem RVG nur vereinbart oder gefordert werden, soweit das RVG dies zulässt; Absatz 2 lässt ein Erfolgshonorar nur in den Fällen des [§ 4a RVG](https://www.gesetze-im-internet.de/rvg/__4a.html) zu, nämlich bei einer Geldforderung von höchstens 2.000 Euro, vorbehaltlich der Ausnahme für unpfändbare Forderungen in § 4a Absatz 1 Satz 2, bei Inkassodienstleistungen außergerichtlich oder in den in § 79 Absatz 2 Satz 2 Nummer 4 ZPO genannten Verfahren oder wenn der Auftraggeber im Einzelfall bei verständiger Betrachtung ohne Erfolgshonorar von der Rechtsverfolgung abgehalten würde. Für Vereinbarungen nach § 34 RVG gelten die Formvorgaben des § 3a Absatz 1 Sätze 1 und 2 nicht; die Kanzlei dokumentiert sie dennoch aus Beweisgründen. Eine sonstige Vergütungsvereinbarung nach [§ 3a RVG](https://www.gesetze-im-internet.de/rvg/__3a.html) bedarf der Textform, muss als solche bezeichnet, von anderen Vereinbarungen deutlich abgesetzt und darf nicht in der Vollmacht enthalten sein; sie enthält den Hinweis auf die begrenzte Kostenerstattung. Bei Beratung gelten die Verbrauchergrenzen des [§ 34 RVG](https://www.gesetze-im-internet.de/rvg/__34.html) von 190 Euro für ein erstes Beratungsgespräch und 250 Euro für die Beratung ohne Vergütungsvereinbarung.

Nach dem BGH-Anker vom 19.02.2026 muss auch der Anwendungsbereich der Vergütungsabrede in Textform erkennbar sein; eine später hinzukommende Angelegenheit wird nicht stillschweigend unter einen früheren Stundensatz gezogen. Die mögliche Erstattung durch Gegner oder Staatskasse wird von der eigenen Zahlungspflicht getrennt. Die Verhandlung im Einzelnen übernimmt der Honorarskill.

### 3.14. Geldwäsche, Datenverarbeitung und Konfliktregister

Prüfe anhand der tatsächlichen Tätigkeit, ob § 2 Absatz 1 Nummer 10 GwG eröffnet ist. Eine gewöhnliche Lohnforderung löst nicht allein wegen anwaltlicher Bearbeitung GwG-Pflichten aus; Immobilien-, Gesellschafts-, Vermögens- und bestimmte Steuerberatungsmandate können im Katalog liegen. Die Anwendungsentscheidung wird dokumentiert und bei Auftragserweiterung erneuert; bei eröffnetem Anwendungsbereich leite Identifizierung, wirtschaftlich Berechtigte und Risiko an [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md). Eine Aufnahmebestätigung darf keine beabsichtigte Verdachtsmeldung offenlegen.

Kläre, welche Ansprechpartner innerhalb eines Unternehmens Informationen erhalten dürfen; ein Verteiler „Rechtsabteilung“ kann Personen enthalten, die bei Organhaftung nicht berechtigt sind. Speichere im Konfliktregister nur die erforderlichen Identifikations- und Gegenstandsdaten und kennzeichne vertrauliche Konfliktdetails getrennt vom allgemeinen Mandatsstamm. Eine Absage beseitigt nicht jede berechtigte Aufbewahrung von Konfliktdaten; Werbemails an abgelehnte Interessenten benötigen eine eigene Grundlage.

### 3.15. Annahme, Bedingung oder Absage formulieren

Triff eine klare Entscheidung mit konkretem Beginn. Bei Annahme benennt das Schreiben Mandant, Gegenstand, Ziel, Umfang, Ansprechpartner, erste Schritte, Fristen und Vergütungsgrundlage; offene Unterlagen werden gezielt angefordert. Der Text darf nicht „Wir übernehmen“ sagen und an anderer Stelle jede Verantwortung bis zu einem unbestimmten Zeitpunkt ausschließen.

Bei ausstehender Konfliktprüfung bestätige nur die Prüfung der Übernahme und erläutere die bekannte Fristlage; eine unklare „vorläufige Annahme“ wird vermieden. Bei Absage nenne den Grund in angemessenem Umfang; eine Kollision kann mitgeteilt werden, ohne frühere Mandanten oder vertrauliche Inhalte offenzulegen. Die Weitergabe an eine andere Kanzlei erfolgt nur bei Auftrag und tragfähiger Offenbarungsgrundlage.

### 3.16. Nachträglicher Konflikt und Auftragserweiterung

Wiederhole die Prüfung anlassbezogen bei neuen Parteien, Anspruchswechsel, Widerklage, Organwechsel, neuen Tatsachen oder Kanzleizugang; eine abgeschlossene Erstprüfung ist keine lebenslange Freigabe. Wer erkennt, dass er entgegen § 43a Absatz 4 bis 6 BRAO tätig ist, hat nach § 3 Absatz 2 BORA in der Fassung vom 01.12.2025 unverzüglich die Mandantschaft zu informieren und alle Mandate in derselben Rechtssache zu beenden. Stoppe deshalb die betroffene Sacharbeit, prüfe die erforderliche Niederlegung und sichere zulässige Übergangshandlungen. Die Mitteilung muss Fristen und alternative Vertretung ermöglichen, ohne fremde Geheimnisse preiszugeben. Die Auswahl des wirtschaftlich wichtigeren Mandanten ist kein gesetzlicher Lösungsmechanismus.

Eine Auftragserweiterung wird hinsichtlich Fachkunde, Honorar, GwG, Fristen und Datenzugriff geprüft; nicht jede Ergänzung ist ein neues Mandat. Der Skill formuliert einen kurzen, vollständigen Nachtrag, wenn er erforderlich ist.

### 3.17. Honorar- und Zeitanschluss

Verwende die [Arbeitsweise](../../references/arbeitsweise.md): gespeicherte Grundlage knapp vorhalten, bei Änderung gezielt klären und bestätigte Angaben übernehmen. Nach tatsächlicher Leistung erfasse Datum, wirkliche Dauer, Abrechenbarkeit und sachliches Narrativ. Konfliktprüfung, Erstgespräch und Mandatsverwaltung sind nicht in jedem Modell gesondert abrechenbar.

Keine erfundenen Stunden, keine hypothetische KI-Ersparnis als Arbeitszeit und keine stillschweigende Deckelerhöhung. Speichere den bestätigten Zeitstand (bestätigte Minuten, offene Zeitfragen) im tatsächlichen Mandatsordner und aktualisiere den RechnungsENTWURF. Wird das Mandat abgelehnt, prüfe eine etwaige bereits entstandene Vergütung gesondert und behaupte keine Zahlungspflicht allein wegen interner Aktenanlage.

### 3.18. Agentischer Lauf und Freigabestufe

Dieser Skill verantwortet die Phase `annahme` des [Mandatslaufs](../../references/mandatslauf-und-freigaben.md); sie endet mit dem Produkt Annahme, begrenzte Beauftragung oder Absage. Bei einem nachträglichen Konflikt oder einer Auftragserweiterung in einer laufenden Akte setzt er `annahme` als Nebenlauf neben die laufende Sacharbeit (`phase --nebenlauf`). Fehlt der vom Hauptskill in der Phase `eingang` angelegte Lauf, legt dieser Skill ihn mit `init` und der von der Kanzlei bestimmten Stufe an.

Auf Stufe 0 liefert er Schreiben und Konfliktprüfnotiz als Text, ohne eine Datei zu schreiben. Auf Stufe 1 legt er `01_Bearbeitung/Annahmeschreiben_v01.docx` und `01_Bearbeitung/Konfliktpruefnotiz_v01.md` an, führt das Dokumentregister und kopiert das fristauslösende Dokument unverändert. Auf Stufe 2 schreibt er Phase, Produkt und Gate mit [mandatslauf.py](../../scripts/mandatslauf.py) in den Mandatslauf, erfasst das Fristobjekt im Zustand „erfasst“, notiert offene Fragen mit `question` und bucht bestätigte Minuten der Konfliktprüfung im Journal. Auf Stufe 3 erstellt er den Übergabevermerk und stößt [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md), [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) und bei eröffnetem Anwendungsbereich [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md) ohne Rückfrage an. Auf keiner Stufe versendet er das Schreiben, behauptet eine unbelegte Vollmacht oder gibt ein Gate selbst frei. `geprueft` setzt eine dokumentierte fachliche Prüfung voraus; `freigegeben` erfordert die persönliche Freigabe der unveränderten geprüften Fassung.

Er öffnet Gate G1 Annahme mit dem Annahme-, Begrenzungs- oder Absageschreiben als Bezug. Freigeben kann nur der verantwortliche Berufsträger namentlich, nachdem Konfliktprüfnotiz und Honorarstand vorliegen; Annahmedatum und Text werden vor der Freigabe abschließend geprüft; danach wird der Hash unverändert im Mandatsstamm dokumentiert. Jede Textänderung verlangt neue Prüfung und Freigabe. Der Versand des Schreibens bleibt Gate G3 Versand und Einreichung; der Versandbeleg wird dort nachgetragen. Bei einem Portalmandat, in dem Anfrage, Identitätsprüfung oder Widerrufsfunktion über einen externen Dienst laufen, öffnet er zusätzlich Gate G6 Dienstleister und übergibt die Prüfung nach § 43e BRAO an [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md).

Im Produktregister trägt er `annahme` (Schreiben) und `berufsrechtsvermerk` (Prüfnotiz) jeweils im Zustand `entwurf` ein; nach der Freigabe von G1 stößt er [Akte und Fristen anlegen](../akte-fristen-anlegen/SKILL.md) ohne Rückfrage an. Beispiel auf Stufe 2:

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/M-26-131" --phase annahme --grund "Anfrage Lindqvist vom 05.10.2026, Konfliktsuche ohne Treffer"
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/M-26-131" --id annahme --pfad "01_Bearbeitung/Annahmeschreiben_v01.docx" --skill mandatsannahme-interessenkollision --zustand entwurf
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-26-131" --gate G1 --aktion oeffnen --person "[zuständige Rechtsanwältin oder zuständiger Rechtsanwalt]" --bezug annahme
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/M-26-131"
```

Stoppregel: Der Skill bleibt stehen, solange Rechtsträger des Mandanten oder Auftragsumfang unbeantwortet sind, solange ein erinnerter Treffer bei unzugänglichem Register ungeklärt ist, und an Gate G1 selbst.

### 3.19. Typische Fehler und Gegenkontrolle

| Fehler | Woran erkennbar | Gegenkontrolle |
|---|---|---|
| Gesellschaft statt Organ als Mandantin angelegt | Anspruch richtet sich persönlich gegen den Geschäftsführer | Mandatsziel in einem Satz mit Rechtsträger formulieren |
| Namenssuche als vollständige Kollisionsprüfung | Prüfnotiz nennt nur Trefferzahl | Rechtssache und Interessenrichtung je Treffer bewerten |
| „Keine Treffer“ bei ausgefallenem Register | Suchprotokoll ohne Systemangabe | Ungeprüften Teilbestand ausdrücklich benennen |
| Zustimmung heilt persönliches Verbot | Verzichtsklausel für den vorbefassten Anwalt | Satz 1 und Sätze 2 bis 4 des § 43a Absatz 4 BRAO trennen |
| Ablehnung aufgeschoben | Antwort „Wir melden uns“ trotz feststehender Absage | § 44 BRAO: Ablehnung unverzüglich erklären |
| Vollmacht als Auftrag gelesen | Weite Formularvollmacht, kein Mandatsvertrag | Innen- und Außenverhältnis getrennt dokumentieren |
| Arbeitsbeginn als Ende des Widerrufsrechts | Formular „Widerruf ausgeschlossen bei Beginn“ | Erlöschensvoraussetzungen des § 356 BGB vollständig prüfen |
| Gegenstandswerthinweis erst in der Rechnung | Annahmeschreiben ohne § 49b Absatz 5 BRAO | Hinweis vor Übernahme datieren |
| Honorarabrede in der Vollmacht | Vollmachtsformular mit Stundensatz | § 3a RVG: getrennte, bezeichnete Vereinbarung |
| Deckungszusage als Vergütungsvertrag | Kostenfrage mit „RSV übernimmt“ beantwortet | Zahlungspflicht des Mandanten gesondert erklären |
| Konzern als Geheimnisverzicht | Mutter verlangt alle Protokolle | Informationsregel durch die Mandantin selbst festlegen |
| Frist in der Aufnahme „nebenbei“ berechnet | Datum ohne Rechenvermerk im Annahmebrief | Fristenskill mit Dokument und Zugangsdatum anstoßen |

### 3.20. Übergabe an Nachbarskills

Jede Übergabe nennt die führende Fassung (Pfad und Hash) von Schreiben und Konfliktprüfnotiz, den Honorarstand (Modell, Satz/Betrag, Umfang, Deckel, netto/brutto), den Zeitstand (bestätigte Minuten, offene Zeitfragen), die offenen Gates und die offenen Fragen; der Nachbarskill beginnt mit diesem Stand, nicht mit einer erneuten Mandatsaufnahme. An [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md) geht das Fristobjekt im Zustand „erfasst“ mit fristauslösendem Dokument, belegtem Zugangsdatum und der Angabe, ob die Kanzlei bereits beauftragt ist; zurück kommt das Fristobjekt im Zustand „berechnet“ mit Rechenvermerk für das Annahmeschreiben, und erst der Kalender macht es „eingetragen“. An [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) gehen Auftragsumfang, Mandantentyp und gewünschtes Modell; zurück kommt der bestätigte Honorarstand mit der Vergütungsvereinbarung in Textform und ihrem Anwendungsbereich. An [Geldwäsche prüfen](../geldwaesche-pruefen/SKILL.md) geht die Anwendungsentscheidung mit Tätigkeitsbeschreibung; zurück kommt der Prüfvermerk mit Identifizierungsstand. An [Anwaltsberufsrecht prüfen](../anwaltsberufsrecht-pruefen/SKILL.md) geht eine ungeklärte Rechtsfrage zu § 45 BRAO oder zur Berufsausübungsgesellschaft; zurück kommt die begründete Entscheidung. An [Akte und Fristen anlegen](../akte-fristen-anlegen/SKILL.md) gehen nach Freigabe von G1 Mandatsstamm, Konfliktvermerk, Auftrag, Vollmacht, Honorarstand und offene Nachweise mit Annahmedatum; zurück kommt das Aktenzeichen mit zuständiger Person. Der Zeitstand läuft über [Zeiten erfassen](../zeiten-erfassen/SKILL.md).

## 4. Quellenpflicht

### 4.1. Normen und Prüfstand

Prüfstand ist der 8. Oktober 2026. Tragende amtliche Normlinks sind [§ 43a BRAO](https://www.gesetze-im-internet.de/brao/__43a.html), [§ 44 BRAO](https://www.gesetze-im-internet.de/brao/__44.html), [§ 45 BRAO](https://www.gesetze-im-internet.de/brao/__45.html), [§ 49b BRAO](https://www.gesetze-im-internet.de/brao/__49b.html), [§ 43e BRAO](https://www.gesetze-im-internet.de/brao/__43e.html), [§ 3a RVG](https://www.gesetze-im-internet.de/rvg/__3a.html), [§ 4a RVG](https://www.gesetze-im-internet.de/rvg/__4a.html), [§ 34 RVG](https://www.gesetze-im-internet.de/rvg/__34.html), [§ 164 BGB](https://www.gesetze-im-internet.de/bgb/__164.html), [§ 167 BGB](https://www.gesetze-im-internet.de/bgb/__167.html), [§ 312c BGB](https://www.gesetze-im-internet.de/bgb/__312c.html), [§ 312g BGB](https://www.gesetze-im-internet.de/bgb/__312g.html), [§ 355 BGB](https://www.gesetze-im-internet.de/bgb/__355.html), [§ 356 BGB](https://www.gesetze-im-internet.de/bgb/__356.html), [§ 356a BGB](https://www.gesetze-im-internet.de/bgb/__356a.html), [§ 80 ZPO](https://www.gesetze-im-internet.de/zpo/__80.html), [§ 87 ZPO](https://www.gesetze-im-internet.de/zpo/__87.html), [§ 2 DL-InfoV](https://www.gesetze-im-internet.de/dlinfov/__2.html) und [§ 2 GwG](https://www.gesetze-im-internet.de/gwg_2017/__2.html). Die BORA wird in der jeweils aktuellen, von der BRAK veröffentlichten Fassung herangezogen. Nutze außerdem [Rechtsquellen](../../references/rechtsquellen.md) und [Zitierweise](../../references/zitierweise.md). Prüfe Übergangsrecht bei älteren Vertragsschlüssen ausdrücklich.

### 4.2. Entscheidungsanker mit Grenzen

BVerfG, Beschl. v. 03.07.2003 – Az. 1 BvR 238/01, Rn. 58–61, [amtlicher Volltext](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2003/07/rs20030703_1bvr023801.html). Trägt: Die damalige undifferenzierte Erstreckung des Tätigkeitsverbots beim Sozietätswechsel war unverhältnismäßig; konkrete Vorbefassung, Informationszugang und Schutzvorkehrungen sind maßgeblich. Trägt nicht: eine Befreiung von den heutigen Voraussetzungen des § 43a Absatz 4 Sätze 2 bis 6 BRAO, insbesondere nicht von der Zustimmung in Textform.

BGH, Urt. v. 23.11.2017 – Az. IX ZR 204/16, Rn. 11–19, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2016/IX_ZR_204-16.pdf?__blob=publicationFile&v=1). Trägt: Anwaltsverträge können Fernabsatzverträge sein; bloße technische Erreichbarkeit über E-Mail und Telefon begründet noch kein organisiertes Fernabsatzsystem. Trägt nicht: eine Aussage zu den heutigen Widerrufsfolgen und zur aktuellen Absatzfolge des § 356 BGB, da die Entscheidung zu früherem Recht erging.

BGH, Urt. v. 19.11.2020 – Az. IX ZR 133/19, Rn. 12–19, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2019/IX_ZR_133-19.pdf?__blob=publicationFile&v=1). Trägt: Bei ausschließlich fernkommunikativem Vertragsschluss muss die Kanzlei das Fehlen eines organisierten Fernabsatzsystems darlegen und beweisen; bundesweite standardisierte Aufnahme und Werbung sind erhebliche Indizien. Trägt nicht: die Behauptung, jede einzelne E-Mail-Beauftragung beweise ein solches System.

BGH, Urt. v. 19.02.2026 – Az. IX ZR 226/22, Rn. 8–18, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1). Trägt: Auch der Anwendungsbereich einer Honorarabrede muss in Textform erkennbar sein; Vertragsauslegung geht der Formkontrolle voraus, und ein neuer Auftrag wird nicht allein durch ähnliche Aktenbezeichnung erfasst. Trägt nicht: eine allgemeine Unwirksamkeit von Zeithonorarvereinbarungen oder eine Pflicht, für jeden Arbeitsschritt eine neue Vereinbarung zu schließen.

BGH, Urt. v. 15.01.2026 – Az. IX ZR 188/24, Rn. 15–19, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2024/IX_ZR_188-24.pdf?__blob=publicationFile&v=1). Trägt: Der Mandatsübergang beim Ausscheiden eines Partners und die vollständige Handaktenherausgabe hängen an Vertragsübernahme und Mandantenentscheidung; der Mandant ist kein übertragbarer Kanzleibestand. Trägt nicht: einen allgemeinen Anspruch jedes ausscheidenden Berufsträgers auf beliebige Mandatsdaten oder eine Freigabe fremder Mandatsgeheimnisse.

### 4.3. Belegdisziplin

Fehlende Verifikation wird konkret benannt; keine Kommentarstellen, Parallelfundstellen oder Randnummern aus Modellwissen ergänzen. Die Aussagen zu §§ 177, 179 BGB, §§ 80, 81, 83, 88 ZPO, §§ 355, 356, 357a BGB, §§ 2 bis 4 DL-InfoV und § 3 BORA sind zum Prüfstand 08.10.2026 am Normtext abgeglichen. Eine plausible Kollisionshypothese wird nicht als gerichtliche Feststellung ausgegeben; bei Zweifeln werden Sachverhaltslücke und Rechtsfrage getrennt beschrieben.

## 5. Ausgabeformat

Erstelle ein vollständig ausformuliertes Annahme-, Begrenzungs- oder Absageschreiben und eine getrennte interne Konfliktprüfnotiz. Die Notiz nennt Suchumfang, Treffer, tatsächliche Vorbefassung, rechtliche Bewertung, mögliche Ausnahme, Schutzmaßnahmen und verantwortliche Entscheidung; sie wird dem Mandanten nicht ungefragt als Anhang übermittelt.

Endprodukte bestehen aus vollständigen, ausformulierten Sätzen; die Ausformulierungspflicht gilt für Schreiben, Vermerk, Klausel und Nachtrag. Skelette, Halbsätze und reine Aufzählungsgerüste sind unzulässig. Formatierte Dokumente verwenden, soweit technisch möglich, Times New Roman 11 pt und ausschließlich dezimale Gliederung. Wird nur Markdown oder Chattext erzeugt, steht der Exporthinweis „Times New Roman, 11 pt, dezimale Gliederung“ in einer getrennten Notiz an den Auftraggeber, nicht im Empfängertext. Technische Hinweise und Quellenkontrolle stehen außerhalb des Empfängertextes. Behaupte weder eine abgeschlossene Konfliktprüfung eines unzugänglichen Bestands noch erteilte Vollmacht, erfolgte Annahme oder versandtes Schreiben ohne Grundlage.

### 5.1. Abnahmekriterien

Das Schreiben erklärt Mandant, Gegenstand, Umfang und Beginn der Tätigkeit oder die Absage. Die Prüfnotiz enthält Suchdatum, Systeme, Begriffe, ungeprüfte Bestände und jede relevante Trefferbewertung. Eine genannte Frist ist durch Rechenvermerk und bestätigten Kalendereintrag belegt oder ausdrücklich vorläufig; ein nicht übernommener Auftrag wird klar abgegrenzt. Vergütung, Gegenstandswerthinweis und Verbraucherinformation sind vollständig oder mit konkreter offener Stelle bezeichnet. Mandatsvertrag, Vollmacht und Honorarabrede bleiben getrennte Dokumente. Ein Konflikttreffer ist begründet unerheblich, als zustimmungsfähige Erstreckung mit Vorkehrungen dokumentiert oder als persönliches Verbot mit Absage behandelt. Nächster Schritt, Person und Datum sind benannt. Führende Fassung, Pfad und Hash stehen im Mandatslauf beziehungsweise im Übergabevermerk; kein Gate wird stillschweigend freigegeben.

## 6. Beispiele

### 6.1. Gesellschaft oder Geschäftsführer mit vollständigem Annahmeschreiben

Ein Geschäftsführer schreibt am Montag, dem 5. Oktober 2026, von seiner Firmenadresse: „Bitte wehren Sie die Forderung gegen uns ab.“ Der Anspruch richtet sich persönlich gegen ihn. Der Skill stellt die erste Rückfrage, erhält die Antwort „für mich persönlich“, prüft den Konfliktbestand ohne Treffer und erstellt das Annahmeschreiben.

> Sehr geehrter Herr Lindqvist,
>
> in der Angelegenheit Rheintal Montage GmbH gegen Sie persönlich bestätigen wir die Übernahme Ihres Mandats mit Wirkung vom 7. Oktober 2026. Gegenstand unserer Beauftragung ist Ihre persönliche Verteidigung gegen den im Schreiben der Gesellschaft vom 28. September 2026 geltend gemachten Anspruch auf Schadensersatz in Höhe von 48.500 Euro. Eine Vertretung oder Beratung der Rheintal Montage GmbH ist mit diesem Mandat nicht verbunden; sollte die Gesellschaft ebenfalls anwaltlichen Rat wünschen, muss sie eine andere Kanzlei beauftragen.
>
> Wir haben in unserem Mandatsbestand keine frühere Tätigkeit für die Gesellschaft oder gegen Sie festgestellt. Als ersten Schritt erstellen wir bis Freitag, dem 16. Oktober 2026, eine schriftliche Einschätzung zu den behaupteten Pflichtverletzungen und zur Darlegungslast. Bitte übersenden Sie uns hierfür den Geschäftsführeranstellungsvertrag, die Gesellschafterbeschlüsse der letzten zwei Jahre und den Schriftverkehr mit der Gesellschaft seit August 2026.
>
> Wir rechnen nach der beigefügten Vergütungsvereinbarung zu einem Stundensatz von 280 Euro zuzüglich Umsatzsteuer ab. Diese Vereinbarung gilt für die außergerichtliche Verteidigung; eine gerichtliche Vertretung bedarf einer gesonderten Vereinbarung. Beigefügt sind außerdem die Vollmacht und unsere Informationen nach der Dienstleistungs-Informationspflichten-Verordnung.
>
> Mit freundlichen Grüßen
>
> Rechtsanwältin Mareike Holtkamp

Auf Stufe 2 setzt der Skill die Phase `annahme` mit dem Grund „Anfrage Lindqvist vom 05.10.2026“, trägt das Schreiben als `annahme` und die Prüfnotiz als `berufsrechtsvermerk` jeweils im Zustand `entwurf` mit Pfad und Hash ein und öffnet Gate G1 mit dem Bezug „Annahmeschreiben_v01.docx“. Den Honorarstand hält er im Übergabevermerk für den Honorarskill bereit, damit die Vergütungsvereinbarung in Textform als Anlage vorliegt. Dann bleibt er stehen: Erst wenn Rechtsanwältin Holtkamp G1 namentlich freigibt, wird das Annahmedatum übernommen, die Akte angelegt und der Versand über Gate G3 vorbereitet.

### 6.2. Frühere gemeinsame Immobilienberatung mit Absageschreiben

Die Ehefrau verlangt die einseitige Durchsetzung einer Ausgleichsregelung, die die Kanzlei im Jahr 2024 für beide Ehegatten gestaltet hat. Der Skill liest den früheren Gegenstand, bejaht dieselbe Rechtssache und den Interessenwiderstreit nach § 43a Absatz 4 Satz 1 BRAO und behandelt die pauschale Zustimmung des Ehemanns nicht als Heilung des persönlichen Verbots. Die Absage wird noch am selben Tag versandfertig gestellt.

> Sehr geehrte Frau Berisha,
>
> vielen Dank für Ihre Anfrage vom Dienstag, dem 6. Oktober 2026, zur Durchsetzung der Ausgleichszahlung aus der Vereinbarung vom 12. März 2024. Wir können dieses Mandat nicht übernehmen. Unsere Kanzlei hat die Vereinbarung seinerzeit für Sie und Ihren Ehemann gemeinsam gestaltet. Die einseitige Durchsetzung einzelner Regelungen gegen Ihren Ehemann betrifft dieselbe Rechtssache mit nunmehr widerstreitenden Interessen. Das Berufsrecht untersagt uns diese Tätigkeit; eine Einverständniserklärung Ihres Ehemanns ändert daran nichts.
>
> Bitte beauftragen Sie rechtzeitig eine andere Kanzlei. Nach Ihrer Schilderung ist die Ausgleichszahlung seit dem 30. September 2026 fällig; ob Verjährung oder vertragliche Fristen drohen, haben wir nicht geprüft und können wir für Sie nicht prüfen. Die Vereinbarung vom 12. März 2024 liegt Ihnen im Original vor; weitere Unterlagen aus der damaligen Beratung dürfen wir ohne Zustimmung beider Beteiligter nicht herausgeben.
>
> Für die Prüfung Ihrer Anfrage berechnen wir nichts. Diese Absage erfolgt unverzüglich, damit Sie Ihre Rechte ohne Verzögerung anderweitig wahrnehmen können.
>
> Mit freundlichen Grüßen
>
> Rechtsanwalt Dr. Jonas Reinholt

### 6.3. Digitaler Erstkontakt mit sofortiger Arbeit

Eine Verbraucherin schließt am Freitag, dem 2. Oktober 2026, über ein bundesweit beworbenes Portal ein entgeltliches Beratungsmandat zu einer Mietminderung und wünscht Bearbeitung am selben Tag. Der Skill bejaht den Fernabsatz, prüft Belehrung und elektronische Widerrufsfunktion nach § 356a BGB und dokumentiert die ausdrückliche Zustimmung zum Beginn vor Fristablauf einschließlich der Kenntnisbestätigung nach § 356 BGB. Die Kanzlei beginnt im wirksam erteilten Auftrag und behauptet nicht, das Widerrufsrecht sei mit dem ersten Dateiabruf erloschen; der Mandantin wird erklärt, dass bei Widerruf vor vollständiger Erbringung Wertersatz für die erbrachte Leistung geschuldet sein kann.

### 6.4. Drittfinanzierung durch die Muttergesellschaft

Eine Tochtergesellschaft wird wegen eines Liefervertrags beraten; die Mutter zahlt und verlangt alle Gesprächsprotokolle. Der Skill trennt Mandantin und Kostenträger, prüft die Vertretungsmacht der handelnden Geschäftsführerin und formuliert eine Berichtsregel: „Die Rheinwerk Logistik GmbH ist alleinige Mandantin. Die Rheinwerk Holding AG trägt die Vergütung, erhält aber Informationen aus dem Mandat nur, soweit die Geschäftsführung der Mandantin dies in Textform freigibt.“ Eine Konzernzugehörigkeit ist kein Geheimnisverzicht; zugleich wird keine zweite Mandatsaufnahme für den bloßen Zahlungsvorgang eröffnet.

### 6.5. Negativbeispiel: Konfliktregister nicht erreichbar

Eine neue Anfrage betrifft eine größere Unternehmensgruppe. Das Register ist vorübergehend nicht zugänglich, eine Mitarbeiterin erinnert sich an ein mögliches Altmandat. Eine falsche Ausgabe lautet: „Konfliktprüfung durchgeführt, keine Treffer. Wir übernehmen das Mandat vollumfänglich und kümmern uns um alle Fristen.“ Diese Ausgabe ist falsch, weil sie eine nicht durchgeführte Prüfung als abgeschlossen ausgibt, eine erinnerte Vorbefassung übergeht, eine umfassende Annahme ohne geklärten Umfang erklärt und eine Fristverantwortung behauptet, die ohne Rechenvermerk und ohne Auftrag nicht besteht. Die korrigierte Fassung lautet:

> Sehr geehrte Frau Dr. Castellani,
>
> wir bestätigen den Eingang Ihrer Anfrage vom Mittwoch, dem 7. Oktober 2026, für die Nordlicht Energie GmbH wegen der Kündigung des Wartungsvertrags mit der Baltic Grid Service AG. Wir prüfen derzeit, ob wir das Mandat übernehmen können. Unser Konfliktregister ist heute technisch nicht erreichbar; die Prüfung wird von Rechtsanwalt Feddersen persönlich bis Freitag, dem 9. Oktober 2026, abgeschlossen. Bis dahin sind wir nicht beauftragt und übernehmen keine Fristverantwortung.
>
> Nach Ihren Angaben hat die Gegenseite eine Stellungnahme bis Mittwoch, dem 21. Oktober 2026, gefordert. Diese Frist haben wir nicht berechnet und nicht geprüft; bitte beachten Sie sie selbst, bis wir die Übernahme bestätigen. Sollten wir absagen müssen, teilen wir Ihnen dies spätestens am 9. Oktober 2026 mit, damit Sie rechtzeitig eine andere Kanzlei beauftragen können.
>
> Ihre Unterlagen haben wir gesichert und bisher ausschließlich für die Übernahmeprüfung verwendet; eine inhaltliche Bearbeitung hat noch nicht begonnen.
>
> Mit freundlichen Grüßen
>
> Rechtsanwalt Hauke Feddersen

### 6.6. Zusätzliche Instanz und bestehender Deckel

Für außergerichtliche Verhandlungen wurde ein Festpreis vereinbart; der Mandant bittet nun um Klage. Der Skill prüft, ob der ursprüngliche Umfang gerichtliche Tätigkeit umfasst, und erstellt einen Nachtrag in Textform, ohne den bestehenden Deckel still zu erhöhen: „Diese Vergütungsvereinbarung wird mit Wirkung vom 7. Oktober 2026 auf die Vertretung im erstinstanzlichen Klageverfahren vor dem Landgericht erweitert. Für diese Tätigkeit gilt abweichend vom Festpreis ein Stundensatz von 260 Euro zuzüglich Umsatzsteuer; der Festpreis für die außergerichtliche Vertretung bleibt unverändert. Wir weisen darauf hin, dass die gegnerische Partei oder die Staatskasse im Fall der Kostenerstattung regelmäßig nicht mehr als die gesetzliche Vergütung erstatten muss.“ Klageentwurf und Fristprüfung werden im autorisierten Umfang weiterbearbeitet.

### 6.7. Kanzleiwechsel mit Prüfnotiz

Eine Anwältin tritt am Donnerstag, dem 1. Oktober 2026, in die Kanzlei ein. Sie hat in ihrer früheren Kanzlei den Verkäufer bei einem Unternehmenskauf beraten; die neue Kanzlei vertritt den Käufer wegen Täuschung im selben Erwerb. Die Prüfnotiz trennt ihr persönliches Verbot nach § 43a Absatz 4 Satz 1 BRAO von der Erstreckung nach Satz 2 und prüft die Ausnahme nach Satz 4: Information beider Mandanten ohne Offenlegung fremder Geheimnisse, Zustimmung in Textform, getrennte Zugriffsgruppe, Ausschluss aus Besprechungen und Kontrolle des Suchindex. Bis zur Entscheidung arbeitet die Anwältin nicht an diesem Mandat mit; nur die zur Kollisionsprüfung erforderlichen Angaben wurden nach Satz 6 offenbart.
