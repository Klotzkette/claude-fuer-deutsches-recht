---
name: verteilung-iv-vorlaeufige
description: Erstellt und prüft Schlussbericht, Schlussrechnung, Schlussverzeichnis, Schlussverteilung, Vollzugsnachweis, Aufhebungsvorlage und Nachtragsverteilung. Kontrolliert Abschlussreife, Konten, Forderungen, Masseverbindlichkeiten, Drittrechte, Rückbehalte sowie gerichtliche und menschliche Freigaben.
---

# Schlussbericht, Schlussrechnung und Verteilung

## 1. Zweck und Anwendungsfall

### 1.1 Auftrag

Dieser Skill führt ein eröffnetes Insolvenzverfahren vom belegten Abschlussstand bis zu einem gerichtsfähigen Abschlusspaket und, soweit beauftragt, bis zum dokumentierten Vollzug der Schlussverteilung, zur Aufhebung des Verfahrens und zu einer späteren Nachtragsverteilung. Er erzeugt je nach Auftrag einen Schlussbericht, eine Schlussrechnung mit Beleg- und Kontenabgleich, ein Schlussverzeichnis, eine Quotenberechnung, die Unterlagen für den Zahlungslauf, einen Vollzugsnachweis, eine Aufhebungsvorlage oder ein Nachtragsverteilungspaket.

Der Skill gilt vorrangig für das eröffnete Regelverfahren mit bestelltem Insolvenzverwalter. Bei Eigenverwaltung, Insolvenzplan, vorläufiger Verwaltung, Einstellung mangels Masse oder Einstellung nach Anzeige der Masseunzulänglichkeit wird zuerst geprüft, welche Abschlussnormen und Rollen tatsächlich gelten. Nur die mit dem jeweiligen Verfahrensweg vereinbaren Arbeitsschritte werden übernommen; insbesondere ersetzt die reguläre Schlussverteilung nach Paragrafen 196 bis 200 InsO nicht die Verteilung und Einstellung nach Paragrafen 208 bis 211 InsO.

### 1.2 Zielzustand

Das Ergebnis erhält für die jeweils erreichte Stufe genau einen Gate-Status: „nicht abschlussreif“, „einreichungsreif“, „gerichtlich zur Schlussverteilung zugelassen“, „menschlich zur Zahlung freigegeben“, „vollzogen“, „aufgehoben“, „Nachtragsverteilung angeordnet“ oder „Nachtragsverteilung vollzogen“. Ein Gate darf nicht übersprungen werden. „Einreichungsreif“ setzt voraus, dass alle entscheidenden Zahlen auf denselben Stichtag bezogen, sämtliche Massekonten centgenau abgestimmt, offene Vermögens- und Verpflichtungspositionen entschieden, die Forderungstabelle mit dem Schlussverzeichnis abgeglichen und gesetzlich zulässige Rückbehalte bestimmt sind. Die späteren Status setzen zusätzlich die jeweils erforderliche gerichtliche Entscheidung, den Fristablauf, die menschliche Freigabe und den belegten Vollzug voraus.

### 1.3 Beleg- und Freigabegrundsatz

Jede tragende Tatsachenangabe erhält eine konkrete Quelle, einen Stichtag und einen Belegstatus. Zulässige Belegstatus sind „abgeglichen“, wenn Primärbeleg und Kontrollquelle widerspruchsfrei übereinstimmen, „belegt“, wenn ein tragfähiger Primärbeleg vorliegt, der erforderliche Gegenabgleich aber noch aussteht, „offen“, wenn ein erforderlicher Nachweis fehlt, „widersprüchlich“, wenn Quellen voneinander abweichen, und „entfällt“, wenn die Position nach dokumentierter Begründung nicht einschlägig ist. Ein offener oder widersprüchlicher Betrag darf weder in eine verbindliche Quote noch in einen Zahlungslauf einfließen.

Einreichung, Auszahlung, Hinterlegung, Vergleich, Forderungsverzicht, Klagerücknahme, Freigabe eines Massegegenstands, Kontoschließung und Antrag auf Nachtragsverteilung bleiben menschlichen Entscheidungsträgern vorbehalten. Der Skill bereitet diese Handlungen vollständig vor, führt sie aber nur aus, wenn die konkret zuständige Person die konkrete Fassung oder Zahlung ausdrücklich freigegeben hat.

## 2. Eingaben

### 2.1 Verfahrens- und Auftragsdaten

Erforderlich sind der Eröffnungsbeschluss, die Bestallung, gerichtliche Verfügungen zum Abschluss, die aktuelle Verfahrensart, die Angaben zu Gläubigerausschuss und Gläubigerversammlung, frühere Berichte und Rechnungen, der gerichtliche Tabellenstand sowie die beauftragte Ausbaustufe. Fehlende Stammdaten werden ausschließlich als klar benannte Eingabefelder geführt, insbesondere `[Insolvenzgericht]`, `[Aktenzeichen]`, `[Schuldnerin oder Schuldner]`, `[Stichtag TT.MM.JJJJ, Uhrzeit]`, `[Name und Funktion der freigebenden Person]` und `[Datum der Freigabe]`.

Der Stichtag bezeichnet den Zeitpunkt, auf den Bankstände, Buchhaltung, Forderungstabelle, Masseverbindlichkeiten, Steuerstand, Rückbehalte und Quotenberechnung gemeinsam eingefroren werden. Nachträgliche Buchungen werden in einem gesonderten Nachlauf erfasst. Verändert der Nachlauf eine tragende Zahl, werden Schlussrechnung, Schlussverzeichnis, Quote und Zahlungsplan gemeinsam auf eine neue, einheitliche Version angehoben.

