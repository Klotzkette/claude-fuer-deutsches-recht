---
name: berichte-fristen-und-verteilung
description: "Führt die Sachbearbeitung vom belegten Zwischenbericht über Schlussbericht, Schlussrechnung und Schlussverzeichnis bis zu Verteilung, Aufhebungsnachbereitung und Nachtragsverteilung. Erzeugt abgestimmte Produkte, Fristenregister und menschliche Freigabevorlagen."
---

# Berichte, Fristen, Verteilung und Verfahrensabschluss bearbeiten

## 1. Zweck und Anwendungsfall

Dieser Skill führt einen eröffneten Insolvenzvorgang vom Zwischenbericht bis zum belegten Abschluss weiter. Er erstellt den konkret bestellten Zwischenbericht, das Fristenregister, die Abschlussreifeprüfung, den Schlussbericht, die Schlussrechnung, das Schlussverzeichnis, die Verteilungs- und Auszahlungsvorlage, die Aufhebungsnachbereitung oder das Paket für eine Nachtragsverteilung. Er beginnt mit dem vorhandenen Aktenstand und schreibt frühere Produkte unter stabilen Kennungen fort.

Die Produkte erfüllen verschiedene Aufgaben und bleiben getrennt. Der Zwischenbericht erklärt die Entwicklung in einem bestimmten Zeitraum. Der Schlussbericht erläutert den Verfahrensverlauf und die noch entscheidungserheblichen Abschlussfragen. Die Schlussrechnung weist Einnahmen, Ausgaben und Bestand mit Belegen nach. Das Schlussverzeichnis ist die für die Schlussverteilung bestimmte Fassung des Verteilungsverzeichnisses. Die Ausschüttung bezeichnet hier nur den technisch ausgeführten Auszahlungslauf der rechtlich freigegebenen Verteilung. Der Aufhebungsbeschluss und die Anordnung einer Nachtragsverteilung sind gerichtliche Entscheidungen; ein Entwurf, eine Einreichung oder ein Zahlungsauftrag ersetzt sie nicht.

Sachbearbeitung sammelt, ordnet, rechnet und bereitet Entscheidungen vor. Die verantwortliche Insolvenzverwalterin oder der verantwortliche Insolvenzverwalter prüft und genehmigt die fachliche Fassung. Ein bestellter Gläubigerausschuss, die Gläubigerversammlung und das Insolvenzgericht nehmen nur die ihnen gesetzlich oder durch Beschluss zugewiesenen Aufgaben wahr. Die KI reicht nichts ein, löst keine Zahlung aus, erklärt keinen Verzicht, ändert keinen gerichtlichen Tabellenstand und behauptet keinen Vollzug ohne Nachweis.

Der Skill ist für Regelverfahren und, nach ausdrücklicher Rollen- und Normprüfung, für entsprechend gelagerte Abschlussarbeiten in anderen Verfahrensarten bestimmt. Endet das Verfahren aufgrund eines Insolvenzplans, einer Masseunzulänglichkeit oder einer sonstigen besonderen Beendigungsroute, wird diese Weiche zuerst geklärt; die hier beschriebene Schlussverteilung wird nicht schematisch übertragen.

## 2. Eingaben

### 2.1 Reproduzierbarer Auftragsdatensatz

Lesen Sie zuerst die vorhandenen Unterlagen. Legen Sie anschließend den folgenden internen Datensatz an und übernehmen Sie nur belegte Angaben. Eine bereits beantwortete Frage wird nicht erneut gestellt.

```text
Verfahren: [interne Kennung, Gericht, Aktenzeichen, genaue Schuldnerperson]
Rolle: [Verwaltung, Eigenverwaltung, Sachwaltung oder andere belegte Rolle]
Verantwortliche Person: [Name und Entscheidungsbefugnis]
Auftrag: [genaues Produkt und Empfänger]
Verfahrensphase: [Berichtsphase, Abschlussvorbereitung, Schlussverteilung, Aufhebung oder Nachtragsverteilung]
Berichtszeitraum: [von TT.MM.JJJJ bis TT.MM.JJJJ]
Rechenstichtag: [TT.MM.JJJJ, Uhrzeit falls erforderlich]
Forderungsstichtag: [Stand der Tabelle oder des Protokolls]
Kontenstichtag: [Stand jedes Massekontos und jeder Kasse]
Maßgebliche Beschlüsse: [Datum, Tenor, Zustellung oder Bekanntmachung, Belegstelle]
Führende Fassungen: [Produktkennung, Datei, Version und Datum]
Offene Entscheidungen: [Frage, Auswirkung, zuständige Person und Frist]
Außenhandlung: [keine oder genau bezeichnete Einreichung, Bekanntmachung, Zahlung oder Mitteilung]
Freigabestand: [Entwurf, fachlich freigegeben, zur Außenhandlung freigegeben oder ausgeführt und belegt]
```

Berichts-, Rechen- und Forderungsstichtag dürfen voneinander abweichen, müssen dann aber im Produkt sichtbar getrennt werden. Jede Zahl erhält Währung, Vorzeichen, Zeitraum, Quelle und Belegstelle. Unbekannte Beträge bleiben offen; sie werden weder mit null angesetzt noch in eine Sammelposition verschoben.

### 2.2 Eingangsprodukte und Mindestunterlagen

