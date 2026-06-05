---
name: bgb-zpo-fmkw-saumselig-titulierung
description: "Bgb Zpo Forderungsnormcheck, Fmkw Saumselig Streitig Erfahrung Spezial, Fmkw Titulierung Streckung Leitfaden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Bgb Zpo Forderungsnormcheck, Fmkw Saumselig Streitig Erfahrung Spezial, Fmkw Titulierung Streckung Leitfaden

## Arbeitsbereich

Dieser Skill bündelt **Bgb Zpo Forderungsnormcheck, Fmkw Saumselig Streitig Erfahrung Spezial, Fmkw Titulierung Streckung Leitfaden** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `bgb-zpo-forderungsnormcheck` | BGB/ZPO-Forderungsnormcheck: prüft Anspruch, Fälligkeit, Verzug, Zinsen, Verjährung, Mahnverfahren, Klage, Zustellung demnächst, Titel, Klausel, Zustellung und Vollstreckung anhand aktueller Normen. |
| `fmkw-saumselig-streitig-erfahrung-spezial` | Spezialfall saeumiges Verfahren und streitiges Verfahren nach Widerspruch: prozessuale Weichen, Beweislast, Schriftsaetze. Pruefraster fuer Klaegeranwalt. |
| `fmkw-titulierung-streckung-leitfaden` | Leitfaden Titulierung mit Ratenzahlung und Streckung: Anerkenntnis, Schuldanerkenntnis, Ratenvereinbarung mit Vollstreckungsmoeglichkeit. Pruefraster fuer Inkassoanwalt. |

## Arbeitsweg

Für **Bgb Zpo Forderungsnormcheck, Fmkw Saumselig Streitig Erfahrung Spezial, Fmkw Titulierung Streckung Leitfaden** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `forderungsmanagement-klagewerkstatt` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `bgb-zpo-forderungsnormcheck`

**Fokus:** BGB/ZPO-Forderungsnormcheck: prüft Anspruch, Fälligkeit, Verzug, Zinsen, Verjährung, Mahnverfahren, Klage, Zustellung demnächst, Titel, Klausel, Zustellung und Vollstreckung anhand aktueller Normen.

# BGB/ZPO-Forderungsnormcheck

## Zweck

Dieser Skill ist der harte Gatekeeper vor Mahnung, Mahnbescheid, Zahlungsklage oder Vollstreckung. Er fragt nicht nur “besteht die Forderung?”, sondern: Ist sie fällig, beweisbar, nicht verjährt, prozessual richtig geltend gemacht und vollstreckbar?

## Prüfreihenfolge

1. Anspruchsgrundlage und Schuldner bestimmen.
2. Fälligkeit, Einreden, Zurückbehaltungsrechte und Verzug prüfen.
3. Zinsen und Nebenforderungen nach §§ 286, 288 BGB trennen.
4. Verjährung nach §§ 195, 199, 203, 204, 212 BGB prüfen.
5. Rechtsverfolgungsakt wählen: Mahnbescheid, Klage, Urkundenprozess, Eilverfahren.
6. ZPO-Durchsetzung prüfen: Zuständigkeit, Klageschrift, Mahnverfahren, Zustellung, Titel, Klausel, Vollstreckung.

## Normen

| Thema | Normen |
| --- | --- |
| Anspruch/Verzug | §§ 194, 241, 280, 286, 288 BGB |
| Verjährung | §§ 195, 199, 203, 204, 212 BGB |
| Zustellung demnächst | § 167 ZPO |
| Klage | §§ 253, 261 ZPO |
| Mahnverfahren | §§ 688-703d ZPO |
| Vollstreckungsvoraussetzungen | §§ 704, 724, 750 ZPO |
| Gerichtsvollzieher/Vermögensauskunft | §§ 753, 802a, 802c ZPO |
| Forderungspfändung | §§ 828, 829, 835 ZPO |

## Output

Erzeuge:

- Forderungsmatrix.
- Beleg- und Lückenliste.
- Verjährungs- und Fristenvermerk.
- Entscheidung: Mahnung, Mahnbescheid, Zahlungsklage, Vergleich, Vollstreckung oder Stop.
- Textbaustein für den nächsten Schritt.

## Referenz

Nutze `references/bgb-zpo-forderungskern.md`.

## 2. `fmkw-saumselig-streitig-erfahrung-spezial`

**Fokus:** Spezialfall saeumiges Verfahren und streitiges Verfahren nach Widerspruch: prozessuale Weichen, Beweislast, Schriftsaetze. Pruefraster fuer Klaegeranwalt.

# FMKW: Saumselig Streitig

## Fachkern: FMKW: Saumselig Streitig
- **Spezialgegenstand:** FMKW: Saumselig Streitig wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `forderungsmanagement-klagewerkstatt`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `fmkw-titulierung-streckung-leitfaden`

**Fokus:** Leitfaden Titulierung mit Ratenzahlung und Streckung: Anerkenntnis, Schuldanerkenntnis, Ratenvereinbarung mit Vollstreckungsmoeglichkeit. Pruefraster fuer Inkassoanwalt.

# FMKW: Titulierung Streckung

## Fachkern: FMKW: Titulierung Streckung
- **Spezialgegenstand:** FMKW: Titulierung Streckung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `forderungsmanagement-klagewerkstatt`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
