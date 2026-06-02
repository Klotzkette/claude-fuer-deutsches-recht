# 17 — Technisch-Organisatorische Massnahmen (TOM) nach Art. 32 DSGVO

**Aktenzeichen:** DSB-NW-44/26
**Bearbeiter:** RAin Miriam Beckenbauer, externer IT-Sicherheitsberater SecureProof GmbH
**Datum:** 30. Januar 2026
**Betreff:** Bewertung und Sanierung der TOM bei VermieterCheck Solutions GmbH

---

## 1. Rechtsrahmen Art. 32 DSGVO

Art. 32 Abs. 1 DSGVO verpflichtet den Verantwortlichen und den Auftragsverarbeiter, unter Berücksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, der Umstände und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeit und Schwere des Risikos geeignete technische und organisatorische Massnahmen zu treffen.

**Regelbeispiele Art. 32 Abs. 1 DSGVO:**
- lit. a: Pseudonymisierung und Verschlüsselung
- lit. b: Gewährleistung von Vertraulichkeit, Integrität, Verfügbarkeit und Belastbarkeit
- lit. c: Fähigkeit zur raschen Wiederherstellung nach Zwischenfällen
- lit. d: Regelmäßige Überprüfung, Bewertung und Evaluierung der Wirksamkeit

---

## 2. Ist-Analyse der TOM bei VCS (Stand Oktober 2025)

### 2.1 Infrastruktur-Sicherheit

| TOM-Bereich | Ist-Zustand | Bewertung |
|-------------|-------------|-----------|
| Datenverschlüsselung (at rest) | AWS S3-SSE (AES-256) | Ausreichend |
| Datenverschlüsselung (in transit) | TLS 1.2 (veraltet: TLS 1.3 Standard) | Unzureichend |
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
| Zutrittskontrolle Serverräume | Cloud (AWS) — kein physischer Server | Ausreichend |
| Datensicherung (Backup) | Täglich, 30 Tage Retention | Ausreichend |
| Löschkonzept | Nicht dokumentiert | Mangelhaft |
| Datenschutz-Folgenabschaetzung | Nicht durchgeführt (s. Akte 05) | Kritisch |

### 2.3 Ergebnis Ist-Analyse

Von 14 geprüften TOM-Bereichen sind 4 als „Ausreichend", 5 als „Mangelhaft" und 5 als „Unzureichend/Kritisch" bewertet. Dies entspricht einem erheblichen Sicherheitsdefizit, das die Datenpanne CVE-2026-0188 erst ermöglichte.

---

## 3. Soll-Konzept: Neue TOM nach Stand der Technik

### 3.1 Technische Massnahmen (Priorität HOCH)

**Massnahme 1 — SQL-Injection-Abwehr:**
- Implementierung Prepared Statements und Parametrisierung in allen Datenbankabfragen
- Einsatz einer Web Application Firewall (AWS WAF oder Cloudflare Enterprise)
- Input-Validierung für alle API-Endpoints
- Frist: 31.01.2026 (bereits eingeleitet, Patch für CVE-2026-0188 aktiv)

**Massnahme 2 — TLS-Upgrade:**
- Upgrade aller API-Verbindungen auf TLS 1.3
- Deaktivierung TLS 1.0 und TLS 1.1
- Zertifikatspinning für kritische API-Verbindungen (Sundara Tech, Schufa-API)
- Frist: 15.02.2026

**Massnahme 3 — Netzwerk-Segmentierung:**
- Vollständige Trennung Staging- und Produktionsumgebung
- Keine Echtdaten im Staging (nur synthetische Testdaten)
- Separates VPC für Produktionsdatenbank
- Frist: 28.02.2026

**Massnahme 4 — Zugangskontrolle:**
- Entzug Admin-Vollzugriff für GF-Account
- Least-Privilege-Prinzip für alle IAM-Rollen
- Multi-Faktor-Authentifizierung für alle Produktionszugänge
- Privileged Access Workstation (PAW) für Datenbankadministration
- Frist: 07.02.2026

**Massnahme 5 — Pseudonymisierung:**
- Pseudonymisierung aller Mietinteressenten-Daten vor Transfer an Sundara Tech
- Tokenisierung des ProspectScores (Score-Wert übertragen, Name + Adresse bleiben in EU)
- Frist: 14.02.2026

### 3.2 Organisatorische Massnahmen (Priorität MITTEL)

**Massnahme 6 — Incident-Response-Plan:**
- Erstellung nach NIST Cybersecurity Framework und BSI IT-Grundschutz
- Rollen: CISO (Tarkan Bilgic), DSB (Kessler-Brandt), Kommunikationsverantwortlicher
- Meldeketten: 1h-Eskalation intern, 72h LDI NRW-Meldung
- Frist: 28.02.2026

**Massnahme 7 — Schulungen:**
- Jährliche DSGVO-Pflichtschulung für alle 38 Mitarbeiter
- Spezialschulung IT-Team zu Secure Coding und OWASP Top 10
- E-Learning-Plattform: TuVit (DSGVO-konform)
- Frist: 31.03.2026

**Massnahme 8 — Löschkonzept:**
- Definition Löschfristen pro Datenkategorie (Scoring-Daten: 24 Monate; Kontaktdaten: 36 Monate nach letzter Interaktion)
- Automatisiertes Löschprotokoll mit Nachweis
- Frist: 15.02.2026

---

## 4. Gap-Analyse nach ISO 27001:2022

| ISO-27001-Kontroll | Status | Priorität Sanierung |
|-------------------|--------|---------------------|
| A 5.3 (Informationssicherheitsrollen) | Nicht vollständig | HOCH |
| A 5.24 (Informationssicherheitsvorfallsplanung) | Fehlt | KRITISCH |
| A 5.26 (Reaktion auf Sicherheitsvorfälle) | Fehlt | KRITISCH |
| A 8.8 (Schwachstellenmanagement) | Fehlt (CVE-2026-0188 zeigt dies) | KRITISCH |
| A 8.25 (Sichere Entwicklung) | Partiell | HOCH |
| A 8.9 (Konfigurationsmanagement) | Partiell | MITTEL |

---

## 5. Dokumentation gegenüber LDI NRW

Im Rahmen des Aufsichtsverfahrens DSB-NW-44/26 wird VCS der LDI NRW bis zum 15.03.2026 folgende TOM-Nachweise übergeben:
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
