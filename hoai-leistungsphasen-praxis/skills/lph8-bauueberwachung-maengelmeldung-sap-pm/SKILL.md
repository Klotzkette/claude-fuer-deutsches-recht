---
name: lph8-bauueberwachung-maengelmeldung-sap-pm
description: "Methodikskill HOAI LPH 8 — Vollstaendiger für Maengelmeldungen in SAP Plant Maintenance PM. Umfasst Meldungsarten M1-M3, Equipment-Nummernstruktur aus Bau-Objektbaum, Schadens- und Ursachencodes nach Normen, Prioritaeten und Faelligkeiten nach VOB/B § 13, Workflows PM-Meldung bis PM-Auftrag mit Ausfuehrungs-Ueberwachung, Integration PlanRadar-SAP-PM via REST-API sowie Abschluss-Meldung und Kostenstellenzuordnung bei HOAI-LPH-8-Projekten im Hoai Leistungsphasen Praxis."
---

# Maengelmeldung und SAP Plant Maintenance in der Bauueberwachung LPH 8

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

SAP Plant Maintenance ist das mächtigste Werkzeug zur strukturierten Mangelverfolgung in Bauprojekten mit Industriebauherren und Betreibern. Die Bauueberwachung in LPH 8 nutzt PM-Meldungen als revisionssicheres Nachweis-System: Jeder Mangel enthaelt Foto, Equipment-ID, Schadenscode, Faelligkeit und Kostenstelle und ist lueckenlos nachvollziehbar bis zur abschliessenden Mangelbeseitigung nach VOB/B § 13.

## Bauwerk und Auftrag

- Pharmafabrik Frankfurt Reinraumausbau: 3.200 PM-Meldungen ueber 24 Monate Bauzeit, Equipment-Baum 850 Positionen, SAP S/4HANA EAM, Bausumme 28 Mio. EUR
- Logistikzentrum Dortmund: SAP PM Integration mit PlanRadar REST-API, automatische Meldungserstellung aus mobiler App, 680 Meldungen
- Klaeranlage Bielefeld: SAP PM mit DIN EN 13306-Schadenscodes für Instandhaltungsplanung nach Abnahme, Uebergabe an Betriebsabteilung

## Erste Schritte SAP PM Einrichtung

1. Equipment-Baum aufbauen: Hoehere Ebene Bauwerk, zweite Ebene Bauteil-Gruppe z.B. Rohbau oder TGA, dritte Ebene Equipment-ID z.B. STUETZE-EG-A04, nach Fliesschema IFC-Objektbaum
2. Meldungsarten konfigurieren: M1 Instandhaltungsanforderung für planmäßige Pruefungen, M2 Stoerungsmeldung für unplanmäßige Maengel, M3 Aktivitaetenmeldung für erledigte Arbeiten
3. Schadenscode-Katalog erstellen: Nach DIN 31051 und DIN EN 13306, Codes K001-K099 Bauwerk, A001-A099 Abdichtung, E001-E099 Elektro, B001-B099 Boden
4. Prioritaetskatalog festlegen: Prio 1 sofortige Sicherheitsmassnahme 24 h, Prio 2 baubetrieblich kritisch T+3, Prio 3 dokumentierter Mangel T+14 nach VOB/B Fristen
5. PM-Auftrag-Abschluss: Meldung MACO Status angelegt, Auftrag erstellt AUFTR, Ausfuehrung gemessen ABGE, Technische Meldung RÜCKG, PM-Auftrag abgeschlossen ABGE
6. Kostenstellen-Zuordnung: Kostenstelle nach Buchungskreis Projekt, PM-Auftrag verknuepft mit PS-Vorgang, Kosten fliessen automatisch in Projektabrechnung

## Normen und Rechtsrahmen

- § 650p BGB, § 650q BGB: Architektenvertrag, Pflicht zur Mangeldokumentation und Verfolgung
- HOAI 2021 § 34 Anlage 10 LPH 8: Grundleistungen Aufstellen und Ueberwachen Maengelliste, Abnahme
- VOB/B § 13 Maengelansprueche: Fristen Maengelbeseitigung, Selbstvornahme, Minderung, Schadensersatz, Verjährungsfristen 4 Jahre
- DIN EN 13306:2018-02 Instandhaltung: Begriffe Schaden, Mangel, Ausfall, Schadensklassen für SAP-PM-Codierung
- DIN 31051:2012-09 Grundlagen der Instandhaltung: Zustandsbeurteilung, Schadensanalyse, Massnahmen
- SAP S/4HANA Enterprise Asset Management: Meldungstypen, Auftragsarten, Funktionsort-Struktur, Schnittstellen

## Prueferaster und Kontrollpunkte

