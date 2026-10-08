---
name: abrechnung-e-rechnung
description: "Verwenden, wenn aus bestätigtem Honorar- und Leistungsstand eine Rechnung, ein Vorschusstext, eine Korrektur oder eine XRechnung für Unternehmer oder Behörde entstehen soll, B2G-Angaben fehlen oder eine Eingangsrechnung zu prüfen ist. Liefert versandfähigen Rechnungstext. Nicht für Honorargrundlage oder Zahlungen."
---

# Anwaltliche Rechnung und E-Rechnung erstellen

## 1. Zweck und Anwendungsfall

### 1.1. Von der dokumentierten Leistung zur konkreten Rechnung

Dieser Skill führt einen bestätigten Honorarstand und Zeitstand zu einer überprüfbaren Rechnung. Er verbindet anwaltliches Vergütungsrecht, Umsatzsteuer, Empfängeranforderungen und die tatsächliche technische Ausgabe. Das Ergebnis ist je nach Auftrag ein fertiger Rechnungstext, eine geprüfte strukturierte XML-Datei oder eine konkrete Korrekturrechnung. Ein bekannter Teilbetrag aus dem Mandatsjournal wird nicht als vollständige Forderung ausgegeben, solange wesentliche Positionen, Zuordnungen oder Grundlagen offen sind.

Rechtliche Abrechenbarkeit, rechnerische Richtigkeit und technische Konformität sind drei getrennte Prüfungen. Eine XML-Datei kann technisch gültig sein und dennoch den falschen Leistungsempfänger, ein nicht vereinbartes Honorar oder eine unzutreffende Umsatzsteuer enthalten. Der Skill dokumentiert deshalb, was geprüft wurde und welche Frage offen ist, und behauptet keine Freigabe allein aus einem erfolgreichen Export.

### 1.2. Die Rechnung ist kein bloßer Dateityp

Eine reine PDF-Datei ist eine sonstige Rechnung, keine E-Rechnung im Sinn von [§ 14 Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html). Eine E-Rechnung wird in einem strukturierten elektronischen Format ausgestellt, übermittelt und empfangen und ermöglicht die elektronische Verarbeitung; das Format muss der europäischen Norm für die elektronische Rechnungsstellung entsprechen oder zwischen den Parteien vereinbart sein und die richtige und vollständige Extraktion der Pflichtangaben in ein der europäischen Norm entsprechendes oder damit interoperables Format erlauben. Bei hybriden Formaten wie ZUGFeRD ist der XML-Teil führend; eine ansprechend gestaltete Sichtfassung heilt keine falschen XML-Daten.

Die endgültige Rechnungsnummer wird vor G4 kontrolliert in die zu prüfende Fassung aufgenommen; G4 Rechnungsausgabe bindet diese Nummer, Fassung und ihren Hash (3.17). Mitteilung, Buchung und Versand sind gesondert freizugebende Schritte; ein Versand erfolgt nur im Rahmen eines Auftrags. Weder der Dateiname „final“ noch ein internes Freigabefeld beweist den Zugang beim Empfänger.

### 1.3. Auslöser, Abgrenzung und Nachbarskills

Der Skill startet, wenn eine Honorarphase abgeschlossen ist und die Mandantin eine Rechnung erwartet, wenn der Rechtsschutzversicherer eine Berechnung nach § 10 RVG mit Gebührentatbeständen anfordert, wenn ein inländischer Unternehmensmandant ab dem Leistungsjahr 2026 eine XRechnung oder ZUGFeRD-Datei verlangt, wenn eine Behörde als Auftraggeberin Leitweg-ID und Portalweg vorgibt, wenn eine bereits gestellte Rechnung berichtigt oder storniert werden muss oder wenn die Kanzlei selbst eine Eingangsrechnung auf Pflichtangaben und Vorsteuerfähigkeit prüft.

Die Honorargrundlage wird in [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) festgelegt; dieser Skill übernimmt sie als gegeben und ändert sie nicht. Zeiteinträge entstehen in [Zeiten erfassen](../zeiten-erfassen/SKILL.md); hier werden sie nur abgerechnet. Zahlungseingänge, Vorschussverrechnung, Fremdgeld und Buchungsvorschläge gehören zu [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md). Die Schlussabrechnung beim Mandatsende und die Aufbewahrungsentscheidung für die Handakte steuert [Mandat abschließen](../mandat-abschliessen/SKILL.md). Das Anschreiben zur Rechnung mit Sachstand und Empfehlung entsteht in [Mandantenkommunikation](../mandantenkommunikation/SKILL.md). Einen offenen Steuerstreit oder eine unklare Verwaltungsauffassung klärt [Recht recherchieren](../recht-recherchieren/SKILL.md).

Dieser Skill verhandelt kein Honorar, erfasst keine Zeiten, bucht nicht, vollstreckt nicht und versendet nichts ohne Auftrag.

## 2. Eingaben

### 2.1. Honorarstand und Zeitstand

Lies die gültige Vergütungsvereinbarung, Nachträge, Gebührenblatt, bestätigte Zeitbelege, Auslagenbelege, bisherige Rechnungen, Vorschüsse und Zahlungseingänge. Halte Honorarstand und Zeitstand knapp vor: „Für die außergerichtliche Prüfung gilt die Vereinbarung vom 1. September 2026 mit 280 Euro netto je tatsächlicher Stunde und einem Gesamtdeckel von 2.500 Euro netto. Bestätigt sind sieben Stunden und 40 Euro eigene steuerpflichtige Auslagen.“ Steht fest, dass der Deckel Auslagen einschließt, wird das nicht erneut gefragt. Eine Rechnung darf eine unklare Preiszusage nicht in ein offenes Stundenhonorar umdeuten; bekannte Daten werden verwendet, während eine Zeitfrage aussteht, der Zeitstand bleibt erkennbar.

### 2.2. Parteien und Zustellungsdaten

Erfasse Rechnungsaussteller, umsatzsteuerlichen Leistungsempfänger, Auftraggeber, Rechnungsempfänger, Zahlenden und etwaige Rechnungsprüfer getrennt. Eine Rechtsschutzversicherung wird nicht allein wegen ihrer Zahlung zum Leistungsempfänger; sie ist Zahlerin im Rahmen der Deckung. Eine Konzernmutter, die Rechnungen zentral bearbeitet, ist nicht zwangsläufig Vertragspartnerin. Benötigt werden Rechnungsnummer, Ausstellungsdatum, Leistungszeitraum, Währung, Zahlungsbedingungen, Steuerbehandlung, Empfängerreferenzen und der vereinbarte oder vorgeschriebene Übermittlungsweg. Bei öffentlichen Auftraggebern kommen Leitweg-ID, Bestellnummer, elektronische Adresse und Portalvorgaben hinzu. Fehlende Referenzen werden nicht erfunden, um eine Validierung zu bestehen.

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

Stelle nur Fragen, deren Antwort das Ergebnis verändert, und bündle sie:

1. „Welche Honorargrundlage gilt für den Abrechnungszeitraum vom [Beginn] bis [Ende]: die Vereinbarung vom [Datum] mit [Satz oder Betrag], oder gab es einen Nachtrag?“
2. „Sind die Zeiteinträge [IDs] vollständig und abrechenbar, oder fehlen noch Leistungen, die in diese Rechnung gehören?“
3. „Wer ist umsatzsteuerlicher Leistungsempfänger: die Mandantin selbst, eine Gesellschaft der Gruppe oder eine andere Person? Wer zahlt?“
4. „Ist der Empfänger Unternehmer mit Sitz im Inland, im übrigen Gemeinschaftsgebiet oder im Drittland, oder Verbraucher?“
5. „Welche Vorschüsse oder Teilzahlungen sind auf diesen Abrechnungsabschnitt bereits eingegangen?“
6. „Verlangt der Empfänger XRechnung, ZUGFeRD oder akzeptiert er eine PDF-Rechnung mit Zustimmung, und welche Referenzen (Leitweg-ID, Bestellnummer, Kostenstelle) benötigt er?“
7. „Soll die Rechnung als Teil-, Vorschuss- oder Schlussrechnung bezeichnet werden?“

