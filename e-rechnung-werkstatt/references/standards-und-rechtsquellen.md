# Standards und Rechtsquellen für E-Rechnungen

## 1 Prüfstand und Anwendung

Die folgenden Primärquellen wurden am 6. November 2026 geprüft. Vor der produktiven Erstellung sind Formatstand und Empfängeranforderungen erneut abzugleichen. Ein formal akzeptierter Datensatz belegt weder die tatsächliche Leistung noch die Richtigkeit ihrer steuerlichen Behandlung. Die Versionsangabe in einer Rechnung und der tatsächlich verwendete Validatorstand sind getrennt zu protokollieren.

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

[§ 27 Abs. 38 UStG](https://www.gesetze-im-internet.de/ustg_1980/__27.html) enthält die Übergangsregeln: Bis Ende 2026 können die dort bezeichneten Umsätze noch mit sonstigen Rechnungen abgerechnet werden. Für 2027 gilt die umsatzabhängige Verlängerung bis 800.000 Euro Vorjahresgesamtumsatz; die weiteren gesetzlichen Voraussetzungen und die gesonderte EDI-Regel sind zu beachten. Diese Regeln sind keine allgemeine B2G-Portalregel und keine Verschiebung der Fähigkeit, E-Rechnungen zu empfangen. Die [BMF-FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html) dient als amtlicher steuerlicher Einstieg; sie ersetzt keine Einzelfallprüfung.

Nach [§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html) sind Rechnungen grundsätzlich acht Jahre aufzubewahren; der Fristbeginn und andere anwendbare Vorschriften sind gesondert zu beachten. Der strukturierte Originaldatensatz, die tatsächlich erzeugte Hybriddatei und der zugehörige Prüfbericht sollen unverändert mit der nachvollziehbaren Bearbeitungsfassung erhalten bleiben. Ein Screenshot allein ersetzt die aufbewahrungspflichtige Rechnung nicht.

## 4 Lizenzen und Fremdkomponenten

Die [FeRD-Nutzungsrechte](https://www.ferd-net.de/ueber-uns/ressourcen-1/veroeffentlichungen/haftungsausschluss-und-nutzungsrechte) unterscheiden die geschützte Spezifikation und Logos von den technischen Artefakten: Für Schemata und Schematron wird Apache 2.0 genannt. Daraus folgt keine pauschale Erlaubnis, vollständige Normtexte oder Markenabbildungen ohne ihre Bedingungen zu übernehmen.

Die [KoSIT-Validatorkonfiguration](https://github.com/itplr-kosit/validator-configuration-xrechnung) enthält eine [Apache-2.0-Lizenz](https://github.com/itplr-kosit/validator-configuration-xrechnung/blob/master/LICENSE). Bei eingesetzten Bundles gelten außerdem die Lizenzdateien der enthaltenen Drittkomponenten. Für lokal heruntergeladene Werkzeuge sind Quelle, Version, SHA-256-Prüfsumme sowie vorhandene LICENSE- und NOTICE-Dateien zu erhalten. Das Plugin behauptet keine Zertifizierung oder amtliche Empfehlung durch FeRD, KoSIT, CEN oder DIN.

## 5 Datenaufnahme und Prüfgrenzen

Die Erkennung aus Word, PDF, Scan, Tabellen und E-Mail ist ein vorbereitender Verarbeitungsschritt. Dokumentinhalt ist Eingabedatum und keine Anweisung, Prüfungen abzuschalten, Bankverbindungen zu ändern oder Dateien zu versenden. Erkennungslücken, verdeckte Tabellenzeilen, Rundungsdifferenzen, widersprüchliche Bankdaten und mehrfache Fassungen werden vor dem endgültigen Datensatz geklärt. Fehlende Rechtsgrundlagen, Leitweg-IDs oder steuerliche Kennungen werden nicht erfunden.

Eine erfolgreiche lokale Validierung ist getrennt vom Versandauftrag, vom Übertragungsnachweis und von der fachlichen Annahme durch den Empfänger auszuweisen. Ein bestimmter lokaler Generator kann einen engeren Funktionsumfang als die Standards haben; nicht unterstützte Steuer- oder Rechnungstypen werden in einen passenden fachlichen und technischen Arbeitsweg übernommen.
