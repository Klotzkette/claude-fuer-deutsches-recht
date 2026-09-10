---
name: messbetrag-und-hebesatz-pruefen
description: Vergleicht festgestellten Grundsteuerwert, separat festgesetzten Messbetrag und den im Jahresbescheid verwendeten Messbetrag. Prüft Promille, Prozent, Hebesatzjahr, Ermäßigungen und Zahlungsraten; macht Übertragungsfehler sichtbar, ohne bindende Grundlagen im falschen Folgebescheid neu zu bewerten.
---

# Messbetrag und Hebesatz prüfen

## 1. Zweck und Anwendungsfall

Finde den ersten Bruch zwischen Wert, Messbetrag und Steuer. Trenne drei Größen: mathematisch errechneter Messbetrag, verbindlich festgesetzter Messbetrag und im Jahresbescheid eingesetzter Messbetrag. Sie dürfen nicht stillschweigend gleichgesetzt werden.

## 2. Eingaben

Lies die drei Verfügungssätze samt Berechnung, Steuerjahr, Grundstücksart, einschlägiger Landesmesszahl und örtlicher Hebesatzregel. Übernimm geleistete Zahlungen nur aus Zahlungsbelegen. Ermäßigungen nicht allein aus einer Alltagsschilderung wie „Altbau“ oder „vermietet“ ableiten.

## 3. Ablauf

### 3.1. Einheiten ausdrücklich rechnen

Grundsteuerwert mal Messzahl in Promille geteilt durch 1000 ergibt den ungerundeten Messbetrag. Der maßgebliche Messbetrag mal Hebesatz in Prozent geteilt durch 100 ergibt die ungerundete Jahressteuer. 0,31 Promille sind nicht 0,31 Prozent. Rechne mit Dezimalzahlen und halte die behördlichen Beträge daneben, statt sie durch die eigene Rundung zu ersetzen.

### 3.2. Bescheidübernahme kontrollieren

Vergleiche Objekt, Stichtag, Messbetrag, Änderungsfassung und Gültigkeitsbeginn. Ein korrekter Rechenweg mit einem fremden oder veralteten Messbetrag bleibt ein Übernahmeproblem. Ein Fehler in der Messzahl ist dagegen auf Messbetragsebene zu verfolgen. Prüfe Befreiung und Messzahlermäßigung mit ihren jeweiligen Voraussetzungen, nicht durch einen frei gewählten Abschlag.

### 3.3. Hebesatz und Zahlung

Prüfe die tatsächlich geltende Hebesatzregel für Gemeinde, Grundstücksart und Steuerjahr einschließlich möglicher Differenzierung. Die Berliner Werte ab 2025 sind nur nach Jahresprüfung zu verwenden. Vergleiche Jahresbetrag, Raten, Fälligkeiten und Vorzahlungen. Eine um wenige Cent abweichende Multiplikation ist zunächst eine Rundungsfrage; benenne die fehlende Rundungsgrundlage. Ein Änderungsbescheid verlangt einen neuen Soll-Ist-Abgleich, keine zweite Vollzahlung.

### 3.4. Rechenhilfe optional einsetzen

Wenn Python verfügbar ist, kann [Rechenabgleich](../../scripts/rechenabgleich.py) mit expliziten JSON-Werten die Rohprodukte und Übernahmedifferenz ausgeben. Er wählt weder Landesrecht noch Rundung und ermittelt keine Fristen. Ohne Laufzeit dieselben Formeln in einer Tabelle rechnen. Ein Werkzeugfehler stoppt nicht den Briefentwurf; keine Installationsschleife.

## 4. Quellenpflicht

Paragrafen 182 und 184 AO, Paragrafen 13 bis 15, 25 und 28 GrStG sowie einschlägiges Landesrecht. Bindungswirkung nach BFH, Beschluss vom 27.05.2024, II B 78/23 (AdV), vom Rechenfehler unterscheiden. [Fachquellen](../../references/grundsteuer-quellen.md), [Zitierweise](../../references/zitierweise.md).

## 5. Ausgabeformat

Liefere Rechenabgleich mit Originalwert, Quelle/Seite, Rohprodukt, abweichendem Bescheidwert und betroffener Stufe. Ergänze das vollständige Überprüfungs- oder Änderungsschreiben mit bestimmtem Ziel. Keine Skelette; Times New Roman 11 pt und dezimale Gliederung bei Textausgabe oder entsprechendem Exporthinweis. Rechenergebnis ist keine Zahlungsfreigabe.

## 6. Beispiele

„Die Jahressteuer verwendet einen anderen Messbetrag als die Rückseite“ führt zum Abgleich der Änderungsstände und erst dann zum Entwurf. „Vier Raten ergeben nicht die neue Jahressumme“ führt zur Prüfung bereits gebuchter Beträge und neu verteilter Restfälligkeiten.
