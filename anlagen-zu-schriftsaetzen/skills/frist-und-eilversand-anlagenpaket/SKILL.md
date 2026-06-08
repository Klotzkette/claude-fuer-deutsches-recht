---
name: frist-und-eilversand-anlagenpaket
description: "Minimalpfad bei drohender Frist: welche Anlagen müssen jetzt mit, welche können nachgereicht, welche Risiken müssen im Schriftsatz offen gehalten werden."
---

# Frist und Eilversand Anlagenpaket

## Normenanker

Arbeitsfokus: **Frist und Eilversand Anlagenpaket**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 294 Abs. 1 ZPO` — Glaubhaftmachung.
- `§ 920 Abs. 2 ZPO` — Verfügungsanspruch und Verfügungsgrund.
- `§ 936 ZPO` — Anwendung Arrestvorschriften auf einstweilige Verfügung.
- `§ 922 Abs. 2 ZPO` — Zustellung/Vollziehung Arrestbefehl.
- `§ 929 Abs. 2 ZPO` — Vollziehungsfrist.
- `§ 130a Abs. 1 ZPO` — elektronische Einreichung.
- `§ 371 ZPO` — Augenschein.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Zweck

Dieser Skill ist der nüchterne Notfallmodus. Er soll nicht alles perfekt machen, sondern die richtige Priorität setzen: fristwahrend, lesbar, nachvollziehbar, nachreichbar.

## Mindestinput

- Fristende.
- Schriftsatztyp.
- Vorhandene Kernanlagen.
- Was noch fehlt oder technisch kaputt ist.

## Arbeitsablauf

1. Bestimme Muss-Anlagen für Fristwahrung und Glaubhaftmachung.
2. Trenne Kür, Nachreichung und interne Kontrolle.
3. Formuliere Begleit-/Nachreichungshinweis.
4. Erstelle 30-Minuten- und 2-Stunden-Plan.

## Ausgabe

- Eilversandliste.
- Nachreichungsplan.
- Risikoampel.

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

## Vertiefter Anlagen-Workflow

Arbeite wie ein Schriftsatzteam kurz vor Versand: erst Ordnung schaffen, dann Beweisfunktion sichern, dann technische Einreichbarkeit prüfen.

1. **Materialkarte:** Jede Datei einer Tatsachenbehauptung, einem Schriftsatzabschnitt und einer Anlagenkategorie zuordnen. Dubletten, alte Fassungen, Screenshots ohne Datum und unleserliche Scans separat markieren.
2. **K1-Logik:** Nummerierung nicht nach Ordnerzufall, sondern nach Beweisgang: Vertrag/Grundlage, Kommunikation, Zahlung, Fristen/Zugang, Fotos/Screenshots, Tabellen, Behörden-/Gerichtsdokumente.
3. **Technikcheck:** PDF/A-Eignung, OCR, Seitenzählung, Dateigröße, Signatur-/beA-/ERVV-Kontext, Anlagenverzeichnis, Deckblatt und Dateinamen konsistent prüfen.
4. **Prozessrisiko:** Nichts Entscheidendes nur in der Anlage verstecken. Wenn eine Anlage eine tragende Tatsache beweist, muss der Schriftsatz diese Tatsache ausdrücklich behaupten und die Anlage präzise referenzieren.
5. **Versandpaket:** Am Ende eine Versandliste mit Paketname, Anlagenbereich, Seitenzahl, Hash/Version, Risikoampel und offener To-do-Liste erzeugen.

## Ergebnisqualität

- Gib immer eine sofort nutzbare Tabelle aus: Anlage, Quelle, Datum, Beweisfunktion, Schriftsatzstelle, technischer Status, Risiko.
- Weise auf fehlende Lesbarkeit, fehlenden Zugangsnachweis, fehlende Übersetzung und fehlende Vollständigkeit ausdrücklich hin.
- Bei elektronischem Rechtsverkehr keine Mutmaßung: aktuelle ZPO/BRAO/ERVV/ERVB-Quelle oder gerichtliche Verfügung prüfen, bevor formale Aussagen final werden.
