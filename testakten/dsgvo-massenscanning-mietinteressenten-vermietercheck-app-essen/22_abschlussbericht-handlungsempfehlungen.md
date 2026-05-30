# 22 — Abschlussbericht und Handlungsempfehlungen

**Aktenzeichen:** alle VCS-Aktenzeichen
**Bearbeiter:** RA Dr. Cornelius Specht (federfuehrend)
**Datum:** 07. Februar 2026
**Betreff:** Gesamtabschluss Erstanalyse und Handlungsempfehlungen

---

## 1. Zusammenfassung der Ausgangslage

Die VermieterCheck Solutions GmbH (VCS) sieht sich einer beispiellosen datenschutzrechtlichen Krisensituation gegenueber, die in ihrer Kumulation juristisch als existenzbedrohend einzustufen ist:

| Verfahrens-/Risikokomplex | Finanzielles Risiko | Rechtsnatur |
|---------------------------|---------------------|-------------|
| Bussgeldbescheid LDI NRW Art. 83 DSGVO | bis 20.000.000 EUR | Verwaltungsrecht |
| VDuG-Sammelklage 8.200 Betroffene | 12.300.000 EUR | Zivilrecht |
| Strafverfahren GF § 42 BDSG | Freiheitsstrafe bis 3 Jahre | Strafrecht |
| Einzelklage Tannenbruck | 1.500 EUR zzgl. Kosten | Zivilrecht |
| Reputationsschaden (NDR, Buch) | Unquantifiziert | Geschaeftlich |
| **Gesamtexposure (theoretisch)** | **> 32.000.000 EUR** | |

Das tatsaechliche Exposure nach erfolgreicher Verteidigung wird auf 1.000.000 bis 5.000.000 EUR geschaetzt (s. Bussgeldbemessung Akte 09, Vergleichsstrategie VDuG Akte 11).

---

## 2. Rechtliche Bewertungen — Kernbefunde

### 2.1 Klare Rechtsverstoesse (nicht bestreitbar)

1. **Art. 6 DSGVO:** Verarbeitung ohne wirksame Rechtsgrundlage — Einwilligung durch Koppelung und Unvollstaendigkeit unwirksam (s. Akte 03)
2. **Art. 22 DSGVO:** Unzulaessige automatisierte Einzelentscheidung — HITL fehlt, Ausnahmen nicht erfullt (s. Akte 04)
3. **Art. 35 DSGVO:** DSFA nicht durchgefuehrt trotz offensichtlicher Pflicht (s. Akte 05)
4. **Art. 44 ff. DSGVO:** Drittlandtransfer an Sundara Tech ohne SCC (s. Akte 06)
5. **Art. 33 DSGVO:** 72h-Meldepflicht versaeumt (s. Akte 07)
6. **Art. 28 DSGVO:** AVV mit Sundara Tech fuer 14 Monate nicht vorhanden; bestehendes AVV mangelhaft (s. Akte 16)

### 2.2 Verteidigungspositionen (bestrittig)

1. **Bussgeldbemessung Art. 83:** Verhaeltnismaessigkeitspruefung — KMU-Abschlag, keine Absicht, Kooperation (s. Akte 09)
2. **Art. 82 Bagatellgrenze:** Kein tatsaechlicher Schaden fuer Segmente C und D (s. Akte 11)
3. **§ 42 BDSG Vorsatz:** Verbotsirrtum, fehlende Bereicherungsabsicht (s. Akte 15)
4. **Art. 83 GRCh / VfB:** Verhaeltnismaessigkeitspruefung auf EU-/Verfassungsebene (s. Akte 21)

---

## 3. Priorisierte Handlungsempfehlungen

### Sofortmassnahmen (bis 15.02.2026)

**Prioritaet KRITISCH:**

1. **Datenpanne-Meldung nacholen (Art. 33 DSGVO):** Sofortiger Eingang der Meldung bei LDI NRW mit vollstaendiger Schadensdarstellung. Jeder weitere Tag des Versaeumnisses verschlimmert die Bussgeldbemessung.
   - Verantwortlich: RA Dr. Specht
   - Frist: 10.02.2026

2. **Auskunft Dr. Tannenbruck erteilen:** Fristerstreckung bei LG Essen beantragen und Auskunft innerhalb von 7 Tagen erteilen.
   - Verantwortlich: RAin Beckenbauer + DSB Kessler-Brandt
   - Frist: 12.02.2026

3. **Datentransfer Sundara Tech stoppen:** Kein weiterer Datentransfer bis SCC unterzeichnet.
   - Verantwortlich: DevOps-Leiter Bilgic
   - Frist: Sofort (bereits angeordnet 14.01.2026)

