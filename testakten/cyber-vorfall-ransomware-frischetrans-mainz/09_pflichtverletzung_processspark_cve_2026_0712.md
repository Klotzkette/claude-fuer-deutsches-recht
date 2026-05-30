# Pflichtverletzungsanalyse ProcessSpark Cloud AG — CVE-2026-0712

**Aktenstück:** 09  
**Datum:** 10.05.2026  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Bearbeiter:** RA Lukas Drosten, Fachanwalt für IT-Recht

---

## 1. Technische Beschreibung der Schwachstelle CVE-2026-0712

### 1.1 Schwachstelle

**CVE-Identifikator:** CVE-2026-0712  
**Betroffene Software:** SAP NetWeaver Application Server ABAP, Versionen 7.50–7.89 (vor Patch-Level SP15)  
**Typ:** Remote Code Execution (RCE) via SSRF und Deserialisierungsfehler im ICM-Subsystem  
**CVSS Base Score:** 9.8 (Critical)  
**SAP Security Note:** 3411852  
**Veröffentlichung:** 18.02.2026 (SAP Patchday Februar 2026)  
**Verfügbarer Patch:** SAP ABAP SP15 (Support Package Stack)

**Technische Beschreibung:**  
Die Schwachstelle ermöglicht einem nicht authentifizierten Angreifer aus dem Netzwerk heraus, beliebigen Code auf dem SAP-Applikationsserver auszuführen. Der Angriff erfordert keine Benutzerinteraktion und keinen gültigen Account. Die Schwachstelle liegt im Internet Communication Manager (ICM) des SAP NetWeaver AS ABAP und wird durch einen Deserialisierungsfehler bei der Verarbeitung von HTTP-Anfragen ausgelöst.

### 1.2 Exploitbarkeit

Zum Zeitpunkt des Angriffs (04./05.05.2026) existierten öffentlich bekannte Proof-of-Concept-Exploits für CVE-2026-0712:
- Exploit-DB Eintrag: EDB-ID 52847 (veröffentlicht 01.03.2026)
- Metasploit-Modul: `exploit/multi/http/sap_netweaver_icm_rce` (verfügbar ab 10.03.2026)

Die leichte Exploitbarkeit war seit März 2026 bekannt und wurde vom BSI in seiner Warnung BSI-2026-0312-SAP-KRITIS ausdrücklich hervorgehoben.

---

## 2. Pflichtverletzung im Einzelnen

### 2.1 Verletzung der Patchpflicht (§ 12 Nachtrag 3)

ProcessSpark Cloud AG war nach § 12 Abs. 2 Nachtrag 3 des Vertrages verpflichtet, Patches für Schwachstellen mit CVSS-Score ≥ 9,0 innerhalb von **14 Tagen** nach Veröffentlichung einzuspielen.

**Frist:** 18.02.2026 + 14 Tage = **04.03.2026**  
**Tatsächliche Einspielung:** Nacht 28./29.04.2026  
**Verzug:** 55 Tage

### 2.2 Verletzung der Informationspflicht

ProcessSpark hatte die Mandantin zu keinem Zeitpunkt über:
- die Existenz der Schwachstelle CVE-2026-0712 informiert
- den Patch-Rückstand informiert
- mögliche Interim-Maßnahmen (z.B. Deaktivierung des ICM, Netzwerk-Segmentierung) empfohlen

Dies verletzt die vertragliche Nebenpflicht zur Information und Beratung (§ 241 Abs. 2 BGB, sog. Schutz- und Rücksichtnahmepflichten). IT-Dienstleister sind nach ständiger BGH-Rechtsprechung verpflichtet, ihren Auftraggeber auf erkannte oder erkennbare sicherheitsrelevante Risiken hinzuweisen (vgl. BGH, Urteil vom 04.03.2010 — III ZR 79/09, NJW 2010, 1817; BGH, Urteil vom 15.05.2012 — X ZR 75/11).

### 2.3 Verletzung der Firewall-Wartungspflicht (Mitursächlichkeit)

Die forensische Untersuchung ergab, dass die Firewall-Firmware seit Oktober 2025 nicht aktualisiert worden war. Die Netzwerk-Segmentierung entspricht nicht dem Stand der Technik (kein Zero-Trust-Konzept, unzureichende Micro-Segmentierung). Diese Mängel sind dem Pflichtenbereich der InsoTec Systems GmbH (Netzwerkbetreuungsvertrag) zuzurechnen.

**Hinweis für spätere Prozesstaktik:** Möglicherweise besteht eine gesamtschuldnerische Haftung von ProcessSpark Cloud AG und InsoTec Systems GmbH, was die Rechtsdurchsetzung erleichtert. Eine Analyse des InsoTec-Vertrages ist separat zu führen.

---

## 3. Kausalität zwischen Pflichtverletzung und Schaden

### 3.1 Conditio-sine-qua-non-Test

Der Kausalitätsbeweis lässt sich wie folgt führen:

