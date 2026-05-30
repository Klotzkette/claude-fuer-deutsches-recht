# Meldung an das BSI gemäß NIS2-Umsetzungsgesetz (NIS2UmsuG)

**Aktenstück:** 06  
**Datum der Übermittlung:** 07.05.2026, 16:30 Uhr  
**Übermittlungsweg:** BSI-MELDEPF-Portal (elektronisch)  
**BSI-Referenznummer:** BSI-REF-2026-1847  
**Bearbeiter:** RA Lukas Drosten für Frischetrans Mittelrhein GmbH

---

## Rechtliche Vorbemerkung: NIS2-Relevanz von Frischetrans

### Einordnung in den Geltungsbereich der NIS2-Richtlinie

Die NIS2-Richtlinie (Richtlinie (EU) 2022/2555) wurde in Deutschland durch das **Gesetz zur Umsetzung der NIS-2-Richtlinie und zur Regelung wesentlicher Grundzüge des Informationssicherheitsmanagements in der Bundesverwaltung** (NIS2UmsuG) umgesetzt, das am 01.11.2024 in Kraft getreten ist.

Die Einordnung von Frischetrans Mittelrhein GmbH in den Geltungsbereich des NIS2UmsuG ergibt sich aus folgenden Überlegungen:

**Sektor:** Frischetrans ist im Bereich der **Lebensmittelversorgungskette** (B2B-Frischelogistik für Großbäckereien) tätig. Der Sektor „Lebensmittel" ist gemäß Anhang I NIS2-Richtlinie als **wichtiger Sektor** eingestuft.

**Größenkriterium:** Frischetrans beschäftigt 280 Mitarbeiter und erzielt einen Jahresumsatz von ca. 38 Mio. EUR. Damit überschreitet das Unternehmen die Schwelle für **mittelgroße Unternehmen** (≥ 50 Mitarbeiter oder ≥ 10 Mio. EUR Umsatz) gemäß Art. 2 NIS2-Richtlinie. Es fällt somit als **wichtige Einrichtung** (nicht: wesentliche Einrichtung) in den Anwendungsbereich.

**Begründung der Versorgungsrelevanz:**  
Frischetrans beliefert die Großbäckereien Frischbäcker AG und Backhaus Süd, die ihrerseits Supermarktfilialisten und Kantinen in der Metropolregion Rhein-Main-Neckar beliefern. Ein Ausfall der Frischelogistik beeinträchtigt die Lebensmittelversorgung einer signifikanten Bevölkerungsgruppe. Das BSI hat den Angriff auf Basis dieser Argumentation als meldepflichtig akzeptiert (Bestätigungsschreiben BSI liegt vor).

---

## Formelle Meldung

**An:**  
Bundesamt für Sicherheit in der Informationstechnik (BSI)  
Außenstelle Frankfurt  
Gutleutstraße 163, 60327 Frankfurt am Main

**Meldung eines erheblichen Sicherheitsvorfalls**  
gemäß § 31 NIS2UmsuG (Meldepflichten wichtiger Einrichtungen)

---

### Meldender Verantwortlicher

**Name:** Frischetrans Mittelrhein GmbH  
**Sitz:** Binger Straße 142, 55131 Mainz  
**Einrichtungstyp:** Wichtige Einrichtung (Sektor: Lebensmittel/Versorgungskette)  
**Ansprechpartner (IT-Sicherheit):** Franz Berkenfeld, IT-Leiter  
**Bevollmächtigter RA:** Lukas Drosten, Kanzlei Drosten & Pekonkur, Mainz

---

### Angaben zum Vorfall

**Art des Vorfalls:**  
Ransomware-Angriff (Verschlüsselung und Datenexfiltration) durch die kriminelle Gruppe „AkiraNext".

**Betroffene Systeme:**  
- SAP S/4HANA ERP-System (on-premises, vollständig verschlüsselt)  
- Telematik-Schnittstellen (GPS-Tracking, Temperaturüberwachung, Fahrerdisposition)  
- Fileserver (3 Systeme verschlüsselt)  
- Active Directory / Domain Controller (kompromittiert, nicht verschlüsselt)

**Zeitpunkt:**  
- Vermutlicher Erstzugang: 04.05.2026, ca. 22:44 Uhr  
- Aktivierung Ransomware: 06.05.2026, ca. 04:17–04:31 Uhr  
- Entdeckung: 06.05.2026, 04:17 Uhr

**Angriffsvektor:**  
Ungepatchte SAP-Schwachstelle CVE-2026-0712 (SAP NetWeaver Application Server ABAP — Remote Code Execution). Das kritische Sicherheitsupdate war laut Vertrag mit dem ERP-Dienstleister ProcessSpark Cloud AG bis 20.03.2026 einzuspielen, wurde jedoch erst am 28./29.04.2026 aufgespielt.

