---
name: lph9-gewaehrleistungsmanagement-lph8
description: "Lph9 Gewaehrleistungsmanagement Lph8: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lph9 Gewaehrleistungsmanagement Lph8

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Lph9 Gewaehrleistungsmanagement Lph8** im Plugin HOAI-Leistungsphasen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-lph9-gewaehrleistungsmanagement-fristen` | HOAI-Fachfrage LPH 9: Objektbetreuung, Gewährleistungsfristen, Mängel vor Fristablauf, Begehung, Unternehmerverfolgung, Planerhaftung und Abschlussdokumentation prüfen. |
| `lph8-bauueberwachung-abnahmeprotokoll-foerder-erp` | Methodikskill HOAI LPH 8 — Abnahmeprotokoll-Erstellung fuer oeffentlich geförderte Projekte mit ERP-Schnittstelle. Umfasst Abnahmeprotokoll nach VOB/B § 12 mit Foerderantrag-Konformitaetsnachweis, Verwendungsnachweis BNH und SAP-FI-Buchung, Abnahmeprotokoll-Erstellung in Dalux und PlanRadar, Upload in SAP PS und ELSTER-Foerderprogramme, Teilabnahmen nach Bauabschnitten sowie digitale Unterschrift eIDAS und Integration in Foerderprogramme KfW Bundesfoerderung und EU-EFRE-Richtlinien. |
| `lph8-bauueberwachung-bautagebuch-erp-import` | Methodikskill HOAI LPH 8 — Bautagebuch-Erstellung und ERP-Import-Workflow. Umfasst Pflichtinhalte Bautagebuch nach HOAI § 34 LPH 8 und BGH-Rechtsprechung, digitale Bautagesbuecher in Nevaris, RIB iTWO und PlanRadar, automatischer Wetter-DWD-API-Import, SAP PS Netzplan-Fortschrittsbuchung aus Bautagebuch, Export-Schnittstellen zu SAP S/4HANA Enterprise Asset Management und Revit BIM360 sowie rechtssichere elektronische Signatur nach eIDAS. |
| `lph8-bauueberwachung-bewehrung-verlegekontrolle` | Bauueberwachung HOAI LPH 8 fuer Bewehrungsverlegung — Kontrolle Stabstaehle BSt 500 S und BSt 500 M nach DIN 488, Betondeckung nach DIN EN 1992-1-1 EC2, Stosslaeange und Ankerlaeange, Biegerollendurchmesser, Abstandhalter-Typ und Anordnung nach DBV-Merkblatt Betondeckung. Umfasst Werksbescheinigungen 3.1 nach EN 10204, Stahllager-Pruefung, fotografische Abnahmedokumentation und BIM360-Integration. |
| `lph8-bauueberwachung-bruecke-spannbeton-vorschub` | Bauueberwachung nach HOAI LPH 8 fuer Bruecken im Freivorbau- oder Vorschubverfahren — Spannstahlpruefung nach ZTV-Ing und DIN EN 1992-2, Pressenprotokoll Vorspannung, Betonguete C40/50 bis C50/60, Lageraus-tausch nach DIN EN 1337 und Messung Gebrauchstauglichkeit Durchbiegung. Praxisnahe Koordination mit SAP PM und RIB iTWO fuer Autobahn- und Bahninfrastrukturbetreiber. |

## Arbeitsweg

Im Plugin HOAI-Leistungsphasen gilt für **Lph9 Gewaehrleistungsmanagement Lph8**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hoai-lph9-gewaehrleistungsmanagement-fristen`

**Fokus:** HOAI-Fachfrage LPH 9: Objektbetreuung, Gewährleistungsfristen, Mängel vor Fristablauf, Begehung, Unternehmerverfolgung, Planerhaftung und Abschlussdokumentation prüfen.

# LPH 9 Gewährleistungsmanagement Und Fristen

## Einsatz

Dieses Fachmodul nach Abnahme, wenn Fristen verstreichen, Mängel wieder auftauchen oder niemand sicher weiß, welcher Unternehmer noch in Anspruch genommen werden kann.

## Normanker

- Anlage 10 HOAI LPH 9.
- BGB-/VOB/B-Mängelrechte nach Vertrag prüfen.
- § 650s BGB Teilabnahme des Planers im Blick behalten.

## Prüfung

1. Abnahmedaten pro Gewerk erfassen.
2. Verjährungsfristen und Vorfristen eintragen.
3. Mängelmeldungen mit Fotos, Ort, Datum und Verlauf verbinden.
4. Verantwortlichkeit Unternehmer/Planer/Fachplaner trennen.
5. Hemmung, Anerkenntnis, Verhandlung oder selbständiges Beweisverfahren prüfen lassen.