### 2.2 Rechnungswesen und Geldbestände

Benötigt werden sämtliche Massekonten, Unterkonten, Anderkonten, Festgeld- und Fremdwährungskonten, Barkassen, Zahlungsdienstleisterkonten und sonstigen Geldbestände mit vollständigen Auszügen bis zum Stichtag. Hinzu kommen die Finanzbuchhaltung mit Eröffnungs- und Schlussbilanz der Verfahrenskonten, Sachkonten, Buchungsjournal, Debitoren- und Kreditorenlisten, Belegregister, Umsatzsteuerkonten, Listen früherer Abschlagsverteilungen sowie Nachweise über noch schwebende Zahlungen, Rücklastschriften und Bankgebühren.

### 2.3 Masse, Prozesse und Verwertung

Benötigt werden das fortgeschriebene Masseverzeichnis, Verwertungsabrechnungen, Kaufverträge, Gutachten, Forderungseinzüge, Versicherungs- und Erstattungsansprüche, Prozesslisten, Vollstreckungsstände sowie alle Anfechtungs-, Organhaftungs-, D&O- und sonstigen Masseansprüche. Für jede noch offene Position müssen Anspruchsgrund, Gegner, Nominalwert, realistischer Nettoerlös, Kosten, Laufzeit, Verjährung, Beweisstand, Prozessstand, Vollstreckbarkeit und vorgeschlagene Abschlussentscheidung vorliegen.

### 2.4 Insolvenzforderungen und Drittrechte

Benötigt werden der aktuelle gerichtliche Tabellenauszug und die interne Tabelle mit laufender Nummer, Gläubigeridentität, Forderungsgrund, angemeldetem und festgestelltem Betrag, Rang, Zinsen, Kosten, Bestreitensgrund, Titel, Feststellungsprozess, Abtretung, Rechtsnachfolge, Bedingung und früherer Ausschüttung. Aussonderungsrechte, Absonderungsrechte, Sicherheiten, Verwertungserlöse, Feststellungs- und Verwertungskosten, Umsatzsteuer, an Sicherungsnehmer ausgekehrte Beträge und mögliche Ausfallforderungen werden gesondert belegt.

### 2.5 Kosten, Masseverbindlichkeiten, Steuern und Vergütung

Benötigt werden Gerichtskostenrechnungen, Vergütungsanträge und Festsetzungsbeschlüsse für vorläufige Verwaltung, Insolvenzverwaltung und Gläubigerausschuss, Auslagen- und Umsatzsteuerberechnungen sowie sämtliche sonstigen Masseverbindlichkeiten. Jede Masseverbindlichkeit wird mit Rechtsgrund, Leistungszeitraum, Gläubiger, Netto- und Bruttobetrag, Steueranteil, Fälligkeit, Streitstand, Zahlungsstatus und Beleg erfasst.

Für Steuern und Sozialabgaben werden die Zeiträume vor und nach Eröffnung getrennt. Erforderlich sind Steuererklärungen, Steuerberechnungen, Bescheide, Kontoauszüge der Finanzbehörden und Einzugsstellen, Rechtsbehelfe, Prüfungsstände, erwartete Nachzahlungen und Erstattungen sowie eine dokumentierte Einschätzung der steuerlichen Beratung zu noch offenen Erklärungs- und Zahlungspflichten.

### 2.6 Vollzug und Freigaben

Benötigt werden die gerichtlichen Bekanntmachungen, Zustimmungen und Terminsverfügungen, Stellungnahmen des Gläubigerausschusses, Einwendungen gegen das Schlussverzeichnis, Nachweise zu Feststellungsklagen und Ausfällen, geprüfte Empfängerdaten, frühere Zahlungsnachweise und die kanzleiinterne Freigaberegel. Eine bloße E-Mail-Adresse, ein ungeprüfter Kontowechsel oder eine aus Altakten übernommene Bankverbindung genügt nicht als Zahlungsfreigabe.

## 3. Ablauf / Checkliste

### 3.1 Aktenstand und Version sperren

Zuerst werden die vorhandenen Unterlagen auftragsbezogen gelesen. Bereits belegte Tatsachen werden nicht erneut abgefragt. Danach werden Stichtag, Datenquellen, Dateiversionen und Bearbeitungsstand in einer Kontrollnotiz fixiert. Jede tragende Zahl erhält einen Verweis auf Kontoauszug, Buchung, Beleg, gerichtliche Tabelle, Bescheid oder sonstigen Primärnachweis und zusätzlich den Belegstatus nach Abschnitt 1.3.

### 3.2 Verfahrensweg und Abschlussreife bestimmen

Es wird festgestellt, ob eine reguläre Schlussverteilung nach Paragrafen 196 bis 200 InsO, eine Einstellung nach Masseunzulänglichkeit gemäß Paragraf 211 InsO oder ein anderer Beendigungsweg vorliegt. Eine reguläre Schlussverteilung ist erst vorzubereiten, wenn die Verwertung der Insolvenzmasse mit Ausnahme eines laufenden Einkommens beendet ist. Bei ungedeckten fälligen oder voraussichtlich bei Fälligkeit ungedeckten sonstigen Masseverbindlichkeiten wird die Prüfung nach Paragrafen 208 bis 211 InsO vorgeschaltet und die reguläre Schlussverteilung gesperrt.

