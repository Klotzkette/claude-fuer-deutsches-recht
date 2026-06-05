---
name: amtssprache-entschluesseln-anhoerung
description: "Amtssprache Entschluesseln Anhoerung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Amtssprache Entschluesseln Anhoerung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Amtssprache Entschluesseln Anhoerung** im Plugin Juristische Sprache Deutsch Als Zweitsprache. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `amtssprache-entschluesseln` | Hilft bei Amtssprache Entschluesseln fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch. |
| `anhoerung-verstehen` | Hilft bei Anhoerung Verstehen fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch. |

## Arbeitsweg

Im Plugin Juristische Sprache Deutsch Als Zweitsprache gilt für **Amtssprache Entschluesseln Anhoerung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `amtssprache-entschluesseln`

**Fokus:** Hilft bei Amtssprache Entschluesseln fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch.

# Amtssprache Entschluesseln

## Zweck

Dieser Skill unterstuetzt bei **Amtssprache Entschluesseln**, wenn deutsche Alltagssprache und deutsche Juristensprache gleichzeitig schwierig sind. Er behandelt die Nutzerin oder den Nutzer als erwachsene, handlungsfaehige Person und erklaert nur die sprachlichen und verfahrensbezogenen Huerden.

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

## Wichtige Warnwoerter und ihre Bedeutung

| Wort | Was es heisst | Was zu tun ist |
| --- | --- | --- |
| **Bestandskraeftig** | Entscheidung ist endgueltig; kein Widerspruch mehr moeglich. | Pruefen, ob Frist vorbei. Notfalls Wiederaufnahme nach § 51 VwVfG. |
| **Unanfechtbar** | Gleiche Bedeutung wie bestandskraeftig. | Schnell Anwalt fragen. |
| **Anerkenntnis** | Sie sagen: "Stimmt, ich habe Schuld." | Nie unterschreiben ohne Anwalt. § 307 ZPO Anerkenntnisurteil. |
| **Verzicht** | Sie geben einen Anspruch auf. | Bedeutet endgueltigen Verlust. § 397 BGB Erlass. |
| **Widerspruch** | Sie sagen: "Nein, ich bin nicht einverstanden." | Frist meist 1 Monat (§ 70 VwGO). Schriftlich oder zur Niederschrift. |
| **Klage** | Sie gehen vor Gericht. | Klagefrist meist 1 Monat (§ 74 VwGO). |
| **Mahnbescheid** | Vorstufe zur Zwangsvollstreckung. | 2 Wochen Widerspruch (§ 692 ZPO), sonst Vollstreckungsbescheid. |
| **Vollziehung** | Behoerde fuehrt Entscheidung aus. | Antrag auf aufschiebende Wirkung (§ 80 V VwGO) erwaegen. |

## Sprachebene waehlen

- **Einfache Sprache:** kurze Saetze, aktive Verben, ein Gedanke pro Satz. Beispiel: "Sie muessen bis 30. Juni zahlen."
- **Leichte Sprache:** noch einfacher; Regeln nach DIN SPEC 33429. Eher fuer Personen mit kognitiver Einschraenkung.
- **Behoerdensprache hoeflich-formal:** "Sehr geehrte Damen und Herren, mit Schreiben vom .. teilen Sie mit ... Hierzu nehme ich wie folgt Stellung: ..."
- Tipp: Mehrdeutige Formulierungen vermeiden ("erforderlichenfalls" → "wenn noetig"; "Sachverhalt" → "Geschehen").


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `anhoerung-verstehen`

**Fokus:** Hilft bei Anhoerung Verstehen fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch.

# Anhoerung Verstehen

## Zweck

Dieser Skill unterstuetzt bei **Anhoerung Verstehen**, wenn deutsche Alltagssprache und deutsche Juristensprache gleichzeitig schwierig sind. Er behandelt die Nutzerin oder den Nutzer als erwachsene, handlungsfaehige Person und erklaert nur die sprachlichen und verfahrensbezogenen Huerden.

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
