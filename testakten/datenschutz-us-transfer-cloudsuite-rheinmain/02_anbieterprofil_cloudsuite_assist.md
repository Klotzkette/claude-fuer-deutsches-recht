# Anbieterprofil CloudSuite Assist

Bearbeiterin: Nora Weidemann, Legal Operations
Stand: 16.05.2026

## 1. Vertragskette

| Rolle | Rechtsträger | Sitz | Dokumentenfundstelle |
|---|---|---|---|
| Kunde / Verantwortlicher | RheinMain Präzisionstechnik GmbH | Frankfurt am Main | Rahmenvertrag 22.11.2024 |
| Vertrieb / Vertragspartner | CloudSuite Ireland Ltd. | Dublin, Irland | Order Form, DPA Intro |
| Technische Plattform / Importeur | CloudSuite Assist Inc. | 221 Harbor Street, San José, CA, USA | DPA Annex 1, Security Addendum |
| EU-Hosting | MainRack GmbH | Frankfurt am Main | Subprocessor List, Stand 15.04.2026 |
| KI-Feature | NorthPeak Analytics LLC | Austin, TX, USA | AI Addendum, Stand 04.04.2026 |

## 2. Produktnutzung bei RheinMain Präzisionstechnik

CloudSuite Assist wird in Vertrieb, Kundenservice und Ersatzteilmanagement eingesetzt. Die Plattform führt Kontaktprofile, Supporttickets, Maschinenseriennummern, Reklamationshistorien, E-Mail-Threadauszüge und interne Bearbeitungsvermerke zusammen. Seit März 2026 ist das Zusatzmodul "ReplyPilot" aktiviert. ReplyPilot erstellt Antwortvorschläge für Supportmitarbeitende, darf aber laut interner Arbeitsanweisung keine vollautomatischen Entscheidungen treffen.

Die Geschäftsführung hat am 10.03.2026 entschieden, dass keine besonderen Kategorien personenbezogener Daten und keine Beschäftigtendaten in CloudSuite Assist verarbeitet werden sollen. Praktisch finden sich in Tickets aber gelegentlich Krankheits- oder Urlaubsangaben von Ansprechpartnern, wenn Kunden Verzögerungen erklären. Ein Vertriebsleiter hat außerdem im April 2026 zwei Bewerberkontakte in CloudSuite als "potenzielle Sales-Kandidaten" angelegt. Das wurde am 14.05.2026 gelöscht und als Abweichung dokumentiert.

## 3. Datenkategorien

- Namen, geschäftliche E-Mail-Adressen, Telefonnummern.
- Funktion, Abteilung, Unternehmenszuordnung.
- Kommunikationsinhalte aus Supporttickets.
- Maschinenseriennummern und Wartungshistorie.
- Reklamationsgründe und Kulanzentscheidungen.
- Nutzungs- und Telemetriedaten der Plattform.
- Freitextfelder mit möglicher Fehlbefüllung.

## 4. Datenflüsse

1. Webanwendung: EU-Login über Frankfurt/Dublin.
2. Primäre Datenbank: Frankfurt am Main.
3. Backup: Dublin, 35 Tage rollierend.
4. 2nd-Level-Support: CloudSuite Assist Inc., USA, Zugriff im Ticketsystem nach Freigabe.
5. Telemetrie/Abuse Detection: Ereignisdaten an Virginia-Cluster, IP-Adresse gekürzt nach 24 Stunden.
6. ReplyPilot: Ticketauszug maximal 2.000 Zeichen an NorthPeak Analytics LLC; Anbieter behauptet "no training on customer prompts".

## 5. Anbieterzusagen

Aus Anbieter-Mail vom 03.04.2026:

> CloudSuite participates in the EU-U.S. Data Privacy Framework and provides the 2021 Standard Contractual Clauses as fallback for all enterprise customers.

Aus DPA Ziff. 8.4:

> International transfers are covered by the EU-U.S. Data Privacy Framework where applicable, and otherwise by the Standard Contractual Clauses, Module 2, incorporated by reference.

Problem: Die Order Form nennt CloudSuite Ireland Ltd.; der DPF-Hinweis nennt "CloudSuite"; der Security-Anhang nennt CloudSuite Assist Inc. als technischen Importeur. Der offizielle Scope wurde bei Vertragsschluss nicht archiviert.
