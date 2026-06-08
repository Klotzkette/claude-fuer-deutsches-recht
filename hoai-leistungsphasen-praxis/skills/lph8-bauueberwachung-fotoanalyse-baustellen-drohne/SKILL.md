---
name: lph8-bauueberwachung-fotoanalyse-baustellen-drohne
description: "Methodikskill HOAI LPH 8 — Strukturierter für die Fotoanalyse von Baustellen mit Drohnen DJI Mavic 3 Enterprise und Matrice 300 RTK. Umfasst Flugplanung nach LuftVO Kap. 4, Orthofoto-Erstellung mit Pix4Dmapper und DroneDeploy, Rissdetektionsauswertung, Soll-Ist-Vergleich mit BIM-Modell in BIM360, thermische Analyse Zenmuse XT2 sowie Integration in PlanRadar und SAP PM für Mangelmanagement bei Bauueberwachung im Hoai Leistungsphasen Praxis: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Fotoanalyse Baustellen-Drohne in der Bauueberwachung LPH 8

## Arbeitsbereich

Methodikskill HOAI LPH 8 — Strukturierter für die Fotoanalyse von Baustellen mit Drohnen DJI Mavic 3 Enterprise und Matrice 300 RTK. Umfasst Flugplanung nach LuftVO Kap. 4, Orthofoto-Erstellung mit Pix4Dmapper und DroneDeploy, Rissdetektionsauswertung, Soll-Ist-Vergleich mit BIM-Modell in BIM360, thermische Analyse Zenmuse XT2 sowie Integration in PlanRadar und SAP PM für Mangelmanagement bei Bauueberwachung. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

Drohnenbefliegungen sind zum unverzichtbaren Werkzeug der Bauueberwachung geworden: Sie ermöglichen die flaechendeckende Dokumentation grosser Baustellen in wenigen Stunden, decken Maengel auf, die vom Boden aus unsichtbar sind, und liefern massstabstreue Orthofotos für As-Built-Dokumentation und Aufmass. Dieser Skill beschreibt den vollstaendigen von der Flugplanung bis zur SAP-PM-Meldungserstellung.

## Bauwerk und Auftrag

- Windpark Neubau Nordsee-Kuestenanlagen: 12 WEA, Fundamentbetonage Orthofotos, Setzungsmonitoring, 18 Befliegungen ueber 14 Monate, Auftraggeber Energiekonzern
- Hochhaus-Rohbau Frankfurt 24 Geschosse: Monatliche Orthofoto-Befliegung für Baufortschritts-Dokumentation und Aufmass-Abgleich, Bausumme 42 Mio. EUR
- Klaeranlage Neubau Bielefeld: Thermografie-Befliegung Dichtheitskontrolle Beckenwand nach Erstbefuellung, Hotspot-Auswertung

## Erste Schritte zur Befliegung

1. Flugplanung und Genehmigung: NOTAM-Pruefung airspace.droniq.de, Luftraum-Klasse C oder D bedarf Genehmigung LBA, BVLOS-Betrieb Sondergenehmigung, Koordination mit Bauleiter
2. Kalibrierung Drohne: IMU-Kalibrierung DJI Mavic 3 Enterprise vor Erstflug, RTK-Basisstation Leica GS18 aufstellen und kalibrieren, GCP-Punkte Ground Control Points einmessen Tachymeter EPSG 25832
3. Flugmission planen: DJI Pilot 2 App, Ueberlappung Frontal 80 Prozent, Seitlich 70 Prozent, Flughoehe 80-120 m, GSD 2 cm/px für Risserkennung
4. Flug durchfuehren: Kontinuierliche Sichtverbindung, Sicherheitsabstand Personen 30 m, Dokumentation Fluganfang und Ende, Wetterbedingungen Wind kleiner 10 m/s
5. Prozessierung Pix4Dmapper: Import Fotos und GCP-Koordinaten, Orthofoto-Generierung, Punktwolke Dense Cloud, Genauigkeitsbericht GSD und GCP-Residuen
6. Auswertung und Reporting: Orthofoto in BIM360 importiert, Soll-IFC-Modell ueberlagert, Abweichungen markiert, Export PlanRadar Meldungsliste

## Normen und Rechtsrahmen

- § 650p BGB, § 650q BGB: Ingenieurvertrag, Dokumentationspflicht Bauueberwachung LPH 8
- HOAI 2021 § 34 Anlage 10 LPH 8: Bauueberwachung Grundleistungen und Besondere Leistungen Aufmass
- LuftVO 2021 Kap. 4 §§ 21a-21i: Drohnenbetrieb Kategorien offen, spezifisch, zertifiziert, Genehmigungen
- DSGVO und BDSG: Personenbezogene Fotos Baustelle, Einwilligung Arbeitnehmer, Datenschutz-Folgeabschaetzung bei Luftaufnahmen Wohngebiete
- VOB/B § 4 Abs. 3: Bauueberwachungspflicht, Dokumentation als Nachweis ordnungsgemaesse Leistungserbringung
- DIN 18202 Toleranzen im Hochbau: Grenzwerte Soll-Ist Vergleich aus Orthofoto, Massstab und Messgenauigkeit

## Prueferaster und Kontrollpunkte

