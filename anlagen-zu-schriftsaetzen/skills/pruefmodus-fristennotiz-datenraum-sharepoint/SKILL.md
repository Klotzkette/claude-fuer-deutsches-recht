---
name: pruefmodus-fristennotiz-datenraum-sharepoint
description: "Validiert ein vorhandenes Anlagenpaket und gibt eine kurze Fristennotiz plus nächste Handlung aus im Anlagen zu Schriftsätzen: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Prüfmodus, Fristennotiz und nächster Schritt

## Arbeitsbereich

Validiert ein vorhandenes Anlagenpaket und gibt eine kurze Fristennotiz plus nächste Handlung aus. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Normenanker

Arbeitsfokus: **Prüfmodus, Fristennotiz und nächster Schritt**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — Schriftsatzanforderungen.
- `§ 130a Abs. 1 ZPO` — elektronisches Dokument.
- `§ 131 Abs. 1 ZPO` — Beifügung von Abschriften/Anlagen.
- `§ 133 Abs. 1 ZPO` — Abschriften für Zustellung.
- `§ 138 Abs. 1 ZPO` — Tatsachenvortrag.
- `§ 253 Abs. 2 ZPO` — Klageinhalt.
- `§ 299 Abs. 1 ZPO` — Akteneinsicht.
- `§ 371 Abs. 1 ZPO` — Augenschein.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieser Skill ist für fertige, aber verdächtige Pakete: einmal streng prüfen, dann sagen, was sofort zu tun ist.

## Mindestinput

- Fertiges Anlagenpaket.
- Schriftsatz.
- Frist.

## Arbeitsablauf

1. Vergleiche Zitate und Dateien.
2. Prüfe Nummern, Lesbarkeit, Schwärzung.
3. Formuliere Fristennotiz.

## Ausgabe

- Prüfbericht.
- Stop-Liste.
- Nächster Schritt.

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
