---
name: abrechnung-e-rechnung
description: Erstellt und prüft anwaltliche Rechnungen und begrenzte XRechnungsentwürfe aus bestätigten Honorargrundlagen; trennt Forderungsprüfung, Umsatzsteuer, Pflichtformat, Validierung, Freigabe und Versand.
---

# Anwaltliche Rechnung und E-Rechnung erstellen

## 1. Zweck und Anwendungsfall

### 1.1. Von der dokumentierten Leistung zur konkreten Rechnung

Dieser Skill führt einen bestätigten Leistungs- und Honorarstand zu einer überprüfbaren Rechnung. Er verbindet anwaltliches Vergütungsrecht, Umsatzsteuer, Empfängeranforderungen und tatsächliche technische Ausgabe. Das Ergebnis ist je nach Auftrag ein fertiger Rechnungsentwurf, eine geprüfte strukturierte XML-Datei oder eine konkrete Korrekturrechnung. Ein bekannter Teilbetrag aus dem Mandatsjournal wird nicht als vollständige Forderung ausgegeben, solange wesentliche Positionen, Zuordnungen oder Grundlagen offen sind.

Rechtliche Abrechenbarkeit, rechnerische Richtigkeit und technische Konformität sind getrennte Prüfungen. Eine XML-Datei kann technisch gültig sein und dennoch einen falschen Leistungsempfänger, ein nicht vereinbartes Honorar oder eine unzutreffende Umsatzsteuer enthalten. Umgekehrt kann ein berechtigter Honoraranspruch mit einem unzureichenden Rechnungsformat geltend gemacht werden. Der Skill dokumentiert deshalb, was geprüft wurde und welche Frage noch offen ist. Er behauptet keine umfassende Freigabe allein aus einem erfolgreichen Export.

### 1.2. Die Rechnung ist kein bloßer Dateityp

Eine PDF-Datei ist grundsätzlich eine sonstige elektronische Rechnung, keine strukturierte E-Rechnung im Sinn des aktuellen Umsatzsteuerrechts. Eine E-Rechnung enthält verarbeitbare strukturierte Daten in einem geeigneten Format. Die zusätzliche lesbare Ansicht erleichtert die Kontrolle, ersetzt jedoch die Originaldaten nicht. Bei hybriden Formaten müssen strukturierter Inhalt und visuelle Darstellung miteinander abgeglichen werden; eine ansprechend gestaltete Sichtfassung heilt keine falschen XML-Daten.

Die KI-native Kanzlei darf die Erstellung vorbereiten und zulässige Werkzeuge ausführen. Die Vergabe einer endgültigen Rechnungsnummer, die anwaltliche Verantwortungsübernahme, die tatsächliche Mitteilung, die Buchung und der Versand werden als eigenständige Schritte dokumentiert. Eine ausdrücklich beauftragte interne Erstellung wird bis zum reviewbaren Ergebnis ausgeführt. Ein Versand erfolgt nur im Rahmen eines entsprechenden Auftrags. Weder der Dateiname „final“ noch ein internes Freigabefeld beweist einen tatsächlichen Zugang beim Empfänger.

## 2. Eingaben

### 2.1. Führender Honorar- und Leistungsstand

Lies die gültige Vergütungsvereinbarung, Nachträge, Gebührenberechnung, bestätigten Zeitbelege, Auslagenbelege, bisherigen Rechnungen, Vorschüsse und Zahlungseingänge. Halte die aktuelle Basis knapp vor: „Für die außergerichtliche Prüfung gilt die Vereinbarung vom [Datum] mit 280 Euro netto pro tatsächlicher Stunde und einem Gesamtdeckel von 2.500 Euro netto. Bestätigt sind bislang sieben Stunden und 40 Euro eigene steuerpflichtige Auslagen.“ Wenn bereits feststeht, dass der Deckel Auslagen einschließt, wird dies nicht erneut gefragt.

Fehlt eine entscheidende Angabe, frage gezielt nach Modell, Umfang, Netto- oder Bruttobezug, Satz, Festpreis, Fee Quote, Schätzung oder Deckel. Eine Rechnung darf eine unklare Preiszusage nicht einseitig in ein offenes Stundenhonorar umdeuten. Nach neu erbrachten Leistungen werden tatsächliche Dauer, Datum, Person, Abrechenbarkeit und Narrativ erfragt, soweit noch offen. Die Rechnungsprüfung darf bekannte Daten verwenden, während eine weitere Zeitfrage noch aussteht; der Vollständigkeitsstatus bleibt dann erkennbar.

### 2.2. Parteien und Zustellungsdaten

Erfasse Rechnungsaussteller, tatsächlichen umsatzsteuerlichen Leistungsempfänger, Auftraggeber, Rechnungsempfänger, Zahlenden und etwaige Rechnungsprüfer getrennt. Eine Rechtsschutzversicherung wird nicht allein wegen ihrer Zahlung zum Leistungsempfänger. Eine Konzernmutter, die Rechnungen zentral bearbeitet, ist nicht zwangsläufig Vertragspartnerin. Prüfe die genaue Firma, Anschrift und erforderliche Steuerkennung aus verlässlichen Stammdaten. Ein Zahlendreher in einer Postanschrift ist anders zu behandeln als die Abrechnung gegenüber der falschen juristischen Person.

Benötigt werden Rechnungsnummer, Ausstellungsdatum, Leistungszeitraum, Währung, Zahlungsbedingungen, Steuerbehandlung, Empfängerreferenzen und der vereinbarte oder vorgeschriebene Übermittlungsweg. Bei öffentlichen Auftraggebern werden Leitweg-ID, Bestellnummer, elektronische Adresse und Portalvorgaben anhand tatsächlicher Angaben geprüft. Fehlende Referenzen werden nicht erfunden, um eine technische Validierung zu bestehen. Eine generische E-Mail-Adresse ersetzt keine vorgeschriebene Empfängerkennung.

