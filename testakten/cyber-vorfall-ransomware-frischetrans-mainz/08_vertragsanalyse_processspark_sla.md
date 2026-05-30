# Vertragsanalyse ProcessSpark Cloud AG — SLA-Bewertung und Pflichtverletzung

**Aktenstück:** 08  
**Datum der Analyse:** 08.–10.05.2026  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Gegner:** ProcessSpark Cloud AG, Leopoldstraße 88, 80802 München  
**Bearbeiter:** RA Lukas Drosten, Fachanwalt für IT-Recht

---

## 1. Vertragsgrundlage

Zwischen der Frischetrans Mittelrhein GmbH und der ProcessSpark Cloud AG besteht ein **IT-Betriebsvertrag (SaaS- und Managed-Service-Vertrag)** vom 15.03.2021, zuletzt geändert durch Nachtrag 3 vom 01.07.2024 (nachfolgend: „Vertrag"). Der Vertrag hat eine Laufzeit bis 31.12.2027 mit einer Kündigungsfrist von 6 Monaten zum Jahresende.

### Vertragsgegenstand (§ 1 Vertrag)

ProcessSpark Cloud AG verpflichtet sich zur:
1. Bereitstellung, Betrieb und Wartung des ERP-Systems SAP S/4HANA (Lizenz-Management, Hosting auf ProcessSpark-Infrastruktur oder on-premises-Betreuung)
2. Durchführung von Sicherheitsupdates und Patches gemäß herstellerseitigem Release-Management
3. Gewährleistung der Systemverfügbarkeit von mind. 99,5 % p.m. (Kernbetriebszeiten: Mo–Fr 06:00–22:00 Uhr)
4. Incident-Response-Service Level: P1 (Kritisch) — Erstreaktion binnen 30 Minuten, Lösung binnen 4 Stunden

### SLA-Bestimmungen (§ 8 Vertrag)

| Service Level | Definition | Reaktionszeit | Lösungszeit |
|---|---|---|---|
| P1 — Kritisch | Systemausfall, Datenverlust-Risiko | 30 Minuten | 4 Stunden |
| P2 — Hoch | Erhebliche Funktionseinschränkung | 2 Stunden | 8 Stunden |
| P3 — Mittel | Eingeschränkte Funktion | 4 Stunden | 24 Stunden |
| P4 — Niedrig | Geringfügige Störung | 8 Stunden | 72 Stunden |

### Patchmanagement-Klausel (§ 12 Vertrag, Nachtrag 3)

*Auszug § 12 Abs. 2 Nachtrag 3:*

> „ProcessSpark Cloud AG verpflichtet sich, sicherheitsrelevante Patches und Updates für das SAP S/4HANA-System, insbesondere für Schwachstellen mit CVSS-Score 7,0 und höher (High und Critical), innerhalb von **30 Tagen** nach offizieller Bereitstellung durch den Hersteller SAP SE einzuspielen. Für Schwachstellen mit CVSS-Score 9,0 und höher (Critical) beträgt die Frist **14 Tage**. Ausnahmen bedürfen der vorherigen schriftlichen Zustimmung des Auftraggebers."

### SLA-Pönale (§ 14 Vertrag)

*Auszug § 14 Abs. 3:*

> „Bei nachgewiesener schuldhafter Verletzung der Patchmanagement-Fristen gemäß § 12 Abs. 2 hat der Auftragnehmer für je angefangene 7 Tage Verzug eine Vertragsstrafe in Höhe von **0,5 % der monatlichen Vergütung** zu leisten, maximal jedoch **5 % der monatlichen Vergütung** (Höchstbetrag). Dies schließt weitergehende Schadensersatzansprüche nicht aus."

Monatliche Vergütung: 14.800 EUR netto.

---

## 2. Analyse der Pflichtverletzung CVE-2026-0712

### 2.1 Zeitlinie CVE-2026-0712

| Datum | Ereignis |
|---|---|
| 18.02.2026 | SAP veröffentlicht Security Note für CVE-2026-0712 (SAP NetWeaver AS ABAP — Remote Code Execution) |
| 18.02.2026 | CVSS-Score: **9.8 (Critical)** — kritischste Einstufung |
| 18.02.2026 | Patch-Frist (14 Tage für Critical): **04.03.2026** |
| 04.03.2026 | Ablauf der 14-Tage-Frist — Patch noch nicht eingespielt |
| 20.03.2026 | Verlängerte Frist nach internem ProcessSpark-Standard (30 Tage) — auch überschritten |
| 28./29.04.2026 | ProcessSpark spielt den Patch tatsächlich ein (Wartungsfenster Nacht 28.04./29.04.2026) |
| 04.05.2026 | AkiraNext nutzt CVE-2026-0712 für initialen Zugang — Patch 5 Tage zuvor war zu spät |

**Verzugsdauer:** 18.02.2026 (Bekanntgabe) bis 28.04.2026 (Einspielung) = **69 Tage**  
**Vertraglich geschuldete Frist (Critical, CVSS 9.8):** 14 Tage  
**Überschreitung:** 55 Tage

Alternativ gemessen an der 30-Tage-Frist für „High":  
Fälligkeitsdatum 20.03.2026 — tatsächliche Einspielung 28.04.2026 = **39 Tage Verzug**

### 2.2 CVSS-Bewertung CVE-2026-0712

Die Schwachstelle CVE-2026-0712 wurde in der offiziellen SAP Security Note wie folgt beschrieben:

- **Typ:** Remote Code Execution (RCE) in SAP NetWeaver Application Server ABAP
- **CVSS Base Score:** 9.8 (Critical)
- **Attack Vector:** Network
- **Authentication:** None required
- **User Interaction:** None required
- **Verfügbarkeit:** Vollständige Kompromittierung möglich

Diese Einstufung macht CVE-2026-0712 zu einer der kritischsten SAP-Schwachstellen des Jahres 2026. Der BSI und CERT@VDE hatten eigene Warnungen herausgegeben.

### 2.3 Verschulden der ProcessSpark Cloud AG

Der Verzug von ProcessSpark bei der Einspielung des Patches ist schuldhaft:

1. **Kenntnis:** Die Schwachstelle und der verfügbare Patch waren seit 18.02.2026 öffentlich bekannt.
2. **Vertragliche Pflicht:** § 12 Abs. 2 Nachtrag 3 des Vertrages sieht für Critical-Patches eine 14-Tages-Frist vor.
3. **Keine Ausnahme beantragt:** ProcessSpark hat keine schriftliche Ausnahme-Genehmigung bei der Frischetrans eingeholt.
4. **Kein Hinweis an Mandantin:** ProcessSpark hat die Frischetrans nicht über den bekannten Patch-Rückstand informiert, was einer eigenständigen Pflichtverletzung entspricht (Informationspflicht aus § 241 Abs. 2 BGB).

---

## 3. Ansprüche der Mandantin

### 3.1 Vertragsstrafe (§ 14 Abs. 3 Vertrag)

Verzug: 55 Tage (über die 14-Tage-Frist hinaus) → 7 angefangene Sieben-Tages-Perioden × 0,5 % = **3,5 % der Monatsvergütung**

Vertragsstrafe: 14.800 EUR × 3,5 % = **518 EUR**

Hinweis: Die vertragliche Pönale ist angesichts des entstandenen Schadens von erheblich geringerem Wert als der Schadensersatzanspruch. Die Pönale ist neben dem Schadensersatz geltend zu machen (§ 340 Abs. 2 BGB).

### 3.2 Schadensersatz (§§ 280, 281, 631, 634 BGB i.V.m. Vertrag)

ProcessSpark hat eine vertraglich geschuldete Leistung (rechtzeitiger Sicherheitspatch) schuldhaft nicht rechtzeitig erbracht. Die Kausalität zwischen verspätetem Patch und Ransomware-Angriff ist nach derzeitigem forensischen Befund gegeben (CVE-2026-0712 war der initiale Angriffsvektor).

**Haftungsumfang:**

Nach §§ 280, 281 BGB schuldet ProcessSpark vollen Schadensersatz für den durch die Pflichtverletzung verursachten Schaden. Die Haftungsbeschränkungsklausel im Vertrag (§ 16 Abs. 2: Haftung begrenzt auf einfache Fahrlässigkeit auf 12 Monatsvergütungen = 177.600 EUR) ist im Hinblick auf § 309 Nr. 7 BGB und die Schwere der Pflichtverletzung einer AGB-rechtlichen Prüfung zu unterziehen.

**Voraussichtliche Schadensposition ProcessSpark:**

| Schadensposition | Betrag |
|---|---|
| IT-Wiederherstellungskosten | 180.000–220.000 EUR |
| Betriebsausfallschaden Logistik | 320.000–450.000 EUR |
| Forensikkosten | 45.000–65.000 EUR |
| Rechtskosten | 80.000–120.000 EUR |
| **Gesamt** | **625.000–855.000 EUR** |

Eine DSGVO-Bußgeld-Erstattung durch ProcessSpark ist theoretisch möglich, aber rechtlich komplex (DSGVO-Verstöße sind primär dem Verantwortlichen zuzurechnen, Regress gegen Auftragsverarbeiter/IT-Dienstleister möglich).

### 3.3 Kündigung aus wichtigem Grund

Die schwerwiegende Pflichtverletzung (Patch-Rückstand an einer CVSS-9.8-Schwachstelle mit verheerenden Folgen) berechtigt die Frischetrans zur außerordentlichen Kündigung des Vertrages aus wichtigem Grund nach § 626 BGB (Dienstvertrag) bzw. §§ 643, 649 BGB (Werkvertrag). Eine Abmahnung ist bei der Schwere der Pflichtverletzung entbehrlich.

Die Kündigung ist in der Klageandrohung (Aktenstück 10) angekündigt, aber noch nicht ausgesprochen, um Verhandlungsmasse zu erhalten.

---

## 4. Prozessrechtliche Überlegungen

**Gerichtsstand:** LG Mainz gemäß Gerichtsstandsklausel (§ 18 Vertrag; Gerichtsstand Mainz für Streitigkeiten zwischen den Parteien). Geplantes Aktenzeichen: 3 O 88/26.

**Streitwert:** ca. 625.000–855.000 EUR (je nach Schadensnachweis) + Vertragsstrafenforderung + ggf. DSGVO-Regress → Streitwert aller Voraussicht nach **> 500.000 EUR**.

**Zuständigkeit:** LG Mainz ist sachlich zuständig (§ 71 GVG, Streitwert > 5.000 EUR).

**Beweissicherung:** Forensischer Abschlussbericht (CyberForensik RheinMain GmbH), SAP-Security-Note CVE-2026-0712, Patch-Log ProcessSpark (per Auskunftsanspruch einzufordern), Vertrag inkl. Nachtrag 3.

**Verjährung:** §§ 195, 199 BGB — Verjährungsfrist 3 Jahre ab Jahresende 2026, Ablauf 31.12.2029.
