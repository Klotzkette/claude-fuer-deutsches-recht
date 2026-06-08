---
name: cra-produkt-lager-intralogistikflotte
description: "Prüft Cyber Resilience Act für Roboter, Steuerungssoftware, Apps, Cloud-Komponenten und Updatekanäle im Robotik-Recht."
---

# CRA für Roboter mit digitalen Elementen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn 02.08.2026 für Hochrisiko (Art. 6 Anhang III), Verbote ab 02.02.2025, Maschinen-VO 20.01.2027, ProdHaftRL-Umsetzung 09.12.2026, KI-VO Art. 73 schwerwiegender Vorfall innerhalb 15 Tagen.
- Tragende Normen verifizieren: EU KI-VO (VO 2024/1689) Art. 6, 8-15, 16, 26, 50, 73, 99, Maschinenverordnung 2023/1230, Produkthaftungs-Richtlinie 2024/2853, BGB §§ 823, 831, ProdHaftG, EU NIS2-RL 2022/2555, EU CRA — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Hersteller, Importeur, Händler, Betreiber, Endnutzer, Marktüberwachungsbehörde (BMAS/BNetzA/BMDV), benannte Stelle (Notified Body), KI-Aufsicht (BNetzA-Stelle).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung, technische Dokumentation Anhang IV KI-VO, Risikomanagement-System Art. 9, Datengovernance-Konzept Art. 10, FAT/SAT-Protokoll, Betriebsanleitung, CE-Kennzeichnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: CRA für Roboter mit digitalen Elementen
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Der Cyber Resilience Act (CRA, VO (EU) 2024/2847) führt eine horizontale CE-Pflicht für "Produkte mit digitalen Elementen" ein. Roboter mit eingebetteter Software, Steuerungs-Apps, Cloud-Komponenten und OTA-Updates fallen darunter und müssen Secure-by-Design entwickelt, Schwachstellen koordiniert behoben und Vorfälle gemeldet werden. Die Vorschriften gelten gestaffelt: Schwachstellen- und Vorfallmeldepflichten ab 11.09.2026, die Hauptpflichten ab 11.12.2027 (Art. 71 CRA). Dieser Skill prüft Robotikprodukte gegen die CRA-Anforderungen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, Distributor, Notified Body (bei "wichtigen" Produkten Klasse I/II), CISO, Marktüberwachung.
2. **Robotertyp:** Industrie-/Cobot, AMR, Servicerobotik, IoT-Komponente; Funktion als "wichtige" Klasse?
3. **Software-Architektur:** Embedded, Companion-App, Cloud-Komponente, Drittsoftware, Open Source.
4. **Anlass:** Markteinführung, Vorfall, Schwachstelle, Audit, Kunden-Audit, Vertragsverhandlung.
5. **Unterlagen:** SBOM (CycloneDX/SPDX), Penetrationstest, Schwachstellen-Policy, OTA-Architektur, Incident-Response-Plan.

## Rechtlicher Rahmen

- **CRA** VO (EU) 2024/2847; Anhang I Cybersecurity Requirements (Teil I) und Vulnerability Handling (Teil II); Anhang III Wichtige/kritische Produkte.
- **Geltungsstaffelung Art. 71 CRA:** Vorfall- und Schwachstellenmeldungen ab 11.09.2026; Hauptpflichten 11.12.2027.
- **Schnittstellen:** MaschinenVO VO (EU) 2023/1230; KI-VO VO (EU) 2024/1689; NIS-2-RL (EU) 2022/2555 und BSIG; ProdHaftG/VO (EU) 2024/2853; RED-VO (EU) 2014/53 i. V. m. delegierter VO (EU) 2022/30 (RED-Cybersecurity).
- **Vorfallmeldungen** an ENISA und CSIRT Art. 14 CRA: Frühwarnung 24 h, Zwischenbericht 72 h, Abschlussbericht 1 Monat.
- **Geldbußen** Art. 64 CRA: bis 15 Mio. EUR oder 2,5 % weltweiter Jahresumsatz für wichtigste Pflichtverstöße.

## Schritt für Schritt

