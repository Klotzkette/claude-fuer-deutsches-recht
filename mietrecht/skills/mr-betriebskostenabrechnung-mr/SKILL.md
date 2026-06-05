---
name: mr-betriebskostenabrechnung-mr
description: "MR Betriebskostenabrechnung MR: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# MR Betriebskostenabrechnung MR

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **MR Betriebskostenabrechnung MR** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mr-betriebskostenabrechnung-fehler-spezial` | Fehlerhafte Betriebskostenabrechnung als Streitfall: formelle Mindestangaben, materielle Umlagefähigkeit, Belegeinsicht nach § 259 BGB, Zahlungsbelege, 12-Monats-Fristen nach § 556 Abs. 3 BGB, Zurückbehaltung, Rückzahlungsklage und Mustertexte. |
| `mr-kuendigungsschutz-praxis` | Wohnraum-Kuendigungsschutz Praxis: ordentliche Kuendigung § 573 BGB nur bei berechtigtem Interesse, Eigenbedarf § 573 Abs. 2 Nr. 2 BGB, Kuendigung bei Pflichtverletzung, Zahlungsverzug. Sozialklausel § 574 BGB. Pruefraster. |
| `mr-modernisierung-und-rolling-rent-spezial` | Spezialfall Modernisierungs-Umlage in der laufenden Mieterhoehung: Verhaeltnis § 559 BGB zur ortsueblichen Vergleichsmiete § 558 BGB, Kappungsgrenze, Haerteeinwand. Aktuelle Rechtsprechung BGH. Pruefraster. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **MR Betriebskostenabrechnung MR**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `mr-betriebskostenabrechnung-fehler-spezial`

**Fokus:** Fehlerhafte Betriebskostenabrechnung als Streitfall: formelle Mindestangaben, materielle Umlagefähigkeit, Belegeinsicht nach § 259 BGB, Zahlungsbelege, 12-Monats-Fristen nach § 556 Abs. 3 BGB, Zurückbehaltung, Rückzahlungsklage und Mustertexte.

# Mietrecht: Betriebskosten-Fehler

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietrecht: Betriebskosten-Fehler` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill ist der Streitfall-Skill: Er hilft, wenn die Abrechnung schon auf dem Tisch liegt, der Mieter nicht zahlen will, der Vermieter eine Nachforderung durchsetzen möchte oder bereits Mahnung, Klage oder Rückzahlung im Raum stehen.

## Einstieg

1. Welche Seite: Mieter, Vermieter, Verwaltung, Anwalt?
2. Abrechnungsjahr, Datum der Abrechnung, tatsächlicher Zugang, Zahlungs-/Mahnlage?
3. Was wird angegriffen: Frist, Form, Kostenart, Schlüssel, Belege, Heizkosten, CO2, Vorauszahlungen?
4. Welche Unterlagen liegen vor: Mietvertrag, Abrechnung, Heizkosten, Rechnungen, Zahlungsbelege, Mieterzahlungen?
5. Gewünschter Output: Einwendung, Belegeinsicht, Rückforderung, Klageerwiderung, Klageentwurf, Vergleich?

## Rechtsanker

- § 556 Abs. 3 BGB: Abrechnung, Nachforderungsausschluss, Einwendungsfrist.
- § 556a BGB: Umlagemaßstab.
- § 259 BGB und § 242 BGB: Rechenschafts-/Belegeinsicht und Zurückbehaltung.
- BetrKV: laufende Betriebskosten und Kostenarten.
- HeizkostenV: Verbrauchserfassung und Kürzungsrecht.
- CO2KostAufG: Vermieter-/Mieteranteil.
- BGH, Urteil vom 09.04.2008 - VIII ZR 84/07: formelle Mindestangaben.
- BGH, Urteil vom 09.12.2020 - VIII ZR 118/19: Zahlungsbelege gehören zur Einsicht.
- BGH, Urteil vom 15.12.2021 - VIII ZR 66/20: Originalbelege als Grundsatz.

## Streitfall-Matrix

| Streitpunkt | Mieterlinie | Vermieterlinie | Beleg |
| --- | --- | --- | --- |
| verspäteter Zugang | Nachforderung ausgeschlossen | Zugang beweisen / Nichtvertretenmüssen | Zustellung/Bote |
| formelle Lücke | Nachforderung nicht fällig | Mindestangaben nachreichen? | Abrechnung |
| nicht umlagefähige Kosten | Position kürzen | BetrKV/Vertrag zeigen | Rechnung/Vertrag |
| fehlende Zahlungsbelege | Zurückbehaltung | Einsicht anbieten | Zahlungsnachweis |
| falscher Schlüssel | Korrekturbetrag | Vertrags-/Gesetzesschlüssel verteidigen | Rechenblatt |
| Heizkosten/CO2 | Kürzung/Korrektur | Daten nachliefern | Heizkosten/CO2 |

## Prozesslogik

1. Ist die Forderung überhaupt fällig?
2. Ist sie fristgerecht geltend gemacht?
3. Ist der Betrag materiell richtig?
4. Wurde Belegeinsicht ermöglicht?
5. Welche Zahlung ist sofort sinnvoll, welche nur unter Vorbehalt, welche gar nicht?
6. Bei Rückzahlungsklage: Zahlung, Vorbehalt, Fehler und Anspruchshöhe sauber darlegen.

## Output

- Fehler- und Betragsmatrix.
- Einwendungsschreiben mit Belegeinsicht.
- Vermieter-Korrektur-/Fälligstellungsschreiben.
- Rückzahlungs- oder Klageerwiderungsbaustein.
- Vergleichsvorschlag mit sauberer Bezifferung.

## Quellenregel

Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 2. `mr-kuendigungsschutz-praxis`

**Fokus:** Wohnraum-Kuendigungsschutz Praxis: ordentliche Kuendigung § 573 BGB nur bei berechtigtem Interesse, Eigenbedarf § 573 Abs. 2 Nr. 2 BGB, Kuendigung bei Pflichtverletzung, Zahlungsverzug. Sozialklausel § 574 BGB. Pruefraster.

# Mietrecht: Kuendigungsschutz

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietrecht: Kuendigungsschutz` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Mietrecht: Kuendigungsschutz
- **Spezialgegenstand:** Mietrecht: Kuendigungsschutz / mr kuendigungsschutz praxis. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `mr-modernisierung-und-rolling-rent-spezial`

**Fokus:** Spezialfall Modernisierungs-Umlage in der laufenden Mieterhoehung: Verhaeltnis § 559 BGB zur ortsueblichen Vergleichsmiete § 558 BGB, Kappungsgrenze, Haerteeinwand. Aktuelle Rechtsprechung BGH. Pruefraster.

# Mietrecht: Modernisierung-Rolling-Rent

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietrecht: Modernisierung-Rolling-Rent` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Mietrecht: Modernisierung-Rolling-Rent
- **Spezialgegenstand:** Mietrecht: Modernisierung-Rolling-Rent / mr modernisierung und rolling rent spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB, BGH.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
