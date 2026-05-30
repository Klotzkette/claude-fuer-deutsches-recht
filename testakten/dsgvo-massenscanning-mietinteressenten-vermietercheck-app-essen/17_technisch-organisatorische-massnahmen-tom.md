# 17 — Technisch-Organisatorische Massnahmen (TOM) nach Art. 32 DSGVO

**Aktenzeichen:** DSB-NW-44/26
**Bearbeiter:** RAin Miriam Beckenbauer, externer IT-Sicherheitsberater SecureProof GmbH
**Datum:** 30. Januar 2026
**Betreff:** Bewertung und Sanierung der TOM bei VermieterCheck Solutions GmbH

---

## 1. Rechtsrahmen Art. 32 DSGVO

Art. 32 Abs. 1 DSGVO verpflichtet den Verantwortlichen und den Auftragsverarbeiter, unter Beruecksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, der Umstaende und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeit und Schwere des Risikos geeignete technische und organisatorische Massnahmen zu treffen.

**Regelbeispiele Art. 32 Abs. 1 DSGVO:**
- lit. a: Pseudonymisierung und Verschluesselung
- lit. b: Gewaehrleistung von Vertraulichkeit, Integritaet, Verfuegbarkeit und Belastbarkeit
- lit. c: Faehigkeit zur raschen Wiederherstellung nach Zwischenfaellen
- lit. d: Regelmaeßige Ueberpruefung, Bewertung und Evaluierung der Wirksamkeit

---

## 2. Ist-Analyse der TOM bei VCS (Stand Oktober 2025)

### 2.1 Infrastruktur-Sicherheit

| TOM-Bereich | Ist-Zustand | Bewertung |
|-------------|-------------|-----------|
| Datenverschluesselung (at rest) | AWS S3-SSE (AES-256) | Ausreichend |
| Datenverschluesselung (in transit) | TLS 1.2 (veraltet: TLS 1.3 Standard) | Unzureichend |
| Netzwerk-Segmentierung | VPC-Subnetz vorhanden, aber Staging = Produktion | Kritisch unzureichend |
| Zugangskontrolle | IAM-Rollen, aber GF-Account hat Admin-Vollzugriff | Mangelhaft |
| Patchmanagement | Keine standardisierte Patch-Strategie | Mangelhaft |
| SQL-Injection-Schutz | Fehlt (CVE-2026-0188) | Kritisch |
| Web Application Firewall | Nicht implementiert | Mangelhaft |

### 2.2 Organisatorische Massnahmen

| TOM-Bereich | Ist-Zustand | Bewertung |
|-------------|-------------|-----------|
| Datenschutzkonzept | Veraltet (2023, nicht aktuell) | Unzureichend |
| Schulungen Mitarbeiter | Letzte Schulung 2022 | Mangelhaft |
| Incident-Response-Plan | Nicht vorhanden | Kritisch |
| Zutrittskontrolle Serverraeume | Cloud (AWS) — kein physischer Server | Ausreichend |
| Datensicherung (Backup) | Taeglich, 30 Tage Retention | Ausreichend |
| Loeschkonzept | Nicht dokumentiert | Mangelhaft |
| Datenschutz-Folgenabschaetzung | Nicht durchgefuehrt (s. Akte 05) | Kritisch |

### 2.3 Ergebnis Ist-Analyse

Von 14 geprueften TOM-Bereichen sind 4 als „Ausreichend", 5 als „Mangelhaft" und 5 als „Unzureichend/Kritisch" bewertet. Dies entspricht einem erheblichen Sicherheitsdefizit, das die Datenpanne CVE-2026-0188 erst ermoeglichte.

---

## 3. Soll-Konzept: Neue TOM nach Stand der Technik

### 3.1 Technische Massnahmen (Prioritaet HOCH)

**Massnahme 1 — SQL-Injection-Abwehr:**
- Implementierung Prepared Statements und Parametrisierung in allen Datenbankabfragen
- Einsatz einer Web Application Firewall (AWS WAF oder Cloudflare Enterprise)
- Input-Validierung fuer alle API-Endpoints
- Frist: 31.01.2026 (bereits eingeleitet, Patch fuer CVE-2026-0188 aktiv)