### 2.3. Steuer- und Formatangaben

Kläre Inland oder Ausland, Unternehmereigenschaft, Leistungsbezug für das Unternehmen, Steuerbefreiung, Kleinunternehmerstatus, Reverse Charge und etwaige Besonderheiten des Leistungsorts. Die Unterstützung durch das lokale Skript ist enger als das Umsatzsteuerrecht: Es verarbeitet ausschließlich EUR, inländische Parteien, positive Positionen und 19 Prozent Umsatzsteuer ohne Vorschussverrechnung, Rabatte, Gutschriften oder Sonderbesteuerung. Ein außerhalb liegender Fall benötigt einen geeigneten Fachablauf und darf nicht durch falsche Stammdaten passend gemacht werden.

Für die Formatentscheidung werden Leistungsdatum und einschlägige Übergangsregel geprüft. Die Empfangspflicht und der zeitweise noch zulässige Verzicht auf Ausstellung einer strukturierten Rechnung sind nicht identisch. Eine Kanzlei kann im Übergangszeitraum weiterhin eine zulässige sonstige Rechnung ausstellen müssen oder dürfen und gleichzeitig bereits E-Rechnungen empfangen können müssen. B2C, B2B und B2G werden getrennt beurteilt.

## 3. Ablauf / Checkliste

### 3.1. Forderung zuerst auf ihre Grundlage prüfen

Ermittle, welche Vergütung entstanden und fällig ist. Bei RVG werden die einschlägigen Gebühren, Auslagen, Werte, Anrechnungen und das Übergangsrecht anhand eines gesonderten Gebührenblatts geprüft. Bei Zeithonorar werden wirksame Grundlage, passende Tätigkeit, tatsächliche Dauer, gültiger Satz und Deckel kontrolliert. Bei Festpreis werden vereinbarter Leistungsumfang, Leistungsstand und Fälligkeitsregel betrachtet. Der im Journal ausgewiesene volle Festpreis ist ein Vereinbarungswert, keine automatische Aussage, dass er bereits vollständig verlangt werden darf.

Ein Vorschuss nach § 9 RVG unterscheidet sich von einer Schlussrechnung. Die Erstattungsfähigkeit gegenüber Gegner oder Staatskasse unterscheidet sich vom Anspruch gegen den Mandanten. Ein rechtsschutzversicherter Mandant schuldet nicht automatisch nur den gedeckten Betrag; ebenso wenig darf eine Deckungszusage als Zustimmung zu jedem Honorar verstanden werden. Prüfe bei Beiordnung oder Beratungshilfe die besonderen Grenzen. Eine Rechnung wird nicht durch einen pauschalen Hinweis „gemäß Vereinbarung“ von dieser Prüfung befreit.

### 3.2. Anwaltliche Berechnung nach § 10 RVG

Nach dem aktuellen § 10 Absatz 1 RVG bedarf die Berechnung der Textform und muss durch den Rechtsanwalt oder auf seine Veranlassung mitgeteilt werden. Eine allgemeine Forderung nach eigenhändiger Unterschrift wäre zum dokumentierten Rechtsstand überholt. Die tatsächliche Veranlassung und Mitteilung werden gleichwohl nicht fingiert. Ein intern fortgeschriebener Entwurf ist noch keine mitgeteilte Berechnung. Der Lauf der Verjährung hängt nicht erst von dieser Mitteilung ab; eine lange liegengebliebene Rechnung wird deshalb nicht automatisch rechtzeitig.

Für gesetzliche Gebühren enthält die Berechnung die einzelnen Gebühren- und Auslagenbeträge, Vorschüsse, kurze Bezeichnung der Gebührentatbestände, die angewandten Nummern des Vergütungsverzeichnisses und bei Wertgebühren den Gegenstandswert. Bei Zeithonorar muss die konkrete Leistungsdarstellung eine Prüfung ermöglichen. Ein einheitlicher Text „Beratung im Oktober“ kann für einen komplexen streitigen Stundenanspruch unzureichend sein. Stelle die Zeitaufstellung in geeigneter Weise bereit, ohne unnötig vertrauliche Einzelheiten an unberechtigte Dritte zu verteilen.

Die vom Mandanten erbetene Rechnungserläuterung ist kein neuer Gebührenanspruch allein deshalb, weil ihre Erstellung Zeit benötigt. Prüfe, ob eine zusätzliche Tätigkeit tatsächlich über die notwendige Abrechnung und Erläuterung hinausgeht und gesondert beauftragt wurde. Kosten einer Korrektur eigener Rechnungsfehler werden nicht ohne Grundlage weiterberechnet. Interne Bearbeitungszeit kann dokumentiert werden, bleibt aber von der Frage ihrer Abrechenbarkeit getrennt.

### 3.3. Rechenweg und Deckelabgleich

Berechne jede Position aus der zutreffenden Grundlage. Bei Stundenhonorar werden tatsächliche Minuten in Stunden umgerechnet und mit dem gültigen Satz bewertet. Festpreise werden nicht zusätzlich um sämtliche Zeitwerte erhöht. Bei einem Deckel wird geprüft, ob er Gebühren allein oder Gebühren und Auslagen umfasst. Ein verbrauchter Gesamtdeckel darf nicht durch eine neue Rechnungsnummer, einen neuen Monat oder eine neue technische Phase zurückgesetzt werden.

