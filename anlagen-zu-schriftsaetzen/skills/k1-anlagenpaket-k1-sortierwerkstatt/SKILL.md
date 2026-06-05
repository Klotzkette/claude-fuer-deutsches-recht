---
name: k1-anlagenpaket-k1-sortierwerkstatt
description: "K1 Anlagenpaket K1 Sortierwerkstatt: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# K1 Anlagenpaket K1 Sortierwerkstatt

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **K1 Anlagenpaket K1 Sortierwerkstatt** im Plugin Anlagen zu Schriftsätzen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `k1-anlagenpaket-aus-chaosordner` | Aus einem Mandantenordner mit beliebigen Dateinamen die erste Anlagenstaffel K1 bis K20 bilden: priorisieren, umbenennen, Lücken markieren, Rückfragen ausgeben. |
| `k1-sortierwerkstatt` | K1-Leitanlage sortieren: Vertrag, Auftrag, Nachtrag, E-Mail-Anhang, Scan, OCR-Fassung und spätere Ergänzungen zu einer gerichtstauglichen Anlage K1 oder einem K1-Konvolut ordnen. |
| `massenanlagen-sampling-und-repraesentativitaet` | Hilft bei Tausenden gleichartiger Dokumente: Auswahl, repräsentative Beispiele, Nachreichungsvorbehalt, Anlagenband und Substantiierungsgrenze. |
| `mehrparteien-rollen-und-praefixe` | Entwirft Nummernkreise bei Streitgenossen, Nebenintervention, Widerklage, Drittwiderklage, selbständigem Beweisverfahren und parallelen Verfahren. |

## Arbeitsweg

Im Plugin Anlagen zu Schriftsätzen gilt für **K1 Anlagenpaket K1 Sortierwerkstatt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `k1-anlagenpaket-aus-chaosordner`

**Fokus:** Aus einem Mandantenordner mit beliebigen Dateinamen die erste Anlagenstaffel K1 bis K20 bilden: priorisieren, umbenennen, Lücken markieren, Rückfragen ausgeben.

# K1 aus Chaosordner bauen

## Zweck

Dieser Skill ist für den Moment gedacht, in dem ein Mandant einen ZIP-Ordner mit „final_final_neu.pdf“, Screenshots, Tabellen und E-Mail-Anhängen sendet und in 90 Minuten eine brauchbare Anlagenstaffel entstehen muss.

## Mindestinput

- Ordnerliste oder Dateiexport.
- Schriftsatzentwurf oder wenigstens Anspruchs-/Verteidigungslinie.
- Nummernkreis und gewünschte Tiefe der Staffel.

## Arbeitsablauf

1. Dateien grob clustern: Vertrag, Leistung, Abnahme, Rechnung, Mahnung, Mangel, Korrespondenz, Zahlung.
2. Doppelte und bloße technische Kopien aussondern.
3. Für jede potentielle K-Anlage Beweiszweck und Schriftsatzstelle bestimmen.
4. K1 bis K20 als erste arbeitsfähige Staffel vorschlagen.
5. Nicht zuordenbare Dateien in Nachforderungs-/Klärliste schieben.

## Ausgabe

- K1-K20-Vorschlagsliste.
- Dateinamensvorschläge.
- Nicht verwendete Dateien mit Grund.
- Eine einzige priorisierte Rückfrage, wenn nötig.

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

## 2. `k1-sortierwerkstatt`

**Fokus:** K1-Leitanlage sortieren: Vertrag, Auftrag, Nachtrag, E-Mail-Anhang, Scan, OCR-Fassung und spätere Ergänzungen zu einer gerichtstauglichen Anlage K1 oder einem K1-Konvolut ordnen.

# K1-Sortierwerkstatt

## Zweck

Dieser Skill entscheidet, was bei einer großen Akte wirklich `Anlage K1` sein soll. Er verhindert, dass die wichtigste Anlage aus fünf Fassungen, einem schlechten Scan und einer halb vergessenen Bestätigungsmail besteht, ohne dass Gericht oder Gegner verstehen, welche Fassung maßgeblich ist.

## Mindestinput

- Ziel-Schriftsatz und Parteirolle.
- Alle potentiellen K1-Dateien mit Dateinamen, Datum, Quelle und kurzer Inhaltsbeschreibung.
- Angabe, welche Tatsachenbehauptung K1 beweisen soll.
- Hinweis, ob Einzelanlage oder Konvolut gewünscht ist.

