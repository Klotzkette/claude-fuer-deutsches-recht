---
name: accuracy-robustness-cybersecurity-ai
description: "Für Accuracy, Robustness, Cybersecurity bei digitale Werkzeuge im Roboter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Accuracy, Robustness, Cybersecurity bei KI im Roboter

## Fachkern: Accuracy, Robustness, Cybersecurity bei KI im Roboter
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Genauigkeit, Robustheit und Cybersicherheit nach Artikel 15 der KI-Verordnung anhand des tatsächlich erfassten Systems prüfen. Artikel 6 Absatz 1 mit Anhang I einschließlich Abschnitt A/B und Artikel 2 Absatz 2 von Absatz 2 mit Anhang III trennen. Artikel 6 Absätze 1a bis 1c samt Berichtigung prüfen. Eine sicherheitsrelevante Maschinenfunktion ist nicht allein deshalb ein Anhang-III-Tatbestand. Artikel 111/113 nach Pflicht und Version anwenden; die Verschiebung auf 02.12.2027 beziehungsweise 02.08.2028 betrifft nur Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5. Technische Tests müssen zur Zweckbestimmung und möglichen Fehlfolge passen; ein allgemeiner Benchmark allein genügt nicht. Schnittstellen zum Produkt- und Cyberrecht separat dokumentieren. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Anbieter (provider) i. S. d. Art. 3 Nr. 3 KI-VO, Betreiber (deployer), Hersteller, Importeur, Integrator, Marktüberwachungsbehörde oder Geschädigter.
2. **Robotertyp:** Industrieroboter, Cobot, AMR/AGV, Service-, Pflege-, OP-, autonomer Liefer- oder Sicherheitsroboter.
3. **KI-Funktion:** Bildverarbeitung, Hinderniserkennung, Pfadplanung, Greifsteuerung, Spracherkennung, GenAI-Schnittstelle, Reinforcement-Learning-Komponente.
4. **Anlass:** CE-Freigabe, Audit der Benannten Stelle, Vorfall mit Fehlverhalten, Behördenanfrage, Vertragsverhandlung Performance-Garantien.
5. **Unterlagen:** Test- und Validierungsberichte, Datenblatt zum Modell (Model Card), Datensatzdokumentation (Data Sheet), Logs, Penetration-Test-Berichte, SBOM, CVE-Tracking.

## Rechtlicher Rahmen

- **Art. 15 KI-VO** Genauigkeit, Robustheit, Cybersicherheit; Geltung im jeweiligen Kapitel-III-Pfad nach Artikel 113: Anhang III ab 02.12.2027, Anhang I ab 02.08.2028. Maschinen nun Anhang I Abschnitt B, Artikel 2 Absatz 2 und Maschinenrecht zuerst prüfen.
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
6. **Logs:** Artikel 12 betrifft technische Aufzeichnung, Artikel 19 die kontrollierten Anbieterlogs und Artikel 26 Absatz 6 die Betreiberlogs. Grundsätzlich mindestens sechs Monate, soweit anderes einschlägiges Recht nichts anderes vorsieht. Ein Verjährungshinweis begründet allein keine pauschale längere Speicherung sämtlicher personenbezogener Daten. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
7. **Human Oversight.** Art. 14 KI-VO; bei Robotern: Notaus, Override, Trennung Autonomie-Level (z. B. SAE-Level analog).
8. **Konformitätsweg:** Artikel 6 Absatz 1 mit Anhang I einschließlich Abschnitt A/B und Artikel 2 Absatz 2 von Absatz 2 mit Anhang III trennen. Artikel 6 Absätze 1a bis 1c samt Berichtigung prüfen. Eine sicherheitsrelevante Maschinenfunktion ist nicht allein deshalb ein Anhang-III-Tatbestand. Artikel 43 Absatz 3 nicht unbesehen auf Anhang I Abschnitt B übertragen. Tatsächlich einschlägiges Produktverfahren und KI-Pflichten gesondert zuordnen. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)

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

> Fiktives Szenario: Ein kniender Mitarbeiter wird bei Gegenlicht nicht erkannt. Für die behauptete Ausfallwahrscheinlichkeit, redundante Sensorik und Stoppgrenze fehlen belastbare Testnachweise. Erstellen Sie einen konkreten Nachtestauftrag. Ein angenommener Konfidenzwert oder ein jährliches Audit belegt noch kein vertretbares Restrisiko. Konformitätsweg erst nach Produkt- und Funktionsprüfung festlegen; ein Cobot ist nicht automatisch ein Anhang-VI-Fall.

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

## Eskalationspfad bei Sicherheitsvorfall

1. **Sofort (T+0 bis T+1h)**: Stillstand, Sicherheitsraum sichern, Verletzte versorgen, Behörden bei Personenschaden.
2. **T+1h bis T+24h**: Logs sichern (Hash, Write-Lock), Versionsstände dokumentieren, Forensik startklar machen.
3. **Vorfallfristen getrennt bestimmen:** Artikel 73: unverzüglich nach dem maßgeblichen Kenntnis-/Kausalitätsstand melden, nicht die Höchstfrist ausschöpfen. Absatz 2 höchstens 15 Tage; Absatz 3 bei weitverbreitetem Verstoß oder Ereignis nach Artikel 3 Nummer 49 Buchstabe b höchstens zwei Tage; Absatz 4 bei Tod unter seinen Kausalitätsvoraussetzungen höchstens zehn Tage. Unvollständige Erstmeldung und Ergänzungen nach Absatz 5 ermöglichen. Rolle, Zuständigkeit und Zeitrecht gesondert prüfen. Cyber- und Datenschutzmeldungen mit eigenem Kenntnisstand, Tatbestand und Adressaten führen; keine starre KI-Meldung erst im Fenster T+24 bis T+72 Stunden. [amtlicher Text, geprüft 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
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