1. **Produkt-Klassifikation.** Standardprodukt vs. "wichtige" Klasse I/II vs. "kritische" Klasse (Anhang III/IV CRA).
2. **Secure-by-Design.** Anhang I Teil I: Standard-Konfiguration ohne bekannte Schwachstellen, Schutz vor unautorisiertem Zugriff, Vertraulichkeit, Integrität, Verfügbarkeit; Update-Mechanismus; minimal-privilege.
3. **Vulnerability Handling.** Anhang I Teil II: Schwachstellen-Policy, Coordinated Vulnerability Disclosure (CVD), SBOM, Sicherheitsupdates während Support-Periode.
4. **SBOM.** Maschinenlesbar (CycloneDX/SPDX), per Update aktualisiert; Hash der Lieferung.
5. **Penetration Testing** und Threat Modeling vor Inverkehrbringen.
6. **Vorfall- und Schwachstellenmeldungen** an ENISA und CSIRT (Single Reporting Platform) ab 11.09.2026; Fristen 24 h / 72 h / 1 Monat.
7. **Konformitätsbewertung** Modul nach Anhang VIII CRA; bei kritischen Produkten Pflicht zur Notified Body.
8. **Support-Periode.** Mindestens 5 Jahre, sofern Lebenszyklus nicht kürzer (Art. 13 Abs. 8 CRA).
9. **Vertragsklauseln** mit Zulieferern: SBOM-Pflicht, Schwachstellen-SLA, Update-Bereitstellung.

## Trade-off-Matrix

| Architektur | Pro CRA | Contra | Empfehlung |
|---|---|---|---|
| Embedded ohne Update-Pfad | – | nicht CRA-konform | OTA mit Signaturkette |
| OTA-Update kontinuierlich | sicher | erneute Konformitätsbewertung bei wesentlicher Änderung | Update-Klassifikation Cosmetic/Functional/Security |
| Cloud-Komponente | flexibel | Abhängigkeit, DSGVO, NIS-2 | hybrid: kritische Steuerung Edge, Telemetrie Cloud |
| Open Source | Auditierbarkeit | Verantwortlichkeit unklar | OSS-Stewards Art. 24 CRA; eigene Verantwortung dokumentieren |

## Praxistipps

- **PSIRT** (Product Security Incident Response Team) etablieren.
- **CVE-Monitoring** automatisiert.
- **Bug Bounty** als Bestandteil der CVD.
- **Roll-back-Mechanismus** bei fehlerhaftem Update.
- **Signatur-Schlüssel** in HSM, getrennte Rolle für Signatur-Freigabe.

## Mustertexte

**Schwachstellen-Policy (Auszug):**

> Wir nehmen Schwachstellenmeldungen an psirt@[Firma].de entgegen. Acknowledgment binnen 48 Stunden; Status-Update alle 14 Tage. Schweregradkategorien CVSS v3.1; kritische Schwachstellen erhalten Patch binnen 30 Tagen, hoch innerhalb 90 Tagen. Wir veröffentlichen Security Advisories in CycloneDX VEX-Format. Wir verpflichten uns zur koordinierten Offenlegung gemäß ISO/IEC 29147 und Art. 13 Abs. 8 CRA.

**Vertragsklausel mit Zulieferer:**

> Der Lieferant stellt mit jeder Lieferung eine SBOM im CycloneDX-Format zur Verfügung. Der Lieferant verpflichtet sich, sicherheitsrelevante Schwachstellen seiner gelieferten Komponenten innerhalb von 24 Stunden nach Bekanntwerden gegenüber dem Auftraggeber zu melden und innerhalb von 72 Stunden eine Risikoeinschätzung zu liefern. Sicherheitsupdates werden im Rahmen der CRA-Support-Periode von 5 Jahren bereitgestellt.

**Frühwarnmeldung (Auszug an CSIRT/ENISA):**

> Frühwarnung Art. 14 Abs. 2 CRA: Datum [Datum], Hersteller [Firma], Produkt [Modell], betroffene Versionen [n]. Beobachtung: ungewöhnliche Authentifizierungsversuche an [Datum/Uhrzeit]. Vorläufige Risikoeinschätzung: hoch. Zwischenbericht folgt binnen 72 h. Ansprechpartner PSIRT: [Name, E-Mail, Telefon].

## Typische Fehler

- **SBOM unvollständig** – Drittlieferanten fehlen.
- **OTA ohne Signaturkette** – Manipulation des Update-Pfads.
- **Keine PSIRT-Adresse** öffentlich – CRA verlangt sie.
- **Support-Periode nicht definiert** im Datenblatt.
- **Meldepflicht-Fristen überschritten** – Bußgeldrisiko Art. 64 CRA.

## Quellen Stand 06/2026

- VO (EU) 2024/2847 (CRA), Art. 13, 14, 24, 64, 71; Anhang I, III, VIII.
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2024/1689 (KI-VO).
- RL (EU) 2022/2555 (NIS-2); BSIG.
- VO (EU) 2014/53 (RED) i. V. m. delegierter VO (EU) 2022/30.
- ISO/IEC 29147 (CVD); ISO/IEC 30111.
- Live-Verifikation auf eur-lex.europa.eu, enisa.europa.eu, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

