# 05 — Datenschutz-Folgenabschaetzung (DSFA) nach Art. 35 DSGVO

**Aktenzeichen:** DSB-NW-44/26
**Bearbeiter:** RAin Miriam Beckenbauer, RA Dr. Cornelius Specht
**Datum:** 20. Januar 2026
**Betreff:** DSFA-Versäumnis für ProspectScore Pro und Nachholungsplan

---

## 1. Rechtliche Grundlage und Pflicht zur DSFA

Art. 35 Abs. 1 DSGVO verpflichtet den Verantwortlichen, vor der Verarbeitung eine Abschätzung der Folgen der vorgesehenen Verarbeitungsvorgänge für den Schutz personenbezogener Daten durchzuführen, wenn eine Verarbeitung voraussichtlich ein hohes Risiko für die Rechte und Freiheiten natürlicher Personen zur Folge hat.

### 1.1 Regelbeispiele nach Art. 35 Abs. 3 DSGVO

Art. 35 Abs. 3 DSGVO nennt als typische Hochrisikoverarbeitungen:
- **lit. a:** Systematische und umfassende Bewertung persönlicher Aspekte natürlicher Personen durch automatisierte Verarbeitung einschliesslich Profiling (explizit: Bonitätsermittlung)
- **lit. c:** Systematische Überwachung öffentlich zugänglicher Bereiche (hier nicht einschlägig)

**Ergebnis:** ProspectScore Pro fällt unmittelbar unter Art. 35 Abs. 3 lit. a DSGVO. Die DSFA-Pflicht war von Beginn an gegeben.

### 1.2 Negativlisten und Positivlisten der LDI NRW

Gemaess Art. 35 Abs. 4 und Abs. 5 DSGVO haben Aufsichtsbehörden Listen der Verarbeitungen zu erstellen, die einer DSFA bedürftig sind (Muss-Listen) bzw. nicht bedürftig sind (Ausnahmelisten). Die LDI NRW hat in ihrer aktuellen Muss-Liste (Stand Oktober 2025) ausdrücklich „KI-gestützte Scoring-Verfahren zur Mietinteressenten-Beurteilung" aufgeführt.

---

## 2. DSFA-Checkliste: Ist eine DSFA erforderlich?

| Kriterium (DSK-Standard 2017) | Befund bei VCS | Punkte |
|-------------------------------|----------------|--------|
| Bewertung oder Einstufung | Ja (Score 0–100, Ampel) | 1 |
| Automatisierte Entscheidung mit Rechtswirkung | Ja (Mietabsagen) | 1 |
| Systematische Überwachung | Mittel (kein Tracking, aber Massenverarbeitung) | 0,5 |
| Sensitive oder hochpersönliche Daten | Ja (Schufa, Familienstatus) | 1 |
| Grosse Mengen / Betroffene | Ja (142.300 Datensätze) | 1 |
| Verknüpfung verschiedener Datensätze | Ja (Schufa + Selbstauskunft + Profiling) | 1 |
| Innovative Technologie | Ja (KI-Modell ohne DSFA-Vorlage) | 1 |
| Hinderung der Ausübung von Rechten | Ja (Wohnungszugang) | 1 |

**Gesamtbewertung:** 7,5 von 8 Punkten. Ab 2 Punkten ist eine DSFA erforderlich. **DSFA-Pflicht eindeutig bejaht.**

---

## 3. Dokumentiertes Versäumnis

### 3.1 Zeitlinie

| Datum | Ereignis |
|-------|----------|
| Jan 2023 | Interne Entwicklung ProspectScore Pro (v1.0) |
| Mrz 2023 | Go-Live Produktivbetrieb — keine DSFA durchgeführt |
| Jun 2023 | Upgrade auf v2.0 (neues ML-Modell) — keine DSFA |
| Feb 2024 | Upgrade auf v3.0 (erweiterte Datenkategorien) — keine DSFA |
| Nov 2025 | Erste interne Kenntnis des DSFA-Versäumnisses (Whistleblower-Meldung) |
| Jan 2026 | Mandatsuebernahme SBD — DSFA noch immer ausstehend |

### 3.2 Interne Warnsignale

- Datenschutzbeauftragte Frau Kessler-Brandt hat laut eigener Aussage zweimal (Mai 2023, Oktober 2024) intern auf die DSFA-Pflicht hingewiesen — ohne Ergebnis
- Diese internen Warnhinweise wurden nicht dokumentiert (fehlende Schriftform)
- Der Geschäftsführer wurde mündlich informiert und hat die DSFA als „nicht praxisrelevant" abgetan

---

## 4. Inhalt einer nachzuholenden DSFA

Die DSFA muss gemaess Art. 35 Abs. 7 DSGVO mindestens enthalten:

### 4.1 Systematische Beschreibung der Verarbeitungsvorgänge (Art. 35 Abs. 7 lit. a)

