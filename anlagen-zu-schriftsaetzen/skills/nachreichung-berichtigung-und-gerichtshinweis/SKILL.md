---
name: nachreichung-berichtigung-und-gerichtshinweis
description: "Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung."
---

# Nachreichung, Berichtigung und gerichtlicher Hinweis

## Normenanker

Arbeitsfokus: **Nachreichung, Berichtigung und gerichtlicher Hinweis**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 520 Abs. 3 ZPO` — Berufungsbegründung.
- `§ 529 Abs. 1 ZPO` — Tatsachengrundlage Berufung.
- `§ 531 Abs. 2 ZPO` — neue Angriffs- und Verteidigungsmittel.
- `§ 522 ZPO` — Berufungszurückweisung.
- `§ 130a Abs. 1 ZPO` — elektronische Einreichung.
- `§ 296 ZPO` — Zurückweisung verspäteten Vorbringens.
- `§ 139 ZPO` — gerichtlicher Hinweis.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Zweck

Dieser Skill ist die Feuerwehr, wenn das Paket schon draußen ist. Er hält Nummern stabil, korrigiert transparent und vermeidet, dass aus einer kleinen Anlagenpanne ein prozessuales Glaubwürdigkeitsproblem wird.

## Mindestinput

- Hinweis/Rüge/Problem.
- Bisheriger Schriftsatz und Anlagenverzeichnis.
- Welche Datei falsch, fehlend oder unleserlich ist.
- Frist für Berichtigung/Nachreichung.

## Arbeitsablauf

1. Klassifiziere Problem: fehlt, falsch, doppelt, unleserlich, geheim, falsche Fassung.
2. Entscheide, ob Nummer beibehalten, ersetzt oder als Nachtrag ergänzt wird.
3. Formuliere Berichtigungs-/Nachreichungsvermerk.
4. Erstelle neue Kontrollliste und Versandplan.

## Ausgabe

- Reparaturplan.
- Berichtigungsschriftsatz-Baustein.
- Nachreichungsverzeichnis.

## Typische Fehler, die du aktiv suchst

- Unklare Anlagenfunktion: Die Datei existiert, aber niemand sagt, welche Tatsache sie beweist.
- Nummerierung folgt dem Ordner, nicht dem Schriftsatz.
- Der Schriftsatz versteckt entscheidenden Vortrag in der Anlage.
- Dateiname, Stempel oder Anlagenverzeichnis widersprechen einander.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.
