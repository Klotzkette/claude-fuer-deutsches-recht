---
name: abrechnung-e-rechnung
description: "Verwenden, wenn aus bestätigtem Honorar- und Leistungsstand eine Rechnung, ein Vorschusstext, eine Korrektur oder eine XRechnung für Unternehmer oder Behörde entstehen soll, B2G-Angaben fehlen oder eine Eingangsrechnung zu prüfen ist. Liefert versandfähigen Rechnungstext. Nicht für Honorargrundlage oder Zahlungen."
---

# Anwaltliche Rechnung und E-Rechnung erstellen

## 1. Zweck und Anwendungsfall

### 1.1. Von der dokumentierten Leistung zur konkreten Rechnung

Dieser Skill führt einen bestätigten Leistungs- und Honorarstand zu einer überprüfbaren Rechnung. Er verbindet anwaltliches Vergütungsrecht, Umsatzsteuer, Empfängeranforderungen und die tatsächliche technische Ausgabe. Das Ergebnis ist je nach Auftrag ein fertiger Rechnungstext, eine geprüfte strukturierte XML-Datei oder eine konkrete Korrekturrechnung. Ein bekannter Teilbetrag aus dem Mandatsjournal wird nicht als vollständige Forderung ausgegeben, solange wesentliche Positionen, Zuordnungen oder Grundlagen offen sind.

Rechtliche Abrechenbarkeit, rechnerische Richtigkeit und technische Konformität sind drei getrennte Prüfungen. Eine XML-Datei kann technisch gültig sein und dennoch den falschen Leistungsempfänger, ein nicht vereinbartes Honorar oder eine unzutreffende Umsatzsteuer enthalten. Umgekehrt kann ein berechtigter Honoraranspruch in einem unzureichenden Format geltend gemacht werden. Der Skill dokumentiert deshalb, was geprüft wurde und welche Frage offen ist, und behauptet keine Freigabe allein aus einem erfolgreichen Export.

### 1.2. Die Rechnung ist kein bloßer Dateityp

Eine PDF-Datei ist eine sonstige Rechnung, keine E-Rechnung im Sinn von [§ 14 Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html). Eine E-Rechnung wird in einem strukturierten elektronischen Format ausgestellt, übermittelt und empfangen und ermöglicht die elektronische Verarbeitung; das Format muss der europäischen Norm für die elektronische Rechnungsstellung entsprechen oder zwischen den Parteien vereinbart sein und die richtige und vollständige Extraktion der Pflichtangaben erlauben. Die lesbare Ansicht erleichtert die Kontrolle, ersetzt die strukturierten Daten aber nicht. Bei hybriden Formaten wie ZUGFeRD ist der XML-Teil führend; eine ansprechend gestaltete Sichtfassung heilt keine falschen XML-Daten.

Die KI-native Kanzlei bereitet die Erstellung vor und führt zulässige Werkzeuge aus. Vergabe der endgültigen Rechnungsnummer, anwaltliche Verantwortungsübernahme, Mitteilung, Buchung und Versand werden als eigenständige Schritte dokumentiert; ein Versand erfolgt nur im Rahmen eines Auftrags. Weder der Dateiname „final“ noch ein internes Freigabefeld beweist den Zugang beim Empfänger.

### 1.3. Auslöser, Abgrenzung und Nachbarskills

Der Skill startet, wenn eine Honorarphase abgeschlossen ist und die Mandantin eine Rechnung erwartet, wenn der Rechtsschutzversicherer eine Berechnung nach § 10 RVG mit Gebührentatbeständen anfordert, wenn ein inländischer Unternehmensmandant ab dem Leistungsjahr 2026 eine XRechnung oder ZUGFeRD-Datei verlangt, wenn eine Behörde als Auftraggeberin Leitweg-ID und Portalweg vorgibt, wenn eine bereits gestellte Rechnung berichtigt oder storniert werden muss oder wenn die Kanzlei selbst eine Eingangsrechnung auf Pflichtangaben und Vorsteuerfähigkeit prüft.

Die Honorargrundlage wird in [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) festgelegt; dieser Skill übernimmt sie als gegeben und ändert sie nicht. Zeiteinträge entstehen in [Zeiten erfassen](../zeiten-erfassen/SKILL.md); hier werden sie nur abgerechnet. Zahlungseingänge, Vorschussverrechnung, Fremdgeld und Buchungsvorschläge gehören zu [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md). Die Schlussabrechnung beim Mandatsende und die Aufbewahrungsentscheidung für die Handakte steuert [Mandat abschließen](../mandat-abschliessen/SKILL.md). Das Anschreiben zur Rechnung mit Sachstand und Empfehlung entsteht in [Mandantenkommunikation](../mandantenkommunikation/SKILL.md). Einen offenen Steuerstreit oder eine unklare Verwaltungsauffassung klärt [Recht recherchieren](../recht-recherchieren/SKILL.md).

Dieser Skill verhandelt kein Honorar, erfasst keine Zeiten, bucht nicht, vollstreckt nicht und versendet nichts ohne Auftrag.

## 2. Eingaben

### 2.1. Führender Honorar- und Leistungsstand

Lies die gültige Vergütungsvereinbarung, Nachträge, Gebührenblatt, bestätigte Zeitbelege, Auslagenbelege, bisherige Rechnungen, Vorschüsse und Zahlungseingänge. Halte die aktuelle Basis knapp vor: „Für die außergerichtliche Prüfung gilt die Vereinbarung vom 1. September 2026 mit 280 Euro netto je tatsächlicher Stunde und einem Gesamtdeckel von 2.500 Euro netto. Bestätigt sind sieben Stunden und 40 Euro eigene steuerpflichtige Auslagen.“ Steht fest, dass der Deckel Auslagen einschließt, wird das nicht erneut gefragt. Eine Rechnung darf eine unklare Preiszusage nicht einseitig in ein offenes Stundenhonorar umdeuten; bekannte Daten dürfen verwendet werden, während eine Zeitfrage aussteht, der Vollständigkeitsstatus bleibt erkennbar.

### 2.2. Parteien und Zustellungsdaten

Erfasse Rechnungsaussteller, umsatzsteuerlichen Leistungsempfänger, Auftraggeber, Rechnungsempfänger, Zahlenden und etwaige Rechnungsprüfer getrennt. Eine Rechtsschutzversicherung wird nicht allein wegen ihrer Zahlung zum Leistungsempfänger; sie ist Zahlerin im Rahmen der Deckung. Eine Konzernmutter, die Rechnungen zentral bearbeitet, ist nicht zwangsläufig Vertragspartnerin. Ein Zahlendreher in der Postanschrift ist anders zu behandeln als die Abrechnung gegenüber der falschen juristischen Person. Benötigt werden Rechnungsnummer, Ausstellungsdatum, Leistungszeitraum, Währung, Zahlungsbedingungen, Steuerbehandlung, Empfängerreferenzen und der vereinbarte oder vorgeschriebene Übermittlungsweg. Bei öffentlichen Auftraggebern kommen Leitweg-ID, Bestellnummer, elektronische Adresse und Portalvorgaben hinzu. Fehlende Referenzen werden nicht erfunden, um eine Validierung zu bestehen.

### 2.3. Steuer- und Formatangaben

