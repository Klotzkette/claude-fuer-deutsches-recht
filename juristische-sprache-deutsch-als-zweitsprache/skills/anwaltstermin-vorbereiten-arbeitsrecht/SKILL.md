---
name: anwaltstermin-vorbereiten-arbeitsrecht
description: "Anwaltstermin Vorbereiten Arbeitsrecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anwaltstermin Vorbereiten Arbeitsrecht

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Anwaltstermin Vorbereiten Arbeitsrecht** im Plugin Juristische Sprache Deutsch Als Zweitsprache. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anwaltstermin-vorbereiten` | Hilft bei Anwaltstermin Vorbereiten fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch. |
| `arbeitsrecht-warnwoerter` | Hilft bei Arbeitsrecht Warnwoerter fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch. |

## Arbeitsweg

Im Plugin Juristische Sprache Deutsch Als Zweitsprache gilt für **Anwaltstermin Vorbereiten Arbeitsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anwaltstermin-vorbereiten`

**Fokus:** Hilft bei Anwaltstermin Vorbereiten fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch.

# Anwaltstermin Vorbereiten

## Zweck

Dieser Skill unterstuetzt bei **Anwaltstermin Vorbereiten**, wenn deutsche Alltagssprache und deutsche Juristensprache gleichzeitig schwierig sind. Er behandelt die Nutzerin oder den Nutzer als erwachsene, handlungsfaehige Person und erklaert nur die sprachlichen und verfahrensbezogenen Huerden.

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

## 2. `arbeitsrecht-warnwoerter`

**Fokus:** Hilft bei Arbeitsrecht Warnwoerter fuer Menschen mit Deutsch als Zweitsprache. Erklaert Juristendeutsch, klaert Risiko, Frist und naechste Handlung, und formuliert respektvoll in einfachem oder formalem Deutsch.

# Arbeitsrecht Warnwoerter

## Zweck

Dieser Skill markiert typische **Warnwoerter im Arbeitsrecht**, deren falsche Unterschrift oder Annahme den Mandanten Geld, Stellung oder Anspruch kosten kann. Er hilft Menschen mit Deutsch als Zweitsprache, diese Fallen zu erkennen, bevor sie eine Erklaerung abgeben.

## Warnwoerter mit hoher Tragweite
- **Aufhebungsvertrag** (Ende des Arbeitsverhaeltnisses einvernehmlich): kann Sperrzeit beim Arbeitslosengeld ausloesen (§ 159 SGB III).
- **Eigenkuendigung**: ebenfalls Sperrzeit-Gefahr.
- **Abwicklungsvertrag**: regelt Folgen der Kuendigung; oft Klageverzicht enthalten.
- **Ausgleichsklausel / Erledigungsklausel**: "Mit Erfuellung dieser Vereinbarung sind alle Ansprueche erledigt." -- erfasst auch unbekannte Ansprueche.
- **Klageverzicht**: macht Kuendigungsschutzklage unmoeglich.
- **Verzicht auf Annahmeverzugslohn (§ 615 BGB)**: verzichtet auf Lohn waehrend des Streits.
- **Freistellung unter Anrechnung von Urlaub**: Urlaub gilt als genommen.
- **"Sofort"** in Bezug auf Frist: 3-Wochen-Klagefrist nach Kuendigungsschutzgesetz (§ 4 KSchG) ist absolut.
- **"unwiderruflich"** / **"endgueltig"**: keine Rueckholmoeglichkeit.

## Vor jeder Unterschrift fragen
- Kann ich die 3-Wochen-Frist nach § 4 KSchG erhalten?
- Verzichte ich auf Geld (Lohn, Abfindung, Urlaub, Zeugnis)?
- Schliesse ich Ansprueche aus, die ich noch gar nicht kenne?

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
