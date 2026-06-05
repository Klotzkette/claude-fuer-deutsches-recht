---
name: anwaltsschreiben-aussergerichtlich
description: "Anwaltsschreiben Aussergerichtlich: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anwaltsschreiben Aussergerichtlich

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anwaltsschreiben Aussergerichtlich** im Plugin Word-Legal-AI für deutsche Anwälte. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anwaltsschreiben-aussergerichtlich` | Außergerichtliches Anwaltsschreiben in drei Spielarten: erster anwaltlicher Brief, Mahnschreiben nach § 286 BGB mit Verzugsbegründung und Vergleichsangebot. Aufbau: Mandantenbezug; Vollmachtnachweis; knapper Sachverhalt; Anspruch oder Forderung mit Berechnung; konkrete Frist mit Datum; Konsequenz bei Nichteinhaltung; Vorbehalt weiterer Schritte. Mit Verzugsfolgen nach § 288 BGB; Annahmefristen und Mustertexten für die drei Brieftypen sowie typischen Drafting-Fehlern. |
| `argumentationsarchitektur-schreiben` | Baut die Argumentationsarchitektur für Schriftsatz, Memo oder Verhandlungsposition. Ordnet These, Norm, Tatsache, Beleg, Gegenargument, Antwort und Ergebnis. Erkennt Sprünge, verdeckte Prämissen, fehlende Beweisangebote und unklare Rechtsfolge und erzeugt eine tragfähige Gliederung. |

## Arbeitsweg

Im Plugin Word-Legal-AI für deutsche Anwälte gilt für **Anwaltsschreiben Aussergerichtlich**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anwaltsschreiben-aussergerichtlich`

**Fokus:** Außergerichtliches Anwaltsschreiben in drei Spielarten: erster anwaltlicher Brief, Mahnschreiben nach § 286 BGB mit Verzugsbegründung und Vergleichsangebot. Aufbau: Mandantenbezug; Vollmachtnachweis; knapper Sachverhalt; Anspruch oder Forderung mit Berechnung; konkrete Frist mit Datum; Konsequenz bei Nichteinhaltung; Vorbehalt weiterer Schritte. Mit Verzugsfolgen nach § 288 BGB; Annahmefristen und Mustertexten für die drei Brieftypen sowie typischen Drafting-Fehlern.

# Anwaltsschreiben aussergerichtlich

## Zweck

Das außergerichtliche Anwaltsschreiben ist häufig der erste Kontakt zwischen Mandant und Gegenseite über anwaltliche Vertretung. Es entscheidet Tonlage, Verzug, Verjährungsunterbrechung und die Bereitschaft der Gegenseite zur einvernehmlichen Erledigung. Drei Brieftypen kommen am häufigsten vor: der Erstkontaktbrief mit Forderung, das Mahnschreiben mit Fristsetzung und das Vergleichsangebot mit Annahmefrist.

Dieser Skill liefert das Drafting-Gerüst für alle drei Spielarten und stellt drei Mustertexte zur Verfügung. Er klärt knapp die rechtlichen Verzugsvoraussetzungen und vermeidet die typischen Fehler.

## Eingaben

- Mandanteninformation (Name, Anschrift, ggf. Vertretung)
- Vollmacht (im Brief erwähnen, beifügen oder vorausgesetzt)
- Adressat (Name, Anschrift, ggf. Vertretung der Gegenseite)
- Sachverhalt in Stichpunkten
- Anspruchsgrundlage und konkrete Höhe (in Euro, ggf. mit Berechnung)
- Frist und gewünschtes Datum
- Brieftyp (Erstkontakt, Mahnung, Vergleichsangebot)

## Rechtlicher und methodischer Rahmen

- § 286 Abs. 1 BGB: Verzug durch Mahnung nach Fälligkeit.
- § 286 Abs. 2 BGB: Verzug ohne Mahnung bei kalendermäßig bestimmtem Termin oder anderen genannten Fällen.
- § 286 Abs. 3 BGB: Verzug spätestens 30 Tage nach Fälligkeit und Rechnungszugang gegenüber Verbrauchern.
- § 288 BGB: Verzugszinssatz fünf Prozentpunkte über Basiszinssatz; bei Entgeltforderungen aus Rechtsgeschäft ohne Verbraucherbeteiligung neun Prozentpunkte.
- § 280 Abs. 2 BGB in Verbindung mit § 286 BGB: Verzugsschaden inklusive Rechtsverfolgungskosten (RVG-Geschäftsgebühr Nr. 2300 VV RVG).
- § 203 BGB: Hemmung der Verjährung durch Verhandlungen.
- § 43a BRAO: Anwaltliche Sorgfalt und Sachlichkeitsgebot.
- §§ 4, 13 RVG; Nr. 2300 VV RVG: Geschäftsgebühr außergerichtlich.
- Methodik: Urteilsstil. Sie-Form. Keine Drohgebärden, klare Konsequenzformulierung.