Ohne Antwort auf Frage 1 oder 2 wird keine Rechnung, sondern eine Leistungsaufstellung mit Platzhaltern erstellt. Fragen 3 bis 5 blockieren den Rechnungstext, nicht die Leistungsaufstellung. Fragen 6 und 7 blockieren nur das Format und die Bezeichnung; der Entwurf kann bis dahin als sonstige Rechnung im Zustand `entwurf` vorbereitet werden.

## 3. Ablauf und Checkliste

### 3.1. Forderung zuerst auf ihre Grundlage prüfen

Ermittle, welche Vergütung entstanden und fällig ist. Nach [§ 8 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__8.html) wird die Vergütung fällig, wenn der Auftrag erledigt oder die Angelegenheit beendet ist; bei gerichtlichen Verfahren zusätzlich mit Kostenentscheidung, Erledigung in der Instanz oder einem Ruhen des Verfahrens von mehr als drei Monaten. Nach [§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html) kann für die entstandenen und voraussichtlich entstehenden Gebühren und Auslagen ein angemessener Vorschuss gefordert werden; der Vorschuss ist keine Schlussrechnung und kein Anerkenntnis des späteren Endbetrags. Bei RVG werden Gebührentatbestände, Werte, Anrechnungen und das Übergangsrecht nach § 60 RVG anhand eines gesonderten Gebührenblatts geprüft; bei Rahmengebühren bestimmt der Anwalt den Satz nach [§ 14 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__14.html) nach billigem Ermessen unter Berücksichtigung aller Umstände, insbesondere Umfang und Schwierigkeit, Bedeutung der Angelegenheit sowie Einkommens- und Vermögensverhältnisse des Auftraggebers, und begründet einen über der Mittelgebühr liegenden Ansatz. Der Mindestbetrag einer Gebühr beträgt nach § 13 Absatz 3 RVG 15 Euro.

Bei Zeithonorar werden wirksame Grundlage, passende Tätigkeit, tatsächliche Dauer, gültiger Satz und Deckel kontrolliert. Bei Festpreis werden Leistungsumfang, Leistungsstand und Fälligkeitsregel betrachtet; der im Journal ausgewiesene volle Festpreis ist ein Vereinbarungswert, keine Aussage, dass er bereits verlangt werden darf. Die Erstattungsfähigkeit gegenüber Gegner oder Staatskasse unterscheidet sich vom Anspruch gegen den Mandanten; eine Deckungszusage ist keine Zustimmung zu jedem Honorar. Bei Beiordnung oder Beratungshilfe gelten die besonderen Grenzen.

### 3.2. Anwaltliche Berechnung nach § 10 RVG