| Eingang | Mindestinhalt | Verwendung in dieser Route |
| --- | --- | --- |
| `VERF` Verfahrensblatt und Beschlussvermerk | Verfahrensphase, Beschlusstenor, Termine, Zustellungs- und Bekanntmachungsnachweise | bestimmt Zuständigkeit, Fristauslöser, gerichtliche Zustimmung und später die belegte Aufhebung |
| `FORD-P` Prüfvermerke und belegter Tabellenstand | Forderungskennung, Gläubiger, Rang, festgestellter Betrag, Widerspruch, Titel, gerichtlicher Stand | bildet die Forderungsbasis; ein interner Prüfvorschlag ist kein Ersatz |
| `SICH` Sicherheiten- und Ausfallvermerk | Sicherheit, Verwertungszuständigkeit, Erlös, Verzicht oder nachgewiesener Ausfall | verhindert Doppelbefriedigung und steuert die Behandlung nach Paragraf 190 InsO |
| `KASSE` Abstimmung und Zahlungsvorlage | Massekonten, Kasse, Buchhaltung, Einzelbelege, offene Massepositionen, Zahlungsnachweise | bildet Schlussrechnung, verfügbare Mittel und Auszahlungskontrolle |
| `EIG` Eigentums- und Herausgabevorlage | Gegenstand, Eigentum, Bestand, Verwertung oder Herausgabe | klärt, ob ein Gegenstand Masse, fremdes Vermögen oder noch unverwertbar ist |
| `BETR` Betriebs- und Personalvorlage | offene Verträge, Personal-, Steuer- und Abrechnungsvorgänge | liefert noch zu erfüllende Pflichten, Erlöse, Kosten und Abgrenzungen |
| frühere `BER`-Produkte | frühere Berichte, Prognosen, Verzeichnisse, Rechnungen und Freigaben | ermöglicht Soll-Ist-Vergleich, Fortschreibung und Versionskontrolle |

Zusätzlich werden die gerichtliche Berichtsanordnung oder der konkrete gerichtliche Hinweis, der letzte Zwischenbericht, das aktuelle Masseverzeichnis, Kontoauszüge bis zum Rechenstichtag, Haupt- und Nebenbücher, Kassenunterlagen, Belegindex, Verwertungsabrechnungen, Steuerstände, Gerichts- und Vergütungsentscheidungen, Kostenrechnungen, offene Prozesse sowie Rückstellungen oder zurückzubehaltende Beträge benötigt. Für jede beabsichtigte Zahlung werden Empfängeridentität und Bankverbindung aus einer hierfür geeigneten, kontrollierten Quelle geführt; Zahlungsdaten werden nicht ungeprüft aus einer neuen E-Mail übernommen.

### 2.3 Fristenregister und Datenzustände

Das Fristenregister enthält für jeden Eintrag eine stabile Kennung, Fristart, Rechtsgrund oder gerichtliche Anordnung, auslösendes Ereignis, Auslösernachweis, Berechnung, Beginn, Ende, Vorfrist, verantwortliche Person, abhängiges Produkt und Erledigungsnachweis. Gesetzliche Frist, gerichtlicher Termin und interne Wiedervorlage stehen in getrennten Zeilen. Zustellung, öffentliche Bekanntmachung, Niederlegung und tatsächliche Kenntnis werden nicht ausgetauscht.

Jede Tatsache und jeder Rechenwert erhält einen der Zustände `belegt`, `streitig`, `rechnerisch abgeleitet`, `Prognose` oder `offen`. Eine Prognose wird beim nächsten Bericht mit dem tatsächlichen Ergebnis verglichen. Eine neue Unterlage ändert nur die davon abhängigen Texte, Tabellenzeilen, Summen, Fristen und Übergaben; die frühere führende Fassung bleibt als ersetzt erkennbar.

### 2.4 Rollen- und Freigabematrix

| Rolle | Aufgabe | Freigabegrenze |
| --- | --- | --- |
| Sachbearbeitung | Akte lesen, Belege zuordnen, Berichte und Tabellen fortschreiben, Abgleiche rechnen und Entscheidungsvorlagen erstellen | darf keinen gerichtlichen Stand, Verzicht, Zahlungsvollzug oder Beschluss erzeugen |
| Buchhaltung oder Zahlungsverkehr | Konten, Kasse, Hauptbuch und Belege abstimmen; den exakt freigegebenen Zahlungslauf technisch ausführen | darf Betrag, Empfänger oder Fassung nicht eigenmächtig ändern |
| verantwortliche Insolvenzverwalterin oder verantwortlicher Insolvenzverwalter | rechtliche Einordnung, Schlussprodukte, Einreichung und Auszahlung fachlich und persönlich freigeben | menschliche Freigabe muss Person, Fassung, Handlung und Empfänger bezeichnen |
| Gläubigerausschuss, soweit bestellt | Geldverkehr überwachen, zur Schlussrechnung Stellung nehmen und vor Verteilungen zustimmen | tatsächlicher Beschluss oder tatsächliche Stellungnahme ist nachzuweisen |
| Gläubigerversammlung | Schlussrechnung erörtern, Einwendungen gegen das Schlussverzeichnis erheben und über nicht verwertbare Gegenstände entscheiden | Termin und Entscheidung werden nicht aus einem Entwurf abgeleitet |
| Insolvenzgericht | Schlussrechnung prüfen, Schlussverteilung genehmigen, Schlusstermin bestimmen, über Einwendungen entscheiden, Verfahren aufheben und Nachtragsverteilung anordnen | nur der tatsächliche gerichtliche Beschluss oder Vermerk trägt den jeweiligen Status |

## 3. Ablauf und Checkliste

### 3.1 Auftrag, Stichtage und Fassungen sperren

Bestimmen Sie zuerst das konkret benötigte Produkt. Wenn nur ein Zwischenbericht bestellt ist, erstellen Sie keine ungefragte Schlussrechnung. Wenn Abschlussarbeiten beauftragt sind, legen Sie eine Produktfolge mit Verantwortlichen und Abhängigkeiten an. Sichern Sie zu Beginn eine schreibgeschützte Ausgangsfassung der übernommenen Tabellen und Rechnungen; arbeiten Sie in einer neuen, eindeutig bezeichneten Fassung.

Gleichen Sie Schuldnerperson, Gericht, Aktenzeichen, Kontoinhaber, Währung und Berichtszeitraum über alle Eingangsprodukte ab. Bei einem Widerspruch erstellen Sie eine kurze Abweichungsmatrix mit beiden Quellen, der Auswirkung und der benötigten Entscheidung. Nur die betroffene Freigabe bleibt gesperrt; unabhängige Teile werden weiterbearbeitet.

