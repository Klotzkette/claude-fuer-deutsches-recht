---
name: accuracy-robustness-cybersecurity-ai
description: "Prüft Genauigkeit, Robustheit und Cybersicherheit von KI-Funktionen im Roboter mit realistischen Einsatzgrenzen."
---

# Accuracy, Robustness, Cybersecurity bei KI im Roboter

## Fachkern: Accuracy, Robustness, Cybersecurity bei KI im Roboter
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Hochrisiko-KI-Systeme in Robotern (Anhang III der KI-VO, z. B. Sicherheitskomponenten von Maschinen, Medizin-, Verkehrsrobotik) müssen ein "angemessenes Maß" an Genauigkeit, Robustheit und Cybersicherheit aufweisen, Art. 15 VO (EU) 2024/1689 (KI-VO). Dieser Skill operationalisiert diese drei Anforderungen für Roboter: vom Performance-Test (Accuracy) über Stresstests gegen Drift, Sensorrauschen und Adversarial Inputs (Robustness) bis zu Härtung gegen Manipulation der Trainingsdaten (Data Poisoning), des Modells (Model Evasion) oder der Inferenz (Prompt-Injection bei GenAI-Robotik). Schnittstellen zum Cyber Resilience Act (VO (EU) 2024/2847, CRA) und zur MaschinenVO VO (EU) 2023/1230 müssen mitgedacht werden.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Anbieter (provider) i. S. d. Art. 3 Nr. 3 KI-VO, Betreiber (deployer), Hersteller, Importeur, Integrator, Marktüberwachungsbehörde oder Geschädigter.
2. **Robotertyp:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, OP-, autonomer Liefer- oder Sicherheitsroboter.
3. **KI-Funktion:** Bildverarbeitung, Hinderniserkennung, Pfadplanung, Greifsteuerung, Spracherkennung, GenAI-Schnittstelle, Reinforcement-Learning-Komponente.
4. **Anlass:** CE-Freigabe, Audit der Benannten Stelle, Vorfall mit Fehlverhalten, Behördenanfrage, Vertragsverhandlung Performance-Garantien.
5. **Unterlagen:** Test- und Validierungsberichte, Datenblatt zum Modell (Model Card), Datensatzdokumentation (Data Sheet), Logs, Penetration-Test-Berichte, SBOM, CVE-Tracking.

## Rechtlicher Rahmen

- **Art. 15 KI-VO** Genauigkeit, Robustheit, Cybersicherheit; Geltung für Hochrisiko-KI ab 02.08.2026 (Art. 113 KI-VO).
- **Art. 9 KI-VO** Risikomanagementsystem; Art. 10 KI-VO Daten-Governance.
- **MaschinenVO** VO (EU) 2023/1230, Anhang III Nr. 1.1.6 Ergonomie und sichere Steuerung, Nr. 1.2 Steuerungssysteme; Geltung ab 20.01.2027.
- **CRA** VO (EU) 2024/2847 Hauptpflichten ab 11.12.2027, Schwachstellen-Meldepflichten ab 11.09.2026; Robotik regelmäßig "Produkt mit digitalen Elementen".
- **NIS-2** Umsetzung im BSIG, OT-Sicherheit bei Robotik in kritischen Sektoren.
- **§ 1 ProdHaftG / VO (EU) 2024/2853** neue Produkthaftungs-RL (Inkrafttreten 09.12.2026): Software und KI sind Produkte, Beweiserleichterungen.

## Schritt für Schritt

1. **Use-case-Schärfung.** Definieren Sie den Einsatzkontext exakt: Umgebung, Beleuchtung, Geschwindigkeitsbereich, Personenkreis, Lastfälle. Performance-Aussagen ohne Kontext sind irreführend.
2. **Metriken festlegen.** Accuracy nicht nur als Single-Number-Wert: Precision, Recall, F1 je Klasse; bei Wahrnehmungsfunktionen mAP, IoU; bei Steuerung Erfolgsquote und Time-to-Stop. Mindestschwellen schriftlich.
3. **Test-Set kuratieren.** Realistische, aus Trainingsverteilung disjunkte Daten; Edge-Cases (Regen, Gegenlicht, ungewöhnliche Posen) explizit abdecken; Daten-Governance nach Art. 10 KI-VO dokumentieren.
4. **Robustheits-Tests.** Verteilungs-Drift (Domain Shift), Sensorrauschen, Sensorausfall, adversariale Eingaben (FGSM, PGD), physikalische Patch-Attacken bei Bildmodellen.
5. **Cybersecurity-Test.** Threat-Model (STRIDE) speziell für KI-Pipeline: Trainingsdaten, Modell-Repository, OTA-Update-Pfad, Inferenz-API, Sensor-Spoofing. Pen-Test gegen Steuerungsschnittstelle.
6. **Logging und Nachvollziehbarkeit.** Art. 12 KI-VO Logs während des gesamten Lebenszyklus; Mindestaufbewahrung 6 Monate (Art. 19 KI-VO), bei Robotik regelmäßig länger wegen § 199 BGB.
7. **Human Oversight.** Art. 14 KI-VO; bei Robotern: Notaus, Override, Trennung Autonomie-Level (z. B. SAE-Level analog).
8. **Konformitätsbewertung.** Modul nach Anhang VI/VII KI-VO; bei Robotik im Maschinen-Bezug regelmäßig integrierte Konformitätsbewertung mit MaschinenVO (Art. 8 ff.).