Beispiel: Bestätigte Zeitwerte betragen 2.420 Euro netto und eigene steuerpflichtige Auslagen 160 Euro netto. Bei einem gemeinsamen Deckel von 2.500 Euro netto darf der Entwurf nicht einfach 2.580 Euro ansetzen. Bei einem nur auf Honorar bezogenen Deckel kann die Behandlung anders ausfallen, wenn die Auslagenerstattung wirksam vereinbart ist. Die Rechnung soll diese Unterscheidung verständlich abbilden. Dokumentiere den tatsächlichen Aufwand und den begrenzten Ansatz getrennt.

Kontrolliere Geldrundung, Steuerbasis und Gesamtsumme. Die Summe einzeln gerundeter Positionen kann von einer erst am Ende gerundeten Gesamtzeit abweichen. Verwende einen konsistenten Rechenweg und gleiche XML, lesbare Ansicht und Buchungsvorschlag ab. Ein Rundungsrest wird nicht durch frei erfundene Leistungspositionen ausgeglichen. Bei ungewöhnlichen Differenzen wird die Ursache geklärt, bevor die Rechnung freigegeben wird.

### 3.4. Umsatzsteuer und Pflichtangaben

Prüfe § 14 Absatz 4 UStG sowie gegebenenfalls besondere Angaben nach § 14a UStG und die einschlägigen Ausnahmen. Die Rechnung muss den tatsächlichen Sachverhalt abbilden. Leistungsbeschreibung und Leistungszeitpunkt werden nicht durch das Ausstellungsdatum ersetzt. Bei einer mehrmonatigen Beratung ist der Leistungszeitraum sachgerecht zu bestimmen; eine unzutreffende Standardperiode wird nicht aus einer früheren Rechnung übernommen.

Eigene Auslagen der Kanzlei können Teil der steuerpflichtigen Leistung sein. Echte durchlaufende Posten setzen eine andere rechtliche und tatsächliche Einordnung voraus. Ein Gerichtskostenvorschuss wird nicht allein wegen des Wortes „Auslage“ mit 19 Prozent beaufschlagt. Ebenso darf eine eigene steuerpflichtige Fremdleistung nicht automatisch als steuerfreier durchlaufender Posten behandelt werden. Rechnungsbeleg, Schuldner der Fremdforderung und Handeln im eigenen oder fremden Namen sind maßgeblich.

Unrichtiger oder unberechtigter Steuerausweis kann eigenständige Folgen auslösen. Bei einer Korrektur werden deshalb nicht nur Endsumme und Zahlbetrag geändert, sondern auch der ursprüngliche Steuerausweis, die Berichtigung und deren Mitteilung betrachtet. Die bloße Bezeichnung „Entwurf“ schützt nicht vor jedem Risiko, wenn ein Dokument tatsächlich wie eine Rechnung verwendet wird. Testdateien werden deshalb mit fiktiven Daten getrennt gehalten und nicht in den produktiven Versand übernommen.

### 3.5. Entscheidungsbaum für das erforderliche Rechnungsformat

Prüfe zuerst, ob der Umsatz in den Anwendungsbereich der inländischen B2B-Regel fällt. Ist der Leistungsempfänger Verbraucher, wird die B2B-Pflicht nicht allein deshalb ausgelöst, weil die Kanzlei Unternehmerin ist. Ist der Empfänger eine öffentliche Stelle, werden zusätzlich Bundes- oder Landesvorgaben und der konkrete Empfangsweg geprüft. Bei Auslandsbezug ist die inländische B2B-Route nicht schematisch anzuwenden. Eine besondere Vertragsvereinbarung zum Format kann neben den gesetzlichen Vorgaben relevant bleiben.

Prüfe danach Ausnahmen, insbesondere Kleinbetragsrechnungen bis einschließlich 250 Euro brutto und die Regelung für Kleinunternehmer. Prüfe anschließend die Übergangsbestimmungen in § 27 Absatz 38 UStG. Für die dort erfassten Umsätze bis Ende 2026 können noch sonstige Rechnungen zulässig sein; bei elektronischen sonstigen Formaten ist die maßgebliche Zustimmung zu beachten. Für 2027 ist unter anderem der Vorjahresgesamtumsatz des Ausstellers von nicht mehr als 800.000 Euro relevant. Daneben besteht die begrenzte EDI-Übergangsregel. Ab 2028 entfallen diese Übergänge, nicht jede gesetzliche Ausnahme.

Das Ergebnis wird in einem Satz mit Tatsachengrundlage festgehalten: „Für diesen inländischen unternehmerischen Leistungsempfänger ist eine strukturierte Rechnung der maßgebliche Zielstandard; die für 2026 noch einschlägige Übergangsmöglichkeit wird nicht benötigt, weil der Empfänger XRechnung 3.0 akzeptiert.“ Eine andere Fallkonstellation erhält eine andere Begründung. Ein allgemeiner Satz „Seit 2025 muss jede Rechnung XML sein“ ist unzutreffend und wird nicht verwendet.

### 3.6. Empfängeranforderungen und Datenminimierung

Kontrolliere, welche Daten der Empfänger für die Zuordnung benötigt und welche rechtlich erforderlichen Daten die Rechnung enthalten muss. Eine Einkaufsabteilung kann interne Bestellnummern verlangen, ohne deshalb sämtliche vertraulichen Beratungsinhalte erhalten zu dürfen. Stimme eine aussagekräftige, begrenzte Leistungsbeschreibung ab. Bei mehreren Mandaten auf einer Sammelrechnung ist zusätzlich zu prüfen, ob der Empfängerkreis für alle enthaltenen Informationen berechtigt ist.