## Arbeitsablauf

1. Bestimme den Beweiszweck von K1 in einem Satz.
2. Trenne gerichtliche Fassung, bloße Vorversion, E-Mail-Transporthülle, OCR-Arbeitsfassung und interne Notiz.
3. Entscheide Einzelanlage oder Konvolut; bei Konvolut Reihenfolge und Untergliederung festlegen.
4. Formuliere einen Schriftsatzanker, der K1 im Vortrag sauber einführt.
5. Erzeuge Dateinamen, Deckblatttext, Anlagenverzeichniszeile und interne Versionennotiz.

## Ausgabe

- K1-Entscheidung mit kurzer Begründung.
- Deckblatt für `Anlage K1` oder `K1-Konvolut`.
- Tabelle: Datei, Rolle, Status, gerichtliche Fassung ja/nein.
- Schriftsatzbaustein zur Einführung der Anlage.

## Typische Fehler, die du aktiv suchst

- K1 enthält mehrere Dokumente ohne gemeinsamen Beweiszweck.
- Unterschriebene Fassung und Entwurf werden verwechselt.
- Scan und OCR-Fassung werden als zwei verschiedene Anlagen gezählt.
- Der Schriftsatz zitiert nur K1, braucht aber K1.3.

## Anschluss-Skills

- `anlagen-zu-schriftsaetzen` für den Hauptworkflow.
- `anlagen-qualitygate-finalcheck` vor Versand.
- `schriftsatz-anlagen-mapping` für Belegmatrix und Lückenliste.

## Quellen- und Vorsichtsregel

Bei tragenden Aussagen zu Form, elektronischer Einreichung oder prozessualer Verwertbarkeit aktuelle amtliche Quellen prüfen: ZPO, BRAO, ERVV, ERVB und gerichtliche Hinweise. Keine BeckRS-/juris-/Literatur-Blindzitate. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle nennen.

## 3. `massenanlagen-sampling-und-repraesentativitaet`

**Fokus:** Hilft bei Tausenden gleichartiger Dokumente: Auswahl, repräsentative Beispiele, Nachreichungsvorbehalt, Anlagenband und Substantiierungsgrenze.

# Massenanlagen, Sampling und Repräsentativität

## Zweck

Dieser Skill ist für Massendokumente: Lieferscheine, Bautagebücher, Einzelrechnungen, Logfiles, Tickets. Er sucht eine faire Balance zwischen vollständigem Vortrag und unlesbarem Anlagenfriedhof.

## Mindestinput

- Masse und Dokumenttyp.
- Streitige Tatsachen.
- Vorhandene Auswertung oder Statistik.

## Arbeitsablauf

1. Trenne Vollbeleg, Beispielbeleg und bloße Dokumentation.
2. Bestimme Repräsentativität und Auswahlkriterien.
3. Prüfe, ob Tabellenzusammenfassung plus Stichprobe genügt.
4. Plane Nachreichungs-/Vorlagebereitschaft.

## Ausgabe

- Sampling-Konzept.
- Anlagenband-Struktur.
- Schriftsatzbaustein zur Repräsentativität.

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

## 4. `mehrparteien-rollen-und-praefixe`

**Fokus:** Entwirft Nummernkreise bei Streitgenossen, Nebenintervention, Widerklage, Drittwiderklage, selbständigem Beweisverfahren und parallelen Verfahren.

# Mehrparteien, Rollen und Präfixe

## Zweck

Dieser Skill verhindert Prefix-Chaos: K, B, WK, DWK, NI, SV, AST, AG, BK, BB, S-W. Er sorgt dafür, dass die Nummerierung der Prozessrolle folgt.

## Mindestinput

- Parteien-/Rollenübersicht.
- Verfahrensarten.
- Vorhandene Nummernkreise.

## Arbeitsablauf

1. Bestimme pro Rolle den klarsten Präfix.
2. Prüfe, ob alte Nummern beibehalten oder gespiegelt werden sollen.
3. Erzeuge Prefix-Legende für Schriftsatz und Anlagenverzeichnis.
4. Markiere Kollisionsrisiken.

## Ausgabe

- Präfixkonzept.
- Legendentext.
- Synchronisationsmatrix.

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