**Schadwirkung:**

1. **Verfügbarkeit:** Vollständiger Ausfall des ERP-Systems für ca. 7 Tage; Ausfall Telematik-System für ca. 4 Tage; 47 von 64 LKW ohne Telematik-Anbindung; geplante Frischlieferungen für 37 Kunden am 07.05.2026 teils nicht durchführbar.

2. **Vertraulichkeit:** Exfiltration von ca. 2,1 TB Daten (Kundenstammdaten 18 Kunden, Personalakten 280 Mitarbeiter inkl. Gesundheitsdaten BEM 38 Mitarbeiter, Finanzdaten Q1/2026, Vertragsdaten).

3. **Wirtschaftlicher Schaden (vorläufige Schätzung):** ca. 850.000–1.200.000 EUR (Wiederherstellungskosten, Betriebsausfall, Forensik, Rechtskosten, ggf. Bußgelder).

---

### Bewertung der Erheblichkeit (§ 31 Abs. 2 NIS2UmsuG)

Der Vorfall ist als **erheblich** einzustufen, da:

1. Er eine erhebliche Betriebsunterbrechung verursacht hat (vollständiger ERP-Ausfall > 24 h)
2. Er zu einem signifikanten finanziellen Schaden geführt hat (> 500.000 EUR)
3. Er die Versorgungssicherheit der Bevölkerung beeinträchtigt hat (Frischelogistik für Lebensmittelketten)
4. Er personenbezogene Daten in großem Umfang betrifft (verbunden mit DSGVO-Meldung)

---

### Getroffene Sicherheitsmaßnahmen

- Network Kill: 06.05.2026, 05:35 Uhr (Trennung aller Systeme vom Netz)
- Beauftragung forensischer Spezialisten
- Koordination mit ZAC Mainz (Strafanzeige)
- Schrittweise Wiederherstellung aus Backup (Backup-Stand 03.05.2026)
- Überarbeitung Patch-Management-Prozess eingeleitet
- Überprüfung Firewall-Konfiguration und Netzwerksegmentierung beauftragt
- Implementierung MFA für alle administrativen Zugänge eingeleitet

---

### Stufenweise Meldung nach § 31 NIS2UmsuG

Diese Meldung ist die **Erstmeldung** (innerhalb 24 Stunden nach Kenntniserlangung der erheblichen Auswirkungen, § 31 Abs. 3 Nr. 1 NIS2UmsuG).

Ein **Folgebericht** (detaillierter Zwischenbericht, § 31 Abs. 3 Nr. 2 NIS2UmsuG) wird innerhalb von 72 Stunden nach Erstmeldung (bis 10.05.2026, 16:30 Uhr) übermittelt.

Ein **Abschlussbericht** (§ 31 Abs. 3 Nr. 3 NIS2UmsuG) folgt innerhalb eines Monats.

---

### Koordinationshinweis

Die Frischetrans Mittelrhein GmbH hat parallel eine Datenschutzpannen-Meldung gemäß Art. 33 DSGVO an den LfDI Rheinland-Pfalz übermittelt (Ref. LfDI-RLP-2026-0508-4419). Eine Abstimmung beider Behörden wird erbeten.

---

**Frankfurt/Mainz, den 07.05.2026**

RA Lukas Drosten  
Kanzlei Drosten & Pekonkur, Mainz  
(handelnd für und im Auftrag der Frischetrans Mittelrhein GmbH)

---

## Anlage: BSI-Meldebestätigung

*Gemäß BSI-Bestätigungsschreiben vom 07.05.2026, 18:45 Uhr (automatische Eingangsbestätigung über das MELDEPF-Portal) wurde die Meldung unter Referenznummer BSI-REF-2026-1847 erfasst. Das Bestätigungs-PDF ist als Anlage „pdfs/bsi_meldbestaetigung.pdf" in der Akte hinterlegt.*

---

## Rechtliche Grundlagen (Nachweise)

- Richtlinie (EU) 2022/2555 (NIS2-Richtlinie), ABl. L 333 vom 27.12.2022  
- Gesetz zur Umsetzung der NIS-2-Richtlinie (NIS2UmsuG), BGBl. 2024 I Nr. 387  
- BSI-Gesetz (BSIG) i.d.F. nach NIS2-Umsetzung  
- BSI-Kritisverordnung (BSI-KritisV) i.d.F. 2025  
- Erwägungsgründe 102–104 NIS2-Richtlinie zur Meldepflicht  

Zur NIS2-Klassifikation von Logistikunternehmen im Lebensmittelsektor vgl. ENISA-Leitlinien „NIS2 Sectoral Classification" (2024, abrufbar unter https://www.enisa.europa.eu).
