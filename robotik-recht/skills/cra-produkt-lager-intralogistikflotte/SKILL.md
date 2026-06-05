---
name: cra-produkt-lager-intralogistikflotte
description: "CRA Produkt Lager Intralogistikflotte: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# CRA Produkt Lager Intralogistikflotte

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **CRA Produkt Lager Intralogistikflotte** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cra-produkt-mit-digitalen-elementen` | Prüft Cyber Resilience Act für Roboter, Steuerungssoftware, Apps, Cloud-Komponenten und Updatekanäle. |
| `lager-und-intralogistikflotte` | Prüft Roboterflotten in Lager und Intralogistik: Flottensteuerung, Zonen, Mitarbeiterschutz, Telemetrie, Wartung und Incident Logs. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **CRA Produkt Lager Intralogistikflotte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cra-produkt-mit-digitalen-elementen`

**Fokus:** Prüft Cyber Resilience Act für Roboter, Steuerungssoftware, Apps, Cloud-Komponenten und Updatekanäle.


# CRA für Roboter mit digitalen Elementen

## Fachkern: CRA für Roboter mit digitalen Elementen
- **Spezialgegenstand:** CRA für Roboter mit digitalen Elementen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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

## Querverweise

- `accuracy-robustness-cybersecurity-ai`
- `agile-entwicklung-und-compliance-gates`
- `ce-zeichen-fehlgebrauch-und-abmahnung`

## Quellen Stand 06/2026

- VO (EU) 2024/2847 (CRA), Art. 13, 14, 24, 64, 71; Anhang I, III, VIII.
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2024/1689 (KI-VO).
- RL (EU) 2022/2555 (NIS-2); BSIG.
- VO (EU) 2014/53 (RED) i. V. m. delegierter VO (EU) 2022/30.
- ISO/IEC 29147 (CVD); ISO/IEC 30111.
- Live-Verifikation auf eur-lex.europa.eu, enisa.europa.eu, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 2. `lager-und-intralogistikflotte`

**Fokus:** Prüft Roboterflotten in Lager und Intralogistik: Flottensteuerung, Zonen, Mitarbeiterschutz, Telemetrie, Wartung und Incident Logs.


# Lager- und Intralogistikflotte

## Fachkern: Lager- und Intralogistikflotte
- **Spezialgegenstand:** Lager- und Intralogistikflotte wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


Fachmodul im Plugin `robotik-recht`. Nutze ihn, wenn der Fall Robotik, autonome oder teilautonome Maschinen, integrierte KI, Sensorik, Remote-Updates, Mensch-Roboter-Interaktion, Produktsicherheit, Haftung, Datenschutz, Cybersecurity oder Robotikverträge berührt.

## Start

Kläre knapp:

1. **Rolle:** Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber, Deployer, Wartung, Versicherer, Behörde oder Geschädigte Person.
2. **Produkt:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, Medizin-, Haushalts-, Agrar-, Sicherheits-, Liefer- oder Sonderrobotik.
3. **Ziel:** Freigabe, CE-Akte, Behördenantwort, Vertragsprüfung, Incident, Rückruf, Haftungsmemo, Datenschutzprüfung, Cyberprüfung, Klage/Verteidigung oder Vorstandsvorlage.
4. **Dringlichkeit:** Unfall, Verletzung, Datenpanne, Cyberangriff, Marktüberwachung, Rückruf, Kundenstillstand, Frist oder nur Prävention.
5. **Unterlagen:** Anleitung, Risikobeurteilung, EU-Konformitätserklärung, technische Dokumentation, Logs, Softwarestände, Verträge, DSFA, SBOM, Wartungsprotokolle, E-Mails.

## Prüfspur

- Baue zuerst eine **Rollenmatrix**. Robotikfälle kippen oft daran, wer rechtlich Hersteller, Anbieter, Betreiber oder bloßer Zulieferer ist.
- Prüfe dann **parallel**: Maschinenrecht/Produktsicherheit, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, sektorspezifisches Recht und Vertrag.
- Trenne sichere Tatsachen, technische Annahmen und Rechtsbewertung. Markiere jede nicht belegte technische Annahme sichtbar.
- Arbeite mit einer **Ampel**: Rot = sofort handeln; Gelb = Unterlagen/Rückfragen; Grün = derzeit tragfähig, aber live zu verifizieren.
- Bei Rechtsprechung und aktuellen Normen: keine Paywall-Fundstellen, keine erfundenen Aktenzeichen; live über amtliche/freie Quellen prüfen.

## Spezifischer Fokus

Dieser Skill fokussiert: **Prüft Roboterflotten in Lager und Intralogistik: Flottensteuerung, Zonen, Mitarbeiterschutz, Telemetrie, Wartung und Incident Logs.**

Quellen-/Normenanker: Maschinenverordnung; Arbeitsschutz; Datenschutz; CRA.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.
