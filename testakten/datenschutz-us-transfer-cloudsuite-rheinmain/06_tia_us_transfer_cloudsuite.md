# Transfer Impact Assessment: CloudSuite Assist USA

Organisation: RheinMain Präzisionstechnik GmbH
Stand: 20.05.2026
Bearbeitung: Datenschutzteam, Legal, IT Security, Einkauf

## A. Transferbeschreibung

RheinMain nutzt CloudSuite Assist für CRM und Support. Die produktive Datenbank liegt in Frankfurt; Backups liegen in Dublin. Es bestehen Drittlandbezüge durch anlassbezogenen Supportzugriff aus den USA, Telemetrieverarbeitung in Virginia und ReplyPilot-Verarbeitung durch NorthPeak Analytics LLC in Texas.

Die Daten betreffen überwiegend geschäftliche Ansprechpartner von Kunden und Lieferanten. Freitextfelder enthalten realistisch auch personenbezogene Details, die nicht geplant sind. Besondere Kategorien personenbezogener Daten werden nicht gezielt verarbeitet, können aber zufällig auftauchen.

## B. Transferinstrument

| Transfer | Instrument | Bewertung |
|---|---|---|
| CloudSuite Assist Inc. Support | DPF, sofern Scope bestätigt; SCC Modul 2 als Backup | Tragfähig mit Auflagen |
| Telemetrie Virginia | SCC Modul 2 + TIA | Tragfähig mit technischen Auflagen |
| NorthPeak ReplyPilot | SCC-Kette und TIA noch unvollständig | Vorläufig nicht freigegeben für sensible Freitexte |
| TicketForge Notfall-Wartung | Nachweis offen | Stop bis Rollenklärung |

## C. Drittlandsrecht und Praxis

Die USA sind Gegenstand des EU-US Data Privacy Framework-Angemessenheitsbeschlusses vom 10.07.2023. Für teilnehmende US-Organisationen kann Art. 45 DSGVO greifen. Zusätzlich bleiben Dokumentationspflichten, Scope-Prüfung, Subprozessorprüfung und Review erforderlich.

Für Transfers außerhalb des konkreten DPF-Scopes stützt RheinMain die Übermittlung auf SCC und ergänzende Maßnahmen. Die Anbieterunterlagen beschreiben eine Policy zur Benachrichtigung und Anfechtung von Behördenzugriffen, soweit rechtlich zulässig. Ein aktueller Transparenzbericht wurde angefordert, liegt aber nur als Zusammenfassung für 2025 vor.

## D. Risiko für Betroffene

| Risiko | Einschätzung |
|---|---|
| Identifizierbarkeit | Mittel, da Namen und Kontaktdaten enthalten sind |
| Sensibilität | Niedrig bis mittel; Freitext kann sensible Zufallsdaten enthalten |
| Umfang | Etwa 18.400 Kontaktprofile, 42.000 Tickets seit 2021 |
| Zugriffswahrscheinlichkeit | Niedrig bis mittel; Supportzugriffe anlassbezogen, Telemetrie dauerhaft |
| Schadenspotenzial | Reputations- und Vertraulichkeitsrisiko, besonders bei Reklamations- und Eskalationsdetails |

## E. Ergänzende Maßnahmen

1. Supportzugriff nur nach Ticketfreigabe durch RheinMain-Admin.
2. Monatlicher Export der Support-Access-Logs.
3. Freitext-Hinweis im Ticketformular: keine Gesundheits-, HR- oder privaten Daten eintragen.
4. ReplyPilot-Freigabe nur für Ticketkategorien `Standard`, `Ersatzteil`, `Lieferstatus`; Sperre für `Beschwerde Geschäftsführung`, `Personal`, `Rechtsfall`.
5. EU-Key-Option für besonders schutzbedürftige Kundengruppen prüfen.
6. Subprozessoränderungen mit 30 Tagen Vorlauf und Widerspruchsprozess.
7. Halbjährliche DPF- und Subprozessorprüfung.

## F. Restrestrisiko

Das Restrestrisiko ist für den Kernbetrieb CRM/Support **vertretbar mit Auflagen**. Für ReplyPilot und TicketForge besteht bis zur Vertrags- und Scope-Klärung ein **nicht ausreichend dokumentierter Transfer**. Diese Komponenten sind nicht sofort abzuschalten, aber für Freitexte mit erhöhtem Schutzbedarf zu sperren und vertraglich nachzuziehen.

## G. Entscheidung

**Entscheidungsvorschlag:** Fortführung CloudSuite Assist Kernbetrieb mit DPF/SCC-Dokumentation und Maßnahmenplan. ReplyPilot eingeschränkt fortführen; keine sensiblen Freitexttickets an ReplyPilot. TicketForge-Zugriff bis zur Klärung deaktivieren.

Entscheidungsträger: Geschäftsführung, DSB, IT Security Lead.
Review: 30.06.2026 und danach halbjährlich.