Für jede offene Masseposition wird eine Abschlussentscheidung dokumentiert. Die Entscheidung lautet auf Einziehung, Verwertung, Vergleich, Prozessführung, Vollstreckung, begründete Nichtverfolgung, Freigabe, konkrete Behandlung im Abschluss oder konkret zu beantragende Nachtragsverteilung. Eine bekannte offene Position wird nicht pauschal mit dem Hinweis „Nachtragsverteilung“ vertagt. Soll sie einer Nachtragsverteilung vorbehalten werden, werden Massezugehörigkeit, Grund der derzeit fehlenden Verwertbarkeit, erwarteter Nettoerlös, Kosten, zeitliche Perspektive und erforderliche gerichtliche Anordnung ausdrücklich begründet.

Offene Anfechtungs- und Haftungsansprüche werden einzeln nach Anspruchsgrund, Gegner, Betrag, Beweislage, Einwendungen, Verjährung, Prozess- und Vollstreckungsrisiko sowie wirtschaftlichem Nettoergebnis bewertet. Eine Nullbewertung oder Nichtverfolgung benötigt eine nachvollziehbare Kosten-Nutzen-Entscheidung und, soweit erforderlich, die Zustimmung des zuständigen Gläubigerorgans oder eine menschliche Freigabe.

### 3.3 Konten- und Belegabgleich durchführen

Die Schlussrechnung wird aus den Einzelbuchungen aufgebaut und nicht aus einer bloßen Saldenliste übernommen. Für jedes Konto werden Anfangsbestand, sämtliche Einnahmen, sämtliche Ausgaben und Schlussbestand nachgewiesen. Interne Umbuchungen zwischen Massekonten werden auf beiden Seiten identifiziert, damit sie weder als zusätzlicher Massezufluss noch als zusätzliche Masseausgabe erscheinen. Fremdwährungen werden mit Kursquelle und Umrechnungsdatum dokumentiert.

Die Kontrollrechnung lautet für jedes Konto und für die Gesamtmasse: Anfangsbestand zuzüglich belegter Einnahmen abzüglich belegter Ausgaben ergibt den Buchschlussbestand; der Buchschlussbestand muss mit dem Bank- oder Kassenbestand zum Stichtag übereinstimmen. Offene Banktransaktionen, Rücklastschriften, Schecks, Gebühren oder zeitversetzte Wertstellungen werden einzeln aufgelöst. Solange die Gesamtdifferenz nicht null Euro beträgt, lautet der Abschlussstatus „nicht abschlussreif“.

Jede Einnahme wird einer Masseposition oder einem sonstigen Rechtsgrund und jede Ausgabe einer Verfahrenskostenposition, Masseverbindlichkeit, Absonderungsauskehrung, früheren Verteilung oder sonstigen belegten Verwendung zugeordnet. Doppelte Buchungen, unklare Sammelbuchungen und Verrechnungen ohne erkennbare Bruttowerte werden aufgeklärt. Schlussbericht, Schlussrechnung, Kontennachweise und Verteilungsbetrag müssen denselben Schlussbestand ausweisen.

### 3.4 Masseverbindlichkeiten, Drittrechte und Steuern abschließen

Kosten des Insolvenzverfahrens nach Paragraf 54 InsO und sonstige Masseverbindlichkeiten nach Paragraf 55 InsO werden getrennt von Insolvenzforderungen erfasst und vor der Verteilung behandelt. Streitig gebliebene Masseverbindlichkeiten werden mit Streitgegenstand, wahrscheinlichem Betrag, Verfahrensstand und vorgeschlagener rechtlicher Behandlung ausgewiesen. Eine Insolvenzforderung darf nicht wegen ihrer wirtschaftlichen Dringlichkeit als Masseverbindlichkeit behandelt werden; umgekehrt darf eine echte Masseverbindlichkeit nicht in das Schlussverzeichnis der Insolvenzgläubiger verschoben werden.

Aussonderungsgegenstände nach Paragraf 47 InsO werden außerhalb der verteilbaren Masse nachgewiesen. Bei Absonderungsrechten werden Bruttoerlös, Feststellungs- und Verwertungskosten, Umsatzsteuer, Nettoauskehrung, Zahlungstag und verbleibender Ausfall miteinander abgestimmt. Nur der nach den gesetzlichen Voraussetzungen berücksichtigungsfähige Ausfall fließt als Insolvenzforderung in das Schlussverzeichnis ein.

Steuer- und Sozialversicherungspositionen werden zeitraum- und steuerartenbezogen abgeschlossen. Noch ausstehende Bescheide, Außenprüfungen, Rechtsbehelfe, Erklärungen, Umsatzsteuerfolgen von Verwertungen, Lohnsteuerfragen, Erstattungsansprüche und mögliche Nachzahlungen werden im Bericht einzeln benannt. Eine erwartete Steuererstattung wird weder ohne Beleg als verfügbare Masse eingerechnet noch ohne konkrete rechtliche Prüfung als freie Rückstellung vom Verteilungsbetrag abgezogen.

Gerichtskosten und Vergütungen werden mit Antrag, Berechnungsgrundlage, festgesetztem Betrag, Auslagen und Umsatzsteuer abgeglichen. Fehlt eine erforderliche Festsetzung, wird dies als Gerichtsgate behandelt. Die Quote wird erst verbindlich, wenn die Kostenposition feststeht oder ihre vorläufige Behandlung rechtlich und gerichtlich belastbar geklärt ist.

### 3.5 Insolvenzforderungen und Schlussverzeichnis konsolidieren