Kläre Inland oder Ausland, Unternehmereigenschaft, Leistungsbezug für das Unternehmen, Steuerbefreiung, Kleinunternehmerstatus, Steuerschuldnerschaft des Leistungsempfängers und den Leistungsort. Das lokale Skript ist enger als das Umsatzsteuerrecht: Es verarbeitet ausschließlich EUR, inländische Parteien, positive Positionen und 19 Prozent Umsatzsteuer ohne Vorschussverrechnung, Rabatte, Gutschriften, Reverse Charge oder Kleinunternehmerfälle. Ein außerhalb liegender Fall benötigt einen geeigneten Fachablauf und darf nicht durch falsche Stammdaten passend gemacht werden. Empfangspflicht und der noch zulässige Verzicht auf Ausstellung einer E-Rechnung sind nicht identisch; B2C, B2B und B2G werden getrennt beurteilt.

### 2.4. Entscheidende Angaben und Vorgehen bei Lücken

| Angabe | Warum entscheidend | Vorgehen, wenn sie fehlt |
|---|---|---|
| Honorarmodell mit Satz, Deckel, Netto- oder Bruttobezug | Bestimmt jede Position und den Deckelabgleich | Rückfrage; keine Rechnung, nur Leistungsaufstellung |
| Bestätigte Zeiteinträge oder geprüftes Gebührenblatt | Ohne sie gibt es keine berechenbare Forderung | Offene Einträge markieren; Teilbetrag als vorläufig ausweisen |
| Gegenstandswert und Auftragsdatum bei RVG | Tabelle nach § 13 RVG und Übergangsrecht nach § 60 RVG hängen davon ab | Gebührenblatt anfordern; keine Tabelle aus dem Gedächtnis |
| Umsatzsteuerlicher Leistungsempfänger | Falscher Empfänger macht die Rechnung unbrauchbar | Mandatsvertrag lesen; Zahler nicht als Empfänger eintragen |
| Unternehmerstatus und Sitz des Empfängers | Entscheidet über E-Rechnungspflicht, Leistungsort und Steuerschuld | Rückfrage; Formatentscheidung zurückstellen |
| Bereits gezahlte Vorschüsse | Pflichtangabe nach § 10 Absatz 2 RVG und Zahlbetrag | Journalzahlungen lesen; ohne Klärung keine Schlussrechnung |
| Leistungszeitraum | Pflichtangabe nach § 14 Absatz 4 UStG; Abgrenzung zu Vorrechnungen | Aus Zeitbelegen ableiten; nie das Ausstellungsdatum einsetzen |
| Leitweg-ID, Bestellnummer, Portalweg bei B2G | Ohne sie wird die XRechnung abgewiesen | Nachforderungsschreiben nach Beispiel 6.2; nichts erfinden |
| Vom Empfänger akzeptiertes Format und Profil | XRechnung, ZUGFeRD oder sonstige Rechnung mit Zustimmung | Rückfrage beim Empfänger; Entwurf als XML vorbereiten |
| Bankverbindung und USt-IdNr. der Kanzlei aus Stammdaten | Falsche Daten lenken Zahlungen fehl | Nur aus dem Kanzleistammsatz; keine E-Mail-Angabe übernehmen |
| Rechnungsnummer aus dem Register | Eindeutigkeit nach § 14 Absatz 4 Nummer 4 UStG | Entwurfsnummer verwenden und als Entwurf kennzeichnen |

### 2.5. Rückfragen in der richtigen Reihenfolge

Stelle nur Fragen, deren Antwort das Ergebnis verändert, und bündle sie. Die Reihenfolge lautet:

1. „Welche Honorargrundlage gilt für den Abrechnungszeitraum vom [Beginn] bis [Ende]: die Vereinbarung vom [Datum] mit [Satz oder Betrag], oder gab es einen Nachtrag?“
2. „Sind die Zeiteinträge [IDs] vollständig und abrechenbar, oder fehlen noch Leistungen, die in diese Rechnung gehören?“
3. „Wer ist umsatzsteuerlicher Leistungsempfänger: die Mandantin selbst, eine Gesellschaft der Gruppe oder eine andere Person? Wer zahlt?“
4. „Ist der Empfänger Unternehmer mit Sitz im Inland, im übrigen Gemeinschaftsgebiet oder im Drittland, oder Verbraucher?“
5. „Welche Vorschüsse oder Teilzahlungen sind auf diesen Abrechnungsabschnitt bereits eingegangen?“
6. „Verlangt der Empfänger XRechnung, ZUGFeRD oder akzeptiert er eine PDF-Rechnung mit Zustimmung, und welche Referenzen (Leitweg-ID, Bestellnummer, Kostenstelle) benötigt er?“
7. „Soll die Rechnung als Teil-, Vorschuss- oder Schlussrechnung bezeichnet werden?“

Ohne Antwort auf Frage 1 oder 2 wird keine Rechnung, sondern eine Leistungsaufstellung mit Platzhaltern erstellt. Fragen 3 bis 5 blockieren den Rechnungstext, nicht die Leistungsaufstellung. Fragen 6 und 7 blockieren nur das Format und die Bezeichnung; der Entwurf kann bis dahin als sonstige Rechnung im Entwurfsstatus vorbereitet werden.

## 3. Ablauf und Checkliste

### 3.1. Forderung zuerst auf ihre Grundlage prüfen

Ermittle, welche Vergütung entstanden und fällig ist. Nach [§ 8 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__8.html) wird die Vergütung fällig, wenn der Auftrag erledigt oder die Angelegenheit beendet ist; bei gerichtlichen Verfahren zusätzlich mit Kostenentscheidung, Erledigung in der Instanz oder einem Ruhen des Verfahrens von mehr als drei Monaten. Nach [§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html) kann für die entstandenen und voraussichtlich entstehenden Gebühren und Auslagen ein angemessener Vorschuss gefordert werden; der Vorschuss ist keine Schlussrechnung und kein Anerkenntnis des späteren Endbetrags. Bei RVG werden Gebührentatbestände, Werte, Anrechnungen und das Übergangsrecht nach § 60 RVG anhand eines gesonderten Gebührenblatts geprüft; bei Rahmengebühren bestimmt der Anwalt den Satz nach [§ 14 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__14.html) nach billigem Ermessen unter Berücksichtigung aller Umstände, insbesondere Umfang und Schwierigkeit, Bedeutung der Angelegenheit sowie Einkommens- und Vermögensverhältnisse des Auftraggebers, und begründet einen über der Mittelgebühr liegenden Ansatz. Der Mindestbetrag einer Wertgebühr nach § 13 RVG beträgt 15 Euro; Absatzzählung und Betrag sind am amtlichen Volltext zu prüfen.

Bei Zeithonorar werden wirksame Grundlage, passende Tätigkeit, tatsächliche Dauer, gültiger Satz und Deckel kontrolliert. Bei Festpreis werden Leistungsumfang, Leistungsstand und Fälligkeitsregel betrachtet; der im Journal ausgewiesene volle Festpreis ist ein Vereinbarungswert, keine Aussage, dass er bereits verlangt werden darf. Die Erstattungsfähigkeit gegenüber Gegner oder Staatskasse unterscheidet sich vom Anspruch gegen den Mandanten; eine Deckungszusage ist keine Zustimmung zu jedem Honorar. Bei Beiordnung oder Beratungshilfe gelten die besonderen Grenzen.

### 3.2. Anwaltliche Berechnung nach § 10 RVG

