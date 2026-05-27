---
name: stellungnahmen-gutachten-upload
description: "Prueft Bereitstellungspflicht fuer grundlegende Stellungnahmen oder Gutachten zu Regelungsvorhaben und Quartalsfrist. Norm § 3 LobbyRG. Output Upload-Log."
---

# Stellungnahmen und Gutachten Upload

## Einsatz

Entscheiden, welche Dokumente in den Bereich Inhalte der Interessenvertretung gehoeren.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wurde ein Dokument an Bundestags- oder Regierungsadressaten gegeben?
2. Ist es grundlegend oder nur Begleitkommunikation?
3. In welchem Quartal wurde es versandt?
4. Wie wird nach dem Upload geprueft, dass Dokument, Regelungsvorhaben und Version oeffentlich richtig erscheinen?

## API-Nachweis nach Upload

Nach dem Portal-Upload soll der Skill eine Nachkontrolle anlegen: oeffentlichen Eintrag per API abrufen, `statements`, `regulatoryProjects`, Version, `sourceDate`, Detailseite und PDF sichern und gegen Versanddatum, Empfaengerkreis, Regelungsvorhaben und Schwärzungsvermerk pruefen. Die API prueft nur den veroeffentlichten Datenstand; sie ersetzt den Portal-Upload nicht.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Upload-Log mit Dokumenttitel, Regelungsvorhaben, Versanddatum, Quartalsfrist, Schwärzungsbedarf und API-Nachweis.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
