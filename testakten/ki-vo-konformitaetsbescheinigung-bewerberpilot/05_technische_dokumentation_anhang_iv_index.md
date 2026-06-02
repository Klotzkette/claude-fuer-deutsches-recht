# Technische Dokumentation: Anhang-IV-Index

**Stand:** 17.05.2026 (Aktualisierung KW 21 geplant)
**Bearbeitung:** Product Compliance Team, Dr. Caspar Lintorf
**Aktenzeichen intern:** BP-DOC-2026-IV-01

Dieser Index folgt der Reihenfolge des Anhangs IV der KI-VO und ordnet jeder Anforderung ein konkret benanntes Dokument oder eine Dokumentengruppe zu. Spalten: Index (intern), Dokument, Bezug Artikel/Anhang, Status (Ampel), Fundstelle (Pfad im Spreebogen-Drive oder Aktenkapitel).

| Index | Dokument | Artikel/Anhang | Status | Fundstelle |
|---|---|---|---|---|
| TD-01 | Systembeschreibung und Zweckbestimmung | Anhang IV Nr. 1 | Grün | Produktakte Kapitel 1, Version v2.4 vom 13.05.2026 |
| TD-02 | Architekturdiagramm und Datenflüsse | Anhang IV Nr. 2 lit. a) und b) | Gelb | Architekturordner, Diagramm v0.9 vom 22.04.2026 |
| TD-03 | Modellbeschreibung Merkmalsextraktion | Anhang IV Nr. 2 lit. c) | Grün | Model Card Extractor v2.4 |
| TD-04 | GPAI-Komponente LexiCore (Lieferanteninformation) | Anhang IV Nr. 2 lit. c) + Lieferantenklausel | Gelb | Supplier Attestation 2026-05 (knapp), Modellversion fehlt |
| TD-05 | Trainings-, Validierungs- und Testdaten | Art. 10, Anhang IV Nr. 2 lit. d) | Gelb/Rot | Data Governance Ordner; D-Train-2024-HR nicht vollständig dokumentiert |
| TD-06 | Risikomanagementakte | Art. 9, Anhang IV Nr. 3 | Gelb | Risk Register 2026-05 (R-01 bis R-08) |
| TD-07 | Human-Oversight-Konzept | Art. 14, Anhang IV Nr. 4 | Gelb | Oversight SOP v0.8; Praxistest fehlt |
| TD-08 | Logging-Konzept | Art. 12, Anhang IV Nr. 5 | Grün/Gelb | Logging Spec v1.1, Implementierung in Release Candidate |
| TD-09 | Accuracy/Robustness/Cybersecurity | Art. 15, Anhang IV Nr. 6 | Gelb | Test Report RC2 vom 05.05.2026 |
| TD-10 | Gebrauchsanweisung für Betreiber | Art. 13, Anhang IV Nr. 7 | Gelb | User Manual Draft v0.7, Beta bei Elbtal |
| TD-11 | Konformitätsbewertung | Art. 43, Anhang IV Nr. 8 | Gelb | Checkliste 2026-05 (07_konformitaetsbewertung_art_43_checkliste.md) |
| TD-12 | Post-Market Monitoring | Art. 72, Anhang IV Nr. 9 | Gelb | PMM Plan Draft v0.5 |
| TD-13 | QMS-Dokumentation | Art. 17 | Gelb | QMS-Handbuch BP-QMS-2026 Rev. 02 |
| TD-14 | EU-Konformitätserklärung | Art. 47, Anhang V | Gelb | Entwurf, vgl. 09_eu_konformitaetserklaerung_anhang_v_entwurf.md |
| TD-15 | Datenschutz-Folgenabschaetzung | Art. 35 DSGVO (i.V.m. KI-VO Berührungspunkten) | Gelb | DSFA Bewerberpilot v0.6 vom 14.05.2026 |
| TD-16 | Bias-Auditbericht | Art. 10 KI-VO | Gelb | Bias-Audit-Bericht v0.4 vom 20.05.2026 |
| TD-17 | Konfigurations- und Versionsprotokoll | Art. 11/12/15 KI-VO | Grün | Git-Tag bp-tr-v2.4-rc; Konfigurations-Logfile-Auszug Kapitel 13 |
| TD-18 | Beschwerdemanagement (Bewerberseite) | Art. 19 KI-VO + DSGVO Art. 12-22 | Gelb | erste Beschwerde dokumentiert (Bewerber B-2026-0411) |

## Lieferantennachweis LexiCore Systems Inc.

LexiCore Systems Inc. (Boston, MA, USA) liefert eine **Supplier Attestation 2026-05** (Datum 04.05.2026, drei Seiten, unterzeichnet durch Compliance Officer Maya Chen). Diese erklärt:

- Das Modell "LexiCore Coordinator v3.1" ist nicht für finale HR-Entscheidungen bestimmt.
- Kundendaten werden nicht zum Training verwendet.
- Technische Dokumentation wird auf Anfrage bereitgestellt.
- Das Modell unterliegt internen Bias-Tests im Quartalsrhythmus.

Der Nachweis reicht für das Evidence-Pack **noch nicht** aus, weil folgende Angaben fehlen:

1. Genaue Modellversion (Coordinator v3.1 vs. v3.1.2 vs. v3.2)
2. Evaluationsgrenzen (welche Sprachen, welche Domainfilter)
3. Sicherheitsfilter (welche Prompt-Injection-Mitigations sind aktiv)
4. Mindestkontextfenstergroesse
5. Reaktion auf besondere Kategorien personenbezogener Daten
6. No-Training-Nachweis als Vertragsklausel (nicht nur als Erklärung)

Eine Nachforderung wurde am 19.05.2026 durch Vendor Management (Lara Berghoff) gestellt. Antwortfrist 07.06.2026.

## Datenherkunft Trainingsdaten 2024 (D-Train-2024-HR)

Die Datenherkunft 2024 ist heterogen:

- 18.700 Profile aus Kunde A (PflegePilot Care GmbH, Berlin) — Datenliefervereinbarung vorhanden, Pseudonymisierungsprotokoll vorhanden.
- 16.400 Profile aus Kunde B (Tellbach Klinikgruppe, Hannover) — Datenliefervereinbarung vorhanden, Pseudonymisierungsprotokoll **fehlt**.
- 13.100 Profile aus Kunde C (StadtPersonal Süd AG, Muenchen) — Datenliefervereinbarung **vorhanden, aber im Lichte der KI-VO nicht spezifisch genug**; Pseudonymisierungsprotokoll vorhanden.

Aktion: Mit Kunde B (Tellbach Klinikgruppe) ist eine Nachvereinbarung des Pseudonymisierungsprotokolls erforderlich, Frist 14.06.2026. Mit Kunde C ist eine Datenliefervereinbarung-Erweiterung in Vorbereitung.

## Lese- und Nachweispflichten

Die Anbieterin hält die in Anhang IV genannten Dokumente über den vollständigen Lebenszyklus des KI-Systems vor (mindestens 10 Jahre nach Inverkehrbringen, Art. 18 KI-VO). Der Index TD-01 bis TD-18 wird im Quartalsrhythmus aktualisiert.

## Dokumentationsentscheidung

Der technische Dokumentationsstand ist für eine **Readiness-Bescheinigung** brauchbar, aber für eine **finale Konformitaetsbescheinigung** noch nicht geschlossen. Die blockierenden Lücken liegen in TD-04 (LexiCore), TD-05 (Trainingsdaten), TD-07 (Oversight-Praxistest) und TD-09 (Test Report finale Freigabe).