Eine Leitweg-ID wird aus dem Auftrag oder einer authentisch bestätigten Mitteilung übernommen. Ihre formale Plausibilität beweist nicht, dass sie der richtigen Behörde zugeordnet ist. Dasselbe gilt für elektronische Adressen und Bankdaten. Ändert sich die Bankverbindung kurz vor Rechnungsstellung, wird der Vorgang nach dem bestehenden Kanzleiverfahren unabhängig geprüft. Ein Manipulationsversuch in einer E-Mail darf nicht als neue verbindliche Stammdatenquelle behandelt werden.

Bei einem vom Mandanten beauftragten externen Rechnungsprüfer sind Rolle, Auftrag, Vertraulichkeit und erforderlicher Datenumfang zu klären. Der Skill erzeugt bei Bedarf eine geeignete Leistungsaufstellung, keine pauschale Freigabe der vollständigen Akte. Schwärzungen müssen die für den Honoraranspruch erforderliche Nachvollziehbarkeit erhalten. Ein gesonderter Detailnachweis kann gezielt bereitgestellt werden, wenn die rechtlichen Voraussetzungen vorliegen.

### 3.7. Den Journalentwurf fachlich freigeben

Lies `rechnungsentwurf.json` mit Journalrevision, Phasen, offenen Positionen und Zahlungen. Prüfe, ob alle für die konkrete Rechnung erforderlichen Einträge bestätigt sind und ob der zeitliche Abrechnungsausschnitt stimmt. Das Feld `complete` bedeutet nur, dass die vom Werkzeug erkannten Erfassungsfragen geschlossen sind. `invoice_ready` bleibt bewusst falsch. Ein fachlicher Freigabevermerk muss tatsächlich erstellt werden und kann sich nicht auf eine vermeintliche automatische juristische Prüfung berufen.

Zahlungen werden vom Journal gesondert gezeigt und nicht automatisch verrechnet. Prüfe deshalb Vorschuss, Teilzahlung, Drittzahlung und Fremdgeld außerhalb der einfachen Summenansicht. Ein bereits gezahlter Betrag kann die Zahlungsforderung mindern, ohne die ursprüngliche steuerliche Leistungsbemessung in gleicher Weise zu verändern. Eine richtige Schlussrechnung benötigt eine passende Verrechnungsdarstellung. Das lokale XML-Skript unterstützt diesen Sonderfall nicht.

RVG-Beträge werden über `manual-fee` nur mit geprüftem Gebührenblatt übernommen. `legal_reviewed=true` ist eine Bestätigung tatsächlicher Prüfung, kein Rechenbefehl. Ungeklärte Gebührenwerte und offene Anrechnung werden nicht durch einen willkürlichen Pauschalbetrag verdeckt. Sobald die fachliche Grundlage vollständig ist, kann der konkrete Rechnungsentwurf mit den erforderlichen Angaben erstellt werden.

### 3.8. XRechnung mit dem vorhandenen Skript erzeugen

Die tatsächliche Schnittstelle ist in [Mandatsordner und CLI](../../references/mandatsordner-und-cli.md) und `assets/xrechnung-beispiel.json` beschrieben. Das Skript `scripts/xrechnung.py` erwartet eine vollständige Eingabedatei mit `schema_version=1`, Dokumentstatus, Währung, Umsatzsteuersatz, Rechnungsnummer, Käuferreferenz, Datumsfeldern, Lieferanten- und Kundendaten sowie positiven Rechnungspositionen. Es erzeugt UBL im begrenzten XRechnungsprofil. Es liest nicht automatisch eine unvollständige Mandatsakte und entscheidet nicht selbst über richtige Gebühren.

Der Aufruf lautet `python3 "<Pluginordner>/scripts/xrechnung.py" --input "<Rechnungsdaten.json>" --output "<Mandatsordner>/02_Honorar/Rechnung_Entwurf_v1.xml"`. Eine vorhandene Ausgabedatei wird nicht überschrieben. Bei einer Korrektur wird eine neue Fassung erzeugt und mit dem vorherigen Stand verknüpft. `document_state=draft` setzt einen Entwurfshinweis. `approved` setzt zusätzlich `legal_reviewed=true` voraus, ersetzt aber weder eine echte Freigabe noch den Auftrag zum Versand.

Die unterstützten Einheiten sind `C62`, `HUR`, `MIN` und `DAY`. Mengen müssen positiv sein; Einzelpreise und Mengen dürfen nur die unterstützte Genauigkeit verwenden. Das Skript prüft bestimmte Datumsfolgen, doppelte Positions-IDs und formale deutsche Steuer- beziehungsweise Bankdaten. Eine formal gültige IBAN ist kein Nachweis eines tatsächlich existierenden oder berechtigten Kontos. Die im Beispiel enthaltenen Testdaten dürfen nicht für eine reale Rechnung verwendet werden.

### 3.9. Technische Validierung und Sichtkontrolle

Zum dokumentierten Prüfstand 7. Oktober 2026 ist die normative XRechnung-Version 3.0 maßgeblich; das aktuelle Bundle ist 3.0.2 Summer 2026 Bugfix vom 31. August 2026. Die im September veröffentlichte Spezifikation 4.0 ist eine Vorversion. Prüfe unmittelbar vor einem produktiven Export den aktuellen Stand und das vom Empfänger akzeptierte Profil. Eine feste Versionsangabe im Skill ersetzt diese Kontrolle nicht.

Validiere jede konkrete exportierte Datei mit dem aktuellen offiziellen KoSIT-Validator und der passenden XRechnung-Konfiguration. Dokumentiere Version, Konfiguration, Datei und Ergebnis. Eine erfolgreiche XSD-Prüfung allein genügt nicht; Geschäftsregeln und gegebenenfalls Empfängerregeln müssen berücksichtigt werden. Ein früher bestandener Beispieltest validiert keine spätere Rechnung. Warnungen werden inhaltlich bewertet, nicht automatisch als bedeutungslos ignoriert.

