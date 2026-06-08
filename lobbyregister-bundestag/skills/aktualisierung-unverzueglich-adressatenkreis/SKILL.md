---
name: aktualisierung-unverzueglich-adressatenkreis
description: "Steuert unverzuegliche Updates bei Stammdaten, Personen, Tätigkeitsbeschreibung, Vorhabenbereichen, Regelungsvorhaben, Auftraegen und Auftraggebern. Output Update-Ticket im Lobbyregister Bundestag."
---

# Unverzuegliche Aktualisierung

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

1. Welche Angabe hat sich wann geaendert?
2. Ist die Aenderung registerrelevant?
3. Wer muss Text, Beleg und Freigabe liefern?
4. Welche veroeffentlichten API-Felder muessen nach der Portalaktion kontrolliert werden?

## API-Nachkontrolle

Nach einer Portalaktualisierung soll der Skill eine Wiedervorlage für den öffentlichen API-Abgleich anlegen:

1. Vorherige API-Antwort oder PDF-Version aus der Akte ziehen.
2. Nach Veroeffentlichung `GET /registerentries/{registerNumber}?format=json` abrufen.
3. Wenn die Version geaendert wurde, alte und neue Version gegenueberstellen.
4. `lastUpdateDate`, `validFromDate`, `fiscalYearUpdate.updateMissing`, `refusedAnything`, Regelungsvorhaben, Stellungnahmen, Personen und Finanzdaten pruefen.
5. Abweichungen in `assets/templates/registerexport-diff.md` dokumentieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 LobbyRG
- § 5 LobbyRG
- § 2 LobbyRG
- § 4 LobbyRG
- § 1 LobbyRG
- § 7 LobbyRG
- § 6 LobbyRG
- § 1 GeschGehG
- Art. 21 GG
- § 28 VwVfG
- § 1 bis 7 LobbyRG
- § 6b BMinG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

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
- Nach der Veroeffentlichung wird die API-Antwort als Beleg gesichert oder die fehlende Veroeffentlichung eskaliert.

