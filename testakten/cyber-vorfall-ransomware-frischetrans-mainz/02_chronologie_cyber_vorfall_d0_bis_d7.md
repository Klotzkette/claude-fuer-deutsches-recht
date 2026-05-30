# Chronologie des Cyber-Vorfalls — D+0 bis D+7

**Mandantin:** Frischetrans Mittelrhein GmbH, Mainz  
**Vorfall:** Ransomware-Angriff „AkiraNext"  
**Erstdetektion:** 06.05.2026, 04:17 Uhr  
**Bearbeiter:** RA Lukas Drosten, Kanzlei Drosten & Pekonkur

---

## Tag 0 — Mittwoch, 06.05.2026 (Vorfallstag)

**04:17 Uhr**  
SOC-System der InsoTec Systems GmbH (externer IT-Dienstleister, Frankfurt) detektiert anomale Netzwerkaktivität im Rechenzentrum der Frischetrans Mittelrhein GmbH (Serverraum Binger Straße 142, Mainz). Ungewöhnlich hoher Netzwerktraffic auf internen SMB-Shares, laterale Bewegungen im Active Directory-Verbund.

**04:23 Uhr**  
SOC-Analyst Mikhail Dragunov (InsoTec) weckt seinen Schichtleiter. Erste Einschätzung: möglicherweise Ransomware. Automatische Segmentierungsregeln greifen verzögert, da Firewall-Konfiguration veraltet (siehe Pflichtverletzungsanalyse Aktenstück 09).

**04:31 Uhr**  
Erste Systeme vollständig verschlüsselt: SAP S/4HANA Applikationsserver (Hostname: FT-ERP-PROD-01, FT-ERP-PROD-02). Datenbankserver FT-DB-01 betroffen. Lösegeldforderung als Desktop-Hintergrund und .txt-Datei auf allen verschlüsselten Systemen sichtbar.

**04:45 Uhr**  
InsoTec benachrichtigt Bereitschaftsnummer der Frischetrans. Diensthabender Logistikleiter Rainer Schäper nimmt Anruf entgegen. Geschäftsführerin Theresia Wallbruck wird um 04:52 Uhr telefonisch erreicht.

**05:10 Uhr**  
Telematik-Schnittstellen (GPS-Tracking, Temperaturüberwachung Kühlkette, Fahrerdispositionssystem) fallen aus. 47 der 64 LKW können keine Positions-/Temperaturdaten mehr übermitteln. Frühschicht-Fahrer werden per Mobiltelefon kontaktiert.

**05:35 Uhr**  
Geschäftsführerin Wallbruck trifft am Firmengelände ein. Sofortentscheidung: alle Systeme vom Netz nehmen (Network Kill). InsoTec schaltet zentrale Switches ab.

**06:00 Uhr**  
Erste Schadenserfassung: ERP-System vollständig ausgefallen, Auftragsabwicklung nicht möglich. Geplante 37 Auslieferungen für Donnerstag 07.05. sind gefährdet. Frischbäcker AG und Backhaus Süd erhalten Notfall-Anrufe.

**07:15 Uhr**  
Theresia Wallbruck ruft Kanzlei Drosten & Pekonkur an. RA Lukas Drosten übernimmt Erstberatung per Telefon.

**08:30 Uhr**  
Erstes persönliches Treffen in der Kanzlei Drosten & Pekonkur (Schillerstraße 14, Mainz). Mandatserteilung. Beginn der rechtlichen Incident-Response.

**09:00 Uhr**  
Forensisches Sicherungsprotokoll startet. InsoTec sichert flüchtige Daten (RAM-Dumps, Netzwerk-Logs). Externale Forensikfirma CyberForensik RheinMain GmbH wird durch Kanzlei Drosten empfohlen und beauftragt.

