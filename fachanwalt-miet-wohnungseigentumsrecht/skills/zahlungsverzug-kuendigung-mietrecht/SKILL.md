---
name: zahlungsverzug-kuendigung-mietrecht
description: "Zahlungsverzug Kuendigung Mietrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Zahlungsverzug Kuendigung Mietrecht

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Zahlungsverzug Kuendigung Mietrecht** im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-zahlungsverzug-kuendigung-schonfrist` | Zahlungsverzug, Kündigung und Schonfrist: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Rückstandshöhe, Fälligkeit, Tilgung, Schonfristzahlung, hilfsweise ordentliche Kündigung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `mietrecht-einfuehrung-vertragstypen` | Einfuehrung Vertragstypen Mietrecht: Wohnraum-, Gewerbe-, Pacht-, Untermiete, Staffel-, Index-, Zeitmiete. Pro Typ: Anwendungsbereich, Schutzvorschriften, Kuendigungsregime, typische Klauselrisiken. Entscheidungstabelle fuer Mandanten und Verweis auf passende Detail-Skills. |
| `spezial-haustiere-mietvertrag` | Haustiere im Mietverhältnis: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft AGB-Klausel, Interessenabwägung, Störung, Erlaubnis und Widerruf; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-kleinreparaturklausel` | Kleinreparaturklausel: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Gegenstandsbereich, Einzelobergrenze, Jahresobergrenze und Transparenz; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |
| `spezial-mietvertrag-agb-klauseln` | Mietvertrag AGB-Klauseln: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft typische Klauseln auf Transparenz, Überraschung und unangemessene Benachteiligung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt. |

## Arbeitsweg

Im Plugin Fachanwalt Miet- und Wohnungseigentumsrecht gilt für **Zahlungsverzug Kuendigung Mietrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-zahlungsverzug-kuendigung-schonfrist`

**Fokus:** Zahlungsverzug, Kündigung und Schonfrist: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Rückstandshöhe, Fälligkeit, Tilgung, Schonfristzahlung, hilfsweise ordentliche Kündigung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Zahlungsverzug, Kündigung und Schonfrist

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zahlungsverzug, Kündigung und Schonfrist` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Rückstandshöhe, Fälligkeit, Tilgung, Schonfristzahlung, hilfsweise ordentliche Kündigung.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 2. `mietrecht-einfuehrung-vertragstypen`

**Fokus:** Einfuehrung Vertragstypen Mietrecht: Wohnraum-, Gewerbe-, Pacht-, Untermiete, Staffel-, Index-, Zeitmiete. Pro Typ: Anwendungsbereich, Schutzvorschriften, Kuendigungsregime, typische Klauselrisiken. Entscheidungstabelle fuer Mandanten und Verweis auf passende Detail-Skills.

# Mietrecht: Vertragstypen

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietrecht: Vertragstypen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Mietrecht: Vertragstypen
- **Spezialgegenstand:** Mietrecht: Vertragstypen / mietrecht einfuehrung vertragstypen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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

## 3. `spezial-haustiere-mietvertrag`

**Fokus:** Haustiere im Mietverhältnis: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft AGB-Klausel, Interessenabwägung, Störung, Erlaubnis und Widerruf; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Haustiere im Mietverhältnis

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Haustiere im Mietverhältnis` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft AGB-Klausel, Interessenabwägung, Störung, Erlaubnis und Widerruf.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 4. `spezial-kleinreparaturklausel`

**Fokus:** Kleinreparaturklausel: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft Gegenstandsbereich, Einzelobergrenze, Jahresobergrenze und Transparenz; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Kleinreparaturklausel

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kleinreparaturklausel` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft Gegenstandsbereich, Einzelobergrenze, Jahresobergrenze und Transparenz.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.

## 5. `spezial-mietvertrag-agb-klauseln`

**Fokus:** Mietvertrag AGB-Klauseln: Fachmodul im Miet- und Wohnungseigentumsrecht; prüft typische Klauseln auf Transparenz, Überraschung und unangemessene Benachteiligung; mit Normprüfung, Beweisen, Fristen, Risikoampel und Arbeitsprodukt.

# Mietvertrag AGB-Klauseln

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietvertrag AGB-Klauseln` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe
Fachmodul im Plugin `fachanwalt-miet-wohnungseigentumsrecht`. Er bearbeitet: prüft typische Klauseln auf Transparenz, Überraschung und unangemessene Benachteiligung.

## Einstieg
1. Welche Seite wird vertreten und welches Ergebnis soll erreicht werden?
2. Welche Norm-/Vertrags-/Beschlussgrundlage ist wahrscheinlich einschlägig?
3. Welche Tatsachen sind unstreitig, welche streitig, welche fehlen?
4. Welche Frist, Form, Zuständigkeit oder Beweislast kann den Fall kippen?
5. Welche Unterlagen belegen den Kern: Vertrag, Nachtrag, Beschluss, Protokoll, Abrechnung, Fotos, Messungen, Kontoauszüge, Mails?

## Prüfraster
1. **Rechtsverhältnis abgrenzen:** Wohnraummiete, Gewerberaum, WEG, Verwaltung, Nachbar-/Ordnungsrecht oder Schnittstelle.
2. **Tatbestand:** Anspruchsgrundlage, Einwendung, Gegenrecht und Rechtsfolge sauber trennen.
3. **Form und Frist:** Zugang, Text-/Schriftform, Beschlussfristen, Abrechnungsfristen, Verjährung.
4. **Beweis:** Darlegungslast, Substantiierung, Beweisangebot, Sachverständigenbedarf.
5. **Taktik:** Sofortmaßnahme, Verhandlung, Vergleich, Klage/Eilantrag, Kostenrisiko.
6. **Ergebnis:** Ampel mit Begründung und konkretem nächsten Arbeitsschritt.

## Output
- Prüfvermerk mit Normen und Belegen.
- Lückenliste der fehlenden Tatsachen.
- Entwurf für Mandantenmail, Gegenseitenschreiben, Beschlussvorschlag oder Schriftsatzbaustein.
- Anschluss-Skills, wenn WEG/Miete/Betriebskosten/GEG/Prozessrecht tiefer laufen muss.

## Quellen- und Sicherheitsregel
- Vor tragenden Aussagen den aktuellen Normtext und die aktuelle Behörden-/Gerichtspraxis prüfen; keine Scheingenauigkeit aus Modellwissen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Annahmen, fehlende Unterlagen, Beweisrisiken und Fristen ausdrücklich markieren.
