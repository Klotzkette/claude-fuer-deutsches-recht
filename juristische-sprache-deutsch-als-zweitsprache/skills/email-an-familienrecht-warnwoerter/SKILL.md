---
name: email-an-familienrecht-warnwoerter
description: "Email AN Familienrecht Warnwoerter: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Email AN Familienrecht Warnwoerter

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Email AN Familienrecht Warnwoerter** im Plugin Juristische Sprache Deutsch Als Zweitsprache. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `email-an-behoerde` | Hilft bei Email An Behoerde fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch. |
| `familienrecht-warnwoerter` | Hilft bei Familienrecht Warnwoerter fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch. |

## Arbeitsweg

Im Plugin Juristische Sprache Deutsch Als Zweitsprache gilt für **Email AN Familienrecht Warnwoerter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `email-an-behoerde`

**Fokus:** Hilft bei Email An Behoerde fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch.

# Email An Behoerde

## Zweck

Dieser Skill unterstuetzt bei **Email An Behoerde**, wenn deutsche Alltagssprache und deutsche Juristensprache gleichzeitig schwierig sind. Er behandelt die Nutzerin oder den Nutzer als erwachsene, handlungsfaehige Person und erklaert nur die sprachlichen und verfahrensbezogenen Huerden.

## Start

- Welches Dokument oder welche Situation liegt vor?
- Wer schreibt oder spricht: Gericht, Behoerde, Arbeitgeber, Vermieter, Anwalt, Polizei, Krankenkasse, Jobcenter, Gegner?
- Gibt es Frist, Termin, Zahlung, Unterschrift, Antrag, Widerspruch, Klage oder Anhoerung?
- Soll die Antwort einfach erklaeren, formal formulieren, uebersetzen, kontrollieren oder auf Risiken hinweisen?

## Arbeitsweise

1. Schwierige Woerter markieren und kurz erklaeren.
2. Den Satz in normale Reihenfolge bringen: Wer tut was, warum, bis wann, mit welcher Folge?
3. Warnwoerter hervorheben: Anerkenntnis, Verzicht, Ruecknahme, Zustimmung, Frist, sofort, bestandskraeftig, unanfechtbar.
4. Eigene Worte des Nutzers sammeln und ohne Bedeutungsverlust in gutes Deutsch uebertragen.
5. Bei Unsicherheit genau eine Rueckfrage stellen.

## Ausgabe

**Einfach erklaert**
- Das bedeutet der Text.
- Das ist wichtig.
- Das kann passieren.

**Formale Fassung**
Gib eine kurze, hoefliche und klare Formulierung aus. Keine uebertriebene Unterwuerfigkeit, keine ungewollten Zugestaendnisse.

**Check vor Absenden**
- Aktenzeichen richtig?
- Datum und Frist richtig?
- Anlagen genannt?
- Keine falsche Zustimmung?
- Sprache klar und respektvoll?

## Qualitaetsgate

Keine herablassende Sprache. Keine falsche Vereinfachung. Keine erfundenen Tatsachen. Umlaute, Namen und Zahlen sorgfaeltig uebernehmen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `familienrecht-warnwoerter`

**Fokus:** Hilft bei Familienrecht Warnwoerter fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch.

# Familienrecht Warnwoerter

## Zweck

Dieser Skill markiert typische **Warnwoerter im Familienrecht** und hilft Menschen mit Deutsch als Zweitsprache, riskante Erklaerungen zu Trennung, Scheidung, Sorgerecht, Unterhalt, Vermoegensauseinandersetzung zu erkennen.

## Warnwoerter mit hoher Tragweite
- **Scheidungsantrag**: leitet Scheidungsverfahren ein; Trennungsjahr Pflicht (§ 1565 BGB), Ausnahme Haertescheidung (§ 1565 Abs. 2 BGB).
- **Trennungsjahr**: § 1567 BGB; nicht "Probetrennung" mit Versoehnung verwechseln, sonst beginnt das Trennungsjahr von vorn.
- **Versorgungsausgleich**: § 1587 BGB; bei kurzer Ehe (< 3 Jahre) nicht automatisch.
- **Zugewinnausgleich**: § 1378 BGB; Vermoegensbilanz Anfang/Ende der Ehe; Auskunftspflicht § 1379 BGB.
- **Sorgeerklaerung** (§ 1626a BGB) bei nichtehelich Geborenen: Achtung -- Sorgerecht teilen, unwiderruflich.
- **Verzicht auf Trennungsunterhalt / nachehelichen Unterhalt**: oft im Ehevertrag; nicht unterschreiben ohne Beratung.
- **Anerkenntnis Vaterschaft** (§ 1594 BGB): in der Folge Unterhaltspflicht.
- **Aufhebungsantrag Ehe** (§ 1313 BGB): seltener Spezialfall (Doppelehe, Geschaeftsunfaehigkeit).
- **Sorgerechtsentzug / Aufenthaltsbestimmungsrecht**: ernste Folge fuer Eltern; Anhoerung Jugendamt und Kind (§ 159 FamFG).
- **Anhoerung beim Familiengericht**: oft entscheidungserheblich, Vorbereitung mit Anwalt sinnvoll.
- **"Einvernehmliche Scheidung"**: bedeutet nicht: ohne Anwalt; Antragsteller braucht Anwalt (§ 114 FamFG).

## Vor jeder Unterschrift / Erklaerung
- Bin ich mir der Tragweite bewusst (Unterhalt, Vermoegen, Sorge)?
- Habe ich Anspruch auf Verfahrenskostenhilfe (§§ 76 ff. FamFG)?
- Wurde ich vor Gericht in der Muttersprache angehoert? Dolmetscher (§ 185 GVG).

## Start

- Welches Dokument oder welche Situation liegt vor?
- Wer schreibt oder spricht: Gericht, Behoerde, Arbeitgeber, Vermieter, Anwalt, Polizei, Krankenkasse, Jobcenter, Gegner?
- Gibt es Frist, Termin, Zahlung, Unterschrift, Antrag, Widerspruch, Klage oder Anhoerung?
- Soll die Antwort einfach erklaeren, formal formulieren, uebersetzen, kontrollieren oder auf Risiken hinweisen?

## Arbeitsweise

1. Schwierige Woerter markieren und kurz erklaeren.
2. Den Satz in normale Reihenfolge bringen: Wer tut was, warum, bis wann, mit welcher Folge?
3. Warnwoerter hervorheben: Anerkenntnis, Verzicht, Ruecknahme, Zustimmung, Frist, sofort, bestandskraeftig, unanfechtbar.
4. Eigene Worte des Nutzers sammeln und ohne Bedeutungsverlust in gutes Deutsch uebertragen.
5. Bei Unsicherheit genau eine Rueckfrage stellen.

## Ausgabe

**Einfach erklaert**
- Das bedeutet der Text.
- Das ist wichtig.
- Das kann passieren.

**Formale Fassung**
Gib eine kurze, hoefliche und klare Formulierung aus. Keine uebertriebene Unterwuerfigkeit, keine ungewollten Zugestaendnisse.

**Check vor Absenden**
- Aktenzeichen richtig?
- Datum und Frist richtig?
- Anlagen genannt?
- Keine falsche Zustimmung?
- Sprache klar und respektvoll?

## Qualitaetsgate

Keine herablassende Sprache. Keine falsche Vereinfachung. Keine erfundenen Tatsachen. Umlaute, Namen und Zahlen sorgfaeltig uebernehmen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
