---
name: xrechnung-erzeugen-validieren
description: "Erzeugt aus bestätigten Rechnungsdaten eine XRechnung und prüft die endgültige XML-Datei gegen das passende Schema sowie EN-16931- und XRechnung-Geschäftsregeln. Kontrolliert Empfängerreferenzen, elektronische Adressen und den Rückvergleich zum fachlichen Datenstand."
---

# XRechnung erzeugen und validieren

## 1. Zweck und Anwendungsfall

Erstellen Sie die verlangte XRechnung als strukturierte XML-Datei. Eine lesbare PDF ist nur eine zusätzliche Darstellung. Verwenden Sie die vom Empfänger akzeptierte und tatsächlich in Kraft befindliche Version. [KoSIT führt am 6. November 2026 XRechnung 3.0.2 mit dem technischen Bundle vom 31. August 2026](https://xeinkauf.de/xrechnung/versionen-und-bundles/); eine veröffentlichte Vorversion von XRechnung 4.0 begründet keine sofortige Umstellung.

## 2. Eingaben

Verwenden Sie den bestätigten Rechnungsdatensatz, seine Belegmatrix und die Empfängervorgaben. Benötigt werden außerdem eine tatsächlich unterstützte Erzeugungssoftware sowie das passende lokale Schema- und Regelpaket. Prüfen Sie vorhandene Werkzeuge und ihre Anleitung, bevor Sie dieselben Komponenten nachfordern oder einen Aufruf erfinden.

## 3. Ablauf und Checkliste

### 3.1 Fachliche Freigabefähigkeit prüfen

Kontrollieren Sie Parteien, Nummer, Ausstellungsdatum, Leistungszeit, Positionen, Mengen, Einheiten, Steuerkategorien, Summen, Zahlbetrag und Zahlungsdaten. Übernehmen Sie elektronische Adressen nur zusammen mit ihrem zutreffenden Kennungsschema. Prüfen Sie Käuferreferenz und gegebenenfalls Leitweg-ID anhand der Empfängervorgabe. Fehlende Angaben werden konkret erfragt und nicht durch Beispielwerte ersetzt.

### 3.2 Syntax und Regelpaket abstimmen

Wählen Sie die unterstützte UBL- oder CII-Syntax mit richtigem Profil, Namespace und Standardkennungen. Ordnen Sie alle fachlichen Angaben den richtigen Business Terms zu. Eine CII-Datei für ein anderes Profil ist nicht schon deshalb eine XRechnung. Versionsnummern und Profilkennungen dürfen nicht unabhängig vom tatsächlichen Regelwerk geändert werden.

### 3.3 XML erzeugen

Nutzen Sie das dokumentierte Werkzeug unter `werkzeuge/` oder eine geeignete vorhandene Rechnungsanwendung. Erzeugen Sie in einem neuen Ausgabeverzeichnis. Bewahren Sie Quellen und frühere Fassungen unverändert und vermeiden Sie unbemerkte Überschreibungen. Eine im Vorgang vorliegende E-Rechnung wird nicht ohne Identitäts- und Korrekturprüfung als zusätzliche neue Rechnung fakturiert.

### 3.4 Tatsächlich validieren

Prüfen Sie die endgültige XML-Datei gegen das zur Syntax gehörende XML-Schema und die passenden EN-16931- und XRechnung-Geschäftsregeln. Verwenden Sie eine nachvollziehbar versionierte KoSIT-Konfiguration. Ein erfolgreicher XML-Parser oder XSD-Lauf allein genügt nicht. Laden Sie keine externen XML-Entitäten oder Dokumentreferenzen aus unkontrollierten Eingaben nach.

Lesen Sie den Bericht einschließlich Fehlern und Warnungen. Korrigieren Sie den fachlichen Datenstand beziehungsweise die Abbildung und erzeugen Sie neu. Prüfen Sie die neue Datei erneut. Unterdrücken Sie keine Regel allein, damit ein grüner Status entsteht. Falls ein Validator fehlt, bezeichnen Sie den Stand ausdrücklich als noch nicht vollständig validiert und benennen die fehlende Komponente.

### 3.5 Inhalt und Darstellung zurückvergleichen

Lesen Sie Identitäten, Rechnungsnummer, Referenzen, Währung, Positionen, Steuergruppen, Summen und Zahlbetrag aus dem erzeugten XML zurück. Vergleichen Sie sie mit dem bestätigten Datensatz. Für eine Lesefassung nutzen Sie eine vertrauenswürdige aktuelle Visualisierung oder eine eigene sichere Darstellung ohne aktive Inhalte. KoSIT führt einen gesonderten Visualisierungs-Hotfix vom 13. Oktober 2026; ein aktueller Validator aktualisiert eine alte Visualisierung nicht automatisch.

### 3.6 Übergabe und Empfang trennen

Liefern Sie XML und Prüfbericht. Eine optionale Lesefassung wird als solche bezeichnet. Behaupten Sie weder Portalannahme noch Versand aus dem lokalen Validierungsergebnis. Eine tatsächlich beauftragte Übermittlung benötigt zusätzlich den bestätigten Zugang und einen verifizierten Übermittlungsnachweis.

## 4. Quellenpflicht

Es gilt `references/zitierweise.md`. Dokumentieren Sie [KoSIT-Version und Bundle](https://xeinkauf.de/xrechnung/versionen-und-bundles/), [Sommer-Bugfix 2026](https://xeinkauf.de/aktuelles/xrechnung/xrechnung-bugfix-summer-2026/), die tatsächlich verwendeten Prüfarbeitsmittel und Empfängerregeln. Der Bugfix enthält Validator 1.6.3 und aktualisierte Validierungsartefakte. Bei einem späteren Einsatz prüfen Sie Fortentwicklung und Kompatibilität neu. Normative Grundlage ist [§ 14 Abs. 1 UStG](https://www.gesetze-im-internet.de/ustg_1980/__14.html); konkrete technische Konformität folgt aus dem tatsächlichen Prüflauf.

## 5. Ausgabeformat

Geben Sie die fertige XML-Datei, den maschinenlesbaren oder lesbaren Prüfbericht und eine kurze Übergabenotiz aus. Die Notiz enthält Standard, Syntax, Version, Profil, Regelpaket, Dateiprüfsumme, Ergebnis und etwaige verbleibende Warnungen. Halten Sie fachliche Prüfung, technische Validierung und Empfangsstatus auseinander.

Die Ausformulierungspflicht gilt für Hinweise und Begleittexte: vollständige Sätze, keine Textskelette. Formatierte Begleitdokumente verwenden, soweit technisch möglich, Times New Roman 11 pt und dezimale Gliederung. XML und technische Berichte folgen ihren vorgegebenen Formaten.

## 6. Beispiele

Eine XRechnung ist XML-syntaktisch gültig, enthält aber keine erforderliche Käuferreferenz. Beschaffen Sie die richtige Angabe und erzeugen Sie neu. Meldet der KoSIT-Bericht danach Annahme, dokumentieren Sie diese lokale Prüfempfehlung; ein Portaleingang ist damit noch nicht erfolgt.

Ein Besteller möchte eine Rechnung und eine Vorschau. Erzeugen Sie das XML und eine daraus abgeleitete Lesefassung. Prüfen Sie beide gegen denselben Datenstand, damit die Vorschau keinen anderen Zahlbetrag zeigt.
