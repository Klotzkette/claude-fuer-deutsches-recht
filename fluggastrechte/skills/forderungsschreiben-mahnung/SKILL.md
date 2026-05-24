---
name: forderungsschreiben-mahnung
description: Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Schlichtung oder Klage zum Amtsgericht. Bei Reaktion der Airline mit Standardausreden Verweis auf den Skill `airline-standardausreden-pruefen` zur Konfrontation mit Pinpoint auf EuGH-Rechtsprechung.
---

# Forderungsschreiben — Mahnung (zweite Stufe)

## Voraussetzung

Erstes Forderungsschreiben aus Skill `forderungsschreiben-erste-stufe` ist versendet — Frist ist abgelaufen oder Airline hat ablehnend reagiert.

## Struktur

```
Betreff: Mahnung — Forderung Ausgleichszahlung gemäß Art. 7 VO (EG)
         Nr. 261/2004 — Flug [Flugnummer] vom [Datum]
         Buchungscode [PNR]
         Mein voriges Schreiben vom [Datum erste Stufe]

Sehr geehrte Damen und Herren,

Sie haben auf mein Schreiben vom [Datum] [nicht reagiert / ablehnend
geantwortet]. Die hierin gestellten Forderungen sind weiterhin offen.

Zu Ihrer ablehnenden Begründung [bei Ablehnung]:

  „[Zitat Airline-Begründung]"

Diese Begründung verfaengt nicht. Bei [technischer Defekt / Streik der
eigenen Mitarbeiter / Crew-Engpass / sonstige Standardausrede] handelt es
sich nach ständiger EuGH-Rechtsprechung regelmäßig NICHT um
außergewöhnliche Umstaende im Sinn des Art. 5 Abs. 3 VO 261/2004:

  EuGH, Urt. v. [Datum] — C-[Nummer] ([Name])
  [Inhalt der Kernaussage]

Die Beweislast für außergewöhnliche Umstaende und für die Ergreifung
aller zumutbaren Maßnahmen liegt bei Ihnen.

Ich setze hiermit eine letzte Frist zur Zahlung des offenen Betrags von

  [Gesamtbetrag] EUR
  zuzueglich Verzugszinsen seit [Datum erste Frist + 1] in Höhe von
  5 Prozentpunkten über dem Basiszinssatz gemäß § 288 Abs. 1 BGB

bis spaetestens [Datum + 10 Tage].

Sollten Sie die Zahlung nicht fristgerecht leisten werde ich:

  a) die Schlichtungsstelle für den öffentlichen Personenverkehr SOEP
     anrufen — kostenfrei für Verbraucher,
  b) anschliessend Klage zum zuständigen Amtsgericht erheben.

Im Klagefall werden Sie zudem die Gerichtskosten Anwaltskosten und alle
ueberfälligen Verzugszinsen zu tragen haben. Die sachliche Zuständigkeit
des Amtsgerichts ergibt sich aus § 23 Nr. 1 GVG bei Streitwerten bis
zehntausend Euro (i. d. F. seit 01.01.2026). Die oertliche Zuständigkeit
ergibt sich nach EuGH C-204/08 (Rehder) wahlweise aus Abflug- oder
Zielflughafen oder aus § 13 ZPO Ihrem Sitz / Niederlassung in Deutschland.

Mit freundlichen Grüßen

[Unterschrift]
[Name]
```

## Standard-Gegenargumente

Wenn die Airline mit einer typischen Begründung argumentiert siehe Skill
`airline-standardausreden-pruefen` — dort sind die EuGH-Pinpoints aufgelistet:

| Airline-Begründung | Kerngegenargument | Rspr. |
|---|---|---|
| „technischer Defekt" | nicht außergewöhnlich solange im Routinebetrieb | EuGH C-549/07 (Wallentin-Hermann) |
| „wilder Streik unserer Mitarbeiter" | nicht außergewöhnlich | EuGH C-195/17 (Kruesemann) |
| „Crew-Engpass" | nicht außergewöhnlich | st. Rspr. — Teil normalen Betriebs |
| „verdeckter Konstruktionsfehler" | nicht außergewöhnlich | EuGH C-257/14 (van der Lans) |
| „Sie haben uns nicht innerhalb von 30 Tagen informiert" | VO 261/2004 sieht keine solche Frist vor | Verjährung drei Jahre § 195 BGB |
| „Sie haben Umbuchung akzeptiert" | Akzeptanz schließt Ausgleichsanspruch nicht aus | EuGH ständig |
| „Sie haben Voucher erhalten" | wenn nicht ausdrücklich als Ausgleichszahlung gewidmet — kein Ausschluss | st. Rspr. |
| „Vorflug aus Vortag verspätet" | regelmäßig nicht außergewöhnlich (Kette aus Routine-Folge) | st. Rspr. EuGH |

## Versand

- **Einschreiben mit Rückschein** wie Erststufe.
- Parallel **E-Mail an Kundenservice** mit Bezugnahme auf die erste Mahnung.

## Nächster Schritt

- Bei weiterer Untätigkeit: **SOEP-Schlichtungsverfahren** oder **Klage** zum Amtsgericht.
- SOEP-Verfahren ist kostenfrei und oft erfolgreich. Voraussetzung: keine anhängige Klage.
- Klage als letzter Schritt — Skill `klage-amtsgericht-fluggast`.

## Ausgabe

- `mahnung-zweite-stufe-<datum>.docx` und PDF.
- Eintrag im Tagesplan — Reaktionsfrist gesetzt.

## Anlagen-Übergabe

Unmittelbar nach Erstellung des Schreibens den Skill `fluggastrechte-anlagen-bauen` aufrufen.

Übergabe-Schema:

```yaml
schriftsatz: mahnung-zweite-stufe-<datum>.docx
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold
bezeichnung: "Anlage K"
```

Wichtig: Die Mahnung nimmt regelmäßig dieselben Anlagen wie das Erstschreiben in Bezug **plus** das erste Forderungsschreiben selbst und ggf. die Antwort der Airline. Vor Übergabe sicherstellen, dass im Schriftsatz alle benötigten Anlagen mit „Anlage K N" benannt sind — der Skill zieht die Reihenfolge aus dem Text.