Nach [§ 10 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__10.html) kann die Vergütung nur aufgrund einer in Textform erstellten und dem Auftraggeber mitgeteilten Berechnung eingefordert werden; die Mitteilung erfolgt durch den Rechtsanwalt oder auf seine Veranlassung. Eine eigenhändige Unterschrift ist zum Prüfstand nicht mehr Voraussetzung. Ein intern fortgeschriebener Entwurf ist noch keine mitgeteilte Berechnung. Der Lauf der Verjährung hängt nicht von der Mitteilung ab; eine liegengebliebene Rechnung wird nicht automatisch rechtzeitig.

Für gesetzliche Gebühren verlangt § 10 Absatz 2 RVG die Beträge der einzelnen Gebühren und Auslagen, die Vorschüsse, eine kurze Bezeichnung des jeweiligen Gebührentatbestands, die Bezeichnung der Auslagen, die angewandten Nummern des Vergütungsverzeichnisses und bei Wertgebühren den Gegenstandswert; bei Rahmengebühren genügt die Angabe des Rahmens nicht, der gewählte Satz ist zu nennen. Bei Zeithonorar muss die Leistungsdarstellung eine Prüfung ermöglichen: Datum, Person, Dauer und konkrete Tätigkeit je Eintrag. Ein einheitlicher Text „Beratung im Oktober“ genügt für einen streitigen Stundenanspruch nicht. Stelle die Zeitaufstellung bereit, ohne vertrauliche Einzelheiten an unberechtigte Dritte zu verteilen.

Die vom Mandanten erbetene Rechnungserläuterung ist kein neuer Gebührenanspruch, nur weil ihre Erstellung Zeit kostet. Kosten der Korrektur eigener Rechnungsfehler werden nicht weiterberechnet. Interne Bearbeitungszeit darf dokumentiert werden, bleibt aber von der Abrechenbarkeit getrennt.

### 3.3. Auslagen nach Teil 7 des Vergütungsverzeichnisses