Der gerichtliche Tabellenauszug wird Zeile für Zeile mit der internen Forderungsliste verglichen. Gläubigeridentität, laufende Nummer, Forderungsgrund, festgestellter Betrag, Rang, Bestreiten durch Verwalter oder Schuldner, Titel, Rechtsnachfolge, Abtretung, Bedingung, Absonderungsausfall und frühere Ausschüttungen werden geprüft. Dubletten, nachträgliche Änderungen und voneinander abweichende Summen werden vor Erstellung des Schlussverzeichnisses aufgelöst.

Das Schlussverzeichnis enthält nur Forderungen, die nach Paragrafen 187 bis 193 InsO bei der konkreten Verteilung zu berücksichtigen sind. Für bestrittene Forderungen wird kontrolliert, ob der nach Paragraf 189 InsO erforderliche Nachweis rechtzeitig und inhaltlich ausreichend geführt ist. Für absonderungsberechtigte Gläubiger werden Verzicht oder Ausfall nach Paragraf 190 InsO geprüft. Aufschiebend bedingte Forderungen werden nach Paragraf 191 InsO behandelt. Änderungen des Verzeichnisses nach Ablauf der Ausschlussfrist werden innerhalb der gesetzlichen Frist nachvollziehbar eingearbeitet.

Für jede berücksichtigte Forderung werden verteilungsfähiger Betrag, bereits erhaltene Abschläge, verbleibende Bemessungsgrundlage, Quote und Auszahlungsbetrag ausgewiesen. Nachrangige Forderungen werden in einer eigenen Rangklasse geführt und nur berücksichtigt, wenn die gesetzlichen Voraussetzungen und die vorhandene Masse dies erlauben. Die Summe der Einzelbeträge muss der im Verzeichnis ausgewiesenen Forderungssumme entsprechen.

### 3.6 Verteilungsbetrag, Quote und Rückbehalte berechnen

Der verfügbare Verteilungsbetrag wird aus dem centgenau abgestimmten Geldbestand abgeleitet. Abgezogen werden bereits fällige oder im Abschluss rechtlich zu berücksichtigende Verfahrenskosten und Masseverbindlichkeiten, notwendige Vollzugskosten sowie gesetzlich zulässige Rückbehalte oder Hinterlegungsbeträge. Jede Kürzung erhält Betrag, Rechtsgrund, Begünstigten, Fälligkeit, Auslöser der Freigabe, Verwahrort und Beleg.

Pauschale Sicherheitsabschläge, freie Liquiditätspuffer und unbestimmte Rückstellungen werden ohne konkret belegte rechtliche und rechnerische Grundlage nicht vom Verteilungsbetrag abgezogen. Zu unterscheiden sind bereits entstandene Masseverbindlichkeiten, gesetzliche Rückbehalte für konkret bezeichnete Forderungen, die Hinterlegung nach Paragraf 198 InsO und Gegenstände oder Beträge, für die eine Nachtragsverteilung nach Paragrafen 203 bis 205 InsO beantragt werden soll. Die vom Bundesgerichtshof anerkannte enge Ausnahme für voraussichtlich ungedeckte Kosten einer Wohlverhaltensperiode bei natürlichen Personen wird nur im einschlägigen Fall, mit aktualisierter Rechtsprüfung und ohne Verallgemeinerung angewandt.

Die Quote ergibt sich aus dem verfügbaren Verteilungsbetrag geteilt durch die Summe der in derselben Rangklasse berücksichtigten Forderungen. Rechenweg, Rundungsregel und Behandlung eines Rundungsrests werden offengelegt. Die Summe aus Auszahlungsbeträgen, zulässigen Rückbehalten, Hinterlegungen, Vollzugskosten und einem gegebenenfalls herauszugebenden Überschuss muss den hierfür verfügbaren Geldbestand vollständig erklären.

### 3.7 Schlussbericht und Schlussrechnung erstellen

Der Schlussbericht stellt Verfahrensgang, wesentliche Maßnahmen, Masseermittlung, Verwertung, Fortführung oder Stilllegung, Rechtsstreitigkeiten, Anfechtungs- und Haftungsansprüche, Aus- und Absonderungsrechte, Insolvenzforderungen, Masseverbindlichkeiten, Steuerstand, Kosten, Vergütung, frühere Verteilungen, Abschlussreife, Schlussquote und mögliche Nachtragspositionen in vollständigen Sätzen dar. Bewertungen werden von Tatsachen getrennt; jede offene Position erhält Entscheidung, Betrag, Belegstatus und nächsten Schritt.

Die Schlussrechnung stellt sämtliche Einnahmen und Ausgaben nachvollziehbar und belegscharf dar. Sie enthält Kontenübersicht, Buchungs- und Belegverzeichnis, Abstimmrechnung, Schlussbestand und eine Überleitung zum verfügbaren Verteilungsbetrag. Belegnummern, Buchungsdaten und Beträge müssen sich gegenseitig widerspruchsfrei zuordnen lassen. Der Schlussbericht darf keine andere Masse, Forderungssumme oder Quote nennen als Schlussrechnung und Schlussverzeichnis.

### 3.8 Gerichtsgate für Einreichung und Prüfung beachten

Vor der Einreichung werden Schlussbericht, Schlussrechnung, Belegverzeichnis, Schlussverzeichnis, Vergütungsunterlagen und Anträge im Vier-Augen-Prinzip geprüft. Danach erteilt die zuständige Person eine dokumentierte menschliche Freigabe der konkret bezeichneten Version. Ohne diese Freigabe wird nur ein einreichungsfertiger Entwurf ausgegeben.

