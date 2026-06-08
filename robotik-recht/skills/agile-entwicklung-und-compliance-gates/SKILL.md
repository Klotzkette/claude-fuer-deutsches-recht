---
name: agile-entwicklung-und-compliance-gates
description: "Entwirft Compliance-Gates für agile Robotikentwicklung: Definition of Done, Release-Board, Sicherheitsfreigabe und Rechtsfreigabe."
---

# Agile Entwicklung und Compliance-Gates in der Robotik

## Fachkern: Agile Entwicklung und Compliance-Gates in der Robotik
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Robotikhersteller arbeiten agil (Scrum, SAFe, Kanban) – das EU-Produkt-, KI- und Cyber-Recht denkt aber in Konformitätsbewertungsverfahren, Versionsständen und Konformitätserklärungen. Dieser Skill bringt beide Welten zusammen: Er definiert die Stage-Gates, die ein Robotikprodukt zwingend durchlaufen muss, damit Sprints am Ende ein CE-fähiges, KI-VO-konformes und cyber-resilientes Release liefern. Schwerpunkt: Definition of Done (DoD) auf Story-, Increment- und Release-Ebene; Sicherheits-, Datenschutz-, KI- und Rechtsfreigabe; Behandlung "substanzieller Änderungen" i. S. d. Art. 3 Nr. 23 VO (EU) 2024/1689 (KI-VO).

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Anbieter/Hersteller, Sicherheitsverantwortlicher (Safety Officer), DSB, CISO, Notified-Body-Auditor.
2. **Methodik:** Scrum, SAFe, Hybrid, V-Modell mit agilen Inseln?
3. **Releasemodell:** Big-Bang-Release, kontinuierliche OTA-Updates, Trains.
4. **Produktklasse:** Hochrisiko-KI nach Anhang III KI-VO, MaschinenVO-Produkt, Medizinprodukt, autonomes Fahrzeug.
5. **Anlass:** Aufbau Compliance-Pipeline, Audit-Vorbereitung, Vorfall nach unkontrolliertem Release, Beratung zu DoD/DoR.

## Rechtlicher Rahmen

- **MaschinenVO** VO (EU) 2023/1230 – Konformitätsbewertung Art. 25 ff., Geltung ab 20.01.2027; Risikobeurteilung pro Konfiguration.
- **KI-VO** VO (EU) 2024/1689 – Art. 9 Risikomanagement (kontinuierlich), Art. 17 Qualitätsmanagement, Art. 43 ff. Konformitätsbewertung, Art. 72 Post-Market-Monitoring.
- **CRA** VO (EU) 2024/2847 – Secure-by-Design, Schwachstellenmanagement; Schwachstellen-Meldepflichten ab 11.09.2026, Hauptpflichten ab 11.12.2027.
- **ProdSG / ProdHaftG / VO (EU) 2024/2853** – Hersteller-Verkehrssicherungspflichten auch nach Inverkehrbringen.
- **DSGVO** Art. 25 (Privacy by Design), Art. 35 DSFA.
- **ISO/IEC** ISO 12100 (Risikobeurteilung), ISO 13849-1, IEC 61508/62061, ISO 10218 / ISO/TS 15066 für Cobots, ISO/IEC 27001, ISO/IEC 42001 (AI-MS).

## Schritt für Schritt

1. **DoR (Definition of Ready) erweitern.** Jede Story mit Sicherheits-, KI- und Datenschutzrelevanz erhält Pflichtfelder: Risikoeinordnung, betroffene Schutzziele, erforderliche Tests, betroffene technische Dokumentation.
2. **DoD je Story.** Code-Review, statische Analyse, Unit-Tests, ggf. Hardware-in-the-Loop-Tests; Risiko-Snippet in der Story aktualisiert.
3. **DoD je Increment / PI (Program Increment).** Risikobeurteilung aktualisiert, SBOM aktuell, technische Dokumentation Anhang IV KI-VO gepflegt, Trainings-/Validierungsbericht aktualisiert.
4. **Gate 1: Safety-Freigabe.** Sicherheitsfunktion freigegeben durch Safety Officer; Performance-Level (PL) und SIL gehalten; Cobot-Validierung nach ISO/TS 15066 reproduziert.
5. **Gate 2: KI-Freigabe.** Art. 10 KI-VO Datenqualität nachgewiesen; Art. 15 KI-VO Tests bestanden; Art. 13/14 Transparenz und Human Oversight realisiert.
6. **Gate 3: Cyber-Freigabe.** SBOM, CVE-Scan, Pen-Test, Signaturkette OTA – CRA-Pflichten erfüllt.
7. **Gate 4: Datenschutz-Freigabe.** DSB-Votum, ggf. DSFA, Auftragsverarbeitungsvertrag mit Cloud-Anbieter.
8. **Gate 5: Rechts- und CE-Freigabe.** EU-Konformitätserklärung (alle einschlägigen Rechtsakte), Notified Body sofern erforderlich, Marktüberwachungs-Schnittstelle dokumentiert.
9. **Post-Release:** Field-Data-Loop, Vigilanz-Meldungen (Art. 73 KI-VO innerhalb 15 Tagen für schwerwiegende Vorfälle), Bewertung "substanzielle Änderung".

## Trade-off-Matrix

| Spannungsfeld | Agil-pur | Compliance-pur | Empfehlung |
|---|---|---|---|
| Release-Frequenz | täglich | quartalsweise | Kategorisierung: Cosmetic, Functional, Safety/AI – nur letzte zwei mit Re-Konformitätsbewertung |
| Refactoring der KI | jederzeit | nur mit Re-Audit | "Frozen Model" pro Release, Refactoring in eigenem Stream |
| Tech-Debt-Backlog | techn. Anliegen | Risikoeinträge im Risikomanagement | Doppel-Tagging Story + Risiko |
| Dokumentation | "Code is doc" | umfangreiche TecDoc | Doc-as-Code mit automatisierter Anhang-IV-Generierung |

