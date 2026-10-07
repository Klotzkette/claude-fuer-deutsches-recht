---
name: zahlungen-buchhaltung
description: Ordnet Zahlungseingänge und Ausgänge einer Kanzlei belegt zu, trennt Honorar, Vorschuss, Drittzahlung und Fremdgeld und erstellt nachvollziehbare Buchungsvorschläge und Zahlungsklärungen ohne ungeprüfte Verrechnung.
---

# Zahlungen zuordnen und Buchhaltung vorbereiten

## 1. Zweck und Anwendungsfall

### 1.1. Jeder Geldfluss erhält einen belegten Rechtsgrund

Dieser Skill verarbeitet konkrete Zahlungsbelege und erstellt daraus einen nachvollziehbaren Zuordnungs- und Buchungsvorschlag. Er unterscheidet Geldbewegung, Forderung, wirtschaftliche Berechtigung, steuerlichen Tatbestand und buchhalterische Erfassung. Ein Zahlungseingang auf einem Kanzleikonto ist nicht automatisch Honorar. Eine Rechnung ist nicht automatisch bezahlt, weil ein gleich hoher Betrag eingeht. Eine Zahlung durch die Gegenseite kann Hauptforderung, Zinsen, Kosten oder einen Vergleichsbetrag betreffen und muss entsprechend aufgeschlüsselt werden.

Das Verfahren beginnt beim tatsächlichen Beleg und endet mit einem prüfbaren Vorschlag, einer abgeschlossenen Klärung oder einer im Rahmen des Auftrags tatsächlich ausgeführten Buchung. Das lokale Mandatsjournal ist kein Hauptbuch und keine vollständige Finanzbuchhaltung. Es dokumentiert Zahlungen gesondert und verrechnet sie nicht automatisch mit Honorar. Der Skill darf deshalb keine produktive Verbuchung behaupten, wenn lediglich eine Zahlungsnotiz oder eine Exportdatei angelegt wurde.

### 1.2. Fremdgeld hat einen eigenständigen Schutzstatus

Fremde Gelder werden unverzüglich an den Empfangsberechtigten weitergeleitet oder auf ein Anderkonto eingezahlt; maßgeblich ist zum dokumentierten Rechtsstand § 43a Absatz 7 BRAO. Die alte Absatznummer aus historischen Entscheidungen wird nicht ungeprüft in aktuelle Handlungsempfehlungen übernommen. Eine steuerliche Einordnung als durchlaufender Posten erlaubt keine berufsrechtlich unzulässige Vermischung. Umgekehrt beantwortet ein berufsrechtlicher Fehler nicht automatisch jede steuerliche Frage.

Eine Verrechnung von Honorar mit einem Herausgabeanspruch auf Fremdgeld wird nicht als Routinefunktion ausgeführt. Sie benötigt eine gesonderte zivilrechtliche, berufsrechtliche und gegebenenfalls insolvenzrechtliche Prüfung. Wirtschaftliche Zweckbindung, Drittberechtigung, Aufrechnungslage, Verbote und erforderliche Erklärung müssen geklärt sein. Der bloße Umstand, dass die Kanzlei eine offene Rechnung besitzt, verschafft ihr keine uneingeschränkte Verfügungsbefugnis über sämtliche für den Mandanten eingehenden Beträge.

## 2. Eingaben

### 2.1. Zahlungsbeleg und Gegenbelege

Benötigt werden Konto, Buchungsdatum, Wertstellung, Betrag, Währung, Zahlender, Verwendungszweck und eine eindeutige Transaktionsreferenz. Ergänzend werden Rechnung, Mandatsvereinbarung, Vorschussanforderung, Kostenfestsetzungsbeschluss, Vergleich, Zahlungsankündigung oder sonstiger Rechtsgrund gelesen. Erhalte den unveränderten Originalbeleg. Ein aus einer E-Mail abgeschriebener Betrag kann eine Zahlungsankündigung sein und beweist keinen tatsächlichen Eingang auf dem Konto.

Prüfe, ob derselbe Umsatz bereits importiert oder manuell erfasst wurde. Eine identische Summe an zwei verschiedenen Tagen kann zwei Zahlungen oder eine Korrekturbuchung betreffen. Ein Zahlungsdienstleister kann Gebühren einbehalten, sodass der Nettogeldeingang von der Tilgungsleistung des Zahlenden abweicht. Diese Differenz wird anhand der Abrechnung geklärt und nicht als unerklärte Honorarreduzierung behandelt. Fremdwährungen, Rückbelastungen und Sammelzahlungen erhalten eine eigene Zuordnungsprüfung.

### 2.2. Bestehende Honorargrundlage und Rechnungsstand

Halte bei jedem wesentlichen Schritt den bekannten Vergütungsstand knapp vor. Beispiel: „Die Rechnung R-2026-41 beruht auf dem bestätigten Festpreis von 1.800 Euro netto. Der Zahlungseingang beträgt 2.142 Euro und trägt diese Rechnungsnummer.“ Sind Grundlage, Rechnung und Betrag eindeutig, muss der Nutzer nicht erneut zwischen RVG, Festpreis und Stundensatz wählen. Fehlt eine Zuordnung, kläre nur die konkrete Lücke.

Ist die Vergütungsbasis selbst ungeklärt, frage nach RVG, Zeithonorar, Festpreis, verbindlichem Fee Quote oder Schätzung mit beziehungsweise ohne Deckel sowie Umfang und Netto- oder Bruttobezug. Eine Zahlung wird nicht als umfassende Zustimmung zu einer unklaren Honorarvereinbarung behandelt. Nach einer zusätzlichen tatsächlichen Bearbeitung werden Datum, Person, Dauer, Narrativ und Abrechenbarkeit nur erfragt, soweit sie fehlen. Die Zuordnung bereits belegter Zahlungen kann unabhängig davon vorbereitet werden.

