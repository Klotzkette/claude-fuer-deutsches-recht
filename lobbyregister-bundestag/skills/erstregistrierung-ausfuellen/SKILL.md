---
name: erstregistrierung-ausfuellen
description: "Führt Schritt für Schritt durch den Portal-Ersteintrag: Stammdaten, Personen, Tätigkeit, Finanzen, Vorhaben, Auftraege und Uploads. Output Eingabeplan im Lobbyregister Bundestag."
---

# Erstregistrierung ausfuellen

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

1. Sind alle Pflichtfelder und Nachweise vorhanden?
2. Welche Angaben sind noch unsicher?
3. Welche Texte muessen vor Eintragung intern freigegeben werden?

## Quellenanker

## Stop-Regel bei Zweigniederlassungen

Wenn die Nutzerin eine unselbststaendige Zweigniederlassung als eigene Organisation registrieren will, muss der Skill stoppen und nachfragen: Ist die Zweigniederlassung eigener Rechtstraeger oder nur Handelsregisterzweigstelle? Liegt eine ausdrueckliche Auskunft der registerfuehrenden Stelle vor? Ohne diese Klaerung nur den ausländischen oder inlaendischen Rechtstraeger als Primaerentwurf ausgeben und die Niederlassung transparent im Eintrag abbilden.

## JSON-nahes Eingabemapping

Erzeuge neben dem Portal-Eingabeplan ein JSON-nahes Arbeitsmapping nach `assets/templates/registerdaten-json-mapping.md`. Das Mapping hilft, Pflichtfelder, Freigaben und den spaeteren API-Diff vorzubereiten. Es darf nicht als technische Einreichung, XML-Upload oder Portalersatz bezeichnet werden.

Fuer jedes Feld angeben:

- interne Quelle
- Portalabschnitt
- Freigabeperson
- Unsicherheiten
- erwartetes öffentliches JSON-Feld nach Veroeffentlichung
- Nachkontrolle per API oder JSON-Download

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
- Die API wird nur als spaetere Kontrollquelle beschrieben, nicht als Einreichungsweg.

