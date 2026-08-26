---
name: lph8-bauueberwachung-rechenzentrum-rz-klima
description: "Für Bauüberwachung Rechenzentrum RZ-Klima (LPH 8): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Bauueberwachung Rechenzentrum RZ-Klima (LPH 8)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: HOAI Paragrafen 1 bis 13 sowie nur das einschlägige Leistungsbild für Gebäude und Innenräume nach Paragraf 34, Freianlagen nach Paragraf 39, Ingenieurbauwerke nach Paragraf 43, Verkehrsanlagen nach Paragraf 47, Tragwerksplanung nach Paragraf 51 oder Technische Ausrüstung nach Paragraf 55; Architekten- und Ingenieurvertrag nach BGB Paragrafen 650p bis 650t. VOB/B nur anwenden, wenn sie wirksam vereinbart und für die konkrete Bauleistung einschlägig ist.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Rechenzentren der Tier-Klassen I bis IV nach Uptime Institute benoetigen ausfallsichere Infrastruktur.
Die Bauueberwachung nach HOAI LPH 8 prüft Kuehlredundanz, Stromversorgungsredundanz und Brandschutz-Loeschanlagen.
Messgroessen wie PUE (Power Usage Effectiveness) und DCIE werden durch korrekt installierte Messtechnik sichergestellt.

## Bauwerk und Auftrag

- Rechenzentrum Tier III, 2000 qm Serverflaeche, Frankfurt, Colocation-Betreiber, 25 Mio. Euro Investition
- Unternehmens-RZ 500 qm, Bayern, Bank, redundante Kuehlsysteme 2N, Notstromaggregat 1000 kVA
- Edge-Rechenzentrum Container-RZ 3 Module, Hamburg, Telekommunikationsunternehmen, 3 Mio. Euro

## Erste Schritte auf der Baustelle

1. Untergrundpruefung Traglast: Bodenbelastung Serverracks bis 12 kN/m, Bodenplatten-Nachweis Statik
2. Doppelbodenmontage: Höhe 60 cm für Kabeltrassen, Trittfestigkeit 4.5 kN nach EN 12825
3. Kuehlsystem Prazisionsklimatisierung: CRAC/CRAH Aufstellung, Kuehlwasserleitungen Druckpruefung
4. USV-Anlage: Inbetriebnahme-Protokoll, Batterietestlauf 100 Prozent Last, Umschaltzeit kleiner 10 ms
5. Gasloesch-System: Inert-Gas FM-200 oder Novec 1230, Aktivierungstest, Leckrate-Prüfung nach EN 15004
6. Physische Sicherheit: Zutrittskontrollsystem, Videoanlage, Mantraps, Kaefigabtrennungen Serverflaeche

## Normen und Rechtsrahmen

- HOAI 2021 § 34 Anlage 10 LPH 8 Grundleistungen
- § 650p BGB Architektenvertrag, § 650q BGB Kuendigung
- ASHRAE TC 9.9 Thermal Guidelines Data Centers: Zulassige Betriebstemperaturen Klasse A1-A4
- DIN EN 15004-1 Gasloesch-Anlagen: Halogenkohlenwasserstoffe, Auslegung, Prüfung
- DIN EN 50173 Informationstechnik: Anwendungsunabhaengige Kabelanlagen
- EN ISO IEC 27001 IT-Sicherheitsmanagement: Anforderungen physische und umgebungsbezogene Sicherheit

## Prüferaster und Kontrollpunkte

1. Kuehlwassersystem: Druckpruefung 1.5-fach Betriebsdruck, keine Undichtheiten, Protokoll je Kreislauf
2. Doppelboden Belastungstest: 4.5 kN Punktlast je Feld, Einfederung kleiner 3 mm, Messprotokoll
3. USV-Batterietest: Spannungsmessung je Zelle, Kapazitaetstest 100 Prozent Last bis Untergrenze
4. Gasloesch: Konzentrationsmessung Loeschangent nach Aktivierung, Haltezeit min. 10 Minuten
5. Zutrittskontrolle: Funktionstest je Lesegeraet, Protokoll Badge-Lese-Zeiten, Alarmausloesung
6. Kabeltrassen: Einzug strukturiert, Biegeradien eingehalten, Schirmung Datenleitungen nach EN 50173

## Foto-, Video- und Dokumentenanalyse

- BIM360 Coordination RZ: IFC-Modell mit Serverflaechen, Kuehlpfad, Kabeltrassen, Clash-Detection
- Drohnenflug Dach RZ: Kuehlturm-Position, Kabelschraenke aussen, Notstromaggregat-Aufstellung
- Prüfprotokolle Kuehlwasser: Druck vs. Zeit-Graph, Temperatur, Kuehlmittelzusammensetzung
- Foto Gasloesch-System: Duesen-Positionen, Raumversiegelung, Deckendurchdringungen abgedichtet
- USV-Testprotokoll: Lastprofil, Spannungseinbruch, Batteriedauer, Umschaltzeit mit Zeitstempel

## Meldungserstellung im ERP / SAP

- SAP PM EAM Rechenzentrum: Equipment-Hierarchie Kuehlanlage/USV/Gasloesch, Wartungsplaene
- SAP PM Meldung M1 kritisch: Ausfall Kuehlsystem, Equipment-Nr., Prioritaet 1-Sofort, Eskalation
- BIM360 Field: Mangel-Markup an 3D-Bauteilgruppe, Verantwortlicher, Faelligkeitsdatum
- ServiceNow oder SAP PM Integration: Incident Ticket bei Betrieb, Verknuepfung Mangel-Bauphase
- Nevaris oder RIB iTWO: Schlusskosten RZ-Ausbau, Gewerk-Abrechnung TGA/IT-Infrastruktur/Sicherheit

## Typische Fallstricke

- Kuehlredundanz unterschaetzt: Ein Ausfall Kuehlsystem ohne Redundanz fuehrt zu Server-Notabschaltung
- Gasloesch-Konzentration zu gering: Loeschwirkung unzureichend, Brand breitet sich aus
- USV-Batterie unterdimensioniert: Testlauf zeigt Kapazitaet unter Anforderung, Nachruesten teuer
- Doppelboden-Traglast ueberschritten: Rackgewicht ue12 kN/m, Bodenplatte versagt, Betrieb unmoeglich

## Quellen

- [HOAI 2021 § 34](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [DIN EN 15004 Gasloesch-Anlagen](https://www.gesetze-im-internet.de/)
- [DIN EN 50173 Kabelanlagen](https://www.gesetze-im-internet.de/)
- [ATEX-Richtlinie 2014/34/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014L0034)
- [DIN EN ISO 13849 Sicherheit Steuerungen](https://www.gesetze-im-internet.de/)