### 3.2 Zwischenbericht und Fristen fortschreiben

Erstellen Sie den Zwischenbericht aus dem letzten freigegebenen Stand und den Bewegungen des neuen Zeitraums. Stellen Sie Vermögens- und Verwertungsentwicklung, Betrieb oder Stilllegung, Forderungstabelle, Sicherheiten und Ausfälle, Prozesse, Steuern, Kosten, Masseverbindlichkeiten, Kontenstand, wesentliche Gläubigerkontakte und die nächsten Maßnahmen dar. Jeder erhebliche Betrag verweist auf Rechnung, Liste oder Beleg. Ein Bericht besteht nicht nur aus Tabellen; er erklärt Abweichungen, Risiken, getroffene menschliche Entscheidungen und den nächsten konkreten Arbeitsschritt in vollständigen Sätzen.

Führen Sie für jede wesentliche Position den bisherigen Berichtswert, Zugang, Abgang, neuen Stand und die Abweichungsbegründung. Vergleichen Sie frühere Erlös-, Kosten- und Quotenschätzungen mit tatsächlichen Ergebnissen. Spätere Erkenntnisse werden als Nachtrag oder neue Berichtsperiode kenntlich gemacht und nicht rückwirkend als am alten Stichtag bekannt dargestellt.

Aktualisieren Sie parallel das Fristenregister. Für Verteilungen sind insbesondere die öffentliche Bekanntmachung des Verteilungsverzeichnisses, die zweiwöchige Ausschlussfrist nach Paragraf 189 Absatz 1 InsO, die Dreitagesfrist nach Paragraf 193 InsO und die terminierten gerichtlichen Schritte einzeln zu berechnen. Bei einer Abschlagsverteilung wird die besondere Einwendungsfrist des Paragrafen 194 Absatz 1 InsO nicht mit Einwendungen gegen das Schlussverzeichnis im Schlusstermin vermischt.

### 3.3 Abschlussreife prüfen

Erstellen Sie vor Schlussbericht und Schlussrechnung eine Abschlussreifematrix. Eine grüne Gesamtfreigabe setzt voraus, dass die Verwertung im Sinn von Paragraf 196 Absatz 1 InsO beendet ist, soweit nicht laufendes Einkommen ausgenommen ist, und dass jede noch offene Position ausdrücklich behandelt wird. Prüfen Sie mindestens die folgenden Abgleiche:

| Prüfkreis | Abgleich | Sperre bei Abweichung |
| --- | --- | --- |
| Massegegenstände | Masseverzeichnis gegen Verwertungs-, Herausgabe- und Ausbuchungsnachweise | ungeklärter Gegenstand, fehlender Erlös oder ungeklärtes Fremdeigentum |
| Forderungseinzug | Debitoren- und Prozessliste gegen Zahlungseingänge, Vergleiche und Ausbuchungsentscheidungen | offener Anspruch ohne dokumentierte Fortführung oder Entscheidung |
| Sicherheiten | Sicherheitenvermerk gegen Erlösabrechnung, Zahlung und nachgewiesenen Ausfall | ungeklärter Ausfall, doppelte Erlösanrechnung oder offener Verzicht |
| Forderungstabelle | gerichtlicher Stand gegen Schlussverzeichnis | interner Vorschlag statt belegter Feststellung, unklarer Rang oder offene Identität |
| Massekosten und Masseverbindlichkeiten | offene Posten gegen Rechnung, Freigabe, Zahlung oder belegte Berücksichtigung | ungedeckte oder unklassifizierte Position |
| Steuern und Vergütung | Bescheide, Anmeldungen und gerichtliche Festsetzung gegen Buchhaltung | offener Betrag mit Einfluss auf die Verteilungsmasse |
| Geldbestand | Bank und Kasse gegen Buchhaltung und Schlussrechnung | ungeklärte Differenz oder Buchung ohne Beleg |
| nicht verwertbare Gegenstände | Bestandsliste gegen Entscheidungsvorlage für den Schlusstermin | Gegenstand ohne Beschreibung, Wertansatz und vorgeschlagene Behandlung |

Kennzeichnen Sie jeden Prüfkreis als `grün`, `gelb` oder `rot` und begründen Sie die Farbe. `Gelb` ist nur zulässig, wenn die Abschlussroute rechtlich und rechnerisch trotz der offenen Position darstellbar ist, etwa durch einen konkret begründeten Rückbehalt oder eine Entscheidung über einen nicht verwertbaren Gegenstand. `Rot` sperrt Schlussverzeichnis oder Auszahlung. Eine pauschale Reserve heilt keine ungeklärte Forderungs-, Eigentums- oder Rangfrage.

### 3.4 Schlussbericht und Schlussrechnung erstellen

Erstellen Sie Schlussbericht und Schlussrechnung als getrennte, aufeinander abgestimmte Produkte. Der Schlussbericht enthält Verfahrenschronologie, Masseermittlung und -realisierung, Betriebs- und Personalabschluss, Forderungseinzug, Anfechtungs- und Haftungsvorgänge, Aus- und Absonderung, Forderungstabelle, Kosten und Masseverbindlichkeiten, offene beziehungsweise nicht verwertbare Gegenstände, Ergebnis der Abschlussreifeprüfung und den Vorschlag für die Schlussverteilung. Umfang und Adressierung eines gesonderten Schlussberichts richten sich nach dem konkreten gerichtlichen Auftrag oder Kanzleistandard; die gesetzliche Schlussrechnung wird dadurch nicht ersetzt.

