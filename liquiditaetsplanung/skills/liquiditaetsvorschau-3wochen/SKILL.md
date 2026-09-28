---
name: liquiditaetsvorschau-3wochen
description: "Erstellt eine Dreiwochenplanung und einen belegten Status zur Prüfung der Zahlungsunfähigkeit. Trennt Zahlungsbedarf, Datenlücken, Indizien und rechtliche Bewertung."
---

# 1. Dreiwochenplanung mit taggenauem Insolvenzstatus

## 1.1. Zweck und Anwendungsfall

Erstelle die beauftragte Dreiwochenplanung und, falls verlangt oder wegen konkreter Krisensignale geboten, die rechtliche Prüfung nach § 17 InsO. Eine operative Wochenübersicht, der Stichtagsstatus und die zeitraumbezogene Liquiditätsbilanz sind verschiedene Darstellungen. Ein positiver Wochenendbestand und eine Tabellenfarbe beweisen keine Zahlungsfähigkeit.

## 1.2. Eingaben und gezielte Rückfragen

Lies vorhandene Unterlagen zuerst. Übernimm Firma, Rechtsform, Stichtag, Rolle, Ziel, Format und Datenquelle aus dem Auftrag. Frage nur entscheidende fehlende Angaben nach; keine erneute Format- oder Connectoraufnahme. Ohne Formatvorgabe ist eine bearbeitbare Excel-Tabelle sinnvoll; ohne Exportmöglichkeit liefere eine nachrechenbare Tabelle.

Erfasse frei verfügbare Bank-/Kassenmittel, noch abrufbare Kreditlinien, Forderungseingänge und Verbindlichkeiten jeweils mit Betrag, Fälligkeit, Zahlungszeitpunkt und Beleg. OPOS mit Bankbewegungen, Teilzahlungen, Umsatzsteuer und Factoring abstimmen. Stundung, Titel, Vollstreckung und Einwendungen je Posten festhalten. Unbekannte Beträge nicht als null oder erfundene Worst-Case-Tatsachen einsetzen. Für OCR-Werte Belegstelle und Lesesicherheit kontrollieren.

Dateiimporte etwa aus CAMT, CSV oder DATEV auswerten, soweit technisch möglich. Verbundene Bankzugänge nur verwenden, wenn verfügbar und für den Auftrag autorisiert; keine bestimmte Werkzeugschnittstelle voraussetzen. Geheimnisschutz und zulässige Datenverarbeitung beachten.

## 1.3. Ablauf

### 1.3.1. Zeitraum und Rechnung

Bestimme den tatsächlichen Stichtag und das kalendergenaue Dreiwochenfenster. Keine automatische Verschiebung auf Montag oder Verkürzung auf drei Freitage. Stelle unterwöchige Engpässe dar. Neu fällige Verpflichtungen der ersten Woche gehören ebenfalls in die Zukunftsbetrachtung, soweit sie am Stichtag noch nicht fällig waren.

Für die Bilanzmethode rechne getrennt: Aktiva I = am Stichtag verfügbare Mittel; Aktiva II = belegbare Zuflüsse im ganzen Fenster; Passiva I = am Stichtag fällige und eingeforderte Verpflichtungen; Passiva II = im selben Fenster neu fällige und eingeforderte Verpflichtungen. `Lücke = max(0, PI + PII − AI − AII)`; `Quote = Lücke / (PI + PII)`. Bei Nenner null keine Quote ausgeben. Zahlungen auf Passiva I nicht noch einmal als neue Passiva II zählen. Auch Anfangsliquidität und Kreditabrufe dürfen nur einmal eingehen.

Die Wochenrechnung bleibt `Endbestand = Anfangsbestand + Einzahlungen − Auszahlungen`. Ein negativer Wert bezeichnet offenen Finanzierungsbedarf. Bestehende Rückstände im Status erfassen, auch wenn die Geschäftsleitung ihre Zahlung im operativen Plan nicht vorgesehen hat.

### 1.3.2. Rechtsbewertung und Belege

Wende die vollständige Zehnprozentregel mit Ausnahmen und den eigenständigen Nachweisweg der Zahlungseinstellung aus den [Prüfregeln](../../references/insolvenzpruefung.md) an. BGH IX ZR 123/04 begründet keine automatische Entwarnung unter zehn Prozent; BGH IX ZR 48/21 erlaubt kein Zählen von Warnzeichen. Ein starkes Einzelindiz kann genügen, zwei schwache müssen nicht genügen. Datenvollständigkeit, Rechenergebnis und rechtliches Ergebnis getrennt kennzeichnen.