### 2.3. Buchhalterischer und steuerlicher Rahmen

Kläre Gewinnermittlungsart, Umsatzsteuerverfahren, Kontenrahmen, Buchungsperiode und zuständige Buchhaltung. Einnahmenüberschussrechnung und Bilanzierung folgen unterschiedlichen zeitlichen Regeln. Soll- und Istbesteuerung sind ebenfalls zu unterscheiden. Die Bezeichnung einer Zahlung als „Vorschuss“ beantwortet diese Fragen nicht vollständig. Eine im Vorjahr ausgestellte Rechnung kann im neuen Jahr bezahlt werden; daraus folgen unterschiedliche Dokumentationsbedürfnisse je nach Verfahren.

Der Skill benötigt nur die für den Vorgang erforderlichen Daten. Vollständige Bankumsätze aller Mandanten werden nicht ohne Anlass offengelegt oder an externe Werkzeuge übertragen. Prüfe Zugriffsrechte, Verschwiegenheit und Datenschutzrolle des jeweiligen Buchhaltungsdienstleisters. Ein allgemeiner Auftragsverarbeitungsvertrag ersetzt nicht jede berufsrechtliche oder datenschutzrechtliche Voraussetzung. Exporte werden auf den erforderlichen Datenumfang begrenzt und in einem nachvollziehbaren Übergabeprozess bereitgestellt.

## 3. Ablauf / Checkliste

### 3.1. Entscheidungsbaum für einen Zahlungseingang

Stelle zuerst fest, ob der Eingang tatsächlich gebucht oder nur angekündigt ist. Bei tatsächlichem Eingang prüfe, für wen der Betrag wirtschaftlich bestimmt ist. Ist er für den Mandanten oder einen Dritten bestimmt, wird die Fremdgeldroute eröffnet. Ist er zur Begleichung einer Kanzleiforderung bestimmt, prüfe die konkrete Rechnung und Tilgungsbestimmung. Ist er für künftig zu erbringende anwaltliche Leistungen bestimmt, prüfe die Vorschussroute. Bleibt der Zweck unklar, wird der Betrag als ungeklärt separiert und eine gezielte Klärung vorbereitet.

Im zweiten Schritt wird die Höhe abgeglichen. Vollzahlung, Teilzahlung, Überzahlung, Doppelzahlung und Sammelzahlung werden unterschieden. Im dritten Schritt wird die steuerliche Behandlung anhand des konkreten Rechtsgrunds bestimmt. Erst danach entsteht ein Buchungsvorschlag. Diese Reihenfolge verhindert, dass eine zufällig passende Summe die rechtliche Einordnung ersetzt. Eine vorläufige Zuordnung wird ausdrücklich als vorläufig bezeichnet und nicht unbemerkt in einen endgültigen Saldo übernommen.

### 3.2. Tilgungsbestimmung und mehrere Forderungen

Hat der Schuldner wirksam bestimmt, auf welche Schuld er leistet, ist diese Bestimmung zu prüfen und grundsätzlich zu beachten. Bei fehlender Bestimmung kann § 366 BGB die Reihenfolge regeln. Innerhalb einer Schuld ist § 367 BGB für Kosten, Zinsen und Hauptleistung relevant. Eine abweichende Bestimmung und deren Annahme beziehungsweise Ablehnung werden nicht durch eine starre Softwarevoreinstellung ersetzt. Der Buchungsvorschlag nennt die angewandte Zuordnung und ihre Tatsachengrundlage.

Ein Verwendungszweck „Rechnung 41“ ist ein stärkerer Zuordnungshinweis als die bloße Übereinstimmung mit einer offenen Gesamtsumme. Bei einer Sammelzahlung mit mehreren Rechnungsnummern wird die Aufteilung anhand einer Zahlungsavisdatei oder anderer Belege nachvollzogen. Fehlt die Aufteilung, wird nicht automatisch die älteste Forderung als vollständig getilgt markiert, wenn konkrete gegenläufige Angaben vorliegen. Zunächst wird die Bedeutung der Zahlung geklärt.

Prüfe zudem, ob Zinsen und Kosten tatsächlich geschuldet sind. Eine unberechtigte Mahngebühr wird nicht dadurch berechtigt, dass sie im offenen Posten steht. Die Zuordnung auf Nebenforderungen darf deshalb nicht losgelöst von deren Anspruchsgrundlage erfolgen. Bei einem Vergleich können Erledigungs- und Zahlungsbestimmungen die Behandlung verändern. Der Wortlaut des Vergleichs ist vor einer automatischen Standardzuordnung zu lesen.

### 3.3. Drittzahlungen und Rechtsschutzversicherung

Eine Zahlung eines Dritten kann eine fremde Schuld erfüllen, ohne den Dritten zum Vertragspartner zu machen. Erfasse Zahlenden und Leistungsempfänger getrennt. Bei einer Rechtsschutzversicherung werden Schadennummer, Mandat, Rechnung, Deckungsumfang und Selbstbehalt abgeglichen. Eine Zahlung von gesetzlichen Gebühren kann eine Differenz zur vereinbarten Vergütung offenlassen. Die Differenz wird anhand der wirksamen Vereinbarung und der tatsächlichen Deckung erläutert, nicht pauschal dem Mandanten aufgebürdet.

Ist eine Überzahlung erkennbar, prüfe deren Ursache und den richtigen Rückzahlungsempfänger. Eine Rückzahlung an ein neu mitgeteiltes Konto wird nicht allein aufgrund einer unbestätigten E-Mail ausgeführt. Bei Zahlung durch Arbeitgeber, Konzernmutter oder Familienangehörige kann der Rückforderungsanspruch von der konkreten Leistungsbeziehung abhängen. Die ursprüngliche Zahlstelle ist ein wichtiger Hinweis, aber nicht in jedem Fall die abschließende rechtliche Antwort.

