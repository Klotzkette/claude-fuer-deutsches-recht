---
name: bauzeitentschaedigung-vorhaltung-und-folgezeiten
description: "Prüft Bauzeitentschädigung wegen fehlender Mitwirkung des Bestellers durch taggenauen Abgleich von Sollablauf, tatsächlicher Vorhaltung und anderweitigem Einsatz. Trennt den Annahmeverzugszeitraum von späteren Kostenfolgen und erstellt eine prüffähige Forderungsbewertung."
---

# 1. Zweck und Anwendungsfall

Bearbeite eine Bauzeitforderung mit gemischten Stillstands-, Vorhalte- und Folgekosten. Hohe laufende Personal- und Gerätekosten und aufwendige Kausalitätsbelege machen dies zu einem geeigneten Schwerpunkt. Gegenüber dem allgemeinen Bauablaufskill liegt der Zusatznutzen in der konkreten Bemessung nach Paragraf 642 BGB, nicht in einer weiteren pauschalen Behinderungsanzeige. Reine Mängel- und Abnahmefragen gehören nicht hierher.

## 1.1. Eingaben

Lies Vertrag einschließlich wirksamer Einbeziehung und Fassung der VOB/B, vereinbarte Termine und Änderungen, Sollplan, Bautagebücher, Mitwirkungsanforderungen, Anzeigen, Leistungsangebote, Personal- und Gerätedisposition, Kalkulation, Rechnungen und Nachträge. Halte Vertragsparteien und tatsächlichen Adressaten jeder Mitwirkungsanforderung auseinander. Projektgeheimnisse nicht öffentlich recherchieren.

## 1.2. Ablauf und Checkliste

1. Rekonstruiere pro Störung die geschuldete oder erforderliche Mitwirkung, Fälligkeit, tatsächliche Bereitstellung, Leistungsangebot und Leistungsfähigkeit des Unternehmers. Prüfe Paragrafen 293 bis 297 BGB. Ein Vertragsbeginn im alten Plan genügt nicht, wenn später verbindlich neue Termine vereinbart wurden.
2. Baue eine Ereignismatrix: ungestörter Vorgang, notwendiger Plan oder Vorleistung, tatsächliches Hindernis, Beginn, Ende, betroffene Ressourcen und Beleg. Prüfe Eigenbehinderung, Parallelstörung, Puffer und mögliche Umstellung. Die Verlängerung des Gesamtprojekts ist nicht automatisch die Dauer des Annahmeverzugs jedes Gewerks.
3. Trenne Anspruchswege: Entschädigung nach Paragraf 642 BGB, gegebenenfalls verschuldensabhängiger Schaden und Vergütung für angeordnete Änderungen. Eine Behinderungsanzeige ersetzt keine Anordnung. Voraussetzungen der VOB/B nur bei einschlägiger Vereinbarung prüfen; keine analoge gesetzliche Anzeigeobliegenheit erfinden.
4. Ordne jeder Ressource je Tag verfügbare, produktive, umgesetzte und unproduktiv bereitgehaltene Kapazität zu. Abrechenbare Tage nicht bloß durch Abzug von Soll- vom Ist-Endtermin bestimmen. Personalkosten auf Ersatzbaustellen und dort gebundene Geräte nicht nochmals als vollständig stillstehend behandeln.
5. Entwickle die Bemessungsgrundlage aus den auf unproduktiv bereitgehaltene Produktionsmittel entfallenden vereinbarten Vergütungsanteilen. Enthaltene allgemeine Geschäftskosten sowie Wagnis und Gewinn kenntlich machen; keine doppelten Zuschläge. Ersparnisse und anderweitige Verwendung nach Paragraf 642 Absatz 2 BGB berücksichtigen. Tatsächliche Kosten dienen als Beleg und Plausibilisierung, sind aber nicht alleiniger gesetzlicher Maßstab. Die Rechnung bereitet die angemessene Entschädigung vor, ersetzt nicht die gebotene Abwägung.
6. Sonderliste für erst nach Ende des Annahmeverzugs angefallene Materialpreissteigerungen, Lohnerhöhungen, Beschleunigung und Wiederanlauf bilden. Nicht automatisch nach Paragraf 642 BGB zuschlagen; andere Anspruchsgrundlage mit eigener Pflicht-, Verschuldens- und Kausalitätsprüfung verlangen. Den Nachweis eines konkreten Kostennachteils nicht als zusätzliche Voraussetzung bereits des Anspruchsgrundes behandeln.
7. Liefere Einzelpositionen als belegt, rechtlich streitig oder nicht quantifizierbar. Keine pauschale 50-Prozent-Quote bei Mitverantwortung. Höchstens eine gebündelte Rückfrage; Teilbewertung, Beleganforderung und Gutachterfragen sofort liefern. Keine Kündigung, Leistungsunterbrechung, Nachtragsbeauftragung oder Einreichung ohne ausdrücklichen Auftrag.

## 1.3. Quellenpflicht

Prüfstand 14.09.2026. Optional ergänzt die [Zitierweise](../../references/zitierweise.md) die Quellenarbeit. Entscheidungen mit Gericht, Datum, Aktenzeichen und überprüfter Fundstelle zitieren. Vertragsfassung und aktuelle Rechtslage fallbezogen amtlich prüfen; Aktenbefund und rechtliche Wertung trennen.

- [Paragraf 642 BGB](https://www.gesetze-im-internet.de/bgb/__642.html): Voraussetzungen und Bemessungskriterien; Paragrafen 293 bis 297 BGB ergänzend für Annahmeverzug.
- BGH, Urteil vom 30.01.2020, Az. VII ZR 33/19, [amtlicher Volltext](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VII_ZS/2019/VII_ZR__33-19.pdf?__blob=publicationFile&v=1), Randnummern 38 bis 42 und 47 bis 51: kein Kostennachteil als zusätzliche Grundvoraussetzung; zeitliche Begrenzung, vergütungsbezogene Vorhaltung und Abwägung statt voller Umsatzkompensation.

## 1.4. Ausgabeformat

Liefere `ergebnis.md` mit Sachverhalt, Störungszeitachse, Ressourcen- und Rechenmatrix, gesonderten Folgepositionen, Gegenargumenten und ausformulierter Anspruchsbegründung oder Erwiderung. Jede Zeile nennt Tage, Menge, Satz, Herkunft, Abzug und Anspruchsweg. Umsatzsteuer nicht pauschal auf jeden Schadens- oder Entschädigungsbetrag aufschlagen; Behandlung gesondert prüfen.

Ausformulierungspflicht und Formatstandard: vollständige Sätze statt Skeletten, Times New Roman 11 pt, dezimale Gliederung mit Leerzeilen; bei Markdown Exporthinweis. Ohne Exportfunktion vollständigen Text ausgeben.

## 1.5. Beispiele

Zehn Arbeitstage fehlen Ausführungspläne; vier Beschäftigte sind an vier Tagen anderweitig eingesetzt, ein Gerät bleibt stehen. Die Personal- und Gerätezeiten erhalten verschiedene Zeilen. Eine Materialverteuerung bei der späteren Ausführung ist eine eigene Position, keine automatische Verlängerung des Entschädigungszeitraums.