Das Gericht prüft die Schlussrechnung nach Paragraf 66 InsO und legt sie mit Belegen, Prüfvermerk und gegebenenfalls den Bemerkungen des Gläubigerausschusses zur Einsicht aus. Der Zeitraum zwischen Auslegung und Gläubigerversammlung soll mindestens eine Woche betragen. Die Schlussverteilung darf nach Paragraf 196 Absatz 2 InsO erst mit gerichtlicher Zustimmung vorgenommen werden. Bei dieser Zustimmung bestimmt das Gericht den Schlusstermin nach Paragraf 197 InsO; zwischen öffentlicher Bekanntmachung und Termin soll mindestens ein Monat und höchstens zwei Monate liegen.

Vor der Verteilung stellt der Insolvenzverwalter das Schlussverzeichnis nach Paragraf 188 InsO auf und legt es auf der Geschäftsstelle zur Einsicht der Beteiligten nieder. Er zeigt dem Gericht die Summe der Forderungen und den verfügbaren Betrag an; das Gericht macht nur diese beiden Summen öffentlich bekannt. Diese Bekanntmachung löst insbesondere die zweiwöchige Ausschlussfrist nach Paragraf 189 InsO aus. Nach Fristablauf werden rechtzeitige Nachweise, notwendige Rückbehalte und Änderungen nach Paragraf 193 InsO eingearbeitet. Einwendungen gegen das Schlussverzeichnis und gerichtliche Entscheidungen hierzu werden vor dem Zahlungslauf vollständig verarbeitet.

### 3.9 Schlussverteilung vollziehen und Aufhebung vorbereiten

Nach Abschluss der gerichtlichen Gates wird eine finale Zahlungsliste aus dem freigegebenen Schlussverzeichnis erzeugt. Empfängeridentität und Bankverbindung werden über einen unabhängigen, dokumentierten Kanal geprüft. Datei- oder Systemimport, Freigabe des Zahlungslaufs und tatsächliche Ausführung werden getrennt protokolliert. Der Skill darf ohne ausdrückliche menschliche Zahlungsfreigabe keine Überweisung, Hinterlegung oder sonstige Vermögensverfügung auslösen.

Nach dem Zahlungslauf werden Zahlungsdatei, Bankauszug, Buchhaltung, Einzelbeträge und Gesamtsumme erneut centgenau abgeglichen. Rückläufer, unzustellbare Zahlungen und nicht erreichbare Berechtigte werden nicht eigenmächtig auf andere Konten umgeleitet; ihre Behandlung wird rechtlich geprüft und erforderlichenfalls dem Gericht zur Entscheidung vorgelegt. Gesetzlich zurückbehaltene Beträge werden nach Paragraf 198 InsO für Rechnung der Beteiligten hinterlegt.

Der Vollzugsbericht weist jede Auszahlung, jede Hinterlegung, jeden Rückläufer, den verbleibenden Kontostand und die Übereinstimmung mit dem Schlussverzeichnis nach. Erst nach vollständigem Vollzug wird dem Gericht der Abschlussstand für die Aufhebung nach Paragraf 200 InsO mitgeteilt. Das Verfahren wird intern erst als aufgehoben gekennzeichnet, wenn Aufhebungsbeschluss und öffentliche Bekanntmachung dokumentiert sind. Massekonten werden erst nach allen Schlussbuchungen, erforderlichen Nachläufen und menschlicher Freigabe geschlossen.

### 3.10 Nachtragsverteilung bearbeiten

Nach dem Schlusstermin sowie gegebenenfalls nach Aufhebung bleibt ein Nachtragsregister aktiv. Ein möglicher Nachtragsfall wird nur angenommen, wenn ein Tatbestand des Paragrafen 203 Absatz 1 InsO vorliegt, insbesondere wenn ein zurückbehaltener Betrag frei wird, ein aus der Masse gezahlter Betrag zurückfließt oder ein Massegegenstand ermittelt wird. Die Aufhebung steht der Anordnung nicht entgegen. Der Insolvenzverwalter oder ein Insolvenzgläubiger kann die Anordnung beantragen; das Gericht kann von Amts wegen tätig werden. Auch der frühere Insolvenzverwalter bleibt nach Aufhebung antragsbefugt. Ein vor Aufhebung bekannter, aber nicht verwerteter Massegegenstand kann nach der amtlich verifizierten Rechtsprechung grundsätzlich erfasst sein; Massezugehörigkeit, konkrete Verwertbarkeit und gerichtliche Anordnung bleiben jedoch eigenständig zu prüfen.

Vor einem Antrag werden Herkunft, Massezugehörigkeit, Bruttozufluss, Kosten, Nettoverteilungsbetrag, Geringfügigkeit, mögliche Kostenvorschusspflicht und betroffene Schlussverzeichnispositionen belegt. Ohne gerichtliche Anordnung wird keine Nachtragsverteilung vorgenommen. Nach der Anordnung wird auf Grundlage des Schlussverzeichnisses verteilt und dem Gericht nach Paragraf 205 InsO Rechnung gelegt. Veränderungen in Person oder Empfangsberechtigung eines Gläubigers werden belegt, ohne die festgestellte Forderung oder Rangfolge ohne Rechtsgrund neu zu bestimmen.

Auch Antrag, Auszahlung und Rechnungslegung der Nachtragsverteilung benötigen jeweils die dokumentierte menschliche Freigabe. Bei einem nach Paragraf 211 InsO eingestellten Verfahren wird die besondere Verweisung in Paragraf 211 Absatz 3 InsO beachtet.