1. Wäre der Patch CVE-2026-0712 innerhalb der vertragsgemäßen 14-Tage-Frist (bis 04.03.2026) eingespielt worden, wäre die Schwachstelle am 04./05.05.2026 nicht mehr vorhanden gewesen.

2. Die forensische Analyse belegt eindeutig (Log-Auswertung, Malware-Analyse), dass der initiale Zugang über CVE-2026-0712 erfolgte. Ohne diese Schwachstelle wäre der Angriff nicht möglich gewesen.

3. Ergo: Die Pflichtverletzung (verzögerte Patcheinspielung) ist conditio sine qua non für den eingetretenen Schaden.

### 3.2 Adäquanzkausalität

Es entspricht dem gewöhnlichen Lauf der Dinge und der allgemeinen Lebenserfahrung, dass:
- eine über 55 Tage bekannte, öffentlich exploitierbare CVSS-9.8-Schwachstelle in einem unternehmenskritischen ERP-System
- bei aktivem Bedrohungsakteur (AkiraNext war seit 2025 bekannt als SAP-angreifende Gruppe)
- zu einem Ransomware-Angriff führt.

Die Adäquanzkausalität ist gegeben. Ein durchschnittlicher professioneller IT-Dienstleister musste dieses Risiko vorhersehen.

### 3.3 Beweisführung / Beweislast

Die Beweislast für die Pflichtverletzung liegt grundsätzlich beim Gläubiger (Frischetrans). Folgende Beweise sind verfügbar:

- SAP Security Note 3411852 (offizieller Nachweis der Schwachstelle und des Patch-Datums)
- ProcessSpark-Patch-Log (anzufordern per Auskunftsanspruch, § 242 BGB)
- Forensischer Bericht CyberForensik RheinMain GmbH (Angriffsvektor-Nachweis)
- BSI-Warnung BSI-2026-0312-SAP-KRITIS (Beweis für öffentliche Wahrnehmung)
- Metasploit-Zeitstempel (Exploit-Verfügbarkeit)

---

## 4. Haftungsausschlüsse und Gegenargumente von ProcessSpark

### 4.1 Mögliche Einwände ProcessSpark

**Einwand 1: Höhere Gewalt**  
ProcessSpark könnte argumentieren, der Ransomware-Angriff sei ein unvorhersehbares Ereignis (höhere Gewalt). Dies ist abzulehnen: Ransomware-Angriffe auf SAP-Systeme sind seit Jahren dokumentiert. CVE-2026-0712 war öffentlich bekannt. Höhere Gewalt scheidet aus.

**Einwand 2: Mitverschulden der Mandantin**  
ProcessSpark könnte ein Mitverschulden (§ 254 BGB) der Frischetrans geltend machen, etwa wegen unzureichender Netzwerksegmentierung oder fehlender MFA. Dem ist entgegenzuhalten:
- Die Netzwerkwartung war an InsoTec ausgelagert (keine unmittelbare Verantwortung der Frischetrans)
- Die MFA-Anforderung war im Vertrag mit ProcessSpark nicht explizit vereinbart
- Ein verbleibendes Mitverschulden ist realistisch auf 10–20 % zu schätzen

**Einwand 3: Haftungsbeschränkung (§ 16 Vertrag)**  
Der Vertrag sieht eine Haftungsbeschränkung auf 12 Monatsvergütungen (177.600 EUR) bei einfacher Fahrlässigkeit vor. Diese Klausel ist nach § 309 Nr. 7 lit. b) BGB unwirksam, soweit sie grob fahrlässiges oder vorsätzliches Verhalten erfassen würde. Ein 55-tägiger Patch-Rückstand bei einer CVSS-9.8-Schwachstelle trotz vertraglicher 14-Tages-Pflicht begründet starke Indizien für **grobe Fahrlässigkeit** (bewusste Missachtung erkennbarer Gefahr).

### 4.2 Rechtliche Einschätzung

Die Haftungsbeschränkungsklausel ist mit hoher Wahrscheinlichkeit als unwirksam oder zumindest nicht einschlägig anzusehen (grobe Fahrlässigkeit). ProcessSpark haftet für den Gesamtschaden. Eine Reduzierung um 10–20 % wegen möglichem Mitverschulden ist einzukalkulieren.

---

## 5. Forderungsschreiben / Weitere Vorgehensweise

Das Klageandrohungsschreiben (Aktenstück 10) wird folgende Forderungen beinhalten:

1. Zahlung der Vertragsstrafe: 518 EUR  
2. Zahlung von Schadensersatz: vorläufig 625.000 EUR (vorbehaltlich des forensischen Abschlussberichts)  
3. Vorlage der vollständigen Patch-Logs  
4. Außerordentliche Kündigung des Vertrages (vorbehalten)  
5. Frist: 14 Tage ab Zugang des Schreibens (26.05.2026)

Bei fruchtlosem Fristablauf: Klageerhebung am LG Mainz (AZ geplant: 3 O 88/26).