## Ablauf / Checkliste

1. **Briefkopf und Bezugslinie.** Mandant, Anschrift Gegenseite, Aktenzeichen Ihrer Kanzlei, Datum, Betreff.
2. **Anrede.** "Sehr geehrte Damen und Herren" bei Unternehmen, sonst persönliche Anrede.
3. **Mandantsbezug und Vollmacht.** "In dieser Sache vertreten wir die Interessen unserer Mandantin, der Frau X. Eine schriftliche Vollmacht liegt vor und wird auf Anforderung übersandt."
4. **Sachverhalt knapp.** Drei bis sechs Sätze. Keine Aktenführung, kein Tagebuch.
5. **Anspruch oder Forderung.** Klar nennen, Höhe konkret, Anspruchsgrundlage angeben.
6. **Frist mit Datum.** "Wir fordern Sie auf, den Betrag bis zum 20. Juni 2026 (Posteingang bei uns) auf das nachstehende Konto zu überweisen." Keine "unverzüglich"-Floskeln.
7. **Konsequenz benennen.** Klageerhebung, gerichtliches Mahnverfahren, Strafanzeige nur wenn berechtigt. Keine leeren Drohungen.
8. **Vorbehalt aller Rechte.** Standardformulierung.
9. **Schlussformel und Unterschrift.** "Mit freundlichen Grüßen", Berufsbezeichnung.

### Brieftyp-Matrix

| Brieftyp | Schwerpunkt | Pflichtelemente | Fristlänge typisch |
|---|---|---|---|
| Erstkontakt | Vorstellung Mandat, erste Forderung | Anspruchsgrundlage, Höhe, erste Frist | 14 Tage |
| Mahnung | Verzugsbegründung, Folgenwarnung | Fälligkeit, Mahnung, Verzugsfolgen | sieben bis 14 Tage |
| Vergleichsangebot | konkretes Zahlenangebot, Annahmemodus | Höhe in Euro, Annahmefrist, Erledigungsklausel | sieben bis 21 Tage |

## Typische Drafting-Fehler

- **Drohungen ohne Substanz.** "Wir behalten uns vor, weitere rechtliche Schritte einzuleiten" ohne Anspruchsgrundlage ist berufsrechtlich heikel.
- **Pauschalforderungen ohne Berechnung.** "Schadensersatz in angemessener Höhe" ist kein anwaltlicher Brief.
- **Unklare Frist.** "Unverzüglich" oder "zeitnah" sind keine Fristen. Konkretes Datum.
- **Schriftform-Fehler.** Bei Kündigungen Schriftform (§ 126 BGB) oder Textform (§ 126b BGB) prüfen. Briefkopf reicht nicht in jedem Fall.
- **Falsche Anrede oder fehlendes "Sie".** Persönliche Anrede in geschäftlichen Briefen ungewöhnlich.
- **RVG-Gebühr nicht angemeldet.** Wenn Verzug vorliegt, ist die Geschäftsgebühr Verzugsschaden und sollte mitgefordert werden.

## Ausgabeformat

- Vollständiger Brief im Format DIN 5008.
- Bei Mahnung: Verzugsdatum, Hauptforderung, Verzugszinsen, RVG-Gebühr separat ausgewiesen.
- Bei Vergleichsangebot: Erledigungsklausel ausformuliert.

## Beispiele

### Mustertext Erstkontakt

```
Anwaltskanzlei Stern und Partner
Musterallee 4 · 12345 Musterstadt

Beklagt GmbH
Industrieweg 5
12345 Beispielstadt Berlin, den 30. Mai 2026

Unser Zeichen: 2026 023 sm
Ihre Mandantin: Anna Muster

Sehr geehrte Damen und Herren,

in dieser Sache vertreten wir die Interessen unserer Mandantin
Frau Anna Muster. Eine schriftliche Vollmacht liegt vor und wird auf
Anforderung übersandt.

Unsere Mandantin und Sie schlossen am 15. Januar 2026 einen Kaufvertrag
über zehn Maschinen Typ A-100 zum Gesamtpreis von 25.000 Euro netto.
Unsere Mandantin lieferte am 1. Februar 2026. Die Rechnung war binnen 30
Tagen ab Lieferung fällig. Eine Zahlung ist bis heute nicht erfolgt.

Wir fordern Sie auf, den Betrag von 25.000 Euro bis zum 14. Juni 2026
(Posteingang bei uns) auf das Konto der Mandantin (IBAN DE12 1234 5678
9012 3456 78) zu überweisen.

Sollte die Zahlung nicht fristgerecht eingehen, werden wir ohne weiteres
Klage erheben. Bereits jetzt machen wir vorsorglich darauf aufmerksam,
dass weitere Kosten entstehen können.

Mit freundlichen Grüßen
Marta Stern
Rechtsanwältin
```

