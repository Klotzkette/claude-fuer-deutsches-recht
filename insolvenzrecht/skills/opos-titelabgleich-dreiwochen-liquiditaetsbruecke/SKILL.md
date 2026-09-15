---
name: opos-titelabgleich-dreiwochen-liquiditaetsbruecke
description: Überführt offene Posten, streitige Vollstreckungstitel und Bankbewegungen in eine abgestimmte Dreiwochen-Liquiditätsbrücke mit neuen Fälligkeiten. Für widersprüchliche Krisendaten und konkrete Statuskorrekturen, nicht für Insolvenzplan oder Forderungsanmeldung.
---

# 1. Zweck und Anwendungsfall

Stimme widersprüchliche Offene-Posten-Listen mit Titeln, Fälligkeiten und tatsächlicher Liquidität ab. Eine falsche Einzelposition kann die Krisenentscheidung und Organhaftung verändern. Anders als `zahlungsunfaehigkeit-pruefung-17-inso` steht die dokumentierte Überleitung der Buchhaltungsdaten in eine Dreiwochenrechnung im Mittelpunkt, die Zu- und Abflüsse bei Zahlungsmitteln und Verbindlichkeiten aufeinander abgestimmt erfasst; kein weiteres allgemeines Insolvenzreife-Gutachten.

## 2. Eingaben

Lies stichtagsbezogene OP-Listen, Konten, freie Kreditlinien, Rechnungen, Zahlungsvereinbarungen, Titel, Zustellungen, Vollstreckungsmaßnahmen und gesicherte Zuflüsse. Erfasse Rechtsträger, Rolle, Stichtag, Datenstand, Beurteilungszweck und bereits laufende Pflichten. Eine gebündelte Rückfrage bei entscheidenden Lücken, dann Teilrechnung mit klarer Unsicherheit. Originaldaten niemals überschreiben.

## 3. Ablauf und Rechenlogik

1. Gib jedem Posten eine ID. Überleitung: Buchbetrag, Dublette, Gutschrift, bereits bezahlter Teil, objektiver Bestand, Fälligkeit, Einforderung, Stundung, Titel und Vollstreckungsstand. Verbinde jede Korrektur mit Beleg, Datum und Begründung. Bloßes Bestreiten ist kein Streichungsgrund und Prozessrisiko kein pauschaler Bewertungsabschlag.
2. Bei streitigem vorläufig vollstreckbarem Titel prüfe Vollstreckungsvoraussetzungen und tatsächlich eingeleitete Vollstreckung. Bei erfüllten Voraussetzungen den Nennwert ansetzen. Bei Einstellung oder Änderung der Vollstreckung neu prüfen, nicht automatisch null setzen. Untitulierte streitige Forderungen anhand objektiver Rechtslage bewerten; ungelöste Rechtsfragen in getrennten vollständigen Szenarien zeigen.
3. Trenne sofort verfügbare Mittel von gebundenen Konten, bereits ausgeschöpften Linien und bloß erhofften Krediten. Eigene Forderungen nicht mit Nennwert als Bargeld behandeln. Zusage, Abrufbedingungen, Verfügbarkeit und Zuflussdatum dokumentieren.
4. Erstelle den Anfangsstatus: verfügbare Mittel gegen am Stichtag fällige Verbindlichkeiten. Danach Dreiwochenbrücke: Anfangsmittel plus gesicherte Zuflüsse gegen Anfangsverbindlichkeiten plus im selben Zeitraum neu fällige und eingeforderte Verbindlichkeiten. Zeige daneben die zeitliche Verteilung. Bei Fortschreibung vermindert eine Zahlung Zahlungsmittel und offenen Posten; in der kumulierten Bedarfsrechnung nicht dieselbe Zahlung nochmals abziehen.
5. Berechne Deckung und Lücke und weise den Nenner ausdrücklich aus: Lücke geteilt durch den jeweiligen Gesamtbedarf, nicht durch Aktiva. Nullbedarf gesondert behandeln. Kontrolliere Summen, negative Bestände, doppelte Mittel und Stichtagssprünge. Eine spätere Zahlung ist im rückblickenden Beweisfall relevant, aber nicht automatisch bereits am Stichtag sicher prognostizierbar.
6. Würdige Zahlungseinstellung eigenständig. Ein rechnerisch günstiger Endtag beseitigt weder frühere Insolvenzreife noch Organpflichten automatisch. Keine starre Entwarnung aus einem einzelnen Prozentwert; Reichweite der gewählten Methode und fehlende Daten nennen. Überschuldung und drohende Zahlungsunfähigkeit getrennt halten.
7. Bei möglicher Antragspflicht unverzüglich Entscheidung und Prüfung durch die verantwortliche Person anstoßen. Dreiwochenhöchstfrist ist keine freie Wartezeit. Keine Zahlung priorisieren oder ausführen, keinen Antrag stellen und keine Stundung vereinbaren.

## 4. Quellenpflicht

Am 14.09.2026 geprüft: [Paragraf 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html), [Paragraf 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html).

BGH, Urteil vom 23.01.2025, Az. IX ZR 229/22, [amtlicher Leitsatz](https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Art=en&Blank=1.pdf&Datum=Aktuell&Gericht=bgh&Sort=12288&anz=1152&nr=140413&pos=16): Nennwert bei erfüllten Vollstreckungsvoraussetzungen und eingeleiteter Vollstreckung. BGH, Urteil vom 19.12.2017, Az. II ZR 88/16, [amtliche Entscheidung, Leitsatz 2](https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Blank=1&Datum=2017-12-19&Gericht=bgh&Sort=6&anz=26&nr=43965&pos=13): Neue Fälligkeiten innerhalb des Dreiwochenzeitraums gehören in die Liquiditätsbilanz. Die damalige Haftungsnorm nicht ungeprüft auf heutige Zahlungen übertragen.

Bei Verwendung zeitlich maßgebliche Rechtslage prüfen. Gericht, Entscheidungsform, Datum, Aktenzeichen, URL und belegte Passage nennen; die [Zitierweise](../../references/zitierweise.md) ist optional ergänzend. Nur verifizierte Passagen zitieren, keine Literatur aus Erinnerung.

## 5. Ausgabeformat

Erstelle `ergebnis.md` mit Sachverhalt, OP-Überleitung, Titelprüfung, Anfangsstatus, Dreiwochenbrücke, Gegenrechnung und ausformulierter Entscheidungsvorlage mit Eskalationsbedarf. Vollständige Sätze, keine Gutachtenskelette; jede Zahl mit Quelle und Stichtag. Exportstandard: Times New Roman, 11 pt, dezimal. Datenstand und Freigabevorbehalt nennen.

## 6. Beispiel

„Die Buchhaltung hat einen bestrittenen Vollstreckungstitel gelöscht und künftige Löhne nicht berücksichtigt. Prüfen Sie die Überleitung und ob die angekündigten Geldeingänge die Lücke tatsächlich schließen.“
