---
name: lph8-bauueberwachung-bautagebuch-erp-import
description: "Methodikskill HOAI LPH 8 — Bautagebuch-Erstellung und ERP-Import-Workflow. Umfasst Pflichtinhalte Bautagebuch nach HOAI § 34 LPH 8 und BGH-Rechtsprechung, digitale Bautagesbuecher in Nevaris, RIB iTWO und PlanRadar, automatischer Wetter-DWD-API-Import, SAP PS Netzplan-Fortschrittsbuchung aus Baut..."
---

# Bautagebuch und ERP-Import in der Bauueberwachung LPH 8

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Das Bautagebuch ist das wichtigste Dokument der Bauueberwachung: Es beweist Witterungsbedingungen, Personalstaerke, Maschineneinsatz und Baumangel zum jeweiligen Datum. Gerichte stuetzen sich bei Bauprozessen regelmassig auf Bautagebuecher als primaere Beweismittel. Die Bauueberwachung in LPH 8 fuehrt das Bautagebuch taeglich digital und importiert die Daten automatisiert in ERP-Systeme für Projektcontrolling und Abrechnung.

## Bauwerk und Auftrag

- Industrieanlage Leverkusen 36 Monate Bauzeit: 1.080 Tagesberichte digital in Nevaris, automatischer DWD-Import Wetterdaten, Bausumme 42 Mio. EUR, Auftraggeber Chemiekonzern
- Krankenhausneubau Stuttgart: Taeglich digitales Bautagebuch in PlanRadar, SAP PS Fortschrittsbuchung, 18 Monate, Bausumme 68 Mio. EUR
- Windpark Nordsee: RIB iTWO Bautagebuch-Modul, taeglich Fortschritt je WEA Fundament, automatischer SAP PS Export, 14 WEA 22 Monate

## Erste Schritte Bautagebuch digital

1. Software-Auswahl und Einrichtung: Nevaris Build, RIB iTWO oder PlanRadar je nach Projektanforderung und Auftraggeber-Vorgabe ERP-Schnittstelle einrichten
2. Grundstruktur Tagesbericht: Datum, Wetter automatisch DWD API, Temperatur, Niederschlag, Wind, Personalstärke AN je Gewerk, Maschinengeraet, Baufortschritt je Vorgaenge
3. Wetter-API DWD Integration: Kostenloser DWD Open Data API JSON-Format, Stationsauswahl naechste DWD-Station, Import automatisch 8 Uhr morgens
4. Vorgangs-Fortschritt SAP PS: Bautagebuch-Eintrag Vorgangsfortschritt 0-100 Prozent, automatischer Update SAP PS Netzplan-Vorgang, Meilenstein-Trigger
5. Behinderungen dokumentieren: Formular Behinderungsanzeige nach VOB/B § 6, Ursache, Dauer, betroffene Vorgaenge, Kostenscha­etzung Nachtrag, elektronische Signatur eIDAS
6. Tagesabschluss und Freigabe: Bauleiter Gegenpruefung Eintrag, elektronische Unterschrift qualifizierte Signatur, Unveraenderlichkeit nach eIDAS, Archivierung revisionssicher

## Normen und Rechtsrahmen

- § 650p BGB, § 650q BGB: Architektenvertrag, Pflicht zur Bauueberwachungsdokumentation
- HOAI 2021 § 34 Anlage 10 LPH 8: Bautagebuch als Grundleistung, Inhalt und Frequenz Taeglich
- VOB/B § 6 Behinderungen und Unterbrechungen: Behinderungsanzeige Schriftform, Fristen, Kausalitaet
- BGH-Urteil VII ZR 157/13: Bautagebuch als Beweis für Bau-Soll und Ist-Vergleich, Anforderungen Vollstaendigkeit
- eIDAS-Verordnung EU 910/2014: Elektronische Signatur, Qualifizierte Signatur für Rechtssicherheit digitales Bautagebuch
- AHO Heft 9 Leistungen Projektmanagement: Bautagebuch als Informations- und Dokumentationspflicht PM

## Prüferaster und Kontrollpunkte