### Mustertext Mahnung

```
[Briefkopf] Berlin, den 30. Mai 2026

Mahnung in Sachen Anna Muster ./. Beklagt GmbH

Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantin Frau Anna Muster mahnen wir
hiermit die Zahlung der offenen Kaufpreisforderung an.

Hauptforderung: 25.000,00 Euro (fällig seit 1. März 2026)
Verzugszinsen § 288 Abs. 2: gemäß gesonderter Berechnung
Geschäftsgebühr Nr. 2300 VV RVG: gesonderte Berechnung

Wir setzen Ihnen eine letzte Zahlungsfrist bis zum 13. Juni 2026
(Posteingang bei uns). Nach Ablauf der Frist werden wir ohne weitere
Mahnung Klage erheben.

Mit freundlichen Grüßen
Marta Stern
Rechtsanwältin
```

### Mustertext Vergleichsangebot

```
[Briefkopf] Berlin, den 30. Mai 2026

Vergleichsangebot in Sachen Anna Muster ./. Beklagt GmbH

Sehr geehrte Damen und Herren,

zur außergerichtlichen Erledigung des Streits über die offene
Kaufpreisforderung schlagen wir Folgendes vor:

1. Die Beklagt GmbH zahlt an unsere Mandantin 22.000 Euro bis zum 30.
 Juni 2026 auf das Konto IBAN DE12 1234 5678 9012 3456 78.

2. Mit der vollständigen Zahlung sind sämtliche wechselseitigen Ansprüche
 aus dem Kaufvertrag vom 15. Januar 2026 erledigt.

3. Jede Partei trägt ihre außergerichtlichen Kosten selbst.

Wir bitten um schriftliche Annahme bis zum 13. Juni 2026
(Posteingang bei uns). Andernfalls erfolgt Klageerhebung.

Mit freundlichen Grüßen
Marta Stern
Rechtsanwältin
```

## Querverweise

- `klage-drafting-253-zpo` als nächste Eskalationsstufe
- `stil-und-ton-juristische-texte`
- `gutachten-memo-internes-drafting` für die interne Vorprüfung
- `revisions-prozess-redlines-comparison` für Markup eines Vergleichstexts

## Quellen (Stand 05/2026)

- §§ 280, 286, 288 BGB; § 203 BGB; gesetze-im-internet.de.
- § 43a BRAO; Sachlichkeitsgebot; vgl. § 6 BORA.
- § 4 RVG; Nr. 2300 VV RVG für die Geschäftsgebühr.
- § 126, § 126b BGB zur Schriftform und Textform.
- `references/zitierweise.md` für Belegpflicht.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `argumentationsarchitektur-schreiben`

**Fokus:** Baut die Argumentationsarchitektur für Schriftsatz, Memo oder Verhandlungsposition. Ordnet These, Norm, Tatsache, Beleg, Gegenargument, Antwort und Ergebnis. Erkennt Sprünge, verdeckte Prämissen, fehlende Beweisangebote und unklare Rechtsfolge und erzeugt eine tragfähige Gliederung.

# Argumentationsarchitektur Schreiben

## Zweck

Viele juristische Texte scheitern nicht an Sprache, sondern an Architektur. Dieser Skill baut die tragende Linie: Was soll bewiesen werden, worauf stützt es sich, was ist die Rechtsfolge, wo sitzt das Gegenargument?

## Bausteine

| Baustein | Frage |
|---|---|
| These | Was soll am Ende gelten? |
| Norm oder Klausel | Worauf stützt sich die These? |
| Tatsache | Welche konkrete Tatsache trägt die Subsumtion? |
| Beleg | Wo steht das in Akte, Anlage, Vertrag, E-Mail oder Zeugnis? |
| Gegenargument | Was wird die Gegenseite sagen? |
| Antwort | Warum trägt das Gegenargument nicht? |
| Rechtsfolge | Was folgt praktisch? |

## Ablauf

1. Ziel des Textes bestimmen.
2. Hauptthese in einem Satz formulieren.
3. Unterthesen bilden.
4. Für jede These Norm, Tatsache und Beleg zuordnen.
5. Gegenargumente danebenstellen.
6. Reihenfolge festlegen: stärkstes Argument zuerst, hilfsweise danach.
7. Überschriften als Ergebnisse formulieren.

## Beispiel-Überschriften

Schwach:

```text
Zur Kündigung
```

Stark:

```text
Die außerordentliche Kündigung ist unwirksam, weil die Abmahnung fehlt.
```

## Output

- Argumentationslandkarte.
- Gliederung mit Ergebnisüberschriften.
- Liste fehlender Belege.
- Erste ausformulierte Kernpassage.

## Querverweise

- `schriftsatz-ueberarbeiten-richterlesbar`
- `mandantenmemo-und-partner-update`
- `drafting-prinzipien-klarheit-bestimmtheit-praezision`


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