### 3.11 Abschließendes Qualitätsgate anwenden

Vor jeder Endfassung wird bestätigt, dass alle Dokumente denselben Stichtag und dieselbe Version verwenden, der Kontenabgleich null Euro Differenz ausweist, offene Masse-, Anfechtungs-, Steuer- und Vergütungsfragen entschieden sind, Insolvenzforderungen und Masseverbindlichkeiten getrennt bleiben, Aus- und Absonderung vollständig abgerechnet sind, jeder Rückbehalt eine konkrete Grundlage besitzt, die Quote reproduzierbar ist, alle gerichtlichen Gates berücksichtigt und alle menschlichen Freigaben der konkreten Fassung zugeordnet sind.

Scheitert ein Prüfschritt, wird kein scheinbar fertiges Abschlusspaket erzeugt. Stattdessen nennt die Kontrollnotiz den Status „nicht abschlussreif“, die betroffene Zahl oder Rechtsfrage, den fehlenden Beleg, die zuständige Person und den konkreten nächsten Arbeitsschritt. Unabhängige, bereits belastbare Teile dürfen als vorläufiger Entwurf ausgegeben werden, müssen ihren Vorläufigkeitsgrund aber sichtbar benennen.

## 4. Quellenpflicht

### 4.1 Verbindliche Quellenregel

Es gilt die zentrale [`references/zitierweise.md`](../../../references/zitierweise.md). Tragende Aussagen werden zuerst mit dem aktuellen Normtext und sodann, soweit erforderlich, mit amtlich oder frei verifizierter Rechtsprechung belegt. Entscheidungen werden nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, konkreter Randnummer und prüfbarer Quelle verwendet. BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen dürfen nicht aus Modellwissen ergänzt werden.