## Trade-off-Matrix

| Dimension | Konservativ (sicher) | Aggressiv (Performance) | Konsequenz |
|---|---|---|---|
| Schwelle Hinderniserkennung | hohe Recall, viele Fehlalarme | hohe Precision, mehr Restrisiko | Stillstandskosten vs. Verletzungsrisiko |
| Update-Frequenz | seltene, validierte Releases | kontinuierliches Lernen | erneute Konformitätsbewertung bei "substantial modification" Art. 3 Nr. 23 KI-VO |
| Edge vs. Cloud | Edge, isoliert | Cloud, mehr Rechenleistung | Datenschutz, NIS-2, OT-Angriffsfläche |
| Closed-Loop-Lernen | aus | an | Drift, Reproduzierbarkeit, Forensik |

## Praxistipps

- **Reproduzierbarkeit:** Seed, Modell-Hash, Daten-Hash und Toolchain-Versionen dokumentieren. Ohne Reproduzierbarkeit lässt sich kein Versagensfall forensisch klären.
- **Sensorredundanz:** Bei sicherheitskritischen Funktionen mindestens zwei Sensormodalitäten (z. B. Kamera + LiDAR + Ultraschall) und Plausibilitätsprüfung.
- **Out-of-Distribution-Detector:** Eigene Komponente, die unsichere Eingaben erkennt und Sicherheitsmodus auslöst.
- **CVE-Pflegeprozess:** Tägliche SBOM-Auswertung, Patch-SLA dokumentieren; im CRA verlangt.
- **Sprach- und GenAI-Komponenten:** Prompt-Injection-Tests und allowlist für Kommandos, die zu physischer Bewegung führen.
- **Drift-Monitoring:** Eingangsverteilungs- und Performance-Telemetrie nach Inverkehrbringen (Art. 72 KI-VO Post-Market-Monitoring) automatisiert; Alerts bei Abweichung über vordefinierten Schwellen.
- **Versionsstand jederzeit ermittelbar.** Roboter zeigt aktuellen Modell- und Software-Versionsstand auf Anforderung an; ohne diese Transparenz kein forensischer Nachweis nach Vorfall.
- **Trennung Safety- und Convenience-Funktionen.** Sicherheitskritische Funktionen laufen auf eigenem, zertifizierten Controller; KI-Komfortfunktionen separat.
- **Schulung der Operatoren** auf Grenzen des Systems (Out-of-Distribution-Erkennung manuell, Override-Pfad).

## Mustertexte

**Klausel Performance-Garantie (Auszug Liefervertrag Cobot):**

> Der Lieferant garantiert für den Pick-and-Place-Anwendungsfall gemäß Anlage 3 eine durchschnittliche Erfolgsquote von mindestens 99,2 % (Toleranz +/- 0.3 %) je Schicht über eine Messdauer von 30 Tagen unter den dort beschriebenen Umgebungsbedingungen. Maßgeblich sind ausschließlich die in Anlage 4 definierten Testfälle. Bei Unterschreitung gilt § 437 BGB; eine Verkürzung der Verjährung wird nicht vereinbart.

**Auszug Risikobeurteilung KI-Funktion:**

> Risikoquelle: Personenerkennung im Cobot-Arbeitsbereich. Schadensszenario: Nicht-Erkennung eines knienden Mitarbeiters bei Gegenlicht. Wahrscheinlichkeit nach Maßnahmen: 1 in 10^6 Betriebsstunden. Maßnahmen: redundante Sensorik (RGB + Tiefenkamera), OOD-Detector, Stopp bei Konfidenz unter 0.85, jährliches Re-Validation-Audit. Restrisiko: vertretbar im Sinne Art. 9 Abs. 5 KI-VO. Konformitätsnachweis: Anhang VI KI-VO.

## Typische Fehler