4. **Patching CVE-2026-0188:** Produktiver Patch live und verifiziert durch SecureProof.
   - Verantwortlich: DevOps-Team
   - Frist: Bereits eingespielt (24.11.2025); Verifikation 10.02.2026

5. **Betroffenenbenachrichtigung Art. 34 DSGVO:** Brief und E-Mail an 142.300 betroffene Mietinteressenten mit Information ueber Datenpanne.
   - Verantwortlich: DSB Kessler-Brandt + externe Kommunikationsagentur
   - Frist: 15.02.2026

### Kurzfristige Massnahmen (bis 28.02.2026)

6. **DSFA fertigstellen (Art. 35 DSGVO):** Vollstaendige DSFA-Dokumentation fuer ProspectScore Pro, anschliessend Vorabkonsultation LDI NRW (Art. 36 DSGVO).

7. **Auskunftsersuchen Drostermann und Kaltenbach beantworten** (Art. 15 DSGVO, Fristen 03.02. und 05.02.2026).

8. **SCC mit Sundara Tech abschliessen:** Modul 2 Controller-to-Processor, inklusive TIA.

9. **Stellungnahme LDI NRW einreichen:** Vollstaendige kooperative Stellungnahme zu DSB-NW-44/26 mit Sanierungsnachweis.

### Mittelfristige Massnahmen (bis 31.03.2026)

10. **HITL-Implementierung:** Human-in-the-Loop fuer ProspectScore Pro, Testphase und Dokumentation.

11. **Betroffenenportal:** Online-Portal fuer Auskunft, Widerspruch, Loeschung, Datenportabilitaet.

12. **Klageerwiderung VDuG:** Schriftsatz LG Essen 18 Mass 4/26 mit vollstaendiger Verteidigungsstrategie und Vergleichsangebot.

13. **Schulungen:** Alle 38 Mitarbeiter DSGVO-Pflichtschulung, IT-Team Secure-Coding.

14. **Loeschkonzept implementieren:** Automatisiertes Loeschprotokoll fuer alle Datenkategorien.

---

## 4. Kostenprognose Rechtsvertretung

| Leistung | Geschaetzte Kosten (netto) |
|----------|--------------------------|
| Verwaltungsverfahren LDI NRW | 45.000 – 60.000 EUR |
| Zivilverfahren VDuG + Tannenbruck | 80.000 – 120.000 EUR |
| Strafverfahren (RA Dr. Ankermann) | 40.000 – 70.000 EUR |
| Beratung (DSFA, TOM, SCC) | 30.000 – 50.000 EUR |
| Externe Gutachter/Forensik | 25.000 – 40.000 EUR |
| **Gesamt Rechtsvertretungskosten** | **220.000 – 340.000 EUR** |

Der geleistete Kostenvorschuss von 85.000 EUR deckt die ersten 3-4 Monate ab. Eine Nachschussanforderung ist fuer April 2026 geplant.

---

## 5. Abschliessende Prognose

Bei konsequenter Umsetzung der Sofort- und Kurzfristmassnahmen und kooperativer Haltung gegenueber LDI NRW ist folgendes Szenario realistisch:

- **Bussgeld LDI NRW:** 300.000 – 800.000 EUR (statt 20 Mio. EUR Maximum)
- **VDuG-Vergleich:** 400.000 – 700.000 EUR (statt 12.3 Mio. EUR Klageforderung)
- **Strafverfahren GF:** Geldstrafe oder Bewaehrungsstrafe (kein Haftantritt)
- **Reputationsschaden:** Begrenzbar durch PR-Offensive und sichtbare Compliance-Massnahmen

**Gesamtaussicht:** Unternehmenserhalt bei konsequenter Compliance-Offensive wahrscheinlich. Die Kanzlei SBD ist zuversichtlich, die Mandantin durch die Krise zu fuehren.

---

## 6. Sorgfaltspflicht-Hinweis

Dieser Abschlussbericht stellt eine erste Gesamtbewertung des Sachverhalts dar, basierend auf den im Zeitraum 14.-31.01.2026 erhobenen Informationen. Er ersetzt keine spezifische Einzelberatung zu den einzelnen Verfahren (s. Akten 01–21). Die Einschaetzungen koennen sich aufgrund neuer Tatsachen oder veraendeter Rechtslage jederzeit aendern.

---

## Quellen

- DSGVO Art. 6, 22, 28, 33, 34, 35, 44, 82, 83 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- BDSG § 42 — [dejure.org/gesetze/BDSG](https://dejure.org/gesetze/BDSG)
- VDuG — [dejure.org/gesetze/VDuG](https://dejure.org/gesetze/VDuG)
- EuGH C-807/21 (Deutsche Wohnen) — [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0807)
- BGH VI ZR 10/24 — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- EDSA-Leitlinien 04/2022 (Bussgeldbemessung) — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-042022-calculation-administrative-fines-under-gdpr_de)
