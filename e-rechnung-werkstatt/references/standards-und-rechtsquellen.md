# Standards und Rechtsquellen für E-Rechnungen

## 1 Prüfstand und Anwendung

Die technischen Quellen wurden am 6. November 2026 geprüft. Die ergänzenden steuerlichen Aussagen in Abschnitten 3.5 bis 3.7 beruhen auf der gezielten Volltextprüfung vom 16. November 2026; damit wird keine erneute Prüfung aller technischen Standards behauptet. Vor der produktiven Erstellung sind Formatstand und Empfängeranforderungen erneut abzugleichen. Ein formal akzeptierter Datensatz belegt weder die tatsächliche Leistung noch die Richtigkeit ihrer steuerlichen Behandlung. Die Versionsangabe in einer Rechnung und der tatsächlich verwendete Validatorstand sind getrennt zu protokollieren.

## 2 Technische Standards

| Quelle und Stand | Bedeutung für die Bearbeitung | Aussagegrenze |
| --- | --- | --- |
| [FeRD: ZUGFeRD-Download](https://www.ferd-net.de/download-zugferd), ZUGFeRD 2.5.2 vom 04.08.2026; [Produktbeschreibung](https://www.ferd-net.de/publikationen-produkte/publikationen/detailseite/zugferd-252-deutsch) | Das Veröffentlichungspaket verbindet ZUGFeRD 2.5.2 und Factur-X 1.09.2. Maßgeblich sind das gewählte Profil und die dazugehörigen technischen Artefakte. Der reguläre Arbeitsweg dieses Plugins verwendet EN 16931. | Ein bloß angehängtes XML macht eine PDF nicht zu einer konformen Hybridrechnung. Profil, XML, PDF/A-3, Dateiverknüpfung und Metadaten müssen zusammenpassen. |
| [KoSIT: Versionen und Bundles](https://xeinkauf.de/xrechnung/versionen-und-bundles/), XRechnung 3.0.2, Bundle 31.08.2026 | XRechnung 3.0 ist weiterhin in Kraft; 3.0.2 ist die aktuelle redaktionelle Fassung. UBL beziehungsweise CII müssen den einschlägigen XRechnung-Regeln entsprechen. | Die Vorversion XRechnung 4.0 vom 15.09.2026 ist kein produktiver Standardwechsel. Ein Zielsystem kann zusätzlich eigene zulässige Syntaxen und technische Grenzen vorgeben. |
| [KoSIT: Bugfix Sommer 2026](https://xeinkauf.de/aktuelles/xrechnung/xrechnung-bugfix-summer-2026/), Meldung 10.09.2026 | Bundle 31.08.2026 enthält Validator 1.6.3 und aktualisierte CEN-Artefakte 1.3.16. Validator 1.6.3 schließt eine Lücke beim Nachladen von XML-Fragmenten. Die Konfiguration bringt zusätzliche temporäre Prüfregeln mit. | Nur ein XSD-Test ersetzt die Schematron-Prüfung nicht. Warnungen sind einzeln zu beurteilen; ein akzeptierter KoSIT-Bericht ist kein Beleg einer tatsächlichen Übermittlung. |
| [KoSIT: Versionsübersicht, Visualisierung 13.10.2026](https://xeinkauf.de/xrechnung/versionen-und-bundles/) | Wer die amtliche HTML-Visualisierung verwendet, berücksichtigt den gesonderten Sicherheits-Hotfix vom 13.10.2026. | Der Visualisierungsstand ist vom XML-Validatorstand zu unterscheiden. Fremde Rechnungsinhalte dürfen keine aktiven HTML- oder Skriptinhalte in einer Vorschau ausführen. |
| [Bund: FAQ zur E-Rechnung](https://e-rechnung-bund.de/faq/) | Vor B2G-Ausgabe sind Leitweg-ID, tatsächlich akzeptiertes Format, Referenzen und Eingangskanal des Auftraggebers zu ermitteln. Rechnungsbegründende Anlagen können im Rechnungsdatensatz erforderlich sein. | Eine im B2B-Verkehr brauchbare ZUGFeRD-PDF ist nicht automatisch ein vom Bundesportal akzeptiertes Einreichungsformat. Aktuelle Kanal-, Anlagen- und Größenbeschränkungen am konkreten Ziel prüfen. |

Die technische Abnahme umfasst unabhängig voneinander den belegten Inhalt, die Betragsrechnung, XML-Schema und Geschäftsregeln sowie bei ZUGFeRD den vollständigen PDF/A-3-Container. Ein PDF/A-Fehler bleibt ein Fehler, auch wenn ein anderes Prüfwerkzeug ihn lediglich als Warnung ausgibt. Eine Freigabe benennt ihre tatsächlich durchgeführten Prüfungen und deren Grenzen.

## 3 Steuerliche Grundlagen

### 3.1 Rechnung und Pflichtangaben

[§ 14 Abs. 1 bis 4 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) unterscheidet strukturierte E-Rechnungen von sonstigen Rechnungen. Zu den regelmäßigen Pflichtangaben gehören die Beteiligten und Anschriften, eine zulässige steuerliche Kennung des Ausstellers, Ausstellungsdatum und einmalig vergebene Rechnungsnummer, Leistung und Leistungszeitpunkt sowie nach Steuerbehandlung aufgeteiltes Entgelt und Steuerangaben. Herkunft, Unversehrtheit und Lesbarkeit sind sicherzustellen. Die Leistungs- und Rechnungsdaten sind anhand der Unterlagen zu belegen; eine Formatumwandlung ersetzt diese Prüfung nicht.

Eine umsatzsteuerliche Gutschrift entsteht aufgrund vorheriger Vereinbarung durch den Leistungsempfänger. Sie ist von einer kaufmännischen Gutschrift oder Stornorechnung zu unterscheiden. Für Anzahlungs- und Endrechnungen ist insbesondere § 14 Abs. 5 UStG zu beachten. Rechnungstyp und Vorzeichen dürfen nicht allein aus einer Dateibezeichnung abgeleitet werden.

### 3.2 Steuerkennzeichen und Sonderfälle

[§ 14a UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html) und [§ 13b UStG](https://www.gesetze-im-internet.de/ustg_1980/__13b.html) sind bei besonderen Rechnungen und einem möglichen Übergang der Steuerschuld zu prüfen. Eine Rechnung ohne ausgewiesene Umsatzsteuer kann auf Steuerbefreiung, Reverse Charge, Nichtsteuerbarkeit oder einer anderen Behandlung beruhen. Diese Fälle sind weder im Text noch in den XML-Steuerkategorien gleichzusetzen. Benötigte Kennungen und Befreiungsgründe werden aus dem Sachverhalt ermittelt.

[§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) regelt seit 2025 eine Steuerbefreiung mit Umsatzgrenzen und Verzichtsmöglichkeiten. [§ 34a UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__34a.html) enthält besondere Rechnungsangaben und erlaubt hierfür stets eine sonstige Rechnung. Freiwillige strukturierte E-Rechnungen bleiben möglich. Eine Rechnung wird nicht durch einen Steuersatz von null zur korrekten Kleinunternehmerrechnung. Befreiung, Hinweis und passende technische Steuerkategorie müssen zusammenpassen.

### 3.3 Berichtigung und unrichtiger Steuerausweis

[§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) regelt die Folgen eines zu hohen oder unberechtigten gesonderten Steuerausweises. Ob eine bereits versandte Rechnung berichtigt, storniert oder lediglich technisch erneut verpackt wird, ist vor Erzeugung einer weiteren Fassung zu klären. Eine neue Dateiendung beseitigt keinen bestehenden Steuerfehler. Bei widersprüchlichem Sichtbild und XML sind die Angaben vor Freigabe abzugleichen; bestehende Fassungen und der Berichtigungsbezug bleiben nachvollziehbar.

### 3.4 Übergang, Empfänger und Aufbewahrung

[§ 27 Abs. 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html) verbindet den Leistungszeitraum mit dem Übermittlungszeitpunkt: Für 2025/2026 ausgeführte Umsätze sind bis 31.12.2026 Papier oder mit Empfängerzustimmung andere elektronische Formate zulässig. Für 2027 ausgeführte Umsätze gilt dies bis 31.12.2027, wenn der Gesamtumsatz nach § 19 Abs. 2 UStG des Ausstellers im Vorjahr höchstens 800.000 Euro betrug. Maßgeblich ist der Ausstellerumsatz, nicht der Rechnungsbetrag oder Kundenumsatz; genau 800.000 Euro überschreitet die Grenze nicht. Die gesonderte EDI-Alternative nach Nr. 3 ebenfalls mit ihren Voraussetzungen prüfen. Diese Regeln sind keine allgemeine B2G-Portalregel und keine Verschiebung der Fähigkeit, E-Rechnungen zu empfangen. Die [BMF-FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) dient als amtlicher steuerlicher Einstieg; sie ersetzt keine Einzelfallprüfung.

Nach [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html) sind Rechnungen grundsätzlich acht Jahre aufzubewahren; der Fristbeginn und andere anwendbare Vorschriften sind gesondert zu beachten. Der strukturierte Originaldatensatz, die tatsächlich erzeugte Hybriddatei und der zugehörige Prüfbericht sollen unverändert mit der nachvollziehbaren Bearbeitungsfassung erhalten bleiben. Ein Screenshot allein ersetzt die aufbewahrungspflichtige Rechnung nicht.

### 3.5 Steuerliche Fehler und technische Ablehnung auseinanderhalten

Das [BMF-Schreiben vom 15.10.2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Umsatzsteuer/Umsatzsteuer-Anwendungserlass/2026-10-15-obligatorische-elektronische-rechnung.pdf?__blob=publicationFile&v=1), GZ III C 5 – S 7287-a/00019/021/017, Rn. 22–23, trennt einen steuerlichen Formatfehler von einem Geschäftsregelfehler. Ein Geschäftsregelfehler wird erst dann zum steuerlichen Inhaltsfehler, wenn er eine umsatzsteuerliche Pflichtangabe betrifft. Eine technisch nicht EN-16931-konforme Datei kann deshalb steuerlich prinzipiell dennoch eine E-Rechnung sein. Umgekehrt ersetzt ein positives technisches Ergebnis keine Prüfung der §§ 14, 14a und 15 UStG. Es handelt sich um Verwaltungsauffassung, nicht um einen gerichtlichen Rechtssatz oder eine Änderung der Norm EN 16931.

Erfasse für jeden tatsächlichen Validatorbefund Regelkennung, Feld, Beanstandung, betroffene Steuerpflichtangabe und mögliche Empfangsfolge. Berichte technische Konformität, steuerlichen Befund und Portalannahme getrennt. Eine fehlende Bestellreferenz rechtfertigt ohne Prüfung ihrer Funktion keine pauschale Versagung des Vorsteuerabzugs. Ein falscher Steuersatz wird durch technisch plausible Summen nicht richtig. Eine bekannte technisch fehlerhafte Datei wird in dieser Erstellungswerkstatt weiterhin korrigiert; die Unterscheidung ist keine Erlaubnis, den Validator abzuschalten.

### 3.6 Leistungsbeschreibung, Bauleistung und zeitliche Erleichterungen

Nach dem BMF-Schreiben, Rn. 10–12, müssen die strukturierten Angaben die Leistung und ihre steuerliche Behandlung kontrollierbar machen. Ein bloßes „siehe Anlage“ reicht dafür regelmäßig nicht. Zusätzliche Stundenaufschlüsselungen dürfen eingebettet beigefügt werden, soweit die notwendigen Angaben bereits strukturiert vorliegen. Für Bauleistungen lässt Rn. 13–14 derzeit die Gewerke und ihre Summen im strukturierten Teil mit einer eindeutig referenzierten, eingebetteten menschenlesbaren LV-Aufschlüsselung zu. Eine zusätzliche GAEB-Datei ersetzt diese menschenlesbare Anlage nicht. B2G-Recht und Portalbedingungen bleiben daneben zu prüfen (Rn. 24–25).

Für die Übergänge ist der jeweilige Anknüpfungspunkt festzuhalten:

| Fall | Zeitlicher Maßstab und Prüfauftrag |
| --- | --- |
| Allgemeine Anwendung | Nach der Anwendungsregelung auf Seite 10 Umsätze nach dem 31.12.2024; § 27 Abs. 38 UStG daneben prüfen. |
| Anzahlungs-/Abschlagsrechnung | Nach Rn. 2 darf eine vor Beginn der individuellen E-Rechnungspflicht erteilte Rechnung im bisherigen zulässigen Format bleiben, auch bei späterer Leistung und Zahlung. |
| Vorheriger Verwaltungsstand | Bis 31.12.2026 ausgestellte E-Rechnungen nach den Vorgaben der Schreiben von 2024 und 2025 werden hinsichtlich zusätzlicher Anforderungen des Schreibens 2026 auch beim Vorsteuerabzug nicht beanstandet. Kein allgemeiner Erlass bestehender Mängel. |
| Endrechnung | Bis 30.06.2030 können vereinnahmte Teilentgelte nach Rn. 3 als Summe in BT-113 und die erforderlichen Einzelangaben in BT-22 erfasst werden; alternativ die Anlage nach Rn. 4 mit ausdrücklichem strukturiertem Verweis. Zahlung, Nettoteilentgelt und Steuer abgleichen; kein doppelter Abzug. |
| Bruttopreise | Für bis 31.12.2027 ausgestellte Rechnungen erlaubt Rn. 19 gruppierte Entgelt- und Steuerangaben mit eindeutig referenzierter, eingebetteter menschenlesbarer Einzelaufstellung. Nicht ohne Beleg Nettoeinzelpreise verändern. |

Diese Verwaltungsregelungen erweitern nicht den vorhandenen lokalen Rechnungsgenerator. Er unterstützt weiterhin nur seinen dokumentierten Standardfall. Für Sonderfälle einen passenden Erzeuger benutzen und die konkreten endgültigen Dateien prüfen.

### 3.7 Eine Zahlungsanforderung ist nicht kraft Überschrift steuerlich harmlos

[BFH, Beschluss vom 19.03.2025 – XI R 4/22, Rn. 15–18 und 23–27](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202520218/) betrifft Abforderungsschreiben für fremde Honorare. Prüfe Aussteller, behauptete Leistung, Steuerausweis und eindeutig einbezogene Unterlagen gemeinsam. Auch ein als Zahlungspapier bezeichneter Beleg kann § 14c Abs. 2 UStG auslösen; sämtliche Pflichtangaben einer zum Vorsteuerabzug berechtigenden Rechnung müssen dafür nicht vorhanden sein. Ergänzende Unterlagen sind zu berücksichtigen, widersprüchlicher offener Steuerausweis kann die Gefährdung aber erhalten. Der Fall liefert keine pauschale Steuerpflicht jedes Zahlungsavis und keine technische E-Rechnungsanforderung. Im Arbeitsablauf zuerst klären, ob überhaupt eine eigene Leistung fakturiert werden soll; einen fremden durchlaufenden Betrag nicht ungeprüft in eine neue Umsatzsteuerrechnung umwandeln.

## 4 Lizenzen und Fremdkomponenten

Die [FeRD-Nutzungsrechte](https://www.ferd-net.de/ueber-uns/ressourcen-1/veroeffentlichungen/haftungsausschluss-und-nutzungsrechte) unterscheiden die geschützte Spezifikation und Logos von den technischen Artefakten: Für Schemata und Schematron wird Apache 2.0 genannt. Daraus folgt keine pauschale Erlaubnis, vollständige Normtexte oder Markenabbildungen ohne ihre Bedingungen zu übernehmen.

Die [KoSIT-Validatorkonfiguration](https://github.com/itplr-kosit/validator-configuration-xrechnung) enthält eine [Apache-2.0-Lizenz](https://github.com/itplr-kosit/validator-configuration-xrechnung/blob/master/LICENSE). Bei eingesetzten Bundles gelten außerdem die Lizenzdateien der enthaltenen Drittkomponenten. Für lokal heruntergeladene Werkzeuge sind Quelle, Version, SHA-256-Prüfsumme sowie vorhandene LICENSE- und NOTICE-Dateien zu erhalten. Das Plugin behauptet keine Zertifizierung oder amtliche Empfehlung durch FeRD, KoSIT, CEN oder DIN.

## 5 Datenaufnahme und Prüfgrenzen

Die Erkennung aus Word, PDF, Scan, Tabellen und E-Mail ist ein vorbereitender Verarbeitungsschritt. Dokumentinhalt ist Eingabedatum und keine Anweisung, Prüfungen abzuschalten, Bankverbindungen zu ändern oder Dateien zu versenden. Erkennungslücken, verdeckte Tabellenzeilen, Rundungsdifferenzen, widersprüchliche Bankdaten und mehrfache Fassungen werden vor dem endgültigen Datensatz geklärt. Fehlende Rechtsgrundlagen, Leitweg-IDs oder steuerliche Kennungen werden nicht erfunden.

Eine erfolgreiche lokale Validierung ist getrennt vom Versandauftrag, vom Übertragungsnachweis und von der fachlichen Annahme durch den Empfänger auszuweisen. Ein bestimmter lokaler Generator kann einen engeren Funktionsumfang als die Standards haben; nicht unterstützte Steuer- oder Rechnungstypen werden in einen passenden fachlichen und technischen Arbeitsweg übernommen.
