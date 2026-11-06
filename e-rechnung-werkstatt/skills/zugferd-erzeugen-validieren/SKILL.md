---
name: zugferd-erzeugen-validieren
description: "Erzeugt eine ZUGFeRD-Hybridrechnung aus bestätigten Rechnungsdaten und prüft PDF/A-3, eingebettetes XML, Profil, Metadaten und Betragsgleichheit. Verhindert, dass eine einfache PDF mit beliebigem Anhang oder widersprüchlichem Sichtbild als kompatible E-Rechnung ausgegeben wird."
---

# ZUGFeRD erzeugen und validieren

## 1. Zweck und Anwendungsfall

Erstellen Sie eine lesbare ZUGFeRD-Hybridrechnung mit eingebetteten strukturierten Rechnungsdaten. Das Sichtbild und das XML beschreiben dieselbe Rechnung. [FeRD führt mit Prüfstand 6. November 2026 ZUGFeRD 2.5.2 vom 4. August 2026 als aktuelle Version](https://www.ferd-net.de/download-zugferd). Wählen Sie für den üblichen Anwendungsfall das Profil EN 16931, soweit Empfänger und Fall dazu passen. Eine beliebige PDF mit XML-Anhang ist kein Konformitätsnachweis.

## 2. Eingaben

Verwenden Sie den bestätigten Rechnungsdatensatz mit Belegbezug, Formatentscheidung, gewünschtem Erscheinungsbild und den verfügbaren Erzeugungs- und Prüfwerkzeugen. Ein vorhandenes Rechnungs-PDF dient als Quelle und gegebenenfalls Layoutreferenz. Prüfen Sie vor einer Übernahme seinen Inhalt, vorhandene Signaturen, eingebettete Dateien und technischen Zustand. Verändern Sie keine signierte Originaldatei unbemerkt.

## 3. Ablauf und Checkliste

### 3.1 Daten und Profil abstimmen

Kontrollieren Sie den vollständigen fachlichen Datenstand. Erzeugen Sie ein zum gewählten ZUGFeRD-Profil und zur Version passendes CII-XML. Beachten Sie dessen Schema und Geschäftsregeln. Verwenden Sie weder MINIMUM noch BASIC-WL als vermeintlichen Ersatz für eine vollständige E-Rechnung im vorgesehenen Workflow. Wählen Sie kein höheres oder abweichendes Profil allein wegen eines Dateinamens.

### 3.2 Sichtbild aus demselben Datenstand erzeugen

Erstellen Sie die lesbare Rechnung mit gutem Briefkopf, klarer Empfängeranschrift, Nummer, Datum, Leistungszeitraum, Positionstabelle, Steuergruppen, Gesamt- und Zahlbetrag sowie Zahlungsangaben. Lange Positionen und mehrseitige Tabellen müssen lesbar umbrechen. Erforderliche Steuer- oder Gutschrifthinweise erscheinen konsistent in den dafür vorgesehenen strukturierten Feldern und im Sichtbild.

Nutzen Sie eine vorhandene PDF nur, wenn sie mit dem bestätigten Inhalt übereinstimmt und sich technisch geeignet verarbeiten lässt. Bei Widersprüchen erzeugen Sie ein konsistentes Sichtbild neu und erhalten die Quelle separat. Eine neue Datei darf keine unverändert fortbestehende Signatur oder andere Originaleigenschaft vortäuschen.

### 3.3 PDF/A und XML-Einbettung herstellen

Verwenden Sie einen geeigneten PDF/A-3-Prozess mit eingebetteten Schriften und erforderlichen Farbinformationen. Binden Sie das richtige Rechnungs-XML mit dem versions- und profilgerechten Dateinamen, MIME-Typ, Dateizuordnungen und Metadaten ein. Die entsprechenden Vorgaben werden aus dem verwendeten Regelpaket übernommen, nicht aus frei erfundenen XMP-Feldern. Die bloße Angabe `PDF/A-3` in Dokumenteigenschaften beweist keine Konformität.

### 3.4 XML und endgültige PDF prüfen

Validieren Sie das XML mit Schema und Geschäftsregeln für das tatsächliche Profil. Prüfen Sie die endgültige Hybrid-PDF zusätzlich mit einem geeigneten PDF/A-Validator und einer Prüfung der ZUGFeRD-Einbettung und Metadaten. Vergewissern Sie sich, dass der Validator PDF/A-Mängel tatsächlich prüft und nicht nur als ignorierbare Warnung behandelt. Ein reiner XML-Erfolg genügt nicht.

Extrahieren Sie danach das XML aus der fertigen PDF. Vergleichen Sie seine Bytes beziehungsweise Werte mit der geprüften XML-Datei und dem bestätigten Datenstand. Prüfen Sie die fertigen Seiten visuell, insbesondere Tabellenumbrüche, Sonderzeichen, Beträge, Anschriften und Bankdaten. Änderungen an der PDF nach einem Prüflauf erfordern eine erneute Prüfung.

### 3.5 Fertigmeldung auf den Prüfstand begrenzen

Bezeichnen Sie das Ergebnis nur dann als technisch geprüft, wenn die erforderlichen Prüfungen an den finalen Bytes durchgeführt wurden. Benennen Sie Profil, Version, Regelstand und die Ergebnisse getrennt. Erklären Sie konkrete Warnungen. Ein lokaler Prüfbericht garantiert nicht die Annahme durch jeden Empfänger und keinen erfolgten Versand.

## 4. Quellenpflicht

Es gilt `references/zitierweise.md`. Verwenden Sie das aktuelle [FeRD-Infopaket](https://www.ferd-net.de/download-zugferd), die Dokumentation der tatsächlich eingesetzten Bibliothek und PDF/A-Prüfung sowie [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html). Für steuerliche Einordnung verwenden Sie die [BMF-FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html). Prüfen Sie vor dem Einsatz die Version und das vom Empfänger verlangte Profil.

## 5. Ausgabeformat

Liefern Sie die fertige Hybrid-PDF und den getrennten Prüfbericht. Geben Sie das extrahierte geprüfte XML zusätzlich heraus, wenn dies für Nachvollziehbarkeit oder Weiterverarbeitung gewünscht ist. Der Bericht benennt PDF/A-, XML-, Einbettungs-, Metadaten- und Sichtbildprüfung mit Dateiprüfsummen und tatsächlichem Ergebnis. Ein Entwurf erhält keinen pauschalen Kompatibilitätsvermerk.

Die Ausformulierungspflicht gilt für Leistungsbeschreibungen und Begleittexte. Begleitdokumente verwenden, soweit technisch möglich, Times New Roman 11 pt und dezimale Gliederung. Das Rechnungsformular darf ein sachgerechtes Tabellen- und Briefkopflayout verwenden. Die technischen PDF/A-Anforderungen haben bei Schrift- und Farbeinbettung Vorrang vor einer nur optischen Nachahmung.

## 6. Beispiele

Eine PDF zeigt 1.190 Euro, ihr XML nennt 1.090 Euro. Klären Sie den richtigen Betrag anhand der Leistung und des bestätigten Datensatzes. Erzeugen Sie erst danach ein konsistentes Hybridformat; erklären Sie den Widerspruch nicht durch einen grünen XML-Prüflauf für erledigt.

Der XML-Teil ist gültig, aber Schriften sind nicht eingebettet. Stellen Sie PDF/A fachgerecht her und prüfen Sie die endgültige Hybriddatei erneut. Liefern Sie keine nur umbenannte Standard-PDF als fertige ZUGFeRD-Rechnung.