Die Schlussrechnung führt jede Einnahme und Ausgabe aus einem nachvollziehbaren Anfangsbestand bis zum Schlussbestand. Sammelzeilen erhalten eine rückverfolgbare Unterrechnung und einen Belegindex. Stimmen Sie für jedes Konto Anfangsbestand zuzüglich Zugänge abzüglich Abgänge mit Endbestand ab. Stimmen Sie anschließend die Summe aller Konten und Kassen mit Hauptbuch und ausgewiesenem Schlussbestand ab. Erlöse aus belasteten Gegenständen, Fremdgeld, durchlaufende Posten, Umsatzsteuerbezüge, Vergütung, Gerichtskosten und sonstige Masseverbindlichkeiten werden nicht in einer unbenannten Nettoposition verborgen.

Die verantwortliche Person prüft die rechtliche Einordnung und die führende Rechnung. Ist ein Gläubigerausschuss bestellt, bereiten Sie die Unterlagen so vor, dass seine Bemerkungen zur Schlussrechnung und seine Prüfung des Geldverkehrs nachvollziehbar dokumentiert werden können. Die gerichtliche Prüfung nach Paragraf 66 Absatz 2 InsO und die Erörterung im Schlusstermin bleiben tatsächliche spätere Verfahrensschritte.

### 3.5 Schlussverzeichnis und Quotenrechnung abstimmen

Leiten Sie das Schlussverzeichnis aus dem belegten gerichtlichen Forderungsstand ab. Führen Sie mindestens Forderungskennung, Tabellenblatt oder laufende Nummer, Gläubigeridentität, Rang, berücksichtigungsfähigen Betrag, Grund der Berücksichtigung, Widerspruchs- oder Nachweisstatus, Sicherheit und Ausfall, Bedingung, Rückbehalt oder Hinterlegung, Quote, rechnerischen Auszahlungsbetrag und Rundungsdifferenz. Zahlungsdaten stehen in einer gesonderten, kontrollierten Zahlungsliste und ändern den rechtlichen Inhalt des Schlussverzeichnisses nicht.

Bereiten Sie den Vorgang nach Paragraf 188 InsO vollständig vor: Verzeichnis zur Niederlegung auf der Geschäftsstelle, Anzeige der Forderungssumme und des verfügbaren Massebetrags an das Insolvenzgericht sowie Erfassung der späteren öffentlichen Bekanntmachung durch das Gericht. Ein eigener Entwurf oder Übermittlungsnachweis wird nicht als gerichtliche Niederlegung oder Bekanntmachung bezeichnet.

Prüfen Sie bestrittene Forderungen nach Paragraf 189 InsO, Absonderungsrechte und Ausfallnachweise nach Paragraf 190 InsO, aufschiebend bedingte Forderungen nach Paragraf 191 InsO sowie eine nachträgliche Gleichstellung nach vorausgegangener Abschlagsverteilung nach Paragraf 192 InsO. Nehmen Sie die aufgrund dieser Prüfung erforderlichen Änderungen innerhalb der Frist des Paragrafen 193 InsO in einer neuen Fassung vor. Eine Gläubiger- oder Forderungsänderung wird nicht allein durch Überschreiben der Bezeichnung erledigt; sie geht mit Anmelde-, Prüfungs- und Identitätsbelegen zurück an `FORD-P`.

Rechnen Sie jede Rangklasse getrennt. Die Rechenkontrolle weist mindestens aus:

```text
Verfügbarer Verteilungsbetrag
= belegter freier Geldbestand
- noch vorweg zu berichtigende Kosten und Masseverbindlichkeiten
- rechtlich gebundene oder zurückzubehaltende Beträge
- konkret belegte Kosten des Verteilungsvollzugs

Quote je Rangklasse
= für diese Rangklasse verfügbarer Betrag / Summe der berücksichtigungsfähigen Forderungen dieser Rangklasse

Kontrollsumme
= Auszahlungsbeträge + Rückbehalte oder Hinterlegungen + ausgewiesener Rundungsrest
= freigegebener Verteilungsbetrag
```

Jeder Abzug wird einzeln bezeichnet und belegt. Der Rechenweg arbeitet mit ungerundeten Zwischenwerten; Währung und Rundungsregel werden dokumentiert. Eine plausible Prozentzahl genügt nicht, wenn Forderungsbasis, Rang oder freier Geldbestand nicht stimmen. Können alle Insolvenzforderungen vollständig berichtigt werden, wird ein verbleibender Überschuss nach Paragraf 199 InsO gesondert berechnet und nicht als zusätzliche Gläubigerquote verteilt.

### 3.6 Gerichtliches Abschluss- und Freigabepaket vorbereiten

Stellen Sie Schlussbericht, Schlussrechnung samt Belegindex, Abschlussreifematrix, Schlussverzeichnis, Quotenrechnung, Liste nicht verwertbarer Gegenstände und interne Entscheidungsnotiz in derselben führenden Version zusammen. Weisen Sie vor jeder Verteilung nach, dass der allgemeine Prüfungstermin stattgefunden hat; ohne diesen Nachweis darf die Befriedigung der Insolvenzgläubiger nach Paragraf 187 Absatz 1 InsO nicht beginnen. Die verantwortliche Insolvenzverwalterin oder der verantwortliche Insolvenzverwalter erteilt die fachliche Freigabe. Einreichung beim Gericht ist eine gesonderte Außenhandlung und benötigt die konkrete Freigabe für Fassung, Empfänger und Übermittlungsweg.

Dokumentieren Sie nach tatsächlichem Rücklauf die gerichtliche Prüfung der Schlussrechnung, die Zustimmung zur Schlussverteilung, den Schlusstermin, die öffentliche Bekanntmachung, die Einsichtszeiträume und die Entscheidungen über Einwendungen. Paragraf 66 Absatz 2 InsO sieht zwischen Auslegung der dort genannten Unterlagen und Gläubigerversammlung einen Zeitraum von mindestens einer Woche als Sollvorgabe vor. Paragraf 197 Absatz 2 InsO sieht zwischen öffentlicher Bekanntmachung des Schlusstermins und Termin grundsätzlich mindestens einen und höchstens zwei Monate vor. Berechnen Sie diese Zeiträume aus dem belegten Ereignis; ein vorbereiteter Kalendervermerk beweist keine Bekanntmachung.

