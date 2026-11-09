---
name: rechnung-berichtigen-und-ausgabe-pruefen
description: "Unterscheidet Formatübertragung, Rechnungskorrektur, Storno und Gutschrift und prüft die endgültige E-Rechnung auf Inhalt, Dubletten, Steuerausweis und Versionsidentität. Liefert konsistente Ausgabedateien mit nachvollziehbarem Prüf- und Übermittlungsstatus."
---

# Rechnung berichtigen und Ausgabe abschließend prüfen

## 1. Zweck und Anwendungsfall

Korrigieren Sie die konkret fehlerhafte Rechnung oder schließen Sie die Prüfung einer erzeugten Rechnung ab. Eine Formatübertragung ohne Inhaltsänderung ist von einer materiellen Berichtigung zu unterscheiden. Nach [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) kann ein falscher gesonderter Steuerausweis eigene Steuerfolgen haben. Ein nachträglich grüner Formatbericht beseitigt diese Folgen nicht automatisch.

## 2. Eingaben

Lesen Sie Originalrechnung, Ausgabestatus, Vertrag, Leistungs- und Zahlungsunterlagen, vorherige Berichtigungen und Prüfberichte. Prüfen Sie, ob das Dokument bereits an einen Empfänger gelangt oder nur ein interner Entwurf geblieben ist. Erfragen Sie nur eine für die Korrektur entscheidende fehlende Angabe. Bewahren Sie die ursprünglichen Dateien und Übermittlungsnachweise unverändert.

## 3. Ablauf und Checkliste

### 3.1 Korrekturgegenstand feststellen

Bestimmen Sie den konkreten Fehler und seine Ursache. Trennen Sie unzutreffende Partei, Leistung, Betrag, Steuer, Zahlungsangabe und bloßen Formatmangel. Klären Sie, welche Fassung beim Empfänger vorliegt. Erfassen Sie die Beziehung zwischen Original, Korrektur und gegebenenfalls Ersatzrechnung so, dass keine doppelte Forderung entsteht.

### 3.2 Geeigneten Korrekturweg wählen

Prüfen Sie, ob ein Entwurf intern ersetzt werden kann oder eine bereits ausgegebene Rechnung nachvollziehbar berichtigt werden muss. Verwenden Sie die passende Dokumentart und die erforderlichen Vorrechnungsreferenzen. Eine kaufmännische Gutschrift, ein Storno und eine vom Leistungsempfänger vereinbarte Gutschrift sind unterschiedliche Vorgänge. Ändern Sie die Bedeutung nicht nur durch das Vorzeichen einer Zahl.

Bei falschem Steuerausweis prüfen Sie die Voraussetzungen und erforderlichen Schritte der steuerlichen Berichtigung gesondert. Versprechen Sie keine automatische Rückwirkung oder Gefährdungsbeseitigung. Eine erforderliche Erklärung gegenüber Finanzamt oder Empfänger wird nur im beauftragten Umfang vorbereitet und nicht eigenmächtig versandt.

Bei [BFH, Urteil vom 09.07.2025 – XI R 25/23, Leitsätzen 2–3 und Rn. 36–39, 54–57](https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202510245/) entfällt § 14c UStG bei vollständig ausgeschlossener Gefährdung. Eine Berichtigung wegen beseitigter Gefährdung wirkt im Zeitpunkt ihrer Beseitigung. Dokumentieren Sie, ob Vorsteuer geltend gemacht oder zurückgezahlt wurde und ab wann die Gefährdung endgültig ausgeschlossen war. Prüfen Sie das Verfahren nach § 14c Abs. 1 und 2 getrennt. Die Entscheidung beurteilt die Steuerschuld des Rechnungsausstellers. Die Abzugsberechtigung des Empfängers prüfen Sie eigenständig nach § 15 UStG.

### 3.3 Alle Darstellungen gemeinsam ändern

