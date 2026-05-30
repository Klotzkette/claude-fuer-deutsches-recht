# 19 — ISO 27001 / TISAX: Compliance-Gap-Analyse

**Aktenzeichen:** intern (Compliance-Akte)
**Bearbeiter:** Externe Beratung SecureProof GmbH (Bochum), koordiniert RA Drosselberg
**Datum:** 01. Februar 2026
**Betreff:** Gap-Analyse ISO 27001:2022 und TISAX fuer VCS im Kontext der Vorfaelle

---

## 1. Ausgangssituation

VCS befindet sich in einem laufenden ISO-27001-Zertifizierungsprozess (Auditor: TuVit GmbH, Essen, Stage-2-Audit geplant April 2026). Durch die Vorfaelle (CVE-2026-0188, Datenpanne, fehlende TOM) ist dieses Zertifizierungsprojekt gefaehrdet.

TISAX (Trusted Information Security Assessment Exchange) ist fuer VCS relevant, wenn Automobilindustrie-Kunden (Vermieter mit Kfz-Lease-Hintergrund) oder potenzielle Kooperationspartner eine TISAX-Bewertung fordern. Derzeit hat VCS keine TISAX-Anforderung — es wird jedoch als Qualitaetsmerkmal fuer den Markt angestrebt.

---

## 2. ISO 27001:2022 — Gap-Analyse

### 2.1 Kontext der Organisation (Kapitel 4)

| Anforderung | Status | Massnahme |
|-------------|--------|-----------|
| 4.1 Verstehen der Organisation | Partiell (SWOT vorhanden, aber veraltet) | Aktualisieren |
| 4.2 Anforderungen interessierter Parteien | Fehlt (Kunden, Regulatoren nicht systematisch erfasst) | Erstellen |
| 4.3 ISMS-Anwendungsbereich | Definiert (Cloud: AWS eu-central-1) | Ausreichend |
| 4.4 ISMS und seine Prozesse | Unvollstaendig (keine vollstaendige Prozessdokumentation) | Ergaenzen |

### 2.2 Fuehrung (Kapitel 5)

| Anforderung | Status | Massnahme |
|-------------|--------|-----------|
| 5.1 Fuehrung und Verpflichtung | Nicht dokumentiert (GF hat DSFA ignoriert) | Sicherheitserklarung GF |
| 5.2 Informationssicherheitspolitik | Vorhanden (2022) | Aktualisieren |
| 5.3 Rollen und Verantwortlichkeiten | Partiell (kein CISO formell ernannt) | CISO-Ernennung |

### 2.3 Unterstützung (Kapitel 7)

| Anforderung | Status | Massnahme |
|-------------|--------|-----------|
| 7.2 Kompetenz | Schulungen nicht dokumentiert | Schulungsnachweise |
| 7.3 Bewusstsein | Kein Awareness-Programm | Awareness-Kampagne |
| 7.4 Kommunikation | Interne IS-Kommunikation fehlt | Policy-Kommunikation |

### 2.4 Betrieb (Kapitel 8)

| Anforderung | Status | Massnahme |
|-------------|--------|-----------|
| 8.1 Betriebsplanung | Partiell | Ergaenzen |
| 8.2 Risikobeurteilung | Nicht jaehrlich durchgefuehrt | Jaehrlicher Zyklus |
| 8.3 Risikobehandlung | Keine dokumentierten Massnahmen zu Risiken | Risikobehandlungsplan |

### 2.5 Leistungsbewertung (Kapitel 9)

| Anforderung | Status | Massnahme |
|-------------|--------|-----------|
| 9.1 Ueberwachung und Messung | Fehlt (kein KPI-System fuer IT-Sicherheit) | KPI-Set definieren |
| 9.2 Internes Audit | Kein internes Audit durchgefuehrt | Audit-Programm |
| 9.3 Managementbewertung | Fehlt | Jaehrliches Review |

### 2.6 Annex A Kontrollen (Auswahl kritischer Luecken)

