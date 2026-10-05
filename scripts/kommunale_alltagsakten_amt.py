"""Vier kleine kommunale Arbeitsakten aus Würzburg, ohne Musterlösung.

Personen, Orte unterhalb der Stadtebene und Ereignisse sind erfunden.
Die Herkunftshinweise werden durch den gemeinsamen Builder außerhalb der PDFs ergänzt.
"""


def D(file, title, day, sender, body):
    return dict(file=file, title=title, date=day, sender=sender, body=body.strip())


def E(file, title, day, sender, recipient, body):
    return dict(file=file, title=title, date=day, **{'from': sender, 'to': recipient}, body=body.strip())


CASES = [
    dict(
        slug='akha-wuerzburg-glatteis',
        title='Würzburg: Ein Schritt auf die glatte Querung',
        summary='Ein Wintermorgen, ein früh gestreuter Straßenübergang und eine Meldung über neue Glätte. Ob der Sturz noch auf der Fahrbahn oder bereits am Gehweg geschah, bleibt streitig.',
        core=['01_Pruefauftrag.eml', '02_Sturzbericht.docx', '03_Streuplan.docx', '04_Einsatzprotokoll.docx', '06_Zeugin.eml', '09_Forderung.eml'],
        xlsx=[],
        attachments={'09_Forderung.eml': ['07_Befund.docx', '08_Haushaltshilfe_Rechnung.docx']},
        documents=[
            E('01_Pruefauftrag.eml', 'Querung Krummblattbogen – Auftrag zur Prüfung', '2026-10-05T08:15:00+02:00', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', 'Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Sehr geehrte Frau Klee,

namens der Stadt Würzburg beauftrage ich Sie mit der Prüfung der Forderung von Frau Kunigunde Zeisig aus ihrem Sturz am 13. Januar 2026. Die betroffene Straße ist eine innerörtliche Gemeindestraße in städtischer Straßenbaulast. Der Bauhof führt den Winterdienst dort mit eigenen Beschäftigten aus. Eine Übertragung der hier betroffenen Fahrbahnquerung auf Anlieger ist nicht dokumentiert. Für den benachbarten Gehweg haben wir die Zuordnung noch nicht abschließend aus dem Straßenverzeichnis geklärt.

Bitte erstellen Sie einen ausformulierten internen Prüfvermerk zu Haftungsgrund, Belegen und Forderungshöhe sowie einen vollständigen Antwortentwurf an Frau Zeisig. Bitte beachten Sie die unterschiedlichen Angaben zum Sturzort und die erneute Glätte nach der ersten Streufahrt. Wir benötigen das Ergebnis bis 8. Oktober; die Anspruchstellerin erwartet bis 12. Oktober eine Antwort. Klären Sie auch, welche Unterlagen für eine belastbare Entscheidung noch fehlen.

Das Mandat betrifft ausschließlich die Stadt. Unterlagen zu Versicherung, kommunalem Schadenausgleich oder Rückdeckung liegen dieser Akte nicht bei; weder eine Mitgliedschaft noch eine Deckungszusage ist festgestellt. Bitte nichts versenden, melden oder anerkennen. Eine Zahlung wurde bisher nicht veranlasst.

Mit freundlichen Grüßen
Gertraud Holler, Rechtsstelle'''),
            D('02_Sturzbericht.docx', 'Mein Sturz am Krummblattbogen', '14.01.2026', 'Kunigunde Zeisig · Flachsblütenweg 7, Würzburg', '''## 1 Weg und Sturz

Am Dienstag, 13. Januar, ging ich zur Bushaltestelle am Krummblattbogen. Ich wollte den Bus um 07:47 Uhr erreichen. Mein Sturz war ungefähr um 07:42 Uhr; Frau Rahmani schaute kurz danach auf ihr Telefon. Es war schon heller, die Straßenlaternen waren aber noch an. Ich trug flache Winterstiefel und hatte meine Einkaufstasche in der rechten Hand. Ich hatte kein Telefon in der Hand und lief nach meiner Erinnerung normal.

An der Einmündung des Spitalblütenwegs überquerte ich den Krummblattbogen auf der abgesenkten Verbindung zwischen Bäckerei und Haltestelle. Es gibt dort keinen Zebrastreifen. Kurz vor der gegenüberliegenden Absenkung rutschte mein rechter Fuß weg. Ich glaube, ich war noch auf der Fahrbahn, vielleicht einen halben Meter vom Bord entfernt. Nach dem Sturz lag meine linke Hand auf dem Gehweg. Die Fahrbahn sah nur feucht aus; beim Aufstehen fühlte ich eine glatte, dünne Schicht.

## 2 Hilfe und Beschwerden

Frau Rahmani half mir auf eine Bank. Eine Bekannte holte mich ab und brachte mich später in die Praxis. Mein rechtes Knie und das linke Handgelenk taten weh. Ich habe den genauen Punkt nicht fotografiert. Mein erster Anruf beim Bauhof erfolgte erst gegen 10 Uhr. An der Absenkung lag etwas Streugut; ich kann nicht sagen, ob es vor oder nach meinem Sturz dort hingelangt war.

Kunigunde Zeisig'''),
            D('03_Streuplan.docx', 'Winterdienst – Abschnitt Krummblattbogen', '02.12.2025', 'Stadt Würzburg · Bauhof · Ottmar Dörflein', '''## 1 Abschnitt und Nutzung

Der Abschnitt W-12 umfasst den Krummblattbogen zwischen dem Flachsblütenweg und dem Hoflaubenplatz innerhalb der geschlossenen Ortslage. Die Fahrbahn ist sechs Meter breit. Am Spitalblütenweg fällt sie auf etwa 25 Metern leicht zur Einmündung ab; die Messung vom Herbst ergab rund vier Prozent. Die Kurve und eine hohe Mauer verschatten die Einmündung morgens. Hier münden die zu Fuß benutzten Wege zur Haltestelle und zur Bäckerei. Eine abgesenkte Querung verbindet beide Gehwegseiten. Ein Fußgängerüberweg mit Markierung ist nicht angeordnet.

Nach unserer Zählung an einem gewöhnlichen Werktag im November benutzten zwischen 07:00 und 08:00 Uhr 74 Fußgänger die Querung. Der nächste abgesenkte Übergang liegt etwa 310 Meter entfernt. Die Straße dient der Buslinie sowie der Zufahrt zum Ärztehaus. Die Busse verkehren werktags ab 06:05 Uhr. Die Zählung ist eine einzelne örtliche Beobachtung; sie erfasst keine Wintertage.

## 2 Einsatzvorgabe

W-12 ist im Dienstplan als erste Tour eingetragen. Bei entsprechender Wetterlage beginnt die Bereitschaft um 05:00 Uhr; die Streufahrt soll um 05:30 Uhr ausrücken. Der Fahrer streut die Fahrbahn einschließlich der bezeichneten Querung. Die Gehwegstreifen außerhalb der Querung gehören nicht zu diesem Tourenblatt. Neue Glättemeldungen sind der Disposition sofort zuzuleiten. Diese entscheidet anhand des betroffenen Orts, laufender Einsätze und der verfügbaren Kräfte über eine Kontroll- oder Nachstreufahrt.

Ottmar Dörflein, Freigabe der Tourenfassung'''),
            D('04_Einsatzprotokoll.docx', 'Winterdienst am 13. Januar – Tour und Rückmeldungen', '14.01.2026', 'Stadt Würzburg · Bauhof · Disposition und Fahrer Emil Kilian', '''## 1 Erste Tour

05:08 Uhr: Bereitschaft meldet Reif und stellenweise glatte Fahrbahn auf dem Betriebshof. 05:31 Uhr: Fahrzeug 2 fährt aus. 05:54 Uhr: Eintrag des Fahrers für Krummblattbogen, Strecke einschließlich Querung gestreut; Dosierung nach Anzeige 15 Gramm je Quadratmeter. Die Fahrzeugaufzeichnung bestätigt die Durchfahrt um 05:54 Uhr, enthält aber keinen gesonderten Sensorwert für den Salzauftrag an der Querung. Der Fahrer erklärt, der Streuer sei durchgehend eingeschaltet gewesen. Um 06:32 Uhr endet die erste Tour.

## 2 Weitere Meldungen

07:20 Uhr: Bäckerei ruft an. „Übergang beim Spitalblütenweg wieder spiegelig, Leute rutschen.“ Die Disponentin notiert zunächst „Gehweg Bäckerei“. Um 07:23 Uhr bittet sie Fahrzeug 2 um Rückruf. Dieses bearbeitet eine Glättemeldung an einer steilen Zufahrt zum Seniorenhaus. Um 07:35 Uhr wird die Nachstreufahrt zum Krummblattbogen zugeteilt. Die Standortaufzeichnung zeigt Ankunft um 07:51 Uhr. Der Fahrer streut um 07:52 Uhr Fahrbahnquerung und beide Absenkungen.

## 3 Nachtrag

Vom Sturz erfuhr die Disposition um 10:03 Uhr. Der Fahrer erinnert sich bei der zweiten Fahrt an einen dünnen glänzenden Belag nahe dem südlichen Bord. Er hat weder fotografiert noch eine Temperatur gemessen. Die ungenaue Ortsbezeichnung der ersten telefonischen Meldung wurde erst bei der Besprechung am 14. Januar berichtigt. Die obigen Zeitangaben stammen aus dem Tourensystem und dem handschriftlichen Telefonblatt.

Ottmar Dörflein'''),
            D('05_Wetterbeobachtung.docx', 'Örtliche Beobachtungen der Frühschicht', '13.01.2026', 'Stadt Würzburg · Bauhof · Huriye Demir', '''## 1 Beobachtungsort

Dieses Blatt gibt unsere eigenen Beobachtungen am Betriebshof am Kieslaubenweg wieder. Der Hof liegt etwa 1,8 Kilometer von der Querung Krummblattbogen entfernt. Die Werte stammen von einem handelsüblichen Außenthermometer unter dem Vordach, nicht von einer amtlichen Wetterstation. Eine Wetterdienstauskunft oder örtliche Messung an der Unfallstelle ist damit nicht verbunden.

## 2 Aufzeichnungen

05:00 Uhr: minus 1,3 Grad Celsius, auf abgestellten Fahrzeugen Reif, kein erkennbarer Niederschlag. 06:15 Uhr: minus 0,7 Grad Celsius, die Oberfläche im Hof nach Streuen feucht. 07:05 Uhr: feiner Sprühregen beginnt. 07:25 Uhr: Thermometer minus 0,4 Grad Celsius; auf einem ungestreuten Metalltritt bildet sich ein glatter Film. Ich melde dies um 07:27 Uhr telefonisch an die Disposition. 08:00 Uhr: Niederschlag schwächer, weiterhin feuchte Hofoberfläche.

Ich war nicht am Krummblattbogen. Ob und ab wann es dort ebenfalls sprühte oder die Fahrbahn wieder fror, kann ich nicht bestätigen. Eine Auswertung einer amtlichen Wetterquelle habe ich nicht vorgenommen. Unsere Notiz soll nur festhalten, was wir während der Schicht selbst wahrgenommen und weitergegeben haben.

Huriye Demir'''),
            E('06_Zeugin.eml', 'Ihre Rückfrage zum Januarsturz', '2026-09-24T16:40:00+02:00', 'Leila Rahmani <leila.rahmani@briefpost.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', '''Sehr geehrte Frau Holler,

ich war an der Haltestelle und sah Frau Zeisig von der Bäckereiseite kommen. Kurz vor dem Ende der Querung fiel sie nach links. Für mich war der rechte Fuß schon am abgesenkten Gehwegrand, aber ich sah das letzte Auftreten nicht genau, weil ein parkendes Lieferfahrzeug die Beine teilweise verdeckte. Ich kann deshalb nicht sicher sagen, wo ihr Fuß wegrutschte. Mein Telefon zeigte nach dem Hinlaufen 07:43 Uhr.

Auf der Fahrbahn und direkt an der Absenkung glänzte es. Ich selbst ging vorsichtig, weil ich kurz vorher auf der Querung etwas gerutscht war. Auf dem Gehweg hinter der Haltestelle fühlte es sich griffiger an. Zwischen diesen Stellen habe ich keine genaue Prüfung gemacht. Frau Zeisig ist nach meinem Eindruck nicht gerannt. Sie sagte allerdings, sie dürfe den Bus nicht verpassen. Ihre Schuhsohlen habe ich nicht angesehen.

Ein Streufahrzeug kam, als ich schon im Bus saß. Eine andere Frau fotografierte wohl die Straße; ihren Namen kenne ich nicht. Eigene Fotos habe ich nicht.

Freundliche Grüße
Leila Rahmani'''),
            D('07_Befund.docx', 'Ambulanter Befund und Verlauf', '03.02.2026', 'Praxis Dr. Parvin Herbst · Wiesenkornweg 4, Würzburg', '''Patientin: Kunigunde Zeisig, geboren am 9. März 1961. Dieser Bericht fasst die Behandlung vom 13. Januar und die Kontrolle vom 3. Februar 2026 zusammen.

## 1 Erstuntersuchung

Am 13. Januar um 11:10 Uhr berichtet die Patientin über einen Sturz auf vereistem Untergrund. Es bestehen eine Prellung am rechten Knie sowie Schwellung und Druckschmerz am linken Handgelenk. Die veranlasste Röntgenuntersuchung zeigt keine frische knöcherne Verletzung. Durchblutung und Sensibilität sind erhalten. Diagnostiziert werden eine Handgelenksdistorsion links und eine Knieprellung rechts. Verordnet werden zeitweise Ruhigstellung, Kühlung und bedarfsgerechte Schmerzmedikation.

## 2 Verlauf

Bei der Kontrolle am 3. Februar ist die Beweglichkeit deutlich gebessert; beim kräftigen Greifen berichtet die Patientin noch über Schmerzen. Eine weitere Kontrolle wird bei fortbestehenden Beschwerden empfohlen. Eine dauerhafte Einschränkung lässt sich derzeit nicht feststellen. Eine Begutachtung der konkreten Haushaltsführung oder des erforderlichen Hilfebedarfs fand nicht statt. Die Patientin gab an, in den ersten zehn Tagen weder einen Wäschekorb noch schwere Einkaufstaschen mit beiden Händen tragen zu können.

Dr. Parvin Herbst'''),
            D('08_Haushaltshilfe_Rechnung.docx', 'Rechnung HH-260124 mit Zahlungseingang', '24.01.2026', 'Haushaltshilfe Agnes Merklein · Malvenkornweg 12, Würzburg', '''Rechnungsempfängerin: Kunigunde Zeisig, Flachsblütenweg 7, Würzburg.

Für die am 15., 19. und 22. Januar 2026 geleistete Hilfe berechne ich insgesamt fünf Stunden zu jeweils 25,00 EUR netto. Am 15. Januar entfielen zwei Stunden auf Einkauf und Reinigung von Küche und Bad, am 19. Januar zwei Stunden auf Wäsche und Böden, am 22. Januar eine Stunde auf Einkauf und Müllentsorgung. Die Auftraggeberin bestätigte die Anwesenheitszeiten jeweils auf meinem Arbeitszettel.

Der Nettobetrag beträgt 125,00 EUR. Hinzu kommen 23,75 EUR Umsatzsteuer bei einem Steuersatz von 19 Prozent. Der Rechnungsbetrag beträgt 148,75 EUR. Weitere Wegegelder oder Materialkosten werden nicht berechnet.

Zahlungsbestätigung vom 29. Januar 2026: Der Betrag von 148,75 EUR ist vollständig per Überweisung eingegangen. Die Hilfen wurden tatsächlich geleistet; es handelt sich nicht um einen Kostenvoranschlag.

Agnes Merklein'''),
            E('09_Forderung.eml', 'Sturz im Januar – jetzt bitte Entscheidung', '2026-09-30T09:12:00+02:00', 'Kunigunde Zeisig <kunigunde.zeisig@briefpost.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', '''Sehr geehrte Frau Holler,

nachdem ich Ihnen im Januar den Sturz gemeldet hatte, möchte ich die Sache nun erledigen. Ich verlange 1.600,00 EUR Schmerzensgeld und 148,75 EUR für die bezahlte Haushaltshilfe, zusammen 1.748,75 EUR. Den Behandlungsbericht und die Rechnung mit Zahlungseingang füge ich bei. Weitere Behandlungskosten verlange ich nicht; diese wurden über meine Krankenkasse abgerechnet. Ob die Krankenkasse Ansprüche geltend macht, weiß ich nicht.

Die Beschwerden am Handgelenk dauerten nach meinem Empfinden etwa sechs Wochen. Einen weiteren Arztbericht habe ich nicht, weil es dann besser wurde. Ich wohne mit meinem Mann in einer Wohnung von 78 Quadratmetern. Er übernahm das Kochen, konnte wegen seiner eigenen Schulterbeschwerden aber keine schweren Einkäufe tragen. Einen zusätzlichen Geldbetrag für seine Hilfe verlange ich nicht.

Nach meinem Sturz sagte jemand, am Morgen sei bereits gestreut worden. Das mag sein; die Stelle war trotzdem glatt. Ich bitte um eine begründete Antwort bis 12. Oktober. Einen Rechtsanwalt habe ich bisher nicht beauftragt.

Mit freundlichen Grüßen
Kunigunde Zeisig'''),
        ],
    ),
    dict(
        slug='akha-wuerzburg-antragsbearbeitung',
        title='Würzburg: Der Kaffeestand im falschen Monat',
        summary='Ein vollständiger Sondernutzungsantrag wird mit einem falschen Veranstaltungsdatum erfasst. Nach Nachfragen bleibt eine Wagenmiete von 238 Euro; der mögliche rechtzeitige Rechtsschutz ist ungeklärt.',
        core=['01_Pruefauftrag.eml', '02_Antrag.docx', '04_Registerauszug.docx', '06_Dringende_Nachfrage.eml', '07_Sachgebietsleitung.docx', '10_Forderung.eml'],
        xlsx=[],
        attachments={'10_Forderung.eml': ['08_Wagenmiete_Rechnung.docx', '09_Vermieter.eml']},
        documents=[
            E('01_Pruefauftrag.eml', 'Kaffeestand Nouri – kleiner Vermögensschaden', '2026-10-05T08:30:00+02:00', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', 'Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Sehr geehrte Frau Klee,

die Stadt Würzburg beauftragt Sie mit der Prüfung der Forderung von Herrn Nouri wegen der Bearbeitung seines Antrags für einen mobilen Kaffeestand. Zuständig für die Sondernutzung der betreffenden Gemeindestraße war unser Sachgebiet Straßenrecht. Die Bearbeitung erfolgte durch eigene Beschäftigte. Es geht um 238,00 EUR Wagenmiete und nicht um einen Sach- oder Personenschaden.

Bitte erstellen Sie einen internen Prüfvermerk und einen vollständigen Antwortentwurf an Herrn Nouri. Wir möchten insbesondere wissen, was der falsche Registereintrag für die tatsächlich mögliche Erlaubniserteilung bedeutet und welche Bedeutung seine Nachfragen und der unterbliebene gerichtliche Eilantrag haben. Bitte prüfen Sie auch, ob die geltend gemachte Ausgabe bei richtiger Bearbeitung in gleicher Höhe angefallen wäre und welchen Nutzen sie dann gehabt hätte. Eine pauschale Aussage, ein Verwaltungsfehler genüge bereits, hilft uns nicht.

Das Ergebnis benötigen wir bis 8. Oktober; Herrn Nouri wurde eine Rückmeldung bis 12. Oktober angekündigt. Das Mandat betrifft nur die Stadt. Versicherungs- oder Schadenausgleichsunterlagen sind nicht vorhanden. Bitte erstellen Sie die Dokumente zur internen Verwendung und versenden Sie nichts. Eine Erstattung wurde weder zugesagt noch gezahlt.

Mit freundlichen Grüßen
Gertraud Holler'''),
            D('02_Antrag.docx', 'Antrag auf Sondernutzung – Kaffeewagen', '28.04.2026', 'Samir Nouri · Kaffee Nouri · Löwensamenweg 3, Würzburg', '''## 1 Beantragte Nutzung

Ich beantrage die Erlaubnis, am Samstag, 20. Juni 2026, und Sonntag, 21. Juni 2026, jeweils von 09:00 bis 17:00 Uhr einen mobilen Kaffeewagen auf der befestigten Seitenfläche des Krummblattplatzes aufzustellen. Beantragt ist ausschließlich der Verkauf von Kaffee, Tee und abgepacktem Gebäck zum Mitnehmen. Alkohol, Sitzplätze und Musik sind nicht vorgesehen. Ich betreibe Kaffee Nouri als Einzelunternehmen. Die gewünschte Fläche liegt neben dem Zugang zum dortigen offenen Handwerkertag, jedoch außerhalb der von dessen Veranstalter gemieteten Fläche.

## 2 Umfang und Standort

Der Wagen ist 2,40 Meter lang und 1,60 Meter breit. Mit Ausgabebereich beantrage ich eine rechteckige Fläche von drei mal zwei Metern. Sie liegt am nordöstlichen Rand des Platzes, beginnend vier Meter südlich des Straßenbaums und mit einem Meter Abstand zur niedrigen Mauer. Zum Gehweg bleiben nach meiner Messung mindestens 2,50 Meter frei. Der Rettungsweg auf der Fahrbahn wird nicht benutzt. Strom und Wasser bringt der Wagen mit; Kabel oder Leitungen über öffentliche Wege sind nicht erforderlich.

## 3 Angaben zum Betrieb

Auf- und Abbau erfolgen an beiden Tagen außerhalb der Verkaufszeit. Ich nehme sämtliche Abfälle mit. Die im Antragsformular verlangten Angaben zu Gewerbe, verantwortlicher Person und Standort sind hier vollständig eingetragen; meine Gewerbeanmeldung ist unter der vorhandenen städtischen Registriernummer bereits zugeordnet. Eine andere Fläche oder andere Tage beantrage ich nicht. Bitte teilen Sie mir bis Ende Mai mit, ob ich den Wagen verbindlich buchen kann.

Samir Nouri'''),
            E('03_Eingangsbestaetigung.eml', 'Ihr Antrag Kaffeewagen – Eingang und Vollständigkeit', '2026-04-29T10:05:00+02:00', 'Edeltraud Merk <strassenrecht@wuerzburg-fallakten.example>', 'Samir Nouri <samir@kaffee-nouri.example>', '''Sehr geehrter Herr Nouri,

Ihr Antrag vom 28. April auf Nutzung der Seitenfläche am Krummblattplatz am 20. und 21. Juni 2026 ist am 28. April um 14:22 Uhr bei uns eingegangen. Die für die Bearbeitung von Ihnen verlangten Angaben sind vollständig. Eine Nachforderung an Sie besteht derzeit nicht. Wir holen noch die örtliche Stellungnahme zur freien Gehwegbreite ein.

Diese Nachricht bestätigt den Eingang, enthält jedoch noch keine Erlaubnis. Über die Sondernutzung entscheidet die Sachgebietsleitung Straßenrecht. Ich nehme Anträge auf und bereite die Unterlagen vor; die Entscheidung treffe ich nicht. Für diesen Antrag wird keine andere Stelle der Stadt einen gesonderten Sondernutzungsbescheid erlassen.

Sie erhalten die Entscheidung nach der örtlichen Abstimmung. Ich habe Ihre Bitte um Rückmeldung vor der verbindlichen Wagenbuchung vermerkt. Bitte teilen Sie Änderungen am Wagen, an der Fläche oder an den Tagen mit; anderenfalls bearbeiten wir die Angaben aus Ihrem eingegangenen Antrag.

Mit freundlichen Grüßen
Edeltraud Merk'''),
            D('04_Registerauszug.docx', 'Auszug aus dem Bearbeitungsregister', '24.06.2026', 'Stadt Würzburg · Sachgebiet Straßenrecht · Eberhard Abelein', '''## 1 Gespeicherte Einträge

28. April, 14:22 Uhr: Antrag Nouri eingegangen. 29. April, 09:48 Uhr: Stammsatz angelegt durch E. Merk. Das Feld „Nutzung von/bis“ enthält 20.07.2026 bis 21.07.2026. Im gespeicherten Originalantrag stehen dagegen 20.06.2026 und 21.06.2026. Das Feld „Wiedervorlage“ wurde nach dem Stammsatz auf 29.06.2026 gesetzt. Eine automatische Gegenprüfung mit dem Text des Antrags gibt es nicht.

7. Mai, 11:30 Uhr: Ortsprüfung durch Straßenbetrieb. Drei mal zwei Meter an der bezeichneten Stelle möglich, Gehwegbreite 2,55 Meter gemessen; keine Überschneidung mit Baustellen oder anderer zugelassener Nutzung. 11. Mai, 08:55 Uhr: Sachgebietsleitung vermerkt „nach Ortsprüfung zustimmungsfähig; zwei beantragte Tage, Wagen ohne Sitzplätze“. Anschließend bleibt die Akte in der Wiedervorlage für Ende Juni.

## 2 Nachträge

15. Juni: Telefonische Nachfrage des Antragstellers als „fragt Bearbeitungsstand“ eingetragen; das Datum des gewünschten Einsatzes wird nicht überprüft. 19. Juni, 11:06 Uhr: Nach der schriftlichen Nachfrage wird die Abweichung erkannt und das Datumsfeld korrigiert. Die Sachgebietsleitung ist an diesem Tag wegen eines Außentermins nur telefonisch erreichbar. Eine Entscheidung wird vor Beginn der beantragten Nutzung nicht erstellt.

Dieser Ausdruck wurde aus den gespeicherten Feldern am 24. Juni hergestellt. Er enthält keine Entscheidung über eine Zahlung an Herrn Nouri.

Eberhard Abelein'''),
            E('05_Falsche_Auskunft.eml', 'Bearbeitungsstand Kaffeewagen', '2026-06-15T15:10:00+02:00', 'Edeltraud Merk <strassenrecht@wuerzburg-fallakten.example>', 'Samir Nouri <samir@kaffee-nouri.example>', '''Sehr geehrter Herr Nouri,

zu Ihrem heutigen Anruf habe ich den Bearbeitungsstand geprüft. Ihr Vorgang liegt auf Wiedervorlage Ende Juni; die Entscheidung ist rechtzeitig vor dem in unserem Register eingetragenen Einsatz im Juli vorgesehen. Eine Bevorzugung gegenüber anderen laufenden Anträgen kann ich nicht zusagen. Für Ihren Antrag fehlen nach unserem Register keine Unterlagen.

Falls Sie meinen, dass die Daten bei uns nicht stimmen, antworten Sie bitte auf diese Nachricht mit dem konkreten Datum und der Bezeichnung Ihres Standorts. Ich kann die Einträge dann mit der Sachgebietsleitung abgleichen. Ich selbst darf keine Sondernutzung erlauben und kann Ihnen deshalb auch telefonisch keine Freigabe geben.

Bitte beachten Sie, dass ein aufgebauter Wagen ohne schriftliche Erlaubnis von uns nicht als genehmigt behandelt wird. Eine Auskunft zu gerichtlichen Verfahren kann ich Ihnen nicht erteilen. Ich bin morgen im Außendienst; das Sammelpostfach wird durch die Vertretung gelesen.

Mit freundlichen Grüßen
Edeltraud Merk'''),
            E('06_Dringende_Nachfrage.eml', 'Dringend: Einsatz ist dieses Wochenende im Juni', '2026-06-16T08:12:00+02:00', 'Samir Nouri <samir@kaffee-nouri.example>', 'Edeltraud Merk <strassenrecht@wuerzburg-fallakten.example>', '''Sehr geehrte Frau Merk,

das muss ein Versehen sein. Mein Antrag betrifft den 20. und 21. Juni, also dieses Wochenende. Das steht auch in Ihrer Eingangsbestätigung. Ich habe den Wagen nach Ablauf der von mir erbetenen Rückmeldefrist am 2. Juni gebucht, weil ich nach sechs Wochen und der bestätigten Vollständigkeit nicht mehr mit solchen Problemen gerechnet habe. Der Vermieter hat nur noch diesen Wagen frei gehabt.

Bitte legen Sie die Sache heute der zuständigen Leitung vor und treffen Sie bis Donnerstag eine Entscheidung. Ich kann den Wagen bis Mittwochabend noch gegen 119,00 EUR stornieren; danach werden die vollen 238,00 EUR fällig. Wenn Sie weitere Angaben brauchen, erreichen Sie mich unter meiner hinterlegten Telefonnummer. Eine andere Veranstaltung habe ich an dem Wochenende nicht.

Ich habe gestern im Internet etwas über einen Eilantrag beim Verwaltungsgericht gelesen. Ich weiß aber nicht, wie ich bis zum Wochenende eine Entscheidung bekommen soll. Zunächst hoffe ich, dass Sie den Datumsfehler selbst berichtigen und den seit April vorliegenden Antrag bearbeiten. Bitte bestätigen Sie mir wenigstens, dass meine Nachricht angekommen ist.

Mit freundlichen Grüßen
Samir Nouri'''),
            D('07_Sachgebietsleitung.docx', 'Notiz zum Ablauf des Antrags Nouri', '24.06.2026', 'Stadt Würzburg · Straßenrecht · Sachgebietsleiter Eberhard Abelein', '''## 1 Zuständigkeit und Bearbeitungsstand

Ich bin nach der internen Zeichnungsregel befugt, über eine zeitlich beschränkte Sondernutzung an der hier betroffenen Gemeindestraße zu entscheiden. Frau Merk bereitet die Vorgänge vor und darf keine Erlaubnis erteilen. Die örtliche Stellungnahme war am 7. Mai vollständig. Aus meiner Sicht sprach nach den damals vorliegenden Angaben nichts gegen den beantragten Kaffeewagen an den beiden Junitagen; deshalb hatte ich am 11. Mai die positive Bearbeitungsnotiz gesetzt. Ich hätte bei richtiger Wiedervorlage den Bescheid mit den üblichen Vorgaben zur Fläche, Gehwegbreite und Reinigung unterschrieben. Einen unterschriebenen Bescheid gab es aber nicht.

## 2 Nachfragen vor dem Wochenende

Die Nachricht vom 16. Juni wurde erst am 19. Juni aus dem Vertretungspostfach zugeordnet. Frau Merk sagte Herrn Nouri nach ihrer Erinnerung am 18. Juni telefonisch, die Sache werde „noch rechtzeitig vorgelegt“. Eine feste Zusage, ich werde an diesem Tag entscheiden, sollte sie damit nicht abgeben. Eine eigene Telefonnotiz von diesem Gespräch gibt es nicht. Herr Nouri erinnert sich an die Worte „Sie bekommen das morgen“.

Am 19. Juni erreichte mich der Anruf der Vertretung erst gegen 15:40 Uhr. Ich ließ mir den Vorgang nicht mehr elektronisch übermitteln und unterschrieb an diesem Tag nichts. Ein Hindernis durch konkurrierende Nutzung, fehlende Unterlagen oder einen geänderten Standort ist mir auch nachträglich nicht bekannt geworden. Die beantragten Tage verstrichen ohne Bescheid. Herr Nouri stellte den Wagen nicht auf.

Eberhard Abelein'''),
            D('08_Wagenmiete_Rechnung.docx', 'Bestätigung der Wagenmiete und Rechnung KN-260602', '02.06.2026', 'Karla Storch · Kleiner Wagenverleih · Saatlaubenweg 8, Würzburg', '''Mieter: Samir Nouri, Kaffee Nouri, Löwensamenweg 3, Würzburg. Gemietet wird der mobile Kaffeewagen „Spatz“ für den 20. und 21. Juni 2026. Übergabe ist für den 19. Juni um 17:00 Uhr, Rückgabe für den 22. Juni um 09:00 Uhr vereinbart. Erforderliche öffentlich-rechtliche Erlaubnisse beschafft der Mieter selbst; ihr Ausbleiben ist nicht als kostenloser Rücktrittsgrund vereinbart.

Der Mietpreis beträgt für beide Einsatztage zusammen 200,00 EUR netto zuzüglich 38,00 EUR Umsatzsteuer, insgesamt 238,00 EUR. Der Rechnungsbetrag ist bis 10. Juni fällig. Er ging am 8. Juni vollständig ein. Bei schriftlicher Stornierung bis 17. Juni um 18:00 Uhr werden 119,00 EUR einbehalten und 119,00 EUR erstattet. Bei späterer Absage bleibt der volle Mietpreis geschuldet, soweit der Wagen nicht anderweitig vermietet werden kann; eine anderweitige Vermietung wird angerechnet.

Die Vermieterin hält den Wagen für die genannten Tage bereit. Betriebsstoffe und Waren gehören nicht zum Mietpreis. Eine Kaution fällt für Herrn Nouri als Bestandskunden nicht an. Diese Bestätigung enthält die bei Buchung vereinbarten Bedingungen und dient zugleich als Rechnung.

Karla Storch'''),
            E('09_Vermieter.eml', 'Keine Ersatzvermietung des Kaffeewagens', '2026-06-23T12:20:00+02:00', 'Karla Storch <karla@kleiner-wagenverleih.example>', 'Samir Nouri <samir@kaffee-nouri.example>', '''Hallo Herr Nouri,

Ihre Absage kam am Freitag, 19. Juni, um 16:22 Uhr. Ich habe anschließend noch zwei Interessenten angerufen, die sich früher nach dem Wagen erkundigt hatten. Beide hatten inzwischen andere Lösungen. Der Wagen blieb über das Wochenende im Hof; eine andere Vermietung oder Einnahme gab es nicht. Die Rechnung über 238,00 EUR bleibt deshalb nach unserer Buchungsvereinbarung bestehen.

Sie hatten den Wagen weder abgeholt noch für eine andere Tätigkeit eingesetzt. Ich kann ihn nicht rückwirkend für ein späteres Wochenende gutschreiben. Für eine spätere Miete könnten wir neu sprechen; eine kostenlose Umbuchung war nicht vereinbart. Das ist für Sie ärgerlich, aber nach Ihrer Absage war die vereinbarte halbe Stornierung bereits abgelaufen.

Den Zahlungseingang am 8. Juni und die Bereitschaft des Wagens am vereinbarten Übergabetag bestätige ich Ihnen. Eine gesonderte Berechnung für Abholung, Reinigung oder Verbrauch stelle ich nicht aus, weil diese Leistungen nicht angefallen sind.

Freundliche Grüße
Karla Storch'''),
            E('10_Forderung.eml', 'Erstattung Wagenmiete – 238 Euro', '2026-09-29T10:45:00+02:00', 'Samir Nouri <samir@kaffee-nouri.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', '''Sehr geehrte Frau Holler,

ich verlange die Erstattung der nutzlos gewordenen Wagenmiete von 238,00 EUR. Die Rechnung und die Bestätigung des Vermieters erhalten Sie als Anlagen. Ich wende die Kleinunternehmerregelung an und ziehe aus dieser Rechnung keine Vorsteuer. Einen Verdienstausfall oder entgangenen Gewinn fordere ich derzeit nicht. Waren hatte ich rechtzeitig weiterverwenden können; dafür entsteht keine zusätzliche Forderung.

Bis Mittwochabend hatte ich auf meine schriftliche Richtigstellung vom 16. Juni noch keine Antwort. Ich ließ die halbe Stornierungsfrist verstreichen, weil ich hoffte, der Datumsfehler werde rechtzeitig behoben. Erst beim Anruf am 18. Juni sagte Frau Merk nach meiner Erinnerung, ich bekäme die Erlaubnis am nächsten Tag. Das bestärkte mich darin, weiter abzuwarten. Am Freitag habe ich um 16 Uhr noch einmal angerufen; erst dann war klar, dass niemand mehr unterschreiben würde. Beim Gericht habe ich nichts eingereicht, weil ich auf die angekündigte behördliche Korrektur vertraute. Einen Rechtsanwalt hatte ich in diesen Tagen nicht.

Ich hätte an den beiden Tagen geöffnet und selbst im Wagen gearbeitet. Verbindliche Vorbestellungen lagen nicht vor. Den Erfolg meines Standes kann ich daher nicht mit sicheren Umsätzen belegen. Ich möchte aber wenigstens die bezahlt gebliebene Miete ersetzt haben. Bitte antworten Sie bis 12. Oktober.

Mit freundlichen Grüßen
Samir Nouri'''),
        ],
    ),
    dict(
        slug='akha-wuerzburg-baugenehmigung',
        title='Würzburg: Ein Büro wird als Werkstatt abgelehnt',
        summary='Eine kleine Nutzungsänderung wird wegen falsch zugeordneter Betriebsangaben versagt und nach Klageerhebung genehmigt. Gefordert werden zwei Monatsmieten und Bereitstellungszinsen.',
        core=['01_Pruefauftrag.eml', '02_Antragsbeschreibung.docx', '03_Versagungsbescheid.docx', '04_Klage.eml', '06_Abhilfe_Genehmigung.docx', '10_Forderung.eml'],
        xlsx=[],
        attachments={'10_Forderung.eml': ['07_Mietvertrag.docx', '08_Bankabrechnung.docx', '09_Zahlungsnachweis.docx']},
        documents=[
            E('01_Pruefauftrag.eml', 'Nutzungsänderung Frau Adebayo – Prüfung der Folgekosten', '2026-10-05T09:05:00+02:00', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', 'Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Sehr geehrte Frau Klee,

für die Stadt Würzburg beauftrage ich Sie mit der Prüfung der Forderung von Frau Tola Adebayo. Unsere Bauaufsicht als untere Bauaufsichtsbehörde der kreisfreien Stadt hatte ihre Nutzungsänderung einschließlich der baulichen Änderung zunächst versagt und nach Überprüfung genehmigt. Frau Adebayo hat gegen die Versagung rechtzeitig Klage erhoben. Das Verwaltungsverfahren und der geltend gemachte Geldanspruch sind getrennt zu betrachten; für das Verfahren vor dem Verwaltungsgericht ist auf ihrer Seite Rechtsanwältin Weller tätig.

Bitte verfassen Sie einen internen Prüfvermerk zu Verantwortlichkeit, Verschulden und dem Ablauf bei zutreffender Bearbeitung sowie einen vollständigen Antwortentwurf an Frau Weller zur Geldforderung. Die behaupteten zwei Monate Verzögerung sollen anhand der Bearbeitungsstände, des Mietvertrags und der Finanzierung geprüft werden. Uns genügt kein Verweis darauf, dass später eine Genehmigung erging. Das Ergebnis benötigen wir bis 8. Oktober, der Antwortentwurf soll die Frist vom 12. Oktober berücksichtigen.

Das Mandat erteile ich ausschließlich für die Stadt als Rechtsträgerin der beteiligten Bauaufsicht. Ein Anspruch gegen einzelne Beschäftigte ist nicht Gegenstand unseres Auftrags. Versicherungsbedingungen oder Unterlagen zu einem kommunalen Schadenausgleich liegen nicht vor. Bitte keine Zahlung zusagen und nichts versenden oder bei Gericht einreichen.

Mit freundlichen Grüßen
Gertraud Holler'''),
            D('02_Antragsbeschreibung.docx', 'Nutzungsänderung Lagerraum zu Planungsbüro', '14.04.2026', 'Tola Adebayo · Bauherrin · Haselkornbogen 5, Würzburg', '''## 1 Gegenstand des Antrags

Ich beantrage die Nutzungsänderung des bisher unbeheizten Lagerraums im Erdgeschoss am Haselkornbogen 5 in ein Planungsbüro sowie den unten beschriebenen Eingriff in eine tragende Innenwand. Das dreigeschossige Gebäude hat sechs selbstständige Nutzungseinheiten. Die Nutzfläche unseres Raums beträgt 42 Quadratmeter. Im Büro werden ich und eine angestellte Zeichnerin arbeiten. Wir erstellen am Computer Innenraumpläne. Es gibt keine Werkstatt, keine Produktionsmaschinen, keinen Warenverkauf und keine Lagerung von Baustoffen. Gelegentliche Kundenbesprechungen mit höchstens zwei Besuchern finden tagsüber statt. Der Zugang erfolgt unmittelbar von der Straße.

## 2 Unterlagen und Grundstück

Grundriss, Betriebsbeschreibung, Angaben zur bisherigen Nutzung und der statische Nachweis zur Wandöffnung wurden am 14. April gemeinsam bei der Bauaufsicht eingereicht. Fenster, Außentür und Sanitärräume bleiben bestehen. In der tragenden Innenwand ist eine neue 90 Zentimeter breite Türöffnung mit berechnetem Sturz vorgesehen; außerdem werden Arbeitsbeleuchtung, Steckdosen und Heizkörper eingebaut. Die bisherige Lagerfläche soll erstmals als dauerhafter Aufenthaltsraum dienen. Die hierfür eingereichten Nachweise zu Belichtung, Lüftung und baulichem Brandschutz liegen beim Antrag. Das Grundstück liegt in einer seit langem bebauten Straßenzeile mit Wohnungen, Büros und kleinen Läden; ein Bebauungsplan liegt dem Antrag nicht zugrunde.

## 3 Zeitlicher Hintergrund

Ich habe den Raum bereits angemietet. Der Mietbeginn ist der 1. Juni. Ich bitte deshalb um eine Entscheidung möglichst bis Mitte Mai. Der alte Dateiname meines Grundrisses enthält das Wort „Werkraum“, weil ich die Datei aus einer Vorplanung übernommen habe. Verbindlich sind die beigefügte Betriebsbeschreibung und die eingetragenen Raumnutzungen; eine handwerkliche Produktion ist ausdrücklich nicht beantragt.

Tola Adebayo

Eingangsvermerk der Bauaufsicht: Eingang am 14. April 2026; die Sachbearbeiterin bestätigte am 17. April 2026 die Vollständigkeit der eingereichten Unterlagen.'''),
            D('03_Versagungsbescheid.docx', 'Bescheid über die beantragte Nutzungsänderung', '02.06.2026', 'Stadt Würzburg · Bauaufsicht · Wolfram Reuther', '''Sehr geehrte Frau Adebayo,

## 1 Entscheidung

Ihr Antrag vom 14. April 2026 auf Nutzungsänderung des Lagerraums am Haselkornbogen 5 einschließlich der beantragten Öffnung in der tragenden Innenwand wird abgelehnt. Über die Verfahrenskosten ergeht eine gesonderte Mitteilung. Gegenstand dieser Entscheidung ist allein die beantragte Nutzung des bezeichneten Erdgeschossraums.

## 2 Begründung

Die bauplanungsrechtliche Zulässigkeit wird nach § 34 BauGB beurteilt. In der näheren Umgebung überwiegen Wohnnutzung, kleinere Büros und Läden. Der von uns der Prüfung zugrunde gelegte Werkstattbetrieb mit täglichem Maschinenbetrieb und regelmäßigem Anlieferverkehr fügt sich nach der Art der Nutzung nicht in diese Umgebung ein. Die für eine Genehmigung nach Art. 68 BayBO erforderlichen Voraussetzungen liegen damit nach dem hier zugrunde gelegten Betriebsumfang nicht vor. Eine Beschränkung der beantragten Werkstatt auf einen bloßen Bürobetrieb wäre eine wesentliche Änderung des Vorhabens, die Sie nicht beantragt haben.

## 3 Rechtsbehelfsbelehrung

Gegen diesen Bescheid kann innerhalb eines Monats nach seiner Bekanntgabe Klage beim Bayerischen Verwaltungsgericht Würzburg erhoben werden. Die Klage kann schriftlich, zur Niederschrift des Urkundsbeamten der Geschäftsstelle oder in zugelassener elektronischer Form erhoben werden. Eine einfache E-Mail genügt der vorgeschriebenen elektronischen Form nicht.

Wolfram Reuther, für die Bauaufsicht

Zustellvermerk der Akte: Die Ausfertigung wurde Frau Adebayo am 5. Juni 2026 gegen Empfangsbestätigung übergeben.'''),
            E('04_Klage.eml', 'Klage eingereicht – Nutzungsänderung Haselkornbogen', '2026-06-17T14:35:00+02:00', 'Rechtsanwältin Anja Weller <anja@weller-kanzlei.example>', 'Tola Adebayo <tola@adebayo-planung.example>', '''Sehr geehrte Frau Adebayo,

ich bestätige Ihnen, dass ich heute die Verpflichtungsklage gegen die Stadt wegen des Bescheids vom 2. Juni elektronisch über mein besonderes Anwaltspostfach beim Bayerischen Verwaltungsgericht Würzburg eingereicht habe. Das Übermittlungsprotokoll weist den Eingang um 14:08 Uhr aus. Ein gerichtliches Aktenzeichen ist mir noch nicht mitgeteilt worden. Der Klageantrag richtet sich auf Aufhebung der Versagung und Erteilung der beantragten Genehmigung, hilfsweise auf erneute Entscheidung. Ich habe die Behörde zugleich um sofortige Überprüfung der offensichtlich unzutreffenden Betriebsannahmen gebeten.

Ich habe in der Klage Ihre Betriebsbeschreibung vom 14. April mit dem Bescheid verglichen. Ihr Antrag beschreibt ausschließlich ein Büro mit zwei Arbeitsplätzen. Der Bescheid setzt dagegen einen Maschinen- und Lieferbetrieb voraus. Zur weiteren Bearbeitung habe ich die unveränderte Betriebsbeschreibung erneut übermittelt. Eine neue oder erweiterte Nutzung haben wir nicht beantragt.

Einen gerichtlichen Eilantrag habe ich heute nicht gestellt. Im Telefonat kündigte die Bauaufsicht an, die Zuordnung der Unterlagen bis Ende der folgenden Woche zu prüfen. Ich werde nachfassen, wenn die Abhilfe ausbleibt. Das Mietverhältnis und mögliche Folgekosten bleiben hiervon unberührt.

Mit freundlichen Grüßen
Anja Weller, Rechtsanwältin'''),
            D('05_Bearbeitungsvermerk.docx', 'Zuordnung der Betriebsbeschreibung und weiterer Ablauf', '28.07.2026', 'Stadt Würzburg · Bauaufsicht · Sachbearbeiterin Yasemin Kraus', '''## 1 Feststellungen zur Akte

Die am 14. April eingegangene Betriebsbeschreibung betrifft ein Büro mit zwei Arbeitsplätzen. Sie ist dem richtigen Grundstück zugeordnet. Bei der Vorbereitung des Bescheids wurde daneben ein Textbaustein aus einer anderen Nutzungsprüfung geöffnet. Die dort genannten Maschinen und regelmäßigen Lieferungen wurden in die Begründung übernommen. Für das Vorhaben von Frau Adebayo enthalten die eingereichten Unterlagen diese Angaben nicht. Der Dateiname „Werkraum“ war Anlass für die Zuordnung, ohne den Inhalt der Betriebsbeschreibung erneut zu lesen.

## 2 Bearbeitungsstände

Am 12. Mai hatte ich den Vorgang intern als entscheidungsreif bezeichnet. Die Kontrolle der zeichnungsbefugten Person war noch offen. Am 19. Mai lag der unzutreffende Entwurf zur Unterschrift vor. Nach der Klage und dem Hinweis der Rechtsanwältin überprüften wir am 23. Juni die Betriebsbeschreibung. Die angekündigte Rückmeldung an Frau Weller erfolgte an diesem Tag nicht. Sie erinnerte telefonisch am 30. Juni und schriftlich am 7. Juli.

Die abschließende erneute Ortsprüfung fand erst am 21. Juli statt. Sie ergab gegenüber dem ursprünglichen Antrag keine neue tatsächliche Anforderung. Am 28. Juli stellte ich den Genehmigungsentwurf fertig. Die Zeichnung ist für den 3. August vorgesehen. Welche Bearbeitungszeit die abschließende Kontrolle bei richtiger Erstzuordnung im Mai tatsächlich beansprucht hätte, lässt sich aus dem Terminkalender nicht sicher rekonstruieren.

Yasemin Kraus'''),
            D('06_Abhilfe_Genehmigung.docx', 'Aufhebung der Versagung und Baugenehmigung', '03.08.2026', 'Stadt Würzburg · Bauaufsicht · Wolfram Reuther', '''Sehr geehrte Frau Adebayo,

## 1 Entscheidung

Der Bescheid vom 2. Juni 2026 wird aufgehoben. Die mit Antrag vom 14. April 2026 beantragte Nutzungsänderung des Lagerraums am Haselkornbogen 5 in ein Planungsbüro mit zwei Arbeitsplätzen einschließlich der beantragten Öffnung in der tragenden Innenwand wird nach Maßgabe der unveränderten Antragsunterlagen genehmigt. Die Entscheidung bezieht sich auf den beschriebenen Bürobetrieb ohne Werkstatt, Produktion oder Warenverkauf. Eine andere Betriebsart wird hiermit nicht zugelassen.

## 2 Gründe

Bei der erneuten Prüfung wurde festgestellt, dass die Versagung von Betriebsabläufen ausging, die Sie nicht beantragt hatten. Maßgeblich ist die ursprüngliche Betriebsbeschreibung. Das dort beschriebene Planungsbüro fügt sich nach den festgestellten Verhältnissen in die nähere Umgebung ein. Die im Verfahren zu prüfenden öffentlich-rechtlichen Anforderungen stehen der beantragten Nutzung nicht entgegen. Geänderte Bauvorlagen oder eine Änderung des Nutzungsumfangs waren für diese Entscheidung nicht erforderlich.

## 3 Weiteres Verfahren

Ihre bevollmächtigte Rechtsanwältin erhält eine Ausfertigung. Das Verwaltungsgericht wird über die Aufhebung der Versagung und die erteilte Genehmigung unterrichtet. Über die prozessualen Erklärungen und die Kosten des gerichtlichen Verfahrens ist dort gesondert zu befinden. Mit dieser Genehmigung wird keine Entscheidung über einen zivilrechtlichen Zahlungsanspruch getroffen.

Wolfram Reuther, für die Bauaufsicht

Empfang durch die bevollmächtigte Rechtsanwältin am 4. August 2026 bestätigt.'''),
            D('07_Mietvertrag.docx', 'Mietvertrag über einen Büroraum', '07.04.2026', 'Vermieter Alfons Späth und Mieterin Tola Adebayo', '''## 1 Mietgegenstand und Beginn

Alfons Späth vermietet Tola Adebayo den Erdgeschossraum mit 42 Quadratmetern am Haselkornbogen 5 in Würzburg zur Nutzung als Planungsbüro. Das Mietverhältnis beginnt am 1. Juni 2026. Die monatliche Nettokaltmiete beträgt 420,00 EUR. Der Vermieter optiert für diese Vermietung nicht zur Umsatzsteuer. Vorauszahlungen auf Betriebskosten werden während der ersten beiden Monate nicht erhoben; nach tatsächlicher Nutzung wird eine gesonderte Vereinbarung getroffen.

## 2 Genehmigung und Ausbau

Die Mieterin beantragt die für die Nutzungsänderung erforderliche Genehmigung und trägt die Kosten der vereinbarten Öffnung in der tragenden Innenwand sowie der elektrischen Arbeitsplatzausstattung und der Heizkörper. Der Vermieter gestattet diese Arbeiten nach Vorlage der Genehmigung. Der feste Mietbeginn bleibt auch bei späterer Genehmigung bestehen. Eine Zusage zum Zeitpunkt oder Erfolg des Verwaltungsverfahrens gibt der Vermieter nicht ab. Der Vermieter übergibt die Schlüssel zum Mietbeginn; eine vorzeitige Nutzung als Büro ohne die erforderliche Genehmigung ist nicht vereinbart.

## 3 Laufzeit

Das Mietverhältnis läuft zunächst zwölf Monate. Die Parteien haben kein besonderes Kündigungsrecht wegen verzögerter Genehmigung vereinbart. Am 7. April unterzeichnen beide Parteien diesen Vertrag. Frau Adebayo teilt mit, die Entscheidung bis Mitte Mai anzustreben. Herr Späth weist darauf hin, dass er nach Vertragsabschluss für den Zeitraum ab Juni keine andere Vermietung suchen werde.

Alfons Späth · Tola Adebayo'''),
            D('08_Bankabrechnung.docx', 'Bereitstellungszinsen für Ausbaukredit', '05.08.2026', 'Genossenschaftliche Musterbank Mainlaub eG · Kundenbetreuung Beate Heckenast', '''Kundin: Tola Adebayo. Zweck des vereinbarten Kredits ist die Finanzierung der Wandöffnung und der technischen Ausstattung des geplanten Büros am Haselkornbogen 5. Der Kreditrahmen beträgt 8.000,00 EUR. Nach der am 20. April geschlossenen Vereinbarung kann die Auszahlung nach Vorlage der Genehmigung und der Handwerkerrechnungen erfolgen. Die Auszahlung war von der Kundin ursprünglich für Anfang Juni angekündigt.

Ab 1. Juni fallen auf den noch nicht abgerufenen Betrag monatlich 0,25 Prozent Bereitstellungszinsen an. Für Juni werden deshalb 20,00 EUR und für Juli weitere 20,00 EUR berechnet, zusammen 40,00 EUR. Während dieser Zeit wurde kein Teilbetrag ausgezahlt. Die Abrechnung wird am 5. August dem Geschäftskonto belastet. Tilgung und reguläre Kreditzinsen sind in diesem Betrag nicht enthalten.

Die Kundin bat am 26. Juni wegen der fehlenden Genehmigung um Aussetzung der Bereitstellungszinsen. Die Bank hielt mit Antwort vom 30. Juni an der vereinbarten Berechnung fest. Eine Umstellung auf einen anderen Kredit oder eine vorzeitige Auszahlung wurde nicht vereinbart. Die Genehmigung wurde der Bank am 4. August vorgelegt; Handwerkerrechnungen lagen zu diesem Zeitpunkt noch nicht vor.

Beate Heckenast'''),
            D('09_Zahlungsnachweis.docx', 'Zahlungen und Nutzung des Raums', '28.09.2026', 'Tola Adebayo · Planungsbüro · Haselkornbogen 5, Würzburg', '''## 1 Zahlungen

Meine Geschäftskontoauszüge weisen am 1. Juni und am 1. Juli jeweils eine Überweisung von 420,00 EUR an Alfons Späth mit dem Verwendungszweck „Miete Haselkornbogen“ aus. Der Vermieter bestätigt unter diesem Blatt den Eingang beider Zahlungen, insgesamt 840,00 EUR. Die Bank belastete am 5. August zusätzlich 40,00 EUR Bereitstellungszinsen nach der beigefügten Abrechnung. Erstattungen auf diese Beträge habe ich nicht erhalten.

## 2 tatsächliche Nutzung

Die Schlüssel bekam ich am 1. Juni. Ein alter Schreibtisch und drei Kartons standen ab Mitte Juni in dem Raum. Gearbeitet haben meine Zeichnerin und ich in dieser Zeit weiterhin an unseren bisherigen Arbeitsplätzen zuhause. Kunden empfing ich dort nicht. Ein zusätzlicher Ersatzraum wurde nicht gemietet. Nach Zugang der Genehmigung beauftragte ich die vereinbarten Innenarbeiten; sie dauerten vom 6. bis 14. August. Den Bürobetrieb nahmen wir am 17. August auf. Bei einer Genehmigung im Mai hätten die Handwerker nach damaliger mündlicher Auskunft Ende Mai Zeit gehabt. Eine schriftliche Terminreservierung gibt es nicht.

Tola Adebayo

Bestätigung vom 29. September: Die genannten Mietzahlungen von zusammen 840,00 EUR sind eingegangen und wurden nicht zurückgezahlt. Alfons Späth.'''),
            E('10_Forderung.eml', 'Adebayo gegen Stadt – Miet- und Finanzierungskosten', '2026-09-30T14:10:00+02:00', 'Rechtsanwältin Anja Weller <anja@weller-kanzlei.example>', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', '''Sehr geehrte Frau Holler,

für Frau Tola Adebayo mache ich 840,00 EUR Mietaufwand für Juni und Juli sowie 40,00 EUR Bereitstellungszinsen geltend, insgesamt 880,00 EUR. Beigefügt sind der Mietvertrag, die Bankabrechnung und die Bestätigung zu Zahlungen und Nutzung. Die Miete wurde ohne Umsatzsteuer vereinbart; die Bankposition enthält keine Umsatzsteuer. Entgangenen Gewinn machen wir nicht geltend. Die Kosten des Verwaltungsgerichtsverfahrens verfolgen wir im dortigen Kostenverfahren und rechnen sie hier nicht erneut ab.

Die Versagung beruhte auf einem Betrieb, den meine Mandantin nie beantragt hatte. Bei zutreffender Prüfung hätte sie aus unserer Sicht noch im Mai eine Entscheidung erhalten und ab Juni das Büro nutzen können. Bitte teilen Sie mit, ob Sie dem aus tatsächlichen Gründen widersprechen. Meine Mandantin hatte einen festen Mietbeginn und keine kostenfreie Lösungsmöglichkeit gegenüber dem Vermieter. Eine entsprechende Bitte um Entgegenkommen vom 10. Juni lehnte dieser telefonisch ab.

Wir haben die Versagung innerhalb der Klagefrist angegriffen und mehrfach um Abhilfe gebeten. Nach der Genehmigung haben wir die Hauptsache für erledigt erklärt; eine gerichtliche Kostenentscheidung liegt mir für diese Forderung noch nicht vor. Bitte nehmen Sie zu dem Zahlungsanspruch bis 12. Oktober Stellung.

Mit freundlichen Grüßen
Anja Weller, Rechtsanwältin'''),
        ],
    ),
    dict(
        slug='akha-wuerzburg-abwasseranlage',
        title='Würzburg: Der Bagger trifft den städtischen Kanal',
        summary='Bei einer Glasfaserbaustelle wird ein öffentlicher Kanal beschädigt. Die Stadt verlangt Reparatur- und Einsatzkosten; Lageangaben, eigene Stunden und die steuerliche Behandlung müssen auseinandergehalten werden.',
        core=['01_Pruefauftrag.eml', '02_Schadenbericht.docx', '03_Leitungsauskunft.docx', '04_Baggerfuehrer.eml', '05_Reparaturrechnung.docx', '09_Unternehmerantwort.eml'],
        xlsx=[],
        attachments={'09_Unternehmerantwort.eml': ['04_Baggerfuehrer.eml']},
        documents=[
            E('01_Pruefauftrag.eml', 'Beschädigung unseres Abwasserkanals – Forderungsentwurf', '2026-10-05T09:30:00+02:00', 'Gertraud Holler <recht@wuerzburg-fallakten.example>', 'Rechtsanwältin Clara Klee <clara@klee-kolben.example>', '''Sehr geehrte Frau Klee,

die Stadt Würzburg beauftragt Sie als Eigentümerin und Betreiberin des öffentlichen Abwasserkanals am Schlehenfächerweg mit der Prüfung ihrer Ersatzansprüche gegen die Grab & Grund Tiefbau GmbH. Der Kanal wird durch einen unselbstständigen städtischen Regiebetrieb geführt. Dieser besitzt keine eigene Rechtspersönlichkeit. Geschädigt ist hier unsere Anlage; es geht nicht um Ansprüche eines Anliegers wegen austretenden Abwassers.

Bitte erstellen Sie einen ausformulierten internen Prüfvermerk zu Anspruchsgegnern, Haftungsgrund und ersatzfähigen Positionen sowie einen vollständigen Forderungsentwurf an die Tiefbaufirma. Die Firma bestreitet die Genauigkeit unserer Leitungsauskunft. Außerdem ist die interne Stundenaufstellung bisher nicht deckungsgleich mit dem Einsatzblatt. Wir benötigen das Ergebnis bis 8. Oktober. Ein Klageauftrag ist damit nicht verbunden.

Der Tiefbauer war von der Faserfink Netz GmbH beauftragt, nicht von uns. Ein privater Bauvertrag zwischen der Stadt und Grab & Grund liegt nicht vor. Unsere Aufgrabungsfreigabe regelte nur die Nutzung der Straßenfläche. Unterlagen über dessen Haftpflichtversicherung oder unsere eigene Deckung sind bislang nicht vorhanden. Bitte keine Versicherer anschreiben, nichts versenden und keine abschließende Forderung ohne unsere Prüfung erklären.

Mit freundlichen Grüßen
Gertraud Holler'''),
            D('02_Schadenbericht.docx', 'Kanalschaden Schlehenfächerweg', '08.09.2026', 'Stadt Würzburg · Regiebetrieb Abwasser · Werkmeister Lorenz Dörflein', '''## 1 Anlage und Beteiligte

Am 7. September 2026 um 10:18 Uhr meldete die Grab & Grund Tiefbau GmbH einen beschädigten Kanal am Schlehenfächerweg vor Haus 9. Die Firma verlegte im Auftrag der Faserfink Netz GmbH eine Glasfasertrasse. Der öffentliche Mischwasserkanal DN 200 steht nach Anlagenverzeichnis seit seiner Herstellung im Eigentum der Stadt. Kontrolle, Reinigung und Reparatur erfolgen durch unseren Regiebetrieb. Es handelt sich um die öffentliche Hauptleitung im Straßenraum, nicht um einen privaten Hausanschluss. Eine Übertragung an eine Gesellschaft ist für diese Anlage nicht erfolgt.

## 2 Befund

Bei unserem Eintreffen um 10:36 Uhr lag der Kanal auf etwa einem Meter frei. Am Scheitel fehlte ein Stück Steinzeugrohr; daneben lagen frische Bruchstücke. Der Bagger stand unmittelbar an der Grube. Nach Angaben des Baggerführers war der Schaden bei einem Aushubhub entstanden. Ein vollständiger Rückstau in angeschlossene Gebäude wurde nicht festgestellt. Um die Leitung bis zum Austausch funktionsfähig zu halten, ließen wir ab 11:05 Uhr eine mobile Überleitung einrichten.

## 3 Wiederherstellung

Der beschädigte Abschnitt wurde am Folgetag durch eine beauftragte Kanalbaufirma ersetzt. Die Kameraprüfung ergab keine weitere sichtbare Beschädigung unmittelbar neben der ausgetauschten Stelle. Unsere Messung der offenliegenden Achse ergab gegenüber der in der Auskunft eingezeichneten Achse eine seitliche Abweichung von etwa 0,65 Meter. Bezug war die Mauerecke an Haus 9. Die Maßbandmessung wurde von mir und Milan Petrovic durchgeführt; ein vermessungstechnisches Aufmaß vor dem Schaden liegt uns nicht vor.

Lorenz Dörflein'''),
            D('03_Leitungsauskunft.docx', 'Leitungsauskunft und Arbeitsvorgaben', '28.08.2026', 'Stadt Würzburg · Regiebetrieb Abwasser · Leitungsauskunft Hanne Pflaum', '''Adressatin: Grab & Grund Tiefbau GmbH, Bauleitung Ida Sauer. Maßnahme: Glasfasertrasse Schlehenfächerweg vor den Häusern 7 bis 11. Diese Auskunft enthält die für den betroffenen Abschnitt aus unserem Bestandsplan übernommene Lagebeschreibung.

## 1 Bestandsangaben

Die öffentliche Leitung DN 200 verläuft annähernd parallel zur nördlichen Straßenkante. Vor Haus 9 liegt die eingetragene Achse 2,10 Meter südlich der dortigen Mauerecke. Die eingetragene Überdeckung beträgt ungefähr 1,20 Meter. Diese Maße stammen aus der Bestandsaufnahme von 1988. Spätere Veränderungen der Bezugspunkte sind nicht nachgemessen. Die tatsächliche Lage und Tiefe sind vor einem maschinellen Aushub durch geeignete Suchschlitze festzustellen; die Planangabe ersetzt diese Feststellung nicht.

## 2 Arbeiten im Leitungsbereich

Innerhalb eines Meters beiderseits der eingetragenen Achse ist zunächst von Hand freizulegen. Bei Abweichungen oder ungeklärter Lage sind die Arbeiten in diesem Bereich zu unterbrechen und der Regiebetrieb zu verständigen. Nach Freilegung ist ein ausreichender Abstand zum tatsächlichen Leitungsverlauf einzuhalten. Diese Hinweise betreffen den Schutz unseres Kanals; sie sind keine Ausführungsplanung für die neue Glasfasertrasse.

## 3 Empfang

Ida Sauer bestätigt für Grab & Grund den Empfang am 28. August um 15:20 Uhr und die Weitergabe an den Polier. Eine Einweisung vor Ort wurde von der Firma nicht angefordert. Die straßenrechtliche Aufgrabungsfreigabe wird gesondert durch die Straßenstelle bearbeitet. Ein Auftrag der Stadt an die Firma wird mit dieser Leitungsauskunft nicht erteilt.

Hanne Pflaum'''),
            E('04_Baggerfuehrer.eml', 'Mein Ablauf am Schlehenfächerweg', '2026-09-09T17:15:00+02:00', 'Nico Yilmaz <nico@grab-grund.example>', 'Ida Sauer <ida@grab-grund.example>', '''Hallo Frau Sauer,

am Montag hatten wir vor Haus 9 zunächst ungefähr auf der im Ausdruck eingezeichneten Achse von Hand gesucht. Wir waren vielleicht 70 oder 80 Zentimeter tief. Dort fanden wir noch kein Rohr. Der Polier sagte, die neue Trasse liege weiter südlich, und ich könne dort vorsichtig mit der schmalen Schaufel weiterarbeiten. Ich habe dann etwa 60 Zentimeter seitlich von unserem Suchschlitz angesetzt. Beim nächsten tieferen Hub gab es ein knackendes Geräusch. Danach sahen wir das gebrochene Rohr.

Den Abstand von einem Meter habe ich vor dem Hub nicht mit dem Band gemessen. Die Leitungsauskunft hatte ich als Ausdruck in der Kabine, aber die Rückseite mit den Arbeitshinweisen lag unter den übrigen Plänen. Ich bin seit Februar fest bei Grab & Grund angestellt und habe auf dieser Baustelle nach Einteilung unseres Poliers gearbeitet. Für die Stadt habe ich keinen eigenen Auftrag ausgeführt.

Der Kanal lag nach meinem Eindruck deutlich anders, als wir ihn anhand der Zeichnung gesucht hatten. Ob die Mauer als Bezugspunkt an der richtigen Ecke gemessen wurde, weiß ich nicht. Wir riefen sofort beim Regiebetrieb an und sicherten die Grube. Fotos vor dem ersten Aushub haben wir nicht gemacht.

Viele Grüße
Nico'''),
            D('05_Reparaturrechnung.docx', 'Rechnung KR-260910 – Kanalreparatur', '10.09.2026', 'Kanalbau Irmgard Behrlein GmbH · Rosenkieselweg 6, Würzburg', '''Rechnungsempfängerin: Stadt Würzburg, Regiebetrieb Abwasser. Auftrag vom 7. September 2026 zur Wiederherstellung des am Schlehenfächerweg vor Haus 9 beschädigten öffentlichen Kanals. Die Arbeiten wurden am 8. September ausgeführt und durch Werkmeister Dörflein abgenommen.

Für Freilegung, Ausbau des beschädigten Stücks und Einbau des Ersatzstücks berechnen wir 1.400,00 EUR netto. Das Ersatzrohr mit zwei Anschlussmanschetten und Bettungsmaterial kostet 460,00 EUR netto. Für die Kamerakontrolle nach Einbau werden 250,00 EUR netto berechnet. Verfüllung und Wiederherstellung der zuvor vorhandenen Straßenoberfläche kosten 650,00 EUR netto. Daraus ergibt sich ein Nettobetrag von 2.760,00 EUR. Die Umsatzsteuer von 19 Prozent beträgt 524,40 EUR; der Rechnungsbetrag beläuft sich auf 3.284,40 EUR.

Die Reparatur beschränkt sich auf den beschädigten Abschnitt und die technisch erforderlichen Anschlüsse. Eine Vergrößerung des Querschnitts oder Sanierung weiterer Leitungslängen ist nicht beauftragt und nicht berechnet. Die mobile Überleitung ist nicht Bestandteil dieser Rechnung; sie wurde durch einen anderen Betrieb gestellt. Zahlungsziel ist der 24. September 2026.

Irmgard Behrlein'''),
            D('06_Ueberleitung_Rechnung.docx', 'Rechnung UP-260909 – vorübergehende Überleitung', '09.09.2026', 'Pumpendienst Anwar Malik · Weidenkernweg 3, Würzburg', '''Rechnungsempfängerin: Stadt Würzburg, Regiebetrieb Abwasser. Einsatzort: öffentlicher Kanal Schlehenfächerweg vor Haus 9. Auftrag telefonisch erteilt durch Lorenz Dörflein am 7. September um 10:42 Uhr.

Die mobile Überleitung wurde am 7. September um 11:05 Uhr eingerichtet und bis zum Abschluss der Rohrreparatur am 8. September um 14:15 Uhr betrieben. Der Preis für An- und Abfahrt, Aufbau und Abbau beträgt zusammen 280,00 EUR netto. Die Bereitstellung der Pumpe, Schläuche und Stromversorgung für den Einsatzzeitraum kostet 420,00 EUR netto. Für zwei Funktionskontrollen werden zusammen 100,00 EUR netto berechnet. Der Nettobetrag beträgt 800,00 EUR. Hinzu kommen 152,00 EUR Umsatzsteuer bei 19 Prozent; insgesamt sind 952,00 EUR zu zahlen.

Während des Einsatzes wurde der Zufluss am beschädigten Stück vorbeigeleitet. Unsere Kontrolle ergab keine Unterbrechung des Pumpbetriebs. Eine Reinigung anderer Straßenabschnitte oder Arbeiten in privaten Gebäuden waren nicht erforderlich und sind nicht abgerechnet. Zahlungsziel ist der 23. September 2026.

Anwar Malik'''),
            D('07_Kassenvermerk.docx', 'Zahlungen und steuerliche Zuordnung der Kanalreparatur', '28.09.2026', 'Stadt Würzburg · Kasse und Steuerstelle · Mirjam Ben Ami', '''## 1 Zahlungen

Die Rechnung der Kanalbau Irmgard Behrlein GmbH vom 10. September über 3.284,40 EUR wurde am 22. September vollständig bezahlt. Die Rechnung des Pumpendienstes Anwar Malik vom 9. September über 952,00 EUR wurde am 21. September vollständig bezahlt. Skonto wurde nicht vereinbart und nicht abgezogen. Für die beiden Fremdrechnungen sind damit 4.236,40 EUR abgeflossen. Eine Erstattung durch Dritte oder einen Versicherer ist auf dem Sachkonto bisher nicht gebucht.

## 2 Steuerliche Behandlung

Nach der für diesen Regiebetrieb geführten steuerlichen Zuordnung betrifft der reparierte Kanal ausschließlich die hoheitliche öffentliche Abwasserbeseitigung. Die beiden Rechnungen sind dieser Tätigkeit vollständig zugeordnet. Für ihre Umsatzsteuerbeträge von zusammen 676,40 EUR wird keine Vorsteuer abgezogen; es gibt in diesem Vorgang keine Zuordnung zu einer steuerpflichtigen Nebenleistung. Diese Aussage betrifft die konkrete Buchung und ist keine Aussage über sämtliche Tätigkeiten der Stadt.

## 3 Eigene Leistungen

Die Personalstunden des Regiebetriebs sind noch nicht als Erstattungsforderung gebucht. Die Werkleitung hat einen Betrag von 336,00 EUR angemeldet. Ob dieser Betrag zusätzlichen Aufwand oder eine interne Verrechnung ohnehin anfallender Personalentgelte enthält, ist aus der Kostenanforderung noch nicht ersichtlich. Eine Zahlung auf eine eigene Rechnung liegt dafür naturgemäß nicht vor.

Mirjam Ben Ami'''),
            D('08_Eigene_Stunden.docx', 'Einsatzstunden Regiebetrieb und Kostenanforderung', '29.09.2026', 'Stadt Würzburg · Regiebetrieb Abwasser · Lorenz Dörflein', '''## 1 Einsatzblatt

Am 7. September war ich von 10:25 bis 12:25 Uhr mit Fahrt, Schadensaufnahme und Beauftragung der Überleitung beschäftigt, insgesamt zwei Stunden. Milan Petrovic war von 10:30 bis 13:00 Uhr vor Ort, insgesamt zweieinhalb Stunden. Am 8. September war ich von 13:30 bis 14:30 Uhr zur Abnahme dort; Herr Petrovic kontrollierte anschließend von 14:30 bis 15:30 Uhr den freien Ablauf. Die auf diesem Blatt eingetragenen Zeiten ergeben insgesamt sechseinhalb Stunden. Alle Zeiten lagen innerhalb der regulären Arbeitszeit; Überstundenzuschläge wurden nicht gezahlt.

## 2 Kostenanforderung

Unsere zunächst an die Kasse geschickte Anforderung lautet auf acht Stunden zu je 42,00 EUR, insgesamt 336,00 EUR. Darin hatte ich zusätzlich anderthalb Stunden für Telefonate, Bestellung und Nachbereitung geschätzt. Für diese anderthalb Stunden habe ich bisher keine Einzelaufzeichnung gefunden. Der Satz von 42,00 EUR ist unser interner durchschnittlicher Verrechnungssatz mit Personalneben- und Gemeinkosten, kein an einen Dritten bezahlter Stundensatz.

Die am 7. September geplante Kontrolle eines anderen Kanalschachts wurde auf den nächsten Tag verschoben und ohne Mehrarbeit nachgeholt. Ob uns durch die Verschiebung ein weiterer messbarer Aufwand entstand, kann ich nicht belegen. Die vorgenannten Stunden betreffen keine Leistungen, die zugleich auf den Fremdrechnungen stehen.

Lorenz Dörflein'''),
            E('09_Unternehmerantwort.eml', 'Kanalschaden Schlehenfächerweg – Ihre Kostenankündigung', '2026-10-01T11:20:00+02:00', 'Ida Sauer <ida@grab-grund.example>', 'Lorenz Dörflein <abwasser@wuerzburg-fallakten.example>', '''Sehr geehrter Herr Dörflein,

wir bestreiten nicht, dass unsere Baggerschaufel das Rohr getroffen hat. Zur Ursache übersende ich die Nachricht unseres Fahrers. Nach unserer Auffassung war die Auskunft zur Lage zu ungenau. Unser Polier hatte einen Suchschlitz an der eingezeichneten Stelle herstellen lassen und dort kein Rohr gefunden. Dass der Kanal rund 65 Zentimeter daneben lag, konnte er nicht sehen. Wir möchten das genaue Aufmaß und die Grundlage der von Ihnen genannten Achse erhalten.

Auftraggeber unserer Glasfaserarbeiten ist allein die Faserfink Netz GmbH. Eine vertragliche Zahlungspflicht gegenüber der Stadt haben wir nicht vereinbart. Das bedeutet nicht, dass wir den Schaden ignorieren; wir wollen die Verantwortlichkeit und die angekündigten Kosten nachvollziehen. Die aus Ihrer telefonischen Mitteilung ersichtlichen Fremdkosten von 4.236,40 EUR erscheinen uns prüfbar, liegen uns aber noch nicht vollständig als Rechnungen vor. Eigene Stadtstunden von 336,00 EUR erkennen wir ohne Aufschlüsselung nicht an.

Eine Erklärung zu einer Versicherung oder eine Zahlungszusage gebe ich mit dieser Nachricht nicht ab. Bitte senden Sie die belegte Forderung zunächst an unsere Geschäftsadresse. Wir antworten nach Durchsicht der Unterlagen.

Mit freundlichen Grüßen
Ida Sauer, Geschäftsführerin'''),
        ],
    ),
]