Aktualisieren Sie bestätigten Datensatz, XML, gegebenenfalls PDF-Sichtbild und Zahlungsüberleitung gemeinsam. Kontrollieren Sie Rechnungsidentität, Referenzen, Nummernkreis und Status. Eine Formatübertragung soll dieselbe Rechnung abbilden; eine berichtigte Rechnung muss ihre Beziehung zum bisherigen Beleg nachvollziehbar machen.

### 3.4 Endgültige Dateien erneut prüfen

Validieren Sie die endgültigen Dateien mit den zum Standard passenden Regeln. Bei XRechnung prüfen Sie XML-Schema, EN-16931- und XRechnung-Geschäftsregeln. Bei ZUGFeRD prüfen Sie zusätzlich PDF/A, Einbettung, Metadaten und Sichtbild. Lesen Sie die kritischen Werte aus dem fertigen Ergebnis zurück. Ein Bericht über eine frühere Fassung ist kein Nachweis für die korrigierten Bytes.

### 3.5 Fachliche Gegenprüfung abschließen

Fragen Sie, welche plausible Fehlerannahme die fertige Rechnung noch gefährdet: falscher Empfänger, ungeklärte Leistung, unbewiesene Befreiung, bereits abgerechnete Position, doppelt verrechnete Anzahlung, veraltete IBAN oder ein falsch bezeichneter Übermittlungsstatus. Prüfen Sie diese Annahme am Material und beheben Sie einen bestätigten Fehler. Die technische Validierung ersetzt diesen Abgleich nicht.

### 3.6 Kontrolliert übergeben

Liefern Sie fertige Rechnung, gegebenenfalls erforderliches Berichtigungsschreiben und getrennten Prüfbericht. Halten Sie fest, welcher Beleg ersetzt oder ergänzt wird und wie sich der Zahlbetrag auswirkt. Ein Versand erfolgt nur bei entsprechendem Auftrag und über den belegten Weg. Bewahren Sie erforderliche Originale, Versionen und tatsächliche Nachweise für die weitere Bearbeitung auf.

## 4. Quellenpflicht

Es gilt `references/zitierweise.md`. Prüfen Sie [§ 14 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html), [§ 14c UStG](https://www.gesetze-im-internet.de/ustg_1980/__14c.html) und die konkrete Berichtigungsregel sowie das jeweils verwendete [KoSIT-](https://xeinkauf.de/xrechnung/versionen-und-bundles/) oder [FeRD-Regelpaket](https://www.ferd-net.de/download-zugferd). Rechtsfolgen der Rückwirkung oder eines Vorsteuerabzugs werden nur auf verifizierter Grundlage erläutert. Erfinden Sie keine Literaturfundstelle.

## 5. Ausgabeformat

Liefern Sie die korrigierte beziehungsweise abschließend geprüfte Rechnung und einen Prüfbericht mit Identität, Vorversion, Änderung, Regelstand, Prüfergebnis, Dateiprüfsummen und tatsächlichem Übermittlungsstatus. Ein erforderliches Begleitschreiben erläutert die Berichtigung verständlich, vollständig und ohne interne Werkzeuganweisungen.

Die Ausformulierungspflicht verlangt vollständige Sätze statt Skelette und Halbsätze. Formatierte Schreiben und Vermerke verwenden, soweit technisch möglich, Times New Roman 11 pt und ausschließlich dezimale Gliederung. XML und Rechnungsformulare folgen den sachlich erforderlichen technischen beziehungsweise tabellarischen Formaten.

## 6. Beispiele

Eine Rechnung wurde bereits mit 19 Prozent ausgegeben, obwohl nach belegter Einordnung der Leistungsempfänger die Steuer schuldet. Bereiten Sie die fachlich richtige Korrektur mit eindeutigem Originalbezug vor und prüfen Sie den bisherigen Steuerausweis gesondert. Das bloße Austauschen der XML-Datei genügt nicht.

Ein Kunde erhält dieselbe Rechnung nun als ZUGFeRD statt als bisherige einfache PDF. Stimmen Identität und Inhalt überein, behandeln Sie dies nicht ohne Grund als zweite neue Forderung. Geben Sie den Formatwechsel im getrennten Übergabehinweis nachvollziehbar an.
