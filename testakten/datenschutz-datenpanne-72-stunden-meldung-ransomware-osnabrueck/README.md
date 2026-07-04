# Testakte: Datenpanne und 72-Stunden-Meldung nach Ransomware (Osnabrück)


<!-- BEGIN gesamt-pdf-section (autogen) -->
## Akte komplett herunterladen

Dieses Aktenpaket gibt es in mehreren Formaten zum Direkt-Download. Das Gesamt-PDF eignet sich zum Lesen, Ausdrucken und für schnelle Durchsichten. Das Akten-ZIP enthält sämtliche Originaldateien (DOCX-Aktenstücke mit Briefkopf, Tabellen, E-Mails, Fotos, PDFs, XLSX) im Originalordnerlayout für eigene Auswertungen. Das Einzel-PDF-ZIP liefert jede einzelne Unterlage als separate, sauber gerenderte PDF im Originalordnerlayout — praktisch, wenn nur einzelne Aktenstücke gebraucht werden.

| Was | Format | Quelle |
| --- | --- | --- |
| Gesamt-PDF (alles in einer Datei, 48 KB) | PDF | [`gesamt-pdf/datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck_gesamt.pdf`](gesamt-pdf/datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck_gesamt.pdf) |
| Akten-ZIP (alle Einzeldateien) | ZIP | [testakte-datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck.zip) |
| Einzel-PDF-ZIP (jede Unterlage als eigene PDF) | ZIP | [testakte-datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck-einzelpdfs.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck-einzelpdfs.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Im Akten-ZIP ist das Gesamt-PDF mit enthalten.

<!-- END gesamt-pdf-section (autogen) -->

Die Hasetal Versandhandel GmbH, ein mittelständischer Online-Versandhändler aus Osnabrück mit rund 240.000 Kundenkonten, wurde in der Nacht vom Freitag, dem 12.06.2026, auf Samstag, den 13.06.2026, Ziel eines Ransomware-Angriffs der Gruppierung „DarkVault". Vor der Verschlüsselung der zentralen Server flossen 382 Gigabyte ab, darunter ein vollständiger Auszug der Kundendatenbank mit Namen, Anschriften, E-Mail-Adressen, Bestellhistorien und bei 96.400 Konten der Bankverbindung. Der erste als kritisch klassifizierte Alarm datiert auf Freitag, 22:14 Uhr, wurde aber vom Bereitschaftsdienst um 23:41 Uhr als Fehlalarm geschlossen. Am Samstagvormittag stand die Verschlüsselung des Kernbestands fest; die Bestätigung des Datenabflusses durch die Forensik erfolgte am Montag, dem 15.06.2026, um 09:30 Uhr. Gemeldet wurde erst am Mittwoch, dem 17.06.2026, um 16:45 Uhr.

Prüfschwerpunkte sind der Beginn der 72-Stunden-Frist (Kenntnis im Sinne des Artikel 33 Absatz 1 DSGVO), die Rechtzeitigkeit und Vollständigkeit der Meldung sowie die Erforderlichkeit der Benachrichtigung der betroffenen Personen bei hohem Risiko (Artikel 34 DSGVO). Der Datenauswertungs-Kern besteht darin, aus dem SIEM-Export, dem Ticketsystem-Export und dem Krisen-Chat den maßgeblichen Kenntniszeitpunkt zu rekonstruieren und die Fristberechnung je nach Anknüpfungspunkt (Freitag 22:14 Uhr, Samstag 09:47 Uhr oder Montag 09:30 Uhr) minutengenau durchzuführen. Die gewollte Diskrepanz: Die Meldung an die LfD Niedersachsen behauptet Kenntnis „erst Montag", während der Krisen-Chat belegt, dass der IT-Leiter die vollständige Verschlüsselung bereits am Samstagvormittag kannte und der Datenschutzbeauftragte noch am selben Tag auf den Fristbeginn hingewiesen hat.

## Beteiligte

| Rolle | Person / Stelle |
| --- | --- |
| Verantwortliche Stelle | Hasetal Versandhandel GmbH, Mindener Straße 212, 49084 Osnabrück, HRB 21884 (AG Osnabrück) |
| Geschäftsführung | Bernd Wiechers |
| IT-Leiter | Thorben Schwegmann |
| Rufbereitschaft (Fehlklassifikation) | Jannik Plettner |
| IT-Administration | Melanie Averbeck |
| Datenschutzbeauftragter (extern) | Dr. Klaus Rosenthal, Osnabrück |
| Forensikdienstleister | NordicShield Forensics GmbH, Hamburg (Az. NS-2026-0614-HAS), Dr. Ingo Vahlbrecht |
| Angreifergruppe | „DarkVault" (fiktiv) |
| Aufsichtsbehörde | Die Landesbeauftragte für den Datenschutz Niedersachsen, Hannover (Az. LfD-Nds 33-2026/00417), RD'in Frauke Menkhaus |

## Aktenstruktur

```
datenschutz-datenpanne-72-stunden-meldung-ransomware-osnabrueck/
├── 01_incident_report_forensik_2026-06-22.docx        — Forensischer Abschlussbericht, dezimal gegliedert, mit Angriffs- und Zeitverlauf
├── 02_siem_alert_export_2026-06.csv                   — SIEM-Alarme mit Zeitstempeln; erster kritischer Alarm 12.06. 22:14 Uhr
├── 03_ticketsystem_export_2026-06.csv                 — Ticketverlauf INC-4471 bis INC-4478; Fehlalarm-Schließung und Wiedereröffnung
├── 05_meldung_art33_lfd_niedersachsen_2026-06-17.docx — Meldung nach Artikel 33 DSGVO im Formularstil, behauptet Kenntnis erst Montag
├── 06_nachmeldung_art33_2026-06-24.docx               — Nachmeldung mit Erstzugang, Abflussumfang und Leak-Hinweis
├── 07_anhoerung_lfd_niedersachsen_2026-06-26.docx     — Anhörungsschreiben der Behörde zu Kenntniszeitpunkt und TOM
├── 08_stellungnahme_unternehmen_2026-07-02.docx       — Antwort des Unternehmens, hält an „Kenntnis Montag" fest
├── 09_betroffenenbenachrichtigung_entwurf.docx        — Entwurf der Artikel-34-Benachrichtigung mit bewussten Mängeln
├── 10_vvt_auszug_kundendatenbank.docx                 — Auszug aus dem Verzeichnis von Verarbeitungstätigkeiten mit Datenumfang
├── 11_tom_liste_stand_2026-01.csv                     — Technische und organisatorische Maßnahmen, Stand vor dem Vorfall
├── 12_eingangsbestaetigung_meldeportal_2026-06-17.docx — Automatische Eingangsbestätigung der Behörde mit Uhrzeit
├── 13_dsb_vermerk_fristberechnung_2026-06-25.docx     — DSB-Vermerk mit Gegenmeinung zur Fristberechnung
├── teams-chat/
│   └── 04_krisenstab_darkvault_2026-06.txt            — Krisen-Chat des IT-Krisenstabs; belegt Kenntnis am Samstagvormittag
├── eml/
│   ├── 2026-06-08_phishing_auftrag_2984.eml           — Phishing-Mail mit Makro-Anhang als Erstzugangsvektor
│   ├── 2026-06-13_erpresserschreiben_darkvault.eml    — Lösegeldforderung mit Bestätigung des Datenabflusses
│   └── 2026-06-15_forensik_bestaetigung_exfiltration.eml — Forensik-Mail, bestätigt Exfiltration am 15.06. 09:30 Uhr
├── rubric.yaml                                        — Sechs Prüfpunkte zur Bewertung einer Bearbeitung
└── README.md                                          — Diese Übersicht
```