Eigene Forderungen nur nach belastbarem rechtzeitigem Zufluss ansetzen. Ein eigener Titel macht die Forderung nicht zu Bargeld. Auf der Passivseite nach BGH IX ZR 229/22 Bestand, Fälligkeit und gegebenenfalls Titel samt Vollstreckungsvoraussetzungen und eingeleiteter Vollstreckung prüfen. Bloßes Bestreiten oder ein Prozessrisikoabschlag tragen keine Herausnahme. Eine Vollstreckungseinstellung ändert nicht automatisch den materiellen Bestand der Schuld.

### 1.3.3. Neue Belege und Konsequenzen

Rechne nach Antworten nur die betroffenen Positionen, Folgebestände und Szenarien neu. Bestätigte Stundungen, später bereitstehende Kredite und veränderte Fälligkeiten konkret abbilden. Bleibt eine entscheidende Lücke, benenne die vorläufige Aussage und frage gezielt weiter; kein starres Ende nach einer Rückfrage.

Bei möglicher Insolvenzreife sofort die Voraussetzungen und Höchstfristen des § 15a InsO prüfen. Eintritt und Fristbeginn nicht aus Tabellenfarbe oder Kalenderwoche ableiten. Die Pflicht besteht ohne schuldhaftes Zögern; drei Wochen sind keine allgemeine Wartefrist. § 15b InsO und besondere Zahlungsrisiken einzeln beurteilen. Bei Bedarf in die vertiefte Prüfung mit `liquiditaetsvorschau-insolvenzrechtlich` übergehen; fehlender Zugriff auf einen weiteren Skill verhindert die Prüfung nach den hier verlinkten Regeln nicht.

## 1.4. Quellenpflicht

Maßgeblich sind § 17 und § 15a InsO sowie die amtlich belegten Entscheidungen in der [Entscheidungskarte](../../references/rechtsprechung/INDEX.md), insbesondere IX ZR 123/04, II ZR 88/16, IX ZR 48/21, II ZR 112/21 und IX ZR 229/22. Entscheidungsart, Datum, Aktenzeichen, genaue Aussage und Randnummer beziehungsweise Originalseite prüfen. Fachstandards nur in zugänglicher geprüfter Fassung zitieren; keine erfundenen IDW-Textziffern oder Literaturfundstellen.

## 1.5. Ausgabeformat

Liefere den verlangten Plan mit belegten Eingaben, Formeln, Status-/Bilanzblock, Datenlücken und begründetem Ergebnis. Excel-Vorlage: `assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`; zusätzliches HTML oder Markdown nur entsprechend Auftrag. Nutze die ausdrücklich getrennten Statusfelder; leite sie nicht pauschal aus KW-Summen ab. Vorlagen dürfen zur korrekten zeitlichen Abgrenzung ergänzt werden. Keine Datei behaupten, die nicht erstellt wurde.

Ein bestellter Vermerk wird vollständig ausformuliert, nicht als Stichwortskelett geliefert. Formatierte Texte verwenden Times New Roman 11 pt und dezimale Gliederung; Tabellen bleiben zahlenorientiert. Interne Quellen-/Techniknotizen vom Empfängertext trennen. Versand, Zahlungen oder Einreichung erfordern einen entsprechenden Auftrag.

## 1.6. Beispiel und Kontrolle

Stichtagsmittel 30.500 EUR; am Stichtag fällige Schulden 61.500 EUR; neu fällige Verpflichtungen im vollständig belegten Fenster 22.000 EUR und 17.600 EUR. Bei belegten rechtzeitigen Zuflüssen von 18.000 EUR und 9.500 EUR ergeben sich 58.000 EUR Mittel, 101.100 EUR Verpflichtungen und 43.100 EUR Lücke, also rund 42,63 Prozent. Fällt der Eingang von 18.000 EUR aus, beträgt die Lücke 61.100 EUR. Eine ungeklärte Zahlung nicht künstlich zu 80 Prozent als tatsächlichen Eingang ansetzen.

Diese Zahlen allein sind noch keine abschließende Subsumtion: Verlauf, Vollständigkeit, Schließungsaussichten, Zumutbarkeit und Zahlungseinstellung prüfen. Die Vorlage darf bei leeren Eingaben weder „grün“ noch „zahlungsfähig“ anzeigen.