Ein externer Zahlender erhält nicht automatisch die gesamte vertrauliche Mandatsabrechnung. Die für die Zahlungszuordnung erforderlichen Informationen werden begrenzt übermittelt. Deckungsfragen, Schweigepflichtentbindung und Mandantenauftrag bleiben getrennte Prüfpunkte. Der Skill erstellt bei Bedarf einen fertigen Klärungsbrief; ein tatsächlicher Versand wird nur bei entsprechendem Auftrag vorgenommen und protokolliert.

### 3.4. Vorschüsse und spätere Verrechnung

Ein Vorschuss auf künftige Leistungen ist weder bereits verdientes Honorar noch zwangsläufig Fremdgeld. Bestimme seinen Rechtsgrund, seine Zweckbindung und die umsatzsteuerliche Behandlung. Im inländischen steuerpflichtigen Standardfall kann die Vereinnahmung eines Entgelts vor Leistungsausführung bereits Umsatzsteuer auslösen. Der konkrete Zeitpunkt hängt vom einschlägigen Steuerrecht und dem tatsächlichen Eingang ab. Eine bloß gestellte Vorschussrechnung wird nicht mit einer tatsächlich vereinnahmten Vorauszahlung verwechselt.

Bei späterer Schlussabrechnung werden geleistete und ordnungsgemäß zugeordnete Vorschüsse nachvollziehbar berücksichtigt. Prüfe Nettobetrag, Steuer und Bruttoverrechnung. Ein Vorschuss von 1.190 Euro brutto entspricht bei ausdrücklich feststehendem Satz von 19 Prozent 1.000 Euro netto und 190 Euro Steuer. Diese Rechnung darf nicht auf Auslands- oder Kleinunternehmerfälle übertragen werden. Die Verrechnung erfolgt mit geeignetem Rechnungswerkzeug; das lokale einfache XRechnungsskript unterstützt sie nicht.

Ist das Mandat beendet, wird ein nicht verbrauchter Vorschuss abgerechnet und gegebenenfalls zurückgezahlt. Die Kanzlei darf ihn nicht allein wegen eigener Liquiditätsbedürfnisse behalten. Prüfe aber zunächst den tatsächlich entstandenen Honorar- und Auslagenanspruch sowie etwaige noch offene Abrechnungsteile. Eine transparente Schlussaufstellung enthält Ausgangsvorschuss, verwendeten Betrag, begründete Restforderung oder Rückzahlungsbetrag und die zugehörigen Belege.

### 3.5. Fremdgeld erkennen und unverzüglich sichern

Typische Fremdgeldindikatoren sind Zahlungen auf die Hauptforderung des Mandanten, Vergleichssummen, treuhänderische Einbehalte oder für Dritte bestimmte Beträge. Der Verwendungszweck allein ist nicht abschließend; prüfe Auftrag und Rechtsgrund. Steht der Empfangsberechtigte fest, wird die unverzügliche Weiterleitung vorbereitet. Ist eine Auszahlung noch nicht möglich, sind die gesetzlichen und berufsrechtlichen Anforderungen an die sichere Verwahrung zu beachten. Eine ungeklärte Bankverbindung rechtfertigt keine private oder betriebliche Nutzung des Geldes.

Dokumentiere Eingang, Berechtigten, Zweck, Verwahrort, geplante Weiterleitung und tatsächlich erfolgte Verfügung. Bei streitiger Berechtigung wird die verantwortliche anwaltliche Person eingeschaltet. Eine vereinbarte Treuhandbedingung darf nicht durch einen simplen Auszahlungswunsch einer Partei übergangen werden. Ebenso ist eine behauptete Gegenforderung der Kanzlei nicht automatisch ein zulässiger Grund, sämtliche Beträge einzubehalten.

Die steuerliche Bezeichnung als durchlaufender Posten wird eigenständig geprüft. Erforderlich ist insbesondere das Handeln im Namen und für Rechnung eines anderen. Eine Zahlung auf dem Geschäftskonto kann berufsrechtlich problematisch sein, ohne dadurch automatisch ihren ursprünglichen wirtschaftlichen Zweck zu verlieren. Dieser Unterschied verhindert falsche Schlüsse in beide Richtungen: Steuerliche Neutralität legalisiert keine Veruntreuung, und ein Berufsrechtsverstoß ersetzt keine steuerliche Subsumtion.

### 3.6. Aufrechnung und Verrechnung nur nach gesonderter Prüfung

Prüfe bei einer beabsichtigten Aufrechnung zunächst Gegenseitigkeit, Gleichartigkeit, Fälligkeit und Erfüllbarkeit nach §§ 387 ff. BGB. Prüfe anschließend vertragliche, gesetzliche, treuhänderische und berufsrechtliche Grenzen. Bei zweckgebundenem oder für Dritte bestimmtem Geld kann eine Verrechnung ausscheiden. In der Insolvenz sind insbesondere die einschlägigen Aufrechnungsverbote und Anfechtungsfragen gesondert zu betrachten. Eine allgemeine Einzugsvollmacht beantwortet diese Fragen nicht.

Der Steuerfall wird ebenfalls gesondert beurteilt. Eine nach außen erklärte Behandlung von Fremdgeld als eigenes Honorar kann die Voraussetzungen eines durchlaufenden Postens verändern. Daraus folgt keine zivilrechtliche Zulässigkeit der Aufrechnung. Der Skill darf eine steuerliche Entscheidung deshalb nicht als Ermächtigung zur Einbehaltung zitieren. Die verantwortliche Entscheidung wird mit Anspruchsgrundlage, Betrag, Erklärung, Zeitpunkt und Belegen dokumentiert.

