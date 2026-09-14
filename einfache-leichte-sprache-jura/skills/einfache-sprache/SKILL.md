---
name: einfache-sprache
description: "Für Einfache Sprache: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Einfache Sprache

Dieses Fachmodul, wenn ein juristischer Text für ein allgemeines Publikum
verständlich werden soll, ohne die Standardsprache vollständig zu verlassen.

## Triage zu Beginn
1. Welche Zielgruppe soll den Text lesen (allgemeines Publikum, Personen mit geringer Lesekompetenz, Verbraucher mit Behördenkontakt)?
2. Welches Medium: Brief, Bescheid, Website, Formular, E-Mail?
3. Darf der Text stark gekürzt werden oder muss der vollständige Rechtsinhalt erhalten bleiben?
4. Gibt es bereits einen Hausstil oder eine Vorlage für Einfache Sprache in der Einrichtung?

## Zentrale Normen
- [Paragraf 11 BGG](https://www.gesetze-im-internet.de/bgg/__11.html): einfache und verständliche Kommunikation sowie bedarfsbezogene Erläuterungen in Leichter Sprache durch erfasste Träger öffentlicher Gewalt; keine allgemeine Pflicht aller privaten Verfasser.
- [Paragraf 4 BITV 2.0](https://www.gesetze-im-internet.de/bitv_2_0/__4.html) verweist für bestimmte Erläuterungen auf Startseiten öffentlicher Stellen auf Anlage 2. Nicht als allgemeine Vorschrift für jeden juristischen Text verwenden.

## Normen & Rechtsprechung

Konkret zu prüfen:

- Paragraf 11 SGB I regelt Leistungsarten, nicht Verständlichkeit; hierfür nicht als Rechtsgrundlage zitieren.
- BGG Paragraf 11 im jeweiligen persönlichen und institutionellen Anwendungsbereich prüfen.
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21

## Output-Template: Einfache-Sprache-Fassung

**Adressat:** Mandant / Buerger — **Tonfall:** klar, direkt, respektvoll

```
### Kurze Antwort

[1-2 Saetze: Das Wichtigste zuerst]

### Was ist passiert?

[Sachverhalt ohne Fachjargon]

### Was bedeutet das für Sie?

[Rechtliche Konsequenzen in verstaendlichen Worten]

### Was koennen Sie jetzt tun?

Option A: [Handlung 1 — Frist: DD.MM.JJJJ]
Option B: [Handlung 2]

### Frist

Wichtig: Bis [DATUM] muessen Sie handeln.
Wenn Sie nichts tun, dann: [Rechtsfolge kurz]

### Schwere Woerter kurz erklaert

- Widerspruch: Sie sagen der Behörde, dass Sie nicht einverstanden sind.
- Verjährung: Nach Ablauf dieser Frist darf die andere Seite die Leistung wegen Verjährung verweigern. Der Anspruch erlischt dadurch nicht automatisch.
```

## Ziel

Der Text soll schnell beantworten:

- Worum geht es?
- Was bedeutet das für die lesende Person?
- Was muss oder kann sie tun?
- Bis wann?
- Was passiert, wenn sie nichts tut?

## Regeln für die Übertragung

- Stelle die wichtigste Information an den Anfang.
- Verwende klare Überschriften.
- Halte Absätze kurz.
- Schreibe aktiv.
- Nutze Verben statt Substantivierungen.
- Vermeide verschachtelte Sätze.
- Erkläre Fachwörter beim ersten Auftreten.
- Verwende denselben Begriff immer gleich.
- Ersetze Amts- und Kanzleistil durch direkte, respektvolle Sprache.
- Lass Rechtsgrundlagen stehen, wenn sie wichtig sind, aber erkläre ihre
 Bedeutung.

## Juristische Struktur

Für Mandantenbriefe und Verbraucherinformationen verwende bevorzugt:

```markdown
### Kurze Antwort

...

### Was ist passiert?

...

### Was bedeutet das für Sie?

...

### Was können Sie jetzt tun?

...

### Frist

...

### Schwere Wörter kurz erklärt

...
```

## Was nicht passieren darf

- Keine Frist verkürzen oder verlängern.
- Keine Pflicht in eine bloße Empfehlung umformulieren.
- Kein Wahlrecht unterschlagen.
- Keine Ausnahme weglassen, wenn sie praktisch wichtig sein kann.
- Keine ungesicherte Rechtsberatung hinzufügen.
- Keine rechtliche Unsicherheit als sicher darstellen.

## Stilhinweise

Schlecht:

> Gegen den Bescheid kann binnen eines Monats nach Bekanntgabe Widerspruch
> erhoben werden.

Besser:

> Sie können Widerspruch einlegen.
> Dafür haben Sie 1 Monat Zeit.
> Die Frist beginnt, wenn Sie den Bescheid bekommen haben.

Dieses Beispiel nur verwenden, wenn tatsächlicher Zugang hier der maßgebliche Bekanntgabezeitpunkt ist. Gesetzliche Bekanntgaberegeln und Fristbeginn nicht durch eine vereinfachte Empfangsformel ersetzen. Für die Erklärung der Verjährung gilt [Paragraf 214 BGB](https://www.gesetze-im-internet.de/bgb/__214.html); geprüft am 14.09.2026.

## Ausgabe

Gib am Ende eine Mini-Prüfung aus:

| Punkt | Ergebnis |
| --- | --- |
| Zielgruppe genannt | ja/nein |
| Fristen erhalten | ja/nein |
| Rechtsfolgen erhalten | ja/nein |
| schwere Wörter erklärt | ja/nein |
| weiterer Prüfbedarf | kurz |

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
