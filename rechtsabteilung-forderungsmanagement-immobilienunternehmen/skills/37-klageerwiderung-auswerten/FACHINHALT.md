---
name: 37-klageerwiderung-auswerten
description: "Neue Klageerwiderung, Gerichtspost oder gegnerischen Schriftsatz im laufenden Prozess als Delta auswerten. Frist, Einwendungen, Zahlung nach Klage, Aufrechnung, Kostenpfad, Beweisrisiken und überholte Prozesspositionen extrahieren. Output Prozess- und Änderungskarte."
---

# Klageerwiderung auswerten

## Zweck und Anwendungsfall

Dieser Skill startet die prozessuale Reaktionsphase in der eigenen laufenden Vermieterklage, sobald eine Klageerwiderung, ein gegnerischer Schriftsatz oder ein gerichtlicher Hinweis eingeht. Außergerichtliche Mieterverein- oder Anwaltsschreiben führt Skill 43. Wenn der Mieter selbst Kläger ist oder Widerklage erhebt, führt Skill 42.

## Bedienmodus

Arbeite für hochtrainierte Rechtsanwalts- und Notarfachangestellte, Renofas, Rechtsfachwirt:innen und Forderungsmanagement-Spezialist:innen. Sie sind keine Anwälte, aber fachlich stark. Keine abgehobene Anwaltsprosa: kurze Arbeitskarten, begründete Prüffragen, kompakte Tabellen, Ampel, Lückenliste und genau eine nächste Arbeitsaktion. Juristisch schwierige Punkte werden als Eskalation markiert, nicht versteckt.

## Eingaben

- Klageerwiderung, gegnerischer Prozessschriftsatz oder gerichtlicher Hinweis.
- Eigene Klage, Anlagen und Belegmatrix.
- Gerichtliche Verfügung mit Frist.
- Bisherige Prozesskarte, letzter Schriftsatzstand und Chronologie, soweit vorhanden.

## Ablauf / Checkliste

1. Frist und gerichtliche Hinweise sofort erfassen.
2. Einwendungen in Kategorien einteilen: Zahlung, Zahlung nach Klageeinreichung, Aufrechnung, dauernde Einrede, Unmöglichkeit, Wegfall Rechtsschutzbedürfnis, Minderung, Zurückbehaltung, Form, Zustellung, Verjährung, Sozialhärte.
3. Bestreiten bestimmen: einfach, substantiiert, pauschal.
4. Beweisangebote der Gegenseite erfassen.
5. Eigene Belege und Nachweise zuordnen.
6. Replikplan für Skill `38-replik-erstellen` erstellen.
7. Gerichtliche Frist mit Ablaufdatum, interner Vorfrist und verantwortlicher Person ausgeben.
8. Neue Tatsachen, unstreitige Punkte und Anerkenntnis-/Erledigungsrisiken getrennt markieren.
9. Bei erledigendem Ereignis zusätzlich Kostenpfad-Matrix erstellen: Ereignis, Datum, vor/nach Rechtshängigkeit, vollständig/teilweise, einseitig/übereinstimmend, Vorverzug, Forderungsstatus bei Einreichung, Wertstellung/Buchung, damaliger Kenntnisstand, Kausalität und Erforderlichkeit der Kosten, Paragraf 91a ZPO, Paragraf 269 Abs. 3 S. 3 ZPO, materiell-rechtliche Kostenerstattung und RA-Eskalation.
10. Bei offener Beweisfrage oder unklarem Sachstand keine Kostenaufhebung riskieren, ohne das Risiko ausdrücklich zu markieren. BGH III ZR 156/12 ist geprüfter Anker für das Wahlrecht zur materiellen Kostenerstattungsklage bei Erledigung vor Rechtshängigkeit. BGH VIII ZB 39/24 ist geprüfter Anker dafür, dass Paragraf 91a ZPO nur summarisch prüft und schwierige Rechtsfragen offenlassen kann. Eine konkrete Klageänderung, Kostenerstattungsklage oder Feststellungslösung stets mit live verifiziertem Volltext und RA-Freigabe bearbeiten.
11. Bei Minderungs- oder Mängeleinwand den Darlegungsmaßstab aus BGH VIII ZR 155/11 anwenden: konkrete Erscheinungsform, Zeitraum und Gebrauchsbeeinträchtigung erfassen. Technische Ursache, exakter Beeinträchtigungsgrad und eine bestimmte Minderungsquote sind keine generellen Substantiierungsvoraussetzungen. Erst danach Beweis- und Gegenbeweisbedarf bestimmen.
12. Abgrenzung prüfen: Nur bei Widerklage, eigener Mieterklage oder konkreter Klageandrohung Skill 42 laden; bloße Minderung, Schimmelbehauptung oder Zahlungseinwendung in der eigenen Klage bleibt in Skill 37 und geht danach zu Skill 38, 39 oder 45.
13. Erste Ausgabe als Prozesskarte liefern: Frist, Vorfrist, Kerneinwendungen, rote Risiken, Replikfähigkeit und nächster Skill.
14. Rückfragen trennen: Tatsachenrückfrage an Hausverwaltung, Belegfrage an DMS/Buchhaltung, Rechtsfrage an Skill 08. Maximal drei Rückfragen gleichzeitig.
15. Bei vorhandener Prozesskarte nur den neuen Schriftsatz oder Hinweis gegen den letzten Stand vergleichen. Neue unstreitige Tatsachen, geänderten Saldo, neue Frist und entwertete Antwortlinie ausdrücklich markieren.
16. Frühere Replik- oder Antragsentwürfe nicht still fortverwenden. Änderungskarte mit Stichtag alt/neu, überholten Passagen und genau einem Folgeskill anlegen.