Ein interner Buchungsvorschlag ist noch keine rechtsgeschäftliche Aufrechnungserklärung. Wenn eine solche Erklärung beauftragt wird, muss ihr Text vollständig ausformuliert und der konkrete Anspruch eindeutig bezeichnet werden. Ohne Auftrag erfolgt keine Erklärung gegenüber dem Mandanten oder einem Dritten. Das Journal wird nicht durch einen negativen Zahlungsbetrag manipuliert, um eine rechtlich ungeklärte Verrechnung darzustellen.

### 3.7. Offene Posten, Verzug und Zinsen

Vor jeder Mahnung werden Rechnung, Zugang, Fälligkeit, Teilzahlungen und Beanstandungen geprüft. Ein im System abgelaufenes Zahlungsziel allein genügt nicht in jeder Konstellation für Verzug. § 286 BGB unterscheidet Mahnung, kalendermäßige Bestimmung, weitere Ausnahmen und die 30-Tage-Regel; bei Verbrauchern ist deren besondere Hinweisanforderung zu beachten. Die Rechnungsanforderungen des § 10 RVG werden nicht übersprungen.

Für Verzugszinsen werden der jeweils geltende Basiszinssatz, Beginn, Ende und Teilzahlungen berücksichtigt. Die gesetzlichen Aufschläge unterscheiden sich nach § 288 BGB. Neun Prozentpunkte für Entgeltforderungen setzen voraus, dass kein Verbraucher beteiligt ist. Die 40-Euro-Pauschale wird nicht gegenüber Verbrauchern angesetzt und nicht unbegrenzt neben denselben Rechtsverfolgungskosten addiert. Ein aktueller Basiszinssatz wird aus einer verifizierten amtlichen Quelle ermittelt, nicht aus Erinnerung eingesetzt.

Bei streitigen Rechnungen kann eine sachliche Erläuterung zweckmäßiger sein als eine automatisierte Mahneskalation. Das ist eine konkrete Mandats- und Kanzleientscheidung, keine generelle Pflicht zum Forderungsverzicht. Dokumentiere, ob ein Einwand geprüft, eine Stundung vereinbart oder eine Zahlungsfrist tatsächlich verlängert wurde. Ein Telefonwunsch „wir zahlen später“ wird nicht ohne Annahme zur verbindlichen Stundung erklärt.

### 3.8. Überzahlungen, Rücklastschriften und Erstattungen

Bei einer Überzahlung vergleiche Originalforderung, bisherige Zahlungen und mögliche weitere Tilgungsbestimmungen. Prüfe, ob eine Doppelzahlung vorliegt oder der Betrag einen weiteren Vorschuss betrifft. Ein bloßer Überschuss im Mandatskonto wird nicht dauerhaft als zusätzlicher Erlös behandelt. Erstelle eine nachvollziehbare Abrechnung und kläre den richtigen Rückzahlungsweg. Eine Rückzahlung erfolgt erst nach tatsächlicher Berechtigten- und Kontoprüfung im vorhandenen Kanzleiverfahren.

Eine Rücklastschrift ist eine neue Geldbewegung und wird nicht durch Löschen des ursprünglichen Zahlungseingangs unsichtbar gemacht. Verknüpfe beide Belege und prüfe, welche Forderung wieder offen ist. Bankgebühren können eigene Kosten sein; ihre Erstattungsfähigkeit gegen den Mandanten benötigt eine Grundlage. Sie werden nicht automatisch mit beliebigen Pauschalen kombiniert. Bei einem Fehler der Kanzlei ist die Weiterbelastung besonders kritisch zu prüfen.

Bei Rückzahlung eines Vorschusses oder einer korrigierten Vergütung werden Umsatzsteuerkorrektur und Buchungsperiode mitgedacht. Ein Geldabfluss beweist noch nicht, dass genau der richtige Steuerbetrag berichtigt wurde. Die Erstattung erhält einen Bezug zur ursprünglichen Rechnung und Zahlung. Der Mandant bekommt eine verständliche Aufstellung, aus der sich der Rückzahlungsbetrag ohne Kenntnis interner Kontonummern ergibt.

### 3.9. Buchungsvorschlag statt erfundener Finanzbuchung

Ein Buchungsvorschlag enthält Beleg-ID, Transaktionsreferenz, Datum, Betrag, Währung, Mandat, Rechtsgrund, steuerliche Einordnung, vorgesehenes Konto und Gegenkonto sowie offene Prüfungen. Kontonummern werden aus dem tatsächlich verwendeten Kontenrahmen übernommen. Der Skill erfindet keine vermeintlich universellen DATEV-Konten. Debitor, Erlöskonto, Umsatzsteuer und Fremdgeldverbindlichkeit sind sachlich unterschiedliche Kategorien; ihre technische Umsetzung hängt vom eingesetzten System ab.

Bei Einnahmenüberschussrechnung wird der tatsächliche Zufluss oder Abfluss mit den einschlägigen Sonderregeln geprüft. Bei Bilanzierung ist die Forderungs- und Verbindlichkeitsebene zusätzlich maßgeblich. Steuerliche Periodenabgrenzung wird nicht allein aus dem Rechnungsdatum abgeleitet. Wird ein Export an eine Steuerberatung vorbereitet, muss die Einordnung nachvollziehbar sein und verbleibende Unsicherheit ausdrücklich enthalten. Eine professionelle Empfängerin soll den Vorschlag prüfen können, ohne die ganze Akte rekonstruieren zu müssen.