Vor jeder Verteilung ist bei bestehendem Gläubigerausschuss dessen Zustimmung nach Paragraf 187 Absatz 3 InsO nachzuweisen. Die Schlussverteilung benötigt zusätzlich die Zustimmung des Insolvenzgerichts nach Paragraf 196 Absatz 2 InsO. Einwendungen gegen das Schlussverzeichnis werden im Schlusstermin erhoben; gerichtliche Berichtigungen und offene Entscheidungen werden in Schlussverzeichnis, Rechnung und Zahlungsliste synchron fortgeschrieben. Jede Änderung nach fachlicher oder gerichtlicher Freigabe erzeugt eine neue Fassung und eine erneute Freigabe der betroffenen Produkte.

### 3.7 Verteilung und Auszahlung vollziehen

Erstellen Sie erst nach Erfüllung der Verfahrensvoraussetzungen den Auszahlungslauf. Die Zahlungsvorlage nennt Verfahrenskennung, freigegebene Fassung des Schlussverzeichnisses, Gläubigerkennung, Empfänger, verifizierte Bankverbindung, Betrag, Quote, Rechtsgrund, Zahlungszweck und Freigabevermerk. Eine zweite menschliche Person kontrolliert bei hierfür vorgesehenem Vier-Augen-Verfahren mindestens Empfänger, Bankverbindung, Betrag, Summe und führende Fassung. Die zahlungsbefugte Person gibt genau diesen Lauf frei.

Nach Ausführung ordnen Sie jeder Position Bankbeleg, Buchungsdatum, Valuta, Betrag und Status `ausgeführt`, `zurückgewiesen`, `zurückgelaufen` oder `offen` zu. Klären Sie Rückläufer und unklare Empfängerzuordnungen, bevor Restbeträge anderweitig behandelt werden. Bei der Schlussverteilung zurückzubehaltende Beträge werden nach Paragraf 198 InsO für Rechnung der Beteiligten bei einer geeigneten Stelle hinterlegt. Behaupten Sie eine Hinterlegung nur mit tatsächlichem Nachweis.

Führen Sie abschließend den Bank-Buchhaltung-Verteilungsabgleich durch. Die Summe belegter Zahlungen, Hinterlegungen, Rückläufer und des verbliebenen Kontostands muss die freigegebene Verteilungsrechnung erklären. Ein Zahlungsauftrag oder Export ist kein Zahlungsnachweis.

### 3.8 Aufhebung nachbereiten

Erstellen Sie nach vollzogener Schlussverteilung `BER-AUF`, bestehend aus Vollzugsmitteilung, Schlussbestandsabgleich, Liste der Hinterlegungen und Rückläufer, offenen Nacharbeiten sowie einer Übergabe an `VERF`. Das Insolvenzgericht beschließt die Aufhebung nach Paragraf 200 Absatz 1 InsO; die Sachbearbeitung setzt weder Aufhebungsdatum noch Rechtswirkungen aus eigener Bewertung.

Erst nach Eingang des tatsächlichen Aufhebungsbeschlusses erfassen Sie Beschlussdatum, öffentlichen Bekanntmachungsnachweis, gegebenenfalls Zustellungen und angeordnete Folgehandlungen. Schließen Sie Konten, Register-, Steuer-, Archiv- und Korrespondenzvorgänge nur im Umfang der belegten Zuständigkeit und führen Sie mögliche Nachtragsgegenstände in einer Beobachtungsliste fort. Der Status lautet erst dann `aufgehoben und belegt`.

### 3.9 Nachtragsverteilung bearbeiten

Legen Sie für jeden späteren Betrag oder Gegenstand einen neuen Vorgang unter derselben Verfahrenskennung an. Dokumentieren Sie Funddatum, Quelle, rechtliche und zeitliche Massezugehörigkeit, Bruttowert, Verwertungskosten, erwarteten Nettoerlös, früheren Schlussverzeichnisstand und die zuständige Person. Eine spätere Auszahlung, Steuererstattung, Abfindung oder Rückzahlung gehört nicht allein wegen ihres Zuflussdatums zur Masse.

Prüfen Sie, ob ein Fall des Paragrafen 203 Absatz 1 InsO vorliegt: Ein zurückbehaltener Betrag wird frei, eine aus der Masse gezahlte Summe fließt zurück oder ein Massegegenstand wird nach dem Schlusstermin ermittelt. Bereiten Sie je nach Rolle einen ausformulierten Antrag oder eine Anregung samt Belegen und Kostenbetrachtung vor. Die Aufhebung hindert die gerichtliche Anordnung nicht. Das Gericht kann bei geringem Wert und unverhältnismäßigen Kosten von der Anordnung absehen oder einen Kostenvorschuss verlangen; diese Entscheidung wird nicht vorweggenommen.

Nach tatsächlicher gerichtlicher Anordnung verwerten und verteilen Sie nur im angeordneten Umfang. Paragraf 205 InsO bindet den Vollzug an das Schlussverzeichnis und verlangt Rechnungslegung gegenüber dem Insolvenzgericht. Gleichen Sie zwischenzeitliche Identitäts-, Rechtsnachfolge- und Zahlungsdatenfragen gesondert ab, ohne die festgestellte Forderungsbasis still zu verändern. Das Produkt endet mit Nachtragsrechnung, Auszahlungsjournal, Bankabgleich und gerichtlicher Rechnungslegung; ein bloßer Zahlungseingang ist kein abgeschlossener Nachtragsvorgang.

### 3.10 Qualitätsgates

