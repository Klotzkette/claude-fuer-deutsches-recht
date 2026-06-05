---
name: nachreichung-berichtigung-ocr-scan-original
description: "Nachreichung Berichtigung OCR Scan Original: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nachreichung Berichtigung OCR Scan Original

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Nachreichung Berichtigung OCR Scan Original** im Plugin Anlagen zu Schriftsätzen. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nachreichung-berichtigung-und-gerichtshinweis` | Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung. |
| `ocr-scan-lesbarkeit-und-beweiswert` | Prüft gescannte Anlagen auf Lesbarkeit, OCR-Durchsuchbarkeit, Seitenreihenfolge, abgeschnittene Ränder, schiefe Scans und Beweiswertprobleme. |
| `original-abschrift-kopie-und-elektronische-fassung` | Klären, wann Original, beglaubigte Abschrift, einfache Kopie, Scan, elektronisches Dokument oder Ausdruck als Anlage sinnvoll oder erforderlich ist. |
| `schriftsatz-anlagen-mapping` | Schriftsatzstellen, Tatsachenbehauptungen, Beweisangebote und Anlagen in eine Matrix bringen; erkennt fehlende, doppelte und nur scheinbar belegte Anlagen. |

## Arbeitsweg

Im Plugin Anlagen zu Schriftsätzen gilt für **Nachreichung Berichtigung OCR Scan Original**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nachreichung-berichtigung-und-gerichtshinweis`

**Fokus:** Plant die Reparatur eines Anlagenpakets nach gerichtlichem Hinweis, Rüge der Gegenseite, falscher Anlage, fehlender Datei oder versehentlicher Einreichung.

# Nachreichung, Berichtigung und gerichtlicher Hinweis

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

## 2. `ocr-scan-lesbarkeit-und-beweiswert`

**Fokus:** Prüft gescannte Anlagen auf Lesbarkeit, OCR-Durchsuchbarkeit, Seitenreihenfolge, abgeschnittene Ränder, schiefe Scans und Beweiswertprobleme.

# OCR, Scanqualität und Lesbarkeit

## Zweck

Dieser Skill schaut wie eine strenge Geschäftsstelle auf das Paket: Kann man es lesen? Kann man es durchsuchen? Fehlt Seite 2? Ist die Unterschrift abgeschnitten? Sind Fotos zu dunkel?

## Mindestinput

- PDF-/Scanliste.
- Hinweis, ob Originale vorhanden sind.
- Frist und gewünschter Aufwand.

## Arbeitsablauf

1. Prüfe Sichtbarkeit, Vollständigkeit, Seitenreihenfolge und OCR.
2. Markiere Dokumente, die neu gescannt oder im Original vorgelegt werden sollten.
3. Entscheide, ob Vergrößerung/Ausschnitt zusätzlich sinnvoll ist.
4. Erzeuge klare Scan-Anweisung für Mandant oder Assistenz.

## Ausgabe

- Lesbarkeitsampel.
- Neuscan-Liste.
- OCR-/PDF/A-Prüfnotiz.
- Anweisung für bessere Reproduktion.

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

## 3. `original-abschrift-kopie-und-elektronische-fassung`

**Fokus:** Klären, wann Original, beglaubigte Abschrift, einfache Kopie, Scan, elektronisches Dokument oder Ausdruck als Anlage sinnvoll oder erforderlich ist.

# Original, Abschrift, Kopie und elektronische Fassung

## Zweck

Dieser Skill verhindert Formverwechslungen: Eine Anlage ist oft nur Beleg, manchmal aber gerade Urkunde, Original, Vollmacht, Ausfertigung oder beglaubigte Abschrift.

## Mindestinput

- Dokumentart.
- Verfahrensart und Gericht.
- Ob Original vorhanden ist.
- Streit über Echtheit ja/nein.

## Arbeitsablauf

1. Ordne Dokumentqualität ein.
2. Prüfe, ob Originalvorlage, Kopie oder Scan genügt.
3. Markiere Echtheits- und Bestreitensrisiken.
4. Formuliere Vorlage-/Nachreichungsvorschlag.

## Ausgabe

- Dokumentqualitätsvermerk.
- Vorlageempfehlung.
- Schriftsatzbaustein.

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

## 4. `schriftsatz-anlagen-mapping`

**Fokus:** Schriftsatzstellen, Tatsachenbehauptungen, Beweisangebote und Anlagen in eine Matrix bringen; erkennt fehlende, doppelte und nur scheinbar belegte Anlagen.

# Schriftsatz-Anlagen-Mapping

## Zweck

Dieser Skill liest den Schriftsatz als Landkarte. Jede erhebliche Behauptung bekommt eine Belegstelle; jede Anlage bekommt eine Funktion. Das verhindert die verbreitete Krankheit: viele Anlagen, aber kein tragender Vortrag.

## Mindestinput

- Schriftsatzentwurf oder Auszug.
- Vorläufiges Anlagenverzeichnis oder Dateiliste.
- Angabe, ob geprüft oder neu nummeriert werden soll.

## Arbeitsablauf

1. Extrahiere alle Anlagenzitate und Beweisangebote.
2. Formuliere den Tatsachenkern jeder Beweisstelle.
3. Ordne vorhandene Dateien zu und markiere unklare Zuordnungen.
4. Prüfe, ob der Tatsachenvortrag im Schriftsatz selbst steht.
5. Erzeuge Lücken-, Doppelungs- und Überhangliste.

## Ausgabe

- Belegmatrix als Tabelle.
- Liste „zitiert, aber Datei fehlt“.
- Liste „Datei vorhanden, aber nicht eingeführt“.
- Korrekturvorschläge für Schriftsatzanker.

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
