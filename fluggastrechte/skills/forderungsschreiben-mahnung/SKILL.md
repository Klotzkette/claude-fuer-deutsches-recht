---
name: forderungsschreiben-mahnung
description: Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und droht konkret SOEP-Schlichtung oder Klage zum Amtsgericht. Bei Reaktion der Airline mit Standardausreden Verweis auf den Skill `airline-standardausreden-pruefen` zur Konfrontation mit Pinpoint auf EuGH-Rechtsprechung.
---

# Forderungsschreiben — Mahnung (zweite Stufe)

## Voraussetzung

Erstes Forderungsschreiben aus Skill `forderungsschreiben-erste-stufe` ist versendet — Frist ist abgelaufen oder Airline hat ablehnend reagiert.

## Struktur

```
Betreff: Mahnung — Forderung Ausgleichszahlung gemaess Art. 7 VO (EG)
         Nr. 261/2004 — Flug [Flugnummer] vom [Datum]
         Buchungscode [PNR]
         Mein voriges Schreiben vom [Datum erste Stufe]

Sehr geehrte Damen und Herren,

Sie haben auf mein Schreiben vom [Datum] [nicht reagiert / ablehnend
geantwortet]. Die hierin gestellten Forderungen sind weiterhin offen.

Zu Ihrer ablehnenden Begruendung [bei Ablehnung]:

  „[Zitat Airline-Begruendung]"

Diese Begruendung verfaengt nicht. Bei [technischer Defekt / Streik der
eigenen Mitarbeiter / Crew-Engpass / sonstige Standardausrede] handelt es
sich nach staendiger EuGH-Rechtsprechung regelmaessig NICHT um
aussergewoehnliche Umstaende im Sinn des Art. 5 Abs. 3 VO 261/2004:

  EuGH, Urt. v. [Datum] — C-[Nummer] ([Name])
  [Inhalt der Kernaussage]

Die Beweislast fuer aussergewoehnliche Umstaende und fuer die Ergreifung
aller zumutbaren Massnahmen liegt bei Ihnen.

Ich setze hiermit eine letzte Frist zur Zahlung des offenen Betrags von

  [Gesamtbetrag] EUR
  zuzueglich Verzugszinsen seit [Datum erste Frist + 1] in Hoehe von
  5 Prozentpunkten ueber dem Basiszinssatz gemaess § 288 Abs. 1 BGB

bis spaetestens [Datum + 10 Tage].

Sollten Sie die Zahlung nicht fristgerecht leisten werde ich:

  a) die Schlichtungsstelle fuer den oeffentlichen Personenverkehr SOEP
     anrufen — kostenfrei fuer Verbraucher,
  b) anschliessend Klage zum zustaendigen Amtsgericht erheben.

Im Klagefall werden Sie zudem die Gerichtskosten Anwaltskosten und alle
ueberfaelligen Verzugszinsen zu tragen haben. Die sachliche Zustaendigkeit
des Amtsgerichts ergibt sich aus § 23 Nr. 1 GVG bei Streitwerten bis
zehntausend Euro (i. d. F. seit 01.01.2026). Die oertliche Zustaendigkeit
ergibt sich nach EuGH C-204/08 (Rehder) wahlweise aus Abflug- oder
Zielflughafen oder aus § 13 ZPO Ihrem Sitz / Niederlassung in Deutschland.

Mit freundlichen Gruessen

[Unterschrift]
[Name]
```

## Standard-Gegenargumente

Wenn die Airline mit einer typischen Begruendung argumentiert siehe Skill
`airline-standardausreden-pruefen` — dort sind die EuGH-Pinpoints aufgelistet:

| Airline-Begruendung | Kerngegenargument | Rspr. |
|---|---|---|
| „technischer Defekt" | nicht aussergewoehnlich solange im Routinebetrieb | EuGH C-549/07 (Wallentin-Hermann) |
| „wilder Streik unserer Mitarbeiter" | nicht aussergewoehnlich | EuGH C-195/17 (Kruesemann) |
| „Crew-Engpass" | nicht aussergewoehnlich | st. Rspr. — Teil normalen Betriebs |
| „verdeckter Konstruktionsfehler" | nicht aussergewoehnlich | EuGH C-257/14 (van der Lans) |
| „Sie haben uns nicht innerhalb von 30 Tagen informiert" | VO 261/2004 sieht keine solche Frist vor | Verjaehrung drei Jahre § 195 BGB |
| „Sie haben Umbuchung akzeptiert" | Akzeptanz schliesst Ausgleichsanspruch nicht aus | EuGH staendig |
| „Sie haben Voucher erhalten" | wenn nicht ausdruecklich als Ausgleichszahlung gewidmet — kein Ausschluss | st. Rspr. |
| „Vorflug aus Vortag verspaetet" | regelmaessig nicht aussergewoehnlich (Kette aus Routine-Folge) | st. Rspr. EuGH |

## Versand

- **Einschreiben mit Rueckschein** wie Erststufe.
- Parallel **E-Mail an Kundenservice** mit Bezugnahme auf die erste Mahnung.

## Naechster Schritt

- Bei weiterer Untaetigkeit: **SOEP-Schlichtungsverfahren** oder **Klage** zum Amtsgericht.
- SOEP-Verfahren ist kostenfrei und oft erfolgreich. Voraussetzung: keine anhaengige Klage.
- Klage als letzter Schritt — Skill `klage-amtsgericht-fluggast`.

## Ausgabe

- `mahnung-zweite-stufe-<datum>.docx` und PDF.
- Eintrag im Tagesplan — Reaktionsfrist gesetzt.
