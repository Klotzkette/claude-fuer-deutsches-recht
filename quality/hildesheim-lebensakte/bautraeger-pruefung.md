# Prüfvermerk zur optionalen Bauträgergestaltung

Prüfdatum: 28. September 2026. Fall: SW-HI-26-08. Bearbeitungsgrundlage: fiktive Verkaufsalternative zum 1. November 2027; das Hauptprojekt bleibt ein Vermietungsprojekt.

## Umfang

Der Generator `scripts/bauwirtschaft_hildesheim_lebensakte_recht.py` erzeugt 36 bearbeitbare Word-Dateien mit zusammen 104 gerenderten Seiten und eine CSV-Datei zur Preis- und Ratenkontrolle:

| Bestandteil | Dateien | PDF-Seiten |
| --- | ---: | ---: |
| Acht wohnungsbezogene Bauträgervertragsentwürfe, jeweils 17 Vertragsziffern | 8 | 64 |
| Teilung und Gemeinschaftsordnung; Baubeschreibung; Bemusterungsordnung | 3 | 8 |
| Acht Raum- und Zuordnungslisten sowie acht Raten- und Sicherungspläne | 16 | 16 |
| Entscheidungsvorbereitung, Aufteilungsplanauftrag und Bankanfrageentwurf | 3 | 3 |
| Ausformulierte Word-Mastervorlage für WE01 und fünf Verfahrensvorlagen | 6 | 13 |
| Summe der Word-Dateien | 36 | 104 |

Die Preis-CSV ist eine Kalkulation der nicht beschlossenen Option. Sie ist kein Buchungsjournal und enthält keine tatsächlichen Forderungen, Zahlungen oder Einnahmen. Die acht konkreten Entwürfe enthalten fiktive, wohnungsbezogene Beteiligte; editierbare Eingabefelder befinden sich ausschließlich in den sechs Dateien unter `12_Wordvorlagen/Bautraeger/`.

## Dokumentprüfung

Alle 36 Word-Dateien wurden mit `documents/render_docx.py` und der gebündelten LibreOffice-Laufzeit gerendert. Sämtliche 104 Seiten wurden nach den letzten inhaltlichen Änderungen einzeln in voller Seitendarstellung visuell geprüft. Tabellen, Ratenbeträge, Anlagenlisten und Unterschriftszeilen sind lesbar; die Prüfung ergab keine abgeschnittenen Textblöcke, Überlagerungen oder unerwarteten Leerseiten. Die laufenden Seitenzahlen sind vorhanden. Die Vertragsentwürfe umfassen jeweils acht Seiten.

Ergänzend wurden 1.957 nicht leere und leere Absatz- beziehungsweise Tabellenzellenpositionen aus den DOCX-Dateien erfasst. Jeder nicht leere Text wurde nach Normalisierung von Leerzeichen, Zeilenumbrüchen und Satzzeichen im jeweiligen PDF nachgewiesen. Kopf- und Fußzeilen wurden für den fortlaufenden Textvergleich herausgerechnet; Seitenzahlen wurden gesondert geprüft. Die SHA-256-Werte sämtlicher Quellen stimmen mit den zur Sichtprüfung verwendeten PDF-Ausgaben überein. Alle 36 Quellen sind im Renderindex enthalten.

Lokale Übergabedateien für den Gesamtpaketbau:

- Renderindex mit relativer Quelldatei, SHA-256, absolutem PDF-Pfad, Seitenzahl und PNG-Verzeichnis: `/tmp/hildesheim-lebensakte/recht/render-index.json`.
- Maschinenprüfergebnis: `/tmp/hildesheim-lebensakte/recht/check-results.json`.
- Gerenderte PDFs und vollständige Seiten-PNGs: `/tmp/hildesheim-lebensakte/recht/qa/`.

Diese temporären Pfade sind technische Übergabedaten der Erstellung und keine öffentlichen Downloadlinks.

## Inhaltliche Kontrollen

