# Transferregister und VVT-Auszug

Organisation: RheinMain Präzisionstechnik GmbH
Verarbeitungstätigkeit: CRM, Support und Ersatzteilservice CloudSuite Assist
Stand: 18.05.2026

## Verarbeitungstätigkeit

| Feld | Eintrag |
|---|---|
| Verantwortlicher | RheinMain Präzisionstechnik GmbH, Frankfurt am Main |
| Fachbereich | Vertrieb, Customer Service, Ersatzteilmanagement |
| System | CloudSuite Assist, Modul CRM, TicketDesk, ReplyPilot |
| Zweck | Kundenkommunikation, Supportbearbeitung, Ersatzteilkoordination, Antwortvorschläge |
| Rechtsgrundlage | Art. 6 Abs. 1 lit. b DSGVO bei Vertragskontakten; Art. 6 Abs. 1 lit. f DSGVO bei B2B-Ansprechpartnern und Serviceorganisation |
| Betroffene | Kundenkontakte, Lieferantenkontakte, Interessenten, gelegentlich interne Ansprechpartner |
| Datenarten | Kontaktdaten, Kommunikationsinhalte, Supporthistorie, Maschinenbezug, Ticketmetadaten |
| Löschfrist | Kontaktstammdaten 3 Jahre nach letztem Geschäftskontakt; Supporttickets 6 Jahre, soweit handels-/steuerrechtlich relevant; Telemetrie 180 Tage |
| Empfänger | CloudSuite Ireland Ltd., CloudSuite Assist Inc., MainRack GmbH, NorthPeak Analytics LLC |

## Drittlandtransfermatrix

| Datenfluss | Drittlandbezug | Datenarten | Transferinstrument | Status |
|---|---|---|---|---|
| 2nd-Level-Support CloudSuite Assist Inc. | Zugriff aus USA auf EU-Tickets | Ticketinhalte, Kontaktdaten, Systemlogs | DPF + SCC Modul 2 Backup | Gelb, Scope prüfen |
| Telemetrie Virginia-Cluster | Übermittlung in USA | Loginmetadaten, Eventlogs, gekürzte IP nach 24h | SCC Modul 2 + TIA | Gelb |
| ReplyPilot an NorthPeak Analytics LLC | Übermittlung in USA | Ticketauszug bis 2.000 Zeichen | SCC noch unvollständig, TIA erforderlich | Rot bis Nachtrag |
| Subprozessor TicketForge LLC | USA, nur Notfall-Wartung | Fehlerlog, Ticket-ID | DPF behauptet, Nachweis offen | Gelb/Rot |

## Schutzbedarfsnotiz

Die regulären Daten sind überwiegend B2B-Kommunikationsdaten. Das Risiko steigt durch Freitextfelder, weil Kundinnen und Kunden ungefragt private Informationen, Krankheitsangaben oder personenbezogene Eskalationsdetails mitteilen können. Deshalb muss der Transfer nicht nur nach Tabellenfeldern, sondern nach realistischen Ticketinhalten bewertet werden.