**10:30 Uhr**  
Erste Indizien für Datenabfluss: Netzwerk-Logs zeigen ab dem 04.05.2026, 22:44 Uhr (D-2) kontinuierlichen ausgehenden Datenverkehr zu einer IP-Adresse in Rumänien (Tor-Exit-Node). Gesamtvolumen ca. 2,1 TB.

**11:45 Uhr**  
Strafanzeige bei ZAC Mainz (Zentrale Ansprechstelle Cybercrime) wird vorbereitet (AZ: 421 UJs 6611/26).

**14:00 Uhr**  
BSI Außenstelle Frankfurt telefonisch vorinformiert durch RA Drosten. NIS2-Relevanzprüfung eingeleitet.

**15:30 Uhr**  
Versicherungsmeldung an CyberCovered AG (Frankfurt) per verschlüsselter E-Mail. Schadensnummer wird vergeben.

**17:00 Uhr**  
Erpressungsschreiben der Gruppe AkiraNext vollständig dokumentiert und rechtlich bewertet (Aktenstück 03).

---

## Tag 1 — Donnerstag, 07.05.2026

**08:00 Uhr**  
CyberForensik RheinMain GmbH beginnt forensische Untersuchung vor Ort. Zwei Spezialisten arbeiten an Sicherung und Analyse der Systeme.

**09:30 Uhr**  
Strafanzeige bei ZAC Mainz persönlich erstattet durch RA Drosten im Namen der Frischetrans. Aktenzeichen 421 UJs 6611/26 vergeben.

**11:00 Uhr**  
Krisenteam konstituiert sich formal: GF Wallbruck, RA Drosten, IT-Leiter Franz Berkenfeld (Frischetrans), SOC-Leiter InsoTec, externer Forensiker.

**14:00 Uhr**  
Betroffene Datenkategorien wurden durch Forensikteam bestätigt:  
- Kundenstammdaten: 18 Kunden, darunter Frischbäcker AG und Backhaus Süd  
- Mitarbeiterdaten: Personalakten 280 MA, davon Gesundheitsdaten aus BEM-Verfahren von 38 Mitarbeitern  
- Vertragsdaten mit Lieferanten  
- Finanzdaten (Buchungsdaten Q1/2026)

**16:30 Uhr**  
BSI-Meldung (NIS2) formal elektronisch übermittelt über das MELDEPF-Portal (Referenznummer BSI-REF-2026-1847).

**19:00 Uhr**  
Kanzlei bereitet Art.-33-DSGVO-Meldung an LfDI RLP vor. Fristablauf: 09.05.2026, 04:17 Uhr.

---

## Tag 2 — Freitag, 08.05.2026

**09:00 Uhr**  
Forensikbericht Zwischenstand: Angriffsvektor identifiziert. Initial Access über ungepatchte SAP-Schwachstelle CVE-2026-0712 (SAP NetWeaver AS ABAP). Patch war laut Vertrag mit ProcessSpark Cloud AG zum 20.03.2026 geschuldet, tatsächlich erst am 28.04.2026 (Nacht zum 29.04.) eingespielt worden — 39 Tage verspätet. In dieser Lücke erfolgte der Angriff.

**11:00 Uhr**  
Vertragsanalyse ProcessSpark beginnt (Aktenstück 08 und 09).

**14:30 Uhr**  
KI-Verordnungs-Compliance-Check für „PalettenAuge AI" aufgenommen (Aktenstück 13).

**22:45 Uhr**  
DSGVO-Meldung Art. 33 an LfDI RLP eingereicht (Aktenstück 05). Frist eingehalten.

---

## Tag 3 — Samstag, 09.05.2026

**04:17 Uhr**  
Ablauf der 72-Stunden-Frist Art. 33 DSGVO. Meldung wurde rechtzeitig übermittelt (22:45 Uhr D+2).

**10:00 Uhr**  
Erste Notfall-Wiederherstellung: Backup-Systeme (letzte Sicherung 03.05.2026, 02:00 Uhr) werden schrittweise eingespielt. Datenverlust: 3 Tage operativer Daten.

