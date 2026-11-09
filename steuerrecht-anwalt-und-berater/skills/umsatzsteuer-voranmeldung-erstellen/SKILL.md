---
name: umsatzsteuer-voranmeldung-erstellen
description: "Erstellt eine Umsatzsteuer-Voranmeldung aus Rechnungen, Gutschriften, Bankdaten und Buchungen. Prüft Zeitraum, Soll- oder Istbesteuerung, Steuerbefreiungen, Vorsteuer, Auslandsfälle und Berichtigungen und liefert eine belegte ELSTER-Erfassungstabelle. Bereitet verifizierten XML-Import oder die beauftragte lokale Übermittlung mit Prüfung und Eingangsprotokoll vor."
---

# Umsatzsteuer-Voranmeldung aus Belegen erstellen

## 1 Zweck und Anwendungsfall

Erstellen Sie die konkrete Umsatzsteuer-Voranmeldung einschließlich der nachvollziehbaren Rechnung und der zugehörigen Belegzuordnung. Arbeiten Sie vom vorhandenen Belegbestand bis zu einem nutzbaren Datensatz weiter. Ein klarer Auftrag kann eine Erfassungstabelle, einen Import oder eine elektronische Abgabe umfassen.

Die Steueranmeldung wirkt nach § 168 AO grundsätzlich als Steuerfestsetzung unter Vorbehalt der Nachprüfung. Bei Herabsetzung oder Vergütung ist die Zustimmung der Finanzbehörde zu beachten. Eine Übertragung ist deshalb eine steuerlich wirksame Erklärung. Prüfen Sie vor ihr den tatsächlichen Inhalt. Bei Eingangsrechnungen beachten Sie den zeitlichen Vorsteuerabzug. Nach BFH, Urteil vom 25. Juni 2025, XI R 17/22, Leitsatz 2 und Rn. 24, wirkt ein erstmaliger Umsatzsteuerausweis in einer berichtigten Rechnung nicht zurück. [§ 168 AO](https://www.gesetze-im-internet.de/ao_1977/__168.html) · [Amtliche Entscheidung](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202520301/)

## 2 Eingaben und erster Arbeitsstand

Lesen Sie die für den Auftrag erheblichen Rechnungen, Gutschriften, Kassen- und Bankdaten, Buchungsjournale, vorherigen Anmeldungen und steuerlichen Stammdaten. Erfassen Sie zuerst, was daraus bereits feststeht. Bei einem klaren Auftrag beginnen Sie mit dem Entwurf. Bei Dateien ohne Auftrag klären Sie den gewünschten Zeitraum und das Arbeitsprodukt. Bei leerem Start fragen Sie nach Unternehmer, Zeitraum und Belegordner.

Fordern Sie nur entscheidende fehlende Angaben nach. Die nächste Frage kann eine Genehmigung zur Istbesteuerung, das Eingangsdatum einer Rechnung, eine offene Zahlung, eine Nutzung oder den Zugang zu einer verwendeten Buchhaltungssoftware betreffen. Führen Sie währenddessen die unabhängigen Teile fort. Arbeiten Sie Antworten und spätere Belege in denselben Entwurf ein und halten Sie die betroffenen Änderungen fest.

Vergewissern Sie sich, ob die Vorlage eine Umsatzsteuer-Voranmeldung oder eine Jahreserklärung ist. Ein Beispiel des Jahresformulars USt 2 A liefert keine ungeprüfte Kennziffernzuordnung für eine Voranmeldung. Identifizieren Sie Datenart, Jahr, Formularversion und den tatsächlich gemeinten Monat oder das Quartal.

## 3 Ablauf

### 3.1 Unternehmer und Anmeldungsstand bestimmen

Stellen Sie Unternehmer, zuständiges Finanzamt, betriebliche Steuernummer, steuerlichen Registrierungstatbestand und Vertretung fest. Trennen Sie persönliche Steueridentifikationsnummer, USt-IdNr. und die für die Anmeldung maßgebliche Steuernummer. Nutzen Sie für eine Übermittlung ausschließlich die dokumentierte Konvertierung in das geforderte Steuernummernformat.

Mehrere trennbare Tätigkeiten derselben natürlichen Person können verschiedene ertragsteuerliche Ergebnisse haben. Prüfen Sie für die Umsatzsteuer den Umfang des einheitlichen Unternehmens. Eine Organschaft oder mehrere Rechtsträger erfordern dagegen eine eigene Zuordnung des Steuerschuldners. Verifizieren Sie eine Kleinunternehmerbefreiung, einen wirksamen Verzicht und besondere Erklärungspflichten, bevor Sie Regelbesteuerung voraussetzen.

Ermitteln Sie, ob es sich um die erstmalige Anmeldung, eine vollständige berichtigte Anmeldung oder einen Abgleich einer bereits erfolgten Festsetzung handelt. Erfassen Sie Übermittlungsprotokoll, bisherigen Inhalt und Zahlungen. Eine bloße Differenzrechnung ist noch kein vollständiger berichtigter Anmeldungsdatensatz.

### 3.2 Zeitraum und Frist belegen

Lesen Sie den Voranmeldungszeitraum aus den geltenden Regeln und den maßgeblichen Bescheiden. Prüfen Sie bei § 18 Abs. 2 UStG die Vorjahressteuer, bei Neugründung die zeitlich geltende Sonderregel, bei einem Wechsel die Geltung für das betreffende Jahr. Prüfen Sie Dauerfristverlängerung, Sondervorauszahlung und deren zulässige Anrechnung gesondert.

Berechnen Sie die tatsächliche Abgabe- und Zahlungsfrist einschließlich Wochenenden und Feiertagen. Unterscheiden Sie Leistungs-, Rechnungs-, Rechnungseingangs-, Zahlungs- und Berichtigungsdatum. Ziehen Sie bei einem Jahreswechsel die Nachlaufunterlagen heran. Eine EÜR-Jahreszuordnung ersetzt keine Prüfung des Umsatzsteuerzeitpunkts.

### 3.3 Originale und Buchungen abstimmen

Vergeben Sie eine stabile Beleg-ID. Ordnen Sie jeder erheblichen Position Dateipfad oder Dokument, Seite beziehungsweise XML-Feld, Aussteller, Empfänger, Rechnungsnummer und Betrag zu. Lesen Sie bei hybriden Rechnungen auch das eingebettete XML und vergleichen Sie es mit dem Sichtbild. Erfassen Sie Fassungen und Berichtigungen. Dieselbe Rechnung in PDF, XML, Versandmail und Bankbuchung ist ein Vorgang.

Gleichen Sie Teilzahlungen, Sammelzahlungen, Skonti, Stornos, Erstattungen, Aufrechnungen und Gebührenverrechnungen ab. Ein saldierter Zahlungseingang kann Erlös und gesonderte Kosten enthalten. Lassen Sie beide Rechenbestandteile sichtbar. Eine Bankbuchung allein belegt weder Steuersatz noch Vorsteuerabzug.

Führen Sie eine Belegmatrix mit mindestens diesen Feldern.

| Feld | Inhalt |
| --- | --- |
| Identität | Beleg-ID, Gegenpartei, Nummer und Fundstelle |
| Zeit | Leistung, Rechnung, Rechnungseingang und Zahlung |
| Rechnung | Netto, ausgewiesene Steuer, Brutto und Währung |
| Einordnung | Leistungsart, Ort, Steuerschuldner und Norm |
| Anmeldung | Zeitraum, Kennziffer, Bemessungsgrundlage und Steuer |
| Abzug | betriebliche Verwendung, Ausschluss und Vorsteueranteil |
| Prüfung | Gegenbeleg, offene Angabe und konkrete Folge |

### 3.4 Ausgangsumsätze zeitlich und materiell prüfen

Prüfen Sie Leistungsgegenstand, Leistungsort, Entgelt, Steuerbefreiung, Steuersatz und Steuerschuldner. Legen Sie die jeweilige rechtliche Voraussetzung dar. Prüfen Sie insbesondere, ob ein Unterrichts-, Heilbehandlungs- oder anderer Befreiungstatbestand tatsächlich belegt ist. Bei Autorenrechten, Verwertungsgesellschaften und Zuschüssen unterscheiden Sie entgeltliche Leistung und gesetzlichen Anspruch anhand der Abrechnung.

Bei Sollbesteuerung bestimmen Sie den Entstehungszeitpunkt nach § 13 UStG aus der ausgeführten Leistung oder Teilleistung. Bei einer gestatteten Istbesteuerung ordnen Sie das vereinnahmte Entgelt dem zutreffenden Zeitraum zu. Prüfen Sie den Geltungsbereich und Beginn der Gestattung nach § 20 UStG. Anzahlungen können bereits vor Ausführung der Leistung Steuer auslösen. Vermeiden Sie beim Wechsel der Besteuerungsart Doppel- und Nichterfassung.

Behandeln Sie Änderungen des Entgelts, Uneinbringlichkeit, Rückzahlungen und unentgeltliche Wertabgaben nach den jeweils einschlägigen Voraussetzungen. Ein fehlerhafter Steuerausweis nach § 14c UStG benötigt eine eigene Prüfung. Setzen Sie die im Text genannte Umsatzsteuer nicht automatisch als gesetzlich geschuldete Steuer an.

### 3.5 Vorsteuer bestimmen

Prüfen Sie nach § 15 UStG die Leistung für das Unternehmen, das Vorliegen der erforderlichen Rechnung, den gesetzlich geschuldeten Steuerbetrag und den maßgeblichen Zeitraum. Für Anzahlungen müssen die besonderen Voraussetzungen vorliegen. Die eigene Istbesteuerung begründet keine pauschale Zahlungsvoraussetzung für jede Eingangsrechnung. Bei Rechnungsberichtigungen prüfen Sie Berichtigungsfähigkeit und Rückwirkung anhand des ursprünglichen Dokuments.

Wenn Leistungszeitraum, Rechnungseingang und Erklärungsabgabe auseinanderfallen, dokumentieren Sie alle drei Daten. Das [EuG-Urteil vom 11.02.2026, T-689/24](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A62024TJ0689), behandelt eine nach Ablauf des Leistungszeitraums und vor Abgabe der Erklärung empfangene Rechnung. Der EuGH überprüft dieses Urteil in [C-167/26 RX](https://eur-lex.europa.eu/legal-content/DE/CASE/?uri=CELEX%3A62026CC0167). Die Schlussanträge vom 10.09.2026 sind ein Entscheidungsvorschlag. Prüfen Sie vor Abgabe den aktuellen Verfahrensstand und stellen Sie eine streitige frühere Zuordnung getrennt dar. Der [BFH-Beschluss vom 26.02.2026, V B 11/25, Rn. 2](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/), eröffnet mit [V R 7/26](https://www.bundesfinanzhof.de/de/anhaengige-verfahren/aktuelle-verfahren/detail/STAH260500007/) ein eigenes Revisionsverfahren zur späteren Berichtigung eines ursprünglich nicht berichtigungsfähigen Dokuments. Leiten Sie daraus keinen bestätigten Rückwirkungsanspruch ab.

Ordnen Sie Eingangsleistungen zunächst direkt zu. Unterscheiden Sie private Verwendung, unternehmerische Verwendung für steuerpflichtige Umsätze und Verwendung für Umsätze mit Ausschluss des Vorsteuerabzugs. Prüfen Sie Ausnahmen vom Ausschluss und sachgerechte Aufteilung nach § 15 Abs. 4 UStG. Trennen Sie die umsatzsteuerliche Zuordnung von einkommensteuerlichen Abzugsfragen. Prüfen Sie bei längerfristiger Verwendung einen möglichen Berichtigungstatbestand nach § 15a UStG.

Bei ausländischer Steuer, einer Rechnung mit falschem Steuerschuldner oder einer Kleinunternehmerrechnung übernehmen Sie keinen deutschen Vorsteuerbetrag aus einem bloßen Bruttodifferenzbetrag. Prüfen Sie Rechnungskorrektur, richtige Erfassung und gegebenenfalls einen anderen Erstattungsweg.

### 3.6 Auslands- und Sonderfälle abarbeiten

Prüfen Sie bei elektronischen Diensten, Software, Werbung, Waren und anderen Auslandsbezügen die tatsächliche Gegenpartei, ihren Sitz, den Leistungsort und die verwendete USt-IdNr. Prüfen Sie § 13b UStG, innergemeinschaftlichen Erwerb, Einfuhrumsatzsteuer, innergemeinschaftliche Lieferung und nicht im Inland steuerbare Leistungen einzeln. Berechnen Sie geschuldete Steuer und einen möglichen Vorsteuerabzug jeweils selbstständig. Ein möglicher gleicher Endsaldo beseitigt die Erklärungspflicht einzelner Felder nicht.

Ordnen Sie OSS-, Zusammenfassende-Meldungs- und andere Spezialverfahren richtig ab. Zeigen Sie, welche Beträge in die aktuelle UStVA gelangen und welche in einem anderen Verfahren zu erklären sind. Wenn die notwendigen Informationen fehlen, beschreiben Sie die entscheidende Frage und bearbeiten Sie den restlichen Datensatz weiter.

### 3.7 Kennziffern und Beträge herleiten

Verwenden Sie die amtliche Ausfüllhilfe und Felddefinition für das konkrete Jahr. Geben Sie Kennziffer und Feldbezeichnung zusammen an. Prüfen Sie Bemessungsgrundlagen, Steuerbeträge, Vorzeichen, zulässige Dezimalstellen und Voll-Euro-Regeln je Feld. Rechnen Sie intern mit Centgenauigkeit. Dokumentieren Sie erst danach die verlangte Rundung oder den Eintrag in volle Euro. Verwechseln Sie Bemessungsgrundlage und Steuerbetrag nicht.

Ermitteln Sie Ausgangssteuer, besondere Steuerbeträge, abziehbare Vorsteuer, Berichtigungen, eine gegebenenfalls anzurechnende Sondervorauszahlung und die Zahllast oder den Überschuss. Stimmen Sie die Feldsumme mit der Belegmatrix und dem bisherigen Anmeldungsstand ab. Bereits geleistete gewöhnliche Vorauszahlungen vermindern nicht ohne entsprechende Feldvorgabe die anzumeldende Periodensteuer. Zeigen Sie den verbleibenden Zahlungs- oder Erstattungsbetrag getrennt.

Prüfen Sie den Datensatz unter der stärksten plausiblen Gegenannahme, etwa ohne nachgewiesene Steuerbefreiung oder bei einem späteren Zahlungseingang. Bei einer entscheidenden offenen Rechtsfrage legen Sie die begründete Einordnung und den Freigabebedarf offen. Füllen Sie keine fehlenden Tatsachen durch erfundene Belege.

### 3.8 Geeigneten Abgabeweg anbieten

Fragen Sie bei noch offenem Format nach dem gewünschten Weg. Die fachliche Bearbeitung läuft unabhängig davon weiter. Formulieren Sie die Option für einen begleiteten lokalen Zugang beispielsweise so.

> Ich kann eine ELSTER-Erfassungstabelle erstellen, einen verifizierten XML-Import vorbereiten oder die Übermittlung in einer freigegebenen lokalen ELSTER-Umgebung begleiten. Welchen Weg möchten Sie nutzen? Bei Zertifikatsanmeldung wählen Sie die Zertifikatsdatei lokal aus und geben die zugehörige PIN beziehungsweise das Passwort selbst im geschützten Anmeldefeld ein. Für eine vorhandene lokale Anbindung genügt mir zunächst die Angabe des Programms und gegebenenfalls des Zertifikatspfads.

Berücksichtigen Sie eine bereits gewählte Zugangsart und bereits erteilte Berechtigung. Fordern Sie kein Zertifikat, Passwort oder PIN als Chatnachricht, Mailanlage oder Repository-Datei an. Halten Sie Geheimnisse auch aus Logs und Ausgabedateien heraus. Verwenden Sie nur die vom Nutzer freigegebene lokale Anbindung oder Anmeldung auf der verifizierten amtlichen Seite.

### 3.9 ELSTER-Erfassungstabelle liefern

Liefern Sie eine tatsächlich nutzbare XLSX- oder CSV-Datei, sofern Dateiausgabe möglich ist, und eine kurze Erfassungstabelle. Enthalten sein müssen Jahr, Datenart, Zeitraum, Finanzamt, benötigte Steuernummer, berichtigte Anmeldung, Kennziffer, amtliche Feldbezeichnung, Eintragswert, Maßeinheit und Belegfundstellen. Führen Sie manuell zu ergänzende Felder und die Prüfsumme der errechneten Zahllast gesondert auf.

Die Tabelle muss das Übertragen in das konkrete Jahresformular ermöglichen. Kennziffern und Werte dürfen nicht allein aus einer gleich aussehenden Vorjahresdatei stammen. Kennzeichnen Sie einen offenen Pflichtwert an genau der betroffenen Stelle. Beschreiben Sie den letzten fachlichen Bearbeitungsschritt bis zur Abgabereife.

### 3.10 XML-Import mit verifiziertem Schema vorbereiten

Mein ELSTER unterstützt den UStVA-Formulardatenimport. Prüfen Sie das Jahresschema. Der Portalimport erwartet den Nutzdatenblock `Anmeldungssteuern` und ISO-8859-15. Ein vollständiger ERiC-Übertragungsumschlag erfüllt diesen Importweg nicht. Beachten Sie die amtlich genannten ausgelassenen Felder. [Amtliche Importanleitung](https://www.elster.de/eportal/helpGlobal?themaGlobal=ustva_upload)

Verwenden Sie die tatsächlich verfügbare, vertrauenswürdige Jahresdokumentation mit XSD und Plausibilitätsregeln. Stimmen Sie Datenart, Namespace, Version, Zeichensatz, Reihenfolge und Zahlenformate ab. Prüfen Sie die Datei gegen dieses Schema und die Jahresregeln. Dokumentieren Sie Prüfergebnis und anschließend die übernommenen Werte im Formular. Das Importergebnis ist noch keine Abgabebestätigung. Ein aus Rechnungen ausgelesenes ZUGFeRD- oder XRechnung-XML ist eine andere Datenart.

Wenn eine benötigte Jahresdokumentation oder validierende Anbindung fehlt, liefern Sie die geprüfte Erfassungstabelle und benennen Sie präzise die noch benötigte Schnittstellenressource. Bezeichnen Sie eine selbst entworfene Datenstruktur nicht als ELSTER-Importdatei. Behaupten Sie keinen erfolgreichen Test, wenn nur syntaktisch wohlgeformtes XML vorliegt.

### 3.11 Lokale Übermittlung und Eingang nachweisen

Prüfen Sie für eine direkte Übertragung die freigegebene ERiC-fähige Steueranwendung, ihr Jahresmodul und ihre authentifizierte lokale Anbindung. ERiC plausibilisiert und übermittelt mit der Steueranwendung. Das Tool muss diese Funktion tatsächlich anbieten. Verwenden Sie Test- und Echtübermittlung in der dokumentierten Umgebung getrennt. [Amtliche Entwicklerbeschreibung](https://www.elster.de/elsterweb/infoseite/entwickler)

Zeigen Sie vor der Echtabgabe Unternehmer, Zeitraum, Berichtigungsstand und endgültigen Steuerbetrag in einer kompakten Übersicht. Prüfen Sie, ob der konkrete Abgabeauftrag und die Befugnis diesen Datensatz bereits decken. Ist das der Fall, verlangen Sie keine erneute allgemeine Zustimmung. Andernfalls holen Sie nach fertiger Berechnung die noch erforderliche konkrete Freigabe ein.

Nach dem Versand lesen Sie das Ergebnis und das Übermittlungsprotokoll. Speichern Sie Zeitpunkt, Transferticket oder andere Bestätigung, übermittelten Datensatz und Steuerberechnung in der Akte. Bei einem Abbruch klären Sie anhand der Rückmeldung, ob die Übertragung bereits angenommen wurde. Lösen Sie eine Wiederholung erst nach dieser Prüfung aus. Ein Formularimport, eine technische Validierung oder eine Ausgangsbestätigung belegt allein noch keinen erfolgreichen Eingang.

### 3.12 Änderungen und Fortsetzung behandeln

Tauchen neue Belege auf, aktualisieren Sie Belegmatrix, Feldzuordnung und Steuerbetrag. Stellen Sie eine berichtigte Anmeldung als vollständigen richtigen Datensatz für denselben Zeitraum her. Prüfen Sie die gesetzlichen Anzeigepflichten nach § 153 AO und trennen Sie sie von einem Einspruch gegen einen abweichenden Festsetzungsbescheid. Bei Bescheidzugang sichern Sie Bekanntgabe, Frist und Abweichungsvergleich und nutzen bei entsprechendem Auftrag den Einspruchsweg.

## 4 Quellenpflicht

Wenden Sie [Zitierweise und Quellenprüfung](../../references/zitierweise.md) an. Prüfen Sie für den Zeitraum insbesondere §§ 1 bis 4, 12 bis 15a, 17 bis 20 UStG, §§ 46 ff. UStDV sowie §§ 108, 150, 153, 164 und 168 AO. Belegen Sie umstrittene Einordnungen durch die einschlägige amtliche Quelle. Bei Befreiungen und ermäßigten Steuersätzen genügt eine ungesicherte Rechnungsbezeichnung nicht.

Die [Quellenkarte und technische Prüfung](../../ustva/quellen-und-uebermittlung.md) nennt die amtlichen Einstiege. Für technische Datenfelder gelten die Jahresdokumentation und die tatsächlich geprüfte Schnittstelle. Belegen Sie in der internen Akte Abrufdatum, Version, entscheidende Aussage und ihre Grenze.

## 5 Ausgabeformat

Das Ergebnis umfasst die fertige Erfassungstabelle oder den tatsächlich validierten Datensatz, eine belegbezogene Steuerberechnung, die noch entscheidenden Rückfragen und den zutreffenden Abgabestatus. Ein ausgearbeiteter Begleitvermerk erläutert die tragenden Zuordnungen und ihre Folgen in vollständigen Sätzen. Reine Stichworte und leere Gliederungen ersetzen das bestellte Endprodukt nicht.

Tabellen weisen Beträge in EUR mit der für das Feld verlangten Genauigkeit aus. Sie enthalten eindeutige Spalten, nachvollziehbare Summen und eine Belegverknüpfung. Formatierte Texte verwenden soweit technisch möglich Times New Roman 11 Punkt und dezimale Gliederung. Technische Hinweise bleiben außerhalb einer versandfähigen Mandanten- oder Behördennachricht.

Geben Sie den Status genau an, etwa berechnet, fachlich noch offen, technisch validiert, importiert oder übermittelt und bestätigt. Schließen Sie mit dem noch erforderlichen konkreten Bearbeitungsschritt. Arbeiten Sie nach dessen Erledigung im vorhandenen Ergebnis weiter.

## 6 Beispiele

### 6.1 Solo-Selbstständiger mit mehreren Tätigkeiten

Ein Programmierer betreut Datenschutzmandate, unterrichtet an einer Musikschule und erhält Autoren-Gutschriften sowie eine VG-WORT-Ausschüttung. Prüfen Sie die Tätigkeit und Abrechnung je Umsatz, die gestattete Istbesteuerung, Befreiungsnachweise, Teilzahlungen und Kostenzuordnung. Die ertragsteuerliche Trennung der Tätigkeiten führt nicht automatisch zu mehreren Umsatzsteuervoranmeldungen. Die Tomasius-Akte eignet sich zur belegten Durchführung.

### 6.2 Berichtigte Eingangsrechnung und spätere Zahlung

Eine im Dezember ausgestellte Rechnung erhält der Unternehmer im Januar. Der Steuerausweis wird später ergänzt. Ordnen Sie die Rechnung nach ihrem ursprünglichen Inhalt und Eingang ein. Prüfen Sie, ob eine Rückwirkung möglich ist und welches Feld in welchem Voranmeldungszeitraum anzupassen ist. Legen Sie die vollständige berichtigte Anmeldung und die Versionsdifferenz vor.

### 6.3 Import und freigegebene Übermittlung

Der Nutzer wählt XML-Import, hat das passende Jahresschema bereitgestellt und meldet sich selbst bei Mein ELSTER an. Validieren Sie den Importblock, lesen Sie die übernommenen Werte zurück und prüfen Sie die ausgelassenen Felder. Bei bereits beauftragter Abgabe des endgültigen Datensatzes führen Sie den verfügbaren autorisierten Weg bis zur Eingangsbestätigung aus.
