---
name: bmftr-forschungsfoerderung
description: "Sachbereich Forschungsfoerderung und Ressortforschung im Geschaeftsbereich BMFTR: Normbestand (BHO; ANBest-P; SubvG; AGVO (Forschung); AGVO; Rahmenprogramm.); Akteure (BMFTR; Projekttraeger (PT; PT-DLR; PT Juelich); Ressortforschungseinrichtungen.); EU-Bezug (Horizon Europe; ERC; EIC; AGVO.); typ — Arbeitskontext: Legistik-Werkstatt (Gesetzgebung), Schwerpunkt bmftr forschungsfoerderung."
---

# Forschungsfoerderung und Ressortforschung (BMFTR)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass für das Spezialthema Forschungsfoerderung und Ressortforschung im Geschaeftsbereich BMFTR. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte für dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmftr`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmftr`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: BHO; ANBest-P; SubvG; AGVO (Forschung); AGVO; Rahmenprogramm.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BMFTR; Projekttraeger (PT; PT-DLR; PT Juelich); Ressortforschungseinrichtungen.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behörden im Vollzug; betroffene Länderbehoerden; Verbaende; wissenschaftliche Beiraete; zuständige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Horizon Europe; ERC; EIC; AGVO.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Foerderbekanntmachung; Antragsbearbeitung; Auswahlverfahren; Erfolgskontrolle; Verwertungsregeln; Open-Access.

Schrittfolge für den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Doppelfoerderung; Auslegung des Forschungsbegriffs; Auswertung; IP-Rechte.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Normenanker

Arbeitsfokus: **Forschungsfoerderung und Ressortforschung (BMFTR)**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmftr` -> `legw-ressortaufgaben-bmftr` -> `legw-bmftr-forschungsfoerderung-und-ressortforschung` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis für den Normgeber.