Auslagen werden einzeln nach [Anlage 1 zum RVG](https://www.gesetze-im-internet.de/rvg/anlage_1.html) angesetzt; die genannten Beträge sind am amtlichen Volltext zu prüfen, weil der Abruf zum Prüfstand nicht möglich war. Die Dokumentenpauschale nach Nr. 7000 VV RVG beträgt für die ersten 50 abzurechnenden Seiten je 0.50 Euro und für jede weitere Seite 0.15 Euro; sie entsteht nur für die dort genannten Fälle, etwa Abschriften aus Behörden- und Gerichtsakten, soweit deren Herstellung zur sachgemäßen Bearbeitung geboten war, oder zusätzliche Abschriften auf Verlangen des Auftraggebers. Interne Arbeitskopien lösen sie nicht aus. Die Pauschale für Post- und Telekommunikationsdienstleistungen nach Nr. 7002 VV RVG beträgt 20 Prozent der Gebühren, höchstens 20 Euro je Angelegenheit; alternativ können die tatsächlichen Entgelte nach Nr. 7001 VV RVG abgerechnet werden, nicht beides. Fahrtkosten mit eigenem Kraftfahrzeug nach Nr. 7003 VV RVG betragen 0.42 Euro je gefahrenen Kilometer; Tage- und Abwesenheitsgeld nach Nr. 7005 VV RVG richtet sich nach der Abwesenheitsdauer. Die Umsatzsteuer auf Gebühren und Auslagen wird nach Nr. 7008 VV RVG in voller Höhe angesetzt, soweit sie nicht nach § 19 UStG unerhoben bleibt.

Bei Zeithonorar gelten diese Nummern nur, wenn die Vereinbarung auf sie verweist; sonst sind Auslagen so abzurechnen, wie die Vereinbarung sie regelt. Ein Gerichtskostenvorschuss, den die Kanzlei im Namen und für Rechnung der Mandantin verauslagt hat, ist ein durchlaufender Posten und erhält keine Umsatzsteuer; eine im eigenen Namen bezogene Fremdleistung ist dagegen Teil der steuerpflichtigen Leistung. Rechnungsbeleg, Schuldner der Fremdforderung und Handeln im eigenen oder fremden Namen entscheiden, nicht das Wort „Auslage“.

### 3.4. Rechenweg und Deckelabgleich

Berechne jede Position aus der zutreffenden Grundlage. Bei Stundenhonorar werden tatsächliche Minuten in Stunden umgerechnet und mit dem gültigen Satz bewertet; Festpreise werden nicht zusätzlich um Zeitwerte erhöht. Bei einem Deckel wird geprüft, ob er Gebühren allein oder Gebühren und Auslagen umfasst. Ein verbrauchter Gesamtdeckel wird nicht durch eine neue Rechnungsnummer, einen neuen Monat oder eine neue Phase zurückgesetzt. Beispiel: Bestätigte Zeitwerte betragen 2.420 Euro netto und eigene steuerpflichtige Auslagen 160 Euro netto. Bei einem gemeinsamen Deckel von 2.500 Euro netto darf der Entwurf nicht 2.580 Euro ansetzen; bei einem nur auf Honorar bezogenen Deckel kann die Behandlung anders ausfallen, wenn die Auslagenerstattung wirksam vereinbart ist. Dokumentiere tatsächlichen Aufwand und begrenzten Ansatz getrennt.

Kontrolliere Geldrundung, Steuerbasis und Gesamtsumme. Die Summe einzeln gerundeter Positionen kann von einer erst am Ende gerundeten Gesamtzeit abweichen; verwende einen konsistenten Rechenweg und gleiche XML, Sichtfassung und Buchungsvorschlag ab.

### 3.5. Umsatzsteuer und Pflichtangaben

Prüfe die Pflichtangaben nach [§ 14 Absatz 4 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html): vollständiger Name und Anschrift von Leistendem und Leistungsempfänger, Steuernummer oder USt-IdNr. des Leistenden, Ausstellungsdatum, fortlaufende einmalige Rechnungsnummer, Art und Umfang der Leistung, Zeitpunkt oder Zeitraum der Leistung, nach Steuersätzen aufgeschlüsseltes Entgelt, anzuwendender Steuersatz und Steuerbetrag beziehungsweise Hinweis auf eine Steuerbefreiung, bei Vorauszahlungen den Zeitpunkt der Vereinnahmung. Leistungsbeschreibung und Leistungszeitraum werden nicht durch das Ausstellungsdatum ersetzt; bei mehrmonatiger Beratung wird der Zeitraum aus den Belegen bestimmt. Die Rechnung ist nach § 14 Absatz 2 UStG innerhalb von sechs Monaten nach Ausführung der Leistung auszustellen, wenn der Empfänger Unternehmer ist; der Umsatz einer Kanzlei ist nicht nach § 4 Nummern 8 bis 29 UStG befreit.

Für Kleinbetragsrechnungen bis einschließlich 250 Euro brutto gelten die erleichterten Angaben nach [§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html). Eine Kanzlei, die als Kleinunternehmerin nach [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) steuerfrei leistet, weist keine Umsatzsteuer aus und vermerkt die Steuerbefreiung; die Grenzen von 25.000 Euro Gesamtumsatz im Vorjahr und 100.000 Euro im laufenden Jahr sind am Volltext zu prüfen. Weist eine Rechnung einen höheren Steuerbetrag aus, als geschuldet wird, schuldet der Aussteller nach [§ 14c Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) auch den Mehrbetrag; eine Berichtigung setzt die Beseitigung der Gefährdung des Steueraufkommens voraus. Wer ohne Berechtigung Steuer ausweist, schuldet den ausgewiesenen Betrag nach § 14c Absatz 2 UStG. Deshalb werden Testdateien mit fiktiven Daten getrennt gehalten; die Bezeichnung „Entwurf“ schützt nicht, wenn ein Dokument tatsächlich wie eine Rechnung verwendet wird.

### 3.6. Leistungsort, Auslandsmandant und Steuerschuldnerschaft

Bei einem Mandanten mit Sitz außerhalb Deutschlands wird zuerst der Leistungsort bestimmt. Eine sonstige Leistung an einen Unternehmer für sein Unternehmen wird nach [§ 3a Absatz 2 UStG](https://www.gesetze-im-internet.de/ustg_1980/__3a.html) an dem Ort ausgeführt, von dem aus der Empfänger sein Unternehmen betreibt; die Leistung ist dann in Deutschland nicht steuerbar. Bei einem Unternehmer im übrigen Gemeinschaftsgebiet wird die Rechnung ohne deutsche Umsatzsteuer mit der Angabe „Steuerschuldnerschaft des Leistungsempfängers“ sowie mit der USt-IdNr. der Kanzlei und des Empfängers nach [§ 14a Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html) ausgestellt; die dort vorgesehene Ausstellungsfrist bis zum 15. des Folgemonats und die Zusammenfassende Meldung werden an [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md) übergeben. Beratungsleistungen an einen Nichtunternehmer im Drittland sind nach § 3a Absatz 4 UStG gesondert zu prüfen. Umgekehrt schuldet die Kanzlei nach [§ 13b Absatz 5 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html) die Steuer für Leistungen, die sie von einem im Ausland ansässigen Unternehmer bezieht. Das lokale Skript unterstützt keinen dieser Fälle; der Rechnungstext wird dann ohne XML-Export erstellt und der Steuervermerk vor Freigabe gegen den aktuellen Normtext geprüft.

### 3.7. Entscheidungsbaum für das erforderliche Rechnungsformat

Prüfe zuerst, ob der Umsatz unter die inländische B2B-Regel fällt: Leistender und Leistungsempfänger sind Unternehmer mit Sitz im Inland und die Leistung wird für das Unternehmen bezogen. Ist der Empfänger Verbraucher, besteht keine E-Rechnungspflicht; eine PDF oder Papierrechnung bleibt zulässig. Ist der Empfänger eine öffentliche Stelle, gelten zusätzlich die Vorgaben des Bundes oder des Landes für den Empfangsweg, insbesondere die ERechV des Bundes und die Landesregelungen mit Leitweg-ID. Bei Auslandsbezug ist die inländische B2B-Route nicht schematisch anzuwenden. Eine vertragliche Formatvereinbarung bleibt daneben relevant.

Prüfe danach die Übergangsregel in [§ 27 Absatz 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html). Für Umsätze bis zum 31. Dezember 2026 (einem Donnerstag) darf noch eine sonstige Rechnung auf Papier oder, mit Zustimmung des Empfängers, in einem anderen elektronischen Format übermittelt werden. Für Umsätze im Jahr 2027 gilt das weiter, wenn der Gesamtumsatz des Ausstellers im Vorjahr nicht mehr als 800.000 Euro betragen hat; daneben besteht die befristete EDI-Regel. Ab dem 1. Januar 2028 entfallen die Übergänge, nicht die gesetzlichen Ausnahmen für Kleinbetragsrechnungen und Kleinunternehmer. Die Pflicht, E-Rechnungen empfangen zu können, besteht für inländische Unternehmer unabhängig davon seit 2025.

Halte das Ergebnis in einem Satz mit Tatsachengrundlage fest: „Für diesen inländischen unternehmerischen Leistungsempfänger ist die XRechnung der Zielstandard; die Übergangsmöglichkeit für 2026 wird nicht benötigt, weil der Empfänger XRechnung 3.0 akzeptiert.“ Der Satz „Seit 2025 muss jede Rechnung XML sein“ ist unzutreffend.

### 3.8. Empfängeranforderungen und Datenminimierung

Kontrolliere, welche Daten der Empfänger für die Zuordnung benötigt und welche die Rechnung rechtlich enthalten muss. Eine Einkaufsabteilung kann Bestellnummern verlangen, ohne vertrauliche Beratungsinhalte erhalten zu dürfen; die Leistungsbeschreibung wird aussagekräftig, aber begrenzt formuliert. Eine Leitweg-ID wird aus dem Auftrag oder einer authentisch bestätigten Mitteilung übernommen; ihre formale Plausibilität beweist nicht die Zuordnung zur richtigen Behörde. Dasselbe gilt für elektronische Adressen und Bankdaten; eine kurz vor Rechnungsstellung per E-Mail mitgeteilte neue Bankverbindung wird nach dem Kanzleiverfahren unabhängig bestätigt. Bei einem externen Rechnungsprüfer des Mandanten werden Rolle, Vertraulichkeit und Datenumfang geklärt; der Skill erzeugt eine Leistungsaufstellung, keine Freigabe der Akte.

### 3.9. Den Journalentwurf fachlich freigeben

Lies `rechnungsentwurf.json` aus dem Mandatsordner nach [Mandatsordner und CLI](../../references/mandatsordner-und-cli.md) mit Journalrevision, Phasen, offenen Positionen und Zahlungen. Das Feld `complete` bedeutet nur, dass die erkannten Erfassungsfragen geschlossen sind; `invoice_ready` bleibt bewusst falsch. Zahlungen werden gesondert gezeigt und nicht verrechnet. RVG-Beträge werden über den Befehl `manual-fee` von [kanzlei.py](../../scripts/kanzlei.py) nur mit geprüftem Gebührenblatt und `legal_reviewed=true` übernommen; das Feld bestätigt eine Prüfung, es rechnet nicht.

### 3.10. XRechnung mit dem vorhandenen Skript erzeugen

Das Skript [xrechnung.py](../../scripts/xrechnung.py) kennt genau die Optionen `--input` und `--output`. Die Eingabedatei nach `assets/xrechnung-beispiel.json` enthält `schema_version` mit dem Wert 1, `document_state` (`draft` oder `approved`), `legal_reviewed`, `invoice_number`, `issue_date`, `due_date`, `period_start`, `period_end` im Format JJJJ-MM-TT, `currency` mit dem Wert EUR, `vat_rate` mit dem Wert 19, `buyer_reference`, die Blöcke `supplier` (mit `name`, `street`, `postal_code`, `city`, `country`, `email`, `vat_id`, `contact`, `phone`, `iban`) und `customer` (mit `name`, `street`, `postal_code`, `city`, `country`, `email`) sowie die Liste `lines` mit `id`, `description`, `quantity`, `unit_code` und `unit_price_net`. Zulässige Einheiten sind `C62`, `HUR`, `MIN` und `DAY`; Mengen müssen positiv sein; Menge und Einzelpreis dürfen höchstens sechs Nachkommastellen haben. Beide Parteien müssen `country` gleich `DE` haben. Die Schlüssel `allowances`, `prepaid_amount`, `credit_note` und `reverse_charge` führen zum Abbruch, damit kein Sonderfall stillschweigend ausgelassen wird.

Der Aufruf lautet `python3 "<Pluginordner>/scripts/xrechnung.py" --input "<Rechnungsdaten.json>" --output "<Mandatsordner>/02_Honorar/Rechnung_Entwurf_v1.xml"`. Eine vorhandene Ausgabedatei wird nicht überschrieben; eine Korrektur erhält eine neue Versionsdatei. `document_state=draft` setzt einen Entwurfshinweis in das Feld `Note`; `approved` setzt `legal_reviewed=true` voraus, ersetzt aber weder eine echte Freigabe noch den Versandauftrag. Das Skript erzeugt UBL mit der CustomizationID für XRechnung 3.0, Rechnungstyp 380, Zahlungsart 58 mit IBAN, prüft Datumsfolgen, doppelte Positions-IDs, das Muster der deutschen USt-IdNr. und die IBAN-Prüfziffer. Es prüft weder ein Nummernregister noch die Echtheit von Steuer- oder Kontodaten und gibt `kosit_validated` stets als falsch aus. Die Testdaten des Beispiels dürfen nicht in eine reale Rechnung gelangen.

### 3.11. Technische Validierung und Sichtkontrolle

Zum Prüfstand 7. Oktober 2026 ist XRechnung 3.0 die normative Version; das aktuelle Bundle ist 3.0.2 Summer 2026 Bugfix vom 31. August 2026, die im September veröffentlichte Spezifikation 4.0 ist eine Vorversion. Prüfe vor jedem produktiven Export den Stand auf der [KoSIT-Versionsseite](https://xeinkauf.de/xrechnung/versionen-und-bundles/) und das vom Empfänger akzeptierte Profil. Validiere jede exportierte Datei mit dem aktuellen KoSIT-Validator und der passenden Konfiguration; dokumentiere Version, Konfiguration, Datei und Ergebnis. Eine XSD-Prüfung allein genügt nicht; Geschäftsregeln und Empfängerregeln sind einzubeziehen, Warnungen werden inhaltlich bewertet. Vergleiche anschließend eine lesbare Visualisierung mit den freigegebenen Eingaben. Bei Abweichungen wird die Ursache in den strukturierten Daten korrigiert und erneut validiert; ein verschönertes PDF bei unverändert falschem XML ist keine Lösung.

### 3.12. Rechnungsnummer, Korrektur und Archiv

Die Rechnungsnummer wird aus dem kanzleiweiten Register vergeben; das Skript führt kein Register. Entwurfsnummern werden nicht in die produktive Folge übernommen. Bei Fehlern in einer ausgestellten Rechnung prüfe, ob eine Ergänzung, eine Berichtigung mit eindeutigem Bezug auf die Ursprungsrechnung oder ein Storno mit neuer Rechnung erforderlich ist. Ein Storno weist denselben Betrag mit umgekehrtem Vorzeichen aus und nennt Nummer und Datum der stornierten Rechnung; die Neuausstellung erhält eine neue Nummer. Verwende das Wort „Gutschrift“ nicht unbedacht, weil es im Umsatzsteuerrecht die vom Leistungsempfänger ausgestellte Rechnung bezeichnet; für Korrekturen eignet sich „Rechnungskorrektur“ oder „Stornorechnung“.

Archiviere strukturierte Originaldaten, Sichtfassung, Validierungsbericht, Freigabe und Übermittlungsnachweis in nachvollziehbarer Zuordnung. Nach [§ 14b Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html) sind ein Doppel jeder ausgestellten und alle empfangenen Rechnungen acht Jahre aufzubewahren, beginnend mit dem Schluss des Kalenderjahres der Ausstellung; die seit dem Vierten Bürokratieentlastungsgesetz geltende Dauer ist am Volltext zu prüfen. [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html) nennt für Buchungsbelege ebenfalls acht Jahre, für Bücher, Inventare und Jahresabschlüsse zehn Jahre und für übrige Unterlagen sechs Jahre; die Handakte unterliegt daneben § 50 BRAO. Die GoBD verlangen einen Prüfpfad; eine E-Rechnung wird im strukturierten Format aufbewahrt, das Ausdrucken und Löschen der XML-Datei genügt nicht. Ein pauschaler Zeitraum für sämtliche Mandatsunterlagen wird nicht behauptet.

### 3.13. Tatsächliche Mitteilung und Zahlungsüberwachung

Vor einem beauftragten Versand werden Empfänger, Kanal, Fassung und Anlagen kontrolliert; der Versandstatus wird erst nach Durchführung gesetzt. Eine Portalannahme ist eine technische Bestätigung, kein Ausschluss materieller Einwendungen. Fälligkeit und Verzug folgen aus Gesetz, Vertrag, Zugang und gegebenenfalls Mahnung; die 30-Tage-Regel des § 286 Absatz 3 BGB setzt gegenüber Verbrauchern den besonderen Hinweis in der Rechnung voraus. Ein frei gewähltes Fälligkeitsdatum im XML begründet keine fehlende Vereinbarung.

### 3.14. Berichtigung und Vorsteuer zeitlich präzise behandeln

Eine Korrektur kann fehlende Steuernummer, ungenaue Leistungsbeschreibung, falschen Zeitraum, falschen Empfänger oder fehlenden Steuerausweis betreffen; diese Fehler haben nicht dieselbe Rechtsfolge. Prüfe, ob das Ursprungsdokument die Mindestangaben einer berichtigungsfähigen Rechnung enthält und ob die materiellen Voraussetzungen des Vorsteuerabzugs nach [§ 15 Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html) vorliegen. Eine Ergänzung wird weder pauschal als rückwirkend noch pauschal als nur zukünftig wirkend behandelt. Der Beschluss des BFH vom 26. Februar 2026 lässt die Frage der zeitlichen Ausübung des Vorsteuerabzugs bei einem zunächst nicht berichtigungsfähigen Dokument zur Revision zu; das ist ein Anlass zur Aktualitätskontrolle, keine Antwort. Benenne im Vermerk die konkrete Unsicherheit. Der neue Datensatz verweist auf die Ursprungsrechnung; der frühere wird weder gelöscht noch überschrieben.

### 3.15. Teilrechnung und mehrere Angelegenheiten

Eine Teilrechnung verlangt einen abgegrenzten Abrechnungsabschnitt und darf nicht den Eindruck erwecken, der Auftrag sei abgeschlossen. Bei mehreren RVG-Angelegenheiten werden Entstehung, Anrechnung und Übergangsrecht je Angelegenheit geprüft; eine Sammelrechnung stellt die Grundlagen getrennt dar. Eine periodenbezogene Stundenrechnung braucht den Abgleich mit bereits abgerechneten Zeiten; ein Abrechnungsnachweis hält fest, welche Eintrags-IDs welcher Rechnung zugeordnet wurden.

### 3.16. Eingangsrechnungen der Kanzlei prüfen

Bei einer Lieferantenrechnung beginnt der Ablauf beim Leistungsbezug: Bestellung, Vertrag, gelieferte Leistung und Rechnung werden verglichen. Eine formal gültige XRechnung beweist weder vollständige Leistung noch richtigen Preis. Prüfe Doppelrechnungen, erfolgte Zahlungen, Kontoverbindungen und Nebenentgelte. Die Vorsteuerfrage nach § 15 UStG wird von der Zahlungsfreigabe getrennt. Für die Buchhaltung werden Original-XML, Anlagen und Prüfhinweise übergeben. Ein Rückfragetext lautet: „Ihre Rechnung [Nummer] vom [Datum] bezeichnet als Leistungszeitraum lediglich den Ausstellungsmonat. Nach unserem Auftrag betrifft die Rechnung die Leistungen vom [Beginn] bis [Ende]. Bitte prüfen Sie den Zeitraum und übersenden Sie eine gegebenenfalls erforderliche Berichtigung mit eindeutigem Bezug auf die ursprüngliche Rechnung.“

### 3.17. Typische Fehler und Gegenkontrolle

| Fehler | Woran erkennbar | Gegenkontrolle |
|---|---|---|
| PDF als E-Rechnung bezeichnet | Keine XML-Datei, nur Sichtfassung | Datei öffnen; ohne XML-Teil ist es eine sonstige Rechnung |
| Rechtsschutzversicherer als Leistungsempfänger | Versicherung im Feld Kunde, Mandant nur im Betreff | Mandatsvertrag lesen; Zahler und Empfänger trennen |
| Leistungszeitraum gleich Ausstellungsmonat | Zeitraum deckt sich mit Rechnungsdatum | Erste und letzte Zeitbuchung des Abschnitts prüfen |
| Vorschuss fehlt in der Berechnung | Zahlbetrag entspricht Gesamtbetrag trotz Journalzahlung | Journalzahlungen je Abschnitt abgleichen, § 10 Absatz 2 RVG |
| Nr. 7002 über 20 Euro | Pauschale rechnerisch 20 Prozent ohne Deckel | Höchstbetrag anwenden oder Nr. 7001 mit Belegen wählen |
| Umsatzsteuer auf Gerichtskostenvorschuss | 19 Prozent auf durchlaufende Posten | Zahlungsbeleg prüfen; im fremden Namen verauslagt bleibt steuerfrei |
| Tabellenwert aus dem Gedächtnis | Kein Gebührenblatt mit Tabellenstand in der Akte | Gebührenblatt mit Auftragsdatum und § 60 RVG anfordern |
| Gesamtdeckel durch neue Phase zurückgesetzt | Summe aller Rechnungen über dem Deckel | Alle Rechnungen zur Vereinbarung addieren |
| Erfundene Leitweg-ID zur Validierung | Validator grün, Behörde weist Rechnung ab | Leitweg-ID nur aus Auftrag oder bestätigter Mitteilung |
| „Gutschrift“ für eine Erstattung | Dokument heißt Gutschrift, Aussteller ist die Kanzlei | Bezeichnung „Rechnungskorrektur“ oder „Stornorechnung“ |
| Export als Validierung ausgegeben | Prüfvermerk nennt keinen Validator | `kosit_validated` ist falsch; KoSIT-Lauf dokumentieren |
| Deutsche Steuer an EU-Unternehmer | 19 Prozent trotz ausländischer USt-IdNr. | § 3a Absatz 2 und § 14a Absatz 1 UStG prüfen |

### 3.18. Übergabe an Nachbarskills

An [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md) gehen die ausgestellte Rechnung mit Nummer, Datum, Netto, Steuer, Brutto, Fälligkeit und Belegreferenz sowie die Liste der verrechneten Vorschüsse; zurück kommen die Zahlungszuordnung, offene Restbeträge und ein Buchungsvorschlag. An [Mandantenkommunikation](../mandantenkommunikation/SKILL.md) geht der versandfähige Rechnungstext mit der Information, welche Phase abgerechnet ist und welche offen bleibt; zurück kommt das Anschreiben mit Sachstand und nächsten Schritten. An [Mandat abschließen](../mandat-abschliessen/SKILL.md) geht die Schlussrechnung mit Abgleich aller Eintrags-IDs; zurück kommt die Bestätigung, dass keine abrechenbare Leistung offen ist. An [Workflow-Übergabe](../workflow-uebergabe/SKILL.md) geht der Prüfvermerk mit den Punkten, die eine fachliche Abnahme verlangen, insbesondere Rahmengebührensatz und Steuervermerk bei Auslandsbezug. Ergibt sich während der Abrechnung, dass die Honorargrundlage unklar ist, geht die Frage an [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) zurück; die Rechnung wartet. Der Honorar- und Zeitanschluss aus [Arbeitsweise](../../references/arbeitsweise.md) gilt dabei unverändert: Gespeicherte Grundlage vorhalten, nur entscheidende Lücken erfragen.

## 4. Quellenpflicht

### 4.1. Normen und amtliche technische Quellen

Beachte [Zitierweise](../../references/zitierweise.md) und [Rechtsquellen](../../references/rechtsquellen.md). Tragende Normlinks sind [§ 8 RVG](https://www.gesetze-im-internet.de/rvg/__8.html), [§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html), [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html), [§ 13 RVG](https://www.gesetze-im-internet.de/rvg/__13.html), [§ 14 RVG](https://www.gesetze-im-internet.de/rvg/__14.html), [§ 60 RVG](https://www.gesetze-im-internet.de/rvg/__60.html), [Anlage 1 zum RVG](https://www.gesetze-im-internet.de/rvg/anlage_1.html), [§ 3a UStG](https://www.gesetze-im-internet.de/ustg_1980/__3a.html), [§ 13b UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html), [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 14a UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html), [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html), [§ 15 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html), [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html), [§ 27 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html), [§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html) und [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html). Für die E-Rechnung werden die [BMF-Information](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) und die [KoSIT-Versionsseite](https://xeinkauf.de/xrechnung/versionen-und-bundles/) herangezogen. Verwaltungsauffassung, Gesetz, Gerichtsentscheidung und eigene technische Umsetzung bleiben unterscheidbar.

### 4.2. Verifizierte Entscheidungsanker

BFH, Urteil vom 20.10.2016 – V R 26/15, Rn. 19–23, [amtlicher Volltext](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE201610285/). Trägt: Eine Rechnung mit bestimmten Mindestangaben kann mit Rückwirkung berichtigt werden. Trägt nicht: Die Heilung eines Dokuments ohne diese Mindestangaben, einen Vorsteuerabzug ohne materielle Voraussetzungen oder eine Rückwirkung bei fehlendem Leistungsempfänger.

BFH, Beschluss vom 26.02.2026 – V B 11/25, Rn. 2, [amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/). Trägt: Die Frage der zeitlichen Ausübung des Vorsteuerabzugs bei ursprünglich nicht berichtigungsfähigem Dokument ist zur Revision zugelassen und zum Prüfstand als V R 7/26 anhängig; die Rechtslage ist insoweit offen. Trägt nicht: Irgendeine Sachaussage über den Ausgang; der Beschluss entscheidet die Rechtsfrage nicht.

BGH, Urteil vom 12.09.2024 – IX ZR 65/23, Rn. 16 und 34–37, [amtlicher Volltext im Curia-Archiv](https://curia.europa.eu/site/upload/docs/application/pdf/2025-04/ix_zr__65-23_2025-04-16_15-06-53_148.pdf). Trägt: Die Zeitabrechnung muss nachprüfbar darlegen, welche Tätigkeit wann und wie lange erbracht wurde. Trägt nicht: Ein Verbot anwaltlicher Stundenhonorare oder die Annahme, ein technischer Rechnungsstandard ersetze diese Darlegung.

BGH, Urteil vom 19.02.2026 – IX ZR 226/22, Rn. 29–34, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1). Trägt: Eine formularmäßige Fiktion, nicht binnen Monatsfrist beanstandete Zeitaufstellungen gälten als anerkannt, ist auch gegenüber Unternehmern unwirksam. Trägt nicht: Die Unwirksamkeit der gesamten Vergütungsvereinbarung oder den Wegfall des übrigen Honoraranspruchs.

### 4.3. Belegdisziplin

Keine Präjudizienbindung: Jeder Anker wird mit seinem Sachverhalt verglichen, nicht als verbindliche Regel zitiert. Keine Tabellenwerte, Pauschalen oder Fristen aus dem Gedächtnis; wo der amtliche Volltext zum Prüfstand nicht abrufbar war, ist das vermerkt und vor einer realen Rechnung nachzuholen. Kommentar- und Aufsatzfundstellen werden nicht aus Modellwissen zitiert; Verwaltungsauffassungen wie die BMF-FAQ sind als solche zu kennzeichnen. Der Rechnungstext enthält keine Fundstellen außer den Nummern des Vergütungsverzeichnisses und dem Steuervermerk.

## 5. Ausgabeformat

### 5.1. Rechnung, Nachweise und Status

Liefere eine vollständige Rechnung beziehungsweise einen klar bezeichneten Entwurf, die Leistungsaufstellung und einen getrennten internen Prüfvermerk. Bei XML-Erstellung kommen die Datei und der konkrete Validierungsstatus hinzu. Nenne einen fehlenden Pflichtwert genau. Behaupte keine Validierung, wenn nur exportiert wurde, und keinen Versand, wenn nur Dateien erstellt wurden. Eine ungelöste wesentliche Steuerfrage wird nicht durch einen Haftungsausschluss verdeckt.

Das Endprodukt wird in vollständigen, ausformulierten Sätzen geliefert; Skelette, Halbsätze und reine Aufzählungsgerüste sind als Endprodukt verboten. Tabellen dürfen Rechnungspositionen darstellen. Lesbare formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung; strukturierte XML-Felder folgen dem technischen Standard. Technische Prüfhinweise und der Exporthinweis stehen außerhalb des versandfähigen Rechnungstextes in einer gesonderten Notiz an den Auftraggeber. Platzhalter wie [Rechnungsnummer] oder [Leitweg-ID] bleiben lesbar und werden vor Versand ersetzt.

### 5.2. Abnahmekriterien

Das Produkt ist fertig, wenn jede Position aus einem Beleg oder Gebührenblatt nachvollzogen werden kann und Netto, Steuer und Brutto rechnerisch stimmen. Das Produkt ist fertig, wenn der umsatzsteuerliche Leistungsempfänger, der Rechnungsempfänger und der Zahler ausdrücklich benannt und voneinander unterschieden sind. Das Produkt ist fertig, wenn bei gesetzlichen Gebühren alle Angaben nach § 10 Absatz 2 RVG und bei jeder Rechnung alle Angaben nach § 14 Absatz 4 UStG vorhanden oder als Platzhalter markiert sind. Das Produkt ist fertig, wenn die Formatentscheidung in einem Satz mit Tatsachengrundlage dokumentiert ist. Das Produkt ist fertig, wenn bei einer XML-Datei der Validator, die Konfiguration und das Ergebnis im Prüfvermerk stehen oder die Validierung ausdrücklich als ausstehend bezeichnet ist. Das Produkt ist fertig, wenn Vorschüsse und Teilzahlungen des Abschnitts verrechnet oder ihre Verrechnung als offen bezeichnet ist. Das Produkt ist fertig, wenn Versandstatus und Rechnungsnummer wahrheitsgemäß als vergeben oder als Entwurf ausgewiesen sind.

## 6. Beispiele

### 6.1. Ausformulierte Berechnung nach § 10 RVG mit Vorschussverrechnung

Sachverhalt: Außergerichtliche Vertretung gegenüber einem Lieferanten, Auftrag vom 1. September 2026, Gegenstandswert 8.000 Euro, 1.3 Geschäftsgebühr nach Nr. 2300 VV RVG, 60 Seiten Abschriften aus der Behördenakte auf Verlangen der Mandantin, Vorschuss von 300 Euro am 18. September 2026 eingegangen. Der Wert der 1.0 Gebühr ist dem Gebührenblatt zum Auftragsdatum zu entnehmen; der im Beispiel verwendete Wert von 500 Euro ist ein Rechenwert zur Darstellung des Rechenwegs, kein geprüfter Tabellenwert.

> Rechnung Nr. 2026-0417 vom 7. Oktober 2026
>
> Sehr geehrte Frau Dr. Wendland, in der Angelegenheit Nordlicht Verpackungen GmbH gegen Fasswerk Hallbach wegen Mängelansprüchen aus dem Liefervertrag vom 14. August 2026 berechnen wir für die außergerichtliche Vertretung aufgrund des Auftrags vom 1. September 2026 die gesetzliche Vergütung wie folgt. Der Gegenstandswert beträgt 8.000 Euro. Die Geschäftsgebühr nach Nr. 2300 VV RVG setzen wir mit dem Satz von 1.3 an, weil die Angelegenheit weder besonders umfangreich noch besonders schwierig war; sie beträgt 650,00 Euro. Für die auf Ihr Verlangen gefertigten 60 Seiten Abschriften aus der Behördenakte berechnen wir die Dokumentenpauschale nach Nr. 7000 VV RVG mit 26,50 Euro, nämlich 50 Seiten zu je 0,50 Euro und 10 Seiten zu je 0,15 Euro. Die Pauschale für Post- und Telekommunikationsdienstleistungen nach Nr. 7002 VV RVG beträgt 20 Prozent der Gebühren, höchstens jedoch 20,00 Euro, und wird mit 20,00 Euro angesetzt.
>
> Die Summe aus Gebühren und Auslagen beträgt 696,50 Euro. Hierauf entfällt Umsatzsteuer nach Nr. 7008 VV RVG in Höhe von 19 Prozent, also 132,34 Euro. Der Gesamtbetrag beläuft sich auf 828,84 Euro. Auf diese Angelegenheit haben Sie am 18. September 2026 einen Vorschuss von 300,00 Euro gezahlt, den wir in Abzug bringen. Es verbleibt ein Zahlbetrag von 528,84 Euro.
>
> Der Leistungszeitraum umfasst den 1. September 2026 bis zum 2. Oktober 2026. Bitte überweisen Sie den Zahlbetrag bis zum 21. Oktober 2026 unter Angabe der Rechnungsnummer auf das unten genannte Konto. Diese Rechnung ist eine Schlussrechnung für die außergerichtliche Vertretung; eine etwaige gerichtliche Vertretung wird gesondert beauftragt und abgerechnet.
>
> Mit freundlichen Grüßen
>
> Rechtsanwältin Dr. Frieda Blum

Vor Verwendung werden Steuernummer oder USt-IdNr., Anschriften, Bankverbindung und die Registernummer ergänzt; der Prüfvermerk hält fest, dass der 1.0-Wert aus dem Gebührenblatt mit Tabellenstand übernommen wurde.

### 6.2. Ausformuliertes Nachforderungsschreiben für fehlende B2G-Angaben

> Sehr geehrte Frau Ostermann, die Rechnung für unsere Beratung der Stadt Lindenbrück zum Vergabeverfahren „Neubau Kita Ahornweg“ ist vorbereitet. Nach Ihrer Vorgabe übermitteln wir sie als XRechnung über das Rechnungsportal des Landes. Für die elektronische Zuordnung benötigen wir noch drei Angaben, die uns nicht vorliegen: die von Ihrer Stelle vergebene Leitweg-ID, die Bestell- oder Vorgangsnummer des Vergabereferats und die elektronische Adresse, unter der Ihre Stelle Rechnungen entgegennimmt. Als Leistungsempfängerin ist derzeit die Stadt Lindenbrück, vertreten durch den Bürgermeister, Rathausplatz 1, dokumentiert. Bitte teilen Sie uns mit, falls die Rechnung an einen Eigenbetrieb oder eine andere rechtlich verantwortliche Stelle auszustellen ist.
>
> Die Honorargrundlage bleibt die Vergütungsvereinbarung vom 1. September 2026 mit dem dort vereinbarten Festpreis für die Prüfung der Vergabeunterlagen. Die Rückfrage betrifft ausschließlich die Rechnungs- und Zuordnungsdaten; sie ändert weder Umfang noch Höhe der Vergütung. Nach Eingang der Angaben erstellen wir die XRechnung, prüfen sie mit dem aktuellen Validator und reichen sie über den von Ihnen benannten Weg ein. Wir bitten um Rückmeldung bis zum 14. Oktober 2026, damit die Rechnung noch im laufenden Haushaltsmonat verarbeitet werden kann.
>
> Mit freundlichen Grüßen
>
> Rechtsanwältin Dr. Frieda Blum

Das Schreiben wird als Entwurf geliefert, solange sein Versand nicht beauftragt ist. Eine bereits in der Akte vorhandene und aktuelle Leitweg-ID wird verwendet und nicht erneut abgefragt.

### 6.3. Negativbeispiel: PDF als E-Rechnung ausgegeben

Falsche Ausgabe: „Die E-Rechnung an die Nordlicht Verpackungen GmbH ist erstellt und validiert. Datei: Rechnung_2026-0417.pdf. Die Rechnung erfüllt die E-Rechnungspflicht ab 2025, weil sie elektronisch per E-Mail versandt wird.“

Warum sie falsch ist: Eine PDF-Datei ist eine sonstige Rechnung im Sinn von § 14 Absatz 1 UStG, weil sie kein strukturiertes elektronisches Format enthält, das die Extraktion der Pflichtangaben erlaubt. Der elektronische Versand macht sie nicht zur E-Rechnung. Eine Validierung mit dem KoSIT-Validator hat nicht stattgefunden und könnte bei einer PDF auch nicht stattfinden. Die Formatentscheidung fehlt: Ob für den Umsatz des Jahres 2026 die Übergangsregel nach § 27 Absatz 38 UStG mit Zustimmung der Empfängerin genutzt werden darf, wurde nicht geprüft. Die Aussage „E-Rechnungspflicht ab 2025“ verwechselt die Empfangspflicht mit der Ausstellungspflicht.

Korrigierte Fassung: „Für die Nordlicht Verpackungen GmbH als inländische Unternehmerin ist die XRechnung der Zielstandard. Für den Leistungszeitraum bis zum 2. Oktober 2026 wäre nach § 27 Absatz 38 UStG noch eine PDF-Rechnung zulässig, wenn die Empfängerin dem zustimmt; eine solche Zustimmung liegt nicht vor. Die Datei Rechnung_Entwurf_v1.xml wurde mit xrechnung.py aus den freigegebenen Eingaben erzeugt; `kosit_validated` ist falsch. Nächster Schritt ist die Validierung mit dem KoSIT-Validator in der Konfiguration XRechnung 3.0.2 und die Sichtkontrolle; danach wird die Rechnungsnummer aus dem Register vergeben. Die PDF-Ansicht ist eine Sichtfassung und wird nur zusammen mit der XML-Datei übermittelt.“

### 6.4. Vorschuss schließt den einfachen XML-Weg aus

Die Kanzlei hat 1.190 Euro brutto als Vorschuss erhalten; die Schlussleistung beträgt 2.380 Euro brutto. Das Skript verarbeitet keine Vorschussverrechnung, und der Schlüssel `prepaid_amount` führt zum Abbruch. Deshalb wird keine reduzierte Position von 1.190 Euro erzeugt, die Leistungsumfang und Steuerausweis verfälschen würde. Der interne Vermerk lautet: „Die Hauptleistung beträgt nach geprüfter Grundlage 2.000 Euro netto zuzüglich 380 Euro Umsatzsteuer. Der Zahlungseingang vom 18. September 2026 ist als Vorschuss zugeordnet und wurde mit 1.000 Euro netto zuzüglich 190 Euro Umsatzsteuer versteuert. Die Schlussrechnung weist die Gesamtleistung, den verrechneten Vorschuss mit Datum und den Restzahlbetrag von 1.190 Euro aus und wird mit einem Rechnungswerkzeug erstellt, das diese Verrechnung unterstützt. Der lokale XML-Standardexport wird nicht verwendet.“

### 6.5. Korrektur des falschen Leistungsempfängers

Eine Rechnung wurde an die Rechtsschutzversicherung adressiert, obwohl der Mandant Empfänger der anwaltlichen Leistung ist. Der Vorgang wird nicht durch Umbenennen der PDF korrigiert. Prüfe die erteilte Rechnung, den Steuerausweis und den Versandstand; erstelle die Berichtigung mit Bezug auf die Ursprungsrechnung. Der Text lautet: „Die Rechnung Nr. 2026-0402 vom 30. September 2026 wird hinsichtlich des Leistungsempfängers berichtigt. Empfänger der dort bezeichneten anwaltlichen Leistung ist Herr Jonas Reinholt, Birkenweg 12, 14542 Werder (Havel). Die Zahlung durch die Versicherung erfolgt im Rahmen der dort bestehenden Deckung; sie ist Zahlerin, nicht Leistungsempfängerin. Leistungszeitraum, Leistungsumfang und Vergütung bleiben unverändert. Diese Berichtigung ist zusammen mit der ursprünglichen Rechnung aufzubewahren.“ Ob diese Ergänzung genügt oder ein Storno mit Neuausstellung erforderlich ist, wird am Ausgangsdokument entschieden.

### 6.6. Prüfprotokoll für eine exportierte XML-Datei

Ein interner Vermerk lautet: „Die Datei Rechnung_Entwurf_v2.xml wurde am 7. Oktober 2026 aus den freigegebenen Eingabedaten erzeugt. Die Honorargrundlage ist die Vereinbarung HV-1; der Leistungsnachweis umfasst die bestätigten Einträge [IDs]. Der inländische Steuerfall ergibt 19 Prozent Umsatzsteuer; Vorschussverrechnung, Rabatte und Gutschriften sind nicht enthalten. Die Datei wurde mit KoSIT-Validator [Version] und Konfiguration [Fassung] geprüft; das Ergebnis lautet [Befund]. Rechnungsnummer, Empfänger, Leistungszeitraum, Positionen, Steuer und Zahlbetrag stimmen mit den freigegebenen Daten überein. Der Versandstatus lautet [Status].“ Die Platzhalter sind keine voreingestellten positiven Ergebnisse; ein Validierungsfehler wird mit Regelkennung und betroffener Stelle benannt und durch die richtige Information behoben. Das Protokoll ist ein interner Nachweis und wird nicht als Rechnungsanlage versandt.