Vergleiche anschließend eine lesbare Visualisierung mit den freigegebenen Eingaben. Prüfe Namen, Rechnungsnummer, Zeitraum, Positionsbeschreibung, Mengen, Nettobeträge, Steuer und Zahlbetrag. Achte auf abgeschnittene Texte und missverständliche Einheiten. Bei Abweichungen wird die Ursache in den strukturierten Daten korrigiert und erneut validiert. Ein manuell verschönertes PDF bei unverändert falschem XML ist keine Lösung.

### 3.10. Rechnungsnummer, Korrektur und Archiv

Die Rechnungsnummer wird anhand des kanzleiweit geführten Registers vergeben. Das Skript erzeugt und prüft dieses Register nicht. Entwurfsnummern werden nicht unkontrolliert in die produktive Nummernfolge übernommen. Die gewählte Organisation muss eindeutige Identifikation und Nachvollziehbarkeit sicherstellen. Bei mehreren Standorten oder Rechnungsserien wird die tatsächliche Zuordnung dokumentiert, statt bloß aus einem Dateinamen auf Eindeutigkeit zu schließen.

Bei Fehlern in einer bereits ausgestellten Rechnung prüfe, ob Ergänzung, Berichtigung oder Storno mit neuer Rechnung erforderlich ist. Erhalte den ursprünglichen Datensatz, die Korrektur und den Bezug zwischen beiden. Verwende das Wort „Gutschrift“ nicht unbedacht, weil es im Umsatzsteuerrecht auch eine durch den Leistungsempfänger ausgestellte Rechnung bezeichnet. Eine kaufmännische Erstattung und eine umsatzsteuerliche Gutschrift sind nicht automatisch dasselbe.

Archiviere strukturierte Originaldaten, erforderliche Sichtfassung, Validierungsbericht, Freigabe und tatsächlichen Übermittlungsnachweis in nachvollziehbarer Zuordnung. Die GoBD verlangen einen geeigneten Prüfpfad; das Ausdrucken und Löschen der XML-Datei genügt nicht. Aufbewahrung und Löschung werden nach Dokumentart und geltendem Recht bestimmt. Ein pauschaler Zeitraum für sämtliche Mandatsunterlagen und Buchungsbelege wird nicht behauptet.

### 3.11. Tatsächliche Mitteilung und Zahlungsüberwachung

Vor einem beauftragten Versand werden Empfänger, Kanal, Rechnungsfassung und Anlagen kontrolliert. Der Versandstatus wird erst nach tatsächlicher Durchführung gesetzt. Eine Portalannahme kann eine technische Bestätigung sein, ohne dass damit sämtliche materiellen Einwendungen ausgeschlossen wären. Ein Fehlerbericht wird gelesen und die Rechnung gezielt nachgebessert. Der Skill erklärt nicht automatisch eine Rechnung für zugegangen, nur weil eine lokale Datei existiert.

Anschließend wird die Rechnung dem Zahlungsworkflow übergeben. Fälligkeit und Verzug werden aus Gesetz, Vertrag, Zugang und gegebenenfalls Mahnung bestimmt. Ein frei gewähltes Zahlungsdatum im XML begründet nicht rückwirkend eine fehlende Vereinbarung. Die 30-Tage-Regel des § 286 Absatz 3 BGB erfordert eine gesonderte Prüfung, insbesondere bei Verbrauchern. Verzugszinsen, Pauschalen und Mahnkosten werden nicht ohne Sachverhalts- und Normprüfung aufgeschlagen.

### 3.12. Gegenprüfung vor Abschluss

Die letzte Kontrolle folgt dem Weg des Geldes rückwärts: Stimmt der geforderte Zahlbetrag mit Leistung, Vereinbarung, Deckel, Steuer und bereits zugeordneten Zahlungen überein? Kann jede Position aus einem Beleg nachvollzogen werden? Sind offene Angaben kenntlich gemacht? Wurde die richtige Person als Leistungsempfänger gewählt? Sind Rechtsgrundlage, technische Validierung und tatsächliche Mitteilung jeweils getrennt dokumentiert?

Prüfe außerdem, ob der Rechnungstext unbeabsichtigt ein Anerkenntnis, einen Verzicht oder eine abschließende Erledigung enthält. Die Bezeichnung „Schlussrechnung“ kann Erwartungen über den Abrechnungsstand erzeugen und sollte dem tatsächlichen Stand entsprechen. Eine weitere noch offene Phase wird klar bezeichnet. Der Nutzer erhält das konkrete Ergebnis und die wenigen materiell verbleibenden Punkte; eine allgemeine lange Warnliste ersetzt diese Abschlussprüfung nicht.

### 3.13. Berichtigung und Vorsteuer zeitlich präzise behandeln

Eine Rechnungskorrektur kann unterschiedliche Fehler betreffen: fehlende Steuernummer, ungenaue Leistungsbeschreibung, falschen Zeitraum, falschen Empfänger oder fehlenden Steuerausweis. Diese Fehler haben nicht notwendig dieselbe Rechtsfolge. Prüfe, ob das ursprüngliche Dokument bereits die erforderlichen Mindestangaben einer berichtigungsfähigen Rechnung enthält und ob die materiellen Voraussetzungen der Leistung vorliegen. Eine spätere Ergänzung wird nicht pauschal als rückwirkend behandelt. Ebenso wird nicht pauschal behauptet, jede Korrektur wirke ausschließlich für die Zukunft.

