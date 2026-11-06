---
name: format-und-empfaengerregeln-klaeren
description: "Bestimmt das geeignete E-Rechnungsformat und die konkreten Empfängervorgaben für B2B, B2G und sonstige Fälle. Klärt ZUGFeRD-Profil, XRechnung-Version, elektronische Adressen, Leitweg-ID, Bestellbezug und Übermittlungsweg ohne Identifikatoren zu erfinden."
---

# Format und Empfängervorgaben bestimmen

## 1. Zweck und Anwendungsfall

Bestimmen Sie das Format, in dem der konkrete Empfänger die Rechnung verarbeiten kann. Nach [§ 14 Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html) sind strukturierte Daten maßgeblich. Ob der Empfänger zusätzlich eine bestimmte Profilfassung, Bestellreferenz, Adresse oder Plattform verlangt, folgt aus dem jeweiligen Geschäfts- und Übermittlungsverfahren. Steuerliche Formateignung beweist keine Annahme durch jedes Portal.

## 2. Eingaben

Lesen Sie Auftrag, Vertrag, Lieferantenregistrierung, Bestellung und Empfangshinweise. Erfassen Sie Aussteller und Leistungsempfänger einschließlich Ansässigkeit, B2B-, B2G- oder Verbraucherbezug, Rechnungsdatum, Zielstandard und gewünschte Übermittlung. Verwenden Sie vorhandene Stammdaten, ohne dieselben Fragen erneut zu stellen.

## 3. Ablauf und Checkliste

### 3.1 Pflicht und Wunsch unterscheiden

Prüfen Sie Anwendungsbereich, Ausnahmen und Übergangsrecht für den konkreten Umsatz. Leiten Sie aus dem allgemeinen E-Rechnungsrecht keine pauschale Pflicht jedes Verbrauchers oder Kleinunternehmers ab. Bei öffentlichen Auftraggebern prüfen Sie zusätzlich die einschlägige Bundes- oder Landesregel und die konkreten Plattformbedingungen. Eine freiwillig gewünschte E-Rechnung kann auch dann erstellt werden, wenn keine Ausstellungspflicht besteht.

### 3.2 Format begründet wählen

Wenn der Nutzer ein geeignetes Format vorgibt, verwenden Sie es. Bei offenem Format wählen Sie für den üblichen B2B-Fall grundsätzlich ZUGFeRD im Profil EN 16931, wenn der Empfänger es akzeptiert. Für eine ausdrücklich verlangte XRechnung erzeugen Sie die zulässige XML-Syntax und prüfen die einschlägigen Geschäftsregeln. Bei unklarer entscheidender Empfängervorgabe fragen Sie gezielt nach; bearbeiten Sie die fachlichen Rechnungsdaten währenddessen weiter.

Am 6. November 2026 führen die Primärquellen ZUGFeRD 2.5.2 und XRechnung 3.0.2 mit technischem Bundle vom 31. August 2026. Die XRechnung-4.0-Vorversion ist kein Ersatz für die in Kraft befindliche Fassung. Prüfen Sie beim konkreten Einsatz, welche Fassung aktuell gilt und welche der Empfänger verarbeitet. Dokumentieren Sie Standardversion, Profil, Syntax und Regelpaket getrennt.

### 3.3 Empfängerkennungen prüfen

Ordnen Sie Käuferreferenz, Leitweg-ID, Bestellnummer, Vertragsreferenz, Lieferantennummer sowie elektronische Absender- und Empfängeradresse den richtigen Feldern zu. Prüfen Sie das Kennungsschema der elektronischen Adresse. Eine E-Mail-Adresse, Leitweg-ID und Peppol-ID sind verschiedene Angaben; leiten Sie keine davon aus dem Namen des Empfängers ab.

Die Käuferreferenz BT-10 wird nicht durch eine beliebige Bestellnummer ersetzt. Bei einem B2G-Empfänger verwenden Sie die mitgeteilte Leitweg-ID entsprechend dessen Vorgabe. Ein syntaktisch passender Identifikator beweist keine tatsächliche Zuordnung. Ist keine Leitweg-ID erforderlich, erfinden Sie dennoch keine scheinbar amtliche Kennung.

### 3.4 Übermittlung gesondert behandeln

Klären Sie, ob E-Mail, Portal oder ein vorhandener Peppol-Zugang gewünscht und tatsächlich verfügbar ist. Beachten Sie Dateigröße, zugelassene Anhänge und weitere dokumentierte Plattformregeln. Ein Erstellungsauftrag umfasst keine eigenständige Einreichung. Ein Prüfbericht darf einen späteren Portaltest nur nennen, wenn er wirklich stattgefunden hat.

## 4. Quellenpflicht

Es gilt `references/zitierweise.md`. Prüfen Sie [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), das einschlägige Übergangsrecht, [§ 34a UStDV](https://www.gesetze-im-internet.de/ustdv_1980/__34a.html), [BMF-FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html), [KoSIT-Versionen](https://xeinkauf.de/xrechnung/versionen-und-bundles/), [FeRD-Download](https://www.ferd-net.de/download-zugferd) und die vom konkreten Empfänger veröffentlichten Empfangsregeln. Dokumentieren Sie Abrufdatum und Aussagegrenze.

## 5. Ausgabeformat

Halten Sie die Formatentscheidung mit Standard, Profil, Syntax, Regelstand, Empfängerkennungen und vorgesehenem Übermittlungsweg fest. Geben Sie konkrete fehlende Empfängerdaten mit ihrer Auswirkung an. Übernehmen Sie diese Entscheidung in die anschließende Erzeugung; liefern Sie bei einem Rechnungsauftrag nicht nur eine Vergleichstabelle.

Die Ausformulierungspflicht gilt für Begründung und Begleittexte. Formatierte Dokumente verwenden, soweit technisch möglich, Times New Roman 11 pt und dezimale Gliederung. Die technische XML-Struktur folgt dem jeweiligen Standard.

## 6. Beispiele

Eine Kommune verlangt XRechnung und teilt eine Leitweg-ID mit. Übernehmen Sie diese in das vorgesehene Feld und prüfen Sie die übrigen Empfangsangaben. Eine optisch gestaltete ZUGFeRD-PDF ersetzt den ausdrücklich verlangten XML-Beleg nicht.

Ein privater Geschäftskunde akzeptiert ZUGFeRD. Erstellen Sie das geeignete Hybridformat mit geprüften Daten. Verlangen Sie keine Leitweg-ID allein deshalb, weil strukturierte Rechnungen erzeugt werden.
