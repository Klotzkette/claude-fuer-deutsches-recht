---
name: robotik-qualitaetsmanagement-robotikhersteller-accuracy
description: "Qualitaetsmanagement Robotikhersteller Accuracy: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Qualitaetsmanagement Robotikhersteller Accuracy

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Qualitaetsmanagement Robotikhersteller Accuracy** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `qualitaetsmanagement-robotikhersteller` | Prüft QM-System eines Robotikherstellers: Design Control, CAPA, Change Control, Lieferantensteuerung und Post-Market-Daten. |
| `accuracy-robustness-cybersecurity-ai` | Prüft Genauigkeit, Robustheit und Cybersicherheit von KI-Funktionen im Roboter mit realistischen Einsatzgrenzen. |
| `agile-entwicklung-und-compliance-gates` | Entwirft Compliance-Gates für agile Robotikentwicklung: Definition of Done, Release-Board, Sicherheitsfreigabe und Rechtsfreigabe. |
| `anwaltliche-quellenhygiene-robotik` | Sichert Quellenhygiene: keine Paywall-Blindzitate, keine erfundenen Rechtsprechungsfundstellen, Normen live prüfen, Aktenzeichen nur verifiziert. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Qualitaetsmanagement Robotikhersteller Accuracy**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `qualitaetsmanagement-robotikhersteller`

**Fokus:** Prüft QM-System eines Robotikherstellers: Design Control, CAPA, Change Control, Lieferantensteuerung und Post-Market-Daten.


# QM Robotikhersteller

## Fachkern: QM Robotikhersteller
- **Spezialgegenstand:** QM Robotikhersteller wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
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

Dieser Skill fokussiert: **Prüft QM-System eines Robotikherstellers: Design Control, CAPA, Change Control, Lieferantensteuerung und Post-Market-Daten.**

Quellen-/Normenanker: Maschinenverordnung, KI-VO, MDR, CRA.

## Ergebnisformat

Liefere je nach Auftrag eines der folgenden Formate:

- **Kurzvermerk** mit Ergebnis, Begründung, Risikoampel und offenen Fragen.
- **Rückfragenliste** an Technik/QM/IT-Security/Datenschutz/Vertrieb.
- **Dokumentenmatrix** mit vorhandenen und fehlenden Nachweisen.
- **Behörden- oder Mandantenentwurf** mit vorsichtiger Sprache und Quellenhinweisen.
- **Red-Team-Check** mit Gegenargumenten, Worst Case und nächstem Schritt.

Schlage am Ende passende Anschluss-Skills aus `robotik-recht` vor. Wenn Datenschutz, KI-VO, IT-Recht, Medizinrecht, Arbeitsrecht oder Vertragsrecht überwiegt, nenne zusätzlich das passende Nachbarplugin.

## 2. `accuracy-robustness-cybersecurity-ai`

**Fokus:** Prüft Genauigkeit, Robustheit und Cybersicherheit von KI-Funktionen im Roboter mit realistischen Einsatzgrenzen.


# Accuracy, Robustness, Cybersecurity bei KI im Roboter

## Fachkern: Accuracy, Robustness, Cybersecurity bei KI im Roboter
- **Spezialgegenstand:** Accuracy, Robustness, Cybersecurity bei KI im Roboter wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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

## 3. `agile-entwicklung-und-compliance-gates`

**Fokus:** Entwirft Compliance-Gates für agile Robotikentwicklung: Definition of Done, Release-Board, Sicherheitsfreigabe und Rechtsfreigabe.


# Agile Entwicklung und Compliance-Gates in der Robotik

## Fachkern: Agile Entwicklung und Compliance-Gates in der Robotik
- **Spezialgegenstand:** Agile Entwicklung und Compliance-Gates in der Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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

## 4. `anwaltliche-quellenhygiene-robotik`

**Fokus:** Sichert Quellenhygiene: keine Paywall-Blindzitate, keine erfundenen Rechtsprechungsfundstellen, Normen live prüfen, Aktenzeichen nur verifiziert.


# Anwaltliche Quellenhygiene Robotik