Der aktuelle Beschluss des BFH vom 26. Februar 2026 lässt gerade eine Frage zur zeitlichen Ausübung des Vorsteuerabzugs bei einem zunächst nicht berichtigungsfähigen Dokument zur Revision zu. Diese prozessuale Entscheidung ist ein Anlass zur Aktualitätskontrolle, keine abschließende Antwort. Ermittle vor einer konkreten steuerlichen Empfehlung den Stand des zugelassenen Verfahrens und einschlägiger unionsrechtlicher Entscheidungen. Wenn die Frage noch offen ist, benennt der Vermerk die konkrete Unsicherheit und den benötigten steuerlichen Entscheidungsschritt. Eine technische Rechnungsberichtigung darf trotzdem sachgerecht vorbereitet werden.

Die Dokumentenkette bleibt erhalten. Der neue Datensatz verweist auf die ursprüngliche Rechnung und beschreibt die geänderte Angabe. Der frühere Originaldatensatz wird nicht gelöscht oder stillschweigend überschrieben. Bei einem bereits gebuchten Vorgang sind Rechnungsberichtigung, Steuerkorrektur und Finanzbuchung aufeinander abzustimmen. Der Skill erzeugt dafür ein konkretes Übergabepaket mit den betroffenen Belegen, statt lediglich eine neue PDF unter dem alten Namen abzulegen.

### 3.14. Teilrechnung und mehrere Angelegenheiten

Eine Teilrechnung verlangt einen eindeutig abgegrenzten Leistungs- oder Abrechnungsabschnitt. Prüfe, ob die Vereinbarung Zwischenabrechnungen vorsieht und ob die gesetzlichen Fälligkeitsregeln passen. Eine Teilrechnung darf nicht den Eindruck erwecken, der gesamte Auftrag sei abgeschlossen, wenn weitere Leistungen offen sind. Ein Vorschuss ist davon zu unterscheiden. Die Rechnung bezeichnet deshalb ihren sachlichen und zeitlichen Umfang und die verbleibende Phase, soweit dies für die Klarheit erforderlich ist.

Bei mehreren RVG-Angelegenheiten wird nicht automatisch ein einheitlicher Wert oder ein einziger Gebührensatz verwendet. Prüfe je Angelegenheit Entstehung, Anrechnung und Übergangsrecht. Eine Sammelrechnung kann die Ergebnisse zusammenführen, muss die einzelnen Grundlagen aber nachvollziehbar darstellen. Bei verschiedenen Honorarvereinbarungen wird die entsprechende Bezugnahme je Position erhalten. Ein gemeinsamer Zahlungsempfänger oder ein gemeinsamer Mandantenname macht getrennte Leistungsgrundlagen nicht zu einem einheitlichen Preisversprechen.

Eine periodenbezogene Stundenrechnung braucht außerdem einen Abgleich mit bereits abgerechneten Zeiten. Die gleichen Minuten dürfen nicht erneut angesetzt werden, nur weil eine neue Exportdatei erzeugt wurde. Das einfache Mandatsjournal führt einen laufenden Entwurf und ist kein vollständiges Abrechnungsregister. Ein gesonderter Abrechnungsnachweis muss deshalb festhalten, welche Eintrags-IDs welcher tatsächlichen Rechnung zugeordnet wurden. Fehlende produktive Funktionen werden nicht als vorhanden beschrieben.

### 3.15. Eingangsrechnungen der Kanzlei prüfen

Wird statt einer Ausgangsrechnung eine Lieferantenrechnung geprüft, beginnt der Ablauf beim tatsächlichen Leistungsbezug. Vergleiche Bestellung, Vertrag, gelieferte Leistung und Rechnung. Eine formal gültige XRechnung beweist weder, dass die bestellte Leistung vollständig erbracht wurde, noch dass der Preis stimmt. Prüfe mögliche Doppelrechnungen, bereits erfolgte Zahlungen, falsche Kontoverbindungen und unberechtigte Nebenentgelte. Eine neue Bankverbindung wird nach dem vorhandenen sicheren Kanzleiverfahren bestätigt.

Die Vorsteuerfrage wird vom Zahlungsfreigabeprozess getrennt. Eine wirtschaftlich fällige Forderung kann einen Rechnungsmangel aufweisen; ein formal einwandfreies Dokument kann eine nicht geschuldete Leistung betreffen. Der interne Vermerk benennt beides. Für die Buchhaltung werden Original-XML, erforderliche Anlagen und konkrete Prüfhinweise übergeben. Ein PDF-Ausdruck ist keine vollständige Archivierung einer strukturierten Rechnung. Vertrauliche Lieferanten- und Mandatsdaten bleiben auf die erforderlichen Empfänger beschränkt.

Ein geeigneter Rückfragetext lautet: „Ihre Rechnung [Nummer] vom [Datum] bezeichnet als Leistungszeitraum lediglich den Ausstellungsmonat. Nach unserem Auftrag betrifft die Rechnung jedoch die Leistungen vom [Beginn] bis [Ende]. Bitte prüfen Sie den Zeitraum und übersenden Sie eine gegebenenfalls erforderliche Berichtigung mit eindeutigem Bezug auf die ursprüngliche Rechnung. Die übrigen Angaben werden gesondert mit dem vereinbarten Leistungsumfang abgeglichen.“ Der Text wird nur mit tatsächlich belegten Daten verwendet und ist ohne Versandauftrag ein fertiger Entwurf.

## 4. Quellenpflicht

### 4.1. Normen und amtliche technische Quellen