```
Verarbeitungsvorgang: Automatisiertes Profiling von Mietinteressenten
Zweck: Risikobeurteilung fuer angeschlossene Privatvermieter
Datenkategorien: Schufa-Score, Negativmerkmale, Beruf, Einkommen,
                  Familienstatus, Haushaltsgroesse
Verarbeitung: ML-Modell ProspectScore Pro v3.0 (Random Forest + Neural Net)
Empfaenger: Privatvermieter (B2B-Kunden, 12.400+)
Drittlandtransfer: Sundara Tech Pvt. Ltd. (Bengaluru) — Entwicklung/Support
Speicherdauer: 24 Monate nach letzter Abfrage
```

### 4.2 Beurteilung der Notwendigkeit und Verhaeltnismaessigkeit (Art. 35 Abs. 7 lit. b)

Die Erhebung des Familienstatus und der Haushaltsgroesse ist für den legitimen Zweck der Bonitätsprüfung nicht erforderlich (Verhaeltnismaessigkeit verletzt). Ausreichend wäre: Schufa-Score + Einkommensnachweise. Alle weiteren Datenkategorien sind zu entfernen.

### 4.3 Risikobewertung (Art. 35 Abs. 7 lit. c)

| Risiko | Eintrittswahrscheinlichkeit | Schwere | Gesamtrisiko |
|--------|----------------------------|---------|-|
| Fehlerhafte Bonitätsbewertung für Betroffene | Hoch | Hoch | KRITISCH |
| Diskriminierung aufgrund Familienstatus | Mittel | Hoch | HOCH |
| Datenleak sensibler Scoring-Daten | Realisiert (CVE-2026-0188) | Sehr hoch | KRITISCH |
| Drittlandtransfer ohne SCC | Hoch | Hoch | KRITISCH |
| Nichtbeachtung Widerruf / Löschung | Mittel | Mittel | MITTEL |

### 4.4 Geplante Massnahmen zur Risikominimierung (Art. 35 Abs. 7 lit. d)

1. Human-in-the-Loop (HITL) Implementierung: Obligatorische menschliche Pruefung
2. Datenminimierung: Streichung Familienstatus und Haushaltsgroesse
3. Auftragsverarbeitungsvertrag (AVV) mit SCC für Sundara Tech
4. Technische Sicherheitsmassnahmen: Behebung CVE-2026-0188, End-to-End-Verschlüsselung
5. Betroffenenrechte: Implementierung Auskunfts-, Widerspruchs- und Loeschungsportal
6. Regelmäßige Pruefung des ML-Modells auf Diskriminierungseffekte (Bias-Audit)

---

## 5. Konsultationspflicht bei LDI NRW (Art. 36 DSGVO)

Gemaess Art. 36 Abs. 1 DSGVO ist der Verantwortliche verpflichtet, vor Beginn der Verarbeitung die Aufsichtsbehörde zu konsultieren, wenn aus der DSFA ein hohes Risiko hervorgeht und der Verantwortliche keine geeigneten Massnahmen zur Eindämmung des Risikos trifft.

Da die DSFA nachträglich durchgeführt wird und das Risiko als KRITISCH eingestuft wurde, ist eine Vorabkonsultation (Art. 36 DSGVO) bei der LDI NRW obligatorisch. Dies wird gleichzeitig zur Entlastung im Aufsichtsverfahren DSB-NW-44/26 genutzt.

---

## 6. Zeitplan DSFA-Nachholung

| Meilenstein | Verantwortlich | Frist |
|-------------|----------------|-------|
| DSFA-Kickoff-Workshop | Dr. Specht + Kessler-Brandt | 20.01.2026 |
| Technische Beschreibung ProspectScore Pro | DevOps-Leiter Bilgic | 27.01.2026 |
| Risikobewertung (extern: SecureProof GmbH) | SecureProof GmbH | 31.01.2026 |
| Entwurf DSFA-Dokument | RAin Beckenbauer | 07.02.2026 |
| Freigabe durch DSB Kessler-Brandt | DSB Kessler-Brandt | 10.02.2026 |
| Einreichung bei LDI NRW (Art. 36 DSGVO) | RA Dr. Specht | 14.02.2026 |

---

## Quellen

- DSGVO Art. 35, 36 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- DSK-Kurzpapier Nr. 5 (DSFA) — [datenschutzkonferenz-online.de](https://www.datenschutzkonferenz-online.de/media/kp/dsk_kpnr_5.pdf)
- LDI NRW Muss-Liste gemaess Art. 35 Abs. 4 DSGVO — [ldi.nrw.de](https://www.ldi.nrw.de)
- EDSA-Leitlinien 09/2022 (DSFA) — [edpb.europa.eu](https://edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-092022-personal-data-breach-notification_de)
- BGH VI ZR 10/24 — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
