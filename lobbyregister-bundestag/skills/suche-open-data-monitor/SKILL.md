---
name: suche-open-data-monitor
description: "Nutzt Suche, Standardlisten, Open Data und API zur Markt-, Compliance- und Gegenparteienpruefung. Output Monitoring-Report."
---

# Suche und Open-Data-Monitor

## Einsatz

Oeffentliche Registerdaten fuer Due Diligence und Monitoring auswerten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Organisation, Branche, Registernummer oder Vorhaben sollen beobachtet werden?
2. Welche Suchfilter und Datenfelder sind relevant?
3. Welche Aenderungen muessen intern gemeldet werden?
4. Geht es um eigene Portal-Nachkontrolle, Gegenparteienpruefung, Dublettenrisiko oder Marktmonitoring?
5. Soll die Abfrage einmalig, periodisch oder als Cursor-gestuetzte Trefferliste laufen?

## API-V2-Arbeitsweise

Nutze die offizielle API V2 nur als lesende Quelle fuer oeffentliche Registerdaten. Fuer jede Abfrage:

1. API-Key ueber `LOBBYREGISTER_API_KEY` verwenden, nicht in die Akte schreiben.
2. `GET /registerentries?q=...&format=json` fuer Suche nach Organisationen, Zweigniederlassungen, Auftraggebern, Unterauftragnehmern, Themen und Schreibvarianten.
3. `GET /registerentries/{registerNumber}?format=json` fuer den amtlichen Einzelabgleich.
4. `GET /registerentries/{registerNumber}/{version}?format=json` fuer Versionsvergleich.
5. `GET /statistics/registerentries?format=json` fuer Datenstand und Monitoring-Kontext.
6. Cursor-Regel beachten: Folgeanfragen wiederholen, bis sich der Cursor nicht mehr aendert.
7. `sourceDate`, Suchparameter, Cursor, Registernummer, Version, `detailsPageUrl`, `pdfUrl` und Hash der Antwort dokumentieren.

Bei Zweigniederlassungen ist zwingend ein Suchlauf auf Rechtstraegername, Niederlassungsname, Sitzstaat, deutsche Adresse und Marken-/Kurzname auszugeben. Ein zweiter Treffer ist nicht automatisch Pflicht oder Fehler, sondern ein Streitpunkt fuer den Doppelregistrierungs-Check.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Monitoring-Report mit Suchprofil, API-Abfrageplan, Trefferliste, Cursor-Protokoll, Datenstand, Feldauffaelligkeiten, rechtlicher Bewertung und Folgeaktion.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- API-Ausgaben werden nicht als Portal-Einreichung oder automatische Registeraenderung dargestellt.