| Gate | Muss-Nachweis | Stoppt |
| --- | --- | --- |
| `Q1 Akte und Version` | Verfahren, Rolle, Stichtage, führende Fassungen und Belegstellen stimmen überein | jede Empfängerfassung bei falscher Zuordnung |
| `Q2 Abschlussreife` | jeder Vermögens-, Prozess-, Sicherheiten-, Steuer- und Masseposten ist erledigt oder konkret behandelt | Schlussverzeichnis bei roter Position |
| `Q3 Dreifachabgleich` | Bank und Kasse, Buchhaltung und Schlussrechnung ergeben denselben erklärten Bestand | Quotenfreigabe und Zahlung |
| `Q4 Forderungsbasis` | gerichtlicher Stand, Rang, Paragrafen 189 bis 192 InsO und frühere Abschläge sind abgeglichen | Schlussverzeichnis und Quote |
| `Q5 Verfahrensfreigaben` | allgemeiner Prüfungstermin, Niederlegung und Bekanntmachung, Ausschusszustimmung soweit erforderlich, gerichtliche Zustimmung zur Schlussverteilung und Einwendungsstand sind belegt | Auszahlungslauf |
| `Q6 Menschliche Zahlungsfreigabe` | genaue Fassung, Empfänger, Bankverbindung, Betrag und Freigebende sind dokumentiert | technische Zahlung |
| `Q7 Vollzug` | Bankbelege, Rückläufer, Hinterlegungen und Restbestand gehen rechnerisch auf | Aufhebungsübergabe |
| `Q8 Nachtrag` | Massezugehörigkeit, gerichtliche Anordnung, Schlussverzeichnis und Nachtragsrechnung sind belegt | Nachtragsauszahlung und Abschlussmeldung |

## 4. Quellenpflicht

### 4.1 Normen und gerichtliche Anordnung

Prüfen Sie für jeden konkreten Auftrag die aktuelle amtliche Fassung und den zeitlichen Anwendungsbereich. Paragrafen 53 bis 55 InsO tragen die Vorwegberichtigung von Verfahrenskosten und sonstigen Masseverbindlichkeiten. Paragraf 64 InsO betrifft die gerichtliche Festsetzung von Vergütung und Auslagen. Paragraf 66 InsO regelt Schluss- und Zwischenrechnungslegung; Paragraf 69 InsO die Unterstützungs- und Überwachungsaufgaben des Gläubigerausschusses einschließlich der Prüfung von Geldverkehr und -bestand. Paragrafen 187 bis 195 InsO regeln Verteilungsbeginn, Verteilungsverzeichnis, bestrittene und gesicherte Forderungen, Bedingungen, nachträgliche Gleichstellung, Verzeichnisänderung, Einwendungen und bei Abschlagsverteilungen den Bruchteil. Paragrafen 196 bis 200 InsO regeln Schlussverteilung, Schlusstermin, Hinterlegung, Überschuss und Aufhebung. Paragrafen 203 und 205 InsO regeln Anordnung und Vollzug der Nachtragsverteilung.

Die InsO nennt die Schlussrechnung und das Schlussverzeichnis ausdrücklich. Inhalt und Bezeichnung eines zusätzlichen Schlussberichts richten sich nach der konkreten gerichtlichen Anforderung und dem belegten Kanzleistandard. Eine örtliche Praxis, ein Formular oder eine gerichtliche Verfügung wird nur übernommen, wenn sie für dieses Verfahren vorliegt. Testakten sind Arbeitsbeispiele und keine Rechtsquellen.

### 4.2 Verifizierte Entscheidungsanker

BGH, Beschl. v. 11.11.2021 – Az. IX ZB 19/20, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2020/IX_ZB__19-20.pdf?__blob=publicationFile&v=1), Rn. 12 und 14–21, trägt die Abschlussreifeprüfung: Eine vorgelegte Schlussrechnung oder ein abgehaltener Schlusstermin genügt bei fortdauernder Verwertung nicht; die Tätigkeit muss grundsätzlich erledigt sein, und vor der Vergütungsfälligkeit kommt nur ein Vorschuss nach Paragraf 9 InsVV in Betracht. Die Entscheidung trägt keine zeitabschnittsweise Teilfestsetzung und macht nicht jeden späteren Massezufluss zu einem Fehler der Schlussrechnung.

BGH, Urt. v. 09.03.2017 – Az. IX ZR 177/15, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2015/IX_ZR_177-15.pdf?__blob=publicationFile&v=1), Rn. 15–17, trägt die Trennung zwischen voller Forderungsanmeldung und Teilnahme eines absonderungsberechtigten Gläubigers an der Verteilung nach Paragraf 190 InsO. Die Entscheidung trägt weder eine Doppelbefriedigung noch den Abzug eines nur geschätzten Sicherungserlöses als feststehenden Ausfall.

BGH, Beschl. v. 26.09.2024 – Az. IX ZB 5/24, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2024/IX_ZB___5-24.pdf?__blob=publicationFile&v=1), Rn. 6–15, bestätigt, dass Restschuldbefreiung eine Nachtragsverteilung von Massegegenständen nicht hindert und dass die Massezugehörigkeit einer späteren Steuererstattung nach ihrem Entstehungsgrund und zeitlichen Anteil zu prüfen ist. Die Entscheidung trägt keine pauschale Massezuordnung jeder später ausgezahlten Steuererstattung und betraf das im dortigen Verfahren anwendbare ältere Recht.

BGH, Beschl. v. 21.05.2026 – Az. IX ZB 45/25, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2025/IX_ZB__45-25.pdf?__blob=publicationFile&v=1), Rn. 7–17, 19–29 und 33–36, bestätigt die Antragsbefugnis des früheren Insolvenzverwalters für eine Nachtragsverteilung nach Aufhebung und trennt diese Rolle von derjenigen des Treuhänders. Die Entscheidung trägt weder eine allgemeine Antragsbefugnis des Treuhänders für jede Nachtragsverteilung noch die Annahme, der Auszahlungszeitpunkt entscheide allein über die Massezugehörigkeit.

