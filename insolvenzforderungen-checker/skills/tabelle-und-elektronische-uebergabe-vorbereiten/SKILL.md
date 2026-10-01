---
name: tabelle-und-elektronische-uebergabe-vorbereiten
description: Überführt begründete Prüfvorschläge in einen abgestimmten Tabellenentwurf und eine kontrollierte Übergabemappe. Trennt interne JSON-, CSV- und XML-Arbeitsdaten von schema- und zielgerichtsgeprüftem XJustiz mit PDF-Unterlagen; verlangt manuelle Freigabe.
---
# 1. Tabelle und elektronische Übergabe vorbereiten

## 1. Zweck und Anwendungsfall

Bereite die Tabelle fachlich vollständig vor, ohne Feststellung, Schemafähigkeit oder gerichtlichen Eingang zu simulieren. Der Export ist eine technische Abbildung bereits geprüfter Entscheidungen, kein Ersatz für deren rechtliche Begründung.

## 2. Eingaben

Verfahrensstammdaten, Einzelanmeldungen, stabile Kennungen, Komponentenrechnung, Rang, Sicherheit, Titel, Prüfvorschlag, tatsächliche Widersprüche und gerichtliche Ergebnisse, zugehörige Belege und Briefentwürfe. Lies vor technischer Arbeit [elektronische-uebergabe.md](../../references/elektronische-uebergabe.md) und die konkrete Zielgerichtsvorgabe.

## 3. Ablauf

1. Originalanmeldung und interne Bewertung getrennt abbilden. Fachlich benötigt werden Gläubiger und Vertreter, Anmeldung und Eingang, Grund, Hauptforderung, Zinsen, Kosten, Gesamtbetrag, beanspruchter und vorgeschlagener Rang, Belege sowie genaue Vorschlagsbegründung.
2. Interne Forderungskennung von gerichtlicher Tabellennummer unterscheiden. Einmal vergebene Zuordnungen nicht durch alphabetisches Sortieren oder Importreihenfolge verändern. Änderungen mit altem und neuem Wert, Grund, Datum und freigebender Person dokumentieren.
3. Prüfvorschlag, tatsächlich erklärte Position des Verwalters und gerichtliches Ergebnis getrennt führen. Widersprüche von Verwalter, einzelnen Insolvenzgläubigern und Schuldner mit Umfang und Datum separat erfassen. Rangbestreiten nicht auf ein einzelnes Betragsfeld reduzieren.
4. Nachrang ohne Aufruf, Masseforderung, Aussonderungsverlangen, mögliche Dublette und noch ungeklärte Forderung in einem nachvollziehbaren Bearbeitungsnachweis erhalten. Nicht als regulär freigegebene Forderung einschleusen, aber auch nicht aus dem Eingangsnachweis verschwinden lassen. Paragraf 175 und notwendige gerichtliche Behandlung eingegangener Anmeldungen beachten.
5. Persönliche Forderung, Sicherungsrecht und Verteilungsdaten nach Paragraf 190 getrennt halten. Eine spätere Verwertungsprognose überschreibt keine historische Anmeldung. Nur tatsächlich eingetretene und rechtlich zutreffend zuzuordnende Befriedigung fortschreiben.
6. Jede Zahl mit Einzelvermerk und Brief vergleichen. Komponenten müssen centgenau zum Gesamtbetrag passen; Streitbeträge dürfen nicht unbemerkt die Anmeldung übersteigen. Auf unbekannte Werte mit offenem Status reagieren, nicht mit künstlicher Null.
7. Der [Exporthelfer](../../scripts/forderungsexport.py) erzeugt interne Ausgaben mit `python3 scripts/forderungsexport.py INPUT.json OUT_DIR` aus dem Pluginverzeichnis. Tatsächliches Eingabeschema und Werkzeugverhalten zuvor lesen. Keine Felder erfinden, die der Export nicht unterstützt, und keinen erfolgreichen Lauf behaupten, wenn er nicht erfolgt ist. Der optionale XJustiz-Weg unterstützt nur die Erstnachricht 0300005, Ereignis 044 ohne Erklärungen, aus einer kontrollierten Vorlage ohne Forderungen. Keine Rollen- oder Vorlagenkennungen erfinden; keine Änderungsnachricht 0300006 oder Feststellungserklärung damit nachbilden.
8. JSON, CSV und ein neutraler XML-Entwurf dienen intern. Für den hier vorgesehenen NRW-XJustiz-Weg PDF-Unterlagen und amtlich spezifiziertes XJustiz-XML gemeinsam vorbereiten; freie XML-Struktur ist kein XJustiz. Zulässige alternative TAB-/ITR-Wege nur nach amtlichen Hinweisen und Zielgerichtsvorgabe behandeln.
9. Am 01.10.2026 ist laut amtlicher Startseite XJustiz 3.6.2 gültig; 3.5.1 ist ausgelaufen, 4.0.0 erst ab 30.04.2027 gültig. Vor realer Übergabe passende Version, Nachrichtentyp, Codelisten, XSD-Prüfung, Dokumentzuordnung und Zielgerichtsanforderungen erneut prüfen. Eine bestandene XSD-Prüfung beweist keine materielle Richtigkeit oder Empfangsbestätigung.
10. Fachliche Freigabe und technische Freigabe dokumentieren. Übermittlung bedarf einer gesonderten manuellen Entscheidung; in diesem Ablauf erfolgt kein automatischer Versand. Gerichtlichen Eingang und späteres Prüfergebnis nur aus tatsächlichen Nachweisen nachtragen.

## 4. Quellenpflicht

Paragrafen 174 bis 179, 183, 188 und 190 InsO; Paragraf 2 eTab InsO NRW und amtliche technische Hinweise. [Rechtsstand](../../references/rechtsstand-und-entscheidungen.md), [Zitierweise](../../references/zitierweise.md), [elektronische Übergabe](../../references/elektronische-uebergabe.md). Gläubigeranmeldung nach Paragraf 174 Absatz 4 nicht mit der Tabellenübergabe an das Gericht verwechseln.

## 5. Ausgabeformat

Abgestimmter Tabellenentwurf mit begründeten Kurzvorschlägen, Dokumentzuordnung und vollständig ausformuliertem Übergabevermerk. Reine Rohdaten, eine Erfolgsmeldung oder ein Skelettvermerk genügen nicht. Brieftexte vollständig ausformulieren. Dokumente soweit möglich Times New Roman 11 pt und dezimale Gliederung; amtliche Formate dürfen begründet abweichen. Fehlende Schema- oder Zielgerichtsvalidierung sichtbar als offene Voraussetzung nennen.

## 6. Beispiele

Ein interner Export enthält dieselben zehn Anmeldungen wie die Prüfmappe. Auch wenn XML technisch lesbar ist, darf die Datei ohne amtliches Schema und Zielgerichtsabgleich nicht „gerichtsfertig“ heißen. Vor einem erst künftigen Prüfungstermin enthalten die Zeilen Vorschläge, keine erfundenen gerichtlichen Ergebnisse.