Ein Import in ein Produktivsystem erfolgt nur innerhalb des konkreten Auftrags und mit den dort erforderlichen Prüfungen. Der Erfolg wird anhand tatsächlicher Rückmeldung kontrolliert. Eine lokal erzeugte CSV-Datei ist noch kein erfolgreicher Import. Doppelte Importe werden durch Beleg- und Transaktionsreferenzen verhindert. Bei Fehlern wird eine nachvollziehbare Korrekturbuchung vorgenommen, nicht heimlich ein bereits festgeschriebener Datensatz überschrieben.

### 3.10. Lokales Mandatsjournal richtig verwenden

Die Schnittstelle in [Mandatsordner und CLI](../../references/mandatsordner-und-cli.md) sieht für `payment` die Felder `id`, `date`, `gross_eur`, `kind`, `reference`, `source` und `confirmed` vor. Zulässige Arten sind `payment`, `advance` und `third_party`. Diese technischen Kategorien sind begrenzt. Eine Fremdgeldverwaltung mit sämtlichen rechtlichen und steuerlichen Unterkonten bildet das Werkzeug nicht ab. Ein komplexer Fremdgeldfall wird daher mit einem geeigneten gesonderten Verfahren geführt.

Der Aufruf lautet `python3 "<Pluginordner>/scripts/kanzlei.py" payment --akte "<Mandatsordner>" --data "<Zahlungsdatei.json>"`. Der Bruttobetrag wird nur aus dem tatsächlichen Beleg übernommen. Unbestätigte Zahlungsankündigungen bleiben `confirmed=false` und werden nicht als erfüllte Forderung behandelt. Das Journal listet Zahlungen gesondert, ohne sie vom Honorar abzuziehen oder als Umsatz zu buchen. Nach Ausführung werden Mandats-ID, Revision und Ausgabe tatsächlich kontrolliert.

Korrekturen erfolgen nachvollziehbar über Storno mit Grund und neue ID. Eine identische Eingabe unter derselben ID ist wirkungslos; eine abweichende Wiederverwendung wird abgewiesen. Der führende Stand liegt in der SQLite-Datenbank. Abgeleitete Dateien werden regeneriert und nicht als Ersatz für das Journal manuell verändert. Eine Sicherung erfolgt fachgerecht, beispielsweise über das SQLite-Backup-Verfahren oder bei geschlossenem Werkzeug. Die bloße Kopie einer gerade veränderten Datenbank kann unvollständig sein.

### 3.11. Monatliche Abstimmung und Übergabe

Gleiche Bankbewegungen, Mandatsjournal, offene Posten und Buchhaltung ab. Beginne bei den tatsächlichen Summen und untersuche Differenzen einzeln. Ein ausgeglichener Gesamtsaldo kann verdecken, dass zwei Mandanten vertauscht wurden. Deshalb werden neben Summen auch Belegzuordnung und Berechtigte geprüft. Fremdgeld wird nach einzelnen Berechtigten und Zwecken abgestimmt, nicht nur als ein einziger Sammelbetrag.

Die Übergabe an Buchhaltung oder Steuerberatung enthält die konkret benötigten Belege und einen kurzen Entscheidungsvermerk. Beispiel: „Der Eingang über 1.190 Euro betrifft den Vorschuss für Mandat K-41; die Leistung ist noch nicht abschließend erbracht. Die umsatzsteuerliche Vorschussbehandlung ist für den dokumentierten Inlandsfall vorgesehen. Die spätere Verrechnung bleibt offen.“ Fehlende Angaben werden mit verantwortlicher Person und benötigtem Beleg bezeichnet. Eine pauschale Kennzeichnung „bitte prüfen“ genügt bei einem erkannten konkreten Problem nicht.

### 3.12. Abschlusskontrolle und Gegenposition

Prüfe jeden wesentlichen Schluss gegen die stärkste naheliegende Gegenposition. Ein Betrag passt zur Rechnung, könnte aber einem anderen Mandat zugeordnet sein. Ein Verwendungszweck nennt „Kosten“, könnte aber Gerichtskosten statt Honorar meinen. Ein Zahlungseingang des Versicherers könnte nur eine Abschlagszahlung darstellen. Ein scheinbarer Überschuss könnte auf einer noch nicht erfassten Rechnung beruhen. Der Vermerk nennt, welcher Beleg diese Alternative bestätigt oder widerlegt.

Die abschließende Statusmeldung unterscheidet bestätigte Zahlung, geklärte Zuordnung, vorgeschlagene Buchung, tatsächlich gebuchte Position und tatsächliche Auszahlung. Kein Status wird aus dem vorherigen automatisch abgeleitet. Bei einem Hindernis wird die konkret fehlende Information genannt. Die übrigen belegten Vorgänge werden weiterbearbeitet. So bleibt der Arbeitsfluss handlungsfähig, ohne aus einer offenen Frage eine fiktive Vollständigkeit zu erzeugen.

### 3.13. Ein vollständiger Fremdgeldabgleich

Eine Fremdgeldabstimmung beginnt mit dem Anfangsbestand je Berechtigtem. Hinzu kommen nachweisbare Eingänge; abgezogen werden tatsächlich ausgeführte und belegte Auszahlungen. Der rechnerische Endbestand wird mit dem Konto und der Einzelfallzuordnung verglichen. Ein bloßer Kontogesamtsaldo genügt nicht, weil eine Überzahlung an einen Mandanten durch einen noch vorhandenen Betrag eines anderen verdeckt werden könnte. Jeder Bestand benötigt daher eine identifizierbare Berechtigten- und Zweckzuordnung.