**Massnahme 2 — TLS-Upgrade:**
- Upgrade aller API-Verbindungen auf TLS 1.3
- Deaktivierung TLS 1.0 und TLS 1.1
- Zertifikatspinning fuer kritische API-Verbindungen (Sundara Tech, Schufa-API)
- Frist: 15.02.2026

**Massnahme 3 — Netzwerk-Segmentierung:**
- Vollstaendige Trennung Staging- und Produktionsumgebung
- Keine Echtdaten im Staging (nur synthetische Testdaten)
- Separates VPC fuer Produktionsdatenbank
- Frist: 28.02.2026

**Massnahme 4 — Zugangskontrolle:**
- Entzug Admin-Vollzugriff fuer GF-Account
- Least-Privilege-Prinzip fuer alle IAM-Rollen
- Multi-Faktor-Authentifizierung fuer alle Produktionszugaenge
- Privileged Access Workstation (PAW) fuer Datenbankadministration
- Frist: 07.02.2026

**Massnahme 5 — Pseudonymisierung:**
- Pseudonymisierung aller Mietinteressenten-Daten vor Transfer an Sundara Tech
- Tokenisierung des ProspectScores (Score-Wert uebertragen, Name + Adresse bleiben in EU)
- Frist: 14.02.2026

### 3.2 Organisatorische Massnahmen (Prioritaet MITTEL)

**Massnahme 6 — Incident-Response-Plan:**
- Erstellung nach NIST Cybersecurity Framework und BSI IT-Grundschutz
- Rollen: CISO (Tarkan Bilgic), DSB (Kessler-Brandt), Kommunikationsverantwortlicher
- Meldeketten: 1h-Eskalation intern, 72h LDI NRW-Meldung
- Frist: 28.02.2026

**Massnahme 7 — Schulungen:**
- Jaehrliche DSGVO-Pflichtschulung fuer alle 38 Mitarbeiter
- Spezialschulung IT-Team zu Secure Coding und OWASP Top 10
- E-Learning-Plattform: TuVit (DSGVO-konform)
- Frist: 31.03.2026

**Massnahme 8 — Loeschkonzept:**
- Definition Loeschfristen pro Datenkategorie (Scoring-Daten: 24 Monate; Kontaktdaten: 36 Monate nach letzter Interaktion)
- Automatisiertes Loeschprotokoll mit Nachweis
- Frist: 15.02.2026

---

## 4. Gap-Analyse nach ISO 27001:2022

| ISO-27001-Kontroll | Status | Prioritaet Sanierung |
|-------------------|--------|---------------------|
| A 5.3 (Informationssicherheitsrollen) | Nicht vollstaendig | HOCH |
| A 5.24 (Informationssicherheitsvorfallsplanung) | Fehlt | KRITISCH |
| A 5.26 (Reaktion auf Sicherheitsvorfaelle) | Fehlt | KRITISCH |
| A 8.8 (Schwachstellenmanagement) | Fehlt (CVE-2026-0188 zeigt dies) | KRITISCH |
| A 8.25 (Sichere Entwicklung) | Partiell | HOCH |
| A 8.9 (Konfigurationsmanagement) | Partiell | MITTEL |

---

## 5. Dokumentation gegenueber LDI NRW

Im Rahmen des Aufsichtsverfahrens DSB-NW-44/26 wird VCS der LDI NRW bis zum 15.03.2026 folgende TOM-Nachweise uebergeben:
1. Aktualisiertes TOM-Dokument (Soll-Zustand nach Sanierung)
2. Penetrationstest-Bericht SecureProof GmbH (Neu-Test nach Sanierung)
3. Schulungsnachweise der Mitarbeiter
4. AVV-Nachweis mit Sundara Tech inkl. SCC
5. Nachweis Incident-Response-Plan-Implementierung

---

## Quellen

- DSGVO Art. 32 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- ISO/IEC 27001:2022 — [iso.org](https://www.iso.org/standard/82875.html)
- BSI IT-Grundschutz-Kompendium 2023 — [bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Kompendium/it-grundschutz-kompendium_node.html)
- OWASP Top 10 (2021) — [owasp.org](https://owasp.org/www-project-top-ten)
- NIST Cybersecurity Framework 2.0 — [nist.gov](https://www.nist.gov/cyberframework)
