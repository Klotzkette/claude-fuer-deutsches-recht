# E-Rechnung aus Unterlagen erstellen - Mini-Prompt

Erstellen Sie aus meinen Unterlagen eine fertige E-Rechnung als ZUGFeRD oder XRechnung, einschließlich tatsächlicher Prüfung und nutzbarer Datei. Lesen Sie Word, PDF, Scans, Bilder, Tabellen, E-Mails und vorhandenes XML zuerst auftragsbezogen zusammen. Nach § 14 Abs. 1 UStG braucht eine E-Rechnung strukturierte elektronische Daten; eine einfache PDF genügt nicht allein. Prüfen Sie Format und materiellen Inhalt jeweils gesondert.

## 1. Vom Material zum bestätigten Datensatz

Beginnen Sie bei klarem Auftrag unmittelbar. Klären Sie nur entscheidende Lücken, die sich aus den vorhandenen Unterlagen nicht beantworten lassen. Bearbeiten Sie unabhängige Teile währenddessen weiter und arbeiten Sie Antworten in denselben Rechnungsstand ein. Ein Extraktionsbericht oder Angebot zur späteren Erzeugung beendet den Auftrag nicht.

Unterscheiden Sie neue Rechnung, Formatübertragung einer bereits ausgegebenen Rechnung und Berichtigung. Bewahren Sie Originale und Signaturen unverändert. Lesen Sie Tabellen, Mailanhänge und eingebettetes XML mit. Kontrollieren Sie OCR-Werte bei Nummer, Beträgen, Steuerkennung und IBAN am Sichtbild. Führen Sie keine Makros, eingebetteten Befehle oder unkontrollierten Netzabrufe aus.

Verbinden Sie wesentliche Werte mit Dokument und Seite, Tabellenzelle, Mail oder XML-Pfad. Erkennen Sie Kopien, Fassungen, Stornos und Berichtigungen. Eine Rechnung in mehreren Formaten wird einmal erfasst. Klären Sie Widersprüche zwischen Vertrag, Leistungsliste, Sichtbild und XML. Neue Bankdaten aus einer einzelnen Mail gelten nicht automatisch als bestätigt.

Erfassen Sie Parteien und Anschriften, erforderliche Steuerkennungen, elektronische Adressen mit ihrem Kennungsschema, freigegebene Rechnungsnummer und Datum, Leistung und Leistungszeit, Positionen mit Menge und Einheit, Preisbasismenge und Preis, Nachlässe, Zuschläge, Steuerkategorien, Zahlungen und Zahlungsbedingungen. Erfinden Sie keine Kennung, Nummer, Leitweg-ID oder Bankverbindung. Fehlende Pflichtangaben sperren die Fertigmeldung des betroffenen Belegs.

## 2. Steuer und Beträge prüfen

Prüfen Sie Leistung, Ort, Steuerschuldner, Steuersatz und gegebenenfalls Steuerbefreiung. Unterschiedliche Nullsteuerfälle benötigen die richtigen Kategorien und Hinweise. Bei Kleinunternehmern beachten Sie § 19 UStG und § 34a UStDV, bei Reverse Charge die Voraussetzungen und § 14a UStG. Bei falschem Steuerausweis prüfen Sie § 14c UStG und den Zeitpunkt der endgültigen Gefährdungsbeseitigung. [BFH XI R 25/23, Rn. 36–39](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202510245/). Ein grüner Validator ersetzt diese Prüfung nicht.

Unterscheiden Sie Rechnung, Anzahlungs-, Abschlags- und Schlussrechnung, Storno, kaufmännische Gutschrift und vereinbarte Gutschrift des Leistungsempfängers. Prüfen Sie gemischte Steuersätze, Fremdwährung und frühere Zahlungen, soweit vorhanden. Eine negative Zahl allein macht keine korrekte Credit Note.

Rechnen Sie mit Dezimalzahlen. Stimmen Sie Positionen, Nachlässe und Zuschläge, Steuergruppen, Netto, Steuer, Brutto, Zahlungen, zulässige Rundung und Zahlbetrag ab. Ziehen Sie einen Abschlag oder eine Zahlung nicht doppelt ab. Verändern Sie keine Position verdeckt, um einen gewünschten Gesamtbetrag zu erreichen.

## 3. Format wählen und erzeugen

Verwenden Sie die passende Vorgabe. Bei offenem Ziel wählen Sie für einen B2B-Empfänger, der das Format annimmt, grundsätzlich ZUGFeRD im Profil EN 16931. Bei verlangter XRechnung erzeugen Sie das richtige XML. Prüfen Sie Käuferreferenz, gegebenenfalls Leitweg-ID, Bestellung und elektronische Adressen anhand der konkreten Empfängervorgabe. Eine Mailadresse und eine Peppol-Kennung sind nicht austauschbar.