Prüfe insbesondere alte Restbeträge. Eine kleine Summe darf nicht allein wegen ihrer geringen Höhe in Kanzleierlös umgebucht werden. Ermittle, wem sie zusteht, weshalb sie noch nicht weitergeleitet wurde und welche konkrete Maßnahme erforderlich ist. Fehlt eine aktuelle Bankverbindung, wird eine gezielte Klärung vorbereitet. Ist der Berechtigte verstorben, insolvent oder nicht mehr vertretungsberechtigt, wird der rechtliche Auszahlungsempfänger gesondert festgestellt. Der frühere Ansprechpartner bleibt nicht automatisch empfangsberechtigt.

Bei einer Differenz wird zunächst geprüft, ob ein technischer Erfassungsfehler, eine fehlende Buchung, eine Bankgebühr oder eine tatsächliche Fehlverfügung vorliegt. Ein Fehlbetrag wird nicht durch Umbuchung aus einem anderen Mandat kaschiert. Die verantwortliche Person erhält eine konkrete Darstellung mit Betrag, betroffenen Belegen und dringendem Klärungsbedarf. Der Skill bleibt bei der sachlichen Feststellung und erfindet keine bereits erfolgte interne Eskalation oder Meldung.

### 3.14. Jahreswechsel und Zahlung unter Vorbehalt

Beim Jahreswechsel werden Rechnungsdatum, Leistungszeitraum, Zahlungsdatum und Wertstellung getrennt dokumentiert. Bei EÜR können Zufluss- und Abflussfragen einschließlich gesetzlicher Ausnahmen entscheidend sein. Bei Bilanzierung kann die Forderung bereits vorher erfasst sein. Umsatzsteuer folgt ihren eigenen Regeln. Eine pauschale Zuordnung sämtlicher Dezemberrechnungen zum alten Jahr wäre deshalb ebenso falsch wie die Behandlung sämtlicher Januareingänge als neue Leistung. Der Vorschlag nennt die Tatsachen und den angewandten steuerlichen Rahmen.

Eine Zahlung unter Vorbehalt wird mit dem konkreten Vorbehalt dokumentiert. Sie kann die Geldschuld erfüllen, ohne jeden Streit über den Rechtsgrund endgültig zu erledigen. Ein pauschaler Vorbehalt wird nicht automatisch als wirksame Rückforderung oder als vollständiges Anerkenntnis behandelt. Prüfe Wortlaut, Zusammenhang und Zweck. Bei einer Zahlung „zur Vermeidung weiterer Kosten“ können andere Fragen entstehen als bei einer ausdrücklich vereinbarten Vergleichszahlung mit Erledigungswirkung.

Die offene Postenliste und das Streitregister können deshalb unterschiedliche Status anzeigen. Eine Rechnung kann bezahlt sein, während ein Rückforderungsstreit offen bleibt. Die Buchhaltung soll nicht allein aufgrund des Zahlungseingangs sämtliche rechtlichen Einwände als erledigt markieren. Umgekehrt darf eine tatsächlich eingegangene Zahlung nicht als unbezahlt geführt werden, nur weil der Mandant ihre Grundlage bestreitet. Zahlungsstatus und Streitstatus werden separat dargestellt.

### 3.15. Konkrete Behandlung einer Sammelzahlung mit Gebührenabzug

Ein Zahlungsdienstleister überweist 2.350 Euro, während der Mandant nachweislich 2.380 Euro bezahlt hat und die Abrechnung 30 Euro Dienstleistergebühr ausweist. Prüfe zunächst, ob die Zahlungsabwicklung im Auftrag der Kanzlei erfolgte und ob die Schuld des Mandanten durch die volle Zahlung erfüllt ist. Ist dies der Fall, darf der verbleibende Unterschied nicht als offene Restforderung von 30 Euro gegen den Mandanten erscheinen. Der Gebührenabzug ist gesondert nach dem Rechtsverhältnis zum Dienstleister und seiner steuerlichen Behandlung zu buchen.

Der Vermerk lautet: „Die Abrechnung des Zahlungsdienstleisters [Referenz] weist eine Kundenzahlung von 2.380 Euro und einen einbehaltenen Gebührenbetrag von 30 Euro aus. Der tatsächliche Bankeingang beträgt 2.350 Euro. Nach Prüfung des vereinbarten Zahlungswegs ist die Rechnung des Mandanten vollständig erfüllt. Der Gebührenabzug wird als eigener Vorgang anhand der Dienstleisterabrechnung beurteilt. Eine Vorsteuer aus dem Gebührenbetrag wird nur bei Vorliegen der erforderlichen Voraussetzungen angesetzt.“

Der Fall zeigt, weshalb eine reine Betragsdifferenz keine ausreichende Mahngrundlage ist. Dieselbe Logik gilt nicht automatisch, wenn der Mandant eigenmächtig Bankspesen abgezogen hat. Dann sind Vertrag, Zahlungsort und Kostentragung gesondert zu prüfen. Die Alternative wird im Vermerk ausdrücklich berücksichtigt und anhand des konkreten Belegs entschieden.

## 4. Quellenpflicht

### 4.1. Normen und Abgrenzungen

Verwende [Zitierweise](../../references/zitierweise.md) und den aktuellen Wortlaut von § 43a Absatz 7 BRAO, § 4 BORA, §§ 362, 366, 367, 387 ff., 286 und 288 BGB sowie den einschlägigen steuerlichen Vorschriften. Bei EÜR sind insbesondere §§ 4 Absatz 3 und 11 EStG, bei Umsatzsteuer insbesondere §§ 10, 13 und gegebenenfalls 20 UStG zu prüfen. GoBD, Aufbewahrung und das konkrete Buchführungssystem werden getrennt vom materiellen Zahlungsanspruch behandelt.

### 4.2. Verifizierte Rechtsprechungsanker

BFH, Urteil vom 29.09.2020 – VIII R 14/17, Rn. 20–32, behandelt die steuerliche Wirkung einer Aufrechnung mit Honorar auf die Verknüpfung eines durchlaufenden Postens. Es erlaubt keine berufsrechtlich unzulässige Verrechnung. [Amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202110029/).