## Praxistipps

- **Quality-Gate als CI-Job** mit Pflichtartefakten: Risiko-Diff, SBOM-Diff, Modell-Diff, Trainingsdaten-Diff, Testbericht; ohne grünen Gate kein Merge.
- **Trunk-based mit Release-Branches**: Safety-Reviews auf Release-Branch konzentrieren.
- **"Frozen Snapshot"** der gesamten technischen Akte zum Zeitpunkt des Inverkehrbringens; Dauer 10 Jahre (Art. 18 KI-VO).
- **Audit-Trail**: Wer hat welches Gate wann passieren lassen? Signatur des Verantwortlichen.
- **Substantial Modification**: Schwellwert vorab definieren (z. B. Modell-Architekturwechsel, neuer Sensor, Erweiterung des Einsatzbereichs).

## Mustertexte

**Auszug DoD-Checkliste (Safety-Story):**

> Definition of Done:
> 1. Code reviewed gemäß SCR-12; statische Analyse ohne Critical Findings (MISRA-C / Cert-C).
> 2. Unit-Test- und HiL-Coverage mindestens 90 % je Sicherheitsfunktion.
> 3. Risiko-ID in `RISK.yml` aktualisiert; Restrisiko bewertet; PL nach ISO 13849-1 reproduziert.
> 4. Anhang-IV-KI-VO-Doku autogeneriert und gegengelesen.
> 5. Safety Officer signiert in CI-Tool; ohne Signatur kein Tag `release/*`.

**Vertragsklausel mit Integrator:**

> Der Lieferant verpflichtet sich, jede substantielle Änderung der KI-Funktionen i. S. d. Art. 3 Nr. 23 KI-VO mindestens 30 Tage vor Auslieferung schriftlich anzuzeigen und die Konformitätsbewertung nach Art. 43 KI-VO vor Auslieferung erneut durchzuführen. Andernfalls steht dem Integrator ein Sonderkündigungsrecht zu.

## Typische Fehler

- **Continuous Deployment ohne Versionsstand** in EU-Konformitätserklärung – formal nicht haltbar.
- **Risikobeurteilung als Einmal-Dokument** – widerspricht Art. 9 KI-VO und MaschinenVO.
- **Pen-Test "danach"** statt Shift-Left – Befunde landen im Backlog statt im Release.
- **Safety Officer ohne Vetorecht** – Gate ist dann nur Theater.
- **Kein Rollback-Plan** für KI-Modelle, dadurch operative Risiken bei Hotfix.

## Querverweise

- `accuracy-robustness-cybersecurity-ai`
- `cra-produkt-mit-digitalen-elementen`
- `ce-zeichen-fehlgebrauch-und-abmahnung`
- `qm-system-iso-9001-und-iso-iec-42001` (sofern im Plugin)

## Pre-Release-Checkliste (Auszug)

- [ ] Risikobeurteilung aktualisiert und vom Safety Officer signiert
- [ ] Anhang-IV-Dokumentation der KI-VO aktualisiert und versioniert
- [ ] SBOM (CycloneDX) erstellt und in CI ausgegeben
- [ ] Pen-Test-Bericht ohne offene Critical/High Findings (oder Risikoakzeptanz dokumentiert)
- [ ] Training-/Validation-Bericht der KI-Komponenten je Klasse und Subgruppe
- [ ] Audit-Trail aller Gate-Freigaben (Wer, Wann, Was) lückenlos
- [ ] DSFA aktualisiert sofern erforderlich; DSB-Votum
- [ ] EU-Konformitätserklärung (alle Rechtsakte) finalisiert und unterzeichnet
- [ ] Notified Body bei pflichtigen Modulen eingebunden, Bescheinigung vorhanden
- [ ] Rollback-Plan dokumentiert, im CI-Job referenziert
- [ ] Field-Safety-Notice-Template vorbereitet für Worst-Case
- [ ] Marktüberwachungs-Kontaktdaten aktuell

## Eskalationspfad bei Gate-Fehlschlag

1. **Safety-Gate red**: Release sofort blockieren; Safety Officer prüft Sicherheitsregression; Hotfix in eigenem Branch.
2. **KI-Gate red**: erneutes Training/Re-Tuning; ggf. erneute Konformitätsbewertung bei substantial modification.
3. **Cyber-Gate red**: PSIRT informieren; Coordinated Vulnerability Disclosure einleiten; ggf. Vorfallmeldung CRA.
4. **Datenschutz-Gate red**: DSB konsultiert; ggf. DSFA überarbeiten; Aufsichtsbehörde nur bei Verdacht auf hohes Risiko.
5. **CE-Gate red**: Veröffentlichung an Marktüberwachung; bei bereits ausgelieferten Produkten Field Safety Notice/Rückruf.

## Quellen Stand 06/2026

- VO (EU) 2024/1689 (KI-VO), insb. Art. 9, 10, 15, 17, 18, 43, 72, 73, 113.
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2024/2847 (CRA).
- VO (EU) 2024/2853 (neue ProdHaftRL).
- DSGVO Art. 25, 32, 35.
- ISO 12100; ISO 13849-1; ISO 10218-1/-2; ISO/TS 15066; ISO/IEC 42001:2023.
- Live-Verifikation auf eur-lex.europa.eu und beim BSI; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
