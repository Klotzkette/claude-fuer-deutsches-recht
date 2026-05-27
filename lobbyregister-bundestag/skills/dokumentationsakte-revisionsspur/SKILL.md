---
name: dokumentationsakte-revisionsspur
description: "Baut Aktenstruktur fuer Belege, Freigaben, Portal-Screenshots, Kontaktlogs, Kostenmethodik, RfS-Kommunikation und Jahresupdates. Output Aktenplan."
---

# Dokumentationsakte und Revisionsspur

## Einsatz

Die Registerarbeit spaeter nachvollziehbar beweisen koennen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Belege liegen wo?
2. Welche Entscheidungen wurden von wem freigegeben?
3. Welche Portalaktionen muessen dokumentiert werden?
4. Welche API- oder JSON-Exportantworten belegen den oeffentlichen Datenstand?

## API-Revisionsspur

Fuer jeden API- oder JSON-Export muss die Akte enthalten:

- Abrufdatum und `sourceDate`
- verwendeter Endpunkt, Suchparameter und Cursor
- Registernummer, Version, `detailsPageUrl` und `pdfUrl`
- Hash oder unveraenderte Rohdatei
- Bearbeiterin/Bearbeiter
- Zweck der Abfrage
- Verweis auf den dazugehoerigen Portalvorgang oder Monitoringlauf
- Bewertung, ob eine Abweichung rechtlich, technisch oder nur formal ist

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Aktenplan mit Ordnerstruktur, Namensschema, Mindestbelegen, API-Rohdatenablage, Aufbewahrung und Pruefspur.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- API-Antworten werden unveraendert archiviert und nicht mit internen Arbeitshypothesen vermischt.