BFH, Urteil vom 16.12.2014 – VIII R 19/12, Leitsätze und Rn. 17–25, trennt die steuerliche Behandlung veruntreuter Fremdgelder von deren rechtswidriger Verwendung. Die Entscheidung ist ausdrücklich keine Gestattung der Eigennutzung. [Amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE201510153/).

BGH, Urteil vom 27.04.2017 – IX ZR 198/16, Rn. 14–16, ist ein Anker für insolvenzrechtliche Risiken der Vermischung und Aussonderung von Treuhandguthaben. Der Fall betrifft keine anwaltliche Standardabrechnung; die Übertragung verlangt die Prüfung des konkreten Kontos und Rechtsverhältnisses. [Amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/IX_ZS/2016/IX_ZR_198-16.pdf?__blob=publicationFile&v=1).

BFH, Beschluss vom 26.02.2026 – V B 11/25, Rn. 2, weist auf eine zur Revision zugelassene Frage des Vorsteuerzeitpunkts hin. Eine Zulassung ist keine Sachentscheidung; ein aktueller Folgestand ist vor einer darauf gestützten Buchungsentscheidung zu ermitteln. [Amtlicher Volltext](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202650044/).

## 5. Ausgabeformat

### 5.1. Nachvollziehbarer Zahlungs- und Buchungsvermerk

Liefere den konkreten Zuordnungsvermerk, den vollständigen Buchungsvorschlag und erforderlichenfalls ein fertiges Klärungs- oder Rückzahlungsschreiben. Technische Tabellen können Beträge und Belegreferenzen ordnen. Das juristische Ergebnis wird in vollständigen, ausformulierten Sätzen erläutert. Skelette, Halbsätze und reine Aufzählungsgerüste sind als Endprodukt verboten. Formatierte Texte verwenden soweit technisch möglich Times New Roman 11 pt und ausschließlich dezimale Gliederung.

Die Ausgabe nennt die Grenzen des tatsächlich Erledigten: erfasst, zugeordnet, vorgeschlagen, importiert oder ausgezahlt. Ein fehlender Kontoabgleich wird ausdrücklich bezeichnet. Technische Hinweise, Quellenprotokolle und interne Kontierungsfragen gehören außerhalb eines versandfertigen Mandantenbriefs. Bei reiner Textausgabe steht ein nötiger Exporthinweis gesondert. Es wird kein tatsächlich nicht erfolgter Bankauftrag, keine Hauptbuchung und kein Versand behauptet.

## 6. Beispiele

### 6.1. Vollzahlung auf eindeutig bezeichnete Rechnung

Der Bankbeleg weist 2.380 Euro mit dem Verwendungszweck „R-2026-41“ aus. Die geprüfte Rechnung beträgt denselben Betrag, vorherige Zahlungen liegen nach Abgleich nicht vor. Der Vermerk lautet: „Der am [Datum] tatsächlich eingegangene Betrag von 2.380 Euro ist der Rechnung R-2026-41 zuzuordnen. Rechnungsaussteller, Schuldner und Verwendungszweck stimmen mit den Stammdaten überein. Der offene Rechnungsbetrag ist damit nach dem geprüften Stand vollständig erfüllt. Die buchhalterische Umsetzung erfolgt im verwendeten Kontenrahmen mit Bezug auf Bankbeleg [ID].“

Der lokale Datensatz enthält `kind=payment`, `gross_eur="2380.00"`, die konkrete Rechnungsreferenz und die bestätigte Belegquelle. Seine Erfassung dokumentiert den Eingang. Die eigentliche Finanzbuchung und die Ausbuchung des offenen Postens werden erst behauptet, wenn sie im betreffenden System tatsächlich erfolgt sind.

### 6.2. Gemischter Vergleichseingang

Auf dem Kanzleikonto gehen 12.000 Euro mit dem Verwendungszweck „Vergleich Müller“ ein. Der Vergleich sieht 10.000 Euro für den Mandanten und 2.000 Euro zur Kostenerstattung vor. Ob der Kostenanteil unmittelbar der Kanzlei zusteht, wird aus Vergleich, Auftrag und Zahlungsbestimmung ermittelt. Er wird nicht allein aufgrund der Bezeichnung „Kosten“ als Kanzleiumsatz vereinnahmt.

Der Prüfvermerk lautet: „Die Vergleichssumme ist zunächst nach den im Vergleich bezeichneten Ansprüchen aufzuteilen. Der Hauptforderungsanteil von 10.000 Euro ist für den Mandanten bestimmt. Für den Kostenanteil wird geprüft, ob ein unmittelbarer Anspruch der Kanzlei, ein Erstattungsanspruch des Mandanten oder eine andere Leistungsbeziehung vorliegt. Eine Verrechnung mit offenen Honoraren wird bis zum Abschluss dieser Prüfung nicht vorgenommen. Die fremden Beträge werden nach den geltenden Verwahrungs- und Weiterleitungsregeln behandelt.“

### 6.3. Vollständiger Brief zur unklaren Zahlung

„Sehr geehrte Frau [Name], am [Datum] ist auf unserem Konto ein Betrag von 1.500 Euro mit dem Verwendungszweck ‚Beratung‘ eingegangen. In Ihren Mandaten sind derzeit die Rechnung [Nummer] über [Betrag] und die Vorschussanforderung vom [Datum] über [Betrag] dokumentiert. Aus dem Verwendungszweck ergibt sich nicht eindeutig, welcher Forderung die Zahlung zugeordnet werden soll.

