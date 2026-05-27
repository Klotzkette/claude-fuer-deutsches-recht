---
name: erstregistrierung-ausfuellen
description: "Fuehrt Schritt fuer Schritt durch den Portal-Ersteintrag: Stammdaten, Personen, Taetigkeit, Finanzen, Vorhaben, Auftraege und Uploads. Output Eingabeplan."
---

# Erstregistrierung ausfuellen

## Einsatz

Aus Datenraum und Checklisten einen konkreten Portal-Eingabeplan machen.

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

Wenn die Nutzerin eine unselbststaendige Zweigniederlassung als eigene Organisation registrieren will, muss der Skill stoppen und nachfragen: Ist die Zweigniederlassung eigener Rechtstraeger oder nur Handelsregisterzweigstelle? Liegt eine ausdrueckliche Auskunft der registerfuehrenden Stelle vor? Ohne diese Klaerung nur den auslaendischen oder inlaendischen Rechtstraeger als Primaerentwurf ausgeben und die Niederlassung transparent im Eintrag abbilden.

## JSON-nahes Eingabemapping

Erzeuge neben dem Portal-Eingabeplan ein JSON-nahes Arbeitsmapping nach `assets/templates/registerdaten-json-mapping.md`. Das Mapping hilft, Pflichtfelder, Freigaben und den spaeteren API-Diff vorzubereiten. Es darf nicht als technische Einreichung, XML-Upload oder Portalersatz bezeichnet werden.

Fuer jedes Feld angeben:

- interne Quelle
- Portalabschnitt
- Freigabeperson
- Unsicherheiten
- erwartetes oeffentliches JSON-Feld nach Veroeffentlichung
- Nachkontrolle per API oder JSON-Download

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Eingabeplan mit Portalabschnitten, Copy-Texten, Anlagenliste, Freigaben, JSON-nahem Mapping, API-Nachkontrollplan und Stop-Punkten.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Die API wird nur als spaetere Kontrollquelle beschrieben, nicht als Einreichungsweg.
