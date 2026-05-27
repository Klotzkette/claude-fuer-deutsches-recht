---
name: regelungsvorhaben-erfassen
description: "Erfasst konkrete aktuelle, geplante oder angestrebte Regelungsvorhaben, auch ohne vorhandenen Referentenentwurf oder Drucksache. Output Regelungsvorhaben-Karte."
---

# Regelungsvorhaben erfassen

## Einsatz

Regelungsvorhaben so konkret eintragen, dass der Einflussgegenstand transparent wird.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche rechtliche Regelung soll eingefuehrt, geaendert, beibehalten oder verhindert werden?
2. Gibt es Referentenentwurf, Drucksache oder bekannte Initiative?
3. Wann steht die erste Kontaktaufnahme dazu bevor?
4. Wie soll das Vorhaben spaeter im oeffentlichen JSON/API-Export wiedergefunden werden?

## API-Suchfaehigkeit

Formuliere Regelungsvorhaben so, dass sie sowohl im Portal als auch spaeter in API/API-Export nachvollziehbar sind: sprechender Titel, Bezug zu Gesetz, Verordnung oder politischer Initiative, keine zu breiten Sammelbegriffe, konsistente Schreibweisen. Fuer Monitoring Suchbegriffe, Varianten und erwartete JSON-Felder `regulatoryProjects` und `statements` notieren.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Regelungsvorhaben-Karte mit Titel, Ziel, Bezug, Dokumentenlinks, Kontaktstart, Updatepflicht und API-Suchprofil.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