Bitte teilen Sie uns mit, auf welche dieser Positionen Sie gezahlt haben. Bis zur Klärung führen wir den Eingang gesondert und behandeln keine der beiden Positionen allein aufgrund einer Vermutung als vollständig ausgeglichen. Die vereinbarte Honorargrundlage bleibt unverändert. Sobald die Zuordnung feststeht, erhalten Sie eine aktualisierte Übersicht.

Mit freundlichen Grüßen
[Name], Rechtsanwältin“

Der Brief wird nur verwendet, wenn die Zuordnung nicht bereits aus einer vorhandenen Zahlungsankündigung hervorgeht. Bereits geklärte Angaben werden nicht erneut erfragt. Eine automatische Mahnung der betroffenen Positionen ist vor Klärung sachgerecht zu überprüfen.

### 6.4. Vorschussabrechnung nach Mandatsende

„Sehr geehrter Herr [Name], wir haben die Abrechnung des am [Datum] beendeten Mandats abgeschlossen. Sie haben am [Datum] einen Vorschuss von 1.190 Euro brutto geleistet. Die nach der Vergütungsvereinbarung vom [Datum] und den bestätigten Leistungsnachweisen entstandene Vergütung beträgt 800 Euro netto zuzüglich 152 Euro Umsatzsteuer, insgesamt 952 Euro brutto. Weitere abrechenbare Auslagen sind nach dem geprüften Stand nicht angefallen.

Nach Verrechnung des Vorschusses verbleibt ein Guthaben zu Ihren Gunsten von 238 Euro. Die beigefügte Schlussabrechnung stellt die Leistung und den Vorschuss nachvollziehbar gegenüber. Die Rückzahlung erfolgt nach Prüfung der hinterlegten Bankverbindung und dem beauftragten Zahlungsablauf. Mit dieser Mitteilung wird keine darüber hinausgehende Erledigung anderer Ansprüche vereinbart.

Mit freundlichen Grüßen
[Name], Rechtsanwältin“

Der letzte Satz wird nur aufgenommen, wenn eine solche Klarstellung im konkreten Fall nötig ist. Die Aussage über eine bevorstehende Zahlung wird nicht in eine bereits erfolgte Überweisung umformuliert, solange diese nicht tatsächlich ausgeführt und bestätigt ist.

### 6.5. Sachliche Zahlungserinnerung

„Sehr geehrte Frau [Name], nach Abgleich unserer Zahlungseingänge ist aus der Rechnung [Nummer] vom [Datum] noch ein Betrag von [Betrag] Euro offen. Die Rechnung beruht auf der bestätigten Vergütungsvereinbarung vom [Datum] für [Leistung]. Die Teilzahlung vom [Datum] über [Betrag] Euro haben wir berücksichtigt.

Bitte überweisen Sie den verbleibenden Betrag bis zum [Datum]. Falls Sie bereits gezahlt haben, genügt uns ein Hinweis auf Zahlungsdatum und Verwendungszweck, damit wir den Eingang zuordnen können. Sollten Sie eine konkrete Rechnungsposition beanstanden, teilen Sie uns bitte mit, welche Position betroffen ist; wir erläutern diese anhand der Leistungsaufstellung. Etwaige Verzugsfolgen werden nur auf der Grundlage der tatsächlich vorliegenden gesetzlichen und vertraglichen Voraussetzungen geltend gemacht.

Mit freundlichen Grüßen
[Name], Rechtsanwältin“

Vor Verwendung werden Zugang, Fälligkeit und verbleibender Saldo tatsächlich geprüft. Der Text ist kein Auftrag zur automatischen Forderungseintreibung. Eine weitergehende Mahnung mit Zinsen oder Kosten benötigt die konkrete Berechnung und Rechtsgrundlage.

### 6.6. Vollständige Übergabe eines ungeklärten Altbestands

„Zum Abstimmungsstichtag [Datum] besteht in Mandat [Nummer] ein rechnerischer Restbestand von 84 Euro. Der Betrag ergibt sich aus dem Eingang vom [Datum] über [Betrag] abzüglich der belegten Auszahlungen [Referenzen]. Die Bankabstimmung bestätigt den Gesamtbestand; die rechtliche Zuordnung des Restes ist noch offen. Nach dem Vergleichstext kann es sich um einen verbleibenden Zinsanteil zugunsten des Mandanten handeln. Eine abweichende Kostenbestimmung ist in den bisher geprüften Unterlagen nicht enthalten.

Benötigt wird die vollständige Zahlungsabrechnung der Gegenseite, auf die deren Nachricht vom [Datum] verweist. Bis zur Klärung wird der Restbetrag nicht als Honorar oder sonstiger Erlös behandelt. Die verantwortliche Person prüft die Berechtigung und veranlasst anschließend die erforderliche Weiterleitung. Eine tatsächliche Auszahlung ist bisher nicht erfolgt.“

Dieser Vermerk benennt Betrag, Belegkette, wahrscheinlichste Einordnung, Gegenprüfung und fehlende Unterlage. Er ist belastbarer als die pauschale Notiz „Altbestand bereinigen“. Die geringe Höhe rechtfertigt keine vereinfachte Aneignung. Falls sich später ein Erfassungsfehler statt eines wirklichen Restguthabens herausstellt, wird die Korrektur mit ihrem Grund dokumentiert. Eine tatsächliche Zahlung wird nicht rückwirkend erfunden, um einen Bericht rechnerisch auszugleichen.

Die Übergabe erhält eine verantwortliche Person und einen sachgerechten Klärungszeitpunkt. Eine bloße Ablage im Monatsordner genügt bei fremden Geldern nicht, wenn dadurch die unverzügliche Bearbeitung unterbleibt. Der Skill darf die zuständige Person jedoch nur als informiert bezeichnen, wenn eine entsprechende Mitteilung tatsächlich im beauftragten Rahmen erfolgt ist.
