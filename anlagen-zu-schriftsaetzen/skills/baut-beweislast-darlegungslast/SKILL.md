---
name: baut-beweislast-darlegungslast
description: "Prüft, ob die Anlage eine konkrete Darlegung trägt oder nur einen pauschalen Anlagenverweis kaschiert; trennt Tatsachenvortrag, Beweisangebot und bloße Hintergrundunterlage."
---

# Beweislast, Darlegungslast und Anlagen

## Normenanker

Arbeitsfokus: **Beweislast, Darlegungslast und Anlagen**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 138 Abs. 1 ZPO` — vollständiger und wahrer Tatsachenvortrag.
- `§ 138 Abs. 2 ZPO` — Erklärungslast.
- `§ 253 Abs. 2 Nr. 2 ZPO` — bestimmter Klagegrund.
- `§ 284 ZPO` — Beweisaufnahme.
- `§ 371 Abs. 1 ZPO` — Augenschein.
- `§ 416 ZPO` — Beweiskraft privater Urkunden.
- `§ 420 ZPO` — Vorlegung durch Beweisführer.
- `§ 142 Abs. 1 ZPO` — Urkundenvorlegung durch Partei/Dritte.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Zweck

Dieser Skill macht die prozessuale Strenge sichtbar: Der Schriftsatz muss die erhebliche Tatsache enthalten. Die Anlage darf den Vortrag belegen, aber nicht ersetzen.

## Mindestinput

- Schriftsatzstelle.
- Anlagenzitat.
- Streitige Tatsache.

## Arbeitsablauf

1. Formuliere die behauptete Tatsache.
2. Prüfe, ob sie im Schriftsatz selbst steht.
3. Ordne die Anlage als Beleg, Erläuterung oder ungeeigneten Anlagenfriedhof ein.
4. Schlage eine bessere Schriftsatzformulierung vor.

## Ausgabe

- Substantiierungscheck.
- Korrekturbaustein.
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