BGH, Beschl. v. 20.11.2014 – Az. IX ZB 16/14, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2014/IX_ZB__16-14.pdf?__blob=publicationFile&v=1), Rn. 11–21, trägt den Ausgangspunkt, dass nach Berichtigung der Masseverbindlichkeiten grundsätzlich die gesamte verwertete Masse zu verteilen ist. Die dort anerkannte Rückstellung für voraussichtlich ungedeckte Kosten der Wohlverhaltensperiode ist eine enge Ausnahme bei natürlichen Personen und keine allgemeine Ermächtigung für pauschale Sicherheitsabschläge oder Liquiditätspuffer.

BGH, Beschl. v. 24.03.2022 – Az. IX ZB 35/21, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2021/IX_ZB__35-21.pdf?__blob=publicationFile&v=1), Rn. 7–13, trennt den Abschluss nach Paragraf 211 InsO von der regulären Schlussverteilung: Dort findet keine Schlussverteilung nach Paragraf 196 InsO und kein förmlicher Schlusstermin nach Paragraf 197 InsO statt. Die Entscheidung trägt die Verfahrensweiche bei Masseunzulänglichkeit, nicht die materielle Einordnung jeder einzelnen Masseverbindlichkeit.

Die [Rechtsquellenreferenz](../../references/rechtsquellen.md) dokumentiert die amtlichen Links, gelesenen Bereiche, Aussagen und Grenzen dieser Entscheidungen. Befolgen Sie die [Zitierweise](../../references/zitierweise.md). Vor produktiver Verwendung prüfen Sie Normfassung und tragende Fundstelle erneut. Keine Literatur-, Datenbank- oder Rechtsprechungsfundstelle aus Modellwissen ergänzen. Ist eine tragende Quelle nicht zugänglich, bleibt die betroffene Rechtsfrage ausdrücklich offen; Tatsachenabgleich, Rechnung und unabhängige Textteile werden weiterbearbeitet.

## 5. Ausgabeformat

### 5.1 Vollständig benannte und anschlussfähige Produkte

| Kennung | Vollständiger Produktname | Pflichtbestandteile | Anschluss |
| --- | --- | --- | --- |
| `BER-ZW` | Belegter Zwischenbericht mit Soll-Ist-Abweichungsanalyse | Berichtszeitraum, Einzelstände, Entwicklungen, Risiken, Entscheidungen, nächste Maßnahmen und Anlagenbezug | Fortschreibung aus allen Fachrouten; Übergabe an `BER-AR` oder nächsten `BER-ZW` |
| `BER-FR` | Fristen-, Termin- und Wiedervorlagenregister | Auslöser, Nachweis, Berechnung, Ende, Vorfrist, Verantwortliche, Produkt und Erledigungsbeleg | Rückgabe kritischer Termine an `VERF` und zuständige Fachroute |
| `BER-AR` | Abschlussreife- und Lückenmatrix | sämtliche Prüfkreise, Ampelstatus, Auswirkung, Entscheidung, Verantwortliche und Nachweis | Sperr- oder Freigabegrund für `BER-SB`, `BER-SR` und `BER-SV` |
| `BER-SB` | Ausformulierter Schlussbericht | Verfahrensverlauf, Masse, Verwertung, Forderungen, Sicherheiten, Kosten, Risiken, nicht verwertbare Gegenstände und Schlussvorschlag | gerichtliches Abschluss- und Freigabepaket |
| `BER-SR` | Schlussrechnung mit Kontenabgleich und Belegindex | Anfangsbestände, Einzelbewegungen, Unterrechnungen, Endbestände, Bank-Kasse-Buchhaltung-Abgleich und Belegverzeichnis | gerichtliche Prüfung, Ausschussbemerkungen und `BER-SV` |
| `BER-SV` | Schlussverzeichnis mit Rang-, Rückbehalts- und Quotenrechnung | berücksichtigungsfähige Forderungen, Paragrafen-189-bis-192-Status, Quote, Einzelbeträge, Kontrollsumme und Versionsstand | gerichtliche Zustimmung, Schlusstermin und `BER-AUS` |
| `BER-AUS` | Freigabe- und Vollzugspaket der Schlussverteilung und Ausschüttung | kontrollierte Zahlungsliste, menschliche Freigaben, Bankbelege, Rückläufer, Hinterlegungen und Schlussabgleich | `KASSE`, `BER-AUF` und gerichtliche Vollzugsmitteilung |
| `BER-AUF` | Aufhebungsnachbereitung und Abschlussübergabe | Vollzugsnachweis, Restbestand, Hinterlegungen, offene Nacharbeiten, tatsächlicher Aufhebungsbeschluss und Bekanntmachungsnachweis | `VERF`, Archiv-, Steuer-, Register- und Beobachtungsvorgänge |
| `BER-NV` | Nachtragsverteilungspaket mit Massezuordnungs-, Antrags-, Rechen- und Vollzugsunterlagen | Fundnachweis, Massezugehörigkeit, Kostenprüfung, gerichtliche Anordnung, Schlussverzeichnisbezug, Nachtragsrechnung, Zahlungsjournal und Rechnungslegung | `VERF`, `KASSE`, `FORD-P` bei Identitätsfragen und gerichtliche Abschlussmeldung |

Verwenden Sie für jede führende Fassung das Schema `[Produktkennung]-[Verfahrenskennung]-[Stichtag]-v[Nummer]`. Eine Übergabe nennt Produktkennung, führende Fassung, Bearbeitungsstichtag, maßgebliche Beschlüsse, entscheidende Belege, Original- und Rechenbeträge, Quellenstatus, offene Frage, Frist, verantwortliche Person, nächste Route und Freigabestand.

### 5.2 Ausformulierungspflicht und Formatstandard