**14:00 Uhr**  
Telefonische Abstimmung LfDI RLP: Behörde bestätigt Eingang der Meldung, stellt Rückfragen zu BEM-Gesundheitsdaten und ordnet Übermittlung eines Folgeberichts innerhalb von 14 Tagen an.

---

## Tag 4 — Sonntag, 10.05.2026

**Keine behördlichen Aktivitäten.**  
Interne IT-Wiederherstellung läuft. Telematik-System teilweise wieder verfügbar (35 von 64 LKW).

---

## Tag 5 — Montag, 11.05.2026

**09:00 Uhr**  
Betriebsrat wird förmlich informiert (§ 75 BetrVG, § 26 BDSG). Anhörung protokolliert (Aktenstück 18).

**11:00 Uhr**  
Mitarbeiterinformation BEM-Betroffene: 38 Beschäftigte werden schriftlich über Datenpanne informiert (Aktenstück 17).

**14:00 Uhr**  
DSFA (Datenschutz-Folgenabschätzung) für BEM-Gesundheitsdaten formell eingeleitet (Aktenstück 11).

---

## Tag 6 — Dienstag, 12.05.2026

**10:00 Uhr**  
Anwaltsschreiben (Klageandrohung) an ProcessSpark Cloud AG abgesandt (Aktenstück 10). Frist: 14 Tage.

**11:00 Uhr**  
Kundenkommunikation an Frischbäcker AG und Backhaus Süd versandt (Aktenstück 16).

**14:00 Uhr**  
Open-Source-Compliance-Audit für „TourPlanner" (AGPL-3.0-Komponente „scheduleHero") begonnen (Aktenstück 14).

---

## Tag 7 — Mittwoch, 13.05.2026

**09:00 Uhr**  
ERP-System SAP S/4HANA zu ca. 80 % wiederhergestellt. Normalbetrieb Logistik teilweise aufgenommen.

**10:30 Uhr**  
Strategiememorandum RA Drosten fertiggestellt (Aktenstück 20).

**14:00 Uhr**  
Pressemitteilung (Entwurf) durch Kanzlei freigegeben — Veröffentlichung nach Abstimmung mit Mandantin (Aktenstück 19).

**16:00 Uhr**  
Keine Reaktion der Erpressergruppe AkiraNext auf Nicht-Zahlung. Forensikteam bestätigt: Lösegeldzahlung wird ausdrücklich nicht empfohlen (keine Garantie auf Schlüssel, Strafbarkeitsrisiken, Versicherungsklauseln).

---

## Angriffs-Technisches Lagebild (Zusammenfassung forensischer Erstbefunde)

| Parameter | Wert |
|---|---|
| Angriffsvektor | CVE-2026-0712 (SAP NetWeaver AS ABAP, ungepatchte Lücke) |
| Erstinfiltration | 04.05.2026, ca. 22:44 Uhr (D-2) |
| Dwell Time (Verweildauer) | ca. 29,5 Stunden vor Aktivierung der Verschlüsselung |
| Verschlüsselte Systeme | SAP S/4HANA (2 App-Server, 1 DB-Server), Fileserver (3), Telematik-Gateway |
| Abgeflossene Datenmenge | ca. 2,1 TB |
| Geforderte Summe | 1.450.000 USD in Monero |
| Zahlungs-Deadline (Erpresser) | 13.05.2026, 23:59 Uhr UTC |
| Reaktion Frischetrans | Keine Zahlung |
| Wiederherstellung | Aus Backup (Stand 03.05.2026) |
| Datenverlust operativ | ~3 Tage |
| Betroffene Personen (Kunden) | 18 Firmenkunden, davon 2 systemrelevante Bäckereiketten |
| Betroffene Mitarbeiter | 280 (Grunddaten), 38 (Gesundheitsdaten BEM) |