Beachte [Zitierweise](../../references/zitierweise.md). Prüfe §§ 8 bis 10, 15 und 60 RVG, §§ 14, 14a, 14c, 15 und 27 Absatz 38 UStG sowie §§ 31, 33 und 34a UStDV nach dem tatsächlichen Fall. Für die elektronische Rechnung werden die aktuelle [BMF-Information](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) und die [KoSIT-Versionsseite](https://xeinkauf.de/xrechnung/versionen-und-bundles/) herangezogen. Verwaltungsauffassung, Gesetz, Gerichtsentscheidung und eigene technische Umsetzung bleiben unterscheidbar.

### 4.2. Verifizierte Entscheidungsanker

BFH, Urteil vom 20.10.2016 – V R 26/15, Rn. 19–23, behandelt rückwirkende Berichtigung einer Rechnung mit bestimmten Mindestangaben. Das ersetzt keine Prüfung materieller Voraussetzungen und ist kein Freibrief für fehlende Empfänger oder Leistungen. [Amtlicher Volltext](https://www.bundesfinanzhof.de/en/entscheidungen/entscheidungen-online/decision-detail/STRE201610285/).

BFH, Beschluss vom 26.02.2026 – V B 11/25, Rn. 2, lässt eine Revision zur zeitlichen Ausübung des Vorsteuerabzugs bei ursprünglich nicht berichtigungsfähigem Dokument zu. Der Beschluss entscheidet diese Rechtsfrage noch nicht. Das amtliche Register führt die Revision zum Prüfstand als V R 7/26; ein späterer Entscheidungsstand ist vor konkreter Beratung zu suchen. [Amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/).

BGH, Urteil vom 12.09.2024 – IX ZR 65/23, Rn. 16 und 34–37, bleibt für nachprüfbare anwaltliche Zeitabrechnung relevant. Technische Rechnungsstandards ersetzen diese Darlegung nicht. [Amtliches Curia-Archiv](https://curia.europa.eu/site/upload/docs/application/pdf/2025-04/ix_zr__65-23_2025-04-16_15-06-53_148.pdf).

BGH, Urteil vom 19.02.2026 – IX ZR 226/22, Rn. 29–34, verhindert die Behandlung ausbleibender Beanstandung als tragfähige formularmäßige Anerkennung. Die Prüfung des übrigen Honoraranspruchs bleibt erforderlich. [Amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2022/IX_ZR_226-22.pdf?__blob=publicationFile&v=1).

## 5. Ausgabeformat

### 5.1. Rechnung, Nachweise und Status

Liefere eine vollständige Rechnung beziehungsweise einen klar bezeichneten Entwurf, die erforderliche Leistungsaufstellung und einen getrennten internen Prüfvermerk. Bei XML-Erstellung kommen die tatsächliche Datei und der konkrete Validierungsstatus hinzu. Nenne einen fehlenden Pflichtwert genau. Behaupte keine erfolgreiche Validierung, wenn lediglich ein Export erfolgt ist, und keinen Versand, wenn nur Dateien erstellt wurden. Eine ungelöste wesentliche Steuerfrage wird nicht durch einen allgemeinen Haftungsausschluss verdeckt.

Das Endprodukt wird in vollständigen, ausformulierten Sätzen geliefert. Skelette, Halbsätze und reine Aufzählungsgerüste sind als juristisches Endprodukt verboten. Tabellen dürfen Rechnungspositionen sachgerecht darstellen. Lesbare formatierte Dokumente verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung; strukturierte XML-Felder folgen dem technischen Standard. Technische Prüfhinweise stehen außerhalb des versandfähigen Rechnungstextes. Bei reiner Textausgabe wird ein erforderlicher Exporthinweis gesondert genannt.

## 6. Beispiele

### 6.1. Ausformulierter Rechnungstext für einen einfachen Standardfall

„Rechnung [Nummer] vom [Datum]

Sehr geehrte Frau [Name], für die außergerichtliche Prüfung des Liefervertrags in der Fassung vom [Datum] berechnen wir auf Grundlage der Vergütungsvereinbarung vom [Datum] die im Zeitraum vom [Beginn] bis [Ende] erbrachten Leistungen. Die beigefügte Leistungsaufstellung weist sieben tatsächliche Stunden zu einem Stundensatz von 280 Euro netto aus. Hieraus ergibt sich ein Honorar von 1.960 Euro netto. Hinzu kommen vereinbarte eigene steuerpflichtige Auslagen in Höhe von 40 Euro netto. Der Nettobetrag beträgt damit 2.000 Euro; die Umsatzsteuer von 19 Prozent beträgt 380 Euro. Der Gesamtbetrag beträgt 2.380 Euro.

Der vereinbarte Gesamtdeckel von 2.500 Euro netto einschließlich Auslagen wird eingehalten. Für den abgerechneten Leistungszeitraum sind nach dem geprüften Stand keine Vorschüsse oder Teilzahlungen zu verrechnen. Bitte überweisen Sie den Rechnungsbetrag entsprechend der vereinbarten Zahlungsfrist bis zum [Datum] unter Angabe der Rechnungsnummer auf das unten genannte Konto.

Mit freundlichen Grüßen
[Name], Rechtsanwältin“

Vor Verwendung werden sämtliche Pflichtangaben ergänzt und die Aussage über fehlende Vorschüsse tatsächlich geprüft. Der Text ist keine universelle RVG-Rechnung; bei gesetzlichen Gebühren werden stattdessen die erforderlichen Gebührentatbestände, VV-Nummern und Werte aufgenommen. Der Betrag ist ein Rechenbeispiel, keine bestehende Forderung.

### 6.2. Vorschuss schließt den einfachen XML-Weg aus

Die Kanzlei hat bereits 1.190 Euro brutto als Vorschuss erhalten. Die Schlussleistung beträgt 2.380 Euro brutto. Eine zutreffende Schlussabrechnung muss die umsatzsteuerlich richtige Vorschussverrechnung und den verbleibenden Zahlbetrag abbilden. Das lokale `xrechnung.py` verarbeitet keine Vorschussverrechnung. Deshalb wird nicht einfach eine reduzierte Leistungsposition von 1.190 Euro erzeugt, die den tatsächlichen Leistungsumfang und Steuerausweis verfälschen könnte.

Der interne Vermerk lautet: „Die Hauptleistung beträgt nach geprüfter Grundlage 2.000 Euro netto zuzüglich 380 Euro Umsatzsteuer. Der Zahlungseingang vom [Datum] ist als Vorschuss zugeordnet. Die Schlussrechnung wird mit einem geeigneten Rechnungswerkzeug erstellt, das die erforderliche Verrechnung unterstützt. Der lokale XML-Standardexport wird für diese Rechnung nicht verwendet. Der konkrete steuerliche Verrechnungsnachweis und die Restforderung werden vor Freigabe abgeglichen.“

### 6.3. Vollständige Anfrage nach fehlenden B2G-Angaben

„Sehr geehrte Frau [Name], die Rechnung für unsere Beratung zum Vergabeverfahren [Bezeichnung] ist vorbereitet. Für die richtige elektronische Zuordnung benötigen wir noch die von Ihrer Stelle vorgegebene Leitweg-ID und, soweit erforderlich, die Bestellnummer. Als Leistungsempfänger ist derzeit [vollständige Körperschaft] mit der Anschrift [Anschrift] dokumentiert. Bitte teilen Sie uns mit, falls die Rechnung an eine andere rechtlich verantwortliche Stelle auszustellen ist.

Nach Ergänzung der Angaben erstellen und prüfen wir die XRechnung für den von Ihnen benannten Empfangsweg. Die Honorargrundlage bleibt die bestätigte Vereinbarung vom [Datum]; die Rückfrage betrifft ausschließlich die erforderlichen Rechnungs- und Zuordnungsdaten.

Mit freundlichen Grüßen
[Name], Rechtsanwältin“

Die Anfrage wird als Entwurf geliefert, solange ihr Versand nicht beauftragt ist. Eine bereits in der Akte vorhandene und aktuelle Leitweg-ID wird stattdessen verwendet und nicht erneut abgefragt.

### 6.4. Korrektur des falschen Leistungsempfängers

Eine Rechnung wurde an die Rechtsschutzversicherung adressiert, obwohl der Mandant selbst Empfänger der anwaltlichen Leistung ist. Der Vorgang wird nicht durch bloßes Umbenennen der PDF-Datei korrigiert. Prüfe die bereits erteilte Rechnung, die steuerliche Behandlung und den tatsächlichen Versandstand. Erstelle die erforderliche Berichtigung mit Bezug auf die ursprüngliche Rechnung und dokumentiere, welche Fassung dem richtigen Empfänger mitzuteilen ist.

Ein erläuternder Text lautet: „Die Rechnung vom [Datum] mit der Nummer [Nummer] wird hinsichtlich des Leistungsempfängers berichtigt. Empfänger der bezeichneten anwaltlichen Leistung ist [Mandant mit Anschrift]. Die Zahlung durch [Versicherung] erfolgt lediglich im Rahmen der dort bestehenden Deckung. Leistungszeitraum, Leistungsumfang und Vergütung bleiben nach dem geprüften Stand unverändert. Diese Berichtigung ist zusammen mit der ursprünglichen Rechnung aufzubewahren.“ Ob gerade diese Ergänzung genügt oder ein anderer Korrekturweg erforderlich ist, wird vor Verwendung anhand des Ausgangsdokuments entschieden.

### 6.5. Prüfprotokoll für eine tatsächlich exportierte XML-Datei

Ein vollständiger interner Vermerk lautet: „Die Datei Rechnung_Entwurf_v2.xml wurde aus den freigegebenen Eingabedaten vom [Datum] erzeugt. Die Honorargrundlage ist die Vereinbarung [Referenz]; der Leistungsnachweis umfasst die bestätigten Einträge [IDs]. Die Prüfung des inländischen Steuerfalls ergibt 19 Prozent Umsatzsteuer. Vorschussverrechnung, Rabatte und Gutschriften sind nach dem belegten Stand nicht enthalten. Der Export liegt damit innerhalb des dokumentierten Funktionsumfangs des lokalen Skripts.

Die Datei wurde mit KoSIT-Validator [tatsächliche Version] und Konfiguration [tatsächliche Fassung] geprüft. Das Ergebnis lautet [tatsächlicher Befund]. Die Sichtkontrolle wurde anhand der aus dieser XML erzeugten Darstellung vorgenommen. Rechnungsnummer, Empfänger, Leistungszeitraum, Positionen, Steuer und Zahlbetrag stimmen mit den freigegebenen Daten überein. Der tatsächliche Versandstatus lautet [Status].“

Ein solches Protokoll wird nur mit tatsächlich durchgeführten Prüfungen ausgefüllt. Die Platzhalter sind keine voreingestellten positiven Ergebnisse. Ergibt die Validierung einen Fehler, werden Regelkennung und betroffene Stelle benannt. Ein Fehler wegen einer fehlenden Käuferreferenz wird durch die richtige Information behoben, nicht durch einen beliebigen Text. Ein Warnhinweis zu einem zulässigen, aber vom Empfänger möglicherweise nicht akzeptierten Verfahren wird gesondert bewertet. Erst danach wird der konkrete nächste Schritt bestimmt.

Auch bei positivem technischen Ergebnis bleibt die materielle Forderungsprüfung eigenständig. Ein Validator kann weder die Echtheit einer Mandantenunterschrift noch die tatsächliche Bearbeitungsdauer feststellen. Das Protokoll dokumentiert deshalb ausdrücklich den begrenzten Gegenstand jeder Prüfung. Es ist ein interner Nachweis und wird nicht ungeprüft als zusätzliche Rechnungsanlage an den Empfänger versandt.