1. Meldungsfeld-Vollstaendigkeit: Equipment-Nr, Meldungsart, Meldungsdatum, Kurzbeschreibung, Schadenscode, Ursachencode, Prioritaet, Kostenstelle, Foto-Anhang
2. Faelligkeits-Kontrolle: Taeglich Auswertung offene Meldungen nach Faelligkeit, Eskalation bei Ueberschreitung Prio-1 an Projektleitung
3. Massnahmen-Protokoll: Jede Massnahme im PM-Auftrag dokumentiert, Ausfuehrender, Datum, Stunden, Materialien, Abschlussfreigabe Bauueberwacher
4. AN-Stellungnahme Frist: VOB/B § 13 Abs. 5 Frist zur Mangelbeseitigung angemessen, Erinnerung automatisch via SAP-T-3 Tage
5. Foto-Pflicht: Mindestens 3 Fotos je Meldung Ueberblick-Detail-Kontext, Aufnahmedatum kongruent zum Meldungsdatum
6. Abschluss-Pruefung: Nachkontrolle Bauueberwacher nach Mangelbeseitigung, Foto Abschluss, technische Meldung SAP PM Status E0004

## Foto-, Video- und Dokumentenanalyse

- PlanRadar-SAP-PM-Integration via REST-API: Meldung PlanRadar automatisch SAP-PM-Meldung M2 erstellt, GPS-Koordinate und Foto uebertragen, bidirektionale Status-Synchronisation
- SAP Fiori App PM Meldung: Mobile Erfassung auf Baustelle, Barcode-Scan Equipment-ID, Offline-Faehigkeit mit Sync bei WLAN
- SAP PM Meldungsliste Auswertung: Offene Meldungen nach Faelligkeit, Schadenscode-Statistik, Kostenstelle Kostenanalyse, Export Excel für Bautagebuch-Anhang
- DALUX BIM-Meldung zu SAP PM: BCF 2.1 aus Dalux zu SAP PM via Middleware, 3D-Koordinate als Meldungsattribut
- SAP PM Auswertung MIGO Statistik: Anzahl Meldungen je Gewerk, durchschnittliche Reaktionszeit AN, Kosten Mangelbeseitigung

## Meldungserstellung im ERP / SAP

- Meldungsart M2 Standard-Prozess: Transaktionscode IW21, Equipment-Nr aus IFC-Baum, Meldungskurztext max. 40 Zeichen, Schadenscode aus Katalog Z001, Ursachencode Z002, Fotos als GOS-Anhang
- Prioritaetssetzung: Prioritaet 1 sofort in Transaktionscode IW72 an Projektleiter weiterleiten, Auto-E-Mail-Benachrichtigung, Eskalations-nach 2 h ohne Reaktion
- Kostenstellen-Buchung: Mangelbeseitigungs-Kosten auf Auftragsart ZM01 Bau-Maengel, automatische Kostenstellenbuchung nach Ausfuehrung und Abschluss PM-Auftrag
- PM-Auftrag aus Meldung: Transaktionscode IW32 Auftrag erstellen, Vorgaenge mit Arbeitsplan und Material-Bedarf, Kapazitaetsplanung Gewerk-Verantwortlicher
- Eskalation: Meldung offen nach Faelligkeit -> automatischer E-Mail Projektleiter -> Nachfrist 48 h -> Eskalation Geschaeftsfuehrer -> VOB-Selbstvornahme-Mahnung

## Typische Fallstricke

- Equipment-Nr falsch: Meldung nicht dem richtigen Bauteil zugeordnet, Kostenstellenbuchung falsch, Nachtraegliche Korrektur aufwaendig
- Schliessen von Meldungen ohne Nachkontrolle: AN gibt Meldung selbst als erledigt, kein Foto Abschluss, Mangel tatsaechlich offen
- Fehlende Kostenstellen-Zuordnung: Kosten landen auf falscher Kostenstelle, Projektabrechnung fehlerhaft
- Zu spaete Meldungserstellung: Mangel erst nach Wochen erfasst, Kausalitaetsnachweis schwierig, VOB-Fristen schon abgelaufen

## Hinweise zur Qualitaetssicherung

- Alle Abnahmeprotokolle muessen vom Bauueberwacher und dem ausfuehrenden Unternehmen unterschrieben sein
- Fristen nach VOB/B § 13 Abs. 4: Maengelansprueche Bauwerk 4 Jahre, Gesamtwerk nach BGB § 634a 5 Jahre
- Bauwerksbuch nach HOAI Anlage 10 LPH 9 wird durch Bautagebuecher LPH 8 vorbereitet

## Quellen

- [HOAI 2021 § 34 Anlage 10](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [VOB/B § 13 Maengelansprueche](https://www.gesetze-im-internet.de/vob/)
- [§ 650q BGB Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650q.html)
- [BGB § 634 Maengelansprueche](https://www.gesetze-im-internet.de/bgb/__634.html)
- [BGB § 640 Abnahme](https://www.gesetze-im-internet.de/bgb/__640.html)