## Argumentationsstandard

Für jeden gegnerischen Angriff entsteht eine Antwortzeile: genaue Fundstelle, Tatsachenbehauptung, Prozessstatus, eigene Erkenntnis, Beweislast, eigener Beleg, einschlägige Norm, vorgeschlagene Antwort und Auswirkung auf Antrag oder Kosten. Einfaches, substantiiertes und zulässiges Nichtwissen werden nicht nach Tonfall, sondern nach § 138 ZPO und der Dichte des Ausgangsvortrags eingeordnet. Die Arbeitsweise folgt `references/schriftsatz-und-argumentationsstandard.md`.

## Quellenpflicht

Es gilt die Zitierweise nach `references/zitierweise.md` (Rechtsprechung vor Literatur, neueste zuerst); Leitentscheidungen werden über `references/leitentscheidungen-anker.md` als Sucheinstieg gewählt und vor Verwendung in einer freien amtlichen Quelle live verifiziert. Für Prozesskosten nach erledigendem Ereignis und mietrechtliche Kernlinien `references/gepruefte-bgh-anker-mietrecht.md` nutzen.

ZPO-Vortrag, Beweislast und materielles Mietrecht mit Normanker. Keine erfundenen Rechtsprechungszitate. Für Bedienführung und Übergaben `references/bedienfuehrung-workflows.md` nutzen.

## Ausgabeformat

Prozesskarte, Änderungskarte und Erwiderungsmatrix mit Randnummer, gegnerischem Vortrag, Kategorie, Relevanz, Antwortlinie, Beweis, Frist, Risiko, Kostenpfad, überholtem Arbeitsstand, Rückfragen und nächstem Arbeitsschritt. Saubere Sätze, keine Stichwort-Endprodukte.

## Beispiele

- Mieter behauptet in der eigenen Zahlungsklage Schimmel: in Skill 37 auswerten, dann Skill 38 für Replik, Skill 39 für Beweisplan und Skill 45 für Hausverwaltungsbelege.
- Mieter bestreitet Mietkonto pauschal: Anlagenplan nachschärfen.
- Mieter zahlt nach Klageeinreichung und behauptet Erledigung: Kostenpfad-Matrix vor Replik oder Erledigungserklärung.