## Fachkern: Anwaltliche Quellenhygiene Robotik
- **Spezialgegenstand:** Anwaltliche Quellenhygiene Robotik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Robotik-Mandate verbinden technische und juristische Quellen. Falsche Aktenzeichen, veraltete Normenstände oder erfundene Kommentar-Fundstellen zerstören die Glaubwürdigkeit eines Memos und können berufsrechtlich relevant werden (§ 43a Abs. 3 BRAO). Dieser Skill etabliert einen prüfbaren Quellenprozess: Auswahl, Verifikation, Zitierung, Versionierung – sowohl für EU-Rechtsakte (KI-VO, MaschinenVO, CRA, neue ProdHaftRL) als auch für technische Normen (ISO, IEC, DIN, harmonisierte Normen).

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Mandatstyp:** Memo, Schriftsatz, Bescheid, Behördenkommunikation, Vorstandsvorlage, Gutachten für Notified Body.
2. **Quellenarten benötigt:** EU-Rechtsakt, BGH-/EuGH-Rspr., harmonisierte Norm, technische Spezifikation, Kommentar, Aufsatz, behördliche Leitlinie.
3. **Datenbankzugang vorhanden?** beck-online, juris, otto-schmidt, IEEE Xplore, BeckRS, ECLI-Portal.
4. **Aktualitätsanspruch:** Stichtag (z. B. Zeitpunkt des Inverkehrbringens), Verfahrenstand, Rechtsmittelfrist.
5. **Adressat:** Mandant, Behörde, Gericht, Gegenseite, Auditor – jeweils unterschiedliche Sorgfaltsanforderungen.

## Rechtlicher Rahmen

- **§ 43a Abs. 3 BRAO** Sachlichkeitsgebot, kein unwahrer Vortrag.
- **§ 138 ZPO** Wahrheitspflicht.
- **§§ 263, 269 StGB** als äußerste Grenze.
- Berufshaftung § 280 BGB i. V. m. Anwaltsvertrag.
- Im Schriftsatz: keine "ständige Rspr."-Floskeln ohne mindestens 2 belegte Entscheidungen.

## Schritt für Schritt

1. **EU-Rechtsakte stets über eur-lex.europa.eu** verifizieren. Stand der konsolidierten Fassung dokumentieren (CELEX-Nummer + Datum der Konsolidierung).
2. **Geltungsstaffelung KI-VO** unbedingt prüfen: Verbote Art. 5 ab 02.02.2025; GPAI-Pflichten ab 02.08.2025; Hochrisiko Art. 6 ff. ab 02.08.2026; volle Anwendung 02.08.2027 (Art. 113 KI-VO).
3. **MaschinenVO** Geltung ab 20.01.2027 – die Maschinen-RL 2006/42/EG bleibt bis dahin maßgeblich. Übergangsregelungen Art. 50 ff. MaschinenVO prüfen.
4. **CRA-Staffelung:** Schwachstellen-Meldepflichten ab 11.09.2026, Hauptpflichten ab 11.12.2027 (Art. 71 CRA).
5. **Produkthaftungs-RL neu** VO (EU) 2024/2853: Inkrafttreten 09.12.2026; nationale Umsetzungsfrist 09.12.2026 (Art. 22).
6. **Rspr.** Live-Verifikation: ECLI, BGH-Datenbank, Bundespatentgericht, OLG-Portale, openJur, dejure.org; keine Modellwissens-Zitate.
7. **Harmonisierte Normen** über OJ-Eintrag prüfen (Amtsblatt-Veröffentlichung). Norm-Version (Jahr) und Berichtigung beachten. ISO/IEC-Normen sind nur dann Vermutungswirkung-trächtig, wenn im OJ veröffentlicht.
8. **Kommentar/Aufsatz** nur zitieren, wenn Volltext geprüft. Bei lizenzierten Datenbanken: Zugang dokumentieren (Sitzung, Datum).
9. **Audit-Trail:** Speichern Sie den Volltext (PDF mit Datum) zur Mandatsakte – Beck-Online-Links altern.

## Trade-off-Matrix

| Quelle | Pro | Contra | Empfehlung |
|---|---|---|---|
| eur-lex konsolidiert | aktuell, amtlich | keine Materialien | für Auslegung mit Erwägungsgründen ergänzen |
| BeckRS / juris | breit | Paywall | nur bei Zugang nutzen; sonst openJur, dejure |
| Modellwissen | bequem | unzuverlässig | nie als Primärquelle |
| ChatGPT/LLM-Zitate | schnell | halluzinationsanfällig | nur als Hypothesen, jede Fundstelle verifizieren |

## Praxistipps

- **Quellen vor Argumenten.** Erst die Quelle prüfen, dann argumentieren. Nicht umgekehrt.
- **"Stand"-Vermerk** in jedem Memo: "Stand 02.06.2026, Live-Verifikation am [Datum]".
- **Aktenzeichen-Konvention:** Gericht – Senat – Aktenzeichen – Datum – ECLI; nicht abkürzen.
- **Norm-Versionen:** ISO 10218-1:2025; ISO/TS 15066:2016; jeweils Jahresangabe.
- **Übersetzungen:** englische und deutsche Fassung der EU-Rechtsakte abgleichen, insb. bei "provider/Anbieter", "deployer/Betreiber".

