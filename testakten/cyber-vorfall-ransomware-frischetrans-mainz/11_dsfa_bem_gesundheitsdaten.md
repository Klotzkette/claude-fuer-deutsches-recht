# Datenschutz-Folgenabschätzung (DSFA) — BEM-Gesundheitsdaten

**Aktenstück:** 11  
**Datum:** 14.05.2026  
**Erstellt durch:** RA Lukas Drosten (Kanzlei Drosten & Pekonkur) gemeinsam mit Markus Feilke (Datenschutzbeauftragter, Datenschutzkanzlei Rhein-Main)  
**Mandantin:** Frischetrans Mittelrhein GmbH  
**Rechtsgrundlage:** Art. 35 DSGVO, § 67 SGB IX (BEM-Verfahren)

---

## 1. Anlass der DSFA

Der Ransomware-Angriff vom 06.05.2026 hat die Frischetrans Mittelrhein GmbH veranlasst, die bestehende Datenverarbeitungstätigkeit für das Betriebliche Eingliederungsmanagement (BEM) einer Datenschutz-Folgenabschätzung zu unterziehen. Diese DSFA wurde durch folgenden Umstand zwingend ausgelöst:

1. **Erhöhtes Risiko durch Datenpanne:** Die exfiltrierten Daten umfassen Gesundheitsdaten im Sinne des Art. 9 Abs. 1 DSGVO (besondere Kategorie personenbezogener Daten) von 38 Beschäftigten aus BEM-Verfahren. Diese Kategorie von Daten verlangt nach Art. 35 Abs. 3 lit. b) DSGVO grundsätzlich eine vorherige DSFA.

2. **Rückfrage der LfDI RLP:** Die Datenschutzbehörde hat in ihrem Schreiben vom 09.05.2026 (Ref. LfDI-RLP-2026-0508-4419) um Vorlage einer DSFA für diese Verarbeitungstätigkeit gebeten.

---

## 2. Beschreibung der Verarbeitungstätigkeit

### 2.1 Zweck der Verarbeitung

Frischetrans führt gemäß § 167 SGB IX (früher § 84 SGB IX a.F.) das BEM-Verfahren für Beschäftigte durch, die innerhalb eines Jahres länger als sechs Wochen ununterbrochen oder wiederholt arbeitsunfähig waren. Zweck ist die Wiedereingliederung und Prävention weiterer Ausfallzeiten.

### 2.2 Art der verarbeiteten Daten

| Datenkategorie | Einstufung | Anzahl Betroffene |
|---|---|---|
| Diagnosen (Erkrankungen) | Art. 9 DSGVO (besondere Kategorie) | 38 |
| Therapieverläufe, Behandlungsberichte | Art. 9 DSGVO | 38 |
| Ärztliche Atteste und Gutachten | Art. 9 DSGVO | 38 |
| Betriebsärztliche Bewertungen | Art. 9 DSGVO | 38 |
| Rehabilitationsmaßnahmen | Art. 9 DSGVO | 22 |
| Krankenhausaufenthalte | Art. 9 DSGVO | 15 |
| Rentenversicherungskorrespondenz | Sozialdaten | 8 |
| Personenstammdaten (Name, Adresse, SV-Nr.) | Art. 6 DSGVO | 38 |

### 2.3 Rechtsgrundlage der Verarbeitung

- Art. 9 Abs. 2 lit. b) DSGVO (Verarbeitung im Rahmen arbeitsrechtlicher Pflichten)
- § 26 Abs. 3 BDSG (Verarbeitung besonderer Kategorien im Beschäftigtenverhältnis)
- § 167 Abs. 2 SGB IX (gesetzliche Grundlage BEM-Verfahren)

### 2.4 Speicherung und Zugriff

BEM-Daten wurden in SAP HR (Modul: Personalwesen — Krankheit/BEM) sowie als digitale Scans in einem Dokumentenmanagementsystem (DMS) gespeichert. Zugriff hatten vor der Panne:
- HR-Abteilung (3 Personen)
- Betriebsärztlicher Dienst (extern, via VPN)
- Betriebsrat (eingeschränkt, nur im BEM-Sitzungsrahmen)
- IT-Administrator (technischer Zugriff, nicht inhaltlich)

---

## 3. Risikoanalyse

### 3.1 Identifizierte Risiken vor dem Vorfall

| Risiko | Eintrittswahrscheinlichkeit (vor Vorfall) | Schwere |
|---|---|---|
| Unbefugter Zugang durch Datenpanne | Mittel | Sehr hoch |
| Unsachgemäße Nutzung durch Mitarbeiter | Niedrig | Hoch |
| Weitergabe an Dritte | Niedrig | Sehr hoch |
| Datenverlust durch technischen Fehler | Niedrig | Mittel |

### 3.2 Risikobewertung nach Vorfall

Durch den Ransomware-Angriff und den Datenabfluss sind folgende Szenarien jetzt konkret eingetreten:

**Szenario 1 — Veröffentlichung durch Erpressergruppe:**  
AkiraNext droht mit Veröffentlichung der Daten auf ihrer Leakseite. Sollte dies geschehen, sind die Gesundheitsdaten von 38 Mitarbeitern öffentlich zugänglich. Folgen:
- Soziale Stigmatisierung (psychische Erkrankungen, Suchterkrankungen)
- Auswirkungen auf Kreditwürdigkeit, Versicherbarkeit
- Diskriminierung bei künftigen Bewerbungen
- Psychische Belastung durch Kontrollverlust über intimste Daten

**Risikoklassifikation:** HOCH — unmittelbare, schwerwiegende Folgen für vulnerable Personen.

**Szenario 2 — Missbrauch durch Dritte:**  
Die Daten könnten an spezialisierte Datenhändler oder Identitätsdiebe verkauft werden.

**Szenario 3 — Erpressung der betroffenen Mitarbeiter:**  
Einzelne Mitarbeiter könnten selbst erpresst werden (z.B. „Wir veröffentlichen Ihre Diagnose, wenn Sie nicht zahlen"). Dies stellt eine zusätzliche Belastung für besonders vulnerable Personen dar.

---

## 4. Bereits bestehende technisch-organisatorische Maßnahmen (TOMs) — Bewertung

| Maßnahme | Status vor Vorfall | Bewertung |
|---|---|---|
| Zugriffskontrolle (Rollenkonzept) | Implementiert | Ausreichend |
| Verschlüsselung der Daten at rest | Nicht vollständig | Unzureichend |
| Netzwerksegmentierung | Unzureichend | Unzureichend |
| Patch-Management | Defizitär (CVE-2026-0712) | Unzureichend |
| MFA für HR-Zugang | Nicht implementiert | Unzureichend |
| Backup und Wiederherstellbarkeit | Vorhanden (3-Tage-Rückstand) | Teilweise ausreichend |
| Protokollierung / SIEM | Über InsoTec (extern) | Teilweise ausreichend |
| Sensibilisierungsschulungen | Jährlich | Ausreichend |
| Auftragsverarbeitungsvertrag (AVV) | Vorhanden (InsoTec, ProcessSpark) | Vorhanden |

**Gesamtbewertung TOMs:** Die TOMs waren vor dem Vorfall für eine Datenverarbeitung der Kategorie „Art. 9 DSGVO — Gesundheitsdaten im Beschäftigtenkontext" **nicht ausreichend**. Insbesondere die fehlende Verschlüsselung at rest und das unzureichende Patch-Management stellen erhebliche Mängel dar.

---

## 5. Geplante Abhilfemaßnahmen

| Maßnahme | Verantwortlich | Frist |
|---|---|---|
| Einführung Ende-zu-Ende-Verschlüsselung für HR-Daten (at rest) | IT / InsoTec | 30.06.2026 |
| MFA für alle HR-Systemzugänge | IT / InsoTec | 15.06.2026 |
| Zero-Trust-Netzwerkarchitektur für HR-Segment | IT / InsoTec | 31.08.2026 |
| Neues Patch-Management-Konzept (SLA-gesichert) | ProcessSpark / intern | 30.06.2026 |
| DSGVO-Schulung HR-Mitarbeiter | DSB Feilke | 30.06.2026 |
| Überarbeitung AVV ProcessSpark und InsoTec | RA Drosten | 31.05.2026 |
| Einführung Data Loss Prevention (DLP) | IT | 31.07.2026 |
| Datenschutzaudit BEM-Prozesse | DSB Feilke | 31.07.2026 |
| Konsultation Betriebsrat zu TOMs | GF Wallbruck | 20.05.2026 |

---

## 6. Konsultation der Aufsichtsbehörde (Art. 36 DSGVO)

Aufgrund des hohen Restrisikos (Gesundheitsdaten, Exfiltration bereits erfolgt, Veröffentlichungsdrohung) wird eine vorherige Konsultation des LfDI RLP gemäß Art. 36 DSGVO durchgeführt. Die DSFA wird dem LfDI als Ergänzung zur Meldung vom 08.05.2026 übermittelt.

---

## 7. Ergebnis der DSFA

Die Datenschutz-Folgenabschätzung ergibt, dass die Verarbeitung von BEM-Gesundheitsdaten ohne die beschriebenen Abhilfemaßnahmen ein **hohes Restrisiko** für die Rechte und Freiheiten der betroffenen Mitarbeiter darstellt. Die geplanten Abhilfemaßnahmen sollen das Risiko auf ein akzeptables Niveau senken.

Die DSFA wird nach Abschluss der Abhilfemaßnahmen (voraussichtlich Herbst 2026) einer **Überprüfung** unterzogen.

**Verantwortliche Unterzeichner:**

Theresia Wallbruck (Geschäftsführerin, Verantwortlicher i.S.d. DSGVO)  
Markus Feilke (Datenschutzbeauftragter)  
RA Lukas Drosten (rechtliche Beratung)

*Mainz, 14.05.2026*