1. GCP-Punktgenauigkeit: Residuen nach Pix4Dmapper Bericht kleiner 2 cm horizontal und 3 cm vertikal, andernfalls Neubefliegung oder GCP nachbessern
2. GSD-Wert Kontrollmessung: Massstabsbalken im Orthofoto, Strecke bekannter Laenge auf Baustelle gemessen, Abweichung kleiner 1.5 Prozent
3. Orthofotos vollstaendig: Keine Luecken im Kachelmosaik, nahtlose Verbindung Einzelfotos, Randbereich 10 m Ueberlappung mit Baustellen-Grenze
4. Thermografie-Auswertung: Temperaturskala kalibriert, Emissionsgrad Material eingegeben, Hotspot definiert als Temperaturunterschied groesser 2 K zu Umgebung
5. BIM-Vergleich: IFC-Modell Koordinate stimmt mit Orthofoto ueberein, Einmesstieferenz-Punkte GCP mindestens 4 verwendet
6. PlanRadar-Import: Meldungen mit Drohnenfoto importiert, GPS-Koordinate automatisch, Bauleiter benachrichtigt

## Foto-, Video- und Dokumentenanalyse

- DJI Mavic 3 Enterprise: 4/3 CMOS Sensor 20 MP, RTK-Modul 1 cm Genauigkeit, Multispektral-Version für Vegetation-Index Messung
- DJI Matrice 300 RTK mit Zenmuse P1: 45 MP Vollformatsensor, Mehrfachkameraversionen, Windwiderstand Stufe 7 Beaufort
- Pix4Dmapper Photogrammetrie-Software: Orthofoto, DSM, Punktwolke, Volume-Berechnung Aushubmassen
- DroneDeploy Cloud-Plattform: Automatische Missionplanung, Echtzeit-Kachelverarbeitung, BIM-Overlay-Feature
- Sitemark Thermografie-Auswertung: KI-gestuetzte Hotspot-Erkennung, automatische Report-Generierung PDF

## Meldungserstellung im ERP / SAP

- SAP PM Meldungsart M2 Drohnen-Befund: Equipment-Nr Bauabschnitt-ID, Schadenscode aus Foto-Auswertung, GPS-Koordinate im Meldungstext
- PlanRadar Drohnen-Layer: Orthofoto als Hintergrundkarte hochgeladen, Meldungen automatisch GPS-verortet auf Orthofoto
- BIM360 RFI-Prozess: Drohnenfoto als Anhang an RFI-Formular, Soll-Ist-Vergleich mit IFC-Modell-Screenshot, Empfaenger AN-Bauleiter
- SAP PS Aufmass-Import: Volumenberechnung Pix4D als CSV, Import Mengen in Vorgaenge Netzplan, Abgleich Aufmassrechnung
- Workflow: Drohnenbefliegung, Orthofoto Pix4D, Auswertung, PlanRadar-Meldung, Bauleiter informiert, AN-Stellungnahme T+3, Massnahme, Nachbefliegung

## Typische Fallstricke

- Flug ohne NOTAM-Pruefung: Luftraumverletzung bussgeldbewehrt bis 50.000 EUR nach LuftVO § 21h
- GCP-Messung ungeprueft: Schlechte GCP-Residuen liefern fehlerhaftes Orthofoto, Soll-Ist-Abweichungen verfaelscht
- Wetterbedingung Wind zu stark: DJI Mavic 3 bei Wind groesser 10 m/s unzuverlaessig, Fotos verwackelt, Orthofoto-Qualitaet ungenügend
- Thermografie-Emissionsgrad falsch: Beton-Emissionsgrad 0.9 statt Metall 0.3, Temperaturanzeige komplett falsch, Fehlinterpretation

## Output

Orthofoto-Mosaik GeoTIFF mit Koordinatensystem EPSG 25832. Pix4Dmapper Genauigkeitsbericht mit GCP-Residuen und GSD. Volumenberechnung Aushubmassen CSV. Thermografie-PDF-Bericht je Befliegung. PlanRadar-Meldungsliste aus Drohnenauswertung. SAP-PM-Meldungen mit GPS-Koordinate und Drohnenfoto. Befliegungsprotokoll Datum, Drohne, Pilot, Wetter.

## Hinweise zur Qualitaetssicherung

- Alle Abnahmeprotokolle muessen vom Bauueberwacher und dem ausfuehrenden Unternehmen unterschrieben sein
- Fristen nach VOB/B § 13 Abs. 4: Maengelansprueche Bauwerk 4 Jahre, Gesamtwerk nach BGB § 634a 5 Jahre
- Bauwerksbuch nach HOAI Anlage 10 LPH 9 wird durch Bautagebuecher LPH 8 vorbereitet

## Quellen

- [HOAI 2021 § 34 Anlage 10](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [LuftVO § 21a Drohnenbetrieb Kategorien](https://www.gesetze-im-internet.de/luftvo_2015/__21a.html)
- [§ 650q BGB Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650q.html)
- [BGB § 634 Maengelansprueche](https://www.gesetze-im-internet.de/bgb/__634.html)
- [VOB/B § 4 Ausfuehrung](https://www.gesetze-im-internet.de/vob/)
