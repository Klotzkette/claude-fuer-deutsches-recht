# Testakte: KI-Recht — Konformitätsbewertung mit Lücken an der Schnittstelle zum Medizinprodukterecht (Triage-System, Freiburg)


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 50 KB) | PDF | [`gesamt-pdf/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg_gesamt.pdf`](gesamt-pdf/ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Die SaniScore Medizintechnik GmbH (Freiburg) will das Hochrisiko-KI-System „TriageAssist" (Version 2.1) in Verkehr bringen, ein entscheidungsunterstützendes Software-Medizinprodukt zur Ersteinschätzung der Behandlungsdringlichkeit in Notaufnahmen. Das Produkt fällt zugleich unter die Medizinprodukteverordnung (Verordnung (EU) 2017/745) und die KI-Verordnung (Verordnung (EU) 2024/1689); die Konformitätsbewertung soll integriert durch eine benannte Stelle erfolgen. Die Akte bildet den Konformitätsbewertungsprozess ab: Produktbeschreibung, Zweckbestimmung, Risikomanagement, technische Dokumentation, Datenübersicht, Validierungslog, Testberichte, Konzept zur menschlichen Aufsicht, den Entwurf der EU-Konformitätserklärung, den Beanstandungsbericht der benannten Stelle sowie interne Entwickler-Kommunikation.

Prüfschwerpunkte sind die Anforderungen an Hochrisiko-KI-Systeme (Risikomanagement, Daten und Daten-Governance, technische Dokumentation, Protokollierung, menschliche Aufsicht, Genauigkeit, Robustheit und Cybersicherheit) und ihr Zusammenspiel mit dem Medizinprodukterecht. Datenauswertungs-Kern: Aus dem Performance-Log (Aktenstück 06) und der Datenübersicht (Aktenstück 05) muss die Bearbeitung selbst nachweisen, dass die technische Dokumentation die Genauigkeit für die Altersgruppe ab 80 Jahren überschätzt — Gesamtsensitivität exakt 94 Prozent (94 von 100), aber nur 15 von 21 (rund 71 Prozent) in der Altersgruppe ab 80 Jahren gegenüber 79 von 79 (100 Prozent) darunter, bei einer Unterrepräsentation dieser Gruppe im Training von nur rund 4.6 Prozent. Gewollte Diskrepanz: Der Entwurf der EU-Konformitätserklärung (Aktenstück 11) behauptet vollständige Konformität und eine „über alle Patientengruppen gleichwertige Leistung", während technische Dokumentation, Logs, Aufsichtskonzept und Risikoregister dem widersprechen; der Beanstandungsbericht der benannten Stelle (Aktenstück 12) hält dies fest. Ein Normstand-Vermerk regelt den Umgang mit dem beweglichen Rechtsstand der KI-Verordnung; alle Artikel- und Fristangaben sind vor Verwendung amtlich zu verifizieren.

## Beteiligte

| Rolle | Person / Stelle |
| --- | --- |
| Herstellerin / Anbieterin | SaniScore Medizintechnik GmbH, Georges-Köhler-Allee 12, 79110 Freiburg (HRB 71204, AG Freiburg) |
| Geschäftsführung (medizinisch) | Dr. med. Katharina Vollmer |
| Geschäftsführung / CTO | Dipl.-Ing. Tobias Reinke |
| Leitung Regulatory Affairs (verantwortliche Person) | Dr. Annika Sperling |
| Modellentwicklung / Data Science | Dr. Jonas Kettler |
| Klinische Bewertung | Petra Lohmann |
| Benannte Stelle | Prüf- und Zertifizierungsstelle für Medizinprodukte Süd GmbH (PZM Süd), NB 2971 (fiktiv), Stuttgart |
| Leitende Auditorin | Dr. Ing. Marion Halbach |
| Marktüberwachungsbehörde KI | Bundesnetzagentur, Referat Marktüberwachung KI-Systeme, Bonn |
| Zuständige Behörde Medizinprodukte | Bundesinstitut für Arzneimittel und Medizinprodukte (BfArM), Bonn |

## Aktenstruktur

```
ki-recht-konformitaetsbewertung-luecken-medizinprodukt-triage-freiburg/
├── 01_produktbeschreibung_triageassist_2025-11.docx                       — Produkt- und Funktionsbeschreibung, Sensitivität als sicherheitskritische Kenngröße
├── 02_zweckbestimmung_und_medizinprodukt_einordnung_2025-11.docx          — Zweckbestimmung, Einordnung als Klasse-IIb-Medizinprodukt und Hochrisiko-KI
├── 03_risikomanagement_akte_auszug_2026-01.docx                           — Risikoregister; Subgruppenrisiko nur als offener Hinweis, nicht aufgenommen
├── 04_technische_dokumentation_auszug_2026-02.docx                        — Behauptet 94 Prozent über alle Gruppen und keine Subgruppenunterschiede
├── 05_datenuebersicht_training_validierung.csv                            — Datensätze je Klinik, Demografie, Fehlerraten (Rohdaten Daten-Governance)
├── 06_performance_log_validierung.csv                                     — 140 Validierungsfälle mit Referenz- und Systemeinstufung (Rohdaten Genauigkeit)
├── 07_testbericht_genauigkeit_robustheit_2026-03.docx                     — Enthält die stratifizierte Tabelle (79 von 79 gegen 15 von 21)
├── 08_testbericht_cybersicherheit_protokollierung_2026-03.docx           — Penetrationstest offen; Übersteuerungen nicht protokolliert, keine Aufbewahrungsfrist
├── 09_menschliche_aufsicht_konzept_2026-02.docx                           — Kein Übersteuerungsverfahren, keine Schulungsvorgabe, kein Grenzenhinweis
├── 10_antrag_konformitaetsbewertung_benannte_stelle_2026-04.docx          — Antrag auf integriertes Verfahren MDR und KI-Verordnung
├── 11_entwurf_eu_konformitaetserklaerung_2026-05.docx                     — Entwurf behauptet vollständige Konformität und gleichwertige Leistung (Diskrepanz)
├── 12_vermerk_benannte_stelle_beanstandungen_2026-06.docx                 — Vier wesentliche Beanstandungen; widerlegt den Erklärungsentwurf
├── 13_normstand_vermerk_2026-07-01.docx                                   — Rechtsstand KI-Verordnung, Omnibus-Vorbehalt, Verifikationsanordnung
├── eml/
│   ├── 2026-02-10_kettler_an_sperling_subgruppe.eml                       — Warnung der Modellentwicklung: 71 Prozent bei über 80-Jährigen, Datenlage dünn
│   ├── 2026-02-14_sperling_an_kettler_zeitplan.eml                        — Entscheidung, nur den Gesamtwert zu führen; Ursprung der Diskrepanz
│   └── 2026-06-24_reinke_an_gf_nach_audit.eml                             — Nach dem Beanstandungsbericht: Umsteuern, Erklärung zurücknehmen
├── chat/
│   └── teams_chat_entwicklung_triageassist_2026-02.txt                    — Teamchat zu Subgruppenproblem, fehlender Protokollierung und Aufsicht
├── rubric.yaml                                                            — Sechs Prüfpunkte zur Bewertung einer Bearbeitung
└── README.md                                                             — Diese Übersicht
```
