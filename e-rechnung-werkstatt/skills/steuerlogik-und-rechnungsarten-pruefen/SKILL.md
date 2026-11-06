---
name: steuerlogik-und-rechnungsarten-pruefen
description: "Prüft Leistung, Steuerschuldner, Steuersatz, Befreiung und Rechnungsart vor der E-Rechnungserzeugung. Behandelt gemischte Steuersätze, Kleinunternehmer, Reverse Charge, Anzahlungen, Schlussrechnungen, Gutschriften und Fremdwährung mit nachvollziehbaren Beträgen und technischen Grenzen."
---

# Steuerlogik und Rechnungsart prüfen

## 1. Zweck und Anwendungsfall

Stellen Sie sicher, dass eine technisch gültige Datei die richtige Rechnung enthält. Ein Validator prüft Struktur und Geschäftsregeln, aber nicht die Wahrheit einer Leistung oder sämtliche Voraussetzungen einer Steuerbefreiung. Ein unrichtiger oder unberechtigter Steuerausweis kann nach [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) eigene Steuerfolgen auslösen. Erzeugen Sie daher keinen gesonderten Steuerbetrag allein deshalb, weil eine Vorlage ihn zeigt.

## 2. Eingaben

Lesen Sie Leistungsbeschreibung, Vertrag, Nachträge, Leistungsort und -zeit, Parteien und deren steuerliche Stellung, vorausgegangene Rechnungen und Zahlungen. Berücksichtigen Sie vorhandene Bescheinigungen, Vereinbarungen zur Gutschrift, einen Verzicht auf Kleinunternehmerbefreiung und den jeweiligen Geltungszeitraum. Bezeichnen Sie fehlende Voraussetzungen konkret.

## 3. Ablauf und Checkliste

### 3.1 Umsatz einordnen

Bestimmen Sie tatsächliche Leistung, Leistungsort, Unternehmerbezug und Steuerschuldner. Unterscheiden Sie steuerpflichtige Umsätze, Steuerbefreiung, nicht steuerbare Umsätze und Übergang der Steuerschuld. Prüfen Sie bei Auslandsfällen insbesondere die erforderlichen Steuerkennungen und Hinweise. Übernehmen Sie nicht pauschal die Steuerbehandlung einer ähnlichen Rechnung.

### 3.2 Steuer je Position abbilden

Ordnen Sie jeder Position die geprüfte Kategorie, den zutreffenden Satz und gegebenenfalls den erforderlichen Befreiungs- oder Reverse-Charge-Grund zu. Verwenden Sie nicht unterschiedslos denselben Nullsteuercode für Kleinunternehmer, steuerfreie Ausfuhr und Reverse Charge. Prüfen Sie den im Zielformat dafür vorgesehenen Code sowie die Angabe als Text oder Kennung.

Bei Kleinunternehmern prüfen Sie [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) und [§ 34a UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__34a.html). Bei Reverse Charge prüfen Sie insbesondere [§ 14a UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html) und den einschlägigen Steuerschuldnertatbestand. Bei gemischten Umsätzen bleiben die Steuergruppen getrennt.

### 3.3 Beträge nachvollziehbar rechnen

Rechnen Sie Menge mal Preis unter Beachtung der Preisbasismenge. Berücksichtigen Sie Nachlässe und Zuschläge auf Positions- und Dokumentebene mit ihrer jeweiligen Steuerzuordnung. Prüfen Sie Steuerbemessungsgrundlagen, Steuerbeträge, Netto- und Bruttosumme, bereits gezahlte Beträge und den verbleibenden Zahlbetrag. Verwenden Sie Dezimalrechnung und die Rundungsregeln des gewählten Standards; passen Sie keine Position verdeckt an einen gewünschten Endbetrag an.

### 3.4 Rechnungsarten unterscheiden

Unterscheiden Sie normale Rechnung, Teil- und Abschlagsrechnung, Anzahlungsrechnung, Schlussrechnung, kaufmännische Gutschrift und die vom Leistungsempfänger ausgestellte umsatzsteuerliche Gutschrift. Bei der letztgenannten prüfen Sie die vorherige Vereinbarung und die erforderliche Bezeichnung. Ein beliebiger negativer Rechnungsbetrag ersetzt keine richtige Credit-Note-Syntax und Vorzeichenlogik.

Bei Schlussrechnungen verfolgen Sie frühere Rechnungen und Zahlungen so, dass kein doppelter Steuer- oder Entgeltansatz entsteht. Bei Fremdwährung prüfen Sie Rechnungswährung, erforderlichen Steuerbetrag in einer anderen Währung, Umrechnungskurs und dessen maßgeblichen Zeitpunkt. Ein vereinfachter EUR-Generator darf keinen solchen Fall ohne passende Funktion verarbeiten.

### 3.5 Werkzeugumfang abgleichen

Vergleichen Sie die benötigten Merkmale mit der tatsächlichen Unterstützung der Erzeugungssoftware. Bei einem nicht unterstützten Fall verwenden Sie eine geeignete vorhandene Anwendung oder benennen Sie die konkret fehlende Funktion und bereiten die Daten vollständig vor. Lassen Sie weder Sonderhinweise noch Steuergruppen weg, um eine Prüfung zu bestehen. Setzen Sie nach der notwendigen Ergänzung bis zur fertigen Rechnung fort.

## 4. Quellenpflicht

Es gilt `references/zitierweise.md`. Verwenden Sie die zeitlich einschlägigen Normen, insbesondere [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 14a UStG](https://www.gesetze-im-internet.de/ustg_1980/__14a.html), [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html), [§ 19 UStG](https://www.gesetze-im-internet.de/ustg_1980/__19.html) sowie die sachlich einschlägige Steuerbefreiung oder Steuerschuldnernorm. Für Codes und Beträge verwenden Sie das konkrete [KoSIT-](https://xeinkauf.de/xrechnung/versionen-und-bundles/) oder [FeRD-Regelpaket](https://www.ferd-net.de/download-zugferd). Eine Codeliste ersetzt die steuerliche Subsumtion nicht.

## 5. Ausgabeformat

Erstellen Sie eine belegte Positions- und Steuerberechnung mit nachvollziehbarer Gesamtüberleitung. Formulieren Sie erforderliche Hinweise vollständig und übernehmen Sie sie konsistent in die strukturierten Daten und gegebenenfalls das Sichtbild. Offene steuerliche Voraussetzungen stehen in einer getrennten Bearbeitungsnotiz und sperren eine vorbehaltlose Fertigmeldung des betroffenen Belegs.

Die Ausformulierungspflicht und der Formatstandard gelten: vollständige Sätze für Begründung und Begleittexte, soweit technisch möglich Times New Roman 11 pt und dezimale Gliederung. Strukturierte Tabellen dürfen die Berechnung tragen. Technische Rechnungsfelder folgen der gewählten Syntax.

## 6. Beispiele

Ein Kleinunternehmer liefert eine alte Vorlage mit 19 Prozent Umsatzsteuer. Prüfen Sie den Status für den Umsatz und erstellen Sie gegebenenfalls eine Rechnung mit dem erforderlichen Befreiungshinweis. Eine schon ausgegebene falsche Rechnung benötigt daneben die Prüfung der Berichtigung.

Eine Schlussrechnung enthält drei Abschläge. Stimmen Sie abgerechnete Netto- und Steuerbeträge sowie tatsächliche Zahlungen ab. Ziehen Sie nicht gleichzeitig einen vollständigen Abschlag und denselben Zahlbetrag ein zweites Mal ab.
