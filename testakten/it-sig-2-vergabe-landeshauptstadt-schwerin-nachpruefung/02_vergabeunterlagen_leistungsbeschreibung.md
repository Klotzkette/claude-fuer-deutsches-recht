# Aktenstück 02 – Vergabeunterlagen: Leistungsbeschreibung SOC + ISB-Beratung

**Aktenzeichen:** VK 1-32/26  
**Vorhabenbezeichnung:** LH-SN-Cyber-SOC-NSV-2026  
**Dokument-Typ:** Leistungsbeschreibung (Teil A der Vergabeunterlagen)  
**Version:** 1.0 vom 27.02.2026  
**Vergabestelle:** Landeshauptstadt Schwerin / Eigenbetrieb SDS

---

## Teil A: Leistungsbeschreibung

### 1. Ausgangslage und Bedarfsbegründung

Die **Nahverkehr Schwerin GmbH (NSV)** betreibt als KRITIS-Betreiber im Sektor Verkehr das städtische Nahverkehrsnetz der Landeshauptstadt Schwerin. Die NSV unterhält eine heterogene IT/OT-Infrastruktur, bestehend aus:

- Leitstelle für Fahrzeugflottensysteme (OT-Systeme)
- Fahrgastinformationssysteme (digitale Anzeigen, App-Backend)
- Ticketing-Systeme und Kasseninfrastruktur
- Enterprise-IT (Active Directory, Exchange, ERP SAP S/4HANA)
- Videoüberwachungsinfrastruktur Haltestellen (ca. 180 Kameras)

Die NSV ist als KRITIS-Betreiber nach § 8a BSIG verpflichtet, dem BSI alle zwei Jahre den Nachweis angemessener organisatorischer und technischer Vorkehrungen zur Vermeidung von Störungen der IT-Systeme zu erbringen. Der letzte Audit-Bericht vom November 2024 hat erhebliche Lücken im Bereich Security Operations und Incident Detection festgestellt. Der IT-SIG 2.0 (in Kraft seit Mai 2021) hat die Anforderungen verschärft; die KRITIS-VO Verkehr sieht erweiterte Meldepflichten binnen 72 Stunden vor.

Zusätzlich ist die NSV nach NIS2-Richtlinie (Richtlinie EU 2022/2555, umzusetzen bis Oktober 2024) als „wichtige Einrichtung" im Sektor Verkehr einzustufen; die vollständige Umsetzung nationaler Anforderungen ist bis Mitte 2026 vorgesehen.

### 2. Leistungsumfang

#### 2.1 Los 1 – Cybersecurity-Operations-Center (SOC) als Managed Service

**2.1.1 SIEM-Betrieb**

Der Auftragnehmer betreibt ein Security Information and Event Management (SIEM) für die IT/OT-Infrastruktur der NSV. Mindestanforderungen:

- Echtzeit-Korrelation sicherheitsrelevanter Ereignisse aus mind. folgenden Quellen:
  - Active Directory / Azure AD (Authentifizierungsereignisse)
  - Firewalls und Next-Generation-Firewalls
  - Endpoint Detection & Response (EDR) der NSV
  - OT-Netzwerk (passives Monitoring, keine aktiven Scans im OT-Bereich)
  - Syslog-Schnittstellen Server-Infrastruktur
- Datenhaltung Ereignisprotokolle: mind. 12 Monate online, mind. 36 Monate Archiv
- Datenschutzkonformität: Verarbeitung ausschließlich in ISO 27001-zertifizierten Rechenzentren in der EU; Auftragsverarbeitungsvertrag gem. Art. 28 DSGVO

**2.1.2 Threat Intelligence**

- Abonnement mindestens eines anerkannten Threat-Intelligence-Feeds (MITRE ATT&CK, strukturiert)
- Sektor-spezifische Threat Intelligence für KRITIS Verkehr (z.B. CISA ICS-CERT Advisories, BSI-Warnmeldungen)
- Monatliche Threat-Intelligence-Berichte an NSV-IT-Leitung

**2.1.3 Incident Detection und Response**

- 24/7/365-Überwachung durch SOC-Analysten (L1/L2/L3)
- Reaktionszeiten:
  - Kritischer Sicherheitsvorfall (Severity 1): Erstreaktion binnen 15 Minuten
  - Schwerwiegender Vorfall (Severity 2): Erstreaktion binnen 1 Stunde
  - Mittlerer Vorfall (Severity 3): Reaktion binnen 4 Stunden (Werktag) / 8 Stunden (Wochenende)
- Einleitung forensischer Erstmaßnahmen (Isolation, Sicherung volatiler Daten) auf Abruf
- Unterstützung bei BSI-Meldepflichten gem. § 8b BSIG (Meldeformular, Berichtsentwurf)

**2.1.4 Vulnerability Management**

- Monatliche Schwachstellenscans IT-Infrastruktur (authentifiziert)
- Halbjährliche Schwachstellenscans OT-Infrastruktur (passiv/nicht-invasiv)
- CVSS-basierte Priorisierung, Patchmanagement-Empfehlungen
- Quartalsbericht Vulnerability Status an IT-Leitung NSV

**2.1.5 Berichtspflichten und SLA**

- Monatlicher SOC-Bericht (Executive Summary + technisches Detail)
- Jährlicher Sicherheitslagebericht für NSV-Geschäftsführung
- SLA-Monitoring und Nachweis Einhaltung Reaktionszeiten (maschinell auswertbar)

#### 2.2 Los 2 – BSI-IT-Sicherheitsbeauftragten-Beratung

**2.2.1 Funktion ISB**

Der Auftragnehmer stellt einen qualifizierten ISB (mind. BSI-Grundschutz-Praktiker oder CISM) als externe Funktion gem. § 8a BSIG bereit. Aufgaben:

- Koordination und Vorbereitung des BSI-Nachweisverfahrens (alle zwei Jahre)
- Pflege des ISMS nach ISO 27001 (Dokumentation, interne Audits)
- Beratung Geschäftsführung zu IT-Sicherheitsstrategien
- Teilnahme an Krisenstab bei Sicherheitsvorfällen Severity 1/2

**2.2.2 ISMS-Dokumentation**

- Erstellung und Pflege Sicherheitsrichtlinien-Set (mind. 20 Richtlinien nach BSI-Grundschutz-Kompendium)
- Risikoanalyse und Behandlungsplan gem. ISO 27005

**2.2.3 Schulungen**

- Jährliche Security-Awareness-Schulung (alle Mitarbeiter NSV, ca. 350 Personen)
- Phishing-Simulationen (mind. 2 × jährlich)

---

### 3. Technische Rahmenbedingungen

- Anbindung: VPN-Zugang zum NSV-Rechenzentrum (IPSec, mind. 100 Mbit/s)
- Schnittstellen: REST-API für SIEM-Ereignisse, STIX/TAXII für Threat Intelligence
- Sprachliche Anforderungen: Alle Berichte und Kommunikation in deutscher Sprache
- Datenhaltungsort: Deutschland oder EU (kein Drittstaatentransfer ohne explizite Genehmigung)

### 4. Qualitätssicherung und Audits

- Jährliche externe Audits durch akkreditierte Prüfstelle (BSI-anerkannt)
- Recht des Auftraggebers auf Vor-Ort-Inspektion SOC-Standort mit 5 Werktagen Vorankündigung
- Penetrationstest NSV-Infrastruktur (mind. 1 × jährlich, durch zertifizierte Pentester, OSCP oder gleichwertig)

---

*Dokument-Ende Teil A Leistungsbeschreibung (Auszug für Testzwecke)*
