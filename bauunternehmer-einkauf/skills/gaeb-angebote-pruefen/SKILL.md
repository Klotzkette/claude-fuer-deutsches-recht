---
name: gaeb-angebote-pruefen
description: "Prüft X83-Anfragen und X84-Angebote auf Austauschphase, Schema, LV-Gleichstand, Positionsrechnung und Abweichungen zu PDF-Angebot und Mail-Nachträgen. Erstellt einen nachvollziehbaren Importvermerk."
---

# GAEB-Angebote fachlich und technisch prüfen

## 1 Zweck und Anwendungsfall

Prüfen Sie das eingegangene Angebot für Import und Vergleich. Die Prüfung verbindet den technischen Formatstatus mit einem getrennten kaufmännischen und fachlichen Abgleich.

## 2 Eingaben

Benötigt werden die freigegebene X83-Anfrage, die X84 je Bieter, eventuelle native Altformate, datierte PDF-Angebote, Mailanhänge und der gewünschte Vergleichsstand. Bei fehlenden Binär- oder XML-Zugriffen arbeiten Sie mit einem belegbaren Export und kennzeichnen die nicht ausführbaren Prüfschritte.

## 3 Ablauf und Checkliste

1. Sichern Sie Eingangsdatei und E-Mail-Bezug. Identifizieren Sie Format und Phase am Dateiinhaltsmodell statt an der Endung allein. Verwenden Sie bei XML einen Parser ohne externe Entitäten und ohne Zugriff auf entfernte Ressourcen. Prüfen Sie gegen das zur Phase und Paketfassung passende offizielle Schema und protokollieren Sie die verwendete Fassung und Fehlerstellen. Bei Altformaten prüfen Sie mit einer tatsächlich verfügbaren Formatprüfung, deren Reichweite Sie angeben.
2. Gleichen Sie Anfragekennung, Leistungsverzeichnis, Hierarchiestufen, Ordnungszahlen, Positionsarten, Menge und Mengeneinheit mit der X83 ab. Stellen Sie fehlende, zusätzliche, umnummerierte oder fachlich geänderte Positionen einzeln dar. Leere Preise, explizite Nullpreise, Textpositionen und Optionen haben verschiedene Bedeutungen.
3. Rechnen Sie Positionspreis und Summe nach. Prüfen Sie Währung, Rundung, Nachlassbasis, Umsatzsteuer und den Umfang jedes Netto- oder Bruttobetrags. Ordnen Sie je OZ die Menge, den Einheitspreis, den Gesamtbetrag und den Status zu. Legen Sie die Rundungsregel offen und erklären Sie Differenzen zum Export.
4. Stellen Sie GAEB-Stand, PDF und nachgereichte E-Mails nebeneinander. Weisen Sie Zusatzkosten, Ausschlüsse, Rabatte, Bindung und Leistungsbedingungen aus, die nur aus Begleitunterlagen folgen. Ein späteres Schreiben aktualisiert nur die darin belegten Aussagen. Nehmen Sie einen bestätigten Dokumentenvorrang aus der Akte auf.
5. Geben Sie geeignete Positionen an den Preisspiegel weiter. Dokumentieren Sie das technische Prüfergebnis, die fachliche Auswertung und noch erforderliche Bestätigungen getrennt. Importerfolg in einer konkreten AVA-Software melden Sie erst nach einem tatsächlichen Import.

## 4 Quellenpflicht

Belegen Sie jede Abweichung mit Dateiname, Fassung und vollständiger OZ oder dem konkreten XML-Pfad. Die herausgebende Stelle dokumentiert Phasen und Schema-Fassungen. [GAEB DA XML](https://www.gaeb.de/de/service/downloads/gaeb-datenaustausch/). [Quellen- und Belegregel](../../references/zitierweise.md)

## 5 Ausgabeformat

Liefern Sie einen Import- und Abweichungsvermerk sowie eine Zeilentabelle mit Originalwert, Vergleichswert und Beleg. Lücken bleiben offen. Bei einem Konflikt entwerfen Sie eine präzise Rückfrage zur maßgeblichen Version.

Formulieren Sie den Vermerk oder Empfängertext vollständig aus. Prüfen Sie vor Abgabe jeden Absatz auf vollständige Sätze und klare Bezüge. Ersetzen Sie Stichwortskelette, Halbsätze und reine Aufzählungen durch ausformulierte Aussagen. Verwenden Sie bei formatierten Dokumenten möglichst Times New Roman 11 pt und ausschließlich dezimale Gliederung. Tabellen und strukturierte Austauschdaten behalten ihr zweckmäßiges Layout. Ein Exporthinweis bei Textausgabe steht außerhalb des Empfängertexts.

## 6 Beispiel

Bei Emswiek kann die Summe der fünf bepreisten Türgruppen den Kern des Angebots richtig wiedergeben. Die Leistung ist erst vergleichbar, wenn die belegt separaten Montage-, Antriebs- und Frachtpositionen sowie etwaige Nachträge erfasst sind.