1. Vollstaendigkeit Pflichtfelder: Datum, Wetter Temperatur Min/Max und Niederschlag, Personalstärke, Maschineneinsatz, Bautaetigkeit, Besonderheiten, Unterschrift
2. Wetter-Daten-Abgleich: DWD-API Import mit Bautagebuch-Eintrag verglichen, Abweichung groeßer 3 Grad Celsius oder 10 mm Regen begruendet
3. Behinderungsanzeige Vollstaendigkeit: VOB/B § 6 Angaben vollstaendig, Zeitpunkt Erkennbarkeit, Behinderungs-Ursache, Einfluss auf Bauzeit, Nachweis durch AN
4. SAP PS Import: Tagesbericht-Daten automatisch in SAP PS Fortschrittsbuchung, Mismatch-Alert bei Abweichung Soll-Ist groesser 10 Prozent
5. Archivierungs-Protokoll: Revisionssichere Ablage eIDAS, Manipulationsschutz Hash-Summe, Loeschsperre mindestens 10 Jahre
6. Lueckenlosigkeit: Kein Werktag ohne Bautagebuch-Eintrag, bei Stillstand-Tagen Eintrag Stillstand mit Ursache

## Foto-, Video- und Dokumentenanalyse

- Nevaris Build Bautagebuch: Modul Tagesberichte, DWD-API-Plugin, SAP-Schnittstelle, eIDAS-Signatur, PDF-Export, Archivierung intern oder Cloud
- RIB iTWO Bautagebuch-Modul: Integration Termin- und Kostencontrolling, Fortschrittsbuchung SAP PS, Behinderungsanzeige-Formular
- PlanRadar Tagesbericht: Mobil aus Baustelle, Foto-Upload, Gewerk-Filter, SAP-Export CSV, Wetter-Autoimport
- DWD Open Data API: Stundenwerte Temperatur, Niederschlag, Wind, Format JSON oder CSV, kostenlos für kommerzielle Nutzung laut DWD-Nutzungsbedingungen
- SAP S/4HANA EAM-Schnittstelle: BAPI Bautagebuch-Import, Vorgangsfortschritt aktualisiert, Meilenstein automatisch gesetzt, KPI-Dashboard Fortschritt

## Meldungserstellung im ERP / SAP

- SAP PS Fortschritt: Transaktionscode CJ20N Projektstruktur, Vorgangs-Fortschritt je Bautagebuch-Import, automatische Terminkontrolle mit Soll-Termin
- SAP PM Meldung bei Behinderung: Equipment-Nr Bauabschnitt, Meldungsart M2 Behinderung, Text VOB/B § 6 Behinderungsanzeige, Fotos und DWD-Protokoll als Anhang
- SAP CO Projekt-Kostenauswertung: Tagesbericht-Stunden fliessen in CO-Kostentraeger, Soll-Ist Vergleich Personalkosten, Prognose Gesamtkosten
- SAP FI Zahlungsfreigabe: Abschlagsrechnung nach Bautagebuch-Fortschritt automatisch vorgeschlagen, Prüfung und Freigabe Projektleiter
- Workflow: Tagesbericht erstellt, Bauleiter Gegenpruefung und Signatur, Import SAP PS automatisch, Meilenstein aktiviert, SAP FI Zahlungsvorschlag generiert

## Typische Fallstricke

- Bautagebuch mehrere Tage nachgeholt: Rechtlich problematisch bei Behinderungsfall, Gericht wertet Nachtraeglichkeit als Indiz für Unzuverlaessigkeit
- Wetterdaten nicht belegt: Nur subjektive Beschreibung, kein DWD-Beleg, Auftraggeber zweifelt Behinderungsanzeige an
- SAP PS Import-Fehler nicht bemerkt: Fortschritt falsch gebucht, Meilenstein fehlerhaft gesetzt, Zahlungsfreigabe blockiert
- Fehlende eIDAS-Signatur: Digitales Bautagebuch ohne qualifizierte Signatur nicht rechtssicher, papierhaft gleichwertig besser

## Hinweise zur Qualitaetssicherung

- Alle Abnahmeprotokolle müssen vom Bauueberwacher und dem ausfuehrenden Unternehmen unterschrieben sein
- Fristen nach VOB/B § 13 Abs. 4: Maengelansprueche Bauwerk 4 Jahre, Gesamtwerk nach BGB § 634a 5 Jahre
- Bauwerksbuch nach HOAI Anlage 10 LPH 9 wird durch Bautagebuecher LPH 8 vorbereitet

## Quellen

- [HOAI 2021 § 34 Anlage 10](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [VOB/B § 6 Behinderungen](https://www.gesetze-im-internet.de/vob/)
- [§ 650q BGB Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650q.html)
- [eIDAS EU 910/2014](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910)
- [BGB § 634 Maengelansprueche](https://www.gesetze-im-internet.de/bgb/__634.html)