Die acht fiktiven Gesamtpreise summieren sich auf 3.672.000,00 EUR. Die Miteigentumsanteile ergeben 600/600, die zugeordneten Wohnflächen 600 m². Die sieben MaBV-Teilraten betragen jeweils 30 / 28 / 12,6 / 6,3 / 8,4 / 11,2 / 3,5 Prozent des gesamten Kaufpreises und summieren sich für jede Wohnung exakt zum Einzelpreis. Der fünfprozentige Sicherheitseinbehalt und die anfängliche Auszahlung von 25 Prozent des Gesamtpreises wurden für jede Wohnung gesondert nachgerechnet. Die Rechnungen verwenden Dezimalwerte.

Die Entwürfe unterscheiden allgemeine Fälligkeitsvoraussetzungen, Bautenstand, Bezugsfertigkeit, Besitzübergabe, individuelle Abnahme von Sonder- und Gemeinschaftseigentum sowie vollständige Fertigstellung. Verkäuferfreundliche Regelungen bestehen insbesondere in einer geordneten Ratenstruktur, begrenzten Änderungsfällen, verbindlicher Bemusterung, koordiniertem Baustellenzugang, geregelten Sonderwünschen und gesetzeskonformer Nacherfüllung. Eine künstlich vorverlagerte Schlussratenfälligkeit oder fremdbestimmte Gemeinschaftseigentumsabnahme ist nicht vorgesehen.

Elf amtliche BGH-Entscheidungen wurden im Original mit Datum, Aktenzeichen, tragenden Randnummern beziehungsweise den im Original vorhandenen Seiten und Anwendungsgrenzen geprüft. Normquellen und Entscheidungsnachweise stehen getrennt von den Aktenoriginalen in [rechtsprechung-bautraeger.md](rechtsprechung-bautraeger.md). Insbesondere werden die 2026 entschiedenen Altverträge und ihre Aussagen zur dreißigjährigen Grenze nicht mit der regelmäßigen Mängelverjährung eines heute abgeschlossenen Bauträgervertrags vermischt.

## Grenzen der Option

Es handelt sich um vollständige Verhandlungsentwürfe einer noch nicht beschlossenen Alternative. Weder ein Beurkundungstermin noch eine erfolgte Verlesung, Unterschrift, Siegelung, Grundbucheinsicht, Teilungseintragung, Bankfreistellung oder Kaufpreiszahlung wird als bereits geschehen dargestellt. Die Wohnungsgrundbuchblätter werden erst nach tatsächlicher Anlage eingesetzt. Der Entwurf einer Bankanfrage ist keine Bankzusage. Historische Erwerbsunterlagen der Notarin Dr. Carla Fink bleiben unverändert; Dr. Johann Bauer gehört ausschließlich zur neuen Verkaufsoption.

Vor einer Aktivierung wären insbesondere der Gesellschafterbeschluss, aktuelle Register- und Grundbuchstände, der hinreichend bestimmte behördliche Aufteilungsplan, die Abgeschlossenheit, die Bankfreistellung und die endgültige notarielle Einbeziehung aller Anlagen zu klären. Die Baubeschreibung benennt zusätzliche vereinbarte Schallschutzwerte und einen zweiten Ladepunkt ausdrücklich als Anforderungen der Verkaufsoption. Diese benötigen vor Aktivierung eine technische, genehmigungsbezogene und wirtschaftliche Abstimmung; sie werden nicht rückwirkend als Nachweis der Hauptplanung ausgegeben. Die Preisansätze sind fiktive Übungswerte und keine Marktwertermittlung.

Ein erst nach Vermietung beschlossener Verkauf erfordert eine angepasste Variante unter Berücksichtigung bestehender Mietverhältnisse, Kautionen, gegebenenfalls Vorkaufsrechten und Kündigungssperren. Die hier zugrunde gelegte zeitliche Reihenfolge darf dabei nicht unverändert übernommen werden. Wegen des fiktiven Vertragsstichtags 2027 muss außerdem der seit dem dokumentierten Rechtsstand eingetretene Rechtswandel neu geprüft werden.
