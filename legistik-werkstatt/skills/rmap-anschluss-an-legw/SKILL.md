---
name: rmap-anschluss-an-legw
description: "Brueckenskill: Wie verzahnt sich die Rulemap-Arbeit mit der uebrigen Legistik-Werkstatt (Auftragsaufnahme; Ressort-Router; Heranfuehrung; Ressortaufgaben; Sachfeld-Spezialfelder; normhierarchie-routing; verfassungsmaessigkeit-quercheck; europarechtskonformitaet; folgenabschaetzung). Output Kettenpfad mit Eingaben; Ausgaben; Verantwortlichkeiten je Stufe. Abgrenzung zur fachlichen Modellierung selbst; hier wird die Werkstattkette beschrieben im Legistik: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt

## Arbeitsbereich

Brueckenskill: Wie verzahnt sich die Rulemap-Arbeit mit der uebrigen Legistik-Werkstatt (Auftragsaufnahme; Ressort-Router; Heranfuehrung; Ressortaufgaben; Sachfeld-Spezialfelder; normhierarchie-routing; verfassungsmaessigkeit-quercheck; europarechtskonformitaet; folgenabschaetzung). Output Kettenpfad mit Eingaben; Ausgaben; Verantwortlichkeiten je Stufe. Abgrenzung zur fachlichen Modellierung selbst; hier wird die Werkstattkette beschrieben. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Normenanker

Arbeitsfokus: **Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

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

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GGO Ressortbeteiligung i.d.R. 4 Wochen, NKR-Stellungnahme 4 Wochen, Bundesrat 1. Durchgang 6 Wochen / 9 Wochen, Vermittlungsausschuss nach Bedarf.
- Tragende Normen verifizieren: GGO §§ 40-49 (Rechtsetzungsverfahren), Handbuch der Rechtsförmlichkeit (BMJ), NKR-Gesetz, BGleiG, IT-Konsolidierungs-Konzept, eNorm-Standard, GG Art. 76, 77, 78 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Ressort (BMJ und Fachressort), Bundeskanzleramt, Bundesrat, NKR, Bundestagsausschüsse, Bundesregierung, Wissenschaftliche Dienste, Lobbyregister.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Referentenentwurf, BT-Drucksache, Gesetzesfolgenabschätzung, NKR-Stellungnahme, Verbändeanhörungs-Stellungnahme, Synopse, Erfüllungsaufwandsberechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Auftragsblatt aus legistik-auftragsaufnahme
- Ergebnis aus legw-ressort-router
- Sachfeld-Kompass aus legw-<ressort>-<thema>

## Kern der Methode

Die Rulemap-Skills bilden eine eigene Subkette; sie werden nach der Ressort- und Sachfeld-Klaerung in das Werkstatt-eingehaengt. Die Quercheckskills (verfassungsmaessigkeit; europarechtskonformitaet) wirken weiter; die rmap-Skills liefern zusaetzlich die maschinenlesbare Fassung.

## Vorgehen

1. Auftragsblatt um Rulemap-Erfordernis ergaenzen
2. Nach Sachfeld-Kompass legw-rmap-grundlagen anstossen
3. Vorgehensmodell aus legw-rmap-norm-zu-rulemap durchlaufen
4. Quercheckskills (verfassungs- und europarechtlich) parallel arbeiten lassen
5. Rulemap mit Begruendung; NKR-Bericht und Vollzugsplan zusammenfuehren
6. Akte schliessen; Builder-Export ablegen

## Pruefpunkte

Pruefen: ist die Werkstattkette vollstaendig durchlaufen? Sind Querprueferei und Rulemap-Erstellung sauber verzahnt? Liegt am Ende ein Aktenstand mit Text- und Logikfassung der Norm vor?

## Output

```
Skill: legw-rmap-anschluss-an-legw
Thema: Anschluss der Rulemap-Arbeit an die Legistik-Werkstatt
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur für Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