## Output

Gewährleistungsdashboard mit Gewerk, Frist, Mangel, Anspruchsgegner, nächstem Schreiben und Eskalationsdatum.

## 2. `lph8-bauueberwachung-abnahmeprotokoll-foerder-erp`

**Fokus:** Methodikskill HOAI LPH 8 — Abnahmeprotokoll-Erstellung fuer oeffentlich geförderte Projekte mit ERP-Schnittstelle. Umfasst Abnahmeprotokoll nach VOB/B § 12 mit Foerderantrag-Konformitaetsnachweis, Verwendungsnachweis BNH und SAP-FI-Buchung, Abnahmeprotokoll-Erstellung in Dalux und PlanRadar, Upload in SAP PS und ELSTER-Foerderprogramme, Teilabnahmen nach Bauabschnitten sowie digitale Unterschrift eIDAS und Integration in Foerderprogramme KfW Bundesfoerderung und EU-EFRE-Richtlinien.

# Abnahmeprotokoll und Foerder-ERP in der Bauueberwachung LPH 8

Oeffentlich gefoerderte Bauprojekte erfordern besonders sorgfaeltige Abnahmeprotokolle: Verwendungsnachweise fuer KfW, EFRE und Bundesfoerderungen muessen lueckenlos nachweisen, dass foerderungsrelevante Baumassnahmen ordnungsgemaess ausgefuehrt wurden. Abnahmeprotokoll und ERP-Buchung sind dabei untrennbar verknuepft. Dieser Skill beschreibt den vollstaendigen von der Abnahmebegehung bis zur SAP-FI-Buchung und Foerderantrag-Konformitaetsnachweis.

## Bauwerk und Auftrag

- Schule Energetische Sanierung KfW 55 Foerderung: Abnahmeprotokoll mit Energieberater, Pruefzertifikat nach KfW-Merkblatt, Foerderbetrag 1.2 Mio. EUR, Auftraggeber Landkreis Bayern
- Klaeranlage EFRE-Foerderung: EU-EFRE-Programm Foerderbedingungen, Abnahmeprotokoll auf Deutsch und Englisch, Pruefpfade Foerdermittelgeber, Bausumme 18 Mio. EUR
- Windpark Neubau Bundesfoerderung: BNetzA-Abnahme und KfW-Foerdernachweis, SAP PS Projektstruktur fuer Foerdermittelcontrolling, Bausumme 22 Mio. EUR

## Erste Schritte Abnahmeprotokoll oeffentlicher Bau

1. Abnahmetermin vorbereiten: Einladung alle Parteien AN, AG, Sachverstaendiger, Foerdermittelbehoerde, Terminbestaetigung 14 Tage vorher, Checklisten Dalux vorab ausgefuellt
2. Begehung strukturieren: Rundgang nach Gewerk-Reihenfolge VOB/C, Foto je Mangel, Protokollant und Schriftfuehrer, Massnahmen sofort festhalten, Fristen definieren
3. Abnahmeprotokoll Formular: VOB/B § 12 Angaben vollstaendig AG AN Datum Ort, Fertigstellungsdatum, Mangelliste nummeriert, Fristen, Vorbehalt und Faelligkeit, Unterschrift alle Parteien
4. Foerderantrag-Konformitaetspruefung: Abnahmemassnahmen gegen Foerderbedingungen abgeglichen, z.B. KfW 55 U-Wert-Nachweis, EFRE-Ausschreibungskonformitaet
5. Verwendungsnachweis-Vorbereitung: Kosten aus SAP PS Ist-Kosten je Foerderposition, Rechnungsbelege archiviert BIM360, Foerderposition zu LV-Position Zuordnung
6. Digitale Signatur eIDAS: Qualifizierte elektronische Signatur aller Parteien, Zeitstempel unveraenderlich, Revisionssicher nach GoBD und eIDAS

## Normen und Rechtsrahmen

- § 650p BGB, § 650q BGB: Architektenvertrag, Koordinationspflicht Abnahme und Foerdermittelnachweis
- HOAI 2021 § 34 Anlage 10 LPH 8: Abnahme als Grundleistung, Foerdermittelkoordination als Besondere Leistung
- VOB/B § 12 Abnahme: Abnahmeprotokoll-Pflicht, Maengelvorbehalt, Faelligkeiten, Verjährungsbeginn Maengelansprueche
- KfW-Merkblatt Energieeffizient Sanieren und Bauen: Abnahmevoraussetzungen, Energieberater-Bestaetigung, Pruefzertifikat
- EFRE-Verordnung EU 2021/1060 Dachverordnung: Verwendungsnachweis, Pruefpfad, Unabhaengige Pruefung Verwendung Foerdermittel
- GoBD BMF-Schreiben 2019: Grundsaetze ordnungsgemaesser DV-gestuetzter Buchfuehrungssysteme, revisionssichere Archivierung Foerderbelege

