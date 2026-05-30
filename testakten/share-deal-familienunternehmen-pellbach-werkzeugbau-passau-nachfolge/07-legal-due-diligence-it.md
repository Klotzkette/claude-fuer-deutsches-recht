# 07 — Legal Due Diligence: IT, IP und Datenschutz

**Aktenzeichen:** SuP/2026-0041-CES
**Bearbeiter IT/IP:** RA Dr. Steffen Brandner, Schwingenstein und Partner München
**Datum:** 01. März 2026

---

## 1. IT-Lizenzaudit — SAP

### Ausgangslage

Pellbach Werkzeugbau betreibt SAP S/4HANA (On-Premise, Lizenz 2019) für ERP (FI, CO, MM, PP, SD). Im Rahmen der VDD wurde ein SAP-Lizenz-Audit aus dem Jahr 2025 bekannt, das noch nicht abgeschlossen ist.

### Befunde

- SAP-Lizenzmessung (USMM-Report März 2025): Named User: 87 vertraglich, 104 tatsächlich aktiv → Unterdeckung 17 Named User Professional (ca. 68 TEUR Nachzahlung geschätzt)
- Suzhou WFOE: Betreibt SAP auf chinesischem Server; Sub-Lizenz vom deutschen Hauptlizenzvertrag nicht explizit geregelt → SAP-Risiko Unterlizenzen China: bis 150 TEUR
- **Gesamtrisiko SAP-Audit: ca. 218 TEUR**; Verkäufer stellt Indemnity bereit (Disclosure Letter)

---

## 2. Eigenentwicklungen und IP

### Werkzeugauslegungs-Software „PellCAD 3.0"

Eigenentwicklung seit 2016; ca. 4,5 Mio. EUR Entwicklungskosten; Urheberrechte liegen bei der KG (Arbeitnehmererfindungen § 7 ArbNErfG korrekt abgelöst). Kein Drittanbieter-IP eingeflossen. Lizenz an Suzhou-Tochter vorhanden (schriftlicher Lizenzvertrag 2019).

### Marken

„PellCAD" und „Pellbach Werkzeugbau" als Wortmarken beim DPMA eingetragen (Nr. 302019000441 und 302019000442); EU-Unionsmarken beantragt 2021, erteilt 2022.

---

## 3. DSGVO-Compliance

- Datenschutzbeauftragter: extern (Kanzlei Datenwächter GbR, Regensburg); Verzeichnis der Verarbeitungstätigkeiten vorhanden, zuletzt aktualisiert 02/2025
- Kundendaten: B2B; kein Consumer-Business; DSGVO-Risiko überschaubar
- China: Personendatenübermittlung an Suzhou nach Art. 46 Abs. 2 DSGVO (SCCs 2021): SCCs-Vertragsanbahnung mit Suzhou abgeschlossen; technische Schutzmaßnahmen (Verschlüsselung) implementiert
- China PIPL: China Personal Information Protection Law (2021) — Pelbach Suzhou hat lokale Compliance-Prüfung durchgeführt; Ergebnis: weitgehend compliant; ein offener Punkt (Aufbewahrungsfristen Produktionsdaten)

---

## 4. OT-Security (Operational Technology, Produktion)

- Werke Passau I und II: Produktionsanlagen SPS-gesteuert (Siemens S7); Netzwerktrennung IT/OT: teilweise (VLAN implementiert, jedoch kein vollständiges Air-Gap)
- Penetrationstest-Ergebnis 2025: 3 kritische Schwachstellen in Siemens-Steuerung identifiziert; gepatcht Q4 2025
- Cyber-Versicherung: vorhanden (Allianz, 5 Mio. EUR Deckung)
- **DD-Empfehlung:** Sicherheitsaudit vor Closing durch neutralen Dritten (Budget ca. 80 TEUR); W&I-Versicherer hat OT-Audit als Auflage genannt

---

## 5. Kritische IT-Abhängigkeiten

| System | Anbieter | Vertragslaufzeit | Risiko bei Change of Control |
|---|---|---|---|
| SAP S/4HANA | SAP AG | 2025-2029; kündbar mit 6 Monaten | Change-of-Control-Klausel: Zustimmung SAP erforderlich → Gespräch initiiert |
| CAD-Software CATIA | Dassault Systèmes | Perpetual-Lizenz 2021 | Kein Change-of-Control-Risiko |
| Cloud-Backup | Microsoft Azure | Monatlich kündbar | Kein Risiko |
| CRM (Salesforce) | Salesforce | 2024-2026; Verlängerung ausstehend | Prolongation vor Closing gesichert |

**Bearbeiter:** RA Dr. Steffen Brandner | SuP/2026-0041-CES