- **Performance-Aussagen ohne Datensatzbeschreibung** ("99,9 %") – nicht prüfbar, haftungsträchtig.
- **Vergessene erneute Bewertung nach Update** Art. 43 Abs. 4 KI-VO substantial modification.
- **Keine Trennung Trainings-/Test-/Real-World-Daten**, dadurch verdeckter Data Leakage.
- **Fehlende OT-Härtung** der Inferenz-API (offene MQTT-, ROS-Schnittstellen).
- **Keine Aufbewahrung der Logs** über die Verjährungsfrist.
- **Allgemeine "Black-Box"-Aussagen** zur KI-Funktion gegenüber Notified Body – Art. 13 KI-VO Transparenz verlangt nachvollziehbare Beschreibung.
- **Keine Pen-Tests** der OTA-Update-Kette; Folge: Manipulation des Modells unbemerkt möglich.
- **Auslagerung an Cloud-Anbieter** ohne TIA bei Drittlandtransfer der Inferenz-Anfragen.

## Anwendungsbeispiele

- **Pick-and-Place Cobot.** Kollabiert bei Glas mit Reflexionen. Maßnahmen: Adversarial-Beispiele mit Reflexionen ins Test-Set; OOD-Detector; Geschwindigkeit drosseln bei niedriger Konfidenz.
- **AMR im Lager.** Verwechselt Schatten mit Hindernis. Maßnahmen: Kombiniere LiDAR und Tiefenkamera; Kalibrierung bei Tageslicht; Heuristik gegen ground-shadow.
- **Service-Roboter mit Sprachsteuerung.** Prompt-Injection beim GenAI-Layer. Maßnahmen: Allowlist physischer Aktionen, Two-Person-Confirmation für sicherheitsrelevante Bewegungen.

## Querverweise

- `cra-produkt-mit-digitalen-elementen`
- `datensatzqualitaet-und-bias-hri`
- `agile-entwicklung-und-compliance-gates`
- `betreiber-mitverschulden-und-fehlbedienung`
- `data-act-roboterdaten`

## Eskalationspfad bei Sicherheitsvorfall

1. **Sofort (T+0 bis T+1h)**: Stillstand, Sicherheitsraum sichern, Verletzte versorgen, Behörden bei Personenschaden.
2. **T+1h bis T+24h**: Logs sichern (Hash, Write-Lock), Versionsstände dokumentieren, Forensik startklar machen.
3. **T+24h bis T+72h**: Vigilanz-Meldung Art. 73 KI-VO bei schwerem Vorfall innerhalb 15 Tagen, Cyber-Vorfall Art. 14 CRA innerhalb 24h Frühwarnung / 72h Zwischenbericht.
4. **T+1 Woche**: Root Cause Analysis, Korrekturmaßnahmen, Information der betroffenen Betreiber (Field Safety Notice).
5. **T+1 Monat**: Abschlussbericht, ggf. Rückruf, ggf. Konformitätsbewertung wiederholen bei substantial modification.

## Checkliste vor Inverkehrbringen

- [ ] Use-Case-Spezifikation mit Umgebungs- und Personen-Kontext schriftlich fixiert
- [ ] Performance-Metriken je Klasse und Subgruppe (Art. 10 KI-VO) gemessen
- [ ] Test-Set disjunkt zum Trainings-Set, Hashes dokumentiert
- [ ] Adversariale Tests durchgeführt (mind. FGSM, PGD, physikalische Patches bei Bildmodellen)
- [ ] Threat-Model (STRIDE) für KI-Pipeline erstellt
- [ ] Pen-Test extern (mind. einmal pro Major-Release)
- [ ] OOD-Detector implementiert und getestet
- [ ] Human-Oversight-Pfad funktional (Art. 14 KI-VO)
- [ ] Logging Art. 12 KI-VO aktiv und resistent gegen Manipulation (write-once)
- [ ] SBOM und Schwachstellen-Policy verfügbar (CRA-Vorgriff)
- [ ] Konformitätsbewertung Modul Anhang VI/VII abgeschlossen
- [ ] EU-Konformitätserklärung unterzeichnet, technische Dokumentation Anhang IV erstellt

## Quellen Stand 06/2026

- VO (EU) 2024/1689 (KI-VO), insb. Art. 9, 10, 12, 13, 14, 15, 43, 113.
- VO (EU) 2023/1230 (MaschinenVO), Anhang III.
- VO (EU) 2024/2847 (CRA).
- VO (EU) 2024/2853 (neue ProdHaftRL).
- ENISA, AI Threat Landscape, fortlaufend; BSI, Leitlinien zu KI-Cloud-Diensten.
- Live-Verifikation in eur-lex.europa.eu und auf BSI-, BfDI-, EDPB-Seiten; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