## Prueferaster und Kontrollpunkte

1. Abnahmeprotokoll-Vollstaendigkeit: Alle VOB/B § 12 Angaben, Datum Fertigstellung und Abnahme, Mangelliste vollstaendig, Fristen schriftlich, Unterschriften aller Parteien
2. Foerderantrag-Konformitaet: Je Foerderposition Nachweis Ausfuehrung nach Foerderbedingungen, z.B. KfW Daemmstandard Protokoll Energieberater
3. Verwendungsnachweis-Vollstaendigkeit: Alle Rechnungsbelege vorhanden, SAP PS Ist-Kosten je Foerderposition ausgewertet, Foerderhoechstbetrag nicht ueberschritten
4. eIDAS-Signatur-Pruefung: Qualifiziertes Zertifikat Signatur Zeitstempel, Verifikation durch Vertrauensdiensteanbieter
5. Foerderantrag-Frist-Kontrolle: Einreichungsfrist Verwendungsnachweis nach Foerderrichtlinie beachtet, typisch 6 Monate nach Abnahme
6. SAP FI Buchung: Foerdermitteleingang als Sonderposten, korrekte Kontengruppe, Kostenstellen-Zuordnung, Pruefbericht Wirtschaftspruefer

## Foto-, Video- und Dokumentenanalyse

- Dalux Abnahmeprotokoll-Modul: Digitales Formular VOB/B § 12, Mangel-Pin Grundriss, Foto-Pflicht je Mangel, eIDAS-Signatur aller Parteien, Export PDF/A fuer Foerderarchiv
- PlanRadar Abnahme-Workflow: Abnahme-Checkliste freigegeben, Mangelerfassung, Status-Update automatisch, PDF-Abnahmeprotokoll Generierung
- BIM360 Document Management: Abnahmeprotokoll als versioniertes Dokument, Zugriffsprotokoll, Foerdermittelgeber-Lesezugriff konfiguriert
- SAP PS Kostenauswertung: Ist-Kosten je Foerderposition, Soll-Foerderbetrag, Budget-Ueberwachung, CSV-Export fuer Foerderantrag-Upload
- ELSTER Foerderantrag-Portal: Upload Verwendungsnachweis als PDF, Verknuepfung SAP FI Buchungsbelege, Einreichung elektronisch nach eIDAS

## Meldungserstellung im ERP / SAP

- SAP PS Abnahme-Meilenstein gesetzt: Transaktionscode CJ20N, Meilenstein ABNAHME-GESAMT mit Datum, automatische Zahlungsfreigabe Schlusszahlung ausgeloest
- SAP FI Foerdermittel-Buchung: Sonderposten KfW-Zuschuss, Kontengruppe Foerdermittel, Kostenstellen-Zuweisung Projekt, Wirtschaftspruefer-Pruefpfad
- SAP PM Abschluss aller offenen Meldungen: Alle M2-Meldungen vor Abnahme geschlossen oder mit Vorbehalt, Abnahme-Datum als Verjährungsbeginn eingetragen
- SAP PS Schlussrechnung-Freigabe: Endabrechnung nach Aufmass, Freigabe Projektleiter digital, Zahlungsvorschlag FI-AP, Zahlungstermin VOB/B § 16 Abs. 3
- Workflow: Abnahme-Begehung, Protokoll Dalux, eIDAS-Signatur, PDF BIM360, SAP PS Meilenstein, SAP FI Buchung, Foerderantrag Upload, Foerdermittelgeber Bestätigung

## Typische Fallstricke

- Abnahme ohne Foerdermittelkonformitaet-Check: Foerdermittelgeber verweigert Verwendungsnachweis nachtraeglich wegen Ausfuehrungsabweichung
- Fehlende Partei-Unterschrift: Abnahme unwirksam nach VOB/B § 12, Verjährungsfrist beginnt nicht, Maengelansprueche laufen weiter
- Verwendungsnachweis-Frist verspasst: Foerdermittelrueckforderung moeglich nach Foerderrichtlinie bei Fristversaeumnis
- SAP FI Buchung falsche Kontengruppe: Wirtschaftspruefer-Pruefung ergibt Fehler, Foerderantrag abgelehnt

## Output