Nach [§ 10 Absatz 1 RVG](https://www.gesetze-im-internet.de/rvg/__10.html) kann die Vergütung nur aufgrund einer in Textform erstellten und dem Auftraggeber mitgeteilten Berechnung eingefordert werden; die Mitteilung erfolgt durch den Rechtsanwalt oder auf seine Veranlassung. Eine eigenhändige Unterschrift ist zum Prüfstand nicht mehr Voraussetzung. Ein intern fortgeschriebener Entwurf ist noch keine mitgeteilte Berechnung. Der Lauf der Verjährung hängt nicht von der Mitteilung ab; eine liegengebliebene Rechnung wird nicht automatisch rechtzeitig.

Für gesetzliche Gebühren verlangt § 10 Absatz 2 RVG die Beträge der einzelnen Gebühren und Auslagen, die Vorschüsse, eine kurze Bezeichnung des jeweiligen Gebührentatbestands, die Bezeichnung der Auslagen, die angewandten Nummern des Vergütungsverzeichnisses und bei Wertgebühren den Gegenstandswert; bei Rahmengebühren wird der Betrag der konkret bestimmten Gebühr angegeben; der gewählte Satz wird genannt, damit die Bestimmung nach § 14 RVG nachvollziehbar bleibt. Bei Zeithonorar muss die Leistungsdarstellung eine Prüfung ermöglichen: Datum, Person, Dauer und konkrete Tätigkeit je Eintrag. Ein einheitlicher Text „Beratung im Oktober“ genügt für einen streitigen Stundenanspruch nicht; die Zeitaufstellung verteilt keine vertraulichen Einzelheiten an unberechtigte Dritte.

Die vom Mandanten erbetene Rechnungserläuterung ist kein neuer Gebührenanspruch, nur weil ihre Erstellung Zeit kostet. Kosten der Korrektur eigener Rechnungsfehler werden nicht weiterberechnet.

### 3.3. Auslagen nach Teil 7 des Vergütungsverzeichnisses

Auslagen werden einzeln nach [Anlage 1 zum RVG](https://www.gesetze-im-internet.de/rvg/anlage_1.html) angesetzt. Die Dokumentenpauschale nach Nr. 7000 VV RVG beträgt bei Schwarz-Weiß-Kopien für die ersten 50 abzurechnenden Seiten je 0.50 Euro und danach 0.15 Euro, bei Farbe 1.00 beziehungsweise 0.30 Euro; sie entsteht nur für die dort genannten Fälle, etwa Abschriften aus Behörden- und Gerichtsakten, soweit deren Herstellung zur sachgemäßen Bearbeitung geboten war, oder Kopien, die im Einverständnis mit dem Auftraggeber zusätzlich angefertigt werden; Nr. 7000 Nummer 1 Buchstabe b verlangt gesetzlich oder von der Verfahrensstelle veranlasste Übermittlung, Buchstabe c notwendige Unterrichtung des Auftraggebers; in beiden Fällen zählt nur der über 100 Seiten hinausgehende Umfang. Interne Arbeitskopien lösen sie nicht aus. Die Pauschale für Post- und Telekommunikationsdienstleistungen nach Nr. 7002 VV RVG beträgt 20 Prozent der Gebühren, höchstens 20 Euro je Angelegenheit; alternativ können die tatsächlichen Entgelte nach Nr. 7001 VV RVG abgerechnet werden, nicht beides. Fahrtkosten mit eigenem Kraftfahrzeug nach Nr. 7003 VV RVG betragen 0.42 Euro je gefahrenen Kilometer; Tage- und Abwesenheitsgeld nach Nr. 7005 VV RVG richtet sich nach der Abwesenheitsdauer. Die Umsatzsteuer auf Gebühren und Auslagen wird nach Nr. 7008 VV RVG in voller Höhe angesetzt, soweit sie nicht nach § 19 UStG unerhoben bleibt.

Bei Zeithonorar gelten diese Nummern nur, wenn die Vereinbarung auf sie verweist; sonst sind Auslagen so abzurechnen, wie die Vereinbarung sie regelt. Ein Gerichtskostenvorschuss, den die Kanzlei im Namen und für Rechnung der Mandantin verauslagt hat, ist ein durchlaufender Posten und erhält keine Umsatzsteuer; eine im eigenen Namen bezogene Fremdleistung ist dagegen Teil der steuerpflichtigen Leistung. Rechnungsbeleg, Schuldner der Fremdforderung und Handeln im eigenen oder fremden Namen entscheiden, nicht das Wort „Auslage“.

### 3.4. Rechenweg und Deckelabgleich

Berechne jede Position aus der zutreffenden Grundlage. Bei Stundenhonorar werden tatsächliche Minuten in Stunden umgerechnet und mit dem gültigen Satz bewertet; Festpreise werden nicht zusätzlich um Zeitwerte erhöht. Bei einem Deckel wird geprüft, ob er Gebühren allein oder Gebühren und Auslagen umfasst. Ein verbrauchter Gesamtdeckel wird nicht durch eine neue Rechnungsnummer, einen neuen Monat oder eine neue Phase zurückgesetzt. Beispiel: Bestätigte Zeitwerte betragen 2.420 Euro netto und eigene steuerpflichtige Auslagen 160 Euro netto. Bei einem gemeinsamen Deckel von 2.500 Euro netto darf der Entwurf nicht 2.580 Euro ansetzen; bei einem nur auf Honorar bezogenen Deckel kann die Behandlung anders ausfallen, wenn die Auslagenerstattung wirksam vereinbart ist. Dokumentiere tatsächlichen Aufwand und begrenzten Ansatz getrennt.

Kontrolliere Geldrundung, Steuerbasis und Gesamtsumme. Die Summe einzeln gerundeter Positionen kann von einer erst am Ende gerundeten Gesamtzeit abweichen; verwende einen konsistenten Rechenweg und gleiche XML, Sichtfassung und Buchungsvorschlag ab.

### 3.5. Umsatzsteuer und Pflichtangaben

Prüfe die Pflichtangaben nach [§ 14 Absatz 4 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html): vollständiger Name und Anschrift von Leistendem und Leistungsempfänger, Steuernummer oder USt-IdNr. des Leistenden, Ausstellungsdatum, fortlaufende einmalige Rechnungsnummer, Art und Umfang der Leistung, Zeitpunkt oder Zeitraum der Leistung, nach Steuersätzen aufgeschlüsseltes Entgelt, anzuwendender Steuersatz und Steuerbetrag beziehungsweise Hinweis auf eine Steuerbefreiung, bei Vorauszahlungen den Vereinnahmungszeitpunkt, sofern er feststeht und vom Ausstellungsdatum abweicht (§ 14 Absatz 4 Satz 1 Nummer 6 UStG). Leistungsbeschreibung und Leistungszeitraum werden nicht durch das Ausstellungsdatum ersetzt. Die Rechnung ist nach § 14 Absatz 2 UStG innerhalb von sechs Monaten nach Ausführung der Leistung auszustellen, wenn ein Unternehmer die Leistung für sein Unternehmen bezieht oder eine nichtunternehmerische juristische Person Empfängerin ist und die gesetzliche Befreiungsausnahme nicht eingreift. Die übrigen Tatbestände und Sonderfristen werden gesondert geprüft.

Für Kleinbetragsrechnungen bis einschließlich 250 Euro brutto gelten die erleichterten Angaben nach [§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html). Eine Kanzlei, die als Kleinunternehmerin nach [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) steuerfrei leistet, weist keine Umsatzsteuer aus und vermerkt die Steuerbefreiung; Voraussetzung ist nach § 19 Absatz 1 UStG, dass der Gesamtumsatz im vorangegangenen Kalenderjahr 25.000 Euro nicht überschritten hat und im laufenden Kalenderjahr 100.000 Euro nicht überschreitet. Weist eine Rechnung einen höheren Steuerbetrag aus, als geschuldet wird, schuldet der Aussteller nach [§ 14c Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) auch den Mehrbetrag; bei Berichtigung gegenüber dem Empfänger gilt § 17 Absatz 1 entsprechend. § 14c Absatz 1 Satz 3 verweist nur für seine besonderen Fälle auf Absatz 2 Satz 3 bis 5. Bei unberechtigtem Steuerausweis nach Absatz 2 setzt die Berichtigung dagegen die Beseitigung der Gefährdung des Steueraufkommens und das dort geregelte Antrags- und Zustimmungsverfahren beim Finanzamt voraus. Deshalb werden Testdateien mit fiktiven Daten getrennt gehalten; die Bezeichnung „Entwurf“ schützt nicht, wenn ein Dokument tatsächlich wie eine Rechnung verwendet wird.

### 3.6. Leistungsort, Auslandsmandant und Steuerschuldnerschaft

Bei einem Mandanten mit Sitz außerhalb Deutschlands wird zuerst der Leistungsort bestimmt. Eine sonstige Leistung an einen Unternehmer für sein Unternehmen wird nach [§ 3a Absatz 2 UStG](https://www.gesetze-im-internet.de/ustg_1980/__3a.html) an dem Ort ausgeführt, von dem aus der Empfänger sein Unternehmen betreibt; liegt dieser Ort oder die maßgebliche empfangende Betriebsstätte im Ausland und greift keine Sonderregel insbesondere aus den Absätzen 3 bis 8 ein, ist die Leistung in Deutschland nicht steuerbar. Wird die Leistung nach § 3a Absatz 2 im übrigen Gemeinschaftsgebiet ausgeführt und schuldet der unternehmerische Empfänger dort die Steuer, wird die Rechnung ohne deutsche Umsatzsteuer mit der Angabe „Steuerschuldnerschaft des Leistungsempfängers“ sowie mit der USt-IdNr. der Kanzlei und des Empfängers nach [§ 14a Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html) ausgestellt; die dort vorgesehene Ausstellungsfrist bis zum 15. des Folgemonats und die Zusammenfassende Meldung werden an [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md) übergeben. Beratungsleistungen an einen Nichtunternehmer im Drittland sind nach § 3a Absatz 4 UStG gesondert zu prüfen. Bei Leistungsbezug von ausländischen Unternehmern prüft die Kanzlei die erfasste Leistungsart und inländische Steuerbarkeit nach [§ 13b Absätze 1, 2 und 5 UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html); der ausländische Sitz allein begründet keine Steuerschuldnerschaft. Das lokale Skript unterstützt keinen dieser Fälle; der Rechnungstext wird dann ohne XML-Export erstellt und der Steuervermerk vor Freigabe gegen den aktuellen Normtext geprüft.

### 3.7. Entscheidungsbaum für das erforderliche Rechnungsformat

Prüfe zuerst, ob der Umsatz unter die inländische B2B-Regel fällt: Leistender und Leistungsempfänger sind Unternehmer mit Sitz im Inland und die Leistung wird für das Unternehmen bezogen. Ist der Empfänger Verbraucher, besteht keine E-Rechnungspflicht; eine PDF oder Papierrechnung bleibt zulässig. Ist der Empfänger eine öffentliche Stelle, gelten zusätzlich die Vorgaben des Bundes oder des Landes für den Empfangsweg, insbesondere die ERechV des Bundes und die Landesregelungen mit Leitweg-ID. Bei Auslandsbezug ist die inländische B2B-Route nicht schematisch anzuwenden. Eine vertragliche Formatvereinbarung bleibt daneben relevant.

Prüfe danach die Übergangsregel in [§ 27 Absatz 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html). Für vom 1. Januar 2025 bis 31. Dezember 2026 ausgeführte Umsätze erlaubt Nummer 1 die Übermittlung einer sonstigen Rechnung bis zum 31. Dezember 2026: auf Papier oder mit Zustimmung elektronisch. Nummer 2 erlaubt dies bis zum 31. Dezember 2027 für im Jahr 2027 ausgeführte Umsätze, wenn der Gesamtumsatz des Ausstellers im Vorjahr nicht mehr als 800.000 Euro betrug; Nummer 3 betrifft mit Zustimmung übermittelte EDI-Rechnungen für 2027 ebenfalls nur bis Ende 2027. Leistungs- und Übermittlungsdatum müssen jeweils passen. Ab dem 1. Januar 2028 entfallen die Übergänge, nicht die gesetzlichen Ausnahmen für Kleinbetragsrechnungen und Kleinunternehmer. Die Pflicht, E-Rechnungen empfangen zu können, besteht für inländische Unternehmer unabhängig davon seit 2025.

Halte das Ergebnis in einem Satz mit Tatsachengrundlage fest: „Für diesen inländischen unternehmerischen Leistungsempfänger ist die XRechnung der Zielstandard; die Übergangsmöglichkeit für 2026 wird nicht benötigt, weil der Empfänger XRechnung 3.0 akzeptiert.“ Der Satz „Seit 2025 muss jede Rechnung XML sein“ ist falsch.

### 3.8. Empfängeranforderungen und Datenminimierung

Kontrolliere, welche Daten der Empfänger für die Zuordnung benötigt und welche die Rechnung rechtlich enthalten muss. Eine Einkaufsabteilung kann Bestellnummern verlangen, ohne vertrauliche Beratungsinhalte zu erhalten; die Leistungsbeschreibung wird aussagekräftig, aber begrenzt formuliert. Eine Leitweg-ID wird aus dem Auftrag oder einer authentisch bestätigten Mitteilung übernommen; ihre formale Plausibilität beweist nicht die Zuordnung zur richtigen Behörde. Dasselbe gilt für elektronische Adressen und Bankdaten; eine kurz vor Rechnungsstellung per E-Mail mitgeteilte neue Bankverbindung wird nach dem Kanzleiverfahren unabhängig bestätigt. Bei einem externen Rechnungsprüfer des Mandanten werden Rolle, Vertraulichkeit und Datenumfang geklärt; der Skill erzeugt eine Leistungsaufstellung, keine Freigabe der Akte.

### 3.9. Den Journalentwurf fachlich freigeben

Lies `rechnungsentwurf.json` aus dem Mandatsordner nach [Mandatsordner und CLI](../../references/mandatsordner-und-cli.md) mit Journalrevision, Phasen, offenen Positionen und Zahlungen. Das Feld `complete` bedeutet nur, dass die erkannten Erfassungsfragen geschlossen sind; `invoice_ready` bleibt bewusst falsch. Zahlungen werden gesondert gezeigt und nicht verrechnet. RVG-Beträge werden über den Befehl `manual-fee` von [kanzlei.py](../../scripts/kanzlei.py) nur mit geprüftem Gebührenblatt und `legal_reviewed=true` übernommen; das Feld bestätigt eine Prüfung, es rechnet nicht.

### 3.10. XRechnung mit dem vorhandenen Skript erzeugen

Das Skript [xrechnung.py](../../scripts/xrechnung.py) kennt genau die Optionen `--input` und `--output`. Die Eingabedatei nach `assets/xrechnung-beispiel.json` enthält `schema_version` mit dem Wert 1, `document_state` (`draft` oder `approved`), `legal_reviewed`, `invoice_number`, `issue_date`, `due_date`, `period_start`, `period_end` im Format JJJJ-MM-TT, `currency` mit dem Wert EUR, `vat_rate` mit dem Wert 19, `buyer_reference`, die Blöcke `supplier` (mit `name`, `street`, `postal_code`, `city`, `country`, `email`, `vat_id`, `contact`, `phone`, `iban`) und `customer` (mit `name`, `street`, `postal_code`, `city`, `country`, `email`) sowie die Liste `lines` mit `id`, `description`, `quantity`, `unit_code` und `unit_price_net`. Zulässige Einheiten sind `C62`, `HUR`, `MIN` und `DAY`; Mengen müssen positiv sein; Menge und Einzelpreis dürfen höchstens sechs Nachkommastellen haben. Beide Parteien müssen `country` gleich `DE` haben. Die Schlüssel `allowances`, `prepaid_amount`, `credit_note` und `reverse_charge` führen zum Abbruch, damit kein Sonderfall stillschweigend ausgelassen wird.

Der Aufruf lautet `python3 "<Pluginordner>/scripts/xrechnung.py" --input "<Rechnungsdaten.json>" --output "<Mandatsordner>/02_Honorar/Rechnung_Entwurf_v1.xml"`. Eine vorhandene Ausgabedatei wird nicht überschrieben; eine Korrektur erhält eine neue Versionsdatei. `document_state=draft` setzt einen Entwurfshinweis in das Feld `Note`; `approved` setzt `legal_reviewed=true` voraus, ersetzt aber weder eine echte Freigabe noch den Versandauftrag. Das Skript erzeugt UBL mit der CustomizationID für XRechnung 3.0, Rechnungstyp 380, Zahlungsart 58 mit IBAN, prüft Datumsfolgen, doppelte Positions-IDs, das Muster der deutschen USt-IdNr. und die IBAN-Prüfziffer. Es prüft weder ein Nummernregister noch die Echtheit von Steuer- oder Kontodaten und gibt `kosit_validated` stets als falsch aus. Die Testdaten des Beispiels dürfen nicht in eine reale Rechnung gelangen.

### 3.11. Technische Validierung und Sichtkontrolle

Nach dem zum Prüfstand 8. Oktober 2026 gelesenen Stand der KoSIT-Versionsseite ist XRechnung 3.0 die normative Version; das aktuelle Bundle ist 3.0.2 Summer 2026 Bugfix vom 31. August 2026, die im September veröffentlichte Spezifikation 4.0 ist eine Vorversion. Prüfe vor jedem produktiven Export den Stand auf der [KoSIT-Versionsseite](https://xeinkauf.de/xrechnung/versionen-und-bundles/) und das vom Empfänger akzeptierte Profil. Validiere jede exportierte Datei mit dem aktuellen KoSIT-Validator und der passenden Konfiguration; dokumentiere Version, Konfiguration, Datei und Ergebnis. Eine XSD-Prüfung allein genügt nicht; Geschäftsregeln und Empfängerregeln sind einzubeziehen, Warnungen werden inhaltlich bewertet. Vergleiche anschließend eine lesbare Visualisierung mit den freigegebenen Eingaben. Bei Abweichungen wird die Ursache in den strukturierten Daten korrigiert und erneut validiert.

### 3.12. Rechnungsnummer, Korrektur und Archiv

Die Rechnungsnummer wird aus dem kanzleiweiten Register vergeben; das Skript führt kein Register. Entwurfsnummern werden nicht in die produktive Folge übernommen. Bei Fehlern in einer ausgestellten Rechnung prüfe, ob eine Ergänzung, eine Berichtigung mit eindeutigem Bezug auf die Ursprungsrechnung oder ein Storno mit neuer Rechnung erforderlich ist. Ein Storno weist denselben Betrag mit umgekehrtem Vorzeichen aus und nennt Nummer und Datum der stornierten Rechnung; die Neuausstellung erhält eine neue Nummer. Verwende das Wort „Gutschrift“ nicht unbedacht, weil es im Umsatzsteuerrecht die vom Leistungsempfänger ausgestellte Rechnung bezeichnet; für Korrekturen eignet sich „Rechnungskorrektur“ oder „Stornorechnung“.

Archiviere Originaldaten, Sichtfassung, Validierungsbericht, Freigabe und Übermittlungsnachweis in nachvollziehbarer Zuordnung. Nach [§ 14b Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html) sind ein Doppel jeder ausgestellten und alle empfangenen Rechnungen acht Jahre aufzubewahren, beginnend mit dem Schluss des Kalenderjahres der Ausstellung; § 27 Absatz 40 UStG erstreckt die Verkürzung auf am 31.12.2024 noch nicht abgelaufene Fristen; für die dort genannten beaufsichtigten Finanzunternehmen gilt sie erst ab 01.01.2026. [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html) nennt für Buchungsbelege ebenfalls acht Jahre, für Bücher, Inventare und Jahresabschlüsse zehn Jahre und für übrige Unterlagen sechs Jahre; der Übergang für Buchungsbelege folgt [Artikel 97 § 19a EGAO](https://www.gesetze-im-internet.de/aoeg_1977/art_97__19a.html), der für die dort genannten Finanzunternehmen weiterhin die frühere Fassung vorsieht. Die Handakte wird getrennt im Abschlussskill beurteilt. Der Prüfpfad muss Beleg, Erfassung und Korrektur nachvollziehbar verbinden; eine E-Rechnung wird im strukturierten Format aufbewahrt, das Ausdrucken und Löschen der XML-Datei genügt nicht.

### 3.13. Tatsächliche Mitteilung und Zahlungsüberwachung

Vor einem beauftragten Versand werden Empfänger, Kanal, Fassung und Anlagen kontrolliert; der Versandstatus wird erst nach Durchführung gesetzt. Eine Portalannahme ist eine technische Bestätigung, kein Ausschluss materieller Einwendungen. Fälligkeit und Verzug folgen aus Gesetz, Vertrag, Zugang und gegebenenfalls Mahnung; die 30-Tage-Regel des § 286 Absatz 3 BGB setzt gegenüber Verbrauchern den besonderen Hinweis in der Rechnung voraus. Ein frei gewähltes Fälligkeitsdatum im XML begründet keine fehlende Vereinbarung.

### 3.14. Berichtigung und Vorsteuer zeitlich präzise behandeln

Eine Korrektur kann fehlende Steuernummer, ungenaue Leistungsbeschreibung, falschen Zeitraum, falschen Empfänger oder fehlenden Steuerausweis betreffen; diese Fehler haben nicht dieselbe Rechtsfolge. Prüfe, ob das Ursprungsdokument die Mindestangaben einer berichtigungsfähigen Rechnung enthält und ob die materiellen Voraussetzungen des Vorsteuerabzugs nach [§ 15 Absatz 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html) vorliegen. Eine Ergänzung wird weder pauschal als rückwirkend noch pauschal als nur zukünftig wirkend behandelt. Der Beschluss des BFH vom 26. Februar 2026 lässt die Frage der zeitlichen Ausübung des Vorsteuerabzugs bei einem zunächst nicht berichtigungsfähigen Dokument zur Revision zu; das ist ein Anlass zur Aktualitätskontrolle, keine Antwort. Benenne im Vermerk die konkrete Unsicherheit. Der neue Datensatz verweist auf die Ursprungsrechnung; der frühere wird weder gelöscht noch überschrieben.

### 3.15. Teilrechnung und mehrere Angelegenheiten

Eine Teilrechnung verlangt einen abgegrenzten Abrechnungsabschnitt und darf nicht den Eindruck erwecken, der Auftrag sei beendet. Bei mehreren RVG-Angelegenheiten werden Entstehung, Anrechnung und Übergangsrecht je Angelegenheit geprüft; eine Sammelrechnung stellt die Grundlagen getrennt dar. Eine periodenbezogene Stundenrechnung braucht den Abgleich mit bereits abgerechneten Zeiten; ein Abrechnungsnachweis hält fest, welche Eintrags-IDs welcher Rechnung zugeordnet wurden.

### 3.16. Eingangsrechnungen der Kanzlei prüfen

Bei einer Lieferantenrechnung beginnt der Ablauf beim Leistungsbezug: Bestellung, Vertrag, gelieferte Leistung und Rechnung werden verglichen. Eine formal gültige XRechnung beweist weder vollständige Leistung noch richtigen Preis. Prüfe Doppelrechnungen, erfolgte Zahlungen, Kontoverbindungen und Nebenentgelte. Die Vorsteuerfrage nach § 15 UStG wird von der Zahlungsfreigabe getrennt. Für die Buchhaltung werden Original-XML, Anlagen und Prüfhinweise übergeben. Ein Rückfragetext lautet: „Ihre Rechnung [Nummer] vom [Datum] bezeichnet als Leistungszeitraum lediglich den Ausstellungsmonat. Nach unserem Auftrag betrifft die Rechnung die Leistungen vom [Beginn] bis [Ende]. Bitte prüfen Sie den Zeitraum und übersenden Sie eine gegebenenfalls erforderliche Berichtigung mit eindeutigem Bezug auf die ursprüngliche Rechnung.“

### 3.17. Agentischer Lauf und Freigabestufe

Im Mandatslauf nach [Mandatslauf und Freigaben](../../references/mandatslauf-und-freigaben.md) führt dieser Skill die Phase `abrechnung`, die er mit [Zeiten erfassen](../zeiten-erfassen/SKILL.md) und [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) teilt, zu Ende. Sie endet mit dem Rechnungsentwurf oder der freigegebenen Rechnung; der XML-Entwurf ist ein zweites Produkt derselben Phase. Eine Vorschussrechnung während laufender Sacharbeit läuft als Nebenlauf `abrechnung`.

| Stufe | Ohne Rückfrage |
| --- | --- |
| 0 | Journal und Belege lesen; Rechnungstext, Leistungsaufstellung und Prüfvermerk als Text liefern; keine Datei schreiben |
| 1 | Leistungsaufstellung und Prüfvermerk intern unter `01_Bearbeitung` anlegen; keine ausgabefertige Rechnung erzeugen |
| 2 | Bestätigte Journalwerte und geprüfte Gebühren übernehmen; interne Rechnungsentwürfe fortschreiben; Abrechnungsnachweis, Produkte und Gates führen |
| 3 | Ausgabefertiges Rechnungs-/XML-Paket vorbereiten; endgültige Nummer kontrolliert einsetzen, erneut prüfen und G4 für Fassung und Hash öffnen |

Ohne namentliche menschliche Freigabe setzt der Skill `document_state` nicht auf `approved`, teilt die Berechnung nach § 10 RVG mit, reicht über ein Portal ein, versendet oder bucht; diese Handlungen hängen am Gate G4 Rechnungsausgabe. Der Skill öffnet G4, sobald der Entwurf den Fehlerkatalog in 3.18 durchlaufen hat und bei einer XML-Datei das Validierungsergebnis dokumentiert ist; Bezug sind registrierte Produkt-ID, endgültige Nummer, Fassung und Hash des Rechnungs-/XML-Pakets. Die verantwortliche Person wird beim Öffnen von G4 namentlich eingetragen. Eine Nummern- oder Inhaltsänderung verlangt erneute Prüfung und Freigabe. Nach Freigabe werden tatsächliches Mitteilungsdatum und Weg sowie die belegte Fälligkeit ergänzt; der Skill setzt das Produkt auf `freigegeben` und übergibt an [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md). Soll ein externer Rechnungs- oder Portaldienst Daten erhalten, wird vorher über [Workflow-Übergabe](../workflow-uebergabe/SKILL.md) das Gate G6 Dienstleister geöffnet.

Im Produktregister trägt der Skill `rechnung` und bei XML-Erstellung `rechnung-xml` als `entwurf` ein; nach Fehlerkatalog und dokumentierter Validierung setzt er `geprueft` und stößt ohne Rückfrage [Mandantenkommunikation](../mandantenkommunikation/SKILL.md) für das Anschreiben an, das bis zur Freigabe als Entwurf wartet:

```bash
python3 "<Pluginordner>/scripts/mandatslauf.py" phase --akte "/Mandate/M-26-104" --phase abrechnung --grund "Schlussrechnung außergerichtliche Vertretung bestellt"
python3 "<Pluginordner>/scripts/mandatslauf.py" product --akte "/Mandate/M-26-104" --id rechnung-xml --pfad "02_Honorar/Rechnung_Entwurf_v2.xml" --skill abrechnung-e-rechnung --zustand geprueft
python3 "<Pluginordner>/scripts/mandatslauf.py" gate --akte "/Mandate/M-26-104" --gate G4 --aktion oeffnen --bezug rechnung-xml --person "Dr. Frieda Blum"
python3 "<Pluginordner>/scripts/mandatslauf.py" next --akte "/Mandate/M-26-104"
```

[mandatslauf.py](../../scripts/mandatslauf.py) berechnet den Hash selbst und weist `freigegeben` ohne geprüfte Fassung ab. Stoppregel: Der Skill bleibt stehen, wenn Leistungsempfänger, Honorargrundlage oder der Steuervermerk bei Auslandsbezug nicht feststeht; ein tatsächlich als Rechnung in Verkehr gebrachtes Dokument kann ungeachtet seines Entwurfstitels § 14c UStG auslösen.

### 3.18. Typische Fehler und Gegenkontrolle

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

### 3.19. Übergabe an Nachbarskills

Jede Übergabe nennt die führende Fassung mit Pfad und Hash, den Honorarstand (Modell, Satz oder Betrag, Umfang, Deckel, netto oder brutto), den Zeitstand (bestätigte Minuten, offene Zeitfragen), die offenen Gates und die offenen Fragen. An [Zahlungen und Buchhaltung](../zahlungen-buchhaltung/SKILL.md) geht nach Freigabe von G4 die führende Fassung der Rechnung mit Nummer, Datum, Netto, Steuer, Brutto, Fälligkeit und Belegreferenz sowie die Liste der verrechneten Vorschüsse; zurück kommen die Zahlungszuordnung, offene Restbeträge und ein Buchungsvorschlag. An [Mandantenkommunikation](../mandantenkommunikation/SKILL.md) geht der versandfähige Rechnungstext mit der Information, welche Honorarphase abgerechnet ist und welche offen bleibt; zurück kommt das Anschreiben mit Sachstand und nächsten Schritten. An [Mandat abschließen](../mandat-abschliessen/SKILL.md) geht die Schlussrechnung mit Abgleich aller Eintrags-IDs; zurück kommt die Bestätigung, dass keine abrechenbare Leistung offen ist. An [Workflow-Übergabe](../workflow-uebergabe/SKILL.md) geht der Prüfvermerk mit den Punkten, die eine fachliche Abnahme verlangen, insbesondere Rahmengebührensatz und Steuervermerk bei Auslandsbezug. Ergibt sich während der Abrechnung, dass der Honorarstand unklar ist, geht die Frage an [Honorar und Budget vereinbaren](../honorar-budget-vereinbaren/SKILL.md) zurück; die Rechnung wartet. Ein Fristobjekt entsteht hier nur, wenn eine Ausstellungsfrist nach § 14 Absatz 2 oder § 14a Absatz 1 UStG läuft; es wird als erfasst an [Fristen berechnen und überwachen](../fristen-berechnen-ueberwachen/SKILL.md) übergeben, nicht selbst eingetragen. Der Honorar- und Zeitanschluss aus [Arbeitsweise](../../references/arbeitsweise.md) gilt dabei unverändert: Gespeicherten Honorarstand vorhalten, nur entscheidende Lücken erfragen.

## 4. Quellenpflicht

### 4.1. Normen und amtliche technische Quellen

Beachte [Zitierweise](../../references/zitierweise.md) und [Rechtsquellen](../../references/rechtsquellen.md). Tragende Normlinks sind [§ 8 RVG](https://www.gesetze-im-internet.de/rvg/__8.html), [§ 9 RVG](https://www.gesetze-im-internet.de/rvg/__9.html), [§ 10 RVG](https://www.gesetze-im-internet.de/rvg/__10.html), [§ 13 RVG](https://www.gesetze-im-internet.de/rvg/__13.html), [§ 14 RVG](https://www.gesetze-im-internet.de/rvg/__14.html), [§ 60 RVG](https://www.gesetze-im-internet.de/rvg/__60.html), [Anlage 1 zum RVG](https://www.gesetze-im-internet.de/rvg/anlage_1.html), [§ 3a UStG](https://www.gesetze-im-internet.de/ustg_1980/__3a.html), [§ 13b UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html), [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 14a UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html), [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html), [§ 15 UStG](https://www.gesetze-im-internet.de/ustg_1980/__15.html), [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html), [§ 27 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html), [§ 33 UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__33.html) und [§ 147 AO](https://www.gesetze-im-internet.de/ao_1977/__147.html). Für die E-Rechnung werden die [BMF-Information](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) und die [KoSIT-Versionsseite](https://xeinkauf.de/xrechnung/versionen-und-bundles/) herangezogen. Verwaltungsauffassung, Gesetz, Gerichtsentscheidung und eigene technische Umsetzung bleiben unterscheidbar.

### 4.2. Verifizierte Entscheidungsanker

BFH, Urt. v. 20.10.2016 – Az. V R 26/15, Rn. 19–23, [amtlicher Volltext](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE201610285/). Trägt: Eine Rechnung mit bestimmten Mindestangaben kann mit Rückwirkung berichtigt werden. Trägt nicht: Die Heilung eines Dokuments ohne diese Mindestangaben, einen Vorsteuerabzug ohne materielle Voraussetzungen oder eine Rückwirkung bei fehlendem Leistungsempfänger.

BFH, Beschl. v. 26.02.2026 – Az. V B 11/25, Rn. 2, [amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/). Trägt: Die Frage der zeitlichen Ausübung des Vorsteuerabzugs bei ursprünglich nicht berichtigungsfähigem Dokument ist zur Revision zugelassen; der Beschluss beantwortet die Rechtsfrage nicht und belegt keinen späteren Verfahrensstand. Trägt nicht: Irgendeine Sachaussage über den Ausgang; der Beschluss entscheidet die Rechtsfrage nicht.

BGH, Urt. v. 12.09.2024 – Az. IX ZR 65/23, Rn. 16 und 34–37, [amtlicher Volltext im Curia-Archiv](https://curia.europa.eu/site/upload/docs/application/pdf/2025-04/ix_zr__65-23_2025-04-16_15-06-53_148.pdf). Trägt: Die Zeitabrechnung muss nachprüfbar darlegen, welche Tätigkeit wann und wie lange erbracht wurde. Trägt nicht: Ein Verbot anwaltlicher Stundenhonorare oder die Annahme, ein technischer Rechnungsstandard ersetze diese Darlegung.

BGH, Urt. v. 19.02.2026 – Az. IX ZR 226/22, Rn. 29–34, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1). Trägt: Eine formularmäßige Fiktion, nicht binnen Monatsfrist beanstandete Zeitaufstellungen gälten als anerkannt, ist auch gegenüber Unternehmern unwirksam. Trägt nicht: Die Unwirksamkeit der gesamten Vergütungsvereinbarung oder den Wegfall des übrigen Honoraranspruchs.

### 4.3. Belegdisziplin

Prüfstand ist der 08.10.2026. Die amtlichen Volltexte wurden für diese Fassung geöffnet und die einschlägigen Absätze beziehungsweise Randnummern gelesen; das Quellenprotokoll nennt Abrufdatum und gelesene Fundstellen. Bei der Mandatsbearbeitung wird der zum Sachverhalt passende Rechtsstand einschließlich Übergangsrecht erneut bestimmt. Eine ungeklärte Quelle bleibt eine interne Rechercheaufgabe und wird nicht als gesicherte Aussage in den Empfängertext übernommen. Jede Entscheidung nennt Gericht, Entscheidungsform, Datum, Aktenzeichen, amtliche Quelle und gelesene Randnummer. Kommentar-, Handbuch- und Aufsatzfundstellen werden nicht als Nachweise verwendet. Jeder Anker behält seine positive Aussage und seine Übertragungsgrenze; eine Präjudizienbindung wird nicht behauptet.

## 5. Ausgabeformat

### 5.1. Rechnung, Nachweise und Status

Liefere eine vollständige Rechnung beziehungsweise einen klar bezeichneten Entwurf, die Leistungsaufstellung und einen getrennten internen Prüfvermerk mit führender Fassung, offenen Gates und offenen Fragen. Bei XML-Erstellung kommen die Datei und der konkrete Validierungsstatus hinzu. Nenne einen fehlenden Pflichtwert genau. Behaupte keine Validierung, wenn nur exportiert wurde, und keinen Versand, wenn nur Dateien erstellt wurden. Eine ungelöste Steuerfrage wird nicht durch einen Haftungsausschluss verdeckt.

Das Endprodukt wird in vollständigen, ausformulierten Sätzen geliefert; Skelette, Halbsätze und reine Aufzählungsgerüste sind als Endprodukt verboten. Tabellen dürfen Rechnungspositionen darstellen. Lesbare formatierte Dokumente verwenden soweit technisch möglich Times New Roman, 11 pt und ausschließlich dezimale Gliederung; strukturierte XML-Felder folgen dem technischen Standard. Technische Prüfhinweise und der Exporthinweis stehen außerhalb des versandfähigen Rechnungstextes in einer gesonderten Notiz an den Auftraggeber. Platzhalter wie [Rechnungsnummer] oder [Leitweg-ID] bleiben lesbar und werden vor Versand ersetzt.

### 5.2. Abnahmekriterien

Zur Abnahme wird jede Position anhand eines Belegs oder Gebührenblatts nachvollzogen; Netto, Steuer und Brutto müssen stimmen. Leistungsempfänger, Rechnungsempfänger und Zahler sind getrennt bezeichnet. Die einschlägigen Angaben nach § 10 Absatz 2 RVG und § 14 UStG sind vollständig; ein fehlender Pflichtwert bleibt im Entwurf sichtbar und sperrt die Ausgabe. Die Formatentscheidung nennt ihre Tatsachengrundlage. Für XML dokumentiert der Prüfvermerk Validator, Konfiguration und Ergebnis; eine ausstehende Validierung sperrt die technische Freigabe. Vorschüsse und Teilzahlungen sind abgeglichen und in der ausgabefertigen Rechnung zutreffend verrechnet. Nummer, Fassung, Hash und Versandstatus werden wahrheitsgemäß dokumentiert; eine spätere Nummernänderung erfordert erneute Freigabe. Die führende Fassung wird mit Pfad und Hash im Mandatslauf eingetragen. Ohne Dateizugriff nennt der Übergabevermerk nur den vorgesehenen Pfad und weist den Hash als nicht ermittelbar aus. Offene Gates bleiben offen, bis die namentliche menschliche Freigabe der geprüften Fassung dokumentiert ist.

## 6. Beispiele

### 6.1. Ausformulierte Berechnung nach § 10 RVG mit Vorschussverrechnung

Sachverhalt: Außergerichtliche Vertretung gegenüber einem Lieferanten, Auftrag vom 1. September 2026, Gegenstandswert 8.000 Euro, 1.3 Geschäftsgebühr nach Nr. 2300 VV RVG, 60 Seiten Abschriften aus der Behördenakte auf Verlangen der Mandantin, Vorschuss von 300 Euro am 18. September 2026 eingegangen. Nach der zum Auftrag geltenden [Anlage 2 zum RVG](https://www.gesetze-im-internet.de/rvg/anlage_2.html) beträgt die 1.0 Gebühr bei 8.000 Euro 533,00 Euro. Die 60 Schwarz-Weiß-Seiten waren zur sachgemäßen Bearbeitung geboten (Nr. 7000 Nummer 1 Buchstabe a VV RVG); die Zahlungswiedervorlage Mittwoch, 21.10.2026, ist eingetragen.

> Rechnung Nr. 2026-0417 vom 7. Oktober 2026
>
> Sehr geehrte Frau Dr. Wendland, in der Angelegenheit Nordlicht Verpackungen GmbH gegen Fasswerk Hallbach wegen Mängelansprüchen aus dem Liefervertrag vom 14. August 2026 berechnen wir für die außergerichtliche Vertretung aufgrund des Auftrags vom 1. September 2026 die gesetzliche Vergütung wie folgt. Der Gegenstandswert beträgt 8.000 Euro. Die Geschäftsgebühr nach Nr. 2300 VV RVG setzen wir mit dem Satz von 1.3 an, weil Umfang und Schwierigkeit den Ansatz von 1.3 rechtfertigen und eine Überschreitung nicht begründen; sie beträgt 692,90 Euro. Für die auf Ihr Verlangen gefertigten 60 Seiten Abschriften aus der Behördenakte berechnen wir die Dokumentenpauschale nach Nr. 7000 VV RVG mit 26,50 Euro, nämlich 50 Seiten zu je 0,50 Euro und 10 Seiten zu je 0,15 Euro. Die Pauschale für Post- und Telekommunikationsdienstleistungen nach Nr. 7002 VV RVG beträgt 20 Prozent der Gebühren, höchstens jedoch 20,00 Euro, und wird mit 20,00 Euro angesetzt.
>
> Die Summe aus Gebühren und Auslagen beträgt 739,40 Euro. Hierauf entfällt Umsatzsteuer nach Nr. 7008 VV RVG in Höhe von 19 Prozent, also 140,49 Euro. Der Gesamtbetrag beläuft sich auf 879,89 Euro. Auf diese Angelegenheit haben Sie am 18. September 2026 einen Vorschuss von 300,00 Euro brutto gezahlt, bestehend aus 252,10 Euro netto und 47,90 Euro Umsatzsteuer, den wir in Abzug bringen. Es verbleibt ein Zahlbetrag von 579,89 Euro.
>
> Der Leistungszeitraum umfasst den 1. September 2026 bis zum 2. Oktober 2026. Bitte überweisen Sie den Zahlbetrag bis zum 21. Oktober 2026 unter Angabe der Rechnungsnummer auf das unten genannte Konto. Diese Rechnung ist eine Schlussrechnung für die außergerichtliche Vertretung; eine etwaige gerichtliche Vertretung wird gesondert beauftragt und abgerechnet.
>
> Mit freundlichen Grüßen
>
> Rechtsanwältin Dr. Frieda Blum

Vor Verwendung werden Steuernummer oder USt-IdNr., Anschriften, Bankverbindung und die Registernummer ergänzt; der Prüfvermerk hält fest, dass der 1.0-Wert aus dem Gebührenblatt mit Tabellenstand übernommen wurde.

### 6.2. Ausformuliertes Nachforderungsschreiben für fehlende B2G-Angaben

Die Rückmeldefrist Mittwoch, 14.10.2026, ist als Wiedervorlage eingetragen; Dr. Blum verantwortet den Brief.

> Sehr geehrte Frau Ostermann, die Rechnung für unsere Beratung der Stadt Lindenbrück zum Vergabeverfahren „Neubau Kita Ahornweg“ ist vorbereitet. Nach Ihrer Vorgabe übermitteln wir sie als XRechnung über das Rechnungsportal des Landes. Für die elektronische Zuordnung benötigen wir noch drei Angaben, die uns nicht vorliegen: die von Ihrer Stelle vergebene Leitweg-ID, die Bestell- oder Vorgangsnummer des Vergabereferats und die elektronische Adresse, unter der Ihre Stelle Rechnungen entgegennimmt. Als Leistungsempfängerin ist derzeit die Stadt Lindenbrück, vertreten durch den Bürgermeister, Rathausplatz 1, dokumentiert. Bitte teilen Sie uns mit, falls die Rechnung an einen Eigenbetrieb oder eine andere rechtlich verantwortliche Stelle auszustellen ist.
>
> Die Honorargrundlage bleibt die Vergütungsvereinbarung vom 1. September 2026 mit dem dort vereinbarten Festpreis für die Prüfung der Vergabeunterlagen. Die Rückfrage betrifft ausschließlich die Rechnungs- und Zuordnungsdaten; sie ändert weder Umfang noch Höhe der Vergütung. Nach Eingang der Angaben erstellen wir die XRechnung, prüfen sie mit dem aktuellen Validator und reichen sie über den von Ihnen benannten Weg ein. Wir bitten um Rückmeldung bis zum 14. Oktober 2026, damit die Rechnung noch im laufenden Haushaltsmonat verarbeitet werden kann.
>
> Mit freundlichen Grüßen
>
> Rechtsanwältin Dr. Frieda Blum

Das Schreiben bleibt Entwurf, solange sein Versand nicht beauftragt ist; eine in der Akte vorhandene aktuelle Leitweg-ID wird verwendet, nicht erneut abgefragt.

### 6.3. Negativbeispiel: PDF als E-Rechnung ausgegeben

Falsche Ausgabe: „Die E-Rechnung an die Nordlicht Verpackungen GmbH ist erstellt und validiert. Datei: Rechnung_2026-0417.pdf. Die Rechnung erfüllt die E-Rechnungspflicht ab 2025, weil sie elektronisch per E-Mail versandt wird.“

Warum sie falsch ist: Eine reine PDF-Datei ist eine sonstige Rechnung im Sinn von § 14 Absatz 1 UStG, weil sie kein strukturiertes elektronisches Format enthält, das die Extraktion der Pflichtangaben erlaubt. Der elektronische Versand macht sie nicht zur E-Rechnung. Eine Validierung mit dem KoSIT-Validator hat nicht stattgefunden und könnte bei einer PDF auch nicht stattfinden. Die Formatentscheidung fehlt: Ob für den Umsatz des Jahres 2026 die Übergangsregel nach § 27 Absatz 38 UStG mit Zustimmung der Empfängerin genutzt werden darf, wurde nicht geprüft. Die Aussage „E-Rechnungspflicht ab 2025“ verwechselt die Empfangspflicht mit der Ausstellungspflicht.

Korrigierte Fassung: „Für die Nordlicht Verpackungen GmbH als inländische Unternehmerin ist die XRechnung der Zielstandard. Für den Leistungszeitraum bis zum 2. Oktober 2026 wäre nach § 27 Absatz 38 UStG noch eine PDF-Rechnung zulässig, wenn die Empfängerin dem zustimmt; eine solche Zustimmung liegt nicht vor. Die Datei Rechnung_Entwurf_v1.xml wurde mit xrechnung.py aus den freigegebenen Eingaben erzeugt; `kosit_validated` ist falsch. Nächster Schritt ist die Validierung mit dem KoSIT-Validator in der Konfiguration XRechnung 3.0.2 und die Sichtkontrolle; die endgültige Nummer wird vor dem abschließenden Prüflauf eingesetzt, dessen unveränderte Fassung G4 bindet. Die PDF-Ansicht ist eine Sichtfassung und wird nur zusammen mit der XML-Datei übermittelt.“

### 6.4. Vorschuss schließt den einfachen XML-Weg aus

Die Kanzlei hat 1.190 Euro brutto als Vorschuss erhalten; die Schlussleistung beträgt 2.380 Euro brutto. Das Skript verarbeitet keine Vorschussverrechnung, und der Schlüssel `prepaid_amount` führt zum Abbruch. Deshalb wird keine reduzierte Position von 1.190 Euro erzeugt, die Leistungsumfang und Steuerausweis verfälschen würde. Der interne Vermerk lautet: „Die Hauptleistung beträgt nach geprüfter Grundlage 2.000 Euro netto zuzüglich 380 Euro Umsatzsteuer. Der Zahlungseingang vom 18. September 2026 ist als Vorschuss zugeordnet und wurde mit 1.000 Euro netto zuzüglich 190 Euro Umsatzsteuer versteuert. Die Schlussrechnung weist die Gesamtleistung, den verrechneten Vorschuss mit Datum und den Restzahlbetrag von 1.190 Euro aus und wird mit einem Rechnungswerkzeug erstellt, das diese Verrechnung unterstützt. Der lokale XML-Standardexport wird nicht verwendet.“

### 6.5. Korrektur des falschen Leistungsempfängers

Eine Rechnung wurde an die Rechtsschutzversicherung adressiert, obwohl der Mandant Empfänger der anwaltlichen Leistung ist. Der Vorgang wird nicht durch Umbenennen der PDF korrigiert. Prüfe die erteilte Rechnung, den Steuerausweis und den Versandstatus; erstelle die Berichtigung mit Bezug auf die Ursprungsrechnung. Der Text lautet: „Die Rechnung Nr. 2026-0402 vom 30. September 2026 wird hinsichtlich des Leistungsempfängers berichtigt. Empfänger der dort bezeichneten anwaltlichen Leistung ist Herr Jonas Reinholt, Birkenweg 12, 14542 Werder (Havel). Die Zahlung durch die Versicherung erfolgt im Rahmen der dort bestehenden Deckung; sie ist Zahlerin, nicht Leistungsempfängerin. Leistungszeitraum, Leistungsumfang und Vergütung bleiben unverändert. Diese Berichtigung ist zusammen mit der ursprünglichen Rechnung aufzubewahren.“ Ob diese Ergänzung genügt oder ein Storno mit Neuausstellung erforderlich ist, wird am Ausgangsdokument entschieden.

### 6.6. Prüfprotokoll für eine exportierte XML-Datei

Ein interner Vermerk lautet: „Die Datei Rechnung_Entwurf_v2.xml wurde am 7. Oktober 2026 aus den freigegebenen Eingabedaten erzeugt. Die Honorargrundlage ist die Vereinbarung HV-1; der Leistungsnachweis umfasst die bestätigten Einträge [IDs]. Der inländische Steuerfall ergibt 19 Prozent Umsatzsteuer; Vorschussverrechnung, Rabatte und Gutschriften sind nicht enthalten. Die Datei wurde mit KoSIT-Validator [Version] und Konfiguration [Fassung] geprüft; das Ergebnis lautet [Befund]. Rechnungsnummer, Empfänger, Leistungszeitraum, Positionen, Steuer und Zahlbetrag stimmen mit den freigegebenen Daten überein. Der Versandstatus lautet [Status].“ Die Platzhalter sind keine voreingestellten positiven Ergebnisse; ein Validierungsfehler wird mit Regelkennung und betroffener Stelle benannt und in den Daten behoben. Das Protokoll ist ein interner Nachweis und wird nicht als Rechnungsanlage versandt. Im agentischen Lauf auf Stufe 3 setzt der Skill anschließend die Phase `abrechnung`, trägt die XML-Datei als Produkt `rechnung-xml` im Zustand `geprueft` ein und öffnet G4 Rechnungsausgabe mit Dateiname und Hash als Bezug. Er stößt Mandantenkommunikation für das Anschreiben an und meldet: „Offenes Gate G4; Die endgültige Nummer 2026-0418 ist in der geprüften Fassung enthalten; Zeitstand 460 bestätigte Minuten, keine offene Zeitfrage.“ Erst nachdem Rechtsanwältin Dr. Blum G4 namentlich freigegeben hat, werden tatsächliche Mitteilung und belegte Fälligkeit dokumentiert; die freigegebene Nummer und Fassung bleiben unverändert und die Rechnung an Zahlungen und Buchhaltung übergeben.
