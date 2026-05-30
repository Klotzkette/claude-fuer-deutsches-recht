# Aktenstück 21 — Interne Mandantenpräsentation: KI-VO-Konformitätsbefunde MedAssist v4

**Aktenzeichen:** 2026-V-0427  
**Erstellt:** 12.05.2026  
**Format:** Präsentationsnotizen für Vorstandssitzung MedAssist AI GmbH, 14.05.2026  
**Adressaten:** CEO Dr. Theresia Vogelkamp, CTO Aravind Krishnamurthy, CMO Dr. Lutz Federkamp  
**Präsentierende:** RAin Dr. Henrietta Vellbruck-Steinheim, RA Dr. Mark Roosendaal  
**Vertraulich**

---

## Folie 1 — Ausgangslage

**Titel:** MedAssist v4: KI-VO-Konformitätsprüfung — Zwischenbilanz

- Prüfungszeitraum: 03.03.2026 – 12.05.2026
- Prüfumfang: Art. 6–49 KI-VO, MDR-Schnittstelle, GPAI-Komponente, behördliche Verfahren
- Frist: **02.08.2026** (Art. 113 Abs. 1 KI-VO) — 82 Tage verbleibend
- Behördliche Verfahren: BNetzA (1-101.05-2026/MA-008), BfDI (13-3120/004#0117), BfArM (MED-AI-2026-0319)

---

## Folie 2 — Auf einen Blick: Ampelstatus

| Bereich | Status | Sofortbedarf |
|---|---|---|
| Menschliche Aufsicht (Art. 14) | Rot — nicht konform | Ja (Roll-out läuft) |
| Risikomanagementsystem (Art. 9) | Rot — nicht konform | Ja |
| Daten-Governance (Art. 10) | Rot — nicht konform | Ja |
| Technische Dokumentation (Art. 11) | Rot — nicht konform | Ja |
| Konformitätsbewertung (Art. 43) | Rot — nicht begonnen | Ja |
| Registrierung EU-DB (Art. 49) | Rot — nicht erfolgt | Abhängig |
| Aufzeichnungspflichten (Art. 12) | Gelb — Lücken | Teilweise |
| Transparenz (Art. 13) | Gelb — Lücken | Teilweise |
| Cybersicherheit (Art. 15) | Gelb — ISO abgelaufen | Ja |
| MDR-Koordination | Gelb — Abstimmung nötig | Mittel |
| GPAI-Dokumentation | Gelb — Lücke | Mittel |

---

## Folie 3 — Das gravierendste Defizit: Art. 14 (Menschliche Aufsicht)

**Status:** In 14 von 18 Kliniken kein technisch erzwungener Quittierungsschritt.

**Was das bedeutet:**
- MedAssist v4 steuert de facto die Notrufdisposition ohne dokumentierte menschliche Prüfung
- False-Negative-Rate 8,8 % bei lebensbedrohlichen Notrufen (Dringlichkeit 1) wird nicht korrigiert
- Jede 11. lebensbedrohliche Lage wird unterklassifiziert → Dispositionsverzögerung
- Haftungsrisiko Anbieter: Produkthaftungsgesetz, § 823 BGB; Haftungsrisiko Vorstand: § 43 GmbHG

**Was bereits eingeleitet ist:**
- Roll-out Quittierungsschritt auf alle 18 Kliniken: **30.04.2026** ✓ (laut CTO: abgeschlossen)
- Protokollierung Disponenten-ID läuft an

**Nächster Schritt:** Schulungsprogramm Disponenten bis 31.05.2026.

---

## Folie 4 — Behördliche Verfahren: Aktueller Stand

### BNetzA (Az. 1-101.05-2026/MA-008)
- Vor-Ort-Besichtigung Klinikum Mannheim-Süd: 12.05.2026 (heute!)
- Ergebnis: BNetzA-Inspektor hat Quittierungsschritt (Beta) positiv vermerkt; weitere Unterlagen angefordert (Bias-Analyse, Schulungskonzept)
- Bewertung: Kooperationsstrategie zeigt Wirkung; kein Sofortbescheid

### BfDI (Az. 13-3120/004#0117)
- DPIA an BfDI übermittelt: 01.05.2026 (fristgerecht)
- BfDI hat 30-Tage-Prüffrist → Rückmeldung erwartet bis 01.06.2026
- Inhalt DPIA: Systematische Verarbeitung Gesundheitsdaten, Bias-Risiken, Art. 22 DSGVO-Analyse, Abhilfemaßnahmen

### BfArM (Az. MED-AI-2026-0319)
- MDR-Konformität bestätigt; KI-VO ausdrücklich ausgeklammert
- Koordination für gemeinsame Prüfung mit TÜV SÜD läuft

### Wettbewerberbeschwerde DiagnoFlow / DG CONNECT
- DG CONNECT hat Beschwerde an BNetzA weitergeleitet (Standardverfahren)
- Kein direktes DG-CONNECT-Verfahren zu erwarten
- BNetzA-Verfahren deckt Beschwerde ab

---

## Folie 5 — Kritischer Pfad bis 02.08.2026

**Muss bis Frist zwingend fertig sein:**

1. Vollständige technische Dokumentation → **01.06.2026**
2. QMS nach Art. 17 KI-VO → **01.06.2026**
3. TÜV SÜD beauftragen → **15.05.2026** (noch ausstehend!)
4. NB-Zertifikat TÜV SÜD → **Mitte Juli 2026**
5. EU-Konformitätserklärung → **20.07.2026**
6. CE-Kennzeichnung KI-VO → **25.07.2026**
7. EU-Datenbank-Registrierung (EUID) → **30.07.2026**

**Engpass:** TÜV SÜD muss sofort beauftragt werden. Jede Woche Verzögerung gefährdet die Frist.

---

## Folie 6 — Empfehlung an den Vorstand

1. **Sofort (diese Woche):** CTO Krishnamurthy beauftragt TÜV SÜD schriftlich mit KI-VO-Konformitätsbewertung.
2. **Bis 31.05.2026:** Disponenten-Schulung in allen 18 Kliniken abgeschlossen.
3. **Bis 01.06.2026:** Vollständige technische Dokumentation an TÜV SÜD.
4. **D&O-Versicherung:** CEO Dr. Vogelkamp nimmt Verhandlungen mit Allianz SE auf, gestützt auf Handlungsplan und Fortschrittsnachweis.
5. **CMO Dr. Federkamp:** Einbindung der Kliniken als Betreiber in den Konformitätsprozess — Betreiberverträge anpassen (Art. 25 KI-VO).

---

## Folie 7 — Risikoszenario: Was passiert bei Fristüberschreitung?

- Bußgeld BNetzA: Bis **15 Mio. EUR** (Art. 99 Abs. 3 KI-VO) für nicht-konforme Hochrisiko-KI
- Vorläufige Maßnahme BNetzA: **Betriebsuntersagung** MedAssist v4 in allen 18 Kliniken möglich (Art. 79 KI-VO)
- Persönliche Haftung Vorstand: § 43 GmbHG — ohne D&O-Schutz erhebliches persönliches Risiko
- Reputationsschaden: DiagnoFlow-Beschwerde + Medienberichterstattung (Ärzte Zeitung 22.02.2026 bereits berichtet)
- Vertragsrisiko Kliniken: 18 Betreiberverträge könnten bei BNetzA-Betriebsuntersagung unter Rücktrittsrecht stehen

---

*Heidelberg, 12.05.2026 — Vellbruck & Partner mbB — Az. 2026-V-0427*  
*Vertraulich — nur für die Empfänger bestimmt*