Abnahmeprotokoll vollstaendig nach VOB/B § 12 mit eIDAS-Signatur aller Parteien. Foerderantrag-Konformitaetsnachweis je Foerderposition. Verwendungsnachweis SAP PS Ist-Kosten-Auswertung. Rechnungsbeleg-Archiv BIM360 fuer Foerdermittelpruefer. SAP FI Buchungsprotokoll Foerdermittelzuschuss. Mangelbeseitigungs-Abschlussprotokoll. Bautagebuch-Gesamtarchiv fuer Gewaehrleistungsphase.

## Hinweise zur Qualitaetssicherung

- Alle Abnahmeprotokolle muessen vom Bauueberwacher und dem ausfuehrenden Unternehmen unterschrieben sein
- Fristen nach VOB/B § 13 Abs. 4: Maengelansprueche Bauwerk 4 Jahre, Gesamtwerk nach BGB § 634a 5 Jahre
- Bauwerksbuch nach HOAI Anlage 10 LPH 9 wird durch Bautagebuecher LPH 8 vorbereitet

## Quellen

- [HOAI 2021 § 34 Anlage 10](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [VOB/B § 12 Abnahme](https://www.gesetze-im-internet.de/vob/)
- [eIDAS EU 910/2014 elektronische Signatur](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910)
- [BGB § 634 Maengelansprueche](https://www.gesetze-im-internet.de/bgb/__634.html)
- [§ 650q BGB Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650q.html)

## 3. `lph8-bauueberwachung-bautagebuch-erp-import`

**Fokus:** Methodikskill HOAI LPH 8 — Bautagebuch-Erstellung und ERP-Import-Workflow. Umfasst Pflichtinhalte Bautagebuch nach HOAI § 34 LPH 8 und BGH-Rechtsprechung, digitale Bautagesbuecher in Nevaris, RIB iTWO und PlanRadar, automatischer Wetter-DWD-API-Import, SAP PS Netzplan-Fortschrittsbuchung aus Bautagebuch, Export-Schnittstellen zu SAP S/4HANA Enterprise Asset Management und Revit BIM360 sowie rechtssichere elektronische Signatur nach eIDAS.

# Bautagebuch und ERP-Import in der Bauueberwachung LPH 8

Das Bautagebuch ist das wichtigste Dokument der Bauueberwachung: Es beweist Witterungsbedingungen, Personalstaerke, Maschineneinsatz und Baumangel zum jeweiligen Datum. Gerichte stuetzen sich bei Bauprozessen regelmassig auf Bautagebuecher als primaere Beweismittel. Die Bauueberwachung in LPH 8 fuehrt das Bautagebuch taeglich digital und importiert die Daten automatisiert in ERP-Systeme fuer Projektcontrolling und Abrechnung.

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
- BGH-Urteil VII ZR 157/13: Bautagebuch als Beweis fuer Bau-Soll und Ist-Vergleich, Anforderungen Vollstaendigkeit
- eIDAS-Verordnung EU 910/2014: Elektronische Signatur, Qualifizierte Signatur fuer Rechtssicherheit digitales Bautagebuch
- AHO Heft 9 Leistungen Projektmanagement: Bautagebuch als Informations- und Dokumentationspflicht PM

## Prueferaster und Kontrollpunkte

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
- DWD Open Data API: Stundenwerte Temperatur, Niederschlag, Wind, Format JSON oder CSV, kostenlos fuer kommerzielle Nutzung laut DWD-Nutzungsbedingungen
- SAP S/4HANA EAM-Schnittstelle: BAPI Bautagebuch-Import, Vorgangsfortschritt aktualisiert, Meilenstein automatisch gesetzt, KPI-Dashboard Fortschritt

## Meldungserstellung im ERP / SAP

- SAP PS Fortschritt: Transaktionscode CJ20N Projektstruktur, Vorgangs-Fortschritt je Bautagebuch-Import, automatische Terminkontrolle mit Soll-Termin
- SAP PM Meldung bei Behinderung: Equipment-Nr Bauabschnitt, Meldungsart M2 Behinderung, Text VOB/B § 6 Behinderungsanzeige, Fotos und DWD-Protokoll als Anhang
- SAP CO Projekt-Kostenauswertung: Tagesbericht-Stunden fliessen in CO-Kostentraeger, Soll-Ist Vergleich Personalkosten, Prognose Gesamtkosten
- SAP FI Zahlungsfreigabe: Abschlagsrechnung nach Bautagebuch-Fortschritt automatisch vorgeschlagen, Pruefung und Freigabe Projektleiter
- Workflow: Tagesbericht erstellt, Bauleiter Gegenpruefung und Signatur, Import SAP PS automatisch, Meilenstein aktiviert, SAP FI Zahlungsvorschlag generiert

## Typische Fallstricke

- Bautagebuch mehrere Tage nachgeholt: Rechtlich problematisch bei Behinderungsfall, Gericht wertet Nachtraeglichkeit als Indiz fuer Unzuverlaessigkeit
- Wetterdaten nicht belegt: Nur subjektive Beschreibung, kein DWD-Beleg, Auftraggeber zweifelt Behinderungsanzeige an
- SAP PS Import-Fehler nicht bemerkt: Fortschritt falsch gebucht, Meilenstein fehlerhaft gesetzt, Zahlungsfreigabe blockiert
- Fehlende eIDAS-Signatur: Digitales Bautagebuch ohne qualifizierte Signatur nicht rechtssicher, papierhaft gleichwertig besser

## Output

Bautagebuch-Archive taeglich mit eIDAS-Signatur revisionssicher. SAP PS Fortschrittsbericht monatlich. Behinderungsanzeigen vollstaendig nach VOB/B § 6. DWD-Wetterdaten-Archiv je Bauphase. SAP PM Meldungen bei Behinderungen. Abschlagsrechnungs-Freigabe-Dokumentation SAP FI.

## Hinweise zur Qualitaetssicherung

- Alle Abnahmeprotokolle muessen vom Bauueberwacher und dem ausfuehrenden Unternehmen unterschrieben sein
- Fristen nach VOB/B § 13 Abs. 4: Maengelansprueche Bauwerk 4 Jahre, Gesamtwerk nach BGB § 634a 5 Jahre
- Bauwerksbuch nach HOAI Anlage 10 LPH 9 wird durch Bautagebuecher LPH 8 vorbereitet

## Quellen

- [HOAI 2021 § 34 Anlage 10](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [VOB/B § 6 Behinderungen](https://www.gesetze-im-internet.de/vob/)
- [§ 650q BGB Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650q.html)
- [eIDAS EU 910/2014](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0910)
- [BGB § 634 Maengelansprueche](https://www.gesetze-im-internet.de/bgb/__634.html)

## 4. `lph8-bauueberwachung-bewehrung-verlegekontrolle`

**Fokus:** Bauueberwachung HOAI LPH 8 fuer Bewehrungsverlegung — Kontrolle Stabstaehle BSt 500 S und BSt 500 M nach DIN 488, Betondeckung nach DIN EN 1992-1-1 EC2, Stosslaeange und Ankerlaeange, Biegerollendurchmesser, Abstandhalter-Typ und Anordnung nach DBV-Merkblatt Betondeckung. Umfasst Werksbescheinigungen 3.1 nach EN 10204, Stahllager-Pruefung, fotografische Abnahmedokumentation und BIM360-Integration.

# Bauueberwachung Bewehrungsverlegung und Verlegekontrolle

Die Bewehrungsabnahme ist eine der wichtigsten Pflichten des Bauueberwachungsingenieurs: Einmal vergossener Beton kann nicht nachgebessert werden. Die Bauueberwachung in LPH 8 stellt sicher, dass jede Bewehrungseinheit fachgerecht verlegt ist, die Betondeckung den Expositionsklassen entspricht und alle Schwei­ssarbeiten an Bewehrung dokumentiert sind. Nur eine lueckenlose Abnahme schuetzt vor Haftungsrisiken.

## Bauwerk und Auftrag

- Parkhausneubau Stuttgart 6-geschossig: Stahlbetonflachdecken 28 cm, BSt 500 S Q335A Mattenbewehrung, Betondeckung cmin 25 mm XC3, Bausumme Bewehrung 2.1 Mio. EUR
- Strassenbruecke Vorlaeufiger Neubau Kreisstrasse: Plattenbalken-Querschnitt, Vorspannung Litzen 1670/1860, Bewehrungskorb 72 t Stahl, intensive Abnahme-Dokumentation
- Industriehalle Stahl-Beton-Verbund: Verbunddecke Comflor 80 mit Aufbeton, Bewehrungsmatte 188, Verbundanker Shear Studs

## Erste Schritte auf der Baustelle

1. Stahllager-Pruefung auf der Baustelle: Lagerungsqualitaet trocken und unterlueftet, keine Roststellen tiefer als Korrosionsgrad C nach DIN EN ISO 8501-1, Chargen-Etikett erhalten
2. Werksbescheinigung 3.1 nach EN 10204: Je Liefercharge Stahlsorte und Chargen-Nr, chemische Analyse und mechanische Kennwerte, Uebereinstimmung mit Bestellspezifikation
3. Biegerollendurchmesser pruefen: Biegerollendurchmesser nach DIN EN 1992-1-1 Tabelle 8.1 d groesser 5d fuer Durchmesser groesser 16 mm, Fehlbiegungen dokumentieren
4. Abstandhalter-Einbau: Typ und Anordnung nach DBV-Merkblatt Betondeckung 2020, Punktlast-Abstandhalter max. 500 mm Abstand, Linienstuetzung bei Matten
5. Stosslageprotokoll: Bewehrungsstoesse nicht im Bereich maximaler Biegemomente, Ueberlappungslaenge nach EC2, Fotos jedes Stosses
6. Zeichnungsabgleich: Plan-Revision aktuell vor Bewehrungseinbau, Stabdurchmesser und Abstaende gemessen und eingetragen in Abnahme-Checkliste

## Normen und Rechtsrahmen

- § 650p BGB, § 650q BGB: Architekten- und Ingenieurvertrag, Pflicht zur Bewehrungsabnahme vor Betonage
- HOAI 2021 § 34 Anlage 10 LPH 8: Bewehrungsabnahme als Grundleistung Bauueberwachung Hochbau und Ingenieurbau
- VOB/C DIN 18331 Betonarbeiten: Dokumentationspflichten Bewehrungseinbau
- DIN 488-1:2009-08 Betonstahl: Gueteeigenschaften BSt 500 S und 500 M, Pruefanforderungen
- DIN EN 1992-1-1 Eurocode 2: Betondeckung cmin und cdev, Stosslaeangen, Mindestbewehrung, Biegeradius
- DBV-Merkblatt Betondeckung und Bewehrung 2020: Abstandhalter-Anordnung, Toleranzregeln fuer Betondeckung

## Prueferaster und Kontrollpunkte

1. Betondeckungsmessung nach Ausschalen: Covermeter Profometer 650 oder Hilti PS200, Messung Raster 1 m x 1 m, Grenzwert Unterschreitung kleiner 10 mm unter cmin
2. Stabdurchmesser Stichprobe: Schieblehre je 10. Stab gemessen, Toleranz nach DIN 488 +-4 Prozent, Protokolliert mit Lage GPS
3. Stosslaeangen-Kontrolle: Schieblehre und Zollstock, Soll-Ueberlappungslaenge nach EC2 Abschnitt 8.7, Protokoll je Stosslage-Position
4. Abstandhalter-Dichte: 1 Abstandhalter je 0.5 m2 Bauteilflaeche Unterseite, 1 je 1.0 m2 Bauteilflaeche Seite, Stichprobe 10 Prozent der Flaeche
5. Schweissqualitaet Bewehrung: bei baustellengeschweisster Verbindung Schweissprotokoll nach DIN EN ISO 17660-1, WPS und Schweisser-Qualifikation vorhanden
6. Fehlerkoordination: Maengelliste Bewehrungsabnahme mit Mangel-Nr, Lage, Foto, Massnah und Freigabe-Vermerk vor Betonage

## Foto-, Video- und Dokumentenanalyse

- Fotodokumentation Bewehrungsabnahme: Systemfoto Flaeche, Detailfoto Stosslage, Detailfoto Abstandhalter, Detailfoto Aussparungsschalung, Zeitstempel
- BIM360 Photo Tracking: Foto gelinkt an IFC-Bauteil-ID Deckenfeld-Nr oder Stuetzen-ID, exportierbar je Bauteil als Abnahme-Paket
- Matterport 360-Grad-Scan grosse Bewehrungsflaechen: Deckenbewehrung 3D dokumentiert, massstabsgerechte Abstands-Messung im Viewer
- Lieferschein-Archiv: Scan per Handy-App, Verknuepfung Chargen-Nr zu Stahlsorte und Einbaubereich, vollstaendig fuer Gewaehrleistungsakte
- Covermeter-Messprotokoll: Tabellarisch je Rasterfeld, Farbmarkierung Unterschreitung rot, Export PDF fuer Bauherrenakte

## Meldungserstellung im ERP / SAP

- SAP PM Meldungsart M2 Bewehrungsmangel: Equipment-Nr Bauteil-ID, Schadenscode B010 Betondeckungsunterschreitung, Zustaendiger Polier zugewiesen
- SAP PS Vorgang BEWEH-020: Status BTAB Teilabnahme Bewehrung, Datum Freigabe durch Bauueberwacher, Dokumenten-Link zu PlanRadar
- PlanRadar Mangel mit IFC-Bauteil-Verknuepfung: Mangel-Nr, Foto, Schweregrad, Faelligkeit, Bauueberwacher als Erfasser, Polier als Empfaenger
- Dalux BIM-Mangel direkt im 3D-Modell: BCF 2.1 Export an Tragwerksplaner fuer Stellungnahme bei Bewehrungsabweichungen
- Workflow: Mangel-Abnahmeprotokoll erstellt, Massnahme definiert, Polier Mangelbeseitigung, Nachkontrolle Foto, Bewehrungsabnahme-Freigabe, Betonage-Freigabe

## Typische Fallstricke

- Abstandhalter bei Plattenunterkante weggedrückt: Durch Betongewicht rutschen Abstandhalter weg, Betondeckungsunterschreitung nach Ausschalen
- Fehlende aktuelle Bewehrungsplan-Revision: Aeltere Plversion eingebaut, Nachtraegliche Aenderungen nicht im Feld, Statik-Widerspruch
- Stosslage in Momentenmaximum: Fehlplatzierung Stosslage durch unklare Plandarstellung, Tragfaehigkeitsminderung im Stutzmomentbereich
- Chargen-Wechsel ohne neue Werksbescheinigung: Stahl anderer Schmelze ohne Nachweis verbaut, Guetedokumentation lueckenhaft

## Output

Bewehrungsabnahme-Protokoll je Bauteil mit Freigabe-Unterschrift Bauueberwacher. Covermeter-Messprotokoll nach Ausschalen. Werksbescheinigungen 3.1 Archiv je Liefercharge. Fotodokumentation Stossstellen und Abstandhalter in BIM360. PlanRadar-Maengelliste. Abnahme-Freigabevermerk vor Betonage je Bauteil.

## Hinweise zur Qualitaetssicherung

- Alle Abnahmeprotokolle muessen vom Bauueberwacher und dem ausfuehrenden Unternehmen unterschrieben sein
- Fristen nach VOB/B § 13 Abs. 4: Maengelansprueche Bauwerk 4 Jahre, Gesamtwerk nach BGB § 634a 5 Jahre
- Bauwerksbuch nach HOAI Anlage 10 LPH 9 wird durch Bautagebuecher LPH 8 vorbereitet

## Quellen

- [HOAI 2021 § 34 Anlage 10](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [VOB/C DIN 18331 Betonarbeiten](https://www.gesetze-im-internet.de/vob/)
- [§ 650q BGB Ingenieurvertrag](https://www.gesetze-im-internet.de/bgb/__650q.html)
- [BGB § 634 Maengelansprueche](https://www.gesetze-im-internet.de/bgb/__634.html)
- [BGB § 640 Abnahme Werkvertrag](https://www.gesetze-im-internet.de/bgb/__640.html)

## 5. `lph8-bauueberwachung-bruecke-spannbeton-vorschub`

**Fokus:** Bauueberwachung nach HOAI LPH 8 fuer Bruecken im Freivorbau- oder Vorschubverfahren — Spannstahlpruefung nach ZTV-Ing und DIN EN 1992-2, Pressenprotokoll Vorspannung, Betonguete C40/50 bis C50/60, Lageraus-tausch nach DIN EN 1337 und Messung Gebrauchstauglichkeit Durchbiegung. Praxisnahe Koordination mit SAP PM und RIB iTWO fuer Autobahn- und Bahninfrastrukturbetreiber.

# Bauueberwachung Bruecke Spannbeton Vorschub (LPH 8)

Spannbetonbruecken im Freivorbau oder Taktschiebeverfahren gehoeren zu den anspruchsvollsten Bauueberwachungsaufgaben.
Die Bauueberwachung nach HOAI LPH 8 prueft Spannstahlguete, Pressenprotokolle, Betonguete und Lagerkraefte.
Gebrauchstauglichkeit und Rissbeschraenkung nach DIN EN 1992-2 (Eurocode 2 Brueckenbau) sind Kernpruefpunkte.

## Bauwerk und Auftrag

- BAB-Bruecke 4-Felder 180 m, Bayern, Autobahndirektion, Freivorbau, Spannbeton C45/55, 12 Mio. Euro
- Eisenbahnbruecke Taktschiebeverfahren 240 m, NRW, DB InfraGo, Einfeldtraeger, 18 Mio. Euro
- Strassenbruecke Bogen-Spannbeton 80 m, Sachsen, Strassenbauverwaltung, Vorschub, 6 Mio. Euro

## Erste Schritte auf der Baustelle

1. Pruefplan Spannstahlguete: Zertifikat nach DIN EN 10138, Chargenidentifikation, Lagerungsprotokoll
2. Bewehrungsabnahme vor Betonage: Spannkanaele gerade, Huellrohr Dichtheit, Bewehrungsdeckung
3. Betonage Freivorbau-Takt: C45/55 XD1 XF2, Frischbetonpruefung, Wuerfelproben je Betoniertakt
4. Pressenprotokoll Vorspannen: Spannkraft je Litzenbuendel, Spannweg, Reibungskoeffizient, Ankerschlupf
5. Traeger-Geometrie nach Taktschieben: Einhoehung, Kreuzgefaelle, Lagerabweichung Toleranz
6. Lagerabnahme nach Einbau: Pressenlager oder Gleitlager, Axialkraft, Rotationswinkel nach DIN EN 1337

## Normen und Rechtsrahmen

- HOAI 2021 § 34 Anlage 10 LPH 8 Grundleistungen
- § 650p BGB Architektenvertrag, § 650q BGB Kuendigung
- DIN EN 1992-2 Eurocode 2: Betonbruecken, Beton- und Spannbetontragwerke
- ZTV-Ing Teil 4 Stahlbeton- und Spannbetonbau: Grundsaetze, Ausfuehrung, Pruefung
- DIN EN 1337-1 Lager im Bauwesen: Allgemeine Konstruktionsprinzipien
- DIN EN 10138 Spannstaehle: Anforderungen, Werksbescheinigung, Pruefverfahren

## Prueferaster und Kontrollpunkte

1. Spannstahlzertifikat: Chargenbezeichnung, Gueteklasse Y1860 oder Y1770, Pruefattest 3.1
2. Spannkanal-Dichtheit: Druckpruefung Huellrohr 2 bar, Verlust kleiner 0.1 bar/min, Protokoll
3. Betonguete: Frischbetonpruefung Konsistenz, Frischbetontemperatur max. 30 Grad C, Wuerfelproben
4. Pressenprotokoll: Istkraft und Sollkraft je Litzenbuendel, Ankerschlupf Toleranz 5 mm
5. Durchbiegung Traeger: Messung nach Vorspannen, Vergleich Berechnungswert Deformation
6. Lagerabnahme: Lagerplatten-Ablotung, Lagerversatz, Lagerpressensimulation Kraftnachweis

## Foto-, Video- und Dokumentenanalyse

- BIM360 Bruecke: IFC-Modell Taktschieben, Clash-Bericht Spannkanale vs. Bewehrung
- Drohnenflug DJI Mavic 3 Enterprise: Uebersicht Brueckenfeld nach jedem Betoniertakt ortho
- Pressenprotokoll-Scan: Spannkraft je Litze als PDF, Zuordnung zu Litzenbuendel und Achse
- Betonkernproben Bruecke: Bohrkerne 28 Tage, Druckfestigkeit, Chloridgehalt, Labor akkreditiert
- Konvergenzmessung: Totalstation-Monitoring Traegergeometrie, Monatsbericht Setzungswerte

## Meldungserstellung im ERP / SAP

- SAP PM DB InfraGo EAM: Equipment Bruecke mit Feldern/Lagern/Ausruestung, Wartungsplaene
- SAP PS Projektsystem: Vorgang je Betoniertakt, Kosten und Termine je Abschnitt
- RIB iTWO: Aufmass Beton nach m3 und Spannstahlmenge nach t, Einheitspreisabrechnung
- PlanRadar Brueckenbau: Mangel-Ticket Pressenprotokoll-Abweichung, Verantwortlicher Spannkolonne
- Dalux BIM-Bruecke: As-Built-Spannplan mit Ist-Kraeften je Litzenbuendel eingetragen

## Typische Fallstricke

- Spannstahl-Charge nicht dokumentiert: Chargenidentifikation fehlt, Abnahme verweigert
- Pressenprotokoll-Abweichung: Ankerschlupf ue5 mm, Spannkraft unzureichend, Nachspannen notwendig
- Betonguete unter C45/55: Wuerfelprobe Unterschreitung, Statiker entscheidet Rueckbau oder Ertuechtigung
- Lagerfehler beim Einbau: Lagerpressung ungleichmaessig, Traeger kippt beim Taktschieben

## Output

Pressenprotokolle je Litzenbuendel und Betoniertakt. Betonguete-Pruefprotokolle C45/55.
Spannkanal-Dichtheitspruefprotokolle. Traeger-Geometriemessung nach Vorschub.
Lagerabnahme-Protokoll. Abnahmeprotokoll Bruecke nach VOB/B und ZTV-Ing.

## Quellen

- [HOAI 2021 § 34](https://www.gesetze-im-internet.de/hoai_2021/__34.html)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html)
- [DIN EN 1992-2 Eurocode 2 Bruecken](https://www.gesetze-im-internet.de/)
- [ZTV-Ing Teil 4 Spannbetonbau](https://www.gesetze-im-internet.de/)
- [DIN EN 1337 Lager im Bauwesen](https://www.gesetze-im-internet.de/)
- [BGH VII ZR 41/08 Brueckenbau Haftung](https://dejure.org/dienste/vernetzung/rechtsprechung?Text=VII+ZR+41/08)