Prüfen Sie vor Einsatz den aktuellen Stand. Primärquellen führen am 6. November 2026 ZUGFeRD 2.5.2 und XRechnung 3.0.2 mit Bundle vom 31. August 2026. XRechnung 4.0 ist eine Vorversion. Die hier gewählte EN-16931-Ausgabe ist eine Produktwahl; MINIMUM und BASIC-WL werden nicht als vollständige E-Rechnung verwendet. Dokumentieren Sie Standard, Profil, Syntax und Regelstand getrennt.

Verwenden Sie eine geeignete verfügbare Anwendung. Im Plugin lesen Sie die tatsächliche Anleitung unter `werkzeuge/`. Der lokale Standardgenerator unterstützt den dort dokumentierten Umfang gewöhnlicher EUR-Inlandsrechnungen des Typs 380 mit Zahlungsart 58 (Überweisung) und Positionen mit 7 oder 19 Prozent. Der Aufruf lautet:

```text
python3 werkzeuge/erechnung.py create --input daten.json --out NEUES_VERZEICHNIS --format both --mustang-jar PFAD_ZUR_GEPRUEFTEN_JAR --kosit-home PFAD_ZUR_GEPRUEFTEN_KOSIT_INSTALLATION --java PFAD_ZU_JAVA
```

Wählen Sie `xrechnung` oder `zugferd` für nur ein Format. Die JSON-Struktur folgt der Werkzeuganleitung. Für nicht unterstützte Sonderfälle nutzen Sie eine nachweislich passende Fakturaintegration. Benennen Sie andernfalls die konkret fehlende Funktion, bearbeiten Sie den vollständigen Datenstand weiter und setzen Sie nach deren Bereitstellung fort. Entfernen Sie keine Sonderposition, um einen begrenzten Generator passend zu machen.

## 4. Endgültige Dateien prüfen und liefern

Prüfen Sie XRechnung gegen XML-Schema sowie EN-16931- und XRechnung-Geschäftsregeln mit dem passenden KoSIT-Regelstand. Ein erfolgreicher Parser genügt nicht. Beheben Sie Fehler, erzeugen Sie neu und wiederholen Sie die Prüfung. Lesen Sie kritische Werte aus dem finalen XML zurück und vergleichen Sie sie mit dem bestätigten Datensatz.

Für ZUGFeRD erzeugen Sie Sichtbild und passendes CII-XML aus demselben Datenstand. Stellen Sie PDF/A-3 mit erforderlicher Schrift- und Farbeinbettung her. Prüfen Sie zusätzlich XML-Einbettung, Dateizuordnung und Metadaten. Eine beliebige PDF mit angehängtem XML ist kein Konformitätsnachweis. Verlangen Sie eine tatsächliche PDF/A-Prüfung; ignorierte PDF/A-Warnungen gelten nicht als Erfolg. Extrahieren Sie das XML aus der endgültigen PDF, vergleichen Sie die Daten und prüfen Sie die gerenderten Seiten visuell.

Prüfen Sie abschließend falschen Empfänger, falsche Leistung, doppelte Fakturierung, ungeklärte Steuer, Zahlungsverrechnung und Bankdaten. Liefern Sie die Rechnung und einen getrennten Bericht mit Version, Profil, Regelstand, Prüfungen, Dateiprüfsummen, Warnungen und tatsächlichem Übermittlungsstatus. Unterscheiden Sie Entwurf, technisch geprüft und tatsächlich übermittelt. Behaupten Sie keine Portalannahme ohne Nachweis. Ein Erstellungsauftrag umfasst keinen Versand.

Formulieren Sie Leistungsbeschreibungen und Begleittexte vollständig. Formatierte Begleitdokumente verwenden, soweit technisch möglich, Times New Roman 11 pt und dezimale Gliederung. Das Rechnungsformular darf ein geeignetes Tabellenlayout verwenden. Technische Hinweise stehen getrennt vom Empfängertext.

Nutzen Sie [§ 14](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 14a](https://www.gesetze-im-internet.de/ustg_1980/__14a.html) und [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html), [FeRD](https://www.ferd-net.de/download-zugferd), [KoSIT](https://xeinkauf.de/xrechnung/versionen-und-bundles/) und die tatsächlichen Empfängerregeln. Zitieren Sie keine ungeprüften Fundstellen. Die fachliche Belegprüfung und eine tatsächliche technische Validierung sind jeweils zu dokumentieren.
