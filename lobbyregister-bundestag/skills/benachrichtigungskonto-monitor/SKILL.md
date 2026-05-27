---
name: benachrichtigungskonto-monitor
description: "Richtet Beobachtung von Registereintraegen, Aktualisierungen und Entwicklungen ueber das Benachrichtigungskonto ein. Output Watchlist."
---

# Benachrichtigungskonto Monitor

## Einsatz

Automatisierte Benachrichtigungen in Compliance- oder Wettbewerbsmonitoring einbauen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Registereintraege oder Themen sollen beobachtet werden?
2. Wer erhaelt Benachrichtigungen?
3. Wie werden Alerts bewertet und dokumentiert?
4. Welche API-Abfrage bildet die gleiche Watchlist maschinenlesbar ab?

## Benachrichtigungskonto und API

Das Benachrichtigungskonto ist die fachliche Watchlist im Lobbyregisterumfeld. Die API ist die technische Kontrollspur. Der Skill soll beide Ebenen trennen:

- Benachrichtigungskonto: Empfaenger, Suchprofil, fachliche Bewertung, Eskalation.
- API-Monitor: Endpunkt, Suchparameter, Cursor, `sourceDate`, Registernummern, Versionswechsel, Diff.
- Revisionsspur: Alert, API-Antwort, interne Bewertung und Portalaktion werden zusammen abgelegt.

Bei eigenen Eintraegen ist ein Alert nur vollstaendig bearbeitet, wenn der oeffentliche API-Datenstand mit der internen Freigabeakte verglichen wurde.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Watchlist mit Suchprofilen, Empfaengern, API-Monitoringplan, Bewertungsschema, Revisionsspur und Eskalation.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Alertdaten und API-Daten werden sauber als getrennte Belege benannt.
