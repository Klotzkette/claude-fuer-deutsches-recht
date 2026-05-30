# Datenschutz-Folgenabschätzung (DPIA) — RecruitAI

**Aktenzeichen intern:** TI-KI-2026-012
**Behördliches AZ:** LfDI BW AZ 1-1085.51/2026/045
**Dokumentversion:** 0.8 (Entwurf, nicht freigegeben)
**Erstellungsdatum:** 10. März 2026
**Verfasserin:** Dr. Carla Eichenmüller, Datenschutzbeauftragte Thalheim Industries SE
**Mitarbeit:** Barbara Trenkmann (HR-Systemverantwortliche); Marcus Petersen (CDO)
**Vorlage-Frist:** 30. Juni 2026 (gemäß LfDI BW Schreiben 02.03.2026)

---

## 1. Einleitung und Rechtsgrundlage

Die Thalheim Industries SE ist gemäß Art. 35 Abs. 1 und Abs. 3 DSGVO (https://dejure.org/gesetze/DSGVO/35.html) verpflichtet, für die Verarbeitung personenbezogener Daten mittels des KI-Systems **RecruitAI** (Vendor: Synaptec Analytics GmbH) eine Datenschutz-Folgenabschätzung (DPIA) durchzuführen.

Die DPIA-Pflicht ergibt sich aus:
- Art. 35 Abs. 3 lit. a DSGVO: Systematische und umfassende Bewertung persönlicher Aspekte natürlicher Personen durch automatisierte Verarbeitung einschließlich Profiling mit erheblichen Folgen für die betroffene Person → Bewerber-Ranking mit Einstellungsrelevanz.
- Art. 35 Abs. 3 lit. b DSGVO: Umfangreiche Verarbeitung besonderer Kategorien von Daten (Art. 9 DSGVO) — nicht ausgeschlossen (Rückschlüsse auf Herkunft, Geschlecht aus Lebensläufen).
- LfDI BW Positivliste: Automatisierte Entscheidungsunterstützung im Recruiting ausdrücklich aufgeführt.
- KI-VO-Synergiegebot: Art. 9 KI-VO und Art. 35 DSGVO sollen koordiniert angewendet werden (Erwägungsgrund 159 KI-VO).

Das Landesbeauftragte für Datenschutz und Informationsfreiheit Baden-Württemberg (LfDI BW) hat mit Schreiben vom 02.03.2026 (AZ 1-1085.51/2026/045) die Vorlage der vollständigen DPIA bis 30.06.2026 angefordert.

---

## 2. Systembeschreibung

| Merkmal | Inhalt |
|---|---|
| Systemname | RecruitAI |
| Anbieter | Synaptec Analytics GmbH, Leopoldstraße 18, 80802 München |
| Einsatz seit | 01. September 2024 |
| Einsatzzweck | Automatisiertes Screening und Ranking von Bewerbungsunterlagen für alle Stellenausschreibungen der Thalheim Industries SE |
| Datenkategorien | Name, Vorname, Kontaktdaten, Lebenslauf, Zeugnisse, Foto (falls beigefügt), Anschreiben, LinkedIn-Profil (optionale Verknüpfung) |
| Betroffene Personen | Bewerberinnen und Bewerber (extern), durchschnittlich 4.500 Bewerbungen p.a. |
| Entscheidungstiefe | Ranking-Score 0–100; Schwelle 65 für automatische Weiterleitung; unter 40 automatische Ablehnung möglich (Override durch HR vorgesehen) |
| Datenspeicherung | Synaptec-Server (EU, Frankfurt a.M.); Aufbewahrung: 6 Monate nach Abschluss Stellenbesetzung |
| Schnittstellen | SAP SuccessFactors (ATS), Outlook (Kommunikation), Active Directory |

---

## 3. Beschreibung des Verarbeitungsvorgangs

**Verarbeitungsschritte:**

1. Eingang der Bewerbungsunterlagen über das Thalheim-Karriereportal oder E-Mail.
2. Automatische Extraktion strukturierter Daten (CV-Parsing): Berufserfahrung, Ausbildung, Skills, Sprachkenntnisse.
3. Scoring durch das RecruitAI-Modell: Vergleich der Kandidatenprofil-Vektoren mit einem Job-Requirement-Profil (erstellt durch HR-Business-Partner).
4. Ranking-Ergebnis: Score-Liste aller Kandidaten für die Stelle.
5. HR-Business-Partner sieht Ranking, kann manuell überstimmen (Override), gibt Bewerbungen in die nächste Runde.
6. Kandidaten unter Schwelle 40: automatische Ablehnungsmail — **kritischer Punkt für Art. 22 DSGVO**.

---

## 4. Notwendigkeit und Verhältnismäßigkeit

**Zweck:** Effiziente Bewältigung hoher Bewerbungsvolumina (4.500 p.a.) bei gleichzeitiger Sicherung einheitlicher Qualitätsstandards.

**Verhältnismäßigkeit:** Das System ist grundsätzlich geeignet und erforderlich. Kritisch ist jedoch die automatische Ablehnung unterhalb der Schwelle 40, die einen Fall von Art. 22 Abs. 1 DSGVO (https://dejure.org/gesetze/DSGVO/22.html) darstellen kann, wenn kein HR-Mensch aktiv eingreift. Synaptec behauptet, dass jede Ablehnungsentscheidung technisch von HR bestätigt werden muss — dies ist jedoch in der Praxis nicht vollständig implementiert (Feststellung Hagedorn-Audit, 28.02.2026).

---

## 5. Risikoidentifikation und -bewertung

| Risiko | Wahrscheinlichkeit | Schwere | Risikostufe | Maßnahme |
|---|---|---|---|---|
| Bias / Diskriminierung (Geschlecht, Herkunft) | Mittel | Hoch | **Hoch** | Bias-Tests erforderlich (fehlen derzeit) |
| Automatische Ablehnung ohne menschliche Kontrolle | Mittel | Hoch | **Hoch** | SOP und technische Sperre erforderlich |
| Fehlende Transparenz gegenüber Bewerbern | Hoch | Mittel | **Hoch** | Datenschutzhinweis aktualisieren |
| Datenpanne (Synaptec-Server) | Niedrig | Hoch | Mittel | AVV, Pen-Test, ISO 27001 Synaptec |
| Profilbildung / Scope Creep | Niedrig | Mittel | Niedrig | Datenminimierungspflicht vertraglich |
| Rückschlüsse auf Sonderkategorien (Art. 9 DSGVO) | Mittel | Sehr hoch | **Hoch** | Filterung besonderer Kategorien technisch |

---

## 6. Konsultation des Datenschutzbeauftragten

Dr. Eichenmüller wurde als Datenschutzbeauftragte gemäß Art. 35 Abs. 2 DSGVO bereits zu Beginn der DPIA eingebunden. Sie hat die Risikoidentifikation begleitet und empfiehlt die vollständige Implementierung aller Maßnahmen aus Abschnitt 5, bevor RecruitAI im Vollbetrieb verbleibt. Sie empfiehlt außerdem, eine Konsultation des LfDI BW nach Art. 36 DSGVO zu prüfen, falls die Risiken nicht vollständig eingedämmt werden können (Bias-Tests ausstehend).

---

## 7. Offene Punkte (Stand: März 2026)

| Offener Punkt | Verantwortlich | Frist |
|---|---|---|
| Bias-Tests Synaptec — Durchführung und Dokumentation | Synaptec / CIO Wolfsbacher | 30.05.2026 |
| Technische Sperre: keine Ablehnung ohne aktiven HR-Override | IT / Synaptec | 30.04.2026 |
| Aktualisierung Datenschutzhinweis Karriereportal (Art. 13 DSGVO) | DSB / HR | 31.03.2026 |
| Überarbeitung Kandidaten-Kommunikation: Hinweis KI-gestütztes Screening | HR / Kommunikation | 31.03.2026 |
| Überprüfung AVV mit Synaptec (neue KI-VO-Klauseln) | DSB / Legal | 30.04.2026 |
| Abschluss DPIA-Bericht und Einreichung LfDI BW | DSB Dr. Eichenmüller | 30.06.2026 |

---

*Aktenzeichen: TI-KI-2026-012. LfDI BW: AZ 1-1085.51/2026/045. Verfasserin: Dr. C. Eichenmüller. Entwurf v0.8, Stand März 2026.*