| Kontrolle | Beschreibung | Status |
|-----------|-------------|--------|
| A 5.23 | Informationssicherheit fuer Cloud-Dienste | Partiell |
| A 5.24 | Vorfallsmanagement-Planung | **Fehlt** |
| A 5.26 | Reaktion auf Vorfaelle | **Fehlt** (CVE-2026-0188 zeigt dies) |
| A 5.30 | IKT-Bereitschaft fuer Betriebskontinuitaet | Fehlt |
| A 8.8 | Schwachstellenmanagement | **Fehlt** (SQL-Injection nicht erkannt) |
| A 8.25 | Sicherheit im Entwicklungslebenszyklus | Partiell |
| A 8.29 | Sicherheitstests in der Entwicklung | Unzureichend (kein SAST/DAST im CI/CD) |

---

## 3. TISAX-Anforderungen (VDA ISA 6.0)

Fuer den Fall einer kuenftigen TISAX-Anforderung:

| TISAX-Assessment-Ziel | Relevanz fuer VCS | Prueftiefe |
|-----------------------|------------------|------------|
| Information Security (AL 2) | Hoch (Kundendaten in SaaS-Plattform) | Standard |
| Prototype Protection (AL 3) | Nicht einschlaegig | - |
| Data Protection | Hoch (DSGVO-Bezug) | Erweitert |

**Empfehlung:** TISAX-Assessment erst nach vollstaendiger ISO-27001-Zertifizierung anstreben (Synergieeffekte). Zieldatum: Q1 2027.

---

## 4. Auswirkungen auf ISO-Zertifizierungsprojekt

### 4.1 Non-Conformities (Nicht-Konformitaeten)

Aus den identifizierten Luecken ergeben sich folgende Non-Conformities, die im Stage-2-Audit zur Feststellung oder sogar zur Versagung der Zertifizierung fuehren koennen:

| Non-Conformity | Schwere | Zeitrahmen Behebung |
|----------------|---------|---------------------|
| Kein Vorfallsmanagementprozess (A 5.24, A 5.26) | Major NC | bis 15.03.2026 |
| Kein Schwachstellenmanagement (A 8.8) | Major NC | bis 28.02.2026 |
| Kein internes Audit | Major NC | bis 31.03.2026 |
| Schulungen nicht dokumentiert (7.2) | Minor NC | bis 15.03.2026 |
| Kein CISO ernannt | Minor NC | bis 14.02.2026 |

### 4.2 Massnahmen zur Aufrechterhaltung des Zertifizierungsprojekts

1. **Sofort (bis 07.02.2026):** CISO-Ernennung (Tarkan Bilgic als interimistischer CISO)
2. **Kurzfristig (bis 28.02.2026):** Vorfallsmanagementprozess dokumentiert und implementiert
3. **Kurzfristig (bis 28.02.2026):** Schwachstellenscan und Patching-Policy
4. **Mittelfristig (bis 31.03.2026):** Internes Audit durchgefuehrt, Massnahmen dokumentiert

---

## 5. Bedeutung fuer Bussgeldverfahren (LDI NRW)

Der Nachweis einer ISO-27001-Zertifizierung (oder zumindest eines fortgeschrittenen Zertifizierungsprozesses) kann als Milderungsgrund im Bussgeldbescheidsverfahren wirken (Art. 83 Abs. 2 lit. j DSGVO: Einhaltung eines genehmigten Verhaltenskodex oder eines Zertifizierungsmechanismus).

**Empfehlung:** Einreichung eines Statusberichts ueber den ISO-27001-Prozess und die Non-Conformity-Behebung als Anlage zur Stellungnahme an LDI NRW.

---

## Quellen

- ISO/IEC 27001:2022 — [iso.org](https://www.iso.org/standard/82875.html)
- VDA ISA 6.0 (TISAX-Anforderungskatalog) — [enx.com](https://www.enx.com/de-DE/TISAX)
- DSGVO Art. 32, 83 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- BSI IT-Grundschutz — [bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html)
- OWASP ASVS 4.0 (Application Security Verification Standard) — [owasp.org](https://owasp.org/www-project-application-security-verification-standard)