Der Rechtsstand ist vor jeder produktiven Einreichung anhand der amtlichen Gesamtfassung der [Insolvenzordnung](https://www.gesetze-im-internet.de/inso/) und der einschlägigen [Insolvenzrechtlichen Vergütungsverordnung](https://www.gesetze-im-internet.de/insvv/) zu prüfen. Für diesen Workflow sind insbesondere Paragraf 47, Paragrafen 49 bis 55, Paragrafen 63 bis 66, Paragrafen 166 bis 173, Paragrafen 187 bis 205 sowie bei Masseunzulänglichkeit Paragrafen 208 bis 211 InsO zu prüfen. Gerichtliche Verfügungen, Bekanntmachungen und Tabellenstände werden aus der Verfahrensakte oder dem Gerichtsportal belegt.

### 4.2 Verifizierte Entscheidungsanker

Eine vorgelegte Schlussrechnung oder ein bereits abgehaltener Schlusstermin beweist für sich keine Abschlussreife. Für die Fälligkeit der Verwaltervergütung muss die vergütungspflichtige Tätigkeit grundsätzlich erledigt und die Verwertung abgeschlossen sein; regelmäßig dürfen nur Schlusstermin und abschließende Schlussverteilung ausstehen. Die Entscheidung trägt damit die Prüfung offener Verwertungspositionen, erlaubt aber keine zeitabschnittsweise Teilfestsetzung der Vergütung: [BGH, Beschl. v. 11.11.2021 - Az. IX ZB 19/20, amtlicher Volltext Rn. 12 und 14 bis 21](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2020/IX_ZB__19-20.pdf?__blob=publicationFile&v=1).

Die unbeschränkte Anmeldung eines absonderungsberechtigten Gläubigers bedeutet noch keinen Verzicht auf das Absonderungsrecht. Die Beschränkung auf den Ausfall wird erst bei der Verteilung nach Paragraf 190 InsO relevant; volle Teilnahme aufgrund eines Verzichts setzt voraus, dass der belastete Gegenstand dadurch für die Masse frei wird. Die Entscheidung trägt keine Doppelbefriedigung und keinen nur geschätzten Ausfall: [BGH, Urt. v. 09.03.2017 - Az. IX ZR 177/15, amtlicher Volltext Rn. 16 bis 17](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2015/IX_ZR_177-15.pdf?__blob=publicationFile&v=1).

Der frühere Insolvenzverwalter ist nach Paragraf 203 Absatz 1 und Absatz 2 InsO zur Beantragung einer Nachtragsverteilung und nach Paragraf 204 Absatz 1 Satz 2 InsO zur Beschwerde befugt. Die Entscheidung betraf einen später aus materiellen Gründen nicht massezugehörigen Abfindungsanspruch und belegt deshalb keine Massezugehörigkeit im Einzelfall: [BGH, Beschl. v. 21.05.2026 - Az. IX ZB 45/25, amtlicher Volltext Rn. 7 bis 17](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZB__45-25.pdf?__blob=publicationFile&v=1).

Bei einer natürlichen Person ist die enge Rückstellung für voraussichtlich ungedeckte Kosten der Wohlverhaltensperiode nach Möglichkeit aus der um Kosten und sonstige Masseverbindlichkeiten bereinigten Masse zu bilden. Ein später frei werdender Überschuss fällt nach Paragraf 203 Absatz 1 Nummer 1 InsO in die Nachtragsverteilung. Die Entscheidung setzt insbesondere natürliche Person, Wohlverhaltensperiode und Kostenstundung voraus und rechtfertigt keine allgemeinen Sicherheitsrückstellungen: [BGH, Beschl. v. 23.04.2026 - Az. IX ZB 36/25, amtlicher Volltext Rn. 9 bis 13 und 15 bis 21](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZB__36-25.pdf?__blob=publicationFile&v=1).

Paragraf 203 Absatz 1 Nummer 3 InsO kann einen vor Aufhebung bekannten, aber unverwertet gebliebenen Massegegenstand erfassen; noch nicht feststehende Steuererstattungsansprüche können der Nachtragsverteilung vorbehalten werden. Die Massezugehörigkeit bleibt Tatbestandsgrenze: [BGH, Beschl. v. 25.09.2025 - Az. IX ZB 13/25, amtlicher Volltext Rn. 7 bis 16 und 20 bis 23](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZB__13-25.pdf?__blob=publicationFile&v=1).

Für den Nachweis nach Paragraf 189 InsO genügt nicht jede bloße Behauptung einer Klageeinreichung. Der Nachweis muss dem Verwalter hinreichende Gewissheit über die tatsächliche gerichtliche Einreichung, den Betrag und die weiteren Voraussetzungen verschaffen; soweit ein Kostenvorschuss Voraussetzung der wirksamen Verfahrenseinleitung ist, ist auch dessen rechtzeitige Zahlung nachzuweisen. Die Entscheidung betrifft nicht festgestellte und nicht titulierte Forderungen und darf nicht auf Paragraf 190 InsO übertragen werden: [BGH, Beschl. v. 13.09.2012 - Az. IX ZB 143/11, amtlicher Volltext Rn. 6 bis 10](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2011/IX_ZB_143-11.pdf?__blob=publicationFile&v=1).

Eine erst nach öffentlicher Bekanntmachung und Niederlegung des Schlussverzeichnisses angemeldete Forderung nimmt nicht mehr an der konkreten Schlussverteilung teil. Das beendet weder die Forderung noch allgemein die Möglichkeit einer späteren Tabellenaufnahme; Forderungsfeststellung und Verteilung bleiben eigenständige Verfahrensabschnitte: [BGH, Beschl. v. 22.03.2007 - Az. IX ZB 8/05, amtlicher Volltext Rn. 8 bis 11](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2005/IX_ZB___8-05.pdf?__blob=publicationFile&v=1).

Im Abschluss nach Paragraf 211 InsO findet keine Schlussverteilung nach Paragraf 196 InsO und deshalb kein förmlicher Schlusstermin nach Paragraf 197 InsO statt. Eine anders bezeichnete abschließende Versammlung wird nicht allein durch die Erörterung von Schlussrechnung, Schlussverzeichnis oder nicht verwertbaren Gegenständen zum Schlusstermin. Die Entscheidung trägt die Verfahrensweiche bei Masseunzulänglichkeit, nicht die Behandlung jeder einzelnen Masseverbindlichkeit: [BGH, Beschl. v. 24.03.2022 - Az. IX ZB 35/21, amtlicher Volltext Rn. 7 bis 13](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2021/IX_ZB__35-21.pdf?__blob=publicationFile&v=1).

Weitere Entscheidungen werden nur aufgenommen, wenn sie im konkreten Arbeitsgang amtlich oder frei verifiziert wurden. Eine nicht verifizierte Rechtsprechungserinnerung wird als Recherchefrage gekennzeichnet und nicht zur Begründung einer Einreichung, Quote, Rückstellung oder Zahlung verwendet.

## 5. Ausgabeformat

### 5.1 Internes Kontrollpaket

Das interne Kontrollpaket enthält eine Abschlussreife-Notiz, die Stichtags- und Versionskontrolle, die Belegstatusmatrix, den Kontenabgleich, die Liste offener und erledigter Massepositionen, die Masseverbindlichkeiten- und Steuerabstimmung, die Rückbehaltsmatrix, die Quotenrechnung und das Freigabeprotokoll. Jeder offene Punkt wird mit Auswirkung, Verantwortlichkeit und nächstem Schritt in vollständigen Sätzen beschrieben.

Als Ausgangsstruktur dienen die internen Arbeitsvorlagen für [Schlussbericht und Schlussrechnung](../../assets/templates/schlussbericht-schlussrechnung.md) sowie für [Schlussverzeichnis und Verteilungsrechnung](../../assets/templates/verteilungsverzeichnis.md). Sie werden mit den konkreten Belegen vollständig ausgefüllt und nicht als leeres Gerüst ausgegeben.

### 5.2 Gerichtspaket

Das Gerichtspaket enthält ein ausformuliertes Anschreiben, den Schlussbericht, die Schlussrechnung, das Belegverzeichnis, den Kontennachweis, das Schlussverzeichnis, die Quotenberechnung, erforderliche Anträge und eine geordnete Anlagenliste. Nach Vollzug kommen der Vollzugsbericht, Zahlungs- und Hinterlegungsnachweise sowie die Mitteilung des Aufhebungsstands hinzu. Interne Prüfcodes und technische Arbeitsanweisungen werden nicht in das versandfertige Gerichtsdokument übernommen.

### 5.3 Verteilungs- und Nachtragspaket

Das Verteilungspaket enthält die freigegebene Zahlungsliste, die dokumentierte Empfängerprüfung, die Zahlungsdatei oder Überweisungsübersicht, das Vier-Augen-Protokoll, den Bank- und Buchungsabgleich sowie die Rückläuferliste. Ein Nachtragsverteilungspaket enthält zusätzlich den belegten Nachtragstatbestand, den Antragsentwurf, die gerichtliche Anordnung, die Berechnung auf Grundlage des Schlussverzeichnisses und die nach Paragraf 205 InsO geschuldete Rechnungslegung.

### 5.4 Sprach- und Formatstandard

Alle Endprodukte werden vollständig, präzise und in grammatikalisch vollständigen Sätzen ausgegeben. Stichwortskelette, Halbsätze, leere Tabellenrümpfe und reine Aufzählungsauswürfe sind als Endprodukt unzulässig. Tabellen sind für Zahlen und wiederkehrende Prüffelder zulässig, müssen aber ausgefüllt, rechnerisch abgestimmt und durch die erforderliche Erläuterung ergänzt sein. Fehlen entscheidende Angaben, werden nur die in Abschnitt 2.1 bezeichneten oder ebenso eindeutig benannten Eingabefelder verwendet; der übrige Text bleibt ausformuliert.

Formatierte Enddokumente verwenden, soweit technisch möglich, Times New Roman in 11 pt und ausschließlich dezimale Gliederung. Überschriften bleiben in derselben Schriftfamilie. Bei reiner Markdown- oder Chat-Ausgabe steht außerhalb des versandfertigen Dokuments ein getrennter Exporthinweis mit dem Wortlaut: „Für den Export ist Times New Roman, 11 pt, mit ausschließlich dezimaler Gliederung zu verwenden.“ Eine nicht tatsächlich erzeugte DOCX- oder PDF-Datei wird nicht behauptet.

Beträge werden in Euro mit zwei Dezimalstellen und nachvollziehbarem deutschen Zahlenformat ausgegeben. Quoten erhalten so viele Nachkommastellen, wie zur centgenauen Reproduktion sämtlicher Auszahlungsbeträge erforderlich sind. Rundungsdifferenzen werden nicht verborgen, sondern mit Regel und Restbetrag dokumentiert.

## 6. Beispiele

### 6.1 Abschlussreifes Regelverfahren

Die Massekonten und die Buchhaltung weisen zum gemeinsamen Stichtag jeweils 84.530,40 Euro aus. Nach belegten Verfahrenskosten und sonstigen Masseverbindlichkeiten von zusammen 12.530,40 Euro verbleiben 72.000,00 Euro. Das abgestimmte Schlussverzeichnis enthält ausschließlich einfache, festgestellte und noch nicht befriedigte Insolvenzforderungen von 240.000,00 Euro. Der Skill weist eine Quote von 30 Prozent aus, erstellt das Gerichtspaket und kennzeichnet den Zahlungslauf bis zur gerichtlichen Zustimmung, zum Abschluss des Schlusstermins und zur menschlichen Zahlungsfreigabe als gesperrt.

### 6.2 Fehlender Kontenabgleich

Die Bankauszüge weisen 61.842,73 Euro aus, während die Buchhaltung 59.000,00 Euro zeigt. Außerdem ist eine Umsatzsteuerzahlung ohne Bescheid oder Berechnung als Sammelbuchung erfasst. Der Skill berechnet keine verbindliche Quote, sondern gibt den Status „nicht abschlussreif“ aus. Er bezeichnet die Differenz von 2.842,73 Euro, die ungeklärte Steuerbuchung, die zuständigen Bearbeiter und die jeweils benötigten Belege als konkrete nächste Schritte.

### 6.3 Bestrittene Forderung mit rechtzeitigem Nachweis

Bei einer verteilungsfähigen Quote von 30 Prozent ist eine Forderung über 50.000,00 Euro bestritten. Der Gläubiger weist innerhalb der Ausschlussfrist durch eine gerichtliche Eingangsbestätigung nach, dass die Feststellungsklage erhoben wurde. Der Skill berücksichtigt einen Rückbehalt von 15.000,00 Euro, dokumentiert Rechtsgrund und Nachweis, führt den Betrag im Schlussverzeichnis und bereitet die Hinterlegung nach Paragraf 198 InsO vor. Nach gerichtlicher Zulassung der Schlussverteilung und menschlicher Freigabe wird der Betrag für Rechnung des Beteiligten hinterlegt; der Ausgang des Feststellungsrechtsstreits bestimmt seine spätere Verwendung.

### 6.4 Erwartete Steuererstattung nach Aufhebung

Aus einer bereits abgegebenen Steuererklärung ist eine Erstattung von 18.700,00 Euro möglich, deren Entstehung und Höhe zum Schlusstermin noch nicht feststehen. Der Skill rechnet den Betrag nicht als vorhandene Masse ein und zieht ihn nicht als freie Rückstellung vom Verteilungsbetrag ab. Er dokumentiert Steuerzeitraum, Massezugehörigkeit, Berechnungsgrundlage, Bearbeitungsstand und Kosten im Schlussbericht und bereitet, soweit die rechtliche Prüfung dies trägt, nach Feststehen des Anspruchs einen Antrag auf Nachtragsverteilung nach Paragraf 203 InsO vor.

### 6.5 Vollzug mit menschlicher Freigabe

Gerichtliche Zustimmung, Schlusstermin und bereinigtes Schlussverzeichnis liegen vor; sämtliche Bankverbindungen sind unabhängig bestätigt. Der Skill erzeugt die finale Zahlungsliste und das Vier-Augen-Protokoll. Erst nachdem die namentlich zuständige Person genau diese Version freigegeben hat, darf der autorisierte Zahlungsweg ausgelöst werden. Anschließend werden Bankauszug, Buchhaltung und Verzeichnis centgenau abgeglichen und der Vollzugsbericht für die Aufhebung nach Paragraf 200 InsO erstellt.