## Mustertexte

**Footer-Quellenhinweis:**

> Sämtliche EU-Rechtsakte zitiert in der am [Datum] über eur-lex.europa.eu abrufbaren konsolidierten Fassung. Aktenzeichen verifiziert am [Datum] in der frei zugänglichen Rechtsprechungsdatenbank des [Gericht] / ECLI-Portal. Harmonisierte Normen entsprechen dem Stand der Veröffentlichung im Amtsblatt vom [Datum].

**Beispielzitat richtig:**

> EuGH, Urteil vom 7. Dezember 2023, Rs. C-634/21 – SCHUFA Holding, ECLI:EU:C:2023:957, Rn. 73.

**Beispielzitat falsch (zu vermeiden):**

> "ständige Rechtsprechung des EuGH" ohne Belegstellen.

## Typische Fehler

- **"Maschinenrichtlinie 2006/42/EG"** angewandt nach 20.01.2027 ohne Übergangsregel.
- **KI-VO als bereits voll geltend** behauptet vor 02.08.2026 für Hochrisiko-Pflichten.
- **Kommentar-Fundstellen aus Modellwissen** – berufsrechtlich riskant.
- **Verlinkung statt Zitat** ohne Volltext-Sicherung.
- **Norm ohne Jahresangabe** ("ISO 10218") – mehrdeutig.

## Querverweise

- `robotik-recht-allgemein`
- alle Fachmodule mit Quellenangabe
- `references/zitierweise.md` im Repository

## Checkliste pro Memo/Schriftsatz

- [ ] Jede juristische Aussage hat eine Belegstelle
- [ ] Jede Belegstelle ist live geprüft (Datum und Stand vermerkt)
- [ ] Aktenzeichen vollständig mit ECLI angegeben
- [ ] Norm-Versionen mit Jahresangabe (ISO/IEC/DIN/EN)
- [ ] EU-Rechtsakte in konsolidierter Fassung mit CELEX-Nummer
- [ ] Geltungsstaffelung von KI-VO/CRA/MaschinenVO/ProdHaftRL beachtet (richtiges Datum für Stichtag)
- [ ] Übersetzungsabgleich bei zentralen Begriffen ("provider"/"Anbieter", "deployer"/"Betreiber")
- [ ] Kommentar/Aufsatz nur bei vorhandenem lizenzierten Zugang zitiert
- [ ] PDF-Volltexte zur Mandatsakte gespeichert (Sicherung gegen Link-Verfall)
- [ ] Footer mit Quellenhinweis und Stand-Datum eingefügt

## Häufige Stolpersteine bei Datenbanken

| Datenbank | Häufiges Problem | Gegenmaßnahme |
|---|---|---|
| beck-online | Paywall, Pagination Drift | Volltext-PDF speichern, Randnummern statt Seitenzahlen |
| juris | Veraltete Fassungen | Fassungsdatum prüfen; konsolidierte Fassung über eur-lex bei EU-Recht |
| BeckRS | Inkonsistente ECLI-Pflege | ECLI vom Portal des ausstellenden Gerichts beziehen |
| openJur/dejure | Vollständigkeit unklar | Cross-Check mit Originalgericht |
| LLM-Ausgaben | Halluzinierte Zitate | Jede Fundstelle einzeln verifizieren |

## Erweiterte Mustertexte

**Behördenschriftsatz – Quellenfooter (Auszug):**

> Sämtliche Bezugnahmen auf das Unionsrecht erfolgen in der über das Amt für Veröffentlichungen der Europäischen Union (eur-lex.europa.eu) am 02.06.2026 abrufbaren konsolidierten Fassung. Soweit auf Rechtsprechung Bezug genommen wird, wurde die Belegstelle am 02.06.2026 in dem ECLI-Portal des entsprechenden Gerichts verifiziert; in keiner Stellungnahme wurden Fundstellen aus generativen Modellen ohne Live-Verifikation übernommen.

## Quellen Stand 06/2026

- Repository-Referenz: `references/zitierweise.md`.
- VO (EU) 2024/1689 (KI-VO), Art. 113 Geltungsstaffelung.
- VO (EU) 2023/1230 (MaschinenVO), Art. 50 ff.
- VO (EU) 2024/2847 (CRA), Art. 71.
- VO (EU) 2024/2853 (neue ProdHaftRL), Art. 22.
- § 43a Abs. 3 BRAO; § 138 ZPO.
- eur-lex.europa.eu; ECLI-Portal; openJur; dejure.org; bundesgerichtshof.de.
- Lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