Das beauftragte Dokument steht zuerst. Berichte, Vermerke, Anträge, Anregungen, gerichtliche Begleitschreiben und Übergaben werden in vollständigen, grammatikalisch sauberen und prägnanten Sätzen geliefert. Skelette, Halbsätze, leere Textbausteine und reine Aufzählungs-Auswürfe sind als Endprodukt verboten. Tabellen dürfen Zahlen, Zuordnungen und Abgleiche darstellen, ersetzen aber weder Begründung noch konkrete nächste Handlung. Ein bloßes Gerüst wird verworfen und vollständig neu geschrieben. Fehlende Einzelangaben erhalten klar lesbare Platzhalter, während der umgebende Satz vollständig bleibt.

Formatierte Dokumente verwenden, soweit technisch möglich, Times New Roman, 11 pt und ausschließlich dezimale Gliederung. Bei Markdown oder Chat steht der Formatwunsch in einem getrennten Exporthinweis. Amtliche Formulare oder gerichtliche Hausformate dürfen abweichen, wenn die Abweichung aus der tatsächlichen Vorgabe folgt. Technische Quellenprotokolle, interne Ampelfelder und Zugriffshinweise gehören nicht ungefragt in den Empfängertext.

### 5.3 Freigabe- und Vollzugsstatus

Jedes Produkt endet mit einer kurzen internen Notiz. Sie unterscheidet `Entwurf`, `fachlich freigegeben`, `zur bezeichneten Außenhandlung freigegeben` sowie `ausgeführt und belegt`. Die fachliche Freigabe nennt Person und Fassung. Die Außenfreigabe nennt zusätzlich Empfänger, Handlung und Übermittlungs- oder Zahlungsweg. Nach einer inhaltlichen Änderung ist die frühere Freigabe verbraucht. Behaupten Sie keine Einreichung, Zustimmung, Bekanntmachung, Zahlung, Hinterlegung, Aufhebung oder Nachtragsverteilung ohne den jeweiligen tatsächlichen Nachweis.

## 6. Beispiele

### 6.1 Vom Zwischenbericht zur Schlussverteilung

In einem Unternehmensverfahren weist der letzte Zwischenbericht geschätzte Maschinen- und Vergleichserlöse aus. Neue Verkaufsabrechnungen, ein gerichtlicher Vergütungsbeschluss und die aktualisierte Forderungstabelle liegen vor. Der Skill erstellt zunächst `BER-ZW` mit dem Vergleich von Schätzung und tatsächlichem Erlös sowie `BER-AR` mit einer gelben Steuerposition. Nach Eingang des Steuerbescheids werden nur Schlussbestand, Kostenabgrenzung, Quotenrechnung und betroffene Berichtspassagen fortgeschrieben. `BER-SB`, `BER-SR` und `BER-SV` verwenden danach denselben Stichtag und dieselbe Forderungsbasis.

Die zuständige Insolvenzverwalterin gibt diese Fassungen fachlich frei und autorisiert die konkrete Einreichung. Erst nach belegter Ausschusszustimmung, gerichtlicher Zustimmung zur Schlussverteilung, Schlusstermin und erledigten Einwendungen wird `BER-AUS` erstellt. Nach dem Zahlungslauf stimmen Bankbelege, Buchhaltung, Hinterlegungen und Restbestand überein. `BER-AUF` dokumentiert diesen Vollzug und übernimmt später den tatsächlichen Aufhebungsbeschluss; es behauptet die Aufhebung nicht vor dessen Eingang.

### 6.2 Nachtragsverteilung nach Aufhebung

Nach der belegten Aufhebung geht eine Steuererstattung für mehrere Veranlagungszeiträume ein. Der Skill eröffnet `BER-NV` unter der alten Verfahrenskennung und trennt Zuflussdatum, steuerlichen Entstehungsgrund und zeitliche Massezugehörigkeit. Er erstellt keine automatische Quotenüberweisung, sondern einen Massezuordnungsvermerk, die Kostenbetrachtung und den ausformulierten Antrag oder die Anregung an das Insolvenzgericht zur menschlichen Freigabe.

Nach tatsächlicher gerichtlicher Anordnung wird der Nettoverteilungsbetrag auf Grundlage des Schlussverzeichnisses gerechnet. Gläubigeridentität und Zahlungsdaten werden kontrolliert; die festgestellte Forderungsbasis wird nicht still geändert. Der Vorgang endet erst, wenn Nachtragszahlung, Bankabgleich und Rechnungslegung nach Paragraf 205 InsO belegt sind.

### 6.3 Schlussverteilung mit Sicherheit und bestrittenem Anspruch

Zum gemeinsamen Stichtag stehen 250.000,00 Euro auf dem Massekonto. Belegte Masseverbindlichkeiten von 40.000,00 Euro, Gerichtskosten von 10.000,00 Euro, festgesetzte Vergütung von 60.000,00 Euro und eine konkret begründete Steuerrückstellung von 5.000,00 Euro lassen 135.000,00 Euro für die Insolvenzgläubiger verfügbar. Festgestellt sind Forderungen von 900.000,00 Euro. Darin ist eine durch Absonderung gesicherte Forderung von 250.000,00 Euro enthalten; aus der Sicherheit wurden 200.000,00 Euro erlöst, sodass nur der belegte Ausfall von 50.000,00 Euro in die Forderungsbasis eingeht. Die sichere Bemessungsgrundlage beträgt deshalb 700.000,00 Euro.

Zusätzlich ist eine Forderung von 100.000,00 Euro bestritten. Der Gläubiger hat den nach Paragraf 189 InsO erforderlichen Nachweis rechtzeitig geführt. Für die Verteilungsrechnung beträgt die Bemessungsgrundlage damit 800.000,00 Euro und die Quote 16,875 Prozent. Der Skill weist für die unstreitige Basis 118.125,00 Euro zur Auszahlung aus und 16.875,00 Euro als gesetzlich zu behandelnden Rückbehalt. `BER-SV` zeigt Rechenweg, Ausfall, Nachweisstatus und Kontrollsumme; `BER-AUS` bleibt bis zur gerichtlichen Zustimmung, zur Erledigung der Einwendungen und zur dokumentierten menschlichen Zahlungsfreigabe gesperrt.
