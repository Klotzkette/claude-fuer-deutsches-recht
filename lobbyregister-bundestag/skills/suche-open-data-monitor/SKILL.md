---
name: suche-open-data-monitor
description: "Nutzt Suche, Standardlisten, Open Data und API zur Markt-, Compliance- und Gegenparteienprüfung. Output Monitoring-Report im Lobbyregister Bundestag."
---

# Suche und Open-Data-Monitor

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 3 LobbyRG Eintragung vor erster Interessenvertretung, § 5 LobbyRG jährliche Aktualisierung, Berichtspflicht ggf. innerhalb 3 Monaten nach Ende des Geschäftsjahres.
- Tragende Normen verifizieren: LobbyRG §§ 1, 2, 3, 5, 6, 7, 8 (i.d.F. Reform 2024), Verhaltenskodex Lobbyregister, GOBT, BGleiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Interessenvertreter, Bundestagsverwaltung (Lobbyregisterstelle), Geschäftsstelle, registrierte Verbände, Bundesregierung (zweiter Registerteil).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lobbyregistereintrag, Verhaltenskodex-Bestätigung, Tätigkeitsbericht, Hausausweisantrag, Finanzangaben, Verbandsmitgliederliste — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

Nutze die offizielle API V2 nur als lesende Quelle für öffentliche Registerdaten. Fuer jede Abfrage:

1. API-Key ueber `LOBBYREGISTER_API_KEY` verwenden, nicht in die Akte schreiben.
2. `GET /registerentries?q=...&format=json` für Suche nach Organisationen, Zweigniederlassungen, Auftraggebern, Unterauftragnehmern, Themen und Schreibvarianten.
3. `GET /registerentries/{registerNumber}?format=json` für den amtlichen Einzelabgleich.
4. `GET /registerentries/{registerNumber}/{version}?format=json` für Versionsvergleich.
5. `GET /statistics/registerentries?format=json` für Datenstand und Monitoring-Kontext.
6. Cursor-Regel beachten: Folgeanfragen wiederholen, bis sich der Cursor nicht mehr aendert.
7. `sourceDate`, Suchparameter, Cursor, Registernummer, Version, `detailsPageUrl`, `pdfUrl` und Hash der Antwort dokumentieren.

Bei Zweigniederlassungen ist zwingend ein Suchlauf auf Rechtstraegername, Niederlassungsname, Sitzstaat, deutsche Adresse und Marken-/Kurzname auszugeben. Ein zweiter Treffer ist nicht automatisch Pflicht oder Fehler, sondern ein Streitpunkt für den Doppelregistrierungs-Check.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-für-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- API-Ausgaben werden nicht als Portal-Einreichung oder automatische Registeraenderung dargestellt.

